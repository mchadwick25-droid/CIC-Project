# Round 2 recheck: era 7 council profiles, batch 2 (2026-11-15)

Four fresh Opus reviewers, one per council, none of whom had seen the drafting or the round 1 fixing: a targeted recheck of the round 1 changes against round 1's findings, with a hard length test of every sentence, at full effort. Part A Regensburg (0 blocking, 1 substantial, 2 minor), Part B Trent (0, 1, 6), Part C Augsburg 1555 (0, 0, 2), Part D Poissy (0, 1, 4). Every round 1 finding is closed. The length test cut one clause at Regensburg that carried no decision, side or source (A2-S1) and a few words in each of the others (Trent B2-M5, B2-M6; Augsburg 1555 C2-M2; Poissy D2-M4). Net after round 2: Regensburg 396 words, Trent 398, Augsburg 1555 399, Poissy 400 (its cuts paid for D2-S1's five words on Sarpi's side).

---

## Council profiles, era 7 batch 2, round 2: Part A (Colloquy of Regensburg 1541)

**Council.** `colloquy-of-regensburg-1541`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/colloquy-of-regensburg-1541.brief.txt`, `audio/colloquy-of-regensburg-1541.audio.txt`, `colloquy-of-regensburg-1541.entry.json`, `records.json` key `colloquy-of-regensburg-1541` (now 91 claims, 8 contested claims, 13 absent details), and the README line "Colloquy of Regensburg (about 2:30)" under "Batch 2". Scope: `git diff f6c9d034 HEAD` on these files (branch `claude/cft-councils-era7-batch2`), against `R1_review.md` Part A and `R1_changes.md` Part A.
**Brief.** 400 words by `wc -w` and the batch's `grade.py` (2.50 min at 160 wpm, at the ceiling). `grade_text`: FK 8.02, Flesch 60.35 (0.35 above the floor). Longest sentence 25 words (the unchanged close, "In his bull he recalled proposing a council ..."). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag (checked by `diff` after stripping the two tags).
**Records.** `working/records_colloquy-of-regensburg-1541.json` equals the `records.json` key (python compare). Changed: claims 10 and 34; added: claims 87-90; contested X6 and X7 changed; absences unchanged.
**Entry.** Every changed entry string is 25 words or fewer per sentence. The JSON parses.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. No repo file was edited. No model, network or paid calls were made. Scratch copies of the brief are in this scratchpad folder (`rg_*.txt`).

Abbreviations as in round 1: CLET1 = `calvin_letters-vol1_bonnet1858.txt`; PALL = `pallavicino_istoria-del-concilio-di-trento-parte1-ita_1664.txt`; SARPI = `sarpi_history-of-the-council-of-trent_brent1676.txt`; WAT = `council-of-trent_canons-and-decrees_waterworth1848.txt`; FAB = `faber_memoriale-lat_1873.txt`; IGN22 = `ignatius-loyola_epistolae-et-instructiones-v22-lat_1903.txt`.

## Verdict: REVISE (0 blocking, 1 substantial, 2 minor)

Every round 1 finding is closed, and every changed or added quote is verbatim or faithfully rendered. The new Faber claim, the envoys claim and the Granvelle claim each sit on their lines. The Sarpi label, the dates and the moved bull are right.

The one substantial point is a length cut. The emperor's motives clause ("for he feared the Turks and trouble with France") carries no decision, side or source the story needs, and the entry already keeps it. Cut alone it breaks the Flesch floor (59.94), so the cut is paired with a word-neutral change that restores it (A2-S1).

The two minor points are both on the new Faber text. In the brief, his general sentence sits between Calvin's joy at the justification formula and Rome's doubt on it, so a listener hears it as a verdict on the formula. Faber names neither the talks nor justification (A2-M1). In the entry, "leaving them to trust in God alone" turns Faber's "we" into an unclear "them" (A2-M2).

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| A-S1 | CLOSED, with a new point | Brief p.2 "Calvin, a Protestant at Strasbourg" rests on CLET1 l.11619-11622 ("on the part of our adversaries ... on our side, Philip Melanchthon, Martin Bucer, and John Pistorius"); records claim 87 quotes it verbatim. Hand sentence deleted. "None of the colloquy's papers" in place. Faber added: FAB l.1055-1056 ("profecti sumus Ratisbonam, ubi facta diæta imperialis") for "was at the Diet"; FAB l.13476-13483 and l.13514-13516 ("Ratisbonæ, 12 Maii t541 ... Perrus FABER") for the date and words. "Went on in great doubt" is a fair rendering of "valde ambigue procedit". Records claim 88 gives the whole Latin sentence verbatim (allowing the hyphen break "homi- / -num") and a faithful translation; the addressee "ad Scholasticos Parisienses" (l.13292-13293), with "omnes fratres nostri" (l.13307). "He does not name the colloquy" holds (search below). New points: placement in the brief (A2-M1); entry `uncertain[7]` "them" (A2-M2). README line in place. |
| A-S2 | CLOSED | Entry `uncertain[3]` ends "The English is the 1858 translation; Calvin's Latin is not held." The edition marks the letters as from Latin originals ("[Lat. orig. autogr. — Library of Geneva. Yol. 106.]", CLET1 l.11836). X7: "blessings" sentence gone; "'crosses' is the 1858 translator's word. No held witness reads 'who' as the pope." The last is an absence; it holds (search below). Contested tag kept. |
| A-M1 | CLOSED | "The next year Pope Paul III called a council to Trent." Bull "MDXLII ... eleventh of the calends of June" (WAT l.12141-12142) against the recess of 28 July 1541 (SARPI l.16158). |
| A-M2 | CLOSED | "Pallavicino says neither side received the articles." (PALL l.28300-28302, "né quegli articoli furono riceuuti da veruna delle Parti"). |
| A-M3 | CLOSED | Brief "nor the agreed articles"; teaser and `knownFor` "reached a formula on justification". |
| A-M4 | CLOSED | "The two papal envoys saw that Gropper wrote it, Pallavicino says." PALL l.27494-27496 (OCR "fuor folo col Nunzio Morone, fè portar dal Granuela vn libro al Legato"); l.27516-27518 ("il legato insieme col Nunzio e col Groppero; e di leggieri s'accorsero i primi due per varij argomenti, che'l terzo n'era l'Autore", normalized from OCR "vari/ argomenti,cbe'l terzo n^ra l'Aiito- re"). The fixer's corrected range (l.27516-27518 for the review's l.27512-27514) is right. Claim 89: Calvin's "The Bishop of Modena, son of Jerome Morone, has been sent separately, under the title and designation of Nuncio" (CLET1 l.10978-10979) supports "Calvin: Morone was sent as nuncio". Claim 34's new range l.27516-27524 covers the twenty places and Gropper's correcting them. |
| A-M5 | CLOSED (moot) | Hand sentence deleted. Claim 20 kept for entry `people` (Charles V); unchanged. |
| A-M6 | CLOSED | "The Venetian friar Paolo Sarpi was hostile to the papal court. The Jesuit Sforza Pallavicino answered him." SARPI "Father Paul the Venetian, of the Order of the Servi" (round 1, l.679-680); PALL l.24-33 ("SFORZA PALLAVICINO DELLA compagnia DI GESV ... rifiutasi ... vn'Istoria ... fotto nome di Pietro Soaue Polano"). "Answered him" is fair for "rifiutasi". Dropping "that" in "a book the emperor's minister Granvelle gave the legate" changes nothing. |
| A-M7 | CLOSED | Entry `uncertain[10]` "saw from various signs" ("per varij argomenti", PALL l.27517); `people` Gropper "the legate and nuncio saw he wrote the Book". "A man he hated" for "à lui odiosissimo" (PALL l.27536-27537). |
| A-M8 | CLOSED | `uncertain[7]` opens "Whether justification was truly agreed." |
| A-M9 | CLOSED | "il Vicelio" alone in `uncertain[10]` and X6 (PALL l.27536, "del Vicelio"). |
| A-M10 | CLOSED | Entry Granvelle: "'was rejected with harsh expressions' when presented to him" (CLET1 l.11903-11905, "when it was presented to Granvelle, was rejected with harsh expressions"; the passive is kept). "His reply 'cut off all hope'": CLET1 l.11951 "Granvelle, when he had cut" and l.11962 "off all hope on the part of our friends by his reply", split by a footnote and page break, under the heading "12^^ May 1541" (l.11948). Claim 90 is verbatim across the break, and its date is right. |
| A-M11 | CLOSED | `issue[3]` "Pallavicino adds the emperor's proviso, 'always saving' the decision and constitution of Augsburg." PALL l.27359-27360 (OCR "(faina fempre la conclnfme t la cofiitHXfom Angufia)"), inside the emperor's own proposal (l.27354-27360). Claim 10 marks the normalized reading; widened range l.27352-27360 now covers it. |
| A-M12 | CLOSED | Bull moved to the head of `writtenLater`; `fromTheCouncil` removed. Entry `record` still calls it "an act of the papacy, not of the colloquy". |
| A-M13 | CLOSED | README: "... with Faber's from the Catholic side, set against two rival histories." "Rival" (the worker's change from "hostile") is right: Pallavicino is not hostile to the Catholic side, and the brief itself says "Two rival historians". Faber's letters from the city are two (12 March via IGN22 l.7027-7029, used in the entry; 12 May, FAB l.13514, in the brief), so the plural is true. |

## New findings

### Blocking

None.

### Substantial

**A2-S1. Substantial (length: a clause that carries no decision, side or source the story needs).**

- Brief p.2, sentence 3: "The emperor Charles V, Calvin thought, wanted peace, for he feared the Turks and trouble with France." (17 words.)
- "Wanted peace" places the emperor's aim with its witness, and stays. The clause "for he feared the Turks and trouble with France" gives the background to that aim. No decision of the colloquy, no side's stand on any article, and no source turns on it. It is already in the entry, `issue[1]` ("He feared the Turk, and an uncertain peace or open war with the king of France"), from CLET1 l.11032-11034.
- Cut alone, the brief is 391 words but Flesch falls to 59.94 (`grade_text` on `rg_cut1.txt`). The brief's short plain words are carrying its readability. So the cut is paired with a word-neutral, more plain rendering in paragraph 6: "unclear" becomes "not clear". "Per la dubbietà loro" (PALL l.27655-27656) is rendered as faithfully either way.
- Fix, brief p.2: `The emperor Charles V, Calvin thought, wanted peace, for he feared the Turks and trouble with France.` → `The emperor Charles V, Calvin thought, wanted peace.` (8 words.)
- Fix, brief p.6: `because their meaning was unclear.` → `because their meaning was not clear.`
- Result (`rg_cut2.txt`): 392 words, 2.45 min (2:27), FK 7.96, Flesch 60.25, longest sentence 25 words (the close). With A2-M1 also applied (`rg_all.txt`): 396 words, 2.48 min (2:29), FK 8.00, Flesch 60.19, longest 25.
- Regenerate the audio from the fixed brief with `mkaudio.py`.

### Minor

**A2-M1. Minor (a new sentence placed so it reads as a verdict its witness does not give).**

- Brief p.6: "He wrote to his friend Farel, 'You will be astonished, I am sure, that our opponents have yielded so much.' The Jesuit Peter Faber was at the Diet. On 12 May he wrote that the faith's business went on in great doubt. In Rome, Pallavicino says, the agreed words did not satisfy, because their meaning was unclear."
- Placed between Calvin's joy at the formula and Rome's doubt on it, Faber's sentence is heard as the Catholic eyewitness's doubt on the justification formula. His letter does not say so. It is to the scholastics at Paris "de Ratione studendi" (FAB l.13292-13293). The sentence goes on to trusting God because "media quibus utimur nihil sint in hominum judicio", and then to winning back "qui ab illa recesserunt" (FAB l.13476-13486). It names neither the colloquy, the formula, nor justification (search below). The entry already says so ("does not name the talks", `uncertain[7]`); the brief does not.
- This is the batch 1 lesson: a fix's new text claiming more than its witness through placement. The claim itself, that Faber wrote this on 12 May, is right, so it is minor.
- Fix, brief p.6: `On 12 May he wrote that the faith's business went on in great doubt.` → `On 12 May, without naming the talks, he wrote that the faith's business went on in great doubt.` (18 words.) With A2-S1 the brief is 396 words, Flesch 60.19 (`rg_all.txt`). Applied alone, it is 404 words (`rg_faber.txt`), over the ceiling, so it goes with A2-S1 or not at all.

**A2-M2. Minor (a translation that shifts the witness's subject).**

- Entry `uncertain[7]`: "He says the business of the faith went forward 'valde ambigue', very doubtfully, leaving them to trust in God alone."
- Faber: "et eo modo ut in Deo solum immediate confidamus" (FAB l.13476-13477), "in such a way that we trust directly in God alone", as records claim 88 renders it. His "we" is himself with his readers, whom he calls "fratres nostri" (l.13307). "Leaving them" has no clear antecedent, and a reader takes "them" to be the theologians at the talks.
- Fix, entry `uncertain[7]` last sentence: `He says the business of the faith went forward 'valde ambigue', very doubtfully, so that he and his readers trust in God alone.` (21 words.)

## Length test

Before: 400 words, 2:30 at 160 wpm, Flesch 60.35, FK 8.02. Sentence by sentence (word counts by `grade.py`'s split):

1. "In March 1541 Cardinal Gaspar Contarini ... called Ratisbon." (21) Keep. Date, legate and place; "Ratisbon" is needed for the bull's "diet of Ratisbon" in the close.
2. "He made so many crosses, John Calvin wrote, ..." (24) Keep. The Protestant eyewitness's own voice on the legate, and the brief's one vivid image.
3. "Calvin, a Protestant at Strasbourg, had come as a deputy." (10) Keep. Places the main witness and his side (A-S1).
4. "Contarini, he wrote, wished to bring the Protestants 'under the yoke ...'" (15) Keep. The Protestant reading of the legate's aim.
5. "The emperor Charles V, Calvin thought, wanted peace, for he feared the Turks and trouble with France." (17) Cut the clause after "peace" (A2-S1).
6. "None of the colloquy's papers is among our sources ..." (19) Keep. The record caveat (C2).
7. "Calvin's letters stand in for them." (6) Keep. Names what carries the story.
8. "Two rival historians of the Council of Trent tell it too." (11) Keep. Places the two later witnesses as later.
9-10. Sarpi's and Pallavicino's labels (11, 6). Keep. Each historian's side, once.
11-13. The six named (10, 12, 12). Keep. The colloquy's make-up, both sides.
14-15. The Book and its author (12, 11). Keep. Granvelle's part and Pallavicino's attribution.
16-17. Original sin, free will, justification (10, 12). Keep. The agreement, with Calvin's words.
18. The letter to Farel (20). Keep. The Protestant side's own surprise at what the Catholics yielded. "His friend" tells the listener who Farel is.
19-20. Faber (8, 14). Keep. The Catholic eyewitness from the city (A-S1); see A2-M1 for its tag.
21. Rome's doubt (15). Keep. The README's named reason.
22-25. The Supper (5, 14, 4, 19). Keep. Sentence 22 names the subject that Calvin's "There stood" needs. Sentence 24 gives the word that sentence 25's "refusing the word" points back to. Calvin and Pallavicino tell the break from the two sides.
26-28. The recess (16, 23, 7). Keep. Sarpi's date and decree, Calvin's terms, Pallavicino's refusal.
29-30. The bull (11, 25). Keep. What came of it, in the Curia's own voice.

No other cut passes. Every other sentence carries a decision, a side, or a witness tag, and the floor leaves no slack: two other trims tried (merging the Faber pair, `rg_merge.txt`, Flesch 59.73) fail it.

After A2-S1: 392 words, 2:27, Flesch 60.25, FK 7.96, longest 25. After A2-S1 and A2-M1: 396 words, 2:29, Flesch 60.19, FK 8.00, longest 25.

**README line.** "Colloquy of Regensburg (about 2:30)" stays true after the cuts (2:27 or 2:29). Its reason still holds: every stage it names keeps its witness, and Rome's doubt keeps its sentence. No change proposed.

## Verified

- **Brief quotes (changed and unchanged, re-run).** "that for two days afterwards his arm, I think, must have felt the fatigue of it" (CLET1 l.10976-10977); "under the yoke of subjection without bloodshed" (l.10979-10980); "was accepted on both sides" (l.11857-11858); "You will be astonished, I am sure, that our opponents have yielded so much" (l.11858-11859). All verbatim. The rest were not changed in round 1 and were verified there.
- **New entry and records quotes.** "was rejected with harsh expressions" (CLET1 l.11905); "cut off all hope" and "had cut off all hope on the part of our friends by his reply" (l.11951, l.11962); "on the part of our adversaries" and "on our side" (l.11620-11621); "valde ambigue" and the whole Faber sentence (FAB l.13476-13483); "salua sempre la conclusione e la costituzione d'Augusta" as a normalized reading (PALL l.27359-27360); "fuor solo col Nunzio Morone" (PALL l.27496, OCR "fuor folo"); "il Vicelio" (l.27536). All verbatim or marked as normalized.
- **Translations.** "Went on in great doubt" and "very doubtfully" for "valde ambigue procedit": faithful. Claim 88's whole-sentence translation adds nothing. "Saw" for "s'accorsero": faithful. "Always saving" for "salua sempre": faithful. Entry "leaving them" is not (A2-M2).
- **Split and joined sentences.** "The Venetian friar Paolo Sarpi was hostile to the papal court. The Jesuit Sforza Pallavicino answered him.": each claim with its own man. Entry Granvelle `part`, split into two: Pallavicino's facts tagged "(Pallavicino)", Calvin's tagged "(Calvin)". Entry `uncertain[10]`, split into two: both Pallavicino's, under "Only Pallavicino tells it". Entry `uncertain[7]`: Faber's two sentences tagged to him.
- **Dates.** Faber 12 May 1541 (FAB l.13514). Calvin's Granvelle letter 12 May 1541 (CLET1 l.11948). Legate's entry 12 March 1541 (IGN22 l.7027-7028, "Ratisbona scribens 12 Martii I541: «Esta tarde ha hecho su entrada en esta ciudad el Legado Reverendísimo Contareno»").
- **Audio.** Equals the brief bar the two tags.
- **Census.** No tradition id or census claim changed; not queried.

## Searches run

All case-insensitive over `cic/texts/*.txt`, with `[[:space:]]+` between words.
- **"No held witness reads 'who' as the pope" (X7).** Calvin's phrase or a parallel: `so[[:space:]]+many[[:space:]]+crosses|distributed[[:space:]]+so[[:space:]]+many|tot[[:space:]]+cruces|tant[[:space:]]+de[[:space:]]+croix|tante[[:space:]]+croci|so[[:space:]]+viele[[:space:]]+kreuz`: 20 files, crossed with the 60-odd files that name Contarini (`contarin|contaren`). The only file in both is CLET1. Pallavicino on the legate's arrival (`cruc|croc|croix|cross|kreuz|benedi|blessing|segn`, PALL l.27380-27470): no hit. Sarpi (`cross|bless`, SARPI l.15640-15760): no hit. Boero's only Contarini line (l.2940) is the legate's appointment. The absence holds.
- **"He does not name the colloquy" (claim 88; entry "does not name the talks").** Faber's letter, FAB l.13296-13516, for `collo|diæt|diaet|diet|conven|imperat|caesar|cæsar|legat|contar|granv|protest|lutheran|hæretic|haeretic|justif|iustif|concord`: one hit, "contra hæreticos" (l.13495), on letters' weakness against heretics. No name of the colloquy, the Diet, the formula or justification. The absence holds.

## Counts

Blocking 0, Substantial 1, Minor 2.

---

## Council profiles, era 7 batch 2, round 2: Part B (Council of Trent 1545-1563)

**Council.** `council-of-trent`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/council-of-trent.brief.txt`, `audio/council-of-trent.audio.txt`, `council-of-trent.entry.json`, `records.json` key `council-of-trent` (equal to `working/records_council-of-trent.json`, checked by script; 144 claims, 10 contested claims, 9 absent details), and the README line "Council of Trent (about 2:30)". The scope is `git diff f6c9d034 HEAD` for these files, against round 1 Part B (`R1_review.md` l.134-282) and `R1_changes.md` Part B (l.75-150).
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm, at the cap). `grade_text`: FK 7.61, Flesch 61.99. 32 sentences. Longest sentence 22 words ("The council ruled that Scripture and the unwritten traditions, ..."). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag. Checked by `diff` after stripping the two tags.
**Entry.** No sentence in any entry string is over 25 words (script check). The JSON parses.
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. No repo file was edited. No model, network or paid calls were made.

Abbreviations as in round 1 (W, S, P1, P2, P3, C1, BOC, ABD, GIUS). Also: BENSOW = `bensow_svenska-kyrkans-bekannelseskrifter-swe_bensow1912.txt`; REUSCH = `reusch_indices-librorum-prohibitorum-sechzehnten-jahrhunderts-deu-lat_1886.txt`.

## Verdict: REVISE (no blocking, one substantial, six minor)

The blocking point B-B1 is closed. The false absence is gone from every profile string. The Smalcald Articles, the Formula of Concord and Pallavicino's account of the envoys are now in the entry and records, each with its own witness and year. Every new quote is verbatim. The new, narrower absence (no Württemberg or Saxon confession held) survives a wide search. Sarpi and Pallavicino are each given as theirs in every changed string.

The one substantial point is the new Formula of Concord sentence in the brief. It says the Formula rejected "the council's decree on good works". The acts have no decree of that name: the Formula's target is the Decree on Justification (canon XXIV, by Jacobs's note). The sentence also gives the condemned side no words of its own, which was the reason for B-S1. The Formula's own words fit in two more words (B2-S1).

The six minor findings are:
- in `uncertain[7]`, Pallavicino's pope is turned into "the cardinals" as the ones who approved, and "held back" overstates what the officials did;
- the records' absent detail still says both confessions were "handed in", against the fixer's own correction;
- the new Book of Concord `record` witness reads as if Luther wrote the Formula;
- the README line now runs the Formula of Concord into "four decrees";
- two small length cuts (3 words and 1 word) that keep every witness tag.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| B-B1 | CLOSED, with a new point | Entry `issue[6]`, `issue[7]`, `uncertain[11]`, `outcome` (Lutherans), `traditions` (Lutheran note), `record[6]`, `people` (Maurice), the new BOC `record` and source; records `absent_details[1]` note and claims 137-140. Checked in context: BOC l.15748-15792 (Smalcald title "WRITTEN BY DR. MARTIN LUTHER IN THE YEAR MDXXXVII"; "a truly free Christian Council", l.15784; "the Romish court is so dreadfully afraid of a free Christian Council", l.15791-15792); W l.11719-11738, 11976-11990 (Mantua 1537, "the city of Mantua was refused us", Vicenza, Trent); BOC l.30993-30999 ("the decree of the Council of Trent, ... should by right be rejected, viz. that our good works support salvation"), l.31038 (Jacobs's "Sess. vi., Can. xxiv."), l.27925 ("Bergen May 29th, 1577", closing "this Epitome"); P2 l.22382-22430 (Württemberg envoys in the morning, "la lor Confessione in mano del Segretario"; the Saxons "verso la sera", "Oratori di Maurizio Elettor di Sassonia"; "à cinque capi"), l.22530-22540 (the fourth head, "innanzi à tutto"). The entry's correction that only the Württemberg confession is said to be handed in is right; the records' `detail` line was left stale (B2-M2). The brief sentence is B2-S1. |
| B-S1 | CLOSED, with a new point | The brief line is in place and the offsetting cuts are applied. The residence sentence now reads "bound bishops to reside, grounding their duties in divine precept, but did not call residence divine right", which matches W l.19388-19422 ("by divine precept, enjoined on all to whom the cure of souls is committed"; "obliged to personal residence in their own church or diocese"). The new Formula line misnames the decree and carries no Lutheran words (B2-S1). |
| B-S2 | CLOSED | `decided[10]` and claim 67 now follow W l.19909-19938: the poor chosen first, then the bishop assigns some, keeps the rest, and "shall supply the place of those who have been withdrawn by others, that so this college may be a perpetual seminary". The fixer's correction of the review's "fills their places" is right. |
| B-S3 | CLOSED, with a new point | Contested claim 5 and claim 141 are in place and cite P3 l.57848-57867, 58030-58039. The entry's new wording has two small slips against those lines (B2-M1). |
| B-S4 | CLOSED | Claims 93, 106, 107, 111 and 132 are "modern reconstruction". The source title, the new `writtenLater` row and the `record[0]` note are in place (W l.24415, "From Le Plat's edition ... 1779"). |
| B-M1 | CLOSED | "In a letter Jules Bonnet's edition dates to 1545" (C1 l.120, 20043, 20050). |
| B-M2 | CLOSED | "Two rival histories tell the debates." |
| B-M3 | CLOSED | "Abdisho, a patriarch from Assyria" in the brief; the numeral is also gone from `traditions`, `record[2]` and the source author. `people` keeps the census name. |
| B-M4 | CLOSED | "In 1562 the fathers split ..." |
| B-M5 | CLOSED | Teaser: "for a time at Bologna" (W l.14722, 14779-14783). |
| B-M6 | CLOSED | Claim 53 note: "OCR 'deterred' and '2.2.' (S l.8790)". S l.8788-8790 re-read. |
| B-M7 | CLOSED | `uncertain[2]` and contested claim 9 now say the two agree "if Sarpi's 25 leaves the legates out". S l.18406 and P1 l.35131-35135 as in round 1. The conditional is fairer than round 1's "plainer reading". |
| B-M8 | CLOSED | `attended[2]` and claims 142-143: W l.7182-7184 ("one hundred and six bishops, four mitred abbots, and four generals"); GIUS l.3650. Giussano's figure tagged Inferential-Thin as a round number. |
| B-M9 | CLOSED, with a new point | The README line now names Calvin, Jewel and the Saxon envoys "as Sarpi gives them". The added Formula clause makes the list misread (B2-M4). |
| B-M10 | CLOSED | `record[2]` kind "participant", with "read at the session of 17 September 1562 (Sarpi, Pallavicino)"; source moved to `fromThoseThere`; claims 123-126 "participant". |
| Sarpi label | CLOSED | Brief: "The Venetian friar Paolo Sarpi was hostile to the papal court." Rests on his own frame against the "exorbitant power" of the See of Rome (S l.8826-8836) and "Father Paul the Venetian, of the Order of the Servi" (S l.677-678). Pallavicino stays "The Jesuit ... wrote to refute him" (P1 l.25-33). |

## New findings

### Blocking

None.

### Substantial

**B2-S1. Substantial (the new Formula of Concord sentence misnames the decree it answers and gives the condemned side no words of its own).**

Location: brief, paragraph 5: "In 1577 the Lutheran Formula of Concord rejected the council's decree on good works."

- The acts have no "decree on good works". The decree in question is titled "DECREE ON JUSTIFICATION" (W l.12960). Its canon XXIV condemns anyone who says "the justice received is not preserved and also increased before God through good works" (W l.13781-13785). Jacobs's footnote ties the Formula's rejection to "Sess. vi., Can. xxiv." (BOC l.31038). A listener hearing "the council's decree on good works" will take it as a separate decree.
- What the Formula rejects is a teaching it reads in that decree: "the decree of the Council of Trent ... viz. that our good works support salvation" (BOC l.30994-30999). The Swedish text agrees independently: "Tridentinska mötets beslut ... nämligen att våra goda gärningar bevara saligheten" (BENSOW l.26802-26807).
- B-S1 asked for the condemned party in its own words (pattern rule 3, C3). The narrator's paraphrase gives none. The Formula's own clause fits in two more words. The paragraph's subject is already the council, so "the decree" is clear.
- Fix, brief paragraph 5: `In 1577 the Lutheran Formula of Concord rejected the decree "that our good works support salvation."` (16 words, +2).
- Same wording in the entry, fix to match: `traditions` Lutheran note, `The Formula of Concord of 1577 rejects 'the decree of the Council of Trent' on good works.` becomes `The Formula of Concord of 1577 rejects 'the decree of the Council of Trent' that 'our good works support salvation'.` (19 words).
- The year holds. The only dated line is the Epitome's "Bergen May 29th, 1577" (BOC l.27925). Bensow says the Epitome and the Solid Declaration were finished together at Bergen as one book and then signed (BENSOW l.31604-31617). So "In 1577" for the Formula as a whole rests on two held lines. The entry's "Its first part is signed at Bergen, 29 May 1577" is exact and should stay.
- With the length cuts below, the brief is 398 words (scratch copy `/tmp/claude-0/-home-user-CIC-Project/af34472b-cc0a-504c-a9aa-6aa7f1f6ba1a/scratchpad/trent_r2_all.txt`). Regenerate the audio from the fixed brief.

### Minor

**B2-M1. Minor (a fix in `uncertain[7]` moves Pallavicino's act from the pope to the cardinals, and "held back" overstates the officials).**

Location: entry `uncertain[7]`: "Both historians say some in Rome first held back from confirming outright. ... The cardinals then approved by common consent."
- Pallavicino's subject is Pius IV: "addomandate secondo il rito le sentenze de' cardinali, di comune consentimento l'approvò e 'l confermò per Bolla da tutti loro segnata" (P3 l.58034-58040). The pope asked the cardinals' votes, then approved and confirmed by common consent.
- The officials did not hold back. They "disconsigliarono il papa dell'assoluta confermazione" (P3 l.57848-57850), advised the pope against it. Sarpi's eight cardinals "were almost all of opinions that it was fit they should be moderated before the Confirmation" (S l.70324-70326). Both are advice against confirming outright.
- Fix: `Both historians say some in Rome first argued against confirming outright.` and `In the consistory, he says, the pope asked the cardinals' votes and confirmed by common consent.` (11 and 16 words).

**B2-M2. Minor (a records line left stale by the fixer's own correction).**

Location: records `absent_details[1]` `detail`: "The Württemberg and Saxon confessions handed in at Trent, 1551-52".
- The fixer corrected the entry because "P2 l.22388-22390 attests only the Württemberg confession handed in; no read line has the Saxons hand one in". Sarpi's lines say the same: the Saxon speech was "presented ... in Writing" (S l.36653-36654), and the second embassy "were to tender the Confession of their Doctrine", in the future (S l.36658-36660).
- Fix: `"detail": "The Württemberg Confession handed in at Trent in 1552, and any Saxon confession"`.

**B2-M3. Minor (a witness string that reads as if Luther wrote the Formula).**

Location: entry, new `record` item, `witness`: "Martin Luther, Smalcald Articles (1537), and the Formula of Concord (1577), in Jacobs's English Book of Concord". Luther died before Trent's first period ended. The Formula is not his.
- Fix: `"witness": "Martin Luther's Smalcald Articles (1537), and the Lutherans' Formula of Concord (1577), in Jacobs's English Book of Concord"`.

**B2-M4. Minor (README list misreads).**

Location: README, "Council of Trent (about 2:30)": "... the Protestant refusal, in Calvin's and Jewel's own words and the Saxon envoys' as Sarpi gives them, with the Lutherans' later answer in the Formula of Concord, four decrees, ..."
- The Formula clause runs straight into "four decrees", so it reads as part of the refusal list. In the brief it sits with the decrees it answers.
- Fix: `The brief keeps only the closing scene, the calling, the Protestant refusal (Calvin's and Jewel's own words, the Saxon envoys' as Sarpi gives them), four decrees with the Lutherans' later answer in the Formula of Concord, the two disputes the historians fight over, and the reach of the close.`
- The length "about 2:30" stays true after the cuts below (398 words, 2:29).

**B2-M5 and B2-M6.** Two small length cuts. See the Length test.

## Length test

The brief runs 400 words, the cap. I tested every sentence. The council ran eighteen years. The brief carries one scene, the calling, three refusing voices, four decrees with the Lutheran answer, the two disputes the historians fight over, and the reach of the close. Each carries a decision, a side or a source. Every attribution is a witness tag. These include "wrote Servanzio, as Waterworth quotes his diary", "Jules Bonnet's edition dates", "by Sarpi's count" and "Each historian counts the votes his own way", which keeps the residence vote with both historians. Two sentences carry a few words of slack:

| # | Sentence | Verdict |
|---|---|---|
| 1-4 | Lorraine, the acclamations, the anathemas, Servanzio | Keep. Scene, the acts, the condemnation, a witness chain. |
| 5-9 | The acts in Waterworth; two histories; Sarpi; Pallavicino | Keep. Sources and their sides. |
| 10-11 | "Pope Paul III called the council in 1542. His bull chose Trent because ..." | Trim 1 word (B2-M6). |
| 12 | Opening, 25 prelates by Sarpi's count | Keep. A count with its witness. |
| 13-14 | Calvin | Keep. |
| 15-16 | "In 1552 envoys from Saxony came. Before anything else, Sarpi says, they asked ..." | Trim 3 words (B2-M5). |
| 17 | Jewel | Keep. |
| 18-21 | Four decrees and the Formula | Keep; B2-S1 adds 2 words. |
| 22-27 | Bologna and residence, each historian as his own | Keep. |
| 28-30 | 255 and 168, the confirmation, Abdisho | Keep. |
| 31-32 | The two rival judgments | Keep. |

**B2-M5. Minor (length, 3 words).** `Before anything else, Sarpi says, they asked the council to affirm that it stood above the pope.` becomes `Sarpi says they first asked the council to affirm it stood above the pope.` (17 to 14 words). "First" is Sarpi's own word: "prayeth the Assembly, That they would first repeat, approve, and ratifie the Article of the Superiority of the Council above the Pope" (S l.36638-36640). The witness tag stays.

**B2-M6. Minor (length, 1 word).** `Pope Paul III called the council in 1542. His bull chose Trent because the Germans "wished for the city of Trent."` becomes `Pope Paul III's bull of 1542 called the council to Trent, because the Germans "wished for the city of Trent."` (21 to 20 words). The bull stays as the witness to the reason (W l.11976-11986, "we have chosen the city of Trent").

**Counts.**
- Before: 400 words, 2:30 at 160 wpm. FK 7.61, Flesch 61.99. Longest sentence 22 words.
- With B2-S1 alone: 402 words, over the cap. FK 7.66, Flesch 61.74.
- With B2-S1, B2-M5 and B2-M6: 398 words, 2:29 at 160 wpm. FK 7.74, Flesch 61.63. Longest sentence 22 words. No sentence over 25. Scratch copy: `/tmp/claude-0/-home-user-CIC-Project/af34472b-cc0a-504c-a9aa-6aa7f1f6ba1a/scratchpad/trent_r2_all.txt`.
- I found no Substantial length cut. The README's "about 2:30" stays true at 398 words. Its list wording needs B2-M4.

## Verified

- **Every new quote, verbatim.** "the Romish court is so dreadfully afraid of a free Christian Council" (BOC l.15791-15792); "a truly free Christian Council" (l.15784); "the decree of the Council of Trent ... should by right be rejected" and "that our good works support salvation" (l.30994-30999, ellipsis over "and whatever elsewhere is set forth in the same sense"); "that so this college may be a perpetual seminary of ministers of God" (W l.19937-19938); "two hundred and fifty Bishops" (GIUS l.3650); "with all the Prelates, in number 25" (S l.18406); "advice and assent" (W l.24172-24175).
- **Translations.** "la lor Confessione in mano del Segretario" is rendered "handed their Confession to the secretary" (P2 l.22388-22390). "disconsigliarono il papa dell'assoluta confermazione ... per le disposizioni onde a lei diminuiva e l'entrata, e l'autorità" is rendered "advised the pope against an absolute confirmation, since it cut the court's revenue and authority" (claim 141; P3 l.57848-57852). "s'opposero" is rendered "opposed them" (l.57862). All faithful; nothing added.
- **Smalcald dating.** "which the edition dates to 1537" is exact: the date is the edition's heading (BOC l.15762-15764). The preface's "convoked a Council last year to assemble at Mantua" (l.15767) fits the bull's Mantua date of 23 May 1537 (W l.11722-11723). "Before Trent met" holds.
- **Pallavicino on the Saxons.** The Saxons "ripetevano le medesime colorite ragioni onde i Protestanti havevan sempre rigettato ogni Concilio" (P2 l.22416-22419). This supports the `traditions` note "refused its terms, by Sarpi's and Pallavicino's accounts". "Colorite" is his hostile word and is not given as fact.
- **Sarpi and Pallavicino, each as his own, in every changed string.** Brief: "by Sarpi's count", "Sarpi says" (twice), "Pallavicino cites", "Each historian counts", "Sarpi judged", "Pallavicino writes". Entry `issue[7]`, `uncertain[2]`, `uncertain[7]`, `uncertain[11]`, `record[6]`, contested claims 5 and 9: each claim carries its historian. Waterworth's leaning to Pallavicino is given as his (`uncertain[0]`).
- **Residence decree.** W l.19384-19422, as above. "Assistunt" footnote (l.19413-19414) unchanged.
- **The bull of 1542.** Claim 139 against W l.11719-11738 (Mantua "on the tenth of the calends of June, in the year 1537"; "the city of Mantua was refused us") and l.11976-11986 (Vicenza; "they (the Germans) wished for the city of Trent").
- **Brief and entry agree.** The brief's Formula, Saxon, Calvin, Jewel, Bologna and residence lines match the entry and records. Audio equals brief plus two tags.

## Searches run

- **Württemberg and Saxon confessions (the new absence in `uncertain[11]` and `absent_details[1]`).** Over all `cic/texts`: `confessio\s*(virt|wirt|wurt|würt|vuirt|vvirt)|(wirt|wurt|würt|virt)[a-z]*\s+confession|w(ü|ue|u)rttembergische[sn]?\s+bekenntnis|wirtembergische[sn]?\s+bekenntnis|confessio\s+saxonica|saxon\s+confession|repetitio\s+(augustanae\s+)?confessionis|confessio\s+doctrinae\s+saxonicarum|s(ä|ae)chsische[sn]?\s+(konfession|confession|bekenntnis)|confession\s+(de\s+)?(saxe|wurtemberg|wirtemberg)|confessione\s+(sassonica|virtemberg)`, case-insensitive. Hits: six false hits on "virtutis/virtute confessionis" (Abelard, Dunstan, Gérard de Frachet, Origen, PL 11, Étienne de Bourbon), and REUSCH l.16571-16573, the Index's titles "(Confeflsio Sazonica.)" and "(Confessio Wirtembergensis.)". Those are mentions, not the texts. File names with `melanch|brenz|brentz|wirtemb|wurtt|wuertt|saxon|sachs` give no confession of 1551-52. The absence holds.
- **Sarpi on a confession handed in.** `conf[eſ][sſ]` in S l.35900-36900: only l.36660, "were to tender the Confession of their Doctrine" (future). Hence B2-M2.
- **The Formula's date.** `1577|1580|MDLXXVII|MDLXXX` in BOC: only the header (l.2, 8) and l.27925. `signing|subscri|bergen|torgau` in BOC: the Preface's Torgau "in the year '76" (l.648) and its seals (l.1026), with no year for the Solid Declaration. Over all `cic/texts`, `formula\s+(of\s+)?concord|concordiae|konkordieformel|concordienformel|solida\s+declaratio`: 19 files. Among them, BENSOW l.31604-31617 (Bergen, epitome with solida declaratio, signed) and `arndt_true-christianity_boehm-schaeffer1868.txt` l.318, 628 ("published in 1580"). So "In 1577" holds on BOC l.27925 with BENSOW.
- **The Formula's target in the acts.** `CANON\s+XXIV|preserved\s+and\s+also\s+increased|on\s+justification` in W: "DECREE ON JUSTIFICATION" (l.12960), canon XXIV (l.13781-13785). No "decree on good works" title. Hence B2-S1.
- **Trent in the Formula, independently.** `trident|tridentin` in BENSOW: l.26805, "Tridentinska mötets beslut", the same passage.

## Counts

Blocking 0, Substantial 1, Minor 6.

---

## Council profiles, era 7 batch 2, round 2: Part C (Diet of Augsburg and the Religious Peace 1555)

**Council.** `diet-of-augsburg-1555` (distinct from `diet-of-augsburg-1530`).
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/diet-of-augsburg-1555.brief.txt`, `audio/diet-of-augsburg-1555.audio.txt`, `diet-of-augsburg-1555.entry.json`, `records.json` key `diet-of-augsburg-1555` (equal to `working/records_diet-of-augsburg-1555.json`, checked by script: 105 claims, 8 contested claims, 12 absent details), and the README "Batch 2" line "Diet of Augsburg 1555 (about 2:30)". Scope: `git diff f6c9d034 HEAD` on branch `claude/cft-councils-era7-batch2`, checked against `R1_review.md` Part C and `R1_changes.md` Part C.
**Brief.** 400 words (2.50 min at 160 wpm, at the ceiling). `grade_text`: FK 7.81, Flesch 63.11. Longest sentence 25 words ("Religion was to be handled in an assembly of Catholics and heretics, and he thought a legate no fit witness to such a monstrous thing."). None over 25.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag. Checked by `diff`.
**Entry.** JSON parses. No sentence in any entry string runs past 25 words (script check).
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. Read and grep only. No repo file edited. No model, network or paid calls.

Abbreviations as in round 1: POL5, PALL2, SARPI, MIRBT, BOSS, SAL, NAD1, CAL4.

## Verdict: PASS WITH MINOR FIXES (no blocking, no substantial, two minor)

Both round 1 blocking points are closed, and their fixes are right against their source lines.

- **Polanco (C-B1).** The brief now says "The rest comes from Polanco's chronicle". In context Polanco writes of the Jesuits at Augsburg in the third person ("praeparabant se nostri", POL5 l.15377). The editors' note has him writing from Rome to Nadal at Augsburg ("Ita Polancus, ex com., Patri,Nadal, 1.* Aprilis 1555", l.15394-15395). "Chronicle" is the right kind for him. The earlier sentence that carries his scene ("writes the Jesuit Juan Alfonso de Polanco") makes no claim that he was there. The entry's new `uncertain[0]` names "Nadal's and Salmerón's letters from the city". That holds: Nadal dates letters "Augustae, 30 Martii 1555" and "Da Augusta, 30 di Margo 1555" (NAD1 l.16761, l.17057), and Salmerón writes "De Augusta oy primero de Setiembre de 1555" (SAL l.8585).
- **Pallavicino and Sarpi (C-B2).** The join is gone. Sarpi's quote now stands in its own sentence with Sarpi, and his cities are the Interim cities (SARPI l.38433-38442). The next two sentences each sit with Pallavicino. Their words match PALL2 l.27522-27529: "inuogliati dalla dissoluzione de' circonuicini", "di viuere anch'essi sciolti dall'osseruanza de' mandamenti ecclesiastici", "seguir la Religion de' Padroni, ò à partirsi". "Their neighbors' freedom" is fair for the neighbors' "dissoluzione" that the subjects asked to share.

Two minor points remain. First, "pleading plain necessity" does avoid the lost word, but it turns Ferdinand's view ("parendogli") into something said in his answer (C2-M1). Second, one length cut (C2-M2).

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| C-B1 | CLOSED | Brief p.5 and entry `uncertain[0]` as above. POL5 l.15369-15381, l.15394-15395; NAD1 l.16761, l.17057; SAL l.8585. |
| C-B2 | CLOSED | Brief p.11 as above. PALL2 l.27522-27529; SARPI l.38433-38442. Each of the three sentences keeps its own witness. |
| C-S1 | CLOSED, with a new point | The brief no longer uses the lost word. PALL2 l.27568-27576 reads "Mà il Rè, parendogli e che / nelle concezioni dannofe acattolici la ma- / nifefia necessità l'hauefse tenuto lungi da-* / e che nelle cofe arbitrarie à sé ... rifpofe con maniere più rifentitc". Entry `outcome[2]` ("felt that plain necessity had kept him 'lungi da' ('far from') something ... The next word is lost in our copy"), records `claims[76]` and the new `absent_details[11]` are faithful. The absence holds (searches 1-3). On "pleading", see C2-M1. |
| C-S2 | CLOSED | "Its editor, Gustav Bossert, notes that the duke added the Zwinglians in his own hand." BOSS l.2 "(Gustav Bossert the elder, Editor ...)"; l.9280 "Zwinglischer über der Zeile, von Herzog Christophs Hand". |
| C-S3 | CLOSED | MIRBT l.21736-21742: "caeteris catholicis et Augustanae confessioni addictis statibus et subditis tribuuut, id eliam iis, qui inter illos reformati vocantur, competere debeat". The brief now has "It gave both religions' rights also to those among them called the Reformed." That is faithful, and "among them" keeps the Latin's own reach. Entry `outcome[16]`, `traditions[4].note`, `uncertain[8]` and `record[8].note`, and records `contested_claims[3]` and the claim at the old l.574, all agree. Westphalia now has its own side. "Kept holy and inviolable": l.21625-21627 "rata habeatur sancteque et inviolabiliter servetur". |
| C-S4 | CLOSED | PALL2 l.27415-27438 is one indirect speech, running from "Scusauasi egli di ciò con addurre" to "conchiudeua il Rè in sua discolpa". `calledBy`, `issue[9]`, `uncertain[10]` and records `claims[26]`, `[30]`, `contested_claims[4]`, `absent_details[2]` and `[8]` now give the speech as Ferdinand's defence. `calledBy`'s "sickness and war kept him from German affairs" matches l.27421-27423 ("per malattia di corpo, e per distrazione di guerra applicar l'animo agli affari dell'Alemagna"). Its narrowed absence, "No held source disputes that Charles called it", agrees with SARPI l.38051-38052 ("which the Emperour had intimated") and l.38056-38057 ("in the Emperours name"). |
| C-S5 | CLOSED | `uncertain[14]` and the old records claim on the brief are deleted. |
| C-S6 | CLOSED | The three absence claims are deleted. Each is still in `absent_details`. Sarpi's "very few were come" remains as a claim. |
| C-S7 | CLOSED | `absent_details[4]` now cites CAL4 l.19188-19439 for the two 1555 letters. The fixer's range is right: the Tarnow letter runs on to where Varaglia begins. |
| C-M1 | CLOSED | "A draft order of Duke Christoph of Württemberg, begun in 1556, ordered Anabaptists and Schwenckfelders punished, since the peace did not include them." BOSS l.9113 ("1556 nach September 11. — Mandat ... (ohne Datum)"); l.9310-9313 ("in jüngstem zuo Augspurg ufgeriebtem religionsfridenstand ... mit nichten begriffen, sonder darvon usgesohlossen, an er, leub und gut zu strafen"); l.9322-9326 ("Der erste ... Entwurf ... stammt aus dem Jahr 1556 ... noch Anfang 1557 wurde der Entwurf beraten"). |
| C-M2 | CLOSED | "either religion"; MIRBT l.16317. |
| C-M3 | CLOSED | `knownFor` is one sentence of 25 words. |
| C-M4 | CLOSED | Tail deleted from `issue[5]`. |
| C-M5 | CLOSED | The labels are statements. The fixer rightly applied the "for ever" label at `[5]`. |
| C-M6 | CLOSED | `uncertain[13]` as proposed. |
| C-M7 | CLOSED | `decided[8]` keeps "not held directly from the empire" ("reichsmittelbaren"). |
| C-M8 | CLOSED | SAL l.8448-8450 ("llegamos ... á 20 de Agosto en esta çibdad de Augusta, y con quanta charidad reçebidos de monseñor Rmo. de Verona"); l.8500-8503 ("el Rmo. de Verona se parta luego para Polonia ... nos partyremos de Augusta"). `attended[6]`, `people` Salmerón, `traditions[3].note` and `claims[42]` agree with these lines. |
| C-M9 | CLOSED | SARPI l.38148-38150 "no ſooner arrived in Awsburg, but Pope Julius died, whereof he received advice cight days after". |
| C-M10 | CLOSED | `claims[50]` witness as proposed. |
| C-M11 | CLOSED | PALL2 l.27479-27481 "rimar, effe pur la prefente ferma cd inaiai abile". The quote is in the print's spelling, and the OCR reading is flagged. |
| C-M12 | CLOSED | SARPI l.38469-38470 "did de-|dare with conſent of the Eccleſiaſtical Order". The notes now say the phrase is legible and the terms break off. |
| C-M13 | CLOSED | "vna" (PALL2 l.27399 "vna pende rofa_»"; l.27429 OCR "vua"). |
| C-M14 | CLOSED | The README now reads "The room comes only from Catholic writers, the Jesuits Polanco and Pallavicino and the friar Sarpi". Pallavicino is a Jesuit, as the brief itself says ("the Jesuit historian Sforza Pallavicino"). |

## New findings

### Blocking

None.

### Substantial

None.

### Minor

**C2-M1. Minor (a thought told as speech).** Brief p.13: `Ferdinand answered sharply, Pallavicino says, pleading plain necessity.`
- PALL2 l.27568-27576: "Mà il Rè, parendogli e che nelle concezioni dannofe acattolici la manifefia necessità l'hauefse tenuto lungi da-* e che nelle cofe arbitrarie à sé ... rifpofe con maniere più rifentitc". Pallavicino gives necessity as how things seemed to Ferdinand ("parendogli"). That view is why he answered sharply. Pallavicino does not say what the answer contained. "Pleading" puts necessity into the answer to Paul IV.
- The fixer grounds "pleading" also on "Scusauasi egli di ciò con addurre" (l.27415). But that excuse is the earlier defence in chapter 13: Charles's curt reply, the feuds, Naumburg, and approving what both sides had agreed. It is not the answer to the December complaints in chapter 14, and the word "necessità" is not in it.
- The fix keeps to the legible words, "la manifesta necessità" and "concessioni", and does not use the lost word. Fix, brief (10 words): `Ferdinand answered sharply, Pallavicino says, feeling the concessions plainly necessary.`
- Optional, same point: `uncertain[9]` and `contested_claims[4]` say Pallavicino has him plead necessity. For the chapter 13 excuse, that is fair as a gist. Leave them.

**C2-M2. Minor (length; scene detail with no decision, side or source).** Brief p.1: `Ferdinand, King of the Romans, came out almost a league with bishops and princes to meet him, writes the Jesuit Juan Alfonso de Polanco.`
- "Almost a league" ("fere leucam unam", POL5 l.15371-15372) is true. But it is the only clause in the brief that carries no decision, side or source. The scene and its witness stay without it.
- Fix, brief (21 words): `Ferdinand, King of the Romans, came out with bishops and princes to meet him, writes the Jesuit Juan Alfonso de Polanco.`

## Length test

Each sentence was tested for a decision, a side or a source that the story would lose without it. Numbers are sentence numbers; there are 29.

- 1-4 (scene, Julius's death, Morone's going). These form the opening scene (C8). They show Rome gone before the business began, and they bring in Julius before sentence 5 names him. Sentence 4 is the only place the listener learns the legate took no part. Keep. Cut "almost a league" from sentence 2 (C2-M2).
- 5-6 (Julius's reluctance). This is Rome's stance, in the pope's own terms. Keep.
- 7 (Pallavicino, a century later). This is a witness tag, and it dates the witness. Keep.
- 8 (Mirbt's recess). This names the source and defines "recess" before it is used. Keep.
- 9 (Polanco's chronicle, Pallavicino, Sarpi). This tells the listener whose account stands in (C2), and it is the C-B1 fix. I tested dropping the second and third "from". That saves 2 words but leaves a ragged list of a book and two persons. Not proposed.
- 10 (no Lutheran). This is the absence, stated once (C3). Keep.
- 11 (not 1530). The README requires it. Keep.
- 12-13 (caller, purpose, opening, thin attendance). These carry C4 and C5. "His brother" says why Ferdinand acts for Charles (SARPI "his Brother"). Keep.
- 14-20 (the recess). There are six clauses plus the date. Each is a decided article. "With their wives and children" gives the article's own scope ("mit iren weib und kindern"). Sentence 20 is the acts' side of the Contested "for ever" claim. Keep.
- 21-23 (Sarpi's bargain; Pallavicino's subjects). These are the two witnesses for "rulers choose", each in its own sentence. Keep.
- 24-25 (Paul IV; Ferdinand's answer). This is a decision rejected, with both voices. Keep. Reword sentence 25 per C2-M1.
- 26-27 (Duke Christoph; Bossert). This is the exclusion in use, with its witness tag. Keep.
- 28-29 (Westphalia). This is the reach of the close, and the other side of the Contested exclusion of the Reformed (C-S3). Keep.

No sentence repeats another, and none restates the README's reason. There are no double attributions. Polanco is named twice, but once as the voice of the scene and once in the list of whose account stands in. Each mention does its own job, and the second is the round 1 blocking fix.

**Counts.**
- Now: 400 words, 2.50 min. FK 7.81, Flesch 63.11. Longest sentence 25.
- After C2-M2 alone: 397 words, 2.48 min. FK 7.78, Flesch 63.08.
- After C2-M1 and C2-M2: 399 words, 2.49 min. FK 7.87, Flesch 62.60. Longest sentence 25.

All three were checked with `grade_text` and the batch's `grade.py` on scratch copies (`aug1555.r2.txt`, `aug1555.r2c.txt` in this scratchpad). The Flesch floor holds, and no sentence passes 25 words.

The brief earns close to its full length. It is at the ceiling because it carries six recess clauses, four witnesses and two later texts, not because it was padded. Only one cut is proposed.

**README line.** "Diet of Augsburg 1555 (about 2:30)" is still true at 397-399 words (2:29). No change.

## Verified

- **Every changed or added brief string**, against its source in context: p.5 (POL5 l.15369-15395); p.9 "either religion" (MIRBT l.16317); p.11 (SARPI l.38433-38442; PALL2 l.27522-27529); p.13 (PALL2 l.27560-27576); p.15 (BOSS l.2, l.9113, l.9240-9244, l.9280, l.9308-9326); p.17 (MIRBT l.21622-21627, l.21733-21742).
- **Quotes re-verified verbatim** (OCR and long s allowed for):
  - Sarpi, "The Catholicks were content that the Cities should do as they pleased" (SARPI l.38441-38442, unchanged).
  - Entry, changed or added: 'lungi da' (PALL2 l.27571); 'vna ponderosa scrittura' (l.27399); 'quasi in vna Contradieta' (l.27429); 'in secca forma' and 'Onde à esso Ferdinando ne rimettea la dispositione' (l.27422-27424); 'qui inter illos reformati vocantur' (MIRBT l.21737-21738); 'rata habeatur sancteque et inviolabiliter servetur' (l.21626-21627); 'ferma ed inuiolabile' (PALL2 l.27481); 'with consent of the Ecclesiastical Order' (SARPI l.38469-38470); 'eight days after' (l.38150); 'die Konfession zu Augsburg' (unchanged wording).
- **Translations.** "far from" for "lungi da"; "as if in a counter-diet" for "quasi in vna Contradieta"; "who among them are called Reformed" for "qui inter illos reformati vocantur". All are faithful and add nothing.
- **Split and joined sentences.** All were checked: brief p.11 (one sentence became two) and p.17 (one became two); entry `issue[9]` (three sentences), `outcome[2]`, `uncertain[0]`, `uncertain[8]`, `record[8].note` and `traditions[4].note`. Each claim still sits with its witness. In p.17 the subject "It" is the Peace of Westphalia, and both sentences rest on the same treaty text.
- **Salmerón's letters** dated from Augsburg (SAL l.8435, l.8585), and Nadal's (NAD1 l.16761, l.17057, l.17084, l.17228). These support "letters from the city" in `uncertain[0]`.
- **Schaff** on Frederick III, "threatened with exclusion from the benefits of the Augsburg Treaty of Peace (concluded in 1555)" (schaff file l.1819-1820), supports the new `traditions[4].note`.
- **Audio** matches the brief with the two tags. **AI tells.** None in the changed strings: no empty contrast, no "X and never Y", no summing-up line, no filler.
- **README.** All three batch 2 lines for this council were checked against the brief. "About 2:30" stands.

## Searches run

All over `cic/texts`, case-insensitive. Each one tests the new absence, "the end of Pallavicino's clause is lost; no other copy of book 13 is held".
1. `temperata +natura`: one file, PALL2 (l.27576). The only other `lungi da colpa|tenuto lungi` hit is Muratori 1748 (unrelated).
2. `concessioni +dann|concezioni +dann`: PALL2 only.
3. Files whose title line names Pallavicino: parte1, parte2 and parte3 (1664), and tomo3 libri 17-24 (1846). Book 13 is only in parte2. No Latin version (Giattini) is held. `manifest[ae] +necessit|manifesta +necessità` finds only unrelated medieval and patristic files.
4. "Letters from the city" in `uncertain[0]`: `august` in NAD1 l.16700-17400 and `augusta` in SAL l.8400-8620. Both are held, as listed under Verified.

## Counts

Blocking 0, Substantial 0, Minor 2. Brief: 400 words, 2.50 min now; 399 words, 2.49 min after both proposed fixes (397 words, 2.48 min after the length cut alone).

---

## Council profiles, era 7 batch 2, round 2: Part D (Colloquy of Poissy 1561)

**Council.** `colloquy-of-poissy-1561`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/colloquy-of-poissy-1561.brief.txt`, `audio/colloquy-of-poissy-1561.audio.txt`, `colloquy-of-poissy-1561.entry.json`, `records.json` key `colloquy-of-poissy-1561` (112 claims, 12 contested claims, 7 absent details; equal to `working/records_colloquy-of-poissy-1561.json`, checked by script), and the README "Colloquy of Poissy (about 2:30)" line. Scope: `git diff f6c9d034 HEAD` (branch `claude/cft-councils-era7-batch2`, HEAD `15a6c7bd`), against `R1_review.md` Part D and `R1_changes.md` Part D.
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm, at the ceiling). `grade_text`: FK 7.41, Flesch 66.29. Longest sentence 25 words ("In January 1562 a royal edict ..."). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag (checked against the diff: every changed line in the audio matches the brief's change).
**Reviewer.** Fresh Opus, full effort, first sight of the drafting and the round 1 fixing. Read and grep only; no repo file edited; no model, network or paid calls. Scratch copies at `/tmp/claude-0/-home-user-CIC-Project/af34472b-cc0a-504c-a9aa-6aa7f1f6ba1a/scratchpad/poissy_r2/`.

Abbreviations as in round 1 (HE1, AYM, LAI8, PAL2, SARPI, WAT, MELV).

## Verdict: REVISE (0 blocking, 1 substantial, 4 minor)

The blocking fix holds. Read whole in the History, Beza's sentence on the Supper is a concession and a limit together, and the brief now gives both. The speech's "nous fommes faits participans de fon corps & de fon fang par une maniere fpirituelle, & moyennant la foy, auffi véritablement que nous voyons les Sacremens" (HE1 l.28526-28529) stands behind "truly shared ... by faith". Its distance clause stands behind the second sentence (HE1 l.28512-28517). The narrative puts the concession first, "combien qu'il nous fuft véritablement offert & communiqué en icelle" (HE1 l.28711-28712), as the brief now does. Every round 1 finding is closed, and every changed quote is verbatim.

One new substantial point comes from the D-S1 fix. The brief now has Sarpi speak for "the Catholic side" as "the friar Paolo Sarpi", with nothing about his stance. The entry, this batch's Regensburg and Trent briefs, and D-S5 all place him as hostile to the papal court (D2-S1). Three minor points are in new entry text: an identification of Catherine's two meetings given without its witness, a word ("canonists") that the cited Waterworth lines lack, and a condition told as done. The fourth minor point is the length test: four small cuts, which pay for D2-S1.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| D-B1 | CLOSED | Brief p.4: "Beza said believers truly shared in Christ's body and blood in the Supper, by faith. But in distance of place, his body was as far from the bread and wine as the highest heaven from the earth." Read whole: HE1 l.28512-28533 (speech) and l.28707-28727 (narrative). The speech answers "fi nous rendons Jefus Chrift abfent ... nous refpondons que non". It limits the distance to "quand il eft queftion de fa prefence corporelle", then says that despite the distance "nous fommes faits participans de fon corps & de fon fang par une maniere fpirituelle, & moyennant la foy, auffi véritablement que nous voyons les Sacremens à l'œil". "Truly" is the speech's "auffi véritablement" and the narrative's "véritablement offert"; "shared in" is "faits participans"; "by faith" is "moyennant la foy". "In a spiritual way" is not said, but "by faith" carries it, and nothing is added. "In the Supper" is the speech's context ("la faincte Cène") and the narrative's "en icelle". The order follows the narrative, which is the account of what set off the uproar ("Cefte feule parole ... fut caufe que les prelats commencèrent à bruire", l.28713-28716). Records `claims[109]` (HE1 l.28523-28529, participant) holds it. |
| D-S1 | CLOSED, with a new point | Brief p.2: "It tells the Reformed side, and prints the prelates' own decisions." True: HE1 l.28996-29013, 33690-33729, 33924-35113. Names and first names in place (PAL2 l.1; SARPI l.677-678). Records `claims[110]`, `[111]` in place. See D2-S1: Sarpi's side. |
| D-S2 | CLOSED, with a new point | Entry `calledBy` and records `claims[67]` now put Catherine's "Colloque gracieux" after Lorraine's reply and on the confession. AYM l.25537-25548 read whole: "Depuis ladite Refponce faite ... je trouvé bon que nosdits Prelatz & Evéques entraffent en quelque Colloque gracieux avec lesdits Miniftres fur les Articles de leur dite ConfeJJion de Foi; mais aiant veu que de deux Communications qu'ils avoient faites à deux divers jours ..." Letter dated "le 18. jour d'Octobre 1561" (AYM l.25619-25620, OCR "iS."). Quote verbatim. See D2-M1. |
| D-S3 | CLOSED | Entry `decided[1]`: "After the first session, the History says, ..."; "Baum and Cunitz date the resolution to 10 September, from Vermigli's letter of 12 September." HE1 l.28996 "Sur cefte première entrée de conférence" (no date); note l.29024-29025 "le lendemain de la séance, le 10 septembre, comme cela se voit par la lettre de Vermigli à Bullinger, du 12 sept." `claims[25]` agrees. The second sentence's "They" still reads as the prelates. |
| D-S4 | CLOSED | Entry `datesNote` and `claims[100]`. HE1 l.27895-27898, in the editors' note: "Une autre édition porte le titre : La première Harangue ... le mardy neufiesme jour de Septembre ... recueillie et rédigée par escript, ainsi que ledict de Besze la prononçoit, 1561 in-8°." "Early" is right (1561). `witness_kind` now `modern reconstruction`. |
| D-S5 | CLOSED | Entry `record`: Sarpi "A Venetian Servite friar; Catholic but hostile to the papal court. Pallavicino wrote against him. Our scanned copy is garbled at the date of the first session." SARPI l.677-678 "Father Paul the Venetian, of the Order of the Servi"; l.42787 "The ſecond of September of the King,Queei)," (garbled; "garbled" is right). Pallavicino: "A Jesuit writing against Sarpi; for the papal court." PAL2 l.1 "della Compagnia di Gesù ... rifiutasi ... un'istoria falsa ... sotto nome di Pietro Soave Polano". |
| D-M1 | CLOSED | "Some prelates murmured": HE1 l.28717-28718 "dont les uns difoient : Blafphemavit". |
| D-M2 | CLOSED | "barred from": HE1 l.33717-33718 "leur fera défendue la demeure en fon Royaume". Sentence 24 words. |
| D-M3 | CLOSED | Teaser: HE1 l.33703-33711 "en casque ledit de Beze & fa compagnie ne veulent prefentement confeffer & foufcrire la confeffion dudit faind facrement ... de ne les plus ouïr en façon que ce foit". Sentences 17, 10 and 18 words. |
| D-M4 | CLOSED | Huguenot note. HE1 l.27839-27841 ("douze, avec 22 députés des Eglifes ... appelles & introduis") and l.30629-30630 ("douze miniftres & non plus, fans que mefmes les députés des Eglifes y fuffent admis"). |
| D-M5 | CLOSED, with a new point | LAI8 l.39599-39605 read. See D2-M3. |
| D-M6 | CLOSED | Entry `uncertain[0]`: "Baum and Cunitz show that its Poissy chapter copies La Place in many passages." |
| D-M7 | CLOSED | `claims[9]` carries the OCR note; SARPI l.42787. |
| D-M8 | CLOSED | `claims[104]` `later narrative`. |
| D-M9 | CLOSED | Entry `outcome[8]`, the Scottish `traditions` note, `claims[83]`. MELV l.33940 "[by Mr James Melvill *"]", l.33950-33951 "[letter by MR JAMES MELVILL TO THE BRETHREN ASSEMBLED AT THE CONFERENCE OF FALKLAND.]", l.33964-33966 "as witnesseth Colloquium Poissiaconum in Gallia, anno 1561". Year: running head "THE CONTINUATION OF 1607" (l.33905), Falkland "the 15 of Junij" (l.33936). |
| D-M10 | CLOSED, with a new point | Entry `outcome[7]`, `claims[81]`. WAT l.9099-9102: "the articles proposed at the Conference of Poissy, were secretly submitted to Simonetta, Castagna, Boncompagno, Paleotto, and Castelli, to be examined". Quote verbatim. See D2-M2. |
| D-M11 | CLOSED (README); Open-Gaps entry still to be made | The README line now ends "and so does what came of it, in the crown's, the Catholic historian's and the edict's own words." Open-Gaps has no Poissy or Palatine census entry yet (`grep -n -i "poissy\|palatin"` Open-Gaps.md: one hit, l.3566, "Lewis the Palatine" for Worms). `R1_changes.md` Part D words the entry; the coordinator owns it. |

## Blocking

None.

## Substantial

**D2-S1. Substantial (a partisan witness given a side that is not quite his, and a label out of step with the batch).** Brief p.2: `The Catholic side speaks through Jesuits who came with the pope's legate. So do two rival historians of Trent, the friar Paolo Sarpi and the Jesuit Sforza Pallavicino.`
- This new text, from the D-S1 fix, gives Sarpi to "the Catholic side" and calls him only "the friar". The listener cannot weigh him. Yet he is the brief's one witness against the History on whether Beza was stopped ("Sarpi says he was told to conclude", p.4; SARPI l.42837-42838).
- The entry, as D-S5 fixed it, says "Catholic but hostile to the papal court". The Regensburg and Trent briefs of this batch now both read "The Venetian friar Paolo Sarpi was hostile to the papal court" (R1_changes Part A, A-M6; Part B, "Sarpi label"). Pattern C1 and Who item 6: a partisan witness carries his side, with one label across councils.
- Held lines: SARPI l.677-678 "Father Paul the Venetian, of the Order of the Servi"; records `claims[110]`; his stance as the Trent records cite it (SARPI l.8820-8836, Trent `claims[13]`).
- Fix, brief (replace the second sentence; 20 words): `So do two historians of Trent, the Jesuit Sforza Pallavicino and Paolo Sarpi, a Venetian friar hostile to the papal court.` "Rival" goes: the two sides, now named, carry it, and the entry `record` keeps "Pallavicino wrote against him". The sentence costs 5 words. The cuts under "Length test" pay for them.
- Checked on a scratch copy: with the cuts, 400 words, FK 7.50, Flesch 65.65, longest sentence 25 words.

## Minor

**D2-M1. Minor (an identification without its witness, in new text).** Entry `calledBy`: `These were the meetings of 24 and 26 September.` Records `claims[67]`: `(the meetings of 24 and 26 September)`.
- The letter gives only "deux Communications qu'ils avoient faites à deux divers jours" (AYM l.25545-25546). The dates are Polanco's (entry `datesNote`, "Polanco dates the third to Wednesday 24 September and the last to Friday 26 September"). The editors' note on Beza's speeches gives the same days (HE1 l.27898-27899, "le 24 et le 26 septembre"). The identification is sound, but it is the profile's, not the letter's.
- Fix, entry `calledBy` (replace the sentence; 15 words): `Her two meetings "à deux divers jours" fit the sessions Polanco dates to 24 and 26 September.` (Use the entry's own quote marks, single quotes.)
- Fix, records `claims[67]`: `(the two meetings fit the sessions of 24 and 26 September, which Polanco dates)`.

**D2-M2. Minor (a word that the cited lines lack).** Entry `outcome[7]` and `claims[81]`: `secretly submitted to canonists at Trent in 1562`. WAT l.9099-9102 names the five men but does not call them canonists. Waterworth does so elsewhere: Simonetta for "his intimate acquaintance with canon law", with Castagna, Boncompagno, Paleotto and Castelli as his assistants (WAT l.7353-7358); "Castagna ... one of the most able canonists of his day" (l.10501-10502); "canonists, Boncompagno, Fachenetti, Paleotto, Lancellotto, to whom Castelli was [after]wards added" (l.9762). The word holds. Fix: records `claims[81]` witness `council-of-trent_canons-and-decrees_waterworth1848.txt l.9099-9102; for "canonists", l.7353-7358, 9762, 10501-10502`. Entry unchanged.

**D2-M3. Minor (a condition told as done).** Entry `traditions` (the-society-of-jesus): `It came in as a college, not a new order, and under another name.` The act received the Society "à la charge qu'ilz seroient tenuz prandre aultre tiltre que de société de Jésus ou de Jésuites" (LAI8 l.39603-39605), "on condition that they be bound to take another title". Whether they took one is not in the act. Fix (15 words): `It came in as a college, not a new order, on condition it take another name.`

**D2-M4. Minor (length: four small cuts, −5 words).** See "Length test".

## Length test

Brief before: 400 words, 2:30 at 160 wpm. I tested each sentence for whether a cut would lose a decision, a side or a source.

- P1, the scene. "About noon on 9 September 1561 ... at Poissy": the opening scene the pattern asks for (C8). One cut: "great" refectory (−1). It is the History's "grand refectoir" (HE1 l.27648), but as scene-setting it carries no decision, side or source. "The king sat with his mother, Queen Catherine": she is needed later. The count of cardinals and bishops: needed, because "That count" in P2 places it with its witness. "Bare-headed at a barrier ... Beza spoke for them": the refused party in the room; keep.
- P2, whose account. The 1580 title with no author, "long credited", and Reuss's view are the pattern's first duty here. One tightening: "thought Beza directed the work and" → "thought Beza directed it and" (−1). "It tells the Reformed side, and prints the prelates' own decisions": needed (D-S1). The Jesuits, and the two historians as D2-S1 places them (+5): needed.
- P3, the stake. "In July an assembly resolved that the ministers should have a safe-conduct and be heard." → "In July an assembly resolved to give the ministers a safe-conduct and a hearing." (−1; HE1 l.25997-25998 "auroient faufconduict pour l'y trouver, & y eftre ouis"). The aim sentence and its tag: keep. The edict at the close answers it.
- P4, Beza's sentence and the uproar. Each sentence carries a sourced act, with its witness tag ("the History says", "Sarpi says"); the "told to conclude" dispute needs both witnesses. Keep all.
- P5, the Catholic replies. Lorraine's "son, not lord": his own voice; keep. "On 26 September the Jesuit Diego Laínez spoke to the queen in Italian." → "On 26 September the Jesuit Diego Laínez spoke to the queen." (−2). The language is a Polanco detail (LAI6 l.3747) with no decision, side or source in it; the entry's `record` keeps it. His words to her: his side's own voice; keep.
- P6, the formula and the refusal. The queen's order, the rejection "as captious", and the conclusion's "one God, one king, one faith and one law": each is a decision in the prelates' own words; keep.
- P7, what came of it. Catherine's letter and Pallavicino's verdict: the crown's and the Catholic historian's voices, which the README names; keep.
- P8, the edict. Its terms and its "one fold" are the edict's own words, and "still" keeps the close from saying the hope ended. Keep.

No sentence repeats another. There is no summing-up line, no double attribution, and no clause that restates the README's reason. The brief earns its length. The four cuts above are a few words each, so they are Minor. They are worth taking to pay for D2-S1 without passing the ceiling.

**Counts.**
- Before: 400 words, 2:30 (2.50 min), FK 7.41, Flesch 66.29, longest sentence 25 words.
- Cuts alone (no D2-S1): 395 words, 2:28 (2.47 min), FK 7.38, Flesch 66.14, longest 25 words.
- Cuts plus D2-S1: 400 words, 2:30 (2.50 min), FK 7.50, Flesch 65.65, longest 25 words ("In January 1562 a royal edict ...", unchanged). The new Sarpi sentence is 21 words by the splitter's count. All checked with `grade_text` and `working/grade.py` on scratch copies.

**README line.** "Colloquy of Poissy (about 2:30)" stays true either way: 400 words is 2:30, and 395 is 2:28. The reason given (standing and Catholic witnesses placed; scene, sentence and uproar, replies, refusal, and what came of it) matches what the brief keeps after the cuts. No change is needed. One note for the coordinator, outside this council: the batch README's "None was written to the ceiling" (l.19) sits beside four briefs that are each exactly 400 words. I leave the wording to the coordinator, since it covers all four.

## Verified

- Every changed brief sentence, against its source line in context: p.1 (Navarre dropped; HE1 l.27647-27651 has Orléans and the King and Queen of Navarre besides Catherine, so dropping them takes nothing false from the brief); p.2 (D-S1); p.3 "to see if they could be reunited with the Roman Church" (HE1 l.25998-25999 "afin d'advifer fil y auroit moyen de les reunir à l'Eglife Romaine", which is faithful); p.4 (D-B1, D-M1); p.6 "reached a formula" without "then" (HE1 l.33193-33203, 33383-33395) and "barred from" (D-M2).
- Every changed or added entry and records quote, verbatim: "quelque Colloque gracieux" (AYM l.25542-25543); "the articles proposed at the Conference of Poissy" (WAT l.9099-9100); "as witnesseth Colloquium Poissiaconum in Gallia, anno 1561" (MELV l.33964-33965); the "Tuesday" title (HE1 l.27895-27898); the Jesuit act (LAI8 l.39602-39605). Translations: "partakers ... in a spiritual way and through faith, as truly as they see the sacraments" (claims[109]) is faithful to HE1 l.28526-28529. "Sets out to refute a false history published under the name Pietro Soave Polano" (claims[111]) is faithful to PAL2 l.1, "rifiutasi ... un'istoria falsa divolgata ... sotto nome di Pietro Soave Polano".
- Split or joined sentences: `calledBy` (D-S2) keeps "Catherine wrote" in the first half, and the second half is D2-M1. `decided[1]` (D-S3) keeps "the History says" on the resolution and gives the date to Baum and Cunitz. `datesNote` (D-S4) is its own sentence and keeps the History on "about noon". The Jesuit note (D-M5) puts the act's tag in the first sentence; the second carries the act's terms, see D2-M3. Each claim sits with its witness.
- The audio matches the brief line for line in the diff, with the two tags only.
- No entry sentence over 25 words in the changed strings (counted: the longest is `decided[1]`'s first sentence, 22 words; `outcome[7]`'s first sentence, 24 words).
- An observation, not a finding, because the text is unchanged and the point is not blocking. Brief p.7, "Catherine wrote that the meetings bred disputes upon disputes", widens her letter a little. The letter says this of the two meetings after Lorraine's reply (AYM l.25545-25548), and the five-and-five came after them. A word-neutral wording, if the fixer wants it: "Catherine wrote that two meetings bred disputes upon disputes, far more than union." It also agrees with the new `calledBy`.

## Searches run

No new or changed absence in the brief, entry or records. The changed text asserts no "not held" or "no source". Searches run for the points above:
- AYM l.25495-25640, the whole Catherine letter (heading, body, date line); `grep -i "octob|1561|jour"` in that range for the date.
- HE1 l.28480-28540 and l.28695-28745, the whole speech passage and the whole narrative of the uproar; `grep` for "abjent|ejloigné du pain|fommes faits participans|niere Jpirituelle|combien qu'il nous fuft|Blafphemavit" for line numbers (hits l.28513, 28516, 28527-28529, 28711, 28718; l.10964 and 28878 are other passages).
- HE1 l.28994-29030 (the resolution and the editors' date), l.27836-27842 and l.27890-27900 (deputies; the edition title), l.30624-30632, l.33700-33720, l.37064-37074 (the edict's "en une mefme bergerie"), l.27645-27652 ("grand refectoir").
- WAT: `grep -n -i "canonist"` (hits l.1539, 2877, 3388, 3874, 4001, 9731, 9742, 10503, 10723) and `grep -n -i "Boncompag|Paleott|Castelli|Castagna"` (l.7357-7358, 9101-9102, 9762, 9881-9882, 10502 and others); read l.7350-7360, 9094-9112, 9755-9763, 10501-10504.
- SARPI l.673-680 and l.42785-42789; PAL2 l.1 (title); LAI8 l.39598-39606; MELV l.33938-33970 and `grep "1607|Falkland"` in l.33700-34100.
- Open-Gaps.md: `grep -n -i "poissy|palatin"`.
- The other era 7 briefs: `grep -o` for Sarpi sentences (label comparison for D2-S1).

## Counts

Round 1 findings: 17 (D-B1, D-S1 to D-S5, D-M1 to D-M11). All 17 are closed; 4 are closed with a new point (D-S1, D-S2, D-M5, D-M10). D-M11's Open-Gaps entry is still to be made by the coordinator.
New: Blocking 0. Substantial 1 (D2-S1). Minor 4 (D2-M1 to D2-M4).
Brief: 400 words (2:30) before; 395 (2:28) with the cuts alone; 400 (2:30) with the cuts and D2-S1.
