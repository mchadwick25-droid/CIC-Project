# Batch 10, the modern pass: apply the card checks

Story folder: `Build/Ministry/Operations/Audits/2026-11-22_batch-10/{SLUG}/`. Mechanical work only: write no wording of your own.

1. Read `Card_Check_Modern.md`. Apply every change it gives to `{SLUG}.card.json` exactly as worded: the field, the old text, the new text. Each old text must stand once in its field; if it does not, change nothing for it and report it. An added entry (old: none) goes where the check says. Keep the file valid JSON with its existing formatting (edit by exact string replacement, never by re-dumping the whole file). {EXTRA}
2. Run `node tools/validate-census.mjs --skip-quotes` against a scratch copy of `cic-website/data/world-census.json` in `/tmp/claude-0/-home-user-CIC-Project/30f7ff74-3ed4-5f83-9127-e384c2ec4ddf/scratchpad/apply/{SLUG}/` with this card in place (and `{SLUG}.brief.txt` as its `longDescription`), and report its errors for this entry.
3. Write `Card_Check_Modern_Applied.md` in the folder as a JSON list, one object per change: `{"field": ..., "old": ..., "new": ...}` exactly as applied (use `"old": null` for an added entry), then a line with the validator result.

Do not edit the brief, the census or any other folder, and do not commit. Reply in under 60 words: changes applied, not applied, validator errors.
