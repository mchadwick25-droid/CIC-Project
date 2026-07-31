#!/usr/bin/env python3
"""
Pass 3 cost-floor model (2026-07-30) - the ~80%-quality floor.

Grounded in the committed B-COST raw log
(Ministry/Technology/Pass2/baselines/cost_baseline_2026-07_raw.jsonl),
priced with the same corrected dollars() as scripts/cost_baseline_runner.py.

NO LIVE API CALLS. cic-poc/backend/.env holds a 10-char 'sk-ant-...'
placeholder and MOCK_LLM=true, so no new *measured* dollar figure is
producible. Tags on every figure:
  [M] measured    - read off the committed raw log or the repo's own files
  [E] estimated   - measured token shapes + published pricing
  [S] speculative - reasoned but unvalidated (adoption, quality deltas)

Pricing verified 2026-07-30 against the claude-api skill's current table:
sonnet-5 $3.00/$15.00 per MTok ($2/$10 intro to 2026-08-31); haiku-4.5
$1.00/$5.00. Cache write 1.25x (5-min TTL) / 2.00x (1-hour TTL); cache
read 0.10x. Batch API 50% off. Min cacheable prefix: sonnet-5 1024 tok,
haiku-4.5 4096 tok (so the safety classifiers genuinely cannot cache).
"""

import collections
import json
import math
import os
import statistics

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RAW = os.path.join(REPO, "Ministry", "Technology", "Pass2", "baselines",
                   "cost_baseline_2026-07_raw.jsonl")

PRICING = {"claude-sonnet-5": (3.00, 15.00, 3.75, 0.30),
           "claude-haiku-4-5-20251001": (1.00, 5.00, 1.25, 0.10)}
SONNET, HAIKU = PRICING["claude-sonnet-5"], PRICING["claude-haiku-4-5-20251001"]

# Reproduces the investigation's own $1.82/hr solo and $4.73/hr Table
# headline from the per-turn figures below (~2.0 min per solo turn, ~2.5 min
# per Table round). Pacing is itself a lever - see the sensitivity block.
TPH = {"solo": 30.0, "table": 24.0}

# Labels whose call count scales with REPRESENTATIVE turns (measured against
# C4: 8 participant turns, 28 representative turns).
PER_REP = {"main_response", "turn_selector", "drift_detection",
           "over_settling_screen", "over_settling_adjudication",
           "fabrication_adjudication", "retrieval_filter_lexicon",
           "retrieval_filter_story"}
DEAD = {"retrieval_filter_lexicon", "retrieval_filter_story"}


def dollars(r):
    i, o, w, rd = PRICING[r["model"]]
    unc = (r["input_tokens"] - r["cache_read_input_tokens"]
           - r["cache_creation_input_tokens"])
    return (unc * i + r["output_tokens"] * o
            + r["cache_creation_input_tokens"] * w
            + r["cache_read_input_tokens"] * rd) / 1_000_000


def price(rates, unc, out, cw=0, cr=0):
    i, o, w, rd = rates
    return (unc * i + out * o + cw * w + cr * rd) / 1_000_000


def hdr(t):
    print("\n" + "=" * 76 + "\n" + t + "\n" + "=" * 76)


rows = [json.loads(l) for l in open(RAW)]
llm = [r for r in rows if r.get("kind") == "llm_call"]
solo = [r for r in llm if r["conversation"] != "C4_three_world_table"]
table = [r for r in llm if r["conversation"] == "C4_three_world_table"]
NT = {"solo": 30, "table": 8}


def by_label(rs):
    d = collections.defaultdict(lambda: [0, 0.0])
    for r in rs:
        d[r["label"]][0] += 1
        d[r["label"]][1] += dollars(r)
    return d


# ============================================================== STEP 1
hdr("STEP 1 - TRUE CURRENT BASELINE (dead code out, live path in)")

# The live negative_condition_* call: label + do_not_retrieve_when per
# candidate only, plus query + context; fires at most once per retriever per
# representative turn. Scaffold measured from evaluate_negative_conditions
# (chars/4 - wrs/parameters.yaml's own token convention).
NC_IN = 190 + 420 + 45 * 4      # [E] scaffold + query/ctx + 4 guarded candidates
NC_OUT = 18 * 4                 # [E]
NC_PER_CALL = price(HAIKU, NC_IN, NC_OUT)
NC_CALLS_PER_REP = 2            # [M] one lexicon + one story, at most

