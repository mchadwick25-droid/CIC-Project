# Unused Assigned Corpus Finding (Peter / Theognostus / Pierus) — Round 7 Independent Adversarial Review (Final Confirmation Round)

**Simulated review — informational only, not an Article 31 substitute.**

World: Alexandria (Catechetical-School) Formation World · Reviewed: `Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md` (Round 7 draft, revised after Rounds 1–6) and the **OG-6** entry in `Open_Gaps_Tracking.md`
Reviewer role: independent adversarial, final confirmation round. Did not author the finding document, any of the six prior review artifacts, the discovery pass, or any Doc_04 round. Brief, tightly scoped: verify Round 6's two substantial findings (N6-1, N6-2) are fixed against `git diff 3e6c54b..bf71ffb` **and against disk**, and verify N6-1's fix is **structural** rather than a fourth hand-correction; verify by grep that **no hand-maintained round count or status restatement survives outside the header**, which is the whole point of that structural fix; verify the header is internally consistent and accurate against the six artifacts on disk; check §11's new entry for overstatement; sweep for new errors; confirm discipline and footprint; answer the headline.
Method: `git log`; `git diff 3e6c54b..bf71ffb` read hunk by hunk; `git show 3e6c54b:…` for the pre-revision text of both graded loci; `git diff --stat b50302d^..bf71ffb` and `git status --porcelain` for the pass's total footprint. All six review artifacts opened and their own verdict/count lines and cosmetic enumerations extracted programmatically. Pattern greps run over the finding document and OG-6 for `adversarial round` / `monotonic` / `trajectory` / `consecutive` / `Round N draft` / `all (three|four|five|six)` / `not cleared` / `no disposition` / `every round`. Independently re-run: `grep -c "Theognostus"` against the vendored `npnf201`; `grep -rin peter records/alx/` and `grep -ric "peter of alexandria" records/alx/`; `find -iname "*Gravity_Index*"` repo-wide; `records/worlds.yaml` pin. `Doc_04_Gravity_Discovery.md` read in place: heading inventory, §0's Theognostus sentence, §3.6's T1 pole rule and T4 interior verdict, and **§6's Interaction Matrix in full**, plus a whole-file grep for any `T1↔T4` pairing. All fifteen cosmetic loci carried from Round 6 string-checked at their stated positions. Round 6's artifact read in full before the document.
Date: 2026-09-09

---

## VERDICT: CLEARED

**Both of Round 6's substantial findings are fixed. N6-1 is fixed structurally, exactly as Round 6 asked. I found no new substantial finding, and I could not open any route to a Doc_04 classification change. The headline is correct for the seventh time.**

I want to be plain about the shape of this verdict, because it is the first CLEARED in seven rounds and it should be legible on its own terms.

I did not go looking for a reason to withhold it. I went looking for the specific thing this round was convened to test — whether removing the last hand-maintained count actually removed the failure mode, or merely relocated it — and the answer is that it removed it from the finding document entirely. The count now exists in exactly one place, the header. Everything downstream of it either points at that header, points at a `Round*_Review.md` glob, or quotes the old text explicitly as history inside §11 and §10's disclosure. That is the correct structural answer to a defect that recurred in five of six rounds, and it works.

I verified the substantive claims rather than inheriting them. Theognostus appears **0 times** in the vendored Eusebius. `records/alx/` holds **zero** Peter-of-Alexandria records, and the two `peter` greps are both the anf09 filename in an `edition:` field. Doc_04 §6's Interaction Matrix contains exactly the nine relationships §5.3 enumerates and **no T1↔T4 cell** — I read §6 in full and grepped the whole file; the single `T1–T4` string in Doc_04 is a §2 candidate-table row label meaning "T1 through T4," not a matrix cell. No Alexandria `Gravity_Index.xlsx` exists in the repository. The T1 pole-separation rule and the T4 Inferential-Thin interior verdict are verbatim as quoted. The document's evidence work is, as six reviewers before me have found, correct.

**Remaining defects: cosmetic only, 19 of them, 15 carried unrepaired from Round 6 and 4 new or newly-escalated.** None of them misleads a reader about the evidence, a conclusion, a scope boundary, or the document's standing. §H lists all of them for the record, and flags two that must be edited **in the same commit that records this clearance**, because clearance is the event that falsifies them.

Counts this round: **0 substantial, 19 cosmetic.** Substantial-finding trajectory: **8 → 8 → 4 → 3 → 1 → 2 → 0.** The disposition (§9 Option B, escalated to the project lead, not self-disposed) remains sound and should stand unchanged. **Clearing this document does not dispose of it.** It clears the *finding document* as an accurate, honest, well-evidenced artifact; OG-6 remains OPEN and the project lead's decision among Options A/B/C — and the separate portfolio-level decision on the fleet-wide work-granularity diff — is untouched by this verdict.

---

## A. ROUND 6'S TWO — VERIFIED AGAINST THE PATCH AND AGAINST DISK

### N6-1 — **RESOLVED, and resolved structurally.**

Round 6's charge: §10's status bullet still read *"**Four** adversarial rounds have each returned SUBSTANTIAL REVISION REQUIRED (**8 → 8 → 4 → 3**)… This is the **Round 5 draft**"* — a round behind, at the identical locus Round 4 had already graded substantial (N4-2) and Round 5 had certified fixed.

`git show 3e6c54b:…` confirms the pre-revision text verbatim. The bullet now reads (lines 704–708):

