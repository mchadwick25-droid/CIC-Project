# Batch 7: apply the card checks and the originals ruling

You apply fixes that others have already worded. You make no judgment of your own. Work in `Build/Ministry/Operations/Audits/2026-11-20_batch-7/`.

## What governs
1. Each folder's `Card_Check.md` gives exact JSON fixes and scan readings.
2. `Batch_Originals_Ruling.md` (this folder) governs every non-English `original` or `printed` wording and the coordinator's calls.
3. Where two held sources differ, the card credits both (Mark, 2026-11-19). Apply it only where a check gives the wording.

## Do
1. For each of the thirteen folders (tertullian-s-voice, cyprian-of-carthage, pontius-the-deacon, novatian, councils-of-rome-and-carthage-251, pamphilus-of-caesarea, eusebius-of-caesarea, dionysius-of-alexandria, peter-of-alexandria, anatolius-of-alexandria-and-laodicea, lactantius, origen, methodius-of-olympus), apply every FIX in `Card_Check.md` to `<slug>.card.json`, word for word, as the ruling amends it. Keep the JSON valid, with the key order the card already has.
2. Add every kept scan reading to `tools/quote_scan_readings.json` (repository root), in the file's own format. Add each once.
3. Write `Card_Apply.md` in the batch folder: for each folder, each change made (field, old → new), each reading added, and anything you could not apply, with the reason.

Do not edit any brief. Do not run `tools/validate-census.mjs` and do not edit the census. Use no scratch file. Do not commit. Reply in under 200 words.
