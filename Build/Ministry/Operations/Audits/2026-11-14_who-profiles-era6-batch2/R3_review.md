# R3 review: era 6 batch 2

Round 3, the last under the cap, is a targeted recheck at full effort by four fresh Opus reviewers, one per part, of what round 2 changed and its findings. Every quotation in the briefs and cards was re-verified against its file and lines. It found 5 blocking and 5 minor points (Part A 1 and 3, Part B 1 and 3, Part C 2 and 1, Part D 1 and 1). Blocking points are open after round 3, so the batch stops for Mark's cap ruling.

## Era 6 Who batch 2, round 3 recheck: PART A

**Scope.** A targeted recheck of `catherine-of-siena` and `bridget-of-sweden` (brief, card, audio, and each one's `records.json` entries changed in round 2) and every `README.md` line changed in round 2, for any person. The R2 findings checked are A2-B1 and A2-M1 to A2-M15 (R2_review.md, "PART A"), against R2_changes.md Part A and `git diff d7c4490c..e072b50d`. Branch `claude/cft-who-era6-batch2` at e072b50d. No repo file was edited. No web, paid or model call was made.

**Method.**
- Read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md`, lessons.md, R2 Part A and R2_changes Part A.
- Took the word diff of both profiles and the README for d7c4490c..e072b50d, and the records diff for these two people.
- Reopened every source behind a changed line with 20 or more lines of context, asking what document a note annotates, who speaks, and whether a condition or hedge dropped.
- Checked every double-quoted string in both briefs and both cards against its file by a whitespace-, case- and hyphen-tolerant script, then by eye at the line.
- For each README line changed in round 2 about another person, checked the line against that person's card and records, and against the source where the line makes its own claim.
- New absence claims: reran Bridget's birth-year search (159 files naming her; 1300 to 1309, MCCCI- and birth words within 200 characters of Birgit-/Brigitt-/Bridget/Brigida). Searched all cic/texts for Cabasil-/Kabasil-/Καβάσιλ- within 300 characters of a see word and a year 1340 to 1399, for the README's new Cabasilas line. Searched all cic/texts for Gobelin- and Platina for first-mention identifiers.
- Diffed both audio files against their briefs by script; checked card field order by script; counted words with `wc -w`; scored all eight briefs with `engine.m1.gates.grade_text`; ran `tools/check_spelling.py` on both briefs, both cards and the README (0 findings).

**Files opened (cic/texts/), with context.**
- BIRGE `birgitta_revelations-enm_cumming1929.txt`: l.850-860, 915-1062, 2115-2140.
- BIRGL `birgitta_revelationes-lat_duranti1628.txt`: l.205-262, 8150-8185, 10321, 11076, 11095-11128, 98405-98425, 98545-98615, 98770-98805, 98940-99022.
- ASMAR3 `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt`: l.132870-132905, 133255-133275.
- MANSI26 `mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt`: l.1-8, 53385-53420, 111550-111560.
- MANSI27 `mansi_sacrorum-conciliorum-collectio-tomus-27-1409-1418-lat_welter-facsimile1902.txt`: l.132414-132422.
- CATHL `catherine-of-siena_selected-letters_scudder1905.txt`: l.1308-1316, 5215-5223, 6788-6797.
- CATHD `catherine-of-siena_dialogue_thorold1896.txt`: l.3196-3202.
- CATHI `catherine-of-siena_libro-della-divina-dottrina-ita_fiorilli1912.txt`: l.14496-14516.
- COVEL `covel_some-account-of-the-present-greek-church_1722.txt`: l.178-200, 51448-51470.
- LEA3 l.29386-29393; TERESA `teresa-of-avila_interior-castle_stanbrook1912.txt` l.676-690; RICH `richental_chronik-des-constanzer-concils-gmh_buck1882.txt` l.3022-3045.
- For README lines: EHRLE1 l.27784-27800; CLAR `clareno_expositio-regulae-fratrum-minorum-lat_oliger1912.txt` l.1415-1426; GASS `cabasilas_mystik-vom-leben-in-christo-grc-deu_gass1849.txt` l.1368-1377, 1770-1788, 1880-1940; PO19 `john-ephesus_lives-eastern-saints-po19-mixed-issue_brooks1926.txt` l.1-12, 18200-18260, 23905-23922, 39860-39952.

**Quotations.** All match their files.
- Catherine brief: "But you, with your taxes and frivolities, are spoiling all that is sown." CATHL l.6796-6797.
- Catherine brief: "Come, come, come, and do not wait for time, since time does not wait for you." CATHL l.5221-5222.
- Catherine brief: "I have made a Bridge of My Word, of My only-begotten Son, and this is the truth." CATHD l.3200-3202.
- Catherine card: "her constant theme is the corruption of every rank in the hierarchy and the immediate necessity for reform." LEA3 l.29390-29392.
- Catherine and Bridget cards: "the books of St. Gertrude, St. Catharine of Siena, or St. Bridget of Sweden" TERESA l.688-689.
- Catherine card: "perhaps" CATHL l.1313.
- Bridget brief and card keyWorks: "a sleer of soules" BIRGE l.2133-2134.
- No quotation marks sit around the drafter's own English of Latin, Italian or German in either brief or card.

**Audio.** Both audio files are the brief exactly, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, two tags and nothing else (script diff). Pass.

---

### catherine-of-siena

**R2 findings: applied?**

| R2 id | Status |
|---|---|
| A2-M1 | OK. "Catherine's letters" (BIRGL l.98793-98796). |
| A2-M2 | OK. "Mansi's collection of church councils" (MANSI26 l.1; running head "VITA GREG. PAP XI", l.53417). |
| A2-M3 | OK. Duranti has his first name and role at his first card mention. |
| A2-M4 | OK. "is taken to be the first" keeps Fiorilli's "è ritenuta" (CATHI l.14506-14507). |
| A2-M5 | OK. Two sentences; COVEL l.183-184, 199, 51460-51461. |

**A3-M1 (brief para 4 and card `uncertain` 1: Gobelinus and Platina have no identifier at first mention).**
- Current brief text: "A life of Gregory in Mansi's collection of church councils says one writer, Gobelinus, credited his return to Bridget's revelations."
- Current card text: "A notice of Gregory's life in Mansi's collection of church councils names other causes: Gobelinus credits Bridget's revelations, and Platina a bishop's retort."
- What the sources give. The same Mansi volume names him "Gobelinus Paderbonensis officialis" (MANSI26 l.111555-111556), and Mansi 27 cites the same work, by age and chapter, as "Gobelinus Cosmodromius cap. 90. aetatis sextae" (MANSI27 l.132418-132419), matching "Gobelinus cap. 73. sextae aetatis" here (MANSI26 l.53404). Duranti places Platina's account "in vita ipsius Gregorii" (BIRGL l.98786-98787, 98793-98794). Mansi: "Platina scribit, quod quidam episcopus ... responderit ... eaque responsione motum pontificem reditum maturasse" (MANSI26 l.53397-53403).
- Brief replacement (±0): "A life of Gregory in Mansi's collection of church councils says Gobelinus of Paderborn credited his return to Bridget's revelations."
- Card replacement: "A notice of Gregory's life in Mansi's collection of church councils names other causes. Gobelinus of Paderborn credits Bridget's revelations. Platina, in his life of Gregory, tells of a bishop's retort that hastened the return."

**The brief as a story.** It opens on Raymond's scene at Avignon, and the who-line follows at once. The peace mission, the letters, the return and its dispute, the Dialogue, the schism and the death run in order. Para 4 weighs its witnesses in place, each named, and the new "Catherine's letters" removes the pronoun fault without a choppy run. The voice stays distinctive. No AI tell is in any changed line.

---

### bridget-of-sweden

**R2 findings: applied?**

| R2 id | Status |
|---|---|
| A2-B1 | OK. Card wording differs from the proposal, and the difference is good: it splits who says what. Her daughter's Life gives "viginti quinque annis cum matre sua" (ASMAR3 l.132892-132893); the Bollandist note to it reads "a Ergo ab anno 1348" (l.133269). Records replacement as worded, tagged Contested. |
| A2-M6 | OK. "eum" is the pope Gregory (BIRGL l.98961-98965, 98984-98989). |
| A2-M7 | OK in brief and card. "qui in linguam Latinam octo libros Reuelationum transtulit" is in Duranti's own treatise on visions (running head "DE VISIONIBVS. CAP. II.", l.11076; BIRGL l.11119-11121). |
| A2-M8 | OK. The difference ("died within a month of reaching Avignon") is right: Cumming, "died the same year, in less than a month after returning to Avignon" (BIRGE l.1023-1024), and "approved by Urban in 1370" (l.1040). The condition now names Avignon, as the heading does ("antequam rediret Auenionem", BIRGL l.98413-98414; "Si contigerit ipsum redire ad terras, vbi fuit electus Papa", l.98553-98554). The delivery is no longer told one way. |
| A2-M9 | OK. Richental l.3027-3045 reread (Candlemas eve 1415). |
| A2-M10 | OK. |
| A2-M11 | OK. |
| A2-M12 | OK. My rerun found no other year: ASJUN5 l.14878-14880 (Hemming of Åbo, d. 1307) and ASMAR3's "anno 1305" (on Clement V) give none; the only other hits are Library file headers. |
| A2-M2 (extended to this card by R2_changes) | OK. |

**A3-M2 (card `legacy.remembered` 4: Gobelinus and Platina have no identifier at first card mention).**
- Current text: "A notice of Gregory XI's life in Mansi's collection of church councils reports that Gobelinus credited his return to Rome to her revelations, conveyed to him through Alphonso. Platina, it says, gave another cause."
- Sources as in A3-M1 (MANSI26 l.111555-111556, 53397-53410; BIRGL l.98786-98787). The first sentence is 28 words after round 2.
- Replacement: "A notice of Gregory XI's life in Mansi's collection of church councils says Gobelinus of Paderborn credited his return to Rome to her revelations. They reached him through Alphonso. Platina, in his life of Gregory, gave another cause."

**The brief as a story.** It opens on the Naples vision, which now names Gregory XI, and gives the who-line in para 2. Para 4 reads cleanly after the splice: Urban comes and goes, the warning, then Cumming's two facts in one sentence with the witness inside it. "Avignon" twice in two sentences is acceptable, since the second answers the first. The close on her first call is unchanged and still works. No AI tell in any changed line.

---

### README.md

Every line changed in round 2 was checked. These hold:
- The Catherine and Bridget names lines, the Alvarez addition to the English-quotation list (TERESA l.688-689), and the Bernardino "among them" line (no Mansi left on Bernardino's card or records).
- Bernardino bullet: matches the card's second `uncertain` item ("No witness says whether these were one case").
- Clareno bullet and names line: match the card and EHRLE1 l.27788-27798 ("wie schon Papebroch berechnete") and CLAR l.1418-1424 ("propensus videtur Raynaldus ... et eam sustinet F. Tocco").
- Palamas names line: the brief has "Philotheos, a patriarch of Constantinople", the card "Philotheos, patriarch of Constantinople".
- Gregory of Sinai "prefaces": the card names two, to Gregory's book and to Philotheos of Sinai's chapters (records, PAISK l.3999).

**A3-B1 (README, Cabasilas bullet: the archbishopric is told as Widely Accepted, and a held witness who denies it is missed).** This is a Part C profile; the README line is mine, and the fault sits under it in Part C's files.
- Current README text: "How he was Nilus's nephew, whether the "Kabasilas of the sakellion" is he and which anti-Latin writings are his are tagged Contested. That he became archbishop of Thessalonica is tagged Widely Accepted, on Fabricius, Gass and a Thessalonica record; no held line gives the date."
- What the Library holds. Martin Jugie, an Assumptionist, edits Cabasilas's homilies on the Nativity, Annunciation and Dormition in Patrologia Orientalis 19 (PO19 l.18200-18222, permission to print 1925; l.39869-39878). He writes: "On a fait de lui, sans aucune preuve serieuse, le successeur de son oncle sur le siege de Thessalonique. Ni Jean Cantacuzene, ni les suscriptions des manuscrits, ni le Synodicon de l'Eglise de Thessalonique ne soufflent mot de ce titre, qui a du lui venir de ce qu'on l'a confondu souvent avec Nil" (PO19 l.39892-39895, 39914; his note cites Louis Petit's 1918 article on the Synodicon, l.39907-39908). He adds that he cannot even affirm Cabasilas was a priest (l.39914-39917).
- So a held scholar denies the archbishopric outright, and contradicts Gass's reading of the Thessalonica Synodikon (GASS l.1884-1888, 1915-1918, via Le Quien). Records cite no PO19 line (0 hits). The records tag "Widely Accepted" (records claim "Archbishop: Fabricius 'in munere successor'…"), the card's role line, the card's first `uncertain` item and brief para 5 ("Fabricius says he later succeeded his uncle as archbishop of Thessalonica. Gass agrees…") all tell a contested point as settled, or with its "no" side missing.
- README replacement: "How he was Nilus's nephew, whether the "Kabasilas of the sakellion" is he, which anti-Latin writings are his, and whether he became archbishop of Thessalonica at all are tagged Contested. Fabricius, Gass and a Thessalonica record Gass quotes make him archbishop; Martin Jugie, editing his sermons on Mary in 1926, finds no serious proof. No held line gives a date."
- Proposed for Part C's files (to be applied with Part C's round 3 recheck of Cabasilas, so the two do not collide):
  - Brief para 5, current: "Fabricius says he later succeeded his uncle as archbishop of Thessalonica. Gass agrees, and finds him named archbishop no earlier than 1354. A record of the church of Thessalonica, which Gass quotes, calls him its most holy archbishop." Replacement: "Fabricius and Gass say he later succeeded his uncle as archbishop of Thessalonica. Martin Jugie, editing his sermons on Mary in 1926, finds no serious proof of this. Jugie thinks the title came from confusing Nicholas with his uncle Nilus." (38 to 40 words, +2; the brief goes from 406 to 408, within "about 405". Gass's 1354 and the Thessalonica record stay on the card.)
  - Card `role`, current: "…archbishop of Thessalonica, by Fabricius and the Thessalonica record". Replacement: "…archbishop of Thessalonica, by Fabricius, Gass and the Thessalonica record Gass quotes, which Martin Jugie doubts".
  - Card `uncertain` 1: after "Symeon of Thessalonica praises him and names no see." insert: "Martin Jugie, editing his sermons on Mary in 1926, finds no serious proof that he succeeded Nilus. He says neither Kantakouzenos, nor the titles in the manuscripts, nor the record of the church of Thessalonica gives him that title, and he thinks it came from confusion with Nilus."
  - Card `sources.about`: add "Homélies mariales byzantines II: Nicolas Cabasilas, introduction", Martin Jugie (ed.), 1926, French and Greek, `cic/texts/john-ephesus_lives-eastern-saints-po19-mixed-issue_brooks1926.txt`.
  - Records: retag the claim "Archbishop: Fabricius 'in munere successor'…" Contested, and add Jugie's words (PO19 l.39892-39895, 39914) to its against side. In contested_claims "When he became archbishop of Thessalonica, and whether he did", add a third side: "No: Jugie, no serious proof; Kantakouzenos, the manuscript titles and the Synodicon of Thessalonica are silent on the title; it came from confusion with Nilus (PO19 l.39892-39895, 39907-39908, 39914)".

**A3-M3 (README para 3: the word, grade and Flesch ranges are stale after round 2).**
- Current text: "The briefs run 403 to 406 words, about 2:30; … `grade_text` scores them at grade 6.6 to 8.6 and Flesch Reading Ease 61.4 to 72.5."
- At e072b50d: 405 to 407 words; FK 6.76 to 8.59; Flesch 61.45 to 71.72 (Grades, below). R2 asked for the recompute, and R2_changes does not record it.
- Replacement, at e072b50d: "The briefs run 405 to 407 words, about 2:30; … `grade_text` scores them at grade 6.8 to 8.6 and Flesch Reading Ease 61.5 to 71.7." Recompute once more after round 3's fixes. With A3-M1 and the proposed Cabasilas para 5, the word range becomes 405 to 408.

**Not applied, by the coordinator's call (A2-M13).** "an era 6 entry is registered with this batch" is still untrue on the branch until the Open-Gaps entry exists. This is a pre-merge condition, not a new finding.

**A2-M14 and A2-M15.** A2-M14 was correctly left alone: C2-M6 already fixed the tag wording, and A3-B1 now supersedes the line. A2-M15 is applied as worded.

---

### records.json (these profiles)

- **catherine-of-siena.** No records entry changed in round 2. With A3-M1, add to the Gobelinus/Mansi claim: "Gobelinus Paderbonensis officialis (MANSI26 l.111555-111556); Platina 'in vita ipsius Gregorii' (BIRGL l.98786-98787)".
- **bridget-of-sweden.** The three round 2 changes hold: the Montefiascone claim with Duranti's two places and Cumming's death line (BIRGL l.98600-98609; BIRGE l.1022-1024), the Rome claim (Contested), and the birth-year note. One small citation slip: the Rome claim cites BIRGE l.955-961, and l.955 is blank, so the range should be l.956-961. With A3-M2, add the same Gobelinus and Platina witnesses to the claim "Gobelinus, in Mansi's notice of Gregory XI…".

### Checklist summary

| # | Item | catherine-of-siena | bridget-of-sweden |
|---|---|---|---|
| 1 | Each sentence's source establishes it | Pass | Pass |
| 2 | Quotes verbatim | Pass | Pass |
| 3 | Nothing invented | Pass | Pass |
| 4 | Reading aids, no AI tells | Pass | Pass |
| 5 | No role standing in for a witness | Pass | Pass |
| 6 | Partisan or hostile witness marked | Pass | Pass |
| 7 | Contested claims show both sides by name | Pass | Pass |
| 8 | Common names and scholars identified at first mention | Fail, minor (A3-M1) | Fail, minor (A3-M2) |
| 9 | One term for one thing | Pass | Pass |
| 10 | Story, scene opening, disputes in place, length | Pass | Pass |
| 11 | `grade_text` (FK ≤ 10, Flesch ≥ 60) | Pass (6.76, 71.72) | Pass (6.85, 68.68) |
| 12 | Card order, missing fields absent, caveat repeated | Pass | Pass |
| 13 | Audio tags only in the audio script, placed right | Pass | Pass |
| 14 | Keeps list line; Who test | Pass | Pass |

Card form for both: fields are in the pattern's order (name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources). `briefLength` is "about 2 minutes 30 seconds", the house form of the era 6 cards, and it fits 405 words for each (`wc -w`). Audio exact. Sources list every work each brief relies on. ownWords holds only the subject's own texts, with the editors' notes named in the titles. keyWorks are two (Catherine) and three (Bridget).

### Grades

| Profile | Words | FK | Flesch |
|---|---|---|---|
| catherine-of-siena (now, and with A3-M1) | 405 | 6.76 | 71.72 |
| bridget-of-sweden (now; A3-M2 is card only) | 405 | 6.85 | 68.68 |

All eight briefs at e072b50d: angelo-clareno 406, 8.16, 62.55; bernardino-of-siena 405, 7.21, 69.87; gregory-of-sinai 406, 8.59, 63.48; gregory-palamas 407, 7.77, 63.26; nicholas-cabasilas 406, 7.99, 61.45; william-of-ockham 405, 8.07, 63.19.

### Count

- catherine-of-siena: 0 blocking, 1 minor (A3-M1).
- bridget-of-sweden: 0 blocking, 1 minor (A3-M2).
- README.md: 1 blocking (A3-B1, which reaches Part C's Cabasilas brief, card and records), 1 minor (A3-M3).
- Part A total: 1 blocking, 3 minor.

## Era 6 Who batch 2, round 3 recheck: PART B

**Scope.** `bernardino-of-siena` and `angelo-clareno`. A targeted recheck of round 2 Part B (R2_review.md, "PART B"; R2_changes.md, "Part B") against `git diff d7c4490c..e072b50d` for both briefs, both cards, both audio scripts, their `records.json` entries and the README lines about them. Branch `claude/cft-who-era6-batch2`. No repo file was edited. No web, paid or model call was made.

**Method.** Read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` with its checklist, and lessons.md. Every changed line was read against its cited source with 20 or more lines of context, asking what each note annotates, who speaks, and whether a hedge or condition was dropped. Every quotation in double quotes in both briefs and cards was checked by eye against its file. The audio scripts were rebuilt from the briefs (`[calmly] ` on the first paragraph, `[warmly] ` on the last) and compared as strings. The briefs were scored with `engine.m1.gates.grade_text`, words counted with `wc -w`, and sentence lengths counted by script. Ehrle's weekday reckoning was checked by computing the Julian Easter for 1250 to 1400 (see B3-B1). "Daniel Papebroch" was searched across `cic/texts/` (held as "Daniel Papebrochius" in EHRLE1 and three Acta Sanctorum files). No changed line adds a new "no", "only", "alone" or absence of the narrator's own; the one "only" in a changed line ("only in 1317, 1337 and 1348") is Ehrle's "nur".

**Files opened (cic/texts/).** ORL = `bernardino-of-siena_sermons_orlandi-robins1920.txt` (l.5818-5836, 6836-6864); BANCHI1 = `bernardino-of-siena_prediche-volgari-1427-v1-ita_banchi1880.txt` (l.312-326, 1138-1166, 6398-6416); GLASS = `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt` (l.92-112, 20684-20714, 21722-21745); LEA3 = `lea_history-of-the-inquisition-of-the-middle-ages-v3_1888.txt` (l.8170-8232, 3333-3340); EHRLE1 = `ehrle-denifle_archiv-literatur-kirchengeschichte-mittelalters-bd1-deu-lat_1885.txt` (l.27760-27800, 27850-27875, 28486-28494); EHRLE2 = `…-bd2-deu-lat_1886.txt` (l.5818-5836, 5856); EHRLE3 = `…-bd3-deu-lat_1887.txt` (l.22694-22708); CLAR = `clareno_expositio-regulae-fratrum-minorum-lat_oliger1912.txt` (l.1390-1400, 1414-1426); CARLINI = `carlini_fra-michelino-e-la-sua-eresia-ita-lat_1912.txt` (l.1455-1466); PG88 = `dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt` (l.43278-43310); SABAT = `speculum-perfectionis_speculum-perfectionis-lat_sabatier1898.txt` (search, l.2510).

### Quotations

All four quotations in double quotes match their files.
- Bernardino brief: "Chew, and chew, it would not go down!" matches ORL l.6860 ("chew it. Chew, and chew, it would not go down!"), the "!" included.
- Bernardino brief: "and we shall see what I have said that is wrong. I am one of those who wish to hold to that which Holy Church doth hold." matches ORL l.5832-5834 ("write it to me, and we shall see what I have said that is / wrong. I am one of those who wish to hold to that which / Holy Chureh doth hold."), with the allowed OCR reading "Chureh".
- Bernardino card: "who counts as the formal founder of the Observantines" matches LEA3 l.8229-8230.
- Clareno card: "a man of the firmest and gentlest spirit" matches LEA3 l.3337-3338.
- The Clareno brief has no quotation marks.

---

### bernardino-of-siena

**R2 findings: applied?**

| R2 id | Result |
|---|---|
| B2-B1 | OK. "He was sent to preach at L'Aquila, and in May 1444 he fell ill and died." Vespasiano gives no month for the sending (BANCHI1 l.1150-1157); the month and year are Glassberger's for the death ("XX. die Maii … in civitate Aquila … reddidit sanctus Bernardinus Christo animam suam", GLASS l.21739-21742). Vespasiano has him fall ill and die "in pochi dì" (l.1155), so the illness in May stands. Word count unchanged (405). |
| B2-M1 | OK. GLASS l.95-97 reads "Filius fuit reformatae familiae Ordinis Minorum, quae nuncupatur de regulari Observantia"; LEA3 l.8223-8224 reads "the Observantines, or Franciscans of strict observance". The LEA3 lines are Lea's own narrative (the quotation mark at l.8225 is OCR for a footnote marker; no opening mark in l.8170-8224). |
| B2-M2 | OK. "decretum sacri concilii Constantiensis in favorem Fratrum de Observantia editum" (GLASS l.20697-20698). The rest of the sentence still matches l.20703-20712. |
| B2-M3 | OK (card title and README line both drop Mansi). |
| B2-M4 | OK (README line 11). |
| Records point (date of the Roman hearing) | OK. BANCHI1 l.6410-6412: "era stato eletto vescovo di Siena da papa Martino V il 4 giugno del 1427", joined to l.320-326 ("chiamato a difendere … i suoi insegnamenti … il papa lo promosse al vescovado"). |

**New findings.** None. The changed lines say what their sources say, and the brief still opens on the sow-thistle scene and reads straight across the para 6 splice.

---

### angelo-clareno

**R2 findings: applied?**

| R2 id | Result |
|---|---|
| B2-B2 | OK. "Not long before his death, Ehrle thinks, the old man went to a hermitage in the Basilicata, in the south, and died there in June 1337." Ehrle's text (EHRLE1 l.27770-27774) and his hedging note (l.27785-27787, "Dies glaube ich daraus entnehmen zu können, dass der Cölestinerprior fr. Thomas Anglicus ihn als 'peregrinus et ignotus' bezeichnet") are read correctly; the witness now covers the move and the year. Oliger's earlier, hedged move to the Basilicata (CLAR l.1396-1398) is to a different hermitage and does not conflict with a sentence given as Ehrle's. |
| B2-B3 | OK in card, records side and README. "propensus videtur Raynaldus … et eam sustinet F. Tocco" (CLAR l.1423-1424); "Eubel dubitat" (l.1423); "non liquet" (l.1421-1422). |
| B2-M1 | OK. "de sue regule observantia credidit" (EHRLE1 l.27866) is now "believed about keeping his rule"; "Hanc heresim me habuisse semper et me nunc habere confiteor" (l.27868) is the fronted "that heresy … he had always held and held still". 27 words, as R2 accepted. |
| B2-M2 | Applied, but the shared wording drops a condition from Ehrle's note (B3-B1). R2_changes' own difference in `dates` ("from a note dated by weekday and the years in which … that weekday fell on 13 June") is clearer than R2's proposal and is not itself the fault. |
| B2-M3 | OK. "Felice Tocco" is held (CARLINI l.1460-1461, OCR "FeLIcE"; SABAT l.2510), and Ehrle's "Prof. F. Tocco" (EHRLE3 l.22702-22703) and Oliger's "F. Tocco, Studii Franc." (CLAR l.1424) write on the same Franciscan question. |
| B2-M4 | Applied. "describes him past mistaking" is true to "ita tamen describit et depingit illum, ut res oculis tangi possit" (PG88 l.43306-43307), but the idiom is hard going at B2 (B3-M1). |
| B2-M5 | OK (CLAR l.1398-1399; EHRLE1 l.27774). |
| B2-M6 | OK. |
| Records point (Robert of Mileto) | OK. EHRLE1 l.28490-28492: "Infrascripta misit dominus Bubertus [Rubertus] de Mileto Gentili (de Fulgineo) modico tempore post obitum fr. Angeli de Glarino". |

**B3-B1 (card `dates`, card `uncertain` "When he died", records: "that weekday" drops "after Pentecost").**
- Current text, `dates`: "The year is Ehrle's reckoning, from a note dated by weekday and the years in which Daniel Papebroch, a Bollandist, had found that weekday fell on 13 June."
- Current text, `uncertain`: "When he died. Ehrle fixed 1337 from a note at the end of the list of his miracles, dated by weekday. Daniel Papebroch, a Bollandist, had already found that in the first half of the fourteenth century that weekday fell on 13 June only in 1317, 1337 and 1348."
- Current text, records claim "Ehrle's reckoning of the year": "… in the first half of the fourteenth century that weekday fell on 13 June only in 1317, 1337 and 1348 …".
- Source: the note is dated "feria VI infra octavam pentecostes scil. festo s. Antonii" (EHRLE1 l.27791-27792, OCR "Philippns … octaram"), that is, the Friday within the octave of Pentecost, namely the feast of Saint Anthony. Ehrle: "Nun fiel aber, wie schon Papebroch berechnete, diese fer. VI … nur in den J. 1317, 1337 und 1348 auf den 13. Juni, das Fest des hl. Antonius" (l.27792-27795, OCR "18. Jani"). The count is for "this Friday", the one after Pentecost. As the card reads, a listener takes "that weekday" to mean a plain Friday, and a plain Friday falls on 13 June in many more years than three in fifty. The condition that makes the reckoning work is dropped, so the card misstates Ehrle's method. (A Julian Easter computation gives the Friday after Pentecost on 13 June in 1337 and 1348 but not in 1317, so Ehrle's "1317" is either his or the scan's slip. The card already gives the list as Papebroch's finding through Ehrle, and should keep it as printed; no change is proposed for the year list.)
- Fix, `dates`: "The year is Ehrle's reckoning, from a note dated to the Friday after Pentecost, which was also the feast of Saint Anthony, 13 June. Daniel Papebroch, a Bollandist, had found the years in which that Friday fell on 13 June."
- Fix, `uncertain`, first two sentences after "When he died.": "Ehrle fixed 1337 from a note at the end of the list of his miracles, dated to the Friday after Pentecost and the feast of Saint Anthony, 13 June. Daniel Papebroch, a Bollandist, had already found that in the first half of the fourteenth century the Friday after Pentecost fell on 13 June only in 1317, 1337 and 1348." (The rest of the item is unchanged.)
- Fix, records: in the claim "Ehrle's reckoning of the year", replace "that weekday fell on 13 June" with "this Friday after Pentecost ('diese fer. VI') fell on 13 June".

