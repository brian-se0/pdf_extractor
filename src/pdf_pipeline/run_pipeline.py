from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import os
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from .audit import build_extraction_audit, format_audit_log_line
from .discover import build_jobs, discover_pdfs
from .extract import run_extraction_pass
from .fallback import fallback_log_line, decide_fallback
from .ocr import run_ocrmypdf
from .quality import run_quality_checks
from .render_markdown import render_markdown
from .tables import extract_tables_camelot
from .types import (
    PaperJob,
    PaperProcessingResult,
    PipelineConfig,
    TableRecord,
    TextExtraction,
)
from .utils import tool_versions, write_json, write_table_csv_assets


def _word_count(text: str) -> int:
    return len(text.split())


def _merge_metadata(primary: dict[str, Any], fallback: dict[str, Any]) -> dict[str, Any]:
    merged = dict(primary)
    for key, value in fallback.items():
        if key not in merged or merged[key] in (None, "", [], {}):
            merged[key] = value
    return merged


def _table_signature(table: TableRecord) -> tuple[int, tuple[str, ...]]:
    head = tuple(table.rows[0]) if table.rows else tuple()
    return table.page_number, head


def _merge_tables(primary_tables: list[TableRecord], fallback_tables: list[TableRecord]) -> list[TableRecord]:
    merged = list(primary_tables)
    seen = {_table_signature(table) for table in merged}

    for table in fallback_tables:
        signature = _table_signature(table)
        if signature in seen:
            continue
        seen.add(signature)
        merged.append(table)

    for idx, table in enumerate(merged, start=1):
        table.table_id = f"table_{idx:03d}"
    return merged


def _select_camelot_pages(
    page_count: int,
    marker_pages: set[int],
    malformed_pages: set[int],
    table_count: int,
) -> set[int]:
    pages = set(malformed_pages)
    if marker_pages and table_count == 0:
        pages |= marker_pages
    if not pages and table_count == 0:
        pages = set(range(1, page_count + 1))
    return pages


def _should_replace_text(primary: TextExtraction, candidate: TextExtraction) -> bool:
    return candidate.total_chars > primary.total_chars


