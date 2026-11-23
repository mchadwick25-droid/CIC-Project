# Card check: John Chrysostom

Checked: `john-chrysostom.card.json` against `john-chrysostom.brief.txt`, `Card_Edits.md`, `Card.existing.json`, `Review.md`, `Revision.md`, `Fresh_Read.md`, `Do_Not_Say_After_Fresh_Read.md` and the held texts. No census entry is written (the person has one), so check 7 does not apply.

## Verdict: FIX (one change)

### FIX 1. quotationOriginals[0].printed

- Old: `"printed": "Glory to God for all things."`
- New: `"printed": "Glory to God for all things;"`
- Evidence: `cic/texts/palladius_dialogue-life-of-chrysostom_moore1921.txt` lines 6498-6499 print “Glory to God / for all things;’’. The print has a semicolon inside the quotation marks, not a period. The validator folds punctuation, so it did not catch this, but `printed` is the verbatim print. `modern` keeps the brief's period.

## The checks

1. **Edits justified.**
   - Edit 1 (Diodore reference): justified. Socrates VI.3 puts Theodore and Maximus, not John, "under the guidance of Diodorus" (npnf202 17163-17170). Socrates's own text gives Diodore's "literal sense of scripture" (17182-17185), so the review's claim that Socrates does not say it was wrong. Sozomen VIII.2 (Book VIII at 42523, chapter II at 42646) names Carterius and Diodorus as John's teachers (42693-42695). The translator is Chester D. Hartranft (21654). The writer was right to set aside the review's "Prevost's preface": npnf110 729-732 is M. B. Riddle's essay (headed at 609).
   - Edit 2 (Marriott preface): justified. npnf110 lines 535-536, "were undoubtedly delivered at Antioch", in the Preface to the Oxford Edition signed C. Marriott (592). It supports the brief's "There, in a sermon on Matthew". The file is already in `sources.ownWords`.
   - Edit 3 (Sozomen in `sources.about`): needed for edit 1. It is in the same format as the Socrates rows.
2. **Nothing else moved.** A JSON diff against `Card.existing.json` (which equals the census card) shows only edits 1-3.
3. **briefReferences.** Each entry names something the brief still tells. The fresh read's change ("Not long before", in place of "That year") touches no reference.
4. **Census rules.** Only allowed keys are used, with no `briefLength` and no connections. There is one quoted span in the brief and one entry for it. Its printed wording is verbatim except for FIX 1. Every cited file is in `sources`. No audit is named. American spelling. No outline, and no held original rendered. The `secondReading` "same" is carried from the census card set at release, and the validator requires a verdict there, so it stays.
5. **"checked at card".** There are none (the one quotation has six words).
6. **Not found / left in.**
   - `legacy.remembered[2]` says "thirty-fifth year after his deposition". In the Origen comparison, Socrates says "after his death" (21478-21479). But Socrates gives "in the thirty-fifth year after his deposition" for the same event at 21465. A held source supports the card, so it is not clearly wrong. Left in, as the writer noted.
   - Nothing else clearly wrong is left in.
