# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 21 Independent Adversarial Review — scoped to verifying the Round 20 fix pass (all fifteen findings), a third re-check of Round 19's declined C1, a full bold-*nesting* sweep of lines the pass did not edit, and a cold cross-document sweep

**Documents reviewed (committed state — `git status --porcelain` clean, 0 lines, at `efc1a95`, "lpc: fix Round 20 review findings on Doc_02 revision (15 of 15)", 2026-09-08 08:52:02 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `worlds/lpc/Doc_02_Source_Ecology.md` (157 lines; §1 through §10 read in full, cold)
- `Source_Registry.md` (329 lines; all 212 rows re-parsed by column position; the front-matter rules, the Saturation statement and all fourteen of its round paragraphs, and the three closing accounting paragraphs read in full)
- `Source_Acquisition_Manifest.md` (88 lines, read in full — front matter, §1's nine G-items with every fulfillment paragraph, §2, §3, and the closing "Decision from the project lead" section)
- `lpc_Decision_Log.md` (337 lines, read in full — every entry, including the 2026-09-02 "First three post-disposition `Source_Registry.md` edits" entry, which this round checks against **four** sites rather than the three Round 20 checked)
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines), searched for the phrases Doc_02 attributes to it
- `Review-Artifacts/Doc02_Round15_Review.md` through `Doc02_Round20_Review.md`, read in full and in order — each round's own **Scope** paragraph extracted verbatim and counted, since two findings below turn on what those paragraphs actually say
- All 19 vendored `cic/texts/*.txt` files the pass touched (programmatic diff of the OCR clause, plus `git show fc18741` on one file to establish which round wrote which clause element); `prosper_chronica-minora-1-lat_mommsen1892.txt`, `perpetua-scillitan-martyrs-lat-grc_robinson1891.txt` and `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` opened at the exact lines the fix pass's own new disclosures name; all 56 atlas files in `cic/corpus-map/`; both engine scripts; `cic/texts/` file listing

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-08 vendoring, did not write the Round 15–20 fix passes, and did not write Rounds 1–20.

**Scope, stated plainly.** Four briefs, run together. First: verify, independently and against primary artifacts, whether each of Round 20's fifteen findings is actually closed by the `efc1a95` pass — and, since every one of the six preceding fix passes introduced or left at least one new checkable error while fixing what it targeted, look specifically for the three shapes this revision's history names: a fix that corrects its target while creating a new defect in the same sentence; a fix whose scope stops short of a sibling site carrying the identical defect; and a claim copied from one live document into another without re-derivation. Second: re-confirm, a third time, that Round 19's declined C1 was rightly declined — targeted, not re-derived from scratch, since Round 20 already opened the file at both loci and at its own page markers. Third: a full bold-marker **nesting** sweep of all four documents through an actual CommonMark parser, applied to the lines the pass did **not** edit as much as to the ones it did, since that is where Round 20's own M1 was found. Fourth: a cold cross-document sweep for staleness, internal contradiction, or unverified claim no round 1–20 has caught, with particular weight on the Doc_02 ↔ Registry ↔ Manifest ↔ Decision Log drift class, which has now produced findings in four of the last five rounds. Rounds 15–20 and the `efc1a95` commit message were treated as claims to re-derive, not as authority.

**Method — what was actually re-derived, not trusted.** A CommonMark render (markdown-it-py 4.2.0, `commonmark` preset) of **every** `**`-bearing line in all four documents (434 lines), with two independent tests run on each: (a) the rendered `<strong>` tree walked for nesting depth, unclosed spans, and literal `**` survival; (b) — the stronger test, not run by any prior round — the CommonMark span list compared **element by element against the naive sequential pairing** of that line's own `**` delimiters (1st↔2nd, 3rd↔4th, …), which is what the author intended in every case in these documents. Any line where the two disagree is a nesting defect by construction, whatever its parity. A fresh regex parser over all 212 Registry rows extracting each column by position, with row-number sequence, physical-order, pipe-count, `**`/backtick/parenthesis balance per row. `yaml.safe_load` across all 56 atlas files in `cic/corpus-map/`, recomputing every census figure and comparator Doc_02 §1 states. Direct line reads of `prosper_…mommsen1892.txt` 45876–45895, `perpetua-scillitan-…robinson1891.txt` 7373–7378, and `cyprian_opera-spuria-…pars3.txt` 40256–40262 against the exact strings the fix pass's own disclosures quote. Markup-stripped, entity-unescaped, whitespace-normalized verification of eight primary-source quotations in Doc_02 §1 and §2 against `anf05` and `npnf104` directly. `git show fc18741`/`efc1a95` diffs on all 24 changed files. Verbatim extraction of each of Rounds 15–20's own Scope paragraphs. Both engine scripts re-run. Nothing was carried forward from Rounds 15–20's tables, from `lpc_Decision_Log.md`, or from the commit message.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 0 HIGH · 4 MEDIUM · 5 LOW · 4 COSMETIC.**

**All fifteen of Round 20's findings are genuinely closed, and the two structural ones are closed exactly.** H1's false provenance predicate is gone from both sites and both replacements match the Manifest's own line-59/line-85 wording. **M1 is fully closed and independently proved so by a test no prior round ran:** across all 434 `**`-bearing lines in all four documents, CommonMark's own pairing is **identical to the naive sequential pairing on every single line** — zero nested spans, zero unclosed spans, zero literal `**` surviving any render, zero `****`. Doc_02 line 29, the defect site, now produces five sibling spans, each closing at its own colon or terminal period, the 1,544-character swallow gone. C1 is closed with the same completeness: Registry row 42 now reads `` `confidence: provisional` ``, and the table's `confidence:` code spans are now 26 `assigned` + 7 `provisional`, all 33 free of markers. M2's identifiers are right (`histoirelittra01moncuoft`, `histoirelittra02moncuoft`, `histoirelitterai03monc_0`). M3's four sites match rows 31–33. M4's rename resolves, and both Doc_02 pointers now name headings that exist and are unique. L1's clause is byte-identical in all 19 files. L4's two quotations are now literal (`QITIBUS` at line 45883, `Adam cum e.sset` at 45891, both confirmed at the lines named). C3's two broadened disclosures are exact against the files (`Augus-`/`tas,` split at 7375–7376; the Vita heading across 40258/40260 with the closing period). C4's proportions now match the siblings (13% bold, against line 87's 13% and line 61's 7%). Registry integrity, both engine scripts, and every census figure hold.

**Round 19's C1 remains correctly declined, on a third independent check.** The Prosper file reads `EPITOMA DE CHRONICON,` at line 45881, between the praefatio's last line (45876) and the chronicle's first entry (45891). Nothing found this round disturbs Round 20's re-derivation.

**The recurrence has again moved to the sites the pass did not sweep — and, once, into the replacement text itself.** Four MEDIUM. Two are the scope-propagation shape at sites inside the very documents the pass edited: the recall-test enumeration L3 was written to retire survives, still enumerated and *already one round stale*, three paragraphs below the paragraph L3 fixed (M1); and the 2026-09-02 post-disposition edit whose non-propagation was Round 20's M3 has a **fourth** unswept site, inside `Source_Registry.md` itself, where the M3 fix pass did not look (M2). One is the new-false-claim shape, written by the fix pass into three live documents while replacing the sentence Round 20's L2 named: Round 15 is now characterised as having been "scoped to verifying the prior round's own fix pass," which its own artifact contradicts in terms, and Rounds 18–20 are characterised as not re-reviewing the document set in full, which their own Scope paragraphs — and the same Decision Log paragraph's own next sentence — contradict (M3). One is pre-existing and previously uncaught by all twenty rounds: Registry row 45's Verification Note opens, in bold, with "Not currently vendored" for a work its own closing sentence says was vendored on 2026-09-05 (M4). The LOW and COSMETIC findings are attribution lag in the same clause L1 just fixed, a sibling heading four lines from the one L5 fixed, a per-round string the M4 rename created a cross-document dependency on, and residuals in the §3 bullets the M3 fix edited.

---

## MEDIUM

### M1. The per-round recall-test enumeration L3 was written to retire is still live at a third site in the same document — `Source_Registry.md` line 325 — and is *already* one round stale

The L3 fix is correct where it landed. Registry line 295 now reads, statelessly:

> **The ten-item relative-recall test and PRESS question … were run once per review round through Round 14 … No round after Round 14 has run either instrument** (stated here as a standing rule rather than a per-round enumeration, independent review Round 20's own L3, after the enumerated version — "Rounds 15, 16 and 17," then "Rounds 15 through 19" — went stale twice in two rounds …)

Doc_02 §9 item 6 (line 136) carries the identical stateless rule. Both are right, and both stay right without a per-round edit.

**Three paragraphs below line 295, in the same Saturation statement, line 325 was not touched:**

> **A round-by-round instrument accounting, rather than a running total restated here:** across the fourteen rounds that actually ran the test (Rounds 1–14), the recall score returned 0/10 in every round except Round 2 (3/10 …) … **Corrected here (independent review, Round 19):** **Rounds 15 through 19** did not run the test at all, per the paragraph above — they are not a further instance of "0/10" and this sentence no longer states or implies otherwise.

That is the enumerated form, at the second of the two sentences Round 19's own M1 split into limbs — and it is already short by one round. Round 20 ran no ten-item recall test and answered no PRESS question (`Doc02_Round20_Review.md` contains the string "recall" only inside its own M1/L3 findings *about* the Registry's claim; no score, no ten-item list, no PRESS answer appears anywhere in it), and neither does this round. So a reader is told, in the Registry's own voice, about Rounds 15–19 and left to infer the rest — the exact property L3 existed to remove, in a paragraph whose own opening clause ("rather than a running total restated here") announces the opposite policy.

A grep across all four documents for live per-round enumerations of this fact returns exactly one hit that is not a historical quotation inside a correction note: this one. The stateless wording is already written twice, thirty lines above and in Doc_02; only this sentence was left out of the sweep.

Rated MEDIUM on the same footing as Round 19's own M1 first limb, which was the identical defect (an enumeration one round short) at the sibling sentence in the same paragraph block.

### M2. The 2026-09-02 post-disposition edit has a fourth un-propagated site — inside `Source_Registry.md` itself, at line 327 — and it describes rows 32 and 33 in a state those rows' own notes reversed six days ago

Round 20's M3 found Doc_02 §3 and §9 item 3 contradicting Registry rows 31–33 about those rows' verification state, traced to the logged 2026-09-02 WebSearch edits never being propagated into Doc_02. The fix pass corrected all four Doc_02 sites. It did not check whether the Registry's own prose says the same thing about its own rows. It does not.

`Source_Registry.md` line 327, in the Saturation statement:

> **Independent verification credited across all rounds run so far, not only imported as a claim.** Round 1 independently WebSearch-verified rows **31** (Lancel), **32** (Burns, *Cyprian the Bishop*), **33** (Burns & Jensen), **34** (Fahey), and **35** (Rebillard) as bibliographically accurate … — **this Registry's own rows for 32–35 continue to state that they were not independently checked or bibliographically re-verified via WebSearch this session and remain flagged**, which is the right direction (under-claiming rather than over-claiming) …

Checked row by row against the current table:

| row | what line 327 says the row says | what the row actually says |
|---|---|---|
| **32** | not WebSearch-re-verified; remains flagged | *"**2026-09-02 update:** … Both editions independently confirmed via WebSearch bookseller/catalogue records this session; still not independently re-read. **Flag resolved**"* |
| **33** | not WebSearch-re-verified; remains flagged | *"**2026-09-02 update:** bibliographic details **now independently verified via WebSearch** … flagged for that [Confidence] decision **rather than for further second-opinion review, which this update has already satisfied**"* |
| **34** | not WebSearch-re-verified; remains flagged | *"not independently checked or bibliographically re-verified via WebSearch this session. **Flagged for priority second-opinion review**"* — accurate |
| **35** | same | same — accurate |

So the sentence is false for two of the four rows it names, in both of its predicates: rows 32 and 33 no longer state they were not WebSearch-verified (they state they were), and row 32 no longer "remains flagged" at all. The paragraph's own justification for keeping the divergence — *"which is the right direction (under-claiming rather than over-claiming)"* — no longer describes anything real, since the rows themselves now claim the check.

This is the same defect class Round 20 rated MEDIUM at its own M3, at the fourth site of the same 2026-09-02 edit, inside the document Round 20 was measuring Doc_02 *against*. It has stood uncaught through Rounds 15–20 and was not swept by the pass that fixed the other three sites. Nothing here asks for a Confidence-letter change; only the Registry's own description of its own rows needs to agree with those rows.

### M3. The L3 replacement wording newly mischaracterises Round 15's own scope, and overstates exclusivity for Rounds 18–20 — at three sites, one of which contradicts itself in the next sentence

The L3 fix did not only make the recall-test claim stateless; it rewrote the scoping clause attached to it. `Source_Registry.md` line 295 now asserts, in bold:

> **each round from Round 15 on has been scoped to verifying the prior round's own fix pass against the 2026-09-08 source-integration revision, rather than to re-reviewing this document set in full, and none has run either instrument in that scope — Round 15 disclosed this explicitly in its own artifact; every round since has continued the same scoping without repeating the disclosure.**

Doc_02 §9 item 6 (line 136) carries the same claim in short form: *"**Each round from Round 15 on has been scoped to verifying the prior round's own fix pass rather than to a full re-review**"*. `lpc_Decision_Log.md` line 334, rewritten in the same pass for L2, carries the third variant: *"including **every round after Round 15, each one commissioned specifically to verify the previous round's own fix pass rather than to re-review the document set in full**"*.

Two things are wrong, and the first is new to this pass.

**(a) Round 15 was not scoped to verifying a prior fix pass — there was none to verify.** `Doc02_Round15_Review.md` line 15, verbatim:

> **Scope, stated plainly rather than left implicit.** This round is **not** a fifteenth full review of Doc_02. Its brief was to re-derive, against primary artifacts, only **what the 2026-09-08 revision newly asserts**, plus the cross-document consistency and stale-claim questions those new assertions raise.

Round 15 was the *first* round against the 2026-09-08 revision; it reviewed the revision itself. The wording this pass replaced had it right — `git diff fc18741..efc1a95` shows the removed text read *"Rounds 15 through 19, scoped specifically to verifying **the 2026-09-08 source-integration revision** rather than re-reviewing this document set in full"* — and the replacement swapped the object of "verifying" from the revision to "the prior round's own fix pass," which is true of Rounds 16–20 and false of Round 15. The sentence then compounds it: *"Round 15 disclosed this explicitly in its own artifact"* now points at a disclosure Round 15 did not make. (Round 15 did disclose the recall-test non-run explicitly; it disclosed nothing about verifying a prior fix pass.) Round 20's own "What was checked" certified the *old* sub-claim as "exact on both halves"; the new one is not.

**(b) "rather than to re-review the document set in full" is false for Rounds 18, 19 and 20.** Their own Scope paragraphs, extracted verbatim this round:

- `Doc02_Round18_Review.md`: *"**Two briefs, run together.** First: verify … Second: **a genuinely cold, whole-document read of §1 through §10** for anything no prior round happened to check…"*
- `Doc02_Round19_Review.md`: *"**Two briefs, run together.** First: verify … Second: **a cold, whole-document read of §1 through §10** … and `Source_Acquisition_Manifest.md` checked for the staleness class Round 18 found…"*
- `Doc02_Round20_Review.md`: *"**Three briefs, run together.** … Third: **a cold, whole-document sweep** … across every line of all four documents, for Registry table integrity, and for staleness or internal contradiction no prior round happened to check…"*

Round 20's own L2 established this distinction in terms and is the reason the number was removed; removing the number while keeping — and now extending — the exclusivity does not answer that finding, it restates it without an arithmetic tell.

The Decision Log version contradicts itself inside one paragraph: line 334 asserts every round after Round 15 was commissioned "rather than to re-review the document set in full," and then, four sentences later in the same paragraph, credits Round 20 with *"two pre-existing defects (M3, M4) surfaced only because this round read text no prior round had checked against its own companion document"* — which is a full-re-review finding by construction.

Rated MEDIUM on the same footing as Round 18's own M1/M2 (a correction banner asserting something the underlying artifact does not support, written in the act of fixing something else), at three sites rather than two.

### M4. `Source_Registry.md` row 45 opens its Verification Note, in bold, with "Not currently vendored" — for a work its own closing sentence says was vendored on 2026-09-05, and which the Manifest's own G3 entry points a reader at this row to learn about

Row 45 (line 59), Verification Note, in full order:

> **Not currently vendored.** Already named in Doc_01 §5 as "not vendored in this corpus" … **Corrected here (Round 2's own H2): the archive.org item this row previously named … is a 2008 audio recording …** The actual bilingual scanned text edition … is a separate Internet Archive item: `archive.org/details/sanctiaugustiniv00possrich`. **Now vendored as row 192 (2026-09-05) — this row kept as the standing reference; row 192 for the actually-committed file and its own Confidence A / OCR-quality assessment.**

The cell's own first bolded assertion and its own last bolded assertion contradict each other. A programmatic sweep of all 212 rows for cells containing both a "not vendored" and a "now vendored" claim returns exactly two: row 40, where the negative is explicitly qualified (*"Not vendored **under this row's own number**"* — correct, since Harnack's edition is at row 205), and row 45, where it is not qualified at all.

This is the eighth sibling of the defect Round 15 rated **HIGH** at its own H4 — Registry rows still reading "Not currently vendored" for work already vendored. The seven rows Round 15 named (40, 41, 56, 78, 89, 90, 99) were all rewritten to open with their current state; row 39 and row 61, the two other "standing reference" rows, likewise now open with *"Pars I and II now vendored as row 191…"* and *"Pars I–IV all now vendored…"*. Row 45 alone kept its stale opener, and it was never swept because its own fulfilment is dated **2026-09-05**, not 2026-09-08 — outside the batch every subsequent round has been checking.

It is not inert. `Source_Acquisition_Manifest.md` G3 (line 29) routes a reader here — *"Registry row 45."* — from a paragraph whose immediately following "Fulfilled 2026-09-05" note says the opposite; and row 45's Licensed-For column still describes the Megalius identification as resting on a work "Doc_01 §5 and §9 both disclose as unvendored," which is accurate about Doc_01 but sits one column away from a bold sentence asserting the same thing in the Registry's own voice about the present.

Rated MEDIUM rather than HIGH because the same cell corrects itself three sentences later and no live claim rests on the negative — but it is a direct internal contradiction in a disposed document's own table, previously uncaught by all twenty rounds.

---

## LOW

### L1. The OCR clause's new attribution drops Round 19 — whose own edit is the clause element still visible in the text — in all nineteen files

The L1 fix is mechanically complete. All 19 files carry, byte-identical and exactly once each:

> Note (independent review, Round 18; **extended, Round 20**): quotations **in this header** (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility…

Limb 1 of Round 20's L1 is fully answered: "elsewhere in this header" is gone and the governing phrase no longer excludes the field the parenthetical adds.

Limb 2 is answered by half. `git show fc18741` on the vendored files establishes which round wrote which element: the Round 19 pass added **"or this Provenance note itself"** to the parenthetical (removing `(Content note, Source line, or Title)`, adding `(Content note, Source line, Title, or this Provenance note itself)`); the Round 20 pass changed "elsewhere in this header" to "in this header" and relabelled. Both edits are live in the current clause. The label names Round 18 and Round 20 and skips Round 19 — so nineteen files now attribute Round 19's field-list to Round 20.

This is the same defect Round 20's L1 named, one round on: *"the text changed and the label did not."* Here the label changed and skipped a round. The convention Round 20 cited for the remedy is stacking — Doc_02 §1 line 25 carries three ("Round 17 … Round 18 … Round 19"), Doc_02 §2 line 54 now carries two ("Round 19's own C2 … Round 20's own M4") — and the exemplar Round 20 pointed to (Registry line 295's *"Round 18; extended, Round 19"*) was itself rewritten away in this same pass, so the file headers are now the only place this clause's history is recorded at all.

### L2. `Source_Acquisition_Manifest.md` §2's heading is stale in exactly the way §1's was — four lines' worth of sweep away from the heading L5 fixed, over a section whose single item is marked Resolved

The L5 fix is correct and follows the Manifest's own convention: line 15 now reads *"## 1. G1–G9 — public domain acquisition candidates, eight now closed"*, with a correction note at line 17 modelled on the §3 and "Decision from the project lead" precedents.

Line 65, the next heading in the same document:

> ## 2. Not yet a confirmed acquisition candidate (named for completeness)

Its one and only item, line 67:

> - **The *Acta Proconsularia Sancti Cypriani*** … Registry row 41. … **Resolved 2026-09-08:** G1's own Pars III fulfilment includes the Acta Proconsularia directly (pp. CX–CXIV of the printed volume, immediately following the Vita) — vendored as part of Registry row 194; **this item is no longer an open question.**

So §2's heading asserts, of a one-item section, that the item is "not yet a confirmed acquisition candidate," over an item that is neither a candidate nor unconfirmed nor unacquired. `Doc_02_Source_Ecology.md` §9 item 8 independently records the same closure (*"**Resolved 2026-09-08.**"*), and Registry row 41 opens *"**Now vendored, inside row 194**"*. This is Round 20's L5 exactly, at the adjacent heading, and the reasoning L5 gave applies unchanged: this Manifest treats stale headings as real defects and has now corrected four of them on that basis.

### L3. The M4 rename fixed the heading by putting a per-round enumeration in it — and Doc_02 §2 now quotes that string verbatim, creating a two-document dependency the next round must edit

The M4 fix is correct on its facts. `lpc_Decision_Log.md` line 318 now reads *"### 2026-09-08 — Doc_02 revision, **Rounds 15 through 20**: independent adversarial review rounds…"*, the entry does carry six round paragraphs, and `grep "^### "` confirms it is one of exactly four entries dated 2026-09-08, uniquely identified by that title. Doc_02 §2 line 54's pointer quotes the new string and resolves.

But the remedy chosen is the form this same fix pass retired twice, on the explicit ground that it must be re-edited every round. L2 removed "three consecutive rounds" because *"a count each further round in this run would otherwise need to increment in turn"*; L3 removed "Rounds 15 through 19" at two sites because *"the enumerated version … went stale twice in two rounds."* The heading now says "Rounds 15 through 20" over an append-only entry that takes a further paragraph each round — and, unlike the two enumerations just retired, this one is **quoted verbatim in a second document**, so the next rename breaks Doc_02 §2's pointer unless both are edited together. A stateless title ("Rounds 15 onward," or the entry's date and subject alone) would have discharged M4 without adding the dependency.

Rated LOW rather than COSMETIC because the coupling is cross-document and because Doc_02 §2's own pointer is the thing Round 19's C2 and Round 20's M4 were both spent on.

### L4. Doc_02 §9 item 3's regrouping fix moved row 33 correctly and left row 37 in a group its own Discovery-channel column contradicts

The M3 regrouping is right for the row it moved. §9 item 3 (line 133) now reads:

> Rows **34, 35, 37, and 38** of `Source_Registry.md` (Fahey, Rebillard, *CIL* VIII, basilica archaeology) **remain recalled from field knowledge** rather than independently re-read this session … Rows **30–33** … are bibliographically WebSearch-verified but not independently re-read …

Rows 34, 35 and 38 carry Discovery channel `builder-prior-knowledge / field knowledge / 2026-09-01` and Verification Notes saying so. **Row 37 does not.** Its Discovery channel reads `Donatism build's own Registry, row 48 / 2026-09-01`, and its Verification Note grounds it there: *"**Already vendored on the sibling Donatism build's own branch** … (confirmed here, Round 5's own M9…)"*. It is inherited from another world's independently-verified Registry entry, not recalled from field knowledge — the same footing as row 36 (Shaw), which §9 item 3 correctly does **not** place in either group and which Doc_02 §3 describes accurately as *"relied on via the sibling Donatism build's own already-verified Registry entry."*

So the item describes two different provenances with one phrase, and the row that does not fit sat inside the exact clause the M3 fix rewrote. Same one-member-at-a-time shape as Round 19's L2 and Round 20's M2. What is true of row 37 — not independently re-checked against a specific volume or inscription this session, flagged for priority second-opinion review — is stated correctly in the row itself; only Doc_02's characterisation of *why* is wrong.

### L5. The M3 fix copied row 33's "five independent scholarly reviews" into Doc_02 §3 — a figure row 33's own parenthetical names four of, and the Decision Log's record of the same check contradicts

Doc_02 §3's Burns & Jensen bullet, rewritten this pass:

> Confidence C … **WebSearch-verified this session across five independent scholarly reviews and the publisher's own catalogue page** (Registry row 33's own 2026-09-02 update — corrected here, independent review Round 20's own M3 …)

Registry row 33, the source of that phrase:

> confirmed consistently across **five independent scholarly reviews** (*Journal of Ecclesiastical History*, *Journal of Theological Studies*, *Reviews in Religion & Theology*, Project MUSE) **and the publisher's own catalogue page** (eerdmans.com)

The parenthetical enumerates **four** items — and one of them, Project MUSE, is a hosting platform rather than a journal — for a claim of five, then adds the publisher page on top, totalling six sources.

`lpc_Decision_Log.md` line 138, the project's own contemporaneous record of that identical check:

> **Row 33** … publisher, city, year, ISBN, and collaborator list independently confirmed across **five sources (four scholarly-journal reviews plus the publisher's own catalogue page)**, all consistent.

Five sources total, four of them reviews. The Registry's figure double-counts the publisher page; the Decision Log's does not. The two have contradicted each other since 2026-09-02, uncaught by Rounds 15–20 — and this fix pass has now propagated the higher of the two into a third live document without checking it against either the parenthetical it sits beside or the log entry it derives from. That is the H1 shape (a claim copied from one live document into another rather than re-derived), at a magnitude rather than a substance.

Rated LOW, not MEDIUM: the underlying verification state Doc_02 now reports for row 33 is correct, and nothing turns on whether four or five reviews were consulted. Only one of the three numbers needs to change, and the artifacts do not say which.

---

## COSMETIC

### C1. The renamed Decision Log heading says "each fixed" over an entry that twice records a finding deliberately not fixed

Line 318, as rewritten this pass: *"Doc_02 revision, Rounds 15 through 20: independent adversarial review rounds … **each finding real defects, each fixed** …"*. The entry's own body says otherwise in two places: Round 15's paragraph records that *"the seventeenth, C2 … was deliberately left"*, and Round 20's records that *"All fifteen findings are fixed above, **with the one exception** that Round 20 itself confirms should stay unfixed: Round 19's own C1."* The predecessor heading carried the same overstatement ("both finding real defects, both fixed") and it survived the rewrite. It matters slightly more now than before, because Doc_02 §2 sends a reader to this heading as *"the fuller record of what each round found."*

### C2. Doc_02 §3's Lancel bullet still hedges the French original as "c. 1999," in a bullet this pass edited, against row 31's now-unhedged 1999

Line 66's citation head reads *"(French original **c. 1999**; English translation, London: SCM Press, 2002)"*. Row 31's Source column, since the 2026-09-02 update, reads *"(London: SCM Press, 2002; French original *Saint Augustin*, Paris: Librairie Arthème Fayard, **1999**)"*, and the update itself records two journal reviews citing the imprint *"from the **1999** French original."* The M3 fix rewrote the rest of this bullet to match the row and left the circa. Nothing depends on it; it is the smallest instance of the one-clause-repaired-one-left shape, in the same sentence.

### C3. Doc_02 §3's Burns & Jensen bullet says "WebSearch-verified this session" in the same sentence in which it cites the row's "2026-09-02 update"

Elsewhere in §3, "this session" means the 2026-09-01 drafting session (rows 34, 35: *"not independently checked or WebSearch-verified this session"*, matching those rows' own wording). The Burns & Jensen verification happened on 2026-09-02, in a separate post-disposition session the same sentence names by date. The Lancel bullet has the same shape (*"WebSearch-verified this session and … reconfirmed"*, where the reconfirmation is the 2026-09-02 update). Both are newly-written or newly-edited text from this pass; neither is false on a loose reading of "this session," but the phrase and the date in one sentence pull against each other.

### C4. The Manifest's priority-ordering advice at line 85 still reads as though all nine G-items were open, with no superseding marker of its own

Line 85: *"a reasonable alternative to acquiring any of G1–G9 is to proceed with Doc_03 and beyond on the currently-vendored ANF05/NPNF corpus alone, **treating all nine as optional depth** … If a priority ordering is wanted rather than an all-or-nothing choice: G3 (Possidius), G4 …, and G7 … add the most real value …"* — a live acquisition recommendation over eight items that are closed. It is corrected in effect by line 87's "Status update, 2026-09-08" immediately below, which is why this is COSMETIC and not LOW; but line 83's *"(Awaiting Mark's decision…)"* paragraph is named and quoted by that update (*"The 'awaiting Mark's decision' framing above…"*) while line 85's is not, and this Manifest's own practice — at line 11 (Round 19's M2), line 61, and line 17 (Round 20's L5) — is to mark the superseded paragraph at its own site.

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**Bold-marker nesting across all four documents, by two independent tests, including on every line the pass did not edit.** All 434 `**`-bearing lines rendered through markdown-it-py 4.2.0 (`commonmark`). Result: **zero** nested `<strong>` spans, **zero** unclosed spans, **zero** literal `**` surviving any render, **zero** `****` sequences, and **zero** lines where CommonMark's own delimiter pairing differs from the naive sequential pairing of that line's `**` markers. The second test is the decisive one — it is what a parity count cannot do and what a "no literal `**` survives" check cannot do either, since Round 20's M1 defect produced neither symptom — and it passes on every line in all four documents, not only the edited ones.

- **Doc_02 line 29 (M1's site), span by span:** five sibling spans at depth 1, lengths 1594 / 248 / 436 / 162 / 378. Span 1 ends at *"…not 'a single' one."*; spans 2, 3 and 4 each end at their own colon (*"…to the contrary:"* / *"…that stated only the first limb):"* / *"…overstated it:"*); span 5 is the new Round 20 note, ending at *"…only the markup."* The 1,544-character swallow Round 20 measured is gone, and the two passages it wrapped (the Acta Proconsularia sentence, the Retractationes sentence) now render plain.
- **Doc_02 line 25 (Round 19's L3 site):** four sibling spans, each closing at its own colon or terminal period. Unchanged and still correct.
- **Registry row 42 (C1's site):** `` `confidence: provisional` ``, no markers inside. Counted directly across the table: 26 `` `confidence: assigned` `` + 7 `` `confidence: provisional` `` = 33 code spans, all clean. The only remaining asterisk inside a code span anywhere in the four documents is `` `*^<>%™#@` `` at `lpc_Decision_Log.md` line 262, a deliberate quotation of a regex character class.
- **The new Manifest note (C4's site):** three sibling spans, no nesting.

**Round 19's C1 — re-confirmed a third time, from the file.** `cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt`, read at 45876–45895: line 45876 `De reliquis libris quicquam addere supervacaneum est.` (praefatio's last line); 45879 `PROSPERI TIRONIS`; **45881 `EPITOMA DE CHRONICON,`**; 45883 `QITIBUS ET GENERATIONES AB ADAM USQUE AD ABRAHAM ET A PAS-`; 45891 `1 Adam cum e.sset annorum CCXXX, genuit Setli.` `DE` is present at the second heading, the structure is exactly as the fix pass and Round 20 both describe it, and Round 20's page-marker derivation (the block sits between the file's own 384 and 386 markers, i.e. on printed p. 385, where the Content note locates it) is not disturbed by anything found this round. **The declination stands, now independently confirmed three times.**

**H1 — the provenance correction, checked at both sites and against the Decision Log.** Manifest line 11 now reads *"G1's remaining Pars III, G2, G5, G6, G7, G8, and G9 were fetched … directly by this build thread …; **G1's earlier Pars I–II and G3 in full were instead supplied directly by Mark himself, on 2026-09-05, before network access existed**"* — matching line 59 (*"G1's remaining Pars III, G2, G5, G6, G7, G8, and G9"*), line 85 (*"G3 was already fulfilled in full 2026-09-05"*), the G1 and G3 fulfilment paragraphs, and `lpc_Decision_Log.md`'s 2026-09-05 G1/G3 entries (which record the 403 gateway denial for `archive.org:443` on that date and the project lead supplying both files himself). Doc_02 §9 item 1's false predicate is removed from the list sentence and replaced by a matching correction note; `grep -c "independently fetched and verified directly"` on Doc_02 returns **1**, and that one occurrence is inside the correction note, quoting the withdrawn wording. Both sites now under-claim rather than over-claim, which is the direction CO-022's attribution discipline requires.

**M2 (Round 20's) — the Monceaux identifiers.** Registry row 56 now reads *"freely hosted at the Internet Archive (`histoirelittra01moncuoft`, `histoirelittra02moncuoft`, `histoirelitterai03monc_0` — corrected here, independent review Round 20's own M2, from an earlier draft's own `histoirelittra00moncuoft` …)"*. The three identifiers match rows 206, 207 and 208 and the three vendored files' own `Source:` lines (`monceaux_…tome2_1902.txt` line 7 reads `archive.org item histoirelittra02moncuoft`). A repository-wide grep for `histoirelittra00moncuoft` returns hits only in historical/correcting contexts: the Manifest's original G5 request paragraph (corrected two lines below by its own "Fulfilled" note), the Decision Log's own correction entry, and prior review artifacts. No live evidentiary use of the wrong identifier remains.

**M3 (Round 20's) — Doc_02 §3 and §9 item 3 against rows 31–33.** All three §3 bullets now match their rows: Lancel's flag *"now resolved"* against row 31's *"Flag resolved"*; Burns's year *"resolved by the same check … now closed"* against row 32's two-edition account and *"Flag resolved"*; Burns & Jensen *"WebSearch-verified … Flagged instead for the Confidence-letter decision … not for further second-opinion review"* against row 33's *"flagged for that decision rather than for further second-opinion review, which this update has already satisfied."* §9 item 3 has moved row 33 into the WebSearch-verified group. The remaining defects are L4 (row 37's group) and L5 (the review count), neither of which touches the verification-state claim M3 was about.

**M4 (Round 20's) — the Decision Log heading and both quoting pointers.** `grep "^### "` returns exactly four 2026-09-08 entries (lines 281, 291, 304, 318). Doc_02 §2 line 54 quotes *"Doc_02 revision, Rounds 15 through 20"* → resolves uniquely to line 318. Doc_02 §9 item 1 quotes *"Network access confirmed working"* → resolves uniquely to line 281, and is the *correct* entry for the claim it supports (the C2 fix), distinct from §2's target. The entry's own escalation paragraph now reads *"any of the **six** rounds"*, which matches its six round paragraphs.

**L1 (Round 20's) — the blanket sweep, verified file by file.** All 19 files carry the clause exactly once; a programmatic uniq across the 19 extracted clauses returns **one** distinct string; `git diff fc18741..efc1a95` shows exactly one changed line per file, and the change is exactly the two-element edit (governing phrase, attribution label). No stale clause is stacked anywhere. The four earlier Latin/bilingual files (rows 88, 191, 192, 193) correctly do not carry it. The wording issue is L1 above; the mechanics are complete.

**L4 (Round 20's) — the Decision Log's Prosper quotations, checked at the lines named.** Line 330 now reads *"…immediately preceding the chronicle's own first entry, '**1 Adam cum e.sset** annorum CCXXX') the file reads 'PROSPERI TIRONIS / EPITOMA DE CHRONICON, / **QITIBUS** ET GENERATIONES…' — quoted here in the file's own literal OCR form…"*. Both strings match the file byte for byte at lines 45891 and 45883. The paragraph now also discloses the normalisation it corrected, which is the standard the Registry rows received.

**C3 (Round 20's) — both broadened disclosures, verified at the exact lines.** Row 194: *"the file's own OCR reads 'iiiilgo' for 'uulgo,' and the heading itself runs across two lines with a closing period this quotation drops"* — file lines 40258/40260 read `VITA CAECILII CYPRIANI` / `(Pontio diacono iiiilgo adscripta).` Both limbs exact. Row 204: *"the file's own OCR reads 'xvI' for 'XVI,' and 'Augustas' is split across a line break as 'Augus-'/'tas,'"* — file lines 7375/7376 read `Praesente bis et Claudiano consulibus, xvI Kalendas Augus-` / `tas, Kartagine in secretario…`. Both limbs exact.

**C5 (Round 20's) — the two descriptive slips.** `lpc_Decision_Log.md` line 330 now reads *"Rounds 1 and 3–14 (in fact only Round 2 differed — corrected here, independent review Round 20's own C5, from an earlier draft's own 'Rounds 3–14,' which dropped Round 1 and undercounted by one)"*. Doc_02 §9 item 6 now names both rounds: *"naming only one of the two rounds it in fact added, **Round 18 and Round 19 both**, per Round 20's own C5."* Both correct.

**Registry table integrity, recomputed row by row.** All 212 rows re-extracted by column position: numbers **1–212 complete, no gap, no duplicate**; **every row exactly 12 pipes / 11 columns**; **every row balanced** on `**`, parentheses and backticks. Three physical-order inversions, at 48→42, 193→60 and 60→52 — the same three Round 20 found, all covered by the front-matter Disclosed-placement rule, which names "48, 52, 60 among them." Excluded set re-parsed from the Boundary Status column: `{28, 29, 98, 128, 204}`, unchanged; no live document states an Excluded enumeration.

**Census and comparator arithmetic, recomputed across all 56 atlas files.** `latin-pastoral-congregational-christianity.yaml`: **99 entries, 97 distinct titles, `Counter({'tradition': 90, 'context': 9})`, 88 distinct titles inside the tradition set, `Counter({'assigned': 87, 'provisional': 12})`**; exactly two duplicate titles (*The Enchiridion*, *The Passion of the Scillitan Martyrs*), so 90 − 2 = 88 reconciles. Comparators re-derived per measure: 99 raw against **68** (`post-apostolic-house-church.yaml`), 90 `tradition` against **59** (`post-apostolic-house-church.yaml` and `alexandria-catechetical.yaml`, tied). Doc_02 §1's "largest … on every count attempted" holds, as do both stated comparator figures. The nine `context` entries are Delehaye, Harnack, Monceaux I/II/III, both von Sodens, Prosper and the Codex Theodosianus — **seven of nine modern (1901–1921) secondary scholarship**, exactly as §1 says.

**Primary-source quotations, re-verified at source after markup stripping.** Eight of Doc_02's load-bearing quotations checked against the vendored XML directly, entity-unescaped and whitespace-normalised: *"by the judgment of God and the favour of the people"*, *"your suffrage and God's judgment"*, *"ancient venom"*, *"neither does any of us set himself up as a bishop of bishops"*, *"every bishop, according to the allowance of his liberty and power, has his own proper right of judgment"*, *"the condescension of his love had chosen me among his household companions to a voluntary exile"* (all `anf05`); *"from the Council and the epistles of Cyprian, to the effect that Christ's baptism may not be given by the hands of heretics"* and *"who strive to defend themselves by the authority of the most blessed bishop and martyr Cyprian"* (both `npnf104`). **All eight present and exact.**

**Cross-references and row citations.** Every row number cited in Doc_02 resolves to an existing Registry row; none falls outside 1–212. Every directional `§N above` / `§N below` reference in Doc_02 direction-checked programmatically: **none fails** (the one apparent hit is `Doc_01 §5 … (§1 above)`, where the two section numbers belong to different documents). Doc_02 §3's `Source_Registry.md` "line 8" pointer is still correct — line 8 is the checkpoint rule; line 6 is the Disclosed-placement rule — and this pass inserted and deleted no Registry lines. Rows 63 (Marec 1958, Hippo) and 82 (Ennabli 1997, Carthage) are the works Doc_02 §5 says they are; row 122 (Gillette 2001) licenses the Sermons 280–281 claim §6 makes from it.

**Rows 191–212, re-read for type/confidence consistency with Doc_02 §3's own account.** Rows 205–208 and 210–212 are all Type **S**, Confidence **C**, Native — matching §3's *"Five older, public-domain secondary works are now vendored in full … Confidence C."* Five distinct works across seven rows (Monceaux's three volumes being one work), consistent with the corrected "five, not four" count.

**Cross-branch claims, checked against this branch's own file tree.** `cic/texts/` holds 88 files. The three sibling-Donatism-branch files this Registry names as *not* present here — `cil8-supplementum-numidiae_cagnat-schmidt1894.txt` (row 37), `optatus_libri-vii-critical_ziwsa1893.txt` (row 64), `monceaux_…tome5_1920.txt` (Manifest G5) — are all genuinely absent, so those rows' "not present on this world's own branch" qualifiers are accurate and Doc_02 §5's *CIL* VIII "not currently vendored" is correct as stated.

**Engine scripts, both re-run this session.** `python cic/engine/texts_registry.py` → **exit 0**, *"OK: every vendored file has a header-verified rights line (public domain, or a recognized open licence), an ENTRIES row, and no ENTRIES row points at a missing file"*; 88 vendored files, 23 non-English, `cic/texts/` at 211 MB (30% of the 700 MB planning trigger). `python cic/engine/corpus_map_merge.py --check` → **exit 0**, 528 works → 788 assignments across 56 Atlas entries, no error.

**The methodological change the pass made, assessed on its own terms.** The pass's stated post-edit validation (LIFO-stack pairing per edited line, plus a whole-document CommonMark render checking for surviving literal `**`) is a genuine advance on the parity count Round 20 showed to be insufficient, and it did catch and fix the M1 site correctly. This round ran the stronger version of it — sequential-pairing comparison on **every** line, edited or not — precisely because that is the gap the pass itself disclosed, and it returns clean. The nesting defect class is, on this evidence, closed across all four documents; it is the only defect class this review sequence has been able to close by construction rather than site by site.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the fix pass and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** M2 concerns whether this Registry's own prose agrees with its own rows; M4 concerns a vendoring state inside this world's own table; L4 concerns how this world describes the provenance of one of its own rows, one inherited from the sibling Donatism build's Registry but not deciding anything for that build. Mark's 2026-08-26 Perpetua ruling and the Optatus double-placement are still reported rather than reasserted. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing here changes `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022, or any governing document. M1 and L3 are findings that a form this document has already ruled against in writing was reintroduced or left standing, not proposals to change the rule. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round **agrees with the fix pass and with Round 20, against Round 19**, on C1 — reached by opening the file at the lines named rather than by preferring any account. That disagreement is now closed three times over. M3 is a disagreement between a fix pass's replacement text and the review artifacts it describes: closed here by quoting each round's own Scope paragraph verbatim, not by preferring one text's authority. L5 is a genuine three-way numeric divergence (Registry row 33, its own parenthetical, and `lpc_Decision_Log.md` line 138) that this round has **not** been able to resolve from the artifacts, since the underlying WebSearch results are not recorded anywhere — but it is a source count inside an otherwise-correct verification claim, it changes no Confidence letter, no finding, and no disposition, and one of the three existing statements is already right. That is a defect to reconcile, not a tension the pipeline cannot close, and the reconciliation does not require the project lead. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

`Doc_02_Source_Ecology.md`'s status line and §10, and `Source_Registry.md`'s status line, still describe the Round 14 disposition of 2026-09-02, still read "Fourteen independent adversarial review rounds" over the sequence "(Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0)", and still point a reader to "`Doc02_Round1_Review.md` through `Doc02_Round14_Review.md`" — while `Review-Artifacts/` holds twenty `Doc02_Round*_Review.md` files before this one, Doc_02 carries 15 in-text attributions to Round 15, 7 to Round 16, 7 to Round 17, 6 to Round 18, 6 to Round 19 and 10 to Round 20, and `Source_Registry.md` carries 10, 4, 1, 4, 6 and 4 respectively. That is reported here as observed, checkable state, on the same footing Rounds 16 through 20 reported it. Whether and how those lines should change, and what disposition follows from this round's counts, is **not assessed here**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition. This review supplies only the input that rule takes: a finding count and a findings list.

**Observed trend, stated as raw counts only and not otherwise characterized.** Across the seven rounds against this 2026-09-08 revision: Round 15 — 4/6/5/2 (17); Round 16 — 4/5/6/3 (18); Round 17 — 0/3/5/4 (12); Round 18 — 0/4/3/3 (10); Round 19 — 0/2/4/3 (9); Round 20 — 1/4/5/5 (15); Round 21 — 0/4/5/4 (13). HIGH returns to zero. Three observations bear on reading this round's counts, stated without weighing them: one of the four MEDIUM findings (M4) pre-dates this revision entirely and has stood through all twenty prior rounds; one (M2) is the fourth site of a defect Round 20 found at three; and the defect class Round 20 rated HIGH last round — a false claim written into a live document by the fix pass itself — recurs here once, at M3, in the replacement text for one of the findings the pass was closing.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 0 HIGH · 4 MEDIUM · 5 LOW · 4 COSMETIC.**
