# Release: Peter of Alexandria

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
- After bringing `main` in (the Josephus release): `atlas-check` and `--edges-only`: no changes. `build_tree_site.mjs`: 0 mismatched. Worker and tree-page tests: 89 of 89 pass. `validate_census_*` tests: all passed before the merge (exit 0); the rerun after the merge was still running at handover.
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
- Release on Mark's word, through the managing session (2026-11-28, "follow your recommendation to move forward").

## Cost

This session's record, `usage.cost_usd` (telemetry at API rates, not a bill): $9.86 at handover (2026-11-28), both Sonnet card hands and the Opus final check included.

## Not done

- No pull request: Mark releases after the grade (2026-11-28, "i release after the grade"), graded from this branch.

- Recording (step 8): not in this run. The old recording (4:17, of the earlier text) keeps its file and manifest entry; the rebuilt page hides its player, as slate decision 5 says.
- The Melitian line and Pamphilus's home stay in Open-Gaps for a later census pass (slate decision 4).
