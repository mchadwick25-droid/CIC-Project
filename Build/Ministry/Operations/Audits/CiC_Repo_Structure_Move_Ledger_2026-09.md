# Repo Structure — Move Ledger

Supplemental record of every path moved, renamed, or deleted by the Repo Structure
Cleanup thread. The moved files carry no notes (P11); this ledger and
`Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md` are the record.
Anyone reading a dated document that cites an old path finds the new one here.

## Phase 1 — cold zone — 2026-09-14 — commit `5aedf3df`

Citations rewritten by `tools/rewrite_paths.py`: 425 replacements in 198 files (current documents only; `records/`, `Archive/` and dated Ministry history untouched).

| from | to | kind |
|---|---|---|
| `L0-Reference` | `reference/L0-Reference` | dir |
| `L1-Foundation` | `reference/L1-Foundation` | dir |
| `L2A-System-Architecture` | `reference/L2A-System-Architecture` | dir |
| `L2B-System-Entry` | `reference/L2B-System-Entry` | dir |
| `L2C-System-Status` | `reference/L2C-System-Status` | dir |
| `L2D-System-Operations` | `reference/L2D-System-Operations` | dir |
| `L3A-Shared-Methodology` | `reference/L3A-Shared-Methodology` | dir |
| `L3B-World-Build-Methodology` | `reference/L3B-World-Build-Methodology` | dir |
| `L3C-Representative-Methodology` | `reference/L3C-Representative-Methodology` | dir |
| `L3D-Encounter-Methodology` | `reference/L3D-Encounter-Methodology` | dir |
| `L4-Templates` | `reference/L4-Templates` | dir |
| `Redesign-Spec` | `reference/Redesign-Spec` | dir |
| `Project-Reference` | `reference/Project-Reference` | dir |
| `fleet-voice` | `reference/fleet-voice` | dir |
| `Syriac-Build` | `Archive/Syriac-Build-2026-07` | dir |
| `Ministry/Technology/Pass2/decisions` | `reference/method/Pass2-decisions` | dir |
| `Ministry/Technology/Pass2` | `Archive/Technology-Pass2-2026-08/Pass2` | dir |
| `Ministry/Technology/Pass3` | `Archive/Technology-Pass2-2026-08/Pass3` | dir |
| `Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_3.md` | `reference/method/CiC_Record_Native_World_Build_Process_V1_3.md` | file |
| `Ministry/Technology/CiC_World_Build_Completion_Standard_V1.3.md` | `reference/method/CiC_World_Build_Completion_Standard_V1.3.md` | file |
| `Ministry/Technology/CiC_Register_Bar_2026-08-29.md` | `reference/method/CiC_Register_Bar_2026-08-29.md` | file |
| `Ministry/Technology/CiC_Representative_Naming_Role_Discipline_2026-09-08.md` | `reference/method/CiC_Representative_Naming_Role_Discipline_2026-09-08.md` | file |
| `Ministry/Technology/CiC_Voice_Style_Guide_and_Scaling_Plan.md` | `reference/method/CiC_Voice_Style_Guide_and_Scaling_Plan.md` | file |
| `Ministry/Operations/Standing/CiC_Adversarial_Review_Standard_Practice.md` | `reference/method/CiC_Adversarial_Review_Standard_Practice.md` | file |
| `Ministry/Features/Atlas-World-Map/Design/tools/validate-census.mjs` | `tools/validate-census.mjs` | file |
| `Ministry/Operations/Standing/lexicon_compliance_checker.py` | `tools/lexicon_compliance_checker.py` | file |
| `CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md` | `reference/L3D-Encounter-Methodology/CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md` | file |
| `CiC_L3D_RelationalSafety_ResourceNaming_Decision_Options.md` | `reference/L3D-Encounter-Methodology/CiC_L3D_RelationalSafety_ResourceNaming_Decision_Options.md` | file |
| `CiC_Live_Safety_Testing_Script_2026-07-21.docx` | `reference/L3D-Encounter-Methodology/CiC_Live_Safety_Testing_Script_2026-07-21.docx` | file |
| `CiC_Step0_Conclusion_FINAL.docx` | `Archive/Superseded-Housekeeping/CiC_Step0_Conclusion_FINAL.docx` | file |
| `CiC_Step0_Conclusion_FINAL_v2.docx` | `reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx` | file |
| `CiC_Step2_Comparative_Source_Ecology_DRAFT.docx` | `Archive/Superseded-Housekeeping/CiC_Step2_Comparative_Source_Ecology_DRAFT.docx` | file |
| `cic_build_cycle_co022.skill` | `Archive/Superseded-Housekeeping/cic_build_cycle_co022.skill` | file |
| `cic_build_cycle_co023.skill` | `Archive/Superseded-Housekeeping/cic_build_cycle_co023.skill` | file |
| `cic_build_cycle_co024.skill` | `Archive/Superseded-Housekeeping/cic_build_cycle_co024.skill` | file |
| `cic_build_cycle_co024b.skill` | `Archive/Superseded-Housekeeping/cic_build_cycle_co024b.skill` | file |
| `CiC_Fable_Analysis_Disciplined_Rebuild_vs_Current_2026-07-04.md` | `Ministry/Operations/Audits/CiC_Fable_Analysis_Disciplined_Rebuild_vs_Current_2026-07-04.md` | file |
| `CiC_Fable_Cascade_Followup_2026-07-04.md` | `Ministry/Operations/Audits/CiC_Fable_Cascade_Followup_2026-07-04.md` | file |
| `CiC_Status_Report_2026-07-04.md` | `Ministry/Operations/Audits/CiC_Status_Report_2026-07-04.md` | file |
| `CiC_Containment_Review.md` | `Ministry/Operations/Audits/CiC_Containment_Review.md` | file |
| `CiC_Jonathan_Orientation_Briefing_V1.docx` | `Ministry/Communication/CiC_Jonathan_Orientation_Briefing_V1.docx` | file |
| `Project-Reference/CiC_Project_Learning_Notes_June2026.docx` | `Archive/Superseded-Housekeeping/CiC_Project_Learning_Notes_June2026.docx` | file-after-dir |
| `Project-Reference/CiC_Project_Status_July2026.docx` | `Archive/Superseded-Housekeeping/CiC_Project_Status_July2026.docx` | file-after-dir |
| `Project-Reference/CiC_Technology_Review_Findings_v1_0.docx` | `Archive/Superseded-Housekeeping/CiC_Technology_Review_Findings_v1_0.docx` | file-after-dir |
| `L3C-Representative-Methodology/desktop.ini` | deleted | delete |
| `Syriac-Build/L3C-Representative-Methodology/desktop.ini` | deleted | delete |

