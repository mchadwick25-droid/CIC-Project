# Doc_01 — Bounded Spot-Check, Round 3

**Document checked:** `witt_Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT, Revision 2, 213 lines)
**Scope:** only what Round 2 asked for — N1–N5 (substantial), N6–N17 (cosmetic), and the six partially-fixed Round 1 items (S16, C2, C11, C12, C13, C15), per this project's own Round 3 precedent (`gallic_Doc01_SpotCheck_Round3.md`). The substantive historical and methodological content Rounds 1 and 2 found sound was **not** re-reviewed. Every quotation, line citation and cross-reference *added or changed by this fix pass* was independently re-verified against its actual source.

**Checked against:** `witt_Doc01_Review_Round2.md` (full); `cic/texts/luther_works-v1-selected_jacobs-spaeth1915.txt` (lines 434–438, 990–994, 1135–1142, 12209–12213, 12692–12696); `cic/texts/luther_works-v2-selected_jacobs-spaeth1916.txt` (lines 13168–13180); `cic/texts/melanchthon_augsburg-confession_anon-pg275.txt` (Articles I–IV, lines 166–240); `cic-website/data/world-census.json` (VI.1, VI.27, VII.2 — parsed, not grepped); `World-Builds/Lutheran-Wittenberg/Step0_Movement_Scope_Confirmation.md`; `World-Builds/Society-of-Jesus/Step0_Movement_Scope_Confirmation.md`; `cic/corpus-map/lutheran-wittenberg-and-its-congregations.yaml`; `world-build-docs/_cross-world/dossiers/lutheran-wittenberg-and-its-congregations_Source_Readiness_Dossier.md`; Construction Framework V7.4 paras 85, 92, 121–122, 128–140, 198–209, 305–312 (python-docx).

---

## VERDICT: MINOR ISSUES REMAIN

All five of Round 2's substantial findings are genuinely fixed, and — unlike the previous two fix rounds — they are fixed *against the sources*, not against the reviewer's word. I independently reproduced every new citation this pass introduced: Framework para 85 and paras 202–204 verbatim from the .docx; the Article I Nicene-decree sentence; the 434–438 and 1139–1140 line ranges; both "Papacy at Rome" headings at 12211 and 12694; the *Kurze Form* title block at v2 line 13172; VI.27's and VII.2's `relationsSummary` fields parsed straight out of the census JSON; Step 0's B3 sentence and its actual section number; VI.11 Step 0 §2 A3; and the dossier's Gutenberg #417 / #9841 rows. Every one checks out.

The pattern Round 2 named — "every new substantial finding sits inside a sentence written to close a Round 1 finding" — is **broken this round.** Nothing substantial was introduced by the fixes. What remains is four small items: one Round 2 finding fixed in the wrong place (N13), one Round 2 partial whose last sub-point survives (C11), and two new overclaims of the exact kind the document just corrected elsewhere (a truncated quotation called "in full," and a load-bearing new claim left untagged). All four are in-place edits.

---

## FIX VERIFICATION — ROUND 2 SUBSTANTIAL FINDINGS (N1–N5)

| # | Status | Why |
|---|---|---|
| **N1** | **FIXED** | §4 now splits the attribution correctly: Article 17 for the *principle* (paraphrased, unquoted), **Construction Framework V7.4 paras 202–204** for the quoted wording. Verified in the .docx: para 203 "Live scholarly disagreement; no dominant position…", para 204 "Carry the tension; do not resolve it." Quotation and paragraph numbers both exact. The correction names its own error class rather than burying it. |
| **N2** | **FIXED** | The false "one this world's own Step 0 does not name" clause is gone; the header now states the opposite and correctly — Step 0 names VI.11 "by Atlas ID and founding date, at §3 B3." Verified: B3 is at Step 0 line 59, under `## 3. Section B — Seed Screening and Tiering` (line 47). Header and §8.4 now agree, and both cite §3 B3. |
| **N3** | **FIXED** | §10 carries a restored, extended unvendored-works bullet (line 179): hymns, *Table Talk*, the Peasants' War tract, *On the Jews and Their Lies*, service orders/hymnals, *Bondage of the Will*. All three broken pointers now resolve — §2.3's Peasants' War (§10) ✓, §5's service-order/hymn (§10) ✓, §9 item 1's *On the Jews* (§10) ✓. The two dossier leads are cited accurately: hymns = Gutenberg #417, *Table Talk* = #9841, both rows present at dossier lines 33–34, and both correctly described as live acquisition targets rather than closed questions. |
| **N4** | **FIXED** | §2.2 now quotes para 85 verbatim ("Nothing in Step 0 performs Step 1's own boundary-determination work" — confirmed) and argues 1580 from the Book of Concord as this world's own most complete confessional self-definition, with 1555 demoted to a political-legal internal-transition marker. The deference formulation ("because it is what the census and Step 0 both already give") is gone. §12's escalation-check sentence now holds. One residue, below: the new argument carries no confidence tag. |
| **N5** | **FIXED** | §8.0's transmission answer now names **VI.27** and **VII.2** by Atlas ID with their own `relationsSummary` text, correctly marked at the census's own confidence and explicitly not independently verified. §3 is rewritten to carry VI.27's four dated markers at the census's own `[S]`/"verified" distinction rather than calling them unavailable; §11 item 2 and new open item 9 match. Census text verified by parsing the JSON: both quotations are verbatim (the census uses a hyphen where the document prints an em-dash; immaterial). |

