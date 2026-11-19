# Batch 5 reshape review prompt (targeted)

You review one reshaped Church Family Tree story about **{NAME}** in `{FOLDER}/` (slug `{SLUG}`). You did not write, reshape or review it before. Read `CLAUDE.md` ("Trust and source fidelity"), Parts 1 and 2 of `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, and Mark's rulings in `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md` (entry "Batch 5 hearts…", 2026-11-18, items 1–10; item 10 is the length ruling and this story's target).

Read `{SLUG}.brief.txt` once, straight through, as a listener; then write who this was, what happened, and why the connection matters (a blank or wrong line is BLOCKING). Then read `{SLUG}.brief.v2.txt` (the checked longer version), `Reshape.md`, `Outline.md`, and this story's entry in `Hearts_Plain.md` (the heart Mark approved; later fixes may have narrowed a wording, and the outline governs).

Check only these:
1. **Nothing essential lost.** For each item `Reshape.md` lists as dropped: is it part of the approved heart, the record's force or conflict, or the connection? If so, BLOCKING, with the shortest restoration (sentences from v2, word for word where possible). Secondary episodes rightly dropped are fine.
2. **New wording.** Every sentence not in v2: held by the outline at the line you cite, saying no more than it, with the right witness.
3. **The kit.** Hook about three sentences; essence complete by about word 150 (give the word); the life once, in order; every church word kept gets its plain sense the first time it is heard; no sentence past about 30 words; ending on the person; quotes unchanged from v2 (a dropped quote is fine).
4. **Flow.** Does it flow as one told story, or does it read clipped? Name any join that jars, with a fix.
5. **Length.** Give the minutes at 150 a minute against the target. Name anything still not needed.
6. Run `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt`.

Write `{FOLDER}/Reshape_Review.md`: the three lines, PASS or FIX, and each finding marked BLOCKING or MINOR with the exact replacement text quoted from the brief. Edit nothing else; no scratch or temporary files; do not commit. Reply in under 150 words.
