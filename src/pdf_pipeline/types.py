from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class PaperJob:
    source_path: Path
    paper_id: str


@dataclass
class PipelineConfig:
    input_dir: Path
    output_dir: Path
    workers: int = 4
    ocr_mode: str = "auto"  # auto|always|never
    min_total_chars: int = 500
    min_page_chars: int = 50
    min_low_text_page_ratio: float = 0.6
    scan_like_image_area_ratio: float = 0.7
    scan_like_page_ratio: float = 0.5
    direct_ocr_scan_like_ratio_threshold: float = 0.85
    direct_ocr_low_text_ratio_threshold: float = 0.85
    table_low_coverage_reference_min: int = 8
    table_low_coverage_ratio_threshold: float = 0.25


@dataclass
class PageText:
    page_number: int
    text: str
    char_count: int
    image_area_ratio: float
    scan_like: bool


@dataclass
class TextExtraction:
    pages: list[PageText] = field(default_factory=list)
    full_text: str = ""
    total_chars: int = 0
    low_text_page_ratio: float = 0.0
    scan_like_page_ratio: float = 0.0


@dataclass
class TableRecord:
    table_id: str
    page_number: int
    rows: list[list[str]]
    caption: str | None = None
    source: str = "pdfplumber"
    csv_file: str | None = None
    quality_score: float = 1.0
    quality_flags: list[str] = field(default_factory=list)


@dataclass
class FigureRecord:
    figure_id: str
    page_number: int
    file_name: str
    caption: str | None = None
    source: str = "embedded"
    quality_score: float = 1.0
    quality_flags: list[str] = field(default_factory=list)


@dataclass
class FallbackState:
    used: bool = False
    use_camelot: bool = False
    use_ocr: bool = False
    reasons: list[str] = field(default_factory=list)
    primary_failed_stage: str = "none"
    stdout_logged: bool = False

    @property
    def fallback_used_label(self) -> str:
        if self.use_camelot and self.use_ocr:
            return "camelot+ocr"
        if self.use_camelot:
            return "camelot"
        if self.use_ocr:
            return "ocr"
        return "none"


@dataclass
class ExtractionPassResult:
    metadata: dict[str, Any] = field(default_factory=dict)
    text: TextExtraction = field(default_factory=TextExtraction)
    tables: list[TableRecord] = field(default_factory=list)
    figures: list[FigureRecord] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stage_errors: dict[str, str] = field(default_factory=dict)
    page_count: int = 0
    table_marker_pages: set[int] = field(default_factory=set)
    table_reference_count: int = 0
    malformed_table_pages: set[int] = field(default_factory=set)


@dataclass
class PaperProcessingResult:
    paper_id: str
    source_file: str
    source_path: str
    output_dir: str
    status: str
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    page_count: int = 0
    word_count: int = 0
    table_count: int = 0
    figure_count: int = 0
    fallback: FallbackState = field(default_factory=FallbackState)
    runtime_seconds: float = 0.0
    manifest_path: str = ""
    markdown_path: str = ""
    quality_checks: list[dict[str, str]] = field(default_factory=list)
    extraction_audit: dict[str, Any] = field(default_factory=dict)
    extraction_issues: list[str] = field(default_factory=list)
    confidence: dict[str, Any] = field(default_factory=dict)
    confidence_score: float = 0.0
    confidence_label: str = "low"
    is_duplicate: bool = False
    duplicate_of: str | None = None
    duplicate_reason: str | None = None

    @property
    def ok(self) -> bool:
        return self.status == "success"
