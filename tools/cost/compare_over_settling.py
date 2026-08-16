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

Use --reps 3 or more. A single draw is a smoke test, not a measurement.

THE --reps 3 RESULT (56 turns, 2026-08-16) - see samples/
--------------------------------------------------------
                                pair      fold
    total confirmations           27        40
    turns confirmed on EVERY draw  2         2
    turns confirmed on SOME draws 16        24
    self-consistency             71%       57%

    stable regressions (pair always / fold never): 0
    stable gains       (fold always / pair never): 1

No stable regressions - the three that blocked the single-draw run were
variance, as suspected. But the honest reading is not "the fold wins": the
two paths have the SAME stable core of 2 turns, and the fold's extra 13
confirmations per draw come almost entirely from turns it does not confirm
reliably. It finds more by being noisier, and it is less self-consistent
than the check it would replace (57% vs 71%).

The dominant finding is not about the fold at all: **this check does not
reproduce itself on 29-43% of turns**, whichever variant runs. A
participant's turn gets a correction or does not, partly at random, and the
82% fire rate and 28% confirm rate the whole cost case rests on are single
draws of a process this noisy.

Likeliest cause, and the cheapest thing to test next: `get_monitoring_llm`
sets no `temperature` at all, so every classifier in the system - both
over-settling stages, relational safety, drift, frame-breaker - runs at the
API default. Pin it and re-run this tool before deciding anything about the
fold.

TEMPERATURE PINNED, RE-RUN (56 turns x 3 draws, 2026-08-16) - see samples/
--------------------------------------------------------------------------
                                  pair            fold
                            default temp0   default temp0
    total confirmations          27    22      40    44
    turns confirmed EVERY draw    2     3       2     6
    turns that flip between draws16    12      24    19
    self-consistency            71%   79%     57%   66%
    stable regressions                         0     1
    stable gains                               1     4

Pinning temperature to 0 helped both paths and settled neither: a third of
the turns still flip. It sharpened the comparison rather than resolving it -
with less noise the fold shows MORE stable findings (6 vs 3) and 4 stable
gains, and one stable regression, turn 48, the same turn that failed the
original single-draw run.

