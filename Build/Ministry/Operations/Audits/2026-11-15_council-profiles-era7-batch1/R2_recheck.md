# Round 2 recheck: era 7 council profiles, batch 1 (2026-11-15)

Three fresh Opus reviewers, one per council, targeted recheck at full effort of round 1's findings and every string changed since f1f6cd220. Part A Worms, Part B Augsburg, Part C Chanforan.

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

---

## Council profiles, era 7 batch 1, round 2: Part B (Diet of Augsburg 1530)

**Council.** `diet-of-augsburg-1530`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-augsburg-1530.brief.txt`, `audio/diet-of-augsburg-1530.audio.txt`, `diet-of-augsburg-1530.entry.json`, `records.json` key `diet-of-augsburg-1530`, and the README's "Diet of Augsburg (about 2:30)" line. The scope is `git diff f1f6cd220 HEAD` on those files (branch `claude/cft-councils-era7-batch1`), checked against `R1_review.md` Part B, `R1_changes.md` Part B and the worker's three edits in the `R1_changes.md` preface.
**Brief.** 400 words (`wc -w` and the batch's `grade.py`), 2:30.0 at 160 wpm, at the ceiling. `grade_text`: FK 7.79, Flesch 60.42. Longest sentence 25 words (the unchanged opening, "At three on a Saturday afternoon ... at Augsburg."). No sentence over 25 words.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag. Checked by `diff` after stripping the two tags.
**Entry.** The JSON parses. No changed entry sentence is over 25 words (script check; the one hit, `decided[13]`, is unchanged and is a splitter artifact at a quotation's closing full stop).
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. No repo file was edited except this part. No model, network or paid calls were made. `cic/texts/` is unchanged since round 1, so its line numbers stand.

Abbreviations as in round 1 (AUG, BOC, BENS, WAT, SARPI, PALL, FPR, ZW2, LW4, BOSS, NIEM).

## Verdict: REVISE (no blocking, one substantial, seven minor)

All three blocking points from round 1 are closed. The brief now says the confession is held in printed texts, the "How could they assent" question sits after the talks with Melanchthon named, and the Coburg absence names Pallavicino as a second witness to Melanchthon's letters. Every changed or added quote is verbatim or faithfully rendered.

One fix carries a new error. The confession's `record` note now says "Jacobs translates Melanchthon's Latin first printing". The held head-note says a joint committee of four Lutheran church bodies prepared that translation (B2-S1).

The seven minor points:
- the worker's cut of "two" brings back round 1's smaller point in B-B1;
- the worker's Buchheim wording makes a gapped sentence that is hard to follow aloud;
- Bensow's "säkerligen" (surely) is dropped from his judgment on the German text;
- a tradition note puts "September" in Pallavicino's mouth, which the fixer kept out of `outcome[0]`;
- the new contested claim gives Waterworth a date for the commission that he does not state;
- the rewritten Coburg absence leaves out the Exhortation, the Coburg writing on the Diet that the brief quotes;
- the `R1_changes.md` preface says one word was cut, but three were.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| B-B1 | CLOSED, with new points | Brief p.2: "the confession in printed texts". `uncertain[0]`, `record[0].note`, claim 107 and absent detail 8 are in place. BENS l.31317-31319 ("De båda till kejsaren öfverlämnade exemplaren hafva ... icke kunnat återfinnas"), l.31340-31342, l.31344-31348; BOC l.1466-1468. The brief no longer contradicts its own close. See B2-S1 (the translator), B2-M1 (the cut "two") and B2-M3 (the hedge). |
| B-B2 | CLOSED | Brief p.6 ends at the copy refused; p.7 has "Told to assent, Melanchthon writes, the princes refused" after the talks and before the quote. BOC l.3375-3386 (first demand, copy refused), l.3388 ("Then, too, negotiations for peace were begun"), l.3394-3398 ("again demanded ... This our princes declined to do. For in a matter pertaining to religion, how could they assent to a writing into which they had not looked?"). Naming Melanchthon keeps the quote off Pallavicino. Entry `decided[10]` opens "When the emperor demanded it again after the talks" and now follows the talks item. |
| B-B3 | CLOSED, with a new point | Absent detail 5 and claim 108 are in place. PALL l.17453-17461: "Fù ella in principalissimi articoli ... Prendiamone per testimonio lo stesso Melantone in vna lettera da lui scritta al Legato ... [Nullum] dogma teniamo diverso dalla Chiesa Romana". WAT l.2461-2462 gives the same letter in Latin. "We hold no dogma different from the Roman Church" is faithful. LW4 l.6232-6247 (Sermon at Coburg, finished 15 July; letter of 5 July). See B2-M6. |
| B-S1 | CLOSED, with a new point | Brief p.8 names both witnesses for the April term, and "They refused" follows both accounts. WAT l.2497-2505, 2541-2544; FPR l.3487-3493; PALL l.17567-17569, 17580-17582, 17600-17601. K10 and `uncertain[9]` carry Pallavicino. See B2-M2 on the worker's rewording of Buchheim's identifier. |
| B-S2 | CLOSED, with a new point | `outcome[0]` now separates the September draft (WAT l.2541-2544), Pallavicino's first recess (PALL l.17600-17601: "Essendo queste condizioni ripudiate da principali Protestanti; venne Cesare ad vn secondo Editto"), the final approval (WAT l.2544-2546) and Melanchthon's "horrible decree" with H. E. Jacobs's note (BOC l.11951-11952, l.11994: "The 'Recess' of November 19th"). Claims 78, 79 and 109 match. See B2-M4 on `traditions[0].note`. |
| B-S3 | CLOSED | `decided[14]` and claim 72 now give section 4 as what the princes "should" do. BOSS l.1012-1020: "Darzu dass sich der gemeldt churfurst zu Sachsen, die fünf fürsten und sechs städt wider dieienen, so das hochwürdige sacrament nicht halten, und die widertäufer mit uns samt den andern churfürsten, fürsten und ständen vergleichen und sich von uns ... keineswegs absondern ... solten ... wie dann unsere churfürsten, fürsten und stände solches alles ... verwilliget und zugesagt hätten". "Side with", "not to separate" and "had agreed to this" are faithful. The split sentences each keep Bossert's decree as witness. |
| B-M1 | CLOSED | "In the same hall" is cut from the brief; `decided[6]` keeps it under Bensow (BENS l.31394-31395). |
| B-M2 | CLOSED, with a new point | "The Venetian friar Paolo Sarpi" (SARPI l.677-678; WAT l.321). Buchheim's side is now "an 1885 historian on Luther's side" (worker's edit after A-B2). FPR l.1578-1583 ("By Professor Buchheim"), header (Philadelphia, Lutheran Publication Society, 1885, for Luther's fourth centenary), l.3450-3451 ("the relentless spirit of fanaticism of the Roman Curia"). The side is supported. See B2-M2 on the sentence it made. |
| B-M3 | CLOSED | "John Faber" (BOC l.12852-12853). |
| B-M4 | CLOSED | `decided[5]`: "the emperor is said to have been angered" for "hvilken berättas hafva blifvit i hög grad uppbragt" (BENS l.31383-31384). Ferdinand `people`: "Bensow tells a story that he whispered to Charles, who then refused the Apology" for "Det berättas, att kejsaren just stod i begrepp att mottaga den, då ärkehertig Ferdinand tillhviskade honom något, hvarefter han vägrade" (l.31437-31439). |
| B-M5 | CLOSED | Teaser: "The Lutheran princes had their confession read to him" (Beyer read it, BENS l.31293-31298). "The final decree ordered them back" stands on WAT l.2548-2550 ("the restoration of the ancient faith ... was commanded"). |
| B-M6 | CLOSED | Old claims 13, 14 and 38 are gone. A2's note carries PALL l.17036-17037 and SARPI l.12718. `record[0].note` keeps the Gutenberg fact. |
| B-M7 | CLOSED | Claims 44 and 45. ZW2 l.1975-1977 ("Bucer and Capito drew up a confession ... handed to the emperor on July 11th"). NIEM l.3956-3959 is Niemeyer's preface: "a Bucero adiuvantibus Casp. Hedione et W. Capitone composita et Carolo V. imperatori per legatos Argentorati, Constantiae, Memmingae et Lindaviae ... tradita" (OCR garbled). The corrected cite is right. NIEM l.46380-46384, the title, "PER LEGATOS CIVITATUM". WAT l.2488-2490 ("Bucer and Capito had presented"). |
| B-M8 | CLOSED, with a new point | Contested claim 13 and `decided[9]` are in place. SARPI l.12916-12923 ("After many Treaties, seven Catholicks, and seven Protestants ..."); PALL l.17449-17450 ("Hebbe principio la conferenza a' 16. d'Agosto", OCR "a’id."); FPR l.3442-3443; BOC l.3388. See B2-M5 on Waterworth's side. |
| B-M9 | CLOSED | A3's note gives the all-texts search, Theiner l.46768-46800 and both Pallavicino lines. Claims 110 and 111. PALL l.17759-17766: "in vna lettera scritta all'Aleandro ... Nunzio alla Dieta di Spira ... si duole che in Augusta douendosi il di susseguente stabilir la sopraddetta concordia, importunamente il Fabri diè fuori vn libro ... e l'Echio vn catalogo degli Eretici ... il che rinfiammò la rabbia" (OCR garbled). "On the eve of the planned concord" renders "il dì susseguente". The fixer was right to drop "later": no held line dates the letter. PALL l.17743-17745: "nè volle che la confutazione fosse data in suo nome". |
| B-M10 | OPEN, by design | Census differences are held for the batch's single Open-Gaps entry at merge (`R1_changes.md` preface). The text in `R1_changes.md` Part B is ready to apply. No tradition id changed in round 1, so no census recheck was needed. |
| B-M11 | CLOSED | README l.10 now reads "and the Catholic reply, known through its opponent and Catholic historians, each need a sentence." It matches the brief p.2. "(about 2:30)" holds at 400 words. |
| B-M12 | CLOSED | `traditions[1].note`: "Catholic theologians wrote the reply, given to them by the legate (Bensow)". BENS l.31366-31369 ("öfverlämnades åt det påfliga sändebudet Campegius, hvilken åter uppdrog affattningen ... åt ett tjugutal ... teologer"). |

## New findings

### Blocking

None.

### Substantial

**B2-S1. Substantial (the translator misnamed, in the entry's `record` note: new text from the B-B1 fix).**

Location: entry `record[0].note`.

Text: "The confession in printed texts, of the Lutheran estates. Jacobs translates Melanchthon's Latin first printing of 1530-31; the Gutenberg text names no translator or basis. Bensow says the signed copies are lost."

Evidence: BOC l.1466-1471, the head-note over the confession itself: "This Translation is made from the Latin Editio Princeps of 1530-31 ... It has been carefully prepared by a Joint Committee of The General Council, The General Synod, The United Synod of the South, and the Joint Synod of Ohio, as a Common Standard of The Augsburg Confession in English. The words in brackets are inserted from the German Editio Princeps." The Library header names H. E. Jacobs as "editor and translator" of the volume (BOC l.2-3). But the source's own line for this text gives the translation to the committee. H. E. Jacobs is the volume's editor. The note gives the work to one man that the held line gives to four church bodies, and it leaves out that the English adds words from the German. "Melanchthon's" first printing is right: Bensow has Melanchthon publish the text himself at the end of 1530 and in spring 1531 (BENS l.31324-31326), and calls it "Melanchtons första upplaga" (l.31345).

Fix, entry `record[0].note`: "The confession in printed texts, of the Lutheran estates. The Book of Concord's English was prepared by a joint committee of four Lutheran church bodies. It follows Melanchthon's Latin first printing of 1530-31, with words added from the German. The Gutenberg text names no translator or basis. Bensow says the signed copies are lost." (Each sentence is under 25 words.) The `record[0].witness` label "H. E. Jacobs's Book of Concord" can stay, since he edited the volume.

### Minor

**B2-M1. Minor (the worker's cut of "two" brings back round 1's smaller point in B-B1).** Brief p.2: "Part of the Diet's own record is held: the confession in printed texts, part of the final decree, and the other confessions." Round 1 noted that "the other confessions" comes before the brief has said there were others; they arrive in p.5. Its fix read "the two other confessions". `R1_changes.md` Part B records that fix as applied. The file does not have "two": the worker cut it to pay for the Buchheim wording (diff against the round 1 scratch copy `scratchpad/rb/augsburg.fixed.txt`). Fix, word-neutral: "Part of the Diet's own record is held: the confession in printed texts, part of the final decree, and two other confessions." (22 words; the brief stays at 400.) Hinke has Zwingli's and the four cities' confessions as the two (ZW2 l.1974-1977, 1990-1994).

**B2-M2. Minor (the worker's Buchheim wording makes a gapped sentence that is hard to follow aloud).** Brief p.8: "Waterworth puts the term in a September draft, C. A. Buchheim, an 1885 historian on Luther's side, in the final decree of 19 November." The second clause has no verb, and an appositive sits inside the gap. Heard aloud, "an 1885 historian on Luther's side, in the final decree" can sound like a description of Buchheim rather than his placing of the term. A B2 listener has to rebuild the sentence. "An 1885 historian" also dates the man rather than his writing. The side itself is supported (B-M2 above). Fix, word-neutral (the brief stays at 400; checked on a scratch copy, FK 7.91, Flesch 60.26, longest sentence 25): "Waterworth puts the term in a September draft. Buchheim, writing on Luther's side in 1885, puts it in the final decree of 19 November." (7 and 16 words.) This drops "C. A." at his only brief mention, as the worker already did for Waterworth's "J.". For the same reading in the entry, `issue[3]` can read "Buchheim, writing on Luther's side in 1885, quotes the writ's aim 'to settle the prevailing discord'."

**B2-M3. Minor (a source's hedge dropped, in the entry and records: new text from the B-B1 fix).** `uncertain[0]`: "He says the printed German differs considerably from the text read at Augsburg, while the Latin is mainly unchanged." Claim 107: "The printed German text differs considerably from the one read at Augsburg". Bensow: "den tyska texten, hvilken säkerligen betydligt afviker från den i Augsburg upplästa" (BENS l.31340-31341). "Säkerligen" (surely) marks his judgment: he infers the difference from Melanchthon's habit of reworking the text (l.31328-31338), since the read copies are lost. He cannot have collated them. Round 1's own evidence kept "surely". Fix, `uncertain[0]`: "He says the printed German surely differs considerably from the text read at Augsburg, while the Latin is mainly unchanged." Claim 107: "Bensow judges that the printed German text surely differs considerably from the one read at Augsburg; ...", with the rest unchanged.

**B2-M4. Minor (a tradition note puts "September" in Pallavicino's mouth: new text from the B-S2 fix).** `traditions[0].note`: "They refused the Catholic reply (Melanchthon) and the September draft decree (Waterworth; Pallavicino)." Pallavicino gives no month. He speaks of "il Recesso", refused, and then "vn secondo Editto" (PALL l.17567-17569, 17600-17601). The fixer saw this in `outcome[0]` and kept the equation as the reader's (K10). This note undoes that. Fix: "They refused the Catholic reply (Melanchthon) and the first terms of the decree (Waterworth's September draft; Pallavicino's first recess)."

**B2-M5. Minor (a date Waterworth does not give, in the new contested claim: new text from the B-M8 fix).** Contested claim 13, side one: "Before the 13 July draft of the reply: Waterworth (WAT l.2441-2446)". Waterworth gives no date for the commission. He tells it, then begins the next sentence "On the 13th of July the reply of the Catholic Theologians was completed" (WAT l.2440-2446). The "before" comes from his order of telling. `decided[9]` words this correctly ("Waterworth tells the commission before the reply was finished"), but the contested claim reads as his dating. Fix, contested claim 13, side one: "Told before the 13 July draft of the reply, with no date given: Waterworth (council-of-trent_canons-and-decrees_waterworth1848.txt l.2440-2446)".

**B2-M6. Minor (the rewritten Coburg absence leaves out the Coburg writing on the Diet: new text from the B-B3 fix).** Absent detail 5, "Luther's letters from Coburg about the Diet": the note lists what LW4 holds from Coburg (the 5 July letter quoted, the Sermon and its dedication, "which does not mention the Diet"). It leaves out the Exhortation to the Clergy Assembled at the Diet. That is held in full in LW4 (l.15631 on), written at Coburg (l.15664-15669), and quoted in the brief p.4. C. M. Jacobs also reports a Coburg letter to Melanchthon of 29 April on it (l.15668-15670: "On April 29 he wrote to Melanchthon that the work was growing under his hands"). The absence itself holds: no letter of Luther's from Coburg is held in full (searches below). But the note as written suggests that nothing Luther wrote at Coburg on the Diet is held, which the entry's own `record` row for the Exhortation contradicts. Fix, the note's first two sentences: "Not held. LW4 holds his Exhortation to the Clergy Assembled at the Diet, written at Coburg (luther_works-v4-selected_various1931.txt l.15631 on, 15664-15669), and C. M. Jacobs reports his letter to Melanchthon of 29 April about it (l.15668-15670). Jacobs quotes his letter to Melanchthon of 5 July (l.6245-6247)". The rest of the note stays as it is.

**B2-M7. Minor (the audit trail misstates the worker's cuts).** The `R1_changes.md` preface says "one word cut to keep the brief at 400". Against the round 1 scratch copy, the Buchheim wording added four words net, and three words were cut: "two" (brief p.2), "J." (Waterworth, p.3) and "church" (Uppsala, p.9). `R1_changes.md` Part B also still records "the two other confessions" as applied. The "J." and "church" cuts are sound: Waterworth's side is still marked, and the Uppsala decree is of an assembly of the estates, "högre oeh nidrigere, lärde och lekte" (BENS l.31001-31002), so "a council" is right. Fix: in the preface, replace "one word cut to keep the brief at 400" with "three words cut to keep the brief at 400 ('two' in paragraph 2, Waterworth's 'J.', and 'church' before 'council at Uppsala')". If B2-M1 is applied, the Part B line on brief paragraph 2 becomes true again.

## Verified

- **Brief, every changed sentence, against its source line in context.**
  - p.1: "writes the Swedish Lutheran editor Oscar Bensow" (BENS title page, "UTGIFNA AF OSCAR BENSOW"; l.31293-31296, "det berättas").
  - p.2: "the confession in printed texts, part of the final decree" (BOC l.1466-1468; BOSS l.1012-1047, sections 4 and 40).
  - p.3: "The Catholic historian Waterworth" (unchanged label, without "J.").
  - p.4: "stayed behind at Coburg castle" (LW4 l.15661-15665, "leaving Luther behind ... the castle — Feste Coburg").
  - p.6: "Waterworth names John Faber, Eck and Cochlaeus" (WAT; BOC l.12852-12853). "It was read on 3 August, and Charles accepted it as his own" (WAT l.2448-2450). "The princes asked for a copy, Melanchthon writes, but could not accept the terms" (BOC l.3378-3386, "could not obtain, unless on the most perilous conditions, which it was impossible for them to accept").
  - p.7: "Talks followed, seven a side" (SARPI l.12916-12918; PALL l.17436-17449). "The Venetian friar Paolo Sarpi". "Told to assent, Melanchthon writes, the princes refused" (BOC l.3394-3396).
  - p.8: "Waterworth puts the term in a September draft" (WAT l.2497-2505, "the proposed edict" of 22 September). Buchheim "in the final decree of 19 November" (FPR l.3489-3493). "They refused" (WAT l.2541-2544; PALL l.17600). "for common defense" (WAT l.2599-2601, "for their mutual defence").
  - p.9: "the unaltered confession handed to Charles" (BENS l.31033-31037: "then äldste, rätte och oförrandrede Ausburgiske confession, hvilken som af chur-, furster och stä[nder] ... blef öfverantvardet käijser Carl then femte på then store rikesdagh i Ausburg år ... 1530").
- **Quotes, verbatim.** "How could they assent to a writing into which they had not looked?" (BOC l.3397-3398). "It is not fitting, dear sirs, that I should appear in person at this diet" (LW4 l.15752-15753). "dissensions in the matter of our holy religion" (AUG l.54). Entry, new or moved: "For in a matter pertaining to religion, how could they assent ..." (BOC l.3396-3398); "against those who do not hold the most worthy sacrament, and the Anabaptists" (a faithful rendering of BOSS l.1013-1015); "a horrible decree" (BOC l.11951); "some few small points of Doctrine", "no concord at all" (SARPI l.12921-12923, long s read as s).
- **Translations.** Claim 108's "we hold no dogma different from the Roman Church" (PALL l.17460-17461). Claim 109 and `outcome[0]` "rejected the conditions of a first recess, before a second edict" (PALL l.17600-17601; "first" is read from "secondo", as the fixer says). Claim 110 (PALL l.17759-17766). Claim 111 (PALL l.17743-17745). `uncertain[0]` "mainly unchanged" for "i det hufvudsakliga oförändrad" (BENS l.31341-31342), apart from B2-M3.
- **Split and joined sentences.** `decided[5]` (two sentences, both Bensow's). `decided[9]` (Sarpi and Pallavicino, then Waterworth and Sarpi, then Waterworth, then Sarpi, then Pallavicino: each claim keeps its named witness). `decided[14]` (Bossert's decree throughout; the fortieth section stays with it). `outcome[0]` (Waterworth, Pallavicino, Waterworth, Melanchthon with H. E. Jacobs). `uncertain[0]` (the Bensow lines are marked "Bensow says", "He says").
- **Records.** Every new or rewritten claim, contested claim and absent detail was checked against its cited lines. Claim 79 carries Jacobs's identification as a second, modern witness inside its witness string, as `R1_changes.md` says. The JSON parses.
- **Audio.** Rebuilt from the brief: identical apart from the two tags.
- **README.** Only the Augsburg line was in scope; the Worms line belongs to Part A.
- **No AI tells** in any changed reader-facing string: no empty contrasts, no "X and never Y", no summing-up lines, no filler. Every changed sentence earns its place. The brief is at the ceiling, and B2-M1 and B2-M2 add no words.

## Searches run (absences)

All over `cic/texts/*.txt`, case-insensitive. Where noted, I joined hyphen line breaks, collapsed whitespace and read long s as s before matching.
- **Luther's letters from Coburg (absent detail 5, rewritten).** `coburg` in every file (40 files hit). I read the relevant hits: LW4 l.6236, 13688, 15646-15669; LW6 (Saxe-Coburg, 1626 only); the Table Talk l.3307 (a distance); the hymns l.863 (Ein feste Burg, not a letter); Zinzendorf l.4530 (a narrative); FPR; BENS; PALL. Also `gruboc|grubok|ex eremo|aus der wüste|ex deserto`, the places Luther signed his Coburg letters from. The hits are all unrelated (patristic and monastic "ex eremo"). **The absence holds; the note needs B2-M6.**
- **The two signed copies (absent detail 8, new).** Normalized: `origina\w*.{0,120}(augsb|augspurg|confession|bekenntn|confessio)`, `(augsb|augspurg|augustana).{0,150}(lost|verloren|perdu|förlor|försvunn|never been found|archiv)` and `(mentz|mainz|mogunt|maintz).{0,120}(origin|copy|exemplar|handschr|manuscript)`, kept where the window also names 1530 or Augsburg and a confession. The hits are Bensow (l.31317-31319, 31344-31348, and his note that the Latin is "säkerligen mindre afvikande från originaltexten"), Arndt's editor (on the confession's scope), Barclay's index and original-sin passages. No held line says a signed copy survives. **Confirmed.**
- **Campeggio document (absent detail 3, rewritten).** Round 1's all-texts search (`campeg|campegg|campeius|campegius|campeggi`, 59 files) stands; `cic/texts` is unchanged. I re-read PALL l.17740-17766 and LW4 l.15675 ("Cardinal Campeggio ordered it translated into Latin", an act reported, not a document). **Confirmed.**
- No new absence was added in the brief.

## Counts

Blocking 0. Substantial 1 (B2-S1). Minor 7 (B2-M1 to B2-M7).

---

## Council profiles, era 7 batch 1, round 2: Part C (Synod of Chanforan 1532)

**Council.** `synod-of-chanforan-1532`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/synod-of-chanforan-1532.brief.txt`, `audio/synod-of-chanforan-1532.audio.txt`, `synod-of-chanforan-1532.entry.json`, `records.json` key `synod-of-chanforan-1532` (now 102 claims, 9 contested claims, 9 absent details), and `README.md` l.11. The scope is `git diff f1f6cd220 HEAD` (branch `claude/cft-councils-era7-batch1`), checked against `R1_review.md` Part C and `R1_changes.md` Part C. The preface's three worker edits touch Worms and Augsburg only; none touches this council.
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm, at the cap). `grade_text`: FK 6.87, Flesch 67.27. Longest sentence 25 words ("The articles survive in printings by the Dauphiné pastor Jean-Paul Perrin, the valleys' historians Pierre Gilles and Jean Léger, and the English envoy Samuel Morland."). No sentence over 25 words.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag (exact string match, two tags counted).
**Entry.** No sentence in any entry string is over 25 words (script check). The JSON parses.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. No repo file other than this part was written. No model, network or paid calls were made.

Abbreviations as in round 1 (GIL81, GIL44, PER19, MOR, LEG, MUS, MON, ZEZ, GOLL, COMEN, BEZA1, CRESP1).

## Verdict: REVISE (one blocking, three minor)

Every round 1 finding but C-S4 is closed, and C-S4 is held for the batch's single Open-Gaps entry at merge, as the R1_changes preface says. Every changed or added quote is verbatim, allowing for OCR. The rewritten dissent paragraph keeps each claim with its witness. The deposition is now told in Gilles's frame, and the teaser gives both sides.

One fix carries a new error. The C-B3 wording, "the valleys changed nothing but their view on bearing arms", reads Léger as saying the arms view changed at the Reformation. Léger says the opposite: they still held it in 1560, during Emanuel Philibert's war, and acted otherwise only later (C2-B1). The entry's `uncertain[12]` and records contested claim 3 carry the same reading.

The three minor findings are an editors' year told without the scan reading, an ambiguous "by Crespin's editors" in Gonin's `people` row, and a Perrin line range in claim 95 that does not hold the year it is cited for.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| C-B1 | CLOSED | Brief p.6 now gives Gilles's "some barbes" with their reasons (GIL81 l.2030-2034, "quelques-uns des Barbes ne consentirent pas à toutes les conclusions ... pas totalement nécessaires ... deshonoroit la mémoire"), then the two as "deux des principaux contredisans ... venus de dehors des Valées ... partirent sans congé ... s'en allèrent en Bohême" (l.2046-2052). "Gilles, on the majority's side" is fair to his "prétendues innovations" (l.2053). Blahoslav's envoys "aiunt se ... missos esse a coetu Waldensium" and stay "per integrum semestre unum" and "ad suos in Gallias revertuntur" (GOLL l.7176-7183). Goll's note names "Daniel von Valence und Johannes von Molines, die 'Abgesandten' der Waldenser" and calls the *Summa* Blahoslav's (l.7223-7226); the *Summa* of 1556 is headed at l.6424-6425. The fixer's three corrections to the review's wording are right: "objected" follows "contredisans"; "two of their leaders" follows "deux des principaux". Sentences 2 and 3 carry no "he says", but they follow "Gilles ... says" and precede "The Brethren's chronicle", so the witness is clear. Entry `uncertain[1]`, `uncertain[8]`, `outcome[2]`, `attended[7]`, Valence's `people` row, Gilles's `record` note, records claim 99 and contested claim 5 are in place and right (MUS l.6540-6542, MON l.9152, ZEZ l.11554-11555 read as quoted). "He does not speak of signing" holds (Searches). |
| C-B2 | CLOSED | Brief p.4: "In 1535, he writes, a ducal raid caught a guard keeping watch for ministers at the hamlet of Chanforans." GIL81 l.2327-2330 (the duke's patents to Bersour, 28 August 1535), l.2345-2349 (Bersour's raid at Rocheplate, "y surprit quelques hommes qui y faisoyent la garde"), l.2441-2445 ("l'un des surpris par Bersour faisant la garde ... qui estoyent assemblez en la bourgade des Chanforans"). "Muston puts Farel at this meeting": MUS l.6403-6410. The quote is unchanged and verbatim (l.2446-2447). Entry `attended[4]`-`[5]` and Peiret's `people` row tell the same frame. |
| C-B3 | CLOSED, with a new point | The exception is now in the brief, but the fix's wording misreads it (C2-B1). |
| C-B4 | CLOSED | Teaser: "Two barbes left for Bohemia; the sources differ on whether they walked out or were sent." Both sides are held: GIL81 l.2051 ("partirent sans congé"); PER19 l.6543, MOR l.21815, LEG l.22899, GOLL l.7176-7177, COMEN l.2805-2806. "New" is gone from "articles of faith". |
| C-S1 | CLOSED | Entry `outcome[5]` and `uncertain[6]`, records contested claim 2 and claim 100 are in place. GOLL l.7176-7179 ("ut viderent, an verum sit ... mutationem quandam accidisse in hac Fratrum Bohemorum Unitate. Item ministros, qui ante caelibes vixerant, uxores duxisse") is rendered faithfully as "whether the Brethren had changed and whether their ministers had married". "Told of discord at home" holds for both: "dissidium seu discordiam exortam" (GOLL l.7161-7162) and "a dissensionibus quibusdam domi ortis" (COMEN l.2806-2807, OCR). Comenius's six months: "menses integros sex" (l.2808, OCR). |
| C-S2 | CLOSED, with a new point | Records contested claim 1, claim 101 and `absent_details[5]`; entry `attended[6]`, Gonin's `people` row, the Crespin source and `uncertain[4]` are in place. CRESP1 l.49900-49911 reads as cited. Reading the note's "1552" as 1532 is sound: the same notes misprint 1526 as "IÇ26" (l.49904) and set Saunier's arrest in "février 1550" against "dès le printemps de 1532" (l.49984-49987), and Crespin's own text has Gonin taken in 1536 (l.49944-49962). See C2-M1 on telling that year to the reader, and C2-M2 on the `people` wording. Gonin's 1536 Geneva errand: PER19 l.12165-12170. |
| C-S3 | CLOSED | Peiret's `record` note, `datesNote`, `uncertain[4]`-`[5]`, the retitled `fromThoseThere[0]` and records claims 9, 34, 35 and contested claim 1 are in place. "Avoyent tenu alors leur Synode qui avoit duré six jours. Le procez Latin dit Capitulum" (GIL81 l.2464-2467) is rendered rightly as "had then held a synod that lasted six days". Keeping "participant" with the note was one of the two options round 1 gave. |
| C-S4 | OPEN (held for the batch's Open-Gaps entry at merge) | `Open-Gaps.md` has no Chanforan line yet (searched `chanforan`, case-insensitive). The entry is worded in R1_changes Part C. I checked its four witness points (MUS l.6470-6471, MON l.939-940, PER47 l.16687 and l.5383-5386, PER19 l.11976-11978) and found nothing wrong in it. It must be applied at merge. |
| C-M1 | CLOSED | "Heads of families" (PER19 l.11974-11975; MOR l.7937). "The people were present too" for "eciam dio del populo" (MON l.980-981). |
| C-M2 | CLOSED | "Pastor at Nyons in Dauphiné" (PER19 header l.2). The sentence is 25 words. |
| C-M3 | CLOSED | The thesis sentence is gone. |
| C-M4 | CLOSED | `uncertain[0]`: "printings by Perrin, Léger and Morland ... and in Gilles's summary". |
| C-M5 | CLOSED, with a new point | "Noch 1532" is verbatim (ZEZ l.6304). Morland's "in the year 1530" is at MOR l.21825-21826. The Perrin line range does not hold the year (C2-M3). |

## New findings

### Blocking

**C2-B1. Blocking (a fix's wording reverses a witness: Léger's arms view did not change at the Reformation).**

Locations:
- brief p.8: "Léger wrote in 1669 that the valleys changed nothing but their view on bearing arms." (the C-B3 fix);
- entry `uncertain[12]`: "Léger says they changed nothing but their view on bearing arms." (unchanged, same fault);
- records contested claim 3, Léger's side: "Nothing changed but the view on bearing arms" (unchanged, same fault);
- entry `outcome[17]` and records claim 91, "except on bearing arms": not wrong, but they leave the reader to supply the same misreading.

Evidence. LEG l.23072-23086. Léger's frame is the Reformation contacts: "Bien qu'au tems de la Reformation, les Vaudois ou habitans des Vallées, eussent envoyé des Députés pour conférer avec Bucer, Melanchton, Oecolampade, Zuingle, Luther, Calvin ... touchant les points de Doctrine, & de Discipline" (OCR normalised). Then: "Je ne trouve point qu'ils y ayent changé la moindre chose, si ce n'est qu'ils étoient presque Anabatistes en ce qui regarde le maniement des armes seulement, car ils croyoient qu'il n'appartenoit qu'aus Magistrats de manier l'épée". He goes on: "Ils en étoient même encore là logés l'an 1560 ... pendant la cruelle guerre que leur fit Emanuel Philibert ... bien qu'enfin à l'exemple des anciens Machabées, ils en ayent uzé autrement du depuis." So the arms view was not changed by the Reformation contacts or the meeting. They still held it in 1560 and acted otherwise only later. The brief's sentence, with the thesis line gone, now opens the paragraph on what the meeting changed. A listener hears that the meeting, or the turn to the Reformers, changed their view on arms. Léger says it did not.

Fix:
- Brief p.8: "Léger wrote in 1669 that the valleys changed nothing but, after 1560, their view on bearing arms." (17 words for 15.)
- To stay at 400, brief p.6, sentence 2: "a slight to the leaders before them" becomes "a slight to earlier leaders" (GIL81 l.2034-2036, "deshonoroit la mémoire de ceux qui avoyent ... conduit ces Eglises jusqu'alors"). A scratch copy with both edits: 400 words (wc), FK 6.91, Flesch 66.98, longest sentence 25 words (`/tmp/claude-0/-home-user-CIC-Project/961c4153-8c1b-50d3-a603-34620231affd/scratchpad/R2C/fixed.txt`).
- Entry `uncertain[12]`, last sentence: "Léger says they changed nothing. They still held in 1560 that only rulers should bear the sword, and acted otherwise later."
- Entry `outcome[17]`: add "Until at least 1560, he says, they held that only rulers should wield the sword; later they acted otherwise."
- Records contested claim 3, Léger's side: "Nothing changed at the Reformation; the view that only magistrates bear the sword held until at least 1560 and changed later: Léger (leger_histoire-generale-eglises-vaudoises-livre1-fra_1669.txt l.23072-23086)."
- Records claim 91: add "; the exception is their old view that only magistrates should wield the sword, which they still held in 1560 and later gave up (l.23076-23086)", and widen the witness to l.23072-23086.

### Minor

**C2-M1. Minor (an editors' year told without the scan reading).** Entry `uncertain[4]`: "Muston, the Baum and Cunitz note and Crespin's editors put Farel in the valleys, or at the synod, in 1532." The note reads "En 1552" (CRESP1 l.49905). The reading 1532 is sound (C-S2 row above), and records claim 101 records it. But the entry tells Léger's heading "as our scanned copy reads it" (`datesNote`), and the same care is owed here. Fix, `attended[6]`, last sentence: "Crespin's editors say Martin Gonin and another barbe invited Farel and Saunier from Grandson to the synod of 12 September. Our scan reads 1552, a slip for 1532."

**C2-M2. Minor (an ambiguous witness tag).** Entry `people`, Martin Gonin: "invited Farel and Saunier to the synod, by Crespin's editors". It can be read as the editors doing the inviting. Fix: "Barbe of Angrogna; with another barbe, invited Farel and Saunier to the synod (Crespin's editors); sent to Geneva in 1536 (Perrin)".

**C2-M3. Minor (a line range that does not hold its claim).** Records claim 95: "the held letters date Morel's mission to 1530 (perrin_histoire-des-vaudois-fra_1619.txt l.14134-14143; ...)". PER19 l.14134-14143 tells the mission under "au regne du Roy François premier" with no year. The year is in the heading of Oecolampadius's reply, "escripte en l'annee 1530" (l.14262-14271, OCR). Fix: cite "perrin_histoire-des-vaudois-fra_1619.txt l.14262-14271".

## Verified

- **Changed or added quotes, verbatim (OCR allowed).** "partirent sans congé de l'assemblée" (GIL81 l.2051); "deux des principaux contredisans" (l.2047); "pas totalement nécessaires" (l.2033); "alors" and "Capitulum" (l.2464-2467); "assemblez en la bourgade des Chanforans au milieu d'Angrogne" (l.2444-2445); "M. Farel, qui avoit la barbe rouge, et un beau cheval blanc" (l.2446-2448, OCR "Farel."); "continuoyent de venir" (l.2450); "missos esse a coetu Waldensium" (GOLL l.7176-7177, OCR "haue" for "hanc" in the line before); "per integrum semestre unum" (l.7179); "dissidium seu discordiam" (l.7161); "une faible minorité" (MON l.9152); "noch 1532" (ZEZ l.6304); "Je ne trouve point qu'ils y ayent changé la moindre chose" (LEG l.23074-23075, OCR long s). Translations checked: Blahoslav's purpose clause, Gilles's "alors", Comenius's discord at home, Zezschwitz's "Zwei Geistliche und Führer jener Minorität". None adds anything.
- **Brief, changed sentences, each with its witness.** p.1 (PER19 l.11974-11975; MON l.980-981). p.2 (PER19 header l.2; GIL81 and LEG headers). p.4 (GIL81 l.2327-2349, 2441-2447; MUS l.6403-6410). p.6 (GIL81 l.2030-2052; GOLL l.6424-6425, 7159-7183, 7223-7226; GOLL header l.2, "Jaroslav Goll ... editor"; "Jan Blahoslav", l.3424). p.8 (C2-B1).
- **Teaser, datesNote, record notes, people rows.** As in the table. "From outside the valleys": "venus de dehors des Valées" (GIL81 l.2049-2050).
- **README l.11.** It still holds. Its third reason is now met: the brief tells the chronicle's own account, with the envoys' claim that they were sent.
- **Writing.** No empty contrast, no "X and never Y", no summing-up line, no filler in any changed string. Each changed sentence earns its place; the brief's ceiling is met because the fixes cost more words than the cut freed, not by padding.

## Searches run (absences)

All in `cic/texts/` with case-insensitive `grep`, long s as f allowed for.
- "He does not speak of signing" (entry `uncertain[8]`, records contested claim 5): `sign|soub|souscri|jur[eéè]|serment` in GIL81 l.1880-2200 (only the oath article, "jurer licitement", and "Ne jurez point"); `sign[eé]|soubsign|souscri` in GIL44 (three hits, all on other matters). The absence holds.
- Léger on arms after 1560: read LEG l.23050-23095 in place (C2-B1).
- Perrin's year for the mission: `1530|trente` in PER19 l.14000-14300 (one hit, l.14271).
- Crespin's note years: `Gonin` in CRESP1 (l.49849, 49883, 49923, 50235, 60221, 114326); the OCR year pattern read at l.49900-49911 and l.49980-49986.
- C-S4: `chanforan` in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (none).

## Counts

Round 1: 12 closed (4 of them with a new point), 1 open (C-S4, held for merge). New: Blocking 1 (C2-B1). Substantial 0. Minor 3 (C2-M1 to C2-M3).

---

