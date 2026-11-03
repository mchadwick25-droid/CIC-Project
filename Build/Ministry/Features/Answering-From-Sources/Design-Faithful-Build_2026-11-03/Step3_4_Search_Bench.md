# Steps 3 and 4: search build, retrieval bench, known misses (2026-11-03)

## Result in brief
- On lpc, meaning search finds the cited passage more often than keyword search at every depth. It does not pass the 99% line at any depth: top 20 is 18 wins, 6 losses, p 0.023. The stop rule in the build plan applies. The search merges as built code with this result reported. It is still the design's search.
- Fusing keyword and meaning, then reranking, does not beat meaning alone on lpc at any depth. Its counts are below meaning's.
- Seeds change nothing on lpc at top 5 or 10, and trade one query for another at top 20.
- rzg is too thin to test: no method finds more than 2 of 50 queries in the top 20.
- Known misses: City of God XXII.8 (q099, q100) and XXI.17 (q029) are found in the top 10. Letter 47.5 and the q101 quote are not.

## How the run was made
The run used the code after the five review fixes:
- token-sized windows, with the reranker scoring a passage's best window;
- vectors keyed by a hash of the lens;
- reviewed seeds winning ties in fusion and reranking;
- the sign test paired by query;
- strengthened tests.

The index was rebuilt from `cic/texts` and every vector was rebuilt from nothing. The longest lpc window is 499 tokens; none passes the model's 512-token limit. lpc has 30,787 windows and rzg has 34,506.

No model call and no spend. The embedder is BAAI/bge-small-en-v1.5 (MIT licence). The reranker is cross-encoder/ms-marco-MiniLM-L-6-v2 (Apache-2.0 licence). Both run locally on onnxruntime. The code is in `Sandbox/answering-library/search/`, outside the hashed `index/` set, so no index stamp changed. The index has no context lines (none exist without a model run), so every keyword figure is the plain-text baseline.

Raw outputs are in `Bench_Results/`: `bench_lpc.json`, `bench_rzg.json` and `known_misses.json`.

## Lens basis
The lens uses the division test, read from the world's corpus-map rows (not the index's row tie):
- If a file holds one row of the world, every passage binds to it.
- If a file holds several rows, a passage binds to the one row whose `locus_ids` hold its division locus (or `whole-file`). A passage that no row claims, or that several rows claim, stays outside.

Only English passages count, and apparatus is left out. The date window is not applied, because neither the index nor the rows give a dated window.

| | lpc | rzg |
|---|---|---|
| shelf files | 112 | 42 |
| passages in the lens | 17,092 | 22,004 |
| English, not apparatus (whole shelf) | 20,149 | 22,004 |

The lpc lens holds 84.8% of the English shelf; the rzg lens holds all of it.

## Step 3: reach of the cited passage, visitor wording
A case is one sub-question, one visitor wording and one record. The record's cited passages are found by line or quote. A query is one sub-question with one wording. Every record cited for that sub-question shares the query's one ranking.

A query is a hit at depth k when any of its cited passages is in the top k. The paired tests count each query once.

lpc: 625 cases in 256 queries, every case with a cited passage inside the lens. rzg: 50 cases in 50 queries, 27 of them with a cited passage inside the lens. The 625 lpc cases differ from the 535 in the brief; the cause is not established.

### Hits, queries (cases in brackets)
| | lpc, 256 queries | | | rzg, 50 queries | | |
|---|---|---|---|---|---|---|
| method | top 5 | top 10 | top 20 | top 5 | top 10 | top 20 |
| keyword, old file-level shelf (reference only) | 5 (5) | 7 (7) | 11 (11) | 0 (0) | 0 (0) | 0 (0) |
| keyword | 7 (7) | 8 (8) | 13 (13) | 0 (0) | 0 (0) | 0 (0) |
| meaning | 11 (13) | 17 (19) | 25 (28) | 0 (0) | 1 (1) | 1 (1) |
| fused (keyword + meaning, reranked) | 8 (8) | 16 (17) | 22 (24) | 1 (1) | 1 (1) | 1 (1) |
| fused with seeds | 8 (8) | 16 (17) | 22 (24) | 1 (1) | 1 (1) | 2 (2) |

### Paired comparison, lpc, one count per query
Each cell shows the first method's wins and losses and the exact two-sided sign-test p. Ties are left out. A method is better only when it wins more than it loses and p < 0.01.

| pair | top 5 | top 10 | top 20 |
|---|---|---|---|
| meaning vs keyword | 9–5, p 0.42 | 14–5, p 0.064 | 18–6, p 0.023 |
| fused vs keyword | 3–2, p 1.0 | 10–2, p 0.039 | 11–2, p 0.022 |
| fused vs meaning | 3–6, p 0.51 | 4–5, p 1.0 | 5–8, p 0.58 |
| fused with seeds vs fused | 0–0 | 0–0 | 1–1, p 1.0 |

No pair passes the 99% line at any depth.

rzg: no pair has more than 1 win, and every pair has 0 losses. With these counts no pair can reach the line.

### What is better and what is not
- Meaning search reaches more cited passages than keyword search on lpc: 25 queries against 13 at top 20. This is not shown past the 99% line at any depth. Meaning beating keyword at the 99% line was the condition to go on; it is not met.
- Fusion with reranking is not better than meaning alone on lpc. It wins fewer queries than it loses at every depth, though not significantly.
- Seeds do not help on lpc: no change at top 5 or 10, and one query gained and one lost at top 20. The seeds come from the same coverage maps as the cited passages, so this column is not independent evidence.
- On rzg, no method reaches more than 2 of 50 queries. The bench cannot separate the methods there.

## Step 4: known misses, lpc, from the visitor's words (existence checks)
| check | question | gold passages (in lens) | keyword | meaning | fused | fused with seeds |
|---|---|---|---|---|---|---|
| Letter 47.5 | q102 | 1 (1) | not found | 13 | 14 | 32 |
| City of God XXII.8 | q099 | 23 (23) | 38 | 2 | 1 | 1 |
| City of God XXII.8 | q100 | 23 (23) | 12 | 4 | 4 | 5 |
| City of God XXI.17 | q029 | 2 (2) | 21 | 16 | 2 | 2 |
| q101 quote (love and do what thou wilt) | q101 | 4 (1) | not found | 83 | 164 | 164 |

Each cell shows the best rank of a gold passage. "Not found" means no gold passage is in the method's ranking.

| check | found in the top 10 |
|---|---|
| Letter 47.5 | no, by any method |
| City of God XXII.8, q099 | yes: meaning, fused, fused with seeds; keyword no |
| City of God XXII.8, q100 | yes: meaning, fused, fused with seeds; keyword no |
| City of God XXI.17, q029 | yes: fused, fused with seeds; keyword and meaning no |
| q101 quote | no, by any method |

Only 1 of the q101 quote's 4 gold passages is inside the lens.

## Checks
- `Sandbox/answering-library/search/tests` and `engine/m4/tests/test_passage_offer.py`: 26 pass. These include the two-world test: a query matching only world B's passage returns nothing for world A by keyword, meaning, fused or fused with seeds.
