# Card edits: Josephus

Card writer, batch 6, 2026-11-19, per `Card_Prompt.md` and `Brief-Kit/roles/card.md`. The existing card (`Card.existing.json`, the same as the census `card` object for `josephus`) is kept word for word; every field and item it had is unchanged and in its old order. Result: `josephus.card.json`.

## New

1. **`uncertain`**, one item added at the end, by Mark's ruling (Decision-Log, 2026-11-19, "Batch 6 hearts approved; Josephus told with what is held", item 2: "The card notes that modern work is not yet in the Library"):
   - New words: "The Library holds no scholarship on the passage on Jesus later than 1899. The latest is a one-line note by Jean-Baptiste Chabot, the French editor of Michael the Syrian's chronicle, who wrote that a Christian had without doubt added to Josephus's original mention of Jesus. He cites an 1897 article by Théodore Reinach, which the Library does not hold. No held source says where scholars stand now."
   - Evidence: `cic/texts/michael-the-syrian_chronique-tome1-livres-i-vii-fra_chabot1899.txt` lines 11208–11209 ("Il n'est pas douteux que la mention primitive de Josèphe ait été interpolée par un chrétien. Cf. Th. Reinach, Josèphe sur Jésus [Rev.des Etudes juives, t. XXXV, 1897)"), re-read; file header lines 1–4 (Chabot, 1899). `Source_Sheet.md` I9 and section 6 ("nothing held after 1899"; Reinach not held). The first name "Théodore" expands the file's "Th."; no quotation marks are used, so the French is paraphrased.
2. **`sources.about`**: four entries added after the existing four, for files the brief or the new note draws on that the card did not cite:
   - Origen, *Commentary on Matthew* 10.17 in Greek (Lommatzsch), `cic/texts/origen_commentarii-in-evangelium-matthaei-tomus3-grc-lat_lommatzsch1834.txt`: the original of Quote 3 (lines 3731–3733).
   - Origen, *Against Celsus* 1.47, `cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`: Origen on Josephus's John passage, "Origen cited Josephus on John and James" (lines 37929–37942).
   - Jerome, *Illustrious Men* 13 in Latin (Migne PL 23), `cic/texts/jerome_opera-pl23-part1-with-regula-pachomii-lat_migne1883.txt`: "Jerome's Latin ... reads that Jesus was believed to be the Christ" ("credebatur esse Christus", line 50907).
   - Michael the Syrian, ed. and tr. Chabot (1899), `cic/texts/michael-the-syrian_chronique-tome1-livres-i-vii-fra_chabot1899.txt`: the source of the new `uncertain` item.
