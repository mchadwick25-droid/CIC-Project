# Card check: Francis of Assisi

Card checker, batch 8 (2026-11-21), under `Card_Check_Prompt.md`. Read: `francis-of-assisi.brief.txt` (and `brief.v1.txt`, to see what the final brief dropped), `francis-of-assisi.card.json`, `Card_Edits.md`, `Outline.md`, and each quoted line in its file. There is no starting card: Francis has no census entry yet.

**Verdict: FIX** (six changes to `briefReferences`, below).

## 1. Each field is justified

Every field was checked against the evidence `Card_Edits.md` gives. Spot re-reads at the cited lines:
- datesNote: Robinson's note that the Testament was "published a few days only before his death", from Quo elongati (ROB 5266-5269); Celano's death date, Sunday the fourth of October 1226 (CEL 4009-4010). Both stand.
- legacy.traces[0], "Gregory had known Francis": Quo elongati speaks of "longa familiaritate, quam idem confessor Nobiscum habuit" and of his help in writing the Rule and having it confirmed (SPECL 31910-31914). It stands.
- legacy.remembered[0], Jacques de Vitry as bishop of Acre, October 1216: the letter's heading is dated "Octob. 1216" and he signs as "Acconensis ecclesie minister humilis" (JDV 5856, 5861). He tells his journey towards Genoa in the same letter ("iter arripui versus Januam", JDV 6033). It stands.

## 2. Nothing else moved

Not applicable: new card, no starting card. No conflict with an existing entry, since there is none. The four differences from the tradition entry `the-franciscan-movement` that `Card_Edits.md` lists are differences of the tradition entry, not of this card, and the card's wording is the one its sources support.

## 3. References

The final brief dropped two things the references still name: "the year he died" (v1, paragraph 3) and "where the order began" (v1, the death line). Other references carry source details the brief never told. Seven entries in all name something the brief does not tell.

**FIX 1.** `briefReferences[0]`
- Old: "Testament, opening, Latin text in the Quaracchi edition and Robinson's English: the Lord led him among the lepers and showed mercy through him; what had seemed bitter turned to sweetness of soul and body; afterwards he waited a little and left the world. Dictated in 1226, a few days before his death, by Robinson's note on Gregory IX's bull."
- New: "Testament, opening, Latin text in the Quaracchi edition and Robinson's English: the Lord led him among the lepers and he showed mercy to them; what had seemed bitter turned to sweetness of soul and body; afterwards he waited a little and left the world. Dictated in 1226."
- Why: the brief says "I showed mercy to them", not through him (and the Latin is "feci misericordiam cum illis"). The brief no longer says he dictated it in the year, or days, before his death.

**FIX 2.** `briefReferences[1]`
- Old: "...he took off his clothes, said nothing, and the bishop covered him with his own mantle; he washed the lepers' sores."
- New: "...he took off his clothes and the bishop covered him with his own mantle; he washed the lepers' sores."
- Why: the brief does not tell that he said nothing.

**FIX 3.** `briefReferences[3]`
- Old: "Celano, First Life: at the Portiuncula, the church of Saint Mary, he heard the Gospel in which Christ sends out his disciples with no gold, no scrip and no shoes, put off his shoes and staff, and took one tunic."
- New: "Celano, First Life: at the Portiuncula, the church of Saint Mary, he heard the Gospel in which Christ sends out his disciples with no gold, no scrip and no shoes, and put off his shoes."
- Why: the brief tells only the shoes, not the staff or the one tunic.

**FIX 4.** `briefReferences[8]`
- Old: "...the Rule and these words to be understood simply and purely, without glosses."
- New: "...the Rule and these words to be understood simply, without glosses."
- Why: the brief says "read simply, without notes"; it does not tell "purely".

