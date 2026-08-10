# Phase 1 — can the table be afforded? Yes, with one design decision.

**The multi-Representative brief's Phase 1 deliverable: a cost architecture
with a target, an honest floor, and the quality price of each lever.**
Every dollar figure comes from `scripts/table_cost_model.py`, a committed
deterministic model over the B-COST raw log — its S0 row reproduces the
baseline report's $0.1585 exactly, which is the check that the model is
reading the data and not my expectations. No app code was touched.

---

## 1. The answer first

**A 3-Representative table can run at ~$0.09/turn — $2.56/hour at a
30-turn pace — without changing models and without touching anything the
six checkpoints validated.** That is roughly half of today and comfortably
under Mark's $5/hour line. It requires one design decision (selective
speaking) plus two pieces of plumbing (shared retrieval, batched
governance). The floor beneath which a table stops being a table is
~$0.063/turn, and it is only ~4% above solo cost — meaning **the second
and third voices are nearly the entire premium, and there is no clever
plumbing that removes them. The design decision cannot be engineered
around.**

| scenario | $/turn | $/hr @30 | × solo |
|---|---|---|---|
| S0 — today, all three speak | 0.1585 | **4.75** | 2.63 |
| S1 — shared retrieval + batched governance | 0.1298 | 3.89 | 2.15 |
| **S2 — S1 + selective speaking (avg 1.6 gens)** | **0.0852** | **2.56** | **1.41** |
| S3 — S2 + reactive gens on Haiku | 0.0718 | 2.15 | 1.19 |
| floor — one voice per turn | 0.0629 | 1.89 | 1.04 |

## 2. A finding that raises the stakes: today's table is already over the line

The baseline priced cache writes at the 5-minute-TTL multiplier (1.25×).
The app now uses **1-hour TTL, whose write multiplier is 2.0×**. Re-pricing
the same token counts: **S0 = $0.1754/turn = $5.26/hour.** Under current
pricing, the table as built today breaches Mark's line *before any growth in
prompt sizes from the rebuild is counted.* (The 1h TTL also eliminates
pause-driven cache rewrites — the thing that made the baseline's paused
conversation its most expensive — so the real net needs the $3.39 re-run.
But the burden of proof has flipped: the plumbing work is not optional
tuning, it is what brings the feature back under its own bar. S2 under
1h-TTL pricing is $0.0947/turn = $2.84/hour — still comfortably under.)

## 3. Where the money actually is — three corrections to intuition

The table turn decomposes into pools: **generations $0.0935** (2.8 ×
$0.0334), retrieval $0.0269, governance $0.0372 (of which $0.0214 scales
with generation count), facilitator $0.0008.

1. **A generation's cost is half fresh input, not output.** $0.0334 splits
   ~$0.0167 fresh input (5,577 uncached tokens: history, retrieved context,
   the dynamic segment — re-billed on every call), ~$0.0080 cache write,
   ~$0.0042 cache read, ~$0.0044 output. The earlier "trimming prompts
   won't fix this" holds for the **cached** blocks (reads are 0.1×) and is
   wrong for the **dynamic** segment. Every extra speaker re-bills it whole.
2. **Governance is not one pool.** $0.0214/turn of it scales with how many
   Representatives speak; $0.0158 is per-participant-turn regardless. Lever
   A automatically shrinks the first pool — selective speaking saves more
   than its generations alone.
3. **Retrieval is the biggest pure-plumbing win**: 11.3 Haiku filter calls
   per turn (one lexicon + one story pass per Representative) that can
   become one batched pass, the same numbered-candidate shape
   `batch_evaluate.py` already uses.

## 4. The levers and their quality price

**B — shared retrieval (save ~$0.018/turn). Quality cost: LOW.** Each world
keeps its own indices; what merges is the *judging* — one batched Haiku call
scoring all worlds' candidates instead of 3+ separate calls. Same judgment,
same shape as existing code.

**D — batched governance (save ~$0.011/turn at 2.8 gens). Quality cost:
LOW–MEDIUM.** Monitors read all Representative outputs in one call instead
of one each. The model assumes batching halves the scaled pool —
deliberately conservative. Fabrication and over-settling *adjudication*
stay per-incident, exactly as today; only the always-on screens batch.

**A — selective speaking (save ~$0.040/turn). Quality cost: THE DESIGN
QUESTION — this is where Phase 2 begins.** Not every Representative
generates every turn: the primary answers; a second joins when its world
*genuinely differs*; a third is rare. The measured basis for believing this
can be honest rather than cheap: the cross-world probe showed **0.000
phrase overlap between every pair of worlds** — when the worlds differ,
they differ completely, so a selector keyed on real divergence (the gravity
index is the divergence map) has signal to work with. The risks to design
against, not deny: a Representative silent too long stops being present;
manufactured turn-taking is as fake as manufactured consensus; and the
selector must never learn to suppress disagreement to save money — that
would be the Goodhart failure wearing a cost-savings costume.

**C — Haiku for reactive generations (save ~$0.013 more). Quality cost:
HIGH — NOT RECOMMENDED.** Every voice was validated on Sonnet; all six
checkpoints, the readability hard edge, the fabrication discipline. S2
clears the bar without it. Hold in reserve; test only if real-world costs
come in above model.

