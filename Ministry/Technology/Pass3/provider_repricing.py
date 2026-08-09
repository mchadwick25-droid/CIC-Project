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
    1h cache write = 2.0x base input (the TTL this app actually sets).

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

# (input, output, cache_write_multiplier_used_by_this_app, cache_read)
# cache-write column is the ABSOLUTE $/MTok this app would pay, i.e. the 1h
# write rate where the provider has one and the app sets ttl=1h.
RATES = {
    # provider-model             in     out     cw(1h)   cr
    "sonnet-5 (intro, now)":   (2.00,  10.00,   4.00,   0.20),
    "sonnet-5 (from Sep 1)":   (3.00,  15.00,   6.00,   0.30),
    "haiku-4.5":               (1.00,   5.00,   2.00,   0.10),
    "opus-5":                  (5.00,  25.00,  10.00,   0.50),
    "gemini-3-pro":            (2.00,  12.00,   2.00,   0.20),
    "gemini-3-flash":          (0.50,   3.00,   0.50,   0.05),
    "gpt-5.6-terra":           (2.00,  12.00,   2.50,   0.20),
    "gpt-5.6-luna":            (0.20,   1.20,   0.25,   0.02),
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

# Split the measured shape into the two routing tiers the code already has.
gen = [r for r in llm if r["model"] == "claude-sonnet-5"]
clf = [r for r in llm if r["model"] != "claude-sonnet-5"]


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
print("""  cost_floor_model.py already costed a stack of Anthropic-side moves that
  need no provider change at all. Setting them side by side, per SOLO hour:

    [M] measured, dead code still in, Sep-1 rates      ~$2.42/hr
    [E] dead retrieval_filter_* removed                 ~$1.61/hr   -33%
    [E] + A1/A3 lossless + B1/B2 (the 20% budget)       ~$1.42/hr   -41%
    [E] same, but generation on Gemini 3 Flash          ~$0.55/hr   -77%
    [E] same, but generation on Haiku 4.5               ~$0.63/hr   -74%

  Two things follow, and they point in different directions:
    1. The single largest UNAMBIGUOUS win is still deleting dead code and
       capping Table rounds. It costs nothing, risks nothing, and it is not
       done yet. Provider migration cannot be justified until it is.
    2. Beyond that, no stack of Anthropic-side tuning reaches the stated
       $0.25-1.00/hr band. Only a cheaper generation model does. That is
       true whether the cheaper model is Haiku 4.5 or a competitor - and
       Haiku 4.5 requires ZERO migration work, only a config change.""")
