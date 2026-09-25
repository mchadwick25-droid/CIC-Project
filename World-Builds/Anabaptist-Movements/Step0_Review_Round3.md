# Step 0 Review, Round 3 — The Anabaptist Movements

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. This is a targeted recheck against Round 2's findings R2-1 to R2-11. It is the final round under the three-round cap.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md` at "Revision 3" (commit `3dc421002`).
**Checked against:** `Step0_Review_Round2.md`; the vendored files in `cic/texts/`; `cic/corpus-map/the-anabaptist-movements.yaml` and the five other batch corpus-maps; `cic-website/data/world-census.json`; `worlds/_cross-world/dossiers/the-anabaptist-movements_Source_Readiness_Dossier.md`.

## Verdict

**CLEARED — approved to proceed.**

Every Round 2 finding has been fixed in substance. Every quotation in the document was re-verified against its vendored file and is present verbatim. The only differences are OCR noise and whitespace. The sourcing numbers match the files exactly. What remains is four low-severity items. None of them makes a statement wrong, unsupported, or misleading in a way that bears on the conclusions. One upstream flag (R2-8) is still open, but it sits outside this document.

## Round 2 findings — status

- **R2-1 (sourcing out of date): FIXED.** B1 now lists all eight works from the current corpus-map, each with the correct word count. `wc -w`: Menno 531,221; *Martyrs Mirror* 1,187,986; Dirk 207,849; McGlothlin 134,065; Hutterite 351,933; Ausbund 136,628; Elkhart Dordrecht 23,740; Vedder 85,544. The total is 2,658,966, so "approximately 2.66M" is correct.
  - I recomputed the batch ranking by summing unique `source_file` entries in each corpus-map. The result is Lollardy 4,950,767; Society of Jesus 3,370,675; Tridentine 2,906,711; Anabaptist 2,658,966; Reformed Cities 2,303,345; Wittenberg 958,758. "Fourth of six" is accurate, and all six rounded figures match.
  - The Hubmaier gap is restated as partly closed. The Ausbund and the Hutterite chronicle are placed at second-witness status for scan quality, not language, which matches the corpus-map notes. The Elkhart Dordrecht is out of the "unassessed" list. §4 item 6 now names only the Täuferakten and Harder. The Tier conclusion's item 2 and §4 item 2 are rescoped to match.
  - The date-stamp is present ("As of … 2026-09-25 state").
