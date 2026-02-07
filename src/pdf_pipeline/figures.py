from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .types import FigureRecord, PageText

FIGURE_CAPTION_RE = re.compile(r"^\s*figure\s+\d+([:.\-]\s*|\s+).*$", re.IGNORECASE)


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


def extract_figures(
    doc: Any,
    assets_dir: Path,
    page_text_lookup: dict[int, str],
) -> tuple[list[FigureRecord], list[str]]:
    records: list[FigureRecord] = []
    warnings: list[str] = []
    seen_xrefs: set[int] = set()
    counter = 1

    assets_dir.mkdir(parents=True, exist_ok=True)

    for page_index in range(doc.page_count):
        page = doc.load_page(page_index)
        page_number = page_index + 1
        page_caption = _find_figure_caption(page_text_lookup.get(page_number, ""))
        page_had_embedded = False

        for image in page.get_images(full=True):
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
            if width * height < 10000:
                continue

            ext = str(image_dict.get("ext", "png")).lower()
            if ext not in {"png", "jpg", "jpeg", "bmp", "tiff", "tif"}:
                ext = "png"

            file_name = f"fig_{counter:03d}.{ext}"
            file_path = assets_dir / file_name
            file_path.write_bytes(image_dict["image"])
            records.append(
                FigureRecord(
                    figure_id=f"figure_{counter:03d}",
                    page_number=page_number,
                    file_name=file_name,
                    caption=page_caption,
                    source="embedded",
                )
            )
            counter += 1
            page_had_embedded = True

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
            records.append(
                FigureRecord(
                    figure_id=f"figure_{counter:03d}",
                    page_number=page_number,
                    file_name=file_name,
                    caption=caption,
                    source="page-crop",
                )
            )
            counter += 1
            break

    return records, warnings


def page_text_lookup_from_pages(pages: list[PageText]) -> dict[int, str]:
    return {page.page_number: page.text for page in pages}