### Known-stale: binaries that embed an old path and cannot be rewritten (13)

Each cites a path this phase moved; the file itself is unchanged. Read the citation through the table above.

- `Ministry/Communication/CiC_Jonathan_Orientation_Briefing_V1.docx` — cites `CiC_Fable_Analysis_Disciplined_Rebuild_vs_Current_2026-07-04.md`, `CiC_Fable_Cascade_Followup_2026-07-04.md`
- `Ministry/Features/Front-End-Integration-Strategy/Design/CiC_FrontEnd_Design_Brief_V1_0.docx` — cites `Project-Reference`
- `Ministry/Funding/CiC_BuildApproach_Budget_Proposals_V1_0.xlsx` — cites `Project-Reference`
- `World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Doc02_Source_Ecology_FINAL.docx` — cites `L3B-World-Build-Methodology`
- `World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Doc02_Source_Ecology_FINAL_v2.docx` — cites `L3B-World-Build-Methodology`
- `World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Doc02_Source_Ecology_FINAL_v3.docx` — cites `L3B-World-Build-Methodology`
- `World-Builds/Cappadocian/cappadocian_Doc_01_World_Identification.docx` — cites `CiC_Step0_Conclusion_FINAL_v2.docx`
- `reference/L2A-System-Architecture/CiC_L2A_Clean_File_Structure_V1.1.docx` — cites `L3C-Representative-Methodology`, `L3B-World-Build-Methodology`, `L3D-Encounter-Methodology`, `L2A-System-Architecture`, `L3A-Shared-Methodology`, `L2D-System-Operations`, `L2C-System-Status`, `Project-Reference`, `L2B-System-Entry`, `L1-Foundation`, `L4-Templates`
- `reference/L2C-System-Status/CiC_L2C_Change_Orders_Register_V1_18.docx` — cites `L3D-Encounter-Methodology`, `L2C-System-Status`, `Project-Reference`, `L1-Foundation`, `L4-Templates`
- `reference/L2C-System-Status/CiC_L2C_Corrections_Tracker_V1.2.docx` — cites `Project-Reference`, `L4-Templates`
- `reference/L3B-World-Build-Methodology/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Blueprint_V7.3.docx` — cites `L3B-World-Build-Methodology`
- `reference/L3B-World-Build-Methodology/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — cites `L3B-World-Build-Methodology`
- `reference/L3B-World-Build-Methodology/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Template_V1.5.docx` — cites `L3B-World-Build-Methodology`

### Correction in the commit following `5aedf3df`

The single-file moves into `reference/L3B-World-Build-Methodology/` and
`reference/L3D-Encounter-Methodology/` ran before the directory moves, so `git mv`
nested each directory inside the one it had just created
(`reference/L3B-World-Build-Methodology/L3B-World-Build-Methodology/…`, likewise L3D).
Both were flattened to the intended paths in the next commit; no file was lost and the
rewritten citations resolve at the flat paths. `tools/check_paths_baseline.txt` was
rebuilt from a diff against the pre-move tree rather than regenerated blind.

### Not rewritten by design

- `records/` (75 citations, mostly `reference/method/CiC_Register_Bar_2026-08-29.md`): a record is copied byte-for-byte into its package and hashed; each world's thread corrects these at its next recompile and repin.
- `Archive/`, `Ministry/Operations/Audits/`, decision logs, launch prompts, tracking documents and dated files: history describes the tree as it was; this ledger maps old to new.
- `canon/`, `fixtures/`, `cic/texts/`, `packages/`: sealed, hashed or vendored.

## Phase 2 — hot zone — 2026-09-15

Citations rewritten by `tools/rewrite_paths.py` against `tools/moves-phase2.tsv`: 955
replacements in 300 files (current documents only; `records/`, `Archive/` and dated
Ministry history untouched, same convention as phase 1).

| from | to | kind |
|---|---|---|
| `World-Builds/01-Post-Apostolic-House-Church` | `worlds/pahc` | dir |
| `World-Builds/Alexandria-Catechetical-School` | `worlds/alx` | dir |
| `World-Builds/Cappadocian` | `worlds/cappadocian` | dir |
| `World-Builds/Desert-Monasticism` | `worlds/desert` | dir |
| `World-Builds/Donatism` | `worlds/don` | dir |
| `World-Builds/Hieronymian-Ascetic-Literary` | `worlds/hal` | dir |
| `World-Builds/Imperial-Juridical-Christianity` | `worlds/ijc` | dir |
| `World-Builds/Syriac-Christianity-Edessa-Nisibis` | `worlds/syr` | dir |
| `World-Builds/Gallic-Monastic-Ascetic-Christianity` | `worlds/gallic` | dir |
| `World-Builds/Latin-Pastoral-Congregational-Christianity` | `worlds/lpc` | dir |
| `World-Builds/Latin-Apologists` | `worlds/latap` | dir |
| `World-Builds/Second-Century-Greek-Apologists` | `worlds/grkap` | dir |
| `world-build-docs/_cross-world` | `worlds/_cross-world` | dir |
| `world-build-docs/alx` | `worlds/alx/build` | dir |
| `world-build-docs/desert` | `worlds/desert/build` | dir |
| `world-build-docs/hal` | `worlds/hal/build` | dir |
| `world-build-docs/ijc` | `worlds/ijc/build` | dir |
| `world-build-docs/pahc` | `worlds/pahc/build` | dir |
| `world-build-docs/syr` | `worlds/syr/build` | dir |
| `CiC_W1_Phase5_RelationalSafety_Retest_Against_Proposed_Mechanism_DRAFT.md` | `worlds/pahc/CiC_W1_Phase5_RelationalSafety_Retest_Against_Proposed_Mechanism_DRAFT.md` | file |

Codes for the 4 non-registered "candidate" worlds (`gallic`, `lpc`, `latap`, `grkap`)
per Mark's own P6 ruling, 2026-09-14 — moved on the same basis as the 8 already-registered
worlds even though they have no `records/worlds/<code>.yaml` entry yet.

### Deliberately not moved: six worlds still awaiting a registry code

`World-Builds/Anabaptist-Movements`, `World-Builds/Lollardy`,
`World-Builds/Lutheran-Wittenberg`, `World-Builds/Reformed-Zurich-and-Geneva`,
`World-Builds/Society-of-Jesus`, `World-Builds/Tridentine-Church` — each at Step 0
only, added to `World-Builds/` after this manifest was staged, with no Mark ruling
assigning a short code. Moving them now would mean renaming a second time once a real
code exists, the same churn this whole phase exists to avoid elsewhere. `World-Builds/`
and `world-build-docs/` themselves therefore stay live roots — `tools/retired_paths.txt`
retires only the twelve specific subdirectories that actually moved, not the roots.

### A stop-hook-caught mistake in this phase's own tooling, fixed before landing

`tools/rewrite_paths.py`'s generic `World-Builds`/`world-build-docs` → `worlds`
dir-prefix rule ran against `tools/check_paths_baseline.txt` itself, along with every
other text file — text-substituting stored baseline strings even for entries whose
*citing file* lives under `records/` (content intentionally never rewritten, per this
project's hash-chain rule). That desynced eight baseline entries from what their real,
untouched source files actually say, surfacing as a false "now resolves" — the same
false-positive shape a stale, git-ignored local build artifact has produced elsewhere
this session (a `packages/desert/2026-09-09T03-17-52Z/` directory this thread's own
`engine.m2.cli restore` calls had regenerated locally; not present in a clean checkout,
kept in the baseline rather than dropped). Fixed by writing the baseline fresh via
`check_paths.py --write-baseline`, diffing every line against the pre-move baseline
(not trusting either side blind, the phase-1 lesson this phase was already following),
and manually restoring the one genuinely-still-broken local-artifact entry the fresh
write itself could not distinguish from a real fix.

### One real, fixable citation found and corrected directly

`Ministry/Features/Tour-Experience-Module-Phase2/CiC_L4_Tour_Manifest_Template_V1_0.md`
already cited `worlds/Imperial-Juridical-Christianity/Review-Artifacts/Doc09_Round1_Review.md`
— anticipating the `worlds/` convention before it existed, but with the long world name
instead of its registry code. Corrected in place to `worlds/ijc/...` (mechanical,
per this project's own default-actions rule for CI/path fixes).

### Not rewritten by design (phase 2, in addition to phase 1's own list)

- Prose in `records/`, `records/WORLDS_REGISTRY_LOG.md`, and dated Ministry documents
  that names a moved `World-Builds/...` path as history (what a source record cites,
  what a decision log describes as of its own date) — baselined, same convention as
  phase 1.
- Genuine false positives from `worlds` now being a real top-level directory name: two
  short passages of ordinary English ("What this world transmits to subsequent
  worlds/history…" in `don`/`ijc`/`lpc`'s own Doc_01 files) and a handful of dated
  audit entries describing an intentionally non-existent `worlds/Alexandria/` path
  (`CiC_Cleaning_Pattern_Log.md`, `desert`'s own Doc_03 review) — all baselined, not
  edited, since editing them would falsify what they correctly say.

---

## Housekeeping — Ministry tree triage — 2026-09-21 — PR branch `housekeeping/ministry-archive-2026-09-21`

Mark's tech-review stress test (thread "CiC — Tech Review & Funding Readiness Prep") identified all early-days strategy drafts (prior to 2026-08-20 system redesign) as superseded material. Files moved per Mark's one-at-a-time review: six categories decided, three document types with special handling, tracked below. Convention: files moved to `Archive/Ministry-Early-Days-2026-07/` preserving the Ministry subpath structure (e.g., `Ministry/Funding/FILE` → `Archive/Ministry-Early-Days-2026-07/Funding/FILE`), except Hosted-Tour which goes beside existing archive at `Archive/Tour-Experience-Module-Phase2/Hosted-Tour-Phase1/`.

**Category A. Move to Archive (90 files + folders)**

| from | to | kind | count |
|---|---|---|---|
| `Ministry/Funding/CiC_Ministry_Funding_Strategy_v1_0.docx` | `Archive/Ministry-Early-Days-2026-07/Funding/CiC_Ministry_Funding_Strategy_v1_0.docx` | file | 13 |
| `Ministry/Funding/CiC_Org_Funding_Bridge_Memo_V0_1_DRAFT.docx` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_Org_Funding_Strategy_Scoping_2026-07-07.md` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_OrgFunding_Thread_Launch_2026-07-07.md` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_Church_Designated_Fund_OnePager_V0_1_DRAFT.docx` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_World_Sponsorship_OnePager_V0_1_DRAFT.docx` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_Wabash_Pilot_OnePager_V0_1_DRAFT.docx` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_Seminary_Alignment_Analysis_V0_1_DRAFT.docx` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_Growth_Plan_V0_1_DRAFT.docx` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_Ministry_Proposal_Packet_V0_1_DRAFT.docx` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_BuildApproach_Budget_Proposals_V1_0.xlsx` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_Phase1_Budget_V0_1_DRAFT.xlsx` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Funding/CiC_Funding_Docs_Brand_Alignment_Change_Log_2026-07-18.md` | `Archive/Ministry-Early-Days-2026-07/Funding/...` | file | |
| `Ministry/Marketplace/*` (3 files) | `Archive/Ministry-Early-Days-2026-07/Marketplace/` | files | 3 |
| `Ministry/Organization/*` (7 files; see byte check below) | `Archive/Ministry-Early-Days-2026-07/Organization/` | files | 7 |
| `Ministry/Scholarly-Review/*` (6 files; V0_2 kept) | `Archive/Ministry-Early-Days-2026-07/Scholarly-Review/` | files | 6 |
| `Ministry/Features/Funding-Strategy/*` (4 files) | `Archive/Ministry-Early-Days-2026-07/Features/Funding-Strategy/` | files | 4 |
| `Ministry/Features/Website/*` (3 files; Decision-Log.md and README.md kept; note: 3 files not found) | `Archive/Ministry-Early-Days-2026-07/Features/Website/` | files | 0 |
| `Ministry/Features/Increment-1-Build/` | `Archive/Ministry-Early-Days-2026-07/Features/Increment-1-Build/` | dir | 3 |
| `Ministry/Features/Level2-Mobile-Popover/` | `Archive/Ministry-Early-Days-2026-07/Features/Level2-Mobile-Popover/` | dir | 3 |
| `Ministry/Features/Hosted-Tour/` | `Archive/Tour-Experience-Module-Phase2/Hosted-Tour-Phase1/` | dir | 4 |
| `Ministry/Features/Prototype-Testing/CiC_Prototype_Testing_Pilot_Plan_DRAFT_V0_1.md` | `Archive/Ministry-Early-Days-2026-07/Features/Prototype-Testing/...` | file | 1 |
| `Ministry/Operations/Standing/Launch-Prompts/*` (33 files; 5 kept: launched 2026-09-16 or later, or with 2026-09-21+ date) | `Archive/Ministry-Early-Days-2026-07/Operations/Standing/Launch-Prompts/` | files | 33 |
| `Ministry/Operations/Markup-Queue/` | `Archive/Ministry-Early-Days-2026-07/Operations/Markup-Queue/` | dir | 3 |
| `Ministry/Communication/*` (19 files; 6 kept: live kit and decision logs) | `Archive/Ministry-Early-Days-2026-07/Communication/` | files | 19 |

