from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

from .types import FigureRecord, PageText

FIGURE_CAPTION_RE = re.compile(
    r"^\s*(?:figure|fig\.?)\s+\d+([:.\-]\s*|\s+).*$",
    re.IGNORECASE,
)


def _embedded_figure_quality(
    width: int,
    height: int,
    payload_size: int,
    has_caption: bool,
    display_area_ratio: float,
) -> tuple[float, list[str]]:
    score = 0.7
    flags: list[str] = []

    area = width * height
    if area < 20_000:
        score -= 0.35
        flags.append("small_area")

    if width < 100 or height < 100:
        score -= 0.25
        flags.append("small_edge")

    aspect_ratio = (width / height) if height else 0.0
    if aspect_ratio > 12.0 or aspect_ratio < (1 / 12.0):
        score -= 0.3
        flags.append("extreme_aspect_ratio")

    if payload_size < 2_500:
        score -= 0.2
        flags.append("small_payload")

    if display_area_ratio < 0.01:
        score -= 0.45
        flags.append("tiny_placement")
    elif display_area_ratio < 0.03:
        score -= 0.18
        flags.append("small_placement")

    if has_caption:
        score += 0.12
        flags.append("caption_nearby")

    score = max(0.0, min(1.0, score))
    return score, flags


def _find_figure_caption(page_text: str) -> str | None:
    for line in page_text.splitlines():
        compact = " ".join(line.split())
        if FIGURE_CAPTION_RE.match(compact):
            return compact
    return None


def _caption_blocks(page: Any) -> list[tuple[str, tuple[float, float, float, float]]]:
    blocks = page.get_text("blocks") or []
    results: list[tuple[str, tuple[float, float, float, float]]] = []
    for block in blocks:
        if len(block) < 5:
            continue
        x0, y0, x1, y1, text = block[0], block[1], block[2], block[3], block[4]
        compact = " ".join(str(text).split())
        if FIGURE_CAPTION_RE.match(compact):
            results.append((compact, (float(x0), float(y0), float(x1), float(y1))))
    return results


def _max_image_display_ratio(page: Any, xref: int) -> float:
    page_area = max(float(page.rect.width) * float(page.rect.height), 1.0)
    try:
        rects = page.get_image_rects(xref) or []
    except Exception:
        return 0.0
    if not rects:
        return 0.0
    areas = [max(float(rect.width), 0.0) * max(float(rect.height), 0.0) for rect in rects]
    return max(areas) / page_area if areas else 0.0


def extract_figures(
    doc: Any,
    assets_dir: Path,
    page_text_lookup: dict[int, str],
) -> tuple[list[FigureRecord], list[str]]:
    records: list[FigureRecord] = []
    warnings: list[str] = []
    seen_xrefs: set[int] = set()
    seen_hashes: set[str] = set()
    counter = 1
    discarded_low_quality = 0
    discarded_duplicates = 0
    discarded_tiny_placement = 0
    discarded_dense_embedded = 0
    discarded_page_cap = 0

    assets_dir.mkdir(parents=True, exist_ok=True)

    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        page_number = page_index + 1
        page_caption = _find_figure_caption(page_text_lookup.get(page_number, ""))
        page_had_embedded = False
        accepted_on_page = 0
        page_images = page.get_images(full=True)
        dense_embedded_page = len(page_images) > 12

        for image in page_images:
            if not image:
                continue
            xref = int(image[0])
            if xref in seen_xrefs:
                continue
            seen_xrefs.add(xref)

            try:
                image_dict = doc.extract_image(xref)
            except Exception as exc:  # noqa: BLE001
                warnings.append(f"image extract failed on page {page_number}: {exc}")
                continue

            width = int(image_dict.get("width", 0) or 0)
            height = int(image_dict.get("height", 0) or 0)
            image_payload = image_dict["image"]
            payload_size = len(image_payload)
            display_area_ratio = _max_image_display_ratio(page, xref)

            if page_caption is None and display_area_ratio < 0.008:
                discarded_tiny_placement += 1
                continue

            if page_caption is None and dense_embedded_page and display_area_ratio < 0.035:
                discarded_dense_embedded += 1
                continue

            score, flags = _embedded_figure_quality(
                width=width,
                height=height,
                payload_size=payload_size,
                has_caption=page_caption is not None,
                display_area_ratio=display_area_ratio,
            )
            if score < 0.35:
                discarded_low_quality += 1
                continue

            image_hash = hashlib.sha1(image_payload).hexdigest()[:16]
            if image_hash in seen_hashes:
                discarded_duplicates += 1
                continue
            seen_hashes.add(image_hash)

            page_limit = 3 if dense_embedded_page and page_caption is None else 5
            if page_caption is None and accepted_on_page >= page_limit:
                discarded_page_cap += 1
                continue

            ext = str(image_dict.get("ext", "png")).lower()
            if ext not in {"png", "jpg", "jpeg", "bmp", "tiff", "tif"}:
                ext = "png"

            file_name = f"fig_{counter:03d}.{ext}"
            file_path = assets_dir / file_name
            file_path.write_bytes(image_payload)
            records.append(
                FigureRecord(
                    figure_id=f"figure_{counter:03d}",
                    page_number=page_number,
                    file_name=file_name,
                    caption=page_caption,
                    source="embedded",
                    quality_score=score,
                    quality_flags=flags,
                )
            )
            counter += 1
            page_had_embedded = True
            accepted_on_page += 1

        if page_had_embedded:
            continue

        # Vector/chart fallback: if caption exists but no embedded image, crop region above caption.
        for caption, (_, y0, _, _) in _caption_blocks(page):
            clip_top = max(y0 - page.rect.height * 0.45, 0.0)
            clip_bottom = max(y0 - 4.0, clip_top)
            if clip_bottom - clip_top < page.rect.height * 0.08:
                continue

            clip = page.rect
            clip.y0 = clip_top
            clip.y1 = clip_bottom

            try:
                pix = page.get_pixmap(clip=clip, dpi=220, alpha=False)
            except Exception:
                try:
                    pix = page.get_pixmap(clip=clip, alpha=False)
                except Exception as exc:  # noqa: BLE001
                    warnings.append(f"figure crop failed on page {page_number}: {exc}")
                    continue

            file_name = f"fig_{counter:03d}.png"
            pix.save(str(assets_dir / file_name))
            crop_score = 0.78 if caption else 0.62
            crop_flags = ["page_crop"]
            if caption:
                crop_flags.append("caption_nearby")
            records.append(
                FigureRecord(
                    figure_id=f"figure_{counter:03d}",
                    page_number=page_number,
                    file_name=file_name,
                    caption=caption,
                    source="page-crop",
                    quality_score=crop_score,
                    quality_flags=crop_flags,
                )
            )
            counter += 1
            break

    if discarded_low_quality:
        warnings.append(f"discarded {discarded_low_quality} low-quality embedded figure(s)")
    if discarded_duplicates:
        warnings.append(f"discarded {discarded_duplicates} duplicate embedded figure(s)")
    if discarded_tiny_placement:
        warnings.append(f"discarded {discarded_tiny_placement} tiny-placement embedded figure(s)")
    if discarded_dense_embedded:
        warnings.append(
            f"discarded {discarded_dense_embedded} dense-page embedded figure candidate(s)"
        )
    if discarded_page_cap:
        warnings.append(f"discarded {discarded_page_cap} embedded figure(s) due to page cap")

    return records, warnings


def page_text_lookup_from_pages(pages: list[PageText]) -> dict[int, str]:
    return {page.page_number: page.text for page in pages}
