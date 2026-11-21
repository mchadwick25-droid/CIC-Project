# Card check: Pontius the Deacon

Card checker, batch 7, 2026-11-20, per `Card_Check_Prompt.md`. Checked `pontius-the-deacon.card.json` against `Card.existing.json` (identical to the census `card`), `Card_Edits.md`, the brief and the held files. Short names as in `Card_Edits.md` (VE, VL, HAR, DEL, MON, BEN, SHK, EP, KNOPF, JE).

**Verdict: FIX** (seven reference changes, below), and three scan readings to list.

## 1. Each edit is justified

- `legacy.traces` (Cheltenham list, 23 manuscripts): HAR 259-263. `legacy.remembered[1]`: HAR 1909-1910 ("die älteste christliche Biographie, die wir besitzen").
- `uncertain[4]` to `[13]`, each re-read at its lines: name and office (HAR 331-341; SHK 31627-31630; DEL 3936-3942); kind of book (HAR 1909-1910; MON 11030-11032; DEL 4077-4102; SHK 31630-31633; DEL 4312-4320); eyewitness (SHK 31630-31631; DEL 4264-4277); the dream (VE 28096-28131; HAR 1379-1380, 1335-1337); the withdrawal (EP 17370-17373); what he left out (DEL 4166-4170; HAR 2086-2093; MON 11092-11103); preface (VE 27709-27712; VL 40364; HAR 589-591); court record (VE 28001-28003; HAR 1829-1833; SHK 31636-31641); style (BEN 27383-27385; DEL 4297-4299); Jerome's date (JE 38785, note "a.d. 492"; JE 15402, Theodosius named Augustus 19 January 379). All hold. Where sources differ, each is credited.
- `sources.about`, seven added: each is cited by a quote entry or a reference.
- Clearly wrong: none claimed, and I found none.

## 2. Nothing else moved

Diffed field by field. Only additions: `legacy.traces`, `legacy.remembered[1]`, `uncertain[4]` to `[13]`, `sources.about[1]` to `[7]`, `briefReferences`, `quotationOriginals`. Every existing field is word for word.

## 3. References

Remaining after the fixes: (1) Life 1, the people and the earlier martyrs; (2) Jerome 68; (3) Harnack, author unnamed, Cheltenham list, oldest biography; (4) Life 1 and 2, aim and baptism; (5) Life 10 and 11 with the scholars, what is told and left out; (6) Proconsular Acts and Benson, 257, Curubis, 14 September 258; (7) Life 12, the willing exile and the dream; (8) Life 13 with Harnack, the day as a year; (9) Life 14 and 15 with Letter 81; (10) Monceaux and Delehaye, kind of book; (11) Life 19, the ending; (12) no early source on his death; (13) census, his tradition. No quotation marks in any.

Parts that name something the brief does not tell:
- [0] "though his living words are silent". FIX 1.
- [1] "notable": Jerome's judgment; the brief does not give it. FIX 2.
- [2] "23": the brief says only that the book was copied with Cyprian's writings. FIX 3.
- [5] "30 August": the brief gives only the year. FIX 4.
- [7] "and the delay as church business": the brief tells only the day read as a year. FIX 5.
- [9] "modeled on the Passion of Perpetua": the brief says only a blend of biography and praise. FIX 6.
- [11] Richardson's 260 and Coxe's martyrdom: the brief says only that no early source tells his death. FIX 7.

## 4. Census rules

Keys allowed; no `briefLength`. Four quoted spans in the brief, four entries, each `modern` the brief's span exactly; no stale entry. Every `printed` stands at its VE lines. Every cited file is in `sources`. No audit, review or ruling named. American spelling throughout ("labors", "honored", "defense", "modeled"). No `secondReading`: correct, all four are new.

## 5. Originals (ruled against `2026-11-19_batch-6/Batch_Originals_Ruling.md`)

The outline renders all four from the Latin, and the card carries all four. No Greek in this card.

- **[0] "exulem uoluntarium" (VL 41015): KEEP as it stands.** Clean. HAR 1299 agrees.
- **[1] the dream (HAR 1309-1313): KEEP, with one reading.** The only fault is "volebatintellegi" (HAR 1311), a dropped space. Hartel's print confirms the word division (VL 41027-41028, "uolebat" / "iutellegi", the line break dividing the words). "senten-/tiam" is a hyphen join. The rest is clean. HAR is the right choice over VL, whose scan reads n for u throughout this passage.
- **[2] the preface (VL 40267-40270): KEEP, with one reading.** "in lo" (VL 40269) is the margin line number 10 run into the line: a stray mark. The rest is clean. Harnack prints the same words (HAR 459-462), and his note at HAR 448 confirms that he strikes the further clause, as the entry's `uncertain` says.
- **[3] the ending (VL 41405-41410): KEEP, with one reading.** "plus 5" (VL 41409) is the margin line number 5: a stray mark. "trium-/phabo ?" is a hyphen join. HAR 1806-1813 gives the same words, with the colon after sententia that the `uncertain` records.

