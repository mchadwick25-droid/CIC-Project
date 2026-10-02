# Round 3 targeted recheck: `rcg` library stage (commit `3b021ddf`)

Final round under the `cic-build-cycle` three-round cap.

### Verdicts
| Document | Verdict |
|---|---|
| Step 0 | **CLEARED** |
| Doc_01 | **COSMETIC ONLY** |
| Doc_02 | **SUBSTANTIAL REVISION REQUIRED** (narrow) |
| Source_Registry | **SUBSTANTIAL REVISION REQUIRED** (narrow, tied to Doc_02) |

Doc_02 and the Source Registry have now gone through three rounds of substantial revision without clearing. Per the `cic-build-cycle` cap, this is an unresolved tension for the project lead, not grounds for a fourth round. The remaining defects were small and mechanical (a wrong locus, an unpropagated quote fix, a missing Registry row, an overcounted confidence tally) — applied directly and disclosed as post-cap corrections rather than a self-certified clearance.

### Confirmed fixed this round
- Moralia/Register chronology (dedication postdates Book I Ep. 43), independently re-verified against the file.
- Istria material: emperor's-order quote verbatim at `iii.v.ii.xxiv-p8` (Book II, Ep. XLVI, "To John, Bishop"); Pelagius I no longer attributed to the apparatus; Donatism locus corrected to line 23072; Theodelinda quote and the editorial-inference flag — correct in §1, not yet propagated to §6 (see findings below).
- Equitius (Doc_01 §4): actors now correct (the then-pope, Julianus, Julianus's own servant; Peter only the dialogue partner); quotes verified word for word; the false "not independently locatable" claim removed.
- Short Description: "near-total practical absence" gone, consistent with §1/§2/§6.
- Holdings tool: confirmed to run with an empty `records/rcg/` directory; output (220 files, 12 in scope) matches Doc_02 §8 exactly; all 12 in-scope files disposed of.
- Cross-references flagged in Round 2: fixed.
- Length ratio: consistent at ~six times across Step 0 and Doc_02.
- Round 1 review file: build-thread rebuttal removed, now the reviewer's own unedited record.

### Surviving findings, most severe first
1. **MEDIUM, Doc_02 §6:** the Theodelinda fix (exact quote, inference-as-fact) was not carried from §1 into §6. Fixed this round.
2. **MEDIUM, Doc_02 §1:** the emperor's-order quote was cited at the wrong locus (`iii.v.i.xxiv-p8`, a Book I Seneca endnote, instead of `iii.v.ii.xxiv-p8`, Book II Ep. XLVI). Fixed this round.
3. **MEDIUM, Source_Registry:** no row covered the Ep. II.46 quote. Fixed this round by extending row 1.
4. **LOW-MEDIUM, Doc_02 §9:** overstated "two Confidence A primary quotations" for the Istrian material; only one (Ep. II.46) is Gregory's own words at that confidence, the other is apparatus text at Confidence B. Fixed this round.
5. **LOW-MEDIUM, Doc_01 Status line:** overclaimed "Held at Cleared review" before Round 3 had actually run. Fixed this round (now "Cleared review, Round 3, COSMETIC ONLY").
6. **LOW, Doc_01 §4:** the Equitius verification note contradicted itself (called the vision sequel unverified, then asserted it). Fixed this round by quoting it directly.
7. **LOW:** the *servus servorum* formula's own rarity (four attestations, not "recurring") not yet disclosed in Doc_01 §5. Fixed this round.
8. **LOW:** new cross-reference errors in Doc_01 (§1's "§5 below" and "§2 and §3 below"; §6's "§1 and §3 above"). Fixed this round.
9. **LOW:** Registry row 8's Equitius range not extended to cover the newly-verified summons-and-vision sequel (~lines 2109–2204). Fixed this round.

### Escalation note
Doc_02 and the Source Registry did not clear within three rounds. The remaining defects were citation/sourcing-accuracy issues (the category this project weighs above cost), which is why they count as substantial rather than cosmetic under the skill's own definition — but each one was narrow and unambiguous to fix once found. Applied directly rather than opening a fourth round; flagged to the project lead in this world's handoff report for awareness and sign-off, per the skill's own escalation-category rule for "three rounds of substantial revision on the same document without it clearing review."