**E — prepared answers (SH-11).** Its own analysis caps it at ~5.2% of
traffic. Immaterial to this decision.

## 5. Target, floor, and the pricing statement

- **Target: ≤ $0.10/turn standard pricing** (S2 has margin against it under
  both TTL pricings). At 30 turns/hour that is ≤ $3.00/hour.
- **Floor: ~$0.063/turn.** One voice per turn ≈ 1.04× solo — the table's
  irreducible premium is the additional voices themselves, ~$0.033 per
  additional generation. **A real table cannot cost less than ~1.4× solo**
  (S2's ratio); anything cheaper has stopped being the product.
- **For the paid tier**: at S2, an hour of table time costs ~$2.60–2.85 in
  API. A subscription must clear that per expected usage-hour; Table mode
  as free tier is not viable at any scenario above the floor.

## 6. What this analysis cannot settle, and the order of operations

The log predates the Voice Rebuild and the TTL change. **First
implementation step: re-run the fixed baseline (~$3.39)** to reprice S0/S2
on the real current system. Then, per the brief's interference rule, B and
D wait for nothing further (the swaps landed, PR #9 merged), but they touch
the shared retrieval/governance stack the solo checkpoints were measured
against — so they get a solo regression checkpoint after landing. Lever A
is Phase 2's opening design question, carried there with its risks named.

**Phase 1 verdict: the table survives the cost test.** It was killed-if-
unfixable and it is fixable — S2 clears Mark's line by ~45% with margin for
the TTL uncertainty, without touching any validated voice. The gating
decision is not financial; it is the selective-speaking design, which is
exactly the question Phase 2 exists to answer well.

---

## Correction (2026-08-10, after reconciling with the api-cost thread)

Section 2's headline — "today's table is already over the line" under 1h-TTL
write pricing — was a **fast-pacing sensitivity bound presented too strongly.**
The 1h TTL was adopted deliberately (commit 1d8e952, cost-reduction scope item
1) for **reflective pacing** (~6 turns/hr), exactly the regime where fewer
pause-driven cache rewrites outweigh the 2× write price. At that pacing the
same S0 table is ~$1.05/hour, deep inside every line. The scenario ordering,
the S2 target, and the floor are unchanged; what moves with pacing is only
how urgent S1's plumbing is. The pacing basis for the $0.25–1.00/hr funding
band is the api-cost thread's open question, not this one's.

Also superseded by events: Mark moved the fleet to Haiku (2026-08-10), which
re-prices every scenario down ~40% again — S2 on Haiku lands near $1.00/hr at
30 turns/hr, ~$0.20/hr reflective. The selective-speaking design question is
unchanged by any of this; it remains Phase 2's opening question.

---

## Addendum (2026-08-10) — the September price change, and why Haiku is immune

Sonnet-5's introductory pricing ($2/$10 per MTok) expires **31 August 2026**,
reverting to standard ($3/$15). Haiku 4.5 has **no intro pricing to expire** —
its $1/$5 is already the standard rate. Priced on the same measured token
shape, generation following `llm_model` and the Haiku classifier tier held
constant:

| | Aug (Sonnet intro) | **Sep (Sonnet standard)** | change | **Haiku — now and in Sep** |
|---|---|---|---|---|
| solo / turn | $0.0486 | $0.0603 | **+24%** | **$0.0369** |
| — at 30 turns/hr | $1.46 | $1.81 | | **$1.11** |
| — at 6 turns/hr | $0.29 | $0.36 | | **$0.22** |
| table / turn | $0.1270 | $0.1585 | **+25%** | **$0.0956** |
| — at 30 turns/hr | $3.81 | $4.75 | | **$2.87** |
| — at 6 turns/hr | $0.76 | $0.95 | | **$0.57** |

**The Haiku switch does two things, not one.** It cuts ~40% off the bill, and
it *removes the 1 September increase entirely* — the Haiku column is
identical either side of the date. Against what the fleet would have paid in
September on Sonnet, the switch is **−39% solo / −40% table**; against what
August is actually billing today it is **−24% / −25%**. Both are true; the
second is the one that will show up on the next invoice, and the smaller of
the two, so it is the honest number to plan against.

**Two corrections this addendum forces:**

1. **Every "start" figure in this document and in my earlier reporting
   ($0.0603 solo, $0.1585 table) was priced at STANDARD rates** — following
   the B-COST report's own convention of quoting the stable figure. That is
   September's price, not today's. Actual August spend is ~24% lower. I was
   comparing Haiku against a Sonnet price that is not yet in effect, which
   flattered the saving against present spend.
2. **The api-cost thread's "+30%" is ~+24–25% on this token shape.** Their
   reasoning is right — the Haiku classifier tier is unaffected, so the
   blended increase is well under Sonnet's own +50% — and the difference is
   just how much of the bill is generation in the measured conversations
   versus their estimate. Their conclusion stands: nothing in the cost plan
   needs re-deriving.

**What this means for the spending limit.** The console cap should be set
against Haiku-at-standard, which is now a flat rate with no scheduled
increase ahead of it. The 1 September date stops being a cost event for this
project the moment the Haiku switch deploys — it is currently on a branch,
not on `main`.
