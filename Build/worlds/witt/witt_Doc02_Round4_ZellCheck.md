# Doc_02 / Source Registry — Round 4 Bounded Check: the Katharina Schütz Zell item only

**Documents checked:** `witt_Doc_02_Source_Ecology.md` (DRAFT, Revision 3, 361 lines) and `witt_Source_Registry.md` (DRAFT, Revision 3, 95 rows).

**Scope:** the Zell thread and nothing else — every occurrence of "Zell" in both documents, rows R54, R55 and R95, the Registry's summary-statistics block, Doc_01's delegation passage, the census entry, and the Source Registry Template's Boundary Check. The substantive historical and methodological content Rounds 1–3 found sound was not re-reviewed.

**Checked directly against:** `Build/reference/L3B-World-Build-Methodology/Source_Registry_Template.md` (read in full; Boundary Check lines 48–61, overlap-permissive paragraph line 52, builder process line 84, living-document protocol line 96); `witt_Doc_01_World_Identification_Boundaries_Orientation.md` lines 19, 67, 180, 192; `cic-website/data/world-census.json` (parsed with `json`, every leaf value containing "Zell" enumerated, every `VI.*` movement listed); `witt_Doc02_SpotCheck_Round3.md` in full. Every Registry statistic below was recomputed by script from the live table, parsing the pipe-delimited rows — no figure was read off the document.

---

## VERDICT: STILL NOT RESOLVED

**Narrower than Round 3, and genuinely better — but the pattern is not broken. It moved again.**

What is now fixed, and should be said first: **every explicit statement of Zell's Boundary Status in either document agrees.** §11, §12.1, §15 item 4, §17, R55, R95 and the Registry's Boundary tally all say Excluded / Named Comparandum for the whole corpus. That is the first round in four where that is true, and the fix note in §17 describing how it was done (grep both documents, read every hit) is the right method, honestly applied. **Every Registry statistic recomputes exactly** — 95 rows, 89 Native / 6 Excluded, A 50 / B 44 / C 0 / D 0 / E 1, the Type tallies, the six "(context)" rows, and the corrected unvendored-leads count of 14. R55 is now a well-formed 11-column row. R55's Comparandum Note is the best-written thing in the item.

But four things fail, and the first is the same failure a fourth time:

1. **The determination is still asserted rather than demonstrated — and this time the document got there by changing the test.** Between Revision 2 and Revision 3 the Excluded branch was rewritten from a positive, restrictive test ("Excluded **only where** the writing's own evidence shows its subject to be a different church or cause **specifically**") into a default residual ("Excluded if… speaks for a different, local cause **the writing itself does not tie to Wittenberg**"). Round 3 found Revision 2 had made the *Native* branch a default residual; Revision 3 fixed that by making the *Excluded* branch one. The change is not disclosed as a change — it is attributed to Round 3 as a finding Round 3 did not make. See Finding 2.1.

2. **The evidentiary standard is still not evenly applied between Grumbach and Zell**, and at this revision the asymmetry has been written into the Registry as an operative rule. R55 instructs a later step that reopening any part of Zell's corpus as Native requires evidence "**from a source actually read**." R54 — Native — rests on content that is "prior knowledge (Widely Accepted), existence-verified, **unread**." The rule the Registry now states would fail R54 itself. See Finding 2.2.

3. **R54 — the comparison row the whole determination is argued against — still carries the superseded Revision 1 test, labelled "the one test applied to R54 and R55 alike."** That test's Excluded branch turns on belonging "to a different confessional line," which §15 item 4 expressly disclaims and which would not exclude the 1524 pieces; its Native branch has no naming requirement at all. Two rows, two incompatible "one tests." See Finding 1.3.

