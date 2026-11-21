# Card check: Cyprian of Carthage (`cyprian-of-carthage`)

Batch 7, 2026-11-20. Card checker; I wrote neither the card nor the brief. New card: every field was checked against its evidence in `Card_Edits.md` and against the entry's own fields. I re-opened each cited line in its file. The validator was not run.

**Verdict: FIX** (4 changes below).

## 1. Each field against its evidence

Confirmed at the cited lines: `otherNames`; `knownFor`; `datesNote` (ANF 27511-27526, BEN 2628 and 4272-4290, EUS 39310 note, 39406-39423, KNOPF 4822-4829, 4850-4857, 4882, 4955-4956, NPNF3 36798-36800); `placeNote` (KNOPF 4917, 4950-4952); `role`; `keyWorks` (UNIT 341-355, MORT 584-588); `legacy` (AUG 11416, 11949, 11588, 11626; MIGNE 99222-99226; MORIN 17206-17212; PROC 2206-2216; Sulpicius 2657-2661; L7 4474; NPNF3 40820-40821; ANF 27669-27672, 28277-28286); `uncertain` items 1-13 and 15. No field contradicts the entry's `sourcing`, `voices`, `legacy`, `why`, `floorNote`, `relationsSummary`, `dates` or `placeLabel`.

Wrong as left in:
- **Who wrote three notes.** The card gives to "the Edinburgh editor" three notes that stand in square brackets, which in this volume are Coxe's, the American editor's (Source_Sheet, ANF entry): the 251 date of On the Unity and "falsifying interpolations, long since exposed" (ANF 42105-42115, "[Written a.d. 251 ... Elucidation I.]"), and "[He was the first of the province, that is.]" (ANF 28280). The introduction at ANF 27511-27526 is the Edinburgh editor's, as ANF 27508 says: FIX 2.
- **Paul of Concordia** (`uncertain[13]`). The card follows Richardson's English, that Paul had been Cyprian's secretary. Jerome's Latin says Paul, as a very young man, had seen Cyprian's aged secretary at Rome: "senem qui se beati Cypriani, jam grandis aetatis, notarium, cum ipse admodum esset adolescens, Romae vidisse diceret" (JERL 55620-55622, read through the scan's "eíalis" and "Rome"). The Tertullian card of this batch reads it the same way, with Heurtley's Kaye (VIN-ed 13543-13545). The card's own "two removes" only fits the Latin: FIX 1.
- **Procopius** (`legacy.traces[2]`). "In 533 Procopius wrote" makes 533 the year of writing. 533 is the year he is telling (PROC 1366, "[533 A.D.] In the seventh year of Justinian's reign"); no held source gives 533 as the year he wrote: FIX 3.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. References

One part of one entry names something the brief does not tell: chapter 5's sun, tree and spring (FIX 4; the brief gives only the mother who bears and feeds). Remaining, all told in the brief: Pontius on the crowded doors, the older men, the admirer, the withdrawal, the plague, the refuge refused, the eyes bound; Pontius on the first martyr bishop; Letter 20; Letter 8; Letter 44; On the Unity 6 and 5 (after FIX 4); On the Mortality 16; Letter 74; Letter 75; the Opinions of the Bishops; the Acta of 257 and 258; Letters 80 and 81; Augustine, On Baptism; the tradition.

## 4. Census rules

Keys allowed; no `briefLength`; no `secondReading`. Eight spans in the brief, eight entries, none for a span the brief no longer quotes. Every `printed`, `original` and `englishPrinted` stands verbatim at its lines, and every cited file is in `sources`. No quotation marks in `briefReferences`. No audit, review or ruling named. American spelling (clamor, honor, traveler).

## 5. Originals, ruled under the batch 6 rule

All Latin; no Greek on this card.

| # | Span | Ruling |
|---|---|---|
| 0 | less than plainly and faithfully | **Keep as it stands.** EP 2967-2968 "minus simpliciter et minus / fideliter" is clean ("UODIS" falls after the span). |
| 1 | Church as mother | **Keep as it stands.** UNIT 364-365 clean. |
| 2 | the plague's questions | **Keep as it stands.** MORT 586-588 clean. |
| 3 | bishop of bishops, the full line | **Keep as it stands.** SENT 140-142 clean. |
| 4 | a Christian and a bishop | **Keep as it stands.** KNOPF 4828-4829 clean; GEB 6489-6490 agrees ("Öyprianus" falls before the span). |
| 5 | Thanks be to God | **Keep as it stands.** KNOPF 4911 clean; GEB 6625 agrees. |
| 6 | bishop of bishops | **Keep as it stands.** SENT 140 clean. |
| 7 | What could be more kind? | Augustine's English only; no Latin of On Baptism is held for the card. Stands. |

The damaged Hartel scan (H3) is rightly used for no quotation.

## 6. Not-found claims

All upheld: Facundus (entry `legacy`) is on no held source the sheet names; Ep. 15.4 is about letters of peace, and the card rightly takes the certificates from LAPS 1028-1029; Sulpicius's traveler wished to worship at the tomb (npnf211 2657-2661), not that he did; Stephen's death in 257 is given as the editor's reckoning.

## FIXes

**FIX 1.** `uncertain[13]`
- Old: `comes from Jerome, who had it from an old man, Paul of Concordia, who said he had been Cyprian's secretary as a young man. It is hearsay at two removes,`
- New: `comes from Jerome, who had it from an old man, Paul of Concordia, who said that as a very young man he had met Cyprian's aged secretary at Rome. Jerome's Latin says so; the English translation wrongly makes Paul himself the secretary. It is hearsay at two removes,`
- And add to `sources.about`: `{"title": "Lives of Illustrious Men, ch. 53, on Tertullian (Migne, Patrologia Latina 23)", "author": "Jerome", "date": null, "language": "Latin", "file": "cic/texts/jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt"}`

**FIX 2.** Coxe's bracketed notes, four places.
- `datesNote` old: `and On the Unity of the Church 251 by the Edinburgh editor.` New: `and On the Unity of the Church 251 by A. Cleveland Coxe, the American editor.`
- `keyWorks[1].about` old: `in 251 by the Edinburgh editor's dating.` New: `in 251 by Coxe's dating.`
- `uncertain[7]` old: `and the Edinburgh editor calls them falsifying interpolations long since exposed.` New: `and Coxe, the American editor, calls them falsifying interpolations long since exposed.`
- `legacy.remembered[0]` old: `the Edinburgh editor adds that he was the first of the province.` New: `Coxe, the American editor, adds that he was the first of the province.`

**FIX 3.** `legacy.traces[2]`
- Old: `In 533 Procopius wrote that Cyprian, a holy man,`
- New: `Telling of the year 533, Procopius wrote that Cyprian, a holy man,`

**FIX 4.** `briefReferences[5]`
- Old: `chapter 5, the sun, the tree and the spring.`
- New: `chapter 5, the one mother from whose womb Christians are born and by whose milk they are fed.`
- Evidence: UNIT 352-353 ("una mater ... illius fetu nascimur, illius lacte nutrimur").

No further change. (The entry's `teaser` states two years from baptism to bishop as fact; the card rightly gives it as a modern reckoning, and the conflict is listed in `Card_Edits.md`.)
