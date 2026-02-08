from __future__ import annotations

from typing import Any

from .types import FallbackState, TextExtraction

ISSUE_WEIGHTS = {
    "missing_text": 0.55,
    "likely_missing_tables": 0.2,
    "likely_incomplete_tables": 0.18,
    "unresolved_table_extraction": 0.15,
    "likely_missing_figures": 0.15,
    "likely_incomplete_figures": 0.12,
    "possible_figure_over_extraction": 0.1,
    "likely_missing_equations": 0.1,
    "possible_math_garbling": 0.1,
}


def _label(score: float) -> str:
    if score >= 0.85:
        return "high"
    if score >= 0.65:
        return "medium"
    return "low"


def compute_confidence(
    *,
    status: str,
    fallback: FallbackState,
    extraction_audit: dict[str, Any],
    quality_checks: list[dict[str, str]],
    text: TextExtraction,
    table_count: int,
    figure_count: int,
) -> dict[str, Any]:
    base = 0.95
    penalties: list[dict[str, Any]] = []
    bonuses: list[dict[str, Any]] = []

    if status == "partial":
        penalties.append({"reason": "status_partial", "weight": 0.25})
    elif status == "failed":
        penalties.append({"reason": "status_failed", "weight": 0.7})

    if fallback.used:
        penalties.append({"reason": "fallback_used", "weight": 0.08})
        if fallback.use_ocr:
            penalties.append({"reason": "ocr_fallback_used", "weight": 0.03})

    for issue in extraction_audit.get("issues", []):
        weight = ISSUE_WEIGHTS.get(issue, 0.08)
        penalties.append({"reason": f"audit:{issue}", "weight": weight})

    failed_checks = sum(1 for check in quality_checks if check.get("status") == "fail")
    if failed_checks:
        penalties.append({"reason": "quality_checks_failed", "weight": 0.07 * failed_checks})

    if text.low_text_page_ratio > 0.5:
        penalties.append(
            {
                "reason": "high_low_text_ratio",
                "weight": min(0.12, text.low_text_page_ratio * 0.2),
            }
        )
    if text.scan_like_page_ratio > 0.5 and not fallback.use_ocr:
        penalties.append({"reason": "scan_like_without_ocr", "weight": 0.15})

    if table_count == 0 and figure_count == 0 and text.total_chars < 1000:
        penalties.append({"reason": "very_sparse_content", "weight": 0.1})

    if not extraction_audit.get("issues"):
        bonuses.append({"reason": "audit_clean", "weight": 0.02})
    if status == "success" and not fallback.used:
        bonuses.append({"reason": "primary_path_success", "weight": 0.02})

    penalty_total = sum(item["weight"] for item in penalties)
    bonus_total = sum(item["weight"] for item in bonuses)

    score = max(0.01, min(0.99, base - penalty_total + bonus_total))
    score = round(score, 3)

    return {
        "score": score,
        "label": _label(score),
        "base": base,
        "penalties": penalties,
        "bonuses": bonuses,
    }
