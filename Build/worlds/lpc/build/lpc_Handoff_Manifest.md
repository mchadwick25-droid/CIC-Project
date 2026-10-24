# Handoff manifest: world `lpc`

| Field | Entry |
|---|---|
| World code | lpc |
| World id | latin-pastoral-congregational-christianity |
| `safety_adjacent` (`true` or `false`, set by Mark at handoff) | true (project lead, 2026-10-23) |
| Slug | latin-pastoral-congregational-christianity |
| Handoff date | 2026-10-23 |
| Prepared by | `lpc` build thread |
| Signed off by Mark on | |

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
| Step 0 | Round 5 (accepted by the rebaseline declaration) | `Build/worlds/lpc/Review-Artifacts/Step0_Round5_Review.md` | 2026-09-01 |
| Step 1 | Round 9 (accepted by the rebaseline declaration) | `Build/worlds/lpc/Review-Artifacts/Doc01_Round9_Review.md` | 2026-09-01 |
| Step 2 | Round 30 (accepted by the rebaseline declaration) | `Build/worlds/lpc/Review-Artifacts/Doc02_Round30_Review.md` | 2026-09-10 |

## The 12 handoff checks

Results of `python -m engine.m10.cli handoff lpc`, run 2026-10-23 before the declaration amendment.

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Identity and registry entry, `safety_adjacent` set | PASS | `records/worlds/lpc.yaml` |
| 2 | Step 0 approved to proceed; census status checked | FAIL | Step 0 does not record the movement's status in `world-census.json` (OG-43) |
| 3 | Step 1 approved to proceed | FAIL | Review-count findings; covered by the declaration amendment of 2026-10-23, to re-run |
| 4 | Step 2 approved; every item has a Registry line | FAIL | Review count (amended); 55 holdings files and 2 corpus-map works with no Registry line (OG-44) |
| 5 | Source Readiness Dossier exists | PASS | Path above |
| 6 | Corpus-map assignments | PASS | Path above |
| 7 | Vendored texts registered | PASS | `cic/texts/REGISTRY.yaml` |
| 8 | Quotations re-verified word for word | FAIL | 194 findings; triage running (OG-45) |
| 9 | Open questions carried forward | FAIL | Two dossier section 5 items (OG-43) |
| 10 | Open_Gaps_Tracking.md exists | PASS | Path above |
| 11 | No process narration in canonical files | FAIL | 9 sites in Step 0, Doc_01 and the dossier (OG-43) |
| 12 | This manifest | FAIL | Did not exist; written 2026-10-23 |

## Outcome

| Field | Entry |
|---|---|
| Checks passed | 5 / 12 (before the fixes of 2026-10-23) |
| Handoff gate run (`python -m engine.m10.cli handoff lpc`) | 2026-10-23 |
| Failed checks sent back to the source-research thread | Check 4 holdings lines (OG-44) |
