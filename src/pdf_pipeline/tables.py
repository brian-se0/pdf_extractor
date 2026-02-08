from __future__ import annotations

import hashlib
import re
import warnings
from pathlib import Path
from typing import Iterable

from .deps import MissingDependencyError, require_module
from .types import PageText, TableRecord

TABLE_MARKER_RE = re.compile(r"\btable\s+\d+\b", re.IGNORECASE)
TABLE_MARKER_ID_RE = re.compile(r"\btable\s+(\d+)\b", re.IGNORECASE)
TABLE_CAPTION_LINE_RE = re.compile(r"^\s*table\s+\d+\b", re.IGNORECASE)
TABLE_CAPTION_LINE_ALT_RE = re.compile(r"^\s*tab\.?\s+\d+\b", re.IGNORECASE)
NUMERIC_TOKEN_RE = re.compile(r"^[()\[\]-]?\d[\d,]*(?:\.\d+)?%?$")
TABLE_NOISE_PATTERNS = (
    re.compile(r"\bjournal\b", re.IGNORECASE),
    re.compile(r"\bvol(?:ume)?\b", re.IGNORECASE),
    re.compile(r"\bdoi\b", re.IGNORECASE),
    re.compile(r"\bdownloaded from\b", re.IGNORECASE),
    re.compile(r"\ball use subject to\b", re.IGNORECASE),
    re.compile(r"\bcopyright\b", re.IGNORECASE),
    re.compile(r"\bpage\s+\d+\b", re.IGNORECASE),
)


def _line_has_table_caption(line: str) -> bool:
    compact = " ".join(line.split())
    if not compact:
        return False
    return bool(TABLE_CAPTION_LINE_RE.match(compact) or TABLE_CAPTION_LINE_ALT_RE.match(compact))


def _line_numeric_density(line: str) -> tuple[int, int]:
    tokens = [token for token in line.split() if token]
    numeric = sum(1 for token in tokens if _looks_numeric_token(token))
    return numeric, len(tokens)


def _table_expectation_score(page_text: str) -> float:
    lines = [" ".join(line.split()) for line in page_text.splitlines() if line.strip()]
    if not lines:
        return 0.0

    caption_line_indices = [idx for idx, line in enumerate(lines) if _line_has_table_caption(line)]
    inline_refs = len(TABLE_MARKER_RE.findall(page_text))
    numeric_lines = 0
    delimiter_lines = 0

    for line in lines:
        numeric_tokens, token_count = _line_numeric_density(line)
        if numeric_tokens >= 3 and token_count >= 4:
            numeric_lines += 1
        if line.count("|") >= 2 or "\t" in line:
            delimiter_lines += 1

    score = 0.0
    if caption_line_indices:
        score += 0.55
    score += min(numeric_lines, 4) * 0.10
    score += min(delimiter_lines, 3) * 0.06
    score += min(inline_refs, 3) * 0.05

    if caption_line_indices:
        near_caption_numeric = 0
        for caption_idx in caption_line_indices:
            start = max(0, caption_idx - 2)
            end = min(len(lines), caption_idx + 14)
            for line in lines[start:end]:
                numeric_tokens, token_count = _line_numeric_density(line)
                if numeric_tokens >= 3 and token_count >= 4:
                    near_caption_numeric += 1
            if near_caption_numeric >= 2:
                break
        if near_caption_numeric >= 2:
            score += 0.2

    if inline_refs >= 2 and numeric_lines >= 2:
        score += 0.12

    return min(score, 1.0)


def detect_table_marker_pages(pages: Iterable[PageText]) -> set[int]:
    markers: set[int] = set()
    for page in pages:
        score = _table_expectation_score(page.text)
        if score >= 0.72:
            markers.add(page.page_number)
    return markers


def count_table_references(pages: Iterable[PageText]) -> int:
    reference_ids: set[int] = set()
    for page in pages:
        for match in TABLE_MARKER_ID_RE.finditer(page.text):
            reference_ids.add(int(match.group(1)))
    return len(reference_ids)


def _read_pdf_camelot_safely(camelot_module: object, pdf_path: Path, **kwargs: object) -> object:
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message=r"No tables found in table area.*",
            category=UserWarning,
        )
        return camelot_module.read_pdf(str(pdf_path), **kwargs)


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


def _normalized_row_text(row: list[str]) -> str:
    return " ".join(" ".join(row).split()).strip().lower()


def _table_rows_digest(rows: list[list[str]]) -> str:
    normalized_rows: list[str] = []
    for row in rows:
        normalized_cells = [" ".join(cell.split()).strip().lower() for cell in row]
        normalized_rows.append("|".join(normalized_cells))
    payload = "\n".join(normalized_rows)
    return hashlib.sha1(payload.encode("utf-8")).hexdigest()[:16]


