# Council profiles, era 4: review round 1 (2026-11-14)

Round 1, the full review, by three fresh Opus agents that had not seen the drafting, at full effort, in three parts: A (Lateran 649, Constantinople 680-681), B (Whitby 664, Quinisext 691-692), C (Nicaea 787, the Photian councils 861-880). Each part is given as written.

---

# Part A


**Scope.** Two major-council profiles in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era4/`: `lateran-council-649` and `third-council-of-constantinople-680`. For each: the brief, the entry, the audio script and that id's part of `records.json`. Reviewer: independent Opus, first sight of these drafts. No profile file was edited.

**Standard.** `Council_Profile_Pattern.md` (C1 to C8) with `Who_Profile_Pattern.md` checklist items 1 to 9, 11 and 13. Form to match: the approved era 3 councils (`Council-Profiles/era3/`, Toledo brief and entry read). Lessons from `2026-11-14_council-profiles-era3/R1_review.md` and the era 4 Who batch 2 and 3 R1 reviews.

**Method.**
- Every quotation in both briefs and entries was found in its vendored file under `cic/texts/` and read in context for speaker and meaning (long-s, OCR and line-break tolerant).
- The file:line in `records.json` was opened for every claim the briefs rest on, and every factual sentence of each brief was checked. Files: Mansi tomus 10 ("M10") and 11 ("M11"), `npnf214_seven-ecumenical-councils.xml` ("NPNF"), Duchesne's Liber Pontificalis t.1 ("DUCH"), Theophanes PG 108 ("THEO"), the Bizya record PG 90 ("PG90"), Bede in Giles ("BEDE"), Michael the Syrian t.2 ("MICH"), Foulke's Paul the Deacon ("FOULKE"), Eutychius in PG 111, the Hispana collection, Denzinger, Mirbt, William of Tyre, al-Duwayhi.
- Counts checked by hand: the Lateran attendance list at M10 l.88794-88949 has 105 bishops and the priest Deusdedit besides Martin (Felice Tarracinensi at an accented "épife." makes the 105th); the three late signers are at l.115370-115390. Twenty canons, the last numbered XX at l.114640. Eutychius's 289 is his own figure (124 + 168 = 292, less three deacons, PG 111 l.85490-85551).
- Absence searches: Honorius's own letter to Sergius (Denzinger l.9211-9246 and M11 l.51548); the condemned documents in the Lateran acts; Pyrrhus in PG 91; Macarius outside the acts (MICH l.34503-34509); "Roman synod under Pope Martin" (no hit in any file); Wilfrid in M11 (l.30612-30624); Paul the Deacon on the 680 council (FOULKE l.11250-11283).
- Verdicts against the era 3 and era 4 Who scans, the supplement, the dedupe list and the 2026-11-14 rescore; ids against the Who cards and the census copy in the scratchpad; tradition ids, names and dates against the census.
- Readability by `engine.m1.gates.grade_text`. Each audio script was compared by script with its brief, with `[calmly] ` at the start and `[warmly] ` before the last paragraph removed. Suggested brief fixes were applied to scratch copies and rescored: `/tmp/claude-0/-home-user-CIC-Project/3fc04891-4b0e-5b02-a097-fe39a900e3e5/scratchpad/R1A/lateran-council-649.fixed.txt` (399 words, FK 7.44, FRE 67.70) and `/tmp/claude-0/-home-user-CIC-Project/3fc04891-4b0e-5b02-a097-fe39a900e3e5/scratchpad/R1A/third-council-of-constantinople-680.fixed.txt` (399 words, FK 7.69, FRE 66.73).
- No model calls, no network calls, no paid services.

**Result in one line.** Both briefs pass readability and audio, and every quotation is verbatim; no finding is blocking, but each profile has one substantial finding to fix before it proceeds: at the Lateran, Theophanes's wrong exile of Maximus to Cherson is told in the narrator's voice; at Constantinople, a false absence says the condemned reach us only inside the acts.

## Per-council table

| Council | Words | FK | FRE | Audio = brief with the two tags only | Verdict |
|---|---|---|---|---|---|
| lateran-council-649 | 398 | 7.38 | 68.07 | yes | PASS WITH FIXES |
| third-council-of-constantinople-680 | 401 | 7.75 | 66.42 | yes | PASS WITH FIXES |

Both audio scripts equal their briefs once the two tags are removed, and carry no other tag. Constantinople is one word over the 400-word mark, so any fix there needs a cut; the scratch copy shows one way. The longest brief sentence is the Lateran close at 28 words (LAT-7); Constantinople's longest is 23.

## Quotations

Every quoted string in both briefs is verbatim in its file, with the right speaker:
- Lateran: Bede IV.18, "the decision of the synod of the blessed Pope Martin and 105 bishops" (BEDE l.10398-10400), said of John, archchanter and abbot of Saint Martin's, at Benedict's monastery "at the mouth of the river Were" (l.10354-10365).
- Constantinople: Agatho, "has never erred from the path of the apostolic tradition" (NPNF l.24937-24938, the subject being "the Apostolic Church of Christ", his see); Macarius, "one will and one theandric operation" (NPNF l.25685-25686, Session VIII); "Honorius who was some time Pope of Old Rome" (l.25707-25708, Session XIII); the definition, "two natural wills and two natural operations" and "subject to his divine and omnipotent will" (l.25864-25870).

The entries' quotations are verbatim too: "Maximus monachus" (M10 l.92672), Bede's Hatfield line (BEDE l.10330-10331, OCR "oF"), George's "Therefore I give my submission to them and thus I profess and believe" (NPNF l.25663-25664), the Toledo XIV Latin (Hispana l.51523-51526), and Percival's English of the Liber Diurnus oath, rightly marked as his (NPNF l.26275-26279).

---

## lateran-council-649

**LAT-1. Substantial (items 1 and 7; a witness comes loose from its claim; contradicts the Maximus Who profile).** Brief, paragraph 8: "Theophanes says Constans was furious. He had Martin and Maximus brought to Constantinople, tortured and exiled to Cherson. Later, at Bizya, a bishop told Maximus the Roman synod had no force, since the emperor had not ordered it."
- Theophanes does say "eosque tormentis excruciatos in exsilium deportari ad Chersonesi plagas" (THEO l.60843-60847). But the second sentence starts fresh with "He", so the listener hears the exile to Cherson in the narrator's voice.
- Theophanes is wrong about Maximus. The sentence of Maximus's last trial and Anastasius the envoy send him to the Lazi, and the era 4 Who card `maximus-the-confessor` says so: "His last exile. The sentence and Anastasius the envoy send him to the land of the Lazi. Theophanes has Constans exile Martin and Maximus together to the region of Cherson." Its brief ends with him "exiled among the Lazi".
- "Later, at Bizya" then puts Bizya after a Cherson exile. Bizya was his first exile, in Thrace ("in primo ejus exsilio, id est, Bizyae", PG90 l.8767), before the Lazi.
- Fix: "Theophanes says Constans, in fury, had Martin and Maximus brought to Constantinople and tortured. Martin died in exile at Cherson. At Bizya, a bishop told Maximus the Roman synod had no force, since the emperor had not ordered it." Martin's death at Cherson is in the account by one of his clergy (M10 l.88330-88336). The fix adds two words; LAT-7 cuts two. In the entry, `outcome[1]` and the people line for Maximus ("seized and exiled with Martin") tell the same joint exile. Make both "by Theophanes's account", and add to `uncertain` that the sentence and Anastasius send Maximus to the Lazi, as the Who card does.

**LAT-2. Minor (item 1; C1 and pattern 3, the partisan witness).** Brief, paragraph 2: "Those acts survive in Latin and Greek, the record of the side that won". In 649 Martin's side did not win: the brief itself tells his seizure and exile, and the Typos stood until 680. "The teaching they condemned is read into them" also misleads when heard: to "read into" a text means to put a meaning there. Paragraph 3 then gives Martin's charge against Paul with a gloss the Latin does not carry: "Paul had urged the emperor to it, to destroy the catholic teaching." Martin says Paul persuaded the emperor "typum exponere, qui catholicum dogma destrueret", to issue a Typos that would destroy catholic teaching (M10 l.89929-89931). He states no aim of Paul's, and Martin, who called the synod, is a partisan witness the brief does not mark. Fix: "Those acts survive in Latin and Greek, the record of Martin's side, and are told here from the Latin. The documents they condemned are quoted in them in Latin translation." The acts say each was read "de Graeco in Latinam vocem translatam" (l.100118-100121). Then: "Martin told the synod that Paul had urged the emperor to issue it, an edict that would destroy the catholic teaching." The scratch copy carries both.

**LAT-3. Minor (C1 and C4; a witness of the wrong kind).** Entry `attended[0]`: "The Book of the Popes and Bede count 105 bishops, as does the heading of the acts." The records' contested claim says "105: the acts' lists and heading (Mansi l.88610 …)". The heading at M10 l.88609-88616, "CONCILIUM LATERANENSE ROMANUM, IN QUO CENTUM ET QUINQUE EPISCOPI … Monothelitarum haeresim … condemnarunt, anno Domini DCXLIX", is the editors' title: it uses "anno Domini" and "Monothelitarum". The acts' own opening follows at l.88644 ("Incipiunt Deo juvante acta …", marked "Ex Harduin"). The hand count of the list is right (see Method). Fix: credit the heading to the editors, or drop it, and keep the acts' witness as the list and signatures.

**LAT-4. Minor (items 1 and 7; entry `knownFor` and `calledBy` tell two open points flat).** `knownFor`: "The synod at which Rome condemned … the emperors' decrees without the emperor's order, for which Martin and Maximus were seized and exiled." The want of an order rests on the hostile Theodosius in a record from Maximus's side, as `uncertain[4]` says. The cause of the seizure is Theophanes's ("his auditis", THEO l.60843). At Martin's trial the charge was rebellion with Olympius, as the Who card `martin-i-of-rome` tells. `calledBy` opens its second half with a colon-reveal: "The emperor did not order it: at Bizya …". Fix, `knownFor`: "The synod at which Rome condemned the teaching of one will and the emperors' decrees. Theophanes says Constans seized Martin and Maximus for it." `calledBy`: "A hostile bishop at Bizya, Theodosius of Caesarea, told Maximus the synod had no force because the emperor had not ordered it (the record of the hearing at Bizya)."

**LAT-5. Minor (item 1; the letter's addressees).** Entry `outcome[4]`: "The Roman synod's letter of 680 to the Sixth Council". The held heading is "The Letter of Agatho and of the Roman Synod of 125 Bishops which was to Serve as an Instruction to the Legates", addressed "To the most pious Lords … Constantine, the great Emperor, and Heraclius and Tiberius" (NPNF l.25511-25520). This is the A-M17 fault of the era 4 batch 2 round. Fix: "The letter of Pope Agatho and a Roman synod of 125 bishops to the emperors, sent with the envoys to the Sixth Council, speaks of the faith set forth in a council over which Pope Martin presided, as Henry Percival summarizes it (NPNF l.25595-25599)."

**LAT-6. Minor (entry field; a name no held source uses).** `informalName`: "The Roman synod under Pope Martin" is in no held file (searched). Bede has "the synod of the blessed Pope Martin" (BEDE l.10398-10399), and the Bizya record has "the Roman synod" (PG90 l.9572-9575). Fix: "The synod of the blessed Pope Martin", or leave the field out.

**LAT-7. Minor (item 4; a sentence past 25 words).** Brief close: "Bede says that John, a Roman abbot, brought 'the decision of the synod of the blessed Pope Martin and 105 bishops' to Wearmouth in England to be copied." It is 28 words. Fix: "… to Wearmouth to be copied." That makes 26, almost all of them the quotation, and it pays for LAT-1's two words. Optionally drop "that" as well.

**LAT-8. Minor (records; witnesses incomplete or uncited).**
- `contested_claims[2]` cites "Foulke, modern: Martin's election lacked the emperor's confirmation" with no file or line, and Foulke is not in `sources` or `record`. The line is FOULKE l.9938-9939. Binius, in his note on this synod, says the opposite: Constans first confirmed Martin's election "more solito", then asked him to approve the Typos, and Martin answered with the synod (M10 l.117080-117094). Add both, with lines.
- `record`, Theophanes: "files the affair under the wrong year" has no witness in the records. Binius gives it: "scribit Theophanes anno 19. Heraclii" (M10 l.117102-117103). Add a claim with that line, or drop the note.

**LAT-9. Minor (C7; a listed person left off the Who click).** `decided[2]` names Theodore of Pharan first in canon 18 (M10 l.114429-114430). The era 4 scan has him LISTED ("Pyrrhus, Cyrus, Paul, Peter, Theodore of Pharan", `Who_Scan_Era4.md` l.160), but he is not in `people`. Fix: add "Theodore of Pharan, LISTED, Dead; anathematized in canon 18".

**LAT-10. Minor (register; process narration in participant-facing fields).**
- `record[0]` note: "the Greek column is poorly read in the file, and the Latin is used". Fix: "The Latin column is followed here."
- `issue[1]`: "The teaching of one will is thus held in two separate documents by different authors, both only inside the acts that condemn them." This is the reviewer's two-witness test, written as text for the participant. Fix: drop the sentence. `uncertain[0]` already says the teaching survives only as read into the acts.
- `uncertain[0]`: "no account of the synod from the other side is held". Fix: "no account of the synod from the other side survives in the books we draw on."

**LAT-11. Minor (C7; the "Gathered" group).** `traditions`, `latin-africa-under-byzantium`, part Gathered, "By letter". The African letters were written to Pope Theodore before Martin's time and read in session II. Gathered stands for those who met. The list does include Victorianus "Uzalensis" (M10 l.88948), and Uzalis is an African see, but the note does not rest on him. Fix: move the row to Affected, or rest Gathered on a named African bishop in the list with his line.

## third-council-of-constantinople-680

**CP3-1. Substantial (C3; a false absence).** Brief, paragraph 2: "The condemned reach us only inside the acts." The same claim is in entry `uncertain[0]` ("Macarius and Polychronius reach us only inside them") and `absent_details[0]` ("None held; Macarius and Polychronius speak only inside the acts").
- Several of the men this council condemned reach us outside its acts. Sergius's Ekthesis and Paul's letter are read into the Lateran acts of 649 (M10 l.100115-100587, 102688-103116). Pyrrhus speaks in Maximus's Disputatio (PG 91). Honorius's letter to Sergius is printed in Denzinger, "Unde et unam voluntatem fatemur Domini nostri Iesu Christi" (`denzinger_enchiridion-symbolorum-lat_bannwart1911.txt` l.9211-9248), though Denzinger takes it from these acts (M11 l.51548).
- Michael the Syrian, outside the acts, reports Macarius's case: "Macarius d'Antioche disputa longuement … appuyé sur les témoignages de Cyrillus" (MICH l.34503-34508). The entry's own `issue[3]` uses it.
- Every one of these comes through opponents, so the sense the brief wants is true. The words say something false.
- Fix, brief: "The condemned reach us only through their opponents' records." The word count does not change. Entry `uncertain[0]`: "The acts are the winners' record. The condemned reach us only through their opponents: these acts, the Roman acts of 649 and Maximus's debate with Pyrrhus. Michael the Syrian, hostile to the council, reports Macarius's argument from outside both parties." Records `absent_details[0]`: "A text of the party of one will outside its opponents' records. None found; Michael the Syrian reports Macarius's argument but not his words." Optionally, C3 is better met if the card quotes Honorius's own "unam voluntatem fatemur" with its line.

**CP3-2. Minor (item 1; a source line heard out of its context).** Brief close: "Michael says Macarius died a prisoner in Rome. That, he wrote, was how the pernicious heresy of Maximus came in." Michael's "C'est ainsi" sums up the whole account before it: Theodore buying the emperor with gold, the bishops signing the definition "de force", and Macarius sent to Rome (MICH l.34484-34523). Heard aloud, "That" falls on Macarius's death alone. Fix: "Michael says the bishops signed under force, and Macarius died a prisoner in Rome. That, he wrote, was how the pernicious heresy of Maximus came in." This adds eight words, so a cut is needed. The scratch copy cuts the Percival clause in paragraph 2 (see CP3-4).

**CP3-3. Minor (item 4; a hedge dropped).** Brief, paragraph 3: "For forty-six years, the pope's envoys told the council …". The envoys say "during the past forty-six years, more or less" (NPNF l.24649-24650). Fix: "For forty-six years or so, the pope's envoys told the council …". The word budget is tight, so this one is optional.

**CP3-4. Minor (items 4 and 5; reading aids).**
- "in English extracts by Henry Percival, their editor": Percival edited and translated the English extracts. He did not edit the acts, which are Mansi's and Labbe's. And "survive … in English extracts" puts a modern translation among the surviving texts. Fix: "They survive in Greek and Latin." Percival stays named in `sources` and `record`, and the cut pays for CP3-2.
- "anathematized" is new to the listener in paragraph 6. Era 3's CON-6 found the same fault. Fix: "the council anathematized, or cursed, …". That is two words; take them from the paragraph 4 count sentence if needed.
- "a new Simon Magus" gives the name with no context. Optional: "a new Simon Magus, the sorcerer of the Book of Acts". Note that the acts say only "Novo Simoni anathema" (M11 l.57936-57937), so "Magus" is the narrator's gloss and could be left out instead.

**CP3-5. Minor (register; process narration in participant-facing fields).** `attended[1]`: "No count of the held list was made for this profile." `traditions[0]` note: "the census entry already says it taught two wills without naming Maximus." `record[0]` note: "the Greek column is poorly read in the file and the Latin is used." `outcome[4]`: "from the losing side of Chalcedon" is a judgment, not a label. Fix: drop the first and the second's closing clause. Make the third "the Latin column is followed here". Make the fourth "Michael the Syrian, of the church that rejected Chalcedon, closes his account …".

**CP3-6. Minor (C1; witness kind).** `record`, Leo II's letters, kind "participant", and `sources.fromThoseThere`. The pattern defines a participant as "someone who was there or who called it". Leo did neither: he became pope after the council and confirmed it. Fix: move the letters to `fromTheCouncil` as the confirming letters printed with the acts (M11 l.68856, 102060), with kind "acts", or keep the kind and say in the note that he was not present. The same applies to "Councils of Toledo XIV and XV", kind "acts". These are another council's acts, which `sources` rightly lists under `writtenLater`. Make the two fields agree.

**CP3-7. Minor (item 7; a held witness left off a contested claim).** `contested_claims[2]`, "Whether George of Constantinople accepted", sets the acts against Michael. Paul the Deacon is a third witness, on Michael's side: "Georgius the patriarch of Constantinople, Macharius, Pyrrus, Paul and Peter stirred up this heresy … And Georgius the patriarch indeed was rebuked" (FOULKE l.11253-11257, 11283). Foulke's note calls it "a mistake" (l.11262-11265). Fix: add Paul and Foulke's note to the sides and to `uncertain[4]`.

**CP3-8. Minor (C7; listed people left off the Who click).** Session XIII anathematizes Peter of Constantinople and Theodore of Pharan by name (NPNF l.25698-25701). `issue[0]` and `decided[2]` name both. The era 4 scan has both LISTED (`Who_Scan_Era4.md` l.160). Neither is in `people`. Fix: add both, LISTED, "Dead; anathematized".

**CP3-9. Minor (records; a wrong line).** `contested_claims[5]`: Mirbt "September to December 682 (… l.8022)". Line 8022 is the section heading. The date is at l.8038 ("Sept. Dez. 682, an Kaiser Konstantin IV."). Fix the line.

---

## Checks that passed, both councils

- **C1.** Every `record` entry has a kind. Partisan witnesses are marked: Martin, Theodosius at Bizya, the Bizya record, Agatho, Constantine IV and Michael the Syrian. The two exceptions are in CP3-6 and LAT-3.
- **C2.** Both councils have held acts, and both briefs cite them first, for the scene and the count. Lateran gives the Gospels set out in the Constantinian church (M10 l.88719-88725). Constantinople gives the Zeuxippus scene from Session XV (M11 l.57296-57301, 57905-57943). The scene was checked line by line: the silver bier, "perque plures horas perseverans, & insusurrans ei", "nullatenus se posse mortuum suscitare", "Novo Simoni anathema".
- **C3.** At the Lateran the condemned are told through two documents by different authors, the Ekthesis and Paul's letter, with the Typos (M10 l.100115-100119, 102688-102691, 103612-103626). At Constantinople, Macarius speaks in his own words. The exception is the false absence in CP3-1.
- **C4.** Every count has its witness, and the counts are kept apart.
  - Lateran: 105 (acts list, by hand count; Book of the Popes, DUCH l.161960 and M10 l.82051; Bede); 150 (Goar's Latin of Theophanes, THEO l.60749-60750); 110 (Anastasius's Latin, l.116628, quoted by Binius, M10 l.117107).
  - Constantinople: 150 (Book of the Popes, DUCH l.165717; Paul the Deacon, FOULKE l.11278); 289 (THEO l.65259-65261; Eutychius); 250 (MICH l.34484); Percival's under 300 with 174 signatures (NPNF l.24574-24576).
  - Dates: Duchesne's 5 to 31 October 649 is credited to him (DUCH l.162758-162760). "October 649" also follows from the acts' "tertia Nonas Octobris, indictione octava" in Constans's ninth year (M10 l.88719-88723). The Constantinople days are the acts' (7 November, 26 April, 16 September, with indictions, M11 l.22004, 57296, 59127), and the years are Percival's.
- **C5.** `issue`, `decided` and `outcome` are separate in both entries. The Lateran's failure to move the emperor is told through Bizya. Constantinople's qualified Spanish reception is told: "in quantum a praemissis conciliis non disciscunt" (Hispana l.51523-51526).
- **C6.** The Lateran definition is told as signed first by Martin. The 680 definition is told as the act of Session XVIII, with the emperor's signature (NPNF l.26147-26148) and Michael's claim of forced signing.
- **C7.** Both entries have `kind` `major-council` and `kindLabel` "Major council". The verdicts match the scans. Martin I, Maximus, Sophronius, Severus of Antioch, Theodosius I of Alexandria, Theodore of Tarsus, Wilfrid of Ripon and Julian of Toledo are WHO. Heraclius is STORY. Sergius, Pyrrhus, Paul, Cyrus and Honorius are LISTED. Constans II, Stephen of Dor, Maurus of Ravenna, Amandus, Constantine IV, Agatho, Leo II, George, Macarius and Polychronius are NOT SCORED; the scan names Stephen and Constantine IV "not scored". Every id resolves to a Who card or a census person (`heraclius`). Every tradition id is in the census with fitting dates: Heraclian 622-843, Latin Africa 533-698, Anglo-Saxon 597-793, Visigothic 560-711, Syriac Orthodox under Islam 650-1054. Wilfrid's signature for the synod of Britain is in M11 l.30612-30624.
- **C8 and item 11.** Both briefs open on a sourced scene, pass `grade_text` and sit at the 400-word cap.
- **Item 3.** No invented scene, feeling or speech. The Lateran sitting and standing ("Sedentibus episcopis & presbyteris, adstantibus diaconis & clero", M10 l.82077-82079), Maurus's letter (l.90372-90380), Stephen of Dor (l.91063-91075, 91435-91470), the Greek monks (l.92084-92103), the Typos's "bonum quidem intentum … dissonantem autem virtutem" (l.103827-103829), Amandus and Sigebert (l.116989-117024) and Bizya (PG90 l.9570-9590) were all checked. So were Macarius's "nec si membratim incidar, & mittar in mare" (M11 l.35453-35458), the stripping of the pallium (l.36066-36076), Leo II's two letters (l.68856-68866, 102060-102070), and Toledo XIV (Hispana l.51318-51324).
- **Item 4.** No "not X but Y" contrast in the narrator's voice, no rhetorical question, no aphorism and no tail line. Both closes end on a sourced statement. The colon-reveal in LAT-4 is in the entry only.
- **Item 5.** No role stands in for a witness: Duchesne, Binius, Percival, Goar, Fabricius and Foulke are all named.
- **Item 13.** The tags are only in the audio scripts, in the two right places.

## Notes for the coordinator (no fix to these profiles)

- **Scan correction.** The era 4 Who scan row "Theophanes the Confessor … WANTED … Not held" (`Who_Scan_Era4.md` l.114) is out of date. His Chronographia was vendored on 2026-11-13: `theophanes-confessor_chronographia-pg108-grc-lat_migne1863.txt`, Greek with Latin, Anastasius's version included. Both councils and the Maximus and Martin Who cards cite it. The row needs a rescore.
- **Open rule, carried from era 3 (TOL-6).** Whether witnesses who were not present go on the Who click. Bede (WHO, `bede-of-jarrow`) is a main witness for the Lateran and is not listed, while Theodore of Tarsus and Wilfrid are listed as "Not present". Michael the Syrian is proposed as an era 5 major in the rescore (`Rescore.md` l.85) and is unscored for now. The rule should be settled once for all eras.
- **Census.** Both entries log that the census has no Roman tradition entry between 604 and 1049, so the convening church of 649 and Agatho's and Leo II's church have no tradition id. This belongs in Open-Gaps if it is not there already.

## Counts

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| lateran-council-649 | 0 | 1 | 10 |
| third-council-of-constantinople-680 | 0 | 1 | 8 |
| **Total** | **0** | **2** | **18** |

Round 2 should be a targeted recheck of LAT-1 and CP3-1 and of any minor fix taken. Both briefs must be rescored after their fixes, since both sit at the word cap.

---

# Part B


**Scope.** Two major-council profiles in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era4/`: `synod-of-whitby-664` and `quinisext-council-692`. For each: the brief, the entry, the audio script and that id's part of `records.json`.

