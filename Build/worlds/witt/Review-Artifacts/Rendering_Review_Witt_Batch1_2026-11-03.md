# Rendering Review: witt quote records, batch 1 (13 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 13 `witt.quote` records.

## Method

Each record's `text`, `modern_rendering`, `sources[].locus`, `confidence.divergence_note` and `use_note.not_for` were read from `records/witt/quote/`. The passage was located in the vendored edition in `cic/texts/` (by the locus's file and lines where given, otherwise by grepping a distinctive phrase), and the tight line span was read directly. The text check is a script comparison: line-end hyphens rejoined, the footnote caret (`^`) dropped, whitespace (including U+00A0) folded, then a substring test of the record's `text` against the span. The rendering was read clause by clause against the edition text. Sentence lengths were counted by script (sentences split at `.`, `!`, `?` and line breaks; words counted as runs of letters, digits and apostrophes) and spot-checked by hand. No record contains an editor's or translator's square-bracketed supplement; the parentheses in the Large Catechism and Admonition passages are the author's own and are rendered as his.

Sources read: `cic/texts/melanchthon_augsburg-confession_anon-pg275.txt`, `cic/texts/luther_small-catechism_smith1994.txt`, `cic/texts/luther_large-catechism_bente-dau1921.txt`, `cic/texts/luther_works-v4-selected_various1931.txt`.

## Results

**13 records: 12 PASS, 1 FAIL (1 P1, 0 P2).**

| Record id (witt.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| article-ii-of-original-sin | cic/texts/melanchthon_augsburg-confession_anon-pg275.txt, lines 194-203 | pass | all clauses; "concupiscence" as "evil desire", "vice of origin" as "inborn fault"; longest 26 (about 25, acceptable) | PASS |
| article-ix-of-baptism | cic/texts/melanchthon_augsburg-confession_anon-pg275.txt, lines 309-315 | pass | all clauses; offered-and-received clause kept as its own sentence; longest 18 | PASS |
| as-when-one-must-kill-a-mad-dog | cic/texts/luther_works-v4-selected_various1931.txt, lines 11945-11963 | pass | all clauses, nothing softened; "smite, slay, and stab" as "strike, kill and stab"; longest 20 | PASS |
| christs-return-to-judgment | cic/texts/melanchthon_augsburg-confession_anon-pg275.txt, lines 435-445 | pass | all clauses; both condemnations kept, "Jewish opinions" kept as the source's; longest 25 | PASS |
| congregation-of-saints | cic/texts/melanchthon_augsburg-confession_anon-pg275.txt, lines 277-285 | pass (text stops at "etc.", before the editor's "Eph. 4, 5. 6.") | all clauses; "congregation" as "community", "administered" as "given"; "etc." as "and so on"; longest 23 | PASS |
| neither-court-nor-mercy | cic/texts/luther_works-v4-selected_various1931.txt, lines 13440-13462 | pass | all clauses; "court" as "a trial"; mercy-for-captives claim kept as Luther's own; longest 24 | PASS |
| nothing-that-varies | cic/texts/melanchthon_augsburg-confession_anon-pg275.txt, lines 1543-1549 | pass | all clauses; "Church Catholic" as "universal Church" (not Rome, per not_for); longest 23 | PASS |
| second-article-of-the-creed | cic/texts/luther_small-catechism_smith1994.txt, lines 195-211 | pass | all clauses of creed and explanation; adverbs as "in righteousness, innocence and blessedness"; longest 23 | PASS |
| the-poor-man-who-comes-to-you | cic/texts/luther_large-catechism_bente-dau1921.txt, lines 1946-1956 | pass | conditional kept ("may ... Then"); "(I say again)" kept; longest 19 | PASS |
| the-sword-is-at-your-throats | cic/texts/luther_works-v4-selected_various1931.txt, lines 10419-10432 | pass | all clauses; Latin tag left out, its English kept; "Psalm cvi" (Vulgate) given as "Psalm 107", the same psalm in modern numbering; longest 24 | PASS |
| the-time-of-the-sword | cic/texts/luther_works-v4-selected_various1931.txt, lines 12155-12163 | pass | all clauses; "lay about them" as "strike out all around them"; souls claim kept as the tract's; longest 24 | PASS |
| you-too-must-have-a-care | cic/texts/luther_works-v4-selected_various1931.txt, lines 10671-10679 | pass | "the princes and lords, who forbid ... and oppress" made into flat claims about all princes and lords | FAIL P1 |
| your-own-judges | cic/texts/luther_works-v4-selected_various1931.txt, lines 10814-10826 | pass | all clauses; "equity" as "fairness", "ordinance" as "order"; longest 20 | PASS |

## Failed renderings: corrected text

**you-too-must-have-a-care.** The edition ties the concession to particular rulers: it is "the princes and lords, who forbid the preaching of the Gospel and oppress the people so unbearably" who deserve to be put down. The rendering turns that clause into two free-standing claims ("The princes and lords forbid the preaching of the Gospel. They oppress the people beyond bearing."), so Luther appears to say that princes and lords as a class do these things and deserve overthrow, and the "one thing" he admits is spread over five sentences.

Corrected rendering:

> So far, dear friends, you have learned only one thing I admit. Sad to say, it is all too true and certain. It concerns the princes and lords who forbid the preaching of the Gospel and oppress the people beyond bearing. They deserve, and have fully earned, that God should put them down from their seats. They are men who have sinned deeply against God and man. And they have no excuse. Even so, you too must take care. You must take up your cause with a good conscience and with justice.
