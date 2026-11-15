# Round 3 recheck (the last round): era 5 council profiles (2026-11-15)

A targeted recheck by three fresh Opus agents, one per council, none of whom had seen the drafting or any earlier fixing, at full effort: every round 2 finding, everything changed since round 2 (`git diff 635a3463 HEAD`, including the pass that split entry sentences over 25 words), and the council's lines in Open-Gaps 267. Part A: Clermont. Part B: Lateran IV. Part C: Lyon.

Open after this round: Lyon C3-B1 (blocking) and C3-S1 (substantial); Lateran IV B3-S1 (substantial). All three came in with the sentence-split pass. Mark's standing cap ruling of 2026-11-14 covers minor round 3 fixes only, so these go to the coordinator for Mark's cap ruling; nothing is applied until then.

---

## Round 3 targeted recheck (last round), Part A: Council of Clermont (1095)

**Council.** `council-of-clermont-1095`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era5/council-of-clermont-1095.brief.txt`, `audio/council-of-clermont-1095.audio.txt`, `council-of-clermont-1095.entry.json`, `records.json` key `council-of-clermont-1095`; Open-Gaps 267 (Clermont lines). Changes `635a3463..HEAD` on `claude/cft-councils-era5` (commits 4c882436, 574a7e0d, 22a56fb9, 7541884e).
**Brief.** 400 words (2:30 at 160 wpm, at the cap). `grade_text`: FK 7.08, Flesch 68.77. Longest sentence 25 words (the Anna sentence). No sentence runs over 25 words.
**Audio.** It equals the brief, with `[calmly] ` at the start and `[warmly] ` before the last paragraph. I checked this by script.
**Entry.** No sentence in any string field runs over 25 words (checked by script). The keys are unchanged.
**JSON.** The entry and `records.json` both parse.
**Reviewer.** A fresh Opus reviewer at full effort. I edited no repo file and made no model, network or paid calls.

Abbreviations as in rounds 1 and 2 (M21, PL152, PL159, PL166, LP1, LP2, MIRBT, CART, WT, ANNA).

## Verdict: PASS, with two minor findings

- **Round 2 findings.** All seven are resolved correctly.
- **The investiture fix (A2-S1).** It is sound everywhere: the brief, `decided[3]`, the new `uncertain[1]`, records claim 34, the Hugh of Die claim and the new contested claim.
- **Sentence-splitting pass.** It changed no fact, number or citation, but in four places the split left a second sentence that no longer carries its writer's name (A3-M1).
- **Records.** One records edit made the year dispute read badly (A3-M2).
- **Severity.** Nothing is blocking or substantial.

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| A2-S1 | RESOLVED | **Brief p.5:** "Another forbade any cleric to hold paid church posts in two cities." This is M21 l.12080-12082: "Urbanus II. in eodem concilio, cap. 14. Nulli clerico liceat deinceps in duabus civitatibus duas praebendas obtinere". **`decided[3]`:** it now opens "The Beauvais record gives these under headings that name Urban II at Clermont." Cap. 11 (l.12064), cap. 12 (l.12071) and cap. 14 (l.12080) each name Urban. "or promoted to church offices" is restored (l.12076, "vel ad alios honores ecclesiasticos promoveantur"). Investiture is gone. **`uncertain[1]`:** it matches M21 l.12045 ("Ex Concilio Clavomontano", no pope) and PL152 l.4329-4351 (Hugh of Die, legate in Gaul, a Clermont council "vel initio ipsiusmet anni 1077 vel sub finem"). **Records:** claim 34 adds "with no pope named". The Hugh of Die claim is Dominant Modern Reconstruction. The contested claim is Inferential-Thin, as the recheck worded it. The cap. 14 claim was already there (records l.227-228). |
| A2-M1 | RESOLVED | **`uncertain[5]`:** "The same notice has Urban die in 1096, where Duchesne dates his death to 1099." This is LP1 l.47699 ("Et anno Domini mxcvi obiit") and LP2 l.71346 ("URBANUS II (1088-1099)"). **Lambert `record` note and the Lambert claim:** both add the death year, with the witness range widened to l.47693-47699. **New claim:** Duchesne's heading. **The "The year" contested claim:** the text was applied where the recheck said, but the result reads wrongly (A3-M2). |
| A2-M2 | RESOLVED | **Brief p.3:** "Lambert, a canon of Saint-Omer writing about 1120, gives 310 bishops." This is LP1 l.47588-47589 ("composa, vers l'an 1120") and l.47695 ("cccx episcoporum"). **Word cuts:** all three 1-word cuts are present ("Adhémar, bishop of Le Puy, came forward"; "a Beauvais council in 1114"; "for devotion alone, not to gain"). **`attended[1]`:** "writing about 1120, gives 310 bishops". |
| A2-M3 | RESOLVED | **`uncertain[9]`:** the false "only" is gone, and "No witness of the time among ours says so." now follows the Hours sentences. The fixer wrote "says Petreius gives no proof that the Carthusians took up the Hours before Clermont". That wording is sound. PL152 l.26645-26654 sets out Petreius's view that the apparition, and so the Carthusian Hours, came before the council and the clergy then copied it. The editor answers "verum quod hic asseverat, nullo plane argumento probat" (l.26653). **Records:** "questions the apparition, without denying it outright (l.26582-26604)" matches "indubitanter negare idcirco non ausim" (l.26591-26592). |
| A2-M4 | RESOLVED | **`calledBy`:** "speaks of the council he held at Clermont, city of Auvergne." This is CART l.13306-13307, "celebravimus". |
| A2-M5 | RESOLVED | **`uncertain[0]`:** "Canons reach us only in later copies, chiefly Mirbt's sourcebook and the Beauvais record of 1114. Editors' notes printed by Mansi describe a few more." The notes in question are M21 l.27445-27448 (Baluze, on the monks' canon) and l.45240 (the collector's note, "Urbanus II. in concilio Claromontano ... cap. 5", on the bishop). **`absent_details[0]` and the new Baluze claim:** both in place (l.27445-27448 read). |
| A2-M6 | RESOLVED | **`datesNote`:** it now ends "the day of Urban's speech." |
| Coordinator, Who click | SOUND | Henry IV and Gregory VII are taken off `people`. Neither took part, condemned or acted on the decisions. That is the rule at Decision-Log l.2719 and l.3292. Alexios (LISTED; he received the armies and required the oath) and Robert of Flanders (who acted on the decree) stay. |
| Coordinator, FK 7.08 | NOTE, no finding | The pattern (l.8) and CLAUDE.md treat grade 8 as a floor. The coordinator's reason is recorded in R2_changes: raising the grade would mean sentences past 25 words, and era 4's Whitby is the precedent. Nothing in the text is padded or flattened. It stays a recorded decision. |

## New findings

### Blocking

None.

### Substantial

None.

### Minor

**A3-M1. Minor (the split pass left four second sentences without their writer).** The pass split long sentences in `issue[1]`, `issue[3]`, `issue[4]` and `outcome[7]`. In each, the writer's "says" now governs only the first sentence. The second now reads as the narrator's own statement. No fact, number or citation changed. The neighbouring text still points to the right writer, so this is minor, not substantial. One of these claims is itself disputed: Gregory VII's plan is one side of "Who started it" (`uncertain[6]`; records contested claim, LP2 l.71356-71362). The pattern asks for "each item with its witness" (Council_Profile_Pattern.md l.52) and for "what only a later narrative says ... told as that writer's account" (l.20).

- **`issue[1]`** (council-of-clermont-1095.entry.json, `issue[1]`) now reads: "William of Tyre says Urban held a council at Piacenza. Then, fleeing the anger of the emperor Henry IV, he left Italy and crossed the Alps into the kingdom of the Franks."
  - Replace the second sentence with: "Then, William says, fleeing the anger of the emperor Henry IV, he left Italy and crossed the Alps into the kingdom of the Franks." (23 words)
- **`issue[3]`** now reads: "The Book of the Popes tells what Urban had heard. His predecessor Gregory VII had preached the journey to Jerusalem for the defense of the Christian faith. He could not carry it out because King Henry persecuted him." The source is LP2 l.71356-71358: "Audierat iste ... praedecessorem suum Gregorium papam praedicasse ... Iherosolimam ... pergere ... quod facere minime potuit quia persecutio Heinrici regis ...".
  - Replace the whole item with: "The Book of the Popes says Urban had heard of his predecessor's plan. In that telling, Gregory VII had preached the journey to Jerusalem for the defense of the Christian faith. He could not carry it out because King Henry persecuted him." (13 / 18 / 11 words)
- **`issue[4]`** now reads: "Anna Komnene says Peter came back from a failed pilgrimage, ill-treated by Turks and Saracens. He proclaimed in all the Latin lands that a divine voice bade him call the counts of Frankia to free Jerusalem."
  - Replace the second sentence with: "In her telling, he proclaimed in all the Latin lands that a divine voice bade him call the counts of Frankia to free Jerusalem." (24 words)
- **`outcome[7]`** now reads: "There he says the same remission of sins was later granted to those going to fight in Spain. It had been granted at Clermont to the defenders of the Eastern church." The source is M21 l.27412-27414: "quae Orientalis ecclesiae defensoribus concessa fuerat in concilio Claromontano".
  - Replace the last sentence with: "In his account, it had been granted at Clermont to the defenders of the Eastern church." (16 words)

**A3-M2. Minor (a records edit makes the year dispute read wrongly).** The location is `records.json`, Clermont `contested_claims`, "The year", the 1096 side. The death clause was inserted after "(LP1 l.47694)", as the A2-M1 recheck instructed. It now reads: "1096: Lambert of Saint-Omer, a contemporary hand by Duchesne (LP1 l.47694); the same notice puts Urban's death in 1096 (LP1 l.47699), against 1099 in Duchesne (LP2 l.71346), Migne's heading to the act (PL159 l.74878), another Bollandist note (AASS-JUN5 l.148148-148149), and Baldric's printed ...".

The problem is the list that follows "against 1099 in Duchesne". Migne's heading, the second Bollandist note and Baldric's bracket now read as further witnesses for 1099, when they are witnesses for the council in 1096. The sources are clear: PL159 l.74878 "(Anno 1096.)"; AASS l.148148-148149 "mxcvi"; PL166 l.77773-77774 "(1096)".

- Replace the 1096 side with: "1096: Lambert of Saint-Omer, a contemporary hand by Duchesne (LP1 l.47694), though the same notice puts Urban's death in 1096 (LP1 l.47699), against 1099 in Duchesne (LP2 l.71346); Migne's heading to the act (PL159 l.74878); another Bollandist note (AASS-JUN5 l.148148-148149); and Baldric's printed 'anno subsequente (1096)' after a star-shower of April 1095 (PL166 l.77749-77751, 77773-77774), the bracket likely an editor's."
- Keep the 1095 side as it is.

### Note for the coordinator (no finding)

**A third council at Clermont.** M21 l.1454-1490 prints a "CONCILIUM CLAROMONTANUM" of 1110 ("MCX.", l.1508). The bishop of Clermont held it at the order of the legate Richard of Albano, on the Mauriac case.
- Like Hugh of Die's council, it falls before Beauvais (1114). I found no investiture text in it.
- `uncertain[1]` says "another council", not "the only other", so the entry is not wrong.
- The contested claim names two candidates. If it is touched for any other reason, this one could be added. It is not a finding, because nothing stated is false.

## Open-Gaps 267: the Clermont lines

Every Clermont statement holds.

- **NOT SCORED list.** The 13 names match `people` exactly, with the NOT SCORED verdict and no id. Hugh of Cluny and Alexios are LISTED, and are rightly left out. "Henry IV and Gregory VII are left off the Clermont click: neither took part" matches the entry.
- **La Chaise-Dieu.** There is no census tradition for it (`movements` has none; `cluniac-reform-monasticism` exists).
- **Census edge** `latin-papal-church-gregorian--latin-church-of-outremer`:
  - The note reads "decreed that the journey to free the church of Jerusalem would count in place of all penance", which drops "pro sola devotione, non pro honoris vel pecuniae adeptione" (MIRBT l.11226).
  - "Latin clergy filled the new sees" rests on the two Dulaurier notes at l.15578-15581 and 15582-15584. Open-Gaps cites them as "Dulaurier's notes, Matthew of Edessa l.15578-15584". Accurate.
- **Library headers.**
  - The PL166 header (Stephen Harding's volume) names only the Cistercian texts.
  - The PL159 content note names only Eadmer.
  - The LP2 and Le Couteulx content notes leave out the Urban items.
  - All accurate.
- **Not held.** None of the cic/texts filenames matches Fulcher, Robert the Monk, Guibert, the Gesta Francorum, Bernold or a PL 151. There is no Mansi tomus 20. The grep hits for those names are only mentions in other works.
- **Scan corrections.** The Lambert line range is l.47693-47697, the count line, and is correct. The Mirbt range l.11220-11233 is correct. `latin-papal-church-gregorian`, `cluniac-reform-monasticism`, `byzantine-church-after-1054` and `military-religious-orders-templars-hospitallers` all exist in the census.

## The brief

- **Accessible and rigorous.** Each sentence carries one fact, and the witnesses are named in the text: Baldric "says he watched"; William "nearly ninety years later"; Lambert "writing about 1120"; Anna "what she called".
- **No AI tells.** There is no hedging filler, empty contrast or assistant cadence.
- **The new cap. 14 sentence.** It is plain and exact. "Paid church posts" is a fair plain rendering of "praebendas", and "deinceps" ("from now on") is dropped without changing the meaning.
- **Order and form.** They follow the pattern: the scene; whose account and that the acts are lost, said early (p.2); who came; what was decided; what came of it.

## Verified

- **The Beauvais canons.** M21 l.12040-12084: every Clermont heading in the Beauvais list (l.12045, 12064, 12071, 12080) and each canon's Latin against the entry's English.
- **Hugh of Die's council.** PL152 l.4325-4352: Hugh of Die's Clermont council and the editor's 1076/1077 dating.
- **The Hours of the Virgin.** PL152 l.26582-26665: the hedged doubt of the vision, Ruinart's "Ferunt", "imo reipsa, ut apparet ... fuerit injunctum", Petreius and "nullo plane argumento probat".
- **Lambert.** LP1 l.47586-47591 and 47690-47699: Lambert about 1120, the notice, 310 bishops, 18 November, 1096 and the death in 1096.
- **Duchesne.** LP2 l.71346-71362: Duchesne's heading "(1088-1099)", and "Audierat ... Gregorium ... praedicasse ... persecutio Heinrici regis".
- **Mirbt.** MIRBT l.11218-11233: canons 2 and 9, "Codex Cencii", "ac primum peregrinis".
- **The act of concord.** PL159 l.74878-74966: Hugh of Cluny and Pontius "in Claromontensi concilio per manum domini papae ... et venerabilium archiepiscoporum ... Hugonis Lugdunensis et ... Aldeberti Bituricensis", the "Anno 1096" heading, and the date 1 December 1095. The `attended[2]` split ("as present"; "With them it names") is supported.
- **Baluze and the collector's note.** M21 l.27404-27416: the Spanish indulgence, "quae Orientalis ecclesiae defensoribus concessa fuerat in concilio Claromontano". l.27443-27450: the monks' canon. l.45236-45242: the collector's note on cap. 5.
- **The 1110 council.** M21 l.1440-1530: the Clermont council of 1110 (see the note for the coordinator).
- **Census and Open-Gaps.** `cic-website/data/world-census.json` edge [297] and the movement ids.
- **The split pass.** Every changed entry sentence was compared word for word with its round 2 text (`git diff --word-diff 635a3463 HEAD`):
  - teaser, knownFor, datesNote, `issue[0-4]`, calledBy, `attended[0-2]`, `decided[0-4, 6, 8, 9]`, `outcome[2, 3, 7]`, the record notes, the Peter the Hermit part, and `uncertain[0, 5, 6, 9]`;
  - no number, date, name, qualifier ("only", "chiefly", "for devotion alone", "until ... or ... before the pope", "above all") or citation was lost or moved;
  - the only defects are the four attributions in A3-M1.

## Searches run

- A script over every string field in the entry, for sentences over 25 words. None was found.
- Brief against audio, by script: equal apart from the two tags.
- `grep -n` in M21 for Clermont forms (Claromont, Clarom) near "Urban": l.12064, 12071, 22819, 27446, 45240. This confirms the "few more" of `uncertain[0]` (Baluze l.27446; collector l.45240). It also shows that l.22819 is a later matter.
- M21 l.1400-1530, for the date of the "CONCILIUM CLAROMONTANUM" at l.1454: 1110.
- `cic/texts/` filenames for Fulcher, Robert the Monk, Guibert, the Gesta Francorum, Bernold, PL 151 and Mansi tomus 20: none held.
- Census `movements` ids, for La Chaise-Dieu and the four scan traditions.

---

## R3 targeted recheck, part B: Fourth Lateran Council (1215)

- **Council:** `fourth-lateran-council-1215`
- **Files:** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era5/fourth-lateran-council-1215.brief.txt`, `audio/fourth-lateran-council-1215.audio.txt`, `fourth-lateran-council-1215.entry.json`, the `fourth-lateran-council-1215` key of `records.json`, and the Lateran IV lines of Open-Gaps 267. Branch `claude/cft-councils-era5`, diffed `635a3463..HEAD` (`7541884e`).
- **Brief:** 400 words, about 2:30 at 160 wpm (at the cap). `grade_text`: **FK 8.13, Flesch 62.84**. Unchanged since round 2 (no diff).
- **Audio:** equals the brief, with `[calmly] ` at the start (l.1) and `[warmly] ` before the last paragraph (l.19). No other tag.
- **JSON:** entry and records parse. Field set and order match the pattern and the era 4 entries; `informalName` is a pattern field (Council_Profile_Pattern.md l.46).
- **Sentence lengths:** no entry sentence now runs past 25 words (scripted split over every string field).

