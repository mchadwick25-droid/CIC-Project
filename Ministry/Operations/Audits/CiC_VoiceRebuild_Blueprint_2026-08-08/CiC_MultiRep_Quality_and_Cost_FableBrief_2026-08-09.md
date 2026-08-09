# Fable thread brief — bringing 1A/1B quality to the multi-Representative table, at a cost that survives scale

**Written 2026-08-09, at the close of the single-Representative Voice
Rebuild.** This is the prompt for a fresh Fable thread. It carries the
measured facts so that thread starts from evidence rather than from
scratch, and it names what is already decided so nothing settled gets
re-litigated.

---

## The two questions, stated exactly

**Q1 — quality.** Everything the Voice Rebuild achieved for a single
Representative (1A accessible rigor at CEFR B2 / FK 8–10, 1B conviction and
fidelity intact, three-level transparency, the conversation palette, the
Goodhart discipline) now has to hold in a **3-Representative table plus the
Facilitator — four voices**. Is that a *Representative* change, a *Table*
change, or both? Answer it with evidence, not intuition.

**Q2 — cost, and it is existential.** A table turn currently costs **2.63×**
a solo turn. Mark: *"we can't afford $5 an hour for hundreds much less
thousands of participants."* At the measured rate that figure is real, not
rhetorical (see below). **If multi-Representative cannot be made
dramatically cheaper, it comes out of the program.** The thread's job is to
find out whether it can, and to say so plainly if it cannot.

---

## What is already measured — do not re-derive this

Source: `Ministry/Technology/Pass2/baselines/cost_baseline_2026-07.md` and
its committed raw log. Standard pricing. Verified against the report's own
totals ($3.3924) before being quoted here.

| | solo turn | **table turn (3 worlds)** |
|---|---|---|
| cost | $0.0603 | **$0.1585** (2.63×) |
| LLM calls | 13.9 | **27.1** |

**At $0.1585/turn, roughly 31 participant turns is $4.91 — which is exactly
the $5/hour Mark is refusing to pay.** The number he is objecting to is the
real one.

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
Three Representatives each compose an answer. Everything else — the whole
Haiku governance and retrieval stack, 24 of the 27 calls — is 41% combined.

Three consequences worth stating before any brainstorming:

