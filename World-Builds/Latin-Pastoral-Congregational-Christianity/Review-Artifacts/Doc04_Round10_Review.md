# Doc_04 — Gravity Discovery: Latin Pastoral-Congregational Christianity
## Round 10 Independent Adversarial Review — the restructure pass: did the extraction lose anything load-bearing, is the new companion file accurate, and is the document now adequate to proceed?

**Marked per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.**

**Review date:** 2026-09-14.

**Documents reviewed, at commit `9c70765b` (prior state `e6c6dd71`), branch `lpc-doc04-round2`, working tree clean:**

- `World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_04_Gravity_Discovery.md` (248 lines, 66,965 bytes)
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_04_Superseded_Claims.md` (59 lines, 7,826 bytes) — **new this pass**
- `World-Builds/Latin-Pastoral-Congregational-Christianity/lpc_Decision_Log.md` (all six 2026-09-14 entries and all four in-place `[CORRECTION]` notices)

**Read for context and used as the test standard, not reviewed:** `L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx` — decompressed and paragraph-split in full from `word/document.xml` (272 paragraphs); `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — likewise, paragraphs 300–320 read in position; `L3B-World-Build-Methodology/Doc_04_Gravity_Discovery_Template_V1.0.md` §§4, 5, 9; `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` at lines 117490–117495 and 121760–121772, and the band 118500–125499 counted directly; `Doc_01_World_Identification_Boundaries_Orientation.md` §§3, 4, 5, 8; `Source_Registry.md` row 65; `Doc04_Round1_Review.md` through `Doc04_Round9_Review.md`; the Doc_04 blob at `e6c6dd71`.

### Method

This reviewer drafted nothing under review, wrote no version of the *Gesta* read, ran no fix pass in this document's history, and did not write the restructure pass being tested. **Candidate 5's classification is the project lead's ruling and is not revisited here.** Nine rounds have now audited how this document *records* that ruling; this round audits what a cleanup did to the record.

An extraction pass has a distinctive risk profile, and the method was built around it.

1. **The full word-level diff `e6c6dd71`..`9c70765b` was read hunk by hunk**, with the prior blob extracted to disk and held open alongside HEAD. Every hunk was classified as *moved*, *rewritten*, or *deleted*, and every rewrite was compared clause by clause against the text it replaced.
2. **Every deletion was traced to a destination.** For each claim, qualification, disclosure or scope limit removed from Doc_04, the appendix and the Decision Log were searched for it by content — not by the deleted sentence's vocabulary, since a rewritten sentence does not preserve vocabulary. Where no destination existed, the deletion was tested for whether the deleted material was a *correction artifact* (legitimately extractable) or a *current claim, disclosure or scope limit* (not).
3. **Every review-round-mandated disclosure was re-derived from the round that mandated it**, not from the document's account of it: Round 2's H1 and H6, Round 2's H2, Round 3's L6, Round 4's H3 and H5, Round 8's H8. A disclosure that exists because a round required it is invisible to any check that looks for the absence of apparatus, which is what this pass optimised for.
4. **The appendix was tested as a factual document, entry by entry**, against the review round each entry names and, where the entry states what a source says, against the source. It was not read as a summary of Doc_04's history; it was read as fifteen assertions about nine rounds and four governing texts.
5. **Appendix §5 verified at source, independently.** `CiC_L3A_Forces_Framework_V1.1.docx` was decompressed and every paragraph enumerated, the target sentence located by string match, and the enclosing headings located by walking backwards through the paragraph list.
6. **The §8 table checked cell by cell against the artifacts' own headers** — every date against each review's `**Review date:**` line, every count against each review's `## VERDICT` block.
7. **Structure machine-checked:** per-row pipe counts on all three tables; `**`, `*` and backtick parity on all 248 lines of Doc_04 and all 59 of the appendix; all 28 matrix pairs for symmetry and against each candidate's own §3 Interaction bullet.
8. **Rounds 5, 6, 7, 8 and 9 re-tested at HEAD at each finding's own named site**, with *fixed* distinguished from *mooted by deletion of the text the finding was about* — which are not the same, and which an apparatus-removal pass systematically conflates.
9. **The two numbers the pass asserts were recomputed**, in both bytes and characters.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 5 HIGH · 11 MEDIUM · 12 LOW · 3 COSMETIC — 31 in total.**

**Did the extraction lose anything load-bearing? Almost nothing, and the near-misses are worth naming.** Every disclosure this review was asked to check specifically survives: Candidate 5's Formation bullet still states that its finding is *"reached against Doc_01 §4's own hedge rather than with its support"*; both the Repetition and Persistence search-bound disclosures survive with the *Gesta* named and routed to Open Item 6; §5's Finding retains Doc_01 §8 item 10's trigger quotation and its consequent word-for-word, and improves the citation; Candidate 2's Dependency bullet no longer attributes its reading to Doc_01 §5; the *"right of communion"* correction survives with its positive attribution intact, and the phrase now occurs zero times in Doc_04, so nothing is left unattributed. **One genuine loss and two weakenings are reported below** (M5, M6, M7). This is a materially better-executed extraction than the eight passes before it were at their own tasks.

**Is the appendix accurate? Substantially yes, and its §5 is right.** The claim this review was asked to test hardest — that Rounds 5–8 were each wrong about the Forces Framework attribution, and that the rule sits at paragraph 200 beneath *"Step 4 — Gravity Discovery"* in *"Section 4"* — **verifies at source, exactly as stated.** So do §§1.1, 1.2, 1.4 and 1.5, §2 in full including its band figures, and six of §4's seven entries. **§1.3 misattributes its round, the §1 heading miscounts its own contents, and §4 is not the complete set its own preamble promises.**

**What is wrong is not what the extraction removed. It is what the extraction did not reach.** The pass rewrote §3 to state the current claim and left §4's index-table cell — the derived table the Template requires precisely so a downstream reader need not read §3 — still carrying the withdrawn ambiguous-results basis, verbatim, including the sentence Round 9's H1 found false on the document's own evidence and the *"ambiguous candidates"* conversion Round 9's H2 identified as the operation that made the provision appear to fit. The same withdrawn basis is live at four places in the Decision Log, two of them inside in-place correction notices that direct the reader to it as current. **That is the ninth consecutive pass to declare a claim withdrawn and leave it standing at a site it did not open** — and the ninth to leave it at a site that states the proposition in the *previous* pass's vocabulary, which is the specific failure Round 8 predicted and Round 9 confirmed.

---

## What was checked hard and found CLEAN

These were tested with the expectation of finding a defect. Each is reported clean, and the basis is given so the check is reproducible rather than asserted.

1. **Candidate 5's Formation bullet keeps its disclosure, and keeps it accurately.** HEAD line 92: *"The finding rests on Doc_02's evidence alone, and is reached against Doc_01 §4's own hedge rather than with its support: Doc_01 §4 declines to fold the conciliar-authority axis into its account of the other two axes, and finds it 'closer to this world's own ordinary exercise of office than the other two axes are,' calling it 'the closest call' without treating it as settled."* Both quotations re-derived from Doc_01 §4 and correct. This is the disclosure Round 2's H1 required after finding the bullet had borrowed a Doc_01 §4 sentence about the *other two* axes. The rewrite is shorter, and it is the same claim with the same disclosure and the same two quotations. **Round 2's H1 discharge survives the extraction.**

