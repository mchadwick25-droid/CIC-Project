#!/usr/bin/env python3
"""
T1 - Table Phase 1 cost model (2026-08-09): the 3-Representative table's
cost architecture, levers, and honest floor.

Grounded in the committed B-COST raw log
(Ministry/Technology/Pass2/baselines/cost_baseline_2026-07_raw.jsonl),
priced with the same dollars() as scripts/cost_baseline_runner.py -
reconciled against the report's own totals ($3.3924 / 689 calls) before
any figure below is trusted. Builds on Ministry/Technology/Pass3/
cost_floor_model.py (2026-07-30) rather than replacing it; where the two
differ it is because this model prices the S4.6/S4.7 governance additions
that landed AFTER both the baseline and the Pass 3 model.

NO LIVE API CALLS. Tags, same convention as Pass 3:
  [M] measured    - read off the committed raw log or the repo's own files
  [E] estimated   - measured token shapes + published pricing
  [S] speculative - reasoned but unvalidated

The one structural claim this model exists to state:

    cost per participant round = FIXED + (rep turns per round) x MARGINAL

Everything except the round-shape lever only moves MARGINAL by cents;
the round shape multiplies all of it.
"""

import collections
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RAW = os.path.join(REPO, "Ministry", "Technology", "Pass2", "baselines",
                   "cost_baseline_2026-07_raw.jsonl")

# (input, output, cache_write@5min, cache_read) $/MTok - standard rates,
# matching scripts/cost_baseline_runner.py PRICING_STANDARD. Intro sonnet
# pricing ($2/$10, ends 2026-08-31) is deliberately NOT used: it is not a
# planning basis.
SONNET = (3.00, 15.00, 3.75, 0.30)
HAIKU = (1.00, 5.00, 1.25, 0.10)
PRICING = {"claude-sonnet-5": SONNET, "claude-haiku-4-5-20251001": HAIKU}


def dollars(r):
    # The raw log's input_tokens INCLUDES cache tokens; uncached input =
    # input - cache_read - cache_write. This is the runner's own
    # convention - and the trap the 2026-07 run notes' "$0.38/turn table"
    # headline fell into (it prices ~2.0x high; see the T1 doc, finding 1).
    i, o, w, rd = PRICING[r["model"]]
    unc = (r["input_tokens"] - r["cache_read_input_tokens"]
           - r["cache_creation_input_tokens"])
    return (unc * i + r["output_tokens"] * o
            + r["cache_creation_input_tokens"] * w
            + r["cache_read_input_tokens"] * rd) / 1e6


def hdr(t):
    print("\n" + "=" * 76 + "\n" + t + "\n" + "=" * 76)


recs = [json.loads(l) for l in open(RAW)]
recs = [r for r in recs if r.get("kind") == "llm_call"]

total = sum(dollars(r) for r in recs)
assert abs(total - 3.3924) < 0.001, f"reconciliation FAILED: {total:.4f}"
print(f"[M] reconciliation gate: ${total:.4f} across {len(recs)} calls "
      f"(report: $3.3924 / 689) - OK")

# ---------------------------------------------------------------- SLICE
# C4 turns 1-8 are the REAL table rounds. Turn 0 is session start; turns
# 9-10 streamed the canned cap message with 0 LLM calls. The report's
# $0.1585/turn headline averages those two free capped turns in; the
# feasibility question must be asked of the uncapped number.
c4 = [r for r in recs if r["conversation"] == "C4_three_world_table"
      and 1 <= r["turn"] <= 8]
NT = 8
REPS = sum(1 for r in c4 if r["label"] == "main_response")  # 28 calls
# [M] report's length-ceiling reconstruction (split_retry_calls): 7 of the
# 28 main_response calls in C4 are hard-ceiling retries -> 21 real
# representative turns, retry spend $0.1765.
RETRIES, RETRY_USD = 7, 0.1765
REP_TURNS = REPS - RETRIES
RPT = REP_TURNS / NT

lab = collections.defaultdict(lambda: [0, 0.0])
for r in c4:
    lab[r["label"]][0] += 1
    lab[r["label"]][1] += dollars(r)
