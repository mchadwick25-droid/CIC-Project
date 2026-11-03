# Steps 3 and 4: search build, retrieval bench, known misses (2026-11-03)

No model call and no spend. The embedder is BAAI/bge-small-en-v1.5 (MIT licence) and the reranker is cross-encoder/ms-marco-MiniLM-L-6-v2 (Apache-2.0 licence), both run locally on onnxruntime. The code is in `Sandbox/answering-library/search/`, outside the hashed `index/` set; no index stamp changed. Indexes were rebuilt from `cic/texts` with no context lines (none exist without a model run), so every keyword figure is the plain-text baseline.

## Lens basis
The bench used the division test, read from the world's corpus-map rows (not the index's row tie). One row of the world in a file: every passage binds to it. Several rows: a passage binds to the one row whose `locus_ids` hold its division locus (or `whole-file`); none or several claiming rows leaves it outside. English, not apparatus. The window is not applied: neither the index nor the rows give a dated window.

| | lpc | rzg |
|---|---|---|
| passages in the lens | 17,092 | 22,004 |
| English, not apparatus (whole shelf) | 20,149 | 22,004 |

lpc matches Library's 17,092 (84.8%); rzg is 100%. The index builder needed no change.

## Step 3: reach of the cited passage, visitor wording
Cases are (sub-question, wording, cited record) with the record's cited passages found by line or quote. Hit means a cited passage is in the top k.

| | lpc, 625 cases | | | rzg, 50 cases | | |
|---|---|---|---|---|---|---|
| method | top 5 | top 10 | top 20 | top 5 | top 10 | top 20 |
| keyword, old file-level shelf (reference) | 5 | 7 | 11 | 0 | 0 | 0 |
| keyword | 7 | 8 | 13 | 0 | 0 | 0 |
| meaning | 13 | 19 | 28 | 0 | 1 | 1 |
| fused (keyword + meaning, reranked) | 10 | 17 | 24 | 0 | 1 | 1 |
| fused with seeds | 10 | 17 | 27 | 0 | 1 | 2 |

rzg has 27 of its 50 cases with a cited passage inside the lens. The count of lpc cases (625) is the wording condition only and differs from the 535 in the brief; the cause is not established.

Paired cases, wins and losses of the first method, exact two-sided sign test, 99% line (p < 0.01). Only pairs that pass the line are better:

| lpc pair | top 5 | top 10 | top 20 |
|---|---|---|---|
| meaning vs keyword | 11–5, p 0.21 | 16–5, p 0.027 | 21–6, p 0.0059, better |
| fused vs keyword | 6–3, p 0.51 | 10–1, p 0.012 | 12–1, p 0.0034, better |
| fused vs meaning | 4–7, p 0.55 | 5–7, p 0.77 | 6–10, p 0.45 |
| fused with seeds vs fused | 0–0 | 0–0 | 4–1, p 0.375 |

rzg: every pair has at most 1 win and 0 losses; none can reach the line with 50 cases.

Reading: meaning search lifts reach past the 99% line at top 20 on lpc, and not at top 5 or 10. Fusing with reranking does not beat meaning alone on lpc. Seeds change 4 cases at top 20 on lpc and do not reach the line. The seeds come from the same coverage maps as the cited passages, so the seeds column is not independent.

## Step 4: known misses, lpc, from the visitor's words (existence checks)
| check | question | gold passages (in lens) | keyword | meaning | fused | fused with seeds |
|---|---|---|---|---|---|---|
| Letter 47.5 | q102 | 1 (1) | not found | 13 | 23 | 32 |
| City of God XXII.8 | q099 | 23 (23) | 38 | 2 | 1 | 1 |
| City of God XXII.8 | q100 | 23 (23) | 12 | 4 | 4 | 5 |
| City of God XXI.17 | q029 | 2 (2) | 21 | 16 | 2 | 2 |
| q101 quote (love and do what thou wilt) | q101 | 4 (1) | not found | 83 | 164 | 164 |

Cells show the best rank of a gold passage. In the top 10: XXII.8 for q099 and q100 (meaning, fused, fused with seeds, not keyword); XXI.17 for q029 (fused, fused with seeds). Not in the top 10 by any method: Letter 47.5 and the q101 quote. Only 1 of the q101 quote's 4 gold passages is inside the lens.

## Checks
`search/tests`: 6 pass, including the two-world test (a query matching only world B's passage returns nothing for world A by keyword, meaning, fused and fused with seeds). `engine/m4/tests/test_passage_offer.py`: 16 pass with the new offer seam. Four `index/tests` fail with and without these changes because `boto3` and `anthropic` are not installed here.
