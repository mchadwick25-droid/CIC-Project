# Rendering Review: desert quote records, batch 3 (20 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 20 `desert.quote` records.

## Method

Each record's `text` was checked against the vendored edition in `cic/texts/`. For the XML editions (NPNF 2/4, NPNF 2/11), `<note>…</note>` blocks and all tags were stripped, curly quotes and dashes folded, and whitespace (including U+00A0) collapsed. Each `...`-separated segment of `text` was then matched in full against the stripped file. Line spans were then confirmed by reading the raw file lines. The plain-text editions (Dysinger's Praktikos, Mason's Macarian Homilies, Schodde's Ethiopic Pachomian rules, Budge's Paradise) were matched the same way and read directly.

Each `modern_rendering` was read clause by clause against the edition lines, not against `text` alone. Sentence length was counted by hand in words for every sentence near or above 20 words. `confidence.divergence_note` and `use_note.not_for` were read for each record and checked where they bear on wording.

Sources read: `cic/texts/npnf204_athanasius-select-works-letters.xml` (Vita Antonii §§2, 41, 74, 75, 79); `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (Institutes II.5; Conferences III.6, X.3, XIII.18, XVIII.4); `cic/texts/evagrius_praktikos_dysinger.txt` (prologue 8; chs. 2, 3, 6, 12, 64); `cic/texts/macarius_fifty-spiritual-homilies_mason1921.txt` (Homilies I, XVII); `cic/texts/pachomius_rules-ethiopic_schodde1885.txt` (Parts I, II); `cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt` (saying 610).

## Results

**20 records: 19 PASS, 1 FAIL (0 P1, 1 P2).**

| Record id (desert.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| the-coming-of-christ-made-thee-weak | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 32256-32259 | pass | all clauses; "at length" as "at last"; final clause split in two; longest 21 | PASS |
| the-deeds-of-christ-prove-him | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 33068-33076 | pass | both segments; list of signs kept whole across two questions; "which shew" carried; longest 21 | PASS |
| the-eight-generic-thoughts | cic/texts/evagrius_praktikos_dysinger.txt, lines 188-197 | pass | all eight in order, "and with it" kept; "not up to us / up to us" contrast kept; longest 20 | PASS |
| the-heart-is-a-deep-gulf | cic/texts/macarius_fifty-spiritual-homilies_mason1921.txt, lines 6320-6326 | pass | every clause; "only, I say" kept; implied "perfection" supplied without new sense; longest 19 | PASS |
| the-kingdom-is-apatheia | cic/texts/evagrius_praktikos_dysinger.txt, lines 174-177 | pass | both definitions kept separate; "according to the capacity of the nous" and "bestowing incorruptibility" carried; longest 19 | PASS |
| the-ladder-from-faith-to-love | cic/texts/evagrius_praktikos_dysinger.txt, lines 159-161 | pass | each step of the chain in order; love as door to knowledge and theology, not summit; longest 18 | PASS |
| the-main-share-is-not-our-works | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 38592-38594 | pass | fragment rendered whole; "merit of our own works" kept; 20 words | PASS |
| the-noonday-demon | cic/texts/evagrius_praktikos_dysinger.txt, lines 216-224 | pass | all six numbered stages and close; "as they say" and "the demon adds" kept; translator's clock glosses kept; longest 24 | PASS |
| the-nous-beholds-its-own-radiance | cic/texts/evagrius_praktikos_dysinger.txt, line 443 | pass | three signs kept; "matters" rendered "events", which narrows the sense | FAIL P2 |
| the-soul-becomes-all-eye | cic/texts/macarius_fifty-spiritual-homilies_mason1921.txt, lines 1526-1531 | pass | communion, irradiation, seat and dwelling, all light/face/eye, eyes of light all kept; longest 15 | PASS |
| the-word-took-a-human-body | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 33023-33026 | pass | "not changed", "being the same", purpose and partaking clauses kept; longest 22 | PASS |
| they-have-taken-away-my-god | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 36051-36054 | pass | every clause; "worship and address" both kept; longest 10 | PASS |
| three-hundred-acres-to-the-villagers | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 31246-31252 | pass | "as though" hedge kept; acreage and qualities kept; purpose clause with sister kept; longest 21 | PASS |
| three-kinds-of-monks | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 42461-42470 | pass | all three orders and their descriptions; "we too hope" kept; longest 17 | PASS |
| three-renunciations-solomon | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 28479-28486 | pass | three books mapped in order with each reason; edition's lower-case "word of God" given as "Word", within the sense; longest 13 | PASS |
| three-years-a-servant | cic/texts/pachomius_rules-ethiopic_schodde1885.txt, line 174 | pass | three-year term, servant-only status, entry after term all kept; longest 18 | PASS |
| twelve-psalms-by-an-angel | cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml, lines 17184-17211 | pass | long period broken into single thoughts; every clause carried, incl. weak brethren, 50/60/beyond, Egyptian sitting custom, Alleluia, disappearance; chanter not named as angel; longest 24 | PASS |
| when-the-cross-of-christ-arose | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 33134-33145 | pass | both segments; three rhetorical questions kept; longest 17 | PASS |
| whence-canst-thou-prove-to-us | cic/texts/anan-isho_paradise-v2-sayings_budge1907.txt, line 2750 | pass | question, parable, three worldly seeds, three grades of monks all kept; elder unnamed; longest 20 | PASS |
| womens-house-across-the-river | cic/texts/pachomius_rules-ethiopic_schodde1885.txt, line 206 | pass | sister unnamed; crossing limits, burial by the brethren, numbers, command all kept; longest 26, within "about 25" | PASS |

## Failed renderings: corrected text

**the-nous-beholds-its-own-radiance** (FAIL P2). The edition reads "it looks at matters calmly." The rendering gives "events," which narrows the sense to happenings. The edition's word covers things and affairs in general. Everything else in the rendering holds.

Corrected rendering:

> The proof of apatheia is this: the nous begins to see its own gentle radiance. It stays calm in the presence of visions during sleep. And it looks at matters calmly.
