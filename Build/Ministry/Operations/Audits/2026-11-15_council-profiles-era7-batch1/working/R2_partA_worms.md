## Council profiles, era 7 batch 1, round 2: Part A (Diet of Worms 1521)

**Council.** `diet-of-worms-1521`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-worms-1521.brief.txt`, `audio/diet-of-worms-1521.audio.txt`, `diet-of-worms-1521.entry.json`, `records.json` key `diet-of-worms-1521` (105 claims, 10 contested claims, 9 absent details; identical to `working/records_diet-of-worms-1521.json`), and the Worms line of `README.md`. Scope: `git diff f1f6cd220 HEAD` on those files, checked against `R1_review.md` Part A and `R1_changes.md` Part A, including the worker's README edit (A-M11).
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm, at the ceiling). `grade_text`: FK 7.03, Flesch 67.90. Longest sentence 23 words ("In the Wartburg, Buchheim writes, ..."). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag. Checked by `diff`.
**Entry.** The JSON parses. No sentence in any entry string runs past 25 words (script check).
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. No repo file edited except this part. No model, network or paid calls.

Abbreviations as in round 1 (FOXE4, PALL1, MIRBT, TT, FP, WAT, SARPI, ARM, LV3, LHYM, ZINZ).

## Verdict: REVISE (one blocking, two substantial, three minor)

Every round 1 finding has been acted on, and every changed or added quote is verbatim or a fair repair of OCR. Most fixes are right. Three carry new errors, each from the round 1 fix wording itself.

The blocking point is the A-M3 fix. The brief now says Charles "read out" his paper. Pallavicino's verb is causative: Charles had it read (A2-B1).

The two substantial points:
- The new contested claim on the first hearing puts Sarpi on the "day after" side, but Sarpi gives no arrival date (A2-S1).
- The new `uncertain[2]` says the Table Talk "gives no speech before the Diet". It gives Luther's first answer to the emperor (A2-S2).

The three minor points:
- "printed by John Wesley" (the printer was R. Hawes);
- the Aleander absence note still lists its hits short;
- the README says the Edict is held, when only Mirbt's excerpt is.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| A-B1 | CLOSED, with new points | Brief p.5, `uncertain[2]` and records `contested_claims[0]` changed. The Table Talk is out of "Held tellings without it" in the records, and its "next day" (TT l.3563-3565, "The next day I was cited by the Bishops and others, who were appointed to deal with me touching my revocation") is right. ARM l.9309 "Hier flehe ich: ich kan nicht anders: Gott helfe / mir! Amen." is the only held "Hier ... stehe ich" (see Searches). But `uncertain[2]` overstates the Table Talk's silence (A2-S2), and "printed by John Wesley" is loose (A2-M1). |
| A-B2 | CLOSED | Brief: "Buchheim, an 1885 historian on Luther's side". FP l.95 "WITH THEOLOGICAL AND HISTORICAL INTRODUCTIONS", l.105-107 Buchheim, l.112-116 Lutheran Publication Society, 1885; l.126 "the fourth centenary"; l.2358 "a bigoted Roman Catholic at heart". "Historian" names the work he wrote in this book, and the side is derived from his own words. `datesNote` still calls him "an 1885 editor"; both are true of him, so no finding. The entry `record` note is right. |
| A-B3 | CLOSED | `decided[10]` now agrees with `uncertain[10]` and `contested_claims[7]`. ARM l.9403-9405 ("ublithed his Decree of, Banifhment againtt him, / ... jleander. the Pope's Legate ... / drawn"); PALL1 l.10448-10450 ("fece commettere all'Aleandro, che distendesse la contenenza del Bando") and l.10452-10453 ("riueduta e riformata in vari Consigli di Cesare"). "No held witness names another drafter": searched, holds (see Searches). |
| A-S1 | CLOSED | `issue[1]`: the emperor is the subject of the sending and of its aim. SARPI l.9743-9746 "he reſolved to ſend to fetch him by one of his Heralds, not to know / and judge the things that concern Faith, which belongeth to the Pope / alone, but to bring him into the. right way with good perſwaſions". The passage is Sarpi's report of the Edict (l.9718-9738). "Bring him back by persuasion" is a fair rendering. |
| A-S2 | CLOSED | `people`, `decided[5]`, records `claims[33]` and `[66]` all read "Dr. Voeus". FOXE4 l.22193 "Dr. Voeus, the marquis of Baden's chaplain"; l.22200 "That Luther was not called to be conferred with, or to disputation"; TT l.3598 "a Doctor unto me, belonging to the Marquis of Baden". "Spoke for the princes": FOXE4 l.22201-22202 ("the princes had procured license ... to exhort Luther"). No "Vehus" left in entry or records. |
| A-S3 | CLOSED, with a new point | The dispute is now named as the interval, and Foxe gives no calendar date for either hearing (FOXE4: only "April the 26th", l.22479, 22497, in l.21600-22540). Citations checked: WAT l.1724-1727 ("on the sixteenth of April ... on the follow / ing clay, the seventeenth of April, 1521"); ARM l.9150-9151 ("Me came thither, 4prid 16. / The next day"); PALL1 l.10012-10013 ("nel giorno immediato dopo l'arriuo, cioè a' 17 d'Aprile"). But Sarpi sits on a side he does not speak to (A2-S1). |
| A-S4 | CLOSED | Records `claims[14]`: MIRBT l.15509-15512 is Mirbt's summary ("Es folgen ... die Strafandrohungen für Luther selbst und seine Anhänger, falls sie nicht binnen 60 Tagen nach Veröffentlichung der Bulle ... Widerruf leisten"). Kind and wording right. |
| A-M1 | CLOSED | Brief p.2 and `uncertain[0]`: "prints part of its Edict, in German". MIRBT l.15588-15590. |
| A-M2 | CLOSED | Brief "a Jesuit whose 1664 history"; `uncertain[0]` "history of 1656-1657, revised in 1664". The held file is the author's 1664 revision, so "1664 history" is true of the text we hold. |
| A-M3 | CLOSED, with a new point | "Wrote" is gone, and the paper "in his own hand" is right ("di ſua mano ben lunga vn foglio", PALL1 l.10142). But "Charles read out" gives him the reading (A2-B1). |
| A-M4 | CLOSED | Brief p.2: "Foxe, a Protestant, gives Luther's speech in English, drawn from Melanchthon and others." FOXE4 l.22529 source note. 400 words. |
| A-M5 | CLOSED | "Lewis" in `attended[2]`, `decided[4]`, `people`, records `claims[35]`. SARPI l.9672. No "Louis" left. |
| A-M6 | CLOSED | MIRBT l.15629-15631 "m i t- / verwandten, anhengern, enthaltern, fürschiebern, gönnern / und n a c h V 0 1 g e r n": six words, six English words in order. Faithful. |
| A-M7 | CLOSED | `issue[8]`: FOXE4 l.22072-22073 "if I be not convinced by testimonies of the Scriptures, and by / probable reasons" verbatim. TT l.3565-3566 and l.3581-3582 give Scripture only. |
| A-M8 | CLOSED | "It was no church council." deleted. |
| A-M9 | CLOSED | `teaser` reworded; no doublet. |
| A-M10 | CLOSED | Through the A-B2 note: "put out on 25 May" (FP l.2518-2519 "promulgated on May 25"). |
| A-M11 | CLOSED, with a new point | The README no longer says "their own voices" or "the contested Edict date". But it says "The Edict is held in its German text" (A2-M3). |
| A-M12 | CLOSED, with a new point | LV3 l.293-294 sentence added. Held name forms are recorded: ARM l.3492-3493 "The LIFE of MARTIN LUTHER. / Written originally in' German, éy John Daniel Hernnfehmid"; PALL1 l.10213 "Riccardo Grieffeclau amico intimo di Federigo, mà buon / cattolico". New `claims[65]` is faithful to PALL1 l.10212-10214 ("Preſe la cura di perſuaderlo l'Arciueſcouo di Treueri"). But the hit list in `absent_details[3]` is still short (A2-M2). |

## New findings

### Blocking

**A2-B1. Blocking (an act given to the wrong doer, in the brief; from the A-M3 fix).**

Brief, paragraph 6: `Next morning, Pallavicino says, Charles read out a paper in his own hand.` Records `claims[60]`: "Charles read a paper in his own hand, a full sheet long, ...".

What Pallavicino says. PALL1 l.10137-10142: "La mattina proſſima Ceſare fè chiamar gli Elettori, / Principi in gran numero, addimandandoli, che lor pareſſe di / quell'affare. Chieſero eſſi indugio à riſpondere; e l'Imperadore allora ſoggiunſe, voler'egli prima eſporre l'opinion ſua: E « / legger vna ſcrittura di ſua mano ben lunga vn foglio" (OCR normalized; the held line has "£ «").
- "Legger" is an infinitive. It needs a governing verb, and the only token before it is a one-character OCR blob. The reading that fits is "E fè legger": he had a paper read.
- That is Pallavicino's own idiom on these pages. The same chapter has "lo fece leggere dal Grancancelliere ad alta voce" (l.10487) and "fece commettere all'Aleandro" (l.10448). Here, at l.10137, "fè chiamar" (had them called).
- On either reading, no held line has Charles reading the paper aloud himself. Buchheim has him "declared to the Diet — in a French document written in his own hand" (FP l.2466-2469), which does not say who read it.

Why it is blocking. It is a small detail, but it is an act told in the brief beyond its witness, and the round 1 fix introduced it ("wrote" was not right either; "read out" swaps one error for another).

Fix, brief paragraph 6, first sentence (one word shorter, so the brief comes to 399; 12 words):
`Next morning, Pallavicino says, Charles produced a paper in his own hand.`
"Produced" says no more than either witness: Pallavicino has the paper read, Buchheim has Charles declare it. The second sentence stands. The audio must be regenerated.

Fix, records `claims[60]`: "Charles had a paper in his own hand read to the electors and princes (held OCR 'E « legger', read as 'E fè legger'), a full sheet long, later read in consistory at Rome. He would hear Luther no more and would proceed against him 'come notorio eretico'".

### Substantial

**A2-S1. Substantial (a witness placed on a side he does not speak to; from the A-S3 fix).**

Records `contested_claims[2]` ("How soon after his arrival the first hearing came"), side "The day after: ... Sarpi, 17 April (sarpi_history-of-the-council-of-trent_brent1676.txt l.9617)". The entry repeats it in `uncertain[4]` ("Pallavicino, Sarpi and Waterworth put it on 17 April, the day after Luther arrived") and in `datesNote` ("Pallavicino, Sarpi and Waterworth put the first hearing on 17 April, the day after").

What Sarpi says. SARPI l.9617: "And 1n that place, the ſeventeenth of 4pril, he was demanded". He gives no arrival date. His run-in (l.9605-9616) names the Diet, the safe-conduct and the "Tiles" saying, with no day of arrival. So he witnesses the calendar day, not the interval the claim is about. The others do: PALL1 l.10012-10013 "nel giorno immediato dopo l'arriuo"; WAT l.1724-1727 "the sixteenth of April ... the follow / ing clay, the seventeenth"; ARM l.9150-9151 "April 16. / The next day".

Fix, records `contested_claims[2]` sides: "The day after: Pallavicino, 17 April (pallavicino_istoria-del-concilio-di-trento-parte1-ita_1664.txt l.10012-10014); Waterworth, arrived 16 April and appeared on the 17th (council-of-trent_canons-and-decrees_waterworth1848.txt l.1724-1727); Herrnschmid, 'April 16. The next day' (arminian-magazine_vol-1_1778.txt l.9150-9151). Sarpi gives 17 April for the hearing but no date for the arrival (sarpi_history-of-the-council-of-trent_brent1676.txt l.9617). The fourth day after: Foxe (foxe_acts-and-monuments-v4_cattley-townsend1837.txt l.21734), who gives no calendar date for either hearing."

Fix, entry `uncertain[4]`: "How soon the first hearing came. Pallavicino and Waterworth put it on 17 April, the day after Luther arrived. Sarpi also gives 17 April, but no arrival date. Foxe puts it 'the fourth day after his repair', and gives no calendar date for it." (Sentences 6, 15, 9 and 18 words.)

Fix, entry `datesNote`: replace "Pallavicino, Sarpi and Waterworth put the first hearing on 17 April, the day after; Foxe says 'the fourth day after his repair'." with "Pallavicino, Sarpi and Waterworth put the first hearing on 17 April. Pallavicino and Waterworth call it the day after his arrival; Foxe says 'the fourth day after his repair'." (12 and 21 words.)

The brief is not touched: its "17 April" stands on all three.

**A2-S2. Substantial (an overstated silence; from the A-B1 fix).**

Entry `uncertain[2]`: "Luther's Table Talk gives no speech before the Diet: its 'next day' is the talks with 'the Bishops and others'."

What the Table Talk gives. Before the "next day", it gives Luther's spoken answer to the emperor in the assembly. TT l.3547-3549: "I appeared in the Senate House before the Council and / State of the whole Empire, where the Emperor, and the Princes Electors in / person were assembled." Then l.3557-3563: "I answered and said, 'Most / gracious Lord and Emperor, some of my books are books of controversies, / ... the same I neither can nor will revoke. ... and for that end I desire respite / of time.' Then they gave me one day and one night." So it does give a speech before the Diet: the first answer. What it lacks is any account of the second hearing. The records' side says this rightly ("tells no speech of the second hearing"). The entry's sentence copies round 1's own overstatement ("It has no speech before the Diet at all").

Fix, entry `uncertain[2]`: "The words are absent from Pallavicino, Sarpi, Waterworth and Buchheim. Luther's Table Talk tells only the first hearing, where he asked for time. Its 'next day' is the talks with 'the Bishops and others'. No held editor discusses whether he said them." (Sentences 10, 13, 11 and 8 words.)

### Minor

**A2-M1. Minor (the printer named wrongly; from the A-B1 fix).** Brief, paragraph 5: `Herrnschmid's Life of Luther, printed by John Wesley in 1778`. The volume was "printed by R. Hawes in Dorset Street, Spitalfields" (ARM l.3); Wesley was its editor (ARM l.2). The entry already has it right: "Herrnschmid, in Wesley's magazine of 1778" (`uncertain[1]`). Fix (word-neutral): `Of our sources, only Herrnschmid's Life of Luther, in John Wesley's magazine of 1778, gives the German "Hier stehe ich."` (20 words.) With A2-B1 the brief comes to 399 words.

