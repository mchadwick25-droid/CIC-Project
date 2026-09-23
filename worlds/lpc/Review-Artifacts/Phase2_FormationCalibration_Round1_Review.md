# Phase Two (Formation Calibration) — Round 1 Independent Adversarial Review

**Document reviewed:** `worlds/lpc/Representative/lpc_Rep_Phase2_Formation_Calibration.md`, as drafted 2026-09-23 (commit `2e19223`).
**Reviewer:** isolated subagent (general-purpose), no prior involvement in drafting this document, instructed to verify every substantive citation against primary source directly rather than trusting the document's own account of its sourcing.
**Method:** every substantive citation checked against primary source text (Doc_01, Doc_04, Doc_05, Doc_08, World Profile, Decision Log, RCF V3.2 docx extracted directly — not the docx's own description), not against the document's own summaries. Structural comparison run against `worlds/don/Representative/don_Rep_Phase2_Formation_Calibration.md`.

---

## HIGH — Fabricated/misattributed characterization of Doc_07 §2D, reintroducing a defect Phase One's own review already caught and corrected

**Location:** §1, "Formation background" bullet: *"not through a developed speculative curriculum (Doc_07 §2D finds this world concentrates its real doctrinal rigor on one recurring question, sacramental validity, 'without a broader interpretive apparatus')"*

**Checked against:** `worlds/lpc/Doc_07_Integrated_Ecology_Analysis.md` §2D, actual opening text: *"Three doctrinal bodies dominate. **Sacramental validity across the church's boundary (G6)**... **Grace and human incapacity (G7)**... **Conciliar authority (G5)**..."*

**Found:** Doc_07 §2D does not say what it is quoted as saying. It names three dominant doctrinal bodies (G6, G7, G5), not one. The phrase "without a broader interpretive apparatus" does not appear anywhere in Doc_07 §2D — it traces instead to `worlds/lpc/lpc_World_Profile.md` §3, an inaccurate gloss of §2D.

This is not a fresh error — it is a **known, previously-identified, and previously-corrected defect recurring**. `worlds/lpc/Review-Artifacts/Phase1_EcologyAssessment_Round1_Review.md` finding M3 flagged the *identical* claim in the Phase One document, in nearly identical wording, explicitly naming it as "inherited verbatim from `lpc_World_Profile.md` line 176." Phase One's own Revision Log confirms the fix was applied: *"§1.1's characterization of Doc_07 §2D is corrected to match §2D's own text (three dominant doctrinal bodies, not one)."* The Phase Two drafter drew from the World Profile's own uncorrected §3 phrasing rather than checking Doc_07 §2D directly — reintroducing exactly the error the pipeline had already caught once. This is the fabrication-class defect this project's history flags as its most serious recurring failure mode.

---

## MEDIUM — G1's connected-forces list is misattributed to include schism-testing, which it does not carry

**Location:** §1: *"that answerability does not lapse under pressure: it is tested by persecution, plague, schism, and invasion in turn, and holds (Doc_08 §5, G1's connected-forces list)"*

**Checked against:** `Doc_08_Forces_Document.md` §5, G1 entry: *"Connected forces: **1A-2**..., **1B-2**..., **1A-1** and **2A-1**..., **2A-2**..., **3A-1**..."* — no 2A-3 (schism). Doc_08 §5 connects the Donatist schism (2A-3) to G3, G5, and G6, not to G1. The §3 RICH table in this same document gets G1's force list exactly right; this §1 sentence is the one place schism is folded in and attributed to a source that doesn't support it.

---

## MEDIUM — Two World Profile section citations point to the wrong section

**Location 1:** §1: *"Doc_08 §5: 'the most densely force-connected gravity in this world,' matching World Profile §5's 'ecological hub' finding."* The "ecological hub" quote is actually at World Profile **Section 2** (G1's Brief Description, sourced there to Doc_05 §9.1); §5 is "Forces Summary" and doesn't contain the phrase.

**Location 2:** §1: *"(Doc_05 §4.1; World Profile §4.2's authority-from-below finding)."* World Profile Section 4 is subdivided 4A–4H (alphabetic); no §4.2 exists. The relevant content is at **§4F**.

Both are locatable, verifiable citation-pointer errors; the underlying substance is genuinely supported elsewhere, but a reader following the citation as given would not find it.

---

## MEDIUM — G8 (Tensional, passes all six tests) is placed in the THIN/ABSENT depth-calibration table, inconsistent with its own evidentiary weight and sibling-document precedent

**Location:** §3, THIN/ABSENT table, row "Confessor-authority against episcopal-regulated peace"

**Checked against:** `Doc_04_Gravity_Discovery.md` Candidate 8: *"passes all six as a persistent, bounded counter-force."* The THIN/ABSENT table's own header promises content that is brief/naturally-quiet — but this row's own "How it manifests" cell describes *"Datus holds both poles in earnest... and does not resolve the tension,"* which is sustained, active engagement, not brevity.

**Structural comparison confirms this is a real miscalibration:** `worlds/don/Representative/don_Rep_Phase2_Formation_Calibration.md` places its own comparable Tensional gravities (T1, T2 — weaker evidentiary bases than lpc's G8) directly in the **RICH** table. lpc's document buries a stronger Tensional gravity in THIN/ABSENT, which will under-calibrate Datus's first-phase engagement with G8 downstream in Phase Three.

---

## LOW — Historical Catalysts plague date drifts from Doc_01's own catalyst-specific figure

§2 states *"the Carthage plague (c. 249–262)"*; Doc_01 §2's own "Historical Catalysts" list (the parallel list this section's structure draws from) uses *"c. 252–253"* (the *De Mortalitate* composition date) for that list specifically, reserving "c. 249–262" for its separate "Historical Pressures" list. Minor conflation; no substantive conclusion depends on it.

## COSMETIC — Force-ID formatting

"Doc_08 §3B-2" should read "Doc_08 Force 3B-2" (Doc_08 has no numbered §3B-2 heading, only "Force 3B-2" under Cell 3B). Formatting only; substance accurate.

---

## What checked out cleanly

- **Identity Determination (§1):** does not reopen the 2026-09-15 M1 decision. Name, role label, role, and object match `lpc_Decision_Log.md` M1 exactly. No dress/age/complexion/family/anecdote invented, consistent with M1's own explicit caution.
- **RCF V3.2 quotations** (Identity Determination, Temporal Horizon, Depth Calibration, No Meta-Awareness, multi-world-address note, accessibility standard) checked against the extracted framework docx text directly — every one is accurate or a faithful paraphrase, including the exact "as the Alexandrian voice held…" example.
- **The 133-year interval reasoning:** the load-bearing quote — *"RCF Part Four's own 'natural quiet' rule is written for a thin domain within an otherwise-attested life, not a 133-year stretch inside a world's own declared span"* — is an exact match to Doc_01 §5, correctly framed as Doc_01's own disclosed extension rather than a claim that the Framework's text reaches the case directly. Sound, properly hedged, no overreach found.
- **G1, G5, G7 force-connection lists in the §3 tables** (as opposed to the §1 prose) match Doc_08 §5 exactly, including the Round-3-corrected G6↔2B-1 relationship.
- **Confidence-vocabulary usage** is present throughout §3, addressing a gap Phase One's own Round 1 review had flagged as missing in a sibling document.

---

## Disposition

**SUBSTANTIAL REVISION REQUIRED.** One HIGH finding (a fabricated-class source misattribution reintroducing a defect this project's own pipeline had already caught and fixed once) plus three MEDIUM findings that touch sourcing conclusions and a depth-calibration scope boundary. These are not wording/tone/formatting fixes — they change what specific citations actually support and how a gravity's engagement depth is scoped for Phase Three.

**CO-022 escalation categories:** none apply, confirmed independently.
- Representative identity/title: not reopened.
- Portfolio-level/cross-world: no such claim made anywhere.
- Governance/methodology: none changed.
- Unresolved tensions the pipeline can't close on its own: this is the first review round; findings above are ordinary review-catchable errors, not a pattern surviving multiple substantial-revision rounds.

No escalation is warranted; a normal revision-and-recheck cycle is the correct next step.

---

## Targeted Recheck (Round 2) — scoped to the six Round 1 fixes only, not a full re-review

**Reviewer:** a second, independent isolated subagent, uninvolved in Round 1 or in applying its fixes.
**Scope, per `cic-build-cycle`'s own discipline:** "From round 2 onward, do a targeted recheck of only what changed... not a full re-review." The reviewer was explicitly instructed not to re-verify parts of the document Round 1 already passed and the fix pass didn't touch.

Targeted recheck of the 6 fixes in `worlds/lpc/Representative/lpc_Rep_Phase2_Formation_Calibration.md`, each verified directly against primary sources (not against the Revision Log's own account).

**1. HIGH fix (Doc_07 §2D three-doctrinal-bodies claim) — VERIFIED CORRECT.** Doc_07 §2D (line 88): "Three doctrinal bodies dominate. Sacramental validity across the church's boundary (G6)... Grace and human incapacity (G7)... Conciliar authority (G5)..." and line 90: "The recurring move is the finding: this world characteristically refuses to let a single factor be decisive." Matches the fixed bullet exactly. The clause "none of the three grows into a general interpretive apparatus independent of the pastoral case that raised it" is not verbatim in Doc_07 §2D itself, but the fixed sentence cites this clause to **both** Doc_07 §2D and Phase One §1.1 together, and Phase One §1.1 (line 32) states this exact language verbatim. The dual citation is accurate.

**2. MEDIUM fix #1 (G1 connected-forces list, schism removed) — VERIFIED CORRECT.** Doc_08 §5's G1 entry (line 322): full connected-forces set is {1A-2, 1B-2, 1A-1, 2A-1, 2A-2, 3A-1}. No 2A-3 anywhere in G1's list. The fixed sentence's parenthetical subset (1A-1, 2A-1, 2A-2, 3A-1) is acceptably scoped to the "tested by pressure" claim it illustrates; the document's own §3 RICH table separately lists the full six-force set, so nothing is hidden.

**3. MEDIUM fix #2 ("the ecological hub" attributed to Doc_05 §9.1) — VERIFIED CORRECT.** Doc_05 §9.1 (line 311) heading: "9.1 What functions as an ecological hub. G1 (Pastoral Office as Flock-Keeping)." Matches. (Aside, out of scope: §1's separate "Place within the tradition's range" bullet still cited this same quote to "World Profile §5" at the time of this recheck — flagged as a minor, out-of-scope, pre-existing citation oddity, not scored against this recheck since it was not a Round 1 finding. Corrected directly afterward as a cosmetic fix, per CO-022.)

**4. MEDIUM fix #3 (World Profile §4F, not §4.2) — VERIFIED CORRECT.** World Profile §4F (lines 222–226, "4F — Social/Institutional") contains squarely authority-from-below / congregational-election-and-demand material, matching what the fix claims is there. World Profile has no §4.2 at all.

**5. LOW fix (plague/De Mortalitate dated 252–253 in the catalyst list) — VERIFIED CORRECT.** Doc_01 §2's "Historical Catalysts" list (line 46) reads "...the Carthage plague and *De Mortalitate* (c. 252–253)..." — exact match. Distinct from the separate "Historical Pressures" list (line 40), which uses 249–262 for a different list with a different convention.

**6. Structural fix (G8 moved to RICH table) — VERIFIED CORRECT.** G8 appears exactly once, in the RICH table, not duplicated in the THIN/ABSENT table. Column-count check: RICH table is consistently 2 columns throughout including the new G8 row, a valid markdown table. Substantive claim check: Doc_04's Candidate 8 entry states verbatim "Passes all six as a persistent, bounded counter-force" — an exact match.

**7. Nothing new broken — VERIFIED CORRECT.** The G2 row's "Tensional gravity G8 — see below" cross-reference still correctly points to the G8 row, now in the same RICH table. No stray pipe characters, no duplicate G8 entries, no column-count breaks introduced by the edits.

**Overall verdict: CLEARED — no substantial revision needed.** All 6 targeted fixes landed correctly and are independently verifiable against their cited primary sources. No fix introduced a new inconsistency, corruption, or broken cross-reference. One minor, out-of-scope, pre-existing citation oddity was noted (see item 3 above) and corrected as a cosmetic fix in the same pass, per CO-022's rule that cosmetic and low-severity record corrections require no further review round.
