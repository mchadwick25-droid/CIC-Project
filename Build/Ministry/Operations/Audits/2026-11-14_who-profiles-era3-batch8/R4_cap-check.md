# R4 cap check: era 3 Who batch 8, round 3 fixes (Mark's cap ruling, 2026-11-14)

## Scope

One targeted check, ordered in Mark's cap ruling ("One check each", 2026-11-14). It does not count toward the three-round cap. It covers the round 3 fixes only:

1. Brendan of Clonfert, R3-B-B1: John Williams ab Ithel named as the editor of the Annales Cambriae.
2. The round 3 minor fixes: R3-A-M1 to M8 and R3-B-M1 to M6. That is fourteen minors; with R3-B-B1 they make the fifteen fixes of round 3. Each was checked against its source lines and the writing rules.
3. The three brief changes (John Climacus: R3-A-M1 and R3-A-M3; Liberatus of Carthage: R3-A-M4), their audio scripts and their scores.
4. That nothing outside the listed fixes changed.

Reviewer: independent Opus, first sight of these files. I edited no profile file, made no git writes and made no web, paid or model calls. I used local scripts and read-only git only. The inputs were R3_recheck.md, R3_changes.md and `git diff 8ed620fc 0411d04c` (plain and `--word-diff`) on the batch 8 folder.

## Method

- I opened every cited line in the vendored file myself and compared it with the changed string. The scans' double spaces were read as single spaces, and OCR noise was read through.
- For each changed string I checked pronoun reference, witness, hedge, sentence length (word count by script), fragments and AI tells.
- An audio script was rebuilt by script from its brief (`[calmly] ` at the start, `[warmly] ` before the last paragraph) and compared byte for byte.
- `grade_text` was run from the repo root on the two changed briefs.
- `git diff --stat 8ed620fc 0411d04c` over the whole repo, and every hunk in the batch 8 folder, were matched against the list of fixes.

## 1. Brendan of Clonfert, R3-B-B1 (card `uncertain` 4): PASS

String: 'The Annales Cambriae record only the death of a Brendan "Byror", whom John Williams ab Ithel, who edited them, takes for Brendan of Birr.' (24 words.)

- Editor: `annales-cambriae-rolls-series-20-lat_williams-ab-ithel1860.txt` l.257-263, "EDITED / BY / THE REV. JOHN WILLIAMS AB ITHEL, M.A.". "Who edited them" holds.
- Identification: preface l.892-893, "the death of Brenda, / abbot of Birre (p. 5)". Entry: l.2501, "cxxx. Annus. Brendan ^ Byror dormitatio." "Takes for Brendan of Birr" holds and is marked as his.
- The role no longer stands in for the witness (checklist item 5). The card's source title, "Annales Cambriae (ed. John Williams ab Ithel)", agrees.
- Writing: two relative clauses in a row ("whom ... who edited them ...") make the sentence a little heavy, but it is clear and under 25 words. Not a finding.

## 2. The minor fixes