**A2-M2. Minor (an absence note that still lists its hits short).** Records `absent_details[3]` lists the hits for "aleand" as "Pallavicino, Waterworth, Sarpi, Foxe, Buchheim and Beza's editors", with Brieger's edition cited in ZKG 7, and now Luther's 1930 editors. It still leaves out two held lines:
- the Loyola letters' editors, whom round 1 named (`ignatius-loyola_epistolae-et-instructiones-v22-lat_1903.txt` l.9858, 11088-11090);
- Mirbt, who cites Kalkoff's edition of the dispatches: "Kalk off. Die Depeschen d. Nuntius Alexander" (OCR for Aleander, MIRBT l.15592).

Neither holds a dispatch, so the absence stands. Fix: add "The Loyola letters' editors annotate him (ignatius-loyola_epistolae-et-instructiones-v22-lat_1903.txt l.9858, 11088-11090). Mirbt cites Kalkoff's edition of the dispatches, not held (MIRBT l.15592)."

**A2-M3. Minor (the README overstates what is held; from the A-M11 text).** README: "The Edict is held in its German text". Only Mirbt's excerpt is held (MIRBT l.15588, "Deutsche Reichstagsakten II 640 ff."), as the brief now says after A-M1. Fix: "Part of the Edict is held in its German text, Luther's speech in Foxe's English with his own later words, and the emperor and the papal envoy through Pallavicino, a Jesuit writing from the envoy's letters."

