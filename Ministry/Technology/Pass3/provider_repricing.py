#!/usr/bin/env python3
"""
Provider repricing (2026-08-09) - what the SAME measured CiC workload costs
on each candidate provider, and what the Sonnet 5 intro-pricing expiry
actually does to the bill.

Companion to cost_floor_model.py. That file asks "how cheap can this get on
Anthropic"; this one asks "does switching provider beat that, and by how
much". Both read the same committed measurement so the two are directly
comparable:
  Ministry/Technology/Pass2/baselines/cost_baseline_2026-07_raw.jsonl

NO LIVE API CALLS. Nothing here is measured on a non-Anthropic provider -
this reprices a measured Anthropic TOKEN SHAPE at other providers' published
rates. Tags:
  [M] measured    - read off the committed raw log
  [E] estimated   - measured token shape + published pricing
  [S] speculative - reasoned but unvalidated (quality, tokenizer deltas)

PRICING VERIFIED 2026-08-09 (all $/MTok, standard/non-batch):

  Anthropic (platform.claude.com/docs/en/about-claude/pricing)
    sonnet-5, through 2026-08-31   in 2.00  out 10.00  cw5m 2.50  cr 0.20
    sonnet-5, from   2026-09-01    in 3.00  out 15.00  cw5m 3.75  cr 0.30
    haiku-4.5                      in 1.00  out  5.00  cw5m 1.25  cr 0.10
    opus-5                         in 5.00  out 25.00  cw5m 6.25  cr 0.50
    Writes are priced at the 5-MINUTE rate (1.25x) throughout, because the
    committed run notes show this baseline was measured under a 5m TTL.
    The deployed code now sets ttl="1h" (2.0x); see the RATES comment for
    why that cannot be applied to these counts by swapping the rate.

  Google Gemini (ai.google.dev pricing; blocked from direct fetch here, so
  taken from aggregator agreement across benchlm/costgoat/pricepertoken)
    gemini-3-pro                   in 2.00  out 12.00   cache read 0.20
    gemini-3-flash                 in 0.50  out  3.00   cache read 0.05
    Explicit context caching ALSO charges storage per hour: $4.50/MTok/hr
    (Pro), $1.00/MTok/hr (Flash). Anthropic has no storage charge. This is
    modelled explicitly below - it is the single biggest structural
    difference for THIS app, which parks a ~13.5k prefix per representative.

  OpenAI (platform.openai.com pricing; blocked from direct fetch here, same
  aggregator-agreement method; rates are post the 2026-07-30 cut)
    gpt-5.6-sol                    in 5.00  out 30.00   cached in 0.50
    gpt-5.6-terra                  in 2.00  out 12.00   cached in 0.20
    gpt-5.6-luna                   in 0.20  out  1.20   cached in 0.02
    GPT-5.6 bills cache WRITES at 1.25x input (older families did not).

TOKENIZER CAVEAT [S], applied as a sensitivity rather than a headline:
Sonnet 5 uses Anthropic's newer tokenizer, which the pricing page states
produces ~30% more tokens for the same text than the previous one. Every
token count in the raw log is therefore a NEW-TOKENIZER count. Gemini and
OpenAI tokenize the same prose differently and generally more compactly, so
a straight token-for-token reprice UNDERSTATES their advantage. The
-20%-tokens row at the end bounds that.
"""

import collections
import json
import os
import statistics

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RAW = os.path.join(REPO, "Ministry", "Technology", "Pass2", "baselines",
                   "cost_baseline_2026-07_raw.jsonl")

