# Doc_07 (Integrated Ecology Analysis) — Round 2 Independent Adversarial Re-Review
## The Reformed Cities — Zurich & Geneva

**Reviewed:** `Doc_07_Integrated_Ecology_Analysis.md` (Revision 2), plus the five other files the build thread's Revision 2 claims to have touched (`Doc_03_Lexicon_Candidate_List.md`, `Doc_04_Gravity_Discovery.md`, `Doc_05_Ecological_Reconstruction.md`, `Lexicon-Chunks/rzglex007_the-lords-supper-spiritual-presence.md`, `Lexicon-Chunks/rzglex008_sign-and-the-thing-signified.md`).
**Scope:** targeted recheck against `Doc07_Round1_Review.md`'s six findings, per this project's own Round-2+ cost discipline — not a full re-review from scratch. Every claim below was independently re-verified directly against the primary sources (`awk`/`sed` against the vendored `.txt` files, and direct reads of Doc_01/Doc_05's own text), not accepted on Doc_07's own revision note or on `Open_Gaps_Tracking.md` item 24's own account of the fix.

---

## Verdict: **Clear with cosmetic notes**

All six Round 1 findings are genuinely fixed at the root, not patched over — including Finding 1 (the HIGH-severity mirror-quotation fabrication), which required getting both the bracket placement and the line range right simultaneously, and Finding 5 (the six-file "Wherefore" elision), which required propagating an identical fix correctly across five sibling documents this build thread does not, in the ordinary case, have standing to touch. Both are genuinely and completely fixed, independently re-verified character-for-character against the vendored source rather than trusted from the revision note. However, the broad search this task specifically asked for (`grep` for "mirror" and "though we distinguish" across the whole world-build directory) turned up exactly the kind of missed-sibling defect this world's build has hit before: three other citations of the identical Second Helvetic "mirror" quotation (Doc_04 §3.1, twice, and `rzglex001`'s own Key Sources) still carried the pre-Doc_07-Round-1 citation style — "line 684" alone, with no bracket disclosing the "onr"→"our" OCR correction — that Doc_07's own Round 1 review specifically found insufficient for its own instance. None of these three is a fabrication (no bracket is misplaced, no invented phrase results), so none is escalation-worthy, but the precision standard Doc_07 now applies to itself was not carried to these three siblings. **Applied directly as cosmetic fixes** below, per this world's own established Round-2+ precedent (`Open_Gaps_Tracking.md` items 22–24) for exactly this situation, no further review round required.

---

## Finding-by-Finding

### Finding 1 — HIGH — Second Helvetic "mirror" quotation fabrication and mis-citation — **Genuinely fixed**

Checked directly against `cic/texts/schaff_second-helvetic-confession-heidelberg-catechism_1919.txt` with `awk`, not accepted on Doc_07's own claim. Line 684 reads exactly: `Let, therefore, Christ be the mirror in which we behold onr predes-`; line 685 completes: `tination.` Line 683 is confirmed blank.

Doc_07 §2B now reads: *"Let... Christ be the mirror in which we behold [our] predestination" (Bullinger, 1566, lines 684–685, correcting the source's own OCR-garbled "onr" to "our," disclosed rather than silently cleaned)."* The bracket now sits immediately before "predestination" — the word actually garbled in the source — not before "Christ," so the fabricated "our Christ" reading is gone and the sentence attests only what the source contains. The citation now reads "lines 684–685," correctly spanning both the line where "onr predes-" appears and the line where "tination" completes it. §2B's own construction note repeats the same corrected citation and explicitly names what was wrong in the prior draft. Both occurrences (main text and construction note) are internally consistent and match the source exactly.

The companion quotation on line 667 ("We reject those who seek out of Christ whether they are chosen") is independently confirmed exact.

### Finding 2 — MEDIUM — Misattributed Wittenberg-contrast quotation — **Genuinely fixed**

Checked `Doc_05_Ecological_Reconstruction.md` and `Doc_01_World_Identification_Boundaries_Orientation.md` directly. Doc_05 §6.3 does contain the exact phrase verbatim: *"the single sharpest structural contrast with the sibling Lutheran Wittenberg world."* Doc_01's own three uses of "sharpest" (Servetus's execution, the Dort/Beza throughline discussion, and the "sharpest intra-Reformed contest" reference to VI.9) confirm none of them is this comparison or this wording — consistent with Round 1's own finding.

