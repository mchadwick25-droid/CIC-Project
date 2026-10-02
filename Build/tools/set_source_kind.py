#!/usr/bin/env python3
"""Library Access Gate D3 SS5/SS7 (increment 7's kind-only half, per change
order CO-5 - Decision-Log.md entry 22). Sets `kind` on every real source
record that doesn't have it yet, mechanically from `edition`: the same
binary rule `engine.m9.confinement.gate_source_kind` already checks
agreement against - `vendored` if `edition` names a file that is really in
`cic/texts/`, `unvendored` otherwise.

Never sets `kind: absence` - that is an editorial judgment about a record's
own subject (it documents a claimed gap, not merely unvendored material),
not something derivable from `edition` alone; a source record whose `edition`
names a real file can still be an absence record (the file exists, but the
specific content the record is ABOUT is what's missing from it - e.g.
gallic's two `*-absence` records point at a real, vendored NPNF volume that
simply omits the letters/conferences in question). Every source record
already following the project's own `*-absence` id convention is skipped
here and left for a human editorial pass (kind: absence + real
absence_probes authored and verified against the text) - not part of this
mechanical migration.

Edits the frontmatter in place with a plain text insertion (finds the next
unindented top-level YAML key after `edition:`'s own line, which may itself
span several physical lines as a folded/quoted scalar, and inserts `kind:
<value>` immediately before it) rather than round-tripping the file through
a YAML dumper, which would reflow hand-authored formatting it doesn't own.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
TEXTS_DIR = REPO_ROOT / "cic" / "texts"
_EDITION_PATH = re.compile(r"cic/texts/([\w\-]+\.(?:txt|xml))")
_FRONTMATTER = re.compile(r"^---\n(.*?\n)---\n", re.DOTALL)
_TOP_LEVEL_KEY = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*:")


def _vendored_files() -> frozenset[str]:
    if not TEXTS_DIR.is_dir():
        return frozenset()
    return frozenset(p.name for p in TEXTS_DIR.iterdir() if p.suffix in (".txt", ".xml"))


def classify_edition(edition: str, vendored_files: frozenset[str]) -> str:
    m = _EDITION_PATH.search(edition or "")
    return "vendored" if (m and m.group(1) in vendored_files) else "unvendored"


def _insertion_line(lines: list[str]) -> int | None:
    """Index of the line to insert `kind:` before - the first unindented
    top-level key strictly after the (possibly multi-line) `edition:`
    field. None if there's no `edition:` line to anchor on."""
    edition_at = next((i for i, line in enumerate(lines) if line.startswith("edition:")), None)
    if edition_at is None:
        return None
    for i in range(edition_at + 1, len(lines)):
        if _TOP_LEVEL_KEY.match(lines[i]):
            return i
    return len(lines)


def migrate_world(world_key: str, *, dry_run: bool = False) -> list[dict]:
    source_dir = REPO_ROOT / "records" / world_key / "source"
    vendored_files = _vendored_files()
    changes: list[dict] = []

    for path in sorted(source_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = _FRONTMATTER.match(text)
        if not m:
            continue
        doc = yaml.safe_load(m.group(1)) or {}
        if doc.get("record_type") != "source":
            continue
        record_id = doc.get("id", path.stem)
        if "kind" in doc:
            continue
        if str(record_id).endswith("-absence"):
            changes.append({"id": record_id, "path": str(path.relative_to(REPO_ROOT)), "kind": "SKIPPED (absence-id, needs editorial pass)"})
            continue

        edition = str(doc.get("edition") or "")
        kind = classify_edition(edition, vendored_files)

        body_lines = text.splitlines(keepends=True)
        frontmatter_lines = m.group(1).splitlines(keepends=True)
        insert_at = _insertion_line(frontmatter_lines)
        if insert_at is None:
            changes.append({"id": record_id, "path": str(path.relative_to(REPO_ROOT)), "kind": "SKIPPED (no edition: line found)"})
            continue

        new_frontmatter = frontmatter_lines[:insert_at] + [f"kind: {kind}\n"] + frontmatter_lines[insert_at:]
        new_text = "---\n" + "".join(new_frontmatter) + "---\n" + text[m.end():]

        changes.append({"id": record_id, "path": str(path.relative_to(REPO_ROOT)), "kind": kind})
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")

    return changes


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("usage: python Build/tools/set_source_kind.py <world_key> [--dry-run]", file=sys.stderr)
        return 2
    world_key = argv[0]
    dry_run = "--dry-run" in argv[1:]
    changes = migrate_world(world_key, dry_run=dry_run)
    for c in changes:
        print(f"{c['id']}: {c['kind']}")
    by_kind: dict[str, int] = {}
    for c in changes:
        by_kind[c["kind"]] = by_kind.get(c["kind"], 0) + 1
    print(f"\n{world_key}: {len(changes)} record(s) touched - " + ", ".join(f"{k}={n}" for k, n in sorted(by_kind.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