**Standard.** `Council_Profile_Pattern.md` (C1 to C8) with `Who_Profile_Pattern.md` checklist items 1 to 9, 11 and 13. Form: the approved era 3 profiles (`era3/third-council-of-toledo-589`), and the TOL-6 rule for the Who click set in `2026-11-14_council-profiles-era3/R1_changes.md` (those who took part, those condemned, and those who acted on the council's decisions; writers who only report go in `record` and `sources`).

**Method.**
- Every quotation in both briefs and entries was found in its vendored file under `cic/texts/` and read in context for speaker, side and meaning (OCR-, long-s- and hyphen-tolerant). Every file:line cited in `records.json` for these two ids was opened.
- Every factual sentence of both briefs was checked against the held lines. Every "only", "no held source", "not held" and "is known" was searched for counter-evidence across `cic/texts/`: for Whitby, Columbanus, Cummian (Segienus, Beccanus), Adomnán's Life of Columba, the Annals of Ulster and Tigernach, the Anglo-Saxon Chronicle, Eadmer, Fridegod and the later Lives in Raine, and every file naming Whitby or Streaneshalch; for the Quinisext, every Armenian-related file (Chamich, Issaverdens x2, Langlois, Ormanian, the RHC Armenian volumes, Conybeare's Rituale, Serpos x4, Sebeos, Stephen of Taron in German and French) for Trullo, Quinisext, 692 and the sixth council, and Mansi's own preface and subscriptions.
- People verdicts against the era 3 and era 4 Who scans, the supplement, the dedupe list and the eras 4-5 rescore; ids against the Who-profile cards and the census. Tradition ids, names and dates against the census, with every census row whose dates cover 664 and 692 listed.
- Readability with `engine.m1.gates.grade_text`; sentences split and counted; each audio compared by script with its brief plus `[calmly] ` at the start and `[warmly] ` before the last paragraph.
- No model calls, network calls or paid services. No profile file was edited.

