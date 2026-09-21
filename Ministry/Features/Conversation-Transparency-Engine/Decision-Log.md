# Decision Log — Conversation & Transparency Engine

Append-only, workstream-local, per `CLAUDE.md`. One entry per PR merged
and per ruling made. Never edit or renumber a past entry; a correction is
a new entry that says what it corrects.

---

**Entry 1 — 2026-09-19.** Workstream opened. Fable design pass 2
(Opus-reconciliation) complete: `Adjusted-Design.md`, `Build-Plan.md`,
`Rulings-Pending.md` written from the Fable agent's report. Reviewable
summary published as an Artifact:
`https://claude.ai/artifact/N8jiwbkB7kqsdH1jiq8622`. Mark authorized
starting the Sonnet build thread on Stages 0–4 only; Stages 5–9 remain
blocked on `Rulings-Pending.md` and Stage 1's own measurement.

**Entry 2 — 2026-09-19.** Prior to this workstream, three live safety
defects found by an independent Opus adversarial review were fixed and
merged to `main` (PR #306, commit `1c522e918`): a reader-timeout
discarding a successful crisis classification (`engine/m5/failure.py`,
`engine/m5/routing.py`); the crisis-continuation message carrying no
actual redirect language (`engine/m4/crisis_resources.py`); the
citation-grounding check being fooled by a fabricated claim built from a
forbidding guard's own vocabulary — partial fix only
(`engine/prose.py`); the full defect is structural and is what
`Build-Plan.md` Stage 1 measures. Noted here for this workstream's own
record since it is the ground truth `Adjusted-Design.md` §0 stands on.

**Entry 3 — 2026-09-19.** Scope correction, same day as entries 1–2. This
workstream was briefly named "Transparency & Safety Redesign" and carried
a 19-item ruling queue, roughly a third of it proposed new safety
machinery (escalation tiers, message decay, a conditional memory window,
output-side sentence withholding, distinct messages per disclosure type)
that Mark never asked for — the original charter was the conversation and
transparency engine only. Mark's direct ruling: *"if there is an
expression of safety then the facilitator will step in and ask, then
provide an encouragement to seek human help, thats it no more crap or
complication, that meets the need and keeps the system clean."*

This closes the following as **resolved, not deferred** — the Facilitator's
safety mechanism is a fixed, single-step shape and is not open design
space:
- **S1** (safety-call failure handling) — closed. No async reclassification,
  no operator paging build-out. The existing fail path stands.
- **S2** (escalation priority / message decay / interim text) — closed. No
  new escalation-tier logic, no decay timer. The already-merged fix (PR
  #306) — a plain redirect on every crisis-relevant turn, first one or
  repeat — is the whole mechanism.
- **R1** (safety-call-failure fallback options) — closed, same as S1.
- **R2** (escalation/decay/interim-text options) — closed, same as S2.
- **R3** (item 16's "conditional memory window" replacement) — closed. No
  replacement is built. The classifier stays fully memoryless, as struck
  in `Adjusted-Design.md` §2 (item 16 itself was already struck there for
  cost reasons; this closes the door on any replacement mechanism too).
- **R4** (reminder-repeat frequency / voice-visibility) — closed. One
  check-in, once. No frequency tuning, no repeat-suppression logic beyond
  what already exists.
- **R14** (output-side sentence withholding) — closed. Never built, in any
  form — the mechanism reports only, exactly as it does today. No future
  reconsideration tied to a measured rate; this is not a "revisit later"
  item.
- **R15** (distinct message for third-party risk disclosure) — closed. One
  message, no branching by disclosure type.

Renamed the workstream directory `Ministry/Features/Transparency-Safety-
Redesign/` → `Ministry/Features/Conversation-Transparency-Engine/` and
rewrote `README.md`, `Adjusted-Design.md`, `Build-Plan.md`, and
`Rulings-Pending.md` to match. Nothing about the three already-merged bug
fixes (PR #306) changes — those were legitimate defect fixes, not
redesign, and Mark confirmed them explicitly ("yes you can fix a couple
of broken things"). Stages 0, 2, 3, 4 of `Build-Plan.md` (conversation/
transparency engine work — retrieval, library connection, citation/
confidence display) are unaffected and continue. Stage 5 is removed from
the build plan entirely, not just reordered.

**Entry 4 — 2026-09-20.** Stage 4c Part 2 merged (PR #325, commit
`2cb5efdad`): `retrieval_words()` relocated from `engine/m2/builders.py`'s
private `_retrieval_words` to public `engine.prose.retrieval_words()` so
`engine/m4/evidence.py` (runtime) and `engine/m2/` (compile-time) score
against the identical retrieval-safe word set without `m4` importing
`m2`. New Stage B2 fill in `select_cell_candidates`: when a cell's own
coverage has zero candidates of a type, fill from whole-repository
`retrieval_words()` overlap, capped at that type's `_TYPE_FLOORS`, tagged
`retrieval_fill: True`. `retrieval_bench` fleet reach: 813 → 1152. Same
PR also fixed a stale `ACCEPTED_OPEN` waiver (`site-portrait/witt`) in
`engine/m1/cross_world.py`, found as a side effect of an unrelated CI
investigation and confirmed pre-existing on `main` via git-worktree
reproduction — root-cause fixed per the file's own "CLOSED" convention,
not worked around. Full suite + fleet gates green.

**Entry 5 — 2026-09-20.** Stage 4d merged (PR #326, commit `402153909`):
`_tier_prior()` (`engine/m4/evidence.py`) adds +0.05/+0.02/+0 by
`retrieval.tier` (1/2/other) to `select_cell_candidates`'s per-cell
ranking, breaking near-ties toward "core" material. `retrieval_bench`:
1152 → 1150 — a small, real, measured regression (4/118 questions moved),
traced to the shared per-cell `budget_chars` interacting with tier-prior
reordering on genuine score ties, and verified not an over-tuning
artifact (identical swaps reproduce under the most conservative possible
tie-break-only design). Surfaced to Mark via options rather than shipped
or reverted silently; his ruling: ship it, document the tradeoff here.
Full suite + fleet gates green.

**Entry 6 — 2026-09-20.** Stage 4f merged (PR #334, commit `114925866`):
`assemble_evidence` gained a new `secondary_context: str | None = None`
parameter (deliberately not reusing the existing `history` list, which
is shared with the live model call's own conversational memory and would
have duplicated content already visible via `context_prefix`) — fills
remaining `top_n_cells` slots from table-conversation context at lower
priority than the participant's own message, tagged
`from_secondary_context: True`. Wired from `table_wiring.py` via new
`_secondary_context_text()`. `retrieval_bench`: byte-identical at 1150
(interview mode never sets `secondary_context`, so the fixture-world
bench is unaffected by design). Full suite, M8 hermetic usage check
(no per-turn growth), and fleet gates green.

**Entry 7 — 2026-09-20.** Stage 3c merged (PR #335, commit `bb1ef7552`):
new `engine/m4/transparency_plan.py` work (Stage 3a/3b) was already
merged in a prior session window; this PR closed the renderer half.
Root cause of the "recurring, inconsistent" citation-mark dropout Mark
had been describing: `VoiceTurnBody.tsx`'s legacy renderer reconstructed
marks by searching finished text for each citation's own sentence, using
three ad hoc dedup structures — `renderedStoryIds`/`renderedWitnessIds`
suppressed a SECOND, non-consecutive citation of the same story/witness
record turn-wide, and because story/witness sources were never passed to
`addReference`, the repeat's sourcing was dropped entirely, not just its
mark — the exact defect `transparency_plan.py`'s own docstring names.
Fix: a new anchor-driven renderer reading the engine-computed
`transparency` plan (every run, including repeats, gets its own mark via
`anchorsByRunEnd`), dispatched behind `VITE_TRANSPARENCY_ANCHOR_RENDERER`
(default off — current behavior — until R10 and label copy are ruled).
Added `vitest` + `@testing-library/react`, a `test` script, and a
`frontend-tests` CI job. A same-day follow-up push to this PR
(`9321610b6`) fixed a real, unrelated CI failure found while verifying:
`jsdom@30.1.0`'s bundled `undici` calls a webidl API only present on
Node ≥22, crashing every test file at import under CI's pinned Node 20 —
reproduced locally on both Node 20 and 22, fixed by pinning `jsdom` to
`26.1.0`. Full suite + fleet gates green; `npx tsc --noEmit` and the new
`npm test` clean on both Node versions.
