# Batch 10: the second card pass (Mark, 2026-11-23)

Read the last entry of `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md` ("Batch 10: the cards carry what the outlines sent them"), then `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/card.md`. You work on one card, in the folder you are given. Do not edit the brief, the census or any other folder.

1. **The checker's changes, word for word.** Read `Card_Check.md`. Apply every change it gives to `<slug>.card.json` exactly as worded (each old text must occur once; if not, change nothing for it and report it). Where it lists scan readings for `tools/quote_scan_readings.json`, append them exactly as listed, in that file's format; add nothing else to it.
2. **What the outline sent to the card.** Read `Outline.md` (and `Fresh_Read.md`, `Review.md`). List every item marked "to the card", "for the card" or "card only". For each the card does not already hold, add it in the field it belongs to (`uncertain`, `legacy.traces`, `legacy.remembered`, `sources.about`, or for the council its `attended`, `decided`, `outcome`, `record`, `calledBy`), worded as plainly as the outline gives it, saying no more than its cited source at its lines, which you re-read. Credit a witness where the outline does. Do not add `briefReferences` for material the brief does not tell. Skip an item the checker already worded under step 1.
3. Keep every other field word for word. American spelling outside printed wording. No audit file named.
4. Run `node tools/validate-census.mjs --skip-quotes` against a scratch copy of `cic-website/data/world-census.json` with this card in place (never the real census), and report its errors for this entry.
5. Append to `Card_Edits.md` a section **Second pass (2026-11-23)**: each checker change, "applied word for word"; each added item, its field, its exact text and its evidence (file and lines); each item skipped and why.

Do not commit. Reply in under 100 words: changes applied, items added and skipped, validator errors.
