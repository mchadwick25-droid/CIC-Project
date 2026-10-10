# Witt claim corrections: adversarial review (2026-10-08)

Scope: branch `records/witt-claim-corrections` at 3621e408 (`git diff origin/main...HEAD`: commits ed34de0e and 3621e408). The branch makes Mark's ruled meaning corrections to six `witt` doctrinal-witness records, repins the package and adds OG-62. It is kept apart from the scaffolding pass (OG-61), which was not re-reviewed. I edited no record and made no model or API call. This is one review, Opus 5.5.

Mechanical checks, run on the branch:
- `python -m engine.m10.cli records witt`: PASS.
- `python -m engine.m10.cli regate witt --base origin/main`: PASS. Every note is a base failure, unchanged. No changed record appears in the notes.
- `python tools/check_live_commentary.py --base origin/main --enforce`: exit 0. Only PROTECTED lines in `Open_Gaps_Tracking.md` are listed. Nothing is flagged in the six records or in `records/worlds/witt.yaml`.
- `python -m engine.m9.cli check`: exit 0. 1285 report-only observations. The library access gate is clean: every finding is waived, and every waiver is live and current.
- Package pin: `records/worlds/witt.yaml` pins `packages/witt/2026-10-08T19-30-45Z` with `manifest_hash: "sha256:ac378d165dc010800d5caee5e20a2f150960d7f5448d8f3c6263c856f86a8e84"`. `sha256sum` of that `manifest.json` gives the same value, and OG-62 states the same path and hash. All 364 manifest entries hash correctly. Its `records_commit` is ed34de0e, and no `records/witt` file changes after that commit. The package's 251 record files match `records/witt/` byte for byte (`diff -rq` gives no output, and each manifest record hash equals the source file's hash). The compiled package holds none of the old readings, except in `witt.quote.the-poor-man-who-comes-to-you` ("go unanswered"), which OG-62 leaves open on purpose.

## Verdict: APPROVED TO PROCEED

Every quoted span is verbatim against its vendored source. No old reading survives in any spoken field of the six changed records. The superlative is gone from `text` and `positions`, and the record's `use_note.not_for` and `tensions` still agree with what is left. The only record that still carries the old wording is the quote record that OG-62 names and leaves open for Mark. There are no substantial findings. Findings 1 to 3 are wrong statements in OG-62, the audit trail, not in any record. Findings 4 and 5 are clarity points in spoken text. All five are one-line edits that need no further review round.

## Source verification

- Augsburg Confession, Article II (`cic/texts/melanchthon_augsburg-confession_anon-pg275.txt`). Heading at line 192. Lines 197-198 read: "of origin, is truly sin, even now condemning and bringing eternal death / upon those not born again through Baptism and the Holy Ghost." The new quote in `witt.dw.a-death-begun-that-a-child-receives`, "bringing eternal death upon those not born again through Baptism and the Holy Ghost.", is a contiguous span of this text, word for word. Leaving out "even now condemning" is a clean cut at the start of the span, so the quote adds and changes nothing.
- Large Catechism (`cic/texts/luther_large-catechism_bente-dau1921.txt`) line 1956: "hearts, and will not allow them to go unavenged." The word "unavenged" is correct.
- Small Catechism (`cic/texts/luther_small-catechism_smith1994.txt`) line 192: "rose again from the dead". Line 191 ends "on the third day" and has no "he". Line 199: "He is my Lord!" Line 203: "Because of this, I am His very own". Both are in the one "What does this mean?" explanation, which starts at line 197. "In the same explanation" is accurate.

## Per-item checks

1. `witt.dw.a-death-begun-that-a-child-receives`. The quote is verbatim (above). The sentence keeps the old claim: the Article II sentence names the remedy, and new birth comes through baptism. It adds one clause, "It calls the disease truly sin". That clause comes straight from the same source sentence ("this disease, or vice of origin, is truly sin"), so nothing is invented. No claim is dropped. The `divergence_note`, `positions`, `tensions`, `use_note` and `sources[1].locus` hold no "until" reading. The locus already quoted the source correctly. See finding 4 on the new clause.
2. `witt.dw.born-in-sin-fed-at-the-table`. "bringing death, until a person is born again through baptism and the Spirit" now reads "bringing death to those not born again through baptism and the Spirit." This is a faithful paraphrase without quote marks. It drops "eternal", but the old text dropped it too. No other field carries "until".
3. `witt.dw.the-poor-man-at-the-door`. "It is the sharpest warning this household book gives anywhere." is removed from `text`, and " -- our sharpest warning against any sin named in this same household book" is removed from `positions[2]`. "unanswered" now reads "unavenged". `use_note.not_for[1]` ("a claim that this is the sharpest warning in the household book, which only one locus was searched to support") and `tensions[1]` (one locus searched) still agree with the record. `positions[1]` ("a real, sharply worded warning") makes no superlative claim. `use_note.means` ("sharply warned") is fine.
4. `witt.dw.how-the-promise-reached-us` now has "on the third day rose again from the dead". `witt.dw.truly-god-and-truly-man` now has "in the same explanation". Both are accurate to the source. No position or tension repeats the old wording. The `sources` locus of `how-the-promise` already quoted without "he". See finding 5.
5. `witt.dw.a-confession-answered-not-a-vote`. The body now carries "Cited story and source records were not re-read for this record." This matches what the body cites (`witt.story.diet-of-augsburg-1530`, and source records). I checked OG-62's claim that this was "the one body that lacked the note". The only other doctrinal-witness body without the note, `witt.dw.a-narrow-word-plainly-spoken`, cites only a quote record verified against its source, so it needs no note. The claim holds. OG-58 item (6) is the separate defect that this body names a Confutation source record its `sources` list does not hold. It is untouched and still open, and OG-62 does not claim to close it.
6. OG-62. The "Changed" bullets match the diff word for word, apart from finding 1. The pin and hash are correct. The record `witt.quote.the-poor-man-who-comes-to-you` is flagged correctly. Its `modern_lens_note` says "in the sharpest language this household book uses anywhere", and its `modern_rendering` ends "He will not let it go unanswered." Both quotations in OG-62 are exact. It is also right that this is OG-58 item (4), and that the voice can still say both from that record. That record's own `use_note.not_for` ("a claim that this is the sharpest warning in the whole household book, which no record has checked") contradicts its own `modern_lens_note`. This adds to the case for Mark's ruling but is not a new defect. The entry's status line marks those items OPEN, which is correct. "Closes item (2)" and "item (3)" of OG-58 are correct. OG-58's own status stays OPEN for its other items, which is right for an append-only log.