**Total Category A: 90 files and 4 directories moved.**

**Byte check (Category A, PDF uniqueness test):**

| pair | result | detail |
|---|---|---|
| `Faithways_Studio_Bylaws_and_Resolutions_SIGNABLE.pdf` vs `Faithways_Studio_Bylaws_and_Organizational_Resolutions_SIGNABLE_2026-07-27.pdf` | DIFFERENT | 104028 vs 8214 bytes |
| `Faithways_Studio_IP_Assignment_Agreement_SIGNABLE.pdf` vs `Faithways_Studio_IP_Assignment_Agreement_SIGNABLE_2026-07-27.pdf` | DIFFERENT | 95421 vs 5846 bytes |
| `Faithways_Studio_Shareholder_Agreement_SIGNABLE.pdf` vs `Faithways_Studio_Shareholder_Agreement_SIGNABLE_2026-07-27.pdf` | DIFFERENT | 70784 vs 5235 bytes |

**Decision:** per instructions "when in doubt leave it," the undated versions were not moved; both versions stay in place as originals.

**Files not found (expected, already archived or renamed):**

- `Ministry/Features/Website/CiC_Website_Alexandria_Status_Fix_Thread_Launch_2026-07-20.md`
- `Ministry/Features/Website/CiC_Website_Simple_Landing_Thread_Launch_2026-07-24.md`
- `Ministry/Features/Website/CiC_Website_Thread_Launch_2026-07-19.md`

