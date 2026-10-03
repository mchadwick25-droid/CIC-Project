"""Record file parsing and per-world/fleet loading (Artifact-1 SS1). One
record = one file: YAML front matter between `---` fences + a free markdown
body. The body is provenance/build notes only - never read by any builder or
gate, so it is kept but excluded from validation.
"""
from functools import lru_cache
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
RECORDS_ROOT = REPO_ROOT / "records"

FENCE = "---"


class RecordParseError(ValueError):
    pass


def _split_record_text(text: str, label: str) -> tuple[dict, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != FENCE:
        raise RecordParseError(f"{label}: does not open with a {FENCE} front-matter fence")
    try:
        close = lines[1:].index(FENCE) + 1
    except ValueError as e:
        raise RecordParseError(f"{label}: no closing {FENCE} fence found") from e
    front_matter_text = "\n".join(lines[1:close])
    body = "\n".join(lines[close + 1 :]).strip()
    record = yaml.safe_load(front_matter_text) or {}
    if not isinstance(record, dict):
        raise RecordParseError(f"{label}: front matter did not parse to a mapping")
    return record, body


def parse_record_file(path: Path) -> dict:
    record, body = _split_record_text(path.read_text(encoding="utf-8"), str(path))
    record["_path"] = str(path.relative_to(REPO_ROOT))
    record["_body"] = body
    return record


def parse_record_text(text: str, label: str) -> dict:
    """A record read from somewhere other than the working tree (e.g. a past
    version from git). `label` names the source in error messages; there is
    no `_path`, since the text has no file in this checkout."""
    record, body = _split_record_text(text, label)
    record["_body"] = body
    return record


def load_world_records(world_key: str, records_root: Path = RECORDS_ROOT) -> dict[str, dict]:
    world_dir = records_root / world_key
    records: dict[str, dict] = {}
    for record_type_dir in sorted(p for p in world_dir.iterdir() if p.is_dir()):
        for record_path in sorted(record_type_dir.glob("*.md")):
            record = parse_record_file(record_path)
            rid = record.get("id")
            if not rid:
                raise RecordParseError(f"{record_path}: record has no id")
            if rid in records:
                raise RecordParseError(f"duplicate record id {rid!r}: {record_path} and {records[rid]['_path']}")
            records[rid] = record
    return records


@lru_cache(maxsize=4)
def load_fleet_records(records_root: Path = RECORDS_ROOT) -> dict[str, dict]:
    """Cached: parsing the ~95 fleet files
    measures 57-63ms warm, and the turn path calls this THREE times per
    participant message - ~190ms of GIL-held CPU per message re-parsing
    identical, image-immutable files. The cache returns one shared dict:
    callers treat it as read-only (every current caller does; the
    selftest's seeded-defect mutation path goes through
    load_world_records, which stays uncached for exactly that reason)."""
    return load_world_records("_fleet", records_root=records_root)



def voiced_records(records: dict) -> dict:
    """The records the voice may speak from: every record not marked
    `voice: analytic`. Only these reach compiled/; the gates and the frozen
    record copy see every record."""
    return {rid: r for rid, r in records.items() if r.get("voice") != "analytic"}
