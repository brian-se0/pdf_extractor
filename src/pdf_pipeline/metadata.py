from __future__ import annotations

import re
from typing import Any

DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19\d{2}|20\d{2})\b")


def _clean_text(value: str | None) -> str | None:
    if not value:
        return None
    cleaned = " ".join(value.replace("\x00", " ").split())
    return cleaned or None


def _parse_authors(author_field: str | None) -> list[str]:
    text = _clean_text(author_field)
    if not text:
        return []
    if ";" in text:
        parts = [part.strip() for part in text.split(";")]
    elif " and " in text.lower():
        parts = [part.strip() for part in re.split(r"\band\b", text, flags=re.IGNORECASE)]
    else:
        parts = [text]
    return [part for part in parts if part]


def _title_from_first_page(doc: Any) -> str | None:
    if doc.page_count == 0:
        return None

    page = doc.load_page(0)
    data = page.get_text("dict")
    candidates: list[tuple[float, float, str]] = []

    for block in data.get("blocks", []):
        if block.get("type") != 0:
            continue
        for line in block.get("lines", []):
            spans = line.get("spans", [])
            if not spans:
                continue
            text = "".join(span.get("text", "") for span in spans).strip()
            if len(text) < 8:
                continue
            max_size = max(float(span.get("size", 0.0)) for span in spans)
            y0 = float(line.get("bbox", [0.0, 0.0, 0.0, 0.0])[1])
            if y0 > page.rect.height * 0.5:
                continue
            candidates.append((max_size, -y0, text))

    if not candidates:
        return None

    candidates.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return _clean_text(candidates[0][2])


def _year_from_date_str(value: str | None) -> int | None:
    if not value:
        return None
    match = YEAR_RE.search(value)
    if not match:
        return None
    year = int(match.group(1))
    if 1900 <= year <= 2100:
        return year
    return None


def _extract_first_pages_text(doc: Any, max_pages: int = 2) -> str:
    chunks = []
    for page_number in range(min(max_pages, doc.page_count)):
        page = doc.load_page(page_number)
        chunks.append(page.get_text("text"))
    return "\n".join(chunks)


def extract_metadata(doc: Any) -> dict[str, Any]:
    raw = dict(doc.metadata or {})

    embedded_title = _clean_text(raw.get("title"))
    title = embedded_title or _title_from_first_page(doc)

    authors = _parse_authors(raw.get("author"))

    first_pages_text = _extract_first_pages_text(doc, max_pages=3)
    doi_match = DOI_RE.search(first_pages_text)
    doi = doi_match.group(0) if doi_match else None

    year = _year_from_date_str(raw.get("creationDate"))
    if year is None:
        year = _year_from_date_str(raw.get("modDate"))
    if year is None:
        text_match = YEAR_RE.search(first_pages_text)
        if text_match:
            year = int(text_match.group(1))

    return {
        "title": title,
        "authors": authors,
        "year": year,
        "doi": doi,
        "raw_pdf_metadata": {k: _clean_text(v) for k, v in raw.items()},
    }