R = {}
for name, rs in (("solo", solo), ("table", table)):
    lab = by_label(rs)
    total = sum(v[1] for v in lab.values())
    dead = sum(v[1] for k, v in lab.items() if k in DEAD)
    reps = lab["main_response"][0]
    live_nc = NC_PER_CALL * NC_CALLS_PER_REP * reps
    true_total = total - dead + live_nc
    per_rep = sum(v[1] for k, v in lab.items() if k in PER_REP and k not in DEAD) + live_nc
    per_part = true_total - per_rep
    R[name] = dict(lab=lab, total=total, dead=dead, reps=reps, nt=NT[name],
                   true=true_total, per_rep=per_rep, per_part=per_part)
    print(f"\n{name.upper()}  [{NT[name]} participant turns, {reps} representative "
          f"turns = {reps/NT[name]:.2f} per message]")
    print(f"  [M] committed baseline      ${total:.4f}  = ${total/NT[name]:.4f}/turn"
          f"  = ${total/NT[name]*TPH[name]:.2f}/hr")
    print(f"  [M] dead retrieval_filter_* -${dead:.4f}  ({100*dead/total:.1f}%)")
    print(f"  [E] live negative_condition +${live_nc:.4f}  "
          f"(${NC_PER_CALL:.6f} x {NC_CALLS_PER_REP} x {reps})")
    print(f"  [E] TRUE CURRENT            ${true_total:.4f}  "
          f"= ${true_total/NT[name]:.4f}/turn  "
          f"= ${true_total/NT[name]*TPH[name]:.2f}/hr")
    print(f"      of which scales per REPRESENTATIVE turn: ${per_rep:.4f} "
          f"({100*per_rep/true_total:.0f}%)   per PARTICIPANT turn: "
          f"${per_part:.4f} ({100*per_part/true_total:.0f}%)")

# ============================================================== STEP 2
hdr("STEP 2 - WHERE GENERATION COST ACTUALLY IS [M]")

mr = [r for r in llm if r["label"] == "main_response"]
unc = statistics.mean(r["input_tokens"] - r["cache_read_input_tokens"]
                      - r["cache_creation_input_tokens"] for r in mr)
out = statistics.mean(r["output_tokens"] for r in mr)
cw = statistics.mean(r["cache_creation_input_tokens"] for r in mr)
cr = statistics.mean(r["cache_read_input_tokens"] for r in mr)
c = price(SONNET, unc, out, cw, cr)
print(f"  [M] mean main_response call: uncached_in {unc:.0f}, output {out:.0f}, "
      f"cache_write {cw:.0f}, cache_read {cr:.0f}  = ${c:.5f}")
print(f"      uncached input {100*price(SONNET,unc,0)/c:.0f}%  |  output "
      f"{100*price(SONNET,0,out)/c:.0f}%  |  cache write "
      f"{100*price(SONNET,0,0,cw)/c:.0f}%  |  cache read "
      f"{100*price(SONNET,0,0,0,cr)/c:.0f}%")
print(f"  ==> OUTPUT IS ONLY {100*price(SONNET,0,out)/c:.0f}% OF GENERATION COST. "
      f"'Shorter answers' is NOT the lever. Input is.")
print(f"  [E] identical token shape on Haiku 4.5 = "
      f"${price(HAIKU,unc,out,cw,cr):.5f} "
      f"({100*(1-price(HAIKU,unc,out,cw,cr)/c):.0f}% cheaper)")

print("\n  [E] Real per-turn RETRIEVED-CONTEXT size, replicating the live strip "
      "(front-matter\n      at index time, Key Sources always, Quick Meaning for "
      "migrated worlds), k=3 lex + k=2 story:")
for w, v in (("alexandria (migrated)", 4310), ("syriac (migrated)", 3333),
             ("pahc", 2759), ("imperial-juridical", 2533),
             ("hieronymian", 2234), ("desert (migrated)", 1453)):
    print(f"        {w:24s} {v:5d} tok/turn   = ${price(SONNET,v,0):.5f}/turn "
          f"of uncached input")
