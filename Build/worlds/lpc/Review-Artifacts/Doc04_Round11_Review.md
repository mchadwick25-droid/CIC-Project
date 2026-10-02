# Doc_04 — Gravity Discovery: Latin Pastoral-Congregational Christianity
## Round 11 Independent Adversarial Review — the mechanical pass run against a given site list: did the list work, what did the list miss, and is the document now adequate?

**Marked per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.**

**Review date:** 2026-09-14.

**Documents reviewed, at commit `619cca3c` (prior state `3d45c279`), branch `lpc-doc04-round2`, working tree clean:**

- `World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_04_Gravity_Discovery.md` (251 lines)
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_04_Superseded_Claims.md` (61 lines)
- `World-Builds/Latin-Pastoral-Congregational-Christianity/lpc_Decision_Log.md` (all seven 2026-09-14 entries and every in-place `[CORRECTION]` / `[FURTHER CORRECTION]` / `[SUPERSEDED]` notice)

**Read for context and used as the test standard, not reviewed:** `Source_Registry.md` row 65 in full; `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` at lines 121700–121800, 118166, 126796, 126874, 128393, 128716, 129009; `L3B-World-Build-Methodology/Doc_04_Gravity_Discovery_Template_V1.0.md` §§4, 5, 6, 7, 9; `Doc04_Round3_Review.md` L6, `Doc04_Round7_Review.md` H8, `Doc04_Round8_Review.md` H8, `Doc04_Round10_Review.md` in full; the Doc_04 and appendix blobs at `3d45c279`.

### Method

This reviewer drafted nothing under review, wrote no version of the *Gesta* read, ran no fix pass in this document's history, wrote neither the mechanical pass nor Round 10's site list, and is not the thread running Round 10's blind read of §4/§5/§6. **Candidate 5's classification is the project lead's ruling and is not revisited here.**

This pass is structurally unlike the ten before it: it did not choose its own sites. The method was built around that single variable.

1. **Every one of the sixteen named sites was opened at HEAD and at `3d45c279` side by side**, and each was classified as *fixed as specified*, *fixed differently*, *not fixed*, or *fixed with a new defect introduced*.
2. **The list was then treated as the suspect object.** Four independent sweeps were run for the propositions Round 10 declared withdrawn — the ambiguous-results basis, the gating-clause denial, the "third clause" argument, and any statement of Candidate 5's classification or test results — across all three files, by vocabulary *and* by subject, without reference to Round 10's site numbers. This is where the method's one structural limit shows (H4).
3. **Every edit the pass made was re-read for what it broke elsewhere**, not only for what it fixed. Two of the four HIGH findings below are defects the pass's own correct edits created at sites nobody had reason to list (H1, H2).
4. **The three restorations were re-derived from the round that originally required them** — Round 3's L6 at `Doc04_Round3_Review.md` line 262, Round 8's H8 at `Doc04_Round8_Review.md` line 228, Round 9's endorsement of its surviving half — and compared to the withdrawn form to test for reinstatement of a superseded version.
5. **The row 65 / act 158 conflict was adjudicated at source**, by opening the *Gesta* file, reading the whole page the act sits on (page header at file line 121727 through act 159 at 121790), and comparing act 158's recorded form against every other Augustine act located in the volume and against the three parallel subscription formulae on the same page. This section is the one that changes the finding Round 10 reached.
6. **Structure machine-checked:** per-row pipe counts on all three tables; `**`, single-`*` and backtick parity on all 251 lines of Doc_04 and all 61 of the appendix; all 28 matrix pairs for symmetry and every §3 Interaction bullet against its own matrix row; §4's Six-Test and Classification cells against §3's bullets and classification lines.
7. **The pass's own Decision Log entry was tested claim by claim** against the diff, not against the review it names.

---

## VERDICT: REVISION REQUIRED

**Findings: 4 HIGH · 7 MEDIUM · 10 LOW · 3 COSMETIC — 24 in total.**

**Did working from a given list work? Yes — materially, and for the first time in eleven passes the enumeration step did not fail.** All six named Doc_04 sites and all four named Decision Log sites were genuinely worked. Nine of Round 10's findings are cleanly closed, including all three of the ones that had survived four and five rounds (`"tested in full and found Supporting"`, `"fully tested"`, `"failing Formation"`). All three restorations are accurate against the round that required them, and none reinstates a superseded form. The §4 index-table cell — the site Round 10 called its central finding and the route a superseded basis would take into Doc_05 — is correct, and the classification now reads identically at the Status line, §3, §4, §5, §6 and Open Item 2. That has never been true before.

**What the list could not do, in three shapes.** *(i)* It inherits the list-writer's omissions: a fifth Decision Log site carrying the same withdrawn basis, in bold and unmarked, was not on the list and is still there (H4), and three sites of inline correction narration the restructure pass existed to eliminate were never named by anyone (M3). *(ii)* It cannot see defects its own correct edits create at sites off the list: adding Round 10 to §8 falsified the Status line and the Disposition in the same commit (H1), and correcting the appendix's non-reliance claim at line 7 put that line into direct contradiction with line 3 and with Doc_04 line 245 (H2). *(iii)* It propagates the list-writer's unverified source adjudications. Round 10 opened the *Gesta* and concluded the Registry has the better of the act-158 question. **It does not. I opened the same file and the finding reverses** (H3, and the adjudication section below). The pass took that conclusion into the permanent record without opening the file — which is the precise failure the two unopened governance items exist to stop, committed this time by a pass whose whole discipline was to take the review's word for things.

**Is the document adequate to proceed to Doc_05? On its substance, yes** — and I say so in the adequacy section below, with the two sentences that have to be corrected first written out. This is the first round in this document's history where the answer is not "not yet."

---

## What was checked hard and found CLEAN

These were tested expecting a defect. Each is clean, with the basis given so the check is reproducible.

1. **§4's Candidate 5 Classification cell is correct and carries nothing withdrawn.** Line 162 now reads *"**Supporting** — on the project lead's ruling of 2026-09-14. This document's six-test profile for the candidate is narrow; see §3."* All four of Round 10's H1 limbs are gone: `grep -c "ambiguous"` in Doc_04 returns **0**; *"directs"* is gone; *"to be revisited at Doc_05"* is gone and occurs nowhere in the world folder outside `Review-Artifacts/`; and *"Supporting (provisional)"* — outside the Template's enumerated set, Round 9's M3 — occurs zero times. The cell's added clause is not a new claim: *"six-test profile ... is narrow"* is line 99's own word, and the cell's Six-Test column two places left states the six verdicts in §3's exact terms. **Round 10's H1, Round 9's H1/H2 at §4, Round 9's M2 and M3 are all discharged at this cell.**

2. **The three restorations are accurate against the rounds that required them, and none reinstates a superseded form.** Round 3's L6 second limb (`Doc04_Round3_Review.md` line 262: row 65's Source is Lancel's SC edition, Confidence C, consultation-only) is back at line 90 as a present-tense fact — *"recorded in Registry row 65's Verification Note — **row 65's own Source cell is Lancel's in-copyright Sources Chrétiennes edition, which is not the text meant here**"* — with the vendored Migne path still named, which is L6's core. `grep -c "Lancel"`: **1** at HEAD, 0 at `3d45c279`. The *"neither established nor refuted"* symmetry is back at line 99 verbatim, which is what Round 8's H1 was written to secure. Round 8's H8 disclosure is back at line 101 in the half Round 9's H5 expressly endorsed — *"Alone among the eight candidates, this line does not record this document's own verdict on the evidence"* — **without** the *"in CF V7.4's own sense"* half Round 9 struck. That was the specific risk in a restoration and the pass did not take it.

3. **§5 and §6 no longer say anything about Candidate 5 that §3 denies.** Line 186 now enumerates *"narrow passes on Repetition, Dependency, Explanatory and Interaction, not clearly passing Formation, and not passing Persistence at world level"* — §3's and §4's exact vocabulary, with *"failing Formation"* gone. Line 188's *"tested in full and found Supporting"* is gone. Line 203's *"fully tested"* is gone. `grep -c "tested in full\|fully tested\|failing Formation\|fails Formation"` in Doc_04 returns **0**. **Round 9's H6(a)(b)(c), Round 7's M2 (fourth round) and Round 6's M12 / Round 9's M9 (fifth round) are discharged.**

4. **The four named Decision Log sites carry the further correction, and it is accurate.** Lines 678 and 696 each close with *"**[FURTHER CORRECTION, Round 9.]** The ambiguous-results basis named here is also withdrawn: CF V7.4's antecedent is 'where gravity tests yield ambiguous **results**,' and this document's six tests yield six determinate verdicts."* Line 750's heading and the *"What is now stated"* paragraph at 764 each carry a `[SUPERSEDED, Round 9: …]` marker. Both markers state the antecedent correctly and neither over-reaches. **Round 8's H4/H5 and Round 9's H9/M12-at-the-log are closed at these four sites.** (The fifth site is H4 below.)

5. **Structure is clean throughout, including the rows the pass added.** Three tables, per-row pipe counts uniform within each: §4 all **6** across ten rows, §6 all **10** across ten rows, §8 all **5** across twenty-four rows — the three new rows included. `**`, single-`*` and backtick parity balanced on all 251 lines of Doc_04 and all 61 lines of the appendix — **zero exceptions in either file**. **All 28 matrix pairs symmetric**, with 2↔7 the reciprocal *Reshaped by* / *Reshapes* pair and 2↔8 the reciprocal *Competing* pair; all eight diagonal cells `—`. Every one of the eight §3 Interaction bullets agrees with its own matrix row, Candidate 5's included (1 weakly, 3, 6 reinforcing; 2, 4, 7, 8 no demonstrated relationship). §4's eight Classification cells agree with §3's eight classification lines, and each §4 Six-Test cell is derivable from its candidate's own six bullets.

6. **§8 satisfies Template §9, and the three added rows are accurate.** Template §9 requires *"every review round, whether it was saved as its own file, and what it found."* The Round 10 row — `2026-09-14 | Round 10 review | Doc04_Round10_Review.md | SUBSTANTIAL REVISION REQUIRED — 5H 11M 12L 3C` — matches Round 10's own `**Review date:**` line and its `## VERDICT` block exactly (*5 HIGH · 11 MEDIUM · 12 LOW · 3 COSMETIC*). The Restructure pass row's date matches commit `9c70765b` (2026-09-14) and its Result cell states what the commit did. The Mechanical pass row's date matches `619cca3c`. **Round 10's M4 and Round 6's H7 are discharged.** (One cosmetic asymmetry at C3.)

