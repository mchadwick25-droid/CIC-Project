# Doc_04 — Gravity Discovery: Latin Pastoral-Congregational Christianity
## Round 4 Independent Adversarial Review — fix-pass verification of Round 3's 20 findings, plus a fresh adversarial read

**Documents reviewed (working tree, branch `lpc-doc04-round2`, at `17d22645`, tree clean):**
- `worlds/lpc/Doc_04_Gravity_Discovery.md` (231 lines) — read in full; both tables parsed programmatically cell-by-cell; all 28 Interaction Matrix pairs machine-checked for symmetry and then checked cell-by-cell against each candidate's own §3 Interaction bullet; the pre-fix state retrieved from git (`ccb25f37`) and diffed against HEAD (`17d22645`) at `-U0`, all 22 hunks read individually — **and, separately from the diff, every section of the document was read at HEAD and searched for the propositions the fix pass claims to have retired, not only for the strings it claims to have removed**
- `Review-Artifacts/Doc04_Round3_Review.md` (353 lines) — read in full; every one of the 20 findings (H1–H6, M1–M5, L1–L6, C1–C3) checked individually at its own named destination and at HEAD. **Round 3's own quotations and renderings were not trusted either**: every quotation the fix pass reproduces from Round 3 was re-derived from its own source file. This caught two (R4 H3 and R4 M1 below), one of them a claim Round 3 had affirmatively certified clean
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines) — §2, §4 (all three authority axes, both deferred World Separation bullets, the Conclusion), §5 (all three Article 21 criteria, the Article 3 argument, the Formation-emphasis and ecological-orientation bullets, the governing-consequence paragraph and the reopening caveat), §6, §8 items 6, 7, 10 read verbatim; direct greps run for `closest call`, `does not clearly touch`, `not yet closed`, `with particular weight`, `once made, governs`, `right of communion`, `persists in a different`, `genuinely lapsed`, `anti-Manichaean`, each located by section
- `Doc_02_Source_Ecology.md` (158 lines) — §1, §2 (both Representativeness and both Influence dimensions in full), §5, §6, §8 (the Confidence Map bracket) read verbatim; grepped for `right of communion` (**0**), `proper right of judgment` (1)
- `Doc_03_Lexicon_Candidate_List.md` (98 lines) — rows 26, 27, 28, 29, 30, 36, 39, 40, 46, 47, 54, 55, 63 parsed cell-by-cell from the raw table; the 687, 31, 119, 113, 57/39/17, 96/114, ~150/128, ~120, 31/20 and 1,798/1,665 figures **and the row-scope attached to each** re-derived from the cell each figure sits in
- `Source_Registry.md` (329 lines) — confidence letters for rows 1, 2, 3, 4, 5, 7, 12, 13, 15, 18, 19, 21, 22, 23, 65, 192 parsed **by field** from the pipe table, not read from prose; rows 1, 4, 22 and 65 read in full; the whole file grepped for `right of communion` (**0**)
- `lpc_Decision_Log.md` (624 lines) — the 2026-09-13 (third) entry read in full and tested against the file it describes; the two in-place corrections to the 2026-09-13 (later) entry diffed and tested; the 2026-09-13 Registry entry read for the set of corrected rows
- `L1-Foundation/CiC_L1_Constitution_V2_2.docx` — extracted verbatim (python `zipfile` + regex on `word/document.xml`); Articles 21 and 22 read in full, including the paragraph that carries the cross-strand clause; whole file counted for `reopen` (**0**) and `revisit` (**0**)
- `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — same extraction; Part III read in full, **and the Tensional paragraph re-extracted run-by-run with its run properties, to test emphasis and not only wording**
- `L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx` — same extraction; Layer 3 and Section 4's Step 4 entry read verbatim
- `L3B-World-Build-Methodology/Doc_04_Gravity_Discovery_Template_V1.0.md` — §4 (the classification labels and the summary-table header) and §5 (the substitute-discipline requirement and the World #9 model example) read verbatim
- `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` — existence and size confirmed on this branch (5.1 MB); not read for content

**Review date:** 2026-09-13
**Reviewer:** independent adversarial review thread. Did not draft Doc_04, did not draft the Round 3 review or the Round 3 fix pass, did not draft Doc_01, Doc_02, Doc_03, the Registry or the Decision Log, and ran no prior round in this world's build history.

**Method note.** This is a fix-pass verification plus a fresh adversarial read, run under this build's own documented failure mode: *"a check that proves something adjacent to the claim, then trusted because it returned something."* The Round 3 fix pass states, in its Status line, its Document Log entry and its Decision Log entry, that it ran a **destination check**: for every finding the destinations the fix claims to reach were listed in advance, then opened and read at HEAD, and asserted to carry the change — thirty destinations across twenty findings, all thirty verified, plus seven superseded false claims asserted absent. **That claim was tested, not credited.**

The test was built around what a destination check *cannot* prove. It proves a **string is present at a listed site**. It does not prove (a) that the inserted text is factually correct; (b) that the listed sites were the only sites needing the change; (c) that the insertion is coherent with the paragraph it landed in; (d) that the change did not break something adjacent. Accordingly: every governing quotation introduced this pass was re-extracted from its own file (including run-level emphasis, not only wording); every proposition the pass says it retired was searched for **in paraphrase across the whole document**, not only as the string the pass removed; every fix's landing paragraph was re-read whole; and the set of sites asserting each retired proposition was rebuilt independently rather than taken from the document's own list. Corpus sweeps were **not** re-run; Doc_03's disclosed sweep results were checked as citations, including the row-scope each figure carries.

Marking per Constitution Article 31: **Simulated review — informational only, not an Article 31 substitute.**

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 6 HIGH · 5 MEDIUM · 6 LOW · 3 COSMETIC — 20 in total.**

**Fix-pass verification tally, against Round 3's 20 findings: 16 genuinely fixed · 4 partially fixed · 0 not fixed.** Of the 16 genuinely fixed, **3 introduced a new defect** (H3, H6, C2); all 4 of the partials did (H1, H4, H5, M4).

**The destination check worked, exactly as far as it reaches, and the failure mode migrated into the gap it leaves.** All thirty listed destinations do carry their change — verified individually at HEAD. All seven superseded strings are genuinely absent: `Tensional test run above` (0), `That distinction is what carries` (0), `Article 21 column` (0), `larger volume it sits inside` (0), `answers Round 1's findings` (0), `tested and confirmed as its own bounded` (0), `reaches Tensional on the Framework` (0), `Cross-Strand Gravity testing` (0). Nothing this pass claimed to fix is byte-identical. The LOW enumeration now sums; the Disposition names the right round; the Decision Log's two false sentences are corrected in place, honestly and in terms.

**And the same mechanism is present anyway, in a new form. It has moved from the *site* to the *proposition*.** The check verified that strings are present at listed sites and that old strings are gone. It could not, and did not, verify that the **claim** the old string carried had stopped being asserted elsewhere. Three times, a proposition the pass certifies as retired is still asserted at a site that was never on the list:

- **`by definition does not organize broadly`** — one hit, at line 175, §5's own **Finding** sentence, in the same section where, 200 words earlier, the pass writes *"An earlier version of this sentence derived that from the Framework's Tensional definition, and misstated it."* The string H4 struck is gone; the proposition H4 struck is not (R4 H2).
- **§3 line 99**, four lines above the line 107 the pass corrected for saying the Tensional test had been run, still says the Framework's Tensional definition is *"applied, not paraphrased"* and quotes both limbs. Line 103 says the second limb was *"never run."* The fix pass opened line 107 and did not open line 99 (R4 H1).
- **§7 Open Item 3**, byte-identical to `ccb25f37`, still says *"Candidate 5 is classified Tensional, a real Framework category, once the Supporting and Tensional definitions are actually run against it."* (R4 H1).

