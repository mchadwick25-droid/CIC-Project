# Card edits: John Chrysostom

Card: `john-chrysostom.card.json`. Everything else is word for word from `Card.existing.json`. It passes `tools/validate-census.mjs` (checked with the card in the census entry, copy outside the repo).

## Correction

1. briefReferences, Diodore line.
   - Old: "Socrates, Church History VI.3, tr. Zenos: John's training under Diodore, who kept to the literal sense of Scripture."
   - New: "Sozomen, Church History VIII.2, tr. Hartranft: John's training under Diodore. Socrates, Church History VI.3, tr. Zenos: Diodore's literal sense of Scripture."
   - Evidence: Socrates VI.3 says Theodore and Maximus, not John, went under Diodorus (`cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml` 17167-17170) and gives the literal sense of Diodorus's writings (17182-17185). John's teachers Carterius and Diodorus are in Sozomen VIII.2 (42693-42695); Zenos's note on literal sense is 17172-17178. The review's suggested wording ("Zenos's note and Prevost's preface") does not hold: the Diodorus passage in `cic/texts/npnf110_chrysostom-homilies-matthew.xml` (lines 729-732) is in M. B. Riddle's Introductory Essay, and Prevost only translated the homilies.

## New

2. briefReferences, inserted after the Homily 50 line: "Homilies on Matthew, Preface to the Oxford Edition, by C. Marriott: the homilies were delivered at Antioch."
   - Evidence: brief sentence "There, in a sermon on Matthew, he told his listeners..."; npnf110 lines 535-536, "were undoubtedly delivered at Antioch".
3. sources.about, added: Sozomen, "Church History, Book 8, chapter 2", English translation, npnf202 file (for edit 1).

## Not changed

- quotationOriginals: the brief's only quotation, "Glory to God for all things.", is unchanged; printed text re-read at the cited lines by the validator.
- No briefLength, no connections.

## Not found / noted

- legacy.remembered, third item says John was "restored to communion in the thirty-fifth year after his deposition". Socrates VII.45 says "after his deposition" at 21465 and "after his death" at 21478. Left in place.

## Second pass (2026-11-23)

- Checker FIX 1 (quotationOriginals[0].printed, "Glory to God for all things." to "Glory to God for all things;"): applied word for word.
- Scan readings to add: none (the checker lists none).
- Outline items added: none. There is no Outline.md for this story, so step 2 was not done. Review.md and Fresh_Read.md were not mined for card items; skipped for that reason.
- Validator (`--skip-quotes`, scratch census copy with this card in place): no errors for john-chrysostom.

## Third pass: what it was about (2026-11-23)

Written to `Card.pass2.json`, copied from `john-chrysostom.card.json`; every field not listed here is word for word. No new quotation: the brief's only quoted span, "Glory to God for all things", is unchanged, so `quotationOriginals` is unchanged.

### New references (briefReferences)

1. After the VI.5 rebuke entry, added: "Socrates, Church History VI.5, tr. Zenos: John's rebukes reaching the Gothic general Gainas, who asked for a church in the city for the Arians, told with Socrates's "it is said". Socrates, Church History I.5, tr. Zenos: the Arian teaching that the Son had a beginning." Evidence: brief sentences on Gainas and the Arians; npnf202 XML 17368-17373 and 2093-2095 (re-read).
2. Added: Socrates VI.7 and VI.9, the monks driven out, the quarrel over God's form, their coming to John, the false report, Theophilus's resolve. Evidence: brief sentences on the monks; npnf202 17578-17592, 17655-17695, 17790-17843 (re-read). The source says the false report was that John "admitted them to a participation of the mysteries"; the reference says "admitted them to the mysteries", in line with the brief's "given them the Eucharist".
3. Added: Photius, Library, Codex 59, tr. Freese: the charges laid at the Oak (sold church property, reviled the clergy, struck Memnon, ate gluttonously alone). Evidence: brief sentence "His accusers charged..."; `cic/texts/photius_library-v1_freese1920.txt` 3872, 3875, 3929, 3933 (re-read).
4. After the VI.15-16 entry, added: Socrates VI.18, the statue and games, John's mockery, Eudoxia's taking it as aimed at her, the second council's ground, the emperor's decree. Evidence: brief paragraph on the games; npnf202 18427-18444, 18468-18473, 18486-18489 (re-read).

### Removed or trimmed references (no longer told)

5. VI.3: "John a native of Antioch in Syria." -> "John a native of Antioch." The brief now says "from Antioch".
6. VI.2: "the court's choice of John in 398; Eutropius making..." -> "Eutropius making Theophilus of Alexandria ordain John in 398." The court's choice is cut.
7. Palladius: "Palladius bishop of Helenopolis; the bishop's spending moved to the hospital and more hospitals built." -> "the bishop's spending moved to the hospital." The brief no longer says Helenopolis or more hospitals.
8. VI.5 rebuke entry: "..., the Eutropius sermon making it worse; Theophilus's grudge over his own favorite." -> "...; Theophilus's grudge over his favorite." Both phrases are cut from the brief.
9. Pityus: "toward Pityus on the Black Sea" -> "toward Pityus". Cut in the brief.

### Outline items sent to the card

