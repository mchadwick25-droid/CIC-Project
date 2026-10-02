# Doc_02 / Source Registry — Independent Adversarial Review, Round 2

**Documents reviewed:** `witt_Doc_02_Source_Ecology.md` (Revision 1, 16,355 words) and `witt_Source_Registry.md` (Revision 1, 94 rows, 12,593 words), reviewed together as the two co-equal Step 2 outputs.

**Reviewer:** independent adversarial reviewer, no drafting context, cold. The Round 1 review (`witt_Doc02_Review_Round1.md`) was read as the checklist this revision was answering — but every Round 1 finding was **re-verified against the primary source directly**, not accepted as correct merely because the revision says it addressed it. That decision turned out to matter: three of Round 1's own claims were wrong, and the revision adopted them.

**Method.** Both word counts re-run by `wc -w` (16,355 / 12,593 — exact). All Registry summary statistics recomputed by script from the live table, plus an independent schema audit of all 94 rows. Roughly sixty citations re-located in the ten vendored files by `grep -n` and by direct line extraction (never by arithmetic from a neighbouring line). The Source Registry Template, the census entry VI.1 in full, Doc_01's §4 Zell paragraph, and the Gallic Registry rows 14–16 and 35 read directly. The six Karlstadt dates, the Amsdorf letter's 1534 date, the 1521 "sin boldly" letter, the 1535–45 Genesis lectures, Bale's 1546 translation, the Wallmann citation and the seven-measures list independently web-verified. Britannica, GAMEO and karlstadt-edition.org are egress-blocked from this session too, so the Karlstadt dates were checked against other hosts.

---

## VERDICT: MINOR ISSUES REMAIN

**3 SUBSTANTIAL findings, 5 COSMETIC.** All 10 Round 1 substantial findings and 12 of 13 cosmetics are genuinely and correctly fixed, checked against the sources rather than against the revision's own account of itself — including the three (S1, S2, S3) that were claims about the document's own verification discipline. The evidentiary spine is now very strong.

But the predicted risk materialised in the narrowest possible way. **Round 1's C3 contained three wrong line numbers, and the fix round wrote all three into the documents, breaking citations that had been correct in Revision 0** — while correctly catching a fourth wrong C3 claim and disputing it. And §17's headline assurance, *"Every disputed claim was re-checked against the actual source, not corrected on the reviewer's word,"* is falsified by those three: the ranges §17 lists as re-read are the very ranges that contain the right answers.

The remaining issues are all locally repairable. This does not need another full revision round; it needs a short targeted fix and an independent spot-check of the fix.

---

## Fix verification — Round 1 S1–S10

