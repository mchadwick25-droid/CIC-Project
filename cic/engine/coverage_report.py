#!/usr/bin/env python3
"""Mechanism coverage across the whole fleet - Tier 3, T3-B's fleet view.

gate_mechanism_coverage (gates.py) answers one world's question: is any
runtime mechanism inert here? That is the gate's job and it is deliberately
narrow - it reports only zero coverage, because no floor has been set.

This answers the question a floor has to be set FROM: what does coverage
actually look like across every world, including the partial cases a
zero-only gate is silent about? alexandria's 1-of-12 dated figures passes
the gate and is still the thinnest real coverage in the fleet; that fact
has to be visible before anyone picks a threshold.

Report only. Exits 0 always, writes nothing, calls no model. It is the
generated replacement for a table that was hand-counted when Tier 3 was
scoped - the point being that nobody should have to hand-count it again.

Usage:
  python cic/engine/coverage_report.py
  python cic/engine/coverage_report.py --world desert
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # cic/
sys.path.insert(0, str(HERE))

from mechanism_dependencies import DEPENDENCIES, coverage  # noqa: E402
from validate import parse_front_matter  # noqa: E402
from worlds import WORLDS as _W  # noqa: E402

# One world authority: worlds.py, same as every other builder in this engine.
RECORD_DIRS = {k: w["records_dir"] for k, w in _W.items()}


def load(records_dir: Path) -> dict:
    """One world's records, keyed by id - the shape run_gates.py assembles."""
    records = {}
    for p in sorted(records_dir.rglob("*.md")):
        rec = parse_front_matter(p)
        if rec:
            records[rec["id"]] = rec
    return records


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--world", help="single world key (default: all)")
    args = ap.parse_args()

    keys = sorted(RECORD_DIRS)
    if args.world:
        if args.world not in RECORD_DIRS:
            raise SystemExit(f"[coverage] unknown world {args.world!r}")
        keys = [args.world]

    labels = [d.label for d in DEPENDENCIES]
    width = max(len(k) for k in keys) + 2
    colw = max(len(x) for x in labels) + 2

    print("MECHANISM COVERAGE - satisfying / of type\n")
    print("world".ljust(width) + "".join(x.ljust(colw) for x in labels))
    print("-" * (width + colw * len(labels)))

    inert_cells = 0
    for key in keys:
        rows = coverage(load(ROOT / "records" / RECORD_DIRS[key]))
        cells = []
        for _dep, n_sat, n_type in rows:
            mark = "" if n_sat else "  INERT"
            if not n_sat:
                inert_cells += 1
            cells.append(f"{n_sat}/{n_type}{mark}".ljust(colw))
        print(key.ljust(width) + "".join(cells))

    total = len(keys) * len(DEPENDENCIES)
    print(f"\n{inert_cells} of {total} (world x mechanism) cell(s) inert "
          f"across {len(keys)} world(s)")
    if inert_cells:
        print("\nAn inert cell means the mechanism runs and finds nothing to "
              "work with.\nRun run_gates.py --world <world> for the specific "
              "consequence of each.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
