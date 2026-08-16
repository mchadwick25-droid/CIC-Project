"""Loader and resolver for a world's Source Registry (Doc_02).

The lexicon and story chunks cite sources inline as parenthetical registry
references, e.g. "(Source Registry #26, cross-checked)" or "(Registry P03)".
This module loads the full registry (extracted from Doc_02's companion
workbook) and resolves those references to the full row - author, date,
confidence, boundary status, and any verification notes - so a citation can
carry more than the bare prose that was quoted at authoring time.
"""

import json
import re
from functools import lru_cache

from app.config import settings

# Matches "Source Registry #10", "Source Registry #10, #13", "Registry P03",
# "Registry #52", etc. Captures the ids substring for further splitting.
REGISTRY_REFERENCE_PATTERN = re.compile(
    r"(?:Source\s+)?Registry\s+((?:#?[A-Za-z]?\d+[,\s]*)+)",
    re.IGNORECASE,
)
ID_PATTERN = re.compile(r"#?([A-Za-z]?\d+)")


@lru_cache(maxsize=None)
def _load_registry(world_id: str) -> dict[str, dict]:
    """Load and index a world's source registry by row id (cached per world).

    Redesign step 6 (2026-08-14): sources.json (the records-generated FAIR
    export) is now the preferred backing - it carries every source record,
    where the frozen source_registry.json extract had fallen behind it
    (references past its last row silently failed to resolve). Worlds that
    still ship only source_registry.json keep working unchanged.
    """
    cfg = settings.get_world_config(world_id)
    path = cfg.source_registry_path
    if path.exists():
        # a world still shipping the frozen extract keeps its exact
        # historical behavior, letter-prefixed row ids ("P03") included
        rows = json.loads(path.read_text(encoding="utf-8"))
        return {row["id"]: row for row in rows}

    # A world whose registry extract has been retired (Syriac first,
    # 2026-08-14) resolves from the records-generated FAIR export instead -
    # which carries EVERY source record, where the frozen extract had
    # fallen behind (references past its last row silently failed).
    fair = cfg.data_path / "sources.json"
    if not fair.exists():
        return {}
    data = json.loads(fair.read_text(encoding="utf-8"))
    indexed = {}
    for row in data.get("sources") or []:
        key = row.get("registry_row")
        if key:
            # keep the resolver's historical row shape on top of the FAIR
            # fields so every existing consumer keeps reading the keys it
            # always read
            indexed[str(key)] = {
                **row,
                "id": str(key),
                "source": row.get("work_title"),
                "type": row.get("source_type"),
            }
    return indexed


def extract_referenced_ids(text: str) -> list[str]:
    """Pull every registry id referenced in a piece of text (Key Sources, Source field, etc.)."""
    ids = []
    for match in REGISTRY_REFERENCE_PATTERN.finditer(text):
        for id_match in ID_PATTERN.finditer(match.group(1)):
            ids.append(id_match.group(1))
    return ids


def resolve_references(world_id: str, text: str) -> list[dict]:
    """Resolve every registry reference found in text to its full registry row.

    Returns a list of resolved rows (deduplicated, in first-seen order). Ids
    that don't match a known registry row are silently skipped - the prose
    citation still carries the reference even if the row can't be resolved.
    """
    registry = _load_registry(world_id)
    resolved = []
    seen = set()

    for ref_id in extract_referenced_ids(text):
        if ref_id in seen:
            continue
        row = registry.get(ref_id)
        if row:
            resolved.append(row)
            seen.add(ref_id)

    return resolved