VERDICT ON THE FOLD: rejected, on turn 48 - see diagnose_over_settling.py
------------------------------------------------------------------------
That regression was diagnosed rather than argued about. The fold's Phase 1
enumerates the disputed claim verbatim on every draw; Phase 2 clears it on
every draw, always by the same move ("speaks from inside a household, does
not claim it as universal"). The two paths saw 37 of 37 IDENTICAL retrieved
chunks, so this is not retrieval drift.

What separates them is the Concern each path writes for that same claim. The
blind screen has read no sources, so all it can name is that the claim is
stated more firmly than a contested thing should be - the question the
adjudicator must then rule on against the record. The fold has already read
the sources when it writes Phase 1, and frames its concern as "is this
universal across households?", which has a stock answer that always clears.

The screen's value is therefore not the filtering the cost case measured -
at an 82% fire rate it demonstrably fails at that - it is BLINDNESS, and
blindness cannot be restored by instruction inside one forward pass that
reads the sources before it writes a word. The flag stays off, and the
~$250/yr the fold would save is not worth one real finding lost per 56 turns
plus a less self-consistent check.
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
    ap.add_argument("--reps", type=int, default=1, help="draws per path per "
                    "turn. Neither path is deterministic, so --reps 1 is a "
                    "smoke test; 3+ is a measurement.")
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
    print(f"{args.reps} draw(s) per path per turn")
    print(f"estimated spend ~${len(plan) * 0.011 * args.reps:.2f}")
    if args.dry_run:
        print("\n--dry-run: nothing sent.")
        return

    from app.graph.nodes import (_adjudicate_over_settling, _folded_over_settling,
                                 _screen_over_settling)

    per_turn = []

    for i, (world_id, text) in enumerate(plan, 1):
        pair_hits, fold_hits, pair_limits, fold_limits = 0, 0, [], []
        screen_fired = 0
        for _ in range(args.reps):
            screened = _screen_over_settling(text)
            screen_fired += screened is not None
            pair = None
            if screened is not None:
                verdict = _adjudicate_over_settling(text, world_id, screened)
                pair = verdict if isinstance(verdict, str) and verdict else None
            if pair:
                pair_hits += 1
                pair_limits.append(pair)

            outcome = _folded_over_settling(text, world_id)
            fold = outcome[1] if isinstance(outcome, tuple) else None
            if fold:
                fold_hits += 1
                fold_limits.append(fold)

        per_turn.append({"i": i, "world_id": world_id, "turn": text,
                         "reps": args.reps, "screen_fired": screen_fired,
                         "pair_hits": pair_hits, "fold_hits": fold_hits,
                         "pair_limits": pair_limits, "fold_limits": fold_limits})
        print(f"  [{i}/{len(plan)}] {world_id[:22]:24}"
              f"pair {pair_hits}/{args.reps}   fold {fold_hits}/{args.reps}")

    records = per_turn
    reps = args.reps

    def unstable(hits):
        return 0 < hits < reps

    pair_unstable = sum(unstable(t["pair_hits"]) for t in per_turn)
    fold_unstable = sum(unstable(t["fold_hits"]) for t in per_turn)
    pair_total = sum(t["pair_hits"] for t in per_turn)
    fold_total = sum(t["fold_hits"] for t in per_turn)
    # "Stable" = the path agreed with itself on every draw. A majority rule
    # would hide exactly the instability this is measuring.
    pair_stable = [t for t in per_turn if t["pair_hits"] == reps]
    fold_stable = [t for t in per_turn if t["fold_hits"] == reps]
    regressions = [t for t in per_turn if t["pair_hits"] == reps and t["fold_hits"] == 0]
    gains = [t for t in per_turn if t["fold_hits"] == reps and t["pair_hits"] == 0]

    n = len(plan)
    print(f"\nFINDINGS ACROSS {reps} DRAW(S) OF {n} TURNS")
    print(f"{'':4}{'':22}{'pair':>10}{'fold':>10}")
    print(f"{'':4}{'total confirmations':22}{pair_total:10}{fold_total:10}")
    print(f"{'':4}{'mean per draw':22}{pair_total/reps:10.1f}{fold_total/reps:10.1f}")
    print(f"{'':4}{'turns confirmed always':22}{len(pair_stable):10}{len(fold_stable):10}")
    print(f"{'':4}{'turns confirmed sometimes':22}{pair_unstable:10}{fold_unstable:10}")

    print("\nSELF-CONSISTENCY (same turn, same code, repeated draws)")
    for label, uns in (("pair", pair_unstable), ("fold", fold_unstable)):
        agree = n - uns
        print(f"    {label}: agreed with itself on {agree}/{n} turns ({agree/n:.0%}); "
              f"flipped on {uns}")

    print("\nSTABLE DISAGREEMENTS (the only ones worth acting on)")
    print(f"    pair always / fold never : {len(regressions)}   <- regressions")
    print(f"    fold always / pair never : {len(gains)}   <- gains")
    for label, rows in (("REGRESSION", regressions), ("GAIN", gains)):
        for t in rows:
            print(f"\n  {label} [{t['i']}] {t['world_id']}")
            print(f"      turn: {t['turn'][:110]}...")
            src = t["pair_limits"] or t["fold_limits"]
            if src:
                print(f"      limit: {src[0][:170]}")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(records, fh, indent=2, ensure_ascii=False)
        print(f"\n  full detail written to {args.json_out}")

    print("\nVERDICT")
    if reps < 3:
        print(f"  {reps} draw(s) per path is a smoke test, not a measurement -")
        print("  neither path is deterministic. Re-run with --reps 3.")
    elif pair_total == 0 and fold_total == 0:
        print("  NO FINDINGS ON EITHER SIDE across every draw. This replay has")
        print("  not tested the fold. Replay more turns, or turns known to")
        print("  carry the defect.")
    elif regressions:
        print(f"  BLOCKED. {len(regressions)} turn(s) where the pair confirmed on every")
        print("  draw and the fold on none. That is a stable loss, not variance.")
        print("  Read the limits above: if the fold's Phase 1 never enumerated")
        print("  the claim, the enumeration instruction needs work, not the ruling.")
    else:
        print(f"  No stable regressions. The fold confirmed {fold_total} times across")
        print(f"  {reps} draws against the pair's {pair_total}, and found {len(gains)} finding(s)")
        print("  the pair never made on any draw.")
        worse = max(pair_unstable, fold_unstable)
        if worse > n * 0.1:
            print(f"\n  BUT both paths are unstable ({pair_unstable} and {fold_unstable} turns flip")
            print("  between draws). A check that answers differently on the same")
            print("  turn is a quality problem in its own right, independent of")
            print("  which variant ships - worth deciding on before the flag.")


if __name__ == "__main__":
    main()
