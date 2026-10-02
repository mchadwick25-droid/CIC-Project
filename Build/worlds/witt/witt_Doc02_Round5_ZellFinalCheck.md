# Doc_02 / Source Registry — Round 5 Bounded Check: the Katharina Schütz Zell item only

**Documents checked:** `witt_Doc_02_Source_Ecology.md` (DRAFT, Revision 4, 366 lines) and `witt_Source_Registry.md` (DRAFT, Revision 4, 129 lines, 95 rows).

**Scope:** Round 4's ten required fixes, verified one by one against the live text; plus an independent recomputation of every Registry statistic, a re-read of Doc_01's delegation passage and the live census entry, a full sweep of every "Zell" occurrence in both documents, and a hunt for defects introduced at Revision 4. Nothing outside the Zell thread was re-reviewed.

**Method:** every Registry figure below was recomputed by script from the live pipe-delimited table — row count, numbering, column counts (by literal pipe count and by field split), Boundary tallies, Confidence tallies by leading tier with full membership ranges, Type tallies, the `(context)` markers, the four field-presence schema checks, and Named-Comparandum note presence. No number was read off the document. `cic-website/data/world-census.json` was parsed and every leaf value containing "Zell" enumerated. Doc_01's delegation sentence was string-matched character-for-character against both Doc_02 occurrences.

---

## VERDICT: MINOR ISSUES REMAIN

**Revision 4 is the first revision in this thread that did what it said it did.** All ten required fixes were attempted and eight are fully and correctly made. The mechanical defects are genuinely gone and I verified them by my own count, not the document's: **all 95 rows have exactly 11 content columns**, R95 is repaired and at Confidence B, the live tally is **A 50 / B 44 / C 0 / D 0 / E 0** with R95 stated separately, the Conventions paragraph's "no row is at E" is now *true*, the append-point reads row 95, R55's cross-reference points at §12.1, and the false attribution to Round 3 is deleted without residue. The core framing fix is real: §15 item 4 and R55 now state the determination as a conservative default on an evidentiary gap, and R55's reopening rule no longer demands of Zell a standard R54 does not meet.

**But the cycle is not broken, and it broke in the same place it has broken every time.** Two sections that state the *ground* of the determination — §11 and §12.1 — were not re-read when §15 item 4 changed its ground, and they now assert the exact positive finding §15 item 4 explicitly disclaims making. §11 and §12.1 are named by number in this document's own §17 log as the sections Round 3 caught drifting. They drifted again, for the same reason, one revision later.

And the fix for Round 4's sharpest finding — the Grumbach/Zell asymmetry — rests on an evidentiary claim about R54 that Revision 4 upgraded without disclosing the upgrade, and that Doc_02 §12.1 and R54's own Discovery cell contradict.

Neither remaining defect changes the disposition. Both are small edits. Neither is something a sixth automated round is well suited to settle — see the final recommendation.

---

## 1. Fix-verification table — Round 4's ten required fixes

