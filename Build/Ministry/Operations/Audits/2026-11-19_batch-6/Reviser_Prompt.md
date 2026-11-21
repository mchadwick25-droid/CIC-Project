# Batch 6 reviser prompt: the one revision

You revise one Church Family Tree story about **{NAME}** in `{FOLDER}/` (slug `{SLUG}`). This is its one revision under the kit (Part 4, step 5). You did not write or review it.

## Read
- `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, Parts 1 and 2.
- `{FOLDER}/Outline.md`, `{FOLDER}/Review.md` and `{FOLDER}/{SLUG}.brief.txt`.
- Mark's rulings for this batch: the Decision-Log entries of 2026-11-19 headed "Batch 6: …" and "Change order: the stories approved before the kit…", in `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`. Length is a pressure, not a cap (Mark, 2026-11-18, quoted below).

Read nothing else in the repository, except a file in `cic/texts/` to check a line the review or outline cites. Use no shared, scratch or temporary file of any kind.

## Do
1. **Keep a copy.** Before you change anything, copy the brief to `{SLUG}.brief.v1.txt`.
2. **The outline.** Add every Do not say line that `Review.md` gives to `Outline.md`, word for word.
3. **The brief.** Fix every finding in `Review.md`, BLOCKING and MINOR alike, using only what the outline holds. Where the review gives exact wording, use it word for word. Keep sentences the review does not touch, word for word. Keep to the kit: a short hook, the essence within the first minute, the life told once and in order, the setting a clause at a time, every word in the outline's "Words to explain" list given its plain sense the first time it is heard, no sentence past about 30 words, and an ending on the person.
4. **Length** (Mark, 2026-11-18): "we do not cut to meet a hard ceiling, that always leaves it not flowing, we want pressure to 3 minutes, but take what it needs". Make the review's listed cuts. Add only what a finding requires. Never cut the record's force or a plain sense to save time.
5. **Check it.** Run `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt`. It must pass. Hear it once as the listener. Check your own work for the four faults: one witness told as fact, an editor's view given to the source, a detail moved onto the wrong event, and force softened. American spelling outside quotes.
6. **Record it.** Write `{FOLDER}/Revision.md`: each review finding and what you did; every new sentence that is neither the outline's nor the old brief's wording, with its outline line; the word at which the essence is complete; the word count and minutes.

Do not commit. Reply in under 150 words: the word count, the scorer line, the word at which the essence ends, and anything you could not do.
