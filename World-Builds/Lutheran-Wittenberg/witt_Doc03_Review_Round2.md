# Doc_03 Review — Round 2 (independent adversarial recheck, cold)

**Document under review:** `witt_Doc_03_Lexicon_Candidate_List.md` (DRAFT, Revision 1), Lutheran Wittenberg & Its Congregations (Atlas VI.1, `witt`).
**Reviewer:** independent, no drafting involvement, no involvement in Round 1, no prior context on this document or on how its fixes were made.
**Date:** 2026-09-15.
**Scope:** targeted Round 2 recheck per the project's own round-2-onward usage discipline — what changed, against Round 1's findings — plus an independent fresh citation sample, per §13's own "Review requirement (next round)" item (f). This is **not** a repeat of Round 1.

**Method.** Both files read in full (Doc_03 Revision 1, 837 lines; `witt_Doc03_Review_Round1.md`, 350 lines), plus Doc_01 §8 in full and `witt_Source_Registry.md`'s header and row R30. The Lexicon Framework V2.1 was opened directly via python-docx to re-read paras 91–111 (the [PV] and [CT] tag definitions) rather than taking either the Round 1 report's or the document's quotation of para 97 on trust. Every vendored locus named in (a)–(e) was re-opened at its stated lines. All disputed counts were re-run with my own `grep`, not read off either document. Two independent scripts were written: one extracting all file+line citations from the entry bodies (§§1–9) and testing each against §13's declared read-ranges (606 distinct citations), one recomputing entry counts, tier counts, tag sets and the full body-vs-Appendix cross-check for all 72 entries. A fresh sample of 24 citations not touched by any Round 1 finding was re-opened by hand across §1, §4, §5, §8 and §9.

---

# VERDICT: MINOR ISSUES REMAIN

**5 new substantial findings (N1–N5). 3 new cosmetic findings (N6–N8). Zero Round 1 findings failed to land.**

**All 24 Round 1 findings (S1–S14, C1–C10) were re-checked against the sources and all 24 landed as claimed.** I could not falsify a single one. In particular, nothing in this revision misquotes a source, miscites a locus, misstates a count, or misclassifies an entry. The three defects that most need fixing (N1, N2, N3) are propagation and warrant defects in the *reporting* of fixes, not errors in the fixes themselves.

**Why not SUBSTANTIAL REVISION STILL REQUIRED.** Round 1's threshold for "substantial" was breached by a misworded quotation, an invented detail, a falsified read-record, and an unapplied governing principle. Nothing at that level survives. N2 is a recurrence of the S14 *pattern* (a sibling document cited for a proposition it does not contain), which Round 1 graded substantial, and a reviewer could reasonably grade this report higher on that basis; I have not, because N2 is a single clause in §0 attached to a disclosure whose main claim — that these neighbours were *not* tested — is correct and honestly made, and because the remedy is one sentence. I record the calibration so a later reader can disagree with it.

**Disposition: none claimed.** This report is a finding, not a ruling; it does not dispose the document. Per the project's governance rule, none of the findings below may be closed by self-certification.

---

# What I verified and what held — stated specifically

Recorded item by item, because "the fixes landed" is a claim a later reader should be able to re-run rather than trust.

## (a) The corrected quotations and citations

