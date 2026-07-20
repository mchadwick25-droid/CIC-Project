# CiC Build-Document Pipeline — Decision Log
**Branch: `CiC-Main-Rebuild` (off `main`). Every document in this pipeline goes: Drafted → Opus deep review (full text always shown, never summarized away) → Mark's explicit sign-off, item by item → applied. Nothing advances to the next stage without an explicit decision recorded here.**

---

## Document 1: Formation World Construction Framework (V7.3 → V7.4 DRAFT)

**Drafted:** 2026-07-04. Four additive changes: Step 2B (Doc_02B), Step 10 cross-reference, new Record Integrity Principle, new Validation Protocol Rigor subsection.

**Opus review (`Opus_Review_Construction_Framework_V7.4_DRAFT.md`):** Verdict "ratify with specific named edits." Found and — with Mark's approval — immediately fixed one mechanical defect (an accidentally-deleted "Historical Plausibility Testing" heading). Recommended 5 further edits.

**Mark's decisions, item by item:**

| Opus recommendation | Decision | Status |
|---|---|---|
| Restore deleted heading | Approved (mechanical fix, not a design call) | Applied, commit `65e71dc` |
| Owner + checkpoint for Record Integrity Principle | Approved | Applied, commit `8d5cb1e` |
| Fold in grounding-anchor mechanism (Step 2B/10) | Deferred — not rejected, not yet applied | Open |
| Add Doc_02B to Freeze Criteria | Deferred — not rejected, not yet applied | Open |
| Reframe "two failures" as systemic | Deferred — not rejected, not yet applied | Open |
| Add "fix the mechanism, not the symptom" clause | Approved | Applied, commit `8d5cb1e` |

**Then superseded by Document 2's rework (below):** the Step 2B section this document originally added was itself removed and merged into a reworked Step 2 — see Document 2. The three deferred items above still apply to the *rest* of the Framework draft (Record Integrity framing, etc.) and remain open.

---

## Document 2, attempt 1: Doc_02B Approved Source Database Template (V1.0 → V2.0 DRAFT) + Cross-World Source Registry (new)

**Drafted:** 2026-07-04. New Boundary Status axis (Native / Shared-Pan-Tradition / Comparandum-Excluded), new Cross-World Source Registry artifact, explicit Doc_01→02A→02B→03 handoff, two-tier runtime design.

**Opus review (`Opus_Review_Doc_02B_V2.md`):** Verdict **"send back for substantial rework."** Central justifying claim inaccurate (the Registry would not have caught the historical Theon defect — that was un-listed generation-time borrowing, not a listed candidate a registry lookup could flag); Boundary Status broke on real secondary/material sources; Shared status was self-launderable (circular criterion); Registry append step had no owner or scale plan.

**Mark's decision:** complete rework, scoped down. Combine Source Ecology and source-tagging into **one** Step 2 (not a separate later step), per-world only — cross-world contamination checking explicitly deferred as its own future design problem, since attempting both at once produced a design that did neither well.

**Status:** superseded by Document 2, attempt 2 (below). Both V2.0 files marked SUPERSEDED in place per the Record Integrity Principle, not deleted.

---

## Document 2, attempt 2: Unified Step 2 (Source Ecology + Source Registry) + Source_Registry_Template.md

**Drafted:** 2026-07-04, commit `2f541e5`. Merged the Framework's separate "Step 2" and "Step 2B" into one "Step 2 — Source Ecology and Source Registry" producing two co-equal outputs in one pass. New `Source_Registry_Template.md` replaces the "Doc_02B" naming and design: Boundary Status (Native/Excluded) assessed by what a source speaks *for*, never by the date scholarship was written (fixes the modern-monograph break); Exclusion Reason split into Out-of-Boundary vs. Named Comparandum (fixes the flattened-comparandum break); "Shared/Pan-Tradition" status removed rather than repaired. Updated Step 3 and Step 10 cross-references to the new terminology.

**Opus review:** Verdict **"send back for targeted rework — lighter than attempt 1, two parts should ratify outright."** Confirmed both schema fixes hold against real Alexandria data. Found three remaining problems:

1. **(Blocking) Still mis-credits itself for the Theon fix.** Claimed building ahead of a completed Source Registry "is what produced the Alexandria/Theon defect" — not accurate; Nyssa was never a listed candidate, and the mechanism that actually closed that defect was the Phase-5 grounding-anchor whitelist in the Permanent Prompt, not source tagging.
2. **(Blocking) "Built together, not deferred" still has no enforcement teeth.** Source Registry wasn't in Freeze Criteria; nothing stopped a builder from writing all of Doc_02's prose first and tagging the Registry as an afterthought within the same nominal step.
3. **(Blocking) Binary Native/Excluded couldn't represent a source native to more than one world** (Scripture being the paradigm case) — the old "Shared" status was removed rather than fixed, hiding the gap instead of closing it.

Plus one non-blocking finding: the Decision Log itself was stale.

