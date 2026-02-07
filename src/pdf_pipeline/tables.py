from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable

from .deps import MissingDependencyError, require_module
from .types import PageText, TableRecord

TABLE_MARKER_RE = re.compile(r"\btable\s+\d+\b", re.IGNORECASE)
TABLE_CAPTION_LINE_RE = re.compile(r"^\s*table\s+\d+\b", re.IGNORECASE)
NUMERIC_TOKEN_RE = re.compile(r"^[()\[\]-]?\d[\d,]*(?:\.\d+)?%?$")


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


def _looks_numeric_token(token: str) -> bool:
    compact = token.strip().replace("$", "").replace("€", "")
    return bool(NUMERIC_TOKEN_RE.match(compact))


def _is_usable_table(rows: list[list[str]], *, caption_confirmed: bool = False) -> bool:
    if len(rows) < 2:
        return False
    col_count = max((len(row) for row in rows), default=0)
    if col_count < 1:
        return False

    if col_count == 1:
        if not caption_confirmed:
            return False

        tokenized = []
        for row in rows:
            cell = row[0] if row else ""
            tokens = [token for token in re.split(r"\s+", cell.strip()) if token]
            if tokens:
                tokenized.append(tokens)

        if len(tokenized) < 3:
            return False

        multi_token_rows = sum(1 for tokens in tokenized if len(tokens) >= 3)
        total_tokens = sum(len(tokens) for tokens in tokenized)
        numeric_tokens = sum(
            1 for tokens in tokenized for token in tokens if _looks_numeric_token(token)
        )
        return multi_token_rows >= 2 and total_tokens >= 8 and numeric_tokens >= 3

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


def _caption_pages_from_text_lookup(
    page_text_lookup: dict[int, str],
    page_numbers: set[int],
) -> set[int]:
    caption_pages: set[int] = set()
    for page_number in page_numbers:
        page_text = page_text_lookup.get(page_number, "")
        for line in page_text.splitlines():
            compact = " ".join(line.split())
            if TABLE_CAPTION_LINE_RE.match(compact):
                caption_pages.add(page_number)
                break
    return caption_pages


def _to_camelot_area(
    left: float,
    top: float,
    right: float,
    bottom: float,
    page_height: float,
) -> str:
    pdf_top = max(0.0, min(page_height, page_height - top))
    pdf_bottom = max(0.0, min(page_height, page_height - bottom))
    if pdf_bottom > pdf_top:
        pdf_top, pdf_bottom = pdf_bottom, pdf_top
    return f"{left:.2f},{pdf_top:.2f},{right:.2f},{pdf_bottom:.2f}"


def _caption_regions_from_pdf(
    pdf_path: Path,
    caption_pages: set[int],
) -> dict[int, list[str]]:
    if not caption_pages:
        return {}

    try:
        fitz = require_module("fitz", install_name="pymupdf")
    except MissingDependencyError:
        return {}

    regions: dict[int, list[str]] = {}

    try:
        doc = fitz.open(str(pdf_path))
    except Exception:  # noqa: BLE001
        return {}

    for page_number in sorted(caption_pages):
        if page_number < 1 or page_number > doc.page_count:
            continue
        page = doc.load_page(page_number - 1)
        width = float(page.rect.width)
        height = float(page.rect.height)
        margin = max(width * 0.05, 10.0)

        page_regions: list[str] = []
        for block in page.get_text("blocks") or []:
            if len(block) < 5:
                continue
            x0, y0, x1, y1, text = block[0], block[1], block[2], block[3], block[4]
            compact = " ".join(str(text or "").split())
            if not TABLE_CAPTION_LINE_RE.match(compact):
                continue

            left = max(0.0, margin)
            right = max(left + 20.0, width - margin)

            below_top = min(height - 2.0, float(y1) + 2.0)
            below_bottom = min(height - 2.0, float(y1) + height * 0.55)
            if below_bottom - below_top >= 20.0:
                page_regions.append(
                    _to_camelot_area(left, below_top, right, below_bottom, height)
                )

            above_top = max(2.0, float(y0) - height * 0.45)
            above_bottom = max(2.0, float(y0) - 2.0)
            if above_bottom - above_top >= 20.0:
                page_regions.append(
                    _to_camelot_area(left, above_top, right, above_bottom, height)
                )

        if page_regions:
            deduped: list[str] = []
            seen: set[str] = set()
            for area in page_regions:
                if area in seen:
                    continue
                seen.add(area)
                deduped.append(area)
            regions[page_number] = deduped[:4]

    doc.close()
    return regions


