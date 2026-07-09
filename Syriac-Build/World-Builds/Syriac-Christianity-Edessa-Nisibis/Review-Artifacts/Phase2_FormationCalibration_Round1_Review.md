Simulated review — informational only, not an Article 31 substitute.

# Independent Adversarial Review — Round 1
## Syriac_Phase2_Formation_Calibration_DRAFT.md (World #7: Syriac Christianity, Edessa/Nisibis)

Reviewer note: this is a cold, adversarial review. No prior discussion of this document was consulted. All source documents (Doc_01–Doc_09, Syriac_Phase1_Ecology_Assessment_DRAFT.md, Representative_Identity_Preliminary_Decision.md) were read in full and checked against the draft's own characterizations, not assumed from the draft's summaries.

---

## 0. Mandatory Truncation Check (two independent methods, raw evidence)

**Method A — Read tool (Windows-side access path).** The file was read in full via the Read tool: 174 numbered lines returned in one pass (no truncation notice). Content ends with Section 6, "Open Items Carried to Voice Construction," item 6, ending in the sentence: "...engaged briefly or by turning toward what did press on this world's own formation, never flagged as an evidentiary gap in the Representative's own voice." This matches the expected final section and item exactly. All six top-level sections (`## 1.` through `## 6.`) are present.

**Method B — bash (Linux-mounted path), independent of the Read tool.**

```
wc -l: 173 (Read tool numbered 174 lines; the one-line offset is consistent with a file with no final trailing newline — not evidence of truncation)
wc -c: 43154 bytes
tail -15: ends with the identical Section 6 / item 6 text quoted above, verbatim
md5sum: 5550b630e20fd86dd83ec5dc8ac2291b
grep -n "^## ": confirms six top-level section headers at lines 12, 27, 60, 110, 124, 166 (Sections 1–6), matching the Read tool's structure exactly
```

**Conclusion: the file is NOT truncated or stale on either access path.** Both methods agree on content, ending, and section count. This project's documented bash-mount staleness bug is not in evidence here.

---

## 1. Findings

### Finding 1 — Deacon determination (Section 2.2): verified sound, no missed contradiction found [no defect — reported for completeness given the task's specific concern]

The two citations underlying "Deacon" were checked independently against source text, not the draft's paraphrase:
- Doc_02, Section 3 states, verbatim: "Ephrem was a deacon and *malpana* (teacher) embedded in the bnay/bnat qyama choir-order," citing Griffith 1997/1986. Confirmed accurate quotation.
- Doc_04, Section 1 states, verbatim: "Real and well-sourced (Doc_02, Section 3; Jerome's *De Viris Illustribus* 115, calling him 'deacon of the church of Edessa')." Confirmed accurate quotation and correctly characterized as an independent, second citation stream.
- Doc_05 §1.1's "a deacon of Edessa's church, embedded in this same qyama-adjacent order" is an exact quotation match.

A full search across Doc_01–Doc_09 and the Ecology Assessment for any hedge, exclusion, or contest of Ephrem's bare deacon title (as distinct from the *specific circumstances* of his ordination, which several documents do treat as later/legendary) found none. Doc_07's own Round 2 review record is instructive here: it independently confirms "deacon" is *Ephrem's* documented title and explicitly corrects an attempt (in an earlier Doc_07 draft) to attach it to Aphrahat as one of several candidate titles — i.e., this project has already stress-tested "deacon" adjacent to exactly this document's own use of it, and found no problem. The Phase Two draft's claim that "no document excludes it, hedges it, or contests it" holds up. **This is the opposite of the Malpana/Doc_02–Doc_03 pattern the task asked me to check for; I did not find a parallel gap here.**

### Finding 2 — Yausep carry-forward (Section 2.1): accurate representation, including the corrected reasoning [no defect]

Section 2.1's account of "why Yausep was chosen" matches Representative_Identity_Preliminary_Decision.md's own "Why Yausep was chosen" paragraph closely and non-selectively. The Ecology Assessment's Section 7 "Summary for Formation Calibration" quotation ("the Yausep name choice... should proceed") is verbatim-accurate. The draft's own added move — noting that the Preliminary Decision's stated reason for a *male* name ("the malpana title itself is directly attested only for a man") no longer holds once Malpana is dropped, and re-grounding Yausep's male-name coherence in Ephrem's attested deaconate instead — is a genuine, correctly-reasoned patch of a reasoning gap that would otherwise have been silently carried forward. This is good practice, consistent with Ecology Assessment Section 7 Point 1's own reasoning.

