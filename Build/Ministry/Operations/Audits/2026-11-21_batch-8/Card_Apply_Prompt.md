# Batch 8: apply the card checks and the originals ruling

You apply fixes that others have already worded. You make no judgment of your own. Work in `Build/Ministry/Operations/Audits/2026-11-21_batch-8/`.

## What governs
1. Each folder's `Card_Check.md` gives exact JSON fixes and scan readings.
2. The originals rule in `Build/Ministry/Operations/Audits/2026-11-19_batch-6/Batch_Originals_Ruling.md`, with Mark's three rulings in the Decision-Log entry "Batch 8: three quoted spans with no clean print" (2026-11-21): each `Card_Check.md` option marked recommended for Bernard's Nivard, Catherine's "with her leading him" and Palamas's Greek is the one that applies.
3. Where two held sources differ, the card credits both (Mark, 2026-11-19). Apply it only where a check gives the wording.

## Do
1. For each of the twelve folders (francis-of-assisi, bernard-of-clairvaux, thomas-aquinas, jan-hus, catherine-of-siena, gregory-palamas, huldrych-zwingli, thomas-cranmer, teresa-of-avila, ambrose-of-milan, jerome, leo-of-rome), apply every FIX in `Card_Check.md` to `<slug>.card.json`, word for word, as the ruling amends it. Keep the JSON valid, with the key order the card already has.
2. Add every kept scan reading to `tools/quote_scan_readings.json` (repository root), in the file's own format. Add each once.
3. Write `Card_Apply.md` in the batch folder: for each folder, each change made (field, old → new), each reading added, and anything you could not apply, with the reason.

Edit no brief except these two, word for word: in `bernard-of-clairvaux.brief.txt` replace `Nivard answered, "So heaven is for you, and earth for me? This is not a fair division."` with `Nivard answered that heaven was for them and earth for him, and the division was not fair.`; in `catherine-of-siena.brief.txt` remove only the quotation marks around `with her leading him`. Remove the matching card entries. Do not run `tools/validate-census.mjs` and do not edit the census. Use no scratch file. Do not commit. Reply in under 200 words.
