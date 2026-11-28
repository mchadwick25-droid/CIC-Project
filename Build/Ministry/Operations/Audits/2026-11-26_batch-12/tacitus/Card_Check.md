# Card check: tacitus (person, Outside witness)

Checked by a hand that did not write the card: `tacitus.card.json` and `Card_Edits.md` against `CLAUDE.md` ("Trust and source fidelity"), Brief Kit Part 1, the person kind kit, the era 1 card standard (`../../2026-11-26_era1-cards/Header.md`, its four sections), the brief, `Outline.md`, `Source_Sheet.md`, `Review.md`, `Fresh_Read.md`, `Card.existing.json` and the census entry. Every timeline line and every quotation was re-read at its file and lines under `cic/texts/`.

## Verdict: FIX (five changes, below)

The card is sound in nearly all of it. The quotations, timeline and legacy lines stand at their cited lines. Three `uncertain` items and one `modernWorks` title carry modern opinion or a modern date, which Kit Part 1 bars from the card ("A date, identification or judgment that only a modern work makes ... stays out of the story and the card"; the card carries "the debates among the old sources"). One timeline reference does not reach the point it supports.

## The fixes

**FIX 1. `uncertain[7]` (what the verdict means).** Schanz-Hosius-Krüger (SCH 24300-24304), Duchesne (DUC 2385-2386) and McGiffert (EUS 13862-13864) are modern readings, rated Dominant Modern Reconstruction (sheet D3). Ruinart, an old reader under the hearts ruling, stays (RUI 3145-3151: "aperte declarat Christianos etiam ante incendium morte dignissimos judicatos fuisse"). Schanz and Duchesne stay findable in `modernWorks`, McGiffert in `sources` (Eusebius with his notes).
- Old: `What the verdict means. Tacitus says only that they were convicted less for setting the fire than for hatred of the human race. Thierry Ruinart took it to show that the Christians were judged worthy of death even before the fire. Schanz, Hosius and Krüger take it to show that the inquiry proved them Christians, not that they set the fire; Louis Duchesne, that no one blamed the fire on the Christians. Arthur McGiffert holds that the attack was not aimed at their religion as such.`
- New: `What the verdict means. Tacitus says only that they were convicted less for setting the fire than for hatred of the human race. Thierry Ruinart took it to show that the Christians were judged worthy of death even before the fire.`

**FIX 2. `uncertain[8]` (Gibbon, Schiller, McGiffert).** Remove the whole item. It is McGiffert's report of two moderns' view and his own counter-argument (EUS 13849-13857; sheet D1: "MODERN opinion. Contested."). No old source is in it. Gibbon reaches the card only as Roberts read him in 1876 (timeline, 1876, line 3), which stays.
- Old: `Gibbon, and later Schiller, held that Nero's victims were the Jews as a whole, and that Tacitus was wrong to call them Christians. Arthur McGiffert, who translated Eusebius of Caesarea in 1890, disagreed, noting that Josephus says nothing of an attack on the Jews under Nero.`
- New: (item removed)

**FIX 3. `uncertain[10]` (the readings of the Latin).** The manuscript reading (TAC-H 45-51) and what each held print prints are facts about the text, and stay. Which reading is "the true" one is Duchesne's and Harnack's judgment (DUC 2078-2082).
- Old: `Duchesne, following Harnack, takes Chrestianos as the true reading; Mirbt and Schanz print Christianos.`
- New: `Mirbt and Schanz print Christianos.`

**FIX 4. Entry field `modernWorks[2]` (Yonge), for release.** The title carries a modern date and a modern claim about where Tacitus's history ends, which the card has just dropped from `datesNote` and `dates` (sheet S3: Dominant Modern Reconstruction). A modern work's title on the card names the work; the note says what it covers. The note stays.
- Old title: `Roman History, translator's preface (Ammianus's history began in 96, "where Tacitus and Suetonius end")`
- New title: `Roman History, translator's preface`

**FIX 5. `timeline[0].lines[0].reference`.** The line's point is the fire. MIR 2527-2528 hold only the rites; the fire first appears at 2537 ("quin iussum incendium crederetur").
- Old: `Tacitus, Annals 15.44, cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt lines 2527-2528`
- New: `Tacitus, Annals 15.44, cic/texts/mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt lines 2527-2537`

After FIX 2 the `uncertain` list has twelve items. `Card_Edits.md`'s numbering of them (9 to 13) shifts by one from item 9 onward; no other field cites those numbers.

## Rulings on the writer's flags

**Q1, "Cliristus".** Upheld. MIR 2541 reads "Cliristus", an OCR misread: the same sentence in Hooker's print reads "ejus Christus, qui Tiberio iinperi- tante per procuratorem Pontium Pilatum supplicio affectus erat" (HOOK 13988-13994). `printed` gives the page's reading, "Christus", with the rest verbatim at MIR 2541-2543 (line-end hyphen in "procurato- rem"). Release adds the writer's listing to `tools/quote_scan_readings.json` exactly as given in `Card_Edits.md`. The quotation's `uncertain` note is true and stays.