| # | Required fix | Status | Evidence |
|---|---|---|---|
| 1 | State the determination as a conservative default on absent evidence, not a demonstrated/evenly-applied finding (§15 item 4, R55) | **FIXED** | §15 item 4 heading now reads "stated honestly at this revision as a conservative default on absent evidence, not a demonstrated finding," and closes with an explicit list of what it does *not* claim: not "evenly applied" in the sense of parity of evidence, not that the 1524 pieces' evidence "has been shown to exclude Wittenberg 'at every date'," and not that the reframing came from any prior review. R55: "Excluded on that basis, as a conservative default… not a demonstrated finding that the writings' own evidence excludes Wittenberg." The Revision 3 phrases "a genuine, non-arbitrary, evenly-applied distinction," "stated once, in full, and applied the same way throughout," and "at every date" as a positive finding are all gone (grep: zero hits in either document). **Undercut by New Finding A below, in §11 and §12.1.** |
| 2 | Disclose that *this revision* changed the Excluded branch; stop attributing it to Round 3 | **FIXED** | The sentence "Round 3's spot-check correctly caught [it] as the test's own Excluded branch being met" is deleted — zero hits in either document. Replaced with: "it does not attribute this revision's own change in how the Excluded branch is framed to any prior review — that framing is this revision's own choice, made because the alternative… had already produced two rounds of self-contradiction." R55 carries a matching revision history naming Revision 3's misattribution explicitly ("rewrote the Excluded branch into an undisclosed default and misattributed the change to Round 3"). Honest and correctly attributed. |
| 3 | State the Grumbach/Zell asymmetry honestly (same standard, different reported facts), and remove the operative rule R54 does not satisfy | **PARTIAL** | The operative-rule defect is **fixed**: R55's reopening instruction now reads "should look for a reported or read naming claim comparable to R54's — **the same standard, not a stricter one** — and should re-examine R54 in the same pass, since its own naming claim is equally unread." The phrase "from a source actually read" is gone (zero hits). §15 item 4 states the difference as "not a difference in the standard applied — it is a difference in what has been reported about each, at the same evidentiary depth." **What is not fixed:** that claim depends on Grumbach's naming claim actually having been *reported to this document*, and Revision 4 changed where R54 says that report came from without saying so (New Finding C). It also does not say, as Round 4's recommendation 3(a) asked, that the two inquiries used different instruments — publisher and H-Net *listings* for Zell, scholarly *reviews* for Grumbach — and that no review-level inquiry was run for the 1524 pieces. |
| 4 | Rewrite R54 to state the identical test R55 states; re-derive Grumbach's Native conclusion under it | **FIXED (test), and the re-derivation holds** | R54's test, restated: "an affirmative indication that the writing draws on, defends, or addresses the Wittenberg movement specifically is required, and a *reported* indication (from secondary description, even where this document has not read the primary text itself) is sufficient." R55's test: "an affirmative indication — reported or read — that the writing draws on, defends, or addresses the Wittenberg movement specifically." These are the same test. The superseded "different confessional line" branch is gone from R54. **I re-derived Grumbach independently under the stated test:** the test requires an affirmative indication, reported or read, of Wittenberg-specific engagement; R54 offers a reported naming of Luther and Melanchthon and a defence of a Wittenberg-trained student; that satisfies the sufficiency clause; → **Native**. It holds on the document's own terms. Zell fails the same test not by meeting an Excluded branch but by producing no affirmative indication, which the document now correctly calls a default rather than a finding. The branches no longer partition the space by negation — Excluded is explicitly the residual, and it says so. |
| 5 | R95 to exactly 11 content columns | **FIXED — verified by my own count** | I counted literal pipe characters and split-field counts on all 95 data rows. Every row: **12 pipes, 13 split fields, 11 content columns.** Distribution is uniform — `{11: 95}`. R95's cells now read: Discovery = "superseded by R55, created Revision 2 (Round 2 N3)", Added = "2026-09-15". The disposition text is in the Source cell where Round 4 asked for it. No row anywhere in the table is malformed. *(Nit, not a defect: the Registry describes this as "13 pipe-delimited fields including the table's own leading/trailing bars." That is an accurate description of a split, but two of those 13 "fields" are empty strings, and a reader counting bars will find 12. Worth one clearer word if the sentence is ever touched.)* |
| 6 | R95 at Confidence B, excluded from the live tally with a disclosed note, no contradiction with the Conventions paragraph | **FIXED** | R95's Confidence cell = `B` (verified by parse). The summary states "**R95 (superseded, not live) is separately B**, not counted in this tally," with an explicit disclosure of the Revision 3 error. The Conventions paragraph still reads "no row is at E" — **and that is now true**: my recount of all 95 rows finds **zero** rows at any E tier. The contradiction is gone because the fact changed, which is the right way to fix it. R95's own note discloses the departure honestly: the Template's E/removed-from-use provision "addresses a source later found unreliable, which this is not… used here only by disclosed analogy." That is disclosed departure rather than borrowed authority — exactly what Round 4 asked for. |
| 7 | Three stale/false lines: G1 Part B, the append-point, R55's cross-reference | **FIXED (all three)** | (a) §15 G1 Part B now removes Zell from the licensed list and adds: "**Zell [R55] is the exception, corrected at Revision 4 (Round 4 Finding 1.1):** R55 is Excluded, and an Excluded row licenses nothing by the schema." (b) Living-document protocol: "appended **after row 95**" — the string "after row 94" has zero hits. (c) R55 now reads "contemporaneous with and doctrinally sympathetic to this world's own arguments (**Doc_02 §12.1**)"; "(§1.3, §6)" has zero hits anywhere in the Registry. §12.1 is "Women," which is where the clerical-marriage material actually sits. |
| 8 | Column-count check in the schema-audit description; and a tally-vs-Conventions consistency check | **PARTIAL** | The column-count check is **added and named**: "every row has exactly 11 content columns," listed as a fifth check alongside the four pre-existing ones, and flagged as "the first pass to actually count columns rather than run only the four field-presence checks." I re-ran all five checks myself: **zero violations** on every one. **Not added:** the second check Round 4 asked for — an assertion that the summary's Confidence tally agrees with the Conventions paragraph's own claims about which tiers are occupied. The two agree *in fact* today (E 0 vs. "no row is at E"), so nothing is currently wrong; but the guard against them drifting apart again — which is what Round 4 was asking for, having just watched them drift — was not installed. This is the second time a requested *guard* was skipped while the *symptom* it was meant to catch was fixed. |
| 9 | Census reconciliation as a tracked open item in §16, inside item 8's seed range | **FIXED (one quotation nit)** | §16 **item 13** is new and substantive: it names the divergence, names the two live census fields, notes that no Era VI entry covers Strasbourg to receive her, and asks the coach thread either to correct the census or to record a standing disclosed divergence. Item 8's seed range now reads "items 1–5, 7, 9–10, 12 and 13" — I enumerated §16's items: 6 is struck, 11 is closed, and the live set is exactly {1,2,3,4,5,7,9,10,12,13}. **The range is correct.** *Nit:* item 13 puts quotation marks around "verified modern edition"; the census says "verified modern edition**s**". A quoted fragment that isn't verbatim, in a new sentence, in a document whose own standing rule is to print what it quotes. |
| 10 | R55's cross-reference to §12.1 | **FIXED** | Verified — see item 7(c). |

