from pdf_pipeline.audit import build_extraction_audit, format_audit_log_line
from pdf_pipeline.types import TextExtraction


def test_audit_flags_missing_tables_when_references_present() -> None:
    text = TextExtraction(
        full_text="Table 1 reports summary statistics. Eq. (1) defines the model.",
        total_chars=80,
    )

    audit = build_extraction_audit(text=text, tables=[], figures=[])

    assert "likely_missing_tables" in audit["issues"]
    assert audit["metrics"]["table_reference_count"] >= 1


def test_audit_log_line_is_none_when_no_issues() -> None:
    text = TextExtraction(full_text="Plain text without references.", total_chars=30)
    audit = build_extraction_audit(text=text, tables=[], figures=[])

    assert audit["ok"] is True
    assert format_audit_log_line("paper.pdf", audit) is None


def test_audit_log_line_contains_issue_summary() -> None:
    text = TextExtraction(
        full_text="Figure 1 shows the result. Table 1 has values.",
        total_chars=60,
    )
    audit = build_extraction_audit(text=text, tables=[], figures=[])
    line = format_audit_log_line("paper.pdf", audit)

    assert line is not None
    assert line.startswith("[AUDIT] paper.pdf | issues=")
    assert "tables=0/" in line
    assert "figures=0/" in line
