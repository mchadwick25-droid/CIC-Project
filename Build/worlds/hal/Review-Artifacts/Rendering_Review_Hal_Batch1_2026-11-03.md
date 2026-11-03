# Rendering Review: hal quote records, batch 1 (16 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 16 `hal.quote` records.

## Method
Each record's `text` was searched in the vendored edition file named by its locus, or by the work it cites: `cic/texts/npnf206_jerome-principal-works.xml` (Jerome's letters and Vulgate prefaces), `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (Sulpitius, Dialogues), and `cic/texts/palladius_lausiac-history_clarke1918.txt` (Lausiac History). The XML was flattened with `<note>…</note>` and all tags removed, whitespace (including U+00A0) folded, and typographic quotes and dashes folded to plain ones. Each `...`-separated part of `text` was then matched as an exact substring, and the first and last file lines of the match were recorded. The matched spans were also read in the raw file. Sentence lengths were counted by hand, word by word, on every sentence that could come near 25 words. Each rendering was read clause by clause against the edition text and checked against `confidence.divergence_note` and `use_note.not_for`. No text in this batch carries an editor's bracketed supplement.

## Results
**16 records: 13 PASS, 3 FAIL (1 P1, 2 P2).**

| Record id (hal.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| a-follower-of-cicero-and-not-of-christ | cic/texts/npnf206_jerome-principal-works.xml, lines 6479-6489 | pass (endnote 577 stripped; quote marks folded) | all clauses; "caught up in the spirit" kept; Matt. 6:21 kept in the Judge's speech; longest 24 | PASS |
| a-man-truly-catholic | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 2859-2862 | pass | all clauses; "was thought at first" hedge kept; "Catholic" as "orthodox" avoids the denominational sense; reversal kept | PASS |
| always-at-his-books | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 2960-2962 | pass | all four clauses; nothing added; longest 9 | PASS |
| boxwood-letters | cic/texts/npnf206_jerome-principal-works.xml, lines 20402-20404 | pass | all clauses; advice kept as imperative; "letters" plainly alphabet pieces; longest 18 | PASS |
| buried-beneath-the-church | cic/texts/npnf206_jerome-principal-works.xml, lines 22130-22133 | pass | all clauses, but second sentence runs to 30 words | FAIL P2 |
| city-taken | cic/texts/npnf206_jerome-principal-works.xml, lines 26320-26325 | pass (endnote 3578 stripped) | all clauses; "nay more" as "Worse"; "beforehand with the sword" as "got there before the sword"; longest 18 | PASS |
| detestable-monks | cic/texts/npnf206_jerome-principal-works.xml, lines 8111-8115 | pass | all five sentences; crowd's words kept as speech; nothing added | PASS |
| dispute-to-learn | cic/texts/npnf206_jerome-principal-works.xml, lines 26166-26170 | pass | all clauses; "as she saw" kept; "not for argument's sake" rendered; longest 21 | PASS |
| dream-follower-of-cicero | cic/texts/npnf206_jerome-principal-works.xml, lines 6483-6486 | pass (endnote 577 stripped) | all clauses; scripture saying kept; longest 14 | PASS |
| ever-let-the-bridegroom-sport-with-you | cic/texts/npnf206_jerome-principal-works.xml, lines 6222-6228 | pass (endnotes 527-529 stripped) | all clauses; "sport" as "take his delight" fits not_for; "hole" as "opening"; longest 18 | PASS |
| eyes-of-faith | cic/texts/npnf206_jerome-principal-works.xml, lines 21139-21143 | pass | sentences 2-3 drop both "she protested that" and "with the eyes of faith", so they state her sight as plain narrated fact | FAIL P1 |
| fabiola-hospital | cic/texts/npnf206_jerome-principal-works.xml, lines 17541-17544 | pass | all clauses; priority claim left as Jerome's statement; "want" as "poverty"; longest 18 | PASS |
| hail-bethlehem | cic/texts/npnf206_jerome-principal-works.xml, lines 21151-21153 | pass (endnotes 2789-2790 stripped; quote mark folded) | all clauses; "house of bread" kept; 15 words | PASS |
| helmeted-preface | cic/texts/npnf206_jerome-principal-works.xml, lines 46908-46911 | pass (quote marks folded) | all clauses; "so that we may be assured" as "It is meant to assure us"; longest 19 | PASS |
| hindered-by-jerome | cic/texts/palladius_lausiac-history_clarke1918.txt, line 475 | pass (bare endnote number "276" after "Paula," left out, as the divergence note states) | third sentence runs to 28 words and joins two thoughts; "having induced her" turned into a causal "for" | FAIL P2 |
| house-destroyed | cic/texts/npnf206_jerome-principal-works.xml, lines 28596-28602 | pass (endnote 3896 stripped) | all clauses; "fleshly" as "earthly"; closing maxim kept; longest 20 | PASS |

## Failed renderings: corrected text

**buried-beneath-the-church** (FAIL P2). The second sentence runs to 30 words ("They did this not only for the three days … but for the rest of that week as well"), past the 25-word limit.

Corrected rendering:
> One after another, they chanted the psalms: now in Greek, now in Latin, now in Syriac. This went on for the three days before she was buried beneath the church, close to the cave of the Lord. And it went on not only then, but through the rest of the week.

**eyes-of-faith** (FAIL P1). The edition puts every item in the list under one frame: "she protested in my hearing that she could behold with the eyes of faith". The rendering keeps that frame only in its first sentence. "She could see the wise men…" and "She could see the virgin mother…" are then stated as narrated fact, with no "eyes of faith". This loses the reported-speech frame and leans toward the literal vision that `not_for` rules out.

Corrected rendering:
> In my hearing she declared that she could see, with the eyes of faith, the infant Lord wrapped in cloths and crying in the manger. She said she could also see, with the eyes of faith, the wise men worshipping him and the star shining overhead. In the same way, she said, she could see the virgin mother, the watchful foster-father, and the shepherds coming by night.

**hindered-by-jerome** (FAIL P2). The third sentence runs to 28 words and joins two thoughts with a semicolon. It also turns the participle "having induced her to serve his own plan" into a causal "for", which is stronger than the source's wording.

Corrected rendering:
> Among them was the Roman lady Paula, mother of Toxotius, a woman of great distinction in the spiritual life. A certain Jerome from Dalmatia held her back. She had great gifts and was able to surpass everyone. But he held her back by his jealousy, having led her to serve his own plan.
