from __future__ import annotations

import re
from typing import Any

from .types import FigureRecord, TableRecord, TextExtraction

TABLE_REF_RE = re.compile(r"\btable\s+\d+\b", re.IGNORECASE)
FIGURE_REF_RE = re.compile(r"\b(?:figure|fig\.)\s*\d+\b", re.IGNORECASE)
EQUATION_REF_RE = re.compile(r"\b(?:eq\.?|equation)\s*\(?\d+\)?", re.IGNORECASE)
GARBLED_MATH_RE = re.compile(r"\(cid:\d+\)|\ufffd")


def _count_equation_like_lines(full_text: str) -> int:
    count = 0
    for raw_line in full_text.splitlines():
        line = " ".join(raw_line.split())
        if len(line) < 3:
            continue

        operator_hits = sum(line.count(token) for token in ("=", "+", "-", "*", "/", "^"))
        symbol_hits = sum(line.count(token) for token in ("=", "<=", ">=", "~", "^", "_") )
        long_word_count = len(re.findall(r"[A-Za-z]{4,}", line))

        if "=" in line and operator_hits >= 1 and long_word_count <= 20:
            count += 1
            continue

        if symbol_hits >= 2 and operator_hits >= 2 and long_word_count <= 25:
            count += 1

    return count


def build_extraction_audit(
    text: TextExtraction,
    tables: list[TableRecord],
    figures: list[FigureRecord],
) -> dict[str, Any]:
    full_text = text.full_text or ""

    table_ref_count = len(TABLE_REF_RE.findall(full_text))
    figure_ref_count = len(FIGURE_REF_RE.findall(full_text))
    equation_ref_count = len(EQUATION_REF_RE.findall(full_text))
    equation_like_line_count = _count_equation_like_lines(full_text)
    garbled_math_token_count = len(GARBLED_MATH_RE.findall(full_text))

    issues: list[str] = []
    issue_details: dict[str, str] = {}

    if text.total_chars == 0:
        issues.append("missing_text")
        issue_details["missing_text"] = "No extractable text was produced."

    if table_ref_count > 0 and len(tables) == 0:
        issues.append("likely_missing_tables")
        issue_details["likely_missing_tables"] = (
            f"Detected {table_ref_count} table references, but extracted table count is 0."
        )
        issues.append("unresolved_table_extraction")
        issue_details["unresolved_table_extraction"] = (
            "Table references were detected but no structured table output was recovered."
        )

    if figure_ref_count > 0 and len(figures) == 0:
        issues.append("likely_missing_figures")
        issue_details["likely_missing_figures"] = (
            f"Detected {figure_ref_count} figure references, but extracted figure count is 0."
        )

    if equation_ref_count > 0 and equation_like_line_count == 0:
        issues.append("likely_missing_equations")
        issue_details["likely_missing_equations"] = (
            f"Detected {equation_ref_count} equation references, but no equation-like lines were detected."
        )

    if garbled_math_token_count >= 5:
        issues.append("possible_math_garbling")
        issue_details["possible_math_garbling"] = (
            f"Detected {garbled_math_token_count} potential math-garbling tokens (cid/replacement chars)."
        )

    return {
        "ok": len(issues) == 0,
        "issues": issues,
        "issue_details": issue_details,
        "metrics": {
            "chars": text.total_chars,
            "pages": len(text.pages),
            "table_reference_count": table_ref_count,
            "figure_reference_count": figure_ref_count,
            "equation_reference_count": equation_ref_count,
            "equation_like_line_count": equation_like_line_count,
            "garbled_math_token_count": garbled_math_token_count,
            "extracted_table_count": len(tables),
            "extracted_figure_count": len(figures),
            "low_text_page_ratio": text.low_text_page_ratio,
            "scan_like_page_ratio": text.scan_like_page_ratio,
        },
    }


def format_audit_log_line(source_file: str, audit: dict[str, Any]) -> str | None:
    issues = list(audit.get("issues", []))
    metrics = dict(audit.get("metrics", {}))
    if not issues:
        return None

    issue_label = ",".join(issues)
    return (
        f"[AUDIT] {source_file} | issues={issue_label} | "
        f"tables={metrics.get('extracted_table_count', 0)}/{metrics.get('table_reference_count', 0)} refs | "
        f"figures={metrics.get('extracted_figure_count', 0)}/{metrics.get('figure_reference_count', 0)} refs | "
        f"equations={metrics.get('equation_like_line_count', 0)}/{metrics.get('equation_reference_count', 0)} refs | "
        f"garbled_math_tokens={metrics.get('garbled_math_token_count', 0)} | "
        f"chars={metrics.get('chars', 0)}"
    )
