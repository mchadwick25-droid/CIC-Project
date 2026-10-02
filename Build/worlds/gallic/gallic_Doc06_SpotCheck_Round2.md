# Doc_06 — Round 2 Bounded Spot-Check

**Scope:** Independent reviewer, fresh context, no drafting or fix-round involvement. Bounded per this build's standard cycle: verify only that the Round 1 fix round (`gallic_Doc06_Full_Lexicon_Development.md` §6, "Round 1 fix round") actually and correctly addressed each of the 17 findings (S1–S8, C1–C9) in `gallic_Doc06_Review_Round1.md`. Not a re-review of the whole document; tier/CT classifications Round 1 said did not need reopening were not re-litigated.

**Date:** 2026-09-10.

---

## Per-finding verdicts

### S1 — Tier-3 Distortion Risk — CONFIRMED FIXED (two residues + one new defect)
All 13 Tier-3 chunks now carry `## Distortion Risk` with a Modern/World Hearing pairing. Read 12 of 13 in full (069, 070, 071, 072, 073, 075, 076, 077, 078, 079, 080, 081); none is boilerplate, each is term-specific and grounded in the chunk's own quoted content. Spot-verified new content against source: 070's "Vincent's one use of 'the holy brethren'" (exactly one Vincent occurrence, at `iii.xii`; the other three in npnf211 are Cassian's); 080's new cross-reference "(Doc_05 §9A.7)" (Doc_05 §9A item 7 does say Christology beyond the office-Trinity is "peripheral to the formation ecology as read").

Twelve of thirteen Final Assembly Instructions disclose both the DR addition and the Key-Sources retention. **Residue:** `galliclex074_massilians.md` was untouched by the fix round (it already had DR) and so retained Key Sources at Tier 3 with no disclosure — the one chunk of 13 without it.

**Residue:** the review's structural demand ("the fix round should decide deliberately whether the Tier-3 chunks are Tier-3 entries with extra prose, or Tier-2 entries mislabelled") is answered only in chunk-level clauses; Doc_06 itself records no Tier-3 depth policy, and §2.5 still says of 069 "Quick Meaning suffices" while the chunk has a 200-word World Meaning, a DR pairing and a Key Sources list. Left open as an optional item (see below).

**NEW DEFECT (introduced by this fix round):** `Lexicon_Deployment_Index.md` §5b, the check sheet added specifically to stop S1 recurring, was a malformed table — header and separator 5 columns, all 81 data rows only 4 cells (Tier value missing), so rendered Markdown shifted every column one to the left. Underlying data were correct (the [DR]-flag cell checked against the master table's own DR column: 0 mismatches of 81).

### S2 — *puritas* in Hilary — CONFIRMED FIXED (one small residue)
Re-grepped `hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt`: exactly 1 hit for `purit[a-z]*`, at line 1233, reading "vite, ! in quo erat consentauca puritas pectoris,". Locus, count and OCR form all check out. Eucherius: 0 hits. Doc_06 §5 item 2 now lists it under "Attested in Hilary" with the phrase, the line, the OCR normalization and the sense-unread caveat; chunk 006's Latin-lemma line and Author Gravity note are both amended as the review asked. Re-verified the remaining "Not found in either" list is true: `discretio`, `regula`, `antiquitas`, `miles`, `liberum arbitrium` = 0/0 in both files. Faustus: `liber* arbitri*` = 0, `initium fidei` = 0, `discretio` = 12, `gratia` high-frequency — all as stated.

**Residue:** §5 item 2 listed ***humilitas*** among Hilary's attested lemmas without the inflected-only qualifier given to *virtus* and *episcopus* — the nominative does not occur, only `humilitate` ×2 and `humilitatem` ×1.

### S3 — fabricated Doc_04 quotation — CONFIRMED FIXED
Independent whole-file case-insensitive search of `gallic_Doc04_Gravity_Discovery.md`: 0 hits for "organizes within", "own context", "Supporting definition", "definition of Supporting" — confirms the review's finding. §2.1 test 1 is now Doc_06's own synthesis with no quotation marks on the criterion; the three Doc_04 phrases it now quotes verify verbatim ("Folded into G1 as its first half"; "Folded into G8"; "Folded."). The fix log's claim to have also corrected the parallel misattribution at the 021 renunciation entry verified against the pre-fix file: real, and not itself named by Round 1.

### S4 — reciprocity diagnosis — CONFIRMED FIXED (numbers exact; one loose attribution)
Rebuilt the directed graph from all 81 chunks' own Related-Terms fields against Doc_06 §2.7's canonical names. Every figure reproduces exactly: 881 directed / 324 reciprocal / 233 one-directional; 96 target-Tier-1 / 137 target-Tier-2-3; 7 Tier-1→Tier-1 edges, identical list; 193 higher-numbered→lower-numbered / 40 reverse; of the 193, 124 cross-tier / 69 same-tier; 62 distinct targets, top target 032 humility at 15. Set-diffed the index's listed 233 rows against the independent recompute: empty in both directions, no duplicates, every "Target tier" cell correct.

**Minor:** Doc_06 §5 item 1 appended "(matching the index's own §6 computation exactly)" to the 124/69 split, but the index §6 as it stood did not yet state those numbers explicitly — a loose attribution rather than a wrong figure (addressed incidentally by the fix below, which brings the two documents into exact alignment).

### S5 — Registry Cross-Reference column — PARTIALLY FIXED (all named cases correct; a real under-capture residue)
Column is genuinely split; parsed all 81 rows: no Excluded row (4, 33–38, 44) appears in any "Key-Source Registry Rows" cell. Every case the review named is now right (008 excludes 43/44; 009 excludes 35/43; 015 excludes Row 4; 005/066 exclude Row 36; 042/044/045/046/047 exclude Row 43).

**Residue:** the column silently missed plural and range row mentions — 15 such mentions across 13 chunks captured in neither column. Worst: **015 anchorite/hermit**, whose Key Sources open "Registry rows 8, 10" (its own two principal Cassian sources) but whose index cell read only "Row 1, Row 3". Also 002/006/008/012/015 lost "rows 26–27" and 054 lost "rows 1–2".

### S6 — Author-Gravity-Risk column — PARTIALLY FIXED (every named case correct; over-flag residue, left open)
Every review-named case is now right: 010, 007, 005 → "Yes — single-voice"; 064, 023, 024, 028, 031, 035, 039, 040, 051, 066, 067 → "Weighted" (were "No"); all 13 Tier-3 rows → "No note (Tier 3)". **Residue (optional, not fixed this pass):** 014, 015, 063 are marked "Yes — single-voice" though their own notes' headline clauses describe cross-node or shared attestation, with the "single-voice" keyword hit landing on a subordinate clause about a rule or a predicate, not the term itself. Less harmful than the original under-flag and already disclosed via the derivation-rule note under the table, so left open as optional.

### S7 — §2.5's Tier-2 count — CONFIRMED FIXED
Heading reads 45; parsed §2.7 for Tier-2 rows with an empty Δ cell: 45. Extracted every reference from §2.5's Tier-2 paragraph: 45 distinct, set-difference against the table empty in both directions. 1.7 elder/senior/abbot present, in the "G5/G4's mechanisms" group, with the Doc_05 §2.1/§4.1 context the review's remedy specified.

### S8 — stale scope — PARTIALLY FIXED (one stale claim survived in the very section rewritten; fixed this round)
Header, §1 "Does"/(d)/(e), §1 "Does not," §5 item 1 and the §6 Document log all described the delivered three-pass set; no occurrence of "two-step," "Step B … is a separate pass," "not met by this pass," or "is to be checked in the index" survived outside the fix log's own description of what it fixed. §5 item 1 stated the reciprocity finding rather than deferring it.

**Residue (fixed this round):** §6's drafting-basis sentence still read "row 43 (Salvian) appears in 001 only" — false for the delivered set. Row 43 is used, within its Licensed For, in nine chunks (001, 014, 020, 021, 022, 033, 054, 068, 071 — independently confirmed by parsing all 81 chunks' registry-row fields).

### C1 — CONFIRMED FIXED
Grepped Doc_05 §10B directly: "The ecology has two hubs, one per node" (line 433), "Every lens above routes through him" (433), "**Peripheral.** G10 in the founding voices (as Doc_04 found)" (437) — all verbatim; Doc_06 §2.2 now reproduces them accurately without false quotation.

### C2 — CONFIRMED FIXED. 065 reads "Tours's weapon and Marseilles's vanity." No surviving "node" usage in any chunk's World Meaning.

### C3 — CONFIRMED FIXED. Verified against `npnf211` at `ii.iv.iii.xiii`: the chunk now carries the angel's full sentence verbatim.

### C4 — CONFIRMED FIXED. Zero occurrences of `gallicNNN` anywhere in `Lexicon-Chunks/`.

### C5 — CONFIRMED FIXED. §2.2's 005 entry carries the disclosure clause for the added [RT].

### C6 — CONFIRMED FIXED. §2.2's coverage paragraph now consistent with the 013 entry and §2.5's G9 term list.

### C7 — CONFIRMED FIXED. Counts withdrawn in favor of presence-only claims; re-ran the review's regexes (Hilary `virtu*` = 27, `episcop*` = 30, Eucherius `erem*` = 60) confirming the original ×23/×23/×27 did not reproduce and that the presence claims are true.

### C9 — PARTIALLY FIXED / residual inaccuracy (fixed this round)
The half the fix log claims was already correct is correct: pre-fix Doc_06 §3's 011 entry already read "ch. 17 [44]"; no change was needed there, as claimed. **But the chunk-011 rewrite inverted the quotation**, stating Vincent's own progress passage "is quoted in" Heurtley's footnote — the footnote in fact quotes Newman (about Origen), not Vincent's progress passage. Chunk 057 states the same underlying fact correctly. The error was inherited from the review's own suggested wording rather than newly invented, but was not caught by the fix round.

---

## Findings outside the bounded 17 (noted, not exhaustively pursued)
- Chunk 008's Key Sources still carries a raw token count ("*gratia* ×175 in the treatise body"), the class of claim C7 caused to be withdrawn elsewhere — inconsistent but not itself one of the 17.
- Index §5b's summary line, when zero chunks are missing, read as a double negative ("0 … missing … : none — all carry …") — cosmetic.

---

## Overall verdict

**The fix round substantially cleared.** Fourteen of seventeen findings were fully and correctly fixed outright. The two hardest to fake — S2's Latin non-finding and S4's six-way recomputation — verified exactly against the primary file and an independent rebuild of the 881-edge graph, including the full 233-row list. The fix round also caught and corrected a defect Round 1 had not itself named (the parallel S3 misattribution at 021).

Did not require a further full review round. Required a short micro-fix pass, applied directly by the build thread following this spot-check (not a further drafting pass), covering:
1. Index §5b's malformed table (new defect, in the check sheet added to prevent S1 recurring) — fixed.
2. Doc_06 §6's false "Salvian appears in 001 only" claim (residual S8) — fixed.
3. Chunk 011's inverted C9 correction (Vincent's passage vs. Newman's) — fixed.
4. Index Key-Source column's under-capture of plural/range row mentions, worst at 015 (residual S5) — fixed.
5. Doc_06 §5 item 2's unqualified *humilitas* claim (residual S2/C7) — fixed.

Left open, by explicit judgment, as genuinely optional and non-blocking: the Author-Gravity-Risk keyword-scrape over-flag at 014/015/063 (residual S6), and a one-line Tier-3 depth-shape ruling in Doc_06 itself (residual S1) — each chunk's own reasoning already states its case, so no participant-facing gap exists.

**Disposition of this spot-check:** no classification (tier, CT, gravity) reopened at any point; no disagreement with Round 1 review's own findings — the residues found here are execution gaps in the fix round, not defects in Round 1's diagnosis.
