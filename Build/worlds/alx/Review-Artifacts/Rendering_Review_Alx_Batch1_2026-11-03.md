# Rendering Review: alx quote records, batch 1 (26 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 26 `alx.quote` records.

## Method

Each record's `text` is searched for in the vendored edition files in `cic/texts/` (ANF02, ANF04, ANF06, ANF09, NPNF1-2/01, NPNF2-04, NPNF2-14, and the Lewis 1911 Philocalia). The XML is normalized before matching: `<note>` blocks and all tags are stripped, entities are decoded, soft hyphens (U+00AD) and line-end hyphens are rejoined, and whitespace (including U+00A0) is folded. A "..." in `text` splits the search into segments. Line spans run from the line holding the quote's first word to the line holding its last word. Where the edition puts a section number (such as "2." or "5.") inside the quoted span, the record leaves it out. This is noted as apparatus and does not count as a text difference.

Each rendering is read clause by clause against the edition text, the record's `confidence.divergence_note` and its `use_note.not_for`. Sentence length is counted by splitting on sentence-final punctuation and counting space-separated words. The bracket rule is applied too: a bracketed or parenthetical supplement by an editor or translator must not be voiced as the source's own where it adds meaning. Reported-speech frames and the source's hedges must be kept.

## Results

**26 records: 22 PASS, 4 FAIL (1 P1, 3 P2).**