## Verdict

**APPROVED TO PROCEED once B3-S1 is applied as worded. 0 blocking, 1 substantial, 5 minor.**

Every round 2 finding is resolved. The new findings all come from the sentence-splitting pass or from Open-Gaps 267. One split (the Pedalion, `outcome[7]`) moved "nearly six centuries later" so that it now reads as six centuries after 1800. The minors are an attribution loosened by a split, a citation that now covers less, an ambiguous "its", a loose "manuscript ... is printed", and a name in Open-Gaps that B2-M3 removed from the entry. All fixes are text-only and worded below; none needs another review round.

---

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| B2-B1 | RESOLVED | `absent_details[10]` detail now "A Cathar or Waldensian voice of the time on the council"; the note adds Léger with the recheck's text. Checked: Léger livre 1 header Creator "Jean Léger, pasteur et modérateur des Églises des Vallées"; l.17714-17715 "cette Tranfubftantiation n'a pû dire établie , ni pafTer en article de Foy , que dans le XIII. fiecle , fous Innocent III. au Concile de Lateran"; l.20345-20347 "Innocent 111. en détermina li forme au ... Concde de Lateran ... par ce moyen lût établie la Tranfubilantiacion en Article de Foy". The note's "became an article of faith under Innocent III at the Lateran council" is fair. |
| B2-M1 | RESOLVED | `traditions` notes for `cathars-albigensians` and `the-waldensians` now read "a heading in Denzinger's Enchiridion, in Bannwart's edition of 1911". Denzinger header l.1-2 ("editio undecima quam paravit Clemens Bannwart"); heading l.13857-13858 "Oecumenicum XII (contra Albigenses, loachim, Waldenses etc)". Optional part applied in `contested_claims` (general/local). |
| B2-M2 | RESOLVED | New `sources.fromTheCouncil` row for Cajetan (thomas-aquinas ... leonine1906.txt). Header l.1 "with the commentary of Cajetan"; l.30504-30513 "Christi corpus et sanguis in sacramento Altaris sub speciebus panis et vini veraciter continentur ... transubstantiatis pane in corpus et vino in sanguinem potestate divina"; l.33673-33676. Optional `record` rows added. Glassberger editors' note 5, l.7318-7323, quotes Salimbene quoting canon 13 ("ne quis de cetero novam Religionem inveniat, sed quicumque ad Religionem converti voluerit, unam de approbatis assumat"). "Dominican commentator": l.63 "THOMAE DE VIO CAIETANI ORDINIS PRAEDICATORUM". |
| B2-M3 | RESOLVED (entry) | `people` name is now "Almaric". Not carried into Open-Gaps 267: see B3-M4. |
| B2-M4 | RESOLVED | `claims[1]` ends "...Jordan tells this a paragraph after the two men of Toulouse gave themselves to Dominic". Acta Sanctorum Aug. I l.93023-93026 "obtulerunt se servo Christi Dominico probi viri & idonei de Tholosa", the two named next (Peter, Thomas); l.93047-93050 "Adjunctus autem eidem episcopo F. Dominicus, ut simul adirent concilium Lateranense". |
| B2-M5 | RESOLVED | `issue[2]`, `attended[4]`, `decided[2]`, `outcome[1]`, `outcome[3]`, `outcome[6]` carry the recheck's text word for word; the Bartholomew `record` note has its period. `attended[5]` was worded differently from the recheck ("Gerard de Frachet wrote a Dominican collection of about 1260. In it he tells..."); sound, but the split leaves "its editor" without a clear antecedent: see B3-M3. |
| B-M10 (R1) | NOT APPLIED-SOUND | Optional close; the coordinator kept the sourced Vitry close, as era 4 accepted. |
| B-S6 (R1) | RESOLVED | The census items are now logged in Open-Gaps 267 (checked under scope 3 below). |
| B-M6 (R1, partial in R2) | RESOLVED | Closed by B2-M1. |

