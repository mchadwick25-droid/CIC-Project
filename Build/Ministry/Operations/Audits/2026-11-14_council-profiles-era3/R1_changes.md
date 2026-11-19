# Council profiles, era 3: changes after review round 1 (2026-11-14)

The answer to `R1_review.md`. Every substantial finding is fixed. Minor findings are fixed, or left with a reason given. After the changes every brief was rescored with `grade_text`, and every audio script was regenerated from its brief. No paid calls were made.

| Council | Words | FK | FRE |
|---|---|---|---|
| second-council-of-constantinople-553 | 400 | 8.15 | 60.22 |
| third-council-of-toledo-589 | 400 | 7.01 | 68.71 |
| council-of-dvin-609 | 371 | 7.67 | 61.77 |

## Substantial

| Finding | Change |
|---|---|
| CON-1 | Brief: the Persia paragraph is now Labourt's reading, by name: "Jérôme Labourt, a French historian of the Persian church, reads the creed of its synod of 585 as an answer to the council's backers." Entry: the Church of the East is now Affected; its note, `outcome` and `record` say the Theodore canon names no council and that Labourt takes it as aimed at Henana's followers. Labourt is added to `record` (modern reconstruction) and `sources.writtenLater`; `records.json` gains his claim and a contested claim on whether the synod answered the council. |
| CON-2 | The false absent detail is removed. Michael the Syrian is added to `record` (later narrative, Syriac Orthodox, twelfth century), `sources.writtenLater`, `attended`, `outcome`, `uncertain` and the contested claims on Origen and on Vigilius's presence. `syriac-orthodox-west-syriac-christianity` is added as Affected. |
| DVN-1 | Brief: "Kyrion's own words reach us only through James Issaverdens, a priest of the Armenian Catholic monastery of San Lazzaro in Venice, writing in 1875. He praises Kyrion's learning and piety." The "only through his foes" sentence is gone. Entry: Issaverdens's side is given in `record` (Mekhitarist, favourable to Kyrion; Ormanian for the house's Catholic founding), and `uncertain[0]` is reworded. |
| DVN-2 | Brief: "Stephen names no council and gives no year" closes paragraph 1, and paragraph 3 says "Of the writers drawn on here, only modern ones tell of a synod at Dvin." "Then called" is now "called". `uncertain[0]` names the modern writers and their years. |
| DVN-3 | Entry `uncertain[4]`, `record` and the contested claim now say the editors date the letter 601 and place it in the eastern, Pontic Iberia rather than Ireland or Spain, without naming Kyrion. The letter is added to `record` and `sources`. It is not used in the brief: it concerns receiving Nestorians, not the break, so it bears on neither the brief's witness sides nor its date. |

## Minor

| Finding | Change or reason |
|---|---|
| CON-3 | The quotation marks are dropped: "Vigilius was in the city, but refused the emperor's repeated calls to come." The records claim names Hefele's digest. Paragraph 3's paraphrase is already without quotation marks; the entry's `record` notes the digest. |
| CON-4 | The records claim is now Widely Accepted, with Victor as the dissent, and Michael the Syrian added. |
| CON-5 | "Vigilius died in Sicily, going home." |
| CON-6 | "The council's final sentence curses the Chapters: 'We therefore anathematize the Three Chapters.'" "Manuscript" in both places. |
| CON-7 | "Gregory the Great of Rome said he honoured a fifth council. But writing to Milan, he called it the synod 'called by many the fifth.'" The records add the Theodelinda context. The cap left no room to name the queen in the brief; the entry's `outcome` carries both letters. |
| CON-8 | "The council's acts survive, the record of the side that won, and are told here from English extracts." "Library" is gone from all three briefs. |
| CON-9 | `calledBy` now gives Hefele and Evagrius on Vigilius's consent, with a new contested claim, and the sentence's own wording. |
| CON-10 | `informalName` is "The Fifth Council". Pelagius II is added to `people` (LISTED). Gregory the Great is not: see TOL-6. `uncertain[3]` now says Justinian wrote to the council and sent his quaestor. |
| TOL-1 | The English renderings are out of quotation marks. Where the Latin is quoted it is the Latin, with the English after it outside the marks. |
| TOL-2 | Dalton's note is now applied to the king's speech at the council, in `decided`, `record`, `uncertain` and the contested claim. |
| TOL-3 | "Eutropius, abbot of Servitanum"; "Masona, bishop of Mérida". |
| TOL-4 | `attended[1]`: "The signed list has sixty-two bishops in person and five who signed through deputies … Two places in the printed text are damaged." |
| TOL-5 | Reccared's letter is added under `fromThoseThere` and `record`, with Barmby's doubt, and as a claim in `records.json`. |
| TOL-6 | One rule for all three councils: the Who click lists those who took part, those condemned, and those who acted on the council's decisions (summoned, exiled, confirmed or pressed them). Writers who only report the council are in `record` and `sources`. Gregory the Great is therefore removed from Toledo's `people` and not added to Constantinople's; Pelagius II, who pressed the Istrian bishops, is added; Euphemius of Toledo, who signed second, is added as NOT SCORED. Victor of Tunnuna stays, as one exiled for the Chapters. |
| TOL-7 | "in twenty-three articles" in the brief; the entry and records say the twenty-third is the closing subscription. |
| DVN-4 | Teaser and `shortName`: "Dvin, between 596 and 609". The brief adds: "Stephen and Issaverdens both set Abraham's quarrel in the reign of the emperor Maurice." `datesNote`, `uncertain` and the contested claim add Issaverdens's damaged year and Barmby's November 602 for Phocas. The id keeps 609, the year of the census and the councils scan, with the dispute in the entry. |
| DVN-5 | "Kyrion came to doubt what Stephen calls the orthodox faith." |
| DVN-6 | "No writer names the bishops or counts them"; "No other writer tells of that meeting"; "No record of the council survives among the books this account draws on". |
| DVN-7 | The brief now closes on Ormanian's "became part of the Greek Church". Brosset's line is in `outcome` with his date and his source, Chamich. |
| DVN-8 | `informalName` is left out: no held source names the council otherwise. |
| DVN-9 | Samuel of Ani is added to `record` (later narrative, Armenian side), with Brosset's judgment, and as a claim. |

## Scan corrections noted

For the councils scan and the Who scans, to go in the Open-Gaps entry: the Who scan has Stephen of Taron WANTED and not held, but his history is held in German (`stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt`); the scan's `aquileian-christianity` (census c. 340-410) is not used for Constantinople, being of the wrong era; Constantinople adds the Church of the East (Affected, through Labourt) and the Syriac Orthodox church (Affected, through Michael the Syrian).
