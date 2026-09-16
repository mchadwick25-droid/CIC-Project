# Doc_04 — Gravity Discovery: Latin Pastoral-Congregational Christianity
## Round 2 Independent Adversarial Review — fix-pass verification of Round 1's 38 findings, plus a fresh adversarial read

**Documents reviewed (working tree, branch `lpc-doc04-round2`, at `5da8b89c`):**
- `worlds/lpc/Doc_04_Gravity_Discovery.md` (216 lines) — read in full; both tables parsed programmatically cell-by-cell; all 28 Interaction Matrix pairs checked for symmetry against each candidate's own §3 Interaction bullet; the pre-fix draft retrieved from git (`dff7ef12`) and diffed line-by-line against the fix pass (`fde29975`) so that every "addressed" claim could be tested against what actually changed rather than against the Document Log's account of it
- `Review-Artifacts/Doc04_Round1_Review.md` (375 lines) — read in full; every one of the 38 findings (H1–H6, M1–M14, L1–L14, C1–C4) checked individually at its own named site
- `Doc_01_World_Identification_Boundaries_Orientation.md` — read in full, with §1 (Core Identity), §3 (the four named candidate gravities, in order), §4 (all three authority axes, the "what stays constant" argument, the two deferred World Separation questions, and the Conclusion), §5 (Strand Determination, all three Article 21 criteria, the Article 3 argument in full, the governing-consequence paragraph and the reopening caveat), §6 (the "what was it refusing" paragraph, the six-cell sketch, the placement note), §8 items 6, 7, 10 read verbatim against every Doc_04 sentence citing them; grepped directly for "Article 3", "readmission", "individual-believer", "permanent exclusion", "right of communion"
- `Doc_02_Source_Ecology.md` — read in full at §1, §2 (both Author Gravity assessments), §5, §6, §8; grepped directly for "Article 3" (0 hits), "plenary" (1 hit, §2), "right of communion" (0 hits), "lay-confessor" (0 hits), "coherence"
- `Doc_03_Lexicon_Candidate_List.md` — all ten cited term-rows parsed cell-by-cell from the raw table (term, definition, phase attribution, tags, Registry sources, evidentiary risk, Tier 1 flag); every frequency figure and every tag assignment Doc_04 cites re-derived from the cell it is drawn from
- `Source_Registry.md` (212 rows) — rows 1, 4, 12, 13, 22, 23, 192 parsed cell-by-cell; rows 37, 44, 64, 65, 206 read in full against the commission's staleness question
- `lpc_Decision_Log.md` — the 2026-09-12 Doc_04 fix-pass entry and the 2026-09-13 Registry-correction entry read in full
- `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` — extracted verbatim (python zipfile + regex on `word/document.xml`); Part III read in full (Core Historical Gravity Discovery, Candidate Gravity Generation, all six tests, Gravity Classification, Confidence/Gravity Cross-Check) and Step 4's own activity list read verbatim
- `L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx` — same extraction; Section 2 (both axes, all six cells) and Section 4's Step 4 entry read verbatim
- `L1-Foundation/CiC_L1_Constitution_V2_2.docx` — same extraction; Articles 21 and 22 read verbatim
- `L3B-World-Build-Methodology/Doc_04_Gravity_Discovery_Template_V1.0.md` — read in full, §§1–9
- `worlds/ijc/Doc_04_Gravity_Discovery.md` — read in full as peer precedent, including §2, Candidates 3/4/5, Open Items 3–5, and the Disposition/revision history
- `CLAUDE.md` (repo root) — read in full
- `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` and `git show c19523fd` (PR #177) — checked directly for the *Gesta Collationis Carthaginiensis* assignment; `git ls-files cic/texts/` used to confirm which shared texts are tracked at HEAD

**Review date:** 2026-09-13
**Reviewer:** independent adversarial review thread. Did not draft Doc_04, did not draft the Round 1 review, did not draft Doc_01, Doc_02, Doc_03 or the Registry, and ran no prior round in this world's build history.

**Method note.** This is a fix-pass verification plus a fresh adversarial read, run under this build's own documented failure mode: *"a search too strict for the text it was run against, then trusted because it returned something."* Every citation was re-derived at source rather than accepted, including citations Round 1 already cleared. No quotation was trusted because it appears in the document, and no finding was marked fixed because the Document Log says it was — each of the 38 was checked at its own named site against the pre-fix draft, so that "not fixed" could be distinguished from "reworded" and from "byte-identical." Three findings turn out to be byte-identical to the draft while the Document Log reports them addressed. Corpus sweeps were **not** re-run; Doc_03's already-disclosed sweep results were checked as citations only, cell-by-cell, and all are accurate as values and, this round, as scope and tag claims too.

Marking per Constitution Article 31: **Simulated review — informational only, not an Article 31 substitute.**

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 7 HIGH · 7 MEDIUM · 10 LOW · 3 COSMETIC — 27 in total.**

**Fix-pass verification tally, against Round 1's 38 findings: 28 genuinely fixed · 7 partially fixed · 3 not fixed.** Of the 7 partials, **3 additionally introduced a new defect** (H1, H4, H6) — the exact class of error this build's Decision Log has now recorded three rounds running.

**This fix pass did real work, and most of it holds.** Twenty-eight of thirty-eight findings are genuinely closed, several of them well: the [CT] tag corrections (H3) are exact against Doc_03's own cells; the IJC-precedent correction (H4c) reports what IJC's record actually says, including the half of Open Item 4 the draft omitted; the Possidius strike (H2) is disclosed rather than silently patched; the Template is named and Open Item 3 is restated as a Framework/Template mismatch (M4), with phase testing declared and argued as the Article 21 substitute discipline the Template requires. The reclassification of Candidate 5 from a non-Framework fourth label to a real Framework category is the right move, and running the Supporting definition against the candidate explicitly is the test Round 1 asked for.

**Eight things were checked hard and found clean, and should be stated before the findings:**

1. **Both tables are structurally clean.** Pipe counts are uniform (6 across all ten Classification Summary lines; 10 across all ten Interaction Matrix lines), and bold-marker nesting is balanced on every table line, checked programmatically. The fix pass did not break either table.
2. **All 28 Interaction Matrix pairs are symmetric**, machine-checked: every reinforcing/competing relation appears in both directions, the 1↔5 pair is now "Reinforcing, weakly" in both cells, and the one deliberate asymmetry (2↔7 "Reshaped by" / 7↔2 "Reshapes") is correctly directional. All eight §3 Interaction bullets were then checked against their own matrix rows cell-by-cell: **all eight agree with the matrix, with no omission and no over-claim.** §6's assertion that no candidate's row is entirely "no demonstrated relationship" is true when checked against the table itself.
3. **Every Doc_03 citation re-derived cell-by-cell is correct** — all ten frequency figures (113; 96/114; 31/20; ~150/128; ~120; 119; 31; 687; 1,798/1,665), all three Tier 1 flags, and, critically, all three corrected tag cells: "bishop of bishops" = `[AS], [TC], [PV]`, "plenary Council" = `[SC], [TC], [PV]`, "heresy" = `[SC], [TC], [DR]`, each now stated exactly as Doc_03 states it, with Doc_03's own reason for withholding [CT] correctly reported. Round 1's H3 is fully and accurately closed.
4. **The Framework extraction confirms Doc_04's two Framework claims.** CF V7.4 Part III's Gravity Classification section names **only** Primary, Supporting and Tensional — Open Item 3's claim is true. And the gravity definition is now quoted clean: *"A gravity is a force around which multiple dimensions organize. A topic recurs. A gravity organizes."* — verbatim, with the Primary clause no longer spliced in. Round 1's H5 splice is gone.
5. **The repointing target is real.** `grep -c "Article 3" Doc_02_Source_Ecology.md` still returns **0**, and Doc_01 §5 does contain a substantial, titled Article 3 coherence argument. The pointer half of Round 1's H1 is correctly fixed, and Candidate 3's Dependency quotation — *"what a bishop of this world does when he disagrees... work to preserve communion... or break communion and build a rival, parallel hierarchy"* — is verbatim Doc_01 §5.
6. **The IJC precedent is now reported accurately in all five places it is invoked** — the folding disposition (Candidate 1's evidence base, matching IJC §2's own wording), Candidate 4's narrower-pass shape against IJC's Candidate 5, Candidate 6's mechanism-persists-while-content-reverses shape against IJC's Candidate 3, Candidate 7's temporally-bounded shape against IJC's Candidate 4, and the "every tested candidate" matrix rule. Open Item 3's withdrawal of the false second-world claim quotes IJC's Open Item 4 exactly.
7. **Doc_01 §3's four named candidates map correctly, in order**, onto Doc_04's Candidates 1, 2, 4 and 3 respectively; §5's four survival bullets state that mapping correctly. Doc_01 §1's Core Identity quotation and the "preaching to the same gathered congregation week after week" quotation are both verbatim.
8. **§2's fragmentation reading still holds.** Doc_01 §6's parenthetical does assign both halves (a minister's own purity; a believer's own unaided will) to Augustine, and Cyprian's refusal in the preceding sentence is of "a single test of purity" deciding who remains within the community. Everything Candidates 6 and 7 rest on is sound.

**Where the findings are.** The HIGH findings cluster in one place and are of one kind. Six of seven concern **Candidate 5** — the classification the commission asked to be scrutinized hardest, and the premise §5's non-reopening argument runs from. Three of those six are **new**: defects the fix pass created or that its deletions exposed. Two are defects Round 1 did not catch and the fix pass therefore carried forward unchanged. The seventh is the document's own certification that all 38 findings were addressed, which is not true of three of them.

The short answer on Candidate 5: **the reclassification to Tensional is the right destination, and the route to it is not sound.** The Formation test that drives it is argued on a Doc_01 §4 sentence that is about the other two axes and that Doc_01 §4 expressly refuses to apply to this one; the Tensional definition is quoted but never run against the candidate's own results, which point the other way; the Confidence/Gravity Cross-Check divergence that used to qualify the classification was deleted in the same pass that raised it; and the sentence that now carries the non-reopening attributes to Article 21 a rule the Constitution does not contain and that Doc_01 §5 explicitly disclaims.

---

## HIGH

### H1 — Candidate 5's Formation test, the premise the whole classification and §5's non-reopening argument run from, is argued on a Doc_01 §4 sentence about the *other two* axes, which Doc_01 §4 expressly refuses to apply to this one

**Site:** line 92 (Candidate 5, Formation). Present in the draft; not caught at Round 1; carried through the fix pass byte-identical.

Doc_04 line 92:

> **Formation:** Does not clearly pass. This document finds no evidence in Doc_02 that ordinary believers, catechumens, or most clergy in either phase were formed by, or even aware of, this specific theoretical question. **Doc_01 §4 itself locates this axis at the level of "a bishop's authority relative to other bishops," explicitly distinguished there from "a bishop's ordinary exercise of authority toward the flock he is personally responsible for"** — the ground Candidate 1 occupies.

Doc_01 §4, verbatim, at the sentence both quoted fragments come from:

> *"The coercive-capacity and rival-consecration-validity axes both concern a bishop's authority **relative to other bishops and to a rival, competing hierarchy**: whether a rival's sacraments are void, and what tools exist against a rival communion claiming the same territory... **Neither axis touches** a bishop's *ordinary* exercise of authority toward the flock he is personally responsible for."*

Both quoted fragments belong to the paragraph about the **coercive-capacity and rival-consecration-validity** axes. Doc_04's first fragment is additionally truncated without ellipsis — "and to a rival, competing hierarchy" is cut, and that clause is precisely what makes the sentence about the *other* two axes rather than this one.

The very next paragraph of Doc_01 §4 says the opposite of what Doc_04 reports:

> *"**The conciliar-authority axis is different in kind, and this document does not fold it into that same account.** Both texts above concern a bishop's answerability *inside his own communion*, not his relation to a rival one... What changes on this axis is not a bishop's relation to a rival hierarchy but the *appellate structure above the individual bishop within his own communion*... **That is closer to this world's own ordinary exercise of office than the other two axes are**, but this document does not consider it settled that it lies outside this world's own recurring gravities either; it is the axis this document finds the closest call, precisely because the rival-hierarchy argument that disposes of the other two does not reach it."*

So Doc_01 §4 (a) explicitly declines to fold the conciliar-authority axis into the account Doc_04 attributes to it, and (b) finds this axis *closer* to ordinary episcopal office than the other two — the reverse of the location Doc_04 cites it for.

**Why this is the review's most consequential finding.** Formation is the only test Candidate 5 is said not to clearly pass other than Persistence, and Doc_04's own classification paragraph (line 99) makes it load-bearing by name: *"does not meet Primary... this candidate fails Formation on this document's own direct finding."* §5 then runs the non-reopening argument from that classification. The first sentence of the bullet — no evidence in Doc_02 of ordinary-believer awareness — is Doc_04's own finding and stands on its own; the second sentence borrows Doc_01's authority for it, and Doc_01 withholds exactly that authority. This is the same defect shape as Round 1's H1 and M8 (a quotation attached to the wrong axis or the wrong section), in the one place where it changes an outcome.

**Fix:** strike the second sentence or rewrite it to what Doc_01 §4 actually says — that Doc_01 §4 finds this axis *closer* to ordinary office than the other two, and calls it the closest call for that reason. Then re-argue Formation on Doc_04's own Doc_02 evidence alone, which is what it is entitled to argue on, and state plainly that the finding is reached against Doc_01 §4's own hedge rather than with its support. The verdict may well survive; it has to survive on this document's evidence rather than on a borrowed sentence about two other axes.

### H2 — Round 1's H1 fix repointed the citation and carried the claim over unchecked: Doc_01 §5's Article 3 argument does not say what Candidate 2's Dependency test says it says

**Site:** line 44 (Candidate 2, Dependency).

Round 1's H1 found Candidates 2 and 3 generated from, and Candidate 3's Dependency argued on, "Doc_02 §10's own Article 3 coherence argument," which does not exist. The fix pass changed the pointer from `Doc_02 §10` to `Doc_01 §5`. Doc_01 §5 does contain an Article 3 argument — that half is correct. But the claim attached to the pointer was carried across word-for-word without being checked against the new target.

Draft, line 44: *"**Doc_02 §10's own Article 3 coherence argument** reads this gravity's own resolution (readmission, not permanent exclusion) as modeling Candidate 3's own logic at the individual-believer level."*

Current, line 44: *"**Doc_01 §5's own Article 3 coherence argument** (the passage this document's own §3 Cross-Check also draws on) **reads this gravity's own resolution (readmission, not permanent exclusion) as modeling Candidate 3's own logic at the individual-believer level** — this candidate's own Doc_02 evidence stream for the same point is direct..."

Doc_01 §5's Article 3 argument does not do this. Read in full, it argues: that coherence rests on Augustine's church documenting itself as the same catholic communion Cyprian led; that *On Baptism* disputes Cyprian's ruling while claiming his communion; that the Donatists also claimed Cyprian; and that the distinguishing axis is **inter-episcopal** — *"what a bishop of this world does when he disagrees, sharply, with a fellow bishop or with the wider church's own discipline."* It then tests that axis against Letter 185. **At no point does it treat the lapsed, readmission, or the individual believer as modeling that logic.** Direct greps confirm it: `"individual-believer"` — 0 hits anywhere in Doc_01; `"permanent exclusion"` — 0 hits; `"believer level"` — 0 hits; `"readmission"` — 1 hit, in Doc_01 §4's new-gravity bullet, not in §5's Article 3 argument.

The same unsupported claim propagates to the Interaction Matrix, cell 2↔3: *"Reinforcing (2's own resolution models 3's own logic at the believer level)."* And cell 2↔6 sources a different claim to Doc_01 §5 — *"both are boundary/reintegration questions Cyprian reasons about consistently — Doc_01 §5"* — which §5 also does not state.

**Why HIGH:** this is the named mechanism, reproduced. The Document Log's own verification for this finding was `grep -c "Article 3" Doc_02_Source_Ecology.md` returning 0 — a check that the old phantom is gone, not a check that the new target says what is claimed. A phantom citation replaced by a phantom claim at a real citation is strictly worse than the original, because the pointer now survives inspection. Candidate 2 is classified **Primary** and Dependency is one of its six tests.

**Fix:** delete the Doc_01 §5 clause from line 44 and rest Candidate 2's Dependency on the evidence the same sentence already supplies and that Round 1 named as available — Doc_02 §2's Cyprian *Influence* entry and Registry rows 4, 12 and 13 — which genuinely support it. Restate the matrix 2↔3 and 2↔6 cell glosses as this document's own reasoning rather than Doc_01 §5's.

### H3 — The Confidence/Gravity Cross-Check divergence for Candidate 5 was deleted in the same pass that raised its classification, leaving the document's most contested candidate the only one with no cross-check *result*

**Sites:** line 96 (Candidate 5, Cross-Check); line 158 (summary table, Cross-Check column); line 201 (§7 Open Item 1).

The draft's Candidate 5 Cross-Check ran two sentences past the confidence rating:

> *"...The claim that this constitutes a world-organizing **gravity**, rather than a real but narrow, twice-instantiated theoretical disagreement, does not reach comparable support — precisely the Cross-Check's own governing concern, that a candidate's textual attestation and its organizing breadth are distinct properties. **Flagged rather than resolved:** the formulas are Documented; their status as a gravity is not supported at the same level, and this document does not upgrade the classification to match the vividness of the two quoted formulas."*

The draft's summary-table cell read: *"Textual existence Documented; **organizing breadth not comparably supported, flagged not upgraded**."*

Both were deleted. Current line 96 reads in its entirety: *"Evidence for the *existence* of both formulas, in their own words, reaches Documented (both directly quoted and re-verified across Doc_01's nine rounds)."* Current line 158's column reads: *"Both formulas' existence Documented."*

Two consequences. First, **Candidate 5 is now the only one of eight candidates whose Cross-Check states no result** — every other candidate closes with "No divergence" or, for Candidate 3, an explicit divergence flagged and carried to Open Item 1. Template §4 names this column "Confidence/Gravity Cross-Check result"; Candidate 5's cell now reports a confidence *rating* instead, which is the one thing the Cross-Check exists to check *against* something. Second, CF V7.4's Cross-Check rule is explicit that where attestation and organizing strength diverge, *"the discrepancy between apparent organizing strength and evidential support [is] noted explicitly rather than resolved by upgrading the classification."* The draft noted it. The fix pass removed the note in the same commit that moved the classification up from "did not reach gravity status" to Tensional, and Open Item 1 still carries forward only Candidate 3's divergence. Nothing in Round 1 asked for this deletion.

**Why HIGH:** the discrepancy the deleted sentences named is real and unchanged by the reclassification — two vividly quoted formulas at Documented confidence, against an organizing breadth the document's own six-test profile says is narrow at best. That is exactly the tension the Cross-Check exists to keep visible, and it is now invisible.

**Fix:** restore the divergence note at line 96 and in the summary-table cell, rewritten for the Tensional classification rather than the withdrawn one — the formulas are Documented; their organizing breadth is not supported at the same level; the classification is set by the six-test profile and not upgraded to match the quotations' vividness. Add it to §7 Open Item 1 alongside Candidate 3's, or as its own item.

### H4 — §5's H6 fix rests on "Article 21's reopening trigger," a rule Article 21 does not contain and that Doc_01 §5 expressly disclaims as its own self-imposed discipline, scoped to a different axis

**Site:** line 169 (§5, the Formation-emphasis paragraph — new in this fix pass).

Doc_04 line 169: *"...but it does not disturb the strand-singular finding itself: **Article 21's reopening trigger is evidence-scoped** ('surfaces evidence this document has not weighed'), and a phase-bound gravity giving way to two new phase-bound gravities is the ordinary shape of a two-phase world under strand-singular status, not new evidence of strand-plurality."*

Constitution Article 21, extracted verbatim, in full, has four sentences: strand is a finding, never a presupposed universal schema; whether a world contains strands is a construction finding that *"once made, governs all subsequent strand attribution"*; strand is defined as a meaningfully distinct pattern of formation emphasis, practice, authority structure or ecological orientation; and strand determination is accountable to evidence and never assigned to satisfy a preference for plurality. **There is no reopening trigger in Article 21, evidence-scoped or otherwise.** If anything the Article runs the other way — "once made, governs."

The reopening caveat is Doc_01 §5's, and Doc_01 §5 says so in terms:

> *"This document nonetheless attaches, **as its own discipline rather than as a rule either governing text states**, a reopening caveat **on the one axis §4 discloses as not fully closed**: if Doc_04's own independent testing surfaces evidence on the conciliar-authority axis this document has not weighed, the strand-singular finding is reopened..."*

Two defects, not one. The caveat is (a) not Article 21's, by the governing document's own explicit disclaimer, and (b) **scoped to the conciliar-authority axis specifically** — while Doc_04 invokes it to dispose of a finding about the *Formation-emphasis* leg, a different criterion entirely. Round 1's H6 fix note anticipated both halves, describing the caveat as *"evidence-scoped and conciliar-authority-scoped by its own terms."* The fix pass kept the first half and dropped the second, and promoted a self-imposed discipline to a Constitution rule in the process.

**Why HIGH:** this is the single sentence that keeps Doc_04's correction of Doc_01 §5's Formation-emphasis bullet from disturbing the strand-singular determination. It is the load-bearing clause of the H6 fix, and it misattributes its own governing authority. Doc_04's escalation self-assessment at line 216 then leans on the same reasoning to conclude no category trips.

**Fix:** attribute the caveat to Doc_01 §5, where it belongs, as that document's own attached discipline rather than an Article 21 rule. Then argue the scope point openly: the caveat as written does not reach the Formation-emphasis leg at all, so what actually disposes of it is Article 21's own "once made, governs" plus the substantive argument Doc_04 already gives (a phase-bound gravity giving way to two phase-bound gravities is not evidence of strand-plurality). That argument is available and good; it just has to stand on its own name.

### H5 — Tensional is quoted at Candidate 5 but never argued against it, and the candidate's own results point the other way: every demonstrated interaction it has is *reinforcing*, and nothing depends on it

**Sites:** line 99 (classification), line 100 (Provisional classification), line 158 (summary table), lines 91, 95, 97 (Dependency, Interaction, forces).

Round 1's H4(a) asked for the Tensional definition to be run against Candidate 5. The fix pass quotes it — accurately — and then treats the quotation as the argument:

> *"What the evidence does show... is 'a live, unresolved theoretical residue of the century-gap itself' and 'real, substantial, and directly quoted evidence of a live theological difference between this world's own two anchor figures' — **which is the Framework's own Tensional definition applied, not paraphrased**: 'persistent counter-forces, alternatives, or unresolved pressures within the ecology... [that] prevent the ecology from being reducible to its primary forces.'"*

The definition has two limbs. Doc_04 argues the first (an unresolved pressure) by restating its own descriptions of the candidate. It never argues the second — *"prevent the ecology from being reducible to its primary forces"* — and Candidate 5's own test results contradict it:

- **Dependency, line 91:** *"**No candidate below depends on this axis resolving one way or the other.**"*
- **Interaction, line 95:** *"Interacts demonstrably with Candidates 1 (weakly...), 3, and 6."* Matrix row 5, machine-parsed: `1 = Reinforcing, weakly`; `3 = Reinforcing`; `6 = Reinforcing`; all five other cells `no demonstrated relationship`. **Candidate 5 has no competing and no reshaping relation with any candidate in the document.**
- **Forces, line 97:** *"Does not hold, shift, intensify, or fracture under a named external force the way Candidates 2, 3, and 6 do."*

A candidate whose every demonstrated relationship is reinforcing, on which nothing depends, and which does not move under any named force, is not on its face a *counter*-force preventing the ecology from reducing to its primary forces. Doc_04's own analogy makes the gap visible rather than closing it: it says Candidate 5 *"has a structurally comparable bounded profile to Candidate 8 (Tensional, below, on a similarly narrow evidentiary base), and the same reframing test applies."* Candidate 8's profile is not structurally comparable in the relevant respect — Candidate 8 **competes** with Candidate 2 (matrix cells 8↔2 and 2↔8, argued in both §3 bullets), which is precisely what makes it a counter-force. Candidate 5 has no such relation. The two candidates are alike in narrowness and unlike in exactly the property Tensional names.

**Why HIGH:** Round 1's H4 said the classification "is not earned." The fix pass changed the destination and reproduced the defect: the label is now a Framework label, and it is still reached by assertion rather than by the test. This is also the claim §7 Open Item 2 carries forward to Doc_05/Doc_07/Doc_08, where the counter-force characterization will be relied on.

**Fix:** either argue the second limb — identify what, specifically, Candidate 5 is a counter-force *to*, and if that is real, say so in the matrix as a competing or reshaping relation rather than three reinforcing ones — or state honestly that Candidate 5 reaches Tensional on the "unresolved pressure" limb while not exhibiting the counter-force shape Candidate 8 does, and record that asymmetry rather than asserting the two profiles are comparable. Drop or qualify the Candidate 8 analogy either way.

### H6 — The 411 Conference *Gesta* is now in this world's own corpus-map and the Registry records it as "available to Doc_04, and not yet drawn on by it," while Candidate 5's Repetition and Persistence verdicts rest on absence claims about exactly that kind of evidence

**Sites:** lines 90 and 94 (Candidate 5, Repetition and Persistence); line 26 (Candidate 1, the "post-411 Conference" citation); header line 7.

Checked directly rather than taken from the commission: PR #177 (`c19523fd`, merged 2026-09-13) added the *Gesta Collationis Carthaginiensis* to `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` (entry at line 749, `source_file: pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`). The file is present and tracked at HEAD. `Source_Registry.md` row 65, as corrected on 2026-09-13, records that Augustine speaks in his own recorded voice in **fourteen numbered acts** of the 411 conference (50, 53, 98, 158, 160, 162, 187, 189, 201, 206, 257, 265, 267, 272 — stated as a floor), and closes: *"**available to Doc_04, and not yet drawn on by it.**"*

Doc_04's Candidate 5 makes two absence claims that this route bears on directly:

- **Repetition, line 90:** *"Augustine's own hierarchical formula recurs internally within one treatise (Row 13...) but **is not independently restated in a second Augustine-authored work this document has drawn on**."*
- **Persistence, line 94:** *"Does not pass at the world level. **No evidence** that either bishop's own theory was independently visible outside the one locus each is drawn from, **or that it was operative or contested among ordinary clergy** — only between two specific bishops at two specific moments."*

The 411 Conference is a formally convened assembly of 279 Donatist and 286 Catholic bishops at which Augustine speaks on the record — the single most obvious place in this world's corpus where inter-episcopal authority structure would be visible in operation among clergy who are not the two anchor figures. Whether it in fact contains conciliar-authority material is not something this review can settle and not something Doc_04 has to settle; what Doc_04 does have to do is disclose the bound of its own search before resting a classification on an absence. It does not. The Persistence bullet's "No evidence" is unqualified, and the Repetition bullet's qualifier — "this document has drawn on" — silently converts a claim about the corpus into a claim about the document's own reading list, in the one candidate where that distinction decides the outcome.

**Why HIGH:** both tests this bears on are Candidate 5's, and both feed the classification H5 already finds under-argued. This is also a straightforward cross-document consistency failure against a companion document Doc_04 names in its own header: the Registry, on the same branch, says the route is available to Doc_04 and unused; Doc_04 says there is no evidence.

**Fix:** disclose the search bound explicitly in both bullets — state that the *Gesta* (Registry row 65; corpus-map entry added 2026-09-13, `role: context`, `confidence: provisional`) has not been read for this question, and that the Persistence and Repetition findings are therefore bounded by that. If the fix pass can afford a targeted read of the fourteen acts, it should run one; if not, carry the question as its own Open Item alongside item 5. Either is honest; the current unqualified "No evidence" is not.

### H7 — The document certifies that all 38 findings were addressed; three were not, and two of those three are byte-identical to the draft

**Sites:** line 3 (Status), line 210 (Document Log), line 214 (Disposition).

Line 3: *"**Status:** REVISED — Round 1 fix pass applied, **addressing all 38 findings**."* Line 210: *"Round 1 fix pass. **All 38 findings addressed**... **M8**/M10/M11 (misattributed and fabricated quotations corrected or restated as this document's own characterization)... **L1–L14** and C1–C4 applied throughout."*

Checked by diffing the draft (`dff7ef12`) against the fix pass (`fde29975`) at each named site:

- **M8 — not fixed, byte-identical.** Line 18's coercive-capacity quotation is character-for-character the draft's: *"Doc_01 §4 already tested this shift as a World Separation criterion and found 'the coercive-capacity... axis does not clearly touch this world's own recurring gravities as established'."* Doc_01 §4's Conclusion is flat on that axis — *"**neither touches** this world's own recurring gravities as established at §3"* — and the hedged "does not clearly touch" belongs to the conciliar-authority axis alone. The Document Log names M8 as corrected. It is not.
- **L9 — not fixed, byte-identical.** Line 131 still claims Doc_01 §6's *"What was it responding to"* prose as the **Ongoing/External cell** content. The cell itself reads *"Manichaeism and Pelagianism as live rival systems Augustine's own pastoral work directly answers."*
- **L5 — not fixed.** No Cross-Check gained a Confidence-B qualifier or a citation of Doc_02 §8's bracket. `grep -c "Confidence B|Doc_02 §8"` across the whole document returns **1**, and that one hit is Candidate 7's *Generated from:* line, which carried it in the draft already.

**Why HIGH:** CLAUDE.md's governance section states that *"a blocking review finding can't be dismissed by self-certification"* and that *"a record marked 'quotes verified' is a claim to re-check, not a fact to trust."* A Status line reading "addressing all 38 findings," taken at face value by a disposition decision, would carry three unfixed findings — one of them a misquotation of a named section of a cleared companion document — past the gate. The defect is the certification, not the three findings' individual severity.

**Fix:** fix M8, L5 and L9, or amend the Status line and Document Log to state what was and was not addressed, with reasons. Given this build's own history, the more useful discipline is the one the 2026-09-13 Registry entry already models: read the full word-level diff hunk by hunk against each finding's site, rather than searching for the phrase the fix was supposed to introduce.

---

## MEDIUM

### M1 — Candidate 3's *Generated from:* attributes "right of communion" to Doc_02 §1, which does not contain the phrase; Doc_02 §1's 256-preface quotation is "right of *judgment*"

**Site:** line 56.

Doc_04: *"Doc_02 §1 (the 256 preface's own **'right of communion'**; the whole rebaptism dispute, where disagreement does not sever fellowship)."*

`grep -n "right of communion" Doc_02_Source_Ecology.md` returns **0**. Doc_02 §1's actual 256-preface quotation is: *"neither does any of us set himself up as a bishop of bishops... every bishop, according to the allowance of his liberty and power, has his own **proper right of judgment**."* The "right of communion" clause is Doc_01 §4's and §5's (*"judging no man, nor rejecting any one from the right of communion, if he should think differently from us"*) and Doc_03's "communion" entry's.

This is Round 1's M9 in a new location, in the same candidate Round 1's H1 concerned, and it bears on the same independence obligation: Doc_01 §8 item 7 requires candidates generated from Doc_02's own evidence streams, and the phrase Candidate 3's Doc_02 grounding turns on is not in Doc_02. The rest of the line (the rebaptism dispute; the Doc_02 §2 *Influence* quotation) is correctly sourced.

**Fix:** either quote Doc_02 §1's own preface fragment ("proper right of judgment"), or attribute the "right of communion" clause to Doc_01 §4/§5 and Registry row 4, alongside the Doc_02 §1 pointer for the rebaptism dispute.

### M2 — §5 claims the discussion below addresses "ecological orientation"; it never does

**Site:** line 167.

Doc_04: *"...reached there on **other** grounds, formation emphasis and practice, **and ecological orientation**, **which the discussion below addresses rather than leaves untouched**."*

`grep -ci "ecological orientation"` across the whole document returns **1** — this sentence. Doc_01 §5's Article 21 determination is tested against three criteria, and Doc_04 §5 assesses two: authority structure (Candidate 5) and formation emphasis (Candidate 2, the new paragraph at line 169). The third is named as addressed and is not.

Round 1's H6 was precisely about §5 "affirmatively describing the untested leg as untouched" while running the assessment against one finding only. The fix closed one leg and added a completeness claim covering both.

**Fix:** either add a sentence assessing whether anything in §3 disturbs Doc_01 §5's ecological-orientation bullet (on this document's own evidence, nothing does — Candidates 1, 2, 3 and 6 all support it, which is a two-sentence discharge), or narrow the claim to formation emphasis and say ecological orientation is untouched and why that is the right result.

