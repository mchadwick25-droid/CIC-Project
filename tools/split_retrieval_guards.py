#!/usr/bin/env python3
"""Transparency Engine Stage 4a (part 2), R11 (`Rulings-Pending.md`, ruled
(a) 2026-09-21): splits every record's `retrieval.do_not_retrieve_when`
list into two real fields with two different jobs, instead of one field
quietly carrying both -

- `retrieval.prefer_instead` - an ordinary retrieval-scoping redirect
  ("ask about X instead, retrieve that record"). Stays nested under
  `retrieval:`, same spot `do_not_retrieve_when` held.
- `claim_guards` - a barred proposition the Representative must never
  assert (e.g. Brictio's succession). Envelope-level, like `retrieval`
  itself, so any record type can carry one; inserted as a new top-level
  key right after the (now-shorter) `retrieval:` block.

Classification reuses `engine.m4.reports.grounding_fooling_measure`'s own
`GUARD_MARKERS` keyword set rather than building a second, independent
classifier: that set is what Stage 1's own D1 measurement actually ran
against (13 of 714 lines fleet-wide are genuine guard clauses - see
Decision-Log.md and Rulings-Pending.md's R11 entry), and a fresh
classifier here would either have to reproduce that same judgment or risk
disagreeing with the one number this ruling was measured against. This is
a considered substitution for Build-Plan.md's literal "Haiku classifier"
language, not a silent deviation - logged as such in Decision-Log.md.

`do_not_retrieve_when` is deleted outright on any record touched: every
line it held moves to exactly one of `prefer_instead` or `claim_guards`,
never both, never dropped silently. A record with no lines going to
`prefer_instead` loses the key entirely rather than being left with an
empty list; same for `claim_guards`.

Edits frontmatter in place with a raw-text line splice - never a YAML
dumper round-trip - so every retained line keeps its own original
quoting/wrapping exactly, the same discipline `tools/set_source_kind.py`
already follows. A record whose `do_not_retrieve_when` block doesn't match
the shape this tool understands (flow-style, or a raw/parsed item-count
mismatch) is left untouched and reported as SKIPPED for a human pass -
never guessed at.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.m4.reports.grounding_fooling_measure import GUARD_MARKERS  # noqa: E402

RECORDS_ROOT = REPO_ROOT / "records"
_FRONTMATTER = re.compile(r"^---\n(.*?\n)---\n", re.DOTALL)
_DNRW_LINE = re.compile(r"^  do_not_retrieve_when:\s*$")
_DNRW_EMPTY_INLINE_LINE = re.compile(r"^  do_not_retrieve_when:\s*\[\s*\]\s*$")
_ITEM_PREFIX = "  - "


def is_guard(value: str) -> bool:
    """Same test `grounding_fooling_measure.collect_guard_lines()` already
    uses and Stage 1's D1 measurement was run against."""
    return any(marker in value.lower() for marker in GUARD_MARKERS)


def _retrieval_block_end(lines: list[str], retrieval_at: int) -> int:
    """Index of the first line at indent 0 after `retrieval:` - one past
    the end of the whole `retrieval:` block."""
    for i in range(retrieval_at + 1, len(lines)):
        if lines[i] and not lines[i].startswith(" "):
            return i
    return len(lines)


def _list_items(lines: list[str], start: int, end: int) -> list[list[str]]:
    """Raw line-groups for each `do_not_retrieve_when` item in
    lines[start:end] - a new group opens on a `  - ` line, and any
    less-indented-than-item-marker-but-still-indented line after it is a
    wrapped continuation of the same item (folded style is out of scope;
    none of the fleet's real lines use it - see this tool's own docstring
    survey)."""
    items: list[list[str]] = []
    for line in lines[start:end]:
        if line.startswith(_ITEM_PREFIX):
            items.append([line])
        elif items:
            items[-1].append(line)
    return items


def _dedent2(line: str) -> str:
    return line[2:] if line.startswith("  ") else line