---

## New findings

### Substantial

**B3-S1. The split of `outcome[7]` re-anchors "nearly six centuries later" to 1800.**
- **Where:** `fourth-lateran-council-1215.entry.json`, `outcome[7]`.
- **Evidence (now):** "The Pedalion is the Orthodox canon-law book of Agapios and Nikodemos of Mount Athos, first printed in 1800. Nearly six centuries later, it called the council a local synod held in the Lateran of Rome in 1215."
- **Before the split:** "Nearly six centuries later the Pedalion, the Orthodox canon-law book of Agapios and Nikodemos of Mount Athos (first printed in 1800), called the council a local synod..." There "later" ran from the council. Now the nearest date is 1800, so the sentence reads as six centuries after the printing. The split changed the meaning.
- **Fix:** replace the second sentence with: "Nearly six centuries after the council, it called the meeting a local synod held in the Lateran of Rome in 1215." (21 words.) The first and third sentences stay.

### Minor

**B3-M1. The split of `uncertain[5]` turns the reported wording into a bare command.**
- **Where:** entry `uncertain[5]`: "What canon 13 forbade: the Bollandists and Salimbene, as Glassberger's editors quote him, give its wording. No one is to found a new religious order."
- **What is wrong:** the second sentence now stands alone, with no mark that it is the canon's wording. The sentence before the split was 25 words, so it did not need splitting.
- **Fix:** "What canon 13 forbade: the Bollandists and Salimbene, as Glassberger's editors quote him, give its wording: no one is to found a new religious order." (24 words.) The last sentence stays.

