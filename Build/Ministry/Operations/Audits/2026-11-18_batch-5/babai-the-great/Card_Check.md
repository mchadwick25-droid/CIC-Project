# Card check: Babai the Great

**Verdict: FIX** (three references).

Base: the census card for `babai-the-great`. It is identical to `Card.existing.json` (object comparison). Diffed field by field: only `briefReferences` and `quotationOriginals` are new, as `Card_Edits.md` lists.

## 1. Edits justified

Every listed edit checks against its evidence. Re-read:
- TM 2015-2017, 2594-2599, 2681-2683, 2766-2768, 3016-3023, 3428-3432, 3996-4013, 4120-4141, 4186-4190, 5160-5188.
- SO 42215-42219, 42365-42368, 42403-42417.
- LAB 13096-13099, 15878-15890 (footnote "De Unione, f. 122 B").
- Guidi, Chronica minora 2013-2019.
- Braun 852, 12426-12437.

## 2. Nothing else moved

Confirmed. Every other field is word for word and in order.

## 3. References

Rule applied: remove what the brief does not tell, but keep a date that grounds one of the brief's dates ("around 609").

FIX 1. `briefReferences[8]`. The brief does not tell the year in prison or Seleucia.
- Old: `Anonymous chronicle, in Chronica minora, Latin tr. Ignazio Guidi: George of Izla accused before the king of leaving the Magian religion, held a year in prison and crucified at Seleucia.`
- New: `Anonymous chronicle, in Chronica minora, Latin tr. Ignazio Guidi: George of Izla accused before the king of leaving the Magian religion and crucified.`

FIX 2. `briefReferences[9]`. The brief does not tell the request of the faithful or the feast.
- Old: `Life of George, German tr. Oskar Braun: George's death in 615; Babai writes the Life at the request of the faithful gathered for his feast.`
- New: `Life of George, German tr. Oskar Braun: George's death in 615; Babai writes his Life.`

FIX 3. `briefReferences[10]`. The brief says Nestorius was condemned in 431. It does not name the council of Ephesus.
- Old: `World census, the Church of the East under Persia: a church under a Zoroastrian shah, whose answer on Christ was neither Chalcedon's nor the Miaphysites'. World census, Nestorius: bishop of Constantinople, removed by the council of Ephesus in 431.`
- New: `World census, the Church of the East under Persia: a church under a Zoroastrian shah, whose answer on Christ was neither Chalcedon's nor the Miaphysites'. World census, Nestorius: bishop of Constantinople, condemned in 431.`

These stay as they are:
- [0] The oath, and Budge's 608 or 609. That date grounds "around 609".
- [1] to [4], [6], [7].
- [5] "Two natures and two hypostases". The brief tells it in the outline's plain words, "two natures ... each real and complete, in one person" (Outline, hypostasis).

## 4. Census rules

Pass.
- Only allowed keys, and no `briefLength`.
- There are two quoted spans in the brief and two entries, with none left over.
- Each `printed` stands at its lines (LAB 15887-15890, TM 5185-5188), under the census fold, with no scan reading needed. Both files are in `sources`.
- There are no quotation marks in the references.
- No audit, review or ruling is named.
- The new fields use American spelling.

Two entries have no `secondReading` yet. That is expected: second readings come at step 7.

## 5. Originals

Pass. Q1's printed wording is Labourt's French, the oldest form held (the Syriac is unpublished). Q2's is Budge's English, and no Syriac is held.

## 6. Not found, and left in

The card writer checked one claim and lists no "not found". Ruling: the claim stands. Mari, in Gismondi's Latin, names Mar Aba the archdeacon and "Mar Babaoo Magno" [Babaeo] as governing the church in its seventeen years with no head (MARI 13517-13520). The sheet missed it because of the OCR. Nothing clearly wrong is on the card.
