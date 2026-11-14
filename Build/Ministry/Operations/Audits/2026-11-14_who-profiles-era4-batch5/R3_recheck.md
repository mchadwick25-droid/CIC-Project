# R3 recheck: era 4 Who batch 5

This is round 3, the last of the three review rounds. A fresh Opus agent did it as a targeted recheck at full effort. The agent had not seen the drafting or the earlier rounds while they were under way. The recheck covers all eight profiles, `records.json` and the README.

## Method

Reviewer: independent Opus, first sight of these files. I edited no profile file. I made no git write and no web, paid or model call, and used local scripts and read-only git only. Inputs: `CLAUDE.md` in full, the review brief, `R1_review.md`, `R1_changes.md`, `R2_recheck.md`, `R2_changes.md`, era 4 batch 3's `R3_recheck.md` for form, and `git diff HEAD~1 HEAD` (8e8e1ef8) over `Who-Profiles/era4/batch5/`, as a word diff for briefs, cards and audio and a line diff for `records.json`. The working tree matches 8e8e1ef8 for this folder.

For every R2 finding and every string changed in 8e8e1ef8, I opened the cited lines again in the vendored file under `cic/texts/` and read them in context. While reading I folded OCR noise, double spaces, hyphen breaks and Migne's two columns. I then read each brief and card whole, as a participant would. Short names follow R2: THEOPH (PG 108), MANSI10, PG87.3, PG111, MEYER, MACLER04, MACLER17, AB7, ASS1, MITCHELL, WIGRAM1929, MARI, CHARLES, HP5 (Evetts's History of the Patriarchs inside the PO 5 file `chronicle-of-seert_..._scher-dib1910.txt`), HP1 (`severus-al-muqaffa_history-patriarchs-coptic-church-v1_evetts1904.txt`), MALECH, BUDGE (Book of Governors v2), HM (Harris-Mingana 1920).

---

## 1. R2 findings

