# Card check: John Calvin

**Verdict: FIX** (three source authors, two spellings, two references).

New card: no starting card, so step 2 does not apply. Each field was checked against its evidence in `Card_Edits.md` and against the entry's own fields.

## 1. Fields against their evidence

Each field checks against its evidence. Re-read:
- K 28822-28825, 28898-28900, 29970-29995, 29999-30009, 31846-31852, 32259-32264, 32317-32322, 32444-32452, 34795-34800, 35675-35680, 35736-35745, 35787-35789, 36325-36330, 36421-36430, 36509-36515.
- INST1 370-381, 1691-1699, 5835-5838. INST2 24550-24558.
- L1 2250-2266. L2 1779-1783, 19431-19436. L4 17138-17142, 17219-17223.
- HOOK 4653-4669. PET 1206-1211. KIRK 14515-14525.

No field contradicts the entry's `sourcing`, `voices`, `legacy`, `why`, `relationsSummary`, `dates` or `placeLabel`. The card writer's notes on `dates` (Geneva's years) and on `legacy` (the 1672 synod and Voetius) are fair.

## 2. Nothing else moved

Does not apply: there is no starting card.

## 3. References

Rule applied: remove what the brief does not tell, but keep a date that grounds one of the brief's dates. Kept on that ground:
- "about twenty-one years after", which grounds "twenty years later".
- January 1555, which grounds "In 1555, the year Geneva's councils confirmed the consistory's rules".
- 27 May 1564, which grounds "He died that May".

FIX 1. `briefReferences[1]`. The brief does not name Basel.
- Old: `born in France, he left it to hide in a quiet corner; at Basel believers burned in France were slandered as rebels; he wrote a short handbook to clear their name.`
- New: `born in France, he left it to hide in a quiet corner; believers burned in France were slandered as rebels; he wrote a short handbook to clear their name.`
- (The entry's opening, up to "born in France", is unchanged.)

FIX 2. `briefReferences[5]`. The brief does not tell the General Council's vote of 20 November 1541.
- Old: `... the weekly meeting with the pastors; the councils keep the last word on punishment. The General Council passes the text on 20 November 1541.`
- New: `... the weekly meeting with the pastors; the councils keep the last word on punishment.`

All other references name what the brief tells.

## 4. Census rules

FIX, for three sources and two spellings.
- Only allowed keys, and no `briefLength`.
- There are three quoted spans in the brief and three entries, with none left over.
- Each `printed` stands at its lines with no scan reading needed: K 29989-29995, INST2 24555-24557, K 35741-35745. "arque- / bute" is Kidd's period form, joined by the line-end hyphen rule, and not a scan fault.
- Every cited file is in `sources`.
- There are no quotation marks in the references.
- No audit, review or ruling is named.

FIX 3. `sources.about[1]`, `sources.about[4]`, `sources.about[5]`. The census check requires an `about` source to carry `author`, as a name or `null` for a work with no named author. These three have no `author` key and will fail. Add `"author": null` after `title` in each:
- "Calvini Opera, volume 8: the trial of Servetus".
- "The Book of the Universal Kirk of Scotland, 1560 to 1602".
- "Book of Common Order and Westminster Directory".

FIX 4. `keyWorks[1].about`. "councillors" is British spelling.
- Old: `drafted by Calvin and his colleagues with six councillors;`
- New: `drafted by Calvin and his colleagues with six councilors;`

FIX 5. `legacy.remembered[1]`. "mould" is British spelling, and this is a paraphrase, not Hooker's verbatim wording.
- Old: `were cast in the mould Calvin had made.`
- New: `were cast in the mold Calvin had made.`

None of the three entries has a `secondReading` yet. That is expected at step 7.

## 5. Originals

Pass.
- Q1 is Calvin's Latin, the held original. No English printing of the preface is held.
- Q2 is Beveridge's English. The outline says the Latin of 1559 is not held. A search of `cic/texts/` for the passage's Latin found nothing.
- Q3 is the French as Pinant took it down.

## 6. Not found, and left in

The edit list names no claim as not found. Nothing clearly wrong is on the card.

Note, not a fix: `uncertain[9]` opens "Verdicts by B. J. Kidd that Library notes carry as the editor's, not as sources". That speaks of the build's notes rather than the sources. A reader may stumble on it, but it names no audit or review.

## Applied (card fixer)

FIX 1 applied (briefReferences[1]).
FIX 2 applied (briefReferences[5]). The old text was given with a leading "..."; the replacement was applied to the exact text after it.
FIX 3 applied ("author": null added after title in sources.about[1], [4], [5]).
FIX 4 applied (keyWorks[1].about).
FIX 5 applied (legacy.remembered[1]).
Not applied: none.
