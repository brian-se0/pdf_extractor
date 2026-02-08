from __future__ import annotations

import datetime as _dt
import re
from typing import Any

from .dedup import compute_first_page_text_hash

DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19\d{2}|20\d{2})\b")
YEAR_IN_DATE_RE = re.compile(r"(19\d{2}|20\d{2})")
VOLUME_PAREN_YEAR_RE = re.compile(r"\b\d{1,4}\s*\(\s*((?:19|20)\d{2})\s*\)\s*\d")
JOURNAL_COMMA_YEAR_RE = re.compile(r"\b((?:19|20)\d{2})\s*,\s*\d{1,4}\s*,\s*\d")
SEASON_YEAR_RE = re.compile(r"\b(?:spring|summer|autumn|fall|winter)\s+((?:19|20)\d{2})\b", re.IGNORECASE)
REFERENCE_SECTION_RE = re.compile(r"\n\s*(references|bibliography)\b", re.IGNORECASE)

YEAR_SOURCE_PRIORITY: dict[str, int] = {
    "doi_journal_citation_line": 10,
    "volume_issue_year": 20,
    "preprint_header": 25,
    "copyright_line": 30,
    "advance_access_or_published_online": 40,
    "received_or_accepted_dates": 50,
    "text_fallback": 90,
}


def _clean_text(value: str | None) -> str | None:
    if value is None:
        return None
    cleaned = " ".join(str(value).replace("\x00", " ").split())
    return cleaned or None


def _parse_authors(author_field: str | list[str] | None) -> list[str]:
    if author_field is None:
        return []
    if isinstance(author_field, list):
        cleaned = [_clean_text(str(item)) for item in author_field]
        return [item for item in cleaned if item]

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
            if y0 > page.rect.height * 0.55:
                continue
            candidates.append((max_size, -y0, text))

    if not candidates:
        return None

    candidates.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return _clean_text(candidates[0][2])


def _year_from_date_str(value: str | None) -> int | None:
    if not value:
        return None
    match = YEAR_IN_DATE_RE.search(value)
    if not match:
        return None
    year = int(match.group(1))
    this_year = _dt.datetime.now(tz=_dt.timezone.utc).year
    if 1900 <= year <= this_year + 1:
        return year
    return None


def _extract_first_pages_text(doc: Any, max_pages: int = 3) -> str:
    chunks = []
    for page_number in range(min(max_pages, doc.page_count)):
        page = doc.load_page(page_number)
        chunks.append(page.get_text("text"))
    return "\n".join(chunks)


def _normalize_doi(value: str | None) -> str | None:
    cleaned = _clean_text(value)
    if not cleaned:
        return None
    lowered = cleaned.lower()
    prefixes = (
        "https://doi.org/",
        "http://doi.org/",
        "doi:",
    )
    for prefix in prefixes:
        if lowered.startswith(prefix):
            cleaned = cleaned[len(prefix):]
            lowered = cleaned.lower()
            break
    match = DOI_RE.search(cleaned)
    if not match:
        return None
    return match.group(0).lower().rstrip(".,;")


def _extract_doi(text: str | None) -> str | None:
    if not text:
        return None
    for match in DOI_RE.finditer(text):
        doi = _normalize_doi(match.group(0))
        if doi:
            return doi
    return None


def _metadata_text_slice(text: str | None, *, max_chars: int = 25000) -> str:
    if not text:
        return ""
    snippet = text[:max_chars]
    marker = REFERENCE_SECTION_RE.search(snippet)
    if marker:
        snippet = snippet[: marker.start()]
    return snippet


def _extract_years(value: str) -> list[int]:
    this_year = _dt.datetime.now(tz=_dt.timezone.utc).year
    out: list[int] = []
    for match in YEAR_RE.findall(value):
        year = int(match)
        if 1900 <= year <= this_year + 1:
            out.append(year)
    return out


def _year_from_arxiv_identifier(value: str | None) -> int | None:
    if not value:
        return None
    this_year = _dt.datetime.now(tz=_dt.timezone.utc).year
    match = re.search(r"(?<!\d)(\d{2})(\d{2})\.\d{4,5}(?:v\d+)?", value)
    if not match:
        return None
    year = 2000 + int(match.group(1))
    if 1900 <= year <= this_year + 1:
        return year
    return None


