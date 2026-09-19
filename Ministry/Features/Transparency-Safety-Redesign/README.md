# Transparency & Safety Redesign — the conversation engine workstream

**Charter (Mark, 2026-09-19):** make the conversation and transparency
engine fully functional, modeling after the best conversation engines,
without losing the scholarly rigor and accessibility this project is
built on. Run the project's own established pipeline: Fable research and
design → Opus adversarial review → Sonnet build.

## What's already happened

1. **Interview + three parallel Fable research threads** (Library & Build
   process, Representative & Conversation/Transparency Engine, Facilitator),
   each in its own isolated worktree, synthesized into one end-to-end design.
2. **Opus adversarial review** of that synthesis against the live code found
   three genuinely live safety defects already in the shipped system
   (unrelated to the redesign itself), plus real problems in two of the
   synthesis's own proposals.
3. **The three live defects were fixed, tested, and merged** (PR #306,
   commit `1c522e918`): a reader-timeout that could silently discard a real
   crisis classification; the crisis-continuation message carrying no actual
   redirect language; the citation-grounding check being fooled by a
   fabricated claim built from a forbidding guard's own vocabulary
   (partial fix — see `Adjusted-Design.md` §0 on why this is structural,
   not closed).
4. **A second Fable design pass** reconciled the full synthesis against
   every Opus finding, under two hard constraints from Mark directly: no
   design element may add per-turn cost to the ordinary turn, and every
   module stays independently fixable. Both versions of the "give safety a
   memory of recent turns" idea are struck outright, not deferred — the
   combined-synthesis version Opus flagged (D6) and a second, standalone
   version buried in the synthesis's own decision list (item 16) that Opus's
   review didn't separately catch.

## Where this leaves things

- **`Adjusted-Design.md`** — the full reconciled decision list (24 original
  points + 5 new findings), what's struck and why, the two hard constraints,
  and the methodology for the one still-open measurement (how often the
  grounding check can actually be fooled). Reviewable summary published as
  an Artifact: `https://claude.ai/artifact/N8jiwbkB7kqsdH1jiq8622`.
- **`Build-Plan.md`** — the staged build instructions a Sonnet thread
  executes against, self-governing per this file's own `CLAUDE.md`
  ("Scaling the build"). Stages 0–4 do not depend on any pending ruling and
  build now. Stages 5–9 are blocked, each on a named ruling or on Stage 1's
  own measurement.
- **`Rulings-Pending.md`** — nineteen rulings (R1–R19) queued for Mark, one
  at a time, each with real options and a recommendation. Nothing in Stages
  5–9 proceeds until its ruling lands here.
- **`Decision-Log.md`** — append-only. One entry per PR merged and per
  ruling made, workstream-local per this project's own convention.

## Model routing

Sonnet builds and keeps the ledger. Fable did the design/synthesis work
and the Opus-reconciliation pass. Opus ran the adversarial review. Any
further groan-zone design work (a ruling that turns out to need real
back-and-forth, not just a yes/no) goes back to Fable, not decided
unilaterally by the build thread.

## Status (2026-09-19)

Design pass 2 complete. Stages 0–4 kicked off now, self-governing, one PR
per stage. Stages 5–9 wait on `Rulings-Pending.md`.