**B3-M2. The split of `outcome[5]` leaves the citation on the second sentence only.**
- **Where:** entry `outcome[5]`: "At Trent, the eighth canon on penance names the constitution of the great Lateran council. It anathematizes anyone who says the faithful are not bound to confess once a year according to that constitution (Mirbt)."
- **Evidence:** Mirbt l.18263-18264, "aut ad eam non teneri omnes et singulos utriusque sexus Christi fideles iuxta magni concilii Lateranensis Constitutionem semel in anno". The text is right. Before the split, "(Mirbt)" covered the whole sentence. Now the first sentence has no witness.
- **Fix:** "At Trent, the eighth canon on penance, as Mirbt prints it, names the constitution of the great Lateran council. It anathematizes anyone who says the faithful are not bound to confess once a year according to that constitution." (19 and 20 words.)

**B3-M3. `attended[5]`: "its editor" has no clear antecedent after the split.**
- **Where:** entry `attended[5]`, sentence 4: "One manuscript and Placid Conway's English put this during the Lateran council, and its editor Reichert dates it to 1215."
- **Evidence:** the collection is named two sentences back, so "its" now reads as "this" (the story). Reichert's note a, Vitae Fratrum l.1743: "Hanc visionem accidisse anno 1215 constat ex II red. huius operis"; variant C, l.1776-1777: "circa concilium Lateranense anno domini 1215". The facts hold.
- **Fix:** "One manuscript and Placid Conway's English put this during the Lateran council. The collection's editor, Reichert, dates it to 1215." (13 and 9 words.)

