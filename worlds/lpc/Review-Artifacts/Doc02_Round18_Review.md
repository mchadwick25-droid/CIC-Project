# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 18 Independent Adversarial Review — scoped to verifying the Round 17 fix pass, plus a cold read of the whole document

**Documents reviewed (committed state — `git status --porcelain` clean at `6fd4973`, "lpc: fix Doc_02 revision per Round 17 independent adversarial review", 2026-09-08 07:10:35 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `worlds/lpc/Doc_02_Source_Ecology.md` (156 lines — *not* 157, as Rounds 16 and 17 both stated; `wc -l` returns 156 at `d3db35a`, `0f7ca8a` and `HEAD` alike. Read in full, §1 through §10, cold, without reference to any prior round's characterization of any section)
- `Source_Registry.md` (329 lines; all 212 rows re-parsed by column position, plus the Saturation statement read in full)
- `Source_Acquisition_Manifest.md` (85 lines)
- `lpc_Decision_Log.md` (330 lines; the 2026-09-08 Rounds 15/16/17 entry read in full and checked against the diffs and artifacts it describes)
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines), §7 and §8 read in full and searched line by line for every phrase Doc_02 attributes to or denies of them
- `Review-Artifacts/Doc02_Round15_Review.md`, `Doc02_Round16_Review.md`, `Doc02_Round17_Review.md`, read in full and in order before any other file
- All 19 files vendored at `c803529` (every intake header read in full), plus `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`, `augustine_epistulae-critical_goldbacher-csel57-pars4.txt`, `possidius_vita-augustini_weiskotten1919.txt` and `codex-theodosianus_latinlibrary.txt`; `cic/corpus-map/_staging/`, all 56 atlas files in `cic/corpus-map/`, `cic/texts/INTAKE.md`, `cic/texts/REGISTRY.yaml`, and both engine scripts

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-08 vendoring, did not write the Round 15, 16 or 17 fix passes, and did not write Rounds 1–17.

**Scope, stated plainly.** Two briefs, run together. First: verify, independently and against primary artifacts, whether each of Round 17's twelve findings (M1–M3, L1–L5, C1–C4) is actually closed by the `6fd4973` fix pass — and, since each of the three preceding fix passes introduced at least one new checkable error while fixing what it targeted, look specifically for errors *this* pass introduced. Second: a genuinely cold, whole-document read of §1 through §10 for anything no prior round happened to check, with at least five vendored-file header claims spot-checked beyond Round 17's own sweep. Rounds 15, 16 and 17 were all treated as claims to re-derive, not as authority: where a prior round's own finding text proves wrong and the fix pass has now inherited that error into a live document, that is stated below as a finding against the live document, not excused as inherited.

**Method — what was actually re-derived, not trusted.** `yaml.safe_load` across all 56 atlas files in `cic/corpus-map/` (59 `.yaml` less `AUTHOR-IDS.yaml`, `UNATTRIBUTED.yaml`, `WORKS.yaml`), counting entries, distinct titles, roles and confidences per file; `git show <commit>:cic/corpus-map/latin-pastoral-congregational-christianity.yaml` at all ten revisions `git log --follow` returns, each re-parsed and set-differenced against its predecessor by `(work, source_file)`; a fresh regex parser over all 212 Registry rows extracting all eleven columns by position, with programmatic `|`, `**`, `(`/`)` and backtick balance counts per row; a programmatic direction check on every `§N above` / `§N below` reference in Doc_02 against the section it sits in; a programmatic sweep extracting every quoted string of ≥18 characters from all 19 vendored headers and testing each against that file's own de-hyphenated, whitespace-normalized body, with every apparent miss then chased by hand into the file; whitespace- and punctuation-normalized verification of every primary-source quotation in Doc_02 §1, §2, §4 and §6 against `anf05`, `npnf101`, `npnf104` and `npnf105` directly; a direct count of each review artifact's own `### ` finding headers and verdict line; and both engine scripts run. Nothing was carried forward from Round 15's, 16's or 17's tables, from `lpc_Decision_Log.md`, from the commit message, or from the brief that commissioned this review.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 0 HIGH · 4 MEDIUM · 3 LOW · 3 COSMETIC.**

**All twelve of Round 17's findings are closed, and this is the second consecutive fix pass with no HIGH-severity regression.** Every one was independently re-derived rather than accepted: row 200 is back in §1's inventory and the "Two of these" sentence's antecedents are both present (M1); the misattributed Doc_01 §7 quotation is gone from Doc_02 and returns zero hits across Doc_01 (M2); the Robinson file's header now states Perpetua's assignment, and that statement is exactly right against `tertullian-s-voice.yaml` (M3); the backwards §2 pointer is corrected and **no** `§N above`/`§N below` reference in the document now runs the wrong way (L1); row 56's `**` count is even and **all 212 rows** are now balanced on `**`, parentheses, backticks and pipe count (L2); all three Decision Log figures Round 17 named are now right on independent recount (L3); the Enchiridion appears only in the duplicates bucket, and the eleven-item decomposition is exact against a set-difference of the census's own commit history (L4); row 78's tense is reconciled (L5); the Possidius banner's account of the withdrawn claim is now accurate (half of C1); the OCR disclosure was added at all five files (C2); the Getty-barcode claim is corrected and accurate at both Epistulae files, checked against their actual tails (C3); and §1's double-object sentence and "this Manifest" deixis are both fixed (C4). Both engine scripts exit 0.

**The findings below are of three kinds, and the pattern the Decision Log's own entry names has not stopped.** Four are new text this pass wrote, all four inside sentences written to correct a Round 17 finding: M1 and M2 assert things about Doc_01 §7 and about this document's own prior draft that the committed artifacts falsify, and C2 and C3 misdescribe what they are correcting. Two more are the fix pass editing one sentence of a cell and leaving the adjacent stale one (L1, and the first limb of L3). Two are the same defect class this pass fixed, left standing at sibling sites the pass did not sweep (M3, C1). Two are pre-existing and previously uncaught, surfaced by this round's cold read: M4 dates from the 2026-09-08 revision itself, and L2 has stood wrong since the Round 7 fix pass, through eleven review rounds.

---

## MEDIUM

### M1. The new M2 correction banner in §1 asserts that Doc_01 §7 "does not discuss these corpus-map rows at all" — Doc_01 §7 names them explicitly, in the same sentence that routes them to §8

Doc_02 §1, line 25, written this pass:

> The two entries are kept distinct in the Registry rather than merged — **corrected here (independent review, Round 17, its own M2), from an earlier draft's own false attribution, standing uncaught since the Round 1 fix pass: no quotation resembling "the 256 council is independently attested twice..." appears anywhere in Doc_01, and Doc_01 §7 does not discuss these corpus-map rows at all; Doc_01 §8 item 2 instead names this same duplication among its own open items carried forward to this document, not as an already-settled practice Doc_02 merely follows.**

The first limb is right, independently re-derived: Doc_01 returns **zero** hits for "attested twice," "independently attested," "two different vendored," "two different classifications," "npnf214," "Seven Ecumenical," and "Acts of the Council," and a repository-wide grep for "independently attested twice" returns exactly two hits — Doc_02 line 25 itself, and Round 17's own quotation of the withdrawn text.

The second limb is false. Doc_01 §7 runs from line 144 to line 168 (§8 opens at line 169). Its **World #4 (Donatism)** bullet, at line 166, reads:

> The reading divergence with Donatism's own Step 0 is now resolved for this document's own purposes (§5 above, Cyprian-scoped reading, on record); what remains open is the Optatus placement question (Step 0 §3 B3, §4 item 2(a)) **and the duplicated Council-of-Carthage-under-Cyprian corpus-map rows (Step 0 §4 item 2(b)) — both genuinely Doc_02's, carried forward again at §8 below.**

Doc_01 §7 therefore does discuss the rows: it names them by the same phrase Doc_02 uses, classifies them as open, assigns them to Doc_02, and hands them to §8 — which is where §8 item 2 picks them up. The banner's own conclusion survives (Doc_01 nowhere states a settled practice, and §8 item 2 does carry the duplication as an open item, verified verbatim at Doc_01 line 172), but the specific negative it asserts about §7 is checkably wrong, and it is wrong in a sentence whose whole purpose is to correct a false claim about Doc_01 §7.

Traced rather than assumed: this text is new at `6fd4973` and reproduces Round 17's own M2, which said "*Doc_01 §7 (lines 144–168, read in full) … never mentions the duplicated corpus-map rows.*" The fix pass adopted a review artifact's sub-claim into a live document without re-deriving it — the precise pattern `lpc_Decision_Log.md`'s own entry names as this revision's recurring failure mode.

### M2. The C1 fix inverted the §2 correction record: the Pontius bullet now says the Possidius entry "never asserted the opposite of this bullet in the first place," when at `d3db35a` it asserted exactly that — and the Possidius bullet nine lines below now says the opposite of the Pontius bullet

Doc_02 §2, line 54, current state (the clause is new this pass):

> corrected here, independent review Round 16's own H2, from **an earlier draft of this bullet that asserted only the English translation, not the Latin, reaches this corpus** — refined further, independent review Round 17's own C1, since the withdrawn claim was about Pontius's own Life, not specifically "the Possidius entry," **which never asserted the opposite of this bullet in the first place**

Both halves fail against the committed text they describe.

- **The Possidius entry did assert the opposite.** `git show d3db35a:…/Doc_02_Source_Ecology.md` line 61: *"a different transmission footing than Pontius's *Life*, **which reaches this corpus only via a 19th-century English translation (Migne-based, per the entry above) with no facing Latin at all in the vendored volume**."* That is precisely the negation of this bullet's claim that Pontius's *Life* "also reaches this corpus in Latin." It is the claim Round 16 rated HIGH at its own H2.
- **The earlier draft of *this* bullet asserted nothing of the kind.** At both `c803529` and `d3db35a` the Pontius bullet read only: *"Pontius's own *Life* transmits inside this same volume and edition, 'often counted the earliest Christian biography' per the corpus map's own note."* It made no claim about Latin at all, so it cannot be the draft that "asserted only the English translation, not the Latin, reaches this corpus."

The result is a flat internal contradiction inside one section of one document, both sides edited in this same pass. Line 61's own banner — which *is* now accurate — says the withdrawn false claim was in the Possidius bullet: *"corrected here (independent review, Round 16, its own H2 … ) from an earlier draft's false claim that Pontius's *Life* reaches this corpus only via the English translation, with no Latin available at all."* Line 54 says the Possidius entry never made that claim. One of the two must be wrong, and the committed record says it is line 54.

Round 17's C1 did not ask for this. Its objection was narrower — that the Possidius entry is not in "this same paragraph," and that pointing "from" a live sibling entry reads as though that entry still asserts the opposite, "**which it no longer does**." The fix over-corrected past the finding into a false statement.

### M3. Two vendored-file headers still assert that Manifest requests are open which the 2026-09-08 pass closed — the identical defect class Round 17 rated MEDIUM at its own M3, fixed at the one file Round 17 named and not swept

`cic/texts/cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`, Content note, current state:

> Does NOT include CSEL 3 Pars III (spuria and indices) -- a separate, **still-unacquired volume**; Source_Acquisition_Manifest.md's own **G1 request stays open for that part only**.

CSEL 3 Pars III was vendored on 2026-09-08 as `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`, Registry row 194. Three other artifacts say so in terms that make this header's claim false:

- `Source_Acquisition_Manifest.md` G1 (line 21): *"**Pars III fulfilled 2026-09-08.** … Vendored at `cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`, registered, staged into corpus-map, and logged as Registry row 194."*
- `Source_Registry.md` row 39: *"**The full CSEL 3 edition (Pars I–III) is therefore now vendored in this corpus.**"*
- Doc_02 §9 item 1: *"G1 (Hartel's CSEL 3, complete, rows 191 and 194)."*

`cic/texts/augustine_epistulae-critical_goldbacher-csel57-pars4.txt`, Content note:

> not the full Augustine correspondence Goldbacher edited across CSEL 34/1 (1895), 34/2 (1898), 44 (1904), 57 (1911, this file), and 58 (1923, preface and indices); Source_Acquisition_Manifest.md's own **G4 request stays open for the other volumes**.

CSEL 34/1–2 and CSEL 44 were vendored 2026-09-08 as rows 195 and 196. Registry row 61 states the current position directly: *"**Pars I–IV all now vendored (rows 193, 195, 196, 2026-09-08, independent review Round 15); only Pars V (CSEL 58, praefatio and indices) remains unacquired**."* The Manifest's own closing status update says the same: *"G4 stays open only for CSEL 58 … Parts I through IV (Epistulae 1–270 in full) are all vendored."*

This is the same shape as Round 17's M3 — a vendored file's own header contradicting the Registry and Manifest about acquisition state — which the Decision Log's own new entry records as fixed. It was fixed at the Robinson file, correctly; the two files above were not examined. `cic/texts/INTAKE.md` makes a file's own header the authoritative account of what that file is, so a downstream build thread reading either header is told to go acquire something this world already holds.

### M4. `Source_Registry.md`'s Saturation statement is stale in two independent respects, both dating from the 2026-09-08 revision, and Doc_02 §9 item 6 points a reader at it as "the single authoritative count"

**Limb 1 — the census figure.** `Source_Registry.md` line 293:

> This Registry reflects, **as of this revision**: the existing corpus-map census for this world (**73 works** — parsed directly this session, not estimated — **65 `confidence: assigned` and 8 `provisional`**, from prior vendoring work)

Recomputed from the raw YAML this session: the census now holds **99 works, 87 `assigned` and 12 `provisional`**. The 73/65/8 triple is exact for the 2026-09-01 baseline (`git show 0269b68:` re-parsed: 73 entries, `Counter({'assigned': 65, 'provisional': 8})`) and has been superseded since 2026-09-03. The Registry itself *was* revised on 2026-09-08 — 22 rows appended, eight corrected — so "as of this revision" now reads as current and is false by 26 works. Doc_02 §1 gives the corrected figures in its own opening sentence and explicitly labels 73 as historical ("up from 73, all `tradition`, at this document's own original drafting"), so the two companion documents state the same census as 99 and 73 respectively.

**Limb 2 — the recall-test practice.** `Source_Registry.md` line 295:

> **The ten-item relative-recall test and PRESS question, per CF V7.4's own Doc_02 review requirement, are run once per review round — recorded here rather than only in the review artifacts.**

The round-by-round record immediately below runs `*Round 1*` through `*Round 14*` and stops. Rounds 15, 16 and 17 each ran without it — Round 15 said so explicitly and in terms: *"No fresh ten-item relative-recall test and no PRESS question were run this round. `Source_Registry.md`'s own saturation statement should therefore **not** be incremented for Round 15."* Neither that non-run nor the two after it is recorded in any live document. Doc_02 §9 item 6 (line 136) compounds it:

> The ten-item relative-recall test and PRESS question **have been run once per review round**; results, including exactly how many rounds so far, are recorded in `Source_Registry.md`'s own saturation statement, **the single authoritative count**

This is structurally the same finding Round 16 rated MEDIUM at its own M5 — a disclosed practice that a live document asserts and three consecutive passes did not follow, with the lapse recorded only inside a review artifact. A non-run that exists only in a reviewer's own text is not a disclosed non-run.

---

## LOW

### L1. The L5 fix reconciled row 78's middle sentence and left the closing one, which still describes the volume as an unacquired candidate

Registry row 78 (line 102), Verification Note, in one cell:

> **Now vendored, row 209 (2026-09-08, independent review Round 15)** — closing Manifest G6; the identifier given here (`sanctiaureliaugu36augu`; …) was located by opening Getty-hosted CSEL-Augustine volumes directly by number … but this specific volume's own identifier **had** not been located despite repeated searches across two rounds (Round 6's own M9) **prior to this session — closed 2026-09-08 as stated above, independent review Round 17** — disclosed rather than filled with an invented placeholder; see `Source_Acquisition_Manifest.md` G6. **A real acquisition candidate once located**