**Score: 8 fixed, 2 partial, 0 missed.**

---

## 2. Independent statistics recomputation — every published figure is exact

Computed by script from the live table; no figure taken from the document.

| Figure | Document claims | I compute | |
|---|---|---|---|
| Rows | 95 total, 94 live | 95 data rows, numbered 1–95, sequential, no gaps, no duplicates | ✓ |
| Column count | every row exactly 11 content columns | `{11: 95}` — uniform; 12 pipes / 13 split fields per row | ✓ |
| Boundary | 89 Native / 6 Excluded | 89 / 6 | ✓ |
| Excluded membership | R33 (Out-of-Boundary); R55, R57, R58, R94, R95 (Named Comparandum) | exactly those six, exactly those reasons | ✓ |
| Named Comparanda with notes | all five | R55, R57, R58, R94, R95 — all five carry non-empty Comparandum Notes | ✓ |
| Confidence, 94 live | A 50 / B 44 / C 0 / D 0 / E 0 | A 50 / B 44 / C 0 / D 0 / E 0 | ✓ |
| A membership | R1–R2, R7–R9, R14–R47, R63–R69, R85–R88 | identical | ✓ |
| B membership (live) | R3–R6, R10–R13, R48–R58, R59–R62, R70–R84, R89–R94 | R3–R6, R10–R13, R48–R62, R70–R84, R89–R94 | ✓ (same set; the "R48–R58, R59–R62" split is the harmless edit artefact Round 4 also noted) |
| R95 tier | separately B | B | ✓ |
| Rows at E | none | none | ✓ |
| Type | P 65; S 25; S/P 1; M 1; M/S 1; M/P 1; L/S 1 | identical, sums to 95 | ✓ |
| Type membership | P = R1–R62, R93–R95; S = R63–R79, R81–R83, R88–R92 | identical | ✓ |
| `(context)` rows | 6 — R36, R39–R43 | exactly those six, all Native | ✓ |
| Schema checks (all five) | zero violations | zero violations on all five, including the new column count | ✓ |
| Unvendored primary leads | 14 — R48–R56, R59–R62, R93 | 9 + 4 + 1 = 14 | ✓ |
| Doc_02 §17's restatement | 95 rows / 94 live / 89 Native / 6 Excluded / A 50 B 44 C 0 D 0 E 0 / R95 separately B | agrees with the Registry and with my recount | ✓ |

**Every published statistic in both documents is exact.** This is the second round running that is true, and it now includes the figure that was wrong last round.

## 3. Doc_01's delegation and the live census — re-verified, no drift