# (input, output, cache_write, cache_read) - absolute $/MTok.
#
# CACHE-WRITE BASIS, corrected 2026-08-09. This first priced Anthropic writes
# at the 1-hour rate (2.0x base) because nodes.py._cached_system_message sets
# ttl="1h" today. That was wrong for THIS log. The committed run notes
# (Pass2/baselines/cost_baseline_2026-07_run_notes.md, note 2) record the
# measurement as textbook 5-minute behaviour: C3 turn 5 cache_read 15,737 ->
# a 330-second pause -> turn 6 cache_read 0 with the full 15,737 re-paid as a
# write. A 5.5-minute pause only expires a 5-minute cache. The app was on the
# 5m TTL when this was measured, so its cache_creation counts are 5m counts
# and must be priced at 1.25x - which is what cost_floor_model.py and
# scripts/cost_baseline_runner.py both do. They were right; this was not.
#
# The 1h TTL cannot be modelled by swapping the rate alone: it changes the
# COUNTS as well (fewer re-writes, each at 2.0x instead of 1.25x). Anthropic
# writes below are therefore 1.25x, matching the counts they multiply.
# cost_floor_model.py's own A2 move analysed the 1h switch properly and found
# it a NET LOSS at the measured pause rate; that the deployed code now sets
# 1h anyway is worth reconciling against fresh measurement, and is logged as
# an open item rather than silently priced here either way.
#
# Gemini's explicit cache charges the write at the base input rate plus a
# separate per-hour storage charge (modelled in STEP 3, not here). GPT-5.6
# bills writes at 1.25x input, same shape as Anthropic.
RATES = {
    # provider-model             in     out     cw      cr
    "sonnet-5 (intro, now)":   (2.00,  10.00,  2.50,   0.20),
    "sonnet-5 (from Sep 1)":   (3.00,  15.00,  3.75,   0.30),
    "haiku-4.5":               (1.00,   5.00,  1.25,   0.10),
    "opus-5":                  (5.00,  25.00,  6.25,   0.50),
    "gemini-3-pro":            (2.00,  12.00,  2.00,   0.20),
    "gemini-3-flash":          (0.50,   3.00,  0.50,   0.05),
    "gpt-5.6-terra":           (2.00,  12.00,  2.50,   0.20),
    "gpt-5.6-luna":            (0.20,   1.20,  0.25,   0.02),
}

# Gemini explicit-cache STORAGE, $/MTok/hour. Anthropic and OpenAI have no
# equivalent line item - a cached prefix costs its write and nothing more.
GEMINI_STORAGE_PER_MTOK_HR = {"gemini-3-pro": 4.50, "gemini-3-flash": 1.00}

# The app's own cache TTL (nodes.py _cached_system_message: ttl="1h").
CACHE_TTL_HOURS = 1.0

TPH = {"solo": 30.0, "table": 24.0}   # turns/hr, same as cost_floor_model
NT = {"solo": 30, "table": 8}         # participant turns in the baseline

# Which measured calls are GENERATION (today: sonnet) vs CLASSIFIER (today:
# haiku). Provider migration decisions can be made separately for each -
# that is the whole point of get_llm() / get_monitoring_llm() being two
# functions.
DEAD = {"retrieval_filter_lexicon", "retrieval_filter_story"}


def price(rates, unc, out, cw=0.0, cr=0.0):
    i, o, w, rd = rates
    return (unc * i + out * o + cw * w + cr * rd) / 1_000_000


def hdr(t):
    print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


rows = [json.loads(l) for l in open(RAW)]
llm = [r for r in rows if r.get("kind") == "llm_call" and r["label"] not in DEAD]

# Every label whose call site constructs get_llm() - i.e. the GENERATION
# tier, billed at settings.llm_model. Everything else goes through
# get_monitoring_llm() (or the retrievers' filter_llm) and is billed at the
# hardcoded classifier model. Derived by reading the log_llm_usage() call
# sites in app/graph/nodes.py, app/main.py and app/graph/*.
#
# Split by LABEL, not by model string. It used to be `model ==
# "claude-sonnet-5"`, which broke silently on 2026-08-09 the moment
# generation moved to Haiku 4.5: both tiers then report the same model and
# a model-based split reports ZERO generation calls, quietly zeroing 71% of
# the bill. The assertion below is the guard - it fails loudly on any
# future baseline containing a label this set does not know about.
GEN_LABELS = {
    "main_response",
    "facilitator_reception",
    "facilitator_handoff",
    "facilitator_bridge",
    "facilitator_close",
    "frame_breaker_response",
    "frame_breaker_response_plain",
    "relational_safety_response",
    "modern_term_bridge_facilitator_turn",
    "closing_turn_resources_offer",
    "closing_turn_resources_show",
    "closing_turn_sensed_close",
}
CLF_LABELS = {
    "frame_breaker", "relational_safety", "epistemology_bridge",
    "modern_term_bridge", "wind_down", "drift_detection",
    "over_settling_screen", "over_settling_adjudication",
    "fabrication_adjudication", "turn_selector", "turn_type_router",
    "convergence_check", "reroot_guidance", "citation_grounding",
    "closing_reply_classifier",
    "negative_condition_lexicon", "negative_condition_story",
}

