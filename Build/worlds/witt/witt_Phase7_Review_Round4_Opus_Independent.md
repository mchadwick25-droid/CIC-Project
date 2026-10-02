# Independent Review — Round 4 (Opus, targeted recheck)
## Target document: `witt_Phase7_Encounter_Ecology_Mapping_DRAFT.md`

**Date:** 2026-09-28
**Reviewer:** Claude Opus 5.5, a separate review agent working from fresh context. It did not draft, revise, or previously review this document.

**What this review is.** A targeted recheck of revision round 2 (commit `321262983`; diff `3535bfc2a..5eacb3b59`). It checks the revision against Round 3's two residuals, R3-P7-1 and R3-P7-2, in `witt_Phase7_Review_Round3_Opus_Independent.md`. It also checks every point where this document cites a score from Phase Five, against the text of Phase Five as it now stands.

**Verdict: CLEARED REVIEW, after the propagation fixes in Section 4.** Both residuals are resolved in substance. Four places still carried an earlier state of Phase Five or disagreed with the document's own §3. All four were propagation fixes, and all four were applied directly. None of them changes a finding, a verdict, or a result for any domain.

---

## Section 1 — What was checked

- The diff for this file, and the current file in full.
- `witt_Doc_09_Story_Inventory.md` §5, lines 290–313. Every string Phase Seven quotes from it was checked and is present verbatim.
- `witt_Source_Registry.md` row 49 (the 1543 treatise: "NOT VENDORED, genuinely blocked").
- Phase Five's current Summary Table, Tally, §3.2 (AN-3), §3.7 (CL-1) and Open Item 6.
- Phase Six's current B3, B5 and B7.
- `engine/m4/reports/live-turn-report-witt.json`.
- The deployed `compiled/prompt.txt` at the pin `2026-09-28T17-57-17Z`.

---

## Section 2 — Round 3 residuals, one by one

| Finding | Status | Basis |
|---|---|---|
| **R3-P7-1** (evidence-absent vs thin-but-real) | **Resolved** | §3 no longer says "all six … thin-but-real". Domain 2 (women's own voice) and domain 6 (material culture) are now classified evidence-absent, both in §3 and in §9. The domain-2 quote from Doc_09 §5 is verbatim. Domain 6 is correctly sourced to World Profile §8, not to Doc_09, which never mentions material culture. OG-50's summary says both come "per Doc_09 §5's own direct naming"; that overstates it, and it is noted in OG-51. |
| **R3-P7-2** (Phase Five's authored text used as confirmation; AN-3 contradiction) | **Resolved, after C-3 and C-4** | AN-3 is now FAIL in §3 and in §9, matching Phase Five. CL-1 is now FAIL, split explicitly, in §3, §8 and §9, matching Phase Five and the live report. §3's opening, the §2 G8 bullet and §6's opening now call Phase Five's probes authored illustration. The "Open Item 6" citation now points at text that exists again in Phase Five. Two residues were left, fixed as C-3 and C-4. |

**Cross-document consistency, checked at every citation of Phase Five's scores rather than a sample.** The citations appear in: §2 (G4, G5, G8, and the closing paragraph); §3 (all six domains); §6; §7; §8; §9 (all rows); Open Items 2 and 6; and §11. After Section 4's fixes, every one matches Phase Five's current scores:
- AN-3: FAIL.
- CL-1: FAIL, split explicitly.
- CT-1, CT-2, CT-3: PASS.
- CL-3: PASS (SECOND LOOK).
- SE-1: PASS (SECOND LOOK).
- DEV Battery: PASS, with three flagged points.
- Open Item 5: the domain-4 gap.

---

## Section 3 — Non-blocking notes (not findings)

- **The rule for splitting evidence-absent from thin-but-real is not applied evenly.** §3 defines thin-but-real as "some form of evidence exists even where a specific layer of it does not". By that test, domain 2 also has some evidence (Katharina's recorded question; the confession's defence of pastors' wives), and the missing layer is her own voice. Domain 3 has its doctrine documented, but Doc_09 §5 records "no Reformed voice at any tier". Domain 5 also has its texts unvendored. The domains are split one way here, but a case could be made the other way. Nothing in the Q1–Q5 answers or the §11 verdict turns on it: every one of these domains is "information-only, limited by design" in either category. So this is precision, not a defect. It is the kind of item the cap discipline says does not justify another round.
- **§8's heading still says "with one real exception".** The section itself now names a second one, the 1543 boundary. The "Why not much" paragraph still calls World Profile §8 "prior to any Representative-construction decision", although §8's own later paragraph says the current 1525/1543 text is a post-construction change order. Both points are carried over from Round 3's notes and are still unaddressed. They are wording, not substance.
- **Open Item 3 is still open.** Doc_04 and Doc_07 have not been read directly. The limitation is honestly disclosed and the request stands.
- **Inline "corrected … Round N" narration** must be stripped before disposition (CLAUDE.md, live/canonical surfaces).

---

## Section 4 — Cosmetic and propagation fixes applied directly (2026-09-28)

- **C-1.** Header and closing status: "(OG-41 through OG-49, and the new entry logged at the close of this revision)" → "(OG-41 through OG-50)".
- **C-2.** §9, 1525/1543 row: "content Facilitator-carried, not evidence-absent" → "content Facilitator-carried by binding disclosure (the texts themselves are also unvendored — Doc_09 §5; Source Registry row 49)". The old §9 wording was flatly contradicted by Doc_09 §5 ("no story of 1525 at all … its harsh 1525 response is not [vendored]") and by Registry row 49. It also disagreed with §3's own wording for the same domain ("not *merely* thin evidence of an absent text"). The domain's classification, thin-but-real for existence, is unchanged.
- **C-3.** §2, G4 bullet: "Phase Five's own Sustained Engagement test (Section 3.8, SE-1) confirmed G8's pacing logic…" → "…probe (Section 3.8, SE-1; authored illustrative text) illustrates…". This is the R3-P7-2 residue.
- **C-4.** §11 verdict: "Thin domains are handled by brief, honest redirection — checked against … real live output (the witt–rzg table; the live-turn report)" → "…handled by honest redirection rather than information-delivery — checked against … real live output …, with two live qualifications: on the 1543 treatise the live output holds the content boundary but narrates its own refusal and trips a 'sources' violation (Section 3; Phase Five CL-1, FAIL, split explicitly), and the witt–rzg table carries one limit-framing line Phase Six B5 flags". The old sentence cited the live-turn report as evidence of "brief, honest redirection". That same report is the evidence for CL-1's FAIL, and this document already says so in §3, §8 and §9. The verdict itself is unchanged: no drift toward content-volume. Only the evidence behind it now agrees with Phase Five.

---

## Section 5 — Verdict and disposition

**CLEARED REVIEW**, with C-1 to C-4 applied. There is no substantial finding.

This review does not change the status line. Phase Seven is last in the directed sequence and depends on Phase Five. Phase Five has not cleared (R4-1), and its exit criterion is accepted as unmet (OG-47). So Phase Seven's disposition should follow Phase Five's, not come before it.

One thing should be checked when Phase Five's R4-1 fix lands: whether any Phase Seven sentence inherits the "Turn 2 routes correctly" framing. A search was run for this, and none does today. Phase Seven does not cite the SR routing.

**Disagreement with predecessors.** One. OG-50 says both evidence-absent domains are named "per Doc_09 §5's own direct naming". Doc_09 §5 does not name material culture. Phase Seven's own text sources it correctly, to World Profile §8, so only the log entry overstates.
