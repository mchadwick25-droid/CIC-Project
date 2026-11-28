# Card check: Lactantius (`lactantius`)

Checker's pass over `lactantius.card.json` and `Card_Edits.md`. I did not write this card. I re-read every timeline line, every headline and every `quotationOriginals` entry at its cited file and lines. The card was put into a census copy outside the repository and run through `tools/validate-census.mjs`.

**Verdict: FIX.** Six changes, listed below. Everything else passes.

## What passes

- **Kept fields (item 2).** Each field listed as kept is word for word from `Card.existing.json`: `otherNames[0]`, the three `keyWorks` titles, the first sentence of `keyWorks[1].about`, the Calvin trace, the Chronicle and millennium lines in `remembered`, `ownWords` 0, 3, 4 and 5, and the Vetera and Calvin items in `about`.
- **Items sent to the card (item 1).** Every Cut first and Leave out item marked "card" is on it. So are What came "To the card" (I3 gold, I4, I5, I6), Review's "one book On persecution" (`uncertain` 7 and timeline 5), and Fresh_Read's name tie (`uncertain` 4). Modern names, dates and judgments are gone. No modern work is cited as content.
- **`briefReferences` (item 3).** Each of the twelve items is told in the final brief.
- **Census rules (item 4).** All keys are allowed. There are five `quotationOriginals`, one for each quoted span in the brief and none for a dropped span. The full validator run shows no `printed` or `englishPrinted` failures. Every timeline file appears in `sources`. No audit file is named. Spelling is American outside verbatim print. The remaining errors are the ones release clears (`secondReading` on the four long quotations, and the `quote_renderings.json` listings).
- **"Checked at card" (item 5).** "by force and tortures." renders *ui atque tormentis* exactly (DI-L 26072), and Fletcher prints "by force and tortures" (AN 5136). It passes.
- **Timeline.** The six periods each have a date and a headline. Each line has its reference straight after it. The worked years show their clues: 303 (Eusebius's nineteenth year, the eighth consulship of Diocletian), 311 and 313 (the consulships), and about 392 (Theodosius's fourteenth year). Apart from the four lines fixed below, every line stands on its lines.
- **Readability.** My own run of the card's running text: `lactantius-card-text.txt: 2868 words, grade 9.2 (names out 7.8), reading ease names out 71.8, 18.2 words a sentence, 0.6 joining words per 100, 19% short sentences, longest sentence 44 words - pass`.
- **Entry fields.** The proposed `teaser`, `why`, `floorNote`, `legacy` (the Letter 58 sentence), `dates` and `modernWorks` changes each stand on the evidence given. The `modernWorks` notes say what each work covers, not what it argues.

## FIX

1. **Timeline, period 1 ("Date unknown"), line 4, `text`.** Lactantius's words (*oratorias litteras*, AN 4487 "rhetorical learning") do not say "Latin", and the line is credited as his own words.
   - Old: "He writes that he was called to Bithynia to teach Latin public speaking, and names no one who called him."
   - New: "He writes that he was called to Bithynia to teach public speaking, and names no one who called him."

2. **Timeline, period 1, line 6, `text`.** At AN 2487 and DI-L 12295–12296 he says he gained some skill "on account of my desire to teach others" (*propter studium docendi*). He does not say there that he taught the art.
   - Old: "He says he taught the art of speaking but was never eloquent himself, since he never so much as set foot in the forum, where cases were pleaded."
   - New: "He says he gained some skill in speaking for the sake of teaching, but was never eloquent himself, since he never so much as set foot in the forum, where cases were pleaded."

3. **Timeline, period 3 ("during and after the persecution"), the philosophers line, `reference`.** "Refute one another" is at AN 2300 (Book III.4: the sects wound "one another", "philosophy consumes and destroys itself"), not at 575 or 584. The phrase "chapter as numbered in the English edition" also reads as leftover working.
   - Old: "Divine Institutes I.1, chapter as numbered in the English edition, cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml lines 575, 584"
   - New: "Divine Institutes I.1 and III.4, cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml lines 575, 584, 2300"

4. **Timeline, period 3, the Book VII line, `reference`.** The thousand-year reign is at AN 6650. Line 6648 holds only the six thousand years.
   - Old: "Divine Institutes VII.14, cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml line 6648"
   - New: "Divine Institutes VII.14, cic/texts/anf07_lactantius-apostolic-constitutions-didache-liturgies.xml lines 6648-6650"

5. **Timeline, period 3, the address line, `text`.** "First Roman ruler to honor the one true God" is the address's praise (AN 571). As written, "as" can read as the card's own statement. The praise belongs in its witness's voice.
   - Old: "Some copies open with an address to the emperor Constantine, as the first Roman ruler to honor the one true God."
   - New: "Some copies open with an address to the emperor Constantine, hailing him as the first Roman ruler to honor the one true God."

6. **`uncertain[3]`.** More than one copy gives the first initial: DI-L 131 ("L. Caecilii, Firmiani Lactantii", a very late hand) and DI-L 32648 ("L CAECILI FIRMIANI LACTANCI").
   - Old: "one with the first name Lucius."
   - New: "some with the first name Lucius."

## Ruling on the writer's "not found": "an ancient doctor of the Church"

**Found. The claim is held, and the "not found" is wrong.** The sentence is not in the Calvin *Institutes* file. It is in Calvin's letters: `cic/texts/calvin_letters-vol1_bonnet1858.txt` lines 16669–16670, in his letter to Monsieur le Curé de Cernex. The line reads: "Lactantius also, an ancient doctor of the Church, and St, Augustine, demonstrate that in their time all the afflictions which had happened in the world were imputed to the Evangel". The letter runs from line 16531 to line 16908 of this volume of Calvin's letters. The volume prints it from the French autograph (line 16908). The entry's `legacy` sentence stands, and no entry fix is needed to remove it. Two changes follow from it.

- **Card, `legacy.traces`: add after the Calvin item.** "In a letter to the parish priest of Cernex, Calvin calls Lactantius an ancient doctor of the Church, meaning one of its early teachers. He writes that Lactantius and Augustine show that in their time the world's troubles were blamed on the Gospel, because it had done away with the pagan rites."
- **Card, `sources.about`: add after the Calvin item.** `{"title": "Letters, volume 1, the letter to the curé of Cernex (English tr., ed. Jules Bonnet)", "author": "John Calvin", "date": null, "language": "English translation", "file": "cic/texts/calvin_letters-vol1_bonnet1858.txt"}`
- **`Card_Edits.md`, "Claims not found":** the "ancient doctor" paragraph no longer applies.
- **Entry field `legacy`, for release (Part 1, explain it or leave it out).** Today's readers know "doctor of the Church" as a formal title, and Lactantius does not hold it. So the sentence needs a gloss.
  - Old: "A letter in his collected letters calls Lactantius “an ancient doctor of the Church.”"
  - New: "In a letter to a parish priest, he calls Lactantius “an ancient doctor of the Church,” meaning one of its early teachers."
