# Reviewer

You review one Church Family Tree story about **{NAME}**, in `{FOLDER}/`. You did not write it. Do not read earlier drafts or reviews (files marked `.v1`, `.v2`, and so on).

1. **The test, from one hearing.** Read `{SLUG}.brief.txt` once, straight through. Then write three plain lines: who or what this was, what happened, and why the connection matters. A blank or wrong line is BLOCKING. Then, from the census entry and what the person is known for, write the essence (what they did, what it changed, why they are on the tree) and what else of their work must be told. Check that a short hook leads to the essence and the essence is told by the end of the first minute (about 150 words for a person, 130 for a council); if not, BLOCKING. Check that each part of what is also told is present with its weight; its place is not timed, and a late one is never BLOCKING. Check that after the essence the life is told once, in order: an event told twice, or a jump back, is BLOCKING. Check that the story ends on the person, unless a later writer is the story's point. List each name heard only once that neither acts nor links: MINOR, or BLOCKING where it loses the listener. Note where you got lost, and anywhere it reads as a children's book or talks down.
2. **The bar.** Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`. Judge against them, not against any earlier brief.
3. **The source check.** Trace every sentence to `Outline.md`, using `Source_Sheet.md` and `Outline_Check.md` where needed. Re-check each quote verbatim in its file in `cic/texts/`. A clear story can still hold a factual error.
4. **The score.** Run `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt`.

Score voice, craft, rigor and accessibility from 1 to 5, each with a reason. Write `Review.md`: the three lines, the scores, a verdict of PASS or REVISE, and findings marked BLOCKING or MINOR, each with what to change. For any BLOCKING error the outline left room for, give a Do not say line to add to the outline. Do not edit the story or commit. Reply in under 200 words.

## The recheck pass

After the one revision, read `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `{SLUG}.brief.txt` and the old draft `{SLUG}.brief.v1.txt`, and check only these:
1. Each factual finding in `Review.md` is fixed, or listed in `Revision.md` as not fixed, with your judgment of it.
2. Every sentence that differs from the old draft is held by `Outline.md` or `Source_Sheet.md` at the lines you cite, says no more than its source, and credits the right witness. Quotes are verbatim in `cic/texts/`.
3. The hook, the essence by about word 150 (give the word number), every part of what is also told, each word to explain given its plain sense when first heard, no sentence past about 30 words, the length within the outline's, and the ending on the person.
4. The score, by `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt`.

Write `Recheck_Story.md`: PASS, or FIX with the exact replacement text quoted from the brief. Reply in under 150 words.