- **S1 — 6.8, the Apology quotation.** `melanchthon_apology-augsburg-confession_bente-dau1921.txt` lines 6492–6495 read "fanatical men, who dream that the Holy Ghost / is given not through the Word, but because of certain preparations of / their own, if they sit unoccupied and silent in obscure places, / waiting for illumination, as the Enthusiasts formerly taught, and the / Anabaptists now teach." The document now reproduces this **character for character**, including the full clause the previous ellipsis had swallowed. AC 253–255 is quoted separately and correctly ("without the external Word, through their own preparations and works"). The entry now states the cross-voice difference explicitly, and the Tags line's distortion flag has been rewritten to attribute "without the external Word" to AC and the other formulation to the Apology. Fixed correctly and completely. **Ap 4729** verified: the line reads "fanatical opinions of the Anabaptists."
- **S2 — 9.6, the "Augustinian" claim.** `grep -i augustin` over `luther_hymns_bacon-allen.txt` returns exactly one hit, at line 1078, about the works of St. Jerome and St. Augustine — unrelated. The order is no longer asserted anywhere in the entry; the preliminary definition now reads "two young monks, named John and Henry," which is what the text supports ("monkish garb," "gown of ordination," "all monkish follies"). The Registry correction was checked too: `witt_Source_Registry.md` row R30's Licensed For column now reads "two young monks, named John and Henry," with an inline correction note naming Doc_03's Round 1 S2 as the trigger, and the file header carries a dated post-approval technical-correction paragraph stating that Boundary Status and Confidence are unchanged. Round 1's fix instruction ("raise R30's wording separately with the Registry owner") is satisfied in substance — the change is disclosed and logged, not silent.
- **S3 — 9.6's internal contradiction.** `grep -i martyr` over `melanchthon_augsburg-confession_anon-pg275.txt` returns **zero** hits, confirming Round 1. AC 765–766 is gone from 9.6's Evidence; the Voices line now reads Luther-only; the AG line is unchanged and now agrees; the Appendix row 9.6 reads `L single (hymn)` / `L (hymn)`, with the stray `M` removed. All four statements agree. All nine hymn loci re-verified verbatim at their stated lines (1744–1745, 1756, 1759–1760, 1763, 1767, 1789–1790, 1800, 1807, 1839).
- **S8 — the 2.2 term-frequency figures.** Re-run against the Apology file: literal case-insensitive `justification` = **124** ✓; `justif` (stem) = **376** ✓ (= justified 138 + justification 124 + justifies 48 + justify 46 + justifying 12 + justifier 6 + justifieth 1 + justifiest 1). The other nine figures all reproduce exactly: the Law 393, promise 314, merit 339, conscience 198, satisfaction 122, sacrifice 156, human tradition 37, vocation 32. Both 2.2 and §11 item 1 now state the counting method. Fixed correctly.
- **S9 — the "two kingdoms" claim.** v3 line 12371 reads, as found, "For this reason these two kin ee must be sharpl" — the document's OCR transcription of 12371–12374 is exact. The running marginals verified at 12123–12127 ("The Two / King- / ' doms") and 12276–12280. `grep -i "two kingdoms"` across all ten files returns three hits, all in Cole's *Bondage* (5220, 14748, 14769) — consistent with the document's account. §10.3's bullet and 7.1's [CT] ground have both been rewritten: the false clause is gone, and the contest is now re-argued on whether the later systematic *label* is Luther's own category, which the evidence supports. The re-argued ground survives the test that defeated the old one.
- **S10 — the two thesis numbers.** v1 line 1249 prints "36." for the thesis whose standard number is 26; line 1285 prints "36." again for the real Th. 36; line 1348 prints "53." for the thesis whose standard number is 52. The document now cites what the file prints at both 1.6 and 1.1/9.3, states the standard number as a correction rather than substituting it silently, and adds a warning to §0 Discipline 1. Fixed correctly (but see **N7** on the count of duplicated numbers).
- **S11 — the barred 1525 language.** `grep -c "smite, slay"` over the whole document returns **0**. The bar at 7.4 is now stated without reproducing the phrase, and attributes the bar to R94. Fixed correctly, and by the better of Round 1's two suggested routes.

## (b) The new entry 2.10