Doc_07 §5 now reads: *"Doc_05 §6.3 already names the republican city-council structure... as 'the single sharpest structural contrast with the sibling Lutheran Wittenberg world' — Wittenberg's own reform proceeding through a princely territorial church rather than city-by-city civic disputation, the same underlying comparison Doc_01 §1 also draws, in its own words, without using this exact phrase."* The quotation marks now attach only to Doc_05 §6.3; Doc_01 §1 is cited separately, unquoted, as the source of the underlying comparative content — independently confirmed accurate: Doc_01 §1's own Distinctive Contribution paragraph does state the same comparison ("Wittenberg's reform runs through a prince's territorial church... where this world's reform runs through republican city-councils and consistorial courts") without the "sharpest" superlative.

### Finding 3 — MEDIUM — Beza's undisclosed motive claim — **Genuinely fixed**

Checked `Doc_01_World_Identification_Boundaries_Orientation.md` §7 directly. It states only the bare facts about the *Tabula praedestinationis*: 1555 publication, nine years before Calvin's 1564 death, and its role as "a real theological throughline toward the controversy the Remonstrance of 1610 answers." No motive for the timing is stated anywhere in §7 or elsewhere in Doc_01.

Doc_07 §3 now reads: *"Its own date — nine years before Calvin's 1564 death — is Documented (Doc_01 §7); that this timing served the same succession-proofing purpose the Second Helvetic Confession's own dating illustrates is this document's own inferred parallel, not a motive Doc_01 §7 itself states, and is named as such rather than carried at the same confidence as the dates themselves."* This is a root-cause fix, not a construction-note patch: the disclosure now sits in the main prose itself, where the original overclaim was, and the construction note repeats it. Genuinely fixed.

### Finding 4 — LOW/COSMETIC — Art. XVIII "verified verbatim" overclaim — **Genuinely fixed**

Doc_07 §2A's construction note now reads: *"Art. XVIII (paraphrased, not quoted, in this lens's own prose) is Documented... the 9th Head of Agreement (quoted verbatim above) is likewise Documented... — corrected at Doc07 Round 1 review, which found an earlier draft of this note claimed both were quoted verbatim, when Art. XVIII is only paraphrased here."* This exactly matches Round 1's suggested fix and remains accurate: §2A's own prose still only paraphrases Art. XVIII ("refusing a repeated sacrifice and a corporeal presence"), while the Consensus Tigurinus quotation is the one direct quotation in that lens. The independently-confirmed line range (4565–4569) is unchanged and accurate.

### Finding 5 — LOW/COSMETIC — Six-file "Wherefore" elision — **Genuinely fixed at all six occurrences, with one adjacent sibling gap found and fixed**

Checked directly against `cic/texts/calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt`: lines 768–770 read exactly *"Wherefore, though we distinguish, as we ought, between the signs and the things signified, yet we do not disjoin the reality from the signs."* All six named occurrences were checked directly, not merely trusted:

- `Doc_03_Lexicon_Candidate_List.md` §4 (Sign and the Thing Signified row) — "Wherefore, though we distinguish..." restored, cited 768–770, with inline disclosure note. **Matches source exactly.**
- `Doc_04_Gravity_Discovery.md` §3.5 (T2, pole b) — "Wherefore, though we distinguish..." restored, cited 768–770, with inline disclosure note. **Matches source exactly.**
- `Doc_05_Ecological_Reconstruction.md` §3 — "Wherefore, though we distinguish..." restored, with inline disclosure note (no explicit line cite at that spot, consistent with the surrounding prose style). **Matches source exactly.**
- `Lexicon-Chunks/rzglex007_the-lords-supper-spiritual-presence.md` Key Sources — restored, cited 768–770, with inline disclosure note. **Matches source exactly.**
- `Lexicon-Chunks/rzglex008_sign-and-the-thing-signified.md` Key Sources — restored, cited 768–770, with inline disclosure note. **Matches source exactly.**
- `Doc_07_Integrated_Ecology_Analysis.md` §2A (its own instance) — restored, cited 768–770, with inline disclosure note. **Matches source exactly.**

