"""The per-record retrievability audit (Build-Plan.md Stage 4c's own Done
criterion: "per-record retrievability audit printed, report-only").

Report-only, same discipline as engine.m1.bar_screen and engine.m4.reports.
retrieval_bench: it prints a summary, it never fails a build or gates
anything. What it measures is narrower than either of those - not whether a
participant's own question actually reaches a record (retrieval_bench), and
not a prose-quality reading level (bar_screen) - just the structural
precondition both of those depend on: does this record carry ANY searchable
word at all in engine.m2.builders.build_retrieval_json's own index? A
record with zero words there is unreachable by every lexical mechanism this
project has (Stage B's cell-seeded ranking, Stage A2's fulltext fallback,
and Stage 4c's own Stage B2 fill alike all score against the same word-
overlap primitive, engine.prose.overlap_coefficient / content_words) -
worth surfacing on its own, before any live query ever tests it.

A record with zero retrieval words is not necessarily a defect: fleet_voice
and voice_craft carry only "instruction" fields by design (never a claim
about the world, never meant to be retrieved) and are EXPECTED to show
zero here every time - reported separately, not folded into the same count
as every other record_type, so a real gap in (say) honest_limit coverage
can't hide inside an expected, harmless voice_craft/fleet_voice total.

Usage: python -m engine.m2.reports.retrieval_audit
"""
from __future__ import annotations

import json

from engine.m1.loader import load_world_records
from engine.m1.registry import load_registry
from engine.m2.builders import build_retrieval_json
from engine.m2.checks import STALENESS_CHECKABLE_STATES

# fleet_voice never reaches load_world_records (it's fleet-wide, not
# per-world - see engine.m1.loader); voice_craft is per-world but, like
# fleet_voice, declares only "instruction"-role fields in engine.m1.
# spoken_fields.SPOKEN_FIELDS, so an empty word set here is its own
# by-design state, not a finding. search_record is build-time bookkeeping
# (source-search sweep tracking) - not declared in SPOKEN_FIELDS at all,
# and already excluded from compiled/repository.json itself (engine.m2.
# builders._PACKAGE_EXCLUDED_RECORD_TYPES), so it never reaches the
# runtime this audit is a precondition for.
_EXPECTED_EMPTY_TYPES = {"voice_craft", "search_record"}


def audit_world(world_key: str) -> dict:
    records = load_world_records(world_key)
    index = json.loads(build_retrieval_json(records))
    by_type: dict[str, dict] = {}
    for record in records.values():
        record_type = record.get("record_type")
        bucket = by_type.setdefault(record_type, {"total": 0, "empty": []})
        bucket["total"] += 1
        if not index.get(record["id"]):
            bucket["empty"].append(record["id"])
    return by_type


def main() -> None:
    registry = load_registry()
    world_keys = sorted(w for w, entry in registry.items() if entry.get("state") in STALENESS_CHECKABLE_STATES)
    print(f"{'world':14s} {'type':18s} {'total':>6s} {'empty':>6s}  unreachable ids")
    for world_key in world_keys:
        by_type = audit_world(world_key)
        for record_type in sorted(by_type):
            bucket = by_type[record_type]
            if not bucket["empty"]:
                continue
            expected = " (expected)" if record_type in _EXPECTED_EMPTY_TYPES else ""
            ids = ", ".join(bucket["empty"][:3]) + (", ..." if len(bucket["empty"]) > 3 else "")
            print(f"{world_key:14s} {record_type:18s} {bucket['total']:6d} {len(bucket['empty']):6d}{expected}  {ids}")


if __name__ == "__main__":
    main()