- AC Article II verified to occupy **lines 192–207** exactly (heading at 192, Article III's heading at 208), which is what §13's corrected AC row now claims.
- Both quotations in the preliminary definition are verbatim: "since the fall of Adam all men begotten in the natural way are born with sin, that is, without the fear of God, without trust in God, and with concupiscence; and that this disease, or vice of origin, is truly sin" and "who deny that original depravity is sin, and who... argue that man can be justified before God by his own strength and reason."
- **Propagation checked by script, and it is complete:** §10.1 has a new "Melanchthon-only, as read (1)" category containing 2.10; §10.2 cluster 1 includes it; the 38→39 Tier 1 count and the 71→72 entry count reproduce (my recomputation: **39 Tier 1 / 27 Tier 2 / 6 Tier 3 = 72**, in both the bodies and the Appendix); the enumerated Tier 1 list in §10.2 is exactly the computed Tier 1 set; 39/72 ≈ 54% is correct; the Appendix has a new row 2.10 that agrees with the body on every column; §11 item 2 now declares AC I and III as the remaining gap and records II as read; §12 and §13 both restate coverage accordingly; §13's word count (24,689 by `wc -w`) reproduces exactly. The entry's own coverage note (AC II alone, not cross-checked against the catechisms or the Apology) is an honest and correct limitation. The only propagation miss found anywhere in the document is **N6**, and it is not 2.10's.

## (c) The [PV] restoration

- Framework para 97 read directly from `reference/L3B-World-Build-Methodology/CiC_L3B_Interpretive_Lexicon_Development_Framework_V2.1.docx`: "The term or concept is important within some streams, voices, or periods of the world but is not universally representative across the whole reconstructed ecology." §0's **quotation** of it is accurate, including "periods." The narrowing S12 found is gone from the quoted definition. See **N4** for what remains.
- [PV] now sits on three entries (5.6, 6.7, 7.4) — confirmed by script against the bodies, and §10.1's PV paragraph lists exactly those three. 5.6's and 6.7's PV cases are genuinely demonstrated (1520/1522/1530 on the mass; polemical vs confessional naming of the adversary) and both are quoted at their cited loci. 7.4's new tag is defensible on the Framework's own "not universally representative across... periods" wording — but see **N4**.
- 5.7 and 8.2 both carry explicit "PV considered and not added" notes, as §13 claims. They are logged and locatable; the reasoning in 5.7's is the weak one (**N4**).

## (d) The extended §13 discovery ranges

I extracted all **606** distinct file+line citations from the entry bodies by script and tested each against §13's declared ranges. Result: **every one of Round 1's five falsified loci is now inside a declared range** — v1 10661/10681/10727 inside the new 10600–10750; v2 15816–15819 inside the new 15816–16042; Ap 4729 inside the new 4700–4730; LC 1630 inside the new 1615–1730. The extensions are real, not nominal: I re-opened each range boundary and each cited locus.

Of the 606, 23 fell outside a declared range. Thirteen are checker artefacts (years and occurrence-counts parsed as line numbers — "the 1525 tract," "Schindel's 1930 English," "184 occurrences," and similar). Nine are loci the document itself explicitly flags as not re-read this pass and cites to a Registry row as a pointer (2.2's Co 15139–15141, 3.5's v3 14586–14594, 4.9's Hy 558–561 and 766–768, 6.8's Co 16090–16091, 6.9's LC 3504, 7.4's v3 10554–10594, 9.1's v1 3994) — all correctly disclosed, which is the discipline working. **One is genuinely undeclared and unflagged: v1 12378 (see N8).**

## (e) S13's AS-scope disclosure and S14's corrected Doc_01 citations

- Doc_01 §8 verified to name **six** neighbours at §8.1–§8.6, exactly as §0 now states, with §8.6 (the Augustinian Hermits) described there as this world's seedbed and not as a separate built world — which is how §0 characterizes it. §11 item 5 now carries all three untested neighbours forward. The "most consequential gap" framing (the monastic-vocabulary entries 8.1, 8.2, 8.4, 8.5) is sound, and §11 item 5 correctly notes that 8.1 and 8.5 are [SC] rather than [AS] and that the seedbed question bears on that decision too. See **N2** for the one clause that does not hold.
- **S14 at 3.4 and 6.2.** Doc_01 §8.0's sentence reads: "Scripture's own authority against institutional hierarchy is the clearest case: this world shares that refusal with both the Reformed cities and the Anabaptist movements, but pairs it with territorial-magisterial authority..." Both entries now describe §8.0's claim accurately and narrowly, attribute the broader comparative judgment to this drafting pass rather than to Doc_01, and route it to the neighbours' own Doc_03s. 6.2's note correctly records that its case is the weaker of the two. Fixed correctly, and the fix is better than the minimum Round 1 asked for.

## (f) Fresh independent citation sample — 24 citations, zero defects

Chosen from entries and Evidence lines untouched by any Round 1 finding, spread across the five clusters named in the review requirement, and re-opened by hand at the stated lines:

§1 — 1.2 AC 344–349; 1.3 v2 8968–8971; 1.5 Hy 975–978; 1.6 v2 2388–2392; 1.7 v1 2269–2270.
§4 — 4.1 TT 2394–2395; 4.2 LC 333–336; 4.4 LC 408–416; 4.7 LC 4460–4463.
§5 — 5.3 SC 496–500 and LC 4075–4077; 5.5 v2 6787–6791; 5.6 v2 14846–14848; 5.8 LC 2840–2843; 5.10 SC 414–417; 2.1 LC 3916–3921; 3.1 v2 14864–14866 and its footnote glosses at v2 15752, 15754.
§8 — 8.1 AC 1110–1115; 8.2 v3 20906; 8.4 LC 1630; 8.5 AC 1233–1239; 8.6 v2 15986–15989.
§9 — 9.4 Hy 979–981; 9.5 TT 3147–3148; 9.7 TT 3011–3015.

**All 24 verify exactly at the stated lines, quoted words included.** Four are worth naming because they test the document's harder disciplines rather than simple string presence:

- **5.3's [AS] wording claim survives a real test.** The Large Catechism at 4075–4077 says "in and under the bread and wine"; the Small Catechism at 496–500 says "under bread and wine," without "in and." The document quotes each to its own file and does not merge them — precisely the cross-text conflation that produced S1.
- **4.2's "typo as found"** reproduces `ma-servants` exactly.
- **5.10** reproduces the Small Catechism's own missing full stop ("admits his sin Second, a person receives absolution") as found.
- **C3's added footnote loci** are right: v2 15752 reads "[4] Right to speak." and 15754 reads "[5] Power to do."

I also independently re-verified three of Round 1's own layer attributions, since the document's Discipline 2 depends on them: v1's contents page attributes the *Treatise on the New Testament* introduction to **J. L. Neve** and *The Papacy at Rome* introduction to **T. E. Schmauk**; v1 10636 and 12218 are the two INTRODUCTION headings in question. Both attributions hold, so 6.2's and 6.8's "this is editorial, not Luther's" claims are correctly grounded.

**Other claims re-run and confirmed:** *Anfechtung* occurs exactly once across all ten files, at v2 5418, in a footnote citing the 1521 *Gravamina* ("Von anfechtung der cordissanen") about attacking benefice titles — 9.2's C10 fix is exact. "Popedom" occurs seven times: six in Bell's Table Talk (589, 1934, 3063, 3147, 3198, 3253) and once lowercase at v1 12378 in Schmauk's introduction — 6.7's C5 fix ("chiefly Bell," six of seven) is exact. The S4 confidence vocabulary, unapplied at Round 1, is now applied 21 times: [Inferential/Thin] on all ten [AS] entries plus 3.4, 6.2 and §0's summary statement, [Contested] on both [CT] entries, and [Documented] six times including all three [PV] entries and 2.10. Both [CT] entries state a contest type drawn from the Framework's own four (paras 106–109), read directly from the .docx.

---

# (g) The "85 vs 82" question — counted independently

**The original document's 85 is correct. Round 1's cosmetic finding C4 is wrong. The revision's re-verification, including its breakdown, is correct.**

My own counts against `cic/texts/luther_works-v3-selected_various1930.txt`:

| Count | Command | Result |
|---|---|---|
| case-insensitive occurrences | `grep -o -i "secular" \| wc -l` | **85** |
| lowercase `secular` | `grep -o "secular"` | **44** |
| capitalised `Secular` | `grep -o "Secular"` | **38** |
| all-capitals `SECULAR` | `grep -o "SECULAR"` | **3** |
| matching lines | `grep -c -i "secular"` | **83** |

44 + 38 + 3 = 85. The three all-capitals occurrences are at lines **109** (contents entry), **11655** (running head) and **11794** (work title) — all genuine occurrences of the word in the volume's English, differing only in typography. Round 1 reached 82 by summing the lowercase and capitalised forms only; the all-capitals form is a distinct case-sensitive string that neither `grep -o "secular"` nor `grep -o "Secular"` matches, so it was silently dropped. Round 1's own report carries the tell: it states "44 lowercase + 38 capitalised = **82** (83 matching lines)" — 82 occurrences cannot appear on 83 lines. The revision is right to decline the correction, and right to state the breakdown so the count is re-runnable rather than asserted.

**A second, unreported instance of the same thing in the same sentence.** Round 1's C4 also stated that v1+v2 contain "temporal" **181** times. I count **184** — v1 82, v2 102 — which is exactly what the revision now states, along with "secular" 4 times in v1+v2, "all in v2" (v1 = 0, v2 = 4). So the revision silently corrected a second Round 1 count while adopting the rest of C4. Correct in substance; it would have been better to say so, since an undisclosed divergence from a review finding is the thing this project's Doc_02 citation-fix history warns about. Not raised as a finding — the figure is right and the document does not claim to be reproducing Round 1's number.

---

# NEW SUBSTANTIAL FINDINGS

## N1 — The new [PV] tag on 7.4 did not propagate to the Appendix, and §13's script-verified agreement claim is false

**What I checked.** I recomputed tier, Origin tag and Risk/Function tag for all 72 entries from the bodies and cross-checked them against all 72 Appendix rows by script.

**What the document claims.** §13, first bullet:
> "72 entries (39 Tier 1 / 27 Tier 2 / 6 Tier 3 — recomputed by script, **body and Appendix agree on all 72**)"

and:
> "All statistics restated after these changes were independently recomputed by script (`verify_doc03.py`: entry count, tier counts, and full body-vs-Appendix cross-check) rather than hand-counted forward from the prior revision's figures."

**What I found.** 71 of 72 rows agree exactly. One does not:

| | Origin | Risk/Function | Tier |
|---|---|---|---|
| **7.4 body** (`- **Tags.** [SC] [DR] [RT] **[PV]**`) | SC | DR, RT, **PV** | 2 |
| **7.4 Appendix row** (`\| 7.4 \| insurrection / common man (1522) \| SC \| DR RT \| 2 \|`) | SC | DR, RT | 2 |

The Appendix's Risk/Function cell for 7.4 omits PV. The comparison entries show this is a miss, not a convention: 5.6's cell reads `DR TC RT PV` and 6.7's reads `DR RT PV`, so PV is carried in that column everywhere else it exists.

**Why it matters.** Two ways, and the second is worse than the first. First, the Appendix is the filtering surface — §13 offers it as the way a builder finds all [PV] entries without reading 72 entries, and a filter on that column now returns two of three. The one it drops is the entry whose own distortion flag says a later period's reputation will be projected onto it, which is the flattening [PV] exists to route to Internal Plurality review.

Second, and this is the finding: **§13 states that this exact cross-check was run by script and came back clean, and it does not come back clean.** Round 1's single most praised result was "the Appendix agrees with the entry bodies on tier, Origin tag and Risk/Function tag for all 71 rows, zero mismatches — an unusually clean result." This revision inherits that claim, extends it to 72, attributes it to a named script, and it is now false by one cell — introduced by the S12 fix itself. A stated, named, script-attributed verification that does not reproduce is a warrant defect of the same family as S5, and it lands on the one statistic a reviewer would otherwise be most entitled to take on trust.

**Fix.** Add PV to the Appendix's 7.4 Risk/Function cell. Separately, re-run `verify_doc03.py` and establish why it passed — if the script does not in fact compare the Risk/Function column, §13's description of what it checks is also wrong and should be corrected to what it actually does.

---

## N2 — §0 cites Doc_01 §8.4 for a finding §8.4 does not contain, and that Doc_01's own review had already corrected away

**What I checked.** §0's tag-key sentence disclosing the [AS] scope limitation, against Doc_01 §8.4 and §8.5 read in full.

**What the document claims.** §0, in the S13 fix:
> "The Society of Jesus (§8.4) and Lollardy (§8.5) were not tested — **Doc_01 itself finds no documented direct vocabulary relationship to either**, but that is not the same as a comparative test having been run."

**What I found.** For Lollardy (§8.5) this is a fair gloss: Doc_01 says it "finds no documented direct contact and, per the same discipline as §8.4, does not assert a 'forerunner' relationship it cannot source."

For the Society of Jesus (§8.4) it is not. Doc_01 §8.4 says the opposite of what is attributed to it, and says so in a passage that exists precisely because the claim now being cited was struck:

> "**Substantially revised in Round 1 (finding S13): the original draft stated 'this is not a rival-by-direct-argument relationship' and 'no documented direct link,' reading only this world's own Step 0 and the census. The Society of Jesus's own Step 0 (§2 A3), now read, states the relationship from the other side in direct terms: 'The direct, real rival relationship in this batch is Lutheran Wittenberg and the Reformed cities — the Jesuits were founded explicitly within, and as a response to, the same crisis those two candidates answer from the opposite direction.'**"

What Doc_01 §8.4 actually records as absent is narrower and different: "no documented *personal* contact between Luther and the Society's own founders exists." It makes no claim about vocabulary in either direction, and it explicitly characterises the Society as "not a movement in mutual isolation from this one."

**Why it matters.** Three ways.

First, it is the S14 pattern one fix later: a proposition sourced to a sibling document that the sibling document does not state. Round 1 graded that substantial at 3.4 and 6.2, and noted it had already recurred once from Doc_01's own S1/S4/S5. It has now recurred inside the fix for a different finding.

Second, it is the *superseded* wording that is reproduced. Doc_01's pre-revision draft said "no documented direct link"; Doc_01's Round 1 struck it; Doc_03 Revision 1 reintroduces its substance as a current Doc_01 finding. A reader following the citation finds a paragraph whose entire purpose is to say that this is no longer the document's position.

Third, it weakens the disclosure it is attached to. §0's disclosure is otherwise good — it names the untested neighbours and flags the Augustinian Hermits as the most consequential gap. But attaching "Doc_01 finds no documented relationship anyway" to the Society softens a gap that Doc_01, as revised, makes *larger*: VI.11 is on its own Step 0's account a direct rival answering the same crisis from the opposite direction, which is exactly the adjacency profile under which an untested [AS] claim is most likely to be wrong. The one clause that looks like reassurance is the one place the disclosure should be sharpest.

**Fix.** Drop the clause, or split it: for Lollardy, cite §8.5's actual "no documented direct contact"; for the Society of Jesus, state §8.4's actual position — a direct rival relationship per VI.11's own Step 0, with no documented personal contact between Luther and the Society's founders, and no vocabulary comparison attempted by either document. Nothing else in the disclosure needs to change.

---

## N3 — §12 claims Neve's introduction was read "in full" at a range that stops short of its end

**What I checked.** §12's "Read in full this pass" list against the v1 file's own structure, prompted by the fact that this is the range the S5 fix extended.

**What the document claims.** §12:
> "Read in full this pass: ... **Neve's introduction to *A Treatise on the New Testament* in full (v1 10600–10750, extended at Round 1 S5)**"

**What I found.** In `luther_works-v1-selected_jacobs-spaeth1915.txt`, the INTRODUCTION heading for this treatise is at line **10636**, and its prose is still running at 10745–10760 ("The object of faith is the Gospel, i. e., the promise of the forgiveness of sins contained in the Words of Institution..."), continues past the declared range, and reaches its FOOTNOTES block at **10836**. The introduction is roughly 10636–10835 plus footnotes; the declared range covers 10600–10750, ending about 85 lines and several paragraphs before it closes.

**Why it matters.** This is the mildest of the five substantial findings and I record it with its mitigation stated first: all three loci the S5 fix existed to cover (10661, 10681, 10727) are comfortably inside 10600–10750, so no citation in the document is unwarranted by it, and nothing is misquoted. The defect is in the coverage statement, not the evidence.

But §12 is the section whose whole function is to say what may and may not be relied on, and the sentence immediately following this list is "Saturation is claimed only for the sections read in full." Adding an item to that list that was not read in full is the S5 defect in its other direction — S5 was citations outside the declared record, this is a declared record claiming more than the range supports — and it was introduced by the S5 fix. §13's own v1 row is more careful: it says "10600–10750 (Neve's introduction to *A Treatise on the New Testament*, extending the range)" without the words "in full." §12 and §13 should not disagree about what was read.

**Fix.** Either extend the range to 10636–10900 and confirm the rest was in fact read, or strike "in full" from §12 and describe the range as what it is — the part of Neve's introduction covering the cited loci. Do not leave §12 and §13 stating different things.

---

## N4 — The restored [PV] key still substitutes "registers" for the Framework's "streams," and 5.7's decline is reasoned from register count rather than the Framework's own test

**What I checked.** Lexicon Framework V2.1 para 97 read directly from the .docx, against §0's restored tag key and against the three "considered" entries (5.7, 7.4, 8.2).

**What the Framework says (para 97, verbatim).**
> "The term or concept is important within some **streams, voices, or periods** of the world but is not universally representative across the whole reconstructed ecology. This tag should trigger explicit attention during Internal Plurality review (per the Template) rather than silent flattening into one position."

**What the document says (§0, after the fix).** It quotes para 97 accurately — and then restates the operative test as:
> "applied where the vendored **registers**, voices, **or periods** demonstrably differ, not where one is merely silent"

**What I found — two connected things.**

**(a) "Streams" has become "registers," undisclosed.** S12's whole subject was a silent substitution in this same definition: "periods" dropped from the operative test while the Framework's definition was presented as adopted. The fix restored "periods" and left the other substitution in place. A stream in the Framework's sense is a sub-tradition or party within the world's ecology; a register in this document's sense is a genre of one author's output (§0 Discipline 3's nine). They are not the same category, and the document has a perfectly good answer available — Doc_01 §6 found this world **strand-singular**, so there are no streams to test, and registers are the nearest available proxy. §0 makes that argument nowhere. As it stands, the fix for an undisclosed narrowing leaves a second undisclosed narrowing of the same definition, in the same sentence.

**(b) 5.7's decline applies the register test, which is not the Framework's test.** 5.7 (transubstantiation) reads:
> "**PV considered and not added (Round 1 S12's list):** the entry is single-register by the AG line below, not multi-register, so no plurality is demonstrated in what was read — a coverage gap, not a shown difference."

The Framework does not ask how many registers attest a term. It asks whether the term or concept is "important within some streams, voices, or periods... but not universally representative across the whole reconstructed ecology." On that test 5.7 has an in-text case the note never engages: the entry's own evidence is Luther **permitting others a position he refuses** — "only let them not press us to accept their opinions as articles of faith" — which is the vendored text itself testifying that the world contains people who hold transubstantiation and people who do not. That is a plurality attested in the library, not an argument from silence, and it is the kind a Representative could flatten in either direction. It may still be right to decline the tag; but it should be declined on the Framework's test, having engaged that sentence.

8.2's decline is sound on any reading and needs no change. 7.4's new tag is correct on the Framework's own "not universally representative across... periods," though I note for the record that it sits awkwardly with §0's own "not where one is merely silent" clause: what is demonstrated at 7.4 is that the term is *confined* to 1521–22 in this library, with the other periods silent rather than different. The Framework's wording carries it; §0's restatement, read strictly, does not. That is a further symptom of (a) — the restatement and the definition it quotes are still not the same test.

**Why it matters.** S12 was graded substantial because narrowing a Framework tag definition unilaterally is a methodology change, which CLAUDE.md's default-actions table routes to "Always ask." §13's escalation check now states that "this revision restores the Framework's own definition rather than adopting or escalating the narrowing, so no methodology variance is being proposed." That statement is not yet fully true. Either the restatement matches the Framework, or the divergence is named and justified (strand-singularity is a good justification) — but the escalation check should not record "no methodology change" while an unexplained substitution remains in the operative test.

**Fix.** Either restate the test in the Framework's own terms, or keep "registers" and add one clause saying why — that Doc_01 §6's strand-singular finding leaves no streams to test, so registers stand in for streams in this world. Re-test 5.7 against the Framework's wording and against its own "let them not press us" evidence, and record whichever answer results. Adjust §13's escalation check to match.

---

## N5 — Round 1's fixes are logged inline throughout the entry bodies, which is change history embedded in a canonical-surface document

**What I checked.** The document as a finished artifact, against CLAUDE.md's "Keep the live/canonical surfaces clean."

**What the rule says.** `World-Builds/` holds "the canonical construction documents... once approved to proceed," and the documents listed there "contain only what runs the program or constitutes the finished record — **no notes, commentary, change history, review discussion, or process narration embedded in them**... Notes, decision logs, audit trails, adversarial-review rounds... belong in `Ministry/`... If you find commentary, changelog cruft, or leftover process notes in a live/canonical file, treat that as corruption."

**What I found.** Revision 1 carries roughly thirty inline fix markers inside the entry bodies, §10 and §11 — "**corrected, Round 1 S10:**", "**cosmetic C8:**", "**added, Round 1 S12:**", "a prior draft of this entry had carried..." — several of them multi-sentence. The heaviest is 7.1's [CT] paragraph, where the statement of the contest type is now preceded by a five-line account of what a prior draft claimed and why it was wrong; 3.4's and 9.6's tag and voice lines are similar. The document is a candidate list a downstream builder reads for terms, and a reader of 7.1 must now walk through review narration to reach the contest statement.

**The tension, stated honestly, because it is real.** This is not a blunder. §13's own review requirement asked for exactly this ("each fix is also marked inline in its entry... so a reviewer can locate every fix without re-reading the whole document"), and it worked — it made this recheck faster and cheaper, which is what the usage discipline asks for. The rule as written also binds documents "once approved to proceed," and this one is explicitly DRAFT, Revision 1, disposition none claimed. So the markers are legitimate *now*.

**Why it is a finding anyway.** Because there is currently no step that removes them. §13's fix log already records every fix, finding by finding, in the place the rule says such things belong; the inline copies are a second, redundant audit trail living in the canonical surface. If this document reaches "Approved to proceed" in its present shape, thirty change-history annotations become permanent canonical content, and the rule's own instruction at that point ("treat that as corruption: remove it, don't add to it") will fall on whoever notices next rather than on the thread that added them. The same pattern is already visible in `witt_Source_Registry.md`, which is APPROVED TO PROCEED and carries round-by-round fix narration in its header and inside row R30's cells.

**Fix.** Not now — the markers have done their job for this round. Before disposition, strip the inline markers and let §13's fix log carry the record, keeping inline only what is substantive content in its own right (for example, 9.6's statement that the hymn does not name the order, and §0's warning about the file's thesis numbering, both of which are findings about the sources rather than about prior drafts). Raise the Registry's own case separately with its owner; it is not this thread's file to edit.

---

# NEW COSMETIC FINDINGS

**N6 — §11 item 5 still says "ten of seventy-one."** The S6 fix updated the entry count from 71 to 72 everywhere else I could find it by script — §10.2, §12, §13, the Appendix — but §11 item 5 reads "The [AS] tags (2.6, 2.7, 4.2, 4.4, 5.3, 6.1, 7.1, 7.5, 8.2, 8.4 — **ten of seventy-one**)". The ten-entry list itself is correct and matches my recomputation exactly. Change to seventy-two. (This is the only stale count I found; §13's several references to "71 original entries" are correct in their context, since they describe Round 1's findings.)

**N7 — §0 names three duplicated thesis numbers where the file has four, and the missing one is the number at issue.** Discipline 1's new S10 warning says the vendored Theses file "prints '36.', '13.' and '73.' each twice." Enumerating every printed thesis number in v1 1139–1602 returns **four** duplicates: 13 (1198, 1201), 36 (1249, 1285), **53 (1348, 1352)** and 73 (1419, 1422). The omitted one, "53.", is exactly the number 1.1 and 9.3 cite and correct. The entries themselves are right — both say the file prints "53." — so this is a gap in the general warning, not in the citations. Worth fixing precisely because §0's stated purpose there is to warn a downstream builder about the trap.

**N8 — v1 12378 is cited outside every declared read range, unlike the comparable Ap 4729.** 6.7's C5 fix adds "it also occurs once at **v1 12378**, lowercase, in Schmauk's 1915 introduction." I verified the locus and the attribution (the Papacy at Rome introduction begins at 12218; the contents page at line 69 attributes it to T. E. Schmauk) — the claim is correct. But 12378 falls in the gap between §13's v1 ranges 10905–11094 and 12775–12974, and carries no "not re-read" flag. It is presumably covered by §13's `builder-grep` row, which does list "Popedom" among the strings swept — but the document set its own standard one row above when it extended the **Ap** range to 4700–4730 to cover a grep-located line for exactly this reason. Either extend the v1 row by a few lines or say the locus is grep-located, so the same class of citation is treated the same way twice.

---

# What a Round 3 check should and should not do

Not a re-review. If the fixes above are made, the checkable surface is small:

1. **N1** — re-run the body-vs-Appendix cross-check by script and confirm 72/72, and confirm the script actually compares the Risk/Function column.
2. **N2, N3** — re-read the two corrected sentences against Doc_01 §8.4/§8.5 and against v1 10636–10836. Both are single-sentence checks.
3. **N4** — read §0's restated [PV] test, 5.7's re-reasoned decline, and §13's escalation check together; they must say the same thing.
4. **N6, N7, N8** — three arithmetic/locus checks.
5. **Do not re-run the 606-citation sweep or the fresh sample** unless Evidence lines change again. Both came back clean this round, and the fixes above touch §0, §11, §12, §13 and one Appendix cell — not the evidence.

**Disposition: none claimed by this review.** Under the project's governance rule, no finding above may be closed by self-certification; each needs independent re-confirmation.
