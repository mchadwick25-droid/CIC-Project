# Card check: Nestorius

**Verdict: FIX.** Eight changes: one date, one attribution in three places, three references, one missing quotation entry, and one scan reading.

This is a new card, written by Mark's ruling (item 9). Every field was checked against its evidence in `Card_Edits.md`, and against the entry's existing fields. There is no starting card to diff against.

## 1. Each field against its evidence

Re-read and confirmed:
- **Socrates**: npnf202 20519-20562, 20701-20757, 20898-20921, 20944-20946.
- **Evagrius**: 1527-1541, 1554-1566, 1596-1672, 1686-1690.
- **Driver and Hodgson**: 264-281, 306-345, 356-382, 403-408, 440-447, 2276-2292, 6936-6955, 20262-20266, 20465-20476, 20686-20704, 20729-20733.
- **Hefele**: 1293-1300, 8309-8321.
- **Codex Theodosianus**: 88695-88736.
- **Badger**: 1553-1564, 12303-12309, 16354-16362, 17208-17216, 17525-17530, 18296-18319, 19146-19163.
- **Synodicon**: 32710-32716 (year 60 of the Arabs), 33280-33288.
- **Nau's Barhadbeshabba**: 35940-35955, 36020-36050.

The three points the writer did not re-read:
- **Marius Mercator.** Confirmed, but the lines have drifted. "Non peperit creatura Creatorem, sed peperit hominem Deitatis instrumentum" stands at MM 59089-59091. "Divido naturas, sed conjungo reverentiam" stands at 59097, not 59099 as the Source Sheet and outline have it. The card cites no Mercator lines, so nothing on the card changes.
- **Nau's "légendaire" note.** Confirmed at BB 35949-35950: "La présente rédaction est légendaire." Nau attaches it to Barhadbeshabba's telling of the captivity incident, which Nestorius himself told and Evagrius summarized. It is not attached to the litter story (36025-36031). `legacy.remembered[3]` ("Nau's note on a neighboring story") says this accurately. `uncertain[4]` ("in a legendary telling") is a fair reading of the source sheet's LEGEND tag, so it is left in.
- **Narsai's death date.** Wrong; see FIX 1.

**FIX 1. `legacy.remembered[0]`.** Connolly prints "(+c. 502 a.d.)" (NAR 161), and reckons "his death will fall in 502" (NAR 301). The "c. 413-503" at NAR 3 is the Library's own metadata header, not the printed book.
- Old: `Narsai, a teacher of the Church of the East at Nisibis who died about 503, says`
- New: `Narsai, a teacher of the Church of the East at Nisibis who died about 502, says`

**FIX 2. The date of writing is Bethune-Baker's, not the editors'.** Driver and Hodgson introduce the passage at 310-312 with "In his preface Dr. Bethune-Baker gives the following account of the work". The 451-or-452 reasoning follows at 314-327. The card already credits the next sentence of that same account, the conjecture of 525 to 533, to Bethune-Baker.
- `datesNote`:
  - Old: `The editors of his book think he wrote it in 451 or 452`
  - New: `Bethune-Baker, as the editors of his book report him, thinks he wrote it in 451 or 452`
- `uncertain[3]`:
  - Old: `The editors reckon from references to later events that he wrote it in 451 or 452, though they note that he seems not to know the decisions of Chalcedon.`
  - New: `Bethune-Baker, as the editors report him, reckons from references to later events that he wrote it in 451 or 452, though he notes that Nestorius seems not to know the decisions of Chalcedon.`
- `briefReferences[8]`:
  - Old: `Bazaar of Heracleides, the editors on the date of writing (Driver and Hodgson 314-327)`
  - New: `Bazaar of Heracleides, Bethune-Baker's dating as the editors give it (Driver and Hodgson 314-327)`

No other field contradicts its evidence or the entry's existing fields (`dates`, `placeLabel`, `sourcing`, `voices`, `legacy`, `why`, `floorNote`, `relationsSummary`).

## 3. References

Rule: remove what the brief does not tell. Keep a date that grounds one of the brief's dates: "10 April 428", "435" and "436", and "451 or 452" all stay.

**FIX 3. `briefReferences[1]`.** The brief does not tell Germanicia.
- Old: `sent for from Antioch, a native of Germanicia, ordained 10 April 428;`
- New: `sent for from Antioch, ordained 10 April 428;`

