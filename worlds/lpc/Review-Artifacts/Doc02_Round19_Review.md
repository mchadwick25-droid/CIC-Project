# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 19 Independent Adversarial Review — scoped to verifying the Round 18 fix pass, plus a cold read of the whole document set

**Documents reviewed (committed state — `git status --porcelain` clean at `5f8625f`, "lpc: fix Doc_02 revision per Round 18 independent adversarial review", 2026-09-08 07:39:03 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `worlds/lpc/Doc_02_Source_Ecology.md` (156 lines; §1 through §10 read in full, cold)
- `Source_Registry.md` (329 lines; all 212 rows re-parsed by column position, plus the Saturation statement and its round-by-round record read in full)
- `Source_Acquisition_Manifest.md` (85 lines, read in full — including the front-matter Disposition paragraph, which no prior round in this sequence appears to have checked against the Manifest's own closing status update)
- `lpc_Decision_Log.md` (332 lines; the 2026-09-08 Rounds 15/16/17/18 entry read in full and checked against the diffs and artifacts it describes)
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines), §7 and §8 read in full and searched line by line for every phrase Doc_02 attributes to or denies of them
- `Review-Artifacts/Doc02_Round15_Review.md` through `Doc02_Round18_Review.md`, read in full and in order before any other file
- All 21 `cic/texts/` files the fix pass touched, plus `possidius_vita-augustini_weiskotten1919.txt` and `codex-theodosianus_latinlibrary.txt`; all 56 atlas files in `cic/corpus-map/`; `cic/texts/INTAKE.md`; `cic/texts/REGISTRY.yaml`; both engine scripts

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-08 vendoring, did not write the Round 15, 16, 17 or 18 fix passes, and did not write Rounds 1–18.

**Scope, stated plainly.** Two briefs, run together. First: verify, independently and against primary artifacts, whether each of Round 18's ten findings (M1–M4, L1–L3, C1–C3) is actually closed by the `5f8625f` fix pass — and, since each of the four preceding fix passes introduced at least one new checkable error while fixing what it targeted, look specifically for errors *this* pass introduced. This pass is the first to try two different strategies against that recurrence: it **simplified** the two correction banners Round 18 found wrong rather than elaborating them further, and it applied **one uniform OCR-quotation disclosure to all nineteen vendored files at once** rather than file-by-file. Both strategies are tested below on their own terms. Second: a cold, whole-document read of §1 through §10 for anything no prior round happened to check, with vendored-file header claims spot-checked beyond any prior round's sweep and `Source_Acquisition_Manifest.md` checked for the staleness class Round 18 found in `Source_Registry.md`. Rounds 15–18 were treated as claims to re-derive, not as authority.

**Method — what was actually re-derived, not trusted.** `yaml.safe_load` across all 56 atlas files in `cic/corpus-map/` (59 `.yaml` less `AUTHOR-IDS.yaml`, `UNATTRIBUTED.yaml`, `WORKS.yaml`), counting entries, distinct titles, roles and confidences per file; `git show <commit>:cic/corpus-map/latin-pastoral-congregational-christianity.yaml` at all six revisions in the file's own history, each re-parsed; a fresh regex parser over all 212 Registry rows extracting every column by position, with programmatic `|`, `**`, `(`/`)` and backtick balance counts per row; the same three balance checks over every line of Doc_02, the Manifest and the Decision Log; an actual CommonMark render of Doc_02 §1's correction banner rather than an eyeball count of its delimiters; a programmatic direction check on every `§N above`/`§N below` reference in Doc_02; a programmatic sweep extracting every quoted string of ≥18 characters from all nineteen vendored headers, **separated by header field**, and tested against each file's own de-hyphenated, whitespace-normalized body, with every apparent miss chased into the file by hand; a direct count of each review artifact's own `### ` finding headers and verdict line; `git log -S` traces on three claims about when a defect entered; and both engine scripts run. Nothing was carried forward from Rounds 15–18's tables, from `lpc_Decision_Log.md`, from the `5f8625f` commit message, or from the brief that commissioned this review.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 0 HIGH · 2 MEDIUM · 4 LOW · 3 COSMETIC.**

**All ten of Round 18's findings are closed, this is the third consecutive fix pass with no HIGH-severity regression, and — for the first time in this sequence — no correction banner this pass wrote contains a checkably false claim.** That last result is the specific thing this round was asked to test, and it holds on independent re-derivation. Every substantive assertion in the rewritten §1 banner about the duplicated 256-council rows was re-checked against Doc_01 directly and every one is exact, including the newly-quoted Doc_01 §7 sentence; the two §2 transmission bullets are now mutually consistent and neither makes a falsifiable claim about which draft asserted what; the Saturation statement's historical/current split is correct to the digit on both the 2026-09-01 baseline (73/65/8, re-parsed at `0269b68`) and the current census (99/87/12, re-parsed from raw YAML); Doc_02 §3's "line 8" is right and the Round 7 displacement it blames is confirmed by `git log -S` and by diffing `9adbe66~1` against `9adbe66`; every finding count now stated in `lpc_Decision_Log.md` for Rounds 15, 16 and 17 matches a direct recount of those artifacts' own `### ` headers; the two stale file headers are corrected and accurate; rows 41, 78 and 90 are in the past tense; and all nineteen vendored files carry exactly one uniform, broadened disclosure with no old clause stacked beneath it. Both engine scripts exit 0, all 212 Registry rows parse to 12 pipes with even `**`, balanced parentheses and balanced backticks, and no line in any of the four documents is unbalanced on any of those three counts.

**The findings below are of three kinds, and the recurrence has changed shape rather than stopped.** None is a false claim inside a correction banner — the simplification strategy worked. Two are the fix pass adopting a review artifact's own enumeration without re-deriving it, so a correction is stale at the moment it is written (M1, L4). Two are the blanket-sweep strategy applied with the wrong reach: one sweep's clause names three header fields and not the fourth, which is the field the clause itself sits in (L1); another was applied at the three rows Round 18 named and not at the three sibling rows carrying the identical sentence (L2). One is a markdown defect introduced by the re-elaborated banner (L3). Two are pre-existing and previously uncaught, surfaced only by this round's cold read: the Manifest's own front-matter Disposition paragraph (M2), which no round in this sequence has checked, and a second unqualified "every round" recall-test claim thirty lines below the one the M4 fix corrected.

---

## MEDIUM

### M1. The recall-test correction is stale in two independent respects — it omits Round 18, the round whose own finding prompted it, and a second unqualified "every round" claim survives thirty lines below it in the same Saturation statement

**Limb 1 — the enumeration stops one round short of the round that forced it.** `Source_Registry.md` line 295, written this pass:

> **The ten-item relative-recall test and PRESS question, per CF V7.4's own Doc_02 review requirement, were run once per review round through Round 14 — recorded here rather than only in the review artifacts. Corrected here (independent review, Round 18): Rounds 15, 16, and 17, scoped specifically to verifying the 2026-09-08 source-integration revision rather than re-reviewing this document set in full, did NOT run a fresh recall test or PRESS question**

Doc_02 §9 item 6 (line 136) carries the identical scope:

> **The ten-item relative-recall test and PRESS question were run once per review round through Round 14; Rounds 15–17, scoped to verifying the 2026-09-08 revision rather than a full re-review, did not run either**

**Round 18 also ran neither.** Checked directly rather than inferred: `Doc02_Round18_Review.md` contains four occurrences of "recall" and three of "ten-item," and every one of them is inside its own M4 finding, quoting or describing the Registry's claim — lines 95, 97, 99 and 101. There is no recall score, no ten-item list, and no PRESS answer anywhere in the artifact. Its own scope paragraph names its two briefs as verification plus a cold read, exactly the scoping the corrected sentence gives as the reason Rounds 15–17 skipped it. The fix pass had `Doc02_Round18_Review.md` in front of it — the same commit adds that file to `Review-Artifacts/` and its message names Round 18's counts — and adopted Round 18's own "Rounds 15, 16 and 17 each ran without it" verbatim rather than re-deriving whether the sentence needed a fourth member. By the Registry's own reading rule ("were run once per review round through Round 14 … Rounds 15, 16, and 17 … did NOT"), Round 18 falls in neither set.

**Limb 2 — the same Saturation statement makes the same kind of unqualified claim again, uncorrected.** `Source_Registry.md` line 325, thirty lines below the corrected paragraph:

> **A round-by-round instrument accounting, rather than a running total restated here:** the recall score **has returned 0/10 in every round except Round 2** (3/10, itself its own prior round's PRESS dispositions being found again rather than new coverage) — see each round's own paragraph above for the specific instruments and the specific gap each one found

Counted directly from the section it points into: the round-by-round record runs `*Round 1*` through `*Round 14*` and stops, and carries exactly fourteen recall scores — thirteen `0/10` and Round 2's `3/10`. In Rounds 15, 16, 17 and 18 the test returned no score at all, which is not "0/10." This is the identical unqualified-universal defect Round 18's M4 limb 2 found at line 295 and the fix pass corrected there; the sentence at line 325 was not touched, and it is inside the same Saturation statement, under a heading that presents itself as *the* accounting for the practice. Doc_02 §9 item 6 routes a reader to that statement as "the single authoritative count."

### M2. `Source_Acquisition_Manifest.md`'s own front-matter Disposition paragraph still tells the project lead that all nine G-items await his acquisition decision — the same document's closing status update says the opposite, and this paragraph carries no superseding note

Manifest line 11, unchanged since before the 2026-09-08 vendoring:

> **Disposition.** This document, `Doc_02_Source_Ecology.md`, and `Source_Registry.md` were self-disposed together by the build thread to **Approved to proceed** on 2026-09-02 … **This Manifest's own G1–G9 candidates are unchanged by that disposition and remain awaiting Mark's own acquisition decision, per Article 21 and the G1-gate checkpoint — a genuine project-lead decision this build thread does not make unilaterally**, distinct from the self-disposable review cycle that has now concluded for these three documents.

Manifest line 85, the closing status update, says the opposite in terms:

> **Status update, 2026-09-08: eight of nine requests are now closed, the ninth (G4) nearly so.** … **No acquisition decision remains for the project lead to make on G1, G2, G3, G5, G6, G7, G8, or G9** … each closed on its own public-domain footing, independently verified, no rights or resource trade-off requiring his own judgment.

Doc_02 §9 item 1 states the same closure, and each of G1, G2, G4, G5, G6, G7, G8 and G9 carries its own dated "Fulfilled 2026-09-08" paragraph (G3's is "Fulfilled 2026-09-05"), each of which was checked against the Registry row it names. So the Manifest asserts, in its own opening front matter, a pending project-lead decision that its own body has recorded as discharged.

The omission is specifically a *propagation* failure, not a deliberate historical record. This Manifest's own established practice for a superseded paragraph is to keep it and mark it — line 57's network-access limitation is followed at line 59 by "**Superseded 2026-09-08: network access confirmed working.** … This paragraph is kept as the historical record of a real, previously-confirmed limitation, not rewritten to look retroactively current," and the "Decision from the project lead" section at line 81 is superseded in place by line 85. Round 15 certified both of those. Line 11 got neither treatment: no superseding note, no date qualifier, no pointer forward. It is the first substantive paragraph a reader of the Manifest reaches, and it is addressed by name to the project lead in his operational acquisition role.

This is the same defect class Round 18 rated MEDIUM at its own M3 (a live artifact describing an already-closed Manifest request as open) and M4 limb 1 (a live document stating a superseded figure "as of this revision"). Round 18's sweep reached two vendored file headers and the Registry's Saturation statement; it did not reach the Manifest, and neither did this fix pass.

---

## LOW

### L1. The uniform OCR-quotation disclosure applied to all nineteen files declares a scope that excludes the Provenance note — the field the clause itself sits in, in all nineteen — leaving five files' normalized quotations uncovered, including both exemplars Round 18 named

The clause, identical in all nineteen files:

> Note (independent review, Round 18): quotations elsewhere in this header **(Content note, Source line, or Title)** are given in standard/readable spelling for legibility; the file's own OCR carries the usual scan-level noise at some of the same points -- letter confusions (V/Y, C/G, u/n and similar), and, at points of heavier degradation, **a single word broken into multiple tokens or joined with an adjacent one**. A reader matching a quoted phrase against the file directly should expect this range of variation, not a discrepancy in substance; the file's own body text, not this header's quotation of it, is authoritative for exact wording.

The broadening Round 18's C2 asked for is genuinely there — "a single word broken into multiple tokens" covers the word-breaking the old clause did not. The *field list* does not. Checked programmatically across all nineteen headers: **in every one of the nineteen, the clause is placed inside the `Provenance note:` field**, and the field list it gives — Content note, Source line, Title — names the three fields it is *not* in.

Five files carry normalized quotations of retained text in their Provenance notes, each therefore outside the clause's stated reach, and two of the five are the exemplars Round 18's own findings were built on:

| file | Provenance-note quotation | file actually reads |
|---|---|---|
| `augustine_enarrationes-…migne-pl36-37` | "kept only from **'PATROLOGIAE LATINAE TOMUS XXXVI'** onward" | `PATRO LOGI Ai LATINJE TOMUS XXXYI.` (l. 13) |
| `monceaux_…tome1_1901` | "after the printer's colophon (**'Angers. -- Imprimerie Orientale de A. Burdin et Cie.'**)" | `ANGERS. — IMPRIMEHIE ORIENTALE DE A. BURDIN ET Cl°.` |
| `monceaux_…tome2_1902` | same sentence | `ANGERS. — iMPiilMEiiiF. ORIENTALE DE A. BDRDIN ET I '".` |
| `monceaux_…tome3_1905` | same sentence | `ANGBHS. — IMPRIMERIE ORIENTALE DE A. BU RIU N ET Cle.` |
| `vonsoden_prosopographie-…1909` | "the article's own heading (**'DIE PROSOPOGRAPHIE DES AFRIKANISCHEN EPISKOPATS ZUR ZEIT CYPRIANS. VON HANS VON SODEN.'**)" | `DIP^ PROSOPOGKAPHIE` … `VON HANS VON SODEN i).` (ll. 13–18) |

The Enarrationes line is the exact case Round 18's C2 named as the one the old clause failed to cover ("one word broken into three tokens, not a character confusion"); the three Monceaux colophons and the von Soden heading are four of the entries in Round 18's own C1 table. All five sit in the one field the new clause does not claim.

Two further Provenance-note quotations that the sweep also does not cover are **correct as they stand and are not part of this finding**, checked individually rather than counted from the same script: `codex-canonum-…bruns-pars1-1839`'s "The Gift of Col. Benjamin Loring" describes a bookplate the note says was *stripped*, and `vonsoden_prosopographie`'s "Toscanische Studien," names the *next* article in the serial, immediately after this slice ends. Both are correctly absent from their files.

Each of the five headers still carries, in the same Provenance note, the sentence "nothing else altered, **no OCR error corrected**" that made this a finding at Harnack (Round 16 C3) and at the five files Round 17's C2 fix reached. As at every prior round, the substance is confirmed present in every case; this is about the quotations, not the claims they support.

### L2. The past-tense repair was applied at the three rows Round 18 named and not at the three sibling rows carrying the identical sentence

Round 18's L1 named rows 41, 78 and 90. All three are fixed and correct:

- Row 41: *"Was flagged as an open acquisition lead rather than a confirmed candidate; **now vendored, as stated above** (corrected here, independent review Round 18)"*
- Row 78: *"**Was** a real acquisition candidate; **now acquired**, as stated above (corrected here, independent review Round 18, from an earlier draft's own present-tense 'once located,' stale since the identifier was in fact located and the volume vendored)"*
- Row 90: *"**Was** a real acquisition candidate; **now acquired**, as stated above (corrected here, independent review Round 18, from an earlier draft's own present-tense 'once located,' stale since G8 is now closed)"*

`git diff 6fd4973..5f8625f -- Source_Registry.md` shows exactly three rows changed: 41, 78, 90. Three sibling rows in the same set — the seven rows Round 15's H4 corrected — carry the identical present-tense construction after their own "Now vendored" opener, and were not touched:

- **Row 89**, opening *"**Now vendored, row 210 (2026-09-08, independent review Round 15)**, closing Manifest G7"*, closes: *"**A real acquisition candidate** — see `Source_Acquisition_Manifest.md`, **new** G7."*
- **Row 99**, opening *"**Now vendored, row 212 (2026-09-08, independent review Round 15)**, closing Manifest G9"*, closes: *"**A real acquisition candidate** — see `Source_Acquisition_Manifest.md`, **new** G9."*
- **Row 56**, opening *"**Vols. I–III now vendored, rows 206–208 … closing Manifest G5 in full**"*, contains: *"**This is a real, public-domain acquisition candidate for vols. I–III specifically**"*.

Row 89's and row 99's sentences are word-for-word the sentence rows 78 and 90 were corrected from. This is the same one-site-at-a-time shape Round 17 named at its L5 and Round 18 named at its L1, recurring at the sibling rows in the same set — and it recurs in the one part of this fix pass that did *not* adopt the blanket-sweep strategy the same pass used successfully on the nineteen file headers.

### L3. The re-elaborated §1 correction banner is unbalanced on `**` nesting, and the rendered result inverts the emphasis: the Round 18 correction label renders plain while the explanation renders bold

Doc_02 §1, line 25, carries **six** `**` delimiters (counted programmatically at offsets 0, 145, 855, 1114, 1335, 1970). The line balances on a naive even/odd test — which is why the standard parity check this project runs passes on it — but CommonMark pairs them 1↔2, 3↔4, 5↔6, not as the author intended. Rendered with a CommonMark parser this session, the banner comes out as:

> **corrected here (independent review, Round 17, its own M2), from an earlier draft's own false attribution, standing uncaught since the Round 1 fix pass: no quotation resembling "the 256 council is independently attested twice..." appears anywhere in Doc_01.** Corrected further here (independent review, Round 18, its own M1), from this same banner's own first draft, which overcorrected into a second false claim — that Doc_01 §7 "does not discuss these corpus-map rows at all": **Doc_01 §7's own World #4 (Donatism) bullet does name them … as an item routed to this document rather than decided for it.**

The document's own uniform convention everywhere else is a bolded correction label followed by plain explanation; here the label is plain for ~220 characters and the explanation is bold for ~630. Traced by diff rather than assumed: at `6fd4973` the same passage carried a single balanced `**…**` pair, so the defect is new at `5f8625f`, introduced by appending a second banner inside the first rather than after it. This is the same class as Round 16's C1 (`****`) and Round 17's L2 (an orphaned closing marker inverting bold parity for the rest of a cell) — both of which the parity check caught. This one it cannot, because the count is even.

*(The banner's substance is entirely correct — see "What was checked and found clean." Only its markup fails.)*

### L4. `lpc_Decision_Log.md`'s new Round 18 paragraph miscounts Round 18's findings as twelve, three clauses after stating the four numbers that sum to ten — and its LOW subtotal over-counts by one against its own enumeration

`lpc_Decision_Log.md` line 328, written this pass:

> **Round 18** … found **0 HIGH findings for the second consecutive round** — **0 HIGH, 4 MEDIUM, 3 LOW, 3 COSMETIC**. … Three further LOW and three COSMETIC findings … rounded out the count. **All twelve of Round 18's own findings were fixed in the same pass this entry records**

Counted directly from `Doc02_Round18_Review.md`: **ten** `### ` finding headers (M1–M4, L1–L3, C1–C3), verdict line "**Findings: 0 HIGH · 4 MEDIUM · 3 LOW · 3 COSMETIC.**", restated identically at its close. The entry contradicts itself twice over — the same sentence gives the four numbers that sum to ten, and the entry's own closing paragraph (line 330) gives the series correctly: *"the finding count has fallen each round since Round 16 (**18 → 12 → 10**)."* The `5f8625f` commit message also has it right ("17 (Round 15) -> 18 (Round 16) -> 12 (Round 17) -> **10** (Round 18)"). Only the entry's own headline is wrong, and "twelve" is the figure belonging to Round 17, whose parallel clause sits two sentences above it.

A second, smaller figure in the same sentence: "**Three further LOW** and three COSMETIC findings" over-counts by one against the entry's own enumeration. The preceding clause has already counted L2 (the `Source_Registry.md` line-number cross-reference) among the "two pre-existing, previously-uncaught staleness items"; Round 18 had three LOW findings in total, so at most two remain "further." L3 is not described anywhere in the paragraph.

This is the fifth consecutive round in which this Decision Log entry's own finding arithmetic is wrong somewhere — Round 17's L3 found three such figures, Round 18's L3 found two more, and both were corrected this pass. The correction did not extend to the paragraph being added alongside it.

---

## COSMETIC

### C1. The Prosper file's header quotes the volume's own title with a word interpolated that appears neither in the file nor in Mommsen's title — and the newly-broadened disclosure does not reach a word insertion

`cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt`, Content note:

> Prosper of Aquitaine's Epitoma Chronicon (this world's own target text) begins at the printed volume's p. 385 with its own full title (**"PROSPERI TIRONIS EPITOMA DE CHRONICON..."**)

The file's own title block, at lines 42580–42585:

```
PROSPERI TIRONIS
EPITOMA CHEONICON
EDITA PRIMVM A. CCCCXXXIII
CONTINVATA AD A. CCCCLV
```

`CHEONICON` is an ordinary R→E confusion of `CHRONICON`, squarely inside the disclosure. The interpolated **`DE`** is not: it is neither a letter confusion nor a word split or joined, and Mommsen's own title carries no such word (*Prosperi Tironis epitoma chronicon*, the form Registry row 203 and Doc_02 §5 both use correctly). The clause the fix pass wrote instructs a reader to expect "this range of variation, not a discrepancy in substance"; a reader searching this string finds nothing and is told by the disclosure that the difference must therefore be substantive.

Nothing downstream rests on it — Registry row 203's Source column and Doc_02 §5's own citation both name the work correctly, and every other claim in this header was verified this round (see below).

### C2. §2's new parenthetical points a reader at "`lpc_Decision_Log.md`'s 2026-09-08 entry"; there are four entries under that date, and only the last carries the record it points at

Doc_02 §2, line 54, written this pass:

> (This document's own account of Pontius's Latin transmission was corrected once, then corrected again, across independent review Rounds 16–18; the statement here is the current, independently re-verified one — see **`lpc_Decision_Log.md`'s 2026-09-08 entry** for the fuller record of what each round found, rather than restating that history here.)

`grep -o "^### [0-9-]*" lpc_Decision_Log.md | sort | uniq -c` returns **four** entries dated 2026-09-08 (network access confirmed; ten sources vendored; G1 closed in full; and the Rounds 15/16/17/18 review entry). Only the fourth records what each round found about Pontius's transmission — which it does, accurately, at all three of its Round 16, Round 17 and Round 18 paragraphs. The pointer is the substitute this pass wrote *in place of* restating the history inline, so its precision is the whole point of the simplification. Doc_02's own practice elsewhere is to qualify a same-date reference: §1 line 21 says "`lpc_Decision_Log.md`'s **2026-09-05 G3 entry**" where three entries share that date. (§9 item 1's "`lpc_Decision_Log.md`, 2026-09-08 entry" carries the same ambiguity and is pre-existing.)

### C3. Registry rows 194 and 204 quote their own files' OCR in normalized form, with no equivalent of the disclosure the blanket sweep gave the nineteen files

The sweep reached the vendored headers. The two Registry rows that quote the same strings were not brought along:

- **Row 194**, Verification Note: *"the Vita's own heading (**'VITA CAECILII CYPRIANI (Pontio diacono uulgo adscripta)'**) directly verified."* The file reads `(Pontio diacono iiiilgo adscripta).` at line 40260.
- **Row 204**, Verification Note: *"**'Praesente bis et Claudiano consulibus, XVI Kalendas Augustas...'**"*. The file reads `consulibus, xvI Kalendas Augus-` at line 7375.

Round 18's C1 noted the row-204 case in passing ("Registry row 204's Verification Note carries the same normalized Scillitan formula as the file it describes") without making it a separate finding; row 194's was not previously named. Both substances are confirmed present — this is about the quotations. The Registry has no header-level disclosure convention of its own, so the corrective here is a per-row note rather than a sweep, which is why it is recorded as cosmetic rather than as a gap in the sweep itself.

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**M1/M2 — the two simplified banners, tested claim by claim rather than accepted as "simpler."** This was the round's central question and the answer is that the simplification worked.

*§1's 256-council banner (line 25)* makes five checkable assertions and every one holds on independent re-derivation:
1. *"no quotation resembling 'the 256 council is independently attested twice...' appears anywhere in Doc_01"* — Doc_01 searched in full: **zero** hits for "attested twice," "independently attested," "two different vendored," "two different classifications," "npnf214," "Seven Ecumenical," and "Acts of the Council."
2. *"standing uncaught since the Round 1 fix pass"* — `git log -S "independently attested twice"` on Doc_02 returns exactly one commit, `4796ee3`, "lpc Doc_02: Round 1 fixes."
3. *"Doc_01 §7's own World #4 (Donatism) bullet does name them, in the same breath that hands them to §8 as unresolved"* — Doc_01 §7 runs 144–168, §8 opens at 169, and the World #4 bullet is line 166. Correct.
4. The quoted sentence — *"what remains open is the Optatus placement question... and the duplicated Council-of-Carthage-under-Cyprian corpus-map rows... both genuinely Doc_02's, carried forward again at §8 below"* — is **verbatim** against Doc_01 line 166, with both ellipses replacing only the two Step 0 cross-references.
5. *"Doc_01 §8 item 2 then carries the duplication among its own open items"* — verified verbatim at Doc_01 line 172, under the heading "Open items carried forward to later steps."

The banner also correctly quotes what it withdraws: *"that Doc_01 §7 'does not discuss these corpus-map rows at all'"* is verbatim against `6fd4973`'s text. **Substantively correct and complete**, subject only to L3's markup.

*§2's two transmission bullets.* The Pontius bullet's substantive claim — *"also reaches this corpus in Latin, at its own source: the Vita Caecilii Cypriani inside Hartel's CSEL 3 Pars III (Registry row 194)"* — was re-verified independently rather than carried forward: Registry row 194's Licensed-For reads *"**The Vita specifically** as this world's own Cyprian-side formation-narrative material, corroborating the already-vendored ANF05 English translation (row 7) at its own Latin source"*; the heading `VITA CAECILII CYPRIANI` is at line 40258 of the file; and the corpus map carries `Vita Caecilii Cypriani (attributed to Pontius the deacon) | pontius | tradition | assigned | cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`. Row 192 is genuinely bilingual: its Confidence is **A**, its Verification Note reads *"A genuinely bilingual edition — because the complete English translation is present throughout, this row's Confidence is **A**, the ordinary-primary-evidence footing, not the second-witness-only footing rows 88, 191, and the Nestle 1904 Greek New Testament carry."* The Pontius bullet's replacement parenthetical makes **no falsifiable claim about which draft asserted what** — it says the account "was corrected once, then corrected again, across independent review Rounds 16–18" and routes the detail to the Decision Log, which does carry it at all three round paragraphs. The Possidius bullet's correction banner was removed outright; its remaining substance (*"Possidius's Latin and English are one facing edition from one hand (Weiskotten's), while Pontius's English (Migne-based, ANF05, Wallis's translation) and Latin (Hartel's CSEL 3) are two independent editions from different editors"*) is accurate and consistent with the Pontius bullet. `grep "only via"` over Doc_02 returns **0**. The two bullets no longer contradict each other or the record. *(Observed, not counted as a finding: the withdrawn HIGH-severity claim of Round 16's H2 lived in the Possidius bullet, which now carries no notice of it at all; the notice sits seven lines above, in the Pontius bullet, phrased broadly enough — "this document's own account of Pontius's Latin transmission" — to cover it, and §10's own paragraph expressly licenses this simplification move.)*

**M3 — both file headers, checked against the Registry and Manifest rather than against the fix's own account.** `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt` now reads: *"Does NOT include CSEL 3 Pars III (spuria, the Vita Caecilii Cypriani, and the Acta Proconsularia) -- a separate volume, **vendored 2026-09-08** at `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` (Registry row 194; corrected here, independent review Round 18 … **G1 is now closed in full, Pars I through III all vendored**)."* `augustine_epistulae-critical_goldbacher-csel57-pars4.txt` now reads: *"Corrected here (independent review, Round 18): **CSEL 34/1, 34/2, and 44 were vendored 2026-09-08 (Registry rows 195-196)** … **G4 now stays open only for CSEL 58** (praefatio and indices, no letter text of its own)."* Both check out against Manifest G1's and G4's own fulfillment paragraphs, against Registry rows 39 and 61, and against Doc_02 §9 item 1. `grep` confirms neither file now contains "stays open" for a closed part. **Correct and complete at both.**

**M4 — the Saturation statement, both limbs, recomputed from raw artifacts.** Limb 1 is exact on both figures. The current census, re-parsed with `yaml.safe_load` this session: **99 entries, 97 distinct titles, `Counter({'tradition': 90, 'context': 9})`, 88 distinct titles inside the tradition set, `Counter({'assigned': 87, 'provisional': 12})`** — matching the corrected "the census has since grown to 99 works (87 `assigned`, 12 `provisional`)" to the digit. The historical baseline re-parsed at `0269b68` (2026-09-01): **73 entries, `Counter({'assigned': 65, 'provisional': 8})`, all `role: tradition`** — matching "73 works … 65 `confidence: assigned` and 8 `provisional`" exactly, and the census's own commit history confirms it was still 73 on the 2026-09-02 disposition date the paragraph now scopes itself to (the next change is `cf1033e`, 2026-09-03). The historical-record framing — *"this paragraph is kept as the historical record of this Registry's own original saturation basis, not updated to the current figure, since the current figure and its own basis are stated where they are current: Doc_02 §1's own opening paragraph"* — matches Doc_02 §1, which does state 99/90/88 and labels 73 as historical. **Limb 1 correct and complete**; limb 2 is the subject of M1 above.

**L1, L2, L3 — closed.** Rows 41, 78 and 90 are all in the past tense (quoted at L2 above); the residual clauses Round 18 quoted ("A real acquisition candidate once located," "Flagged as an open acquisition lead") are gone from all three. Doc_02 §3 now reads *"`Source_Registry.md` **line 8** — corrected here, independent review Round 18, from 'line 6,' stale since the Round 7 fix pass inserted the Disclosed-placement rule above it, eleven rounds ago"*, and every part of that was re-derived: `Source_Registry.md` line 8 is *"Every source named in `Doc_02_Source_Ecology.md` **in support of a specific claim** has a corresponding row below, per the Registry's own checkpoint rule"* — the exact phrase Doc_02 quotes — while line 6 is the Disclosed-placement rule; `git show 9adbe66~1:` puts the checkpoint rule at line 6 and `git show 9adbe66:` puts the Disclosed-placement rule there with the checkpoint rule at line 8, so the Round 7 attribution is exact. "line 8" and "line 6" are the only two `line N` references in Doc_02 and the second is inside the correction banner quoting the withdrawn one. The three Decision Log figures Round 18's L3 named are all corrected: the Round 16 numerator now reads "found **most** of the sixteen applied fixes held" (no longer "fifteen of the sixteen," which contradicted the four regressions named in the same sentence), and both "eighteen, not seventeen" and "sixteen, not seventeen" now correspond to actual single corrections above them in the entry.

**L3's finding counts, recounted from each artifact's own headers and verdict line, and checked against every figure the Decision Log entry states.** Counted directly: `Doc02_Round15_Review.md` — **17** `### ` headers (H1–H4, M1–M6, L1–L5, C1–C2), verdict "4 HIGH · 6 MEDIUM · 5 LOW · 2 COSMETIC" (= 17); `Doc02_Round16_Review.md` — **18** (H1–H4, M1–M5, L1–L6, C1–C3), verdict "4 · 5 · 6 · 3" (= 18); `Doc02_Round17_Review.md` — **12** (M1–M3, L1–L5, C1–C4), verdict "0 · 3 · 5 · 4" (= 12); `Doc02_Round18_Review.md` — **10** (M1–M4, L1–L3, C1–C3), verdict "0 · 4 · 3 · 3" (= 10). Against the Decision Log entry: "4 HIGH, 6 MEDIUM, 5 LOW, 2 COSMETIC" for Round 15 ✓; "Of the seventeen findings Round 15 made, 16 (H1–H4, M1–M6, L1–L5, C1) were fixed in place; the seventeenth, C2 … deliberately left" ✓ (enumeration sums to 16); "All eighteen of Round 16's own findings (H1–H4, M1–M5, L1–L6, C1–C3)" ✓; "0 HIGH, 3 MEDIUM, 5 LOW, 4 COSMETIC" for Round 17 ✓; "All twelve of Round 17's own findings (M1–M3, L1–L5, C1–C4)" ✓; "0 HIGH, 4 MEDIUM, 3 LOW, 3 COSMETIC" for Round 18 ✓; "(18 → 12 → 10)" ✓. **Every stated count reconciles except the two at L4 above.**

**C1/C2 — the blanket sweep, verified file by file rather than by the pass's own account.** All **19** files vendored at `c803529` carry the new clause; `grep -c` returns exactly **1** per file, so no file has it twice. The old Round 17 clause is gone everywhere: `grep -r "usual letter-level confusions"` and `grep -r "minor character-level variants"` over `cic/texts/*.txt` each return **zero** hits, so no file carries an old and a new clause stacked. The three files that still contain the string "independent review, Round 17" carry unrelated Round 17 corrections (the Getty-barcode disclosure at the two Epistulae files, the Perpetua-assignment correction at the Robinson file), not a residual OCR clause. The clause's own text covers word-breaking as Round 18's C2 asked — *"a single word broken into multiple tokens or joined with an adjacent one"* — and is broadened from the old "Content note" scope to three fields; the field-scope defect is L1 above. The set of 19 is exactly the 2026-09-08 batch: the four Latin/bilingual files vendored earlier (rows 88, 191, 192, 193) correctly do not carry it, and two of those four were touched this pass for M3 only.

**C3 — the "two clauses later" miscount, checked against the current sentence structure.** §1 line 29 now reads *"row 200 — restored here, independent review Round 17's own M1, after the Round 15 fix pass dropped it from this list while adding **the following sentence, which still names it**"*. Verified: the list sentence runs on through three further members (rows 201, 209, 202) and ends at a full stop; the very next sentence is *"**Two of these are the Maurist text, not a modern critical edition** …"*, which names rows 200 and 201. "The following sentence" is exact. **Correct.**

**Registry table integrity, recomputed row by row rather than trusted from Round 18.** All 212 rows re-extracted by column position: numbers **1–212 complete, no gap, no duplicate**; **every row parses to exactly 11 columns / 12 pipes**; **every row has an even `**` count, balanced parentheses, and balanced backticks**. `grep -c "****"` returns **0** in `Source_Registry.md`, `Doc_02_Source_Ecology.md`, `lpc_Decision_Log.md` and `Source_Acquisition_Manifest.md` alike, and the same three balance checks pass on **every line** of all four documents. (The one place where an even count is not sufficient is L3 above, which is why this round rendered the line rather than only counting it.)

**Census and comparator arithmetic, recomputed across all 56 atlas files.** `latin-pastoral-congregational-christianity.yaml`: 99 entries, 97 distinct titles, 90 `tradition` / 9 `context`, 88 distinct tradition titles, 87 `assigned` / 12 `provisional`; exactly two duplicate titles (`The Enchiridion (On Faith, Hope, and Love)`, `The Passion of the Scillitan Martyrs`), both inside the tradition set, so 90 − 2 = 88 reconciles. Comparators re-derived per measure: 99 raw against **68** (`post-apostolic-house-church.yaml`), 97 distinct against 67, 90 `tradition` against **59** (`alexandria-catechetical.yaml` and `post-apostolic-house-church.yaml`, tied), 88 tradition-distinct against 59 — so §1's "largest … on every count attempted" holds and both stated comparators are exact. The nine `context` entries are Delehaye 1921, Harnack 1913, Monceaux I/II/III (1901/1902/1905), von Soden 1904, von Soden 1909, Prosper (Mommsen 1892) and the Codex Theodosianus — **seven of the nine modern (1901–1921) secondary scholarship**, exactly as §1 says. The census history re-parsed at all six revisions: 73 (`0269b68`, 09-01) → 74 (`cf1033e`, 09-03) → 75 (`97419d7`) → 76 (`7ead600`) → 77 (`4911c02`, all 09-05) → 99 (`c803529`, 09-08), so §1's "four earlier additions … 2026-09-02 through 2026-09-05" and the Decision Log's "five passes (four before this revision, one on the day itself)" both hold.

**Cross-references and row citations.** All directional `§N above` / `§N below` references in Doc_02 were direction-checked programmatically against the section each sits in: **none fails**. Every `row`/`rows` number cited anywhere in Doc_02 (66 distinct) falls inside 1–212 and exists in the table; **every row number 191–212 is referenced**, so Round 15's L4 gap stays closed.

**Doc_02 §2's "not yet closed" row list, re-derived against `cic/texts/` rather than carried forward.** The list is rows 19, 22, 23, 15, 18, 25, 21, and 13–14. The Latin Augustine files actually present are the two City of God parts, the Confessions, Bruder's *De Doctrina Christiana*/Enchiridion, the Enarrationes, the three Epistulae volumes, and the Retractationes — none of which covers *De Baptismo* (13), *Contra Litteras Petiliani* (14), *De Catechizandis Rudibus* (15), the creedal works (18), the Sermons (19), the Tractates on John (21), the anti-Manichaean corpus (22), the anti-Pelagian corpus (23), or *De Trinitate* and the grouped treatises (25). The list is neither over- nor under-inclusive.

**Vendored-file header content claims, spot-checked at six files and on claims no prior round checked.**
- `augustine_civitate-dei-1-13-…csel40-1`: "Covers Books I-XIII of twenty-two … **No index in this Pars** (the indices are bound with Pars II)" — the file's last content lines are apparatus (`dominus uigilius' Domb.`), with no index section. Confirmed.
- `augustine_civitate-dei-14-22-…csel40-2`: the closing prayer is at l. 35611 (`gratias congratulantes agant. Arnen.`, the OCR variant the disclosure covers), followed by a scripture index opening `Index locorum` at l. 36368 and `INDEX AVCTORVM GRAECORVM ET LATINO RVM.` at l. 41229 — both indices present as claimed, the second with a word-break the disclosure covers.
- `vonsoden_cyprianische-briefsammlung-deu_1904` — **a file no prior round checked at all.** Its header's full structural claim was verified against the volume's own *Inhaltsübersicht* (ll. 361–494): Vorwort (l. 303, dated `November 1903` at l. 356), Einleitung, **Erster Teil §§3–9** (ll. 375–404), **Zweiter Teil §§10–20** (ll. 406–460), **four Exkurse I–IV** (ll. 464, 466, 472, 476), Literaturverzeichnis (l. 479), Handschriftenverzeichnis (l. 481), and Tabellen I–VI. Every element accurate.
- `prosper_chronica-minora-1-…mommsen1892`: `I. ADDITAMENTA AFRICANA A. 446—455.` at l. 55195 and `V. EPITOME CARTHAGINIENSIS.` at l. 55871, sitting between the printed page marks 484 (l. 55090) and 496 (l. 56021) — consistent with the header's "pp. 486-497." The Liber Genealogus is confirmed a distinct text at l. 1484ff, as the header warns. Only the quoted title fails (C1).
- `perpetua-scillitan-martyrs-…robinson1891`: the header's claim that the file "carries the **Latin/Greek** text of BOTH" was tested rather than assumed — the file contains **zero Greek-script characters**, but the volume's own table of contents reads `THE LATIN AND GREEK TEXTS OF THE PASSION . . 60-95` (l. 159), `The Latin and Greek Texts . . . 112` (l. 171) and `Index of words in the Greek Text of S. Perpetua . . . 128` (l. 176), and the Greek is genuinely present, OCR'd into Latin lookalikes — `MAPTYPION TOY ATIOY KAI KAAAINIKOY MAPTYPOZ ZTTEPATOY` at l. 7428, followed by continuous transliterated Greek. The three page ranges the header gives (60–95, 112–117, 118–121) all match the TOC. **Header claim correct**; the absence of Greek Unicode is an OCR artifact, not a content gap.
- `monceaux_…tome2_1902`: `LIVRE TROISIÈME` at l. 78, `LIVRE QUATRIÈME` at l. 11324, `APPENDICE` from l. 20746 with the tomb-and-basilicas material at ll. 20769–20830 — the header's "Covers Livre Troisieme … and Livre Quatrieme, ending with an appendix on Cyprian's own tomb and basilicas at Carthage" is accurate.

Also re-verified: the corpus map's own note for the ANF05 Pontius entry contains the phrase Doc_02 §2 attributes to it — *"By Pontius the Deacon, Cyprian's own deacon - often counted the earliest Christian biography"* (the phrase is line-wrapped in the YAML source, so a line-based grep misses it; it is present in the parsed value).

**Engine scripts, both re-run this session.** `python cic/engine/texts_registry.py` → **exit 0**, *"OK: every vendored file has a header-verified rights line (public domain, or a recognized open licence), an ENTRIES row, and no ENTRIES row points at a missing file"*; 23 non-English sources listed, all 19 new files among them; `cic/texts/` at 211 MB (30% of the 700 MB planning trigger). `python cic/engine/corpus_map_merge.py --check` → **exit 0**, *"528 distinct work(s) → 788 assignment(s) across 56 Atlas entry(ies) [check only, nothing written]"*, no error.

**Internal arithmetic across Doc_02.** 430 − 246 = **184** (§6's span); 391 − 258 = **133** (§7's gap); §9 item 1's eight closed G-items (G1, G2, G3, G5, G6, G7, G8, G9) match the Manifest's own eight and are listed identically in both, with the same G4/CSEL 58 residual; §9 item 11's three sub-parts for Doc_01 §8 item 2 match Doc_01 line 172's own three. The Saturation statement's round-by-round record carries exactly fourteen round paragraphs and fourteen recall scores (thirteen `0/10`, Round 2's `3/10`), matching the status line's "fourteen rounds."

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the fix pass and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** M2 concerns this world's own Manifest contradicting its own fulfillment record about acquisition state; M1 concerns a stale enumeration and an unqualified universal inside this world's own Registry. Neither decides anything for another world, and neither reopens Mark's own 2026-08-26 Perpetua ruling or the Optatus double-placement, both of which this document set continues to report rather than reassert. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing here changes `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022, or any governing document. M1 limb 2 and L1 are findings that a stated scope does not reach what it was written to reach, not that the convention changed. C1 and C3 are findings that a quotation does not match its source, not that the quoting convention changed. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round disagrees with no prior round on any point of fact. It extends Round 18's own M4 limb 2 by one round (Round 18 did not observe that it too ran no recall test) and by one further site (line 325), both closed here by reading the artifacts directly rather than by preferring any account. Neither requires the project lead. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

Doc_02's status line and §10, and `Source_Registry.md`'s status line, still describe the Round 14 disposition of 2026-09-02, still read "Fourteen independent adversarial review rounds" over the sequence "(Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0)", and still point a reader to "`Doc02_Round1_Review.md` through `Doc02_Round14_Review.md`" — while Doc_02 now carries 15 in-text attributions to Round 15, 7 to Round 16, 6 to Round 17 and 3 to Round 18, and `Source_Registry.md` carries 9, 4, 1 and 5 respectively. That is reported here as observed, checkable state, on the same footing Rounds 16, 17 and 18 reported it, and it is the same staleness M1 limb 2 documents inside the Saturation statement, whose round-by-round record likewise stops at Round 14. Whether and how those lines should change, and what disposition follows from this round's counts, is **not assessed here**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition. This review supplies only the input that rule takes: a finding count and a findings list.

**Observed trend, stated as raw counts only and not otherwise characterized.** Across the five verification rounds against this 2026-09-08 revision: Round 15 — 4/6/5/2 (17); Round 16 — 4/5/6/3 (18); Round 17 — 0/3/5/4 (12); Round 18 — 0/4/3/3 (10); Round 19 — 0/2/4/3 (9). HIGH has been zero for three consecutive rounds; MEDIUM has fallen from 6 to 5 to 3 to 4 to 2; the total has fallen at each round since Round 16.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 0 HIGH · 2 MEDIUM · 4 LOW · 3 COSMETIC.**
