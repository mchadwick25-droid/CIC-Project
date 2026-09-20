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
