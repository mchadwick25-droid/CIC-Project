# Batch 5 card fix prompt

You apply the card checks for the folders you are given, under `Build/Ministry/Operations/Audits/2026-11-18_batch-5/`. You did not write or check these cards.

For each folder, read `Card_Check.md`, `<slug>.card.json` and `Card_Edits.md`.

1. Apply every FIX in `Card_Check.md` to `<slug>.card.json`, **word for word** as the checker gives it (field, old text, new text). Change nothing else. Keep the JSON valid, two-space indented, UTF-8, ending in a newline.
2. A FIX that is not exact text, or that cannot be applied as written (the old text is not there, or two fixes collide), is not guessed: list it under **Not applied** with the reason.
3. Scan readings for `tools/quote_scan_readings.json` are **not** added by you. Copy every reading the check gives, verbatim, into `Build/Ministry/Operations/Audits/2026-11-18_batch-5/<slug>/Scan_Readings.json` as a JSON array (only for folders that have any). A reading the checker marks as needing a page image is copied with a `"hold": "<the checker's reason>"` key.
4. Append to `Card_Check.md` a section "Applied (card fixer)": each FIX applied, and each not applied with its reason.

Do not edit any brief, outline or source sheet, or any file outside those folders. Do not run `tools/validate-census.mjs`. Use no scratch or temporary file of any kind. Do not commit. Reply in under 80 words per folder.
