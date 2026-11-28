# Cyprian of Carthage: release

Released in one pull request with Peter of Alexandria and the ten of #1846 (branch `claude/cft-story-peter-of-alexandria`, head 61646985), the Josephus grade fix (`claude/cft-fix-josephus-grade`, head 6e5676b1, draft #1848), and the final Tatian and Suetonius (folders from `claude/cft-release-batch12-13`, head 34ea1b40). Mark: "release", then "release everything waiting", then one merge for everything (relayed by the managing session, 2026-11-28).

## What changed

- `cic-website/data/world-census.json`, entry `cyprian-of-carthage`: `longDescription` is the brief (final newline removed); `card` is `cyprian-of-carthage.card.json`, with `secondReading` "same", "same", "minor" on the three long quotes (Final_Check.md, Verdict item 3) and "checked at card" on "Thanks be to God."; `dates` "Died 258"; `teaser`, `why`, `relationsSummary` and `modernWorks` (Benson, Koch, von Soden, Monceaux) as `Card_Edits.md`, Entry fields, gives them, passed by the final check (card item 6). No other field changed; no link change.
- `tools/quote_renderings.json`: the four batch 7 `cyprian-of-carthage` listings are replaced by the brief's four spans, each with `second_reading` pointing at `Final_Check.md`.
- Entries `tatian` and `suetonius`, with their renderings: copied whole from the census and renderings of `claude/cft-release-batch12-13`, where their release applied the brief, card and passed entry fields; no other field differs from `main`. Their folders and the batch's `Second_Readings*.md` records come from the same branch. Methodius stays at its live text.
- Rebuilt: `cft-website/index.html`, the tree pages of Cyprian, Tatian, Suetonius and `latin-pastoral-congregational-christianity` (Cyprian's shown dates), and `Story-Ledger.md`. `corpus_coverage.py` changed nothing. `cft-website/privacy.html` was rewritten by the page builder from an older source and put back.

## Judgment calls

- The card hand carried `secondReading: "same"` from the old card onto three new renderings; removed under `roles/card.md` before the final check (`Card_Edits.md`, "After the card hand").
- Suetonius's `regions` ("Asia Minor", no held support), which its card writer left for release to judge: left as it is, since it is a census change no one has ruled on. For Mark.
- Merge of the Peter branch: `suetonius.brief.txt` and `Revision.md` conflicted; the release branch's later versions (34ea1b40, the grade fixes) were kept.

## Checks

- `validate-census.mjs`: 0 errors, 4 warnings (other entries' shortName length).
- `atlas-check`: pass. `atlas-check --edges-only`: no changes.
- `build_tree_site.mjs`: 1778 own files, 0 mismatched.
- `worker.test.mjs`, `generate_tree_pages.test.mjs`: 89 pass, 0 fail.
- `profile_readability`: Cyprian, Tatian and Suetonius briefs, 0 failing.
- `check_live_commentary.py --enforce`: pass. `check_open_gaps_numbers.py`: pass. `check_spelling.py --enforce`: 0 found. `check_standard_lock.py`: no locked file changed.
- `validate_census_*.test.mjs`: left to CI (the local run is longer than ten minutes, as for Josephus).

## Rulings for this story, and where each lives

- "Batch 12: the slate approved" (2026-11-27): the job, no census change, no quote reuse. This story only.
- "Batch 12: hearts and lengths approved" (2026-11-27): the heart. This story only.
- "Batch 12: the first two briefs approved, and the long stories' lengths" (2026-11-27): about 965 words. This story only.
- "Batch 12: three hearts, the era's heart timing and five lengths" (2026-11-28), item 5: 1,006 words. This story only.
- "Batch 12: the full cards for its twenty people" (2026-11-27, "a"). This story only.
- "The Jewish people" and own-title rule (2026-11-28): in the kit, Part 1. Nothing to change here (`After_Review_3.md`).
- The grade and blind check before Mark's read ("i release after the grade", 2026-11-28): grade B; blind check against Epiphanius B+, "slightly" worse (`Blind_Check.md`). A second blind check against Basil, run by the managing session, gave C; Mark released with both in hand.
- "release", "release everything waiting" (2026-11-28).

## The three reviews

- Review 1, the outline check: FIX, 1 blocking (length) and 8 minor, all applied at the outline.
- Review 2, the brief review: REVISE, 8 blocking and 10 minor; after the one revision, the fresh read found 0 blocking.
- Review 3, the final check: FIX on the card only. Brief: 13 changed sentences, 10 held and 3 summary holds, 0 blocking; quotes 2 same, 1 minor, 1 checked at card. Card: 2 blocking faults carried from the old card, settled by exact changes, applied word for word.

## Cost (session record `cost_usd`: telemetry, not a bill)

- This thread, `session_01JMNsSDYxU8Xw8aKKVo8Uju`: about $10.3 at the time of writing, including the card hand, the final check, the blind check and the combined release. Under the $25 cap. Batch 12's research, writing and reviews are counted in batch 12's own threads.

## Not done

- Recording (Kit step 8): a paid run, still to come.