**Result in one line.** Both pass the gates and every quotation is verbatim; no finding is blocking. Each has a false absence that needs fixing before it is approved to proceed (Columbanus's Easter letters for Whitby; Serpos's answer to the canons for the Quinisext), and the Quinisext brief closes on a contested claim with only one side.

## Per-council table

| Council | Words | FK | FRE | Audio = brief | Verdict |
|---|---|---|---|---|---|
| synod-of-whitby-664 | 395 | 6.22 | 75.53 | yes | PASS WITH FIXES |
| quinisext-council-692 | 399 | 7.55 | 63.13 | yes | PASS WITH FIXES |

Each audio script equals its brief with the two tags and no others. No brief sentence runs past 25 words: Whitby's longest is the 25-word close, which is mostly Bede's quotation; the Quinisext's is 23. Both briefs are within 5 words of the 400-word cap, so every fix that adds words below names what to cut, and both need a rescore. Whitby sits at FK 6.2, under the grade 8 floor the standard calls worth staying above. That is not a fail and must not be padded, but the fixes below should not make it choppier.

## Quotations

All verbatim, speaker right:
- Whitby brief: "thought nothing better than what they taught" (`bede_ecclesiastical-history-english-people_giles1903.txt` l.7927-7928); "accomplices in obstinacy" (l.8018); "It is true, O king!" and "None." (l.8197-8200); "is the door-keeper, whom I will not contradict" (l.8205-8206); "was to serve God, not the world — to feed the soul, and not the belly" (l.8292-8297, across the page break). Entry: "it was agreed, that a synod should be held" (l.7957-7958); "a most careful interpreter for both parties" (l.7969-7970); "all present, both great and small" (l.8215); "to consult with his people what was to be done in this case" (l.8232-8233); "for the king much loved Bishop Colman on account of his singular discretion" (l.8266-8267); "such as would not comply with the Catholic Easter and the tonsure" (l.8229-8230).
- Quinisext brief: "they offer wine only on the Holy Table" (canon 32, `npnf214_seven-ecumenical-councils.xml` l.28132-28133); "equal privileges with the see of Old Rome" (canon 36, l.28311-28312); "And let no one doubt concerning them" (Tarasius, l.39056). Entry: "valid and firm" (the Ancient Epitome of canon 13, l.27508); "with wine mixed with water" (l.28171); "bishops or representatives of bishops" (l.26445-26446); "in the region of Armenia" (l.28132); "humana fragilitate timidus" (`liber-pontificalis_…duchesne1886.txt` l.174585), with its English gloss outside the marks, which is the right form.

---

## synod-of-whitby-664

