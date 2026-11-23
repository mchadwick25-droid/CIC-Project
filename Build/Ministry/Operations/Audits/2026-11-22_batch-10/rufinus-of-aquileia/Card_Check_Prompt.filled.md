# Batch header

- **Story:** Rufinus of Aquileia (census id `rufinus-of-aquileia`). **Folder:** `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/`. **Card file:** `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/Card.existing.json`.
- **Census entry:** exists; no new entry is written. Its other fields are in `cic-website/data/world-census.json`.


---

**Your task:** the check pass at the end of the role below ("The check pass"), for this card only. You did not write it.

# Card writer

You update the card for **Rufinus of Aquileia** to go with its finished brief. The existing card, `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/Card.existing.json`, comes from earlier Library builds that were checked more than once. Keep it word for word, and make only two kinds of edit.

1. **New.** Add what the new brief brings: its quotations, each with the modern rendering exactly as the brief has it, the printed or original wording verbatim from its file and lines, and the work. Add the references the brief draws on, and its real `briefLength`. For the format, see `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/benedict-of-nursia.card.json`. Re-read each cited line in its file.
2. **Clearly wrong.** Correct a statement only when a held source contradicts it, or when it contradicts the finished brief. Change the fewest words that put it right. A claim you cannot find support for is not wrong: leave it in place and list it as not found.

Do not reword, reorder, expand or shorten anything else. Leave connections to other entries out for now.

The card goes into the census, so it must pass `tools/validate-census.mjs`. Use only the keys it allows, and no `briefLength`. Give `quotationOriginals` one entry for each quoted span in the brief, and none for a span the brief no longer quotes. Leave out `secondReading` for a quotation of six words or more: release sets it from the second readings, never inventing one. A quotation under six words is not read blind: give it `"checked at card"`, and the card checker checks its rendering against its original and print. In `briefReferences`, use no quotation marks unless the words stand verbatim in the brief. The card is a live surface: name no audit file, review or ruling in it. Use American spelling, except in printed wording quoted verbatim.

Part 1 of `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, under Rigor, governs the card too. Whatever the outline, review or fresh read sends to the card goes under `uncertain` or the field it belongs to. A quote whose original is held only in a damaged scan prints its English alone unless another held print confirms the reading. Check Greek by hand.

Read the brief `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/rufinus-of-aquileia.brief.txt`, `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/Outline.md`, `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/Source_Sheet.md`, `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/Review.md` and `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/Fresh_Read.md`. Write the card to `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/rufinus-of-aquileia.card.json`, and list every edit in `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/Card_Edits.md`: the old words, the new words, and the evidence (file and lines, or the brief's sentence). Do not edit the census, the existing card or the brief, and do not commit. Reply in under 120 words: each edit in one line, and any claim not found.

## A new card

Where there is no existing card, build one with every field the other cards carry that the sources hold, in the format above. Every claim comes from the source sheet or outline at a cited line, or from the finished brief. Where the census entry already has other fields (`voices`, `legacy`, `why`, `sourcing` and the like), the card must not contradict them: list each conflict. In `Card_Edits.md`, list each field with its evidence.

## A new person's census entry

Where the person has no census entry, also write `Build/Ministry/Operations/Audits/2026-11-22_batch-10/rufinus-of-aquileia/rufinus-of-aquileia.entry.json`, `major: true`, told within the tradition the slate names. Follow `cyril-and-methodius` in `cic-website/data/world-census.json`: the same keys, in the same order, and no others, filled as the other person entries of that era fill them. `atlasId` is the next free one in that era's series. Dates, places and regions come only from the card and the outline's Setting. The `teaser` is one sentence in the model's form, saying no more than the card's `knownFor` and the brief. `longDescription` is the brief, final newline removed; `reviewStatus` is "AI-checked"; `card` is the card. List each field and its source in `Card_Edits.md`.

## The check pass

The card checker did not write the card. Read `CLAUDE.md` ("Trust and source fidelity") and this role, then the brief, the card, `Card_Edits.md`, the starting card if there is one, and the entry if there is one. Check:
1. Each edit or field is justified by its evidence.
2. With a starting card, nothing else moved: every field not listed in `Card_Edits.md` is word for word.
3. A `briefReferences` entry that names something the brief no longer tells is removed.
4. The census rules above: allowed keys, one `quotationOriginals` entry per quoted span and none for a dropped one, each `printed` verbatim at its file and lines, each cited file in `sources`, no audit named, American spelling. Where the outline renders from a held original, the card carries it.
5. Each quotation marked "checked at card": its rendering against its original and print.
6. Each claim listed as not found, and anything clearly wrong left in.
7. A census entry: each field against its source, no `atlasId` already in use.

Write `Card_Check.md`: PASS, or FIX with each change exact (the field, the old text, the new text). Edit nothing. Reply in under 120 words.
