# Card edits 2: Moses the Black

Starting card: the census object `card` for movement `moses-the-black` in `cic-website/data/world-census.json`. Every field except `briefReferences` and `quotationOriginals` is kept word for word and in its order. No `briefLength` (the census does not allow it). No statement was corrected.

## quotationOriginals

Kept unchanged (still quoted in the brief, paragraph 3):

1. "I am not allowed to hurt anyone. So what do you tell me to do with these?" (LH 335).
2. "If a man so great and powerful in robbery has feared God, why should we put off our salvation?" (LH 335; the brief breaks it around "they said").

Removed (no longer quoted in the brief):

3. "Get outside, O Ethiopian." (PAR2 1028). The new brief tells the scene without quoting the clergy.
4. "Those who take the sword shall perish by the sword." (PAR2 1464, chapter XIV saying 45). The barbarians saying is no longer in the brief (Outline, Leave out and Do not say).

Added:

5. "Why does this Ethiopian come and go among us?" Printed: "Why doth this Ethiopian come and go in our midst?" (`anan-isho_paradise-v2-sayings_budge1907.txt` 164, saying 55; re-read). `secondReading`: same (Second_Readings_4.md, S4-03 SAME). That entry cites "PAR2 line 166"; the saying stands at line 164, so the card gives 164. No `uncertain`: neither the outline nor the second reading notes a doubt.
6. "They have treated you rightly, you whose skin is dark and black. You shall not go back in as if you were a man." Printed: "They have treated thee rightly, O thou whose skin is dark and black; thou shalt not go back as if thou wert a [white] man." (PAR2 1028, saying 477; re-read). `secondReading`: minor (S4-04 MINOR). `uncertain`: Budge's "[white]" is his own bracketed supply and is left out; Dorotheus of Gaza, Doctrina XIV, reads "non homo" (`dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt` 136342–136344, re-read: "Sterqui- linium cum sis et cinis, non homo ; cur ad homines ingrederis?"); "go back" becomes "go back in". Evidence: Outline, Quotes 3 and beat 6; Second_Readings_4.md, note on S4-04; Source_Sheet Y3 and Library sweep. No original-language fields: the Syriac is not held, and Dorotheus is a parallel, not the original.

## briefReferences

Replaced. The old list cited the Nile swim, the water-pots, the demon's blow, the clergy's words, the Ethiopian Synaxarium's death by barbarians, and the PAR2 1464 barbarians saying, none of which the new brief uses. The new list, ten items, in plain text with no quotation marks:

- LH 337: among the great ones of the fathers; priest at Scete; seventy disciples.
- LH 197 with note 713, and 657: Palladius in Alexandria in 388, writing in 419–420, the ground for around the year 400; LH 18, Palladius the bishop, for "a bishop writing around 420".
- LH 333: house-servant, Ethiopian by race and black, driven out for immorality and brigandage, said to have murdered, crimes told to show his repentance, reported leader of a robber-band by the Nile.
- LH 335: conscience-stricken by one of his adventures; the four robbers; their confession and renouncing the world because of his conversion.
- LH 337: the long fight with his old lust, six years standing at night, Isidore the priest of Scete, the dreams ceased, Communion, two months later.
- PAR2 164: the fathers' contumely, his silence, his fear.
- PAR2 1028: the bishop's test, the clergy driving him from the sacrarium, his words against himself.
- PAR2 header 7–8: the 7th-century Syriac compiler, for "sayings gathered in the 600s".
- LH 337: death at Scete at seventy-five.
- World census, desert monasticism: the desert fathers of Egypt.

## The barbarians saying (PAR2 1464)

Its quotation entry and its `briefReferences` item are removed; no other part of the card cites line 1464 or the sword saying. No card statement tells it as his. The only other mention is the fourth `uncertain` item ("A saying tells that barbarians came to Scete and killed Abba Moses ... It does not name him the Ethiopian. Palladius says only that he died at Scete at seventy-five."), which says the saying does not name him and sets it against Palladius. It is a caution, not a claim, and is left in place.

## Checked, left alone

- `knownFor`: "driven out for robbery". The brief says "for immorality and robbery" (LH 333), and the outline lists "Driven out for robbery" alone under Do not say. The card's words are partial, not contradicted, so they stay; flagged for the checker.
- `sources.about` still lists the Ethiopian Synaxarium, which the new brief no longer uses. It is not wrong, so it stays.

## Check

A script check of the card against the brief, using the validator's folding and span-run rule: the brief's five quoted spans are all covered by the four entries, every entry's `modern` is in the brief, every `printed` stands in its cited lines, every entry has a verdict, and the card has only allowed keys. The full census validator was not run.

## Not found

None.
