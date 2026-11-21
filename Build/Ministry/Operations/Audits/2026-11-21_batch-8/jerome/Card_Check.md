# Card check: Jerome

Card checker, batch 8 (2026-11-21), under `Card_Check_Prompt.md`. I wrote neither the card nor the brief. Read: `jerome.brief.txt` (and `brief.v1.txt`), `jerome.card.json`, `Card_Edits.md`, the census entry `jerome` (no card), and each cited line in its file. New card: every field was checked against its evidence and against the entry's `sourcing`, `voices`, `legacy`, `why`, `floorNote`, `relationsSummary`, `dates` and `placeLabel`. The validator was not run.

**Verdict: FIX** (three changes below).

## 1. Each field against its evidence

Re-read and confirmed: PRO 53895-53903 (dies in his ninety-first year, "prid. kal. Octobris", 30 September); JR 41786-41789 (born 331, died 420; Strido; the fourteenth year of Theodosius); JW 2549, 3445-3448 (born 345, dies 20 September 420); CIV 36730-36740 (the presbyter Jerome; Schaff's note, died 419); JW 2691, 2776, 2846, 2929, 8591-8592, 46629; JW 46735-46741 (begun about 391, finished about 404); JW 47291-47299 (the three stages, 390 to 404); JW 47354-47359 (Gallican Psalter, 1566); JR 41809-41812 (the manuscripts that have or omit "the Old Testament from the Hebrew"); JW 19006-19013 (Baraninas); JR 49452-49465, 50306-50310 (Barabbas); JR 46247-46262 (close friends, estranged over Origenism, reconciled before 397); ISI 13114-13119; TRE 12392-12394 (8 April 1546), 12468-12481, 4170-4176; SUL 2889-2900, 2949-2962; PAL 435, 1221-1224; AUGL 20546-20561; AUG 54030-54040 (Letter 195, 418).

One statement misreports its sources (FIX 1). `uncertain[1]` says the sources differ "by a day or a year" for his death. Prosper gives 30 September 420 (PRO 53901-53902), Fremantle 20 September 420 (JW 3447), Schaff 419 (CIV 36737): ten days or a year.

One statement misreports the Latin (FIX 2). `quotationOriginals[2].uncertain` says the brief follows the Latin, "whose order puts the Greeks' outcry first", and that Cunningham keeps that order. The Latin begins with the uproar, "factus est tantus tumultus in plebe maxime Graecis arguentibus" (AUGL 20553-20554), and Cunningham too begins "such a tumult in the congregation, especially among the Greeks" (AUG 32547-32548). It is the brief that puts the Greeks first.

No conflict with the entry's fields. `why`'s "in the work later called the Vulgate" is qualified, not contradicted, by the card's note on the Psalter and the decree. `floorNote` and the attack on Jovinian have no cited held line and are rightly not claimed. `voices` and `relationsSummary` (the friendship and the break over Origen, the letters to Augustine) agree. The four birth and death dates are each credited; the entry's `dates` ("374-420") is untouched.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. References

None names something the brief does not tell. The final brief dropped "Christian brother" and "They ended as allies"; no reference names either. Remaining: [0] Letter 125, fasting, the brother who had been a Jew, the cost to a scholar of Quintilian and Cicero (the print's names for the brief's "Rome's great Latin writers"); [1] the Old Testament from the Hebrew, the old Latin from the Greek, Trent; [2] the Gospels preface and the many forms; [3] Letters 45, 39 and 108, the women, the funeral crowd and the Tiber, the accusation and retraction, August, Bethlehem; [4] Paula's questions and Hebrew, Palladius, the prefaces from about 391; [5] Augustine's plea and the Septuagint, Rufinus, Origen and the charge; [6] Oea, the Jews' testimony, the correction; [7] the plant, the refusal in church, 418; [8] 420, Isidore, Trent 1546; [9] about 411. No quotation marks in any.

## 4. Census rules

Only allowed keys; no `briefLength`. Five quoted spans in the brief, five entries, each `modern` word for word; none for a dropped span (v1 had the same five, the Oea one reworded). Each `printed` and `original` stands at its lines by the fold rule. Every cited file is in `sources`. No audit, review or ruling named. One British spelling, "traveller", outside printed wording (FIX 3). The four long spans have no `secondReading` yet, as the new-card prompt asks.

**Checked at card: "old and Vulgate edition".** Waterworth prints "the said old and Vulgate edition" (TRE 12478). The Latin decree is not held, so the English print stands alone, as the card says. Right.

## 5. Originals

The Oea span carries Goldbacher's Latin, clean at AUGL 20553-20556. No Latin of Jerome's letters to Rusticus or of Rufinus's Apology is held (searched `cic/texts/`; PL23 part 1 has neither passage), so the other three long spans rightly carry English alone. Greek: none. Nothing missing.

## 6. Not-found claims

All upheld: `floorNote`'s Nicene defense; Marcella; Ildefonsus continuing the list; the teachers Didymus, Gregory and Apollinaris as a card claim. The note that the letter headings do not settle Augustine's rank in 394 or 395 is for the story's owner, not the card.

## FIXes

**FIX 1.** `uncertain[1]`
- Old: `by a day or a year for his death.`
- New: `by ten days or a year for his death.`

**FIX 2.** `quotationOriginals[2].uncertain`
- Old: `The brief follows the Latin, whose order puts the Greeks' outcry first, as the cause of the uproar and of the summons; Cunningham's English keeps that order.`
- New: `The brief puts the Greeks' outcry first, as the cause of the uproar and of the summons; the Latin and Cunningham's English name the uproar first, with the Greeks inside that sentence.`

**FIX 3.** `legacy.remembered[0]`
- Old: `the traveller Postumianus`
- New: `the traveler Postumianus`
