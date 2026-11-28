# Card check: Valentinus (`valentinus.card.json`)

The checker did not write this card. Read against `CLAUDE.md` ("Trust and source fidelity"), Brief Kit Part 1, the person kind kit, the role, the brief, `Outline.md`, `Review.md`, `Fresh_Read.md`, `Card_Edits.md`, `Card.existing.json` and the census entry. Every timeline line and headline was read against its cited file and lines in `cic/texts/`. File short names: IR `anf01_apostolic-fathers-justin-irenaeus.xml`, CL `anf02_…clement-alexandria.xml`, TE `anf03_tertullian.xml`, KR `tertullian_opera-pars3-lat_kroymann-csel47.txt`, HIP `anf05_hippolytus-cyprian-caius-novatian.xml`, WEN `hippolytus_refutatio-…wendland-gcs26-1916.txt`, HOLL `epiphanius_…holl1915.txt`, JER `npnf203_theodoret-jerome-gennadius-rufinus.xml`.

## Verdict: FIX

Seven exact changes below. Everything else holds.

## What holds

- **Timeline (37 lines, seven periods).** Each line was found at its file and lines: IR 39968–39970, 31519–31543, 19254–19256, 39869–39873, 41174–41178, 31390–31392, 29871–29873, 50552–50554; CL 52956–52967, 34289–34303, 32722–32735, 36157–36161 (Latin, read by hand), 39090–39100, 40954–40960, 46642–46646; TE 21332–21339, 20640–20645, 43109–43122, 43159–43163; KR 9633–9666; HIP 9124–9129, 9168–9174, 9640–9666, 9787–9802, 10054–10059; WEN 12542–12556, 12707–12740 (the two corrections, θέρος P and ἐξειχουμένην P, read in the apparatus); OR 23165–23169; EUS 26652–26658, 34813–34815; HOLL 29802–29807. Hippolytus's chapter numbers (VI.29, 35, 37) are the Greek edition's; the ANF prints them as XXIV, XXX, XXXII. This is right.
- **Quotations.** The brief has three quoted spans, and the card has three entries. Each `modern` matches the brief word for word. Each `printed` is verbatim at its lines (CL 34298–34302; TE 43109–43113, with the ANF's inline note "Martyrii." left out; CL 39090–39093). The Latin `original` matches KR 9633–9653 under the file's entries in `tools/quote_scan_readings.json` (line number 25, Yalentinus, aliura, the apparatus range). None runs under six words, so none is "checked at card", and `secondReading` is rightly left out.
- **Quoted spans in card prose.** All were found in cited files. "the disciple of Platonism." has a question mark in TE 21333. The validator folds punctuation, and the span was kept from the starting card, so no change.
- **Keys.** Every card, period and line key is allowed (`tools/validate-census.mjs` lines 207, 294–295). `keyWorks` keeps to the three that the census notes allow. No audit is named, the spelling is American, and each cited `cic/texts/` file is in `sources`.
- **Kept fields** (`role`, `uncertain[0]`, `[4]`, `[8]`, `legacy.remembered[5]`, the Kroymann entry, the quotation `work` and `uncertain` texts) are word for word with `Card.existing.json`.
- **Outline and fresh read items sent to the card** are all on it: Cut first 1–6; Leave out (Epiphanius on birthplace and Cyprus, Theudas, the psalm, E11, the vision in Hippolytus's voice, the Gospel of Truth, Polycarp, Ambrose and Origen); "Who keeps him today"; the two positions on Jesus's body (Fresh_Read A); the time difference over the expulsion (Fresh_Trust_Second note).
- **No modern opinion, date or identification.** McGiffert's years and the ANF editor's 207 are left out. Ardesianes is not named as Bardaisan. "The middle of the second century" is worked out from the reign of Antoninus that the sources give (Header, "Dates from the sources' own clues"). `modernWorks` notes say what each work covers.
- **`briefReferences`** tell nothing the brief no longer tells. The two lines dropped from the starting card (VI.29, which the brief no longer tells, and the ANF date of 207) are rightly gone.
- **Teaser** (Entry fields): it holds against the card's `knownFor` and the brief.
- **Readability.** The checker's run on the card's running text: `1652 words, grade 7.3 (names out 5.3), reading ease names out 81.4, 13.7 words a sentence, … longest sentence 33 words - pass (note: grade 7.3 is under 8…)`. This is under the floor of 8. It comes from short timeline lines, one fact each, as the card form asks, and the sources' own wording is kept, so the text is not flat. Not blocking.

## Changes

1. **`timeline[0].lines[2].text`** ("Gnostic" is first met here, and the line stands alone, so the gloss belongs here; outline Do not say, "Gnostic" without its plain sense)
   - Old: "He founds a school, a circle of students around a teacher. Irenaeus says he adapted the principles of the Gnostic teaching to it."
   - New: "He founds a school, a circle of students around a teacher. Irenaeus says he adapted to it the principles of the Gnostic teaching, that of people who claimed a special knowledge."

2. **`timeline[5].lines[0].text`** (Fresh_Read B cut this label from the brief because no sense was attached to it, and the line has to stand alone)
   - Old: "Irenaeus writes five books against what he calls knowledge falsely so called, aimed above all at Ptolemy's school, a bud of Valentinus's."
   - New: "Irenaeus writes five books against people who claimed a special knowledge, which he calls knowledge falsely so called. He aims them above all at Ptolemy's school, a bud of Valentinus's."

3. **`timeline[3].lines[4].text`** and **`legacy.remembered[5]`** ("the Word" is a church word, and the card never glosses it; TE 20645–20650: "His own Word… this Word is called His Son")
   - Old (in both): "…who told him he was the Word."
   - New (in both): "…who told him he was the Word, a name for God's Son."
   - `timeline[3].lines[4].reference`: add "; Tertullian, Prescription against Heretics 13, cic/texts/anf03_tertullian.xml lines 20645-20650" after the existing reference.

4. **`timeline[5].lines[3].reference`** (the `when` "Early in the third century" rests on Jerome, and the working must be shown at the line)
   - Old: "Tertullian, Against the Valentinians 5, cic/texts/anf03_tertullian.xml lines 43159-43163"
   - New: "Tertullian, Against the Valentinians 5, cic/texts/anf03_tertullian.xml lines 43159-43163; Jerome, Lives of Illustrious Men 53, under Severus and Caracalla, cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml lines 40494-40499"

5. **`timeline[6].lines[0].reference`** (it has no file; every line carries its file)
   - Old: "World census, Valentinian and other Gnostic Christianities"
   - New: "World census, Valentinian and other Gnostic Christianities, cic-website/data/world-census.json, entry valentinian-and-other-gnostic-christianities, longDescription and legacy"

6. **`briefSources[0].title`** (`briefReferences[1]` rests the brief's "middle of the second century" on Stromata VII.17)
   - Old: "Stromata, Books 2, 4 and 5, in Ante-Nicene Fathers vol. 2"
   - New: "Stromata, Books 2, 4, 5 and 7, in Ante-Nicene Fathers vol. 2"

7. **The writer's flag on the division by nature. The claim is found and is restored.** Irenaeus does report it, of the school, in Against Heresies I.6.2: "they hold that they shall be entirely and undoubtedly saved, not by means of conduct, but because they are spiritual by nature" (IR 30758–30763). The starting card was right, and "not found" in `Card_Edits.md` is wrong. The source sheet does not have the row, but it is a held line on Valentinus's school. It also bears on the point `uncertain[1]` makes, since Clement gives the same teaching to the man (CL 39095–39096, 40955–40957).
   - **`uncertain[1]`**: after "…his long account of the powers is of Ptolemy's school." insert "There Irenaeus reports that the school held its own members would be saved because they were spiritual by nature. Clement gives the teaching of a class saved by nature to Valentinus himself."
   - **`sources.about[0].title`**: "Against Heresies, Book 1 preface and chapters 10 and 11; Book 3 chapters 3, 4 and 11; Book 5 preface" → "Against Heresies, Book 1 preface and chapters 6, 10 and 11; Book 3 chapters 3, 4 and 11; Book 5 preface"
   - **`Card_Edits.md`**, Conflicts and not found: the line "From the starting card, not carried: \"The division of people by nature is reported by Irenaeus\" (not found in the sheet's held lines)" should say the claim is found at IR 30758–30763 (Against Heresies I.6.2) and is carried in `uncertain[1]`.

## The writer's other flag: `regions` "Asia Minor"

The writer was right not to change it on the card. No held line puts Valentinus in Asia Minor: the record has Rome only (S1, S3), and the outline's Setting gives no birthplace. The fault is not this entry's alone. Many era 1 Rome entries carry the same pair (Hermas, Tacitus, Suetonius, Hippolytus, Novatian, Damasus, Leo and others). `regions` is a fleet field owned by the map build slice, and the defect is registered there (`Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md`, "Era 3 on the live tree: carried items (2026-11-14)", the `regions` item). Valentinus's value does not even follow the rule that item records: his home tradition, `valentinian-and-other-gnostic-christianities`, carries ["Mediterranean"] only. Release should not change it under this card. It goes to the map build slice, with Valentinus named in that item, as a case where the value matches neither the person nor the home tradition.

## Not found, and anything clearly wrong left in

- No other claim is listed as not found. "as the American edition's note on his Book 6 shows" was rightly dropped, because a modern note is not a witness.
- The tradition entry's `why` ("an Alexandrian teacher who came to Rome around 136", "a divine spark… trapped"): the writer flagged it, rightly, because it is outside this card. The card does not repeat it.
- Nothing clearly wrong is left in, beyond the changes above.
