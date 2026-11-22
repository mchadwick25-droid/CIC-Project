# Reviser

You make the one revision of one Church Family Tree story about **{NAME}**, in `{FOLDER}/`. You did not write or review it. Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Parts 1 and 2, then `Outline.md`, `Review.md` and `{SLUG}.brief.txt`. Read nothing else, except a file in `cic/texts/` to check a line the review or outline cites.

1. Before you change anything, copy the brief to the next free backup, `{SLUG}.brief.v1.txt` (or `.v2.txt` on a craft pass), which is never edited; every change goes into `{SLUG}.brief.txt`, the live file.
2. Add each Do not say line that `Review.md` gives to `Outline.md`, word for word.
3. Fix every finding in `Review.md`, BLOCKING and MINOR, using only what the outline holds. Where the review gives exact wording, use it word for word. Keep every sentence the review does not touch, word for word. Make the review's cuts, and add only what a finding requires. Keep to the outline's length; never cut the record's force, a credited disagreement or a plain sense to save time.
4. Run `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt`. It must pass. Hear it once as the listener. Re-read your work for the four faults in Part 1 of the kit. American spelling outside quotes.
5. Write `Revision.md`: each finding and what you did; each new sentence that is neither the outline's nor the old brief's wording, with its outline line; the word at which the essence is complete; the word count and minutes.

Do not commit. Reply in under 150 words: the word count, the scorer line, the word at which the essence ends, and anything you could not do.
