# Card check: The Second-Century Greek Apologists

Checker: did not write the card. Read: `CLAUDE.md` (Trust and source fidelity), Kit Part 1, `kinds/tradition.md`, the role, the brief (final after `Grade2_Fixes_Applied.md`), `Outline.md`, `Review.md`, `Fresh_Read.md`, `Card.existing.json`, `greek-apologists-second-century.card.json`, `Card_Edits.md`. No entry file (the tradition has its census entry).

## Verdict: FIX

Two changes. Everything else passes.

### FIX 1. teaser (overstates the source)

- Field: `teaser` (entry field, Card_Edits "Entry fields" 2 / card edit 2).
- Old: "that the Greek poets and philosophers had spoken of one God too."
- New: "that most Greek poets and philosophers had spoken of one God too."
- Why: Athenagoras says it only "for the most part" (athen-grc 311, ὡς ἐπὶ τὸ πλεῖστον); the brief says "almost all spoke of one God". As written, the teaser makes it all of them.

### FIX 2. "honour" in Quote 1 (a paired change: brief and card together)

- Ruling: "honour" is a defect. Our modern renderings use American spelling (Answering-From-Sources Decision-Log 77), and the printed English it is rendered from has "honor" (npnf201 25828). It is the only British form on the card (spelling table check).
- The card cannot change alone. `quotationOriginals[0].modern` has to match the brief's quoted span word for word, or the validator fails. So the card stays as it is now, and this change goes to whoever applies changes to the brief, as one paired edit:
  - Brief, Melito's quote. Old: "we gladly accept the honour of such a death." New: "we gladly accept the honor of such a death."
  - Card, `quotationOriginals[0].modern`. Old: "...and we gladly accept the honour of such a death." New: "...and we gladly accept the honor of such a death."
- The word count (675) and the scorer result do not change.

## Ruling: `dates` "c. 124-200" and `start` 124

No change. Reasons:
- These are census placement fields. They are not card prose, and they are not among the short texts the role names. The card's `people[].year` (124, 125, ...) and `documentedStories[0].when` "c. 165" belong to the same class. The writer rightly kept them all.
- The year is given loosely ("c."), and it rests on an old source. Eusebius's Chronicle, in Jerome's Latin, sets the books of Quadratus and Aristides under Hadrian at Olympiad 226 (Fotheringham 1923, 42525-42545). Converting that to about 124/125 tells the date only as roughly as the old source allows (Kit Part 1, Rigor).
- The outline bars "in 124" / "around 124" in the telling. The brief and the card prose now keep to that: voices[0] has dropped it.
- Moving a tradition's `start` would shift the tree's layout. That is a census decision, not a card edit.

## Checks

1. **Edits justified; items sent to the card are on it.** I re-opened every edit's evidence: why, teaser, voices 0/2/3/4/6, legacy, and the moved modern works. They hold, apart from FIX 1. Every Cut first item marked card is on the card (1, 3, 4 with "raised from the dead", 5, 6, 7, 11-17, 19-22, 24), and so are the Leave out and Do not say items marked card (tortured servants, Trinity, the Aristides headings, Fundanus, Jerome). Review.md and Fresh_Read.md send nothing else. Both modern works sit only in `modernWorks`, and their notes say what each work covers.
2. **Nothing else moved.** A field-by-field diff against `Card.existing.json` shows changes only in why, teaser, voices[0,2,3,4,6], legacy and documentedStories[*].sources/modernWorks. It also shows the three new keys. sourcing, floorNote, relationsSummary, people and every documented story's other fields are word for word.
3. **briefReferences:** none on the card. Nothing to remove.
4. **Census rules.** Three quoted spans in the brief, three `quotationOriginals`, each `modern` equal to its span. No `secondReading` (all are 29+ words). No `briefLength`. Every cited file is in `sources`. No audit file is named. Spelling is American apart from FIX 2.
   - Printed text re-read at its lines:
     - Melito: npnf201 25826-25829, verbatim.
     - Athenagoras: Greek at athen-grc 1546-1550, verbatim once the milestone tag is stripped; English at anf02 13330-13349, verbatim once footnote 830 is stripped. The Greek was checked by hand: πλησίον, ἀπηγορεύσαμεν, ἅγος καὶ μίασμα.
     - Diognetus: Greek at diog-grc 312-317, verbatim, πάνθ̓ included; English at anf01 2735-2738, verbatim.
   - The renderings match their originals. Rendering from the Greek for Q2 and Q3 is carried. The Melito English stands alone, as Otto 1872 is a damaged scan, and its `uncertain` says so.
   - Validator, on a scratch census outside the repository with the card, the brief as `longDescription`, livingEvidence and modernWorks merged: the full run was killed for lack of memory. With `--skip-quotes`: 629 movements, 736 edges, 10 eras, 0 errors, 4 warnings, all on other entries. I checked the quotes by hand instead (above).
5. **"checked at card":** none.
6. **Not found / left in.** I agree with each item the writer listed as not found; none is contradicted by a held source. The teaser's "emperors who had them killed anyway" can stand: Justin was sentenced for refusing "the command of the emperor", anf01 29396-29398. New claims I spot-checked at their lines all hold:
   - Aristides's headings (anf09 19003-19008; 1apol-grc 68-69).
   - Syriac-only fasting and slaves (anf09 19587-19609; the Greek at 18945-18964 lacks both).
   - Quadratus and Jerome (npnf201 21056-21068; npnf203 39904-39906).
   - Crescens (2apol-grc 272-276).
   - Melito on Hadrian and the father's letters (npnf201 25888-25897).
   - The Chronicle (42525-42545).
   - Clement on Tatian (anf02 29724-29727), Tatian as Justin's hearer (anf01 33664), and the Trinity figure (anf02 8990-8993).
7. **Census entry:** none written. `livingEvidence.basis` ("A circle" → "A number") passes, per Outline, Do not say.
