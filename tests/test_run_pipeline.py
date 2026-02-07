from pathlib import Path

from pdf_pipeline.run_pipeline import _resolve_output_dir, _should_attempt_direct_ocr_image_fallback
from pdf_pipeline.types import PipelineConfig, TextExtraction


def test_resolve_output_dir_defaults_to_input_extracted() -> None:
    input_dir = Path("/tmp/my_pdfs")
    assert _resolve_output_dir(input_dir, None) == Path("/tmp/my_pdfs/extracted")


def test_resolve_output_dir_keeps_explicit_output() -> None:
    input_dir = Path("/tmp/my_pdfs")
    output_dir = Path("/tmp/out")
    assert _resolve_output_dir(input_dir, output_dir) == output_dir


def test_direct_ocr_triggered_by_high_scan_like_ratio() -> None:
    config = PipelineConfig(input_dir=Path("/in"), output_dir=Path("/out"))
    text = TextExtraction(total_chars=6000, low_text_page_ratio=0.2, scan_like_page_ratio=0.9)
    assert _should_attempt_direct_ocr_image_fallback(text, config) is True


def test_direct_ocr_triggered_by_high_low_text_ratio() -> None:
    config = PipelineConfig(input_dir=Path("/in"), output_dir=Path("/out"))
    text = TextExtraction(total_chars=6000, low_text_page_ratio=0.92, scan_like_page_ratio=0.2)
    assert _should_attempt_direct_ocr_image_fallback(text, config) is True


def test_direct_ocr_not_triggered_for_healthy_text() -> None:
    config = PipelineConfig(input_dir=Path("/in"), output_dir=Path("/out"))
    text = TextExtraction(total_chars=6000, low_text_page_ratio=0.2, scan_like_page_ratio=0.2)
    assert _should_attempt_direct_ocr_image_fallback(text, config) is False
