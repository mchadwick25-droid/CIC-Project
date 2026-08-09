# Fable thread brief — the multi-Representative table: can it be afforded, and can it carry 1A/1B?

**Written 2026-08-09, at the close of the single-Representative Voice
Rebuild.** Paste this into a fresh Fable thread. It carries the measured
facts so the thread starts from evidence, names what is already decided so
nothing settled is re-litigated, and **phases the work so the question that
can kill the feature is answered before anyone designs for it.**

---

## Read this first: the work is phased, and the phases are not optional

**PHASE 1 — cost feasibility. Analysis only. Touches no code.**
Can a 3-Representative table be run at a price the program can pay? Produce
a cost architecture and an honest floor. **This phase gates the next one.**

**PHASE 2 — quality: research, design, blueprint, build.**
Bring 1A/1B and the Voice Rebuild's upgrades to the four-voice dialogue.
**Do not start this until Phase 1 has an answer Mark has accepted.**

Why this order, stated plainly: Mark has killed a feature on cost before
(`S6.2_M_table_cap_and_trr_cost.md` stopped a TRR re-run mid-flight). If the
floor turns out to be above what the program can pay, then a table design, a
blueprint and a build are all wasted work. His own words: *"we can't afford
$5 an hour for hundreds much less thousands of participants"* — and at the
measured rate that figure is real, not rhetorical. **Find out whether this
survives before investing in how it should feel.**

---

## PHASE 1 — the cost question

### What is already measured. Do not re-derive it.

Source: `Ministry/Technology/Pass2/baselines/cost_baseline_2026-07.md` and
its committed raw log, standard pricing. Every figure below was reconciled
against the report's own total ($3.3924) before being quoted.

| | solo turn | **table turn (3 worlds)** |
|---|---|---|
| cost | $0.0603 | **$0.1585** (2.63×) |
| LLM calls | 13.9 | **27.1** |

**At $0.1585/turn, ~31 participant turns is $4.91.** The $5/hour Mark is
refusing to pay is the measured number.

Where a table turn's money goes:

| call site | calls/turn | $/turn | share |
|---|---|---|---|
| **main_response** (Sonnet) | 2.8 | 0.0935 | **59%** |
| retrieval_filter_lexicon (Haiku) | 5.8 | 0.0138 | 9% |
| retrieval_filter_story (Haiku) | 5.5 | 0.0131 | 8% |
| over_settling_adjudication (Haiku) | 1.5 | 0.0127 | 8% |
| turn_selector (Haiku) | 2.9 | 0.0072 | 5% |
| drift_detection (Haiku) | 2.1 | 0.0048 | 3% |

**The dominant fact: ~2.8 full Sonnet generations per participant turn.**
Three Representatives each compose an answer. The entire Haiku governance
and retrieval stack — 24 of the 27 calls — is 41% combined.

### Three things to internalise before proposing anything

