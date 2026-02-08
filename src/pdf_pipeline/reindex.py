from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .dedup import (
    build_duplicate_flags,
    extract_first_page_excerpt,
    extract_main_text_from_markdown,
)
from .inventory import build_canonical_inventory
from .metadata import normalize_metadata
from .utils import write_json


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_markdown(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def _manifest_records(extracted_dir: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for item in sorted(extracted_dir.iterdir(), key=lambda p: p.name.lower()):
        if not item.is_dir():
            continue
        manifest_path = item / "manifest.json"
        if not manifest_path.exists():
            continue

        manifest = _read_json(manifest_path)
        markdown_text = _load_markdown(item / "paper.md")
        main_text = extract_main_text_from_markdown(markdown_text)
        first_page_excerpt = extract_first_page_excerpt(main_text)

        previous_metadata = dict(manifest.get("metadata") or {})
        previous_year = previous_metadata.get("year")
        updated_metadata = normalize_metadata(
            previous_metadata,
            text_hint=main_text,
            first_page_text=first_page_excerpt,
            source_file=str(manifest.get("source_file") or ""),
        )
        manifest["metadata"] = updated_metadata

        records.append(
            {
                "manifest_path": manifest_path,
                "manifest": manifest,
                "paper_id": manifest.get("paper_id"),
                "source_file": manifest.get("source_file"),
                "status": manifest.get("status"),
                "word_count": int((manifest.get("counts") or {}).get("words", 0) or 0),
                "table_count": int((manifest.get("counts") or {}).get("tables", 0) or 0),
                "figure_count": int((manifest.get("counts") or {}).get("figures", 0) or 0),
                "metadata": updated_metadata,
                "previous_year": previous_year,
            }
        )
    return records


def _apply_duplicate_flags(records: list[dict[str, Any]]) -> None:
    dedup_records = [
        {
            "paper_id": record["paper_id"],
            "source_file": record["source_file"],
            "status": record["status"],
            "word_count": record["word_count"],
            "table_count": record["table_count"],
            "figure_count": record["figure_count"],
            "metadata": record["metadata"],
        }
        for record in records
    ]
    flags = build_duplicate_flags(dedup_records)

    for record in records:
        paper_id = str(record.get("paper_id") or "")
        flag = flags.get(
            paper_id,
            {
                "is_duplicate": False,
                "duplicate_of": None,
                "duplicate_reason": None,
            },
        )
        record["is_duplicate"] = bool(flag["is_duplicate"])
        record["duplicate_of"] = flag["duplicate_of"]
        record["duplicate_reason"] = flag["duplicate_reason"]

        manifest = record["manifest"]
        manifest["is_duplicate"] = record["is_duplicate"]
        manifest["duplicate_of"] = record["duplicate_of"]
        manifest["duplicate_reason"] = record["duplicate_reason"]


def _write_manifests(records: list[dict[str, Any]]) -> None:
    for record in records:
        write_json(record["manifest_path"], record["manifest"])


def _update_batch_report(batch_report_path: Path, records: list[dict[str, Any]]) -> bool:
    if not batch_report_path.exists():
        return False

    batch_report = _read_json(batch_report_path)
    by_source = {str(record.get("source_file")): record for record in records}

    for result in batch_report.get("results", []):
        source_file = str(result.get("source_file"))
        record = by_source.get(source_file)
        if record is None:
            continue
        metadata = dict(record.get("metadata") or {})
        result["is_duplicate"] = bool(record.get("is_duplicate", False))
        result["duplicate_of"] = record.get("duplicate_of")
        result["duplicate_reason"] = record.get("duplicate_reason")
        result["publication_year"] = metadata.get("publication_year")
        result["year"] = metadata.get("year")
        result["doi"] = metadata.get("doi")

    canonical = build_canonical_inventory(
        [
            {
                "paper_id": record.get("paper_id"),
                "source_file": record.get("source_file"),
                "status": record.get("status"),
                "metadata": record.get("metadata"),
                "manifest": str(record.get("manifest_path")),
                "is_duplicate": bool(record.get("is_duplicate", False)),
                "duplicate_of": record.get("duplicate_of"),
                "duplicate_reason": record.get("duplicate_reason"),
            }
            for record in records
        ],
        exclude_duplicates=True,
        min_year=None,
    )
    batch_report["canonical_summary"] = {
        "exclude_duplicates": True,
        "total": canonical["total"],
        "success": canonical["success"],
        "partial": canonical["partial"],
        "failed": canonical["failed"],
        "duplicates_excluded": canonical["duplicates_excluded"],
    }

    write_json(batch_report_path, batch_report)
    return True


def reindex_extracted_directory(
    *,
    extracted_dir: Path,
    batch_report_path: Path | None = None,
    inventory_output_path: Path | None = None,
    min_year: int | None = None,
    include_duplicates: bool = False,
) -> dict[str, Any]:
    records = _manifest_records(extracted_dir)
    _apply_duplicate_flags(records)
    _write_manifests(records)

    inventory_records = [
        {
            "paper_id": record.get("paper_id"),
            "source_file": record.get("source_file"),
            "status": record.get("status"),
            "metadata": record.get("metadata"),
            "manifest": str(record.get("manifest_path")),
            "is_duplicate": bool(record.get("is_duplicate", False)),
            "duplicate_of": record.get("duplicate_of"),
            "duplicate_reason": record.get("duplicate_reason"),
        }
        for record in records
    ]
    inventory = build_canonical_inventory(
        inventory_records,
        exclude_duplicates=not include_duplicates,
        min_year=min_year,
    )
    if inventory_output_path is None:
        inventory_output_path = extracted_dir / "canonical_inventory.json"
    write_json(inventory_output_path, inventory)

    batch_report_updated = False
    if batch_report_path is not None:
        batch_report_updated = _update_batch_report(batch_report_path, records)

    year_changes = []
    for record in records:
        previous_year = record.get("previous_year")
        current_year = (record.get("metadata") or {}).get("year")
        if previous_year != current_year:
            year_changes.append(
                {
                    "paper_id": record.get("paper_id"),
                    "source_file": record.get("source_file"),
                    "before_year": previous_year,
                    "after_year": current_year,
                }
            )

    duplicates = [
        {
            "paper_id": record.get("paper_id"),
            "source_file": record.get("source_file"),
            "duplicate_of": record.get("duplicate_of"),
            "reason": record.get("duplicate_reason"),
        }
        for record in records
        if record.get("is_duplicate")
    ]

    return {
        "extracted_dir": str(extracted_dir),
        "manifests_processed": len(records),
        "year_changes": year_changes,
        "duplicates_marked": duplicates,
        "batch_report_updated": batch_report_updated,
        "inventory_path": str(inventory_output_path),
        "inventory_summary": {
            "total": inventory["total"],
            "success": inventory["success"],
            "partial": inventory["partial"],
            "failed": inventory["failed"],
            "duplicates_excluded": inventory["duplicates_excluded"],
            "year_threshold": inventory["year_threshold"],
        },
    }


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Backfill publication-year and duplicate metadata for extracted manifests",
    )
    parser.add_argument("--extracted-dir", type=Path, required=True)
    parser.add_argument("--batch-report", type=Path, default=None)
    parser.add_argument("--inventory-output", type=Path, default=None)
    parser.add_argument("--min-year", type=int, default=None)
    parser.add_argument(
        "--include-duplicates",
        action="store_true",
        help="Include duplicates in canonical inventory output",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    summary = reindex_extracted_directory(
        extracted_dir=args.extracted_dir,
        batch_report_path=args.batch_report,
        inventory_output_path=args.inventory_output,
        min_year=args.min_year,
        include_duplicates=args.include_duplicates,
    )
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