**Mark's decision:** fix all of it, at the right level — "fix the source, not the symptom." Also resolved the multi-world-source question directly rather than engineering around it: cross-world overlap in sources is fine and expected (Scripture native to every world; Calvin using Augustine is real inheritance, not contamination) — Native means "this world's own evidence shows genuine use," not "exclusive to this world." No schema change needed once the definition is stated correctly.

**Fixes applied, commit `b6210ff`:**
- E1 — corrected the causal claim in both the Framework and the Source Registry Template: the Registry is the curated quarry; the Permanent Prompt's grounding-anchor paragraph (distilled from it at Step 10) is the actual mechanism that constrains generation-time borrowing. Stopped crediting the Registry alone for preventing the Theon/Nyssa defect.
- E2 — added a Freeze Criterion: a world is not freeze-eligible on a complete Registry alone; the deployed Permanent Prompt's grounding-anchor paragraph must be verified drawn from it.
- E3 — added a real checkpoint: "Doc_02 may not name a source in support of a specific claim unless that source has a corresponding Registry row" — in both the Framework's Step 2 text and the template's Builder Process.
- E4 — resolved per Mark's direction above; added directly to both documents.
- E6 (Chloe over-elaboration blind spot) — not yet addressed; still open.

**Status:** not yet re-reviewed by Opus against this fix round. Held for a verification pass before final ratification.

**Post-commit integrity check on `b6210ff` (caught before Opus re-review, not after):** verifying this commit directly against the branch tip (not the drafting copy) found that `Source_Registry_Template.md` had been silently truncated mid-word during the commit — cut off partway through the Builder Process step 1, before the E3 checkpoint sentence and the entire "How Phase 5 and runtime use this document" section. The Framework docx was independently verified complete (all E1-E4 phrases present via pandoc extraction). Fixed by restoring the full intended text directly against the git clone and re-verifying line-for-line before committing — see the fix-up commit immediately following `b6210ff`. Noting this here rather than quietly re-committing without a record: this is exactly the kind of un-tracked partial-apply the Record Integrity Principle exists to catch, and it happened inside the very commit that introduced that principle's own enforcement teeth.

---

## L1-L3 Document Consistency Review — Step 2 / Source Registry redesign carried into the surrounding system

**Requested:** 2026-07-04, by the project lead, after the E1-E4 fix round above: "look through the level 1-3 documents and have opus do a review of document consistency and flow to support the additions and changes we have made to step 2 of the build process."

**Opus review (`L1-L3 Document Consistency Review`, full text presented to the project lead in full, unedited):** Verdict **"ratify with named fixes -- substantive, not cosmetic, two of them load-bearing."** Six findings, four blocking:

1. **(Blocking, most severe)** The "grounding-anchor paragraph (Template Section 3)" reference in both the Source Registry Template and the V7.4 Framework was factually wrong -- Section 3 is "Voice and Reasoning Mode" and never contained this mechanism. Verified against all five deployed prompts (Theon, Chloe, Kimon, Cordus, Eumathios): the mechanism is real and consistently applied, but existed only as hand-replicated convention, never a defined, required element of the Permanent Prompt Template.
2. **(Non-blocking)** L2A Architecture Map and System Level Map still described Step 2 as producing only Source Ecology; an orphan "Source Metadata Framework" deliverable had no owning document.
3. **(Non-blocking)** Forces Framework's Step 2 heading and output line don't mention the Registry; its required "transmission history" dimension isn't tied to the Boundary Check.
4. **(Blocking)** Constitution Article 31's external-human-review requirement covers "Source Ecology, Gravity Discovery, and major historical claims" but is silent on the Source Registry's boundary judgments -- exactly the provenance calls whose failure produced the original defect.
5. **(Blocking)** The Formation World Blueprint and Formation World Template -- the actual per-world deliverable structures a builder fills out -- had a Source Ecology section and no Source Registry section.
6. **(Blocking)** The Representative Construction Framework (L3C, governs Step 10/Phase 5) never mentioned the Source Registry, Approved Source List, grounding-anchor paragraph, or Permanent Prompt content pipeline -- the causal chain the redesign draws breaks at the exact handoff where the mechanism is supposed to get built.

Plus two additional findings from full reading: (A) no formal Change Order existed for a redesign of comparable weight to CO-014; (C) the superseded Doc_02B file's SUPERSEDED banner needed a confirmation check.

**Project lead's decision on Finding 4 (the one governance-level item):** hold, do not edit the Constitution in this pass -- log it as a flagged open item, consistent with how CO-014 handled the Article 23 tension (flag, don't unilaterally edit a founding document). All other findings approved for direct implementation.

