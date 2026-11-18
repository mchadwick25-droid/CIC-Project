# Round 2 changes, era 8 batch 2 (2026-11-16)

`R2_recheck.md` closed 23 of the 25 findings and found new problems in the fixes for two. Both were corrected in
`mkspec2.py` and the batch was vendored again from it. The text files came out byte for byte the same; only shelf
rows changed. The review cycle ends here: one review and one targeted recheck.

| finding | what changed |
|---|---|
| F8 Vieira | "the first Lisbon edition" removed. Each note now says "as printed at Lisbon in" the title page's year. |
| F25 Davies | The Finley row holds the sermon only, dated by its own title page ("May 28, 1761", host line 583), with the title page at host lines 573-600. The appendix memoir has its own row under the anonymous slug `davies-memoirs-anonymous`: the volume says it is "by another hand", "drawn up by a gentleman, who was Mr. Davies's intimate Friend". Bostwick's evidence range is file lines 2752-2759. |

The spec's line-anchor checks, the map check and the registry checks pass after the change.
