# Round 2 recheck: era 5 council profiles (2026-11-15)

A targeted recheck by three fresh Opus agents, one per council, none of whom had seen the drafting or the round 1 fixing, at full effort: every round 1 finding, and everything changed since round 1 (`git diff e96e6250 HEAD`). Part A: Clermont. Part B: Lateran IV. Part C: Lyon.

---

## Round 2 targeted recheck, Part A: Council of Clermont (1095)

**Council.** `council-of-clermont-1095`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era5/council-of-clermont-1095.brief.txt`, `audio/council-of-clermont-1095.audio.txt`, `council-of-clermont-1095.entry.json`, `records.json` key `council-of-clermont-1095`. These are the changes from `e96e6250` to HEAD (branch `claude/cft-councils-era5`).
**Brief.** 400 words (2:30 at 160 wpm, at the cap). `grade_text`: FK 7.02, Flesch 69.26. Longest sentence 25 words (the Anna sentence). No sentence is over 25 words.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph. Checked by script.
**JSON.** The entry and `records.json` parse. The entry's key order is unchanged and matches the pattern form used by era 4 Whitby and Constantinople 861-880 (`informalName` is optional).
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 fixing. No repo file was edited. No model, network or paid calls were made.

Abbreviations as in round 1 (PL166, WT, MIRBT, CART, PL152, PL159, LP1, LP2, ANNA, MATT, M21, AASS).

## Verdict: REVISE (one substantial finding, six minor)

Every round 1 finding has been dealt with. Fifteen are resolved correctly, and A-M16 was not applied for a sound reason. One fix brought in a new attribution the held text does not carry. The brief's new canon on investiture ("Another forbade kings and princes to invest anyone with a church office") is the one Beauvais item whose heading names no pope. A held source records a second council at Clermont, held by Hugh of Die about 1077 amid the councils against lay investiture. So the brief tells an uncertain attribution as settled (A2-S1). The minor findings are a reliability point on Lambert's dates, a false "only", and a "we" left without its quotation marks.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| A-B1 | RESOLVED | Brief p.3 now reads "Lambert, a canon of Saint-Omer, counts 310 bishops." `attended[1]`, `datesNote`, `uncertain[2-4]`, the Lambert `record` entry and the LP1 `writtenLater` source are all in place. Records claims 24 and 25 are added, the two `absent_details` are rewritten, and Lambert is on the 1096 side of "The year". The text was checked at LP1 l.47588-47590, 47681-47682 and 47693-47697. See A2-M1 and A2-M2 for two refinements. |
| A-B2 | RESOLVED, with a new error | Brief p.2 now says canons "survive in later copies, among them the record of a council at Beauvais in 1114" (M21 l.11886-11887, 11936-11944). `decided[0]`, `decided[3]`, `uncertain[0]`, the record entry, `fromTheCouncil` and records claims 33-37 are added. But the one canon the brief picked is the one not headed as Urban's (A2-S1). |
| A-S1 | RESOLVED | Brief p.7: "Anna Komnene, daughter of the emperor Alexios, wrote that as the armies came east, ..." (ANNA l.1068-1069, 15626-15628). `outcome[5]` matches. |
| A-S2 | RESOLVED | The quotation marks are gone from "like rivers flowing together from everywhere" in `outcome[5]`. The Greek is at ANNA l.15675-15676. |
| A-S3 | RESOLVED, wording slip | `uncertain[8]` and the contested claim now say the editor accepts the Clermont prescription (PL152 l.26632-26636). But "He doubts only the Carthusian vision" is a false "only" (A2-M3). |
| A-S4 | RESOLVED | `uncertain[4]` and `record` say "1095 in one note and 1096 in another". AASS l.26403-26405 is on the 1095 side; l.148148-148149 gives "mxcvi". |
| A-M1 | RESOLVED | Brief p.2: "Baldric gives the pope's words, or words like them" (PL166 l.77696). Records claim 5 is added. |
| A-M2 | RESOLVED | All three long sentences are split. "Raised" is gone (PL166 l.77477-77478, "residens in pulpito"). The call to fight is supported by PL166 l.77629-77631 and 77639-77640 ("pro vestra Jerusalem decertetis"). |
| A-M3 | RESOLVED | Jerusalem is now named in p.1, sentence 2. |
| A-M4 | RESOLVED | "Some of the council's rulings, its canons" (p.2). |
| A-M5 | RESOLVED | The brief no longer mentions pilgrims. `decided[2]` reads "above all for pilgrims" (MIRBT l.11233, "ac primum"). |
| A-M6 | RESOLVED | Brief: "her father feared what she called their greed and broken promises". `outcome[5]` calls these "her own charges against the Franks" (ANNA l.15631-15632). |
| A-M7 | RESOLVED | Baluze is named in `outcome[7]`, the record, the source title and the records claim (M21 l.27334, 27397). |
| A-M8 | RESOLVED | Albert's note now follows Fabricius (PL166 l.27615-27620). |
| A-M9 | RESOLVED | `record[0]`: "Mirbt cites Mansi's volume 20, columns 816 and 902 ... and marks canon 9 as from the Codex of Cencius" (MIRBT l.11222, 11228). |
| A-M10 | RESOLVED | "or the case was settled before the pope" (CART l.13313-13315). |
| A-M11 | RESOLVED | `outcome[3]` and the Robert people line no longer place him in Flanders, and they add "son of Robert the Frisian" (PL166 l.65370). |
| A-M12 | RESOLVED | `calledBy` (WT l.6114-6115 against l.6140-6142). |
| A-M13 | RESOLVED | `traditions[2].note` now gives Bernard of Valence (MATT l.15578-15581). |
| A-M14 | RESOLVED, new slip | The Latin is dropped from `decided[1]` and `calledBy`. But `calledBy` now reads "the council which we held" with no quotation marks (A2-M4). |
| A-M15 | RESOLVED | `{"country": "France", "countryId": "Q142", "place": "Clermont"}` |
| A-M16 | NOT APPLIED, SOUND | Decision-Log l.2719 and l.3292: "writers who only report a council are in its record and sources". Anna, William and Ibn al-Athir only report the council. |

## New findings

### Substantial

**A2-S1. Substantial (an uncertain attribution told as settled; a fix that brought in a new error).** Locations: brief p.5, sentence 3; entry `decided[3]`, first clause; records claim 34 (no sides recorded).
- The brief, `council-of-clermont-1095.brief.txt` p.5, reads: "Another forbade kings and princes to invest anyone with a church office."
- The entry, `decided[3]`, reads: "From the Beauvais record: kings and princes were forbidden to grant investiture of church offices; ..."
- What the source shows. In the Beauvais list, the other Clermont items name Urban:
  - M21 l.12064: "Ex concilio Claromontano ab Urbano II. celebyato. cap. 11"
  - l.12071: "Urbanus papa II. in concilio Claromontano ... cap. 12"
  - l.12080: "Urbanus II. in eodem concilio, cap. 14"
- The investiture item does not. It is headed only M21 l.12045: "Ex Concilio Clavomontano". Its text is at l.12047-12049: "Interdictum est, ne reges, vel aliqui principes, aliquam investituram de honoribus ecclesiasticis faciant". It sits in the left column between an item of Gregory VII (l.12040) and one from the council of Poitiers held by the cardinals John and Benedict (l.12051-12052).
- A held source records an earlier council at Clermont, held amid the councils against lay investiture. PL152 l.4329-4333: "Inter diversa, quae adversus Simoniacos, acceptasque a laicis investituras ... celebrata fuere concilia, commemorandum hic venit, quod Hugo Diensis, sedis apostolicae in Galliis legatus, Claromonte celebravit". The editor dates it at l.4350-4351: "concilium, quod Hugo Diensis Claromonte celebravit, vel initio ipsiusmet anni 1077 vel sub finem" (that is, early 1077 or the end of 1076).
- No held line ties the ban on kings and princes to Urban's council. I searched all of `cic/texts/` for Clermont forms within 400 characters of "investitur" together with Urban, 1095 or mxcv. The only hit is Baluze's note on a different canon (M21 l.27445-27450).
- So the attribution to 1095 is an inference from the items around it. The brief tells it as fact, and it is the only canon from the Beauvais list that the brief uses.
- Fix, brief p.5. Replace "Another forbade kings and princes to invest anyone with a church office." (12 words) with "Another forbade any cleric to hold paid church posts in two cities." (12 words). Source: M21 l.12080-12082, "Urbanus II. in eodem concilio, cap. 14. Nulli clerico liceat deinceps in duabus civitatibus duas praebendas obtinere". A prebend is a canon's paid post, and "paid church posts" is the plain telling. The word count stays at 400. The full brief with A2-S1 and A2-M2 applied is in the scratch copy below.
- Fix, entry `decided[3]`. Replace the whole item with: "From the Beauvais record, under headings that name Urban II at Clermont: no layman was to seize another's inheritance, and no priest was to admit him to penance until he made it good. Sons of concubines and of clergy were not to be ordained or promoted to church offices unless they became monks or regular clergy. No cleric was to hold prebends in two cities." The rewrite also splits a 62-word sentence, and it restores "vel ad alios honores ecclesiasticos" (l.12076), which the old text dropped.
- Fix, entry `uncertain`. Insert after item [0]: "The Beauvais record also gives a ban on kings and princes granting investiture of church offices. Its heading names the council of Clermont but no pope. The editor of Bruno's Acta tells of another council at Clermont, held by the legate Hugh of Die about 1077, so the heading alone does not settle which council made the ban."
- Fix, records. Change claim 34 to: "Headed in the Beauvais excerpts 'Ex Concilio Clavomontano' (OCR for Claromontano), with no pope named: kings and princes are forbidden to grant any investiture of church offices". Add a contested claim: `{"claim": "Which council of Clermont made the ban on lay investiture recited at Beauvais", "sides": "Urban II's council of 1095: inferred from the items around it that name Urban at Clermont (M21 l.12064-12083). The heading names no pope (M21 l.12045). Hugh of Die held a council at Clermont about 1077, amid the councils against lay investiture (PL152 l.4329-4351).", "formation_confidence": "Inferential-Thin"}`.
- Other route. If Mark prefers to keep investiture in the brief, it has to carry the hedge, for example "A ban on kings and princes investing anyone with a church office is also headed 'Clermont', though no pope is named." That costs about 8 more words, which then have to be cut elsewhere. I recommend the cap. 14 replacement.

### Minor

**A2-M1. Minor (the weight of a new witness on the year).** Locations: entry `uncertain[4]`; records contested claim "The year"; Lambert's `record` note.
- What the source shows. The same notice that gives 1096 for the council also has Urban die in 1096. LP1 l.47699: "Et anno Domini mxcvi obiit." Duchesne's own heading for Urban is LP2 l.71346: "URBANUS II (1088-1099)".
- Why it matters. The year dispute now counts Lambert as a contemporary witness for 1096, without the sign that his dates in this notice are unreliable.
- Fix, `uncertain[4]`. Replace "Lambert of Saint-Omer, writing about 1120 by Duchesne's dating, gives 1096." with "Lambert of Saint-Omer, writing about 1120 by Duchesne's dating, gives 1096, though the same notice also has Urban die in 1096; Duchesne dates his death to 1099."
- Fix, records "The year", 1096 side. After "(LP1 l.47694)" add "; the same notice puts Urban's death in 1096 (LP1 l.47699), against 1099 in Duchesne (LP2 l.71346)".

**A2-M2. Minor (a later writer heard as a witness; "counts").**
- Location: brief p.3, "Lambert, a canon of Saint-Omer, counts 310 bishops."
- The problem. The sentence comes straight after Baldric, who was there. It gives no time, so a listener hears a second eyewitness. "Counts" also suggests Lambert counted them himself.
- What the source shows. Lambert compiled his book "vers l'an 1120" (LP1 l.47588-47590). The notice gives the number "cccx episcoporum" (l.47695).
- Fix: "Lambert, a canon of Saint-Omer writing about 1120, gives 310 bishops." This adds 3 words. Three 1-word cuts keep the brief at 400:
  - "Then Adhémar" becomes "Adhémar".
  - "the record of a council at Beauvais in 1114" becomes "the record of a Beauvais council in 1114".
  - "He had to go for devotion alone, and not to gain honor or money." becomes "He had to go for devotion alone, not to gain honor or money."
- Scratch copy with A2-S1 and A2-M2 applied: `/tmp/claude-0/-home-user-CIC-Project/ae522d88-ff95-54e2-81c3-aaef67a4f314/scratchpad/R2A/clermont.r2fixed.txt`. It is 400 words, FK 7.08, Flesch 68.77, with a longest sentence of 25 words. The audio script needs the same edits.
- Entry `attended[1]` ("counts 310 bishops"): change it to "gives 310 bishops".

**A2-M3. Minor (a false "only"; a "says so" with no clear subject).**
- Location: entry `uncertain[8]`, which reads: "... which the editor of Bruno's Acta cites and accepts. He doubts only the Carthusian vision told beside it. No witness of the time among ours says so."
- What the source shows. The editor also rejects Petreius's claim that the Carthusian practice came before Clermont: "verum quod hic asseverat, nullo plane argumento probat" (PL152 l.26653). His doubt of the vision is itself hedged: he will not deny it outright ("indubitanter negare idcirco non ausim", l.26591-26592).
- The second problem. "Says so" now follows the sentence about the vision, so it reads as if no witness tells of the vision.
- Fix, for the second and later sentences: "That Clermont prescribed the Hours of the Virgin for clergy rests on Ruinart, who reports it as hearsay, and on Labbe's printed councils, which the editor of Bruno's Acta cites and accepts. No witness of the time among ours says so. The editor questions the Carthusian vision told beside it, and rejects the claim that the Carthusians took up the Hours before Clermont."

**A2-M4. Minor (the narrator says "we").**
- Location: entry `calledBy`, which reads: "His own letter to Grenoble speaks of the council which we held at Clermont, city of Auvergne."
- The problem. With the Latin gone (A-M14), "we" now reads as the narrator's word.
- What the source shows. CART l.13306-13307: "Concilii, quod apud Clarummontem civitatem Arverniae [OCR Arverniz] celebravimus".
- Fix: "His own letter to Grenoble speaks of the council he held at Clermont, city of Auvergne."

**A2-M5. Minor (a false "only" on where the canons reach us).**
- Locations: entry `uncertain[0]`, which reads: "canons reach us only in later copies, in Mirbt's sourcebook and the Beauvais record of 1114". The records `absent_details[0]` says the same: "Canons reach us in Mirbt's extracts ... and in the Beauvais record of 1114".
- What the source shows. Baluze gives a further Clermont ruling, that monks were not to place priests in their parish churches without the bishop's consent. M21 l.27445-27448: "constitutio Urbani II. qui in concilio Claromontano statuerat ne monachi in parochialibus ecclesiis, quas tenent, absque episcoporum consensu, presbyteros collocent". A Mansi note at l.45240 cites "Urbanus II. in concilio Claromontano ... cap. 5" on a bishop.
- Fix, `uncertain[0]`, first clause: "The acts are not among our sources; canons reach us only in later copies, chiefly Mirbt's sourcebook and the Beauvais record of 1114, and a few more are described in editors' notes printed by Mansi."
- Fix, `absent_details[0]` note: add "; Baluze describes one more (M21 l.27445-27448)".

**A2-M6. Minor (form).**
- Location: the `datesNote` ends "No source among ours gives the day of Urban's speech" with no final period.
- This was already so before round 1, but round 1 rewrote the field. Add the period.

### Note for the coordinator (no finding)

The brief's FK is 7.02. The pattern (Council_Profile_Pattern.md l.8) and CLAUDE.md treat grade 8 as a floor worth staying above. The two other era 5 briefs score 8.13 and 8.02. Round 1 split three long sentences, and that pushed the score down. Nothing in the text is wrong or flattened, so I raise no finding. I mention it only so the reading is a decision, not an accident.

## Verified

- LP1 l.47691: the notice is printed "d'après le Parisinus 8865". l.47990 lists that manuscript as a 13th-century manuscript of Lambert's compilation. l.47681-47682 says the notices from Urban II to Calixtus II are "de main contemporaine".
- LP1 l.47693-47697: "mxcvi, indictione vi, xiiii kl. decembris ... apud Clarum montem cccx episcoporum, présidente ipso papa Urbano". 14 Kal. Dec. is 18 November, which is correct.
- No other count is held. I grepped every file for Clermont forms within 120 characters of numbers and words for bishops. Only LP1 l.47695 hit on the council.
- M21 l.11886-11887: Beauvais, 1114, under the legate Cono. l.11936-11938 and 11944: the excerpts are decrees "partim edita, partim recitata et confirmata". Canon headings were read in place at l.12040-12083. Each of cap. 11, 12 and 14 names Urban at Clermont, and each English telling matches its Latin.
- MIRBT l.11220-11233: canon 2, and canon 9 with peasants and merchants, three years, the food shortage and "ac primum". The brief's truce sentence is right.
- PL166 l.77475-77478 ("residens in pulpito"), l.77627-77641 (the call to fight for "vestra Jerusalem"), l.77694-77700 ("His vel hujuscemodi aliis", "nobis videntibus"), l.65367-65380 (Robert, son of Robert the Frisian, wife and children) and l.27613-27621 (Fabricius on Albert).
- ANNA l.15624-15633: Alexios heard of the Frankish armies coming and feared them, knowing their greed and their breaking of agreements. l.15668-15676: the unarmed crowd, sand and stars, crosses on their shoulders, women and children who had left their lands, rivers flowing together.
- M21 l.27330-27336 and 27395-27415: Baluze, and the Spanish indulgence.
- AASS l.26400-26406 and 148146-148150: the two Bollandist years.
- PL152 l.26580-26660: Ruinart's "Ferunt", the editor's "imo reipsa, ut apparet ... fuerit injunctum" with Labbe tom. X col. 517, the hedged doubt of the vision, and the rejection of Petreius.
- WT l.6112-6119 and 6138-6143, the Latin and the Old French. CART l.13303-13316, the Grenoble letter with both ends of the ban.
- MATT l.15576-15585: Bernard of Valence and Daimbert.
- Decision-Log l.2719 and 3292: the Who click rule (A-M16).
- Brief writing: no "X and never Y", no empty contrast and no AI cadence in the changed sentences. Each sentence carries one fact.

## Searches run

- **Investiture tied to Urban or 1095.** A Python scan of all `cic/texts/` (whitespace-normalized, long s folded). It looked for Clermont forms within 400 characters of "investitur" together with "urban", "1095" or "mxcv". The only hit was Baluze's note on the monks' canon (M21 l.27445-27450), which is not about kings and princes. A grep for "investituram de honoribus" and reges/investitur pairs found only M21 l.12048.
- **Other councils at Clermont before 1114.** Grep of PL152, CART and M21 for Clarom/Arvern. I found Hugh of Die's Clermont of about 1077 (PL152 l.4329-4351; CART l.2135 is the same council's matter). M21 also prints a "CONCILIUM CLAROMONTANUM" at l.1454 (a later council on the Mauriac case, its year not checked here), with no investiture text.
- **Counts of bishops.** See Verified.
- **Clermont canons beyond Mirbt and Beauvais.** M21 l.27445-27452, 45236-45262; PL159 l.42298-42306; Denzinger l.12704-12720.
- **Urban's death year.** LP2 for 1099 and mxcix: l.71346 "URBANUS II (1088-1099)".

---

## R2 targeted recheck, part B: Fourth Lateran Council (1215)

- **Council:** `fourth-lateran-council-1215`
- **Files:** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era5/fourth-lateran-council-1215.brief.txt`, `audio/fourth-lateran-council-1215.audio.txt`, `fourth-lateran-council-1215.entry.json`, and the `fourth-lateran-council-1215` key of `records.json`. Branch `claude/cft-councils-era5`, diffed `e96e6250..HEAD` (`635a3463`); the working tree is clean for these files.
- **Brief:** 400 words, about 2:30 at 160 wpm, which is at the cap. `grade_text`: **FK 8.13, Flesch 62.84**. The longest sentence is 24 words. The brief equals the R1 proposed text word for word.
- **Audio:** equals the brief, with `[calmly] ` at the start and `[warmly] ` before the last paragraph. There is no other tag (diff checked).
- **JSON:** both files parse. The entry keeps the pattern's field set and order.