def extract_tables_pdfplumber(
    pdf_path: Path,
    page_text_lookup: dict[int, str],
) -> tuple[list[TableRecord], list[str], set[int]]:
    warnings: list[str] = []
    malformed_pages: set[int] = set()
    tables: list[TableRecord] = []

    pdfplumber = require_module("pdfplumber")

    with pdfplumber.open(str(pdf_path)) as pdf:
        all_pages = set(range(1, len(pdf.pages) + 1))
        caption_pages = _caption_pages_from_text_lookup(page_text_lookup, all_pages)

        for page_number, page in enumerate(pdf.pages, start=1):
            raw_tables = page.extract_tables() or []
            if not raw_tables:
                continue

            for table_idx, raw in enumerate(raw_tables, start=1):
                rows = _normalize_rows(raw)
                if not _is_usable_table(
                    rows,
                    caption_confirmed=page_number in caption_pages,
                ):
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

    if not page_numbers:
        return [], warnings

    try:
        camelot = require_module("camelot")
    except MissingDependencyError as exc:
        return [], [str(exc)]

    caption_pages = _caption_pages_from_text_lookup(page_text_lookup, page_numbers)
    caption_regions = _caption_regions_from_pdf(pdf_path, caption_pages)

    flavor_records: dict[str, list[TableRecord]] = {"lattice": [], "stream": []}
    raw_counts: dict[str, int] = {"lattice": 0, "stream": 0}
    errors: list[str] = []
    flavor_seen_signatures: dict[str, set[tuple[int, tuple[str, ...], int, int]]] = {
        "lattice": set(),
        "stream": set(),
    }

    for flavor in ("lattice", "stream"):
        table_list = []

        caption_pages_with_regions = {
            page for page in caption_pages if page in caption_regions and caption_regions[page]
        }
        non_caption_or_no_region_pages = sorted(page_numbers - caption_pages_with_regions)

        for page_number in sorted(caption_pages_with_regions):
            for area in caption_regions[page_number]:
                try:
                    region_tables = camelot.read_pdf(
                        str(pdf_path),
                        pages=str(page_number),
                        flavor=flavor,
                        table_areas=[area],
                    )
                    table_list.extend(region_tables)
                except Exception as exc:  # noqa: BLE001
                    errors.append(
                        f"camelot {flavor} failed on page {page_number} region {area}: {exc}"
                    )

        if non_caption_or_no_region_pages:
            try:
                page_spec = ",".join(str(page) for page in non_caption_or_no_region_pages)
                full_page_tables = camelot.read_pdf(
                    str(pdf_path),
                    pages=page_spec,
                    flavor=flavor,
                )
                table_list.extend(full_page_tables)
            except Exception as exc:  # noqa: BLE001
                errors.append(f"camelot {flavor} failed: {exc}")

        raw_counts[flavor] = len(table_list)

        for table in table_list:
            try:
                page_number = int(table.page)
            except Exception:  # noqa: BLE001
                page_number = min(page_numbers)

            raw_rows = table.df.values.tolist()
            rows = _normalize_rows(raw_rows)
            if not _is_usable_table(
                rows,
                caption_confirmed=page_number in caption_pages,
            ):
                continue

            cols = max((len(row) for row in rows), default=0)
            signature = (page_number, tuple(rows[0]) if rows else tuple(), len(rows), cols)
            if signature in flavor_seen_signatures[flavor]:
                continue
            flavor_seen_signatures[flavor].add(signature)

            flavor_records[flavor].append(
                TableRecord(
                    table_id="",
                    page_number=page_number,
                    rows=rows,
                    source="camelot",
                )
            )

    if raw_counts["lattice"] == 0 and raw_counts["stream"] == 0:
        warnings.extend(errors or ["camelot found no tables"])
        return [], warnings

    best_flavor = max(
        ("lattice", "stream"),
        key=lambda flavor: (len(flavor_records[flavor]), 1 if flavor == "lattice" else 0),
    )
    records = flavor_records[best_flavor]

    if not records:
        warnings.append(
            "camelot found raw tables, but none were usable "
            f"(lattice_raw={raw_counts['lattice']}, stream_raw={raw_counts['stream']})"
        )
        warnings.extend(errors)
        return [], warnings

    for idx, record in enumerate(records, start=start_index):
        record.table_id = f"table_{idx:03d}"
        record.source = f"camelot:{best_flavor}"

    other = "stream" if best_flavor == "lattice" else "lattice"
    if best_flavor == "stream" and len(flavor_records["lattice"]) == 0 and len(
        flavor_records["stream"]
    ) > 0:
        warnings.append("camelot lattice produced no usable tables; using stream output")

    _assign_captions(records, page_text_lookup)
    warnings.extend(errors)
    return records, warnings