## Verified

- **Audio.** `diff` of the brief, with `[calmly] ` prefixed and `[warmly] ` before the last paragraph, against the audio script: identical.
- **Brief, every changed sentence, against its source and in context:**
  - "Carl Mirbt's collection prints part of its Edict, in German." (MIRBT l.15586-15590);
  - "Foxe, a Protestant, gives Luther's speech in English, drawn from Melanchthon and others." (FOXE4 l.22529);
  - "a Jesuit whose 1664 history draws on the papal envoy Aleander's letters" (PALL1 l.52675 "nelle lettere dell' Aleandro", l.6157);
  - "Of our sources, only Herrnschmid's ... gives the German 'Hier stehe ich.'" (ARM l.9308-9311; the quoted words are the OCR "Hier flehe ich" repaired). True as worded; see Searches on Zinzendorf;
  - "He would hear Luther no more, and would proceed against him as a notorious heretic." (PALL1 l.10170-10177 "come notorio eretico"; FP l.2474-2475);
  - "Buchheim, an 1885 historian on Luther's side, says it went out without the Diet's formal consent." (FP l.2518-2519 "without the formal sanction of the Diet").
- **Every changed or added quote in the entry and records**, verbatim against its file: SARPI l.9744-9746; FOXE4 l.22072-22073, 22193, 22200; TT l.3563-3564, 3598; FP l.2358; MIRBT l.15509-15512, 15629-15631; ARM l.9150, 9309; PALL1 l.10213. All match, allowing for long s and OCR. The Mirbt list and the Pallavicino paraphrases are faithful and add nothing.
- **Split sentences.** `issue[1]` (three sentences), `issue[8]` (three), the Buchheim `record` note (three), `decided[10]` (three), `uncertain[0]`, `[2]`, `[4]` and `datesNote`: each claim keeps its witness, except A2-S1 and A2-S2.
- **Sentence lengths.** Brief: longest 23. Entry: none over 25 (script).
- **AI tells and writing.** The changed reader-facing strings have no empty contrast, no "X and never Y", no summing-up line and no filler. "It was rather to bring him back by persuasion" in `issue[1]` follows Sarpi's own "not ... but". The brief's new sentences each carry a sourced point; none is padding.
- **Records.** `records.json` key `diet-of-worms-1521` equals `working/records_diet-of-worms-1521.json`. 105 claims, 10 contested, 9 absent. No "Vehus" or "Louis" remains.
- **Census.** No tradition id or census claim changed, so no census query was needed.