**Category B. Supersession banners added (5 files kept in place):**

| file | banner | location |
|---|---|---|
| `CiC_Go_Live_Cost_Model_V0_1.md` | "Superseded 2026-08-24..." | `Ministry/Funding/` |
| `CiC_LLM_Provider_Cost_Options_2026-08-09.md` | "Premised on the retired cic-poc..." | `Ministry/Technology/` |
| `CiC_Business_Roadmap_V0_1.md` | "Partly superseded..." | `Ministry/Features/Funding-Strategy/` |
| `CiC_Cost_Study_Per_Transaction_V0_1.md` | "cic-poc measurement..." | `Ministry/Features/Funding-Strategy/` |
| `CiC_Cost_Reduction_Feasibility_Study_V0_1.md` | "cic-poc; Answer Bank recommendation..." | `Ministry/Features/Funding-Strategy/` |

**Category C. Small edits (5 tasks):**

- **C1:** Created `Ministry/Communication/README.md` with standing-status notice for FAQ and Letter-to-Friends docx files (python-docx unavailable; fallback per instructions).
- **C2:** Extracted Organizational Covenant for "always-free core access" sentence — text searched, phrase not found in extracted XML; noted in PR description. Covenant remains in place; roadmap already references this as an open task (line 54).
- **C3:** Updated `Ministry/Features/README.md` to annotate Hosted-Tour, Increment-1-Build, Level2-Mobile-Popover archive moves.
- **C4:** Appended 2026-09-21 decision log entry to `Ministry/Funding/CiC_Org_Funding_Decision_Log.md` (tech-review verdict, entity supplement exploration, tech-readiness program dispatch).
- **C5:** This ledger entry; added tracking file entry; updated `Ministry/Operations/README.md` to note Markup-Queue archived 2026-09-21.

