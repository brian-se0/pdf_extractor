from pathlib import Path

from pdf_pipeline.run_pipeline import _resolve_output_dir


def test_resolve_output_dir_defaults_to_input_extracted() -> None:
    input_dir = Path("/tmp/my_pdfs")
    assert _resolve_output_dir(input_dir, None) == Path("/tmp/my_pdfs/extracted")


def test_resolve_output_dir_keeps_explicit_output() -> None:
    input_dir = Path("/tmp/my_pdfs")
    output_dir = Path("/tmp/out")
    assert _resolve_output_dir(input_dir, output_dir) == output_dir