4. **A new malformed row, in exactly the class Round 3 flagged, and the guard Round 3 asked for was not added.** Round 3 New-3 found R55 with 10 cells where the schema has 11; Revision 3 fixed R55 and left **R95 with 12**. Round 3's recommendation 5 was to add a column-count check to the Registry's schema script; the Registry still claims "Schema check re-run by script at Revision 3" and still names the same four checks, none of which is a column count. Separately, Revision 3's own edit made the Registry's Conventions paragraph false: it still reads "**no row is at E**" while the summary statistics three sections later read "**E 1** (R95)". See Findings 3.1–3.3.

Doc_01's delegation is real, quoted verbatim, and correctly characterised; the census claims are accurate and independently verified. Point 4 passes cleanly.

---

## 1. Internal consistency — every location that states or implies a Boundary Status

**Explicit Boundary Status statements — all thirteen agree. This is fixed.**

| # | Location | What it says | Agrees? |
|---|---|---|---|
| 1 | Doc_02 §11, line 237 ("Lost voices") | "**Not Zell:** §15 item 4 and Registry R55 determine her Excluded / Named Comparandum" | ✓ |
| 2 | Doc_02 §12.1, line 261 (Affirmative Duty, closing) | "**Katharina Schütz Zell does not** — §15 item 4 and Registry R55… determine her Excluded / Named Comparandum" | ✓ |
| 3 | Doc_02 §15 item 4, line 315 | "the whole corpus, 1524 through 1558, is Excluded on one ground"; "**R55 Excluded / Named Comparandum, for her whole corpus**" | ✓ |
| 4 | Doc_02 §17, lines 357–358 | reversion from the split to whole-corpus Excluded, R95 removed-from-use | ✓ |
| 5 | Doc_02 §17, line 360 (escalation check) | "the Zell determination (§15 item 4; R55)" as Doc_01's delegated question | ✓ |
| 6 | Doc_02 status line, line 5 | names the Zell thread as the recommended next check; no status claim | ✓ (neutral) |
| 7 | Registry R55, line 71 | Boundary **Excluded**, Exclusion Reason **Named Comparandum**, Licensed For "—", Comparandum Note present | ✓ |
| 8 | Registry R95, line 111 | Boundary **Excluded**, Named Comparandum, removed-from-use | ✓ |
| 9 | Registry summary, line 120 | "**6 Excluded** — R33…; R55, R57, R58, R94, R95" | ✓ |
| 10 | Registry summary, line 124 | "R55 within this range is Excluded (Zell's whole corpus, as of Revision 3)" | ✓ |
| 11 | Registry status line, line 5 | reversion described accurately | ✓ |
| 12 | Registry R58 | "WebSearch (incidental to R55)" — no status claim | ✓ (neutral) |
| 13 | Doc_01 line 192, open item 4 | "not resolved here" — correctly left to Doc_02 | ✓ |

**But the agreement is only at the level of the words "Native" and "Excluded." Five further locations state or imply something that no longer holds — two of them implying the superseded Native/licensed state, one carrying a superseded version of the test itself, and one made false by this very revision.**

**1.1 — Doc_02 §15, G1 Part B (line 323).** "the Peasants' War tract [R48]… **Grumbach [R54] and Zell [R55] — each now has a Registry row stating what it is licensed for (disclosure only, in every case)** and why it is not in hand."

R55's Licensed For field is "—". Under the Template's schema, Licensed For is "*required if Native, blank if Excluded*"; an Excluded row licenses nothing, which is the whole point of Excluded ("A source that fails the Boundary Check does not stop being worth recording — it stops being worth *licensing*", Template line 61). This sentence asserts that R55 states what Zell is licensed for. It does not and must not. Round 3's New-6 flagged this same sentence for a different reason (it omitted R95); Revision 3 did not touch it, and under the reverted determination it is no longer merely incomplete — it is wrong about R55. It is also the one place in Doc_02 a reader could come away believing Zell is licensed for disclosure use.

**1.2 — Registry Conventions paragraph (line 9).** "(**the second sentence restored at Revision 2, Round 2 N5** — Revision 1's Conventions paragraph dropped it while claiming a verbatim quotation; **no row is at E, so the tallies are unaffected**…)"