**Fixes applied, commits `ac5029e` through `dd56512`:**
- New mandatory Section 2A (Approved Source Anchoring) added to the Permanent Prompt Template (v2.1 -> v2.3), with builder guidance, fill-in scaffolding matching the deployed convention, and Theon's field-tested paragraph as worked example. Sections 3-8 deliberately not renumbered.
- Wrong "Section 3" pointers corrected to Section 2A in the Source Registry Template and the V7.4 Framework's Step 10 text.
- Finding 3's transmission-history cross-reference added to the Source Registry Template's Boundary Check paragraph.
- L2A Architecture Map and System Level Map updated to show the Source Registry as a co-equal Step 2 output; orphan "Source Metadata Framework" deliverable resolved.
- Source Registry section added to the Formation World Blueprint V7.3 (heading renamed "3. Source Ecology & Source Registry (Doc_02)") and the Formation World Template V1.5.
- Source Registry added as a required Step 10 input, and a new "Approved Source Anchoring" subsection added to Part Five (Voice Construction), in the Representative Construction Framework V3.2.
- New "Approved Source Anchoring" subsection added to Section 2 of the Representative Construction Notes Template (v2.1 -> v2.2), giving the Freeze Criterion a documented artifact to check against.
- CO-016 filed in the Change Orders Register (V1.13), enumerating this entire fix set.
- Doc_02B's SUPERSEDED banner confirmed intact (Additional C) -- no action needed.

**Open item (Finding 4):** amend Constitution Article 31's first bullet to read "Source Ecology **and its Source Registry**, Gravity Discovery, and major historical claims," mirrored in the Blueprint's Article-31 validation question -- held pending a separate governance-level decision by the project lead, not applied in this pass.

**Status:** all methodology-level (L2/L3) fixes committed on `CiC-Main-Rebuild`. Not yet re-reviewed by Opus against this fix round -- held for a verification pass, same discipline as the E1-E4 round above, before this filing and CO-016 are considered closed.

---

## L1-L3 Consistency Fix Round — Verification Review and Closure

**Requested:** 2026-07-04, by the project lead: "yes and make it a focused review not only on fixes but the impact of the changes and ensure nothing was lost in the changes." A deliberately different kind of review from the discovery pass above -- not looking for new design problems, but verifying the agreed fix set (commits `ac5029e` through `f7ded16`) was applied correctly, completely, and without collateral damage.

**Opus verification review (full text presented to the project lead, unedited):** Verdict **"ready to be considered closed."**