The tense repair Round 17's L5 asked for is done and correct. The cell's final clause is not: "A real acquisition candidate once located" states a condition the same cell has just twice said is satisfied. Rows 41 and 90 carry the same residue — row 41 closes *"Flagged as an open acquisition lead rather than a confirmed candidate"* after opening *"**Now vendored, inside row 194**"*, and row 90 closes *"A real acquisition candidate once located"* after opening *"**Now vendored, row 211**"*. Row 40 shows the practice these are measured against: its stale sentence was *edited* to stay true (*"Not vendored **under this row's own number**, and neither located at a specific URL this session"*) rather than prefixed. This is the same one-sentence-at-a-time shape Round 17 named at L5, recurring one clause further down the same cell.

### L2. Doc_02 §3's cross-reference to "`Source_Registry.md` line 6" points at the wrong paragraph — it has been wrong since the Round 7 fix pass, through eleven review rounds

Doc_02 §3, line 75:

> **The Registry's own checkpoint rule (`Source_Registry.md` line 6)** requires a row for a source named "in support of a specific claim"

`Source_Registry.md` line 6 is the **Disclosed-placement rule**: *"**Disclosed-placement rule (stated once here rather than as row-range prose at each affected row, Round 7's own L1/L2 …)**: a handful of rows (48, 52, 60 among them) sit physically out of numeric order…"*. The checkpoint rule is at **line 8**: *"Every source named in `Doc_02_Source_Ecology.md` in support of a specific claim has a corresponding row below, per the Registry's own checkpoint rule."* The quoted phrase Doc_02 attributes to line 6 is in line 8.

