# Batch header

- **Story:** John Chrysostom (census id `john-chrysostom`). **Folder:** `Build/Ministry/Operations/Audits/2026-11-22_batch-10/john-chrysostom/`. **Card file:** `Build/Ministry/Operations/Audits/2026-11-22_batch-10/john-chrysostom/Card.existing.json`.
- **Job on the slate (Mark, 2026-11-23, "Batch 10: the slate approved"):** approved before the kit, live and recorded; reviewed here, not researched again, under the change order of 2026-11-19: "approved wording is kept wherever it passes; a fix touches only what fails." `john-chrysostom.brief.approved.txt` is the live text; `john-chrysostom.brief.txt` is the same text, under review.
- **No outline.** There is no `Outline.md` or `Source_Sheet.md`. Trace the story to `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/` (`drafts/john-chrysostom.refs.md`, `reviews/`, `renderings/`), `Build/Ministry/Operations/Audits/2026-11-11_person-brief-pilot/final/`, the card's `quotationOriginals`, and `cic/texts/`. There is no approved heart on `Hearts.md`: take the essence from the census entry and the story itself.
- **Siblings and links in this batch:** `john-cassian`, `theodoret-of-cyrrhus` (links). Live: `epiphanius-of-salamis` (tells their clash). Check its quotes against this batch's drafts (`Build/Ministry/Operations/Audits/2026-11-22_batch-10/*/*.brief.txt`) for overlap; its own quotes stay with it.
- **Findings:** every finding names the exact words to change and the smallest replacement; do not propose rewrites of passing text. A change in text means it is re-recorded, so block only for the bar's reasons. It is about 358 words; it is not lengthened.

---

# Reviewer

You review one Church Family Tree story about **John Chrysostom**, in `Build/Ministry/Operations/Audits/2026-11-22_batch-10/john-chrysostom/`. You did not write it. Do not read earlier drafts or reviews (files marked `.v1`, `.v2`, and so on).

1. **The test, from one hearing.** Read `john-chrysostom.brief.txt` once, straight through. Then write three plain lines: who or what this was, what happened, and why the connection matters. A blank or wrong line is BLOCKING. Then, from the census entry and what the person is known for, write the essence (what they did, what it changed, why they are on the tree) and what else of their work must be told. Check that a short hook leads to the essence and the essence is told by the end of the first minute (about 150 words for a person, 130 for a council); if not, BLOCKING. Check that each part of what is also told is present with its weight; its place is not timed, and a late one is never BLOCKING. Check that after the essence the life is told once, in order: an event told twice, or a jump back, is BLOCKING. Check that the story ends on the person, unless a later writer is the story's point. List each name heard only once that neither acts nor links: MINOR, or BLOCKING where it loses the listener. Note where you got lost, and anywhere it reads as a children's book or talks down.
2. **The bar.** Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`. Judge against them, not against any earlier brief.
3. **The source check.** Trace every sentence to `Outline.md`, using `Source_Sheet.md` and `Outline_Check.md` where needed. Re-check each quote verbatim in its file in `cic/texts/`. A clear story can still hold a factual error.
4. **The score.** Run `python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-22_batch-10/john-chrysostom/john-chrysostom.brief.txt`.

Score voice, craft, rigor and accessibility from 1 to 5, each with a reason. Write `Review.md`: the three lines, the scores, a verdict of PASS or REVISE, and findings marked BLOCKING or MINOR, each with what to change. For any BLOCKING error the outline left room for, give a Do not say line to add to the outline. Do not edit the story or commit. Reply in under 200 words.
