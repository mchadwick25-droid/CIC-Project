# Batch 6 card prompt

Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/card.md` and follow it for **{NAME}** in `{FOLDER}/` (slug `{SLUG}`). Add these points:

- **The existing card** is the census's current card for `{SLUG}` in `cic-website/data/world-census.json` (its `card` object, or its `council` object for a council). The folder copy `Card.existing.json` is the same object; read either. Write your result to `{FOLDER}/{SLUG}.card.json`.
- **Second readings.** For a quoted span whose modern wording and source are unchanged from the census card's entry, copy that entry's `secondReading`. For a new or changed span, leave `secondReading` out. The second-reading step fills it in, and `Card_Edits.md` lists these spans as "awaiting second reading".
- Use no shared, scratch or temporary file of any kind, and do not run `tools/validate-census.mjs`.