Traced rather than assumed: `git log -S` puts the "line 6" reference in `252a0dd` (Round 2 fix pass, 2026-09-01), where it was **correct** — at `9adbe66~1` the checkpoint rule is line 6. The Round 7 fix pass (`9adbe66`, 2026-09-02) inserted the Disclosed-placement rule above it, pushing the checkpoint rule to line 8 and leaving Doc_02's pointer behind. It is the only `line N` reference anywhere in Doc_02, and the irony is exact: the paragraph that displaced it exists because this project had twice watched row-range prose go stale, and says so in its own text.

### L3. The Decision Log's Round 16 paragraph now says one applied fix failed, in the same sentence that names four HIGH-severity regressions — and its account of what Round 17 corrected over-counts

`lpc_Decision_Log.md` line 324, as edited this pass:

> **Round 16** … found **fifteen of the sixteen applied fixes held** — several exactly … **But it found four HIGH-severity regressions the fix pass itself introduced:** [four named]

The denominator was corrected this pass (seventeen → sixteen, which is right: Round 15 made 17 findings and 16 fixes were applied). The numerator was not re-derived. Fifteen of sixteen holding means exactly one did not, which the same sentence then contradicts by naming four regressions, and which Round 16's own next paragraph contradicts more fully: *"**Two fixes** were applied at one of the two sites the review named … **Four fixes** introduced a *new* checkably-false claim the build thread did not have before (H2, H4, M1, M3, L6)."* On Round 16's own account at least six of the sixteen did not hold cleanly. The pre-fix "fifteen of the seventeen" was already wrong; narrowing the denominator without touching the numerator made the arithmetic tighter and the claim further from Round 16's own text.