### M3 — Round 1's M8 is carried forward unfixed: the coercive-capacity quotation is still spliced from two different Doc_01 §4 findings

**Site:** line 18. See H7 for the certification problem; the underlying finding stands at Round 1's own severity.

Doc_04 attaches the coercive-capacity axis's name to the conciliar-authority axis's weaker verdict, blends Doc_01 §4's Conclusion wording with §5's, and presents the result inside quotation marks as a single §4 finding. Doc_01 §4's Conclusion is flat on that axis: *"neither touches this world's own recurring gravities as established at §3."*

**Fix:** quote Doc_01 §4's Conclusion accurately. Note that this misquotation and H1's run in opposite directions from the same paragraph — this one makes Doc_01 weaker than it is, H1's makes it stronger — which is itself a signal that the paragraph is being cited from memory rather than re-read.

### M4 — Candidate 7's Classification Summary verdict hides a second narrow pass, reproducing in an unchecked row the exact defect the fix pass reconciled in rows 4 and 5

**Sites:** line 122 (§3 Interaction); line 160 (summary table).

§3, line 122: *"**Interaction:** Passes **narrowly** — see §6."*
Summary table, line 160: *"**Repetition/Formation/Explanatory/Interaction pass** within Augustine's phase; Persistence fails at world level; **Dependency narrow**."*

