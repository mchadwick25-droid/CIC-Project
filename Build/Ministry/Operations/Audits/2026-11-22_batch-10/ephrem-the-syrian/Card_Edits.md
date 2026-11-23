# Card edits: Ephrem the Syrian

Card written to `ephrem-the-syrian.card.json` from `Card.existing.json`. All else word for word. Validated with `tools/validate-census.mjs` (card placed in a scratch copy of the census): 0 errors.

## Edits

1. **briefReferences, Palladius entry (clearly wrong against the brief).**
   - Old: `... the exchange, "See, on your behalf I appoint myself hospitaller."; the year of relief ...`
   - New: `... the exchange, "Look, on your behalf I appoint myself to run the shelter."; the year of relief ...`
   - Evidence: the quotation marks may stand only on words verbatim in the brief; the brief (paragraph 1) has "Look, on your behalf I appoint myself to run the shelter." The printed wording stays in quotationOriginals (`cic/texts/palladius_lausiac-history_clarke1918.txt` line 471, re-read verbatim).

2. **briefReferences, new entry after the Jerome entry.**
   - New: `Jerome, Lives of Illustrious Men 115, tr. Richardson: Ephrem a deacon of the church at Edessa, who composed many works in the Syriac language.`
   - Evidence: brief ("a deacon of its Syriac church", Edessa "Syriac-speaking"); `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml` lines 41540-41542.

## quotationOriginals
The brief has one quotation; the existing entry matches it (modern wording identical to the brief, printed verbatim at line 471). Kept unchanged, including its secondReading ("changes meaning") and uncertain note. No briefLength key.

## Not found
- Brief: Edessa "of upper Mesopotamia on Rome's border with Persia". Held texts say this of Nisibis (Theodoret II.26, npnf203 11065-11067) and place Edessa only loosely; no held line puts Edessa itself on the border. Left, no card change.
- Existing card claims not re-audited beyond those the brief touches; the card's "a few days" (Sozomen, npnf202 32161) and Palladius's month (line 471) both hold.

## Third pass: what it was about (2026-11-23)

Starting card kept unchanged as `Card.pass2.json`; edits made in `ephrem-the-syrian.card.json`.

1. **briefReferences, Palladius entry.** Old: `"Look, on your behalf I appoint myself to run the shelter."` New: `"See, on your behalf I appoint myself to take in and care for the needy."` Evidence: brief paragraph 1; `records/syr/quote/syr.quote.palladius-hospitaller.md` (`modern_rendering`, second sentence).
2. **quotationOriginals[0].modern.** Old: `Look, on your behalf I appoint myself to run the shelter.` New: `See, on your behalf I appoint myself to take in and care for the needy.` Evidence: same brief sentence and record. `printed` unchanged, re-read verbatim: `cic/texts/palladius_lausiac-history_clarke1918.txt` line 471, "See, on your behalf I appoint myself hospitaller."
3. **quotationOriginals[0].secondReading removed** (value was "changes meaning"). The quotation is over six words and the rendering changed, so release sets the second reading anew. The validator's skip-quotes run still asks for this key.
4. **briefReferences, new entry after the Mitchell entry (Mani).** Mani's two Roots, Light and Darkness, mixed; Darkness framing the body as a prison, in Ephrem's telling. Evidence: brief paragraph 2; Mitchell `cic/texts/ephraim_prose-refutations_mitchell1912-1921.txt` lines 418, 431, 727, 771.
5. **briefReferences, new entry (Manichaean prayer).** Two Roots, Bright and Dark, mixed and to be parted again. Evidence: brief ("A later prayer of Mani's own followers"); `cic/texts/manichaean-texts_dr-steins-turkish-khuastuanift-in-jras-1911_le-coq1911.txt` lines 16575-16585, 16643-16672. New `sources.about` entry for that file (Le Coq, 1911).
6. **briefReferences, new entry (Marcion).** Second God, the Stranger above the Maker, came down to lift souls out, as Ephrem tells it. Evidence: brief; Mitchell lines 592, 596, 1003, 1603.
7. **briefReferences, Nisibene Hymn 51 entry.** Old: `the body not raised as reproach to God's grace and slander of his justice.` New: `Ephrem's charge that a book of Bardaisan denied the body would rise; the body not raised as reproach to God's grace and slander of his justice.` Evidence: brief ("In a hymn, Ephrem charged that Bardaisan denied the body would rise"); Gwynn `cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml` lines 11200-11214.
8. **uncertain, new last entry.** Bardaisan's denial of the resurrection comes from Ephrem alone; a modern editor of Eusebius writes he "seems" to have denied it, Hort held he kept the common faith except on isolated points; no work of Bardaisan's own held. Evidence: `cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml` lines 26542-26556 (editor's note, Book 4, chapter 30). New `sources.about` entry for it.

Skipped: outline item 10 (Narsai's quarrel): the brief names none, nothing to add. The outline's confidence notes on Mani's body-as-prison wording, Marcion (Ephrem only) and the schools ("began with Ephrem") are not marked for the card; the brief already credits each to its witness, so no `uncertain` entries added. The quotation's `uncertain` note (hospitaller, "on your behalf") left as is.

Validator (`--skip-quotes`, scratch census with this card and the new brief in the entry): the only error is the missing `secondReading` noted in edit 3, which release sets. Against the old brief text in the entry, it also reports the quotation mismatch, as expected.
