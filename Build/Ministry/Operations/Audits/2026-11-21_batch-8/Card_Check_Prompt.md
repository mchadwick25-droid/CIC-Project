# Batch 8 card check prompt

You are the card checker (Brief-Kit Kit.md, Part 4, step 6). You did not write these cards. Read `CLAUDE.md` ("Trust and source fidelity") and `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/card.md`. Then, for each folder you are given, read `<slug>.brief.txt`, `<slug>.card.json`, `Card_Edits.md`, and the starting card: the census entry's `card` in `cic-website/data/world-census.json` (also in the folder as `Card.existing.json`). Four entries have no card (Tertullian, Cyprian of Carthage, Pamphilus of Caesarea, Lactantius): their cards are new, so for them check every field against its evidence in `Card_Edits.md`, and check it does not contradict the entry's existing fields.

Check each card:
1. **Each edit is justified.** Confirm it against its evidence (file and lines, or the brief's sentence).
2. **Nothing else moved** (cards with a starting card only). Diff the card against its starting card: every field not listed in `Card_Edits.md` is word for word.
3. **One rule for references, for every card.** A `briefReferences` entry, or part of one, that names something the brief no longer tells is removed. List each one that remains.
4. **Census rules.** Only allowed keys, and no `briefLength`. One `quotationOriginals` entry for each quoted span in the brief, and none for a span the brief no longer quotes. Each `printed` stands verbatim at its `file` and `lines`, and every cited file is in `sources`. No quotation marks in `briefReferences` unless the words are verbatim in the brief. No audit, review or ruling named. American spelling outside verbatim printed wording.
5. **Originals.** Where the outline renders a quote from a held original (Latin, Greek, French, German), the card's `quotationOriginals` should carry it; a card that leaves it out where the outline cites it is a FIX.
6. **Rule on each "not found" claim, and on anything clearly wrong that was left in.**

Write `Card_Check.md` in each folder: PASS or FIX, with each FIX as an exact JSON change (the field, the old text, the new text). Do not edit any card or brief, do not run `tools/validate-census.mjs`, use no shared, scratch or temporary file of any kind, and do not commit. Reply in under 120 words per folder.
