from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def _safe_div(numerator: int | float, denominator: int | float) -> float:
    if denominator == 0:
        return 0.0
    return float(numerator) / float(denominator)


def evaluate_batch_report(
    batch_report: dict[str, Any],
    gold: dict[str, Any] | None = None,
) -> dict[str, Any]:
    results = list(batch_report.get("results", []))
    total = len(results)

    success = sum(1 for result in results if result.get("status") == "success")
    partial = sum(1 for result in results if result.get("status") == "partial")
    failed = sum(1 for result in results if result.get("status") == "failed")
    fallback_used = sum(1 for result in results if result.get("fallback", {}).get("used"))

    tables = [int(result.get("table_count", 0) or 0) for result in results]
    figures = [int(result.get("figure_count", 0) or 0) for result in results]
    words = [int(result.get("word_count", 0) or 0) for result in results]

    issues = Counter()
    papers_with_audit_issues = 0
    table_ref_gap = 0
    figure_ref_gap = 0
    equation_ref_gap = 0

    for result in results:
        extraction_issues = list(result.get("extraction_issues", []))
        if extraction_issues:
            papers_with_audit_issues += 1
        for issue in extraction_issues:
            issues[issue] += 1

        audit = result.get("extraction_audit", {})
        metrics = audit.get("metrics", {})

        if (
            int(metrics.get("table_reference_count", 0) or 0) > 0
            and int(metrics.get("extracted_table_count", 0) or 0) == 0
        ):
            table_ref_gap += 1

        if (
            int(metrics.get("figure_reference_count", 0) or 0) > 0
            and int(metrics.get("extracted_figure_count", 0) or 0) == 0
        ):
            figure_ref_gap += 1

        if (
            int(metrics.get("equation_reference_count", 0) or 0) > 0
            and int(metrics.get("equation_like_line_count", 0) or 0) == 0
        ):
            equation_ref_gap += 1

    warning_counts = Counter()
    for result in results:
        for warning in result.get("warnings", []):
            warning_counts[warning] += 1

    summary: dict[str, Any] = {
        "total": total,
        "success": success,
        "partial": partial,
        "failed": failed,
        "success_rate": round(_safe_div(success, total), 4),
        "fallback_rate": round(_safe_div(fallback_used, total), 4),
        "avg_tables": round(_safe_div(sum(tables), total), 3),
        "avg_figures": round(_safe_div(sum(figures), total), 3),
        "avg_words": round(_safe_div(sum(words), total), 1),
        "papers_with_audit_issues": papers_with_audit_issues,
        "issue_counts": dict(issues),
        "table_ref_gap_papers": table_ref_gap,
        "figure_ref_gap_papers": figure_ref_gap,
        "equation_ref_gap_papers": equation_ref_gap,
        "top_warnings": warning_counts.most_common(10),
    }

    if gold:
        expectations = dict(gold.get("papers", {}))
        gold_total = 0
        gold_pass = 0
        failures: list[dict[str, Any]] = []

        by_source = {result.get("source_file"): result for result in results}

        for source_file, expectation in expectations.items():
            gold_total += 1
            result = by_source.get(source_file)
            if result is None:
                failures.append(
                    {
                        "source_file": source_file,
                        "reason": "missing_in_batch",
                    }
                )
                continue

            table_count = int(result.get("table_count", 0) or 0)
            figure_count = int(result.get("figure_count", 0) or 0)
            issues_here = set(result.get("extraction_issues", []))

            min_tables = expectation.get("min_tables")
            max_tables = expectation.get("max_tables")
            min_figures = expectation.get("min_figures")
            forbidden_issues = set(expectation.get("forbidden_issues", []))

            checks = []
            if min_tables is not None:
                checks.append(table_count >= int(min_tables))
            if max_tables is not None:
                checks.append(table_count <= int(max_tables))
            if min_figures is not None:
                checks.append(figure_count >= int(min_figures))
            if forbidden_issues:
                checks.append(len(issues_here & forbidden_issues) == 0)

            ok = all(checks) if checks else True
            if ok:
                gold_pass += 1
            else:
                failures.append(
                    {
                        "source_file": source_file,
                        "table_count": table_count,
                        "figure_count": figure_count,
                        "issues": sorted(issues_here),
                        "expectation": expectation,
                    }
                )

        summary["gold_eval"] = {
            "total": gold_total,
            "pass": gold_pass,
            "fail": gold_total - gold_pass,
            "pass_rate": round(_safe_div(gold_pass, gold_total), 4),
            "failures": failures,
        }

    return summary


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate extraction quality from batch_report.json")
    parser.add_argument("--batch-report", type=Path, required=True)
    parser.add_argument("--gold", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    batch_report = json.loads(args.batch_report.read_text(encoding="utf-8"))
    gold = None
    if args.gold is not None:
        gold = json.loads(args.gold.read_text(encoding="utf-8"))

    summary = evaluate_batch_report(batch_report, gold)

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
