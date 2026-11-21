# Card check: Anatolius of Alexandria and Laodicea

Batch 7, 2026-11-20. Independent checker; I wrote neither the brief nor the card. Files are under `cic/texts/` unless noted.

**Verdict: FIX** (7 changes, below).

## 1. Each edit justified

I opened every cited range.

- **quotationOriginals [0]** (the speech): McGiffert, npnf201 42736-42739. Justified.
- **quotationOriginals [1]** (Wilfrid): Giles 8135-8141 and Plummer 21583-21587. Justified.
- **legacy.traces**, three new items:
  - Bede's leap-year letter: Giles 15510-15513.
  - Socrates on the equinox rule: npnf202 41694-41704, with note 1556 "Extracts from the canons of Anatolius".
  - Elias of Nisibis: 41058-41065.
  - All three justified.
- **legacy.remembered**, two new items:
  - The Bollandists' note (69809-69811) is justified.
  - Bar Hebraeus (4958-4965) needs FIX 2. The "Eusebius" the chronicle pairs with Anatolius is "Eusebius, Laodiceae episcopus" (4960-4961), the deacon. Everywhere else on this card, a bare "Eusebius" means the historian, so a reader would take it as him.
- **uncertain**, twelve new items. I read each against its lines:
  - Rufinus: 12530-12545, 12650-12658.
  - Duchesne: 17773-17796, 18885-18888.
  - Harnack: Chronologie 4766-4874 and Mission 1401-1405.
  - Hefele: 20636-20668.
  - Bardy: 10723-10729, 11406-11413.
  - Bucherius: PL67 36039-36046.
  - Guidi: 3718-3724.
  - McGiffert: 40903-40915, 41937-41938, 42673-42676.
  - Salmond: anf06 14730.
  - Ceolfrid: Giles 14738-14743.
  - The Latin book: anf06 15009-15012.
  - Giles 5749-5757 and 8117-8121.

  All hold except one. In **uncertain[9]** (FIX 1), Loofs does not say that Anatolius left before the fall. He says the most likely view is that "ihre Reise nach Syrien, zum mindesten die des Eusebius" came before it (13983-13985), that is, their journey, or at least the deacon's. The card drops his hedge.
- **sources.about**, fourteen added: each is cited by a new item or entry. Justified.

## 2. Nothing else moved

I diffed the card against `Card.existing.json` field by field. Every starting field is word for word and in order. New items are only appended, to `legacy.traces` (3), `legacy.remembered` (2), `uncertain` (12) and `sources.about` (14). `briefReferences` and `quotationOriginals` are new.

## 3. References

Seven parts name things the brief does not tell (FIX 3 to 7):

- Alexandrian by birth, and the school of Aristotle: the brief has neither.
- The deacon's name, Eusebius: the brief says "a deacon" and "that same deacon".
- Theotecnus: the brief says "its bishop".
- "the new moon that begins" the cycle: the brief has only the table of nineteen years.
- Stephen: the brief says "another man".

After the fixes, these entries remain:

- [0] VII.32.6, learning
- [1] VII.32.7-9, the siege
- [2] VII.32.9-11, the council and the exodus
- [3] VII.32.12 and 21, Caesarea and Laodicea
- [4] VII.29.1, the synod
- [5] VII.32.14-19, the Easter rule
- [6] McGiffert and Hefele on the cycle
- [7] VII.32.21-22, the end
- [8] Bede III.25
- [9] the Latin Paschal Canon
- [10] McGiffert and Harnack on the Latin book
- [11] Loofs, Harnack, Hefele and the sources that differ
- [12] the census tradition

## 4. Census rules

- Keys are allowed, and there is no `briefLength`.
- There are two entries for the brief's two quoted spans, and no extra.
- Both `printed` wordings stand at their lines. The `original` stands at 21583-21587, where fold drops the stray mark before "Christi".
- All three cited files are in `sources`.
- No quotation marks in `briefReferences`. No audit named. American spelling.
- Neither entry has a `secondReading` yet. Both wait for step 7, and the census check requires one before release.

## 5. Originals, and the ruling on each printed form

