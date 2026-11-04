# desert quote renderings: per-rendering review log (61 records)

Date: 2026-11-03. Records: the 61 `desert.quote.*` records, each with a `modern_rendering` and a `text` taken from a vendored source.

What this log is for: it lets the claim "reviewed" be checked, one record at a time. Each row gives the record id (the `desert.quote.` prefix is dropped), the review file or files that read the rendering, and the verdict. All review files are in `Build/worlds/desert/Review-Artifacts/`.

How it was made. Independent Opus 5.5 reviewers read every rendering in 3 batch files (`Rendering_Review_Desert_Batch*_2026-11-03.md`). Each rendering was read against the record's `text` and against the edition text at its locus in `cic/texts/`. The bar: every clause rendered, nothing added, one thought per sentence, no sentence past about 25 words, no word whose modern sense misleads, and the source's own hedges kept. Round 1 failed 15. Each was re-rendered by Opus at the source record and rechecked by a second, independent Opus reader in `Rendering_Review_Desert_Round2_2026-11-03.md`. The independent pull-request review then found the bracket rule (an editor's bracketed supplement must not be voiced as the source's own where it adds meaning) applied unevenly. Six records with bracketed supplements were read against it in `Rendering_Review_Desert_Brackets_2026-11-03.md`. Three failed, were re-rendered by Opus, and passed a third independent Opus reader in `Rendering_Review_Desert_Round3_2026-11-03.md`, within the three-round cap.

