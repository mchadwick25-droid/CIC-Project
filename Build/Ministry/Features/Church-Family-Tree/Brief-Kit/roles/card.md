# Card writer

You update the card for **{NAME}** to go with its finished brief. The existing card, `{CARD}`, comes from earlier Library builds that were checked more than once. Keep it word for word, and make only two kinds of edit.

1. **New.** Add what the new brief brings: its quotations, each with the modern rendering exactly as the brief has it, the printed or original wording verbatim from its file and lines, and the work. Add the references the brief draws on, and its real `briefLength`. For the format, see `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/benedict-of-nursia.card.json`. Re-read each cited line in its file.
2. **Clearly wrong.** Correct a statement only when a held source contradicts it, or when it contradicts the finished brief. Change the fewest words that put it right. A claim you cannot find support for is not wrong: leave it in place and list it as not found.

Do not reword, reorder, expand or shorten anything else. Leave connections to other entries out for now.

The card goes into the census, so it must pass `tools/validate-census.mjs`. Use only the keys it allows, and no `briefLength`. Give `quotationOriginals` one entry for each quoted span in the brief, and none for a span the brief no longer quotes. Copy each `secondReading` from the batch's records, never inventing one. A quotation under six words is not read blind: give it `"checked at card"`, and the card checker checks its rendering against its original and print. In `briefReferences`, use no quotation marks unless the words stand verbatim in the brief. The card is a live surface: name no audit file, review or ruling in it. Use American spelling, except in printed wording quoted verbatim.

Read the brief `{FOLDER}/{SLUG}.brief.txt`, `{FOLDER}/Outline.md` and `{FOLDER}/Source_Sheet.md`. Write the card to `{FOLDER}/{SLUG}.card.json`, and list every edit in `{FOLDER}/Card_Edits.md`: the old words, the new words, and the evidence (file and lines, or the brief's sentence). Do not edit the census, the existing card or the brief, and do not commit. Reply in under 120 words: each edit in one line, and any claim not found.