- **[0], Eusebius's Greek (Schwartz 12485-12492): LEAVE OUT, as the card has it.** I checked it by hand. It has these faults:
  - "xci" for καί (12486, 12487, 12491).
  - "ποϑ᾽" (12486).
  - "βαδίζειν»" (12488).

  No held print confirms a reading. Schwartz holds the only Greek of Book VII, and Rufinus paraphrases. The outline says the same: "the card prints the English alone". So leaving it out is not a FIX under check 5.

  Where the rendering follows the Greek ("small children" for νήπια, "surplus" for περιττούς), the English says the same. No `uncertain` note is needed.
- **[1], Plummer's Latin (21583-21587): KEEP as it stands.** "sed quid uobis cum illo ... contemnitis." is clean. The one mark before "Christi" (21586) is a stray mark, plainly no part of the text.

  The first sentence (21581-21582, "Constat ... dignissimum") is clean too, apart from "Repiyoi". That is the scan of a side-note, plainly no part of the text: compare "Replyof" at 21561. Under the ruling it could stand, but the census check would need a listed scan reading in `tools/quote_scan_readings.json` to drop it. The card's shorter original is right as it stands. Adding the sentence is the coordinator's choice, together with that listing.

## 6. "Not found" and anything left wrong

The card claims none not found, and I found none beyond FIX 1 and FIX 2.

## Fixes

**FIX 1.** `uncertain[9]`
- Old: `On the year of the siege, McGiffert notes that Eusebius's Chronicle puts it in 272. Salmond gives 262. Harnack ties it to the revolt of Aemilian in the time of Gallienus. Loofs thinks the palace quarter fell probably in 270, and that Anatolius left for Syria before it fell.`
- New: `On the year of the siege, McGiffert notes that Eusebius's Chronicle puts it in 272. Salmond gives 262. Harnack ties it to the revolt of Aemilian in the time of Gallienus. Loofs thinks the palace quarter fell probably in 270, and that the journey to Syria, at least the deacon Eusebius's, most likely came before it fell.`

**FIX 2.** `legacy.remembered[3]`
- Old: `Bar Hebraeus, in the thirteenth century, calls Eusebius and Anatolius, both Alexandrians, true leaders in sacred and secular learning.`
- New: `Bar Hebraeus, in the thirteenth century, calls Eusebius, bishop of Laodicea, and Anatolius, both Alexandrians, true leaders in sacred and secular learning.`

**FIX 3.** `briefReferences[0]`
- Old: `Church History VII.32.6, tr. Arthur McGiffert: Anatolius an Alexandrian by birth, first among the ablest men of his time in learning; the report that the citizens asked him to found a school of Aristotle's philosophy.`
- New: `Church History VII.32.6, tr. Arthur McGiffert: Anatolius first among the ablest men of his time in learning.`

**FIX 4.** `briefReferences[1]`
- Old: `Church History VII.32.7-9, with McGiffert's note on the palace quarter: the siege, told from report; the bread failing; the deacon Eusebius, outside the lines, winning a promise of safety from the Roman general.`
- New: `Church History VII.32.7-9, with McGiffert's note on the palace quarter: the siege, told from report; the bread failing; the deacon outside the lines winning a promise of safety from the Roman general.`

**FIX 5.** `briefReferences[3]`
- Old: `Church History VII.32.12 and 21: Theotecnus of Caesarea in Palestine making him a bishop to succeed him; the synod at Antioch calling him; the believers at Laodicea keeping him after the deacon Eusebius, their bishop, had died.`
- New: `Church History VII.32.12 and 21: the bishop of Caesarea in Palestine making him a bishop to succeed him; the synod at Antioch calling him; the believers at Laodicea keeping him after the deacon, their bishop, had died.`

**FIX 6.** `briefReferences[5]`
- Old: `Church History VII.32.14-19, the extract from his Paschal Canons: the first month not to begin before the spring equinox; the mistake of those who begin it earlier; the rule known to the Jews of old, with their writers cited; the new moon that begins the nineteen-year cycle.`
- New: `Church History VII.32.14-19, the extract from his Paschal Canons: the first month not to begin before the spring equinox; the mistake of those who begin it earlier; the rule known to the Jews of old, with their writers cited; the nineteen-year cycle.`

**FIX 7.** `briefReferences[7]`
- Old: `Church History VII.32.21-22: the last bishop of Laodicea before the persecution was Stephen. No held source tells how Anatolius died.`
- New: `Church History VII.32.21-22: another man bishop of Laodicea before the persecution. No held source tells how Anatolius died.`