- **R2-2 (Round 1 file missing): FIXED.** `Step0_Review_Round1.md` now sits beside this file.
- **R2-3 (Lactantius mis-citation): FIXED.** The text now reads "pneumatological and eschatological." It also says explicitly that the precedent is invoked only for the *kind* of complication, not the same commitment.
- **R2-4 (Herman truncation and scope): FIXED.** Herman's reply is quoted through "and not the seed of Mary." That wording is verified verbatim in `van-braght_martyrs-mirror_sohm1886.txt`. The heading of A1, the Section A conclusion, the Tier conclusion and §4 item 1 all now carry the complication to all three pillars: Menno, Dirk, and the *Martyrs Mirror*.
- **R2-5 (Hubmaier's placement): FIXED.** §1 places Hubmaier at Nikolsburg in Moravia from 1526, and A1 separates him from the Swiss Brethren proper. B2 now says "his own Moravian base." The dissent on the sword is disclosed in §1 and carried into §4 item 4.
  - The Vedder Appendix (p. 273) is addressed "To the noble and Christian Lords, Arekleb of Bozkowitz and Tzernehor of Trebitz, Chancellor of the Margravate of Moravia." Vedder p. 164 says Hubmaier "had never … taught the extreme doctrine of non-resistance, forbidden Christians to be magistrates." Schleitheim (McGlothlin) forbids Christians the sword. The conflict is real. See L3 on the wording.
- **R2-6 (floor evidence from the Dutch wing only): FIXED.** A1 paragraph 2 states plainly that the evidence is Dutch-wing only. It links the Swiss and Moravian floor question to §4 item 4, and that link is repeated in the Section A conclusion, the Tier conclusion and §4 item 4.
  - The Riedemann lead is disclosed as McGlothlin's own summary. "twelve articles of religion" is verified in the McGlothlin file.
- **R2-7 (narration strip): FIXED in substance.** All the phrases listed in Round 2 are gone from §§0–4, including "Revision 1 attributed…", "brought current", "scope corrected", "New in this revision", and "rather than an inherited, unverified quotation". The Menno misattribution is now a present-tense source-fidelity note. §5 was not assessed, as instructed. For a small remaining trace of corpus-history wording, see L2.
- **R2-8 (dossier root cause): STILL OPEN UPSTREAM. This is not a defect in this document.** Dossier §5 still attributes "as through a channel" to Menno and still gives Minucius Felix as the precedent. Dossier §4 still calls Vedder "scattered quoted excerpts." This is carried below as a flag to the owning thread.
- **R2-9 (the "abominable errors" paraphrase): FIXED.** The text now follows Menno's own construction: errors "result from their confession," and the first is "A divided Christ." This is verified in *Reply to Gellius Faber*.
- **R2-10 (cross-references): FIXED.** §0 carries the 1,100-year figure, and B4 points to §0.
- **R2-11 (citation looseness): FIXED.** The Waterlander citation is now "Article II", and both sentences are verified there. The VI.14 name is quoted exactly as the census gives it. The census's "read with care for genre… coerced, not plain inside voice" qualification is quoted exactly.

## Quotations re-verified (normalized for whitespace and hyphenation)

- **Menno** (`menno-simons_complete-works_funk1871.txt`):
  - the anti-Donatist sentence;
  - "weighty and intolerable improprieties and abominable errors" and "A divided Christ";
  - the opponents' confession "the whole person, Christ Jesus, with body and soul, is the natural fruit of the flesh and blood of Mary" (OCR "Ijody");
  - "truly God and man… became a miserable, suffering and mortal man in Mary, the pure virgin… planted in her… fed and nourished in her virgin body" (OCR "suftering"). The elisions are fair;
  - "the man of Mary's flesh".
  - **"as through a channel" is absent from the file**, which confirms the correction.
- **Dirk** (`dirk-philips_enchiridion_kolb1910.txt`):
  - "liken us to the Donatists… A great injustice is done to us" (OCR "tous");
  - the Trinitarian sentence, with the elision checked;
  - "it is impossible for the flesh of Christ to be formed by Mary…" (OCR "for-neither").
- ***Martyrs Mirror*** (`van-braght_martyrs-mirror_sohm1886.txt`):
  - Dordrecht Article I;
  - "the Word, Himself became flesh and man; that He was conceived in the virgin Mary";
  - the friar Cornelis's sieve/spout line;
  - Herman's full reply.
- **McGlothlin** (`mcglothlin_baptist-confessions-of-faith_1911.txt`): Waterlander Article II (OCR "In sacred") and Article VIII.
- **Census** (`world-census.json`): the "RICH in ordinary inside voice…" string, the "Tiered Strong (Tier 1) on a rich base" string, and the full VI.14 name are all exact.

## Remaining findings

### Low severity

**L1. The two vendored translations of Dordrecht Article IV differ on the preposition the "in, not of" argument uses.** A1 cites Dordrecht's "conceived in the virgin Mary" as fitting the celestial-flesh pattern, and the Section A conclusion calls the complication "specific to the Dutch wing's own confessional 'in Mary' phrasing."
- The *Martyrs Mirror* text does read "in."
- The standalone Elkhart 1890 edition, which the document now lists as vendored, reads "he was conceived **by** the Virgin Mary."

Part of the "in" inference therefore depends on the translation. It is only corroboration. The complication itself stands on Menno's, Dirk's and Herman's explicit words, so no conclusion changes. **Carry-forward for Doc_01 and Doc_02:** name the variant between the two editions, and check the 1632 Dutch before leaning on the preposition. This does not need a fourth revision.

**L2. Some temporal wording about the corpus remains.** B2 has "not the clean zero the corpus previously carried" and "is now partly available." The Tier conclusion has "now partly recovered" and "now joined by." These describe changes in the corpus's state, not the document's revision history. They are mild. At the next edit, restate them in the present tense.

**L3. "Rejects Schleitheim's own non-resistance position" (§1, §4 item 4) slightly overstates how directly the treatise engages Schleitheim.** Per Vedder, *On the Sword* is aimed at "certain brothers" at Nikolsburg, meaning the Hut and Widemann party. It does not name Schleitheim. The conflict in substance with Schleitheim's article on the sword is real and verified. A more precise wording would be "argues against the non-resistance position Schleitheim holds." This is a precision point and does not change the coherence question.

**L4. There is a housekeeping mismatch in the Status line and §6.** The Status line has a stray "(see `Step0_Review_Round2.md`)" attached to the dossier citation. Both the Status line and §6 still say "Not independently reviewed at this revision." Update both to point to this Round 3 clearance when the status is next touched.

### Flag to the owning thread (outside this document)

**R2-8 is carried forward.** The Source Readiness Dossier still has the Menno "as through a channel" misattribution and the Minucius Felix precedent in §5, and the stale Vedder verdict in §4. Doc_01 and Doc_02 will read that dossier, so the owning source-research thread must correct it before Doc_01 drafting begins. Otherwise the defect this document fixed will come back downstream.

## Disposition

**CLEARED — approved to proceed.** No high- or medium-severity findings remain. L1–L4 are low: L1 is a carry-forward for Doc_01 and Doc_02, and L2–L4 are wording and housekeeping to fold into the next touch. None of them justifies a fourth revision round.

The headline conclusions hold as stated:
- It clears Section A, on the Dutch wing's affirmative confessions, with the Swiss and Moravian floor dependency disclosed.
- It is Tier 1, provisional, with three binding items.

Approval at Step 0 closes nothing at the portfolio level. Selecting the candidate and opening a build thread remain Mark's decisions.
