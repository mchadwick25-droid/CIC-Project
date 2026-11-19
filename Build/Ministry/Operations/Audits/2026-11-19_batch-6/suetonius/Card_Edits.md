# Card edits: Suetonius

2026-11-19. Base: the census `card` for `suetonius` (= `Card.existing.json`). Every existing field is kept word for word. Only additions were made; no statement was found clearly wrong. Brief: `suetonius.brief.txt`. Short names as in `Source_Sheet.md`: **ROL** = `cic/texts/suetonius_lives-of-the-caesars-loeb_rolfe1914.txt`, **THF** = `cic/texts/suetonius_lives-of-the-twelve-caesars_thomson-forester1909.txt`, **NT-E** = `cic/texts/webbe_world-english-bible-british-edition.xml`, **TERT-L** = `cic/texts/tertullian_quae-supersunt-t1-apologetica-lat_oehler1853.txt`, **TERT-E** = `cic/texts/anf03_tertullian.xml`, **LAC-E** = `cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml`. Every line cited below was re-read in its file.

Keys used: only those `tools/validate-census.mjs` allows (CARD_KEYS). No `briefLength`, no connections, no `secondReading` (all six quoted spans are new).

## Edits

**New: `sources.about`, three entries.** Old: (none). New: Acts 18 in NT-E; Tertullian, *Apology* 3, Latin in TERT-L; *Apology* 3, English in TERT-E. Evidence: the brief quotes Acts ("because Claudius had commanded all the Jews to depart from Rome,", NT-E 88523–88524) and Tertullian (rendered from TERT-L 12453–12455; English TERT-E 1713–1716). Every quotation file must be among the files the card cites. Formats follow the census rows for TERT-E (`pliny-the-younger`) and the Oehler volumes (`marcion-of-pontus`).

**New: `briefReferences`, nine lines.** Old: (none). New, with evidence:
1. Claudius 25.4 and its neighbours: ROL 25841–25845, 25905–25912; brief para. 1.
2. Nero 16.2, 19.3, 38: ROL 28452–28463, 28516–28530, 28653–28656, 28700–28704, 30559–30563; brief para. 5.
3. Rolfe's introduction: ROL 205–216 (Pliny), 229–240 (Hadrian), 320–323 (published in 120, Julius to Domitian); brief paras. 2–3.
4. Rolfe's note: ROL 25871–25874; brief para. 4.
5. THF preface and notes: THF 62–63 (closest friendship), 19535–19537 (how little), 20362–20382 (note 528), 20575–20581 (Tacitus on Nero's Christians); brief paras. 3–6.
6. Acts 18:1–2: NT-E 88521–88524; brief para. 4.
7. Tertullian and Oehler's note: TERT-L 12452–12455, 12505–12514; TERT-E 1712–1716; brief para. 6.
8. Lactantius: LAC-E 3163 (by the change of a letter), 3165 (note: kind, gentle, good); brief para. 6 ("Christian writers had complained"; "The Greek chrestos means kind, or good").
9. Mirbt 1911 and Schanz 1922 print both lines (Source_Sheet I1: MIR 141–151, 2500–2572; SCH 24311–24312, 24348–24349); brief para. 6 ("Historians still weigh both lines").
No quotation marks are used in any line.

**New: `quotationOriginals`, six entries, one for each quoted span in the brief, in the brief's order.**
1. Claudius line. Printed: Latin, ROL 25843–25844. English: Rolfe, ROL 25907–25909 (his footnote mark after "Chrestus" dropped). Entry note on "since", "all" and "one": Source_Sheet E1 (THF 10639–10640).
2. Acts phrase. Printed: NT-E 88523–88524 (the verse ends with a period; the brief's comma is its own sentence).
3. Nero line. Printed: Latin, ROL 28458–28460. English: Rolfe, ROL 28524–28525, from "the Christians" only. The line before, ROL 28523, reads "inflicted a" for "inflicted on" (a scan fault, not listed in `tools/quote_scan_readings.json`), and THF 11612–11614 carries a footnote mark "[577]" inside the sentence, so neither full English can stand verbatim. Entry note on *maleficae*: Source_Sheet E4 (THF 11613, 20568–20569; ROL 28525).
4. "beyond criticism." Printed: Rolfe, ROL 28700–28701. Original: ROL 28653–28654.
5. "how little". Printed: THF 19535–19536 (note 335).
6. Tertullian. Printed: ANF English, TERT-E 1713–1716. No `original` is given: the Oehler scan at TERT-L 12453–12455 is badly damaged ("*Chrestia • Dus*", "pcnes") and no scan reading is listed for it. Entry note: the rendering is from Oehler's Latin; the ANF "the name you hate" against the Latin "nec nominis certa est notitia" (TERT-L 12454).

**Clearly wrong:** none found. Every existing statement was checked: knownFor (ROL 25843–25844, 28458–28460); datesNote (ROL 155–157; THF 57); placeNote; legacy (ROL 377–400); uncertain 1–5 (ROL 25871–25874; THF 10640, 20362–20382; ROL 155–157; THF 49–51; ROL 30559–30563, 28452–28463); keyWorks (ROL 320–323).

**Claims not found:** none.

## Quoted spans, awaiting second reading

| # | Modern (the brief) | Printed | Original / English |
|---|---|---|---|
| 1 | He drove from Rome the Jews who were constantly rioting at the urging of Chrestus. | ROL 25843–25844 (Latin) | ROL 25907–25909 (English) |
| 2 | because Claudius had commanded all the Jews to depart from Rome, | NT-E 88523–88524 | — |
| 3 | Punishments were inflicted on the Christians, a kind of people given to a new and harmful superstition. | ROL 28458–28460 (Latin) | ROL 28524–28525 (English) |
| 4 | beyond criticism. | ROL 28700–28701 | ROL 28653–28654 (Latin) |
| 5 | how little | THF 19535–19536 | — |
| 6 | And even when you wrongly say 'Chrestianus', since you do not even know the name for certain, it is formed from sweetness or kindness. | TERT-E 1713–1716 | Rendered from TERT-L 12453–12455 (Latin) |