**Path check:**

`python3 tools/check_paths.py --baseline tools/check_paths_baseline.txt`: 0 new unresolved citations, 0 retired paths present. Executed without --baseline first to gather the delta; all 90 moves produced citations within the expected Ministry/Operations audit and decision-log files describing them. Baseline regenerated with `--regenerate` after verifying all are Ministry-internal prose references or file-move audit records.

## 2026-09-24 — Live-Surface-Cleanup, witt PR: `records/WORLDS_REGISTRY_LOG.md` out of `records/`

| from | to | kind |
|---|---|---|
| `records/WORLDS_REGISTRY_LOG.md` | `Ministry/Operations/Standing/WORLDS_REGISTRY_LOG.md` | file |

CLAUDE.md's "Keep the live/canonical surfaces clean" names `records/` as a live surface holding only current, compiled content — no decision logs. This file is itself a decision log (world-registry rulings and provenance), already recognized as such by its own header ("this file holds why it says what it says") and by `tools/check_live_commentary.py`'s `PROTECTED_REGISTRY_LOG` exemption, which treats it as already the registry's own designated decision-log rather than a fresh finding. Moved via `git mv` in the Live-Surface-Cleanup program's first (witt) PR, per that program's own launch brief. Root `README.md`'s `Ministry/` row and `records/` row checked; `Ministry/` row updated to name the new location.

