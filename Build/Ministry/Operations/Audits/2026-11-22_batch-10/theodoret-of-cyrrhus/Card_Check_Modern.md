# Theodoret of Cyrrhus: card check, the modern pass (2026-11-23)

Check pass of `roles/card.md` on `theodoret-of-cyrrhus.card.json`. Starting card: `Card.pass3.json`. Edit list: `Card_Edits.md`, **Fourth pass: no modern opinion (2026-11-23)**. Brief: `theodoret-of-cyrrhus.brief.txt` as it now stands. The checker did not write the card. Indexes count from 0.

## Verdict: FIX

## What holds

- **Nothing else moved.** A JSON diff of `Card.pass3.json` and the card shows only the listed edits: `uncertain[29]` to `[31]` added, `briefReferences[2]` added, `briefReferences[6]` replaced, and `briefReferences[12]` extended.
- **Cited lines, all re-read.** NP3 2577-2596 (Cyrestica, "a wretched little place", "scantily inhabited"); NP3 29918-29919 ("solitary as it is, and with only a small population, and that a poor one"); NP3 2714-2716 ("bound by ties of close friendship"); NP3 3303-3304 ("his ancient friend"); EVW 213 ("FROM 431 TO 594 A.D."); EVW 12203-12204 ("in the twelfth year of the reign of Maurice Tiberius"); NP14 17263-17280 (the decree); NP14 18650-18653 (John's meeting "as soon as he was come to Ephesus"); NP14 17710-17720 ("Theodoret of Cyrus" among those who withdrew with John); NP3 36858-36868 (Candidian's order to await the bishops); NP2 20944-20945 (the consulate of Bassus and Antiochus). Each holds its entry.
- **`briefReferences`.** No entry names wording the brief no longer has. "friend", "northern Syria", "his English translator says", "without waiting", "In 433", "then" and "About 140 years later" are gone from the card's references. The new Letter 32 entry matches "a small town", and the Evagrius addition matches "Long after".
- **Quotations.** The brief has seven quoted spans, the same words as before. There are seven `quotationOriginals`, unchanged. The four "checked at card" spans ("unwillingly", "Anathema to Nestorius", "a most excellent record", "not a tomb") are verbatim at NP3 31499, NP3 3335, EVW 1110 and NP3 33203.
- **Rules.** Allowed keys only. Every cited file is in `sources`. No audit is named. The spelling is American outside printed wording.

## What fails

1. **"about 593".** The card's own reckoning, taken from the source sheet, credited to no one by name and not marked as modern. The new `uncertain[31]` does not cure it. It calls the date "the same kind of reckoning" as Walford's heading, but it names no one as its source. Under the rule, the date must go, or be credited by name as modern. No named source holds 593: Walford's heading gives 594. So the date goes from `legacy`, and `uncertain[31]` keeps Walford's 594, marked as modern.
2. **433 credited to no one by name.** "the editors' reckoning" names no one. The held source is Blomfield Jackson's chronological table and prolegomena (NP3 2149-2152, 4410). `uncertain[7]` gives 433 with no credit at all.
3. **Modern views named but not marked as modern.** Jackson, Tillemont, Garnier, Möller, Zenos, Richardson and Hogg are named, but in the fields below none of them is called modern. The new entries' own standard is "a modern judgment". `uncertain[20]` credits "the translator's note" but names no translator. The note is Jackson's: NP3 20518-20519, in his English of the Eranistes. Each fix marks the person as modern once, at their first mention in each field. Later mentions in the same field stand.
4. **Clearly wrong, left in.** `uncertain[0]` makes Jackson the source for John of Antioch's request that Theodoret answer Cyril. The request is in Theodoret's own Letter 150, headed "Letter of Theodoretus, Bishop of Cyrus, to Joannes, Bishop of Antioch": "the anathematisms which you have sent to request me to refute in writing" (NP3 36076-36090). The brief rests on that letter, and so does the card's `briefReferences[3]`.
5. **`briefReferences[6]`, the list.** "The same council's list" follows the Eastern bishops' report, so it reads as the Eastern side's list. The list is in the letter of Cyril's council (NP14 17708-17720), which names those who withdrew with John.

## Changes, exact

**1. `legacy.traces[5]`**
- Old: `Evagrius, writing about 593 from the acts, says`
- New: `Evagrius, writing from the acts, says`

**2. `uncertain[31]`**
- Old: `The year of the peace between Cyril and John is not given in any held old line. 433 is the editors' reckoning. Walford's heading puts the close of Evagrius's history at 594 AD, and the card's "about 593" is the same kind of reckoning. Evagrius himself says only that he closes it in the twelfth year of the reign of Maurice Tiberius.`
- New: `The year of the peace between Cyril and John is not given in any held old line. 433 is the modern reckoning of Blomfield Jackson, his translator. The heading of Walford's modern English edition puts the close of Evagrius's history at 594 AD, also a modern reckoning. Evagrius himself says only that he closes it in the twelfth year of the reign of Maurice Tiberius.`
- Evidence: NP3 2149-2152, 4410; EVW 213, 12203-12204.

**3. `uncertain[7]`**
- Old: `which fits the peace of 433.`
- New: `which fits the peace that Jackson dates to 433.`

**4. `uncertain[0]`**
- Old: `Blomfield Jackson, his translator, is the source for his friendship with Nestorius of Constantinople and for John of Antioch's request that he answer Cyril.`
- New: `Blomfield Jackson, his modern translator, is the source for his friendship with Nestorius of Constantinople.`

**5. `uncertain[1]`**
- Old: `he reports that Garnier gave 386 and Möller 390.`
- New: `he reports that Garnier gave 386 and Möller 390. All four are modern scholars.`

**6. `uncertain[4]`**
- Old: `Ernest Cushing Richardson's note gives 457.`
- New: `Ernest Cushing Richardson, a modern translator of Gennadius, gives 457 in a note.`

**7. `uncertain[20]`**
- Old: `the translator's note says this is the only fragment of Methodius that Theodoret preserved.`
- New: `a note by Blomfield Jackson, its modern translator, says this is the only fragment of Methodius that Theodoret preserved.`

**8. `uncertain[22]`**
- Old: `Hope W. Hogg, in the Ante-Nicene Fathers edition`
- New: `Hope W. Hogg, a modern editor, in the Ante-Nicene Fathers edition`

**9. `datesNote`**
- Old: `Born in 393 by Tillemont's reckoning, which Blomfield Jackson follows (Garnier gave 386 and Möller 390);`
- New: `Born in 393 by the modern reckoning of Tillemont, which Blomfield Jackson, his modern translator, follows (the modern scholars Garnier gave 386 and Möller 390);`

**10. `placeNote`**
- Old: `Antioch, by Jackson's account;`
- New: `Antioch, by the account of Blomfield Jackson, his modern translator;`

**11. `keyWorks[2].about`**
- Old: `whom Blomfield Jackson reads as`
- New: `whom Blomfield Jackson, its modern translator, reads as`

**12. `legacy.traces[1]`**
- Old: `Jackson notes that he was reinstated`
- New: `Blomfield Jackson, his modern translator, notes that he was reinstated`

**13. `legacy.traces[2]`**
- Old: `A. C. Zenos, in the edition of Socrates of Constantinople,`
- New: `A. C. Zenos, a modern editor, in the edition of Socrates of Constantinople,`

**14. `briefReferences[6]`**
- Old: `The same council's list names Theodoret of Cyrus among John's men.`
- New: `The letter of Cyril's council names Theodoret of Cyrus among John's men.`

No other change. Once the changes are made, run `node tools/validate-census.mjs --skip-quotes` again on a scratch copy of the census.