## Searches run

All over `cic/texts/*.txt`, tolerant of spacing, long s as f or ſ, and OCR.
- **"Only Herrnschmid gives the German" (brief p.5).** `h\s*i\s*e\s*r\s+[sſf]\s*[tl]\s*e\s*h\s*e\s+i\s*c\s*h` finds one file, ARM (l.9309). `hier\s+[sſf][tl]eh`, `[sſf]tehe\s+ich ... k[aä]nn?\s+nicht` and `kan+\s+nicht\s+anders` find only unrelated German (Bengel, Ephrata, Ausbund, Finke and others) and ARM. ZINZ l.30869-30871 has "da ſtehe / ich, ich kan nicht anders, GOtt helffe mir", but in Zinzendorf's own voice ("habe darinnen den Sinn den D. Luther zu Worms gehabt"), and not "Hier". LHYM l.651 is Carlyle's English. The absence holds as worded.
- **Another drafter of the Edict (`decided[10]`).** `drawn|drew|framed|penned|composed|verfa[sß]|entw[uo]rf` near Edict, ban, decree, Edikt or Acht, in SARPI, WAT, FP, FOXE4, LV2, LV3, LV4 and MIRBT. Hits are Trent decrees and unrelated matter. No other drafter named; the absence holds.
- **Sarpi's arrival date (A2-S1).** Read SARPI l.9596-9619. No arrival day.
- **Foxe's calendar dates (A-S3).** `april|aprill` in FOXE4 l.21600-22540: only l.22479 and l.22497 (26 April). The added "no calendar date for either hearing" holds.
- **Aleander hits (A2-M2).** `aleand` per file, and `depeschen` in all files. New relevant lines: MIRBT l.15592 (Kalkoff's edition cited) and the Loyola v22 editors. No dispatch from Worms is held.
- **Who read Charles's paper (A2-B1).** `(f[eè]|fece|fè|fé)\s+legg` in PALL1: l.10487 "fece leggere dal Grancancelliere", l.43175. Read l.10130-10145 in context.

## Counts

Round 1 findings: 19, all closed; 5 with new points (A-B1, A-S3, A-M3, A-M11, A-M12).
New: Blocking 1 (A2-B1). Substantial 2 (A2-S1, A2-S2). Minor 3 (A2-M1 to A2-M3). Total 6.
