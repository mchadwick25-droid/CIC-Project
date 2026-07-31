# Launch prompt — Answer Bank full-system research, evaluation, and design

**Paste this whole document as your first message in a new thread. Select Opus as the
model before sending — this is a research/design pass with real unknowns, not an
implementation task, and that's the project's own standing model-tier policy for this
shape of work.**

---

I'm Mark, building Church in Conversation (CiC) — an app where participants have real
conversations with AI Representatives of historical Christian traditions ("the Table").
You're starting fresh with no memory of prior sessions. Read the files this prompt
points you to before proposing anything; don't reason from the prompt text alone.

## What already exists — read these first

A narrower version of this idea already shipped tonight (2026-07-31), as "SH-11." Don't
duplicate it or propose replacing it wholesale without understanding what it actually
does and why it's shaped the way it is:

- `Ministry/Features/Guided-Questions/CiC_Answer_Bank_SH11_V0_1.md` — the design writeup.
  Read this first; it explains the architecture and the reasoning behind every
  constraint.
- `cic-poc/backend/app/answer_bank.py` and `app/answer_bank_logging.py` — the real code.
- `Ministry/Technology/Pass3/cost_floor_model.py` STEP 5 — the cost grounding. Its
  finding: a precomputed answer can only be served when three things hold at once
  (question-first door chosen, a starter tapped rather than typed, the participant
  stays on the curriculum's own walk without deviating) — **~5.2% central estimate**,
  not the 30-50% first assumed. That estimate is for SH-11's narrow case specifically
  (exact taps on the 100-question curriculum only). **Re-derive whether it still holds,
  or whether it changes, for the broader system below** — a bigger question bank and a
  live-traffic-growth mechanism could plausibly serve a meaningfully larger fraction,
  but that needs real modeling, not inherited optimism.
- `Ministry/Features/Guided-Questions/Design/CiC_Guided_Questions_Curriculum_V1_0.md` and
  its `.json` data contract — the existing 100-question curriculum (4 roles x 5 sets x
  ~4.5 questions), safety-reviewed against 10 fit tests, including a hard rule (question
  1 of every set must be world-framed, never participant-framed — a real safety
  mechanism, not a style preference; the design doc explains why).
- `Ministry/Features/Guided-Questions/Design/CiC_QuestionFirst_Entry_Design_V0_1.md` —
  the entry-flow design (three co-equal doors: pick-a-world, question-first, guided
  onboarding). Explains where a curriculum tap fits in the participant's actual path
  through the app.
- Task Board (`Ministry/Operations/Standing/CiC_Task_Board_2026.md`), **SH-7**:
  "Identify the ~150 most probable interview questions. Multi-step process, not yet
  designed — needs its own scoping conversation before work starts." **This thread is
  that scoping conversation** — figure out how SH-7's ~150-question target relates to
  the existing 100-question curriculum (superset? different selection method? both
  converge on largely the same list?) rather than treating them as unrelated.

## What I actually want designed

Three things, explicitly in this priority order, and explicitly **research and design
only — no code, no build**:

### 1. A broader answer bank for interview (solo) mode

SH-11 serves only an exact, unmodified tap on one of the 100 existing curriculum
questions. I want this widened toward the ~150 most likely questions a real participant
would ask (SH-7's own framing) — figure out how that list actually gets built (is it the
existing curriculum plus 50 more in the same rigorous, safety-reviewed style? A
different derivation method entirely?), and how serving expands the SH-11 mechanism
without weakening any of its real constraints (see "what not to break," below).

### 2. The live-traffic growth mechanism — the genuinely new, hard part

Track real conversations once the pilot is live. When **the same question has
effectively been asked three times** — not three identical strings, real participants
paraphrase — take the three best real answers that were actually given, and build one
reviewed, canonical answer from them to add to the bank. This needs real design work on
several genuinely open questions, not just an implementation plan:

- **"Asked three times" detection.** Free-typed text won't match verbatim. What's the
  real mechanism — embedding-based similarity clustering? An LLM-judge that classifies
  "is this the same question as X"? Something else? What's the false-positive cost (two
  genuinely different questions wrongly merged) versus false-negative cost (real
  repetition never detected)?