7. **Round 10's second closing step is correctly declined, not excused.** The pass states that Round 10's blind read *"cannot be taken here"* because *"this thread wrote all four sections and cannot perform that test on its own work."* That is accurate, not an evasion: Round 10's test is defined by its reader's ignorance of §3, and this pass rewrote §3 in the same commit. The thread cannot unread it, and a self-administered version would return a guaranteed pass and would be worse than not running it. **This is the correct answer and the pass gives it plainly.** (What it does not do — route the test to anyone — is M7.)

8. **The one fact Doc_04 says it relies on is true at source.** Verified independently, against the vendored file rather than against either withdrawn read or either record that describes it. See the adjudication section. **This is the first claim in this build's *Gesta* history to survive an at-source check by a thread that did not make it.**

---

## HIGH

### H1 — Adding Round 10 to §8 falsified the Status line and the Disposition in the same commit: Doc_04 now says its review record stops at Round 9 while its own log lists Round 10, and records nowhere that Round 10's findings are outstanding

**Sites:** lines 3 and 249. **Cause:** the three rows added to §8 at lines 241–243. **Neither line was on Round 10's list, because at Round 10 both were true.**

Line 3, the Status line, untouched by this pass:

> *"Review rounds **1–9** are listed at §8; findings from **Rounds 5–9** are outstanding and the artifacts in `Review-Artifacts/` are the record of them."*

Line 249, the Disposition:

> *"**Not yet self-disposed.** Findings from `Doc04_Round5_Review.md` **through `Doc04_Round9_Review.md`** are outstanding."*

§8 at HEAD lists **ten** review rounds. The first clause of line 3 is now flatly false. And the second clause of each is false in the direction that matters: by the pass's own Decision Log entry, Round 10's **L1–L12, M9 and M11** were not addressed, and this review finds a further six of Round 10's findings unclosed or half-closed (H5, M3, M8, H3-residue, C1, C2). Fourteen-plus outstanding findings from a review the document's own log names, and the document's two self-description sentences both stop one round short.

**Why this is HIGH rather than a stale-pointer MEDIUM.** These two sentences are the only places Doc_04 tells a downstream reader what state its review record is in, and the Status line is the first line a Doc_05 builder reads. A builder who reads line 3 and then opens `Review-Artifacts/` for *"Rounds 5–9"* will not open `Doc04_Round10_Review.md` at all — and Round 10 is the round carrying the act-158 tension, the completeness defect, and the finding that the whole build has a derived-restatement problem. The document actively directs the reader away from its own most recent review.

It is also exactly the class of defect ten rounds have found, produced by the one method that was supposed to be immune to it: the pass edited §8 correctly and did not ask what else in the document states a fact about §8.

