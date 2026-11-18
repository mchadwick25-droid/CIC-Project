# Card check: the Council of Nicaea (325)

Checker, 2026-11-18. Starting card: the census `council` object for `council-of-nicaea-325` in `cic-website/data/world-census.json`.

**Verdict: FIX** (five `briefReferences` changes). Separately, four `quotationOriginals` entries still need a second reading before the census check can pass (see 4).

## 1. Edits justified

- "God of God, Light of Light" removed from `quotationOriginals` and from the creed reference: not in the brief. Justified.
- "shall not be set aside" narrowed: the brief quotes only these words. Printed, file and lines unchanged (npnf214 13970-13972). Justified.
- New quotations, each verbatim at its lines: "a creature" (npnf214 6346-6347); "whispering ... and winking" (npnf204 27991-27992); "in the sight of all" (npnf203 6395-6396). Justified.
- "one in essence" and "of one substance" replaced by "of one being": the brief's words. Justified.
- Socrates I.6 and Antioch canon 1 removed: not in the brief. Justified.
- New references 5-13 checked at their lines (npnf214 6343-6347; npnf201 64282-64288, 64360-64361; npnf203 6387-6396; npnf204 26762-26763, 27989-27995; npnf201 64525-64527; npnf202 2950-2954, 3382-3384; npnf214 13972-13977). Each matches the brief's sentence. Justified.

## 2. Nothing else moved

Diffed against the census `council` object. Only `briefReferences` and `quotationOriginals` differ, as listed. Every other field is word for word; order kept.

## 3. References that remain, and those that do not

Five references still name what the brief no longer tells, or never told. Each was kept word for word by the card writer; the rule applies to them all the same.

- Arius's letter: "driven out by Alexander". The earlier brief (v1) said "after his bishop had driven him out"; the finished brief cut it.
- Eusebius's Letter to his church: "his creed read, the emperor's approval". The brief tells only that the emperor asked for one word to be added (Athanasius, npnf204 19655-19660: "he advised all present ... to subscribe its articles ... with the insertion of the single word, One-in-essence").
- De decretis 19-20: "the words written more distinctly" (npnf204 27887-27889, 28015-28018). Not in the brief.
- The creed reference: "as at Rome and Alexandria" and "canon 13, the last communion for the dying". The brief says only "Easter would fall on one day everywhere", and names canons 4 and 11, not 13.
- Constantinople and Chalcedon: "Chalcedon recites the creeds of Nicaea and of Constantinople apart (20225-20230)". Not in the brief.

These remain, with nothing to remove: Life of Constantine III.4-7; III.6-8; III.12; De decretis 20; Eustathius in Theodoret I.8; Life III.14 and Socrates I.8; Socrates I.8 and Sozomen I.20 (Eusebius and Theognis are kept, because "before them" needs them to place Arius's recall, which the brief tells); Constantine's letter in Socrates I.9; canons 4 and 11; Constantinople canon 1 (newer heresies); Jerome; Braun; the African code; the synodal letter.

### FIX

Field `briefReferences`, entry 0.
- Old: `Arius, Letter to Eusebius of Nicomedia, in Theodoret I.4 (Greek, PG 82; English, npnf203): driven out by Alexander; the Son has a beginning.`
- New: `Arius, Letter to Eusebius of Nicomedia, in Theodoret I.4 (Greek, PG 82; English, npnf203): the Son has a beginning.`

Field `briefReferences`, entry 5.
- Old: `Eusebius of Caesarea, Letter to his church (in Athanasius, npnf204, and Socrates, Greek ed. Hussey): his creed read, the emperor's approval, "of one being" added.`
- New: `Eusebius of Caesarea, Letter to his church (in Athanasius, npnf204, and Socrates, Greek ed. Hussey): the emperor's advice to add "of one being".`

Field `briefReferences`, entry 6.
- Old: `Athanasius, De decretis 19-20 (npnf204, 27875-27889, 28015-28018): "from God" chosen from Scripture and read as true of all creatures; the words written more distinctly.`
- New: `Athanasius, De decretis 19-20 (npnf204, 27875-27889): "from God" chosen from Scripture and read as true of all creatures.`

Field `briefReferences`, entry 10.
- Old: `The creed of Nicaea, the synodal letter and the twenty canons (npnf214): "begotten, not made", "of one being"; the anathema; Arius, Theonas and Secundus condemned; Melitius kept his title but could not ordain; one Easter, as at Rome and Alexandria; canon 13, the last communion for the dying.`
- New: `The creed of Nicaea, the synodal letter and the twenty canons (npnf214): "begotten, not made", "of one being"; the anathema; Arius, Theonas and Secundus condemned; Melitius kept his title but could not ordain; one Easter.`

Field `briefReferences`, entry 14.
- Old: `Council of Constantinople (381), canon 1, and Council of Chalcedon (451), definition (npnf214): the faith of the 318 fathers "shall not be set aside" and "pre-eminent"; Chalcedon recites the creeds of Nicaea and of Constantinople apart (20225-20230).`
- New: `Council of Constantinople (381), canon 1, and Council of Chalcedon (451), definition (npnf214): the faith of the 318 fathers "shall not be set aside" and "pre-eminent".`

## 4. Census rules

- Keys: the council's allowed keys only; no `briefLength`.
- The brief quotes twelve spans; twelve entries, one for each. "there was a time when he was not" stands quoted once and covers both uses.
- Printed verbatim, spot-checked at their lines: npnf214 2411-2421; npnf206 32412-32413; Heikel 11167-11168; PG 82 70615-70616 with npnf203 6045-6046; npnf201 64468-64470; and the four new or changed entries above. Every cited file is in `sources`.
- Quotation marks in `briefReferences`: each quoted phrase is verbatim in the brief.
- No audit, review or ruling named. American spelling ("anathematized").
- **Open:** four entries carry no `secondReading` ("whispering ... and winking", "in the sight of all", "a creature", "shall not be set aside"). The census check requires one on every entry. This is a second reading still owed, not a card fault to fix here: none may be invented.

## 5. Rulings

- "Not found": none claimed. None found.
- Nothing clearly wrong left in, beyond the references in 3.
