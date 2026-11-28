# Release: Tertullian (`tertullian-s-voice`) and the House Church Corinth fix, 2026-11-28

Mark: "release tertullian" (2026-11-28, relayed by the managing session).

## What changed

- **Tertullian brief:** the repeated "around the year 200" cut from the opening and kept in the approved essence ("At Carthage, in Roman Africa, around the year 200, Tertullian wrote" → "At Carthage, in Roman Africa, Tertullian wrote"). Mark saw this change before he released. 810 words, grade 8.1 (names out 7.0), reading ease 77.2, pass.
- **Card:** `secondReading` set per `Final_Check.md`: [0] minor, [1] [5] [6] same; [2]–[4] same and [7] "checked at card" stand. `briefReferences[0]` brought into line with the cut opening ("the brief puts him around the year 200; the book's own year, 197, is Widely Accepted").
- **Census** (`movements` entry `tertullian-s-voice`): `longDescription` (the brief, final newline removed), `card`, and the entry fields `Card_Edits.md` section 4 listed and the final check passed (item 6), word for word: `modernWorks` (new), `why`, `relationsSummary`, `teaser`, `legacy`, `dates`, `voices`. No other field moved. The tradition link (`tertullian-s-voice--latin-apologists`) was already there.
- **`tools/quote_renderings.json`:** the five old Tertullian listings replaced by seven, one per quoted span of our modern English, each with `second_reading` pointing at `Final_Check.md`. "Give me the master" stands verbatim in Richardson's English and is not listed.
- **The House Church fix:** `claude/cft-fix-house-church-corinth` merged at 146bfe97 (two Corinth phrases in the `post-apostolic-house-church` brief and card; census, index and tree page as that branch built them).
- **Rebuild:** `atlas-sync`, `generate_tree_pages.mjs`, `corpus_coverage.py`. Changed: `cft-website/tree/tertullian-s-voice.html`, `cft-website/index.html`, and `cft-website/tree/latin-apologists.html` (its Tertullian link carries the new teaser). `cft-website/privacy.html` was not changed by the run.
- **Logs:** five Decision-Log entries (Tertullian's length; Tertullian's fix pass; the heart held to what his books show; the House Church Corinth fix; Ebionites stays as it is). Open-Gaps 453–456 (the census edge on Cyprian's secretary; the House Church recording; the domain's nameservers; the opponents-only tradition shape).
- **Ledger:** Tertullian was not listed in `Earlier-Approved.yaml`; `python tools/list_story_status.py --write` run.

## Judgment calls

- `briefReferences[0]` reworded after the opening lost its date: the card no longer says the brief dates the book. This is card text in line with the brief, as the fix pass ruled.
- The entry fields were applied as `Card_Edits.md` worded them, since the final check passed each one (item 6).

## Checks

See the list at the end of this file.

## Mark's rulings for this story

- "yes use foremost" (2026-11-20): never "the first". This story only.
- "Never counted a saint" left out (2026-11-20). This story only.
- Jerome's "the master" story goes to Tertullian, as one clause (2026-11-20). This story only.
- New work passes at B or with his sign-off (2026-11-28). Decision-Log, "New work passes at B or with Mark's sign-off".
- Length up to about 800 words, "a" (2026-11-28). Decision-Log, "Tertullian: length up to about 800 words". This story only.
- One fix pass, then a fresh grade, "a" (2026-11-28). Decision-Log, "Tertullian: one fix pass, then a fresh grade". This story only.
- The heart held to what his books show: the kit's own rule (Part 2, The heart), with no ruling needed. Decision-Log, "Tertullian: the heart held to what his books show". This story only.
- "release tertullian" (2026-11-28), after the opening date was cut.

## The three reviews

Outline check: FIX, 1 blocking, 10 minor. Brief review: REVISE, 3 blocking, 5 minor. Final check: FIX (card only), 0 blocking, 4 card fixes, 1 brief minor; quotes 4 same, 1 minor, 0 change meaning. Fix-pass check (`Fix_Check.md`): FIX (card only), 0 blocking in 14 changed sentences, 1 card change. Grade after the fix pass: B (rigor B, craft C); blind check passes (B, C+, B).

## Cost

This session's `total_cost_usd` is not readable from inside it. Estimated from the session's token usage at assumed list rates: about $14.60 for the fix pass and this release together, above the $10 cap. That is telemetry, not a bill. No metered spend.

## Not done

No recording (Open-Gaps 454 for the House Church). Promotion to `live` is Mark's.

## Check results

- `validate-census.mjs`: 629 movements, 736 edges, 10 eras, 0 errors, 4 warnings (shortName length, on other entries).
- `validate_census_*.test.mjs`, run file by file with a 120-second limit each: card_layout 2/0, kind 6/0, modern_works 2/0, online 10/0, outcome 7/0, retired 4/0, search_names 6/0 (pass/fail). card, council, people, quotation_originals, renderings, river_origins, secondary and story_text did not finish inside the limit on this machine; none failed. They are left to CI.
- `atlas-check` and `atlas-check --edges-only`: no changes.
- `build_tree_site.mjs`: 0 mismatched.
- `worker.test.mjs`, `generate_tree_pages.test.mjs`: pass.
- `check_live_commentary.py --base origin/main --enforce`: rc 0.
- `check_open_gaps_numbers.py`: rc 0.
- `check_spelling.py --enforce`: 0 found.
- `profile_readability`: Tertullian 810 words, grade 8.1 (names out 7.0), ease 77.2, pass; House Church 677 words, grade 7.1 (names out 6.6), ease 75.9, pass.
- `check_standard_lock.py`: no locked standard file changed.