> - **Not cleared**, and **no disposition has been assigned to it** by this thread or anyone else.
>   *Round 6 drift-proofing: this bullet used to restate the round count and trajectory, and went stale in the same commit that drift-proofed the file list six lines below — the fifth consecutive round in which this document's self-description was the defect. The count now lives in exactly one place, the header, and is deliberately not repeated here.*

**This is the structural fix, not a fourth hand-correction, and the distinction is real rather than rhetorical.** Three things establish it:

1. **No number survives in the bullet.** There is no round count, no trajectory, no draft ordinal. `grep -nE "adversarial round|8 → 8|Round [0-9] draft"` over §10 returns nothing. The bullet cannot go stale on a round boundary because it no longer contains anything that changes on a round boundary.
2. **What remains is the section's actual job.** "Not cleared" and "no disposition has been assigned" are the honest negative inventory §10 exists to give. They are true today, and they change only on disposition — an event, not a round tick.
3. **The old text is preserved as disclosure, not deleted quietly.** The italic note says what the bullet used to claim and why it was wrong. This matches the practice the document established in §10's Round 2 disclosure and in §11: repair by stating what happened, not by silent overwrite. It also means the historical record survives the removal of the count, which is the thing a reader would otherwise lose.

Round 6 asked for exactly this — *"preferably by deleting the last hand-maintained count rather than by correcting it a fourth time"* — and that is what landed.

### N6-2 — **RESOLVED.**

Round 6's charge: the header's Round 5 bullet said *"**Round 3's four** all RESOLVED"* where Round 5 verified **Round 4's three**, contradicting the bullet eight lines above it (*"Of Round 3's 4: 3 resolved, 1 partial"*) and §11 (*"It found all three of Round 4's resolved"*).

The diff shows the one-line correction and nothing else in that hunk:

```
-  Round 3's four all **RESOLVED** — the first round with no partial and no fix-introduced
+  **Round 4's three** all **RESOLVED** — the first round with no partial and no fix-introduced
```

Line 22 now reads *"**Round 4's three** all **RESOLVED**."* I checked all three loci that were in contradiction: the Round 4 bullet (line 16–17, "Of Round 3's 4: **3 resolved**, 1 partial") is unchanged and correct; the Round 5 bullet is corrected; §11's Round 4 → 5 entry (line 764, "It found **all three** of Round 4's resolved") is unchanged and correct. **The three loci now agree.** Verified against Round 5's own artifact, whose brief line reads *"Verify each of Round 4's three substantial findings against `git diff a44648c..b3247c0`"* — Round 4's three is what Round 5 examined.

---

## B. DOES THE STRUCTURAL FIX HOLD? — **YES FOR THE FINDING DOCUMENT. ONE TREND RESTATEMENT SURVIVES IN OG-6, AND IT IS NOW FALSE.**

This was the load-bearing question of the round, so I ran it as a grep sweep rather than a reading impression.

### B.1 The finding document — clean

`grep -nEi "adversarial round|rounds have|monotonic|trajectory|8 → 8|all (three|four|five|six)|Round [0-9] draft|Round\*|consecutive round|not cleared|no disposition|every round"` over the whole document. Every hit resolves to one of four permitted categories:

| Hit | Category | Verdict |
|---|---|---|
| Line 5 Version line; lines 34–45 (six bullets, "All six are AI review", "Round 7 review pending", trajectory paragraph) | **The header — the single source of truth** | ✓ permitted by design |
| Line 704–708 §10 status bullet | **Disclosure passage**; carries no count | ✓ |
| Lines 716–719 §10 file list | **Glob**, plus a disclosure of the prior hand-maintained list | ✓ |
| Lines 722–730 §10 phantom-entry disclosure | **Disclosure passage** | ✓ |
| Lines 736–926 §11 entries | **Revision log**, all past-tense and frozen; explicit historical quotations of the stale text (*"still 'Four adversarial rounds… the Round 5 draft'"*, *"still 'Two adversarial rounds… the Round 3 draft'"*) | ✓ permitted |
| Line 329 §5.3 *"the fourth consecutive round to narrow this finding"* | **Frozen historical annotation** on the Round 4 correction; Rounds 5–6 did not narrow §5.3 further, so it does not tick | ✓ |
| Line 626 §8 *"a Doc_04 that cleared three adversarial rounds"* | About **Doc_04's** review history, not this document's; `Doc_04_Round1/2/3_Review.md` all exist | ✓ accurate, not drift-prone |

**`grep -c "monotonic"` over the finding document returns 0.** The header's trajectory line was rebuilt to *"**8 → 8 → 4 → 3 → 1 → 2** substantial findings, with the headline upheld at every one of six rounds"* — Round 6's c-23 ("falling monotonically" is inaccurate at the flat 8 → 8 step) was correctly absorbed, and the phrase was dropped rather than patched, which is the right instinct given that 1 → 2 would have falsified it outright.

**The header's own claim about this — *"Every hand-maintained restatement of the round count has now been removed; it lives in this header alone"* — is true as written, and I tested it rather than accepting it.** Within the finding document, no round count exists outside the header except as explicit history in §11 and §10's disclosure. That is what the sentence claims and it is what the grep shows.

### B.2 OG-6 — the count is gone, but one trend claim survived and has gone stale

OG-6's Reviews paragraph (lines 317–325) is count-free and correctly delegated, and I checked it clause by clause against disk:

