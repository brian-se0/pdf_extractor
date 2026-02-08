from __future__ import annotations

from pathlib import Path

from .deps import MissingDependencyError, require_module
from .figures import extract_figures, page_text_lookup_from_pages
from .metadata import extract_metadata
from .tables import count_table_references, detect_table_marker_pages, extract_tables_pdfplumber
from .text import extract_text
from .types import ExtractionPassResult, PipelineConfig, TextExtraction


def run_extraction_pass(
    pdf_path: Path,
    assets_dir: Path,
    config: PipelineConfig,
    include_figures: bool,
) -> ExtractionPassResult:
    result = ExtractionPassResult()

    try:
        fitz = require_module("fitz", install_name="pymupdf")
    except MissingDependencyError as exc:
        result.stage_errors["open"] = str(exc)
        return result

    doc = None
    try:
        doc = fitz.open(str(pdf_path))
        result.page_count = doc.page_count
    except Exception as exc:  # noqa: BLE001
        result.stage_errors["open"] = str(exc)
        return result

    try:
        result.text = extract_text(doc, config)
    except Exception as exc:  # noqa: BLE001
        result.stage_errors["text"] = str(exc)
        result.text = TextExtraction()

    try:
        result.metadata = extract_metadata(doc, text_hint=result.text.full_text)
    except Exception as exc:  # noqa: BLE001
        result.stage_errors["metadata"] = str(exc)

    page_lookup = page_text_lookup_from_pages(result.text.pages)
    result.table_marker_pages = detect_table_marker_pages(result.text.pages)
    result.table_reference_count = count_table_references(result.text.pages)

    try:
        tables, table_warnings, malformed_pages = extract_tables_pdfplumber(pdf_path, page_lookup)
        result.tables = tables
        result.warnings.extend(table_warnings)
        result.malformed_table_pages = malformed_pages
    except MissingDependencyError as exc:
        result.stage_errors["tables"] = str(exc)
    except Exception as exc:  # noqa: BLE001
        result.stage_errors["tables"] = str(exc)

    if include_figures:
        try:
            figures, figure_warnings = extract_figures(doc, assets_dir, page_lookup)
            result.figures = figures
            result.warnings.extend(figure_warnings)
        except Exception as exc:  # noqa: BLE001
            result.stage_errors["figures"] = str(exc)

    doc.close()
    return result