**Verdict: NOT APPROVED TO PROCEED. 1 blocking, 0 substantial, 5 minor.**

Twenty-two of the 25 round 1 findings are resolved, and three were not applied for sound reasons. There is one partial miss: B-M6 is fixed in `issue` and `record`, but not in the two `traditions` notes. One new blocker is in records only. The rewritten absence on Cathar and Waldensian voices still says no Waldensian voice on the council is held. Jean Léger, the Vaudois moderator, speaks of it in 1669. The fix is one note.

---

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| B-B1 | RESOLVED | `attended[5]`, `uncertain[4]`, Francis's `people` part, the Glassberger note, the new Frachet `record` and `writtenLater` rows, and `contested_claims` ("at Rome during the council") all carry Frachet. Checked against Reichert l.1743, 1750-1770 and variant C l.1776-1777 ("circa concilium Lateranense anno domini 1215"), and against Conway l.996-1017 and l.1044-1050 ("during the sitting of the Lateran Council"; "embraced him with a kiss"). "About 1260" holds: Conway l.205-214, "the book was completed in 1260". |
| B-B2 | RESOLVED | `claims[34]`, the `record` witness and the `sources` row now name the Psalterium. Checked: Buonaiuti l.3009 "P=Psalterium decem chordarum", l.17812-17817, and "(P., fol. 229b-c)" at l.17856. |
| B-B3 | RESOLVED | The source row is split. `outcome[0]` and `claims[41]` name Bartholomew. l.94619-94624 reads "VITA ALTERA, Quam F. Bartholomaeus Tridentinus ... ante medium seculi XIII", and l.94739 reads "Honorius itaque Papa Ordinem confirmavit". |
| B-B4 | RESOLVED | The brief now reads "Most canons we hold come in extracts". The Bollandists' note, `uncertain[0]` and `absent_details[0]` now cover all the held quotations. Checked: Glassberger's editors' note 5 at l.7318-7323, and Cajetan in the Leonine Summa at l.30506-30512 and 33675-33677. The file header names Cajetan's commentary. See B2-M2 for the missing source row. |
| B-B5 | RESOLVED | Vitry's note now reads "later bishop of Acre; no source among ours puts him at the council". Letter I has "Acconensis ecclesie minister humilis" (Röhricht l.5860-5861). My grep found no Vitry name on a line with Lateran or concil in the 30 files that name him. |
| B-B6 | RESOLVED (Cathar part) | The Interrogatio note matches Döllinger l.128-140. The volume's title is "Dokumente vornehmlich zur Geschichte der Valdesier und Katharer". The Nobla Leiczon is held in two files (de Stefano 1909, Montet 1888), and neither mentions Lateran. The Waldensian half of the absence is still false: see B2-B1. |
| B-S1 | RESOLVED | The brief reads "at least at Easter, unless that priest advised a pause". Mirbt l.12401-12403 reads "ad minus in Pascha ... nisi forte de consilio proprii sacerdotis ... ad tempus". |
| B-S2 | RESOLVED | `decided[2]` and `claims[24]` match Mirbt l.12366-12369: "bis aut saltem semel ... in qua fama fuerit haereticos habitare ... tres vel plures boni testimonii viros". |
| B-S3 | RESOLVED | `uncertain[5]` uses the review's text. The canon 13 contest is gone, and `claims[58]` cites both Salimbene places. |
| B-S4 | RESOLVED | Joachim's `record` row and both Joachim claims are "later narrative". `claims[37]`: Ehrle-Denifle l.3349-3351 reads "(gest. 1202)". |
| B-S5 | RESOLVED | Hethum's stake is now paragraph 2. The record and who came follow it. |
| B-S6 | NOT APPLIED-SOUND | These are census items, carried in R1_changes for the coordinator. Open-Gaps.md has no era 5 councils entry yet (the last council entry is 266, era 4). The items must go into that entry before the era 5 profiles proceed. |
| B-M1 | RESOLVED | No sentence in the brief runs past 24 words. The doubled "among our sources" is gone. |
| B-M2 | RESOLVED | The brief has "Dominic, a Spanish preacher" (Mansi notice l.1048-1049, "Dominicus, Hispanus") and "the abbot Joachim". The `people` row was renamed as the review asked, but the name it gave is not sourced: see B2-M3. |
| B-M3 | RESOLVED | The brief reads "had ordered his writings judged by Rome. He asked this in a letter he signed himself". Denzinger l.14043-14046 reads "omnia scripta sua nobis assignari mandaverit ... dictans epistolam, quam propria manu subscripsit". |
| B-M4 | RESOLVED | The brief reads "drive from their lands". Mirbt l.12314 reads "de terris suae iurisdictioni subiectis". |
| B-M5 | RESOLVED | Röhricht's headings: "I. Octob. 1216" (l.5856) and "II. Sub finem Martii 1217" (l.6116; the changes file is right that it is not l.6112). Denifle's "im J. 1255" (l.5149-5151). `outcome[1]` now names its witnesses. |
| B-M6 | NOT RESOLVED (partial) | `issue[4]`, Denzinger's `record` note and `claims[7]` and `claims[25]` are fixed. The `traditions` notes for `cathars-albigensians` (entry l.207) and `the-waldensians` (entry l.213) still say "Denzinger's heading". See B2-M1. |
| B-M7 | RESOLVED | The Pedalion is "later narrative" in `record` and in `claims[29]` and `claims[30]`. |
| B-M8 | RESOLVED | The `teaser` is three sentences. `knownFor` is 25 words. |
| B-M9 | RESOLVED | Rows were added for the Assisi catalogue (Ehrle l.26363-26365: "der Catalog des Richard von Poitiers, Mönchs in Cluny"), Pulkava, the Anagni protocol, Covel and Alishan. Covel's "titular" fairly renders his "two Latin Nominal Patriarchs" (l.4916). Alishan is a Mekhitarist per the file header. The Denifle article title matches the Ehrle-Denifle header content note. |
| B-M10 | NOT APPLIED-SOUND | The close is optional, and the review marked it as Mark's choice. |
| B-M11 | RESOLVED | `issue[2]` and `claims[31]` now carry the full clause. Denzinger l.13947-13949 reads "et illa non est generans, neque genita, neque procedens". |
| B-M12 | RESOLVED | `attended[4]` now uses the review's wording. |
| B-M13 | RESOLVED (records) | `claims[0]` and `claims[1]` are split (l.93023-93026; l.93039-93050). The brief is unchanged, as the review allowed. See B2-M4 on the wording of `claims[1]`. |