The table names exactly one narrow pass. §3 records two — Dependency **and** Interaction. This is Round 1's M6 shape (§3's honest narrow texture flattened in the summary row), in the one candidate row Round 1 did not check, surviving a fix pass whose whole M6/M7 limb was reconciling summary rows against §3 verdicts. Template §4's stated purpose for this table is to let a downstream builder confirm what each candidate received *without reading the full document*, which is exactly what this row defeats.

**Fix:** restate line 160 as "Repetition/Formation/Explanatory pass within Augustine's phase; Persistence fails at world level; narrow pass on Dependency and Interaction." Then re-check rows 1, 2, 3, 6 and 8 the same way, which this review confirms are currently faithful.

### M5 — §5 declares Doc_01 §4's new-gravity question "closed" while §7 Open Item 4 concedes half of the material it was asked about was never tested

**Sites:** line 169 (§5); line 204 (Open Item 4).

Doc_01 §4's new-gravity bullet names its subject matter explicitly: *"The **anti-Manichaean and anti-Pelagian** material that occupies much of Augustine's own later output is new *subject matter*; whether it represents a genuinely new gravity or the same recurring concern in new clothing... is Doc_04's own question."*

Doc_04 §5: *"whether a genuinely new gravity emerged in Augustine's own phase — **closed: yes, Candidate 7** (Grace and Human Incapacity), independently generated and tested."*

