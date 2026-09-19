# Doc_04 (Gravity Discovery) — Round 2 Independent Adversarial Re-Review (Targeted)

**World:** The Reformed Cities — Zurich & Geneva (`rzg`)
**Document under review:** `World-Builds/Reformed-Zurich-and-Geneva/Doc_04_Gravity_Discovery.md`, DRAFT, Revision 2
**Scope:** Targeted recheck against `Review-Artifacts/Doc04_Round1_Review.md` findings 1–10 only, per this project's own Round 2+ cost discipline (`CLAUDE.md`: "targeted recheck ... against prior findings, not a full re-review from scratch") — not a full re-review.
**Re-verified against:** `Doc_01_World_Identification_Boundaries_Orientation.md`, `Doc_02_Source_Ecology.md`, `Doc_03_Lexicon_Candidate_List.md`, `Source_Registry.md`, `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml`, `cic/corpus-map/_staging/zwingli_selected-works_jackson1901.yaml`, and the vendored files `zwingli_selected-works_jackson1901.txt`, `calvin_institutes-christian-religion-vol3_beveridge1845.txt`, `schaff_second-helvetic-confession-heidelberg-catechism_1919.txt` — all read directly this pass, not taken on Doc_04's own word.
**Reviewer:** independent adversarial review agent, per `cic-build-cycle` / `cic-gravity-index`
**Date:** 2026-09-15

---

## Verdict: **Clear, with one cosmetic note**

All ten Round 1 findings are genuinely fixed — re-verified independently against the primary sources, not accepted on Doc_04's own revision notes. Every corrected quotation, citation, and cross-reference checked out exactly as claimed, the Source Registry and both corpus-map YAML files were updated consistently and both parse as valid YAML, the Interaction Matrix now genuinely covers all 15 required pairs with honest reasoning (including the newly-added G2↔G4 pair, which is a real, Doc_03-grounded reading, not a manufactured fill-in), and the two medium framing findings (8, 9) are now named as real tensions/corrections rather than smoothed over. One purely cosmetic self-inconsistency was introduced or left uncorrected: the document's own closing line still reads "DRAFT, Revision 1" against the masthead's "DRAFT, Revision 2."

---

## Findings 1–10, rechecked

### 1. [CRITICAL] Fabricated/altered Zwingli quotation — **Genuinely fixed.**

**Checked:** `zwingli_selected-works_jackson1901.txt`, line 9678, read directly this pass.

**Found:** the vendored file reads, verbatim: "God's election, predestination or marking out, calling, **beatifies**, you will ever say right." Doc_04 §3.1 (both the Repetition-test paragraph and the Confidence/Gravity Cross-Check paragraph) now quotes exactly this — "beatifies," no bracketed substitution — and both passages explicitly flag the Round 1 correction and name the discarded word ("[justification]"). Quotation matches the source exactly, character for character, at the cited line.

### 2. [HIGH] Load-bearing claim outside Source Registry row 7's declared date scope — **Genuinely fixed.**

**Checked:** `Source_Registry.md` row 7, `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml`, and `cic/corpus-map/_staging/zwingli_selected-works_jackson1901.yaml`.

**Found:** `Source_Registry.md` row 7's "Licensed For" field now reads "Zurich's own reform record, **1522–1527**," with an explicit note this was updated at Doc04 Round 1 review and reasoning why. Both corpus-map files were also updated, and — importantly — updated in the *correct direction*: the staging file (`_staging/zwingli_selected-works_jackson1901.yaml`, the actual source of truth per its own generated-file's header, "Edit the staging file... a re-merge overwrites it") carries the same corrected "1522-1527" language and the same reasoning, and the generated file (`the-reformed-cities-zurich-and-geneva.yaml`) matches it. A re-merge from staging would not silently revert this fix. Both YAML files parse cleanly (`yaml.safe_load` confirmed on both). Independently confirmed the underlying fact: the vendored file's own heading dates the *Refutation of the Tricks of the Ca[ta]baptists* "ZURICH, July 31, 1527" (line 5340), and its "On Election" section header is at line 9591 — both consistent with the corrected 1522–1527 range and with Doc_04's own cited loci.

### 3. [HIGH] Misattributed "seed form" cross-reference — **Genuinely fixed.**

**Checked:** `Doc_01_World_Identification_Boundaries_Orientation.md` §3/§4, `Doc_03_Lexicon_Candidate_List.md` §1.

