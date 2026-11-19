# Handoff manifest: world `latap`

| Field | Entry |
|---|---|
| World code | latap |
| World id | latin-apologists |
| `safety_adjacent` (`true` or `false`, set by Mark at handoff) | not yet set; the project lead's call. The registry entry exists at `records/worlds/latap.yaml` |
| Slug | latin-apologists |
| Handoff date | 2026-10-31 (prepared; Step 2 approved to proceed, not Frozen) |
| Prepared by | Library thread |
| Signed off by Mark on | not yet |

## Paths

| Item | Path |
|---|---|
| Registry entry | `records/worlds/latap.yaml` |
| Step 0 Movement-Scope Confirmation | `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md` |
| Step 1 World Identification | `Build/worlds/latap/Doc_01_World_Identification_Boundaries_Orientation.md` |
| Step 2 Source Ecology | `Build/worlds/latap/Doc_02_Source_Ecology.md` |
| Source Readiness Dossier | `Build/worlds/_cross-world/dossiers/latin-apologists_Source_Readiness_Dossier.md` |
| Corpus-map assignments | `cic/corpus-map/latin-apologists.yaml` |
| Vendored texts (registry entries) | `cic/texts/REGISTRY.yaml` |
| Open gaps | `Build/worlds/latap/Open_Gaps_Tracking.md` |
| Cross-world questions | `Build/worlds/_cross-world/NEEDS-RULING.md` |
| Build log | `Build/worlds/latap/build/latap_Build_State.yaml` |

## Review round per step

| Step | Review round it cleared in | Review file | Date |
|---|---|---|---|
| Step 0 | 7 (past the three-round cap; the cap ruling of 2026-10-29 is on file in `CiC_System_Hub_Decision_Log.md`, naming `Review-Artifacts/Step0_CapRuling_Review.md`) | Review-Artifacts/Step0_Round7_Review.md | 2026-09-29 |
| Step 1 | 3 | Review-Artifacts/Doc01_Round3_Review.md | 2026-10-29 |
| Step 2 | 2 | Review-Artifacts/Doc02_Round2_Review.md | 2026-10-29 |

## The 12 handoff checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | The world's identity is fixed. Its registry entry at the registry entry for `latap` exists, with one `world_id`, before any of the world's records reach `main`. Every later file uses that same `world_id`. The entry carries `safety_adjacent: true` or `false`, set by Mark. A new world fails this check until it is set. | FAIL | `records/worlds/latap.yaml` has no `safety_adjacent` field. Mark sets it. |
| 2 | Step 0, Movement-Scope Confirmation, is approved to proceed. It cleared independent Opus review within the round cap, and the movement's own status in `cic-website/data/world-census.json` was checked. | FAIL | Step 0 has 7 review files against a cap of 3, and the latest numbered review (round 7) does not say Approved to proceed. The targeted cap-ruling review (`Review-Artifacts/Step0_CapRuling_Review.md`) says Approved to proceed (Step 0 only; not Frozen); the gate does not read it. Owner: engine/m10 tooling; the cap ruling is on file in `CiC_System_Hub_Decision_Log.md`. |
| 3 | Step 1, World Identification, is approved to proceed, under the same review rule. | PASS | |
| 4 | Step 2, Source Ecology, is approved to proceed. Its Source Registry gives every item in the library package a line, and no dossier item, corpus-map entry or holdings-report file is missing one. | PASS | |
| 5 | The Source Readiness Dossier is at `Build/worlds/_cross-world/dossiers/latin-apologists_Source_Readiness_Dossier.md`. | PASS | |
| 6 | The corpus-map assignments are at `cic/corpus-map/latin-apologists.yaml`, and `python cic/engine/corpus_map_merge.py --check` passes. | PASS | `corpus_map_merge.py --check` reports no findings. |
| 7 | The vendored texts are in `cic/texts/`, each with a `cic/texts/REGISTRY.yaml` entry and verified rights. Every assigned work opens, and `python cic/engine/corpus_index.py --build` is clean. | PASS | |
| 8 | Every quotation in Steps 0-2 is re-verified word for word against the vendored file, speaker included. An opponent's paraphrase is never quoted as the subject's own words. | FAIL | One quotation in Step 0 (the Arnobius passage in section 4 item 2) is not found word for word; the words are right and the checker cannot read the line-number tag inside them. Kept flagged on purpose by the Step 0 quotation change order. |
| 9 | Open questions are carried forward, not decided. Every cross-world question in the dossier sits in `Build/worlds/_cross-world/NEEDS-RULING.md` or the world's `Open_Gaps_Tracking.md`. | PASS | |
| 10 | The world's `Open_Gaps_Tracking.md` exists, with the library stage's own gaps already listed. | PASS | |
| 11 | No process narration is in anything that will become canonical. History goes to the build log. | PASS | |
| 12 | A one-page handoff manifest lists the paths above, the review round each step cleared in, and the date. The build thread reads it first. | PASS | |

## Outcome

| Field | Entry |
|---|---|
| Checks passed | 9 / 12 |
| Handoff gate run (`python -m engine.m10.cli handoff latap`) | Full run on 2026-10-31, quotation check included. Checks 3, 4, 5, 6, 7, 9, 10, 11 and 12 pass (9 of 12); checks 1, 2 and 8 fail. |
| Failed checks sent back to the source-research thread | None. Check 1 (`safety_adjacent`) is Mark's call. Check 2 is a gap in the gate, not an open ruling: the cap ruling is on file and Step 0 is approved to proceed, but `latest_review` (`engine/m10/rounds.py`) reads only round 7 and counts seven numbered rounds; the owner is the engine/m10 tooling. Check 8 is the Arnobius flag kept on purpose; a later change order may close it. |
