# Card edits: Eusebius of Caesarea

Batch 7, 2026-11-20. Card: `eusebius-of-caesarea.card.json`. Existing card: `Card.existing.json` (unchanged census object). Every other word of the existing card is kept as it stands, in its order. The existing card has no `quotationOriginals`, so no `secondReading` could be copied.

Files: EUS = `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml`; ATH = `npnf204_athanasius-select-works-letters.xml`; SOC = `npnf202_socrates-sozomen-ecclesiastical-histories.xml`; SOCG = `socrates_historia-ecclesiastica-tomus1-grc-lat_hussey1853.txt`; HEF2 = `hefele_history-of-the-councils-v2-326-429_oxenham1876.txt`; GRK = the Schwartz-Mommsen file with Rufinus's Latin.

## 1. Correction (clearly wrong)

**`uncertain[0]`, last clause.**
- Old: `and Athanasius says only that Eusebius was "accused of sacrificing."`
- New: `and the bishops of Egypt, in a letter Athanasius kept, say only that Eusebius was "accused by our confessors of sacrificing to idols."`
- Evidence: the words are in the encyclical letter of the council of Egypt, which Athanasius kept in his Defence Against the Arians (ATH 21991-21996 for the letter and its senders; ATH 22308-22309 for "accused by our confessors of sacrificing to idols"; "end of 338 or beginning of 339", ATH-ed 21662-21663). Athanasius is not the speaker. McGiffert (EUS 1537-1540) gives the phrase to Athanasius, and in his own wording ("accused of sacrificing"); that wording is not in the Egyptian letter, so the quote is now the letter's own. The brief says "the bishops of Egypt wrote that he had been "accused"".

## 2. New: quotation originals (all awaiting second reading)

| # | Modern (as the brief has it) | Printed | Lines |
|---|---|---|---|
| 1 | I confess that it is beyond my power ... lonely and untrodden path. | McGiffert, HE I.1.4 | EUS 6934-6937 |
| 2 | With our own eyes we saw the houses of prayer ... mocked by their enemies. | McGiffert, HE VIII.2.1 | EUS 43431-43437 |
| 3 | You sit there, Eusebius ... judged by you? | McGiffert's English of Epiphanius, Panarion 68.8 | EUS 1515-1517 |
| 4 | Tell me, were you not with me in prison ... or did it? | same | EUS 1517-1523 |
| 5 | of one being | "One in substance"; original ὁμοούσιος | EUS 2091 (both) |
| 6 | not without inquiry | McGiffert, letter to his church; original οὐκ ἀνεξετάστως | EUS 2160; SOCG 7520 |
| 7 | accused | "accused by our confessors of sacrificing to idols" | ATH 22309 |

