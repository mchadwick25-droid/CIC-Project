# R2 review: era 6 batch 2

Round 2 is a targeted recheck at full effort by four fresh Opus reviewers, one per part, of what round 1 changed and its findings. Every quotation in the briefs and cards was re-verified against its file and lines. Brief: the round 1 brief's scope narrowed to the round 1 changes, with the lessons list.

## Era 6 Who batch 2, round 2 recheck: PART A

**Scope.** A targeted recheck of `catherine-of-siena` and `bridget-of-sweden` (brief, card, audio, each one's `records.json` entry) and the batch `README.md` (all its lines). The R1 findings checked are A-B1 to A-B5 and A-M1 to A-M32 (R1_review.md l.5-389), against R1_changes.md Part A and `git diff ba5a9f37..d7c4490c`. Branch `claude/cft-who-era6-batch2` at d7c4490c. No repo file was edited. No web, paid or model call was made.

**Method.**
- I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md`, lessons.md, the R1 Part A text, R1_changes.md and the handover note.
- For every changed line I reopened the cited source with 20 or more lines of context. I asked what document each note annotates, who is speaking, and whether a condition or hedge was dropped.
- I checked every double-quoted string in both briefs and both cards against its file by eye, and by a whitespace- and hyphen-tolerant script.
- I searched all of `cic/texts/` (windowed regex, my script) before judging each new "only" or absence note.
  - Canonization: canoniz-/canonis-/"in sanctorum numerum"/adscripsit within 300 characters of Catharin-/Caterin-/Katherin-/Catherin- + Sien-/Senen-/Senis/Sene, in every file naming Siena. Hits: Covel, Fiorilli's 1517 entry, and Guyon's translator's preface (no date).
  - Bridget's birth year: 1300 to 1309 and MCCCI- within 250 characters of Birgit-/Brigitt-/Bridget/Brigid, and age words (aetatis, annorum, years of age), in all 165 files that name her.
- I diffed both audio files against the briefs by script and checked card field order by script.
- I scored all eight briefs and my proposed texts with `engine.m1.gates.grade_text`, and counted sentence lengths by script.
- For the README I recomputed the ranges, and checked each changed line against the cards, records, Open-Gaps.md and the census. `origin/main` is not present in this checkout, so the census check used the branch's own `cic-website/data/world-census.json`, which this batch does not touch.

**Files opened (cic/texts/), with context.**
- MIRBT `mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt`: l.13860-13895.
- CATHL `catherine-of-siena_selected-letters_scudder1905.txt`: l.512-524, 1195-1400, 4924-5240 (letter headings), 5212-5224, 6775-6805, 12720-12735, 12880, 12918-12936.
- CATHD `catherine-of-siena_dialogue_thorold1896.txt`: l.15-45, 3190-3202.
- CATHI `catherine-of-siena_libro-della-divina-dottrina-ita_fiorilli1912.txt`: l.14336-14346, 14380-14515, 14600-14636, 15158-15172, 15540-15551.
- BIRGL `birgitta_revelationes-lat_duranti1628.txt`: l.1-12, 205-262, 755-775, 1183-1200, 1500-1528, 8150-8185, 11090-11130, 98262-98315, 98405-98422, 98545-98615, 98770-98800, 98940-99020.
- BIRGE `birgitta_revelations-enm_cumming1929.txt`: l.1-10, 72, 880-1060, 2120-2135, 9585-9595.
- ASJUN5 `acta-sanctorum_junii-tomus-5-lat_palme1867.txt`: l.52505-52592.
- ASMAR3 `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt`: l.132850-133010, 133200-133280.
- MANSI26 `mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt`: l.1-10, 53370-53420.
- WILKENS `jacques-de-vitry_briefe-in-zeitschrift-fuer-kirchengeschichte-14-lat-deu_rohricht1894.txt`: l.16052-16072, 16108-16122, 16300-16312.
- LEA3 l.29380-29395; TERESA `teresa-of-avila_interior-castle_stanbrook1912.txt` l.640-700; COVEL l.180-186, 51452-51468; BANCHI1 l.155-161; GLASS `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt` l.1-10, 71, 96-116; `carmelite-general-chapters_…wessels1912.txt` (Bernardinus de Senis, for the README).

**Quotations.** All match their files.
- Catherine brief: "But you, with your taxes and frivolities, are spoiling all that is sown." CATHL l.6795-6796.
- Catherine brief: "Come, come, come, and do not wait for time, since time does not wait for you." CATHL l.5221-5222 (letter to Gregory XI, running head l.5159).
- Catherine brief: "I have made a Bridge of My Word, of My only-begotten Son, and this is the truth." CATHD l.3199-3201.
- Catherine card: "her constant theme is the corruption of every rank in the hierarchy and the immediate necessity for reform." LEA3 l.29390-29392.
- Catherine and Bridget cards: "the books of St. Gertrude, St. Catharine of Siena, or St. Bridget of Sweden" TERESA l.683-685.
- Catherine card: "perhaps" CATHL l.1313.
- Bridget brief and card: "a sleer of soules" BIRGE l.2133.
- No quotation marks sit around the drafter's English of Latin, Italian or German in either brief or card.

**Audio.** Both audio files are the brief exactly, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, two tags and nothing else (checked by script). Pass.

---

### catherine-of-siena

**R1 findings: applied?**

| R1 id | Status |
|---|---|
| A-B1 | OK. The condition is in the brief and records, and checked against CATHL l.6788-6791. |
| A-B2 | OK. Card, records and README now carry the later softening and the commentator's own view (ASJUN5 l.52514-52590 reread: "sicuti reformata et mitigata etiam fuit … non diu post, Bulla Sixti IV"). |
| A-B3 | OK in the brief, card, records and README. R1_changes' difference ("credited his return to Bridget's revelations") is better than the proposal and true to MANSI26 l.53403-53408. One new pronoun fault sits in the same paragraph (A2-M1). |
| A-M1 | OK. Fiorilli's notes 5-7 (CATHI l.14432-14442) name the three. |
| A-M2 | OK. |
| A-M3 | OK. The Covel sentence is cut from the brief, and the card gives his role. The card sentence is now 30 words (A2-M5). |
| A-M4 | OK. |
| A-M5 | OK. Checked against CATHI l.14444-14472. |
| A-M6 | OK. Checked against CATHI l.14436-14438, 14462-14465. |
| A-M7 | Applied, but the wording is unclear (A2-M4). |
| A-M8 | OK for Gardner, Lea and Alvarez. Duranti lost his first name at his first card mention (A2-M3). |
| A-M9 | OK. Five claims retagged; Fiorilli added (CATHI l.14604-14607, 14631-14634 reread). |
| A-M10 | OK. CATHI l.15166-15169 reread: "A c. 6: «Qui comincia lo libro … E questo fu nel 1377 (_sic_)»". |
| A-M11 | OK. My search found no further witness. |

R1_changes does not list one cut. "and dictated most of her letters" left the end of para 2. It is harmless, because the card's keyWorks carries the dictation (CATHL l.517-522), and it may have been in the reviewer's full text. It is noted here, not counted.

**A2-M1 (brief para 4: "her" can be heard as Bridget).**
- Current text: "Consalvo Duranti, in his 1628 notes on Bridget of Sweden's Revelations, says her letters handled the whole matter of his return."
- Source: BIRGL l.98792-98796, "litterae S.Catharinae Senensis ad eundem Pontificem scriptae, quibus totum negotium cum eo de reditu in Italiam peregit". The letters are Catherine's.
- The nearest woman before "her" is Bridget of Sweden, so a listener can hear "Bridget's letters".
- Replacement: "Consalvo Duranti, in his 1628 notes on Bridget of Sweden's Revelations, says Catherine's letters handled the whole matter of his return." (±0)

**A2-M2 (brief para 4 and card `uncertain` 1: "Mansi's councils" is unexplained).**
- Current brief text: "A life of Gregory printed in Mansi's councils says one writer, Gobelinus, credited his return to Bridget's revelations."
- Current card text: "A notice of Gregory's life printed in Mansi's councils names other causes".
- Source: MANSI26 l.1-3 (title page as catalogued: "Sacrorum conciliorum nova et amplissima collectio … quae Joannes Dominicus Mansi … evulgavit"); the Life is headed "VITA GREG. PAP XI" (l.53417).
- A listener does not know who Mansi is or what "Mansi's councils" means. The fix says what the book is and adds no claim.
- Brief replacement: "A life of Gregory in Mansi's collection of church councils says one writer, Gobelinus, credited his return to Bridget's revelations." (+2)
- Card: see A2-M3.

**A2-M3 (card `uncertain` 1: Duranti at first card mention has no first name and no role).**
- Current text: "How far she caused the pope's return. Scudder writes that Gregory, swayed by her representations, returned, and Duranti says her letters handled the whole matter of the return. Matilde Fiorilli writes that she did much toward it. A notice of Gregory's life printed in Mansi's councils names other causes: Gobelinus credits Bridget of Sweden's revelations, and Platina a bishop's retort. Scudder also writes that Gregory, perhaps regretting his return, became alienated from her."
- Before round 1 the item read "Consalvo Duranti". R1's proposed card wording dropped the first name, and no earlier card field names him.
- Source: BIRGL l.221 and 763 ("Confaluo Duranto Episcopo Feretrano"); l.98792-98796.
- Replacement: "How far she caused the pope's return. Scudder writes that Gregory, swayed by her representations, returned. Consalvo Duranti, annotating Bridget of Sweden's Revelations in 1628, says Catherine's letters handled the whole matter of the return. Matilde Fiorilli writes that she did much toward it. A notice of Gregory's life in Mansi's collection of church councils names other causes: Gobelinus credits Bridget's revelations, and Platina a bishop's retort. Scudder also writes that Gregory, perhaps regretting his return, became alienated from her."

**A2-M4 (card `legacy.traces` 3: "as it is held" is unclear, and reads as the Library's "held").**
- Current text: "Fiorilli lists many manuscripts and early printings of the Dialogue in Italian, the first, as it is held, in 1472."
- Source: CATHI l.14506-14510, "delle quali si trovano alcune di data posteriore a quella che è ritenuta edizione principe, 1472".
- Replacement: "Fiorilli lists many manuscripts and early printings of the Dialogue in Italian. The printing of 1472 is taken to be the first."

**A2-M5 (card `dates`: the Covel sentence is 30 words).**
- Current text: "John Covel, Master of Christ's College, Cambridge, writing in 1722 against prayer to the saints, says Pius II canonized her about eighty years after her death, and gives no year."
- Source: COVEL l.183-184 ("Master of CHRIST College in CAMBRIDGE"), l.51456-51466.
- Replacement: "John Covel, Master of Christ's College, Cambridge, wrote in 1722 against prayer to the saints. He says Pius II canonized her about eighty years after her death, and gives no year."

**The brief as a story.** It still opens on Raymond's scene at Avignon, and the who-line follows at once. The peace mission, the letters, the return and its dispute, the Dialogue, the schism and the death flow in order. The splice in para 4 tells the dispute in place and names each witness. Para 4 is a run of four "X says" sentences. It reads as a weighing of witnesses, not as a choppy run, and it is acceptable. The voice stays distinctive, carried by the scene and her own lines. With A2-M1 and A2-M2 the brief is 405 words, FK 6.76, Flesch 71.72 (my text: `scratchpad/r2a/cath.txt`).

---

### bridget-of-sweden

**R1 findings: applied?**

| R1 id | Status |
|---|---|
| A-B4 | Applied in the brief, card, records and README, and the owner is now right (BIRGL l.11096-11124 and 8157-8181 reread). The verb "gives all eight books to" no longer says what Peter Olavus did (A2-M7). |
| A-B5 | OK. BIRGL l.99007-99016 reread. |
| A-M12 | Applied. The split brought in a pronoun fault: "him" now follows "Christ" (A2-M6). |
| A-M13 | The condition is applied, and the records note Cumming's Alphonso. "If he went back" is unclear, and the brief still tells "she handed him" as settled against Cumming (A2-M8). |
| A-M14 | OK. "Fifteenth-century" is on the title page itself (BIRGE l.72), not only in the header. |
| A-M15 | OK in the brief. The card's Wilkens still has no role (A2-M11). |
| A-M16 | OK. BIRGL l.1502-1527 reread. |
| A-M17 | OK. BIRGE l.9590-9592 reread. |
| A-M18 | OK. "Savior" appears nowhere else in the batch except Cabasilas's card ("the Savior's"), which is consistent. |
| A-M19 | OK. |
| A-M20 | OK. |
| A-M21 | OK. "Roman" is on the 1628 title page: "MDCXXVIII ROMA, Superiorum permissu" (BIRGL l.239-240), and the title holds "libros quinque". |
| A-M22 | OK. BIRGL l.98270-98312 is headed "Revelatio tangens Papam Urbanum … super confirmatione Regulae Salvatoris". |
| A-M23 | Applied. Glassberger's role holds on his own title page (GLASS l.71, 96-102). The Richental sentence now names the Council of Constance twice (A2-M9). |
| A-M24 | Wrongly applied for the Rome years (A2-B1). The 23 July Bollandist note is right (ASMAR3 l.133269 note b, on "Mortis … b matris suae S. Birgittae", l.132979). |
| A-M25 | OK. MANSI26 l.53393-53410 reread. |
| A-M26 | OK. The new absent_details note does not state its searches (A2-M12). |
| A-M27 | OK. |

**A2-B1 (card `place` and records claim: the Rome years are given to "Cumming's reckoning", and the Bollandist note is misread).**
- Current card text: "Rome, where she lived from 1348 or 1349, by Cumming's reckoning, and died."
- Current records claim: "Rome from 1348 or 1349 by reckoning; the Bollandists 'ab anno 1348'; her death 'Anno 1373 die 23 Julii'."
- What the sources say:
  - Cumming dates only the start of the journey: "two or three years elapsed before her journey began" (BIRGE l.967), after the revelation of 1346 (l.928-929). He gives no year for her arrival in Rome, and he makes no reckoning.
  - Cumming quotes the Extravagantes, ch. 8, that she "mansit ibi … xv annis, antequam veniret Papa, videlicet Vrbanus V". He then notes that "Birgitta did not see Urban V until 1367, over twenty years later", and points to an attempt "to explain this chronological discrepancy" (BIRGE l.955-961, 996-998). On his own page, the year she reached Rome is in doubt.
  - The Bollandists' note "a Ergo ab anno 1348" (ASMAR3 l.133269) annotates the daughter's Life: "Cum staret Romae viginti quinque (a) annis cum matre sua" (l.132892-132893). It reckons the daughter's twenty-five years in Rome with her mother back from 1373. It is the Bollandists' reckoning, not Cumming's.
- So the card gives Cumming a reckoning he does not make, on a point his own note shows to be uncertain.
- Card replacement: "Rome, where she lived and died. A Bollandist note on her daughter's Life counts the daughter's twenty-five years there with her from 1348." (The `dates` field already says she left Sweden two or three years after 1346.)
- Records replacement: "Rome: Cumming dates only the start of the journey, two or three years after the revelation of 1346 (BIRGE l.928-929, 967). He quotes the Extravagantes, fifteen years in Rome before Urban V came, and notes the chronological discrepancy (BIRGE l.955-961, 996-998). The Bollandists' note to her daughter's 'viginti quinque annis' in Rome with her mother: 'Ergo ab anno 1348' (ASMAR3 l.132892-132893, 133269). Her death: 'Anno 1373 die 23 Julii' (ASMAR3 l.133269)." Witness: BIRGE l.928-929, 955-961, 967, 996-998; ASMAR3 l.132892-132893, 133269. Tag: Contested, or Inferential-Thin with the discrepancy named.

**A2-M6 (brief para 1: "him" now follows "Christ").**
- Current text: "She told Christ that the Queen of Naples and many others called it impossible for him to come to Rome."
- Source: BIRGL l.98961-98965 and 98983-98988. The revelation is "pro Papa Gregorio XI", and "impossibile est eum venire Romam" means the pope.
- The R1 split moved "Christ" into the sentence just before "him". Spoken aloud, it says Christ cannot come to Rome.
- Replacement: "She told Christ that the Queen of Naples and many others called it impossible for Pope Gregory XI to come to Rome." (+2) The last sentence of the paragraph then reads "Gregory reached Rome in January 1377." (−1)

**A2-M7 (brief para 3 and card `uncertain` 1: "gives all eight books to" does not say what Peter Olavus did).**
- Current brief text: "Consalvo Duranti, a bishop annotating the Latin in 1628, gives all eight books to a Cistercian confessor he calls Peter Olavus."
- Current card text: "Consalvo Duranti gives all eight books to Peter Olavus, a Cistercian confessor, in one place, and in another names Peter Olavus, Master Matthias and Alphonso as the three who put her words into books." (37 words)
- Source: BIRGL l.11120-11123, "qui in linguam Latinam octo libros Reuelationum transtulit". "Gives … to" can be heard as authorship.
- Brief replacement: "Consalvo Duranti, a bishop annotating the Latin in 1628, says a Cistercian confessor he calls Peter Olavus translated all eight books." (±0)
- Card replacement: "Consalvo Duranti says in one place that Peter Olavus, a Cistercian confessor, translated all eight books. In another he names Peter Olavus, Master Matthias and Alphonso as the three who put her words into books."

**A2-M8 (brief para 4: "went back" is unclear, the delivery is told one way, and the death line is not quite Duranti's).**
- Current text: "When Urban V, who came in 1367, left again in 1370, she handed him a revelation. If he went back, it warned, he would soon suffer a blow. Duranti notes he died after his return. That year, Cumming says, Urban approved her Order of St Savior."
- What the sources say:
  - The condition is "Si contigerit ipsum redire ad terras, vbi fuit electus Papa" (BIRGL l.98553-98555), and the heading reads "antequam rediret Auenionem" (l.98413-98415). After "left again", "If he went back" can be heard as going back to Rome.
  - The heading says "quam ipsa praesentauit ei in Monteflascone" (l.98416-98419). Cumming says "This revelation was delivered to him by Alphonso" (BIRGE l.993, 1022). The records note the clash, but "she handed him" tells one side as settled.
  - Duranti does not say "after his return". He reports Platina: "dum enim proficiscebatur in Galliam … mortuus est, vel ut alij volunt, Auenione vitam finiuit" (BIRGL l.98603-98609). That gives two versions, on the road or at Avignon. Cumming says plainly that he "died the same year, in less than a month after returning to Avignon" (BIRGE l.1022-1024).
- Replacement: "Urban V came in 1367 and left again in 1370. A revelation of hers warned him that if he returned to Avignon, he would soon suffer a blow. That year, Cumming says, he approved her Order of St Savior, and died there within a month of arriving." (+3)
- Offset: in para 6, "Her bones were carried home to Vadstena" becomes "Her bones were carried to Vadstena" (−1).
- With A2-M6, A2-M7 and A2-M8 the brief is 405 words, FK 6.85, Flesch 68.68, longest sentence 24 words (my text: `scratchpad/r2a/brid.txt`, which has the "died within a month of reaching Avignon" variant; "died there within a month of arriving" has the same count).

**A2-M9 (card `legacy.traces` 3: the Council of Constance twice in one sentence).**
- Current text: "At the Council of Constance in February 1415, Ulrich Richental, chronicler of the Council of Constance, writes, learned men of Sweden, Denmark and Norway asked the council to make her a saint."
- Replacement: "At the Council of Constance in February 1415, its chronicler Ulrich Richental writes, learned men of Sweden, Denmark and Norway asked the council to make her a saint."

**A2-M10 (card `dates`: one sentence of 40 words).**
- Current text: "Cumming gives her death in Rome as 23 July 1373 in one place and 28 July in another; Boniface IX's bulls set her feast on 23 July, and a Bollandist note on her daughter's Life gives the same day."
- Replacement: "Cumming gives her death in Rome as 23 July 1373 in one place and 28 July in another. Boniface IX's bulls set her feast on 23 July, and a Bollandist note on her daughter's Life gives the same day."

**A2-M11 (card `uncertain` 1: Wilkens has no role at his first card mention).**
- Current text: "C. A. Wilkens, in 1894, says Prior Peter and Alphonso…"
- Source: WILKENS l.16058-16062 and 16310. He signs a review of Binder's and Flavigny's books. The brief already reads "in an 1894 review".
- Replacement: "C. A. Wilkens, in an 1894 review, says Prior Peter and Alphonso…" (Item 8 applies to each text separately.)

**A2-M12 (records `absent_details`, "A primary witness for her birth year": the searches are not stated).**
- Current note: "Only Cumming's line (BIRGE l.857); the Library file headers' 'about 1303' is not a witness."
- My search (see Method) found no other year line. It found two near witnesses that give no year: Cumming's quotation of the Extravagantes, "anno aetatis suae xxxxii" at her coming to Rome (BIRGE l.959-960), and the Bollandists' note that Hemming of Åbo, "cui revelatus fuit ortus S. Brigittae", died in 1307 (ASJUN5 l.14878-14880).
- Replacement note: "Searched all cic/texts for 1300 to 1309 and MCCCI- within 250 characters of Birgit-/Brigitt-/Bridget/Brigid, and for age words near her name. Only Cumming's line gives a year (BIRGE l.857). The Extravagantes give her age at her coming to Rome without a year (BIRGE l.959-960). The Library file headers' 'about 1303' is not a witness."

**The brief as a story.** It opens on the Naples vision and gives the who-line in para 2. It flows from marriage to call, to Rome, the Latin dispute, Urban V, the denunciation, the burial and canonization, and closes on the first call. The R1 splices read cleanly. The closing paragraph's turn back to her first call is unchanged and still works as a close. With A2-M6 the scene names the pope it concerns, which also strengthens the opening.

---

### README.md

All changed lines were checked against the cards, records, Open-Gaps.md and the census. These hold:
- The ranges: 403 to 406 words, FK 6.64 to 8.64, Flesch 61.41 to 72.47. These are my recount of all eight briefs at d7c4490c. Recompute them after round 2's fixes; Catherine and Bridget both move to 405 words if A2-M1, A2-M2 and A2-M6 to A2-M8 are applied.
- Para 2: each of the eight is a voice and on the people list of its card tradition, except Ockham, who is a Franciscan Order voice and not on its people list. The Fraticelli entry names him in its text only. This is checked on the branch's `cic-website/data/world-census.json`, since `origin/main` is not in this checkout.
- Catherine and Bridget bullets, the "among them" lists, the Clareno bullet (Papebroch, 14 June) and the Clareno and Bernardino names lines all match the cards and records. Bernardinus de Senis is in the Carmelite general chapters file (l.15081, 16211 and others).

**A2-M13 (README para 3: "an era 6 entry is registered with this batch" is not yet true).**
- Current text: "Which five the river shows is Mark's pick, as for eras 4 and 5 (Open-Gaps 263); an era 6 entry is registered with this batch, and the coordinator asked for the count to be noted here."
- Open-Gaps.md on this branch ends at entry 265 and has no era 6 batch 2 entry. The handover note plans it "just before merging" (Handover_after_R1.md, "Still to do" 2). The lessons rule is that the log comes before the README claims it.
- Fix: register the entry before merge and cite its number here. Until then, read "an era 6 entry is to be registered with this batch".

**A2-M14 (README, Cabasilas bullet: "tagged Contested" is wrong for the archbishop claim).**
- Current text: "When he became archbishop of Thessalonica (…), how he was Nilus's nephew, whether the "Kabasilas of the sakellion" is he and which anti-Latin writings are his are tagged Contested".
- Records: the archbishop claim is tagged "Widely Accepted", as round 1 (C-B2) retagged it. It has a contested_claims record ("When he became archbishop of Thessalonica, and whether he did"). The other three are tagged Contested.
- Replacement: "…and which anti-Latin writings are his each have a contested claim in the records".

**A2-M15 (README, quotation-marks paragraph: the list leaves out an English source both part A cards quote).**
- Current text: "Quotation marks are kept only for lines held in English: Scudder's and Thorold's Catherine, Cumming's Middle English Bridget, Robins's Bernardino, Lea's and Shirley's English, and the 1931 English Luther."
- Both cards quote Rodrigo Alvarez's note in the Stanbrook English of Teresa's Interior Castle (TERESA l.683-685). The sentence reads as a full list.
- Replacement: "…Robins's Bernardino, Lea's and Shirley's English, the Stanbrook English of Rodrigo Alvarez's note, and the 1931 English Luther."

---

### records.json (these profiles)

- **catherine-of-siena.** All R1 records fixes are in place and their lines reread. Every brief sentence and card field has a claim. The canonization and burial absences hold on my search. No new records fix is needed beyond the wording in A2-M3 (the card only).
- **bridget-of-sweden.** All R1 records fixes are in place. Two need fixing: the Rome-years claim (A2-B1) and the birth-year absent note (A2-M12). The Montefiascone claim's "she foretold that if he returned home he would die very soon, which happened" drops Platina's two places as Duranti gives them. Add "on the way to France or, as others say, at Avignon (BIRGL l.98604-98609)" so the claim carries what A2-M8 relies on.

### Checklist summary

| # | Item | catherine-of-siena | bridget-of-sweden |
|---|---|---|---|
| 1 | Each sentence's source establishes it | Pass | Fail (A2-B1; A2-M8 death line) |
| 2 | Quotes verbatim | Pass | Pass |
| 3 | Nothing invented | Pass | Pass |
| 4 | Reading aids, no AI tells | Fail, minor (A2-M1 pronoun, A2-M4, A2-M5) | Fail, minor (A2-M6 pronoun, A2-M8, A2-M9, A2-M10) |
| 5 | No role standing in for a witness | Pass | Pass |
| 6 | Partisan or hostile witness marked | Pass | Pass |
| 7 | Contested claims show both sides by name | Pass | Fail, minor (A2-M8: delivery told one way) |
| 8 | Common names and scholars identified at first mention | Fail, minor (A2-M2, A2-M3) | Fail, minor (A2-M11) |
| 9 | One term for one thing | Pass | Pass |
| 10 | Story, scene opening, disputes in place, length | Pass | Pass |
| 11 | `grade_text` (FK ≤ 10, Flesch ≥ 60) | Pass (6.64, 72.47) | Pass (6.58, 69.87) |
| 12 | Card order, missing fields absent, caveat repeated | Pass | Pass |
| 13 | Audio tags only in the audio script, placed right | Pass | Pass |
| 14 | Keeps list line; Who test | Pass (voice and people list) | Pass (voice and people list) |

Card form for both: the fields are in the pattern's order. `briefLength` is "about 2 minutes 30 seconds", the house form of every era 6 card, and it matches 403 and 404 words. The audio is exact. Sources list every work each brief relies on (Mirbt, Scudder, Thorold, Fiorilli, Duranti and Mansi 26 for Catherine; Duranti with Torquemada, Cumming, Wilkens, Lea, Scudder and the bulls in the 1628 file for Bridget). ownWords holds only the subject's own texts (the editors' notes ride in the same files, as their titles say). keyWorks are two and three.

### Grades

| Profile | Words | FK | Flesch |
|---|---|---|---|
| catherine-of-siena (now) | 403 | 6.64 | 72.47 |
| catherine-of-siena (with A2-M1, A2-M2) | 405 | 6.76 | 71.72 |
| bridget-of-sweden (now) | 404 | 6.58 | 69.87 |
| bridget-of-sweden (with A2-M6 to A2-M8) | 405 | 6.85 | 68.68 |

All eight briefs at d7c4490c: angelo-clareno 406, 7.93, 63.29; bernardino-of-siena 405, 7.21, 69.87; gregory-of-sinai 403, 8.64, 62.87; gregory-palamas 406, 7.69, 63.81; nicholas-cabasilas 406, 8.11, 61.41; william-of-ockham 405, 8.04, 63.41.

### Count

- catherine-of-siena: 0 blocking, 5 minor (A2-M1 to A2-M5).
- bridget-of-sweden: 1 blocking (A2-B1), 7 minor (A2-M6 to A2-M12).
- README.md: 0 blocking, 3 minor (A2-M13 to A2-M15).
- Part A total: 1 blocking, 15 minor.

## Era 6 Who batch 2, round 2 recheck: PART B

**Scope.** `bernardino-of-siena` and `angelo-clareno`. This is a targeted recheck of round 1 Part B (R1_review.md l.390-665; R1_changes.md, Part B) against `git diff ba5a9f37..d7c4490c` for both briefs, both cards, both audio scripts, their `records.json` entries and the README lines about them. Branch `claude/cft-who-era6-batch2`. No repo file was edited, and no web, paid or model call was made.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its checklist, and lessons.md. For every changed line I opened the cited source lines with at least 20 lines around them, and read the Latin, Italian and German myself. I asked, for each one, what the note annotates, who speaks, and whether a hedge or condition was dropped. Every quotation in double quotes was checked by eye against its file. For every new "no", "only" and absence I searched all of `cic/texts/` for name variants (`Angel* (de|da|of) Clar[ei]n`, `Clarenus`, `Clareno`, `Angel* de Cingul`), which gave 22 files. I then read each hit for birth years. That search found files round 1 did not open: Carlini, Bernard Gui (Mollat), the Quaracchi Opuscula, Haupt, Salimbene (Coulton), Thomas of Celano (d'Alençon) and the Bullarium Romanum. I also searched for "Felice Tocco", for Wadding as annalist, and for "strict observance" in Lea. The audio scripts were rebuilt from the briefs and compared byte for byte. The briefs were scored with `engine.m1.gates.grade_text`, and sentence lengths were counted by script. `tools/check_spelling.py` was run on all six files: no British spellings. House style is American (Decision-Log 77), so "practice" and "defense" are right.

**Files opened (cic/texts/).** ORL = `bernardino-of-siena_sermons_orlandi-robins1920.txt` (l.180-190, 236-243, 2950-2957, 5815-5840, 6815-6870); BANCHI1 = `bernardino-of-siena_prediche-volgari-1427-v1-ita_banchi1880.txt` (l.155-162, 300-336, 815-822, 1140-1166, 1250-1270, 5320-5380, 6402-6415); BANCHI2 = `…-v2-ita_banchi1884.txt` (l.16145-16178); GLASS = `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt` (l.94-112, 20686-20712, 21134-21143, 21715-21745); RAYN = `raynaldus_annales-ecclesiastici-tomus28-1424-1453-lat_theiner1874.txt` (l.2386-2428); BULN = `bullarium-franciscanum_nova-series-v1-lat_huntemann1929.txt` (l.13105-13192); LEA3 = `lea_history-of-the-inquisition-of-the-middle-ages-v3_1888.txt` (l.2192-2202, 3333-3339, 3626-3633, 8210-8232); CLAR = `clareno_expositio-regulae-fratrum-minorum-lat_oliger1912.txt` (l.1026-1040, 1130-1140, 1180-1225, 1240-1252, 1286-1298, 1340-1347, 1386-1440, 1480-1510, 1524-1570); EHRLE1 = `ehrle-denifle_archiv-…-bd1-deu-lat_1885.txt` (l.27538-27545, 27765-27800, 27855-27872, 28484-28500, 28555-28570, 29150-29226); EHRLE2 = `…-bd2-deu-lat_1886.txt` (l.5714-5718, 7665-7712); EHRLE3 = `…-bd3-deu-lat_1887.txt` (l.22698-22706); EHRLE4 = `…-bd4-deu-lat_1888.txt` (l.584-655); ASMAR3 = `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt` (l.24770-24835); SABAT = `speculum-perfectionis_speculum-perfectionis-lat_sabatier1898.txt` (l.484, 2510, 3822-3832, 4575-4592, 6826); PG88 = `dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt` (l.41440-41448, 43280-43308); CARLINI = `carlini_fra-michelino-e-la-sua-eresia-ita-lat_1912.txt` (l.1458-1464, 3830-3860, searches); ROBINSON = `francis-assisi_writings-of-saint-francis_robinson1906.txt` (l.1053-1058, 2806-2809); `actus-beati-francisci_…_sabatier1902.txt` (l.207). I also searched, without opening ranges: `bernard-gui_manuel-inquisiteur-t1-lat-fra_mollat1926.txt`, `francis-assisi_opuscula-lat_quaracchi1904.txt`, `haupt_…-bd7-deu_1885.txt`, `salimbene_from-st-francis-to-dante_coulton1907.txt`, `thomas-celano_…_d-alencon1906.txt`, `underhill_jacopone-da-todi-poet-and-mystic_beck1919.txt`, `leo-assisi_scripta-fratris-leonis-lat_lemmens1901.txt` and `bullarium-romanum_magnum-bullarium-tomus2-…-lat_cherubini.txt`.

### Quotations

All four quotations in double quotes match their files.
- Bernardino brief: "Chew, and chew, it would not go down!" matches ORL l.6860, the "!" included.
- Bernardino brief: "and we shall see what I have said that is wrong. I am one of those who wish to hold to that which Holy Church doth hold." matches ORL l.5832-5834, with the OCR allowance "Chureh".
- Bernardino card: "who counts as the formal founder of the Observantines" matches LEA3 l.8229-8231.
- Clareno card: "a man of the firmest and gentlest spirit" matches LEA3 l.3337-3338.
- The Clareno brief has no quotation marks. Each modern-words telling in both briefs was checked against its lines.

---

### bernardino-of-siena

**R1 findings: applied?**

| R1 id | Result |
|---|---|
| B-B1 | OK ("went to buy chamois skin"; ORL l.6840-6842, BANCHI2 l.16150-16152) |
| B-B2 | OK (the year 1920 is dropped from the brief) |
| B-B3 | OK ("Glassberger goes on" puts the witness inside the outcome sentence) |
| B-B4 | OK (the item and both records entries are gone). Two stale "Mansi" mentions are left behind (B2-M3). |
| B-B5 | OK in the brief, card and records (BANCHI1 l.318-322, 5337-5341, 5373-5375 read as cited). One records side misses a witness (see records). The README line is stale (B2-M4). |
| B-M1 | OK |
| B-M2 | OK |
| B-M3 | OK (RAYN l.2422-2424) |
| B-M4 | OK. R1_changes says the shorter wording was adopted ("a friar of the strict Observant branch"). It is sound (GLASS l.95-97; LEA3 l.8223-8224), and the offsetting cuts were taken. |
| B-M5 | OK |
| B-M6 | Wrongly applied: the new wording puts "May 1444" on the sending (B2-B1). |
| B-M7 | OK (ORL l.5823-5834: "any one who doth wish to give the lie … say it to my face") |
| B-M8 | OK |
| B-M9 | OK (BANCHI1 l.1257) |
| B-M10 | OK (BANCHI1 l.819; ORL l.2955) |
| B-M11 | Applied, but the new clause misnames the decree (B2-M2). |
| B-M12 | OK (ORL l.186-187) |
| B-M13 | OK |

**B2-B1 (brief para 6: a date put on an event no witness dates).**
- Current text: "In May 1444 he was sent to preach at L'Aquila, and he fell ill and died."
- Source: Vespasiano gives no month for the sending. His vicar sent him while he was preaching at Milan: "e predicando a Milano, gli fu commesso dal suo vicario che andasse all' Aquila a predicare … Innanzi che giugnesse all' Aquila, si ammalò di febre, e in pochi dì … si morì" (BANCHI1 l.1147-1153). The month belongs to the death: "XX. die Maii … reddidit sanctus Bernardinus Christo animam suam" (GLASS l.21737-21739). Built from B-M6, the sentence tells the listener he was sent in May.
- Fix: "He was sent to preach at L'Aquila, and in May 1444 he fell ill and died." The word count is unchanged (405). The next sentence still names Vespasiano for the road.

**B2-M1 (records: the witness for "the strict Observant branch" does not say it).**
- Current text: the records claim "Glassberger was an Observant Franciscan …" reads "The Observance as the stricter branch: GLASS l.21136-21142."
- Source: GLASS l.21136-21142 tells of the vicar general's appointment and does not call the Observance stricter. The held lines that do are the Quaracchi editors' note, "Filius fuit reformatae familiae Ordinis Minorum, quae nuncupatur de regulari Observantia" (GLASS l.95-97), and Lea, "the Observantines, or Franciscans of strict observance" (LEA3 l.8223-8224).
- Fix: change the claim's second sentence to "The Observance as the strict branch: GLASS l.95-97 (the editors' note); LEA3 l.8223-8224." Add LEA3 l.8223-8224 to the claim's witness field.

**B2-M2 (card `legacy.traces`: "the Observants' decree" says they issued it).**
- Current text: "when the minister general tried at the Council of Basel to undo the Observants' decree".
- Source: "tentavit, si infringere posset decretum sacri concilii Constantiensis in favorem Fratrum de Observantia editum" (GLASS l.20697-20698). The decree was the Council of Constance's, made in the Observants' favor.
- Fix: "when the minister general tried at the Council of Basel to undo the Council of Constance's decree in the Observants' favor".

**B2-M3 (card `sources` and README: Mansi left behind after B-B4).**
- Current text: the card's `sources.about` title "Annales ecclesiastici, volume 28 (1424-1453), with Mansi's notes". The README's held-witness line "Raynaldus's annals, with Sigonius's Bologna story, Surius's account of the death and Mansi's notes".
- Source: after B-B4, no card, brief or records line uses Mansi (a search of the card and records for "Mansi" finds only the title).
- Fix: card title "Annales ecclesiastici, volume 28 (1424-1453)". README: "Raynaldus's annals, with Sigonius's Bologna story and Surius's account of the death".

**B2-M4 (README: "two records" is no longer the whole account).**
- Current text: "Glassberger's accusation before Martin V and Eugenius IV's letter of 1432 are told as two records, and the card says no witness joins them."
- Source: the brief and card now also tell Bernardino's own words on Rome and Banchi's note (BANCHI1 l.318-322, 5337-5341, 5373-5375), and the card says "No witness says whether these were one case."
- Fix: "Glassberger's accusation before Martin V, Bernardino's own words on his hearing at Rome with Banchi's note, and Eugenius IV's letter of 1432 are told as separate records, and the card says no witness joins them."

---

### angelo-clareno

**R1 findings: applied?**

| R1 id | Result |
|---|---|
| B-B6 | OK (SABAT l.4586 is Sabatier's own chapter summary, and l.484 and 6826 match it). The absence of any other birth year holds after searching all 22 files that name him. |
| B-B7 | OK in the card and records (ASMAR3 l.24804-24829 read as cited). "The same contemporary miracles" is true, though the records do not cite it (see records). |
| B-B8 | Applied, but the new sentence drops Ehrle's own hedge (B2-B2). |
| B-B9 | OK (EHRLE1 l.29195-29200; CLAR l.1217-1218) |
| B-B10 | OK (PG88 l.43283, 41442). The added "though Ambrose does not name him" leaves out the rest of Rader's sentence (B2-M4). |
| B-B11 | OK (EHRLE1 l.27792-27795) |
| B-B12 | Applied, but Raynaldus's hedge is dropped in the card, README and records (B2-B3). |
| B-M14 | Applied. The card's and README's wording of what Papebroch reckoned is loose (B2-M2). |
| B-M15 | OK |
| B-M16 | Applied, but the new sentence drops "keeping" from the source and runs 27 words (B2-M1). |
| B-M17 | OK. Both readings of "his band" (Liberatus's or Angelo's) are true to CLAR l.1292-1295. |
| B-M18 | OK (CLAR l.1208, 1288) |
| B-M19 | OK (CLAR l.1190-1192) |
| B-M20 | OK (LEA3 l.3629-3632; CLAR l.1343-1345) |
| B-M21 | OK (CLAR l.1403-1405, 1490) |
| B-M22 | OK (EHRLE4 l.594-596, 648-650: 28 February [1334], before "fratre Symone inquisitore"; the bull is 21 February 1334, EHRLE4 l.1074) |
| B-M23 | OK (CLAR l.1245-1246) |
| B-M24 | OK (CLAR l.1249-1251) |
| B-M25 | Applied. "Franciscan annalist" is sound (ROBINSON l.1055-1056, "the renowned Annalist of the Order, Father Luke Wadding"; EHRLE2 l.5716). "Professor F. Tocco" was R1's fallback "if no held line spells 'Francesco'". A held line does spell the name, as "Felice" (B2-M3). |
| B-M26 | OK (EHRLE2 l.7707-7711) |

**B2-B2 (brief para 5: Ehrle's inference told as fact, with no witness in its sentence).**
- Current text: "Not long before his death, the old man went to a hermitage in the Basilicata, in the south. He died there in June 1337, Ehrle reckons."
- Source: Ehrle's "Jedoch nicht sehr lange vor seinem Tode*) begab er sich trotz seines hohen Alters in das Eremitorium" (EHRLE1 l.27770-27772) carries a note. The note hedges exactly this point: "Dies glaube ich daraus entnehmen zu können, dass der Cölestinerprior fr. Thomas Anglicus ihn als 'peregrinus et ignotus' bezeichnet" (l.27785-27786, OCR "glanbe … in kennen"). The note is the second in the run (OCR "3)"). The run is 1) Wadding, 2) this note, 3) the 15 June note (OCR "8)"), matching the markers after "Tode" and after "1337". Oliger also hedges, and dates the move earlier: "Sed Angelus eo tempore [1334] recessisse videtur in Italiam meridionalem … verosimiliter in eremitorium S. Michaelis" (CLAR l.1393-1396). As written, "Ehrle reckons" covers only the second sentence, so the first stands as the narrator's fact.
- Fix: "Not long before his death, Ehrle thinks, the old man went to a hermitage in the Basilicata, in the south, and died there in June 1337." (26 words, one fewer than the two sentences it replaces. The witness now covers both the move and the year.) Records: add EHRLE1 l.27785-27786 to the death claim, with "Ehrle infers the late move ('Dies glaube ich … entnehmen zu können')".

**B2-B3 (card `uncertain` "Whether a bull of 1331 was aimed at him", records contested claim, README: Raynaldus's hedge dropped).**
- Current text: card, "Raynaldus and Professor F. Tocco take him for Clareno, Eubel doubts it, and Oliger says it is not clear." Records side, "Raynaldus and Tocco: yes (CLAR l.1420-1424)". README, "Raynaldus and Tocco think so".
- Source: Oliger gives them two different strengths: "Ad eam vero assumendam propensus videtur Raynaldus l. c. n. 7, et eam sustinet F. Tocco, Studii Franc. 289, aliique" (CLAR l.1423-1424). In other words, Raynaldus "seems inclined" to the identity, while Tocco "holds" it. This is the same kind of dropped hedge as round 1's B-B10.
- Fix (card): "Whether a bull of 1331 was aimed at him. John XXII's bull of 23 November 1331 names a leader, Angelo of the Spoleto valley. Oliger says Raynaldus seems inclined to take him for Clareno and Felice Tocco holds that he was, while Eubel doubts it and Oliger finds it not clear." Fix (records side): "Raynaldus seems inclined to it; Tocco and others hold it (CLAR l.1423-1424)". Fix (README): "Whether the Angelo of the Spoleto valley of the 1331 bull is Clareno is open: Raynaldus seems inclined to think so and Tocco holds it, Eubel doubts it, and Oliger leaves it unsettled."

**B2-M1 (brief para 4: "of his rule" drops "keeping"; 27 words).**
- Current text: "If it was heresy to believe and practice humbly what Francis believed of his rule, he wrote, he had always held that heresy and held it still."
- Source: "id, quod sanctus Franciscus de sue regule observantia credidit" (EHRLE1 l.27864-27865), that is, what Francis believed about the keeping of his rule. The round 1 draft had "about keeping his rule", and B-M16's split lost it.
- Fix: "If it was heresy to believe and practice humbly what Francis believed about keeping his rule, that heresy, he wrote, he had always held and held still." (27 words, the same length. The meaning is restored. A shorter form would need an added frame the source does not give.)

**B2-M2 (card `dates`, card `uncertain` "When he died", README: what Papebroch reckoned).**
- Current text: `dates`, "The year is Ehrle's reckoning, from a weekday first worked out by Daniel Papebroch, a Bollandist." `uncertain`, "Ehrle fixed 1337 from a note dated by weekday at the end of the list of his miracles, as Daniel Papebroch, a Bollandist, had first reckoned it." README, "from a weekday Papebroch first worked out".
- Source: "Nun fiel aber, wie schon Papebroch berechnete, diese fer. VI … nur in den J. 1317, 1337 und 1348 auf den 13. Juni" (EHRLE1 l.27792-27795). Papebroch reckoned the years in which that weekday fell on 13 June. No held line says he worked out the weekday or fixed 1337 (ASMAR3 l.24810-24817 gives the day only). In the `uncertain` sentence, "it" is heard as 1337.
- Fix (`dates`): "The year is Ehrle's reckoning, from a weekday note, using the years Daniel Papebroch, a Bollandist, had found for that weekday." Fix (`uncertain`, first two sentences): "When he died. Ehrle fixed 1337 from a note at the end of the list of his miracles, dated by weekday. Daniel Papebroch, a Bollandist, had already found that in the first half of the fourteenth century that weekday fell on 13 June only in 1317, 1337 and 1348." README: "His death year is Ehrle's reckoning, using Papebroch's list of the years the weekday fits, and the card says so; the Bollandists give 14 June for the day."

**B2-M3 (card `uncertain`, twice: a held first name not used).**
- Current text: "Professor F. Tocco" (authorship item and 1331 item).
- Source: "scritti di Felice Tocco" (CARLINI l.1461, OCR "FeLIcE"); "Felice Tocco" (SABAT l.2510; `actus-beati-francisci_…_sabatier1902.txt` l.207); "Prof. F. Tocco" (EHRLE3 l.22702).
- Fix: "Professor Felice Tocco" at the first mention (the authorship item), and "Felice Tocco" in the 1331 item (as in B2-B3). Add CARLINI l.1461 to the records' 1331 claim.

**B2-M4 (card `legacy.traces`, Rader: half of Rader's sentence).**
- Current text: "Ambrose of Camaldoli, Rader adds, found that version obscure, word for word, though Ambrose does not name him."
- Source: "et quamvis Angeli nomen non exprimat, ita tamen describit et depingit illum, ut res oculis tangi possit" (PG88 l.43306-43307). Rader grants that the name is missing, and says the description is unmistakable. Cut off there, the clause reads as a doubt that Rader rejects.
- Fix: "Ambrose of Camaldoli, Rader adds, found that version obscure, word for word. Ambrose does not name him, Rader says, but describes him past mistaking."

**B2-M5 (card `dates`: a colon that holds back the day).**
- Current text: "He died in June 1337 at the hermitage of Santa Maria de Aspro: on the 15th, Oliger and Ehrle say."
- Source: CLAR l.1398-1399; EHRLE1 l.27773-27774.
- Fix: "He died in June 1337 at the hermitage of Santa Maria de Aspro, on the 15th by Oliger and Ehrle."

**B2-M6 (card `sources`: the term's form).**
- Current text: "Archiv für Litteratur- und Kirchengeschichte des Mittelalters IV: a fraticelli trial of 1334".
- Source: everywhere else the card writes "Fraticelli" (`knownFor` aside, the `uncertain` 1334 item, `tradition`).
- Fix: "… IV: a Fraticelli trial of 1334".

---

### records.json (these profiles)

- **bernardino-of-siena.** Every new or changed claim's lines were opened, and they say what the claims quote. Three faults remain. The Observance witness is misplaced (B2-M1). The contested side "Bernardino himself and Banchi: a Roman hearing on his teaching before June 1427" gives no witness for "before June 1427". The date is Banchi's note on Martin V naming him bishop on 4 June 1427 (BANCHI1 l.6410-6412), joined to the introduction's "il papa lo promosse al vescovado" after Rome (l.318-324). Add l.6410-6412 to that side. The sending to L'Aquila rests on the death claim's Vespasiano quote, which already holds "gli fu commesso … che andasse all' Aquila a predicare" (B2-B1 needs no new claim).
- **angelo-clareno.** The death claim needs Ehrle's hedging note (B2-B2). The 1331 contested side drops Raynaldus's "propensus videtur" (B2-B3). The Bollandists claim says the 14 June rests on Robert of Mileto's miracles. The card's "the same contemporary miracles" also needs the line showing that Ehrle's list is Robert's collection: "Infrascripta misit dominus Rubertus de Mileto Gentili (de Fulgineo) modico tempore post obitum fr. Angeli de Clarino" (EHRLE1 l.28490-28492). Add it to the claim. The Sabatier, 1334-trial, Rader, Simon and Lea claims were checked and stand. The birth-year claim's "one witness" stands after the all-file search.

### Checklist summary

| # | Item | bernardino-of-siena | angelo-clareno |
|---|---|---|---|
| 1 | Each sentence's source establishes it | Fail (B2-B1) | Fail (B2-B2, B2-B3) |
| 2 | Quotes verbatim | Pass | Pass |
| 3 | No invented detail | Fail (B2-B1, a date added to the sending) | Pass |
| 4 | Reading aids, no AI tells | Pass | Pass (the 26- and 27-word sentences are noted in B2-B2 and B2-M1) |
| 5 | No role for a named witness | Pass | Pass |
| 6 | Partisan or hostile witness marked | Pass | Pass |
| 7 | Contested claims shown both sides | Pass | Fail (B2-B2 drops Ehrle's hedge; B2-B3 drops Raynaldus's) |
| 8 | Common names have a place | Pass | Pass |
| 9 | One term for one thing | Pass | Pass (B2-M6 is a capital only) |
| 10 | Story, scene first, disputes in place, length | Pass (it opens on the sow-thistle and flows across the splices) | Pass (it opens on the Avignon hearing and flows) |
| 11 | `grade_text` | Pass | Pass |
| 12 | Card order, missing fields, caveat repeated | Pass (stale Mansi title, B2-M3) | Pass |
| 13 | Audio tags | Pass (byte match) | Pass (byte match) |
| 14 | List line kept; Who test | Pass | Pass |

Card form: both cards are in the pattern's field order. Each `briefLength` reads "about 2 minutes 30 seconds", the house form for 405 and 406 words. Each `keyWorks` has at most three entries. `ownWords` holds the subject's works (Clareno's Historia is marked "attributed", as the card's authorship item requires). `sources` lists every work the briefs rely on.

### Grades

| Brief | Words (`wc -w`) | FK | Flesch | With the fixes above |
|---|---|---|---|---|
| bernardino-of-siena | 405 | 7.21 | 69.87 | 405, FK 7.21, Flesch 69.87 |
| angelo-clareno | 406 | 7.93 | 63.29 | 406, FK 8.16, Flesch 62.55 |

Both match R1_changes and sit inside the README ranges (403-406 words; grade 6.6-8.6; Flesch 61.4-72.5). Sentences over 25 words: Bernardino, one (26, the closing line, counted to the first full stop inside the quotation). Clareno, two (26 and 27). With the fixes, Clareno still has a 26 and a 27.

### Count

- **bernardino-of-siena:** 1 blocking (B2-B1), 4 minor (B2-M1 to B2-M4).
- **angelo-clareno:** 2 blocking (B2-B2, B2-B3), 6 minor (B2-M1 to B2-M6).

## Era 6 Who batch 2, round 2 recheck: PART C

**Scope.** `william-of-ockham` and `nicholas-cabasilas`: every round 1 finding of Part C (R1_review.md l.666-950; R1_changes.md Part C), every line changed in `git diff ba5a9f37..d7c4490c` for the brief, card, audio and `records.json` entry of each, and the README lines about them. Every double-quoted passage in both briefs and cards was checked again, changed or not, and the card form (item 6) was checked whole. Branch `claude/cft-who-era6-batch2` at d7c4490c. No repo file was edited. No web, paid or model call was made.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its checklist, lessons.md, the R1 Part C findings and R1_changes Part C, then the diff for these two people. For every changed line I opened the cited source with 20 or more lines of context and asked who is speaking, what document the line annotates, and whether a condition or hedge was dropped. Quotations were matched by grep against the file (whitespace, case and hyphen breaks allowed). New absence notes were searched across all of `cic/texts/` with the name forms Cabasil-, Kabasil-, Καβάσιλ-, Καβασίλ- (34 files, the Library index files included), with "Nicol-" next to them, and with lay/laic/Laie. `grade_text` was run on the current briefs and on the briefs with this round's fixes. The audio was compared by script against the brief with the two tags added. Spelling: the brief for this round lists "American spelling outside quotations" as a fault, but Decision-Log 77 and the batch entries (Decision-Log l.2719, 2751) require American spelling in the profiles' own prose. The lessons list says the same ("British spelling outside quotations"). I checked against that rule. No British form is in either profile's own prose.

**Files opened (cic/texts/).**
- LEA3 `lea_history-of-the-inquisition-of-the-middle-ages-v3_1888.txt`, l.54, 6485-6510, 6810-6856.
- BUL5 `bullarium-franciscanum_v5-lat_eubel1898.txt`, l.1-10, 18-80, 3445-3458, 42395-42452, 42495-42520, 72720-72745, 86108-86120.
- GLASS `glassberger_chronica-analecta-franciscana-v2-lat_1887.txt`, l.1-3, 98-125, 11140-11156, 13525-13535.
- CARL `carlini_fra-michelino-e-la-sua-eresia-ita-lat_1912.txt`, l.1-4, 190-199, 4694-4702, 5322-5340, 6262-6295, 8678-8705.
- SCHOLZ `scholz_unbekannte-kirchenpolitische-streitschriften-v2-lat_1914.txt`, l.21020-21030, 22676-22698, 25835-25870.
- FZ `fasciculi-zizaniorum_shirley1858.txt`, l.1-4, 3072-3090, 3355-3366.
- GERSON `gerson_opera-omnia-tomus-2-pars-1-tractatus-ad-schisma-lat_dupin1706.txt`, l.27006-27020, 27198-27212.
- LUTHER4 `luther_works-v4-selected_various1931.txt`, l.16766-16782.
- HILTON `hilton_scale-or-ladder-of-perfection_dalgairns1908.txt`, l.1-8, 147, 205-222, 2426-2436.
- CATHAY `cathay-and-the-way-thither_vol3-...yule-cordier1914.txt`, l.10488-10496.
- CANT2 `cantacuzenus_historiarum-libri-iv-v2-grc-lat_schopen1831.txt`, l.32135-32141.
- CANT3 `cantacuzenus_historiarum-libri-iv-v3-grc-lat_schopen1832.txt`, l.6393-6400, 16588-16640.
- PG150 `palamas_opera-omnia-pg150-grc-lat_migne1865.txt`, l.1-12, 155-200, 250-265, 336-350, 26050-26110, 35850-35868, 36552-36600, 44335-44395, 49305-49322.
- PG161 `bessarion_opera-omnia-pg161-grc-lat_migne1866.txt`, l.110880-110890, 128926-128932.
- GASS `cabasilas_mystik-vom-leben-in-christo-grc-deu_gass1849.txt`, l.1-8, 1225-1240, 1365-1395, 1768-1800, 1872-1942.
- PHRAN `sphrantzes-cananus-anagnostes_chronicles-grc-lat_bekker1838.txt`, l.7950-7996.
- PO15 `patrologia-orientalis-tomus15_petit-documents-concile-de-florence-purgatoire-grc-fra_graffin-nau1927.txt`, l.1-10, 110-125, 193, 505-650, 1288, 35785-35803, 45375-45410.
- PG155 `symeon-thessalonica_opera-omnia-pg155-grc-lat_migne1866.txt`, l.350-360, 378-388.
- GREG2 `gregoras_byzantina-historia-v2-grc-lat_schopen1830.txt`, l.1, 168, 36466-36480, 47124-47132.
- ACTA `acta-et-diplomata-graeca_acta-patriarchatus-...miklosich-mueller1860.txt`, l.14060-14068.
- NPNF214 `npnf214_seven-ecumenical-councils.xml`, l.4888-4896 (a namesake, Cabasilas of Durazzo).
- Ehrle-Denifle Archiv I, l.27540 ("der Bollandist Papebroch").
- Census: `cic-website/data/world-census.json` (working tree; `origin/main` is not fetched in this checkout), movement `franciscan-order-era-6`, people list.

**Quotations.** These are all the double-quoted passages in both briefs and both cards.
- Ockham brief: "there was nothing sure but Scripture". LEA3 l.6825 reads "There  was  nothing  sure  but  Scripture ;". It matches apart from case, and the full stop now sits outside the marks. Pass.
- Ockham brief: "the glory and the reproach of his order". FZ l.3081-3082 reads "Ockham,  the  glory / and  the  reproach  of  his  order,". Pass.
- Ockham card, legacy remembered: "the glory and the reproach of his order". FZ l.3081-3082, as above. Pass.
- Ockham card, legacy traces: "Occam, my dear master". LUTHER4 l.16777 reads "Occam, my dear master, writes". It is the 1931 English. Pass.
- Ockham card, uncertain: "more than doubtful". LEA3 l.6851 reads "but  this  is  more  than  doubtful,". Pass. R1 cited l.6838; the line is 6851 in this file.
- Cabasilas brief and card: no double quotes. Every Greek, Latin and German line is told in modern words without marks. Pass.

**Audio.** Both scripts equal the brief, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph and no other tag (checked by script). Pass for both. Any brief fix below needs the audio rebuilt.

---

### william-of-ockham

**R1 findings: applied?**

| R1 id | Status |
|---|---|
| C-B1 (1323 summons condition) | OK. "They were to do so if they found he had preached the friars' view" matches "si ea repereritis veritate fulciri" (BUL5 l.42444) and Lea (LEA3 l.6500-6501). Dropping "at Bologna" is fine, since the bishops of Bologna are named. |
| C-M1 (Benedict XII loose from Lea) | OK. "poured out works in their defense" stands for "poured forth ... in defence of the cause" (LEA3 l.6816-6818). |
| C-M2 (quote heard as narrator's; stop) | OK. |
| C-M3 (qualifier dropped from his words) | Applied in the short form, but the new verb shifts the Latin. See C2-M2. |
| C-M4 (thesis opener) | OK. |
| C-M5 ("lords in England") | OK. |
| C-M6 ("it"; Carlini's role) | OK. |
| C-M7 (Lea, Wadding, Glassberger at first mention; cuts) | Applied. Glassberger: GLASS l.1, 106 ("an. 1508"). Wadding: BUL5 l.86114-86116. Lea 1888: LEA3 l.54. R1_changes' cap-holding wording "the papal letters' editor of 1898" reads badly. See C2-M1. |
| C-M8 (Dialogus line is Ambrose's) | OK. Matches SCHOLZ l.22683-22696. |
| C-M9 (Gerson's argument with no context) | OK on the facts. The new sentence runs to 39 words. See C2-M5. |
| C-M10 (Luther cut off) | OK. Matches LUTHER4 l.16776-16779. |
| C-M11 (Dalgairns 1870) | OK. HILTON l.212-217; 1908 at l.147. |
| C-M12 (otherNames) | OK. "Wilhelmus Occam" is at SCHOLZ l.21026. |
| C-M13 (Carlini ownWords) | OK. Removed and folded into the "about" entry. |
| C-M14 (card names: Lea, Carlini, Riezler) | Applied. The new Lea and Riezler clauses leave a "he" that now reads as Lea. See C2-M3 and C2-M4. Müller is still without a role or time: Carlini gives only "il MuLLER, o. c." (CARL l.6278), and no other line of the file names him. Log him with Nicolaus Minorita in the Open-Gaps entry. |
| C-M15 (Wyclif's line) | OK, in the short form. The cut gloss is reasonable. |
| C-M16 (tombstone) | OK. CARL l.8692-8699 ("una lastra ... EX ANGLIA"). |
| C-M17 (README quotation list) | OK. |
| Not counted, Perugia 1322 | Added to records as a third side of the 1323-identity claim. The lines read as cited (CARL l.4698-4700, 5326-5329; BUL5 l.42504-42507; CATHAY l.10492-10494). |

**C2-M1 (brief para 3: a stacked possessive).**
- Current text: "Conrad Eubel, the papal letters' editor of 1898, thinks him more likely Ockham than William of Alnwick, another Englishman."
- Problem: "the papal letters' editor of 1898" reads as a title. Heard aloud, "of 1898" can attach to the letters. The year is held at BUL5 l.70-77 ("CONRADO EUBEL ... ROMAE, MDCCCXCVIII").
- Fix (+1): "Conrad Eubel, who edited the papal letters in 1898, thinks him more likely Ockham than William of Alnwick, another Englishman."
- Offset: C2-M2 (−1).

**C2-M2 (brief para 5: "brought persecution on himself" shifts the Latin).**
- Current text: "He brought persecution on himself knowingly, he says."
- Source: "Persecutioni igitur scienter me ingerens et eam fugere non intendens" (SCHOLZ l.25861-25862). "Me ingerens persecutioni" means "putting myself in persecution's way". "Brought persecution on himself" can be heard as "caused it by his own fault", which he does not say.
- Fix (−1): "He walked into persecution knowingly, he says."
- Records: in the tract claim, change "the brief says only that he brought persecution on himself knowingly" to "the brief says only that he walked into persecution knowingly".

**C2-M3 (card knownFor: the pronoun now captures Lea).**
- Current text: "In the summary of Henry Charles Lea, writing a history of the Inquisition in 1888, he argued that a pope can fall into heresy, and so can a council."
- Problem: after the clause on Lea, "he" reads as Lea.
- Fix: "In the summary of Henry Charles Lea, writing a history of the Inquisition in 1888, William argued that a pope can fall into heresy, and so can a council."

**C2-M4 (card dates: "he notes" reads as Lea, in a 41-word sentence).**
- Current text: "Armando Carlini, in a 1912 study of Michael of Cesena, dates the flight to the night of 26 May 1328, after Nicolaus Minorita, whom Lea also cites; he notes that Riezler, writing in 1874, and Müller give the 25th."
- Source: the note giving Riezler and Müller is Carlini's (CARL l.6278-6280). The nearest "he" is Lea.
- Fix: "Armando Carlini, in a 1912 study of Michael of Cesena, dates the flight to the night of 26 May 1328, after Nicolaus Minorita, whom Lea also cites. Carlini notes that Riezler, writing in 1874, and Müller give the 25th."

**C2-M5 (card legacy traces, Gerson: one 39-word nested sentence).**
- Current text: "Jean Gerson wrote in 1418, near the close of the Council of Constance, in a tract on an appeal from the pope to a council, that William had argued the matter at length in his Dialogus."
- Source: GERSON l.27010-27016 ("Scriptus est iste Tractatus Anno 1418. sub finem Concilii Constantiensis occasione appellationis Oratorum Polonorum ad futurum Concilium") and l.27205-27206 ("latissime & studiosissime prosecutus est, & fundavit Ockam in Dialogo suo").
- Fix (no new claim): "In 1418, near the close of the Council of Constance, Jean Gerson wrote a tract on an appeal from the pope to a council. He writes there that William had argued the matter at length in his Dialogus."

**C2-M6 (records: two date claims rest on the Library header).**
- Current: "Eubel edited the volume in 1898 ... (file header and title page)", witness "BUL5 ... l.1-10 (header)". "Carlini's book dated 1912", witness "CARL ... l.1-6 (header, quoting the title page)".
- Source: the title pages are held in the scans: BUL5 l.70-77 ("A / CONRADO EUBEL / ... / ROMAE, MDCCCXCVIII") and CARL l.195-198 ("BOLOGNA / DITTA NICOLA ZANICHELLI / 1912."). Both lines changed in round 1 (C-M6, C-M7), so their witnesses are in scope.
- Fix: change the witnesses to "BUL5 l.70-77 (title page)" and "CARL l.195-198 (title page)".

**Checked and true (changed lines).** "a few friars" and the flight (CARL l.6269-6275). "Two days later" and the 1330 doctors (BUL5 l.72730-72739: "pluribus doctoribus assignata ... qui iam multos articulos declaraverunt haereticales"). "Letters ... went to Germany and England" (BUL5 l.3451-3455). The 1323 bull (LEA3 l.6504-6511), with the summons letter dated 1 December 1323 (BUL5 l.42407). The Munich line (GLASS l.11153-11156). The Munich stone with "EX ANGLIA" (CARL l.8698-8699). Gerson's occasion (GERSON l.27012-27016). The census people list for `franciscan-order-era-6` is Clareno, Ubertino and John XXII, so the README's "not on its people list" is true.

**Not counted.** "For twenty years, Lea writes" sits after the Munich sentence, but Lea starts the twenty years from the 1324 letter (LEA3 l.6812-6817). Nothing in the brief states a start year, so this is not wrong.

---

### nicholas-cabasilas

**R1 findings: applied?**

| R1 id | Status |
|---|---|
| C-B2 (archbishop question; Gass misread; Synodikon missed) | Brief applied, with Gass's hedge misplaced (C2-M2). Card item 1 and the records side were applied, but they put a year in Gass's mouth that he does not give (C2-B2). The README and the claim tag disagree (C2-M6). |
| C-B3 (Petit reversed) | OK. Card item 5 and records match PO15 l.513-517, 540-544, 584-587, 630-640. "Editing ... in 1920" is held: Petit's fascicle carries "Paris, 16-25 juin A920" (PO15 l.193) and a preface of March 1918 (l.1288). The header's own lines 35801 and 45405 belong to other fascicles. |
| C-M18 ("prayed for a new patriarch") | OK. CANT3 l.16594-16596; Latin "divina sancti Spiritus gratia invocata" (l.16627). |
| C-M19 (who-line; Philotheos's see) | Applied, but the who-line was put inside Kantakouzenos's attribution (C2-B1). "Philotheos, bishop of Heraclea" is right (CANT3 l.16597, 16628). |
| C-M20 (Life in Christ paragraph) | Applied. The fix leaves a pronoun that Gass captures (C2-M1) and a God-came-down line with no witness (C2-M3). The readings themselves match PG150 l.35858-35860, 36562-36568, 36579-36582 and 44358-44389. |
| C-M21 (Migne and Fabricius roles; long sentence) | Applied. The year 1865 has no records witness (C2-M7). |
| C-M22 (process-narration opener) | OK. |
| C-M23 (Phrantzes names the archbishop) | OK. PHRAN l.7957-7962 ("τῇ ἀδελφῇ τῶν τριῶν ἀρχιερέων ... τὸν ἀδελφὸν αὐτῆς Καβάσιλαν ἀρχιερέα"). |
| C-M24 (otherNames) | OK. "Καβάσιλας Νικόλαος" is at CANT3 l.6395. |
| C-M25 (Kantakouzenos volume 2) | OK. |
| C-M26 (names and terms at first mention) | Applied. "Mark of Ephesus, the Greek spokesman at Florence" sits inside Gass's witness and leaves out Bessarion (C2-M4). "Boivin, who edited Gregoras's history" says more than is held (C2-M5). "The Bollandist Daniel Papebroch" is held (Ehrle-Denifle Archiv I, l.27540: "der Bollandist Papebroch"). The other glosses are OK. |
| C-M27 (Gregoras's friend; README) | OK for the friend. The same README sentence now misstates the archbishop tag (C2-M6). |
| C-M28 (Symeon's date; Palamite tie) | OK. PG155 l.796-806; the Palamite claim now has three witnesses. |

**C2-B1 (brief para 1: the narrator's who-line put inside Kantakouzenos's attribution).**
- Current text: "The third, John Kantakouzenos writes in his history, was Nicholas Cabasilas, a writer on the sacraments who was still a layman."
- Source: Kantakouzenos writes only "καὶ Νικόλαον τὸν Καβάσιλαν, ὄντα ἔτι ἰδιώτην" (CANT3 l.16599-16601; Latin "privatum adhuc Nicolaum Cabasilam", l.16629). He does not call him a writer on the sacraments. The records claim says so itself: "'A writer on the sacraments' rests on his works in PG150."
- Why it matters: the sentence says a named witness wrote something he did not write. This is a witness swap made in round 1's fix.
- Fix (21 words, the same as now): "The third was Nicholas Cabasilas, a writer on the sacraments. He was still a layman, John Kantakouzenos writes in his history."
- The scene still opens the brief. The who-line comes at sentence 3, and the witness sits inside the sentence it covers.

**C2-B2 (card uncertain item 1; records contested side: a year put in Gass's mouth).**
- Current card text: "Gass presumes he took the see some years after 1353 and finds him named archbishop no earlier than 1354."
- Current records side: "Gass, presuming the see some years after 1353, not named archbishop before 1354 (GASS l.1373-1375, 1781-1785)".
- Source: Gass gives no 1353, and the year appears nowhere in his file. His "some years" follow Palamas and the synod of 1351: "von wo ihn dieser zur Theilnahme an der vierten Synode von Constantinopel berief (1351) ... Es wird nirgends gesagt, ob er nach der Synode doch noch Aufnahme in dem Bisthum gefunden ... wahrscheinlich hätte sich Thessalonich nicht sogleich einen zweiten Anhänger des Cantacuzen aufdrängen lassen. Muthmasslich wird also Cabasilas erst nach einigen Jahren das Erzbisthum angetreten haben, ungewiss unter welchen Umständen" (GASS l.1773-1784). Elsewhere he says only "nach 1350" (l.1375).
- Why it matters: 1353 is Kantakouzenos's year (CANT3 l.16593). Put in Gass's mouth, it makes Gass look as if he had weighed Kantakouzenos, which he did not.
- Fix, card: "Gass presumes he took the see only some years after the synod of 1351, and finds him named archbishop no earlier than 1354."
- Fix, records side: "Gass, presuming the see only some years after the synod of 1351, and not named archbishop before 1354 (GASS l.1373-1375, 1773-1786)".

**C2-M1 (brief para 7: "he" can be heard as Gass).**
- Current text: "The life in Christ begins and grows here, he wrote in his book of that name, and is made complete in the world to come."
- Problem: the paragraph before ends on Gass ("Gass finds him named among the followers of Gregory Palamas"). Para 2 says Gass printed this very book. So "he wrote in his book of that name" can be heard as Gass.
- Fix (±0): "The life in Christ begins and grows here, Cabasilas wrote in his book of that name, and is made complete in the world to come."

**C2-M2 (brief para 9: Gass's hedge on the wrong point).**
- Current text: "Gass presumes so too, and finds him named archbishop no earlier than 1354."
- Source: Gass states the succession plainly: "verwaltete dasselbe Amt zehn Jahr nachher (nach 1350)" (GASS l.1374-1375). His "Muthmasslich" covers only the late start (l.1782-1784). As written, the brief makes him doubt the succession itself.
- Fix (−2): "Gass agrees, and finds him named archbishop no earlier than 1354."

**C2-M3 (brief para 7: the source's claim heard as the narrator's).**
- Current text: "People did not go up to God; God came down to them."
- Source: "Οὐ γὰρ αὐτοὶ πρὸς τὸν Θεὸν ἐκινήθημεν οὐδὲ ἀνέβημεν, ἀλλ᾽ αὐτὸς πρὸς ἡμᾶς ἐλήλυθε καὶ κατῆλθεν" (PG150 l.36579-36582). It is fourth in the paragraph, three sentences after the only "he wrote". In audio it is heard as the narrator's own theology, in a contrast shape.
- Fix (+2): "People did not go up to God, he wrote; God came down to them."
- Offset: C2-M2 (−2).

**C2-M4 (card legacy traces: a gloss inside Gass's witness, dropping Bessarion).**
- Current text: "Gass writes that Mark of Ephesus, the Greek spokesman at Florence, drew heavily on him and copied him."
- Source: Gass says only "von Männern wie Marcus Eugenicus stark benutzt und ausgeschrieben" (GASS l.1878-1880). The role comes from Petit: "ces deux prélats avaient seuls reçu mission de répondre aux Latins", meaning Mark and Bessarion, at Ferrara (PO15 l.627-641).
- Fix: "Gass writes that Mark of Ephesus drew heavily on him and copied him. Louis Petit, editing the Florence documents on purgatory in 1920, names Mark and Bessarion as the two Greek prelates sent to answer the Latins at Ferrara."
- Then shorten card item 5's first mention, since Petit now has his role in legacy: "Louis Petit notes that a tract on purgatory has been given to Nilus, to Nicholas and to Barlaam of Calabria."

**C2-M5 (card uncertain item 4: "edited" is more than is held).**
- Current text: "Boivin, who edited Gregoras's history, and Gass take him for Nicholas."
- Source: the Bonn title holds Boivin's notes, not his edition: "cum annotationibus ... Io. Boivini" (GREG2 l.1, 168, 36471). Migne cites "Boivinus notis ad Gregoram" (PG150 l.50236). The identification is in the notes (GREG2 l.47127).
- Fix: "Boivin, in his notes on Gregoras's history, and Gass take him for Nicholas."

**C2-M6 (README and records: the archbishop claim's tag is stated two ways).**
- Current README text: "When he became archbishop of Thessalonica (Fabricius, Gass and a Thessalonica record say he did), how he was Nilus's nephew, whether the "Kabasilas of the sakellion" is he and which anti-Latin writings are his are tagged Contested".
- Records: the claim "Archbishop: ..." is tagged "Widely Accepted". The `contested_claims` entry beside it has one real side. Its second side is "A date and a silence", and no held witness denies the see (R1 C-B2, rechecked: no line of the 34 files says he stayed a layman or never held it; the "lay theologian" phrases are only Library headers, GASS l.2 and the Library README).
- Fix, README: "How he was Nilus's nephew, whether the "Kabasilas of the sakellion" is he and which anti-Latin writings are his are tagged Contested. That he became archbishop of Thessalonica is tagged Widely Accepted (Fabricius, Gass and a Thessalonica record), and no held line gives the date; Gregoras's old friend is Boivin's identification, followed by Gass."
- The coordinator still has R1's open call: keep the `contested_claims` entry, or move "when" wholly to the existing absent_details note. Either way the README must match the tag.

**C2-M7 (records: the brief's "In 1865" has no witness, and the volume's own OCR reads 1863).**
- Current: the Fabricius-notice claim cites only Migne's name (PG150 l.161, 195). No records line holds the year the brief and card give.
- Source: the PG150 title page OCR reads "1863" (PG150 l.261). The list of Migne's volumes reads "CL (1865)" (PG161 l.110885). The Library header weighs both (PG150 l.6), and a header is not a witness.
- Fix, records: add to that claim "Year: 'CL (1865)' in the list of Migne's volumes (PG161 l.110885); this scan's title page OCR reads '1863' (PG150 l.261)". The brief and card can keep 1865.

**C2-M8 (card sources: an ownWords entry names a notice that is not his).**
- Current text: ownWords title "Commentary on the Divine Liturgy, The Life in Christ, the sermon against usurers and the encomium of St Theodora, with the notice from Fabricius, in Patrologia Graeca 150".
- Problem: the notice is Fabricius-Harles's (PG150 l.26062), and ownWords holds only the subject's words. The line is unchanged since round 1, but item 6 of the round 2 brief checks it.
- Fix: drop ", with the notice from Fabricius" from that title. Add an "about" entry: title "Notice from Fabricius's Bibliotheca Graeca, in Patrologia Graeca 150", author "J. A. Fabricius, in Harles's edition; J.-P. Migne (ed.)", date "1865", language "Latin", file `cic/texts/palamas_opera-omnia-pg150-grc-lat_migne1865.txt`.

**Checked and true (changed lines).** Kantakouzenos at 1346 and 1349 (CANT2 l.32136-32139; CANT3 l.6394-6400). The Fabricius notice: "ex fratre nepos", "in munere successor", "saepe confundi", "Vir fuit omnino doctus" (PG150 l.26066-26080). "Most holy archbishop" in the brief tells "τοῦ ἁγιωτάτου μητροπολίτου Θεσσαλονίκης" (GASS l.1919); the card says "metropolitan". Both are fair, and "archbishop" keeps the brief to one term. The Synodikon is the church of Thessalonica's own record, quoted by Gass from Le Quien (GASS l.1884-1888, 1938-1940). Card role and knownFor, "civil war of the 1340s" and "chrismation (the anointing with chrism)". Card item 2 on Phrantzes. Card item 5 on Petit. The new card item 1 line "No witness gives the date or tells how he took office" was searched as above, and Gass's own "ungewiss unter welchen Umständen" (l.1784) agrees with it.

**Not counted (for the coordinator).** Allatius, quoted in PG155 l.383, says Nicholas "sub Manuele florebat", which is later than Fabricius's "about 1350". It is a held later witness on his dates that the card does not use. The card's "flourished about 1350" is told as the notice's and is not wrong.

---

### records.json (these profiles)

- **william-of-ockham.**
  - The summons condition, the Dialogus with Ambrose, Dalgairns 1870, Christ's leave to flee, Gerson's occasion, Luther's "These are the best of them", the Munich stone and the Perugia side are present and read as cited.
  - C2-M2: the tract claim's note on the brief's wording needs the new verb.
  - C2-M6: the Eubel 1898 and Carlini 1912 claims should cite the held title pages, BUL5 l.70-77 and CARL l.195-198.
  - The "Letters ordering his arrest to bishops and lords" claim heading still says "lords in ... England". Its contents name the King of England correctly, and the brief no longer says it. A heading fix ("to German bishops and lords, the English bishops and the King of England") is optional.
- **nicholas-cabasilas.**
  - C2-B2: the archbishop contested side needs the 1351 synod in place of 1353.
  - C2-M7: the Fabricius-notice claim needs the 1865 witness.
  - C2-M6: the tag on the archbishop claim must match the README.
  - If C2-M4 is applied, add a claim: "Petit: Mark of Ephesus and Bessarion 'avaient seuls reçu mission de répondre aux Latins' (PO15 l.627-641)".
  - Everything else, including the Petit side, the Synodikon lines and the Palamite tie with three witnesses, reads as cited.

### Checklist summary

| # | Item | william-of-ockham | nicholas-cabasilas |
|---|---|---|---|
| 1 | Each sentence sourced, source establishes it | Pass (C2-M2 is precision) | Fail (C2-B1, C2-B2) |
| 2 | Quotes verbatim | Pass (5 checked) | Pass (none) |
| 3 | No invented detail | Pass | Fail (C2-B2: a year put in Gass's mouth) |
| 4 | Reading aids, no AI tells | Fail, minor (C2-M1, C2-M3, C2-M4, C2-M5) | Fail, minor (C2-M1, C2-M3) |
| 5 | No role standing in for a witness | Pass | Pass |
| 6 | Partisan or hostile witness marked | Pass | Pass |
| 7 | Contested claims both sides, not settled | Pass | Pass (archbishop told with three witnesses; tag consistency is C2-M6) |
| 8 | Common names and scholars at first mention | Pass (Müller to the gap log) | Fail, minor (C2-M4, C2-M5) |
| 9 | One term for one thing | Pass | Pass |
| 10 | Story, scene, disputes in place, length | Pass | Pass (scene first, who-line at sentence 3 after C2-B1) |
| 11 | Readability | Pass (8.04 / 63.41) | Pass (8.11 / 61.41) |
| 12 | Card order, missing fields absent, caveat repeated | Pass | Fail, minor (C2-M8: ownWords) |
| 13 | Audio tags only in the script, at start and close | Pass | Pass |
| 14 | Keeps the list line; Who test | Pass | Pass |

Card form (item 6), both profiles: the field order is name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources, as in the pattern. keyWorks has three entries. briefLength reads "about 2 minutes 30 seconds", the house form for the 97 cards near 405 words, and it matches 405 and 406 words. The sources list every work each brief relies on. Ockham's ownWords holds only Scholz's edition of his tracts. For Cabasilas's ownWords, see C2-M8.

### Grades

| Profile | Words (`wc -w`) | FK | Flesch | With this round's fixes |
|---|---|---|---|---|
| william-of-ockham | 405 | 8.04 | 63.41 | 405 words, FK 8.07, Flesch 63.19 (C2-M1, C2-M2) |
| nicholas-cabasilas | 406 | 8.11 | 61.41 | 406 words, FK 7.99, Flesch 61.45 (C2-B1, C2-M1 to C2-M3) |

Both briefs stay at about 2:30. No fix adds net words, and Cabasilas's Flesch stays above 60. Rescore after any further edit.

### Count

- william-of-ockham: 0 blocking, 6 minor (C2-M1 to C2-M6).
- nicholas-cabasilas: 2 blocking (C2-B1, C2-B2), 8 minor (C2-M1 to C2-M8).

## Era 6 Who batch 2, round 2 recheck: PART D

**Scope.** `gregory-palamas` and `gregory-of-sinai`: every round 1 finding in Part D (D-B1 to D-B4, D-M1 to D-M20) and how R1_changes says it was applied; every line changed between `ba5a9f37` and `d7c4490c` in the two briefs, cards, audio files and records entries, and the README lines on the two men; all quotations in double marks (items 3 and 6 of the brief). Branch `claude/cft-who-era6-batch2`. No repo file edited. No network, paid or model call.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its checklist, lessons.md, R1_review.md l.951-1184 and R1_changes.md Part D (l.60-72). I diffed the two men's files across `ba5a9f37..d7c4490c` (word diff for the briefs). For each changed line I opened the cited source with 20 or more lines around it and read the Greek, Latin, Church Slavonic, Croatian and German myself. I asked of each note what document it annotates and who speaks. I searched every held file naming Palamas (Palama-, Παλαμ-, Палам-) for 1296, 1359 and 1362, and the two Synaxaristes volumes for a Palamas death year, before accepting the moved absent_details note. I diffed each audio file against its brief, checked card field order, counted words with `wc -w`, listed sentences over 22 words by script, and scored the briefs and my scratch fixes with `engine.m1.gates.grade_text`.

**A note on spelling.** This brief's item 5 names "American spelling outside quotations" as a fault. lessons.md names British spelling, and R1_changes (l.72) says British is the fault meant. Both cards use American spelling ("favor", "worshipers", "Defenses"). I did not count it, and the conflict between the two briefs should be settled once by the coordinator.

**Files opened (cic/texts/).**
- CANT1 `cantacuzenus_historiarum-libri-iv-v1-grc-lat_schopen1828.txt` l.32715-32760
- CANT2 `cantacuzenus_historiarum-libri-iv-v2-grc-lat_schopen1831.txt` l.34215-34345
- GREG3 `gregoras_byzantina-historia-v3-grc-lat_bekker1855.txt` l.13060-13200
- PALH `palamas_homiliae-41-grc_jerusalem1857.txt` l.95-110, 500-560, 1280-1292, 2105-2150
- MANSI26 `mansi_sacrorum-conciliorum-collectio-tomus-26-1344-1409-lat_welter-facsimile1901.txt` l.10175-10185, 19570-19605
- PAISK `paisius-velichkovsky_vostorgnutye-klasy-chu_optina1849.txt` l.1-60, 9825-9845
- PHIL1 `philokalia_ton-ieron-neptikon-v1-grc_tzelatis1893.txt` l.140-156
- PG150 `palamas_opera-omnia-pg150-grc-lat_migne1865.txt` l.69098-69180, 71955-71975, 72480-72500, 72555-72630
- PAISZ `paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt` l.3986-4006, 4518-4530, 4635-4665, 10515-10548, 11000-11040, 14192-14228
- MEYER `athos-monasteries_haupturkunden-fur-die-geschichte-der-athoskloster-ger-grc_meyer1894.txt` l.1-3, 3990-4015
- RACKI `racki_bogomili-i-patareni-rad-viii-hrv_jazu1869.txt` l.3490-3552, 3640-3700
- For the death-year search: BESSARION PG161 l.14612-14620 (the Gregorius there is a later patriarch, not Palamas); CHARON l.668-678 (Cabasilas, not Palamas); `nikodemos-hagiorite_synaxaristes-vol1-sep-feb-grc_1900.txt` and `-vol2-mar-aug-` (Palamas hits are incipits and indexes only).

### Quotations

Neither brief holds a double quotation mark (`grep -c '[“”"]'` gives 0 for both). Neither card holds one inside any field (checked on the parsed JSON for straight and curly quotes). There is nothing to check verbatim under item 3. Every line held only in Greek, Latin, Slavonic, Croatian or German is told in modern words with no marks. I checked each changed telling against its original under the profile below.

---

### gregory-palamas

`grade_text`: FK 7.69, Flesch 63.81. 406 words. Audio: the brief exactly, `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, no other tag. Card fields in the pattern's order.

**R1 findings: applied?**

| R1 id | Verdict |
|---|---|
| D-B1 (Anna's wish for peace) | OK. CANT2 l.34226-34227 has her running from settlement; her son, "tum quindecim natus annos", begs her (l.34233-34240); "lico persuasa mater" (l.34275). The offset "Kantakouzenos, his ally, tells this." keeps the partisan mark. |
| D-M1 (Gregoras's hedge) | OK. "nescio, utrum … an tribuendum sit divinae supremaeque iustitiae" (GREG3 l.13187-13189). "Wonders if" and "asks whether" are fair. |
| D-M2 (Philotheos's see) | OK in the brief. Card applied, but the new wording parses badly; see D2-M4. |
| D-M3 (sainthood narrowed) | OK. "μάλιστα δὲ ἀκριβῶς πεπληροφόρημαι τοῦτο … ὡς ΑΓΙΟΝ ἀπὸ τῶν θαυμάτων αὐτοῦ" (PALH l.552-555). "He" is the editor, the subject of the sentence before. |
| D-M4 ("for him", "base") | "Base" is OK. "For him" is wrongly applied; see D2-M1. |
| D-M5 (synods that upheld him) | OK. |
| D-M6 (Combefis marked hostile) | Applied, but "the tome" is ambiguous; see D2-M3. |
| D-M7 (who threw the books) | OK. "ὁ βάρβαρος", with Hyrcanus's elder son present, orders Palamas's own books "κατὰ μέσης … ῥιφῆναι θαλάσσης" and the whips (GREG3 l.13113-13115, 13127, 13140, 13148). |
| D-M8 (age when he left) | OK. "τὸν ἔφηβον ὑπερβεβηκὼς ἤδη" (PALH l.2125); "ἐπὶ πάνυ παιδικῇ τῇ ἡλικίᾳ", "aetate admodum puerili" (CANT1 l.32726, 32751-32752). Cutting "As a young man" was right. The new bare "He" captures the wrong man; see D2-M2. |
| D-M9 (sources and records) | OK on the card. One records witness is a file header; see D2-M7. |
| D-M10 (header as a side; reported speech) | OK. The "Year of death" contested_claim is gone. The note sits in absent_details, and my search found no year in a source text. |

**New findings**

**D2-M1 (brief para 1; records claim 1: "for him" is not in the edition's Latin).**
- Current text: "Through all he had suffered for him, he writes, Palamas never said or did anything base."
- Source: the Greek reads "ὅτι πολλὴν ὑπὲρ αὐτοῦ δικαίου καὶ τῆς ἀληθείας κάκωσιν ὑπενεγκών, οὐδὲν ἀγεννὲς οὔτε ἔπραξεν" (CANT2 l.34299-34303, OCR). Schopen's facing Latin gives "quod pro iustitia veritateque gravissime afflictus, usque ad extremum nihil abiectum aut fecerit, aut dixerit" (l.34334-34336). The edition's own translator reads the phrase as "for justice and truth", with no "for him". Kantakouzenos uses the same phrase earlier in the volume and sets it against "for him": "σπουδὴν ὑπὲρ αὐτοῦ, ἢ τἀληθέστερον εἰπεῖν, ὑπὲρ αὐτοῦ δικαίου", Latin "pro ipso, aut, ut verius dicam, pro iustitia" (l.11275-11276, 11305). So "αὐτοῦ" goes with "δικαίου", meaning justice itself, and "for him" misreads it. It also makes "him" mean Kantakouzenos one sentence after "his ally" meant Palamas. The partisan mark does not need it, since "his ally" carries it.
- Fix, brief: "Through all he had suffered for justice and truth, he writes, Palamas never said or did anything base." (+2). Offset: "lay in a prison inside the imperial palace" becomes "lay in prison inside the imperial palace" (−1). With D2-M2 my scratch copy is 407 words, FK 7.77, Flesch 63.26.
- Records claim 1: the witness lines for this sentence are wrong. The Greek is at CANT2 l.34299-34304 and the Latin at l.34334-34336, not l.34328-34333. Then replace "'For him' and 'base' render 'ὑπὲρ αὐτοῦ' and 'ἀγεννές'" with "'For justice and truth' follows Schopen's Latin 'pro iustitia veritateque' for 'ὑπὲρ αὐτοῦ δικαίου καὶ τῆς ἀληθείας'; 'base' renders 'ἀγεννές'."

**D2-M2 (brief para 2: a new bare "He" can be heard as Philotheos or the father).**
- Current text: "Philotheos, a patriarch of Constantinople who wrote a speech in his praise, says his father sat in the senate. He left for Athos with his two brothers, and became a monk at Vatopedi."
- Why: round 1 cut "As a young man" (right, under D-M8). The sentence now opens on "He" straight after a sentence whose subject is Philotheos and whose last man named is the father.
- Fix: "Palamas left for Athos with his two brothers, and became a monk at Vatopedi." (0 words)

**D2-M3 (card `uncertain`, the 1341 item: "the tome" points to the wrong document).**
- Current text: "François Combefis, a Dominican hostile to the tome, writes in a note printed by Mansi, after Gregoras, that no doctrine was debated at that synod."
- Source: Combefis's note is printed under the heading "CONSTANTINOPOLITANA PSEUDO-SYNODUS" (MANSI26 l.10180) and annotates its tome, the 1347 one. He objects that "damnatum Barlaamum asserit Synodus in prooemio ob Palamitarum dogma impugnatum, cum nihil de dogmate disceptatum sit in ea Synodo, ut auctor est Gregoras" (l.19592-19597). The item is about the 1341 synod, so a reader takes "the tome" as the 1341 one. The sentence is also 26 words.
- Fix: "François Combefis, a Dominican, annotates the tome of 1347 in Mansi and calls it heretical. After Gregoras, he writes that no doctrine was debated at the 1341 synod."
- Records: in the claim "Combefis's note…", change "he calls the tome" to "he calls the 1347 tome".

**D2-M4 (card `dates`: "patriarch of Constantinople and his panegyrist" parses as one title, and "panegyrist" is undefined).**
- Current text: "Philotheos, patriarch of Constantinople and his panegyrist, says he died at sixty-three."
- Source: "ΝΕΑΣ ΡΩΜΗΣ ΚΑΙ ΟΙΚΟΥΜΕΝΙΚΟΥ ΠΑΤΡΙΑΡΧΟΥ" (PALH l.1286, OCR); the encomium follows.
- Fix: "Philotheos, patriarch of Constantinople, who wrote a speech in his praise, says he died at sixty-three." (The brief's own words.)

**D2-M5 (card `place`: "Kantakouzenos" at first mention in the card has no first name or role).**
- Current text: "…and where Kantakouzenos says he was raised at court."
- Why: `place` is the card's first mention. The family name is shared, and the card names John only in `sources`. Checklist item 8. The line is unchanged, but this is a real fail on the item.
- Fix: "…and where the emperor John Kantakouzenos says he was raised at court."

**D2-M6 (records, the capture claim: the old sentence stands beside the new one that corrects it).**
- Current text: "Gregoras's hostile account reads the capture as divine justice. … Gregoras offers divine justice as one of two causes: 'nescio, utrum … an tribuendum sit divinae supremaeque iustitiae'". GREG3 is also cited twice in the witness field.
- Why: this is a fix laid on a fix. The first sentence is the one D-M1 found wrong, and the claim now says both things.
- Fix: delete "Gregoras's hostile account reads the capture as divine justice." Merge the witness to "PALH l.7280-7433; GREG3 l.13053-13148, 13160-13163, 13186-13193; MANSI26 l.19735-19741".

**D2-M7 (records, the Paisius Slavonic claim: line 1 is the Library file header).**
- Current text: witness "PAISK … l.1, 9835".
- Source: l.1 is the header the Library thread added. The book's own title page reads "НѢСКОЛЬКО ПЕРЕВОДОВЪ ИЗЪ СВЯТЫХЪ ОТЦЕВЪ СТАРЦА ПА[И]СІЯ ВЕЛИЧКОВСКАГО" (l.29-41, OCR). The contents list has "Григорія Паламы Архіепископа Ѳессалонитскаго, о молитвѣ" (l.9835-9836).
- Fix: witness "PAISK l.29-41 (title page), 9835-9836".

**D2-M8 (card `legacy.traces` 4: "put him on prayer into Slavonic" does not read as English).**
- Current text: "…and Paisius Velichkovsky put him on prayer into Slavonic."
- Source: PAISK l.9835-9836, a piece by Palamas "о молитвѣ", in a book of Paisius's translations (l.29-41).
- Fix: "…and Paisius Velichkovsky translated his piece on prayer into Slavonic."

**D2-M9 (README l.44: a claim made untrue by D-M2).**
- Current text: "…and Philotheos is named by his see's city on the card only where needed."
- Why: after D-M2 the brief also says "a patriarch of Constantinople".
- Fix: "…and Philotheos is named as patriarch of Constantinople at his first mention in the brief and in the card."

---

### gregory-of-sinai

`grade_text`: FK 8.64, Flesch 62.87. 403 words. Audio: the brief exactly, with the two tags in place and no other. Card fields in the pattern's order.

**R1 findings: applied?**

| R1 id | Verdict |
|---|---|
| D-B2 (Basil's line from the wrong preface) | OK. The line is at PAISZ l.4651-4653, inside "ПРЕДИСЛОВІЕ НА ГЛАВИЗНЫ БЛАЖЕННАГО" (l.4523-4526). The contents list puts that preface at page 85 and Hesychius at 97 (l.14206-14209). Basil is "спостника и друга блаженнаго Отца Паѵсія" (l.14198-14199) and "Старца Поляномерульской обители" (l.14215). |
| D-B3 (the held "no one" side) | OK. "отнюдь никогоже обрѣте въ ней, ни[ж]е малое вѣдѣніе о молитвѣ сей имущаго" (PAISZ l.11025-11029). It is told in place, a card item exists, and records hold the claim and a contested_claim. In the brief "the prayer" has nothing to refer to yet; see D2-M10. |
| D-B4 (false "one"; the notice "drawing on" the Life) | OK in substance. The notice says only that Kallistos "κατὰ πλάτος συνέγραψεν" the Life (PG150 l.69142-69144). The new item 1 has an antecedent fault and a 33-word sentence; see D2-M16. |
| D-M11 (Paisius's context) | Applied in the brief. "Archimandrite" is undefined (D2-M11), and on the card the context sits on a later mention (D2-M14). |
| D-M12 (Meyer sentence cut) | OK. Crete, Arsenios and the thirteenth century stay on the card with Meyer's name. |
| D-M13 (paroria) | OK in the brief, card `place` and `knownFor`. The card `role` was left with the old place name; see D2-M17. In `place` the new Rački clause is his first card mention; see D2-M14. |
| D-M14 ("In it") | OK. Rački: "Gregorij bijaše već na sv. Gori … u asceteriju Magali, i u drugih mjestih sakupio oko sebe više učenika, grčkoga i slovenskoga roda" (RACKI l.3668-3685). |
| D-M15 (two forms of the prayer) | "Some Fathers … Others" is OK (PG150 l.72589-72591). "Some say it" drops "teach"; see D2-M12. |
| D-M16 (the condition) | OK in the brief: "εἴπερ διήνοικται", Latin "si quidem apertum sit" (PG150 l.72579; l.72620). The card keyWorks still drops it; see D2-M13. |
| D-M17 (neglect of the commandments) | OK. "ἢ διὰ τῆς τῶν ἐντολῶν ἀμελείας τοῖς πάθεσι συγχωσθεῖσα, καὶ τὴν μετάνοιαν ἡμῶν ἀναμένουσα" (PG150 l.72492-72494). |
| D-M18 (knownFor) | "Taught" is OK ("ἐδίδασκεν", PG150 l.69134). "Tonsured" is an undefined term; see D2-M18. |
| D-M19 (Kallistos at first card mention) | OK. `dates` is the first mention and now reads "the patriarch Kallistos". |
| D-M20 (sitting piece separate) | OK. The fifteen chapters begin at PG150 l.71955-71971. "ΠΕΡῚ ΤΟΥ ΠΩΣ ΔΕῚ ΚΑΘΕΖΕΣΘΑΙ…" follows at l.72557, then "Περὶ τοῦ πῶς δεῖ λέγειν τὴν εὐχήν" (l.72588). No other heading falls between. |

**New findings**

**D2-M10 (brief para 2: "the prayer" has no antecedent yet).**
- Current text: "Citing the Life, he also says Gregory found no one on Athos who knew the prayer."
- Why: by this point the brief has named only guarding of the mind, stillness and contemplation (para 1). "Prayer of the mind" first appears in para 3 and the prayer's words in para 4. Paisius's "молитва сія" is the prayer worked "умомъ въ сердцѣ", by the mind in the heart (PAISZ l.11000-11001).
- Fix: "Citing the Life, he also says Gregory found no one on Athos who knew the prayer of the mind." (+3)

**D2-M11 (brief para 2, card `uncertain` 1: "archimandrite" is an undefined term).**
- Current text: "Paisius Velichkovsky, archimandrite of Neamț in Moldavia, says…"
- Source: Basil's preface calls Paisius "настоятеля Нямецкаго Вознесенскаго Монастыря", the superior of the Neamț Ascension Monastery (PAISZ l.3993-3994). The contents list has "Архимандрита Молдавскихъ Святыхъ монастырей Нямецкаго и Сѣкула" (l.14193-14196), which gives Moldavia.
- Fix, brief: "Paisius Velichkovsky, abbot of Neamț in Moldavia, says…" (0 words). Card: the same words, moved to his first card mention (D2-M14).

**D2-M12 (brief para 4, card `keyWorks` 2: "Some say it" drops "teach").**
- Current text: brief "Some say it with the mouth and some with the mind, he added, and he taught both." Card "Some teach it with the mouth and some with the mind, he writes, and he teaches both."
- Source: "οἱ μὲν διὰ στόματος, οἱ δὲ διὰ νοῦ διδάσκουσι λέγειν αὐτήν. Ἐγὼ δὲ ἀμφότερα τίθημι" (PG150 l.72599-72601). Some teach saying it through the mouth, and others through the mind. The brief turns the teachers into people who pray, and that weakens "he taught both". The card's "teach it with the mouth" can be heard as teaching aloud.
- Fix, brief: "Some teach it said with the mouth, some with the mind, he added, and he taught both." (0 words). Card: "Some teach it said with the mouth, some with the mind, he writes, and he teaches both."

**D2-M13 (card `keyWorks` 2: the condition D-M16 restored in the brief is still dropped here).**
- Current text: "(on a stool, bent low, gathering the mind into the heart)".
- Source: "τὸν νοῦν ἐν τῇ καρδίᾳ συνάγων, εἴπερ διήνοικται" (PG150 l.72578-72579).
- Fix: "(on a stool, bent low, gathering the mind into the heart if it has opened)".

**D2-M14 (card: four first mentions without role or place).**
- `dates` is Meyer's first card mention: "Philipp Meyer, in 1894, places…". His role is in his title: the main Athos documents "herausgegeben … von Ph. Meyer" (MEYER l.1, and the title page). Fix: see D2-M15, which gives "Philipp Meyer, who edited the main Athos documents in 1894".
- `place` is Rački's first card mention: "Rački names a mountain Paroria near Adrianople". Fix: "the Croatian historian Franjo Rački names a mountain Paroria near Adrianople." In `legacy.traces` 1 the next mention can then read "Rački, retelling Kallistos's Life…".
- `legacy.traces` 2 is the first card mention of both Basil and Paisius: "Basil of Poiana Marului wrote a preface for those who wish to read his book. It is printed among the writings of Paisius Velichkovsky's circle." Round 1 put Paisius's context on `uncertain` 1, which comes later in the card. Fix: "Basil, elder of the Poiana Marului monastery, wrote a preface for those who wish to read his book. It is printed among the writings of the circle of his friend Paisius Velichkovsky, abbot of Neamț in Moldavia." Sources: "Старца Поляномерульской обители Василія" (PAISZ l.14215); "спостника и друга блаженнаго Отца Паѵсія" (l.14198-14199); the preface's title "предпутіе хотящимъ чести книгу иже во Святыхъ Отца нашего Григорія Синаита" (l.14201-14202). Then `uncertain` 1 drops the title (D2-M16).

**D2-M15 (card `dates`; records contested_claim side 2: Meyer's tradition is not said to come from the Life).**
- Current text: card "…after a tradition he takes from the Life by the patriarch Kallistos." Records "Meyer: in the thirteenth century, by a tradition from Kallistos's Life".
- Source: "Damals aber wurde sie einer glaubhaften Ueberlieferung nach durch den Mönch Gregorios eingeführt … (Vgl. den Bios des Gregorios von seinem Zeitgenossen, dem Patr. Kallistos im Neon Eklogion S. 327 ff.)" (MEYER l.4002-4009). Meyer calls it a credible tradition and refers the reader to the Life with "Vgl.". He does not say he takes the tradition from it. The thirteenth-century dating also rests on "Sie scheint vor dem 13. Jahrh. auf dem Athos nicht bekannt gewesen zu sein" (l.4001-4002), a "seems".
- Fix, card: "Philipp Meyer, who edited the main Athos documents in 1894, places the bringing of the prayer of the mind to Athos in the thirteenth century. He calls this a credible tradition and refers to the Life by the patriarch Kallistos." Records side 2: "Meyer: in the thirteenth century, by what he calls a credible tradition, referring to Kallistos's Life (MEYER l.4001-4009)".

**D2-M16 (card `uncertain` 1: "which Migne reprinted" attaches to the Philokalia, and one sentence runs 33 words).**
- Current text: "Most of the story comes from a short notice by the editors of the Philokalia, which Migne reprinted in 1865. The notice names a longer Life by his disciple, the patriarch Kallistos. Meyer and Paisius Velichkovsky, archimandrite of Neamț in Moldavia, cite that Life, and Paisius says the Greek copy which reached his community was incomplete and lacked the account of Gregory's death."
- Why: Migne reprinted the notice in PG150 (l.69105-69218), not the Philokalia. The last sentence is 33 words.
- Fix: "Most of the story comes from a short notice by the editors of the Philokalia. Migne reprinted the notice in 1865. It names a longer Life by his disciple, the patriarch Kallistos. Meyer and Paisius Velichkovsky cite that Life. Paisius says the Greek copy which reached his community was incomplete and lacked the account of Gregory's death." (The title moves to the first mention, D2-M14.)

**D2-M17 (card `role`: "the lauras of Paroria" takes one side of a dispute the card now keeps open).**
- Current text: "Monk and teacher of the prayer of the mind; founder of the lauras of Paroria".
- Why: after D-M13, `knownFor` and `place` say "the paroria, the borderlands, of Macedonia", and `uncertain` asks "What Paroria was" (Lecomte's "in finibus Macedoniae", PG150 l.69175; PHIL2's capital, l.33628). The role still uses it as a place name. Checklist items 7 and 9.
- Fix: "Monk and teacher of the prayer of the mind; founder of three lauras in the paroria of Macedonia".

**D2-M18 (card `knownFor`: "tonsured" is an undefined term).**
- Current text: "A monk, tonsured on Mount Sinai, who taught…"
- Source: "ὁ κατὰ τὸ Σίναιον ὄρος μοναχὸς ἀποκαρεὶς, καὶ διὰ τοῦτο ἐπικληθεὶς Σιναΐτης" (PG150 l.69111-69115).
- Fix: "A monk of Mount Sinai who taught the prayer of the mind to the monks of Mount Athos…" (`place` already says the notice has him become a monk there.)

**D2-M19 (card `sources`, README l.25: "Basil of Poiana Marului's preface" is now two prefaces).**
- Current text: card "Life and Writings of Paisius Velichkovsky, with Basil of Poiana Marului's preface". README "Paisius Velichkovsky's volume with Basil of Poiana Marului's preface".
- Why: the card uses Basil's preface to Gregory's book (`legacy` 2; PAISZ l.3999ff) and, after D-B2, his preface to Philotheos of Sinai (`uncertain`; l.4523ff).
- Fix: "…with Basil of Poiana Marului's prefaces" in both.

**Whole brief as a story.** It still opens on a scene, Gregory going round Athos. Paisius's "no one" sits in place one paragraph after the notice's three monks, so a listener hears the clash. Paragraph 2 is now dense with witnesses: the notice, Kallistos, Paisius twice. It still reads in order, and D2-M10 removes the one point where a listener would lose the thread. The last line was rebuilt with its condition and still closes on Gregory's own teaching. My scratch copy with D2-M10 to D2-M12 is 406 words, FK 8.59, Flesch 63.48.

---

### records.json (these profiles)

- **gregory-palamas.** D-B1, D-M1, D-M8, D-M9 and D-M10 entries are present and match their sources, apart from D2-M1 (the "for him" note), D2-M3 (which tome), D2-M6 (the leftover sentence and the doubled witness) and D2-M7 (the header witness). The contested_claim "His age when he left for Athos" is right. absent_details: I accept the four entries. My search for 1296, 1359 and 1362 in every file naming Palamas found only the three Library headers giving "c. 1296-1359", page and column numbers, and other men's dates (Gregory Mammas in PG161 l.14617; Cabasilas in Charon l.674). The two Synaxaristes volumes hold Palamas incipits and indexes only.
- **gregory-of-sinai.** Basil's witness is corrected (D-B2). The Paisius "no one" claim and its contested_claim are present and match PAISZ l.11025-11031; Meyer's pupils are at MEYER l.4006-4007. The sitting-piece and neglect-clause claims match PG150. One fix is D2-M15 (contested side 2). absent_details: unchanged, and I accept them.
- **Census points** (from R1, for Open-Gaps): the Handover lists them for the batch's Open-Gaps entry (Handover_after_R1.md l.12-13). Nothing to add.

### Checklist summary

| # | Item | gregory-palamas | gregory-of-sinai |
|---|---|---|---|
| 1 | Each sentence sourced, source establishes it | Pass (D2-M1 is minor: a reading against the edition's Latin) | Pass (D2-M15 is minor) |
| 2 | Quotes verbatim | Pass (no quotations in marks) | Pass (no quotations in marks) |
| 3 | No invented family, feeling, thought, anecdote, speech | Pass | Pass |
| 4 | Reading aids, no AI tells | Fail, minor (D2-M2, D2-M4, D2-M8) | Fail, minor (D2-M10, D2-M11, D2-M16, D2-M18) |
| 5 | No role for a named witness | Pass | Pass |
| 6 | Partisan or hostile witness named and marked | Pass (Kantakouzenos "his ally"; Gregoras "his enemy"; Combefis marked, D2-M3 fixes the document) | Pass |
| 7 | Contested claim shows both sides | Pass | Fail, minor (D2-M17) |
| 8 | Common names with place at first mention, each text | Fail, minor (D2-M5) | Fail, minor (D2-M14) |
| 9 | One term for one thing | Pass | Fail, minor (D2-M17) |
| 10 | Story, scene opening, disputes in place, length | Pass | Pass |
| 11 | Readability (FK ≤10, Flesch ≥60) | Pass (7.69 / 63.81) | Pass (8.64 / 62.87) |
| 12 | Card order, missing fields absent, caveat in What is uncertain | Pass | Pass (D2-M16 is wording only) |
| 13 | Audio tags only in audio, at start and before last line | Pass | Pass |
| 14 | Keeps list line; a Who with body of work or following | Pass | Pass |

Card form (item 6 of the brief): field order is right on both. `briefLength` is "about 2 minutes 30 seconds" on both. That is the house form for this field across all Who cards (97 cards use it), not a word count. At 403 and 406 words it is right. `sources` cover every work each brief relies on. `ownWords` hold only the subject's own works; the PALH entry names the encomia it also carries. `keyWorks` hold three each.

### Grades

| Profile | Words (`wc -w`) | FK | Flesch | With my fixes |
|---|---|---|---|---|
| gregory-palamas | 406 | 7.69 | 63.81 | 407, FK 7.77, Flesch 63.26 (D2-M1, D2-M2) |
| gregory-of-sinai | 403 | 8.64 | 62.87 | 406, FK 8.59, Flesch 63.48 (D2-M10 to D2-M12) |

### Count

- **gregory-palamas:** 0 blocking, 9 minor (D2-M1 to D2-M9). All 11 round 1 points applied. D-M4's "for him" is wrongly applied (D2-M1), and D-M6's wording needs the document named (D2-M3).
- **gregory-of-sinai:** 0 blocking, 10 minor (D2-M10 to D2-M19). All 13 round 1 points applied. D-M15 was applied with "say" for "teach" (D2-M12). D-M16 was not carried to the card (D2-M13). D-M11 was placed on a later card mention (D2-M14).
- **Part D total:** 0 blocking, 19 minor.
