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


def run_records(records_dir: Path, voice_material: str) -> int:
    records = {}
    for p in sorted(records_dir.rglob("*.md")):
        rec = parse_front_matter(p)
        records[rec["id"]] = rec
    vm = Path(voice_material).read_text(encoding="utf-8") if voice_material else ""
    total = 0
    for name, fn in GATES.items():
        v = fn(records, vm)
        v, notes = core.split_alias_reports(v)
        total += len(v)
        print(f"## {name}: {len(v)} violation(s)"
              + (f" (+{len(notes)} documented-exception note(s))" if notes else ""))
        for x in v:
            print(" -", x)
    print(f"\nTOTAL: {total} violation(s) across {len(records)} records")
    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--world")
    p.add_argument("--records")
    p.add_argument("--voice-material")
    args = p.parse_args()
    if args.records:
        return run_records(Path(args.records), args.voice_material)
    if args.world:
        return run_records(ROOT / "records" / args.world, args.voice_material)
    p.error("pass --world or --records")


if __name__ == "__main__":
    sys.exit(main())