R95 is at E as of this revision, and the tallies say so. This is not stale text inherited from an earlier pass — **Revision 3 created the E row and did not re-read the paragraph that says no E row exists.** That is the identical mechanical failure this item has now produced four times, in a fourth location.

**1.3 — SUBSTANTIAL. R54 still states a superseded test, and calls it "the one test applied to R54 and R55 alike."**

R54's Verification Note, unchanged at this revision: *"**Boundary test (the one test applied to R54 and R55 alike, Round 1 S7):** Native if the writing's own subject is the Wittenberg-led movement — its cause, people, texts, churches — on the writing's own evidence; **Excluded if its subject is a church or cause that belonged, on that evidence, to a different confessional line.**"*

That is Revision 1's formulation. It is not the test §15 item 4 and R55 now state, and the two are not interchangeable — **they deliver opposite results on Zell's 1524 pieces.** R54's Excluded branch requires the subject to belong "to a different confessional line," and §15 item 4 concedes in its own words that the 1524 material was "contemporaneous with and doctrinally sympathetic to Wittenberg's own arguments" and expressly disclaims the confessional-line reading ("it is not that Zell is doctrinally too independent to count"). In 1524 Strasbourg was not a different confessional line; the Tetrapolitan is 1530. So under R54's live version of "the one test," the 1524 pieces fall into neither branch — which is exactly the Round 2 N3 defect — while R54's Native branch ("the writing's own subject is the Wittenberg-led movement — its cause, people, texts, churches") contains no naming requirement at all, and the *Apologia*'s defense of clerical marriage is a Wittenberg cause on this document's own showing (§12.1, AC XXIII [R37], the Teutonic Order treatise [R24]).

**The Registry therefore contains two different documents-of-record for "the one test," in the two rows the determination is built by comparing, and only one of them produces the Revision 3 result.** This is the recurring failure in its most consequential location yet: the determination changed at §15 item 4 and R55, and the comparison row it is argued against was not re-read. R54 must be rewritten to carry the same test R55 now states, with its own Native conclusion re-derived under it — see Finding 2.2 for what that re-derivation will surface.

**1.4 — Registry living-document protocol (line 129), minor.** "Any new source surfaced by Doc_03–Doc_10 is appended **after row 94**." R95 exists; this should read row 95.

**1.5 — The live participant-facing surface is unreconciled and untracked.** `cic-website/data/world-census.json` still lists Zell as the fifth of VI.1's five `voices`, and its `statusDescription` still credits this world with "women's voices in verified modern editions (Argula von Grumbach, Katharina Zell)." Doc_02 discloses that it overrides this ("the override is stated, not implied") — which is correct practice — but **no open item in §16 and no gap entry anywhere carries the reconciliation forward.** §16 item 8's seed list for this world's future `Open_Gaps_Tracking.md` does not include it. `cic-website/` is a live participant-facing surface under this project's own rules; a build document that overrides it should leave a tracked item behind, not only a disclosure.

---

## 2. Does the argument work?

**What works — and it is not nothing.** The Template's overlap-permissive paragraph is now engaged correctly, and the distinction the caller asked about is drawn accurately. §15 item 4: *"Overlap-permissiveness answers a different question than this one, though: it says a source is not disqualified merely for also belonging elsewhere; it does not lower what counts as belonging here in the first place."* That is a fair and correct reading of Template line 52, and the Template's own primary formulation at line 50 — Boundary Status "assessed by what the source speaks *for* — its own subject, tradition, or evidentiary target" — is exactly the shape of test the document applies. The quotation of line 52 is verbatim and the elision is not self-serving. Round 1 S7's and Round 2 N3(b)'s complaint on this axis is genuinely closed.

**The later material is genuinely well-founded.** The second route — Strasbourg presenting the Tetrapolitan Confession in 1530 [R58], subscribing the AC only in 1532 under Bucer for League purposes, the Wittenberg Concord of 1536, and Zell's own 1557 letter arguing against the Lutheran line by name — independently supports Excluded for the 1553–1558 material on its own. That leg holds. Everything below concerns the 1524 pieces, which is the only part of the corpus the weak argument carries.

