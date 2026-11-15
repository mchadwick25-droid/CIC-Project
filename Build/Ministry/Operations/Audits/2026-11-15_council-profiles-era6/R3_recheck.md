# Round 3 recheck: era 6 council profiles (2026-11-15)

The last allowed round. Two fresh Opus reviewers at full effort, one per council, neither of whom had seen the drafting or the earlier fixing. Targeted recheck of the changes from `e3021cfc` to `3c9deb30` against round 2. Part A: 0 blocking, 0 substantial, 2 minor (PASS). Part B: 1 blocking, 1 substantial, 2 minor (REVISE); B3-B1 and B3-S1 go to Mark for a cap ruling.

## Council profiles, era 6, round 3: Part A (Council of Constance 1414)

**Council.** `council-of-constance-1414`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/council-of-constance-1414.brief.txt`, `audio/council-of-constance-1414.audio.txt`, `council-of-constance-1414.entry.json`, and `records.json` key `council-of-constance-1414`. The scope is `git diff e3021cfc HEAD` on `claude/cft-councils-era6`, checked against `R2_recheck.md` Part A and `R2_changes.md` Part A.
**Brief.** 400 words (2:30 at 160 wpm, at the cap). `grade_text`: FK 6.72, Flesch 70.25. Longest sentence 23 words ("We commit your soul to the devil," they said, and Hus answered, "And I commit it to the most gracious Lord Jesus Christ."). No sentence is over 25 words.
**Audio.** It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and has no other tag. Checked by `diff` with the two tags stripped.
**Entry.** No sentence in any entry string is over 25 words (script check). The JSON parses.
**Records.** The file parses. A key-by-key comparison with `e3021cfc` shows only five fields changed in this key: `claims[24]` (claim and witness), `claims[108]` (claim and witness), and `absent_details[2].note`.
**Reviewer.** A fresh Opus reviewer at full effort, who had not seen the drafting or the round 1 or round 2 fixing. I edited no repo file and made no model, network or paid calls.

Abbreviations as in rounds 1 and 2 (FIN2, FIN3, MANSI27, RICH, PALDOC, PALUB, LUTH2, GERSON, RAYN28, FOXE, BRAGHT). Also: CRESPIN1 = `crespin_histoire-des-martyrs-t1-fra_benoit-lelievre1885.txt`; FOXE8 = `foxe_acts-and-monuments-v8_cattley-townsend1837.txt`.

## Verdict: PASS, with two minor findings

- **Round 2 findings.** All seven are closed, and every fix is right where it touches the entry and the brief.
- **The last session (A2-S1).** The order of events is now right in `decided[12]` and in records claim 24. The command is the pope's and the whole council's. One small point remains: the dismissal did not come "just" after the Mass, because the litanies and prayers came between (A3-M2).
- **Wyclif's bones (A2-S2).** The new note is true in what it claims: the burning is held only in later writers, and no witness of the time is held. But its list reads as complete, and it is not. Crespin tells the burning as done, twice (A3-M1). This is in the records only, and the entry does not rely on it.
- **Severity.** Nothing is blocking or substantial.

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| A2-S1 | CLOSED, with a new point | **Entry `decided[12]`.** The dismissal now comes first, then the Polish request, Martin V's answer, the sermon and the decree. That is the order in the single-column first account. MANSI27 l.129231-129246: "Qua finita, & litaniis cum solitis orationibus finitis & peractis, reverendissimus pater dominus * macello diaconus cardinalis, de mandato ipsius domini nostri totiusque sacri Concilii ... pronunciavit ... Domini, ite in pace ... Quo facto ... Joannes de Podiomitis episcopus Catanensis". Then the left column: "Antequam ... ambassiatores ... Uladislai Poloniae regis ... petierunt ... libellum ... Joannis Falkemberg" (l.129290-129300); "de appellando ad futurum Concilium" (l.129306-129307); "conciliariter ... & non aliter" (l.129310-129314); "fecit collationem solemnem" (l.129320); Chalant reads "Martinus episcopus" (l.129332-129341); "ipsum Concilium absolvimus ... licentiam impartimur" (l.129367-129370). The right column's second account has "Ynibaldus ... sancti Viti in Macello ... de mandato domini nostri Papae, totiusque sacri concilii" before "Domini, ite in pace" (l.129318-129327). "At the command of the pope and the whole council" is right. "A decree in his name" is right for "Martinus episcopus servus servorum Dei". **Records claim 24.** The order, the speaker and the command are right, and the witness range covers every step. See A3-M2 on "just after". |
| A2-S2 | CLOSED, with a new point | **Records `absent_details[2].note`.** All four cited places say what the note says. LUTH2 l.1761-1763 is note [22]: "the body of Wycliff was exhumed and cremated and the ashes cast into the water (1427)". BRAGHT l.45476-45486 quotes Mehrning: "forty-one years after his death, his bones, by order of the pope, were exhumed, burnt, and the ashes thrown into the water". FOXE l.7920-7922 is the heading "... A. D. 1425", and l.8042 reads "burnt his bones, and drowned his ashes". "No witness of the time is held" stands (see Searches). But the list leaves out Crespin (A3-M1). |
| A2-M1 | CLOSED | **Entry `outcome[1]`.** "(the acts, in Mansi)" is now "(Mansi)". That fits a sentence that already opens "His written reply said", and it matches MANSI27 l.111386-111390: "Respondet idem dominus Papa, quod praedicti congregati in Constantia non sunt generalis Synodus". "(Finke)" now ends the cardinals' sentence. FIN3 l.29733-29738 is no. 244, "Antwort der Kardinäle Benedikts XIII. auf die Aufforderung Alfonsos ... Peñíscola 1416 Mai 3", addressed "d. Alfonso Aragonum et Sicilie regi" (l.29750-29753). The words are at l.29988-29989: "ad congregacionem Constancie ire non possumus nee debemus". |
| A2-M2 | CLOSED | **Entry `outcome[4]`.** "It said he had Hus condemned and burned 'under his safe-conduct, or rather his bald-conduct', and Jerome in the same way." PALUB l.2328-2332: "virum M. Joh. Hus ... sub suo salvo aut potius calvo conductu. similiter Jeronymum ... eadem crudelitatis nece jussit condemnari et exuri". The phrase now sits with Hus alone, and "in the same way" renders "similiter ... eadem ... nece". It adds nothing. Jerome is introduced earlier in the entry (`decided`, l.54 of the file). |
| A2-M3 | CLOSED | **Entry `record`, Richental row.** "Buck judges the Aulendorf codex he prints a mid-1400s copy of an exemplar from the 1420s." RICH l.406-412: "als ob der Aulendorfer codex ... eine um die mitte des fünfzehnten jahrhunderts gefertigte abschrift einer aus den zwanziger jahren stammenden vorlage sei". l.904: "Der zu gründe gelegte codex aulendorfensis (A)" confirms that this is the text he prints. |
| A2-M4 | CLOSED | **Records claim 108 and entry `uncertain[4]`.** GERSON l.26993-26999 is the heading "Quomodo, & an liceat in causis Fidei a Summo Pontifice appellare". The Monitum, l.27012-27015, reads: "Scriptus est iste Tractatus Anno 1418. sub finem Concilii Constantiensis occasione appellationis Oratorum Polonorum ad futurum Concilium circa negotium Libri seditiosi Joannis Falkemberg". The file header gives the editor as Louis Ellies Du Pin, 1706. "Several times in public" is right for "pluries palam dixit" (l.27293). The date is now told as Du Pin's, and it does not read as Gerson's own. That is the right correction to the round 2 proposal. "Polish envoys" is right for "Oratorum Polonorum". The appeal the tract answers is the one in MANSI27 l.129306-129307 ("protestabantur de gravamine & de appellando ad futurum Concilium"). The witness range l.26985-27015 and 27283-27294 covers both the heading and the passage. |
| A2-M5 | CLOSED | **Brief p.8.** "by their editor František Palacký's count." PALDOC's header names Palacký as editor, Prague 1869. His heading no. 85 has "sigillis 452 additis" (l.30063-30067). His note gives "concilio vero VIII literae missae fuerunt" (l.30270). **Brief p.3 and p.5.** The two full stops keep each claim with its witness. In p.3, "Fillastre writes" governs only the first sentence, as it did before the split. In p.5, neither sentence carried a witness before, and neither does now. The audio has the same three edits. |

## New findings

### Blocking

None.

### Substantial

None.

### Minor

**A3-M1. Minor (the rewritten note on Wyclif's bones reads as a complete list, and it leaves out Crespin).**

Location: `records.json`, `council-of-constance-1414`, `absent_details[2]` ("The burning of Wyclif's bones as carried out"). The note reads: "That the burning was done is held only in later writers: Foxe, under the heading A.D. 1425 (...); the 1916 editors of Luther's works, who date it 1427 (...); and van Braght's Martyrs Mirror, quoting Mehrning, ... No witness of the time is held."

What the sources show. Crespin's martyrology also tells the burning as done, in two places:
- CRESPIN1 l.19221-19225: "quarante & vn ans après sa mort, il fut déterré par le commandement du Pape, ses oz furent bruflez, & fes cendres iettees dedans l'eau". This means "forty-one years after his death, he was dug up by the pope's command, his bones were burned, and his ashes thrown into the water".
- CRESPIN1 l.19965-19968: "après la mort de Hus, par sentence dudit Concile, les os de Wicleff furent déterrez & bruflez". This means "after the death of Hus, by sentence of the said council, Wyclif's bones were dug up and burned".
- The file is the 1885 Benoit edition of the 1619 text (header). Crespin died in 1572. He is a later writer, so the note's main claim still holds.
- Foxe tells it a second time, in his eighth volume, dated "about the year of the Lord 1400" (FOXE8 l.23562-23564). That is still Foxe, so it does not make the note false.

Why it matters. The colon and the "and" before the last item make the list read as complete. It is the same kind of point as A2-S2, in milder form. The note's main claim is true, and the entry does not rely on it. So this is minor.

Fix. Replace the note with:

"The council ordered them dug up in 1415 (Mansi), and Martin V's letter of his eleventh year orders them burned (raynaldus l.7977-8019). That the burning was done is held only in later writers. Among them are Foxe, under the heading A.D. 1425 (foxe l.7920-7922, 8042); Crespin's martyrology, which says he was dug up 'par le commandement du Pape' and his bones burned (crespin t1 l.19221-19225, 19965-19968); the 1916 editors of Luther's works, who date it 1427 (luther_works-v2 l.1761-1763); and van Braght's Martyrs Mirror, quoting Mehrning, 'forty-one years after his death' (van-braght l.45484-45486). No witness of the time is held."

**A3-M2. Minor ("just after the Mass" leaves out the litanies).**

Location: entry `decided[12]`, first sentence: "At the last session, the acts say, the words 'Lords, go in peace' came just after the Mass."

What the source shows. MANSI27 l.129231-129233: "Qua finita, & litaniis cum solitis orationibus finitis & peractis". The Mass ended, then the litanies and the usual prayers were said, and only then came the dismissal. "Just" claims nothing came between. Records claim 24 says "After the Mass", which is right.

Fix. Replace the sentence with: "At the last session, the acts say, the words 'Lords, go in peace' came after the Mass and the litanies." (19 words)

## Verified

- **Every changed or added quote, checked against its file and line in context (speaker, council, year):**
  - "Domini, ite in pace", its speaker and the command of the pope and the whole council: the last session, 22 April 1418, both accounts (MANSI27 l.129231-129246, 129318-129327);
  - "conciliariter ... & non aliter": Martin V at that session (l.129310-129314);
  - the dissolution decree, "ipsum Concilium absolvimus ... licentiam impartimur" (l.129367-129370);
  - "not a general synod": Benedict XIII's reply, Peñíscola, January 1417 (MANSI27 l.111386-111390);
  - "could not and must not go": the three cardinal deacons to Alfonso, 3 May 1416 (FIN3 l.29733-29753, 29988-29989);
  - "sub suo salvo aut potius calvo conductu ... similiter Jeronymum": Prague to Venice, 1420 (PALUB l.2328-2332);
  - Buck's "abschrift einer ... vorlage" for the Aulendorf codex (RICH l.406-412, 904);
  - Gerson's "pluries palam dixit" and Du Pin's Monitum dating the tract to 1418 (GERSON l.26993-27015, 27283-27294);
  - "sigillis 452" and the eight letters: Palacký's heading and note (PALDOC l.30063-30067, 30270-30273);
  - LUTH2 note [22] (l.1761-1763), BRAGHT quoting Mehrning (l.45476-45486), FOXE (l.7920-7922, 8042).
- **Translations.** "Several times in public" for "pluries palam", "in the same way" for "similiter ... eadem ... nece", "a decree in his name" for "Martinus episcopus", and "gave all leave to go home" for "ad propria remeandi ... licentiam impartimur". All are faithful and add nothing.
- **Split or joined sentences.**
  - Brief p.3 and p.5: each claim keeps its witness.
  - `decided[12]`: "the acts say" opens the item, and "(Mansi)" closes it. Every step sits inside one account.
  - `outcome[1]`: Mansi and Finke each sit with their own sentences.
  - `uncertain[4]`: Hefele, the acts, Gerson and Du Pin each keep their own claims.
- **Writing.** No changed reader-facing string has an empty contrast, an "X and never Y", a summing-up line, filler or an editor's view told as settled. On p.8, "by their editor František Palacký's count" stacks a possessive on a name. That reads a little heavily aloud, but nothing in it is wrong, so it is not a finding.
- **Reading level.** FK 6.72 is under the grade 8 floor in CLAUDE.md, down from 7.03 before round 2 because of the A2-M5 splits. The brief is not flattened: Richental's foxes, the paper crown and the "bald-conduct" all survive. I record it as a note for the coordinator, as with era 5's Clermont, and not as a finding.
- **Census.** No tradition id or census claim changed.

## Searches run

All of `cic/texts/` unless named. Case-insensitive, with OCR and spelling variants.
- **Wyclif's bones burned (A2-S2, A3-M1).**
  - Single-line grep: the name forms `w[iy]c?k?l[iey]ff?e?|wicleff|viclef|wikleff|wiklef` within 200 characters of `bones|ossa|gebeine|beine|cineres|ashes|ossements|cendres|kosti|popel|exhum|ausgegraben|verbrann|cremat|combust|concremat`.
  - A Python scan of every file that names Wyclif (`w[iy]c?k?l[iey]f|wiclef|viklef|viclef|wicleff|wiklef|wickliff`). It joined hyphen line breaks, flattened whitespace, and printed every hit with `bones|ossa|offa|gebein|cineres|ashes|exhum|ausgegrab|cremat|digged|dug up|ossement|cendres|oz|os|déterr|kosti|popel|ausgrab|asche` within 250 characters. That gave 71 hits in 35 files.
  - Hits telling the burning as done: FOXE (several), FOXE8 l.23562-23564, CRESPIN1 l.19221-19225 and 19965-19968, LUTH2 l.1762, BRAGHT l.45485.
  - Hits giving the order only: MANSI27, Gratius, Palacký's Documenta, Workman's Hus letters l.10019, Gillett v2 l.5739, Hughes's Methodistiaeth Cymru, and RAYN28 l.198 ("ossa exuri jussa").
  - Also `lutterw|luttyrw` and `swift|avon|severn`, plus checks in Vaughan, Matthew, Arnold, Perrin, Knighton and the Fasciculi. None gives a witness of the time.
  - The file list holds no Netter, Walsingham for 1428, or Lincoln register of the right years.
- **The last session's order (A3-M2).** I read MANSI27 l.129210-129375, both columns.
- **Gerson's tract.** GERSON l.26980-27020 and l.27278-27298 (heading, Monitum, passage).
- **Finke.** FIN3 l.29728-29756 and l.29980-29990. These were read in the bd3 file alone: a first `sed` over both Finke files ran them together and gave the wrong lines.

## Counts

Blocking 0. Substantial 0. Minor 2 (A3-M1, A3-M2). Round 2 findings: 7 closed, 2 of them with a new point (A2-S1, A2-S2). None open.


## Council profiles, era 6, round 3: Part B (Council of Basel–Ferrara–Florence 1431)

**Council.** `council-of-basel-ferrara-florence-1431`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era6/council-of-basel-ferrara-florence-1431.brief.txt`, `audio/council-of-basel-ferrara-florence-1431.audio.txt`, `council-of-basel-ferrara-florence-1431.entry.json`, and `records.json` key `council-of-basel-ferrara-florence-1431` (now 129 claims, 21 contested claims, 12 absent details). Changes `e3021cfc..HEAD` on `claude/cft-councils-era6`, read against `R2_recheck.md` Part B and `R2_changes.md` Part B.
**Brief.** Unchanged in this round (`git diff e3021cfc HEAD` is empty for it). 400 words (2:30 at 160 wpm, at the cap). `grade_text`: FK 6.53, Flesch 70.83. Longest sentence 20 words ("The acts print a note, found after his death, accepting all that the church of elder Rome holds and teaches.").
**Audio.** Unchanged. It equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph (checked with `diff`).
**Entry.** The JSON parses. In the rewritten `uncertain` item the longest sentence has 20 words. No new or changed entry string has a sentence over 25 words (checked by script; the only hit over 25 is a splitter artifact on question marks inside quotes in unchanged `outcome` text).
**Reviewer.** A fresh Opus reviewer at full effort, who has not seen the drafting or the round 1 or round 2 fixing. No repo file was edited. No model, network or paid calls were made.

