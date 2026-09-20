# Doc_03 Review — Round 4 (independent minimal recheck, cold)

**Document under review:** `witt_Doc_03_Lexicon_Candidate_List.md` (DRAFT, Revision 3), Lutheran Wittenberg & Its Congregations (Atlas VI.1, `witt`).
**Reviewer:** independent, no drafting involvement, no involvement in Rounds 1–3, no prior context on this document or on how its Revision 3 fixes were made.
**Date:** 2026-09-15.
**Scope:** exactly the five-item list Round 3 set for itself in "What a Round 4 check should and should not do," applied to Revision 3. **Not a re-review, and smaller than Round 3.** The 606-citation sweep, the 24-citation fresh sample, the full body-vs-Appendix cross-check beyond the one re-run Round 3 asked for, the thesis-number enumeration and the Doc_01 §8.4/§8.5 comparison were **not** re-run. S1–S14, C1–C10 and N1–N8 were not re-checked.

**Method.** §0, §11, §12, §13 and entries 5.7, 6.7 read in full; `Open_Gaps_Tracking.md` read in full. Every boundary named in §12 re-opened in the vendored file itself and checked against the next structural heading — including the items §12 still claims were read *in full*, which were re-derived from the files rather than accepted on the document's word. Lexicon Framework V2.1 opened directly with python-docx and paragraph 97 read from the file. A body-vs-Appendix extractor written from scratch for this round. Every `Hy` locus and every `v2` locus cited anywhere in the document swept by script against the declared ranges. Doc_02 §15 item 4, §17 and its header read directly to test `Open_Gaps_Tracking.md`'s own claims rather than its summary of them.

---

# VERDICT: MINOR ISSUES REMAIN

**All four items on Round 3's Round 4 list were checked, and three pass outright.** The N1 cross-check reproduces exactly (72/72). All four single-phrase checks (R3-3 – R3-6) are correctly fixed, verified against the `.docx` and the vendored files rather than against the document's account of them. `Open_Gaps_Tracking.md` exists, is substantive, and its four entries are accurate against the documents they cite — with one quotation defect.

**R3-1's fix is real, and its central safety claim holds.** Every boundary Revision 3 newly declared for *The Papacy at Rome*, the *Kurze Form*, and hymns I, IV, V and XXVI reproduces exactly against the files. I swept every `Hy` and every Kurze-Form-range `v2` locus cited in all 72 entries: **no citation anywhere in the document falls inside a zone the correction newly marked unread.** The one condition under which this fix would have been broken rather than merely a coverage correction does not obtain.

**Two new substantial findings, both in §12's coverage list, both the same class R3-1 named.** R3-1's remedy was an audit of the whole "read in full" list, and §12 and §13 both state that the audit was performed and that the remaining items were "confirmed still accurate." That certification does not hold for one item (**R4-1**, the Augsburg Confession), and the extent stated for one of the five newly corrected items is itself wrong (**R4-2**, the hymnal prefaces). This is the third round in which the same defect class has been found in this one list, and the first in which it is found *inside* the sweep meant to close it.

**Nothing found in this round misquotes a source, miscites a locus, misstates a tag or a count, or misclassifies an entry.** Every quotation and locus I tested reproduced verbatim at its stated lines. As at Round 3, the findings are about coverage statements and verification claims, not about the evidence.

**Disposition: none claimed.** This report is a finding, not a ruling; it does not dispose the document. Per the project's governance rule, none of the findings below may be closed by self-certification.

---

# The four items, checked

## 1. R3-1 — §12's coverage list — **FIX CONFIRMED IN PART; see R4-1 and R4-2**

### (a) The five items moved to "read in part" — **four of five verified exact, one misstated**

Each boundary re-derived from the file by locating the next structural heading, not read off the document:

