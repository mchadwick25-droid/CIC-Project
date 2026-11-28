# Josephus: release

## What changed

- `cic-website/data/world-census.json`, entry `josephus`: `longDescription` is the brief (final newline removed). `card` is `josephus.card.json`, with each quotation's `secondReading` set to "same", as the final check gave it. `dates` is "37 to after 93" (final check C1, item 9). `modernWorks` lists three works: Whiston's Dissertation I (`Card_Edits.md`), and McGiffert and Chabot (final check C1, item 10). `teaser` takes the wording `Card_Edits.md` proposed, which the final check said holds. No other field changed. The census gets no link change (slate decision 3).
- `tools/quote_renderings.json`: the three old `josephus` listings from batch 6 are replaced by the brief's three spans, each with `second_reading` pointing at `Final_Check.md`. Origen's line on James's justice is no longer quoted, so its listing is gone.
- Rebuilt: `cft-website/index.html` (the map's Josephus record), `cft-website/tree/josephus.html`, `Story-Ledger.md`. `corpus_coverage.py` changed nothing.
- `tools/cut_source_excerpts.py`: now reads the source sheet's `**NAME**: \`file\`` form (from `claude/kind-cannon-rpw8d0`). `Source_Sheet.md` is back as batch 12 wrote it.

## Judgment calls

- Chabot's `year` is given as the string "1899", the census's form for years. The final check gave it as a number, and the tree page builder fails on a number.
- One spelling, "Acts of Pilate and our Saviour" → "Savior", in a timeline line in the card and census. The line is a paraphrase, not a quotation, so the American-spelling check (Decision-Log 77) applies. The final check did not word this change, so it goes to Mark.
- `cft-website/privacy.html` was rewritten by the page builder from a source older than `main`'s page. This is not the story's change, so it was put back.
- The quotes in the War 3.8 and Antiquities 18.3 passages were changed after review 3 by Mark's ruling "b". Their `secondReading` stays "same" from the final check, which read the earlier wording. Only the word group for *Ioudaioi* changed.

## Checks

- `validate-census.mjs`: 0 errors, 4 warnings (other entries' shortName length).
- `node --test tools/tests/validate_census_*.test.mjs`: see the pull request's CI. The local run did not finish within 10 minutes.
- `atlas-check`: pass. `atlas-check --edges-only`: no changes.
- `build_tree_site.mjs`: 1778 own files, 0 mismatched.
- `worker.test.mjs`, `generate_tree_pages.test.mjs`: pass.
- `check_live_commentary.py --enforce`: pass. `check_open_gaps_numbers.py`: pass. `check_spelling.py --enforce`: 0 found. `check_standard_lock.py`: no locked file changed.
- `profile_readability`: 787 words, grade 9.3 (8.4 with names out), reading ease 72.6 with names out, 0 failing.

## Rulings for this story, and where each lives

- "Batch 12: the slate approved" (2026-11-27): the job, decision 3 (no census change), decision 6 (no quote reuse). This story only.
- "Batch 12: hearts and lengths approved" (2026-11-27): the heart. This story only.
- "Batch 12: three hearts, the era's heart timing and five lengths" (2026-11-28), item 5: 778 words and its heart timing. This story only.
- "Batch 12: the full cards for its twenty people" (2026-11-27, "a"). This story only.
- "the Jewish people" in the narrator's words (2026-11-28, "A, and make it a rule for every story"). It now lives in the kit, merged to `main` by PR #1842.
- "b" (2026-11-28): "the Jewish people" in the two quotes where Josephus speaks, and the title "Jewish Antiquities". Whether this goes into the kit is the managing session's call (PR #1842). Here it is applied to this story.
- "release" (2026-11-28).

## The three reviews

- Review 1, the outline check: FIX, 6 blocking and 5 minor, all applied.
- Review 2, the brief review: REVISE, 5 blocking and 8 minor, judged at 725 words.
- Review 3, the final check: FIX. The brief: 3 quotes SAME, 0 blocking. The card: 1 blocking fault (C1, ten exact changes) and 3 minor, all applied word for word.

## Cost (session records, `cost_usd`: telemetry, not a bill)

- First thread, `session_01JMNsSDqQg4xAt2fkcFSYg3`: $8.81. That figure includes its card hand, and also its work on the kit rule, PR #1842.
- Second thread, `session_01JMNsSChJz9HD9ucqmkYdbi`, at release: $5.96, including the final check's hand.
- Total: about $14.77, under the $25 cap. Batch 12's research, writing and reviews are counted in batch 12's own threads.

## Not done

- Recording (Kit step 8): a paid run, still to come.
- The outline's "card only" line for modern works, which caused the card's blocking fault: raised as a kit gap, for the managing session.
