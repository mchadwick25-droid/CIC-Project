# Confirming Review — commit `59dec2a5` (Donatism ordinary-believer pass, Round 2)

Targeted independent confirming re-review of the fix pass (commit `59dec2a5`)
against Round 1's findings (`OrdinaryBeliever_Round1_Review.md`), run per
CLAUDE.md's rule that "a blocking review finding can't be dismissed by
self-certification — it needs independent re-confirmation." Not a fresh
open-ended review; targeted at whether the two BLOCKING findings actually
landed, plus a spot-check of the rest.

## CHECK 1 — BLOCKING F-1 (circumcellion / Axido-Fasir withdrawal): PASS

File: `records/don/doctrinal_witness/don.dw.what-we-did-with-the-power-we-had.md`

- Every occurrence of "slave," "debt," "III.4," "Axido" in the file is
  footer prose only (the explanatory note of what was withdrawn and why).
  Zero hits for "chariot," "master," "III, ch. 4" anywhere in live fields.
- `sources:` no longer carries `don.source.optatus-against-the-donatists`.
- The `text` Circumcellion paragraph is byte-identical to the pre-pass
  baseline (`98b78db9`), ending at "...or deny it as though we had a
  better one." The hostile-narrative addition, the corresponding
  `positions` bullet, and the merged Theodosian-corroboration clause are
  all gone.
- The withdrawal is named, not silent: `confidence.divergence_note` and
  the footer both name Doc_09 §6's reservation, quote it verbatim, and
  close "The material - and the standing Article 23 question it runs
  into - is left for the project lead, not resolved here."
- Verified independently against primary sources, not taken on the
  footer's word: `Doc_09_Story_Inventory.md` line 110 does contain the
  quoted reservation; `don_Decision_Log.md` carries 13 "Article 23" hits
  and the most recent entries (lines 848-849) still list it open;
  `cic/texts/optatus_against-the-donatists.txt` III.4 confirms the
  debt/master-slave material is the immediate continuation of Axido/Fasir,
  and that the officer who acted was Taurinus on the Donatist bishops' own
  letter, not imperial law - the footer's factual correction is right.

## CHECK 2 — BLOCKING F-3 (Crispinus allegation not re-narrated): PASS

`don.dw.becoming-one-of-us.md` - every hit for Crispinus / eighty /
Mappalian / Calama / "single day" / tenants is footer-only. Zero hits for
"farm" or "miserable groans" anywhere in the file. The live `text`
paragraph now only names that hostile-sourced charges exist and
cross-references `don.limit.bagai-violence-no-account` rather than
repeating their content. `positions` and `tensions` match. The two source
entries that carried the withdrawn material were removed from `sources:`.

`don.limit.bagai-violence-no-account.md` is not corrupted: diffed against
baseline `98b78db9`, its `statement` and `why_sources_cannot_answer` are
byte-identical to what they always were. The only changes are the
reciprocal `relations` edge and the footer note. The corrected footer
("Its first drafted revision claimed to follow 'the identical discipline'
while actually narrating that charge's own particulars in full... caught
by independent review and corrected before this note was written")
accurately describes what happened and introduces no new inaccuracy.

## CHECK 3 — spot-check of the other fixes: PASS

- "in a single day," "eighty tenants," "young": absent from all live
  fields, present only in footer prose describing removal.
- Quantifiers re-verified directly against
  `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml` (On
  Baptism I.5.6, §6): source reads "almost all their laity... confess...
  and many who... strive with many secret efforts." Record now matches:
  "almost all of our laity... and that many who wished to join us..."
- Adeodatus binary resolved: old text left "boast or admission" fully
  unresolved; new text reads "less like an apology than a claim to his
  own standing - but either way, fear is the word he himself used for
  what held the place." The matching `tensions` bullet was rewritten and
  now carries the OCR/translation caveat.
- `don.dw.what-belonging-cost.md`: *pietas* correctly rendered "family
  devotion," not "love" (a different, pre-existing "everyone you love"
  sentence elsewhere in the text is unrelated and untouched).
  `confidence.divergence_note` now discloses the OCR/translation caveat
  explicitly.
- `don.limit.no-ordinary-day-survives.md`: the "whole of what survives on
  women among us" locus now reads "...in their own names," consistent
  with the record's own new third (anonymous, virgins) trace.

## CHECK 4 — gate battery, run independently: PASS

`python3 -m engine.m2.cli build don` -> 17/18 gates pass, sole failure
`reciprocity` with 55 findings - identical to both the pre-fix and
original-draft builds, no growth. Of the 55, exactly 2 touch this pass's
records, and both existed at baseline `98b78db9` already; this pass's own
new edge pair (`becoming-one-of-us` <-> `bagai-violence-no-account`) is
declared in both directions and generates no finding.
`python3 -m engine.m1.cross_world --world don` -> 0 new defects, 16
accepted-open, 64 observations.

## Verdict: CONFIRMED

Both blocking fixes landed correctly and fully. F-1's material is
withdrawn from every live field with the Article 23 reservation named
rather than quietly disposed; F-3's allegation content is gone from
`becoming-one-of-us`'s live fields, the honest_limit record it defers to
is intact and uncorrupted, and the false "identical discipline" claim is
corrected accurately. All 12 spot-checked items hold. Gates and
cross-world checks are unchanged from baseline.

## Three non-blocking observations (none affecting the verdict above)

1. **Dangling reference, now fixed.** `don.dw.becoming-one-of-us.md` cited
   "`Review-Artifacts/` findings F-3 through F-7" before any artifact from
   this review existed there. This file and its Round 1 companion
   (`OrdinaryBeliever_Round1_Review.md`) resolve that.
2. **No Decision Log entry existed at the time of this check.** Required
   by CLAUDE.md's gap-tracking rule; added to `don_Decision_Log.md`
   immediately after this confirming review, per this world's own Phase 4
   convention.
3. **Minor commit-message imprecision** (a headline finding-count that
   didn't match the body, and one footer sentence whose "unchanged from
   the first pass" heading covered one item that had in fact changed).
   Neither affects live record content; noted for the record rather than
   re-committed.
