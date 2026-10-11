# Donatist identity-and-scaffolding pass: adversarial review, round 2 targeted recheck (2026-10-06)

Scope: commit fa98527a on branch `records/identity-scaffolding-don`, checked only against the round 1 findings (`don_identity_scaffolding_review_round1_2026-10-06.md`). No model or API call was made.

Mechanical checks: `tools/check_live_commentary.py --surface records --base origin/main` gives 0 hits. `packages/don/2026-10-06T21-54-53Z` exists and matches the pin in `records/worlds/don.yaml`. A sweep of the `text` field in all nine touched doctrinal-witness records finds no remaining "you should", "note", "notice", "start with", "walk it", "you asked" or "your second/third question". The one question mark left (`written-by-our-opponents` P1, "who wrote it down?") is the world's own rhetorical question and was not a round 1 finding.

## Verdict: REVISE

The records clear. One OG-25 sentence is still inaccurate (finding A).

## Round 1 substantial findings

1. `what-belonging-cost`: FIXED. Now reads "the smaller ledger: what belonging cost inside one family or one street." No quantitative claim. Every element comes from the next three sentences.
2. `washed-for-the-first-time`: FIXED. Opens "Yes, we were born again, and we would fight over the arithmetic." The answer and the asked-about term are back. "The other side says again" is kept and is supported.
3. `hypocrites-and-those-who-left`: FIXED. P1 opens "Teachers who turned out to be hypocrites were among us". P3 reads "where God was when suffering came to us." Both antecedents are now explicit. The later "it is in the court record" refers clearly to the hypocrisy.
4. Second-person stage directions: FIXED in all four places. `what-we-argued-among-ourselves` P5, `written-by-our-opponents` P3 ("- but the copy..."), `not-a-death-wish` P4 and `hypocrites-and-those-who-left` P3 ("It was never a teaching about suffering that we worked out.") all read correctly. No new claim was added.
5. `refusal-and-recourse` quote: FIXED. The text field now reads "What has the Emperor to do with the Church?", which matches `cic/texts/optatus_against-the-donatists.txt` line 1904. The `positions` field (line 41) is still in lower case. That field was outside this pass, and OG-25 now says so.
6. OG-25: PARTLY FIXED. See finding A.

## Applied non-substantial suggestions

- Item 7, `who-jesus-was-among-us`: reads correctly. "the Son, one God with the Father and the Spirit, who died and was raised." The ambiguity is gone, and so is the unsourced "truly". The first sentence still leads with who Christ was to this world. It is still about 28 words long. That is a readability point, not a finding.
- Item 9, `two-churches-in-one-town`: reads correctly ("hold that authority through the people and the bishops together").
- Item 10, `walking-to-one-font`: applied in a different form from the suggestion: "Whether Christ would want anything to do with someone like you we can answer, at least, from our own doctrine". It is grammatical and adds no claim. A comma after "you" would ease reading. Not a finding.

## Finding A. SUBSTANTIAL: OG-25 still says nothing was added, and it contradicts itself on the quote

- "No claim, figure or name was added or dropped, apart from one correction in review" is still false for `who-jesus-was-among-us`. Before this pass, the text said only "on Christ himself we said what our opponents said." It now spells out the creed's content: "the Son, one God with the Father and the Spirit, who died and was raised." Round 1 judged this content source-covered (`don.core.donatism`) but named it as added content under finding 6. The entry lists it under "What moved", but the blanket sentence still denies it.
- "Quotes: no quoted passage was changed" contradicts the same paragraph, which records that the capitalisation of the `refusal-and-recourse` quote was changed to match the source.

Fix: change the sentence to "No claim, figure or name was added or dropped, apart from the creed content now spelled out in the Jesus witness's first sentence (drawn from `don.core.donatism`) and one correction in review: ...". Change the quote line to "Quotes: no quoted wording was changed; one quote's capitalisation was corrected to the source (below)." Once these are made, the status can move off "OPEN until the round 2 targeted recheck". This is an independent recheck item. It does not need a full round 3 of the records.

Everything else in OG-25 is accurate: the list of 21 records, the review reference, the new package pin, the note on the lower-case `positions` field, the item carried forward under OG-23 item 12, and the oblique note.
