# Handoff manifest: world `lpc`

| Field | Entry |
|---|---|
| World code | `lpc` |
| World id | `latin-pastoral-congregational-christianity` |
| `safety_adjacent` (`true` or `false`, set by Mark at handoff) | `false`, set by Mark |
| Slug | `latin-pastoral-congregational-christianity` |
| Handoff date | 2026-09-30 |
| Prepared by | the `lpc` build thread, from the final gate run |
| Signed off by Mark on | pending |

## Paths

| Item | Path |
|---|---|
| Registry entry | `records/worlds/lpc.yaml` |
| Step 0 Movement-Scope Confirmation | `Build/worlds/lpc/Step0_Movement_Scope_Confirmation.md` |
| Step 1 World Identification | `Build/worlds/lpc/Doc_01_World_Identification_Boundaries_Orientation.md` |
| Step 2 Source Ecology | `Build/worlds/lpc/Doc_02_Source_Ecology.md` |
| Source Readiness Dossier | `Build/worlds/_cross-world/dossiers/latin-pastoral-congregational-christianity_Source_Readiness_Dossier.md` |
| Corpus-map assignments | `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` |
| Vendored texts (registry entries) | `cic/texts/REGISTRY.yaml` |
| Open gaps | `Build/worlds/lpc/Open_Gaps_Tracking.md` |
| Cross-world questions | `Build/worlds/_cross-world/NEEDS-RULING.md` |
| Build log | `Build/worlds/lpc/lpc_Decision_Log.md` |

## Review round per step

| Step | Review round it cleared in | Review file | Date |
|---|---|---|---|
| Step 0 | 5 | `Build/worlds/lpc/Review-Artifacts/Step0_Round5_Review.md` | 2026-09-01 |
| Step 1 | 9 | `Build/worlds/lpc/Review-Artifacts/Doc01_Round9_Review.md` | 2026-09-01 |
| Step 2 | 30 | `Build/worlds/lpc/Review-Artifacts/Doc02_Round30_Review.md` | 2026-09-26 |

The three steps cleared under the earlier process. The project lead accepted the round counts and the approval wording in the declaration of 2026-09-29 (`Build/worlds/lpc/build/lpc_Rebaseline_Declaration.md`). The independent checks run since then are listed under Open gaps.

## The 12 handoff checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | The world's identity is fixed. Its registry entry at `records/worlds/<code>.yaml` exists, with one `world_id`, before any of the world's records reach `main`. Every later file uses that same `world_id`. The entry carries `safety_adjacent: true` or `false`, set by Mark. A new world fails this check until it is set. | PASS | `handoff-01-identity: PASS` |
| 2 | Step 0, Movement-Scope Confirmation, is approved to proceed. It cleared independent Opus review within the round cap, and the movement's own status in `cic-website/data/world-census.json` was checked. | PASS (2 accepted) | `handoff-02-step0: PASS (2 accepted)`; round cap and verdict wording accepted by the declaration |
| 3 | Step 1, World Identification, is approved to proceed, under the same review rule. | PASS (2 accepted) | `handoff-03-step1: PASS (2 accepted)` |
| 4 | Step 2, Source Ecology, is approved to proceed. Its Source Registry gives every item in the library package a line, and no dossier item, corpus-map entry or holdings-report file is missing one. | PASS (2 accepted) | `handoff-04-step2: PASS (2 accepted)`; the Registry has 355 rows |
| 5 | The Source Readiness Dossier is at `Build/worlds/_cross-world/dossiers/<slug>_Source_Readiness_Dossier.md`. | PASS | `handoff-05-dossier: PASS` |
| 6 | The corpus-map assignments are at `cic/corpus-map/<slug>.yaml`, and `python cic/engine/corpus_map_merge.py --check` passes. | FAIL (Library-owned) | `handoff-06-corpus-map: FAIL`: the generated corpus-map file on main carries no `row_id` on any of its 147 rows; the Library issues every `row_id` |
| 7 | The vendored texts are in `cic/texts/`, each with a `cic/texts/REGISTRY.yaml` entry and verified rights. Every assigned work opens, and `python cic/engine/corpus_index.py --build` is clean. | PASS | `handoff-07-texts: PASS` |
| 8 | Every quotation in Steps 0-2 is re-verified word for word against the vendored file, speaker included. An opponent's paraphrase is never quoted as the subject's own words. | PASS | `handoff-08-quotes: PASS`; 207 quotations checked, 0 unverified, 0 unbalanced |
| 9 | Open questions are carried forward, not decided. Every cross-world question in the dossier sits in `Build/worlds/_cross-world/NEEDS-RULING.md` or the world's `Open_Gaps_Tracking.md`. | PASS | `handoff-09-open-questions: PASS` |
| 10 | The world's `Open_Gaps_Tracking.md` exists, with the library stage's own gaps already listed. | PASS | `handoff-10-ledger: PASS` |
| 11 | No process narration is in anything that will become canonical. History goes to the build log. | PASS | `handoff-11-narration: PASS`; removed text is kept in `Build/Ministry/Operations/Audits/lpc_Live_Surface_History_2026-09-30.md` |
| 12 | A one-page handoff manifest lists the paths above, the review round each step cleared in, and the date. The build thread reads it first. | PASS | this file |

## Outcome

| Field | Entry |
|---|---|
| Checks passed | 11 / 12 (check 6 is the Library's to fix; three steps pass with pre-V2.0 approval history accepted by declaration) |
| Handoff gate run (`python -m engine.m10.cli handoff <code>`) | 2026-09-30, after the merge with main |
| Failed checks sent back to the source-research thread | check 6: `row_id` for the generated corpus-map file, and its re-merge (the staging files hold 59 lpc assignments the generated file lacks) |
