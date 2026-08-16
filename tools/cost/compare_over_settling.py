#!/usr/bin/env python3
"""A/B the folded OVER_SETTLING check against the two-stage pair it replaces.

    cd cic/runtime
    PYTHONPATH=. python3 ../../tools/cost/compare_over_settling.py

Replays real representative turns from the recorded session logs
(`transcripts/events/*.jsonl`) through both paths and diffs the verdicts.
Spends money - roughly $0.011 per turn, so ~$0.55 for a 48-turn replay.
`--dry-run` prints the plan and spends nothing; `--limit N` caps the replay.

WHY THIS EXISTS RATHER THAN A COST ARGUMENT
-------------------------------------------
The fold is justified on measurement: the blind screen fires on 82% of turns
(95% CI 68-90%) against a 60% break-even, so it costs more than it turns
away, and every screen false-negative is a miss the adjudicator never sees.

But the check it replaces carries a warning about exactly this kind of
change, in OVER_SETTLING_SCREEN_PROMPT's own words: this check "was first
tried as one signal among ten in a general drift monitor and caught nothing,
because a turn that reads well overall reads as clean." Cost is not a reason
to ship a check that finds less. So the folded call has to be shown to find
at least what the pair finds, on real traffic, before the flag flips.

WHAT THE NUMBERS MEAN
---------------------
    BOTH CONFIRMED    the fold reproduces a finding the pair made
    FOLD ONLY         a finding the blind screen missed - the prize, and the
                      only direct evidence of the screen's false-negative
                      rate that can exist, since a screened-out turn leaves
                      no trace in production
    PAIR ONLY         a finding the fold lost - the risk, and the number
                      that should block the flag if it is not near zero
    BOTH CLEAR        agreement on an ordinary turn

Ordinary traffic is a low-signal setting: measured confirm rate is ~28% of
flagged turns, so expect a handful of findings across a 48-turn replay, not
dozens. A replay that produces no findings on either side has not tested
anything - say so rather than reading it as agreement.

READ THIS BEFORE TRUSTING A SINGLE RUN
--------------------------------------
Measured 2026-08-16, and it invalidates the naive reading of this tool:
**neither path is deterministic.** Replaying the same three turns that
scored PAIR ONLY in the first 56-turn run produced, on two further draws:

    turn   run 1        run 2        run 3
      13   PAIR ONLY    BOTH CLEAR   BOTH CLEAR
      30   PAIR ONLY    BOTH CLEAR   PAIR ONLY
      48   PAIR ONLY    BOTH CLEAR   FOLD ONLY

Same inputs, same code, three different verdicts. So a single-draw diff
cannot distinguish "the fold lost a finding" from "the pair produced a
finding it would not reproduce" - and the PAIR ONLY count, which is what
gates the flag, is exactly the number that instability corrupts.

That is a property of the check as it exists in production, not of the
fold: the two-stage path is equally unstable, which means today a
participant's turn gets a correction or does not, partly at random. The
measured 82% fire rate and 28% confirm rate are single draws too.

Until this tool replays each turn N times per path and compares
distributions rather than draws, treat its verdict as a smoke test: a large
PAIR ONLY count is worth investigating, a small one is noise, and neither
should flip settings.over_settling_folded on its own.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import sys
from collections import Counter

FACILITATOR = "facilitator"


def sessions(pattern: str) -> list[tuple[str, list[str]]]:
    """(world_id, [representative turn texts]) per recorded session."""
    out = []
    for path in sorted(glob.glob(pattern)):
        world_id, turns = None, []
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            payload = event.get("payload") or {}
            if event.get("type") == "session_started":
                world_id = payload.get("world_id")
            elif event.get("type") == "spoken_message":
                if payload.get("name") not in (None, FACILITATOR):
                    text = (payload.get("text") or "").strip()
                    if text:
                        turns.append(text)
        if world_id and turns:
            out.append((world_id, turns))
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", default="transcripts/events/*.jsonl")
    ap.add_argument("--limit", type=int, default=0, help="cap turns replayed")
    ap.add_argument("--only", default="", help="replay only these 1-based turn "
                    "indices (comma-separated) - for diagnosing disagreements "
                    "without paying for the whole replay again")
    ap.add_argument("--json-out", default="", help="write full untruncated "
                    "detail here; the printed report truncates, and a "
                    "disagreement cannot be diagnosed from 150 characters")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    key = os.environ.get("CIC_ANTHROPIC_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("set CIC_ANTHROPIC_KEY (or ANTHROPIC_API_KEY)")
    os.environ["ANTHROPIC_API_KEY"] = key

    found = sessions(args.events)
    plan = [(w, t) for w, turns in found for t in turns]
    if args.only:
        want = {int(x) for x in args.only.replace(" ", "").split(",") if x}
        plan = [(w, t) for i, (w, t) in enumerate(plan, 1) if i in want]
    if args.limit:
        plan = plan[:args.limit]
    if not plan:
        sys.exit(f"no representative turns found in {args.events}")

    worlds = Counter(w for w, _ in plan)
    print(f"{len(plan)} turns from {len(found)} session(s): "
          + ", ".join(f"{w}x{n}" for w, n in worlds.items()))
    print(f"estimated spend ~${len(plan) * 0.011:.2f}")
    if args.dry_run:
        print("\n--dry-run: nothing sent.")
        return

    from app.graph.nodes import (_adjudicate_over_settling, _folded_over_settling,
                                 _screen_over_settling)

    tally = Counter()
    disagreements = []
    records = []

    for i, (world_id, text) in enumerate(plan, 1):
        # --- the pair, exactly as production runs it today ---
        screened = _screen_over_settling(text)
        if screened is None:
            pair = None                     # screen cleared: never adjudicated
        else:
            verdict = _adjudicate_over_settling(text, world_id, screened)
            pair = verdict if isinstance(verdict, str) and verdict else None

        # --- the fold ---
        outcome = _folded_over_settling(text, world_id)
        fold = outcome[1] if isinstance(outcome, tuple) else None
        fold_candidates = outcome[0] if isinstance(outcome, tuple) else None

        if pair and fold:
            bucket = "BOTH CONFIRMED"
        elif fold and not pair:
            bucket = "FOLD ONLY"
        elif pair and not fold:
            bucket = "PAIR ONLY"
        else:
            bucket = "BOTH CLEAR"
        tally[bucket] += 1
        tally["screen_fired"] += screened is not None

        if bucket != "BOTH CLEAR":
            disagreements.append((i, world_id, bucket, text, pair, fold,
                                  screened is not None))
        records.append({"i": i, "world_id": world_id, "bucket": bucket,
                        "turn": text, "screen_fired": screened is not None,
                        "screen_candidates": screened,
                        "pair_limit": pair, "fold_limit": fold,
                        "fold_candidates": fold_candidates})
        print(f"  [{i}/{len(plan)}] {world_id[:22]:24}{bucket}")

    n = len(plan)
    print(f"\n{'':4}{'bucket':18}{'n':>5}{'share':>9}")
    for bucket in ("BOTH CONFIRMED", "FOLD ONLY", "PAIR ONLY", "BOTH CLEAR"):
        c = tally[bucket]
        print(f"{'':4}{bucket:18}{c:5}{c/n:9.0%}")
    print(f"\n  blind screen fired on {tally['screen_fired']}/{n} "
          f"({tally['screen_fired']/n:.0%})")

    if disagreements:
        print("\nDETAIL")
        for i, world, bucket, text, pair, fold, fired in disagreements:
            print(f"\n  [{i}] {world}  {bucket}  (screen fired: {fired})")
            print(f"      turn: {text[:110]}...")
            if pair:
                print(f"      pair: {pair[:150]}")
            if fold:
                print(f"      fold: {fold[:150]}")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(records, fh, indent=2, ensure_ascii=False)
        print(f"\n  full detail written to {args.json_out}")

    print("\nVERDICT")
    findings = tally["BOTH CONFIRMED"] + tally["FOLD ONLY"] + tally["PAIR ONLY"]
    if findings == 0:
        print("  NO FINDINGS ON EITHER SIDE. This replay has not tested the")
        print("  fold - it has only shown both paths agree that ordinary")
        print("  traffic is ordinary. Do not read it as agreement. Replay")
        print("  more turns, or turns known to carry the defect.")
    elif tally["PAIR ONLY"] > 0:
        print(f"  BLOCKED on this draw. The fold scored {tally['PAIR ONLY']} fewer "
              "finding(s) than the pair.")
        print("  Before treating that as a regression, re-run those turns with")
        print("  --only: neither path is deterministic (see the module header),")
        print("  and findings that do not reproduce are variance, not loss.")
        print("  Cost is not a reason to ship a check that finds less. Read the")
        print("  detail above: if Phase 1 failed to enumerate the claim, the")
        print("  enumeration instruction is what needs work, not the ruling.")
    else:
        print(f"  The fold reproduced {tally['BOTH CONFIRMED']} of the pair's "
              f"{tally['BOTH CONFIRMED']} finding(s) and lost none.")
        if tally["FOLD ONLY"]:
            print(f"  It also found {tally['FOLD ONLY']} the blind screen missed - "
                  "direct evidence")
            print("  of the screen false-negative rate, which cannot be measured")
            print("  any other way once a turn has been screened out.")
        print(f"\n  On {n} turns this is suggestive, not conclusive - findings are")
        print("  sparse in ordinary traffic. Weigh it as evidence, not proof.")


if __name__ == "__main__":
    main()
