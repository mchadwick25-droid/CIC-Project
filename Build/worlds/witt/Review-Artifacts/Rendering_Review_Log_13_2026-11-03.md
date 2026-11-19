# witt quote renderings: per-rendering review log (13 records)

Date: 2026-11-03. Records: the 13 `witt.quote.*` records, each with a `modern_rendering` and a `text` taken from a vendored source.

What this log is for: it lets the claim "reviewed" be checked, one record at a time. Each row gives the record id (the `witt.quote.` prefix is dropped), the review file or files that read the rendering, and the verdict. All review files are in `Build/worlds/witt/Review-Artifacts/`.

How it was made. Independent Opus 5.5 reviewers read every rendering in 1 batch file (`Rendering_Review_Witt_Batch*_2026-11-03.md`). Each rendering was read against the record's `text` and against the edition text at its locus in `cic/texts/`. The bar: every clause rendered, nothing added, one thought per sentence, no sentence past about 25 words, no word whose modern sense misleads, and the source's own hedges kept. Round 1 failed 1. Each was re-rendered by Opus at the source record and rechecked by a second, independent Opus reader in `Rendering_Review_Witt_Round2_2026-11-03.md`. For `you-too-must-have-a-care` the independent pull-request review then disputed the round 1 finding; the original rendering was restored and a third independent Opus reader (`Rendering_Review_Witt_Round3_2026-11-03.md`) confirmed it, within the three-round cap.

| Record | Review file(s) | Verdict on the rendering |
|---|---|---|
| article-ii-of-original-sin | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses; "concupiscence" as "evil desire", "vice of origin" as "inborn fault"; longest 26 (about 25, acceptable)) |
| article-ix-of-baptism | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses; offered-and-received clause kept as its own sentence; longest 18) |
| as-when-one-must-kill-a-mad-dog | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses, nothing softened; "smite, slay, and stab" as "strike, kill and stab"; longest 20) |
| christs-return-to-judgment | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses; both condemnations kept, "Jewish opinions" kept as the source's; longest 25) |
| congregation-of-saints | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses; "congregation" as "community", "administered" as "given"; "etc." as "and so on"; longest 23) |
| neither-court-nor-mercy | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses; "court" as "a trial"; mercy-for-captives claim kept as Luther's own; longest 24) |
| nothing-that-varies | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses; "Church Catholic" as "universal Church" (not Rome, per not_for); longest 23) |
| second-article-of-the-creed | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses of creed and explanation; adverbs as "in righteousness, innocence and blessedness"; longest 23) |
| the-poor-man-who-comes-to-you | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (conditional kept ("may ... Then"); "(I say again)" kept; longest 19) |
| the-sword-is-at-your-throats | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses; Latin tag left out, its English kept; "Psalm cvi" (Vulgate) given as "Psalm 107", the same psalm in modern numbering; longest 24) |
| the-time-of-the-sword | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses; "lay about them" as "strike out all around them"; souls claim kept as the tract's; longest 24) |
| you-too-must-have-a-care | Rendering_Review_Witt_Batch1_2026-11-03.md, Rendering_Review_Witt_Round2_2026-11-03.md, Rendering_Review_Witt_Round3_2026-11-03.md | round 1 FAIL P1 (concession said to be limited to some lords); round 2 PASS on a restrictive re-rendering; the independent pull-request review found the edition's clause non-restrictive (commas) and the re-rendering a narrowing; the original rendering was restored; round 3 PASS (round 1 finding a misreading; original rendering meets the bar) |
| your-own-judges | Rendering_Review_Witt_Batch1_2026-11-03.md | PASS (all clauses; "equity" as "fairness", "ordinance" as "order"; longest 20) |
