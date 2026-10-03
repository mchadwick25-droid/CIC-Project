Simulated review - informational only, not an Article 31 substitute

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Round: 1
Truncation check method 1: PASS. Direct read of the final lines of all 11 files. Every file ends on a complete sentence, table row or YAML key. The state-file template parses with `yaml.safe_load` (15 top-level keys, ending `freeze_package_pointer`). The live gravity skill's truncated ending ("If this document r...") does not recur in the vendored copy.
Truncation check method 2: PASS. Declared lists compared against actual content. The skills README names six skills and six `SKILL.md` directories exist. The launch prompt's nine "Read first" paths all exist except the versioned Completion Standard path (Finding 1). The handoff manifest's 12 check rows match V2.0 Section 4 items 1-12, and its "/ 12" outcome row matches. The document lists in the state file (Doc_03 to Doc_10, Representative_identity, Validation) and in the ledger's per-document table match each other and V2.0's Step 3-10 table. Each skill's "What an independent review must check" list is complete, and so is each index-view list.
Verdict: SUBSTANTIAL FINDINGS

Scope: (a) `Build/Ministry/Operations/Standing/Launch-Prompts/CiC_World_Build_Launch_Prompt_V2.0.md`; (b) `Build/reference/L4-Templates/World_Build_State_File_Template.yaml`, `World_Build_Cost_Ledger_Template.md`, `World_Build_Handoff_Manifest_Template.md`; (c) `Build/reference/method/skills/` (six `SKILL.md` files plus `README.md`). Binding decisions: the converged spec of 2026-09-29. `CiC_Record_Native_World_Build_Process_V2.0.md` was used for consistency checks only.

## Findings

### 1. Launch prompt cites Completion Standard V1.3. The current standard is V1.4.

- **Where:** `CiC_World_Build_Launch_Prompt_V2.0.md:11-12`. This is the only occurrence in the reviewed files. `grep -n "V1\.3"` finds no other hit in the templates or skills.
- **What is wrong:** it points to `Build/reference/method/CiC_World_Build_Completion_Standard_V1.3.md`. That file does not exist. `ls Build/reference/method/` shows only `CiC_World_Build_Completion_Standard_V1.4.md`, and V2.0:28 cites V1.4. The hedge "(read the version on disk)" does not cure a wrong path. It tells the thread to guess.
- **Minimal fix:** cite `CiC_World_Build_Completion_Standard_V1.4.md` and delete the parenthetical.

### 2. Launch prompt forbids commits. V2.0's session rules require them.

- **Where:** `CiC_World_Build_Launch_Prompt_V2.0.md:179-180` ("Do not commit or push unless told to.").
- **What is wrong:** V2.0 Section 10 rule 7 says "End every session deployable. Partial work commits at the last green checkpoint." Rule 8 says "Commits carry step IDs. Push only on Mark's word." V2.0 gates only the push. The launch prompt gates both. A thread that obeys the prompt cannot meet rule 7, so a session break across the Friday reset loses uncommitted work.
- **Minimal fix:** "Commit at each green checkpoint, with the step ID. Push only on Mark's word."

### 3. The validation skill states an out-of-date gate count ("the seven gates at zero").