1. **Trimming prompts will not fix this.** The big static blocks already sit
   behind 1-hour cache breakpoints (`_cached_system_message`, and
   `table_discourse.py`'s own marker). Shrinking cached text saves cache-read
   tokens at 0.1× — pennies. **The cost is generation count, not prompt size.**
2. **Retrieval filtering runs per Representative** — 11.3 Haiku calls per
   table turn against 4.9 solo. Largest non-generation line, most obviously
   shareable.
3. **The governance stack runs per Representative turn too.** Whether all of
   it must is a real question, not an assumption.

### The levers, and the one that matters

- **Do all three Representatives speak every turn?** 2.8 generations per turn
  *is* the cost problem. One or two speaking, with the others entering only
  when they genuinely differ, is by far the largest available saving — and it
  goes directly at what a table is *for*. **This is the central tension and
  deserves the most rigor in the thread.** Do not resolve it by assertion in
  either direction.
- **Share retrieval across the table** rather than filtering per
  Representative (11.3 → possibly ~4 Haiku calls/turn).
- **Model tiering for generation**, and what it costs in voice fidelity.
  Everything Sonnet does at a table is `main_response`; nothing else.
- **Governance scope** — per Representative turn, or per participant turn?
- **Non-model levers**: prepared answers (SH-11 exists in code but has no bank
  data for any world, and its own analysis puts its ceiling at ~5.2% of
  traffic), and the paid-tier pricing structure.

### Phase 1 deliverables

1. A cost architecture with a **target number**, and what each lever buys.
2. **An honest floor.** If the cheapest table that still deserves the name
   costs more than the program can pay, **say the number and say so.** A clear
   *"this cannot be done under $X/turn without ceasing to be a real table"* is
   a usable, respected answer — not a failure.
3. A statement of what each saving costs in quality, so Mark is trading with
   his eyes open.

### The one interference rule

**Do not modify the shared retrieval or governance stack until the five
pending world swaps have landed and PR #9 has merged.** Levers 2–4 all touch
components the six single-Representative checkpoints were measured against;
changing them mid-flight invalidates baselines that just went green and
destroys the ability to attribute cause. Phase 1 is analysis, so this costs
nothing — it only bars premature implementation.

Everything else is clear: **`app/prompts/table_discourse.py` is app-side only
and never enters the WRS prompt assembly** (verified 2026-08-09), so table
work cannot collide with `assembly_identity`, the swaps, or the per-world
checkpoints.

---

## PHASE 2 — the quality question (only after Phase 1 clears)

**Q1: is carrying 1A/1B to the table a Representative change, a Table change,
or both?** Answer with evidence. There is already a strong measured lead.

### The finding that probably answers it

**`app/prompts/table_discourse.py` is the one conversational-design block the
entire 1A pass never touched.** Its last commit is an unrelated merge from
`main`. Measured against the bar every other voice now meets:

| block | words | FK | FRE | B2 floor |
|---|---|---|---|---|
| `REACTIVE_TURN_GUIDANCE` | **1,845** | **14.13** | 48.13 | **BREACH** |
| `OPENING_TURN_LARGE_TABLE_GUIDANCE` | 254 | **17.66** | 42.08 | **BREACH** |
| `CROSS_WORLD_VOCABULARY_GUIDANCE` | 161 | **16.90** | 29.09 | **BREACH** |

This is the Facilitator defect repeated exactly. There the root cause was not
the stated rules but that *the prompts were written at FK 11.3–11.5 and so
taught density by example*; fixing the prose moved the Facilitator from FK
12.4 to 8.37 with every substantive constraint kept.
`REACTIVE_TURN_GUIDANCE` is worse than the Facilitator ever was, it is the
longest conversational block in the system, and at a table it shapes **three**
generations per participant turn.

Working hypothesis to **test, not assume**: Q1 is mostly a *Table* change
concentrated in one file, because the Representative-side work
(`_HOW_YOU_ENGAGE`, the records, the demonstrations, the guards) is already
carried by every voice whether it speaks alone or at a table.

**Do not conflate this with Phase 1.** That block is cached. Rewriting it buys
readability and conversational shape and **roughly zero dollars.**

### Phase 2 deliverables

A defensible answer to Q1 with its evidence, and a work list at the same grain
as `Ministry/Technology/Pass2/VR_1A_WORKLIST.md`.

---

## Already decided — carry, do not reopen

- **Table cap is hard at 3 Representatives** (`S6.2_M_table_cap_and_trr_cost.md`,
  Mark verbatim: *"we are hard capping the number of representatives at a
  table at 3, 5 costs too much to run"*), already enforced as `world_ids[:3]`.
  Three Representatives + Facilitator = the four-voice dialogue in question.
- **Table is the planned paid tier**; single-Representative Deep Interview is
  the free tier (2026-07-31 product-shape decision, enforced at the entry
  point in `WorldSelector.tsx`). Pricing structure is a live lever.
- **1A is the goal, 1B the constraint**, and readability is a **hard edge** —
  one breaching turn fails a world. The four decision documents stand:
  `VR_1A_NorthStar_Readability_Target`, `VR_1A_Writing_Standard`,
  `VR_1A_Conversation_Palette`, `VR_1A_Representative_Voice_Design`.
- **The Goodhart rule.** Every diversity/palette metric is observational,
  never a target. A Representative performing variety is the failure the
  measurement exists to notice.
- **Emitted is what ships**; per-world failure measures; the sustained bar
  consults `matched_contested`.

## How to work

- **Measure before proposing.** The instrument exists:
  `scripts/cost_baseline_runner.py --run` drives a fixed conversation set
  through the real app and attributes every call exactly. The fixed set
  (`cost_baseline_conversations.json`) **must not change**, or comparability
  dies.
- **Every quality claim gets a number or a named human read.** That discipline
  caught three of my own errors during the single-Representative rebuild that
  reading the code did not.
- **Report what does not work.** The 1A pass's most useful outputs included a
  records fix backed out when the behaviour did not reproduce, an
  engagement-demonstration hypothesis the battery did not confirm, and a claim
  of mine — *"every voice now meets the B2 floor"* — corrected on the next
  measurement. A brief that only reports wins is not usable.

## Known instrument gap this thread will hit

The 8-turn probe battery is **adversarial by design**, which makes it blind to
exactly the behaviours a table exists for. Measured 2026-08-09: the engagement
demonstrations moved turns-ending-on-a-question **0 → 0** for Marius across his
pre- and post-v2 checkpoints, while the same behaviour appears readily in
ordinary conversation. **Before grading table quality with the existing
battery, check whether it can see what is being asked of it.** A conversational
probe set may have to be built first — `scripts/variance_probe.py` and
`scripts/cross_world_probe.py` are the closest existing models.

## State of the single-Representative work at the time of writing

Six Representatives live and rebuilt; four of five v2 checkpoints returned
PASS on every hard bar (Marius, Theon, Papnoute, Yausep), Albina's running.
Five worlds sit in `PENDING_RECHECKPOINT` awaiting their swap. PR #9 is open,
CI green, and carries the whole rebuild to a site currently serving `main`.
