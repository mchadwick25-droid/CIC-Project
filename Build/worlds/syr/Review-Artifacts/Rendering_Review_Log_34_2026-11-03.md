# syr quote renderings: per-rendering review log (34 records)

Date: 2026-11-03. Records: the 34 `syr.quote.*` records, each with a `modern_rendering` and a `text` taken from a vendored source.

What this log is for: it lets the claim "reviewed" be checked, one record at a time. Each row gives the record id (the `syr.quote.` prefix is dropped), the review file or files that read the rendering, and the verdict. All review files are in `Build/worlds/syr/Review-Artifacts/`.

How it was made. Independent Opus 5.5 reviewers read every rendering in 2 batch files (`Rendering_Review_Syr_Batch*_2026-11-03.md`). Each rendering was read against the record's `text` and against the edition text at its locus in `cic/texts/`. The bar: every clause rendered, nothing added, one thought per sentence, no sentence past about 25 words, no word whose modern sense misleads, and the source's own hedges kept. Round 1 failed 12. Each was re-rendered by Opus at the source record and rechecked by a second, independent Opus reader in `Rendering_Review_Syr_Round2_2026-11-03.md`. The independent pull-request review then found one inconsistency: `the-temple-of-the-church-of-the-christians` kept "temple", which round 1 failed in `chronicle-flood-line`, the same edition sentence. It was re-rendered to match and passed a further independent Opus reader (`Rendering_Review_Syr_Temple_2026-11-03.md`). Two round-2 renderings (`sozomen-melodies` and `the-scribes-and-the-prefects-over-the-archives`) then fell below the hard readability floor, FRE 60. They were re-rendered by Opus to clear it, with every clause kept. `tatian-barbaric-writings` took American spelling ("centered"). All three passed a third independent Opus reader (`Rendering_Review_Syr_Round3_2026-11-04.md`).

