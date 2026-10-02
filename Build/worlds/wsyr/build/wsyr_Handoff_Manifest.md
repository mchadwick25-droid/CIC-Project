# Handoff manifest: world `wsyr`

| Field | Entry |
|---|---|
| World code | wsyr |
| World id | syriac-orthodox-west-syriac-christianity |
| `safety_adjacent` (`true` or `false`, set by Mark at handoff) | not yet set; the project lead sets it |
| Slug | syriac-orthodox-west-syriac-christianity |
| Handoff date | 2026-10-02 |
| Prepared by | Library thread |
| Signed off by Mark on | not yet |

## Paths

| Item | Path |
|---|---|
| Registry entry | `records/worlds/wsyr.yaml` |
| Step 0 Movement-Scope Confirmation | `Build/worlds/wsyr/Step0_Movement_Scope_Confirmation.md` |
| Step 1 World Identification | `Build/worlds/wsyr/Doc_01_World_Identification_Boundaries_Orientation.md` |
| Step 2 Source Ecology | `Build/worlds/wsyr/Doc_02_Source_Ecology.md` |
| Source Readiness Dossier | `Build/worlds/_cross-world/dossiers/syriac-orthodox-west-syriac-christianity_Source_Readiness_Dossier.md` |
| Corpus-map assignments | `cic/corpus-map/syriac-orthodox-west-syriac-christianity.yaml` |
| Vendored texts (registry entries) | `cic/texts/REGISTRY.yaml` |
| Open gaps | `Build/worlds/wsyr/Open_Gaps_Tracking.md` |
| Cross-world questions | `Build/worlds/_cross-world/NEEDS-RULING.md` |
| Build log | `Build/worlds/wsyr/build/wsyr_Build_State.yaml` |

## Review round per step

| Step | Review round it cleared in | Review file | Date |
|---|---|---|---|
| Step 0 | 3 | Step0_Review_Round3.md | 2026-09-25 |
| Step 1 | 3 | Review-Artifacts/Doc01_Round3_Review.md | 2026-09-25 |
| Step 2 | 3 | Review-Artifacts/Doc02_Round3_Review.md | 2026-09-25 |

## The 12 handoff checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | The world's identity is fixed. Its registry entry at `records/worlds/wsyr.yaml` exists, with one `world_id`, before any of the world's records reach `main`. Every later file uses that same `world_id`. The entry carries `safety_adjacent: true` or `false`, set by Mark. A new world fails this check until it is set. | Open | `safety_adjacent` is unset; the project lead sets it |
| 2 | Step 0, Movement-Scope Confirmation, is approved to proceed. It cleared independent Opus review within the round cap, and the movement's own status in `cic-website/data/world-census.json` was checked. | Pass | `Step0_Review_Round3.md` carries the disposition line |
| 3 | Step 1, World Identification, is approved to proceed, under the same review rule. | Pass | `Review-Artifacts/Doc01_Round3_Review.md` |
| 4 | Step 2, Source Ecology, is approved to proceed. Its Source Registry gives every item in the library package a line, and no dossier item, corpus-map entry or holdings-report file is missing one. | Pass | Source Registry is Doc_02 section 2, Tables A to D |
| 5 | The Source Readiness Dossier is at `Build/worlds/_cross-world/dossiers/syriac-orthodox-west-syriac-christianity_Source_Readiness_Dossier.md`. | Pass | dossier present, five sections, no ISO dates in header |
| 6 | The corpus-map assignments are at `cic/corpus-map/syriac-orthodox-west-syriac-christianity.yaml`, and `python cic/engine/corpus_map_merge.py --check` passes. | Pass | `corpus_map_merge.py --check` valid; every row has a `row_id` |
| 7 | The vendored texts are in `cic/texts/`, each with a `cic/texts/REGISTRY.yaml` entry and verified rights. Every assigned work opens, and `python cic/engine/corpus_index.py --build` is clean. | Pass | `texts_registry.py` OK; `corpus_index.py --build` clean |
| 8 | Every quotation in Steps 0-2 is re-verified word for word against the vendored file, speaker included. An opponent's paraphrase is never quoted as the subject's own words. | Pass | 32 quotations checked, 2 from project documents |
| 9 | Open questions are carried forward, not decided. Every cross-world question in the dossier sits in `Build/worlds/_cross-world/NEEDS-RULING.md` or the world's `Open_Gaps_Tracking.md`. | Pass | dossier section 5 questions are in `Open_Gaps_Tracking.md` items 2, 3, 4 and 19 |
| 10 | The world's `Open_Gaps_Tracking.md` exists, with the library stage's own gaps already listed. | Pass | `Open_Gaps_Tracking.md` items 1 to 21 |
| 11 | No process narration is in anything that will become canonical. History goes to the build log. | Pass | `check_live_commentary.py --base origin/main --enforce` exits 0 |
| 12 | A one-page handoff manifest lists the paths above, the review round each step cleared in, and the date. The build thread reads it first. | Pass | this file |

## Outcome

| Field | Entry |
|---|---|
| Checks passed | 11 / 12 |
| Handoff gate run (`python -m engine.m10.cli handoff wsyr`) | 2026-10-02: check 1 fails on the unset `safety_adjacent`; checks 2 to 12 pass |
| Failed checks sent back to the source-research thread | none; check 1 waits on the project lead |