def _clean_lines(text: str) -> list[str]:
    lines: list[str] = []
    for line in text.splitlines():
        cleaned = _clean_text(line)
        if cleaned:
            lines.append(cleaned)
    return lines


def _append_candidate(
    candidates: list[dict[str, Any]],
    seen: set[tuple[int, str]],
    *,
    year: int,
    source: str,
    evidence: str,
) -> None:
    key = (year, source)
    if key in seen:
        return
    seen.add(key)
    candidates.append(
        {
            "year": year,
            "source": source,
            "evidence": evidence[:300],
        }
    )


def _collect_text_year_candidates(text: str, doi: str | None) -> list[dict[str, Any]]:
    lines = _clean_lines(text)
    if not lines:
        return []

    candidates: list[dict[str, Any]] = []
    seen: set[tuple[int, str]] = set()

    for idx, line in enumerate(lines):
        lowered = line.lower()
        context_window = lines[max(0, idx - 1) : min(len(lines), idx + 2)]
        context = " ".join(context_window)

        has_doi_signal = bool(re.search(r"\bdoi\b", lowered)) or "doi.org" in lowered
        if doi and doi in lowered:
            has_doi_signal = True
        if has_doi_signal:
            years = _extract_years(line)
            for year in years:
                _append_candidate(
                    candidates,
                    seen,
                    year=year,
                    source="doi_journal_citation_line",
                    evidence=line,
                )

        for match in VOLUME_PAREN_YEAR_RE.findall(line):
            _append_candidate(
                candidates,
                seen,
                year=int(match),
                source="volume_issue_year",
                evidence=line,
            )
        for match in JOURNAL_COMMA_YEAR_RE.findall(line):
            _append_candidate(
                candidates,
                seen,
                year=int(match),
                source="volume_issue_year",
                evidence=line,
            )
        for match in SEASON_YEAR_RE.findall(line):
            _append_candidate(
                candidates,
                seen,
                year=int(match),
                source="volume_issue_year",
                evidence=line,
            )

        if any(
            token in lowered
            for token in ("copyright", "©", "(c)", "the author", "all rights reserved", "published by")
        ):
            for year in _extract_years(line):
                _append_candidate(
                    candidates,
                    seen,
                    year=year,
                    source="copyright_line",
                    evidence=line,
                )

        if any(
            token in lowered
            for token in ("advance access", "published online", "publication date", "online first", "first published")
        ):
            for year in _extract_years(context):
                _append_candidate(
                    candidates,
                    seen,
                    year=year,
                    source="advance_access_or_published_online",
                    evidence=context,
                )

        if any(
            token in lowered
            for token in ("received", "accepted", "editorial decision", "revised", "submission", "submitted")
        ):
            for year in _extract_years(context):
                _append_candidate(
                    candidates,
                    seen,
                    year=year,
                    source="received_or_accepted_dates",
                    evidence=context,
                )

        if "arxiv:" in lowered:
            for year in _extract_years(line):
                _append_candidate(
                    candidates,
                    seen,
                    year=year,
                    source="preprint_header",
                    evidence=line,
                )

    head_years: list[int] = []
    for line in lines[:120]:
        head_years.extend(_extract_years(line))
    if head_years:
        _append_candidate(
            candidates,
            seen,
            year=max(head_years),
            source="text_fallback",
            evidence=lines[0],
        )

    return candidates


