# Doc_08 — Round 2 Bounded Spot-Check

**Scope:** Independent reviewer, fresh context, no drafting or fix-round involvement. Bounded per this build's standard cycle: verify only that the Round 1 fix round addressed each of the 14 findings in `gallic_Doc08_Review_Round1.md`. Not a re-review of the whole document; gravity classifications, tier assignments, and the Heurtley "in-window" correction were not re-litigated.

**Date:** 2026-09-10. **Verdict: does not clear — one more bounded fix round required.**

---

## Substantial findings 1–7

### Finding 1 (barbarian tally at 2A-5 + six downstream loci) — PARTIALLY FIXED; new defect introduced
Verified correct at the source: independent grep of `npnf211` confirms 19 `barbar*` hits and every claim in the rewritten Cell 2A-5 Layer 1 (both *Vita* IV occurrences; *Vita* XVIII; *Dial.* III.4; *Dial.* III.15/Brictio; the Cassian and Vincent findings; Heurtley's Vandal note; both Hilary of Arles line numbers, 528 and 747).

**Downstream consistency fails in two places:**
- **§4 Connection 13 was never edited** despite the Document Log's claim — still reports only two northern episodes and an unrevised "the north's literature keeping the force out" reading that *Dial.* III.15 directly complicates.
- **§4 Connection 3 was also not touched** and now contradicts Cell 2A-5 directly: "The barbarian and fiscal forces (2A-5, 3A-2) do not enter this chain ... they attach to G10 only ... confirmed at Cell 2A-5" — Cell 2A-5 now says four further attachments, not "G10 only."
- **New defect at §5 gap (iv):** the fifth item in the five-occurrence list is given as "the Bagaudae/Goth material Salvian alone carries at length" — Salvian is not Sulpitius; this doesn't match Cell 2A-5's own enumeration.
- "At Tours" is wrong for the *Vita* IV discharge scene — the chapter is explicitly set at Worms.
- "Four ... forms" (2A-5, §5) is enumerated as five instances (G6 twice, G1, G2, G8).
- §6/§8 say "one unread Latin phrase" where 2A-5 itself says Hilary has two occurrences.
- Stale phrasing survives verbatim in the Document Log's Drafting basis bullet (vi) and its search_record table (still lists Hilary "lines 670, 716, 881," where line 670 is exactly the citation Finding 14 found misleading).

### Finding 2 (Cross-Strand Gravity Note) — CONFIRMED FIXED
"Complete in both directions" is gone; four named exceptions spot-checked directly against Section 5's prose all hold.

### Finding 3 (two-vs-four attachments) — CONFIRMED FIXED
Cell 2A-5 and Section 5's G10 note both now say four, matching Appendix A.1/A.2 exactly. Minor wobble: "four thin or borrowed forms" is enumerated as five instances (same root cause as Finding 1's residue).

### Finding 4 (Faustus Latin) — PARTIALLY FIXED; the same defect recurs in the replacement
The honesty label ("normalized reconstruction, not a transcription") is genuine, and all three original diagnoses are confirmed. But the two replacement anchors, asserted in bold as grep-verified at lines 3569 and 3628, both fail a whitespace-tolerant regex against the actual OCR (which reads "coupotenter" at 3569 and "Areh^tensis ... subscriptioneni ... adiei ... nouis" at 3626–3628) — only sub-fragments of each actually grep clean. The Confidence line's upgrade to "Documented for the two grep-verified phrases specifically" is unearned. A further new citation error: the Prolegomena dating quote is cited at "lines 530–550, 318–335" but actually sits at line 555.

### Finding 5 (*Dial.* II.5 speaker) — CONFIRMED FIXED

### Finding 6 (§8 From-Within exceptions) — PARTIALLY FIXED
All four disclosed exceptions verified verbatim against their Layer 2 entries. Residue: Section 9's completion checklist still certifies "no modern analytical overlay (two edge-of-layer disclosures at Section 8)" — not updated to four.

### Finding 7 (Vincent/Massilian tension) — PARTIALLY FIXED; the backwards version is still live
Both corrected loci (Cell 3B-3 Layer 1; §7's Contested-level bullet) now state the tension correctly and verbatim, with Heurtley's actual counter-statement restored. **But Section 7's "Named Scholarly Tensions Carried at Full Strength" item 2 was not touched and still reads the backwards framing verbatim: "Heurtley and the editors he cites vs. Vincent's silence."** Three loci state this tension; only two were fixed.

---

## Cosmetic findings 8–14

- **8 — CONFIRMED FIXED at both loci** (Cell 1B-1 and Section 5's G10 note).
- **9 — CONFIRMED FIXED.**
- **10 — CONFIRMED FIXED**, verified verbatim against Gennadius ch. XIX.
- **11 — CONFIRMED FIXED.**
- **12 — PARTIALLY FIXED, and the replacement text is itself now false.** Section 8's paragraph was rewritten, but: Cell 2A-5's own heading still reads "abbreviated treatment"; Appendix A.1's Treatment column for 2A-5 still reads "abbreviated"; Section 9's checklist still reads "2A-5 abbreviated at all three layers"; and — most seriously — the rewritten §8 claim was never re-measured against the fix round's own expansion of Cell 2A-5. Independent word count: 2A-5 is now 1,321 words, the **longest** of the twenty-two entries (not 789/fifth-longest as originally flagged, and not what the rewritten §8 claims), with its bulk in **Layer 1** (641 words), not Layer 3 (529 words) as the new §8 text asserts.
- **13 — CONFIRMED FIXED**, verified verbatim against *Commonitory* ch. 4's heading.
- **14 — CONFIRMED FIXED on all seven nits.** One residue: the Registry row 44 disclosure cites "per Round 1 review's own check (item (e))" — the Round 1 review has no lettered items; the document's own draft-era instruction to the reviewer that originally had an item (e) was deleted in the same commit, leaving a dangling reference.

---

## Overall verdict

Nine of fourteen findings (2, 3, 5, 8, 9, 10, 11, 13, 14) are cleanly and correctly fixed, with every primary-text claim independently re-verified and holding, including all four barbarian loci, both Hilary line numbers, the Heurtley passages, Gennadius XIX and LXXXVI, and both div-id corrections. The evidentiary work of the fix round is real and sound.

Five findings carry residue, three of which are the same defect the finding named recurring in a different place in the document (the backwards Vincent tension still live at §7's tension list; the barbarian tally's own downstream propagation incomplete at two Section 4 connections; the Faustus grep-anchor problem recurring in its own replacement).

**Ten targeted items remain, none requiring reopening a gravity classification, a tier, the Heurtley correction, or the matrix itself:**
1. §7 Named Tensions item 2 — still backwards.
2. §4 Connection 3 — now contradicts Cell 2A-5.
3. §5 gap (iv) — Salvian misattributed as a Sulpitian occurrence.
4. Cell 3A-1 — grep anchors fail; confidence claim must come down; Prolegomena line citation wrong.
5. §8 Proportionality — word counts wrong; central claim now false.
6. §4 Connection 13 — never edited.
7. §9 checklist — "two" disclosures (should be four); "2A-5 abbreviated at all three layers."
8. Cell 2A-5 heading and Appendix A.1 Treatment column — still "abbreviated."
9. Document Log — stale Drafting-basis tally; stale search_record Hilary line list.
10. "At Tours" for the Worms discharge scene; "one unread Latin phrase" vs. two; "four forms" enumerated as five; the dangling "item (e)" reference.
