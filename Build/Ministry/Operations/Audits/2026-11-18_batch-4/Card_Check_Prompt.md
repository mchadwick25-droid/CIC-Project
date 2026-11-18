# Batch 4 card check prompt

You are the card checker (Brief-Kit Process.md, step 6). You did not write these cards. Read `CLAUDE.md` ("Trust and source fidelity") and `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/card.md`. Then, for each folder you are given, read `<slug>.brief.txt`, `<slug>.card.json`, `Card_Edits.md`, and the starting card: the census entry in `cic-website/data/world-census.json`, or for Cyril and Methodius `Build/Ministry/Operations/Audits/2026-11-17_varied-batch/cyril-and-methodius/cyril-and-methodius.card.json`.

Check each card:
1. **Each edit is justified.** Confirm it against its evidence (file and lines, or the brief's sentence).
2. **Nothing else moved.** Diff the card against its starting card: every field not listed in `Card_Edits.md` is word for word.
3. **One rule for references, for all twelve.** A `briefReferences` entry, or part of one, that names something the brief no longer tells is removed. List each one that remains.
4. **Census rules.** Only allowed keys, and no `briefLength`. One `quotationOriginals` entry for each quoted span in the brief, and none for a span the brief no longer quotes. Each `printed` stands verbatim at its `file` and `lines`, and every cited file is in `sources`. No quotation marks in `briefReferences` unless the words are verbatim in the brief. No audit, review or ruling named. American spelling outside verbatim printed wording.
5. **Rule on each "not found" claim, and on anything clearly wrong that was left in.**

Write `Card_Check.md` in each folder: PASS or FIX, with each FIX as an exact JSON change (the field, the old text, the new text). Do not edit any card or brief, do not run `tools/validate-census.mjs`, use no shared or scratch file, and do not commit. Reply in under 120 words per folder.