| # | Round 1 finding | Status | Evidence |
|---|---|---|---|
| **S1** | LC line spliced backwards; Lawrence made patron against pestilence | **FIXED** | LC 450–456 read in full. Doc_02 §6 now prints the sentence in source order with Lawrence against **fire** and Sebastian/Rochio against **pestilence**, cited 451–455 — exactly right, and the ellipsis correctly stands for the bracketed German-text insertion at 452–453. R25 now cites 453–455 for the fire/pestilence clauses (453 ends "if he was afraid of fire, he"; 455 ends "…or Rochio") and records the Revision 0 defect rather than certifying it. |
| **S2** | "Could not locate" the Cole Amsdorf heading | **FIXED** | Cole 15195–15235 read. Heading at 15209–15223, `TP` for `TO` as described, "FINIS." 15199, "1525" 15201, opening 15227, closing "my friend / Armsdorff" 16104–16105 — all verified. §16 item 6 struck; R35 re-tiered B→A for the passages read. |
| **S3** | Asserted absence the Apology refutes | **FIXED** | Apology 8438–8452 read. §1.3 now quotes 8447–8449 in Melanchthon's own voice at **[Documented]**, and correctly locates `_Confutation_` at 8442–8443 "two sentences earlier" (there are exactly two intervening sentences). R39 carries the locus. |
| **S4** | Sources named with no Registry row | **FIXED** | Britannica → R89, GAMEO → R90, Zorzin → R91, Wallmann → R92, Melanchthon's 1546 oration/preface-biography → R93. Doc_02 re-scanned for named-source-without-row: none found. R92's citation is exact (see "What held up"). |
| **S5** | Five-dimension claim delivered for two of six | **FIXED** | §3.4 now carries six separate entries (Philadelphia introducers, Aurifaber/Lauterbach, Bell, Bacon, Morley, Cole), each labelling Visibility / Representativeness / Influence / Limitations / Transmission. Every line the four rebuilt entries cite was spot-checked and sits inside a range an existing row records as read (R66, R69, R45, R67, R68, R33). |
| **S6** | Wikipedia-derived content tagged Documented; phrases quoted from an unopenable text | **FIXED** | §12.3 and §12.4 name Wikipedia explicitly at every point of use; both tags lowered to **[Widely Accepted]** with the reason stated; "three terrible sins" and "may be a true martyr" are now paraphrased without quotation marks, matching the prior treatment of "smite, slay and stab". R83 capped at B as tertiary. |
| **S7** | Zell excluded on half the census and on a test Grumbach never faced | **PARTIALLY FIXED** | Census disclosure is now complete and honest (verified against the JSON: the `voices` array and the `statusDescription` say what §15 and R55 say they say). One test is now stated and Grumbach is run against it. But the 1524 pieces are excluded on a criterion the stated test does not contain, the Template's own overlap-permissive paragraph is not engaged, and §11 and §12.1 were never reconciled with the determination. See **N2** and **N3**. |
| **S8** | No Named Comparandum row for the wider Luther corpus | **FIXED** | R94 exists, Excluded / Named Comparandum, with a substantive Comparandum Note and an explicit supersession of R69's item-level caution. Gallic Registry row 35 read directly — the precedent is real and R94 is modelled on it correctly. |
| **S9** | Marburg Articles mis-marked "(context)" | **FIXED** | R56 no longer carries the marker; script confirms exactly six "(context)" rows (R36, R39–R43), all opponent texts. §1.3 and §13 both state the confinement rule and R56's exception in matching terms. |
| **S10** | Confidence tiers silently redefined, then not followed | **FIXED** | The Conventions paragraph now reproduces the Template's A–D wording verbatim (E loses one sentence — N5). Tallies recomputed by script from the live table: **94 rows, 89 Native / 5 Excluded, A 50 / B 42 / C 2 / D 0 / E 0, 6 "(context)" rows = R36, R39–R43** — every figure matches the claim exactly. A small residual application inconsistency at R59/R60 is at N5. |

## Fix verification — Round 1 C1–C13