- **Part B (checked first, per the project lead's stated priority): nothing was lost.** Every one of the eleven touched files was diffed old-vs-new (docx via paired pandoc text extraction, md/txt via direct git diff). All differences are intentional additions or matched substitutions -- no paragraph, heading, table row, or brace/bracket count was dropped, corrupted, or silently truncated. The two line-count cases flagged for special scrutiny (System Level Map 443->443 lines; Construction Framework 2083->2084 lines) were both independently explained and cleared: a widened table cell and a longer corrected cross-reference, not truncation. No repeat of the earlier `Source_Registry_Template.md` mid-word truncation incident.
- **Part A: all six findings, plus CO-016 and the Decision Log entry, independently confirmed correctly and completely applied**, including verifying that dependent fixes actually resolve (the Section 3 -> Section 2A pointer corrections were checked against Section 2A's actual heading text, not assumed).
- **Part C (impact assessment):** four items checked fine as-is (version-numbering practice is consistent with project precedent; the Blueprint heading rename doesn't break any cross-reference repo-wide; cross-document terminology and file paths for the Registry mechanism are fully consistent; CO-016 and the Decision Log hold themselves to the project's own anti-overclaiming standard). One minor, non-blocking item: `Archive/Superseded-Housekeeping/L3B_duplicate_Representative_Construction_Notes_Template.md`, a stale v1.0 duplicate of the just-updated template, had no in-body SUPERSEDED banner (unlike the Doc_02B and Cross-World Registry superseded files).

**Project lead's decision:** apply the one follow-up item and close the filing.

**Fixes applied, this pass:**
- Added a SUPERSEDED banner to `Archive/Superseded-Housekeeping/L3B_duplicate_Representative_Construction_Notes_Template.md`, pointing to the live v2.2 template.
- CO-016 in the Change Orders Register updated from IN PROGRESS to RESOLVED, with a new V1.14 version-history entry recording the verification review's outcome.

**Status:** this fix round is closed. The Constitution Article 31 recommendation (Finding 4) remains open and tracked separately -- its resolution is a distinct governance-level decision for the project lead, not affected by this closure.

---

## Finding 4 (Constitution Article 31) — resolved

**Requested:** 2026-07-04. Mark asked what the suggested Constitution change actually was and whether it genuinely needed to be constitution-level. Given the full text of Article 31 and Article 37 (Constitutional Evolution Principle) to read directly, the honest answer offered was: probably not -- Article 31 already says "major historical claims," which arguably already covers the Source Registry's boundary judgments in substance; and Article 37 explicitly bars revising a Level 1 document because of a downstream artifact's specific design, which is exactly the shape of the original justification for this edit. The alternative offered: leave the Constitution untouched and instead make the Framework/Blueprint explicit that "major historical claims reviewed under Article 31" includes the Registry's boundary judgments -- mirroring how Article 29 handles Living Tradition Status ("the method of confirmation is governed by the build documents; the requirement that it occur is constitutional").

**Mark's decision, considered and explicit:** amend the Constitution anyway. "it fits and being constitutional will drive the rigor we are wanting." This is read as a deliberate application of Article 37's own governance-gap ground for revision ("project maturity reveals a gap in this Constitution's own governance coverage") rather than an exception to Article 37 -- the project lead's judgment that the addition is a genuine, if narrow, gap in the Constitution's own coverage, and that stating it at the constitutional level is itself the intended effect (driving external-review rigor), not incidental to it.

**Applied:**
- Constitution Article 31, first bullet: "Source Ecology, Gravity Discovery, and major historical claims" -> "Source Ecology **and its Source Registry**, Gravity Discovery, and major historical claims." Constitution version bumped 2.2 -> 2.3.
- Mirrored in the Formation World Blueprint's Article 31 validation question (Section 17, External Scholarly Review).
- Filed as CO-017 in the Change Orders Register, with the full reasoning on both sides (the original hold-don't-edit recommendation and the project lead's override) recorded in its Rationale column, per this project's "nothing hidden" standard -- the record shows the tension was surfaced and consciously resolved, not skipped.

**Status:** Finding 4 is closed. No open items remain from the L1-L3 consistency review.

---

## Document 4: Bringing forward general methodology from CiC-Fable-Experiment (CO-018)

**Context:** after merging `origin/CiC-Main-Rebuild` into `main` and branching `CiC-L1L3-Foundation` (Levels 1-3 only, no world-specific work), the project lead asked whether anything good and non-world-specific should also be pulled in from `origin/CiC-Fable-Experiment` — a separate, independent branch (184 commits, never merged into `CiC-Main-Rebuild`) that did substantial earlier development, including building and validation-testing all five of the project's existing Representatives.

**Investigation:** every L1-L4/Project-Reference file was diffed between the two branches. For the Constitution, Architecture Map, System Level Map, Blueprint, Template, and L3C Framework, the only differences were this lineage's own Source Registry work (CO-016/017) — Fable-Experiment simply didn't have it yet. Fable's own "V7.4" Construction Framework (no `_DRAFT` suffix) turned out to be an *earlier* snapshot, missing the Fix-the-Mechanism and Record Integrity principles this lineage later added — not a more-finished version. Two items were genuinely new and worth evaluating: the Representative Permanent Prompt Template's subject-of-utterance rule (v2.3-v2.5 on Fable), and Facilitator-Governance, which existed on both branches but at different versions (this lineage: V3.4; Fable: V3.6, via Fable's own CO-018/CO-019 — a colliding but unrelated numbering scheme on that branch).

**The project lead's specific question:** whether the Facilitator-Governance V3.4->V3.6 work was a symptom-level fix patching the five existing built worlds into compliance, or a genuine system-level addition — and to check it against this lineage's own Step 2/Source Registry rework for conflicts.

**Finding:** genuine system-level work, arrived at in two steps. Fable's CO-018 discovered (via independent fresh-context testing on both Theon and Cordus) that the subject-of-utterance rule — a Representative-prompt-level text fix — did not reliably hold under sustained adversarial pressure, and confirmed this was systemic to the we-voice design (CO-014 on that branch), not a defect in any one world's prompt. CO-018's first fix (single-call Facilitator routing) was itself found insufficient under live-encounter testing. CO-019 is the real architectural fix: a decoupled classify-then-route-then-generate pipeline where a narrow classifier intercepts construction/grammar questions before any Representative is invoked at all — tested at 10/10 correct across adversarial batches, making the failure structurally impossible rather than dependent on prompt wording. This governs the Facilitator layer, which sits above every world, not any one world's prompt — genuinely non-world-specific. No conflict against Step 2/Source Registry: they solve different problems (Source Registry governs *what content* a Representative draws on; this governs *who answers* when a question is about the system's own construction rather than the world's content).

**Caveat, not hidden:** Fable's own Change Orders Register still marks both CO-018 and CO-019 as IN PROGRESS, with explicit unexecuted follow-ups (audit Kimon's/Eumathios's prompts under the same lens; larger-scale live-encounter validation; latency/cost evaluation of the three-call pipeline). This was validated through that branch's own empirical testing protocol, not the Opus-adversarial-review-plus-explicit-sign-off discipline this lineage has used for CO-016/017.

**Project lead's decision:** bring forward Facilitator-Governance V3.4->V3.6 in full, and the Permanent Prompt Template's subject-of-utterance rule (Section 1 backstop paragraphs, v2.3-v2.4) — but explicitly *not* Fable's v2.6 grounding-anchor paragraph (Section 3), since this lineage's own Section 2A already governs the same generation-time content-borrowing risk via the more rigorous, Opus-reviewed Source Registry mechanism. Bringing both forward would have created a duplicate, conflicting mechanism for the same problem.

**Applied, on `CiC-L1L3-Foundation`:**
- `L3D-Encounter-Methodology/CiC_L3D_Facilitator_Governance_V3.4.docx` replaced with Fable's V3.6 (verified content-preserving via full V3.4->V3.6 plain-text diff before applying: the new Section 10 Self-Narration signal and Section 15 Known Limits entry are clean insertions, and Section 12's Frame-Breaker paragraph was expanded in place -- all of its prior text retained, with new examples and cross-references woven in, not merely appended alongside it. Correction, caught by the Opus review of this integration: an earlier version of this entry claimed 'no removed or altered content beyond the version-number header,' which was not literally accurate -- Section 12's wording did change, even though no governance was lost. Corrected here per the Record Integrity Principle.).
- `L3B-World-Build-Methodology/Representative_Permanent_Prompt_Template.txt` v2.3 -> v2.4: Section 1 backstop paragraphs (museum-guide worked example) spliced in at the same location as Fable's version; new Final Assembly Instruction check 5d added, cross-referencing both 5a (existing build-time QA check for self-narrating residue) and the Facilitator-Governance routing mechanism as complementary, not redundant.
- CO-018 filed in the Change Orders Register (this lineage's numbering, distinct from Fable's own colliding CO-018/019), status APPLIED, not yet independently reviewed.

**Opus review (`Opus_Review_CO018_Integration_2026-07-04.md`):** Verdict PASS-WITH-FIXES. Confirmed the system-vs-symptom judgment holds, the exclusion of Fable's v2.6 grounding-anchor paragraph is correct (Section 2A's own wording verifiably subsumes the redirect-specific case it was built for), and L3C already anticipates the Facilitator-routing rule rather than contradicting it. Found one Blocking citation error (fixed, see below) and one Record Integrity accuracy issue (fixed, see above). Two non-blocking follow-ups recommended, not applied in this pass: (1) L3C's Self-Referential Probes section has a stale carve-out gap — it exempts relational-safety Facilitator handoffs from its scoring but not the new construction/grammar frame-break interception, creating two different tellings of who answers "what are you" questions; recommended as its own follow-up CO, not bundled into this one. (2) The three-call pipeline's latency/cost tradeoff is a genuinely orphaned open item — not gating this methodology integration, but should gate any future implementation/deployment on this branch, since no existing gate currently captures it.

**Fixes applied, this pass:** corrected the Constitution citation in `CiC_L3D_Facilitator_Governance_V3.6.docx` (Section 10 and the Constitutional Grounding note) and in the CO-018 register entry — the fabrication prohibition is Article 28 alone (Anti-Fabrication Prohibition), not "Article 3, Article 28"; "TC-001" has no referent in the Constitution and was dropped. Both had been inherited from Fable-Experiment's own filing without independent verification against this lineage's Constitution — exactly the kind of unverified cross-reference CO-016/017 exist to catch. Corrected the Decision Log's "additive-only" claim above to accurately describe Section 12 as a content-preserving in-place expansion, not an unaltered original.

**Status:** APPLIED and reviewed. The two non-blocking follow-ups above (L3C probe-scoring carve-out; latency/cost open item) remain open, tracked here, not silently dropped — neither gates closure of CO-018 itself.

---

*This log is itself a living document — append new entries per document, never edit past decisions after the fact. If a decision is later reversed, record the reversal as a new entry rather than rewriting the old one.*

## Document 5: Movement-Scope Principle — defining what makes a movement "Christian" for project scope (CO-019)

**Context:** the Constitution states the project's subject is "the movements of Christ's Church" (Article 4, Convictions 1 and 3) but never defines what qualifies as such a movement. The project lead identified this as a genuine credibility gap for pastor/seminary-level users and asked for a defensible boundary — explicitly not as an influence on how a selected world represents itself, but as a scope-eligibility test for which movements are considered at all.

**First attempt, reverted:** a draft built from the earliest New Testament confessional fragments (1 Cor 15:3-7 and similar pre-literary creedal material) as an original synthesis. The project lead rejected this specifically — he did not want the project inventing its own theological framework, he wanted an existing, majority-recognized standard.

**Research finding:** the Nicene-Constantinopolitan Creed (381) has, by a wide margin, the broadest current cross-tradition institutional recognition of any single standard — confirmed via 2025's 1700th-anniversary statements from Pope Leo XIV ("the common profession of all Christian traditions"), the Vatican's ecumenism office, and Orthodox dialogue leadership, plus a November 2025 AP/Religion News Service piece describing Catholic/Orthodox/most historic Protestant acceptance and evangelical statements of faith largely agreeing with it, naming Jehovah's Witnesses and Latter-day Saints as the explicit modern exceptions.

**Draft, round 1, sent to Opus:** a Nicene Confessional Scope Principle testing a movement's own confession against the Creed's doctrinal content (not conciliar authority), with pre-Nicene continuity and hand-selected-exception provisions. Opus verdict: PASS-WITH-FIXES. Two blocking findings (conditional): the draft leaned on a "Step 0" pre-construction screening stage that did not exist anywhere in the Construction Framework; and the draft's "beliefs not authority" framing under-described what it was doing (a real doctrinal floor) and was silent on how the standard applies to contemporary movements specifically. Five should-fix findings: the "proto-orthodox" scholarly term was used normatively while claiming to be purely descriptive (inverting Bart Ehrman's own non-normative use of the term); the hand-selected-exception mechanism had no bound on how much divergence could be waived or how many exceptions could accumulate; unaddressed interactions with Articles 20/21/23; a placement/band mismatch (a foundational scope principle drafted as a very late-numbered Article); and the justification should be grounded in Article 37's "governance gap" language rather than "credibility."

**Response, round 1:** split into two documents (a short Constitutional principle; a separate, detailed Step 0 methodology document carrying the mechanics) and, at the project lead's specific instruction, added a plain-denial vs. reinterpretation distinction — naming "progressive Christianity" explicitly as a non-monolithic hard case, assessed at the specific-candidate level rather than by label, since the movement spans both sides of the floor.

**Draft, round 2, sent to Opus:** the short principle folded directly into Constitution Article 4 itself (at the project lead's instruction), avoiding any renumbering, paired with the Step 0 methodology document. Opus verdict: PASS-WITH-FIXES. Two blocking-conditional findings: the "Step 0" delegation still pointed at a step that didn't exist in the repository (the same failure as round 1, now embedded in the Constitution itself); and folding new content into "The Five Convictions" Article risked being misread as a sixth binding conviction, given the Article's own opening language ("no revision, addition... may contradict them"). Five should-fix findings: A3's reinterpretation test didn't cover the plain-denial case (the JW/LDS examples the project itself had researched); the hand-selected mechanism had no aggregate cap, only per-instance bounds; the floor's content was now stated twice, in slightly different technical precision, across two documents at two authority levels (a drift risk); the creed rendering was still unverified against a critical source, exactly as its own drafting note had flagged; and naming living individuals (Cupitt, Spong) as reinterpretation examples was flagged as a deliberate-not-accidental choice to confirm.

**Fixes applied before filing:** verified the creed's precise wording against the ELLC (English Language Liturgical Consultation) 1988 ecumenical English text (the standard used across Anglican, Lutheran, Methodist, Presbyterian, and Reformed bodies), correcting the earlier hand-drafted "maker of all things" to the accurate "maker of heaven and earth, of all that is, seen and unseen," and "of one Being with the Father" in place of the vaguer "fully divine." Added an explicit "this is not a sixth conviction" structural disclaimer to the Article 4 section, with its own heading distinct from the "Conviction N" pattern. Made Constitution Article 4 the sole authoritative source of the floor's content; the Step 0 Methodology document's Section A now explicitly defers to it rather than restating it. Added an explicit plain-denial paragraph to Step 0 A1, naming Jehovah's Witnesses and Latter-day Saints directly as the ordinary case (worded as description of confessional difference, not a value judgment), separate from A3's harder reinterpretation test. Added a concrete numeric cap to the hand-selected mechanism (flagged for external review at 5 total or 10% of the floor-clearing pool per phase, whichever comes first — a stated default, adjustable by the project lead). Cupitt/Spong naming was reviewed and kept as a deliberate, defensible choice (both publicly and extensively self-described their own positions; the framing explicitly disclaims ruling on any movement as a whole).

**Applied, on `CiC-L1L3-Foundation`:**
- `L1-Foundation/CiC_L1_Constitution_V2_2.docx`: new closing section added to Article 4, after Conviction 5, before Article 5 (Governing Constraint on All Versions). No renumbering of any other Article.
- `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4_DRAFT.docx`: new Step 0 stub added immediately before "Part I — World Identification & Boundaries" (which is where Step 1 begins). No renumbering of Steps 1-10.
- `L3B-World-Build-Methodology/CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx`: new file, Sections A (Movement-Scope Eligibility: the floor by reference, pre-Nicene continuity, contemporary/interpretive-fidelity test, bounded hand-selected inclusion, Article 20/21/23 interactions) and B (the original five-criteria seed-screening process: Sourcing, Ecology, Uniqueness, User Needs, Scale — unchanged from the earlier draft).
- CO-019 filed in the Change Orders Register, status APPLIED.

**Status:** APPLIED, following two full Opus adversarial review rounds with all findings addressed, on the project lead's direct sign-off. No further review round requested before application.

---

## Document 6: Onboarding Framework updated for Step 0 / Movement-Scope Principle (prep for Coach 3 thread)

**Context:** the project lead asked what else is needed before spinning up a new coaching thread ("Coach 3") to run Step 0 for real and build the first world step-by-step, with per-step review and Opus review on substantial changes.

**Finding:** the project already has a rigorous, existing onboarding mechanism for exactly this — `CiC_L2B_World_Build_Onboarding_Framework` (Part Two, Rounds One through 3B), each round pairing a document reading list with verification questions the project lead confirms before the next round is sent. This is precisely the "questions to make sure understanding" mechanism the project lead was describing; it did not need to be invented, only updated, since it predates this session's Movement-Scope Principle and Step 0 work.

**Applied, on `CiC-L1L3-Foundation`:**
- Round One (Constitutional and Foundational Layer) gained a Question 7 testing understanding of Article 4's new closing section — naming it, stating what it governs, its doctrinal source, and why it is explicitly not a sixth conviction. The "all six questions" gate text updated to "all seven."
- Round Two (Build Methodology Layer) gained the Step 0 Methodology document to its reading list (now 9 documents, was 8) and a Question 9 testing understanding of Step 0 as a phase-level (not per-world) gate, the floor's source and belief-vs-authority framing, the two exception paths and their bounds, and where the floor's authoritative content actually lives (Constitution, not Step 0). The "all eight questions" gate text updated to "all nine," including a missed instance in the round's loading instruction paragraph.
- Framework's internal version bumped from 1.2 to 1.3 (filename unchanged, consistent with the project's existing filename/internal-version cosmetic drift already noted for the Constitution).

**Not done, flagged as an open question for the project lead rather than decided unilaterally:** the Phase Status document (`CiC_L2C_Phase_Status_V1.2.docx`) still carries a World Status Dashboard listing four not-yet-started worlds by name — Early Communal, Desert Christianity, Nicene-Cappadocian, and Early Latin — carried forward from before this session's Step 0 rebuild. This creates a real tension with Step 0's own design intent (a fresh, unbiased survey producing seeds without a pre-existing thematic sketch, per the Step 0 draft's own "what this does not do" section and the project lead's original concern about boundary work being biased by a name chosen in advance). Whether Coach 3's Step 0 run should proceed as a genuinely blind survey (potentially arriving at a different candidate list than these four) or treat this dashboard as a reference starting point is a decision for the project lead, not something resolved here.

**Status:** onboarding documents updated and ready. No Change Order filed for this entry — it is a direct, mechanical extension of CO-019's own content into the existing onboarding apparatus, not a new architectural decision.

---

## Document 7: Phase Status World Dashboard cleaned of pre-named candidates (prep for Coach 3 / blind Step 0)

**Context:** the project lead asked to clean the Phase Status World Status Dashboard, which listed four not-yet-started worlds by specific name (Early Communal, Desert Christianity, Nicene-Cappadocian, Early Latin) — a direct carryover from the pre-Step-0 process the project lead already identified as having gone "too deep in unaligned values." Leaving these names in place would bias Coach 3's Step 0 survey exactly the way Step 0 was rebuilt to avoid.

**Applied, on `CiC-L1L3-Foundation`:**
- Phase Status Section 2 (World Status Dashboard): removed the four named "Not started" rows and replaced them with a single generic row — "Additional Ancient Church worlds (c. 30-700 CE) — not yet identified," code "TBD (Step 0)." Alexandria's row is untouched (it is a real, built asset — V7 complete, in production — not a pre-named future candidate, so it does not create the bias problem the other four did). The c. 30-700 CE date range is a proposed default, not sourced from an existing document (none was found defining "Ancient Church" with specific dates — Phase Structure uses the term without a date range); flagged for the project lead's adjustment if a different range is intended.
- Phase Status Section 5 (Cross-Build Constraint Status): the existing "known high-blur pairings" table references two of the now-removed world codes (desert, cappadocian) directly. Rather than deleting this analysis outright, added a note marking it stale and pending re-derivation once Step 0 produces its actual seed list — the vocabulary/figure-overlap concerns it names (shared use of Origen, theosis, apatheia, Nicene confession, ascetic vocabulary) may still be useful as worked examples of what cross-world blur looks like, but the specific pairings assume a world list Step 0 may not reproduce.

**Status:** applied on the project lead's direct instruction. No Change Order filed — this is direct cleanup of stale status content, not an architectural decision.

---

## Document 8: Phase Status fully blanked of world names, including Alexandria (correction to Document 7)

**Context:** Document 7 kept Alexandria's row in the World Status Dashboard, reasoning it was a real built asset rather than a pre-conceived candidate. The project lead corrected this: for this branch and this fresh restart, no world names should appear at all — not even Alexandria's. He will add back whatever he decides is worth carrying forward, if he feels a need to, once Step 0 has actually run.

**Applied, on `CiC-L1L3-Foundation`:**
- Section 2 (World Status Dashboard): now a single row, "None tracked on this branch — search restarting from scratch via Step 0."
- Section 4 (Deployment Gate Status): Alexandria's specific gate table (Checkpoint One, TC-001 Fabrication Remediation, Article 29 Living Tradition Status naming "Coptic Orthodox," Article 31, Deployment Outputs) cleared to "None tracked."
- Section 5 (Cross-Build Constraint Status): the known high-blur pairings table (alex+desert, alex+cappadocian, desert+cappadocian, naming Origen, theosis, apatheia, Nicene confession, ascetic vocabulary, Basil's Rule) cleared to "None tracked — pending Step 0's seed list," along with the standalone "Alex-Desert cross-build provisional constraint: Active" line.
- All surrounding narrative notes updated to match — no residual references to Alexandria, desert, or cappadocian remain in this document.

**Not destroyed:** Alexandria's actual build content, gate history, and cross-build analysis are not deleted from the project — they live on `main` and other branches where World-Builds content still exists; this branch never had that content in the first place (removed when `CiC-L1L3-Foundation` was created). This is a display/tracking-scope decision for a fresh-start branch, not a loss of the underlying work.

**Status:** applied on the project lead's direct instruction. No Change Order filed.

---

## Document 9: Architecture Map corrected — confidence vocabulary and story-tier conflicts were stale

**Context:** while onboarding through Round One documents in full (as part of preparing to run Step 0 for real), the Architecture Map's Layer 4 maturity note was found to still describe the confidence-vocabulary (three-level vs. five-level) and story-tier (Attributed Tradition vs. Hagiographic Narrative) conflicts as open, pending project-lead decision and a Construction Framework update.

**Finding:** both are already resolved in the Construction Framework V7.4 DRAFT on this branch — verified directly, not assumed: the five-level vocabulary (Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin) is fully present, and Tier 3 is defined as Attributed Tradition with Hagiographic Narrative as a named sub-type, matching the reconciliation option the transition-era Holding Document had itself proposed.

**Applied, on `CiC-L1L3-Foundation`:** corrected the Architecture Map's Layer 4 maturity note to state both are resolved, with the verification method named. Flagged, not fixed here: the Constitution's own two inline notes ("the Construction Framework must be updated...", after Articles 17 and 19) are themselves now stale for the same reason, but touching the Constitution is a higher-stakes edit than this Level 2 correction — left for a future pass rather than bundled in here.

**Status:** applied on the project lead's direct instruction. No Change Order filed — stale-reference correction, not an architectural decision.

---

## Document 10: Stale "Article 3, TC-001" citation corrected in two more documents (same defect as Document 4's Facilitator-Governance fix)

**Context:** while reading the Construction Framework (V7.4 DRAFT) and the Representative Construction Framework (V3.2) in full during Round Two of coach onboarding, both were found to still cite "(Constitution Article 3, TC-001)" / "(Constitution Article 3; TC-001)" when grounding the prohibition on inventing Representative biography. Document 4 above already established that "TC-001" has no referent anywhere in the Constitution and that the correct, sole grounding is Article 28 (Anti-Fabrication Prohibition) — that finding was applied to Facilitator-Governance V3.6 at the time, but evidently not propagated to these other two documents, which carried the same stale citation inherited from the same source.

**Finding:** confirmed directly against the Constitution (not assumed) — Article 3 (Formation-World Principle) does not address fabrication or invented biography at all; Article 28's Anti-Fabrication Prohibition is the correct and only constitutional grounding for the claim being made in both places ("never from invented biography" / "never from fabricated life-detail").

**Applied, on `CiC-L1L3-Foundation`:**
- `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4_DRAFT.docx` (Step 10 text): "(Constitution Article 3, TC-001)" → "(Constitution Article 28, Anti-Fabrication Prohibition)."
- `L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx` (Part Ten, second governing commitment): "(Constitution Article 3; TC-001)" → "(Constitution Article 28, Anti-Fabrication Prohibition)."
- Both edits verified content-preserving before and after applying: paired pandoc plain-text diffs of each file (old vs. new) show exactly one changed line per file, with no other paragraph, heading, or content altered. Paragraph counts unchanged (718→718 and 213→213) per the pack validator.

**Operational note, recorded for the project record:** this fix was drafted and validated against the read-only clone at `/tmp/pilot-setup` (filesystem-owned by a different user than the session's shell user — no write access, no sudo available in that sandbox). Rather than silently working around this or applying the fix somewhere the project lead couldn't see, the blocker was surfaced directly and the project lead chose to have a new git worktree for `CiC-L1L3-Foundation` created inside the actual connected `CiC-Project` folder (at `.worktrees/CiC-L1L3-Foundation`, fetched read-only from the `/tmp/pilot-setup` clone's identical git history — same commit hashes, verified). `main` and its pre-existing uncommitted changes in the primary `CiC-Project` checkout were not touched. This commit is therefore landing in a new location relative to prior entries in this log; future coach threads should locate the branch here going forward unless the project lead relocates it again.

**Status:** applied on the project lead's direct instruction. No Change Order filed — stale-reference correction, not an architectural decision, consistent with Document 9's precedent.

---