---

## Blocking

**B2-B1. False absence: a Waldensian voice on the council is held.**
- **Where:** `records.json`, `fourth-lateran-council-1215` `absent_details[10]`:
  - detail: "A Cathar or Waldensian voice on the council"
  - note: "Neither is held. ... and the Waldensian poem the Nobla Leiczon. Neither speaks of the council."
- **Evidence:** Jean Léger, "pasteur et modérateur des Églises des Vallées" (header Creator line), wrote the *Histoire générale des Églises Évangéliques des Vallées de Piémont ou Vaudoises* (1669). He speaks of this council in his own voice:
  - `leger_histoire-generale-eglises-vaudoises-livre1-fra_1669.txt` l.17714-17715: "cette  Tranfubftantiation  n'a  pû  dire  établie , ni  pafTer en  article  de  Foy , que  dans  le  XIII.  fiecle , fous  Innocent  III.  au  Concile  de  Lateran" (OCR verbatim; "dire" is OCR for "estre").
  - Same file, l.20345-20347: "Innocent  111.  en  détermina  li  forme  au™"*/"- Concde  de  Lateran.Sc  qui  ordonna  quon  crût  que  le  Pain  clloit  tranfubllantié  au Corps  de  Chnft" (OCR verbatim, damaged).
  - Livre 2, in a quoted passage (l.27474-27476): Innocent "les  fit  con- damner  au  Concile  de  Latran  tenu  l'an  izif." (OCR verbatim; "izif" is 1215), with Dominic as "boute-feu".
  - The round 1 search ("Lateran") missed these because the French spelling is "Latran", and this file's OCR gives "Lateran" only in livre 1.