Candidate 7 is the anti-Pelagian half (Registry row 23). Doc_04's own Open Item 4 says of the other half: *"**was not independently tested here as its own candidate**, since Doc_03's own discovery pass had not yet surfaced a specific enough term to test against."*

Closing a two-part question on one part, while the document's own Open Items record the other part as untested, overstates the discharge. The honest form is available and is not weaker: the question is answered *yes* on the evidence tested, with the Manichaean half carried forward as a possible second front or a ninth candidate, which Open Item 4 already says.

**Fix:** scope the closure at line 169 to the Pelagian half and point to Open Item 4 for the rest.

### M6 — Doc_04's header states `Source_Registry.md` is "Approved to proceed"; the Registry returned to independent review on 2026-09-13

**Site:** line 7 (Companion documents).

`lpc_Decision_Log.md`, 2026-09-13 entry, Disposition: *"These are corrections to `Source_Registry.md`, which reached **Approved to proceed** on 2026-09-12 on Round 30's clearing verdict. Because they change text-location claims and narrow one Confidence justification, they are substantial under CO-022 and **the Registry returns to independent review**; this entry does not self-dispose them."*

Eight stale claims across seven rows were corrected, one Confidence-B justification was narrowed, and row 65 — which Doc_04's Candidate 5 material bears on directly (see H6) — changed substantively. Doc_04's header carries the pre-correction status.

