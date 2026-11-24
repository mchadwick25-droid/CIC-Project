# Card check: Basil of Caesarea

Checked: `basil-of-caesarea.card.json` against `Card.existing.json`, with `Card_Edits.md`, the brief (733 words), `Outline.md`, `Review.md`, `Fresh_Read.md`, `CLAUDE.md` (Trust and source fidelity), Part 1 of the kit, `kinds/person.md` and `roles/card.md`. `Card.existing.json` is identical to the live census card. The census entry exists already, so no new entry is written.

## Verdict

FIX

## FIX

### Card

1. **keyWorks[2].about.** These are Jackson's dates. Nothing in the field credits them, so they stand as content (check 1; Kit Part 1, Rigor). The outline marks them as his ("the dates of Letters 94, 159 and 223", Who tells it).
   - Old: "Letter 223, placed in 375, defends him"
     New: "Letter 223, placed by Jackson in 375, defends him"
   - Old: "Letter 94, placed in 372, answers the governor Elias"
     New: "Letter 94, placed by Jackson in 372, answers the governor Elias"
   - Old: "Letter 159, placed about 373, to Eupaterius"
     New: "Letter 159, placed by Jackson about 373, to Eupaterius"
2. **briefReferences[0].** Here "placed" follows the translator credit, so it is not clear who placed the letter. Same evidence as change 1.
   - Old: "Letter 223.2, tr. Blomfield Jackson, placed in 375:"
     New: "Letter 223.2, tr. Blomfield Jackson, placed by Jackson in 375:"
3. **briefReferences[5].** Same evidence as change 1.
   - Old: "Letter 94, to the governor Elias, placed in 372:"
     New: "Letter 94, to the governor Elias, placed by Jackson in 372:"
4. **briefReferences[6].** Same evidence as change 1.
   - Old: "Letter 159.2, placed about 373:"
     New: "Letter 159.2, placed by Jackson about 373:"
5. **uncertain[9].** Same evidence as change 1.
   - Old: "Letter 159 is placed about 373, before the attack"
     New: "Letter 159 is placed by Jackson about 373, before the attack"

### Card_Edits.md

6. **Not found.** The Iris entry is wrong. An old source does hold the claim: Basil's own Letter 223.5, `cic/texts/npnf208_basil-letters-select-works.xml` 39261-39262, "visit me in my monastery on the Iris". That file is already in `sources.ownWords`. So `placeNote` stands on an old source and is not a gap.
   - Old: the whole bullet under "## Not found", beginning "`placeNote`, "The monastery on the river Iris in Pontus": no old source held names the Iris"
     New: "None. `placeNote`'s "The monastery on the river Iris in Pontus" stands on Basil's Letter 223.5 (`npnf208...xml` 39261-39262, "my monastery on the Iris")."

## What was checked

1. **Edits against their evidence.** I diffed the two cards field by field. The changes are exactly edits 1 to 13 in `Card_Edits.md`, and nothing else moved. I re-read each cited line in its file, and all of them hold:
   - Jackson 39105-39137, including "sullying my reputation among the brethren" and "the uselessness of 'the wisdom of the princes of this world'".
   - PG 31 72544-72549 and Clarke 13458-13464.
   - Letter 159, 33483-33485.
   - On the Holy Spirit, 14165-14170.
   - Letter 94, 29990-30016 ("come off worse than my accusers"; "what harm the government suffers from me?").
   - Gregory of Nyssa to Peter, `npnf205` 2787-2810.
   - Socrates on Sasima, `npnf202` 21065-21066.
   - Sozomen on Ephrem, `npnf202` 32065-32067.
   - Rufinus's preface, PL 103 40460-40489 ("poposcisti ut hoc opus in Latinum verterem"; "interrogantibus ... monachis ... responsa statuit"). The OCR is damaged, but the card gives it as a report without quotation marks.
   - Gennadius 17, `npnf203` 42466-42471.
   - The creed of 381, `npnf214` 13393-13396.
   - Or. 43.59, `npnf207` 42604-42615.

   Every item in the outline's For the card list is on the card, as are the Leave out items it sends there: Theodoret's lands, Eustathius and the rules, Meletius, Ephrem, Dionysius and the synods of Sp8. The same holds for the card links Links names (Theodoret, Evagrius, Dionysius). `Review.md` sends only its "Later" Do not say line, and the card uses no time word at the rival bishop. `Fresh_Read.md` sends nothing. Changes 1 to 5 above are the only modern dates I found stated without credit.
2. **Nothing else moved.** Every unlisted field is word for word: otherNames, datesNote, placeNote, role, keyWorks, uncertain, sources.ownWords and quotationOriginals.
3. **briefReferences.** The items removed (the monks he went looking for, Nyssa and Sasima, "in praise", Fremantle's year, the council of 787) are things the brief no longer tells. Each remaining entry names something the brief tells. Item [2]'s "legislation" is the reference for the brief's rules sentences. The old brief did not tell it either, so it stays.
4. **Census rules.**
   - I built a scratch copy of the census with this card, the brief as `longDescription`, the 14 `modernWorks` and the three entry-field changes. It passes `node tools/validate-census.mjs` with the full quotation check: 0 errors, and 4 warnings, all on other entries.
   - `tools/list_second_readings.py` finds 3 spans, all carried. Each `modern` matches the brief word for word, and each `printed` is verbatim at its lines.
   - I checked the Greek of Quote 2 by hand: "Τίνα οὖν ἀπονίψεις ; τίνα θεραπεύσεις ; τίνος ἔσχατος ἔσῃ, αὐτὸς καθ᾽ ἑαυτὸν διάγων ;" is verbatim at 72547-72549. The rendering follows it, and "feet" stands only in the sentence before (72546).
   - Every cited file is in `sources`. No audit is named. Spelling is American outside the printed "marvellous". There is no `briefLength`.
5. **"Checked at card".** None. All three quotations run to six words or more.
6. **Not found.** The one claim listed is found (change 6). Nothing clearly wrong is left in.
7. **Entry fields.**
   - `modernWorks` matches the outline's Who tells it, all 14 works. It includes the three moved word for word from `sources.about`. Each note says what the work covers. Names and years match the file headers (Jackson `npnf208` 476; Gwynn `npnf213` 10425). All are pre-1929 and vendored.
   - `why` drops Jackson's "from about 370" and the council of 787, and adds Benedict from the brief.
   - `relationsSummary` drops the bishoprics and the friend's hurt, which the brief no longer tells.
   - `teaser` drops the years and the council.

   `Card_Edits.md` shows `why` with an ellipsis, so the exact new text, with the middle unchanged, is: "Basil was bishop of Caesarea in Cappadocia. His treatise On the Holy Spirit answered those who ranked the Spirit below the Father and the Son. He argued from how the church already prayed. In the sixth century Benedict of Nursia pointed his monks to Basil's rule as an example of good living, and later churches call him "the Great"."

   No `atlasId` question arises.

## Considered, not a FIX

- **`modernWorks` author "Gwynn".** The file gives "John Gwynn" (`npnf213` 10425). The role moves the card's item word for word, so it stays.
- **The 787 council, Sasima and Ephrem on the card's `legacy`.** The brief no longer tells these, but the outline sends each to the card (Cut first 15 and 17; Leave out). The card's legacy is where they belong, so they stay.
