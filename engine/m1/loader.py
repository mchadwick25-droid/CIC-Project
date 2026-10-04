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


# A world's records outside records/<code>/: what the site and the
# Facilitator read (Build/worlds/<code>/surface/) and the build's own search
# log (Build/worlds/<code>/build/records/). Neither reaches a package.
SURFACE_RECORD_TYPES = frozenset({"world_front", "facilitator_brief"})
RESIDUE_RECORD_TYPES = frozenset({"search_record"})


def world_record_homes(world_key: str, records_root: Path = RECORDS_ROOT) -> dict[str, Path]:
    """Each home of a world's records by name: "world" (records/<code>/,
    what the package carries), "surface" and "residue"."""
    worlds = records_root.parent / "Build" / "worlds" / world_key
    return {"world": records_root / world_key, "surface": worlds / "surface", "residue": worlds / "build" / "records"}


def home_for_record_type(record_type: str | None) -> str:
    if record_type in SURFACE_RECORD_TYPES:
        return "surface"
    if record_type in RESIDUE_RECORD_TYPES:
        return "residue"
    return "world"


def _load_record_dirs(roots, records: dict[str, dict]) -> dict[str, dict]:
    for root in roots:
        if not root.is_dir():
            continue
        for record_type_dir in sorted(p for p in root.iterdir() if p.is_dir()):
            for record_path in sorted(record_type_dir.glob("*.md")):
                record = parse_record_file(record_path)
                rid = record.get("id")
                if not rid:
                    raise RecordParseError(f"{record_path}: record has no id")
                if rid in records:
                    raise RecordParseError(f"duplicate record id {rid!r}: {record_path} and {records[rid]['_path']}")
                records[rid] = record
    return records


def load_world_records(world_key: str, records_root: Path = RECORDS_ROOT) -> dict[str, dict]:
    """Every record of the world, from all its homes."""
    return _load_record_dirs(world_record_homes(world_key, records_root).values(), {})


def package_records(world_key: str, records: dict[str, dict], records_root: Path = RECORDS_ROOT) -> dict[str, dict]:
    """The records that live in records/<code>/, the ones a package carries."""
    world_dir = (records_root / world_key).resolve()
    return {rid: r for rid, r in records.items() if (REPO_ROOT / r["_path"]).resolve().is_relative_to(world_dir)}


# The fleet's own records, kept with the engine module that owns each kind:
# the shape's fleet_voice, the canon questions, and M5's modern terms with
# the sources and contested claim their cards cite.
FLEET_RECORD_ROOTS = (
    REPO_ROOT / "engine" / "shape" / "records",
    REPO_ROOT / "engine" / "canon" / "records",
    REPO_ROOT / "engine" / "m5" / "records",
)


@lru_cache(maxsize=1)
def load_fleet_records() -> dict[str, dict]:
    """Every fleet record by id. Cached: the turn path reads it several
    times per message and the files never change in a running image, so
    callers treat the shared dict as read-only."""
    return _load_record_dirs(FLEET_RECORD_ROOTS, {})


def voiced_records(records: dict) -> dict:
    """The records the voice may speak from: every record not marked
    `voice: analytic`. Only these reach compiled/; the gates and the frozen
    record copy see every record."""
    return {rid: r for rid, r in records.items() if r.get("voice") != "analytic"}