unknown = {r["label"] for r in llm} - GEN_LABELS - CLF_LABELS
assert not unknown, (
    f"unclassified log labels {sorted(unknown)} - add each to GEN_LABELS or "
    "CLF_LABELS by checking whether its log_llm_usage() call site builds "
    "get_llm() (generation) or get_monitoring_llm() (classifier). Do NOT "
    "guess from the model string; both tiers can run the same model."
)

gen = [r for r in llm if r["label"] in GEN_LABELS]
clf = [r for r in llm if r["label"] in CLF_LABELS]

# The baseline predates the 2026-08-09 switch, so on THIS log the two
# splits must still agree. Keeps the label sets honest against the one
# measurement where both methods are valid.
assert gen == [r for r in llm if r["model"] == "claude-sonnet-5"], \
    "label-based split disagrees with the baseline's own model split"


def shape(rs):
    """Aggregate token shape of a set of calls."""
    unc = sum(r["input_tokens"] - r["cache_read_input_tokens"]
              - r["cache_creation_input_tokens"] for r in rs)
    return dict(
        n=len(rs),
        unc=unc,
        out=sum(r["output_tokens"] for r in rs),
        cw=sum(r["cache_creation_input_tokens"] for r in rs),
        cr=sum(r["cache_read_input_tokens"] for r in rs),
    )


def by_conv(rs, key):
    return [r for r in rs if (r["conversation"] == "C4_three_world_table")
            == (key == "table")]


hdr("STEP 0 - WHAT THE 'AUGUST INCREASE' ACTUALLY IS  [M]")
print("""  It is not a price rise on an existing rate. Claude Sonnet 5 launched with
  INTRODUCTORY pricing of $2/$10 per MTok, stated up front as running
  through 2026-08-31. On 2026-09-01 it reverts to Sonnet's standard
  $3/$15 - the same rate Sonnet 4.5 and 4.6 have always charged. So:

    - The bills Mark has actually SEEN were at the discounted rate.
    - +50% is the correct arithmetic on input, output, writes and reads.
    - But this project's own Pass 3 cost floor model (cost_floor_model.py,
      2026-07-30) was ALREADY priced at $3.00/$15.00 - see its PRICING dict.
      Every planning figure it produced ($1.61/hr solo, $4.14/hr table true
      current; ~$1.35/$2.08 after the stacked moves) is a POST-increase
      figure. Nothing in the plan of record needs re-deriving because of
      September 1. What changes is the gap between the plan and the bill.""")

for key in ("solo", "table"):
    g, c = shape(by_conv(gen, key)), shape(by_conv(clf, key))
    now = (price(RATES["sonnet-5 (intro, now)"], g["unc"], g["out"], g["cw"], g["cr"])
           + price(RATES["haiku-4.5"], c["unc"], c["out"], c["cw"], c["cr"]))
    sep = (price(RATES["sonnet-5 (from Sep 1)"], g["unc"], g["out"], g["cw"], g["cr"])
           + price(RATES["haiku-4.5"], c["unc"], c["out"], c["cw"], c["cr"]))
    print(f"\n  {key.upper():6s} [M] measured baseline, dead code excluded, "
          f"{NT[key]} participant turns")
    print(f"    at intro rates (what was billed) ${now:.4f}  "
          f"= ${now/NT[key]:.4f}/turn = ${now/NT[key]*TPH[key]:.2f}/hr")
    print(f"    from Sep 1                       ${sep:.4f}  "
          f"= ${sep/NT[key]:.4f}/turn = ${sep/NT[key]*TPH[key]:.2f}/hr")
    print(f"    delta                            +{100*(sep/now-1):.1f}%  "
          f"(<100% x1.5 because Haiku classifiers are unaffected)")

hdr("STEP 1 - WHERE THE MONEY IS, BY TIER  [M]")
G, C = shape(gen), shape(clf)
gsep = price(RATES["sonnet-5 (from Sep 1)"], G["unc"], G["out"], G["cw"], G["cr"])
chai = price(RATES["haiku-4.5"], C["unc"], C["out"], C["cw"], C["cr"])
tot = gsep + chai
print(f"  GENERATION  (get_llm, sonnet-5)   {G['n']:3d} calls  ${gsep:.4f}  "
      f"{100*gsep/tot:4.1f}% of spend")
print(f"  CLASSIFIER  (get_monitoring_llm)  {C['n']:3d} calls  ${chai:.4f}  "
      f"{100*chai/tot:4.1f}% of spend")
print(f"\n  ==> {100*gsep/tot:.0f}% of the bill is ONE function's calls. A provider swap "
      f"that touches\n      only get_llm() captures almost all of the available saving.")
