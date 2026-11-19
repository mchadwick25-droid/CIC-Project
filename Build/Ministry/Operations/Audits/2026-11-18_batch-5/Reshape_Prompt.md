# Batch 5 reshape prompt (Mark's length ruling, Decision-Log item 10)

You reshape one finished Church Family Tree story about **{NAME}** in `{FOLDER}/` (slug `{SLUG}`) to about **{TARGET}**, at 150 words a minute. You did not write or review it.

Mark: "i did want them closer to 3 minutes with the most robust pushing 4 or a little more, but 5:30 is beyond what studys say people will stay engaged for", and earlier, "we do not cut to meet a hard ceiling, that always leaves it not flowing". So reshape the story; do not clip it. Choose fewer beats and tell those well, rather than squeezing every beat.

## Read
- `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Parts 1 and 2.
- `{FOLDER}/{SLUG}.brief.txt` (the checked story), `{FOLDER}/Outline.md` (its source of truth), and `{FOLDER}/Review.md` and `{FOLDER}/Recheck_Story.md` (what the checks fixed: keep every fix).
Read nothing else in the repository. Use no scratch or temporary file of any kind.

## Do
1. Copy the current brief to `{SLUG}.brief.v2.txt` before changing anything.
2. Rewrite `{SLUG}.brief.txt` to about {TARGET}. Keep: a short hook; the essence complete by about word 150; the life told once, in order; the record's force and conflict (never softened by leaving it out); the connection; an ending on the person; every church word that stays gets its plain sense the first time it is heard. Drop secondary episodes, side names and the words that only served them. Prefer keeping the checked sentences word for word; any sentence you change or write must say no more than the outline holds.
3. Quotes: use only the outline's quotes, word for word, as the current brief has them (ellipses included). You may drop a quote; do not change one or add one.
4. Run `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt`; it must pass. Hear it once as the listener. Check for the four faults: one witness told as fact, an editor's view given to the source, a detail moved onto the wrong event, force softened.
5. Write `{FOLDER}/Reshape.md`: the new word count and minutes; each beat or passage dropped, in one line; each quote dropped; every sentence that is neither the old brief's nor the outline's wording, with its outline line; where the essence ends.

Do not commit. Reply in under 120 words: the word count, the scorer line, and what was dropped.