### 2.1 — SUBSTANTIAL. The Excluded branch was rewritten to make it satisfiable, and the rewrite is attributed to Round 3

Revision 2's test, as Round 3 quoted it: *"**Excluded only where the writing's own evidence shows its subject to be a different church or cause specifically**."* Positive and restrictive: something must be *shown*.

Revision 3's test, §15 item 4: *"**Excluded if the writing's own evidence, even where doctrinally sympathetic and contemporaneous, speaks for a different, local cause the writing itself does not tie to Wittenberg.**"*

Three changes, none disclosed: "only where" (a limiter) is dropped; "even where doctrinally sympathetic and contemporaneous" is added, which admits precisely the class Revision 2's branch kept out; and "the writing itself does not tie to Wittenberg" converts the branch into the negation of the Native branch. The two branches now partition the space exhaustively, so **a source about whose content nothing is known falls automatically to Excluded**. Round 3's finding against Revision 2 was that its Native branch had become a default residual; Revision 3 has made the Excluded branch one. That is the same error with its sign flipped — the third sign-flip on this item (Revision 1 default-Excluded, Revision 2 default-Native, Revision 3 default-Excluded again, now with a test built to produce it).

A default-Excluded rule for unread sources is defensible — arguably it is the right conservative rule for this project. The defect is that it is presented as a demonstration rather than as a default, and that the change is laid at the previous reviewer's door.

**§15 item 4 as it now reads:** *"Revision 2 asserted the 1524 pieces met the Native branch… without that evidence, which Round 3's spot-check **correctly caught as the test's own Excluded branch being met** (a local, contemporaneous, doctrinally-aligned cause) while the Native branch was asserted rather than shown."*

**What Round 3 actually wrote (New-2):** *"What is actually being applied to the 1524 pieces is the **negation of the Excluded branch** ('not a different church or cause specifically'), which converts a positive Native test into a default-Native residual."*

Round 3 said the Excluded branch was **not** met and was being negated. It did not find the Excluded branch met; on Revision 2's wording it could not have, since "a local, contemporaneous, doctrinally-aligned cause" is not "a different church or cause specifically." Round 3 went further in the other direction: *"The determination may well be right — Zell's 1524 Apologia plausibly does cite Luther — but the document cannot rely on that."* Revision 3 has converted a reviewer's "you have not shown this" into a reviewer's "the opposite is shown," and used it to license the opposite determination. **That is the pattern this round was convened to test for, in its purest form so far: the document again asserts a determination it has not demonstrated, and this time the undemonstrated thing is what the previous review found.**

Against this, §15 item 4 claims the test is *"stated once, in full, and applied the same way throughout this item"* and the result *"a genuine, non-arbitrary, evenly-applied distinction rather than a date-based or confessional-purity test."* The first claim is false as between revisions (the test changed); the second fails on 2.2 below.

### 2.2 — SUBSTANTIAL. The remaining Grumbach/Zell asymmetry, now written into the Registry as a rule

The two women are tested on the same evidentiary class — an in-copyright modern edition, existence-verified, **unread**, contents known only from third-party reporting — and given opposite standards.

| | Grumbach [R54] | Zell [R55] |
|---|---|---|
| What was actually checked | Edition verified; "per reviews located"; content basis "prior knowledge (Widely Accepted), existence-verified, unread" | Edition verified; "contents verified by search (publisher and H-Net listings)" — a **list of titles**, not a description of content |
| Depth of the inquiry | Content level: what the pamphlets *name* (Luther, Melanchthon, Seehofer) | Title level: what the pieces are *called* |
| Standard applied | Reported naming is admitted as evidence → **Native** | "This document does not have evidence, **from a source it has actually read**, that either 1524 piece names or specifically identifies the Wittenberg movement" → **Excluded** |

