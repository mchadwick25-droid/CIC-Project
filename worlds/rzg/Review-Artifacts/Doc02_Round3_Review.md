# Doc_02 (Source Ecology) / Source Registry / Source Acquisition Manifest — Round 3 Adversarial Review (Targeted Recheck)

**World:** The Reformed Cities — Zurich & Geneva (`rzg`)
**Reviewed at commit:** `e5259cda` ("Fix Doc_02's own Dort/Schaff undercount, found at Round 2 review"), branch `reformed-cities-doc01` (checked out elsewhere; reviewed from a content-identical local branch `review-round3-e5259cda` at the same commit, confirmed via `git rev-parse`)
**Documents reviewed:**
- `World-Builds/Reformed-Zurich-and-Geneva/Doc_02_Source_Ecology.md` (DRAFT, Revision 3)
- `World-Builds/Reformed-Zurich-and-Geneva/Source_Registry.md`
- `World-Builds/Reformed-Zurich-and-Geneva/Source_Acquisition_Manifest.md`
**Prior round:** `Review-Artifacts/Doc02_Round2_Review.md` — SUBSTANTIAL REVISION REQUIRED (narrow scope: 1 new High, 1 new Medium), reviewed at `4fd3579b`.
**Reviewer stance:** cold adversarial review, no drafting context. Per `cic-build-cycle` and this project's cost discipline, this is a **narrow, targeted recheck** of Round 2's two findings, plus a final holistic sanity skim — not a full re-review from scratch.

---

## Verdict: CLEARED

Both defects Round 2 found are genuinely, independently fixed, cleanly and precisely — no fix-on-a-fix, no new collateral defect introduced, no residual inconsistency. The holistic skim of all three documents and Doc_01 found nothing this revision's own edits disturbed. This document set is ready for disposition.

---

## 1. The Dort/Schaff fix — independently re-verified

Grepped `cic/texts/schaff_second-helvetic-confession-heidelberg-catechism_1919.txt` for "dort" directly, myself, without trusting Doc_02's own account:

```
2724: ...the synods of Wesel, 1568, of Emden, 1571, and of Dort, 1574, recommended and enjoined its use;
2751: ...the famous General Synod of Dort, after a careful examination, opposed any change, and, in its 148th Session, May 1, 1619, it unanimously delivered the judgment that the Heidelberg Catechism 'formed altogether a most accurate compend of the orthodox Christian faith...'
2869: The English delegates to the Synod of Dort, George Carleton (Bishop of Llandaff), John Davenant (afterwards Bishop of Salisbury), Archdeacon Samuel Ward, Dr. Thomas Goade, and Walter Balcanqual, said...
2878: The favorable judgment of the Synod of Dort itself has already been quoted.
```