def _row_looks_like_noise(row: list[str]) -> bool:
    text = _normalized_row_text(row)
    if not text:
        return True

    if len(text) <= 3:
        return True

    if re.fullmatch(r"\d+", text):
        return True

    words = [token for token in re.split(r"\s+", text) if token]
    numeric_tokens = sum(1 for token in words if _looks_numeric_token(token))
    if len(words) >= 14 and numeric_tokens <= 1:
        return True

    return any(pattern.search(text) for pattern in TABLE_NOISE_PATTERNS)


def _table_quality_score(
    rows: list[list[str]],
    *,
    caption_confirmed: bool,
) -> tuple[float, list[str]]:
    row_count = len(rows)
    col_count = max((len(row) for row in rows), default=0)
    if row_count == 0 or col_count == 0:
        return 0.0, ["empty_table"]

    tokens = [
        token
        for row in rows
        for cell in row
        for token in re.split(r"\s+", cell.strip())
        if token
    ]
    token_count = len(tokens)
    numeric_tokens = sum(1 for token in tokens if _looks_numeric_token(token))
    numeric_ratio = numeric_tokens / token_count if token_count else 0.0

    noise_rows = sum(1 for row in rows if _row_looks_like_noise(row))
    noise_ratio = noise_rows / row_count if row_count else 0.0
    narrative_rows = 0
    for row in rows:
        text = _normalized_row_text(row)
        words = [token for token in re.split(r"\s+", text) if token]
        numeric_tokens = sum(1 for token in words if _looks_numeric_token(token))
        if len(words) >= 18 and numeric_tokens <= 1:
            narrative_rows += 1
    narrative_ratio = narrative_rows / row_count if row_count else 0.0

    unique_rows = len({_normalized_row_text(row) for row in rows})
    unique_ratio = unique_rows / row_count if row_count else 0.0

    score = 0.75
    flags: list[str] = []

    if caption_confirmed:
        score += 0.1
        flags.append("caption_confirmed")

    if col_count >= 3:
        score += 0.05
    elif col_count == 1 and not caption_confirmed:
        score -= 0.55
        flags.append("single_column_without_caption")
    elif col_count == 1 and caption_confirmed:
        flags.append("single_column_with_caption")

    if token_count < 8:
        score -= 0.25
        flags.append("very_low_token_count")
    elif token_count < 20:
        score -= 0.1
        flags.append("low_token_count")

    if noise_ratio >= 0.5:
        score -= 0.55
        flags.append("high_noise_rows")
    elif noise_ratio >= 0.25:
        score -= 0.3
        flags.append("medium_noise_rows")
    elif noise_ratio > 0.0:
        score -= 0.1
        flags.append("some_noise_rows")

    if narrative_ratio >= 0.3:
        score -= 0.45
        flags.append("high_narrative_rows")
    elif narrative_ratio > 0.0:
        score -= 0.15
        flags.append("some_narrative_rows")

    if unique_ratio < 0.55:
        score -= 0.25
        flags.append("low_row_diversity")

    if numeric_ratio < 0.02 and col_count >= 2:
        score -= 0.2
        flags.append("very_low_numeric_density")
    elif numeric_ratio < 0.06 and col_count >= 2:
        score -= 0.08
        flags.append("low_numeric_density")

    score = max(0.0, min(1.0, score))
    return score, flags


def _postprocess_tables(
    tables: list[TableRecord],
    page_text_lookup: dict[int, str],
    *,
    table_id_start: int,
    source_name: str,
    quality_threshold: float = 0.35,
) -> tuple[list[TableRecord], list[str]]:
    warnings: list[str] = []
    if not tables:
        return [], warnings

    pages = {table.page_number for table in tables}
    caption_pages = _caption_pages_from_text_lookup(page_text_lookup, pages)

    filtered: list[TableRecord] = []
    seen_digests: set[str] = set()
    dropped_low_quality = 0
    dropped_duplicates = 0

    for table in sorted(tables, key=lambda item: (item.page_number, item.table_id)):
        caption_confirmed = table.page_number in caption_pages
        score, flags = _table_quality_score(
            table.rows,
            caption_confirmed=caption_confirmed,
        )

        table.quality_score = score
        table.quality_flags = flags

        if score < quality_threshold:
            dropped_low_quality += 1
            continue

        digest = _table_rows_digest(table.rows)
        if digest in seen_digests:
            dropped_duplicates += 1
            continue

        seen_digests.add(digest)
        filtered.append(table)

    for idx, table in enumerate(filtered, start=table_id_start):
        table.table_id = f"table_{idx:03d}"

    if dropped_low_quality > 0:
        warnings.append(
            f"{source_name} table quality filter dropped {dropped_low_quality} low-quality table(s)"
        )
    if dropped_duplicates > 0:
        warnings.append(f"{source_name} table dedup removed {dropped_duplicates} duplicate table(s)")

    return filtered, warnings


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
        if TABLE_MARKER_RE.match(compact) or TABLE_CAPTION_LINE_ALT_RE.match(compact):
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
            if TABLE_CAPTION_LINE_RE.match(compact) or TABLE_CAPTION_LINE_ALT_RE.match(compact):
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

                tables.append(
                    TableRecord(
                        table_id="",
                        page_number=page_number,
                        rows=rows,
                        source="pdfplumber",
                    )
                )

    tables, post_warnings = _postprocess_tables(
        tables,
        page_text_lookup,
        table_id_start=1,
        source_name="pdfplumber",
    )
    warnings.extend(post_warnings)
    _assign_captions(tables, page_text_lookup)
    return tables, warnings, malformed_pages


