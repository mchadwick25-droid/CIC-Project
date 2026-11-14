# R3 recheck: era 3 batch 5

The third and last round. Three fresh Opus reviewers, none of whom drafted or fixed the files, rechecked the R2 findings, every changed sentence, and each brief read whole, at full effort. Totals: all 17 R2 findings resolved but one partly (R2-A-M1, carried as R3-A-M1); 1 new blocking and 9 new minor points (part A 0 and 3, part B 0 and 3, part C 1 and 3). Verdicts: nine profiles CLEAR; Venantius Fortunatus NOT CLEAR on R3-C-B1, a card sentence (its brief is clear).

## Part A

Scope: round 3, the last allowed. Part A covers Columba and Augustine of Canterbury (major), Evagrius Scholasticus and Henana of Adiabene (standard), with their cards, audio scripts and `records.json` entries, and the batch README. I am a fresh reviewer; I did not draft or fix these files. I read the round 2 changes as a word diff from `0b995947` (the files R2 reviewed) to the working tree, limited to `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch5/`. I checked them against `R2_recheck.md` (R2-A-B1, R2-A-M1 to M4, with A-M8, A-M10 and A-M18) and `R2_changes.md`. Under part A, these changed:
- the Augustine brief, audio, card and records entry
- the Columba brief, audio, card and records entry
- the Henana brief and audio
- the README's Henana sentence

Evagrius did not change. I then read all four briefs whole, aloud in my head. I opened each changed sentence at its line in the vendored file and checked who speaks there: the ancient writer, a translator, an editor's note, or a title page or preface. Coordinator rulings applied: Evagrius's card tradition is "The Byzantine Imperial Church (Justinianic)"; Henana's brief says the teaching he was condemned for is known only through his opponents, and that a pupil's praise of the man survives; the README's Open-Gaps sentence is met by Open-Gaps 248, written before merge. I edited no profile file, and made no git writes, model calls or web requests. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines.

### 1. The R2 findings