**Fix — two sentences, given in full so no further round is needed to specify them.** Line 3: *"Review rounds 1–10 are listed at §8; findings from Rounds 5–10 are outstanding and the artifacts in `Review-Artifacts/` are the record of them."* Line 249: *"Findings from `Doc04_Round5_Review.md` through `Doc04_Round10_Review.md` are outstanding."*

---

### H2 — The appendix's completeness claim is now asserted at two sites and denied at a third, and the pass reports it "corrected"

**Sites:** `Doc_04_Superseded_Claims.md` lines 3 and 7; `Doc_04_Gravity_Discovery.md` line 245. **Round 10's H5, not fixed, and made worse.**

Appendix line 3, **unchanged by this pass** though the pass lists it among the sites it worked:

> *"It holds **every** claim that document has made and withdrawn, so the document itself can state current claims only."*

Appendix line 7, rewritten by this pass, four lines below it:

> *"This file records the withdrawn claims its sections cover; **it is not an exhaustive index of every claim the document has ever revised**, and §4 in particular is a selection."*

Doc_04 line 245, rewritten by this pass:

> *"**Every claim** this document has made and withdrawn is recorded at `Doc_04_Superseded_Claims.md`."*

Two of the three say *every*; one says *not exhaustive*. They cannot all be right, and Round 10's H5 established which is wrong: at least three withdrawn citation claims of §4's own class are absent — Round 1's M8 (the coercive-capacity quotation spliced from two findings, the named precedent for the ellipsis defect §1.4 *does* record), Round 1's M10, Round 1's M11 — plus the Round 3 fix pass's *"twenty-four lines"* / *"seven of twenty"* figures and the Round 1 fix pass's *"all 38 findings addressed"* report. None was added.

Round 10's H5 offered two exits: soften line 3, **or** add the missing entries and stand on the claim. The pass took neither. It added a denial at line 7, left the assertion at line 3, and then **wrote a fresh assertion of the same claim into Doc_04 at line 245** — so the contradiction that previously ran between two files now also runs inside one.

And the pass's Decision Log entry reports: *"The appendix's completeness and non-reliance claims are corrected (M8)."* The **non-reliance** claim (line 7's second half, Round 10's M8) is corrected and correctly so. The **completeness** claim is not corrected at any of its three sites. **This is the tenth consecutive pass with an inaccurate self-report**, and it is inaccurate about the one sentence Round 10 rated HIGH.

**Fix:** delete *"every"* from appendix line 3 and Doc_04 line 245, replacing both with *"the claims this document has withdrawn that a reader of the current text might otherwise expect to find in it"*; **or** add the three Round 1 entries to §4 and delete line 7's *"not an exhaustive index"* clause. Either closes it; doing neither is what is not available.

---

### H3 — The pass carried an adverse source adjudication into the permanent record without opening the source, and the adjudication is wrong: at file line 121764 the Registry and Doc_04 are compatible, and Doc_04's reading is the one the text supports

**Sites:** `lpc_Decision_Log.md`, seventh 2026-09-14 entry — the *"Not addressed"* paragraph and the *"Escalation check."*

The entry states:

> *"**M11 is the one to carry forward:** `Source_Registry.md` row 65 and the act-158 diagnosis have been unreconciled for four rounds, and Round 10 records that on the evidence it opened, **the Registry has the better of it** — which bears on the single fact `Doc_04_Gravity_Discovery.md` says it relies on from the withdrawn reads."*

and logs, under Escalation check, *"**Unresolved tensions: two open** — the evidentiary question at §7 Open Item 6, and the row 65 / act 158 conflict above."*

**I opened the file. The adjudication reverses.** The full argument is in the dedicated section below; the finding here is what the pass did with it. Doc_04's diagnosis is correct at source; row 65's factual observation is also correct at source; the two are *compatible*, and Doc_04's sentence is the explanation of row 65's anomaly, exactly as appendix §2 says it is. There is no conflict to carry, and *"the Registry has the better of it"* is not true of the text.

**Why this is HIGH and not a reporting nicety.** Three consequences, all live in the world folder right now:

1. The build's permanent record now states that the **one fact Doc_04 says it relies on** is probably wrong. It is not. A Doc_05 builder, or the project lead deciding whether to commission the *Gesta* read, reads that and discounts the only surviving datum from two withdrawn reads — the datum that is in fact the soundest thing in this build's *Gesta* history.
2. A non-conflict has been escalated as an open unresolved tension under CO-022 category 4, on a row belonging to a document that is *"returned to independent review."* That is a governance action taken on a false premise.
3. **It is the failure mode the whole governance question exists to prevent, committed by the pass built to avoid it.** The pass's own opening line is that the enumeration was taken from the review because *"every remedy this thread designed for itself has failed."* Taking the *enumeration* from the review is sound. Taking a *source adjudication* from the review, restating it in the record as bearing on reliance, and declaring it *"another document's row and is not altered from here"* — without opening the file it is about — is the propagation-before-verification defect under a new name. Round 8's own remedy, quoted in this log at line 740, is *"the proposition was verified against the whole governing [source] before being propagated, not after."* That was not done here.

**Fix:** correct the seventh entry — record that the adjudication was run at source at Round 11 and reversed, that the two records are compatible, and that what remains is a one-clause Registry amendment rather than an escalation; and strike the row 65 / act 158 item from the entry's unresolved-tensions count. The amendment row 65 needs is given in the adjudication section.

---

### H4 — The withdrawn ambiguous-results basis is still asserted, in bold and unmarked, at a fifth Decision Log site Round 10 did not name — inside the very entry the pass marked in two other places

**Site:** `lpc_Decision_Log.md` line **766**, the fifth 2026-09-14 entry's closing paragraph. **Not on Round 10's list. Not on the pass's list. Live at HEAD.**

> *"**This is the first classification statement in eight rounds that is neither an over-claim nor an under-claim.** The sequence was: a non-Framework fourth label (unearned) → Tensional (quoted, never argued) → Supporting on the concession clause (a concession read as a licence) → Supporting with the gating clause denied (an invalid inference from a mis-ellipsed quotation of the document's own sentence) → **Supporting held provisionally, on the provision written for candidates whose tests come out ambiguous.** Every earlier basis is withdrawn in place rather than deleted."*

Three things are wrong with it and none is marked.

**(a)** The sentence names the withdrawn basis as the sequence's terminus, in bold, two lines after a `[SUPERSEDED]` marker that withdraws it. The pass marked the entry's heading (750) and the *"What is now stated"* paragraph (764) — the two sites Round 10 listed — and stopped.

**(b)** The framing claim is now false on its own terms. *"The first classification statement in eight rounds that is neither an over-claim nor an under-claim"* describes a basis Round 9 found rested on an antecedent that is not satisfied and on a predicate moved from results onto candidates. It was an over-claim. The sentence is a self-assessment that the next round refuted, standing unmarked in the record as a verdict.

