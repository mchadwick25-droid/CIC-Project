# Handoff manifest: world `hus`

| Field | Entry |
|---|---|
| World code | hus |
| World id | the-hussite-and-bohemian-brethren-movement |
| `safety_adjacent` (`true` or `false`, set by Mark at handoff) | false, set by the project lead; the registry entry exists |
| Slug | the-hussite-and-bohemian-brethren-movement |
| Handoff date | 2026-09-30 |
| Prepared by | Library thread |
| Signed off by Mark on | not yet |

## Paths

| Item | Path |
|---|---|
| Registry entry | the registry entry for `hus` (not yet created) (not yet created) |
| Step 0 Movement-Scope Confirmation | `Build/worlds/hus/Step0_Movement_Scope_Confirmation.md` |
| Step 1 World Identification | `Build/worlds/hus/Doc_01_World_Identification_Boundaries_Orientation.md` |
| Step 2 Source Ecology | `Build/worlds/hus/Doc_02_Source_Ecology.md` |
| Source Readiness Dossier | `Build/worlds/_cross-world/dossiers/the-hussite-and-bohemian-brethren-movement_Source_Readiness_Dossier.md` |
| Corpus-map assignments | `cic/corpus-map/the-hussite-and-bohemian-brethren-movement.yaml` |
| Vendored texts (registry entries) | `cic/texts/REGISTRY.yaml` |
| Open gaps | `Build/worlds/hus/Open_Gaps_Tracking.md` |
| Cross-world questions | `Build/worlds/_cross-world/NEEDS-RULING.md` |
| Build log | `Build/worlds/hus/build/hus_Build_State.yaml` |

## Review round per step

| Step | Review round it cleared in | Review file | Date |
|---|---|---|---|
| Step 0 | 3 | Step0_Review_Round3.md | 2026-09-25 |
| Step 1 | 5 | Review-Artifacts/Doc01_Round5_Review.md | 2026-09-30 |
| Step 2 | 5 | Review-Artifacts/Doc02_Round5_Review.md | 2026-09-30 |

## The 12 handoff checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | The world's identity is fixed. Its registry entry at the registry entry for `hus` (not yet created) exists, with one `world_id`, before any of the world's records reach `main`. Every later file uses that same `world_id`. The entry carries `safety_adjacent: true` or `false`, set by Mark. A new world fails this check until it is set. | | |
| 2 | Step 0, Movement-Scope Confirmation, is approved to proceed. It cleared independent Opus review within the round cap, and the movement's own status in `cic-website/data/world-census.json` was checked. | | |
| 3 | Step 1, World Identification, is approved to proceed, under the same review rule. | | |
| 4 | Step 2, Source Ecology, is approved to proceed. Its Source Registry gives every item in the library package a line, and no dossier item, corpus-map entry or holdings-report file is missing one. | | |
| 5 | The Source Readiness Dossier is at `Build/worlds/_cross-world/dossiers/the-hussite-and-bohemian-brethren-movement_Source_Readiness_Dossier.md`. | | |
| 6 | The corpus-map assignments are at `cic/corpus-map/the-hussite-and-bohemian-brethren-movement.yaml`, and `python cic/engine/corpus_map_merge.py --check` passes. | | |
| 7 | The vendored texts are in `cic/texts/`, each with a `cic/texts/REGISTRY.yaml` entry and verified rights. Every assigned work opens, and `python cic/engine/corpus_index.py --build` is clean. | | |
| 8 | Every quotation in Steps 0-2 is re-verified word for word against the vendored file, speaker included. An opponent's paraphrase is never quoted as the subject's own words. | | |
| 9 | Open questions are carried forward, not decided. Every cross-world question in the dossier sits in `Build/worlds/_cross-world/NEEDS-RULING.md` or the world's `Open_Gaps_Tracking.md`. | | |
| 10 | The world's `Open_Gaps_Tracking.md` exists, with the library stage's own gaps already listed. | | |
| 11 | No process narration is in anything that will become canonical. History goes to the build log. | | |
| 12 | A one-page handoff manifest lists the paths above, the review round each step cleared in, and the date. The build thread reads it first. | | |

## Outcome

| Field | Entry |
|---|---|
| Checks passed | / 12 |
| Handoff gate run (`python -m engine.m10.cli handoff hus`) | |
| Failed checks sent back to the source-research thread | |