| Fix | Where | Source lines | Verdict |
|---|---|---|---|
| R3-A-M1 | Climacus brief P6 and audio: "Gregory's English translator, James Barmby, takes this John to be Climacus, still alive then." (14) | npnf213 l.397 "REV. James Barmby"; l.408 "Barmby (James), D.D., Gregory the Great"; l.5356-5357 the note on "Gregory to John, Abbot of Mount Sina": "No doubt the John called *Climacus*" | PASS. "Gregory's" removes the pointer to John. |
| R3-A-M2 | Climacus card `legacy.remembered` 0: 'Ketel "expounded therefrom sentiments full of spiritual truth", Thomas says, so that wise men marveled at how well he understood the book.' (22) | kempis arthur1905 l.12188-12191: "and expounded therefrom / sentiments full of spiritual truth, so that wise men / marvelled that he had so good an understanding / of the book." | PASS. The quoted words are verbatim. The witness is back. "Marveled" is American spelling in the narrator's words, outside the quote. |
| R3-A-M3 | Climacus brief P7 and audio: '"Sometimes he read the book of John Climacus", Thomas writes.' (10) | kempis l.12186-12187: "Sometimes he read the book of John Climacusr / " On perfect renunciation ..." ("Climacusr" is OCR; no comma follows) | PASS. See part 3. |
| R3-A-M4 | Liberatus brief P5 and audio: "...to be this exile, which Liberatus shared until his bishop died." (18) | PL68 l.75566-75574: "Qua nempe Reparato Carthaginensi episcopo, cujus erat diaconus, fidum se comitem, vel in exsilio, ita dedit, ut non nisi post episcopi mortem ab Euchayda recesserit" (OCR read through) | PASS. The claim stays inside "Garnier takes". See part 3. |
| R3-A-M5 | Liberatus card `uncertain` 2: "Garnier says the envoys named in Agapetus's letter left Africa only after Pope John had died." (16) | PL68 l.81391-81396: "missus est Romam Liberatus Diaconus, cum episcopis duobus Caio et Petro ... non nisi tamen post obitum Joannis ... legati solverunt ex Africa" | PASS. "Only after" renders "non nisi ... post". The witness is named. |
| R3-A-M6 | Liberatus card `dates`: "Theodor Mommsen dates the Breviarium between 555 and 567, since it tells of the death of Pope Vigilius. He adds that Liberatus wrote while Theodosius, once bishop of Alexandria, and Apollinaris of Alexandria were alive." (18, 17) | mommsen1894 l.17568-17571: "inter annos 555 (nam meminit mortis Vigilii c. 20) et 567 (nam scripsit, ut ait c. 20, vivo Theodosio episcopo quondam Alexandreae ... item ... vivo Apollinare successore eius in ea sede mortuo a. 569)" | PASS. The first "nam" is now a stated reason. "He adds" keeps the second ground with Mommsen. It does not say that this ground sets the 567 end, but nothing in it is wrong. Not a finding. |
| R3-A-M7 | Dionysius card `uncertain` 1: "Duchesne says Dionysius drew it from the letter of Proterius of Alexandria to Pope Leo." (15) | Duchesne LP1 l.16343-16345: "c'est Denys qui l'a déduite, par une exégèse habile, de la lettre de Proterius d'Alexandrie au pape saint Léon sur la question pascale (Krusch, l. c. p. 107)" | PASS. The charge is now Duchesne's by name. "With Krusch, he calls it ..." now reads as Duchesne. |
| R3-A-M8 | Dionysius card `legacy.traces` 1: "Abbot Ceolfrid wrote a letter that Bede gives in his Ecclesiastical History. In it he says that after Cyril of Alexandria, Dionysius added as many cycles again, reaching down to Ceolfrid's own time." (12, 21) | plummer1896 l.28820-28825: "misit illi et litteras scriptas in hunc modum: ... Ceolfrid abbas in Domino salutem"; l.29185-29188: "Cyrillus seriem XC et V annorum in quinque decennovenalibus circulis conprehendit; post quem Dionysius Exiguus totidem alios ex ordine pari schemate subnexuit, qui ad nostra usque tempora pertingebant" | PASS. The garden path is gone. "He" follows Ceolfrid, the subject before. |
| R3-B-M1 | Martin card `knownFor`: "Martin led the Second Council of Braga and wrote a sermon against the pagan customs of country people." (18) | The card's own `dates` and the council acts it cites (unchanged); the fix only replaces "He" | PASS. The pointer to Isidore is gone. |
| R3-B-M2 | Martin card `uncertain` 2: "Many, Krusch says, have guessed that Chararic and Theudemir were one man." (12) | arndt-krusch1885 l.45634-45636: "unde plerique Chararicum eundem ac Theudemirum fuisse coniecerunt" | PASS. "Guessed" keeps "coniecerunt", and Krusch owns it. |
| R3-B-M3 | Brendan `records.json`: contested side 3 now "Book of Lismore story: 'Brenainn maccu Altai was in Clonfert' (stokes lismore1890 l.878-881)"; new plain claim "Bollandist note: Cluain ferta founded by S. Brandano; says nothing of Adomnan's Brendan Mocu Alti" | stokes lismore1890 l.880-881: "Once when Brenainn maccu Altai was in / Clonfert"; acta-sanctorum augusti-1 l.58936-58939: "Cluain ferta coenobium duplex ... hoc a S. Brandano conditum, in sedem exinde crevit episcopalem, vulgo Cleiefart" | PASS. The quote is verbatim. The note says nothing of Adomnan. The OCR flags ('ttnditum', 'Cleiefart') are given. `records.json` loads as JSON. |
| R3-B-M4 | Barhadbeshabba card `uncertain` 4: "For that, Nau says, it is enough to suppose he wrote the History young and the Cause in old age." (20) | po09 l.31601-31606: "Il suffit de supposer qu'il a écrit « l'Histoire des saints Pères » dans sa jeunesse ... et qu'il a prononcé ou écrit le discours sur la Cause ... dans sa vieillesse" | PASS. Nau's supposition is kept as his. "For that" points back to "not impossible that this man is also the bishop of Halwan". |
| R3-B-M5 | Barhadbeshabba card `uncertain` 9: "They say Sabrisho of Lashom, head of the church, wanted him as his successor." (14) | scher1919 l.29179-29181: "choisir un successeur à Mar Sabrisoʿ. Celui-ci avait recommandé aux fidèles de choisir Barhadbsabba le moine"; gismondi1899 l.13591-13592: "Mar Sabarjesus mandavisset in patriarcham assumi Barhadbsabba monachum" | PASS. "They" can only be the Chronicle of Seert and Mari, named in the sentence before. |
| R3-B-M6 | Theopistus card `legacy.traces` 2: "A Coptic sermon in praise of Macarius, bishop of Tkow, says in its heading that Dioscorus spoke it in exile." (20) | nau1903 l.795-801: "Voici maintenant le commencement du panégyrique copte ... Eloge que prononça ... le saint Dioscore. Il le prononça sur l'abbé Macaire, l'évêque de la ville de Tkoou, du temps que le roi Marcien l'avait exilé à Gangres" | PASS. The claim is now owned by the sermon's heading, which Nau prints as its opening. |

