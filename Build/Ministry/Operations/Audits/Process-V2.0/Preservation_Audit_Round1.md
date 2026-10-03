Simulated review — informational only, not an Article 31 substitute.

Reviewer model: claude-opus-5-5
Drafter model: claude-sonnet-5-5
Reviewer agent: preservation-audit subagent, fresh context, session_01L5xhWKCzK96CZGy1fPzqGp
Drafter agent: Process V2.0 drafting thread (main thread), session_01L5xhWKCzK96CZGy1fPzqGp
Round: 1
Truncation check, method 1: direct Read of the two main new documents and both archived predecessors, end to end. Process V2.0 ends at line 1266, Appendix B, "Source records require `language`." Standard V1.4 ends at line 192, Section F, "Doc_05 and Doc_07 carry this spine." V1.9 ends at line 999, Appendix C item 3. V1.3 ends at line 124, Section F. The launch prompt V2.0 ends at line 187, "Mark decides Frozen status." All end on a finished sentence.
Truncation check, method 2: bash `wc -l`, `md5sum` and `tail -c 60` on the same five files at commit dff9a2ba. Line counts 1266, 192, 187, 999 and 124 match method 1. md5 prefixes: V2.0 bafcd9a0b7db, V1.4 526b42143510, launch prompt 8b38b953f8db, V1.9 09ff635b8b92, V1.3 e7ee6e8cedf2. The tail bytes match the final sentences quoted in method 1.

# Review of Process V2.0: preservation audit against every earlier build process

## What this audit asks

Mark asked whether the new build process keeps every strength of the earlier ones. This file lists the strengths of the old processes, one per row, and says where each one lives now.

The new process is the set of files named in the brief: Process V2.0, Completion Standard V1.4, the six vendored skills, the V2.0 launch prompt, the new L4 templates, the gate layer in `engine/m10` and the unchanged method neighbours.

The converged spec of 2026-09-29 is binding. A deliberate replacement that Mark decided is not a loss. Those rows say REPLACED BY DECISION and name the spec item.

## Status words

- **CARRIED.** A new file holds the strength with the same force. The row cites it.
- **REPLACED BY DECISION.** Mark's converged spec, or an earlier ruling he made, replaced it on purpose.
- **WEAKENED.** It survives only as a mention, moved from a gate to a note, lost its check, or lost part of its reach.
- **LOST.** Nothing in the new process carries it.

For each WEAKENED or LOST row, the "Restore?" column says whether it is a real strength a world build now lacks. The proposed restoring text is in the section after the tables.

## Sources and short names

New:

- **P** = `Build/reference/method/CiC_Record_Native_World_Build_Process_V2.0.md`
- **S** = `Build/reference/method/CiC_World_Build_Completion_Standard_V1.4.md`
- **LP** = `Build/Ministry/Operations/Standing/Launch-Prompts/CiC_World_Build_Launch_Prompt_V2.0.md`
- **BC, LX, GR, FO, ST, VS** = the vendored skills under `Build/reference/method/skills/` (build-cycle, lexicon-index, gravity-index, forces-index, story-repository, validation-suite)
- **m10** = `engine/m10/*.py` at commit dff9a2ba

Old:

- **V1.9** = `Archive/Superseded-Method/CiC_Record_Native_World_Build_Process_V1.9.md`
- **CS1.3** = `Archive/Superseded-Method/CiC_World_Build_Completion_Standard_V1.3.md`
- **BC24b** = `SKILL.md` inside `Archive/Superseded-Housekeeping/cic_build_cycle_co024b.skill`. co023 and co024 differ from it only by the coach-correction exception. co022 lacks the cross-document fact section. No strength exists in an earlier copy that co024b dropped.
- **Old skills** = the account copies of the five other build skills as they stood before V2.0, read from the session's synced skill cache. Line numbers are those files' own.
- **OD** = `Build/reference/Project-Reference/CiC_OneDocAtATime_Build_Protocol_2026-07-06.md`
- **GSR** = `Build/reference/Project-Reference/CiC_Governance_Standing_Rules.md`
- **SC** = `Archive/Technology-Pass2-2026-08/Pass2/SESSION_CONTRACT.md`
- **LPv2** = `Archive/Ministry-Early-Days-2026-07/Operations/Standing/Launch-Prompts/CiC_New_World_Build_Record_Native_Launch_V2_2026-08-30.md`
- **LPv3** = `Build/Ministry/Operations/Standing/Launch-Prompts/CiC_New_World_Build_Record_Native_Launch_V3_2026-09-08.md`
- **CF** = Construction Framework V7.4 (.docx). **RCF** = Representative Construction Framework V3.2 (.docx). **FG** = Facilitator Governance V3.6 (.docx). "¶N" means the Nth non-empty paragraph of the file's `word/document.xml`, after tags are stripped.
- **ARSP** = `Build/reference/method/CiC_Adversarial_Review_Standard_Practice.md`
- **lpc DL** = `Build/worlds/lpc/lpc_Decision_Log.md`
- **don VL** = `Build/worlds/don/don_Validation_Layer.md`
- **M2 audit** = `Build/Ministry/Operations/Audits/CiC_M2_Migration_Validation_Gap_Audit_2026-09-27.md`

## Counts

146 items.

| Status | Count |
|---|---|
| CARRIED | 105 |
| REPLACED BY DECISION | 16 |
| WEAKENED | 18 (16 worth restoring) |
| LOST | 7 (6 worth restoring) |

## The inventory

### 1. Sourcing and handoff

