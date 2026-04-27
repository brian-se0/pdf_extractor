from __future__ import annotations

import hashlib
import re
import unicodedata
from difflib import SequenceMatcher
from typing import Any

TITLE_SIMILARITY_THRESHOLD = 0.98
MAX_FIRST_PAGE_HASH_DISTANCE = 20
MIN_DOI_SUFFIX_LENGTH = 4

ARTIFACT_PATTERNS = (
    "ebsco-fulltext",
    "downloaded-fulltext",
)


def _clean_text(value: str | None) -> str:
    if not value:
        return ""
    return " ".join(str(value).replace("\x00", " ").split())


def normalize_doi(value: str | None) -> str | None:
    text = _clean_text(value).lower()
    if not text:
        return None

    prefixes = (
        "https://doi.org/",
        "http://doi.org/",
        "doi:",
    )
    for prefix in prefixes:
        if text.startswith(prefix):
            text = text[len(prefix):]
            break
    text = text.strip().rstrip(".,;")
    if not _is_plausible_doi(text):
        return None
    return text or None


def _is_plausible_doi(value: str) -> bool:
    match = re.match(r"^10\.\d{4,9}/(.+)$", value)
    if not match:
        return False

    suffix = match.group(1).strip()
    if len(suffix) < MIN_DOI_SUFFIX_LENGTH:
        return False

    return bool(re.search(r"[a-z0-9]", suffix))


def normalize_title(value: str | None) -> str:
    cleaned = _clean_text(value)
    normalized = unicodedata.normalize("NFKD", cleaned)
    ascii_value = normalized.encode("ascii", "ignore").decode("ascii")
    lowered = ascii_value.lower()
    collapsed = re.sub(r"[^a-z0-9]+", " ", lowered)
    return " ".join(collapsed.split())


def extract_main_text_from_markdown(markdown_text: str) -> str:
    marker = "\n## Main Text\n"
    start = markdown_text.find(marker)
    if start == -1:
        return ""
    section = markdown_text[start + len(marker):]
    end_markers = (
        "\n## Tables\n",
        "\n## Figures\n",
        "\n## Extraction Notes\n",
    )
    end = len(section)
    for end_marker in end_markers:
        idx = section.find(end_marker)
        if idx != -1:
            end = min(end, idx)
    return section[:end].strip()


def extract_first_page_excerpt(text: str, max_tokens: int = 400) -> str:
    if not text:
        return ""
    tokens = _clean_text(text).split()
    return " ".join(tokens[:max_tokens])


def _tokenize_for_hash(text: str) -> list[str]:
    normalized = normalize_title(text)
    if not normalized:
        return []
    return normalized.split()


def compute_first_page_text_hash(text: str | None) -> str | None:
    if not text:
        return None
    tokens = _tokenize_for_hash(text)
    if not tokens:
        return None

    grams = [" ".join(tokens[idx : idx + 3]) for idx in range(max(len(tokens) - 2, 0))]
    if not grams:
        grams = tokens[:200]

    bit_weights = [0] * 64
    for gram in grams:
        digest = int(hashlib.sha1(gram.encode("utf-8")).hexdigest()[:16], 16)
        for bit in range(64):
            if (digest >> bit) & 1:
                bit_weights[bit] += 1
            else:
                bit_weights[bit] -= 1

    value = 0
    for bit, weight in enumerate(bit_weights):
        if weight >= 0:
            value |= 1 << bit
    return f"{value:016x}"


def first_page_hash_distance(first_hash: str | None, second_hash: str | None) -> int | None:
    if not first_hash or not second_hash:
        return None
    try:
        return (int(first_hash, 16) ^ int(second_hash, 16)).bit_count()
    except ValueError:
        return None


def title_similarity(first_title: str | None, second_title: str | None) -> float:
    first = normalize_title(first_title)
    second = normalize_title(second_title)
    if not first or not second:
        return 0.0
    return SequenceMatcher(None, first, second).ratio()


def _is_artifact_record(record: dict[str, Any]) -> bool:
    source_file = _clean_text(record.get("source_file")).lower()
    paper_id = _clean_text(record.get("paper_id")).lower()
    joined = f"{source_file} {paper_id}"
    return any(pattern in joined for pattern in ARTIFACT_PATTERNS)


def _status_rank(status: str | None) -> int:
    value = _clean_text(status).lower()
    if value == "success":
        return 0
    if value == "partial":
        return 1
    if value == "failed":
        return 2
    return 3


def _record_score(record: dict[str, Any]) -> tuple[Any, ...]:
    metadata = dict(record.get("metadata") or {})
    doi = normalize_doi(metadata.get("doi"))
    words = int(record.get("word_count", 0) or 0)
    tables = int(record.get("table_count", 0) or 0)
    figures = int(record.get("figure_count", 0) or 0)
    return (
        1 if _is_artifact_record(record) else 0,
        _status_rank(record.get("status")),
        0 if doi else 1,
        -words,
        -tables,
        -figures,
        _clean_text(record.get("paper_id")).lower(),
    )


