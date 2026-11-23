# Card edits: John Chrysostom

Card: `john-chrysostom.card.json`. Everything else is word for word from `Card.existing.json`. It passes `tools/validate-census.mjs` (checked with the card in the census entry, copy outside the repo).

## Correction

1. briefReferences, Diodore line.
   - Old: "Socrates, Church History VI.3, tr. Zenos: John's training under Diodore, who kept to the literal sense of Scripture."
   - New: "Sozomen, Church History VIII.2, tr. Hartranft: John's training under Diodore. Socrates, Church History VI.3, tr. Zenos: Diodore's literal sense of Scripture."
   - Evidence: Socrates VI.3 says Theodore and Maximus, not John, went under Diodorus (`cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml` 17167-17170) and gives the literal sense of Diodorus's writings (17182-17185). John's teachers Carterius and Diodorus are in Sozomen VIII.2 (42693-42695); Zenos's note on literal sense is 17172-17178. The review's suggested wording ("Zenos's note and Prevost's preface") does not hold: the Diodorus passage in `cic/texts/npnf110_chrysostom-homilies-matthew.xml` (lines 729-732) is in M. B. Riddle's Introductory Essay, and Prevost only translated the homilies.

## New

2. briefReferences, inserted after the Homily 50 line: "Homilies on Matthew, Preface to the Oxford Edition, by C. Marriott: the homilies were delivered at Antioch."
   - Evidence: brief sentence "There, in a sermon on Matthew, he told his listeners..."; npnf110 lines 535-536, "were undoubtedly delivered at Antioch".
3. sources.about, added: Sozomen, "Church History, Book 8, chapter 2", English translation, npnf202 file (for edit 1).

## Not changed

- quotationOriginals: the brief's only quotation, "Glory to God for all things.", is unchanged; printed text re-read at the cited lines by the validator.
- No briefLength, no connections.

## Not found / noted

- legacy.remembered, third item says John was "restored to communion in the thirty-fifth year after his deposition". Socrates VII.45 says "after his deposition" at 21465 and "after his death" at 21478. Left in place.

## Second pass (2026-11-23)

- Checker FIX 1 (quotationOriginals[0].printed, "Glory to God for all things." to "Glory to God for all things;"): applied word for word.
- Scan readings to add: none (the checker lists none).
- Outline items added: none. There is no Outline.md for this story, so step 2 was not done. Review.md and Fresh_Read.md were not mined for card items; skipped for that reason.
- Validator (`--skip-quotes`, scratch census copy with this card in place): no errors for john-chrysostom.
