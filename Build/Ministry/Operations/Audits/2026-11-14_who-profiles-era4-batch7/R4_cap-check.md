# R4 cap check: era 4 batch 7

## Scope

One targeted check, under Mark's standing ruling of 2026-11-14 (Decision-Log, "Minor round 3 fixes to reader-facing text get one targeted check without asking Mark"). It does not count toward the three-round cap. It covers only the strings changed in commit cb4cbec5 under `Who-Profiles/era4/batch7/`:

1. Symeon the New Theologian, card `legacy.remembered` item 2 (index 1): the Calecas sentence split in two (R3-M1).
2. Niketas Stethatos, card `legacy.traces` item 2 (index 1): the skete sentence split in two (R3-M2).
3. `records.json`, Niketas, the claim "A monk in a skete on Athos ...": its `witness` lines (R3-M3).
4. README, third paragraph: the word counts and times (R3-M4).

Reviewer: independent Opus, first sight of these files and of the drafting. I edited no profile file, made no git writes and made no web, paid or model calls. I used local reads, read-only git and local scripts only.

## Method

- I read R3-M1 to R3-M4 and their fix text in `R3_recheck.md`, then `git diff HEAD~1 HEAD --stat`, `git diff HEAD~1 HEAD -- Build/Ministry/Features` and the same with `--word-diff`.
- I opened the vendored files myself and read the cited passages in context, with line numbers from `awk`/`grep -n`:
  - PG152 (`calecas_opera-omnia-pg152-grc-lat_migne1866.txt`): the header, the ELENCHUS entry at l.304, the running heads l.28037-29536, and l.29280-29345, Greek and Latin. OCR noise was read through.
  - PAISIUS (`paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt`): l.10150-10230 and l.10480-10500.
- For items 1 and 2 I checked what the source says, the witness, pronoun reference, sentence length, AI tells and spelling.
- By script: `json.load` on all seven cards and `records.json`; words per sentence in the two changed card strings; words in each `<id>.brief.txt` by whitespace split and by `wc -w`, and time at 162 words a minute.

## 1. Symeon, card `legacy.remembered` 2: PASS

String: "Michel Le Quien calls him the parent of the Palamite error. Combefis writes that he is wrongly counted a source of the Palamites, who twisted his words. Manuel Calecas, a Dominican, wrote against the Palamites. In a note, Combefis reads the deluded monks that Calecas attacks as Symeon and his disciples." (11, 16, 8 and 16 words.)

- The change is the R3-M1 fix, word for word. Only the third and fourth sentences changed.
- "a Dominican": the PG152 header reads "Manuelis Calecae ordinis Fratrum Praedicatorum". Holds.
- "wrote against the Palamites": the volume's content note lists his De essentia et operatione among the anti-Palamite works. The passage itself attacks those who hold that one sees "φῶς ἄκτιστον ... μήτε οὐσίαν Θεοῦ, μήτε ὑπόστασιν, ἀλλ᾽ ἐνέργειαν" (l.29295-29297), the Palamite teaching. Holds.
- The note is Combefis's: the ELENCHUS gives "De essentia et operatione, editore et interprete Francisco Combefisio" (l.304), and the passage sits inside that work (running heads "DE ESSENTIA ET OPERATIONE" at l.29181 and l.29536, "MANUELIS CALECAE" at l.29327).
- "the deluded monks that Calecas attacks": "ἔκ τινων μοναχῶν, ἀρετὴν ὑποκρινομένων, ἀλόγων καὶ πεπλανημένων (10)" (l.29298-29299); the Latin "quorumdam monachorum, virtutem simulantium (rudium scilicet hominum ac seductorum)" (l.29337-29339).
- "reads ... as Symeon and his disciples": the note "Ἀλόγων καὶ πεπλανημένων. Symeonem notat ejusque discipulos" (l.29302-29303). Holds, with Combefis as the witness.
- Reference: the appositive is gone from between subject and verb. "Calecas" is named again, so nothing is left for a pronoun to catch. "his disciples" can only be Symeon's.
- Writing: every sentence is 16 words or fewer. American spelling. No contrast frame, triad, colon reveal, tail or hedge filler. The short third sentence introduces Calecas before he is used, as CLAUDE.md asks of a new name.

## 2. Niketas, card `legacy.traces` 2: PASS

String: "Paisius Velichkovsky translated his three hundred chapters into Slavonic. A monk in a skete on Athos told him the skete held only twenty-two in Greek. Paisius says the older Slavonic had only parts of the three hundreds." (9, 16 and 12 words.)

- The change is the R3-M2 fix, word for word: ", and" became a full stop.
- "translated his three hundred chapters": "вновь преведохъ сія: Святаго Марка, и Святаго Никиты Стифата триста главъ" (l.10487-10488).
- The skete on Athos: Paisius goes from the Lavra toward the skete of Saint Anna, below the hill of the Prophet Elijah, "третія часть ... святаго Аѳона", where "обрѣтается единъ скитъ Святаго Василія Великаго" (l.10166-10173). The monk is met in that skete (l.10184-10185).
- "only twenty-two in Greek": "Святаго же Никиты Стифата точно двадесять и двѣ главы, а цѣлая въ насъ, рече, не обрѣтается" (l.10217-10218). Paisius is seeking the books "на эллиногречестѣмъ языцѣ" (l.10161-10162), and the monk says they are written "самымъ чистымъ эллиногреческимъ языкомъ" (l.10225-10226). Holds.
- "the older Slavonic had only parts of the three hundreds": "отъ древнихъ временъ на словенскій языкъ преведенныя части нѣкоторыя тріехъ сотницъ бяху", and he had never seen the whole book with all three hundred (l.10488-10492). Paisius owns it ("Paisius says"). Holds.
- Reference: "him" in the second sentence follows "Paisius Velichkovsky", the first sentence's subject; "his" there is Niketas, the card's subject, dead seven centuries before, so no reader takes "told him" as Niketas. The third sentence names Paisius again.
- Writing: all three sentences are 16 words or fewer. American spelling. No AI tell. The two claims from two places in Paisius now stand in two sentences.