| Record id (alx.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| a-doctrine-they-would-not-have-taught | cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml, lines 41593-41600 | pass | all clauses; "I hold" kept; "not only ... but" split into two sentences, sense intact; longest 20 | PASS |
| appointed-by-the-fathers-to-be-read | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 68817-68823 | pass | all clauses; "writing of necessity" carried by "I must"; full book list; longest 25 (the list) | PASS |
| athanasius-death-trampled-down | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 17442-17450 | pass (edition section number "2." left out) | both conditionals kept ("if", "If so"); "sojourn" as "stay among us"; longest 23 | PASS |
| athanasius-fountains | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 68808-68811 | pass | all three sentences; add/take-away command kept; longest 19 | PASS |
| athanasius-made-god | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 18743-18744 | pass | "made God" kept, not softened; ellipsis kept; 12 | PASS |
| clement-bee | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 27492-27495 | pass | all clauses; no name added for "He"; longest 14 | PASS |
| clement-instructor | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 18785-18786 | pass | clauses complete, but "unnatural passions" now reads as sexual vice; longest 20 | FAIL P2 |
| clement-new-song | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 15213-15218 | pass | all clauses; "as dead" kept as a likeness; longest 25 | PASS |
| clement-possessions | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 56548-56558 | pass | every quality in the long sentence kept, in order; "meet heir" as "fit heir"; longest 17 | PASS |
| clement-rash-martyrdom | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 37819-37827 | pass | Clement's own parenthesis rendered as his; "banish themselves" as "cast themselves out", not exile; longest 21 | PASS |
| clement-schoolmaster | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 27890-27895 | pass | "Perchance" hedge kept as "Perhaps"; "schoolmaster" as "guardian"; law/Hebrews parallel kept; longest 21 | PASS |
| couches-and-trenchers-and-bowls | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 22127-22136 | pass | every item kept; "thyine" as "citron wood"; "relinquished" as "given up"; longest 23 | PASS |
| demetrius-accused-him-bitterly | cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml, lines 33217-33233 | pass (edition section number "5." left out) | all clauses; Eusebius's "overcome by human weakness" stays in his narration; longest 22 | PASS |
| dionysius-nepos | cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml, lines 41312-41318 | pass | all clauses; "extensive psalmody" as "many psalms"; longest 20 | PASS |
| dionysius-plague | cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml, lines 41084-41090 | pass | "The most of" kept as "Most"; all clauses; longest 20 | PASS |
| dionysius-too-high-for-me-to-grasp | cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml, lines 41418-41428 | pass (edition section number "5." left out) | "I suppose", "I suspect" hedges kept; all clauses; longest 21 | PASS |
| ecclesiastical-and-apostolical-tradition | cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml, lines 22432-22438 | pass | "think they hold" kept; succession and "to this day" kept; longest 23 | PASS |
| gregory-spark | cic/texts/anf06_gregory-thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml, lines 3017-3021 | pass | both objects of love kept; "like some spark" simile kept; longest 25 | PASS |
| no-festal-letter-was-written | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 64366-64369 | pass | clauses complete, but one sentence joins the flight and the search, 26 words, and adds "men" as searchers | FAIL P2 |
| no-sun-no-moon-no-sky | cic/texts/anf04_tertullian4-minucius-felix-commodian-origen1-2.xml, lines 33725-33732 | pass (soft hyphens rejoined) | all clauses; "as it were" kept as "so to speak"; questions kept as questions; longest 24 | PASS |
| origen-gospel-firstfruits | cic/texts/anf09_gospel-of-peter-diatessaron-origen-commentaries.xml, lines 20575-20577 | pass | "make bold" kept; "firstfruits" kept; longest 15 | PASS |
| origen-punishment-heals | cic/texts/origen_philocalia_lewis1911.txt, line 436 | pass | "we think" kept; all three nouns; longest 23 | PASS |
| origen-scripture-senses | cic/texts/origen_philocalia_lewis1911.txt, line 76 | pass | analogy and purpose clause kept; longest 15 | PASS |
| the-grades-here-in-the-church | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 47889-47900 | pass | translator's bracket "[as deacons]" voiced as Clement's own words | FAIL P1 |
| timothy-ordinary-questions | cic/texts/npnf214_seven-ecumenical-councils.xml, lines 44111-44164 | pass | Questions VIII, X, XI fine; in Question I, "may be present ... and eat" reads as permission, not as the case put | FAIL P2 |
| to-believe-or-disbelieve | cic/texts/anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml, lines 40327-40330 | pass | definition, examples and conclusion kept; longest 19 | PASS |

## Failed renderings: corrected text

**clement-instructor (FAIL P2).** The rendering keeps "unnatural passions" from the 1885 English. To a modern reader that phrase points to sexual vice. Clement means the soul's disordered feelings and appetites, the ones contrary to nature, which the record's own `not_for` also flags. The phrase needs rewording so the misleading sense goes away.

Corrected rendering:

> So our Instructor, the Word, cures the passions of the soul that go against its nature. He does this by urging us on.

**no-festal-letter-was-written (FAIL P2).** The second sentence joins two thoughts (Athanasius's flight and the search for him) and runs to 26 words. It also brings in "men" as the searchers, which the edition does not name; there the search is told in the passive.

Corrected rendering:

> Then George entered on the thirtieth of Mechir and acted with excessive violence. But Athanasius the Bishop had fled. He was searched for in the city with great harshness, and many people were in danger because of it. Therefore no Festal Letter was written.

**the-grades-here-in-the-church (FAIL P1).** The edition reads "will first minister [as deacons]". The square brackets mark a translator's or editor's supplement. "As deacons" adds meaning: it names the office the verb "minister" is taken to mean. The rendering voices it plainly as Clement's own ("will first serve as deacons"), so the supplement has to stay marked. The rest of the rendering is sound.

Corrected rendering:

> In my view, the ranks here in the Church, of bishops, presbyters and deacons, imitate the glory of the angels. They also imitate the order which, the Scriptures say, awaits those who have followed in the footsteps of the apostles. These people have lived in perfect righteousness, as the Gospel teaches. For those taken up in the clouds, the apostle writes, will first serve [as deacons]. Then they will be ranked among the presbyters, promoted in glory, for one glory differs from another. This goes on until they grow into "a perfect man."

**timothy-ordinary-questions (FAIL P2).** In Question I the edition sets out a case: "If a lad ..., being present at the oblation, does eat of it through ignorance". The rendering's "may be present at the offering and eat of it" can be read as granting permission. That misleads, because this is a ruling on what to do after it has happened. The other questions are sound.

Corrected rendering:

> Question I. Suppose a boy of seven, or a man, is a catechumen. He is present at the offering and eats of it in ignorance. What should be done in this case? Answer. Let him be illuminated, that is, baptized, for he is called by God. ... Question VIII. Should a woman who has just given birth keep the Paschal fast? Answer. No. ... Question X. Is a sick man required to keep the Paschal fast? Answer. No. Question XI. A clergyman is called to celebrate a marriage, and he has heard that it is incestuous. Should he comply and perform the offering? Answer. No; he must not share in other men's sins.
