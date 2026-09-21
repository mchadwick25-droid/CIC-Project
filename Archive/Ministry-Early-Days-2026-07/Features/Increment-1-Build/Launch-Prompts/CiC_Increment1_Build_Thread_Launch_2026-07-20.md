# Launch Prompt — Build Increment 1

Paste this into a fresh thread (Sonnet is fine for this — no need for Opus/Fable).

---

## Scope note

Build exactly what's specified in
`Ministry/Features/Full-UX-Design/Design/CiC_Build_Handoff_Increment1_V1_0.md`
— read it in full before writing any code, it is genuinely implementation-ready
(exact CSS token values, exact component files, acceptance criteria per
section, a suggested commit sequence). This launch prompt doesn't repeat that
spec; it gives you the parts a technical spec doesn't carry on its own —
current state, coordination boundary, and where to log your work.

**One-line goal, from the spec itself:** a participant lands on a stable,
budget-clean conversation screen in the finalized brand — same features as
today, in the right clothes, with the furniture that knows the Table is the
point. No new participant features ship in this increment.

## What governs

- The build handoff itself is the primary spec. It in turn points to
  `Ministry/Features/Full-UX-Design/Design/CiC_Full_UX_Design_V1_0.md` and
  `Ministry/Features/Front-End-Integration-Strategy/Design/` for the design
  rationale behind each acceptance criterion — read those if a build decision
  isn't obvious from the handoff alone, don't guess.
- Brand assets (palette, Alegreya, the "Arriving" logo/favicon/motion
  reference): `Ministry/Communication/Brand-Assets/`.
- **The standing merge rule, unchanged and binding:** nothing merges into a
  branch that could reach a live pilot before or during Prototype Testing 1.
  Build this on its own branch; running branches stay untouched.

## Current-state grounding — verify before assuming any of this is stale

- All six frontend files the spec names (`table.css`, `TheTable.tsx`,
  `RefreshWarningBanner.tsx`, `LexiconModal.tsx`, `CitationModal.tsx`,
  `WorldSelector.tsx`) were confirmed to still exist at the paths it expects,
  2026-07-20 — but re-check current content yourself before editing, don't
  assume nothing has moved since.
- **Not a conflict, but don't confuse the two:** a separate "citation-UI
  migration" (moving citations from a bottom list to inline hover/click
  markers, `CitationMarker.tsx`) already shipped and is live — that's
  different from this spec's §3, which changes the *modal container itself*
  (`LexiconModal`/`CitationModal` go from centered overlay to side
  panel/phone bottom sheet). §3 is still fully unbuilt.
- Alexandria (Theon) was installed as a 5th live world since this spec was
  written — doesn't change any Increment 1 scope, just means `WorldSelector`
  now renders 5 tiles instead of 4 wherever the spec discusses that screen.
- Prototype Testing 1 has not started and is not imminent — hosting
  (`#101/401` on the Task Board) hasn't been stood up yet. This means you
  are safely building on a branch well before any pilot window; the "never
  merge before/during PT1" rule is about the merge/deploy step, not about
  doing the build itself.

## One open question, not yours to resolve — flag it back, don't guess

The build handoff's own closing line says it's "the spec the build thread
executes in the post-Prototype-Testing-1 window" — written 2026-07-18,
before Mark's later decision that "P1 launches with the full feature set,
not the minimum-viable path" (`CiC_UX_to_Bedrock_Pilot_Readiness_2026-07-19.md`
V1.2). Whether Increment 1 should now merge *before* P1 (so P1 testers see
the finished brand) or still wait until after, per the handoff's original
sequencing, is a real, live scheduling question — not something this thread
should decide by picking whichever reading is convenient. Build it, get it
reviewable, and hand the merge-timing question back to System Hub/Mark
rather than merging on your own judgment call.

## What to produce

Follow the build handoff's own §8 commit sequence — six small, independently
reviewable commits (tokens/fonts → table bar → Level-3 panel/sheet → toggle
retirement → favicon/logo → breakpoints). Run the §7 five-count check on both
breakpoints before calling it done. Screenshot or otherwise demonstrate each
acceptance criterion rather than asserting it passed.

## Coordination boundary

Stay inside `cic-poc/frontend/`. Don't touch the Atlas/World Map integration,
Representative Modes, or anything backend — those are separate, currently
active workstreams (see `Ministry/Features/` for each one's own
`Integration-Notes.md` if you need to check what's safe to leave alone). If
you find a real defect outside this scope while working, log it and hand it
back rather than fixing it inline.

## Logging

`Ministry/Features/Increment-1-Build/Decision-Log.md` (new — create it),
dated entries, same discipline as every other thread in this project. Report
back to System Hub when the six commits are done and the five-count check
passes, including the merge-timing question above.