---

## FIX VERIFICATION — ROUND 2 COSMETIC FINDINGS (N6–N17)

| # | Status | Why |
|---|---|---|
| **N6** | **FIXED** | The header's blanket "re-read all six files" claim is now qualified and the miss is disclosed by name. §1 records both occurrences — section title page line 12211 ("THE PAPACY AT ROME"), translation heading line 12694 ("TO THE PAPACY AT ROME") — and states plainly that the corpus-map's title was never wrong, correcting Round 1's C3. Both lines verified; corpus-map line 175 matches the 12694 form. |
| **N7** | **FIXED** | §8.4 now cites **§3 B3** and says why ("Section B, 'Seed Screening and Tiering,' not Section A"). Correct. |
| **N8** | **FIXED** | "reads in full" is replaced by "in relevant part," with the omitted opening clause described rather than silently dropped. The quoted remainder is verbatim against Step 0 line 15. |
| **N9** | **FIXED** | Verified line-by-line: 434 "THE DISPUTATION…", 435 "ON THE POWER…", 436 "(THE NINETY-FIVE THESES)", 437 "1517", 438 "TOGETHER WITH THREE LETTERS…"; "II" at 1137, heading at 1139–1140, 1138 blank. The document states all of this exactly. Line 992 = "OCTOBER 31, 1517" still correct. |
| **N10** | **FIXED** | §4 cites `longDescription` alone; the `why` co-citation and the dangling "corrected below" are both gone. Confirmed against the JSON: `why` contains nothing about hymns or households; the quoted phrase is in `longDescription`, verbatim. |
| **N11** | **FIXED** | §8.4 quotes VI.11 Step 0 §2 A3 verbatim ("the same crisis those two candidates answer from the opposite direction" — confirmed at that file's line 31) and its own following paraphrase now preserves the direction of the claim: this world *responds to* the crisis rather than *representing* it. The inversion is named and retracted explicitly. |
| **N12** | **FIXED** | The disagreement log no longer says "this is the first review round"; it now reads "none — no Round 1 finding is disputed by Round 2, and this revision does not dispute any Round 2 finding either," with the C3/N6 supersession handled separately and accurately. |
| **N12a** | **FIXED** | §10's *Bondage of the Will* bullet now states the asymmetry outright: the dossier row is an on-record artifact, the launch-instruction account is corroborated by no file or log this document found. Dossier row (line 28) re-verified: three identifiers, `pd-us-by-date`, "direct fetch, 2026-09-15." |
| **N13** | **PARTIALLY FIXED** | The *Kurze Form* is added — at **§1 only** (line 20), cited as `luther_works-v2…` line ~13172, which I verified (title block at 13172–13174) along with the corpus-map note quoted from it (yaml lines 11–13, accurate). But N13's actual complaint was that **§2.3** rests "catechesis… present from the earliest treatises" on *A Treatise on the Holy Sacrament of Baptism* (1519), a sacramental treatise. §2.3 is unchanged — line 40 still cites only the Baptism treatise, and the *Kurze Form* appears nowhere in §2.3 or §4. The text was added where it was easy, not where the argument needs it. (The "§4 below" pointer at the end of that §1 parenthetical also does not land on anything about the *Kurze Form*.) |
| **N14** | **FIXED** | The Carlstadt trajectory claim is split out of the [Widely Accepted] tag, retagged **[Inferential/Thin, pending a Doc_02 source]**, explicitly marked as not a claim the file makes, and logged as new open item 10. The strand-versus-transition argument at §6 is correctly re-based on the documented 1522 silencing alone. The spelling inconsistency is now noted in-text as a deliberate convention. |
| **N15** | **FIXED (with one caveat, below)** | §10 abandons the "three-coeternal-persons" basis and uses Article I's Nicene endorsement instead — "the decree of the Council of Nicaea concerning the Unity of the Divine Essence and concerning the Three Persons, is true and to be believed without any doubting," verified verbatim at lines 168–171. This is the basis Round 2 recommended. |
| **N16** | **FIXED** | §12's escalation check now names the `witt` file-code assignment explicitly, disposes of it with a stated reason (working, ecology-neutral identifier; decides nothing about scope, window or Atlas placement), and declines to treat it as category 2 rather than passing over it. |
| **N17** | **FIXED** | §1's candidate-gravity bullet now carries four **[Documented]** tags on the evidence, with an in-text correction stating the distinction Round 2 drew — the vocabulary rates the evidence, not the gravity determination. The "not a claim this document is making at any confidence level" formulation is gone. |

---

## FIX VERIFICATION — ROUND 1 PARTIALS CARRIED INTO THIS PASS

| # | Status | Why |
|---|---|---|
| **S16** | **FIXED** | §10 now clears the floor "on Articles I **and** III together, not on Article III alone," with commitment (1) placed in Article I ("the Maker and Preserver of all things, visible and invisible" — verbatim, line 173) and commitment (5) rested on the Nicene endorsement. Article III's own Spirit language is described accurately ("only as sent into believers' hearts" — the file reads "by sending the Holy Ghost into their hearts," line 220). Step 0's overbroad claim is reported plainly rather than inherited. |
| **C2** | **FIXED** | Line range corrected to 434–438 with line 436 identified precisely; the "different arrangement of front matter" wording remains gone. Verified. |
| **C11** | **PARTIALLY FIXED** | The substantive half is closed — §12's escalation check now names and disposes of the file-code decision (N16). The residue Round 2 also flagged survives: the header's file-code disclosure still carries **no "C11" cross-reference**, while §12 line 207 still asserts that all fifteen Round 1 cosmetic findings were "each cross-referenced to its finding number at the point of correction." Only two occurrences of "C11" exist in the document, both in §12. `witt` remains recorded in no registry, corpus-map field or `world-build-docs` record (re-checked) — but that is honestly disclosed and is not something a Doc_01 can itself close. |
| **C12** | **FIXED** | The §8 worship pointer is withdrawn and the over-claim named: worship is now routed to §5 alone, with §8's comparisons correctly characterized as doctrinal rather than practice. Belonging is still named as a real gap rather than answered thinly. (Wording residue, not a finding: the bullet still says the document "defers worship and belonging" and then says worship is addressed at §5 — "defers" here means "handles elsewhere," which the following sentence makes clear.) |
| **C13** | **FIXED** | "Paris" and "Peter Canisius" are removed rather than left uncited, replaced by "Rome then worldwide" sourced to VI.11's own Step 0 (verified at that file's line 15), with an explicit note that neither addition was sourced. The Step 0 founding-date correction remains reported at §8.4 and flagged in the header and §12. |
| **C15** | **FIXED** | The `why` co-citation is removed; only `longDescription` is cited, and the misattribution is disclosed in place. The dangling "corrected below, finding C15" is gone. |