3. **`briefReferences`** (new key): nine entries, one for each source the brief draws on (War 3, 4 and 5; Life; Antiquities 18 and 20; Suetonius, *Vespasian* 5; Origen, *Against Celsus* 1.47 and *Commentary on Matthew* 10.17; Eusebius, *Church History* 1.9, 1.11 and 3.5; Jerome, *Illustrious Men* 13; McGiffert's notes to 1.11 and 2.23). Quotation marks only around words verbatim in the brief: "treachery", "let others judge of my character.", "a good man", "the brother of Jesus, who was called Christ". Evidence: `Source_Sheet.md` E1–E14, I1–I3, I6–I7; the outline's beats and What came 1–3; Eusebius 3.5 at `npnf201_…xml` 15246–15303 (Chapter V, "The Last Siege of the Jews after Christ").
4. **`quotationOriginals`** (new key; the census card had none). One entry per quoted span in the brief, eight in all. Each is new, so none carries a `secondReading`. All JW lines are in `cic/texts/josephus_works-antiquities-wars-life_whiston1859.txt`, each re-read.
   - Q1. Modern: "I declare it openly: I do not go over to the Romans as a deserter from the Jews, but as a servant sent by you." Printed: "And I protest openly, that I do not go over to the Romans as a deserter of the Jews, but as a minister from thee." JW 110853–110856 (War 3.8).
   - Q2. Modern: "treachery". Printed: "occasioned by my treachery". JW 5342 (Life).
   - Q3. Modern: "a good man". Printed: "for Herod slew him, who was a good man". JW 82091–82092 (Antiquities 18.5).
   - Q4. Modern: "About this time there lived Jesus, a wise man, if it is right to call him a man. For he did astonishing deeds, and taught people who gladly accept the truth." Printed: "Now, there was about this time Jesus, a wise man, if it be lawful to call him a man, for he was a doer of wonderful works,—a teacher of such men as receive the truth with pleasure." JW 81405–81409 (Antiquities 18.3). **Scan fault:** line 81406 reads "call hima / man"; the card gives "him a". `tools/quote_scan_readings.json` has no entry for this file, so the census check will not find "call him a man" in these lines until a reading (scan "hima", reads "him a", line 81406, OCR misread) is listed there. Not added here: that file is outside this task.
   - Q5. Modern: "He was the Christ". Printed: "He was [the] Christ" (Whiston's brackets kept). JW 81411.
   - Q6. Modern: "the brother of Jesus, who was called Christ". Printed: the same. JW 91004–91008 ("Je- / sus" split across blank lines) (Antiquities 20.9).
   - Q7. Modern: "And this is the remarkable thing. He did not accept that our Jesus was the Christ. Yet he still bore witness that James was so upright." Printed (the Greek the rendering is made from): "Καὶ τὸ θαυμαστόν ἐστιν, ὅτι τὸν Ἰησοῦν ἡμῶν οὐ καταδεξάμενος εἶναι Χριστὸν, οὐδὲν ἧττον Ἰακώβῳ δικαιοσύνην ἐμαρτύρησε τοσαύτην." OMG 3731–3733. The scan reads "τὸ 4) ϑαυμαστόν ἔστιν;", "Ἴη- σοῦν", "ἣτ- τον", "᾿Ιαχώβῳ"; the card gives the sheet's reading (I2), with the footnote marker dropped. English printed beside it: "And the wonderful thing is, that, though he did not accept Jesus as Christ, he yet gave testimony that the righteousness of James was so great", `cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` 30627–30629 (it leaves out ἡμῶν, "our").
   - Q8. Modern: "let others judge of my character." Printed: "and let others judge of my character by them as they please". JW 5485–5487 (Life).

## Clearly wrong

None. Re-read against the held sources and the brief: McGiffert's four views and their holders (`npnf201_…xml` EH-ed 9185–9199, per sheet I7); "of late been greatly questioned by many" (JW-ed 138244–138250); Neander and "the common opinion of critics" on the bracketed words naming James, which McGiffert's Greek brackets as the whole phrase "[τὸν ἀδελφὸν ᾽Ιησοῦ τοῦ χριστοῦ λεγομένου, ᾽Ι€κωβος ὄνομα αὐτῷ, καί]" (`npnf201_…xml` 13594–13608); Whiston's discussion of Origen's James line (JW-ed 139654 onward). The brief's "A century and a half later" for Origen does not contradict the card's "more than a century later". Nothing on the card contradicts the brief.

## Not found

None.

## Not added

- `briefLength`: the census card allows no such key (`tools/validate-census.mjs`, `CARD_KEYS`). The brief is 594 words by the profiler, about 4 minutes (`Revision.md`).

## Awaiting second reading

All eight spans are new; `secondReading` is left out of each:
- "I declare it openly: I do not go over to the Romans as a deserter from the Jews, but as a servant sent by you."
- "treachery"
- "a good man"
- "About this time there lived Jesus, a wise man, if it is right to call him a man. For he did astonishing deeds, and taught people who gladly accept the truth."
- "He was the Christ"
- "the brother of Jesus, who was called Christ"
- "And this is the remarkable thing. He did not accept that our Jesus was the Christ. Yet he still bore witness that James was so upright."
- "let others judge of my character."