**B3-M1 (card `legacy.traces`, Rader: an idiom hard for a B2 reader).**
- Current text: "Ambrose does not name him, Rader says, but describes him past mistaking."
- Source: "et quamvis Angeli nomen non exprimat, ita tamen describit et depingit illum, ut res oculis tangi possit" (PG88 l.43306-43307).
- Fix: "Rader grants that Ambrose does not give his name, and says the description makes plain who is meant."

**B3-M2 (card `uncertain`, authorship item: a name with no context, in the sentence R2 changed).**
- Current text: "… and Ehrle reports doubts from Richard and from Professor Felice Tocco."
- Source: Ehrle, "Richard 1) schliesst sich blindlings den erwähnten Zweifeln Affós an" (EHRLE2 l.5822-5823, OCR "Richard!)"), with note 1, "Bibl. de l'école des Chartes 1884, XLV, 528s." (l.5856). A listener has nothing to place "Richard" by.
- Fix: "… and Ehrle reports doubts from Richard, writing in 1884, and from Professor Felice Tocco."

**B3-M3 (README line 12: the same dropped condition as B3-B1).**
- Current text: "His death year is Ehrle's reckoning, using Papebroch's list of the years the weekday fits, and the card says so; the Bollandists give 14 June for the day."
- Source: EHRLE1 l.27791-27795, as in B3-B1.
- Fix: "His death year is Ehrle's reckoning, using Papebroch's list of the years in which the Friday after Pentecost fell on 13 June, and the card says so; the Bollandists give 14 June for the day."

