# CiC Build-Process Review Audit — Direct Extraction, All Six Worlds

Read directly (Decision Logs where they exist, full review-round files elsewhere) across `World-Builds/{01-Post-Apostolic-House-Church, Alexandria-Catechetical-School, Desert-Monasticism, Hieronymian-Ascetic-Literary, Imperial-Juridical-Christianity, Syriac-Christianity-Edessa-Nisibis}`. No sub-agents used for this final analysis.

**Note on this pass's own history:** this agent's first attempt returned only a status update saying it had spawned six further per-world extraction agents, rather than doing the reading itself. It was resumed with an explicit instruction not to delegate further and to read the files directly. The report below is the corrected, complete result.

## 1. Build order (evidence-based, not folder-name order)

The "World #N" label is a **Step-0 survey number**, not build-chronology — the six worlds were built in this order, per internal dates and explicit cross-references each build makes to the others:

| Order | World | Label | Core build dates | Evidence |
|---|---|---|---|---|
| 1 (tie) | Post-Apostolic House-Church | World #1 | 2026-07-07 → 07-09 | `01-Post-Apostolic-House-Church/CiC_W1_Doc05_Simulated_Review_2026-07-07.md` |
| 1 (tie) | Syriac (Edessa-Nisibis) | World #7 | 2026-07-07 → 07-08 | `CiC_W7_Decision_Log.md` (compiled retroactively 07-11 from files dated 07-07/07-08) |
| 3 | Desert-Monasticism | World #3 | 2026-07-11 | `CiC_W3_Decision_Log.md` — explicitly built to "match World #7's own testing methodology," "closing the gap...against World #7" |
| 4 | Hieronymian-Ascetic-Literary | World #9 | 2026-07-12 → 07-13 | `hal_Decision_Log.md` line 3: world-code assigned early "per the explicit process lesson that World #7's code was assigned late" |
| 5 | Alexandria-Catechetical-School | — | 2026-07-17 | `CiC_Alexandria_World_Build_Thread_Launch_2026-07-17.md`; full ground-up rebuild of pre-existing "Alexandria-v7" content (`Analysis/alex_v7_vs_current_comparison.md`) under current methodology |
| 6 | Imperial-Juridical-Christianity | — | 2026-07-19 → 07-22 | `CiC_Imperial_Juridical_Christianity_World_Build_Thread_Launch_2026-07-19.md`; first live use of the brand-new Step-0 Movement-Scope gate |

## 2. Per-document round ledger (severity as each file's own vocabulary states it)

**Post-Apostolic House-Church (24 review files, ~17 artifacts)**