---

## NEW FINDINGS FROM THIS FIX PASS

Two, both cosmetic, both inside sentences written to close a Round 2 finding — the same risk surface Round 2 named, though at much lower severity than before.

#### NEW-1 — §8.0 calls a truncated census quotation "cited in full," which is the N8 defect one section over.

§8.0 describes VI.27's `relationsSummary` as "**cited in full at §3**." §3's citation begins at "Denmark-Norway's decisive break" and ends at "Iceland by 1550 [S]." The actual field opens "Two established national churches: …" and closes "…; ends the atlas's 500-year Scandinavian silence." Both ends are dropped. Nothing load-bearing is lost, and §3 itself never claims completeness — only §8.0 does. This is exactly N8's defect (a truncation-correction labelling its own quotation "in full"), recurring in the sentence written to close N5. Fix: "cited at §3," or restore the two clauses.

#### NEW-2 — §2.2's replacement ending-point argument is untagged and rests on an unvendored claim.

The N4 fix makes the Book of Concord's composition load-bearing for the 1580 ceiling — "the Augsburg Confession and its Apology… the Small and Large Catechisms… plus the Smalcald Articles and the Formula of Concord." The document says in the same breath that the last two are not vendored, and the Book of Concord as a compilation is not in the library at all. §2.2 now carries **no confidence tag anywhere**, while §2.1's parallel beginning-point finding closes with **[Documented]**. After N17 expressly established that this document tags evidence rather than conclusions, the section that replaced a deference argument with an evidence argument should carry the tag that argument earns — plausibly [Widely Accepted] for the Book of Concord's contents, with the vendored/unvendored split already stated.

