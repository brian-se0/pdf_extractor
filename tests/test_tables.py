from pathlib import Path

import pdf_pipeline.tables as tables


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
                _FakeCamelotTable("1", [["h1", "h2"], ["a", "b"]]),
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