| # | Status | Evidence |
|---|---|---|
| **C1** | **FIXED** | §3.1 now "Eight of the ten files are Luther; the other two (AC/Apology)". All word-count figures re-run and exact (471,515 ≈ "~470,000"; 116,624; 52,785; 58,055; 125,737; total 824,716). |
| **C2** | **FIXED** | `grep -o "Jew"` across all ten files returns **198**. §12.3 now says 198 and notes the recount. |
| **C3** | **PARTIALLY FIXED — and the source of this round's worst regression** | Five items. **v1 "mid-day" 473→474: correctly fixed** (474 = "but mid-day[3] when the Theses were nailed up"). **LC "ma-servants": the revision disputed Round 1 and is right** — 335 = "household is obliged to do the same with respect to his domestics,", 336 = "ma-servants and maid-servants…", so R25's 335–336 and Doc_02 §6's 334–336 are both correct as Revision 0 had them. **The other three were correct in Revision 0, wrong in Round 1, and are now wrong in Revision 1.** See **N1**. |
| **C4** | **FIXED** | v3 20784–20790 read: the editor gives no year for the conversion to a duchy and dates the marriage "July 1, / 1526". §4 and R24 now attribute the 1525 to the builder. |
| **C5** | **FIXED** | SC 38–40 is the translator's note ("This version of the Small Catechism is under continuous / revision."); 19–24 is this project's intake header. R65 cites 38–40 and records the error. |
| **C6** | **FIXED** | R49 closes the Bertram/Sherman non-discrepancy explicitly (Bertram translated, Sherman edited vol. 47). Independently confirmed. |
| **C7** | **FIXED** | R86 raised to A / **[Widely Accepted]**, with the 1523 *Deuttung* identified, Cranach workshop named, Melanchthon→Papal Ass and Luther→Monk Calf stated, and the "Whore of Babylon" gloss explained. Second-opinion flag withdrawn, consistently, in both row and summary. |
| **C8** | **FIXED** | v1 165–178 read. §2 now gives "with especial reference to the discussions which, we have every reason to believe, will then occur" with "then" glossed, cited 171–175. Exact. |
| **C9** | **FIXED** | "Sacramentarians": Cole 16090 (Luther's voice, once); v1 10661, 10727 (editorial), 15611 (index). §13 now accounts for all four. |
| **C10** | **FIXED** | LC 3277 "enthusiasts", 3841 and 3916 "new spirits", 4069 "prating of nearly all the fanatical / spirits", 4095 "all fanatics" — all five verified at the exact lines. Used in §12.5 and §13 as support for the finding, not against it. |
| **C11** | **FIXED** | R87 restructured: the source is now the translators' glossing footnotes (v1 344–346 verified: "[5] _Des Pabats Drecet and Drecketal_…"), Licensed For is real and unconditional, the lexicon absence moved to §16 item 9. Confidence D→A. |
| **C12** | **FIXED** | Script-checked: the ten rows the summary lists (R48, R49, R50, R52, R54, R72, R82, R89, R90, R91) are exactly the ten rows carrying "Flagged for second-opinion review" in their own Verification Notes. R86's withdrawal is recorded in both places. |
| **C13** | **FIXED** | §2 item 1 now "the library's *fullest* connected narrative", with Bacon and Morley acknowledged. §3.4's narrower "the library's only account of the hymnals' publication history 1524–1545" is defensible. |

---

## New findings

### N1 — SUBSTANTIAL. Three citations that were correct in Revision 0 are now wrong, and §17's "re-checked against the actual source" claim is falsified by them

Round 1's C3 asserted five ±1–2 line offsets. Two of its five claims were wrong. The revision caught one of them (the LC "ma-servants" range — correctly, see below) and swallowed the other three, moving correct line numbers onto wrong lines.

Verified by `grep -n`, which is the method Round 1 itself said it used:

| Citation | Revision 0 | Round 1 C3 said | Actual (`grep -n`) | Revision 1 now says |
|---|---|---|---|---|
| v3, *Teutonic Order* title "…lay aside false chastity and take upon them the true chastity of wedlock" | 20634–20635 | "actual 20632–20633" | **20634–20635** | **20632–20633** (Doc_02 §12.1) — blank lines |
| v3, the AC-XVI Anabaptist footnote | 11776 | "actual 11775" | **11776** | **11775** (R20) — a blank line |
| v3, *Secular Authority* dedication heading | 11804 | "actual 11803" | **11804** | **11803** (R20) — a blank line |

```
20634:THAT THEY LAY ASIDE FALSE CHASTITY AND TAKE
20635:UPON THEM THE TRUE CHASTITY OF WEDLOCK
11776:1The Anabaptists. See Augsburg Confession, Article xvi.
11804:LETTER OF DEDICATION
```

Two aggravating facts.

**First, R20 now asserts the error as a correction**: "(Both loci corrected by one line at Revision 1 — Round 1 C3.)" A row that had two right numbers now has two wrong ones and a sentence certifying the change. This is the project's named "no fix on a fix" hazard in its literal form.

**Second, §17 claims these exact ranges were re-read.** Its fix log lists, as ranges re-checked against the actual source, "v3 20630–20636, v1 472–475, v3 11773–11777 and 11801–11806, LC 332–337 (C3)". Every one of those ranges **contains the correct line**. So either the ranges were not opened, or they were opened and the reviewer's numbers were written down anyway. Either way the sentence *"Every disputed claim was re-checked against the actual source, not corrected on the reviewer's word"* is not true as written, and it is a claim about the documents' own verification discipline — the same category as S1, S2 and S3, which Round 1 asked to be fixed first and independently confirmed.

Note that R24's own heading range (20627–20638) still brackets the right lines, so the Registry and Doc_02 §12.1 now disagree with each other about where the same title sits.

**Fix:** restore 20634–20635, 11776 and 11804; delete R20's "corrected by one line" sentence; and rewrite the §17 assurance to say what actually happened — including that Round 1 was wrong on three of five C3 items and right on two.

*(For the record, on the one place the revision disagreed with Round 1: the revision is right. LC 335 reads "household is obliged to do the same with respect to his domestics," and 336 "ma-servants and maid-servants and not to keep them in his house if they". R25's 335–336 for the short quotation and §6's 334–336 for the long one are both correct, and Round 1's C3 claim on that item was mistaken. The disagreement is well-reasoned and well-evidenced; it should have been extended to the other three.)*

### N2 — SUBSTANTIAL. §11 and §12.1 were never reconciled with the Zell determination §15 now makes

§15 item 4 and R55 determine Zell **Excluded / Named Comparandum**, with a Comparandum Note that says she must "not to be reached for as a 'Lutheran woman's voice'". Two sections that the fix round did not touch still treat her as one of this world's own.

- **§11, "Lost voices":** "the visited villagers of 1527–28 (recorded, but not here); **Grumbach and Zell (published, but not here)**; the Brussels friars…". A source determined not to belong to this world is not one of this world's lost voices. As written, §11 asserts the opposite of §15.
- **§12.1, Missing Voices, closing sentence:** "**The named, unvendored voices remain the real answer:** Argula von Grumbach [R54] — Native… — and Katharina Schütz Zell [R55], whose placement Doc_01 open item 4 asked this document to settle (§15)." The pointer to §15 is a half-disclosure; the framing sentence still offers Zell as part of the answer to this world's women's-voices gap, which R55 forbids. A Doc_03 or acquisition pass reading §12.1 would take Zell as a target.

This is the standard fix-round defect — a rewritten section and an untouched section now contradicting each other — and it lands in the Affirmative Duty section, which the Framework (para 184) makes participant-facing.

**Fix:** §11 should list Zell under the Excluded determination with a cross-reference, not under "Lost voices"; §12.1's closing sentence should name Grumbach as the answer and Zell as determined out, with the determination's own caveat.

### N3 — SUBSTANTIAL. The boundary test is one test in name, but the 1524 Zell pieces are excluded on a criterion it does not contain — and the Template is cited selectively, the same defect S7 caught at the census

The census disclosure is now genuinely honest: I read `world-census.json` and confirmed all three elements — the sources-block "wider evangelical orbit, placement note", the `voices` array's fifth entry ("Katharina Schütz Zell — Strasbourg pastor's wife who published devotional writing, hymn collections and open letters in her own name"), and the `statusDescription`'s "including women's voices in verified modern editions (Argula von Grumbach, Katharina Zell)". §15 and R55 quote all three and state the override rather than implying it. That half of S7 is fixed properly.

The argument is where it still does not hold.

**(a) The stated test has two branches, and the 1524 pieces fall into neither.** The test as written: *"Native if its own subject is the Wittenberg-led movement… Excluded if its subject is a church or cause that, on the writing's own evidence, belonged to a different confessional line."* The document then finds the Kentzingen letter's and *Apologia*'s subject to be "the undivided evangelical movement of 1524" — which is, on the document's own words, **not** a different confessional line. It resolves the gap by adding a third criterion that appears nowhere in the stated test: "not for Wittenberg's cause **by name** as Grumbach's pamphlets do." That naming criterion is applied only to Zell. Grumbach's 1523 pamphlets and Zell's 1524 letters are a year apart and both precede the confessional split; the whole determination for the two strongest counter-cases now rests on whether Luther and Melanchthon are named in the text — and the Grumbach side of that comparison is itself **unread prior knowledge** (R54 is Confidence B, "content basis is prior knowledge… flagged for second-opinion review"). An unverified claim is carrying the decisive asymmetry between the two women.

**(b) The Template is quoted for the half that excludes and not the half that permits.** §15 calls its test "the Template's own", and the "assessed by what a source speaks *for*… never by where or when it was written" half is quoted accurately. But the Template's very next paragraph is the one that bears hardest on this case, and neither Doc_02 nor R55 engages it:

> **Native does not mean exclusive to this world, and it was never supposed to.** … The question this check asks is never "does another world already have this" — it is simply **"was this source actually used, inherited, or drawn on as part of this world's own formation, on this world's own evidence?"** … The failure this mechanism exists to prevent is not overlap — overlap is often exactly right.

R55's Comparandum Note states the temptation as "a Reformation-era woman's voice looks Native to the world that most lacks one" — which is a reason for care, but the Template says the question is never whether another world has a claim. Selective citation of the governing source is precisely the defect S7 found at the census; it has been fixed at the census and reappeared, one layer up, at the Template.

**(c) R55 excludes her without allocating her.** R57 names its home world (VI.2, `the-reformed-cities-zurich-and-geneva`). R55 names none — Strasbourg is not VI.2. So the only world in the census that names Zell as one of its voices has now excluded her, and no other world holds her. That is worth stating in the row.

**On the escalation question the revision raised and declined:** I think the revision's self-assessment is **defensible, and I would not escalate it** — but for a reason the document does not give. Doc_01, which is APPROVED, delegates this decision explicitly: *"Doc_02 should settle whether Zell belongs to this world's own congregational record or is better treated as an adjacent-world witness, rather than this document assuming the placement."* Excluded / Named Comparandum is exactly the second of Doc_01's two named options. An approved document handing a build thread a binary and the thread choosing one of the two branches is not a portfolio-level decision under CO-022 escalation category 2. §15 and §17 should cite that delegation — it is a better argument than the one they make, and it would let the item be disposed rather than left hanging. What must not be disposed on this argument is (a) and (b): the determination needs to be argued against the whole of the Template's boundary rule, including the overlap paragraph, or restated as a licensing decision ("not usable as this world's women's register on the current evidence") rather than a boundary determination.

### N4 — COSMETIC. The summary mischaracterises three of the sixteen unvendored leads

Summary statistics: "**Unvendored primary leads with a row:** 16 (R48–R62, R93), each Licensed For disclosure or named absence only". R55, R57 and R58 are inside that range and are Excluded, with blank Licensed For by the schema the same summary certifies two bullets earlier. The count is right; the characterisation is not true of three of the sixteen.

### N5 — COSMETIC. Two residual Confidence-tier inconsistencies

1. **R59 and R60 are the only two C rows, and they satisfy the Template's B.** The Template's B is "Specific work/locus named"; R59 names *Formula Missae* (1523) and *Deutsche Messe* (1526) by title and date, R60 names *Das Newe Testament Deutzsch* (September 1522) and the 1534 German Bible — and both rows point at loci inside the library where those works are referenced. Meanwhile R48 and R50 were moved C→B on the stated ground that "a specific locus is named". The operative distinction the Registry is actually applying is *"a modern edition is named"*, which is neither the Template's B nor its C. Either move R59/R60 to B or state the edition criterion.
2. **"verbatim" is very nearly verbatim.** The Conventions paragraph reproduces A–D exactly but gives E as "No traceable source", dropping the Template's second sentence ("Not a resting tier — remove or re-ground to at least D"). Immaterial to the tallies (E 0), but the paragraph's own word is "verbatim".

### N6 — COSMETIC. §16 item 6's stated reason for keeping its number does not hold

Item 6 is struck, "the number is kept so that item 8's range still reads." Item 8's range reads "items 1–7 and 9–12 here" — which includes the struck item 6 inside "1–7". Either the range should read "1–5, 7 and 9–12" or the justification should change.

### N7 — COSMETIC. R94 scopes itself by row numbers that include three non-Luther rows

R94 bars "everything of Luther's beyond the works rowed above (**R1–R35 vendored**…)". R32 is Aurifaber's testimony, R33 is Bell's *Narrative* (itself Excluded), and R36 — immediately outside the range — is Erasmus as embedded in the vendored file. In a Boundary-Status-level row whose whole function is an unambiguous bar, the scope should be stated by content ("the vendored Luther works, R1–R31 and R34–R35") rather than by a row span that includes two other authors.

### N8 — COSMETIC. A short residual citation sweep

- §3.1 cites hymns line **1087** for "sold under our name"; the phrase spans 1086–1087 ("come to be sold / under our name"). R28 has it right at 1086–1087.
- Cole's Erasmus quoting rule: Doc_02 §1.3 and §3.4 cite **218–227**, R36 and R68 cite **218–230**. The passage runs 218–225 (line 230 is blank). Harmless, but the two documents should agree.
- R87 reconstructs the footnote as "*Des Pabsts Drecet **und** Drecketal*" and flags only `Pabats`→`Pabsts`; the file at v1 344 reads "and", not "und". Flag both or neither.

---

## What held up

I went at the items the revision itself nominated for a second look, and at the standard fix-round defects. Most of it holds, and some of it holds better than the revision claimed.

**The Registry's arithmetic and schema are exact, recomputed independently.** 94 rows, sequentially numbered with no gaps; 89 Native / 5 Excluded; Confidence A 50 / B 42 / C 2 / D 0 / E 0; exactly six "(context)" rows and they are R36, R39, R40, R41, R42, R43; Type tallies P 64 / S 25 / S/P 1 / M/S 1 / M 1 / M/P 1 / L/S 1 = 94. A full schema audit found **zero** violations: every Native row has a non-empty Licensed For and a blank Exclusion Reason; every Excluded row has an Exclusion Reason and a blank Licensed For; all four Named Comparanda carry Comparandum Notes; the Boundary column contains only Native or Excluded. The ten "flagged for second-opinion review" rows are exactly the ten the summary lists. Both documents' stated word counts reproduce to the word.

**All six Karlstadt dates hold up, independently verified.** The three hosts really are blocked from this session as well (Britannica, GAMEO and karlstadt-edition.org all returned `EGRESS_BLOCKED`), so I checked elsewhere. Every date in §15 item 10 and R89 is correct: Orlamünde pastorate **May 1523**; exile from Saxony by Frederick the Wise and Duke George **September 1524**; hidden in Luther's house for eight weeks during **1525**; left for Switzerland in **1529** (via Holstein and East Friesland, so "Switzerland from 1529" is Britannica's own phrasing and the right one to have used); Old Testament professorship at **Basel from 1534** until his death; died at Basel **24 December 1541, of the plague**. The three dates the revision could not re-verify (1524, 1525, 1529) are the three I can now confirm. The rows' honesty about what was and was not opened is exemplary and should be kept as written even though the content checks out — but §16 item 11 can be closed and R89–R91's flags reduced to "chronology independently confirmed at Round 2; interpretive frames still unread."

**The three other new prior-knowledge claims are correct.** The Amsdorf letter is the 1534 "Letter of Luther Concerning Erasmus" — the 1534 date in §0 and R35 is right. "Sin boldly" is the letter to Melanchthon of 1 August 1521 from the Wartburg (*pecca fortiter sed fortius fide*) — R94's "letter to Melanchthon, 1521" is right. The Genesis lectures ran 1535–1545 — R94's dating is right. Bale's 1546 English rendering of Melanchthon's funeral oration is corroborated at search level, which is exactly the level R93 and §16 item 10 claim for it ("search result, not examined").

**The §12.3 disclosure reproduces its tertiary source faithfully, including the point most likely to drift.** I fetched the Wikipedia article and compared the seven measures item by item. All seven match, including the second — "to refuse to let Jews own houses among Christians", which Doc_02 renders "that Jews be forbidden to own houses among Christians" rather than reaching for the more commonly quoted "razed and destroyed". That is the harder and more honest choice: the document reports what its named source says, not what the memory of the text says. R92's citation is exact against the article's own bibliography (*Lutheran Quarterly*, Spring 1987, 72–97).

**The census disclosure is complete and fairly stated.** I read the VI.1 entry in full. All three elements are reported accurately, the `voices` array does have five entries as §15 says, and the override is stated in both the document and the row rather than left implicit. On the one point Round 1 pressed hardest — citing only the supporting half — the revision has done the work.

**The Gallic precedent is real, again.** Rows 14–16 carry **(context)** exactly as described, and row 35 is "The rest of Augustine's corpus… Excluded / Named Comparandum" with the generation-risk note. R94 is a faithful adaptation of it, not an invented cross-reference.

**Citation fidelity outside N1 is high.** Roughly sixty loci re-located, including every line the four rebuilt §3.4 entries cite and every line the fix log claims to have re-read. Verified exact: LC 92–98, 241–243, 245–247, 330–336, 451–455, 3277, 3504, 3841, 3916, 4069, 4095; SC 38–40, 445–446, 454, 557–558, 649; AC 49–51, 253, 314, 351, 418, 440, 754–756, 765–766, 1559–1567 (nine signatories, correctly listed); Apology 97, 156, 2359, 4145, 4701, 4909–4910, 5171, 5407, 5778, 5867, 5915, 6333, 7595, 8442–8449, 8490–8496, 8512–8514, 8531; v1 165–178, 344–346, 470–478, 488–491, 10661, 10727, 12283–12309, 15611; v2 107–109, 13182–13183, 14446, 14676–14681, 15834–15841; v3 10556–10586, 10665–10672, 14553–14557, 20627–20638, 20784–20790; hymns 105–110, 556–571, 601, 651–652, 690–692, 711, 743–795, 819–824, 831–832, 856–866, 874–881, 919–922, 960, 975–985, 1068–1069, 1086–1087, 1744–1745, 1759–1760, 1799–1800, 3667–3668, 3708; TT 84–90, 94–120, 135–156, 1040, 2394–2395, 3013–3015, 3100–3102, 3129–3135, 3147–3148, 3508–3509; Cole 154, 186, 200, 218–225, 759, 15199–15235, 16090, 16104–16105, 16272.

**The negative searches re-run true.** "Zwingli" and "Marburg": zero hits in all ten files, checked file by file. "Jew": 198. "Sacramentarians": four hits, one in Luther's voice. The S1-pattern ellipsis sweep claim holds — I checked every elided quotation in §5, §6, §7, §12.1, §12.3, §13 and found no second inversion.

**The Round 1 disagreement was right, and stating it as a disagreement was the right call.** The revision could have absorbed C3's ma-servants claim silently and did not. That behaviour is what should have been applied to the other three C3 items, and the fact that it was applied once shows the capability was there.

---

## Recommended disposition

**Not ready to self-dispose as "Approved to proceed" under CO-022 — but close, and not by another full revision round.**

CO-022 lets a build thread dispose of procedural work itself; it does not let a blocking finding be closed by self-certification. N1 is a blocking finding in this project's most-named defect class (citations pointing at the wrong lines, plus a false claim about the documents' own verification), and N2 is a live internal contradiction inside the Affirmative Duty section. Both are small and mechanical to repair.