**B3-M4. `calledBy`: the split says a manuscript is printed in a note.**
- **Where:** entry `calledBy`, sentence 3: "A variant manuscript of Pulkava's Bohemian chronicle is printed in its editor's note."
- **Evidence:** `laurentius-de-brezova_historia-hussitica-lat-ces_goll1893.txt` l.14999-15001. The note prints one passage that manuscript 3 adds under this year ("K tomuto roku klade rk. 3 následující zprávu: Anno Domini MCCXIII epistola a domino papa per orbem mittuntur de concilio convocando, que incipit: Vineam Domini Sabaoth"). It does not print the manuscript.
- **Fix:** "One manuscript of Pulkava's Bohemian chronicle adds a passage, printed in its editor's note." (15 words.) The next sentence ("It says letters went out...") stays.

**B3-M5. Open-Gaps 267 still names "Almaric of Bène".**
- **Where:** `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` l.3503: "Lateran IV: Almaric of Bène, Fulk of Toulouse, Honorius III, ..."
- **Evidence:** B2-M3 renamed the `people` row "Almaric". No held source gives him a place-name, except a book title cited in de Stefano's note ("Almarich'a von Bena", `waldensians_nobla-leicon-pro_destefano1909.txt` l.4742). The Open-Gaps list is meant to match the people rows it lists.
- **Fix:** "Lateran IV: Almaric, Fulk of Toulouse, Honorius III, Dionysius O'Lonargan of Cashel, Conar O'Heney of Killaloe, Eghdon Mac Gilluir." Open-Gaps is append-only by number, not by wording. This is the entry's own unmerged text, so it can be corrected in place before merge.

### Note for the coordinator (no finding)

Open-Gaps 267 says the three profiles "are approved to proceed" and cites the Decision-Log entry "Major councils, era 5" (2026-11-15), which does not exist yet (grep: no hit in Decision-Log.md). This follows era 4, where the Decision-Log entry was written in the round 3 commit (era 4 R3_changes l.16). Both statements hold only once this round closes and that entry is written in the same commit.

---

## Scope 3: Open-Gaps 267, Lateran IV lines

All accurate except B3-M5:
- **People not scored:** Fulk, Honorius III, Dionysius O'Lonargan, Conar O'Heney and Eghdon Mac Gilluir match the entry's NOT SCORED rows. Dominic, Joachim and Francis are WHO with no id in the entry. Innocent III has `id: innocent-iii` (STORY), and the Maronite patriarch is LISTED, so neither belongs in the list.
- **Census gaps:** these were checked against `cic-website/data/world-census.json`.
  - `medieval-irish-christianity` runs c. 664-1169, and `the-dominican-order` runs 1216-1300.
  - No census entry covers the Latin church of Constantinople: `latin-church-of-outremer` covers Jerusalem, Antioch, Acre and Cyprus, with no 1204.
  - Canon 5 ranks Constantinople first after Rome (Denzinger l.14105-14116, "Constantinopolitana primum").
  - Canon 2 condemns Almaric's teaching.
- **Pattern gap:** Joachim's letter of 1200 and the Psalterium are filed `later narrative`, and the note reads "The condemned party's own voice, written before the council" (entry `record`; records `claims`).
- **Census text:**
  - The `latin-papal-church-gregorian` Canon 68 story has "more than four hundred bishops and eight hundred abbots" and "seventy-one constitutions".
  - `maronite-christianity` has "to settle its terms", the pallium and Quia divinae sapientiae.
  - The edge note reads "This rests on modern historians of the Maronites, not on the bull or the council's acts".
  - `innocent-iii` has "summoned the Fourth Lateran Council in 1215".
  - Pulkava's 1213 is at l.14999-15001, in a file whose header names Josef Emler as Pulkava's editor (l.5).
  - Vitry's attendance line is at l.10741-10747.
- **Not held:** no file for Roger of Wendover, Richard of San Germano, Peter of Vaux-de-Cernay, Innocent III's sermons (PL 217), Mansi 22 or the bull Quia divinae sapientiae. The Vineam letter is named only in the Pulkava note.
- **Library headers:**
  - The PL 214 content note names the Gesta and the Registers, but not the Notitia (l.958 "NOTITIA EX CONCILIIS. (Mansi, XXII, 687.)").
  - The Acta Sanctorum Aug. I note names the Dominic commentary and Jordan, but not the Bollandist extracts or Bartholomew.
  - The Maii VI note names Joachim's Life and Luke of Cosenza, but not Honorius's letters or Joachim's letter.
