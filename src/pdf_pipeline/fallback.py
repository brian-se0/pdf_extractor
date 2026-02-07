from __future__ import annotations

from collections import OrderedDict

from .types import FallbackState, PipelineConfig, TextExtraction

PARSE_ERROR = "parse_error"
LOW_TEXT_YIELD = "low_text_yield"
SCAN_LIKE = "scan_like"
TABLE_MISMATCH = "table_expectation_mismatch"
FORCED_OCR = "forced_ocr"


def _dedupe(values: list[str]) -> list[str]:
    return list(OrderedDict((value, None) for value in values))


def decide_fallback(
    config: PipelineConfig,
    text_result: TextExtraction | None,
    table_count: int,
    table_marker_pages: set[int],
    stage_errors: dict[str, str],
) -> FallbackState:
    state = FallbackState()
    reasons: list[str] = []

    if stage_errors:
        primary_failed_stage = next(iter(stage_errors.keys()))
        state.primary_failed_stage = primary_failed_stage
        reasons.append(PARSE_ERROR)

        if primary_failed_stage in {"open", "metadata", "text"}:
            state.use_ocr = config.ocr_mode != "never"
        if primary_failed_stage in {"tables"}:
            state.use_camelot = True

    if text_result is not None:
        low_text = (
            text_result.total_chars < config.min_total_chars
            or text_result.low_text_page_ratio >= config.min_low_text_page_ratio
        )
        if low_text:
            reasons.append(LOW_TEXT_YIELD)
            state.use_ocr = config.ocr_mode != "never" or state.use_ocr

        scan_like = text_result.scan_like_page_ratio >= config.scan_like_page_ratio
        if scan_like:
            reasons.append(SCAN_LIKE)
            state.use_ocr = config.ocr_mode != "never" or state.use_ocr

    if table_marker_pages and table_count == 0:
        reasons.append(TABLE_MISMATCH)
        state.use_camelot = True

    if config.ocr_mode == "always":
        reasons.append(FORCED_OCR)
        state.use_ocr = True

    if config.ocr_mode == "never":
        state.use_ocr = False

    state.reasons = _dedupe(reasons)
    state.used = state.use_camelot or state.use_ocr
    return state


def fallback_log_line(source_file: str, state: FallbackState) -> str:
    reason_code = ",".join(state.reasons) if state.reasons else "unspecified"
    return (
        f"[FALLBACK] {source_file} | primary_failed_stage={state.primary_failed_stage} "
        f"| fallback_used={state.fallback_used_label} | reason={reason_code}"
    )