- **Where:** `skills/cic-validation-suite/SKILL.md:22`.
- **What is wrong:** `engine.m1.gates.GATES` now registers 22 gates (`python -c "from engine.m1.gates import GATES; print(len(GATES))"` prints 22). "7 gates" comes from the 2026-08-01 lean-validation decision (`Pass2-decisions/2026-08-01_M_lean_validation_interview_spend.md:25`). No other current document uses it: V2.0 (around line 873) says "the gates at zero." A thread could read "seven" as leave to run a subset.
- **Minimal fix:** "every M1 gate at zero" (V2.0's wording). Drop the number.

### 4. The validation skill's review checks a Dynamic Encounter Validation run that no step in the skill or in V2.0 schedules.

- **Where:** `skills/cic-validation-suite/SKILL.md:8` and `:78`.
- **What is wrong:** the live skill had its own section, "Run the Dynamic Encounter Validation battery." It said to run the Framework's fixed question set and score it against the encounter-success standard. The vendored skill drops that section, which fits the lean set (probes, one Deep Interview, the Craft/Focus spot-check). Yet line 78 still asks the reviewer, "Was the Dynamic Encounter Validation run against the current success standard...?" V2.0 never mentions Dynamic Encounter Validation (grep finds no hit). As written, a reviewer must either fail every lean world or ignore a check. Either way the review bar is misleading.
- **Minimal fix:** pick one. (a) Say that the live Deep Interview is the Part Eight encounter run, scored against Part Eight's success standard, and reword line 78 to match. (b) Drop line 78 and list Dynamic Encounter Validation among what lean gives up (line 57). If V2.0 has not decided which, that is a methodology question for Mark, not a drafting choice.

### 5. The build-cycle skill keeps "a dated inline note" inside world files. CLAUDE.md forbids it.

- **Where:** `skills/cic-build-cycle/SKILL.md:139`.
- **What is wrong:** the rule is carried over from the live skill, where a coach correction inside a world file "carries a dated inline note." `Build/worlds/` is a live/canonical surface under CLAUDE.md ("no notes, commentary, change history ... embedded in them"). A dated correction note is change history, and the converged spec's repo-hygiene section repeats the rule. This is a live-skill rule V2.0 should have dropped or changed.
- **Minimal fix:** "...if the correction changes no claim, finding or decision. Log it, with the date, in the world's build log at `Build/worlds/<code>/build/`, not in the file."

### 6. The build-cycle pre-draft check needs a Mark disposition that "Approved to proceed" never has.

- **Where:** `skills/cic-build-cycle/SKILL.md:47`, against `:36` and `:114`.
- **What is wrong:** line 47 says to stop when a document already marked "Approved to proceed" or "Frozen" has no "linked review file plus an explicit Mark disposition." Lines 36 and 114 say the build thread applies "Approved to proceed" itself, with no reply from Mark. So every properly self-approved document fails the line 47 test. That forces a stop the self-disposition rule exists to prevent. The live skill had the same tension ("shown to and confirmed by the project lead"). Under V2.0's self-governance it is now plainly wrong.
- **Minimal fix:** "...and there is no linked review file plus a disposition log entry (for Frozen, Mark's own recorded decision), stop."

### 7. The ledger and state-file templates have no place for items V2.0 requires them to record.

- **Where:** `World_Build_Cost_Ledger_Template.md:17-31`; `World_Build_State_File_Template.yaml:2, 8-74`.
- **What is wrong:** V2.0:1063-1065 says the ledger records "model and effort for each document and each review round, and the `/usage` reading before and after." The per-document table has token columns by tier, but no effort column and no per-round or per-document `/usage` columns. Only world start and freeze are recorded. V2.0:1170 says "a world freezes against the process version and Completion Standard version in force when its build began." The state file stamps `process_version` only, so a pilot world cannot show which Completion Standard it froze against. The launch prompt (`:153-158`) mirrors the template, not V2.0.
- **Minimal fix:** in the ledger, add a per-round table (Document, Round, Model, Effort, `/usage` before, `/usage` after). In the state file, add `completion_standard_version:` beside `process_version`. Align launch prompt lines 155-157 to match. If the other reviewer finds V2.0 lines 1063-1065 over-specified, trim V2.0 instead, but make the two agree.

### 8. The gravity skill narrows candidate generation to Doc_02. The template it tells the thread to follow allows Doc_02 and/or Doc_03.

- **Where:** `skills/cic-gravity-index/SKILL.md:22`, against `:18` ("The structural template is ... Follow it.").
- **What is wrong:** Doc_04 template Section 1 says "every candidate traced to a specific, named Doc_02 and/or Doc_03 evidence stream." The skill says "only from elements recurring across several Doc_02 evidence streams." Under the skill, a reviewer would wrongly reject a candidate traced to the Doc_03 lexicon. The live skill had the same wording, but the vendored skill now adopts the template explicitly, so the two now conflict.
- **Minimal fix:** "...across several Doc_02 and/or Doc_03 evidence streams..."

## The reconstructed gravity-index ending

The live body breaks off in its fifth review bullet: "If this document r...". The vendored review list (`cic-gravity-index/SKILL.md:45-51`) keeps the four live bullets (lines 45-48) and adds three:

- `:49` forces-connection notation for every confirmed gravity. **Supported.** The Doc_04 template (Section 3) lists "a forces-connection notation (Forces Framework Step 4)" per candidate, and the live skill's own body calls a blank "a completion failure."
- `:50` "If the document restates any claim from another document, does the wording match or is the difference disclosed?" **Not from the Doc_04 template.** The template has no review checklist at all. The rule comes from the build-cycle skill's cross-document consistency section and from V2.0's cross-document fact consistency check, so it invents no requirement. It is only a guess at what the lost "If this document r..." said. A more likely candidate is the cross-build sheet (the only index view in the live body with no matching review check). Either way, nothing unsupported was added.
- `:51` simulated-review label and truncation record. **Supported** by the converged spec and V2.0 Section 10 rules 14-15.

Result: faithful enough. No invented requirement. Not a finding.

## Rulings R26, R27, R31-C, R36, R37, R38, R41: where each belongs

Each ruling was read in `Build/Ministry/Features/Conversation-Transparency-Engine/Rulings-Pending.md`. None of the six vendored skills mentions any of them. V2.0 already carries R26, R27/R42, R31-C, R37 and R41 in its "Runtime rulings the records serve" table (V2.0:799-807). R36 and R38 are missing.

| Ruling | Status | Fold into | What to carry |
|---|---|---|---|
| R26 | RULED 2026-09-22; built 09-23 (conditional directive) | V2.0 (already there); `cic-validation-suite` | Add an other-tradition first-ask probe to the lean set. Where the world's records hold nothing on the tradition, the voice gives the fixed honest-limit sentence and then answers from its own records. Where the records hold something, it answers only from those records, cited. `neighbour_named` and `own_doctrine_in_other_tradition_turn` are fabrication failures. The lexicon and story skills should also say: name another tradition in a record only where this world's own sources do (V2.0:791-794 already says this). |
| R27 (+R27-A, R42) | RULED 2026-09-22 | V2.0 (already there); `cic-validation-suite` grading; `cic-build-cycle` Draft | Grading reads uncited-paragraph reports as places to look. Records are authored so every claim has a record to cite. **For the V2.0 reviewer:** V2.0:804 states R27's sentence-level form. R27-A moved the unit of enforcement to the paragraph. The row should say so. |
| R31-C | RULED 2026-09-24 | V2.0 only (already there) | A record-authoring and display rule (`doctrinal_witness` listed at the end of the reply; figure marks inline). No skill change needed. |
| R36 | RULED 2026-09-23 | V2.0 runtime-rulings table; `cic-validation-suite` grading | Enforcement covers `wholly_uncited_paragraph` only, flag-gated (`CIC_R27_ENFORCE`, default off). `inherited_ungrounded` stays report-only, because of the known exemption-asymmetry bug. A grader must not score an `inherited_ungrounded` flag as a FAIL. |
| R37 (+R37-A, R37-B) | RULED and BUILT 2026-09-23/24 | V2.0 (row exists but is incomplete); `cic-validation-suite` | Add R37-A's test (the named tradition's `time_window` start is at or before the speaking world's `time_window` end). Add R37-B's third source for condition (b): another Representative in the conversation. The validation suite grades the other-tradition pivot probe against that test. |
| R38 | RULED 2026-09-23 | V2.0 runtime-rulings table; `cic-validation-suite` | A fabricated clause can ride a real citation. The grader checks each tagged sentence against the full text of the record it cites, not just the match. Runtime self-revision is scoped to `other_tradition` turns. A leak there is a fabrication finding and a full-validation trigger. |
| R41 (+R41-A) | RULED 2026-09-23 | V2.0 (row exists, misstated); `cic-lexicon-index`; `cic-validation-suite` | The Representative names the modern word as the participant's own and never defines it. The modern sense lives on the term's hover card (via `term_glosses`), in no one's voice. The bridge route stays until the R41 measurement comes back near zero. Mark writes the about-page wording himself. Lexicon: terms on `anachronistic_term_ids` need a modern-sense gloss for the hover card. Validation: the re-gloss and exact-form probe grades "never defines the modern word." **For the V2.0 reviewer:** V2.0:807 says "The Facilitator explains the modern sense." R41 moves that sense out of any spoken turn and onto the hover card. The row misstates the ruling. |

## Not findings

- `Never say "finalized."` (`launch prompt:120`) names the banned word in order to ban it, as CLAUDE.md itself does. This is not a use of it.
- The metered ceiling stays an open, named field everywhere: the state file's `metered_ceiling:` is blank, the ledger has a blank line at `:43`, `METERED_CEILING_LEAN_SET` is marked open at `validation-suite:37`, and launch prompt `:45-47` says the same. No number is invented. The three labels differ from V2.0's bold label, but they name one value and no reading makes them conflict.
- No skill requires `.xlsx` workbooks. All five index skills say "No workbook." The Doc_04 template's optional companion workbook (Section 8) is overridden by the spec. That template text is a coach-thread amendment, not a defect in these drafts.
- No skill says "as many rounds as it takes." Every skill states the three-round cap and escalation to Mark, with no fourth round. The reviewer is never the drafter. Round 1 runs at high effort and rounds 2-3 at medium.
- The Craft/Focus spot-check and its four criteria (Rigor, Accessibility, Craft, Focus) match V2.0:912-931. `engine.m3.generation.LiveModelAnswerer`, `engine/m4/uncited_claims.py` and `guard_proximity` (`engine/m7/instruments.py:84`) all exist. The canon question IDs exist under `canon/sealed_probes/`.
- RS-1 and RS-2 are scored separately. An RS-2 redirect in the Representative's voice is ACCEPTABLE FALLBACK, not PASS (`validation-suite:53`, matching V2.0:927-929).
- File locations agree across the launch prompt, the templates and V2.0: `Build/worlds/<code>/build/<code>_Build_State.yaml`, `_Cost_Ledger.md` and `_Handoff_Manifest.md` (V2.0:429, 1022, 1068).
- Every cited static path exists: the V7.4 and V3.2 `.docx` frameworks, the Register Bar, the Naming Discipline, the Adversarial Review Standard Practice, `records/syr/demonstration/syr.demo.room-for-doubt.md`, the Doc_04 template, `NEEDS-RULING.md`, `cic/texts/REGISTRY.yaml`, `corpus_map_merge.py`, `corpus_index.py` and `world-census.json`. All `engine.m10.cli` subcommand names are on the allowed list.
- The handoff manifest's 12 checks match V2.0 Section 4 word for word in substance.
- Additions in the lexicon, story and forces skills are all in V2.0: the alias-safety preflight (V2.0:451, 759), CT audit before Doc_06 clears (V2.0:454), `tellable_as` 30/25-word limits (V2.0:783), composites with element-to-source tables, outsider witnesses and boundary figures (V2.0:761). The M4 lens-spine line in the forces skill (`:22`) is hedged "where the standard calls for it." V2.0 applies the spine to Doc_05 and Doc_07 only, so the line is superfluous but not wrong.
- `tools/check_live_commentary.py --surface reference` flags lines in the build-cycle and validation skills (reviewer, review-round, route-cue). Those lines state method rules, not process narration. The tool is report-only in CI (`.github/workflows/ci.yml:272`), and V2.0 itself draws 114 such flags.
- The Deep Interview's paid status and the pilot's Doc_10 dual draft are handled consistently with the spec. The spot-check's `LiveModelAnswerer` calls are live-model calls, but six calls are not a bulk run under CLAUDE.md's gate.
- Readability (FK 8-10, FRE ≥ 60) is a gate on participant-facing fields. These files are thread-facing method documents. Their prose is plain and short-sentenced, with no assistant cadence. Not measured mechanically (`textstat` is not installed).