def split_frontmatter(frontmatter: str) -> tuple[str, dict] | None:
    """Returns (new_frontmatter, change_summary), or None if this record
    has no do_not_retrieve_when to split, or its shape isn't one this tool
    can safely rewrite."""
    if "do_not_retrieve_when:" not in frontmatter:
        return None
    doc = yaml.safe_load(frontmatter) or {}
    retrieval = doc.get("retrieval")
    if not isinstance(retrieval, dict) or "do_not_retrieve_when" not in retrieval:
        return None
    parsed_items = retrieval.get("do_not_retrieve_when") or []

    lines = frontmatter.splitlines(keepends=True)
    retrieval_at = next((i for i, l in enumerate(lines) if l.startswith("retrieval:")), None)
    if retrieval_at is None:
        return None

    # `do_not_retrieve_when: []` - an inline empty flow list. Nothing to
    # redirect and nothing to guard either way, so the whole line is just
    # dropped - the common case fleet-wide (a record authored with the
    # field present but never populated).
    empty_at = next(
        (i for i in range(retrieval_at + 1, len(lines)) if _DNRW_EMPTY_INLINE_LINE.match(lines[i])),
        None,
    )
    if empty_at is not None:
        if parsed_items:
            return None  # inline line disagrees with the parsed value - don't guess
        new_lines = lines[:empty_at] + lines[empty_at + 1:]
        return "".join(new_lines), {"prefer_instead": 0, "claim_guards": 0}

    dnrw_at = next(
        (i for i in range(retrieval_at + 1, len(lines)) if _DNRW_LINE.match(lines[i])),
        None,
    )
    if dnrw_at is None:
        return None  # not a shape this tool understands

    block_end = _retrieval_block_end(lines, retrieval_at)
    raw_items = _list_items(lines, dnrw_at + 1, block_end)
    if len(raw_items) != len(parsed_items):
        return None  # can't safely correlate raw lines to parsed values

    prefer_lines: list[str] = []
    guard_lines: list[str] = []
    for raw, parsed in zip(raw_items, parsed_items):
        (guard_lines if is_guard(str(parsed)) else prefer_lines).extend(raw)

    injected = (["  prefer_instead:\n"] + prefer_lines) if prefer_lines else []
    new_retrieval_block = lines[:dnrw_at] + injected + lines[block_end:]

    if guard_lines:
        insert_at = dnrw_at + len(injected)
        claim_guards_block = ["claim_guards:\n"] + [_dedent2(l) for l in guard_lines]
        new_lines = new_retrieval_block[:insert_at] + claim_guards_block + new_retrieval_block[insert_at:]
    else:
        new_lines = new_retrieval_block

    prefer_count = sum(1 for raw, parsed in zip(raw_items, parsed_items) if not is_guard(str(parsed)))
    guard_count = len(parsed_items) - prefer_count
    change = {"prefer_instead": prefer_count, "claim_guards": guard_count}
    return "".join(new_lines), change


def migrate_world(world_key: str, *, dry_run: bool = False) -> list[dict]:
    world_dir = RECORDS_ROOT / world_key
    results: list[dict] = []

    for path in sorted(world_dir.glob("*/*.md")):
        text = path.read_text(encoding="utf-8")
        m = _FRONTMATTER.match(text)
        if not m:
            continue
        if "do_not_retrieve_when:" not in m.group(1):
            continue

        record_id_match = re.search(r"^id:\s*(\S+)", m.group(1), re.MULTILINE)
        record_id = record_id_match.group(1).strip('"\'') if record_id_match else path.stem
        rel_path = str(path.relative_to(REPO_ROOT))

        result = split_frontmatter(m.group(1))
        if result is None:
            results.append({"id": record_id, "path": rel_path, "status": "SKIPPED (unrecognized shape - needs a human pass)"})
            continue

        new_frontmatter, change = result
        new_text = "---\n" + new_frontmatter + "---\n" + text[m.end():]

        results.append({
            "id": record_id,
            "path": rel_path,
            "status": f"prefer_instead={change['prefer_instead']} claim_guards={change['claim_guards']}",
        })
        if not dry_run:
            path.write_text(new_text, encoding="utf-8")

    return results


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("usage: python tools/split_retrieval_guards.py <world_key> [--dry-run]", file=sys.stderr)
        return 2
    world_key = argv[0]
    dry_run = "--dry-run" in argv[1:]
    results = migrate_world(world_key, dry_run=dry_run)
    for r in results:
        print(f"{r['id']}: {r['status']}")
    skipped = sum(1 for r in results if r["status"].startswith("SKIPPED"))
    print(f"\n{world_key}: {len(results)} record(s) touched, {skipped} skipped" + (" (dry run - nothing written)" if dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