- **What is wrong:** the absence as written has no time limit, so it is false. It meant the time of the council. Nothing held from the thirteenth century is a Cathar or Waldensian voice on the council. My greps for Lateran, Latran, 1215 and Innocent III over the Waldensian and Cathar files found only later historians, editors' notes and the 1179 council.
- **Fix** (records only, so the 25-word cap does not bind; sentences are kept short anyway):
  - detail: "A Cathar or Waldensian voice of the time on the council"
  - note: "Neither is held. The Library holds the Interrogatio Iohannis, a dualist apocryphon that Döllinger prints among his documents on the Cathars and notes in a second text from the Carcassonne inquisition records (Döllinger II), and the Waldensian poem the Nobla Leiczon. Neither speaks of the council. A later Waldensian voice is held. Jean Léger, pastor and moderator of the Vaudois churches, wrote in 1669 that transubstantiation became an article of faith under Innocent III at the Lateran council (leger_histoire-generale-eglises-vaudoises-livre1-fra_1669.txt l.17714-17715, 20345-20347)."

---

## Minor

**B2-M1. B-M6 not carried to the `traditions` notes.**
- **Where:** `fourth-lateran-council-1215.entry.json`:
  - l.207 (`cathars-albigensians`): "...the canons name no group, and the name Albigenses is Denzinger's heading."
  - l.213 (`the-waldensians`): "...the canon names no group, and the name Waldenses is Denzinger's heading."
