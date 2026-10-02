# SH-11 — The Answer Bank: Design, What Was Built, What's Left

**Date:** 2026-07-31. **Status:** mechanism built and verified offline; zero
real content exists yet; zero UI exists yet. Not live in any sense a
participant could reach.

## 1. What this actually is, and what it is not

Grounded in `Archive/Technology-Pass2-2026-08/Pass3/cost_floor_model.py` STEP 5 (restored
to `main` alongside this work - it existed only on an orphaned branch,
stranded by the branch-chaining cleanup, never superseded). Its finding:
serving a prepared answer instead of generating live can only happen when
**three things hold at once** - the participant took the question-first
door (~1/3 of entries), tapped a starter rather than typing freely, and
stayed on the curriculum's own walk without deviating. Combined: **~5.2%
central estimate**, not the 30-50% first assumed. Real, worth building for
the quality/consistency win on curriculum-path traffic (the Task Board's own
framing) - not a big cost lever.

**It is not a general FAQ or RAG answer-matcher.** It serves exactly one
thing: an exact, unmodified tap on a known Guided-Questions curriculum
starter (`Build/Ministry/Features/Guided-Questions/Design/
CiC_Guided_Questions_Curriculum_V1_0.json` - 100 real, safety-reviewed
questions, 4 roles x 5 sets x ~4.5 questions each), for a single-world
(interview-mode) session only. Never a paraphrase, never a free-typed
question that merely resembles a starter, never Table mode.

**Why Table mode is out of scope here, not just deferred:** the cost
model's own table bank is "the expensive one, ages fastest," and Table is
becoming a paid-tier feature per the 2026-07-31 Table-mode product-shape
decision - that needs its own subscription-gating infrastructure (folded
into SH-12), which this build doesn't touch.

## 2. The hard constraint that shaped the whole design

**"No question here has faced a live model"** - the curriculum doc's own
words. Nobody has verified these 100 questions produce good live answers
yet. That's a real content-quality gate, not a formality: caching a bad
first-draft answer would serve it to every future participant who taps that
same question, which is a much higher-stakes mistake than one bad live
turn. So this build is deliberately split into two halves that don't
depend on each other shipping together:

- **The mechanism** (this build): storage format, lookup, live-shaped
  serving, structured hit/miss logging. Fully built and verified. Contains
  zero real content.
- **The content** (not this build, needs a live key): actually running the
  100 questions against a live model, world by world, and reviewing what
  comes back before it's trusted to serve repeatedly.

## 3. Architecture

**Client signal, not text inference.** A curriculum tap is identified by an
explicit `curriculum_ref: {role, set_id, question_order}` on
`SendMessageRequest` (`CurriculumRef` in `app/main.py`) - present only when
a (future) UI renders this app's own exact curriculum text as a tappable
button. Never inferred from parsing free-typed text; that is what makes
"never serves a paraphrase" true by construction, not by hoping a fuzzy
matcher never misfires.

**Defense in depth.** Even given a `curriculum_ref`, `app/answer_bank.py`'s
`lookup()` still normalize-compares the participant's actual message text
against the bank entry's own stored question text, and refuses to serve on
any mismatch - a second, independent safeguard against a future UI bug or a
tampered request, not just trusting the ref alone.

**Drop-in substitution, not a parallel code path.** `try_answer_bank()`
returns exactly the same shape `app.graph.nodes.representative_engages()`
returns; `stream_answer_bank()` matches `stream_representative_turn()`'s
yield contract exactly. Both return `None` on any kind of miss, and both
call sites in `main.py` do "try the bank, fall through to the unchanged
live call on `None`" - so a miss is provably byte-identical to how the app
already behaved before this existed. This is also why the failure mode of
"bank not populated yet" is safe by default: an empty or missing bank file
means every request just falls straight through to live generation.

**Storage:** one JSON file per world
(`cic-poc/backend/data/answer_bank/<world_id>.json`), matching this app's
existing per-world data layout. Self-invalidating cache (mtime/size keyed),
same pattern as `app/graph/world_sources.py`.

**Measurement built in from day one.** `app/answer_bank_logging.py` logs
every hit and miss whenever a `curriculum_ref` is present (never for
ordinary free-typed traffic, which was never a candidate) - `[answer_bank_decision]`
lines, parseable the same way `scripts/cost_baseline_runner.py` already
parses `[llm_usage]` lines. This is what would let someone eventually check
the 5.2% estimate against real traffic, the same way the length-ceiling and
over-settling instrumentation shipped earlier tonight did for their own
mechanisms.

## 4. What was verified, and how

No live API key used or needed - `scripts/answer_bank_check.py` (14/14
checks) exercises the real `/api/session/{id}/message` and
`/message/stream` endpoints via FastAPI's `TestClient`, with the test
world's retrievers pre-seeded to skip FAISS/HuggingFace entirely (real
retrieval correctness is `scripts/redesign_battery.py`'s job, already
covered there - this script's job is the bank's own wiring). Confirmed: a
bank hit serves the exact precomputed text and citations, both non-
streaming and token-by-token streaming; a text-mismatched `curriculum_ref`
and an ordinary free-typed message both fall through to live generation
unaffected; no artifacts left in the repo. Full regression run clean
afterward: `redesign_battery.py` 68/68, `giving_flow_check.py` 18/18,
`answer_bank_check.py` 14/14, `S6.2_length_ceiling_observability_gate.py`
22/22.

`scripts/build_answer_bank.py` (the precompute script) was verified
mechanically the same way - chain-threading, mock-generation integration,
and bank-file merging all confirmed correct - but **never run against a
real model**, and its own output carries a loud banner refusing to let
that be mistaken for real content (see the script's own top-of-file
warning). It is not run as part of this build.

## 5. What's left to actually do (yours, not mine)

1. **Authorize a real build run** (needs a live API key). One command per
   world: `python scripts/build_answer_bank.py --world <world_id> --all`
   (drop `--all` to scope to one role/set for a smaller first pass). Cost
   note: this calls the same live code path an ordinary turn takes
   (`representative_engages`), which is the point - a precomputed answer
   must be indistinguishable in quality from a live one - but that means
   standard per-call pricing, not the cost model's Batch-API-discounted
   estimate. Budget roughly 2x that figure for a first synchronous run;
   Batch support is a named, real follow-up, not attempted here.

2. **Review before trusting it.** Since none of these 100 questions have
   faced a live model yet, someone should actually read a sample of what
   comes back - at minimum spot-check a full chain or two per world - before
   the bank file is treated as safe to serve to real participants. This
   build has no automated quality gate for that; it's a human judgment call
   the curriculum doc itself asks for ("log what testers type... that
   harvest is the evidence for V1.1").

3. **The curriculum-picker UI** (Tier 3 of
   `CiC_QuestionFirst_Entry_Design_V0_1.md`) is explicitly the front-end
   thread's domain to build, not built here - "zero UI code exists" stands
   as of this entry. Until it exists, `curriculum_ref` is never populated by
   any real client, so this mechanism has nothing to serve regardless of
   how much content gets built. Worth sequencing: content review (#2) can
   happen before or in parallel with the UI work, since they don't depend
   on each other.

4. **Decide whether/when to actually run the build**, per curriculum-doc
   priority - all six solo worlds are wired identically
   (`SOLO_WORLDS` in the build script), so this is a "how much to spend
   now vs. later" question, not a technical blocker.