Abbreviations as in rounds 1 and 2 (M31, RAY, GLASS, DOUK, LUD, ZY, MEND, ALM). Added here:
- LUDH = `ludolf_new-history-of-ethiopia_jp1682.txt` (Ludolf's Historia Aethiopica, "Made English by J. P.", London 1682).
- TEL = `telles_travels-of-the-jesuits-in-ethiopia_1710.txt`.

## Verdict: REVISE (one blocking, one substantial, two minor)

All five round 2 findings are closed as findings. The four minor fixes (B2-M1 to B2-M4) are right, and every changed witness line checks out. Every new Latin and Portuguese rendering in the B2-S1 fix is faithful.

But the B2-S1 fix gave Ludolf's "Nihil autem tale" a new antecedent, and it is the wrong one. The entry, the records claim and the contested claim now read as Ludolf denying that the king's envoys came to Florence. Ludolf's own History, held in the library and never cited in this profile, says no one doubts the embassy Zara Yaqob sent in 1439 (B3-B1). The new Innocent X claim is tagged `acts`, which the pattern keeps for the council's own record (B3-S1). Two new entry sentences read loosely (B3-M1, B3-M2).

This is round 3, the cap. B3-B1 and B3-S1 go to the coordinator for Mark's cap ruling.

## Round 2 findings

| ID | Status | Evidence |
|---|---|---|
| B2-S1 | CLOSED, with a new blocking point (B3-B1), a new substantial point (B3-S1) and two new minor points (B3-M1, B3-M2) | The held witnesses are now in: ALM l.28117-28125, 28184, 28464-28468 (the oration, "pelo Emperador e Patriarcha"); ALM l.7658-7697; MEND l.1414-1420, 1432-1440, 1450-1451 (Innocent X, "regem Zerah oratores ad Eugenium IV ... in concilio Florentino, qui tum Ferrariae agebatur, legasse"; "die xxx octobris mdcxxxxv"); MEND l.6747-6750 ("monachorum ad Florentinam synodum confluentium relatione"); MEND l.1420, 1457-1464 (Beccari, "quae, ut historicis notum, commentitia est"). The corrected line numbers in `R2_changes.md` are right. The new antecedent for Ludolf's "Nihil autem tale" is wrong (B3-B1). |
| B2-M1 | CLOSED | GLASS l.20476: "celebrata est prima sessio concilii Basileensis". Both places now cite l.20474-20476. |
| B2-M2 | CLOSED | RAY l.382: "Coepta Synodus Ferrariae, praeside Nicolao Albergato." |
| B2-M3 | CLOSED | Split in two. M31 l.28617-28623: "concordata sunt inter legatos sancti concilii Basiliensis, & generalem congregationem inclyti Regni Bohemie & Marchionatus Moravie, in civitate Pragensi" (`acts`). M31 l.28596-28599 (Mansi's admonition): "compactata cum Bohemis, ab ipsis primum concilii legatis ejus nomine in Praga & alibi concordata, ac dein ab ipso demum concilio confirmata" (`modern reconstruction`). The corrected range l.28594-28599 is right. |
| B2-M4 | CLOSED | The decree claim now cites only Mirbt and Denzinger. The new Doukas claim cites DOUK l.12004-12007 ("τὸ ὅπερ λέγουσιν οἱ Γραικοὶ ἐκ πατρὸς δι' υἱοῦ") and l.12038-12040 ("id quod Graeci dicunt ex patre per filium"), tagged `later narrative`. |

## New findings

### Blocking

**B3-B1. Blocking (a witness's position reversed; a held witness missing). Ludolf is made to deny the embassy, and his own History, which affirms it, is not cited.**

*Locations (all changed in round 2).*
- Entry `uncertain`, "Who sent the Ethiopians: ...": "Catholic writers, Ludolf says, hold that the king's envoys came to Eugenius at Florence. Ludolf answers that nothing of the kind was done at the council. The Jesuits themselves, he says, show that Zara Yaqob stood apart from the Roman church."
- Records claim: "Ludolf answers the Catholic writers who say the Ethiopian king's envoys came to Eugenius at Florence: nothing of the kind was done at the council, he says. The Jesuit fathers themselves, he says, show Zara Yaqob stood apart from the Roman church".
- Contested claim "Who sent the Ethiopian envoys", the side "Nothing of the kind was done at Florence, and Zara Yaqob stood apart from Rome: Ludolf (... l.52403-52408; ... l.52431-52442)".

*Evidence.*
- LUDH l.19489-19496 (Ludolf's own History, Book III): "Nor is there any doubt made of the Embassy Which Zera-Jacob sent to Eugenius the Fourth, in the year 1439. toward the Conclusion of the Council of Florence. Gregory had known nothing of it, had he not seen the Embassador and his Retinue painted at Rome, and known his own Countrymen by their Habit." (OCR: "Embasly", "Councrymen", "Habic".) So Ludolf takes the embassy as Zara Yaqob's, beyond doubt.
- LUD l.52444, the Commentarius itself, a few lines on: "Post illa tempora nulla Aethiopica legatio Romam venit", after those times no Ethiopian embassy came to Rome. This grants the earlier embassy. `R2_changes.md` noticed this line and still set the antecedent to the envoys' coming.
- What "tale" denies. LUD l.52432-52434: "Nihil autem tale in Concilio Florentino actum, sed potius Zera-Jacobum ab Ecclesia Romana alienum fuisse, testantur ipsi Patres Societatis". The "sed potius" sets "tale" against Zara Yaqob's standing apart from Rome. What came just before is Miraeus, who "Zera-Iacobo attribuit" a confession and "corrumpit & adulterat" it to look Catholic (l.52411-52413; OCR poor). So Ludolf denies a Catholic union by the king at Florence, not the embassy.
- The dossier had flagged LUDH l.19493 as "not read in context" (`working/dossier_florence.md` l.260). It was never cited.
- TEL l.6272-6295 (the English Tellez, 1710) also puts the embassy under Zara Yaqob: "In the Days of this Zara Facob [Jacob] the Florentine Councel was held ... he that desir'd to reduce his Empire to the Catholick Faith ... and sent some of his Abyssinians to Pope Eugenius the 4th".

*Why blocking.* As written, a reader takes Ludolf as a witness against the embassy. His History says the opposite. A witness's stance is reversed in reader-facing entry text and in a contested claim's sides.

*Fix, entry `uncertain`.* Replace the three Ludolf sentences above with these four (21, 15, 15 and 17 words):
> "Ludolf's History, in its English of 1682, says no doubt is made of the embassy Zara Yaqob sent in 1439. The Jesuit history of Tellez, in English, also says Zara Yaqob sent Ethiopians to Eugenius. In his Commentarius of 1691, Ludolf denies that Zara Yaqob joined Rome at the council. The Jesuits themselves, he says, show the king stood apart from the Roman church."

*Fix, entry `record`.* Ludolf item:
- witness: "Hiob Ludolf, Commentarius ad Historiam Aethiopicam (1691) and his History in English (1682), with a Latin version of the oration of the Portuguese patriarch Alphonsus Mendez"
- note: "Ludolf takes the embassy of 1439 as Zara Yaqob's, but says the king stood apart from the Roman church. The oration, in his Latin, says the emperor and the metropolitan sent the envoys."

*Fix, entry `sources.writtenLater`.* Add:
- {"title": "A New History of Ethiopia", "author": "Hiob Ludolf, made English by J. P.", "language": "English", "file": "cic/texts/ludolf_new-history-of-ethiopia_jp1682.txt"}
- {"title": "The Travels of the Jesuits in Ethiopia", "author": "Balthazar Tellez (the title page's attribution; the work is credited to Manuel de Almeida), English translation anonymous", "language": "English", "file": "cic/texts/telles_travels-of-the-jesuits-in-ethiopia_1710.txt"}

*Fix, records.*
- Ludolf claim. Text: "Ludolf's Commentarius denies that Zara Yaqob joined Rome at the council of Florence. The Jesuit fathers themselves, he says, show the king stood apart from the Roman church". Witness LUD l.52403-52413; LUD l.52431-52444. Later narrative, Contested.
- Add: "Ludolf's History, in its English of 1682, says no doubt is made of the embassy Zara Yaqob sent to Eugenius IV in 1439, toward the end of the council. The Ethiopian Gregory, it says, knew of it only from a painting at Rome". Witness `ludolf_new-history-of-ethiopia_jp1682.txt l.19489-19496`. Later narrative, Contested.
- Add: "Tellez's Jesuit history, in English, says Zara Yaqob wished to bring his empire to the Catholic faith and sent some of his Abyssinians to Eugenius IV". Witness `telles_travels-of-the-jesuits-in-ethiopia_1710.txt l.6272-6295`. Later narrative, Contested.
- Contested claim "Who sent the Ethiopian envoys":
  - After the Perruchon side, add: "Zara Yaqob, in 1439, toward the council's end, beyond doubt: Ludolf's History, English of 1682 (ludolf_new-history-of-ethiopia_jp1682.txt l.19489-19496). Zara Yaqob: Tellez, in English (telles_travels-of-the-jesuits-in-ethiopia_1710.txt l.6272-6295)."
  - Replace the Ludolf side with: "Zara Yaqob did not join Rome at the council and stood apart from it: Ludolf's Commentarius (ludolf_commentarius-ad-historiam-aethiopicam-lat_1691.txt l.52403-52413; ludolf_commentarius-ad-historiam-aethiopicam-lat_1691.txt l.52431-52444)."
- `absent_details`, "An Ethiopian-side witness", second sentence. Replace with: "Ludolf's Commentarius (1691) and his History in English (1682) were read in context. So were Tellez, Almeida and Mendez, with Beccari's introduction and Innocent X's brief. None is an Ethiopian text of the time."

### Substantial

**B3-S1. Substantial (pattern rule broken: a 1645 papal brief tagged as the council's own record).**

*Location.* Records claim "Pope Innocent X's brief of 30 October 1645, as Beccari prints it, says King Zerah of Ethiopia sent envoys to Eugenius IV ...", `witness_kind: "acts"`.

*Evidence.* `Council_Profile_Pattern.md` l.16: "**acts**: the council's own minutes, canons, creed, decree, synodal letter or subscription list". l.72: `witness_kind` "lets a reviewer see at a glance which claims rest on the council's own record and which on later tellers". MEND l.1450-1451 dates the brief "die xxx octobris mdcxxxxv", two centuries after the council. The precedents `R2_changes.md` cites are not like it: Lateran V's decree and the Lausanne synod's decree are acts of councils (and Lausanne is Basel's own continuation). A papal brief of 1645 that recounts 1439 is a later teller.

*Fix.* Change `witness_kind` to `"later narrative"`. Text, witness and confidence stay as they are.

### Minor

**B3-M1. Minor (an unclear referent, made by the round 2 wording).** Entry `uncertain`: "Alphonsus Mendez, the Catholic patriarch sent to Ethiopia, gave an oration there in 1626. In Almeida's Portuguese of it, the emperor and the patriarch sent them." With Mendez just named "the Catholic patriarch", "the patriarch" in the next sentence reads as Mendez. ALM l.28464-28465 has "ao concilio Florentino forão mandados embaixadores pelo Emperador e Patriarcha", a patriarch of 1439. Fix: "In Almeida's Portuguese of it, the emperor and the patriarch of that day sent them." (14 words)

**B3-M2. Minor ("only" understates the witness).** Entry `uncertain`: "Almeida's history says only that some Ethiopians came with the Armenians as the council ended." ALM l.7674-7680 also says they made "profissão da sancta fee catholica" and "levarão com sigo as letras da união", and l.7693-7697 says Eugenius's bulls reached Ethiopia in Zara Yaqob's time. The point of "only" is that he names no sender. Fix: "Almeida's history names no sender: some Ethiopians, it says, came with the Armenians as the council ended." (17 words)

## Verified

- **Brief and audio.** Unchanged since `e3021cfc`; numbers as in the header.
- **The oration (ALM).** l.28117-28121 has the chapter heading naming "o patriarca dom Affonso Mendez". l.28124-28125 has "huma quarta feira, dia undecimo de fevereiro do anno de 1626". At l.28174-28182 Almeida says he gives "ao menos a substancia della". l.28184 has "Pratica do Patriarca no acto do juramento". l.28464-28468 has "pelo Emperador e Patriarcha ... o emperador David ... dizia ter a dita carta em seu poder", and l.28514 resumes "Em se acabando a pratica do patriarcha". "Alphonsus Mendez, the Catholic patriarch sent to Ethiopia, gave an oration there in 1626" is supported.
- **Ludolf's Latin of the oration.** LUD l.57418-57421: "Venerunt ab Imperatore & metropolita vestro Oratores ad concilium Florentinum", then "quas adhuc apud se extare testatus est Imperator David". "Your metropolitan" and "still had" are faithful. LUD l.56873-56877 gives the Italian print of Mendez's letter of 1 June 1626 as the source, so "a Latin version" in the `record` witness is right.
- **Innocent X's brief.** MEND l.1432-1440 and l.1450-1451. "Then held at Ferrara" renders "qui tum Ferrariae agebatur". "To join the Ethiopian church to the Roman" renders "ut Aethiopicam Ecclesiam cum Romana coniungeret". "Also names the king, as Zerah" is right.
- **Beccari.** MEND l.1420 ("Mirari, ut mitius loquar, iure") runs on to l.1457-1464: "commemorari obedientiam praestitam a Zara Iacob in concilio Florentino, quae, ut historicis notum, commentitia est". The running heads "INTRODUCTIO XXXI" (l.1405) and "XXXII INTRODUCTIO" (l.1456) confirm it is Beccari's own introduction. "Historians know ... to be a fiction" is faithful. Tagging it `modern reconstruction` is right. Beccari's margin summary of Almeida (ALM l.30012-30013) says envoys gave obedience in Zara Yaqob's time. That is not the same as obedience by the king, so it does not conflict with his verdict.
- **Mendez's history.** MEND l.6747-6750: "piissimorum Lusitaniae Regum ... Cum enim ex Marci Pauli veneti peregrinatione et monachorum ad Florentinam synodum confluentium relatione agnovissent ... Presbyterum Ioannem". "Portugal's kings" and the monks are faithful.
- **Almeida's narrative.** ALM l.7658-7697: "como refere o cardeal Baronio ... no fim do tal concilio chegarão ali com os Armenios alguns Ethiopes ou Abexins ... nem o emperador Zara Jacob, em cujo tempo chegarão a Ethiopia as bullas do papa Eugenio, nem seus successores se mudarão, nem melhorarão do schisma". The records claim is faithful.
- **The Mendez records claim** and the new `record` items for Almeida and Mendez, with their kinds (`later narrative`) and the two `sources.writtenLater` entries, match their files and headers.
- **Contested sides.** Every line range in the rewritten "Who sent the Ethiopian envoys" was opened and checked. Only the Ludolf side is wrong (B3-B1).
- **B2-M1 to B2-M4** as in the table.
- **Counts.** The records key holds 129 claims, 21 contested claims and 12 absent details. That matches `R2_changes.md` (123 + 2 split + 4 added).

## Searches run

- **For B3-B1, Ludolf on the embassy.** Grepped LUD for `floren` (hits l.52406, 52433, 52757, 57423, plus unrelated "florentes" and "Florentius"). Read LUD l.52390-52456 in context. Grepped LUDH for `zera|1439` and `floren|eugen` (hits l.19417, 19492-19493); read LUDH l.19405-19510.
- **For B3-B1, other held sender witnesses.** Grepped TEL for `eugen|1439|florence|embass`; read TEL l.6270-6300 and noted l.8345-8361 (the passage round 2 read).
- **"An Ethiopian-side witness" (the changed absence note).** Listed `cic/texts/` names matching `ethiop|aethiop|gez|abyss|habes|ludolf|zara|kebra|synax|mendes|almeida|paez|alvar|telles|castanhoso|basset|dengel`. Grepped all of `cic/texts/` for `zar.?a[ -]?y(a|â)|zera-?jac|zara-?iac|zara[ -]?jac|zar'a|zär'a|zara ?yaq|zara ?iacob|zera ?iacob`. In 21 Ethiopian and Jesuit files I grepped `flor[eê]n[cçtz]|florenti|ferrar|eugen(ius|e|io)`.
  - The Ethiopian texts of the time give nothing on Florence. Amda Seyon, the Futuh, Sarsa Dengel, both Basset synaxaires and the Pachomian rules hit only on Florence libraries or modern editors. The Ethiopian Synaxarium hits only on saints named Eugenius and an index entry, "Eugenius IV" (v1 l.4557). The gadla of Maba Seyon and of Takla Haymanot, the Taamra Maryam and the Kebra Nagast have no hits. The Zara Yaqob chronicles hit only at ZY l.674, Perruchon's own note that they are silent.
  - The hits in Paez, Alvares and Castanhoso are unrelated (a Florentine jeweller and the like).
  - Conclusion: the absence holds. No held Ethiopian text of the time names Florence. Ludolf's History and Tellez are later Western texts and do not break it.

## Counts

Blocking 1 (B3-B1). Substantial 1 (B3-S1). Minor 2 (B3-M1, B3-M2). Round 2 findings: 5 closed (B2-S1 with new points B3-B1, B3-S1, B3-M1 and B3-M2). The brief is unchanged: 400 words, FK 6.53, Flesch 70.83, longest sentence 20 words.