The document is candid that its evidence is thin ("on the evidence this document actually has"), and that candour is to its credit. But it then converts that thinness into a positive finding about the sources: *"the writings' own reported subject is Strasbourg's own local church and clergy, not the Wittenberg movement specifically, **at every date**."* A publisher's contents list and an H-Net listing report titles. They do not report whether a text names Luther, and their silence is not evidence of absence. **"We did not look" has become "not shown," and "not shown" has become a determination stated as demonstrated.**

The asymmetry is no longer merely in the reasoning — Revision 3 has made it an operative instruction. R55's Comparandum Note: *"A later step that wants any part of her corpus as Native must show, **from a source actually read**, that the specific passage names or specifically identifies the Wittenberg movement."* Apply that rule to R54 and Grumbach fails it: nobody has read her pamphlets either. The Registry now states a reopening standard that its own comparison row does not meet. That is the sharpest, most checkable form the Grumbach/Zell asymmetry has taken in four rounds, and it is checkable entirely from the documents' own words.

Note also what follows from 2.1 plus 2.2 together: under Revision 3's default-Excluded test applied to the same evidentiary class, **R54 should also fall to Excluded** — Grumbach's naming is reported, not shown from a source read. R54 stays Native. The test is therefore not "applied the same way throughout."

### 2.3 — The remaining defect is in the characterisation, not the disposition

Worth stating plainly so the next fix is not over-scoped. Excluded / Named Comparandum licenses nothing, bars her from the congregational and women's registers, and tells a later step exactly how to reopen the question. That is the conservative, downstream-safe disposition, and it answers Doc_01's delegated question within Doc_01's own terms. **Nothing downstream is currently at risk.** What is wrong is that the document claims to have demonstrated an even-handed determination when what it actually has is a conservative default on absent evidence, reached by a test it changed without saying so.

### 2.4 — COSMETIC. R55's supporting cross-reference points at the wrong sections

R55: "local Strasbourg causes, contemporaneous with and doctrinally sympathetic to Wittenberg's own arguments **(§1.3, §6)**." §1.3 is "Opponent voices that reach this library only in adversarial quotation"; §6 is "Material Evidence." Neither carries the clerical-marriage or evangelical-preaching material this sentence leans on — that is at §12.1 (AC Article XXIII at AC lines 754–756, 765–766 [R37]; *To the Knights of the Teutonic Order*, v3 20634–20635 [R24]). Point the reference at §12.1.

---

## 3. Registry mechanics

### 3.1 — SUBSTANTIAL (mechanical). R55 is fixed; R95 is now malformed, in the same way

Parsing every row's pipe-delimited cells against the header (`# | Source | Type | Confidence | Boundary | Exclusion Reason | Licensed For | Verification Note | Comparandum Note | Discovery | Added`):

- **94 of 95 rows have 11 cells. R95 (line 111) has 12.**
- **R55 is now correct** — 11 cells, Comparandum Note restored, Discovery "census; existence re-verified WebSearch / 2026-09-15", Added "2026-09-15". Round 3's New-3 is properly fixed.
- **R95's overflow:** Discovery = "—", Added = "superseded by R55, Revision 3 / 2026-09-15", and a **twelfth, unheaded cell containing "2026-09-15"**. The disposition text was written into the Added column and the original Added date pushed past the end of the row.

Round 3's recommendation 5 was: *"Add a **column-count check** to whatever script runs the Registry's schema audit, so a malformed row cannot pass a 'schema check re-run by script' claim again."* The Registry's line 120 still reads "Schema check re-run by script at Revision 3" and still names the same four checks — Native rows have Licensed For and blank Exclusion Reason; Excluded rows the reverse; all five Named Comparanda carry Comparandum Notes; the Boundary column contains only Native or Excluded. **All four of those pass (I re-ran them: zero violations).** All four read columns 0–8 and none can see a twelfth cell. The recommended guard was not added, and the defect it was meant to catch recurred at this revision in the row this revision edited most heavily. This is the fix-a-symptom-not-the-cause pattern in its mechanical form.

### 3.2 — SUBSTANTIAL. R95's "removed-from-use" does not actually match the Template's protocol