**(c)** *"Every earlier basis is withdrawn in place rather than deleted"* is false of the paragraph containing it: this basis was not withdrawn in place until the pass under review, and this sentence still has not been.

`grep -n "held provisionally"` across the world folder, excluding `Review-Artifacts/`, returns **two** hits: line 764 (marked) and line 766 (unmarked).

**This is the answer to whether Round 10's list was complete, and it is the given-list method's one structural limit.** The pass's enumeration could not fail, because it did not enumerate. It also could not *reach* anything the list omitted — and the list omitted one site of the same class, in the same entry, two lines from a site it did name. A list is only as good as the sweep that wrote it, and Round 10's sweep of the fifth entry stopped at the paragraph it quoted.

**Fix:** append to line 766: *"**[SUPERSEDED, Round 9.]** This self-assessment does not hold: the ambiguous-results basis named as the sequence's terminus is itself withdrawn, and a sixth basis — the project lead's ruling of 2026-09-14, standing alone — is the current one."*

---

## MEDIUM

### M1 — The Tensional exclusion is still not a live claim of Doc_04, and Open Item 8 now routes the reader for it into a file whose line 7 says nothing in it is a live claim

Round 10's H3 had two consequences. The pass closed the first and left the second.

**Closed:** Open Item 8 no longer asserts *"Tensional excluded at §3."* Line 214 now reads *"**§3 excludes Primary explicitly; it does not currently exclude Tensional**"* — true of the document. `grep -n "Tensional"` returns nine hits, eight about Candidate 8 and one at 214. Doc_04 no longer says anything false about itself here.

**Open:** the argument that Candidate 5 is not Tensional — *"nothing depends on it, it moves under no named external force, and all three of its demonstrated relations in §6 are reinforcing"* — exists in the world folder only at `Doc_04_Superseded_Claims.md` §1.2, under the heading *"**1.2 Tensional.** Withdrawn,"* in a file whose line 7 still opens *"Nothing here is a live claim"* with a carve-out for **act 158 only**. So the negative classification argument for the most-contested candidate in this build is recorded exclusively as withdrawn material, and Doc_04 now points a reader at it by name.

This also sharpens Round 9's L8 / Round 10's L7 rather than closing it: §1.2 says *"nothing depends on it"*; Doc_04 line 91 says *"Doc_01's strand-singular finding is the one place in this world's construction record that **depends on this axis** at all."* Before this pass a reader had to notice the pair; now Open Item 8 sends them from one to the other.

**Fix:** either restore one sentence of the exclusion to §3 as Round 10 specified, or widen line 7's carve-out to name §1.2's argument as a second live item and reconcile it with line 91 (*"nothing depends on the candidate's classification resolving one way or the other"* is the reading both sentences will bear).

### M2 — Doc_04's Disposition and the Decision Log's newest entry now state different escalation positions, in two dimensions at once

Doc_04 line 251: *"**Governance/methodology: open, raised and not closed.** `Doc04_Round8_Review.md` and `Doc04_Round9_Review.md` each recommend opening it, on **two items**…"* and *"**Unresolved tensions: open** — the evidentiary question at §7 Open Item 6."* — **one**.

`lpc_Decision_Log.md`, seventh entry: *"**Governance/methodology: open**, now with **three items** on the record… and Round 10's addition, that extraction is itself a defect surface. **Unresolved tensions: two open**."*

Round 9's M12 found CO-022 category 3 recorded in one record and absent from the other. Round 10's M9 found the divergence had **reversed direction**. It has now reversed a third time and widened to two dimensions. The pass declared M9 not addressed, which is honest as to the sixth entry — but it wrote a *new* escalation check into the seventh entry and did not reconcile it with Doc_04's, which is how the divergence grew.

Note that the correct reconciliation depends on H3: on my adjudication the tension count is **one**, not two, and Doc_04's line is the accurate one.

**Fix:** update Doc_04 line 251 to three governance items; leave the tension count at one in both records once H3 is corrected.

### M3 — Inline correction narration survives at three sites in Doc_04, against the Status line's "held at `Doc_04_Superseded_Claims.md`, **not inline**" — and one of the three duplicates appendix §3

Line 3 states the rule. Three sites break it, none named by Round 10 and none reachable from the given list:

- **Line 34:** *"Candidate 1's Documented rating stands on Pontius, the two Letters, and the 256 preface alone; **this is a citation correction, not a classification change.**"*
- **Line 175:** *"**An earlier version of this sentence attributed the caveat to Article 21.**"* — which is recorded, in the same terms, at appendix §3: *"a version before that attributed the reopening caveat to Constitution Article 21."* The extraction's whole justification is that this content lives in one place; it lives in two.
- **Line 207:** *"per §3's own **restored** Cross-Check note"* — *restored* is a correction-history word describing an event no record in the world folder now documents. A reader cannot tell what was restored, when, or from what.

This is the defect class the restructure pass was commissioned to eliminate and which Round 10 certified eliminated (*"Where the extraction preserved, it preserved well"*). It survives at three sites. Round 10 measured apparatus reduction (its L11) and did not sweep for residue.

**Fix:** delete the clause at 34 and the sentence at 175 (both are recorded elsewhere or need no record); at 207 replace *"restored"* with *"own"*.

### M4 — Appendix §4's new preamble contradicts appendix line 5, and Round 10's M3 is reported addressed without being addressed

Line 5 (unchanged, and named among the sites the pass says it worked): *"Entries record what was claimed, what is wrong with it, and **which review round established that**."*

New §4 preamble: *"A selection, not an index. **Where a round is not named against an entry, the finding's origin is not recorded here** and the `Review-Artifacts/` files are the source."*

Round 10's M3 was that six of §4's seven entries carry no round attribution *against the promise at line 5*. The pass's Decision Log reports it as *"§4 now says it is a selection rather than an index (M3)."* That is not M3; it is H5's completeness limb wearing M3's number. Six of seven entries still carry no round — and Round 10 supplied four of the six missing attributions in its own text (Round 4's H3, Round 2's M1, Round 3's M1, Round 3's L1), so the fix was available at zero research cost and was not taken. What was added instead is a disclaimer that contradicts the file's own preamble.

**Fix:** add the four attributions Round 10 names, narrow line 5 to *"where the round is recorded, which round established it,"* and delete the contradiction.

### M5 — The pass's self-report is inaccurate in four respects, three of them in the safe direction and one not

Tested claim by claim against the diff:

