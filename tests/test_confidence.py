from pdf_pipeline.confidence import compute_confidence
from pdf_pipeline.types import FallbackState, TextExtraction


def test_confidence_high_for_clean_primary_success() -> None:
    confidence = compute_confidence(
        status="success",
        fallback=FallbackState(used=False),
        extraction_audit={"issues": []},
        quality_checks=[],
        text=TextExtraction(total_chars=5000, low_text_page_ratio=0.0, scan_like_page_ratio=0.0),
        table_count=3,
        figure_count=2,
    )

    assert confidence["label"] == "high"
    assert confidence["score"] >= 0.85


def test_confidence_low_for_partial_missing_text() -> None:
    confidence = compute_confidence(
        status="partial",
        fallback=FallbackState(used=True, use_ocr=True),
        extraction_audit={"issues": ["missing_text"]},
        quality_checks=[{"check": "text_threshold", "status": "fail"}],
        text=TextExtraction(total_chars=0, low_text_page_ratio=1.0, scan_like_page_ratio=1.0),
        table_count=0,
        figure_count=0,
    )

    assert confidence["label"] == "low"
    assert confidence["score"] <= 0.5