| Finding | Status | Check against source |
|---|---|---|
| R2-A-B1 (Augustine: Ewald credited with Hartmann's judgment), with A-M8 and A-M10 | RESOLVED | Brief l.7: "Ludwig Hartmann, editing Gregory's letters, says these answers have often been doubted, and judges them genuine." The title page reads "POST PAVLI EWALDI OBITVM / EDIDIT / LVDOVICVS M. HARTMANN" (`gregory-great_registrum-epistolarum-t2-pars2-libri-10-14-lat_ewald-hartmann1895.txt` l.103–106). The note: "De hac epistula, an genuina sit, saepe disputatur" (l.12643), "non dubito, quin genuina sit" (l.12704), and Ewald in the third person, "Ewald coniecit etiam" (l.12696–12697). Card `uncertain` 3: Mommsen "excerpta tantum nobis asservata esse" (l.12704–12706); Boniface "quaesita non inveniebatur" (l.12696); "a. 735" in the preface (l.196) and "ante a. 741" in the note (l.12690). Both dates now go to Hartmann, and neither is told as settled. Card `uncertain` 4: "Laurentius a. 606 Augustino episcopus successit" (l.10692–10693). `sources.about` 3 cites the 1893 volume, which has the same title page (`…t2-pars1-libri-8-9-lat_ewald-hartmann1893.txt` l.136–139). Records claims 15, 17 and 27 and contested claim 2 now give the witness as Hartmann, with the title-page line. No "Ewald and Hartmann" or "the editors" is left in the Augustine card or records. Two changed card sentences run past 25 words (R3-A-M2). |
| R2-A-M1 (Columba: Huyshe's reserve dropped) | PARTLY | The reserve is now on the card, in the records and in the brief. Huyshe's introduction says "It was this battle, according to tradition, that led to his exile" (`adomnan_life-of-saint-columba_huyshe1905.txt` l.542–543). It says "Such are the legends and traditions which cluster about the 'exile of Columba.'" (l.625–627) and gives the Old Irish Life's "perfectly simple and probable statement" (l.628–629). The resolve to go on pilgrimage was "from the beginning of his life" (l.636). His note says "It was the cause of Columba's exile" (l.3022–3026). Brief l.5 now reads "Huyshe and later Irish tradition tie the battle to his leaving", which holds for both the note and the introduction. But the fix gives the "constant one" sentence to Huyshe's note, and that sentence is from the introduction (R3-A-M1). |
| R2-A-M2 (Augustine: "then" after the Christmas sentence) | RESOLVED | Brief l.5 now runs: the king's baptism; "Bede says Augustine then went to Arles…"; Aetherius and Turchi's Vergilius; and last, Gregory's Christmas letter. Bede follows the baptism and the gift of Canterbury (`bede_ecclesiastical-history-english-people_giles1903.txt` l.2033–2051) with I.27, "In the meantime, Augustine, the man of God, repaired to Arles" (l.2063–2064; OCR "Aries"). So "then" now follows the event Bede puts before it. Gregory: "plusquam decem milia Angli ab eodem nuntiati sunt fratre et coepiscopo nostro baptizati" (`gregory-great_epistolae-selectae_turchi1907.txt` l.9332–9333). The paragraph no longer sets one order against the other. Card `uncertain` 2 still names both orders. Read aloud, the Christmas sentence closes the paragraph clearly. |
| R2-A-M3 (Henana: pronouns at l.7 and l.11) | RESOLVED | l.7: "condemned Henana's books", from the Chronicle, "alors Gregoire condamna les livres qu'Il avait composes" (`chronicle-of-seert_histoire-nestorienne-seconde-partie-po13-ara-fra_scher1919.txt` l.28610, OCR). "At the gate": "secoue la poussiere de ses sandales k la porte de Xisibe" (l.28668–28669, OCR). l.11: "Henana's pupil Barhadbeshabba wrote … while his master lived, Scher says." Scher's words are "du vivant même de son maître Hnana" (`barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt` l.16994). l.13: "worked day and night to read and explain the Scriptures", from "il s'appliquait jour et nuit à la lecture et à l'interprétation des Écritures" (l.21062–21063). The subject there is Henana, who succeeds Abraham at l.21006. Every pronoun in l.7 to l.13 now has a clear owner. Flesch 60.51 is still above the floor. |
| R2-A-M4 (README: Henana sentence) | RESOLVED | README l.7: "The teaching Henana of Adiabene was condemned for is known only through his opponents; a pupil's praise of the man survives, and the brief says both." This matches the ruling, the brief l.3 and card `knownFor` and `uncertain` 1. It also agrees with Scher's "Il ne nous est parvenu de ces ouvrages que les traités sur les Rogations et le vendredi d'or" (scher1908 l.21084–21085). |
| A-M18 (README: "The correction is logged in Open-Gaps.") | DEFERRED, as ruled | README l.9 is unchanged. Open-Gaps 248 is not yet in `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`. The coordinator's ruling has it written before merge, and it must log the Evagrius tradition correction. Until it exists, the README sentence is not true. |

### 2. New findings in changed text

- **R3-A-M1 MINOR (`columba.card.json` `uncertain` 4; `records.json` `columba` claim 11 and contested claim 3, first side; items 1 and 9).** This is R2's own fix wording.
  - The card says: "Huyshe's note says the battle of Cooldrevny was the cause of his exile, and he calls the tradition that it had something to do with his leaving a constant one. His introduction gives the battle as the cause 'according to tradition'."
  - The "constant one" sentence is not in a note. It is on page xlvi of Huyshe's introduction, in the section headed "THE 'ALTUS' OF COLUMBA" (huyshe1905 l.1548–1574). The notes begin after the text, and the note on "Cule-Drebene" is at l.3018–3026.
  - The card's "he" is Huyshe, so read strictly it is true. But the card sets the note against "His introduction", so the reader takes the constant-tradition sentence as part of the note's firmer view. In fact it is one of the introduction's reserved lines: "had something to do with".
  - The records say it outright. Claim 11 has "Huyshe's note holds the battle the cause of his exile: 'It was the cause of Columba's exile'; 'The tradition is a constant one…'". Contested claim 3 has "his note says … 'was the cause of Columba's exile', a constant tradition (l.1571–1574, 3022–3026)". Both put an introduction line in the note.
  - A second, smaller point: this card field is the only one in part A that quotes with single quotation marks. The rest of the batch uses double ones (Augustine `uncertain` 1, Evagrius `legacy.remembered` 1). Its two long sentences also run 30 and 29 words.
  - These do not change what Huyshe says, so this does not block.

  Fixes:
  - Card `uncertain` 4, everything before "Adomnán names the battle only to date the voyage.": "Why he left Ireland. Huyshe's note says the battle of Cooldrevny was the cause of his exile. His introduction gives the battle as the cause \"according to tradition\", and calls the tradition that it had something to do with his leaving a constant one. It counts the tales around his exile, the penance among them, as legends. It calls the Old Irish Life's account of a pilgrimage long resolved \"perfectly simple and probable\"." The rest of the field stays as it is. The longest sentence is now 25 words.
  - Records claim 11: "Huyshe's note holds the battle the cause of his exile: 'It was the cause of Columba's exile' (l.3026). His introduction is more reserved: 'It was this battle, according to tradition, that led to his exile' (l.542–543); 'The tradition is a constant one that the strife and bloodshed of Cuil Dremhne had something to do with Columba's leaving Ireland' (l.1571–1574); of the tales: 'Such are the legends and traditions which cluster about the exile of Columba. The Old Irish Life says nothing of them', and its account is 'perfectly simple and probable' (l.626–629)". The witness line can stay.
  - Contested claim 3, first side: "Huyshe: his note says the battle of Cooldrevny 'was the cause of Columba's exile' (adomnan huyshe1905 l.3022–3026); his introduction gives it 'according to tradition' (l.542–543), calls the tradition that the battle had something to do with his leaving a constant one (l.1571–1574), counts the tales around the exile as legends (l.626–627) and calls the Old Irish Life's pilgrimage account 'perfectly simple and probable' (l.628–629)".
  - The brief needs no change.

- **R3-A-M2 MINOR (`augustine-of-canterbury.card.json` `uncertain` 3; item 4, sentence length; R2's own fix wording).**
  - "Ludwig Hartmann, who edited this part of Gregory's Register in the Monumenta Germaniae Historica after Paul Ewald's death, says they have often been doubted, and judges them genuine." This is 28 words and has a long nested clause.
  - "Boniface, in a letter Hartmann dates to 735 in his preface and to before 741 in his note, reported that no copy could be found at Rome." This is 27 words, with the two dates nested inside it.
  - Fix: "The questions and answers. Ludwig Hartmann edited this part of Gregory's Register in the Monumenta Germaniae Historica after Paul Ewald's death. He says they have often been doubted, and judges them genuine. He reports Theodor Mommsen's view that only extracts survive. James Barmby, translating the Register, holds Bede's copy the most authentic. Boniface reported that no copy could be found at Rome. Hartmann dates his letter to 735 in his preface and to before 741 in his note."
  - The content is right. The longest sentence is now 18 words. This does not block.

- **R3-A-M3 MINOR (`henana-of-adiabene.card.json` `uncertain` 3, first sentence; item 5).** This text did not change in round 2. R1 and R2 did not raise it, and I record it because it fails a checklist item.
  - The card says: "The synods that their editors date to 585, 596 and 605…". A role stands in for the named witness, the case item 5 names ("his editor").
  - The records' absent detail gives the dates from Chabot's edition (`synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt` l.26590–26712, 30464–31377, 31388–31700). Chabot is already named on this card, in `dates`, as "J.-B. Chabot".
  - Fix: "The synods. The synods that Chabot, their editor, dates to 585, 596 and 605 defend Theodore's writings but never name Henana, as Braun notes." The next sentence's "Chabot and Braun" then reads as a second mention. The word count is unchanged.
  - This does not block.

No changed text adds a misquotation, a witness swap, a false absence, an unsupported claim, a dropped hedge, or a contested point told as settled. Hartmann's preface says it largely repeats Paul Ewald's own published study ("maxima ex parte succincte ea repetunt, quas Paulus Ewald ipse… disseruit", ewald-hartmann1895 l.169–171). Hartmann signs it (l.178–181), and it speaks in his first person ("Equidem non dubito", l.190). So "Hartmann dates [it] to 735 in his preface" is fair, and it is not a finding. Every name new to round 2 has its identifier at first mention: Ludwig Hartmann and Paul Ewald in brief and card, and Henana and Barhadbeshabba in the brief.

### 3. The four briefs read whole

- **Columba.** It reads as a story from the granary scene to the death before the altar. The new l.5 sentence, "Huyshe and later Irish tradition tie the battle to his leaving", sits well between the two dates and Adomnán's use of the battle. There are no AI tells or beat lines.
- **Augustine of Canterbury.** With the move, l.5 follows Bede's order and ends on Gregory's own count of the baptisms. The new l.7 sentence is clear, and its single witness makes it shorter. The close is plain.
- **Evagrius Scholasticus.** It is unchanged and still reads well.
- **Henana of Adiabene.** It now flows from the walkout to Barhadbeshabba's prayer. "Henana's" at l.7 and l.11 settles the owners of the books and the pupil. "His master" at l.11 and l.13 is clear.

None of the four has a choppy run, a pronoun left without its owner, or a narrator sentence past 25 words. The longest are Henana l.9 (25) and Columba l.7 (24). Augustine l.7 (31) is long only because of Gregory's quoted words.

### 4. Mechanical checks

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Columba (major) | 401 | 2:29 | 5.67 | 77.25 | 405 |
| Augustine of Canterbury (major) | 402 | 2:29 | 7.15 | 70.29 | 405 |
| Evagrius Scholasticus | 325 | 2:00 | 7.42 | 67.02 | 325 |
| Henana of Adiabene | 325 | 2:00 | 8.04 | 60.51 | 325 |

- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script).
- Each script opens with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in a brief or card.
- `grade_text` passes on all four: FK 10 or below, Flesch 60 or above.
- All four are within their length caps, and each `briefLength` still fits: "about 2 minutes 30 seconds" for the majors and "about 2 minutes" for the standards.
- Evagrius's `tradition` reads "The Byzantine Imperial Church (Justinianic)", as ruled.
- `records.json` and the four cards parse. `records.json` holds the ten batch ids, and part A has these entries:

| Profile | Claims | Contested claims | Absent details |
|---|---|---|---|
| Columba | 36 | 5 | 3 |
| Augustine of Canterbury | 28 | 3 | 2 |
| Evagrius Scholasticus | 22 | 1 | 4 |
| Henana of Adiabene | 26 | 3 | 4 |

- The records cover every fact in the changed text.

### Verdict per profile

- **Columba: CLEAR.** R3-A-M1 is minor: Huyshe's introduction line is given to his note, plus quotation-mark style and two long sentences.
- **Augustine of Canterbury: CLEAR.** R2-A-B1 is resolved against the title page and note. R3-A-M2 is a minor sentence split.
- **Evagrius Scholasticus: CLEAR.** Nothing changed and nothing is open.
- **Henana of Adiabene: CLEAR.** R3-A-M3 is a minor role-for-witness fix on the card.
- **README: CLEAR on its text.** A-M18 waits on Open-Gaps 248, which must exist before merge, as ruled.

### Totals

R2 findings:
- R2-A-B1, R2-A-M2, R2-A-M3 and R2-A-M4 are RESOLVED, with A-M8 and A-M10.
- R2-A-M1 is PARTLY resolved, carried by R3-A-M1.
- A-M18 is DEFERRED to Open-Gaps 248, as ruled.
- None is NOT RESOLVED.

New: 0 blocking and 3 minor.
- R3-A-M1: Columba card and records.
- R3-A-M2: Augustine card.
- R3-A-M3: Henana card.

No brief or audio script needs to change.

## Part B

Scope: round 3, the last allowed. This recheck covers the R2 part B findings (R2-B-B1, R2-B-M1 to R2-B-M5) and the R2-A-B1 credit change as `R2_changes.md` applied it to part B. It covers `leander-of-seville`, `reccared` and `gregory-of-tours` (brief, audio, card, `records.json`). I read each changed sentence as if new. I also read each brief whole, aloud in my head, for writing quality. I made no git, model or web calls, so I read no word diff. Instead I read the current files against R2's quoted wording and the change log. Each cited line was opened in its vendored file, and I checked who speaks there. I edited no profile file. Line numbers point to files under `cic/texts/` unless another path is given. In the briefs, paragraphs sit on l.1, 3, 5 and so on, because blank lines count.

Context rulings applied. Reccared is a Who on Mark's named ruling. Dalton's view that Leander composed the speech is given as Dalton's, by the coordinator's call. Leander and Reccared are major (cap 405 words). Gregory of Tours is standard length as a recorder (cap 325). The 25-word limit applies to the narrator's prose, not to quoted words.

## 1. The R2 findings

| Finding | Status | Check against source |
|---|---|---|
| R2-B-B1 Gregory card `dates`: Arndt reported as setting 573 for the 172nd-year count | RESOLVED | The card now reads "Bishop from 573, which W. Arndt reckons from Gregory's own date, the twelfth year of King Sigibert. Gregory also calls it the 172nd year after Martin's passing, a count Arndt says does not agree." Arndt: "Ex ipsis Gregorii verhis constat, anno duodecimo Sigiberti regis episcopum se consecratum esse" (`gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt` l.391–392, OCR). Then "cum anno tantum 573. convenit. Cum hac ratione Gregorius ipse non consentit, duodecimo regis Sigiberti anno cum centesimo septuagesimo secundo post transitum sancti Martini comparans… Quae computatio annum 569. efficit, qui sine dubio falsus est" (l.410–414, OCR read by line). Krusch: "In calculo sibi minime constat, nam 172 annos Mir. S. Mart. II, 1. computavit" (l.35416–35418). Gregory's own line gives both counts together: "Anno centesimo septuagesimo secundo post transitum beati Martini… Sigiberto gloriosissimo rege duodecimo anno regnante", with "573." in the margin (l.46663–46664). The records claim now quotes Arndt l.410–414 and Krusch, with the witness widened to match. The drafter's l.414 end point is right: "falsus est" sits on l.414. The brief did not change. |
| R2-B-M1 Leander card `uncertain` 3: attachment | RESOLVED | It now says "wrote two books against the heretics while in exile abroad". The source is "in exsilii sui peregrinatione composuit duos adversus haereticorum dogmata libros" (PL 83 l.122776–122778). |
| R2-B-M2 Leander brief close: pronoun | RESOLVED | It now says "Gregory once wrote to him of carrying "the image of thy countenance" stamped deep within his heart." The gerund takes the writer as its subject, so "his heart" is Gregory's. The quoted piece is verbatim: "I carry the image of thy countenance stamped within the bowels of my heart" (npnf212 l.32625–32626). "Deep" is the narrator's word and sits outside the quotation marks. The audio follows. |
| R2-B-M3 Reccared brief close: pronoun | RESOLVED | It now says "Isidore of Seville, Leander's brother, wrote that Leovigild was irreligious and quick to war, and his son pious in faith and famed for peace." This is 23 words, and "his son" now follows Leovigild, the subject. The source is "namque ille inreligiosus et bello promptissimus, hic fide pius et pace praeclarus" (mommsen1894 l.28264–28265, OCR). The paired contrast is whole again. |
| R2-B-M4 paragraph breaks | RESOLVED, with one side effect in Reccared (R3-B-M3) | Leander has new paragraphs at "Travellers from Spain told Gregory…" (l.7) and "Near death, Gregory the Great writes…" (l.9). Reccared has a new paragraph at "God stirred him, burning with faith…" (l.7). The words are unchanged, and both audio scripts match. In Leander, the break leaves l.5 to l.9 as three short paragraphs in a row. Each holds one matter, and their sentence lengths vary, so this is not a finding. In Reccared, the new paragraph opens on a pronoun whose antecedent is in the paragraph before (R3-B-M3). |
| R2-B-M5 Reccared records: "manu sua" | RESOLVED | The contested claim now gives both readings. The line numbers are right: "synodo intererat" is at l.20394, and "tonio scriptam manu sua epi- / scopis porrigens" (OCR) is at l.20395–20396 (mommsen1894). Claim 26 still quotes "tomo scriptam manu sua" in Latin under "handed the bishops", which takes no side. |
| R2-A-B1 as applied to part B (credit to Ludwig M. Hartmann) | PARTLY RESOLVED (R3-B-M1, R3-B-M2) | The title page has "POST PAVLI EWALDI OBITVM EDIDIT LVDOVICVS M. HARTMANN" (ewald-hartmann1893 l.136–139). The note speaks in the first person singular: "equidem credo" (l.15337, OCR). So the single credit is right. The swap from "Paul Ewald and Ludwig Hartmann… They" to "Hartmann… He" left two verbs plural ("think", "answer") and one pronoun unclear, in Reccared's card and records. Leander's card and records read cleanly. |

## 2. New findings in changed text

- **R3-B-M1 MINOR (`reccared.card.json` `uncertain` 7, last two sentences; the R2-A-B1 swap; items 4 and 9).** The card reads: "Ludwig M. Hartmann… reports that Gams judged it false and Mommsen agreed. He answers that the priest Probinus carried it, beyond doubt, and think it badly preserved and corrupt in many places." "He" follows "Mommsen agreed", so a reader can take Mommsen as the one who answers, which is the opposite of the dispute. "Think" is left over from the plural "They". This is participant-facing card text. Fix, with no change in claim (20 words): "Hartmann answers that the priest Probinus carried it, beyond doubt, and thinks it badly preserved and corrupt in many places." Source: "translata sine dubio per Probinum presbyterum" and "equidem credo et hanc ep. male adservatam multisque locis corruptam esse" (ewald-hartmann1893 l.15333, 15337, OCR).

- **R3-B-M2 MINOR (`records.json`, `reccared`; claims[32] and `contested_claims` "The letter in Reccared's name to Gregory"; the same swap).** Claim 32 reads "he holds it carried 'sine dubio' by the priest Probinus, and think it 'male adservatam…'". Fix: "and thinks it". The contested claim reads "Hartmann heads it 'translata sine dubio per Probinum presbyterum' (l.15333) and answer 'equidem credo…'". Fix: "and answers". Neither changes a claim.

- **R3-B-M3 MINOR (`reccared.brief.txt` l.7 and the audio; item 4, pronoun; a side effect of the R2-B-M4 break).** The new paragraph opens "God stirred him, burning with faith, to call back a people who served error under the name of religion." The paragraph before ends "It confesses Father, Son and Spirit as one substance." Before that, the last man named is Leander of Seville. On the page, the reader starts a new paragraph on "him" with nobody named, and "it says" does not come until the second sentence. Fix (+1 word, brief 396 words): "God stirred the king, burning with faith, to call back a people who served error under the name of religion." The source is "me quoque… calore fidei accensum in eo Dominus excitavit, ut… populum, qui sub nomine religionis famulabatur errori… revocarem" (collectio l.36672–36675). The audio follows the brief.

Observation, not a finding. In the Gregory card `dates`, "a count Arndt says does not agree" leaves "with what" to the reader, but the sentence before supplies it, and nothing in it is wrong. Similar wording could also be used: "a count Arndt says does not agree with that year".

The changed text adds no misquotation, witness swap, false absence, unsupported claim, dropped hedge or contested point told as settled. Every quote in the three briefs was re-checked at its line: bliss1844 l.387–388 and 452–454; gardner1911 l.8075–8076; npnf212 l.32625–32626; mommsen1894 l.28264–28265; brehaut1916 and dalton1927 as R2 cited, where nothing changed. Each common name in the changed text has its place or role at first mention. Dalton's authorship view stays given as Dalton's (Reccared l.5, card `uncertain` 2; dalton1927 l.29214).

## 3. Writing, read whole

- **Leander.** It reads as a story, from the Constantinople scene through the exile, the Hermenegild dispute, Toledo, the Rule and the dispute over his death year, to Gregory's line. It has no AI tells and no beat lines. The new close is natural. A bare "Gregory" always means Gregory the Great, and Gregory of Tours is always named in full, so the close is clear.
- **Reccared.** It reads well apart from R3-B-M3. The new close fixes the old "Leander's son" mishearing, and "his son" now follows cleanly.
- **Gregory of Tours.** The brief did not change in R2 and still reads as two scenes and a trial, told without tails.

## 4. Mechanical checks

- Audio: each script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in a brief or a card.
- No narrator sentence runs past 25 words. The longest are Reccared l.13 (23) and Reccared l.5 (22).
- The three cards and `records.json` parse. `records.json` holds the ten batch ids, each with `claims`, `contested_claims` and `absent_details`. The `briefLength` values fit: "about 2 minutes 30 seconds" for Leander and Reccared, "about 2 minutes" for Gregory.

| Profile | Words | FK | Flesch | Cap |
|---|---|---|---|---|
| Leander of Seville (major) | 404 | 7.6 | 62.5 | 405, within |
| Reccared (major) | 395 (396 with R3-B-M3) | 7.0 | 69.0 | 405, within |
| Gregory of Tours (recorder) | 324 | 5.0 | 78.7 | 325, within |

## Verdict

- **Leander of Seville: CLEAR.** R2-B-M1, M2 and M4 are resolved. No new finding.
- **Reccared: CLEAR.** R2-B-M3, M4 and M5 are resolved. Three new minor points do not block: R3-B-M1 (card pronoun and verb), R3-B-M2 (records verbs) and R3-B-M3 (paragraph-opening pronoun). Each is a one- or two-word fix with no change in claim.
- **Gregory of Tours: CLEAR.** R2-B-B1 is resolved against Arndt l.391–414 and Krusch l.35416–35418.

## Totals

R2 part B findings: 1 blocking and 5 minor. All 6 are RESOLVED. R2-A-B1 as applied to part B is PARTLY RESOLVED, through R3-B-M1 and R3-B-M2. New: 0 blocking and 3 minor (R3-B-M1 and R3-B-M3 for `reccared`, the card and the brief; R3-B-M2 for `reccared`, the records).

## Part C

Scope: round 3, the last allowed. Part C covers Venantius Fortunatus, Baudonivia (a recorder) and Dorotheus of Gaza, all standard length, with their cards, audio scripts and `records.json` entries in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch5/`. I checked them against `R2_recheck.md` (R2-C-M1 to R2-C-M6) and `R2_changes.md` (part C, and the lead's Venantius change logged at its top). I checked Dorotheus against the paired batch 3 profile `barsanuphius-and-john-of-gaza` (`Who-Profiles/era3/batch3/`).

I am a fresh reviewer. I did not draft or fix these files. I worked from the files as they stand, without git. I opened each changed sentence at its line in the vendored file and checked who speaks there. I read each brief whole, aloud in my head. I edited no profile file, and I made no git, model or web calls. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines, so paragraphs sit on l.1, 3, 5, 7, 9 and 11.

## 1. The R2 findings

| Finding | Status | Check against source |
|---|---|---|
| R2-C-M1 the Library's word "held" in participant text | RESOLVED | No "held" is left in the three briefs, audio scripts or cards (searched as a whole word). Venantius brief l.9 now reads "Dalton notes that Gregory never calls him bishop." Dalton: "Gregory never alludes to Fortunatus as bishop" (`gregory-tours_history-of-the-franks-v2_dalton1927.txt` l.26297-26298). Baudonivia brief l.3: "The sources give nothing of her family, age or death. This account rests on her book." The card wordings follow R2. `records.json` keeps "held", as the finding allows. The changed Venantius card wording in `uncertain` 1 adds a false quantifier; see R3-C-B1. |
| R2-C-M2 Venantius l.7, "says when" | RESOLVED | Now "says that when Radegund's house received a relic of the Cross, Fortunatus marked it with hymns." Dalton: "the arrival of which at Poitiers was celebrated by Fortunatus in several hymns" (dalton1927 l.27597-27598). It now reads cleanly aloud. |
| R2-C-M3 Baudonivia l.7, pronoun and number | RESOLVED | Now "Fortunatus first wrote it of Hilary raising Pascentius, then bishop of Poitiers. There, Krusch says, it means Hilary's monastery raised Pascentius." "It" now matches "One phrase", and "raised Pascentius" names him. Fortunatus to Pascentius: "qui te ab ipsis cunabulis ante sua vestigia quasi peculiarem vernulam familiariter enutrivit" (`venantius-fortunatus_opera-mgh-aa-4-lat_leo-krusch1881.txt` l.43008-43009). Krusch: "Erat quidem Pascentius S. Hilarii alumnus, neque vivi, sed monasterii" (l.41121-41122). Pascentius as bishop: "Pascentio Pictanensi [OCR] episcopo misit" (l.41118). Her own phrase: "quam ab ipsis cunabulis ante sua vestigia peculiarem vernulam familiariter enutrivit" (`fredegar-…-mgh-srm-2-lat_krusch1888.txt` l.29449-29450). One new ambiguity in "then bishop of Poitiers"; see R3-C-M1. |
| R2-C-M4 Dorotheus l.9, both sides of the monastery dispute | RESOLVED | l.9 adds "The scholar François Nau instead makes him a later head of Seridus's monastery." Nau: "le monastére dont les hégouménes successifs ont été, au vi siecle, Barsanuphios, Séridos et enfin Dorothée" (`po08_…_1912.txt` l.11423-11424). The other side, the Synaxaristes, reads (OCR) "ὕστερον δὲ συστησάμενος μοναστήριον ἴδιον, μετὰ τὴν τελευτὴν τοῦ Ἀββᾶ Ἰωάννου τοῦ καλουμένου προφήτου" (`nikodemos-hagiorite_…_1900.txt` l.37916-37919). The paragraph is no longer a single line. The l.3 trim holds: "sub finen [OCR] seculi vı floruisse nostrum archimandritam arguunt Bollandiani" (`dorotheus-gaza_…_migne-pg88.txt` l.121960-121962) supports "late in the sixth century", and the unknown death year (l.121969-121970) stays on the card's `dates`. Dropping "which Migne reprints" leaves Gallandi with no context; see R3-C-M3. |
| R2-C-M5 Venantius, the subject's first mention | RESOLVED | l.1 opens "Venantius Fortunatus and his friend Felix of Treviso". Paul names Felix "the bishop of the church of Tarvisium (Treviso)" (`paul-the-deacon_…_foulke1907.txt` l.4050). l.3 now reads "Fortunatus was a poet from northern Italy." |
| R2-C-M6 Dorotheus card `uncertain` 3, "his abbot John" | RESOLVED | Now "Dorotheus calls the abbot John the disciple of blessed Barsanuphius". Dorotheus was "apud abbatem Seridum", and the abbot ordered him to serve John (migne-pg88 l.126276-126278). Dorotheus: "Memini me quandoque abbatem Joannem beati Barsanuplii [OCR] discipulum interrogasse" (l.124094-124096). |
| Lead's change, Venantius l.9 | RESOLVED, and it reads clearly | "Dalton notes that Gregory never calls him bishop. Dalton thinks Fortunatus became bishop only after Gregory died." Dalton: "Gregory never alludes to Fortunatus as bishop, because the latter was only consecrated to the see of Poitiers after his death (cf. Introduction, p. 83 n. i)" (dalton1927 l.26297-26299). The thinker is now plain. "Thinks" rightly marks as Dalton's view what he states as fact on the strength of an Introduction that is not among the sources used here, and the records tag it Dominant Modern Reconstruction. Read aloud, the paragraph is four short sentences with "bishop" in each and "Dalton" twice in a row. It is plain and correct, and the repetition is what keeps the witness clear, so I raise no finding on it. |

## 2. New findings in changed text

- **R3-C-B1 BLOCKING (Venantius card `uncertain` 1; `records.json` claim and contested side; item 1; a false quantifier from the R2-C-M1 rewording).** The card says: "Gregory of Tours calls him a priest each time he names him." That is not true. In the prologue to Virt. Mart. I, Gregory names him with no title: "Utinam Severus aut Paulinus viverent, aut certe Fortunatus adesset, qui ista discriberent!" (`gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt` l.45002-45003). The card's own `legacy.remembered` 2 gives that passage ("wishes that Fortunatus were there to write them"), and the profile's own records quote it, so the card contradicts itself. The R1 form, "in every held mention", had the same fault. Dalton is the witness for "never bishop", not for "always priest" (dalton1927 l.26297-26298). The point the item makes, that Gregory never calls him bishop, stands. Only the quantifier is wrong.
  - Card fix: "Gregory of Tours calls him a priest and never bishop." (10 words for 10). Witnesses: "Fortunatus presbiter" (Virt. Mart. I.2, arndt-krusch1885 l.45245); "venerabilem conservum meum Fortunatum presbiterum" (I.13, as Leo quotes it, leo-krusch1881 l.51804-51806); "the priest Fortunatus" (HF, dalton1927 l.8393-8394); Dalton for "never" (l.26297-26298).
  - Records fix, the claim: "Gregory calls him presbyter in HF V.8 ('the book of his Life composed by the priest Fortunatus'), Virt. Mart. I.2 and I.13, and Gl. Conf. ('a Fortunato presbytero conscriptam'), and never bishop; the prologue to Virt. Mart. I names him with no title ('aut certe Fortunatus adesset', gregory-tours arndt-krusch1885 l.45003)". Keep its witness line.
  - Records fix, contested side 2 of "Whether and when he was bishop of Poitiers": open with "Gregory of Tours calls him presbyter and never bishop (…)" in place of "Gregory of Tours calls him presbyter in each held mention (…)".
  - The brief does not carry the fault: l.9 says only "Gregory never calls him bishop".

- **R3-C-M1 MINOR (Baudonivia brief l.7; item 4, pronouns clear; from the R2-C-M3 fix).** "Fortunatus first wrote it of Hilary raising Pascentius, then bishop of Poitiers." Heard aloud, "then bishop of Poitiers" can attach to Hilary. Hilary of Poitiers is the famous bishop of Poitiers, and he is named that way two sentences earlier. A listener can take the line to mean Hilary raised Pascentius while Hilary was bishop. That is the literal reading Krusch says is an error ("quidam conieceruut [OCR], sed erraverunt", leo-krusch1881 l.41121). Fix: "Fortunatus first wrote it of Bishop Pascentius of Poitiers, as raised by Hilary." (13 words for 12). The next sentence stays as it is: "There, Krusch says, it means Hilary's monastery raised Pascentius." Scored: 325 words, FK 7.3, Flesch 66.0.

- **R3-C-M2 MINOR (Dorotheus brief l.1; item 8, the first mention of a common name; agreement with batch 3).** The brief first names John as "the abbot John" (l.1). John is a name that could mean many people, and the pattern wants a place at first mention. The paired batch 3 brief gives "the abbot John of Gaza". The vendored source gives the place: the Synaxaristes puts Barsanuphius and "Ἰωάννης ὁ μαθητὴς αὐτοῦ" in Seridus's community "τοῦ πλησίον τῆς Γάζης" (nikodemos l.37908-37911, OCR). The role "disciple of blessed Barsanuphius" comes only at l.3. Fix: "While Dorotheus of Gaza lived with the abbot Seridus, the attendant of the abbot John of Gaza fell sick." (+3). To hold length, l.3: "He tells this in his Teachings, printed by J.-P. Migne." becomes "He tells this in his Teachings." The card's `sources.ownWords` keeps Migne's edition. With R3-C-M3, scored: 325 words, FK 7.2, Flesch 67.0.

- **R3-C-M3 MINOR (Dorotheus brief l.3; items 4 and 8, a name with no context; from the R2-C-M4 trim).** "Andrea Gallandi's notice calls Dorotheus a Palestinian archimandrite". Once ", which Migne reprints," was cut, nothing tells a listener who Gallandi is or what his "notice" is. Gallandi is the brief's main modern witness (l.3 twice, l.11), and he comes before Nau, who now has "The scholar". The other two briefs place Krusch as "The German scholar". Fix: "The scholar Andrea Gallandi calls Dorotheus a Palestinian archimandrite, the head of a monastery." (+1, offset in R3-C-M2). The claim is his own notice: "Dorotheus archimandrita Palestinus" (migne-pg88 l.121957). The card keeps "Notice on Dorotheus" in `sources.about`.

Other checks on the changed text. I found no other misquotation, witness swap, false absence, dropped hedge, or contested point told as settled. Baudonivia l.3, "The sources give nothing of her family, age or death", is a true absence. The unsigned PL 72 note's "Baudonivia Fortunato aequalis" makes her his contemporary and says nothing of her age, and her `absent_details` record the search. The Venantius l.7 Dalton sentence, the Baudonivia l.7 Krusch sentences and the Dorotheus l.3 and l.9 sentences each match their lines.

## 3. Dorotheus and the batch 3 Barsanuphius and John profile

The two profiles agree on every shared point. Both make John Dorotheus's teacher and the disciple of Barsanuphius. Both give the epithet "the Prophet" to the heading of the Questions and to Gallandi. Both say, through Gallandi, that the Life of Dositheus has Dorotheus meet the two old men when he entered Seridus's monastery. Both give Nau's heads in turn (Barsanuphius, Seridus, Dorotheus), his Thabatha, and his birth "about 540". Both give Migne's 596 heading over Gallandi's notice, and the Bollandists' end of the sixth century, which this brief gives as "late in the sixth century" for Gallandi's "sub finem seculi vi". Both give the anonymous preface's two Barsanuphii and two Dorothei, Theodore the Studite's separating out the condemned men, and Hilarion of Verona's Latin as revised by Fronto Ducaeus. The new l.9 sentence matches batch 3's card `uncertain` 3. The only difference is the name form for John, which R3-C-M2 brings into line. The Synaxaristes' "his own monastery" side appears only in this profile, and it does not contradict batch 3.

## 4. Writing, read whole

**Venantius Fortunatus.** The brief opens on the healing at Ravenna, and the full name now comes first. It moves through Tours, Poitiers, Radegund and Agnes, the verse and hymns, and the bishopric dispute, and closes on Paul's epitaph. The R2 changes read cleanly aloud. I heard no AI tells, beat lines, aphorisms or "not X but Y" turns. The longest sentence is l.5 at 25 words, unchanged.

**Baudonivia.** The burial scene on the wall comes first, then the caveat, her purpose, the copied prologue, the Cross with Gregory's other account, and the death in the voice of the whole house. The two-sentence caveat in l.3 is plain and in place. The only flow fault is the attachment in R3-C-M1.

**Dorotheus of Gaza.** The service to John comes first, then the Teachings and the Bollandist time, Dositheus, the noble of Gaza, the monastery dispute with both sides, and Gallandi's judgment. With the second sentence added, l.9 tells the dispute in place. The faults are the two missing identifiers (R3-C-M2, R3-C-M3).

## 5. Mechanical checks

- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag is in a brief or card.
- `records.json` loads and holds all three ids. The three cards parse as JSON. The records cover the brief's facts, including the Nau side of "Which monastery Dorotheus headed" and the Dalton and Luchi side of the bishopric.
- An observation, not a finding: in the Dorotheus entry, two `contested_claims` give `sides` as one string and the third as a list. The batch mixes both forms, and batch 3 uses strings throughout. No field is missing.

| Profile | Words (cap 325) | Est. @162 | FK | Flesch | Longest sentence |
|---|---|---|---|---|---|
| Venantius Fortunatus | 325 | 2:00 | 6.1 | 72.5 | 25 (l.5, unchanged) |
| Baudonivia | 324 | 2:00 | 7.3 | 65.9 | under 25 |
| Dorotheus of Gaza | 324 | 2:00 | 6.8 | 68.0 | under 25 |

The R2_changes table gives Venantius 324 words. After the lead's l.9 change the brief is 325, which is still at the cap. With every fix above applied, Baudonivia is 325 (FK 7.3, Flesch 66.0) and Dorotheus is 325 (FK 7.2, Flesch 67.0). Venantius is unchanged, since R3-C-B1 touches only the card and the records. `briefLength` "about 2 minutes" fits all three.

## Verdict

- **Venantius Fortunatus: NOT CLEAR.** One blocking point, R3-C-B1: the card and the records say Gregory calls him a priest each time he names him, and Gregory's own prologue to Virt. Mart. I (l.45003) disproves it. The fix is one card sentence and two records strings, worded above. The brief itself is clear.
- **Baudonivia: CLEAR.** One minor point (R3-C-M1).
- **Dorotheus of Gaza: CLEAR.** Two minor points (R3-C-M2, R3-C-M3). It agrees with the batch 3 Barsanuphius and John profile.

## Totals

R2 findings: R2-C-M1 to R2-C-M6, 6 of 6 RESOLVED, and the lead's Venantius l.9 change RESOLVED. None is PARTLY or NOT RESOLVED.

| Profile | Blocking | Minor |
|---|---|---|
| Venantius Fortunatus | 1 (R3-C-B1) | 0 |
| Baudonivia | 0 | 1 (R3-C-M1) |
| Dorotheus of Gaza | 0 | 2 (R3-C-M2, R3-C-M3) |
| **Part C** | **1** | **3** |

