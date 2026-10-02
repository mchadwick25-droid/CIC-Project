Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Reviewer agent: round-2 recheck subagent, Opus 5.5 at medium effort, fresh context, independent of every drafting and revising agent, session_01L5xhWKCzK96CZGy1fPzqGp
Drafter agent: Process V2.0 drafting and revision agents (the main thread and its Sonnet 5.5 subagents), session_01L5xhWKCzK96CZGy1fPzqGp
Round: 2
Truncation check, method 1: direct Read of Process V2.0 (all 1481 lines) and Standard V1.4 (all 231 lines) end to end, plus the final lines of the launch prompt, the six vendored skills and the eight changed L4 templates. V2.0 ends in Appendix B on "`quote.license` is `verbatim`, `paraphrase-only` or `do-not-voice`." V1.4 ends in Section F on "Doc_05 and Doc_07 carry this spine." The launch prompt ends "Mark decides Frozen status." The build-cycle skill ends "...say so plainly to Mark instead of forcing the cycle." Every file ends on a finished sentence, table row or YAML key.
Truncation check, method 2: bash at commit 07245847. `wc -l` gives V2.0 1481, V1.4 231, launch prompt 240, skills 150/43/53/49/42/93, matching method 1. `tail -c1` is a newline on all nine prose files. `grep -c '^## '` gives 16 in V2.0, which is Sections 0 to 13 plus Appendices A and B. Every "Section N" cross-reference (0-6 and 8-13) resolves to a heading. The state-file template parses with `yaml.safe_load` (16 keys, last `freeze_package_pointer`). md5 prefixes: V2.0 6c70f46e7d73, V1.4 60708457699e, launch prompt b32d69ff6c50. Changed modules pass `python -m py_compile`: engine/m10/*.py, engine/m2/profile.py, builders.py, cli.py, engine/m1/schemas.py, gates.py, registry.py and engine/m7/turn_readability.py.

# Review of Build Process V2.0, Completion Standard V1.4, the launch prompt, skills, templates and the gate layer: round 2 targeted recheck

Verdict: SUBSTANTIAL FINDINGS. Most of the round-1 work is closed, and closed well. Eleven substantial findings remain. Three carry over from round 1. Eight are new: seven are places where a document disagrees with the code, and one is a converged resolution that was not applied. None is a fabrication or a safety fail-open. This is round 2 of at most 3.

Scope: the work at commit 07245847, measured against the four round-1 files in this folder, the converged spec of 2026-09-29, and Mark's later acceptance of T22, T5 and the four trigger definitions. Read-only runs were made against `cappadocian`, and against `fix` where state mattered. Fixtures were built under a temp directory by a scratch script (47 expectations, all held). No repository file other than this one was edited.

## 1. Closure table

Status key: CLOSED (with file:line evidence), PARTIAL, OPEN.

### 1a. V2.0_and_Standard_V1.4_Review_Round1.md

| # | Finding | Status | Evidence |
|---|---|---|---|
| 1 | Lean single-trial vs CF's two-trial rule | PARTIAL | V2.0:23-26 and V1.4:9-11 now rest on the CF deferring freeze detail to the Standard. V2.0:1101-1102 declares the lost second trial. But the CF itself (V7.4 docx, Representative-freeze paragraph, which this branch repointed from V1.0 to V1.4) says §C of V1.4 "specifies" Part Eight "under the Validation Protocol Rigor discipline" plus "the Table Readiness Round passed". V1.4 §C (147-168) specifies neither for a lean freeze. See finding G. |
| 2 | Session rules said to be "in full" but missing five rules | CLOSED | V2.0:1263-1270 (sample-based re-run), 1271-1274 (`Touches:` diff check), 1276-1279 (done means committed and re-runs green), 1297-1299 (cosmetic), 1319-1324 (direct read wins, and a dismissal needs confirmation). |
| 3 | Two triggers not checkable in code | PARTIAL | Code closed: `engine/m10/validation.py:276-317` implements all four accepted definitions. The documents still read as placeholders (V2.0:1070-1076, 1402-1403). See finding A. |
| 4 | Three CI behaviours claimed as live | CLOSED | `.github/workflows/ci.yml:294` (`--enforce`), 335-353 (library validators), 302-329 and 171-172 (world gates on drafts). |
| 5 | `world_core` fields that do not exist | CLOSED | V1.4:23 names `time_window`, `horizon`, `formation_logic`, `thinness` and `cautions`, with gravities resolving by `world_id`. `pairing_guidance` sits on `facilitator_brief` (V1.4:32). `integrative_observation` is now in the schema (`engine/m1/schemas.py:390`). The inhabited-voice text is an open item (V2.0:1407-1408). |
| 6 | Commentary in V2.0 and V1.4 | CLOSED | The dated rulings, the R6 history and the "[V1.x]" tags are gone, and V1.4:3-7 is a plain status line. Two unflagged "earlier versions" phrases remain as minor items (section 3). |
| 7 | Deep Interview actor and deployment | CLOSED | V2.0:919-931 and 1008-1012: the build thread deploys to `cic-engine-staging` and runs the interview after Mark approves the paid sample. The smoke test sits in Phase D. |
| 8 | B-8 two-trial dropped without a decision | PARTIAL | V2.0:833 now reads "Two trials when the world is on full validation. One trial on the lean path." No decision records this. The decision log entry (`CiC_System_Hub_Decision_Log.md:5599-5684`) does not mention B-8. See finding H. |
| 9 (minor) | Readability of instruction passages | CLOSED | V2.0:3-9 and 937-940 are split into short sentences. |
| 10 (minor) | Vendored skills path not named | CLOSED | V2.0:48-50. |
| cross-check | Handoff manifest path; header comma; ceiling logged | CLOSED | The `handoff` run on cappadocian looks in `build/` (`handoff-12-manifest: Build/worlds/cappadocian/build/...`). The template and `reviewfile.py:17-18` both use "Truncation check, method 1". The ceiling is logged at decision log:5651. |

### 1b. Launch_Templates_Skills_Review_Round1.md

| # | Finding | Status | Evidence |
|---|---|---|---|
| 1 | Launch prompt cites V1.3 | CLOSED | Launch prompt:11. |
| 2 | Launch prompt forbids commits | CLOSED | Launch prompt:217, "Commit at each green checkpoint, with the step ID. Push only on Mark's word." |
| 3 | "Seven gates" | CLOSED | `cic-validation-suite/SKILL.md:22`, "the full M1 gate battery ... at zero". |
| 4 | Dynamic Encounter Validation unscheduled | CLOSED | Encounter-Success grading is on the Deep Interview (V2.0:1021-1028; validation skill review list; Probe Result template rule). |
| 5 | Dated inline note in world files | CLOSED | `cic-build-cycle/SKILL.md:146`: the correction is logged in the Ministry decision log, never in the world file. |
| 6 | Pre-draft check needs a Mark disposition | CLOSED | `cic-build-cycle/SKILL.md:48`. |
| 7 | Ledger and state file lack V2.0 items | CLOSED | Cost ledger template:20 and 36 (effort and `/usage` before and after, per document and per round); state file template:3 `completion_standard_version`. |
| 8 | Gravity skill narrows candidates to Doc_02 | CLOSED | `cic-gravity-index/SKILL.md:22`, "Doc_02 and/or Doc_03". |
| note | R27 and R41 rows in V2.0 misstate the rulings | OPEN | V2.0:870 still states R27 at sentence level, but R27-A moved the unit to the paragraph. V2.0:873 still says "The Facilitator explains the modern sense". See finding F. R36 and R38 are now carried in the validation skill (:42). |

### 1c. Gate_Layer_Code_Review_Round1.md

| # | Finding | Status | Evidence |
|---|---|---|---|
| 1 | "Not Approved to proceed" read as cleared | CLOSED | `handoff.py:23` `NEGATIVE_VERDICT`, and :164. |
| 2 | An invented quote exempts itself through a second document | CLOSED | `quotes.py:207-226` excludes the whole world folder and its dossier. Exemptions are always notes (:306). |
| 3 | `--skip-quotes` exits 0 | CLOSED | `common.py:36-39` and :56 `passed` (the incomplete flag); `handoff --help`, "exits non-zero as incomplete". |
| 4 | Unnormalized reviewer and drafter comparison | CLOSED | `reviewfile.py:38-44` `model_id`, and :99-106 separate agent fields. |
| 5 | Trigger detector prints `lean` when it cannot evaluate | CLOSED | `validation.py:320-323` and :490. Fixtures: a missing or non-boolean `safety_adjacent`, no Primary gravity, or a graded row with no Fabrication value each give `undetermined`. On cappadocian the run prints `undetermined` and exits 1. |
| 6 | m1 cross-world waivers unchecked | CLOSED | `regate.py:231-254`, called from `run_regate` (:218) and `run_records` (:287). |
| 7 | `records` fails every non-admitted world | CLOSED | `regate.py:265-286`. `records fix` passes with a note; `records fix --freeze` fails on the missing `facilitator_brief` and site JSON. The documents do not say `--freeze`; see finding C. |
| 8 | `live-commentary --enforce` fails this PR | OPEN | Re-run: `check_live_commentary.py --base 7521c09a --enforce` exits 1. It finds 288 REWRITE or ROUTE lines in 16 reference files this branch edits, plus 3 ROUTE lines in `Build/worlds/_cross-world/SOURCE-READINESS.md`. See finding I and section 5. |
| 9 | Per-turn readability never called | CLOSED | `validation.py:29`, 138-151 and 206-210. CLAUDE.md:23 now cites `engine/m7/turn_readability.py`. |
| 10 | `citations <code>` does not run | CLOSED | `deployed.py:548` and 562 default to the build documents and probe files. `probes` runs the label check (:565-567). On cappadocian, `citations` runs and exits 1 with 3 real findings. |
| 11 | Loader guard refuses the local cache layout | CLOSED | `deployed.py:89` accepts any `packages/<code>/<pin>/compiled/prompt.txt`, including `packages/packages/...`. |
| 12 (minor) | List insertion fails untouched items | CLOSED | `regate.py:170-178` matches by the base's text set. |
| 13 (minor) | Living-tradition flag without text is only a note | CLOSED | `deployed.py:265-270`: a note for grandfathered worlds, a finding for new ones. |
| 14 (minor) | Known-failing Library test not registered | CLOSED | `ci.yml:355-360`; `CiC_System_Health_Tracking.md:1407`. |

### 1d. Preservation_Audit_Round1.md: the 22 items marked worth restoring

| Item | Status | Evidence |
|---|---|---|
| S18 prior partial build | CLOSED | V2.0:416-419 |
| S19 Doc_03 from Native rows | CLOSED | V2.0:469-471, 479 |
| R19 coach verification | CLOSED | V2.0:1371-1377; build-cycle skill:140-142 |
| R31 claims register as a halting control | CLOSED | `engine/m10/claims.py`; V2.0:287, 489-518. Fixtures: an unregistered claim fails, a registered one passes, a stale entry fails. |
| R32 independent propagation sweep | CLOSED | V2.0:529-533 |
| R33 one state during review | CLOSED | V2.0:534-535 and 1344-1345 |
| R35 structural locators | CLOSED | V2.0:525-528; `quotes.py:242-259` (fixtures: inside the division passes, outside fails, an unknown locus fails, no address is not checked) |
| R37 Record Integrity | PARTIAL | `engine/m10/integrity.py` checks open items, superseded files and stated counts (fixtures pass and fail). Its fourth part, "the deployed artifact holds what was applied", only re-runs `deployed`'s fixed item set (`integrity.py:107`). See finding E. |
| V8 approved-source anchoring | CLOSED | `schemas.py:639-643`; `builders.py:327` and 471; `deployed.py:219-249`. Six fixtures pass and fail as documented. |
| V22 World Profile | CLOSED | `engine/m2/profile.py`. It is deterministic, invents nothing, and reads INCOMPLETE honestly (the cappadocian run leaves Sections 4 and 10 not carried). |
| F9 safety trigger fails open | CLOSED | `validation.py:299-303` and 490 |
| F13 absent voices in the brief | CLOSED | V2.0:831 |
| T3 Part Eight coverage | CLOSED | V2.0:988-1005; V1.4:128-132; `validation.py:224-232` |
| T5 Encounter-Success (accepted by Mark) | CLOSED | V2.0:1021-1028; V1.4:154-158; `validation.py:233-244`; Probe Result template rule |
| T16 validation belongs to the pin | CLOSED | V2.0:969-975; `validation.py:248-257`; `deployed.py:462-496`. A minor looseness is noted in section 3. |
| T20 a thread may raise the level | CLOSED | V2.0:1084-1087 |
| T22 Ecological Integrity and Differentiation (accepted by Mark) | CLOSED | V2.0:590, 1165-1173; V1.4:49-55; attestation template:51-71 |
| G9 reasoned decisions | CLOSED | V2.0:1280-1282 |
| O7 one story | CLOSED | V2.0:1346-1348 |
| O12 halt, never thin | CLOSED | V2.0:1220-1224; launch prompt:185 |
| O18 fetch first, one thread per world | CLOSED | V2.0:413-416 and 1258-1262 |
| Z13 System Hub summary | CLOSED | Launch prompt:238-239 |

### 1e. The 12 practices worth codifying

| # | Practice | Status | Evidence |
|---|---|---|---|
| 1 | Halting claims register | CLOSED | as R31 |
| 2 | Outward-sweeping propagation check | CLOSED | V2.0:529-533 |
| 3 | One state during review | CLOSED | V2.0:1344-1345 |
| 4 | Structural locators | CLOSED | V2.0:525-528 |
| 5 | Fetch first, one thread per world | CLOSED | V2.0:1258-1262 |
| 6 | The don and rzg Validation Layer shape | CLOSED | Attestation template, Sections 2 and 5 ("Named, not skipped"; "Freeze criteria not met") |
| 7 | Validation on the current pin | CLOSED | as T16 |
| 8 | Neighbour re-confirms differentiation | CLOSED | V2.0:459-461; attestation template:67 |
| 9 | Fleet visual collision check at M1 | CLOSED | V2.0:163-166 |
| 10 | Read the deployed prompt before probing | CLOSED | V2.0:962-967 |
| 11 | Answer-the-Canon pass | CLOSED | V2.0:832 (B-7b) |
| 12 | Escalate a returning defect class | CLOSED | V2.0:1349-1352 |

### 1f. The 14 contradictions

| # | Contradiction | Status | Evidence |
|---|---|---|---|
| 1 | Part Eight coverage | CLOSED | V2.0:988-1005; `validation.py:224-232` |
| 2 | Probe result shape | CLOSED | Probe Result template, last rule; validation skill:64-68 (the attestation matrix carries scenario, criteria and indicators) |
| 3 | Register-Fidelity | CLOSED | Doc_10 template:540-542 and 762-765 call it a Part Five construction check |
| 4 | Where the Deep Interview runs | CLOSED | V1.4:154-155 and V2.0:1008 both say `cic-engine-staging` |
| 5 | CF freeze criteria nothing met | CLOSED | V2.0:1165-1173 |
| 6 | Field names the schema lacks | CLOSED | V2.0:828, 1411-1430; V1.4:26-31, 35-38 |
| 7 | World Profile | CLOSED | as V22 |
| 8 | Claims-register trigger | CLOSED | V2.0:489-492; build-cycle skill:52 |
| 9 | What the round counter counts | CLOSED | V2.0:286 and 1302-1306; `rounds.py:21-47` |
| 10 | Freeze package in the launch prompt | CLOSED | Launch prompt:220-236 |
| 11 | Skills not in the read list | CLOSED | Launch prompt:19-20 |
| 12 | Missing input as a stop | CLOSED | V2.0:203 |
| 13 | Label punctuation | CLOSED | V2.0:1316; launch prompt:122; build-cycle skill:79 |
| 14 | ARSP routes the largest passes to Fable | PARTIAL | ARSP:33 is fixed. ARSP:5 still reads "Opus for a deep pass, Fable for the largest comprehensive ones", against V2.0 §2. Minimal fix: delete that parenthetical. |

**Counts (80 items):** 74 CLOSED, 5 PARTIAL (V2.0 R1-1, R1-3 and R1-8; preservation R37; contradiction 14), 1 OPEN (gate R1-8). One further OPEN note carries forward from the launch review: the R27 and R41 rows.

## 2. Doc-vs-code agreement, subcommand by subcommand

Each was checked with `--help`, by reading the code, and, where safe, by a read-only run on cappadocian (and on `fix` for `records`).

| Subcommand | Agrees? | Run and notes |
|---|---|---|
| `handoff` | Partly | Exit 1 on cappadocian (a built world with no manifest; expected). The locus check runs and matches V2.0:283. **Check 1 also fails a non-grandfathered world whose registry entry has no boolean `safety_adjacent` (`handoff.py:180-182`). V2.0 §4 item 1, the manifest template and the launch prompt never say so** (finding A). |
| `prereview` | **No** | The documented form, `prereview <code> <document>` (V2.0:284 and 806; launch prompt:86), exits 2 with "unrecognized arguments". The code takes `--doc <int>` (`prereview.py:83`); `--doc Doc_04` also exits 2 (finding B). |
| `roundcount` | **No** | The documented form, `roundcount <code> <document>` (V2.0:286; launch prompt:88), exits 2 with Doc_04 ("invalid int value"). The code needs a number. Without `--check-new --round N` it does not block a fourth file: a fixture with three round files returns no finding, and only `--check-new` blocks (finding B). |
| `reviewfile` | Yes | Label, seven fields, Opus id, agent independence, distinct methods, round matching the file name. This file passes it. |
| `gaps` | Yes | Exit 1 on cappadocian, 41 unmatched open items (real legacy debt). |
| `citations` | Yes | With no files it defaults to the top-level build documents and the probe files. Exit 1 on cappadocian with 3 real findings (a wrong namespace and an unknown id). |
| `claims` | Mostly | Exit 1 on cappadocian: 85 derived claims and no register. It has fourteen patterns, as V2.0:512 says. The gate-table example "only this world..." (V2.0:287) is not derived by any pattern (fixture). Minor; section 3. |
| `integrity` | **Overclaims** | Exit 1 on cappadocian: 41 open items, and two live versions each of the Construction Notes and the World Profile. The fourth part is `check_deployed` over its fixed item set. It does not read what any document says was applied (finding E). |
| `deployed` | Yes | PASS on cappadocian in about 2 minutes. The anchor is a note there, because cappadocian is grandfathered. Fixtures: 5 named entries verbatim in their own section pass. Four entries, an entry not named in the paragraph, a paragraph that is not verbatim, or a new world with no anchor each fail. |
| `probes` | Yes | PASS on cappadocian. It runs the pin checks and the label checks. |
| `validation` | Yes | Exit 1 on cappadocian. The verdict is `undetermined` (no `safety_adjacent`; 14 graded rows with no Fabrication value), all 8 categories are missing, and the legacy table lacks columns. Fixtures cover all four triggers, "Primary only", coverage, every encounter condition, and the current pin. |
| `wiring` | Yes | PASS on cappadocian. It uses a scripted client, with no network. |
| `records` | **Partly** | V2.0:292 runs `records <code>` "at freeze". Without `--freeze` a world in state `built` is not asked for `world_front`, `facilitator_brief` or the site JSON: `records fix` exits 0 and `records fix --freeze` exits 1 (finding C). |
| `regate` | Yes | PASS on cappadocian (4 edited fields graded; 210 carried-over failures noted, not failed). Waiver checks are included. |
| `engine.m2.cli profile` | Yes | Exit 0 on cappadocian. The status line reads INCOMPLETE (Sections 4 and 10), as V2.0:298 and 588 say. |

Fleet byte-identity: `python -m engine.m2.cli staleness-check` gives `"pass": true`, with 12 worlds and none stale. The anchor and `integrative_observation` additions change no existing package.

## 3. Findings

### Substantial

**A. The accepted trigger definitions are in the code but not in the documents, and the `safety_adjacent` field is required but undocumented.**
- **Where:** V2.0:1070-1076 still reads "defined by: project lead, before the pilot" three times. V2.0:1402-1403 lists the definitions as owed by Mark. V1.4:182 points to those placeholders. V2.0:1078-1080 gives "a definition is still a placeholder" as a live cause of `undetermined`.
- **What the code does:** `validation.py:279-282` implements the four definitions Mark accepted: a Primary gravity tagged Inferential-Thin; a Primary gravity whose own tag is Contested; the registry field `safety_adjacent: true`; and a Fabrication column value of `yes`. `handoff.py:180-182` fails a new world without the boolean field.
- **The gap:** no document tells Mark, who creates the registry entry (V2.0:12), to set it. That covers V2.0 §4 item 1, `World_Build_Handoff_Manifest_Template.md` and the launch prompt. The decision log (:5653-5657) still says "Proposed ... not yet answered".
- **Minimal fix:** replace V2.0:1070-1076 with the four definitions, worded as `validation.py:279-282` words them. Delete the §13 item. Add to V2.0 §4 item 1: "The registry entry carries `safety_adjacent: true` or `false`, set by Mark." Add a line to the handoff manifest template and the launch prompt. Append a decision-log entry recording Mark's acceptance of the trigger definitions, T22 and T5.

**B. `prereview` and `roundcount` do not run as documented, and `roundcount` blocks a fourth file only with a flag the documents never give.**
- **Where:** V2.0:284, 286 and 806; launch prompt:86 and 88. Proof is in section 2.
- **Minimal fix:** document `prereview <code> [--doc N]` and `roundcount <code> N --check-new --round R`, where N is the document number (0 for Step 0). Say that only `--check-new` blocks. (Changing the code to accept `Doc_04` is the alternative. That is a gate change, so it belongs to a session that is not also bound by the gate.)

**C. `records <code>` "at freeze" passes a world that lacks the required record types.**
- **Where:** V2.0:292; launch prompt:98.
- **Proof:** `records fix` exits 0 and `records fix --freeze` exits 1. A world is admitted only after freeze (V2.0:913), so at freeze it is in state `built`.
- **Minimal fix:** V2.0:292's freeze case and the freeze package use `records <code> --freeze`.

**D. V2.0 B-7 says the readability gate does not read `source_anchor`. It does.**
- **Where:** V2.0:830, "The readability gate does not read `source_anchor`, so the reviewer reads it against the FK grade 10 limit."
- **The code:** `engine/m1/spoken_fields.py:91` declares `source_anchor` an instruction field. `gate_readability` (via `_readability_checks`, `gates.py:507-532`) and `regate` (`regate.py:79`) therefore grade it. `voice_craft_prompt_parts` counts it in the budget (`gates.py:696`).
- **Fixture:** a dense `source_anchor` gives "source_anchor scores FK grade 41.6, above the ceiling of 10".
- **Minimal fix:** "`gate_readability` grades it like the other four fields." (Section 4 below has the question as asked.)

**E. The Record Integrity check claims to verify "what was applied". It re-runs `deployed`.**
- **Where:** V2.0:297 and 1157-1160, and V1.4:109-115 by reference; `integrity.py:8-10` docstring ("a fix described as applied is found there or is a finding").
- **The code:** `integrity.py:107` calls `check_deployed`. That checks only the confirmed `world_core` items, the self-reference hardening, the quote and gravity indexes, the counts and the anchor. Nothing reads a review's or a document's "applied" statements.
- **Minimal fix:** reword the fourth part as "`deployed` passes at the pinned package (confirmed items, rule counts, source anchor)". Add "each fix a document calls applied is found in the deployed artifact" to the reviewer's parts, both at V2.0:1160-1163 and in the §13 list of checks with no script. Correct the docstring to match.

**F. Two rows of the runtime-rulings table misstate the rulings, and the skills now contradict V2.0.**
- **R41:** V2.0:873 says "The Facilitator explains the modern sense." `Rulings-Pending.md:536-537` moves that sense "out of a spoken turn entirely, into the term's hover card". The lexicon skill (:26) and the validation skill (:43) already say so.
- **R27:** V2.0:870 states the rule at sentence level. R27-A moved the unit to the paragraph (validation skill:42).
- **Minimal fix:** R41: "It never defines the modern word. The modern sense sits on the term's hover card, in no one's voice." R27: "Every paragraph of a voice turn carries a citation, except ..." Optional: add R37-A's time-window test to the R37 row.

**G. (carried over from R1-1) The governing CF describes Standard §C as the two-trial rule plus the Table Readiness Round.**
- **What conflicts:** V2.0 ranks the CF first. The CF's Representative-freeze paragraph says the freeze runs "as the governing Completion Standard V1.4 section C specifies: ... under the Validation Protocol Rigor discipline above ... and the Table Readiness Round passed". V1.4 §C makes lean single-trial without the Table Readiness Round the default.
- **Why it matters:** the "deferral" V2.0:23-26 relies on is contradicted by the CF's own summary of what it defers to. The branch touched this sentence (V1.0 to V1.4) and left the substance.
- **Minimal fix (Mark's call, a change order to a governing document):** CF paragraph: "run as the governing Completion Standard V1.4 section C specifies: lean by default; Validation Protocol Rigor in full and the Table Readiness Round when a full-validation trigger fires". Or apply round 1's plain sentence in V2.0 §8 and V1.4 §C: "Lean single-trial validation is a project-lead deviation from CF V7.4's two-trial Validation Protocol Rigor."

**H. (carried over from R1-8) B-8 probe parity became single-trial on the lean path with no recorded decision.**
- **Where:** V2.0:833 and V2.0:1092.
- **Why it matters:** the spec makes the Phase D probe set lean. It says nothing about B-8, a release gate for the record-native swap.
- **Minimal fix:** record Mark's decision in the Process V2.0 decision-log entry, or restore "two-trial" at B-8.

**I. (carried over from gate R1-8, OPEN) The blocking `live-commentary` job fails this pull request.**
- **Where:** 288 REWRITE or ROUTE lines in reference files this branch edits, plus 3 ROUTE lines in `SOURCE-READINESS.md`.
- **What they are:** mostly process vocabulary in method documents, which are false positives. Section 5 classifies them. It proposes a narrow rule that clears 202 of them and passes all 173 existing labelled tests. What remains is finding J's real commentary, plus 22 lines the tool's own tests say must stay flagged: bare ruling numbers such as "(R11)" and "(R26, R37)", and pointers such as `Decision-Log.md` and `Rulings-Pending.md`.
- **Minimal fix:** Mark decides the classifier rule (a governance change). Then drop the bare ruling numbers from V2.0:827, 830, 836, 857, 869-873, 880 and 1310, and from the lexicon and validation skills, keeping the rules. Also reword V2.0:1153 and 1269, V1.4:113, build-cycle skill:48 and `SOURCE-READINESS.md`:95-105. The remaining three are V2.0:166 and 864 (the `Decision-Log.md` and `Rulings-Pending.md` path pointers) and V2.0:1034 (a subject-and-date citation). Rewrite them, or extend the rule to keep a pointer inside a backticked path, which is Mark's call.

**J. Two canonical files this branch edits still carry real commentary (CLAUDE.md: a PR that edits a live file removes its commentary).**
- **ARSP:** edited at :33. It keeps 7 lines of review-history narration (section 5).
- **`CiC_Voice_Style_Guide_and_Scaling_Plan.md`:** edited at :988 and :1234 (two path repoints). It is a dated session report: "Written 2026-09-08 from the Chloe ... editorial pass", first-person "I found", branch names, shipped-status counts. §4.3 argues model routing from the superseded V1.9, against V2.0 §2. 58 of its 59 flagged lines are real.
- **Minimal fix:** clean the ARSP (section 5 gives the rewrites). For the Voice Style Guide, either strip the dated and attributed lines and delete §4.3, or move the file to `Build/Ministry/` as the analysis it is and keep only its style rules in reference. Moving it is a structural change, so ask Mark first, with a README and tracking entry. The third choice is to revert the two repoints, which would bring back broken paths.

**K. Resolution 3 ("M1/M2/M3 everywhere") is not applied in the Naming and Role Discipline.**
- **Where:** V2.0:153 makes that document the M1 rule, and it is on the launch prompt's read-first list (#6). It still says "the bar G2 applies everywhere" (:6), "This governs G2 in every launch prompt (V2 and V3 alike)" (:21), and uses G2 at :29 and :85 and G3 at :47.
- **Minimal fix:** G2 becomes M1, "V2 and V3 alike" is deleted, and G3 becomes the Register Bar reading. This is inside the converged decision, so auto mode applies.

### Minor (not blocking)

- V2.0:287 uses "only this world..." as an example of a derived claim. No pattern derives it (fixture). Use "the only surviving source..." instead.
- `pin_not_current` (`deployed.py:471-472`) passes a results file with no `Tested artifact` line if the current pin appears anywhere in it. A fixture that says "run against <old pin>; the current pin is now <new pin>" passes. The template requires the line, so consider requiring it in code at freeze.
- V2.0:1021-1022 says the fifth check "reads the whole transcript". The template and `validation.py:233-244` need the four conditions on every Deep Interview round row. Make the wording match: "on each round's row".
- V1.4:35-36 ("fields that earlier versions of this standard named") and V2.0:1411-1413 ("Earlier versions named these fields") are change-history phrasing. Say "fields the schema does not define yet".
- `gates.py:704-716` ("The four voice_craft fields ...") and `builders.py` ("The four voice_craft fields, together, above the line") are code comments that now miss `source_anchor`.
- The decision-log entry (:5663) says "The World Profile generated view is not built". It now is, so record that in the addendum from finding A.
- `citation_files` scans only the world folder's top-level files, so documents in `Representative/` are not covered by default.

## 4. The `voice_craft.source_anchor` question

The premise that the readability gate does not read `source_anchor` is no longer true, as finding D shows. The fix the question proposes is already in place, and done the right way: one declared registry drives both checks. `spoken_fields.py:91` registers the field, so `gate_readability` and `regate` grade it through `_readability_checks`. `voice_craft_prompt_parts` (`gates.py:696`) adds it to the 900-word budget. The budget and the FK gate therefore read the same five fields. No new code is needed.

The interim sentence in V2.0:830, "a reviewer reads it against FK 10", is not acceptable. It is not dangerous, since the reviewer only does extra work. But it is a false description of the gate, and a reader would conclude the gate has a hole it does not have. Replace it as finding D says.

## 5. Live-surface commentary in `Build/reference/method/*.md`, the skills and L4-Templates

`python tools/check_live_commentary.py --surface reference` flags 329 lines in this scope. I classify 75 of them as REAL: change history, dated narration, review narration, attribution or provenance stories. The other 254 are legitimate process vocabulary: "reviewer", "round 1", "open item", "unresolved tension", "at the freeze", "adversarial review", paragraph widening from "re-confirmation", and ruling numbers used as names. The unflagged REAL passages are V2.0:1411-1413, V1.4:35-36 and Naming:3-5.

### REAL lines and the minimal rewrite

| File:line | What it is | Minimal rewrite |
|---|---|---|
| ARSP:3 | Origin story with dated review references | "A standard practice for adversarial review of any document whose claims matter." |
| ARSP:13 (clause) | "round 1 found this at ~68/32 and named ..." | Keep the check. Replace the clause with "A heavy framing share predicts an excellent re-diagnosis with a thin design attached." |
| ARSP:17 (last sentence) | "Round 3 caught a fourth instance ..." | Delete the sentence. |
| ARSP:25, 26, 27, 29 | "Round 1: ... Round 2 ... Round 3 ..." history | Replace the section with one line: "It catches mechanism misattributions, fabricated composite quotes, claimed data that does not exist, clauses that invert their source, and misattributed statistics." |
| VSG:3 | "Written 2026-09-08, from the Chloe ... pass (commits ...)" | "Derived from the Chloe / Scattered Households editorial pass." Commits and date go to Ministry. |
| VSG:14, 102 | Session-transcript provenance of the companion analyses | Name the two companion files only. |
| VSG:42, 347, 370 | "Mark's ruling of 2026-08-30 ..."; "Mark's ruling, verbatim: ..." | State each rule plainly: no word-rule ledger; all text is brought to this standard; website copy only, never record files. |
| VSG:62 | "(measured, 2026-09-08)" | Drop the parenthetical. |
| VSG:178, 220, 274, 1220 | "in Mark's own words", "derived from Mark's own catches" | Drop the attribution and keep the rule. |
| VSG:504, 587, 890 | Shipped-status counts ("Still open across the Atlas ... 264 others", "123 entries still open ...", "Known display issue, not yet fixed") | Route to the Atlas prose tracker in Ministry. |
| VSG:619, 965 | Commit-row status ("Shipped. Mark's own plainer wording"; "per Mark's explicit instruction") | Keep the before-and-after example. Drop the status and attribution. |
| VSG:1154 | "(`gate_voice_perspective`, 2026-09-04). Reviews had not caught it." | "`gate_voice_perspective` now catches it." |
| VSG:1360 | "Mark's two most efficient contributions this session ..." | "Offer drafted options, not open questions." |
| VSG:1460 | "Branch ..., all 2026-09-08." | Delete. |
| VSG:1225-1310 (§4.3; flagged 1234, 1237-1241, 1247, 1277-1308) | Model-routing argument from superseded V1.9 and branch history, contradicting V2.0 §2 | Delete §4.3, or route it to Ministry. V2.0 §2 governs routing. |
| Register Bar:1 | "(2026-08-29, Mark's ruling)" | "# The Register Bar" |
| Register Bar:34-35 | "Added 2026-09-04 (Cross-System Analysis finding, not Mark's own words ...)" | Delete the provenance clause and keep the property. |
| Register Bar:52 | "(engine/m1/gates.py, added 2026-09-04)" | "(engine/m1/gates.py)" |
| Register Bar:69 | "(Mark, 2026-08-30: ...)" | Keep the quote as the stated standard, without the date. |
| Naming:3-6 | "Origin. Stated by Mark, live, while working the Donatism build thread ..." | "The standard, in Mark's words:" followed by the quote. |
| Facilitator_Brief_Backlog:5 | "During Phase One world-selection work (2026-07-04), ..." | "Participants will ask for things the architecture does not provide in the form they expect ..." The file is a living backlog, not a template, so route it to Ministry. |
| World_Facilitation_Brief_Template:17 | "(Mark, 2026-09-20)" | Drop the attribution. |
| World_Facilitation_Brief_Template:158 | Card-accuracy change note (v1.2, audit history) | Delete. The requirements already live in Section A. |
| World_Facilitation_Brief_Template:160 | "Generated-brief note (S6.1, 2026-07-27) ... no longer hand-authored ... cic-poc/backend/wrs/views/..." (also a dead path, resolution 7) | "For a record-native world this brief is a view over its `facilitator_brief` and `world_core` records." |
| V2.0:1411-1413; V1.4:35-36 | "earlier versions named" | See the minor list. |

Of these, the ARSP (7) and the Voice Style Guide (58) are files this branch edits, so finding J applies. The Register Bar, the Naming Discipline, the Backlog and the Facilitation Brief template are not edited here. Under CLAUDE.md's default for doc hygiene outside one's own thread, they are flagged, not touched.

### Proposed classifier rule for the reference surface

The rule is scoped like the `engine/m10` rule. It applies only to the governing build-method files: `Build/reference/method/CiC_Record_Native_World_Build_Process_V*.md`, `.../CiC_World_Build_Completion_Standard_V*.md`, `.../skills/*/SKILL.md` and `Build/reference/L4-Templates/*.md`. In those files, a REWRITE or ROUTE hit becomes KEEP when:
- every matched pattern is in {`reviewer`, `review-round`, `era-gate`, `route-cue`, `change-history-cue`, `change-history-block`, `marks-word`};
- any `marks-word` hit is only "Mark's word" or "Mark's call";
- the line has no history shape: a line starting "Round N:" or "Round N (", "round N found/caught/flagged", or "previously", "formerly", "no longer", "used to", "was changed" or "earlier version";
- the line has no status cue: TODO, FIXME, "not yet resolved/fixed", "still open/pending", "known gap/issue" or "has not yet been".

`iso-date`, `ruling-number`, `decision-log`, `rulings-pending`, `per-mark` and "Mark's ruling/own" are untouched.

```python
_METHOD_DOC = re.compile(
    r"^Build/reference/(?:method/(?:CiC_Record_Native_World_Build_Process_V[\d.]+|CiC_World_Build_Completion_Standard_V[\d.]+)\.md"
    r"|method/skills/[^/]+/SKILL\.md|L4-Templates/[^/]+\.md)$")
_METHOD_VOCAB = {"reviewer", "review-round", "era-gate", "route-cue", "change-history-cue", "change-history-block", "marks-word"}
_METHOD_HISTORY = re.compile(r"^\s*[-*]?\s*\**Round\s+\d+\**\s*[:(]|\bround\s+\d+\s+(?:found|caught|flagged|named)\b"
    r"|\b(?:previously|formerly|no longer|used to|was changed|were changed|earlier (?:draft|version)s?)\b", re.I)
_METHOD_STATUS = re.compile(r"\b(?:TODO|FIXME|not yet (?:resolved|fixed|answered|acquired)|still (?:pending|open)"
    r"|known (?:gap|issue|defect)|has not yet (?:been|done))\b", re.I)
_MARKS_ROLE = re.compile(r"\bMark'?s\s+(?:word|call)\b", re.I)

def _method_vocabulary_category(rel, line, matched, category):
    if category not in BLOCKING_CATEGORIES or not _METHOD_DOC.match(rel.as_posix()):
        return category
    if not set(matched) <= _METHOD_VOCAB:
        return category
    if "marks-word" in matched and not _MARKS_ROLE.search(line):
        return category
    if _METHOD_HISTORY.search(line) or _METHOD_STATUS.search(line):
        return category
    return "KEEP"
# called in scan_file right after _gate_vocabulary_category
```

Tested on a scratch copy of `tools/` with the rest of the repository symlinked. `tools/` was not edited.
- **Labelled tests:** all 173 tests in `test_check_live_commentary.py`, `_scope.py` and `_gates.py` pass, including the 60-line hand-labelled precision and recall sample (VSG:1301, ARSP:25 and Naming:6 stay REWRITE, and RCN template:371 stays KEEP).
- **Effect:** in reference files this branch edits, blocking lines fall from 288 to 91 (197 flip). Across the whole reference surface 202 lines flip. All of them are in V2.0, V1.4, the skills and the templates, and none of them is a REAL line in the table above. What still blocks is finding J's real commentary (ARSP 7 real plus 3 false positives, VSG 58 real plus 1 false positive) and the 22 lines named in finding I.
- **Why ruling numbers stay flagged:** the rule deliberately leaves `ruling-number` alone. Two existing tests (`test_registry_word_far_from_r_number_still_rewrites`, `test_registry_yaml_filename_does_not_suppress_nearby_ruling`) require a bare "(R11)" or "(R33)" in a method document to stay REWRITE. Changing that means relabelling tests, which is Mark's call.
- **Decision needed:** adopting the rule is a governance change to what the blocking job enforces, so it goes to Mark.

## 6. Test status

- `full_pytest.txt` is complete (`exit=1`). Scope: engine/m10, m7, m9, m1/tests, m2/tests and tools/tests, run with `-x`. Result: 793 passed and 1 failed, then the run stopped.
- `pytest_all.txt` covers the same scope without `-x` and is also complete: 825 passed and 2 failed.
- Both failures are the same stale hand label: `Representative_Construction_Notes_Template.md:366` became :371 when the template gained lines. Commit 07245847 fixed it. At that commit I re-ran the three commentary test files, and all 173 passed.
- The in-scope suite is green at HEAD.
- Not covered by either run: engine/m4, engine/api and the cic/engine test scripts.

## 7. What remains for round 3

1. Findings A to F, J (the ARSP half) and K: drafting fixes inside converged decisions.
2. Findings G, H and I, and the Voice Style Guide half of J: decisions for Mark. These are the CF paragraph or the deviation sentence, B-8, the classifier rule, and whether to route the Voice Style Guide.
3. Round 3 should be a targeted recheck of those lines only: re-run `prereview` and `roundcount` in their documented form, `records --freeze`, `live-commentary --enforce`, and `reviewfile` on the round-3 file. If G, H or I are still open after round 3, they go to Mark under the round cap, not to a fourth round.
