from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from .deps import MissingDependencyError, require_module
from .types import PageText, TableRecord

TABLE_MARKER_RE = re.compile(r"\btable\s+\d+\b", re.IGNORECASE)


def detect_table_marker_pages(pages: Iterable[PageText]) -> set[int]:
    markers: set[int] = set()
    for page in pages:
        if TABLE_MARKER_RE.search(page.text):
            markers.add(page.page_number)
    return markers


def _normalize_cell(value: object) -> str:
    if value is None:
        return ""
    text = str(value)
    text = " ".join(text.replace("\n", " ").split())
    return text.strip()


def _normalize_rows(raw_rows: list[list[object]] | None) -> list[list[str]]:
    if not raw_rows:
        return []
    cleaned = [[_normalize_cell(cell) for cell in row] for row in raw_rows if row is not None]
    cleaned = [row for row in cleaned if any(cell for cell in row)]
    return cleaned


def _is_usable_table(rows: list[list[str]]) -> bool:
    if len(rows) < 2:
        return False
    col_count = max((len(row) for row in rows), default=0)
    if col_count < 2:
        return False
    non_empty_cells = sum(1 for row in rows for cell in row if cell)
    return non_empty_cells >= 4


def _caption_candidates_from_page(page_text: str) -> list[str]:
    candidates = []
    for line in page_text.splitlines():
        compact = " ".join(line.split())
        if TABLE_MARKER_RE.match(compact):
            candidates.append(compact)
    return candidates


def _assign_captions(tables: list[TableRecord], page_lookup: dict[int, str]) -> None:
    used_caption_pages: dict[int, int] = {}
    for table in tables:
        captions = _caption_candidates_from_page(page_lookup.get(table.page_number, ""))
        if not captions:
            continue
        used = used_caption_pages.get(table.page_number, 0)
        if used < len(captions):
            table.caption = captions[used]
            used_caption_pages[table.page_number] = used + 1
        else:
            table.caption = captions[-1]


def extract_tables_pdfplumber(
    pdf_path: Path,
    page_text_lookup: dict[int, str],
) -> tuple[list[TableRecord], list[str], set[int]]:
    warnings: list[str] = []
    malformed_pages: set[int] = set()
    tables: list[TableRecord] = []

    pdfplumber = require_module("pdfplumber")

    with pdfplumber.open(str(pdf_path)) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            raw_tables = page.extract_tables() or []
            if not raw_tables:
                continue

            for table_idx, raw in enumerate(raw_tables, start=1):
                rows = _normalize_rows(raw)
                if not _is_usable_table(rows):
                    malformed_pages.add(page_number)
                    warnings.append(
                        f"pdfplumber unusable table on page {page_number} index {table_idx}"
                    )
                    continue

                table_id = f"table_{len(tables) + 1:03d}"
                tables.append(
                    TableRecord(
                        table_id=table_id,
                        page_number=page_number,
                        rows=rows,
                        source="pdfplumber",
                    )
                )

    _assign_captions(tables, page_text_lookup)
    return tables, warnings, malformed_pages


def extract_tables_camelot(
    pdf_path: Path,
    page_numbers: set[int],
    page_text_lookup: dict[int, str],
    start_index: int,
) -> tuple[list[TableRecord], list[str]]:
    warnings: list[str] = []
    records: list[TableRecord] = []

    if not page_numbers:
        return records, warnings

    try:
        camelot = require_module("camelot")
    except MissingDependencyError as exc:
        return records, [str(exc)]

    pages_spec = ",".join(str(page) for page in sorted(page_numbers))

    def _run(flavor: str):
        return camelot.read_pdf(str(pdf_path), pages=pages_spec, flavor=flavor)

    table_list = None
    errors: list[str] = []
    for flavor in ("lattice", "stream"):
        try:
            table_list = _run(flavor)
            if len(table_list) > 0:
                break
        except Exception as exc:  # noqa: BLE001
            errors.append(f"camelot {flavor} failed: {exc}")

    if table_list is None or len(table_list) == 0:
        warnings.extend(errors or ["camelot found no tables"])
        return records, warnings

    for offset, table in enumerate(table_list, start=1):
        try:
            page_number = int(table.page)
        except Exception:  # noqa: BLE001
            page_number = min(page_numbers)

        raw_rows = table.df.values.tolist()
        rows = _normalize_rows(raw_rows)
        if not _is_usable_table(rows):
            continue

        records.append(
            TableRecord(
                table_id=f"table_{start_index + offset:03d}",
                page_number=page_number,
                rows=rows,
                source="camelot",
            )
        )

    _assign_captions(records, page_text_lookup)
    warnings.extend(errors)
    return records, warnings