def _process_one(job: PaperJob, config: PipelineConfig) -> PaperProcessingResult:
    started = time.time()
    output_dir = config.output_dir / job.paper_id
    assets_dir = output_dir / "assets"
    markdown_path = output_dir / "paper.md"
    manifest_path = output_dir / "manifest.json"
    output_dir.mkdir(parents=True, exist_ok=True)
    assets_dir.mkdir(parents=True, exist_ok=True)

    warnings: list[str] = []
    errors: list[str] = []

    primary = run_extraction_pass(
        pdf_path=job.source_path,
        assets_dir=assets_dir,
        config=config,
        include_figures=True,
    )

    warnings.extend(primary.warnings)
    for stage, message in primary.stage_errors.items():
        errors.append(f"{stage}: {message}")

    metadata = primary.metadata
    text_result = primary.text
    tables = list(primary.tables)
    figures = list(primary.figures)
    page_count = primary.page_count

    fallback = decide_fallback(
        config=config,
        text_result=text_result,
        table_count=len(tables),
        table_marker_pages=primary.table_marker_pages,
        stage_errors=primary.stage_errors,
    )

    if fallback.use_camelot:
        table_count_before_camelot = len(tables)
        pages = _select_camelot_pages(
            page_count=page_count,
            marker_pages=primary.table_marker_pages,
            malformed_pages=primary.malformed_table_pages,
            table_count=len(tables),
        )

        camelot_tables, camelot_warnings = extract_tables_camelot(
            pdf_path=job.source_path,
            page_numbers=pages,
            page_text_lookup={page.page_number: page.text for page in text_result.pages},
            start_index=len(tables) + 1,
        )
        warnings.extend(camelot_warnings)
        if camelot_tables:
            tables = _merge_tables(tables, camelot_tables)
        table_count_after_camelot = len(tables)
        if table_count_after_camelot <= table_count_before_camelot:
            message = (
                f"[FALLBACK] {job.source_path.name} | "
                "fallback attempted but no additional tables recovered "
                f"| primary_tables={table_count_before_camelot} "
                f"| final_tables={table_count_after_camelot}"
            )
            print(message, flush=True)
            warnings.append(message)

    ocr_pdf_path = output_dir / "_ocr.pdf"
    if fallback.use_ocr:
        ocr_ok, ocr_error = run_ocrmypdf(
            input_pdf=job.source_path,
            output_pdf=ocr_pdf_path,
            force_ocr=config.ocr_mode == "always",
        )
        if not ocr_ok:
            warnings.append(f"OCR fallback failed: {ocr_error}")
        else:
            ocr_pass = run_extraction_pass(
                pdf_path=ocr_pdf_path,
                assets_dir=assets_dir,
                config=config,
                include_figures=False,
            )
            warnings.extend([f"ocr: {warning}" for warning in ocr_pass.warnings])
            if ocr_pass.stage_errors:
                for stage, message in ocr_pass.stage_errors.items():
                    warnings.append(f"ocr {stage}: {message}")

            metadata = _merge_metadata(metadata, ocr_pass.metadata)
            if _should_replace_text(text_result, ocr_pass.text):
                text_result = ocr_pass.text

            if ocr_pass.tables:
                tables = _merge_tables(tables, ocr_pass.tables)

            page_count = max(page_count, ocr_pass.page_count)

    if fallback.used:
        print(fallback_log_line(job.source_path.name, fallback), flush=True)
        fallback.stdout_logged = True

    write_table_csv_assets(tables, assets_dir)

    status = "success"
    if errors and text_result.total_chars == 0 and not tables and not figures:
        status = "failed"
    elif errors:
        status = "partial"

    markdown = render_markdown(
        paper_id=job.paper_id,
        source_file=job.source_path.name,
        metadata=metadata,
        text=text_result,
        tables=tables,
        figures=figures,
        warnings=warnings + errors,
        status=status,
    )
    markdown_path.write_text(markdown, encoding="utf-8")

    manifest = {
        "paper_id": job.paper_id,
        "source_file": job.source_path.name,
        "source_path": str(job.source_path),
        "status": status,
        "page_count": page_count,
        "counts": {
            "words": _word_count(text_result.full_text),
            "tables": len(tables),
            "figures": len(figures),
            "chars": text_result.total_chars,
        },
        "metadata": metadata,
        "warnings": warnings,
        "errors": errors,
        "fallback": {
            "used": fallback.used,
            "primary_failed_stage": fallback.primary_failed_stage,
            "fallback_used": fallback.fallback_used_label,
            "reasons": fallback.reasons,
            "camelot_used": fallback.use_camelot,
            "ocr_used": fallback.use_ocr,
            "stdout_logged": fallback.stdout_logged,
        },
        "scan_like_page_ratio": text_result.scan_like_page_ratio,
        "low_text_page_ratio": text_result.low_text_page_ratio,
        "runtime_seconds": round(time.time() - started, 3),
        "tool_versions": tool_versions(),
    }

    extraction_audit = build_extraction_audit(
        text=text_result,
        tables=tables,
        figures=figures,
    )
    manifest["extraction_audit"] = extraction_audit

    audit_line = format_audit_log_line(job.source_path.name, extraction_audit)
    if audit_line:
        print(audit_line, flush=True)
        warnings.append(audit_line)
        manifest["warnings"] = warnings

    # Persist once before quality checks so manifest existence checks are meaningful.
    write_json(manifest_path, manifest)

    quality_checks = run_quality_checks(
        output_dir=output_dir,
        markdown_path=markdown_path,
        manifest_path=manifest_path,
        markdown_text=markdown,
        total_chars=text_result.total_chars,
        table_count_manifest=len(tables),
        figure_count_manifest=len(figures),
        figures=figures,
        fallback=fallback,
        scan_like=text_result.scan_like_page_ratio >= config.scan_like_page_ratio,
    )
    manifest["quality_checks"] = quality_checks

    if any(check["status"] == "fail" for check in quality_checks) and status == "success":
        status = "partial"
        manifest["status"] = status

    write_json(manifest_path, manifest)

    if ocr_pdf_path.exists():
        try:
            ocr_pdf_path.unlink()
        except OSError:
            warnings.append(f"Could not remove temporary OCR file: {ocr_pdf_path}")

    return PaperProcessingResult(
        paper_id=job.paper_id,
        source_file=job.source_path.name,
        source_path=str(job.source_path),
        output_dir=str(output_dir),
        status=status,
        warnings=warnings,
        errors=errors,
        metadata=metadata,
        page_count=page_count,
        word_count=_word_count(text_result.full_text),
        table_count=len(tables),
        figure_count=len(figures),
        fallback=fallback,
        runtime_seconds=round(time.time() - started, 3),
        manifest_path=str(manifest_path),
        markdown_path=str(markdown_path),
        quality_checks=quality_checks,
        extraction_audit=extraction_audit,
        extraction_issues=list(extraction_audit.get("issues", [])),
    )


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Extract PDFs into markdown with assets")
    parser.add_argument("--input", type=Path, required=True, help="Input PDF folder")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output folder (default: <input>/extracted)",
    )
    parser.add_argument("--workers", type=int, default=max(os.cpu_count() or 1, 1))
    parser.add_argument(
        "--ocr",
        choices=["auto", "always", "never"],
        default="auto",
        help="OCR policy",
    )
    return parser.parse_args(argv)