R95's Source cell: *"REMOVED-FROM-USE, Revision 3 (Round 3 spot-check New-2) — kept in the table **per the Template's own living-document protocol** ('a source later found unreliable… stays in the table as a record of what was tried')."*

The Template, line 84 and line 96: *"never renumber, never remove — **a source later found unreliable** moves to Confidence E and is marked removed-from-use, but the entry stays as a record of what was tried."* (The ellipsis in the Registry's quotation elides "moves to Confidence E and is marked removed-from-use, but the entry" — material that supports the row's own action, so the elision is not self-serving.)

The provision's trigger is a **source found unreliable**. R95 is not that, and the row says so itself, in bold: *"**Not a boundary error — the Excluded determination for this material was and remains correct; the error was the row split itself.**"* The source is fine; the *row* was a mistake. The Template has no provision for a duplicate row created by an erroneous split and later withdrawn. It has a rule that plainly covers the important half of this — append-only, never delete — and **keeping R95 in the table is unambiguously right.** What is improvised is the label:

- **Confidence E is factually wrong here and the row admits it:** *"Confidence set to E ('not a resting tier') per the Template's own protocol for a row no longer relied on, **not because the underlying chronology is unverified**."* E is defined in this same Registry, verbatim from the Template, as "**No traceable source.** Not a resting tier — remove or re-ground to at least D." R95's source is traceable, and the row is now parked permanently at a tier the definition forbids resting at.
- **It injects a phantom into the Confidence tally.** "E 1" now appears in the Registry's own summary and contradicts the Conventions paragraph's "no row is at E" (Finding 1.2). Any downstream filter reading the Confidence column will treat R95 as an untraceable source.
- **It is a claim about a provision the provision does not make** — the same species of defect as Findings 2.1 and 2.2: invoking an authority for a determination that authority does not actually deliver.

**The clean fix:** keep the row, keep Boundary Excluded / Named Comparandum, mark disposition "superseded by R55, Revision 3" in the Source cell, **leave Confidence at B** (its real tier — the underlying material is exactly as traceable as it was), exclude it from the live Confidence tally with a one-line note, and state openly that the Template's E/removed-from-use provision addresses unreliability rather than supersession, so this row is handled by analogy and the departure is disclosed. Disclosed departure is this project's own standard; borrowed authority is not.

### 3.3 — Summary statistics: recomputed independently, every figure exact

Computed by script from the live table, not read off the document:

- **95 rows**, numbered 1–95, sequential, no gaps, no duplicates ✓
- **Boundary: 89 Native / 6 Excluded** ✓ — Excluded are R33 (Out-of-Boundary) and R55, R57, R58, R94, R95 (Named Comparandum) ✓; **five Named Comparanda, all carrying Comparandum Notes** ✓
- **Confidence: A 50 / B 44 / C 0 / D 0 / E 1** ✓. Computed membership: A = R1–R2, R7–R9, R14–R47, R63–R69, R85–R88 ✓ exactly as stated; B = R48–R62 contiguous plus R3–R6, R10–R13, R70–R84, R89–R94 ✓ (the document prints the same set split as "R48–R58, R59–R62" — an edit artefact, accurate but worth merging); E = R95 ✓
- **Type: P 65** (R1–R62, R93, R94, R95) ✓; **S 25** (R63–R79, R81–R83, R88–R92) ✓; S/P 1 (R80), M 1 (R84), M/S 1 (R85), M/P 1 (R86), L/S 1 (R87) ✓ — sums to 95 ✓
- **"(context)" marker: exactly 6 rows** — R36, R39, R40, R41, R42, R43 ✓, all Native ✓
- **Unvendored primary leads: 14** — R48–R56 (9) + R59–R62 (4) + R93 (1) = 14 ✓. Round 3's New-4 arithmetic defect is genuinely fixed, and the composition statement is correct: 13 Native (R48–R54, R56, R59–R62, R93) and R55 Excluded ✓
- **Vendored primary works with a row: 35** (R1–R35) ✓
- **Schema audit, the four checks the Registry names: zero violations** ✓
- **Second-opinion flags:** exactly the ten listed (R48, R49, R50, R52, R54, R72, R82, R89, R90, R91) ✓; R86's withdrawal recorded ✓

