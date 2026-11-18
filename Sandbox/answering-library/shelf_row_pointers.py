"""Point each vendored source record at its corpus-map bucket row.

For one world, every `kind: vendored` source record whose edition names a
vendored file gets a `shelf_row` line copied from the `row_id` of the row in
that world's own bucket whose `source_file` is that file.

  one row for the file         -> that row's row_id
  several rows (shared volume) -> the row whose `work` equals the record's
                                  `work` after normalisation, or whose work
                                  slug equals the record id slug, provided
                                  exactly one row qualifies; otherwise the
                                  record is reported as ambiguous
  no row for the file          -> reported as off-shelf, record unchanged

A record is edited by inserting the one `shelf_row:` line after its
`kind: vendored` line. No other byte of the record changes.

Usage: python Sandbox/answering-library/shelf_row_pointers.py WORLD
       [--apply] [--ambiguities PATH] [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT))

from engine.m1.registry import load_registry  # noqa: E402
from engine.m9.confinement import _EDITION_PATH  # noqa: E402
from engine.m9.loader import read_bucket_rows, read_vendored_files  # noqa: E402

AMBIGUITIES_PATH = (
    REPO_ROOT / "Build" / "Ministry" / "Features" / "Answering-From-Sources" / "Stage2_ShelfRow_Ambiguities.md"
)
DUPLICATED_FIELDS = ("author", "work", "edition", "citation")
_KIND_LINE = re.compile(r"^kind: vendored[ \t]*$")


def normalise(text: str) -> str:
    """Case, punctuation and diacritics removed; runs of other characters
    collapse to one space."""
    decomposed = unicodedata.normalize("NFKD", str(text))
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", stripped.casefold()).strip()


def slugify(text: str) -> str:
    return normalise(text).replace(" ", "-")


def row_slug(row: dict) -> str:
    return str(row["row_id"]).split("--", 1)[1]


def record_slug(record_id: str) -> str:
    return record_id.split(".source.", 1)[1]


@dataclass
class Outcome:
    record_id: str
    path: Path
    status: str
    row_id: str | None = None
    candidates: list[str] = field(default_factory=list)
    reason: str = ""


def edition_file(record: dict) -> str | None:
    m = _EDITION_PATH.search(str(record.get("edition") or ""))
    return m.group(1) if m else None


def pick_row(record_id: str, record: dict, rows: list[dict]) -> tuple[str | None, str]:
    """(row_id, reason). row_id is None when the choice is not unique."""
    if len(rows) == 1:
        return rows[0]["row_id"], "only row for the file"
    work = normalise(record.get("work") or "")
    by_work = [r for r in rows if work and normalise(r.get("work") or "") == work]
    if len(by_work) == 1:
        return by_work[0]["row_id"], "work text matches one row"
    slug = record_slug(record_id)
    by_slug = [r for r in rows if row_slug(r) == slug]
    if len(by_slug) == 1:
        return by_slug[0]["row_id"], "record id slug equals the row work slug"
    if len(by_work) > 1:
        return None, f"work text matches {len(by_work)} rows"
    if len(by_slug) > 1:
        return None, f"record id slug matches {len(by_slug)} rows"
    return None, f"{len(rows)} rows share the file; neither work text nor id slug matches exactly one"


def parse_frontmatter(text: str) -> dict:
    parts = text.split("\n---", 1)
    if not text.startswith("---") or len(parts) < 2:
        raise ValueError("record has no frontmatter")
    return yaml.safe_load(parts[0][3:] + "\n") or {}


def insert_shelf_row(text: str, row_id: str) -> str:
    """The record text with one `shelf_row:` line after its kind line."""
    try:
        parsed = yaml.safe_load(f"shelf_row: {row_id}")["shelf_row"]
    except yaml.YAMLError as exc:
        raise ValueError(f"row_id {row_id!r} is not a plain YAML scalar") from exc
    if parsed != row_id:
        raise ValueError(f"row_id {row_id!r} is not a plain YAML scalar")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].rstrip("\r\n") != "---":
        raise ValueError("record has no frontmatter")
    for i in range(1, len(lines)):
        stripped = lines[i].rstrip("\r\n")
        if stripped == "---":
            break
        if _KIND_LINE.match(stripped):
            newline = lines[i][len(stripped):] or "\n"
            return "".join(lines[: i + 1]) + f"shelf_row: {row_id}{newline}" + "".join(lines[i + 1 :])
    raise ValueError("no `kind: vendored` line inside the frontmatter")


def classify(world: str) -> tuple[list[Outcome], list[dict]]:
    census_id = load_registry()[world]["census_id"]
    rows = read_bucket_rows(census_id)
    vendored = read_vendored_files()
    by_file: dict[str, list[dict]] = {}
    for row in rows:
        by_file.setdefault(row.get("source_file"), []).append(row)

    outcomes = []
    for path in sorted((REPO_ROOT / "records" / world / "source").glob("*.md")):
        record = parse_frontmatter(path.read_text(encoding="utf-8"))
        rid = record["id"]
        if record.get("kind") != "vendored":
            outcomes.append(Outcome(rid, path, "not-vendored"))
            continue
        if record.get("shelf_row"):
            outcomes.append(Outcome(rid, path, "already-set", row_id=record["shelf_row"]))
            continue
        filename = edition_file(record)
        if filename is None or filename not in vendored:
            outcomes.append(Outcome(rid, path, "invalid-edition", reason="edition names no vendored file"))
            continue
        candidates = by_file.get(filename, [])
        if not candidates:
            outcomes.append(Outcome(rid, path, "off-shelf", reason=f"{filename} is not in this world's bucket"))
            continue
        row_id, reason = pick_row(rid, record, candidates)
        ids = [r["row_id"] for r in candidates]
        if row_id is None:
            outcomes.append(Outcome(rid, path, "ambiguous", candidates=ids, reason=reason))
        else:
            outcomes.append(Outcome(rid, path, "set", row_id=row_id, candidates=ids, reason=reason))
    return outcomes, rows


def apply(outcomes: list[Outcome]) -> int:
    changed = 0
    for outcome in outcomes:
        if outcome.status != "set":
            continue
        original = outcome.path.read_bytes().decode("utf-8")
        updated = insert_shelf_row(original, outcome.row_id)
        outcome.path.write_bytes(updated.encode("utf-8"))
        changed += 1
    return changed


def duplicated_field_counts(world: str, rows: list[dict]) -> dict[str, int]:
    """Over records that carry shelf_row: how many carry each field the row
    also holds, and how many of those agree with the row once normalised."""
    by_id = {r["row_id"]: r for r in rows}
    counts = {"records_with_shelf_row": 0}
    for name in DUPLICATED_FIELDS:
        counts[f"carries_{name}"] = 0
    counts["work_equals_row_work"] = 0
    for path in sorted((REPO_ROOT / "records" / world / "source").glob("*.md")):
        record = parse_frontmatter(path.read_text(encoding="utf-8"))
        row = by_id.get(record.get("shelf_row"))
        if row is None:
            continue
        counts["records_with_shelf_row"] += 1
        for name in DUPLICATED_FIELDS:
            if record.get(name):
                counts[f"carries_{name}"] += 1
        if normalise(record.get("work") or "") == normalise(row.get("work") or "") and record.get("work"):
            counts["work_equals_row_work"] += 1
    return counts


def render_section(world: str, outcomes: list[Outcome]) -> str:
    ambiguous = [o for o in outcomes if o.status == "ambiguous"]
    off_shelf = [o for o in outcomes if o.status == "off-shelf"]
    lines = [f"## {world}", ""]
    lines.append(f"### Ambiguous ({len(ambiguous)})")
    lines.append("")
    if ambiguous:
        for o in ambiguous:
            lines.append(f"- `{o.record_id}`: {o.reason}. Candidates:")
            lines.extend(f"  - `{c}`" for c in o.candidates)
    else:
        lines.append("None.")
    lines += ["", f"### Off-shelf ({len(off_shelf)})", ""]
    if off_shelf:
        lines.extend(f"- `{o.record_id}`: {o.reason}" for o in off_shelf)
    else:
        lines.append("None.")
    return "\n".join(lines) + "\n"


def append_section(path: Path, world: str, outcomes: list[Outcome]) -> bool:
    """Append the world's section; never rewrite existing text. False when
    the world already has a section."""
    existing = path.read_text(encoding="utf-8") if path.is_file() else ""
    if re.search(rf"(?m)^## {re.escape(world)}$", existing):
        return False
    if not existing:
        existing = "# Shelf-row ambiguities and off-shelf records\n"
    body = existing.rstrip("\n") + "\n\n" + render_section(world, outcomes)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")
    return True


def summary(world: str, outcomes: list[Outcome]) -> dict:
    tally: dict[str, int] = {}
    for o in outcomes:
        tally[o.status] = tally.get(o.status, 0) + 1
    return {"world": world, "records": len(outcomes), **tally}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("world")
    parser.add_argument("--apply", action="store_true", help="write shelf_row lines and the ambiguity section")
    parser.add_argument("--ambiguities", type=Path, default=AMBIGUITIES_PATH)
    args = parser.parse_args(argv)

    outcomes, rows = classify(args.world)
    result = summary(args.world, outcomes)
    if args.apply:
        result["written"] = apply(outcomes)
        result["ambiguity_section_added"] = append_section(args.ambiguities, args.world, outcomes)
        result["duplicated_fields"] = duplicated_field_counts(args.world, rows)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
