# Doc_03 Review — Round 1 (independent adversarial review, cold)

**Document under review:** `witt_Doc_03_Lexicon_Candidate_List.md` (DRAFT, Revision 0), Lutheran Wittenberg & Its Congregations (Atlas VI.1, `witt`).
**Reviewer:** independent, no drafting involvement, no prior context on this document.
**Date:** 2026-09-15.

**Method.** All 820 lines of the document read. The three context documents read (Doc_01, Doc_02 §§1–2 and §§12–17, the Source Registry header, summary statistics and the rows Doc_03 cites). The two governing frameworks read directly from the `.docx` via python-docx: CF V7.4 paras 620–645 and 340–360; Interpretive Lexicon Development Framework V2.1 paras 30–124 (Parts I and II in full, Part III's Tier 1 opening only). Citations were checked two ways, per the project's two-independent-methods discipline: (a) a script built a whitespace- and bracket-normalised index of all ten vendored files, extracted all 316 quote/locus pairs from the entries' Evidence lines, and tested each quoted fragment against the cited file and line range; (b) roughly 45 citations spread across all nine thematic clusters and all ten files were then re-opened by hand and read in context, to catch what a string match cannot — wrong voice, editorial layer presented as primary, correct words at a locus that does not support the claim. All internal statistics (entry counts, tier counts, tag counts, the §10.1 Author Gravity lists, the §10.2 Tier 1 enumeration, and the whole Appendix against the entry bodies) were recomputed by script. Term-count and absence claims were re-run with `grep`.

---

# VERDICT: SUBSTANTIAL REVISION REQUIRED

**14 substantial findings. 10 cosmetic findings.**

**What is genuinely strong, stated first, because it is unusual and should not be lost in revision.** Citation accuracy in this document is far better than this project's documented baseline. Of 316 quote/locus pairs in the Evidence lines, 266 matched at the exact cited lines on the first automated pass; of the 50 flagged, 44 were artefacts of the checker (thesis numbers, dates and Registry row numbers parsed as line numbers) or citations the document itself already marks as not-re-read, and hand-checking cleared them. The OCR-as-found quotations at 2.9 (Co 755–762), 3.3 (Co 803–806), 7.1 (v3 12371–12374, Co 14748–14750) and 8.5 (v3 12427–12428) reproduce the degraded files **character for character**, including `miUtatingagainst`, `asser- tioQ^`, `two kin ee`, `is a i report`, and `counsels!` — this is exactly right and should be preserved verbatim through revision. The "typo as found" flag at 4.2 (`ma-servants`, LC 334–336) is accurate. The translator attributions are correct in every case I tested against the volumes' own contents pages: Jacobs for the Theses and *Christian Nobility* (so the sidenote at v2 2171 is his), Steinhaeuser for *Babylonian Captivity* and the *Magnificat* (so the sidenote at v2 6713 and the *Gewissen* footnote at v3 7180 are his), Steimle for the Wittenberg Sermons, *The Papacy at Rome* and the *Answer to Emser*, Schindel for *A Treatise on the New Testament* and *Secular Authority*, Lambert for *Doctrines of Men*, the *Earnest Exhortation* and the Teutonic Order piece, Neve for the introduction at v1 10681. The Appendix and the entry bodies agree on tier, Origin tag and Risk/Function tag for all 71 entries with **zero** mismatches. The boundary discipline is clean: no Excluded row is used as a source for any candidate term, nothing is drawn from Zell, and the 7.4 entry's restriction to the 1522 *Earnest Exhortation* holds. And Discipline 2's central claim — that no German or Latin lemma is supplied from general knowledge — **survives testing**: I checked *Taufe*/*tief* (v1 2254–2257), *Aus der Taufe gehoben* (v1 2275–2276), *Gemeinde*/*Christenheit*/*Versammlung* (LC 2822–2858), *Gemeinden* (v1 10944), *Bussetun* (v1 1523), *Gewissen* (v3 7180), *Mein Wort* (v3 11232), *Geysterey* (v3 21027), *Menschenlehren* (v2 15819), *Zur Halfte... geistlich* (v1 14770), *characteres indelebiles* (v2 2227–2228), *Accedat verbum ad elementum* (LC 3861), *opus operatum* (v2 7289–7290), *jus verbi*/*executio* (v2 14864–14865), *meritum congrui*/*condigni*, *prima gratia*, *Ascensus mentis ad Deum*, *Der alt' boese Feind* (Hy 3712) — every one is present in the vendored text at the cited locus. The absence claims for *sola fide*, *sola scriptura*, *sola gratia*, *simul justus et peccator* and "theology of the cross" are correct (zero occurrences across all ten files).

**Why revision is nonetheless substantial.** Four things break: one Apology quotation is materially misworded in a way that conflates two different confessional texts (S1); a personal identification is asserted that the vendored text does not contain (S2); an entire governing principle of the Lexicon Framework — confidence calibration — is unapplied, in a document whose two predecessors apply it 22 and 69 times respectively (S4); and the document's own read-record and coverage-limit statements, which are the load-bearing warrant for every other claim in it, are falsified at six places (S5, S6). The last is the most consequential: this document asks to be trusted on the strength of §13's record of what was and was not read, and that record is not accurate.

---

# SUBSTANTIAL FINDINGS

## S1 — 6.8: an Apology quotation materially misworded, conflating the Apology with AC Article V

**What I checked.** The Evidence line at 6.8 (sects / "new spirits" / fanatics), specifically `Ap 4729, 6492–6495`, read in the vendored Apology file.

**What the document claims.**
> `Ap 4729, 6492–6495 ("fanatical men, who dream that the Holy Ghost is given without the Word... as the Enthusiasts formerly taught" — located by grep, read in its lines only)`

**What I found.** `melanchthon_apology-augsburg-confession_bente-dau1921.txt` lines 6491–6496 read:

> `so far as can be done, to adorn the ministry of the Word with every`
> `kind of praise against fanatical men, who dream that the Holy Ghost`
> `is given not through the Word, but because of certain preparations of`
> `their own, if they sit unoccupied and silent in obscure places,`
> `waiting for illumination, as the Enthusiasts formerly taught, and the`
> `Anabaptists now teach.`

The words inside the document's quotation marks are not the Apology's. The Apology says the Holy Ghost is given **"not through the Word, but because of certain preparations of their own"**. The document prints **"without the Word"**. That phrase comes from a different text — the Augsburg Confession Article V, at AC 253–255: *"They condemn the Anabaptists and others who think that the Holy Ghost comes to men without the external Word, through their own preparations and works."* AC 253–255 is cited in the same Evidence line, three citations earlier. The drafting pass has carried AC's wording into a quotation attributed to the Apology.

Two further consequences. First, the ellipsis conceals the deletion of twenty-two words, including the whole vivid clause ("if they sit unoccupied and silent in obscure places, waiting for illumination") that is the Apology's actual characterisation of the charge — precisely the "world's own imagery" the project's writing standard exists to protect. Second, the document's own Tags line for 6.8 builds a distortion flag on the phrase — *"'enthusiast'/'fanatic' in modern hearing vs. a specific theological charge (the Spirit 'without the external Word')"* — and that phrase is AC's, not both voices'. As written, the entry makes it look as though Luther's catechesis, AC and the Apology converge on one formula. They do not: AC says "without the external Word," the Apology says "not through the Word, but because of certain preparations of their own," and the difference is the kind of cross-voice wording variation this document is otherwise careful to record (compare its good handling of 6.4 calling/office/estate).

**Why it matters.** This is a misattributed and mis-transcribed quotation of exactly the type CLAUDE.md names as "a real, recurring defect here," at the seam between the two voices this world's Author Gravity analysis turns on. It also sits on a boundary: 6.8 is the entry that names the people Doc_01 §8.2 records this world's own authority as having helped suppress. A Representative reciting "without the Word" as the Apology's charge would be putting a confessional formula in Melanchthon's mouth that he did not write there.

**Fix.** Quote the Apology as it reads, or quote AC 253–255 and attribute it to AC. Separate the two formulations in the entry and record the difference, rather than merging them.

---

## S2 — 9.6: "two Augustinians" is not in the vendored text

**What I checked.** The Preliminary definition at 9.6 (martyr — "the two youths"), against hymn V and its heading in `luther_hymns_bacon-allen.txt` (Hy 1741–1870), plus a `grep -i augustin` sweep of the whole hymns file.

**What the document claims.**
> **Preliminary definition.** The library's one martyrology: **two Augustinians** "burnt at Brussels by the Sophists of Louvain," who "For God's dear Word... shed their blood"...

**What I found.** Every quoted phrase is exact — the heading at Hy 1744–1745 ("A Song of the Two Christian Martyrs burnt at Brussels by the Sophists of Louvain in the year MDXXII [July 1, 1523]"), "For God's dear Word they shed their blood" (1763), "They won the crown of martyrs" (1767), "Their monkish garb from them they take" (1789), "True priests of God's own making" (1800). But the word **"Augustinian" does not occur anywhere in the hymns file** in connection with these men. The only hit for `augustin` in the entire file is at Hy 1078, about the works of St. Jerome and St. Augustine. What the vendored text supplies is: "two youths" (1756), "One of these youths was called John, / And Henry was the other" (1759–1760), "monkish garb" and "gown of ordination" (1789–1790), "all monkish follies" (1807). The text says they were monks. It does not say which order.

The identification is correct history — Hendrik Vos and Johann van Esschen were Augustinian friars — which is exactly the problem: it is correct *general knowledge about Luther*, imported into a document whose Discipline 1 states that "every term below was found in a passage read in a vendored file during this pass" and whose governing rule is "if a detail isn't derivable from the completed world, it doesn't belong."

**Provenance, and a defect that has propagated.** This does not originate with Doc_03. Source Registry row R30's Licensed For column reads *"non-founder participants (the two Augustinian friars)"* — while its own Verification Note lists only what was verified verbatim in the hymn, and "Augustinian" is not among those items. So an unsourced identification entered an APPROVED TO PROCEED Registry and has now been inherited into Doc_03 without a flag. Doc_03 is not free to rely on it: R30 is a pointer, and CLAUDE.md is explicit that "a record marked 'quotes verified' is a claim to re-check, not a fact to trust."

**Why it matters.** A Representative built downstream of this entry would be able to state the friars' order as something this world's own library says. It does not. This is the small, plausible, checkable kind of invention the "never invent" rule is aimed at, and it is worse for being true.

**Fix.** Say what the text says — two young monks, named John and Henry, stripped of "monkish garb" — and if the order is to be carried at all, carry it as an unattested detail with a stated source, not inside the preliminary definition. Raise R30's wording separately with the Registry owner under its append-only discipline.

---

## S3 — 9.6: the Author Gravity flag contradicts the entry's own Voices and Evidence lines

**What I checked.** 9.6's AG flag against its own Voices line, its Evidence line, the Appendix row, and the vendored AC file.

**What the document claims.** Three statements inside one entry, plus the Appendix:
- **Evidence:** `... AC 765–766.`
- **Voices:** `Luther — hymn (Bacon's English throughout); Melanchthon — AC.`
- **AG:** `Luther-only, single-register (hymn V), in a translator's rendering — the weakest evidentiary base of any entry, flagged accordingly.`
- **Appendix row 9.6, Voices column:** `L (hymn) M`

**What I found.** The Voices line, the Evidence line and the Appendix all assert two voices; the AG flag asserts one. That is an internal contradiction on its face. Re-checking the source resolves it against the Evidence line, not the AG flag: `grep -i martyr` over `melanchthon_augsburg-confession_anon-pg275.txt` returns **zero hits**. AC 765–766 reads:

> `But now men, and that, priests, are cruelly put to death, contrary to`
> `the intent of the Canons, for no other cause than marriage.`

That passage is about the execution of married priests. It does not use the word "martyr" and does not attest the candidate term. So the AG flag ("Luther-only") is the correct call, and the Evidence and Voices lines are the error: they cite and credit a passage to a term it does not carry.

**Why it matters.** §10.1 is explicitly offered as the input Doc_04 will use to decide which vocabulary is safe, and §13's own review request asks specifically for AG attributions to be checked against the texts. An entry whose three attestation statements disagree with each other cannot be used as that input. It also means the Appendix's `L (hymn) M` overstates the evidentiary base of the entry the document itself calls "the weakest of any entry."

**Fix.** Drop AC 765–766 from 9.6's Evidence, correct the Voices line and the Appendix row to Luther-only, and if the AC passage is worth keeping, keep it where it already correctly sits — at 8.3 marriage, where the document cites AC 765–766 for exactly this content.

---

## S4 — The five-level confidence vocabulary is not applied anywhere in the document

**What I checked.** Lexicon Framework V2.1 paras 41–43, then a count of confidence tags in Doc_03, Doc_02 and Doc_01.

**What the Framework requires.** Para 41–43, in the Framework's front matter governing all Parts:

> **Confidence Inheritance Principle** — "Lexicon entries inherit the confidence discipline governed by the Template and Construction Framework. A lexicon entry's claims about how a term functioned should be calibrated using the constitutional five-level confidence vocabulary — Documented, Widely Accepted, Dominant Modern Reconstruction, Contested, Inferential/Thin..."

CLAUDE.md states the same requirement independently: "Contested or uncertain claims get tagged with the project's five-level confidence vocabulary."

**What I found.** Doc_03 contains **zero** instances of any of the five terms. For comparison, on the same grep, `witt_Doc_01` has 22 and `witt_Doc_02` has 69. The document's §0 lists what it applies from the Framework — "Part I (Candidate Discovery) and Part II (Term Classification) only" — and the Confidence Inheritance Principle sits at paras 41–43, ahead of Part I's opening at para 45, so it is not excluded by that scoping. The document has not disclosed the omission either; §0's governance paragraph does not mention it.

This is not a formality. The document makes calibrated claims constantly and calibrates them only in prose: "this world's own on the evidence read" (2.6), "Luther's own coinage as read" (8.2), "the German-territorial form of this argument as read" (6.1), "probably a form-feature Doc_06 records under 4.1" (4.3). Each of these is a different confidence level in the constitutional vocabulary, and each is currently indistinguishable from the others to a downstream reader or to a script.

**Why it matters.** Confidence propagation is how this project keeps an inferential claim from hardening into a documented one three documents later. Doc_04 will consume this list; the [AS] tags in particular (ten of them, all flagged in §11 item 5 as resting on a comparative test against worlds whose lexicons do not exist) are exactly the claims the vocabulary exists to mark.

**Fix.** Apply the five-level vocabulary to the preliminary definition and to each Origin and Risk/Function tag judgment, at minimum on the ten [AS] entries, the two [CT] entries and the two [PV] entries.

---

## S5 — The §13 read-record is falsified at five loci

**What I checked.** I extracted every `file + line` citation from the entry bodies (§§1–9) by script and tested each against the read ranges §13's discovery table declares. Artefacts (thesis numbers, years, Registry row numbers) were filtered out, and every remaining out-of-range citation was opened by hand.

**What the document claims.** Discipline 1: *"Every term below was found in a passage read in a vendored file during this pass... The Document Log (§13) records exactly which sections were read and which were not."* Where a locus was not re-read, the document says so — and it does this correctly and repeatedly (2.2's Co 15139–15141, 3.5's v3 14586–14594, 4.9's Hy 766–768 and 558–561, 6.8's Co 16090–16091, 6.9's AC 49–51 and LC 3504, 7.4's v3 10554–10594, 9.1's v1 3994, all properly flagged).

**What I found — five loci that are cited or asserted as read, sit outside every range §13 declares, and carry no flag:**

| Locus | Where cited | §13's declared range for that file | What is actually there |
|---|---|---|---|
| **v1 10681** | 6.2 Preliminary definition; §10.3 | v1 ranges are 250–432, 1139–1602, 2243–2422, 3165–3324, 6713–6882, 10905–11094, 12775–12974, 14735–14809 | Neve's introduction: *"the conception of a true priesthood in the Church, viz., the priesthood of all believers."* Confirmed present. |
| **v1 10661, 10727** | 6.8 Evidence, asserted to be "Neve's, editorial (R7)" | as above | *"the opposition of the Sacramentarians[5]"* and *"the spiritualistic interpretation of the Sacramentarians"*. Confirmed present, and confirmed to be in Neve's introduction. |
| **v2 15816–15819** | 3.4 Evidence, first citation in the entry | v2 ranges run 15611–15815 then 15893–16042 — 15816–15819 is in the gap | The work's title page: *"THAT DOCTRINES OF MEN ARE TO BE REJECTED / TOGETHER WITH A REPLY TO TEXTS QUOTED IN DEFENCE OF THE DOCTRINES OF MEN (VON MENSCHENLEHREN ZU MEIDEN)"*. Confirmed present. |
| **Ap 4729** | 6.8 Evidence | Ap ranges are 552–771, 1108–1125, 4896–4935, 6492–6495 | *"fanatical opinions of the Anabaptists."* Confirmed present. §13's Ap row logs "6492–6495 (one grep-located line)" and does not mention 4729 at all. |
| **LC 1630** | 8.4 Evidence | LC ranges run 1045–1060 then 1685–1730 — 1630 is in the gap | *"it would greatly detract from the religious estate, and infringe upon the sanctity of Carthusians."* Confirmed present. |

**Why it matters.** In every case the content is genuinely there and the document's characterisation of it is right — so this is not a fabrication finding. It is a warrant finding, and that is nearly as serious here. This document's entire claim on a reviewer's trust is that §13 says exactly what was read, so that anything outside it is disclosed as inherited rather than verified. Five citations quietly outside that record mean the record cannot be used the way the document asks. Two of the five are not incidental: **v1 10681 is the exemplar the document itself leads with** in Discipline 2 and repeats in §10.3 as the proof that "priesthood of all believers" is editorial rather than Luther's — a "name the layer" claim resting on a line the read-record does not cover. And **v2 15816–15819 is where the German lemma *Menschenlehren* enters the document**, one of the lemmas Discipline 2 and §11 item 3 both list as shown by the vendored text.

**Fix.** Extend §13's ranges to cover these five loci (all five are short and were evidently read), or flag each as inherited. Do not leave the record as it stands.

---

## S6 — AC Articles I–III were not read, are not declared unread, and a core term is missing as a result

**What I checked.** The Augsburg Confession's own article boundaries in the vendored file, against §13's declared AC read range and §11 item 2's list of unread sections.

**What the document claims.**
- §13 discovery table, AC row: `232–1383 (Articles IV–XXVIII, abuses preamble)`
- §12: "Read in full this pass: ... AC Articles IV–XXVIII and the abuses preamble"
- §11 item 2 ("Unread vendored sections named") lists nine items. **AC Articles I–III is not among them.**

**What I found.** In `melanchthon_augsburg-confession_anon-pg275.txt`: Article I (Of God) begins at line 166, **Article II (Of Original Sin) at line 192**, Article III (Of the Son of God) at line 208, Article IV (Of Justification) at line 232. So Articles I–III — lines 166 to 231 — were not read, and the document's coverage-limit apparatus does not say so anywhere. §12 and §13 describe what *was* read accurately; §11 item 2, which is the document's list of what was *not*, has a hole in it.

**The substantive consequence.** `grep -i "original sin"` over Doc_03 returns **zero**. There is no candidate entry for **sin** or **original sin** anywhere in the 71. Nor is there one for the **Holy Ghost / Holy Spirit**, or for the **person of Christ**. AC II, unread, is where this world states original sin confessionally (AC 200–203: *"They Condemn the Pelagians and others who deny that original depravity is sin"*); AC III, unread, is where it states the person and work of Christ (AC 210–223). "Sin" is not a marginal term here: it is the presupposition of the entire justification cluster the document builds as its §2, it appears inside dozens of the quotations the document itself reproduces, and both catechisms — read in full and in part respectively — are saturated with it.

**Why it matters.** Two ways. First, §12 claims saturation for the sections read in full, on the Lexicon Framework's own stopping criterion (para 63) — but a saturation claim over AC is not available when a quarter of its doctrinal articles were not opened. Second, and worse for Doc_04: a candidate list offered so that "gravity discovery can be conducted in this world's own words" cannot omit the world's own word for the condition its central doctrine answers, and then not record the omission.

**Fix.** Read AC 166–231, add the coverage limit to §11 item 2 regardless, and reconsider whether sin / original sin and the Holy Ghost belong as candidate entries. If the judgment is that they do not, say so in §10.3 with a reason, the way §10.3 already does for "the Reformation" and "Sacramentarians."

---

## S7 — The §10.1 Author Gravity taxonomy does not classify 2.9, and misclassifies 6.4 against its own definition

**What I checked.** I recomputed the AG value of all 71 entries by script and compared them against the five lists in §10.1.

**What I found.** The lists' own arithmetic is right — 45, 17, 7 and 3 members respectively, and each list's membership matches the entry bodies exactly, with no false entries in either direction. But:

**(a) 2.9 (free will / bondage / "assertion") appears in no §10.1 category at all.** Its AG reads *"weighted to a single work (*Bondage*) whose OCR requires per-quotation re-check; Melanchthon's Article XVIII is the cleaner witness"* — which is a sixth category the summary never creates. Accounting for the three entries that legitimately appear twice (2.2, 7.5, 8.2) and for 1.4's alias line, the five lists cover 70 of the 71 entries. 2.9 is the one that falls through. A reader of §10.1 would conclude that every entry has been placed; one has not.

**(b) 6.4 (calling / "regularly called") is placed under "Weighted to Melanchthon" and excluded from "none," although it satisfies the document's own definition of "none."** §0 Discipline 3 defines that category as *"Luther in two or more registers **and** Melanchthon."* 6.4's own Voices line reads *"Melanchthon — AC (the term's home as read); Luther — sermon (of his own call), conversation"* — two Luther registers plus Melanchthon. The document handles the identical situation correctly at 2.2, which it places in **both** lists and explains ("its *weight*, not its attestation, sits with the Apology"). 6.4 should be treated the same way or the definition should be amended. By contrast 8.5, also weighted to Melanchthon, is correctly excluded from "none" — Luther appears there in one register only.

**Why it matters.** §10.1 is the section CF V7.4 para 635 actually requires ("Flag Author Gravity risks"), and §13's review request singles it out for checking. An unclassified entry and an inconsistently applied definition are small errors, but they are in the one output of this document that Doc_04 is obliged to act on.

---

## S8 — "justification 376" is a stem count presented alongside nine literal string counts

**What I checked.** Every term-frequency figure the document states, re-run with `grep -o -i` against the vendored Apology and v3.

**What the document claims.** §11 item 1:
> "Its term counts (justification 376, the Law 393, promise 314, merit 339, conscience 198, satisfaction 122, sacrifice 156, human tradition 37, vocation 32)..."

and 2.2's Voices line: *"the Apology's 376 hits make it the term's home."*

**What I found.** Nine of the ten figures reproduce exactly as literal case-insensitive substring counts of the string named: the Law 393 ✓, promise 314 ✓, merit 339 ✓, conscience 198 ✓, satisfaction 122 ✓, sacrifice 156 ✓, human tradition 37 ✓, vocation 32 ✓ — and elsewhere, indulgence 14 ✓ (1.1), purgatory 30 ✓ (1.5). **"justification" does not.** Its literal count is **124**. The figure 376 is the count of the stem `justif` (justify / justified / justifies / justification / justifieth). `justifi` returns 318; `justified` returns 138; `justificat` returns 124.

**Why it matters.** The list is presented as homogeneous and is used to rank the Apology's unread bulk as "the place where several 'Luther-only' flags in §10.1 may be corrected" — a prioritisation for Doc_06's reading. The headline figure overstates the named term threefold, and does so by a different counting method than the nine figures beside it, undisclosed. A reader re-running the check finds nine matches and one three-to-one discrepancy, which is worse for trust than a stated stem count would have been.

**Fix.** Either state 124 for "justification," or state the figure as `justif*` 376 and re-run the other nine on the same basis so the list is comparable.

---

## S9 — §10.3's "two kingdoms" claim is contradicted by the document's own 7.1 Evidence line, and the 7.1 [CT] contest type rests on it

**What I checked.** The §10.3 bullet against 7.1's Evidence line, and both against `luther_works-v3-selected_various1930.txt`.

**What the document claims.** §10.3:
> **"two kingdoms"** as a doctrinal label — **only the 1930 editor's marginal in *Secular Authority***; Luther's own "two kingdoms" in *Bondage* has a different referent...

and 7.1's Layer note: *"the running marginal 'The Two Kingdoms' (v3 12123–12127)... Luther's text at these loci says 'two classes,' 'two governments,' 'the kingdom of God... the kingdom of the world.'"*

**What I found.** The editorial marginals are correctly identified — v3 12123–12127 does read `The Two / King- / ' doms` and 12276–12280 does read `Spiritual / and Sec- / ular / Govern- / ment`, both set as running marginalia. But **Luther's own text in *Secular Authority* also uses the phrase**, and the document's own Evidence line for 7.1 quotes it, five citations earlier:

> `12371–12374 (OCR-damaged: "these two kin ee must be sharpl distinguished, and both be permitted to remain..." — recovered "kingdoms... sharply")`

I re-read v3 12371–12374 and confirm both the OCR as printed and the recovery: the sentence runs *"For this reason these two kin[gdoms] must be sharpl[y] distinguished, and both be permitted to remain; the one to produce piety, the other to bring about external peace and prevent evil deeds."* The context, three lines after "two governments" at 12319 and in the middle of the church/civil argument, admits no other reading — and the document itself makes that recovery. So the phrase in *Secular Authority* is **not** "only the 1930 editor's marginal": it is in the treatise's own text, in the church/civil sense, in the OCR-mangled form the document has already transcribed. (A plain `grep "two kingdoms"` across all ten files returns three hits, all in *Bondage* — which is presumably how the claim was formed, and which the line-broken marginal and the `kin ee` mangling both defeat.)

**Why it matters.** This is not a stray bullet. It is the evidentiary basis of 7.1's **[CT]** tag, whose stated contest type is:

> "the term's **historical scope** — whether the later systematic label ('two kingdoms doctrine') applies as broadly to Luther's own usage as claimed, given that **the vendored texts use 'governments,' 'classes,' and, in *Bondage*, 'kingdoms' in a different sense**."

The clause after "given that" is false on the document's own evidence. *Secular Authority* uses "kingdoms" in the church/civil sense too. The contest may still be real — that is a specialist question, and §11 item 4 rightly concedes no secondary source is rowed for it — but the in-text ground the document offers for it does not hold, which leaves the [CT] tag resting on this pass's judgment alone.

**Fix.** Correct the §10.3 bullet, and either re-argue the 7.1 contest type on grounds that survive v3 12371, or drop it to §11 item 4's open-items list until a source is rowed.

---

## S10 — The Ninety-Five Theses numbering: two citations silently correct the vendored file

**What I checked.** Every thesis number the document asserts, against the numbering the vendored file actually prints. I enumerated all 95 numbered theses in v1 with `grep -n "^[0-9]\{1,2\}\. "`.

**What I found.** Fifteen of seventeen thesis-number assertions verify exactly at the cited lines: Th. 1 (1154), Th. 2 (1158), Th. 10 (1191), Th. 16 (1213), Th. 21 (1230), Th. 27 (1253), Th. 30 (1264), Th. 34 (1278), Th. 36 (1285), Th. 40 (1301), Th. 43 (1312), Th. 58 (1373), Th. 62 (1387), Th. 82 (1457), Th. 92–93 (1506–1510), Th. 94–95 (1512–1518). Two do not:

| Document says | Actual text at the cited lines |
|---|---|
| 1.6: `v1 1249–1251 (**Th. 26**: "not by the power of the keys (which he does not possess)")` | `36. The pope does well when he grants remission to souls [in purgatory], not by the power of the keys (which he does not possess),[5] but by way of intercession.` |
| 1.1 and 9.3: `v1 1348–1349 (**Th. 52**: "The assurance of salvation by letters of pardon is vain")` | `53. The assurance of salvation by letters of pardon is vain, even though the commissary,[15]...` |

The quoted words are exact in both cases. The *numbers* are not what the file prints. The vendored file's own numbering is corrupt in places — it prints "36." twice (1249 and 1285), "13." twice (1198 and 1201) and "73." twice (1419 and 1422) — and "Th. 26" and "Th. 52" are the correct standard numbers that the file has garbled. The document is right about the theses and wrong about the file.

**Why it matters.** Under "read, don't infer," a silent correction of the vendored text from general knowledge is the same operation as a silent emendation, and this project has ruled on it before: Registry row R87's own Verification Note records a Revision-1 defect where a quotation was "silently emended... while flagging only the first change," and the correction was to print the file's own text and disclose the oddity either way. A reviewer following either citation finds a number that does not match and has no way to tell whether the document misread the file or corrected it.

**Fix.** Cite what the file prints and note the file's own numbering error — e.g. "Th. 26 (the file prints '36.', one of several numbering errors in this scan)". The point is worth making once in §0 as well, since a downstream builder citing theses by number from this file will hit the same trap.

---

## S11 — 7.4 reproduces barred language from the unvendored 1525 tract, in the sentence declaring it barred

**What I checked.** The bar statement at 7.4, against a `grep` sweep of all ten vendored files and against Registry row R94's own text.

**What the document says.** 7.4, Evidence line:
> **Bar, stated:** the 1525 tract and its language ("**smite, slay and stab**" etc.) are not in this library and are barred by R94; nothing here characterizes 1525.

and Discipline 1: *"Nothing is drawn from... *Against the Murderous, Thieving Hordes of Peasants* (1525) — neither is vendored."*

**What I found.** "smite, slay and stab" returns **zero hits across all ten vendored files** — confirming the document's factual claim and, at the same time, establishing that the phrase in Doc_03 came from outside the library. R94 names that exact phrase in its bar:

> "Specifically: the Worms 'Here I stand' formula in any rendering; the actual language of *On the Jews and Their Lies* (1543) and of *Against the Murderous, Thieving Hordes of Peasants* (1525), **including 'smite, slay and stab'**... **These must not be reached for, even though they are famous and are almost certainly in a generating model's training data.**"

**How to weigh it.** This is the mildest of the substantial findings and I record it with its mitigation stated: R94 itself prints the phrase in order to name it, so Doc_03 is plausibly echoing the Registry's bar rather than the tract, and the document's intent — to fence the entry — is exactly right. But the phrase in Doc_03 carries no attribution to R94 at the point of use (the Registry line offers only `94 (bars)`), and Doc_03 is a construction document that feeds the lexicon and, through it, runtime vocabulary. R94's own rationale is that these are "the items a model is most likely to recall verbatim"; a barred phrase propagating one document further, unattributed, is the first step of exactly the failure R94 was appended to prevent. Discipline 1's flat "nothing is drawn from" is also literally untrue as long as the phrase is there.

**Fix.** Either attribute the phrase to R94 explicitly at the point of use, or — better, and cheaper — state the bar without reproducing the language: "the 1525 tract's own language is not in this library and is barred by R94."

---

## S12 — [PV] is under-applied, because §0 narrows the Framework's own definition of the tag

**What I checked.** Lexicon Framework V2.1 para 97 against §0's tag key and against the entries that carry no PV.

**What the Framework says (para 97).**
> **[PV] — Plural Voices.** "The term or concept is important within some streams, **voices, or periods** of the world but is not universally representative across the whole reconstructed ecology. This tag should trigger explicit attention during Internal Plurality review... rather than silent flattening into one position."

**What the document says (§0).**
> **[PV]** Plural Voices (**applied only where the vendored registers or voices demonstrably differ, not where one is merely silent**)

**What I found.** The document's added restriction is a defensible instinct — it prevents tagging on absence of evidence, and §10.1 applies it consistently, correctly refusing PV at 8.8 because "the Third Sermon is unread, so no plurality is *demonstrated*." But the restriction has been written as though the Framework's definition were "voices differ," when the Framework's definition is "not universally representative across streams, voices **or periods**." Dropping "periods" from the operative test produces a concrete miss:

**7.4 (insurrection / rebellion / "the common man") carries no PV tag**, while its own AG line reads: *"Luther-only, cross-register — and **period-bound to 1521–22 in this library**, a real coverage limit for Doc_04."* A term the document itself describes as period-bound and not representative of the whole window is the Framework's definition of [PV], almost verbatim. And 7.4 is the entry where flattening is most dangerous — its own distortion flag says so: *"the 1525 tract's reputation will be projected onto the 1522 vocabulary."* [PV] is the tag that would route that to Internal Plurality review instead of leaving it in prose.

Two further candidates on the same test, weaker but worth a decision rather than silence: 5.7 (transubstantiation, one work, a position Luther holds as permissible rather than shared) and 8.2's inverted coinage (one occasion, 1523).

**Why it matters.** A narrowing of a Framework tag definition is a methodology change, which CLAUDE.md's own default-actions table routes to "Always ask." The document made it unilaterally in §0 and the change is not flagged in §13's escalation check, which records "no governance or methodology change."

**Fix.** Either restore the Framework's own definition and re-test every entry against "streams, voices, or periods," or state the narrowing as a proposed methodology variance and escalate it.

---

## S13 — The [AS] comparative test was run against three of the six neighbours Doc_01 §8 names

**What I checked.** Doc_01 §8's section headings against §0's statement of the [AS] test.

**What the document claims.** §0, tag key:
> "the Framework's test is comparative, 'unlikely to carry equivalent weight in neighboring worlds,' and this document applies it against **the neighbours Doc_01 §8 names** (the Reformed cities, the Anabaptist movements, the Tridentine Church)"

**What I found.** Doc_01 §8 names **six**: §8.1 the Reformed cities (VI.2), §8.2 the Anabaptist movements (VI.3), §8.3 the Tridentine Church (VI.22), **§8.4 the Society of Jesus (VI.11)**, **§8.5 Lollardy (V.5)**, **§8.6 the Augustinian Hermits** — the last identified in Doc_01 as this world's own seedbed and therefore the single most likely source of shared late-medieval vocabulary that an [AS] tag would need to exclude. The parenthesis is presented as an enumeration of what §8 names, and it names half of it. §11 item 5 compounds this: it schedules re-testing against "VI.2's or VI.3's Doc_03" only, so the Tridentine Church is dropped from the forward plan too.

**Why it matters.** [AS] is the one Origin tag that makes a claim about *other* worlds, and §11 item 5 already concedes it is the most likely classification defect ("the Gallic precedent... is that AS over-tagging is the most likely classification defect"). Ten entries carry it. The Augustinian Hermits omission bites hardest on 8.1 vows, 8.4 "spiritual"/*Geysterey* and 8.5 perfection — monastic vocabulary tested against three non-monastic neighbours.

**Fix.** Either run the test against all six and say so, or state plainly which three it was run against and why, and add the missing three to §11 item 5's re-test list.

---

## S14 — Two entries cite Doc_01 §8.0 for propositions §8.0 does not contain

**What I checked.** Every cross-reference to Doc_01 in the entry bodies, against the cited sections of Doc_01. Most verify: 4.2's "(Doc_01 §5 'formation')" is right (§5: *"with the household (not only the monastery or the confessional) as a formation site the movement explicitly targets"*); 5.3's appeal to §7 and §8.1 on Marburg is right; 7.2's quotation of §8.2 — *"from the establishment side"* — is exact; 6.8's reading of §8.2 is right; §0's account of the strand-singular finding reproduces Doc_01 §6 accurately, including both rejected candidates. Two do not.

**(a) 3.4 (doctrines of men / human traditions):**
> "Kept SC: the Reformed cities and the Anabaptist movements refuse 'human traditions' with comparable weight (**Doc_01 §8.0**)"

**(b) 6.2 ("we are all priests"):**
> "Kept SC: the Reformed cities and Anabaptist movements carry a comparable claim (**Doc_01 §8.0**)"

**What I found.** Doc_01 §8.0's relevant sentence reads: *"**Scripture's own authority against institutional hierarchy** is the clearest case: this world shares that refusal with both the Reformed cities and the Anabaptist movements, but pairs it with territorial-magisterial authority..."* §8.0 makes one comparative claim, about Scripture's authority. It says nothing about human traditions and nothing about the priesthood of all believers. Both statements are very likely true of those movements — and that is the difficulty: they are being sourced to a document that does not contain them, in the two places where the document decides **not** to tag a term [AS]. These are negative classification decisions with a citation that does not support them.

**Why it matters.** Doc_01 finding S4 — cited approvingly in Doc_03's own §10.3 — was raised against exactly this move: "§1: a Latin phrase in quotation marks attributed to a vendored treatise that does not contain it," and the Round 1 reviewer grouped it with S1 and S5 as "three claims sourced from an index or a sibling document while presented as sourced from the primary text or the cited framework." The same pattern has recurred one document later.

**Fix.** Either ground both on §8.0's actual Scripture-authority claim (which supports 3.4 reasonably well and 6.2 less well), or state them as this pass's own comparative judgment awaiting the neighbours' own Doc_03s, in line with §11 item 5.

---

# COSMETIC FINDINGS

**C1 — §0's blanket no-citation claim is contradicted by 7.4's own Registry line.** §0 states "nothing below cites R33, R55, R57, R58, R94 or R95," but 7.4's Registry line reads `11, 15, 19, 44 (context); 48, **94** (bars)`, and §10.3 names R55, R48, R94 and R49. I confirmed by script that no Excluded row is used as a *source* for any candidate term — the substantive discipline holds, in all 71 entries — so this is purely the word "cites" doing more work than intended. Reword to "nothing below draws a candidate term from R33, R55, R57, R58, R94 or R95."

**C2 — 1.7 drops a translator's bracket without an ellipsis.** The document quotes v1 2269–2270 as *"Christ, our Captain, under Whose banner (i. e., the Holy Cross) we continually fight against sin."* The file reads *"...we are known as a people of Christ, **[Heb. 2:10]** our Captain, under Whose banner..."*. The bracketed reference is the translator's, and this is the one document in the build whose whole Discipline 2 is about marking that layer. Mark the elision.

**C3 — 3.1 quotes two footnote glosses without their loci.** *"Steimle's fns. [4]–[5] gloss the Latin as 'Right to speak' / 'Power to do'"* appears inside the parenthesis for `14864–14866`. The footnotes are at **v2 15752 and 15754**. Discipline 1 says "every quoted phrase is given with the file and line(s) where it begins"; these two are not. The footnote markers at 14864–14865 are correct, and the glosses verify exactly.

**C4 — Two counts at 7.2 do not reproduce.** *"'Secular' is Schindel's 1930 English (v3, **85 hits**); the 1915–16 volumes say 'temporal.'"* Actual v3 occurrences: 44 lowercase + 38 capitalised = **82** (83 matching lines). And v1+v2 contain "secular" **4** times, against "temporal" 181 — so the contrast is right in substance but "the 1915–16 volumes say 'temporal'" is stated more absolutely than the files support.

**C5 — "Popedom" is not only Bell's.** 6.7 and §10.3 record "Popedom" as "Bell's seventeenth-century English." It also appears at **v1 12378**, lowercase, in Schmauk's introduction to *The Papacy at Rome* — a different layer of the same apparatus the document is otherwise scrupulous about naming. Six of the seven occurrences are Bell's; the claim needs "chiefly."

**C6 — §10.3 conflates two different editorial phrases.** *"'priesthood of all believers' — an editor's introduction (v1 10681) and sidenote (v2 2171)."* v1 10681 reads "the priesthood of all believers" ✓; the sidenote at v2 2171 reads "**The Priesthood of Believers**" — without "all". §0's Discipline 2 gets this right, quoting the sidenote exactly; §10.3 should match it.

**C7 — "the two v1 occurrences" of "Sacramentarians" is three.** 6.8 and §10.3 name v1 10661 and 10727. There is a third at **v1 15611**, an entry in Lambert's index. Arguably not an "occurrence" in a text, but the count is stated as exhaustive.

**C8 — 2.2 quotes "the grand hinge" in a form the file does not print.** Co 15140 reads `saw, what was the ^^nd hinge, upon which the iwhole`. The document flags the citation as "per R34's recovered reading — OCR-degraded, not re-read this pass," which is honest, and the recovery is obviously correct. But every other *Bondage* quotation in the document is given as-found with the recovery stated alongside (2.9, 3.3, 7.1), and this one is not. Match the house style.

**C9 — "matching the Appendix's AG column exactly" is loose for three entries.** §10.1's "none" list claims exact correspondence with the Appendix AG column. The bodies match perfectly (I verified all 45 by script), but the Appendix cells for 2.2, 7.5 and 8.2 are compound — `none (wt. M)`, `none / L single (serm)`, `none / L single (exh)` — so "exactly" overstates a correspondence that is substantively fine.

**C10 — the *Anfechtung* absence claim is right but could be more precise.** 9.2 and §10.3 state "No vendored text glosses *Anfechtung*... (checked)." I confirm: the word occurs exactly once across all ten files, at v2 5418, inside a footnote citing the 1521 *Gravamina* (*"Von anfechtung der cordissanen"*) in the wholly unrelated sense of attacking a benefice title. The claim as worded ("no gloss") holds. Saying "one occurrence, unrelated sense, v2 5418" would make the check reproducible rather than asking the reader to take "(checked)" on trust — which is the standard this document applies to itself everywhere else.

---

# Framework compliance: checked and clear

Recorded so a future reader knows these were tested rather than assumed.

- **Scope (CF V7.4 para 638; Lexicon Framework para 61).** No entry drifts into Doc_06 depth. No World Meaning, no Ecological Function, no paired Modern-Hearing/World-Hearing writeup. Every distortion note is a single clause, as §0 promises. CF para 634 explicitly authorises "preliminary definitions based on source evidence," so the one-to-three-sentence definitions are within scope, not against para 61. The longest definitions (1.1, 5.6, 6.7, 7.1) sit at the upper edge of "basic definitions" but do not cross it.
- **§0's quotations of the governing frameworks are accurate.** CF paras 630, 631, 633, 638 and Lexicon Framework paras 61, 63 and 121 all reproduce correctly, including "from the Source Registry's Native entries — not from the raw ecology (Doc_02) directly" (para 633) and "A world's Tier 1 list should be small relative to its total lexicon" (para 121).
- **[CT] contest types (Lexicon Framework paras 105–109).** Both [CT] entries state a contest type from the four listed: 2.2 states two of them ("the term's meaning within its historical context, and its relationship to present-day traditions that use the term differently"); 7.1 states "its historical scope." Both disclose that no secondary source is rowed. Compliant as to form — but see S9 on whether 7.1's stated ground survives.
- **Internal statistics.** Every stated count reproduces: **71** entries; **38** Tier 1 / **27** Tier 2 / **6** Tier 3; the enumerated Tier 1 list in §10.2 is exactly the computed Tier 1 set; the fifteen clusters in §10.2 account for exactly 38 entries with no double-counting; **10** [AS]; **2** [CT]; **2** [PV]; the §10.1 lists number 45, 17, 7 and 3 as stated and their memberships match the entry bodies. The **Appendix agrees with the entry bodies on tier, Origin tag and Risk/Function tag for all 71 rows, zero mismatches** — an unusually clean result.
- **Cross-document consistency.** The strand-singular finding, both rejected strand candidates, the 1517–1580 window, the Zell Excluded determination, the Grumbach named-absence, the Marburg boundary, and the "from the establishment side" quotation all reproduce Doc_01 and Doc_02 accurately. The Registry row numbers cited resolve correctly. (The two exceptions are at S14.)
- **Escalation.** §13's escalation check is correct on three of its four heads — no Representative identity decision, no portfolio-level decision, no unresolved inter-document tension. Its fourth ("no governance or methodology change") is contradicted by S12.

---

# What Round 2 should re-check

Per the usage discipline's targeted-recheck rule, a second round should not repeat this one. It should check, specifically:

1. **S1** — the corrected Apology quotation, character by character, and the separation of AC V's wording from the Apology's.
2. **S2** — that 9.6 no longer asserts the order, and that the R30 wording has been raised with the Registry owner rather than edited in place.
3. **S3** — 9.6's Evidence, Voices, AG and Appendix row now agreeing with each other and with the AC file.
4. **S5, S6** — §11 item 2, §12 and §13 re-run against the entry bodies by script, including AC 166–231, and whether sin / original sin has been added or its absence reasoned.
5. **S4, S12** — whether the confidence vocabulary has been applied and whether the PV narrowing was escalated or withdrawn.
6. **S9, S10** — the §10.3 "two kingdoms" bullet, the 7.1 contest type, and the two thesis numbers.
7. Any entry whose Evidence line changed: re-run the full 316-pair citation sweep, not a sample, since edits to Evidence lines are where line numbers drift.

**Disposition: none claimed by this review.** This report is a finding, not a ruling; it does not dispose the document. Under the project's governance rule, none of the substantial findings above may be closed by self-certification — each needs independent re-confirmation.