10. uncertain (second item): Eutropius made Theophilus ordain John by showing him the memorials of charges and bidding him choose between ordaining John and a trial (outline item 6). Evidence: Socrates VI.2, 17097-17108.
11. uncertain: Theophilus's resolve after the false report; the Origen letters as a cover for revenge on the monks; no mention of Origen at the Oak (item 9), credited to Socrates. Evidence: 17655-17695 (revenge), 17790-17843 (false report and Origen letters), 18271-18272.
12. uncertain: the charges at the Oak known from the minutes as Photius summarizes them, written more than four centuries later; he calls the synod unlawfully summoned and John a holy man; Socrates calls many charges ridiculous; nothing held proves them (item 10). Evidence: Photius 3843, 3939; Socrates 18271-18274.
13. uncertain: Socrates says deposed only for refusing; the minutes record the first and second counts examined, then a unanimous vote of forty-five (item 11). Evidence: Socrates 18293-18297; Photius 3946, 4027-4031.
14. uncertain: the sermon against women, taken as aimed at Eudoxia, her complaint and the emperor's authorization of Theophilus's synod (item 12). Evidence: Socrates 18239-18249.
15. uncertain: John's reply at the second council that the rule was an Arian canon from the Antioch council against Athanasius (item 15). Evidence: Socrates 18474-18480.
16. legacy.traces: the fire set by some Johannites on the day of his departure, spreading to the senate-house (item 17). Evidence: Socrates 18497-18500.
17. sources.about: added Photius, Library, Codex 59, `cic/texts/photius_library-v1_freese1920.txt` (item 10; the file is cited by edits 3 and 12).

### Skipped

- Items 1-5, 7, 8, 13 (brief explanations already covered by existing references or fields), 14 (Herodias sermon, left out with no card home), 16, 18: no card instruction.
- Item 15's "Antiochene way" clause: the existing Diodore and census references already carry it.
- The outline's "Socrates is no friend of Theophilus" (VI.13, 18122-18125): those lines do not say it; not added.
- Item 2's aim of the law (revenge): the outline gives it no card instruction.

### Validator

`node tools/validate-census.mjs --skip-quotes` on a scratch census copy with this card: 0 errors (4 warnings, none for this entry).

## Card check applied (2026-11-23)

`Card_Check_About.md` (FIX, three changes), applied word for word: the Oak minutes `uncertain` item ("say the first and second counts were examined" → "say several of the counts were examined, beginning with the first and second,"); the Theophilus motive `uncertain` item ("revenge on the monks." → "revenge on Isidore and Dioscorus and the removal of John."); `sources.about`: the Socrates Book 1, chapter 5 entry inserted after Book 7, chapter 45.

## Fourth pass: no modern opinion (2026-11-23)

Starting card kept unchanged as `Card.pass3.json`. Evidence for the sent-to-card items: `Outline.md` "Modern pass", `Modern_Pass.md`, `Fresh_Read_Modern.md`; each cited line re-read.

### uncertain (four items added at the end)

1. Antiochene school: new item crediting Zenos's note (`npnf202` 17173-17179, "the corner-stone of the Antiochian system of interpretation") and the Oxford preface to Matthew (`npnf110` 730-732, "reckoned the leader of the so-called Antiochian school of exegetes"), marked a modern judgment. Evidence: the brief no longer says "in the Antiochene way" (diff of `brief.v4.txt`).
2. Oak and march dates: new item. 403 from Freese's note citing Hefele (Photius 3862-3864) and Moore's table of dates (Palladius 678); June 407 for the removal to Pityus from Moore's table (Palladius 706); Palladius gives no year for the march. Evidence: the brief no longer says "In 403" and puts 407 on the death (Socrates VI.21, `npnf202` 18609-18612).
3. Matthew homilies at Antioch: new item, the Oxford editor's "undoubtedly delivered at Antioch" and "probably in the latter part of the time during which he preached as a Presbyter" (`npnf110` 534-536), marked modern. Evidence: the brief no longer says "There".
4. Author of the Dialogue: new item, Moore's introduction: anonymous as it stands, "generally attributed to Palladius, Bishop of Helenopolis" (Palladius 729-731), nothing but the title suggests the speaker is Palladius (753-756), another Palladius proposed by Bigot (894-903). Evidence: the brief no longer says "who stood by John to the end".

### briefReferences

5. Removed "Homilies on Matthew, Preface to the Oxford Edition, by C. Marriott: the homilies were delivered at Antioch." The brief no longer places the sermon.
6. "the Oak near Chalcedon in 403, John refusing" -> "the Oak near Chalcedon, John refusing". Brief has no year.
7. "the second council that silenced him" -> "the second council that condemned him". Brief: "condemned".
8. Palladius entry: "in 407 soldiers hurrying him" -> "soldiers hurrying him"; added "Socrates, Church History VI.21, tr. Zenos: his death on the way, on the 14th of September in the seventh consulate of Honorius." Evidence: `npnf202` 18609-18612. The file is already in `sources.about` (Church History, Book 6).
9. Removed "World census, Antiochene Exegetical Christianity (Chrysostom-centered): his tradition." The brief no longer names the tradition.

### Unchanged

- `quotationOriginals`: one span in the brief, "Glory to God for all things.", unchanged, entry word for word.
- The Diodore reference already cites Socrates VI.3 for the literal sense.
- `sources`: no change. Not found: nothing new.

### Validator

`node tools/validate-census.mjs --skip-quotes` on a scratch census with this card and brief in place: 0 errors (4 warnings, none for this entry).
