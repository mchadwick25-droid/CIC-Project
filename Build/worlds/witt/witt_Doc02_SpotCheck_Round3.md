# Doc_02 / Source Registry — Bounded Spot-Check

**Documents checked:** `witt_Doc_02_Source_Ecology.md` (DRAFT, Revision 2, 359 lines) and `witt_Source_Registry.md` (DRAFT, Revision 2, 95 rows).

**Scope:** only the prior pass's own findings — N1–N3 (substantial), N4–N8 (cosmetic), and the prior pass's item 5 (the Karlstadt flag softening), per this project's own bounded spot-check precedent (`gallic_Doc01_SpotCheck_Round3.md`, `witt_Doc01_SpotCheck_Round3.md`). The substantive historical and methodological content already found sound was **not** re-reviewed. Everything this fix pass added or changed was independently re-verified against its actual source — every line citation printed from the vendored file by `awk`, every statistic recomputed by script from the live table, the Template and Doc_01 passages read directly. No number was taken from any earlier pass's or this revision's own word.

**Checked against:** `cic/texts/luther_works-v3-selected_various1930.txt` (20627–20640, 11773–11778, 11800–11808); `cic/texts/luther_bondage-of-the-will_cole1823.txt` (214–234); `cic/texts/luther_hymns_bacon-allen.txt` (1082–1090); `cic/texts/luther_works-v1-selected_jacobs-spaeth1915.txt` (342–348); `Build/reference/L3B-World-Build-Methodology/Source_Registry_Template.md` (read in full, boundary-check section lines 48–61); `witt_Doc_01_World_Identification_Boundaries_Orientation.md` §4 and open item 4; `cic-website/data/world-census.json` (parsed, all `Zell` occurrences); `Build/reference/Project-Reference/CiC_OneDocAtATime_Build_Protocol_2026-07-06.md` (CO-022 and the four escalation categories); `witt_Doc02_Review_Round2.md` in full.

---

## VERDICT: SUBSTANTIAL REVISION STILL REQUIRED

**Narrowly scoped, but genuinely substantial, and it is the same item failing for a third consecutive pass.**

Most of this fix pass is excellent, and better than the last one. **N1 is fully and correctly fixed** — v3 20634–20635, 11776 and 11804 were printed directly and all three are exactly what the documents now cite, R20's false "corrected by one line" sentence is gone and replaced by an honest account, and §17's earlier-revision log now states plainly that three of the first pass's five C3 claims were wrong and were adopted before the second pass caught it. **N7 and N8 are fully fixed**, and on N8 this revision was right to reject the earlier pass's own suggested Cole range: line 230 is not blank, it reads "seintiments in substance only.", and 218–230 is the correct span of the numbered item. **Every Registry statistic reproduces exactly** — 95 rows, sequential, no gaps; 90 Native / 5 Excluded; A 50 / B 45 / C 0 / D 0 / E 0 with the stated row ranges exact; Type tallies exact and summing to 95; six "(context)" rows and they are the six named; the ten second-opinion flags are the ten listed. **The census disclosure, the Template quotation and Doc_01's delegation are all quoted verbatim and accurately**, checked against the JSON, the Template and Doc_01 directly.

But the revision did to N2 exactly what Revision 1 did to C3. **§11 and §12.1 were rewritten to match Revision 1's blanket-Excluded determination, and then §15/R55 changed the determination to a split, and nobody went back.** Both sections now state, in the documents' own words, that "Registry R55 determine her Excluded / Named Comparandum" — and R55's Boundary column reads **Native**. The contradiction N2 named is not fixed; it has been inverted. And §17 logs it as fixed. That is the same class of claim-about-its-own-state flagged previously, on the same item (Zell) that has had to be reopened twice before.

