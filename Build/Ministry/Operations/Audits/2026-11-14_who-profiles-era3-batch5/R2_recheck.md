# R2 recheck: era 3 batch 5

Three fresh Opus reviewers, none of whom drafted or fixed the files, rechecked the batch at full effort, part by part: each R1 finding, every changed sentence, and each brief read whole. Totals: all 11 R1 blocking points resolved; of the 46 R1 minors, 44 resolved and 2 partly (A-M8 and A-M10, carried by R2-A-B1); 2 new blocking and 15 new minor points (part A 1 and 4, part B 1 and 5, part C 0 and 6). A-M18, the README's Open-Gaps sentence, is met by Open-Gaps 248.

## Part A

Scope: Columba, Augustine of Canterbury, Evagrius Scholasticus and Henana of Adiabene, with their cards, audio scripts and `records.json` entries, and the batch README. I am a fresh reviewer; I did not draft or fix these files. I read the changes as a word diff from `9fcb5dee` (the drafts R1 reviewed) to HEAD (`0b995947`), limited to `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch5/`. I then read each brief whole for writing quality, as the brief asks. I opened every new or changed sentence, quotation and records entry at its line in the vendored file, and checked who is speaking there: the ancient writer, a document he copies, the translator, or an editor's note or title page. Quotations were searched with whitespace and punctuation collapsed; OCR passages were read by line. Coordinator rulings applied: Columba and Augustine are major; Evagrius's card tradition is "The Byzantine Imperial Church (Justinianic)"; Henana's brief says the teaching he was condemned for is known only through his opponents, and that a pupil's praise of the man survives. A-M18 (README) is to be met by an Open-Gaps entry written before merge, and is marked deferred. I edited no profile file, and made no git, model or web calls. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines, so paragraphs sit on l.1, 3, 5 and so on.

Mechanical checks, all four:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in a brief or card.
- `grade_text` passes for all four (FK at most 10, Flesch at least 60). Henana (60.5) sits nearest the floor.
- No narrator sentence runs past 25 words. The longest are Henana l.9, "In his Life of the martyr George of Izla, a monk says Henana taught that fate rules everything and denied the resurrection of the body." (25), and Columba l.7 (24). Augustine l.7 (31) and l.3 (24) are carried by Gregory's quoted words.
- `briefLength` matches on all four. All four cards and `records.json` parse; `records.json` holds the ten batch ids. Every `file` named in the four cards' sources exists, including the new Annales Cambriae entry on Columba.

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Columba (MAJOR) | 403 | 2:29 | 5.7 | 77.1 | within 405 |
| Augustine of Canterbury (MAJOR) | 405 | 2:30 | 7.2 | 70.5 | 405, at the cap |
| Evagrius Scholasticus | 325 | 2:00 | 7.4 | 67.0 | 325, at the cap |
| Henana of Adiabene | 325 | 2:00 | 8.0 | 60.5 | 325, at the cap |

### 1. The 6 R1 blocking findings