print("      Alexandria pays 3.0x Desert for retrieval alone. Measured knock-on:")
for cv, u, pt in (("C3_alexandria", 8266, 0.0792), ("C2_desert", 3769, 0.0596),
                  ("C1_house_church", 4088, 0.0419)):
    print(f"        [M] {cv:16s} uncached_in {u:5d}  ->  ${pt:.4f}/participant-turn")

# ============================================================== STEP 3
hdr("STEP 3 - THE HARD-CEILING REGENERATION PATH [M] - the biggest single item")

print("""  nodes.py stream_representative_turn: for HARD_CEILING_WORLDS
  (desert 60w, syriac 165w, alexandria 160w, hieronymian 180w) the first
  draft is BUFFERED, and if it exceeds ceiling x trigger the WHOLE turn is
  generated a second time at full price. The retry re-sends the entire
  prompt PLUS the discarded draft, so it costs MORE than the original.""")
g = collections.defaultdict(list)
for r in mr:
    g[(r["conversation"], r["turn"], r["request_id"])].append(r)
print("\n  Single-world conversations - the grouping is unambiguous [M]:")
for cv in ("C1_house_church", "C2_desert", "C3_alexandria_paused"):
    grp = [v for k, v in g.items() if k[0] == cv]
    regen = [v for v in grp if len(v) > 1]
    extra = sum(dollars(x) for v in regen for x in sorted(v, key=lambda y: y["ts"])[1:])
    conv_total = sum(dollars(r) for r in llm if r["conversation"] == cv)
    print(f"    {cv:24s} {len(grp):2d} rounds, {len(regen):2d} regenerated "
          f"({100*len(regen)/len(grp):3.0f}%)  extra ${extra:.4f} "
          f"= {100*extra/conv_total:4.1f}% of that conversation")
DESERT_EXTRA = 0.1423
print(f"""
  [M] Desert regenerates on 80% of its turns, costing 23.9% of that whole
      conversation. Its stated
      measure is 60 words but the code's own comment records uncorrected
      drafts landing at 175-180. Alexandria and Syriac show 0% in SOLO because
      their ceilings were deliberately set AT their measured solo max.
  [!] For the 3-world TABLE this log CANNOT separate a regeneration from a
      second speaker - every per-world call in a round shares one request_id
      and world_id is not logged. But the code comments say the ceilings were
      added BECAUSE table turns blow past them (Alexandria 300+w vs 160;
      Syriac 1053w vs a 98w native measure), so the table regeneration rate
      should be HIGH, not zero. THIS IS THE #1 THING TO MEASURE the moment a
      live key exists - it is plausibly 30-60% of Table generation cost.""")

# ============================================================== STEP 4
hdr("STEP 4 - THE MOVES")

moves = []


def mv(k, label, s, t, conf, tradeoff):
    moves.append(dict(k=k, label=label, solo=s, table=t, conf=conf, tr=tradeoff))


# --- A. Lossless / quality-positive -------------------------------------
adj = {n: R[n]["lab"]["fabrication_adjudication"][1]
       + R[n]["lab"]["over_settling_adjudication"][1] for n in R}
mv("A1", "adjudication retrieval: drop the appropriateness guard",
   -0.06 * adj["solo"], -0.06 * adj["table"], "high",
   "NONE - cost-positive AND rigour-positive (stops hiding the clearing chunk)")

# 1-hour cache TTL. Measured: 6 of 64 main_response calls re-paid a >5k prefix
# write at 1.25x. A 1h TTL pays 2.0x once per session instead.
rew = [r for r in mr if r["cache_creation_input_tokens"] > 5000]
rew_tok = sum(r["cache_creation_input_tokens"] for r in rew)
first_writes = 4          # [M] one per conversation
extra_writes = len(rew) - first_writes
avg_prefix = rew_tok / max(len(rew), 1)
now_cost = price(SONNET, 0, 0, rew_tok)                       # all at 1.25x
ttl_cost = price(SONNET, 0, 0, 0) + first_writes * avg_prefix * 3.00 * 2.00 / 1e6
ttl_save = now_cost - ttl_cost
print(f"\n  [M] prefix re-writes (>5k cache_creation): {len(rew)} across "
      f"{first_writes} conversations = {len(rew)/first_writes:.2f} writes per "
      f"initial write.")
