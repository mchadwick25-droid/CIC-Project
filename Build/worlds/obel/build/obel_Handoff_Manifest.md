# Handoff manifest: world `obel`

| Field | Entry |
|---|---|
| World code | obel |
| World id | the-old-believers |
| `safety_adjacent` (`true` or `false`, set by Mark at handoff) | not yet set; the project lead sets it |
| Slug | the-old-believers |
| Handoff date | 2026-10-02 |
| Prepared by | Library thread |
| Signed off by Mark on | not yet |

## Paths

| Item | Path |
|---|---|
| Registry entry | `records/worlds/obel.yaml` |
| Step 0 Movement-Scope Confirmation | `Build/worlds/obel/Step0_Movement_Scope_Confirmation.md` |
| Step 1 World Identification | `Build/worlds/obel/Doc_01_World_Identification_Boundaries_Orientation.md` |
| Step 2 Source Ecology | `Build/worlds/obel/Doc_02_Source_Ecology.md` |
| Source Registry | `Build/worlds/obel/Source_Registry.md` |
| Source Readiness Dossier | `Build/worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_Dossier.md` |
| Corpus-map assignments | `cic/corpus-map/the-old-believers.yaml` |
| Vendored texts (registry entries) | `cic/texts/REGISTRY.yaml` |
| Open gaps | `Build/worlds/obel/Open_Gaps_Tracking.md` |
| Cross-world questions | `Build/worlds/_cross-world/NEEDS-RULING.md` |
| Build log | `Build/worlds/obel/build/obel_Build_State.yaml` |

## Review round per step

The three steps were reviewed together: a Round 1 review and a Round 2 targeted recheck. The project lead's ruling of 2026-09-26 (System Hub Decision Log, "Escalation does not park the document: a named escalated item waits, the document proceeds") settled the one escalation question the Round 2 recheck raised, and the Round 2 files carry the line `Disposition: Approved to proceed`. The one item that waits is the census `floorNote`.

| Step | Review round it cleared in | Review file | Date |
|---|---|---|---|
| Step 0 | 2 | Step0_Review_Round2.md | 2026-09-26 |
| Step 1 | 2 | Review-Artifacts/Doc01_Round2_Review.md | 2026-09-26 |
| Step 2 | 2 | Review-Artifacts/Doc02_Round2_Review.md | 2026-09-26 |

## The 12 handoff checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | The world's identity is fixed. Its registry entry at `records/worlds/obel.yaml` exists, with one `world_id`, before any of the world's records reach `main`. Every later file uses that same `world_id`. The entry carries `safety_adjacent: true` or `false`, set by Mark. A new world fails this check until it is set. | Open | `safety_adjacent` is unset; the project lead sets it |
| 2 | Step 0, Movement-Scope Confirmation, is approved to proceed. It cleared independent Opus review within the round cap, and the movement's own status in `cic-website/data/world-census.json` was checked. | Pass | `Step0_Review_Round2.md` carries the disposition line; the census check passes |
| 3 | Step 1, World Identification, is approved to proceed, under the same review rule. | Pass | `Review-Artifacts/Doc01_Round2_Review.md` |
| 4 | Step 2, Source Ecology, is approved to proceed. Its Source Registry gives every item in the library package a line, and no dossier item, corpus-map entry or holdings-report file is missing one. | Pass | `Review-Artifacts/Doc02_Round2_Review.md`; `Source_Registry.md` rows 1 to 12 |
| 5 | The Source Readiness Dossier is at `Build/worlds/_cross-world/dossiers/the-old-believers_Source_Readiness_Dossier.md`. | Pass | dossier present, five sections, no ISO dates in header |
| 6 | The corpus-map assignments are at `cic/corpus-map/the-old-believers.yaml`, and `python cic/engine/corpus_map_merge.py --check` passes. | Pass | `corpus_map_merge.py --check` valid; every row has a `row_id` |
| 7 | The vendored texts are in `cic/texts/`, each with a `cic/texts/REGISTRY.yaml` entry and verified rights. Every assigned work opens, and `python cic/engine/corpus_index.py --build` is clean. | Pass | `handoff` check 7 passes |
| 8 | Every quotation in Steps 0-2 is re-verified word for word against the vendored file, speaker included. An opponent's paraphrase is never quoted as the subject's own words. | Pass | 34 quotations checked, 14 from project documents, 20 found in an assigned file with no `cic:` address cited |
| 9 | Open questions are carried forward, not decided. Every cross-world question in the dossier sits in `Build/worlds/_cross-world/NEEDS-RULING.md` or the world's `Open_Gaps_Tracking.md`. | Pass | dossier section 5 question is in `Open_Gaps_Tracking.md` (the Greek-authority cross-link entry) |
| 10 | The world's `Open_Gaps_Tracking.md` exists, with the library stage's own gaps already listed. | Pass | `Open_Gaps_Tracking.md` entries 1 to 25 |
| 11 | No process narration is in anything that will become canonical. History goes to the build log. | Pass | `check_live_commentary.py --base origin/main --enforce` exits 0 |
| 12 | A one-page handoff manifest lists the paths above, the review round each step cleared in, and the date. The build thread reads it first. | Pass | this file |

## Outcome

| Field | Entry |
|---|---|
| Checks passed | 11 / 12 |
| Handoff gate run (`python -m engine.m10.cli handoff obel`) | 2026-10-02: check 1 fails on the unset `safety_adjacent`; checks 2 to 12 pass |
| Failed checks sent back to the source-research thread | none; check 1 waits on the project lead |
