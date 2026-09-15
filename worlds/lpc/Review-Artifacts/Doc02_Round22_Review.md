# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 22 Independent Adversarial Review — scoped to verifying the Round 21 fix pass (all thirteen findings), a fourth spot-check of Round 19's declined C1, an independent re-run of the sequential-pairing-versus-CommonMark bold-nesting test, and a cold sweep weighted toward claims dated outside the 2026-09-08 batch

**Documents reviewed (committed state — `git status --porcelain` clean, 0 lines, at `f0be10a`, "lpc: fix Round 21 review findings on Doc_02 revision (13 of 13)", 2026-09-08 09:17:50 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `worlds/lpc/Doc_02_Source_Ecology.md` (156 lines by `wc -l`, as are all counts in this list; §1 through §10 read in full, cold)
- `Source_Registry.md` (329 lines; all 212 rows re-parsed by column position — **every column, not only the Verification Note**, which is where this round's HIGH finding sits)
- `Source_Acquisition_Manifest.md` (89 lines, read in full — front matter, §1's nine G-items with every fulfillment paragraph, §2, §3, and the closing "Decision from the project lead" section)
- `lpc_Decision_Log.md` (338 lines, read in full — every entry, with the 2026-09-05 G1/G3/G4 intake entries read against the vendored files they describe rather than against the rows that summarize them)
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines), searched for the phrases Doc_02 attributes to it
- `Review-Artifacts/Doc02_Round15_Review.md` through `Doc02_Round21_Review.md`, with each round's own **Scope** paragraph extracted verbatim, since the M3 fix's replacement text turns on what those paragraphs say
- All 19 vendored `cic/texts/*.txt` files the pass touched (programmatic diff of the OCR clause across all 19, plus `git show 6fd4973/5f8625f/fc18741/efc1a95/f0be10a` on one file to establish which round wrote which clause element); `possidius_vita-augustini_weiskotten1919.txt` and `prosper_chronica-minora-1-lat_mommsen1892.txt` opened directly; all 56 atlas files in `cic/corpus-map/`; both engine scripts; `cic/texts/` file listing
- **A live archive.org fetch** — item metadata and the full `_djvu.txt` for `sanctiaugustiniv00possrich` — run because the M4 fix's replacement text makes a provenance claim about that item that no document in this set had previously asserted

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-05 or 2026-09-08 vendoring, did not write the Round 15–21 fix passes, and did not write Rounds 1–21.

**Scope, stated plainly.** Four briefs, run together. First: verify, independently and against primary artifacts, whether each of Round 21's thirteen findings is actually closed by the `f0be10a` pass — and, since every one of the seven preceding fix passes introduced or left at least one new checkable error while fixing what it targeted, look specifically for the three shapes this revision's history names: a fix that corrects its target while creating a new defect in the same sentence; a fix whose scope stops short of a sibling site carrying the identical defect; and a claim written or copied into a live document without re-derivation. Second: spot-check that Round 19's declined C1 is undisturbed — targeted, not re-derived from scratch, since Rounds 19, 20 and 21 have each opened the file and reached mutually consistent line numbers. Third: independently re-run the sequential-pairing-versus-CommonMark bold-nesting comparison across every `**`-bearing line of all four documents, fresh rather than trusted from the commit message, to test whether Round 21's "closed by construction" claim survives this pass's edits. Fourth: a cold cross-document sweep, weighted per the commissioning brief toward **claims whose own relevant date falls outside the 2026-09-08 batch** — the shape Round 21's own M4 (row 45, fulfilled 2026-09-05) showed keeps escaping rounds scoped to that batch. Rounds 15–21 and the `f0be10a` commit message were treated as claims to re-derive, not as authority.

**Method — what was actually re-derived, not trusted.** A CommonMark render (markdown-it-py 4.2.0, `commonmark` preset) of every `**`-bearing line in all four documents (437 lines), with the rendered `<strong>` tree walked for nesting depth, unclosed spans, literal `**` survival and `****`, and compared element by element against a **run-aware** naive sequential pairing of that line's own bold delimiters (a run of two or three asterisks contributing exactly one bold delimiter, so that `***word***` — bold closing on an italic — is not mis-split, which a naive two-character scan does). A fresh regex parser over all 212 Registry rows extracting all eleven columns by position, with row-number sequence, physical-order, pipe-count and per-row `**`/backtick/parenthesis balance, plus a whole-table sweep of the **Licensed-For** column for present-tense acquisition-state claims — the column no prior round in this sequence appears to have swept for that. `yaml.safe_load` across all 56 atlas files in `cic/corpus-map/`, recomputing every census figure and comparator Doc_02 §1 states. Direct reads of `prosper_…mommsen1892.txt` at 42578–42586 and 45876–45892. A live fetch of `https://archive.org/metadata/sanctiaugustiniv00possrich` and of that item's own full text, byte-compared against the vendored Possidius file at both ends. Punctuation-normalized verification of six load-bearing primary-source quotations against `anf05` and `npnf104` directly, and of two Weiskotten quotations against the vendored Possidius file. Verbatim extraction of each of Rounds 15–21's own Scope paragraphs. Both engine scripts re-run. Nothing was carried forward from Rounds 15–21's tables, from `lpc_Decision_Log.md`, or from the commit message.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 1 HIGH · 2 MEDIUM · 3 LOW · 4 COSMETIC.**

**All thirteen of Round 21's findings are genuinely closed, and four of them are closed exactly.** M1's enumeration at Registry line 325 is now stateless and says nothing a further round must increment. M2's line-327 sentence now distinguishes rows 34–35 (accurate) from rows 32–33 (corrected), and both halves check out against those rows. M3's replacement wording is, at all three sites, **accurate against the review artifacts' own Scope paragraphs** — Round 15 is now described as reviewing the revision itself, and the "Rounds 18 onward also adding a cold, whole-document read" qualifier survives verbatim extraction of every Scope paragraph, including the narrower §1-and-§2 fresh reads Rounds 16 and 17 carried, which the wording correctly does not call whole-document. L1's attribution is byte-identical across all 19 files. L2's and C4's Manifest markers follow the document's own conventions. L4's row-37 regrouping matches row 37's own Discovery channel and Doc_02 §10's own parallel statement. L5 reconciles Registry row 33 and Doc_02 §3 to the Decision Log's "five sources, four of them reviews." C2's "c. 1999" is unhedged and matches row 31. Registry integrity, both engine scripts, every census figure and comparator, and all six primary-source quotations hold.

**The bold-nesting class is still closed by construction, independently reproduced.** Across all **437** `**`-bearing lines in the four documents — three more than Round 21 counted, the three lines this pass added — CommonMark's own delimiter pairing is identical to run-aware sequential pairing on **every single line**: zero mismatches, zero nested `<strong>` spans, zero unclosed spans, zero literal `**` surviving any render, zero `****`. Round 21's claim survives this pass's edits.

**Round 19's C1 is undisturbed** — the Prosper file still carries `EPITOMA CHEONICON` at line 42582 and `EPITOMA DE CHRONICON,` at line 45881, exactly as three prior rounds found. Nothing here reopens it.

**Where the recurrence went this time: into the one Registry column no round has swept, and into the M4 fix's own replacement sentence.** The HIGH finding is the ninth and tenth siblings of the defect class Round 15 rated HIGH at seven rows and Round 21 found an eighth of at row 45 — but in the **Licensed-For** column rather than the Verification Note, phrased "remains unacquired" rather than "not vendored," which is exactly why Round 21's own cell-level "not vendored"/"now vendored" sweep did not reach them, and with **no self-correction anywhere in either row**, which is the mitigation Round 21 cited for rating row 45 MEDIUM. Both rows are dated 2026-09-05 — the same outside-the-batch shape the brief asked this round to weight for. One MEDIUM is a claim the M4 fix newly wrote into row 45, asserting an archive.org item identity that five other sites in this same document set explicitly say is unknown and deliberately not guessed. The second MEDIUM is what checking that claim at source turned up: the vendored Possidius file's own provenance description — "a Google Books scan" — is wrong at four sites, and the archive.org item it actually derives from is an Internet Archive/MSN scan whose full text contains the word "Google" zero times.

---

## HIGH

### H1. Registry rows 191 and 193 state, in their own Licensed-For columns and in the present tense, that acquisitions completed on 2026-09-08 "remain unacquired" and that Manifest G1 and G4 "stay open" for them — with no correction anywhere in either row

Row 191 (line 248), Licensed-For column, in full:

> **The critical edition row 39 names, now actually vendored** — the Latin original behind the already-vendored ANF05 English translation of Cyprian's own corpus … and an independent check on that translation's own base text. **Covers Pars I and II only; Pars III (spuria and indices) remains unacquired and Manifest G1 stays open for that part alone**

Row 193 (line 250), same column:

> **Part of the edition row 61 names, now actually vendored** … **Covers Pars IV only; CSEL 34/1, 34/2, 44, and 58 remain unacquired and Manifest G4 stays open for those parts**

Both trailing clauses are false, and every other artifact in this set says so:

| claim | what the rest of the document set says |
|---|---|
| row 191: "Pars III … remains unacquired" | Registry **row 194**: *"**Vendored** at `cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`, closing Source_Acquisition_Manifest G1's own open Pars III gap"* |
| row 191: "Manifest G1 stays open for that part alone" | Manifest G1: *"**Pars III fulfilled 2026-09-08** … **G1 is now closed in full**"*; Registry **row 39**: *"Pars III … now also vendored, as row 194 (2026-09-08)"*; Doc_02 §9 item 1: *"G1 (Hartel's CSEL 3, **complete**, rows 191 and 194)"* |
| row 193: "CSEL 34/1, 34/2, 44 … remain unacquired" | Registry **rows 195, 196**, both *"**Vendored**"*, both fetched directly on 2026-09-08 from `sanctiaureliaugu34augu` and `sanctiaureliaugu44augu` |
| row 193: "Manifest G4 stays open for those parts" | Manifest G4: *"**G4 now stays open for CSEL 58 only**"*; Registry **row 61**: *"Pars I–IV all now vendored (rows 193, 195, 196…); only Pars V (CSEL 58 …) remains unacquired"*; Doc_02 §9 item 1: *"only CSEL 58 … is still unacquired"* |

Row 193's clause is wrong about three of the four volumes it names and right only about CSEL 58.

**Neither row corrects itself.** Row 191's Verification Note runs to a full OCR-quality assessment and a second-witness caveat and never mentions Pars III at all. Row 193's does the same and never mentions CSEL 34 or 44. This is the mitigation Round 21 explicitly relied on in rating row 45 MEDIUM rather than HIGH — *"the same cell corrects itself three sentences later"* — and it is absent here. A reader who lands on row 191 or 193 and does not independently follow the pointer to row 39 or 61 is told, in the Registry's own present-tense voice, that a closed acquisition request is open.

**Why twenty-one rounds missed them, stated precisely rather than guessed.** Round 15's H4 swept for *"Not currently vendored"* in the Verification Note; Round 21's M4 ran a programmatic sweep of all 212 rows *"for cells containing both a 'not vendored' and a 'now vendored' claim"* and reported exactly two hits (rows 40 and 45). Neither sweep reaches these two: the negative sits in the **Licensed-For** column, not the Verification Note; it is phrased *"remains unacquired"* / *"stays open"*, not *"not vendored"*; and in row 191's case it sits in the same cell as an affirmative *"now actually vendored"* that a cell-level pairing test reads as the correction. Both rows are dated **2026-09-05** in their own Added and Discovery columns — outside the 2026-09-08 batch, the same blind spot Round 21's own M4 named at row 45.

A fresh sweep of the Licensed-For column across all 212 rows for present-tense acquisition-state language (`stays open`, `remains open`, `remain(s) unacquired`, `still unacquired`, `awaiting`, `not yet located`) returns exactly these two live instances. Rows 41, 56, 78, 89, 90, 99 and 209–212 were all checked in the same sweep and are correct; row 61's own two "remains unacquired" instances are both correctly scoped to CSEL 58.

**A smaller point inside the same clause, for the fix pass rather than as a separate finding:** row 191 calls Pars III *"(spuria and indices)"*, which is the Decision Log's 2026-09-05 shorthand. Row 194's own Source column names its actual contents — the *Opera Spuria*, the *Vita Caecilii Cypriani*, and the *Acta Proconsularia* — and it is the Acta Proconsularia, not an index, that closes row 41 and Manifest §2.

Rated **HIGH**, one notch above Round 21's M4, on the calibration Round 21 itself set: this is the same defect class Round 15 rated HIGH at seven rows, at two further unswept sites, in a disposed document, and **without** the self-correction that took row 45 down to MEDIUM.

---

## MEDIUM

### M1. The M4 fix's own replacement sentence asserts an archive.org item identity that five other sites in this document set explicitly say is unknown and deliberately not guessed

Round 21's M4 asked for one thing: reorder row 45's Verification Note so it opens with its current state. The pass did that correctly. It also rewrote the cell's closing sentence. Before (`efc1a95`):

> The actual bilingual scanned text edition … is **a separate Internet Archive item**: `archive.org/details/sanctiaugustiniv00possrich`.

After (`f0be10a`):

> The actual bilingual scanned text edition … is **the same Internet Archive item vendored as row 192**: `archive.org/details/sanctiaugustiniv00possrich`.

That is a new claim — that the file committed as row 192 derives from this specific archive.org item — and it is contradicted, in terms, at five sites this pass did not touch:

1. `cic/texts/possidius_vita-augustini_weiskotten1919.txt`, `Source:` line: *"The exact archive.org item identifier was not stated when the file was supplied -- **to be added here once confirmed, per this corpus's own no-guessed-identifier discipline**."*
2. Registry **row 192**, Verification Note: *"the exact archive.org item identifier was not stated when supplied and **is not guessed**"*
3. `Source_Acquisition_Manifest.md` G3, "Fulfilled 2026-09-05": *"(exact item identifier not stated when supplied)"*
4. `lpc_Decision_Log.md`, 2026-09-05 G3 entry: *"The exact archive.org item identifier was not stated when supplied and **was not guessed**."*
5. The same entry's own "What remains open": *"The exact archive.org identifier, if the project lead can supply it."*

The word the rewrite dropped is also doing work: *"a separate Internet Archive item"* was separate **from `PossidiusAug`**, the audio recording the Round 2 H2 banner three sentences earlier is correcting. Replacing "separate" with "the same … as row 192" removes that contrast and substitutes an assertion about a different pair of things entirely.

**This round derived the claim rather than only flagging it, and it holds — which is the useful half of the finding.** A live fetch of `https://archive.org/metadata/sanctiaugustiniv00possrich` and of that item's own full text shows the vendored file is unmistakably built from it: the item's text opens `SANCTI AUGDSTINI VITA / iCRIPTA A POSSIDIO EPISCOPO / IC-NRLF / B IDfl 7E3 / … / FRKSENTEO TO THE / PRINCF.TON UNIVERSITY`, and the vendored file's own first body lines are that string character for character, garble for garble — OCR errors of that specificity do not recur across independent scans. The item's text then ends with the UC Berkeley circulation-desk slip (*"RETURN TO: CIRCULATION DEPARTMENT / 198 Main Stacks … UNIVERSITY OF CALIFORNIA, BERKELEY"*) that the Decision Log's G3 entry records stripping; the vendored file ends immediately before it, at the index's last entry (`Zosimus 160`).

So the remedy is not to withdraw row 45's sentence. It is that a claim of this kind is not this document set's to assert on inference — five sites currently promise a reader the identifier is open, and one now states it as settled. The fix pass had working network access (the Manifest's own §1 superseding note and the Decision Log's own 2026-09-08 entry both record it) and did not use it before writing the sentence. Rated MEDIUM as an internal contradiction across five sites in disposed documents, on the same footing as Round 21's own M2 and Round 20's own M3.

### M2. The vendored Possidius file's own provenance header, and three documents describing it, call its source "a Google Books scan" — the archive.org item it demonstrably derives from is an Internet Archive/MSN scan whose full text contains the word "Google" zero times

Checking M1 at source surfaced a separate, pre-existing error dated **2026-09-05**, the outside-the-batch shape this round was asked to weight for.

The claim, at four sites:

- `cic/texts/possidius_vita-augustini_weiskotten1919.txt`, `Source:` line — *"built from an archive.org-hosted 'Full text' / 'See other formats' view of **a Google Books scan** (the University of California, Berkeley library's own copy…)"*
- the same file's `Provenance note:` — *"**archive.org/Google Books site-navigation chrome and Google's own standard public-domain usage notice** (at the head of what was supplied) were stripped"*
- Registry **row 192**, Verification Note — *"Mechanically extracted from a docx Mark compiled from an archive.org 'Full text' view of **a Google Books scan** of the University of California, Berkeley's own copy"*
- `lpc_Decision_Log.md`, 2026-09-05 G3 entry — *"**Confirmed via the file's own embedded content**: an archive.org 'Full text' view of a Google Books scan of the University of California, Berkeley's own library copy"*, and its action list — *"archive.org/Google Books chrome and the library due-date slip cut"*

What the item's own archive.org metadata says, fetched this round:

| field | value |
|---|---|
| `identifier` | `sanctiaugustiniv00possrich` |
| `contributor` | University of California Libraries |
| `sponsor` | **MSN** |
| `scanningcenter` | **rich** (the Internet Archive's Richmond, CA scanning center) |
| `call_number` | `nrlf_ucb:GLAD-50452006` |
| `collection` | `cdl`, `americana`, `theses-and-dissertations` |

`sponsor: MSN` and `scanningcenter: rich` are the signature of an Internet Archive scan under the Microsoft/Open Content Alliance program, not a Google Books digitization; a Google-partner item carries neither field and does carry Google's usage notice in its own text. A direct count over the item's full `_djvu.txt` (386,678 characters) returns **zero** occurrences of "Google."

The "Berkeley library copy" half of the description is right — the call number is a Northern Regional Library Facility/UC Berkeley number, and the circulation slip is in the scan. It is the "Google Books scan" half that is not, and it carries a second claim with it: that "Google's own standard public-domain usage notice (at the head of what was supplied) were stripped" describes an extraction step performed on material the source item does not contain. The Decision Log's *"Confirmed via the file's own embedded content"* is the load-bearing sentence, and it is the one that does not hold.

Nothing rights-critical turns on this — the public-domain basis stated everywhere is the 1919 imprint date, which is unaffected — and this round makes no claim about the Hartel (row 191) or Goldbacher (row 193) intakes, whose own source items were not checked here and whose "Google Books scan" descriptions may well be correct. But `cic/texts/INTAKE.md` §4 makes the provenance header the artifact of record for where a vendored file came from, and this is the header of a Confidence **A** row — the only file in this world's 2026-09-05/09-08 intake carrying ordinary-primary-evidence footing.

Rated MEDIUM, on the same footing as Round 21's own M4: a pre-existing, previously-uncaught factual error inside a disposed document, dated outside the batch every round since Round 15 has been checking, that no live substantive claim rests on.

---

## LOW

### L1. Two adjacency claims this pass newly wrote are wrong — the Manifest's "four lines above it" is fifty lines, and the Registry's "the paragraph immediately above this one" is fifteen paragraphs above

Both are in correction text the pass authored, both point a reader at the wrong place, and both trace to a phrase adopted from Round 21's own finding titles rather than re-derived.

**(a) `Source_Acquisition_Manifest.md` line 67**, the new §2 heading-correction note:

> **Heading corrected here (independent review, Round 21's own L2), on the same reasoning as **the §1 heading four lines above it** (Round 20's own L5)…**

`grep "^## "` on the Manifest returns headings at lines **15** (§1), **65** (§2), **71** (§3), **81** ("Decision from the project lead"). §1's heading is **fifty** lines above §2's, not four. Round 21's own L2 body states the two line numbers correctly (*"line 15 now reads…"*, *"Line 65, the next heading in the same document"*); only its finding **title** used the phrase "four lines' worth of sweep away," and it is that phrase that was carried into the live document as a spatial claim it was not making.

**(b) `Source_Registry.md` line 325**, the new stateless recall-test sentence:

> …the same enumeration defect **the paragraph immediately above this one**, and Doc_02 §9 item 6, were already converted to a standing rule to retire

The paragraph immediately above line 325 is line 323 — the ***Round 14*** per-round instrument paragraph, which was not converted to anything. The paragraph actually meant is line **295**, thirty lines and fifteen paragraphs above, with the whole Round 1–14 round-by-round record between them. Round 21's own M1 got the distance right (*"Three paragraphs below line 295 … line 325 was not touched"*, and *"already written twice, thirty lines above"*).

Neither error misdirects a reader to a wrong *target* — both sentences also name the target by section ("the §1 heading", "Doc_02 §9 item 6"), so the referent is recoverable — which is why this is LOW rather than MEDIUM. But it is the same shape Round 18 rated MEDIUM when a `Source_Registry.md` line pointer inside Doc_02 §3 had drifted onto the wrong paragraph: a cross-reference that does not resolve to what it says it resolves to, this time wrong on the day it was written rather than after eleven rounds of drift.

### L2. The OCR clause's attribution still starts at Round 18, but the clause was introduced at Round 17 and Round 17's own wording is still visibly in it — in five of the nineteen files

The L1 fix is mechanically perfect. All 19 files carry, exactly once each and byte-identical through the clause's full 734-character common prefix:

> Note (independent review, **Round 18; extended, Round 19; extended, Round 20**): quotations in this header (Content note, Source line, Title, or this Provenance note itself) are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, a single word broken into multiple tokens or joined with an adjacent one…

(The only text that varies across the 19 is the per-file rights sentence that follows, which is legitimately file-specific.) Round 20's L1 limb 2 is now fully answered: the field-list addition is credited to Round 19, where it belongs.

But `git show 6fd4973` — the Round 17 fix pass — shows the clause did not begin at Round 18. In `prosper_chronica-minora-1-lat_mommsen1892.txt` and the four other files Round 17 reached, it read:

> Note (**independent review, Round 17**): quotations elsewhere in this header's own Content note are given in **standard/readable spelling**; the file's own OCR carries the usual **letter-level confusions (V/Y, C/G, u/n, and similar)** at some of the same points, so a reader matching a quoted phrase against the file directly should expect minor character-level variants, not a discrepancy in substance.

Two of the current clause's elements are that text, near-verbatim: the "standard/readable spelling" framing, and the `(V/Y, C/G, u/n and similar)` letter-confusion list. Round 18 broadened the clause (word-breaking, the authoritative-body-text sentence, the field list) and wrote it into all nineteen; Round 19 and Round 20 made the two further edits the label now records. The label starts one round late.

This is exactly the reasoning Round 20's L1 and Round 21's L1 both applied — *"the text changed and the label did not"*, then *"the label changed and skipped a round"* — one generation further back, and it matters for the same reason Round 21 gave: the exemplar it cited at Registry line 295 was rewritten away, so **these nineteen file headers are now the only place this clause's history is recorded at all**. For fourteen of the nineteen files the label is right (Round 18 wrote the clause there first); for five it is not.

### L3. The L5 fix corrected row 33's count to "four scholarly-journal reviews" and kept Project MUSE inside the enumeration — sharpening the mislabel the same finding named in terms

Round 21's L5 made two observations about row 33's parenthetical: the count was wrong, and *"one of them, Project MUSE, is a hosting platform rather than a journal."* The fix took the first. Registry row 33 now reads:

> confirmed consistently across **four independent scholarly-journal reviews** (*Journal of Ecclesiastical History*, *Journal of Theological Studies*, *Reviews in Religion & Theology*, **Project MUSE**) and the publisher's own catalogue page (eerdmans.com) — **five sources in total**, matching `lpc_Decision_Log.md`'s own contemporaneous count of the same check…

The arithmetic is now right and matches `lpc_Decision_Log.md` line 138 (*"five sources (four scholarly-journal reviews plus the publisher's own catalogue page)"*) and Doc_02 §3 (which states the same figures and does not enumerate). But the replacement label is **more** specific than the one it replaced — "five independent scholarly reviews" became "four independent **scholarly-journal** reviews" — and Project MUSE is now affirmatively enumerated as one of four scholarly-journal reviews. It is a hosting platform; whatever review was consulted there appeared in some journal, which the row does not name.

Rated LOW rather than COSMETIC because the fix pass had Round 21's sentence in front of it, resolved one of its two limbs, and tightened the other into a sharper assertion in the same clause. Nothing turns on which four instruments were consulted; the fix is either to name the journal the MUSE-hosted review appeared in, or to say "four independent scholarly reviews (three journals plus a MUSE-hosted review)" and stop calling MUSE a journal.

---

## COSMETIC

### C1. The renamed Decision Log heading's replacement for "each finding real defects" now under-claims against the entry's own pattern paragraph

Line 318, as rewritten this pass: *"Doc_02 revision: independent adversarial review rounds against the 2026-09-08 source-integration revision, one dated paragraph appended per round, **most finding real defects, most fixed**…"*. C1 was raised against *"each finding real defects, each fixed"* on the second limb only — two findings the entry records as deliberately unfixed. The pass hedged **both** limbs. The entry's own pattern paragraph, four paragraphs below, states the first limb the other way: *"independent re-verification caught a real, previously-uncaught defect at **every single round** of this specific revision's review."* All seven rounds found real defects; "most" is the one word in the new heading its own body contradicts. "Each finding real defects, most fixed" would carry both facts.

### C2. The Decision Log's new Round 21 paragraph names the wrong pair as "closed exactly"

Line 334: *"…all fifteen of Round 20's own findings are genuinely closed, **two of them (H1, M1's own site) exactly**."* Round 21's own verdict paragraph reads: *"All fifteen of Round 20's findings are genuinely closed, and **the two structural ones** are closed exactly"* — and the two structural findings among Round 20's fifteen are **M1** (bold-marker nesting at Doc_02 line 29) and **C1** (literal asterisks inside a code span at Registry row 42), which Round 21 describes in successive sentences as *"fully closed and independently proved so"* and *"closed with the same completeness."* H1 is a provenance-claim fix, not a structural one. The same class as Round 20's own C5 — a small descriptive slip about a review artifact's own findings text, in this log's summary of it.

### C3. Doc_02 §9 item 3 still folds row 38 into "flagged for priority review per the Registry's own trigger," which the Registry's own trigger rule does not reach

After the L4 fix, item 3 reads: *"Rows **34, 35, and 38** … remain recalled from field knowledge rather than independently re-read this session — **flagged for priority review per the Registry's own trigger**."* Rows 34 and 35 each carry *"**Flagged for priority second-opinion review**"* in their own Verification Notes. **Row 38 does not** — its Verification Note reads only *"Recognized field category …; no specific site report or excavation record identified or verified this session."* And the Registry's own stated rule (line 283, under "Priority second-opinion review flags") is: *"a row is flagged for priority second-opinion review when it is Confidence C or below **and** it licenses a claim this document actually makes (**not merely a non-empty Licensed-For field, which can state a negative**)."* Row 38's Licensed-For states exactly such a negative: *"Not currently licensed for a specific claim."* So the trigger does not fire for it.

The underlying material *is* flagged, twice, elsewhere in Doc_02 (§5's closing sentence and §9 item 2), so no reader is misinformed about the state of the evidence — only about which instrument produces the flag. Third member of the same group-membership shape Round 20's M3 and Round 21's L4 each corrected one member of.

### C4. Doc_02 §3's Lancel bullet keeps "WebSearch-verified this session" while its sibling bullet, edited in the same pass, was given an explicit date

The C3 fix is correct where it landed: the Burns & Jensen bullet now reads *"WebSearch-verified **in a 2026-09-02 post-disposition pass, not this document's own original 2026-09-01 drafting session**."* Round 21's C3 named the Lancel bullet in the same finding as having *"the same shape."* Line 66 still reads *"bibliographic details … **WebSearch-verified this session** and, per two independent journal-review citations, reconfirmed … (Registry row 31's own 2026-09-02 update…)."*

Unlike row 33, row 31's Discovery channel does record a genuine `WebSearch / 2026-09-01`, so "this session" is literally true for Lancel and false only for Burns & Jensen — which is why this is COSMETIC and why the pass's choice is defensible. The residue is presentational: one bullet in a four-bullet block now dates its check explicitly and its neighbour does not, in a section where "this session" has needed disambiguation twice in two rounds.

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**Bold-marker nesting, independently reproduced across all four documents, run-aware.** markdown-it-py 4.2.0 (`commonmark`), **437** `**`-bearing lines. Result: **zero** nested `<strong>` spans, **zero** unclosed spans, **zero** literal `**` surviving any render, **zero** `****`, and **zero** lines where CommonMark's own delimiter pairing differs from the naive sequential pairing of that line's bold delimiters. One implementation note, offered because it matters for whoever runs this test next: a two-character `**` scan reports three false mismatches (Registry lines 26 and 36, Manifest line 69), all of them `***word***` constructions where an italic closes at the same point as the bold. Treating a run of two-or-three asterisks as contributing exactly one bold delimiter removes all three and leaves a clean zero. The class remains closed by construction, and the three lines this pass added are clean.

**Round 19's C1 — spot-checked, undisturbed.** `cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt` line **42582** reads `EPITOMA CHEONICON` (the section half-title, no "DE"); line **45881** reads `EPITOMA DE CHRONICON,` between the praefatio's last line at 45876 (`De reliquis libris quicquam addere supervacaneum est.`) and the chronicle's first entry at 45891 (`1 Adam cum e.sset annorum CCXXX, genuit Setli.`). Identical to what Rounds 19, 20 and 21 each read. The declination stands on four consistent checks.

**M1 (Round 21's) — the recall-test enumeration, at all three sites.** Registry line 325 now reads *"**No round after Round 14 is a further instance of '0/10'** (stated here as a standing rule rather than a per-round enumeration … restated statelessly, Round 21's own M1, after 'Rounds 15 through 19' went one round stale at Round 20 …): per the paragraph above, no round after Round 14 has run the test at all, so none returns any score, '0/10' included."* A grep across all four documents for live per-round enumerations of this fact returns **none** — every remaining "Rounds 15…" string is a historical quotation inside a correction note. Registry line 295, Doc_02 §9 item 6 and line 325 now say the same stateless thing three ways, and none needs a further round's edit.

**M2 (Round 21's) — Registry line 327 against rows 32–35, row by row.** The sentence now reads *"this Registry's own rows for **34 and 35** continue to state that they were not independently checked or bibliographically re-verified via WebSearch this session and remain flagged, which is the right direction **for those two** … — **rows 32 and 33 no longer do** …: each was independently WebSearch-re-verified in its own right on 2026-09-02, and each row's own flag was resolved then."* Checked against the current table: row 34 and row 35 both read *"Recalled from general field knowledge, not independently checked or bibliographically re-verified via WebSearch this session. **Flagged for priority second-opinion review**"* — accurate. Row 32 reads *"Both editions independently confirmed via WebSearch … **Flag resolved**"*. Row 33 reads *"bibliographic details now independently verified via WebSearch … flagged for that [Confidence-letter] decision **rather than for further second-opinion review, which this update has already satisfied**."* The sentence's *"each row's own flag was resolved then"* reads, in its own context, as the second-opinion flag, which is exactly what row 33 says was satisfied; row 33's surviving Confidence-letter flag is a different flag and both Doc_02 §3 and row 33 itself say so. Accurate as written.

**M3 (Round 21's) — the scoping wording, tested against every Scope paragraph.** All seven extracted verbatim this round. Round 15: *"This round is **not** a fifteenth full review … Its brief was to re-derive … only what the 2026-09-08 revision newly asserts"* — the new wording's *"Round 15 by reviewing the revision itself"* is right, and the false *"scoped to verifying the prior round's own fix pass"* is gone from all three sites. Rounds 16 and 17: fix-pass verification plus a fresh read of §1 (R16) and of §1 and §2 (R17) — narrower than whole-document, which is why the new *"Rounds 18 onward also adding a **cold, whole-document** read"* qualifier is accurate rather than merely one round safer. Rounds 18, 19, 20, 21 each state a second brief that is a whole-document read in terms. The Decision Log's own self-contradiction (the pattern paragraph asserting exclusivity four sentences before crediting Round 20 with a full-re-review finding) is gone. And *"none has run either instrument"*: `grep -i "recall\|PRESS"` across Rounds 16–21 returns only discussion *about* the Registry's claim — no ten-item list, no score, no PRESS answer, in any of the six.

**M4 (Round 21's) — row 45's reordering.** The cell now opens *"**Now vendored as row 192 (2026-09-05)** — this row kept as the standing reference…"* with a correction note naming the finding and the reason it escaped twenty rounds, and the surviving Doc_01 reference is now scoped in time (*"Already named in Doc_01 §5 as 'not vendored in this corpus' **as of this row's own original drafting**"*). The reordering itself is exactly right; the rewritten closing sentence is M1 above. A re-run of Round 21's own two-claim cell sweep across all 212 rows now returns one hit, row 40, where the negative is explicitly qualified (*"Not vendored **under this row's own number**"*) and correct.

**L2 and C4 (Round 21's) — the two Manifest markers.** §2's heading is now *"## 2. Resolved: the one item once named here as not yet a confirmed acquisition candidate"* with a correction note modelled on §1's; the section's single item is marked *"**Resolved 2026-09-08**"* and Registry row 41 and Doc_02 §9 item 8 both independently record the same closure. Line 87's new superseding marker names the practice it follows at line 11, line 61 and the §1 heading — all three verified present and all three still at those line numbers, since the pass's own two-line insertion at §2 falls below them. Its factual claim (*"eight of the nine items this paragraph weighs are now closed"*) matches §1's nine fulfilment paragraphs and the closing Status update.

**L3 (Round 21's) — the heading and its cross-document pointer.** `grep "^### 2026-09-08"` returns exactly four entries (lines 281, 291, 304, 318); `grep -c "Doc_02 revision:"` returns **1**. The new heading carries no round numbers, and the entry beneath it holds exactly seven `**Round N**` paragraphs (15 through 21), matching *"one dated paragraph appended per round."* Doc_02 §2's rewritten pointer quotes two strings — `"Doc_02 revision:"` and `"independent adversarial review rounds against the 2026-09-08 source-integration revision"` — both present, both unique, and both stable under a further round's appended paragraph, which is what L3 asked for. (The parenthetical's *"the one beginning …"* is loose — the entry's heading begins with its date, and the quoted phrase begins the subject clause after "Doc_02 revision:" — but it disambiguates correctly and is not counted as a finding.) Doc_02 §9 item 1's separate pointer to *"Network access confirmed working"* still resolves uniquely to line 281.

**L4 (Round 21's) — row 37's regrouping, checked against the row's own columns.** Row 37's Discovery channel reads `Donatism build's own Registry, row 48 / 2026-09-01` and its Verification Note *"**Already vendored on the sibling Donatism build's own branch** … (confirmed here, Round 5's own M9…)"* — inherited, not recalled. Row 36 (Shaw) reads the same way (`Donatism build's own Registry, row 24`), and Doc_02 §10 already pairs the two: *"Relying on the sibling Donatism build's own already-verified Registry entries for Shaw (row 36) and *CIL* VIII (row 37)."* The regrouping is consistent with that, and row 37's own priority flag is still carried at Doc_02 §9 item 2.

**C2 (Round 21's) — the Lancel year.** Doc_02 §3 line 66 now reads *"(French original **1999**; English translation, London: SCM Press, 2002)"*, matching row 31's Source column (*"French original *Saint Augustin*, Paris: Librairie Arthème Fayard, 1999"*) and row 31's own 2026-09-02 update, which records two journal reviews citing the imprint *"from the 1999 French original."*

**Registry table integrity, recomputed row by row.** All 212 rows re-extracted by column position: numbers **1–212 complete, no gap, no duplicate**; **every row exactly 12 pipes / 11 columns**; every row balanced on `**`, parentheses and backticks. Three physical-order inversions, at 48→42, 193→60 and 60→52 — the same three Rounds 20 and 21 found, all covered by the front-matter Disclosed-placement rule, which names "48, 52, 60 among them." Excluded set re-parsed from the Boundary Status column: `{28, 29, 98, 128, 204}`, unchanged; no live document states an Excluded enumeration. Doc_02 §3's `Source_Registry.md` "line 8" pointer is still correct (line 8 is the checkpoint rule; line 6 is the Disclosed-placement rule), and this pass inserted and deleted no Registry lines.

**Census and comparator arithmetic, recomputed across all 56 atlas files.** `latin-pastoral-congregational-christianity.yaml`: **99 entries, 97 distinct titles, `Counter({'tradition': 90, 'context': 9})`, 88 distinct titles inside the tradition set, `Counter({'assigned': 87, 'provisional': 12})`**; exactly two duplicate titles (*The Enchiridion*, *The Passion of the Scillitan Martyrs*), so 90 − 2 = 88 reconciles. Comparators re-derived per measure: 99 raw against **68** (`post-apostolic-house-church.yaml`), 90 `tradition` against **59** (`alexandria-catechetical.yaml` and `post-apostolic-house-church.yaml`, tied). Doc_02 §1's "largest … on every count attempted" holds. The nine `context` entries are Delehaye, Harnack, Monceaux I/II/III, both von Sodens, Prosper and the Codex Theodosianus — **seven of nine modern (1901–1921) secondary scholarship**, exactly as §1 says.

**Primary-source quotations, re-verified at source.** Six of Doc_02's load-bearing quotations checked against the vendored XML directly, markup-stripped, entity-unescaped, whitespace- and apostrophe-normalized: *"by the judgment of God and the favour of the people"*, *"your suffrage and God's judgment"* (in the "ancient venom" passage), *"neither does any of us set himself up as a bishop of bishops"*, *"the condescension of his love had chosen me among his household companions to a voluntary exile"* (all `anf05`); *"from the Council and the epistles of Cyprian, to the effect that Christ's baptism may not be given by the hands of heretics"* and *"who strive to defend themselves by the authority of the most blessed bishop and martyr Cyprian"* (both `npnf104`). **All six present and exact.**

**Doc_02 §2's and §4's Possidius material, checked against the vendored file rather than against the row.** Weiskotten's introduction carries both quotations §2 attributes to it, once each and in the order §2 gives them: *"in all likelihood younger than his teacher and friend"* and *"probably not over thirty, as Augustine was then thirty-five."* The file independently supports §2's surrounding claims — *"In 397, probably within a short time after the death of Megalius, Bishop of Calama and Primate of Numidia, Possidius succeeded to this episcopate"* — and §2's and §4's "close to / nearly forty years" against Possidius's own *"almost forty years."* Round 16's L6 qualification holds at source.

**Cross-references and row citations.** Every row number cited in Doc_02 resolves to an existing Registry row; none falls outside 1–212. Every directional `§N above` / `§N below` reference in Doc_02 direction-checked programmatically: **none fails**.

**Cross-branch claims, checked against this branch's own file tree.** `cic/texts/` holds 88 registered files. The three sibling-Donatism-branch files this Registry names as *not* present here — `cil8-supplementum-numidiae_cagnat-schmidt1894.txt` (row 37), `optatus_libri-vii-critical_ziwsa1893.txt` (row 64), `monceaux_…tome5_1920.txt` (Manifest G5) — are all genuinely absent, so those rows' qualifiers are accurate and Doc_02 §5's *CIL* VIII "not currently vendored" is correct as stated.

**Engine scripts, both re-run this session.** `python cic/engine/texts_registry.py` → **exit 0**, *"OK: every vendored file has a header-verified rights line (public domain, or a recognized open licence), an ENTRIES row, and no ENTRIES row points at a missing file"*; 88 vendored files, 23 non-English, `cic/texts/` at 211 MB (30% of the 700 MB planning trigger). `python cic/engine/corpus_map_merge.py --check` → **exit 0**, 528 works → 788 assignments across 56 Atlas entries, no error.

**The 19 vendored files' diff, bounded.** `git diff efc1a95..f0be10a` touches exactly one line in each of the 19 files, and the change in each is exactly the attribution label. No file's Content note, Source line, Title or rights sentence was altered, and no twentieth file was touched.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the fix pass and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** H1 concerns whether two of this world's own Registry rows agree with this world's own Manifest about this world's own acquisitions. M1 and M2 concern the provenance of one file in this world's own `cic/texts/` intake. C3 concerns how this world describes its own flag trigger. Nothing here decides anything for another world's build thread; the sibling Donatism build's own vendoring state is reported, not reasserted. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing here proposes a change to `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022, or any governing document. M2 is a finding that a header does not match its own source under the intake convention already in force, not a proposal to change that convention. M1 is a finding that one site departs from a discipline (no guessed identifiers) this project has already adopted and states at five other sites. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round disagrees with no prior round on any point of fact, and agrees with Rounds 20 and 21 against Round 19 on C1, reached by reopening the file at the lines named. M1 and M2 are the one place this round could have produced an unresolved tension — a claim in a live document contradicted by four or five others, with no artifact on this branch able to settle it — and it is closed rather than left open, by fetching the archive.org item itself and comparing its own full text against the vendored file at both ends. The identity holds; the "Google Books scan" description does not. Both are now checkable facts, not competing accounts, and neither requires the project lead. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

`Doc_02_Source_Ecology.md`'s status line and §10, and `Source_Registry.md`'s status line, still describe the Round 14 disposition of 2026-09-02, still read "Fourteen independent adversarial review rounds" over the sequence "(Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0)", and still point a reader to "`Doc02_Round1_Review.md` through `Doc02_Round14_Review.md`" — while `Review-Artifacts/` holds twenty-one `Doc02_Round*_Review.md` files before this one, and both documents carry in-text attributions to Rounds 15 through 21 throughout. That is reported here as observed, checkable state, on the same footing Rounds 16 through 21 reported it. Whether and how those lines should change, and what disposition follows from this round's counts, is **not assessed here**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition. This review supplies only the input that rule takes: a finding count and a findings list.

**Observed trend, stated as raw counts only and not otherwise characterized.** Across the eight rounds against this 2026-09-08 revision: Round 15 — 4/6/5/2 (17); Round 16 — 4/5/6/3 (18); Round 17 — 0/3/5/4 (12); Round 18 — 0/4/3/3 (10); Round 19 — 0/2/4/3 (9); Round 20 — 1/4/5/5 (15); Round 21 — 0/4/5/4 (13); Round 22 — 1/2/3/4 (10). Three observations bear on reading this round's counts, stated without weighing them: the single HIGH (H1) and one MEDIUM (M2) both pre-date this revision and both sit on rows or files dated **2026-09-05**, the outside-the-batch shape Round 21's own M4 identified and this round was commissioned to sweep for; the other MEDIUM (M1) is text this fix pass itself wrote while closing that same M4; and the defect class Round 21 closed by construction — bold-marker nesting — returns zero on an independent re-run, the only class in this sequence to have stayed closed without a site-by-site sweep.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 1 HIGH · 2 MEDIUM · 3 LOW · 4 COSMETIC.**