**Fix:** update the companion-documents line to record the Registry's current status, and check whether anything Doc_04 draws from rows 44, 64 or 65 has moved. (Rows 1, 4, 12, 13, 22, 23 and 192, which Doc_04 actually cites, were re-verified this review and are unaffected.)

### M7 — §2 names "the Repetition test" as the unified fifth candidate's failing test, but the argument given is a fragmentation argument, not a recurrence argument, and on the Framework's own wording the unified candidate would pass Repetition

**Site:** line 20.

Round 1's M12 asked §2's second not-advanced candidate to name its failing test, as the first one does. The fix pass supplies: *"**It fails the Repetition test at the point of generation, in the unified form Doc_01 §6 poses it:** what recurs across the two bishops is not one evidentiary base but three distinct ones wearing a single label."*

CF V7.4 Part III's Repetition Test, verbatim and entire: *"**Does it recur across evidence streams?**"* On that criterion the unified candidate recurs across three independent streams (Cyprian's lapsed corpus, the anti-Donatist corpus, the anti-Pelagian corpus) — which is a pass, not a failure. What Doc_04 actually argues is that the three streams are not instances of one thing, which is a claim about whether the candidate is a single organizing force at all — closer to Dependency ("do other dimensions depend upon *it*") or to the Candidate Gravity Generation discipline than to Repetition. The argument itself is good and the fragmentation reading is correct (verified independently, see clean-check 8); the test label attached to it is not.