**Scope the fix to exactly this, and nothing else:**

1. **N1** — restore v3 20634–20635 (Doc_02 §12.1), 11776 and 11804 (R20); delete R20's "corrected by one line" sentence; rewrite §17's re-check assurance to record that Round 1's C3 was wrong on three of five items and that Revision 1 adopted the errors before Round 2 caught them. Do not touch the two C3 items that are now correct (v1 474; LC 334–336 / 335–336).
2. **N2** — reconcile §11's "Lost voices" list and §12.1's closing sentence with §15/R55.
3. **N3** — add the Template's overlap paragraph to §15's and R55's reasoning and answer it; state the "by name" criterion as part of the test or drop it; cite Doc_01's own delegation of this decision as the escalation answer; name in R55 that no other census world currently holds Zell.
4. **N4–N8** — a single cosmetic pass.
5. Close §16 item 11 and soften R89–R91's flags on the strength of the Round 2 verification recorded above (the Karlstadt chronology is now independently confirmed; the interpretive frames remain unread).

**Then a spot-check, not a re-review.** Per the from-round-2-onward discipline, a short independent pass over only the lines and sentences the fix touches — re-located by `grep -n`, not by arithmetic — is sufficient to dispose. Everything else in these two documents has now been checked twice by two independent reviewers and holds.

**One standing note for the next fix round, and for the project generally.** The specific failure in N1 is that a reviewer's line numbers were treated as authoritative. They are not. A review finding is a *prompt to check the source*, and Round 1's own C3 is the proof — three of its five line numbers were wrong. The fix round already knew this well enough to dispute one of them. The rule that would have caught all four: never change a line citation without printing the line.