| ID | Strength | Old source | Status | Where it lives now, or what changed | Restore? |
|---|---|---|---|---|---|
| S1 | Source Registry built on the template from its first row. Machine-readable rows. Load-bearing caveats are row fields, not prose. Holdings dispositions (R13) for every unassessed file. | V1.9:163 | CARRIED | P:318; handoff check 4 | — |
| S3 | Every item of the library package gets a line. Step 2 hands over loci, quotability flags, voice flags, a thin-evidence map, editions and pairs. | V1.9:175-203 | CARRIED | P:329-350 | — |
| S5 | Verification-first library use: coverage check, scoped index, discovery helper off the sandbox, the shared download queue, `--write-only` merges, canonical addresses. Scoped search is the one read path. A corpus-map row is not a registry row. | V1.9:285-360 | CARRIED | P:352-397 | — |
| S8 | Twelve handoff checks. Any failure stops the build and sends the world back. | V1.9:208-246 | CARRIED (stronger: now code) | P:399-436; `m10/handoff.py` | — |
| S9 | Every Step 0-2 quote re-verified against the vendored file, speaker included. An opponent's paraphrase is never the subject's words. | V1.9:234-236 | CARRIED | P:422-424; `handoff` check 8 | — |
| S10 | Mark signs off each handoff. The build never redoes Steps 0-2. Gaps go back to the Library so the next world gets them. | V1.9:248-253 | CARRIED | P:438-442; handoff manifest template | — |
| S11 | Registry rigour: every Doc_02 claim has a row; every Native row names what it is licensed for; reviewer's ten-item recall test and verbatim PRESS question; search record, bibliography sweep and saturation statement; rights fail-closed. | CF ¶581, ¶619-627; CS1.3:23; V1.9:616 | CARRIED | Library stage; P:764-766; S:24, 58 | — |
| S15 | Source Acquisition Manifest and intake cross-check as Mark's edition ruling. | LPv2:119-145, 192-210 | REPLACED BY DECISION | Spec "Scope": the Library owns Steps 0-2 | — |
| S16 | Doc_02 analytic duties: Author Gravity with transmission history, secondary scholarship, material culture, missing voices, preliminary forces. | CF ¶124-191, ¶223-276 | REPLACED BY DECISION | Spec "Scope" (Library). Doc_05 still requires Material Culture, P:459 | — |
| S17 | Cross-world questions carried forward, never decided inside one world. | V1.9:237-239 | CARRIED | P:425-428 | — |
| S18 | Before building, check for a prior partial build of the same world (unmerged branches, `Archive/`, older folders). Recover and audit it rather than start fresh. | LPv2:41-44; V1.9:995-999 | LOST | Nothing in P, S, LP or the handoff checks asks it. Cappadocian was found on an orphan branch this way. | Yes |
| S19 | Doc_03 draws its terms from the Registry's Native rows, not from raw Doc_02, because Doc_02 can still name excluded sources. | CF ¶634 | WEAKENED | P:447 says Doc_03 searches "the world's shelf". The shelf is the corpus-map bucket, which holds context and antecedent works that are not Native. | Yes |

### 2. The per-document cycle and review

| ID | Strength | Old source | Status | Where it lives now, or what changed | Restore? |
|---|---|---|---|---|---|
| R1 | One document at a time. Nothing later is drafted, outlined or planned. | OD:25, 55 | CARRIED | P:451-453; BC:39 | — |
| R2 | Derive the document sequence fresh from the Framework and confirm it before work. | OD:20-21 | REPLACED BY DECISION | The sequence is fixed in P:455-465 | — |
| R3 | A review is its own file; if it is not on disk it did not happen. It checks each claim's accuracy, consistency with earlier decisions, attribution, the stage's job, and forces integration at the six integration steps. | OD:26; BC24b:28, 36-38 | CARRIED | BC:46, 75-79; `roundcount` counts files | — |
| R6 | A finding is never dismissed as a tooling artifact, and a blocking finding is never dismissed by self-certification. Both need independent re-confirmation (high effort, fresh context). | OD:62; BC24b:40; GSR:31; V1.9:916 | CARRIED | P:237, 1170-1173; BC:80 | — |
| R7 | Content called "shown" is included verbatim. Nothing is shown in summary at a review or sign-off. | OD:56, 64 | CARRIED | BC:81; P:248-252 | — |
| R8 | Substantial versus cosmetic threshold. | GSR:32 | CARRIED | P:1141-1146 | — |
| R9 | Four escalation categories, including every later identity change. Two disagreeing reviews are logged and escalated. Portfolio decisions are labeled as such. | OD:34-39, 61 | CARRIED | P:193-201; BC:92-103 | — |
| R11 | The build thread applies "Approved to proceed" itself when an independent review clears and no escalation applies. Frozen is Mark's alone, on an unambiguous act; doubt defaults down; Frozen can be reopened. | OD:29, 59; BC24b:67-79 | CARRIED | P:188-191; BC:111-115 | — |
| R13 | A status line is not evidence. An "approved" file with no review record stops the thread. Nothing is attributed to Mark without a record. Each disposition is logged with its review file paths. | OD:30, 58, 60, 63 | CARRIED | BC:47, 117-119; state file `review_files` | — |
| R15 | All output goes in the world's canonical folder. | OD:65 | CARRIED | BC:48 | — |
| R17 | Name and term changes propagate to every file. Cross-document facts match, with the two worked defects as warning. | OD:43, 47 | CARRIED | P:473-477; BC:105-107, 121-123 | — |
| R19 | Periodic coach verification across a batch: review files exist and support what cites them, the log matches disk, decisions match the governing designs. It caught phantom reviews on Worlds #1 and #7. | OD:9, 51; BC24b:92-94 | WEAKENED | Only BC:133-135 mentions it. P names no owner, cadence or trigger. P:1207's five-world review is a cost-and-quality review. | Yes |
| R20 | Governing files are coach-edited. A build thread writes only in its own world and routes a framework gap as a finding. | OD:51 | CARRIED | P:203-204; BC:137 | — |
| R21 | Round cap of three, then Mark. Opus reviews every round; rounds 2-3 are targeted rechecks. The reviewer is never the drafter. | CLAUDE.md; V1.9:864-876 | CARRIED (stronger: `roundcount`, `reviewfile`) | P:219, 1141-1154 | — |
| R24 | Simulated-review label on every agent review. Two-method truncation check with raw evidence; the direct read wins; a dismissed disagreement needs independent confirmation. | GSR:29-30 | CARRIED | P:1160-1169; `reviewfile` (it checks that two different methods are named, not the raw evidence) | — |
| R27 | Fix script-catchable defects before review. The brief says what the scripts covered and what they cannot cover. Briefs are pointers, not summaries. | V1.9:598-604, 927-932 | CARRIED | P:248-268 | — |
| R29 | Adversarial practice: read prior findings first, name the failure mode to hunt, count structural checks, give a plain verdict. Reviewer tier checked every round. | ARSP:11-19; V1.9:940-944 | CARRIED | LP:17 (read in full); P:256-257; `reviewfile` | — |
| R31 | Claims register as a control: a script derives every absence or exclusivity claim ("no source says...") from the deliverables and halts on an unregistered or stale claim. That one class was 8 of 11 HIGH findings on lpc Doc_09. | lpc DL:1629-1650 | WEAKENED | P:467-471 asks only that a register is kept. No gate derives or checks claims. BC:51 uses a different trigger (see Contradictions). | Yes |
| R32 | A correction's propagation is verified by a separate thread against the source, sweeping outward from each named site. On lpc it failed twice before it held, both times by fixing only the named instance. | lpc DL:1795-1835 | WEAKENED | P:469-471 says every carrying document "is checked", but not by whom, and not against source. | Yes |
| R33 | One state at a time: no structural edit to a tree while a review of that tree is running. | lpc DL:1625 | LOST | Not in P §10 or BC. | Yes |
| R34 | Status lines hold current status only. Round history lives in one log, so it cannot go stale in two places. | lpc DL:559-571 | CARRIED | P:714-745, 1095-1099 | — |
| R35 | Find a cited passage by its structural marker (`div` title, chapter heading), never by a single grep hit. Both lpc Doc_02 HIGHs of Rounds 28-29 came from grep hits in the wrong work. | lpc DL:559, 573-580 | WEAKENED | P:475-477 says to confirm each locus "with a scoped corpus_index search", which is itself a hit-based lookup. | Yes |
| R36 | A scoped final round aimed at the one live failure mode; stop when the substance clears. | lpc DL:573-580, 1745-1756 | CARRIED | P:1141-1154 | — |
| R37 | Record Integrity Principle, a CF freeze criterion: a fix closes out the earlier documents in the same change set; a reviewer's fix recommendation is executed or deferred with a reason; "applied" means found in the deployed artifact; superseded files are archived at once. | CF ¶76-83, ¶580 | WEAKENED | P:21 names it. `gaps` covers open items and `deployed` covers three confirmed items, but no freeze-time read checks the rest. S never mentions it. | Yes |
| R38 | Fix the mechanism, not the symptom. No banned-phrase lists. | CF ¶73-75 | CARRIED | P:139-141, 565-566 | — |