### Finding 3 — SUBSTANTIAL: Recurring unsupported superlative about the Persian-side emotional material

Four separate places in the draft (Sections 3.2, 3.3, 3.5, and 5.6) characterize the Persian-side/C6 emotional material as, variously, "this world's single most vivid, emotionally-textured passage," "this world's own richest emotionally-textured material," and "this world's single most vivid, emotionally-textured domain" — each time citing Doc_05, Section 7 (the Proportionality Assessment).

Checked directly against Doc_05 Section 7's actual text, the finding it supports is narrower: "Human Ecology (Section 1) is not uniformly Ephrem-heavy in the same way — on inspection, the Persian/Aphrahat register (1.2) is **the fuller, more vivid passage**, appropriately reflecting the richer emotional evidence Doc_02/04 supply for the persecution-endurance gravity (C6), while Ephrem's own formation passage (1.1) is long chiefly because of hedging..." This is a comparison **between Doc_05's own two Human Ecology subsections (1.1 vs 1.2)** — it does not compare C6's material against Worship Ecology, Community Ecology, Organizational Ecology, or Ministry Ecology content, and no document in the construction record makes that broader, document-wide comparison. Doc_08's parallel claim (Force 2A-1, "the most direct force-to-gravity connection in this document") is about causal directness, not emotional vividness, and does not support the superlative either.

This matters because Section 3 is explicitly the one determination this document is required to leave open and present without thumbing the scale (Section 3, opening line: "This is the one identity question this document does not resolve"), and because Section 6 names the anchor-context decision as "the single most consequential open item." A repeated, unearned superlative describing the cost of the *recommended* option (Roman anchor forfeits C6) inflates the evidentiary basis for that stated cost beyond what Doc_05 actually established. It does not appear to favor the recommendation (if anything it overstates the recommendation's own cost), but it is a real, citable evidentiary overreach, recurring four times rather than once, in exactly the section the task flagged for closest scrutiny.

**Recommended fix:** scope all four instances back to "the fuller, more vivid passage within this document's own Human Ecology account (Doc_05, Section 7)," and drop the "this world's single most vivid... in the construction record" framing unless a document-wide comparison is actually performed and cited.

### Finding 4 — COSMETIC: Header cross-reference error (line 6)

The document's own header states that the Preliminary Decision's rejected "Malpana" finding "is not carried forward, per the reasoning in Section 2.3 below." The actual Malpana-not-carried-forward reasoning is in **Section 2.2** ("Role/Title: Deacon," which contains "This resolves the Malpana question by avoidance, not adjudication..."). Section 2.3 is a related but distinct sub-argument (the breadth-of-encounter preference test). Minor, but worth fixing given this project's own history of catching exactly this class of wrong-section cross-reference (e.g., Doc_05's Round 2 second-pass fix to a mis-pointed Section 9 cross-reference).

### Finding 5 — COSMETIC: Spliced quotation in Section 5.8

Section 5.8 quotes Doc_08 Section 6 as one continuous passage via ellipsis: "what did not survive, structurally and near-completely, is any text authored by an ordinary lay believer... material without an institutional home to keep re-copying and re-performing it simply stopped being carried forward." These two clauses are drawn from two different subsections of Doc_08 Section 6 ("What Selection Effects Shaped What Survives" and, several paragraphs later, "What the Transmission Pattern Reveals About Forces"), not from one continuous passage. This is the same class of error — splicing wording from two separate source locations under one continuous quotation mark — that this project's own Ecology Assessment Round 1 review previously caught and categorized as a minor/cosmetic finding (its Section 5 quotation-splicing fix). The underlying claim is accurate; only the presentation as a single unbroken quotation is imprecise.

### Finding 6 — COSMETIC: Section 5.5 mixes citation targets

Section 5.5 (Depth Calibration for C3, doctrinal rivalry) supports its "Rich, as lived first-person experience" rating for C3 by citing "Doc_08 (Force 2A-2) documents this as an ongoing, career-spanning, intensifying pressure on C1 itself." Force 2A-2 in Doc_08 does both things (intensifies C1 and directly produces C3), but citing its effect on C1 specifically, inside a paragraph rating C3, reads as a target mix-up rather than the more directly relevant half of Force 2A-2's Layer 3 finding (that it "directly produces Confirmed Gravity C3"). Does not change the Rich rating, which is independently supported by Doc_04's own C3 test results.