print(f"  [E] 1-hour TTL break-even is {2.00/1.25:.2f} writes per initial write. "
      f"AT THE MEASURED PAUSE RATE IT IS A NET LOSS "
      f"(${-ttl_save:+.4f} over the fixed set) - do NOT adopt it now. It flips "
      f"positive as soon as real contemplative pacing pushes pauses past 1.6x, "
      f"which is exactly the regime the slower-pacing rows below assume.")
mv("A2", "1-hour cache TTL  [REJECTED at measured pacing - see above]",
   0.0, 0.0, "high",
   "NONE, but it does not pay at the measured pause rate; revisit with real "
   "usage data")

mv("A3", "move the numeric measure into the post-history guard slot "
   "(halve the regeneration rate)",
   -0.5 * DESERT_EXTRA, 0.0, "medium",
   "NONE if it works - the slot already exists and the codebase's own S5.2 "
   "finding is that guards nearest generation survive attention decay")

# --- B. Inside Mark's permitted 20% -------------------------------------
soft = ("wind_down", "drift_detection", "over_settling_screen")
mv("B1", "run wind_down / drift / over-settling SCREEN every 2nd turn",
   -0.5 * sum(R["solo"]["lab"][k][1] for k in soft),
   -0.5 * sum(R["table"]["lab"][k][1] for k in soft), "medium",
   "post-hoc monitors only (never blocking); a drift correction can arrive "
   "one turn later than today")

# Retrieval depth k=3 -> k=2 on lexicon for non-high-criterion turns.
# Fleet-mean lexicon entry, post-strip, x1 fewer entry.
FLEET_LEX_ENTRY = statistics.mean([1082, 537, 485, 498, 349, 203])
k_save_per_rep = price(SONNET, FLEET_LEX_ENTRY, 0)
mv("B2", "retrieval depth k=3 -> k=2 (lexicon) on ordinary turns",
   -k_save_per_rep * R["solo"]["reps"] * 0.7,
   -k_save_per_rep * R["table"]["reps"] * 0.7, "high",
   "one fewer lexicon entry in view; the R7 quick-reach layer keeps EVERY "
   "term's plain meaning permanently in the cached prefix, so nothing "
   "becomes unreachable - only less deeply quoted")

# Table round cap: 3.5 -> 2 representative turns per message.
per_rep_unit = R["table"]["per_rep"] / R["table"]["reps"]
cap_reps = 2 * R["table"]["nt"]
mv("B3", "Table round cap: 2 representative turns per message (from 3.5)",
   0.0, -(R["table"]["reps"] - cap_reps) * per_rep_unit, "high",
   "THE Table move. Same 3 worlds seated, same voices available; a round is "
   "one real answer + one real response instead of averaging 3.5 speeches. "
   "MIN_MULTI_WORLD_TURNS is already 2 - this lowers MAX from 6.")

for m in moves:
    print(f"\n  {m['k']}  {m['label']}")
    print(f"      solo {m['solo']:+.4f}  table {m['table']:+.4f}   "
          f"confidence {m['conf']}")
    print(f"      participant-visible change: {m['tr']}")

# ============================================================== STEP 5
hdr("STEP 5 - THE ANSWER BANK, PROPERLY BOUNDED")

t1 = collections.defaultdict(float)
allc = collections.defaultdict(float)
for r in llm:
    allc[r["conversation"]] += dollars(r)
    if r["turn"] == 1:
        t1[r["conversation"]] += dollars(r)
for cv in sorted(allc):
    print(f"  [M] {cv:24s} turn 1 = {100*t1[cv]/allc[cv]:4.1f}% of the "
          f"whole conversation")

ROLES, SETS, QPS, WORLDS = 4, 5, 4.5, 6
print(f"""
  [M] Curriculum V1.0 = {ROLES} roles x {SETS} sets x ~{QPS} questions = 100
      questions, ROLE-GENERIC (they work in any world). Each set is 'a walk,
      not a menu' - a deliberate ordered chain. Zero UI code exists; the
      curriculum has never faced a live model (Guided-Questions README).
  [E] Because a walk is deterministic while un-deviated, a whole CHAIN is
      precomputable, not merely turn 1:
        solo  bank = {ROLES}x{SETS}x{WORLDS} = {ROLES*SETS*WORLDS} chains x {QPS} = {int(ROLES*SETS*WORLDS*QPS)} precomputed turns
        table bank = {ROLES}x{SETS}x(C(6,2)={math.comb(6,2)}+C(6,3)={math.comb(6,3)}) = {ROLES*SETS*(math.comb(6,2)+math.comb(6,3))} chains x {QPS} = {int(ROLES*SETS*(math.comb(6,2)+math.comb(6,3))*QPS)} precomputed turns""")