| Claim in the seventh entry | Verdict |
|---|---|
| H1–H5 addressed | **H1, H4 fully. H3 half (M1). H2 four of five sites (H4). H5 not (H2).** |
| M1–M8, M10 addressed | **M1, M2, M4, M5, M6, M7, M10 yes. M3 no (M4). M8 half (H2).** |
| *"Not addressed: Round 10's L1–L12"* | **L9 is closed** by the H1 fix and **C1 substantially closed** — both of which Round 10 had marked *"subsumed by H1's fix,"* so the closure is real and the statement is stale rather than false. |
| *"…and the outstanding findings of Rounds 5 through 9"* | **Inaccurate.** The H4 fix closes **Round 7's M2** (live four rounds), **Round 9's H6** and **Round 9's M9** (live five rounds); the H1 fix closes **Round 9's M2** and **M3**. Five Rounds 5–9 findings were closed by a pass reporting that none was. |
| *"The appendix's completeness … claims are corrected"* | **False** — H2. |

Four of the five are conservative misstatements, which is a change of character worth recording: this is the first self-report in the sequence that *understates* what the pass achieved. The fifth is not conservative and is the one that matters.

### M6 — Line 188 drops the search-bound qualifier Round 10's fix specified, so §5's summary of the Article 21 result is still cleaner than §3 supports

Round 10's prescribed replacement for line 188 was *"…is tested against all six tests, **with Repetition and Persistence resting on a disclosed and undischarged search bound**, and is classified Supporting on the ruling."* The pass wrote *"…is tested against all six tests without reopening the finding that flagged it, and is classified Supporting on the project lead's ruling."*

Nothing there is false — all six tests were run. But §5 is the section that carries the Article 21 determination to every subsequent step, and its one-sentence summary of the contested axis now tells a reader the axis was tested against all six tests and gives no indication that two of the six rest on a bound the document has not discharged and carries as an OPEN item. The half of Round 7's M2 that was about *"found Supporting"* is fixed; the half about a summary that reads cleaner than the testing is not.

**Fix:** restore the eleven words Round 10 specified.

### M7 — Open Item 6's commissioning recommendation is correctly stated but has no owner and no acceptance criterion, and Round 10's blind read is correctly declined and then not routed to anyone

**Open Item 6, tested as asked.** The recommendation reads: *"**The read should be commissioned from a thread that wrote neither withdrawn version, and its findings applied by a thread other than the one that reads.**"* It is **correctly stated**: both withdrawn reads were written by this build thread, so *"a thread that wrote neither"* is a satisfiable and non-vacuous condition, and the second clause reproduces Round 9's recommendation accurately. The item also states the question with enough specificity to be answerable — *"the most obvious place in this world's corpus where inter-episcopal authority structure would be visible among clergy other than the two anchor figures,"* bearing on Candidate 5's Repetition and Persistence.

**It is not actionable as it stands**, for two reasons. It names **no commissioner** — Doc_04 cannot commission a thread, and the item does not route the request to the project lead, who is the only party who can. And it names **no acceptance criterion**: it does not say what the read must produce (an artifact? a Registry amendment? a finding against a named test?) or what would count as bearing on Persistence, so a compliant independent thread could not tell when it had finished. A third read that comes back with the wrong shape is how the first two went wrong.

**The same gap applies to Round 10's blind read.** The pass correctly declines it (CLEAN 7) and then records nothing about who should run it, when, or what happens to the result — and the Escalation check names three governance items without adding it. The one check Round 10 said would settle adequacy is declined into silence.

**Fix:** add an owner and a deliverable to Open Item 6 (*"commissioning is the project lead's; the read should produce a dated artifact in `Review-Artifacts/` answering, against the vendored Migne file by file line, whether the acts evidence inter-episcopal authority structure among clergy other than Cyprian and Augustine"*), and record the blind read as a named, unrun step in the Disposition rather than only in a Decision Log paragraph.

---

## LOW

### L1 — Appendix §2 still cites file line 121764 for a phrase that sits at 121768; my source read confirms the error and also confirms the attribution

Round 10's L1, declared not addressed and not addressed. Line 35: *"act 158 (file line **121764**) is Augustine's subscription to the delegation's mandate, ***mandatum suscepi et subscripsi***."* At source, 121764 is the act header; the formula is at **121768**. Doc_04's own Open Item 6 cites 121764 for *act 158* and is right. **Fix:** *"act 158 (act header at file line 121764, its subscription formula at 121768)."*

### L2 — Round 9's L1 / Round 10's L5 live: the Primary definition is still quoted three sentences of four, without an ellipsis

Line 99 closes the quotation before CF V7.4 ¶305's fourth sentence, *"They pass all or nearly all gravity tests with strong confidence."* The omission runs in the document's favour, which is why it is LOW, and it is the one remaining spliced quotation in a document corrected three times for spliced quotations.

### L3 — Round 9's C2 / Round 10's L6 live: Doc_01 §8 item 7 is still quoted with two silently altered verbs

Doc_04 line 7 has *"**generate**… and **state** explicitly whether"*; Doc_01 line 180 has *"**generates**… and **states** explicitly whether."* Two verbs changed inside quotation marks, unmarked, in the sentence that states this document's own governing instruction.

### L4 — Round 9's L6 / Round 10's L8 live: *"has not been validly read"* still understates against row 65's *"not yet drawn on by it"*

Lines 90 and 94. The Registry's formulation is the stronger, and it is the one row 65 will be read against when the reconciliation at H3 is made.

### L5 — Round 10's L4 live: appendix §5 still gives paragraph 200 with no counting convention, against Round 9's 199

The single most-verified claim in this build's record is cited by two artifacts with two different paragraph numbers for the same sentence, and neither states whether it counts all `w:p` elements or only non-empty ones. **Fix:** *"paragraph 200 on a 1-based count of all `w:p` elements (paragraph 199 as cited at `Doc04_Round9_Review.md`)."*

### L6 — Round 10's L2 and L3 live: appendix §2.1's *"~45%"* and *"two missed acts"* are still the withdrawn read's figures, not Round 5's

Round 5's M3 gives *"roughly forty per cent"*; Round 5's M4 establishes one missed act, not two. In an entry whose stated authority is Round 5, the figures should be Round 5's.

### L7 — Round 9's L3/L4/L5 live: the *Gesta* artifact is untouched

`Doc04_Gesta_Targeted_Read_2026-09-14.md` still carries the three defects Round 9 found. It is the artifact any commissioned third read will open first. Declared not addressed and consistent with that declaration; recorded because Open Item 6's fix (M7) should reach it.

### L8 — The appendix's §1 heading now reads *"all five superseded"* while every entry under it reads *"Withdrawn"*, and the sixth basis is no longer counted anywhere

