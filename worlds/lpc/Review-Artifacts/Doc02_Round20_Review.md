# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 20 Independent Adversarial Review — scoped to verifying the Round 19 fix pass (including its one declined finding), plus a cold read of the whole document set

**Documents reviewed (committed state — `git status --porcelain` clean, 0 lines, at `fc18741`, "lpc: fix Round 19 review findings on Doc_02 revision (8 of 9)", 2026-09-08 08:12:31 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `worlds/lpc/Doc_02_Source_Ecology.md` (156 lines; §1 through §10 read in full, cold)
- `Source_Registry.md` (329 lines; all 212 rows re-parsed by column position; the Saturation statement, its fourteen round paragraphs, and the front-matter rules read in full)
- `Source_Acquisition_Manifest.md` (85 lines, read in full — front matter, all nine G-items with their fulfillment paragraphs, §§1–3, and the closing "Decision from the project lead" section)
- `lpc_Decision_Log.md` (334 lines, read in full — every entry, not only the 2026-09-08 ones, since two findings below turn on a 2026-09-02 entry no round in this sequence has checked against Doc_02)
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines), searched for every phrase Doc_02 attributes to or denies of it
- `Review-Artifacts/Doc02_Round15_Review.md` through `Doc02_Round19_Review.md`, read in full and in order before any other file
- All 19 vendored `cic/texts/*.txt` files the fix pass touched, plus `prosper_chronica-minora-1-lat_mommsen1892.txt` opened directly at both cited loci and at its own printed-page markers; `delehaye_…1921`, `vonsoden_prosopographie-…1909`, `cyprian_opera-spuria-vita-pontius-…pars3` and `perpetua-scillitan-martyrs-…robinson1891` checked at specific quoted strings; all 56 atlas files in `cic/corpus-map/`; both engine scripts
- One external artifact fetched live and read directly: `archive.org` item `histoirelittra00moncuoft`, opened at its own title page (M2 below)

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-08 vendoring, did not write the Round 15, 16, 17, 18 or 19 fix passes, and did not write Rounds 1–19.

**Scope, stated plainly.** Three briefs, run together. First: verify, independently and against primary artifacts, whether each of the eight Round 19 findings the `fc18741` pass says it fixed (M1, M2, L1–L4, C2, C3) is actually closed — and, since every one of the five preceding fix passes introduced or left at least one new checkable error while fixing what it targeted, look specifically for that shape here. Second: independently re-adjudicate the one Round 19 finding the pass **declined** (C1, the Prosper title quotation), by opening the file at both cited locations and at its own page markers, rather than accepting either the review's assertion or the fix pass's rebuttal. Third: a cold, whole-document sweep for bold-marker *nesting* (not parity) across every line of all four documents, for Registry table integrity, and for staleness or internal contradiction no prior round happened to check — in particular the cross-document consistency of Doc_02 §3 against the Registry rows it summarises, which no round in this sequence appears to have run. Rounds 15–19 were treated as claims to re-derive, not as authority; so was the fix pass's own commit message.

**Method — what was actually re-derived, not trusted.** A CommonMark render (markdown-it-py 4.2.0, `commonmark` preset) of **every** line of all four documents, with the resulting `<strong>` tree compared against the author-intended pairing and scanned for nested or unclosed spans and for literal `**` surviving the render — the check Round 19's own L3 established a parity count cannot perform. A fresh regex parser over all 212 Registry rows extracting each column by position, with per-row pipe, `**`, parenthesis and backtick balance, plus a full row-number sequence and physical-order check. `yaml.safe_load` across all 56 atlas files in `cic/corpus-map/`, recomputing entry counts, distinct titles, roles, confidences and every comparator Doc_02 §1 states. Direct reads of `cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt` at lines 42570–42600, 45790–45900 and 54190–54580, plus its own printed-page running heads at 45348, 45493, 45802, 45944 and 46110, and its consular-year headings at 54201, 54489 and 54625. Direct string checks of every quotation the two new Registry per-row disclosures and the Decision Log's own C1 paragraph make against the files they name. A live fetch of `histoirelittra00moncuoft`'s own `_djvu.txt` from the archive.org node, read at its title page. A programmatic diff of the OCR clause across all 19 vendored files. Both engine scripts re-run. Nothing was carried forward from Rounds 15–19's tables, from `lpc_Decision_Log.md`, or from the `fc18741` commit message.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 1 HIGH · 4 MEDIUM · 5 LOW · 5 COSMETIC.**

**The declined finding was declined correctly, and this round says so plainly.** Round 19's C1 does not survive independent re-verification, exactly as the fix pass concluded and for exactly the reason it gave. The Prosper volume carries two distinct title headings: a section half-title at lines 42580–42585 reading `PROSPERI TIRONIS / EPITOMA CHEONICON` with no `DE` (the one Round 19 read), and a second at lines 45879–45888 reading `PROSPERI TIRONIS / EPITOMA DE CHRONICON,` — with `DE` — which sits between the file's own printed-page marker for p. 384 (line 45802) and its own running head for p. 386 (line 45944), i.e. **on printed p. 385**, precisely where the Content note says the work "begins." The Content note's quotation is accurate; applying Round 19's C1 would have replaced a correct quotation with an incorrect one. The fix pass's reasoning, its two line ranges, and its account of what sits immediately before and after the second heading were each re-derived here from the file and all hold.

**Seven of the eight applied fixes are also genuinely closed, and two of them are exact.** M1's two limbs are both correctly discharged and the new "Rounds 15 through 19 … did NOT run" claim was independently checked against all five artifacts rather than adopted (Round 15 discloses its non-run in terms; Rounds 16 and 17 contain the word "recall" zero times; Rounds 18 and 19 contain it only inside findings *about* the Registry's claim — no score, no ten-item list, no PRESS answer in any of the five). L2's past-tense repair reached rows 56, 89 and 99 and now matches rows 41, 78 and 90 word for word. C3's two new per-row disclosures name real OCR readings verified at the exact lines (`iiiilgo` at line 40260 of the Pars III file; `xvI` at line 7375 of the Robinson file). L1's clause is byte-identical across all nineteen files, present exactly once in each, with no old clause stacked beneath. L4's two counts are now right against a direct recount of `Doc02_Round18_Review.md`'s own ten `### ` headers. Registry integrity is intact: 212 rows, numbers 1–212 with no gap and no duplicate, every row at exactly 12 pipes, balanced parentheses and backticks on every line of all four documents. Both engine scripts exit 0. Every census figure Doc_02 §1 states — 99 / 97 / 90 / 88 / 87 / 12, against comparators 68 and 59 — recomputes to the digit from raw YAML.