| Finding | Status | Evidence |
|---|---|---|
| A-B1 (Columba: Huyshe made a doubter of the battle as cause) | RESOLVED | Brief l.5: "Huyshe, with later Irish tradition, makes the battle the cause of his leaving. Adomnán names it only to date the voyage." Huyshe's note: "The battle was fought in 561… It was the cause of Columba's exile" (l.3022–3026); "The tradition is a constant one that the strife and bloodshed of Cuil Dremhne had something to do with Columba's leaving Ireland" (l.1571–1574). Adomnán names the battle twice, both times as a date: the preface, "In the second year after the battle of Culedrebina" (l.2219–2224), and I.7, "Two years having passed after the battle of Cule-Drebene… at the time when the blessed man first sailed away" (l.3000–3003). So "only to date the voyage" holds. Card `uncertain` 4: the Teltown synod "not rightly, as afterwards in the end became clear" (l.9318–9321), "Teilte [Teltown, Meath]" (l.9356–9357); Reeves "possibly in 561, after the battle" (l.9362–9368). Records claims 11 to 13 and contested claim 3 match. The fix now leaves out the reserve Huyshe shows in his introduction (R2-A-M1). |
| A-B2 (Columba: false absence of annals) | RESOLVED | Annales Cambriae: "521. Lxxvii. Sanctus Columcille nascitur" (l.2399), "562. cxviii. Annus. Columcille in Brittania exiit" (l.2417), "CLI. Annus. Columcille moritur" (l.2516). The margin "595." stands at l.2480, displaced by the OCR column; the count agrees (118 = 562, so 151 = 595). The header gives "Anonymous Welsh annalists (10th c. compilation of earlier entries)" (l.2–3). Card `uncertain` 2, 3 and 5, `sources.about` 5, records claims 9, 28 and 29, contested claims 1 and 2, and `absent_details` 2 and 3 all match. |
| A-B3 (Augustine: two meetings told as one) | RESOLVED | Brief l.9 as R1 worded it. Bede II.2: the first conference "at a place which is to this day called Augus-/tine's Ac, that is, Augustine's Oak" (l.3567–3568), then the Britons "desired that a second synod might be appointed"; before it, the hermit: "If he is a man of God, follow him… if at your approach he shall rise up to you, hear him submissively" (l.3631–3660); "when they came, Augustine was sitting on a chair" (l.3670); "is said, in a threatening manner, to have foretold… if they would not preach the way of life to the English nation, they should at their hands undergo the vengeance of death" (l.3676–3682); "that perfidious nation" (l.3685). The card's `uncertain` 1 and records claims 21 to 23 now split the two meetings, and claim 22 notes that Bede gives no place for the second. |
| A-B4 (Evagrius: the loss dated to the wrong year) | RESOLVED | Brief l.7: "Nearly two years before writing this, he lost a daughter and her son." Walford: "not quite two years before my writing this, being now in the fifty-eighth year of my age… I lost a daughter and her son" (l.9043–9046). Records claim 9 quotes the full clause. |
| A-B5 (Henana: false absence of his own works) | RESOLVED | Brief l.3 as the coordinator ruled: "The teaching he was condemned for is known only through his opponents, though a pupil's praise of the man survives." Card `keyWorks` 1: "Addai Scher says only his treatises on the Rogations and on Golden Friday survive; they are not among the sources used here." Scher: "Il ne nous est parvenu de ces ouvrages que les traités sur les Rogalions et le vendredi d'or" (barhadbeshabba scher1908 l.21084–21085). Card `knownFor` and `uncertain` 1 are narrowed the same way. Records claim 25 and `absent_details` 1 match. The README's Henana sentence was not narrowed (R2-A-M4). |
| A-B6 (Henana: Sabrisho's side told as settled) | RESOLVED | Brief l.7 now opens "In the chronicle's telling," and ends "But Timothy I, a later head of the church, says Sabrisho condemned Henana's writings." Chronicle: "le catholicos, bien loin de confirmer leur sentence, accueillit favorablement la lettre de Hnana" (seert l.28659–28660). Mai: "damnabatque, quemadmodum Sabariesus catholicus Hanani Adiabeni scripta" (l.18862–18865). The speaker is Timothy: the chapter opens "Timotheus… haec clare exponit in sua synodica epistola quam in synodo ab ipso collecta anno Arabum 174… Timotheus, inquam, dicit" (l.18711–18717), and the passage goes on "Nosque similiter blasphemias… Iosephi, atque Iohannis Daliathensis proscripsimus" (l.18870–18872). Labourt: "Sabriso' se prononça cependant contre eux dans le synode général… (mai 596)" (l.12231–12234), where "eux" is the Henanians (l.12221–12229). Chabot: "ouvrages furent condamnés à différentes re[prises]" (l.26755–26757). Card `uncertain` 4, records claims 16 and 17, and contested claim 3 match. Moving Mari's sentence to the card left an unclear pronoun at l.11 (R2-A-M3). |

### 2. R1 minor findings

**All four**
- A-M6: RESOLVED. No card in part A uses the Library's word "held" for its holdings. Evagrius's "held to the Council of Chalcedon" means loyalty. Augustine `keyWorks` 1 now reads "kept as Bede copied them".

**Columba**
- A-M1: RESOLVED. "the birthday the Book of Lismore Life gives, a Thursday, 7 December, points to 517 or 523, but Bishop William Reeves thinks 521 most likely." Stokes's note is keyed to the Lismore Life's own lines 799–802 and says "points to the years 517 and 523… But Bishop Reeves thinks a.d. 521 'most likely to be the true period'" (l.24008–24011). The drafter's narrowing from "the Irish Lives" is correct.
- A-M2: RESOLVED. "Bede, who followed the Roman Easter, says Columba's heirs kept uncertain rules for it." Bede: "they followed uncertain rules in their observance of the great festival, as having none to bring them the synodal decrees for the observance of Easter" (l.5869–5872).
- A-M3: RESOLVED. "In the night he gave his last words for the monks. Only Diormit heard them:". Huyshe: "he gives his last commands to the Brethren, his attendant alone hearing them" (l.10812–10814). The quotation is exact (l.10814–10817).
- A-M4: RESOLVED. l.1 is now "…his Sabbath, his rest. That night he would go the way of his fathers." Adomnán has "a certain little secret chat" and "this night, at midnight… I shall go the way of my fathers" (l.10703–10722). l.9 is now three sentences: "Bede adds that he had founded the Field of Oaks in Ireland. Many houses in Britain and Ireland grew from it and from Iona. The island was ruled by its abbot…" Bede: "he had built a noble monastery in Ireland… The Field of Oaks. From both which monasteries, many others had their beginning through his disciples, both in Britain and Ireland" (l.5847–5853). "The island" follows "Iona" directly and reads clearly. The paragraph flows.
- A-M5: RESOLVED. "Wilfrid, the priest who spoke for the Roman side".

**Augustine of Canterbury**
- A-M7: RESOLVED. "Augustine of Canterbury and his companions came singing a litany. They bore a silver cross…" Bede l.1946–1950.
- A-M8: PARTLY. A role no longer stands for the witness, but the witness now named is wrong. The volume was edited by Ludwig Hartmann after Paul Ewald's death, and the judgment is Hartmann's alone (R2-A-B1).
- A-M9: RESOLVED on the card (`uncertain` 2: "Gregory's letter to Eulogius has him made bishop before he was brought to the English; Bede has him go to Arles after the king's baptism"). Turchi: "a Germaniarum episcopis episcopus factus cum eorum quoque solaciis ad praedictam gentem… perductus est" (l.9325–9326). Contested claim 3 was added. The brief's new "then" sits after the wrong sentence (R2-A-M2).
- A-M10: RESOLVED in form, as worded. Its "Paul Ewald and Ludwig Hartmann have Laurentius succeed him in 606" carries the same misattribution (R2-A-B1).
- A-M11: RESOLVED. Records claims 18 and 19. Bede: "ordain twelve bishops, who shall be subject to your jurisdiction", "shall also ordain twelve bishops", "it is necessary that you rejoice with fear, and tremble whilst you rejoice". All three are exact.

**Evagrius Scholasticus**
- A-M12: RESOLVED. "Writings, most of them in Gregory's name, won him the ranks of quaestor and prefect." Walford: "The memorials were principally composed in the name of Gregory… and by means of them I obtained two dignities… questorian rank… prefecture, in consideration of what I composed at the time when he… [became] the father of Theodosius" (l.12222–12229). "He served Gregory, patriarch of Antioch." reads cleanly.
- A-M13: RESOLVED. "so his account of Gregory is that of his adviser." Walford "accompanied by myself as his adviser" (l.11417–11418).
- A-M14: RESOLVED. `dates`: "when the Persian king Chosroes took Antioch, in 540 by Walford's page heading". The heading is "PERSIAN INVASION.—A.D. 540" (l.8710). `legacy.traces` 1: "Socrates of Constantinople and Theodoret of Cyrrhus". Freese names "Theodoret, bishop of Cyrrhus" (l.2998) and "Theodoret of Cyrrhus" (l.3581). Records claims 7 and 8 match.

**Henana of Adiabene**
- A-M15: RESOLVED. The beat line is gone, and the paragraph now opens "The chronicle, which writes against him, says…". The card's "Two later witnesses agree" is a fair narrowing.
- A-M16: RESOLVED. "…and of sharing with the Severians the teaching of one nature and one hypostasis in Christ rest on Babai the Great alone". Chabot: "doctrines impies qu'il partage avec les Sévériens, en professant qu'il y a dans le Christ une nature et une hypostase" (l.42142–42143). Records claim 9 and contested claim 1 carry it.
- A-M17: RESOLVED. "the martyr George of Izla" in brief, card and source title. Chabot: he took the name George at baptism and made his profession in the convent of Dadisho after visiting the Izla solitaries (l.42084–42088). Labourt: "Georges le martyr" among the Izla disciples (l.12225–12227). The place is a fair identifier and adds no claim. Records claim 11 holds it.

**README**
- A-M18: DEFERRED, as the coordinator ruled. README l.9 still says "The correction is logged in Open-Gaps." The batch 5 Open-Gaps entry must log the Evagrius tradition correction before merge, or the sentence must change to match. The README's Henana sentence also lags the ruling (R2-A-M4).

### 3. The drafter's own departures from R1 wording

- **Columba A-M4, l.9.** The drafter's reason holds. R1's "these two" pointed to one house, and the new "from it and from Iona" follows Bede's "From both which monasteries" (l.5852).
- **Augustine A-M9, the brief.** "In Bede's telling, Aetherius of Arles ordained him" avoids two sentences in a row opening with "Bede". The words are faithful. See R2-A-M2 on where "then" now sits.
- **Evagrius A-M12, "Over the years it took" kept.** The reason holds: "by its recurrence at different times" (l.9035–9036).
- **Henana A-B6, the Chronicle's side on the card.** The card says Sabrisho "welcomed Henana's letter and would not confirm the Fathers' sentence against him". That keeps to the chronicle (l.28659–28660), and the narrowing of R1's "letter against Gregory" is correct.

### 4. New findings

- **R2-A-B1 BLOCKING (`augustine-of-canterbury.brief.txt` l.7; card `uncertain` 3 and 4, `sources.ownWords` 2 and `sources.about` 3; `records.json` claims 15, 17 and 27 and contested claim 2; items 1 and 5; a witness swap carried by R1's own A-M8 and A-M10 wording).**
  - The brief says: "Paul Ewald and Ludwig Hartmann, editing Gregory's letters, say these answers have often been doubted, and judge them genuine."
  - Ewald did not make this judgment. The title page of the held volume reads "POST PAVLI EWALDI OBITVM EDIDIT LVDOVICVS M. HARTMANN" (`gregory-great_registrum-epistolarum-t2-pars2-libri-10-14-lat_ewald-hartmann1895.txt` l.103–106). The same words stand on the part I title page (`…t2-pars1-libri-8-9-lat_ewald-hartmann1893.txt` l.136–139).
  - Hartmann's preface says he drew on Ewald's notes, changing some and adding others: "nonnulla ex notis manuscriptis Ewaldi mutavi; alia ipse addidi" (l.175–176).
  - The note on XI.56a is in one editor's first person: "non dubito, quin genuina sit" (l.12704). The same note names Ewald in the third person: "Ewald coniecit etiam" (l.12696–12697).
  - The Laurentius note (l.10690–10691) and the preface that dates Boniface's letter (l.196–197) belong to the same volume and the same editor.
  - So the brief and card put the judgment in the mouth of a scholar who had died before the volume appeared.
  - The archive.org catalogue's "ediderunt Paulus Ewald et Ludovicus M. Hartmann" (file header l.1) credits the whole edition to both and does not change who wrote this note.
  - There is a second, smaller point. The note dates Boniface's letter "ante a. 741" (l.12690), while the preface gives "a. 735" (l.196). The card cites only the 735.

  Fixes:
  - Brief l.7, last sentence: "Ludwig Hartmann, editing Gregory's letters, says these answers have often been doubted, and judges them genuine." This saves two words. Augustine then runs 403 words; with R2-A-M2 the score is FK 7.2 and Flesch 70.3.
  - Card `uncertain` 3: "The questions and answers. Ludwig Hartmann, who edited this part of Gregory's Register in the Monumenta Germaniae Historica after Paul Ewald's death, says they have often been doubted, and judges them genuine. He reports Theodor Mommsen's view that only extracts survive. James Barmby, translating the Register, holds Bede's copy the most authentic. Boniface, in a letter Hartmann dates to 735 in his preface and to before 741 in his note, reported that no copy could be found at Rome."
  - Card `uncertain` 4, last sentence: "Ludwig Hartmann has Laurentius succeed him in 606."
  - `sources.ownWords` 2 and `sources.about` 3: "(ed. Ludwig Hartmann, after Paul Ewald)".
  - Records claims 15, 17 and 27: change the witness from "MGH editors'" to "Ludwig Hartmann's note (or preface), in the volume he edited after Ewald's death (title page l.103–106)". Claim 17 should also carry "ante a. 741" (l.12690).
  - Contested claim 2: make the first side "Ludwig Hartmann".

  Cross-part, for the coordinator: part B's Leander and Reccared cards cite these same two volumes as "(ed. Paul Ewald and Ludwig Hartmann)". Leander cites "the editors' dating" and Reccared "the editors' notes". The same title-page fact applies to both.

- **R2-A-M1 MINOR (`columba.card.json` `uncertain` 4; `records.json` `columba` claim 11 and contested claim 3; optional for brief l.5; items 1 and 7; R1's A-B1 fix overshoots the other way).**
  - The fix now has Huyshe holding the battle to be the cause, which his note says (l.3022–3026).
  - His introduction is more reserved. It says: "It was this battle, according to tradition, that led to his exile from Ireland" (l.542–543).
  - It retells the mustering, the battle, the Teltown synod and the penance. Then it sets the whole group aside: "Such are the legends and traditions which cluster about the 'exile of Columba.'" (l.625–627).
  - Against them it sets the Old Irish Life's pilgrimage account, which it calls "perfectly simple and probable" (l.628–629).
  - The card keeps only his note's side and the penance as legend. It drops his own judgment that the plain pilgrimage account is probable.

  Fixes:
  - Card `uncertain` 4, the first two sentences: "Why he left Ireland. Huyshe's note says the battle of Cooldrevny was the cause of his exile, and he calls the tradition that it had something to do with his leaving a constant one. His introduction gives the battle as the cause 'according to tradition'. It counts the tales around his exile, the penance among them, as legends, and calls the Old Irish Life's account of a pilgrimage long resolved 'perfectly simple and probable'." Keep the rest as it stands.
  - Records claim 11: add "'It was this battle, according to tradition, that led to his exile' (l.542–543); the Old Irish Life's account is 'perfectly simple and probable' (l.628–629)". Add the same to the Huyshe side of contested claim 3.
  - Brief l.5, optional: "Huyshe and later Irish tradition tie the battle to his leaving." This saves two words: 401 words, FK 5.7, Flesch 77.2.

- **R2-A-M2 MINOR (`augustine-of-canterbury.brief.txt` l.5; items 1 and 7; the A-M9 brief fix).**
  - The brief reads: "Gregory wrote to Eulogius of Alexandria that more than ten thousand English were reported baptized one Christmas. Bede says Augustine then went to Arles…".
  - "Then" now follows the Christmas sentence. A listener hears that, in Bede, Augustine went to Arles after the Christmas baptisms.
  - Bede never mentions the Christmas baptisms. He opens I.27 "In the meantime, Augustine… repaired to Arles", right after the king's baptism and the gift of Canterbury (l.2033–2063).
  - Gregory's own letter says the opposite order: Augustine was "fratre et coepiscopo nostro" at those baptisms (Turchi l.9331).
  - Fix, word count unchanged: put Gregory's sentence last in the paragraph. "At Canterbury the king believed and was baptized. Bede says Augustine then went to Arles to be made archbishop of the English. In Bede's telling, Aetherius of Arles ordained him; the editor Nicola Turchi names Vergilius. Gregory wrote to Eulogius of Alexandria that more than ten thousand English were reported baptized one Christmas."
  - "Then" now follows the king's baptism, as in Bede, and the brief no longer sets Bede's order against Gregory's letter.

- **R2-A-M3 MINOR (`henana-of-adiabene.brief.txt` l.7 and l.11; item 4, pronouns; l.11 damaged by the A-B6 fix).**
  - l.11 now opens "His pupil Barhadbeshabba…". Mari's sentence, which named Henana just before, has moved to the card. The nearest "he" is now Labourt: "He cannot say if the charge about fate is false, but finds it plausible." (l.9).
  - l.7's "Gregory of Kashkar, metropolitan of Nisibis, condemned his books" can be heard as Gregory's own books. The drafter fixed the same trap in the Timothy sentence ("Henana's writings") but not here.

  Fixes:
  - l.7: "…condemned Henana's books." and "at the gate" for "at the city gate".
  - l.11: "Henana's pupil Barhadbeshabba wrote the Cause of the Foundation of the Schools while his master lived, Scher says." Scher: "du vivant même de son maître Hnana" (l.16994–16996).
  - l.13: "He says his master worked day and night to read and explain the Scriptures." Barhadbeshabba: "il s'appliquait jour et nuit à la lecture et à l'interprétation des Écritures" (l.21062–21063).
  - Scored together on a scratch copy: 325 words (2:00), FK 8.0, Flesch 60.5. "Henana's books" alone takes Flesch to 59.99, below the floor. The l.13 change is what keeps it above 60. Re-score after any other change.

- **R2-A-M4 MINOR (`README.md` l.7; for the lead, with A-M18).** "Henana of Adiabene's teaching is known only through his opponents". After A-B5 and the coordinator's ruling, the brief, card `knownFor` and `uncertain` 1 all read "the teaching he was condemned for". The README still makes the broader claim that Scher contradicts (scher1908 l.21084–21085). Fix: "The teaching Henana of Adiabene was condemned for is known only through his opponents; a pupil's praise of the man survives, and the brief says both."

No new or changed quotation is misquoted. I found no new absence claim that a held file contradicts, no editor's year told as the ancient writer's, and no contested point told as settled in a brief beyond R2-A-M2. Every common name in the new text carries a place or role at first mention: Augustine of Canterbury, Aetherius of Arles, Nicola Turchi, Wilfrid, Chosroes, Theodoret of Cyrrhus, George of Izla, Timothy I and the Annales Cambriae. Read whole and aloud in my head, the four briefs tell a story and flow, with no AI tells or beat lines. The fixes did not leave a choppy run, apart from the pronouns in R2-A-M3. Evagrius l.7's "before writing this" follows "he writes" and is clear in context. That is not a finding.

### Totals

R1 findings: of 6 blocking, 6 RESOLVED. Of 18 minor:
- 15 RESOLVED.
- 1 PARTLY (A-M8: a witness is now named, but the wrong one; see R2-A-B1).
- 1 resolved in form but carrying the same misattribution (A-M10; see R2-A-B1).
- 1 DEFERRED (A-M18, the README, to the batch 5 Open-Gaps entry before merge).
- None is NOT RESOLVED.

New: 1 blocking and 4 minor.
- R2-A-B1 (Augustine brief, card and records: Ewald credited with Hartmann's judgment).
- R2-A-M1 (Columba card and records).
- R2-A-M2 (Augustine brief).
- R2-A-M3 (Henana brief).
- R2-A-M4 (README).

R2-A-B1 and R2-A-M2 touch the Augustine brief and audio, and R2-A-M3 the Henana brief and audio. Each suggested brief fix was scored on a scratch copy and stays within its cap and above the Flesch floor.

Verdict: not clear until R2-A-B1 is fixed. It is a one-sentence brief fix plus card and records wording, checked here against the title page and note it cites. It needs a targeted recheck, not a new full round.

## Part B

Reviewer: fresh and independent; I did not draft or fix these files. Scope: the R1 part B findings (B-B1 to B-B3, B-M1 to B-M16) and every sentence `R1_changes.md` says was changed in `leander-of-seville`, `reccared` and `gregory-of-tours` (brief, audio, card, `records.json`). Each brief was also read whole, aloud in my head, for writing quality. I made no git, model or web calls, so I did not read a word diff. Instead I read the current files against R1's quoted old wording and the change log. Every new or changed sentence, quote and record was opened at its line in the vendored file, and I checked who speaks there: the ancient writer, a document he quotes, the translator, or an editor's note or margin. The OCR Latin files (PL 72, PL 83, Mommsen's Chronica minora II, the Madrid 1808 Collectio, Ewald and Hartmann, Arndt and Krusch, Leo and Krusch) were read by line. I edited no profile file. Line numbers point to files under `cic/texts/` unless another path is given. In the briefs, paragraphs sit on l.1, 3, 5 and so on, because blank lines count.

Context rulings applied. Reccared is a Who on Mark's named ruling, on his own confession at Toledo III. Dalton's view that Leander composed the speech is given as Dalton's, by the coordinator's call. Leander and Reccared are major (cap about 405 words). Gregory of Tours is standard length as a recorder (cap about 325). The 25-word limit applies to the narrator's prose and not to words quoted from a source.

Mechanical checks, all three:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]`. Each has one `[warmly]`, and it opens the closing paragraph. No tag appears in a brief or a card.
- `grade_text` passes for all three.
- No narrator sentence runs past 25 words. The longest are Reccared l.9, the letter (23, mostly quotation), and Reccared l.11, the Isidore close (23). Gregory's close is 26 words, but the narrator frame is 13 and the other 13 are Dalton's verbatim (dalton1927 l.22716–22717). That is within the ruling.
- All three cards and `records.json` parse. `records.json` holds the ten batch ids. The `briefLength` values fit. Reccared's "about 2 minutes 30 seconds" covers 2:26.

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Leander of Seville (MAJOR) | 405 | 2:30 | 7.6 | 62.6 | 405, at the cap |
| Reccared (MAJOR) | 394 | 2:26 | 7.0 | 68.7 | within |
| Gregory of Tours (recorder) | 324 | 2:00 | 5.0 | 78.7 | within |

## 1. The 3 R1 blocking findings

| Finding | Status | Evidence |
|---|---|---|
| B-B1 (Leander: Turchi's 584 given to the exile) | RESOLVED | Card `uncertain` 3: "Nicola Turchi says Leovigild exiled him for turning Hermenegild to the Catholic faith, and gives no year." Read across the two OCR columns, Turchi has: "Clarus episcopus Hispalensis ab an. circ. 584 ad an. 600 vel 601. Exilio multatus est a Leovigildo rege ariano Visigothorum Hispaniae, ob filium S. Hermenegildum ad fidem catholicam conversum" (turchi1907 l.2436–2445). The exile carries no year. Cave: "In Hispaniam reversus, anno 384, a Leuvigildo rege exsilio multatus est: qui tamen anno sequenti jam morti vicinus… Reccaredum filium Leandri curae commendavit" (PL 72 l.65149–65153). The card now gives no year for Cave, which is right, because "384" is damaged. Dalton: "After the prince's conversion Leander withdrew to Constantinople" (dalton1927 l.26925); "dared not return to Spain until the death of Leuvigild" (l.28853–28854). The records' exile `contested_claim` and `absent_details` now match. The card wording, which is R1's, keeps an attachment fault that R1 fixed in the brief (R2-B-M1). |
| B-B2 (Reccared: Ewald and Hartmann reported the wrong way round) | RESOLVED | Card `uncertain` 7 now gives both sides by name. Ewald and Hartmann's heading: "translata sine dubio per Probinum presbyterum anno 595 in Hispaniam profectum, nunc Romam reversum". Then Gams "contendit hanc epistulam falsam esse; cui Mommsen assentit putans eam ex seq. ep. confictam esse; equidem credo et hanc ep. male adservatam multisque locis corruptam esse et rusticitatem stili huic tempori…" (ewald-hartmann1893 l.15333–15337, OCR). Barmby: "The genuineness of this letter is considered doubtful. It may have been a forgery founded on Epistle CXXII… being such indeed Reccared's was not unlikely to be" (npnf213 l.2250–2255). The card's "They answer that the priest Probinus carried it, beyond doubt" reports their rebuttal and claims no more. The drafter was right not to tell the clause cut off after "huic tempori" as theirs in the card. The records mark it as cut off. |
| B-B3 (Gregory: false absence on the council) | RESOLVED | Card `uncertain` 1: "Leudast's charge and the trial are known only from Gregory… Venantius Fortunatus wrote a poem to King Chilperic for it". The poem's heading is "Ad Chilpericum regem quando synodus Brinnaco habita est" (leo-krusch1881 l.17820, OCR "Briunaco"). Dalton: "This council is celebrated by Fortunatus in a poem addressed to Chilperic, and containing a panegyric of Fredegund (Carm. ix. 1). He says nothing of the affair mentioned by Gregory" (dalton1927 l.27121–27123). The records' `contested_claim` adds the poem as the one outside witness, silent on the charge. |

## 2. R1 minor findings

**Leander of Seville**
- B-M1: RESOLVED. "Gregory's letter to him opens the finished Moralia on Job." The drafter's added change, "Monks who had followed Gregory there begged him…", holds: "whither I was followed by many of my brethren from the monastery" (bliss1844 l.622–623), at Constantinople (l.386–388, 452–454). "you too adding your influence" is at l.651–653.
- B-M2: RESOLVED. "Leander of Seville" at l.1. "Eutropius, abbot of Servitanum" at l.7. Card `legacy.traces` 2 and `uncertain` 7 read "abbot of the monastery of Servitanum". The source is "beatissimum Eutropium monasterii Servitani abbatem" (mommsen1894 l.20399–20400; also "Eutropius abbas monasterii Servitani", l.20237).
- B-M3: RESOLVED. "Isidore writes as his brother and from the Catholic side."
- B-M4: RESOLVED. "In exile abroad, Isidore says, Leander wrote two books against the heretics. Isidore names no place or year." The source is "Hic namque in exsilii sui peregrinatione composuit duos adversus haereticorum dogmata libros" (PL 83 l.122775–122778). "persecuted Leander" is right: "unto Bishop Leander, whom before he had greatly persecuted" (gardner1911 l.8075–8076).
- B-M5: RESOLVED. "A homily under Leander's name is told here in modern words. It calls this the most solemn of feasts…". The source is "Festivitatem hanc omnium esse solemniorem festivitatum novitas ipsa significat, quoniam sicut nova est conversio tantarum plebium" (collectio l.38313–38316) and "quorum asperitatem quondam gemebamus, de eorum nunc gaudemus credulitate" (l.38327–38329).
- B-M6: RESOLVED. "and he doubts the epitaph." The source is "sed ei epitaphio codicibus nescio quibus propagato quatenus fides habenda sit, nescio" (mommsen1894 l.21986–21987).
- B-M7: RESOLVED. "bowels" is gone from the brief. The verbatim piece "the image of thy countenance" is exact (npnf212 l.32625–32626). The card keeps the full quote. The new close leaves the subject of "he carried" open to Leander (R2-B-M2).
- B-M8: RESOLVED. The scan clause is gone.
- The cut of "Gregory was there on the business of the see of Rome." is RESOLVED. The quote "my most blessed brother" and the embassy line carry the scene.

**Reccared**
- B-M9: RESOLVED. "The whole Gothic people was there, it says. A great host of Sueves, brought under his kingdom, had also been called back." The sources are "Adest enim omnis gens Gothorum inclyta" (collectio l.36675) and "Nec enim sola Gothorum conversio ad cumulum nostrae mercedis accessit, quinimmo et Suevorum gentis infinita multitudo, quam praesidio coelesti nostro regno subjecimus… ad veritatis originem studio revocavimus" (l.36680–36683). The records note that the Goths are said to be present and the Sueves only converted. "called back" picks up the earlier "to call back a people", so the split reads well.
- B-M10: RESOLVED. The Spanish-era sentence is gone, and the card `dates` keeps it. The new close, "writes Isidore of Seville, Leander's brother, and his son…", now puts "Leander" right before "his son" (R2-B-M3).
- B-M11: RESOLVED. Percival is now in `sources.about`, with Henry Percival as author.

**Gregory of Tours**
- B-M12: RESOLVED. "He refused. If he died on the way, he said, they must "carry my dead body there and bury it", in Ernest Brehaut's English." The source is "if I have merit to see the holy Martin's church, I shall thank God; but if not, carry my dead body there and bury it, because I am determined not to return home" (brehaut1916 l.11595–11597). "He refused" rests on "I am determined not to return home" and does not stand as a beat line: it answers the friends' plea.
- B-M13: RESOLVED. "Gregory's own History tells of his clash with King Chilperic, who held Tours. Brehaut says the two were as a rule unfriendly." The source is "During these years Chilperic held Tours and the relations between him and Gregory were as a rule unfriendly" (brehaut1916 l.416–418).
- B-M14: RESOLVED in the brief. "In 573, by the reckoning of his editor W. Arndt, he became bishop of Tours" is right, and Arndt is named. "often the sole authority, Brehaut says, for the events it tells" matches "for these events it is often the sole authority" (brehaut1916 l.68–69). The l.3 pronoun slip is gone. The card `dates` wording, R1's with "his" changed to "Gregory's", gets Arndt the wrong way round (R2-B-B1).
- B-M15: RESOLVED. "No copy of that Life is quoted here." The records confirm that PL 133 holds only a notice.
- B-M16: RESOLVED. The `date` key on Fortunatus, Poems V.3 is removed.
- The close trim is RESOLVED. It is 13 narrator words around 13 words of Dalton, verbatim.

**Declined / noted.** R1_changes declines nothing. Its note on Turchi's "concilii Toletani III an. 585" (turchi1907 l.2443–2445) is accurate. Both briefs give 589 without crediting it to Turchi, so they need no change. Adding 585 to the records as a minority date stays with the coordinator.

## 3. New findings

- **R2-B-B1 BLOCKING (`gregory-of-tours.card.json` `dates`; items 1 and 7; an editor's judgment reported the wrong way round, carried by R1's B-M14 wording).** The card reads: "Bishop from 573, the year W. Arndt sets for Gregory's own count, the 172nd year after Martin's passing." Arndt says the reverse. He takes 573 from Gregory's twelfth year of King Sigibert and from the day count after Eufronius's death. He then says Gregory's own count of the 172nd year after Martin does not agree with it, and that this count gives 569, which is false: "Ex ipsis Gregorii verbis constat, anno duodecimo Sigiberti regis episcopum se consecratum esse, qui… cum anno 572. iam vergente et anno 573. magna ex parte completo congruit… [consecratum esse] constat, qui cum anno tantum 573. convenit. Cum hac ratione Gregorius ipse non consentit, duodecimo regis Sigiberti anno cum centesimo septuagesimo secundo post transitum sancti Martini comparans. Hic enim, Gregorio teste, Attico Caesario consulibus, id est a. 397, mortuus est. Quae computatio annum 569. efficit, qui sine dubio falsus est" (arndt-krusch1885 l.391–415, OCR read by line). Krusch says the same: "172 annos Mir. S. Mart. II, 1. computavit… In calculo sibi minime constat" (l.35416–35418). The editors' margin "573" beside Mir. Mart. II.1 (l.46663–46664) dates the event. It does not endorse the 172nd-year count. The brief needs no change.
  - Fix, card `dates`, second sentence: "Bishop from 573, which W. Arndt reckons from Gregory's own date, the twelfth year of King Sigibert. Gregory also calls it the 172nd year after Martin's passing, a count Arndt says does not agree."
  - Records: in the claim "'Anno centesimo septuagesimo secundo…'", add after "Arndt: consecration 'cum anno tantum 573 convenit'": "; Arndt: 'Cum hac ratione Gregorius ipse non consentit… Quae computatio annum 569 efficit, qui sine dubio falsus est' (l.410–415); Krusch: 'In calculo sibi minime constat' (l.35416–35418)", and widen the witness to "Arndt's preface (l.391–415); Krusch (l.35416–35418)".

- **R2-B-M1 MINOR (`leander-of-seville.card.json` `uncertain` 3; item 4; R1's B-B1 wording repeats the attachment fault R1 fixed in the brief at B-M4).** "Isidore says he wrote two books against the heretics in exile abroad, and gives no place or year." This can be heard as "heretics in exile". Fix: "Isidore says he wrote two books against the heretics while in exile abroad, and gives no place or year."

- **R2-B-M2 MINOR (`leander-of-seville.brief.txt` l.13 and the audio; item 4; pronoun in the closing line, from the B-M7 fix).** "Gregory once wrote to him that he carried "the image of thy countenance" stamped deep within his heart." After "to him" (Leander), "he carried" and "his heart" can be heard as Leander's. Only "thy" tells the listener otherwise, and this is the last line they hear. Fix (16 words, one fewer): "Gregory once wrote to him of carrying "the image of thy countenance" stamped deep within his heart." The quoted piece stays verbatim (npnf212 l.32625–32626). The audio follows the brief.

- **R2-B-M3 MINOR (`reccared.brief.txt` l.11 and the audio; item 4; pronoun, from the B-M10 fix).** "Leovigild was irreligious and quick to war, writes Isidore of Seville, Leander's brother, and his son pious in faith and famed for peace." The inserted "Leander's brother" now sits right before "his son", so the line can be heard as Leander's son. It also breaks Isidore's paired contrast in the middle. Fix (23 words): "Isidore of Seville, Leander's brother, wrote that Leovigild was irreligious and quick to war, and his son pious in faith and famed for peace." The source is "namque ille inreligiosus et bello promptissimus, hic fide pius et pace praeclarus" (mommsen1894 l.28264–28265). The next sentence keeps "Reccared". Re-scored with R2-B-M4: 395 words, FK 7.0, Flesch 69.0.

- **R2-B-M4 MINOR (`leander-of-seville.brief.txt` l.5 and `reccared.brief.txt` l.5; `CLAUDE.md` "one idea per paragraph (1–4 sentences)"; Reccared's paragraph lengthened by the B-M9 split).** Leander l.5 runs eight sentences on three matters: the exile, who turned Hermenegild, and the charge of Reccared. Reccared l.5 runs ten sentences, from the voice of the book through its creed to the signature. Both are long blocks on the page, though the audio is not affected. Fix, with no change to the words: in Leander, start new paragraphs at "Travellers from Spain told Gregory…" and at "Near death, Gregory the Great writes…". In Reccared, start a new paragraph at "God stirred him, burning with faith…". Gregory's l.1 and l.5 each tell one scene and pass. Leander after this and R2-B-M2: 404 words, FK 7.6, Flesch 62.6.

- **R2-B-M5 MINOR (`records.json`, `reccared`, `contested_claims` "Whose words the book of faith is"; item 1; unchanged text, found while checking B-B2's neighbours).** "John of Biclaro: written 'manu sua' (mommsen1894 l.20393-20395)." John has "confessionem tomo scriptam manu sua episcopis porrigens" (l.20390–20392). Here "manu sua" may go with "porrigens" (handing it to the bishops with his own hand) as well as with "scriptam", so the records give one reading as John's settled word on authorship. The card and brief do not use it. Fix: "John of Biclaro: the confession 'tomo scriptam manu sua episcopis porrigens', which can be read as written by his own hand or handed over by his own hand (mommsen1894 l.20390–20392)."

Observation, not a finding. Reccared l.5 says "O. M. Dalton, translating Gregory of Tours, says Bishop Leander of Seville composed the speech", which is accurate. The claim is in Dalton's note: "His speech on that occasion was composed by Leander (Labbe, Concilia, v, p. 997)" (dalton1927 l.29214). The sentence keeps Dalton's own word "speech" beside the brief's "book". It is given as Dalton's, per the coordinator's call, and nothing in it is wrong.

No new or changed quotation is misquoted. Every quote in the three briefs was re-checked at its line: bliss1844 l.386–388 and 452–454; gardner1911 l.8012–8017 and 8073–8077; npnf212 l.32625–32626; npnf213 l.3871–3872 and 3934; brehaut1916 l.11595–11597; dalton1927 l.10370–10371, 10397–10398 and 22716–22717. I found no witness swap and no new absence that a held file contradicts. No contested point is told as settled in a brief, and no hedge was dropped by a fix. Every common name in the changed text carries a place or role at first mention: Leander of Seville, Eutropius abbot of Servitanum, Isidore of Seville in the Reccared close, Ernest Brehaut, W. Arndt, Venantius Fortunatus and King Chilperic. The writing reads as story, with no AI tells. The only breaks in flow are the two pronoun slips and the two long paragraphs above.

## Totals

R1 part B findings: 3 blocking, all 3 RESOLVED. 16 minor, all 16 RESOLVED. None is partly or not resolved, and nothing was declined. Three R1 fix wordings each raise a new point: B-M14's card wording gives R2-B-B1, B-B1's card wording gives R2-B-M1, and B-M7's close gives R2-B-M2.

New: 1 blocking and 5 minor.
- R2-B-B1, BLOCKING, `gregory-of-tours` card `dates` and records: the card says Arndt sets 573 for Gregory's own 172nd-year count. Arndt says that count disagrees with 573 and gives 569, which he calls false.
- R2-B-M1, `leander-of-seville` card `uncertain` 3: attachment.
- R2-B-M2, `leander-of-seville` brief close: pronoun.
- R2-B-M3, `reccared` brief close: pronoun.
- R2-B-M4, `leander-of-seville` and `reccared` brief l.5: paragraph breaks.
- R2-B-M5, `reccared` records: the reading of "manu sua".

Every suggested wording was checked against the line it cites and keeps each brief within its cap. Verdict: not clear until R2-B-B1 is fixed. It is a card and records fix and needs no change to a brief. The three brief fixes (R2-B-M2 to M4) are pronoun and paragraph fixes, and their audio scripts follow the briefs. None of these needs a further full review round. A targeted check of the R2-B-B1 wording against arndt-krusch1885 l.391–415 is enough.

## Part C

Reviewer: fresh and independent. I did not draft or fix these files. Scope: Venantius Fortunatus, Baudonivia (a recorder) and Dorotheus of Gaza, all standard length, with their cards, audio scripts and `records.json` entries in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch5/`. I checked each against `R1_review.md` and `R1_changes.md` (part C), and checked Dorotheus against the paired batch 3 profile `barsanuphius-and-john-of-gaza` (`Who-Profiles/era3/batch3/`).

Method. I worked from the files as they stand, without git. I matched every R1 change against the before-text quoted in `R1_review.md`. I opened every new or changed sentence, quotation and `records.json` entry at its line in the vendored file, and checked who speaks there: the ancient writer, the translator, or an editor's note or apparatus. I read the OCR files (Leo and Krusch's MGH AA 4, Krusch's SRM 2 and 3, Arndt and Krusch's SRM 1, Migne PG 88, PG 99 and PL 88, Nau PO 8, the Nikodemos Synaxaristes) by line. Because R2 asks for writing quality at full effort, I read each brief whole, aloud in my head. I made no edits to profile files, and no git, model or web calls. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines, so paragraphs sit on l.1, 3, 5, 7, 9 and 11.

Mechanical checks, all three:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in a brief or card.
- `grade_text` passes all three (FK at most 10, Flesch at least 60).
- Length: all three are at 325 words, the standard cap. `briefLength` is "about 2 minutes" on all three.
- Sentences: no narrator sentence runs past 25 words. The longest is Venantius l.5, "He called Agnes a mother in honour and a sister in sweet love, and said his love was of the spirit, with Christ as witness." (25, unchanged). The longest changed sentence is Dorotheus l.3, "Gallandi reports that the Bollandists place him at the end of the sixth century, and that his death year is not clearly known." (23).
- `records.json` loads, the three ids are present, and all three cards parse as JSON. The two `date` keys C-M12 asked for are present.

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Venantius Fortunatus | 325 | 2:00 | 6.1 | 72.7 | 325, at the cap |
| Baudonivia (recorder) | 325 | 2:00 | 7.3 | 66.5 | 325, at the cap |
| Dorotheus of Gaza | 325 | 2:00 | 6.7 | 69.6 | 325, at the cap |

## 1. The 2 R1 blocking findings

| Finding | Status | Evidence |
|---|---|---|
| C-B1 (Baudonivia: her willing bishop dropped; a disagreement told as agreement) | RESOLVED | Brief l.9: "When the relic reached Poitiers, she says, the bishop and all the people wished to receive it. But the enemy of mankind worked through his agents to keep it out. Gregory of Tours tells it otherwise. Bishop Maroveus, he says, rode off to a country estate rather than receive it." Baudonivia II.16: "At ubi lignum… Pictavis civitatem… advenit, et pontifex loci cum omni populo devote hoc vellet excipere, inimicus humani generis per satellites suos egit, ut pretium mundi repellerent nec in civitatem recipere vellent" (`fredegar-…-mgh-srm-2-lat_krusch1888.txt` l.30256-30260, OCR "veUet", "repcnerent"). Gregory, HF IX.40: "the queen requested the bishop himself to deposit them in the convent… But he disregarded her proposal, mounting his horse, and going off to a country estate" (`gregory-tours_history-of-the-franks-v2_dalton1927.txt` l.19605-19610). The two accounts now differ, as the sources do. "To keep it out" leaves open who refused in the end, which is where the Latin is open: Dalton reads the devil as seducing "the Bishop Maroveus and the people" (l.29584-29586). Card `uncertain` 3 gives that reading, Krusch's note "Maroveus lignum noluit excipere" (l.30297), and Justin, Sophia and the triptych as Krusch's and Dalton's, not hers (Dalton l.29578-29581). Records: the claim and contested side 1 quote "pontifex loci cum omni populo devote hoc vellet excipere". |
| C-B2 (Dorotheus: false absence; John named by Dorotheus as Barsanuphius's disciple) | RESOLVED | Brief l.3: "Elsewhere in them he calls John the disciple of blessed Barsanuphius." Doctrina I: "Memini me quandoque abbatem Joannem beati Barsanuplii [OCR] discipulum interrogasse" (`dorotheus-gaza_…_migne-pg88.txt` l.124094-124096). Card `knownFor`, `uncertain` 3 and records claim 4 (now Documented) agree. "The Prophet" stays with the Questions heading ("cognomento Prophetam", l.139574-139576) and Gallandi ("Prophetae titulo clarum", l.121958). The drafter rightly left out R1's "the only abbot John in the Teachings": unqualified mentions stand at l.124325, 132084 and 136052. **Agreement with the paired batch 3 profile now holds on every shared point.** Batch 3 makes John Dorotheus's teacher ("his teacher, the abbot John of Gaza"; `knownFor` "whose written answers guided Dorotheus"), and so does this profile. Both give the epithet to the heading. Both use Gallandi's report of the Life of Dositheus, Nau's heads in turn (Barsanuphius, Seridus, Dorotheus) and his birth "vers 540", Thabatha, Migne's 596 heading over Gallandi's notice, the anonymous preface's two Barsanuphii and two Dorothei, Theodore's separating the condemned men, and Hilarion of Verona's Latin as revised by Fronto Ducaeus. Neither retells the other's scenes. |

## 2. R1 minor findings

**Venantius Fortunatus**
- C-M1: RESOLVED. Brief l.5, "Radegund, once the wife of King Chlothar the First". Krusch "a Chlothario I rege Francorum capta" (AA 4 l.41894-41895).
- C-M2: RESOLVED. l.7 places Dalton ("O. M. Dalton, Gregory's English translator"). l.9 reads "Dalton thinks". Dalton's note cites his Introduction, which is not among the sources used here (l.26296-26299). The changed l.7 sentence has a flow fault; see R2-C-M2.
- C-M3: RESOLVED. "Gregory of Tours, who calls him his venerable fellow servant, says he told Martin's life in four books of verse." Virt. Mart. I.2, "Fortunatus presbiter omne opus vitae eius in quattuor libris versu conscripsit" (`gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt` l.45245-45246); I.13 as Leo quotes it (AA 4 l.51804-51806). Both are in the same work, so "Gregory… says" is true of both. "Radegund's house" picks up "her monastery of the Holy Cross" from l.5. The two length trims ("church of Saints Paul and John", "altar of Martin of Tours") keep the sense of Paul's "the church of the blessed Paul and John… an altar, built in honor of St. Martin the Confessor" (`paul-the-deacon_…_foulke1907.txt` l.4084-4087).
- C-M4: RESOLVED. Card `uncertain` 3: "W. D. Foulke, citing R. Jacobi's study of Paul's sources, says…". Foulke "Venantius Fortunatus (Jacobi, 27, 28). From the poem… Paul took the birth place of the poet" (l.15711-15713); "A complete discussion by Dr. R. Jacobi of the sources from which Paul derived his history appeared in… 1877" (l.174-177). The records witness matches.
- C-M5: RESOLVED. Card `dates`: "M. A. Luchi reports the belief that he was born about 530, and puts his death early in the seventh century". Luchi, "si ipse natus crediiur [OCR] circ:i annum 530, jamque senex Pictavis obiit, saeculo septimo ferme ineunte" (`regula-magistri-cresconius-pl88-lat_migne1862.txt` l.1101-1103, OCR cleaned).
- C-M6: RESOLVED. The contested claim "Which prose Lives are his" checks: the codex clause and Soissons monks (AA 4 l.42457-42468); Krusch "post a. demum 602 scripta" and "quaestio inanis" (l.42545-42550); Tillemont on a "Fortunatum quendam poeta paulo vetustiorem" (l.41187-41193) and on Fortunatus of Vercelli for Marcellus (l.42163-42164), which Krusch rejects (l.42186-42187); Arndt and Krusch "brevis, Fortunato male tributa" (SRM 1 l.60196-60197). The Agnes claim checks: Carm. XI.5 heading "ad abbatissam" and "Agnes" (OCR, AA 4 l.22331-22334).

**Baudonivia**
- C-M7: RESOLVED. Brief l.3: "Baudonivia was a nun of Holy Cross at Poitiers, the house Queen Radegund founded." Dalton "when the blessed Radegund founded the monastery" (l.19597-19598); Krusch "regina Thoringorum" (AA 4 l.41894). Records claim added.
- C-M8: RESOLVED in substance. Pascentius is now "then bishop of Poitiers": Fortunatus sent him the book as bishop ("Pascentio Pictanensi [OCR] episcopo misit", AA 4 l.41118) and addresses him "PATRI PaSCENTIO PAPAE" (l.42997). The narrator's own inference is gone, and Krusch's reading replaces it ("neque vivi, sed monasterii", l.41121-41122). Card `uncertain` 2 and the records match. The rewording leaves a pronoun and number fault; see R2-C-M3.

**Dorotheus of Gaza**
- C-M9: RESOLVED. "Seridus sent Dorotheus to serve John." "apud abbatem Seridum… imperavit abbas" (l.126276-126278).
- C-M10: RESOLVED. "A Greek letter printed before the Teachings calls Dositheus his first disciple." The Greek reads "τὸν… Δοσίθεον, τὸν γενόμενον πρῶτον μαθητὴν τοῦ μακαρίου ἀββᾶ Δωροθέου ἔτι ὄντος αὐτοῦ ἐν τοῖς τοῦ ἀββᾶ Σερίδου" (OCR "Aozídsos, -Sv T5670 re6rov pa0nziyy to$ paxapiou àC6d Auoo0£ou", l.122463-122464). The Synaxaristes has Dositheus in Seridus's house "ὑπὸ τὴν προστασίαν τοῦ ἁγίου Δωροθέου" (l.37925-37927). Card `uncertain` 5 and the records claim match. Dropping "in Greek and Latin" after Migne loses nothing, since the card keeps the languages.
- C-M11: RESOLVED on the card and in the records. Card `uncertain` 1 adds Nau, "Barsanuphios, Séridos et enfin Dorothée" (po08 l.11421-11424). The "?" is footnote 3, "3. Dorothée est né vers 540" (l.11524), and the records now say so. The new `contested_claims` entry "Which monastery Dorotheus headed" checks. The brief still tells only one side of it; see R2-C-M4.

**Two cards**
- C-M12: RESOLVED. `"date": null` is on the Luchi entry (Venantius card l.91) and the unsigned PL 72 note (Baudonivia card l.84).

## 3. The declined and reworded points

- **C-B2, "the only abbot John in the Teachings".** The reason for leaving it out holds. See the evidence in section 1.
- **C-M2 and C-M3, Venantius l.7, reworded.** The source support holds. The new Dalton sentence reads badly aloud (R2-C-M2).
- **C-M8, Baudonivia l.7, reworded into two sentences.** The facts hold. The pronoun does not (R2-C-M3).
- **C-M10, Dorotheus l.5, the letter given its own sentence.** The reason holds: the attribution now attaches to the right claim, and "Dorotheus says" in the next sentence keeps "he" from pointing at the letter.

## 4. New findings

No new blocking finding.

- **R2-C-M1 MINOR (all three cards, two briefs; items 4, 12; the Library's word "held").** The batch 1 review ruled the Library's register off participant text. Batch 1 `R1_changes.md` carried "Part A M16… the Library's word 'held' on a participant card" to every card, and this batch's own A-M6 applied it to part A, with "used here" as the accepted form. Part C still uses "held" in two briefs, which are spoken, and on all three cards. A listener cannot know what "a held mention" or "no held source" means.
  - Venantius brief l.9: "Gregory calls him a priest in every held mention." Fix: "Gregory never calls him anything but a priest." (8 words for 9). Dalton is the witness for "never": "Gregory never alludes to Fortunatus as bishop" (l.26297-26298). Every Gregory mention in the Library agrees (records claim "Gregory calls him presbyter in each held mention").
  - Baudonivia brief l.3: "No held source gives her family, age or death; this account rests on her book." Fix: "The sources give nothing of her family, age or death. This account rests on her book." (+1 word, offset in R2-C-M3).
  - Venantius card: `keyWorks` 2 "held in Latin only" becomes "given here in Latin only". `uncertain` 1: "in every held mention" becomes "each time he names him"; "which is not held" becomes "which is not among the sources used here"; "No held source dates the bishopric" becomes "No source used here dates the bishopric". `uncertain` 4: "No English translation of them is held" becomes "No English translation of them is among the sources used here"; "with no held source behind it" becomes "with no source used here behind it".
  - Baudonivia card: `dates` "No year of her life is held" becomes "No source used here gives a year of her life". `uncertain` 1: "No held source gives" becomes "No source used here gives".
  - Dorotheus card: `uncertain` 4 "without his reasons in the held lines" becomes "without giving his reasons in the lines used here". `uncertain` 5 "The Life itself is not held" becomes "The Life itself is not among the sources used here". `uncertain` 6 "no held line ties him" becomes "no line used here ties him". `uncertain` 7 "No English of Dorotheus is held" becomes "No English of Dorotheus is among the sources used here".
  - `records.json` is not participant text and may keep "held".

- **R2-C-M2 MINOR (Venantius brief l.7; item 4; created by the C-M2/C-M3 fix).** "O. M. Dalton, Gregory's English translator, says when Radegund's house received a relic of the Cross, Fortunatus marked it with hymns." Aloud, "says when" first sounds as if Dalton says when something happened, and the clause only resolves at "Fortunatus". Fix: "O. M. Dalton, Gregory's English translator, says that when Radegund's house received a relic of the Cross, Fortunatus marked it with hymns." (+1 word, offset by the l.9 fix in R2-C-M1.) Dalton: "the arrival of which at Poitiers was celebrated by Fortunatus in several hymns" (l.27597-27598).

- **R2-C-M3 MINOR (Baudonivia brief l.7; items 4, 9; created by the C-M8 fix).** "One phrase says Radegund raised her from the cradle as her own household servant. Fortunatus first wrote those words of Hilary and Pascentius, then bishop of Poitiers. There, Krusch says, they mean that Hilary's monastery raised him." There are three faults. "Those words… they" follows "One phrase", so the number shifts. "Words of Hilary and Pascentius" can be heard as words Hilary and Pascentius wrote. "Raised him" can point to Fortunatus, Hilary or Pascentius. The Latin is plain: Fortunatus writes of Hilary, "qui te ab ipsis cunabulis ante sua vestigia quasi peculiarem vernulam familiariter enutrivit", where "te" is Pascentius (AA 4 l.43008-43009). Krusch reads it "Erat quidem Pascentius S. Hilarii alumnus, neque vivi, sed monasterii" (l.41121-41122). Fix: "Fortunatus first wrote it of Hilary raising Pascentius, then bishop of Poitiers. There, Krusch says, it means Hilary's monastery raised Pascentius." This is 21 words for 22. With R2-C-M1 the brief stays at 325 words; scored FK 7.3, Flesch 65.9.

- **R2-C-M4 MINOR (Dorotheus brief l.9; items 7, 10, 4; a Contested claim told one way, as a one-line paragraph).** Brief l.9 is a single sentence: "A later Greek book of saints, revised by Nikodemos the Hagiorite, says he founded his own monastery after John died." Since C-M11, the records hold this as a `contested_claim`, "Which monastery Dorotheus headed", and the card gives Nau's other side. The pattern's Confidence section says a Contested point "gives both sides by name", and the brief tells disputes in place. The sentence is attributed and marked late, so it is not told as settled, and the finding is minor. But a listener hears one account only. Nau has Dorotheus as a later head of Seridus's own house: "le monastère dont les hégouménes successifs ont été, au vi siecle, Barsanuphios, Séridos et enfin Dorothée" (po08 l.11422-11424). The paragraph also stands as one line. Fix, scored (324 words, FK 6.8, Flesch 68.0):
  - l.9: "A later Greek book of saints, revised by Nikodemos the Hagiorite, says he founded his own monastery after John died. The scholar François Nau instead makes him a later head of Seridus's monastery." Nau's first mention in this brief gets "the scholar", as Krusch gets "The German scholar" in the other two briefs.
  - To hold length, l.3: "Andrea Gallandi's notice, which Migne reprints, calls…" becomes "Andrea Gallandi's notice calls…". The reprint stays on the card's `sources.about`, and the credit stays with Gallandi, so batch 3's C-B5 fault does not come back. Also in l.3, "Gallandi reports that the Bollandists place him at the end of the sixth century, and that his death year is not clearly known." becomes "The Bollandist scholars, Gallandi reports, place him late in the sixth century." That keeps the time anchor. The unknown death year stays on the card's `dates` and in the records. "Bollandist scholars" gives the Bollandists the context they lack. Gallandi's "eruditus ex sociis Bollandianis" (l.121968) supports it, and "late in" stands for his "sub finem seculi vi" (l.121961-121962).
  - The paired profile agrees: batch 3 card `uncertain` 3 gives Nau's heads in turn in the same terms.

- **R2-C-M5 MINOR (Venantius brief l.1; item 8; the subject's first mention).** The brief opens "Fortunatus and his friend Felix of Treviso…" and gives "Venantius Fortunatus" only at l.3. The pattern's common-name rule covers the subject's own name ("Gregory of Nazianzus came to Constantinople"). Fortunatus is a common name, and the card itself lists Fortunatus of Grado, of Naples and of Fano as other men (`uncertain` 6). R1 checked only Chlothar for this item. Fix, with no change in length: l.1 "Venantius Fortunatus and his friend Felix of Treviso suffered…", and l.3 "Fortunatus was a poet from northern Italy." With R2-C-M1 and R2-C-M2 the brief stays at 325 words, FK 6.1, Flesch 72.7.

- **R2-C-M6 MINOR (Dorotheus card `uncertain` 3; item 1; wording).** "Elsewhere in the Teachings Dorotheus calls his abbot John the disciple of blessed Barsanuphius". John was not Dorotheus's abbot. Dorotheus was "apud abbatem Seridum" and served John at Seridus's order (l.126276-126278). "Abbot" is John's title, and the card's `keyWorks` keeps the two apart ("the abbot Seridus and the abbot John"). This is the same ambiguity R1 fixed in the brief (C-M9). Fix: "Elsewhere in the Teachings Dorotheus calls the abbot John the disciple of blessed Barsanuphius".

Read whole, the three briefs tell stories and carry the dispute in place. Venantius has the bishopric with Paul, Baudonivia and Gregory, and Baudonivia has the Cross with Gregory. Their R1 changes did not break the flow beyond R2-C-M2 and R2-C-M3. I heard no AI tells, beat lines, aphorisms or "not X but Y" contrasts in the narrator's prose. Every quotation in the changed text matches its file.

## Part C totals

| Profile | Blocking | Minor |
|---|---|---|
| Venantius Fortunatus | 0 | 3 (R2-C-M1 part, R2-C-M2, R2-C-M5) |
| Baudonivia | 0 | 2 (R2-C-M1 part, R2-C-M3) |
| Dorotheus of Gaza | 0 | 3 (R2-C-M1 part, R2-C-M4, R2-C-M6) |
| **Part C** | **0** | **6 (R2-C-M1 to R2-C-M6)** |

R1 status: both blocking findings (C-B1, C-B2) and all 12 minor findings (C-M1 to C-M12) are resolved. Dorotheus agrees with the batch 3 Barsanuphius and John profile on every shared point. With every fix above applied, all three briefs stay at or under 325 words and pass `grade_text`.

