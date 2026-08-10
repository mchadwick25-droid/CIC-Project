"""Table cost model - Phase 1 of the multi-Representative brief.

Deterministic scenario model over the committed B-COST raw log
(Ministry/Technology/Pass2/baselines/cost_baseline_2026-07_raw.jsonl).
Same log -> byte-identical output. No API calls, no app code touched -
this is the "analysis only" instrument Phase 1 of
CiC_MultiRep_Quality_and_Cost_FableBrief_2026-08-09.md calls for.

WHAT IT MODELS. The measured table turn ($0.1585, 2.63x solo) decomposed
into four spend pools, then re-priced under each lever:

  gens        main_response generations (2.8/turn @ $0.0334 each)
  retrieval   per-Representative Haiku filtering (11.3 calls/turn)
  governance  the monitor/adjudicator stack
  facilitator reception/handoff (negligible)

THE ANATOMY FINDING this script exists to keep honest: a generation's
$0.0334 splits roughly HALF fresh input (5,577 uncached tokens - history,
retrieved context, dynamic segment - re-billed every call), a quarter
cache write, and the rest read+output. So "trim the prompts" is wrong for
the CACHED blocks (reads are 0.1x) but the DYNAMIC segment is real money,
and every additional speaker per turn re-bills it.

LEVERS (see the Phase 1 analysis doc for the quality cost of each):
  A  selective speaking - not all three Representatives generate every turn
  B  shared retrieval   - one batched filter pass per participant turn
  D  batched governance - monitors read all outputs in one call
  C  model tiering      - reactive generations on Haiku (HIGH quality risk)

KNOWN LIMITS, stated rather than smoothed:
  - The log predates the Voice Rebuild (bigger prompts land mostly in
    CACHED blocks -> start-of-conversation write cost, little steady-state)
    and predates the 1h cache TTL (write 2.0x vs the 1.25x priced here;
    the --ttl-1h flag re-prices writes, but the TTL also ELIMINATES
    pause-driven rewrites, which this log cannot show). The $3.39 re-run
    is the first implementation step, not an analysis blocker.
  - Second-order savings (fewer speakers -> shorter history for later
    calls) are ignored; every scenario is therefore conservative.

Usage (from repo root or backend):
  python scripts/table_cost_model.py [--turns-per-hour 30] [--ttl-1h]
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
LOG = (BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" /
       "baselines" / "cost_baseline_2026-07_raw.jsonl")

# standard pricing (per MTok): input, output, 5m-cache-write, cache-read
PRICING = {
    "claude-sonnet-5": (3.00, 15.00, 3.75, 0.30),
    "claude-haiku-4-5-20251001": (1.00, 5.00, 1.25, 0.10),
}

GOV_PER_GEN = {  # monitors that run per Representative generation
    "drift_detection", "over_settling_screen", "over_settling_adjudication",
}
RETRIEVAL = {"retrieval_filter_lexicon", "retrieval_filter_story"}


def call_cost(r: dict, ttl_1h: bool) -> float:
    i, o, w, rd = PRICING[r["model"]]
    if ttl_1h:
        w = i * 2.0  # 1h cache-write premium
    fresh = (r["input_tokens"] - r["cache_read_input_tokens"]
             - r["cache_creation_input_tokens"])
    return (fresh * i + r["output_tokens"] * o
            + r["cache_creation_input_tokens"] * w
            + r["cache_read_input_tokens"] * rd) / 1e6


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--turns-per-hour", type=int, default=30)
    ap.add_argument("--ttl-1h", action="store_true",
                    help="re-price cache writes at the 1h-TTL 2.0x multiplier")
    args = ap.parse_args()
    tph = args.turns_per_hour

    rows = [json.loads(l) for l in LOG.read_text(encoding="utf-8").splitlines()
            if l.strip()]
    calls = [r for r in rows if r["kind"] == "llm_call"]
    T = [r for r in calls if r["conversation"] == "C4_three_world_table"]
    S = [r for r in calls if r["conversation"] != "C4_three_world_table"]
    TURNS = 10  # C4's participant turns, fixed by the conversation set

    pool = collections.defaultdict(float)
    n_gen = 0
    for r in T:
        c = call_cost(r, args.ttl_1h)
        if r["label"] == "main_response":
            pool["gens"] += c; n_gen += 1
        elif r["label"] in RETRIEVAL:
            pool["retrieval"] += c
        elif r["label"].startswith("facilitator"):
            pool["facilitator"] += c
        else:
            pool["governance"] += c
    for k in pool: pool[k] /= TURNS
    gens_per_turn = n_gen / TURNS
    per_gen = pool["gens"] / gens_per_turn
    gov_scaled = sum(call_cost(r, args.ttl_1h) for r in T
                     if r["label"] in GOV_PER_GEN) / TURNS
    gov_fixed = pool["governance"] - gov_scaled
    solo = sum(call_cost(r, args.ttl_1h) for r in S) / 30

    def turn(gens_sonnet, gens_haiku=0.0, retrieval_share=1.0, gov_batched=False):
        g = gens_sonnet * per_gen + gens_haiku * per_gen / 3  # haiku ~ 1/3 price
        total_g = gens_sonnet + gens_haiku
        ret = pool["retrieval"] * retrieval_share
        gv = gov_fixed + gov_scaled * (total_g / gens_per_turn) * (0.5 if gov_batched else 1.0)
        return g + ret + gv + pool["facilitator"]

    scenarios = [
        ("S0  today (all three speak)", turn(gens_per_turn)),
        ("S1  +shared retrieval +batched governance", turn(gens_per_turn, retrieval_share=1/3, gov_batched=True)),
        ("S2  S1 + selective speaking (avg 1.6 gens)", turn(1.6, retrieval_share=1/3, gov_batched=True)),
        ("S3  S2 + reactive gens on Haiku (HIGH RISK)", turn(1.0, 0.6, retrieval_share=1/3, gov_batched=True)),
        ("FLOOR one voice/turn (no longer a table)", turn(1.0, retrieval_share=1/3, gov_batched=True)),
    ]

    ttl = " [1h-TTL write pricing]" if args.ttl_1h else ""
    print(f"[tcm] pools ($/turn){ttl}: gens {pool['gens']:.4f} "
          f"({gens_per_turn:.1f} x {per_gen:.4f}) | retrieval {pool['retrieval']:.4f} | "
          f"governance {pool['governance']:.4f} (scales-with-gens {gov_scaled:.4f}) | "
          f"facilitator {pool['facilitator']:.4f}")
    print(f"[tcm] solo reference: ${solo:.4f}/turn  (${solo*tph:.2f}/hr @ {tph} turns)")
    print(f"[tcm] {'scenario':<44}{'$/turn':>8}{'$/hr':>7}{'x solo':>7}")
    for name, c in scenarios:
        print(f"[tcm] {name:<44}{c:>8.4f}{c*tph:>7.2f}{c/solo:>7.2f}")
    print("[tcm] Mark's line: $5/hour. Quality costs per lever are in the "
          "Phase 1 analysis doc - this prints dollars only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