Round 10's M1 is closed as arithmetic — §§1.1–1.5 are five and the heading says five. Two residues. The heading's verb (*superseded*) differs from all five entries' verb (*Withdrawn*), in a file whose function is precise status vocabulary. And Round 10's reading — that the ruling is a **sixth** basis, recorded under *"Current"* at line 23 — is now invisible: the heading counts five bases where six have been held. Doc_04 line 105 sidesteps it entirely (*"Earlier bases … have been superseded"*), which is safe but drops the count a reader of Open Item 8 would want.

### L9 — The `[SUPERSEDED]` marker at Decision Log line 750 points at the seventh entry for the current classification; the seventh entry does not state it

*"See the seventh entry below."* The seventh entry is the mechanical-pass entry; it reports that §4's cell *"now records the ruling"* but nowhere states the classification or its basis. The entry that states the ruling is the **first** 2026-09-14 entry (line 640). Round 10's H2 fix asked for a repoint to the sixth entry **and to appendix §1.5**; neither target was used. **Fix:** *"See the 2026-09-14 (first) entry and `Doc_04_Superseded_Claims.md` §1.5."*

### L10 — Round 10's C1 residue: §4's Candidate 5 cell still carries two clauses where the other seven carry a bolded label alone

Reduced from three sentences to one sentence plus a bolded label, which is most of the fix. The second clause (*"This document's six-test profile for the candidate is narrow"*) restates the Six-Test cell two columns to its left in the same row.

---

## COSMETIC

### C1 — Round 10's C2 live: appendix line 33's literal `*` inside `` `mandav*` `` still leaves an odd single-asterisk count on that line

Renders correctly. Recorded because the parity sweep flags it and the next one will too.

### C2 — Round 10's C3 live: appendix §4's third entry still makes a live positive attribution in a file whose line 7 says nothing in it is a live claim

*"It belongs to Doc_01 §4 and §5 and Doc_03's 'communion' entry."* Line 7's carve-out now names act 158 only. Related to M1 — there are three live claims in that file, not one.

### C3 — §8's *"Mechanical pass"* row carries no artifact and no result where the *"Restructure pass"* row directly above it carries both

The Restructure row reads `Doc_04_Superseded_Claims.md` / *"Correction history extracted"*; the Mechanical pass row reads `—` / `—`, matching the older fix-pass rows. Both conventions are Template §9-compliant; having both in adjacent rows is not a convention.

---

## Verification table — Round 10's 31 findings at `619cca3c`

*Fixed* means the defect is gone and the claim it was about is stated correctly. *Fixed differently* means the pass chose another route to a correct result. *Half* means one limb closed and one live.

| Finding | Round 10's claim | Status at HEAD |
|---|---|---|
| H1 | §4 cell carries the withdrawn ambiguous-results basis | **FIXED** — all four limbs; `ambiguous` ×0 in Doc_04 |
| H2 | Same basis live at four Decision Log sites | **FIXED at all four; a fifth site missed by the list — H4** |
| H3 | Open Item 8 asserts a premise the extraction deleted | **HALF — the falsity is gone; the exclusion is still not a live claim (M1)** |
| H4 | §5/§6: third vocabulary, *"tested in full and found Supporting"*, *"fully tested"* | **FIXED** at all three sites; one qualifier dropped (M6) |
| H5 | Appendix claims completeness it lacks; §8 points at it for a disclaimed record | **NOT FIXED and worsened — H2**; the §8 pointer half is fixed |
| M1 | §1 heading miscounts; Doc_04 repeats it | **FIXED differently** (L8 residue) |
| M2 | §1.3 attributed to Round 8; it is Round 7's H8 | **FIXED** — re-derived at `Doc04_Round7_Review.md` line 195 |
| M3 | Six of seven §4 entries carry no round attribution | **NOT FIXED, reported fixed — M4** |
| M4 | Restructure pass not logged in §8 | **FIXED** — three rows added, all accurate |
| M5 | Round 3's L6 second limb deleted with no destination | **FIXED** — restored, accurate against R3 L6 and R4's verification |
| M6 | *"neither established nor refuted"* symmetry lost | **FIXED** — restored verbatim at line 99 |
| M7 | Round 8's H8 disclosure narrowed | **FIXED** — restored in the half Round 9 endorsed |
| M8 | Appendix line 7 false | **HALF** — act 158 carved out; the Tensional case is not (M1) |
| M9 | Sixth entry carries no escalation check | **LIVE and widened — M2** |
| M10 | Companion block certifies row 65 unused while an item uses it | **FIXED** |
| M11 | Row 65 vs act 158 unreconciled; *"the Registry has the better of it"* | **ADJUDICATED AT SOURCE AND REVERSED — see below; propagated into the record as stated — H3** |
| L1 | Appendix reintroduces the 121764 line number | **LIVE — L1** |
| L2 | *"~45%"* is the withdrawn read's figure | **LIVE — L6** |
| L3 | *"two missed acts"* overstates Round 5 | **LIVE — L6** |
| L4 | Paragraph 200 vs 199, no convention stated | **LIVE — L5** |
| L5 | Primary definition three sentences of four | **LIVE — L2** |
| L6 | Item 7's altered verbs | **LIVE — L3** |
| L7 | §1.2 vs line 91 contradiction relocated, not resolved | **LIVE and aggravated — M1** |
| L8 | *"not validly read"* understates row 65 | **LIVE — L4** |
| L9 | *"revisit at Doc_05"* mechanism, at §4 | **FIXED** by the H1 fix |
| L10 | Character counts labelled bytes | **LIVE** — the sixth entry is untouched |
| L11 | *"42% → under 5%"* not reproducible | **LIVE** — the sixth entry is untouched |
| L12 | Candidate 2's Dependency negation dropped | **LIVE** — not a defect, a reduced guard |
| C1 | §4 cell a three-sentence argument | **SUBSTANTIALLY FIXED — L10 residue** |
| C2 | Appendix line 33 asterisk | **LIVE — C1** |
| C3 | §4 entry 3 a live claim in a no-live-claims file | **LIVE — C2** |

**What remains live across Rounds 5–10, stated as a list rather than a count.** Fixed by this pass: R5 H1–H4, H5–H7/M3/M4/M6/L1–L5 (mooted at withdrawal), M5, M8, L8 (declined and logged); R6 H1, H2, H6, H7, H8, M12; R7 H1–H10 including M2; R8 H1 at the log (four of five sites), H2, H3, H4, H5, H7, H8; R9 H1, H2, H3, H5, H6, H7, H8, H9, H10, M2, M3, M5, M6, M9, M10, M15, L2 in Doc_04, L7; R10 H1, H4, M1, M2, M4, M5, M6, M7, M10, L9.
**Still live:** R6 M9 (recast — see the adjudication); R8 H1(d) at line 97; R9 H4 (and its second premise now expressly disclaimed rather than restored); R9 M1-residue, M8, M11, M12, L1-residue, L3, L4, L5, L6, L8; R10 H3-half, H5, M3, M8-half, M9, M11, L1–L8, L10–L12, C1–C3; plus the four HIGH and four MEDIUM findings above that are new or newly created.
**Mooted by deletion rather than fixed**, and not counted as closed: R6 H3–H5/M1–M8/L3/L4/L7; R9 M4, M5, M7, M13, M14, C1, C3.