- **What "best" means.** Three answers to the same question could differ in
  length, register, which sources they drew on, even which world answered. What's the
  selection criterion, and who or what applies it?
- **The synthesis step is a real fabrication-rigor risk, not just an engineering step.**
  This project's whole discipline is record-grounded speech — parroting measured at
  near-zero (0.000 in Hieronymian's own freeze battery tonight) across multiple worlds'
  freeze batteries, real cost paid to get there. Synthesizing "one canonical answer" out
  of three separately-generated real answers is a fundamentally different operation from
  SH-11's precompute (one clean live generation, captured as-is). Does the synthesized
  answer keep real citations? Whose voice does it speak in if the three source answers
  came from slightly different framings? Could stitching three answers together produce
  a claim none of the three actually made on their own? **Design the review gate this
  needs before anything gets promoted to the bank** — human review, an automated
  fidelity check against the source answers, both, something else — and say plainly if
  you don't think this can be made safe at an acceptable cost, rather than proposing a
  weak gate to have something to propose.
- **How this interacts with SH-11's existing safety design.** SH-11's "never serves a
  paraphrase" guarantee comes from being told *exactly* which button was tapped, not
  from inferring intent — read the design doc's reasoning on this before proposing
  anything that re-introduces inference-based matching for the *serving* side (matching
  a NEW incoming question against the growing bank is a different, and different-risk,
  problem than clustering PAST questions to decide what to add — be precise about which
  of these two matching problems any given design choice actually solves).

### 3. Table mode — scope it honestly, don't force a design

I know this gets "very complex" for the multi-representative table — that's exactly
why I want it scoped rather than guessed at. `cost_floor_model.py` already calls the
table bank "the expensive one, ages fastest." Explain concretely why table mode is
harder (multiple representatives responding to one question, in relation to each
other, not independently — a precomputed chain can't easily anticipate who else is
seated or what they just said). Give me a real recommendation: attempt a bounded
version now, or explicitly defer it, and why.

## What not to break

- **Never serve a paraphrase as if it were an exact answer to what was actually asked.**
  This is SH-11's central safety property. Any design for the broader system must
  either preserve it or explain, with real reasoning, why a different guarantee is
  still safe.
- **Rigor and sourcing are never gated for money, and never quietly degraded for cost.**
  Standing project principle. A cost lever that trades against answer quality or
  citation fidelity needs to say so explicitly, not bury it.
- **No question here has faced a live model yet** applies to any new questions this
  thread proposes adding to the ~150, the same way it applied to the original 100 —
  don't treat "we wrote a good question" as equivalent to "we verified it produces a
  good live answer."

## Sequencing — read this before proposing a build timeline

**The live-traffic growth mechanism (item 2) cannot do anything without real pilot
traffic to learn from** — there's no "asked three times" to detect before real
participants are actually asking things. Separately, I've decided SH-12 (the paid tier)
waits until piloting is far enough along to know real costs and keep the pilot
experience simple — same logic applies here: **design this now, build the
traffic-tracking/promotion piece once real pilot data exists to build it against.** The
broader static bank (item 1) doesn't have that dependency and could plausibly build
sooner, once its own content is reviewed — say so if your design agrees, or explain if
you think the sequencing should be different.

## What I want back

A real design document — grounded, not aspirational. Use this project's own [M]/[E]/[S]
tagging discipline (measured / estimated / speculative) from `cost_floor_model.py` for
any cost or served-fraction claim. Name every real tradeoff explicitly rather than
picking a side quietly. End with a clear list of what's designed and ready, versus what
still needs my own decision before anything gets built.
