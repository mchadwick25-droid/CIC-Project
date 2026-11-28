# Release: Peter of Alexandria

Released in one merge with release 13 (PR #1846's branch, merged in), less the three stories it graded F and D (Mark, 2026-11-28, Decision-Log "Release 13 and Peter of Alexandria in one merge; the F and D stories held"). Release 13's own record is `Build/Ministry/Operations/Audits/2026-11-26_batch-12/Release.md`.

## Held from release 13

- Suetonius (F), Tatian (F) and Methodius of Olympus (D): census entries, tree pages and `tools/quote_renderings.json` listings put back to `main`'s, then the tree rebuilt; each page now equals `main`'s. `tools/quote_scan_readings.json` is keyed by source file, not story, and is kept as release 13 wrote it. Open-Gaps 449.
- The six graded C go out on Mark's choice, his sign-off under "New work passes at B or with Mark's sign-off".

## What changed

- `cic-website/data/world-census.json`, entry `peter-of-alexandria` only: `longDescription` is the final brief (698 words, final newline removed); `card` is `peter-of-alexandria.card.json` with `secondReading` "same" on its three quotations (`Final_Check.md`, Quotes); `teaser` as the final check worded it (card item 7); `modernWorks` added, the seven works listed in `Card_Edits.md` (Entry fields, and the section after review 3), titles taken from the files' own headers for the ANF 6 and NPNF volumes as `Card_Edits.md` asked.
- `tools/quote_renderings.json`: the three batch 7 listings for this entry replaced by the three current quotations (Pedalion Greek, ANF6 English, NPNF 1 English), second reading `Final_Check.md`, "same". The Epiphanius listing is gone with its quote.
- Rebuilt: `cft-website/index.html` and `cft-website/tree/peter-of-alexandria.html`; `cic-website/data/corpus-coverage.json` unchanged.
- `Build/Ministry/Features/Church-Family-Tree/Story-Ledger.md`: the story's batch 7 → 12 (from `tools/list_story_status.py --write`). It was not in `Earlier-Approved.yaml`.
- `tools/cut_source_excerpts.py`: the version from `claude/kind-cannon-rpw8d0`, which reads batch 12's sheet form (the same change the Josephus PR carries).

## Judgment calls

- The tree generator also rewrote `cft-website/privacy.html` from an older text than `main` holds; that change was put back, as it is not this story's. The index rebuild also carries Pliny the Younger's census text (tile and description) that `main`'s census already held but the index did not.
- The final check's MINOR on `knownFor` ("Great Persecution", "lapsed") had no exact wording, so it was not applied.

## Checks

- `validate-census.mjs --atlas --tree`: 629 movements, 736 edges, 0 errors, 4 warnings (existing).
- After bringing `main` in (the Josephus release): `atlas-check` and `--edges-only`: no changes. `build_tree_site.mjs`: 0 mismatched. Worker and tree-page tests: 89 of 89 pass. `validate_census_*` tests: 124 of 124 pass.
- `check_live_commentary.py --enforce`: pass. `check_open_gaps_numbers.py`: pass. `check_spelling.py --enforce`: 0. `profile_readability`: 692 words, grade 9.5 (names out 8.7), reading ease 69.1, pass. `check_standard_lock.py`: no locked file changed.

## Reviews

- Review 1, outline check (batch 12): FIX, 4 BLOCKING, 7 MINOR; all applied in the fix pass.
- Review 2, brief review (batch 12, `Review.md`): REVISE, 3 BLOCKING, 10 MINOR; the one revision, then a fresh read's three word-for-word changes.
- Review 3, final check (`Final_Check.md`): FIX. Brief: 0 BLOCKING; quotes 3 SAME of 3. Card: 7 changes, applied word for word (six to the card, the teaser at release); item 8 to Mark.

## Rulings for this story

- "Batch 12: the slate approved" (2026-11-27): the job; decisions 4 (no census change) and 7 (no quote reuse). This story only.
- "Batch 12: hearts and lengths approved" (2026-11-27): the heart. This story only.
- "Batch 12: three hearts, the era's heart timing and five lengths" (2026-11-28), item 5: 698 words. This story only.
- "Batch 12: the full cards for its twenty people" (2026-11-27, "a"). This story only.
- Final check card item 8, "b" (2026-11-28), applied under "Modern works on the cards" (2026-11-26) and Kit Part 1, Rigor: the eight modern-view items of `uncertain` (`Card_Edits.md`, last section). This story only; it follows the kit lines it cites.
- Graded B, "OK to keep" (`Build/Ministry/Operations/Audits/2026-11-28_era1-new-grades/Grades.csv`). Released by Mark, 2026-11-28: "lets get everything together in one merge then continue" (Decision-Log, same day). This merge only.

## Cost

This session's record, `usage.cost_usd` (telemetry at API rates, not a bill): $9.86 at handover (2026-11-28), both Sonnet card hands and the Opus final check included.

## Not done


- Recording (step 8): not in this run. The old recording (4:17, of the earlier text) keeps its file and manifest entry; the rebuilt page hides its player, as slate decision 5 says.
- The Melitian line and Pamphilus's home stay in Open-Gaps for a later census pass (slate decision 4).

## Mechanical fix in release 13's cards

- `check_spelling.py --enforce` found "Saviour" twice in card prose (not quotes): Pamphilus's timeline ("the Saviour's deeds") and Hippolytus's card ("On the praise of our Lord and Saviour"). Both are now "Savior" (Decision-Log 77, American spelling), and the pages are rebuilt.