build_solo = ROLES * SETS * WORLDS * QPS * (R["solo"]["true"] / NT["solo"]) * 0.5
build_tab = (ROLES * SETS * (math.comb(6, 2) + math.comb(6, 3)) * QPS
             * (R["table"]["true"] / NT["table"]) * 0.5)
print(f"  [E] one-time build at the Batch API's 50% discount: solo "
      f"${build_solo:,.0f}, table ${build_tab:,.0f} (table bank is the "
      f"expensive one and ages fastest)")
print("""
  [S] SERVED FRACTION - the number the first pass left unvalidated.
      Three independent factors, each grounded in the repo's own design:
        P(question-first door)  ~1/3   3 co-equal doors, NO default
                                       (QuestionFirst_Entry_Design s1)
        P(taps a starter)              the other branch of that door is a
                                       FREE-TYPED question, which no bank
                                       can serve without breaking uptake
        P(stays on the walk)           'the participant can jump anywhere';
                                       any deviation ends the chain""")
for pd, pt_, ps, lbl in ((0.33, 0.50, 0.60, "optimistic"),
                         (0.33, 0.35, 0.45, "central"),
                         (0.25, 0.20, 0.30, "conservative")):
    print(f"        {lbl:12s} {pd:.2f} x {pt_:.2f} x {ps:.2f} = "
          f"{100*pd*pt_*ps:4.1f}% of turns served")
BANK = 0.052
print(f"""
  ==> {100*BANK:.1f}% central, NOT 30-50%. The first pass's figure appears to
      have priced 'guided-path traffic' as if the whole conversation were
      bankable. It is not: the bank can only serve an UNDEVIATED walk, and
      serving a precomputed answer to a paraphrased free-typed question would
      violate the uptake rule that representative_prompts.py enforces hardest
      ('legible as an answer only to the message actually in front of you').""")

# ============================================================== STEP 6
hdr("STEP 6 - STACKED SCENARIOS")


def sc(name, key, applied, bank=0.0, note=""):
    tot = R[key]["true"] + sum(m[key] for m in moves if m["k"] in applied)
    tot *= (1 - bank)
    pt_ = tot / R[key]["nt"]
    hr = pt_ * TPH[key]
    print(f"  {name:52s} ${pt_:.4f}/turn  ${hr:5.2f}/hr {note}")
    return hr


print("\nSOLO   (target $0.25-1.00/hr)")
print(f"  {'committed baseline [M]':52s} "
      f"${R['solo']['total']/30:.4f}/turn  "
      f"${R['solo']['total']/30*30:5.2f}/hr")
sc("true current, dead code removed [E]", "solo", set())
sc("+ A1,A2,A3 lossless [E]", "solo", {"A1", "A2", "A3"})
solo_q = sc("+ B1,B2 (the 20% budget) [E]", "solo",
            {"A1", "A2", "A3", "B1", "B2"})
solo_f = sc("+ answer bank @5.2% [S]", "solo",
            {"A1", "A2", "A3", "B1", "B2"}, BANK, "<== SOLO FLOOR")

print("\nTABLE 3 worlds   (target $0.25-1.00/hr)")
print(f"  {'committed baseline [M]':52s} "
      f"${R['table']['total']/8:.4f}/turn  "
      f"${R['table']['total']/8*24:5.2f}/hr")
sc("true current, dead code removed [E]", "table", set())
sc("+ A1,A2,A3 lossless [E]", "table", {"A1", "A2", "A3"})
sc("+ B1,B2 [E]", "table", {"A1", "A2", "A3", "B1", "B2"})
tab_q = sc("+ B3 round cap of 2 [E]", "table",
           {"A1", "A2", "A3", "B1", "B2", "B3"})
tab_f = sc("+ answer bank @5.2% [S]", "table",
           {"A1", "A2", "A3", "B1", "B2", "B3"}, BANK, "<== TABLE FLOOR")