**One nuance worth a line.** R55 carries "**Flagged as the judgment call in this document most deserving a second look — the third round running**," but it is not in the Registry's formal second-opinion flag list. That is defensible — the Template's step-4 flag is triggered by a row *licensing* a load-bearing claim, and an Excluded row licenses nothing — but it means the item the document itself calls its single most doubtful judgment does not appear in the list a reviewer would scan. Round 3's New-2 fix note asked that "R55's flag status should reflect" whatever determination was chosen. Either add R55 to the list with a one-clause note on why an Excluded row is being flagged, or say in the flag bullet that R55 is flagged separately and why.

---

## 4. The escalation question — accurate, and independently verified

**The delegation is real, verbatim, and correctly characterised.** Doc_01 line 67: *"Doc_02 should settle whether Zell belongs to this world's own congregational record or is better treated as an adjacent-world witness, rather than this document assuming the placement."* I string-matched this against both Doc_02 occurrences (§15 item 4 and §17's escalation check) — **character-for-character identical in all three places**, including apostrophes. Doc_01 line 192, open item 4: *"Katharina Schütz Zell's placement (§4) — Wittenberg-Lutheran congregational voice, or better treated as a witness from the Reformed-adjacent Strasbourg orbit; **not resolved here**."*

Doc_01 poses a binary and hands it to Doc_02. Excluded / Named Comparandum is the second branch of that binary, answered in Doc_01's own terms. **This is Doc_02's delegated question, not a new portfolio-level decision, and the document's claim to that effect is accurate.** I would not escalate it under CO-022 category 2.

**The census claim is accurate.** Parsing `world-census.json` and enumerating every leaf value containing "Zell": exactly three, all inside movement `lutheran-wittenberg-and-its-congregations` (`atlasId` VI.1) — the sources-block note ("Both verified this session. Women's voices in their own published words; Zell writes from Strasbourg - wider evangelical orbit, placement note"), `voices[4]`, and the `statusDescription`. The `voices` array has exactly **five** entries, so "one of this world's five named voices" is exact. Both quoted fragments reproduce the JSON exactly. **VI.2 is "The Reformed Cities - Zurich & Geneva," whose voices are Zwingli, Bullinger, Calvin, Beza and Marie Dentière — Zell is not among them**, as §15 item 4 states. No other census movement mentions her. "No other census-listed world currently claims her" is **true**.

**One observation for the portfolio, not a defect in this document.** I listed all thirty `VI.*` entries: only VI.1 and V.2 (Rhineland Mysticism) mention Strasbourg at all, and there is no Era VI entry for Strasbourg or the Bucer/Capito orbit. So the "adjacent-world witness" branch Doc_01 offered has, at present, **no adjacent world to receive her** — excluding her from VI.1 leaves her claimed by nothing in the census. That does not make this a portfolio decision (Doc_02 is not allocating her anywhere, and no other world's claim is disturbed), and it does not change the determination. But combined with Finding 1.4 — the live census still naming her as one of this world's voices — it is something that should leave a tracked item behind rather than only a disclosure inside a build document.

---

## Recommendation: not closed. One more round, tightly scoped — and here is exactly what is still wrong

**The Zell item is not closed.** The disposition is now the right one to rest on and the status statements finally agree, but the reasoning still asserts what it has not shown, and the mechanics broke in a new place. Nothing here needs another re-argument of the boundary question from scratch — the fixes below are all in-place, and none of them should change the outcome for Zell.

**Do not repeat the pattern. The pattern is: fix the thing the review named, in the place the review named it, and let the justification, the neighbouring rows, or the tallies drift out of step.** All four rounds have failed the same way. The specific things still wrong:

1. **Stop claiming the determination is demonstrated and evenly applied; state it as what it is.** Keep Excluded / Named Comparandum for the whole corpus. Rewrite §15 item 4 and R55 so the ground is: *on the evidence this document has — an unread edition, contents known only at title level — no part of Zell's corpus is shown to name or specifically identify the Wittenberg movement; the boundary default for a source not shown to belong here is Excluded, and that default is what is being applied.* Delete "a genuine, non-arbitrary, evenly-applied distinction" and "at every date" as positive findings about the content.

2. **Disclose that the Excluded branch changed, and stop attributing the change to Round 3.** §15 item 4 currently says Round 3 "correctly caught [the 1524 pieces] as the test's own Excluded branch being met." Round 3 said the opposite — that Revision 2 was *negating* the Excluded branch — and said explicitly that the determination "may well be right… but the document cannot rely on that." Replace that sentence with an honest one: Revision 2's Excluded branch was positive and restrictive, Revision 3's is a default residual, and that is a change this revision made, with its reason.

3. **Fix the Grumbach asymmetry, in one direction or the other, and say which.** Either (a) accept third-party reported content as admissible evidence for both women — in which case say plainly that no equivalent content-level inquiry was run for Zell's 1524 pieces, and that the determination stands pending one; or (b) require read-source evidence for both — in which case R54's Native status is equally provisional and must say so. What cannot stand is R55's Comparandum Note stating a reopening rule ("from a source actually read") that R54's own Native status does not satisfy.

4. **Rewrite R54's boundary-test paragraph to state the same test R55 states**, and re-derive Grumbach's Native conclusion under it. Two rows cannot both be "the one test applied to R54 and R55 alike" while stating incompatible branches. If the re-derivation shows R54 does not survive the naming requirement on read-source evidence, say so and mark R54 provisional — do not quietly keep two tests so that each row reaches its preferred answer.

5. **Repair R95: 12 cells → 11**, with the Added date restored to the Added column and the disposition text moved into the Source cell.

6. **Re-ground R95's disposition rather than borrowing the Template's unreliability provision.** Keep the row (append-only is right). Return Confidence to **B**, mark the disposition "superseded by R55, Revision 3," exclude it from the live Confidence tally with a one-line note, and disclose that the Template's E/removed-from-use provision addresses unreliability, not supersession.

7. **Fix the two locations still implying Native/licensed, plus one stale line:** §15's G1 Part B sentence (line 323) must not say R55 states what Zell is licensed for; the Registry's Conventions paragraph (line 9) must not say "no row is at E"; the living-document protocol (line 129) should read "after row 95."

8. **Add the column-count check Round 3 asked for**, before any further "schema check re-run by script" claim is made. Add a second check while there: assert that the Confidence tally in the summary agrees with the Conventions paragraph's own claims about which tiers are occupied.

9. **Register the census reconciliation as a tracked item** in §16 and in the seed list at item 8 — the live `world-census.json` still names Zell as one of VI.1's five voices, and no census world currently covers Strasbourg to receive her.

10. **Correct R55's "(§1.3, §6)" cross-reference to §12.1.**

**Then check the Zell thread one final time as a unit** — §11, §12.1, §15 item 4, §15 G1 Part B, §17's Round-3/Round-4 entries, R54, R55, R95, the Conventions paragraph and the full statistics block, read in one pass — and re-run the Registry parse with the column-count check in place.

**The standing note, extended.** Round 2's lesson was "never change a line citation without printing the line." Round 3's was "never change a determination without re-reading every section that states it." Round 4's is the one that would have caught all three of this round's failures: **never change a test, a tier, or a row's shape without re-reading everything that depends on it — the comparison row (R54 still states a superseded test as "the one test applied to R54 and R55 alike"), the tally (the Conventions paragraph still says no row is at E), and the schema (R95 now has twelve columns).** And one more, specific to this round: **when quoting what a review found, quote it.** Revision 3's single most consequential move — rewriting the Excluded branch into a default — was justified by a finding the previous reviewer did not make.