A second, smaller figure in the same entry (line 326): *"It also corrected this entry's own count of Round 16's findings (eighteen, not seventeen, **both instances now fixed above**)."* The diff `0f7ca8a..6fd4973` shows only **one** instance corrected from seventeen to eighteen ("All seventeen → eighteen of Round 16's own findings"); the other seventeen → sixteen change concerned Round 15's *applied fixes*, a different quantity about a different round. The parallel clause for Round 15 — "seventeen made, sixteen fixed, both now fixed above" — is right.

---

## COSMETIC

### C1. The C2 fix added the OCR-quotation disclosure at the five files Round 17 named; nine further files in the same nineteen carry the identical defect, including the Harnack file already fixed for it at Round 16

Every quoted string of ≥18 characters in all 19 headers was tested against its own file's de-hyphenated, whitespace-normalized body, and each apparent miss chased into the file by hand. Beyond the five files this pass disclosed, the same normalize-the-quotation practice stands undisclosed at:

| file | header quotes | file actually reads |
|---|---|---|
| `harnack_…lat-deu_1913` | "Der im folgenden dargebotene Text ist der **Hartels**." | `ist der Harteis.` (l. 383) |
| `harnack_…lat-deu_1913` | "…schien mir erwünscht, **weil** es eine solche m. W. bisher nicht gibt" | `schien mir er-` / `ll wünscht, w^eil es eine solche` (ll. 389–90) |
| `augustine_epistulae-1-123-…csel34` | "**opere perfecto subsequetur praefatio**" | `OPERE PERFECTO SVBSEQYETYR PRAEFATIO.` (l. 94) |
| `augustine_doctrina-christiana-enchiridion-…bruder1838` | "ex **Benedictinorum recensione**"; "S. AURELII AUGUSTINI **ENCHIRIDION AD LAURENTIUM** SIVE…" | `BENEDICTINORUM RECENSIONE` (l. 30, caps); `ENCHIRIDION AD LAURENTIUxM.` / `ENCHIRIDION AD LAURENTIUM` (ll. 25, 8978) |
| `perpetua-scillitan-martyrs-…robinson1891` | "Praesente bis et Claudiano consulibus, **XVI** Kalendas Augustas…" | `consulibus, xvI Kalendas Augus-` (l. 7375) |
| `vonsoden_prosopographie-…1909` | "**DIE PROSOPOGRAPHIE** DES AFRIKANISCHEN EPISKOPATS ZUR ZEIT CYPRIANS. VON HANS VON SODEN." | `DIP^ PROSOPOGKAPHIE` … `VON HANS VON SODEN i).` (ll. 13–18) |
| `delehaye_…fra_1921` | "**Histoire, tradition, litterature.**" | `HISTOIRE, TRADITION, LITTERATURE` (l. 17760) |
| `monceaux_…tome1_1901` / `tome2_1902` / `tome3_1905` | "**Angers. -- Imprimerie Orientale de A. Burdin et Cie.**" | `ANGERS. — IMPRIMEHIE ORIENTALE DE A. BURDIN ET Cl°.` / `ANGERS. — iMPiilMEiiiF. ORIENTALE DE A. BDRDIN ET I '".` / `ANGBHS. — IMPRIMERIE ORIENTALE DE A. BU RIU N ET Cle.` |

