# Card edits: Justin Martyr

Card: `justin-martyr.card.json`, built from `justin-martyr.original.card.json`. Every existing field is kept word for word and in its order. Brief: `justin-martyr.brief.txt` (470 words).

## New

1. **`briefLength`** (added after `role`). Old: none. New: "about 3 minutes 10 seconds". Evidence: the brief is 470 words (`wc -w`), at the kit's 150 words a minute (`Brief-Kit/roles/writer.md` line 8) = 3 min 8 s.

2. **`briefReferences`** (added). Old: none. New: fourteen references, one per source the brief draws on: First Apology 1, 2, 4, 26, 46; Dialogue 1, 2, 3, 7, 8, 16, 142; Second Apology 2, 8, 12; the Martyrdom of Justin; Eusebius IV.16 with McGiffert's note; Irenaeus, Against Heresies I.28.1 and IV.6.2; Hippolytus, Refutation VIII (ANF ch. 9); Tatian, Address 18–19; Tertullian, Against the Valentinians 5. Evidence, re-read in `cic/texts/`: R1 72–75, 124–126, 729–731, 1230–1234; AR 87–89, 139–141, 163–169, 175–180, 399–401, 788–791, 6603–6605; R2 136–139 (ch. 2), 273–276 (ch. 8), 368–370 (ch. 12); GEB 1300–1303, 1347–1353, 1423–1426, 1433–1438; EUS 22420–22422, 23764–23766, 23774–23782; ANF1 33663–33667, 44907–44918; ANF5 12996–13006 (Book VIII, ch. IX); TAT 7956–7960; ANF2 6526–6533, 6550–6556; ANF3 43161–43163.

3. **`quotationOriginals`** (added). Old: none. New: three entries, the brief's modern wording exactly, with the Greek the rendering was made from, verbatim as the file stands (OCR kept):
   - "At once a fire was lit in my soul. … That is how, and why, I am a philosopher." / Dialogue 8.1–2, `justin-martyr_dialogue-with-trypho-grc_archambault1909.txt` 429–435. Note: ANF English (anf01 17853–17857) prints "safe and profitable" for ἀσφαλῆ τε καὶ σύμφορον.
   - "So you suppose that you will go up into the heavens, to receive some reward?" / Martyrdom V.3, `acta-martyrum-selecta_gebhardt1902.txt` 1410–1411. Note: OCR "ἀναβή on eis" for ἀναβήσῃ εἰς; Dods's English, anf01 29371–29373.
   - "I do not suppose it. I know it, and I am fully sure of it." / Martyrdom V.3, `acta-martyrum-selecta_gebhardt1902.txt` 1420–1421. Note: Dods's English, anf01 29373–29374.
   No `secondReading` field: no second rendering reading is recorded in this folder.

## Clearly wrong

None. Every existing statement was checked and holds:
- "Flavia Neapolis in Palestine": anf01 13965–13969 ("natives of Flavia Neapolis in Palestine").
- Eusebius, "a genuine lover of the true philosophy": EUS 21864–21865.
- Crescens known only from Justin and Tatian, his enemies; not named in the trial account: EUS 23782–23787.
- Two traditions; McGiffert favours Marcus Aurelius; Rusticus prefect in 163: EUS 23775–23780.
- Dods: date and author unknown, "most trustworthy of the Martyria", hemlock "an absurd addition": anf01 29216–29220 (the translator's notice, introduced as such at 29213–29214; Dods named at 29257).
- Nothing in the card contradicts the brief.

## Not found

None.
