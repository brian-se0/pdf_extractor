from __future__ import annotations

import re
from pathlib import Path

from .types import FallbackState, FigureRecord


def run_quality_checks(
    output_dir: Path,
    markdown_path: Path,
    manifest_path: Path,
    markdown_text: str,
    total_chars: int,
    table_count_manifest: int,
    figure_count_manifest: int,
    figures: list[FigureRecord],
    fallback: FallbackState,
    scan_like: bool,
) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []

    def add(name: str, ok: bool, detail: str) -> None:
        checks.append(
            {
                "check": name,
                "status": "pass" if ok else "fail",
                "detail": detail,
            }
        )

    add("output_folder_exists", output_dir.exists(), str(output_dir))
    add("paper_md_exists", markdown_path.exists(), str(markdown_path))
    add("manifest_exists", manifest_path.exists(), str(manifest_path))

    threshold_ok = total_chars > 500 or scan_like
    add(
        "text_threshold",
        threshold_ok,
        f"chars={total_chars}, scan_like={scan_like}",
    )

    figure_refs = re.findall(r"!\[Figure", markdown_text)
    table_refs = re.findall(r"^### Table ", markdown_text, flags=re.MULTILINE)

    add(
        "figure_count_match",
        len(figure_refs) == figure_count_manifest,
        f"markdown={len(figure_refs)}, manifest={figure_count_manifest}",
    )
    add(
        "table_count_match",
        len(table_refs) == table_count_manifest,
        f"markdown={len(table_refs)}, manifest={table_count_manifest}",
    )

    missing_figures = [
        figure.file_name
        for figure in figures
        if not (output_dir / "assets" / figure.file_name).exists()
    ]
    add(
        "figure_assets_exist",
        len(missing_figures) == 0,
        ", ".join(missing_figures) if missing_figures else "all figure assets exist",
    )

    fallback_ok = (not fallback.used) or fallback.stdout_logged
    if not fallback.used:
        fallback_detail = "fallback not used"
    elif fallback.stdout_logged:
        fallback_detail = "fallback used and stdout logged"
    else:
        fallback_detail = "fallback used but stdout logging flag is false"

    add(
        "fallback_stdout_manifest_alignment",
        fallback_ok,
        fallback_detail,
    )

    return checks