### 3. Record authoring gates (Phase B)

| ID | Strength | Old source | Status | Where it lives now, or what changed | Restore? |
|---|---|---|---|---|---|
| A1 | Born record-native by committed per-step scripts with dense docstrings; gates green from the first record; the scripted pass runs before every review. | V1.9:575-604 | CARRIED (stronger: `prereview`) | P:546-555, 747-758 | — |
| A4 | Register bar as a birth condition: one approved sample, no banned lists; a sentence the reviewer must re-read fails; bar-screen artifact saved before B-8. | V1.9:366-377, 483-490 | CARRIED | P:557-566, 662-669 | — |
| A5 | NorthStar readability as a visibility number, "nothing gates on a number". | V1.9:378-380, 487-490 | REPLACED BY DECISION | Spec "Quality bar" and resolution 9: readability is now a mechanical gate. P:135-137; `regate` | — |
| A6 | Decision 8B; `modern_rendering` at birth, Opus-authored and separately Opus-checked; non-English primaries; the fragment rule; source-spoken forms, lists and ellipses; the register rule for renderings. | V1.9:381-447 | CARRIED | P:570-628 | — |
| A10 | No model retypes a source. The verbatim gate runs at birth, with honest `verification_state` and general fixes only (R33). The rendering-fidelity graders need two clean runs, and a standing disagreement is recorded, not chased. | V1.9:448-482, 619 | CARRIED | P:629-661, 769 | — |
| A14 | Transparency ground: each cell offers a story and a term, or records an honest empty. The witt "Answer-the-Canon" pass closed every blank cell with grounded records or an honest limit. | V1.9:492-507; `Build/worlds/witt/Open_Gaps_Tracking.md`:950 | CARRIED | P:671-684; S:82-89; `gate_canon_coverage` (`engine/m1/gates.py`:731) | — |
| A16 | No spoken field hard-binds a first-mention introduction. | V1.9:508-518 | CARRIED | P:685-693 | — |
| A17 | Voice perspective as a birth condition and gate. | V1.9:520-541 | CARRIED | P:695-712 | — |
| A18 | File discipline: clean operative fields, durable record bodies, full provenance fields, no invented fields, residue read before every pin; the narration scan. | V1.9:543-573; LPv2:233-272 | CARRIED (stronger: the scan blocks PRs) | P:284, 714-745; S:91-98 | — |
| A20 | B-1 rows at birth (shelf row, caveats verbatim, language, Article 29 provisional); B-1a sweep with saturation record; B-2 alias safety at zero with a coverage assertion. | V1.9:614-617 | CARRIED | P:764-767 | — |
| A23 | B-3 confidence extracted, never re-judged; reciprocal relations; `gloss_forms`. | V1.9:618 | CARRIED | P:768; `gate_reciprocity` | — |
| A24 | A confirmed-gloss file, with Mark confirming each gloss one at a time. | V1.9:618; LPv2:326; LPv3:110 | REPLACED BY DECISION | The earlier glossary-retrofit ruling: term records are the gloss list (P:768; gate `glossary-retrofit-complete`). Not in this spec. | — |
| A25 | B-4 to B-6: tier justifications verbatim, composite element-to-source tables, outsider witnesses own their accounts; Doc_04/Doc_08 reasoning in full, matrices mirrored including no-relationship pairs, never force-fit; contested claims with live divergence partners and declared non-claims. | V1.9:619-621 | CARRIED | P:769-771 | — |
| A28 | B-7: register position earned from genre evidence; length measured, not designed; demonstrations grep-clean; 900-word budget; hard conversion, not a copy. | V1.9:622 | CARRIED (field names stale, see Contradictions) | P:772 | — |
| A29 | B-7a pairing cautions; living traditions and telos provisional. | V1.9:623 | CARRIED | P:773; telos parked in the construction notes until a field exists (P:1235) | — |
| A30 | B-8 four parities, the production-eval verdict rule, golden set before tuning; B-9 guards only record-derived and cold-verified. | V1.9:624-625 | CARRIED | P:774-775 | — |
| A32 | R11 guards versus redirects; guard only what could mislead. | V1.9:627-636 | CARRIED | P:777-786 | — |
| A33 | R6 register ceilings, advisory. | V1.9:638-646 | REPLACED BY DECISION | Resolution 9: now a gate. P:788-796; S:69-80 | — |
| A34 | R26 other traditions named only where the world's own sources do. | V1.9:648-652 | CARRIED | P:798-802 | — |
| A35 | Guard-coverage read after B-6. | V1.9:654-661 | REPLACED BY DECISION | Resolution 4: the Craft/Focus spot-check, P:932-945 | — |
| A36 | Re-proof of any prompt fix under the deployed runtime. | V1.9:663-667 | CARRIED | P:816-820 | — |
| A37 | Record status R16 is never hand-set; the registry entry comes first. | V1.9:877-889 | CARRIED | P:821-824, 1156-1159 | — |
| A39 | Schema-enum collision list. | V1.9:972-981 | CARRIED (names stale, see Contradictions) | P:1257-1266 | — |
| A40 | No `.xlsx` workbooks; every index derived from records, never a hand list. | V1.9:279-283 | CARRIED | P:518-519; all skills | — |
| A41 | The four index bars: lexicon (tags as own fields, CT Contest Type audit, reciprocity, author-gravity flag), gravity (candidate table, interaction matrix with visible thin rows, not-advanced list, cross-build sheet), forces (inverted by-gravity view, transmission check), story (No-Tier-5 audit, Native-source check, Absent Stories). | Old skills: lexicon 14-32, gravity 22-49, forces 14-39, story 14-32 | CARRIED | LX:30-49; GR:31-53; FO:24-43; ST:24-42 | — |
| A45 | Story tier to confidence cross-walk; Writing-From-Inside in all inhabited prose. | CF ¶216-222, ¶386, ¶517 | CARRIED | ST:28; LX:19; P:695-712 | — |
| A47 | Confidence/Gravity Cross-Check and the Article 21 cross-strand test; forces in every Doc_05 lens; Doc_07 lens spine with Material and Ethical/Legal required; Doc_08 complete before validation. | CF ¶123, ¶308-311, ¶657-694 | CARRIED | GR:26-27; P:459-462; S:184-192; `confidence-crosscheck` gate | — |
| A50 | Tier 1 lexicon entries reach real depth before the Doc_07 lenses start. | CF ¶668, ¶674 | WEAKENED | Not stated. The fixed sequence and Doc_06 review cover most of it. | No |
| A51 | The world's own words go into spoken prose in label form, so the transparency scan can light them. | LPv2:214-219 | CARRIED | P:562-564 | — |