def extract_tables_camelot(
    pdf_path: Path,
    page_numbers: set[int],
    page_text_lookup: dict[int, str],
    start_index: int,
    quality_threshold: float = 0.35,
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
                    region_tables = _read_pdf_camelot_safely(
                        camelot,
                        pdf_path,
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
                full_page_tables = _read_pdf_camelot_safely(
                    camelot,
                    pdf_path,
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

    for record in records:
        record.source = f"camelot:{best_flavor}"

    if best_flavor == "stream" and len(flavor_records["lattice"]) == 0 and len(
        flavor_records["stream"]
    ) > 0:
        warnings.append("camelot lattice produced no usable tables; using stream output")

    records, post_warnings = _postprocess_tables(
        records,
        page_text_lookup,
        table_id_start=start_index,
        source_name=f"camelot:{best_flavor}",
        quality_threshold=quality_threshold,
    )
    warnings.extend(post_warnings)
    _assign_captions(records, page_text_lookup)
    warnings.extend(errors)
    return records, warnings


def _parse_ocr_table_block(lines: list[str]) -> list[list[str]] | None:
    candidate_rows: list[list[str]] = []
    for line in lines:
        compact = " ".join(line.split())
        if not compact:
            continue

        tokens = [token.strip() for token in compact.split() if token.strip()]
        if len(tokens) < 3:
            continue

        numeric_tokens = sum(1 for token in tokens if _looks_numeric_token(token))
        if numeric_tokens >= 3 and len(tokens) >= 4:
            candidate_rows.append(tokens)

    if len(candidate_rows) < 2:
        return None

    col_count = max(len(row) for row in candidate_rows)
    if col_count < 3:
        return None

    first_numeric_tokens = sum(1 for token in candidate_rows[0] if _looks_numeric_token(token))
    first_row_is_header = first_numeric_tokens <= max(1, len(candidate_rows[0]) // 2)

    if first_row_is_header and len(candidate_rows) >= 3:
        header = candidate_rows[0]
        body = candidate_rows[1:]
    else:
        header = [f"col_{idx + 1}" for idx in range(col_count)]
        body = candidate_rows

    rows = [header] + body
    return rows


def extract_tables_from_ocr_text(
    pages: list[PageText],
    start_index: int,
) -> tuple[list[TableRecord], list[str]]:
    records: list[TableRecord] = []
    warnings: list[str] = []
    table_counter = start_index

    for page in pages:
        lines = [" ".join(line.split()) for line in page.text.splitlines()]
        line_count = len(lines)
        idx = 0

        while idx < line_count:
            line = lines[idx]
            if not (TABLE_CAPTION_LINE_RE.match(line) or TABLE_CAPTION_LINE_ALT_RE.match(line)):
                idx += 1
                continue

            caption = line
            block: list[str] = []
            cursor = idx + 1
            while cursor < line_count:
                next_line = lines[cursor]
                if TABLE_CAPTION_LINE_RE.match(next_line) or TABLE_CAPTION_LINE_ALT_RE.match(next_line):
                    break
                if next_line.startswith("## "):
                    break
                if next_line:
                    block.append(next_line)
                if len(block) >= 50:
                    break
                cursor += 1

            parsed_rows = _parse_ocr_table_block(block)
            if parsed_rows is not None:
                records.append(
                    TableRecord(
                        table_id=f"table_{table_counter:03d}",
                        page_number=page.page_number,
                        rows=parsed_rows,
                        caption=caption,
                        source="ocr-text",
                    )
                )
                table_counter += 1

            idx = cursor if cursor > idx else idx + 1

    if not records:
        warnings.append("OCR text table fallback found no recoverable structured tables")

    return records, warnings