Brief as a story: it still opens on the Avignon hearing, places Angelo within the first lines of paragraph two, and the para 4 and para 5 splices read cleanly. No new finding in the brief.

---

### records.json (these profiles)

- **bernardino-of-siena.** The Observance claim (GLASS l.95-110; LEA3 l.8223-8224) and the Roman-hearing side with BANCHI1 l.6410-6412 were opened and say what the entries quote. No fault.
- **angelo-clareno.** The death claim with Ehrle's hedge (EHRLE1 l.27785-27786; CLAR l.1394-1399), the 1331 claim and side (CLAR l.1417-1424; EHRLE3 l.22702; CARLINI l.1461) and the Bollandists claim with Robert of Mileto (EHRLE1 l.28490-28492) were opened and stand. One change is needed in the claim "Ehrle's reckoning of the year" (B3-B1). Small point, no change asked: the Bollandists claim's `witness` field still lists only ASMAR3 although its text now also cites EHRLE1 l.27789-27790 and l.28490-28492 inline.

### Checklist summary

| # | Item | bernardino-of-siena | angelo-clareno |
|---|---|---|---|
| 1 | Each sentence's source establishes it | Pass | Fail (B3-B1) |
| 2 | Quotes verbatim | Pass | Pass |
| 3 | No invented detail | Pass | Pass |
| 4 | Reading aids, no AI tells | Pass | Pass (B3-M1 is an idiom; B3-M2 an unplaced name) |
| 5 | No role for a named witness | Pass | Pass |
| 6 | Partisan or hostile witness marked | Pass | Pass |
| 7 | Contested claims shown both sides | Pass | Pass |
| 8 | Common names have a place | Pass | Pass |
| 9 | One term for one thing | Pass | Pass |
| 10 | Story, scene first, disputes in place, length | Pass | Pass |
| 11 | `grade_text` | Pass | Pass |
| 12 | Card order, missing fields, caveat repeated | Pass | Pass |
| 13 | Audio tags | Pass (string match) | Pass (string match) |
| 14 | List line kept; Who test | Pass | Pass |