### 4. Representative construction and voice

| ID | Strength | Old source | Status | Where it lives now, or what changed | Restore? |
|---|---|---|---|---|---|
| V1 | M1: grounded role and name options, one recommendation each, identity and image in one package of 2-4 candidates checked against the naming discipline's five tests; Mark's words recorded verbatim; never proceed on the recommendation. | V1.9:109-128; LPv3:42-51 | CARRIED | P:150-179; LP:171-173 | — |
| V4 | No invented biography; uniform polish is a fabrication risk; hedges are the world's own. | CLAUDE.md; RCF ¶63 | CARRIED | P:500-506 | — |
| V5 | Ecology Assessment (four domains plus Thinness Mapping) calibrates the probes. | RCF ¶43-56; old VS:10-12 | CARRIED | P:465; VS:21 | — |
| V6 | The Ecology Assessment comes before identity and can decide construction should not proceed. | RCF ¶178, ¶182 | WEAKENED | It now sits inside Doc_10, after M1 | No. lpc and rzg chose identity first from Doc_01-09 and it held. |
| V7 | Depth calibrated from Doc_04/Doc_08; thinness is silence, not confession; uneven depth is authentic. | RCF ¶37, ¶69-72, ¶130-132 | CARRIED | Doc_10 template §3 (`Representative_Construction_Notes_Template.md`:223-266), which P:43-46 makes mandatory | — |
| V8 | Approved Source Anchoring: 5-10 of the Registry's Native entries in a grounding-anchor paragraph of the deployed prompt. It is the generation-time guard against reaching for another world's more vivid image, and a CF freeze criterion. | RCF ¶101-103, ¶184; CF ¶581, ¶709 | WEAKENED | The Doc_10 template §2 keeps a design section. No record field carries it into `compiled/prompt.txt`, `deployed` does not check it, and P and S never mention it. | Yes |
| V9 | Witness-not-recruitment and fierceness calibration, Christ-ward telos derivation, living-tradition handling (Facilitator-carried). | RCF ¶207-210; lpc DL:1887 | CARRIED | Doc_10 template §4-§6; P:181-186, 773; `facilitator_brief.living_tradition_handling` | — |
| V12 | Register fidelity and readability are separate checks; a voice that could be swapped for another world's has failed. | RCF ¶60, ¶86-87 | CARRIED | P:63-76; Register Bar | — |
| V14 | Four criteria with Craft as keystone; the measured defect rate is not the checker's miss rate; vision framing. | V1.9:33-100 | CARRIED | P:52-124 | — |
| V15 | Stories told, not summarized; the Doc_10 Craft/Focus bar (a)-(e). | V1.9:55-63, 277 | CARRIED | P:78-84, 479-498 | — |
| V18 | Fable drafts Doc_03, Doc_06, Doc_08 and Doc_09, because discovery misses are invisible to every gate. | V1.9:898; LPv2:280-285 | REPLACED BY DECISION | Spec "Models". Note: the pilot's Sonnet-versus-Fable test covers Doc_10 only, so discovery depth on Doc_03/06/09 is not measured. | — |
| V19 | Test the built runtime artifacts, not illustrative examples. | RCF ¶188 | CARRIED | P:896-901 | — |
| V20 | Facilitator coordination drawn from the thinness map. | RCF ¶194 | CARRIED | `facilitator_brief` required (P:535; S:32), with `formation_limitations` (`engine/m1/schemas.py`:748-757) | — |
| V21 | Encounter Ecology Mapping as its own phase. | RCF ¶195-202 | REPLACED BY DECISION | Spec "Deliverables": a short section in Doc_10, P:533 | — |
| V22 | The World Profile: a synthesis of all construction work, and an input to the Validation Layer, the Ecology Assessment and the Facilitator. | CF ¶701-703; RCF ¶175 | WEAKENED | The spec makes it generated (P:530; S:38-42). No builder exists in `engine/m2` or `engine/m10` (grep finds none), and P §13 lists only the integrative-observation field. Today a new world gets neither a written nor a generated profile. | Yes |
| V23 | Capsule Core inhabited-voice text. | RCF ¶188 | REPLACED BY DECISION | Spec "Deliverables"; field open, P:531, 1231-1234 | — |
| V24 | Voice Configuration. | Template | REPLACED BY DECISION | Spec "Deliverables": dropped unless audio ships | — |

