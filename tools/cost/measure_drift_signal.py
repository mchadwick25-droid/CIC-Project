#!/usr/bin/env python3
"""Measure drift_detection's real fire rate on ordinary traffic - never
measured before this script.

Prompted by the "cut drift_detection to reach $0.30" line in the cost
review. Before answering that, one architectural fact changes the question:
drift_detection is not a stylistic nice-to-have sharing a line item with
relational_safety by coincidence. Reading app/graph/nodes.py's
_detect_drift_signal_impl: FABRICATION is one of eleven signals bundled into
this single call, and it is the ONLY place in the whole codebase that
screens for fabrication on ordinary conversation - the source-fed
_adjudicate_fabrication second pass never runs unless this blind first pass
flags it first. Cutting drift_detection does not trim a style monitor; it
deletes the system's only defense against Facilitator Governance Section
11's "cardinal failure" - a real author misattributed a saying, an invented
scene delivered to a participant as witness.

Despite that, nobody has ever measured what this call actually catches on
real traffic. app/drift_signal_logging.py exists for exactly this and has
never been wired into a capture run - the 2026-08-16 48-turn sample recorded
[llm_usage] and [over_settling_decision] but not [drift_signal] (see
run_traffic_sample.py's captured-logger list). This replays the SAME 48
recorded turns from that sample - already paid for once, at ~$0.0022/turn
for this call alone - through _detect_drift_signal directly, so the fire
rate and signal breakdown cost pocket change to produce.

    cd cic/runtime
    PYTHONPATH=. python3 ../../tools/cost/measure_drift_signal.py

Spends ~$0.0022 x 48 turns =~ $0.11. --dry-run prints the plan and spends
nothing.
"""
from __future__ import annotations

import argparse
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compare_over_settling import sessions          # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", default="transcripts/events/*.jsonl")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    key = os.environ.get("CIC_ANTHROPIC_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("set CIC_ANTHROPIC_KEY (or ANTHROPIC_API_KEY)")
    os.environ["ANTHROPIC_API_KEY"] = key

    plan = [(w, t) for w, turns in sessions(args.events) for t in turns]
    if args.limit:
        plan = plan[:args.limit]
    if not plan:
        sys.exit(f"no representative turns found in {args.events}")

    print(f"{len(plan)} turns; estimated spend ~${len(plan) * 0.0022:.2f}")
    if args.dry_run:
        print("\n--dry-run: nothing sent.")
        return

    from app.graph.nodes import _detect_drift_signal

    signals = Counter()
    severities = Counter()
    fabrication_turns = []
    clean = 0

    for i, (world_id, text) in enumerate(plan, 1):
        signal = _detect_drift_signal(text, world_id=world_id)
        if signal is None:
            clean += 1
            print(f"  [{i}/{len(plan)}] {world_id[:24]:26} clean")
            continue
        signals[signal.signal_type] += 1
        severities[signal.severity] += 1
        if signal.signal_type == "fabrication":
            fabrication_turns.append((i, world_id, text, signal))
        print(f"  [{i}/{len(plan)}] {world_id[:24]:26} "
              f"{signal.signal_type:22}{signal.severity}")

    n = len(plan)
    fired = n - clean
    print(f"\n{n} turns, {fired} fired ({fired/n:.0%}), {clean} clean")

    print(f"\nSIGNAL BREAKDOWN")
    for sig, count in signals.most_common():
        print(f"  {sig:24}{count:4}  ({count/n:.0%} of all turns)")

    print(f"\nSEVERITY")
    for sev in ("high", "medium", "low"):
        c = severities.get(sev, 0)
        print(f"  {sev:8}{c:4}")

    print(f"\nFABRICATION - the signal with no other detector in the system")
    print(f"  fired on {len(fabrication_turns)}/{n} turns "
          f"({len(fabrication_turns)/n:.0%})")
    for i, world_id, text, signal in fabrication_turns:
        print(f"\n  [{i}] {world_id}  severity={signal.severity}")
        print(f"      turn: {text[:110]}...")
        print(f"      finding: {signal.description[:200]}")

    non_fab = fired - len(fabrication_turns)
    print(f"\nVERDICT")
    print(f"  Of {fired} total findings, {len(fabrication_turns)} were fabrication "
          f"and {non_fab} were one of the other ten (style/shape/stance) signals.")
    if fabrication_turns:
        print("  Cutting drift_detection entirely removes both - including every")
        print("  fabrication catch above. Read the findings printed above before")
        print("  deciding anything: a real misattribution here is the strongest")
        print("  argument against the cut this sample can produce.")
    else:
        print("  No fabrication fired in this sample. That does not mean the")
        print("  detector isn't earning its cost elsewhere - drift_detection's own")
        print("  design note observes fabrication rates are low and the cost of a")
        print("  miss is not - but it does mean this sample alone cannot show you")
        print("  a save. A larger or adversarial sample would be needed to bound")
        print("  the miss rate before cutting this on the strength of one draw.")


if __name__ == "__main__":
    main()