2. **Both search-bound disclosures survive, on both bullets, with the route to Open Item 6 intact.** Repetition (line 90): *"**Search bound:** the Migne PL XI printing of the *Gesta Collationis Carthaginiensis* (`cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`, per Registry row 65's Verification Note) has not been validly read for this question — see §7 Open Item 6."* Persistence (line 94): *"Does not pass at the world level, on a disclosed search bound rather than an unqualified absence… The *Gesta* has not been validly read for this question; whether it bears on this test is untested, not settled."* Round 2's H6 required exactly this — the bound disclosed on both bullets and carried as an open item — and it is exactly what is there. The vendored Migne path, which was Round 3's L6, also survives. (What does not survive is L6's *second* limb; see M5.)

3. **§5's Finding retains item 10's trigger quotation and its consequent, and is better cited than before.** HEAD line 175 quotes *"weighing this axis directly, surfac[ing] evidence this document has not weighed — in which case the finding is reopened rather than defended past the evidence"* and reaches *"the trigger is not met."* Re-derived against `Doc_01_World_Identification_Boundaries_Orientation.md` line 180: *"until and unless Doc_04's own formal six-test assessment, weighing this axis directly, surfaces evidence this document has not weighed — in which case the finding is reopened rather than defended past the evidence."* Word-for-word, with `surfac[ing]` a properly bracketed alteration. The rewrite additionally corrects *"item 10"* to *"Doc_01 §8 item 10"*, and the consequent — *"it re-weighs Doc_01 §4's two quotations… and adds nothing to them"* — is intact. **This is the one rewrite in the pass that improved its target.**

4. **Candidate 2's Dependency attribution is correct at HEAD, and the false one is gone.** Line 44 reads *"models Candidate 3's logic at the individual-believer level — this document's own reading,"* with the Doc_02 evidence stream named (Doc_02 §2; Registry rows 4, 12, 13). Round 2's H2 required the attribution to Doc_01 §5 be withdrawn and the claim restated as this document's own; it is. `grep -c "Doc_01 §5" ` at that bullet returns zero.

5. **The *"right of communion"* correction survives with its positive attribution, and nothing is orphaned.** The phrase occurs **2 times** in the prior blob and **0 times** at HEAD, so Doc_04 makes no use of it that would need attributing. The positive attribution — *"It belongs to Doc_01 §4 and §5 and Doc_03's 'communion' entry"* — is preserved at appendix §4, as is the Round 4 H3 finding that the phrase occurs zero times in `Source_Registry.md`, which I re-ran: `grep -c "right of communion" Source_Registry.md` returns 0. Round 2's M1 (Doc_02 §1 reads *"proper right of judgment"*) is also preserved, and Doc_04's Candidate 3 *Generated from:* line quotes it correctly.

6. **Appendix §5 is right, and it is the appendix's strongest section.** Extracted independently: `CiC_L3A_Forces_Framework_V1.1.docx` contains 272 paragraphs. The sentence *"A gravity that cannot be connected to the forces acting on the world is a gravity whose ecology is incomplete"* appears **twice** — at paragraph 176, inside *"Section 3 — Three-Layer Documentation Requirement" → "Layer 3 — Formation Impact"* (para 172), and **verbatim again at paragraph 200**, whose immediately preceding heading is *"Step 4 — Gravity Discovery"* (para 198), itself inside *"Section 4 — Integration with the Construction Process"* (para 182). Doc_04's attribution at lines 6 and 97 to *"Forces Framework V1.1 §4 (Step 4)"* is **correct**, and para 200 is the more apposite of the two for a Doc_04 forces notation. Round 5's L8, Round 6's L5, Round 7's L5 and Round 8's L2 each asked this document to introduce an error. **Round 9's M15 — that the disagreement had never been logged — is discharged by this appendix section and by the Decision Log's sixth entry. Credit where it is due: this is the first time in ten rounds that this build has correctly refused a review finding on the record rather than silently.**

7. **§8's nine review-round rows are complete and accurate, and the chronology is fixed.** Every date re-derived from each artifact's own `**Review date:**` line and every count from its `## VERDICT` block: R1 2026-09-10 / 6·14·14·4; R2 2026-09-13 / 7·7·10·3; R3 2026-09-13 / 6·5·6·3; R4 2026-09-13 / 6·5·6·3; R5 2026-09-14 / 7·8·8·3; R6 2026-09-14 / 8·12·8·3; R7 2026-09-14 / 10·12·8·3; R8 2026-09-14 / 9·12·8·3; R9 2026-09-14 / 10·15·8·3. **All nine match the table exactly.** Round 5's date is corrected from the old log's 2026-09-13 to 2026-09-14, and the old log's chronological disorder (Round 5 filed before Round 4) is gone. **Round 9's M6 and M5 are discharged.** The table satisfies Template §9's three requirements — every review round, whether it was saved as its own file, what it found — on its face.

8. **Appendix §§1.1, 1.2, 1.4 and 1.5 check out against the rounds and against CF V7.4 at source.** §1.1 against Round 1's H4(a), which does state that *neither* the Tensional *nor* the Supporting definition was ever applied. §1.2 against Round 2's H5, with the Tensional operative limb re-derived: CF V7.4 paragraph 307 reads *"They may not organize as broadly as primary gravities but they prevent the ecology from being reducible to its primary forces"* — quoted exactly. §1.4 against Round 8's H1, including both the line-96 and line-99 renderings and the seven-word ellipsis, all three matching Round 8's text. §1.5 against Round 9's H1/H2, with the provision re-derived at CF V7.4 paragraph 312: *"Where gravity tests yield ambiguous results, developers should:"* — the appendix's emphasis on **results** is the correct reading. The Supporting definition at paragraph 306 is confirmed **two sentences**, and the Primary definition at 305 confirmed as quoted (with L5 below).

9. **Appendix §2's *Gesta* account is accurate, including figures I re-derived directly from the vendored file.** §2.2's band claim was tested against `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` lines 118500–125499: **138** `mandav` tokens and **401** `episcop-` tokens, matching the appendix exactly, and the band does carry numbered act headers rather than footnote apparatus. §2.1's `concili-`, Emeritus-at-117505, and Lateran-649 items each match Round 5's L6, H5 and H6. §2's Aurelius line was opened: 117490–117495 carries *"limitem istius mandati, quod nobis patres vel fratres nostri universalis concilii Ecclesiae catholicae, hic apud Carthaginem constituti, mandarunt"* — genuinely on-axis, as claimed. (Two figure-level slips are reported at L2 and L3.)

10. **Structure is clean throughout Doc_04.** Three tables, per-row pipe counts uniform within each: §4 all 6, §6 all 10, §8 all 5. `**`, single-`*` and backtick parity balanced on all 248 lines — zero exceptions. **All 28 matrix pairs symmetric**, with 2↔7 correctly the reciprocal pair (*Reshaped by* / *Reshapes*). Every one of the eight §3 Interaction bullets agrees with its own matrix row, Candidate 5's included. Open Item 8's premise that all three of Candidate 5's demonstrated relations are with **Primary** candidates is true as the matrix stands: 1, 3 and 6 are all classified Primary at §4.

11. **Doc_04 still discharges everything it is bound to discharge.** Doc_01 §8 item 6 (Antiochene contrast) — §5, *"Discharged"*, with the framing argument intact. Item 7 (independent derivation, state whether the preliminary reading survives) — §5's six-bullet survival list, complete and unchanged. Item 10 (weigh the axis, reopen if new evidence) — §5's Finding, per CLEAN 3. **The Article 21 substitute-discipline declaration survives intact** at §5: phase testing, named as the substitute, tied to Template §5's requirement, with the §4 status column and the Persistence tests named as where it is run. None of the four was touched by the extraction.

12. **The pass asserts no finding count, and that is right.** The Decision Log's sixth entry reads *"Disposition. None. Findings from Rounds 5 through 9 are outstanding; `Review-Artifacts/` is the record."* After eight consecutive passes whose closure self-reports were found inaccurate, this one does not make the attempt. Its two measurements are substantively right and mislabelled by unit (L10).

---

## HIGH

### H1 — §4's Candidate 5 Classification cell still carries the withdrawn ambiguous-results basis, verbatim, in the one table the Template exists to let a downstream reader use instead of §3

**Site:** line 162, untouched by this pass. **Contradicts:** lines 3, 99, 101, 186, 210, 212; `Doc_04_Superseded_Claims.md` lines 7 and 21.

The cell reads, in full:

> *"**Supporting (provisional)** — this candidate's six-test profile is **ambiguous**, and CF V7.4 Part III directs that such candidates be classified provisionally and revisited as ecological reconstruction progresses. Held on the project lead's ruling, 2026-09-14; **to be revisited at Doc_05**. See §3"*

Every clause of that is a claim the pass declares withdrawn.

**(a) *"Six-test profile is ambiguous."*** §3 line 99, rewritten this pass, now reads *"This candidate's six-test profile is **narrow**"* and then enumerates six determinate verdicts. Round 9's H1 found the ambiguity assertion *"falsified by the clause after its own colon."* The colon clause is still there, in the same cell's neighbour two columns left — *"Narrow passes on Repetition, Dependency, Explanatory and Interaction; does not clearly pass Formation; does not pass Persistence at world level"* — six determinate results, in the same table row as the word *ambiguous*.

**(b) *"CF V7.4 Part III directs that such candidates be classified provisionally."*** This is both halves of Round 9's H2 in one clause: *"ambiguous results"* rendered as *ambiguous **candidates*** (the predicate moved from results onto candidates, which Round 9 identified as the operation that makes the provision appear to fit), and *"should"* rendered as *"directs."* Verified at source: CF V7.4 paragraph 312 reads *"Where gravity tests yield ambiguous results, developers **should**:"*.

**(c) *"To be revisited at Doc_05."*** §3 issues no such instruction at HEAD. Open Item 2, rewritten this pass, dropped it and replaced it with *"note that Open Items 6 and 8 may both bear on the classification."* The instruction three downstream steps inherit now exists at one site only, and it is the site the pass did not open.

**(d) *"Supporting (provisional)"* is not in the Template's enumerated set** — Round 9's M3, unfixed, now the only surviving instance.

**Why this is the round's central finding.** The appendix asserts, at its line 7, *"Nothing here is a live claim,"* and at §1.5 that this basis is **withdrawn**. Both are false while line 162 stands. And the failure is diagnostic, not incidental: this pass enumerated its sites by *rewriting §3 and following §3's pointers*, and §4's cell is a **derived** restatement that no pointer from §3 reaches. Round 4 found that a copied enumeration is a defect surface; Round 8 found that a vocabulary-matched propagation check is blind to superseded vocabulary; Round 9 found that a by-subject sweep misses claims riding inside sentences about something else. This round adds: **a rewrite-the-source-and-point-at-it pass is blind to every derived restatement of the source.** §4 is derived from §3 by construction — it is the index table — which makes it the *first* place to check, and it is the place nine consecutive passes have had to be told about. Round 7's H1, Round 8's H1(e) and Round 9's M3 all landed on this same cell.

**Fix:** replace the cell's Classification content with `**Supporting**` and a single clause — *"on the project lead's ruling of 2026-09-14; see §3"* — matching line 101 exactly, and delete the ambiguity sentence, the *"directs"* sentence and the Doc_05 instruction. If the revisit instruction is wanted, it belongs at Open Item 2 where the downstream instruction lives, not in the index table.

---

### H2 — The same withdrawn basis is live at four places in `lpc_Decision_Log.md`, two of them inside in-place correction notices that send the reader to it as the current position

**Sites:** `lpc_Decision_Log.md` lines 678 and 696 (the `[CORRECTION]` notices on the second and third 2026-09-14 entries); line 750 (the fifth entry's heading); the fifth entry's *"What is now stated"* paragraph. **The sixth entry, created by this pass, corrects none of them.**

Line 678, inside a correction notice added to fix a different error:

> *"Candidate 5 is classified **Supporting, provisionally**, under the Framework's ambiguous-results provision; see the fifth 2026-09-14 entry below."*

Line 696, identically. And the fifth entry, which those two notices nominate as the current record, is itself unmarked and reads:

> *"Candidate 5's six-test profile is **ambiguous**… the classification is **Supporting held provisionally** on the project lead's ruling, and it is **flagged for revisit at Doc_05**."*

So a reader who follows the Decision Log's own correction apparatus is routed, by two notices whose whole purpose is to prevent exactly this, to a withdrawn basis presented as current. The fifth entry also contains, at the sentence Round 9's H1 killed, *"genuinely unresolved on this document's evidence — neither established nor refuted"* — which is the formulation Doc_04 itself has now dropped (M6), so the two records disagree in a second direction as well.

**This is Round 8's record-boundary finding, third occurrence.** Round 8's H4 and H5 found Decision Log entries asserting withdrawn claims; Round 9's H9 and M12 found the same; the pass that withdrew the basis declared `Doc_04_Gravity_Discovery.md` as its domain and left the companion record standing. The pass's own Decision Log entry says sites were enumerated *"across Doc_04 and `lpc_Decision_Log.md` together"* — that is the **fifth** entry's claim, not this one; the **sixth** entry makes no site claim at all, which is honest, and leaves the four sites.

**Fix:** append a `[CORRECTION, 2026-09-14, Round 9's H1/H2]` notice to the fifth entry recording that the ambiguous-results basis is withdrawn because the provision's antecedent is not satisfied, and repoint lines 678 and 696 to the sixth entry and to `Doc_04_Superseded_Claims.md` §1.5 rather than to the fifth.

---

### H3 — The extraction deleted the premise Open Item 8 asserts: Tensional is no longer excluded anywhere in §3, and Doc_04 now says something false about itself at the item carrying Round 9's central unaddressed finding

**Site:** line 214. **Cause:** the deleted paragraph at the prior blob's §3, *"How this classification was reached, stated in full because it was reached twice wrongly first."*

Open Item 8 at HEAD:

> *"That review holds that a determinate Framework classification for Candidate 5 is reachable from this document's own premises — **Primary excluded at §3, Tensional excluded at §3**, and all three of the candidate's demonstrated relations in §6 being with Primary candidates…"*

**Primary is excluded at §3**, at line 99, with the definition quoted. **Tensional is not excluded at §3, or anywhere else in Doc_04.** `grep -n "Tensional"` returns eight hits — lines 139, 147, 150, 152, 165, 186, 211, 214 — every one of them about **Candidate 8**, except line 214 itself. Candidate 5's §3 entry, lines 84–105, contains the word zero times.

The exclusion existed at `e6c6dd71`, in the paragraph the pass deleted: *"The Round 2 fix pass reclassified it Tensional, which Round 2's own H5 found quoted but never argued: the Tensional definition's operative limb… was never run, and the candidate's own results ran against it."* That paragraph was correction apparatus in form and it was right to move it — but it was also the document's **only** statement of why Candidate 5 is not Tensional, and the argument moved wholesale to `Doc_04_Superseded_Claims.md` §1.2, a file whose own line 7 declares that **nothing in Doc_04 relies on anything in it**.

Two consequences. First, Doc_04 asserts of itself a premise that is false of it, at the item that carries the review finding the document says it has not addressed — so a reader auditing Open Item 8 finds its second premise missing and cannot tell whether that is the finding's error or the document's. Second, the negative classification argument for the most-contested candidate in this build now lives only in a file explicitly framed as containing no live claims, which means the exclusion of Tensional is not, on the record, a claim Doc_04 makes.

**This is the extraction's one genuinely load-bearing loss, and it is a loss that generated a new false statement rather than merely dropping a true one.**

**Fix:** restore the Tensional exclusion to §3 as a current claim, stated without correction narration — one sentence is enough: *"It does not meet **Tensional** (CF V7.4 Part III: 'they prevent the ecology from being reducible to its primary forces'): nothing in this document depends on the candidate, it moves under no named external force, and all three of its demonstrated relations at §6 are reinforcing."* Then Open Item 8's premise is true, and §1.2 becomes what it should be — the record of a withdrawn *classification*, not the sole home of a live *argument*.

---

### H4 — Round 9's H6 is untouched at both sites, and §5 — the section that carries the Article 21 determination to every subsequent step — still states the profile in a third, incompatible vocabulary and still says the axis was "tested in full and found Supporting"

**Sites:** lines 186 and 188, plus line 203. All three byte-identical to `e6c6dd71` and to the two blobs before it.

**(a) Line 186**, the Doc_01 §8 item 7 survival bullet:

> *"Candidate 5 (conciliar authority… returning narrow passes on four tests and **failing Formation and world-level Persistence**; classified Supporting on the project lead's ruling, not on this document's own profile)"*

§3 and §4 both say *"does not clearly pass"* Formation. §5 says it **fails**. A test that does not *clearly* pass and a test that *fails* are different findings about the same evidence, asserted eighty lines apart in the same document — and the difference is not decorative, because *"fails Formation"* is the premise that made the Tensional route look necessary in the first place, and it is now the only Formation verdict a reader of §5 sees. Round 9's H6(a) raised it; the pass fixed neither half.

**(b) Line 188**, the section's own closing summary:

> *"one axis Doc_01 flagged for particular weight is **tested in full** and **found Supporting**"*

*"Tested in full"* contradicts line 90 (*"has not been validly read for this question"*), line 94 (*"on a disclosed search bound"*) and Open Item 6 (*"The question is open and unprejudiced"*). *"Found Supporting"* asserts that this document's testing produced the label — the precise claim line 101 and line 186's own second clause deny. Round 7's M2, Round 8's M7, Round 9's H6(b): **unfixed for four rounds, at a sentence that is the document's summary of its own Article 21 result.**

**(c) Line 203**, §6's inclusion note: *"Candidate 5's own row is included because it was **fully tested**."* Round 6's M12, Round 9's M9 — **unfixed for five rounds**, and further from true at HEAD than when raised, since §3 now carries the undischarged bound on two of the six tests with no offsetting claim anywhere.

These three sentences are what Round 9 identified as the migration: claims about Candidate 5 riding inside sentences whose apparent subject is Article 21 survival, or matrix inclusion. This pass enumerated by rewriting §3 and following §3's pointers, and no pointer from §3 reaches any of the three.

**Fix:** line 186 to *"…returning narrow passes on four tests, no clear pass on Formation, and no pass on Persistence at world level; classified Supporting on the project lead's ruling of 2026-09-14 (§3)."* Line 188 to *"…is tested against all six tests, with Repetition and Persistence resting on a disclosed and undischarged search bound, and is classified Supporting on the ruling."* Line 203 to *"tested against all six tests."*

---

### H5 — The appendix claims completeness it does not have, and §8 points at it for a record it expressly disclaims holding — so the account of what each fix pass changed now exists nowhere in the world folder

**Sites:** `Doc_04_Superseded_Claims.md` lines 3 and 5; `Doc_04_Gravity_Discovery.md` line 242.

The appendix opens, line 3: *"It holds **every** claim that document has made and withdrawn, so the document itself can state current claims only."*

**It does not.** §4 records seven citation and attribution claims. At least three withdrawn citation claims of the same class are absent:

- **Round 1's M8** — §2's quotation of Doc_01 §4 on the coercive-capacity axis *"spliced from two different findings,"* fixed at Round 2's M3. Round 8's H1 cites it by name as the precedent for the ellipsis defect the appendix does record at §1.4; recording the later instance and not the earlier one inverts the lineage.
- **Round 1's M10** — Candidate 3's Cross-Check quoting Doc_03 *"with words Doc_03 does not contain."*
- **Round 1's M11** — Candidate 8's *Generated from:* attributing to Doc_02 §6 a phrase belonging to Registry row 1.

Also absent: the Round 3 fix pass's *"twenty-four lines"* and *"seven of twenty"* figures, which Round 5 found unreproducible and inaccurate in both directions and which the old §8 carried an explicit *"not to be relied on"* warning against; and the Round 1 fix pass's *"all 38 findings addressed"* report, which Round 2 found untrue. Both were live withdrawn claims in Doc_04 until this pass deleted them.

And in the opposite direction, Doc_04 line 242 closes §8 with:

> *"**What each fix pass changed**, and every claim withdrawn, is recorded at `Doc_04_Superseded_Claims.md`."*

Against appendix line 5: *"**They are not an account of any pass's work.**"*

So the two files disagree about what one of them contains, and the disagreement is not merely formal: the old §8 held a detailed, round-by-round record of what each of the seven fix passes changed and which findings each closed, and that record is now in neither file. A reviewer of Round 11 cannot reconstruct from the world folder what the Round 2 fix pass did; only `git show` will tell them.

This matters more than a pointer error normally would, because the whole justification for the extraction is that the record is preserved elsewhere. **Where the extraction preserved, it preserved well. Where it did not, the document now asserts that it did.**

**Fix:** either soften line 3 to *"the claims this document has withdrawn that a reader of the current text might otherwise expect to find in it"* and add the three Round 1 items to §4, or add them and stand on the completeness claim. Separately, correct line 242 to say what is true — that every *claim* withdrawn is recorded there, and that the round-by-round record of each fix pass is in `Review-Artifacts/` and `lpc_Decision_Log.md`.

---

## MEDIUM

### M1 — The appendix's §1 heading miscounts its own contents, and Doc_04 repeats the miscount

`Doc_04_Superseded_Claims.md` line 11: *"## 1. Candidate 5's classification — five successive bases, **four withdrawn**."* §§1.1, 1.2, 1.3, 1.4 and 1.5 each open with *"Withdrawn:"* — **five** are withdrawn, and the sixth basis (the ruling) is recorded separately at line 23 under *"Current."* Doc_04 line 105 repeats it: *"**Four** earlier bases for this classification have been withdrawn, and `Doc_04_Superseded_Claims.md` §1 records each."* §1 records five. **Fix:** *"six successive bases, five withdrawn"* and *"Five earlier bases."*

### M2 — Appendix §1.3 attributes the two-sentences/three-clauses finding to Round 8; it is Round 7's H8

Line 17: *"Withdrawn: **Round 8** found CF V7.4's Supporting definition is two sentences, not three clauses."* Round 7's H8 is the finding, by its own heading — *"Supporting's stated basis does not hold: the third clause is a concession attached to a requirement"* — with the segmentation argument at Round 7 lines 205–227 and the definition extracted there from `word/document.xml` paragraph 305. Round 8 refers to the three-clause basis only as already withdrawn (its H3, H5). The appendix's own preamble (line 5) promises each entry records *"which review round established that."* **Fix:** Round 7 H8.

### M3 — Six of appendix §4's seven entries carry no round attribution at all, against the same preamble

Only the first names its rounds (*"Round 1 H1… Round 2 H2"*). The Letter 185 / *CTh* entry, the Registry row 4 entry (Round 4's H3), the Doc_02 §1 256-preface entry (Round 2's M1), the Primary definition entry, the Article 22 entry (Round 3's M1) and the Doc_03 687 entry (Round 3's L1) name none. In a file whose function is to be the checkable record, an entry without its round cannot be checked without re-reading nine reviews.

### M4 — The restructure pass does not log itself in §8, in the table it wrote

Every other pass since 2026-09-12 has a row: Round 1 fix pass, Round 2 fix pass, Round 3 fix pass, Reconciliation pass, Withdrawal pass, Basis-correction pass, Provisional-classification pass. The table ends at *"Round 9 review."* Doc_04 therefore carries no internal record that its correction history was extracted, that `Doc_04_Superseded_Claims.md` was created, or on what date — only the Status line's bare pointer. Round 6's H7 was this exact defect against the withdrawal pass (*"§8, the Document Log, was not touched"*), and it was treated as HIGH then. **Fix:** add `| 2026-09-14 | Restructure pass — correction history extracted | `Doc_04_Superseded_Claims.md` | — |`.

### M5 — Round 3's L6's second limb is deleted: the Repetition bullet no longer discloses that Registry row 65's Source cell is a different, in-copyright edition

Prior text: *"…recorded in Registry row 65's Verification Note — **row 65's own Source cell is Lancel's in-copyright SC edition, which is *not* the text meant here**; assigned to this world's own corpus-map entry 2026-09-13, `role: context`, `confidence: provisional`."* HEAD: *"per Registry row 65's Verification Note."* `grep -c "Lancel"` — prior blob 1, HEAD 0.

This is not correction narration. It is a **source-identity disclosure**, and it was a review-mandated one: Round 3's L6 required the vendored Migne file be cited rather than row 65 flat; Round 4's verification table recorded it *"GENUINELY FIXED — §3's Repetition bullet additionally states that row 65's Source cell is Lancel's in-copyright SC edition and 'not the text meant here'"*; Round 7's clean-list item 5 re-verified it present verbatim after the withdrawal pass's reversion. Two rounds certified this specific sentence present. A reader who now follows the pointer to row 65 lands on *"Serge Lancel (ed. and trans.), Actes de la Conférence de Carthage en 411, Sources Chrétiennes"* — a different edition, Confidence C, unread — with nothing in Doc_04 telling them that is not the file the bound is about. **It is also not in the appendix**, so this is the one place a disclosure existing because a round required it was dropped with no destination. The core of L6 survives (the Migne path is still named), which is why this is MEDIUM and not HIGH.

**Fix:** restore the clause, stated as a current fact rather than a correction: *"(the vendored Migne text, not row 65's Source cell, which is Lancel's in-copyright SC edition)."*

### M6 — The "neither established nor refuted" symmetry is lost, and the one-sided phrasing reopens the reading Round 8 killed

Prior §3: *"whether the candidate 'organize[s] significant portions of the ecology' is **genuinely unresolved on this document's evidence, neither established nor refuted**."* HEAD line 99: *"…is **not established** on this document's evidence."*

Round 8's H1 turned on the difference. Its finding was that *"the evidence for X is weaker than the evidence for Y"* is not *"not-X"* — and *"not established"* standing alone is precisely the formulation that slides back into *"not met."* The negative half was doing work: it was what prevented the Cross-Check divergence from being read as a substantive denial. §3's *"What the classification does not claim"* paragraph, which previously carried the explicit *"Nor is it a finding that the candidate does organize significant portions of the ecology — nor that it does not,"* now omits the point entirely.

**Fix:** restore *"neither established nor refuted"* at line 99. It is six words and it is the sentence Round 8's whole H1 was written to secure.

### M7 — Round 8's H8 disclosure is narrowed: the statement that Candidate 5's classification line, alone among eight, does not record this document's own verdict is deleted

Prior text: *"Every other candidate's 'Provisional classification' line above records this document's own verdict on the evidence. **This one does not:** it records the project lead's ruling… The distinction is stated because the line's form is otherwise identical to the seven that mean something different."* HEAD line 101: *"**Provisional classification: Supporting**, on the project lead's ruling of 2026-09-14."*

The inline qualifier does carry *whose* ruling, which is why this is MEDIUM rather than a full regression to Round 8's H8. But Round 9's H5 — which struck the *"in CF V7.4's own sense"* half of that paragraph — expressly affirmed the other half: *"The genuine difference at Candidate 5's line is **whose verdict it records**."* The pass deleted the sentence Round 9 endorsed along with the sentence Round 9 rejected. **Fix:** one sentence after line 101 — *"Unlike the seven lines above it, this one records a ruling rather than this document's own verdict on its own testing."*

### M8 — The appendix's line 7 is false: Doc_04 cites it four times, and the one fact Doc_04 relies on from the withdrawn reads is documented only there

Line 7: *"Nothing in `Doc_04_Gravity_Discovery.md` relies on anything in this file."* Doc_04 cites it at line 105 (*"§1 records each"*), Open Item 3 (*"see `Doc_04_Superseded_Claims.md` §1.1"*), Open Item 6 (*"Two attempts to read it were withdrawn (`Doc_04_Superseded_Claims.md` §2)"*) and line 242. And Open Item 6's *"One narrow finding survives and is relied on here: act 158…"* has its provenance, its confirmation and its scope recorded nowhere in Doc_04 — only at appendix §2. Under H3, the exclusion of Tensional is in the same position. The sentence is presumably meant as *"no live claim of Doc_04's rests on a withdrawn claim recorded here,"* which is a different and defensible statement. **Fix:** say that instead.

### M9 — The new Decision Log entry carries no escalation check, breaking the pattern of every prior entry, and Round 9's M12 is therefore unaddressed

Every 2026-09-14 entry before it closes with an **Escalation check** naming all four CO-022 categories. The sixth entry closes with *"**Disposition.** None."* and nothing else. Round 9's M12 found CO-022 category 3 recorded in one record and absent from the other; Doc_04's Disposition now states it (*"Governance/methodology: open, raised and not closed"*) and the Decision Log's newest entry does not. The divergence has reversed direction rather than closed.

### M10 — Doc_04's companion-documents block still certifies row 65's "not yet drawn on by it" and cites as its proof the open item that draws on it

Line 7, untouched: *"…row 65's own record that the *Gesta* is 'available to Doc_04, and not yet drawn on by it' is accurate: this document does not draw on it, **see §7 Open Item 6**."* Open Item 6 reads: *"One narrow finding survives and **is relied on here**: act 158 (file line 121764) is Augustine's subscription to the delegation's mandate, not a debate speech."* The certification and its own cited proof contradict each other. Round 9's M10, unfixed. **Fix:** *"…this document draws on it at one narrow point only, named at §7 Open Item 6; row 65 should be reconciled to that."*

### M11 — Registry row 65 remains unreconciled with the act-158 diagnosis, now for a fourth round, and I find the Registry has the better of it on the evidence I opened

Round 6's M9, Round 9's M11. Row 65 states: *"**Act 158 is the weakest of the set** — a genuine act in which Augustine speaks, but it **truncates at `158. Augustinus episcop`** and **carries none of the formula the others share**, so it does not support a claim about the recorded form."* Doc_04's Open Item 6 and appendix §2 both assert act 158 **is** Augustine's subscription, *mandatum suscepi et subscripsi*.

I opened the file. Line 121764 is `158.  Augustinus  episcop` — truncated, exactly as row 65 says. The *mandatum* formula is at line **121768**, four lines below, with three intervening lines naming Marcellinus the tribune. Whether those four lines belong to act 158 is the whole question, and it is the question row 65 declines to answer and Doc_04 answers in the affirmative without argument.

**This is the single fact Doc_04 retains from two reads it withdrew as overstated and unsound**, it is the fact Open Item 6 says is *"relied on here,"* and the Registry entry it is supposed to diagnose contradicts it. **Fix:** either argue the four-line attribution at Open Item 6 or open a Registry item against row 65; do not leave the two records asserting different things about the one surviving datum.

---

## LOW

### L1 — Appendix §2 reintroduces Round 9's L2, at the line number Round 9 corrected

Line 35: *"act 158 (file line **121764**) is Augustine's subscription to the delegation's mandate, ***mandatum suscepi et subscripsi***."* Verified at source: 121764 is the act header; the normalization sits at **121768**. Doc_04's own Open Item 6 was repaired this pass — it now cites 121764 for *act 158*, which is right — and the appendix re-attaches the phrase to the wrong line. A known-corrected error, reintroduced in the file written to correct the record.

### L2 — Appendix §2.1's *"~45% low"* is the withdrawn rewrite's own self-description, not Round 5's finding

Round 5's M3 says the headline count of 58 *"undercounts by roughly **forty** per cent."* The 45% figure is what the second read claimed to be fixing, per Round 6's M1. In an entry whose stated authority is Round 5, the figure should be Round 5's.

### L3 — Appendix §2.1's *"it missed two of Augustine's acts"* is at least one too many

Round 5's M4: the read itself identified act 14 as a fifteenth; Round 5 found act 230 at line 129294 as a sixteenth. One missed act is established. If two are meant, the second is not named in Round 5 and is not derivable from it.

### L4 — Appendix §5 cites paragraph 200 where Round 9 cites 199, and neither states its counting convention

I count 200 on a 1-based enumeration of all `<w:p>` elements in `word/document.xml`; Round 9's 199 is consistent with a 0-based or empty-paragraph-excluding count. Both point at the same paragraph and the appendix is not wrong — but in the one section of the record whose purpose is to settle a four-round disagreement by citation, two artifacts giving different numbers for the same sentence invites a fifth round of it. **Fix:** *"paragraph 200 on a 1-based count of all `w:p` elements (paragraph 199 as cited at `Doc04_Round9_Review.md`)."*

### L5 — Round 9's L1 is half-fixed: the citation is restored, the three-of-four quotation is not

Line 99 now reads *"CF V7.4 Part III: 'Primary Gravities organize the ecology broadly. Multiple dimensions depend on them. They shape formation pervasively'"* — citation restored. Paragraph 305 has a fourth sentence the quotation closes over without an ellipsis: *"They pass all or nearly all gravity tests with strong confidence."* The omission runs in the document's favour (the fourth sentence would strengthen the exclusion), which is why this is LOW, but a document that has been corrected three times for spliced quotations should not close one short.

### L6 — Round 9's C2 is live: Doc_01 §8 item 7 is still quoted with silently altered verbs

Doc_04 line 7 quotes item 7 as *"**generate** its own candidate gravities… and **state** explicitly whether."* Doc_01 line 180 reads *"Doc_04 **generates** its own candidate gravities… and **states** explicitly whether."* Two verbs changed inside quotation marks, unmarked.

### L7 — Round 9's L8 has been relocated to the appendix, not resolved

Appendix §1.2: *"the candidate's own results run against it: **nothing depends on it**."* Doc_04 line 91, Dependency: *"**Passes narrowly.** Doc_01's strand-singular finding is the one place in this world's construction record that **depends on this axis** at all."* The two sentences contradict each other across the file boundary, and the extraction moved one of them without noticing it was half of a pair.

### L8 — Round 9's L6 is live: *"has not been validly read"* still understates against row 65's *"not yet drawn on by it"*

Lines 90 and 94. Row 65's formulation is the stronger and the one the Registry will be read against.

### L9 — Round 9's M2 survives only at §4: *"to be revisited at Doc_05"* names no amendment mechanism, and Doc_05's own activity list contains no classification act

Fixed at §3 and Open Item 2, unfixed at line 162. Subsumed by H1(c); recorded separately because if H1's fix keeps the revisit instruction anywhere, this is still open against it.

### L10 — The two figures the pass asserts are character counts labelled as bytes

Decision Log sixth entry: *"**42%** of `Doc_04_Gravity_Discovery.md` **by byte count**"* and *"Doc_04: **93,503 → 66,394 bytes**."* Recomputed: **94,230 → 66,965 bytes**; **93,503 → 66,394 characters**. The measurement is right and the unit label is wrong, by 0.8%. Recorded rather than passed over because eight consecutive passes have had a self-reported number found wrong, and a reader checking this one with `wc -c` will get a different answer and will not know why. **This is not a ninth inaccurate self-report** — it is a mislabelled unit, and the distinction should be on the record.

### L11 — *"Apparatus 42% → under 5%"* is not reproducible from any stated method

The reduction is real and large; the figure is not checkable. A line-level sweep at HEAD for correction vocabulary (`earlier version|earlier draft|superseded|withdraw|corrected here|prior version|not to be relied on|misstat`) returns 8 lines totalling 7.5% of the file's characters. That is a different measure from whatever the pass used, and no measure is stated. **Fix:** state the sweep, or state the claim qualitatively.

### L12 — Candidate 2's Dependency bullet drops the explicit negation Round 2's H2 installed

Prior: *"**this document's own reading, not Doc_01 §5's.**"* HEAD: *"this document's own reading."* The positive attribution — which is what H2 required — survives, and the negation is correction apparatus in form. Recorded because H2's finding was specifically that the reading had been *attributed to Doc_01 §5*, and the sentence that says it is not is the one a future reviewer would look for. Not a defect; a reduction in a guard.

---

## COSMETIC

### C1 — §4's Candidate 5 Classification cell carries a three-sentence argument where the other seven carry a bolded label

Round 9's L7, live at line 162. Subsumed by H1's fix.

### C2 — The appendix's only unbalanced-emphasis line is line 33, and it is harmless

The literal `*` inside `` `mandav*` `` leaves an odd single-asterisk count on that line. Renders correctly; noted because the parity sweep flags it and a future sweep will flag it again.

### C3 — Appendix §4's third entry makes a live positive attribution in a file whose line 7 says nothing in it is a live claim

*"It belongs to Doc_01 §4 and §5 and Doc_03's 'communion' entry."* That is a current, correct attribution — and it is the *only* place it is now recorded, since the parenthetical carrying it was deleted from Doc_04's Candidate 3. Related to M8.

---

## Extraction losses — what moved, what was rewritten, and what went nowhere

This section exists because a rewritten-by-hand extraction can drop content silently, and no check for the *absence of apparatus* would see it. Every deletion in the diff was traced.

| Removed from Doc_04 | Kind | Destination | Verdict |
|---|---|---|---|
| Status line's ambiguous-results block, ellipsis narration, both withdrawn arguments | Correction apparatus | Appendix §§1.3, 1.4, 1.5 | **Correctly extracted** |
| Candidate 2 Dependency: *"not Doc_01 §5's"* + the §5 inter-episcopal-axis rebuttal | Correction apparatus | Appendix §4 entry 1 (in outline) | Extracted; guard reduced (L12) |
| Candidate 3 *Generated from:*: the Doc_02 §10 repointing | Correction apparatus | Appendix §4 entry 1 | **Correctly extracted** |
| Candidate 3 *Generated from:*: the whole *"right of communion"* parenthetical | Mixed — correction **and** a live attribution | Appendix §4 entries 3 and 4 | **Correctly extracted**; phrase now absent from Doc_04, so nothing orphaned |
| Cand. 5 Repetition: *"row 65's Source cell is Lancel's… not the text meant here"* | **Source-identity disclosure**, review-mandated (R3 L6) | **None** | **LOST — M5** |
| Cand. 5 Repetition: corpus-map `role: context`, `confidence: provisional` | Scope disclosure | Disposition retains PR #177 only | Partial loss; acceptable |
| Cand. 5 Repetition: *"at least fourteen numbered acts"* + the no-longer-characterises note | Correction apparatus | Nowhere needed | **Correctly deleted** — also fixes R9 M14 |
| Cand. 5 Formation: *"An earlier version cited Doc_01 §4 in the opposite direction"* | Correction apparatus | Not recorded | Extracted; the **disclosure itself survives** (CLEAN 1) |
| Cand. 5 Persistence: the withdrawn-reads narration and the named survival | Correction apparatus | Appendix §2; Open Item 6 keeps the survival | **Correctly extracted** |
| Cand. 5: the whole *"How this classification was reached"* paragraph | Mixed — narration **and the only Tensional exclusion** | Appendix §1.2 | **LOST as a live claim — H3** |
| Cand. 5: *"neither established nor refuted"* | Live qualification | **None** | **LOST — M6** |
| Cand. 5: *"This one does not: it records the project lead's ruling"* | Live disclosure (R8 H8) | **None** | **Weakened — M7** |
| §5 Finding: *"A prior version held the trigger was met"* | Correction apparatus | Appendix §3 | **Correctly extracted**; trigger quotation and consequent intact (CLEAN 3) |
| Open Item 3: the IJC-precedent correction | Correction apparatus | Appendix §1.1 | **Correctly extracted** |
| Open Item 6: the two-reads narration | Correction apparatus | Appendix §2 | **Correctly extracted** |
| Old §8: per-pass records of what each fix pass changed and closed | Historical record | **Nowhere** — and §8 line 242 says otherwise | **LOST — H5** |
| Old §8: the *"twenty-four lines"* / *"seven of twenty"* warnings; *"all 38 findings addressed"* | Withdrawn claims | **Nowhere** | Loss; appendix claims completeness — H5 |

**Summary.** Sixteen deletions, twelve correctly executed. **One outright loss of a review-mandated disclosure (M5). One live claim demoted to a withdrawn-claims file and then asserted from Doc_04 as if still present (H3). One live qualification and one live disclosure dropped without destination (M6, M7). One historical record dropped while the document asserts it was preserved (H5).**

**Nothing in Priority One's named list was lost.** The Formation bullet's *"against Doc_01 §4's own hedge"* disclosure, both search-bound disclosures, Candidate 2's Dependency attribution, Candidate 3's *"right of communion"* correction, and §5's item-10 trigger quotation and consequent all survive, verified against the rounds that required them and against Doc_01 at source.

---

## Audit of `Doc_04_Superseded_Claims.md`

Fifteen assertions, tested individually.

| Entry | Claim about what was withdrawn | Round attribution | Verdict |
|---|---|---|---|
| §1 heading | *"five successive bases, four withdrawn"* | — | **WRONG — five are withdrawn (M1)** |
| §1.1 | Non-Framework fourth label; false IJC second-world claim | Round 1 H4 | **ACCURATE** — R1 H4(a) does state neither Supporting nor Tensional was run |
| §1.2 | Tensional; operative limb never run; three relations reinforcing | Round 2 H5 | **ACCURATE**; limb re-verified at CF V7.4 ¶307 |
| §1.3 | Two sentences, not three clauses; concession attached to a requirement | *"Round 8"* | **MISATTRIBUTED — Round 7 H8 (M2)**; substance accurate, ¶306 confirms two sentences |
| §1.4 | Gating-clause denial; the seven-word ellipsis; the distinct-properties sentence | Round 8 H1 | **ACCURATE** — both renderings match R8 H1; ¶311 confirms the CF sentence |
| §1.5 | Ambiguous-results antecedent not satisfied; *results* → *candidates* | Round 9 H1/H2 | **ACCURATE**; ¶312 confirms *"ambiguous results… should"* |
| §1 *"Current"* | Supporting on the ruling | — | Accurate as to §3; **falsified by §4 line 162 (H1)** |
| §2.1 | `concili-` unsearched; Emeritus polarity at 117505; Lateran-649 subscriber; *mandat* ~45% low; two missed acts | Round 5 | Accurate on the first three; **~45% is the read's figure, not Round 5's (L2)**; **"two missed acts" overstates (L3)** |
| §2.2 | Band 118500–125499 not footnotes: 40 act headers, 138 `mandav*`, 401 `episcop-`; the two-column misassignment | Round 6 | **ACCURATE** — 138 and 401 re-derived from the file exactly; band does carry act headers |
| §2 survival | Act 158 is the subscription; Aurelius at 117492 on-axis | Round 6 | Aurelius line verified on-axis. **Line number wrong (L1); contradicted by Registry row 65 (M11)** |
| §3 | §5 reopening asserted and withdrawn; the *"by definition"* Tensional claim; the Article 21 mis-attribution of the caveat | — (no round given) | **ACCURATE** against R3 H4 and R3's caveat finding; Doc_01 §5's *"as its own discipline"* re-verified at source |
| §4 ×7 | Seven citation/attribution claims | 1 of 7 attributed | Each of the seven **accurate and genuinely withdrawn** — verified at HEAD: *"right of communion"* ×0, *CTh* ×0, *"shape formation pervasively"* correct, 687 qualifier correct, Article 22 gloss gone. **Set incomplete (H5); attributions missing (M3)** |
| §5 | Rounds 5–8 each wrong; rule at ¶200 under *"Step 4 — Gravity Discovery"* in *"Section 4"* | Rounds 5–8 | **VERIFIED AT SOURCE AND CORRECT.** ¶200; preceding heading ¶198 *"Step 4 — Gravity Discovery"*; enclosing ¶182 *"Section 4 — Integration with the Construction Process."* R5 L8, R6 L5, R7 L5, R8 L2 confirmed present. **Numbering convention unstated (L4)** |
| Line 3 | *"Holds every claim that document has made and withdrawn"* | — | **FALSE (H5)** |
| Line 7 | *"Nothing in Doc_04 relies on anything in this file"* | — | **FALSE (M8)** |

**Does the appendix omit a withdrawn claim still live in Doc_04 or the Decision Log?** No — the inverse. §1.5 records the ambiguous-results basis as withdrawn while that basis is live at Doc_04 line 162 and at four Decision Log sites (H1, H2). The appendix's coverage of Candidate 5's bases is complete; the *withdrawal* is not.

**Overall.** The appendix is a competent, largely accurate document, and its §5 is the best-verified thing in this build's record. Its defects are one misattributed round, one arithmetic error in its own heading, six missing attributions, two overstated framing sentences, and an incomplete §4. None of them is of the class this build has repeatedly produced — it does not invent a source, misquote a governing text, or reach a conclusion its evidence does not support. **Written by the thread that made most of the errors it describes, it describes them accurately.**

---

## Verification table — Rounds 5, 6, 7, 8 and 9 at `9c70765b`

*Fixed* means the defect is gone and the claim it was about is now stated correctly. **Mooted** means the text the finding was about was deleted, which is not the same thing and is marked separately.

| Round | Finding | Status at HEAD |
|---|---|---|
| R5 | H1 Open Item 3 states superseded classification as settled | **FIXED** |
| R5 | H2 §5 certifies trigger not met vs Finding saying met | **FIXED** |
| R5 | H3 Open Item 2 self-contradictory | **FIXED** |
| R5 | H4 Supporting on a one-clause quotation | **FIXED** — §3 now quotes both sentences |
| R5 | H5–H7, M3, M4, M6, L1–L5 (*Gesta* read defects) | **MOOTED** by the read's withdrawal; the artifact itself still carries R9's L3/L4/L5 |
| R5 | M5 two stale sites in Candidate 5's subsection | **MOOTED** — both sentences rewritten |
| R5 | M8 *"Persistence passes at world level"* | **FIXED** |
| R5 | L8 Forces attribution | **CORRECTLY DECLINED, now logged** — appendix §5 |
| R6 | H1, H2 §5 reopening | **FIXED** |
| R6 | H3–H5, M1–M8, L3, L4, L7 (rewrite defects) | **MOOTED** by withdrawal |
| R6 | H6 Disposition escalation self-assessment | **FIXED** |
| R6 | H7 §8 untouched | **FIXED for rounds; the pass again omits itself (M4)** |
| R6 | H8 Status line *"falsified both limbs"* | **FIXED** |
| R6 | M9 row 65 unreconciled with the read | **LIVE — M11** |
| R6 | M12 Repetition *"Passes"* on a contentless second locus | **LIVE** in substance at line 90 |
| R7 | H1–H7, H9, H10 | **FIXED** (six verified at Round 8; the remainder by this pass or the two before it) |
| R7 | H8 third clause | **WITHDRAWN** — appendix §1.3 |
| R7 | M2 *"tested in full and found Supporting"* | **LIVE — H4(b), fourth round** |
| R8 | H1 gating-clause denial | **WITHDRAWN** at §3; **LIVE in the Decision Log's fifth entry's framing** |
| R8 | H2 §8's targeted-read entry | **FIXED** — table row reads *"Both withdrawn"* |
| R8 | H3 Open Item 3's three-clause basis | **FIXED** |
| R8 | H4, H5 Decision Log entries | **LIVE — H2** |
| R8 | H7 Cross-Check in two incompatible forms | **FIXED** — §3 and §4 now agree |
| R8 | H8 bare *"Provisional classification: Supporting."* | **PARTIALLY FIXED** — inline qualifier present, disclosure deleted (M7) |
| R8 | H1(d) *"where attestation and organizing strength diverge"* generalises the rule | **LIVE** at line 97 |
| R8 | L2 Forces attribution | **CORRECTLY DECLINED** |
| R9 | H1 ambiguity antecedent false | **FIXED at §3; LIVE at §4 — H1** |
| R9 | H2 *results* → *candidates*; *should* → *directs* | **FIXED at §3; LIVE at §4 — H1** |
| R9 | H3 invokes the provision while declining to classify | **MOOTED** — provision no longer invoked at §3 |
| R9 | H4 determinate answer available, not run | **LIVE**, now carried at Open Item 8 — **whose second premise the pass deleted (H3)** |
| R9 | H5 *"provisional in CF V7.4's own sense"* | **FIXED** — sentence deleted (with the half R9 endorsed, M7) |
| R9 | H6 §5's three sentences | **LIVE — H4** |
| R9 | H7 escalation says the classification *"is settled"* | **FIXED** — Disposition rewritten |
| R9 | H8 §8 asserts the gating denial in the present tense | **MOOTED** — §8 replaced |
| R9 | H9 §8's false counts | **MOOTED** — and the record they belonged to is gone (H5) |
| R9 | H10 inaccurate closure self-report | **NOT REPEATED** — no count asserted |
| R9 | M1 Status line no longer names the withdrawal artifact | **LIVE**, but properly relocated to appendix §2 |
| R9 | M2 revisit-at-Doc_05 mechanism | **LIVE at §4 — L9** |
| R9 | M3 classification value outside the Template set | **LIVE — H1(d)** |
| R9 | M4, M5, M7, M13, M14 (§8 and Status-line apparatus) | **MOOTED** by the rewrite |
| R9 | M6 §8 chronology and Round 5's date | **FIXED** |
| R9 | M8 third entry's row-65 certification | **LIVE** in the Decision Log |
| R9 | M9 §6 *"fully tested"* | **LIVE — H4(c), fifth round** |
| R9 | M10 line 7 certifies *"not drawn on"* | **LIVE — M10** |
| R9 | M11 row 65 vs act 158 | **LIVE — M11** |
| R9 | M12 CO-022 cat. 3 in one record only | **LIVE, direction reversed — M9** |
| R9 | M15 four declined Forces findings never logged | **FIXED** — appendix §5 |
| R9 | L1 Primary definition | **HALF-FIXED — L5** |
| R9 | L2 file line 121764 | **FIXED in Doc_04; REINTRODUCED in the appendix — L1** |
| R9 | L3, L4, L5 (the *Gesta* artifact) | **LIVE** — artifact untouched |
| R9 | L6 *"not validly read"* | **LIVE — L8** |
| R9 | L7 §4 cell a three-sentence argument | **LIVE — C1** |
| R9 | L8 *"nothing depended on it"* | **RELOCATED to the appendix, not resolved — L7** |
| R9 | C1 lowercase sentence start | **MOOTED** |
| R9 | C2 item 7's altered verbs | **LIVE — L6** |
| R9 | C3 correction-notice spacing | **MOOTED** |

**What remains live across Rounds 5–9, stated as a list rather than a count, per Round 8's remedy:** R6 M9 and M12; R7 M2; R8 H1 (at the Decision Log), H4, H5, H1(d), H8-residue; R9 H1 and H2 (at §4), H4, H6, M1-residue, M2, M3, M8, M9, M10, M11, M12, L1-residue, L3, L4, L5, L6, L8, L7, C2. **Twenty-seven named. Of these, six are new instances or relocations created or left by this pass** (H1, H2, H3, H4, H5 and the appendix's own defects). **Substantially more was genuinely closed this pass than in any of the eight before it** — R5's H1–H4, R6's H1, H2, H6, H7, H8, R8's H2, H3, H7, R9's H5, H6-half, H7, M5, M6, M15 — and a large further set was mooted by deletion rather than fixed, which is why no aggregate is asserted here.

---

## Is Doc_04 adequate to proceed to Doc_05?

**My judgement: not yet — but the blocker is four sentences wide, it is review-shaped, and this is the first round in six where I would say that.**

**What is adequate.** The gravity discovery itself has not been in serious contention since Round 4. Candidates 1, 2, 3, 4, 6, 7 and 8 — seven of eight — have survived nine adversarial rounds with their six-test work, their Cross-Checks, their forces notations and their matrix relations intact; the matrix is symmetric across all 28 pairs and agrees with every §3 bullet; Doc_01 §8 items 6, 7 and 10 are all discharged; the Article 21 substitute discipline is declared and argued. **Every review from Round 5 onward has been about Candidate 5's classification apparatus and about the accuracy of this build's self-reports — not about whether this world's gravities have been correctly found.** Doc_05 does not need Candidate 5's label settled to do ecological reconstruction; it needs to know what the label is, what it rests on, and what is still open, and Open Items 6 and 8 carry the two real questions competently.

**What blocks it.** Doc_04 currently says two different things about the one candidate the whole build has been arguing about, and it says the wrong one in the **index table** — the derived artifact the Template requires precisely so a downstream builder need not read §3. A Doc_05 that consults §4, as it is designed to, inherits: a classification labelled *provisional* in a sense §3 has withdrawn; a Framework provision Round 9 found inapplicable, cited as *directing* the classification; and a *"revisit at Doc_05"* instruction §3 no longer issues. That is not a cosmetic split. It is a superseded basis propagating into the next document by the route the structure is built to make easy.

Alongside it: §5, the section that carries the Article 21 determination forward, asserts that the axis was *"tested in full and found Supporting"* and that Formation **fails** — three claims incompatible with §3 and with Open Item 6, unfixed for four and five rounds respectively. And Open Item 8, which carries the one substantive finding the document concedes it has not addressed, states a premise the same pass deleted.

**Is the blocker review-shaped?** **The blocker is. The pattern is not.**

The fix is mechanical: one table cell, three sentences in §5 and §6, one restored sentence in §3, one appendix heading. No new reasoning, no source work, no judgement call. A single competent pass closes it, and I would then say proceed.

But that has been true after each of the last five rounds, and each time the next pass has closed the sites it was shown and left a new set it was not. The remedies tried are: enumerate destinations in advance (R3 — the list was the defect); read the word-level diff hunk by hunk (R2 — blind to untouched sites); search the whole document for the old vocabulary (R4 — twenty-four lines, unreproducible); verify the proposition against the governing text before propagating (R7 — verified the external text, misread the internal premise); enumerate by subject across both files (R8/R9 — blind to claims riding inside sentences about something else); extract the apparatus so there is less to keep consistent (this pass — blind to derived restatements). **Six remedies, six blind spots, each one a different shape.** This is not a thread that cannot check its work; it is a thread checking its work against a document whose claims are restated in five places by design, with no mechanism that enumerates those places independently of the pass making the change.

**What would actually close it, and it is not another review round.** §4 is *derived* from §3. So is §5's survival bullet, so is §6's inclusion note, so is Open Item 2. A derivation that is performed by hand each time, by the same thread that wrote the source, will diverge — and it has diverged, in a different place, nine times. The two governance items Rounds 8 and 9 asked the project lead to open — separating the thread that reads a source from the thread that applies the reading, and the record-boundary question — both address this, and neither has been opened. **A tenth fix pass will close the five findings above. A tenth review will find a set it did not open. The question the project lead has to answer is not whether Doc_04 is right; it is whether a document with five hand-maintained restatements of one contested proposition can be made consistent by the thread that maintains them — and after nine rounds the answer on the evidence is no.**

**Recommendation.** Commission the mechanical pass, with the site list above given as findings rather than as a list to be regenerated. Then, before Round 11, have a thread that has not written any version of Doc_04 run one check and one check only: **read §4, §5 and §6 without reading §3, and write down what they say about Candidate 5.** If the three answers match §3, the document is adequate. That is a ten-minute check, it is the one this build has never run, and it tests the exact failure that nine rounds have found.

---

## CO-022 escalation assessment

**1. Representative-identity decisions — does not apply.** Nothing in this pass touches what the Representative is or says. Candidate 5's classification is the project lead's ruling, already made.

**2. Portfolio-level / cross-world decisions — does not apply.** The *Gesta* corpus-map assignment is applied, not decided, and PR #177 is verified in the record (`Doc04_Round2_Review.md` lines 18, 158, 384; commit `c19523fd`, corpus-map line 749). Appendix §1.1's account of Imperial-Juridical-Christianity's use of the fourth label is a report of a sibling world's record, not a decision for it, and it reports it in the corrected direction. The Framework/Template mismatch remains routed to IJC's existing System Hub item and is not re-logged.

**3. Governance / methodology — OPEN, and this round adds a third item.** Rounds 8 and 9 each recommended opening this, on two items, and both remain unopened: **(a)** separating the thread that reads a source from the thread that applies the reading; **(b)** the record-boundary question — a pass declaring one file as its domain while the companion record it is judged against carries the same claims. Item (b) has now recurred a third time (H2). **This round adds (c): an extraction pass is itself a defect surface, and a new one.** Moving claims out of the file where they are checked into a companion file that nothing checks creates exactly the divergence (b) describes, this time between a document and a file the same pass created — and it can *delete a live claim while leaving the document asserting that claim about itself* (H3), which none of the six earlier remedies could produce. Any discipline adopted for (b) has to cover companion files a pass creates, not only records that predate it. **Recorded here for the project lead; not decided by this reviewer.**

**4. Unresolved tensions — OPEN, two.** **(i)** The evidentiary question at §7 Open Item 6: the *Gesta* has been read twice by this build thread and both reads are withdrawn, and the question cannot be closed by this thread reading it a third time. Round 9's recommendation — commission from an independent thread, apply from a third — stands unactioned. **(ii)** New, or rather four rounds old and never escalated: **`Source_Registry.md` row 65 and Doc_04 assert incompatible things about act 158**, the single fact Doc_04 retains from the two withdrawn reads and expressly says it *"relies on."* Row 65 says act 158 *"carries none of the formula the others share, so it does not support a claim about the recorded form."* I opened the file: the act header is at 121764 and the *mandatum* formula at 121768, with three intervening lines. Round 6's M9 and Round 9's M11 both raised it; neither record has moved. **This is an unresolved tension between two approved-to-proceed records of the same build, on the one datum the contested candidate's open item depends on, and it should be logged as such rather than carried a fifth round as a MEDIUM.**

---

*End of Round 10 review. Simulated review — informational only, not an Article 31 substitute.*
