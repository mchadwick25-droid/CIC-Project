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