- **Scan corrections:**
  - `innocent-iii` has `kind: person`.
  - Denzinger holds Cap. 4 (l.14072), Cap. 5 (l.14105) and Cap. 21 (l.14118-14120).
  - Canon 2's heading is at l.13942 ("Cap. 2. De errore Abbatis Ioachim"), with the condemnation at l.13944.

## Verified

Every changed string was diffed word by word (`git diff --word-diff`) and read against the source in context. The checks for each split:
- **`issue[1]`:** the Mansi notice's three aims are unchanged.
- **`issue[2]`:** matches Denzinger l.13943-13949.
- **`issue[3]`:** Denzinger l.14078-14089. "Postquam enim Graecorum ecclesia ... se subtraxit, in tantum Graeci coeperunt abominari Latinos, quod ... lavissent; baptizatos etiam a Latinis ipsi Graeci rebaptizare ... praesumebant: et adhuc, sicut accepimus, quidam hoc agere non verentur". The added "also" keeps the "since" over both acts; the split is sound.
- **`attended[2]`:** "So, he says" holds for Vitry's "Unde & eorum Patriarcha interfuit generali concilio Lateranensi" (l.10741-10744).
- **`attended[4]`:** "In the same year" is kept; it matches the R2 text.
- **`attended[5]`:** Reichert l.1743-1777. "Cum esset Rome beatus Dominicus et pro ordinis confirmacione apud Deum et apud dominum papam instaret" supports "Dominic was there to press the pope to confirm his order".
- **`decided[0]`, `[1]`, `[3]`, `[5]` and `[6]`:**
  - The split clauses keep every condition: Easter "for a reasonable cause"; "twice or at least once"; "three or more".
  - "Above all, it was spared because..." keeps "maxime cum" (Denzinger l.14040-14046).
  - "He would bear with their customs" keeps "in quantum cum Domino possumus" (l.14075-14077).
- **`outcome[0]`:** the Jordan citation covers the same sentences as before.
- **`outcome[2]`:** "The ground given for calling them heretics" matches "sumens occasionem ex eo, quod ... Innocencius ... damnavit" (Acta SS Maii VI l.80602-80611).
- **`outcome[4]` and `[6]`:** the splits are sound.
- **`uncertain[0]`, `[1]`, `[2]`, `[3]`, `[4]`, `[6]` and `[7]`:** the splits are sound. In `[7]`, "That letter is addressed to..." keeps the reading of the interleaved columns, which "are read as part of" still hedges.
- **The `record` rows for Jordan and Denzinger:** sound.
- **records.json (Lateran key):**
  - `claims[1]`;
  - `contested_claims` general/local, with the Bannwart wording;
  - `absent_details[10]`, the Léger wording, checked as above.
- **Audio, grade, word count, JSON and pattern:** as in the header.

## Searches run

- `git diff --word-diff=plain 635a3463 HEAD` on the entry and on records.json (the Lateran hunks), and on Open-Gaps.md.
- A script splitting every entry string into sentences and flagging any over 25 words: none.
- `grep -n "Albigens\|Waldens"` and the header over Denzinger; `grep -n "rebaptiz"` over Denzinger and Mirbt; `grep -n "Lateranensis"` over Mirbt (Trent at l.18264).
- `grep -n -i "caietan\|de vio"` over the Leonine tome 12 (l.63, Ordinis Praedicatorum).
- `grep -n -i "emler"` over the Pulkava/Brezova file (header l.5).
- `ls cic/texts | grep -i -E "wendover|germano|vaux|cernay|pl217"`: no file. `grep -rli "quia divinae sapientiae"` gave only unrelated hits (Fulgentius, the African canons, Aquinas).
- A census scan of `world-census.json` for the start and end of every tradition the Lateran lines cite, and for any Latin-Constantinople or Irish tradition after 1169: none. Also the text of `latin-church-of-outremer` for Constantinople and 1204.
- `grep -rn "Major councils, era 5"` over Build/Ministry: only R2_changes and Open-Gaps. `grep "Major councils, era 4"` in the era 4 R3_changes confirms the precedent.

---

## Round 3 targeted recheck, Part C: Second Council of Lyon (1274)

**Council.** `second-council-of-lyon-1274`. Branch `claude/cft-councils-era5`, HEAD 7541884e, diffed against 635a3463 (the round 2 base).

**Brief.** Unchanged since round 2. 392 words (about 2:27 at 160 wpm). FK 8.02, Flesch 64.06 (`engine.m1.gates.grade_text`). Audio equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph (checked by script). Entry and `records.json` parse. No entry sentence is over 25 words (checked by script).

**Verdict.** REVISE. One blocking finding and one substantial finding. Both come from the round 2 sentence-split pass, which made the attribution in two `attended`/`outcome` items more specific than the sources allow. Each fix is a one-line text change. All three round 2 findings are resolved correctly. Round 1's C-S3 is now resolved in Open-Gaps 267. This is the third round, so the coordinator should note the cap. These findings are defects the split pass brought in. They are not another revision of the content that round 2 reviewed.