def _resolve_publication_year(
    *,
    text: str,
    doi: str | None,
    raw_pdf_metadata: dict[str, Any],
    extra_candidates: list[dict[str, Any]] | None = None,
) -> tuple[int | None, list[dict[str, Any]], str, int | None]:
    raw_pdf_year = _year_from_date_str(_clean_text(raw_pdf_metadata.get("creationDate")))
    if raw_pdf_year is None:
        raw_pdf_year = _year_from_date_str(_clean_text(raw_pdf_metadata.get("modDate")))

    candidates = _collect_text_year_candidates(text=text, doi=doi)
    if extra_candidates:
        candidates.extend(extra_candidates)
    if raw_pdf_year is not None:
        candidates.append(
            {
                "year": raw_pdf_year,
                "source": "raw_pdf_metadata",
                "evidence": "creationDate/modDate",
            }
        )

    publication_candidates = [
        candidate
        for candidate in candidates
        if candidate["source"] in YEAR_SOURCE_PRIORITY
    ]
    if not publication_candidates:
        reason = "no_reliable_text_year_found"
        if raw_pdf_year is not None:
            reason = "no_reliable_text_year_found(raw_pdf_year_ignored)"
        return None, candidates, reason, raw_pdf_year

    publication_candidates.sort(
        key=lambda candidate: (
            YEAR_SOURCE_PRIORITY[candidate["source"]],
            -int(candidate["year"]),
        )
    )
    chosen = publication_candidates[0]
    reason = f"{chosen['source']}:{chosen['year']}"
    return int(chosen["year"]), candidates, reason, raw_pdf_year


def normalize_metadata(
    metadata: dict[str, Any] | None,
    *,
    text_hint: str | None = None,
    first_page_text: str | None = None,
    source_file: str | None = None,
) -> dict[str, Any]:
    normalized = dict(metadata or {})
    raw_pdf_metadata = normalized.get("raw_pdf_metadata")
    if not isinstance(raw_pdf_metadata, dict):
        raw_pdf_metadata = {}
    cleaned_raw_pdf_metadata = {
        str(key): _clean_text(value)
        for key, value in raw_pdf_metadata.items()
    }
    normalized["raw_pdf_metadata"] = cleaned_raw_pdf_metadata

    normalized["title"] = _clean_text(normalized.get("title"))
    normalized["authors"] = _parse_authors(normalized.get("authors"))

    text_for_metadata = _metadata_text_slice(text_hint)
    title_text = _clean_text(normalized.get("title"))
    if title_text:
        text_for_metadata = "\n".join(part for part in (title_text, text_for_metadata) if part)

    extra_candidates: list[dict[str, Any]] = []
    source_preprint_year = _year_from_arxiv_identifier(source_file)
    if source_preprint_year is not None:
        extra_candidates.append(
            {
                "year": source_preprint_year,
                "source": "preprint_header",
                "evidence": str(source_file),
            }
        )

    doi = _normalize_doi(normalized.get("doi"))
    if doi is None and text_for_metadata:
        doi = _extract_doi(text_for_metadata[:6000])
    normalized["doi"] = doi

    publication_year, raw_candidates, reason, raw_pdf_year = _resolve_publication_year(
        text=text_for_metadata,
        doi=doi,
        raw_pdf_metadata=cleaned_raw_pdf_metadata,
        extra_candidates=extra_candidates,
    )
    normalized["publication_year"] = publication_year
    normalized["raw_year_candidates"] = raw_candidates
    normalized["year_resolution_reason"] = reason
    normalized["raw_pdf_year"] = raw_pdf_year
    normalized["year"] = publication_year

    if first_page_text:
        first_page_hash = compute_first_page_text_hash(first_page_text)
        if first_page_hash:
            normalized["first_page_text_hash"] = first_page_hash

    return normalized


def extract_metadata(doc: Any, text_hint: str | None = None) -> dict[str, Any]:
    raw = dict(doc.metadata or {})

    embedded_title = _clean_text(raw.get("title"))
    title = embedded_title or _title_from_first_page(doc)
    authors = _parse_authors(raw.get("author"))

    first_pages_text = _extract_first_pages_text(doc, max_pages=3)
    merged_text = "\n".join(part for part in (first_pages_text, text_hint) if part)
    doi = _extract_doi(merged_text)

    first_page_text = None
    if doc.page_count > 0:
        first_page_text = doc.load_page(0).get_text("text")

    return normalize_metadata(
        {
            "title": title,
            "authors": authors,
            "doi": doi,
            "raw_pdf_metadata": {k: _clean_text(v) for k, v in raw.items()},
        },
        text_hint=merged_text,
        first_page_text=first_page_text,
    )