**Four occurrences, confirmed.** One (2724) is the unrelated 1574 synod. Three (2751, 2869, 2878) genuinely describe the real 1618–19 Synod: the 148th Session verdict (dated 1 May 1619 in the text, matching Doc_02's citation exactly), a verbatim quotable fragment ("a most accurate compend of the orthodox Christian faith" — checked character-for-character against the source, an exact substring), and the five named English delegates — George Carleton, John Davenant, Samuel Ward, Thomas Goade, Walter Balcanqual — matching Doc_02 §7's list name-for-name (including that the text spells the office "Archdeacon Samuel Ward," which Doc_02 correctly compresses to a bare name without inventing a title it didn't check). Line 2878 is confirmed as a back-reference to the same 148th-Session judgment already quoted at 2751, not a fourth independent claim — Doc_02 correctly treats it as part of the same three-line cluster rather than double-counting it as separate content.

I also independently confirmed these four lines sit within the same §69 ("The Heidelberg Catechism, 1568," pp. 548–551) that Registry row 10 already cites as verified (original pp. 529–554) — including the false-positive line 2724, which falls in the same section/page range as the other three. This matters because it shows the false-positive and the genuine hits were never separable by "wrong section" — the drafter's original miss was a reading failure, not a section-boundary error, and this revision's fix correctly does not imply otherwise.

**Doc_02 §7's new text:** accurately states the 1574/1619 distinction, correctly attributes the 148th Session verdict and its date, quotes only the verbatim fragment actually in the source (in quotation marks, not overextended), and names the five English delegates exactly as they appear. It explicitly and correctly declines to treat this as evidence for or against Doc_01 §7's own separate, still-unverified claim about a Zurich/Genevan delegation (Diodati, Tronchin, Breitinger — none of whom appear anywhere in this file), stating plainly "the delegates named here are English, not Swiss." This is exactly the boundary Round 2's H1 finding asked the fix to hold, and it holds it without hedging or blurring.

**Source Registry row 10's Verification Note:** correctly cites the same three genuine lines (2751, 2869, 2878), correctly describes the same 148th Session verdict and the English delegates' praise, and correctly cross-references Doc_02 §7 rather than re-arguing the point independently. It does not re-mention the 1574 false-positive (line 2724) — a reasonable editorial choice for a per-source ledger entry describing what this row's own text actually contains that touches Dort, not an exhaustive keyword inventory — and this does not contradict or duplicate Doc_02 §7's fuller narrative account; it summarizes the same finding at the appropriate grain for its own document type, consistent with the Source Registry Template's role as "the per-source ledger," not the narrative judgment.

**No overclaiming found.** Neither document treats this Schaff-mediated English-delegate testimony as bearing on Doc_01 §7's Zurich/Geneva delegation question, and neither expands into the Synod's broader doctrinal controversy (correctly left to VI.26 per Doc_01's confirmed boundary).

## 2. The Registry's "Priority second-opinion review trigger" sentence — verified against rows 13–17 directly

Current sentence (`Source_Registry.md` line 31):

> "Rows 11–12 are consultation-only secondary scholarship. Rows 13–17 are Native (subject matter squarely in this world's own boundary) but not yet acquired — Confidence D/E, not 'excluded,' per the Template's own schema (Doc_02 Round 1 review finding H3)..."

Read rows 13–17 directly: all five show Boundary Status = **Native** and Exclusion Reason = **"—"** (blank), matching the sentence's claim exactly. Confidence values are D (row 13) and E (rows 14–17), matching "Confidence D/E." No row among 13–17 is marked Excluded, and the sentence no longer asserts otherwise. **Fully consistent — the contradiction Round 2 found (the summary sentence still calling these rows "excluded" while their own fields said Native) is gone**, and I found no other stray use of "excluded" describing rows 13–17 anywhere in Source_Registry.md, Doc_02, or the Manifest (checked by direct grep across all three files — the only other "Excluded" hits are the Boundary Status column's own legend definition and Doc_02's masthead retrospectively naming the historical Round 1 defect, neither a live mischaracterization).

## Diff-scope check

`git diff 4fd3579b e5259cda` confirms the fix was exactly as narrow as it should have been: Doc_02's masthead status line and §7 (the Dort passage), Source_Registry row 10 and its closing summary sentence, plus the new Round 2 review artifact. `Source_Acquisition_Manifest.md` was not touched at all, correctly — nothing in Round 2's findings required it. No collateral edits, no fix-on-a-fix, nothing else in either document disturbed.

## Holistic sanity check (final pass before disposition)

Read the full current text of all three documents and Doc_01 §7/§8 (Dort scope) against them:

- **Doc_01 §7's own delegation claim** (Diodati, Tronchin, Breitinger — the Swiss/Genevan delegation, still "attested in standard historiography, not yet verified against a vendored primary source") is unaffected by and consistent with Doc_02's new §7 text, which correctly treats the two delegation claims (English vs. Swiss) as distinct and does not let one bear on the other.
- Doc_02 §9's open-items list does not add a new item for this now-resolved finding — appropriate, since it is disclosed and closed within this pass, not an outstanding gap requiring future action (Round 2's suggestion to "consider" adding it was advisory, not a fix requirement).
- `Open_Gaps_Tracking.md` was not checked as in-scope for this document set's own review (it belongs to Doc_01's own gap trail), but a quick check found no stale reference to the old undercount claim there.
- No other content in Doc_02 §1–§6, §8, §10, the Registry rows 1–9 and 11–17, or the Manifest's G1–G5 items shows any sign of having been disturbed by this revision's edits — all match what Round 1 and Round 2 already independently verified, and nothing in this revision's diff touched them.
- No new fabrication, no reintroduced reserved-vocabulary misuse, no new schema conflation found anywhere in the current text.

## Escalation-category check

- Representative identity/title/voice: does not apply.
- Portfolio-level or cross-world decision: does not apply.
- Governance or methodology decision: does not apply.
- Unresolved tension the pipeline can't close on its own: does not apply.

No escalation category is live.

---

## Recommendation

This document set (Doc_02 Revision 3, Source_Registry.md, Source_Acquisition_Manifest.md) is clean. No further revision round is required on the substance reviewed here. Recommended disposition: proceed per `cic-build-cycle`'s own self-governance — Doc_02 may move to "Approved to proceed."