Each of these headers carries the same "nothing else altered, **no OCR error corrected**" sentence that made this a finding at Harnack (Round 16 C3) and at the five files this pass fixed (Round 17 C2). The Harnack case is the sharpest: its Provenance note now says one quotation is *"quoted here as it actually reads, corrected from an earlier draft that silently normalized it, per independent review's own C3 finding, Round 16,"* while two quotations in its own Content note six lines below remain silently normalized — including `Harteis` → `Hartels`, which is the name of the editor whose text Harnack is reproducing. As at Round 17, the substance is confirmed present in every case; this is about the quotations, not the claims they support. Registry row 204's Verification Note carries the same normalized Scillitan formula ("XVI Kalendas Augustas") as the file it describes.

### C2. The disclosure clause the fix pass wrote describes letter-level OCR confusion, which does not cover the largest variant in one of the five files it was written for

The clause added to all five files reads, identically:

> Note (independent review, Round 17): quotations elsewhere in this header's own Content note are given in standard/readable spelling; the file's own OCR carries **the usual letter-level confusions (V/Y, C/G, u/n, and similar)** at some of the same points, so a reader matching a quoted phrase against the file directly should expect **minor character-level variants**, not a discrepancy in substance.

Accurate and adequate at four of the five, checked one variant at a time: `Amen`/`Arnen`, `excellentissimus`/`cxcellentissimus`, `V. kl.`/`Y. kl.`, `Iuliani`/`luliani`, `quae`/`qnae`, `uulgo`/`iiiilgo`, `Honorii`/`Honmorii` are each a letter-level substitution or insertion. It does not describe the Enarrationes file's own largest case: the header's "PATROLOGIAE LATINAE TOMUS XXXVI" stands in the file as **`PATRO LOGI Ai LATINJE TOMUS XXXYI.`** (l. 13) — one word broken into three tokens, not a character confusion. A reader following the disclosure's own instruction ("expect minor character-level variants") would not find that string by the search it authorizes.

### C3. §1's restored row-200 entry misdescribes where the sentence that needs it sits

Doc_02 §1, line 29, the M1 fix:

> On Christian Doctrine and the Enchiridion (Bruder's 1838 Tauchnitz text, row 200 — restored here, independent review Round 17's own M1, after the Round 15 fix pass dropped it from this list while adding the "Two of these" sentence **two clauses later** that still names it)

The "Two of these" sentence is not two clauses later. Three further list members intervene — *"the Expositions on the Psalms (Migne's PL 36–37, row 201); the Retractationes (Knöll's CSEL 36, row 209 …); and the Code of Canons of the African Church (Bruns's 1839 edition, row 202)."* — and the sentence then begins after a full stop, as its own sentence rather than a clause. This is the same class Round 17 rated COSMETIC at its own C1: a correction banner whose account of the correction does not match the text.

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**M1 — row 200 restored, and the "Two of these" sentence's antecedents both present.** §1's inventory now runs to eight groups: the whole Cyprianic corpus (rows 191, 194); the Confessions (197); the general and Jerome-cluster correspondence (195, 196, 193); City of God (198–199); **On Christian Doctrine and the Enchiridion (200)**; the Expositions on the Psalms (201); the Retractationes (209); and the Code of Canons (202). The sentence that follows — *"**Two of these are the Maurist text, not a modern critical edition …:** On Christian Doctrine and the Enchiridion (… row 200 …) and the Expositions on the Psalms (… row 201 …)"* — now has both of its members inside the list it points into. §2's parallel inventory carries the same nine items with the same six per-edition labels, so the cross-sectional disagreement Round 17 found is closed. **Correct and complete**, subject only to C3's misdescription of the fix.

**M2 — the misattribution is gone, and Doc_01 §8 item 2 was read directly rather than through any round's account.** Doc_01 line 172, in full: *"2. **The Donatism boundary's remaining open items (§7 above; Step 0 §4 item 2).** The Optatus placement question (re-home, hold, or double-place); **the duplicated Council-of-Carthage-under-Cyprian corpus-map rows**; the Article 23 reconstruction of Donatism as this world's own internal rival."* The section heading is "Open items carried forward to later steps," and Doc_01 §8 contains twelve such items. So the banner's substantive conclusion — that Doc_01 carries this as an open item rather than a settled practice Doc_02 follows — is right; only its §7 negative fails (M1 above). Independently re-verified in the corpus map: the `npnf214` entry's note reads verbatim *"Donatism is included as shared ancestry rather than heresiology: the Donatists claimed this council's baptismal doctrine as their patrimony, so it is tradition claimed by both sides, not description of either. Provisional on that double placement,"* and rows 4 and 42's `author`/`confidence` values are as §1 states (`cyprian`/`assigned`, `council-of-carthage-under-cyprian`/`provisional`).