All six carry an inline disclosure note rather than a silent change, satisfying the specific requirement this task asked to check. No grammar break in any of the six: in every case "Wherefore" is inserted immediately after a colon or "that" introducing the quotation, which reads naturally in all six sentences.

**One adjacent point checked and found clean, not a defect:** `rzglex007` and `rzglex008` each also use the phrase "though we distinguish, as we ought, between the signs and the things signified, yet we do not disjoin the reality from the signs" a second time, inside their own inhabited-voice World Meaning narrative (unquoted, no citation attached) — e.g. *"both cities put their names to a single formula that neither had used alone before: though we distinguish..."* These are not presented as direct quotations (no quotation marks, no line citation), so the absence of "Wherefore" here is stylistic paraphrase in the inhabited voice, not a silently-elided quotation — the same technique Doc_07's own §6 Integrative Observation and Doc_05's own inhabited passages use elsewhere in this world's build. Confirmed not a defect.

### Finding 6 — LOW/COSMETIC — Forces Framework Principle 4 overstatement — **Genuinely fixed**

Doc_07 §4 now reads: *"Cross-cell connections, anticipating Doc_08's own required treatment (Forces Framework Principle 4, whose own text locates full documentation of cross-cell connections in Doc_08's own Forces-and-Gravities Synthesis specifically) — named here early, as disclosed synthesis, not as this document's own required output."* This no longer cites Principle 4 as though it specifically governs Doc_07's own Step 7 output; it now correctly discloses this section as anticipating Doc_08's own required work. Matches Round 1's suggested softening.

---

## Newly Introduced/Missed Sibling Errors — applied as direct cosmetic fixes per `cic-build-cycle`'s own rule, no further review round required

The task specifically asked for a broad `grep` across the whole `World-Builds/Reformed-Zurich-and-Geneva/` directory for "though we distinguish" and "mirror," to check whether either fix missed a sibling occurrence. The "Wherefore" fix (Finding 5) is complete and exact at all six named occurrences — no sibling missed. The mirror-quotation fix (Finding 1) is exact within Doc_07 itself, but the same underlying citation-precision gap Doc_07's own Round 1 review found and fixed in Doc_07 — an undisclosed "onr"→"our" OCR normalization and a citation that stops at line 684 instead of the full 684–685 range where "predestination" completes — was still present, unfixed, in three sibling citations of the identical quotation that Round 1 never scoped to check (Round 1 reviewed Doc_07 only; these three sit in already-Approved Doc_04 and `rzglex001`):

1. `Doc_04_Gravity_Discovery.md` §3.1, Formation test — cited "line 684" only, no bracket. **Fixed directly**: now "[our] predestination," lines 684–685, with inline disclosure note.
2. `Doc_04_Gravity_Discovery.md` §3.1, Confidence/Gravity Cross-Check — cited "line 684" only, no bracket (already carried one prior correction note from Doc04 Round 1 review, for the line-677→684 fix; the bracket/685 gap was never caught until now). **Fixed directly**, with an added disclosure note distinct from the existing one.
3. `Lexicon-Chunks/rzglex001_predestination-election.md` Key Sources — cited "line 684" only, no bracket. **Fixed directly**, with inline disclosure note.

A fourth, lower-stakes instance was also corrected for consistency: `Doc_05_Ecological_Reconstruction.md` §10's own Tier 4 traceability footnote cited "line 684" for the same element; extended to "lines 684–685" with a brief note. (Doc_05 §3's own inhabited-voice quotation of the same phrase carries no line citation at all, so there was nothing there to correct.)

