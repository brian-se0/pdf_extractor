# PDF Extractor Pipeline

Python pipeline to extract PDF text, tables, figures, captions, and metadata into per-paper markdown outputs.

## Run

```bash
WORKERS=$(python - <<'PY'
import os, pathlib
input_dir = pathlib.Path("/Volumes/T9/lit_review")
pdfs = [p for p in input_dir.rglob("*.pdf") if p.is_file() and not p.name.startswith("._")]
cpu = max(os.cpu_count() or 1, 1)
recommended = max(1, min(len(pdfs), 8, (cpu - 1) if cpu > 2 else cpu))
print(recommended)
PY
)
echo "Using workers=$WORKERS"
python -m pdf_pipeline.run_pipeline \
  --input /Volumes/T9/lit_review \
  --workers "$WORKERS" \
  --ocr auto
```

`--output` is optional. If omitted, outputs are written to `<input>/extracted`.
For the command above, output will be written to `/Volumes/T9/lit_review/extracted`.

Fallback log lines are printed when primary extraction is insufficient:

```text
[FALLBACK] <pdf_filename> | primary_failed_stage=<stage> | fallback_used=<camelot|ocr|camelot+ocr> | reason=<reason_code>
```

Extraction audit lines are also printed to flag likely missing content:

```text
[AUDIT] <pdf_filename> | issues=<issue_codes> | tables=<extracted>/<refs> refs | figures=<extracted>/<refs> refs | equations=<detected>/<refs> refs | garbled_math_tokens=<n> | chars=<n>
```

## Output layout

- `<output>/<paper_id>/paper.md`
- `<output>/<paper_id>/assets/*`
- `<output>/<paper_id>/manifest.json`
- `<output>/batch_report.json`
- `<output>/canonical_inventory.json`

`manifest.json` and `batch_report.json` include an `extraction_audit` section with per-file and batch-level issue summaries.
Each `manifest.json` now records publication-year resolution metadata:
- `metadata.publication_year`
- `metadata.raw_year_candidates`
- `metadata.year_resolution_reason`
- `metadata.raw_pdf_year`
- `metadata.year` (canonical publication year)

Duplicate detection metadata is also included:
- `is_duplicate`
- `duplicate_of`
- `duplicate_reason`

`canonical_inventory.json` excludes duplicates by default.

Each `manifest.json` and batch `results[]` entry also includes a `confidence` object with:
- `score` (0-1)
- `label` (`high`/`medium`/`low`)
- scoring breakdown (`penalties`/`bonuses`)

## Quality Evaluation

After a run, evaluate overall extraction quality from the batch report:

```bash
python -m pdf_pipeline.quality_eval \
  --batch-report /Volumes/T9/lit_review/extracted/batch_report.json
```

Optional: compare against a gold expectation file and write JSON output:

```bash
python -m pdf_pipeline.quality_eval \
  --batch-report /Volumes/T9/lit_review/extracted/batch_report.json \
  --gold /path/to/gold_expectations.json \
  --output /Volumes/T9/lit_review/extracted/quality_eval.json
```

To include duplicates in quality evaluation:

```bash
python -m pdf_pipeline.quality_eval \
  --batch-report /Volumes/T9/lit_review/extracted/batch_report.json \
  --include-duplicates
```

## Reindex / Backfill

Repair year metadata and duplicate flags for existing extracted folders without rerunning OCR:

```bash
python -m pdf_pipeline.reindex \
  --extracted-dir /Volumes/T9/lit_review/extracted \
  --batch-report /Volumes/T9/lit_review/extracted/batch_report.json
```
