# Josephus: story README (brief kit, one story per thread)

Run under the brief kit as merged in PR #1841. Launch: from the managing session `session_01JMNsSEDBczUWe4gaYxbKDj`. Branch `claude/cft-story-josephus`, from `main`; this folder alone came over from `claude/batch12-era1-persons`.

## Step

- Done: research, outline check (review 1), writing, brief review (review 2), revision, all in batch 12. Mark accepted the length, 778 words, as it stands.
- Done here: `Source_Sheet.md` file names put in the kit's `**NAME** = \`file\`` form (13 lines, nothing else) so `tools/cut_source_excerpts.py` could read them; `Excerpts.md` cut. `Story_Header.md`, `Card_Prompt.filled.md` and `Final_Check_Prompt.filled.md` written.
- Step 5, card: done by one Sonnet hand from `Card_Prompt.filled.md`: `josephus.card.json` and `Card_Edits.md`. A census copy leaves three validator errors that release clears: no `secondReading` yet, and three old `tools/quote_renderings.json` records to replace. Not found: the death date in `datesNote` (modern editors only; left in place). The Greek of the passage on Jesus is held only in damaged scans, so that entry prints its English alone.
- Second thread (`session_01JMNsSChJz9HD9ucqmkYdbi`): `Source_Sheet.md` put back as batch 12 wrote it, and the tool fixed to read that form (from `claude/kind-cannon-rpw8d0`); `Excerpts.md` re-cut, unchanged. Review 3 done: `Final_Check.md`, FIX. Its card changes applied word for word to `josephus.card.json`; its entry-field changes (items 9 and 10: `dates` "37 to after 93", McGiffert and Chabot added to `modernWorks`) are applied at release. Brief unchanged. Brief page sent to Mark: https://claude.ai/artifact/FqWLXytRYEZvm3HGth6186. Waiting for his word.
- Handover: the first thread stopped at about 150,000 tokens of context, as the launch requires.

## Next, in order

1. Card: done (above). Go straight to review 3.
2. Review 3: `python tools/list_second_readings.py <folder> --requests <folder> --prefix josephus`, then one fresh Opus hand from `Final_Check_Prompt.filled.md` alone. It must not open the earlier reviews. Apply its exact changes word for word. A blocking fault its exact change cannot settle stops the story and goes to Mark.
3. Mark reads the brief: one Artifact page with the final brief and the three reviews' counts (the outline check, `Outline_Check.md`; the batch 12 review as review 2, `Review.md`; the final check). Send the link to the managing session and wait for Mark's word.
4. Release (`roles/release.md`): one draft pull request into `main`, pushed once after the local checks pass, then marked ready; merge when CI is green; check churchfamilytree.com. Cost in `Release.md` from the session records (`total_cost_usd`, telemetry, not a bill).

## Open items

- "The Jewish people" (Mark, 2026-11-28, in the first thread: "A, and make it a rule for every story"). Applied after review 3 to the narrator's own words: 6 brief sentences (`Revision.md`, last section) and 16 card lines (`Card_Edits.md`, last section). Quotes and the title *Antiquities of the Jews* are unchanged. The brief is now 785 words. The wording is the thread's own and came after review 3, so under the kit it goes to Mark with the brief page. The kit rule itself is not yet written: it needs its own pull request to `main` and one targeted check.

- The card's scope: the launch gives the existing card as the starting card under `roles/card.md`; Mark's batch 12 ruling "a" (2026-11-27) asks for the full card, Timeline included. Both are kept: the header quotes the ruling, and the card writer keeps the existing card word for word and adds the Stage Two sections. Raised to the managing session for Mark.
- Kit gap from the final check, for Mark: the outline line "Modern, making claims of their own (card only)" sent modern views to the card; proposed "modernWorks only, by what each covers". Not applied.
- Cost cap (Mark, through the managing session): $25 on the session record's `total_cost_usd`; stop at about $20 before release and report. First thread at handover: about $2.50, plus its card hand.

## Rulings for this story

- "Batch 12: the slate approved" (2026-11-27): the job, decisions 3 (no census change) and 6 (no quote reuse). This story only.
- "Batch 12: hearts and lengths approved" (2026-11-27): the heart as `Outline.md` states it. This story only.
- "Batch 12: three hearts, the era's heart timing and five lengths" (2026-11-28, "follow recommendations on all"), item 5: Josephus 778 and its heart timing. This story only.
- "Batch 12: the full cards for its twenty people" (2026-11-27, "a"). This story only.
- "The Jewish people" (2026-11-28): every story; the kit line is to follow (above).
