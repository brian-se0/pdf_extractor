from __future__ import annotations

import re
from statistics import median
from typing import Any

from .types import PageText, PipelineConfig, TextExtraction


def _normalize_text(value: str) -> str:
    text = value.replace("\r", "\n")
    text = re.sub(r"(\w)-\n(\w)", r"\1\2", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _render_heading_candidate(line_text: str, size: float, median_size: float) -> str:
    compact = " ".join(line_text.split())
    if len(compact) < 5:
        return compact
    if size >= max(16.0, median_size + 2.5) and len(compact) <= 120:
        return f"## {compact}"
    if size >= max(14.0, median_size + 1.5) and len(compact) <= 100:
        return f"### {compact}"
    return compact


def _compute_image_area_ratio(page: Any, blocks: list[dict[str, Any]]) -> float:
    page_area = max(page.rect.width * page.rect.height, 1.0)
    image_area = 0.0
    for block in blocks:
        if block.get("type") != 1:
            continue
        bbox = block.get("bbox", [0.0, 0.0, 0.0, 0.0])
        width = max(float(bbox[2]) - float(bbox[0]), 0.0)
        height = max(float(bbox[3]) - float(bbox[1]), 0.0)
        image_area += width * height
    return min(image_area / page_area, 1.0)


def extract_text(doc: Any, config: PipelineConfig) -> TextExtraction:
    pages: list[PageText] = []
    all_page_chunks: list[str] = []

    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        data = page.get_text("dict")
        blocks = data.get("blocks", [])

        line_items: list[tuple[float, float, str, float]] = []
        font_sizes: list[float] = []

        for block in blocks:
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                spans = line.get("spans", [])
                if not spans:
                    continue
                text = "".join(span.get("text", "") for span in spans)
                text = text.strip()
                if not text:
                    continue
                bbox = line.get("bbox", [0.0, 0.0, 0.0, 0.0])
                x0, y0 = float(bbox[0]), float(bbox[1])
                max_size = max(float(span.get("size", 0.0)) for span in spans)
                font_sizes.append(max_size)
                line_items.append((y0, x0, text, max_size))

        median_size = median(font_sizes) if font_sizes else 11.0
        line_items.sort(key=lambda item: (item[0], item[1]))

        rendered_lines = [_render_heading_candidate(text, size, median_size) for _, _, text, size in line_items]
        page_text = _normalize_text("\n".join(rendered_lines))
        char_count = len(page_text)

        image_area_ratio = _compute_image_area_ratio(page, blocks)
        scan_like = (
            char_count < config.min_page_chars
            and image_area_ratio >= config.scan_like_image_area_ratio
        )

        pages.append(
            PageText(
                page_number=page_index + 1,
                text=page_text,
                char_count=char_count,
                image_area_ratio=image_area_ratio,
                scan_like=scan_like,
            )
        )
        all_page_chunks.append(page_text)

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

    return TextExtraction(
        pages=pages,
        full_text=full_text,
        total_chars=total_chars,
        low_text_page_ratio=low_text_ratio,
        scan_like_page_ratio=scan_like_ratio,
    )
