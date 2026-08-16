#!/usr/bin/env python3
"""Measure turns-per-hour from session event logs.

Every cost figure in the review is a $/turn measurement multiplied by an
assumed 12 turns/hour. The multiplier was never measured, and it moves the
headline further than any lever in the review: at 20 turns/hour the whole
apparatus-cutting programme still lands above the $0.30 target.

`app/graph/events.py` already records what is needed - every event carries an
ISO timestamp, and consecutive `participant_message` events bracket exactly
one conversational turn. This turns those files into the number.

    python3 tools/cost/analyze_pacing.py cic/runtime/transcripts/events/*.jsonl

WHAT THIS CAN AND CANNOT MEASURE
--------------------------------
One turn's wall clock is three parts:

    system      participant sends -> representative's words exist
    tail        post-response classifiers still running (drift, grounding)
    human       reader finishes, thinks, and types the next question

The first two are machine time and are measured exactly here. **The third
requires a human and cannot be derived from any log a script produced.** On a
scripted run it is ~0 by construction, so this script detects that and reports
the result as a FLOOR - the fastest a conversation could physically go - not
as a pacing measurement.

Reading time is estimated, not measured: response length in words at a
configurable words-per-minute. That converts an unknown into a bounded one,
and it is the honest half of the human component. Composition time is left
where it belongs, as the explicit unknown.

Makes no API calls.
"""
from __future__ import annotations

import argparse
import glob
import json
import statistics
import sys
from datetime import datetime

FACILITATOR = "facilitator"


def load(path: str) -> list[dict]:
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return out


def ts(event: dict) -> datetime | None:
    raw = event.get("ts")
    try:
        return datetime.fromisoformat(raw) if raw else None
    except ValueError:
        return None


