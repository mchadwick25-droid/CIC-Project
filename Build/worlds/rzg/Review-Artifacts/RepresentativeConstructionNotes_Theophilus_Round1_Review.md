# Round 1 Review — Representative Construction Notes & Permanent Prompt (Theophilus)

**Documents reviewed:** `rzg_Representative_Construction_Notes_Theophilus.md`, `rzg_Representative_Permanent_Prompt_Theophilus.txt`
**Reviewer:** independent cold adversarial review, model=Sonnet, worktree-isolated, per `cic-build-cycle`.
**Date:** 2026-09-16

## Worktree note (from reviewer)

The reviewer's worktree initially contained a local `reformed-cities-doc01` one commit ahead of `origin/reformed-cities-doc01` at the time it ran, already carrying the two new files (the build thread's own commit `74078533`, pushed immediately before the review agent was launched, to ensure the isolated worktree could see the drafts). The reviewer reset to `origin/reformed-cities-doc01` and re-extracted the files from that commit before reviewing, per its own stated caution. No propagation or merge issue resulted — the reviewer's own working copy matched the build thread's actual committed draft.

## Findings, most severe first

1. **MEDIUM-HIGH — Fabricated quotation "never fully let up," attributed to Doc_08 Force 2A-4.** Used as a scare-quoted "citation" in Construction Notes §2 (Emotional Register) and §4 (Fierceness Calibration), and echoed as unquoted paraphrase in the deployed Permanent Prompt (twice). Independently re-verified by the build thread: the phrase does not appear anywhere in `Doc_08_Forces_Document.md`. Force 2A-4's actual Layer 2 text: "Rome did not simply lose this ground once and withdraw; it kept pressing at the edge of what this world had won, and every generation had to hold what the last one had claimed, not merely inherit it settled." **CONFIRMED, independently re-verified by the build thread via direct grep and read of Doc_08.**

2. **MEDIUM — Blended/paraphrased quotation "truly given to those who receive believing," attributed to Doc_05 §3.** Doc_05 §3 (line 64) actually reads: "Christ's own promise, received in faith, is truly given here — not carnally, but by the Spirit's own power, to those who come believing." The Construction Notes' quoted phrase dropped "here," swapped "come" for "receive," and presented the result in quotation marks as verbatim. **CONFIRMED, independently re-verified by the build thread via direct grep and read of Doc_05.**

3. **LOW-MEDIUM — Citation attributed to a restatement rather than the originating source.** Construction Notes §2 (Named Comparanda) cited "the single sharpest structural contrast with the sibling Lutheran Wittenberg world" to "Doc_07 §5, third finding." The phrase originates at Doc_05 §6.3; Doc_07 §5 itself explicitly discloses that it is quoting Doc_05 §6.3, and separately discloses a prior regression where this exact sentence was misattributed (also caught at this world's own Validation Layer Round 1 review). **CONFIRMED, independently re-verified by the build thread against Doc_07 §5's own text.**

4. **LOW-MEDIUM — Interaction Matrix citation attributed to Doc_07 §2I rather than its own originating source, Doc_04 §6.** Doc_07 §2I's own construction note discloses this is "carried directly from Doc_04 §6's own Interaction Matrix, not independently re-derived." Construction Notes §1 (Strand attribution) cited Doc_07 §2I alone. **CONFIRMED, independently re-verified by the build thread against Doc_07 §2I's own construction note.**

5. **LOW/COSMETIC — Truncated quotation without an ellipsis marker.** Construction Notes §3 quoted Doc_05 §11 as ending at "...none should be manufactured," when the actual sentence continues "...to fill the absence Donatism's own martyr-cult world does not share." **CONFIRMED, independently re-verified by the build thread against Doc_05 §11's own text.**

## What checked out well (reviewer's own independent verification, not taken on the documents' word)

- Permanent Prompt Section 1's mandatory museum-guide subject-of-utterance boilerplate (Template v2.4 check 5d) — diffed programmatically against the template, byte-for-byte verbatim.
- The banned analytical-distance word list (check 5) — fully clean.
- No invented biography, family, age, decade of birth, or self-narrated grammar-rule language anywhere in the Permanent Prompt.
- Word count: exactly 3,220 words, matching the Construction Notes' own claimed figure.
- The Bullinger "mirror" quote (including its disclosed OCR correction "onr"→"our") and the Sixty-Seven Articles Art. XVIII quote both checked directly against the vendored primary texts and match exactly.
- All 9 rows of the Approved Source List (Section 2A) correctly map to `Source_Registry.md` rows 1–9.
- The three mandatory vision sections are present, complete, non-placeholder, and genuinely world-specific.
- The Representative Identity and Structure Confirmation decision files are accurately represented, including the rejected "Constans" alternative and the Fidelis/Renatus unlocated-label precedent (independently confirmed against `gallic_Representative_Construction_Notes_Renatus.md`).
- Section 6 (Living Tradition) accurately restates World Profile §9 and Validation Layer §7's PENDING/preliminary status without overclaiming.
- Doc_04's gravity classifications and the G3-as-generative-logic claim are accurately characterized.
- Doc_09 story-chunk citations (`rzgstory001`, `rzgstory003`) both verified verbatim against the actual chunk files.

## Acknowledged limitation, not a defect

The reviewer could not independently confirm the three Test Exchanges in Section 4 were genuinely obtained via live model testing rather than authored after the fact — this is inherently unverifiable from outside the construction session. No internal red flags of after-the-fact fabrication were found (the content is calibrated, includes a disclosed near-miss correction, and is consistent with the document's own stated calibration risks). Not treated as a finding.

## Disposition of this review

Findings 1–2 are treated as **substantial** per `cic-build-cycle` (fabricated/blended quotations are a sourcing-fidelity defect, matching this world's own established treatment of identical defects at Doc_07 Round 1 and Validation Layer Round 1). Findings 3–5 are cosmetic citation-precision fixes. All five fixed directly in Revision 2 (see `rzg_Decision_Log.md`). A targeted Round 2 recheck follows, per this world's own established from-round-2-onward discipline.