c4_total = sum(v[1] for v in lab.values())

hdr("MEASURED TABLE TURN, UNCAPPED [M]  (C4 turns 1-8; seating: "
    "house-church + desert + syriac)")
print(f"  ${c4_total:.4f} / {NT} rounds = ${c4_total/NT:.4f} per "
      f"participant round   ({REP_TURNS} rep turns = {RPT:.2f}/round, "
      f"+{RETRIES} ceiling retries)")
solo = [r for r in recs if r["conversation"] != "C4_three_world_table"
        and 1 <= r["turn"] <= 8]
solo_pt = sum(dollars(r) for r in solo) / 24
print(f"  solo comparison (C1-C3 turns 1-8): ${solo_pt:.4f}/turn "
      f"-> table = {c4_total/NT/solo_pt:.2f}x solo")
for k, v in sorted(lab.items(), key=lambda x: -x[1][1]):
    print(f"    {k:32s} {v[0]:3d} calls  ${v[1]:.4f}  "
          f"(${v[1]/NT:.4f}/round, {100*v[1]/c4_total:4.1f}%)")

# ------------------------------------------------------- DECOMPOSITION
hdr("DECOMPOSITION: FIXED + rep_turns x MARGINAL [M]")

gen_draft = (lab["main_response"][1] - RETRY_USD) / REP_TURNS
retry_ovh = RETRY_USD / REP_TURNS
retr = (lab["retrieval_filter_lexicon"][1]
        + lab["retrieval_filter_story"][1]) / REP_TURNS
gov_rep = (lab["drift_detection"][1] + lab["over_settling_screen"][1]
           + lab["over_settling_adjudication"][1]
           + lab["fabrication_adjudication"][1]) / REP_TURNS
sel_per_call = lab["turn_selector"][1] / lab["turn_selector"][0]
# selector runs before each speaker + once to end the round: reps+1 calls
marg = dict(generation=gen_draft, retry_overhead=retry_ovh,
            retrieval_filter=retr, governance=gov_rep,
            turn_selector=sel_per_call)
fixed = dict(
    participant_msg_governance=sum(lab[k][1] for k in (
        "frame_breaker", "relational_safety", "epistemology_bridge",
        "modern_term_bridge", "wind_down")) / NT,
    round_end_selector=sel_per_call,
)
M, F = sum(marg.values()), sum(fixed.values())
for k, v in marg.items():
    print(f"  MARGINAL/rep-turn  {k:24s} ${v:.4f}")
for k, v in fixed.items():
    print(f"  FIXED/round        {k:24s} ${v:.4f}")
print(f"  => MARGINAL ${M:.4f}/rep-turn, FIXED ${F:.4f}/round; "
      f"check: {F:.4f} + {RPT:.3f} x {M:.4f} = "
      f"${F + RPT*M:.4f}  (measured ${c4_total/NT:.4f})")

# ------------------------------------------------- POST-BASELINE DRIFT
hdr("WHAT THE BASELINE NO LONGER MEASURES (landed after 2026-07-26)")

# S3.4: LLM relevance vote GONE (evaluate_batch has no production caller;
# app/rag/pipeline.py runs the local cross-encoder + a guard-only Haiku
# vote that fires only when relevance-kept candidates carry an evaluable
# Do-Not-Retrieve-When). Pass 3's estimate for the live call, kept:
NC_PER_REP = 0.0020        # [E] at most lexicon+story guard votes
# S4.4a: direct-address detection now skips the selector call on
# addressed turns.  [E] modest; kept at face value below.
# S4.6/S4.7 ADDITIONS the baseline never saw, all Haiku, per round:
# convergence_check, manufactured_resolution_check, closing_synthesis_check,
# misattribution_check, vocab_drift_verdict, register_classification,
# repair classifier (per participant msg), citation_grounding (per rep turn).
NEW_TAIL_PER_ROUND = 0.016  # [E] ~6 small Haiku calls x ~$0.002-0.003
CITE_PER_REP = 0.0025       # [E] citation_grounding, Haiku, per rep turn
print(f"""  [-] S3.4 retrieval: ${retr:.4f}/rep-turn measured -> ~${NC_PER_REP:.4f} [E]
  [+] S4.6/S4.7 governance tail: +${NEW_TAIL_PER_ROUND:.4f}/round [E]
  [+] citation_grounding: +${CITE_PER_REP:.4f}/rep-turn [E]
  Net effect near zero: the new governance roughly eats the retrieval
  saving. The re-measure after PR #9 + the five world swaps is the only
  honest way to know the current number.""")

