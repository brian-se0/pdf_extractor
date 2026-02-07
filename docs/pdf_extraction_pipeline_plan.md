# PDF Extraction Pipeline Implementation Plan

## Objective
Build a batch pipeline that converts each PDF in `/Volumes/T9/lit_review` into:
- `<output>/<paper_id>/paper.md`
- `<output>/<paper_id>/assets/*`

The markdown should include extracted text, tables, figures, captions, and available metadata.

## Current Corpus Notes
- Source folder currently contains 54 `*.pdf` files.
- 27 are AppleDouble sidecar files (`._*.pdf`) and must be skipped.
- Effective corpus size: 27 PDFs.

## Target Output Contract
For each PDF, create:
1. `paper.md`
2. `assets/` for figures and optional table CSVs
3. `manifest.json` with extraction metadata and diagnostics

Suggested `paper.md` structure:
- YAML front matter: `paper_id`, `source_file`, `title`, `authors`, `year`, `doi`, `page_count`, `extracted_at`, `status`
- `# Title`
- `## Metadata`
- `## Abstract` (if identified)
- `## Main Text`
- `## Tables`
- `## Figures`
- `## Extraction Notes`

## Technical Architecture
Use Python with modular extractors:
- `PyMuPDF (fitz)`: text blocks, images, page rendering, PDF metadata
- `pdfplumber`: table extraction (primary)
- `camelot-py`: required table fallback for difficult ruled/aligned tables
- `pytesseract` + `ocrmypdf`: required OCR fallback for scanned/low-text PDFs
- `pydantic` or dataclasses: normalized intermediate schema
- Explicitly do not use `pypdf-table-extraction` (deprecated)

Pipeline modules:
1. `discover.py` - file discovery/filtering
2. `metadata.py` - metadata extraction and normalization
3. `text.py` - page text extraction and section assembly
4. `tables.py` - table extraction and markdown/CSV conversion
5. `figures.py` - figure extraction and caption association
6. `render_markdown.py` - final markdown rendering
7. `run_pipeline.py` - orchestration, logging, retries, manifests

## Extraction Strategy
### 1) Discovery and ID assignment
- Input glob: `*.pdf`
- Skip names starting with `._`
- `paper_id` strategy:
  - Preferred: sanitized basename
  - Add short hash suffix on collision (`<slug>_<8hex>`)

### 2) Metadata
Extract in priority order:
1. Embedded PDF info (`title`, `author`, `creation date`)
2. First-page title heuristic (largest font text block near top)
3. DOI regex from first pages
4. Year from metadata/date/DOI context

### 3) Text
- Extract page text in reading-order blocks.
- Normalize ligatures, whitespace, hyphenation at line breaks.
- Preserve heading cues using font size/weight heuristics.
- Record page boundaries in intermediate JSON for traceability.

### 4) Fallback Policy (Locked)
Fallback is mandatory and always enabled in batch runs.

Primary path:
- Text/metadata/figures via `PyMuPDF`
- Tables via `pdfplumber`

Fallback triggers (any trigger activates fallback for that PDF):
- Primary extractor throws parse errors for critical stage(s).
- Very low text yield after normalization (e.g., `<500` chars total or `<50` chars on most pages).
- Page(s) look scan-like (large image coverage and minimal extractable text).
- Table expectation mismatch (table markers in text such as `Table 1` but zero usable tables extracted).

Fallback actions:
1. Table fallback: run `camelot-py` on pages where `pdfplumber` found no usable table or malformed tables.
2. OCR fallback: run `ocrmypdf` then rerun extraction on OCR-enriched PDF when scan/low-text triggers are hit.
3. Combined fallback allowed: a PDF may use both `camelot-py` and OCR.

### 5) Tables
- Run `pdfplumber` table detection page-by-page.
- If `pdfplumber` table quality is low or empty, run `camelot-py` fallback for those pages.
- Convert simple tables to Markdown tables.
- For complex/merged tables, emit HTML table block in markdown and store raw table as CSV in `assets/`.
- Associate nearest caption (`Table N`) by spatial proximity or nearby text.

### 6) Figures
- Extract embedded raster images from PDF objects via `PyMuPDF`.
- For vector-heavy charts not exposed as embedded images:
  - Render page at high DPI and crop detected figure regions.
