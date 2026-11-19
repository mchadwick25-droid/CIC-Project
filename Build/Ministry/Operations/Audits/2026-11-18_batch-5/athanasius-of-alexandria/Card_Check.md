# Card check: Athanasius of Alexandria

Checker, 2026-11-19. Starting card: the census `card` for Athanasius of Alexandria in `cic-website/data/world-census.json` (identical to `Card.existing.json`).

**Verdict: FIX** (nine `briefReferences` changes, two `quotationOriginals` originals).

## 1. Edits justified

- The three old quotations are rightly removed. The brief no longer quotes "begotten, not made", the On the Incarnation 54 line, or Cyril.
- All four new `printed` wordings stand verbatim: `npnf204_athanasius-select-works-letters.xml` 37302-37304, 19679, 58857 and 68810-68811. The `secondReading` is correctly left out of all four (Card_Prompt.md).
- The four new `sources.about` files exist and hold what their references cite: BELL 4693-4706, Jerome at NP3 41678-41682, NP14 26731-26746, BELLU 4675-4679.
- **The books.** The brief now says he "listed the books to be read as God's word". The card agrees. Nowhere does it say "books of the Bible". `briefReferences[26]` keeps the canon (twenty-two and twenty-seven) apart from the books for new believers, and so does the `ownWords` title "the canon list and the books appointed to be read".
- `Card_Edits.md` says "Existing 17 entries kept unchanged". That breaks rule 3. See the FIX list below.

## 2. Nothing else moved

I diffed the card field by field against the starting card. `knownFor`, `role`, `keyWorks`, `legacy`, `uncertain` and `sources.ownWords` are word for word. `sources.about` keeps its first four entries and adds four. `briefReferences[0-16]` are unchanged. Key order is kept.

## 3. References that remain (after the FIXes)

0 Festal Index VIII, Tyre 335. 3 Sozomen II.25 (trimmed). 4 Socrates I.8, deacon. 5 Discourse I.5, Arius's teaching. 6 On the Decrees, the creed (trimmed). 7 Discourse II. 8 On the Incarnation 54 (quotation marks removed). 9 Socrates I.35, Trier (trimmed). 10 Festal Index, the later flights and death. 13 Life, preface. 16 World census, his tradition. 17 Defence of his Flight 24 (trimmed). 18 Historia Acephala (trimmed). 19 Festal Index, 328, 337, Eudaemonis, 366-7. 20 Socrates I.27, refusal. 21 Melitian letter. 22 De Synodis 41. 23 Life, heading and preface. 24 Jerome, Illustrious Men 125. 25 Budge. 26 Festal Letter 39. 27 Gregory 21.37 (trimmed). 28 Trullo canon 2. 29 Documents on Christian Unity.

Naming Syrianus (17), the New River villa (18) and Eudaemonis (19) is kept. Each one identifies a soldier, place or woman that the brief does tell.

## 4. Census rules

- Only allowed keys are used, and there is no `briefLength`.
- There are four quoted spans and four entries.
- Every cited file is in `sources`.
- No audit is named.
- The spelling is American. "Defence" appears only in the edition's title, which the census already uses.
- Quotation marks appear in `briefReferences[6]`, `[8]` and `[15]`, and those words are not in the brief. The FIXes below take all three out.

## 5. Originals

The outline renders Q1 and Q3 from the Greek (Outline 83, 85). The card leaves both originals out, so this is a FIX. Both Greek spans hit scan faults. The validator folds Greek away, so these faults would not fail the check. The readings below still make the file read as the page does, as the Gregory of Nyssa entry already does. These are for `tools/quote_scan_readings.json`; I have not edited it.

```json
{"file": "cic/texts/athanasius_opera-omnia-pg25-grc-lat_migne1857.txt", "lines": "97995", "scan": "χαὶ", "reads": "καὶ", "kind": "OCR misread (χ for κ)"},
{"file": "cic/texts/athanasius_opera-omnia-pg25-grc-lat_migne1857.txt", "lines": "97995", "scan": "προχινδυνεύειν", "reads": "προκινδυνεύειν", "kind": "OCR misread (χ for κ)"},
{"file": "cic/texts/athanasius_opera-omnia-pg25-grc-lat_migne1857.txt", "lines": "97994-97995", "scan": "χα: \nταλεῖψαι", "reads": "καταλεῖψαι", "kind": "OCR misread (χ for κ), with the line-end hyphen read as a colon"},
{"file": "cic/texts/athanasius_opera-omnia-pg26-grc-lat_migne1857.txt", "lines": "113085", "scan": "ἐπιδαλλέτω", "reads": "ἐπιβαλλέτω", "kind": "OCR misread (δ for β)"}
```