| Item | Document's stated extent | File | Verdict |
|---|---|---|---|
| *The Papacy at Rome* | title 12694, declared range 12775–12974, footnotes 14691, ends mid-argument | title `TO THE PAPACY AT ROME` 12694; `THE STATEMENT OF THE CASE` 12775; 12972–12973 closes the Romanist's syllogism ("B. Inasmuch as all Christendom is one community on earth, it must have a head, which is the pope"); 12975 opens Luther's reply (`[Sidenote: The Futility of the Argument]`); `FOOTNOTES` 14691 | **Exact** |
| *Kurze Form* | declared 13172–13341; work runs to roughly 14403; unread section begins at "THE TRANSGRESSION OF THE COMMANDMENTS," continuing through the Creed and the Lord's Prayer | work title 13172; `PREFACE` 13179; `THE TEN COMMANDMENTS` 13220; `THE TRANSGRESSION OF THE COMMANDMENTS` 13339; `THE CREED` 13736; `THE LORD'S PRAYER` 13973; `FOOTNOTES` 14349; next work 14403 | **Accurate** (the heading is at 13339, two lines inside the declared end — immaterial) |
| Hymn I | runs 1258–1430, Hymn II begins 1431 | I at 1258, last text 1427, II at 1431 | **Exact** |
| Hymn IV | runs 1647–1740, Hymn V begins 1741 | IV at 1647, V at 1741 | **Exact** |
| Hymn V | runs 1741–1991, Hymn VI begins 1992 | V at 1741, last text 1988, VI at 1992 | **Exact** |
| Hymn XXVI | runs 3660–3756, Hymn XXVII begins 3757 | XXVI at 3660, XXVII at 3757 | **Exact** |
| The four hymnal prefaces | declared 890–1124 covers the first three in full and the Fourth in part; "Luther's Fourth Preface, begun at 1103, continues past 1124 to roughly 1230 before Hymn I's own heading at 1258" | First 890, Second 940, Third 1059, Fourth 1103 — **but the Fourth Preface ends at 1178**; 1182–1236 is a separately titled fifth piece, `A Preface to All Good Hymn-Books. By Dr. Martin Luther`; 1240–1254 is `A Warning by Dr. Martin Luther` | **Misstated — see R4-2** |

### (b) Carry-forward into §11 — **confirmed**

§11 item 2 now carries all five forward by name and range: *The Papacy at Rome* beyond its introduction (v1 12975–14690, R8), the *Kurze Form* beyond its preface and Commandments (v2 13341–14403), the Fourth Preface beyond 1124, Hymn I in full, Hymn IV beyond 1696, Hymn V beyond 1870, Hymn XXVI beyond 3719. The Papacy remainder is present, which was the specific thing Round 3 asked Round 4 to confirm.

One cross-reference note: Round 3's fix instruction, and §13's own restatement of it in the review-requirement bullet, both say "§11 item **8**." The carry-forward was in fact written into **item 2** ("Unread vendored sections named"), which is the correct home — item 8 is Registry maintenance for sections this pass *did* read. The document did the right thing and left the stale item number in its own restatement of the requirement.

### (c) The items still claimed "read in full" — **one fails**

Re-derived from the files, not accepted on the document's word:

| Item | Declared | File | Verdict |
|---|---|---|---|
| SC | whole file, 1–681 | 682 lines, last non-blank 681 | **Complete** |
| Ninety-Five Theses + footnotes | v1 1139–1602 | Disputation heading 1139; first thesis 1154; footnote block's last line 1603; next work (`III`, Letter to Staupitz) 1606 | **Complete** (the block ends at 1603, one content-free line past the declared 1602; §12 says it ends "immediately before the next work begins at 1606," which is right in substance) |
| 1539 and 1545 prefaces | v1 250–432 | `SELECTIONS FROM LUTHER'S PREFACES...` 250; `I` 253 / 1539 preface 255; `II` 349 / `DR. MARTIN LUTHER TO THE CHRISTIAN READER` 350, 1545; footnotes to 431; Theses title page 434 | **Complete — both prefaces, ending cleanly** |
| Wittenberg Sermons 2, 5, 8 | v2 14827–14963; 15285–15422; 15611–15815 | Second 14827 → Third 14964; Fifth 15285 → Sixth 15423; Eighth 15611 → next work 15816 | **Complete and exact** |
| Wittenberg Sermon 1 | v2 14634–14833 | First 14634 → **Second 14827** | **Overruns by seven lines — see R4-3** |
| AC Article II | 192–207 | Article II 192 → Article III 208 | **Complete** |
| **AC Articles IV–XXVIII + abuses preamble** | **232–1383** | Article IV 232; abuses preamble 652; **Article XXVIII 1271, running to 1526; `CONCLUSION.` 1531; file ends 1567** | **Not complete — see R4-1** |

