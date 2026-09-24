"""R37 build battery (Rulings-Pending.md R37, R37-A, R37-B), deterministic,
no model calls. For each of the 11 formation worlds' own real
B-other-tradition probe (engine.m4.live_uncited_claims_battery.
_other_tradition_turn, imported, not re-implemented), this runs the same
engine functions a live other_tradition turn runs - match_named_
tradition, world_records_mention_tradition, tradition_known_in_window,
and engine.m4.turn._other_tradition_directive - and records which
branch the voice's private directive takes and which R37 condition
licenses the pivot.

Every probe is turn 1 of a fresh session, so condition (b) has nothing
to quote on any of them by construction - the battery reports it for
completeness. R37-A's own expectation for this battery is 11 of 11
licensed under condition (a) (the design brief's asymmetric count, PR
#438); a lower number is a real disagreement between the build and the
ruling, not a tolerance.

The real probes all name an earlier tradition, so they never reach the
"question's own words alone" branch. A second, synthetic probe per world
(C-later-tradition) names the OTHER formation world with the latest
window start, in the same "What was your relationship with X?" shape,
so that branch is exercised on real registry data too. Its expected
licence is R37-A's own test, computed independently from the two
time_windows in this script and compared row by row.

Run: python -m engine.m4.reports.r37_build_battery
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3]))

from engine.m1.registry import formation_world_keys, load_registry
from engine.m4 import evidence as ev
from engine.m4.live_uncited_claims_battery import _other_tradition_turn
from engine.m4.turn import R26_HONEST_LIMIT_SENTENCE, _other_tradition_directive
from engine.m4.uncited_claims import (
    conversation_revealed_excerpts,
    match_named_tradition,
    tradition_known_in_window,
    world_records_mention_tradition,
)
from engine.m4.world_loader import LazyWorldLoader

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]
REPORT_PATH = pathlib.Path(__file__).resolve().parent / "r37-build-battery-2026-09-24.json"


def _branch(evidence_ids: list[str], known_in_window: bool | None) -> str:
    if evidence_ids:
        return "records_name_it"
    if known_in_window:
        return "condition_a"
    return "question_words_only"


def _later_tradition_turn(world_key: str, registry: dict) -> str:
    latest = max(
        (k for k in formation_world_keys(registry) if k != world_key),
        key=lambda k: (registry[k]["time_window"]["start"], k),
    )
    return f"What was your relationship with {registry[latest]['card_name']}?"


def _row(world_key: str, probe_id: str, message: str, world, registry: dict) -> dict:
    entry = registry[world_key]
    named_key = match_named_tradition(message, registry, exclude_world_key=world_key)
    named = registry[named_key] if named_key else None
    evidence_ids = world_records_mention_tradition(ev.repository_records_by_id(world.repository), named) if named else []
    known = tradition_known_in_window(entry, named) if named else None
    revealed = conversation_revealed_excerpts([], named, speaking_world_key=world_key) if named else []
    directive = _other_tradition_directive(evidence_ids, known_in_window=known, revealed_excerpts=revealed)
    expected = named["time_window"]["start"] <= entry["time_window"]["end"] if named else None
    return {
        "world": world_key,
        "probe_id": probe_id,
        "window": entry["time_window"],
        "probe": message,
        "named_tradition": named_key,
        "named_window": named["time_window"] if named else None,
        "known_in_window": known,
        "expected_under_r37_a": expected,
        "records_name_it": evidence_ids,
        "revealed_excerpts": revealed,
        "branch": _branch(evidence_ids, known),
        "honest_limit_sentence_in_directive": R26_HONEST_LIMIT_SENTENCE in directive,
        "directive": directive,
    }


def _summary(rows: list[dict]) -> dict:
    return {
        "probes": len(rows),
        "licensed_under_condition_a": sum(1 for r in rows if r["known_in_window"]),
        "matches_r37_a": sum(1 for r in rows if r["named_tradition"] and r["known_in_window"] == r["expected_under_r37_a"]),
        "branch_counts": {b: sum(1 for r in rows if r["branch"] == b) for b in ("records_name_it", "condition_a", "question_words_only")},
    }


def run() -> dict:
    registry = load_registry()
    loader = LazyWorldLoader()
    rows = []
    for world_key in formation_world_keys(registry):
        entry = registry[world_key]
        world, _timing = loader.load(
            world_key, package_dir=REPO_ROOT / entry["package"]["location"],
            expected_manifest_hash=entry["package"]["manifest_hash"],
        )
        rows.append(_row(world_key, "B-other-tradition", _other_tradition_turn(world_key, registry), world, registry))
        rows.append(_row(world_key, "C-later-tradition", _later_tradition_turn(world_key, registry), world, registry))
    by_probe = {p: [r for r in rows if r["probe_id"] == p] for p in ("B-other-tradition", "C-later-tradition")}
    return {
        "rulings": ["R37 (2026-09-23)", "R37-A (2026-09-23, asymmetric window)", "R37-B (2026-09-24)"],
        "summary": {p: _summary(r) for p, r in by_probe.items()},
        "rows": rows,
    }


def main():
    report = run()
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    for probe_id, summary in report["summary"].items():
        print(f"{probe_id}: {summary}")
    print(f"wrote {REPORT_PATH.relative_to(REPO_ROOT)}")
    real = report["summary"]["B-other-tradition"]
    every_row_matches = all(s["matches_r37_a"] == s["probes"] for s in report["summary"].values())
    return 0 if every_row_matches and real["licensed_under_condition_a"] == real["probes"] else 1


if __name__ == "__main__":
    sys.exit(main())
