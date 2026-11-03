# Spec 8: the held-out measurement (chunks D9 to D13)

**Model:** Opus for the harness (D9); in-plan helpers draft, one Opus reader per world reads (D10 to D13). No model API call.

**Purpose.** Answer one question per world: does the new path answer the visitor's question at least as well as the old engine, with rigor held and abstentions at or below 10%?

**Arms, on the frozen held-out set (Spec 5), every world.**
- A: the old engine, the live path as it is on main.
- B: the Stage 4 bound-draft path after the revert (Spec 1), flag off for passages.
- C: B with search (Spec 2), the diversity rule (Spec 4) and the before-drafting test (Spec 3) switched on.

**Harness (D9).** Builds on the shadow runner and the Step 2 harness fix. Request files per arm per question; drafts written by the voice-drafter helper; reader packets with the arm hidden; one scoring script. The run is void if the passages a helper was shown differ from those offered.

**Noise floor.** Arms A and C are drafted a second time with a fresh seed on every question. Per world, the floor is the larger of the two arms' repeat gaps in the "yes" count. A difference smaller than the floor is "even".

**Reader.** One blind Opus reader per world reads all arms of that world, the whole answer and the whole offer: answers the visitor's question (yes, partly, no); depth (rich, adequate, thin, flat); rigor (no issue, tier 3, tier 2, tier 1, as in CP.9); abstained or not. Reader disagreements between the two drafts of one arm are reported.

**Runs.** D10 lpc, ijc, cappadocian; D11 alx, pahc, don; D12 rzg, syr, desert; D13 hal, witt, gallic, then the comparison report. The allowance used is reported after each run.

**Success, set before the runs.** Per world: C's "yes" count at least A's, allowing the floor; zero tier 1 (false or invented) in C; C's abstentions at or below 10%. Depth is reported beside it, and a fall in depth counts against C. No single question is evidence.

**Test written first (D9).** The scoring script reproduces the CP.9 tables exactly from their raw files; arm labels never reach a reader packet; every arm gets the same questions in the same order; the shown-against-offered check voids a mismatched run.

**Done when.** D13's report is merged: per world, yes / partly / no, depth, rigor, abstentions for each arm, with the floor. **Cost:** none (in-plan allowance).
