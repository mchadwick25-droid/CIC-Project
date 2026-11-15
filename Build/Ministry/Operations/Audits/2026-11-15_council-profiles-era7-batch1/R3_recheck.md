# Round 3 recheck: era 7 council profiles, batch 1 (2026-11-15)

The last round under the cap. Three fresh Opus reviewers, one per council, targeted recheck at full effort of round 2's findings and every string changed since 7e0ce987c. Worms PROCEED (2 minor); Augsburg PROCEED (1 minor, applied); Chanforan REVISE (1 blocking open at the cap, 2 minor): sent to the coordinator for Mark's cap ruling.

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

---

## Council profiles, era 7 batch 1, round 3: Part B (Diet of Augsburg 1530)

**Council.** `diet-of-augsburg-1530`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-augsburg-1530.brief.txt`, `audio/diet-of-augsburg-1530.audio.txt`, `diet-of-augsburg-1530.entry.json`, `records.json` key `diet-of-augsburg-1530` (identical to `working/records_diet-of-augsburg-1530.json`, script check), and the README's "Diet of Augsburg (about 2:30)" line. The scope is `git diff 7e0ce987c HEAD` on those files (branch `claude/cft-councils-era7-batch1`, head d20f98a85), checked against `R2_recheck.md` Part B and `R2_changes.md` Part B and preface.
**Brief.** 400 words (`wc -w`), 2:30.0 at 160 wpm, at the ceiling. `grade_text`: FK 7.91, Flesch 60.26. Longest sentence 25 words (the unchanged opening, "At three on a Saturday afternoon ... at Augsburg."). No sentence over 25 words. The figures match `R2_changes.md`.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag (script check after stripping the two tags).
**Entry.** The JSON parses. No changed entry sentence is over 25 words. The one script hit, `decided[13]` (28 words), is unchanged and is the splitter artifact at a quotation's closing full stop that round 2 noted.
**README.** The Augsburg line is unchanged in this round and still matches the brief.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or any fixing. No repo file was edited except this part. No model, network or paid calls were made. `cic/texts/` is unchanged since 7e0ce987c, so all line numbers stand.

Abbreviations as in rounds 1 and 2 (AUG, BOC, BENS, WAT, SARPI, PALL, FPR, ZW2, LW4, BOSS, NIEM).

## Verdict: PASS (no blocking, no substantial, one minor)

All seven round 2 points are closed, and the one substantial point (B2-S1, the translator) is closed. Every changed quote and rendering is faithful. The brief's two changes read cleanly aloud and keep each claim with its witness.

The one minor point is in the B2-S1 fix itself. "The Book of Concord's English" reads as the whole volume's English. The joint committee made only the confession's translation; the volume's editor H. E. Jacobs translated the Apology, which this entry also quotes from the same book (B3-M1).

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| B2-S1 | CLOSED, with a new point | `record[0].note`: "The Book of Concord's English was prepared by a joint committee of four Lutheran church bodies. It follows Melanchthon's Latin first printing of 1530-31, with words added from the German." BOC l.1466-1471: "This Translation is made from the Latin Editio Princeps of 1530-31 ... carefully prepared by a Joint Committee of The General Council, The General Synod, The United Synod of the South, and the Joint Synod of Ohio ... The words in brackets are inserted from the German Editio Princeps." Four bodies, the Latin basis and the bracketed German are right. "Melanchthon's" first printing: BENS l.31324-31326 ("beslöt Melanchton ... själf utgifva texten, hvilket skedde mot slutet af år 1530 och på våren 1531") and l.31345 ("denna Melanchtons första upplaga"). The witness label "H. E. Jacobs's Book of Concord" stands (BOC l.2, "editor and translator"; l.306 signed preface). See B3-M1 on "The Book of Concord's English". |
| B2-M1 | CLOSED | Brief p.2: "and two other confessions." p.5 then names the four cities' and Zwingli's (ZW2 l.1972-1977, 1990-1994). The sentence is 22 words; the brief stays at 400. |
| B2-M2 | CLOSED | Brief p.8: "Waterworth puts the term in a September draft. Buchheim, writing on Luther's side in 1885, puts it in the final decree of 19 November." (7 and 16 words.) WAT l.2497-2505 ("On the 22nd of September ... the proposed edict ... time was now allowed them till the I5th of the ensuing April"); FPR l.3488-3493 ("This Imperial Decree ... was finally issued on the 19th of November with the additional clause ... a time of respite ... until the 15th April, 1531"). Buchheim's authorship and date: FPR header (Philadelphia, 1885) and l.1576-1583 ("By Professor Buchheim"). "They refused" still follows both accounts (WAT l.2541-2544; PALL l.17600-17601). The fixer applied the entry change at `issue[4]`, the right index: "Buchheim, writing on Luther's side in 1885, quotes the writ's aim 'to settle the prevailing discord'." FPR l.3337 ("His avowed object was 'to settle the prevailing discord"). The `record` label "An 1885 historian on Luther's side" is a label, not a spoken sentence, and may stay. |
| B2-M3 | CLOSED | `uncertain[0]`: "He says the printed German surely differs considerably from the text read at Augsburg, while the Latin is mainly unchanged." Claim 107: "Bensow judges that the printed German text surely differs considerably from the one read at Augsburg; ...". BENS l.31339-31341: "De största förändringarna äro vidtagna i den tyska texten, hvilken säkerligen betydligt afviker från den i Augsburg upplästa. Den latinska texten är däremot i det hufvudsakliga oförändrad." "Surely" renders "säkerligen"; "mainly unchanged" renders "i det hufvudsakliga oförändrad". Claim 107's remaining clauses are Bensow's at l.31343-31348 (Mainz manuscript, "hvars noggrannhet är underkastad starka tvifvel"), inside the cited range l.31330-31348. |
| B2-M4 | CLOSED | `traditions[0].note`: "They refused the Catholic reply (Melanchthon) and the first terms of the decree (Waterworth's September draft; Pallavicino's first recess)." "September" now sits with Waterworth only. "First recess" stands on Pallavicino himself: PALL l.17567-17569 ("publicò il Recesso"), l.17600-17603 ("Essendo queste condizioni ripudiate da principali Protestanti; venne Cesare ad vn secondo Editto ... rammemorando ciò che si conteneva nel primo, e 'l rifiuto d'esso", OCR garbled). |
| B2-M5 | CLOSED | Contested claim 13, side one: "Told before the 13 July draft of the reply, with no date given: Waterworth (... l.2440-2446)". WAT l.2440-2446: the commission "of seven, but which was afterwards reduced to three, of each party" is told, then "On the I3th of July the reply of the Catholic Theologians was completed, but ... it was required to be made shorter". "Draft" is fair, since Waterworth has the reply amended before 3 August (l.2446-2450). |
| B2-M6 | CLOSED | Absent detail 5, new first two sentences: "LW4 holds his Exhortation to the Clergy Assembled at the Diet, written at Coburg (... l.15631 on, 15664-15669), and C. M. Jacobs reports his letter to Melanchthon of 29 April about it (l.15668-15670). Jacobs quotes his letter to Melanchthon of 5 July (l.6245-6247)". LW4 l.15631-15634 (title), l.15645-15646 ("Luther's first work at Feste Coburg"), l.15664-15669 ("On April 23, he took up his residence at the castle — Feste Coburg ... He began work on the Exhortation as soon as he was settled in the castle. On April 29 he wrote to Melanchthon that the work was growing under his hands"), signed "CHARLES M. JACOBS" l.15723. The 5 July letter: l.6245-6247, in the Sermon's introduction, signed "CHARLES M. JACOBS" l.6284, so "Jacobs" is C. M. Jacobs, named in the sentence before. The absence itself still holds (searches below). |
| B2-M7 | CLOSED | Not applied to `R1_changes.md`, which stays as the round 1 record. `R2_changes.md` Part B records the correction: three words cut ("two", Waterworth's "J.", "church"). With B2-M1 applied, `R1_changes.md` Part B's line on "the two other confessions" is again true of the brief. Correcting in the later, append-only record is the right way to fix an audit trail. |
| B-M10 | OPEN, by design | Census differences are still held for the batch's single Open-Gaps entry at merge (`R2_changes.md` Part B, "For Open-Gaps"). No tradition id changed in round 2, so no census recheck was needed. |

## New findings

### Blocking

None.

### Substantial

None.

### Minor

**B3-M1. Minor (the committee given the whole volume's English, in the entry's `record` note: new text from the B2-S1 fix).**

Location: entry `record[0].note`.

Text: "The Book of Concord's English was prepared by a joint committee of four Lutheran church bodies. It follows Melanchthon's Latin first printing of 1530-31, with words added from the German."

Evidence: the joint committee made the confession's translation only. H. E. Jacobs's 1911 preface: "for the translation of the Augsburg Confession ... we have substituted the translation officially approved by the General Council after its preparation by a joint committee of the various synodical bodies" (BOC l.286-293). The preface to the first edition: "The Apology of the Augsburg Confession, the Smalcald Articles and the Formula of Concord were translated by the Editor" (BOC l.328-330); the Large Catechism by A. Martin (l.322-323). Read as written, "The Book of Concord's English" covers the volume. This entry quotes the Apology's preface from the same book ("How could they assent ...", `fromThoseThere` "Melanchthon's preface (H. E. Jacobs's Book of Concord)"), and that English is Jacobs's, not the committee's. The note sits under the confession's own witness row, so most readers will take it for the confession; the wording still claims more than the held line gives. Also, the bracketed words come from the "German Editio Princeps" (BOC l.1470-1471), not from the German in general.

Fix, entry `record[0].note`, its second and third sentences: "Its English in the Book of Concord was prepared by a joint committee of four Lutheran church bodies. It follows Melanchthon's Latin first printing of 1530-31, with words added from the German first printing." (15 and 18 words.) The rest of the note stays as it is. The brief is untouched.

## Verified

- **Brief, the two changed sentences, against their source lines in context.**
  - p.2: "and two other confessions" (ZW2 l.1972-1977, Bucer and Capito's confession of the four cities; l.1990-1994, Zwingli's Fidei ratio). Both are named in p.5, after the brief's own record sentence, which is now a fair forward reference.
  - p.8: "Waterworth puts the term in a September draft" (WAT l.2497-2505, the proposed edict of 22 September). "Buchheim, writing on Luther's side in 1885, puts it in the final decree of 19 November" (FPR l.3488-3493; FPR header; side, FPR l.3450-3451 as round 2 found). Split from one gapped sentence into two; each keeps its own witness, and "They refused" follows both.
- **Quotes, verbatim.** No quote in the brief changed. In the entry, `issue[4]` keeps "'to settle the prevailing discord'" (FPR l.3337, verbatim) and "'heresy'" (unchanged).
- **Translations.** "Surely ... considerably ... mainly unchanged" for BENS l.31340-31342 (faithful, nothing added). "First recess" for PALL l.17600-17603 ("nel primo"), faithful. The `record` note's "words added from the German" for "The words in brackets are inserted from the German Editio Princeps" (BOC l.1470-1471), faithful apart from B3-M1's precision point.
- **Split and joined sentences.** Brief p.8 (above). `record[0].note` now has five sentences: the committee and its basis are BOC l.1466-1471; "Melanchthon's" first printing is Bensow's (l.31324-31326, 31345), which the note's witness row also cites; the Gutenberg and Bensow sentences are unchanged. Absent detail 5: the Exhortation and 29 April letter sit with LW4 and C. M. Jacobs; the 5 July letter with C. M. Jacobs; the Sermon and Melanchthon's letters unchanged.
- **Records.** Claim 107, contested claim 13 and absent detail 5 checked against every cited line. `records.json` key equals the working file. The JSON parses.
- **Audio.** Identical to the brief apart from the two tags.
- **Writing.** No AI tells in any changed reader-facing string: no empty contrasts, no "X and never Y", no summing-up lines, no filler, no editor's view told as settled. "Surely" is Bensow's own hedge, now attributed. Every changed sentence earns its place, and the brief stays at the ceiling without the fixes adding words.

## Searches run (absences)

No new absence was added in round 2. Absent detail 5 ("Luther's letters from Coburg about the Diet") was rewritten, so its absence was rechecked over `cic/texts/*.txt`, case-insensitive:
- `coburg|koburg|coburgk|choburg|gruboc|grubok` (34 files). Read the relevant hits: LW4 (l.6236, 15645-15669, the Sermon's and Exhortation's introductions), BENS l.31232, 31238, 31311 (the journey and the copy sent to Coburg, not a letter of Luther's), Table Talk l.3307 (a distance), Spener l.2152 (a later Coburg superintendent); the rest are unrelated (Palacky's Hussite-war Koburg, the printer Koburger in Schwenckfeld, Glassberger, Perry's "Coburgi 1770").
- `from (the )?(castle of )?coburg|aus coburg|ex coburg|coburgi|in eremo nostr|vom reichstag|reichstage? zu augs`, and `luther.{0,60}(an|to|ad) (melan|philipp)` restricted to lines with 1530. No hit is a held letter of Luther's from Coburg; Spener l.1343 names the Diet in passing.
- **The absence holds.** The rewritten note now names the held Coburg writing (the Exhortation) and the two reported letters, so it no longer suggests that nothing is held.

## Counts

Blocking 0. Substantial 0. Minor 1 (B3-M1).

---

## Council profiles, era 7 batch 1, round 3: Part C (Synod of Chanforan 1532)

**Council.** `synod-of-chanforan-1532`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/synod-of-chanforan-1532.brief.txt`, `audio/synod-of-chanforan-1532.audio.txt`, `synod-of-chanforan-1532.entry.json`, `records.json` key `synod-of-chanforan-1532` (102 claims, 9 contested claims, 9 absent details; identical to `working/records_synod-of-chanforan-1532.json`), and `README.md` l.11 (unchanged in this round). The scope is `git diff 7e0ce987c HEAD` on those files (branch `claude/cft-councils-era7-batch1`), checked against `R2_recheck.md` Part C and `R2_changes.md` Part C with its preface (the worker's brief edit for C2-B1 and the two word cuts that pay for it).
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm, at the cap). `grade_text`: FK 6.93, Flesch 66.84. Longest sentence 25 words ("The articles survive in printings by the Dauphiné pastor Jean-Paul Perrin, the valleys' historians Pierre Gilles and Jean Léger, and the English envoy Samuel Morland."). No sentence over 25 words.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag (checked by `diff` after stripping the two tags). The R2_changes preface says only Augsburg's audio changed; Chanforan's changed too, with the worker's brief edit, and it matches.
**Entry.** No sentence in any changed entry string is over 25 words. The JSON parses.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the fixing. No repo file other than this part was written. No model, network or paid calls were made.

Abbreviations as in rounds 1 and 2 (GIL81 = `gilles_histoire-ecclesiastique-eglises-vaudoises-v1-fra_1881.txt`, LEG = `leger_histoire-generale-eglises-vaudoises-livre1-fra_1669.txt`, PER19 = `perrin_histoire-des-vaudois-fra_1619.txt`, CRESP1 = `crespin_histoire-des-martyrs-t1-fra_benoit-lelievre1885.txt`).

## Verdict: REVISE (one blocking, two minor)

The entry and records now read Léger rightly: the arms view held through 1560 and changed only later. C2-M1, C2-M2 and C2-M3 are closed, and every changed quote is verbatim.

The worker's new brief sentence carries a new error. "Except that later they took up arms" tells the listener the valleys bore no arms until after 1560. Léger says their rule allowed defense "en toute extrémité", and that they kept that rule through Emanuel Philibert's war. Gilles, whom Léger cites there, tells the valleys fighting that war in self-defense under the same rule. What changed later was going beyond defense, not taking up arms (C3-B1).

The two minor findings are "nothing changed in their dealings with the reformers", which can be read as a claim about relations rather than doctrine, and Muston and Montet left with no word on what kind of witness they are, after "the historians" was cut to pay for the C2-B1 sentence.

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| C2-B1 | CLOSED in entry and records; OPEN in the brief, with a new point | LEG l.23072-23086 re-read in place (quoted under C3-B1). Entry `outcome[17]` ("He names one exception: they were nearly Anabaptists on arms, holding that only magistrates should wield the sword. They still held this in 1560, in Emanuel Philibert's war, and acted otherwise only later.") is faithful to "presque Anabatistes en ce qui regarde le maniement des armes seulement", "qu'il n'appartenoit qu'aus Magistrats de manier l'épée", "encore là logés l'an 1560 ... pendant la cruelle guerre que leur fit Emanuel Philibert" and "ils en ayent uzé autrement du depuis". Records claim 91 says the same and adds "after the Maccabees' example" ("à l'exemple des anciens Machabées", l.23086); its witness is widened to l.23072-23086. Entry `uncertain[12]` and records contested claim 3 have the right timing; see C3-M1 on their opening clause. Keeping "acted otherwise" rather than round 2's "gave up" is right: "en ayent uzé autrement" says no more. The brief sentence is the worker's, not round 2's proposal, and it misstates the change (C3-B1). The cut "a slight to earlier leaders" is faithful to "deshonoroit la mémoire de ceux qui avoyent tant heureusement conduit ces Eglises jusqu'alors" (GIL81 l.2034-2036). The cut "the historians" is C3-M2. |
| C2-M1 | CLOSED | Entry `attended[6]` ends "Our scan reads 1552, a slip for 1532." CRESP1 l.49905 "En 1552, il vint . avec un autre barbe, inviter Farel et Saunier, qui se trouvaient à Granson, au synode d'An- grogne . qui se tint le 12 septembre." The 1532 reading stands on round 2's evidence (the same note misprints 1526 as "IÇ26", l.49902). |
| C2-M2 | CLOSED | Gonin's `people` row: "Barbe of Angrogna; with another barbe, invited Farel and Saunier to the synod (Crespin's editors); sent to Geneva in 1536 (Perrin)". "Avec un autre barbe" (CRESP1 l.49905); "en l'annee mille cinq cens trente six ils envoyerent à Geneve vn certain Martin Gonin" (PER19 l.12164-12166, OCR). The tag no longer reads as the editors inviting. |
| C2-M3 | CLOSED | Records claim 95 cites PER19 l.14262-14271: "Lettre d'Oecolampade escrite aux Vaudois de Prouence" (l.14262, OCR) and "escripte en l'annee 1530" (l.14271, OCR). The range holds the year. |
| C-S4 (round 1, held) | OPEN, held for the batch's Open-Gaps entry at merge | Unchanged in this round, as R2_changes Part C says. Not rechecked further. |

## New findings

### Blocking

**C3-B1. Blocking (the brief's new Léger sentence misstates what changed: the valleys bore arms in defense before the change).**

Location: brief p.8, sentence 1: "Léger wrote in 1669 that the valleys changed nothing at the Reformation, except that later they took up arms."

Evidence:
- LEG l.23072-23086 (OCR and long s normalised): "Je ne trouve point qu'ils y ayent changé la moindre chose, si ce n'est qu'ils étoient presque Anabatistes en ce qui regarde le maniement des armes seulement, car ils croyoient qu'il n'appartenoit qu'aus Magistrats de manier l'épée, & que quand ils étoient persecutés en un lieu, ils se devoient contenter de fuir en un autre, ou, en toute extrémité, d'être seulement sur la defensive, sans seulement faire un pas pour poursuivre leurs ennemis quand ils prenoient la fuite. Ils en étoient même encore là logés l'an 1560 [OCR "l ait 1 fSo. 8c <f I .", which may add 61] pendant la cruelle guerre que leur fit Emanuel Philibert ... comme le remarque Pierre Gilles ... bien qu'enfin à l'exemple des anciens Machabées, ils en ayent uzé autrement du depuis."
- So the old rule already allowed defense in the last extremity, and it held during the war of 1560-61. Léger points to Gilles for that war.
- GIL81 l.8768-8789: in that war the ministers would not let the people pursue the beaten army, "car ils avoyent conclu dès le commencement de la guerre au mois d'octobre précédent, et puis confirmé au commencement de février dernier, que si l'extrême nécessité les contraignait de se défendre par armes, ... on se contiendroit en la seule défense". GIL81 l.8276-8278 has the people bring in "grande quantité d'armes de toutes sortes, harquebuses, morions, tambours, picques, halebardes, espées, et autres despouilles des ennemis".
- A listener hears that the valleys took no arms until after 1560. Léger and Gilles both have them fighting in self-defense in 1560-61. What changed "du depuis" was going beyond defense, which is what "en ayent uzé autrement" refers back to.

Fix, brief p.8, sentence 1 (17 words for 19): "Léger wrote in 1669 that the valleys changed nothing at the Reformation, but later went beyond self-defense." The brief's spelling is American ("pretense"), so "self-defense". With this fix alone the brief is 398 words, FK 6.94, Flesch 66.77, longest sentence 25 words (scratch copy `/tmp/claude-0/-home-user-CIC-Project/961c4153-8c1b-50d3-a603-34620231affd/scratchpad/R3C/b1only.txt`). The entry and records need no change for this point; they already say "acted otherwise only later".

### Minor

**C3-M1. Minor (an opening clause that can be read as relations, not doctrine).** Entry `uncertain[12]`: "Léger says nothing changed in their dealings with the reformers." Records contested claim 3, Léger's side: "Nothing changed in their dealings with the reformers; ...". Léger's "y" refers back to the deputies' talks "touchant les points de Doctrine, & de Discipline" (LEG l.23071-23074): he finds they changed nothing in doctrine or discipline through those talks. "Nothing changed in their dealings" can be heard as saying the relationship with the reformers did not change, which he does not say. Fix: entry `uncertain[12]`, the Léger sentence: "Léger finds they changed nothing in doctrine or discipline through their talks with the reformers." (15 words.) Records contested claim 3, Léger's side, opening clause: "Nothing changed in doctrine or discipline through the talks with the reformers; ..." (rest unchanged).

**C3-M2. Minor (two main witnesses left with no kind).** Brief p.2, sentence 1: "That manuscript reaches us only in quotations by Alexis Muston and Édouard Montet." Round 2 had "by the historians Alexis Muston and Édouard Montet"; the words were cut to pay for the C2-B1 sentence. Muston and Montet are the only relays of the manuscript, and nothing else in the brief says what kind of witness they are. "All wrote on the Reformed side" follows the printers' sentence, so the listener cannot tell whether it covers them. The pattern (`Council_Profile_Pattern.md` l.15) asks for each main witness's kind. The README (l.11) still says "a manuscript quoted by two historians". Fix: restore "the historians": "That manuscript reaches us only in quotations by the historians Alexis Muston and Édouard Montet." With C3-B1 the brief is back at 400 words, FK 6.99, Flesch 66.50, longest sentence 25 words (scratch copy `/tmp/claude-0/-home-user-CIC-Project/961c4153-8c1b-50d3-a603-34620231affd/scratchpad/R3C/fixed.txt`). The audio follows the brief through `mkaudio.py`.

## Verified

- **Changed or added quotes, verbatim (OCR allowed).** "Je ne trouve point qu'ils y ayent changé la moindre chose" (LEG l.23074-23075); CRESP1 "En 1552" (l.49905); PER19 "escripte en l'annee 1530" (l.14271).
- **Translations and paraphrases of Léger.** "nearly Anabaptists on arms" for "presque Anabatistes en ce qui regarde le maniement des armes seulement"; "only magistrates should wield the sword" for "qu'il n'appartenoit qu'aus Magistrats de manier l'épée"; "still held this in 1560, in Emanuel Philibert's war" for "encore là logés l'an 1560 ... pendant la cruelle guerre que leur fit Emanuel Philibert"; "after the Maccabees' example" for "à l'exemple des anciens Machabées"; "acted otherwise only later" for "en ayent uzé autrement du depuis". None adds anything. The brief's "at the Reformation" follows "au tems de la Reformation" (l.23071).
- **Gilles's dissent sentence after the cut.** "A slight to earlier leaders" (GIL81 l.2034-2036). The claim still sits with "Gilles ... says" in the sentence before.
- **Sentences joined or split.** Entry `outcome[17]` now has three sentences; the two added ones carry "He names" and follow "Léger wrote", so the witness is clear. Entry `uncertain[12]`'s three Léger sentences open with "Léger says" (see C3-M1). Records claim 91 opens "Léger, on the Waldensians' talks with the reformers".
- **Records.** The `records.json` key equals the working copy (Python comparison). Counts: 102 claims, 9 contested claims, 9 absent details.
- **Writing.** In the changed strings: no empty contrast, no "X and never Y", no summing-up line, no filler. Each changed sentence earns its place.

## Searches run

No new or changed absence in this round. Searches made for the points above, all in `cic/texts/` with case-insensitive `grep`, OCR and long s allowed for:
- `anaba|machab` in LEG: the only arms passage is l.23076-23086; the other "Machab" hits are book lists (l.4172, 11939, 12733-12737, 12843). Léger gives no other statement on when the arms view changed.
- `armes` in GIL81 after l.3000, then read in place at l.7284-7294, l.8268-8280 and l.8766-8794 (the 1560-61 war: arms used in defense, pursuit refused under the ministers' rule).
- `(prendre|prindrent|prirent|pris) les armes` in GIL81 v1 and v2: no hit in that form.
- Spelling check: no "defence" in any era 7 brief.

## Counts

Round 2: 4 closed (C2-B1 in entry and records, C2-M1, C2-M2, C2-M3), 1 open with a new point (C2-B1 in the brief), C-S4 still held for merge. New: Blocking 1 (C3-B1). Substantial 0. Minor 2 (C3-M1, C3-M2).

---