---

## Adjudication at source — `Source_Registry.md` row 65 versus the act-158 diagnosis

This is the question Round 10 raised as M11 and as its second unresolved tension, that Round 6's M9 and Round 9's M11 raised before it, and that the mechanical pass carried forward in the terms Round 10 gave it. It bears on the single fact `Doc_04_Gravity_Discovery.md` says it relies on. I opened both records and the file.

**The two statements.**

Row 65 (`Source_Registry.md` line 83, Verification Note): *"**Act 158 is the weakest of the set** — a genuine act in which Augustine speaks, but it **truncates at `158. Augustinus episcop`** and **carries none of the formula the others share**, so it does not support a claim about the recorded form."*

Doc_04 §7 Open Item 6: *"One narrow finding survives and is relied on here: act 158 (file line 121764) is Augustine's subscription to the delegation's mandate, not a debate speech."* Appendix §2 adds the formula: *"…**mandatum suscepi et subscripsi**, not a debate speech — which diagnoses an anomaly `Source_Registry.md` row 65 has recorded since Round 28 without explaining."*

**What the file shows.** `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`, read from the page header at line 121727 through act 159 at 121790. The relevant run, with OCR normalized and normalization marked as such:

```
121756   l.")7.  PtUUamt tpiucpit dixii            → 157. Petilianus episcopus dixit
121764   158.  Augustinus  episcop                 → 158. Augustinus episcop[us …]
121765   Miin ' ribagiai ooiiktiluiue priEsente    → [… Car]thagini constitutus, praesente
121767   riro < i.in .niiio iribuno el nourio Marcdliuo
                                                   → viro c[larissimo] tribuno et notario Marcellino
121768   mendalum ·usccpi fll nibacripsj           → mandatum suscepi et subscripsi
121790   139. PeiHktnat epitcopuÂ» dixit           → 159. Petilianus episcopus dixit
```

**Row 65's factual observation is exactly right.** Line 121764 reads `158.  Augustinus  episcop` and stops. It does not carry the speech formula. I verified the contrast against every other Augustine act the volume yields to a name search in the *Gesta* span: **act 50 at 126796, act 53 at 126874, act 160 at 128393, act 187 at 128716, act 201 at 129009** each read *"N. Augustinus episcopus Ecclesiae catholicae dixit."* Act 158 alone has no `Ecclesiae catholicae` and no `dixit`. Row 65's conclusion — that act 158 *"does not support a claim about the recorded form"*, i.e. should not be counted as evidence for the recorded speech formula — follows, and is correct.

**Doc_04's diagnosis is also right, and it is the explanation of row 65's observation.** Three independent grounds:

1. **The formula at 121765–121768 is a subscription, and it is the standard one.** The same page carries three parallel instances, each attaching the identical clause chain to the bishop named immediately before it: **Adeodatus** at 121736–121740 (*"…coram viro clarissimo tribuno et notario Marcellino suprascripta mandavi et subscripsi Carthagine"*), **Vincentius** at 121772–121775 (*"…Ecclesiae cath[olicae] Carthagini constitutus, prae[sente]… notario Marcellino hoc mandatum [suscepi et] subscripsi"*), and the **bishop of Constantina** at 121784–121787 (*"…Carthagini constitutus, praesente viro clarissimo tribuno et notario [Mar]cellino hoc mandatum suscepi et subscripsi"*). Act 158's text is that formula, clause for clause.
2. **No other name intervenes.** The only proper noun between the act header and the formula is **Marcellinus**, and he is not a candidate subscriber — he is the tribune and notary *before whom* the subscription is made, a fixed element of the formula itself in all four instances. The first-person *suscepi et subscripsi* requires a named subscriber and the only one available is the Augustinus at 121764.
3. **The debate/subscription distinction is visible in the numbering itself.** 157 and 159 are Petilianus *dixit*; 158 is the recitation of a subscription, followed by *"Quo recitato, idem dixit"* — the formula that punctuates every subscription on this page. The section is the reading-out of the mandate's subscriptions with the Donatists interjecting, not an exchange of speeches.

**Where Round 10's adjudication went wrong, specifically.** Round 10 reports: *"The mandatum formula is at line 121768, four lines below, with three intervening lines naming Marcellinus the tribune. Whether those four lines belong to act 158 is the whole question."* It read the intervening lines as a possible break. **They are the middle of the formula.** `Carthagini constitutus, praesente viro clarissimo tribuno et notario Marcellino` is the connective tissue of the subscription clause, present verbatim in the two subscriptions that follow on the same page and in the one that precedes it. Round 10 was rightly alert to the two-column hazard that sank the second withdrawn read — but the test for that hazard is whether the candidate lines match the column's own running formula, and here they match it three times over.

**Adjudication.**

- **Doc_04 and appendix §2 are correct at source.** The surviving datum holds. It is, on this check, the only claim in this build's *Gesta* history to survive an at-source audit by a thread that did not make it.
- **Row 65's factual observation is correct at source.** Nothing in it needs withdrawing.
- **There is no conflict between them.** They are the same observation from two sides: row 65 records that act 158 lacks the speech formula; Doc_04 says why — because it is not a speech. Appendix §2's characterisation, *"which diagnoses an anomaly row 65 has recorded since Round 28 without explaining,"* is accurate.
- **Round 10's M11 verdict — *"the Registry has the better of it on the evidence I opened"* — does not hold**, and the pass's propagation of it into the Decision Log is H3 above.
- **The one genuine residue is a single loose clause in row 65**, and it is what makes the pair *look* contradictory: row 65 calls act 158 *"a genuine act in which Augustine speaks"* and includes it in a count of *"fourteen numbered acts in which Augustine speaks"* while stating in the same sentence that it carries none of the speech formula. That set mixes two kinds of act.
- **Doc_04's own residue is that it asserts the four-line attribution without argument.** The attribution is sound; the argument for it exists nowhere in the world folder, in a build where two reads of this file were withdrawn for misreading exactly this page's column structure. A claim of this provenance should carry its grounds.