def turns_of(events: list[dict]) -> list[dict]:
    """One record per participant turn, with its timing decomposed.

    A turn opens at a `participant_message` and closes at the next one. The
    representative's reply is the first non-facilitator `spoken_message`
    inside it - facilitator lines are framing, not the answer being waited on.
    """
    events = sorted(events, key=lambda e: e.get("seq", 0))
    turns = []
    open_turn = None
    for ev in events:
        when = ts(ev)
        if when is None:
            continue
        kind = ev.get("type")
        if kind == "participant_message":
            if open_turn is not None:
                open_turn["next_ask"] = when
                turns.append(open_turn)
            open_turn = {"ask": when, "reply": None, "last": when,
                         "words": 0, "next_ask": None}
        elif open_turn is not None:
            open_turn["last"] = when
            if kind == "spoken_message":
                payload = ev.get("payload") or {}
                if payload.get("name") != FACILITATOR:
                    if open_turn["reply"] is None:
                        open_turn["reply"] = when
                    open_turn["words"] += len((payload.get("text") or "").split())
    if open_turn is not None and open_turn["next_ask"] is not None:
        turns.append(open_turn)
    return [t for t in turns if t["next_ask"] and t["reply"]]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("logs", nargs="+", help="session .jsonl event files (globs ok)")
    ap.add_argument("--wpm", type=float, default=220.0,
                    help="reading speed for the estimated reading component")
    ap.add_argument("--synthetic-threshold", type=float, default=1.0,
                    help="median human seconds below this means a scripted run")
    ap.add_argument("--cost-per-turn", type=float, default=0.03103,
                    help="measured $/turn (default: the 2026-08-16 sample) - "
                         "turns pacing into the $/hour the review reports")
    args = ap.parse_args()

    paths = sorted({p for pattern in args.logs for p in glob.glob(pattern)})
    if not paths:
        sys.exit("no event files matched")

    rows, all_turns = [], []
    for path in paths:
        turns = turns_of(load(path))
        if not turns:
            continue
        all_turns.extend(turns)
        rows.append((path.rsplit("/", 1)[-1][:12], len(turns), turns))

    if not all_turns:
        sys.exit("no completed turns found - a turn needs a reply and a "
                 "following question to be measurable")

    def secs(turn, a, b):
        return (turn[b] - turn[a]).total_seconds()

    system = [secs(t, "ask", "reply") for t in all_turns]
    tail = [max(0.0, secs(t, "reply", "last")) for t in all_turns]
    human = [max(0.0, secs(t, "last", "next_ask")) for t in all_turns]
    total = [secs(t, "ask", "next_ask") for t in all_turns]
    words = [t["words"] for t in all_turns]

    print(f"{len(all_turns)} measurable turns across {len(rows)} session(s)\n")
    print(f"{'session':14}{'turns':>7}{'median gap':>13}{'turns/hr':>10}")
    for name, count, turns in rows:
        gaps = [secs(t, "ask", "next_ask") for t in turns]
        med = statistics.median(gaps)
        print(f"{name:14}{count:7}{med:12.1f}s{3600/med:10.1f}")

    med_total = statistics.median(total)
    print(f"{'ALL':14}{len(all_turns):7}{med_total:12.1f}s{3600/med_total:10.1f}")

    print("\nWHERE THE TIME GOES (median seconds per turn)")
    for label, series in (("system  ask -> reply", system),
                          ("tail    post-response classifiers", tail),
                          ("human   read, think, type", human)):
        print(f"  {label:36}{statistics.median(series):7.1f}s")
    print(f"  {'TOTAL':36}{med_total:7.1f}s")

    med_words = statistics.median(words)
    read_s = med_words / args.wpm * 60
    print(f"\nREPLY LENGTH  median {med_words:.0f} words "
          f"-> ~{read_s:.0f}s to read at {args.wpm:.0f} wpm")

    med_human = statistics.median(human)
    synthetic = med_human < args.synthetic_threshold
    machine = statistics.median([s + t for s, t in zip(system, tail)])

    med_system = statistics.median(system)
    med_tail = statistics.median(tail)

    print("\nVERDICT")
    if synthetic:
        print(f"  SCRIPTED RUN - median human time {med_human:.2f}s. These turns were")
        print("  sent by a script with no reading or thinking, so this is NOT a")
        print("  pacing measurement. What it does establish is a hard floor:")
        print(f"\n  machine time per turn: {machine:.1f}s  ->  CEILING "
              f"{3600/machine:.1f} turns/hour")
        print("  No participant can go faster than the system answers.")
        # The tail is NOT additive with reading. Drift detection and the
        # groundedness checks run after the representative's words exist, so
        # they overlap the reader rather than delaying them; only whichever
        # is longer sets the pace. Summing them would inflate every estimate
        # below by the full tail.
        print(f"\n  Turn = wait for answer ({med_system:.0f}s) + max(reading, "
              f"post-response {med_tail:.0f}s) + compose.")
        print(f"  Reading estimated at {read_s:.0f}s ({med_words:.0f} words @ "
              f"{args.wpm:.0f} wpm); the post-response tail is absorbed by it.")
        print(f"\n  {'compose':>10}{'turn':>9}{'turns/hr':>10}{'$/hour':>10}"
              f"{'$/yr @1000h':>13}")
        for compose in (0, 15, 30, 60, 120, 240):
            turn_s = med_system + max(med_tail, read_s) + compose
            tph = 3600 / turn_s
            hourly = tph * args.cost_per_turn
            mark = "  <-- the assumed 12" if abs(tph - 12) < 0.6 else ""
            print(f"  {compose:9}s{turn_s:8.0f}s{tph:10.1f}{hourly:10.3f}"
                  f"{hourly*12000:13,.0f}{mark}")
        # Solve for the composition time the assumed rate implies, and say it
        # out loud - it is the assumption stated in units anyone can judge.
        implied = 300 - med_system - max(med_tail, read_s)
        print(f"\n  12 turns/hour means a 300s turn, which implies "
              f"{implied:.0f}s ({implied/60:.1f} min)")
        print("  of thinking and typing per question, every question. That is the")
        print("  assumption every cost figure in the review rests on. It is a")
        print("  claim about people, and it has never been checked against any.")
        print("\n  Composition time is the one unknown left, and no log written by a")
        print("  script can supply it. Run this again over real participant sessions.")
    else:
        print(f"  REAL PACING: median {med_total:.1f}s per turn -> "
              f"{3600/med_total:.1f} turns/hour.")
        print(f"  Human share {med_human:.0f}s ({100*med_human/med_total:.0f}%), "
              f"machine {machine:.0f}s ({100*machine/med_total:.0f}%).")
        lo = 3600 / statistics.quantiles(total, n=4)[2]
        hi = 3600 / statistics.quantiles(total, n=4)[0]
        print(f"  Interquartile range: {lo:.1f} to {hi:.1f} turns/hour.")
        rate = 3600 / med_total
        print(f"\n  At the measured ${args.cost_per_turn:.5f}/turn that is "
              f"${rate*args.cost_per_turn:.3f}/hour")
        print(f"  (${rate*args.cost_per_turn*12000:,.0f}/yr @1,000 h/mo), "
              f"IQR ${lo*args.cost_per_turn:.3f}-${hi*args.cost_per_turn:.3f}.")
        print("  Use this, not 12, everywhere the review says $/hour.")


if __name__ == "__main__":
    main()