The root cause is visible on the page. The fix pass took its destination list for the escalation from **§3 line 105's own four-item list** — *"§4's summary row, §5's non-reopening argument, §6's matrix inclusion, §7 Open Item 2"* — rather than searching the document for every place the proposition is asserted. Line 105's list was wrong, and the destination check inherited its error without being able to see it. A list checked exhaustively is still only as complete as the list.

**And one claim in the newly inserted text is simply false at source.** The M4 fix moved the "right of communion" correction into a new trailing parenthetical at Candidate 3 and carried its attribution across unchecked: the clause is said to belong to *"Doc_01 §4 and §5 and Registry row 4."* The phrase `right of communion` occurs **zero times in `Source_Registry.md`** — in row 4 or anywhere else. Round 3 certified this attribution clean in its own "checked hard and found clean" list. It is a pointer to a real target carrying a claim the target does not support: Round 2's H2 mechanism, reproduced inside the fix for the finding that touched it, and now surviving two rounds of review (R4 H3).

**Twelve things were checked hard and found clean, and should be stated before the findings:**

1. **Both tables are structurally clean, and the fix pass did not break either.** Machine-parsed at HEAD: pipe counts uniform (6 across all ten Classification Summary lines, 10 across all ten Interaction Matrix lines); `**` and backtick nesting balanced on every table line.
2. **All 28 Interaction Matrix pairs are symmetric**, machine-checked at HEAD, with the one deliberate asymmetry (2↔7 "Reshaped by" / 7↔2 "Reshapes") correctly directional. **All eight §3 Interaction bullets were then checked cell-by-cell against their own matrix rows: all eight agree, with no omission and no over-claim.** §6's assertion that no candidate's row is entirely "no demonstrated relationship" is true against the table. Candidate 5's row is exactly three reinforcing, four none, zero competing or reshaping — the count §3 and the Decision Log both state.
3. **M1's fix is exact at source, in the strong form.** Constitution Article 21 is headed *"Strand Determination Principle"* and its second paragraph reads verbatim: *"Whether a world contains distinct internal strands is a construction finding that, once made, governs all subsequent strand attribution; where strands exist, convergence across them is a test of a gravity's centrality. The method of strand determination and cross-strand gravity testing is governed by the Construction Framework."* Article 22 is headed *"Forces Principle."* The corrected Governed-by line is right on both articles and quotes the convergence clause character-for-character. `reopen` and `revisit` each occur **0** times in the whole Constitution — Round 3's H4 finding independently re-confirmed. Forces Framework V1.1 §4 Step 4 independently attributes the cross-strand convergence test to Article 21 as well.
4. **M2's fix is exact, per row, and the letters were parsed by field.** Row 1 = **A**, row 2 = **B**, row 7 = **A**; row 4 = A, rows 5/15/18/19/21/22/23 = B, rows 12/13 = A, row 65 = C, row 192 = A. Candidate 2's new clause (*"the *De Lapsis* locus (Registry row 2) sits at Confidence B; the Epistles and Pontius loci (rows 1 and 7) sit at A"*) and Candidate 8's (*"the Epistles (Registry row 1) sit at Confidence A and *De Lapsis* (row 2) at B"*) are both correct. The unchanged blanket clause at Candidates 4 and 7 remains correct at those two.
5. **M5's substantive claim is true, and was verified against the corrected-row set rather than against the sentence.** The 2026-09-13 Registry entry names the seven corrected rows as **37, 44, 56, 64, 65, 206, 208**. Every Registry row Doc_04 cites was enumerated from the document itself (1, 2, 3, 4, 5, 7, 12, 13, 15, 18, 19, 21, 22, 23, 65, 192); none other than 65 is among the seven. The sentence's "which include" is non-exhaustive and therefore survives its own omission of row 3.
6. **L1's fix is exact at the cell the figure sits in.** Doc_03's `heresy` row reads *"'baptism' occurs 687 times within the treatise itself, markup stripped, scoped to its own div2 boundaries — the length at which the question is argued"*; Doc_04 line 111 now reproduces that character-for-character and attributes it to that entry's own words. The composite qualifier from the `plenary Council` row is gone (0 hits).
7. **Doc_03's tag cells and its other nine frequency figures are unchanged and still correct as values**, each re-derived by parsing its own row: `[AS], [TC], [PV]` (row 46), `[SC], [TC], [PV]` (row 47), `[SC], [TC], [DR]` (row 55), `[SC], [RT]` / `[SC], [TC], [RT]` (rows 27/28); 119 in row 19's bounds; 31 "plenary" in row 13; 96/114 for "the lapsed"; ~150 corpus-wide and 128 in row 1 for "confessor"; ~120 for "communion"; 31/20 for "penitence"; 1,798 raw / 1,665 stripped for "grace".
8. **Doc_01's locating claims are all correct at HEAD.** §8 item 10 is quoted verbatim, including the bracketed *"surfac[ing]"*. `closest call` occurs three times — twice in §4, once in §5, and **not** in §8 item 10, exactly as M3's fix now states. `does not clearly touch` occurs twice — in §2's transition-criteria summary (line 28) and §5's authority-structure bullet (line 92) — and **not** in §4, exactly as L3's fix now states. `with particular weight` is present at both §4 and §8 item 7, as attributed. Doc_01 §4 does in fact carry exactly two conciliar-authority quotations, and they are the 256 preface and *On Baptism* II.3's "authority of plenary Councils," as §5 now says.
9. **Registry row 65 checks out in full, and the *Gesta* bound is consistent across §3, §5 and Open Item 6.** The Verification Note carries the Migne path, the Internet Archive item, the 2026-09-13 corpus-map assignment at `role: context` / `confidence: provisional`, the fourteen numbered acts stated **as a floor** with the explicit instruction that any restatement carry the floor, and the closing words *"available to Doc_04, and not yet drawn on by it."* Row 65's Source cell is Lancel's in-copyright SC edition at Confidence C, as §3 now discloses. The vendored file exists on this branch. L5's and L6's fixes are both discharged, and §3, §5 and Open Item 6 agree on the bound.
10. **Every other governing quotation re-extracted from the `.docx` files is verbatim.** CF V7.4 Part III: the gravity definition (*"A gravity is a force around which multiple dimensions organize. A topic recurs. A gravity organizes."*), the Primary paragraph (*"They shape formation pervasively"*), the Supporting paragraph, the Cross-Check rule (*"noted explicitly rather than resolved by upgrading the classification"*), the Author Gravity rule (*"at the point of generation, before it is tested"*), the Interaction-Test warning. Part III names only Primary, Supporting and Tensional. Forces Framework V1.1 §4 Step 4: *"A gravity that cannot be connected to the forces acting on the world is a gravity whose ecology is incomplete"* — verbatim and genuinely in Step 4. The Template's V7.3 companion line, §4 label list, §4 summary-table header and §5 World #9 substitute requirement all check out as cited.
11. **The Decision Log's two in-place corrections to the 2026-09-13 (later) entry are accurate and honest.** Both were diffed and tested against the file. The "flagged provisional" sentence is correctly retracted and correctly characterised (*"all four sites were byte-identical"* — verified true of `ccb25f37`). The "every governing quotation re-derived" claim is correctly narrowed with the 687 exception named at the right row. Neither correction overstates what it fixes.
12. **Two of the pass's own structural certifications hold.** The non-ASCII inventory is exactly `§`, em dash, en dash and `↔` (249/215/9/2). `grep -c "Article 3" Doc_02_Source_Ecology.md` still returns 0, and `right of communion` still returns 0 in Doc_02. Nothing Round 3 certified clean at items 1, 2, 3, 4, 6, 7, 8 and 9 of its own list was broken by this pass — **with the single exception of its item 5**, half of which was never true (R4 H3).

