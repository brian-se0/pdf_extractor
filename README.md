# PDF Extractor Pipeline

Python pipeline to extract PDF text, tables, figures, captions, and metadata into per-paper markdown outputs.

## Run

```bash
python -m pdf_pipeline.run_pipeline \
  --input /Volumes/T9/lit_review \
  --workers 4 \
  --ocr auto
```

`--output` is optional. If omitted, outputs are written to `<input>/extracted`.
For the command above, output will be written to `/Volumes/T9/lit_review/extracted`.

Fallback log lines are printed when primary extraction is insufficient:

```text
[FALLBACK] <pdf_filename> | primary_failed_stage=<stage> | fallback_used=<camelot|ocr|camelot+ocr> | reason=<reason_code>
```

## Output layout

- `<output>/<paper_id>/paper.md`
- `<output>/<paper_id>/assets/*`
- `<output>/<paper_id>/manifest.json`
- `<output>/batch_report.json`