**FIX 4. `briefReferences[7]`.** The brief does not tell the Oasis, the raiders, Panopolis or Elephantine. It tells only that soldiers dragged him to and fro.
- Old: `Evagrius, Church History I.7: his letters to the governor of the Thebaid, the Oasis, desert raiders, the forced journey from Panopolis toward Elephantine, a mangled hand and side.`
- New: `Evagrius, Church History I.7: his letters to the governor of the Thebaid, the forced journey under soldiers, a mangled hand and side.`

**FIX 5. `briefReferences[9]`.** The brief tells only the Syriac translation. It does not tell the one manuscript, Kotchanes, the 1890s or 1910.
- Old: `Driver and Hodgson 328-333, 358-380: the Syriac translation and its date, the one damaged manuscript at Kotchanes. Their note 334-345 and 358-361: noticed in the 1890s; Syriac text and French translation of 1910.`
- New: `Driver and Hodgson 328-333, 358-380: the Syriac translation and its date.`

These stay as they are, besides [1], [7], [8] and [9] as fixed:
- [0] The preface.
- [2] Anastasius names the priest the brief tells.
- [3] The two parties.
- [4] Loofs.
- [5] The council.
- [6] The law of 435.
- [10] Badger and Abdisho.
- [11] The census.

## 4. Census rules

- **Keys.** Only allowed keys, and no `briefLength`.
- **Files.** Every cited file exists and is in `sources`.
- **Quotation marks and names.** The card's prose has no quotation marks, and names no audit, review or ruling.
- **Wordings.** Each English `printed` stands at its lines.
- **Second readings.** None has been given yet; that is expected at step 7.

**FIX 6. One entry is missing.** The brief quotes "Mother of God" three times. The card's one entry, Bazaar 6936, fits the narrator's use in paragraph 2 and Nestorius's two parties in paragraph 4. It does not fit the third span: "Socrates also says he backed a priest who preached against calling Mary 'Mother of God'". That is Socrates's report, and his translator prints the Greek title. Add this entry after the "the earth purged of heretics" entry:

```json
{
  "modern": "Mother of God",
  "printed": "Theotocos",
  "work": "Socrates, Church History VII.32, English translation (Nicene and Post-Nicene Fathers)",
  "file": "cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml",
  "lines": "20705",
  "uncertain": "The translation keeps the Greek title, Theotocos; the brief renders it Mother of God."
}
```

**FIX 7. A scan fault in the sermon's Greek.** The writer copied the scan letter for letter, including the misread "τεροσχύνησιν". The same scan misreads προσκυνῶ as "γιυροσχυνῶ" two lines up (14309). Loofs prints προσκύνησιν, as the outline has it, and Mercator's Latin "reverentiam" agrees. The validator's folding strips Greek letters, so it cannot catch this.

Change `quotationOriginals[5].printed`:
- Old: `ἀχώριστος τοῦ φαινομένου ϑεός, διὰ τοῦτο τοῦ μὴ χωριζομένου τὴν τιμὴν οὐ χωρίζω. χωρίζω τὰς φύσεις, ἀλλ᾽ ἑνῶ τὴν τεροσχύνησιν.`
- New: `ἀχώριστος τοῦ φαινομένου ϑεός, διὰ τοῦτο τοῦ μὴ χωριζομένου τὴν τιμὴν οὐ χωρίζω. χωρίζω τὰς φύσεις, ἀλλ᾽ ἑνῶ τὴν προσκύνησιν.`

Add this entry to `tools/quote_scan_readings.json`:

```json
{
  "file": "cic/texts/nestorius_nestoriana-fragmenta-grc-lat-deu_loofs1905.txt",
  "lines": "14312",
  "scan": "τεροσχύνησιν",
  "reads": "προσκύνησιν",
  "kind": "OCR misread"
}
```

Left as is: the comma after ϑεός. The outline has a raised dot there, and this scan never produces a raised dot. But the printed page is not held as an image, so I cannot confirm the reading.

**FIX 8, in the brief, not the card.** The sermon rendering spells "honour", which is British. The card's `modern` must match the brief, so the change goes in the brief ("honor"), and the card's `modern` then follows it.

## 5. Originals

Pass. The sermon is carried in its Greek (Loofs). The Bazaar's Syriac is not held. The card says that Nau's French was used as a check, not as the original. Socrates's Greek (Hussey) is listed in `sources`, but the outline does not render from it.

## 6. Not found, and left in

- **No birth year**: upheld. The sheet has none.
- **"perhaps a century later"**: the writer flagged it, and it is a matter for the brief. The card's dates (about 535, or 525 to 533) are correct to their sources.
- **"Thomas"**: Badger prints "Tooma" (BAD 17529), and the card gives the English form of the name. That is acceptable.
- Babai's Life of George is rightly left out, by ruling. Nothing else clearly wrong was left in.