**Fix:** either re-label the failure to the test the argument actually runs, or restate it as a generation-stage finding (the unified candidate is not one candidate) rather than a six-test result — which is what §2's own heading, "Candidates Considered and Not Advanced," is for, and which the first not-advanced candidate does correctly.

---

## LOW

### L1 — Round 1's L5 is carried forward unfixed: four Cross-Checks still state "Documented" flatly over Registry Confidence-B rows
Lines 49, 79, 130, 145. Candidate 2 rests partly on row 2 (*De Lapsis*, **B**, "not independently re-collated line-by-line this session"); Candidate 4 on rows 15, 18, 19, 21 (**all B**); Candidate 7 on row 23 (**B**); Candidate 8 on row 2 again. Doc_02 §8's bracket — *"Documented / Widely Accepted: ... the existence and basic content of the major primary texts named at §1"* — makes the ratings defensible, and is still not cited. **Fix:** cite Doc_02 §8's bracket, or state "Documented for existence and basic content; the specific loci at Registry Confidence B."

### L2 — Round 1's L9 is carried forward byte-identical: Candidate 7's forces notation quotes §6 prose while claiming it as the Ongoing/External *cell* content
Line 131. The cell reads *"Manichaeism and Pelagianism as live rival systems Augustine's own pastoral work directly answers"*; the quoted words are from §6's *"What was it responding to"* paragraph. Candidate 2's parallel notation (line 50) quotes its cell exactly, so the inconsistency is visible within the document. **Fix:** quote the cell; cite the prose separately if wanted.

### L3 — Round 1's L3 is only half-fixed: §5's attribution is corrected, line 88's is not
Line 88 still reads *"Doc_01 §8 item 10 directs this document to weigh this axis 'with particular weight, not yet closed'"* — byte-identical to the draft. "not yet closed" is item 10's own heading; "with particular weight" is Doc_01 §4's and §8 **item 7**'s. §5 (line 165) now dual-attributes the same spliced phrase to "(Doc_01 §4, §8 item 10)," which is closer but still presents one quotation assembled from two sites. **Fix:** quote each phrase from its own site, at both places.

### L4 — Candidate 5's classification paragraph cites "the document's own words above" for a phrase that appears only below it
Line 99 quotes *"real, substantial, and directly quoted evidence of a live theological difference between this world's own two anchor figures"* as being "in the document's own words above." The phrase occurs at exactly two places in the document: line 99 itself, and line 202 (§7 Open Item 2) — 103 lines *below*. (The companion phrase in the same sentence, "a live, unresolved theoretical residue of the century-gap itself," does appear above, at line 97.) **Fix:** attribute to §7 Open Item 2, or drop "above."

### L5 — The sentence correcting Round 1's H5 splice misquotes the Primary definition it is correcting against
Line 167: *"('**Shaping participants pervasively**' is the **Primary** gravity definition three subsections later...)"*. CF V7.4 Part III's Primary paragraph reads: *"Primary Gravities organize the ecology broadly. Multiple dimensions depend on them. **They shape formation pervasively.**"* — *formation*, not *participants*. The phrase inside Doc_04's quotation marks is the draft's own splice being quoted back, not the Framework's words. The substance of the correction is right; the quotation is not. **Fix:** quote the Framework's actual clause.

### L6 — Template §9's Document Log requirement is not discharged as worded
Template §9: *"Required, per the OneDocAtATime Build Protocol's own file-saved-review discipline: **every review round, whether it was saved as its own file, and what it found**."* Doc_04 §8 logs two entries — the drafting and the fix pass. The Round 1 review round itself (2026-09-10, saved as `Review-Artifacts/Doc04_Round1_Review.md`, verdict SUBSTANTIAL REVISION REQUIRED) is never logged as a round with its own date; its existence is inferable only from the fix-pass entry. IJC's own Doc_04 keeps rounds in its Disposition instead, which is why the Template asks for them by name. **Fix:** add the Round 1 round as its own Document Log line.

### L7 — Candidate 6's "687" citation drops Doc_03's own two scope qualifiers, which Candidate 5's parallel citation keeps
Line 103: *"'baptism' occurs 687 times within *On Baptism* alone per Doc_03's own sweep."* Doc_03: *"'baptism' occurs 687 times within the treatise itself, **markup stripped**, **scoped to its own div2 boundaries** rather than the larger volume it sits inside."* Candidate 5's "plenary" citation (line 86) carries the div2 qualifier correctly, so the omission is inconsistent within the document. **Fix:** carry both qualifiers, as line 86 does.

### L8 — The Forces Framework's own consequence for a gravity that cannot be connected to a force is never engaged, at the one candidate that exhibits it
Forces Framework V1.1 Section 4, Step 4, verbatim: *"**A gravity that cannot be connected to the forces acting on the world is a gravity whose ecology is incomplete.**"* Candidate 5's forces notation (line 97) reports exactly that shape — *"Does not hold, shift, intensify, or fracture under a named external force the way Candidates 2, 3, and 6 do"* — and Doc_04 never notes what the governing framework says follows from it. (It does place the candidate inside Doc_01 §6's Ongoing/Internal cell placement note, which is a partial connection and worth saying so.) **Fix:** name the Forces Framework rule and state how the cell-placement connection answers it, or record the incompleteness as an Open Item.

### L9 — The Classification Summary's fourth column is renamed from the Template's own wording without saying so
Template §4 specifies the column as *"Cross-Strand (or declared substitute) status."* Doc_04 heads it *"Article 21 status."* The cells do carry the declared substitute's results (phase-boundedness per candidate), so this is compliant in substance — but Doc_04's own header claims the Template as the source of this table, and renaming a specified column silently makes the compliance harder to check than it needs to be. **Fix:** use the Template's column name, or note the rename.

### L10 — "Doc_03's 'preaching'/'catechesis' entry" is singular for two separate Doc_03 entries with different evidentiary grounds
Line 71. Doc_03 carries "preaching" and "catechesis" as two distinct rows, with different tags (`[SC], [RT]` vs `[SC], [TC], [RT]`), different Registry sources, and expressly different kinds of ground — preaching on raw frequency, catechesis on dedicated treatises, a distinction Doc_03's own risk cell makes a point of. Doc_04's compressed citation collapses them. **Fix:** name both entries, or cite the one the figure comes from.

---

## COSMETIC

### C1 — Round 1's C3 is only half-fixed: the Status line and the Disposition still restate the same CO-022 sentence
Line 3: *"Not yet self-disposed; per CO-022, a substantial revision returns to independent review before disposition."* Line 214: *"**Not yet self-disposed.** ...per CO-022, a substantial revision returns to independent review before any disposition."* The fix pass added a cross-reference ("this document's own status above states current status only") without removing the duplication the cross-reference acknowledges.