**Where the findings are.** They cluster where Round 3's did — on Candidate 5 — but the subject has shifted once more. Round 3's HIGHs were about the escalation being declared and not carried. This pass carried it to the four sites §3 names and the escalation is now genuinely visible at §4, §6 and Open Item 2. **Four of six HIGHs here are about what a per-site check cannot see: a proposition still asserted at unlisted sites, a struck proposition restated in different words inside the same section, an inserted claim that is false at source, and a governing trigger quoted correctly and then tested at the wrong scope.** The fifth is a six-test result the fix pass contradicted without noticing. The sixth is the certification, for the fifth consecutive round.

---

## HIGH

### H1 — The escalation is carried to the four sites §3 lists and to no others: three further sites still assert Candidate 5's classification — and the Tensional test itself — as settled, and one of them is four lines from the escalation

**Sites:** line 99 (§3, the Classification paragraph — untouched); line 175 (§5's Finding — touched, contradiction left standing); line 211 (§7 Open Item 3 — **byte-identical to `ccb25f37`**, md5-confirmed). The list that produced the omission is line 105.

The escalation itself is real and the four sites it names now carry it. §4's cell reads **"Tensional (provisional — classification escalated to the project lead; see §3 and §7 Open Item 7)"**; §6 reads *"its inclusion does not depend on the Tensional label, which is escalated and pending"*; Open Item 2 opens *"Candidate 5's classification is escalated and pending — read §7 Open Item 7 before relying on anything in this item."* That is good work and it answers Round 3's H1 as stated.

But §3 line 105 defines the destination set as *"every use of it in this document — §4's summary row, §5's non-reopening argument, §6's matrix inclusion, §7 Open Item 2."* That enumeration is not complete, and the destination check adopted it wholesale. Three further sites assert the disputed proposition:

- **Line 99, §3's own Classification paragraph, four lines above the escalation**, closes: *"...which is **the Framework's own Tensional definition applied, not paraphrased**: 'persistent counter-forces, alternatives, or unresolved pressures within the ecology... [that] prevent the ecology from being reducible to its primary forces.'"* Line 103 states the opposite in terms: *"this document argues the first (an unresolved pressure) and **never runs the second** — 'prevent the ecology from being reducible to its primary forces'."* This is the identical contradiction Round 3 found at line 107 and the pass corrected at line 107 — in the same subsection, four lines earlier, unopened. Note also that line 99's ellipsis-and-bracket (*"...[that] prevent..."*) deletes the hedged first limb and re-attaches the second as a relative clause: the same structural misreading of the definition that H4 found at §5 and struck there.
- **Line 175, §5's Finding** — see H2.
- **Line 211, §7 Open Item 3:** *"This candidate did not, in the end, need that label: **Candidate 5 is classified Tensional, a real Framework category, once the Supporting and Tensional definitions are actually run against it (§3 above) rather than reached past.**"* And, later in the same item: *"this document's own use very nearly repeated it before **the Supporting/Tensional test above was actually run**."* Both sentences assert the settled classification and the run test. The item is byte-identical to the pre-fix state.

**Why HIGH.** Open Item 3 is a carried-forward item, addressed to whoever picks this document up next, and it tells them the classification is settled on a test §3 says was never run. Line 99 is the paragraph a reader reaches *first*, before the escalation, and it certifies the definition as applied. The Decision Log's account — *"the escalation now reaches all four sites §3 names"* — is true and reads as completeness when it is not. This is the failure mode's newest form: the check was exhaustive over a list that was itself the defect.

**Fix:** at line 99, replace *"which is the Framework's own Tensional definition applied, not paraphrased"* with a statement that this is the first limb of the definition only, and restore the elided *"They may not organize as broadly as primary gravities but"* rather than bracketing past it. At Open Item 3, replace *"Candidate 5 is classified Tensional, a real Framework category, once the Supporting and Tensional definitions are actually run against it"* with the pending form — the Supporting test was run and failed; the step to Tensional is escalated (§7 Open Item 7) — and strike *"before the Supporting/Tensional test above was actually run."* Then **replace line 105's four-item list with a statement of the proposition** ("every place this document states or implies that the Tensional classification is reached, tested or confirmed"), so the next pass's destination list is derived by searching for the claim rather than copied from a list.

### H2 — §5's Finding sentence restates the Tensional misstatement H4 struck, in different words, 200 words after §5 itself retracts it — and re-rests the non-reopening on the escalated label that the same paragraph has just said it does not rest on

**Site:** line 175 (§5, the **Finding**; a `+` line in this pass's diff — the fix pass wrote this line and left the clause in it).

The pass split the old §5 closing paragraph in two. The new paragraph at line 173 does exactly what Round 3's H4 and H5 asked: it retracts the misstatement in terms —

> *"**An earlier version of this sentence derived that from the Framework's Tensional definition, and misstated it:** CF V7.4 reads "They *may* not organize as broadly as primary gravities **but they prevent the ecology from being reducible to its primary forces**" — a hedged first limb and an operative second one, not a categorical disqualifier. That second limb is the escalated question (§3), and nothing here rests on it."*

— and re-bases the argument: *"**The label placed beyond that is escalated and pending (§3; §7 Open Item 7), and the non-reopening finding below does not rest on it.** What carries the non-reopening is Doc_01 §8 item 10's own trigger."*

Line 175, the very next paragraph, is the Finding:

> *"**Finding: on the evidence weighed, Doc_01 §5's own strand-singular determination stands, unreopened. This is a revision of the argument that carries the non-reopening — from "not a gravity" to "a Tensional gravity, **which by definition does not organize broadly**" — not a reopening of the finding itself...**"*

Two defects in one clause, both of them the ones the pass certifies as fixed:

- *"which by definition does not organize broadly"* is the struck proposition. The string H4 named (`does not organize the ecology broadly enough`) is gone — 0 hits. This paraphrase of it survives — 1 hit — and it is the only surviving instance in the document. CF V7.4's first limb is hedged (*"may not organize as broadly"*) and was never a definition of what a Tensional gravity does not do. §5 retracts this and then states it again, inside the bolded Finding.
- *"the argument that carries the non-reopening ... a Tensional gravity"* says the non-reopening **is** carried by the classification. Line 173 says it is not (*"does not rest on it"*), and line 105 says the same (*"The non-reopening finding at §5 is therefore independent of how this classification resolves"*). Round 3's H5 was precisely that §3 and §5 gave incompatible accounts of what carries the non-reopening. The accounts are still incompatible; only the location of the incompatibility has moved, from across two sections to across two consecutive paragraphs.

**Why HIGH.** This is the bolded sentence a reader takes away from §5, and it is the sentence that stands an Article 21 determination on a label under escalation. A destination check that opens §5 and confirms it carries "escalated and pending" returns a pass on this section while the Finding it closes with says the opposite. That is the failure mode exactly: a check that proves something adjacent to the claim.

**Fix:** rewrite line 175 to remove both clauses: *"**Finding: on the evidence weighed, Doc_01 §5's own strand-singular determination stands, unreopened — on Doc_01 §8 item 10's own trigger and Article 21's 'once made, governs,' independently of Candidate 5's classification, which is escalated and pending (§7 Open Item 7).** This is a revision of the argument that carries the non-reopening, not a reopening of the finding itself..."*

### H3 — The M4 fix repoints the "right of communion" clause to Registry row 4; the phrase occurs zero times in `Source_Registry.md`

**Site:** line 56 (Candidate 3's *Generated from:*, the trailing parenthetical — **new text in this pass**).

The M4 fix moved the correction out of the middle of the citation list and into a trailing parenthetical, which is what Round 3 asked for. In doing so it carried the attribution across without re-deriving it:

> *"*(The companion "right of communion" clause — "judging no man, nor rejecting any one from the right of communion, if he should think differently from us" — belongs to Doc_01 §4 and §5 and **Registry row 4**, not to Doc_02, which does not contain the phrase.)*"*

Checked by direct grep over the whole file: `right of communion` occurs **0 times in `Source_Registry.md`**, and `rejecting any one` 0 times. Row 4's Licensed-For cell was read in full; it carries *"neither does any of us set himself up as a bishop of bishops... every bishop, according to the allowance of his liberty and power, has his own **proper right of judgment**"* — the other clause, the one Doc_02 §1 carries. The clause Doc_04 is re-homing is not in row 4, not in the Registry at all.

Where it actually occurs, across this world's non-review files: `Doc_01` three times (§4 line 73, §5 line 104, §8 line 213) and **`Doc_03` row 54**, the "communion (preserved despite disagreement)" entry — which Doc_04 cites two sentences earlier and which the parenthetical does not name.

**Why HIGH.** This is Round 2's H2 mechanism — a pointer repointed to a real target with the claim carried across unchecked — reproduced inside the fix for Round 3's M4, in a sentence whose entire purpose is to correct a mis-homing. It also survived a round of review: Round 3's own clean list, item 5, states *"it is present at Doc_01 §4, Doc_01 §5 and Registry row 4."* The fix pass's destination check opened line 56 and confirmed the correction is there; nothing in that check asks whether the correction is true. This is gap (a) — the inserted text is present and wrong.

**Fix:** *"belongs to Doc_01 §4 and §5 and Doc_03's own 'communion' entry (row 54), not to Doc_02, which does not contain the phrase — nor does the Registry."* Verify by grep before the sentence stands.

### H4 — §5 quotes Doc_01 §8 item 10's trigger correctly and then tests a narrower proposition, certifying the trigger "not met" on a check adjacent to the one item 10 requires

**Sites:** line 173 (§5 — new in this pass); line 105 (§3 — the same substitution, in the paragraph that lets the escalation proceed).

Doc_01 §8 item 10, verified verbatim, makes reopening turn on: *"...until and unless **Doc_04's own formal six-test assessment, weighing this axis directly, surfaces evidence this document has not weighed** — in which case the finding is reopened rather than defended past the evidence."* Doc_04 quotes this accurately, with a correct bracket.

What Doc_04 then runs is a different test:

> *"**This document re-weighed Doc_01 §4's own two quotations — the 256 preface and *On Baptism*'s "authority of plenary Councils" — and surfaced no evidence Doc_01 had not already weighed. The trigger is therefore not met**"*

and, at line 105: *"this document re-weighs Doc_01's own two quotations and surfaces none."*

Item 10 asks whether **Doc_04's own six-test assessment** surfaced evidence Doc_01 has not weighed. Doc_04 answers whether **re-weighing Doc_01's own two quotations** did. Those are different questions, and Doc_04's own six-test assessment did draw on material outside Doc_01's two quotations: Doc_03's corpus sweep of "plenary" within Row 13 (31 occurrences, scoped to div2 — a figure Doc_01 never had), the negative result from searching Cyprian's Novatianist/Felicissimus correspondence for a second authority-theory locus, Doc_02 §2's Influence dimension, and — named by Doc_04 itself in the same paragraph — the *Gesta*, a source Doc_01 never weighed, which the Registry records as *"available to Doc_04"*, and of which Doc_04 says two sentences later: *"**If a targeted read surfaced such material it would be evidence Doc_01 has not weighed, and item 10's trigger would be met.**"*

The conclusion may well survive the right test. But it is stated in bold, unqualified — *"The trigger is therefore not met"* — before the paragraph discloses that the assessment on which the trigger turns is bounded and its most obvious source unread, and the test actually performed is not the one item 10 names.

**Why HIGH.** This is the load-bearing sentence for an Article 21 determination carried forward to every later step, and it is the build's root failure mode in its purest form: a check that proves something adjacent to the claim (Doc_01's two quotations still say what Doc_01 said they say), returned something, and was trusted. Round 3's H5 asked for the item-10 argument to be moved into §5 and made §5's own. It was moved; it was not re-derived at the scope item 10 states.

**Fix:** state the test at item 10's own scope: *"This document's own six-test assessment above draws on Doc_01 §4's two quotations, Doc_03's row-scoped sweeps, and a negative search of Cyprian's Novatianist and Felicissimus correspondence. Within that bound — and the bound is disclosed, the* Gesta *being unread — it surfaces no evidence bearing on strand-plurality that Doc_01 had not already weighed, and the trigger is not met on the evidence weighed."* Move the bolded conclusion after the bound rather than before it.

### H5 — The fix pass's new "stands either way" language contradicts Candidate 5's Dependency bullet, which is the only stated ground on which that test passes

**Sites:** line 91 (Candidate 5, Dependency — untouched); lines 105 and 173 (both new in this pass).

Candidate 5's Dependency test passes — narrowly — on exactly one stated ground:

> *"- **Dependency:** Passes narrowly. **Doc_01's own strand-singular finding is the one place in this world's construction record that genuinely depends on how this axis resolves** — §5 reaches its finding "with that qualification stated on the record, not concealed" specifically because of this axis's own non-closure. No candidate below depends on this axis resolving one way or the other."*

The fix pass then wrote, at line 105: *"**Doc_01 §5's strand-singular determination stands either way**... The non-reopening finding at §5 is therefore independent of how this classification resolves"*; and at line 173: *"the non-reopening finding below does not rest on it."*

If the strand-singular finding stands either way and is independent of how this axis's classification resolves, then the one construction finding Dependency names as depending on this axis does not depend on it in the way the bullet asserts. The bullet's fallback — that §5's *qualification* was stated because of the axis's non-closure — is a weaker claim than "genuinely depends on how this axis resolves," and it is a claim about a qualification Doc_01 has already made, not about a dependency in this document's ecology.

**Why HIGH.** The six-test profile is the object of the escalation: §3, §4, §5 and Open Item 2 all hand the project lead *"narrow passes on Repetition, Dependency, Explanatory, and Interaction; does not clearly pass Formation; does not pass Persistence"* as the settled input to a label decision. If the Dependency pass is undercut by the document's own new text, the profile handed up is not what the document believes. This is gap (d) — the change broke something adjacent — and the destination check cannot see it, because Dependency was not a destination.

**Fix:** reconcile at line 91. Either restate Dependency as passing on the narrower ground actually available (*"§5's strand-singular finding attaches an explicit qualification to this axis and to no other — this axis is the only one in this world's construction record that any finding is qualified by; no finding turns on how it resolves"*), or, if the stronger dependency is meant, withdraw "stands either way" at lines 105 and 173. Whichever is chosen, say at §3 that the profile was re-checked after the escalation language was added.

### H6 — The certification is overstated again, for the fifth consecutive round, in the pass that adopted the anti-certification remedy — and the Round 2 pass's headline is repeated uncorrected while the Round 1 pass's is corrected

**Sites:** line 3 (Status); line 225 (Document Log, the Round 3 fix-pass entry); the Decision Log's 2026-09-13 (third) entry.

The countable parts are right this time, and that should be said. The Document Log's Round 3 enumeration is HIGH `H1–H6` (6), MEDIUM `M1–M5` (5), LOW `L1, L2, L3, L4, L5, L6` (6), COSMETIC `C1, C2, C3` (3) = **20**, matching the headline and matching Round 3's own counts. Round 3's H6(a) is genuinely closed.

What is not right:

**(a) "Addressing all 20 of Round 3's findings" is not true.** Four are partial (H1, H4, H5, M4 — see the table below), and four of the partials plus three of the fixed introduced a new defect. Two of the partials (H1, H4) leave the *same proposition* Round 3 named still asserted on the page.

**(b) The Status line corrects the older overstatement and repeats the newer one.** It states, as its own finding, that the Round 1 pass *"certified 'all 38 findings addressed' while three... were untouched"* — correct and creditable. In the same line it states *"The preceding Round 2 fix pass addressed **26 of Round 2's 27 findings**"* — the Round 2 pass's own headline, which Round 3 verified and downgraded to **22 genuinely fixed, 4 partial**. The Document Log records Round 3's tally two entries later; the Status line does not carry it. A line whose own claim is *"this line states a count it has verified rather than one taken from a fix list"* is taking the most recent count from a fix list.

**(c) Three claims in the Decision Log's 2026-09-13 (third) entry over-state what is on the page.** *"H4: ...Struck."* — struck at one sentence, restated at line 175 (H2). *"H1: the escalation now reaches all four sites §3 names"* — true, and three further sites were never on the list (H1). *"Thirty destinations... all thirty carry it, and seven superseded false claims were separately asserted absent"* — verified true at string level, and the entry does not record that this proves presence and absence of strings, not of propositions, which is the whole of what went wrong.

**Why HIGH.** CLAUDE.md's governance rule is that *"a record marked 'quotes verified' is a claim to re-check, not a fact to trust."* This entry is the most detailed and most nearly accurate account of method this build has produced, which is exactly what makes three over-stated elements consequential: a reader who trusts it inherits a belief that the Tensional misstatement is gone from §5, that the escalation reaches everywhere it needs to, and that a destination check closes the class. None is true.

**Fix:** restate the Status line as *"addressing 16 of Round 3's 20 findings in full and 4 in part"* once the table below is checked, or restate it after fixing H1, H2, H4 and M4. Carry Round 3's 22/4 tally into the Status line's Round 2 sentence. In the Decision Log, narrow "Struck" to the sentence actually struck, and record the destination check's own limit in terms: **it verifies strings at listed sites; it does not verify that the proposition is retired, that the list is complete, or that the inserted text is true.**

---

## MEDIUM

### M1 — The Tensional quotation newly inserted at §5 carries emphasis CF V7.4 does not have, presented as what "CF V7.4 reads" and certified as re-extracted at source

**Sites:** line 173 (§5 — new in this pass); the Decision Log's 2026-09-13 (third) entry, H4 paragraph.

Doc_04 line 173:

> *"CF V7.4 reads "They *may* not organize as broadly as primary gravities **but they prevent the ecology from being reducible to its primary forces**" — a hedged first limb and an operative second one"*

The paragraph was re-extracted from `word/document.xml` **run by run**. The Tensional paragraph is a single run with no `<w:b/>` and no `<w:i/>`: *"Tensional Gravities function as persistent counter-forces, alternatives, or unresolved pressures within the ecology. They may not organize as broadly as primary gravities but they prevent the ecology from being reducible to its primary forces."* The wording is exact. **The emphasis is not in the source, and no "emphasis added" is stated.** The rendering with emphasis on `may` and on the second limb is Round 3's review's rendering of the same sentence, carried across — the one thing this round's commission and the pass's own Decision Log both say must not happen. The Decision Log repeats the emphasised rendering under the words *"re-extracted at source."*

Substantively the point survives without the emphasis — "may" is hedging on its own reading — so this is MEDIUM rather than HIGH. But the emphasis is doing argumentative work (it is what makes "a hedged first limb and an operative second one" visible at a glance), and it is presented inside a claim about what a governing framework *reads*.

**Fix:** either quote without emphasis, or append *"(emphasis added)"*. Same in the Decision Log.

### M2 — Candidate 1's "the flock" citation splices Doc_03's row-scope for one sub-count onto the 113 combined figure: the same defect Round 3 found at 687, one candidate away, never swept for

**Site:** line 31 (Candidate 1, *Generated from:* — untouched this pass).

> *"Doc_03's "the flock" entry (**Row 1, 2, 3, 5 — 113 combined occurrences** of flock/shepherd/pastor in Cyprian's own corpus alone, used in both bishops' own words)."*

Doc_03's row 26 was parsed cell by cell. The two figures live in two different cells and carry two different scopes:

- Evidentiary-ground cell: *"A full-text sweep of Cyprian's own vendored corpus returns 57 occurrences of 'flock,' 39 of 'shepherd,' and 17 of 'pastor'... **Of the 57 'flock' occurrences, 52 sit within rows 1, 2, 3, and 5**... the remaining 5 sit outside that set — 2 in the 256 Council's own preface (row 4), 1 in Pontius's *Life* (row 7), and 2 in the treatises attributed to Cyprian on questionable authority."*
- Tier-1 cell: *"**113 combined occurrences of flock/shepherd/pastor in Cyprian's own corpus alone**."*

"Rows 1, 2, 3, 5" is the scope of **52 of the 57 "flock" hits only**. 113 is a corpus-wide combined total across three words, and the same cell says expressly that some of it sits **outside** that row set. Doc_04 attaches the narrower scope to the broader figure. Separately, the entry's own Registry-source cell is *"Row 1, Row 2, Row 5, Row 11, Row 19"* — it does not list row 3 and does list rows 11 and 19, so the parenthetical is not the entry's source list either.

**Why MEDIUM.** This is structurally identical to Round 3's L1 (the 687 qualifier taken from the wrong Doc_03 row) — a real figure joined to a scope from a different cell — sitting one candidate away, in the same document, in the same kind of parenthesis. The fix pass fixed the instance Round 3 named and did not sweep for siblings, which is the discipline this world's own Decision Log records at the 2026-09-13 Registry entry (*"a correction made at one row without checking for siblings"*). Registry row 3 is also expressly *"general subject-matter only"* in its own Licensed-For cell, so citing it for a frequency claim reads past its licence.

**Fix:** *"Doc_03's 'the flock' entry (Rows 1, 2, 5, 11, 19 — 113 combined occurrences of flock/shepherd/pastor across Cyprian's own corpus, of which 52 of the 57 'flock' hits sit in rows 1, 2, 3 and 5 per Doc_03's own cell)."* Then re-check every other frequency parenthetical in §3 against the cell its figure sits in.

### M3 — §5 closes Doc_01 §4's "disappeared gravity" question as "genuinely lapsed" while Doc_04's own Persistence finding reports the concern present in exactly the register Doc_01 named

**Sites:** line 177 (§5, the Formation-emphasis paragraph); line 40 (Candidate 2, Persistence).

Doc_01 §4, verbatim: *"whether the underlying concern (how the community holds and reintegrates its own failed members) **persists in a different register (ordinary sin and schism-temptation) or has genuinely lapsed** is Doc_04's own question. This document's own reading, offered but not asserted as settled, favors persistence in a different register over disappearance."*

Doc_04 §5 closes it: *"whether the underlying lapsed-crisis concern "persists in a different register... or has genuinely lapsed" — **closed: it has genuinely lapsed under its own name**, surviving only as family resemblance."*

Doc_04's own Candidate 2 Persistence bullet says: *"The closest analogues — **Donatist schism-temptation, ordinary catechized sin** — are real but are tested and classified below as their own distinct gravities (Candidates 6 and 7)."* Those are the two registers Doc_01 §4 named, verbatim, and Doc_04 finds them real. Doc_04's disagreement with Doc_01 is about whether the continuation is *the same gravity under its own name* — a third option Doc_01's binary does not offer — and the closure is stated as though it selected Doc_01's second limb.

The same over-reach appears in the sentence before it: *"This corrects Doc_01 §5's own bullet — the specific concern registered there does not continue in the form the bullet's hedged reading favored."* Doc_01 §5's hedged reading favoured *"the same underlying concern in a different register (ordinary sin, schism-temptation)"*; Doc_04 finds that concern present in that register, under two new gravity names. That is a refinement of Doc_01's reading, not a correction of it.

**Why MEDIUM.** §5 presents this as one of the two deferred World Separation questions "closed... by name, as bound to close them," and Doc_01 §4 bound Doc_04 to close it. A closure that answers a differently-scoped question is not a closure, and Doc_01's own bullet is the thing it is measured against.

**Fix:** state the answer at the scope of the question: *"closed: the underlying concern does persist in the register Doc_01 named — ordinary sin and schism-temptation — but not as this gravity continuing under its own name; independent testing classifies that continuation as Candidates 6 and 7. Doc_01 §5's hedged reading is therefore refined rather than corrected."*

### M4 — §5's revisitation reading stretches Article 21's narrower clause while the governing text that actually says "governs all subsequent work" goes uncited

**Site:** line 173 (§5 — new in this pass); line 177 (§5, the Formation-emphasis paragraph).

Doc_04 rests the disposition on Article 21: *"the strand determination, "once made, governs all subsequent strand attribution" (**read here, with Doc_01 §5, as governing revisitation and not attribution alone — a reading this document inherits rather than invents**)."* The disclosure is honest and is L4's fix working.

But the stretch is unnecessary. Doc_01 §5's Finding paragraph, which Doc_04 cites as the source of the inherited reading, actually rests on **two** texts: *"Per Article 21, a strand determination, 'once made, governs all subsequent strand attribution'; **per CF V7.4's own Strand Determination entry, the determination 'is made at Step 1 and governs all subsequent work.'**"* The second quotation says without stretching exactly what Doc_04 needs. Doc_01 §8 item 10 likewise says *"the strand-singular finding stands **per Article 21 and CF V7.4**"* — two authorities, of which Doc_04 carries only the narrower one.

**Why MEDIUM.** The document discloses a stretch it does not have to make, and does so at the sentence a later reader will test hardest, while the unstretched authority is one line away in the document it says it is inheriting from. It also makes the inheritance claim weaker than it is: Doc_01 §5 is not reading Article 21 broadly, it is pairing it with a broader CF clause.

**Fix:** *"...and Constitution Article 21's own clause governs — 'once made, governs all subsequent strand attribution' — alongside CF V7.4's own Strand Determination entry, which Doc_01 §5 pairs with it: the determination 'is made at Step 1 and governs all subsequent work.' It is the second that reaches revisitation; this document applies Doc_01 §5's pairing rather than reading Article 21 past its own object."*

### M5 — CF V7.4 Part III's own provision for ambiguous test results is never engaged, anywhere, in the escalation

**Sites:** §3 lines 99–107; §7 Open Item 7; the Disposition.

CF V7.4 Part III, extracted verbatim, closes its Confidence/Gravity Cross-Check subsection with:

> *"Where gravity tests yield ambiguous results, developers should: acknowledge the ambiguity / classify provisionally / revisit classification as ecological reconstruction progresses."*

Doc_04's own §3 reports a candidate whose tests yield precisely ambiguous results (four narrow passes, one unclear, one failed at world level), and then reaches for a governance route — escalation to the project lead under CO-022 category 4 — without ever quoting or engaging the Framework provision written for that situation. The document engages the Framework's Primary, Supporting and Tensional definitions, its Cross-Check rule, its Author Gravity rule and its Interaction-Test warning, all correctly; this one it does not cite anywhere.

**Why MEDIUM.** The document's own practice — *"Provisional classification"* at every candidate, and Open Item 5's provision for revisiting Candidate 8 at Doc_05 — is the Framework provision already being followed without being named. Naming it changes what the escalation is asking for: whether the project lead is being asked to settle a label the Framework says to classify provisionally and revisit at Doc_05, or something more than that. This review takes no position on which; the Framework text belongs on the page either way.

**Fix:** quote the provision at §3's classification paragraph and at Open Item 7, and state in one sentence how the escalation relates to it — whether it supplements the "classify provisionally, revisit" route or replaces it.

---

## LOW

### L1 — Candidate 3's citation list still severs "§2" from its head
Line 56. The M4 fix removed the interpolated correction but left the full stop the correction had introduced: *"Doc_02 §1 (the 256 preface's own "proper right of judgment" — "..."; the whole rebaptism dispute...)**.** **§2** (Cyprian's Influence: ...); Doc_01 §5 (...), §3 (...)."* The `§2` item now opens a sentence with no document name. Every other candidate's list runs off commas from its head (Candidate 1: *"Doc_02 §1 (...), §2 (...), §4 (...), §5 (...)"*). **Fix:** change the full stop to a comma, or repeat "Doc_02".

### L2 — The M2 fix leaves verbless fragments at two Cross-Checks
Lines 49 and 151. *"**Per Doc_02 §8's own bracket ("Documented / Widely Accepted: ... the existence and basic content of the major primary texts named at §1").**"* and *"**Per Doc_02 §8's own bracket (as at Candidate 2).**"* The replaced text carried a subject and predicate (*"Documented for existence and basic content, per..."*); the replacement dropped both. **Fix:** *"Documented for existence and basic content per Doc_02 §8's own bracket (...)."*

### L3 — Candidates 4 and 7 still certify a flat "Documented" from a two-name band
Lines 79 and 136. Both read *"**Documented for existence and basic content, per Doc_02 §8's own bracket ("Documented / Widely Accepted: ...")**"*. The bracket is headed *"Documented / Widely Accepted"* — it licenses "Documented **or** Widely Accepted," not "Documented." Round 3's M2 raised this as a second, smaller point on the same clause and the fix pass addressed only the first. **Fix:** *"at the Documented/Widely-Accepted band per Doc_02 §8's own bracket."*

### L4 — "Supporting rather than load-bearing:" is a subjectless fragment using a classification term, at the sentence that disposes of an Article 21 determination
Line 173. *"...a reading this document inherits rather than invents). **Supporting rather than load-bearing:** Article 21's authority-structure criterion is tested here through Doc_01 §4/§5's own routing..."* "Supporting" is one of the Framework's three classification labels and one of the two Candidate 5 was tested against; using it here as an adjective meaning "subsidiary" is avoidable ambiguity in the paragraph where it will read worst. **Fix:** *"A supporting point, not a load-bearing one:"*.

### L5 — Doc_01 §8 item 7 is quoted with silently altered verbs
Line 7. Doc_04's header: *"per Doc_01 §8 item 7's own binding instruction that this document "**generate** its own candidate gravities independently from Doc_02's Source Ecology... and **state** explicitly whether this document's preliminary reading survives that independent derivation.""* Item 7 reads *"Doc_04 **generates** its own candidate gravities... and **states** explicitly whether this document's preliminary reading survives that independent derivation."* The tense shift is inside quotation marks with no brackets. Untouched by any of the four rounds. **Fix:** bracket the alterations, or quote item 7 as it stands.

### L6 — Open Item 4 attributes the purity/sufficiency-test candidate to Doc_03
Line 212. *"**The Manichaean half of Doc_03's own "refusing a purity/sufficiency test" gravity candidate** (Registry row 22's own Licensed-For phrase)."* The candidate is Doc_01 §6's, and row 22's Licensed-For cell says so in terms: *"the 'refusing a purity/sufficiency test' gravity candidate (Doc_01 §6)."* Doc_03's own grace row likewise calls it *"Doc_01 §6's own purity/sufficiency-test candidate gravity."* Doc_03 is where the term-level discovery gap is recorded, not where the candidate originates — and §2 above, correctly, treats it as Doc_01 §6's throughout. **Fix:** *"The Manichaean half of Doc_01 §6's own 'refusing a purity/sufficiency test' candidate (Registry row 22's own Licensed-For phrase; the term-level gap is Doc_03's own Notes)."*

---

## COSMETIC

### C1 — The C2 fix introduces a new sentence-case defect at the same sentence
Line 20. The replacement sentence Round 3 supplied was adopted verbatim and ends in a full stop where the old one ended in a colon; the following word was not re-cased: *"**It is not advanced — as a generation-stage finding rather than a six-test result: in the unified form Doc_01 §6 poses it, it is not one candidate.** what recurs across the two bishops is not one evidentiary base..."* **Fix:** capitalise "What", or restore a colon.

### C2 — §5 has a lowercase sentence start where the H4 fix removed the preceding clause
Line 173. *"...disclosed here so the dependency is visible rather than reconstructed). **the** conciliar-authority disagreement being real, Documented, and bounded on §3's own six-test profile is weaker..."* The clause was formerly joined by a semicolon. **Fix:** capitalise "The". While there: *"An earlier version of **this sentence** derived **that** from the Framework's Tensional definition"* now has no antecedent on the page — name what was derived.

### C3 — The escalation is stated in four different forms in four places
Line 84 (`[Tensional — escalated]`), line 101 (*"Tensional — escalated to the project lead, not settled here (CO-022 category 4)"*), line 164 (*"Tensional (provisional — classification escalated to the project lead; see §3 and §7 Open Item 7)"*), line 205 (*"escalated and pending (§3, §7 Open Item 7)"*). Each is individually fine; a reader scanning for the status meets four. **Fix:** pick one short form and one long form and use them consistently.

---

## Fix-pass verification table

| Round 3 finding | Status | Note |
|---|---|---|
| H1 — escalation declared at §3, carried to none of the four sites it names; line 107 contradicts it | **PARTIALLY FIXED / NEW DEFECT** | All four named sites now carry it, verified individually at HEAD; line 107 corrected; Decision Log corrected in place. **But the destination list came from §3 line 105 and was incomplete** — §3 line 99, §5 line 175 and §7 Open Item 3 (byte-identical, md5-confirmed) still assert the classification and the test as settled (R4 H1, H2) |
| H2 — "Carried to §7 Open Item 1" false; Open Item 1 carried only Candidate 3's divergence | **GENUINELY FIXED** | Open Item 1 rewritten to carry both divergences, with Candidate 5's named as the more consequential; Document Log's certification of the limb corrected. Clean |
| H3 — §5's non-reopening unconditional after the same pass disclosed a bounded search on that axis | **GENUINELY FIXED / NEW DEFECT** | Bound carried into §5 by name and path, "if a targeted read surfaced such material... the trigger would be met" stated, Open Item 6 pointed to, Finding qualified *"on the evidence weighed"*. All four limbs of the fix done. New defect in the same paragraph: the trigger is tested at the wrong scope (R4 H4) |
| H4 — §5 misstates the Tensional definition at the sentence carrying the non-reopening | **PARTIALLY FIXED / NEW DEFECT** | The sentence is struck and the definition re-quoted with a correct account of its two limbs. **But the proposition is restated at line 175** — *"a Tensional gravity, which by definition does not organize broadly"*, the only surviving instance in the document (R4 H2) — and the replacement quotation carries emphasis the `.docx` does not have (R4 M1) |
| H5 — §3 and §5 give incompatible accounts of what carries the non-reopening | **PARTIALLY FIXED / NEW DEFECT** | *"That distinction is what carries the non-reopening argument"* deleted (0 hits); §5 now states the item-10 argument itself. **But line 175 re-rests the non-reopening on the escalated label**, so §5 is still internally incompatible, one paragraph apart instead of one section (R4 H2); and the argument imported is narrower than item 10's (R4 H4) |
| H6 — certification wrong in three checkable ways | **GENUINELY FIXED / NEW DEFECT** | (a) L6 restored to the LOW enumeration, which now sums to ten for Round 2 and twenty for Round 3; (b) Disposition now names Round 3; (c) Decision Log's "flagged provisional" retracted in place and the "every quotation" claim narrowed with the 687 exception named. All three limbs done. The new certification is itself overstated (R4 H6) |
| M1 — Article 22 glossed as cross-strand gravity testing | **GENUINELY FIXED** | Constitution re-extracted: Article 21 *"Strand Determination Principle"* and holds the convergence clause, quoted verbatim in the new line; Article 22 *"Forces Principle"*, with what discharges it named. Exemplary |
| M2 — Confidence-B boilerplate false at Candidates 2 and 8 | **GENUINELY FIXED** | Letters parsed by field: rows 1 and 7 = A, row 2 = B; both clauses now name the row. Correct at all four Cross-Checks. Minor fragments introduced (R4 L2); the band over-read left at 4 and 7 (R4 L3) |
| M3 — "closest call" attributed to §8 item 10 | **GENUINELY FIXED** | Cell now reads *"the axis Doc_01 §4 calls 'the closest call' and §8 item 10 heads 'not yet closed'"*; both located at source, and internally consistent with lines 86 and 88 |
| M4 — the M1 fix broke Candidate 3's citation list | **PARTIALLY FIXED / NEW DEFECT** | Correction moved to a trailing parenthetical as asked. **But the claim was carried across unchecked and is false — `right of communion` occurs 0 times in `Source_Registry.md`** (R4 H3) — and the `§2` item is still severed from its head by the full stop the old interpolation left (R4 L1) |
| M5 — the Registry row list misdescribes Doc_04's citations | **GENUINELY FIXED** | Restated as what it establishes; verified against the corrected-row set (37, 44, 56, 64, 65, 206, 208) and against the document's full citation set. True as written |
| L1 — 687 qualifier imported from the wrong Doc_03 row | **GENUINELY FIXED** | Now quoted from the `heresy` cell character-for-character and attributed to *"that entry's own words"*; the `plenary Council` phrase gone (0 hits). The structurally identical defect at Candidate 1 was not swept for (R4 M2) |
| L2 — §5 points at a column name the L9 fix removed | **GENUINELY FIXED** | Now *"the Cross-Strand (or declared substitute) status column at §4, and the Persistence test at each §3 entry"* — both targets exist and carry what is claimed |
| L3 — "does not clearly touch" located in §4 | **GENUINELY FIXED** | Now *"occurs at Doc_01 §2's transition-criteria summary and §5's authority-structure bullet, not in §4"*; both occurrences independently located by section (lines 28 and 92) |
| L4 — "once made, governs" truncated past its object | **GENUINELY FIXED** | Full clause given at the operative sentence, with the revisitation reading disclosed as inherited from Doc_01 §5. Residual: the broader CF authority Doc_01 §5 pairs with it is still uncited (R4 M4) |
| L5 — "those fourteen acts" asserted flat | **GENUINELY FIXED** | Open Item 6 now reads *"a targeted read of those acts"*, with *"at least fourteen"* retained as the floor, per row 65's own instruction |
| L6 — *Gesta* cited as "row 65" without the Migne distinction | **GENUINELY FIXED** | All four sites now name the Migne PL XI printing and the vendored path; §3's Repetition bullet additionally states that row 65's Source cell is Lancel's in-copyright SC edition and *"not the text meant here"*. Verified against row 65 in full |
| C1 — sentence-case defect at Candidate 2's Dependency | **GENUINELY FIXED** | *"this gravity's own resolution"* — lowercase |
| C2 — the M7 replacement sentence ungrammatical | **GENUINELY FIXED / NEW DEFECT** | Round 3's suggested replacement adopted verbatim; the following word left lowercase after the punctuation changed (R4 C1) |
| C3 — the two Tensional headings carry different conventions | **GENUINELY FIXED** | Heading now `[Tensional — escalated]`, the short form Round 3 proposed |

**Totals, counted from the table above and checked to sum: 16 genuinely fixed · 4 partially fixed · 0 not fixed = 20.**

- **Genuinely fixed (16):** H2, H3, H6; M1, M2, M3, M5; L1, L2, L3, L4, L5, L6; C1, C2, C3.
- **Partially fixed (4):** H1, H4, H5, M4 — **all four introduced or left standing a new defect**; three of the "genuinely fixed" (H3, H6, C2) also introduced one.
- **Not fixed (0).** Nothing is byte-identical at a site the pass listed. The list, not the site, is where this round's failures live.

**Against the document's own claim of "all 20 findings addressed":** four are partial, and two of those four (H1, H4) leave the exact proposition Round 3 named still asserted on the page, at sites the pass did not list. This is the **fifth consecutive round** in which the fix pass's self-certification overstates — though the margin continues to shrink (38/38 over three untouched; 26/27 over four partials; 20/20 over four partials with nothing untouched).

---

## Escalation-category assessment (CO-022)

Run against all four categories, with near-misses checked rather than assumed away.

**1. Representative-identity decisions — does not apply.** Nothing in Doc_04 names, titles, characterizes or constrains this world's Representative. The `[CT]`-withholding tag cells were re-derived per-row and remain correct and untouched.

**2. Portfolio-level / cross-world decisions — does not apply.** The IJC precedent claims at Open Item 3 and Candidates 4, 6 and 7 were not edited this pass. The *Gesta* corpus-map assignment is applied, not made (PR #177). The Framework/Template mismatch is routed to IJC's existing System Hub item and no new one is opened. Note that Open Item 3 — the item carrying the IJC correction — is the one byte-identical site now contradicting the escalation (R4 H1); that is a within-document defect, not a portfolio one.

**3. Governance / methodology decisions — TRIPPED, at low intensity, on one limb, and the limb has moved for the second consecutive round.** Round 3 recommended the destination check as a condition of this fix pass rather than as a portfolio rule. It was adopted, applied, and **it worked for what it covers**: thirty listed destinations verified, seven superseded strings confirmed absent, nothing byte-identical at a listed site. What it cannot cover is what replaced it — a proposition still asserted at an *unlisted* site (R4 H1), a struck proposition restated in different words *inside a listed site* (R4 H2), an inserted claim that is *false at source* (R4 H3), and a trigger quoted correctly and tested at the wrong *scope* (R4 H4). None of the four is detectable by opening a listed destination and confirming a string.

The additional discipline this round's failures all needed is, again, one sentence: **derive the destination list from the claim, not from the document's own list of where the claim lives — search the whole document for every paraphrase of the proposition being retired, and re-verify every claim the fix inserts at its own source before the sentence stands.** As at Round 3, this is a build-thread verification condition, not a portfolio rule, and this review **recommends it be attached as a condition of the next fix pass rather than escalated as a new category-3 item**. It does, however, recommend that the project lead be told, alongside the live category-4 escalation, that this is now **five consecutive rounds of the same root mechanism in five different forms**, and that each adopted remedy has answered the previous form — which is a pattern about the remedy design, not about any one pass.

**4. Unresolved tensions the pipeline can't close — occupied, and not this review's to settle.** Candidate 5's classification is escalated to the project lead on the project lead's own direction of 2026-09-13. This review takes no position on whether Tensional is earned, does not reopen the question, and does not treat its own H5 or M5 as bearing on the answer — H5 is about an internal contradiction in the profile handed up, and M5 is about a governing provision that is missing from the record either way.

What this review does assess is whether the escalation is **honestly and completely recorded**. The answer is: **honestly, yes; completely, no.**

- *Honestly:* the escalation is recorded in full at §3 (lines 101–107), §4's Classification cell, §6's inclusion note, §7 Open Items 2 and 7, the Disposition and the Decision Log. Round 2's contrary escalation assessment is recorded in Round 2's own terms and not softened, at both §7 Open Item 7 and the Disposition. The Decision Log's previously false "flagged provisional" sentence is retracted in place, in terms, with an accurate account of what was wrong. The evidence most likely to settle it is named, its unreadness disclosed at three sites, and its route recorded with the vendored path. Open Item 2 now warns a downstream builder to read Open Item 7 first. This is a genuine and substantial improvement on Round 3's "half."
- *Incompletely:* three sites still present the classification as settled — §3 line 99 (*"the Framework's own Tensional definition applied, not paraphrased"*), §5 line 175 (*"a Tensional gravity, which by definition does not organize broadly"*, stated as what carries an Article 21 finding), and §7 Open Item 3 (*"Candidate 5 is classified Tensional... once the Supporting and Tensional definitions are actually run against it"*). Two of the three assert not merely the label but that **the test was run**, which is the precise proposition the escalation exists because it is not true. Open Item 3 is a carried-forward item; line 99 precedes the escalation a reader has not yet reached. And the six-test profile handed up contains a Dependency pass the same pass's new language undercuts (R4 H5).

**Result: one category tripped (category 3, governance/methodology), at low intensity, on a verification-discipline limb inside this document's own fix cycle; category 4 is already occupied by a live escalation made outside the pipeline, honestly but incompletely recorded. Categories 1 and 2 do not apply. This review proposes no new escalation, and recommends one observation be attached to the existing one.**

---

## Note on disposition — deliberately not assessed

Consistent with this folder's practice across the Doc01, Doc02, Doc03 and Doc04 Round 1–3 series, this review does not recommend a disposition. Doc_04's Status line and Disposition both state that a substantial revision returns to independent review before disposition, and the sequencing is the build thread's and the project lead's to run.

Three observations offered without recommendations attached.

**First, on the shape of what is left.** Of 20 findings, 6 are internal-consistency defects (claims this document makes about its own other sections), 5 are citation- or scope-accuracy defects, 3 concern the reasoning, 3 are cosmetic, and 3 are residuals of partial fixes. **One is a misquotation of an external governing document** — M1, the added emphasis on the CF V7.4 Tensional paragraph — which reverses the single best thing Round 3 could say about the previous pass, and reverses it in the specific way this round's commission predicted: by reproducing the reviewer's rendering rather than the source's. Only one of the twenty (H3) is a false statement about an external file's content, and it was inherited rather than invented. The document's hardest substantive judgments all continue to hold: §2's fragmentation reading, the demotion of Doc_01's third-named candidate, the refusal to let Candidate 2's cross-phase lean survive, the Framework/Template correction, the refusal to argue a contested classification a third time, and now a genuinely well-carried escalation across four of seven sites. What still does not hold is the document's account of itself.

**Second, on the mechanism — it has migrated again, and the direction is now predictable.** Five of this build's last six rounds have found the same class of error:

- **Round 1:** fabricated and misattributed quotations. *Remedy adopted:* re-derive every quotation at source.
- **Round 2:** a pointer repointed to a real target, the claim carried across unchecked. *Remedy adopted:* read the full word-level diff hunk by hunk.
- **Round 3:** a fix announced at a destination that was never opened — invisible to a diff, because an untouched site produces no hunk. *Remedy adopted:* the destination check.
- **Round 4:** **the destination list is the defect.** The check is exhaustive over the sites the document itself names, and the document's own enumeration of where a claim lives is the thing that was wrong. A per-site string check also cannot see a retired proposition restated in different words at a site it passes, an inserted claim that is present and false, or a governing test quoted correctly and run at the wrong scope.

The common root is unchanged: *a check that proves something adjacent to the claim, then trusted because it returned something.* Each remedy has been the mirror of the previous failure and has been complete against it. The pattern is that the *form* of the check keeps being derived from the *previous* failure, and the next failure is always one level of indirection out — from the quotation, to the pointer, to the site, to the list of sites. The next level out from a list is **the criterion by which the list is built**: the next remedy is not another instrument but a rule about derivation — *no list of destinations may be taken from the document being fixed; it must be rebuilt by searching for the proposition, and every inserted claim must be re-verified at its own source before the sentence stands.* On this round's evidence that step would have caught R4 H1, H2 and H3 — three of six HIGHs.

**Third, on what the destination check earned.** It should not be discarded. It closed Round 3's H2 completely, closed all three limbs of H6, and produced the first round in this document's history with nothing byte-identical and nothing left untouched at a named site. Its limit is stated wrongly in the Decision Log — as a general answer to the class — and stating that limit accurately (*it verifies strings at listed sites*) is most of what the next condition needs to say.

---

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 6 HIGH · 5 MEDIUM · 6 LOW · 3 COSMETIC, 20 in total. Fix-pass verification: 16 of Round 3's 20 findings genuinely fixed, 4 partially fixed, 0 not fixed; all 4 partials and 3 of the fixed introduced a new defect.**

**Simulated review — informational only, not an Article 31 substitute.**