- **Doc_01 line 67, verbatim:** *"Doc_02 should settle whether Zell belongs to this world's own congregational record or is better treated as an adjacent-world witness, rather than this document assuming the placement."* String-matched: **1 occurrence in Doc_01, 2 in Doc_02** (§15 item 4 and §17's Revision-3 escalation check), character-for-character identical in all three. No drift.
- **Doc_01 line 192, open item 4:** still "not resolved here." Correct — the question is Doc_02's to settle, and Doc_02 settles it in Doc_01's own binary.
- **Census (`cic-website/data/world-census.json`), parsed:** exactly **three** leaf values contain "Zell," all inside `movements[133]`, `atlasId` **VI.1**. The `voices` array has exactly **five** entries, Zell at index 4 — so "one of this world's five named voices" is exact. `statusDescription` contains "women's voices in verified modern editions (Argula von Grumbach, Katharina Zell)" — R55's and §15 item 4's quotations of this fragment are verbatim; §16 item 13's is not (see 4.D). No other census movement mentions her. The claim that no other census world currently claims her holds.

---

## 4. New findings — defects introduced or newly exposed at Revision 4

### A — SUBSTANTIAL. §11 asserts the positive finding §15 item 4 explicitly disclaims

**Doc_02 §11, line 237:** *"**Not Zell:** §15 item 4 and Registry R55 determine her Excluded / Named Comparandum — **her own corpus speaks for Strasbourg's church, not this world's** — so she is not counted among this world's own lost voices."*

**Doc_02 §15 item 4, as rewritten at Revision 4:** *"**What this revision does not claim…** it does not claim the 1524 pieces' own evidence has been shown to exclude Wittenberg 'at every date'."*

These cannot both stand. §15 item 4's whole Revision-4 correction is that the document has **no evidence either way** about what the 1524 pieces speak for — an absence of reported evidence, not a reported absence. §11 states, flatly and without qualification, that her corpus speaks for Strasbourg's church. That is the claim Revision 4 was convened to withdraw, still live one section over.

This is the identical mechanical failure, a fifth time — and this document's own §17 log names §11 and §12.1 by number as the two sections Round 3 caught in exactly this state. Revision 3's log even records the reasoning that let them survive: *"§11 and §12.1 required no further change, since they already stated Excluded."* Revision 4 checked the same thing — the *status word* — and again did not check the *ground*.

**Fix:** delete the em-dash clause, or replace it with "on the ground argued there (documented from 1530; a disclosed conservative default for 1524)."

### B — §12.1 carries a softer version of the same overreach

**Line 261:** *"…determine her Excluded / Named Comparandum: **her own corpus, on the argument made there, speaks for Strasbourg's own church rather than for this world.**"*

Hedged by "on the argument made there," which makes it a report rather than an assertion — but the argument made there does not say this about the 1524 pieces. Same correction, one clause.

### C — SUBSTANTIAL. R54's evidentiary provenance was upgraded without disclosure, and three other places contradict it

This is load-bearing: Revision 4 resolves Round 4's asymmetry finding by saying the two rows apply one standard and differ only in *what has been reported*. That resolution requires Grumbach's naming claim to have actually been reported to this document.

**R54 as it now reads:** *"**Reviews located this session report** that Grumbach's 1523 pamphlets defend Arsacius Seehofer, a Wittenberg-trained student condemned at Ingolstadt, and name Luther and Melanchthon — a specific, reported naming claim."*

Three things in the live documents say otherwise:

1. **Doc_02 §12.1, line 261** — the same claim, same row: *"Native, since her 1523 pamphlets defended a Wittenberg-trained student and the evangelical cause by name… (existence and edition verified; content unread; **[Widely Accepted] from prior knowledge**)."* Prior knowledge, not a located review.
2. **R54's own Discovery cell** — the field whose entire purpose is to record the channel and instrument: *"census ('verified this session,' prior pass); **existence re-verified WebSearch** / 2026-09-15."* It records an existence check. It records no content-level search.
3. **Doc_02 §15 item 4** — scopes the session's verification narrowly and then leaves the report unsourced: *"secondary description (**existence and edition verified this session**; content itself unread, Confidence B) reports that…"*

Round 4 quoted Revision 3's R54 as stating the content basis as *"prior knowledge (Widely Accepted), existence-verified, unread"*; that phrase no longer appears anywhere in the Registry. So the basis was re-labelled from prior knowledge to located reviews, at the exact point the argument needs it, in the same revision, with no entry in §17's fix log recording a new search and no update to the Discovery cell.

**Why it matters, not just as bookkeeping.** If Grumbach's naming claim really is builder's prior knowledge, then the two rows are *not* "the same standard, different reported facts." They are: prior knowledge admitted as evidence for one woman, and a title-level listings search treated as exhausting the evidence for the other. That is the Grumbach/Zell asymmetry Round 4 named — surviving under a new description rather than fixed. If a review really was located and read this session, the fix is trivial: name it, and put it in the Discovery cell.

**This is a question of fact only the builder can answer.** No further review round can settle it from the documents.

### D — MINOR. §16 item 13 misquotes the census

Item 13: *credits this world with her "verified modern edition."* The census says "verified modern edition**s**." A quoted fragment that isn't verbatim, in a sentence written this revision. Trivial to fix; noted because this thread's own standing rule is that a quotation is re-checked against the source before it is written down, and because R55 and §15 item 4 both quote the same fragment correctly.

### E — COSMETIC. One stale revision reference in the Registry summary

Registry line 124: *"R55 within this range is Excluded (Zell's whole corpus, **as of Revision 3**)."* Not false — the whole-corpus determination does date from Revision 3 — but the ground was restated at Revision 4, and this is one more place that was not re-read when the surrounding text was. Also, the Registry status line says R54 and R55 are "both honestly flagged as resting on unread, **reported-only evidence**"; R55 rests on the *absence* of reported evidence, which is the distinction Revision 4 otherwise draws carefully.

### What I checked for and did *not* find

No new citation defect: the Doc_01 delegation quote, the two census fragments in R55 and §15 item 4, the Template's overlap-permissive quotation in §15 item 4, and the Template's living-document quotation are all verbatim against their sources. No new cross-reference defect beyond those listed: §12.1 resolves correctly, §16 item 13 exists and is in item 8's range, R95's pointer to R55 is correct. No statistic is wrong. No row is malformed. The Round-3 log entry's historical "E 1 (R95)" is correct *as history* and correctly scoped to Revision 3. The four escalation categories are correctly judged: this remains Doc_02's delegated question, not a portfolio decision, and I would not escalate it under CO-022 category 2.

---

## 5. Recommendation — and what this item actually needs now

**The disposition is right and nothing downstream is at risk.** Excluded / Named Comparandum licenses nothing, bars Zell from the congregational and women's registers, tells a later step how to reopen the question, and answers Doc_01's binary in Doc_01's own terms. That has been true since Revision 3 and is not in question.

**The remaining edits are four lines and one factual answer:**

1. §11 line 237 — delete or qualify "her own corpus speaks for Strasbourg's church, not this world's."
2. §12.1 line 261 — same, softer.
3. §16 item 13 — "verified modern editions," verbatim.
4. Registry line 124 — "as of Revision 4," and the status line's "reported-only evidence" for R55.
5. **R54's provenance — a question, not an edit.** Was a review actually located and read this session reporting that Grumbach's pamphlets name Luther and Melanchthon? If yes: name it in R54, put it in the Discovery cell, and bring Doc_02 §12.1 into line. If no: R54 must say the naming claim is prior knowledge, and §15 item 4 must stop claiming the two rows differ only in what has been reported — because then they differ in what was *asked*, which is the asymmetry itself.

### Does this need another automated round? No.

Five rounds have now each found something, and the shape of what they find has changed in a way that matters. Rounds 1–3 found the determination wrong. Round 4 found the fix wrong. Round 5 finds the fix substantially right, with two dependent sentences left behind and one question of fact the documents cannot answer about themselves.

A sixth review round would find the same class of thing again, because the failure is not a reasoning failure a reviewer can catch better — it is that each revision edits the section a finding names and does not re-read the sections that depend on it. Two mechanisms would end that, and neither is a review:

- **A mechanical guard, not a prose instruction.** Three rounds running have now asked for a check and gotten the symptom fixed instead: Round 3 asked for a column-count check and got R55 repaired; Round 4 asked for a tally/Conventions consistency check and got the tally corrected. The column-count check finally landed at Revision 4. The consistency check did not. The Zell-thread equivalent — a script that greps both documents for the source's name and prints every hit for reading, which §17 already describes as the method — should be a required step of any revision that touches a Boundary Status or its ground, and its output should be recorded, not asserted.
- **A human decision on R54.** Finding C is a factual question about what this build thread actually did. Only the builder knows. Until it is answered, §15 item 4's central claim — that one standard is applied to both women — cannot be verified by anyone, including a sixth reviewer.

**Recommendation: apply edits 1–4 as mechanical corrections, answer question 5 directly, and then close the Zell item by decision rather than by another round.** The item is close to stable; it is not going to be *made* stable by a sixth independent read of the same text. What it needs is the one fact only the builder holds, and a check that runs instead of a lesson that is written down.

**The standing note, extended one last time.** Round 2: never change a line citation without printing the line. Round 3: never change a determination without re-reading every section that states it. Round 4: never change a test, a tier, or a row's shape without re-reading everything that depends on it. **Round 5: re-reading a section to confirm its *status word* is not re-reading it. §11 and §12.1 have now said the right word and the wrong reason across three consecutive revisions, and each revision checked the word.** And: when a revision changes where a claim's evidence came from, that is a change, and it goes in the fix log like any other.
