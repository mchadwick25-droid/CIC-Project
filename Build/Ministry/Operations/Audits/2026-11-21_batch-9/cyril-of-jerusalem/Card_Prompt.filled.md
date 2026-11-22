# Batch header

- **Story:** Cyril of Jerusalem (census id `cyril-of-jerusalem`). **Folder:** `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/`. **Card file:** `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/Card.existing.json`.
- **Census entry:** exists; no new entry is written. Its other fields are in `cic-website/data/world-census.json`.
- **Mark's ruling (2026-11-22, "Batch 9: two lengths after review"):** two lines go to the card: Theodoret's later quoting of the fourth lecture, and Egeria's order of teaching (the Scriptures from Genesis, the creed after five weeks, Easter-week teaching in the tomb chapel with the doors shut).

---

# Card writer

You update the card for **Cyril of Jerusalem** to go with its finished brief. The existing card, `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/Card.existing.json`, comes from earlier Library builds that were checked more than once. Keep it word for word, and make only two kinds of edit.

1. **New.** Add what the new brief brings: its quotations, each with the modern rendering exactly as the brief has it, the printed or original wording verbatim from its file and lines, and the work. Add the references the brief draws on, and its real `briefLength`. For the format, see `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/benedict-of-nursia.card.json`. Re-read each cited line in its file.
2. **Clearly wrong.** Correct a statement only when a held source contradicts it, or when it contradicts the finished brief. Change the fewest words that put it right. A claim you cannot find support for is not wrong: leave it in place and list it as not found.

Do not reword, reorder, expand or shorten anything else. Leave connections to other entries out for now.

The card goes into the census, so it must pass `tools/validate-census.mjs`. Use only the keys it allows, and no `briefLength`. Give `quotationOriginals` one entry for each quoted span in the brief, and none for a span the brief no longer quotes. Leave out `secondReading` for a quotation of six words or more: release sets it from the second readings, never inventing one. A quotation under six words is not read blind: give it `"checked at card"`, and the card checker checks its rendering against its original and print. In `briefReferences`, use no quotation marks unless the words stand verbatim in the brief. The card is a live surface: name no audit file, review or ruling in it. Use American spelling, except in printed wording quoted verbatim.

Part 1 of `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, under Rigor, governs the card too. Whatever the outline, review or recheck sends to the card goes under `uncertain` or the field it belongs to. A quote whose original is held only in a damaged scan prints its English alone unless another held print confirms the reading. Check Greek by hand.

Read the brief `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/cyril-of-jerusalem.brief.txt`, `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/Outline.md`, `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/Source_Sheet.md`, `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/Review.md` and `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/Recheck_Story.md`. Write the card to `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/cyril-of-jerusalem.card.json`, and list every edit in `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/Card_Edits.md`: the old words, the new words, and the evidence (file and lines, or the brief's sentence). Do not edit the census, the existing card or the brief, and do not commit. Reply in under 120 words: each edit in one line, and any claim not found.

## A new card

Where there is no existing card, build one with every field the other cards carry that the sources hold, in the format above. Every claim comes from the source sheet or outline at a cited line, or from the finished brief. Where the census entry already has other fields (`voices`, `legacy`, `why`, `sourcing` and the like), the card must not contradict them: list each conflict. In `Card_Edits.md`, list each field with its evidence.

## A new person's census entry

Where the person has no census entry, also write `Build/Ministry/Operations/Audits/2026-11-21_batch-9/cyril-of-jerusalem/cyril-of-jerusalem.entry.json`, `major: true`, told within the tradition the slate names. Follow `cyril-and-methodius` in `cic-website/data/world-census.json`: the same keys, in the same order, and no others, filled as the other person entries of that era fill them. `atlasId` is the next free one in that era's series. Dates, places and regions come only from the card and the outline's Setting. The `teaser` is one sentence in the model's form, saying no more than the card's `knownFor` and the brief. `longDescription` is the brief, final newline removed; `reviewStatus` is "AI-checked"; `card` is the card. List each field and its source in `Card_Edits.md`.