- **Evidence:** Denzinger died in 1883. The held edition is Bannwart's of 1911 (Denzinger header l.1-2). `issue[4]` was already corrected on this ground.
- **Fix:**
  - l.207: "Canon 3 condemned all heretics, and canon 1 affirmed that married people too can be saved; the canons name no group, and the name Albigenses is a heading in Denzinger's Enchiridion, in Bannwart's edition of 1911."
  - l.213: "Canon 3 excommunicated those who preached without authority from the pope or bishop; the canon names no group, and the name Waldenses is a heading in Denzinger's Enchiridion, in Bannwart's edition of 1911."
  - Optional: in `records.json` `contested_claims` (general or local), "Denzinger's heading" becomes "the heading in Denzinger's Enchiridion (Bannwart, 1911)".

**B2-M2. Cajetan is used but is in neither `sources` nor `record`. Glassberger's editors' note is used but has no `record` row.**
- **Where:**
  - `uncertain[0]` names "Cajetan's commentary in the Leonine Summa". No `sources` row points to `thomas-aquinas_opera-omnia-t12-summa-theologiae-lat_leonine1906.txt` (grep: 0 hits in the entry).
  - Glassberger's editors' quotation of canon 13 has a `fromTheCouncil` source row. In `record` it appears only inside the Bollandists' note.
- **Fix:**
  - Add a `sources.fromTheCouncil` row: `{"title": "Phrases of canon 1, quoted in Cajetan's commentary", "author": "Fourth Lateran Council, in Cajetan's commentary in the Leonine Summa theologiae, tome 12", "language": "Latin", "file": "cic/texts/thomas-aquinas_opera-omnia-t12-summa-theologiae-lat_leonine1906.txt"}`.
  - Optionally, add `record` rows. First: `{"witness": "Canon 13, as Salimbene quotes it, in the notes of Glassberger's editors (Analecta Franciscana II, 1887)", "kind": "acts", "note": "The council's own words, through a Franciscan chronicler and modern editors."}`. Second: `{"witness": "Phrases of canon 1 in Cajetan's commentary (Leonine Summa, 1906)", "kind": "acts", "note": "The council's own words, quoted by a Dominican commentator."}`.

