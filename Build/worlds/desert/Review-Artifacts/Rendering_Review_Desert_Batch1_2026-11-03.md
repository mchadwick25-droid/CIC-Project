# Rendering Review: desert quote records, batch 1 (21 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 21 `desert.quote` records.

## Method

Each record's `text`, `modern_rendering`, `confidence.divergence_note` and `use_note.not_for` were read from `records/desert/quote/<id>.md`. The passage was located in the vendored file under `cic/texts/` from the record's locus, or by searching a distinctive phrase where the locus gives no file or lines.

The text check used a script that rebuilds each file as one stream with line numbers kept. In XML files it removes `<note>…</note>` and all tags. It joins line-end hyphens after a letter and folds all whitespace, including U+00A0. It then searches for each segment of `text` (split at "..." elisions) and reports the first and last line of the match. A segment that did not match was read by hand in context. Curly and straight quotation marks are treated as one character. A capital at the very start of a quote that begins mid-sentence, a drop-cap capital ("NOW"), and the edition's own page markers ("|97") and bare endnote numbers are counted as typography, not wording. Any other difference is reported as a FAIL.

Each `modern_rendering` was compared clause by clause with the edition text in the file. Sentence lengths were counted by hand, word by word, splitting at sentence-final punctuation. A dash or colon does not end a sentence, and a speech tag counts with the sentence it introduces.

Files read: `npnf204_athanasius-select-works-letters.xml`, `npnf211_sulpitius-severus-vincent-lerins-cassian.xml`, `anan-isho_paradise-v2-sayings_budge1907.txt`, `evagrius_praktikos_dysinger.txt`, `palladius_paradise-v1-syriac_budge1907.txt`, `pachomius_rules-ethiopic_schodde1885.txt`, `palladius_lausiac-history_clarke1918.txt`, `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`.

## Results

**21 records: 19 PASS, 2 FAIL (0 P1, 2 P2).**

One text check fails (`antony-on-living-near-kin`, a capitalisation difference inside the sentence). It is reported in its row and below. The verdict column grades the rendering.