Writing, across all fifteen changed strings: no fragment, no loose pronoun, no AI tell, no contrast or colon reveal, no tail. The longest is 24 words (R3-B-B1).

## 3. The brief changes, audio and scores

| Profile | Change | Audio = brief + tags | Words | Time at 162 | FK | Flesch |
|---|---|---|---|---|---|---|
| john-climacus (major, cap about 405) | R3-A-M1, R3-A-M3 | yes (1 `[calmly]`, 1 `[warmly]`) | 405 | 2:30 | 6.6 | 75.6 |
| liberatus-of-carthage | R3-A-M4 | yes (1 `[calmly]`, 1 `[warmly]`) | 325 | 2:00 | 8.5 | 60.1 |

- **Thomas à Kempis punctuation (R3-A-M3): PASS.** The source runs "Sometimes he read the book of John Climacusr" straight into the title, with no comma (l.12186-12187). The brief's quotation marks close on "Climacus" and the comma sits outside them, so nothing inside the marks differs from the source but the OCR "r". The card quotes the same words the same way.
- **"Gregory's English translator" (R3-A-M1): PASS**, as in part 2.
- **"which Liberatus shared" (R3-A-M4): PASS**, as in part 2. Liberatus's Flesch, 60.1, sits just above the floor. Any later change to this brief must be scored again.
- Both audio scripts equal their brief, with `[calmly] ` at the start and `[warmly] ` before the closing paragraph, byte for byte.
- Process note, not a finding: R3_changes gives 404 words for Climacus. A whitespace split gives 405, the same as R3_recheck. Both are within the cap.

## 4. Nothing else changed: PASS

`git diff --stat 8ed620fc 0411d04c` touches only the batch 8 folder and the two new audit files (R3_recheck.md, R3_changes.md). Every hunk in the batch 8 folder is one of the listed fixes:

- Climacus: brief and audio (M1, M3), card (M2).
- Liberatus: brief and audio (M4), card `dates` (M6) and `uncertain` 2 (M5).
- Dionysius: card (M7, M8).
- Martin: card (M1, M2).
- Brendan: card (B1) and `records.json` (M3).
- Barhadbeshabba: card (M4, M5).
- Theopistus: card (M6).

No other string in any card, brief, audio script or record changed.

## Findings

None. No BLOCKING or MINOR finding.

## Verdict

CLEAR.

- R3-B-B1 is resolved. John Williams ab Ithel is named as the editor and as the owner of the Birr identification (l.257-263, 892-893, 2501).
- All fourteen minors say what their source lines say, no more. Each has its witness, and each meets the writing rules.
- Both changed briefs pass `grade_text` (Climacus FK 6.6, Flesch 75.6, 405 words; Liberatus FK 8.5, Flesch 60.1). Their audio scripts match.
- Nothing outside the listed fixes changed.
