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

`manifest.json` and `batch_report.json` include an `extraction_audit` section with per-file and batch-level issue summaries.
