# Batch 4 reviser prompt: the one revision

You revise one Church Family Tree story about **{NAME}** in `{FOLDER}/` (slug `{SLUG}`). This is its one revision under the kit (Process.md, step 5).

## Read
- `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Standard.md` as it now stands, and `Shapes.md`. Both changed on 2026-11-18: a short hook, the essence early, the setting woven in, and an ending on the person.
- `{FOLDER}/Outline.md`, `{FOLDER}/Review.md` and `{FOLDER}/{SLUG}.brief.txt`.
- Your piece's entry in `Build/Ministry/Operations/Audits/2026-11-18_batch-4/Essences.md` (Mark approved it).

Read nothing else in the repository. Use no shared or scratch file.

## Do
1. **Keep a copy.** Before you change anything, copy the brief to `{SLUG}.brief.v1.txt`.
2. **The outline.** Add the outline's **Essence** and **Also told** fields, copied word for word from `Essences.md`. Add every Do not say line that `Review.md` gives, word for word.
3. **The brief.** Revise it to meet all of the following, using only what the outline holds:
   - The opening is a hook of no more than about three sentences, leading straight into the essence.
   - The essence is told by about word 150 for a person, or 130 for a council.
   - Each "also told" part is present, with its weight, wherever the story is strongest. A late one is fine.
   - The setting comes in a clause at a time, never stacked in one sentence.
   - The story ends on the person: a scene, their words, their death, or the opening image seen again. It ends on a later writer only if that is the story's point.
   - Every factual finding in `Review.md` is fixed: BLOCKING and MINOR alike.
   - A blocking finding that only asks for an "also told" part to come earlier no longer applies, and is to be ignored.
   - Keep approved sentences that are not affected, word for word.
   - Length is up to about 460 words for a person and 550 for a council, and craft comes before time. Never fill, and never cut the record's force.
   {EXTRA}
4. **Check it.** Run `python -m engine.m1.profile_readability {FOLDER}/{SLUG}.brief.txt`. It must pass. Then hear it once as the listener. Check your own work for the four faults: one witness told as fact, an editor's view given to the source, a detail moved onto the wrong event, and force softened. Use American spelling outside quotes.
5. **Record it.** Write `{FOLDER}/Revision.md`. List each review finding and what you did. List every new sentence you wrote that isn't the outline's or the old brief's wording, with its outline line. Give the word at which the essence is complete, and how the story opens and ends.

Do not commit. Reply in under 150 words: the word count, the scorer line, the word at which the essence ends, and anything you could not do.
