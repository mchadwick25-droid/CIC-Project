# Round 3 review: era 4 Who batch 10

Three fresh Opus reviewers that had not seen the drafting or the earlier rounds, at full effort, on 2026-11-15. Round 3 rechecked every round 2 fix, read every brief again, and read the close-out records (the two batch 10 Decision-Log entries and Open-Gaps 272) and the release 44 census. Part A found 0 blocking and 7 minor points, Part B 0 and 10, Part C 1 and 9. The one blocking point, Part C R3-B1, is an absence on Ilarion's card and records: Harasiewicz's Annales Ecclesiae Ruthenae (1862), a held file, dates Ilarion's election to 1031 (l.1672 and l.1749) and George I to 1063 (l.1749), and no card field or record gives either. No brief changes. It goes to Mark for a cap ruling.

---

## Era 4 Who batch 10, round 3 review: PART A

**Scope.** `theophanes-the-confessor`, `stephen-the-younger`, `nikephoros-of-constantinople`: every round 2 fix as new text against its source (the 581b8e13..HEAD diff of the briefs, cards, audio and records), each brief read in full as a listener would, the README sections on these three, the batch's Decision-Log entries and Open-Gaps 272 as they concern them, and the majors and river counts against release 44 (`cic-website/data/world-census.json`, `meta.release.number` 44). I edited no repo file.

**Method.** I reopened every range behind a changed sentence (`sed -n`). I checked every quoted string in the three records entries by script, whitespace- and hyphen-tolerant: all are found (one, "ergo anno 813", sits in the PG100 range the same witness also cites). I walked the whole release 44 census for "Theophan", "Nikeph", "Nicephor", "Nikifor", "Stephen the Younger", "Stephanos/Stephanus" and "Auxent", and read each hit. I scored every replacement below on a scratch copy.

**Scores now.** Theophanes 332 words, FK 7.49, Flesch 69.37. Stephen 333, FK 7.22, Flesch 66.79. Nikephoros 330, FK 8.48, Flesch 60.35. No sentence runs past 24 words. All three audio scripts equal their briefs with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. Pass.

### Round 2 fixes: applied, and right as new text?