print(f"\n  Generation token mix [M]: uncached_in {G['unc']:,}  output {G['out']:,}  "
      f"cache_write {G['cw']:,}  cache_read {G['cr']:,}")
print(f"    of generation cost: uncached input "
      f"{100*price(RATES['sonnet-5 (from Sep 1)'],G['unc'],0)/gsep:.0f}%  |  output "
      f"{100*price(RATES['sonnet-5 (from Sep 1)'],0,G['out'])/gsep:.0f}%  |  cache write "
      f"{100*price(RATES['sonnet-5 (from Sep 1)'],0,0,G['cw'])/gsep:.0f}%  |  cache read "
      f"{100*price(RATES['sonnet-5 (from Sep 1)'],0,0,0,G['cr'])/gsep:.0f}%")

hdr("STEP 2 - THE SAME TOKEN SHAPE, EVERY CANDIDATE  [E]")
print("  Generation tier only (classifiers held on Haiku 4.5 throughout, since")
print("  nothing cheaper is on the table for a one-word classifier).\n")
print(f"  {'generation model':26s} {'gen $':>9s} {'+clf':>9s} {'total':>9s} "
      f"{'solo $/hr':>10s} {'table $/hr':>11s}  vs Sep-1")

BASE = None
for name in ("sonnet-5 (from Sep 1)", "sonnet-5 (intro, now)", "opus-5",
             "haiku-4.5", "gemini-3-pro", "gemini-3-flash",
             "gpt-5.6-terra", "gpt-5.6-luna"):
    rates = RATES[name]
    g = price(rates, G["unc"], G["out"], G["cw"], G["cr"])
    t = g + chai
    if BASE is None:
        BASE = t
    # per-hour, split back out by conversation kind
    sg, sc = shape(by_conv(gen, "solo")), shape(by_conv(clf, "solo"))
    tg, tc = shape(by_conv(gen, "table")), shape(by_conv(clf, "table"))
    s_hr = (price(rates, sg["unc"], sg["out"], sg["cw"], sg["cr"])
            + price(RATES["haiku-4.5"], sc["unc"], sc["out"], sc["cw"], sc["cr"])
            ) / NT["solo"] * TPH["solo"]
    t_hr = (price(rates, tg["unc"], tg["out"], tg["cw"], tg["cr"])
            + price(RATES["haiku-4.5"], tc["unc"], tc["out"], tc["cw"], tc["cr"])
            ) / NT["table"] * TPH["table"]
    print(f"  {name:26s} {g:9.4f} {chai:9.4f} {t:9.4f} {s_hr:10.2f} {t_hr:11.2f}  "
          f"{100*(t/BASE-1):+6.1f}%")

hdr("STEP 3 - THE GEMINI CACHE-STORAGE CORRECTION  [E] - easy to miss")
print("""  Anthropic charges a cache WRITE and nothing else; the prefix sits there
  free for its TTL. Gemini's EXPLICIT context cache charges storage per
  MTok per hour on top of the write. This app parks a large static prefix
  per representative (permanent prompt + world capsule + engagement
  principles) with ttl=1h, which is exactly the shape that charge targets.
""")
# Measured mean cached prefix actually held per generation call.
mr = [r for r in gen if r["label"] == "main_response"]
held = statistics.mean(r["cache_read_input_tokens"] + r["cache_creation_input_tokens"]
                       for r in mr)
print(f"  [M] mean prefix held per main_response call: {held:,.0f} tokens")
for name in ("gemini-3-pro", "gemini-3-flash"):
    rate = GEMINI_STORAGE_PER_MTOK_HR[name]
    per_hr = held / 1_000_000 * rate * CACHE_TTL_HOURS
    print(f"  [E] {name:16s} storage ${rate:.2f}/MTok/hr -> ${per_hr:.4f} per "
          f"representative per cached hour")
    print(f"      3 representatives seated at a Table, 1h session: "
          f"${3*per_hr:.4f} - charged even if nobody speaks.")
print("""
  [E] At the Table this is a real but second-order line, roughly 1-4% of a
      session on Flash and 5-15% on Pro. It does NOT overturn the ranking.
      It DOES mean Gemini's headline rate flatters it slightly, and it
      punishes idle/contemplative pacing - the exact pacing this project
      says it wants. Gemini's IMPLICIT cache has no storage charge but also
      no hit guarantee, which is a worse trade for a prompt this app has
      deliberately engineered to be byte-stable.""")