**Found:** "in seed form" appears in Doc_01 at line 57 (within §3, "Distinct World Criteria") and line 65 (within §4, "World Separation Criteria") — confirmed by section-header line numbers (§3 starts line 52, §4 starts line 61, §5 starts line 78). It also appears in Doc_03 §1 (Candidate Roster, line 39, Predestination row: "present in seed form in Zwingli's own providential theology"). Doc_04 §3.1 now cites exactly "Doc_01 §3/§4 and Doc_03 §1 (Predestination candidate row)" and no longer cites Doc_02 §2 at all. Citation is accurate.

### 4. [HIGH] Decontextualized "carnal" citations — **Genuinely fixed.**

**Checked:** all three cited lines (5422, 6931–6932, 8266–8289) plus a full-file grep for "carnal" in `zwingli_selected-works_jackson1901.txt`.

**Found:** Doc_04 §3.2 (Dependency test) and §6 (Interaction Matrix, G2↔G3) both now explicitly disclose the Round 1 correction, state plainly that no vendored "carnal" occurrence supports a Eucharistic reading, and state the Dependency/Interaction relationship in general terms without citing a specific line for it. Re-ran the full-file grep independently: all occurrences of "carnal" in the file (5422, 6931, 6932, 7784, 8266, 8270, 8287, 8289, 8345) are in the civil-magistracy/Anabaptist/marital-discipline register, none in a Eucharistic context — confirms the correction is accurate, not merely asserted.

### 5. [HIGH] Interaction Matrix "full pairwise coverage" claim, 6 of 15 pairs missing — **Genuinely fixed.**

**Checked:** §6, counted all listed pairs against the 15 required (6-choose-2).

**Found:** all 15 pairs are now present: G1↔G2, G1↔G3, G1↔G4, G1↔T1, G1↔T2, G2↔G3, G2↔G4, G2↔T1, G2↔T2, G3↔G4, G3↔T1, G3↔T2, G4↔T1, G4↔T2, T1↔T2. The section's own header now correctly states this was corrected at Round 1 review rather than re-asserting "full pairwise coverage" as an unexamined given.