def _pick_canonical(records: list[dict[str, Any]]) -> dict[str, Any]:
    return sorted(records, key=_record_score)[0]


def build_duplicate_flags(records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    flags = {
        _clean_text(record.get("paper_id")): {
            "is_duplicate": False,
            "duplicate_of": None,
            "duplicate_reason": None,
        }
        for record in records
    }
    by_paper_id = {_clean_text(record.get("paper_id")): record for record in records}

    by_doi: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        paper_id = _clean_text(record.get("paper_id"))
        metadata = dict(record.get("metadata") or {})
        doi = normalize_doi(metadata.get("doi"))
        if not paper_id or not doi:
            continue
        by_doi.setdefault(doi, []).append(record)

    for doi, group in by_doi.items():
        if len(group) < 2:
            continue
        canonical = _pick_canonical(group)
        canonical_id = _clean_text(canonical.get("paper_id"))
        for record in group:
            paper_id = _clean_text(record.get("paper_id"))
            if paper_id == canonical_id:
                continue
            flags[paper_id] = {
                "is_duplicate": True,
                "duplicate_of": canonical_id,
                "duplicate_reason": f"doi_match:{doi}",
            }

    candidates = [record for record in records if not flags[_clean_text(record.get("paper_id"))]["is_duplicate"]]
    grouped_indices: list[set[int]] = []
    used = [False] * len(candidates)

    for idx, record in enumerate(candidates):
        if used[idx]:
            continue
        group = {idx}
        used[idx] = True
        changed = True
        while changed:
            changed = False
            for probe_idx, probe in enumerate(candidates):
                if probe_idx in group:
                    continue
                for member_idx in list(group):
                    member = candidates[member_idx]
                    member_meta = dict(member.get("metadata") or {})
                    probe_meta = dict(probe.get("metadata") or {})

                    sim = title_similarity(member_meta.get("title"), probe_meta.get("title"))
                    if sim < TITLE_SIMILARITY_THRESHOLD:
                        continue

                    member_hash = member_meta.get("first_page_text_hash")
                    probe_hash = probe_meta.get("first_page_text_hash")
                    distance = first_page_hash_distance(member_hash, probe_hash)
                    if distance is None or distance > MAX_FIRST_PAGE_HASH_DISTANCE:
                        continue

                    group.add(probe_idx)
                    used[probe_idx] = True
                    changed = True
                    break
        grouped_indices.append(group)

    for group_indices in grouped_indices:
        if len(group_indices) < 2:
            continue
        group_records = [candidates[idx] for idx in sorted(group_indices)]
        canonical = _pick_canonical(group_records)
        canonical_id = _clean_text(canonical.get("paper_id"))
        canonical_meta = dict(canonical.get("metadata") or {})

        for record in group_records:
            paper_id = _clean_text(record.get("paper_id"))
            if paper_id == canonical_id:
                continue
            metadata = dict(record.get("metadata") or {})
            sim = title_similarity(metadata.get("title"), canonical_meta.get("title"))
            distance = first_page_hash_distance(
                metadata.get("first_page_text_hash"),
                canonical_meta.get("first_page_text_hash"),
            )
            reason = f"title_hash_match(sim={sim:.3f},distance={distance})"
            flags[paper_id] = {
                "is_duplicate": True,
                "duplicate_of": canonical_id,
                "duplicate_reason": reason,
            }

    for record in records:
        paper_id = _clean_text(record.get("paper_id"))
        if not paper_id or flags[paper_id]["is_duplicate"]:
            continue
        if not _is_artifact_record(record):
            continue

        metadata = dict(record.get("metadata") or {})
        best_target: tuple[float, str] | None = None
        for other in records:
            other_id = _clean_text(other.get("paper_id"))
            if other_id == paper_id:
                continue
            if _is_artifact_record(other):
                continue
            other_meta = dict(other.get("metadata") or {})
            sim = title_similarity(metadata.get("title"), other_meta.get("title"))
            if sim < 0.99:
                continue
            if best_target is None or sim > best_target[0]:
                best_target = (sim, other_id)
        if best_target is not None:
            flags[paper_id] = {
                "is_duplicate": True,
                "duplicate_of": best_target[1],
                "duplicate_reason": f"artifact_source_title_match(sim={best_target[0]:.3f})",
            }

    return flags


def apply_duplicate_flags(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    flags = build_duplicate_flags(records)
    enriched: list[dict[str, Any]] = []
    for record in records:
        paper_id = _clean_text(record.get("paper_id"))
        merged = dict(record)
        merged.update(flags.get(paper_id, {}))
        enriched.append(merged)
    return enriched
