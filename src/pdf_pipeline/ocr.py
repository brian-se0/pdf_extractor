from __future__ import annotations

import io
import re
import shutil
import subprocess
from pathlib import Path

from .deps import MissingDependencyError, require_module
from .types import PageText, PipelineConfig, TextExtraction

WATERMARK_LINE_PATTERNS = (
    re.compile(r"reproduced with permission of the copyright owner", re.IGNORECASE),
    re.compile(r"further reproduction prohibited", re.IGNORECASE),
    re.compile(r"downloaded from https?://", re.IGNORECASE),
    re.compile(r"this content downloaded from", re.IGNORECASE),
    re.compile(r"all use subject to", re.IGNORECASE),
    re.compile(r"terms-and-conditions", re.IGNORECASE),
    re.compile(r"access to the journal", re.IGNORECASE),
    re.compile(r"https?://about\.jstor\.org/terms", re.IGNORECASE),
    re.compile(r"wiley online library", re.IGNORECASE),
    re.compile(r"^license$", re.IGNORECASE),
)


def _normalize_text(value: str) -> str:
    text = value.replace("\x00", "").replace("\r", "\n")
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _compact_line(value: str) -> str:
    return " ".join(value.replace("\x00", "").split()).strip()


def _is_watermark_line(value: str) -> bool:
    compact = _compact_line(value)
    if not compact:
        return False
    return any(pattern.search(compact) for pattern in WATERMARK_LINE_PATTERNS)


def run_ocrmypdf(
    input_pdf: Path,
    output_pdf: Path,
    force_ocr: bool = False,
) -> tuple[bool, str | None]:
    if shutil.which("ocrmypdf") is None:
        return False, "ocrmypdf binary not found on PATH"

    output_pdf.parent.mkdir(parents=True, exist_ok=True)

    command = ["ocrmypdf", "--quiet", "--optimize", "0"]
    if force_ocr:
        command.append("--force-ocr")
    else:
        command.append("--skip-text")

    command.extend([str(input_pdf), str(output_pdf)])

    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)

    if completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip() or "unknown OCR error"
        return False, message

    return True, None


def run_tesseract_page_ocr(
    input_pdf: Path,
    config: PipelineConfig,
) -> tuple[TextExtraction | None, str | None]:
    try:
        fitz = require_module("fitz", install_name="pymupdf")
        pytesseract = require_module("pytesseract")
        pil_image = require_module("PIL.Image", install_name="pillow")
    except MissingDependencyError as exc:
        return None, str(exc)

    try:
        doc = fitz.open(str(input_pdf))
    except Exception as exc:  # noqa: BLE001
        return None, str(exc)

    pages: list[PageText] = []
    all_page_chunks: list[str] = []

    try:
        for page_index in range(doc.page_count):
            page = doc.load_page(page_index)
            try:
                pix = page.get_pixmap(dpi=220, alpha=False)
                image = pil_image.open(io.BytesIO(pix.tobytes("png")))
                raw_text = pytesseract.image_to_string(image)
            except Exception:
                raw_text = ""

            filtered_lines = []
            for line in raw_text.splitlines():
                compact = _compact_line(line)
                if not compact or _is_watermark_line(compact):
                    continue
                filtered_lines.append(compact)

            page_text = _normalize_text("\n".join(filtered_lines))
            char_count = len(page_text)
            scan_like = char_count < config.min_page_chars

            pages.append(
                PageText(
                    page_number=page_index + 1,
                    text=page_text,
                    char_count=char_count,
                    image_area_ratio=1.0,
                    scan_like=scan_like,
                )
            )
            all_page_chunks.append(page_text)
    finally:
        doc.close()

    full_text = _normalize_text("\n\n".join(chunk for chunk in all_page_chunks if chunk))
    total_chars = len(full_text)

    if pages:
        low_text_pages = sum(1 for page in pages if page.char_count < config.min_page_chars)
        scan_like_pages = sum(1 for page in pages if page.scan_like)
        low_text_ratio = low_text_pages / len(pages)
        scan_like_ratio = scan_like_pages / len(pages)
    else:
        low_text_ratio = 0.0
        scan_like_ratio = 0.0

    return (
        TextExtraction(
            pages=pages,
            full_text=full_text,
            total_chars=total_chars,
            low_text_page_ratio=low_text_ratio,
            scan_like_page_ratio=scan_like_ratio,
        ),
        None,
    )
