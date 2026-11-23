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