| Record | Review file(s) | Verdict on the rendering |
|---|---|---|
| an-old-man-in-the-next-village | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; "give heed to themselves" as "pay attention to their own soul" is a fair sense; longest 18) |
| antony-arians-serpents | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; "saying that" frame kept; 18 words) |
| antony-dying-daily | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses across three segments, elisions kept; "allots it daily" as "one day at a time"; not read as despair; longest 16) |
| antony-nicene-formula | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; indirect-teaching past tense kept; "it was impious to say" frame kept; longest 15) |
| antony-not-worsted | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; "brute beasts" as "wild animals"; elision kept; longest 15) |
| antony-on-living-near-kin | Rendering_Review_Desert_Batch1_2026-11-03.md, Rendering_Review_Desert_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| arch-drawn-from-the-centre | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; "a man" as "a builder" is in the image; "without any error" kept in sense; longest 21) |
| arsenius-flee-tace-quiesce | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; no Latin triad brought in; "fundamental" as "basic"; longest 12) |
| charity-is-the-offspring-of-apatheia | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; "Charity" as "Love" avoids the modern sense; "exists naturally even in those who have not yet believed" kept; longest 19) |
| christ-worketh-them-not-we | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; Christ kept as the agent; longest 14) |
| composed-by-bishop-palladius-for-the-prefect-lausus | Rendering_Review_Desert_Batch1_2026-11-03.md, Rendering_Review_Desert_Brackets_2026-11-03.md | round 1 PASS; the independent pull-request review's sample then found Budge's "[which they gave]" voiced unmarked (P2); re-rendered with the bracket kept; bracket recheck PASS |
| discretion-greatest-prize | Rendering_Review_Desert_Batch1_2026-11-03.md, Rendering_Review_Desert_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| eight-principal-faults | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all eight terms and glosses in order; "faults" kept, not "sins"; longest 8) |
| equal-measure-of-strength | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; purpose clause kept as removing an excuse; longest 20) |
| ethiopic-rule-eat-and-drink | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; work by "measure of their eating" kept, not Palladius's strength wording; longest 23) |
| for-thirty-two-years-i-touched-no-fruit | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; "as he told us himself" frame kept; "timidity" as "fear"; longest 18) |
| god-is-not-a-body | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; Monas and Henas glossed; "so to speak" kept; "greater and a less" as "greater part and lesser part"; longest 17) |
| good-good-i-dont-mind | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; "Providence ... guiding" kept; "take her" as "keep her"; longest 16) |
| grace-and-free-will-in-harmony | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; "seem ... but really" kept; "in harmony" as "work together"; longest 13) |
| he-healed-by-the-name | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses; narrator's "it was clear to all" kept; longest 18) |
| he-longed-to-suffer-martyrdom | Rendering_Review_Desert_Batch1_2026-11-03.md | PASS (all clauses across three segments; "as I said before" kept; "confessors" made plain; longest 26 (about 25)) |
| he-puts-into-us-the-beginnings | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (all three "now" clauses kept; "men" to "people" sound; longest 25) |
| in-real-experience-and-feeling | Rendering_Review_Desert_Batch2_2026-11-03.md, Rendering_Review_Desert_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| ladder-from-compunction | Rendering_Review_Desert_Batch2_2026-11-03.md, Rendering_Review_Desert_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| melania-to-the-governor | Rendering_Review_Desert_Batch2_2026-11-03.md, Rendering_Review_Desert_Round2_2026-11-03.md | round 1 FAIL P1; round 2 PASS, after re-rendering |
| monks-like-hyenas | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS ("in name only" renders "as far as their names are concerned"; all clauses; longest 23) |
| moses-sins-run-out | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (Budge's bracket "[The sands are]" kept; "I, even I" kept; all clauses) |
| never-held-communion-with-the-schismatics | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (the advice exception kept; "intercourse" made "contact"; longest 24) |
| never-kneel-saturday-to-sunday | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (all clauses; "Whitsuntide" made "Pentecost"; Egyptians kept as subject) |
| no-one-seize-the-hand | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (all five prohibitions; stops before "there shall be distance" as the record says) |
| origen-on-the-sinning-brother | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (hedges "would seem" and "I do not think" kept; every listed sin kept) |
| origen-to-gregory-handmaidens | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (handmaid analogy kept whole; all subjects named; longest 21) |
| pachomian-rule-opening-superscription | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS ("ordinance… commanded" made "rule… gave… as a command"; nothing added) |
| pachomius-angel-tablet | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (all three commands kept; elision kept) |
| piamon-judge-of-the-earth | Rendering_Review_Desert_Batch2_2026-11-03.md, Rendering_Review_Desert_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| rule-for-the-weak | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (angel's answer left unquoted as the scan has it; all clauses; longest 20) |
| sarah-man-among-you | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (exact; "brethren" made "brothers") |
| sin-and-grace-in-one-soul | Rendering_Review_Desert_Batch2_2026-11-03.md | PASS (question recast in three short sentences with nothing lost; "hate it, is" spelled out) |
| so-perfectly-silent | Rendering_Review_Desert_Batch2_2026-11-03.md, Rendering_Review_Desert_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| talida-key-never-taken | Rendering_Review_Desert_Batch2_2026-11-03.md, Rendering_Review_Desert_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| taor-not-compelled-to-market | Rendering_Review_Desert_Batch2_2026-11-03.md, Rendering_Review_Desert_Brackets_2026-11-03.md | round 1 PASS; bracket recheck PASS |
| the-coming-of-christ-made-thee-weak | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (all clauses; "at length" as "at last"; final clause split in two; longest 21) |
| the-deeds-of-christ-prove-him | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (both segments; list of signs kept whole across two questions; "which shew" carried; longest 21) |
| the-eight-generic-thoughts | Rendering_Review_Desert_Batch3_2026-11-03.md, Rendering_Review_Desert_Brackets_2026-11-03.md, Rendering_Review_Desert_Round3_2026-11-03.md | round 1 PASS; bracket recheck FAIL P2; round 3 PASS, after re-rendering |
| the-heart-is-a-deep-gulf | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (every clause; "only, I say" kept; implied "perfection" supplied without new sense; longest 19) |
| the-kingdom-is-apatheia | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (both definitions kept separate; "according to the capacity of the nous" and "bestowing incorruptibility" carried; longest 19) |
| the-ladder-from-faith-to-love | Rendering_Review_Desert_Batch3_2026-11-03.md, Rendering_Review_Desert_Brackets_2026-11-03.md, Rendering_Review_Desert_Round3_2026-11-03.md | round 1 PASS; bracket recheck FAIL P2; round 3 PASS, after re-rendering |
| the-main-share-is-not-our-works | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (fragment rendered whole; "merit of our own works" kept; 20 words) |
| the-noonday-demon | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (all six numbered stages and close; "as they say" and "the demon adds" kept; translator's clock glosses kept; longest 24) |
| the-nous-beholds-its-own-radiance | Rendering_Review_Desert_Batch3_2026-11-03.md, Rendering_Review_Desert_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| the-soul-becomes-all-eye | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (communion, irradiation, seat and dwelling, all light/face/eye, eyes of light all kept; longest 15) |
| the-word-took-a-human-body | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS ("not changed", "being the same", purpose and partaking clauses kept; longest 22) |
| they-have-taken-away-my-god | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (every clause; "worship and address" both kept; longest 10) |
| three-hundred-acres-to-the-villagers | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS ("as though" hedge kept; acreage and qualities kept; purpose clause with sister kept; longest 21) |
| three-kinds-of-monks | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (all three orders and their descriptions; "we too hope" kept; longest 17) |
| three-renunciations-solomon | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (three books mapped in order with each reason; edition's lower-case "word of God" given as "Word", within the sense; longest 13) |
| three-years-a-servant | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (three-year term, servant-only status, entry after term all kept; longest 18) |
| twelve-psalms-by-an-angel | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (long period broken into single thoughts; every clause carried, incl. weak brethren, 50/60/beyond, Egyptian sitting custom, Alleluia, disappearance; chanter not named as angel; longest 24) |
| when-the-cross-of-christ-arose | Rendering_Review_Desert_Batch3_2026-11-03.md | PASS (both segments; three rhetorical questions kept; longest 17) |
| whence-canst-thou-prove-to-us | Rendering_Review_Desert_Batch3_2026-11-03.md, Rendering_Review_Desert_Brackets_2026-11-03.md | round 1 PASS; bracket recheck PASS |
| womens-house-across-the-river | Rendering_Review_Desert_Batch3_2026-11-03.md, Rendering_Review_Desert_Brackets_2026-11-03.md, Rendering_Review_Desert_Round3_2026-11-03.md | round 1 PASS; bracket recheck FAIL P2; round 3 PASS, after re-rendering |