### (d) The independent locus sweep — **clean, which is the finding that matters most here**

Every `Hy` and every `v2` locus cited anywhere in the 72 entries, extracted by script and tested against the corrected boundaries:

- **Kurze Form:** four entries cite inside it — v2 13182–13187, 13202–13210, 13264–13265, 13272–13273. All four fall inside the corrected 13172–13341. **None is orphaned by the narrowing.**
- **Hymns:** every cited `Hy` locus in hymns I, IV, V and XXVI falls inside the ranges actually read — 1286–1293 (I), 1671–1677 (IV), 1744–1853 (V), 3671–3705 (XXVI). Entry 9.6's citations all fall inside 1741–1870, as §12 claims. **No hymn citation falls into a newly-declared-unread zone.**
- Three `Hy` loci sit outside every declared read range: 558–561 and 766–768 (both attributed in entry 4.9 to Registry rows R47 and R45, with an explicit "read by the Registry pass, not re-read here") and 651–652 (§10.3, Carlyle's "Here I stand" as quoted by Bacon, barred by R94). None falls in a corrected zone, so none bears on R3-1 — but see **R4-5** on how §13 words the claim.

**So the fix is not broken.** The one condition Round 4 was told to test for — a citation stranded outside the corrected, narrower boundaries — does not occur anywhere in the document.

## 2. The N1 check description, and the check itself — **PASS**

**The filename claim is gone.** `verify_doc03.py` now appears in §13 only as the thing being corrected, at both places Round 3 found it, each replaced with a prose description of what the check actually compares ("a script that parses each `### n.m` entry's `Tier (est.)` line and each Appendix row's Tier column and compares them as a set" for Revision 1; the Origin/Risk-Function rewrite described in prose for Revision 2). No sentence in the document now offers the filename as a re-runnable warrant. `find` over the whole repository confirms no such file exists under `/home/user/cic-project`, which is what §13 now says. (A file of that name does sit in a session scratchpad directory outside the repository; that is consistent with, not contrary to, §13's statement.)

**I re-ran the check with my own extractor**, parsing the `- **Tags.**` and `- **Tier (est.).**` lines from each `### n.m` entry and the Origin, Risk/Function and Tier cells from the Appendix table, comparing as sets:

- **72 entry bodies, 72 Appendix rows, symmetric difference empty.**
- **72/72 agreement on Tier, Origin tag and Risk/Function tag together. Zero mismatches.**
- Tier split reproduces independently in both surfaces: **39 / 27 / 6 = 72**.
- [PV] on exactly {5.6, 6.7, 7.4} in both surfaces; [CT] on exactly {2.2, 7.1}; [AS] on exactly {2.6, 2.7, 4.2, 4.4, 5.3, 6.1, 7.1, 7.5, 8.2, 8.4} — ten, matching §11 item 5's enumerated list and `Open_Gaps_Tracking.md` OG-3.

## 3. The four single-phrase checks — **ALL PASS**

**R3-3 — PASS.** §0 no longer says "as unsourced." It now reads: Doc_01's own Round 1 struck the earlier claim "as contradicted by a source — the Society's own Step 0 — once actually read," with an explicit correction note: "not 'as unsourced'; the original claim was not unsourced, it was written without reading a source that, once read, said the opposite." That is Doc_01 §8.4's own account of itself, and it is the distinction Round 3 asked for.

**R3-4 — PASS, verified against the `.docx`.** I opened `reference/L3B-World-Build-Methodology/CiC_L3B_Interpretive_Lexicon_Development_Framework_V2.1.docx` with python-docx. Paragraph 97 reads:

> The term or concept is important within some streams, voices, or periods of the world but is not universally representative across the whole reconstructed ecology. This tag should trigger explicit attention during Internal Plurality review (per the Template) rather than silent flattening into one position.

§0 now quotes "important within some streams, voices, **or periods** of the world but **is** not universally representative across the whole reconstructed ecology." **That is an exact substring of paragraph 97.** The "quoted here verbatim" claim is now true, and the restoration is disclosed in its own correction note.

**R3-5 — PASS.** Verified directly in `luther_works-v2-selected_jacobs-spaeth1916.txt`:

- Footnote **[45]** stands at **10562–10566** and reads "In the dogma of transubstantiation (Fourth Lateran Council, 1215) the Church taught that the substance of bread and wine was changed into the substance of Christ's body and blood, while the accidents of the former...remained." 5.7's quotation of it is verbatim.
- Its anchor `[45]` is in this treatise at 7026 ("real bread and real wine, and not their accidents only[45]"), as 5.7 now states.
- Footnote **[50]** stands at **10577** and reads only "_Decretal. Greg. lib. I, tit. i, cap. I, section 3_." The marker `[50]` is indeed the one printed against *Firmiter* at 7223. 5.7 now says exactly this, and no longer attaches the Lateran gloss to it.
- The locus is declared: §13's v2 discovery row now carries "**10562–10566 grep-located (footnote [45] on transubstantiation/*Firmiter*, cited at 5.7 — corrected, Round 3 R3-5...)**."

The underlying quotation at 7221–7224 and the "common people" passage at 7143–7149 both still reproduce verbatim. One residual, at **R4-6**.

**R3-6 — PASS.** 6.7 now reads "corrected, Round 3 R3-6: not 'the same way' — Ap 4729's range was extended, this locus is grep-flagged instead, the other of the two routes Round 2 offered." That states the two methods as different and both legitimate, which is what Round 3 asked for.

## 4. `Open_Gaps_Tracking.md` — **EXISTS, SUBSTANTIVE, ACCURATE — one quotation defect**

The file exists at `World-Builds/Lutheran-Wittenberg/Open_Gaps_Tracking.md`, 95 lines, four numbered entries (OG-1 – OG-4), each with a status line, a stated basis and a named action. It states the append-only, never-renumbered discipline and the subject-plus-date cross-reference rule in its own header, matching CLAUDE.md. It is not a stub. I checked each entry's claims against the documents it cites rather than against its own summary:

- **OG-1 (Zell/Grumbach) — accurate in substance.** Doc_02 §15 item 4 and Registry R55 do determine Zell's whole corpus Excluded / Named Comparandum on a disclosed conservative default; the phrase "an absence of reported evidence, not a reported absence" appears verbatim twice in Doc_02; five rounds (`Round1`, `Round2`, `SpotCheck_Round3`, `Round4_ZellCheck`, `Round5_ZellFinalCheck`) are all on disk; Doc_02 and the Registry are both APPROVED TO PROCEED, Revision 5, self-disposed under CO-022 on 2026-09-15, with the Zell item flagged for coach verification rather than closed. **The quotation attributed to Doc_02 §17 is not verbatim — see R4-4.**
- **OG-2 (Doc_03's inline markers) — accurate.** The round tallies (14+10, 5+3, 1+6) match the three review files. "Round 3 counted 38 bolded inline fix markers across 19 of 72 entries" matches Round 3's own report exactly. Doc_03 is DRAFT, Revision 3, disposition none claimed, so the status line ("not blocking its current DRAFT status") is right. The `witt_Source_Registry.md` precedent checks out: its header is APPROVED TO PROCEED, Revision 5, and does carry per-round fix narration.
- **OG-3 (the ten [AS] tags) — accurate.** Six neighbours named, three tested; the ten tagged entries match my own independent recomputation and §11 item 5; the Augustinian-Hermits reasoning and the 8.1/8.5 [SC] caveat match §0 and §11 item 5.
- **OG-4 (the unread Apology, and the two [CT] tags) — accurate.** The read ranges (552–771, 1108–1125, 4896–4935, plus grep-located 4729) match §11 item 1 exactly; the two [CT] tags (2.2, 7.1) and the "no secondary source rowed" statement match §11 item 4 and my own tag sweep. One imprecision: the Apology file is **10,466 lines**, not "roughly 8,500+" — the figure looks to have been taken from the highest Apology line number cited in Doc_02 rather than from the file. It understates the unread remainder; worth correcting in passing.

The cross-reference back from Doc_03 is in place: §13 and the escalation check both point N5 at OG-2 rather than leaving it inside §13 alone, which was R3-7's whole point.

---

# NEW SUBSTANTIAL FINDINGS

## R4-1 — the AC is still on §12's "read in full" list, and Article XXVIII is read less than halfway; Revision 3 certified this item as checked

**What the document claims.** §12, first sentence of the read-in-full list: "Read in full this pass, **boundaries verified against the files**: SC (whole file, 1–681); the Ninety-Five Theses and their footnotes...; **AC Article II and Articles IV–XXVIII and the abuses preamble**..." And §13's Revision 3 fix log: "**Confirmed still accurate on this pass:** SC (whole file), the Ninety-Five Theses and footnotes, **AC (Article II plus IV–XXVIII, I and III already disclosed as unread)**, Sermons 1/2/5/8..., and the 1539/1545 prefaces."

**What the document's own read record declares.** §13's AC discovery row: "**232–1383** (Articles IV–XXVIII, abuses preamble), drafting pass."

**What I found in `melanchthon_augsburg-confession_anon-pg275.txt`:**

| Feature | Line |
|---|---|
| `Article IV: Of Justification.` | 232 |
| `ARTICLES IN WHICH ARE REVIEWED THE ABUSES WHICH HAVE BEEN CORRECTED.` | 652 |
| `Article XXVII: Of Monastic Vows.` | 1084 |
| `Article XXVIII: Of Ecclesiastical Power.` | 1271 |
| **Declared range ends here, mid-article** | **1383** |
| Article XXVIII still running: "the observance of the Lord's Day, Easter, Pentecost" | 1461 |
| Article XXVIII's close: "a cause for schism." | 1526 |
| `CONCLUSION.` | 1531 |
| File's last non-blank line | 1567 |

Article XXVIII runs **1271–1526, about 256 lines**. The declared range covers **113 of them**. **Roughly 143 lines — about 56% of the article — are unread**, and so is the Confession's own **Conclusion (1531–1567)**, which is named nowhere in §11 item 2 or §12.

**Why it matters.** Three ways, and the third is the finding.

First, this is not a small tail. Article XXVIII is the Confession's longest and most consequential article on ecclesiastical power, and the unread half is where its argument actually lands: the bishops' power over traditions and consciences (1404–1419), the Lord's-Day passage (1461 ff.), and the closing appeal at 1516–1518 — "we are bound to follow the apostolic rule, Acts 5, 29, which commands us to obey God rather than men." §11 item 2's own list of terms "expected there and not yet carried" names "the limits of obedience," looking to *Secular Authority*'s unread third part for it; the Confession's own statement of that limit sits unread in a section the document says it read in full. It bears directly on §7 (the two governments, obedience) and on 6.7, which draws its AC evidence from inside this very article (AC 1276–1280).

Second, function. §12 exists to say what may and may not be relied on, and its closing sentence claims saturation "only for the sections read in full." A downstream builder reading §12 would conclude AC IV–XXVIII is exhausted for candidate terms. It is not.

Third, and this is the grading: **this item was affirmatively certified.** R3-1's finding was that a class of defect had been diagnosed and not swept, and its fix instruction was to "audit the remaining items on the §12 'read in full' list against the files in one pass... and say in §13 that the list as a whole was checked." Revision 3 says exactly that, in both §12 ("this whole list was audited item by item against the vendored files this revision") and §13 ("confirmed still accurate on this pass"). The audit found five items and missed a sixth, and the sixth is detectable the same way the other five were — by comparing the declared range in §13's own discovery row against the next structural heading in the file. By parity with N3 and R3-1, both graded substantial, so is this; it is aggravated, not mitigated, by the certification, because a later reader now has a stated warrant not to re-check.

**Mitigation, recorded as Rounds 2 and 3 did for the same class: no citation in the document is unwarranted by it.** I swept all 61 distinct AC loci cited anywhere in the 72 entries: the highest is **AC 1344**, and **every one falls inside 232–1383**. I also re-opened five of them (277–279, 502, 631–633, 789–791, 1276–1280) and each reproduces the document's quoted wording verbatim at the stated lines. The defect is in the coverage statement, not in the evidence.

**Fix.** Move AC Articles IV–XXVIII from §12's "read in full" list to the "read in part" list, described as what was read — Articles IV–XXVII in full and Article XXVIII to 1383 — and add Article XXVIII's remainder (1384–1526) and the AC's Conclusion (1531–1567) to §11 item 2's carry-forward. Correct §13's "confirmed still accurate" sentence, which is now itself the false claim. Do not reissue a certification sentence for the list as a whole without re-deriving every declared range from the files line by line; the two rounds in which the list was said to have been checked are both rounds in which it had not been.

## R4-2 — the hymnal-prefaces item, newly rewritten at Revision 3, misstates its own extent and folds two separate Luther pieces into one

**What the document now claims.** §12: "**The four hymnal prefaces** (Hy 890–1124): Luther's Fourth Preface, begun at 1103, continues past 1124 to **roughly 1230** before Hymn I's own heading at 1258; the declared range covers the first three prefaces in full and the Fourth Preface in part." §11 item 2 carries the same figure: "the hymnal prefaces' Fourth Preface beyond 1124 (**Hy 1124–1230**)."

**What is actually in `luther_hymns_bacon-allen.txt`:**

| Line | Content |
|---|---|
| 890 | `Luther's First Preface.` |
| 940 | `Luther's Second Preface.` |
| 1059 | `Luther's Third Preface.` |
| 1103 | `Luther's Fourth Preface` (to Valentine Bapst's Hymn-book, Leipzig, 1545) |
| 1178 | **End of the Fourth Preface** (its closing translator's note, "*Luther's mistake for _Michael Weysse_...") |
| 1182–1183 | `A Preface to All Good Hymn-Books.` / `By Dr. Martin Luther.` — from Joseph Klug's Hymn-Book, Wittenberg, 1543; the *Lady Musick* poem, ending with Winkworth's translation note at 1236 |
| 1240–1254 | `A Warning by Dr. Martin Luther.` — the four-line German verse and Massie's translation |
| 1258 | Hymn I |

So the declared range's first half is right — 890–1124 does cover the first three prefaces in full and the Fourth in part. **The unread remainder is stated wrongly.** The Fourth Preface's own unread tail is **1125–1178, about 54 lines**, not the ~106 implied by "roughly 1230." The rest of what the document assigns to it is two further, separately titled pieces of Luther's own material: a **fifth preface** and a **warning**, neither named anywhere in §12 or §11 item 2.

**Why this is substantial and not a rounding slip.** The fifth preface is not incidental to this document. Entry **4.9 hymn / "spiritual songs" / German singing** is built on the hymnal prefaces (Hy 896–930) and is tagged Tier 1 [SC] [RT]. "A Preface to All Good Hymn-Books" is Luther on exactly that subject — music's power over "hate, anger, envy," Saul and David's harp, the heart that "opens to God's Truth and Word" — and it is unread and undisclosed, because the coverage statement has absorbed it into another work's remainder. That is the same harm R4-1 does: a builder reading §11 item 2 is told what remains unread, and this piece is not on the list under any name. The heading itself is unambiguous in the file, on its own line, with its own attribution and source hymn-book, 56 lines before the next heading.

I note, in the fix's favour, that **no citation is affected** — no entry cites any locus between 1125 and 1257, so nothing relies on the misdescribed span.

**Fix.** State the Fourth Preface's true end (1178) and its true unread tail (1125–1178). Add "A Preface to All Good Hymn-Books" (1182–1236) and "A Warning by Dr. Martin Luther" (1240–1254) to §11 item 2 as named unread items, and flag the first of them at entry 4.9 as directly relevant unread material. Reconsider the phrase "the four hymnal prefaces," which the file does not support: five preface-titled pieces stand in this section, four of them numbered and a fifth titled.

---

# NEW COSMETIC FINDINGS

**R4-3 — Sermon 1's declared range overruns into Sermon 2, against §12's explicit "no overrun" verification.** §12 states the four sermons' ranges were "each range verified to run from its own sermon's heading to the next sermon's heading **with no gap and no overrun**." Sermon 1 is declared **14634–14833**; `THE SECOND SERMON` stands at **14827**. The declared range runs seven lines past the next sermon's heading, into its dateline and first sidenote. Sermons 2, 5 and 8 are exact (14827→14964, 15285→15423, 15611→15816), so this is the only one. Nothing is harmed — both sermons were read, and the overlap double-covers rather than leaving a gap — but the claim is falsifiable from the document's own two adjacent numbers without opening the file at all, which suggests the "no overrun" half of the certification was not run on this item. Correct Sermon 1's range to 14634–14826, or drop the "no overrun" clause.

**R4-4 — `Open_Gaps_Tracking.md` OG-1 presents a constructed sentence as a direct quotation of Doc_02 §17.** OG-1 reads: *Doc_02's own §17 states plainly: "This document does not claim the Zell thread is closed; that determination is left to the next reviewer or the coach thread."* **That sentence does not appear in Doc_02.** What Doc_02 §17 actually says is: "This document does not declare the Zell thread closed on its own say-so a sixth time; it records what was found and fixed, and treats 'self-disposition-ready' as a judgment for the next reviewer or the coach thread to make, not one more claim added to a list of five prior claims" — and, separately, in its status header: "This document does not claim the Zell thread is settled beyond doubt... the item is flagged as a standing note for the coach thread, not closed by this document's own say-so." **The substance is faithful** — both halves of the paraphrase are things Doc_02 genuinely says, and OG-1's characterisation of the Zell determination is accurate throughout. What is wrong is the form: two sentences from two places have been merged into one and put inside quotation marks with a section attribution. This is the project's own named recurring defect ("misattributed and mis-transcribed quotes have been a real, recurring defect here"), landing in a newly created durable governance record on its first day, and it is a larger version of what R3-4 was. Either quote one of the two sentences exactly, or drop the quotation marks and attribute it as a summary.

**R4-5 — §13's "every `Hy` locus... falls inside them" is overstated.** §13's Hy discovery row states: "None of these five corrections affects a citation: every `Hy` locus cited anywhere in the document was checked against the corrected boundaries and falls inside them." **The load-bearing half of that is true** — I verified independently that no cited `Hy` locus falls into any newly-declared-unread zone. But three cited `Hy` loci fall outside *every* declared read range: 558–561 and 766–768 (entry 4.9, Spangenberg's preface and Walter's reminiscence) and 651–652 (§10.3, Carlyle's "Here I stand" as Bacon quotes it). The first two are honestly handled — attributed to Registry rows R47 and R45 with "read by the Registry pass, not re-read here" — and the third is attributed to Bacon and barred by R94, so none is a fabrication risk. It is only the universal wording that does not hold. Say "no cited locus falls in a newly-unread zone," which is what was actually checked and what is actually true.

**R4-6 — 5.7's corrected gloss introduces one more locus outside every declared v2 range, unflagged.** The R3-5 fix correctly declares v2 10562–10566 as grep-located. In the same sentence it also newly cites **v2 7026** ("anchored to this same treatise's own earlier use of the term at v2 7026"). 7026 falls between the declared ranges 6470–6799 and 7100–7359, and is not declared or flagged anywhere. It carries no quotation, only a structural claim about where footnote [45] is anchored — which I verified is correct — so the exposure is small. But it is the same class R3-5 itself named, reintroduced by R3-5's own fix, which is the third time this pattern has appeared in this document's fix history. Either extend the v2 range or flag 7026 the way 10562–10566 is now flagged.

**R4-7 — the word-count figure does not reproduce, and the gap has grown.** §13 states "27,937 words by `wc -w` after Revision 3's edits." `wc -w` on the current file returns **28,440** — a difference of 503. Round 3 recorded the same figure failing to reproduce by 9 at Revision 2. A stated, re-runnable statistic that has now missed twice, by a growing margin, should either be re-run as the last edit before the revision closes or dropped.

---

# Statistics re-run and confirmed

Independently recomputed this round, all agreeing with the document: 72 entries; 39 / 27 / 6 tier split; 72/72 body-vs-Appendix agreement on Tier, Origin and Risk/Function; ten [AS] entries ({2.6, 2.7, 4.2, 4.4, 5.3, 6.1, 7.1, 7.5, 8.2, 8.4}); three [PV] ({5.6, 6.7, 7.4}); two [CT] ({2.2, 7.1}); 61 distinct AC loci, maximum 1344, all inside the declared range; four Kurze-Form loci, all inside the corrected range; every hymn locus inside the ranges actually read. The only statistic that did not reproduce is the word count (R4-7).

---

# What a Round 5 check should and should not do

Smaller than this round, and concentrated in one place.

1. **R4-1 and R4-2** — re-derive **every** declared range in §12 and §13's discovery table from the files by locating the next structural heading, including the items already corrected, and confirm §11 item 2 carries the AC Article XXVIII remainder, the AC Conclusion, the Fourth Preface's true tail, "A Preface to All Good Hymn-Books" and "A Warning by Dr. Martin Luther." This is the only item of weight, and it is the same item that has now carried a finding in three consecutive rounds.
2. **R4-3, R4-5, R4-6, R4-7** — four single-line checks against the files and one `wc -w`.
3. **R4-4** — open Doc_02 §17 and confirm OG-1 either quotes it exactly or no longer claims to quote it.
4. **Do not re-run** the 606-citation sweep, the 24-citation sample, the body-vs-Appendix cross-check, the thesis-number enumeration, the Doc_01 §8.4/§8.5 comparison, the Framework paragraph 97 check, or the `Hy`/Kurze-Form locus sweep. All came back clean at Rounds 2–4, and the fixes above touch §11, §12, §13, entry 5.7 and `Open_Gaps_Tracking.md` only.
5. **N5 remains open by design** and is now owned outside this document at `Open_Gaps_Tracking.md` OG-2. It does not need re-litigating. It does still need to be closed before disposition, and the marker layer grew again at Revision 3.

**Disposition: none claimed by this review.** Under the project's governance rule, no finding above may be closed by self-certification; each needs independent re-confirmation.
