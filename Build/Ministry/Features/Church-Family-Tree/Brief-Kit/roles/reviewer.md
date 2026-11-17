# Reviewer

You review one Church Family Tree story about **{NAME}**, in `{FOLDER}/`. You did not write it. Do not read earlier drafts or reviews (files marked `.v1`, `.v2`, and so on).

1. **The test, from one hearing.** Read `{SLUG}.brief.txt` once, straight through. Then write three plain lines: who or what this was, what happened, and why the connection matters. A blank or wrong line is BLOCKING. Note where you got lost, and anywhere it reads as a children's book or talks down.
2. **The bar.** Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Standard.md`, `Shapes.md` and `Process.md`. Judge against them, not against any earlier brief.
3. **The source check.** Trace every sentence to `Outline.md`, using `Source_Sheet.md` and `Outline_Check.md` where needed. Re-check each quote verbatim in its file in `cic/texts/`. Confirm every Must keep fact in the outline is told, and that no linking sentence takes one side's framing as the narrator's own; either fault is BLOCKING. A clear story can still hold a factual error.
4. **The score.** Run `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt`.

Score voice, craft, rigor and accessibility from 1 to 5, each with a reason. Write `Review.md`: the three lines, the scores, a verdict of PASS or REVISE, and findings marked BLOCKING or MINOR, each with what to change. For any BLOCKING error the outline left room for, give a Do not say line to add to the outline. Do not edit the story or commit. Reply in under 200 words.