**B2-M3. "Almaric of Paris" is a name no source gives.**
- **Where:** `people`, `"name": "Almaric of Paris"`. This came from the R1 fix B-M2.
- **Evidence:** the Mansi notice ties him to Paris only by the burning: "cum sectariis pluribus Parisiis post obitum exhumatus, combustus est" (`innocent-iii...pl214...txt` l.1056-1058). A built name like "of X" reads as his origin or see. The only held line that gives him a place-name says "Almarich von Bena" (de Stefano's note citing Hahn, `waldensians_nobla-leicon-pro_destefano1909.txt` l.4742), and that line is a book title.
- **Fix:** `"name": "Almaric"`. Keep the new part: "Dead; his teaching condemned in canon 2; exhumed and burned at Paris, by the notice in Mansi".

**B2-M4. Process commentary inside a records claim.**
- **Where:** `records.json` `claims[1]`: "...; Jordan tells this a paragraph after the bishops' setting out, so the brief's first sentence joins the two".
- **What is wrong:** the clause after the semicolon comments on the brief. It is not a claim the source makes. The review note behind it (B-M13) belongs in the review file, where it already is.
- **Fix:** "Dominic joined Fulk, bishop of Toulouse, so that they might go to the Lateran council together; Jordan tells this a paragraph after the two men of Toulouse gave themselves to Dominic".

**B2-M5. Changed entry sentences over about 25 words, and two missing closing periods.**
- **Where and fix.** Each replacement keeps every clause and stays at 25 words or fewer per sentence. "Röhricht dates..." keeps the C4 attribution.
  - `issue[2]`, sentence 2 (37 words). Replace with: "In it he called Lombard a heretic and a madman for what he said in his Sentences. Lombard had said that there is one supreme reality which is Father, Son and Holy Spirit, and which neither begets nor is begotten nor proceeds." (17 and 25 words)
  - `attended[4]`, sentence 2 (39 words). Replace with: "The Annals of the Four Masters, in O'Donovan's English, say Conar O'Heney, bishop of Killaloe, died on his way home from the council. In the same year they enter the death at Rome of Dionysius O'Lonargan, archbishop of Cashel. The Annals of Ulster, in O'Donovan's notes, say Eghdon Mac Gilluir, coarb of Patrick and primate of Ireland, died at Rome after the general council." (24, 19 and 25 words)
  - `attended[5]`, sentence 1 (38 words), and it has no closing period. Replace the whole item with: "Whether Francis of Assisi was there: Gerard de Frachet, in a Dominican collection of about 1260, tells of Dominic meeting Francis in a church at Rome. Dominic was there to press the pope to confirm his order. One manuscript and Placid Conway's English put this during the Lateran council, and its editor Reichert dates it to 1215. The Observant Franciscan chronicler Nicolaus Glassberger says Francis met Dominic at the council. Neither says Francis sat in the sessions." (26, 12, 20, 13 and 7 words. The title *Lives of the Brethren* stays in `record` and `sources`.)
  - `decided[2]`, the visitation clause (34 words). Replace "Bishops were to go, ... on oath to name them; a negligent bishop was to be deposed." with: "Bishops were to go, twice or at least once a year, through any parish where heretics were said to live. There they were to put three or more men of good name on oath to name them. A negligent bishop was to be deposed." (20, 17 and 7 words)
  - `outcome[1]`, sentence 2 (32 words). Replace the last two sentences with: "Jacques de Vitry tells how he found the body there, stripped of its robes in the night and left almost naked in the church. The cardinals elected Honorius the next day. Röhricht dates Vitry's letter to October 1216." (24, 7 and 7 words)
  - `outcome[3]` (41 words). Replace with: "The censure of Joachim passed into Gregory IX's Decretals, as Heinrich Denifle notes. By Denifle's dating, the commission at Anagni sat in 1255. It judged that a passage of Joachim's Concordia seemed still to assert the heresy the Lateran council condemned." (13, 10 and 18 words. Denifle l.5149-5150 reads "was ... zu Anagni im J. 1255 geschehen ist".)
  - `outcome[6]` (44 words). Replace with: "Jacques de Vitry wrote that the patriarch of the Maronites, with his archbishops, bishops and people, had left all errors. They had submitted to the Catholic faith and the obedience of the Roman church. Röhricht dates the letter to the end of March 1217." (20, 15 and 11 words. Röhricht l.6802-6805 reads "relictis omnibus erroribus, catholice et obedientie sancte Romane ecclesie se subdidit".)
  - `record` (Bartholomew of Trent) note: add the closing period, to match the other notes: "Dominican, before the middle of the thirteenth century, by the Bollandists."

---

## Verified

Every new or changed sentence was read against `cic/texts/` in context.

- **Brief, changed sentences:**
  - "Dominic, a Spanish preacher" (Mansi notice l.1048-1050).
  - "Dominic's successor" (Jordan as second master general, R1 l.92240-92242).
  - Hethum's stake moved, text unchanged.
  - "Most canons we hold..." holds against the held quotations: Bollandists, Glassberger's editors, Cajetan.
  - Canon 21 (Mirbt l.12399-12403).
  - "from their lands ... the heretics the church named" (Mirbt l.12314-12316: "ab ecclesia denotatos").
  - "the abbot Joachim" (Denzinger l.13944).
  - The monastery and letter sentences (Denzinger l.14040-14046).
  - "stripped of its robes at night" (Röhricht l.5936-5938: "de nocte ... spoliaverunt").
- **Entry:**
  - `teaser` and `knownFor`.
  - `issue[2]` (Denzinger l.13943-13949) and `issue[4]`.
  - `attended[4]` (R1-verified lines; wording only changed).
  - `attended[5]` (Reichert l.1743-1777; Conway l.996-1017, 1044-1050). Conway l.1012-1015 names the chain of witnesses: a friar minor, then the brethren, then Jordan.
  - `decided[2]` (Mirbt l.12364-12384).
  - `outcome[0]`, `[1]`, `[3]` and `[6]` (Bartholomew l.94619-94624, 94737-94740; Glassberger l.2118-2120; Röhricht l.5856, 6116; Denifle l.5149-5151).
  - Every new `record` row:
    - Assisi catalogue (Ehrle l.26363-26365);
    - Pulkava, as R1 verified;
    - Anagni protocol, as R1 verified (l.7739-7740);
    - Covel (l.4909, 4914-4918);
    - Alishan (header Creator line, Mekhitarist);
    - Frachet, Bartholomew and Vitry.
  - `uncertain[0]`, `[4]` and `[5]` (Glassberger l.7318-7323; Leonine Summa l.30506-30512, 33675-33677, header naming Cajetan; Coulton as R1 verified).
  - New `sources` rows, against file names and headers: Reichert's own name at l.113 and l.1121; Conway's title page in the header.
  - People: Francis and Almaric (Almaric under B2-M3).
- **Records:** every new or changed claim:
  - `claims[0]`, `[1]`, `[5]`, `[7]`, `[24]`, `[25]`, `[29]`, `[30]`, `[31]`, `[34]`, `[36]`, `[37]`, `[39]`, `[41]`, `[44]`, `[45]`, `[49]`, `[50]`, `[56]`, `[58]`, `[64]`, `[68]` and `[69]`;
  - the new Francis `contested_claims` row;
  - `absent_details[0]` and `[8]`;
  - `absent_details[10]` (see B2-B1).
- **Confidence tags:** `claims[44]`, "Widely Accepted", follows the existing convention for the Bollandists' canon 13 quotation (`claims[43]`). `claims[68]`, "Inferential-Thin", fits Francis's presence, which rests on a later story.
- **Audio, grade, word count and JSON** as in the header.

## Searches run

- **Vitry at the council.** Listed the 30 files that name Vitry (vitriaco, de vitry, vitriacensis), then grepped them for his name within 120 characters of Lateran, Latran or concil: no hit.
- **Nobla Leiczon and the Interrogatio.** "Nobla Leiczon" and its variants give 9 hits; the two Waldensian editions have no Lateran or Latran line. Döllinger II has one Lateran line, l.19118, which is unrelated.
- **Waldensian and Cathar voices on Lateran IV.** In every Waldensian, Vaudois, Cathar or Albigensian file (Léger, Perrin, Gilles, Arnaud, Montet, Muston, Morland, Haupt, Gabotto, Döllinger, Zezschwitz, Gilly, Wattenbach), grepped "lat[eé]r[ao]n", "latran", "1215" and "Innocent III". The hits:
  - Léger livre 1 l.17715, 20346 and livre 2 l.27475 (B2-B1);
  - Montet 1885 l.2230 (a modern historian on "le quatrième concile de Latran");
  - Haupt (modern scholarship);
  - Perrin, Muston and Gilly: the 1179 council.
- **Almaric's place-name.** Grepped amalric, amaury, almarich, almaricus and amalricus followed by of, de or von and a place: one hit only, "Almarich'a von Bena" (de Stefano l.4742, a book title).
- **Aquinas file in the entry's sources.** Grep "thomas-aquinas" in the entry: 0.
- **Era 5 councils entry in Open-Gaps.md.** Grep "era 5" and "lateran": no era 5 councils entry; the last council entry is 266 (era 4).

---

## Round 2 targeted recheck, Part C: Second Council of Lyon (1274)

**Council.** `second-council-of-lyon-1274`. Branch `claude/cft-councils-era5`, HEAD 635a3463, diffed against e96e6250.

**Brief.** 392 words (about 2:27 at 160 wpm). FK 8.02, Flesch 64.06 (`engine.m1.gates.grade_text`). Longest sentences 26 words (paragraph 1, the welcome; the close, most of it the quotation). Audio equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, checked by script. Both JSON files parse. The entry keeps the pattern's form (fields in pattern order; `informalName` and `fromThoseThere` now absent, as the pattern allows: "A missing field is absent, never filled").

**Verdict.** NOT YET. No blocking finding. All round 1 findings are resolved, or not applied for a sound reason. Two substantial findings, both brought in by round 1 fix text on the mendicant decree. One minor finding.

---

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| C-B1 | RESOLVED | Brief p.2 now "The Greek side reaches us from later writers, from about 1300 on." `uncertain[0]`, `absent_details`, `record`, `sources`, `issue[3]` and the Byzantine tradition note name Nikephoros Kallistos. PG 147 l.21339 heading "NICEPHORI CALLISTI ENARRATIO DE EPISCOPIS BYZANT."; the list ends with John and Athanasios's return (l.21320-21328, Greek l.21391-21402); Andronikos is "εὐσεβεστάτου" (OCR l.21376-21377). Palamas not cited: SOUND. PG 150 l.52618-52700 is a codex index giving titles and incipits ("Initium: ... Fol. 04"), not the work's text. A fresh grep for Βέκκ-/Βέχχ- and Λουγδ- across `cic/texts/` finds no Greek text earlier than PG 147's list (see Searches). |
| C-B2 | RESOLVED | Records "Michael VIII's motive" now gives the Recueil editors' side, cites l.54168-54172, words the census point as asked, and is Contested. `uncertain[6]` replaced. Recueil l.54168-54170: "Les Grecs, espérant se concilier la faveur et l'appui des princes d'Occident". |
| C-S1 | RESOLVED, with new errors | Salimbene added to `decided[3]`, `record`, `sources.writtenLater`, `absent_details`, five claims and a contested claim. But the fix text misreads Salimbene and makes Lea say "only" (C2-S1, C2-S2). |
| C-S2 | RESOLVED | Tocco and the depositions are under `sources.writtenLater`; `fromThoseThere` is gone. |
| C-S3 | NOT APPLIED-SOUND, still open | R1_changes gives the full Open-Gaps text and assigns it to the coordinator. `Open-Gaps.md` has no Lyon II census entry yet (grep "lyon": only l.101, 1615, 2213, 2224, 3300, 3364-3370, none on this). It must land before the PR, or the gap goes quiet. |
| C-S4 | RESOLVED | Brief p.5 "Clemens Bannwart, Denzinger's editor, notes..." (header l.1-2: "editio undecima quam paravit Clemens Bannwart"; note l.14515-14517). Brief p.8 "The chronicle printed under Sphrantzes's name says...". |
| C-M1 | RESOLVED | Brief, `outcome[1]` and the records claim say "flogged, ill-treated and exiled". Sphrantzes l.1259-1260 "ἐμαστίγωσε xai ἐκάχωσε καὶ ἔξώρισε"; Latin l.1290 "flagellavit vel mutilavit vel eiecit". |
| C-M2 | RESOLVED | `attended[1]`: "Germanos, who had been patriarch some years before, between Arsenios and Joseph". Creyghton l.3062-3063 "Germanum non itanuper Patriarcham; qui medius inter Arsenium, & Josephum primum intercedens". |
| C-M3 | RESOLVED | `uncertain[8]` and the contested claim give Doukas his own side, "set beside Florence ... nothing said of its terms". Doukas l.14310-14315: oaths "σὺν ἀφορισμοῖς ἀλύτοις", Lyon beside Florence. "Corrupted" fits PG 159 l.56915 "Acta adulterarunt". |
| C-M4 | RESOLVED | Close: "In 1870 the First Vatican Council looked back to Lyon. With that council's approval, it said, ..." "Lyon" outside the quotation. Quotation unchanged and verbatim (Schaff, R1-verified). |
| C-M5 | RESOLVED | "Michael VIII, emperor at Constantinople"; "Patriarch Joseph of Constantinople". |
| C-M6 | RESOLVED | Kalekas and Thomas now form paragraph 4. |
| C-M7 | RESOLVED | `attended[5]` "was on the road in Lent ... when he fell ill at Maenza". Acta Sanctorum l.116097-116100: "convocabat Concilium, ad quod Concilium dictus Frater Thomas vocatus ibat: de mense & die certa dixit se non recordari: tamen dixit, quod fuit tempore Quadragesimali". Records claim reworded to match. |
| C-M8 | RESOLVED | `decided[1]` "that the Roman church makes the eucharist from unleavened bread" (Denzinger l.14611 "Sacramentum Eucharistiae ex azymo conficit eadem Romana Ecclesia"); new claim on purgatory (l.14584) and seven sacraments (l.14604). `outcome[7]` follows Bullarium V l.14402-14406 "sit in brevi ut creditur relinquendus, in dispositione sedis apostolicae ... remansurus". |
| C-M9 | RESOLVED | "per the dossier"/"not rechecked" gone; the Dominicans are "Affected" with the Glassberger charge (l.7291-7292 "praecipue Fratribus Minoribus et Praedicatoribus praedicationem crucis"); `informalName` removed. |

---

## New findings

### Substantial

**C2-S1. False "only" and a dropped condition on Lea: the confirmed orders were also struck.** (Brief rules: false "only", dropped condition; a fix that brings in a new error.)

- Where: entry `uncertain[4]` (new): "Clement XIV and Lea say it struck only unconfirmed orders, and Lea that the Carmelites and Augustinians were left on sufferance." Records `contested_claims`, "What the mendicant decree did", Lea's side: "...and let confirmed mendicant orders continue: Lea, 1888 (... l.1856-1862)."
- Evidence: `lea_history-of-the-inquisition-of-the-middle-ages-v3_1888.txt` l.1861-1865: "Such mendicant Orders as had been confirmed since the Council of Lateran were permitted to continue, but they were instructed to admit no new members, to acquire no new houses, and not to sell what they possessed without special license from the Holy See." By Lea, the confirmed orders were frozen too, so "struck only unconfirmed orders" is false for him. Clement XIV (`mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt` l.23010-23015) says Gregory renewed the ban on new orders and "perpetuo prohibuit" the post-Lateran mendicant orders "qui nullam confirmationem sedis apostolicae meruerunt". He says nothing of the confirmed ones, so "only" goes beyond him as well.
- Fix, `uncertain[4]` (four sentences: 16, 17, 21, 22 words): "What the mendicant decree did: Glassberger says all orders but the Minors and Preachers were dissolved. Salimbene says the new orders, such as the Sack friars and the Apostles, were dissolved. Clement XIV says it banned for ever the mendicant orders founded since the Fourth Lateran Council without confirmation. Lea says confirmed orders could go on but take no new members, and the Carmelites and Augustinians were left on sufferance."
- Fix, records Lea side: "Left the Carmelites and Augustinians on sufferance until further order, and let mendicant orders confirmed since the Lateran council continue, but admit no new members, acquire no new houses and sell nothing without the Holy See's licence: Lea, 1888 (lea_history-of-the-inquisition-of-the-middle-ages-v3_1888.txt l.1856-1865)."

**C2-S2. Salimbene is made to say Gregory "forbade new orders such as the Sack friars". He says Gregory dissolved the new orders, and the grouping is not in Coulton's English.** (Misread witness; wrong work cited for the wording; a fix that brings in a new error.)

- Where: entry `decided[3]`: "Salimbene, a Franciscan of the time, says in Coulton's English that Gregory forbade new orders such as the Sack friars and the Apostles." Records contested claim "What the mendicant decree did", Salimbene's side: "Forbade new orders such as the Sack friars and the Apostles: Salimbene, in Coulton's English and in Glassberger's editors' Latin (... l.16092-16094; ... l.7323-7325)."
- Evidence: Salimbene's Latin, quoted by Glassberger's editors (`glassberger_chronica-analecta-franciscana-v2-lat_1887.txt` l.7323-7325): "Gregorius X. cassavit in concilio Lugdunensi Religiones mendicantes, quae noviter apparuerant, ut Saccatorum et istorum ribaldorum, qui se appellabant Apostolos". "Cassavit" is "dissolved, annulled": orders that already existed, not a ban on founding new ones. In Coulton's English the two orders are told apart. The Sack friars are abolished, and this is Coulton's report, not Salimbene's words: "Salimbene, therefore, is convinced that Gregory X was divinely inspired in abolishing the Order" (`salimbene_from-st-francis-to-dante_coulton1907.txt` l.15763-15765). Only the Apostles' "further multiplication" was forbidden (l.16092-16094). The phrase "new orders such as the Sack friars and the Apostles" comes from the Latin, not from Coulton. The error also makes Salimbene look further from Glassberger ("aliis omnibus cassatis", l.7304) than he is. The records claims that quote the Latin (l.7323-7328) and Coulton (l.15763-15766, l.16092-16094) are right as written.
- Fix, `decided[3]` second sentence (22 words, then the tag): "Salimbene, a Franciscan of the time, says Gregory dissolved the new mendicant orders, such as the Sack friars and the Apostles (Glassberger's editors quote his Latin)."
- Fix, records Salimbene side: "Dissolved the newly founded mendicant orders, such as the Sack friars and the Apostles: Salimbene's Latin, quoted by Glassberger's editors (glassberger_chronica-analecta-franciscana-v2-lat_1887.txt l.7323-7325); in Coulton's English, Gregory forbade the Apostles' further multiplication (salimbene_from-st-francis-to-dante_coulton1907.txt l.16092-16094), and Coulton reports that Salimbene thought him inspired in abolishing the Order of the Sack (l.15763-15766)."
- The `record` note on Salimbene ("in Coulton's selected English, with his Latin on the mendicant ruling quoted by Glassberger's editors") and the `absent_details` note are right and stay.

### Minor

**C2-M1. The records claim that dates the patriarch list uses a year that comes before the list's own last entries.** Records claim: "...closes its count at the year 6800 (1292 in Migne's bracket); so it was written about 1300". The count runs "μέχρι τοῦ αὐτοῦ Ἰωάννου ... ἔτει ςω΄" (PG 147 l.21409-21411). But the list gives John nine years and then Athanasios's return (l.21395-21402). So 6800 cannot be the year of writing, and it is no evidence for "about 1300". The date rests on the last entries and on Andronikos being called "most pious". The conclusion stands; the reasoning in the claim should be put right. Fix: "Nikephoros Kallistos's patriarch list ends with John XII's nine years and the return of Athanasios under Andronikos II, and calls Andronikos 'the most pious emperor'; so it was written in his reign, about 1300. Its count closes at the year 6800 (1292 in Migne's bracket), earlier than those last entries."

---

## Verified

- Brief: every changed sentence was checked. "From about 1300 on": PG 147 list (above); no earlier held Greek text. Bannwart: Denzinger header l.1-2 and note l.14515-14517 ("anno 1267 a CLEMENTE IV Michaeli Palaeologo proposita ct ab hoc in Concilio LUGDUN. II GREGORIO X oblata est"). Sphrantzes "ill-treated": l.1259-1260. The close: Mirbt l.26478 "Approbante vero Lugdunensi concilio secundo"; the quotation is unchanged.
- The writing passes. Sentences are at or under 26 words, and the 26-word close is mostly the quotation. There is no empty contrast and no "X and never Y". Each paragraph holds one idea.
- Entry: `attended[1]`, `attended[5]`, `decided[1]`, `decided[3]` (apart from C2-S2), `outcome[1]`, `outcome[7]`, `uncertain[0]`, `[6]`, `[8]`, the Dominican and Carmelite notes, the record notes, `sources` (Salimbene file header l.1-6 matches the title and translator).
- Records, new or changed: Salimbene l.13617-13619 ("In 1274 he celebrated a General Council at Lyons, wherein he appeared truly holy, for there he ordained many good constitutions"), l.15763-15766, l.16092-16094; Glassberger l.7301-7305 and l.7323-7328 ("volens implere decretalem Innocentii III"); Eubel l.14488-14489 ("Alias « Saccorum », de quibus (in concilio Lugdunen. se-"); Clement V's bull l.14393-14410; the Recueil l.54168-54172; Doukas l.14310-14316; Joseph of Methone PG 159 l.56894-56920; Creyghton and Galesinius on Kalekas (R1-checked lines, unchanged citations); the `absent_details` Greek note (Kalekas "post errores a Palama disseminatos", PG 152 l.367-369; died 1410, l.388).
- Records changed only under this key and parse; the entry parses.

## Searches run

- `grep -c -E "Β[έε][κχ][κχ][οου]|Βεκκ|Βέκκ"` over all `cic/texts/`. The Greek hits are Gregoras v2 l.38300 (a Ducange note), the Sphrantzes chronicle l.1313 and l.1433, Gedeon, Papadopoulos-Kerameus, Syropoulos, Bessarion, PG 159, and Cantacuzenus v3 l.13458 (a false hit). None is earlier than about 1300.
- `grep -c -E "Λουγδ|Λούγδ"`: Routh, Bessarion, PG 159, Gennadios, Chrysostom, the Pedalion, Palamas's homilies, PO 15, Socrates. As in round 1, none is a Greek account of 1274-1282.
- `ls cic/texts | grep` for PG 140-146, Bekkos, Gregory of Cyprus, Blemmydes, Pachymeres, Ephraim's chronicle, Metochites, Planoudes, Akropolites, Moschabar, Choumnos. Only Cantacuzenus v1-3, Gregoras v2-3 and PG 147 are held. Bekkos's own works (PG 141) are not held. The absence stands.
- Palamas PG 150 l.52600-52700: a codex index (titles, incipits, folio numbers). Round 1 changes were right not to cite it as text.
- Lea l.1844-1872, read in full around the cited lines. This found the dropped condition in C2-S1.
- `Open-Gaps.md` grep "lyon": no Lyon II census entry (C-S3).