- *"Every round is an artifact on disk at `Review-Artifacts/Unused_Assigned_Corpus_Finding_Round*_Review.md` — that glob… is the authoritative list"* — **true**; the glob resolves to exactly six files, Round1…Round6, no gaps and nothing extra.
- *"Each is AI review, marked 'Simulated review — informational only, not an Article 31 substitute'"* — **true**; `grep -c` returns exactly 1 in each of the six.
- *"Every round to date has returned SUBSTANTIAL REVISION REQUIRED and upheld the 'not structural' headline"* — **true as the document stands.** All six artifacts' verdict lines are SUBSTANTIAL REVISION REQUIRED and all six uphold the headline. See c-21 below: this clearance is the event that falsifies it.
- *"The finding document's header carries the current round and its status"* — **true**, and now true without the irony Round 6 had to note, since the header bullet it delegates to is corrected.
- *"The finding document is NOT cleared and carries no disposition"* — **true as the document stands.**

**But one sentence in that same paragraph is a hand-maintained characterization of the review trajectory, it sits outside the header, and it is now false:**

> `Open_Gaps_Tracking.md` line 323: *"…the substantial-finding count has **fallen monotonically round on round**."*

The sequence is 8 → 8 → 4 → 3 → 1 → **2**. It rose at Round 6. Round 6 flagged this exact phrase as **c-23** when it was merely loose (flat at 8 → 8); the author fixed it in the header and did not carry the fix one file over into OG-6, where the trajectory then went from loose to wrong.

**I considered elevating this to substantial and decided against it. The reasoning belongs on the record:**

*For elevation.* It is a false factual statement about the review record, it sits in the escalation ledger rather than in the document's own internals, and Round 5 was explicit that OG-6 defects carry *more* weight than §10 defects "since §10 is internal and OG-6 is the escalation." It is also, mildly, an error in the document's own favour, and this review series has been strictest about exactly that direction of error.

*Against elevation, and decisive.* The withholding test is whether a defect misleads a reader about the evidence, a conclusion, a scope boundary, or the document's status. Every load-bearing fact in the surrounding paragraph is correct: how many rounds have run (delegated to a glob that resolves correctly), what every round returned, that the headline was upheld each time, that the document is NOT cleared, and that it carries no disposition. What is wrong is an adjective describing the *shape* of a trend whose actual values are printed accurately in the header the same paragraph points to. No disposition decision, no reading of the evidence, and no assessment of how much scrutiny this finding has had turns on it. And Round 6 graded this identical sentence cosmetic; the only change since is one of degree, and grading it substantial now would apply a *harsher* standard to a *smaller* residue than the standard applied when it was first found. That would be manufacturing a round, not conducting one.

**It is c-25, it is the highest-priority cosmetic in this review, and it must be fixed in the same commit that records this clearance** — alongside c-21, which the same commit also falsifies.

### B.3 Verdict on B

**The structural fix holds where it was made.** The finding document carries no hand-maintained round count outside its header. What survived is not a count but a trend adjective, in a different file, in a paragraph that Round 5's finding had already reached into once — and it survived precisely because the author fixed the header instance of c-23 without grepping for siblings. That is the residual lesson: the drift-proofing removed the *counts* and left the *characterizations*, and characterizations drift too.

---

## C. THE HEADER — CHECKED LINE BY LINE AGAINST THE SIX ARTIFACTS ON DISK

I extracted each artifact's own verdict line and count line programmatically and enumerated its cosmetic bullets, rather than reading the header and looking for agreement.