**FIX 5.** `briefReferences[12]`
- Old: "Francis's form of life and last wish for Clare's sisters, in Robinson's Writings and in Clare's Rule: they are to live always in poverty. Clare's Rule is in the bull Solet annuere of Innocent IV."
- New: "Francis's last wish for Clare's sisters, in Robinson's Writings and in Clare's Rule: they are to live always in poverty. Clare's Rule is in the bull Solet annuere of Innocent IV."
- Why: the brief tells his last wish only, not the form of life.

**FIX 6.** `briefReferences[13]` and `briefReferences[14]`
- [13] Old: "Mirror of Perfection: told by a physician that he would die, he said Welcome, my Sister Death, had Angelo and Leo sing the Canticle, and added verses on Sister Death before its last verse. The Mirror's date and author are contested."
- [13] New: "Mirror of Perfection: told by a physician that he would die, he said Welcome, my Sister Death, had Angelo and Leo sing the Canticle, and added a verse on Sister Death. The Mirror's date and author are contested."
- Why: the brief says "he added a verse"; it does not tell its place in the song.
- [14] Old: "Celano, First Life: he died in October 1226 at the Portiuncula, in the city of Assisi, where he first planted the Order of Lesser Brethren."
- [14] New: "Celano, First Life: he died in October 1226 at the Portiuncula, in the city of Assisi."
- Why: the final brief cut "where the order began".

References kept as they stand: [2], [4], [5], [6], [7], [9], [10], [11]. Each names what the brief tells, or the source a told claim comes from (Jacques de Vitry, Honorius III, Bonagratia, Ugolino, Bonaventure's dates for "a generation later"). [13] keeps Welcome, my Sister Death without quotation marks; those words stand verbatim in the brief, so marks would also be allowed.

## 4. Census rules

Only allowed keys; no `briefLength`. The brief has four quoted spans (paragraphs 1, 13, 21 and 23) and the card has four entries, one each, each `modern` word for word as the brief has it. Each `printed` stands at its lines (re-read): ROB 5368-5374 (the scan's stray "/" after "and I" and "*" after "to them." fold away); OPU 2577-2578; SPEC 8979; ROB 8663-8666. Each `original` stands: SPECL 27500-27501 "Bene veniat soror mea mors" (the "%3" after it is a stray note mark); SPECL 27258-27259, the death verse. Every cited file is in `sources`. No quotation marks in `briefReferences`. No audit, review or ruling named. American spelling; "amongst" is inside Robinson's printed wording. The three spans of six words or more carry no `secondReading` yet, as the new-card prompt asks; the four-word span has "checked at card".

**Checked at card: "Welcome, my Sister Death,".** "Bene veniat soror mea mors" is "Welcome, my sister death": the rendering is right, and Evans prints the same words (SPEC 8979).

## 5. Originals

- Quote 1, the Testament. The outline renders it from the Quaracchi Latin (OPU 2823-2830). The card leaves the Latin out. That is right under the batch 6 originals ruling. The scan reads "inihi" for mihi (OPU 2823), and no held print confirms the reading: Celano's Latin quotes only the part from "Quia cum essem" (CELL 7373-7377, itself faulty), and Robinson's note prints only "feci misericordiam cum Mis". The "(a)" and "(1)" marks are stray note marks, but "inihi" is not. Not a FIX.
- Quote 2 prints the Latin itself. Quote 3's death verse carries Sabatier's Italian. "poskappare" stands twice in Sabatier's print of the Assisi text (SPECL 27259 and 27693), so it is the print's own diplomatic reading, not a scan fault; the outline's "pò skappare" is a normalization. The card's entry credits both and the other manuscripts. It stands.
- "Welcome, my Sister Death" carries its Latin. Nothing is missing.

## 6. Not found, and anything clearly wrong left in

- `Card_Edits.md` reports no unsupported claim, and one search that found nothing: no held text says in those words that the Portiuncula lies near Assisi. Ruling: no change. The card's `placeNote` already says Celano puts it in the city of Assisi; the brief's "near Assisi" is the brief's, not the card's.
- Nothing else in the card is clearly wrong.
