# Blind scoring, reader Y

You score six Church Family Tree stories, one at a time, in this order: S02, S06, R1, S08, S03, R2. Each is a folder in `Build/Ministry/Operations/Audits/2026-11-23_blind-cross-batch/` holding `story.txt` (the story), `Outline.md` and `Source_Sheet.md`. You do not know who wrote them, when, or how they have been scored before, and you must not try to find out: read nothing in the repository except those six folders, `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, `CLAUDE.md`, and files in `cic/texts/` that an outline or source sheet cites. Do not read the census, any other folder under `Build/Ministry/`, git history, or any `Scores.md`.

For each story, do the reviewer's steps 1 to 4 below, as written, with these readings: the story file is `story.txt`; "the census entry and what the person is known for" means the outline and what the person is known for; skip anything that refers to a batch or to earlier drafts. Hold every story to the same bar; do not grade on a curve across the six.

Write `Build/Ministry/Operations/Audits/2026-11-23_blind-cross-batch/Reader_Y.md`: for each story, its id, the three lines, the four scores (voice, craft, rigor, accessibility, each 1 to 5) with a one-line reason each, and its BLOCKING findings if any (one line each). End with a table: id, voice, craft, rigor, accessibility. Edit nothing else; do not commit. Reply with the table only.

---

# Reviewer

You review one Church Family Tree story about **each story**, in `Build/Ministry/Operations/Audits/2026-11-23_blind-cross-batch/<id>/`. You did not write it. Do not read earlier drafts or reviews (files marked `.v1`, `.v2`, and so on).

1. **The test, from one hearing.** Read `story.txt` once, straight through. Then write three plain lines: who or what this was, what happened, and why the connection matters. A blank or wrong line is BLOCKING. Then, from the census entry and what the person is known for, write the essence (what they did, what it changed, why they are on the tree) and what else of their work must be told. Check that a short hook leads to the essence and the essence is told by the end of the first minute (about 150 words for a person, 130 for a council); if not, BLOCKING. Check that each part of what is also told is present with its weight; its place is not timed, and a late one is never BLOCKING. Check that after the essence the life is told once, in order: an event told twice, or a jump back, is BLOCKING. Check that the story ends on the person, unless a later writer is the story's point. List each name heard only once that neither acts nor links: MINOR, or BLOCKING where it loses the listener. Note where you got lost, and anywhere it reads as a children's book or talks down.
2. **The bar.** Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`. Judge against them, not against any earlier brief.
3. **The source check.** Trace every sentence to `Outline.md`, using `Source_Sheet.md` and `Outline_Check.md` where needed. Re-check each quote verbatim in its file in `cic/texts/`. A clear story can still hold a factual error.
4. **The score.** Run `python -m engine.m1.profile_readability Build/Ministry/Operations/Audits/2026-11-23_blind-cross-batch/<id>/story.txt`.

Score voice, craft, rigor and accessibility from 1 to 5, each with a reason. Write `Review.md`: the three lines, the scores, a verdict of PASS or REVISE, and findings marked BLOCKING or MINOR, each with what to change. For any BLOCKING error the outline left room for, give a Do not say line to add to the outline. Do not edit the story or commit. Reply in under 200 words.