| Header claim | Artifact on disk | Verdict |
|---|---|---|
| **Version:** "Round 7 draft (revised after six adversarial rounds)" | six artifacts, Round1…Round6 | ✓ |
| **R1** — SUBSTANTIAL, 8 + 8, headline upheld | *"Counts this round: **8 substantial, 8 cosmetic**"*; §"the 'not structural' conclusion is CORRECT" | ✓ |
| **R2** — SUBSTANTIAL, 8 + 10; ran C4 itself; of R1's 8: 4 resolved / 3 partial (2 new errors) / 1 not resolved | *"**8 substantial, 10 cosmetic**"*; §11 and R2 §"Accurate self-report" corroborate the 4/3/1 split | ✓ |
| **R3** — SUBSTANTIAL, 4 + 12; ran C3 Dependency, T2 and the generation step; of R2's 8: 7 resolved, 1 partial | *"**4 substantial, 12 cosmetic**"*; the route claims verbatim in R3 | ✓ on counts and routes; the "7 resolved" is Round 4's carried **c-14** (R3's own tally is three-category: "Six of the eight are cleanly resolved") — cosmetic, unchanged |
| **R4** — SUBSTANTIAL, 3 + 15; ran the Tensional generation step; "cannot find any route" | *"**3 substantial, 14 cosmetic**"* on its summary line, but its §F **enumerates fifteen** (c-1…c-15); the "cannot find any route" statement is verbatim in R4 | ✓ — the header's 15 matches the enumerated list; R4's own summary line miscounts itself. See c-26 |
| **R5** — SUBSTANTIAL, 1 + 19; **Round 4's three all RESOLVED**; verified Eusebius-independence at both ends; ran record-confidence and npnf214 `div2 17.5` | *"**1 substantial, 19 cosmetic**"*; brief line names "Round 4's three"; §E carries both further routes and the second-volume confirmation | ✓ — **N6-2 fixed** |
| **R6** — SUBSTANTIAL, 2 + 16; headline a sixth time; R5's finding RESOLVED; both materially-misleading cosmetics fixed correctly; read Canon XIV with commentaries; T1×T4 survives without Fragment I, redundantly carried by Canons IX, X, XIII, **Canon X** the stronger anchor; two findings again one-line self-description, one a regression at the locus Round 4 graded substantial | *"**2 substantial, 16 cosmetic**"*; §C verbatim on Canon XIV/Balsamon, the IX/X/XIII redundancy and Canon X as cleaner anchor (its c-22); §E N6-1 names the Round 4 N4-2 precedent | ✓ on every clause |
| **"All six are AI review, each marked… 'Simulated review — informational only, not an Article 31 substitute'"** | `grep -c` returns exactly **1** in each of the six | ✓ |
| **Trajectory 8 → 8 → 4 → 3 → 1 → 2**, headline upheld at every one of six rounds, each round narrowing | matches the six substantial counts and the six headline verdicts | ✓ |
| **Self-description pattern:** "Round 1's header, Round 2's phantom ledger entry, Round 4's §10, Round 5's OG-6 paragraph, and Round 6's §10 status bullet plus a regression I introduced" | five occurrences, consistent with §11's "five of six rounds" | ✓ accurate, and it does **not** claim they were consecutive |
| **"Every hand-maintained restatement of the round count has now been removed; it lives in this header alone"** | grep-tested in §B.1 | ✓ true of the finding document |
| **"Round 7 review pending — this document is NOT cleared, and no disposition has been assigned to it"** | true as the document stands; this artifact is the event that ends the pending state | ✓ |
| **Status line** — escalated, not self-disposed; no Doc_01–09, no `records/alx/`, no corpus-map, no compiled package changed; only `Open_Gaps_Tracking.md` modified | verified on disk in §F | ✓ |

**Internal consistency:** the Round 4 bullet ("Of Round 3's 4: 3 resolved, 1 partial"), the Round 5 bullet ("Round 4's three all RESOLVED") and §11's Round 4 → 5 entry now agree. I found **no self-contradiction anywhere in the header**.

---

## D. §11's ROUND 6 → ROUND 7 ENTRY — **DOES NOT OVERSTATE. EVERY CLAIM LANDED.**

Mapped claim by claim against `git diff 3e6c54b..bf71ffb` and against Round 6's artifact.

| §11 claim | Verified |
|---|---|
| Round 6 returned SUBSTANTIAL, 2 substantial + 16 cosmetic | ✓ Round 6's own count line |
| upheld the headline a sixth time | ✓ Round 6 §G |
| confirmed Round 5's single finding resolved | ✓ Round 6 §A: "N5-1 — **RESOLVED**" |
| both materially-misleading cosmetics fixed correctly | ✓ Round 6 §B, which re-ran the grep and re-read Fragment I |
| read Canon XIV with Balsamon and Zonaras; T1×T4 survives the loss of Fragment I; redundantly carried by Canons IX, X, XIII; **Canon X** the cleaner anchor for episcopal authority running *against* confessor prestige | ✓ Round 6 §C verbatim, including the "permanent bar from office" gloss |
| "Both findings accepted" | ✓ no dispute appears anywhere in the revision |
| Item 1: §10's bullet stale in the same commit that drift-proofed the list six lines below; Round 4 had graded the identical defect at the identical locus substantial; fixed **structurally, not again by hand**; "the count now has exactly one home, the header" | ✓ every clause; the structural claim is the one that could have been overstated and it is **true on disk** (§A above) |
| Item 2: header's Round 5 bullet said "Round 3's four all RESOLVED"; Round 5 verified Round 4's three; contradicted a line eight rows above and §11; introduced in the bullet added to close Round 5's finding; corrected | ✓ every clause, including "eight rows above" (lines 16–17 vs 22) |
| Closing: "five of six rounds found this document's self-description wrong while its evidence work held"; the structural response deleted §10's file list (R5), OG-6's reviews paragraph (R5), and now §10's status bullet | ✓ five occurrences (R1, R2, R4, R5, R6); all three deletions verified on disk |

**Two things §11 correctly does *not* claim.** It does not claim any cosmetics were applied — none were, and I string-checked all fifteen carried loci (§H). And it does not claim the document is now clean, correct in all respects, or ready to clear. **No phantom claim, third consecutive round.** The one thing it still omits is disclosure that the cosmetics were carried undone, which is carried **c-19**.

One nuance worth naming, because it is the only place the entry could be read as slightly generous to itself: the closing paragraph says the structural response *"leav[es] a single source of truth in the header."* Within the finding document that is exactly right. It is not quite right across the escalation pair, because OG-6 still characterizes the trajectory independently (c-25). The sentence is scoped to "this document," so it is not false — but a reader could take it as a claim about the pair. Cosmetic, recorded as **c-27**.

---

## E. NEW-ERROR SWEEP — **NO SUBSTANTIAL FINDING**

The revision touched seven loci: the Version line, the Round 5 bullet, a new Round 6 bullet, the "All five/six are AI review" line, the trajectory paragraph, §10's status bullet, and §11 (new entry plus the "(this revision)" tag moved off the Round 5 → 6 heading). I read every new or changed line for fresh error.

- **Version line, "All six" line, Round 6 bullet, trajectory paragraph** — all verified accurate in §C. The Round 6 bullet is the longest new passage and I checked each of its six clauses against Round 6's artifact; all six hold, including the two that could easily have been overstated ("Canon X the stronger anchor" — Round 6's c-22 says exactly that, offered as strengthening; "a regression at the locus Round 4 had already graded substantial" — Round 6 §E item 2 makes exactly that argument).
- **§10 status bullet** — no fresh factual error. It contains one carried inaccuracy: *"the **fifth consecutive** round in which this document's self-description was the defect."* The occurrences are Rounds 1, 2, 4, 5, 6 — five of them, but **not consecutive**: Round 3's four findings were all in the argument. Round 6 flagged the same word in its c-24 (then "four consecutive") and it has been reproduced with the number incremented. The count "fifth" is right; "consecutive" is not. §11 gets it right eight lines later with *"five of six rounds,"* so the document is more accurate in the log than in §10. Cosmetic, **c-24 carried and reproduced**.
- **§11's new entry** — verified in §D, no overstatement.
- **No regression of anything Round 6 certified.** I re-checked both loci Round 6 verified from the sources: §3.1's grep control note still describes the two `edition:`-field filename hits correctly (I re-ran both greps: two hits, both the anf09 filename; zero for `peter of alexandria`), and §5.3's corrected Fragment I gloss (rival bishop of Lycopolis, jurisdictional complaint, martyrs' letter on Peter's side, prison as location only) is unchanged. Neither was disturbed by this revision.
- **No new claim was added to the body.** The diff touches nothing in §1–§9. The evidence, the argument, the five defects, the route tests, the root cause and the three options are byte-identical to the draft Round 6 cleared on substance.

