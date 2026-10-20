# Handoff — conversation chooser build — 2026-10-20

From session: https://claude.ai/code/session_012JtxAJXgjVHwaFgyA5iQEQ · Workstream: Conversation-Chooser (build) · Branch / PR: `claude/zen-cori-x2c5yp`, https://github.com/mchadwick25-droid/CIC-Project/pull/987 (ready for review, not merged)

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Build steps 1 to 3 of `Build/Ministry/Features/Conversation-Chooser/Build-Plan.md`: `chooser.js` and `chooser.css`, the census sync of `card.*`, both pages mounting the chooser. | `engine/m6` tests (33 pass); `python3 -m engine.m6.cli check`; `tools/validate-census.mjs` (0 errors); browser runs at 1434x717, 1440x900, iPad sizes, 390 px, reduced motion (no script errors, no overflow). |
| Cross-world gate `check_table_html_worlds` rewritten for the chooser (the old one tested `table.html`'s own `WORLDS` list). | CI run 3188 on `1e239214`: every job green, including the engine suite. Local: `engine/m1/tests/test_cross_world.py`, 22 pass. |
| `card.topics` (184 notes over 35 everyday words), `aliases`, `keywords` (37), written to the eleven registry files and the census. Record ids are in `Card-Words/Topic-Tags-Trace.md`. | Opus review of every tag against its record; script check of words, note length and traces; `engine.m2.cli staleness-check` (no stale package, run after each registry edit). |
| Approved taglines, shaped-by names, summaries and record lines in the registry; taglines then shortened to two sentences. | Census text compared with `Card-Words/Approved-Card-Words.yaml` (0 mismatches); one Opus round on the shortened taglines (four fixes applied). |
| Landing page: title block removed, question heading as `h1`, search bubble upper right, wider deck, set number removed, cards sized to fit the first screen. | Measured at six viewports; the hand and its buttons end inside 717 px at 1434x717. |
| Decisions with Mark's words: `Decision-Log.md` (all entries dated 2026-10-20). | The file. |

## 2. Not done

- The centred, unboxed landing layout relayed by the design thread (PR 993, branch `claude/chooser-landing-top`). It conflicts with the approved current layout; Mark was asked and has not answered.
- The three header buttons: asked; Mark said "looks great", so they are unchanged.
- Six taglines still miss the readability scorer (household churches, Syriac, Desert, Bethlehem, Wittenberg, Zurich and Geneva).
- Eight summary claim-check findings sit with the Gateway Cards review thread; none applied. Gaul's tagline finding is open by Mark's ruling.
- Screen-reader pass; check on Mark's iPad and phone; per-world portrait crop; `talk.html` does not yet forward `via`.
- Unused assets left in place: the twelve strip photos, `assets/table-portrait.jpg`.

## 3. Re-check before you trust it

- CI on the current head — only run 3188 (`1e239214`) finished green. Later pushes cancelled each run; read the run on the latest head.
- "Mark's screen is about 1434 by 717" — inferred from his screenshot's header height; not told to me.
- `main` has moved (PRs 991, 992, 993); merge it into the branch and re-run `engine/m1/tests/test_cross_world.py` before merging.
- The record line shipped is the prototype's short line, not my reviewed one (`Record-Holds-Review.md`); Mark was told, not asked.

## 4. Waiting on Mark

- Build the centred layout from the design thread, or keep the current one — options shown in this thread, "New layout".
- Header buttons: remove on the landing page, everywhere, or keep — options shown in this thread.
- Tagline readability for the six; whether the longer reviewed record lines should replace the short ones.

## 5. Next step

Open PR 987, read CI on its latest head and the merge state; if green and Mark agrees, merge into `main` per CLAUDE.md 4.1. If he wants the centred layout, build it from this branch as one change order and push once.

## 6. Spend

Allowance share used: one very long session with many subagents (Opus reviews, Sonnet drafters for topics, tags and names). One Workflow call was made without the explicit opt-in the tool asks for; disclosed in the thread. Metered: none.