**The recurrence has not stopped; it has moved to the two places this pass did not look.** One finding is the fix pass writing a new, checkably false claim into a live document (H1) — and it is false in the same way, and in nearly the same words, as a claim already standing uncaught in Doc_02 §9 item 1, which the pass copied rather than checked. Two are the pass's own defect class recurring at a site the pass did not sweep: the identical bold-nesting defect L3 was written to fix, four lines away in the same section and half again as large (M1), and a corrected-away archive.org identifier still standing in the very row the pass edited (M2). Two are pre-existing and previously uncaught, surfaced only by this round's cold read: a three-way contradiction between Doc_02 §3 and Registry rows 31–33 dating from a logged 2026-09-02 post-disposition edit (M3), and a Decision Log entry heading that has misstated its own scope since the Round 17 fix pass and which this pass has now made load-bearing by quoting it (M4). The rest are counts, scopes and conventions in newly-written correction text.

---

## HIGH

### H1. The new Manifest superseding note credits this build thread with fetching G3 and G1 that the project lead supplied himself — false against the same document's own G1 and G3 fulfillment paragraphs, its own §1 superseding note, and its own closing status update, all three of which get it right

`Source_Acquisition_Manifest.md` line 11, the sentence written this pass to discharge Round 19's M2:

> **Superseded 2026-09-08 (corrected here, independent review Round 19's own M2, …): with network access confirmed working the same day (§1 below), eight of these nine candidates (G1, G2, G3, G5, G6, G7, G8, G9) were fetched, opened, and independently verified directly by this build thread rather than requiring Mark's own manual download — no acquisition decision remains for him to make on any of those eight.**

The *closure* half of that sentence is right. The *provenance* half is false for two of the eight it names, and the falsity is not marginal — it inverts who did the work:

- **G3 was supplied by the project lead in full, and closed three days before network access existed.** The Manifest's own G3 fulfillment paragraph, line 29: *"**Fulfilled 2026-09-05.** The project lead supplied a compiled docx of exactly this Weiskotten edition, from an archive.org 'Full text' view (exact item identifier not stated when supplied)."* `lpc_Decision_Log.md`'s own 2026-09-05 G3 entry (line 232) is more explicit still: network access was *"re-checked and re-confirmed blocked at the infrastructure level — this time verified two ways… a `403` policy denial at the gateway for `archive.org:443`… The project lead then downloaded and supplied the file himself."* Nothing about G3 was fetched by this build thread.
- **G1's larger part was likewise supplied by him.** Manifest line 21: *"**Fulfilled 2026-09-05 for Pars I and II.** The project lead supplied a compiled docx covering both Pars I (the treatises) and Pars II (*Epistulae* I–LXXXI) in one file."* Only Pars III was fetched directly, on 2026-09-08.

The Manifest's own two other superseding notes both state this correctly, and both were certified by Round 15:

- Line 59: *"Consequence: **G1's remaining Pars III**, G2, G5, G6, G7, G8, and G9 were all fetched, opened, and independently verified directly by this build thread rather than requiring the project lead's own manual download."* Seven items, G1 narrowed to Pars III, G3 absent.
- Line 85: *"this build thread fetched, opened, and independently verified **G1's remaining Pars III**, G2, G5, G6, G7, G8, and G9 directly… **G3 was already fulfilled in full 2026-09-05.**"*

So the new front-matter note contradicts the same document at two places, in the direction of over-claiming for the build thread. The "with network access confirmed working the same day" framing compounds it: G3 and G1 Pars I–II closed on 2026-09-05, under a block the Decision Log records as confirmed present on that date.

**This is not an error the pass invented from nothing — it is one it copied without checking.** `Doc_02_Source_Ecology.md` §9 item 1 (line 131) already reads:

> eight of the nine are now closed on their own public-domain footing, **independently fetched and verified directly rather than requiring the project lead's own manual download**: G1 (Hartel's CSEL 3, complete, rows 191 and 194), G2 …, **G3 (Possidius's *Vita Augustini*, row 192, closed 2026-09-05)**, …

`git log -S "independently fetched and verified directly"` on Doc_02 returns exactly one commit, `c803529` — the 2026-09-08 vendoring revision itself. The claim has therefore stood uncaught through Rounds 15, 16, 17, 18 and 19 (Round 19's M2 quoted §9 item 1 for its *closure* statement and did not test the provenance predicate), and this fix pass has now propagated it into a second live document instead of catching it. The §9 item 1 sentence is self-contradicting on its face — it parenthesises "closed 2026-09-05" onto an item it has just said did not require the project lead's manual download.

Rated HIGH rather than MEDIUM for three reasons. It is a substantive factual claim, not a count or a pointer. It sits in the first substantive paragraph of the document addressed by name to the project lead in his operational acquisition role, and it tells him something about his own actions that is not true. And it runs against CO-022's attribution discipline from the unusual direction: this build's standing rule is that nothing may be *attributed* to the project lead without a verifiable record, and the mirror-image obligation — not to reassign to the build thread work he verifiably did — is the same rule's other half. Both sites need correcting; the Manifest's own line-59 and line-85 wording is the model, and it is already in the file.

---

## MEDIUM

### M1. The identical bold-nesting defect L3 was written to fix is still live four lines away in the same section, half again as large — and the fix pass re-verified using the parity check Round 19 had just demonstrated cannot detect it

The L3 fix at Doc_02 line 25 is correct: rendered through a CommonMark parser this session, that banner now produces four sibling `<strong>` spans, each closing at its own colon, with every explanatory sentence plain. Verified span by span.

Doc_02 **line 29**, in the same §1, was not checked. It carries eight `**` delimiters at offsets 0, 1596, 2588, 2838, 3253, 3881, 4045 and 4799. Parity passes. CommonMark does not pair them as written:

```
<strong> Original-language witnesses …                       (0 → 1596)   correct
<strong> Two of these are the Maurist text …                 (2588 → 2838) correct
<strong> Every one of these is a second witness …            (3253 → 4799) WRONG
   <strong> Corrected here (… Round 16, its own M4) …        (3881 → 4045) nested
```

The delimiter at 3881 is preceded by a space, so it cannot close; it opens a **nested** strong instead. The result, confirmed by walking the rendered tag sequence, is that the outer span runs **1,544 characters** — from "Every one of these is a second witness" all the way to "not supplying content with no English counterpart at all." Two passages the document's own convention requires to be plain render bold inside it:

- **190 characters:** *"the Acta Proconsularia (inside row 194) has no English translation vendored anywhere in this corpus — real, new, citable content on that basis, not merely a check on an existing rendering."*
- **752 characters:** *"no complete English translation of the Retractationes is vendored, but substantial excerpts are, quoted inside NPNF's own editorial apparatus — the passage this document's own §2 below quotes … Row 209's own real value is what its own Licensed-For column states precisely — closing a citation this document previously held only at that second hand…"*

That is 942 characters rendering bold that should be plain, against the ~630 Round 19's own L3 measured at line 25 — a larger instance of the same defect, in the same section, four lines below the one just fixed.

**Traced rather than assumed.** The eight-delimiter structure of line 29 is present at `0f7ca8a` (Round 16 fix pass), `6fd4973`, `5f8625f` and `fc18741` alike — pre-existing, introduced when the Round 16 M4 correction banner was appended inside the Round 15 M4 banner rather than after it, exactly the construction Round 19 diagnosed at line 25. Rounds 17, 18 and 19 did not catch it; Round 19 rendered one line, not every line.

What makes this MEDIUM rather than another LOW markup note is the verification claim attached to the pass. Round 19's L3 said, in terms: *"The line balances on a naive even/odd test — which is why the standard parity check this project runs passes on it… This one it cannot [catch], because the count is even."* The `fc18741` commit message answers: *"All four documents re-verified clean: **even bold-marker counts**, balanced parens/backticks, 12-pipe registry rows."* The pass re-ran the one check it had just been told is insufficient for this defect class, and reported the document clean on that basis while a bigger instance sat four lines from the fix.

A full nesting sweep of all four documents (below, under "What was checked and found clean") returns exactly one further anomaly, at Registry row 42, recorded at C1.

### M2. Registry row 56 still offers `histoirelittra00moncuoft` as evidence that Monceaux vols. I–III are freely hosted — independently re-fetched this round and confirmed to be Tome Cinquième (1920) — in the row this fix pass edited

`Source_Registry.md` row 56 (line 70), unchanged by this pass except at its closing clause:

> **Rights position resolved, not hedged:** Monceaux died in 1941; vols. I–III (1901–05) are public domain on their own imprint dates alone… and **are freely hosted at the Internet Archive (`histoirelittra00moncuoft`, `histoirelitterai03monc_0`)** and Gallica (`bpt6k141717k`)

`histoirelittra00moncuoft` does not host any of vols. I–III. Fetched live this round from the archive.org node and read at its own title page:

```
PAUL  MONCEAUX
…
TOME   CINQUIÈME
SAINT    OPTAT
ET    LES    PREMIERS
ÉCRIVAINS    DONATISTES
PARIS
ÉDITIONS    ERNEST    LEROUX
1920
```

That is Tome V, 1920 — the volume already vendored on the sibling Donatism branch, and not part of G5's request at all. This is not a new discovery: the same build session established it on 2026-09-08 and recorded it in three other places. `Source_Acquisition_Manifest.md` G5's fulfillment paragraph (line 39): *"this build thread independently opened `histoirelittra00moncuoft` directly and found it is **not** Tome Premier at all — its own title page reads 'TOME CINQUIÈME / SAINT OPTAT ET LES PREMIERS ÉCRIVAINS DONATISTES,' 1920… That lead is corrected here rather than used."* Registry **row 206** carries the same correction in its own Verification Note. The vendored file `monceaux_…tome1_1901.txt` carries it in its own `Source:` line. `lpc_Decision_Log.md` line 310 carries it.

Row 56 is the one place that did not get it — and row 56 is where the Manifest's own G5 entry points a reader ("Registry row 56"), and where the identifier is doing live evidentiary work, supporting the rights determination that raised this row from Confidence C to B. The correct identifiers for the volumes the sentence is about (`histoirelittra01moncuoft`, `histoirelittra02moncuoft`) appear nowhere in the row.

The fix pass edited this exact cell — L2's past-tense repair rewrote its closing clause and added a Round 19 correction note — without the identifier three sentences earlier being checked. Same shape as Round 18's L1 and Round 19's L2: one clause in a cell repaired, another left.

*(Not part of this finding, checked separately: `histoirelitterai03monc_0` is genuinely Tome III, and rows 206–208 all name correct, independently verified identifiers.)*

### M3. Doc_02 §3 and §9 item 3 contradict Registry rows 31, 32 and 33 on those rows' verification state — three sites, all pointing the same way, standing since a logged 2026-09-02 post-disposition edit that was never propagated to Doc_02

`lpc_Decision_Log.md`'s 2026-09-02 entry "First three post-disposition `Source_Registry.md` edits" records that WebSearch resolved all three self-flagged bibliographic questions and says the edits are "disclosed here per the same post-disposition-edit practice." It does not say Doc_02 was checked against them, and it was not. The Registry rows and Doc_02 §3 now say opposite things:

| | `Source_Registry.md` row | `Doc_02_Source_Ecology.md` §3 |
|---|---|---|
| **Lancel (31)** | *"**2026-09-02 update:** the English publication year previously flagged for priority second-opinion review is now confirmed… **Flag resolved**; translator name added"* | line 66: *"bibliographic details WebSearch-verified this session from a review summary rather than a library catalogue, and **flagged for priority second-opinion review on the exact English publication year**"* |
| **Burns, *Cyprian the Bishop* (32)** | *"**2026-09-02 update:** the year previously flagged… is now resolved… hardback 2001 / paperback 2002… **Flag resolved**"* | line 67: *"publisher and title WebSearch-verified, **publication year recalled from field knowledge and flagged for priority second-opinion review**"* |
| **Burns & Jensen (33)** | *"**2026-09-02 update:** bibliographic details now independently verified via WebSearch — publisher, city, and year confirmed consistently across five independent scholarly reviews… and the publisher's own catalogue page… flagged for that [Confidence] decision **rather than for further second-opinion review, which this update has already satisfied**"* | line 68: *"recalled from general field knowledge **rather than independently checked or WebSearch-verified this session**. **Flagged for priority second-opinion review** before it supports any specific claim"* |

The row-33 pair is a direct contradiction in both halves: Doc_02 says the work was not WebSearch-verified, the Registry says it was, across five named sources; Doc_02 flags it for second-opinion review, the Registry says that review is already satisfied.

A fourth site carries the same drift. Doc_02 §9 item 3 (line 133) sorts the rows into two groups — *"Rows **33**–35, 37, and 38 … remain recalled from field knowledge rather than independently re-read this session"* versus *"Rows 30–32 … are bibliographically WebSearch-verified but not independently re-read"* — while row 33's own note says in terms that it now *"matches rows 30/31/32's WebSearch-verified-but-not-independently-read pattern."* Row 33 is in the wrong group by the Registry's own words.

This is the same defect class Round 18 rated MEDIUM at its own M3 and M4 (a live artifact stating a verification state its own companion has already superseded), at three rows rather than two files, and in the section of Doc_02 that is its whole account of its secondary scholarship. Nothing here changes a Confidence letter — the Registry deliberately did not self-apply that, and this finding does not ask for it either; only the description of what has been checked needs to agree across the two documents.

### M4. The C2 fix disambiguated Doc_02's Decision Log pointer by quoting a heading that misstates its own entry's scope — the entry titled "Rounds 15 and 16 … two independent adversarial review rounds" now records five

The C2 fix is correctly aimed: Doc_02 §2 (line 54) now reads

> see `lpc_Decision_Log.md`'s 2026-09-08 **"Doc_02 revision, Rounds 15 and 16"** entry — disambiguated here, independent review Round 19's own C2, from the four entries this Decision Log dates 2026-09-08 — for the fuller record of what each round found

and the quoted string does match the head of the target entry. Confirmed: `grep "^### "` returns exactly four 2026-09-08 entries (lines 281, 291, 304, 318), and 318 is the right one.

But the heading it now quotes is itself wrong about its own contents. Line 318, in full:

> ### 2026-09-08 — Doc_02 revision, Rounds 15 and 16: **two** independent adversarial review rounds against the 2026-09-08 source-integration revision, both finding real defects, both fixed

That entry now carries five round paragraphs — Round 15 and Round 16 (line 322 and 324), Round 17 (326), Round 18 (328) and, added by this pass, Round 19 (330). The Round 17 fix pass appended to it without renaming; so did Round 18's; so did this one. A reader using this log's own headings as its index — which is what the log's own retired-directional-pointers rule directs them to do, and what Doc_01's status line calls "the authoritative, append-only record" — finds no entry recording Rounds 17, 18 or 19 at all.

That was a latent defect before this pass. It is load-bearing now: Doc_02's cure for an ambiguous pointer is to name the entry by its title, and the title it names promises two rounds where the reader needs five. The disambiguation therefore only half-works — a reader looking for "the fuller record of what each round found" is sent to an entry whose own heading says it is not that record.

---

## LOW

### L1. The broadened OCR clause's governing phrase still excludes the field its own new parenthetical adds — and the whole clause is still attributed to Round 18, though its current wording is Round 19's

The L1 fix landed cleanly at the mechanical level: all 19 files, exactly one occurrence each, byte-identical text, no old clause anywhere (`grep` for the Round 17 wordings returns zero across `cic/texts/`). The clause now reads, in all nineteen:

> Note (independent review, Round 18): quotations **elsewhere in this header** (Content note, Source line, Title, **or this Provenance note itself**) are given in standard/readable spelling for legibility…

The parenthetical now names the field the clause sits in — which is what Round 19's L1 asked for — but the phrase the parenthetical is glossing was not adjusted with it. "Elsewhere in this header" means *other than here*; "this Provenance note itself" is *here*. A reader who takes the governing phrase as controlling still finds the five files' Provenance-note quotations excluded; a reader who takes the parenthetical as controlling finds the governing phrase wrong. The one-word fix is available ("quotations in this header (Content note, Source line, Title, or this Provenance note itself)"), and this is the same defect Round 19 found, one layer in.

Second limb: the clause's own attribution. Its label reads "(independent review, Round 18)" in all nineteen files, but its current field list is Round 19's edit. This document set's established practice when a later round modifies existing correction text is to stack the attribution — Doc_02 §1's own banner now carries three ("Round 17 … Round 18 … Round 19"), and Registry row 78 carries two — and the Round 18 pass itself replaced the Round 17 clause outright and relabelled it. Here the text changed and the label did not, so nineteen files now attribute Round 19 wording to Round 18. Registry line 295's parallel note gets this right ("Corrected here (independent review, Round 18; **extended, Round 19**)"), which makes the file headers the outlier rather than the convention.

### L2. `lpc_Decision_Log.md`'s pattern paragraph still says "three consecutive rounds" — the same pass updated every other count in that paragraph, and the figure resolves under no grouping

Line 332, rewritten this pass to add Round 19:

> …independent re-verification caught a real, previously-uncaught defect at every single round of this specific revision's review, including **three consecutive rounds** whose own job was **only** to verify the previous round's fixes.

Everything else in that paragraph was brought forward. "Rounds 17 and 18 both introduced no HIGH-severity regression" became "Rounds 17, 18, and 19 all"; "(18 → 12 → 10)" became "(18 → 12 → 10 → 9)"; a full clause on Round 19's own finding shape was inserted. "Three" was left.

Counted from the artifacts' own scope paragraphs rather than inferred:

- `Doc02_Round16_Review.md`: *"This round is **not** a sixteenth full review… Its brief was to verify…"* — verification only.
- `Doc02_Round17_Review.md`: *"This round's brief was to verify…"* — verification only.
- `Doc02_Round18_Review.md`: *"**Two briefs, run together.** First: verify… Second: a cold, whole-document read…"*
- `Doc02_Round19_Review.md`: *"**Two briefs, run together.** First: verify… Second: a cold, whole-document read…"*

So under the sentence's own word "only," the answer is **two** (Rounds 16 and 17). Under the looser reading — rounds commissioned to verify the previous fix pass — it is **four** (16 through 19). "Three" was the right answer for the looser reading at the moment the sentence was written, one round ago, and is now the answer to neither question. This is the fifth consecutive round in which this Decision Log entry's own arithmetic is wrong somewhere, and the second consecutive round in which the wrong figure sits in a paragraph the same pass otherwise updated in full.

### L3. The recall-test correction was closed by extending a per-round enumeration — the form this Registry's own Round-8 remedy exists to retire, stated two clauses later in the same paragraph

`Source_Registry.md` line 295 now reads, correctly on its facts:

> **Corrected here (independent review, Round 18; extended, Round 19): Rounds 15 through 19 … did NOT run a fresh recall test or PRESS question…** *(A running count of how many times was stated here through Round 8's own fix pass; **dropped at that point rather than incremented an eighth time**, on the same reasoning Round 8's own M1 applied to this Registry's row count — the round-by-round record immediately below states exactly how many, each one dated and titled, **without a separate number here that the next round would need to update again**.)*

The paragraph closes by explaining why this Registry stopped maintaining a figure that a later round would have to update — and opens with a figure a later round will have to update. The enumeration has now gone stale twice in two rounds: Round 18's fix wrote "Rounds 15, 16 and 17" and Round 19 found it one short; Round 19's fix wrote "Rounds 15 through 19" and this round is already outside it, having run no recall test either. Doc_02 §9 item 6 (line 136) carries the same enumeration and inherits the same property.

A stateless formulation is available and matches the Registry's own established remedy exactly — "no round after Round 14 has run either instrument; the round-by-round record below is the authoritative list of the rounds that did" — which stays true without a per-round edit. Rated LOW because the current text is factually correct today; it is the chosen form, not the facts, that is the defect, and the form is one this document has already ruled against in writing.

### L4. The Decision Log's own C1 adjudication quotes the Prosper file in normalized form while saying "the file reads" and "exactly as quoted" — the same defect the same pass was fixing at Registry rows 194 and 204

Line 330's C1 paragraph, the passage that carries the whole weight of declining Round 19's finding:

> at that location (the file's own lines 45879–45888, immediately following the preface's own closing line and immediately preceding the chronicle's own first entry, **"Adam cum esset annorum CCXXX"**) **the file reads** "PROSPERI TIRONIS / EPITOMA DE CHRONICON, / **QUIBUS** ET GENERATIONES…" — "DE" present, **exactly as quoted**.

Checked at the lines it names:

- Line 45883 reads `QITIBUS ET GENERATIONES AB ADAM USQUE AD ABRAHAM ET A PAS-`. Not `QUIBUS`.
- Line 45891 reads `1 Adam cum e.sset annorum CCXXX, genuit Setli.` Not `Adam cum esset annorum CCXXX`.

The load-bearing word — `DE`, at line 45881 — is exactly as the paragraph says, and the finding's conclusion is right (see the verdict above). But the two supporting quotations are silently normalized and presented with an explicit literal frame ("the file reads"), in the same clause that says "exactly as quoted," in a paragraph whose entire subject is whether a quotation matches its file. The same fix pass added per-row disclosures to Registry rows 194 and 204 for exactly this — quoting OCR in normalized rather than literal form without saying so — and did not apply the standard to the paragraph it was writing at the same time. `lpc_Decision_Log.md` has no header-level OCR-disclosure convention of its own, so the corrective here is the same per-site note the Registry rows received.

### L5. `Source_Acquisition_Manifest.md` §1's heading still reads "OPEN requests … real acquisition candidates" over a list in which eight of nine are closed — four lines below the paragraph the M2 fix corrected for saying exactly that

Manifest line 15:

> ## 1. OPEN requests — public domain, real acquisition candidates

Round 19's M2 was that the front matter still told the project lead all nine G-items awaited his decision. The fix corrected the Disposition paragraph at line 11. The section heading four lines below makes the same assertion in three words, over a section in which G1, G2, G3, G5, G6, G7, G8 and G9 each carry a dated "Fulfilled" paragraph and only G4 remains open (for CSEL 58's praefatio and indices).

This Manifest treats stale headings as real defects and has corrected two already on exactly this reasoning: §3's heading at Round 3's L2 and again at Round 6's C3, and the "Decision from the project lead" heading at Round 6's L9 — *"this section governed a single request when first written and is renamed now that it governs nine."* The same reasoning applies here in the opposite direction. Rated LOW rather than COSMETIC because it is a section heading, because it contradicts the closure the same document now states in four places, and because it is the nearest unswept site to the one the fix pass did reach.

---

## COSMETIC

### C1. Registry row 42 puts bold markers inside a code span, so the asterisks render literally — the only one of the table's 33 `confidence:` code spans that does

`Source_Registry.md` line 56 (row 42), Verification Notes column:

> Corpus map `role: tradition`, `` `confidence: **provisional**` ``

Rendered through CommonMark, this is the one line in all four documents where a literal `**` survives into output: `<code>confidence: **provisional**</code>`. A reader sees the asterisks. Counted directly, the table carries 26 `` `confidence: assigned` `` and 6 `` `confidence: provisional` `` code spans with no markers inside them, and this one with them — so the convention is unambiguous and this is the single exception. `git log -S` puts it in `4796ee3`, the Round 1 fix pass; nineteen rounds have passed over it because a parity count and a backtick count both accept it. Nothing depends on it.

### C2. Doc_02 §9 item 1's same-date Decision Log pointer is still ambiguous — the second of the two sites Round 19's own C2 named

Round 19's C2 closed with: *"(§9 item 1's '`lpc_Decision_Log.md`, 2026-09-08 entry' carries the same ambiguity and is pre-existing.)"* Line 131 still reads *"With this build session's own network access confirmed working for the first time (`lpc_Decision_Log.md`, **2026-09-08 entry**)…"*, and four entries carry that date. The one it means is "Network access confirmed working; this build's own prior blocker resolved" (line 281) — a *different* entry from the one §2's fix names, so the two pointers cannot be disambiguated by the same phrase. Same one-site-at-a-time shape as L2 above and as Round 19's own L2, at a site the review had already named in the finding text.

### C3. The two new per-row OCR disclosures each name one of the two normalizations in the string they quote

Both new disclosures are accurate about the reading they name, verified at the exact lines. Both quoted strings contain a second normalization that goes unmentioned:

- **Row 204** quotes *"Praesente bis et Claudiano consulibus, XVI Kalendas **Augustas**…"* and discloses only `xvI` for `XVI`. The file (lines 7375–7376) reads `consulibus, xvI Kalendas Augus-` / `tas,` — a hyphenated line break inside the quoted range, the very word-break class Round 18's C2 existed to get covered.
- **Row 194** quotes *"VITA CAECILII CYPRIANI (Pontio diacono **uulgo** adscripta)"* and discloses only `iiiilgo` for `uulgo`. The file carries the heading across two lines (40258 and 40260) with a closing period the quotation drops.

Both are covered in substance by the vendored files' own header clause, which each row's disclosure invokes ("of the same kind the vendored file's own header disclosure covers"), so nothing is left undisclosed in effect. But each row's own sentence names a single reading with "at this exact word," which reads as exhaustive for the string it quotes and is not.

### C4. The new Manifest superseding note bolds its whole body, where the Manifest's own two sibling superseding notes bold only their labels

Measured from the rendered output: the new note at line 11 is a single `<strong>` span of 948 characters — 57% of the paragraph. Its two models are line 59 (*"**Superseded 2026-09-08: network access confirmed working.** Direct WebFetch and curl tests…"*) at 56 bold characters, 7% of its paragraph, and line 85 (*"**Status update, 2026-09-08: eight of nine…**"*) at 188 bold characters across two spans, 13%. Both bold a label and leave the explanation plain — the same convention Round 19's L3 identified as this document set's uniform practice, and the convention the new note's own §1 sibling is cited as following.

### C5. Two small descriptive slips in newly-written correction text

- `lpc_Decision_Log.md` line 330 describes M1's second limb as a sentence that *"continued to describe **Rounds 3–14** (in fact only Round 2 differed)."* The sentence it corrected read *"the recall score has returned 0/10 in every round except Round 2"*, which describes **Rounds 1 and 3–14** — thirteen rounds, not twelve. Round 1's own paragraph in the same Saturation statement records `0/10`. Registry line 325's own replacement gets the scope right ("across the fourteen rounds that actually ran the test (Rounds 1–14)"), so only the log's description of it is off.
- Doc_02 §9 item 6 describes this pass's edit as *"extended, Round 19, **to add Round 18 itself**, which Round 18's own correction had left off this list."* The list in fact went from "Rounds 15–17" to "Rounds 15–19" — it gained Round 18 **and** Round 19. The correction note names one of the two rounds it added.

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**The C1 disagreement — re-adjudicated from the file, not from either party's account of it. The fix pass is right.** This was the round's second brief and the answer is unambiguous on the artifact.

1. *Round 19's location is real and reads as Round 19 says.* Lines 42580–42585: `PROSPERI TIRONIS` / `EPITOMA CHEONICON` / `EDITA PRIMVM A. CCCCXXXIII` / `CONTINVATA AD A. CCCCLV`. No `DE`. Round 19 quoted it exactly.
2. *The fix pass's location is also real, and reads as the fix pass says.* Lines 45879–45888: `PROSPERI TIRONIS` (45879) / `EPITOMA DE CHRONICON,` (45881) / `QITIBUS ET GENERATIONES AB ADAM USQUE AD ABRAHAM…` (45883–45888). `DE` present at line 45881.
3. *They are the only two.* A full-file scan for `EPITOMA`/`EPITOME` in heading position returns the half-title at 42582, the `DE`-bearing incipit at 45881, and thereafter only running heads (`EPITOMA CHRONICON. 345`, `… 347`, and so on) and the volume's own contents entries. `grep -c "EPITOMA DE CHRONICON"` returns 2 — the header's Content note and line 45881. The volume genuinely carries two title headings, exactly as the fix pass says.
4. *The Content note's own locator decides between them, and it points at the second.* The note says the work "begins at the printed volume's **p. 385** with its own full title." The file's printed-page markers around the second heading: `884` (OCR of 384) at line 45802, then the title block at 45879–45888, then `380` (OCR of 386) at 45944, then `388` at 46110 — and, walking back, `382` at 45493 and `380` at 45348. The title block sits between the marks for 384 and 386, i.e. on p. 385. The first heading sits before the running head `344 PROSPERI TIRONIS` at line 42756, inside the preface the same note dates to pp. 341–384. Both halves of the Content note's own sentence check out.
5. *The surrounding structure is as described.* Line 45876 is the praefatio's last line (`De reliquis libris quicquam addere supervacaneum est.`); line 45891 is the chronicle's first entry (`1 Adam cum e.sset annorum CCXXX, genuit Setli.`). Nothing else intervenes.

**Conclusion: applying Round 19's C1 would have introduced an error.** The fix pass's decision to decline it, and its stated reasoning, are both correct. The only defect in the handling is the two normalized quotations in the log paragraph itself (L4 above), which does not touch the conclusion.

**The Prosper file's remaining Content-note claims, checked while there.** The Augustine-death entry is at line 54206 (`Aurelius Augustinus episcopus per omnia cxcellentissimus / moritur Y. kl. Sept., libris luliani inter impetus obsidentium…`) under the consular heading `Theodosio XIII et yalentiniano III. a. -130` (line 54201, OCR of 430) — the printed year 430, as claimed. The Vandal-Carthage entry is at lines 54558–54561 (`Gisiricus, de cuius amicitia nihil mctucbatur, |XIIII kal. Nov.j Carthagineni dolo pacis iiivadit omiiesque opes eius…`), sitting between `Theodosio XVII et Festo. a. 439` (line 54489) and `Valcntiniano Aug. V ct Anatolio. a. 440` (line 54625) — the printed year 439, as claimed. Both quotations are normalized in the ordinary way the header's own clause covers. The Liber Genealogus is a distinct text at line 1484ff, as the header warns.

**M1 — the recall-test correction, both limbs, re-derived against all five artifacts rather than adopted.** Limb 1: Registry line 295 and Doc_02 §9 item 6 both now say Rounds 15 **through 19**. Checked independently for each round rather than accepting the enumeration: `Doc02_Round15_Review.md` discloses its own non-run in terms (*"No fresh ten-item relative-recall test and no PRESS question were run this round"*); `Doc02_Round16_Review.md` and `Doc02_Round17_Review.md` contain the string "recall" **zero** times; `Doc02_Round18_Review.md`'s and `Doc02_Round19_Review.md`'s occurrences are all inside their own M4/M1 findings, quoting or analysing the Registry's claim. No score, no ten-item list and no PRESS answer appears in any of the five. The new sub-claim *"Round 15 disclosed this explicitly in its own artifact; Rounds 16 through 19 continued the same scoping without repeating the disclosure"* is exact on both halves. Limb 2: line 325 now reads *"across the fourteen rounds that actually ran the test (Rounds 1–14), the recall score returned 0/10 in every round except Round 2 (3/10…)"* with an appended Round 19 correction note; counted directly from the section it points into, the round-by-round record runs `*Round 1*` through `*Round 14*` and carries exactly fourteen scores — thirteen `0/10` and Round 2's `3/10`. The unqualified universal is gone. **Both limbs correct and complete.**

**L2 — the past-tense repair, checked at all six rows rather than the three that changed.** Rows 56, 89 and 99 now match rows 41, 78 and 90 in construction and in attribution. Row 89: *"**Was** a real acquisition candidate; **now acquired**, as stated above (corrected here, independent review Round 19, from an earlier draft's own present-tense 'a real acquisition candidate,' stale since G7 is now closed)"*; row 99 the same for G9; row 56: *"**Was a real, public-domain acquisition candidate for vols. I–III specifically** … now acquired, as stated above (corrected here, independent review Round 19 …)"*. The residual "new G7"/"new G9" wording Round 19 quoted is gone from both. `git diff 5f8625f..fc18741` shows exactly seven Registry lines changed — rows 56, 89, 99, 194, 204 and the two Saturation-statement paragraphs — and no other row touched. **Correct and complete**, subject to M2, which is a different sentence in row 56's cell.

**C3 — the two new Registry disclosures, verified against the files by direct line read.** Row 194's *"the file's own OCR reads 'iiiilgo' for 'uulgo' at this exact word"* — file line 40260 reads `(Pontio diacono iiiilgo adscripta).` Row 204's *"the file's own OCR reads 'xvI' for 'XVI' at this exact word"* — file line 7375 reads `Praesente bis et Claudiano consulibus, xvI Kalendas Augus-`. Both exact. Both substances confirmed present. The second normalization in each string is C3 above and does not affect these.

**L1 — the blanket sweep, verified file by file.** All 19 files carry the clause; `count` returns exactly 1 per file; the clause text is identical across all nineteen (one distinct variant, compared programmatically). `grep -r` for the two Round 17 wordings (`usual letter-level confusions`, `minor character-level variants`) returns zero hits across `cic/texts/`, so no file stacks an old clause under a new one. `git diff` over the 19 files shows exactly one changed line each, and the change is exactly the field-list phrase: 19 removals of `(Content note, Source line, or Title)` and 19 additions of `(Content note, Source line, Title, or this Provenance note itself)`. No other header content was touched. The four earlier Latin/bilingual files (rows 88, 191, 192, 193) correctly do not carry it. **Mechanically complete**; the wording issues are L1 above.

**L4 — the Decision Log's Round 18 arithmetic, recounted from the artifact.** `Doc02_Round18_Review.md` carries exactly **ten** `### ` finding headers (M1–M4, L1–L3, C1–C3) and a verdict line of "0 HIGH · 4 MEDIUM · 3 LOW · 3 COSMETIC." The entry now says "All **ten**." Its enumeration also reconciles now: two correction banners (M1, M2) + two file headers as one finding (M3) + two pre-existing staleness items (M4, L2) = five, plus "**Two** further LOW" (L1, L3) and three COSMETIC (C1–C3) = ten. Round 18's own L1 does name three rows (78 in its heading, 41 and 90 in its body), so the entry's "three already-fulfilled Registry rows" for that single finding is accurate. **Both corrected figures right.**

**M2 (Round 19's) — the Manifest front-matter fix, checked structurally.** A superseding note is now present at line 11, it names the finding that prompted it, it keeps the superseded text rather than rewriting it, it points forward to §1 and to the closing "Status update, 2026-09-08" paragraph, and both of those cross-references resolve to the right places. Rendered bold structure is well-formed (three sibling spans, no nesting). Its *closure* claim — that no acquisition decision remains on the eight — matches Manifest line 85, Doc_02 §9 item 1, and each item's own fulfillment paragraph. Only its provenance clause is wrong, at H1.

**Registry table integrity, recomputed row by row.** All 212 rows re-extracted by column position: numbers **1–212 complete, no gap, no duplicate**; **every row exactly 12 pipes / 11 columns**; **every row balanced on parentheses and backticks**. Three rows sit physically out of numeric sequence — 42 (after 48), 60 and 52 (both after 193) — all covered by the front-matter Disclosed-placement rule, which names "48, 52, 60 among them," and rows 60 and 52 additionally carry their own in-place placement notes. The Excluded set re-parsed from the Boundary Status column is now `{28, 29, 98, 128, 204}`; no live document states an Excluded enumeration, and the Decision Log's `{28, 29, 98, 128}` is correctly scoped to what was checked on 2026-09-02.

**Bold-marker nesting across all four documents, rendered rather than counted.** Every line containing `**` in all four documents was rendered through CommonMark and its `<strong>` tree walked for nesting depth, unclosed spans, and literal `**` survival. Result: **two** anomalies across the 432 bold-bearing lines in the four documents — Doc_02 line 29 (M1) and Registry line 56 (C1). Every other line, including the four-label banner the L3 fix produced at Doc_02 line 25 and the new Manifest note at line 11, pairs exactly as written. `grep -c "\*\*\*\*"` returns 0 in all four documents.

**Census and comparator arithmetic, recomputed across all 56 atlas files.** `latin-pastoral-congregational-christianity.yaml`: **99 entries, 97 distinct titles, `Counter({'tradition': 90, 'context': 9})`, 88 distinct titles inside the tradition set, `Counter({'assigned': 87, 'provisional': 12})`**; exactly two duplicate titles (`The Enchiridion (On Faith, Hope, and Love)`, `The Passion of the Scillitan Martyrs`), both inside the tradition set, so 90 − 2 = 88 reconciles. Comparators re-derived per measure: 99 raw against **68** (`post-apostolic-house-church.yaml`), 97 distinct against 67, 90 `tradition` against **59** (`post-apostolic-house-church.yaml` and `alexandria-catechetical.yaml`, tied), 88 tradition-distinct against 59 — so Doc_02 §1's "largest … on every count attempted" and both stated comparators hold exactly. The nine `context` entries are Delehaye 1921, Harnack 1913, Monceaux I/II/III, von Soden 1904, von Soden 1909, Prosper (Mommsen 1892) and the Codex Theodosianus — **seven of the nine modern (1901–1921) secondary scholarship**, as §1 says.

**Cross-references and row citations.** Every `row`/`rows` number cited anywhere in Doc_02 resolves to an existing Registry row; none falls outside 1–212. Every directional `§N above` / `§N below` reference in Doc_02 was direction-checked programmatically against the section it sits in: **none fails**. Doc_02 §3's `Source_Registry.md` "line 8" pointer is still correct — line 8 is the checkpoint rule (*"Every source named in `Doc_02_Source_Ecology.md` in support of a specific claim has a corresponding row below"*) and line 6 is the Disclosed-placement rule, unchanged by this pass, which inserted and deleted no lines in the Registry.

**Vendored-file headers, swept for the stale-open-request class Round 18 found and spot-checked on claims no prior round has tested.** A programmatic sweep of all 50 `cic/texts/*.txt` headers for "stays open," "remains open," "not yet acquired," "not yet located," "awaiting," "unacquired," "has not been located" returns two hits, both in corrected text describing the current state accurately (the Hartel Pars I–II file's Round 18 correction, and the CSEL 57 file's *"G4 now stays open only for CSEL 58"*). The von Soden *Prosopographie* file's "NOT YET VENDORED" is about the companion article it deliberately excludes, correctly. Spot-checks beyond any prior round: `delehaye_passions-…1921`'s header claim of *"Six chapters (I-VI), running from 'Les passions historiques' through 'Histoire, tradition, litterature'"* — verified against the volume's own six chapter openings (lines 479, 7600, 9808, 13274, 15294, 17757) and its own Table des matières (lines 18691–18720), every element accurate, including the honest disclosure that the "Subsidia Hagiographica 13b" series number cannot be confirmed from this scan. `vonsoden_prosopographie-…1909` opens at the article's own heading and closes inside its own alphabetical register with cross-references to `S. 252-254. 255. 259. 2G3 f.`, consistent with the claimed pp. 247–270 slice.

**Engine scripts, both re-run this session.** `python cic/engine/texts_registry.py` → **exit 0**, *"OK: every vendored file has a header-verified rights line (public domain, or a recognized open licence), an ENTRIES row, and no ENTRIES row points at a missing file"*; `cic/texts/` at 211 MB (30% of the 700 MB planning trigger). `python cic/engine/corpus_map_merge.py --check` → **exit 0**, no error.

**Doc_01 consistency, re-checked at the one place Doc_02 makes a claim about it.** Doc_02 §1's disclosure that Doc_01 *"still states [Possidius's *Life*] is 'not vendored in this corpus,' now stale"* is accurate — Doc_01 §5 carries that phrase verbatim, and §9's Round 8 and Round 9 log paragraphs repeat it as historical record. Doc_02 correctly flags rather than edits it, since Doc_01 is a separate disposed document.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the fix pass and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** H1 concerns who fetched this world's own sources; M2 concerns an archive.org identifier for a work this world requested; M3 concerns this world's own two documents agreeing about their own rows. None decides anything for another world. Mark's 2026-08-26 Perpetua ruling and the Optatus double-placement are still reported rather than reasserted. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing here changes `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022, or any governing document. L1 and L5 are findings that a stated scope does not reach what it was written to reach; L3 is a finding that a chosen form contradicts a remedy this Registry already adopted, not a proposal to change it. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round **agrees with the fix pass and against Round 19** on C1 — and reaches that position by opening the file at both locations and at its own page markers, not by preferring the more recent text. That closes the disagreement rather than leaving it open, on the same footing this log's 2026-09-01 entries established for the `donatism.yaml` and sibling-build disputes. H1 records that a fix pass wrote a false claim, which is a defect to correct, not a tension between two accounts: the Manifest's own body, the Decision Log, and Doc_02 §9 item 1 are not in dispute about what happened on 2026-09-05; two of the three simply state it wrongly. Neither requires the project lead. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

Doc_02's status line and §10, and `Source_Registry.md`'s status line, still describe the Round 14 disposition of 2026-09-02, still read "Fourteen independent adversarial review rounds" over the sequence "(Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0)", and still point a reader to "`Doc02_Round1_Review.md` through `Doc02_Round14_Review.md`" — while `Review-Artifacts/` now holds twenty `Doc02_Round*_Review.md` files counting this one, Doc_02 carries 15 in-text attributions to Round 15, 7 to Round 16, 7 to Round 17, 6 to Round 18 and 3 to Round 19, and `Source_Registry.md` carries 9, 4, 1, 7 and 8 respectively. That is reported here as observed, checkable state, on the same footing Rounds 16 through 19 reported it, and it is the same staleness M4 above documents inside the Decision Log's own entry heading. Whether and how those lines should change, and what disposition follows from this round's counts, is **not assessed here**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition. This review supplies only the input that rule takes: a finding count and a findings list.

**Observed trend, stated as raw counts only and not otherwise characterized.** Across the six verification rounds against this 2026-09-08 revision: Round 15 — 4/6/5/2 (17); Round 16 — 4/5/6/3 (18); Round 17 — 0/3/5/4 (12); Round 18 — 0/4/3/3 (10); Round 19 — 0/2/4/3 (9); Round 20 — 1/4/5/5 (15). HIGH had been zero for three consecutive rounds and is not zero this round. Two observations bear on reading that reversal, stated without weighing them: H1 and three of the four MEDIUM findings sit in text or documents this round examined that no prior round in the sequence had checked in the same way (the Manifest's provenance predicate, Doc_02 §3 against Registry rows 30–33, every line of the four documents rendered rather than parity-counted, and one archive.org identifier fetched live); and two of the five findings above (M3 and C1) pre-date this revision entirely.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 1 HIGH · 4 MEDIUM · 5 LOW · 5 COSMETIC.**
