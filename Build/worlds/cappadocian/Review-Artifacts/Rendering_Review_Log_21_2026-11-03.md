# cappadocian quote renderings: per-rendering review log (21 records)

Date: 2026-11-03. Records: the 21 `cappadocian.quote.*` records, each with a `modern_rendering` and a `text` taken from a vendored source.

What this log is for: it lets the claim "reviewed" be checked, one record at a time. Each row gives the record id (the `cappadocian.quote.` prefix is dropped), the review file or files that read the rendering, and the verdict. All review files are in `Build/worlds/cappadocian/Review-Artifacts/`.

How it was made. Independent Opus 5.5 reviewers read every rendering in 1 batch file (`Rendering_Review_Cappadocian_Batch*_2026-11-03.md`). Each rendering was read against the record's `text` and against the edition text at its locus in `cic/texts/`. The bar: every clause rendered, nothing added, one thought per sentence, no sentence past about 25 words, no word whose modern sense misleads, and the source's own hedges kept. Round 1 failed 12. Each was re-rendered by Opus at the source record and rechecked by a second, independent Opus reader in `Rendering_Review_Cappadocian_Round2_2026-11-03.md`. A later check found that the round-2 rendering of `gregory-nyssa-on-becoming-god` had dropped the edition's "reasonably". It was restored, and a third reader (`Rendering_Review_Cappadocian_Round3_2026-11-04.md`) found two grounding "For"s dropped as well. Under the project lead's cap ruling, a fresh fourth reader (`Rendering_Review_Cappadocian_Round4_2026-11-04.md`) passed the first restored "For" and failed the second sentence, which had dropped "although". Under a second ruling, a fresh fifth reader (`Rendering_Review_Cappadocian_Round5_2026-11-04.md`) passed the fourth reader's wording: "For although this last form of God's presence among us differs from that former one, his existence among us is still shown equally, then and now."

| Record | Review file(s) | Verdict on the rendering |
|---|---|---|
| baptize-believe-glorify-in-sequence | Rendering_Review_Cappadocian_Batch1_2026-11-03.md | PASS (all three limbs of the dilemma kept; "as we have received" read as baptism handed down; longest 13) |
| basil-against-delaying-baptism | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| basil-against-eunomius-ant | Rendering_Review_Cappadocian_Batch1_2026-11-03.md | PASS (all clauses both sides of the elision; "physiological" as "account of nature"; longest 21) |
| basil-canon-on-digamy | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| basil-canon-to-amphilochius | Rendering_Review_Cappadocian_Batch1_2026-11-03.md | PASS (all four stages and the final admission kept; longest 20) |
| basil-on-antiphonal-psalmody | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| basil-on-common-life | Rendering_Review_Cappadocian_Batch1_2026-11-03.md | PASS (all clauses; "as it is written" kept; foot analogy whole; longest 24) |
| basil-on-eustathius-rupture | Rendering_Review_Cappadocian_Batch1_2026-11-03.md | PASS (all clauses; "they falsely accuse" frame kept; longest 24) |
| basil-on-his-retreat | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P1; round 2 PASS, after re-rendering |
| basil-on-the-doxology-challenge | Rendering_Review_Cappadocian_Batch1_2026-11-03.md | PASS (both doxology forms; objectors' charge kept inside "They said"; both purposes of the request; longest 23) |
| basil-on-work-and-prayer | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| basil-to-the-chorepiscopi | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| gregory-nyssa-on-becoming-god | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md, Rendering_Review_Cappadocian_Round3_2026-11-04.md, Rendering_Review_Cappadocian_Round4_2026-11-04.md, Rendering_Review_Cappadocian_Round5_2026-11-04.md | round 1 FAIL P2; round 2 PASS, after re-rendering; round 3 FAIL (minor): two grounding "For"s dropped, after "reasonably" was restored; targeted fourth read under the cap ruling FAIL on one sentence ("although" dropped); targeted fifth read under the second ruling PASS, after re-rendering that sentence |
| julian-galilaeans | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| macrina-refuses-remarriage | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P1; round 2 PASS, after re-rendering |
| macrina-the-elder-taught-me | Rendering_Review_Cappadocian_Batch1_2026-11-03.md | PASS (all clauses of `text`; "delivered" as "handed down"; longest 21) |
| ousia-and-hypostasis | Rendering_Review_Cappadocian_Batch1_2026-11-03.md | PASS (all clauses; "a man"/"Paul" contrast kept; longest 22) |
| reading-scripture-hexaemeron | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| spirit-numbered-with-father-and-son | Rendering_Review_Cappadocian_Batch1_2026-11-03.md | PASS (all clauses; "ranked with the Father" kept, not raised to "is God"; longest 23) |
| we-look-to-the-east | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
| what-is-the-written-source | Rendering_Review_Cappadocian_Batch1_2026-11-03.md, Rendering_Review_Cappadocian_Round2_2026-11-03.md | round 1 FAIL P2; round 2 PASS, after re-rendering |