- All seven: `secondReading` left out; the second-reading step fills it in.
- Originals (Batch_Originals_Ruling rule):
  - Quote 2 (Greek GRK 13615-13620): left out. The scan has faults (χ for κ in προσευχτηρίων and οἴχους) and no held print of the Greek confirms the reading; Rufinus's Latin is a translation, not a print of the Greek. English alone.
  - Quote 3 (Epiphanius's Greek, EPI 44590-44604): left out for the same reason; Petavius's Latin is a translation. English alone. The entry's note says the modern wording agrees with the Latin (EPI 44669-44675).
  - Quote 1: HE I in Greek is not held. English alone.
  - "accused" (ATHG 61819-61820): left out. The scan reads "χατηγορεῖτο" (χ for κ), with no held print to confirm. English alone.
  - "of one being": the Greek word ὁμοούσιος stands clean in EUS 2091, printed by McGiffert in his English, checked by hand letter by letter.
  - "not without inquiry": οὐκ ἀνεξετάστως stands clean in SOCG 7520 (the line's other marks are outside the span), checked by hand. The same line run is in SOCG's own apparatus (7540). The note records Hussey's remark that two older printings lack the clause (SOCG 7538-7541), and that Athanasius's English has it (ATH 19866-19868).
- Notes (`uncertain` on entries): entry 2, one Greek verb for "we saw" (sheet E6); entry 3, Epiphanius's report, about forty years later; entry 4, "our persecutors" renders "those that put upon us the pressure of persecution", and the brief drops "Who can bear such things?" between the two spans (EUS 1517); entry 5, ὁμοούσιος printed "One in substance"; entry 7, the words are the Egyptian bishops'.

## 3. New: sources

- `sources.ownWords`, added at the end: SOCG (Greek, with Hussey's Latin), for the original in entry 6.
- `sources.about`, added at the end: SOC (a second entry, Book 1 chapters 1 and 32, Book 2 chapters 4 and 21: SOC 1842-1868, 5208-5211, 5802-5806, 6916-6921); ATH (De Decretis 3, ATH 26780-26786; the Egyptian letter; De Synodis 17, ATH 57219-57221); HEF2 (the presidency, HEF2 1790-1791; Rufinus against Epiphanius, 1826-1835; the judgments of his faith, 1104-1108 and 1124-1129); Philostorgius in Photius's summary (`philostorgius_ecclesiastical-history_walford1855.txt`, line 88).

## 4. New: `briefReferences` (14)

Written fresh, with no quotation marks. Each draws on a passage the brief uses: HE I.1, VI.20.1, VIII.2.1-4; Martyrs of Palestine 7 and 11 (EUS 46694-46699, 47068-47069); McGiffert's Prolegomena (EUS-ed 1086-1091, 1120-1123, 1600-1604, 2785-2786, 1017-1019, 4575-4578); VC I.11, I.19, I.28, IV.41; his letter on Nicaea; Socrates I.8 and Athanasius, De Decretis 3; Epiphanius 68.8 and Socrates I.32; the Egyptian letter; Rufinus X.18 and prologue (GRK 28009-28017, 26043-26056); Socrates I.1; HE V.24, I.11, III.33; Socrates II.21 and II.4, De Synodis 17. The brief's words "Eusebius ... knew him as emperor" and "wrote the Life after 337" rest on VC I.19 and I.28 and McGiffert's dates.

## 5. New: `legacy.traces` (four added, after the existing two)

1. Many earlier writings known only through his extracts: McGiffert's note, EUS-ed 6965-6969 (brief: "survive only in his quotations").
2. Polycrates, Josephus, Pliny: EUS 31104 (the only writing of Polycrates known) and 31324 ff.; EUS-ed 9212-9214 ("the first one to quote this passage"); EUS 19448-19452, 19541-19543, 19555-19556 (Pliny and Trajan, taken from Tertullian's Latin Apology).
3. Socrates begins where Eusebius stopped (SOC 1861-1868); Rufinus puts the History into Latin (GRK 26043-26056; the brief's "carried it on" rests on Rufinus's Books X and XI, GRK 26095-26101).
4. Eusebius as eyewitness: EUS 44268-44272 (the Thebais; "decapitation, others torture by fire"); McGiffert, EUS-ed 1569-1574. Review.md (section 1) says the card can carry this; the story leaves it out.

## 6. New: `uncertain` (eight added, after the existing three, in time order)

Each credits every held source that differs (Mark, 2026-11-19).

1. **First to try.** His claim and McGiffert's agreement, with Hegesippus and Julius Africanus as the two partial forerunners: EUS 6934-6937, EUS-ed 6937-6952. (Source_Sheet D1: "the forerunners are for the card".)
2. **The month the persecution began.** HE VIII.2.4 (March); Martyrs of Palestine (April); Lactantius (February 23); McGiffert trusts Lactantius and thinks Eusebius gave the month the edicts reached other places: EUS 43460-43480 with notes. (Outline "Leave out": the date dispute, "for the card".)
3. **How he came to sign.** His letter (EUS 2129-2133, 2158-2162), Socrates (SOC 2971-2978), Athanasius (ATH 26780-26786). The brief names all three.
4. **Eustathius and Sabellius; Antioch's see.** SOC 4708-4711, 4752-4760. (Outline "Leave out": "For the card".)
5. **Who presided at Tyre.** Epiphanius (EPI 44478-44479, 44539-44540), McGiffert (EUS-ed 2556-2560), Hefele (HEF2 1790-1791). The brief says only that he sat among the judges, Epiphanius says.
6. **Rufinus's scene.** GRK 28009-28017 (Paphnutius, Maximus of Jerusalem, "effosso oculo et poplite succiso", "te, inquam, non patiar sedere in concilio malignantium"); Hefele's view, HEF2 1826-1835. (Outline 86 and Outline_Check 13: "the names are for the card".) The date "about 402" is left out; "writing later in Latin" follows the brief.
7. **The Life of Constantine.** VC I.11 (EUS 60653-60663); SOC 1863-1866; VC IV.41 (EUS 67217-67226), which names neither Athanasius nor Potamo. The brief's three credits.
8. **His beliefs.** ATH 57219-57221 (Euphration); SOC 6916-6921; Philostorgius in Photius's summary (line 88); Hefele (HEF2 1104-1108, 1124-1129). The brief's "judged both ways".

## 7. Not carried, and claims not found

- Sabinus's praise (Outline 157, "for the card"): already in the existing card's `legacy.remembered`; not repeated.
- The sheet's note that Hefele volume 1 (`hefele_history-of-the-councils-v1-to-nicaea_clark1872.txt`) has Arius naming Eusebius among his supporters: not carried. It is optional ("the card can carry it"), and the held scan (lines 16348, 16640) reads "Ceesarea" and breaks the sentence across lines; it needs a hand check before use.
- No claim in the existing card was found unsupported. "Wrote the first history of the church" (`knownFor`) is his own claim as McGiffert endorses it, and the new `uncertain` entry 1 credits it.
