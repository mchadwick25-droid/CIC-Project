# rzg quote renderings: per-rendering review log (6 records)

Date: 2026-11-03. Records: the 6 `rzg.quote.*` records, each with a `modern_rendering` and a `text` taken from a vendored source.

What this log is for: it lets the claim "reviewed" be checked, one record at a time. Each row gives the record id (the `rzg.quote.` prefix is dropped), the review file or files that read the rendering, and the verdict. All review files are in `Build/worlds/rzg/Review-Artifacts/`.

How it was made. Independent Opus 5.5 reviewers read every rendering in 1 batch file (`Rendering_Review_Rzg_Batch*_2026-11-03.md`). Each rendering was read against the record's `text` and against the edition text at its locus in `cic/texts/`. The bar: every clause rendered, nothing added, one thought per sentence, no sentence past about 25 words, no word whose modern sense misleads, and the source's own hedges kept. Round 1 failed none.

| Record | Review file(s) | Verdict on the rendering |
|---|---|---|
| christ-the-mirror-of-election | Rendering_Review_Rzg_Batch1_2026-11-03.md | PASS ("out of Christ" as "apart from Christ" is accurate; both elisions kept; longest 15) |
| mass-not-a-sacrifice | Rendering_Review_Rzg_Batch1_2026-11-03.md | PASS (all clauses: once, forever, sure and valid, all the faithful, not a sacrifice, remembrance and assurance; longest 18) |
| seniors-selected-from-the-people | Rendering_Review_Rzg_Batch1_2026-11-03.md | PASS ("seniors" as "elders" and "bishops" as "pastors" avoid misleading modern senses; Calvin uses the titles interchangeably (line 2810); longest 13) |
| signs-and-things-signified | Rendering_Review_Rzg_Batch1_2026-11-03.md | PASS (distinguish / "as we ought" / do not separate the reality from the signs, all kept; trailing elision kept; longest 22) |
| taught-better-from-scripture | Rendering_Review_Rzg_Batch1_2026-11-03.md | PASS (all clauses incl. "called inspired by God", "not now correctly understood", "only from said Scriptures"; longest 19) |
| zwinglis-last-words | Rendering_Review_Rzg_Batch1_2026-11-03.md | PASS (both sentences rendered; "it is true" kept; the "It was reported" frame (line 1584) sits outside the quote and is carried by `speaker_or_author`; longest 12) |
