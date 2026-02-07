from __future__ import annotations

import csv
import importlib.metadata
import json
from pathlib import Path
from typing import Any

from .types import FigureRecord, TableRecord


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def package_version(distribution: str) -> str | None:
    try:
        return importlib.metadata.version(distribution)
    except importlib.metadata.PackageNotFoundError:
        return None


def tool_versions() -> dict[str, str | None]:
    return {
        "pymupdf": package_version("pymupdf"),
        "pdfplumber": package_version("pdfplumber"),
        "camelot-py": package_version("camelot-py"),
        "pytesseract": package_version("pytesseract"),
    }


def write_table_csv_assets(tables: list[TableRecord], assets_dir: Path) -> None:
    assets_dir.mkdir(parents=True, exist_ok=True)
    for table in tables:
        file_name = f"{table.table_id}.csv"
        path = assets_dir / file_name
        with path.open("w", encoding="utf-8", newline="") as file_obj:
            writer = csv.writer(file_obj)
            writer.writerows(table.rows)
        table.csv_file = file_name


def check_figure_assets(figures: list[FigureRecord], assets_dir: Path) -> list[str]:
    missing = []
    for figure in figures:
        if not (assets_dir / figure.file_name).exists():
            missing.append(figure.file_name)
    return missing
