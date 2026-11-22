# Card check: Gregory of Nyssa (batch 9)

Read: `CLAUDE.md` (Trust and source fidelity), the card role, `gregory-of-nyssa.brief.txt` (with the recheck's "Gregory also wrote" applied), `gregory-of-nyssa.card.json`, `Card_Edits.md`, `Card.existing.json`, `Review.md`, `Revision.md` and `Recheck_Story.md`. No census entry is written (the person has one).

## Verdict: PASS

## The checks

1. **Edits against evidence.**
   - **Edit 1** (Great Catechism 26) is held at npnf205 44413-44418: "after long periods of time ... restoration of those who are now lying in Sin ... purgation have suffered chastisement". It is also held at 44405 ("the separation is agonizing") and 44425-44427 ("healing even the introducer of evil himself ... the chastisement, however painful"). The same passage names "the adversary" at 44406.
   - **Edit 2** (Life of Macrina) is held. The Clarke file, line 2, reads "Creator: Gregory of Nyssa". Line 58 reads "Gregory's account of his sister's life". The edit does not say "the only life".
   - **Edit 3** (On the Soul and the Resurrection) is held at npnf205 38087-38099: Basil had died, Gregory "journeyed to her", and she was "lying in a state of prostration even unto death" and "tried to check me by speaking".
   - **Edit 4** (XII to II) is held. Lines 8957-8958 fall after "Book II." at 8727 and before "Book III." at 11996. Book XII starts at 21359.
   - **Edit 5** removes quotation marks around printed wording that is not verbatim in the brief, with the words unchanged, as the role requires.
2. **Nothing else moved.** A JSON diff of `Card.existing.json` against the card shows only the listed changes. `Card.existing.json` equals the census card.
3. **`briefReferences`.** Every entry names something the revised brief still tells. The sentence the revision cut ("The sources we have do not show ...") had no reference. None is to be removed.
4. **Census rules.**
   - The keys are allowed, and there is no `briefLength`.
   - The brief has three quoted spans and the card has three entries, matching word for word.
   - Each `printed` is verbatim: npnf205 2788, 8957-8958 and 27944.
   - The cited file is in `sources`. No audit file is named, and the spelling is American.
   - The card passes `tools/validate-census.mjs`, run on a scratch copy of the census: 0 errors. There is no outline, so no rendering from a held original is owed.
5. **Short quotations.** Two spans are under six words: "inherited the controversy with Eunomius." (five words) and "is above every name." (four words).
   - Each keeps the verdict of a real blind reading made earlier (`2026-11-16_eight-standard-v1/renderings/eight/comparison.md`): Q15 "minor", Q16 "same". The change order of 2026-11-21 reopens no finished reading, and the validator accepts these verdicts at any length. Both stand.
   - Against the print, "is above every name." is identical to 8957-8958.
   - "inherited the controversy with Eunomius." renders "I received the legacy of Eunomius' controversy" (2788). Its `uncertain` note carries the one point where the English could be read two ways.
   - No Greek original is held at either passage, so the card rightly prints the English alone.
6. **Not found, and left in.** The writer lists none. I found nothing clearly wrong left in.
7. **Census entry:** none written, so there is nothing to check.

Outside this check's remit, and not a change: `sources.about` does not list Socrates (npnf202), Basil's letters (npnf208) or the Codex Theodosianus, although `briefReferences` cite them. This was so in the existing card already, and no new card claim rests on them.
