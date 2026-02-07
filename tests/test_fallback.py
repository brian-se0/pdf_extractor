from pathlib import Path

from pdf_pipeline.fallback import LOW_TEXT_YIELD, TABLE_MISMATCH, decide_fallback, fallback_log_line
from pdf_pipeline.types import PipelineConfig, TextExtraction


def test_low_text_triggers_ocr() -> None:
    config = PipelineConfig(input_dir=Path("/in"), output_dir=Path("/out"), ocr_mode="auto")
    text = TextExtraction(total_chars=100, low_text_page_ratio=1.0, scan_like_page_ratio=0.0)

    state = decide_fallback(
        config=config,
        text_result=text,
        table_count=0,
        table_marker_pages=set(),
        stage_errors={},
    )

    assert state.use_ocr is True
    assert LOW_TEXT_YIELD in state.reasons


def test_table_marker_triggers_camelot() -> None:
    config = PipelineConfig(input_dir=Path("/in"), output_dir=Path("/out"), ocr_mode="never")
    text = TextExtraction(total_chars=5000, low_text_page_ratio=0.0, scan_like_page_ratio=0.0)

    state = decide_fallback(
        config=config,
        text_result=text,
        table_count=0,
        table_marker_pages={3},
        stage_errors={},
    )

    assert state.use_camelot is True
    assert TABLE_MISMATCH in state.reasons


def test_fallback_line_format() -> None:
    config = PipelineConfig(input_dir=Path("/in"), output_dir=Path("/out"), ocr_mode="auto")
    text = TextExtraction(total_chars=0, low_text_page_ratio=1.0, scan_like_page_ratio=1.0)

    state = decide_fallback(
        config=config,
        text_result=text,
        table_count=0,
        table_marker_pages={1},
        stage_errors={"text": "boom"},
    )

    line = fallback_log_line("paper.pdf", state)
    assert line.startswith("[FALLBACK] paper.pdf | primary_failed_stage=text | fallback_used=")
    assert "reason=" in line