#### Noted, not a finding — the N15 basis is one council removed.

The Nicene *decree* of 325 says only "And in the Holy Spirit"; "worshiped and glorified together with the Father and the Son" is Constantinopolitan (381). §10 reasons that Article I's endorsement of "the decree of the Council of Nicaea" "carries the Creed's own Spirit clause… with it." That inference depends on reading Article I's "Nicaea" as the Niceno-Constantinopolitan creed — which is standard Lutheran confessional usage (the Book of Concord prints the 381 text as "the Nicene Creed"), so the conclusion holds. But the step is left implicit, and this was Round 2's own recommended basis, so it is not charged against the reviser. One clause naming the 381 expansion would make it airtight.

---

## WHAT I RE-VERIFIED AND FOUND EXACT

Every new or changed citation in this pass: Framework paras 85, 92, 122, 128–131, 133–137, 202–204, 309; Augsburg Confession Article I (Nicene decree, Maker-and-Preserver, the six-name condemned list), Article III (Spirit into believers' hearts), Article IV (justification); v1 lines 434–438 / 992 / 1137–1140 / 12211 / 12694; v2 line 13172; corpus-map `A Brief Explanation…` entry (locus and note); census VI.1 `legacy` / `longDescription` / `why`, VI.27 and VII.2 `relationsSummary`, all four `dates`/`atlasId` values; this world's Step 0 §1 and §3 B3; VI.11 Step 0 §1 and §2 A3; dossier rows 28, 33, 34. Also checked: all 108 internal `§` pointers resolve to sections that exist; VI.27 and VII.2 have no `World-Builds/` directory, so "unbuilt" is accurate.

---

## RECOMMENDATION

**Ready to self-dispose as "Approved to proceed" under CO-022, after four in-place edits — no fourth review round.** Nothing here is a substantial revision: no finding is disputed, no claim is unsourced in a way that changes a conclusion, no quotation is wrong, and no internal contradiction survives. None of CO-022's four escalation categories is triggered — no Representative identity/title decision is made; the temporal ceiling, the strand finding and the cross-world framing are now genuinely argued from this world's own evidence rather than deferred (N4 closed); no governance or methodology change is made; and the one unresolved tension the document carries (the *Bondage of the Will* acquisition discrepancy) is already correctly flagged under category 4 and routed to Doc_02 rather than adjudicated. The four remaining edits are: move the *Kurze Form* into §2.3 where the catechesis claim actually needs it (N13); add the "C11" marker at the header's file-code disclosure, or soften §12's blanket cross-reference claim (C11); change "cited in full at §3" to "cited at §3" (NEW-1); and give §2.2 a confidence tag (NEW-2). None requires re-reading a source, none changes a finding, and none is blocking — so under the build cycle's own per-document self-governance the reviser can apply them and dispose, rather than spending a fourth adversarial round on four sentences.

**Reviewer:** independent adversarial reviewer, bounded Round 3, no drafting or revision context.
**Date:** 2026-09-15
