# John Cassian: card check, third pass (what it was about)

Checked `john-cassian.card.json` against `Card.pass2.json`, the section "Third pass: what it was about (2026-11-23)" of `Card_Edits.md`, and `john-cassian.brief.txt` as it now stands. Every cited line opened.

**Verdict: FIX** (one change).

## What holds

- **Nothing else moved.** A field-by-field diff with `Card.pass2.json` shows changes only in `keyWorks[0].about`, a new last `uncertain` entry, two new `sources.about` entries, `briefReferences[0]`, `[4]`, `[5]`, `[6]`, `[7]`, `[8]`, `[10]` and the new `[9]`, each listed in the edit list. The key set is unchanged and allowed.
- **Edit 1** (`[0]`): the brief's paragraph 1 no longer names Honoratus and Eucherius; "the two" and "seven Conferences" match it.
- **Edit 2** (`[4]`): Palladius 2640-2648 has "sent into exile through a plot formed by Acacius ... Theophilus ... Antiochus ... and Severianus"; this matches the brief's "bishops had plotted".
- **Edit 3** (`[5]`): the brief's paragraph 9 no longer tells the tempering. The cut is correct.
- **Edit 4** (`[6]`): the brief's paragraph 11 has "an old hermit" and no name.
- **Edit 5** (`[7]`): Goldbacher 16932-16936 (Multi ... seruorum Christi ... in Massiliensi urbe), 17014-17016 (eligendorum et reiciendorum ... ante mundi initium ... discretio), 17040-17050 (superfluus labor; cassa sit adnitentis intentio). This matches "effort was in vain".
- **Edit 6** (`[8]`): npnf211 48713-48718 (the Pelagians: men could be without sin if they liked) and 48738-48741 (note 2370, "Nestorius", "declares that our Lord and Saviour was born a mere man ... exactly the same thing which the Pelagians said before him"). The charge is credited to Cassian.
- **Edit 7** (`[10]`): npnf211 15781-15794 has proposition (1), on good thoughts from God, "allow[ed] to be catholic and orthodox", and "all the others are erroneous". 15812-15818 has proposition (4), "sometimes the first beginnings of a good will arise". The entry still says the book is not held and gives this as Gibson's account.
- **Edits 8 and 10** (`[9]`, `sources.about`): Socrates, npnf202 20703-20716 (Anastasius: "Let no one call Mary Theotocos") and 20737-20739 ("totally rejected the epithet"); Ephesus, npnf214 17263-17280 ("Nestorius be excluded from the episcopal dignity"). Both files are now in `sources.about`.
- **Edit 9** (`uncertain`): npnf202 20741-20744 ("reputation among the masses of asserting ... that the Lord is a mere man") and 20753-20755 ("I cannot then concede ... that he denied the Divinity of Christ: but he seemed scared at the term Theotocos"). This is credited to Socrates, and Cassian's charge is kept separate. It follows the outline, "What it was about" item 7.
- **Edit 11** (`keyWorks[0]`): npnf211 16503-16514 (miracles left out; "only their institutions and the rules of their monasteries ... the principal faults, of which they reckon eight, and the remedies"). Petschenig 7996-8003 (moderationem ... pro asperitate aerum ... diuersitate morum ... Palaestinam uel Mesopotamiam ... temperem). This follows outline items 16 and 17, "To the card".
- **Rule 4.** The brief has four quoted spans and the card has four `quotationOriginals` entries. Each `printed` field is verbatim at its lines: npnf211 38028-38030, 15774-15775, and 25949-25952, and npnf203 43669-43671. "the Conferencer", marked "checked at card", is a fair English for "Contra Collatorem", and its `uncertain` note explains it. No audit file is named, and spelling is American. `node tools/validate-census.mjs` on `scratch_census.json`, which carries this card, gives 0 errors.
- **Rule 6.** No claim is listed as not found in this pass, and nothing clearly wrong is left in.

## FIX

**Rule 3.** The brief's paragraph 19 no longer tells the Rule's last chapter (chapter 73) and its list of a monk's tools. It now reads only "Benedict's Rule names no author for its Conferences, but the title is Cassian's." The edit list skips outline item 13 because the card already carries it. That is right for `legacy.traces`, which keeps it, but the `briefReferences` entry still names what the brief has dropped. Chapter 42, at RB 6838-6846 ("legat unus Collationes"), carries what the brief still tells.

- Field: `briefReferences[12]`
- Old: `Rule of Benedict, chs. 42 and 73, ed. Hunter Blair: the Conferences read aloud after supper, first among the readings; the Conferences, Institutes and Lives of the Fathers named among a monk's tools. The Rule names no author; Gibson takes them for Cassian's books. Hunter Blair dates the Rule about 535.`
- New: `Rule of Benedict, ch. 42, ed. Hunter Blair: the Conferences read aloud after supper, first among the readings. The Rule names no author; Gibson takes them for Cassian's books. Hunter Blair dates the Rule about 535.`

(`sources.about` keeps "The Rule of Saint Benedict, chapters 42 and 73", because `legacy.traces` still cites chapter 73.)

## Notes on the edit list (no card change)

- The header of the third-pass section reverses the two files. It reads "Starting card: `john-cassian.card.json` (unchanged); result: `Card.pass2.json`". On disk, `Card.pass2.json` is the starting card, and `john-cassian.card.json` holds the edits.
- Edit 10 says the two sources go "after the Gallic Chronicle entry". On the card they come after Gregory of Tours and before the Gallic Chronicle. No existing entry is reordered.
