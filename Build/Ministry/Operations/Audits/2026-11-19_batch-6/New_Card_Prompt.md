# Batch 6 new-card prompt (Polycarp of Smyrna)

Mark's ruling (Decision-Log, "Batch 6: era 1 first…", 2026-11-19, item 5): Polycarp's approved text goes live word for word with a new card, checked. The census entry has no `card`. You build a full one for **{NAME}** (slug `{SLUG}`) in `{FOLDER}/`.

## Read
- `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/card.md`, for the rules a card keeps (live surface, census keys, American spelling, no audit names, quotation originals, second readings). Its "keep the existing card word for word" does not apply: there is none.
- The format: `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/benedict-of-nursia.card.json`, and one batch 5 card built from an existing one, `Build/Ministry/Operations/Audits/2026-11-18_batch-5/babai-the-great/babai-the-great.card.json`.
- `tools/validate-census.mjs`, only to learn which card keys it allows. Do not run it.
- In your folder: `{SLUG}.brief.txt` (the approved story, which is not changed). Its research is in `Build/Ministry/Operations/Audits/2026-11-16_polycarp-clean-write/`: `Source_Sheet.md`, `Writer_Sheet.md`, `Polycarp_final.references.md` and `Polycarp_B2_source_check.md`. Mark ruled on 2026-11-16 that the source check's cautions go on the card, under `uncertain`.
- The census entry `{SLUG}`'s own fields other than `longDescription` (`sourcing`, `voices`, `legacy`, `why`, `floorNote`, `relationsSummary`, `dates`, `placeLabel`). These stay as they are; the card must not contradict them, and where it would, list the conflict.

## Do
1. Write `{FOLDER}/{SLUG}.card.json`: every field the other cards carry that the sources hold (other names, known for, dates and place notes, role, key works, sources, uncertain points, brief references, quotations with `quotationOriginals`). Every claim comes from the source sheet or outline at a cited line, or from the finished brief. Each quotation's modern rendering is exactly the brief's; its original is verbatim from its file and lines. Leave every `secondReading` out; the second-reading step fills them. Leave connections to other entries out.
2. Write `{FOLDER}/Card_Edits.md`: since everything is new, list each field with its evidence (file and lines, or the brief's sentence), each quoted span as "awaiting second reading", and any conflict with the entry's existing fields.

Re-read each cited line in its file. Never invent. Use no shared, scratch or temporary file of any kind. Edit nothing else; do not commit. Reply in under 120 words: the fields written, the quoted spans, and any conflict or claim not found.