### 5. Safety and the Facilitator boundary

| ID | Strength | Old source | Status | Where it lives now, or what changed | Restore? |
|---|---|---|---|---|---|
| F1 | The redirect is Facilitator-only, template-anchored and never conditional; the draft mechanism is not settled. | CLAUDE.md | CARRIED | P:508-516; LP:133-135 | — |
| F2 | Historical otherness is not distress; near safety, default to caution. | CLAUDE.md | CARRIED | VS:15-16; CLAUDE.md is read first (LP:10) | — |
| F4 | Per-world wiring check; the shared classifier is validated once, fleet-wide. | CS1.3:74-81 | CARRIED (stronger: `wiring`) | S:109-114 | — |
| F5 | RS-1 and RS-2 scored apart; a Representative-voice redirect is ACCEPTABLE FALLBACK, not PASS. | Decision-log rule named in the spec | CARRIED | P:948-951; `m10/validation.py` | — |
| F6 | Relational safety tested apart from frame-break probes, so tuning cannot suppress disclosure; encounter-readiness safety review. | RCF ¶142; CF ¶527 | CARRIED | `wiring`; B-7 review of R19 | — |
| F7 | R19 distress-comparison guard in the world's idiom, never pointing outward. | V1.9:622 | CARRIED | P:772 | — |
| F9 | A safety-adjacent Representative gets full validation. Under CS1.3 every Representative did. | CS1.3:83-96 | WEAKENED | P:967 names the trigger, but `m10/validation.py`:155 marks it undeterminable and the verdict still prints `lean`. This fails open. Already raised as Gate_Layer_Code_Review_Round1 finding 5. At audit time an uncommitted working-tree change adds an `undetermined` verdict; it holds only once committed and tested. | Yes |
| F10 | Clean passes in known hard-to-detect domains stay provisional. | Old VS:39; FG ¶112-120 | CARRIED | P:914-915; VS:58 | — |
| F12 | World Facilitation Brief content: strengths, limits, participant fit, pairings, cautions. | FG ¶35 | CARRIED | `facilitator_brief` schema; P:535; S:32 | — |
| F13 | Article 20: naming whose voices the sources omit is a participant-facing duty the Facilitator carries. | CF ¶185 | WEAKENED | Doc_02 names absences and Doc_09 answers Absent Stories, but nothing requires `facilitator_brief` to carry them. | Yes (low) |

### 6. Validation and probes

| ID | Strength | Old source | Status | Where it lives now, or what changed | Restore? |
|---|---|---|---|---|---|
| T1 | Lean by default, over a floor that is never cut. | V1.9:722-736 | CARRIED | P:878-894 | — |
| T2 | The lean probe classes: naming collision, horizon press, fabrication press at the thinnest areas, world-specific, parroting, pushback, over-settling, re-gloss. | V1.9:738-753 | CARRIED | P:905-915 | — |
| T3 | Every one of RCF Part Eight's eight categories gets a concrete probe: Source-Awareness, Anachronism, Confidence-under-Thinness, Self-Referential, Scholarly-Framework, Relational Safety, Claim-Laundering and Decontextualization, Sustained Engagement. Parroting and pushback come on top. gallic and cappadocian Phase Five ran all eight. | CS1.3:83-87; RCF ¶136-144; old VS:14-18; `Build/worlds/gallic/gallic_Phase5_Boundary_Testing_Validation_DRAFT.md`:75-205 | WEAKENED | P:905-915 and S:123-129 list no Source-Awareness, Self-Referential, Scholarly-Framework or Claim-Laundering probe. Only VS:33 and the Doc_10 template §7 ask for all eight, and `validation` does not check coverage. FG ¶120 records self-narration under direct pressure as a systemic failure, and the lean set no longer presses it. | Yes |
| T4 | Each probe has a scenario, a pass criterion and a linked Violation Indicator. | Old VS:18, 26-33 | CARRIED | VS:64-66; Doc_10 template §7 (see Contradictions for the result template) | — |
| T5 | Dynamic Encounter Validation and the four Encounter-Success conditions (Constitution Article 6): the voice stays itself, the participant keeps authorship, tensions are held, nothing is steered or tilted. gallic Phase Five §4 scored them. | RCF ¶149-163; old VS:20-22 | LOST | P, S and the Deep Interview grading never mention them. The four criteria do not test non-steering. | Yes |
| T6 | Extended Deep Interview, 6-8 rounds off the actual answers, graded on six dynamics. | V1.9:755-766 | CARRIED | P:916-931 | — |
| T7 | Live smoke test against the real production deploy. | V1.9:713-716, 766 | REPLACED BY DECISION | Spec "Scope": go-live is a separate thread. The Deep Interview runs on staging (P:916-931). | — |
| T8 | Pre-score transcripts; the grader still reads every transcript in full. | V1.9:768-774 | CARRIED | P:954-959 | — |
| T9 | Six-question Craft/Focus spot-check. | V1.9:776-792 | CARRIED | P:932-945 | — |
| T10 | Declare in the freeze package what lean gives up. | V1.9:794-807 | CARRIED | P:988-999 | — |
| T11 | Loop until dry: root-cause, fix at the record, cold re-probe, re-run the class. | V1.9:809-813 | CARRIED | P:1001-1005 | — |
| T12 | Validation Protocol Rigor: two trials, fresh context, blind grading for every freeze. | CF ¶529-535; CS1.3:83-87 | REPLACED BY DECISION | Spec "Validation (decision 1)": lean single-trial by default; full on triggers (P:978-986) | — |
| T13 | Table Readiness Round in its cost-capped form, with findings routed (a), (b), (c) and Mark closing (b) and (c). | CS1.3:88-96; V1.9:815-819 | CARRIED | S:154-161, under full validation | — |
| T14 | Results labeled observed or authored; only `compiled/prompt.txt` is tested. | Decision-log rules named in the spec | CARRIED | P:896-901, 951; `probes`, `validation` | — |
| T16 | Validation evidence belongs to the pin being frozen. After any rebuild the battery is re-run. The M2 audit found ten of eleven worlds tested only against pre-rebuild artifacts. | M2 audit:69-90, 109-121 | WEAKENED | `probes` reports a tested pin that differs from the current pin as a note only (`m10/deployed.py`:411 at dff9a2ba; still a note at line 430 in the uncommitted working tree). P never says a repin after validation re-opens the affected probe classes. | Yes |
| T17 | Validation matrix and its views, continuity regression, checkpointed probe state, metrics recorded with "threshold not yet set". | Old VS:24-40; CS1.3:88, 98-108; V1.9:824-826 | CARRIED | VS:64-73; S:129, 163-173; P:1014-1016 | — |
| T20 | If the build judges lean too thin for this world's risks, it says so to Mark with the reason and the price. | LPv2:316-320 | WEAKENED | P:961-963 makes the triggers code-only. Nothing lets a thread raise the level; the spec forbids only thread judgment that lowers it. | Yes |
| T22 | Ecological Integrity testing (Balance, Reduction, Complexity, Emergence, Worship Integration) and Differentiation testing. Both are CF world-freeze criteria, and the don and rzg Validation Layers tested both. | CF ¶536-551, ¶569-575; don VL:36-52; `Build/worlds/rzg/rzg_Validation_Layer.md`:47-68 | LOST | The spec's thin Validation Layer lists only Historical Plausibility, Anachronism, Author Dominance, Living Tradition and what cannot be tested (P:532; S:43-47). The gates report cannot cover the rest, because no gate tests balance or differentiation. | Yes. This is a gap in the decision's own list, so it goes to Mark. |
| T23 | The Validation Layer names what it cannot test and which freeze criteria are not met, instead of skipping or claiming them. | don VL:76-93 | CARRIED | P:532; S:43-47 | — |
| T24 | Re-extract the governing text fresh; never test against a remembered list. | Old VS:8; gallic Phase Five:21-25 | CARRIED | VS:8; GR:18; LP:12-14 | — |
| T25 | Admission rests on Mark's own live conversation with the world, never on a score. | LPv2:180-184 | REPLACED BY DECISION | Spec "Scope": go-live and admission are Mark's separate acts; he reads the transcript in the freeze package (P:918-920) | — |
| T26 | A $3 ceiling per M3 admission run. | V1.9:821-822 | REPLACED BY DECISION | Spec resolution 10: one metered ceiling for the lean set, owed by Mark | — |