| Record | Review file(s) | Verdict on the rendering |
|---|---|---|
| a-man-called-wise-amongst-the-jews | Rendering_Review_Syr_Batch1_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md | round 1 FAIL P1; round 2 PASS, after re-rendering |
| a-pearl-upon-the-palm | Rendering_Review_Syr_Batch1_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| abgar-letter | Rendering_Review_Syr_Batch1_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| aphrahat-anti-jewish-frame | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS ("This is" renders the translator's grammatical "(This is)" plainly; all clauses; 16) |
| aphrahat-medicine-penitence | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS (all clauses; "smitten" as "wounded" holds; longest 25) |
| aphrahat-one-innocent | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS ("begotten" as "born", "put on a body" as "taken on a body"; all clauses; 22) |
| aphrahat-persecuted-litany | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS (all five clauses, order kept; longest 12) |
| aphrahat-stone-foundation | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS ("[this]" is a purely grammatical supplement, so rendering it plainly is allowed; all clauses; longest 20) |
| aphrahat-sure-thing | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS (all sixteen titles present and in order; split into "He is" sentences with nothing added; longest 23) |
| as-a-stonecutter-i-have-brought-stones | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS (all clauses; "wrangling" as "quarreling", "edify" as "build up"; longest 17) |
| basil-credits-a-syrian | Rendering_Review_Syr_Batch1_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md | round 1 FAIL P1; round 2 PASS, after re-rendering |
| blc-one-name | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS (all clauses; "lo!" as "see"; longest 25) |
| chronicle-flood-line | Rendering_Review_Syr_Batch1_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| death-knew-his-kingdom-was-to-be-made-void | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS (the poison simile is carried whole; "bringer to nought" is rendered through the simile, then "destroyed"; longest 20) |
| dem6-visit-the-sick | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS (rendering matches the edition; 11) |
| ephrem-keeper-of-strangers | Rendering_Review_Syr_Batch1_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md | round 1 FAIL P1; round 2 PASS, after re-rendering |
| ephrem-only-begotten-dwelling | Rendering_Review_Syr_Batch1_2026-11-03.md | PASS ("[being]" is grammatical, and "left his place with God" holds the sense; all clauses; longest 24) |
| ephrem-resurrection-pledge | Rendering_Review_Syr_Batch2_2026-11-03.md | PASS (all clauses; "would" keeps both clauses inside the pledge; "bring them to" supplies the verb the edition implies; longest 13) |
| nativity-this-is-the-day | Rendering_Review_Syr_Batch2_2026-11-03.md | PASS (all clauses; "fulfilled ... performed" becomes "came true - all of them"; longest 14) |
| nisibene-death-trembled | Rendering_Review_Syr_Batch2_2026-11-03.md | PASS (all clauses; the elliptical "and Satan" kept as "Satan, too"; longest 8) |
| on-a-certain-day-a-pearl | Rendering_Review_Syr_Batch2_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| palladius-hospitaller | Rendering_Review_Syr_Batch2_2026-11-03.md | PASS ("on your behalf I appoint myself" kept; "hospitaller" glossed by its function, which the next sentence of the chapter describes; no office implied; longest 15) |
| pearl-mysteries | Rendering_Review_Syr_Batch2_2026-11-03.md | PASS (all clauses; "semblances and types" as "pictures and signs"; longest 15) |
| permitted-to-erect-churches | Rendering_Review_Syr_Batch2_2026-11-03.md | PASS (all clauses; "decimated" rendered in its exact sense (one in ten put to death); the king's grant kept; longest 23) |
| sozomen-melodies | Rendering_Review_Syr_Batch2_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md, Rendering_Review_Syr_Round3_2026-11-04.md | round 1 FAIL P2; round 2 PASS, after re-rendering; round 3 PASS, after re-rendering to clear the readability floor (FRE 60) |
| symeon-and-usthazanes | Rendering_Review_Syr_Batch2_2026-11-03.md | PASS (all clauses; the Magi relative clause split cleanly; visible organisation stays the provocation; longest 15) |
| tatian-barbaric-writings | Rendering_Review_Syr_Batch2_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md, Rendering_Review_Syr_Round3_2026-11-04.md | round 1 FAIL P2; round 2 PASS, after re-rendering; round 3 PASS, after "centred" became "centered" (American spelling) |
| tatian-born-assyrian | Rendering_Review_Syr_Batch2_2026-11-03.md | PASS (all clauses; "barbarian philosophy" kept as Tatian's own self-description; longest 15) |
| the-blasphemy-of-madmen | Rendering_Review_Syr_Batch2_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| the-scribes-and-the-prefects-over-the-archives | Rendering_Review_Syr_Batch2_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md, Rendering_Review_Syr_Round3_2026-11-04.md | round 1 FAIL P2; round 2 PASS, after re-rendering; round 3 PASS, after re-rendering to clear the readability floor (FRE 60) |
| the-temple-of-the-church-of-the-christians | Rendering_Review_Syr_Batch2_2026-11-03.md, Rendering_Review_Syr_Temple_2026-11-03.md | round 1 PASS (all clauses; "more than two thousand" kept exactly; "lamentation" as "mourning"; longest 17); the independent pull-request review found "temple" kept here but failed in chronicle-flood-line, the same edition sentence; re-rendered as "church building" to match; recheck PASS |
| the-wedding-feast-continues-for-but-seven-days | Rendering_Review_Syr_Batch2_2026-11-03.md | PASS (all clauses; "(virgins)" is a referential supplement that names who "these" are, as the context already shows, so rendering it plainly adds no meaning; each antithesis is one thought; longest 24) |
| theodoret-gnats | Rendering_Review_Syr_Batch2_2026-11-03.md | PASS (all clauses; "on them" only restates the "darts of his curse" at the barbarians in the line before; length 18) |
| warned-before-baptism | Rendering_Review_Syr_Batch2_2026-11-03.md, Rendering_Review_Syr_Round2_2026-11-03.md | round 1 FAIL P1; round 2 PASS, after re-rendering |
