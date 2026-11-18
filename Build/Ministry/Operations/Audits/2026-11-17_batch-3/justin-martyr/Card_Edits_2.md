# Card edits 2: Justin Martyr

Card: `justin-martyr.card.json`, rebuilt from the census's current `card` object for `justin-martyr` (`cic-website/data/world-census.json`). Brief: `justin-martyr.brief.txt` (the rewritten brief). Every field not listed below is kept word for word and in its order. `briefLength` is left out (the census check does not allow it), so the old batch card's `briefLength` is gone.

## New

1. **`sources.about`**: one item added at the end, because two of the brief's quotations now cite Franchi's text. New: "The Martyrdom of Justin and his companions, Greek, Franchi de' Cavalieri's text, in Ausgewählte Märtyrerakten (ed. Rudolf Knopf and Gustav Krüger)", author Unknown, date 1929, Greek, `cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt`. Evidence: Source_Sheet H7 (KK 1613–1769, editor's note 1793–1812); Outline, Quote 3.

2. **`briefReferences`**: the fourteen old references replaced by fifteen for what the new brief draws on, each with file and lines: First Apology 1 (R1 68–75; ANF1 13965–13969); McGiffert's note (EUS 22420–22422); the lodging above a bath-house (GEB 1347–1354); Second Apology 2 (R2 136–158) and First Apology 4 (R1 124–126); First Apology 46 (R1 1230–1234; ANF1 15684–15692); First Apology 61 and 67 (R1 1577–1579, 1759–1785; ANF1 16502–16534); Dialogue 2, 3, 7, 8 (AR 139–169, 175–180, 399–435); Dialogue 1, 16, 142 (AR 87–89, 788–791, 6589–6607); the trial (KK 1754–1757; GEB 1300–1441; ANF1 29266–29406; Dods ANF1 29216–29218); Eusebius IV.16 with McGiffert (EUS 23775–23780); Irenaeus IV.6.2 (ANF1 44907–44918) and First Apology 26 (R1 729–731); Irenaeus I.28.1 (ANF1 33663–33672) and Hippolytus (ANF5 13004–13006); Tatian 42 and 18–19 (ANF2 7460–7464, 6526–6533, 6550–6556; TAT 7956–7960, 8105–8111); Eusebius IV.29 (EUS 26424–26426, 26433) and the Doctrine of Addai (ADD 65); Tertullian (ANF3 43161–43163). Dropped: the Second Apology 8 (Crescens) and 12 references, which the new brief no longer draws on. No quotation marks are used inside them. Each cited line was re-opened.

3. **`quotationOriginals`**: rebuilt to match the brief's six quoted spans.
   - Removed (their `modern` is no longer quoted in the brief): the full Dialogue 8.1–2 passage ("At once a fire was lit in my soul. … I am a philosopher."); "So you suppose … to receive some reward?" (Gebhardt); "I do not suppose it. I know it, and I am fully sure of it." (Gebhardt).
   - Added "word": printed λόγον ὄντα, R1 1231; English "He is the Word", ANF1 15685. secondReading same (S3-22).
   - Added "reason": printed μετὰ λόγου, R1 1232; English, the ANF note "“with reason,” or “the Word.”", ANF1 15687–15688. secondReading same (S3-22; its verdict judges "word" and "reason" together).
   - Added the First Apology 46 quotation (three sentences): printed R1 1230–1233; English ANF1 15684–15692. secondReading same (S3-23). Note in `uncertain`: S3-23 covered only the first two sentences (its request stopped before Καὶ οἱ μετὰ λόγου βιώσαντες); the third sentence had no blind reading of its own beyond S3-22's sense of μετὰ λόγου. Also noted: the file's οἷ for οὗ, ANF "lived reasonably" and "atheists".
   - Added "the only philosophy that is sure and useful": printed ταύτην μόνην εὕρισκον φιλοσοφίαν ἀσφαλῆ τε καὶ σύμφορον, AR 431–432; English ANF1 17856. secondReading same, carried from the removed full-passage entry (Second_Readings.md, justin-martyr Q1, SAME), of which this phrase is part; the ἀσφαλῆ note kept.
   - Added Rusticus's question, "… some good rewards?": printed KK 1754–1756 (OCR as it stands), lines as corrected in Second_Readings_3.md; English ANF1 29371–29372. secondReading same (S3-24). Note: χρηστάς ("good") lacking in Otto's text, GEB 1410–1411.
   - Added Justin's answer, "I know it for certain …": printed KK 1756–1757, lines as corrected; English ANF1 29373–29374. secondReading same (S3-25). Note: ἀκριβῶς ("for certain") lacking in Otto's text, GEB 1420–1421.

## Clearly wrong

None. Nothing in the card contradicts the new brief or a held source. "Flavia Neapolis in Palestine" (placeNote) stands in ANF1 13965–13969 and does not contradict the brief's "a Roman town in Samaria".

## Not found

None.

## For the coordinator

The First Apology 46 entry carries "same" from S3-23, whose blind reading stopped before its third sentence. If a verdict on the whole span is wanted, that sentence needs its own second reading.