---

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| C2-S1 | RESOLVED | Entry `uncertain[4]` has the four sentences from the recheck, and "only" is gone. Records, Lea side: "...let mendicant orders confirmed since the Lateran council continue, but admit no new members, acquire no new houses and sell nothing without the Holy See's license ... l.1856-1865". Lea l.1861-1865: "Such mendicant Orders as had been confirmed since the Council of Lateran were permitted to continue, but they were instructed to admit no new members, to acquire no new houses, and not to sell what they possessed without special, license from the Holy See." Clement XIV side is now "Banned for ever the..." with no "only". Mirbt l.23010-23012: "cunctas vero generaliter religiones et ordines mendicantes post concilium Lateranense IV. adinventos, qui nullam confirmationem sedis apostolicae meruerunt, perpetuo prohibuit". He says nothing of confirmed orders. |
| C2-S2 | RESOLVED | `decided[3]`: "Salimbene, a Franciscan of the time, says Gregory dissolved the new mendicant orders, such as the Sack friars and the Apostles. Glassberger's editors quote his Latin." The split of the recheck's parenthesis keeps the attribution. Records, Salimbene side: wording as asked. The fixer's line correction is right. `grep -n` gives "cassavit" at l.7319 and "Saccatorum" at l.7320, "Apostolos" at l.7321, and the Lateran decretal runs to l.7324 ("unam de approbatis assumat"). Round 2's l.7323-7325 was wrong, and so was l.7323-7328 on the claim "Glassberger's editors quote Salimbene's Latin". Both now read l.7319-7321 and l.7319-7324. Coulton l.15763-15766 ("Gregory X was divinely inspired in abolishing the Order") and l.16092-16094 ("had forbidden their further multiplication") check out. |
| C2-M1 | RESOLVED | Claim: "...ends with John XII's nine years and the return of Athanasios under Andronikos II, and calls Andronikos 'the most pious emperor'; so it was written in his reign, about 1300; its count closes at the year 6800 (1292 in Migne's bracket), earlier than those last entries". PG 147 l.21391-21402: John "ἔτη θ΄", then "ἀνάγεται πάλιν ὁ Ἀθανάσιος". The Bekkos entry calls Andronikos "εὐσεβεστάτου βασιλέως" (l.21375-21377). The count closes at l.21409-21411 with "ἔτει ςω΄", and the Latin has "anno C800 [Christi 1292]" (l.21336). The witness range adds l.21391-21411. The reasoning is now right. |
| C-S3 (round 1, still open in round 2) | RESOLVED | Open-Gaps 267, the "Census text, to check" bullet, gives all four `byzantine-church-after-1054` points with the lines round 1 asked for: "needed help from the West" set against the Recueil editors (l.54168-54172); "Lyons 1274 acta"; the Pachymeres story and the burial (Boulliau l.32499-32501, Creyghton l.3090-3094, Guillaume Adam l.63744-63748); and "compliant patriarch" set against l.63805-63812. Each was checked against the census and the texts (see Verified). It is a bullet under 267, not the separate entry round 1 proposed. Nothing is lost, and the owner is named. |

---

## New findings

### Blocking

**C3-B1. The split pass attributes Clement V's 1309 grant to Glassberger. The source is Clement V's own letter in the Franciscan bullarium.** (Misattribution. The sentence split moved the attribution so it covers more than before.)

- Where: entry `outcome[7]`, now: "In 1309, Glassberger says, Clement V gave the Oxford Franciscans the Sack friars' house. It was expected soon to fall to the apostolic see under Gregory's constitution. Boniface VIII later set the Augustinian Hermits and the Carmelites on a firm footing, as before the council (Glassberger)."
- Before the split (635a3463, entry l.58): "In 1309 Clement V gave the Oxford Franciscans the Sack friars' house, which was expected soon to fall to the apostolic see under Gregory's constitution, and Boniface VIII later set the Augustinian Hermits and the Carmelites on a firm footing, as before the council (Glassberger)." The trailing tag was ambiguous. The split turned it into an explicit claim that Glassberger is the witness for 1309.
- Evidence: `records.json` gives the 1309 grant to the bull, kind "acts": "Clement V in 1309 gave the Oxford Franciscans the house of the Friars of the Penitence of Jesus Christ (the Sack friars)..." with witness `bullarium-franciscanum_v5-lat_eubel1898.txt l.14393-14410`. Bullarium V l.14389-14392: "131. Fratribus Min. Oxonen. concedit locum fratrum de Poenitentia I. C. eis contiguum. ... 1309, maii 27, Avinione". At l.14404-14408: "a dictis fratribus sit in brevi ut creditur relinquendus, in dispositione sedis apostolicae iuxta tenorem constitutionis a Gregorio pp. X ... in generali concilio Lugdunen. editae remansurus". Glassberger has no Oxford passage: `grep -n -i "oxon"` gives only l.13962, 14131, 17405, 19604 and the index, none on the Sack friars' house. His one claim here, on Boniface VIII, is at l.7330-7332. The error also turns the council's own papal act into a 1508 chronicler's report, which is a change in witness kind.
- Fix, `outcome[7]` (sentences of 10, 11, 15, 18, 13 and 19 words): "In the Latin church the conclave decree was taken up. The decree set prayers and processions for a vacant Roman see. A council at Ravenna in 1311 ordered them held for vacant cathedrals of its province. In 1309 Clement V gave the Oxford Franciscans the Sack friars' house (his letter, in the Franciscan bullarium). It was expected soon to fall to the apostolic see under Gregory's constitution. Boniface VIII later set the Augustinian Hermits and the Carmelites on a firm footing, as before the council (Glassberger)."

### Substantial

**C3-S1. "Glassberger names their interpreter as John of Balastri (Parastron)". Glassberger does not give "Parastron", and no records claim does.** (Attribution made more specific by the split. A detail in the entry that has no records claim.)