**WHI-1. Substantial (false absence; C3; item 1).** `records.json`, `absent_details[3]`: "Cummian's and Columbanus's Easter letters, the Annals of Ulster and the Anglo-Saxon Chronicle are not held." Columbanus's Easter letters are held, in Latin, in `paulus-emeritanus-braulio-sisebut-pl80-lat_migne1863.txt` (the file's header names only the Spanish texts, but PL 80 also prints "SANCTI COLUMBANI ABBATIS ET CONFESSORIS EPISTOLAE", l.20270-20280). Letter I, to Gregory the Great, opens on the question "de Pascha" and argues from Anatolius against Victorius (l.20279-20483). Letter II, to a synod of Gallic bishops, says he trusts "traditioni patriae meae juxta doctrinam et calculum lxxxiv annorum et Anatolium ... quam juxta Victorium" (l.20791-20796), and asks to be left in peace "in his silvis" by the bones of his brothers (l.20758-20760). That is the Irish Easter case in an Irish writer's own words, about sixty years before Whitby. It is the same case Colman makes in Bede, who has him appeal to Anatolius and to Columba (`giles1903` l.8117-8124). Columbanus is a census person (`columbanus`, 543-615) and a WHO in the era 3 scan (l.94). Cummian's letter is indeed not held (only cited in Harnack and Williams). The brief's "The Irish side reaches us only through these two" is true of the meeting itself and can stand. The entry's `uncertain[0]` ("the Irish case reaches us only as they report it") is true only of the case made at Whitby, and the absent detail is false.
Fix: in `absent_details[3]`, drop Columbanus and say his Easter letters are held in PL 80. In the entry, add to `issue` a line such as: "The Irish case in its own words is older than the synod. Columbanus, an Irish abbot in Gaul, wrote to Pope Gregory the Great and to a synod of Gallic bishops that he trusted the Easter reckoning of his homeland and Anatolius over Victorius (Patrologia Latina 80)." None of the pattern's four witness kinds fits a writer who was not there and wrote before the meeting. Either list him in `issue` and `sources` only, with a claim in `records.json`, or add him to `record` with a note that he is an earlier Irish witness to the Easter case, not to the synod, and log the kind as a pattern gap. Reword `uncertain[0]`: "the Irish case at the synod reaches us only as they report it". The brief need not change; if the drafter adds a line, it goes in paragraph 3 and costs a cut elsewhere.

**WHI-2. Minor (item 8; common names).** Brief paragraph 3: "Stephen, a priest of Wilfrid's circle". This is the brief's first mention of Wilfrid, with no place. The tree has two Wilfrids of York; the approved Hild brief and the Decision-Log entry for era 4 batch 3 fix this man as "Wilfrid of Ripon" (`Decision-Log.md` l.2939; `Who-Profiles/era4/batch1/hild-of-whitby.brief.txt` paragraph 5), and this entry's `people` uses that name. The entry `teaser` ("the priest Wilfrid") and `knownFor` (no Wilfrid) are separate texts; the teaser's first mention also lacks the place. Fix: brief, "Stephen, a priest close to Wilfrid of Ripon," (+2 words). Teaser: "the priest Wilfrid of Ripon".

**WHI-3. Minor (item 8; item 4, no statement without context).** Brief paragraph 11 brings in Columba ("Could he show such power given to Columba?") and paragraph 13 brings in Aidan ("taking part of Aidan's bones") with nothing to tell the listener who either was. Columbanus and Columba are a known namesake trap (era 3 scan l.247). Bede gives what is needed: Colman's "our most reverend Father Columba and his successors" kept this Easter (l.8117-8124); Iona is the island "whence he had been sent" (l.9202); Aidan was the first of the three Irish bishops, "Aidan was bishop seventeen years, Finan ten, and Colman three" (l.8240-8241). Fix: "such power given to Columba, the founder of Iona" (+4); "taking part of the bones of Aidan, Lindisfarne's first Irish bishop," (+4).

**WHI-4. Minor (items 1, 9).** Brief paragraph 1: "Easter was sometimes kept twice in one year." Bede: "Thus it is said to have happened in those times that Easter was twice kept in one year" (l.7895-7897). The brief drops "it is said" and makes it a recurring event; the entry `issue[0]` and the records say "once". Fix: "At the court of King Oswy of Northumbria, it was said, Easter was once kept twice in one year." (+3). Or keep the sentence and change "sometimes" to "once", and make the next "Bede of Jarrow says it was told that the king had kept the feast".

**WHI-5. Minor (item 1).** Two small additions to Bede:
- Paragraph 1: "Oswy had been taught and baptized by the Irish monks, whom Bede calls the Scots". Bede: "having been instructed and baptized by the Scots" (l.7925-7926). "Monks" is not his. Fix: "by the Irish, whom Bede calls the Scots" (-1).
- Paragraph 5: "the tonsure, the way a monk's head was shaved". The tonsure in dispute is "the ecclesiastical tonsure" of clergy (l.7937, 8247); Mansi's heading has "de tonsura sacerdotum" (`mansi…tomus-11` l.7659). Fix: "the way a cleric's head was shaved".

**WHI-6. Minor (item 4; heard aloud).** Brief paragraph 11: "The king asked Colman whether the keys of heaven were given to Peter. "It is true, O king!" Could he show such power given to Columba? "None."" Heard aloud, the two quotations have no speaker, and "Could he show such power given to Columba?" sounds like the narrator asking a question. Fix: "The king asked Colman whether the keys of heaven were given to Peter. "It is true, O king!" Colman said. Asked if he could show such power given to Columba, he answered, "None."" (+4). With WHI-3, give Columba's identifier here.

**WHI-7. Minor (C2; item 4).** Brief paragraph 3: "No record of the meeting survives." The next two sentences name two records of it, Bede's and Stephen's. The entry's absent detail is "Acts, canons or a list of those present". Fix: "No acts of the meeting survive." (0 words).

**WHI-8. Minor (item 1; a false "only").** Entry `issue[4]`: "Stephen names only the two bishops, Colman and Agilbert, and Hild as present." `attended[1]`: "Stephen names the two kings, Hild, and the bishops Colman and Agilbert, with abbots, priests and all the ranks of the church." Stephen also names "Agathone presbytero" and "Sancto Wilfritho presbytero et abbati" (`byrhtferth_vita-s-oswaldi-in-historians-of-the-church-of-york-v1-lat_raine1879.txt` l.5138-5140), and the kings as "Oswiu et Alchfritho filio ejus" (l.5075). Fix: `issue[4]`: "Stephen names on the Roman side Agilbert, the priest Agatho and Wilfrid, and on the other Colman; he names Hild only as present." `attended[1]`: add "the priest Agatho and Wilfrid". Extend the records claim and its lines.

**WHI-9. Minor (item 7; item 4).** Entry `uncertain[1]`: "Stephen's Wilfrid argues from the 318 fathers of the Council of Nicaea and the nineteen-year cycle, not from Peter". `contested_claims[0]` gives Stephen's side the same way. Stephen's Wilfrid also says "Hec ratio discipline Apostolice sedis est, et pene totius mundi" (Raine l.5149), so the two accounts share the appeal to Rome and the whole world; they differ on Peter and Nicaea. This is the fault A-M18 found in the Wilfrid of Ripon card (batch 3 R1). "Not from Peter" is also an "X, not Y" contrast in participant text. Fix: "Stephen's Wilfrid argues from the 318 fathers of Nicaea and their nineteen-year cycle, and from the practice of the apostolic see and nearly the whole world. In Stephen it is the king who raises Peter." Add l.5149 to the contested claim.

**WHI-10. Minor (item 1; a false "only").** Entry `record`, Bede: "The fullest account and the only one with the long speeches, Cedd's interpreting and the year". Eadmer's Life retells the speeches, with "rex Oswius ... locutus" (Raine l.15948-15949), and the later Vita S. Wilfridi in the same volume (from l.34853) gives the year, "anno Domini sexcentesimo sexagesimo quarto" (l.35930), both from Bede. Fix: "the only independent one with the long speeches, Cedd's interpreting and the year; later Lives copy these from him."

**WHI-11. Minor (C7; item 8).** Entry `people`:
- Agatho, James the Deacon and Romanus took part, by Bede's account (l.7962-7966) and Mansi's heading (l.7656-7657), and are in the era 4 scan's Whitby row as "not scored" (`Who_Scan_Era4.md` l.199). They are missing. Fix: add each as NOT SCORED with their part ("priest with Agilbert, on the Roman side"; "deacon of Paulinus, kept the Roman Easter, on the Roman side"; "Queen Eanfleda's Kentish priest, on the Roman side").
- Aidan "Long dead" neither took part nor acted on the decisions, so he is off the click under the TOL-6 rule the era 3 councils adopted. Either remove him or log why the rule is set aside here.
- "Alfrid of Northumbria" is ambiguous. Giles's Bede uses "Alfrid" for Aldfrith too ("Alfrid, king of the English", l.13553), and the approved Wilfrid of Ripon card writes "Alfrid of the Deiri and Bernicians" for that later king. Fix: "Alfrid, son of Oswy".

**WHI-12. Minor (item 1; optional).** Entry `issue[1]`: "Stephen frames the question the same way, with a variant reading in one manuscript". Stephen frames it as Easter "more Brittonum et Scottorum, omnisque Aquilonalis partis" against "ratione sedis Apostolice" (Raine l.5089-5094). In manuscript A the Irish range runs to the twenty-second moon, against Bede's twentieth (the bracket and note 6, l.5091-5093, 5112-5121). Fix: "Stephen sets the custom of the Britons, the Scots and the whole north against that of the apostolic see; one manuscript runs the Irish range to the twenty-second moon."

**Word budget for Whitby.** WHI-2, -3, -4, -5 and -6 add about 16 words, to about 411. Suggested cuts: paragraph 9, "where Peter and Paul were buried" (-6); paragraph 13, "Cedd took the Roman Easter." (-5; it is in the entry and in the Cedd and Chad profile); paragraph 7, "a Frank and" (-3). Rescore after.

## quinisext-council-692

