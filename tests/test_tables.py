from pathlib import Path
import warnings

import pdf_pipeline.tables as tables
from pdf_pipeline.types import PageText, TableRecord


class _FakeValues:
    def __init__(self, rows: list[list[object]]) -> None:
        self._rows = rows

    def tolist(self) -> list[list[object]]:
        return self._rows


class _FakeDF:
    def __init__(self, rows: list[list[object]]) -> None:
        self.values = _FakeValues(rows)


class _FakeCamelotTable:
    def __init__(self, page: str, rows: list[list[object]]) -> None:
        self.page = page
        self.df = _FakeDF(rows)


class _FakeCamelot:
    def __init__(self, by_flavor: dict[str, list[_FakeCamelotTable]]) -> None:
        self.by_flavor = by_flavor

    def read_pdf(self, *_args, **kwargs):  # noqa: ANN002
        flavor = kwargs["flavor"]
        return self.by_flavor.get(flavor, [])


def test_extract_tables_camelot_prefers_usable_stream_when_lattice_unusable(monkeypatch) -> None:
    fake = _FakeCamelot(
        {
            "lattice": [
                _FakeCamelotTable("1", [["single-col"], ["value"]]),
            ],
            "stream": [
                _FakeCamelotTable(
                    "1",
                    [["Metric", "Value"], ["A", "10.2"], ["B", "11.4"]],
                ),
            ],
        }
    )
    monkeypatch.setattr(tables, "require_module", lambda *_args, **_kwargs: fake)

    records, warnings = tables.extract_tables_camelot(
        pdf_path=Path("/tmp/example.pdf"),
        page_numbers={1},
        page_text_lookup={1: "Table 1. Example"},
        start_index=1,
    )

    assert len(records) == 1
    assert records[0].source == "camelot:stream"
    assert records[0].table_id == "table_001"
    assert records[0].caption is not None
    assert any("lattice produced no usable tables" in warning for warning in warnings)


def test_extract_tables_camelot_warns_when_no_usable_tables(monkeypatch) -> None:
    fake = _FakeCamelot(
        {
            "lattice": [
                _FakeCamelotTable("1", [["only-one-col"], ["x"]]),
            ],
            "stream": [
                _FakeCamelotTable("1", [["header"], ["y"]]),
            ],
        }
    )
    monkeypatch.setattr(tables, "require_module", lambda *_args, **_kwargs: fake)

    records, warnings = tables.extract_tables_camelot(
        pdf_path=Path("/tmp/example.pdf"),
        page_numbers={1},
        page_text_lookup={1: "Table 1. Example"},
        start_index=1,
    )

    assert records == []
    assert any("none were usable" in warning for warning in warnings)


def test_single_column_caption_confirmed_numeric_rows_are_usable() -> None:
    rows = [
        ["Table 1  Value  StdErr"],
        ["A  10.2  0.4"],
        ["B  11.5  0.5"],
    ]
    assert tables._is_usable_table(rows, caption_confirmed=True) is True


def test_single_column_without_caption_is_not_usable() -> None:
    rows = [
        ["A 10.2 0.4"],
        ["B 11.5 0.5"],
        ["C 9.8 0.3"],
    ]
    assert tables._is_usable_table(rows, caption_confirmed=False) is False


def test_postprocess_tables_drops_noise_and_duplicates() -> None:
    good_rows = [
        ["Metric", "Value"],
        ["A", "10.1"],
        ["B", "11.2"],
    ]
    noise_rows = [
        ["Journal of Something 2026 Vol 1"],
        ["Downloaded from provider"],
        ["All use subject to terms"],
    ]

    records = [
        TableRecord(table_id="", page_number=2, rows=good_rows, source="camelot:stream"),
        TableRecord(table_id="", page_number=2, rows=good_rows, source="camelot:stream"),
        TableRecord(table_id="", page_number=3, rows=noise_rows, source="camelot:stream"),
    ]

    filtered, warnings = tables._postprocess_tables(
        records,
        page_text_lookup={2: "Table 1. Results", 3: "Table 2. Notes"},
        table_id_start=1,
        source_name="camelot:stream",
    )

    assert len(filtered) == 1
    assert filtered[0].table_id == "table_001"
    assert filtered[0].quality_score >= 0.35
    assert any("dedup removed" in warning for warning in warnings)
    assert any("quality filter dropped" in warning for warning in warnings)


def test_extract_tables_from_ocr_text_recovers_numeric_rows() -> None:
    page = PageText(
        page_number=3,
        text=(
            "Some context line\n"
            "Table 1. Empirical Size\n"
            "T p a b c\n"
            "8 0 9.85 12.14 14.10\n"
            "16 0 9.83 12.97 14.85\n"
            "32 0 9.88 12.68 14.34\n"
        ),
        char_count=120,
        image_area_ratio=1.0,
        scan_like=False,
    )

    records, warnings = tables.extract_tables_from_ocr_text([page], start_index=1)

    assert len(records) == 1
    assert records[0].source == "ocr-text"
    assert records[0].caption is not None
    assert len(records[0].rows) >= 3
    assert warnings == []


def test_detect_table_marker_pages_ignores_inline_reference_only() -> None:
    pages = [
        PageText(
            page_number=1,
            text="As shown in Table 1, results improve for model B.",
            char_count=52,
            image_area_ratio=0.0,
            scan_like=False,
        )
    ]

    markers = tables.detect_table_marker_pages(pages)
    assert markers == set()


def test_detect_table_marker_pages_flags_caption_with_numeric_block() -> None:
    pages = [
        PageText(
            page_number=2,
            text=(
                "Table 2. Simulation Results\n"
                "T p alpha beta gamma\n"
                "8 0 9.85 12.14 14.10\n"
                "16 0 9.83 12.97 14.85\n"
                "32 0 9.88 12.68 14.34\n"
            ),
            char_count=140,
            image_area_ratio=0.0,
            scan_like=False,
        )
    ]

    markers = tables.detect_table_marker_pages(pages)
    assert markers == {2}


def test_count_table_references_uses_unique_ids() -> None:
    pages = [
        PageText(
            page_number=1,
            text="Table 1 reports values. Table 1 appears again. Table 2 is in appendix.",
            char_count=80,
            image_area_ratio=0.0,
            scan_like=False,
        ),
        PageText(
            page_number=2,
            text="Further discussion of Table 2 and Table 1.",
            char_count=45,
            image_area_ratio=0.0,
            scan_like=False,
        ),
    ]

    assert tables.count_table_references(pages) == 2


class _WarningCamelot:
    def read_pdf(self, *_args, **_kwargs):  # noqa: ANN002
        warnings.warn("No tables found in table area (0, 0, 10, 10)", UserWarning, stacklevel=1)
        return []


def test_extract_tables_camelot_suppresses_no_table_area_warning(monkeypatch) -> None:
    monkeypatch.setattr(tables, "require_module", lambda *_args, **_kwargs: _WarningCamelot())

    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        records, warnings_out = tables.extract_tables_camelot(
            pdf_path=Path("/tmp/example.pdf"),
            page_numbers={1},
            page_text_lookup={1: "Table 1. Example"},
            start_index=1,
        )

    assert records == []
    assert any("camelot found no tables" in warning for warning in warnings_out)
    assert not any("No tables found in table area" in str(item.message) for item in caught)