Separately, the N3 rework's decisive argument does not close. The test §15 now states in bold requires, on its Native branch, that "the writing's own evidence shows it drawing on, defending, or addressing the Wittenberg-led movement's own cause **by name**." The Grumbach application satisfies that ("cite Luther and Melanchthon by name"). The Zell application supplies no naming at all — it supplies shared window, shared cause and a not-yet-divided milieu — and then asserts "On the test's Native branch, that is enough." It is not enough on the branch as written. The prior pass gave two options: state the naming criterion as part of the test, or drop it. Revision 2 stated it *and* then decided the case against it.

Everything else remaining is small and mechanical.

---

## Fix verification — prior pass's N1–N8

| # | Status | Why |
|---|---|---|
| **N1** | **FIXED** | Printed directly: `20634:THAT THEY LAY ASIDE FALSE CHASTITY AND TAKE` / `20635:UPON THEM THE TRUE CHASTITY OF WEDLOCK`; `11776:1The Anabaptists. See Augsburg Confession, Article xvi.`; `11804:LETTER OF DEDICATION`. Doc_02 §12.1 cites 20634–20635 ✓; R20 cites 11776 and 11804 ✓; R24's heading range 20627–20638 still brackets the title correctly, so Registry and §12.1 now agree. R20's "corrected by one line" sentence is gone, replaced by an accurate account of the Revision 1 error. §17's earlier-revision log now says C3 "is the exception, and it is a real one," names the three wrong items, and states the errors were written in "without re-opening the files" and were found by a later, independent pass, not by this thread. Honest as required. |
| **N2** | **NOT FIXED** | §11 line 237 and §12.1 line 261 both now read "§15 item 4 and Registry R55 determine her Excluded / Named Comparandum." R55's Boundary column reads **Native**. The sections were reconciled with the determination that Revision 2 then replaced. See New-1. |
| **N3** | **PARTIALLY FIXED** | (a) The Template's overlap paragraph is now quoted directly and accurately (verified against Template line 52; the elision covers only "If yes, it is Native here…", which would have *helped* the document's case, so the elision is not self-serving) — but the test as restated keeps the "by name" criterion and the Zell application does not meet it, while claiming to. See New-2. (b) R55 / R95's division **is** consistent with §15 as to substance (R55 = the two 1524 pieces; R95 = hymn collection, 1553 Schwenckfeld letter, 1557 Rabus letter, 1558 meditations), with one wording mismatch and one unallocated gap — see New-6. (c) **Statistics recomputed independently and every figure is exact** (detail below). (d) **Escalation grounding verified and sound:** Doc_01 line 67 reads verbatim "Doc_02 should settle whether Zell belongs to this world's own congregational record or is better treated as an adjacent-world witness, rather than this document assuming the placement," and open item 4 is "not resolved here." A split is a considered answer to a delegated Step-1 question, and the document says so. The census claim also holds: parsing `world-census.json`, Zell occurs **only** in movement VI.1 (three places, all quoted accurately), so "no other census-listed world currently claims her" is true. |
| **N4** | **PARTIALLY FIXED** | The mischaracterisation is genuinely corrected — the bullet now distinguishes Native disclosure rows from the Excluded rows in the same span, and R94/R95 are counted separately. But the enumeration no longer adds up: "17 (R48–R56, R59–R62, R93, R95, plus R54/R55 for Grumbach/Zell)" sums to **15**, and "plus R54/R55" double-counts two rows already inside R48–R56. 17 is right if the set is R48–R62, R93, R95. Revision 1's arithmetic ("16 (R48–R62, R93)") was correct; this fix broke it. See New-4. |
| **N5** | **FIXED** | Both parts. R59 and R60 now read **B**, and B is right on the Template's own wording ("Specific work/locus named, not independently re-checked this session") — *Formula Missae* (1523), *Deutsche Messe* (1526), *Das Newe Testament Deutzsch* (Sept. 1522) and the 1534 Bible are all specific named works with named loci; C 0 confirmed by script. The E definition now reads "No traceable source. Not a resting tier — remove or re-ground to at least D." — I compared all five tiers against Template lines 42–46 and A–E are now verbatim, with the departure disclosed. |
| **N6** | **PARTIALLY FIXED** | §16 item 8 now reads "items 1–5, 7 and 9–12 here (6 and 11 are struck/closed, not seeds)." Item 6 is out of the range, but **item 11 is still inside "9–12"** while the same parenthetical declares it not a seed — the identical defect N6 named, moved one item along. Should read "1–5, 7, 9, 10 and 12." See New-5. |
| **N7** | **FIXED** | R94 now reads "the vendored Luther works specifically, R1–R31 and R34–R35." Verified against the Source column of every row: R1–R31 are all "Luther, …" (R31 is the Table Talk, Luther's speech, correctly counted); **R32 is Aurifaber's *Testimony* and R33 is Bell's *Narrative*, neither a Luther work**; R34 and R35 are Luther's. The scope statement is now accurate and content-stated rather than span-stated. |
| **N8** | **FIXED — all three, and one of them against the prior pass's own finding** | (i) hymns: printed 1086 "…come to be sold" / 1087 "under our name." — Doc_02 §3.1 now cites 1086–1087 ✓, matching R28. (ii) Cole: printed 214–234. The numbered item "4." runs 218–230; **line 230 is not blank** (`230:seintiments in substance only.`), so the prior pass's own "the passage runs 218–225 (line 230 is blank)" was wrong and Revision 2's 218–230 is right. Doc_02 §1.3 and §3.4 now both cite 218–230, matching R36 and R68 — the two documents agree, which is what N8 actually asked for. (iii) R87: printed v1 344 — `[5] _Des Pabats Drecet and Drecketal_.` The row now quotes "Pabats" and "and" exactly as the file prints them and discloses that Revision 1 had silently emended both while flagging one. ✓ |

**The prior pass's item 5 (Karlstadt flags):** §16 item 11 is closed and the closure is accurately grounded on the prior verification. The flag softening, however, exists **only** in the Registry's summary-statistics bullet — R89, R90 and R91 each still carry an unmodified "**Flagged for second-opinion review** (Doc_02 §16 item 11)" pointing at an item that now reads "Closed." See New-7.

**Statistics, recomputed from the live table by script (not tallied by hand, not read off the document):**

- 95 rows, numbered 1–95, sequential, no gaps, no duplicates ✓
- Boundary: **90 Native / 5 Excluded** ✓ — Excluded are R33 (Out-of-Boundary), R57, R58, R94, R95 (Named Comparandum) ✓; four Named Comparanda, all carrying Comparandum Notes ✓
- "(context)" marker: exactly 6 rows, R36, R39, R40, R41, R42, R43 ✓
- Confidence: **A 50 / B 45 / C 0 / D 0 / E 0** ✓, and the stated ranges are exact — A = R1–R2, R7–R9, R14–R47, R63–R69, R85–R88; B = R3–R6, R10–R13, R48–R62, R70–R84, R89–R95 ✓
- Type: P 65 (R1–R62, R93–R95), S 25 (R63–R79, R81–R83, R88–R92), S/P 1 (R80), M/S 1 (R85), M 1 (R84), M/P 1 (R86), L/S 1 (R87) — sums to 95 ✓
- Schema audit: every Native row has a non-empty Licensed For and blank Exclusion Reason; every Excluded row has an Exclusion Reason and blank Licensed For; Boundary column contains only Native or Excluded — **zero violations** ✓
- Second-opinion flags: exactly the ten listed (R48, R49, R50, R52, R54, R72, R82, R89, R90, R91); R86's withdrawal is recorded in both places ✓
- Vendored primary works with a row: 35 (R1–R35) ✓

Every figure the Registry claims is correct. The one arithmetic defect is in the *enumeration* at the unvendored-leads bullet, not in any tally.

---

## New findings introduced or left by this fix pass

### New-1 — SUBSTANTIAL. §11 and §12.1 now assert the opposite of §15 and R55, and §17 logs it as fixed

This is N2, not fixed but inverted, and it is the third consecutive pass in which the Zell item has left the two documents disagreeing with themselves.

- **§11, "Lost voices" (line 237):** "**Not Zell:** §15 item 4 and Registry R55 determine her Excluded / Named Comparandum — her own corpus speaks for Strasbourg's church, not this world's — so she is not counted among this world's own lost voices."
- **§12.1, closing sentence (line 261):** "**Katharina Schütz Zell does not** — §15 item 4 and Registry R55… determine her Excluded / Named Comparandum: her own corpus, on the argument made there, speaks for Strasbourg's own church rather than for this world… she is not this gap's answer."

R55's Boundary column reads **Native**. Its Licensed For reads "Disclosure of a real Missing Voices gap (**§12.1**); a 1524 lay-evangelical parallel to this world's own 1519–1525 treatises' arguments…" — so R55 points at §12.1 as the gap it answers, and §12.1 points back at R55 to say she does not answer it. §15 item 4's own conclusion is "**Native for the two 1524 pieces specifically**." Both §11 and §12.1 also mis-describe "her own corpus" as a whole, which §15 has just finished splitting.

Two aggravating facts, both the same category flagged previously:

1. **§17's fix log certifies the fix.** "**N2** — §11 now excludes Zell from 'Lost voices' with a cross-reference to §15; §12.1's closing sentence names Grumbach as the actual answer to the gap and **states Zell's exclusion** rather than offering her as part of the answer." The edit was made; what it states is now false.
2. **This lands in the Affirmative Duty section**, which Framework para 184 makes participant-facing, and it is precisely the case the protocol's own "Cross-document fact consistency" rule exists for.

**Fix:** §11 should list Zell's 1524 pieces alongside Grumbach as published-but-not-here, with the 1530s–1550s material cross-referenced to R95; §12.1's closing sentence should name Grumbach **and** Zell's two 1524 pieces as the named unvendored answers (each unread, each conditioned on acquisition), and name R95 as the part determined out. §17's N2 entry should be rewritten to describe what the section now says, not what Revision 1 made it say.

### New-2 — SUBSTANTIAL. The restated test's Native branch requires naming; the Zell application does not supply it, and the document says it does

§15 item 4 now states the rule in bold: "**Native if the writing's own evidence shows it drawing on, defending, or addressing the Wittenberg-led movement's own cause by name** — even if the same writing could also, on other evidence, belong to another world; **Excluded only where the writing's own evidence shows its subject to be a different church or cause specifically**…"

- *Grumbach:* "defend Arsacius Seehofer, a Wittenberg-trained student condemned at Ingolstadt, and **cite Luther and Melanchthon by name**" — the Native branch is met.
- *Zell's 1524 pieces:* "defend evangelical preaching and clerical marriage during the same 1521–1525 window… and do so from inside Strasbourg's own still-undivided evangelical movement." No naming of Wittenberg, Luther, Melanchthon or this world's cause is asserted. The document then writes: "**On the test's Native branch, that is enough.**"
- *Zell's later material:* "Zell's own 1557 letter argues against the Lutheran line specifically, **by name**" — so naming is doing the discriminating work on the Excluded side too.

What is actually being applied to the 1524 pieces is the *negation of the Excluded branch* ("not a different church or cause specifically"), which converts a positive Native test into a default-Native residual. That is more permissive than the Template, whose own question is positive: "was this source actually used, inherited, or drawn on as part of this world's own formation, on this world's own evidence?" The prior pass's N3 finding asked for the naming criterion to be **stated as part of the test or dropped**; Revision 2 stated it and then decided the decisive case against it. The determination may well be right — Zell's 1524 *Apologia* plausibly does cite Luther — but the document cannot rely on that, because R55 is Confidence **B**, "content still unread," and the row asserts no naming either. An unread source is again carrying the load, as N3(a) warned previously.

Note also the practical effect: Revision 1 excluded an unread source (conservative); Revision 2 grants an unread source **Native** status with a Licensed For (permissive). The licensing is conditioned on acquisition, which bounds the risk, but the direction of the error class has flipped.

**Fix, one of three:** (i) drop "by name" from the Native branch and re-state the branch in the Template's own terms ("actually used, inherited, or drawn on… on this world's own evidence"), then show what satisfies it for the 1524 pieces; or (ii) keep "by name" and state honestly that the 1524 pieces are placed Native on a *provisional* reading pending acquisition, with R55 marked as the judgment call most in need of the second opinion; or (iii) restate the whole thing as a licensing decision rather than a boundary determination, which is what the prior pass offered as the fallback.

### New-3 — COSMETIC (must fix). R55 is a malformed table row

R55 has **10 cells where every other row has 11**. When the Comparandum Note was removed (correctly — R55 is now Native), the cell delimiter went with it, so the columns shift from position 8 onward: what sits in the **Comparandum Note** column is the census/discovery sentence ("census `voices` array names her as one of this world's five named voices… existence re-verified WebSearch / 2026-09-15"), the **Discovery** column holds a bare "2026-09-15" with no channel, and the **Added** column — required by the Template schema — is **gone**.

The Registry's summary asserts "Schema check re-run by script at Revision 2." The four checks it names do pass (they read columns 0–7, which are unaffected), but a column-count check would have caught this in the one row this revision edited most heavily. Restore the "—" for Comparandum Note and split the Discovery and Added cells.

### New-4 — COSMETIC. The unvendored-leads enumeration no longer sums to its own count

"**Unvendored primary leads with a row:** 17 (R48–R56, R59–R62, R93, R95, plus R54/R55 for Grumbach/Zell)". The listed spans give **15**, and "plus R54/R55" re-adds two rows already inside R48–R56. 17 is correct for R48–R62, R93, R95 — which is presumably what was meant, since the same bullet goes on to discuss R57 and R58 as "within this range." Either print "17 (R48–R62, R93, R95)" or fix the count.

### New-5 — COSMETIC. §16 item 8's range still sweeps in a non-seed item

"items 1–5, 7 and 9–12 here (6 and 11 are struck/closed, not seeds)" — item 11 is inside 9–12. Should read "items 1–5, 7, 9, 10 and 12."

### New-6 — COSMETIC. The R55/R95 split has a wording mismatch and a small unallocated gap

§15 concludes "**Excluded** for the **1553–1558** material"; R95's Source field and §17 both scope it "**the 1530s–1550s** material," and the hymn collection R95 lists is 1530s, not 1553–58. Use one span. Separately, R55's own note records the McKee corpus as "1524–1558": R55 covers "two 1524 pieces only" and R95 covers the 1530s–1550s, leaving **1525–1529 unallocated** by either row. If nothing exists in that window, say so in R95; if something does, it is undetermined.

Also, §15's closing G1 Part B sentence still reads "Grumbach [R54] and Zell [R55] — each now has a Registry row stating what it is licensed for (**disclosure only, in every case**)" — it does not mention R95, whose Licensed For is blank because it is Excluded.

### New-7 — COSMETIC. R89–R91's flags were softened only in the summary, not in the rows

Each of R89, R90 and R91 still carries "**Flagged for second-opinion review** (Doc_02 §16 item 11)" unchanged, cross-referencing an item that now reads "**Closed.**" The softening text ("chronology independently confirmed; the three named sources' own interpretive framing remains unread") lives only in the Registry's summary-statistics bullet, and §17 claims "R89–R91's flags are softened." A reader of the row gets neither the softening nor a live cross-reference.

### New-8 — COSMETIC. "Disagreement log: none" is not accurate

Revision 2 did **not** adopt the prior pass's stated Cole range. That earlier finding said "the passage runs 218–225 (line 230 is blank)"; Revision 2 uses 218–230, and it is **right** — line 230 reads "seintiments in substance only." That is a real, well-grounded disagreement with a review finding, and it is exactly the behaviour §17 elsewhere praises Revision 1 for on the LC "ma-servants" item. Logging it as "none — every prior finding is accepted and fixed as described" understates the document's own good work and, more to the point, leaves a claim about its own verification discipline slightly untrue. Record it in the disagreement log.

### New-9 — COSMETIC. Stated word count is off by three

§17 gives "17,912 (Doc_02), 13,320 (Registry), by `wc -w` after the last edit." `wc -w` now returns **17,915** and 13,320. The Registry figure is exact; the Doc_02 figure is stale by three words.

---

## What held up

- **N1 is the model of how this should be done.** Every one of the three restored citations is right, I printed all three, and R20 now records the Revision 1 error rather than certifying it. §17's rewritten earlier-revision log is candid to the point of discomfort ("recorded here rather than left to read as though it had been caught at this pass, since it was not"). That is the standard.
- **The Registry's arithmetic and schema are exact**, recomputed independently; see the block above. Nothing in the tallies is off by anything.
- **The Template is now engaged honestly on the half that permits.** The overlap paragraph is quoted accurately against Template line 52, and the elision covers a clause that would have strengthened the document's own case — so the citation is not selective in the way earlier findings S7 and N3(b) found.
- **The census is quoted accurately and completely.** I parsed `world-census.json`: the sources-block "wider evangelical orbit, placement note", the fifth `voices` entry, and the `statusDescription`'s "women's voices in verified modern editions (Argula von Grumbach, Katharina Zell)" are all reproduced correctly, and Zell appears in no other movement entry.
- **Doc_01's delegation is real and verbatim**, at Doc_01 line 67, with open item 4 explicitly "not resolved here." The escalation reasoning built on it is well-grounded, and I would not escalate this under CO-022 category 2 on the delegation question itself.
- **N7's scope correction is right on the merits**, verified row by row.
- **N8 (iii) is a genuine improvement in honesty** — the R87 footnote now matches the file character for character, and the row says which emendation Revision 1 had hidden.
- **R59/R60 at B is the correct tier** on the Template's own definition, and the stated reason is the right one.

---

## Recommended disposition

**Not ready to self-dispose as "Approved to proceed" under CO-022.**

CO-022 permits self-disposal only where "no escalation trigger applies **and** the review cleared with nothing substantial outstanding." Two things are substantial outstanding:

1. **New-1** — a live contradiction between §11/§12.1 and §15/R55 about a boundary determination, which the protocol's step 3 classes as substantial on its face ("a sourcing conclusion… anything a reader of the document would notice as different"), logged in §17 as fixed. A blocking finding cannot be closed by self-certification.
2. **New-2** — the decisive argument for the Zell split does not satisfy the test the same paragraph states.

Neither needs a full further pass. Both are in-place repairs, and the rest of the two documents has now been checked three times by three independent reviewers and holds.

**Scope the fix to exactly this:**

1. **New-1** — rewrite §11's Zell bullet and §12.1's closing sentence to the split determination, and correct §17's N2 entry to describe what the sections now say.
2. **New-2** — reconcile the stated Native branch with the Zell application: drop "by name," or evidence it, or restate the 1524 placement as provisional-pending-acquisition. Whichever is chosen, R55's flag status should reflect it.
3. **New-3** — repair the R55 row's column count and restore its Added date.
4. **New-4 to New-9** — one cosmetic pass.
5. Add a **column-count check** to whatever script runs the Registry's schema audit, so a malformed row cannot pass a "schema check re-run by script" claim again.

**Then a second bounded spot-check of the Zell thread only** — §11, §12.1, §15 item 4, R55, R95 and §17's N2/N3 entries, read together in one pass to confirm they say the same thing — plus a re-run of the Registry column-count and tallies. Nothing else needs re-opening.

**One standing note.** An earlier pass's lesson was "never change a line citation without printing the line." This pass's lesson is its sibling: **never change a determination without re-reading every section that states it.** The Zell item has now been revised three times, and all three times the revision left one part of the pair of documents speaking for a determination the other part had abandoned — Revision 1 left §11/§12.1 behind the exclusion, Revision 2 left them behind the split. The mechanical rule that would catch it: after any Boundary-Status change, grep both documents for the source's name and read every hit.