- Where: entry `attended[2]`: "Glassberger names their interpreter as John of Balastri (Parastron), a Franciscan of Constantinople who knew Greek and Latin. At Lyon he interpreted for the emperor and the Greek prelates." Also `people`: "John of Balastri (Parastron)". Also Open-Gaps 267, people bullet: "Lyon: ... John Parastron, ...".
- Evidence: Glassberger l.7252: "interpretem, fratrem Iohannem de Balastri 4 de Constantinopoli". His editors' note 4, l.7265: "Alias Palastro; cfr. Card. Hergenröther". At l.7359-7361 he has "frater Iohannes de Balaslri ... pridem in concilio Lugdunensi interpres Imperatoris Graecorum et Praelatorum Graeciae". "Parastron" is held only in Ducange's note on Gregoras (`gregoras_byzantina-historia-v2-grc-lat_schopen1830.txt` l.38381-38383: "Hi porro Constantinopolin advenerant a Gregorio missi, in quibus erat Ioannes Parastron"). That note does not tie him to Lyon or to Balastri, and no records claim cites it. Before the split, the trailing "(Glassberger)" was already loose. Now Glassberger is made to "name" the man as Parastron. Separately, the second sentence (interpreter for the emperor and the prelates, from l.7360-7361) has no records claim. The only claim on the interpreter is the Creed one (l.7249-7253).
- Fix, `attended[2]` (sentences of 17 and 11 words): "Glassberger names their interpreter as John of Balastri, a Franciscan of Constantinople who knew Greek and Latin. At Lyon he interpreted for the emperor and the Greek prelates."
- Fix, `people` name: "John of Balastri".
- Fix, records (add): `{"claim": "John of Balastri, a Friar Minor learned in Greek and Latin, had been interpreter at the council of Lyon for the emperor of the Greeks and the prelates of Greece, was sent back with the Greeks, and died at Constantinople", "witness": "glassberger_chronica-analecta-franciscana-v2-lat_1887.txt l.7359-7362", "witness_kind": "later narrative", "formation_confidence": "Widely Accepted"}`.
- Fix, Open-Gaps 267 (the coordinator's text): "John Parastron" becomes "John of Balastri".

### Minor

None.

---

## Verified

- **Split pass, every changed string checked against the 635a3463 text.** `teaser`, `datesNote`, `issue[0]` ("Glassberger says" now leads; same witness), `issue[2]`, `calledBy`, `attended[0]`, `[1]`, `[3]`, `[4]`, `decided[0]-[3]` (in [0] and [1], citations moved to the first sentence still cover the whole item), `outcome[1]-[4]`, `outcome[8]`, `uncertain[0]`, `[4]`, `[5]`, `[9]`, and the Dominican, Byzantine, Athonite and Carmelite notes. No meaning, condition or qualifier is lost. The exceptions are C3-B1 and C3-S1.
- `attended[5]`: "A witness at his canonization says he was on the road in Lent when he fell ill at Maenza." The witness speaks of the four days at "castro Magentiae" with the herrings (Acta Sanctorum Martii I l.116080-116087). He says it was "tempore Quadragesimali" while Gregory "convocabat Concilium, ad quod ... vocatus ibat" (l.116095-116100). So the witness supports both the time and Maenza. Tocco (l.112359-112366) and Nicholas of Fossanova (l.114090-114111) are named for the rest.
- `outcome[7]`, Ravenna: Mansi 25 l.43733-43746 ("per constitutionem Gregorianam, Ubi periculum ... fiant orationes & processiones"). The wording is unchanged from the round 1-verified text.
- `decided[2]`: Mirbt l.13385-13386 ("uno solo ferculo ... panis, vinum et aqua").
- Open-Gaps 267, the Lyon lines:
  - The people list matches the entry's 13 NOT SCORED names. Thomas Aquinas is WHO with no id. The census has no `thomas-aquinas` movement (it appears only as an author in a source list). `bonaventure` is a census person.
  - Parties with no census entry: there is no movement for the Augustinian Hermits, the Sack friars, the Apostolic Brethren or the Tatars (script over `world-census.json` movements).
  - Census text: "needed help from the West" (`why`, `longDescription`), "Lyons 1274 acta" (`sourcing`), the story "Michael VIII Punishes the Anti-Unionists" (sources: Pachymeres; Michael VIII, De vita sua), "refused the emperor a Christian burial" and "with the exception of a compliant patriarch" are all present as quoted. Boulliau l.32499-32501 ("sepulturae pompa ac consuetis honoribus privavit"), Creyghton l.3090-3094 ("insepultus projicitur"), Guillaume Adam l.63744-63748 ("nunquam in perpetuum eundem permitteret sepeliri"), the Recueil note l.63805-63812 ("La résistance qu'il opposa d'abord") and the Recueil editors l.54168-54172 all check out.
  - Not held: Zelus fidei (no hit in `cic/texts/`); Religionum diversitatem (only Glassberger's citation of the chapter); Salimbene's Latin chronicle, Pachymeres and Akropolites (no files; Gregoras v2 and v3 only).
  - Scan ranges: Mirbt decree heading at l.13349 ("306. 3. Konzil zu Lyon (1274)"); Glassberger opening l.7157-7158 and editors' "1 Maii" at l.7205; Denzinger Lyon heading at l.14472-14474; Glassberger l.7360-7367 is Balastri's death.
- The records C2-S1 and C2-S2 sides, and C2-M1, as in the table. `records.json` changed only under this key between 635a3463 and HEAD, apart from the other councils' keys.

## Searches run

- `grep -n -i "Balastr\|Parastr"` in Glassberger: l.7252 and l.7359 only (with note l.7265 "Alias Palastro"). `grep -rl "Parastron" cic/texts/`: Gregoras v2 only (l.38383, Ducange's note).
- `grep -n -i "oxon"` in Glassberger: no passage on the Oxford house. Bullarium V l.14385-14410 read in place.
- `grep -n "cassavit\|Saccatorum"` in Glassberger: l.7319-7320 in the Lyon note. Only one copy of the file.
- `grep -l -E "Zelus[[:space:]]+fidei"` and `"Religionum[[:space:]]+diversitatem"` over `cic/texts/`. `ls cic/texts | grep -i` for pachymer, akropol, gregoras, salimbene and the Liber Sextus.
- `world-census.json` scan for movement ids and names matching augustin, sack, apostol, tatar, mongol, thomas, michael and carmel.
- An entry-wide script for sentences over 25 words: none.
