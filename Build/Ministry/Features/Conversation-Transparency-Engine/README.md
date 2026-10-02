# Conversation & Transparency Engine — workstream

**Charter (Mark, 2026-09-19):** make the conversation and transparency
engine fully functional, modeling after the best conversation engines,
without losing the scholarly rigor and accessibility this project is
built on. Run the project's own established pipeline: Fable research and
design → Opus adversarial review → Sonnet build.

**Scope correction (Mark, 2026-09-19, same day):** this workstream was
briefly named "Transparency & Safety Redesign" and carried a 19-item
governance queue, a third of it proposed new safety machinery — escalation
tiers, message decay, a memory window, output-side sentence withholding,
distinct messages per disclosure type. Mark rejected that scope directly:
*"if there is an expression of safety then the facilitator will step in
and ask, then provide an encouragement to seek human help, thats it no
more crap or complication, that meets the need and keeps the system
clean."* The Facilitator's safety mechanism is not open design space —
it's a single, fixed shape: **recognize a safety-relevant signal → step
in with one check-in/message → encourage the participant to seek real
human help. Nothing more.** That's what's already built (a check-in turn
for ambiguous signals, a Facilitator message with a plain redirect for
acute/harmful-dynamic signals), and it stays that shape.

Renamed accordingly. This workstream's real and only scope is the
conversation and transparency engine — retrieval, the library connection,
citation/confidence display — matching the original ask. See
`Decision-Log.md` entry 3 for the full closure and what it resolved.

## What's already happened

1. **Interview + three parallel Fable research threads** (Library & Build
   process, Representative & Conversation/Transparency Engine, Facilitator),
   each in its own isolated worktree, synthesized into one end-to-end design.
2. **Opus adversarial review** of that synthesis against the live code found
   three genuinely live defects already in the shipped system (unrelated to
   the redesign itself), plus real problems in two of the synthesis's own
   proposals.
3. **The three live defects were fixed, tested, and merged** (PR #306,
   commit `1c522e918`) — the only safety-mechanism change this workstream
   makes, ever: a reader-timeout that could silently discard a real crisis
   classification; the crisis-continuation message carrying no actual
   redirect language; the citation-grounding check being fooled by a
   fabricated claim built from a forbidding guard's own vocabulary
   (partial fix — see `Adjusted-Design.md` §0 on why this is structural,
   not closed — this is a transparency/honesty-check defect, not a
   safety-mechanism one).
4. **A Fable design pass** reconciled the transparency/library synthesis
   against every Opus finding, under two hard constraints from Mark
   directly: no design element may add per-turn cost to the ordinary turn,
   and every module stays independently fixable.
5. **Scope correction**: every item of proposed new safety machinery is
   closed as resolved, not deferred — see `Rulings-Pending.md`. The
   Facilitator's mechanism does not change beyond the three already-merged
   bug fixes.

## Where this leaves things

- **`Adjusted-Design.md`** — the reconciled decision list for the
  conversation/transparency engine (retrieval, library connection,
  citation and confidence display), what's struck and why, the two hard
  constraints, and the methodology for the one still-open measurement (how
  often the grounding check can actually be fooled). Reviewable summary
  published as an Artifact: `https://claude.ai/artifact/N8jiwbkB7kqsdH1jiq8622`
  (written before the scope correction — read it alongside `Decision-Log.md`
  entry 3, not instead of it).
- **`Build-Plan.md`** — the staged build instructions a Sonnet thread
  executes against, self-governing per this file's own `CLAUDE.md`
  ("Scaling the build"). Stages 0–4 (conversation/transparency engine work)
  build now. Stage 5 (the safety mechanism) is closed — no further build.
  Stages 6–9 remain blocked on their own rulings or on Stage 1's own
  measurement.
- **`Rulings-Pending.md`** — the remaining rulings queued for Mark, one at
  a time, each with real options and a recommendation. All safety-mechanism
  rulings (S1, S2, R1–R5, R14, R15) are closed, not pending — resolved by
  the single-step model above.
- **`Decision-Log.md`** — append-only. One entry per PR merged and per
  ruling made, workstream-local per this project's own convention.

## Model routing

Sonnet builds and keeps the ledger. Fable did the design/synthesis work
and the Opus-reconciliation pass. Opus ran the adversarial review. Any
further groan-zone design work (a ruling that turns out to need real
back-and-forth, not just a yes/no) goes back to Fable, not decided
unilaterally by the build thread. The Facilitator's safety mechanism is
explicitly not open to this process any further — see the scope
correction above.

## Status (2026-09-19)

Scope corrected same day as design pass 2. Stages 0, 2, 3, 4 (conversation/
transparency engine) in progress, self-governing, one PR per stage. Stage
5 (safety) closed — no build. Stages 6–9 wait on `Rulings-Pending.md`.
