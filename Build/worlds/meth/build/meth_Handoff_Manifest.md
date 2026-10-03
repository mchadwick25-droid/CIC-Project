# Handoff manifest: world `meth`

| Field | Entry |
|---|---|
| World code | meth |
| World id | the-methodist-revival |
| `safety_adjacent` (`true` or `false`, set by Mark at handoff) | not yet set; the project lead sets it |
| Slug | the-methodist-revival |
| Handoff date | 2026-10-02 |
| Prepared by | Library thread |
| Signed off by Mark on | not yet |

## Paths

| Item | Path |
|---|---|
| Registry entry | `records/worlds/meth.yaml` |
| Step 0 Movement-Scope Confirmation | `Build/worlds/meth/Step0_Movement_Scope_Confirmation.md` |
| Step 1 World Identification | `Build/worlds/meth/Doc_01_World_Identification_Boundaries_Orientation.md` |
| Step 2 Source Ecology | `Build/worlds/meth/Doc_02_Source_Ecology.md` |
| Source Registry | `Build/worlds/meth/Source_Registry.md` |
| Source Acquisition Manifest | `Build/worlds/meth/Source_Acquisition_Manifest.md` |
| Source Readiness Dossier | `Build/worlds/_cross-world/dossiers/the-methodist-revival_Source_Readiness_Dossier.md` |
| Corpus-map assignments | `cic/corpus-map/the-methodist-revival.yaml` |
| Vendored texts (registry entries) | `cic/texts/REGISTRY.yaml` |
| Open gaps | `Build/worlds/meth/Open_Gaps_Tracking.md` |
| Cross-world questions | `Build/worlds/_cross-world/NEEDS-RULING.md` |
| Build log | `Build/worlds/meth/build/meth_Build_State.yaml` |

## Review round per step

None of the three steps is cleared by an independent review. Three review files are on record for each step, and three is the cap. Round 1 was a same-thread pass by the drafting thread. Rounds 2 and 3 describe themselves as independent cross-model reviews, but no reviewer record accompanies them and the pull request records every round as same-thread. Round 3 finds Step 0 cleared on substance and finds Step 1 and Step 2 still substantial. A later recheck that the branch's commit message describes has no review file. The project lead rules on review clearance, and on the Whitefield allocation escalation in Step 1 section 9.

| Step | Review round it cleared in | Review file | Date |
|---|---|---|---|
| Step 0 | not cleared; 3 rounds used, cap reached | Step0_Review_Round3.md | 2026-09-25 |
| Step 1 | not cleared; 3 rounds used, cap reached | Review-Artifacts/Doc01_Round3_Review.md | 2026-09-25 |
| Step 2 | not cleared; 3 rounds used, cap reached | Review-Artifacts/Doc02_Round3_Review.md | 2026-09-25 |

## The 12 handoff checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | The world's identity is fixed. Its registry entry at `records/worlds/meth.yaml` exists, with one `world_id`, before any of the world's records reach `main`. Every later file uses that same `world_id`. The entry carries `safety_adjacent: true` or `false`, set by Mark. A new world fails this check until it is set. | Open | `safety_adjacent` is unset; the project lead sets it |
| 2 | Step 0, Movement-Scope Confirmation, is approved to proceed. It cleared independent Opus review within the round cap, and the movement's own status in `cic-website/data/world-census.json` was checked. | Fail | `Step0_Review_Round3.md` does not say Approved to proceed; the census check passes |
| 3 | Step 1, World Identification, is approved to proceed, under the same review rule. | Fail | `Review-Artifacts/Doc01_Round3_Review.md` does not say Approved to proceed |
| 4 | Step 2, Source Ecology, is approved to proceed. Its Source Registry gives every item in the library package a line, and no dossier item, corpus-map entry or holdings-report file is missing one. | Fail | `Review-Artifacts/Doc02_Round3_Review.md` does not say Approved to proceed; every package item has a Registry line |
| 5 | The Source Readiness Dossier is at `Build/worlds/_cross-world/dossiers/the-methodist-revival_Source_Readiness_Dossier.md`. | Pass | dossier present, five sections, no ISO dates in header |
| 6 | The corpus-map assignments are at `cic/corpus-map/the-methodist-revival.yaml`, and `python cic/engine/corpus_map_merge.py --check` passes. | Pass | `corpus_map_merge.py --check` valid; every row has a `row_id` |
| 7 | The vendored texts are in `cic/texts/`, each with a `cic/texts/REGISTRY.yaml` entry and verified rights. Every assigned work opens, and `python cic/engine/corpus_index.py --build` is clean. | Pass | `handoff` check 7 passes; `texts_registry.py` reports OK |
| 8 | Every quotation in Steps 0-2 is re-verified word for word against the vendored file, speaker included. An opponent's paraphrase is never quoted as the subject's own words. | Pass | 43 quotations checked, 19 from project documents, 17 inside a cited `cic:` division |
| 9 | Open questions are carried forward, not decided. Every cross-world question in the dossier sits in `Build/worlds/_cross-world/NEEDS-RULING.md` or the world's `Open_Gaps_Tracking.md`. | Pass | the dossier's section 5 question (the Moravian Church at Herrnhut) is `Open_Gaps_Tracking.md` item 2 and stays open; the Whitefield allocation question is escalated in Step 1 section 9 |
| 10 | The world's `Open_Gaps_Tracking.md` exists, with the library stage's own gaps already listed. | Pass | `Open_Gaps_Tracking.md` entries 1 to 34 |
| 11 | No process narration is in anything that will become canonical. History goes to the build log. | Pass | `check_live_commentary.py --base origin/main --enforce` exits 0 |
| 12 | A one-page handoff manifest lists the paths above, the review round each step cleared in, and the date. The build thread reads it first. | Pass | this file |

## Outcome

| Field | Entry |
|---|---|
| Checks passed | 8 / 12 |
| Handoff gate run (`python -m engine.m10.cli handoff meth`) | 2026-10-02: check 1 fails on the unset `safety_adjacent`; checks 2, 3 and 4 fail because no review round says Approved to proceed; checks 5 to 12 pass |
| Failed checks sent back to the source-research thread | none; checks 2 to 4 wait on the project lead's ruling on review clearance, and check 1 waits on the project lead |
