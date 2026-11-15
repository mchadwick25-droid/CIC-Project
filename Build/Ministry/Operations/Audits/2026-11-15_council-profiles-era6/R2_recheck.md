# Round 2 recheck: era 6 council profiles (2026-11-15)

Two fresh Opus reviewers at full effort, one per council, neither of whom had seen the drafting or the round 1 fixing. Targeted recheck of the changes from `d583e23e` to `e3021cfc` against round 1. Part A: 0 blocking, 2 substantial, 5 minor. Part B: 0 blocking, 1 substantial, 4 minor.

## Council profiles, era 6, round 2: Part A (Council of Constance 1414)

**Council.** `council-of-constance-1414`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/council-of-constance-1414.brief.txt`, `audio/council-of-constance-1414.audio.txt`, `council-of-constance-1414.entry.json`, and `records.json` key `council-of-constance-1414`. The scope is the changes from `d583e23e` to HEAD (branch `claude/cft-councils-era6`), checked against `R1_review.md` Part A and `R1_changes.md` Part A.
**Brief.** 400 words (2:30 at 160 wpm, at the cap). `grade_text`: FK 7.03, Flesch 69.73. Longest sentence 23 words ("We commit your soul to the devil," ...). No sentence is over 25 words.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag. Checked by `diff`.
**Entry.** No sentence in any entry string is over 25 words (script check). The JSON parses.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. No repo file was edited. No model, network or paid calls were made.

Abbreviations as in round 1 (FIN2, FIN3, MANSI27, RICH, MIRBT, DENZ, PALDOC, PALUB, LUTH2, LUTH3, HEF1, GERSON, RAYN28, HARAS). Also: FOXE = `foxe_acts-and-monuments-v3_cattley-townsend1837.txt`; BRAGHT = `van-braght_martyrs-mirror_sohm1886.txt`.

## Verdict: REVISE (two substantial, five minor)

Every round 1 finding has been dealt with, and every changed or added quote is verbatim or faithfully rendered. Two fixes carry new errors.

The first is in the fix for "Lords, go in peace" (A-S4). It now names the right speaker. But the entry still tells the dismissal as the last act of the session, after Martin V's answer and the decree, and the records say the session "closed with" it. Both held accounts in Mansi put the words straight after the Mass, before the Polish request, Martin's answer, the sermon and the decree (A2-S1).

The second is in the rewritten absence on Wyclif's bones (A-S5). It says the burning "is held only in Foxe". Two more held texts say the bones were burned and the ashes thrown into water: the 1916 editors of Luther's works and van Braght's Martyrs Mirror (A2-S2).

The five minor findings are:
- a witness label "the acts" on Benedict XIII's own reply, and a split sentence left without its witness;
- the Prague letter's safe-conduct phrase stretched to Jerome;
- an ambiguous "his text" in Buck's note;
- Gerson's tract, which is dated in the held text but recorded as "date not checked";
- Palacký named in the brief with nothing to tell the listener he is a modern editor.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| A-B1 | CLOSED, with a new point | `outcome[1]`, `traditions[0].note`, the new participant `record` row, FIN3 moved to `fromThoseThere`, and records claims 80-82 are all in place. The deleted absence is gone. Checked: MANSI27 l.110726-110760 (the instrument, 21 January 1417, Peñíscola); l.111237-111246 ("citationi sibi in castro Paniscolae ... praesentata, respondet per modum qui sequitur"); l.111387-111391 ("praedicti congregati in Constantia non sunt generalis Synodus, nec universalem Ecclesiam repraesentant; cum sint excommunicati"). FIN3 no. 244 is headed l.29733-29738, "Peñíscola 1416 Mai 3", with the three cardinal deacons "collegium facientes" at l.29750-29753 and "ad congregacionem Constancie ire non possumus nee debemus" at l.29988-29989. FIN3 no. 258 is at l.31527-31553, "VI. idus Aprilis anno vicesimo tercio", which is Maundy Thursday, 8 April 1417. See A2-M1. |
| A-B2 | CLOSED, with a new point | The summing-up line is gone from `uncertain[4]`. Hefele's reading (HEF1 l.3333-3337, 3393-3400, 3938-3941) and Gerson's statement (GERSON l.27283-27294) are rendered faithfully, and HEF1 is in `writtenLater`. The contested claim and claims 107-108 are in place. See A2-M4 on Gerson's date and "often". |
| A-B3 | CLOSED | The `people` name, `uncertain[13]`, claim 93 and the HARAS source are in place. HARAS l.4821-4823 reads "Anno 1418 perhibetur Metropolita Kijoviensis Gregorius Semivlach suscepisse iter ad synodum Constantiensem". "Set out for the council" is right for "suscepisse iter". The header gives the author as an archpriest of the Ruthenian chapter of Lviv, 1862. |
| A-S1 | CLOSED | Brief p.6 now reads "In September the council ruled that no safe-conduct shields a heretic from a church court." MIRBT l.13957-13978 gives session XIX, 23 September 1415. The decree says no safe-conduct to heretics bars a "iudici competenti et ecclesiastico" from proceeding, "etiamsi de salvo conductu confisi ad locum venerint iudicii". Both sides of the safe-conduct question are now in the brief. The cuts that made room keep each claim with its witness. |
| A-S2 | CLOSED, with a new point | Brief p.8 reads "by František Palacký's count" (PALDOC l.30063-30065, 30270-30273). See A2-M5. |
| A-S3 | CLOSED | The six verdicts match `Who_Scan_Supplement.md` l.234, 241, 245 and 247-249. Richental WHO matches `Who_Scan_Era6.md` l.110. For d'Ailly, the scan's "WHO (thin; judgment call)" is given as plain WHO, which is the pattern's verdict set. I spot-checked the remaining NOT SCORED names in every Who scan. Zabarella appears only as "not scored" (Era6 l.252). Tsamblak, Heusden, Dominici, Petit, Ludwig, Frederick and Lodi hits are other people or non-rows. |
| A-S4 | CLOSED, with a new point | The speaker is now right, and claim 25 (the decree, MANSI27 l.129362-129370) is added. But the order of events is wrong in the entry and in claim 24 (A2-S1). |
| A-S5 | CLOSED, with a new point | RAYN28 l.7971-8027 is checked: "V id. Decembris, anno xi" (l.8017) and "igne publice concremari" (l.8015). "Per alias nostras litteras ... confirmavimus" is at l.8000-8001, and the year heading 1427 at l.7559. `uncertain[5]`, the record row, the source and claims 133-134 are right. The rewritten absence is not (A2-S2). |
| A-S6 | CLOSED | `outcome[8]` quotes LUTH3 l.5226-5229 verbatim, and the editors' note is at l.5245-5248. The rewritten absence ("printed in full ... Not held") stands; see Searches. |
| A-M1 | CLOSED | "the most gracious Lord Jesus Christ" for "piissimo" (PALDOC l.17288-17289). |
| A-M2 | CLOSED | "names envoys from Constantinople" (RICH l.2722-2724, "zwen hertzogen von Tropi ... in bottschaft des kaysers von Constantinopel"). "Bischoff hundert und xxxxv" is at l.11634. |
| A-M3 | CLOSED, with a new point | Claim 3 now cites RICH l.406-429 and says "vorlage". The entry note's "his text" is ambiguous (A2-M3). |
| A-M4 | CLOSED, with a new point | "had ... condemned and burned" is right for "jussit condemnari et exuri" (PALUB l.2328-2332). But the sentence now hangs the safe-conduct on Jerome too (A2-M2). |
| A-M5 | CLOSED | FIN2 l.966-976: the Italian "cedula" on confirming Pisa, d'Ailly's counter-schedule, "Et ita siluit illa materia. Interim actum est contra ... Johannem Hus". |
| A-M6 | CLOSED | "Duke Ludwig, son of Clem of Bavaria (Mladoňovice)" (PALDOC l.17304-17305). |
| A-M7 | CLOSED | Bridget card l.48: "confirmed by John XXIII in 1414 and Martin V in 1419". The split sentence keeps Cumming as the witness. |
| A-M8 | CLOSED | "Fillastre praised God that the church stood under one head" ("Laudetur et benedicatur altissimus", FIN2 l.8162-8163). |

## New findings

### Substantial

**A2-S1. Substantial (a fix that keeps a wrong order of events; "closed with" is false).**

Locations:
- entry `decided[12]`;
- records claim 24, "The last session, XLV ... closed with 'Domini, ite in pace', spoken by the cardinal deacon of St Vitus in Macello at the pope's command".

What the entry says: "Martin V answered that he would keep what the council had decided in matters of faith 'conciliarly, and not otherwise'. His decree dissolved the council and gave all leave to go home. At his command a cardinal deacon said, 'Lords, go in peace' (Mansi)."

What the sources show. Both held accounts put the dismissal first, straight after the Mass.
- First account. MANSI27 l.129225-129246, single column, reads: "Qua finita, & litaniis cum solitis orationibus finitis & peractis, reverendissimus pater dominus * macello diaconus cardinalis, de mandato ipsius domini nostri totiusque sacri Concilii ... pronunciavit haec verba ... Domini, ite in pace. Et responsum fuit per adstantes: Amen. Quo facto reverendus pater Joannes de Podiomitis episcopus Catanensis ... ambonem ascendit."
- The same account goes on in the left column. The Polish envoys ask for Falkenberg's book to be condemned (l.129290-129300). Martin answers "conciliariter ... et non aliter" (l.129307-129315). The bishop of Catania preaches, "fecit collationem solemnem" (l.129319-129322). Then Cardinal de Chalant reads the decree "Martinus episcopus ..." (l.129333-129341), "ipsum Concilium absolvimus ... licentiam impartimur" (l.129362-129370).
- Second account. In the right column, after the Mass, "Ynibaldus ... de mandato domini nostri Papae, totiusque sacri concilii, & consensu ... pronunciavit; haec videlicet: Domini, ite in pace. Et responsum fuit per adstantes, Amen" (l.129310-129328). The Podiomitis and Polish passages follow it (l.129350-129370).
- The command was "of our lord the pope and the whole council" in both accounts. "At his command" drops the council.

Why it matters. The round 1 fixer dropped "then" because the columns are interleaved. But the order of the sentences still tells the dismissal as the session's last act. The first account's opening is single-column and clear.

Fix, entry `decided[12]`, replace the whole item with: "At the last session, the acts say, a cardinal deacon said 'Lords, go in peace' just after the Mass. He spoke at the command of the pope and the whole council. The Polish envoys then asked to have a book by John Falkenberg condemned. Martin V answered that he would keep what the council had decided in matters of faith 'conciliarly, and not otherwise'. After a sermon, a decree in his name dissolved the council and gave all leave to go home (Mansi)." The sentences run 19, 12, 13, 19 and 19 words.

Fix, records claim 24: "The last session, XLV, met on Friday 22 April 1418, Martin V presiding. After the Mass the cardinal deacon of St Vitus in Macello said 'Domini, ite in pace', at the command of the pope and the whole council. The Polish request on Falkenberg, Martin V's answer, a sermon by the bishop of Catania and the reading of the dissolution decree followed." Witness: MANSI27 l.129215-129246, 129280-129370.

**A2-S2. Substantial (false absence in the rewritten absent detail).**

Location: records `absent_details`, "The burning of Wyclif's bones as carried out". Its note reads: "... The burning itself is held only in Foxe, under the heading A.D. 1425."

What the sources show. Two other held texts tell the burning as done:
- LUTH2 l.1761-1763, the 1916 editors' note: "the body of Wycliff was exhumed and cremated and the ashes cast into the water (1427)."
- BRAGHT l.45484-45486, quoting Mehrning: "forty-one years after his death, his bones, by order of the pope, were exhumed, burnt, and the ashes thrown into the water."

Foxe's heading is at FOXE l.7920-7922, and "burnt his bones, and drowned his ashes" at l.8042. None of the three is a witness of the time.

Why it matters. This is the same kind of point as A-S5 in round 1. The entry does not rely on the absence, so this is not blocking.

Fix, records, replace the note with: "The council ordered them dug up in 1415 (Mansi), and Martin V's letter of his eleventh year orders them burned (raynaldus l.7977-8019). That the burning was done is held only in later writers: Foxe, under the heading A.D. 1425 (foxe l.7920-7922, 8042); the 1916 editors of Luther's works, who date it 1427 (luther_works-v2 l.1761-1763); and van Braght's Martyrs Mirror, quoting Mehrning, 'forty-one years after his death' (van-braght l.45484-45486). No witness of the time is held."

### Minor

**A2-M1. Minor (Benedict's own reply labelled "the acts"; a split sentence without its witness).**

Location: entry `outcome[1]`.
- "His written reply said those gathered at Constance were 'not a general synod' (the acts, in Mansi)." The words are Benedict's, not the council's. The new `record` row and `traditions[0].note` ("his reply, in Mansi") say so, and the point of A-B1 was to give his own voice.
- "His cardinals had told King Alfonso in May 1416 that they could not and must not go there." This sentence has no witness. It follows the Mansi sentences, so a reader can take it as Mansi's.

Fix: change "(the acts, in Mansi)" to "(his reply, in Mansi)". Add "(Finke)" at the end of the cardinals' sentence.

**A2-M2. Minor (the safe-conduct charge stretched to Jerome).**

Location: entry `outcome[4]`, "It said he had Hus and Jerome condemned and burned 'under his safe-conduct, or rather his bald-conduct'."

The Latin hangs the phrase on Hus alone. PALUB l.2329-2332 reads "virum M. Joh. Hus ... sub suo salvo aut potius calvo conductu, similiter Jeronymum ... eadem crudelitatis nece jussit condemnari et exuri". Records claim 122 gets this right.

Fix: "It said he had Hus condemned and burned 'under his safe-conduct, or rather his bald-conduct', and Jerome in the same way." (22 words)

**A2-M3. Minor (an ambiguous "his text").**

Location: entry `record`, Richental row note, "Buck judges his text a mid-1400s copy of an exemplar from the 1420s."

In a note about Richental, "his text" reads as Richental's chronicle as a whole. Buck judges only the Aulendorf codex, the oldest of several texts, a mid-fifteenth-century copy of a 1420s exemplar (RICH l.406-412). Records claim 3 names the Aulendorf codex.

Fix: "Buck judges the Aulendorf codex he prints a mid-1400s copy of an exemplar from the 1420s."

**A2-M4. Minor (Gerson's tract is dated in the held text; "often" for "pluries").**

Locations: records claim 108, "Gerson, writing after Martin V's election (tract date not checked) ..."; entry `uncertain[4]`, "Gerson, writing after the election, says Martin said often and in public ...".
- The date. Du Pin's Monitum dates the tract. GERSON l.27012-27015 reads "Scriptus est iste Tractatus Anno 1418 sub finem Concilii Constantiensis occasione appellationis Oratorum Polonorum ad futurum Concilium circa negotium Libri seditiosi Joannis Falkemberg". The tract is headed "Quomodo, & an liceat in causis Fidei a Summo Pontifice appellare" (l.26993-26999), under the Paris chancellor's name (l.26985). So it answers the very appeal of the last session.
- The adverb. "Pluries palam dixit" (l.27293) is "said several times in public". "Often" is a little stronger than the Latin.

Fix, records claim 108: "Gerson, in a tract Du Pin dates to 1418, at the end of the council, on the Polish appeal over Falkenberg (l.27012-27015), says Martin said several times in public that he would keep inviolably what was done 'conciliariter' at Constance". Witness: l.26985-27015, 27283-27294.

Fix, entry: "Gerson, writing in 1418 on the Polish appeal, says Martin said several times in public that he would keep what was done conciliarly." (23 words)

**A2-M5. Minor (a modern editor heard as a witness, in the brief).**

Location: brief p.8, "eight letters under 452 seals, by František Palacký's count."

The round 1 fix gave the name in place of the role. But the listener now hears an unknown Czech name in a paragraph of 1415 events, with nothing to say he is a nineteenth-century editor. That is the same point as A2-M2 in era 5's Clermont recheck.

Fix, word-neutral, all three changes together:
- "by František Palacký's count" becomes "by their editor František Palacký's count" (+2 words);
- p.3, "chose a third, but neither yielded" becomes "chose a third; neither yielded" (−1);
- p.5, "John fled in March 1415, and on 6 April" becomes "John fled in March 1415. On 6 April" (−1).

A scratch copy with these changes is at `/tmp/claude-0/-home-user-CIC-Project/32884fc0-bbef-57f8-b700-3dcb6b3c59ab/scratchpad/R2A/constance.r2.txt`. It runs 400 words, FK 6.90, Flesch 69.80, with the longest sentence at 23 words. The audio file needs the same three edits.

## Verified

- Every changed or added quote, checked against its file and line in context (speaker, council, year):
  - "not a general synod" and the excommunicate clause: Benedict XIII, Peñíscola, January 1417 (MANSI27 l.111387-111391);
  - "could not and must not go": the three cardinal deacons, 3 May 1416 (FIN3 l.29988-29989);
  - "que melius damnata intrusio dici debet": Benedict XIII, 8 April 1417 (FIN3 l.31549-31550, where the OCR reads "qiip");
  - Hefele's "in materiis fidei conciliariter et non aliter" and "tumultuariter" (HEF1 l.3393-3400);
  - Gerson's "conciliariter facta ... pluries palam dixit" (GERSON l.27289-27293);
  - "Gregorius Semivlach" (HARAS l.4822);
  - "igne publice concremari" and "V id. Decembris, anno xi": Martin V to the bishop of Lincoln (RAYN28 l.8015-8017);
  - Luther, 1521, "all the articles of John Hus condemned at Constance are altogether Christian" (LUTH3 l.5227-5229);
  - "Domini, ite in pace" and its speaker (MANSI27 l.129227-129233, 129317-129322);
  - the dissolution decree (l.129362-129370);
  - "jussit condemnari et exuri" (PALUB l.2331-2332);
  - "Et ita siluit illa materia" (FIN2 l.975);
  - Buck's "vorlage" (RICH l.410-412);
  - the session XIX decree (MIRBT l.13959-13978);
  - "piissimo" (PALDOC l.17288-17289);
  - the Bridget card's "and Martin V in 1419" (card l.48).
- Translations: "most gracious" for "piissimo", "lay silent" for "siluit", "set out" for "suscepisse iter", "condemned and burned" for "condemnari et exuri", and "praised God" for "Laudetur". All are faithful and add nothing. "Being excommunicate" renders "cum sint excommunicati" correctly, as the reason for both clauses.
- Split or joined sentences:
  - The brief's cuts in p.2-4 keep Richental, the acts, Fillastre and Hus's letters each with its own claim.
  - `outcome[1]`'s split leaves the cardinals' sentence without a witness (A2-M1).
  - `uncertain[4]` keeps each reading with its writer: Hefele, Gerson, the acts.
  - `uncertain[12]` keeps Cumming.
  - `uncertain[13]` keeps Harasiewicz.
- New `record` rows and sources:
  - The kinds are right: Benedict and Martin V are participants, and Hefele and Harasiewicz modern reconstruction.
  - The file paths exist.
  - FIN3 is now in `fromThoseThere`, which suits papers of the refusing party.
- No reader-facing change has an empty contrast, an "X and never Y", a summing-up line, filler or an editor's view told as settled.
- Census: no tradition id or census claim changed.

## Searches run

All of `cic/texts/` unless named. Case-insensitive, with OCR and spelling variants.
- **Wyclif's bones burned (A2-S2).** First, `(Wy|Wi)c?k?l(i|e|y)f+e?.{0,120}(bones|ossa|beine|cineres|ashes)` and the reverse order. This found LUTH2 l.1762. Second, `exhum|ausgegraben|exhumed|dug +up|digged` filtered for `wy|wi[ck]|lutter|1427|1428|bones|ossa`. This found BRAGHT l.45485 and gillett v2 l.5739 (the exhumation order only), and confirmed RAYN28 and FOXE. Third, `fleming`, plus `1428|1427|Fleming|ossa|bones` in `fasciculi-zizaniorum_shirley1858.txt`: no account of the burning.
- **Luther at Leipzig in full.** `leipzig|lipsi[ae]|lipsic` for file hits, then `(leipzig|lipsi).{0,40}disput`, `Resolutio Lutheriana` and `Disputatio ... Eccii`. Hits are introductions and notes in LUTH1-4, the Wace and Buchheim volume, `haupt_...`, Reusch, Vedder, and Zwingli's correspondence (l.5351, Luther at Leipzig on purgatory, not on Hus). No full text of Luther at Leipzig. The absence stands.
- **Gerson's tract date.** `tractat|appell|liceat` in GERSON l.26900-27240 found the Monitum (A2-M4).
- **The last session's order (A2-S1).** I read MANSI27 l.129210-129375 in both columns. I also searched for `SESSIO|sessio|fessio` near the Benedict instrument, to confirm it is printed inside the acts (l.110300-110560).
- **Who scans for the NOT SCORED names.** Searched the names in `Build/Ministry/Operations/Audits/2026-11-1*_who-scan*/*.md`: no new verdicts.

## Counts

Blocking 0. Substantial 2 (A2-S1, A2-S2). Minor 5 (A2-M1 to A2-M5). Round 1 findings: 17 closed, 7 of them with a new point (A-B1, A-B2, A-S2, A-S4, A-S5, A-M3, A-M4). None open.


## Council profiles, era 6, round 2: Part B (Council of Basel–Ferrara–Florence 1431)

**Council.** `council-of-basel-ferrara-florence-1431`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/council-of-basel-ferrara-florence-1431.brief.txt`, `audio/council-of-basel-ferrara-florence-1431.audio.txt`, `council-of-basel-ferrara-florence-1431.entry.json`, and `records.json` key `council-of-basel-ferrara-florence-1431` (now 123 claims, 21 contested claims, 12 absent details). This covers the changes from `d583e23e` to HEAD (`e3021cfc`, branch `claude/cft-councils-era6`), read against `R1_review.md` Part B and `R1_changes.md` Part B.
**Brief.** 400 words (2:30 at 160 wpm, at the cap). `grade_text`: FK 6.53, Flesch 70.83. The longest sentence has 20 words ("The acts print a note, found after his death, accepting all that the church of elder Rome holds and teaches."). No sentence is over 25 words.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag. Checked with `diff`.
**Entry.** The JSON parses and the key order is unchanged. A script checked every entry string except file paths: none is over 25 words.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. No repo file was edited. No model, network or paid calls were made.

Abbreviations are as in round 1 (M31, M32, RAY, SYR, DOUK, SPHR, GLASS, MIRBT, ZY, LUD, HPC). Added here:
- MEND = `mendes_expeditio-aethiopica-liber-1-2-lat_beccari1908.txt` (Mendez's Expeditio Aethiopica, with Beccari's Latin introduction).
- ALM = `almeida_historia-aethiopiae-liber-5-8-por_beccari1907.txt` (Manuel de Almeida, Historia Aethiopiae V-VIII, ed. Beccari).

## Verdict: REVISE (no blocking, one substantial, four minor)

Every round 1 finding is closed. Each brief fix matches its witness, and so do the word trims the coordinator made around them. Every quote that was changed or added is verbatim or a faithful rendering. The brief needs no change.

One fix needs more work. The B-S6 rewrite of the Ethiopian-sender dispute now quotes the Mendez oration through Ludolf's Latin. But the library also holds:
- the oration in Almeida's Portuguese, which names the patriarch where Ludolf's Latin has "metropolita";
- Mendez's own history;
- Innocent X's brief of 1645;
- Beccari's verdict that Zara Yaqob's obedience at Florence "commentitia est".

The new Ludolf sentence also leaves "nothing of the kind" with no antecedent (B2-S1). The minor findings are a witness range cut one line short, a weak witness line, and two claims that mix witness kinds.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| B-B1 | CLOSED, with a new minor point | Brief p.2: "For Basel we hold some of its letters, but its session records reach us only in quotation." This matches M31 l.3352-3361 ("LITERE CONCILII BASILEENSIS"). I grepped M31 l.1400-30000 for `sessio`/`sess.`/`in sessione`: no Basel session record is printed in the volume (one bare citation, "Basileensis sess.", at l.21184). The other evidence checks out: `uncertain[0]`, the two `record` items, John of Ragusa's `people` line, the source title, the rewritten records claim, the two added claims and `absent_details[0]`. That evidence is M31 l.25913 and 26065-26101 (Felix V's letter "Datum Lausannae ... XXVII Maji 1440"; "RELATIO D. JOANNIS DE RAGUSIO ... Oratoris Sacri Concilii Basiliensis plurimis annis apud Graecos"), M31 l.28590-28614, and RAY l.31580-31582 ("quam ipse Joannes dein pro Concilio legit"). The Compacts claim mixes witness kinds (B2-M3). |
| B-B2 | CLOSED | Brief p.3: "Those who stayed at Basel denied he could move it, deposed him and chose their own pope." GLASS l.20987-20992 places this in the 1437 transfer: "Eodem anno ... transtulit ... Ferrariam ... Patres autem concilii Basileensis dicebant ... Papa illud sine eius consensu nec transferre nec dissolvere posset." |
| B-S1 | CLOSED | DOUK l.355 has "BULLIALDI PRAEFATIO". At l.484-495 Boulliau titles the book himself ("anonymus liber proditurus erat"), and he writes "Catholicae ecclesiae communionis studiosissimum ... ficte ac simulate ... ut a principibus Occidentalibus ... auxilia contra Turcos consequerentur". DOUK l.14324-14327 has "plebs fera ... faex nationis Graecae ... acta omnia pro infectis reputabat". The brief p.7, `outcome[2]`, the `record` note, the two new claims and the money sides all agree. |
| B-S2 | CLOSED | `datesNote`: "Mansi's note says two rival decrees came out of the same session." RAY l.31504-31505: "bina decreta inter se opposita eadem die eademque in sessione prodierunt". |
| B-S3 | CLOSED | Supplement l.250 has Eugenius IV as STORY, and l.233 has Aeneas Sylvius Piccolomini as "WHO (hostile inside writer; flag)". The entry now matches. |
| B-S4 | CLOSED, with a new minor point | GLASS l.20474 "die veneris, VII. 6 mensis Decembris"; footnote l.20494 "... Bruck, l. c. p. 428: 14 Dec." The `datesNote`, the new `uncertain` item, the new claim and the new contested claim are right. The narrowed witness range drops the line that says "first session" (B2-M1). |
| B-S5 | CLOSED | SPHR l.10236-10254 has "ceterum cogita de synodo et rem curae habe, praesertim, quum impii tibi timendi sunt; cogere autem eam ne iam aggrediare", then "σχεδὸν γὰρ φοβοῦμαι μὴ καὶ χεῖρον σχίσμα γένηται", then "μηδὲν εἰπὼν ἀναστὰς ἀπῆλϑε". `issue[3]`, the claim and the "Why the Greeks came" side render it faithfully and add nothing. |
| B-S6 | CLOSED, with a new substantial point | The new line numbers are right: ZY l.552-553 and 673-674 (Perruchon's "délégation/députation envoyée par le roi Zar'a Yâ'eqôb"), ZY l.578-582 (Dillmann), LUD l.52432-52434, 56873-56876 and 57421-57425. In LUD, the running heads "Oratio Alph. Mendezii" at l.57003, 57164 and 57310 confirm that l.57421-57425 is still the oration. But held witnesses are still missing, and one new sentence is unclear (B2-S1). |
| B-M1 | CLOSED | Brief p.5 now gives the signing first. SYR l.47625-47627: "Eiusdem Dominici hora secunda post meridiem". SYR l.47967-47971: "cumque audiisset Ephesium non subscripsisse: Ergo, inquit, nihil praestitimus: Deinde dixit, Cras solennem Liturgiam celebrabimus". |
| B-M2 | CLOSED | Brief p.4 reads "from twenty sees". |
| B-M3 | CLOSED | Brief pp.5 and 8 say "Mark of Ephesus". The last `outcome` item and the records claim say "The Roman history printed before the acts". M31 l.46011-46014: "Graeci numquam hoc generale concilium receperint, quod octavum ab ipsis appellatur" supports "The Greeks call it the eighth, it adds". Brief p.8: HPC l.508-510, "ὅλως τοῦ Ἐφέσου μὴ ὑπογράψαντος, ἀλλὰ καὶ λογομαχίας καὶ αὖθις κινησάντων πολλῶν, ὅτε εἰς τὴν Κωνσταντίνου ἐπανῆλθον". "Had refused ... at home many renewed the quarrel" is faithful, and the Latin at l.538 has "recusaret". |
| B-M4 | CLOSED, with a new minor point | `decided[3]` reads "The fathers' phrase" (MIRBT l.14266, "id quod sancti doctores et patres dicunt"). The Greek of Doukas, DOUK l.12004-12007, has "τὸ ὅπερ λέγουσιν οἱ Γραικοὶ ἐκ πατρὸς δι' υἱοῦ". The records claim joins acts and Doukas under one kind (B2-M4). |
| B-M5 | CLOSED, with a new minor point | The claim was split correctly: the dating clause is at RAY l.35133-35139, and Raynaldus's own count follows it. The added witness l.31494 is weak (B2-M2). |
| B-M6 | HANDED OVER | Not a profile defect. These items are listed for Open-Gaps in `Handover.md` l.33-37, to be registered before merging. |

The coordinator also made word trims in the brief that round 1 did not propose. Each was checked against its source:
- p.1, "Bishops from Pope Eugenius IV told him" (SYR l.17789);
- p.2, "who signed but wrote a memoir hostile to the union" (M31 l.97328-97329);
- p.3, "and in 1433 heard";
- p.4, "the words the Latins added";
- p.8, "it says, and at home many renewed the quarrel" (HPC l.508-510).
All five are right.

## New findings

### Substantial

**B2-S1. Substantial (a contested claim still missing held witnesses; one fix sentence with no clear referent).**

*Locations.*
- Entry `uncertain` item "Who sent the Ethiopians: ...". Its last sentence is: "Ludolf says Zara Yaqob stood apart from the Roman church, and that nothing of the kind was done at Florence."
- Records, the contested claim "Who sent the Ethiopian envoys".
- Records, the claim beginning "The oration of the Portuguese patriarch Alphonsus Mendez, printed by Ludolf".
- Records, `absent_details`, "An Ethiopian-side witness".

*What the library holds and the fix left out.*
- **The oration in Portuguese.** ALM prints the oration Mendez gave at the 1626 act of obedience. The chapter heading is at l.28117-28120: "Obediencia que o Emperador ... derão publicamente ... nas mãos do patriarca dom Affonso Mendez". The passage is at l.28464-28468: "ao concilio Florentino forão mandados embaixadores pelo Emperador e Patriarcha, e trouxerão cartas do papa Eugenio quarto ao emperador Zara Jacob; e o emperador David no anno 24 do seculo passado ... dizia ter a dita carta em seu poder". So the Portuguese has "Patriarcha" where Ludolf's Latin (LUD l.57422) has "metropolita". Ludolf says his text comes from an Italian print (LUD l.56875-56876). The entry's "the emperor and the metropolitan" follows only the Latin, and it does not say so.
- **Almeida's own account.** ALM l.7658-7697 says some Ethiopians came to Rome with the Armenians at the end of the council, "como refere o cardeal Baronio, e ... muitos authores gravissimos". It says David's letters of 1524 mention Eugenius's briefs. Almeida names no sender. He adds that neither Zara Yaqob, "em cujo tempo chegarão a Ethiopia as bullas do papa Eugenio", nor his successors came over. Beccari's Latin summary (ALM l.30012-30013) reads: "Etsi tempore Zara Iacob Aethiopum legati in concilio Florentino Romano Pontifici obedientiam praestiterint ...".
- **Mendez's own history.** MEND l.6701-6705: "Zara Iacob ... Vivebat tempore concilii Florentini ut constat ex epistola Eugenii IV ad ipsum ... cuius meminit rex Onag Seguedus, sive David, ad summum pontificem Clementem VII". MEND l.6749-6750 says the Portuguese learned of "Presbyterum Ioannem" from Marco Polo and from "monachorum ad Florentinam synodum confluentium relatione", the report of monks who came to the Florentine synod. That fits Dillmann's monks.
- **Innocent X's brief.** Beccari prints it (MEND l.1432-1440, dated 30 October 1645): "Compertum vero speciatim est Aethiopiae regem Zerah oratores ad Eugenium IV ... in concilio Florentino, qui tum Ferrariae agebatur, legasse".
- **Beccari's verdict.** He is the modern editor of both Jesuit texts. MEND l.1463-1465: "commemorari obedientiam praestitam a Zara Iacob in concilio Florentino, quae, ut historicis notum, commentitia est". This is a modern editor on the "no" side, and it says plainly what Ludolf's "nihil tale" denies.

*Why the Ludolf sentence misleads.* In LUD, "Nihil autem tale" (l.52432) answers the Catholic writers at l.52405-52412: "Doctores Ecclesiae Romanae communiter scribunt; Legatos Regis Aethiopiae ... Florentiam ad Eugenium IV ... venisse", which Miraeus "Zera-Iacobo attribuit". In the entry, "nothing of the kind" comes straight after Dillmann's Nicodemus. A reader can take it as Ludolf denying Dillmann, which is the opposite of what he says. (The OCR at l.52405-52412 is poor, but "Legatos Regis Aethiopiae", "Florentiam ad Eugenium" and "Zera-Iacobo attribuit" can be read.)

*Fix, entry `uncertain`.* Replace the whole item with the text below. Every sentence is within 25 words, and each claim keeps its witness.
> "Who sent the Ethiopians: Eugenius's letter, Patrizi and Perruchon name the emperor, Zara Yaqob. So does Pope Innocent X's brief of 1645, as Beccari prints it. The patriarch Alphonsus Mendez, in an oration of 1626, says the emperor and the patriarch sent them. Ludolf's Latin of it has the metropolitan. It adds that the emperor David later said he still had Eugenius's letter. Dillmann, as Perruchon reports, says Nicodemus of the Ethiopian convent in Jerusalem sent them, without the king's knowledge. Mendez's own history says the Portuguese learned of Prester John from Marco Polo and from monks who came to the Florentine synod. Catholic writers say the king's envoys came to Eugenius at Florence. Ludolf denies it, saying Zara Yaqob stood apart from the Roman church. Beccari, a modern editor of the Jesuit histories, calls Zara Yaqob's obedience at Florence a fiction."

*Fix, entry `record`.* Change the Ludolf item's witness to "Hiob Ludolf, Commentarius ad Historiam Aethiopicam (1691), with a Latin version of the oration of the Portuguese patriarch Alphonsus Mendez". Add two items:
- `{"witness": "Manuel de Almeida, Historia Aethiopiae, books V-VIII (ed. Beccari), with Mendez's oration of 1626 in Portuguese", "kind": "later narrative", "note": "Jesuit history of the mission. For Rome."}`
- `{"witness": "Alphonsus Mendez, Expeditio Aethiopica, books I-II (ed. Beccari), with Innocent X's brief of 1645", "kind": "later narrative", "note": "The patriarch's own history; Beccari's introduction judges the Florentine obedience a fiction."}`

*Fix, entry `sources.writtenLater`.* Add:
- "Historia Aethiopiae, liber V-VIII", Manuel de Almeida, Portuguese and Latin, `cic/texts/almeida_historia-aethiopiae-liber-5-8-por_beccari1907.txt`.
- "Expeditionis Aethiopicae liber I et II", Alphonsus Mendez, Latin, `cic/texts/mendes_expeditio-aethiopica-liber-1-2-lat_beccari1908.txt`.

*Fix, records.*
- Mendez claim. Change the text to: "The oration of the patriarch Alphonsus Mendez (1626) says envoys came to Florence from the emperor and the patriarch; Ludolf's Latin has the metropolitan. They took Eugenius's letters back to Zara Yaqob, and the emperor David later said he still had them". Add the witness `almeida_historia-aethiopiae-liber-5-8-por_beccari1907.txt l.28117-28120; ... l.28464-28468`.
- Add claims, each tagged Contested:
  - Innocent X's brief: King Zerah sent envoys to Eugenius IV at Florence (MEND l.1432-1440, acts).
  - Mendez's history: the Portuguese learned of Prester John from Marco Polo and from monks who came to the Florentine synod (MEND l.6749-6750, later narrative).
  - Almeida: some Ethiopians came with the Armenians at the council's end, and Eugenius's bulls reached Ethiopia in Zara Yaqob's time (ALM l.7658-7697, later narrative).
  - Beccari: Zara Yaqob's obedience at Florence is a fiction (MEND l.1458-1465, modern reconstruction).
- Ludolf claim. Change the text to: "Ludolf answers the Catholic writers who say the Ethiopian king's envoys came to Eugenius at Florence: nothing of the kind was done there, and the Jesuit fathers themselves show Zara Yaqob stood apart from the Roman church". Change the witness to LUD l.52405-52434.
- Contested claim "Who sent the Ethiopian envoys":
  - Add to the emperor's side: Innocent X's brief (MEND l.1432-1440).
  - Mendez oration side: "The emperor and the patriarch (Almeida's Portuguese, ALM l.28464-28468), or the metropolitan (Ludolf's Latin, LUD l.57421-57425)".
  - Add to Dillmann's side, as consistent with it: "monks who came to the synod: Mendez's history (MEND l.6749-6750)".
  - Add to Ludolf's side: "Beccari (MEND l.1458-1465)".
- `absent_details`, "An Ethiopian-side witness". Change the second sentence to: "Ludolf (1691), Almeida and Mendez, with Beccari's notes, were read in context; none is an Ethiopian text of the time."

### Minor

**B2-M1. Minor (a witness range cut one line short).** The records claim "Glassberger dates Basel's first session to Friday 7 December 1431" and the contested claim "The day of Basel's first session" both cite GLASS l.20474-20475. But "celebrata est prima sessio concilii Basileensis" is at l.20476. Lines 20474-20475 hold only the date. Fix: cite l.20474-20476 in both places.

**B2-M2. Minor (a weak witness line).** The records claim "Raynaldus says the legate Nicholas (Albergati) presided at Ferrara's first session ..." cites RAY l.31494 for the surname. That line is Mansi's note on Albergati leaving Basel in an earlier year, so it supports the name only by inference. Raynaldus's own summary of 1438, RAY l.382, says it directly: "Coepta Synodus Ferrariae, praeside Nicolao Albergato". Fix: replace l.31494 with l.382.

**B2-M3. Minor (one claim, two witness kinds: the Compacts).** The claim "Mansi prints the Compacts with the Bohemians, agreed by Basel's legates at Prague and elsewhere in the council's name and then confirmed by the council itself" is tagged `acts`. "Then confirmed by the council itself" is Mansi's admonition (M31 l.28590-28593, "ac dein ab ipso demum concilio confirmata"), not the Compacts' text. Fix: split it in two.
- "The Compacts with the Bohemians, as Mansi prints them, were agreed between the legates of the council of Basel and the general assembly of Bohemia and Moravia at Prague". Witness M31 l.28617-28623 ("concordata sunt inter legatos sancti concilii Basiliensis, & generalem congregationem inclyti Regni Bohemiae ... in civitate Pragensi"); `acts`; Documented.
- "Mansi's note says the council itself then confirmed them". Witness M31 l.28590-28593; `modern reconstruction`; Documented.

**B2-M4. Minor (one claim, two witness kinds: the procession).** The decree claim "... It reads the holy doctors' and fathers' 'through the Son' in that sense. Doukas calls the phrase the Greeks'. ..." is tagged `acts`, but it now also cites DOUK l.12037-12040, a later narrative. Fix:
- Remove the Doukas sentence and the DOUK witness from the decree claim.
- Add a claim: "Doukas calls 'from the Father through the Son' the phrase the Greeks use". Witness DOUK l.12004-12007 (Greek, "τὸ ὅπερ λέγουσιν οἱ Γραικοὶ") and l.12037-12040 (Latin, "id quod Graeci dicunt"); `later narrative`; Documented.

## Verified

- **The brief.** Every quote in the brief, changed or not, was re-read in place:
  - p.1: SYR l.17873-17875 and 17904-17905.
  - p.5: SYR l.47655-47656 ("cum lacrymis & suspiriis nostrorum plurimi subscripsimus"); SYR l.47970 ("Ergo, inquit, nihil praestitimus").
  - p.7: DOUK l.12135-12137.
  - p.8: HPC l.506-510.
  All are verbatim or faithful renderings. The brief's 400 words leave no room for any brief fix, and none is proposed.
- **Changed entry quotes and renderings.**
  - `issue[3]` (SPHR l.10236-10254).
  - `decided[3]` (MIRBT l.14266).
  - The Doukas `record` note (DOUK l.484-495, 14324-14327).
  - The last `outcome` item (M31 l.46011-46014; HPC l.508-510).
  - The `datesNote` additions (GLASS l.20474-20476, 20494; RAY l.31504-31505).
  - `uncertain[0]` (M31 l.3352-3361, 25913-27173 and the Felix V heads at l.25913, 26065, 26286, 26399, 26865 and 27058; l.26095-26101; l.28590-28640).
- **Changed records claims.**
  - Boulliau (DOUK l.484-495).
  - Doukas's scorn (DOUK l.14324-14327).
  - Ferrara's date (RAY l.35133-35139) and the count (l.35139-35142).
  - Sphrantzes (SPHR l.10236-10254).
  - John of Ragusa (M31 l.26095-26101; RAY l.31580-31582, which is Mansi's note: "ego ex Codice Vindobonensi Ms. dedi in Supplem. Concil.").
  - Perruchon (ZY l.552-553, 673-674).
  - The Mendez oration (LUD l.56873-56876, 57421-57425).
  - Ludolf (LUD l.52432-52434).
- **People verdicts.** Eugenius IV is STORY and Aeneas is WHO (supplement l.250 and l.233).
- **Sentence lengths.** No entry string is over 25 words, by script.

## Searches run

- **Basel session records in M31** (for the brief's "session records reach us only in quotation"). I grepped M31 l.1400-30000 for `sessio`, `s e s s i o` (spaced), `sess\.`, `in sessione` and `XXXIV|XLV`. The only Basel hit is the bare citation "Basileensis sess." at l.21184. The `Sessio` hits at l.1173-1286 are the index of Florence's sessions. The absence holds.
- **An Ethiopian-side witness, and the sender dispute** (the changed `absent_details` note). I listed every file in `cic/texts/` whose name matches `ethiop|aethiop|gez|abyss|habes|ludolf|zara|kebra|synax`. Then I grepped all of `cic/texts/` for `zar.?a[ -]?y(a|â)|zera-?jac|zara-?iac|zara-?jac|zar'a` (25 files). In the 14 Ethiopian and Jesuit files I grepped `flor[eê]n[cçtz]|florenti|ferrar|eugen(io|ius|e) ?(iv|4|quart)`.
  - Hits read in context: MEND l.1432-1465, 5883-5886, 6701-6705, 6749-6750 and 10300; ALM l.7658-7705, 28117-28120, 28440-28470 and 30009-30016; Telles l.6271-6278 and 8345-8356 (an English summary of the same Jesuit account).
  - These give B2-S1. The others are no-hits or unrelated: Alvares l.11821, a Florentine; Castanhoso and Paez, bibliography and a jeweller; Sarsa Dengel and Basset-Guidi, Florence manuscripts; the Ethiopian Synaxarium v1 l.4557, an index entry.
  - No Ethiopian text of the time names Florence, so "An Ethiopian-side witness" still holds as an absence.
- **The Doukas Greek for "through the Son".** I grepped DOUK l.11800-12200 for `υἱο`. The hit at l.12004-12007 is quoted above.

## Counts

Blocking 0. Substantial 1 (B2-S1). Minor 4 (B2-M1 to B2-M4). Round 1 findings: 13 closed (4 of them with a new point), and B-M6 handed over to Open-Gaps. The brief is unchanged by these fixes: 400 words, FK 6.53, Flesch 70.83, longest sentence 20 words.