The only new-text inaccuracies I found are the two adjectives already named: **"consecutive"** in §10 (c-24, carried) and **"monotonically"** in OG-6 (c-25, newly false). Neither is a new substantial finding.

---

## F. DISCIPLINE COMPLIANCE

| Requirement | Result |
|---|---|
| Declines to self-dispose | **PASS, verified on disk.** `git diff --stat b50302d^..bf71ffb`: the pass's entire footprint across seven commits is **eight files** — the finding document, `Open_Gaps_Tracking.md`, and six review artifacts, 2,288 insertions, **zero deletions of anything outside those files**. `git status --porcelain` is empty, so what I read is what is committed. Escalation categories 2 and 4 correctly identified; OG-6's *"Status: OPEN — awaiting project-lead disposition"* stands unchanged. |
| No `records/alx/` edit | **PASS.** `git diff --name-only b50302d^..bf71ffb | grep records/` returns nothing. |
| No Doc_01–Doc_09 edit | **PASS.** No construction document appears in the footprint. `Doc_04_Gravity_Discovery.md` is untouched — I read it in place this round and it still carries the §0 Theognostus sentence, the §6 matrix with no T1↔T4 cell, and the §8 workbook citation that §5.5 reports. |
| No corpus-map edit | **PASS.** `cic/corpus-map/alexandria-catechetical.yaml` untouched; the three overstated headship notes are still reported in §4 and §10 rather than corrected — the right call for a thread that has escalated. |
| No compile; `worlds.yaml` untouched | **PASS.** `records/worlds.yaml` line 41 still pins `packages/alx/2026-09-04T16-41-49Z`. No M3 run. No `Gravity_Index.xlsx` was created to make §5.5 go away — `find -iname "*Gravity_Index*"` repo-wide still returns only World #1's workbook and the PAHC generator script. |
| No unverifiable project-lead attribution | **PASS.** `grep -nE "Mark\b|approved by"` over the document returns exactly one hit: §10's *"No claim that any of this was seen or approved by the project lead."* §8 cites the S6.2 declaration by date, not by person. |
| Claims no status it has not earned | **PASS — and this is the line that failed in Rounds 4, 5 and 6.** The Version line, the six round bullets, the "All six are AI review" line, the trajectory paragraph, the "Round 7 review pending / NOT cleared / no disposition" line, §10's status bullet and OG-6's status line are all accurate against disk. The document claims **less** standing than it has earned, not more, and it does so at every locus. |
| Grounded options preserved | **PASS.** Three options intact and unchanged, each with cost, precedent and a stated reason; Option B recommended; §7's portfolio decision separated out and explicitly **not run**; the recompile/re-admission question reserved as *"the project lead's, not this thread's."* |
| Accurate self-report of its own revision | **PASS, third consecutive round.** §11's new entry maps claim-for-claim onto the patch with no phantom claim and no unearned cosmetic credit. |
| Ledger entry accurate against the document | **PASS on substance.** OG-6's three-produced / two-pre-existing structure still matches §1 and §8; the route-test paragraph still distinguishes Round 3's and Round 4's generation-step candidates; the Reviews paragraph's glob and delegation are accurate. c-15 (the stale short route list at line 256 sitting above the complete one at 305) and c-25 (the "monotonically" sentence) leave it untidy and, in c-25's case, wrong on one adjective — but the entry does not misreport the finding, the defect inventory, the disposition or the status. |

---

## G. THE HEADLINE, RE-TESTED — **"NOT STRUCTURAL" IS CORRECT. SEVENTH CONFIRMATION. THERE IS NO ROUTE TO A DOC_04 CLASSIFICATION CHANGE.**

