## Council profiles, era 7 batch 1, round 3: Part A (Diet of Worms 1521)

**Council.** `diet-of-worms-1521`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-worms-1521.brief.txt`, `audio/diet-of-worms-1521.audio.txt`, `diet-of-worms-1521.entry.json`, `records.json` key `diet-of-worms-1521` (105 claims, 10 contested claims, 9 absent details; identical to `working/records_diet-of-worms-1521.json`, checked by script), and the Worms line of `README.md`. Scope: `git diff 7e0ce987c HEAD` on those files, checked against `R2_recheck.md` Part A and `R2_changes.md` Part A, including the worker's own brief and README fixes (A2-B1, A2-M1, A2-M3).
**Brief.** 399 words by `wc -w` (2:30 at 160 wpm, 2:29.6). `grade_text`: FK 7.12, Flesch 67.17. Longest sentence 23 words ("In the Wartburg, Buchheim writes, ..."). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag. Checked by `diff`.
**Entry.** The JSON parses. No sentence in any entry string runs past 25 words (script check; longest is `knownFor`, 25).
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or any fixing. No repo file edited except this part. No model, network or paid calls.

Abbreviations as in rounds 1 and 2 (FOXE4, PALL1, MIRBT, TT, FP, WAT, SARPI, ARM). Also LOY22 = `ignatius-loyola_epistolae-et-instructiones-v22-lat_1903.txt`.

## Verdict: PROCEED (no blocking, no substantial, two minor)

All six round 2 findings are closed, and each fix is right as applied. The corrected form of A2-B1 in the records is sound: the OCR blob before "legger" cannot settle who read the paper, so a neutral claim is the honest one. Every changed quote and citation matches its line, except two witness ranges that stop a line or three short of the words they carry (A3-M1). The Aleander absence note now names the Loyola editors and Mirbt, but two further held lines still go unlisted (A3-M2). Neither touches the brief or the entry, and neither changes what the reader is told.

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| A2-B1 | CLOSED | Brief p.6: "Next morning, Pallavicino says, Charles produced a paper in his own hand." PALL1 l.10137-10142 ("La mattina proſſima Ceſare fè chiamar gli Elettori ... voler'egli prima eſporre l'opinion ſua: £ « / legger vna ſcrittura di ſua mano ben lunga vn foglio"). "Produced" claims no more than the held line. Records `claims[60]` now reads "brought before the electors and princes ... The held OCR ('£ « legger') leaves unclear whether he read it himself or had it read." That is right: "voler" can govern "legger" as well as "eſporre", so the blob need not be "fè". "Later read in consistory at Rome": l.10143-10144 ("la comunicò per mezzo del ſuo Ambaſciadore in Roma, al Pontefice, che la fece vdire al Conciſtoro"). The entry's other mention is passive ("a French paper in Charles's own hand, read on 19 April"), so no string still gives Charles the reading. No "read out" left anywhere. See A3-M1 on the witness range. |
| A2-S1 | CLOSED | Records `contested_claims[2]` sides, entry `uncertain[4]` and `datesNote` replaced as proposed. Sarpi is off the "day after" side and stated on his own: SARPI l.9617 "the ſeventeenth of 4pril", with no arrival day in l.9596-9619 (see Searches). Pallavicino l.10012-10014 "nel giorno immediato dopo l'arriuo, cioè a' 17 d'Aprile"; Herrnschmid ARM l.9150-9151 "Me came thither, April 16. / The next day"; Foxe FOXE4 l.21734 "The fourth day after his repair". In `datesNote`, "his arrival" follows the sentence on Luther's arrival, so the antecedent is clear. See A3-M1 on the Waterworth range. |
| A2-S2 | CLOSED | Entry `uncertain[2]`: "Luther's Table Talk tells only the first hearing, where he asked for time. Its 'next day' is the talks with 'the Bishops and others'." TT l.3547-3563 ("I appeared in the Senate House ... I desire respite / of time.' Then they gave me one day and one night. The next day I was / cited by the Bishops and others"). TT's other Worms passages (l.984-1000, 1918-1923, 3494-3534, 3564-3615) give the talks and the journey, not a second hearing. The sentence is true as worded, and the next one says what the "next day" holds. |
| A2-M1 | CLOSED | Brief p.5: "Herrnschmid's Life of Luther, published by John Wesley in 1778". ARM header: Wesley "editor"; title page l.96-103: "Printed by R. Hawes ... and sold at the Foundery" (OCR "Printep", "SOLDAT"). The preface ("To the Reader", dated "London, Nov. 1. 1777", l.298) states at l.168-169 "Our design is, to publish some of the most remarkable Tracts". "Published by" is a fair word for the magazine's editor and issuer, and it no longer names him the printer. The entry's "in John Wesley's Arminian Magazine" and "ed. John Wesley" agree. |
| A2-M2 | CLOSED, with a new point | The two named lines are added and right: LOY22 l.9858 ("Hieronymus Aleander, a patria sua dictus Motensis"), l.11088-11090 ("Porro Aleander «Romae cessit e vita 1542"); MIRBT l.15592 ("Kalk off. Die Depeschen d. Nuntius Alexander"). But two more held lines on Aleander are still not listed (A3-M2). |
| A2-M3 | CLOSED | README: "Part of the Edict is held in its German text". MIRBT l.15586-15590 (heading "Das Wormser Edikt (1521)", source "Deutsche Reichstagsakten II 640 ff."). Agrees with the brief's "prints part of its Edict". |

## New findings

### Blocking

None.

### Substantial

None.

### Minor

**A3-M1. Minor (two witness ranges that stop short of the words they carry).**
- Records `claims[60]`, witness `pallavicino_istoria-del-concilio-di-trento-parte1-ita_1664.txt l.10137-10177`. The claim quotes "come notorio eretico", which is at l.10178 ("coRui come notorio eretico^"); l.10177 ends "era fermo di perſeguitar". Fix: witness `... l.10137-10178`.
- Records `contested_claims[2]` sides, "Waterworth, arrived 16 April and appeared on the 17th (council-of-trent_canons-and-decrees_waterworth1848.txt l.1724-1727)". The arrival is at l.1720 ("On alighting at Worms,") and l.1726 ("on the sixteenth of April"). The 17th is at l.1729 ("ing clay, the seventeenth of April, 1521"), after "on the follow" at l.1728. Fix: `(council-of-trent_canons-and-decrees_waterworth1848.txt l.1720-1729)`.

Neither string is reader-facing; no brief or entry change.

**A3-M2. Minor (the Aleander absence note still lists its hits short).** Records `absent_details[3]` says "Searched all texts for 'aleand' and 'aleandro': hits are ..." and, after the A2-M2 fix, names Pallavicino, Waterworth, Sarpi, Foxe, Buchheim, Beza's editors, Haupt (ZKG 7), the Loyola editors, Mirbt and Luther's 1930 editors. Two more held lines name him:
- `theiner_vetera-monumenta-slavorum-meridionalium-v1-lat_1863.txt` l.48761, a letter of 1538 (l.48715 "PAULI PP. III. ANNO IV. CHRISTI 1538") naming "Hieronymum Aleandrum tit. Sancti Grisogni presbiterum Cardinalem, Sanctitatis Vestrae Legatum";
- `jacques-de-vitry_briefe-in-zeitschrift-fuer-kirchengeschichte-14-lat-deu_rohricht1894.txt` l.24362, ZKG 14's notice of Capasso's 1892 work on the Vicenza legates of 1538: "Beigegeben sind sechs Briefe in der Mehrzahl von Aleander" (printed by Capasso, not held).

Neither is from Worms, so the absence stands. Fix: after the Mirbt sentence, add "Two 1538 items name him as legate: a letter in Theiner (theiner_vetera-monumenta-slavorum-meridionalium-v1-lat_1863.txt l.48761), and ZKG 14's notice of six letters, mostly his, printed by Capasso (jacques-de-vitry_briefe-in-zeitschrift-fuer-kirchengeschichte-14-lat-deu_rohricht1894.txt l.24362)."

## Verified

- **Audio.** `diff` of the brief, with `[calmly] ` prefixed and `[warmly] ` before the last paragraph, against the audio script: identical.
- **Brief, the two changed sentences, in context.**
  - "Of our sources, only Herrnschmid's Life of Luther, published by John Wesley in 1778, gives the German 'Hier stehe ich.'" (ARM header and title page; l.9309 for the German, unchanged). 20 words.
  - "Next morning, Pallavicino says, Charles produced a paper in his own hand." (PALL1 l.10137-10142). 12 words. The next sentence, "He would hear Luther no more, and would proceed against him as a notorious heretic", still sits with Pallavicino (l.10170-10178).
- **Entry, every changed string.**
  - `datesNote`: "Pallavicino, Sarpi and Waterworth put the first hearing on 17 April. Pallavicino and Waterworth call it the day after his arrival; Foxe says 'the fourth day after his repair'." PALL1 l.10012-10014; SARPI l.9617; WAT l.1726-1729; FOXE4 l.21734 verbatim ("The fourth day after his repair").
  - `uncertain[2]`: TT l.3547-3564. "the Bishops and others" verbatim (l.3564).
  - `uncertain[4]`: as above. Foxe "the fourth day after his repair" verbatim.
- **Records, every changed string.** `claims[60]` (PALL1 l.10137-10178; the "£ «" OCR quoted as held); `contested_claims[2]` (all five witnesses re-opened, lines as above); `absent_details[3]` (LOY22 l.9858, 11088-11090; MIRBT l.15592, OCR "Alexander" for Aleander, read in context with the Edict heading l.15586).
- **Split sentences.** `uncertain[2]` (now four sentences), `uncertain[4]` (four) and `datesNote` (the 17 April sentence split in two): each claim keeps its witness. Sarpi is attached only to the calendar day.
- **Writing.** The changed reader-facing strings have no empty contrast, no "X and never Y", no summing-up line and no filler. "Sarpi also gives 17 April, but no arrival date" is a plain statement of what one witness lacks, needed because the contested claim is about the interval. Each changed sentence earns its place.
- **Records file.** `records.json` key `diet-of-worms-1521` equals `working/records_diet-of-worms-1521.json` (script). 105 claims, 10 contested, 9 absent.
- **Census.** No tradition id or census claim changed, so no census query was needed.

## Searches run

All over `cic/texts/*.txt`, tolerant of spacing, long s as f or ſ, and OCR.
- **Sarpi's arrival date (A2-S1).** `arriv|came to worms|entred|entered|ſixteenth|sixteenth|16\.` and `april|aprill|4pril` in SARPI l.9550-9800: only l.9617 (the 17th, the hearing), l.9711 and l.9713 (the Edict). No arrival day. Holds.
- **The Table Talk's second hearing (A2-S2).** `worms` in TT (l.986, 1921, 3494-3615) and `the second time|next day|following day|morrow|eighteenth` in TT l.3480-3700: l.3501 is the herald's journey, l.3563 the talks. No second-hearing speech. Holds.
- **Aleander (A2-M2, A3-M2).** `a\s*l\s*e\s*a\s*n\s*d` (case-insensitive) per file, then every hit read: most are Spanish "aleando", English OCR run-ons ("healeand", "Maleand") or "caleandi". Person hits beyond the note's list: Theiner v1 l.48761 and ZKG 14 l.24362, both 1538. `aléand|aleandre` and `depeschen`: only Haupt ZKG 7 and MIRBT. No Worms dispatch held.
- **Who read Charles's paper (A2-B1).** Read PALL1 l.10130-10178 in context.
- **Wesley's role (A2-M1).** ARM header, title page and preface ("To the Reader", to "London, Nov. 1. 1777"); `wesley` in ARM.

## Counts

Round 2 findings: 6, all closed; 1 with a new point (A2-M2).
New: Blocking 0. Substantial 0. Minor 2 (A3-M1, A3-M2). Total 2.