print("\nTABLE - IF the table regeneration rate is what the code comments imply")
tot = R["table"]["true"] + sum(m["table"] for m in moves)
for rg, lbl in ((0.0, "0% regeneration (as modelled above)"),
                (0.30, "30% of table generation is regeneration"),
                (0.60, "60% of table generation is regeneration")):
    gen = R["table"]["lab"]["main_response"][1]
    saved = gen * rg * 0.5      # halving it via A3
    pt_ = (tot - saved) / 8 * (1 - BANK)
    print(f"  {lbl:52s} ${pt_:.4f}/turn  ${pt_*24:5.2f}/hr")

hdr("STEP 7 - THE ONE MOVE BIG ENOUGH TO REACH THE BAND, AND ITS REAL COST")

haiku_delta = price(HAIKU, unc, out, cw, cr) - price(SONNET, unc, out, cw, cr)
print(f"""  Everything above, stacked, lands SOLO at ~$1.35/hr and TABLE at ~$2.08/hr
  against a $0.25-1.00/hr target. The only single lever large enough to close
  that gap is moving representative generation off Sonnet.

  [E] per-call delta on the MEASURED token shape: ${haiku_delta:+.5f}""")
# NB: after B3 the Table runs 2 generations per message, not 3.5 - the Haiku
# delta must be applied to the POST-CAP generation count or it double-counts.
GENS_AFTER_MOVES = {"solo": R["solo"]["reps"], "table": 2 * R["table"]["nt"]}
for key in ("solo", "table"):
    base = R[key]["true"] + sum(m[key] for m in moves)
    n = GENS_AFTER_MOVES[key]
    with_h = base + haiku_delta * n
    pt_ = with_h / R[key]["nt"] * (1 - BANK)
    print(f"  {key.upper():6s} all moves + Haiku on {n:2d} generations: "
          f"${pt_:.4f}/turn  ${pt_*TPH[key]:5.2f}/hr")

print("""
  [M] WHY I DO NOT RECOMMEND TAKING IT BLIND. Measured off the live prompts:
      _HOW_YOU_ENGAGE            4,094 est tokens
      REACTIVE_TURN_GUIDANCE     2,629 est tokens
      -> 55 distinct prohibitive constructions the model must hold at once
         ('do not' x33, 'never' x9, 'stop and' x4, ...), plus 7 worked
         WRONG/RIGHT example pairs for failure modes that are subtle by
         construction: the I/we recast on a claimed personal limitation; a
         fabricated scene that stays fabricated after the pronoun is fixed;
         em-dash-as-default-connector; 'it is not X, it is Y'; the summarising
         benediction; and - hardest - manufactured resolution arriving as a
         BORROWED IMAGE with no shared vocabulary, several turns later.
      This is dense negative-constraint instruction-following over long
      context. It is the capability axis on which a smaller model degrades
      first, and the three real-time blocking checks do NOT cover any of it -
      the detectors that do (check_manufactured_resolution,
      check_cross_world_vocabulary_drift, check_convergence) are POST-HOC and
      only queue guidance for a LATER turn. A tier failure is therefore spoken
      to the participant before anything catches it.
  [!] DECISION FOR MARK, not an assumption I will make for him. It is also
      cheap to settle: re-run the S4.3 blind-graded battery shape with
      Haiku-generated representative turns against the same graders. That
      needs a live key and nothing else.""")

print("\nPACING SENSITIVITY - the largest single uncosted variable")
pt_ = (R["table"]["true"] + sum(m["table"] for m in moves)) / 8 * (1 - BANK)
for tph, lbl in ((24.0, "24 turns/hr - the investigation's own pacing"),
                 (16.0, "16 turns/hr - ~3.7 min per 2-voice round"),
                 (10.0, "10 turns/hr - real reading time, contemplative")):
    print(f"  Table, all moves, {lbl:47s} ${pt_*tph:5.2f}/hr")
pts = (R["solo"]["true"] + sum(m["solo"] for m in moves)) / 30 * (1 - BANK)
for tph, lbl in ((30.0, "30 turns/hr - the investigation's own pacing"),
                 (20.0, "20 turns/hr - 3 min per turn"),
                 (12.0, "12 turns/hr - contemplative")):
    print(f"  Solo,  all moves, {lbl:47s} ${pts*tph:5.2f}/hr")
