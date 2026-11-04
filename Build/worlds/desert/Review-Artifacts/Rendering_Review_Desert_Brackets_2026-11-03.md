# Rendering Review: desert quote records, bracketed supplements (6 records)

- **Reviewer:** Opus 5.5 (independent; did not render these records)
- **Date:** 2026-11-03

## Method (short)

For each record, the reviewer reads the edition in `cic/texts/` at the record's locus and confirms the record's `text` matches it. The reviewer then lists every square-bracketed supplement in `text` and checks how `modern_rendering` handles it. A supplement voiced without brackets passes only when it is purely grammatical: English needs it, and it adds no sense the source lacks (a missing object, a determiner, a referent that the source makes plain). A supplement that adds sense (an interpretive gloss, an occasion, a choice between readings the source leaves open) fails P2 when it is voiced unmarked. For composed-by-bishop-palladius-for-the-prefect-lausus the reviewer checks the full bar as well: every clause, nothing added, one thought per sentence, no sentence past about 25 words, no misleading modern word, frames kept, plain English. Each corrected rendering below is held to that same full bar.

Edition lines read: `anan-isho_paradise-v2-sayings_budge1907.txt` lines 50 and 2750; `palladius_paradise-v1-syriac_budge1907.txt` line 1133; `evagrius_praktikos_dysinger.txt` lines 159-161 (pr 8) and 188-196 (ch. 6); `pachomius_rules-ethiopic_schodde1885.txt` line 206. Each record's `text` matches its edition.

## Results

| Record id (desert.quote.…) | Bracketed words in text | Rendering check | Verdict |
|---|---|---|---|
| composed-by-bishop-palladius-for-the-prefect-lausus | "[which they gave]" | The supplement now stays in brackets, as Budge prints it. Budge's "(sic)" is an editor's mark and is rightly left out. Every clause is present: "And again", "by the power of our Lord", "we begin", "the Third Part", the counsels, the questions and answers, "to the Brethren". "We begin it" repeats the source's own verb to split the sentence and adds no sense. "Old Men" becomes "elders", which is accurate. Sentences run 13 and 20 words. | PASS |
| taor-not-compelled-to-market | "[them]" | Voiced as "them". This is the object English needs for "need"; the items (apparel, veil, sandals) are named in the edition's own sentence. It adds nothing. Both clauses kept. | PASS |
| the-eight-generic-thoughts | "[tempting-]" (twice) | Voiced unmarked twice as "tempting thought". English does not need it: "eight general kinds of thought" is complete. The word is Dysinger's gloss on what kind of thought a logismos is, so it adds an interpretation and gives it to Evagrius. | FAIL P2 |
| the-ladder-from-faith-to-love | "[these]", "[when conferring it]", "[my]", "[this fear]", "[is strengthened]", "[virtue]", "[dispassion]" | "these", "my" and "this fear" are grammatical or idiomatic and add no sense; "This latter [virtue]" is rightly made "Self-control"; "[dispassion]" is a gloss of the term and is rendered as one. "[is strengthened]" fills a gapped verb; it is rendered with a new verb rather than the source's own "steadied", which shades it. But "[when conferring it]" is voiced unmarked as "when they give it". This names the occasion of the fathers' words, which the edition does not state; it is meaning-bearing. | FAIL P2 |
| whence-canst-thou-prove-to-us | "[seeds]", "[kinds of]" | "some seeds fell" supplies the noun the sower's sowing already implies. "three kinds of seed" makes "three seed" grammatical and points to the three falls the old man has just listed. Neither adds sense. The scripture reference is Budge's and is rightly left out. | PASS |
| womens-house-across-the-river | "[the men]" (twice), "[the women's]" (three times), "[the women]" | All voiced unmarked. In "neither did these see their faces nor did the latter see the faces of the former" the resolution adds nothing, because the sentence is symmetric. But in the numbers, Schodde's brackets decide which count belongs to which group ("[the women] ... one hundred and eighty, and these [the men] three hundred and forty"). In the command, they decide whose faces are meant. The source has only pronouns there. Voicing those as plain fact gives an editor's reading to the text. | FAIL P2 |

## Failed renderings: corrected text

### the-eight-generic-thoughts (FAIL P2)

"[tempting-]" is the translator's interpretive gloss, so it stays in brackets. Everything else in the earlier rendering holds and is kept.

Corrected rendering:

> There are eight general kinds of [tempting] thought, called logismoi, and these eight hold within them every [tempting] thought. First is gluttony, and with it sexual immorality. Third is love of money; fourth, sadness; fifth, anger; sixth, acedia; seventh, vainglory; eighth, pride. Whether these thoughts can disturb the soul or not is not up to us. But whether they linger or not, and whether they stir up passions or not, is up to us.

Longest sentence 19 words. The source's missing "second" is kept as the edition has it.

Note for the record's owner (outside this verdict): `use_note.means` says "eight generic tempting thoughts" without marking "tempting" as the translator's.

### the-ladder-from-faith-to-love (FAIL P2)

"[when conferring it]" stays in brackets. The gapped verb is now filled with the source's own "steadied", so it adds no sense of its own. "which brings into being love" is rendered as one clause, as the edition has it, rather than restated as a separate act.

Corrected rendering:

> The habit, then, is like a symbol that sums up these things. These are the words the fathers always say to them [when they give it]: "Faith, my child, is steadied by the fear of God. This fear, in turn, is steadied by self-control. Self-control is made unshakable by patient endurance and hope. From these is born apatheia, dispassion, which brings love into being. Love is the door to the knowledge of nature, which leads to theology and the highest blessedness."

Longest sentence 17 words.

Note for the record's owner (outside this verdict): `modern_lens_note` ("words the elders say when handing over the habit", "a formula recited at a clothing") and `use_note.means` ("the fathers' words at the giving of the habit") rest on Dysinger's bracket, not on the edition's own words.

### womens-house-across-the-river (FAIL P2)

The symmetric sentence is rendered without naming either group, so it needs no supplement. The brackets that decide which number and whose faces stay marked. Three smaller points are fixed at the same time. The 26-word sentence of three acts is split. "over her" and "to them" are dropped, because the edition has neither. "instigation", whose modern sense suggests stirring up trouble, becomes "urging".

Corrected rendering:

> His sister by blood loved the monastic life. He cut her hair and put a belt around her. He made a dwelling for her alone, a mile away on the other side of the river. Through her urging, virgins and widows gathered together and became very good. No one crossed over, except those ordained by Abba Pachomius, and chosen ones, on the fixed festival days of our Lord.
>
> When one of these women went to her rest, they sang psalms, adorned her in holiness, and wrapped her in linen. And the brothers received her on a raft and buried her in their own place.
>
> But neither side saw the other's faces. [The women] reached the number of one hundred and eighty, and [the men] three hundred and forty. He commanded them to take great care not to see [the women's] faces or hear their voices.

Longest sentence 21 words.

Note for the record's owner (outside this verdict): `use_note.means` ("180 women lived unseen by 340 men") and `modern_lens_note` ("one hundred and eighty women to three hundred and forty men") state Schodde's assignment of the numbers as the text's own.