**Q2 and Q3, English only.** Upheld. No held clean Latin witness exists for either.
- Q2: Sulpicius's Latin is held only in Halm (SUL-L 4789-4790, damaged: "^tur uertit inuidiam in Christianos, actaeque in innoiios cnide-lissimae quaestiones"). A search of `cic/texts/` for the sentence in both spellings and for "crudelissimae quaestiones" and "innoxios" finds no other print. Ruinart quotes Sulpicius 2.29 only at the laws and edicts (RUI 3161-3165), not this sentence.
- Q3: Mirbt's last words are damaged (MIR 2564, "in saevitiara unius desumerentur"). Ruinart gives only the first half, and in his own paraphrase (RUI 3134-3136, "quamquam adversus sontes et novissima exempla meritos ... miseratio tamen Gentilium oriebatur"). Hooker and Otto (OTTO 12189-12193) stop at "celebranturque"; Schanz and Duchesne do not print it. "utilitate publica sed" occurs in no held file but Mirbt.
- So the damaged-scan rule governs, and check 4 ("the card carries it") is met as far as a held reading allows. Each entry's `uncertain` note says so plainly. The printed English stands verbatim (SUL-E 10659-10661; TAC 68).

**`regions` "Asia Minor".** The conflict is real: no held line, the card or the outline's Setting puts Tacitus there (Rome, S4). But it is not this card's to fix. The same pair, "Mediterranean" and "Asia Minor", sits on eleven Rome entries in the census (`suetonius`, `hermas`, `valentinus`, `marcion-of-pontus`, `hippolytus-of-rome`, `novatian`, `liberius-of-rome`, `damasus-of-rome`, `marcella-of-rome`, `leo-of-rome` and this one), while other Rome entries carry "Mediterranean" alone. That is a fleet-level map-data defect, and this batch makes no census change beyond the card's listed fields. The coordinator should register it as a fleet-level gap (or `ACCEPTED_OPEN` waiver) for Mark to rule on, not fix it here alone.

## The checks, in order

1. **Evidence and sends.** Every listed field rests on its cited lines, outside the five fixes. Each item the outline sends to the card is on it (numbered as in `Card_Edits.md`, before FIX 2): What came of it 2 (legacy.remembered 2-5, timeline 5 and 6); R1a (legacy.traces 2, timeline 4); Cut first 2 and 3 (timeline 1 line 6, timeline 3 line 1); the 1876 debate and D2 (remembered 5, timeline 6, `uncertain` 10); D5 (`uncertain` 11). D1 and D3 are moderns' readings: after FIX 1 and 2 they are reachable through `modernWorks` and `sources`, which is where Kit Part 1 puts them. The translator's and editor's pointer to Tacitus in legacy.traces 2 is a note on the old text (a parallel passage, SUL-E 11453-11455, SUL-L 5695), allowed as clarifying, not an opinion. The "standardly identified" wording follows the file's own header (TAC-H 22-25). Review.md and Fresh_Read.md send nothing.
2. **Nothing else moved.** A full new card, so every field is listed in `Card_Edits.md`. The kept fields (`otherNames`, `label`, `role`, `uncertain` 1, 12, 13, TAC in `ownWords`, and four `about` sources) match `Card.existing.json` word for word.
3. **`briefReferences`.** All five name what the brief still tells. The removed ones are correctly gone.
4. **Census rules.** Keys allowed by `tools/validate-census.mjs` (`witness` is an allowed period key). Three quoted spans in the brief, three entries, none for the dropped Tertullian span. Each `modern` equals the brief's sentence exactly; each `printed` and `englishPrinted` is verbatim at its lines. Every cited file is in `sources`. No audit named. American spelling in card prose; "cruellest" stands only inside Q2's `modern`, which must match the brief.
5. **"Checked at card."** None: all three quotations run past six words.
6. **Not found.** "Benedictine": correctly not used (RUI 789-792 gives "Monachus Sti Germani a Pratis"). Hooker's and Whiston's dates from the file headers ("1553/4-1600"; "in the eighteenth century"): Widely Accepted lifetimes, which Kit Part 1 allows told plainly, as "before 1600" and "the 1700s". Upheld. Nothing clearly wrong left in beyond the five fixes.
7. **Entry fields.** `dates` "a generation or more after 64" and the new `teaser` match S3, `knownFor` and the brief. `modernWorks` as listed, with FIX 4. The entry exists (`atlasId` I.68), so no new id.

**Readability.** Re-run on the writer's plain text (`/tmp/claude-0/-home-user-CIC-Project/98634fa3-c2ec-54fe-a7b0-4692f28aec1c/scratchpad/tacitus-card/card_text.txt`): `1976 words, grade 8.5 (names out 7.2), reading ease names out 73.2, 16.6 words a sentence, 0.6 joining words per 100, 20% short sentences, longest sentence 39 words - pass`. The longest sentences (`knownFor`, 37 words; the Tertullian timeline line, 33) are warnings only: the knownFor length comes from the two glosses Part 1 requires.
