# Batch 5 story recheck prompt (the one recheck)

You are an independent checker. You did not write, review or revise these stories. Read `CLAUDE.md` ("Trust and source fidelity") and Parts 1 and 2 of `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md`, and the Decision-Log entry "Batch 5 hearts: church words explained, and Luther's job re-set" (2026-11-18) in `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md`. For each folder you are given, read `Review.md`, `Revision.md`, `Outline.md`, `Source_Sheet.md`, `<slug>.brief.txt`, and the old draft `<slug>.brief.v1.txt`.

Check only these:
1. **Review findings.** Each factual finding in `Review.md` is fixed. A finding the reviser could not fix is listed in `Revision.md`; judge it.
2. **New wording.** Every sentence listed in `Revision.md` as new, and any other sentence that differs from v1, must be held by `Outline.md` or `Source_Sheet.md` at the lines you cite. Check it says no more than its source, with the right witness. Quotes must be verbatim in `cic/texts/`.
3. **The kit lines.** The hook is no more than about three sentences. The essence is complete by about word 150: give the word number. Every "also told" part is present. Every church word in the outline's "Words to explain" list that the story uses gets its plain sense the first time it is heard. No sentence runs past about 30 words. Length follows Mark's ruling 8: no ceiling; list only what the story does not need. The setting is not stacked in one sentence. The story ends on the person, unless a later writer is the story's point.
4. **Score.** Run `python -m engine.m1.profile_readability <folder>/<slug>.brief.txt`.

Do not raise new "could be stronger" points. For each folder, write `Recheck_Story.md` with a verdict of PASS or FIX. Each FIX must give the exact replacement text, quoted from the brief. Write nothing else, use no shared, scratch or temporary file of any kind, and do not commit. Reply in under 150 words per folder.
