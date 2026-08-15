#!/usr/bin/env python3
"""Run the gates over a world's records in the clean system.

Carried from the old tree's gate runner at the clean-room setup.
gates.py is the proven gate module carried whole - the checks
that actually execute are the one part of the old system this rebuild
exists to preserve.

  python cic/engine/run_gates.py --world syriac
  python cic/engine/run_gates.py --world syriac --voice-material FILE
  python cic/engine/run_gates.py --selftest
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # cic/
sys.path.insert(0, str(HERE))

import gates as core  # noqa: E402
from validate import parse_front_matter  # noqa: E402

GATES = {
    "referential": lambda r, vm: core.gate_referential_integrity(r),
    "reciprocity": lambda r, vm: core.gate_reciprocity(r),
    "completion": lambda r, vm: core.gate_field_completion(r),
    "narratability": lambda r, vm: core.gate_figure_narratability(r, vm),
    "quote_recording": lambda r, vm: core.gate_quote_fidelity_recording(r),
    "sentinel": lambda r, vm: core.gate_no_sentinel_conditions(r),
    "discovery_instrument": lambda r, vm: core.gate_discovery_instrument(r),
    "priority_review": lambda r, vm: core.gate_priority_review_trigger(r),
    "alias_safety": lambda r, vm: core.gate_alias_safety(r, vm),
    "distribution_health": lambda r, vm: core.gate_distribution_health(r),
    "confidence_source_crosscheck":
        lambda r, vm: core.gate_confidence_source_crosscheck(r),
    "mechanism_coverage": lambda r, vm: core.gate_mechanism_coverage(r),
}


BASELINE_PATH = HERE / "gate_baseline.json"


def load_records(records_dir: Path) -> dict:
    records = {}
    for p in sorted(records_dir.rglob("*.md")):
        rec = parse_front_matter(p)
        records[rec["id"]] = rec
    return records


def gate_counts(records: dict, vm: str = "") -> dict:
    """{gate_name: violation count} - advisory findings excluded.

    The ratchet's unit. Advisory entries are split out here exactly as the
    printing path splits them, so a gate reporting behind _NOTE_PREFIX
    (mechanism_coverage today) can never trip the check - which is what
    keeps the advisory decision of 2026-08-15 true in CI and not just at
    the console.
    """
    out = {}
    for name, fn in GATES.items():
        violations, _notes = core.split_alias_reports(fn(records, vm))
        out[name] = len(violations)
    return out


def run_records(records_dir: Path, voice_material: str) -> int:
    records = load_records(records_dir)
    vm = Path(voice_material).read_text(encoding="utf-8") if voice_material else ""
    total = 0
    advisory_total = 0
    for name, fn in GATES.items():
        v = fn(records, vm)
        v, notes = core.split_alias_reports(v)
        total += len(v)
        advisory_total += len(notes)
        print(f"## {name}: {len(v)} violation(s)"
              + (f" (+{len(notes)} advisory)" if notes else ""))
        for x in v:
            print(" -", x)
        # Advisory findings are PRINTED, not just counted. split_alias_reports
        # has always documented them as "printed but never counted"; this
        # runner counted them and printed nothing, so the whole advisory
        # channel was write-only - a gate could report a real finding and the
        # operator would see a bare number. Fixed here so the channel is
        # usable by any gate that needs to report without blocking
        # (mechanism_coverage is the first).
        for x in notes:
            # "~" already marks the line advisory; the in-string prefix the
            # gate used to route it here would just repeat that.
            print(" ~", x[len(core._NOTE_PREFIX):].lstrip())
    print(f"\nTOTAL: {total} violation(s)"
          + (f", {advisory_total} advisory" if advisory_total else "")
          + f" across {len(records)} records")
    return 0


def _fleet_counts() -> dict:
    """{world_key: {gate: count}} across every world worlds.py declares."""
    from worlds import WORLDS
    return {
        key: gate_counts(load_records(ROOT / "records" / w["records_dir"]))
        for key, w in sorted(WORLDS.items())
    }


def check_against_baseline() -> int:
    """A RATCHET, not an absolute floor - the CI mode.

    The six built worlds carry ~194 violations between them, every one of
    them pre-existing and none of them introduced by the change under test.
    A runner that exits non-zero on any violation would be red on its first
    run and every run after, and a permanently-red check is one people learn
    to ignore - worse than no check, because it also launders real
    regressions into familiar noise.

    So this fails on REGRESSION only: a gate whose count rose above the
    committed baseline for that world, or a world with no baseline at all.
    Existing violations are recorded, visible, and do not block; new ones
    cannot land silently. Improvements are reported and never fail - but the
    baseline is not lowered automatically, because a count that drops on its
    own and is then quietly re-consumed is exactly the drift a ratchet
    exists to stop. Lowering it is a deliberate --update-baseline commit.
    """
    if not BASELINE_PATH.exists():
        print(f"no baseline at {BASELINE_PATH.name} - "
              f"run: python cic/engine/run_gates.py --update-baseline")
        return 1

    baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))["worlds"]
    current = _fleet_counts()

    regressions, unbaselined, improvements = [], [], []
    for world, gates_now in current.items():
        if world not in baseline:
            unbaselined.append(world)
            continue
        for gate, n in sorted(gates_now.items()):
            was = baseline[world].get(gate)
            if was is None:
                regressions.append(f"{world}/{gate}: {n} (no baseline for "
                                   f"this gate - new gate needs a baseline)")
            elif n > was:
                regressions.append(f"{world}/{gate}: {was} -> {n} (+{n - was})")
            elif n < was:
                improvements.append(f"{world}/{gate}: {was} -> {n}")

    for world, gates_now in sorted(current.items()):
        total = sum(gates_now.values())
        mark = "  NO BASELINE" if world in unbaselined else ""
        print(f"{world:<22}{total:>4} violation(s){mark}")

    if improvements:
        print(f"\n{len(improvements)} improvement(s) - baseline not lowered "
              f"automatically; commit them with --update-baseline:")
        for x in improvements:
            print("  +", x)

    if unbaselined:
        print(f"\n{len(unbaselined)} world(s) with no recorded baseline: "
              f"{', '.join(unbaselined)}")
        print("  A new world must have its gate state recorded, not inherited "
              "silently. Run --update-baseline and commit the result.")

    if regressions:
        print(f"\nFAIL: {len(regressions)} gate(s) worse than baseline")
        for x in regressions:
            print("  -", x)
        return 1

    if unbaselined:
        return 1
    print("\nOK: no gate is worse than its recorded baseline")
    return 0


def update_baseline() -> int:
    current = _fleet_counts()
    blob = {
        "note": "Per-world, per-gate violation counts as of the date below - "
                "the ratchet floor for run_gates.py --check. Advisory "
                "findings (_NOTE_PREFIX) are excluded by construction and "
                "can never trip the check. Regenerate deliberately, never to "
                "make a failing run pass: the gate-integrity rule at the top "
                "of gates.py governs this file too.",
        "generated": "2026-08-15",
        "worlds": current,
    }
    BASELINE_PATH.write_text(
        json.dumps(blob, indent=1, sort_keys=False) + "\n", encoding="utf-8")
    total = sum(sum(g.values()) for g in current.values())
    print(f"wrote {BASELINE_PATH.name}: {len(current)} world(s), "
          f"{total} violation(s) recorded as the ratchet floor")
    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--world")
    p.add_argument("--records")
    p.add_argument("--voice-material")
    p.add_argument("--check", action="store_true",
                   help="CI mode: fail if any gate is worse than its "
                        "recorded baseline (exit 1). Existing violations "
                        "do not fail.")
    p.add_argument("--update-baseline", action="store_true",
                   help="rewrite gate_baseline.json from the current fleet "
                        "state - a deliberate, committed act")
    args = p.parse_args()
    if args.update_baseline:
        return update_baseline()
    if args.check:
        return check_against_baseline()
    if args.records:
        return run_records(Path(args.records), args.voice_material)
    if args.world:
        return run_records(ROOT / "records" / args.world, args.voice_material)
    p.error("pass --world, --records, --check or --update-baseline")


if __name__ == "__main__":
    sys.exit(main())