# --------------------------------------------------------- SCENARIOS
hdr("ARCHITECTURES  (standard pricing; $/hr at 24 / 16 / 10 rounds per hr)")

PACING = (24.0, 16.0, 10.0)


def show(name, f, m, rpt, note=""):
    pt = f + rpt * m
    hrs = "  ".join(f"${pt*t:5.2f}" for t in PACING)
    print(f"  {name:44s} ${pt:.4f}/round   {hrs}   {note}")
    return pt


print(f"  {'':44s} {'$/round':>8s}   {'24/hr':>6s} {'16/hr':>6s} {'10/hr':>6s}")
show("A0 measured baseline (2026-07-26) [M]", F, M, RPT)

# A1: code as of today [E] - S3.4 in, S4.6/S4.7 in
m1 = M - retr + NC_PER_REP + CITE_PER_REP
f1 = F + NEW_TAIL_PER_ROUND
show("A1 current code, pre-remeasure estimate [E]", f1, m1, RPT)

# A2: + lossless fixes: ceiling-retry prompt fix (halve, Pass3 A3,
# medium confidence), over-settling adjudication once per round
m2 = m1 - 0.5 * retry_ovh - 0.004
show("A2 + lossless fixes (retry, os-adjudication) [E]", f1, m2, RPT,
     "no participant-visible change")

# A3: + round shape 2.0 (hard cap MAX_MULTI_WORLD_TURNS 6->2... or
# selector honesty landing the average there)
show("A3 = A2 at 2.0 rep turns/round [E]", f1, m2, 2.0,
     "round = answer + one response")

# A4: selector-driven floor-1 average ~1.6
show("A4 = A2 at 1.6 rep turns/round [E/S]", f1, m2, 1.6,
     "one voice + others join when they differ")

# A5: reactive turns on Haiku (opening voice stays Sonnet) at 2.0 shape
haiku_gen = 0.0120  # [E] measured C4 token shape repriced on Haiku
m5_first, m5_react = m2, m2 - gen_draft + haiku_gen
pt5 = f1 + m5_first + 1.0 * m5_react
hrs5 = "  ".join(f"${pt5*t:5.2f}" for t in PACING)
print(f"  {'A5 = A3 with reactive turns on Haiku [S]':44s} ${pt5:.4f}/round   "
      f"{hrs5}   UNMEASURED voice-quality risk")

# --------------------------------------------------------- BOUNDS
hdr("BOUNDS THAT FRAME THE PRICING DECISION")

cap_reps = 100  # message_cap.py CONVERSATION_TURN_CAP_TABLE (rep turns)
print(f"""  [M] worst-case single sitting (100-rep-turn table cap):
        measured   ${cap_reps*M + (cap_reps/RPT)*F:6.2f}
        at A2      ${cap_reps*m2 + (cap_reps/RPT)*f1:6.2f}
        at A3      ${cap_reps*m2 + (cap_reps/2.0)*f1:6.2f}
  [M] solo free tier, same slice: ${solo_pt:.4f}/turn
      (40-turn solo cap => ${40*solo_pt:.2f} worst-case conversation)
  [E] a weekly 1-hour table participant, per month (4.3 sittings):
        measured @24/hr  ${(F+RPT*M)*24*4.3:6.2f}/mo
        A3       @24/hr  ${(f1+2.0*m2)*24*4.3:6.2f}/mo
        A3       @16/hr  ${(f1+2.0*m2)*16*4.3:6.2f}/mo
  Reference points: the funding thread's unit-cost anchor is ~$1/user/
  month (the live ask copy is built on it); the recurring supporter
  anchor is $8/mo; Table is decided paid-tier at public launch (SH-12).""")
