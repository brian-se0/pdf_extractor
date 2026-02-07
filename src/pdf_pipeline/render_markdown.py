from __future__ import annotations

import html
import re
from datetime import datetime, timezone
from typing import Any

from .types import FigureRecord, TableRecord, TextExtraction


def _yaml_str(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value).replace("\x00", "").replace("\n", " ").strip()
    escaped = text.replace('"', '\\"')
    return f'"{escaped}"'


def _escape_md_cell(value: str) -> str:
    return value.replace("\x00", "").replace("|", "\\|").replace("\n", " ").strip()


def _table_to_markdown(rows: list[list[str]]) -> str | None:
    if not rows:
        return None

    max_cols = max((len(row) for row in rows), default=0)
    if max_cols < 2:
        return None

    normalized = [row + [""] * (max_cols - len(row)) for row in rows]

    if len(normalized) < 2:
        return None

    header = normalized[0]
    if all(not cell.strip() for cell in header):
        header = [f"col_{idx+1}" for idx in range(max_cols)]

    body = normalized[1:]

    header_line = "| " + " | ".join(_escape_md_cell(cell) for cell in header) + " |"
    separator_line = "| " + " | ".join("---" for _ in header) + " |"
    body_lines = [
        "| " + " | ".join(_escape_md_cell(cell) for cell in row) + " |"
        for row in body
    ]

    return "\n".join([header_line, separator_line, *body_lines])


def _table_to_html(rows: list[list[str]]) -> str:
    max_cols = max((len(row) for row in rows), default=0)
    normalized = [row + [""] * (max_cols - len(row)) for row in rows]
    parts = ["<table>"]

    for row_idx, row in enumerate(normalized):
        parts.append("  <tr>")
        tag = "th" if row_idx == 0 else "td"
        for cell in row:
            parts.append(f"    <{tag}>{html.escape(cell)}</{tag}>")
        parts.append("  </tr>")

    parts.append("</table>")
    return "\n".join(parts)


def _extract_abstract(full_text: str) -> str | None:
    sample = full_text[:8000]
    match = re.search(
        r"(?is)\babstract\b\s*[:\n]\s*(.+?)(?:\n\s*(?:\d+[.)]?\s+)?introduction\b)",
        sample,
    )
    if match:
        abstract = " ".join(match.group(1).split())
        if len(abstract) > 40:
            return abstract

    lines = [line.strip() for line in sample.splitlines() if line.strip()]
    if not lines:
        return None
    for idx, line in enumerate(lines[:25]):
        if line.lower() == "abstract" and idx + 1 < len(lines):
            candidate = " ".join(lines[idx + 1 : idx + 8])
            if len(candidate) > 40:
                return candidate
    return None


def render_markdown(
    paper_id: str,
    source_file: str,
    metadata: dict[str, Any],
    text: TextExtraction,
    tables: list[TableRecord],
    figures: list[FigureRecord],
    warnings: list[str],
    status: str,
) -> str:
    title = str(metadata.get("title") or source_file).replace("\x00", "")
    authors = [str(author).replace("\x00", "") for author in (metadata.get("authors") or [])]
    year = metadata.get("year")
    doi = str(metadata.get("doi")).replace("\x00", "") if metadata.get("doi") else None
    extracted_at = datetime.now(timezone.utc).isoformat()

    frontmatter_lines = [
        "---",
        f"paper_id: {_yaml_str(paper_id)}",
        f"source_file: {_yaml_str(source_file)}",
        f"title: {_yaml_str(title)}",
        f"authors: [{', '.join(_yaml_str(author) for author in authors)}]",
        f"year: {_yaml_str(year)}",
        f"doi: {_yaml_str(doi)}",
        f"page_count: {_yaml_str(len(text.pages))}",
        f"extracted_at: {_yaml_str(extracted_at)}",
        f"status: {_yaml_str(status)}",
        "---",
        "",
    ]

    lines = frontmatter_lines
    lines.append(f"# {title}")
    lines.append("")

    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- **Source File:** `{source_file}`")
    lines.append(f"- **Authors:** {', '.join(authors) if authors else 'Unknown'}")
    lines.append(f"- **Year:** {year if year is not None else 'Unknown'}")
    lines.append(f"- **DOI:** {doi if doi else 'Unknown'}")
    lines.append("")

    abstract = _extract_abstract(text.full_text)
    lines.append("## Abstract")
    lines.append("")
    lines.append(abstract if abstract else "Not found.")
    lines.append("")

    lines.append("## Main Text")
    lines.append("")
    lines.append(text.full_text if text.full_text else "No extractable text.")
    lines.append("")

    lines.append("## Tables")
    lines.append("")
    if tables:
        for index, table in enumerate(tables, start=1):
            lines.append(f"### Table {index}")
            lines.append("")
            if table.caption:
                lines.append(f"*Caption:* {table.caption}")
                lines.append("")
            table_md = _table_to_markdown(table.rows)
            if table_md is None:
                lines.append(_table_to_html(table.rows))
            else:
                lines.append(table_md)
            if table.csv_file:
                lines.append("")
                lines.append(f"Raw CSV: `assets/{table.csv_file}`")
            lines.append("")
    else:
        lines.append("No tables extracted.")
        lines.append("")

    lines.append("## Figures")
    lines.append("")
    if figures:
        for index, figure in enumerate(figures, start=1):
            caption = figure.caption or f"Figure {index}"
            lines.append(f"![Figure {index}: {caption}](assets/{figure.file_name})")
            lines.append("")
    else:
        lines.append("No figures extracted.")
        lines.append("")

    lines.append("## Extraction Notes")
    lines.append("")
    if warnings:
        for warning in warnings:
            lines.append(f"- {warning}")
    else:
        lines.append("- No warnings.")
    lines.append("")

    return "\n".join(lines).replace("\x00", "")
