# Handoff — conversation chooser, landing page finish — 2026-10-20

From session: https://claude.ai/code/session_01DieKxWNS33gUktGHTTiGeS · Workstream: Conversation-Chooser (design thread, which took over the build to finish it) · Branch / PR: `claude/zen-cori-x2c5yp`, https://github.com/mchadwick25-droid/CIC-Project/pull/987, merged into `main` by this thread once CI was green

Read with the build thread's own handoff, `2026-10-20_conversation-chooser-build.md`, which covers the chooser component, the census sync, the topic search and the card words. This one covers what changed after Mark moved the work here.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| `main` merged into the branch twice (the build thread's merge and this thread's); the decision-log conflicts resolved keeping every entry. One push went up with conflict markers left in `Decision-Log.md`; the next commit removed them. | `grep` for markers returns none; 36 entries in the log. |
| Landing page takes the Google Arts and Culture feel (Mark's change orders of 2026-10-20): chooser unboxed, question centred in the text colour at weight 400, search bubble under it with its hint read only by screen readers, sub-line moved under the hand's controls, hand up to 400 px cards, era chips and count in one centred row. | Rendered locally with web fonts blocked: no script errors at 1280x900, 1434x717, 1024x768, 820x1180, 390x844; no sideways overflow. Cards 219 to 777 px at 1280x900; cards end at the fold at 1434x717. |
| Masthead on every page that carries it: the three feature links as text links, one row with the wordmark, "Tell us what you think" and Menu. Applied to `index.html`, `table.html`, the eleven tradition pages, `assets/style.css` (header row widened to 64rem) and `assets/feedback.css` (four-column header row from 1000 px). The Tree's bar and the conversation page's bar untouched. | Header 68 px on the landing, table and tradition pages; 61 px on `about.html` and `privacy.html`, at 1024 and 1280 px. |
| "See all" lays the whole deck on the page under the hand's buttons: wrapping grid, no sideways scroll, no scroll buttons; the small cards lose the era strip, run the portrait to the top and carry name, tradition and "Shaped by …" at a smaller size. Mark: "great that looks much better". | Eleven cards render; plate heights 88 to 99 px of 210; no errors at 1280 and 390 px. |
| Records: five decision-log entries in Mark's words (title off; page feel; takeover and masthead; See all on the page; small cards). PR 987's description rewritten for the takeover. | `Build/Ministry/Features/Conversation-Chooser/Decision-Log.md`. |
| Local checks on the merged branch. | `engine/m1/tests/test_cross_world.py` 22 pass; `engine/m6` 33 pass; `tools/validate-census.mjs` 0 errors; `tools/check_live_commentary.py --enforce --base origin/main` exit 0; `tools/check_paths.py` 0 new unresolved. |

## 2. Not done

- Everything in section 2 of the build thread's handoff still stands: screen-reader pass, Mark's iPad and phone check, per-world portrait crop, `via` not forwarded by `talk.html`, six taglines not yet scored for readability, eight summary claim-check findings with the Gateway Cards review thread, Gaul's tagline finding open by Mark's ruling, unused strip photos and `assets/table-portrait.jpg` left in place.
- The hand hint line ("Hover or tab to raise a card…") stays under the deck; Mark has not said whether it should go.
- The tradition pages' masthead CSS was edited in place on the eleven generated pages; `cic-website/templates/tradition.html` carries no masthead rule, and the generator keeps each page's chrome, so a regeneration should not revert it. Not re-run to prove it.
- Promotion of `main` to `live` is Mark's call through the promotion runbook.

## 3. Re-check before you trust it

- That the masthead holds one row with the real web fonts; the local renders used fallback fonts, which are wider, so the real fonts should only help. Check the branch preview or the staging deploy at 1024 and 1280 px.
- That `generate_tradition_pages.py` leaves the edited masthead CSS alone: run it and diff.
- Mark's screen size: the build thread inferred 1434 by 717 from a screenshot; not confirmed.

## 4. Waiting on Mark

- Nothing for this PR. After merge: whether to promote `main` to `live`; the record-line choice (short prototype line vs the longer reviewed lines in `Card-Words/Record-Holds-Review.md`); the six taglines' readability; the hint line.

## 5. Next step

Check the staging deploy of `main` on an iPad and a phone (build plan step 4), then run the screen-reader pass. Open `Build/Ministry/Features/Conversation-Chooser/Build-Plan.md` step 4 and the build thread's handoff section 2.

## 6. Spend

Allowance share used: one long session; four read-only Opus subagents earlier in the day for the claim checks; none for the build. Metered: none.