## 3. `records.json`, Niketas skete claim, witness: FAIL (MINOR, records only)

Witness now: "PAISIUS (paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt) l.10159-10160, 10172-10177, 10216-10218, 10224-10225, 10487-10494".

The commit applies the R3-M3 fix as worded. Three of its ranges hold. Two point to the wrong lines in the file as vendored, and the place on Athos and the monk are outside every range:

- l.10159-10160 read "ими же вѣсть судьбами ... сподобитъ мене обрѣсти таковыя книги". They do not say Greek. The Greek is at l.10161-10162: "о стяжаніи книгъ отеческихъ на зллиногречестѣмъ [эллиногречестѣмъ] языцѣ".
- l.10224 is the monk's "по мнѣнію моему вина" with no language named. The Greek is at l.10225-10226: "самымъ чистым г, эллішогреческимъ [эллиногреческимъ] / языкомъ суть написаны".
- l.10172-10177 places the skete of Saint Basil; Athos is named at l.10170-10171, and the monk is met in the skete at l.10184-10185. The claim says "A monk in a skete on Athos".
- l.10216-10218 (the twenty-two chapters) and l.10487-10494 (the older Slavonic, the translation) hold.

The claim text and its `formation_confidence` (Documented) are right. Only the line numbers are wrong. No participant text is affected.

## 4. README word counts: PASS

Counted by whitespace split (the batch's counter) and by `wc -w`; time at 162 words a minute:

| Brief | Split | `wc -w` | Time |
|---|---|---|---|
| symeon-the-new-theologian | 404 | 404 | 2:30 |
| niketas-stethatos | 354 | 354 | 2:11 |
| paul-the-deacon | 365 | 365 | 2:15 |
| paulus-emeritanus | 348 | 348 | 2:09 |
| cedd-and-chad | 392 | 392 | 2:25 |
| elipandus-of-toledo-and-felix-of-urgell | 399 | 399 | 2:28 |
| pisentius-of-coptos-and-john-the-elder | 400 | 398 | 2:28 (2:27 at 398) |

- "His brief runs 404 words, about 2:30." Holds.
- "Niketas Stethatos, Paul the Deacon and Paulus Emeritanus run 348 to 365 words, about 2:09 to 2:15." Holds (348, 354, 365).
- "The three paired profiles run 392 to 400 words, about 2:25 to 2:28". Holds on the batch's counter (392, 399, 400).

Considered, and not a finding: Pisentius is 400 by whitespace split and 398 by `wc -w`. The two extra tokens are the two spaced dashes inside Budge's closing quotation ("whatsoever thou givest — everything — to the poor"). R3 noted this. The README follows the batch's own counter, as `R2_changes.md` does, and "about 2:28" holds on either count.

## Commit scope and JSON

- `git diff HEAD~1 HEAD --stat`: the Symeon card, the Niketas card, `records.json` and the README, one line each, plus `R3_changes.md` and `R3_recheck.md` under `Build/Ministry/Operations/Audits/`. The last two are the round 3 audit trail, not participant text.
- The word-diff shows only the four strings above under `Build/Ministry/Features`. No brief, no audio file and no other card field changed. Nothing else in participant text changed.
- All seven cards and `records.json` load with `json.load`. `records.json` holds exactly the seven ids. PASS.

## Findings

- **R4-M1 MINOR (`records.json`, `niketas-stethatos`, the claim "A monk in a skete on Athos: only twenty-two chapters in Greek in his skete; older Slavonic held parts; Paisius translated the three hundred"; records only; witness lines off).** Two ranges miss their text by one or two lines, and the Athos and monk lines are not covered (section 3).
  - Fix, `witness`: "PAISIUS (paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt) l.10159-10160, 10172-10177, 10216-10218, 10224-10225, 10487-10494" -> "PAISIUS (paisius-velichkovsky_zhitie-i-pisaniia-chu_optina1847.txt) l.10161-10162, 10170-10177, 10184-10185, 10216-10218, 10225-10226, 10487-10494".
  - This is a records-only line-number fix and changes no claim or reader-facing text. Once applied, confirming it needs only `sed -n` on the six ranges and a `json.load`. It needs no further review round.

No BLOCKING finding. No finding on participant text.

## Verdict

NOT CLEAR, on item 3 alone, and only until R4-M1 is applied.

- Items 1, 2 and 4 are CLEAR. R3-M1 and R3-M2 are applied word for word. They hold against PG152 l.304, l.29295-29303 and l.29337-29339, and against PAISIUS l.10161-10162, 10166-10173, 10184-10185, 10217-10218, 10225-10226 and 10487-10492. Each sentence is 16 words or fewer, and every pronoun resolves. The README counts match the briefs.
- Item 3: the R3-M3 witness as worded cites l.10159-10160 and l.10224-10225 for the Greek, which is at l.10161-10162 and l.10225-10226. It leaves Athos and the monk uncited. Apply R4-M1 as worded and confirm the ranges mechanically. With that done, the batch is CLEAR.
- Nothing in this batch closes until Phase Five boundary testing and full-system review are complete.
