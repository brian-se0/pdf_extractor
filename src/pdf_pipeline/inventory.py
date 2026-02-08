from __future__ import annotations

import datetime as _dt
from typing import Any


def _coerce_year(value: Any) -> int | None:
    if isinstance(value, int):
        return value
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return None


def _metadata_year(metadata: dict[str, Any]) -> int | None:
    publication_year = _coerce_year(metadata.get("publication_year"))
    if publication_year is not None:
        return publication_year
    return _coerce_year(metadata.get("year"))


def build_canonical_inventory(
    records: list[dict[str, Any]],
    *,
    exclude_duplicates: bool = True,
    min_year: int | None = None,
) -> dict[str, Any]:
    prepared: list[dict[str, Any]] = []
    duplicates_excluded = 0
    year_excluded = 0

    for record in records:
        metadata = dict(record.get("metadata") or {})
        is_duplicate = bool(record.get("is_duplicate", False))
        if exclude_duplicates and is_duplicate:
            duplicates_excluded += 1
            continue

        year = _metadata_year(metadata)
        if min_year is not None and (year is None or year < min_year):
            year_excluded += 1
            continue

        prepared.append(
            {
                "paper_id": record.get("paper_id"),
                "source_file": record.get("source_file"),
                "status": record.get("status"),
                "year": year,
                "doi": metadata.get("doi"),
                "manifest": record.get("manifest"),
                "is_duplicate": is_duplicate,
                "duplicate_of": record.get("duplicate_of"),
                "duplicate_reason": record.get("duplicate_reason"),
            }
        )

    prepared.sort(key=lambda item: str(item.get("source_file", "")).lower())

    unknown_year = sum(1 for item in prepared if item.get("year") is None)
    year_2020_plus = sum(1 for item in prepared if isinstance(item.get("year"), int) and item["year"] >= 2020)

    inventory = {
        "generated_at": _dt.datetime.now(tz=_dt.timezone.utc).isoformat(),
        "exclude_duplicates": exclude_duplicates,
        "year_threshold": min_year,
        "total": len(prepared),
        "success": sum(1 for item in prepared if item.get("status") == "success"),
        "partial": sum(1 for item in prepared if item.get("status") == "partial"),
        "failed": sum(1 for item in prepared if item.get("status") == "failed"),
        "duplicates_excluded": duplicates_excluded,
        "excluded_by_year_filter": year_excluded,
        "unknown_year_count": unknown_year,
        "year_2020_plus_count": year_2020_plus,
        "papers": prepared,
    }
    return inventory

