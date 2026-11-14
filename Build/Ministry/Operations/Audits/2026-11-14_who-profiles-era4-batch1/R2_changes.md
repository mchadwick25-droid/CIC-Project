# R2 changes: era 4 batch 1

Each profile's drafter applied the round 2 findings, opening every cited line before changing it. The parts follow, unchanged.

## R2 changes, part 1: era 4 batch 1 (Bede, Hild of Whitby)

I opened each cited line in its file before making any change. Afterwards I rebuilt both audio files by script and checked that each equals its brief once the two tags are removed. I re-checked the quotations in the briefs and cards by script. The script flags two quotations, and I confirmed both by eye. "The faithful testimony of innumerable witnesses" is split by a page header (GILES l.229). "Beda presbyter dormit" has an OCR footnote mark inside it (ANNALES l.2893). I did not write the repo `records.json`, on the coordinator's instruction. Only the scratchpad records were edited.

| Finding | Done |
|---|---|
| R2-1-M1 (Bede card `dates`) | Taken as worded. The line now reads "the Saxon Chronicle and several other chronicles give 734". This matches PLUMMER l.5479-5481 ("734 is the date of all MSS. of the Sax. Chron., of the Ann. Ult. …") and the card's `uncertain` 1. |
| R2-1-M2 (Bede notes, census side) | Taken. Two items are added to the census-difference list: item 5 and item 6. Item 5: the live card's `keyWorks` 3 joins On the Times to the "De Temporibus" of III.17 (GILES l.6988-6990; PLUMMER l.2736-2738). Item 6: the live card's `remembered` opens with the beat line "Rome honors him." |
| R2-1-M3 (Hild brief P2, "later" with no anchor) | Taken: "writing about fifty years after her death". To stay under the cap, P1's "with verses in praise of God" became "with verses praising God". Giles says he began "to sing verses to the praise of God" (l.11177-11178). The brief is now 404 words, FK 5.58, Flesch 78.1. |
| R2-1-M4 (Hild `otherNames`) | Taken. `otherNames` is now `["Hilda"]`. The oblique forms are Raine's "matre piissima Hilde" at l.5083 and "Hylde religiose memorie" at l.9425. The nominatives are "Hild" (PLUMMER l.24823) and "Hilda" (GILES l.10891; AASS June 5 l.95275). The records gain a claim on the name forms that marks Hilde and Hylde as Latin case forms. |

Bede brief unchanged: 405 words, FK 6.54, Flesch 71.8.

## R2 changes, part 1: era 4 batch 1 (Aidan of Lindisfarne, Adomnán of Iona)

Every cited line was opened in its vendored file first. Audio scripts were rebuilt by script from their briefs and confirmed equal to them once the two tags are removed. Every quotation in the briefs and cards was re-checked by script. Records were edited in `scratchpad/records/<id>.json` only, not in the repo `records.json` (coordinator's correction). Aidan: 405 words, FK 6.3, Flesch 77.7. Adomnán: brief unchanged, 404 words, FK 7.3, Flesch 71.1. No brief or card sentence passes 25 words.

| Finding | Done |
|---|---|
| B-M4 / R2-1-M6 (Aidan: "see" heard as "sea") | Taken and reworded. GILES l.5763-5765 confirmed. The reviewer's "the seat of his bishopric" could mean Oswald's, so P2 reads "Oswald made Lindisfarne, an island at high tide, the seat of Aidan's bishopric." The card keeps "see". |
| R2-1-M7 (Aidan: "eighty years later" counted from the 630s) | Taken and reworded. GILES l.15189-15191, 15317-15318 and 7003-7004 confirmed. P2 reads "…Bede, who wrote some eighty years after his death, learning from those who knew him." This is two words shorter than the reviewer's text, to make room for "Aidan's" and stay at 405. ", which Bede calls Hii," was dropped from P2 as suggested; card `place` keeps it. |
| R2-1-M5 (Adomnán card traces 4: 28 words; White without context) | Taken as worded. WHITE l.3763-3768 confirmed (Aedh "bishop of Sleibte (Sletty)"). Records: an Aedh claim was added. |
| R2-1-M8 (Adomnán card: Lebar Brecc dates and context) | Taken and reworded. Antiphonary of Bangor l.17717-17719 and HUY l.1684-1685 confirmed. The reviewer's "manuscript printed by Whitley Stokes" would say Stokes printed the manuscript, when he printed only the note. Traces 5 now reads "A note in the Lebar Brecc, a late medieval Irish manuscript, counts Adomnán's rule, not to slay women, among four rules of Ireland. Whitley Stokes prints it." `uncertain` 3 adds the Antiphonary's date as worded. The Antiphonary volume was added to `sources.about`, with no author, since Warren's name is not on the held title page. |

## R2 changes, part 2: era 4 batch 1 (Dhuoda, Nennius)

Every cited line was opened in context before the change. The audio scripts were rebuilt by script, and each equals its brief once the two tags are removed. Every quotation in both briefs and cards was re-checked against its file by script. The scratchpad records were rebuilt by script (`work/build_*.py`), with every quotation pulled as exact text from its lines. No sentence in either brief or card runs past 25 words. Boniface and Alcuin were not touched.

| Finding | Done |
|---|---|
| R2-D-B1 (Dhuoda P5: second condition cut off from the prayer) | Taken as worded. DHU l.10106-10112 confirmed. "pacem et concordiam, si fieri potest, cum omnibus" gives "peace with all, if it could be", and "ad regnum, si jubet, faciat pervenire supernum" gives "heaven, if God willed". Both clauses are now inside "pray often that God would give his father…". I tried keeping "after this life" (post expletum vitae praesentis), but it ran the sentence to 30 words. The records claim already quotes the full Latin, so it needed no change. Brief: 402 words. |
| R2-D-M1 (card `dates`: "its") | Taken as worded: "reckons from the book's closing note that she began it on 30 November 841" (l.13224-13229). |
| R2-D-M2 (notes: "dead before 813") | Taken: "a Dodana dead by 813" (l.620-627). |
| R2-N-M1 (card `uncertain` 3 and contested claim: 809 is the editor's year) | Taken as worded. ANN l.3102-3103 (the annal year only) and l.3114 (the editor's margin) confirmed. The records' contested side now reads "in the editor's 768 … in the editor's 809". |
| R2-N-M2 (card `remembered` 2: later than what) | Taken as worded. ANN l.1084-1086 confirmed: Badon "is noticed by two contemporaries, Gildas and Taliesin", and l.1101 says the author of Nennius "lived at a later period". The records claim now quotes l.1085-1087. |
| R2-N-M3 (notes: Elbodug linked to Giles) | Taken as worded. The link to Giles is dropped. |

**After R2.** Dhuoda: 402 words, about 2:29, FK 7.1, Flesch 75.5. Nennius: 340 words, about 2:06, FK 6.6, Flesch 70.0.

**Process note.** Before the coordinator's correction arrived, the repo `records.json` was written once by script, with only the `dhuoda` and `nennius` entries replaced. `git diff` shows only three changed lines, all in the `nennius` entry. A script check confirms both entries in `records.json` equal the scratchpad `records/<id>.json`, which remain the source.
