# Batch 4 story recheck prompt (the one recheck)

You are an independent checker. You did not write, review or revise these stories. Read `CLAUDE.md` ("Trust and source fidelity") and `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Standard.md` as it now stands. For each folder you are given, read `Review.md`, `Revision.md`, `Outline.md` (with its Essence and Also told fields), `Source_Sheet.md`, `<slug>.brief.txt`, and the old draft `<slug>.brief.v1.txt`.

Check only these:
1. **Review findings.** Each factual finding in `Review.md` is fixed. Ignore findings that only asked for an Also told part to come earlier; those were superseded.
2. **New wording.** Every sentence listed in `Revision.md` as new, and any other sentence that differs from v1, must be held by `Outline.md` or `Source_Sheet.md` at the lines you cite. Check it says no more than its source, with the right witness. Quotes must be verbatim in `cic/texts/`.
3. **The kit lines.** The hook is no more than about three sentences. The Essence is complete by about word 150 (130 for the council): give the word number. Every Also told part is present. The setting is not stacked in one sentence. The story ends on the person, unless a later writer is the story's point.
4. **Score.** Run `python -m engine.m1.profile_readability <folder>/<slug>.brief.txt`.

Do not raise new "could be stronger" points. For each folder, write `Recheck_Story.md` with a verdict of PASS or FIX. Each FIX must give the exact replacement text, quoted from the brief. Write nothing else, use no shared or scratch file, and do not commit. Reply in under 150 words per folder.