### Finding 7 — COSMETIC: No independently-verifiable record of the project lead's Deacon decision

Section 2.2 states "This is a change... made by the project lead specifically to resolve the contradiction." Unlike the original Yausep/Malpana decision, which has its own dedicated artifact (Representative_Identity_Preliminary_Decision.md, explicitly stating "Discussed directly with the project lead"), no equivalent standalone record exists anywhere in the provided document set for the Malpana→Deacon change. This document is the sole extant record of that attribution. This may simply reflect Phase Two's normal operation (Identity Determination is this phase's own job per Part Four), but given this project's strong anti-self-certification discipline elsewhere (see Doc_06's revision log), the absence of an independently-checkable decision record for this specific claim is worth noting, not smoothing over.

### Finding 8 — COSMETIC/observation: Section 3.3's use of Ecology Assessment Point 1

Section 3.3 cites the Ecology Assessment's Point 1 reasoning (that a teaching role whose own authority is not cleanly episcopal "fits unusually well" with C4's ambiguity) as a "gain" specifically for the **Persian anchor** option. In its original context, Point 1's reasoning was about the *role-shape* generally (teacher-in-qyama vs. other role options), not about anchor-context choice specifically, and applies with some force to Ephrem's side too (via C2×C4 reshaping). Using it as a Persian-anchor-specific "gain" is a defensible but generous extension of the original argument; the project lead should read this bullet knowing it is not as squarely on-point as the document's other citations in this section.

---

## 2. Points Checked and Confirmed Sound (no issues found)

- **Temporal Horizon (Section 4):** the 200/410 boundary reasoning, and every item on the excluded-material list (Rabbula's episcopate/411–435; the Peshitta name/Moses bar Kepha, d. 903; the 424 Synod of Dadisho/Markabta; the post-489 School of Nisibis; the Ephrem-choir-leadership legend/Jacob of Serugh and the *Vita Ephraemi*), were checked against Doc_01 §§2/9, Doc_02 §11, Doc_03 §§1.2/3.1/3.2, Doc_04 §1/C2 Scope Note, and Doc_08 Force 3B-2. All check out accurately, including exact-quote matches ("a genuine gap in what is currently locatable").
- **Depth Calibration ratings (Section 5), items 5.1–5.4, 5.6, 5.7, 5.9:** each Rich/Moderate/Thin/split rating traces to a specific, correctly-quoted Doc_04 gravity test result or Doc_08 force, not asserted judgment (see Findings 3, 5, 6 above for the specific exceptions found).
- **Scope discipline (Voice Construction boundary):** no instance found where the document makes a specific register, phrasing, or address-pattern decision under cover of "illustrative" framing. Every place the draft approaches this line (Sections 3.5, 4's "boundary-edge note," 5.3, 5.7/5.8, Section 6 items) explicitly names the boundary and defers the actual decision to Voice Construction.
- **The anchor-context section's overall structure** (4 gains/2 costs for Option A vs. 2 gains/4 costs for Option B) reflects a genuinely asymmetric evidentiary base already established in Doc_02 §1 ("Ephrem's corpus overwhelms the other two in sheer volume"), not an artificial thumb on the scale.
- Note: Part Four's own verbatim governing text was not among the documents supplied for this review, so claims that specifically characterize "what Part Four instructs" (e.g., the breadth-of-encounter preference test in Section 2.3, or the horizon/biography distinction in Section 4) could not be independently checked against that source and are reported here as a scope limitation of this review, not as a finding against the document.

---

## 3. Overall Verdict

**SUBSTANTIAL REVISION REQUIRED.**

The load-bearing Identity Determination work (Deacon, Yausep) is sound and well-sourced, and the Temporal Horizon and scope-discipline work hold up well under adversarial re-checking. However, Finding 3 — a citable, four-times-repeated evidentiary overstatement in the one section (anchor-context tradeoff) this document is specifically required to present without thumbing the scale — is a real defect, not a wording preference, and should be corrected before this document proceeds. The fix is narrow and mechanical (rescope four instances of one claim), not a reopening of any underlying determination. Findings 4–8 are cosmetic and may be applied directly per this project's own build-cycle discipline without a further full review round.