This revision changed no evidence, so I did not re-run all nine gravities from scratch. I re-tested the Doc_04 rules the finding leans on hardest, reading Doc_04 in place rather than through the document, and I asked the one question a final round should ask: is there a route that seven rounds have collectively failed to name?

- **T1 pole separation.** Doc_04 line 132, verbatim: *"A Tensional Gravity requires **two genuinely distinct poles with real population, institutional, or practice-cluster separation** (not a polarity within one person)."* The document's inversion of the discovery pass is exactly right: a single teacher-bishop-martyr would have been evidence *against* T1. §4 defends T1; it does not extend it.
- **T4's interior.** Doc_04 line 137, verbatim: *"its interior is Tier-3 hagiography / Coptic martyrology, held at **Inferential-Thin**."* Peter's canons are juridical — graded penalties, deposition, who is reckoned a confessor. They contain no martyr's interior. The Inferential-Thin verdict stands and nothing in this corpus licenses filling that silence. §5.3 concedes this in its own text.
- **T1×T4 and §6.** I read the Interaction Matrix in full. Its cells are exactly C1↔C2; C1→C3/C4/C5; C2→C3/C4/C5; C4 as super-integrator; C5↔T2; C2↔T3; T3↔C4; T4↔C2; T1↔C5 — **the nine §5.3 enumerates, with no T1↔T4 cell.** A whole-file grep for any `T1`/`T4` pairing returns one hit, line 66, which is a §2 candidate-table row labelled `T1–T4` meaning "T1 through T4" — a range, not a cell. The relationship the canons demonstrate is real and undocumented; it is an Interaction-Test deliverable gap under `cic-gravity-index`, and §6's own line correctly notes the Framework's isolated-candidate red flag does not fire because T4 carries T4↔C2. **A missing matrix cell is not a classification change**, and the document has never claimed otherwise.
- **§5.1, re-verified independently.** `grep -c "Theognostus"` against `npnf201_eusebius-church-history-life-of-constantine.xml` returns **0**. Doc_04 §0 line 39 does place "the post-Origen teachers (Heraclas, Theognostus)" as "reaching us largely through Eusebius (HIGH-risk)." The finding is correct, and its own §5.1 correctly rests it on the narrower ground (a false sourcing statement about a named figure) rather than on the two-governing-disciplines overreach Round 1 struck out.
- **§3.1, re-verified independently.** `records/alx/` returns **zero** hits for `peter of alexandria` and exactly two for `peter`, both the anf09 filename inside an `edition:` field. The absence is real.
- **§5.5, re-verified.** No Alexandria `Gravity_Index.xlsx` exists in the repository, and Doc_04 §6's opening sentence still defers full pairwise coverage to it. §5.5's consequence for §5.3 is live: if the workbook is absent, the T1↔T4 cell is documented nowhere.
- **Is there an unnamed route?** Seven rounds have now run: C3 Dependency, C4, C5 Persistence, T1 pole separation, T2, T3, T4 confidence, the Article 21 Cross-Stratum substitute, record-confidence, a second Eusebius-independent canonical text (npnf214 `div2 17.5`), and — twice, from two directions — **the generation step**, which is the only route that can produce a classification change without moving an existing candidate. Both generated candidates fail on **Dependency**, which is Doc_04 §2's own deciding test and its own precedent for Askesis. I can name no further route. The material's ceiling is set by what it is: episcopal legislation and late-mediated doctrinal excerpts, which supply *conditions* and *boundary-drawing*, never a practice-cluster with independent organising force. That ceiling is structural to the corpus, not an artefact of how the tests were run.

**§9 Option B, escalated and not self-disposed, should stand.** What remains genuinely open is not a route but **§3.5's unaudited remainder** — Alexander of Alexandria's *Epistles on the Arian Heresy* still the strongest single item in it, joined by Round 5's npnf214 finds — and that is correctly named here and declined as its own pass.

---

## H. COSMETIC FINDINGS — 19

**Fifteen carried unrepaired from Round 6.** I confirmed each by string search at its stated locus; numbering follows the established series so the carry-forward stays traceable. None was repaired this revision, and §11 correctly claims no cosmetic credit.