- Name assets deterministically: `fig_001.png`, `fig_002.png`, etc.
- Associate caption using nearby `Figure N` text anchors.

### 7) Markdown rendering
- Emit clean markdown with stable section ordering.
- Figure references format:
  - `![Figure 1: Caption](/Volumes/T9/pdf_extractor/extracted/<paper_id>/assets/fig_001.png)`
- Keep links relative inside `paper.md` when practical (`assets/fig_001.png`) to support repo portability.

### 8) Manifest and diagnostics
Create `<output>/<paper_id>/manifest.json` with:
- counts: pages, words, tables, figures
- extraction method flags (ocr used, camelot fallback used)
- warnings/errors per stage
- runtime and tool versions
- primary-path status, fallback reason(s), and fallback stage(s) used

## CLI and Runtime
Implement CLI:
```bash
python -m pdf_pipeline.run_pipeline \
  --input /Volumes/T9/lit_review \
  --workers 4 \
  --ocr auto
```

Default output behavior:
- If `--output` is omitted, use `<input>/extracted`.
- For `/Volumes/T9/lit_review`, default output is `/Volumes/T9/lit_review/extracted`.

Runtime behavior:
- Parallelize by PDF (process-level workers)
- Per-paper failure should not stop batch
- Write `batch_report.json` summarizing success/failure
- Print fallback usage to stdout during run and in end-of-run summary

Required stdout reporting format:
```text
[FALLBACK] <pdf_filename> | primary_failed_stage=<stage> | fallback_used=<camelot|ocr|camelot+ocr> | reason=<reason_code>
```

Required end-of-run summary:
```text
Fallback used for N PDF(s):
- <pdf_1> -> <fallback_used> (<reason_code>)
- <pdf_2> -> <fallback_used> (<reason_code>)
```

## Quality Gates
Define acceptance checks:
1. Every non-sidecar PDF has an output folder.
2. Every output folder has `paper.md` and `manifest.json`.
3. `paper.md` non-empty text threshold (e.g., >500 chars unless flagged scan/error).
4. All referenced figure files exist.
5. Table/figure counts in markdown match manifest counts.
6. If fallback was used, stdout entry and manifest flags must agree for that PDF.

## Validation Plan
### Phase A: Pilot (3 PDFs)
- One arXiv-style paper
- One Elsevier-formatted paper
- One scanned or image-heavy PDF
- Tune heuristics for headings/captions/tables.

### Phase B: Full batch (27 PDFs)
- Run full pipeline
- Review top 20 warnings from manifest
- Patch heuristics and rerun only failed/low-quality cases

### Phase C: Regression safety
- Add snapshot tests for markdown renderer
- Add fixture-based tests for table and figure extraction on representative PDFs

## Proposed Repository Layout

`/Volumes/T9/pdf_extractor/`
- `src/pdf_pipeline/`
- `tests/`
- `docs/pdf_extraction_pipeline_plan.md`
- `extracted/` (generated outputs)
- `pyproject.toml`
- `README.md`

## Implementation Sequence
1. Scaffold package, CLI, config, and logging.
2. Implement discovery + metadata + text (minimum viable output).
3. Implement fallback manager (trigger detection + reason codes + per-PDF fallback state).
4. Add tables extraction with `pdfplumber` primary + `camelot-py` fallback.
5. Add figure extraction + caption linking.
6. Add OCR fallback path (`ocrmypdf` + `pytesseract`) and re-extraction flow.
7. Add markdown rendering + manifests + batch report + fallback stdout summary.
8. Run pilot, tune thresholds/heuristics, run full corpus.

## Risks and Mitigations
- Multi-column reading order errors: use block ordering heuristics and optional layout fallback.
- Complex tables degrade in markdown: fallback to HTML + CSV assets.
- `camelot-py` dependency issues on some environments: pin versions and validate system dependencies early.
- Vector figures missed: page render + crop fallback.
- Scanned PDFs: OCR fallback and explicit confidence flags.
- Filename collisions/odd characters: slug + hash paper IDs.

## Deliverable Definition of Done
- All 27 non-sidecar PDFs processed into per-paper markdown + assets.
- Figure links resolve and render in markdown.
- Tables represented in markdown/HTML with preserved structure as feasible.
- Metadata fields populated where extractable and marked null otherwise.
- Batch report identifies failures and low-confidence outputs for manual review.