Card form: both cards are in the pattern's field order (name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources). Each `briefLength` reads "about 2 minutes 30 seconds", the form all era cards use for briefs near 405 words (97 cards). `keyWorks` has two and three entries. `ownWords` holds only the subject's words (the History marked "attributed"). `sources` lists every work the briefs rely on.

### Grades

| Brief | Words (`wc -w`) | FK | Flesch | Sentences over 25 words |
|---|---|---|---|---|
| bernardino-of-siena | 405 | 7.21 | 69.87 | one (26, the closing line, counted to the full stop inside the quotation) |
| angelo-clareno | 406 | 8.16 | 62.55 | three (26, 27, 26) |

No proposed fix touches a brief, so the grades stand. Both sit inside the README's ranges (403 to 406 words; grade 6.6 to 8.6; Flesch 61.4 to 72.5).

### Count

- **bernardino-of-siena:** 0 blocking, 0 minor.
- **angelo-clareno:** 1 blocking (B3-B1), 3 minor (B3-M1 to B3-M3).

## Era 6 Who batch 2, round 3 recheck: PART C

**Scope.** `william-of-ockham` and `nicholas-cabasilas`. Covered: every round 2 Part C finding (R2_review.md, PART C), every difference R2_changes.md lists for Part C, every line changed in `git diff d7c4490c..e072b50d` for the two briefs, cards, audio scripts, their `records.json` entries and the README lines about them. Every double-quoted passage in both briefs and cards was checked again, and the card form (item 6) was checked whole. Also judged: the open call in R2_changes.md's last line, which kept the Cabasilas contested claim. Branch `claude/cft-who-era6-batch2` at e072b50d. No repo file was edited. No web, paid or model call was made.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md`, lessons.md, R2 PART C and R2_changes Part C. Then I read the word diff for these two people. For every changed line I opened the cited source with 20 or more lines of context. I asked who is speaking, what the line annotates, and whether a condition or hedge was dropped. For the Cabasilas archbishop lines this meant reading Gass from l.1364 to 1395 and l.1765 to 1800 as continuous text, and the Synodikon footnote at l.1919 to 1940. Quotations were matched by grep and sed (whitespace, case and hyphen breaks allowed). I searched the 34 Cabasil-/Kabasil-/Καβάσιλ- files for "Synodic" and for any Thessalonica metropolitan heading that names Nicholas with a surname. Audio was compared by script, with the two tags removed. `grade_text` was run on both current briefs and on the Cabasilas brief with this round's fix. On spelling: the profiles' own prose follows the Decision-Log rule (American), as R2 noted. No British form was found in either profile's own prose.