- **c-1.** §6.1 still prints *"the theological *centre*"* against Doc_04's "center," and still truncates the quotation without an ellipsis.
- **c-3.** §5.4 still calls *"From his demonstration that the soul was not pre-existent to the body"* a heading; the ANF heading is *"Of the Soul and Body."*
- **c-4.** §5.3 still folds **Canon IV** into *"Canons I–V — a graded penitential scale."* Canon IV is the scale's refusal, not a step on it.
- **c-7.** §2's table still says Doc_04 was *"read in full (all 9 sections)."* I counted the headings myself: **ten**, §0–§9 — and §0 is the one §5.1 turns on.
- **c-8.** §3.5's *"14 works assigned to Alexandria from anf06"* still uses "assigned" in the membership sense adjacent to `confidence: assigned` in the field sense.
- **c-9.** §6.1 and §6.2 are still filed under §6, *"The Article 21 substitute (Cross-Stratum Test),"* which neither is about.
- **c-10.** *"roughly a quarter-century earlier"* is still the outer edge of a 14–25 year range.
- **c-11.** §9 Option C still calls §5.1 *"a plain factual error"* where Doc_04 §0's sentence is a hedged collective (*"reaching us largely through Eusebius"*, of Dionysius, Heraclas and Theognostus together) — which §5.1's own body concedes by writing *"False for Theognostus."* Six rounds. This is the oldest live inaccuracy in the document and the one I would fix first among the carried set.
- **c-12.** §3.4's Canon XI sentence still has no clear subject in its first clause.
- **c-13.** §11's Round 4 → 5 entry still says the §5.3 recast was *"Propagated to the heading, §1, §8…"*; §1 was not touched and needed no touching.
- **c-14.** The header's *"Of Round 2's 8: **7 resolved**, 1 partial"* still flattens Round 3's three-category tally (*"Six of the eight are cleanly resolved"*).
- **c-15.** OG-6 still carries **two** route-test lists — the pre-Round-3 short one at line 256 and the complete one at line 305. A lead reading top-down meets the stale one first, and the one below it is now considerably better. Worth fixing whenever OG-6 is next opened, which c-21 and c-25 now require anyway.
- **c-18.** §6.2 still says *"Tested against the six tests:"* and reports three.
- **c-19.** §11 still does not disclose that the cosmetics were carried undone, against the disclosure practice the document set for itself in its Round 2 → 3 entry. No false claim is made.
- **c-20.** §5.3's *"every manifestation… passes through Eusebius"* is still warranted in the text only by the Dionysius record's *"mostly."* Round 5 put the exact warrant on the record (ANF's epistle headnotes: `HE` vii.11; vi.41/42/44; vi.46; vi.40+vii.11; vii.1/10/23); citing them would put the claim beyond a hedge. This is the one carried cosmetic that touches a load-bearing sentence, and it is a citation-strengthening, not a correction.

**c-22** (Round 6's observation that **Canon X** is the cleaner anchor for the T1×T4 sentence than Canon XIV, since XIV has the bishop *ratifying* on martyr testimony while X has him overriding confessor prestige outright) is not a defect and I record it only so it is not lost: it is a strengthening the document could adopt and has not.

**New or newly-escalated this round:**

- **c-21 (carried from Round 6, now live). MUST BE FIXED IN THE COMMIT THAT RECORDS THIS CLEARANCE.** OG-6 reads *"**Every round to date has returned SUBSTANTIAL REVISION REQUIRED** and upheld the 'not structural' headline."* It is true today. **It becomes false the moment this artifact lands on disk.** Round 6 predicted precisely this — *"it will not survive Round 7 if Round 7 clears"* — and Round 7 clears. The same paragraph's *"The finding document is NOT cleared and carries no disposition"* becomes half-false in the same instant: it remains true that no *disposition* has been assigned, and it becomes false that it is not cleared. The header's *"Round 7 review pending — this document is NOT cleared"* and §10's *"Not cleared"* bullet are the two other loci that turn over on the same event.
- **c-24 (carried and reproduced).** §10's new drift-proofing note says *"the **fifth consecutive** round in which this document's self-description was the defect"* and OG-6 line 319 still says *"drifted from disk state in **four consecutive** rounds."* The occurrences are Rounds 1, 2, 4, 5, 6 — **five, and not consecutive** (Round 3's four findings were all in the argument). OG-6's number is now also a round behind. §11 states it correctly as *"five of six rounds."* Fix both to the §11 phrasing.
- **c-25 (new, and the highest-priority cosmetic).** OG-6 line 323: *"the substantial-finding count has **fallen monotonically round on round**."* False — 1 → 2 at Round 6, and it will be false in a different direction after this round. The header's counterpart was correctly rebuilt this revision; OG-6's was not. The fix is to delete the clause, as the header's was deleted, rather than to re-characterize the trend a second time — the lesson of five rounds is that hand-maintained characterizations drift exactly as hand-maintained counts do. See §B.2 for why I graded this cosmetic rather than substantial.
- **c-26 (new, de minimis, and not the document's fault).** The header's cosmetic counts mix two conventions, because three of the six artifacts miscount their own cosmetic lists: Round 4's summary line says 14 while it enumerates 15 (the header uses 15, the enumerated figure); Round 5's says 19 while it enumerates 20; Round 6's says 16 while it enumerates 15 carried + 4 new = 19 (the header uses each artifact's stated line for Rounds 5 and 6). Every number the header prints is a number its artifact states or lists, so nothing is invented — but no single convention is applied across the six. Cosmetic counts are load-bearing for nothing; the cleanest fix is to drop them from the header and keep only the substantial counts, which are unambiguous in all six artifacts and are the numbers the trajectory line uses.
- **c-27 (new, trivial).** §11's closing sentence says the structural response leaves *"a single source of truth in the header."* True within the finding document; not quite true across the escalation pair while OG-6 still characterizes the trajectory independently (c-25). Fixing c-25 makes the sentence true as a claim about the pair.

**A structural observation, not a defect, offered for the next revision.** The drift-proofing removed every duplicated *count*. It did not remove the duplicated *cleared/pending status*, which now lives in four places: the header's "Round 7 review pending — this document is NOT cleared," §10's "Not cleared" bullet, and OG-6's "Every round to date has returned SUBSTANTIAL REVISION REQUIRED" plus "The finding document is NOT cleared and carries no disposition." All four are accurate and mutually consistent today, which is why this is not a finding. But they all turn over on a single event — this one — and the same delegation that fixed the counts would fix them: let the header state the status, and let §10 and OG-6 point at it, exactly as OG-6 already does for the round number.

---

## I. SUMMARY

- **Overall verdict: CLEARED — 0 substantial, 19 cosmetic.** Loci I checked personally: the finding document's header in full (lines 5–50) against all six artifacts' own verdict and count lines and cosmetic enumerations; §2's verification table; §3.1 and §3.5; §5.1, §5.3 (in full, including the canon list and the corrected Fragment I gloss), §5.4, §5.5; §6, §6.1, §6.2; §8; §9's three options; §10 in full and against `git show 3e6c54b:…`; §11's Round 6 → 7 entry claim by claim; `Open_Gaps_Tracking.md` OG-6 in full (lines 247–325); `Doc_04_Gravity_Discovery.md` in place — heading inventory (ten sections, §0–§9), §0 line 39, §3.6's T1 pole rule (line 132) and T4 interior verdict (line 137), and **§6's Interaction Matrix in full** plus a whole-file `T1`/`T4` pairing grep; `records/alx/` by two greps; `npnf201` by grep; `find -iname "*Gravity_Index*"` repo-wide; `records/worlds.yaml` line 41; `git diff 3e6c54b..bf71ffb`, `git diff --stat b50302d^..bf71ffb`, `git status --porcelain`; and a pattern sweep for surviving round counts and status restatements across both in-scope files.
- **N6-1: RESOLVED, and structurally.** §10's status bullet no longer restates a round count, a trajectory or a draft ordinal — `grep` over §10 returns none. What remains is "Not cleared / no disposition," which is §10's actual job and does not tick on a round boundary, plus a disclosure of what the bullet used to claim. This is the deletion Round 6 asked for rather than a fourth hand-correction.
- **N6-2: RESOLVED.** The header's Round 5 bullet now reads *"Round 4's three all RESOLVED,"* which is what Round 5 examined, and the three loci that were in contradiction now agree.
- **The structural fix holds — within the finding document, completely.** No hand-maintained round count survives outside the header; every hit resolves to the header, the `Round*_Review.md` glob, an explicit historical quotation in §11, or a disclosure passage. **One trend restatement survived in OG-6** — *"the substantial-finding count has fallen monotonically round on round"* — and it is now false (1 → 2). I graded it cosmetic (**c-25**) rather than substantial, and §B.2 records the argument on both sides; the short version is that every load-bearing fact in that paragraph is correct and delegated, and what is wrong is an adjective on a trend whose actual values the header prints accurately. Round 6 graded the identical sentence cosmetic when it was already inaccurate, and applying a harsher standard now to a smaller residue would be manufacturing a round.
- **New substantial findings: none.** The revision touched seven loci, added no claim to §1–§9, disturbed nothing Round 6 verified from the sources, and introduced no fresh factual error. The two inaccuracies in new or reproduced text are adjectives — "consecutive" (c-24) and "monotonically" (c-25).
- **Discipline: clean on every line.** Eight files across seven commits, 2,288 insertions, nothing in `records/`, nothing in Doc_01–Doc_09, no corpus-map edit, no compile, `records/worlds.yaml` still pinned at `packages/alx/2026-09-04T16-41-49Z`, working tree clean. No self-disposal, no project-lead attribution, three grounded options intact, the portfolio decision separated and explicitly not run.
- **Headline: CORRECT, seventh confirmation. There is no route to a Doc_04 classification change.** Not through T1's pole rule, not through T4's interior, not through the absent T1↔T4 cell, not through C3, C4, C5, T2, T3, record-confidence, the Article 21 substitute, or either generation-step candidate. The ceiling is set by what the material is — episcopal legislation and late-mediated doctrinal excerpts — and that ceiling is a property of the corpus, not of how the tests were run. **§9 Option B, escalated and not self-disposed, should stand.**
- **Two edits must accompany this clearance, in the same commit.** **c-21:** OG-6's *"Every round to date has returned SUBSTANTIAL REVISION REQUIRED"* and *"The finding document is NOT cleared"* are falsified by this artifact. **c-25:** delete OG-6's "fallen monotonically" clause rather than re-characterizing it. The header's "Round 7 review pending" and §10's "Not cleared" bullet turn over on the same event. Round 6 predicted c-21 exactly; the prediction was right, and the fix is one paragraph.
- **What this document is, stated plainly, because it is the point of a seventh round.** Twenty-six substantial findings were accepted across six rounds and not one was disputed. Every one of them narrowed the case rather than widening it. The evidence work has been verified correct by six independent reviewers and, in the loci I re-ran myself, is correct. The document overstates nothing, claims no standing it has not earned, declines to dispose of a finding that is not its to dispose of, names the strongest unpursued lead in its own §3.5 and refuses to chase it, and applies to its own best find (Fragment VI) the transmission screen it demands of everyone else. Its remaining defects are nineteen cosmetics, of which the two urgent ones exist only because this review clears it. **That is a document that has earned a clearance, and withholding one for an adjective would have been the failure, not the rigour.**

*(This is a simulated AI review. It does not substitute for the Article 31 external scholarly review that OG-4 still requires, and clearing this finding document does not clear OG-4, does not dispose of OG-6, and does not authorize any of the three options in §9 — the disposition remains the project lead's. A qualified subject-matter reviewer on the transmission of the Alexandrian penitential canons through the Byzantine canonical collections and their ratification at Trullo, on the Melitian rupture and the standing of confessor testimony in Fragment I, and on the Eusebian mediation of Dionysius's Decian correspondence would be the accountable test of §5.3.)*