Grep across `records/witt` for "until born again", "until a person", "until ... born again", "sharpest", "unanswered", "next line" and "he rose again". The only spoken-field hits for the old readings are in `witt.quote.the-poor-man-who-comes-to-you` (flagged). "sharpest" in `witt.gravity.the-word`, `witt.gravity.must-and-free`, `witt.term.must-and-free` and `witt.term.pope-and-antichrist` belongs to other claims (the Word/"must and free" tension, the pitch of the Antichrist naming), not this one. "unanswered" in `witt.dw.scripture-judges-every-other-voice` and in the `divergence_note` of `a-death-begun` is unrelated. "he rose again" in the `modern_rendering` of `witt.quote.second-article-of-the-creed` (line 67) is in a modern rendering, where adding the subject is right, not a recitation of the source text. `witt.quote.article-ii-of-original-sin` (verbatim text and `modern_rendering`) carries no "until" reading.

## Findings

### 1. NOT SUBSTANTIAL: OG-62 gives the wrong line numbers for the Article II quote
Old (OG-62, first "Changed" bullet): "The quoted words match Article II (`cic/texts/melanchthon_augsburg-confession_anon-pg275.txt`, lines 195-196)."
The source: `grep -n` puts "bringing eternal death" on line 197 and "upon those not born again" on line 198. Lines 195-196 are "natural way are born with sin, ..." and "trust in God, and with concupiscence; ...". The same wrong pair appears in OG-61 and in the round 3 scaffolding review. That review is a past audit file and stays as it is.
Fix: "lines 195-196" → "lines 197-198".

### 2. NOT SUBSTANTIAL: OG-62 miscounts the gap between "He is my Lord!" and "I am His very own"
Old (OG-62, `truly-god-and-truly-man` bullet): ""I am His very own" comes three lines after "He is my Lord!" (Small Catechism, lines 197-203)."
The source: "He is my Lord!" is on line 199 and "I am His very own" is on line 203, four lines later. OG-61's "three lines later" has the same error.
Fix: ""I am His very own" comes four lines after "He is my Lord!" (Small Catechism, lines 199 and 203), in the same explanation."

### 3. NOT SUBSTANTIAL: OG-62 miscounts and mislabels the OG-61 items it closes
Old (OG-62, opening paragraph): "Closes the four carried items that pass listed for Mark."
OG-61 flags two items for Mark: (1), the "until" reading in two records, and (2), the superlative. It notes three more "for the build thread": "he rose again", "the very next line" and "unanswered". OG-62 fixes all five. There are not four, and only two were listed for Mark.
Fix: "Closes the carried items that pass listed: the two flagged for Mark and the three noted for the build thread."

### 4. NOT SUBSTANTIAL: "the disease" is used in spoken text before the record introduces it
Old (`witt.dw.a-death-begun-that-a-child-receives` `text`): "The same sentence that names us "born with sin" names the remedy. It speaks of those brought to eternal death "until born again through Baptism and the Holy Ghost.""
New: "The same sentence that names us "born with sin" names the remedy. It calls the disease truly sin, "bringing eternal death upon those not born again through Baptism and the Holy Ghost.""
The quote is now right. But "the disease" appears nowhere earlier in this record's `text`, so a participant hears a definite article with nothing it refers to. The writing standard asks for a term to be introduced before it is used. The sister record `born-in-sin-fed-at-the-table` does introduce it ("We call this a disease, a vice of origin"). The added clause is sourced, so this is a clarity point, not a fidelity one.
Fix (keeps the verbatim quote and adds no claim): "It calls that inborn sin a disease and truly sin, "bringing eternal death upon those not born again through Baptism and the Holy Ghost.""

### 5. NOT SUBSTANTIAL: the creed recitation now reads as a sentence with no subject
Old (`witt.dw.how-the-promise-reached-us` `text`): "household under our catechism says: on the third day he rose again from the dead... just as he is risen from death"
New: "household under our catechism says: on the third day rose again from the dead... just as he is risen from death"
Dropping "he" makes the words verbatim. But the span has no quote marks, so in the voice's own speech it reads, and sounds, like a grammar slip rather than a recitation. Marking it as the creed's own words keeps it verbatim and makes the missing subject read as quotation.
Fix: "household under our catechism says: "on the third day rose again from the dead... just as He is risen from death, lives and reigns forever. Yes, this is true."" Inside the quote marks, "He" takes the source's capital (line 205). The `sources` locus already quotes it this way.

None of these findings blocks the branch. Findings 1 to 3 are corrections to OG-62, an append-only entry that has not merged yet, so they can be made in place. Findings 4 and 5 are record edits, and each would need a package rebuild and repin under the default actions.
