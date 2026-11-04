# Rendering Review: hal quote records, batch 2 (16 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 16 `hal.quote` records.

## Method

Each record's `text`, `modern_rendering`, `sources[].locus`, `confidence.divergence_note` and `use_note.not_for` were read from `records/hal/quote/`. Where the locus gave no file, the passage was found by its work and section in the vendored file (Jerome's letters in `npnf206`; Innocent's Letter CXXXVII, which travels in the Jerome volume, also in `npnf206`; Augustine's Letter 71 in `npnf101`). The text check is a script run against the vendored file. It strips `<note>` blocks and other tags, unescapes entities, folds whitespace (U+00A0 included), rejoins line-end hyphens, and treats "..." as an elision. Each `text` is then searched for verbatim, and its first and last words are mapped back to file lines. Every span was also read by eye, with its surrounding context, for reported-speech frames, editorial brackets and endnotes. Sentence lengths in each rendering were counted by hand, word by word. Hyphenated compounds count as one word, and dashes and ellipses as none.

## Results

**16 records: 15 PASS, 1 FAIL (0 P1, 1 P2).**

| Record id (hal.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| i-gather-the-rose-from-the-thorns | cic/texts/npnf206_jerome-principal-works.xml, lines 6021-6023 | pass | all clauses, near-verbatim; "but it is because they give me virgins" kept; longest 16 | PASS |
| innocent-ravages | cic/texts/npnf206_jerome-principal-works.xml, lines 28468-28474 | pass | "which they say" kept as "They say the devil has done these things"; the human agent is still unnamed; longest 19 | PASS |
| let-her-be-brought-up-in-a-monastery | cic/texts/npnf206_jerome-principal-works.xml, lines 20730-20734 | pass | all eight jussive clauses kept and still commands (prescription, not report); longest 17 | PASS |
| no-one-preferred-to-the-seventy | cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml, lines 36730-36743 | pass | "although ... still" concession carried by "Still,"; "the Jews acknowledge" / "contend" kept as the Jews' claims; elision kept; longest 23 | PASS |
| oea-tumult | cic/texts/npnf101_augustine-confessions-letters.xml, lines 32546-32550 | pass | "such a tumult ... that" kept as "so great that"; "especially among the Greeks" kept; Oea parenthesis is Augustine's own; longest 20 | PASS |
| partially-acquired-hebrew | cic/texts/npnf206_jerome-principal-works.xml, lines 22016-22019 | pass (a `<pb>` page-break tag splits "unceas-ingly" in the file; the joined word matches) | "partially" kept, so the claim stays modest; "lest" rendered "in case"; longest 21 | PASS |
| paula-escaped-his-envy | cic/texts/palladius_paradise-v1-syriac_budge1907.txt, line 1233 | pass | "he told me" frame kept on the Paula claim, as the divergence note requires; envy and evil-eyedness kept (not temper); longest 25 | PASS |
| paula-hebrew-psalms | cic/texts/npnf206_jerome-principal-works.xml, lines 22019-22022 | pass | "it" made explicit as Hebrew (grammatical); "too" kept; "pronunciation peculiar to Latin" kept as "Latin accent"; longest 21 | PASS |
| portus-strangers | cic/texts/npnf206_jerome-principal-works.xml, lines 17716-17718 | pass | both clauses kept; "strangers" left as the source has it; longest 15 | PASS |
| recourse-to-marcella | cic/texts/npnf206_jerome-principal-works.xml, lines 26177-26179 | pass | "recourse was had to her" given as people turning to her, with no office implied; longest 20 | PASS |
| rome-resounded | cic/texts/npnf206_jerome-principal-works.xml, lines 8636-8641 | pass | Jerome's self-report kept in the first person; "worthy of the episcopate" kept as "worthy to be a bishop", not a candidacy; longest 14 | PASS |
| rufinus-writes-because-rome-is-where-the-news-is | cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml, lines 45939-45949 | pass | "I venture to believe", "may have been directed" and "I hear it reported" hedges all kept; every clause rendered; longest 22 | PASS |
| she-put-on-sackcloth | cic/texts/npnf206_jerome-principal-works.xml, lines 17449-17464 | pass | "Who would believe it?" is cut loose from its object and now reads as disbelief that her husband died | FAIL P2 |
| the-city-which-had-taken-the-whole-world | cic/texts/npnf206_jerome-principal-works.xml, lines 26320-26325 | pass | "as I dictate" kept; "nay more" given as "Worse"; "famine was beforehand with the sword" kept; longest 19 | PASS |
| they-have-left-untold-the-name | cic/texts/npnf206_jerome-principal-works.xml, lines 28468-28474 | pass | same text and rendering as innocent-ravages; "they say" frame kept; nobody named; longest 19 | PASS |
| those-of-my-own-order | cic/texts/npnf206_jerome-principal-works.xml, lines 6367-6371 | pass | "I speak of those of my own order" kept as an aside; satire kept as Jerome's own; longest 25 | PASS |

## Failed renderings: corrected text

**she-put-on-sackcloth.** The edition asks one rhetorical question: "Who would believe that, after the death of her second husband ... that at this time Fabiola came to herself?" The rendering cuts this down to "Who would believe it?" and puts "Her second husband had died" straight after it. The question now seems to doubt the husband's death, not Fabiola's turn. The edition's "Yet it was then" is also moved, so the incredulity frame no longer points where Jerome points it. Neither bracket in the span is an editor's supplement: both parentheses are Jerome's own, and the Lateranus endnote is left out.

Corrected rendering:

> Her second husband had died. At such a time most widows shake off the yoke of servitude. They grow careless and allow themselves more liberty than ever... Who would believe that at this very time Fabiola came to herself? Yet it was then that she put on sackcloth to make public confession of her error. It was then that she stood in the ranks of the penitents, in the presence of all Rome. This was in the basilica that once belonged to that Lateranus who died by the sword of Caesar. Before bishop, presbyters and people she showed her disheveled hair, pale features, soiled hands and unwashed neck. They all wept when they saw her weep.
