# Card check: John Wesley (new card)

Checker, 2026-11-18. I did not write this card. Read against `john-wesley.brief.txt` (and `.v1`, to see what the brief no longer tells), `Card_Edits.md`, `Outline.md`, `Source_Sheet.md`, the census entry's own fields and the cited lines in `cic/texts/`.

## Verdict: FIX (five brief references trimmed, one uncertain point)

### FIX 1: `briefReferences[2]`: the brief no longer tells the Oxford origin of the name

The v1 brief said "a nickname from his Oxford days"; the finished brief says only "a nickname at first".

- Old: `"Journal, 1739, his letter to the bishop of Bristol: ordained a priest and a Fellow of a College, he had no particular cure. The Character of a Methodist: the name was fixed on them by way of reproach, first given to three or four young men at Oxford."`
- New: `"Journal, 1739, his letter to the bishop of Bristol: ordained a priest and a Fellow of a College, he had no particular cure. The Character of a Methodist: the name was fixed on them by way of reproach."`

### FIX 2: `briefReferences[4]`: the brief does not tell the London classes

- Old: `"Journal, 15 February 1742, and A Plain Account: the Bristol society's debt, a penny a week, classes of about twelve each with one collector; the collectors report members not living as they should; the leader sees each member weekly; some turned from their ways and some were put away. Journal, 25 March 1742: the classes begin in London."`
- New: `"Journal, 15 February 1742, and A Plain Account: the Bristol society's debt, a penny a week, classes of about twelve each with one collector; the collectors report members not living as they should; the leader sees each member weekly; some turned from their ways and some were put away."`

### FIX 3: `briefReferences[5]`: the brief does not tell the waistcoat

The brief says only "He came back with a little skin off one hand."

- Old: `"... he came back having lost one flap of his waistcoat and a little skin from one hand. Journal, February 1744: James Jones's account of mobs in Darlaston and Wednesbury."`
- New: `"... he came back having lost a little skin from one hand. Journal, February 1744: James Jones's account of mobs in Darlaston and Wednesbury."`

(The text before "he came back" stays word for word.)

### FIX 4: `briefReferences[7]`: the brief does not tell the Conference's three questions

- Old: `"Conference Minutes, 1744: the first Conference at the Foundery asks what to teach, how to teach and what to do, and allows lay assistants only in cases of necessity."`
- New: `"Conference Minutes, 1744: the first Conference at the Foundery allows lay assistants only in cases of necessity."`

### FIX 5: `briefReferences[8]`: the brief does not tell his view of presbyters and bishops

The brief tells the occasion ("After American independence") and that "only bishops normally did so", not Wesley's view that presbyters and bishops are one order.

- Old: `"... Curnock's introduction to the volume: his reasons, and his view of presbyters and bishops."`
- New: `"... Curnock's introduction to the volume: his reasons."`

(The text before "Curnock's introduction" stays word for word.)

### FIX 6: `uncertain[7]`: "as a Superintendent" is the editor's bracket, not the Diary

At J7 1151-1152 the Diary reads "4 Prayed, ordained Dr. Coke"; the words "as a Superintendent, by the imposition of my hands..." follow inside Curnock's square brackets, quoting another document (he points to the facsimile and the letter of 10 September).

- Old: `"The ordinations of 1784. The published Journal says he appointed Whatcoat and Vasey to serve in America. His Diary for the same days says he ordained them, and Dr. Coke as a Superintendent. The reasons are Curnock's account: Wesley held that presbyters and bishops were no different in rank."`
- New: `"The ordinations of 1784. The published Journal says he appointed Whatcoat and Vasey to serve in America. His Diary for the same days says he ordained them, and Dr. Coke; the words as a Superintendent are the editor's, set in brackets beside it. The reasons are Curnock's account: Wesley held that presbyters and bishops were no different in rank."`

## 1. Each field against its evidence

Re-read at the cited lines; each holds except FIX 6. Checked in full: J7 1108-1113 (appointed Whatcoat and Vasey), J7 1142-1152 (Diary); J8 8742 (Tuesday, 1 March), 9029-9037 (Ritchie, cried out, repeated), 9095 (the last word "Farewell"); LEE 4277-4287 (Episcopal church; reform the continent); LEE 7561-7567 (died in London 2 March 1791, not quite eighty-eight); MIN 35380-35420 (72,476; 136,622; America printed 61,146; the West Indies note); ALLEN 734-750 (plain doctrine, good discipline, tyrants, no trial). The 1791 arithmetic holds: 57,621 + 6,525 = 64,146, and 64,146 + 72,476 = 136,622. "A scan fault" in `uncertain[8]` may be a printer's slip rather than a scan fault. The sum shows the printed figure is wrong, but it cannot show which, so this is not ruled a FIX.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. Brief references that remain

All 14, as trimmed above: Aldersgate and Charles's "I believe."; Bristol, the brickyard; priest, the name a reproach; the bishop of Bristol and the wrath to come; the Bristol class; Wednesbury and Walsall, and Jones's report; Nelson; the 1744 Conference and necessity; the 1784 ordinations; the 1784 Episcopal church and the 1789 Dublin words; the 1791 count; Lee, the Discipline and Allen; Ritchie and Lee on his death; the census entries.

## 4. Census rules

- Keys: all allowed; no `briefLength`.
- Quotations: the brief has 4 quoted spans; the card has 4 entries, one each, none extra. Each `modern` is the brief's wording exactly.
- Each `printed` stands at its file and lines (folded as the validator folds; checked in memory, no file written): J1 27071-27074, CW 7723-7724, J3 5741-5742, J8 9033. Every cited file is in `sources`. No scan fault inside any span, so no `tools/quote_scan_readings.json` entry is needed.
- Quotation marks in `briefReferences`: only "I believe." in `briefReferences[0]`, which stands verbatim in the brief. Allowed.
- American spelling throughout ("Labors" in Allen's title, "favor", "organizer").
- `secondReading` is absent from all four, as the new-card prompt directs; the second-reading step must fill it before the card can pass the validator.

## 5. Originals

All four quotations come from English printed wording. There is no held non-English original. Nothing to add.

## 6. "Not found" claims and conflicts

- Whitefield as "a fellow priest": not in the cited lines (J2 10699-10700), so the card is right to leave it off. The brief still says it (paragraph 4). That is the brief's matter, not the card's; it is flagged for the story's owner.
- Nelson hearing him outdoors: the card is right to put it under `uncertain[6]` as a reading of LEP 1600 and 1631-1642.
- Curnock's notes that the writer did not re-read (J1 26952-26955, 27030-27037; J2 10871-10876, 31864-31870): J1 26965 and 27015 name Nettleton Court, so `uncertain[1]` holds there. The rest are not contradicted by anything read.
- No conflict with the entry's own fields.

## Applied to the brief (coordinator, 2026-11-19)
- "George Whitefield, a fellow priest, called him" -> "George Whitefield called him": the card check found "a fellow priest" in no cited line (J2 10699-10700). Words removed only.

## Applied (card fixer)
- FIX 1, 2, 3, 4, 5, 6: all applied word for word.
- Not applied: none.