| Finding | Status | Evidence |
|---|---|---|
| R2-B1 (Sophronius, Umar or the temple) | RESOLVED | Brief P9 and audio now read "Sophronius wept." The Greek "Toy vady iFhrnaev" (τὸν ναὸν ἐζήτησε, THEOPH l.61787) and "Toiroy d wy Lwpdvs" (Τοῦτον δὲ ἰδὼν Σωφρόνιος, l.61789) leave the object open. The Latin "Hune cum Sophronius vidisset" (l.61824) takes Umar. "multaque simul lacrymarum copia ... deflebat" (l.61826-61828) and "Caxpuo" (δάκρυσι, l.61792) back "wept". "he said" can only be Sophronius. The records note is corrected and its witness widened to l.61787-61792. The added card sentence brings a pronoun fault (R3-M1). |
| R2-B2 (Moses, Burkitt not Mitchell) | RESOLVED | "INTRODUCTORY ESSAY / BY F. C. BURKITT" (MITCHELL l.2585-2586), signed "F. C. BURKITT." (l.2777). Burkitt's preface says he wrote "a wholly new chapter" (l.1310). "Moses bar Kepha died 903 A.D." is at l.2656. The card's `uncertain` 1 ("F. C. Burkitt, introducing the second volume of C. W. Mitchell's edition of Ephrem, gives 903."), `sources.ownWords` 3 (title, author "Moses bar Kepha; F. C. Burkitt (English)", date 1921 from the file header l.10-11), the records claim and the 903 side all now name Burkitt. Footnote 9 sends the reader to Nau's text (l.3001), so "(English)" for Burkitt is fair. |
| R2-M1 (held him back) | RESOLVED | "but the Saracen invasion hindered him." This renders "incursionem Sarracenorum præpedior" (MANSI10 l.91459-91460). |
| R2-M2 (he says) | RESOLVED | "Sergius says Sophronius could not bring texts of the Fathers that spoke of two in those very words. In the end, he writes, it was agreed that Sophronius would speak no more of one or two." Witnesses: "duas nominatim et ipsis verbis operationes ... Ille autem hoc facere penitus non valuit" (PG87.3 l.25686-25688); "Et ad ultimum stetit ac placuit, quatenus prædictus Sophronius ... nullum sermonem de cætero, de una sive duabus operationibus movere debeat" (l.25704-25707). "he writes" follows a sentence whose subject is Sergius, and the same clause names Sophronius, so it cannot be heard as him. |
| R2-M3 (Papebroch's style point) | RESOLVED | "though its style is very different from that of the Miracles." This renders "multum alioqui diversus est stylus ab eo, quo SS. Cyri et Joannis laudationem atque miracula descripta" (PG87.3 l.25420-25424). The card's `uncertain` 5 has already named "the Miracles". Papebroch's "quam utramque" also covers the Life of Anastasius the Persian. The card leaves that out, which takes nothing away from what it says of Mary of Egypt. |
| R2-M4 (Kyminas from the Life) | RESOLVED | "His own rule calls Michael, uncle of Nikephoros, his abbot. Mount Kyminas and the family name Maleinos come from Meyer, who draws on the Life of Athanasios and on Michael's own Life." The rule has "τῇ τοῦ µακαρίου θείου αὐτοῦ λαύρᾳ Μιχαὴλ ... τοῦ ἐμοῦ καθηγουµένου" (MEYER l.5381-5382), with no mountain. In Meyer, Kyminas is at "He- gumen vom Berge Kyminas" (l.1259-1260) and the note "Alles nach dem Bios" (l.1277). Maleinos is at "Ueber den Maleinos giebt sein Bios Aufschluss" (l.1279-1281). |
| R2-M5 (testament line) | RESOLVED | "Μετὰ λύπης ὑπερβαλλούσης διήνυσα πᾶσας τὰς ημέρας" is at MEYER l.6592, and "εἰς τὸ προϊΐστασθαι ἑτέρων" at l.6594. The witness now reads l.6592-6594. |
| R2-M6 (his name, Macler) | RESOLVED, by the cut R2 offered | The 11-word sentence is gone from P3. The card's `legacy.traces` 1 keeps it ("son livre est lui-même une source à laquelle ses successeurs viendront recueillir leurs renseignements", MACLER04 l.264-265). "under his name" now follows "as written by Bishop Sebeos". |
| R2-M7 (the invasion's referent) | RESOLVED | "After the Greeks crossed the Jordan to fight the Arabs" fits "bataille contre ceux-ci (les Arabes) ... Arrivés au Jourdain, [les Grecs] le franchirent et pénétrèrent en Arabie" (MACLER04 l.6468-6473). "the Arab invasion" renders the note's "l'invasion des Arabes" (l.6514-6515). |
| R2-M8 (names his witnesses) | RESOLVED | "Sebeos says who his witnesses were." This rests on "Nous avons appris ces faits de prisonniers [venus] d'Arabie, qui en ont été témoins oculaires" (MACLER04 l.6752-6753). |
| R2-M9 (a second copy) | RESOLVED | "another copy, manuscript 52 of the Mekhitarist library at Vienna, with extracts of Moses of Khoren and Stephen of Taron" fits "Le n° 52 des manuscrits de la bibliothèque des PP. Mkhitharistes de Vienne ... renferme l'histoire de Sebéos et des extraits de Moïse de Khorèn et d'Étienne de Tarôn" (MACLER17 l.361-363). |
| R2-M10 (Antony `knownFor`) | RESOLVED | "The Bollandist heading also gives him the Miracles of the Mother of God at Choziba." The heading has "ANTONIO HOZEBITA AUCTORE" and "eodem auctore Antonio" (AB7 l.38275-38281). |
| R2-M11 (flat absence) | RESOLVED | The card reads "Everything the held sources say of him comes from the Life and from the Miracles printed under his name. No other held source names him." The README reads "known in the held sources only from his own writings". I searched all of `cic/texts/` again for Choziba, Chozeba and Χοζεβ. That turns up five files besides AB7: the Welsh Bible, Nicephorus Callistus PG 147, Cyril of Scythopolis, the Horologion and Nikodemos. None names an Antony within three lines of a hit. |
| R2-M12 (same volume) | RESOLVED | "The Bollandists' volume also prints, under his name, miracles ..." P2 has just named the Bollandists' edition of 1888. The Life and the Miracles are both in Analecta Bollandiana 7 (AB7 header; l.38275). |
| R2-M13 (He lived) | RESOLVED | "Moses lived about ninety years, it says." |
| R2-M14 (his tract) | RESOLVED | "a line from Moses's tract on baptism". |
| R2-M15 (Mr. Aytoun) | RESOLVED | The author line now reads "Moses bar Kepha, in English as Mr. Aytoun gives it; J. Rendel Harris and Alphonse Mingana (ed.)". That fits HM l.1174-1179 and the brief. |
| R2-M16 (Beth-Ceno lines) | RESOLVED | "BETH-CENO" is at PG111 l.36957, and "Raman, Beth-Ceno, & Mosal" at ASS1 l.109580 (l.109579-109580 with the line before). |
| R2-M17 (Wigram's side) | RESOLVED | Wigram 1929 is now a third side, "About 630: W. A. Wigram, 1929 (WIGRAM1929 l.4184-4190)". The source has "the Si-an monument tells us how the Emperor Tsai ... gave greeting to 'Olopen ...' about the year 630" (l.4186-4190). |
| R2-M18 (his brother) | RESOLVED | "the patriarch's brother Thomas" renders "quo tempore ei adstitit ipsius frater Thomas Bagarmae metropolita" (MARI l.12747). |
| R2-M19 (John, hedge order) | RESOLVED | "A John, bishop of Nikiu, appears in the History of the Patriarchs of Alexandria ... R. H. Charles takes him for the chronicler. This John was among the bishops at the deathbed of the patriarch John III ..." "Abba John, bishop of Niciu" is among those at the deathbed (HP5 l.1230-1233) and at the election (l.1313-1318). Charles makes the chronicler the bishop "who took part in the election of the successor of John of Samnûd in 690" (CHARLES l.177-182). The identity is now owned by Charles before it is used. "This John" and the next sentence's "him" can only be the bishop. |
| R2-M20 (HP1 in sources) | RESOLVED | The entry was added to `sources.about`. The file header gives "Tome I, Fasc. 4 ('Peter I to Benjamin I', 1907)", and its content note puts the Benjamin chapters in that fascicule. "Amr gave orders that Benjamin should be brought before him with honour" is at HP1 l.44676-44679. |
| A-B1 and B-M8, R1 partlies | RESOLVED | They were carried into R2-B1 and R2-B2 and are closed with them. |

---

## 2. New findings

### Blocking

None.

### Minor

- **R3-M1 MINOR (Sophronius card `uncertain` 1; items 4 and 7, pronoun capture; participant text; made by the R2-B1 recommended sentence).** The item reads: "Theophanes's account of Umar at Jerusalem, with Sophronius's words on the abomination of desolation, was written in the early ninth century. His Greek can be read as saying it of the temple or of Umar; the Latin printed with it takes Umar." The nearest man before "His" is Sophronius, in "Sophronius's words", and the words being discussed are his. So "His Greek" can be heard as Sophronius's own Greek. What is meant is Theophanes's text: "Τοῦτον δὲ ἰδὼν Σωφρόνιος" (THEOPH l.61789, OCR "Toiroy d wy Lwpdvs"), set against the Latin "Hune cum Sophronius vidisset" (l.61824).
  - Fix: "His Greek can be read as saying it of the temple or of Umar; the Latin printed with it takes Umar." -> "Theophanes's Greek can be read as saying it of the temple or of Umar; the Latin printed with it takes Umar." (20 words.)

Considered, and not a finding:
- Sebeos brief P3: "Stephen of Taron ... lists the History of Heraclius as written by Bishop Sebeos. The printed editions place three books under his name." Stephen is the grammatical subject, but the name that has just been given to the book is Bishop Sebeos. The next sentence but one names Stephen as a source the second book copies, so no listener can take the books as Stephen's. R2 accepted this order when it offered the cut.
- Sophronius brief P3 opens two sentences in a row on Sergius ("Sergius ... wrote", "Sergius says"). Each carries a different claim from a different place in his letter (PG87.3 l.25686-25688, 25704-25707). This is a wording preference.
- Sebeos card `uncertain` 1, "another copy": the copy is of the history that the item opens on, and `keyWorks` names the Etchmiadzin manuscript. True as it stands.
- Thomas brief P5, "Jérôme Labourt ... says he wrote between 832 and 850": the "he" cannot be Labourt, writing in 1904, or Budge. Unchanged since R1.
- The phrase "not among the sources used here" appears on these cards and on the approved batch 2 and 3 cards. It is a card convention for an honest limit, not narration in a brief.
- John card `sources.about`: the new HP1 entry says "English translation", and the PO 5 entry says "Arabic with English translation". Both are true of what the entries name.
- Records, the contested claim "Sophronius's words to Umar": the side "he called it the abomination of desolation" does not name what "it" is, so it does not settle the R2-B1 reading.

---

## Changed strings checked

Every string changed in 8e8e1ef8, against its lines:

| File, field | Result |
|---|---|
| sophronius brief P1, and audio ("hindered him") | PASS (MANSI10 l.91459-91460) |
| sophronius brief P3, and audio | PASS (PG87.3 l.25686-25688, 25704-25707) |
| sophronius brief P5, and audio ("Sophronius wept.") | PASS (THEOPH l.61787-61792, 61824-61828) |
| sophronius card `uncertain` 1, added sentence | PASS for the source; pronoun fault (R3-M1) |
| sophronius card `uncertain` 7 | PASS (PG87.3 l.25420-25424) |
| sophronius records, Theophanes claim and witness | PASS (THEOPH l.61787, 61789, 61824) |
| athanasios card `uncertain` 6 | PASS (MEYER l.1259-1260, 1277, 1279-1281, 5381-5382) |
| athanasios records, testament witness | PASS (MEYER l.6592-6594) |
| sebeos brief P3, cut sentence | PASS (kept on card, MACLER04 l.264-265) |
| sebeos brief P4, and audio | PASS (MACLER04 l.6468-6473, 6514-6515) |
| sebeos brief P5, and audio | PASS (MACLER04 l.6752-6753) |
| sebeos card `uncertain` 1 | PASS (MACLER17 l.361-363) |
| antony brief P6, and audio | PASS (AB7 l.38275-38281) |
| antony card `knownFor`, `uncertain` 1 | PASS (AB7 l.38275-38281; the Choziba search) |
| moses brief P3 and P7, and audio | PASS |
| moses card `uncertain` 1, `sources.ownWords` 2 and 3 | PASS (MITCHELL l.10-11, 1310, 2585-2586, 2656, 2777; HM l.1174-1179) |
| moses records, Burkitt claim, 903 side, Beth-Ceno lines | PASS (MITCHELL l.2585-2586, 2656; PG111 l.36957; ASS1 l.109579-109580) |
| alopen records, third side | PASS (WIGRAM1929 l.4186-4190) |
| thomas brief P5, and audio | PASS (MARI l.12747) |
| john brief P3, and audio | PASS (HP5 l.1230-1233, 1313-1318; CHARLES l.177-182) |
| john card `sources.about` 5 | PASS (HP1 header; l.44676-44679) |
| README, word span and "in the held sources" | PASS |

In the changed strings, every witness is attached and every hedge is kept: "takes him for", "can be read as" and "Sebeos never says so outright". The pronouns resolve except the one in R3-M1. No changed string adds a quotation. There is no new AI tell, contrast frame, beat line or colon reveal. The longest changed brief sentence runs 22 words: "This John was among the bishops at the deathbed of the patriarch John III, and met with them to choose the next."

---

## Mechanical checks

By script, on the files as they stand.

| Profile | Words | Time @162 | FK | Flesch | Audio = brief + tags | Card order, no empty or null field | Longest brief sentence |
|---|---|---|---|---|---|---|---|
| sophronius-of-jerusalem | 354 | 2:11 | 7.88 | 66.99 | yes (1 calmly, 1 warmly) | yes | 24 |
| athanasios-the-athonite (major) | 405 | 2:30 | 7.05 | 68.98 | yes | yes | 24 |
| sebeos | 354 | 2:11 | 6.73 | 73.09 | yes | yes | 26 (P1, unchanged since R1) |
| antony-of-choziba | 348 | 2:09 | 6.25 | 74.99 | yes | yes | 21 |
| moses-bar-kepha | 356 | 2:12 | 6.62 | 71.66 | yes | yes | 25 |
| alopen (major) | 362 | 2:14 | 7.23 | 63.82 | yes | yes | 26 (the closing verse, quoted) |
| thomas-of-marga | 356 | 2:12 | 6.12 | 75.44 | yes | yes | 25 |
| john-of-nikiu | 352 | 2:10 | 5.98 | 75.06 | yes | yes | 26 (P1, with a quote; unchanged) |

- All eight pass `grade_text` (FK 10 or below, Flesch 60 or above). The figures match `R2_changes.md`. Alopen's Flesch margin is still the thinnest, at 63.82. R3-M1 is on a card and does not touch any brief score.
- Each audio file equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, one of each.
- Every card parses as JSON. Its keys run in Mark's order, from `name` to `sources`, and no field is null or empty. `records.json` parses.
- README: "Athanasios's brief runs 405 words, about 2:30. Alopen's runs 362 words, about 2:14 ... The other six run 348 to 356 words, about 2:09 to 2:12." All of this matches the table: Antony 348 and Moses and Thomas 356, at 2:09 and 2:12.
- Quotations: the briefs hold 21 quoted strings, counting each pair of quotation marks once: Alopen 8, John 7, Moses 1, Thomas 5. R2 counted Alopen's verse lines one by one. A script checked each string against its file with case, punctuation, line breaks and footnote digits folded. Nineteen matched at once. The other two break across a line at a hyphen, and I checked them by eye: "holy men have no in- / variable station" (MALECH l.13699-13700) and "not vain imagin- / ations of my own" (BUDGE l.1067-1068). Both are verbatim. Sophronius, Athanasios, Sebeos and Antony quote nothing in the brief. Every other quotation mark in the briefs is on held English.

---

## Each brief read whole

I read each brief once more as a listener, start to end, and each card against checklist items 1-14.

- **Sophronius.** It opens on Calvary and stands apart from Maximus. The oath, the "hindered him", the Sergius account and the Christmas sermon read cleanly. The Umar scene now leaves open what Sophronius looked at. The "he said" in P1 and P5 can only be Sophronius. On the card: R3-M1.
- **Athanasios.** It reads well at the cap. Every claim about his early life is owned by "that Life" and Meyer. "He asked only" and "He was murdered" are the emperor. The testament line fits MEYER l.6592-6594. No new fault.
- **Sebeos.** The Cross scene opens it. The Jordan paragraph now has its enemy, and the witnesses paragraph no longer claims names. Macler's hedge is kept ("Sebeos never says so outright, Macler adds"). No new fault.
- **Antony.** It reads as his own story from start to end, and the closing paragraph now names its volume. No new fault.
- **Moses.** The paradise opening, the Basil correction and the two pronoun fixes hold. "His editors" in P4 follows "his chronicle" and is Bar Hebraeus's editors, as the brief named them in P3. No new fault.
- **Alopen.** It is unchanged since R2, and every quotation is verbatim. The stone's finding and the authenticity debate are owned by Yule and Williams. No fault.
- **Thomas.** The new "the patriarch's brother" settles the one loose pronoun. No new fault.
- **John.** P3 now names the identity as Charles's before it uses it. The deposition story and the quotations hold. No new fault.

No brief has hedging filler, a colon-reveal outside a quotation, a rhetorical question, an aphorism, a beat line or process narration.

---

## 3. Verdicts

| Profile | R2 findings | New blocking | New minor | Verdict |
|---|---|---|---|---|
| Sophronius of Jerusalem | R2-B1, R2-M1 to R2-M3 resolved | 0 | 1 (R3-M1, card) | CLEAR |
| Athanasios the Athonite | R2-M4, R2-M5 resolved | 0 | 0 | CLEAR |
| Sebeos | R2-M6 (by the cut) to R2-M9 resolved | 0 | 0 | CLEAR |
| Antony of Choziba | R2-M10 to R2-M12 resolved | 0 | 0 | CLEAR |
| Moses bar Kepha | R2-B2, R2-M13 to R2-M16 resolved | 0 | 0 | CLEAR |
| Alopen | R2-M17 resolved | 0 | 0 | CLEAR |
| Thomas of Marga | R2-M18 resolved | 0 | 0 | CLEAR |
| John of Nikiu | R2-M19, R2-M20 resolved | 0 | 0 | CLEAR |
| README.md | R2-M11's README part resolved; numbers match | 0 | 0 | CLEAR |

**Totals.**
- Earlier findings resolved: 22 of 22 R2 findings (R2-B1, R2-B2, R2-M1 to R2-M20). R2-M6 was resolved by the cut R2 offered. The two R1 partlies, A-B1 and B-M8, closed with R2-B1 and R2-B2. None is open.
- New blocking: 0.
- New minor: 1 (R3-M1, participant text, the Sophronius card).
- Every quotation in the eight briefs matches its vendored file. Every brief passes `grade_text`. Every audio file equals its brief plus the tags.
- All eight profiles are CLEAR.

**Cap note.** This is round 3, the last of the three review rounds the cap allows on each profile. No blocking finding is open, so nothing has to escalate. R3-M1 is participant text, on the Sophronius card. Changing it after this round needs a cap ruling from Mark, so it goes to him as an optional one-word fix ("His Greek" -> "Theophanes's Greek"), in final wording checked against THEOPH l.61789 and l.61824. Nothing in this batch closes until Phase Five boundary testing and full-system review are complete.
