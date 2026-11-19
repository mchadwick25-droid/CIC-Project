# Rendering Review: ijc quote records, batch 1 (20 records)

- **Reviewer:** Opus 5.5 (independent; did not draft or render any of these records)
- **Date:** 2026-11-03
- **Subject:** the `text` and `modern_rendering` of 20 `ijc.quote` records.

## Method

Each record's `text`, `modern_rendering`, `sources[].locus`, `confidence.divergence_note` and `use_note.not_for` were read from `records/ijc/quote/<id>.md`. The passage was then read at the cited lines of the vendored file in `cic/texts/` (or found by a distinctive phrase where the locus gives no lines). The text check strips `<note>` elements and other markup, rejoins line-end hyphens and folds whitespace; "..." in `text` is read as an elision. The Ammianus file is a raw OCR text layer, so its differences are named as OCR misreads where they are plainly that. For the rendering check, each rendering was compared clause by clause against the edition text. Sentence lengths were counted by a script that splits on sentence-final punctuation, and the longest sentences were then recounted by hand. Bracketed editorial supplements were checked under the bracket rule: a supplement that adds meaning must stay bracketed or be left out; a purely grammatical one may be rendered plainly.

## Results

**20 records: 19 PASS, 1 FAIL (1 P1, 0 P2).**

| Record id (ijc.quote.…) | Edition text at (file, lines) | Text check | Rendering check | Verdict |
|---|---|---|---|---|
| a-fine-talent-for-making-verses | cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml, lines 41382-41385 | pass | all clauses; "heroic metre" given as the verse form of epic poetry, not subject matter; longest 15 | PASS |
| ambrose-blessing-changes-nature | cic/texts/npnf210_ambrose-select-works-letters.xml, lines 33203-33205 and 33263-33271 | pass | all clauses of IX.50 and IX.54; "consecrated" as "made holy", "signified" as "meant"; no later technical terms; longest 20 | PASS |
| ambrose-cannot-surrender | cic/texts/npnf210_ambrose-select-works-letters.xml, lines 41754-41755 | pass | both clauses; "may not fight" as "must not fight" keeps the sense of what is not permitted; longest 13 | PASS |
| ambrose-dare-not-offer | cic/texts/npnf210_ambrose-select-works-letters.xml, lines 44181-44186 | pass | all clauses; the disclaimer of a charge kept; "I do not think so" kept; longest 18 | PASS |
| ambrose-emperor-in-church | cic/texts/npnf210_ambrose-select-works-letters.xml, lines 42660-42665 | pass | all clauses; "As it is said, it is said without sin" kept; longest 16 | PASS |
| ammianus-roman-luxury | cic/texts/ammianus-marcellinus_roman-history_yonge1862.txt, lines 23191-23207 | pass except OCR misreads only ("1"/"I", "vastuess"/"vastness", "east"/"cast", "sober-mirfded"/"sober-minded"), disclosed in the divergence note | all clauses; "I do not deny" hedge and "may be justified" kept; the vices clause and the priests' description fully rendered; longest 24 | PASS |
| ammianus-sicininus-massacre | cic/texts/ammianus-marcellinus_roman-history_yonge1862.txt, lines 23176-23189 | pass (OCR section numbers and footnote mark lie outside the quoted words) | all clauses; "It is certain that" kept; partisan violence kept; longest 25 | PASS |
| augustine-vigil-hymns | cic/texts/npnf101_augustine-confessions-letters.xml, lines 13765-13775 | pass | all clauses on both sides of the elision; "lest the people should pine away" given as purpose; longest 20 | PASS |
| canon28-equal-privileges | cic/texts/npnf214_seven-ecumenical-councils.xml, lines 22223-22232 | pass | all clauses; "justly judging" kept as the bishops' judgment; "the Fathers" left as is; longest 23 | PASS |
| canon3-new-rome | cic/texts/npnf214_seven-ecumenical-councils.xml, lines 14398-14400 | pass | both clauses; singular "prerogative of honor" kept; longest 16 | PASS |
| chalcedon-definition | cic/texts/npnf214_seven-ecumenical-councils.xml, lines 20287-20296 | pass | "[of God]" kept bracketed, but the editor's "[united]" is voiced as the source's own and recasts the four adverbs as a statement of union; longest 20 | FAIL P1 |
| compelled-to-come-in | cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, lines 19616-19617 and 19624 | pass | all clauses of both parts; the condition "if that power is what compels" kept; ends at the verbatim break, adding nothing from the paraphrase; longest 25 | PASS |
| constantine-bishop-outside | cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml, lines 66731-66733 | pass | both clauses; "ordained" as "appointed" avoids a priestly sense; longest 15 | PASS |
| eutropius-right-of-refuge | cic/texts/npnf109_chrysostom-priesthood-ascetic-homilies-statutes.xml, lines 17737-17746 | pass | all clauses; "you say" frame kept; "right of refuge" kept; longest 21 | PASS |
| happy-christian-emperors | cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml, lines 11060-11094 | pass | every "if" condition rendered as its own sentence; "happy" kept throughout; longest 25 | PASS |
| he-deferred-it-in-the-hope | cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml, lines 67751-67761 | pass | all clauses; the motive stays framed as his belief ("He firmly believed", "would"); longest 21 | PASS |
| he-held-aloof-for-a-short-time | cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml, lines 2972-2978 | pass | all clauses; "after mature consideration" attached to his assent, a fair reading; longest 26, within "about 25" | PASS |
| hymns-and-psalms-should-be-sung | cic/texts/npnf101_augustine-confessions-letters.xml, lines 13767-13775 | pass | all clauses; "still unmelted by the heat of Thy Spirit" kept as Augustine's own distance; longest 20 | PASS |
| jerome-damasus-verses | cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml, lines 41382-41385 | pass | all clauses; "heroic metre" given as the verse form of epic poetry, not subject matter; longest 15 | PASS |
| julius-custom | cic/texts/npnf204_athanasius-select-works-letters.xml, lines 23549-23552 | pass | both questions; the appeal to "the custom" kept as a claim; longest 25 | PASS |

## Failed renderings: corrected text

**chalcedon-definition (FAIL P1).** In the edition, "[united]" is the translator's bracketed supplement. The four adverbs qualify how Christ is confessed "in two natures". The rendering's "The two are united without mixing, without change, without division, and without separation" voices that supplement as the Council's own words and turns the adverbs into a new statement of union. That adds sense under the bracket rule. "[of God]" is correctly kept bracketed. The corrected rendering keeps both supplements bracketed and keeps the adverbs attached to the confession.

Corrected rendering:

> This one and the same Jesus Christ, the only-begotten Son [of God], must be confessed to be in two natures. He is confessed in them without mixing, without change, without division and without separation [united]. The difference between the natures is not taken away by such union. Rather, the special character of each nature is kept. Both are united in one Person and subsistence. He is not separated or divided into two persons. He is one and the same Son and only-begotten, God the Word, our Lord Jesus Christ...