**QUI-1. Substantial (false absence; C3; items 1, 6).** Brief paragraph 13: "No Armenian answer to the council is known." Entry `issue[3]`: "no held Armenian text answers the canons"; `outcome[5]`: "No held Armenian source answers the council"; `uncertain[7]`: "no held Armenian text answers the council". The records' absent detail concedes Serpos names the council but treats it as no answer. Serpos answers it. Giovanni de Serpos, an Armenian Catholic writing to Propaganda from Venice in 1783, gives a section "Riflessioni sul Sinodo Trullano, e su ciò, che ne' suoi Atti si legge rapporto alla Nazione Armena" (`serpos_dissertazione-due-dubbi-armeni-cattolici-ita_1783.txt` l.1027-1029). He calls it a council "congregato in Costantinopoli da' Greci senza veruna autorità, non avendovi prestato il suo consenso il Pontefice Romano", a "Pseudosinodo" (l.1039-1044). He then argues that its canons 32, 33, 56 and others only rebuke the Armenians and never anathematize the nation (l.1060-1080). In his Compendio he also calls some Armenian ceremonies "giustamente riprovate dal sinodo Trullano" (`serpos_compendio-storico-nazione-armena-t3-ita_1786.txt` l.519-523). He is late and writes from the Catholic side, but he is an Armenian answering the council. No Armenian writer of the time answers it in any held file (searched as listed under Method).
Fix: brief, "No Armenian answer from the time survives in the books we draw on." (+5). Entry: rewrite `issue[3]`, `outcome[5]` and `uncertain[7]` to say no Armenian answer from the time is held, and that the first held Armenian answer is Serpos's of 1783, who calls the council a false synod and says its canons rebuke the Armenians without cursing them. Add Serpos to `record` (later narrative, Armenian Catholic, hostile to the council) and `sources.writtenLater`, a claim to `records.json`, and correct the absent detail.

**QUI-2. Substantial (item 7; C5; close).** The brief closes: "At the Second Council of Nicaea in 787, Tarasius of Constantinople said the canons came from the fathers of the Sixth Council. "And let no one doubt concerning them."" The records hold this as Contested (`contested_claims[5]`), and every held witness weighs against Tarasius. Percival breaks into the very speech: "We have seen that this is an error. Vide Introduction to Trullan Canons" (`npnf214` l.39054-39055), and says "the bishops were not the same, as can readily be seen by comparing the subscriptions" (l.26420-26422). Mansi's editors' preface says only forty-three had sat at the sixth council (`mansi…tomus-11` l.89081-89085). The brief ends on one side's claim and its "let no one doubt", with no other side. Fix: give Percival's side in place, for example: "At the Second Council of Nicaea in 787, Tarasius of Constantinople said the canons came from the fathers of the Sixth Council. "And let no one doubt concerning them." Percival says the signatures show they were not the same bishops." (+11). Or, to keep the close on Tarasius, put Percival's sentence first. Either way, keep it sourced and with no summing-up.

**QUI-3. Minor (item 1).** Brief paragraph 1: "the next line is marked in Latin as the place of the most holy pope of Rome." The list is Greek; Mansi prints a Latin translation beside it. The Greek column has the same line, "Τόπος τοῦ ἁγιωτάτου πάπα Ῥώμης" (OCR "Tonos ts ayionits tare Pons", l.95170), beside "Locus sanctissimi papae Romani". The listener hears that a Constantinople council marked the pope's place in Latin. Paragraph 3's "Its record survives in Greek and Latin" has the same slant. Fix: "the next line is marked as the place of the most holy pope of Rome" (-2); "Its record survives in Greek, printed with a Latin translation" (+3), or leave paragraph 3 if the cap is tight.

**QUI-4. Minor (C4; item 5).** Brief paragraph 7: "Later Greek writers give 227 and 240." The witnesses are unnamed. The Pedalion gives 227 "κατὰ τὸν Βαλσαμῶνα καὶ Ζωναρᾶν" and 240 after "τὸν συγγραφέα τοῦ Συνοδικοῦ" (`nikodemos-hagiorite_pedalion-canons-grc_1886.txt` l.22398); Percival dates Zonaras and Balsamon "of the twelfth century" (`npnf214` l.3576). Fix: "The Greek canon lawyers Balsamon and Zonaras, of the 1100s, give 227, and a Greek list of synods gives 240." (+11). Separately, the records and `attended` leave out the one count taken from the signed list itself. Mansi's preface names eight signers after the emperor and the pope's blank, then says "Post hanc deinceps ducentorum et quinque subsunt episcoporum subscriptiones" (l.89062-89081). Add it to `attended[1]` and the count's `contested_claim`, kept apart from Percival's 211, as C4 asks.

**QUI-5. Minor (item 2; paraphrase stronger than the source).** Brief paragraph 7: "Percival says the West was not represented at all." Percival: "the West was not really represented at it at all" (l.26375-26376). His "really" allows for Basil of Gortyna's claim, which the brief has just told. Fix: "Percival says the West was not really represented at all." (+1).

**QUI-6. Minor (items 9, 4).** Paragraph 5 says "The councils of 553 and 681"; the close says "the Sixth Council". The listener is not told these are the same thing. The brief also never says what "Quinisext", the page's own title, means. Fleury, in Percival, gives it: "named in Latin Quinisextum, in Greek Penthecton, as one might say, the fifth-sixth, to mark that it is only the supplement of the two preceding Councils" (l.26400-26403). Fix: paragraph 5, "The fifth and sixth councils, of 553 and 681, had made no canons, the bishops told the emperor." (+5). Optionally, after it: "So the council was later called the Quinisext, the fifth-sixth." (+10), if the cap allows.

**QUI-7. Minor (item 1).** Brief paragraph 13: "It kept the sacrament without water." Stephen of Taron says the synod met to purge the land of the two-natures teaching and of "der Gewohnheit durch gegohrenes Brot und Wasser das heilige Sakrament zu schänden", a custom "seit den Tagen Ezrs bis dahin in Griechisch-Armenien üblich", and then required the sacrament "ohne gegohrenes Brot und ohne Wasser" (`stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt` l.3725-3735). "Kept" says it continued an unbroken practice; Stephen says it removed water where it had been used. Fix: "It required the sacrament without water." (0).

**QUI-8. Minor (item 8; namesakes across profiles).** Brief paragraph 1 and entry `people`: "Paul of Constantinople". The era 4 Lateran brief calls the Monothelete patriarch condemned in 649 and 681 "Paul, patriarch of Constantinople", so the tree would have two Pauls with the same identifier, one condemned and one signing first in 692. No held file gives a numeral. Fix: brief, "Then came Paul, bishop of Constantinople at the time, and the bishops of Alexandria, Jerusalem and Antioch" (+3), or drop Paul's name ("the bishops of Constantinople, Alexandria, Jerusalem and Antioch", -2). In `people`, "Paul of Constantinople (bishop 692)", or as the cards elsewhere distinguish him.

**QUI-9. Minor (item 7).** Entry `knownFor`: "which the East kept as church law and Rome refused". Percival says "even in the East their authority was rather theoretical than real" (l.26379-26380). The Pedalion holds the council ecumenical (l.22318-22324). Fix: "which the Greek church received as canon law, and Rome refused."

