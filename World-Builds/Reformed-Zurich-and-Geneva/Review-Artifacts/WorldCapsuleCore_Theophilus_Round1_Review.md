# Round 1 Review — World Capsule Core (Theophilus / rzg)

**Document reviewed:** `rzg_World_Capsule_Core.md`
**Reviewer:** independent cold adversarial review, model=Sonnet, worktree-isolated, per `cic-build-cycle`.
**Date:** 2026-09-16

## Findings, most severe first

1. **HIGH — Fabricated/inverted historical detail: "you have also buried a pastor" (Section 5, "What This World Is Responding To").** Zwingli was not buried. Per this world's own vendored, Documented primary source (`Story-Chunks/rzgstory003_myconius-account-of-zwinglis-death.md`, Myconius's own near-eyewitness account): "After the battle, once the victors had time to search among the fallen, Zwingli's body was found, given a mock trial, and burned." His body was denied burial and deliberately destroyed by the victors — a well-attested, symbolically loaded fact, inverted here. Internally inconsistent with the same document's own Section 9 ("a death in battle reported without ornament," no burial claim) and with the already-Approved `rzg_Representative_Permanent_Prompt_Theophilus.txt` (line 41: "a pastor killed in the same war," no burial claim). **CONFIRMED, independently re-verified by the build thread directly against `rzgstory003`.**

2. **MEDIUM — Section 2 conflated a unity-supporting finding with the T1 tension.** The tensional-gravity paragraph rendered T1 (Council-Led Civic Authority vs. Consistorial Independence) using language that actually restates G3's strand-specific enactment difference (Disputation vs. catechesis-and-Consistory) — which Doc_04 §3.3/§5 and Doc_07 §2I explicitly classify as evidence *strengthening*, not weakening, cross-strand unity, not as an unresolved tension. The genuine T1 tension concerns authority over ongoing church discipline specifically, correctly rendered later in Section 7. **CONFIRMED, independently re-verified by the build thread against Doc_07 §2I's own "strengthening, not weakening" language.**

3. **LOW — Paraphrase drift: "bound its whole territory to what was decided" (Section 6, Primary Vocabulary).** The actual source, `Story-Chunks/rzgstory001_first-zurich-disputation.md`, states the council "required every priest in the canton to preach the same way" — a specific claim about priestly preaching, broadened here into vaguer territorial language. **CONFIRMED, independently re-verified by the build thread against `rzgstory001`.**

## What checked out well (reviewer's own independent verification)

- T1 and T2 held open properly everywhere else in the document; no sentence resolves either tension or picks a side.
- Banned analytical-distance phrase list (Final Assembly Instruction): fully clean.
- Section 10 (builder-only Voice Notes) genuinely absent.
- Word count ~2,571 words (~3,300–3,400 tokens), within the 3,000–5,000 token target.
- The "never fully let up" fabrication (caught and fixed in the immediately-preceding Construction Notes/Permanent Prompt review) does **not** recur here — this document correctly reuses the corrected, verbatim-sourced Doc_08 Force 2A-4 language from the start.
- Primary Vocabulary section (Section 6) correctly uses exactly the five terms World Profile §6 marks always-present YES, correctly excludes the one marked NO ("Sign and the Thing Signified"), and correctly respects the Consistory term's Geneva-scope-only caveat.
- Temporal horizon closing edge (Section 8) word-for-word consistent with the Permanent Prompt's Dort framing.
- Spot-checked claims not otherwise flagged (1549 Consensus signing, T1/T2 substance, the Wittenberg/republican-city-state comparison, the Memory Structures "confessions written to survive the founding generation" claim) all traced cleanly to their cited sources.

## Noted, not treated as a new defect

- The organ/Psalter worship claim (Section 4) is stated with the same confidence level as the already-Approved Permanent Prompt (flat, without an emic hedge, despite the underlying date being Dominant Modern Reconstruction per Doc_01 §5/Doc_05 §3) — a pre-existing, cross-document pattern, not something new or worse introduced here.
- Section 6 uses 5 terms rather than the template's 6–10 range, because World Profile §6 names only 5 always-present-YES Tier 1 terms — a real, source-bounded constraint correctly honored, not an oversight, matching the same disclosed pattern already logged for the Permanent Prompt's own word-count overage.

## Disposition of this review

Finding 1 is treated as substantial per `cic-build-cycle` (a factual inversion in an always-present document is Constitution Article 28 territory, the same severity class as the fabricated quotations found in every prior document this session). Findings 2–3 are cosmetic/low fixes. All three fixed directly in Revision 2. A targeted Round 2 recheck follows.
