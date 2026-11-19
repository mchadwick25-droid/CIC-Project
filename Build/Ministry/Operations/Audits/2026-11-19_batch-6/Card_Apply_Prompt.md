# Batch 6: apply the card checks and the originals ruling

You apply fixes that others have already worded. You make no judgment of your own except where this prompt names one. Work in `Build/Ministry/Operations/Audits/2026-11-19_batch-6/`.

## What governs
1. Each folder's `Card_Check.md` gives exact JSON fixes and scan readings.
2. `Batch_Originals_Ruling.md` governs every non-English `original` or `printed` wording. Where it says LEAVE OUT, remove that entry's `original`, `originalFile` and `originalLines` (or, where the original was the `printed` wording, make the English the `printed` wording as the ruling says). Do not add that entry's scan readings. Where it says KEEP, apply that entry's readings. Its "sources that differ" section gives `uncertain` notes: add each word for word.
3. The coordinator's two calls: keep Pliny's "O sententiam" with its reading, as the ruling did; for Tatian Q3, leave the Greek out and add no Latin in its place.
4. Mark's guidance (Decision-Log, "Batch 6: where sources disagree", 2026-11-19): where two held sources differ, the card credits both. Apply it only where a check or the ruling gives the wording.

## Do
1. For each of the thirteen folders, apply every FIX in `Card_Check.md` to `<slug>.card.json`, word for word, as the ruling above amends it. Keep the JSON valid, with the key order the card already has.
2. Add every kept scan reading to `tools/quote_scan_readings.json` (repository root), in the file's own format (`file`, `lines`, `scan`, `reads`, `kind`, and `drop` with `lines_held` where a check gives it). Add each once.
3. Two story fixes, each word for word:
   - In `irenaeus-of-lyon/irenaeus-of-lyon.brief.txt`, apply FIX 7 from `irenaeus-of-lyon/Card_Check.md`, and its matching card changes (`uncertain[8]`, `briefReferences[8]`).
   - In `ignatius-of-antioch/ignatius-of-antioch.brief.txt`, replace `Polycarp, writing soon after to the church at Philippi, which Paul had once written to, asked for news of "the blessed Ignatius".` with the replacement in `Batch_Originals_Ruling.md`, Part 2. Then make the card's `quotationOriginals` and `briefReferences` match the brief's quoted spans and what it tells.
   - Run `python -m engine.m1.profile_readability <brief>` on both. Each must pass.
4. Write `Card_Apply.md` in the batch folder: for each folder, each change made (file, field, old → new), each reading added, and anything you could not apply, with the reason.

Do not run `tools/validate-census.mjs` and do not edit the census. Use no scratch file. Do not commit. Reply in under 200 words.