## Build Process version rename — 2026-09-25

Citations rewritten in current documents outside `worlds/`, `records/` and `engine/`
(3 replacements in 2 files, plus the check-paths baseline). See
`Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md`, 2026-09-25 entry.

| from | to | kind |
|---|---|---|
| `reference/method/CiC_Record_Native_World_Build_Process_V1.5.md` | `reference/method/CiC_Record_Native_World_Build_Process_V1.7.md` | file |

## 2026-09-26 — Live/Build split

`reference/`, `Ministry/`, `worlds/`, `World-Builds/`, and the building-tools subset of
`tools/` moved under a new top-level `Build/`, one manifest row per immediate child
directory (following the same nested-path convention as the phase 1/2 manifests — not a
bare top-level rule; the table below is the full mapping, kind by kind). The raw manifest
itself (and the phase 1/2 manifests) is deleted, not kept — a pure record of an
already-executed move, fully redundant with this table. Narrative, the `check_paths.py`
bug found and fixed, and the tools-with-root-detection fixes:
`Build/Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md`, 2026-09-26 entry.

| from | to | kind |
|---|---|---|
| `reference/` (15 children) | `Build/reference/` | dir |
| `Ministry/` (8 children) | `Build/Ministry/` | dir |
| `worlds/` (15 children) | `Build/worlds/` | dir |
| `World-Builds/` (6 children) | `Build/World-Builds/` | dir |
| `tools/` (12 files, zero CI references) | `Build/tools/` | file (×12) |