**Files opened (cic/texts/).**
- BUL5 `bullarium-franciscanum_v5-lat_eubel1898.txt`, l.60-80, 3444-3458, 42504-42516.
- SCHOLZ `scholz_unbekannte-kirchenpolitische-streitschriften-v2-lat_1914.txt`, l.25845-25870.
- CARL `carlini_fra-michelino-e-la-sua-eresia-ita-lat_1912.txt`, l.190-199, 6260-6285.
- GERSON `gerson_opera-omnia-tomus-2-pars-1-tractatus-ad-schisma-lat_dupin1706.txt`, l.26990-27030, 27185-27215.
- LEA3 `lea_history-of-the-inquisition-of-the-middle-ages-v3_1888.txt`, l.6808-6856.
- FZ `fasciculi-zizaniorum_shirley1858.txt`, l.3076-3086.
- LUTHER4 `luther_works-v4-selected_various1931.txt`, l.16772-16780.
- CANT3 `cantacuzenus_historiarum-libri-iv-v3-grc-lat_schopen1832.txt`, l.16586-16635.
- PG150 `palamas_opera-omnia-pg150-grc-lat_migne1865.txt`, l.343-346, 26062-26074, 36555-36600.
- GASS `cabasilas_mystik-vom-leben-in-christo-grc-deu_gass1849.txt`, l.1340-1395, 1765-1800, 1872-1942.
- PO15 `patrologia-orientalis-tomus15_petit-documents-concile-de-florence-purgatoire-grc-fra_graffin-nau1927.txt`, l.1, 10, 97, 505-520, 580-645.
- GREG2 `gregoras_byzantina-historia-v2-grc-lat_schopen1830.txt`, l.1, 166-170, 36466-36474, 47122-47140.
- PG155 `symeon-thessalonica_opera-omnia-pg155-grc-lat_migne1866.txt`, l.378-400.
- PG160 `gennadius-scholarius_opera-omnia-pg160-grc-lat_migne1866.txt`, l.49384 (grep hit only).

**Quotations.** These are all the double-quoted passages in both briefs and both cards.
- Ockham brief, "there was nothing sure but Scripture": LEA3 l.6825, "There  was  nothing  sure  but  Scripture ;". It differs only in case. Pass.
- Ockham brief, "the glory and the reproach of his order": FZ l.3081-3082, "Ockham,  the  glory / and  the  reproach  of  his  order,". Pass.
- Ockham card, legacy remembered, "the glory and the reproach of his order": FZ l.3081-3082, as above. Pass.
- Ockham card, legacy traces, "Occam, my dear master": LUTHER4 l.16777, "Occam, my dear master, writes". Pass.
- Ockham card, uncertain, "more than doubtful": LEA3 l.6851, "but  this  is  more  than  doubtful,". Pass.
- Cabasilas brief and card: no double quotes (checked by grep). Pass.

**Audio.** Both scripts equal their brief, with `[calmly] ` at the start, `[warmly] ` at the start of the last paragraph, and no other tag (checked by script). Pass for both. The Cabasilas fix below needs the audio rebuilt.

---

### william-of-ockham

**R2 findings: applied?**

| R2 id | Status |
|---|---|
| C2-M1 (Eubel "editor of 1898") | OK. "who edited the papal letters in 1898" (BUL5 l.70-77). Eubel's note is at l.42506-42512. |
| C2-M2 ("walked into persecution") | OK. "Persecutioni igitur scienter me ingerens" (SCHOLZ l.25858-25859). The records note was changed to match. |
| C2-M3 (knownFor "he" reads as Lea) | OK. The line is held at LEA3 l.6820-6822. |
| C2-M4 ("he notes" reads as Lea) | OK. The note is Carlini's (CARL l.6278-6280). |
| C2-M5 (Gerson, 39 words) | OK. The Monitum dates it ("Anno 1418 ... sub finem Concilii Constantiensis occasione appellationis Oratorum Polonorum ad futurum Concilium", GERSON l.27010-27013). The title is "an liceat in causis Fidei a Summo Pontifice appellare" (l.26996-27002). "Hanc autem materiam ... fundavit Ockam in Dialogo suo" comes straight after "Concilium appello" (l.27198-27206), so "the matter" is the appeal. "He" is Gerson. |
| C2-M6 (title-page witnesses) | OK. BUL5 l.70-77 ("CONRADO EUBEL ... ROMAE, MDCCCXCVIII") and CARL l.195-198 ("BOLOGNA ... 1912."). |
| Optional arrest-letters heading | OK. BUL5 l.3451-3455 ("Marchionem de Baden aliosque nobiles"; "Episcopos Angliae"). |
| C-M14 carry-over (Müller to the Open-Gaps entry) | Not done. A grep of Build/Ministry finds no gap entry for Müller or Nicolaus Minorita. This is the coordinator's task. It is not counted here. |

No new findings. Every changed line reads as its source says. The brief still opens on the night flight. It reads as one story after the splices, with the witness inside each sentence it covers.

---

### nicholas-cabasilas

**R2 findings: applied?**