### C2 — The L4 Template is a companion to Construction Framework **V7.3**; Doc_04 is governed by V7.4, and the difference is not noted
`Doc_04_Gravity_Discovery_Template_V1.0.md`, first line: *"Companion to Construction Framework **V7.3**, Part III."* Doc_04's "Governed by" line names V7.4 Part III and the Template together with no note. Nothing in this review's check of Part III suggests the two versions diverge on anything Doc_04 relies on — but Open Item 3 is a finding *about* a Framework/Template mismatch, so the version pairing is worth one clause.

### C3 — Candidate 8's heading carries "[Tensional]" inline; Candidate 5, now also Tensional, does not
Line 135: *"### Candidate 8 **[Tensional]** — Confessor-Authority vs. Episcopal-Regulated Peace."* Line 84: *"### Candidate 5 — Conciliar Authority Theory (Egalitarian vs. Hierarchical)."* The convention is inherited from IJC's Doc_04 (its Candidate 6 heading). Two candidates now share a classification and only one is marked in its heading, which makes the reclassification harder to see at a glance than it should be.

---

## Fix-pass verification table

| Round 1 finding | Status | Note |
|---|---|---|
| H1 — Doc_02 §10 Article 3 phantom (Cands. 2, 3) | **PARTIAL / NEW DEFECT** | Pointer correctly repointed to Doc_01 §5 (real); Cand. 3's Dependency quotation now verbatim. But Cand. 2's claim carried over unchecked and is false of Doc_01 §5 (R2 H2); Cand. 3's "right of communion" still miscited to Doc_02 §1 (R2 M1) |
| H2 — Possidius in Cand. 1's Cross-Check | **FIXED** | Struck from line 34 and restated at line 26 with the vendoring date and the unread-status disclosure |
| H3 — false [CT] tags (Cands. 5, 6) | **FIXED** | Actual tags substituted exactly; Doc_03's reason for withholding [CT] correctly reported |
| H4 — fourth label unearned; IJC precedent inverted | **PARTIAL / NEW DEFECT** | (c) and (d) fully fixed; Supporting genuinely tested. Tensional quoted but not argued (R2 H5); Cross-Check divergence deleted in the same pass (R2 H3) |
| H5 — Primary clause spliced into gravity definition | **FIXED** | Gravity definition now quoted verbatim and clean; residual misquote of the Primary clause itself (R2 L5) |
| H6 — Article 21 check run against Cand. 5 only | **PARTIAL / NEW DEFECT** | Formation-emphasis leg now assessed. But the sentence carrying it misattributes the reopening trigger to Article 21 (R2 H4), and the paragraph claims to address ecological orientation and does not (R2 M2) |
| M1 — Author Gravity flags | **FIXED** | Flagged at generation for Cands. 2, 5, 7, 8 — the four Round 1 named |
| M2 — two deferred World Separation questions | **PARTIAL** | Both closed by name; the new-gravity closure overstates (R2 M5) |
| M3 — Antiochene contrast (§8 item 6) | **FIXED** | Discharged explicitly at §5 |
| M4 — Template unnamed; Open Item 3; §5 substitute | **FIXED** | Template added to Governed by; Open Item 3 restated as a mismatch citing Template §4; phase testing declared and argued against Template §5's "serves the same purpose" requirement |
| M5 — Cand. 5 Interaction three-way inconsistency | **FIXED** | 1↔5 argued in both §3 bullets; line 95 and §6's note now agree with the matrix |
| M6 — Cand. 4 verdict stated three ways | **FIXED** | §3, classification paragraph and summary row all reconciled |
| M7 — summary table hardens Cand. 5's Formation | **FIXED** | Restated as "does not clearly pass Formation" |
| M8 — coercive-capacity quotation spliced | **NOT FIXED** | Byte-identical to the draft; Document Log reports it corrected (R2 M3, R2 H7) |
| M9 — *On Baptism* II.3 miscited to Doc_02 §1 | **FIXED** | Repointed to Doc_01 §4/Doc_03, with the thin Doc_02 footprint disclosed |
| M10 — fabricated clause in Doc_03 quotation | **FIXED** | Quotation restored verbatim; the second clause restated as Doc_04's own gloss |
| M11 — "lay-confessor" miscited to Doc_02 §6 | **FIXED** | Attributed to Registry row 1's Licensed-For column, Doc_02 §6 pointer retained |
| M12 — unified candidate's failing test unnamed | **PARTIAL** | A test is now named; the argument given does not run that test (R2 M7) |
| M13 — Cand. 6 as novel discovery | **FIXED** | Stated as a promotion of Doc_01 §4's rival-consecration-validity axis |
| M14 — undisclosed dependency on Doc_01's routing | **FIXED** | Disclosed in one clause at §5 |
| L1 — dropped "alone" scope qualifier | **FIXED** | Restored at lines 26 and 56; the two claims separated |
| L2 — "respectively" for three entries | **FIXED** | All three entries now carry their own figures |
| L3 — §8 item 10 quotation spliced | **PARTIAL** | §5 dual-attributes; line 88 byte-identical (R2 L3) |
| L4 — "weakest on the axis" subject collapsed | **FIXED** | Argument and finding now distinguished, as Doc_01 §5 distinguishes them |
| L5 — flat "Documented" over Confidence-B rows | **NOT FIXED** | No Cross-Check gained the qualifier (R2 L1) |
| L6 — Cand. 1's bullet omits Cand. 5 | **FIXED** | "reinforced weakly by Candidate 5" added |
| L7 — Cand. 8 Dependency verdict missing | **FIXED** | "Passes." added |
| L8 — Ending/Transforming adjective substituted | **FIXED** | "theological" restored, with the narrowing disclosed as Doc_04's own application |
| L9 — Cand. 7 quotes §6 prose as cell content | **NOT FIXED** | Byte-identical to the draft (R2 L2) |
| L10 — IJC folding reported one candidate wide | **FIXED** | Matches IJC §2's own wording |
| L11 — "Attention Presence" with no presence pattern | **FIXED** | Doc_02 §5's liturgical-evidence concentration named as the presence pattern; verified accurate against §5 |
| L12 — row 22's Licensed-For phrase | **FIXED** | Row 22's own phrase now quoted |
| L13 — "Doc_03's own full sweep" | **FIXED** | Scoped to "any candidate term on Doc_03's own list" |
| L14 — "Doc_01's own preliminary list" | **FIXED** | Narrowed to "Doc_01 §3's own four named candidates" |
| C1 — Article 22 omitted | **FIXED** | "Articles 21 and 22" |
| C2 — truncation without ellipsis | **FIXED** | Doc_02 §2 quotation extended and ellipsed |
| C3 — Status/Disposition duplication | **PARTIAL** | Cross-reference added; duplication retained (R2 C1) |
| C4 — swept headword "preach" | **FIXED** | Headword now named correctly |

**Totals, counted from the table above and checked to sum: 28 genuinely fixed · 7 partially fixed · 3 not fixed = 38.**

- **Genuinely fixed (28):** H2, H3, H5; M1, M3, M4, M5, M6, M7, M9, M10, M11, M13, M14; L1, L2, L4, L6, L7, L8, L10, L11, L12, L13, L14; C1, C2, C4.
- **Partially fixed (7):** H1, H4, H6, M2, M12, L3, C3 — of which **H1, H4 and H6 additionally introduced a new defect** (R2 H2/M1, R2 H3/H5, R2 H4/M2 respectively).
- **Not fixed (3):** M8, L5, L9 — two of them (M8, L9) byte-identical to the pre-fix draft.