1. **Trimming prompts will not fix this.** The big static blocks already sit
   behind 1-hour cache breakpoints (`_cached_system_message`,
   `table_discourse.py`'s own marker). Shrinking cached text saves cache-read
   tokens at 0.1× — pennies. The cost is generation count, not prompt size.
2. **Retrieval filtering runs per Representative** — 11.3 Haiku calls per
   table turn against 4.9 solo. This is the largest non-generation line and
   the most obviously shareable.
3. **The governance stack runs per Representative turn too.** Whether all of
   it must is a real question, not an assumption.

---

## Already decided — carry, do not reopen

- **Table cap is hard at 3 Representatives** (`S6.2_M_table_cap_and_trr_cost.md`,
  Mark verbatim: *"we are hard capping the number of representatives at a
  table at 3, 5 costs too much to run"*). Already enforced in code
  (`world_ids[:3]`). Three Representatives + Facilitator = the four-voice
  dialogue in question.
- **Table is the planned paid tier**; single-Representative Deep Interview is
  the free tier (2026-07-31 product-shape decision; `WorldSelector.tsx`
  keeps that boundary at the entry point). Pricing structure is therefore a
  live lever, not a fixed constraint.
- **1A is the goal, 1B the constraint**, and readability is a **hard edge**
  — one breaching turn fails a world. All four decision documents stand
  (`VR_1A_NorthStar_Readability_Target`, `VR_1A_Writing_Standard`,
  `VR_1A_Conversation_Palette`, `VR_1A_Representative_Voice_Design`).
- **The Goodhart rule.** Every diversity/palette metric is observational,
  never a target. A Representative performing variety is the failure the
  measurement exists to notice.
- **Emitted is what ships**; per-world failure measures; the sustained bar
  consults `matched_contested`.

---

## The finding that most likely answers Q1

**`app/prompts/table_discourse.py` is the one conversational-design block
the entire 1A pass never touched.** Its last commit is an unrelated merge
from `main`. Measured against the same bar every other voice now meets:

| block | words | FK | FRE | B2 floor |
|---|---|---|---|---|
| `REACTIVE_TURN_GUIDANCE` | **1,845** | **14.13** | 48.13 | **BREACH** |
| `OPENING_TURN_LARGE_TABLE_GUIDANCE` | 254 | **17.66** | 42.08 | **BREACH** |
| `CROSS_WORLD_VOCABULARY_GUIDANCE` | 161 | **16.90** | 29.09 | **BREACH** |

This is the Facilitator defect repeated exactly. There, the root cause was
not the stated rules but that *the prompts were written at FK 11.3–11.5 and
so taught density by example*; fixing the prose moved the Facilitator from
FK 12.4 to 8.37. `REACTIVE_TURN_GUIDANCE` is worse than the Facilitator
ever was, it is the longest single conversational block in the system, and
in a table it shapes **three** generations per participant turn.

So the working hypothesis — which the thread should test, not assume — is
that **Q1 is mostly a Table change, concentrated in one file**, because the
Representative-side work (`_HOW_YOU_ENGAGE`, the records, the
demonstrations, the guards) is already carried by every voice whether it
speaks alone or at a table.

**Important and easy to get wrong: this is a QUALITY fix, not a cost fix.**
That block is cached. Rewriting it buys readability and conversational
shape; it will not move the $0.1585.

---

## What the thread should actually produce

1. **A defensible answer to Q1** — Representative vs Table vs both — with
   the evidence for it, and a concrete work list at the same grain as the
   1A worklist.
2. **A cost architecture for multi-Representative**, aimed at a stated
   target. Candidate levers, all needing analysis rather than assertion:
   - **Do all three Representatives speak every turn?** 2.8 generations per
     turn is the entire cost problem. One or two speaking, with the others
     entering only when they genuinely differ, is the single largest
     available saving — but it directly threatens what the table is *for*.
     This is the central design tension and deserves the most rigor.
   - **Share retrieval across the table** rather than filtering per
     Representative (11.3 → possibly 4 Haiku calls/turn).
   - **Model tiering for generation**, and what it costs in voice fidelity.
     Everything Sonnet does at a table is `main_response`; nothing else.
   - **Governance scope** — must every monitor run per Representative turn,
     or per participant turn?
   - **Non-model levers**: prepared answers (SH-11 exists in code but has no
     bank data for any world, and its own analysis says it only ever covers
     ~5.2% of traffic), and the paid-tier pricing structure.
3. **An honest floor.** If the cheapest table that still deserves the name
   is above what the program can pay, say the number and say so. Mark has
   already killed features on cost (`S6.2_M_table_cap_and_trr_cost.md`
   stopped a TRR re-run mid-flight). A clear "this cannot be done under
   $X/turn without ceasing to be a real table" is a usable answer.

---

## How to work

- **Measure before proposing.** The instrument already exists:
  `scripts/cost_baseline_runner.py --run` drives a fixed conversation set
  through the real app and attributes every call. The fixed set
  (`cost_baseline_conversations.json`) must not change, or comparability
  dies.
- **Every quality claim gets a number or a named human read.** That is the
  discipline the single-Representative rebuild ran on, and it caught three
  of my own errors that reading the code did not.
- **Report what does not work.** The 1A pass's most useful outputs included
  a records fix backed out when the behaviour did not reproduce, an
  engagement-demonstration hypothesis the battery did not confirm, and a
  claim of mine ("every voice now meets the B2 floor") corrected on the next
  measurement. A brief that only reports wins is not usable.

## Known instrument gap the thread will hit

The 8-turn probe battery is **adversarial by design**, and that makes it
blind to exactly the behaviours a table is for. Measured today: the
engagement demonstrations moved turns-ending-on-a-question **0 → 0** for
Marius across pre- and post-v2 checkpoints, while the same behaviour appears
readily in ordinary conversation. Before grading table quality with the
existing battery, check whether it can see what is being asked of it. A
conversational probe set may have to be built first.