**M3 — the Robinson header, checked against the atlas rather than against the fix's own account.** The header now reads: *"Corrected here (independent review, Round 17): the Passio S. Perpetuae is NOT unassigned -- it is already assigned to `tertullian-s-voice` (Mark's own 2026-08-26 ruling), and this file's own vendoring adds a second entry to that same world's corpus-map bucket, `source_file: perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`, `role: tradition`, `confidence: assigned`."* `tertullian-s-voice.yaml` re-parsed: two entries for *The Passion of the Holy Martyrs Perpetua and Felicitas*, `author: passion_of_perpetua`, `role: tradition`, `confidence: assigned`, from `anf03_tertullian.xml` and from this file — every field the header names is exact. The zero hits for "not yet assigned" in the file are confirmed. **Correct and complete.**

**L1 — every cross-reference direction checked, not only the one Round 17 named.** All 67 `§N above` / `§N below` references in Doc_02 were direction-checked programmatically against the section each sits in. **None fails.** The single flagged candidate is a regex artifact (§2 line 59's *"the Megalius/primate-of-Numidia identification **Doc_01 §5** names (**§1 above**)"*, where the number belongs to Doc_01 and the direction word to §1, which is correctly above §2). The M4-correction sentence now reads *"the passage this document's own **§2 below** quotes (corrected from "above," independent review Round 17's own L1, since §2 follows §1),"* and sits in §1, which ends at line 29 with §2 opening at line 31.

**L2 — Registry table integrity, recomputed row by row.** All 212 rows re-extracted by column position: numbers 1–212 complete, **no gap, no duplicate**; **every row parses to exactly 11 columns / 12 pipes**; **every row has an even `**` count**, balanced parentheses, and balanced backticks. Row 56 is at 16 and balanced, so the orphaned closing marker is gone and the enumeration and rights paragraph following it render plain as intended. `grep -c "****"` returns **0** in both `Source_Registry.md` and `Doc_02_Source_Ecology.md`, and the same three balance checks pass on every line of Doc_02, `lpc_Decision_Log.md` and `Source_Acquisition_Manifest.md` as well.

**L3 — the Decision Log's three named figures, recounted from the artifacts.** Counted directly: `Doc02_Round15_Review.md` has **17** `### ` finding headers (H1–H4, M1–M6, L1–L5, C1–C2) and a verdict line reading "4 HIGH · 6 MEDIUM · 5 LOW · 2 COSMETIC"; `Doc02_Round16_Review.md` has **18** (H1–H4, M1–M5, L1–L6, C1–C3), verdict "4 HIGH · 5 MEDIUM · 6 LOW · 3 COSMETIC"; `Doc02_Round17_Review.md` has **12** (M1–M3, L1–L5, C1–C4), verdict "0 HIGH · 3 MEDIUM · 5 LOW · 4 COSMETIC". The entry's "Of the seventeen findings Round 15 made, 16 (H1–H4, M1–M6, L1–L5, C1) were fixed in place; the seventeenth, C2 … was deliberately left" is right and its enumeration sums to 16. "All eighteen of Round 16's own findings (H1–H4, M1–M5, L1–L6, C1–C3)" is right and sums to 18. "All twelve of Round 17's own findings (M1–M3, L1–L5, C1–C4)" is right and sums to 12. The census-pass figure is right on independent re-derivation: the file's own history is 73 (`0269b68`, 09-01) → 74 (`cf1033e`, 09-03) → 75 (`97419d7`) → 76 (`7ead600`) → 77 (`4911c02`, all 09-05) → 99 (`c803529`, 09-08), so "five passes (four before this revision, one on the day itself)" is exact. Only the two figures at L3 above fail.

**L4 — the eleven, set-differenced against the census's own baseline rather than adopted.** The 2026-09-08 additions are **22** (14 `tradition`, all Latin/Greek originals; 8 `context`), nothing removed. Exactly two are exact-title duplicates of baseline titles — `The Enchiridion (On Faith, Hope, and Love)` (from `augustine_doctrina-christiana-enchiridion-lat_bruder1838.txt`) and `The Passion of the Scillitan Martyrs` (from the Robinson file) — and the Bruder file *separately* supplies `On Christian Doctrine (De Doctrina Christiana), Books I-IV`, a differently-worded second witness to the baseline's `On Christian Doctrine`. The fix's bracketed correction is therefore right on both limbs. The nine added today are City of God ×2, the Confessions, Epistulae 1–123, Epistulae 124–184A, the complete Enarrationes, De Doctrina Christiana, the Codex Canonum, and the Vita Caecilii Cypriani — nine as written and enumerated; the two earlier are Hartel CSEL 3 Pars I–II and Goldbacher CSEL 57 Pars IV. The Retractationes, the Acta Proconsularia and the Opera Spuria are correctly *not* in the eleven: the 73-entry baseline (re-parsed at `0269b68`, 73 entries, 73 distinct titles, all `tradition`) contains none of them.

**C3 — the Getty barcode, checked against both files' actual tails.** `augustine_epistulae-1-123-lat_goldbacher-csel34.txt` ends `Explicit epistula sancti hieronimi ad agustinum K EXPLICIT N` / `GETTY CENTER LIBRARY` / `3 3125 00640 3113 ^`, so its new note — *"the back-cover Getty Center Library barcode ("GETTY CENTER LIBRARY" / call number) was NOT fully stripped -- it survives as the file's own last content lines, after the final letter's apparatus"* — is exact, including the call number it quotes. `augustine_epistulae-124-184a-lat_goldbacher-csel44.txt` ends with two bare `.` lines, `getty center library`, `1`; its note makes the same disclosure without quoting, correctly. The third file Round 17 named as carrying the identical Provenance sentence, `augustine_retractationes-lat_knoll-csel36.txt`, was checked and correctly left alone: `grep -i "getty center library"` matches only its own header line, and its body genuinely ends after the closing indices with unrelated scan noise. **Correct and complete at all three.**

**C4 — both halves, and the underlying facts.** §1 now reads *"row 88 (the Codex Theodosianus, project-lead-supplied outside **the Manifest's own numbered list**, per `Source_Acquisition_Manifest.md`'s own record — corrected from "this Manifest," independent review Round 17's own C4, since Doc_02 is not the Manifest) was added 2026-09-02, three days before row 191 — **row 88, not row 191, is therefore this world's actual first Latin-language vendored source**."* The string "this Manifest" now survives in Doc_02 only inside that correction banner, quoting the withdrawn text. The double-object reading is gone: the assertion is now made in its own independent clause. Both underlying facts re-derived: row 88's Added column reads 2026-09-02 and row 191's 2026-09-05 (three days), and the census took the Codex Theodosianus at `cf1033e` before Hartel's CSEL 3 at `97419d7`. The 2026-09-01 baseline is all-ANF/NPNF English, so "no Latin exception of any kind existed yet" holds.

**Census and comparator arithmetic, recomputed across all 56 atlas files.** `latin-pastoral-congregational-christianity.yaml`: **99 entries, 97 distinct titles, `Counter({'tradition': 90, 'context': 9})`, 88 distinct titles inside the tradition set, exactly two duplicate titles (both inside that set, so 90 − 2 = 88 reconciles), `Counter({'assigned': 87, 'provisional': 12})`.** Comparators re-derived on each measure separately: 99 raw entries against **68** (`post-apostolic-house-church.yaml`), 97 distinct titles against 67, 90 `tradition` entries against **59** (`alexandria-catechetical.yaml` and `post-apostolic-house-church.yaml`, tied), 88 tradition-distinct against 59. lpc leads on all four, so §1's "on every count attempted" holds and both stated comparators (68, 59) are exact. The nine `context` entries are Delehaye 1921, Harnack 1913, Monceaux I/II/III, von Soden 1904, von Soden 1909, Prosper (Mommsen 1892) and the Codex Theodosianus — **seven of the nine modern (1901–1921) secondary scholarship**, as §1 says.

**Every primary-source quotation in Doc_02, tested against the vendored volumes rather than against any prior round's certification.** Verified verbatim, whitespace- and punctuation-normalized: in `anf05` — *"your suffrage and God's judgment,"* *"ancient venom,"* *"neither does any of us set himself up as a bishop of bishops,"* *"every bishop, according to the allowance of his liberty and power, has his own proper right of judgment,"* *"by the judgment of God and the favour of the people, he was chosen to the office of the priesthood and the degree of the episcopate while still a neophyte,"* the *"household companions"* phrase §4 rests its Pontius-ordination negative on, and both `Celerinus to Lucian` / `Lucian Replies to Celerinus` headings; in `npnf104` — *"from the Council and the epistles of Cyprian, to the effect that Christ's baptism may not be given by the hands of heretics"* and *"who strive to defend themselves by the authority of the most blessed bishop and martyr Cyprian"*; in `npnf101` — *"of historical value, as embodying the rules of nunneries belonging to the Augustinian orders,"* plus the `To Albina` and `To the Nuns` letter headings; in `npnf105` — **18** `Extract from Augustin's Retractations` sections, so §1's "further such excerpts" holds. In the corpus map: the Scillitan note's *"the direct root of the Carthaginian congregational tradition"*, the Optatus hedge *"because the entry choice is inferred from region and date — Mark may prefer another Latin home for a Numidian polemicist"*, and `donatism.yaml`'s own Optatus note *"Assigned twice with different roles, deliberately"* (`role: context`, `confidence: assigned`) — all exact, so §1's Optatus paragraph and §10's escalation reasoning both rest on what the files say.

**Cross-document row and section references.** Every `row`/`rows` number cited anywhere in Doc_02 falls inside 1–212 and exists; **every row number 191–212 is referenced**, so Round 15's L4 gap stays closed. Every Registry row label §2's "not yet closed" list attaches was checked against the row itself: 19 = Sermons, 22 = anti-Manichaean, 23 = anti-Pelagian ("thirteen works," matching §1's corrected count), 15/18/25 = catechetical / creedal / *De Trinitate*-and-related, 21 = Tractates on John and related exegetical, 13–14 = anti-Donatist with row 13 at Confidence A — so Round 16's C2 labelling defect stays fixed and no row is mislabelled. §5's rows 63 (Marec) and 82 (Ennabli) are both Confidence C as stated; §9 item 3's rows 33–35, 37, 38 and 30–32 and 46–47 all match their stated verification states; §3's five vendored secondary works across seven rows (205, 206–208, 210, 211, 212) are all Type S / Confidence C as stated; row 5's own note records **four** of ten Cyprianic minor treatises as Tertullian-dependent, matching §2's "at least four." Doc_01 §8 items 1–5 exist and items 6–12 are directed elsewhere (item 10 explicitly to Doc_04), so §9 item 11's "items 1–5" scoping holds.

**Row 204's two columns, and the Excluded set.** Boundary Status now takes exactly two values across all 212 rows — `Native` (**207**) and `**Excluded**` (**5**) — with no hybrid. Row 204's Boundary Status is `**Excluded**` (both portions) and its Exclusion Reason agrees. Its "mirroring row 28 exactly" claim was checked at the level it actually asserts: the corpus map carries both Scillitan entries as `role: tradition`, `confidence: provisional`, which is what row 204's own Verification Note says it mirrors — not the Registry Confidence column, where row 28 is C and row 204 is B.

**Internal arithmetic across the document.** 391 − 258 = **133** (§7's gap); 430 − 246 = **184** (§6's span); 17 + 11 + 2 + 138 = **168** letters (§1's cluster split, each figure confirmed in `_staging/npnf101_augustine-confessions-letters.yaml`, and the Donatist and Pelagian clusters confirmed `role: context` in `donatism.yaml` and `pelagianism.yaml` and absent from lpc's own census); §9 item 1's eight closed G-items match the Manifest's own eight and are listed identically in both. The status line's own sequences were recounted from the fourteen artifacts' verdict lines: HIGH **6/2/1/1/0/0/0/0/0/0/0/0/0/0** and MEDIUM **15/6/7/4/9/9/2/2/1/2/1/1/1/0** — both exact.

**Vendored-file header content claims, spot-checked well beyond Round 17's own five.** Checked this round and found accurate in substance: the Hartel Pars III file's three-component sequence (spuria → `VITA CAECILII CYPRIANI` at l. 40258 → `ACTA PEOCONSVLARIA` at l. 41413, with printed page marks CXII and CXIII inside the Acta, confirming §9 item 8's and row 41's "pp. CX–CXIV, immediately following the Vita"); the Confessions file (`Magnus es, domine, et laudabilis ualde`, `Liber Tertius Decimus`, Index Scriptorum); the Retractationes file (Praefatio, both books, closing indices, and its Getty claim, above); the Bruder file (both works present in sequence, the Enchiridion's separate title block at l. 8978, and zero hits for "CSEL," "Green," "1963"); the CSEL 34 file (Ep. 123's manuscript explicit and the deferred-praefatio line, both present); the CSEL 57 Pars IV file (`EP. CLXXXV— CCLXX` at l. 34, heading `CLXXXV.` at l. 44 — so Round 16's Letter-185 correction remains true at both ends); the von Soden *Prosopographie* article's own opening and its `87 Yotanten des Konzils von Karthago am 1. September 256` line; the Delehaye chapter range; the three Monceaux volumes' own stated contents. The only header **content** defects found are M3's two stale acquisition claims; the rest are accurate in substance, with the quotation-fidelity caveat at C1.

**Engine scripts, both re-run this session.** `python cic/engine/texts_registry.py` → **exit 0**, *"OK: every vendored file has a header-verified rights line (public domain, or a recognized open licence), an ENTRIES row, and no ENTRIES row points at a missing file"*; 88 vendored files, 23 non-English sources, `cic/texts/` at 211 MB (30% of the 700 MB planning trigger). `python cic/engine/corpus_map_merge.py --check` → **exit 0**, *"528 distinct work(s) → 788 assignment(s) across 56 Atlas entry(ies) [check only, nothing written]"*.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the fix pass and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** M3 concerns two vendored files' headers contradicting this world's own Manifest and Registry about acquisition state; the corrective is to bring each header into line with a fulfillment record that already exists. M4 concerns a stale figure and a lapsed disclosure inside this world's own Registry. Neither decides anything for another world. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing here changes `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022, or any governing document. M4's second limb is a finding that a stated practice was not followed and the non-run was not disclosed outside a review artifact, not that the practice changed. C1 and C2 are findings that headers do not match their files, not that the header convention changed. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round disagrees with Round 17 on one narrow point of fact — its M2's sub-claim that "Doc_01 §7 does not discuss these corpus-map rows at all," which Doc_01 §7 line 166 falsifies, and which the fix pass has now carried into Doc_02 (M1 above). It also disagrees with Rounds 16 and 17 on Doc_02's line count (156, not 157), a figure nothing depends on. Both were closed here by reading the primary artifact directly rather than preferring any round's account. Neither requires the project lead. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

Doc_02's status line and §10, and `Source_Registry.md`'s status line, still describe the Round 14 disposition of 2026-09-02, still read "Fourteen independent adversarial review rounds" over the sequence "(Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0)", and still point a reader to "`Doc02_Round1_Review.md` through `Doc02_Round14_Review.md`" while Doc_02 now carries in-text attributions to Rounds 15, 16 and 17, and `Source_Registry.md` carries attributions to Rounds 15, 16 and 17 (counted: 8, 4 and 1 mentions respectively). That is reported here as observed, checkable state, on the same footing Rounds 16 and 17 reported it — and it is the same staleness M4's second limb documents inside the Saturation statement, where the round-by-round record stops at Round 14. Whether and how those lines should change, and what disposition follows from this round's counts, is **not assessed here**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition. This review supplies only the input that rule takes: a finding count and a findings list.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 0 HIGH · 4 MEDIUM · 3 LOW · 3 COSMETIC.**