### 7. Freeze and closure

| ID | Strength | Old source | Status | Where it lives now, or what changed | Restore? |
|---|---|---|---|---|---|
| Z1 | Only Mark assigns Frozen. | V1.9:138-141 | CARRIED | P:188-191 | — |
| Z2 | Article 29 determination drafted and carried provisional for Mark's word; Article 31 is not a stop. | V1.9:130-136; lpc DL:2242-2262 | CARRIED | P:181-186 | — |
| Z4 | Freeze package: gate report, declaration in the S6.2 shape, fleet sweep green, completion summary. | V1.9:831-839 | CARRIED (expanded) | P:1018-1032 | — |
| Z5 | World-freeze split from Representative-freeze; required record completeness; views render, the brief renders complete, the repository ships fail-closed. | CS1.3:12-31 | CARRIED | S:13-33 | — |
| Z7 | Every freeze check is a saved artifact, never a self-report. | CS1.3:33-39 | CARRIED | S:54-60 | — |
| Z8 | The standard is versioned; a world freezes against its start version; a standard nothing fails is not a standard. | CS1.3:112-115 | CARRIED | S:175-180; P:1212-1218 | — |
| Z10 | Nothing closes until Phase Five boundary testing and full-system review. | GSR:16 | CARRIED | P:1034-1037; S:180-182 | — |
| Z11 | Stop at the world boundary with a completion summary. | SC:17; V1.9:839 | CARRIED | P:1032, 1129 | — |
| Z13 | Hand a summary to the System Hub thread to sync the Standing files; never edit the Dashboard, Task Board or Gantt directly. | LPv2:328-330; LPv3:111-113 | LOST | Not in P or LP. | Yes (low) |

### 8. Governance vocabulary

| ID | Strength | Old source | Status | Where it lives now, or what changed | Restore? |
|---|---|---|---|---|---|
| G1 | "Approved to proceed", never "finalized"; three dispositions. | GSR:15-17; OD:11 | CARRIED | P:1174-1175; BC:111-115 | — |
| G3 | Change orders, never quiet edits. | CLAUDE.md; CS1.3:113 | CARRIED | P:1187-1189, 1212-1218 | — |
| G4 | Five confidence levels; "Not Attested" is not a sixth. | CLAUDE.md | CARRIED | P:826-832 | — |
| G5 | Open_Gaps append-only, numbered, cited by subject and date; ACCEPTED_OPEN waivers; every open item in a review has an entry. | CLAUDE.md; spec rule | CARRIED (stronger: `gaps`) | P:283, 1176-1182 | — |
| G7 | Logs in Ministry, superseded files to Archive; defects filed, never silently patched; upstream wording referred. | CLAUDE.md; SC:36 | CARRIED | P:1130-1131, 1183-1186 | — |
| G9 | Full autonomy, done responsibly: record the real alternatives and why the chosen one is most defensible, not just the conclusion. | SC:12-13 | WEAKENED | P:1129 says only "Every decision is recorded." | Yes |
| G10 | Uncertainty past one's own confidence is filed, not decided. | SC:14 | CARRIED | P:193-204, 1130 | — |

### 9. Session, cost and operations