def _resolve_output_dir(input_dir: Path, output_dir: Path | None) -> Path:
    if output_dir is None:
        return input_dir / "extracted"
    return output_dir


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    config = PipelineConfig(
        input_dir=args.input,
        output_dir=_resolve_output_dir(args.input, args.output),
        workers=max(args.workers, 1),
        ocr_mode=args.ocr,
    )

    pdf_paths = discover_pdfs(config.input_dir)
    jobs = build_jobs(pdf_paths)

    config.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Discovered {len(jobs)} PDF file(s) to process.", flush=True)
    if not jobs:
        batch_report = {
            "status": "empty",
            "input": str(config.input_dir),
            "output": str(config.output_dir),
            "total": 0,
            "results": [],
        }
        write_json(config.output_dir / "batch_report.json", batch_report)
        return 0

    results: list[PaperProcessingResult] = []
    workers = min(config.workers, len(jobs))

    if workers == 1:
        for job in jobs:
            result = _process_one(job, config)
            results.append(result)
            print(f"[DONE] {result.source_file} -> {result.status}", flush=True)
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            future_map = {
                executor.submit(_process_one, job, config): job
                for job in jobs
            }
            for future in as_completed(future_map):
                job = future_map[future]
                try:
                    result = future.result()
                except Exception as exc:  # noqa: BLE001
                    failed_output = str(config.output_dir / job.paper_id)
                    errors = [str(exc)]
                    result = PaperProcessingResult(
                        paper_id=job.paper_id,
                        source_file=job.source_path.name,
                        source_path=str(job.source_path),
                        output_dir=failed_output,
                        status="failed",
                        errors=errors,
                    )
                results.append(result)
                print(f"[DONE] {result.source_file} -> {result.status}", flush=True)

    results.sort(key=lambda item: item.source_file.lower())

    fallback_results = [item for item in results if item.fallback.used]
    issue_to_files: dict[str, list[str]] = defaultdict(list)
    issue_counter: Counter[str] = Counter()
    for item in results:
        for issue in item.extraction_issues:
            issue_counter[issue] += 1
            issue_to_files[issue].append(item.source_file)
    print(f"Fallback used for {len(fallback_results)} PDF(s):", flush=True)
    for item in fallback_results:
        reason = ",".join(item.fallback.reasons) if item.fallback.reasons else "unspecified"
        print(
            f"- {item.source_file} -> {item.fallback.fallback_used_label} ({reason})",
            flush=True,
        )

    papers_with_issues = sum(1 for item in results if item.extraction_issues)
    print(f"Extraction audit flagged {papers_with_issues} PDF(s) with potential gaps.", flush=True)
    for issue, count in issue_counter.most_common():
        print(f"- {issue}: {count}", flush=True)

    batch_report = {
        "input": str(config.input_dir),
        "output": str(config.output_dir),
        "ocr_mode": config.ocr_mode,
        "workers": workers,
        "total": len(results),
        "success": sum(1 for item in results if item.status == "success"),
        "partial": sum(1 for item in results if item.status == "partial"),
        "failed": sum(1 for item in results if item.status == "failed"),
        "fallback_used": len(fallback_results),
        "extraction_audit": {
            "papers_with_issues": papers_with_issues,
            "issue_counts": dict(issue_counter),
            "issue_files": {issue: sorted(files) for issue, files in issue_to_files.items()},
        },
        "results": [
            {
                "paper_id": item.paper_id,
                "source_file": item.source_file,
                "status": item.status,
                "output_dir": item.output_dir,
                "manifest": item.manifest_path,
                "paper_md": item.markdown_path,
                "table_count": item.table_count,
                "figure_count": item.figure_count,
                "word_count": item.word_count,
                "fallback": {
                    "used": item.fallback.used,
                    "fallback_used": item.fallback.fallback_used_label,
                    "reasons": item.fallback.reasons,
                    "primary_failed_stage": item.fallback.primary_failed_stage,
                    "stdout_logged": item.fallback.stdout_logged,
                },
                "errors": item.errors,
                "warnings": item.warnings,
                "quality_checks": item.quality_checks,
                "extraction_audit": item.extraction_audit,
                "extraction_issues": item.extraction_issues,
            }
            for item in results
        ],
    }

    batch_report_path = config.output_dir / "batch_report.json"
    write_json(batch_report_path, batch_report)

    print(f"Batch report written to: {batch_report_path}", flush=True)

    return 0 if batch_report["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
