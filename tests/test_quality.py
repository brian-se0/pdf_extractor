from pathlib import Path

from pdf_pipeline.quality import run_quality_checks
from pdf_pipeline.render_markdown import render_markdown
from pdf_pipeline.types import FallbackState, TextExtraction


def test_quality_check_fallback_detail_when_not_used(tmp_path: Path) -> None:
    output_dir = tmp_path / "paper"
    output_dir.mkdir(parents=True)
    markdown_path = output_dir / "paper.md"
    markdown_path.write_text("# test", encoding="utf-8")
    manifest_path = output_dir / "manifest.json"
    manifest_path.write_text("{}", encoding="utf-8")

    checks = run_quality_checks(
        output_dir=output_dir,
        markdown_path=markdown_path,
        manifest_path=manifest_path,
        markdown_text="# test",
        total_chars=600,
        table_count_manifest=0,
        figure_count_manifest=0,
        figures=[],
        fallback=FallbackState(used=False, stdout_logged=False),
        scan_like=False,
    )

    fallback_check = next(
        check for check in checks if check["check"] == "fallback_stdout_manifest_alignment"
    )
    assert fallback_check["status"] == "pass"
    assert fallback_check["detail"] == "fallback not used"


def test_render_markdown_strips_null_bytes() -> None:
    markdown = render_markdown(
        paper_id="paper\x00id",
        source_file="file.pdf",
        metadata={"title": "Title\x00", "authors": ["A\x00uthor"], "year": 2024, "doi": None},
        text=TextExtraction(full_text="line1\x00\nline2", total_chars=10),
        tables=[],
        figures=[],
        warnings=[],
        status="success",
    )

    assert "\x00" not in markdown