hdr("STEP 4 - TOKENIZER SENSITIVITY  [S]")
print("""  Every count above is a Sonnet-5-tokenizer count, and Anthropic states
  that tokenizer emits ~30% more tokens for the same text than its
  predecessor. Non-Claude models tokenize this prose differently. If a
  competing tokenizer produces 20% fewer tokens for identical prompts:""")
for name in ("gemini-3-flash", "gpt-5.6-luna", "gemini-3-pro", "gpt-5.6-terra"):
    rates = RATES[name]
    g = price(rates, G["unc"] * .8, G["out"] * .8, G["cw"] * .8, G["cr"] * .8)
    print(f"  {name:16s} {g + chai:8.4f} total  "
          f"({100*((g+chai)/BASE-1):+.1f}% vs Sonnet 5 from Sep 1)")
print("""  [!] Unvalidated in either direction. Worth one hour of measurement
      (tokenize the actual permanent prompts with each provider's own
      tokenizer) before any figure here is quoted to anyone.""")

hdr("STEP 5 - MIGRATION vs THE MOVES ALREADY ON THE SHELF")
print("""  CORRECTED 2026-08-09. The first version of this block claimed removing
  the dead retrieval_filter_* calls was a -33% saving still available to
  take. That was wrong twice over, and the error was mine, not the cost
  model's - cost_floor_model.py's Step 1 is headed "dead code out, LIVE
  PATH IN" and its "TRUE CURRENT" line already means "what the code costs
  today". Verified directly against the source:

    - S3.4 (Pass 1 R6) had ALREADY removed the batched relevance vote.
      The functions that made those calls (evaluate_batch, _run_batch,
      partition_tier1_short_circuit in app/rag/batch_evaluate.py) sat
      uncalled in the file until they were deleted 2026-08-09. Nothing in
      app/rag/pipeline.py ever imported them. The saving was banked before
      this analysis started.
    - The magnitude was wrong too. -33% came from dividing against the
      wrong baseline. Correctly: the dead calls were 15.6% of the measured
      run; net of the live negative_condition call that replaced them
      (+$0.0828), the already-realised saving is ~11%, not 33%.

  What is actually left, per SOLO hour, at Sep-1 rates:

    [M] committed baseline, as measured 2026-07          ~$1.81/hr
    [E] TRUE CURRENT - what the code costs today          ~$1.61/hr   (banked)
    [E] + A1/A3 lossless + B1/B2 (the 20% budget)         ~$1.42/hr   -12%
    [E] same, but generation on Haiku 4.5                 ~$0.63/hr   -61%
    [E] same, but generation on Gemini 3 Flash            ~$0.55/hr   -66%

  Two things follow:
    1. There is no large no-risk saving left on the shelf. The Anthropic-
       side tuning that remains (A1/A3/B1/B2, plus B3 at the Table) is
       worth ~12% and is worth doing, but it is not the answer.
    2. Nothing short of a cheaper generation model reaches the stated
       $0.25-1.00/hr band. Haiku 4.5 gets there and requires ZERO
       migration work, only a config change; Gemini 3 Flash gets margi-
       nally further for weeks of work. That gap is the whole case
       against migrating.

  NB - the cache-TTL discrepancy this script previously flagged is now
  RESOLVED, against this script. It priced cache writes at the 1h rate
  (2.0x) because the deployed code sets ttl="1h"; cost_floor_model.py and
  cost_baseline_runner.py priced them at 5m (1.25x). The committed run
  notes settle it: the 2026-07-26 measurement shows a 330-second pause
  expiring the cache, which only a 5-minute TTL does. The counts in this
  log are 5m counts and are now priced at 1.25x here too, matching the
  other two tools. Solo TRUE CURRENT accordingly moves $1.65 -> $1.53/hr,
  and the generation token mix now matches cost_floor_model.py's Step 2
  almost exactly (52% uncached input / 15% output vs its 52% / 14%) - a
  cross-check that was not passing before this correction.

  WHAT IS STILL OPEN, and it is a real question rather than a rounding
  item: the deployed code sets ttl="1h" NOW, and cost_floor_model.py's own
  A2 move found the 1h TTL to be a NET LOSS at the measured pause rate
  (break-even is 1.6 writes per initial write; the run measured 1.5). Either
  pacing changed, or 1h was adopted against that finding. A 1h TTL cannot be
  modelled by swapping the rate alone - it changes the re-write COUNTS too -
  so this needs one fresh measurement, not arithmetic. Worth folding into
  the same live run as the Haiku battery, since both need only a key.""")