Each reading was applied in the validator's way and the wording then checked with its folding: all three stand. For `tools/quote_scan_readings.json`:

```json
{
 "file": "cic/texts/harnack_vita-cypriani-commentary-lat-deu_1913.txt",
 "lines": "1311",
 "scan": "volebatintellegi",
 "reads": "volebat intellegi",
 "kind": "OCR dropped a space; Hartel's print divides the words (cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt, lines 41027-41028)"
},
{
 "file": "cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt",
 "lines": "40269",
 "scan": "documentum in lo",
 "reads": "documentum in",
 "kind": "line number run into the line"
},
{
 "file": "cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt",
 "lines": "41409",
 "scan": "exulto, plus 5",
 "reads": "exulto, plus",
 "kind": "line number run into the line"
}
```

## 6. Not found, and anything clearly wrong left in

- Existing `uncertain[3]`, "Archbishop Benson rejects that view and follows Pontius": found. BEN 2901-2907 (two-column scan, read across the columns): Ritschl "conceives that the Horti must have been confiscated later and that Pontius mistakes this for charitable sale", and Benson answers that "Pontius' personal knowledge seems to present to him no difficulty". It stands.
- "About 130 years later" (brief) and `uncertain[13]`: no held source states 392, but it follows from JE 38785 with JE 15402 (379 plus thirteen years). The entry says this openly and credits the note's "492". It stands.
- Nothing else clearly wrong was found.

## FIX

**FIX 1.** `briefReferences[0]`
- Old: `The Life and Passion of Cyprian 1, tr. Ernest Wallis: Cyprian's people want to hear everything about him, though his living words are silent; earlier Christians recorded the sufferings of martyrs who were ordinary believers in great detail, so the death of so great a bishop should not be passed over.`
- New: `The Life and Passion of Cyprian 1, tr. Ernest Wallis: Cyprian's people want to hear everything about him; earlier Christians recorded the sufferings of martyrs who were ordinary believers in great detail, so the death of so great a bishop should not be passed over.`

**FIX 2.** `briefReferences[1]`
- Old: `Jerome, Lives of Illustrious Men 68: Pontius, Cyprian's deacon, shared his exile until the day of his death and left a notable volume on his life and death; Jerome's list ends in the fourteenth year of the Emperor Theodosius.`
- New: `Jerome, Lives of Illustrious Men 68: Pontius, Cyprian's deacon, shared his exile until the day of his death and left a volume on his life and death; Jerome's list ends in the fourteenth year of the Emperor Theodosius.`

**FIX 3.** `briefReferences[2]`
- Old: `Harnack, Das Leben Cyprians von Pontius (1913): no manuscript and not the Cheltenham list names the author; the Life stands at the end of Cyprian's works in the Cheltenham list of 359 and is held in 23 manuscripts; the oldest Christian biography that survives.`
- New: `Harnack, Das Leben Cyprians von Pontius (1913): no manuscript and not the Cheltenham list names the author; the Life stands at the end of Cyprian's works in the Cheltenham list of 359 and is held in manuscripts; the oldest Christian biography that survives.`

**FIX 4.** `briefReferences[5]`
- Old: `The Proconsular Acts of Cyprian, in Knopf, Ausgewählte Märtyrerakten: the hearing of 30 August 257, the governor's sentence of exile to Curubis, and the death on 14 September 258. Benson: Curubis, a small coast town.`
- New: `The Proconsular Acts of Cyprian, in Knopf, Ausgewählte Märtyrerakten: the hearing of 257, the governor's sentence of exile to Curubis, and the death on 14 September 258. Benson: Curubis, a small coast town.`

**FIX 5.** `briefReferences[7]`
- Old: `The Life and Passion of Cyprian 13, with Harnack: Pontius reads the day as a year and the delay as church business; Harnack finds this unconvincing.`
- New: `The Life and Passion of Cyprian 13, with Harnack: Pontius reads the day as a year; Harnack finds this unconvincing.`

**FIX 6.** `briefReferences[9]`
- Old: `Monceaux and Delehaye on the kind of book the Life is: a speech of praise, and a blend of biography and praise modeled on the Passion of Perpetua.`
- New: `Monceaux and Delehaye on the kind of book the Life is: a speech of praise, and a blend of biography and praise.`

**FIX 7.** `briefReferences[11]`
- Old: `Jerome and the editors' notes in Ante-Nicene Fathers 5 and Nicene and Post-Nicene Fathers 3: Richardson gives about 260 and Coxe says a martyr, each without a source; no early source says how or when Pontius died.`
- New: `Jerome and the editors' notes in Ante-Nicene Fathers 5 and Nicene and Post-Nicene Fathers 3: no early source says how or when Pontius died.`