**QUI-10. Minor (C7).** Entry `people`:
- Tarasius of Constantinople is LISTED, but no Who scan scores him (searched every scan, the supplement, the dedupe list, the rescore and the census). The council profile may not make a verdict. Fix: NOT SCORED.
- Under the TOL-6 rule, those who took part or acted on the decisions are missing: Peter of Alexandria, Anastasius of Jerusalem and George of Antioch, who signed (Mansi l.95176-95187); John, bishop of Porto, and Boniface, counselor of the apostolic see, whom Justinian had taken to Constantinople (LP l.170987-170988); and Popes John VII and Constantine, to whom the volumes were later sent (LP l.174288-174291 and Constantine's life). Fix: add each as NOT SCORED with their part.

**QUI-11. Minor (register; item 4).** Entry `record[0]`: "The Greek text is poorly read in the file and the Latin is used." This is process narration in a participant-facing field (the TOL-4 fault). Fix: "The canons and signatures survive in Greek, printed with a Latin translation." Entry `traditions`, Armenian row: "Its customs, not its teachers: canon 32 …" is an "X, not Y" contrast with a colon-reveal. Fix: "Canon 32 deposes priests who, "in the region of Armenia", offer wine without water. Canons 33, 56 and 99 name other Armenian customs; none names an Armenian teacher."

**QUI-12. Minor (item 7; records).** `contested_claims[2]`, "Whether Rome was represented", leaves out the Pedalion, which says Basil of Gortyna "καί τις Ἐπίσκοπος Ῥαβέννης" held the place of Rome (l.22399-22400). Percival and Mansi's preface say Ravenna's place was left blank (l.26451-26452; Mansi l.89074-89075). Fix: add the Pedalion's side with both lines; `uncertain[3]` may stay as it is.

**Word budget for the Quinisext.** QUI-1, -2, -3, -4, -5, -6 and -8 add about 32 words, to about 431. Suggested cuts: paragraph 9, the canon 55 sentence (-8; it stays in the entry); paragraph 13, "a former Armenian patriarch of Constantinople" to "an Armenian patriarch" (-4); paragraph 7, "Basil of Gortyna in Crete signed as holding the place of the church of Rome." to "Basil of Gortyna in Crete signed in Rome's place." (-6); paragraph 3, "Charles Joseph Hefele, the historian of the councils," keep; drop "No minutes of its debates are known." (-7; it is in `uncertain[0]`); QUI-4 shortened to "Balsamon and Zonaras, Greek canon lawyers of the 1100s, give 227. A Greek list of synods gives 240." The drafter should choose, keep within 400 and rescore (FRE is 63.1).

---

## Checks that passed

- **C1.** Every `record` entry in both entries has a kind. Partisan witnesses are marked: Bede ("Openly on the Roman side"), Stephen ("writing for him"), the Book of the Popes ("from Rome's side, hostile to the council"), Justinian II ("partisan for it"), Mansi's preface and Binius ("from the Roman side"), Paul the Deacon ("Latin side"). Serpos is the gap (QUI-1).
- **C2.** Whitby says early that no acts survive and names whose accounts stand in (with WHI-7's wording). The Quinisext cites its held acts first: the signatures open the brief, then the address and canons, before any history.
- **C3.** Whitby says the Irish side of the meeting reaches us only through Bede and Stephen, both named and placed; WHI-1 is about the records. The Quinisext gives the Roman refusal through the Book of the Popes and the 1054 reply, and the Armenian custom through the canon and Stephen of Taron; QUI-1 adds the one held Armenian answer.
- **C4.** Every count and date has its witness. Whitby: no count is given, and 664 is Bede's (l.8236-8241). Quinisext: Hefele's September 691 to September 692 is his, through Percival (l.26430-26437), Fleury's and Duchesne's 692 (l.26385; LP l.172486), the Pedalion's 691 (l.22318) and Theophanes's later date with Goar's rejection (PG 108 l.65546-65553, 65636-65641) are kept apart; Percival's and Fleury's 211 are named; the Annales Cambriae years 665 and 768 are given as the editor's (l.2759-2764, 2955-2986). Gaps: QUI-4.
- **C5.** `issue`, `decided` and `outcome` are separate in both. Rome's refusal is told as refusal, with Sergius's own reason given as his biographer's ("eligens ante mori quam novitatum erroribus consentire", LP l.170979). Whitby's failure to rule on the tonsure is told as such (`decided[3]`).
- **C6.** No creed; the Quinisext's canon 1 is told as the council's confirmation of the six councils' faith, and the emperor's signature as asked for by the bishops (Mansi l.89719-89721).
- **C7.** Both have `kind` `major-council` and `kindLabel` "Major council", in the tradition-page field order of era 3. Verdicts match the scans for Hild (WHO), Wilfrid of Ripon (WHO, supplement l.187 and the batch 3 rename), Cedd and Chad (WHO, batch 7 card), Aidan (WHO), Colman (STORY, era 4 l.73), Niketas Stethatos (WHO, supplement l.199), Humbert (WHO, era 4 l.51), and NOT SCORED for Oswy, Alfrid, Agilbert, Eanfleda, Tuda, Eata, Justinian II, Sergius I, Paul, Basil and Zacharias (the era 4 scan's Whitby row and its Quinisext row, "Participants not opened"). Every id resolves to a card or census row. Every tradition id is in the census with dates that fit: `anglo-saxon-christianity` 597-793, `insular-irish-monastic-christianity` 450-664, `medieval-irish-christianity` 664-1169, `british-welsh-christianity` 451-768, `byzantine-imperial-church-heraclian-iconoclast` 622-843, `armenian-christianity-before-the-bagratids` 554-884. The Quinisext rightly leaves out the scan's `roman-church-gregorian` (560-604); no census row for Rome covers 692, as its absent detail says. Exceptions: WHI-11, QUI-10.
- **C8 and item 11.** Both within 400 words, both pass `grade_text`, both open on a sourced moment: the double Easter at Oswy's court (Bede l.7895-7900), and the emperor's signature with the blank place for the pope (Mansi l.95155-95170; Percival l.26442-26444).
- **Items 2, 3.** Every quotation verbatim (above). No invented scene, feeling or speech: Oswy's smile is Stephen's "subridens" (Raine l.5153); Zacharias under the bed is "sub lecto pontificis" (LP l.171268) and Paul the Deacon VI.11 (`foulke1907` l.11506-11514).
- **Item 4.** Neither brief has a narrator's "not X but Y", a tail line, an aphorism or a hedge filler; Bede's "not the world — to feed the soul, and not the belly" is a quotation. The one question-shaped sentence is WHI-6.
- **Item 5.** Every modern witness is named: Percival, Hefele, Fleury, Duchesne, Goar, Ormanian, Raine, Plummer, Binius, Mansi, Williams ab Ithel.
- **Consistency with era 4 Who profiles.** Whitby agrees with the Hild, Cedd and Chad, Cuthbert and Wilfrid of Ripon texts (Hild held with Colman in Bede; Stephen "Wilfrid's biographer"; Cedd interpreter for both; Bede's History "finished in 731", as in the Bede brief). The Quinisext agrees with the Niketas Stethatos and Humbert cards on 1054.
- **Item 13.** Tags only in the audio scripts, in the two right places.

## Notes for the coordinator (no fix to these profiles)

- **Library header.** `cic/texts/paulus-emeritanus-braulio-sisebut-pl80-lat_migne1863.txt` has a content note naming only the Mérida Lives, Sisebut and Braulio. PL 80 also holds Columbanus's works: his letters (l.20270 onward, including the two Easter letters), and the editors' notices on his Rule and Penitential (l.15946-16521). The header should say so; that file is live, so this is for the Library thread, not this thread. It is why WHI-1's false absence was easy to make.
- **Tarasius's verdict.** `second-council-of-nicaea-787.entry.json` also gives Tarasius LISTED ("Patriarch; asked for the council and led it") with no scan behind it. That is outside part B; the part A reviewer or a scan should settle it once for both entries.
- **Stale scan rows.** `2026-11-12_major-events-scan/Councils_Scan.md` l.63 and `Who_Scan_Era4.md` l.199 still say "Wilfrid not scored". He is WHO, `wilfrid-of-ripon`. The Councils_Scan Quinisext row (l.65) lists `roman-church-gregorian`, which ends in 604; the entry rightly leaves it out. Both belong in an Open-Gaps entry like 246 when the era is approved.
- **Quinisext participants never scored.** The era 4 scan's Quinisext row says "Participants not opened". Justinian II, Sergius I, Paul, the three other patriarchs and Basil of Gortyna are NOT SCORED by default; Justinian II and Sergius I at least have held lines (signature, LP lives) a scan could weigh.

## Counts

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| synod-of-whitby-664 | 0 | 1 | 11 |
| quinisext-council-692 | 0 | 2 | 10 |
| **Total** | **0** | **3** | **21** |

Round 2 should be a targeted recheck of the three substantial findings and of any minor fix taken. Both briefs must be rescored after their fixes, since both sit within five words of the cap.

---

# Part C


**Scope.** Two major-council profiles in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era4/`: `second-council-of-nicaea-787` and `councils-of-constantinople-861-880`. For each: the brief, the entry, the audio script and that id's part of `records.json`.

**Standard.** `Council_Profile_Pattern.md` (C1 to C8) with `Who_Profile_Pattern.md` checklist items 1 to 9, 11 and 13. Form matched against `Council-Profiles/era3/second-council-of-constantinople-553` and the era 3 R1 review.

**Method.**
- Every quotation in both briefs and entries was searched in its vendored file under `cic/texts/`, tolerant of whitespace, hyphens, OCR and long-s. Each was read in context for who speaks and about what.
- Every file:line cited in `records.json` for a claim the briefs rest on was opened. Every factual sentence of both briefs was checked against the held lines.
- Every "only", "no" and "not held" was tested against the Library. Searches covered Mansi tomus 14, 15, 16, 17-18 and 31; the Pedalion; Duchesne's Liber Pontificalis t.1 and t.2; Theophanes (Goar and Anastasius); PG 99 and PG 100; Boretius; the Annales regni Francorum and Bertiniani; Will; Freese; and Percival's excursuses (`npnf214` l.39476-42288).
- People verdicts were checked against the era 4 Who scan, the 2026-11-14 rescore, the era 6 scan, the supplement and the dedupe list. Ids and tradition rows were checked against the census copy in the scratchpad. The Photius Who profile (`Who-Profiles/era4/batch2/photius-of-constantinople.*`) was read for contradictions.
- Readability was scored with `engine.m1.gates.grade_text`. Sentences were split and counted.
- No model calls, no network, no paid services. No profile file was edited.

**Result in one line.** Both pass the gates, and every quotation is verbatim, with the right speaker. Nicaea has minor findings only. Constantinople has one substantial finding: a false absence on the council of 861, whose canons are held, and which the brief says reaches us only through Photius's enemies.

## Per-council table

| Council | Words | FK | FRE | Audio = brief + two tags | Verdict |
|---|---|---|---|---|---|
| second-council-of-nicaea-787 | 399 | 7.41 | 64.35 | yes | PASS |
| councils-of-constantinople-861-880 | 400 | 7.99 | 61.81 | yes | PASS WITH FIXES |

The two audio scripts differ from their briefs only by `[calmly] ` at the start and `[warmly] ` before the last paragraph. No sentence runs past 25 words. Each brief has three 25-word sentences at most (Nicaea's close; Constantinople's second sentence and its last). Both briefs are at the 400-word cap, so any fix that adds words needs a cut and a rescore.

## Quotations

Every quoted string in the two briefs is verbatim in its file, and the speaker is right:
- Nicaea:
  - Hefele's epitome of the Hieria decree, as Percival gives it: "either depicts the Godhead which cannot be depicted" (`npnf214_seven-ecumenical-councils.xml` l.39300-39301) and "is bread and wine in the holy Supper" (l.39305).
  - The emperors' Sacra: "decline communion with us" (l.38488-38489). Tarasius in Session IV: "Shall we not weep …" (l.39027-39028).
  - The decree: "honourable reverence" (l.39745) and "For the honour which is paid …" (l.39749-39750).
  - Photius, Library codex 20: "at the sessions of which …" (`photius_library-v1_freese1920.txt` l.2236-2238). Freese's note identifies the council as the second of Nicaea (l.2266).
- Constantinople: the brief quotes nothing. Its two paraphrased lists are right. The pledges from "pellarios, & pisces vendentes, & lignarios, & acus facientes" are at `mansi…tomus-16…txt` l.14211-14213. Mark of Ephesus's anathema reads "Omnibus quae adversus sanctos patriarchas, Photium & Ignatium, scripta vel dicta sunt, anathema" (`mansi…tomus-31…txt` l.53796-53799). Both are told in modern words, without quotation marks. The speaker at Florence is Mark, "Ὁ Ἐφέσου … ἀπεκρινάμην τότε, τοῦτο καὶ νῦν λέγω" (l.53614).

The entries' quotations are verbatim too. The one exception is PHO-11, an English rendering of Latin set in quotation marks.

---

## second-council-of-nicaea-787

**NIC-1. Minor (item 1).** Brief: "The only true image of his humanity 'is bread and wine in the holy Supper.'" The held text reads "The only admissible figure of the humanity of Christ, however, is bread and wine" (`npnf214` l.39304-39305). "True" is the narrator's word, and the epitome does not use it (searched). Fix: "The only fit image of his humanity, it says, 'is bread and wine in the holy Supper.'"

**NIC-2. Minor (C5; close).** The brief's outcome stops at Frankfurt and Photius's praise. It never says that the ban came back. Percival records that "several iconoclastic rulers sat on the throne of the East" after Irene died (`npnf214` l.41520-41523). The Life of Methodius places the council's "firmam … auctoritatem" in 843 (`nikephoros-cp…pg100…txt` l.103894-103899). The entry's `outcome[4]` carries both. Heard alone, Photius's "the iconoclasts were defeated" can sound like a final victory in 787. Fix (optional, mind the cap): add "Iconoclast emperors returned after Irene. Only in 843, his Life says, under the patriarch Methodius, did the council gain firm authority." Cut "Bishops of the soldiers' party went out to them, shouting that they had won." (14 words) to make room.

**NIC-3. Minor (C7).** `people` lists Photius ("Not present") and Alcuin ("Not at Nicaea"), but leaves out two named witnesses who have WHO verdicts:
- Theophanes the Confessor, WHO (recorder). See `2026-11-14_who-rescore-eras4-5/Rescore.md` l.155 and `Opus_Check_Notes.md` l.752. He is the brief's opening witness.
- Theodore the Studite, WHO (`Opus_Check_Notes.md` l.739). The entry quotes him in `attended[2]` and `uncertain[3]`, and his uncle Plato attended (`theodore-studite…pg99…txt` l.8835-8836).

Neither has a census id, so they go in without one. Fix: add both, with "Not present" or "witness" parts, as the era 3 Constantinople entry does for Gregory and Victor.

**NIC-4. Minor (records; false absence).** `absent_details[2]`: "Theophanes gives only the indiction." Theophanes also gives the rulers' year: "Anno imperii sui sexto" (`theophanes…pg108…txt` l.123631). Goar's heading gives "A. C. 778 … A. M. 6278" (l.83374). Neither is an anno Domini date, so the honest limit stands. Its wording is wrong. Fix: "Theophanes dates it by the world-year 6278, the rulers' sixth year and the ninth indiction, not by anno Domini."

**NIC-5. Minor (item 7; records and `uncertain[2]`).** The contested claim on session dates says "No held act gives a session date". It sets Theophanes against Duchesne. Two more held witnesses belong on it:
- The PG 99 editor's note gives a third start date: "Coepta ea synodus 8 Kalend. Octobr., indict. 11, anno 787" (24 September; `theodore-studite…pg99…txt` l.69540-69541).
- W. M. Sinclair, whom Percival quotes, gives "seven sittings" (`npnf214` l.39596-39597), against Duchesne's eight.

Fix: add both to `contested_claims[1]` and to `uncertain[2]`. The brief need not change.

**NIC-6. Minor (items 1, 5).** `uncertain[4]`: "Hefele and Boretius say the Franks judged wrongly". Boretius's note cites Hefele for it: "non recte iudicavit … Hefele, Conciliengeschichte III. p. 705" (`capitulatio-de-partibus-saxoniae_pertz1881.txt` l.5680-5682). These are one witness, not two. Fix: "Hefele, followed by Boretius, says …". Change `contested_claims[3]` to match.

**NIC-7. Minor (C1).**
- `record[5]` puts "the Frankish royal annals" under kind "acts" with the Frankfurt capitulary. The annals are a later narrative (`annales-regni-francorum_kurze1895.txt` l.6594-6598). Fix: give them their own row, kind "later narrative", Frankish.
- `record[8]`, the Life of Methodius, has no side. Fix: "for the images".

**NIC-8. Minor (register; era 3 TOL-4 and DVN-6).** Entry fields shown on the page use project words and process narration:
- `issue[0]`, "is held as Percival's English summary";
- `attended[1]`, "No list of signatures is held";
- `record[0]`, "The full acts … are not held";
- `record[6]`, "neither held";
- `uncertain[0]`, "are not held; the profile rests on";
- `uncertain[5]`, "The books are not held".

Fix: "survives here only in", "No list of signatures is given in the extracts", "The full acts, in Mansi, are not among our sources", "this profile draws on" becomes "we draw on", and so on.

**NIC-9. Minor (item 7; `calledBy`).** "Tarasius led the council." Percival's note on Gibbon's "the president Tarasius" reads: "Who was possibly at least not the president, vide Michaud" (`npnf214` l.37901-37902). The brief does not say who presided, so it is unaffected. Fix: "Tarasius led the council, though Percival, after Michaud, doubts that he presided."

## councils-of-constantinople-861-880

**PHO-1. Substantial (false absence; C2, C3; items 1, 6).** Brief paragraph 2: "The councils of 861 and 867 have no surviving acts, and those of 867 were burned by order. They reach us through Photius's enemies, Nicetas … and Anastasius the Librarian". Entry `uncertain[0]` and `absent_details[0]` say the same ("The acts of 861: Not held"). The Library holds otherwise:
- **The canons of 861 are held.** The Pedalion says of the "First and Second" council in the Holy Apostles, "ἐν ἔτει 861" (`nikodemos-hagiorite_pedalion-canons-grc_1886.txt` l.33222-33224): "Ἐν δὲ τῇ Β΄. αὐτῆς συνελεύσει ἐξεδόθησαν καὶ οἱ παρόντες ιζ’. κανόνες". That is, in its second meeting the seventeen canons printed here were issued (l.33300). They follow with commentary (from l.33330). The pattern counts canons as acts. What the Pedalion says is lost is the minutes: "ταύτης οὐχ εὑρίσκονται πρακτικά" (l.33335-33336).
- **A Latin record existed.** Duchesne, in a note on the Life of Nicholas, says a slightly shortened Latin version of the synod held with Radoald and Zacharias is in Cardinal Deusdedit's collection. It came from the papal archives, and the Roman biographer had it in front of him (`liber-pontificalis…t2…duchesne1892.txt` l.51685-51693). `absent_details[0]` names Deusdedit, so this point is half-known to the draft. The brief still says "no surviving acts".
- **Not only enemies.** The Pedalion is an Orthodox witness. It calls Photius "τὸν σοφώτατον … Φώτιον" (l.33257-33260). It says this synod "οὐδὲν εἶπε κατὰ Φωτίου" (l.33345), and that it was confirmed by the council of 879 (l.33340-33341) and by Photius's own Nomocanon (l.33348-33349). It also gives another purpose for Nicholas's envoys, "ἀποσταλέντες κατὰ τῶν εἰκονομάχων", sent against the iconoclasts (l.33227-33228). The Book of the Popes says they were sent to inquire into Ignatius's removal (l.49600-49604). The brief tells only the second, without a witness ("Pope Nicholas sent two envoys to look into it").

Fix:
- Brief, paragraph 2: "The acts of 867 were burned by order. The canons of 861 survive in the Pedalion, a Greek book of church law. Its story reaches us mainly through Photius's enemies, Nicetas the Paphlagonian, who wrote the Life of his rival Ignatius, and Anastasius the Librarian, Rome's translator." Then shorten paragraph 7's first mention to "says the Pedalion". The new paragraph is about six words longer, so cut "down to leather-workers, fishmongers and needle-makers" to "down to fishmongers and needle-makers" and drop "over Rome's protest" or similar. Rescore.
- Paragraph 3: "Pope Nicholas sent two envoys to look into it, the Book of the Popes says."
- Entry: list the seventeen canons under `decided` for 861 and the Pedalion under `sources.fromTheCouncil`. Rewrite `uncertain[0]` and `absent_details[0]` as "the minutes of 861 are lost; its canons survive; a shortened Latin version, in Deusdedit's collection, is not among our sources".
- Records: add a contested claim on the envoys' purpose (the Book of the Popes against the Pedalion). Mark the Pedalion's side in `record` as Orthodox and favourable to Photius.

**PHO-2. Minor (items 1, 7).** Brief: "In 869 it declared that Photius had never been a bishop, and restored Ignatius." Entry `decided[2]` and `outcome[1]` say the same. The Book of the Popes says Basil put Photius out and himself restored Ignatius to the patriarch's palace, before the council: "pervasorem Photium pepulit et Ignatium patriarcham … patriarchio restituit" (`liber-pontificalis…t2…txt` l.53408-53409). Ignatius sits as patriarch in the council's sessions (`mansi…tomus-16…txt` l.36862). The council confirmed the popes' definitions "pro … restitutione Ignatii" (l.16882-16886). Hincmar does write "Ignatium restituentes" of the council (`prudentius-troyes_annales-bertiniani_waitz1883.txt` l.7148), so the brief is not without a witness. But it tells as settled what the Book of the Popes and the acts place earlier. Fix: "In 869 it declared that Photius had never been a bishop, and confirmed Ignatius, whom Basil had put back." The fix adds two words. In the entry, credit "restored" to Hincmar and add the Book of the Popes.

**PHO-3. Minor (item 7; C6).** Brief: "The council kept the creed with nothing added and nothing taken away." This is told flat. `contested_claims[4]` holds as Contested whether the session that made the definition is genuine. A note printed in Mansi says Photius invented it: "extremas duas istas Actiones suo Marte finxit" (`mansi…tomus-17-18…txt` l.52604-52624). The Photius Who profile tells the doubt. Fix: "Its acts say the council kept the creed …" (+3 words; see PHO-1 for cuts).

**PHO-4. Minor (item 8).** Brief paragraph 2: "Nicetas, who wrote the Life of his rival Ignatius". "Nicetas" is a common name, and here it has no identifier. The Photius Who profile and the entry's `record` use "Nicetas the Paphlagonian". Fix: as in PHO-1.

**PHO-5. Minor (items 1, 9).** Brief: "Photius wrote to the bishops of the East". Will says the encyclical went "ad eos qui archiepiscopales thronos per Orientem obtinebant, i. e. Alexandrinum et caeteros" (`will_acta-et-scripta…1861.txt` l.3443-3444). The entry's `issue[2]` and the Photius Who profile say "the Eastern patriarchs", and the brief itself later says "the envoys of the Eastern patriarchs". Fix: "Photius wrote to the patriarchs of the East".

**PHO-6. Minor (ambiguous pronoun).** Brief: "He was stripped of his robe, and the pope's envoys joined the cry that he was unworthy. In Rome, Nicholas condemned them." Heard aloud, "them" can reach back to the seventy-two false witnesses. The Book of the Popes has Zacharias deposed and Radoald's case held over, then condemned later (`liber-pontificalis…t2…txt` l.49826-49835). Fix: "In Rome, Nicholas condemned his envoys."

**PHO-7. Minor (item 4, colon-reveal).** Brief close: "In the great church of Constantinople, he said, this was still read: anathema to all written or said against the holy patriarchs Photius and Ignatius." Fix: "In the great church of Constantinople, he said, an anathema was still read on all written or said against the holy patriarchs Photius and Ignatius."

**PHO-8. Minor (pattern 1, "later narrative … when"; item 1).** Brief: "The Latins, says the Pedalion, a Greek book of church law, named the council against Photius the eighth." The Pedalion is placed beside Mark of Ephesus and reads as an old witness. It was first printed at Leipzig in 1800 (file header l.2), and the entry's `record` rightly classes it as modern reconstruction. Fix: "a Greek book of church law of 1800". If PHO-1 brings the Pedalion into paragraph 2, date it there.

Optional: Mark spoke in Session VI on 20 October 1438 (`mansi…tomus-31…txt` l.53568-53569), while the council still sat at Ferrara. Percival also writes "the Council of Florence (1438)" (`npnf214` l.42261-42262), so the common name is defensible. "At the council of Ferrara and Florence, in 1438" would be exact.

**PHO-9. Minor (C7; verdict to confirm, not to make).**
- Mark of Ephesus, the brief's closing witness, is WHO in the era 6 scan (`2026-11-12_who-scan-era6/Who_Scan_Era6.md` l.119). He is not in `people`, while Hincmar is listed as "Not present". Fix: add him without an id ("Not present; at Ferrara-Florence in 1438 held the council of 879 to have undone that of 869").
- Ignatius is NOT SCORED in the entry. The era 4 scan's council row reads "Photius (WHO), Ignatius, Boris (LISTED)" (`2026-11-11_who-scan-era4/Who_Scan_Era4.md` l.224), which can be read as LISTED for both. No Ignatius person row exists. Fix: leave NOT SCORED unless the coordinator reads the row as LISTED (see Notes).

**PHO-10. Minor (records).** `contested_claims[6]` and `datesNote`: "Pagi: May 861 … No ancient held witness." Pagi argues from Nicetas. Nicetas says that after the synod, as Pentecost came round, Ignatius was besieged and fled. Pagi sets Pentecost 861 on 25 May, and he also cites the author of the Libellus synodicus, "qui hoc tempore vivebat", for "post Pascha anni Chr. 861" (`mansi…tomus-15…txt` l.63995-64010). Nicetas therefore gives the anchor, and Pagi supplies the year's calendar. Fix: "Pagi, reckoning from Nicetas's Pentecost and the Libellus synodicus, puts it in May 861."

**PHO-11. Minor (item 2; the TOL-1 fault).** `attended[0]`: 'Severinus Binius … gives 318 schismatic bishops, "as they boasted"'. This is an English rendering of "ut ipsi jactabant" (`mansi…tomus-15…txt` l.63849) set in quotation marks. `uncertain[1]` and `contested_claims[0]` give "who says they boasted it" and 'as they boasted' the same way. Fix: drop the marks, or quote "ut ipsi jactabant" with the gloss outside them.

**PHO-12. Minor (register; era 3 TOL-4).** Participant-facing entry fields narrate process or use project words:
- `attended[2]`, "A list of signatures is held; no count of it was made for this profile";
- `attended[3]`, "The first session's list is held and was not counted";
- `attended[0]` and `[1]`, "No list is held";
- `outcome[3]` and `uncertain[4]`, "No letter of John himself saying so is held";
- `uncertain[0]`, "no held acts".

Fix, for example: "The acts end with a list of signatures. Binius counts 101." "No list of names survives." "No letter of John's own saying so survives in our sources."

**PHO-13. Minor (entry field).** `informalName`: "The Photian councils". The held use is the hostile Latin label for 879 alone: "Pseudo-Synodus Photiana" (`mansi…tomus-17-18…txt` l.383) and "pseudosynodus Photiana" (Will l.16714). Neither names the four councils together. Fix: leave the field out, or give "The Photian synod (the Latin name for 879)".

---

## Checks that passed

- **C1.** Every `record` row in both entries has a kind. Partisans are marked: Percival ("argues for it"), Theophanes, Irene and Constantine VI, Frankfurt, Nicetas, Anastasius, Metrophanes, Binius and Pagi, and Nilus. The gaps are in NIC-7 and PHO-1 (the Pedalion's side).
- **C2.**
  - Nicaea names its held acts (Percival's extracts) as the winners' record, and says the Hieria decree survives inside them. Hefele's "We have no complete Acts of this assembly, but its very verbose ὅρος … is preserved among the acts of the Seventh" (`npnf214` l.39524-39527) supports "survives only in".
  - Constantinople says early which acts are held and which are lost, with the error in PHO-1.
- **C3.**
  - Nicaea gives the condemned council's case in its own decree, through Hefele's epitome, and says it reaches us inside its opponents' acts.
  - Constantinople gives Photius's own case in his encyclical (Will l.3478-3483, 3808-3812).
- **C4.**
  - Every count is credited: about 350 (`liber-pontificalis…t1…txt` l.204382-204383; PG 99 l.8834-8835); 338 at Hieria (`npnf214` l.39245; Theophanes l.77050-77052); 318 for 861 (Binius, with "ut ipsi jactabant"); about a thousand forged signatures, with twenty-one real (Anastasius, `mansi…tomus-16…txt` l.1210-1214); 102 (Nicetas, l.26091-26092); and 383 and 380 for 879.
  - Modern dates are named: Duchesne's 25 September to 22 October (`…t1…txt` l.207926-207928), Pagi's May 861 and Will's 891. Theophanes's "quinto Idus Octobrias indictionis undecime" (l.123694-123696) converts to 11 October 787 and needs no modern name. The acts' "Nonis Novembribus" in Basil's third year (`mansi…tomus-16…txt` l.14040-14043) converts to November 869.
- **C5.** Issue, decided and outcome are separate in both entries. Refusals are told as such: Frankfurt and Paris 825 for Nicaea, and Nicholas against his envoys and the rival reckonings of "the eighth" for Constantinople.
- **C6.** The Nicaea decree is told as the council's act, with the emperor's and Irene's signatures at the Magnaura (Theophanes l.123697-123700). Constantinople's creed definition is told as the act of 879, with the caveat in PHO-3.
- **C7.** Both entries have `kind` `major-council` and `kindLabel` "Major council".
  - The verdicts match the scans: Tarasius and Irene LISTED (Era4 l.153-154); Constantine V LISTED (l.158); Charlemagne STORY (l.76); Alcuin, Photius and Hincmar WHO; Nicholas I and Boris LISTED (l.162-163); Basil I, Hadrian II and John VIII NOT SCORED (l.259).
  - The ids `alcuin-of-york`, `photius-of-constantinople` and `hincmar-of-reims` resolve in the census. The five tradition ids are census rows with dates that fit: Heraclian and Iconoclast 622-843, Iconophile 726-843, Carolingian 751-888, Macedonian 843-1054, Cyrillo-Methodian 863-916, with Bulgaria in its region. The Nicaea and Constantinople place ids match the era 2 entries.
  - The Nicaea Alcuin line is supported: "Alcuinum qui huic synodo e Britannia legatus interfuit" (`capitulatio…txt` l.5948-5949).
- **C8 and item 11.** Both briefs are within 400 words and pass `grade_text`. Each opens on a sourced moment: Theophanes's broken meeting at the Holy Apostles (Anastasius l.123638-123662; Goar l.83397-83410), and the fire of the eighth session (`mansi…tomus-16…txt` l.14204-14263, with Bahanes speaking "jubente Basilio").
- **Item 3.** No invented scene, feeling or speech. The day of the broken meeting (7 or 17 August) is not told in the brief and is held as contested in the records, which is right.
- **Item 4.** No rhetorical questions in the narrator's voice; Tarasius's question is a quotation. No tail lines, no aphorisms, no summing-up close. Nicaea's "given 'honourable reverence,' but not the true worship due to God alone" carries the decree's own distinction (l.39745-39748), so it is not a narrator's "not X but Y". The one colon-reveal is PHO-7.
- **Item 5.** Every editor is named: Percival, Hefele, Duchesne, Boretius, Binius, Pagi, Will and Freese.
- **No contradiction with the Photius Who profile.** Both texts give six days from layman to patriarch, the encyclical's charges, the council of 879 with John VIII's legates and the creed decree. Two differences are noted above: "bishops of the East" (PHO-5) and the definition told without its doubt (PHO-3).
- **Item 13.** The tags are only in the audio scripts, in the two right places.

## Notes for the coordinator (no fix to these profiles)

- **Scan correction (era 4 scan, l.224).** "Constantinople (Photian) … Not held: Mansi 16 and 17 are not in the Library (file list checked)" is wrong. `mansi_sacrorum-conciliorum-collectio-tomus-16-lat_welter-facsimile1902.txt`, `…tomus-15…` and `…tomus-17-18…` are held. The Photius Who profile already uses all three.
- **Scan ambiguity (same row).** "Ignatius, Boris (LISTED)" can be read as a LISTED verdict for Ignatius of Constantinople. No person row for him exists. A ruling is needed (see PHO-9).
- **Scan staleness (era 4 scan, l.101 and l.114).** Theodore the Studite and Theophanes the Confessor are "WANTED … Not held" there. The rescore makes both WHO, and PG 99 and PG 108 are held. Nicaea's `people` should follow the rescore (NIC-3).
- **Census note.** The `byzantine-imperial-church-macedonian` row's `sourcing` reads "conciliar records of 861/867/879-880". The records of 867 were burned (Hadrian II's letter, `mansi…tomus-16…txt` l.2370-2385). The acts of 869-870, the fullest held record, are not named. The row's sources should name 861 (canons), 869-870 and 879-880.
- **Library note.** The Pedalion holds the canons of 861 and of 879 (l.33300 ff., l.34515 ff.). It is the Orthodox canonical witness for both councils. Any later profile on these councils, or a Shared-Events record, should cite it under the council's own record.

## Counts

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| second-council-of-nicaea-787 | 0 | 0 | 9 |
| councils-of-constantinople-861-880 | 0 | 1 | 12 |
| **Total** | **0** | **1** | **21** |

Round 2 should be a targeted recheck of PHO-1, and of any minor fix taken. Both briefs must be rescored after fixes, since both sit at the 400-word cap.
