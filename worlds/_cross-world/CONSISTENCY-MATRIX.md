# Per-world consistency matrix — six formation worlds

Generated from the live tree at `9128cf21be84` by `worlds/_cross-world/gen_matrix.py`. Every cell is measured, not transcribed. Companion to `CiC_Cross_System_Consistency_Audit_2026-08-26.md`, which carries the reasoning and the findings.

**Verdict column.** `OK` — every world agrees, and agreement is the contract. `DRIFT` — worlds disagree on something the pipeline treats as one shape; a bolded cell is the world that differs. `VARIES` — worlds differ on something with no fixed contract; the numbers are reported so a reader can tell substance apart from build effort, and nothing here is a defect on its own.


## 1. Registry — `records/worlds.yaml`

| invariant | verdict | `alx` | `pahc` | `desert` | `hal` | `syr` | `ijc` |
|---|---|---|---|---|---|---|---|
| entry carries the full key set | OK | 11 keys | 11 keys | 11 keys | 11 keys | 11 keys | 11 keys |
| `census_id` set and resolves to a Built & Live census entry | OK | yes | yes | yes | yes | yes | yes |
| `world_id` == `census_id` | DRIFT | yes | yes | yes | yes | yes | **no** |
| `display_name` == census formal `name` | DRIFT | **no** | yes | yes | yes | yes | yes |
| `living_tradition_flag` == census `living` | DRIFT | **no** | **no** | yes | **no** | yes | **no** |
| `representative.name` == census `representativeName` | DRIFT | yes | yes | yes | yes | **no** | yes |
| `representative.role_label` == census `representativeTitle` | DRIFT | yes | **no** | **no** | yes | **no** | **no** |
| `time_window` == census `start`/`end` | OK | yes | yes | yes | yes | yes | yes |
| `state` / `kind` | OK | built/formation | built/formation | built/formation | built/formation | built/formation | built/formation |
| package pinned (`location` + `manifest_hash`, manifest on disk) | OK | yes | yes | yes | yes | yes | yes |

## 2. Records — `records/<world>/`

| invariant | verdict | `alx` | `pahc` | `desert` | `hal` | `syr` | `ijc` |
|---|---|---|---|---|---|---|---|
| record-type directories present | OK | 14 | 14 | 14 | 14 | 14 | 14 |
| M1 gate battery (15 gates) | OK | 15/15 green | 15/15 green | 15/15 green | 15/15 green | 15/15 green | 15/15 green |
| `schema_version` on every record | OK | 2 | 2 | 2 | 2 | 2 | 2 |
| record `world_id` + id prefix agree with registry | OK | yes | yes | yes | yes | yes | yes |
| id type-token vocabulary matches the fleet | DRIFT | yes | **`witness.` / `craft.`** | yes | yes | yes | yes |
| `confidence` block complete on every record | OK | 175/175 | 128/128 | 127/127 | 153/153 | 160/160 | 154/154 |
| `figure.dates` key vocabulary | DRIFT | born/died/floruit | died/display/note | born/died/floruit | born/died/floruit | born/died/floruit | born/died/floruit |
| quote speaker resolves to a readable label | DRIFT | yes | yes | yes | yes | **4 raw ids** | yes |
| no record id / build ref in participant-facing fields | DRIFT | yes | yes | **3 leaks** | yes | yes | yes |
| `voice_craft.flavor_notes` segment vocabulary | VARIES | 5 segs | 4 segs | 4 segs | 5 segs | 5 segs | 8 segs |

## 2b. Records — measured, no fixed contract

| invariant | verdict | `alx` | `pahc` | `desert` | `hal` | `syr` | `ijc` |
|---|---|---|---|---|---|---|---|
| records total (density — expected to vary) | VARIES | 175 | 128 | 127 | 153 | 160 | 154 |
| `retrieval.retrieve_when` coverage (READ at turn time) | VARIES | 59/72 (82%) | 43/43 (100%) | 40/40 (100%) | 35/51 (69%) | 19/41 (46%) | 21/33 (64%) |
| `retrieval.tier` spread (read by no runtime path) | VARIES | 59/13/0 | 16/22/5 | 20/16/4 | 26/21/4 | 27/12/2 | 22/8/3 |
| `do_not_retrieve_when` authored (enforced nowhere) | VARIES | 40 | 29 | 11 | 10 | 19 | 16 |
| `sources[].license` filled | VARIES | 254/254 | 189/189 | 80/192 | 215/215 | 246/246 | 201/201 |
| `source.external_ids` filled | VARIES | 20/20 | 15/18 | 10/24 | 22/23 | 14/36 | 20/23 |
| `demonstration.tags` filled | VARIES | 7/7 | 5/9 | 5/9 | 8/8 | 3/8 | 9/9 |
| `contested_claim.divergence_partners` filled | VARIES | 2/5 | 9/9 | 3/3 | 7/7 | 2/8 | 2/7 |

## 3. Compiler + package — `engine/m2` → `packages/<world>/<id>/`

| invariant | verdict | `alx` | `pahc` | `desert` | `hal` | `syr` | `ijc` |
|---|---|---|---|---|---|---|---|
| compiled file classes emitted | OK | 14 classes | 14 classes | 14 classes | 14 classes | 14 classes | 14 classes |
| `prompt.txt` section kinds | OK | 19 kinds | 19 kinds | 19 kinds | 19 kinds | 19 kinds | 19 kinds |
| `frame.json` fields, all non-null | OK | 9/9 | 9/9 | 9/9 | 9/9 | 9/9 | 9/9 |
| validation/ files emitted | OK | 3 | 3 | 3 | 3 | 3 | 3 |
| package not stale vs pinned manifest hash | OK | yes | yes | yes | yes | yes | yes |

## 4. Engine runtime — `engine/m4`, `engine/m5`

| invariant | verdict | `alx` | `pahc` | `desert` | `hal` | `syr` | `ijc` |
|---|---|---|---|---|---|---|---|
| per-world branching in code | OK | none | none | none | none | none | none |
| canon cells substantive / honest-limit (of 28) | VARIES | 27/1 | 27/1 | 24/4 | 26/2 | 27/1 | 24/4 |
| doorway starter cells selected | OK | C-I,C-P,C-E | C-I,C-P,C-E | C-I,C-P,C-E | C-I,C-P,C-E | C-I,C-P,C-E | C-I,C-P,C-E |
| M5 anachronism terms in reach (1-entry fleet dictionary) | VARIES | none | trinity | none | none | none | none |

## 5. API — `GET /api/worlds`

| invariant | verdict | `alx` | `pahc` | `desert` | `hal` | `syr` | `ijc` |
|---|---|---|---|---|---|---|---|
| world summary fields returned | OK | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 | 10/10 |
| `census_id` passed through to the client | OK | yes | yes | yes | yes | yes | yes |

## 6. Front ends — `cic-poc/frontend`, `cic-website`

| invariant | verdict | `alx` | `pahc` | `desert` | `hal` | `syr` | `ijc` |
|---|---|---|---|---|---|---|---|
| app `WORLD_ASSETS` + `WORLD_ORDER` entry | OK | yes | yes | yes | yes | yes | yes |
| site `PORTRAIT_FILES` entry | OK | yes | yes | yes | yes | yes | yes |
| Atlas deep link reaches the doorway | OK | yes | yes | yes | yes | yes | yes |
| distinct participant-facing names for one world (registry `display_name` + census `name`/`shortName`/`entry.worldName`) | VARIES | 3 | 3 | 3 | 3 | 3 | 3 |
| Atlas `dates` string house style (en-dash + CE) | DRIFT | yes | yes | yes | yes | yes | **c. 312-451** |