**Recommended disposition — an amendment, not an escalation.** *(a)* Row 65: append *"Act 158 is a subscription to the mandate, not a debate speech — hence the absence of the speech formula; the count of fourteen therefore mixes two kinds of act and the floor for speech-form acts is thirteen."* This is a Registry row and belongs to that document's own review. *(b)* Doc_04 Open Item 6: add the grounds in one clause — *"the act header at 121764 continues to the subscription formula at 121768, the same clause chain the parallel subscriptions at 121736–40, 121772–75 and 121784–87 carry, with no intervening speaker."* *(c)* Strike the row 65 / act 158 item from the Decision Log's unresolved-tensions count and record the reversal.

---

## Is Doc_04 adequate to proceed to Doc_05?

**My judgement: yes, on its substance — and I would not hold Doc_05 for a twelfth review round. Two sentences in Doc_04 should be corrected in the same commit that opens Doc_05, and I have written both out at H1 so that no round is needed to specify them.**

**What makes it adequate, tested rather than assumed.** A Doc_05 builder needs four things from a Doc_04: the gravities, their test results, their classifications, and what is still open. All four are now consistent everywhere they are stated.

- **The classification reads identically at every site that states it** — Status line, §3 line 101, §4 line 162, §5 line 186, §5 line 188, Open Item 2 and Open Item 7: *Supporting, on the project lead's ruling of 2026-09-14*. Eleven rounds have been about exactly this and it is the first time it is true. The withdrawn ambiguous-results basis occurs **zero times** in Doc_04.
- **The test results read identically at §3, §4 and §5** — four narrow passes, Formation not clearly passing, Persistence not passing at world level — with the third vocabulary gone and no site now claiming the axis was tested in full or found Supporting on this document's own evidence.
- **The structure is sound**: 28 symmetric matrix pairs, every §3 bullet agreeing with its row, three uniform tables, full parity, Template §§4, 5, 6, 7 and 9 satisfied.
- **The open questions are stated honestly and travel**: Open Item 1 carries both Cross-Check divergences; Open Item 6 carries the undischarged search bound and is unprejudiced; Open Item 8 carries the one substantive finding the document concedes it has not run, and now states its own premises accurately rather than falsely.
- **The one fact the document says it relies on is true at source.** I checked it independently and it holds. That was the largest unverified load-bearing item in the build and it is no longer unverified.
- **Seven of eight candidates have not been in contention since Round 4.** Nothing in eleven rounds has been about whether this world's gravities were correctly found.

**What blocks it, precisely, and whether it is review-shaped.** My four HIGH findings sort into two classes, and only one class touches Doc_04.

*In Doc_04:* **H1 alone.** Two sentences that misstate the document's own review state. A Doc_05 builder reading line 3 is told the review record stops at Round 9 and will not open Round 10. That is a real defect and it should not go into Doc_05 uncorrected — but it is two sentences, the replacement text is written above, and it misleads about the *review record*, not about a gravity, a test, a classification or an open item. Nothing a Doc_05 builder would carry forward about this world's ecology is wrong.

*Outside Doc_04:* **H2, H3 and H4** live in the appendix and the Decision Log. H2 is a record-hygiene contradiction. H4 is one unmarked paragraph in a superseded log entry. H3 is the serious one — the record asserts that Doc_04's surviving datum is probably wrong when at source it is right — and it is serious precisely because it is *false*, which means the fix makes the position stronger, not weaker. None of the three is a reason to delay Doc_05; all three are reasons to correct the record.

**So: the blocker is review-shaped, and it has shrunk.** Round 10 called it *"four sentences wide and review-shaped"* and said not yet. It is now **two sentences wide, both inside one document, both with their replacement text already written**, and the substantive core — the classification propagating consistently out of the index table into the next step — is closed. I would let Doc_05 open on a commit that fixes H1 and, in the same commit, corrects the seventh Decision Log entry per H3.

**One reservation I will not dress up as a blocker.** Round 10's diagnosis of the *pattern* — that a document with five hand-maintained restatements of one proposition, maintained by the thread that wrote them, will diverge — is confirmed again here, in a new way. The given-list method removed the enumeration failure and produced by far the best pass in the sequence, and it still produced two new defects at sites the list could not name, because the pass's own edits created them. That is not an argument for a twelfth round; a twelfth round would find a thirteenth set. It is an argument for the two governance items Rounds 8, 9 and 10 have each asked the project lead to open, and for Round 10's blind read, which is being run separately and which I have deliberately not attempted. **My adequacy judgement stands independently of that test's outcome**: if the blind read finds §4, §5 and §6 agreeing with §3, it confirms what I found by direct comparison; if it finds a divergence I missed, that divergence will be in the self-description layer, where all four of my HIGH findings already are.

---

## CO-022 escalation assessment

**1. Representative-identity decisions — does not apply.** Nothing in this pass touches what the Representative is or says.

**2. Portfolio-level / cross-world decisions — does not apply.** The *Gesta* corpus-map assignment is applied, not decided. The Framework/Template mismatch remains routed to Imperial-Juridical-Christianity's existing System Hub item and is not re-logged. **One item to note rather than escalate:** the row 65 amendment recommended above belongs to `Source_Registry.md`, which is *returned to independent review*; it should reach that review as a finding, not be made from a Doc_04 pass.

**3. Governance / methodology — OPEN, and this round adds a fourth item.** Items (a) separating the thread that reads a source from the thread that applies the reading, (b) the record-boundary question, and (c) Round 10's addition that extraction is itself a defect surface all remain unopened. **This round adds (d): a pass that takes its site list from a review inherits that review's unverified source adjudications, and must be told which of the review's statements are findings to apply and which are conclusions to re-derive.** H3 is the instance: the pass correctly declined to design its own enumeration and then, in the same entry, adopted a source conclusion the review had reached by opening a file the pass never opened — and that conclusion was wrong. The given-list discipline is the right remedy for the enumeration failure and it needs one clause: *a review's site list is applied as given; a review's reading of a primary source is re-derived before it is recorded.* **Recorded for the project lead; not decided by this reviewer.**

**4. Unresolved tensions — OPEN, one, not two.** **(i)** The evidentiary question at §7 Open Item 6 stands: the *Gesta* has been read twice by this build thread and both reads are withdrawn, and the question cannot be closed by this thread reading it a third time. Round 9's and Round 10's recommendation — commission from an independent thread, apply from a third — remains unactioned, and Open Item 6 still names no owner (M7). **(ii) The row 65 / act 158 item is closed by this review, not carried.** It was adjudicated at source above; the two records are compatible, Doc_04's reading is the one the text supports, and what remains is a one-clause Registry amendment. **It should be removed from the Decision Log's unresolved-tensions count rather than escalated, and the record's current statement that the Registry has the better of it should be corrected (H3).** Closing a tension by opening the file is the outcome the category exists to reach.

---

*End of Round 11 review. Simulated review — informational only, not an Article 31 substitute.*