**New-pair honesty check (per this round's brief):** each of the 6 newly-added pairs gives a specific, checkable reason rather than being filled reflexively:
- G1↔T1, G1↔T2, G2↔T1, G4↔T2 are all reasoned "–" (no relationship), each with a specific stated reason (different axes, no vendored text connecting them) rather than a bare dash.
- G3↔T2 ("R") is defensible: both of T2's poles (Zwingli's 1523 Art. XVIII; the Consensus's 1549 formula) are indeed scriptural-exegetical products, consistent with G3's own definition.
- **G2↔G4 ("R") specifically checked, per this round's brief.** Doc_03 Cluster 4's own "Excommunication" entry (line 66) defines it in Doc_03's own words as "Formal exclusion from **the sacraments** and the visible church for unrepented sin — the Consistory's own most severe disciplinary tool." This directly and independently supports Doc_04's claim that excommunication "operates directly on access to G2's own sacrament" — the relationship is grounded in Doc_03's own existing definition, not manufactured to complete the count.

### 6. [MEDIUM] Second Helvetic "mirror" quotation mis-pinpointed at line 677 — **Genuinely fixed.**

**Checked:** `schaff_second-helvetic-confession-heidelberg-catechism_1919.txt`, lines 660–689, read directly.

**Found:** line 667 reads "We reject those who seek out of Christ whether they are chosen" (as before, correctly cited). Line 684 reads "Let, therefore, Christ be the mirror in which we behold o[u]r predestination" (an OCR "onr"/"our" artifact in the source scan, immaterial to the quoted wording) — confirmed at exactly line 684, not 677. Both of Doc_04's two citations of this quotation (§3.1 Formation test, and §3.1 Confidence/Gravity Cross-Check) now cite line 684 and both explicitly flag the correction.

### 7. [MEDIUM] "Sacrifice of the mass" line 20657 does not contain the phrase — **Genuinely fixed, replacement citations verified.**

**Checked:** `calvin_institutes-christian-religion-vol3_beveridge1845.txt`, lines 20735, 20812, 20934, 20943 (the new citation set, replacing 20657/20735/20812/20934).

**Found:** all four lines independently confirmed to contain the phrase or its immediate variant:
- 20735: "...the oblation of Melchizedek was a figure of **the sacrifice of the mass**..."
- 20812: "...they rear up **their sacrifice of the mass**..."
- 20934: "...**the sacrifice of the mass** pretends to give a price to God..."
- 20943: "**The sacrifice of the mass** uses a very different language..."

Line 20657 is no longer cited anywhere in the document (confirmed by search). This is a clean fix with an accurate replacement set, not a fix that merely relocated the error.

### 8. [MEDIUM] "Sharpens without contradicting" oversoftened the tension — **Genuinely fixed.**

**Checked:** §3.1 Repetition-test paragraph and §7 carry-forward instruction.

**Found:** §3.1 now explicitly states the finding "complicates, without simply overturning" Doc_01's characterization, names this "a tension this document names rather than resolves," and states plainly that "Doc_01's own 'seed form' language was never scoped to the Sixty-Seven Articles specifically." §7's first bullet now instructs Doc_05 to "carry this document's own finding on Zwingli's 1527 election exposition (§3.1) forward, including the named tension with Doc_01's own 'seed form' language, rather than repeating that characterization unqualified." This matches the Round 1 fix requirement to name the tension plainly rather than fold it into an easy reconciling frame.

### 9. [MEDIUM] Augustinian-inheritance cell placement — **Genuinely fixed.**

**Checked:** Doc_01 §6's six-cell table and its "What larger world was it embedded in" prose.

**Found:** Doc_01 §6's own table places "The late-medieval Latin church's own sacramental and clerical order, contested from within the Swiss Confederacy's own decentralized city-state structure" at **Cell 1A (External, Initiating)**, while Cell 1B is explicitly reserved for "two independent local triggers" (Zwingli's 1519/1522 Zurich origin; Geneva's 1526/1536/Calvin-1541 origin). The Augustinian-inheritance quotation ("a direct theological line across eleven centuries...") sits in the "What larger world was it embedded in" prose, introduced as "more distantly, the Augustinian tradition" — an external antecedent, not one of the two local founding acts. Doc_04 §3.1's forces-connection now places this in **Cell 1A**, explicitly correcting the earlier Cell 1B placement and explaining why Doc_01's own table does not support 1B. This is the more defensible reading of Doc_01's own logic.

### 10. [MEDIUM] Dropped Beza/Dort "at one remove" hedge — **Genuinely fixed.**

**Checked:** Doc_01 §7's exact wording.

**Found:** Doc_01 §7 states: "though at one remove: Arminius's own immediate teacher was Beza at Geneva, but his immediate opponents at Leiden were Franciscus Gomarus and Franciscus Junius, not Beza directly." Doc_04's Confidence/Gravity Cross-Check paragraph (§3.1) now restates this accurately in compressed form: "at one remove — Arminius's own immediate teacher was Beza, but his own immediate opponents at Leiden were Gomarus and Junius, not Beza directly, the same qualification Doc_01 §7 itself states." Substance preserved; only cosmetic compression (dropping "at Geneva" and first names), which does not change the claim.

---

## Newly-introduced errors

**One found, cosmetic only:** the document's closing line (final paragraph, end of file) still reads *"DRAFT, Revision 1"* — "*End Doc_04. Companion: `Gravity_Index.xlsx` (not yet built). **DRAFT, Revision 1.** Classification: 3 Primary, 1 Supporting, 2 Tensional, 2 not advanced...*" — while the document's own masthead (line 9) correctly states "**Status:** DRAFT, Revision 2." This is a genuine self-inconsistency about the document's own revision number, the kind of thing `CLAUDE.md`'s governance-vocabulary discipline cares about getting right, but it carries no sourcing or content risk — it does not affect any finding, quotation, citation, or classification above. Recommend a one-line fix (footer to "Revision 2") before this document is treated as closed at this stage; does not itself warrant another full review round.

No other newly-introduced errors were found in the specific areas checked (the 6 new Interaction Matrix pairs, the 3 corrected citation loci, the Doc_01/Doc_03 cross-reference correction, and the two updated YAML files).

---

## Summary

All ten Round 1 findings are genuinely and correctly fixed on independent re-verification against the primary sources; one cosmetic revision-number self-inconsistency (footer "Revision 1" vs. masthead "Revision 2") should be corrected but does not block proceeding.

**Escalation categories:** none apply. This was ordinary sourcing-fidelity and citation-accuracy recheck work within a single document's own build cycle — it does not touch Representative identity/title/voice, portfolio-level or cross-world scope, governance or methodology, or an unresolved tension the pipeline itself cannot close. All findings above (and the one cosmetic note) are correctable by the build thread itself, at Doc_04's own revision stage, per `cic-build-cycle`'s ordinary self-governance.