| Doc | Rounds | Pattern |
|---|---|---|
| Doc_01 | 1 (no confirmation round exists) | SUBSTANTIAL — governance citation to unratified draft; unverifiable self-narrated review history |
| Doc_02 | 2 | R1 SUBSTANTIAL (4 subst.); **R2 also SUBSTANTIAL** (new regression: 3 derived index sheets not regenerated; `recalc.py` claimed but doesn't exist) |
| Doc_03 | 1 | Clean — "ready to finalize" |
| Doc_04 | 1 (7 prior rounds self-claimed, untraceable) | SUBSTANTIAL — stale workbook cells contradicting its own "finalized to match" claim |
| Doc_05 | 1 (7 prior rounds self-claimed) | 4 WFI voice-register leaks despite self-certified "clean" claim |
| **Doc_06** | **3** | R1: 7 substantial (WFI leaks, fabricated LDF quote, dropped Doc_03 item, false "agape" premise); R2: 3 chunk files found truncated after self-cert "all complete"; R3: disputed Tier-3 finding, unresolved |
| Doc_07 | 1 | COSMETIC ONLY (citation-address errors) |
| Doc_08 | 1 (no confirmation round exists) | SUBSTANTIAL-narrow — index/prose sync gaps |
| BatchFix (validation consolidation) | 2 | R1 SUBSTANTIAL (false classification precedent, unmet "Verbatim" self-cert, spliced misattributed quote); R2 all closed |
| CapsuleCore+Prompt | 1 | Qualified Pass — template gravity omitted; invented untraceable prompt detail |
| EngagementArchitecture, FormationCalibration, RepEcologyAssessment, VoiceConstruction | 1 each (no confirmation rounds) | Each Qualified Pass with Significant/Moderate findings never independently re-verified |
| Phase5 BoundaryTesting | 1 | 7/8 pass; Relational Safety fails (no Facilitator layer built yet) |
| Phase6 B1–B6 | 1 (no confirmation round) | Qualified Pass, 2 significant findings |
| Phase6 SectionA/B7 | 2 | R1 2 significant/3 moderate; R2 all confirmed fixed |

**Alexandria (28 review files, 17 artifacts)** — all dated 2026-07-17-19

| Doc | Rounds | Pattern |
|---|---|---|
| Doc_01, Doc_02, Doc_03 | 2 each | Each R1 SUBSTANTIAL (1-2 findings), R2 CLEARED |
| **Doc_04** | **3** | R1: 2 substantial (Antony self-contradiction; C4/C5 ID collision); **R2: partial fix — collision relocated, not fixed** (`Doc_04_Round2_Review.md`); R3 CLEARED |
| Doc_05 | 2 | R1: T4 tension resolved instead of held (contra Doc_04's own handoff); §6.3 fails its own "every lens" claim |
| Doc_06 | 2 | R1: 6 substantial incl. a **Related-Terms reciprocity sheet that falsely reported non-mutual chunk pairs as reciprocal** — a QC deliverable lying about its own output |
| Doc_07, Doc_08 | 2 each | Standard subst.→cleared pattern |
| **Doc_09** | 1, then a surprise 2nd round 2 days later | R1 "CLEARED (no revision called for)"; a 2026-07-19 portfolio audit re-derived it from scratch and found **2 new substantial findings R1 had missed entirely** — including a validation-table PASS row citing "the Syriac world" as a comparandum with **zero support anywhere in Alexandria's own record** (verified directly, `Doc_09_Round2_Review.md` F1). No confirming Round 3 file exists on disk. |
| Rep Phase 1, 2 | 1 each | Cosmetic only |
| Rep Phase 3 (Voice Construction) | Cleared cosmetic-only, then **reopened by the project lead himself**, not by any review round | The AI review explicitly tested for personalizing/Violation Indicators and passed it clean; Mark judged independently that the voice was "personalizing into an individual" (`Rep_Phase3_VoiceConstruction_Confirmation_Review.md`) — the review process's blind spot was caught by a human, not by re-review |
| Rep Phase 4 | 2 | 1 substantial (missing cross-build hold-open flag) |
| StoryChunks, WorldCapsuleCore, PermanentPrompt | 1 each | Minor/clean |

**Desert-Monasticism (27 review files, 13 artifacts, all 2026-07-11)**

Doc_01, 02, 03, 05, 07 = 2 rounds each (narrow substantial → cosmetic). Doc_09(abc bundle), Doc_10, WorldCapsuleCore, StoryChunks = 2 rounds each.
**Doc_04, Doc_06, Doc_08 = 3 rounds each** — the Decision Log itself names this explicitly: *"this document, alongside Doc_04, is the build's second demonstration that a revision's own claim to have completed a fix is not evidence of completion"* (Doc_06 entry) and *"this document is the third...after Doc_04 and Doc_06"* (Doc_08 entry). Four distinct **illusory-fix instances** are named by the project's own record: Doc_04 R2 (numbering-fix claimed, Section 6 silently reintroduced the old scheme), Doc_06 R2 (two "completed" claims not actually complete), Doc_08 R2 (confidence-label fix survived at a location the scan missed), Doc_10 R1 (a sentence-length fix claimed in prose but never delivered in the actual Permanent Prompt text). Live-testing also caught a fabricated leaking-jug episode and a post-430 Chalcedon anachronism on the first pass, and a "softened" anti-fabrication guard that itself failed retest before a stricter categorical version held.

**Hieronymian-Ascetic-Literary (30 review files, 14 artifacts, 2026-07-12/13)**

Doc_02–07, 09a, 09c, World Profile, Doc_10 = 2 rounds each.
**Doc_01 and Doc_08 = 3 rounds each.** Doc_01 R2 found the *fix itself* introduced a fresh chronological impossibility (Arsenius placed at Nitria in 385–386; his actual arrival is c. 394) — an illusory-fix instance the project's own review explicitly flags. Doc_08 R1 found the world's central transforming event (the 384–385 Rome crisis) had no force entry at all; R2 caught a **premature self-certification** (header marked "Approved to proceed" while §5 still said "Pending"). Doc_09c (the world's own self-validation document) drew almost entirely F-coded findings — it overclaimed the rigor of its own earlier catches and declared a live tension "closed" when two upstream documents still carried it open.

**Syriac (Edessa-Nisibis) — largest corpus (49 review files, ~20 artifacts, 2026-07-07/09, log compiled 07-11)**

Doc_02, 04, 05, 07, 08 = 2 rounds each. **Doc_01 = 3 rounds** (a fabricated "Seppälä 2023" citation caught at R2). **Doc_06 = 3 rounds plus a dedicated Retroactive Verification round** — the build thread investigated its own truncation finding, self-certified it "resolved," and was overruled: *"the re-verification described was conducted by the same party that built this document — a self-certification, not an independent confirmation... a recurring convenient explanation that only the author ever gets to verify is exactly the pattern independent review exists to catch."* This produced a **new standing project rule** (no self-certified dismissal of a blocking finding) — adopted at World #7, i.e., before Desert (#3) and Hieronymian (#9) were built, yet the identical pattern recurred in both of them anyway. **Doc_09 Story Inventory = 3 rounds** (files genuinely truncated after a "fixed" claim). **Phase Two (Formation Calibration) = 3 rounds.** Live testing initially found 2 of 3 scenarios FAIL, and a first fix-and-retest round introduced *two new fabrications* not present before the fix.

**Imperial-Juridical-Christianity (24 review files, 10 gated artifacts, 2026-07-19–22)**

**Zero of ten documents cleared in a single round** — the only world with this property. Step0, Doc_06, Doc_07, and Doc_08 each needed **3 rounds**; the remaining six (Doc_01–05, Doc_09) each needed exactly 2. Doc_07 Round 2 found a "checked directly" claim was **wrong a second consecutive time** on the same 12-term citation graph; Doc_08 Round 1's central finding was a false claim that no governing template existed for the document at all (`Doc08_Round1_Review.md`); Doc_09 Round 1's Validation Layer §9 falsely certified sibling documents as "each individually Cleared review" when neither had ever been reviewed. Several rounds carry findings of the form "status header pre-declared this round's own outcome before the round ran."

## 3. Answer 1 — Defect types recurring across multiple worlds (structural, not one builder)

Every one of the following appears in **all six worlds**, at every point in build order — this is the strongest evidence for a process-level cause:

| Defect type | PAHC | Alexandria | Desert | Hieronymian | Syriac | Imperial |
|---|---|---|---|---|---|---|
| Fabricated/misattributed citation | Doc_06 (fabricated LDF quote), FormationCalib (invented Polycarp fact) | Doc_01/Doc_03 (van den Broek/van den Hoek/Scholten inverted twice) | Doc_03 (fabricated Antirrhetikos citation), Doc_08, Doc_10 ("Abba Moses"), LiveTest | Doc_03-Addendum (fabricated Jerome quote from Ep.77.6) | Doc_01 (fabricated "Seppälä 2023"), Doc_02 (fabricated Lattke cite), Phase5/5B | Doc_01, Doc_04, Doc_06, Doc_08 |
| Self-certification not independently verified / "illusory fix" | Doc_02 R2, Doc_04, Doc_08 | Doc_04 R2 (partial fix), Doc_06 R1 (reciprocity sheet lies about itself), Doc_09 R2 | **Named explicitly 4×** in Doc_04/06/08/10 | Doc_01 R2, Doc_06 R2, Doc_08 R2 (×2), Doc_09c (whole document) | **Named explicitly**, triggered a standing project rule at Doc_06 | Doc_06 (×2 same section), Doc_07 R2 (2nd consecutive wrong "checked" claim), Doc_08 R1 |
| Internal cross-document inconsistency (numbering/ID collisions, index-vs-prose drift) | Doc_02, Doc_04, Doc_08 | Doc_04 (C4/C5 collision), Doc_06, Doc_08 | Doc_04 (numbering scheme), Doc_06, Doc_08 | Doc_04, Doc_06, Doc_08 | Doc_03, Doc_06 | Doc_02, Doc_06, Doc_07, Doc_08 |
| Template-field omission | CapsuleCore (G03 missing), VoiceConstruction | Doc_02 (Author-Gravity dimensions) | Doc_02 (Formation Narrative Sources) | Doc_05 (Representative Theological Patterns) | (less prominent) | Doc_02, Doc_05, Doc_08 (5 sections) |
| Chronological error | (minor only) | Doc_01, Doc_03, Doc_08 | Doc_01 (Theophilus letter inverted), WorldCapsuleCore, LiveTest | Doc_01 (multiple), Doc_05 (Marcella "after her own death") | Doc_01 | Doc_01 (451/476 off by 20), Doc_02, Doc_06 |
| Voice-register drift | Doc_05 (4×), Doc_06 (3×) | Doc_06, Doc_08, Rep Phase 3 (human-caught) | Doc_10, Permanent Prompt | Doc_06, Doc_08, Doc_10 (×2) | Permanent Prompt | Doc_06 (3 chunks), Doc_08 |

**Internal cross-document inconsistency (D) and self-certification failures (F) are the two dominant patterns overall.** In Alexandria alone, D accounted for 55% of all *substantial*-severity findings. The self-certification pattern is the most damning for process-design purposes: Syriac's own build **named it, diagnosed it, and wrote a standing rule against it** at Doc_06 — before Desert or Hieronymian existed — and it recurred anyway in both of them, and again in the very last world built (Imperial-Juridical), even under later rounds explicitly instructed to "trust no arithmetic," "verify every claim directly," and "give no benefit of the doubt." A written rule did not stop the pattern; it only guaranteed a later round would eventually catch it.

## 4. Answer 2 — Does the defect rate trend down over build order, or stay flat?

**It does not trend down. On the two hardest quantitative proxies, it is flat-to-worse for the later worlds.**

**(a) Share of documents needing 3+ rounds** (the cleanest severity proxy):

| Build order | World | Docs needing 3+ rounds / total gated docs | Rate |
|---|---|---|---|
| 1 | PAHC | 1 / ~17 (Doc_06) | 6% |
| 1 | Syriac | 4 / ~20 (Doc_01, Doc_06+retro, Doc_09, Phase2) | ~20% |
| 3 | Desert | 3 / 13 (Doc_04, 06, 08) | 23% |
| 4 | Hieronymian | 2 / 14 (Doc_01, Doc_08) | 14% |
| 5 | Alexandria | 1 / 17 (Doc_04) | 6% |
| 6 | Imperial-Juridical | **4 / 10** (Step0, Doc_06, Doc_07, Doc_08) | **40% — the worst of any world** |

**(b) Share of documents clearing in a single round** (0 findings needing a second look):

PAHC and Alexandria each clear roughly a third of their documents in one round; Desert, Hieronymian, and Syriac clear almost none in one round (nearly everything gets a confirmation round by design); **Imperial-Juridical clears zero of ten in one round** — worse than every predecessor, despite being built last with the most process scaffolding (a new Step-0 gate, a Source Registry, explicit "verify directly" instructions).

**What did genuinely improve, and in which specific dimension:** the *discipline of independently re-verifying a claimed fix* got measurably better and stayed better. PAHC's five Representative-construction-phase documents (Formation Calibration, Ecology Assessment, Voice Construction, Engagement Architecture, Phase6 B1–B6) each surfaced Significant/Moderate findings in their one and only review round and were never independently re-checked — the fix is simply asserted. Every subsequent world (Desert onward) treats an un-confirmed fix as not having happened, and Syriac's build explicitly turned a caught self-certification into a **standing project rule**. That rule is a genuine, durable process improvement. But the rule governs *verification discipline*, not *drafting accuracy* — and drafting accuracy (the rate at which a document needs 3 rounds because the same class of error keeps slipping past the builder) shows no improving trend and gets markedly worse in the newest world, largely because Imperial-Juridical was also breaking in a brand-new, first-time-used process component (Step 0) — adding new machinery introduced new defect surface area rather than the pipeline becoming uniformly safer with experience.

## 5. Answer 3 — Which document types most often need 2+ rounds, and why

Ranked by how consistently they exceed 2 rounds across the whole six-world portfolio:

1. **Doc_06 (Full Lexicon Development + deployment chunks) — 3+ rounds in 4 of 6 worlds** (PAHC, Desert, Syriac [+dedicated retroactive round], Imperial-Juridical), exactly 2 in the other two (Alexandria, Hieronymian). **Common thread, stated almost identically by every world's own review record:** Doc_06 requires perfect three-way correspondence between the narrative document, a set of separately-saved per-term deployment chunk files (9 to 45 of them), and a companion index workbook with several *derived* cross-reference views (reciprocity graphs, tag tables, tier tables). Every world's Doc_06 failure is some version of "the fix landed in the prose but not the chunk," "the fix landed in one chunk but not its sibling," or "the derived index view was never regenerated after a row was added" — a fan-out consistency problem across many discrete files, not a factual-content problem.

2. **Doc_08 (Forces Document) — 3+ rounds in 3 of 6 worlds** (Desert, Hieronymian, Imperial-Juridical). Same structural cause: a six-cell matrix cross-referenced against a companion Force Index workbook with multiple derived views (by-confidence, by-connected-gravity), plus a specific recurring sub-defect — a non-conforming confidence label or a missing force entry surviving one round's "complete" sweep because the sweep wasn't actually exhaustive.

3. **Doc_04 (Gravity Discovery) — 3 rounds in 2 of 6 worlds** (Alexandria, Desert), 2 rounds everywhere else, and flagged in every world as the step most prone to candidate-numbering collisions between the narrative and its companion index — the same "many cross-references, one silently un-renumbered" failure mode as Doc_06/08, just with fewer total files.

4. **Step 0 (Movement-Scope gate)** — only exists in Imperial-Juridical, but needed 3 rounds there, the same rate as that world's Doc_06/07/08. Its own review record attributes this partly to the gate's own template/procedure being new and under-specified — direct evidence that *introducing a new process component*, not builder inexperience, drove that round count.

**The common thread across all four is not subject-matter difficulty — it is companion-artifact fan-out.** Every one of the four hardest document types requires keeping a prose document synchronized with a separate structured artifact (a spreadsheet, a set of standalone chunk files, or both) that has its own derived, computed views. Doc_01, Doc_02, Doc_03, and the Representative-construction phases — which are single-document, single-artifact steps — clear in 1–2 rounds almost everywhere. The build process's recurring failure is specifically the "fix touched the place a reviewer looked, not the other three places the same fact lives" pattern, and no world's countermeasure (spot-checks, self-declared "full sweeps," even a written standing rule against self-certification) fully closed it — only an explicitly *exhaustive, not sampled* re-trace round ever did, and that had to be ordered freshly nearly every time.
