from pdf_pipeline.audit import build_extraction_audit, format_audit_log_line
from pdf_pipeline.types import FigureRecord, TableRecord, TextExtraction


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


def test_audit_flags_likely_incomplete_tables() -> None:
    refs = " ".join(f"Table {idx}" for idx in range(1, 15))
    text = TextExtraction(full_text=refs, total_chars=len(refs))
    tables = [
        TableRecord(
            table_id=f"table_{idx:03d}",
            page_number=1,
            rows=[["A", "B"], ["1", "2"]],
        )
        for idx in range(1, 3)
    ]

    audit = build_extraction_audit(text=text, tables=tables, figures=[])

    assert "likely_incomplete_tables" in audit["issues"]


def test_audit_flags_figure_over_extraction() -> None:
    refs = " ".join(f"Figure {idx}" for idx in range(1, 13))
    text = TextExtraction(full_text=refs, total_chars=len(refs))
    figures = [
        FigureRecord(
            figure_id=f"figure_{idx:03d}",
            page_number=1,
            file_name=f"fig_{idx:03d}.png",
        )
        for idx in range(1, 30)
    ]

    audit = build_extraction_audit(text=text, tables=[], figures=figures)

    assert "possible_figure_over_extraction" in audit["issues"]


def test_audit_flags_likely_incomplete_figures() -> None:
    refs = " ".join(f"Figure {idx}" for idx in range(1, 18))
    text = TextExtraction(full_text=refs, total_chars=len(refs))
    figures = [
        FigureRecord(
            figure_id=f"figure_{idx:03d}",
            page_number=1,
            file_name=f"fig_{idx:03d}.png",
        )
        for idx in range(1, 5)
    ]

    audit = build_extraction_audit(text=text, tables=[], figures=figures)

    assert "likely_incomplete_figures" in audit["issues"]


def test_audit_uses_unique_numbered_references() -> None:
    text = TextExtraction(
        full_text=(
            "Table 1 is summarized below. Table 1 is discussed again. "
            "Table 2 provides robustness. "
            "Figure 3 is shown in panel A. Fig. 3 is discussed in detail. Figure 4 follows."
        ),
        total_chars=180,
    )
    tables = [
        TableRecord(table_id="table_001", page_number=1, rows=[["A", "B"], ["1", "2"]]),
        TableRecord(table_id="table_002", page_number=2, rows=[["A", "B"], ["3", "4"]]),
    ]
    figures = [
        FigureRecord(figure_id="figure_001", page_number=1, file_name="fig_001.png"),
        FigureRecord(figure_id="figure_002", page_number=2, file_name="fig_002.png"),
    ]

    audit = build_extraction_audit(text=text, tables=tables, figures=figures)

    assert audit["metrics"]["table_reference_count"] == 2
    assert audit["metrics"]["figure_reference_count"] == 2


def test_audit_equation_detection_handles_unicode_minus_and_control_chars() -> None:
    text = TextExtraction(
        full_text=(
            "As shown in Eq. (4), we use a HAR model.\n"
            "\x03yi \x02 \u03bc + \u03b2Dyt\u22121 + \u03b2W yt\u22125 + \u03b2M yt\u221222\n"
            "Equation (4) is estimated with OLS."
        ),
        total_chars=120,
    )

    audit = build_extraction_audit(text=text, tables=[], figures=[])

    assert "likely_missing_equations" not in audit["issues"]
    assert int(audit["metrics"]["equation_like_line_count"]) >= 1
