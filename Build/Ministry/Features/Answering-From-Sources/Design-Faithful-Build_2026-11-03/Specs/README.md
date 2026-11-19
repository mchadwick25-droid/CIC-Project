# Specs for the remaining engine parts (2026-11-03)

One page each: purpose, inputs and outputs, files it may and must not touch, the test written first, done-when, cost. Part 1 of the engine work, steps 3 and 4, is `../Step3_4_Search_Bench.md` and pull request #1465.

| Spec | Model | Needs | Can run |
|---|---|---|---|
| 1 Revert Decision-Log 63 and 64, and the shared voice change | Opus | nothing | first, alone |
| 5 Held-out set | Sonnet drafts; code freezes and hashes | nothing from the engine (needs the questions kept blind) | first, in parallel with 1 |
| 2 Offer assembler | Opus | the search package (#1465 merged) | after #1465 |
| 4 Diversity rule | Opus | 2 (the ranked candidate list it reorders) | after 2 |
| 3 Before-drafting test (A seam) | Opus | 2 for the searched passages; 5 for its measure | build after 2; measure after 5 |

Measures in specs 3 and 4 use the held-out set (5). Code-only counts are free. Counts that need a drafted answer run with in-plan helpers, free, and are labelled helper-written. A live test is proposed to Mark only afterwards, with a name and a cap.

## Chunks on the plan page

| Chunk | Spec |
|---|---|
| D2 revert and voice rules | 1 |
| D3 held-out set | 5 |
| D4 offer assembler and diversity rule, one pull request | 2 and 4 |
| D5 before-drafting test, design A | 3 |
| D6 conformance removals | 6 |
| D7 lens share for all twelve worlds | 7 |
| D9 to D13 held-out measurement | 8 |

## Open item for Mark, raised when a live switch-on is proposed
Where the built index and vectors live in a deployment. Each world's index and vectors come to about 100 MB, are built offline and are not in the repository. The assembler takes their paths as parameters, so the specs do not decide this. Nothing in the engine reads the index at question time today.