---

## Registry staleness question, checked directly and answered against the current record

The commission asked whether rows 37, 44, 64, 65 and 206 of `Source_Registry.md` still assert their texts are unavailable on this world's branch, and whether Doc_04 relies on that unavailability. Checked at source:

**The premise no longer holds, as of earlier today.** `lpc_Decision_Log.md`'s 2026-09-13 entry records eight stale text-location claims corrected across seven rows (37, 44, 56, 64, 65, 206, 208), each verified with `git ls-tree` rather than `ls`. Reading the rows themselves confirms it: row 37 now reads *"Vendored in the shared corpus"*; row 206 reads *"Vendored"*; row 64's "not currently vendored" is scoped to Labrousse's in-copyright SC edition specifically, with Ziwsa's public-domain CSEL 26 named as already vendored and the edition of first resort; row 65's is scoped to Lancel's in-copyright SC edition. Row 44's remaining "not vendored" concerns the OTA TEI file under CC BY-NC-SA, correctly excluded by the project's own vendoring rule. None of the five is stale in the way described. That Decision Log entry also anticipates this round by name: *"Doc_04's own Round 2 review was already running against the pre-correction text when these edits were made."*

**But the substantive question it points at is live, and is reported above as H6.** Row 65, as corrected, states that the *Gesta Collationis Carthaginiensis* is vendored in the shared corpus, is now assigned to this world's own corpus-map entry (verified: PR #177, commit `c19523fd`, corpus-map line 749, `role: context`, `confidence: provisional`), carries Augustine speaking in his own recorded voice in fourteen numbered acts of the 411 Conference, and is **"available to Doc_04, and not yet drawn on by it."** Doc_04 does not rely anywhere on those texts being *unavailable* — it never mentions them — which is itself the problem: Candidate 5's Repetition and Persistence verdicts rest on unqualified absence claims about inter-episcopal authority evidence outside two single loci, and the most obvious place in this world's corpus to test those claims has not been opened. One consequential note for Doc_04's own header (R2 M6): the same Decision Log entry returns `Source_Registry.md` to independent review, so its "Approved to proceed" status in Doc_04's companion-documents line is now stale.

---

## Escalation-category assessment (CO-022)

Run against all four categories, with near-misses checked rather than assumed away.

**1. Representative-identity decisions — does not apply.** Nothing in Doc_04 names, titles, characterizes or constrains this world's Representative. Round 1's near-miss (the [CT] claims travelling into Doc_06) is retired: H3 is fully and accurately fixed, and this review re-derived all three tag cells independently rather than accepting the fix's account of them.

**2. Portfolio-level / cross-world decisions — does not apply, and the near-miss Round 1 flagged is closed.** Round 1 made category 2's standing conditional on line 197 being corrected. It was: Open Item 3 now withdraws the false "second independent world's own use" claim and reports IJC's record accurately, quoting the half of IJC's Open Item 4 the draft omitted. All five IJC references were re-read at source this round and all five are accurate. The *Gesta* corpus-map assignment (H6) is a cross-world resource decision, but it was made by the project lead on the record (PR #177) and Doc_04 would be *applying* it, not making it.

**3. Governance / methodology decisions — TRIPPED, at low intensity, on one limb, and the limb has moved.** Round 1's two limbs are both discharged: Template §5's substitute requirement is now declared and argued (phase testing), and Open Item 3 correctly states the Framework/Template mismatch and routes it to IJC's existing System Hub item rather than opening a new one. What replaces them is narrower and is properly a build-thread fix, not an escalation: **H7's certification defect.** A fix pass that reports 38/38 addressed while three findings sit byte-identical is a process failure in the build thread's own verification discipline, not a methodology change — and the remedy already exists in this world's own record, at the 2026-09-13 Registry entry, which caught the identical mechanism by reading the full word-level diff after a too-strict search returned clean. Recommend that discipline be applied to Doc_04's next fix pass as a condition of the pass, not as a new rule for the portfolio.

**4. Unresolved tensions the pipeline can't close — does not apply, checked directly on the question this commission raised.** Every HIGH finding above closes inside the pipeline without new evidence, with one qualified exception:

- H1, H2, H3, H4, H5 and H7 close on documents already in hand — re-reading Doc_01 §4 and §5, restoring a deleted Cross-Check note, re-attributing a caveat, and either arguing or qualifying a Framework definition. None requires a decision the build thread cannot make.
- **H6 is the exception, and it is a resource question, not a tension.** Testing Candidate 5's absence claims against the *Gesta* requires reading a poor-OCR Migne scan that the Registry itself instructs be handled by normalization rather than quotation. If that read is not affordable in this pass, the honest disposal is disclosure — state the bound, carry the question as an Open Item — which is fully within the build thread's competence and is what this review recommends. Escalation would only be warranted if the classification were to be defended *past* the undisclosed bound.
- **On whether the Tensional classification itself is safe to hold:** yes, on Doc_01 §8 item 10's own terms, and this review reaches that independently of the defects above. Item 10's trigger is *"surfaces evidence this document has not weighed."* Doc_04 re-weighs Doc_01's own two quotations and surfaces none — so the strand-singular finding stands whatever Candidate 5's final classification is. That conclusion does **not** currently rest where §5 puts it (H4), and it should be rebuilt on item 10's own wording plus Article 21's "once made, governs," rather than on a reopening trigger the Constitution does not contain.

**Result: one category tripped (category 3, governance/methodology), at low intensity, on one limb that is a verification-discipline failure inside this document's own fix cycle rather than a methodology change. Categories 1, 2 and 4 do not apply. No project-lead escalation is warranted ahead of the next fix pass.**

---

## Note on disposition — deliberately not assessed

Consistent with this folder's practice across the Doc01, Doc02, Doc03 and Doc04 Round 1 series, this review does not recommend a disposition. Doc_04's own Status line and Disposition both state that a substantial revision returns to independent review before disposition, and the sequencing is the build thread's and the project lead's to run.

Two observations offered without recommendations attached.

**First, on the shape of what is left.** Of 27 findings, 12 are citation-accuracy defects, 6 are carried-forward or half-fixed Round 1 findings, 3 are new defects the fix pass itself created, and 6 concern the reasoning. That is a better ratio than Round 1's, and the document's hardest structural judgments — the fragmentation reading at §2, the demotion of Doc_01's third-named candidate, the refusal to let Candidate 2's cross-phase lean survive, and now the move from a non-Framework label to a real one — all hold. What does not hold is the argument *around* the one classification the commission flagged, and it does not hold in four separate places at once.

**Second, on the mechanism.** Three of this build's last four rounds have now found the same thing: a fix that repoints, deletes or renames without re-reading what sits at the other end. H2 above is the purest instance yet — the pointer was corrected, the claim attached to it was not checked against the new target, and the verification run afterward tested only that the old pointer was gone. The two byte-identical "fixed" findings (M8, L9) are the same mechanism at one remove: a Document Log entry written from the fix list rather than from the file. The remedy this world already owns — read the full word-level diff, hunk by hunk, against each finding's own site, after the targeted search comes back clean — was applied to `Source_Registry.md` yesterday and caught three instances no search would have found. It was not applied here.

---

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 7 HIGH · 7 MEDIUM · 10 LOW · 3 COSMETIC, 27 in total. Fix-pass verification: 28 of Round 1's 38 findings genuinely fixed, 7 partially fixed, 3 not fixed; 3 of the partials introduced new defects.**

**Simulated review — informational only, not an Article 31 substitute.**
