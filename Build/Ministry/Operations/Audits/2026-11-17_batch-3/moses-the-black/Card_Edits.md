# Card edits: Moses the Black

Every field of `moses-the-black.original.card.json` is kept word for word and in its order. The only changes are additions. The card has no corrections.

## New

1. **`briefLength`** (added after `role`). Old: none. New: "about 2 minutes 10 seconds". Evidence: `moses-the-black.brief.txt` is 331 words (`wc -w`). That is about 2:10 at the pace the finished cards use (354 words is "about 2 minutes 20 seconds").
2. **`sources.about`, new item: the Ethiopian Synaxarium.** Old: none. New: "The Book of the Saints of the Ethiopian Church, 24 Sane (tr. E. A. Wallis Budge)", `cic/texts/ethiopian-synaxarium_book-of-saints-ethiopian-church-v2-v4-microform_budge1928.txt`, 1928. Evidence: the brief's sentence "a later Ethiopian tradition remembers raiders killing him there". The file says "On this day Saint Abba moses the Black became a martyr" (37094) and "the Barbanans came and killed him" (37183–37184, OCR).
3. **`briefReferences`** (new list, nine items). Each was re-read at its lines:
   - LH 19, the ethnicity, the master, the murder, the robber band and the Nile: `palladius_lausiac-history_clarke1918.txt` 333 ("an Ethiopian by race and black", "he was said to go even the length of murder", "they used to say that he was leader", "one night with his dogs impeded him", "grasped his sword in his mouth").
   - LH 19, the turn and the four robbers: 335 ("conscience-stricken as a result of one of his adventures", "recognized that it was Moses the erstwhile renowned and far-famed robber", "renounced the world because of his conversion").
   - LH 19, the long fight: 337 ("old habit of sexual incontinence", "six years", "taking their water-pots secretly", "the demon ... gave him a blow", "Come to Communion", "some two months later, he said that he no longer suffered anything").
   - LH 19, the priest, seventy-five and seventy disciples: 337.
   - Clarke's notes for "the late 300s": 197 with note 713 ("I. e. 388"), and 657 ("I.e. 419-420").
   - Saying 55: `anan-isho_paradise-v2-sayings_budge1907.txt` 164 ("treated him with contumely", "Why doth this Ethiopian come and go in our midst?", "held his peace").
   - Saying 477: 1028 ("wishing to try him", "drove him out", "Get outside, O Ethiopian", "O thou whose skin is dark and black").
   - Ethiopian Synaxarium, 24 Sane: 37094 and 37163–37184.
   - The census, desert monasticism: `Outline.md` Setting, *Tradition*, which cites the census entry for "the desert fathers".
4. **`quotationOriginals`** (new list, three items). The modern wording is the brief's. The printed wording is verbatim from the file and lines. All three were re-read in the file.
   - "I am not allowed to hurt anyone. So what do you tell me to do with these?" The brief breaks this quotation around "he told the brothers". Printed: "Since I am not allowed to hurt anyone, what do you bid me do with these?" (LH 335).
   - "If a man so great and powerful in robbery has feared God, why should we put off our salvation?" The brief breaks it around "they said". Printed: "If he who was so great and powerful in brigandage has feared God, why should we defer our salvation?" (LH 335).
   - "Get outside, O Ethiopian." Printed: "Get outside, O Ethiopian" (PAR2 1028).
   - **`secondReading` verdicts are the card writer's.** The folder has no `Second_Readings.md`, and neither the Greek nor the Syriac original is held. The verdicts ("minor", "minor", "same") come from comparing each rendering with Clarke's or Budge's English. The checker should confirm them.

`node tools/validate-census.mjs` was run on the census as it stands, which does not include this card: 0 errors. The quotation entries were checked against the brief with the validator's own folding rule. Every quotation in the brief has an entry, and every printed wording stands in its cited lines.

## Checked, left alone

- `uncertain`: "John Cassian's Abbot Moses spent his boyhood in the Thebaid near Antony". This is supported. Abbot Moses speaks in Conference II.ii: "while I was still a boy, in the region of Thebaid, where the blessed Antony lived" (`npnf211_sulpitius-severus-vincent-lerins-cassian.xml` 27197–27199). Gibson's suggestion that he may be Moses the Libyan is at 24272–24276.
- `datesNote`: "in 419 or 420". Clarke's note reads "I.e. 419-420" (LH 657). This is a fair reading, not a contradiction.
- `knownFor`: "driven out for robbery". LH 333 gives "because of his immorality and brigandage". The card is partial but not contradicted.
- `uncertain`: "No source used here names his master, his family, or the bishop who made him a priest". This still holds now that the Ethiopian Synaxarium is cited. That entry gives his master as "a man who worshipped the sun" and speaks of "the archbishop", but names neither (37101–37147).
- `uncertain`: the barbarians saying, which "does not name him the Ethiopian". This matches PAR2 1464. The brief's Ethiopian tradition is a different witness, so the card does not contradict it.
- `legacy.remembered` quotes: Palladius, "This was the manner of life of Moses the Ethiopian" (LH 337), and Sozomen, "he died at the age of seventy-five, leaving behind him numerous eminent disciples." (`npnf202_socrates-sozomen-ecclesiastical-histories.xml` 39524–39525). Both are verbatim.
- `uncertain`: Clarke on Butler, who tells the several Moseses apart and takes the robber for the Moses of the sayings. This is LH 919, note 143.

## Not found

None.
