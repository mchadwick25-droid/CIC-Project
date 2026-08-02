# The Answer Bank, Full System — Research & Design V0.1

**Status:** For Mark, 2026-07-31. Research and design only — no code, no build, per the
launch prompt. Answers the scoping conversation Task Board named for SH-7 and extends
SH-11 toward the system it always pointed at. **Nothing in this document changes
`cic-poc`, the curriculum content, or any governing document.**

**Tagging discipline**, inherited from `cost_floor_model.py`: **[M]** measured — read
directly off committed files or code. **[E]** estimated — measured shapes + a stated
formula. **[S]** speculative — reasoned, not validated; no pilot data exists yet for any
of this document's served-fraction or clustering claims, and that is stated at every
place it matters, not just here.

---

## 0. What was read, and the one finding that reorganizes everything below

Every file the launch prompt named was read in full, plus the build script
(`scripts/build_answer_bank.py`), the live serving code path
(`app/graph/nodes.py`'s `select_next_speaker`), the fabrication-adjudication node and
its two-stage structure, the Design Study's full fit-test catalog, the Calibration
Results, the World Coverage Cards, and the Gap Closures document.

**The reorganizing finding:** SH-11's storage schema is already keyed by
`(role, set_id, question_order)` inside a per-world JSON file, looked up by an explicit
client signal, with a defense-in-depth text match, and a "miss falls through to live"
contract. **Nothing about that architecture is sized to 100 questions.** Widening the
static bank (item 1) is not a redesign — it is more entries in the same table, built by
the same script, served by the same unmodified `lookup()`. The real design work below is
almost entirely about *content* (item 1), a *genuinely new operation this codebase has
never done before* (item 2's synthesis), and *why the same architecture does not
generalize to Table mode* (item 3) — not about changing what SH-11 already built. That
reframes the whole brief: this is not "SH-11 v2," it is "SH-11's mechanism, unchanged,
fed by two new content pipelines with very different risk profiles, plus an honest no
for the third."

---

## 1. SH-7 × SH-11 — how the ~150 relates to the 100

**Answer: superset, same derivation method, not a different one.** The Task Board's own
SH-7 language — "the ~150 most probable interview questions" — and the Design Study's
governing finding are the same claim from two directions. The Design Study's Part 0
finding (three independent literatures: Baram-Tsabari on spontaneous vs. school-prompted
questions, Fuller on unexpressed doubt, the epistemic-injustice literature on
pre-emptive self-silencing) is that **the question already exists; the affordance
authorizes it, it does not invent it.** That is a claim about *method*, not headcount:
the 100 questions were derived by (a) stating role needs from evidence before drafting
anything, (b) building a fit-test instrument in advance (10 tests, later corrected to 12
by live calibration), (c) authoring against it, (d) live-testing a sample and letting the
evidence overrule the desk-check where it disagreed (0 of 5 predicted cuts survived;
2 new tests were added from *observed* failures, not reasoned ones). SH-7's "~150" is
not asking for a different selection method — it is asking to run more of the same
method further, because 100 was where the first pass stopped, not where the market data
stopped.

**Concretely, what SH-7 is:**

1. **Keep the existing 100 unchanged.** They already passed the fit-test/calibration
   process; nothing here proposes touching them beyond the ordinary content-drift
   maintenance this project already does.
2. **Author ~50 more, same process, same instrument.** Design Study §1.1's own General
   role section already surfaces real, ungathered demand this project knows about but
   hasn't authored into starters yet — its own Google-autocomplete harvest ("did early
   christians eat pork," "celebrate birthdays," "pray to saints," "believe in the
   trinity") only partially overlaps the current 20 sets. The Study explicitly names a
   **failed harvest** (r/AskHistorians, r/AcademicBiblical — blocked automated access)
   as "worth doing properly; it is the closest available proxy for our actual
   interaction" — that is a concrete, already-identified place to look for the next 50,
   not a blank page.
3. **Do NOT reintroduce the cancelled role × world matrix.** The curriculum doc is
   explicit that questions are role-generic by design, licensed by the live calibration
   (a generic question meeting a thin record produced an honest calibrated answer, not a
   failure). A "different derivation method" that authors per-world variants would be
   reopening a design decision this project already made and verified wrong, not a
   neutral alternative.
4. **The two SH items converge on the same real growth pipeline.** The curriculum doc's
   own closing section ("What this document does not establish") names the actual
   evidence for V1.1: *"log what testers type into the box... that harvest, not this
   document, is the evidence for V1.1."* **That is item 2's data source, verbatim.**
   SH-7 has a natural two-phase shape: **Phase A**, desk-authored expansion now, same
   process as the 100, reaching ~150 by construction (100 + ~50 ≈ SH-7's own headline
   number — worth naming as a clean convergence, not a coincidence, since both numbers
   trace to the same four-role, sets-of-four-or-five-questions shape). **Phase B**, once
   real pilot traffic exists, mining the actual logged free-typed questions
   (`app/transcript_logging.py`'s `messages` table, already built, currently off by
   default) for what real participants ask that neither the 100 nor Phase A anticipated.
   **Phase B and item 2 are not two separate things that happen to share a birthday —
   they are the same pipeline being asked two different questions of the same data**
   (Phase B: "what should get authored as new door-opening content" — a human,
   editorial decision; item 2: "what should get synthesized as a servable canonical
   answer" — a narrower, higher-bar operation, see §3). Recommend naming this
   explicitly wherever SH-7 next gets scoped, so the two threads don't independently
   build overlapping traffic-mining tooling.

---

## 2. Item 1 — the broader static bank for interview mode

### 2.1 What actually needs designing (not much — content, not architecture)

`app/answer_bank.py`'s `_load_bank()` reads every entry in a world's JSON file and keys
them by `(role, set_id, question_order)`; `build_answer_bank.py` iterates
`curriculum["roles"] → sets → questions` from the JSON data contract with no cap and no
awareness of "100." **Growing the curriculum JSON from 100 to 150 entries requires zero
changes to `app/answer_bank.py`, `app/answer_bank_logging.py`, or the build script.**
The only real design questions are (a) content generation, already answered in §1, and
(b) whether the served fraction is worth it, addressed next.

### 2.2 Re-deriving the served fraction — the launch prompt's explicit ask

The 5.2% central estimate is a product of three gates, none of which is "how many
questions exist":

| Gate | What it measures | Function of catalog size? |
|---|---|---|
| P(question-first door) | Entry-flow choice, ~1/3, no default among 3 co-equal doors | **No** — a pure UI/entry-flow property |
| P(taps a starter) | Free-typed vs. tapped, on that door | **Partially** — a richer catalog can better match real intent |
| P(stays on the walk) | Deviation ends the chain | **Weakly** — richer content might reduce the urge to deviate, marginally |

**[S] Re-derivation, content-growth-only scenario (150 questions, same UI/entry gates
unchanged):**

| | pd (unchanged, structural) | pt (catalog-quality-dependent) | ps (weakly catalog-dependent) | Served |
|---|---|---|---|---|
| Optimistic | 0.33 | 0.55 *(+5pt: catalog now covers more real intent)* | 0.61 | **11.1%** |
| Central | 0.33 | 0.38 *(+3pt)* | 0.46 | **5.8%** |
| Conservative | 0.25 | 0.21 *(+1pt: poorly-targeted additions barely move behavior)* | 0.30 | **1.6%** |

**The honest finding: this does not meaningfully move the needle.** 5.2% → ~5.8%
central is the same order of magnitude, not a step change, because **catalog size was
never the binding constraint.** The two dominant gates — only a third of participants
take the question-first door at all, and any deviation from the walk kills the bank hit
— are structural properties of the *entry flow*, unrelated to how many starters exist
behind door two. **This uplift is also conditional, not free**: it only materializes if
the ~50 new questions genuinely fill real gaps (SH-7's own framing, §1) rather than
padding the catalog with more of the same territory the existing 100 already cover. A
poorly-targeted expansion nets closer to the conservative row — essentially flat.

**Where a "meaningfully larger fraction" (the launch prompt's own phrase) would
actually have to come from: gate-widening, not catalog-widening.** If a tappable
canonical starter could be surfaced *outside* the question-first door — e.g., an
in-conversation "others have asked..." suggestion available regardless of entry
choice, fed by item 2's real-traffic-validated catalog — that loosens pd itself, not
just pt within it. This is real, structurally could matter far more than §2.2's ~6%,
and is **explicitly out of scope for this document**: it is a new UI/UX surface (not
named in `CiC_QuestionFirst_Entry_Design_V0_1.md`'s three-door model), it depends on
item 2 having already produced validated entries (pilot-traffic dependency, see §5),
and its real uptake rate is currently unmeasurable — putting a number on it now would
be exactly the "inherited optimism" the launch prompt asked not to repeat. **Flagged
here as the one lever worth a real design pass once item 2 has live data, not modeled
as a number.**

### 2.3 Cost — genuinely not the constraint

Running `cost_floor_model.py` directly [M]: the current 100-question solo bank build is
**$14 at the Batch API's modeled 50% discount**, or **~$28 at the synchronous pricing
the build script actually runs at today** (per its own "budget roughly 2x" note — Batch
isn't implemented). A 150-question bank scales roughly linearly with content volume:
**[E] ~$21 batch-equivalent / ~$42 synchronous for a first full run across all 6 solo
worlds.** This is trivial next to reviewer time. **The real cost of item 1 is human
review labor** (§2.4), not API spend — worth saying plainly so the sequencing decision
in §5 isn't made on the wrong cost axis.

### 2.4 What does NOT change: the live-model gate

Per "what not to break": **"no question here has faced a live model" applies to the new
~50 exactly as it applied to the original 100.** A well-designed question is not
evidence it produces a good live answer — the calibration battery's own headline (all
five predicted cuts were wrong, and the two real failures happened on questions marked
*safest*) is the standing proof that desk judgment and live behavior diverge in ways
neither direction predicts. Any new content added under SH-7 needs the same two-step
SH-11 already named and left undone for the original 100: a real build run, then a human
read of a sample before the bank file is trusted. **This is not a new gate for the
broader bank — it is the same gate, applied twice instead of once, and it should not be
skipped for the new content just because the process is now familiar.**

---

## 3. Item 2 — the live-traffic growth mechanism

This is the genuinely new design work, and the launch prompt is right to size it that
way. Three sub-problems, taken in order: detection, selection, synthesis-and-review. A
fourth section resolves how this interacts with SH-11's serving-side guarantee.

### 3.1 "Asked three times" detection

**Not exact-match; participants paraphrase, so this needs something closer to intent
clustering. Recommend a two-stage pipeline, deliberately mirroring a pattern this
codebase has already built and already fixed once (see the callout below), rather than
inventing a new one:**

- **Stage 1 — embedding-based candidate generation.** Cheap, high-recall, deliberately
  loose threshold. Its only job is to never *miss* a real cluster — a missed cluster
  just means slower growth (pure opportunity cost, see below), so err toward
  over-including candidates.
- **Stage 2 — LLM-judge confirmation**, given *both* full candidate questions (not bare
  strings) and asked a precision-biased question: **"would the same single answer,
  without hedging or forcing either one, genuinely and fully satisfy someone who asked
  either phrasing?"** Only confirmed pairs count toward "asked three times."

**Why two-stage, and why this specific split of cheap/loose then expensive/strict:**
this is the same shape as `nodes.py`'s existing fabrication-adjudication node — a cheap
signal-detection stage 1, followed by a stage 2 that gets real grounding material before
it's trusted to judge. **That pattern was already built, already found broken, and
already fixed once in this exact codebase**: the calibration battery caught the original
fabrication monitor being asked to judge groundedness *"against sources it is never
shown"* — it fired high-severity FABRICATION on correctly-retrieved, attested Antony
material because the judge only saw response text, never the retrieval. The fix
(preserved in the current code's Stage 2 comments) was to give the judge the actual
sources it needs to judge against. **The question-equivalence judge in Stage 2 above
must not repeat that mistake**: it needs full context (both candidate questions, ideally
with enough surrounding transcript to know if either is context-dependent — see the
scoping note below), not bare strings compared in isolation.

**Two structural constraints on the candidate pool, both necessary for correctness, not
just tuning:**

1. **World-scoped, and role-scoped.** A "canonical answer" is inherently a single
   Representative's voice — this project's whole discipline refuses a harmonized
   cross-world narrative (Babintseva: *"there are histories, there is no one
   narrative"*; the Gap Closures doc's own authored/generated split for Compare Worlds
   exists because a shared answer across worlds is a different, harder claim than a
   world's own answer). Clustering must never merge "similar questions asked to
   different Representatives" — that is not the same question in any sense this
   project can safely act on, even if the words are close.
2. **Restricted to context-independent, turn-zero-shaped questions.** A free-typed
   question at turn 4 of a chain means something different out of context than the same
   words at turn 1 — the curriculum's own Q1 world-framed hard rule already treats
   "turn zero" as a special, structurally different position (no prior transcript to
   anchor to). A canonical answer built from a context-dependent turn, later served
   standalone, would misrepresent what was actually asked. Recommend restricting the
   candidate pool to messages an LLM classifies as self-contained (not "and also,"
   "what about them," pronoun-dependent, etc.), independent of literal turn number.

**False-positive cost (two genuinely different questions wrongly merged):** real, but
bounded by construction — see §3.4. A wrongly-merged cluster produces, at worst, a
*review candidate* that a human reviewer should catch (it will read as answering neither
question cleanly), or in the worst case a poor catalog entry — never a live participant
served an inferred answer to their own different question, because nothing here changes
how anything is *served* (§3.5).

**False-negative cost (real repetition never detected):** pure opportunity cost — the
catalog grows more slowly than it could. Given this asymmetry — false positive risks
catalog *quality* (mitigated downstream by mandatory human review), false negative only
risks catalog *velocity* — **Stage 2 should be tuned to bias precision over recall.**
Better to miss a real cluster this month than promote a bad merge.

### 3.2 What "best" means

**Not length, not citation count.** The Design Study's own pastoral-mode finding names
the trap directly: *"here are three sermon points"* is the project's own named
over-producing anti-pattern — *"an encyclopedic resource rather than a voice with its
own perspective."* Rewarding length or citation density as a selection proxy would
train promotion toward exactly the failure mode Governance already named and Modes
already guards against.

**Recommended selection criterion, in order:**

1. **Score each of the three candidate answers against the same 10+2 fit-test rubric
   this project already built and validated** (Design Study §2.3, corrected by the
   calibration battery) — reuse the existing, evidence-corrected instrument rather than
   inventing a new one for this narrower purpose.
2. **Register/voice fit** for this world (informed by, not delegated to, the
   Representative-Modes register-invariance work — see the caution in §3.3 about RM-8's
   own current FAIL state).
3. **Presence of real citations/retrieval grounding**, as a *floor* (an answer with no
   retrieved grounding shouldn't win on that basis alone unless the other two answers
   are worse on the primary criteria), not a *reward* (more citations ≠ better, per the
   over-producing caution above).
4. **Human final sign-off** — not optional, see §3.4.

**Who applies it:** an automated pre-score (criteria 1–3) narrows three candidates to a
recommended winner *or* flags that none is clean enough to build from; a human applies
criterion 4 before anything is promoted. Full automation of selection is not recommended
— not because the scoring itself is unsafe, but because selection and the synthesis step
next to it (§3.3) are inseparable in practice, and synthesis is where automation alone
is explicitly not safe enough.

### 3.3 The synthesis step — the real fabrication-rigor risk

**Name the operation precisely, because the risk follows directly from what kind of
operation it is.** SH-11's precompute is **one clean live generation, captured
verbatim** — `representative_engages()` runs once, on the real code path, and the
answer text is never touched again. **Nothing in this codebase today takes three
separately-generated real texts and produces a fourth text claiming to represent all
three.** That is a new generative operation, and it introduces failure modes SH-11
structurally cannot have:

1. **Claim invention via combination.** Two true statements, each individually
   supported by its own source answer, can combine into a compound claim neither source
   actually made. Concretely: if answer A says leadership was contested between bishop
   and presbyters, and answer B (a different framing of the "same" clustered question)
   says communities disagreed sharply, some nearly splitting, a careless synthesis could
   produce *"the leadership dispute nearly split the community"* — a sentence with no
   single source, assembled from true parts into an unsupported whole. This is a
   different failure class from ordinary fabrication (inventing content from nothing);
   it is **synthesis-level over-claiming**, and the project's existing fabrication
   tooling has never had to catch it because nothing before this has generated text from
   *other generated text* rather than from retrieved evidence.
2. **Citation mismatch.** A citation attached to a sentence in the synthesized answer
   may have actually supported a *different* sentence in a *different* source answer.
   This is worse than an uncited claim, because it reads as verified when it isn't — a
   direct hit against the exact discipline the parroting/citation-fidelity measurement
   work (0.0–0.01 mean overlap across worlds, per `S5.1_parroting_baseline.md`) exists
   to protect.
3. **Voice incoherence.** Even with world-and-role scoping (§3.1) enforced, three real
   answers triggered by three different real phrasings can differ in register — one
   more clinical, one more pastoral. A naive merge can produce a voice matching none of
   the Representative's validated registers. **This is not a hypothetical caution
   layered on for safety's sake**: `RM-8` (Representative Modes Battery A, run
   2026-07-22) is the project's own most recent, currently-unresolved finding that
   register/content-invariance is *not yet reliable* — 3 of 5 probes failed outright on
   content-invariance, concentrated in the `reevaluation` mode specifically (dropping
   content, not just changing tone). A synthesis operation asked to reconcile
   differently-registered real answers is asking the system to do, by hand, exactly the
   thing its own most recent live battery just measured as unreliable. **This argues for
   real caution about scope, not just a review gate** — see the recommendation below.
4. **Loss of "legible as an answer to the message actually in front of you."** This is
   `representative_prompts.py`'s own hardest-enforced rule, and it is the literal
   mechanism behind SH-11's "never serve a paraphrase" guarantee. A canonical answer
   built from three different real phrasings cannot, by construction, be "the answer to
   the message actually in front of it" for a *fourth*, still-different tap or type —
   **unless the promotion step also authors a fifth thing: a fresh, human-approved
   canonical *question* string**, and the entry is then served only against an exact tap
   on *that* string, never against any of the three original phrasings and never against
   a future free-typed variant. This closes the loop and is the resolution in §3.5 — it
   is not optional, it is what makes the rest of this design safe at all.

**Verdict on whether this can be made safe at acceptable cost: yes, conditionally — not
with a weak gate, and not fully automated.** The four failure modes above are real and
specific to this operation; none of them are automatically fixed by "make the model
careful." The gate has to actually check for them.

**Recommended review gate — two mandatory layers, mirroring the fabrication-adjudication
pattern's own fixed shape (source-aware, not blind), never collapsed to one:**

- **Layer A — automated, sources-aware entailment check.** An LLM-judge is given the
  proposed synthesized answer, **all three source answers verbatim**, and their
  citations/retrieval audit, and asked, per claim: *is this entailed by (supported by,
  not contradicted by) at least one of the three source answers or their cited
  retrieved context?* Any flagged claim blocks promotion. This is explicitly modeled on
  the fix already proven in this codebase (give the judge the sources it needs), not a
  new invention — and it explicitly avoids the exact mistake the calibration battery
  found in the pattern it's modeled on.
- **Layer B — mandatory human review, not replaced by Layer A.** Same standing as the
  "someone should actually read a sample of what comes back" step SH-11 already
  requires for the original 100 before trust — this is that same discipline, extended,
  not a new one invented for this purpose. Reviewer checks: (1) does this read as
  something this Representative would actually say, informed by but not delegated to
  the Modes battery instrument; (2) does every citation actually support the sentence
  it's attached to, spot-checked against Layer A's flags; (3) approves or hand-writes
  the canonical *question* string the entry will be served against (§3.5).

**Cost shape, and why it stays bounded rather than needing to be weakened:** review cost
scales with *confirmed clusters*, not with total traffic — Stage 2's precision bias
(§3.1) and the "three real askings" threshold itself already keep the candidate volume
low relative to raw conversation count. This is the design's own answer to "rigor is
never gated for money": the gate can stay full-strength because its cost is bounded by
construction, not because cost was declared irrelevant. **The tripwire to watch, named
explicitly per "never quietly degraded for cost":** if traffic volume ever makes Layer B
reviewer time feel like a bottleneck, the wrong fix is loosening Layer A's entailment
bar or making Layer B optional/sampled. That would be exactly the quiet degradation the
standing principle forbids, and it should come back to Mark as a real tradeoff, not get
solved silently in the pipeline.

### 3.4 Two different matching problems — being precise, per the launch prompt's own ask

**Correction, 2026-08-02 (System Hub, at Mark's direct request — the section below is left
intact as a record of what was recommended and why at the time; it no longer describes the
decided direction).** This section's core conclusion — "do not build inference-based serving
matching, at all" — is **rescinded**. Mark, in the Funding Strategy thread, on being shown the
option this section treats as a real risk to avoid: *"that is exactly what we need."*
Inference-based (semantic) matching for Problem B is now the live, endorsed direction, not a
ruled-out one. Two things below this correction are superseded along with the headline
recommendation, not just the recommendation itself: the "explicit tap = signal" framing in
Problem B's own text, and the tap-confirm "did you mean" suggestion offered afterward as "a real,
separable design option" — the decided shape is **hidden auto-serve**, no tap-confirm step and no
participant-visible indication a match occurred at all, which is a stronger version of inference-
based serving than either the old recommendation or its own proposed compromise anticipated.

**What's actually decided, for anyone building from this document instead of the correction:**
hidden auto-serve; pre-generated response variations (~5 per canonical answer, generated once
offline, never live-rephrased) under a **re-word-never-re-content guardrail** — every variation
must pass the same citation/entailment check used elsewhere, with mandatory human review of a
sample before going live (this project's own RM-8 testing, 2026-07-22, found register-invariance
not yet reliable — 3 of 5 probes failed on content-invariance — so this isn't a formality); a
conservative, high-confidence-only launch threshold as the actual safety mechanism, loosened later
from real data; and full silent match logging (question asked, entry matched, confidence score,
variation served) on every decision regardless of UI state. **Validation path decided:** the real
pilot, not a separate offline calibration study first — the study's threshold-calibration and
blind tone-comparison test designs stay available as a fallback if pilot logging shows a real
mismatch pattern, not as a launch gate. Full detail: `Ministry/Features/Funding-Strategy/
Decision-Log.md`, 2026-08-02 entries ("Mark rescinds..." and the build-scope dispatch entry
after it); build recipe: `Ministry/Operations/Standing/Launch-Prompts/
CiC_Cost_Reduction_Build_Scope_2026-08-02.md`, Answer Bank redesign item.

---

**Problem A — clustering PAST questions to decide what to add.** This is all of §3.1.
It is allowed to use inference freely (embeddings, LLM judgment) because **its output is
never served directly** — it only ever produces a *review candidate* that a human must
approve (§3.3, Layer B) before it can exist as a bank entry at all. An imperfect
clustering algorithm is safe by construction here, because every path from "candidate"
to "servable" passes through mandatory human review.

**Problem B — matching a NEW incoming question against the growing bank, to decide
whether to serve.** This is the one SH-11's design doc is explicit must never become
inference-based — *"never inferred from parsing free-typed text; that is what makes
'never serves a paraphrase' true by construction, not by hoping a fuzzy matcher never
misfires."* **This document's core recommendation: do not build inference-based serving
matching, at all.** A promoted entry is served **only** by an explicit tap on its own
freshly-authored canonical question string — the exact same mechanism SH-11 already
uses for the original 100, unmodified. Growth widens the *catalog* (more exact strings
that can be tapped); it never touches the *serving logic* (which string was tapped).

**The one place inference legitimately touches the serving side, named as optional and
clearly separated from the core mechanism:** a "did you mean — others have asked..."
suggestion, shown alongside a free-text box, built from embedding similarity between
what's being typed and the canonical catalog. This never auto-serves anything — it only
ever offers a tap target, and tapping it is the same explicit signal as tapping any
other starter. The real risk here is not safety (nothing is served without a tap) but
trust/UX: a suggestion that over-matches unrelated questions can read as "the system
already knows what I'm asking" when it doesn't, so the copy would need to say "a related
question others have asked," never "the answer to what you typed." **This is a real,
separable design option, not required for the core mechanism, and left as Mark's call**
(§5) — building it is a UI/UX decision with its own tradeoffs, not a dependency of
items 1 or 2's safety properties.

### 3.5 Interaction with SH-11's "never serve a paraphrase" guarantee — the resolution

**Correction, 2026-08-02 (System Hub):** this section states it is "the hinge the rest of this
section depends on" — that hinge is §3.4's now-rescinded recommendation (see the correction
note there). With hidden auto-serve decided, an entry can be served as a system-generated
variation rather than verbatim, and without a tap-confirm step to make the signal explicit —
both premises this section's resolution rests on no longer hold as stated. Left intact below as
history, not current guidance; see §3.4's correction for what actually governs now.

Stated plainly, since it is the hinge the rest of this section depends on: **every
promoted entry gets its own new, human-approved exact question string at promotion
time — never one of the three original phrasings, never inferred from the cluster.**
The entry is then indistinguishable, mechanically, from any of the original 100: stored
by `(role/topic key, question_order-equivalent)`, looked up by explicit client signal,
defense-in-depth text-matched, served verbatim on hit, falls through to live on any
miss. **SH-11's guarantee is preserved unchanged, not reinterpreted** — growth adds
content to a catalog that is exact-tap-only by construction; it does not add a new way
to be served.

---

## 4. Item 3 — Table mode, scoped honestly

### 4.1 Why it is harder — concretely, from the live code, not by assertion

`select_next_speaker` in `app/graph/nodes.py` chooses who speaks next by giving an LLM
the full public transcript so far, each seated world's per-round and per-conversation
speaking count, and an explicit instruction that **real conversation "is not 'everyone
gives one statement in order' — it has shape: someone opens, another responds and then
adds their own view, the first may come back once there's something new to answer, a
third may jump in partway through."** The selector is also fed a live `register_note`
(a mode-dominance correction from the previous round) and explicitly weighs who has
"gone quiet" across the whole conversation, not just this round.

**A precomputed chain cannot supply any of this in advance**, for reasons that compound
rather than stack:

- **Who is seated is not fixed.** Six solo worlds means `C(6,2) + C(6,3) = 35` possible
  seatings for a 2- or 3-world table, before any content is written.
- **Speaking order is not fixed even within one seating.** `select_next_speaker`'s own
  prompt optimizes explicitly *against* rotation — the same seating produces a different
  real conversation depending on what was actually just said. Precomputing "the chain"
  for one seating would mean precomputing not just answers but a **scripted dialogue
  order and each speaker's reaction to the prior speaker** — a fundamentally different
  artifact than "cache one Representative's honest answer to one question." That risks
  writing theater, which cuts directly against Governance's *"testimony, not argument"*
  discipline for the Reevaluation role specifically — a role Table mode would include.
- **`cost_floor_model.py`'s own numbers already show the combinatorial cost, and that's
  before the ordering problem above is even counted:** [M] the table bank build is 3,150
  precomputed turns (35 seatings × 4 roles × 5 sets × ~4.5 questions) against 540 for
  solo — **~5.8x the volume**, and that 3,150 already assumes a deterministic walk per
  seating, which §4.1's own finding says table conversation structurally is not.
- **[M/E] Cost, run directly:** solo bank build is $14 (batch-modeled) / ~$28
  (synchronous); table is **$272 (batch-modeled) / ~$544 (synchronous)** — the same
  ~19-20x multiple `cost_floor_model.py` already names when it calls the table bank
  "the expensive one, ages fastest." Larger build cost, at the same time as the least
  static content (who's seated varies live), is the worst cost/value ratio in this
  entire design space.

### 4.2 A sibling thread already reached this conclusion, independently

The Gap Closures document (`CiC_Guided_Questions_Gap_Closures_V0_1.md`, Gap 1) faced the
identical structural problem for a narrower feature — Compare Worlds subsequents at a
multi-world table — and reached the same answer for the same reason, worth citing as
converging evidence rather than restating this document's own reasoning as if it were
novel: *"A Compare Worlds subsequent is definitionally responsive — its whole job is to
follow what two or three voices just said to each other. It sits on the generated side
by its nature, not by our convenience."* **That is this document's Table-mode-precompute
conclusion, reached independently by another thread about a smaller piece of the same
problem.**

The same document's Gap 2 is a second, orthogonal piece of standing context worth naming
plainly: **the generated (live) surface at a multi-world table has no validation
instrument today** — the probe battery Gap 2 designs to test it (register-invariance
under diverge/converge conditions, the two ✗-cut-derived adversarial probes) is
*designed, not run*. Building a Table-mode answer bank on top of an already-unvalidated
generated layer would compound risk rather than reduce it — it isn't this document's gap
to close, but it is a real reason not to add caching complexity to Table mode before that
underlying validation exists.

### 4.3 Recommendation: defer, do not attempt a bounded version now

**Defer Table-mode banking entirely.** Not "defer everything except a small piece" —
the honest bounded-version sketch below has its own real open question that makes it
unready, stated rather than smoothed over.

**The one narrower idea worth naming, and why it is not recommended as a build item
today:** a table round's very *first* representative turn — before anyone else at the
table has spoken, with no `public_transcript` yet and no reaction-to-prior-speaker
dependency — is structurally closer to a solo turn than anything later in the round. In
principle, an exact curriculum tap that triggers that first turn could be served from
the same per-world solo bank entries already built, with only "which seated world speaks
first" needing a decision (which `select_next_speaker` already makes live for any
opening turn today). **But this has a real, unresolved fidelity gap, not a solved
technicality**: the already-shipped multi-world address/anchoring convention (Task
Board, DONE 2026-07-20) means Representatives are built to acknowledge co-presence at a
table — whether a world's *very first* utterance in a multi-world session differs at all
from its solo answer to the identical question, purely because it now knows who else is
seated, is untested. Serving a solo-bank entry as a table's opening turn would be a
live, unverified assumption that "first turn" and "solo turn" are answer-equivalent —
exactly the kind of assumption this project's own calibration discipline (predicted-safe
things failing, predicted-risky things passing) argues against taking on faith.

**Revisit criteria, stated so this doesn't quietly become "never":** (1) real
pilot Table-mode traffic exists to know whether a table's opening reply landing on an
exact curriculum tap is even common enough to matter; (2) SH-12's paid-tier
subscription-gating infrastructure is built, since Table mode is paid-tier at public
launch per the 2026-07-31 product-shape decision — table-bank work has a hard
dependency on that gating existing regardless of the technical question; (3) the
first-turn-vs-solo-turn fidelity question above is actually tested live, not assumed.
None of these hold today.

---

## 5. Sequencing

**Agree with the proposed sequencing, with one sharpened reason for item 2's delay and
one small now-task named.**

- **Item 1 (broader static bank) — buildable now, no pilot-traffic dependency.** Same
  dependency chain SH-11 already named for itself: a real build run (cheap, §2.3), then
  human content review before trust (§2.4), then the curriculum-picker UI (front-end
  thread's own domain, already named as not-yet-built). The ~50 new questions can be
  authored in parallel with SH-11's own still-open review/UI items — they don't block
  each other.
- **Item 2 (traffic growth mechanism) — design now (this document), build once real
  pilot traffic exists.** Agree, and add the sharper reason beyond "no traffic to learn
  from": **the engineering itself can't be responsibly tuned pre-pilot.** Stage 1/Stage
  2's similarity threshold and precision bias (§3.1), and the review gate's real
  false-positive/false-negative rates (§3.3), are empirical questions that need real
  paraphrase data to answer — building the pipeline now would mean shipping an
  unvalidated instrument on guessed thresholds, which is the same standing risk Gap 2
  already named for the generated-surface validation gap (§4.2). **One small, cheap
  now-task, distinct from building the pipeline:** confirm
  `app/transcript_logging.py`'s existing `sessions`/`messages` Supabase schema already
  captures what clustering will eventually need (world_id, role if available, message
  text, turn position, citations) so nothing needs a schema migration once pilot data
  starts arriving — worth doing now precisely because it's cheap now and would be a
  quiet, avoidable blocker later.
- **Item 3 (Table mode) — fully deferred**, per §4.3's explicit criteria, not built or
  designed further until those criteria are met.

---

## 6. What's designed and ready, vs. what needs Mark's decision

### Ready — no further design work needed to start building, when the sequencing above says to

- **SH-7 × SH-11 relationship resolved:** superset, same rigor process, 100 + ~50
  converges on SH-7's own ~150 by construction (§1).
- **Item 1 architecture:** no code changes to SH-11's mechanism — more curriculum
  entries, same unmodified `answer_bank.py`/build script (§2.1).
- **Item 1 served-fraction re-derivation:** [S] ~5.8% central for content-growth-alone,
  same order of magnitude as SH-11's own 5.2% — the honest finding that catalog size
  alone is not the lever (§2.2).
- **Item 1 cost:** [M/E] trivial — $14–42 for a 150-question build; review labor is the
  real cost, not API spend (§2.3).
- **Item 2 detection mechanism:** two-stage (embedding candidates + sources-aware
  LLM-judge confirmation), precision-biased, world-and-role-scoped, restricted to
  context-independent questions (§3.1).
- **Item 2 selection criterion:** fit-test rubric + register fit + citation-presence
  floor (not reward) + mandatory human sign-off; explicitly rejects length/citation-count
  as quality proxies (§3.2).
- **Item 2 review gate:** two mandatory layers (sources-aware automated entailment check
  + human review), explicitly judged safe *at that cost*, explicitly judged unsafe if
  either layer is skipped, made optional, or weakened under traffic-volume pressure
  (§3.3).
- **Item 2 serving-side resolution:** promoted entries get a fresh, human-approved
  canonical question string, served only by exact tap — SH-11's guarantee preserved
  unchanged, not reinterpreted (§3.4–3.5). **Superseded 2026-08-02 — see the correction
  notes at §3.4/§3.5.** Exact-tap-only is no longer the decided mechanism; Mark rescinded
  it in favor of hidden auto-serve inference-based matching. Not "ready" under this line's
  original meaning — the real ready/not-ready state now lives in the build-scope dispatch
  cited at §3.4.
- **Item 3:** deferred, with explicit, checkable revisit criteria and an honestly
  incomplete bounded-version sketch named but not recommended (§4.3).
- **Sequencing:** item 1 now, item 2 design-now/build-post-pilot with a named small
  now-task, item 3 fully deferred (§5).

### Needs Mark's decision

- **Whether SH-7 Phase A (the ~50 desk-authored questions) runs now, or waits for
  Phase B's real-traffic harvest to prioritize which 50 to write.** This document
  recommends starting Phase A now (no dependency blocks it), but whether that's the
  best use of authorship time before any real pilot signal exists is a real call, not a
  foregone one.
- **Who reviews the original 100/150's live-generated content before it's trusted** —
  this was already an open item in SH-11's own "what's left" list and is not resolved
  here; it just now applies to more content.
- **Who is the designated human reviewer for item 2's Layer B promotions once pilot
  traffic exists**, and what reviewer-time budget that implies as traffic scales. This
  is a new role/workflow this document does not assign.
- **Whether to build the optional "did you mean — others have asked" suggestion
  surface** (§3.4). Not required for either item's core safety properties; a real UX
  and trust tradeoff, and its own design pass.
- **Whether the transcript_logging.py schema check (§5's small now-task) happens now**
  — cheap, but still a task someone has to actually pick up.
- **How item 1's new content authorship is resourced relative to SH-11's own still-open
  items** (original-100 content review, curriculum-picker UI) — recommended as
  parallel, not sequential, but that's a resourcing call, not a technical one.
