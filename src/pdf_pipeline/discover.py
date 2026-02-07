from __future__ import annotations

import hashlib
import re
import unicodedata
from pathlib import Path

from .types import PaperJob


def discover_pdfs(input_dir: Path) -> list[Path]:
    paths = []
    for path in sorted(input_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() != ".pdf":
            continue
        if path.name.startswith("._"):
            continue
        paths.append(path)
    return paths


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = ascii_value.lower()
    cleaned = re.sub(r"[^a-z0-9]+", "-", lowered)
    cleaned = re.sub(r"-+", "-", cleaned).strip("-")
    return cleaned or "paper"


def build_jobs(pdf_paths: list[Path]) -> list[PaperJob]:
    jobs: list[PaperJob] = []
    seen_ids: set[str] = set()

    for path in pdf_paths:
        base = slugify(path.stem)
        paper_id = base
        if paper_id in seen_ids:
            digest = hashlib.sha1(str(path).encode("utf-8")).hexdigest()[:8]
            paper_id = f"{base}_{digest}"
        seen_ids.add(paper_id)
        jobs.append(PaperJob(source_path=path, paper_id=paper_id))

    return jobs