| R2 id | Status |
|---|---|
| C2-B1 (who-line inside Kantakouzenos's attribution) | OK. "He was still a layman, John Kantakouzenos writes in his history" matches "Νικόλαον τὸν Καβάσιλαν, ὄντα ἔτι ἰδιώτην" and "privatum adhuc" (CANT3 l.16599-16601, 16629). The scene still opens the brief. |
| C2-B2 (1353 in Gass's mouth) | OK. "only some years after the synod of 1351" matches "von wo ihn dieser zur Theilnahme an der vierten Synode ... berief (1351) ... Muthmasslich wird also Cabasilas erst nach einigen Jahren das Erzbisthum angetreten haben" (GASS l.1773-1784). |
| C2-M1 ("he" heard as Gass) | OK. |
| C2-M2 (Gass's hedge on the wrong point) | Wrongly applied. "Gass agrees" makes Gass endorse Fabricius's succession, and Gass puts Palamas between the two. See C3-B1. |
| C2-M3 ("God came down", heard as the narrator's) | OK. PG150 l.36579-36582. The "not X; Y" shape is the source's own οὐ ... ἀλλ᾽, and it is told as his words. |
| C2-M4 (Mark gloss; Petit) | OK, and the difference is good. "Only two ... charged with answering" keeps Petit's "ces deux prelats avaient seuls recu mission de re-pondre aux Latins" (PO15 l.637-638, OCR "r6- pondre"). The setting is the Ferrara purgatory debate (PO15 l.97, 615-645). Card item 5 was shortened as proposed. |
| C2-M5 (Boivin "edited") | OK. GREG2 l.1, 168; the note "Nicolaus scilicet" is signed "BOIVIN" (OCR "soiviw", l.47125-47134). |
| C2-M6 (README against the tag) | The splitting is fine. The "Thessalonica record" wording carries the fault in C3-B2. |
| C2-M7 (1865 witness) | OK. |
| C2-M8 (Fabricius notice moved out of ownWords) | OK. The new "about" entry is correct. |

**C3-B1 (brief para 5: "Gass agrees" with a succession Gass contradicts).**
- Current text: "Fabricius says he later succeeded his uncle as archbishop of Thessalonica. Gass agrees, and finds him named archbishop no earlier than 1354."
- Source: Fabricius says "ejusdemque, defuncti vita, in munere successor fuit" (PG150 l.26071-26072), meaning Nilus's successor once Nilus had died. Gass says "verwaltete dasselbe Amt zehn Jahr nachher (nach 1350), so das[s] zwischen Beide nur die bischöfliche Regierung des Gregorius Palamas ... fällt" (GASS l.1374-1377, OCR "bischuf- liche Regierang", "föUt"). That is: he held the same office ten years later, so that only the episcopal rule of Gregory Palamas falls between the two. Gass therefore does not agree that Nicholas succeeded his uncle. He puts Palamas between them, and puts Nicholas's start only some years after 1351 (l.1782-1784). R2 read l.1374-1375 as "the succession plainly", but the same sentence goes on to place Palamas between the two. The round 2 wording ("agrees") turned this into a direct misstatement of the witness.
- Fix (brief): see the combined replacement under C3-B2.
- Fix (card, uncertain item 1): see the combined replacement under C3-B2. It sets the two witnesses side by side.
- Fix (records, the claim "Archbishop: ..."): after "'Jedenfalls wird er nicht vor 1354 als Erzbischof genannt'" insert "; on the order, 'so dass zwischen Beide nur die bischöfliche Regierung des Gregorius Palamas ... fällt' (OCR 'bischuf- liche Regierang', 'föUt')". In the witness, change "GASS (...) l.1373-1375, 1781-1785" to "GASS (...) l.1373-1377, 1773-1786".

**C3-B2 (brief, card, README: the Thessalonica record names only a Nicholas, and the identification is Gass's).**
- Current brief text: "A record of the church of Thessalonica, which Gass quotes, calls him its most holy archbishop."
- Current card text, uncertain item 1: "A record of the church of Thessalonica, quoted by Gass, calls him its most holy metropolitan."
- Current card text, role: "archbishop of Thessalonica, by Fabricius and the Thessalonica record".
- Current README text: "That he became archbishop of Thessalonica is tagged Widely Accepted, on Fabricius, Gass and a Thessalonica record; no held line gives the date."
- Source: the Synodikon line that Gass quotes from Le Quien reads "Νικολάου τοῦ ἁγιωτάτου μητροπολίτου Θεσσαλονίκης τοῦ λόγοις ἅμα καὶ ἔργοις καὶ θείοις συγγράμμασιν ἀγωνισαμένου ὑπὲρ τῆς ἐκκλησίας Χριστοῦ ... αἰωνία ἡ μνήμη" (GASS l.1919-1938, OCR heavily garbled). It gives a first name, Nicholas, and no surname. Gass reads it as Cabasilas: "ein Zeugniss aus dem Synodicon der Kirche von Thessalonich, dass er nämlich ... gekämpft habe" (GASS l.1884-1888). No other held file carries this Synodikon entry. The PG155 Synodikon note at l.393-395 is Symeon's own elogium. The brief and card tell the identification as the record's own words. The card treats the same kind of identification as uncertain elsewhere: the "Kabasilas of the sakellion" item and Gregoras's friend, where Boivin and Gass "take him for Nicholas". This is an editor's identification told as settled.
- Fix, brief para 5 (combined with C3-B1). Replace "Gass agrees, and finds him named archbishop no earlier than 1354. A record of the church of Thessalonica, which Gass quotes, calls him its most holy archbishop." with: "Gass finds him named archbishop no earlier than 1354. He takes him for the Nicholas whom a record of the church of Thessalonica calls its most holy archbishop."
  - The brief goes from 406 to 407 words, which is still about 2:30. FK is 8.02 and Flesch 61.33 (scored on a copy).
  - "He" is Gass, the subject of the sentence before; "him" is Cabasilas.
  - "Takes him for" is the card's own form for identifications.
- Fix, card uncertain item 1 (whole item; it also carries C3-B1 and C3-M1): "When he became archbishop of Thessalonica. Fabricius says he succeeded his uncle Nilus in that office after Nilus died, and Migne heads him as metropolitan of Thessalonica. Gass puts Gregory Palamas in the see between uncle and nephew. Gass presumes Nicholas took it only some years after the synod of 1351, and finds him named archbishop no earlier than 1354. A record of the church of Thessalonica, quoted by Gass, calls a Nicholas its most holy metropolitan, and Gass takes him for Cabasilas. Kantakouzenos calls him still a layman in 1353. Symeon of Thessalonica praises him and names no see. No witness gives the date or tells how he took office."
- Fix, card role: change "archbishop of Thessalonica, by Fabricius and the Thessalonica record" to "archbishop of Thessalonica, by Fabricius and Gass".
- Fix, README line 16. Replace "How he was Nilus's nephew, whether the "Kabasilas of the sakellion" is he and which anti-Latin writings are his are tagged Contested. That he became archbishop of Thessalonica is tagged Widely Accepted, on Fabricius, Gass and a Thessalonica record; no held line gives the date." with: "When he took the see of Thessalonica, how he was Nilus's nephew, whether the "Kabasilas of the sakellion" is he and which anti-Latin writings are his are tagged Contested. Fabricius has him follow his uncle, and Gass puts Gregory Palamas between them. That he became archbishop is tagged Widely Accepted, on Fabricius and Gass. The Thessalonica record names only a Nicholas, whom Gass takes for him, and no held line gives the date."
- Fix, records, the claim "Archbishop: ...". Change "the Synodikon of the church of Thessalonica, quoted by Gass from Le Quien, 'Νικολάου τοῦ ἁγιωτάτου μητροπολίτου Θεσσαλονίκης ... αἰωνία ἡ μνήμη'" to "the Synodikon of the church of Thessalonica, quoted by Gass from Le Quien, 'Νικολάου τοῦ ἁγιωτάτου μητροπολίτου Θεσσαλονίκης ... αἰωνία ἡ μνήμη', a first name with no surname, which Gass reads as Cabasilas ('dass er nämlich ... gekämpft habe')". In the same claim, change "Against or silent:" to "Bounds and silence:", since no held line argues against the see.

**C3-M1 (the open call: the Cabasilas contested claim kept; the card heading "and whether he did").**
- My judgment: keep the `contested_claims` entry, but only for "when". With C3-B1 it now has two real held sides: Fabricius (direct successor once Nilus died) and Gass (after Palamas, only some years after 1351, not named before 1354). The "whether" half has no held doubt. Its second side is "a date and a silence": Kantakouzenos's "still a layman" in 1353 sets an earliest date and does not deny a later see, and Symeon simply names no see. R1 and R2 found no line in the 34 files that says he never held the see. The absent_details note says so too. A heading that asks "whether he did" therefore raises a doubt no witness gives. The README's Widely Accepted tag is the right tag for the "whether".
- Current records entry: claim "When he became archbishop of Thessalonica, and whether he did". Sides: "Yes: Fabricius ...; Migne's heading ...; Gass, presuming ...; the Thessalonica Synodikon via Le Quien ..." and "A date and a silence: ...".
- Fix, records `contested_claims` entry (whole entry):
  - claim: "When he became archbishop of Thessalonica"
  - sides:
    - "Fabricius: his uncle Nilus's successor in office once Nilus had died, 'defuncti vita, in munere successor' (PG150 l.26071-26072); Migne heads him metropolitan of Thessalonica (PG150 l.343-346)"
    - "Gass: Gregory Palamas held the see between uncle and nephew (GASS l.1374-1377); Nicholas presumably took it only some years after the synod of 1351, and is not named archbishop before 1354 (GASS l.1773-1786)"
- Kantakouzenos's 1353 layman line and Symeon's silence stay in the "Archbishop" claim under "Bounds and silence" (C3-B2), and on the card.
- Fix, card: the heading change is made in the C3-B2 replacement of item 1 ("When he became archbishop of Thessalonica.").

**Checked and true (changed lines).**
- The split who-line (CANT3 l.16595-16601, 16628-16630).
- "Cabasilas wrote in his book of that name" (PG150 l.35858-35860).
- "People did not go up to God, he wrote; God came down to them" (PG150 l.36579-36582).
- Card item 1's "only some years after the synod of 1351" (GASS l.1773-1784).
- Card item 4's Boivin notes (GREG2 l.47125-47134).
- Card item 5's shortened Petit sentence, whose role now comes first in legacy (PO15 l.513-517, 630-640).
- The legacy trace on Petit, Mark and Bessarion (PO15 l.633-638).
- The new "about" entry for Fabricius's notice (PG150 l.26062-26072).
- The records 1865 line (PG161 l.110885; PG150 l.261, as R2 cited).

**Not counted.** PG160 l.49384 heads a work "Auctore Nicolao Cabasila Thessalonicensi metropolita". It is another Migne heading on the same side as PG150 l.343-346, and it is not needed.

---

### records.json (these profiles)

- **william-of-ockham.** Every changed entry reads as cited: the title-page witnesses (BUL5 l.70-77; CARL l.195-198), the arrest-letters heading (BUL5 l.3451-3455) and the tract note's "walked into persecution" (SCHOLZ l.25858-25859). Nothing further.
- **nicholas-cabasilas.**
  - C3-B1: add Gass's line placing Palamas between uncle and nephew to the "Archbishop" claim, and widen the GASS lines.
  - C3-B2: mark the Synodikon as naming only a Nicholas, with Gass's identification, and relabel "Against or silent" as "Bounds and silence".
  - C3-M1: the contested entry becomes "When he became archbishop of Thessalonica", with Fabricius and Gass as its two sides.
  - The new Petit claim (PO15 l.627-641) reads as cited. Its quotation normalizes the OCR "r6- pondre" to "repondre", which is within the hyphen allowance.

### Checklist summary

| # | Item | william-of-ockham | nicholas-cabasilas |
|---|---|---|---|
| 1 | Each sentence sourced, source establishes it | Pass | Fail (C3-B1, C3-B2) |
| 2 | Quotes verbatim | Pass (5 checked) | Pass (none) |
| 3 | No invented detail | Pass | Pass |
| 4 | Reading aids, no AI tells | Pass | Pass |
| 5 | No role standing in for a witness | Pass | Pass |
| 6 | Partisan or hostile witness marked | Pass | Pass |
| 7 | Contested claims both sides, not settled | Pass | Fail (C3-B2: an identification told as settled; C3-M1: a heading with one real side) |
| 8 | Common names and scholars at first mention | Pass (Müller still awaits the gap log; coordinator) | Pass |
| 9 | One term for one thing | Pass | Pass |
| 10 | Story, scene, disputes in place, length | Pass | Pass (scene first; who-line at sentence 3) |
| 11 | Readability | Pass (8.07 / 63.19) | Pass (7.99 / 61.45; 8.02 / 61.33 with the fix) |
| 12 | Card order, missing fields absent, caveat repeated | Pass | Pass |
| 13 | Audio tags only in the script, at start and close | Pass | Pass (rebuild after the fix) |
| 14 | Keeps the list line; Who test | Pass | Pass |

Card form (item 6), both profiles:
- Field order is name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources, as in the pattern.
- keyWorks has three entries in each.
- briefLength is "about 2 minutes 30 seconds", which matches 405 and 406 words (407 after the fix).
- Sources list every work each brief relies on.
- ownWords holds only the subject's own works: Scholz's edition for Ockham; PG150 and Gass for Cabasilas.

### Grades

| Profile | Words (`wc -w`) | FK | Flesch | With this round's fix |
|---|---|---|---|---|
| william-of-ockham | 405 | 8.07 | 63.19 | no change |
| nicholas-cabasilas | 406 | 7.99 | 61.45 | 407 words, FK 8.02, Flesch 61.33 |

### Count

- william-of-ockham: 0 blocking, 0 minor.
- nicholas-cabasilas: 2 blocking (C3-B1, C3-B2), 1 minor (C3-M1, the open call).

## Era 6 Who batch 2, round 3 recheck: PART D

**Scope.** `gregory-palamas` and `gregory-of-sinai`. Every round 2 finding in Part D (D2-M1 to D2-M19) and how R2_changes says it was applied, including the three differences the fixer listed (D2-M1 witness lines, D2-M7 records text, D2-M12 wording, D2-M14 Basil trace). Every line changed between `d7c4490c` and `e072b50d` in the two briefs, cards, audio files and records entries, and the README lines on the two men. All quotations in double marks (items 3 and 6 of the brief). Branch `claude/cft-who-era6-batch2`. No repo file edited. No network, paid or model call.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its checklist, lessons.md, R2_review.md Part D and R2_changes.md Part D. I word-diffed the two men's files and README across `d7c4490c..e072b50d`, and read the records diff for their entries. For each changed line I opened the cited source with 20 or more lines of context and asked what document a note annotates and who speaks. For the Combefis change I traced the Mansi 26 document from its heading to the notes, column by column. I diffed each audio file against its brief, checked card field order on the parsed JSON, counted words with `wc -w`, and scored both briefs with `engine.m1.gates.grade_text`.

**Files opened (cic/texts/).**
- CANT2 `cantacuzenus_historiarum-libri-iv-v2-grc-lat_schopen1831.txt` l.34285-34340
- MANSI26 `mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt` l.10168-10240, 10355-10372, 10495-10535, 12060-12200, 12440-12530, 19560-19615; running heads and headings l.10100-19800 by grep
- PAISK `paisius-velichkovsky_vostorgnutye-klasy-chu_optina1849.txt` l.1-45, 9820-9845
- PAISZ `paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt` l.3984-4008, 10995-11035, 14190-14226
- MEYER `athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt` l.1-3, 28-52, 3985-4015
- RACKI `racki_bogomili-i-patareni-rad-viii-hrv_jazu1869.txt` l.1-8, 19, 3660-3672
- PG150 `palamas_opera-omnia-pg150-grc-lat_migne1865.txt` l.72572-72605

### Quotations

Neither brief holds a double quotation mark (`grep -c '[“”"]'` gives 0 for both). No card field value holds a straight or curly double mark (checked on the parsed JSON). There is nothing to check verbatim under item 3. Lines held only in Greek, Latin, Slavonic, Croatian or German are told in modern words with no marks; I checked each changed telling against its original below.

---

### gregory-palamas

**R2 findings: applied?**

| R2 id | Verdict |
|---|---|
| D2-M1 ("for justice and truth") | OK. "ὑπὲρ αὐτοῦ δικαίου καὶ τῆς ἀληθείας κάκωσιν ὑπενεγκών, οὐδὲν ἀγεννὲς" (CANT2 l.34299-34302, OCR); Latin "pro iustitia veritateque gravissime afflictus, usque ad extremum nihil abiectum aut fecerit, aut dixerit" (l.34334-34336). The fixer's witness lines are right: "Παλαμᾶν δὲ ἐπήνει" opens l.34298, "Palamam" ends l.34333. "Lay in prison" offset OK. |
| D2-M2 ("Palamas left for Athos") | OK. |
| D2-M3 (Combefis's tome) | Wrongly applied. The round 2 finding named the wrong tome. Combefis annotates the tome of 1351, not 1347. See D3-B1. |
| D2-M4 (Philotheos in `dates`) | OK. |
| D2-M5 ("the emperor John Kantakouzenos") | OK. `place` is his first card mention. |
| D2-M6 (capture claim) | OK. The old sentence is gone and the GREG3 witness is one entry. |
| D2-M7 (PAISK witness) | OK. Title page "НѢСКОЛЬКО ПЕРЕВОДОВЪ … СТАРЦА ПАИСІЯ … ВЕЛИЧКОВСКАГО" is l.29-41; the contents entry "Григорія Паламы Архіепископа Ѳессалонитскаго, о молитвѣ" is l.9835-9836. The fixer's extra change to the claim text is right. |
| D2-M8 ("translated his piece on prayer") | OK. One piece, "о молитвѣ" (PAISK l.9836), in a book of his translations (l.29-41). |
| D2-M9 (README) | OK. Philotheos is "a patriarch of Constantinople" at his first brief mention and "patriarch of Constantinople" in `dates`, the card's first mention. |

**New findings**

**D3-B1 (card `uncertain`, the 1341 item; records claim "Combefis's note": the tome Combefis annotates is the 1351 one, not 1347).**
- Current text, card: "François Combefis, a Dominican, annotates the tome of 1347 in Mansi and calls it heretical. After Gregoras, he writes that no doctrine was debated at the 1341 synod."
- Current text, records: "he calls the 1347 tome 'heretico plane spiritu conscripta, & mendaciis conferta'."
- What the source says. Mansi's 1347 heading (MANSI26 l.10181-10199, "7. die Februarii anno 1347") opens a run of documents. It is not the document Combefis annotates. At column 109 Mansi says part of the 1347 tome "recitatur inter acta synodi Palamiticae anni 1350, rectius an. 1351, a Combefisio vulgata" (l.10511-10524, OCR). That 1351 tome begins at column 127: "TOMUS … a divina & sacra synodo, adversus sectatores Barlaami & Acindyni, regnantibus piis & orthodoxis Imperatoribus nostris, Cantacuzeno & Palaeologo" (l.12063-12070, OCR). Mansi's note on it reads "Hujus acta prolixe veriusque describuntur a Nicephoro Gregora, qui in ea contra Palamam disputavit" (l.12128, 12189). The running heads from there to column 206 read "PSEUDO-SYNODUS CANTACUZ. & PALAEOL. IMP. OR." (l.12060, 12456-12462). No new document heading falls between that tome and the notes. Combefis's notes follow at columns 207-208, "NOT. PSEUDO-SYNOD. CONSTANTINOPOLIT." (l.19574). Inside the note he says that Gregoras "ipse in hac Synodo ut Palamitarum erroris impugnator damnatur" (l.19596-19597). Gregoras disputed and was condemned at the synod of 1351, the one held under Kantakouzenos, so "hac Synodo" is 1351. The tome of 1347 recounts the deposition of Kalekas and does not condemn Gregoras. The tome of 1351 recounts 1347 as past: "editus est a synodo Tomus sacer … triginta episcoporum subscriptionibus roboratus" (l.12475-12478). Round 2 read the heading at l.10181 as the heading of the annotated text. That was a misreading of what document the note annotates. The reading of "in ea Synodo" as the 1341 synod still holds: "ea" is set against "hac" (l.19595-19596), and the 1351 prooemium is reporting Barlaam's earlier condemnation.
- Fix, card: "François Combefis, a Dominican, annotates the tome of 1351 in Mansi and calls it heretical. After Gregoras, he writes that no doctrine was debated at the 1341 synod." (0 words)
- Fix, records claim "Combefis's note…": replace "he calls the 1347 tome" with "he calls the 1351 tome, held under Kantakouzenos and John Palaiologos ('regnantibus … Cantacuzeno & Palaeologo'), at which he says Gregoras was condemned ('in hac Synodo … damnatur'),". Witness: "MANSI26 (mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt) l.10511-10524, 12063-12070, 12189, 19574, 19583, 19592-19597".

**Whole brief as a story.** It still opens on the palace prison scene in 1347, with the who-line in the first sentence. The D2-M1 change reads naturally ("for justice and truth") and puts no second "him" beside "his ally". D2-M2's "Palamas left for Athos" removes the stray pronoun. The brief flows as before.

---

### gregory-of-sinai

**R2 findings: applied?**

| R2 id | Verdict |
|---|---|
| D2-M10 ("the prayer of the mind") | OK. Paisius's "молитва сія" is the prayer "умомъ въ сердцѣ дѣйствуемая" (PAISZ l.11000); "отнюдь никогоже обрѣте въ ней, ниже малое вѣдѣніе о молитвѣ сей имущаго" (l.11027-11029). The passage is on page 232, inside Paisius's own writings, which begin at page 165 (l.14222-14226). |
| D2-M11 ("abbot of Neamț") | OK. "настоятеля Нямецкаго Вознесенскаго Монастыря" (PAISZ l.3993-3994); Moldavia from "Молдавскихъ Святыхъ монастырей Нямецкаго" (l.14195-14196). On the card it sits at his first mention (traces 2). |
| D2-M12 ("Some teach saying it") | OK. The fixer's wording keeps "διδάσκουσι λέγειν αὐτήν" (PG150 l.72599-72600), and the difference is sound. |
| D2-M13 (condition in keyWorks) | OK. "εἴπερ διήνοικται" (PG150 l.72579). |
| D2-M14 (first mentions) | OK. Meyer and Rački have their roles. The fixer's Basil wording names Gregory and Paisius and removes the "his … his" clash. "Наставникъ, спостникъ и другъ блаженнаго Отца Паисія" (PAISZ l.3991-3992); "Старца Поляномерульской обители Василія" (l.14215). |
| D2-M15 (Meyer's tradition) | OK. "Damals aber wurde sie einer glaubhaften Ueberlieferung nach durch den Mönch Gregorios eingeführt"; "(Vgl. den Bios des Gregorios … dem Patr. Kallistos" (MEYER l.4002-4003, 4008-4009). "Who edited the main Athos documents in 1894" matches the title page, "DIE HAUPTURKUNDEN FÜR DIE GESCHICHTE DER ATHOSKLÖSTER … HERAUSGEGEBEN … VON PH. MEYER" (l.32-48). |
| D2-M16 (uncertain 1 split) | OK. |
| D2-M17 (role) | OK. |
| D2-M18 (knownFor) | OK. |
| D2-M19 ("prefaces") | OK, card and README. |

**New findings**

**D3-M1 (records: the new card and brief identifiers for Paisius, Basil and Meyer have no witness line).**
- Current text: the records claim "Paisius on the copies…" witnesses Paisius only as "Архимандрита Молдовлахійскія Нямецкія обители" (l.14222-14223). The brief and card now say "abbot". The claim "Basil, elder of the Poiana Marului monastery and friend of Paisius…" cites l.3999, 4523-4526, 4651-4653, 14198-14199, 14206-14207, and none of those names Poiana Marului. The claim "Meyer 1894…" cites l.3998-4009 only, not the title page behind "who edited the main Athos documents".
- Source: "старецъ схимонахъ Василій въ своемъ скиту, именуемомъ Поляномерульскимъ … наставникъ, спостникъ и другъ блаженнаго Отца Паисія, настоятеля Нямецкаго Вознесенскаго Монастыря" (PAISZ l.3987-3994); "Старца Поляномерульской обители Василія" (l.14215); MEYER title page l.32-48.
- Fix, records: in "Paisius on the copies…", change the witness to "PAISZ (paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt) l.3993-3994, 10528-10541, 14222-14223" and add to the claim "; abbot, 'настоятеля Нямецкаго Вознесенскаго Монастыря' (l.3993-3994)". In the Basil claim, add "3987-3994, 14215" to the witness. In "Meyer 1894…", add "32-48 (title page)" to the witness.

**Whole brief as a story.** It still opens on Gregory going round Athos, and the who-line follows at once. "The prayer of the mind" now gives paragraph 2's last sentence a clear referent. The term matches paragraph 3's "prayer of the mind" and the notice's "νοερᾶς προσευχῆς". The paragraph 4 splice ("Some teach saying it with the mouth, some with the mind, he added, and he taught both.") reads aloud without a break. The brief still closes on Gregory's own teaching.

---

### records.json (these profiles)

- **gregory-palamas.** The D2-M1, D2-M6 and D2-M7 entries are applied and match their sources (CANT2 l.34298-34303, 34333-34336; PAISK l.29-41, 9835-9836). The "Combefis's note" entry carries the wrong tome; D3-B1 gives the fix. The contested_claim "Whether the 1341 synod examined doctrine" (MANSI26 l.19594-19597) stands. No absent_details note changed in round 2.
- **gregory-of-sinai.** The contested_claim side 2 now reads "by what he calls a credible tradition, referring to Kallistos's Life (MEYER l.4001-4009)", which matches l.4001-4009. Witness gaps for the new identifiers are listed in D3-M1. No absent_details note changed in round 2. No new "no", "only", "alone" or "none" claim entered either brief or card in round 2. The one new phrase of that kind, Paisius's "no one … who knew the prayer of the mind", is attributed to him and held at PAISZ l.11027-11029.

### Checklist summary

| # | Item | gregory-palamas | gregory-of-sinai |
|---|---|---|---|
| 1 | Each sentence sourced, source establishes it | Fail (D3-B1: wrong tome) | Pass (D3-M1 is a records witness gap) |
| 2 | Quotes verbatim | Pass (no quotations in marks) | Pass (no quotations in marks) |
| 3 | No invented family, feeling, thought, anecdote, speech | Pass | Pass |
| 4 | Reading aids, no AI tells | Pass | Pass |
| 5 | No role for a named witness | Pass | Pass |
| 6 | Partisan or hostile witness named and marked | Pass | Pass |
| 7 | Contested claim shows both sides | Pass | Pass |
| 8 | Common names with place at first mention, each text | Pass | Pass |
| 9 | One term for one thing | Pass | Pass |
| 10 | Story, scene opening, disputes in place, length | Pass | Pass |
| 11 | Readability (FK ≤10, Flesch ≥60) | Pass | Pass |
| 12 | Card order, missing fields absent, caveat in What is uncertain | Pass | Pass |
| 13 | Audio tags only in audio, at start and before last line | Pass | Pass |
| 14 | Keeps list line; a Who with a body of work or following | Pass | Pass |

Card form (item 6 of the brief). Field order on both cards is name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources, as the pattern sets it. `briefLength` reads "about 2 minutes 30 seconds" on both. That is the house form for this field on every Who card, and round 2 recorded it the same way. At 407 and 406 words the time is right, but it is not a word count as this brief's item 6 states. The coordinator should settle which form is meant once, for all cards. Audio: with the tags stripped, each script matches its brief exactly. Each has one `[calmly] ` at the start and one `[warmly] ` at the start of the last paragraph. `sources` list every work each brief relies on. `ownWords` hold only the subject's own works. `keyWorks` hold three each.

### Grades

| Profile | Words (`wc -w`) | FK | Flesch |
|---|---|---|---|
| gregory-palamas | 407 | 7.77 | 63.26 |
| gregory-of-sinai | 406 | 8.59 | 63.48 |

D3-B1 and D3-M1 do not touch either brief, so these scores stand after the fixes.

### Count

- **gregory-palamas:** 1 blocking (D3-B1), 0 minor. Eight of the nine round 2 points were applied correctly. D2-M3 was applied as worded, but its wording named the wrong tome.
- **gregory-of-sinai:** 0 blocking, 1 minor (D3-M1). All ten round 2 points were applied correctly, and the fixer's two differences (D2-M12, D2-M14) are sound.
- **Part D total:** 1 blocking, 1 minor.