## 6. Not found, and anything left in

- `keyWorks`, "by one who had attended him": **leave it.** Robertson's text reads "I was his attendant for a long time" (NP4 31199). His note marks a manuscript variant (NP4 31201-31206). The edition's text supports the words, so they are not wrong.
- This is outside the card, for the brief's owner. The brief says "a young deacon … says Socrates". Socrates I.8 (SZ 2793-2797) says "a deacon" and does not say he was young.

## FIX (exact JSON changes)

1. `briefReferences[1]`: remove. The brief no longer tells the severed hand, Arsenius or magic.
   - Old: `Socrates, Church History I.27, tr. A. C. Zenos: the churches divided over Arius; the charge of the severed hand, Arsenius and magic.`
   - New: (entry removed)
2. `briefReferences[2]`: remove.
   - Old: `Socrates, Church History I.29, tr. Zenos: Arsenius found, led in with his hands under his cloak, and both hands shown. Socrates writes with plain sympathy for Athanasius.`
   - New: (entry removed)
3. `briefReferences[3]`:
   - Old: `Sozomen, Church History II.25, tr. Chester D. Hartranft: the rumor that Athanasius had hidden Arsenius; the council's deposition of him.`
   - New: `Sozomen, Church History II.25, tr. Chester D. Hartranft: the council's deposition of him.`
4. `briefReferences[6]`: the brief no longer quotes these words.
   - Old: `Athanasius, On the Decrees of the Council of Nicaea, Eusebius's letter, ed. Robertson: the creed of Nicaea, "begotten not made".`
   - New: `Athanasius, On the Decrees of the Council of Nicaea, Eusebius's letter, ed. Robertson: the creed of Nicaea.`
5. `briefReferences[8]`: the brief paraphrases this line, so the quotation marks come out.
   - Old: `Athanasius, On the Incarnation 54, ed. Robertson: "For He was made man that we might be made God".`
   - New: `Athanasius, On the Incarnation 54, ed. Robertson: He was made man that we might be made God.`
6. `briefReferences[9]`: the brief gives no reason for Trier.
   - Old: `Socrates, Church History I.35, tr. Zenos: Constantine sends him to Trier over the grain ships, though some said it was for the unity of the church, since he would not hold communion with Arius.`
   - New: `Socrates, Church History I.35, tr. Zenos: Constantine sends him to Trier.`
7. `briefReferences[11]`, `[12]`, `[14]`, `[15]`: remove all four. These are Gregory 21.35 (hypostases), Gregory 21.33 (the confession to the emperor), Jerome's Letter 127.5 (Marcella) and Cyril's letter. The brief tells none of them.
8. `briefReferences[17]`: the brief no longer tells the psalm. It credits the monks alone.
   - Old: `the night in the church, Syrianus's soldiers, the psalm, the people sent home, and the monks and clergy who drew him out past the soldiers.`
   - New: `the night in the church, Syrianus's soldiers, the people sent home, and the monks who drew him out past the soldiers.`
9. `briefReferences[18]`: the brief tells no order in 365.
   - Old: `the order of 365 and his four months at a villa near the New River`
   - New: `his four months at a villa near the New River`
10. `briefReferences[27]`: the brief tells the tears, not old age or the honors.
    - Old: `his death in old age, and the honors at his departure, the object of many tears.`
    - New: `his death, the object of many tears.`
11. `quotationOriginals[0]`: add after `"lines": "37302-37304"`:
    `"original": "Ἐγὼ δὲ ἄλογον ἡγούμενος ἐν τοσαύτῃ συγχύσει καταλεῖψαι τοὺς λαοὺς, καὶ μὴ μᾶλλον προκινδυνεύειν αὐτῶν", "originalFile": "cic/texts/athanasius_opera-omnia-pg25-grc-lat_migne1857.txt", "originalLines": "97994-97996"`
12. `quotationOriginals[3]`: add after `"lines": "68810-68811"`:
    `"original": "Μηδεὶς τούτοις ἐπιβαλλέτω, μηδὲ τούτων ἀφαιρείσθω τι.", "originalFile": "cic/texts/athanasius_opera-omnia-pg26-grc-lat_migne1857.txt", "originalLines": "113085-113086"`

## Applied to the brief (coordinator, 2026-11-18)
- "a young deacon" -> "a deacon": the card check's note that Socrates I.8 (SZ 2793-2797) says only "a deacon". One word removed; nothing added. The card fixes above wait for the batch applier.
