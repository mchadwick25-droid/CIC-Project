"""Stage 2d (Build-Plan.md): the holdings report - one row per vendored
file, per world, naming whether it is in scope, already named in this
world's own records, actually drawn on, and its own disposition from a
closed vocabulary. Report-only, per the stage's own bar ("nothing
blocks"); gate only after R13 (Rulings-Pending.md).

Reuses `engine.m1.cross_world`'s own `corpus_tier`/`BY_DESIGN`/
`observe_second_hand_sources` rather than duplicating that judgment, and
`cic/engine/texts_registry.discovered_files()` for the vendored-file list.
A file's "drawn on" status is a full-text scan of this world's own
`records/<world>/` subtree for the literal `cic/texts/<file>` path - the
same technique `texts_registry.citing_records()` already uses fleet-wide
(catching a citation that lives in a quote record's body prose, not just
a source record's `edition` field), scoped here to one world.
"""
from __future__ import annotations

import re
import sys

from engine.m1.cross_world import BY_DESIGN, corpus_key, corpus_tier, observe_second_hand_sources
from engine.m1.loader import load_world_records
from engine.m1.registry import REPO_ROOT, load_registry

sys.path.insert(0, str(REPO_ROOT / "cic" / "engine"))
from texts_registry import discovered_files  # noqa: E402

_RECORDS_DIR = REPO_ROOT / "records"
_EDITION_PATH = re.compile(r"cic/texts/([\w.-]+)")

# Mechanically derived, in priority order, from corpus_tier's own four
# tiers plus the two flags this report adds (drawn_on, BY_DESIGN
# membership) - no new judgment beyond what corpus_tier already asserts.
# "not yet assessed" is corpus_tier's own tier 1 ("named, never opened"):
# this world's records already name the author, so the volume is a real,
# identified candidate nobody has opened yet - the literal "19 unopened
# volumes" Build-Plan.md's own Stage 2d Done bar names for gallic.
# corpus_tier's OTHER tier-4 case (no COVERAGE entry at all - no date
# judgment made for any world, not just this one) is a different, weaker
# claim and gets its own label so the two are never conflated.
DISPOSITIONS = (
    "by design",
    "drawn on",
    "not yet assessed",
    "in scope, unread",
    "out of window",
    "no coverage entry",
)


def _drawn_on_files(world: str) -> set[str]:
    world_dir = _RECORDS_DIR / world
    found: set[str] = set()
    if not world_dir.is_dir():
        return found
    for p in world_dir.rglob("*.md"):
        try:
            text = p.read_text(encoding="utf-8")
        except OSError:
            continue
        found |= set(_EDITION_PATH.findall(text))
    return found


def _named_files(world: str, records: dict) -> set[str]:
    findings = observe_second_hand_sources(records={world: records}, worlds=[world])
    named: set[str] = set()
    for f in findings:
        named |= set(re.findall(r"[\w.-]+\.(?:xml|txt)", f.message))
    return named


def holdings_for(world: str) -> list[dict]:
    """One row per vendored file for `world`: in_scope, named_in_records,
    drawn_on, and a disposition drawn from DISPOSITIONS above."""
    registry = load_registry()
    window = registry[world]["time_window"]
    records = load_world_records(world)
    drawn = _drawn_on_files(world)
    named = _named_files(world, records)

    rows = []
    for filename in discovered_files():
        if filename == "README.md":
            continue
        key = corpus_key(filename)
        drawn_on = filename in drawn
        named_in_records = filename in named
        if key in BY_DESIGN:
            disposition = "by design"
        elif drawn_on:
            disposition = "drawn on"
        else:
            tier = corpus_tier(filename, world, window, named=named_in_records)
            if tier == "1 - named, never opened":
                disposition = "not yet assessed"
            elif tier in ("2 - same time and place", "3 - same time, different region"):
                disposition = "in scope, unread"
            elif tier == "4 - outside this window":
                disposition = "out of window"
            else:
                disposition = "no coverage entry"
        in_scope = disposition in ("drawn on", "not yet assessed", "in scope, unread")
        rows.append({
            "file": filename,
            "in_scope": in_scope,
            "named_in_records": named_in_records,
            "drawn_on": drawn_on,
            "disposition": disposition,
        })
    return rows


def report(world: str) -> str:
    rows = holdings_for(world)
    counts: dict[str, int] = {}
    for r in rows:
        counts[r["disposition"]] = counts.get(r["disposition"], 0) + 1
    lines = [f"holdings: {world} - {len(rows)} vendored file(s)", ""]
    for d in DISPOSITIONS:
        if counts.get(d):
            lines.append(f"  {d:20} {counts[d]}")
    lines.append("")
    for r in sorted(rows, key=lambda r: (r["disposition"], r["file"])):
        lines.append(f"  {r['disposition']:20} {r['file']}")
    return "\n".join(lines)