| Record id (desert.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| an-old-man-in-the-next-village | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 31274-31281 | pass | all clauses; "give heed to themselves" as "pay attention to their own soul" is a fair sense; longest 18 | PASS |
| antony-arians-serpents | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 32917-32919 | pass (initial "He" is "he" mid-sentence in the edition) | all clauses; "saying that" frame kept; 18 words | PASS |
| antony-dying-daily | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 31709-31720 | pass (curly quotes in edition) | all clauses across three segments, elisions kept; "allots it daily" as "one day at a time"; not read as despair; longest 16 | PASS |
| antony-nicene-formula | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 32931-32936 | pass (curly quotes in edition) | all clauses; indirect-teaching past tense kept; "it was impious to say" frame kept; longest 15 | PASS |
| antony-not-worsted | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 31499-31505 | pass | all clauses; "brute beasts" as "wild animals"; elision kept; longest 15 | PASS |
| antony-on-living-near-kin | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 47573-47587 | FAIL: edition "the Anchorite system", text "the anchorite system" (the edition's "For" before "when" is cut at the quote's start, which is acceptable) | the elder's closing sentence runs 35 words with its speech tag; "also" moves from "in the world to come also" onto "judged" | FAIL P2 |
| arch-drawn-from-the-centre | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 47381-47390 | pass (curly apostrophe in edition) | all clauses; "a man" as "a builder" is in the image; "without any error" kept in sense; longest 21 | PASS |
| arsenius-flee-tace-quiesce | cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt, line 56 | pass | all clauses; no Latin triad brought in; "fundamental" as "basic"; longest 12 | PASS |
| charity-is-the-offspring-of-apatheia | cic/texts/evagrius_praktikos_dysinger.txt, line 497 | pass | all clauses; "Charity" as "Love" avoids the modern sense; "exists naturally even in those who have not yet believed" kept; longest 19 | PASS |
| christ-worketh-them-not-we | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 33169-33171 | pass | all clauses; Christ kept as the agent; longest 14 | PASS |
| composed-by-bishop-palladius-for-the-prefect-lausus | cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt, line 50 | pass | all clauses of the rubric; "Old Men" as "elders"; Budge's "(sic)" and brackets are editor's marks, not source wording; longest 20 | PASS |
| discretion-greatest-prize | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 27180-27187 | pass | all clauses, but "discretion" is left bare, and its modern sense (tact) misleads, which `not_for` itself names | FAIL P2 |
| eight-principal-faults | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 30132-30137 | pass | all eight terms and glosses in order; "faults" kept, not "sins"; longest 8 | PASS |
| equal-measure-of-strength | cic/texts/palladius_paradise-v1-syriac_budge1907.txt, line 1119 | pass (edition's drop-cap "NOW") | all clauses; purpose clause kept as removing an excuse; longest 20 | PASS |
| ethiopic-rule-eat-and-drink | cic/texts/pachomius_rules-ethiopic_schodde1885.txt, line 174 | pass | all clauses; work by "measure of their eating" kept, not Palladius's strength wording; longest 23 | PASS |
| for-thirty-two-years-i-touched-no-fruit | cic/texts/palladius_lausiac-history_clarke1918.txt, line 495 | pass (edition page marker "\|146" omitted) | all clauses; "as he told us himself" frame kept; "timidity" as "fear"; longest 18 | PASS |
| god-is-not-a-body | cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml, lines 22799-22808 | pass | all clauses; Monas and Henas glossed; "so to speak" kept; "greater and a less" as "greater part and lesser part"; longest 17 | PASS |
| good-good-i-dont-mind | cic/texts/palladius_lausiac-history_clarke1918.txt, line 355 | pass (edition page marker "\|97" and endnote numbers 163, 164 omitted) | all clauses; "Providence ... guiding" kept; "take her" as "keep her"; longest 16 | PASS |
| grace-and-free-will-in-harmony | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 38028-38031 | pass | all clauses; "seem ... but really" kept; "in harmony" as "work together"; longest 13 | PASS |
| he-healed-by-the-name | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 33320-33323 | pass | all clauses; narrator's "it was clear to all" kept; longest 18 | PASS |
| he-longed-to-suffer-martyrdom | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 32370-32386 | pass | all clauses across three segments; "as I said before" kept; "confessors" made plain; longest 26 (about 25) | PASS |

## Failed renderings: corrected text

**antony-on-living-near-kin.** The elder's closing sentence ("The elder said to him: 'You should know this: in the world to come, you will also be judged along with those whose gains and losses…'") runs 35 words. It also moves the edition's "also" ("in the world to come also") onto "judged", and "along with" weakens "in the lot of those". Separately, the record's `text` reads "anchorite system" where the edition prints "Anchorite system" (line 47574).

Corrected rendering:

> As I said, a man came to the elder I mentioned. He said the hermit's way of life deserved no admiration at all. He claimed it took greater virtue to live a life of perfection among other people than in the desert. Blessed Antony asked him where he himself lived. The man said he lived close to his relatives. He boasted that their support freed him from all the care and worry of daily work. He said he gave himself only to reading and prayer, without ceasing and without any distraction of spirit. Blessed Antony spoke again: "Tell me, my good friend, do you grieve over their griefs and misfortunes? Do you rejoice in the same way over their good fortune?" The man admitted he shared in both. The elder said to him, "You should know this. In the world to come, too, you will be judged in the same lot as certain people. They are the people whose gain or loss, whose joy or sorrow, affected you in this life because you shared in it."

**discretion-greatest-prize.** The rendering keeps "discretion" with nothing to fix its sense. In modern English that word first means tact or keeping things private. The record's own `not_for` excludes that sense, and the edition's next clause defines the gift as "a power of discerning". The corrected text carries that meaning at the term's first use, drawn from the passage itself. It also keeps "with unerring judgment" more closely.

Corrected rendering:

> So you see: the gift of discretion, the power to discern, is not an earthly thing, and not a small matter. It is the greatest prize of divine grace. A monk must pursue it with all his zeal. He must gain the power to discern, with judgment that never errs, the spirits that rise up in him. Unless he does, he is sure to go wrong. It will be as if he were in the dark of night, in thick blackness. He will not only fall into dangerous pits and over cliffs. He will also make frequent mistakes in matters that are plain and simple.
