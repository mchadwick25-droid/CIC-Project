# Batch header

- **Story:** Priscillian (census id `priscillian`). **Folder:** `Build/Ministry/Operations/Audits/2026-11-22_batch-10/priscillian/`. **Card file:** `Build/Ministry/Operations/Audits/2026-11-22_batch-10/priscillian/Card.existing.json`.
- **Census entry:** exists; no new entry is written. Its other fields are in `cic-website/data/world-census.json`.
- **This batch's ruling (Mark, 2026-11-23, "Batch 10 hearts approved, with the lengths and a cut-first line in the kit", item 5):** "the story does not say he was the first Christian put to death on a church accusation, which rests only on editors' notes. It tells the verdict as the court's, for sorcery; the card carries the editors' claim and Bernays's view (as Hefele reports it), each credited."

---

# Card writer

You update the card for **Priscillian** to go with its finished brief. The existing card, `Build/Ministry/Operations/Audits/2026-11-22_batch-10/priscillian/Card.existing.json`, comes from earlier Library builds that were checked more than once. Keep it word for word, and make only two kinds of edit.

1. **New.** Add what the new brief brings: its quotations, each with the modern rendering exactly as the brief has it, the printed or original wording verbatim from its file and lines, and the work. Add the references the brief draws on, and its real `briefLength`. For the format, see `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/benedict-of-nursia.card.json`. Re-read each cited line in its file.
2. **Clearly wrong.** Correct a statement only when a held source contradicts it, or when it contradicts the finished brief. Change the fewest words that put it right. A claim you cannot find support for is not wrong: leave it in place and list it as not found.

Do not reword, reorder, expand or shorten anything else. Leave connections to other entries out for now.

The card goes into the census, so it must pass `tools/validate-census.mjs`. Use only the keys it allows, and no `briefLength`. Give `quotationOriginals` one entry for each quoted span in the brief, and none for a span the brief no longer quotes. Leave out `secondReading` for a quotation of six words or more: release sets it from the second readings, never inventing one. A quotation under six words is not read blind: give it `"checked at card"`, and the card checker checks its rendering against its original and print. In `briefReferences`, use no quotation marks unless the words stand verbatim in the brief. The card is a live surface: name no audit file, review or ruling in it. Use American spelling, except in printed wording quoted verbatim.

Part 1 of `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, under Rigor, governs the card too. Whatever the outline, review or fresh read sends to the card goes under `uncertain` or the field it belongs to. A quote whose original is held only in a damaged scan prints its English alone unless another held print confirms the reading. Check Greek by hand.

Read the brief `Build/Ministry/Operations/Audits/2026-11-22_batch-10/priscillian/priscillian.brief.txt`, `Build/Ministry/Operations/Audits/2026-11-22_batch-10/priscillian/Outline.md`, `Build/Ministry/Operations/Audits/2026-11-22_batch-10/priscillian/Source_Sheet.md`, `Build/Ministry/Operations/Audits/2026-11-22_batch-10/priscillian/Review.md` and `Build/Ministry/Operations/Audits/2026-11-22_batch-10/priscillian/Fresh_Read.md`. Write the card to `Build/Ministry/Operations/Audits/2026-11-22_batch-10/priscillian/priscillian.card.json`, and list every edit in `Build/Ministry/Operations/Audits/2026-11-22_batch-10/priscillian/Card_Edits.md`: the old words, the new words, and the evidence (file and lines, or the brief's sentence). Do not edit the census, the existing card or the brief, and do not commit. Reply in under 120 words: each edit in one line, and any claim not found.
