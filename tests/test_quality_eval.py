from pdf_pipeline.quality_eval import evaluate_batch_report


def test_evaluate_batch_report_summary_counts() -> None:
    report = {
        "results": [
            {
                "source_file": "a.pdf",
                "status": "success",
                "table_count": 2,
                "figure_count": 1,
                "word_count": 100,
                "fallback": {"used": False},
                "extraction_issues": [],
                "warnings": [],
                "extraction_audit": {
                    "metrics": {
                        "table_reference_count": 1,
                        "extracted_table_count": 2,
                        "figure_reference_count": 1,
                        "extracted_figure_count": 1,
                        "equation_reference_count": 0,
                        "equation_like_line_count": 0,
                    }
                },
            },
            {
                "source_file": "b.pdf",
                "status": "partial",
                "table_count": 0,
                "figure_count": 0,
                "word_count": 50,
                "fallback": {"used": True},
                "extraction_issues": ["likely_missing_tables"],
                "warnings": ["warn"],
                "extraction_audit": {
                    "metrics": {
                        "table_reference_count": 2,
                        "extracted_table_count": 0,
                        "figure_reference_count": 1,
                        "extracted_figure_count": 0,
                        "equation_reference_count": 1,
                        "equation_like_line_count": 0,
                    }
                },
            },
        ]
    }

    summary = evaluate_batch_report(report)

    assert summary["total"] == 2
    assert summary["success"] == 1
    assert summary["partial"] == 1
    assert summary["failed"] == 0
    assert summary["papers_with_audit_issues"] == 1
    assert summary["table_ref_gap_papers"] == 1
    assert summary["figure_ref_gap_papers"] == 1
    assert summary["equation_ref_gap_papers"] == 1


def test_evaluate_batch_report_with_gold() -> None:
    report = {
        "results": [
            {
                "source_file": "a.pdf",
                "status": "success",
                "table_count": 3,
                "figure_count": 2,
                "word_count": 120,
                "fallback": {"used": False},
                "extraction_issues": [],
                "warnings": [],
                "extraction_audit": {"metrics": {}},
            }
        ]
    }
    gold = {
        "papers": {
            "a.pdf": {"min_tables": 2, "min_figures": 1, "forbidden_issues": ["likely_missing_tables"]}
        }
    }

    summary = evaluate_batch_report(report, gold)

    assert summary["gold_eval"]["total"] == 1
    assert summary["gold_eval"]["pass"] == 1
    assert summary["gold_eval"]["fail"] == 0