| ID | Strength | Old source | Status | Where it lives now, or what changed | Restore? |
|---|---|---|---|---|---|
| O1 | Read the state first; re-run the previous checkpoint by kind, against committed IDs. | SC:31-32 | CARRIED | P:1111-1119 | — |
| O3 | Declared `Touches:`; never edit a gate in the session that must pass it. | SC:33-34 | CARRIED | P:1120-1124 | — |
| O5 | Done means a committed artifact that re-runs green; end every session deployable. | SC:35, 37 | CARRIED | P:1125-1136 | — |
| O7 | The ledger, the commits and the checkpoint artifacts tell one story; a mismatch is itself a filed flag. | SC:38 | WEAKENED | P:1137 keeps step IDs in commits only. | Yes (low) |
| O8 | Push only on Mark's word. | V1.9:860 | CARRIED | P:1137 | — |
| O9 | Safety and retrieval regression reruns. | V1.9:861-863 | CARRIED | P:1138-1140 | — |
| O10 | Everything that can be a program is a program. | SC:40 | CARRIED (stronger: P §3) | P:261-300 | — |
| O11 | Budget check before a world; never strand a world across a reset; state file; heavy steps early; version stamped. | SC:19; spec | CARRIED | P:57-59, 1079-1102, 1212 | — |
| O12 | Stewardship never outranks quality. A budget number never thins the work. The build halts and states the choice; running out is not a licence to rush. | LPv2:293-301; SC:21 | WEAKENED | CLAUDE.md states the principle. P §9 adds per-world targets, ceilings and a start check, but no halt-never-thin rule. | Yes |
| O13 | A per-world dollar envelope, approved once at launch. | LPv2:303-309 | REPLACED BY DECISION | Spec "Standing constraints": allowance share, two ledgers, start-of-world check | — |
| O14 | Per-document and per-round model, effort and `/usage`; pinned routing; `xhigh` kept for the reasoning edge. | V1.9:882-925 | CARRIED | P:208-246, 1091-1093; ledger template | — |
| O16 | Paid-bulk-run gate. | CLAUDE.md | CARRIED | P:1067-1077 | — |
| O17 | The repository is the context bus; no phase re-narrates state. | LPv2:287-289 | CARRIED | P:248-252, 1095-1102 | — |
| O18 | Fetch `origin/main` before judging what exists, and run one live thread per world. An lpc thread on a stale checkout duplicated a merged phase and overwrote a real review file. | lpc DL:2210-2220 | LOST | Not in P §10 or BC. | Yes |
| O19 | While waiting at a boundary, do bounded scoped work instead of idling. | SC:19 | LOST | — | No. One world at a time and the start check cover the case. |

## Restorations proposed (minimal text or check)

Each item names where the text goes. Nothing here is applied. Items that change methodology need Mark's word.

- **T3 (Part Eight coverage).** P §8 item 1 and S §C: "The lean set holds at least one probe in each of RCF Part Eight's eight categories. Relational Safety is met by the wiring check and the RS rows. Parroting and pushback come on top." In `m10/validation.py`, fail when a Part Eight category has no row. This fits inside 10-14 probes.
- **T5 (Encounter-Success).** P §8, Deep Interview grading: "It is also scored on Constitution Article 6's four encounter-success conditions: the voice stays itself; the participant keeps authorship of their own direction; tensions are held as the world held them; nothing is steered or tilted by cumulative persuasion." This is a methodology choice, so it goes to Mark. The launch-templates review Round 1 already put a related choice to him.
- **T22 (Ecological Integrity and Differentiation).** Mark's call, since the spec enumerates the categories. Proposed P §5 and S §A wording: "The Validation Layer also attests Ecological Integrity (Balance, Reduction, Complexity, Emergence, Worship Integration) and Differentiation, citing Doc_04, Doc_07 and Doc_01, as the don and rzg Validation Layers did." Otherwise a change order must remove them from the CF freeze criteria.
- **R31 (claims register).** `prereview` runs a claims check on the lpc model (`Build/worlds/lpc/scripts/check_claims.py`). It derives every absence or exclusivity sentence and fails on an unregistered claim or a stale register entry. P:467: "Registration is the control. Verification is separate work, and the register shows which claims are verified."
- **R32 (propagation).** P, cross-document consistency: "A correction that changes a claim is verified by a separate agent against the source before the document proceeds. It sweeps outward from every site the correction names, not only those sites."
- **R35 (locators).** P:475-477: "Confirm each cited locus by its structural marker (div title, chapter heading) in the vendored file. A single search hit is a lead, not a confirmation."
- **R33 (one state).** P §10, new rule: "No structural change to a tree while a review of that tree is running."
- **O18 and S18 (stale state, prior builds).** P §10 rule 1: "Fetch `origin/main` before reading the state file. One live thread per world." Handoff, new check or a line in check 1: "Search unmerged branches, `Archive/` and `Build/World-Builds/` for a prior partial build of this world. Recover and audit it rather than start fresh."
- **V8 (source anchoring).** Either state how the record-native prompt meets the CF grounding-anchor freeze criterion, for example a `voice_craft` field compiled into the prompt with a `deployed` check, or record a change order that retires the criterion. Today the CF, which P ranks as the first authority, requires something the build cannot produce.
- **V22 (World Profile).** P §13, new open item: "World Profile view builder. Until it exists, the World Profile is neither written nor generated. S §A's 'renders without error' cannot be checked." Add it to the `records` check once built.
- **R37 (Record Integrity).** P §8 freeze package: "A Record Integrity read: every finding an earlier document records as open is closed there with a cross-reference or is still open in Open_Gaps; no superseded draft sits unmarked in the world folder."
- **T16 (current pin).** In `probes`, a result file for a pin other than the current pin is a finding at freeze. P §8: "A repin after a probe run re-opens every probe class the changed records touch."
- **F9 (safety trigger).** Land Gate_Layer_Code_Review_Round1 finding 5 as written: an undetermined trigger gives `undetermined` and a non-zero exit, never `lean`.
- **T20 (thread may raise).** P §8: "A thread may recommend full validation to Mark, with the reason and the price. It never lowers what the code decides."
- **O12 (quality over stewardship).** P §9: "Budget targets plan the work. They never thin it. If staying inside a number would mean shipping work below the bar, stop at the last green checkpoint and put the choice to Mark in allowance and dollars."
- **R19 (coach verification).** P §11: "The five-world review includes a coach verification: review files exist and support what cites them; the decision log matches disk; decisions match the governing designs."
- **G9 (reasoned decisions).** P §10 rule 6: "Every decision is recorded with the real alternatives and why this one is the most defensible."
- **S19 (Doc_03 source).** P, Doc_03 row: "Candidate terms come from the Source Registry's Native rows."
- **F13 (absent voices).** P, B-7a: "`facilitator_brief.formation_limitations` names whose voices the sources structurally omit, from Doc_02 and Doc_09's Absent Stories answer (Article 20)."
- **O7 (one story).** P §10 rule 9: "A mismatch between the state file, the commits and the checkpoint artifacts is filed in Open_Gaps."
- **Z13 (System Hub).** LP "When done": "Send a summary to the System Hub thread. Do not edit the Standing dashboard files."

## Strengths of the last builds worth codifying

These worked in lpc, witt, rzg, don, gallic and cappadocian but were never written into a process document. The first seven are rows above. They are listed here because the build history is the evidence.

