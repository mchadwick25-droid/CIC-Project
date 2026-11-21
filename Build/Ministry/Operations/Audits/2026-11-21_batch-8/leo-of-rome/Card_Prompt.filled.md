# Batch 8 card prompt

Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/card.md` and follow it for **Leo of Rome** in `Build/Ministry/Operations/Audits/2026-11-21_batch-8/leo-of-rome/` (slug `leo-of-rome`). Add these points:

- **The existing card** is the census's current card for `leo-of-rome` in `cic-website/data/world-census.json` (its `card` object, or its `council` object for a council). The folder copy `Card.existing.json` is the same object; read either. Write your result to `Build/Ministry/Operations/Audits/2026-11-21_batch-8/leo-of-rome/leo-of-rome.card.json`.
- **Second readings.** For a quoted span whose modern wording and source are unchanged from the census card's entry, copy that entry's `secondReading`. For a new or changed span of six words or more, leave `secondReading` out; give a shorter one `"checked at card"`, as the role says. The second-reading step fills it in, and `Card_Edits.md` lists these spans as "awaiting second reading".
- Use no shared, scratch or temporary file of any kind, and do not run `tools/validate-census.mjs`.
- **Where held sources differ**, the card credits each (Mark, 2026-11-19). Carry onto the card what the review, recheck or outline sent there (look for "for the card", "the card should" and "For the card, not the story" in `Outline.md`, `Review.md` and `Recheck_Story.md`).
- **Originals.** A quote whose original is held only in a damaged scan is printed in English alone on the card unless a held print confirms the reading (`Build/Ministry/Operations/Audits/2026-11-19_batch-6/Batch_Originals_Ruling.md`). Greek is checked by hand as well as by the census check.
- For Constantine, the research is in `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/` (`drafts/leo-of-rome.refs.md`, `quotation-originals.json`); there is no Outline.md.