- **R2-B1 (Theophanes, Life's hostility).** Applied. "The Life, which calls Leo the wickedest of men, gives Theophanes's answer." The line is inside the Life (running heads "THEOPHANIS VITA", l.1985, l.2184), THEOPH l.2079: "Leonem, inquam, scelestissimum hominem". The "Leo" is the Armenian, named in the sentence before. With "to Leo's offers" gone, "What I refused when young" still reads, since paragraph 4 has him give up marriage and wealth, and the Life's "rogus accendatur" (l.2347) answers threats Theophanes names himself. Right.
- **R2-M1 ("disputed").** Applied in the brief and in README l.11. Goar, l.318-319: "a Metaphraste, vel ex Baronii judicio a Theodoro Studita"; Combefis has it "ab æquali, vel suppari" (l.618). The author is disputed, and the date follows from it. Right. README l.32 was missed (R3-M1).
- **R2-M2 (Stephen, the chroniclers' charge).** Applied with "Stephen" for "he": right, since "he" would fall nearest Nikephoros. THEO l.78713-78714 "quod plerosque ad monasticam vitam esset hortatus"; PG100 l.81484-81488. "Another charge" has no first charge named in the brief (R3-M2).
- **Stephen records.** New claim 11 is verbatim at PG100 l.95739-95742 ("misit; ut secundum leges judicium / Subiret, eo quod imperatoris imaginem coulra leges / conculcasset"). The contested side added to "Why he was killed" is right.
- **R2-B2 ("another Theophanes").** Applied. PG100 l.1647 and l.1656: "Aljus ergo hic noster Theo-" … "phanes est et aliquanto junior". The card's `uncertain[0]` names him "Theophanes, a priest and abbot" and tells him apart in its last sentence. Right. Claim 34's range stops short of "junior" (R3-M5).
- **R2-B3 (Joseph's restoration).** Applied. "says Nikephoros agreed" is the Sirmond chronology's "utcumque consentiente" (PG99 l.5639, the scan "utennque"). The brief now tells no motive; the card's `uncertain[4]` gives both. Claim 21 and the contested side now cite THEO l.87280-87284, which holds "postquam ipse ut imperatoris gratiam iniret ad pristina eum munia instauraverat" (l.87282-87284). Right.
- **R2-M3 ("it felt like").** Applied. PG100 l.4612 and l.4651-4653: "Videbatur enim / sibi vir $anctus … quasi in spinas et / iribulos mannin injicere". "It seemed to him" is fairly "it felt like". Right.
- **R2-M4, R2-M5, R2-M6.** Applied. Leo is the speaker (PG100 l.5286-5288 "Orditur ergo succensus iracundia", "majestate nostra"; "loqui vos atque eum eis jubemus dispulare", l.5333-5334). Right.
- **README R2-B4, B5, M7, M8, M9.** Applied and right against release 44. The coin text: census "He asked for a coin … for insulting metal or for insulting the emperor?"; PG100 l.95534-95536 "Cum vero sanctus jam introducendus erat ad imperatorem, a pio aliquo viro nummum petiit". The John Climacus `uncertain[1]` sentence is in release 44. The range "328 to 333" is right: Nicholas 328, Ilarion 329, Keroularios 329, Nikephoros 330, Peter 330, Theophanes 332, Stephen 333.

**"Applied with change" items, judged.** R2-M2's "Stephen" for "he": right. The README R2-B4 rewrite, which avoids two "X, not Y" turns: right, and true to l.95534-95536 and l.95704/l.95722. Part C's R2-M6: the README already listed the Paulicians story, and the merged wording names its text, caveat and sources. Right against release 44 (`paulicians.documentedStories[0]` text, caveat and `sources[0].work`).

---

## theophanes-the-confessor

**Verdict: passes; two minor points (R3-M1, R3-M4).** I read the brief in full once more. Every changed sentence holds, and the unchanged ones stand as rounds 1 and 2 checked them. "kidney stones" is fair to the Life, THEOPH l.2274-2277, as the scan reads: "renum et urine difficul-/late laboraret (instrumentis … in vesicam admissis, qu lapides insi-/tos commolirent …)". George "an abbot": "Georgius abbas quondam Syncellus" (l.3731).

## stephen-the-younger

**Verdict: passes; one minor point (R3-M2).** The coin dialogue, the 754 council and Callistus, the 342 monks, the eleven months, the feast-day cry, the ropes, Philomates and the pit all stand as round 2 checked them. The partisan marker and both "of Constantinople"s are in place.

## nikephoros-of-constantinople

**Verdict: passes; one minor point (R3-M5).** The night exile reads true to PG100 l.8500-8531. The Life has "in tem-/pli maximi exaudibile catechumenium" (l.8521-8522), the gallery of the Great Church, so "the church where he often prayed all night" is fair. Joseph "illegally married" Constantine VI to Theodote follows THEO l.87776, l.87800-87801: "corollas … nuptiales Constantino et Theodote illegitime pridem jmponentem". Flesch 60.35 still just clears the floor; nothing below lowers it.

---

### R3-M1. README "Who the sources are", Theophanes: "open" left behind (README l.32)

- Round 2 changed "open" to "disputed" in the brief and in README l.11, so that the Decision-Log, the brief and the README agree. README l.32 still reads "His life rests on a Life and Eulogy whose author and date are open."
- Source: THEOPH l.318-319, "Vitæ Theophanis a Metaphraste, vel ex Baronii judicio a Theodoro Studita conscriptæ".
- Fix: "whose author and date are open." → "whose author and date are disputed."

### R3-M2. Stephen brief para 7: "another charge" has no first charge ("Two chroniclers name another charge.")

- The brief never calls anything a charge before this sentence. A listener has to infer the first charge from the coin scene. The Life gives it: Stephen was sent to the Praetorium "ut secundum leges judicium / Subiret, eo quod imperatoris imaginem coulra leges / conculcasset" (PG100 l.95740-95742; record claim 11).
- Fix, para 5: "Stephen was held in the Praetorium prison." → "Stephen was jailed for trial in the Praetorium." (+1. "jailed" keeps that the Praetorium is a prison, the Life's "in publicum Byzantii carcerem, sacrum prælorium dictum", l.95739-95740. Coming straight after "the scene with the coin", "for trial" names the charge without a new clause. The sentence runs 21 words.)
- Offset, para 1: "Certainly, said those standing by." → "Certainly, said the bystanders." (−1; the Life's "Omnino" from those standing by, l.95722.)
- With both, the brief runs 333 words, FK 7.26, Flesch 66.54. The next sentence, "There, the Life says, he found 342 monks…", still reads.

### R3-M3. README and Open-Gaps 272: the Stephen story's own 765 is not named, and Open-Gaps drops "c. 809"

- Release 44, `iconophile-byzantine-monasticism.documentedStories[0]`: `when` "28 November 765"; text "On 28 November 765, the account continues, a mob from the palace faction dragged him from the prison". So the story also gives 765 and gives it to the Life's account. The README lists the 765 only in `why`, `longDescription` and `voices[1]`. The rule asks the README to flag each live passage. The bullet's "No held line gives 765" covers the substance, but the passage is not named.
- The README's "Fabricius dates the Life to 808, not 'c. 809'" (the story's caveat; Fabricius, PG100 l.88570: "an. Christi 808 scripsit Vitam") is not carried into Open-Gaps 272.
- Fix, README l.23: "The story "Stephen the Younger Dragged Through the Mese" (marked "primary text not yet read") differs too." → "The story "Stephen the Younger Dragged Through the Mese" (marked "primary text not yet read") differs too. Its `when` and text give 28 November 765, the text as the Life's account."
- Fix, Open-Gaps 272, first sub-bullet: "Stephen: Iconophile Byzantine Monasticism's `why`, `longDescription` and `voices[1]` say he was killed in 765, the first two "his Life says"." → "Stephen: Iconophile Byzantine Monasticism's `why`, `longDescription` and `voices[1]`, and the `when` and text of its story "Stephen the Younger Dragged Through the Mese", say he was killed in 765; `why`, `longDescription` and the story's text give it to the Life."
- And in the same sub-bullet: "the crowd (l.96917-96955) and the coin," → "the crowd (l.96917-96955), the Life's date (its caveat's "c. 809", where Fabricius gives 808, PG100 l.88570) and the coin,"

### R3-M4. Theophanes card `dates`: "which" points at the winter

- Card: "Born about 751 or 752 by Jacques Goar's reckoning from the winter of the ice, which Goar says Theophanes's own figures would put about 744."
- "which" falls on "the winter of the ice", and the winter is 755 by Theophanes's own figures, not 744. The 744 is the birth. Goar, THEOPH l.333: "ut ipse numerat, 744, ut melius alii 751 vel alii 752"; record claim 2: "the ice in 755 by his own figures".
- Fix: "Born about 751 or 752 by Jacques Goar's reckoning from the winter of the ice, which Goar says Theophanes's own figures would put about 744." → "Born about 751 or 752 by Jacques Goar's reckoning from the winter of the ice; about 744, Goar says, by Theophanes's own figures."

### R3-M5. Records, Nikephoros claim 34: the range stops before "junior"

- Claim: "Theophanes the priest is another and younger man than Theophanes the Confessor (Bollandists)", witness PG100 l.1629-1648.
- The scan sets the clause across two columns. "Aljus ergo hic noster Theo-" is at l.1647, and "phanes est et aliquanto junior" at l.1656. The range holds "another" but not "younger".
- Fix, witness: "PG100 l.1629-1648" → "PG100 l.1629-1648, l.1656 (the scan carries the clause into the next column)".

### R3-M6. README "Names and ids" and the Decision-Log: first mention is now "Patriarch Nikephoros of Constantinople"

- After R2-M6 the brief opens "Patriarch Nikephoros of Constantinople crowned him". README l.54 says "The brief says "Patriarch Nikephoros" first". The Decision-Log's "Names and ids" bullet says "The brief names "Patriarch Nikephoros" apart from the emperor Nikephoros I". Both are true as far as they go, but they describe the text before round 2.
- Fix, README l.54: "The brief says "Patriarch Nikephoros" first" → "The brief says "Patriarch Nikephoros of Constantinople" first".
- Fix, Decision-Log batch entry: "The brief names "Patriarch Nikephoros" apart from the emperor Nikephoros I" → "The brief names "Patriarch Nikephoros of Constantinople" apart from the emperor Nikephoros I".

### R3-M7. Majors and river counts: state release 44's own figure

- Release 44 has no person row for any of the seven, so the README and Decision-Log are right to use the re-score's Major column. It marks all three of mine "no" (Rescore l.141, l.143, l.155).
- River counts, both rules, against release 44:
  - **Census Who rows.** Greek East & Orthodoxy era 4 rows with `"major": true` are five: Maximus, Martin I, Photius, Athanasios, Symeon. Batch 9's three majors (John of Damascus, Theodore the Studite, Cyril and Methodius) have no rows yet, so "eight after batch 9" is five in the census plus three.
  - **Era 4 card traditions.** Nine: the same eight plus Humbert of Silva Candida (`major` true, a Latin West row), whose only era 4 card tradition is the Macedonian-era church.
  - Iconophile Byzantine Monasticism has no census Who row at all, so this batch's three add no major under either rule.
- The README's "eight … nine" is right. But "By the census's own Who rows … holds eight" can be read as eight rows already in the census.
- Fix, README l.13: "By the census's own Who rows, Greek East & Orthodoxy era 4 holds eight majors after batch 9; counted by era 4 card traditions, it holds nine." → "By the census's own Who rows, Greek East & Orthodoxy era 4 holds five majors in release 44 (Maximus, Martin I, Photius, Athanasios, Symeon), and batch 9's three make eight; counted by era 4 card traditions, it holds nine, with Humbert."

### Close-out records, as they touch these three

- **Decision-Log, "Who profile length: 2:00 restated…".** It quotes Mark's pick as the README does. The README's citation (subject and date) finds it (l.3539). Right.
- **Decision-Log, batch entry.** Its contested points for my three are right: 818 or about 820; exile in 814, 815 or 816; no death year in Stephen's brief, with each witness's on the card (`dates` and `uncertain[2]`). Its round 2 bullets match R2_review: the sermon's "Theophanes, a priest and abbot" came from the worker's tightening (Tighten_2-00.md l.3), and the cut of "The Life calls him the wickedest of men" came from a round 1 change (R1_changes l.20). "No majors" and "None … has a census person row" are true against release 44. Apart from R3-M6, nothing to change.
- **Open-Gaps 272.** The line references are right: README l.23 and l.25, l.26-28, l.42-48, l.70. The Theophanes, Stephen and Nikephoros re-score corrections match README l.42-44 and their lines (Antirrhetici heading at l.14725; the header gives the host offset as +12). The Library items for my three are right. Apart from R3-M3, nothing to change.
- **Census walk, release 44.** Every hit for Theophanes (Philoxenus longDescription and card; Sophronius; Maximus; Martin I; John Climacus; Pisentius; the Melkite story's caveat and sources; the Heraclian-era stories [0] text and [1] caveat; the Stephen story's sources; Photius; the Paulicians story) is in the README bullet. So is every hit for the patriarch Nikephoros (`voices[4]`, edge 238 note and quote, John Climacus `uncertain[1]`). Every other "Nikephoros" or "Nicephorus" is Phokas, Kallistos, the Monk, or the exarch of 1596. For Stephen, the only addition is R3-M3.

---

**Verdict: Part A passes round 3 with no blocking point. All seven minor fixes are exact, and only R3-M2 touches a brief (it stays at 333 words). Counts: 0 blocking, 7 minor (R3-M1 to R3-M7).**

---

## Round 3 review, Part B: Nicholas Mystikos, Peter of Sicily, Michael Keroularios (era 4 batch 10)

Reviewer: fresh Opus, full effort, under the brief's "Round 3 scope". Branch `claude/cft-who-era4-batch10` at 4ef7e119. No repo file was edited.

## How I checked

- `git diff 581b8e13 HEAD` on the three briefs, cards, audio scripts and `records.json`. Every round 2 Part B change is in the files, as R2_changes.md says. I reread each changed sentence as new text against its source lines:
  - Nicholas: "prima Februarii" (PG109 l.33542; R2_changes cites l.33541, one line off, in the audit log only), and Alexander naming the guardians (PG111 l.471-530; records claim 25).
  - Peter: "secundo anno imperii Basilii ... novem menses commoratus" (PETER l.3825-3829); "sperantes eo se adjutum iri, quod divina praedicatio ibi initium modo ceperit ... latenti adhuc vero tritico" (l.835-837); "Haec omnia sunt" (l.182) after the 868-871 window (l.148-164); "Petrum falli, qui Paulicianos cum Manichaeis re vera eosdem esse contendat" (l.3878-3881); Rački's header, "read to the Academy on 28 November 1868", Rad VII (1869) (RACKI l.1-3), and "Neznamo ... njihova je nauka onamo svakako doprla" (l.857-866).
  - Keroularios: "nisi forte resipuerint" (WILL l.15036-15046); Imbros and the Thracian court in the speech (PSELL l.23818-23870); "colloquium congressionemque detrectavimus" (WILL l.18076); the envoys' entry "cum cruce et baculis" (l.17228-17232).
  All pass.
- The two items applied with a change are right. For R2-B3, MANSI l.103092 reads "anno Mundano VIM. CDXXVIII. Indi@ione VIII", which is 6428. For R2-M11, the offset sentence "His letters to Peter, patriarch of Antioch, tell of Rome's envoys" is true to Letter I (WILL l.17210-17242).
- R2-M13: the "records only" tags are on claims 8 and 11 (the brother's death; the seal). Both claims still match their lines.
- R2-M15 was not taken in Part B. The worker resolved it with the Decision-Log entry at l.3539, which exists.
- Audio: each script equals its brief, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. Pass for all three.
- Words and readability now:
  - Nicholas: 328 words, FK 7.17, FRE 68.85.
  - Peter: 330 words, FK 7.14, FRE 65.34.
  - Keroularios: 329 words, FK 6.84, FRE 69.21.
  No sentence runs past 23 words.
- With my replacements below applied by script:
  - Nicholas: 330 words, FK 7.20, FRE 68.74.
  - Peter: 333 words, FK 7.17, FRE 65.38.
  - Keroularios: 329 words, FK 6.84, FRE 69.21.
  All stay at or under 333, so the README's "328 to 333" still holds.
- Census: I walked `cic-website/data/world-census.json` (release 44, merged on this branch) for every spelling: Mystik, Nicholas, Nicolaus, fourth marriage, tetragamy, Peter of Sicily, Petrus Siculus, Paulician, Tephrike, Keroularios, Cerularius, Caerularius.
  - New release-44 person rows that cite the PG111 file (Sophronius, Dionysius of Tel Mahre, Moses bar Kepha) cite it for Eutychius only and do not name Nicholas.
  - The Photius row names Pope Nicholas I. That is another man.
  - No new passage names Peter or Keroularios.
- Majors and river counts against release 44:
  - None of the three has a census person row. The re-score marks each "no" (Rescore.md l.152-154).
  - Census Who rows, era 4, Greek East & Orthodoxy, `major: true`: Maximus, Martin I, Photius, Athanasios and Symeon, 5 in all. Batch 9 adds John of Damascus, Theodore the Studite, and Cyril and Methodius, which makes 8.
  - Era 4 card traditions add Humbert, whose row has `major: true` (his only era 4 card tradition is Macedonian). That makes 9.
  - So the README's "eight ... nine" and the Decision-Log's "The river counts in the batch 9 README stand" are true under both counting rules after release 44.

---

## nicholas-mystikos

Read in full as a listener. The scene, the partisan marking ("to win the pope over", "the other side's account"), the treason charge with de Boor's concession, the chronicle's Thomas, and the 906 refusals by de Boor's reading all stand. The R2-B1 fix leaves the year to de Boor's paragraph, by implication only. That is attributed, and the card carries all three placings.

**R3-M1. Brief, last paragraph: "Once, on his knees, he had told Leo that a king is called an unwritten law, whose deeds should match the written law."**
- The kneeling and the plea rest on one partisan witness, his own Letter 32: "Cujus autem ad genua, imo ad pedes provolutus" (PG111 l.14028-14029) and "Rex dicitur esse lex non scripta ... similis esse debet legi scriptae" (l.14093-14097).
- Every other report from the letter in this brief is attributed ("Nicholas later wrote", "Nicholas writes", "Nicholas says"). This one, the closing line and the brief's only words of his own, is told as the narrator's fact.
- Replacement (+2, brief 330): `Once, he writes, he had told Leo on his knees that a king is called an unwritten law, whose deeds should match the written law.` (24 words.)
- "He" is Nicholas, the subject of the sentence before.

**Records, minor (R3-M2).** Contested claim "When the legates arrived", Nicholas's side, cites PG111 l.14277-14279. The "eight or nine months" is at l.14275: "Octavo vel nono mense post initas illas nuptias ... veteris Romae legati advenerunt" (l.14275-14277). Replacement witness: `(PG111 l.14275-14277; the arrest follows at l.14390-14402)`.

## peter-of-sicily

Read in full. The opening scene, the embassy, the flagged thin life ("He says that is all we know of Peter for certain"), the hostile marking ("The History is hostile polemic"; "An earlier hostile witness"), and the Photius dispute with Montfaucon all stand.

**R3-M3. Brief paragraph 5: "Gieseler says Peter is wrong to call them Manichaeans."**
- The round 2 fix gives the sentence a referent. But it now says less exactly what Gieseler says. Two sentences earlier the brief says the title "calls the Paulicians Manichaeans". Theophanes the Confessor, writing before Peter, already uses the name (THEO l.89626; card `uncertain[0]`).
- Gieseler does not object to the name. He says Peter errs in holding that they are really the same: "Petrum falli, qui Paulicianos cum Manichaeis re vera eosdem esse contendat" (PETER l.3878-3881).
- The card has it right: "mistaken that the Paulicians are really Manichaeans".
- Replacement (+3, brief 333): `Gieseler says Peter is wrong to hold that they are really Manichaeans.`

## michael-keroularios

Read in full. The partisan marking of Psellos and of the envoys' sentence, the two Michaels kept apart, the condition on the curse, the two death tellings in the brief (the card has the third), and the close all stand.

**R3-M4. Brief paragraph 5: "They walked into the palace with a cross and staffs, he writes, and would not greet him or bow."**
- The sentence before ends on "Peter, patriarch of Antioch". So "he writes" falls nearest Peter, the man written to, and "him" could be either man.
- The letter is Michael's: "cum cruce et baculis intra regiam ingressi sunt" (WILL l.17231-17232).
- Replacement (0 words): `They walked into the palace with a cross and staffs, Michael writes, and would not greet him or bow.`

---

## README (sections on these three)

The round 2 fixes are in place and right:
- The Nicholas census bullet's four added points: DEBOOR l.5795-5802; PG111 l.662-664; PG111 l.862-865; DEBOOR l.8640-8656; MANSI l.103092; DEBOOR l.4693-4694.
- The Keroularios death sentence in "Corrections".

The census lists for Peter (movement 75, edges 242 and 243) and for Keroularios (movements 79, 102, 320, 617 and 618; edges 15 and 235) are complete. Edge 15's "patriarch in name only" and "seeds of heresy ... every day" agree with the sentence ("abusive dictus patriarcha"; "zizania haereseon quotidie semi-", WILL l.14970).

**R3-M5. "Live census mentions", Nicholas: one more point is missed under "The rest agrees".**
- The story runs: "Leo appealed to Rome and the eastern patriarchs, all of whom allowed a dispensation, and in February 907 he deposed Nicholas". That puts the dispensation before the deposition.
- The held witnesses disagree on that order. Nicholas has Rome's legates arrive "Octavo vel nono mense post initas illas nuptias", before his arrest (PG111 l.14275-14277).
- De Boor reads the Life as having them not yet come on the day of the exile ("am Tage der Verbannung des Nicolaus die Legaten als noch nicht eingetroffen", DEBOOR l.8548-8550). He prefers the Life (l.8599-8611). The card's "When the legates came" item carries both sides.
- Insert before "The rest agrees.": `It also has the dispensation come before the deposition. Nicholas has Rome's legates arrive before his arrest (PG111 l.14275-14277); in the Life, as de Boor reads it, they had not yet come on the day of his exile, and de Boor prefers the Life (DEBOOR l.8546-8561, l.8599-8611).`

**R3-M6. "Live census mentions", Keroularios: "A link note says he kept the post "until 1058"; Will gives 1059 (l.4053)."**
- Blackmore, who is held, gives the census's year: "His successor was Michael Cerularius, who sat till 1058" (MOUR l.16005). Open-Gaps 272 already says "which is Blackmore's year".
- As written, the README reads as though no held line supports 1058. That is the same kind of point as the Peter bullet's "as Rader and Gifford give".
- Replacement: `A link note says he kept the post "until 1058", which is Blackmore's year (MOUR l.16005-16006); Will gives 1059 (l.4053).`

**R3-M7. "Corrections to the re-score", Nicholas: the row's one disputed date is left out.**
- The README says "The row lists no disputed dates". But the row cites the Life for "l.5361-5365 (exile 907)" (Rescore.md l.154).
- That is de Boor's year. Krug and Muralt have 908 ("nicht, wie Krug und Muralt nach Symeon Magister annehmen, a.908", DEBOOR l.5798-5800). Mai has nine years after the election, or eleven by Leunclavius (PG111 l.662-664).
- Replace `The row lists no disputed dates; the election (895 or 901), the return (911 or 912) and the death (924 or 925) are all in dispute.` with `The row gives the exile as 907, which is de Boor's; Krug and Muralt give 908, and Mai nine years after the election, or eleven by Leunclavius (DEBOOR l.5798-5800; PG111 l.662-664). It lists no other dates, though the election (895 or 901), the return (911 or 912) and the death (924 or 925) are all in dispute.`

---

## Decision-Log, "Who profiles, era 4 batch 10" (Part B content)

Checked against the README, the reviews and the files:
- Round 1 Part B, 13 and 20.
- Round 2 Part B, 3 and 15.
- The Nicholas, Peter and Keroularios round 1 examples, which match R1-B1, B3, B4, B5, B6, B7, B8, B9 and B10.
- "No majors".
- "none is a census person entry".
- The lengths.

All are right, apart from the following.

**R3-M8. "Contested points told in place": two of the three profiles are not told as stated.**
- "Nicholas's fall is 907 for de Boor and 908 for Krug and Muralt". Since R2-B1 the brief gives no year. The card gives three placings, and Mai's is the one the sentence leaves out (PG111 l.662-664).
- "whether eastern legates came is told with de Boor and his doubters". The brief gives de Boor only ("So, de Boor finds"). The doubters are on the card.
- "Keroularios's death is told three ways". It is told two ways in the brief and three on the card.
- Replace `Nicholas's fall is 907 for de Boor and 908 for Krug and Muralt, and whether eastern legates came is told with de Boor and his doubters.` with `Nicholas's brief leaves the year of his fall untold; his card gives de Boor's 907, Krug and Muralt's 908, and Mai's nine years after the election, or eleven by Leunclavius. Whether eastern legates came is told with de Boor in the brief and with his doubters on the card.`
- Replace `Keroularios's death is told three ways` with `Keroularios's death is told two ways in his brief and three on his card`.

**R3-M9. Round 2 list: "The tightening put back Nicholas's disputed year 907 with one placing."**
- The year was never taken out of the brief. The draft (66ba54ee) and the round 1 text (3e1ec684) both have "The banquet and the boat followed on 1 February 907". Round 1's R1-B1 took it off the card's `knownFor` only.
- So this blocking point came neither from a round 1 fix nor from the tightening.
- Replace `The tightening put back Nicholas's disputed year 907 with one placing. It also left "the same" with no referent in Peter's brief, on the profile's main contested point.` with `Nicholas's brief still gave his disputed year 907 with one placing; round 1 had taken it off his card only. The tightening left "the same" with no referent in Peter's brief, on the profile's main contested point.`

## Open-Gaps 272 (Part B content)

The README line numbers it cites are right: l.23, l.25, l.26-28, l.42-48 and l.70. So are its Keroularios census text and its Library items for these three.

**R3-M10. Peter, Nicholas and the re-score bullet drop points the README holds.**
- **Peter.** "the link `paulicians--bogomils` has "around 870", and Gieseler dates the embassy to 868 (PETER l.154)." This leaves out that two held witnesses give 870: Rader, "praeter propter DCCCLXX" (PETER l.599), and Gifford, "circ. a.d. 870" (NPNF7 l.9962-9963). A census fixer would read 870 as wrong.
  - Replace that clause with: `the link `paulicians--bogomils` has "around 870", as Rader and Gifford give (PETER l.599; NPNF7 l.9962-9963), where Gieseler dates the embassy to 868 (PETER l.154).`
- **Nicholas.** The entry leaves out the README's point that the account before the Tomus, in the lines read, says nothing of Constantine VII's legitimacy. With R3-M5 it would also lack the order of the dispensation.
  - Insert before `Owner: the coordinator` in the first bullet: `The story's council accepts Constantine VII's legitimacy; the account before the Tomus of Union, in the lines read, says nothing of it. The story puts the dispensation before the deposition; Nicholas has Rome's legates arrive before his arrest (PG111 l.14275-14277), and the Life, as de Boor reads it, after his exile (DEBOOR l.8546-8561).`
- **Re-score corrections, Nicholas** (follows R3-M7).
  - Replace `the row lists no disputed dates, but the election (895 or 901), the return (911 or 912) and the death (924 or 925) are all disputed.` with `the row's exile of 907 is de Boor's, against Krug and Muralt's 908 and Mai's nine years after the election (DEBOOR l.5798-5800; PG111 l.662-664); the election (895 or 901), the return (911 or 912) and the death (924 or 925) are also disputed.`

---

## Verdict

No blocking point in Part B. Every round 2 fix is applied and right as new text. The three briefs read cleanly and stay inside 2:00. The minor points are wording and record fixes, each with exact text, and none needs new research. Counts: 0 blocking, 10 minor (R3-M1 to R3-M10).

---

## R3, Part C: ilarion-of-kyiv, the README as a whole, and the close-out records (era 4 batch 10)

Reviewer: fresh Opus, full effort, 2026-11-15. Branch `claude/cft-who-era4-batch10` at 4ef7e119. No repo file edited.

## Checks run

- Lengths, len(text.split()): Ilarion 329, Keroularios 329, Nicholas 328, Nikephoros 330, Peter 330, Stephen 333, Theophanes 332. The README's and Decision-Log's "328 to 333" is right.
- `grade_text`, all seven: FK 6.8 to 8.5, Flesch 60.3 to 69.4. Ilarion FK 6.97, Flesch 66.45. All pass.
- Audio equals brief plus `[calmly] ` on the first paragraph and `[warmly] ` on the last, by script, all seven. Pass.
- Card key order, all seven, against the pattern. Pass (Stephen has no `keyWorks`, left out).
- `git diff 581b8e13 HEAD` on the Ilarion brief and card: every line changed in round 2 reread against its source.
- Census: release 44 (`meta.number` 44, 2026-11-15) on this branch is identical to origin/main. I walked every string in `movements` and `edges` for every spelling of the seven names, in release 43 (`1959c7f2^1`) and in release 44. The 184 passages are byte-identical between the two releases, so the README's census bullets, checked against 43 in round 2, still hold for 44. I re-spot-checked the Keroularios spellings (three entries and two links read "Cerularius"; Macedonian voices and Humbert read "Keroularios") and the Ilarion passages. Both are as the README says.
- Majors in release 44: 250 Who rows (`kind: person`), 108 flagged major. None of the seven ids, nor `hilarion-of-kyiv` or `michael-cerularius`, is a movement id.
- A fresh whole-corpus search of `cic/texts` for Hilarion, Ilarion, Иларион, Иларіон and Ларион in files that also name Kyiv. This found finding R3-B1 and R3-M5.

## Round 2 Part C fixes: applied and right as new text?

| R2 point | State | Right against the source? |
|---|---|---|
| B1 Susza missing from Sources | Both Susza entries added. The Paterik entry was widened to "the founding account, and Simon of Vladimir's letter" | Yes. The headers match. Widening the Paterik title was right, since the card now cites PAT l.1086-1111 as well as the letter. |
| B2 Paterik misreported | `uncertain[5]` and `[7]` rewritten; records claim added; claim 33's range is now l.1098-1106 | Yes. PAT l.1086-1092: Antony to Kyiv, "на Брестовое приде", the cave "ископали варязи". l.1094-1097: after Vladimir's death Sviatopolk "нача избивали братёо свою", and Antony "пакы бЪжа въ святую гору". "Mount Athos" for "святую гору" is right; the Paterik's abbot is on the Holy Mountain at l.1084-1086. The ordering ("earlier, before Ilarion dug his cave") holds: the Ilarion passage starts at l.1098. Using "in nearly the same words" for `[7]`, not "repeats", was right. |
| B3 Clement | "Clement of Smolensk, a later metropolitan" | Yes. MOUR l.2064, "Clement a monk of Smolensk"; l.2076-2077, "the native Russian metropolitans Hilarion and Clement". |
| M1, M2 brief | Applied | Yes. GORSKII l.759 has "of him". "The foreword holds" fixes the pronoun. |
| M3 "grew there" | Applied | Yes. |
| M4 Izyaslav | "early in the reign of Izyaslav, Yaroslav's son" | Yes. MOUR l.1693-1694 has George sent "early in the reign of Isyaslaff", and l.1571-1572 has "Isyaslaff the son of Yaroslaff". |
| M5 quotation marks on Russian | Removed | Yes. |
| README B4, M6-M11 | Applied, M6 and M10 with changes | Yes. The Decision-Log entry exists (l.3539). M6's merged wording names each Theophanes passage once. M10's two-sentence Susza line avoids "the opposite view", which was right: Smotrytsky's refusal and Mouravieff's later letter of blessing are not exact opposites. |

The "not taken" and "applied with change" calls in R2_changes Part C are all sound.

## ilarion-of-kyiv

### The brief, read in full as new text

As a listener hears it, the brief holds up. It opens on the Berestovoye scene and the cave (CROSS l.11744-11753). It places him and the 1051 making (l.11741-11742), and flags the thin life in ¶3. The consecration dispute is told in place, with both sides named (GORSKII l.796-803; MOUR l.1489-1496). The confession comes next (GORSKII l.179-182, l.3994-3995), then the Sermon as the foreword's argument, then the Sermon's own images. Each sentence changed in round 2 checks out against its lines. The quotation is verbatim (CROSS l.11747-11748). No sentence runs past 25 words. I find no AI tell, no aphorism, no rhetorical question and no unclear pronoun. The brief needs no change in this round, including under R3-B1 below. It gives 1051 as the Chronicle's ("In 1051, the Chronicle says"), and the confession's own year 6559 matches.

### R3-B1. A held annalist gives 1031 for his election and 1063 for George, and no field gives either (card `dates`, `uncertain[6]`, `sources.about`; records; README "Who the sources are")

Michael Harasiewicz's *Annales Ecclesiae Ruthenae* (Lviv, 1862) is held at `cic/texts/harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt`. It dates the election twice, and both times the scan reads 1031:
- l.1671-1673: "erat celeberrimum illud Criptarum (Peezar) subterranearum / Kijoviae, cui initia dedit Hilarion, electus anno 1031 in / Metropolitam".
- l.1748-1749, his series of Kyiv metropolitans: "3. Theopemptus (1023). 4. Hilarion (1031). 5. Georgius I (1063). 6. Joan-nes I (1072)."

The card's `dates` gives 1051 by the Chronicle and the confession and names no other placing. `uncertain[6]`, "His end", gives George by 1079 (the foreword), by 1072 (Cross) and "early in the reign of Izyaslav" (Mouravieff), but not Harasiewicz's 1063. That is the earliest held year for the next metropolitan, and the closest held bound on Ilarion's term. Round 1 counted the same gap as blocking (R1-B1, the missed 1072). The records' `absent_details` note on his death says "Searched all cic/texts for Hilarion, Ilarion, ...". That search should have found l.1672, which reads plainly "Hilarion".

The rule is that disputed dates give every held placing. Harasiewicz's list is loose elsewhere: he has Theopemptus in 1023, and the Chronicle's 1051 is matched by Ilarion's own dated confession. So the card can say plainly which way the evidence runs. But it cannot leave the placing out. The brief needs no change, since it attributes 1051 to the Chronicle.

Fixes, checked against the lines above:

Card `dates`. After "...by the Russian Primary Chronicle and his own confession of faith." insert:
> Michael Harasiewicz's Annales Ecclesiae Ruthenae (1862) gives 1031 for the election, as the scan reads twice, and dates the next metropolitan, George I, to 1063.

That is one sentence of 25 words.

Card `uncertain[6]`. After "...and Mouravieff says George was sent early in the reign of Izyaslav, Yaroslav's son." insert:
> Michael Harasiewicz's list of the Kyiv metropolitans (1862) puts George I in 1063.

That is 13 words.

Card `sources.about`. Append:
```json
{
  "title": "Annales Ecclesiae Ruthenae",
  "author": "Michael Harasiewicz, archpriest of the Ruthenian metropolitan chapter of Lviv",
  "date": "1862",
  "language": "Latin",
  "file": "cic/texts/harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt"
}
```
The header (l.1-4) gives "Archpriest and Provost of the Ruthenian Metropolitan Chapter of Lviv" and "1862 (preface dated Leopoli, 29 June 1862...)".

Records, `claims`. Add:
> {"claim": "Harasiewicz: \"Kijoviae, cui initia dedit Hilarion, electus anno 1031 in Metropolitam\"; his series: \"4. Hilarion (1031). 5. Georgius I (1063).\" (quoted as the scan reads)", "witness": "HARAS (harasiewicz_annales-ecclesiae-ruthenae-lat_1862.txt) l.1672-1673, l.1748-1749", "formation_confidence": "Contested"}

Records, `contested_claims`. Add:
> {"claim": "The year he was made metropolitan", "sides": ["Russian Primary Chronicle: 6559 (1051) (CROSS l.11741-11742; PSRL1 l.6896-6897)", "His confession: 6559 (1051) (GORSKII l.181, l.3995)", "Harasiewicz (1862): 1031, as the scan reads twice (HARAS l.1672, l.1749)"]}

Records, `absent_details`, "Year of his death or end of office". Replace "Searched all cic/texts for Hilarion, Ilarion, Иларион, Ларион, Ларіон and OCR variants." with:
> Searched all cic/texts for Hilarion, Ilarion, Иларион, Ларион, Ларіон and OCR variants. Harasiewicz (1862) gives no end for him and lists George I under 1063 (HARAS l.1749).

README, "Who the sources are", Ilarion. Before "Nothing held gives his birth...", insert:
> Michael Harasiewicz's Annales Ecclesiae Ruthenae (1862) gives 1031 for the election and 1063 for George I (l.1672, l.1749).

### R3-M4. The card calls the batch's own Who "Michael Cerularius" (card `uncertain[3]`, twice)

The batch names him Michael Keroularios, and his profile and the Humbert profile use that form. On the Ilarion card the narrator's own prose (no quotation marks) has "a letter of blessing from the patriarch Michael Cerularius" and "consecration from Michael Cerularius". A reader moving between the two cards meets two names for one man. "Cerularius" is Blackmore's form (MOUR l.1504-1505), and it is already listed as an other name on the Keroularios card.

In `uncertain[3]`, replace "from the patriarch Michael Cerularius" with:
> from the patriarch Michael Keroularios

and "from Michael Cerularius, whom he calls the leader of the schism" with:
> from Michael Keroularios, whom he calls the leader of the schism

Optionally make the same change in the README's Ilarion sources line ("from Michael Cerularius" → "from Michael Keroularios").

### R3-M5. A second held witness on why he was consecrated in Kyiv, readable only as garble (records; Open-Gaps 272)

`arkhiv-iugo-zapadnoi-rossii_ch1-t7-pamiatniki-polemiki-vyshensky-mogila-rus_1887.txt` holds a Polish pamphlet of the Vilnius disputes (p. 384). Its scan prints the Polish in Cyrillic letters. At l.16547-16552 it reads, as garble, "Ні-Іагіоп Меігороііі окоіо гоки Рапзкіе^о 1051 сііа чѵоупу, кіог$ па іеп сгйз Киз 2 Сггаекаті лѵіосііа, о сгет Раіегік Кііолѵзкі Ріесгегзкі, аіе чѵугагпіеу 2опагаз". That is: Hilarion was made metropolitan about 1051 because of the war Rus was then waging with the Greeks, as the Kyiv Caves Paterik says, and more clearly Zonaras. The volume's index points to it (l.32507-32511, "о поставленіи на кіевскую митрополію Иларіона безъ сношенія съ Греціей), 384") and names Theopemptus as Ilarion's predecessor (l.34362-34363, p. 449).

The text cannot be quoted, and it sides with Mouravieff, so the card loses nothing a reader needs. But the records' search note should not read as if the corpus held nothing more. Add to `absent_details`:
> {"detail": "A Polish pamphlet on the consecration", "note": "Arkhiv Iugo-Zapadnoi Rossii I.7 (1887), p. 384, gives the war with the Greeks as the reason, citing the Caves Paterik and Zonaras; its scan prints the Polish in Cyrillic letters (l.16547-16552), so it is not used. The index points to it (l.32507-32511)."}

Optionally add the same to Open-Gaps 272's Library line: "a readable scan of the Polish pamphlets in Arkhiv Iugo-Zapadnoi Rossii I.7 (p. 384, on Ilarion's consecration)".

## README.md, as a whole

### What checks out

- **Framing (l.3-5).** Seven ids. The plan's nine plus batch 9's two make eleven (Rescore l.101). Seven are written and four Georgian entries split off. The four entries and the one Peeters volume match Rescore l.161-164, and the pairing question is Rescore l.164. The approval reads "The worker told the coordinator, who approved the split (2026-11-15)", which matches the Decision-Log's coordinator's call. "None is a census person entry" is true in release 44.
- **Majors (l.9).** Release 44 does carry the flag, and no batch id is a Who row, so the re-score's Major column ("no" for all seven) is the right fallback.
- **Lengths (l.11).** 328-333 is right. No brief claims an exception, so no README line is owed. The Decision-Log citation and Mark's quoted pick match the entry at l.3539-3543.
- **River counts (l.13), against release 44.** By the census's own Who rows, release 44 flags five Greek East & Orthodoxy era 4 rows major: Maximus, Martin I, Photius, Athanasios and Symeon. These are the five batch 9 counted. With batch 9's John of Damascus, Theodore the Studite, and Cyril and Methodius, that makes **eight**. By era 4 card traditions, Humbert's card adds The Byzantine Imperial Church (Macedonian Era), for **nine**. John of Damascus counts through Iconophile Byzantine Monasticism and Melkite Arabic Christianity, and Cyril and Methodius through Cyrillo-Methodian Slavic Christianity, both on lane 3. Antony and Theodosius are left out, as batch 9 sets out, because they sit on the map in era 5. This batch adds no majors, so both counts stand. (Latin West is not this README's subject. In release 44 its era 4 count is still ten, Humbert's row among them.)
- **Traditions (l.15, l.62-68).** The names are exact in release 44: "Iconophile Byzantine Monasticism" (726-843), "The Byzantine Imperial Church (Macedonian Era)" (843-1054), "Kievan Rus' Christianity" (988-1054), "The Byzantine Church after the Schism" (`byzantine-church-after-1054`, era 5, 1054-1300), and "The Byzantine Imperial Church (Heraclian & Iconoclast Eras)" (622-843). All are on "3 Greek East & Orthodoxy". The 3/3/1 + 1 count matches the cards.
- **Live census mentions (l.18-28).** Unchanged from release 43 to 44 (see Checks), so round 2's verification carries over. The Keroularios "six other places" and "three entries and both links" are right.
- **Names (l.50-57).** Right, and each form named is on its card.
- **Language (l.72-74).** Each quotation listed is on the card named, and the English is held. Sathas's prologue is shelved as "Modern Greek", which "Greek" covers.
- **File table (l.76-81).** It matches the card keys and the records' shape.

### R3-M1. The river-count paragraph does not say it was checked against release 44's flags (README l.13; Decision-Log batch entry, "No majors")

The paragraph says the batch 9 counts "stand" because this batch adds no majors. Batch 9 counted before the flag existed, and the brief for this round asks for both rules against release 44. The figures are right, but the README should say they were checked.

Replace "This batch adds no majors, so the counts in the batch 9 README stand. By the census's own Who rows, Greek East & Orthodoxy era 4 holds eight majors after batch 9; counted by era 4 card traditions, it holds nine." with:
> This batch adds no majors. Release 44's flags mark the same five Greek East & Orthodoxy era 4 Who rows that batch 9 counted: Martin I, Maximus, Photius, Athanasios and Symeon. With batch 9's three, the census's own Who rows give eight. Counted by era 4 card traditions, Humbert's Macedonian-era card makes nine; Antony and Theodosius sit in era 5, as batch 9 sets out.

In the Decision-Log entry, replace "The river counts in the batch 9 README stand." with:
> Release 44 flags the same five Greek East era 4 rows that batch 9 counted, so the river counts in the batch 9 README stand: eight by the census's Who rows, nine by era 4 card traditions.

### R3-M2. "will be logged" is out of date (README l.20)

Open-Gaps 272 now exists. Replace "Each difference below will be logged in Open-Gaps, in an entry "Era 4 Who batch 10", for the census fix." with:
> Each difference below is logged in Open-Gaps, "Era 4 Who batch 10" (2026-11-15), for the census fix.

### R3-M3. The Stephen bullet's 767 has no line (README l.23)

"Fabricius gives 766 (l.88570-88571) and the PG108 editors 767." The records cite the editors at THEO l.131105-131109. Replace "and the PG108 editors 767." with:
> and the PG108 editors 28 November 767 (THEO l.131105-131109).

## Close-out records

### Decision-Log, "Who profile length: 2:00 restated, longer only when earned" (l.3539-3543)

The entry is accurate. Mark's pick and the option text are quoted, and so are his two remarks. The cross-reference "Who profile length: non-majors to 2:00 from the next batch, and era 4 batch 7 kept as written" (2026-11-14) exists at l.3067. "Hold to two without cutting off" is there (l.3069). The "restatement, not a new rule" framing rests on Mark's own "its not a new rule". The 2026-11-14 entry's reading ("non-majors aim at 2:00, and a good story at about 2:15 is preferred", l.3071) is consistent with "longer only when earned". The writing is clean.

### Decision-Log, "Who profiles, era 4 batch 10" (l.3545-)

Checked against the reviews and the files:
- Round 1's 22/61 and its split (A 6/21, B 13/20, C 3/20) match R1_review l.3. Each listed blocking point matches an R1 heading: Part A B1, B3, B4 and B5; Part B B1-B5, B6-B7, B8-B11 and B12; Part C B1 and B3.
- Round 2's 12/35 and its split (A 5/9, B 3/15, C 4/11) match the three verdicts (R2_review l.106, l.209, l.462). The seven bullet points account for all twelve blocking points.
- "All were applied." This holds in substance. Part B's R2-M15 was "not taken here", and it was the same point as Part C's R2-B4, which the length entry resolved. The entry says so.
- The contested points, names, traditions, active year and "American spelling (Decision-Log 77)" all match the README and cards. "Opus for all" is at l.2349.

### R3-M9. Two lines read as settled before round 3 closes (Decision-Log batch entry; Open-Gaps 272)

- "This batch's pull request waits for data release 44 (PR #1669)." Release 44 is merged and on this branch (1a18674a). Replace with:
  > This batch's pull request waited for data release 44 (PR #1669), which is now merged into this branch.
- The closing "Approved to proceed (coordinator, 2026-11-15; Mark may overrule)" and Open-Gaps 272's "are approved to proceed" are written before round 3's result. If R3-B1 goes to Mark for a cap ruling, these should stand only once that ruling is in. When the worker fills the "**Round 3.**" line, it should name the cap ruling or say that none was needed. No text change is needed now if the worker does this.

### Open-Gaps 272 (l.3555-)

Every cross-reference checks: README l.23 and l.25 (the Stephen and Nicholas bullets), l.26-28, l.42-48 and l.70; Rescore l.164; batch 9's card l.8 and l.36; Humbert's card l.43. The cited source lines match the README's. The Antony and Theodosius note is right. Their brief has "On a hill outside Kyiv he dug a cave", and their card has the 1462 Paterik's earlier stay but not the Varangian cave. The owners are named. The number is in sequence and nothing earlier was renumbered.

### R3-M6. Open-Gaps 272, Stephen: two held placings dropped

The README gives five placings for the death. The entry gives three. Replace "The Life gives 28 November in his fifty-third year (PG100 l.97215-97217), Fabricius 766 (PG100 l.88570-88571), and Theophanes 20 November under Goar's 757 (PG108 l.78706-78707)." with:
> The Life gives 28 November in his fifty-third year (PG100 l.97215-97217), Fabricius 766 (PG100 l.88570-88571), the Short History's marker 766 (PG100 l.81476), Theophanes 20 November under Goar's 757 (PG108 l.78706-78707), and the PG108 editors 28 November 767 (PG108 l.131105-131109).

### R3-M7. Open-Gaps 272, Nicholas: one README difference left out

The README's Nicholas bullet says the account before the Tomus of Union, in the lines read, says nothing of Constantine VII's legitimacy. The census story says the council condemned fourth marriages "while accepting Constantine VII's legitimacy". The entry leaves this out. After "...and 921 in de Boor (DEBOOR l.4693-4694)." add:
> Its "accepting Constantine VII's legitimacy" is not in the account before the Tomus of Union, in the lines read.

### R3-M8. Open-Gaps 272 has no blank line before it

Entries 269-271 are each set off by a blank line. Entry 272 follows 271's last sub-bullet directly (l.3554-3555). Insert one empty line before "272.".

---

**Verdict:** The Ilarion brief is sound and needs no change. Every round 2 fix is right as new text. The README's majors and river counts hold against release 44 by both rules, and its census bullets are unchanged by 44. One blocking point: a held 1862 annal gives 1031 for the election and 1063 for George, and no card field or record gives it (card and records only). Counts: 1 blocking (R3-B1), 9 minor (R3-M1 to R3-M9, numbered across sections).