1. **Claims register with a halting check** (lpc, R31). It turned "caught by whichever reviewer happened to look" into a control. After it, Round 8 was the first round with no HIGH.
2. **Independent propagation verification that sweeps outward** (lpc, R32). Two passes fixed only the named instance, and the third, told to sweep, held.
3. **One state at a time during review** (lpc, R33).
4. **Structural locators, not grep hits** (lpc Round 30, R35).
5. **Fetch before judging state; one thread per world** (lpc, O18).
6. **The don and rzg Validation Layer shape.** It is category by category, with a "Named, Not Skipped" section and a "Freeze Criteria Explicitly Not Met" section. It is the natural template for the thin attestation (T22, T23).
7. **Validation against the current pin** (M2 audit; witt OG-38 re-ran M3 against the rebuilt pin, T16).
8. **Differentiation re-confirmed once a neighbour is built.** don's Validation Layer (don VL §4) confirmed its boundary with World #8 from its own side only and logged the re-check as an open item. P has no route that re-opens a built world's differentiation claim when its neighbour is later built. Proposed line for P §4: "When a new world names a built neighbour in Doc_01, log an Open_Gaps item on the neighbour to re-confirm the shared boundary."
9. **Fleet visual collision check in the M1 package.** lpc's image choice hit a binding portfolio rule found on `main` after the object was chosen: no flat written-text objects, at icon scale (lpc DL:1538). P's M1 package names "the image choice" but not a check against the fleet's existing images. Proposed line for P §1: "The image option is checked against the fleet's existing portraits and the object and silhouette rules in `Build/Ministry/Features/In-App-Icons-Graphics/`."
10. **Find deployed defects before probing** (gallic Phase Five opening). gallic read the compiled prompt in full at the pin and found a stale `[quotation]` count before writing a probe. The `deployed` check now does this mechanically.
11. **An Answer-the-Canon pass** (witt OG-17). It closed every blank canon cell with grounded records, or with an honest limit where silence is the true answer. The canon-coverage gate enforces the outcome. Naming the pass as a step between B-7a and B-8 would tell the next thread when to do it.
12. **Escalate a recurring defect class instead of chasing it** (witt OG-5, 11 rounds on Doc_03; lpc Doc_02, 30 rounds). The round cap now does this.

## Contradictions between new documents

1. **Part Eight coverage.** VS:33 says every Part Eight category needs a probe, and adds an other-tradition probe. P:905-915 and S:123-129 list a lean set without that rule, and `m10/validation.py` does not check category coverage.
2. **Probe result shape.** VS:64-66 requires "Pass criteria" and "Linked Violation Indicator(s)" columns. `Build/reference/L4-Templates/Probe_Result_Record_Template.md`, the shape `validation` reads, has neither.
3. **Register-Fidelity.** The Doc_10 template §7 has a Register-Fidelity Probe. S:102-104 says Register-Fidelity is not a probe category.
4. **Where the Deep Interview runs.** S:126 says "against the deployed site". P:916-920 says staging, through the site's own chat path.
5. **CF freeze criteria that nothing satisfies.** P:18-26 ranks CF V7.4 first. Its world-freeze list still requires ecological integrity testing, established differentiation (CF ¶573-575), the Record Integrity read (¶580) and a verified grounding-anchor paragraph in the deployed prompt (¶581). P and S provide none of the four (T22, R37, V8).
6. **Field names that the live schema lacks.** P and S name fields that `engine/m1/schemas.py` does not define: `native_measure` (P:772), `trait_rubric`, `avoid_traits`, `grounding_criterion`, `field_relations`, `conceptual_distance_note` (P:1257-1266; S:25, 31), `interaction[]` and `connections[]` (S:28), `partner_claim_id` (P:771), `alias_generic_override_note` (P:767). The live schema carries relations in `relations[]` (schemas.py:329). A builder who follows P's names fails schema validation, and S §A rows name requirements no gate can check. These are V1.9's WRS-era names, carried over unchanged.
7. **World Profile.** P:530 and S:38-42 call it generated and require it to "render without error". No builder exists (V22).
8. **Claims-register trigger.** P:467-471 applies it to "each phase document that makes claims other documents rely on". BC:51 applies it to "any document that restates claims from several sources". These are different sets.
9. **What the round counter counts.** P:281 says it counts "substantial-revision review files". `m10/rounds.py`:236-239 counts every file named Review, SpotCheck or Recheck with a round number, whatever the verdict. P:1147-1151 also leaves open whether the third substantial revision is ever reviewed before it goes to Mark. With a fourth file blocked, it is not. P should say so plainly.
10. **Freeze package in the launch prompt.** LP:183-187 hands Mark fewer items than P:1018-1032. It leaves out the freeze declaration, the M2 determination, the Deep Interview transcript, the Craft/Focus reading and the residue read.
11. **Skills not in the read list.** P:48-50 says every thread reads the vendored skills. LP:7-19, the read-first list, does not name `Build/reference/method/skills/`.
12. **Missing input as a stop.** BC:103 and CLAUDE.md say to stop for a missing input. P §1 (193-201) and P:1129 list the only allowed stops and leave it out.
13. **Label punctuation.** The header template and `reviewfile.py` use an em dash in the simulated-review label. P:1161 and LP:106 use a hyphen. The code treats them as equal, but the documents should read the same.
14. **Stale neighbour.** ARSP:31-33 still routes the largest passes to Fable, "capped at 2/week", against the spec's model routing.

## Top three by importance

F9 (the safety trigger that fails open) is the most urgent protection gap. It is left out of this ranking only because Gate_Layer_Code_Review_Round1 has already filed it with a fix.

1. **T3 with T5: lean validation no longer presses four of RCF Part Eight's categories and drops the Encounter-Success conditions.** The missing categories are Self-Referential, Source-Awareness, Scholarly-Framework and Claim-Laundering. FG ¶120 records self-narration under pressure as a systemic failure, and the lean set no longer tests for it. It also no longer tests steering or persuasion.
2. **T22: the thin Validation Layer drops Ecological Integrity and Differentiation.** Both are CF freeze criteria, and don and rzg tested both. No gate covers them. This is a gap in the decision's own list, so it needs Mark's word.
3. **R31: the claims register fell from a halting check to a document habit.** It guards against the class behind 8 of 11 HIGH findings in the strongest recent build.
