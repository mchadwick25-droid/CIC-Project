# Recheck of the review fixes: Apocryphal and Pseudepigraphal Literature

Targeted recheck of what `Fixes_Review.md` changed in `Outline.md` and `Source_Sheet.md`, against `Review.md` and the vendored sources. No `.v1` file opened. Brief read: `apocryphal-and-pseudepigraphal-literature.brief.txt`, 672 words (wc).

## Verdict: FIX

Two BLOCKING findings, both with exact replacements. Everything else holds.

## What holds

- **B1g row (Source_Sheet.md 35).** Lines checked. Schwartz 2519 and 2621 read "χαταλαβόμενοι ὁποίας ἢν αἱρέσεως ὁ Μαρ- / »xutróc, (ὃς) καὶ ἑαυτῷ ἐναντιοῦτο, μὴ νοῶν ἃ ἐλάλει". Rufinus 2588 and 2679 read "cuius haereseos fuerit Marcianus, qui etiam sibi / ipsi contrarius extitit, non intellegens quae loqueretur". npnf201 33716–33739 agrees, and note 1837 calls him "otherwise unknown". My rendering: "But we, brothers, have grasped what heresy Marcianus belonged to, who even contradicted himself, not understanding what he was saying." The row's text, confidence (Documented as what Serapion says), witness kind and its caveat (no stated tie between Marcianus and the backers) are right. The editor's "(ὃς)" changes nothing: without it, Marcianus is still the one who contradicts himself, and Rufinus's "qui" confirms it.
- **Section E bullet and the set-asides (Source_Sheet.md 121, 164).** The search for what the teaching was is real. Clement 7.17 and Hippolytus Ref. 8 name the Docetae but not Rhossus. The tie between them is McGiffert's (note 1838, modern). Setting them aside is right.
- **Heresy row (Source_Sheet.md 130).** Supported at its cited lines.
- **B2 (beat 2).** CSEL 20 12260–12267: the presbyter ("sciant in Asia presbyterum…") comes before Paul's rule ("qui ne discere quidem constanter mulieri permisit"). The new beat and the Do not say row match the source.
- **B7 (Ending 1).** End on the reading (B6c). The heart's "What came of them" still holds the reading at her memorial.
- **Do not say rows 163–168.** Each is supported. "Other books like it" rests on B5d's "or of any others besides them" (npnf201 18256–18260).
- **Names (Marcianus) and Leave out (Docetae).** Right. Marcianus acts only in Serapion's report.
- **Heart and order.** The heart is untouched. In the brief it is told by about word 70, inside the first minute. The Marcianus sentence sits inside beat 1, before the borrowed book, so each beat still runs once and in order. The ending is not told early.

## BLOCKING

**R1. The writer's Marcianus wording says more than its source, and its Reason line misreads the order.**

(a) In the narrator's voice, "He saw what one Marcianus held: a man who contradicted himself…" states as fact Serapion's hostile verdict on a man no other old source knows. The source gives only Serapion's claim. The outline handles Thecla's wonders the same way ("the book says"), so this needs Serapion's attribution too. The fix is 19 words. Net of "some heresy," (−2), it adds +17, the review's full budget: 658 + 17 = **675**, at the cap and not past it. No cut is needed. If a draft runs past 675, the existing fallback applies ("from far-distant lands", −3).

(b) The Reason gives "then what he saw of Marcianus, then his own reading", which is not what the source says. Serapion's next clause opens with γάρ ("for we were able… to go through it", Schwartz 2621–2622). Rufinus has "investigata per nos ab illis" (2680). So the reading is how he learned of Marcianus, not a step after it.

Exact replacements in `Outline.md`:
- Beat 1 (line 62): "Then Serapion's report of the teaching, in plain wording the writer may use (16 words, narrator's voice, not a quote): He saw what one Marcianus held: a man who contradicted himself, not understanding what he said." → "Then Serapion's report of the teaching, in plain wording the writer may use (19 words, told as what Serapion wrote, not a quote): He wrote that he saw what one Marcianus held: a man who contradicted himself, not understanding what he said."
- Beat 1 (line 62): "Reason: what he was told of the backers' teaching, then what he saw of Marcianus, then his own reading." → "Reason: what he was told of the backers' teaching, and what he learned of Marcianus through his own reading of the book (γάρ, Schwartz 2621–2622; Rufinus 2680)."
- Do not say (line 165), Right column: "\"He saw what one Marcianus held: a man who contradicted himself, not understanding what he said\" (B1g); nothing more is kept" → "\"He wrote that he saw what one Marcianus held: a man who contradicted himself, not understanding what he said\" (B1g), always as Serapion's report; nothing more is kept"
- Cut first, Review fix pass (line 209): "B3: \"some heresy,\" out (−2), the Marcianus sentence in (+16): **672**, under the 675 cap." → "B3: \"some heresy,\" out (−2), the Marcianus sentence in (+19): **675**, at the cap."
- Length (line 18): "Review fix pass: **672**" → "Review fix pass: **675**"

Exact replacement in `Source_Sheet.md` (line 35, end of the B1g row): "Plain wording for the story (16 words): \"He saw what one Marcianus held: a man who contradicted himself, not understanding what he said.\"" → "Plain wording for the story (19 words, told as Serapion's report): \"He wrote that he saw what one Marcianus held: a man who contradicted himself, not understanding what he said.\""

**R2. The leftovers the fixer flagged conflict with B1 and B5.** These are writer notes, but they sit next to Do not say rows that bar their own words. A writer who follows them gets "letter" or "never canon" back.

- Header (line 3): "spoken name **Christian Apocrypha**, or in full \"the books that were never canon\" (census `shortName`, `informalName`)." → "spoken name **Christian Apocrypha**, brought in as \"books that never entered the New Testament: the Christian Apocrypha\" (census `shortName`; the census `informalName`, \"the books that were never canon\", is not spoken, Review B5)."
- Connection (line 103): "passed to Eusebius, who kept his letter and sorted the books by it" → "passed to Eusebius, who kept what he wrote to them and sorted the books by it"
- Who tells it (line 123), Source cell: "Serapion's letter, in Eusebius, Church History 6.12" → "Serapion's writing On the so-called Gospel according to Peter (a λόγος, listed apart from his letters), in Eusebius, Church History 6.12"
- Who tells it (line 123), Credited cell: "inside the sentence about Serapion's letter, that Eusebius kept it." → "inside the sentence about what Serapion wrote to them, that Eusebius kept it."
- Links (line 115): "kept Serapion's letter; sorted the books." → "kept what Serapion wrote to Rhossus; sorted the books."
- Length (line 18): "Eusebius keeps Serapion's letter" → "Eusebius keeps what Serapion wrote"

## Length

The live brief has 672 words. Net of the review's fixed changes it comes to 658. With R1 it reaches 675, at the cap. The other changes are notes only and add no words.