None of these four is a fabrication — in every case the word rendered ("our") is the correct, sensible reading of the source's own OCR artifact ("onr"), and no bracket is misplaced before the wrong word. The defect class is citation-completeness and disclosure-consistency, not quotation fabrication, and none of it changes any substantive finding in Doc_04, Doc_05, or `rzglex001`. Per this world's own established precedent for exactly this situation (`Open_Gaps_Tracking.md` item 22's direct fix to Doc_03's header count during Doc_06 drafting; item 23/Doc06 Round 2's direct fixes to `rzglex004` and `rzglex007`), these are applied directly rather than requiring a fresh review round for either already-Approved document.

A "beatifies" citation-range note, checked but left unfixed as out of this task's specifically bounded search scope: `Doc_04_Gravity_Discovery.md` §3.1 cites the "beatifies" quotation at "line 9678" alone, while Doc_07 and `rzglex001` correctly cite "lines 9677–9678" (the quoted phrase begins on 9677). This task's search instruction was scoped to "mirror" and "though we distinguish" specifically; "beatifies" was not part of that instruction, and Round 1 confirmed Doc_07's own citation of it is exact. Flagged here for visibility, not corrected, since fixing it is outside this recheck's own defined scope — worth a note to the build thread for a future pass.

---

## `Open_Gaps_Tracking.md` Item 24 — checked for accuracy

Item 24 (the file's last entry) accurately describes what Round 1 found and what Revision 2 actually contains, independently cross-checked against the live Doc_07 text and the Round 1 review file:

- Correctly states no regression on the three previously-flagged defects (independently re-confirmed above: "beatifies" at lines 9677–9678 exact; Institutes IV.3.8 at lines 2831–2832 and 10503–10504 both exact; the mirror quotation's prior line-684 fix not regressed).
- Correctly and specifically describes the High, both Medium, and all three Low findings, matching `Doc07_Round1_Review.md` verbatim in substance.
- Correctly describes the fixes actually present in Revision 2 for all six findings, matching what is independently verified above.
- Correctly states the "Wherefore" fix was applied at all six occurrences with an inline disclosure note at each — independently confirmed true.
- **Correctly avoids claiming a disposition.** It ends "Round 2 targeted recheck pending," not "Approved to proceed" — accurate, since this recheck had not yet occurred when item 24 was written. No correction needed to item 24 itself.

---

## What checked clean (re-confirmed, not re-litigated)

- No regression on any of this world's three specifically-flagged prior defects (the "beatifies" quotation, the Second Helvetic "mirror" line-684/685 citation, the Institutes IV.3.8 loci), independently re-verified against the vendored files, not merely re-read from Doc_07's own text.
- The Consensus Tigurinus 9th Head of Agreement quotation's own line range (768–770) is accurate everywhere it appears, both before and after the "Wherefore" fix.
- No grammar was broken by inserting "Wherefore" at any of the six restored occurrences.
- The two inhabited-voice paraphrases of the same Consensus Tigurinus language in `rzglex007`/`rzglex008` (unquoted, no citation) are legitimate stylistic echoes, not silently-elided quotations, and required no fix.

---

## Summary

All six Round 1 findings are genuinely fixed at the root, independently re-verified against primary sources rather than the revision note's or `Open_Gaps_Tracking.md`'s own say-so. The one High finding (the mirror-quotation fabrication) is fully corrected: the bracket sits before the actually-garbled word, and the citation now spans both lines the corrected word occupies. The six-file "Wherefore" propagation is complete and exact at all six occurrences, each properly disclosed. The broad sibling search this task asked for found one real, narrow gap — three further citations of the same mirror quotation elsewhere in this world's build (Doc_04 twice, `rzglex001` once) that still used the pre-fix citation style — corrected directly as cosmetic fixes, plus one further citation-range extension in Doc_05 for consistency. Nothing found rises above Low/cosmetic, and nothing here blocks Doc_07 from proceeding.

**Escalation categories:** none apply. This is ordinary sourcing-fidelity and citation-precision work — no Representative identity/title/voice question, no cross-world/portfolio-level decision, no governance/methodology change, and no unresolved tension the pipeline itself cannot close.
