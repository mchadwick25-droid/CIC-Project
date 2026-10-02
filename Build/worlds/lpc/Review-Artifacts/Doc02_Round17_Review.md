# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 17 Independent Adversarial Review — scoped to verifying the Round 16 fix pass

**Documents reviewed (committed state — `git status --porcelain` clean at `0f7ca8a`, "lpc: fix Doc_02 revision per Round 16 independent adversarial review", 2026-09-08 06:44:52 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_02_Source_Ecology.md` (157 lines; §1 and §2 read in full, fresh, without reference to any prior round's characterization of them)
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Source_Registry.md` (329 lines; 212 rows, all re-parsed by column position)
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Source_Acquisition_Manifest.md` (85 lines)
- `World-Builds/Latin-Pastoral-Congregational-Christianity/lpc_Decision_Log.md` (328 lines; the new 2026-09-08 Rounds 15/16 entry read in full and checked against the diffs it describes)
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines), searched in full for every phrase Doc_02 §1 and §2 attribute to it
- `Review-Artifacts/Doc02_Round15_Review.md` and `Doc02_Round16_Review.md`, read in full and in order before any other file
- All 19 files vendored at `c803529`, their intake headers, `cic/corpus-map/_staging/`, all 56 atlas files in `cic/corpus-map/`, `cic/texts/INTAKE.md`, `cic/texts/REGISTRY.yaml`, and `cic/engine/texts_registry.py`

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-08 vendoring, did not write the Round 15 or Round 16 fix passes, and did not write Rounds 1–16.

**Scope, stated plainly.** This round's brief was to verify, independently and against primary artifacts, whether each of Round 16's eighteen findings (H1–H4, M1–M5, L1–L6, C1–C3) is actually closed by the `0f7ca8a` fix pass — and, given that each of the two preceding fix passes introduced at least one new checkable error while fixing the ones it targeted, to look specifically for errors this third pass introduced. It also carried a fresh, from-scratch read of §1 and §2 for defects no prior round happened to name. Rounds 15 and 16 were both treated as claims to re-derive, not as authority: where either round's own finding text or count proves wrong, that is stated below rather than inherited.

**A count correction stated up front, because everything downstream depends on it.** The task that commissioned this review, the `0f7ca8a` commit message, and `lpc_Decision_Log.md`'s new entry all describe Round 16 as having made **17** findings. Counted directly from `Doc02_Round16_Review.md` — eighteen `### ` finding headers, and that document's own verdict line reading "**Findings: 4 HIGH · 5 MEDIUM · 6 LOW · 3 COSMETIC**" — Round 16 made **18**. Round 15 made 17 (4+6+5+2), of which 16 were fixed and one (C2) deliberately left. Those are the figures this round verified against, and the discrepancy is itself a finding (L3 below).

**Method — what was actually re-derived, not trusted.** Every figure here was recomputed this session from the raw artifact. `yaml.safe_load` across all 56 atlas files in `cic/corpus-map/` (59 `.yaml` files less `AUTHOR-IDS.yaml`, `UNATTRIBUTED.yaml`, `WORKS.yaml`), counting entries, distinct `work:` titles, and role composition per file; `git show <commit>:cic/corpus-map/latin-pastoral-congregational-christianity.yaml` at all six historical revisions, each re-parsed and set-differenced against its predecessor by `(work, source_file)` key; a fresh regex parser over all 212 Registry rows extracting all eleven columns by position, plus programmatic `(`/`)` and `**` balance counts per row; a programmatic sweep extracting every quoted string of ≥18 characters from all 19 vendored files' own intake headers and testing each against that file's own de-hyphenated, whitespace-normalized body; the same sweep run over Doc_02 §1–§2's quotations against the Registry, Doc_01, the Manifest, the corpus map and `INTAKE.md`; a programmatic direction check on every `§N above` / `§N below` cross-reference in Doc_02 against the section it sits in; and both engine scripts run. Nothing was carried forward from Round 15's or Round 16's tables, from the Decision Log, from the commit message, or from the commissioning brief.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 0 HIGH · 3 MEDIUM · 5 LOW · 4 COSMETIC.**

**All eighteen of Round 16's findings are closed, and this is the first fix pass in this sequence that introduced no HIGH-severity regression.** The four HIGH fixes are correct and complete on independent re-derivation: §2 no longer calls rows 200/201 critical editions and now states the CSEL/Maurist distinction explicitly at each of six named rows (H1); the Pontius and Possidius *Transmission History* bullets are both accurate about row 194 and mutually consistent (H2); the 90/88 census pair, the 68 and 59 comparators, the two duplicates, the nine `context` entries and the seven modern secondary works among them were each recomputed from raw YAML and are exact (H3); row 88's priority over row 191 and the four-earlier-passes count are right at both sites, with the non-Manifest addition correctly distinguished from the G-items (H4/M1). The row-196 Letter 185 error is corrected at all four artifacts and the substantive claim independently verified in both files (M2); row 204's two columns now agree (M3); the Retractationes/Acta distinction is drawn correctly and both halves verified in the NPNF volumes (M4); a Decision Log entry now exists covering both passes (M5). All twelve previously-touched Registry rows still carry exactly 12 pipes, no `****` survives in either document, and both engine scripts exit 0.

**The findings below are of three kinds.** Two are defects the Round 15 fix pass created and Round 16 did not catch, still standing (M1, L5). One is a long-standing misattributed quotation in §1 that sixteen rounds have passed over, surfaced by this round's fresh read (M2). The remainder — L1, L2, L3, L4, C1, C2 — are new, introduced by this pass while fixing something else, which is the same recurrence the Decision Log's own new entry names as this revision's governing pattern.

---

## MEDIUM

### M1. §1's inventory of newly-vendored Latin second witnesses drops row 200 entirely, and the very next sentence's "Two of these" then names row 200 as one of the two — §2's parallel inventory does include it, so the two sections' inventories disagree

§1 (line 29) enumerates what is now vendored:

> Latin-language second witnesses are now vendored for: the whole Cyprianic corpus … (Hartel's CSEL 3, complete, rows 191 and 194); Augustine's Confessions (Knoll's CSEL 33, row 197); the full run of his general and Jerome-cluster correspondence (… rows 195, 196, 193 …); City of God (Hoffmann's CSEL 40, both parts, rows 198–199); the Expositions on the Psalms (Migne's PL 36–37, row 201); the Retractationes (Knöll's CSEL 36, row 209 …); and the Code of Canons of the African Church (Bruns's 1839 edition, row 202). **Two of these are the Maurist text, not a modern critical edition …:** On Christian Doctrine and the Enchiridion (Bruder's 1838 Tauchnitz printing of the Maurist text, row 200 …) and the Expositions on the Psalms (Migne's 1861 printing, row 201, same disclosure) are both pre-critical texts…

Row 200 is not in the list. "Two of these" therefore has a false antecedent for one of its two members, and the document's own inventory of the day's Latin vendoring omits one of the nineteen files.

Traced by diff rather than assumed: at `c803529` the list **did** contain it — *"City of God (Hoffmann's CSEL 40, both parts, rows 198–199); **On Christian Doctrine and the Enchiridion (Bruder's 1838 Tauchnitz text, row 200)**; the Expositions on the Psalms, complete (Migne's PL 36–37, row 201)…"*. The Round 15 fix pass (`d3db35a`) deleted that list member in the act of adding the "Two of these are the Maurist text" correction, and neither Round 16 nor this pass restored it.

The inconsistency is cross-sectional, not merely local. §2's corresponding list, rewritten this pass for H1, **does** carry row 200: *"…the Expositions on the Psalms (Migne PL 36–37, row 201, the 1861 Maurist printing, **not** a modern critical edition), and On Christian Doctrine and the Enchiridion (the Tauchnitz/Maurist text, row 200, likewise **not** a modern critical edition)."* A reader taking §1's list as this document's inventory of what the 2026-09-08 vendoring produced gets eight items where §2 gets nine.

### M2. §1 attributes to Doc_01 §7 a direct quotation about the duplicated 256-council entries that appears nowhere in Doc_01 — and Doc_01 §7 does not discuss those entries at all

§1 (line 25):

> The two entries are kept distinct in the Registry rather than merged, **per Doc_01 §7's own established practice for this exact council** ("The 256 council is independently attested twice, from two different vendored volumes with two different classifications... kept... distinct")

Doc_01 was searched in full (302 lines) this session. Zero hits for **"attested twice"**, zero for **"two different vendored volumes"**, zero for **"two different classifications"**, zero for **"npnf214"**, zero for **"Seven Ecumenical"**, zero for **"Council of Carthage under Cyprian"**, zero for **"Acts of the Council"**. Doc_01 §7 (lines 144–168, read in full) is the World Continuity & Distinction section: it discusses Tertullian's vocabulary, the World #6/#9/#4 boundaries and the Antiochene contrast, and never mentions the duplicated corpus-map rows. A repository-wide `grep` for "attested twice" and for "two different classifications" returns exactly one hit each — Doc_02 line 25 itself.

What Doc_01 *does* say about the matter is the opposite of an established practice: §8 item 2 lists *"the duplicated Council-of-Carthage-under-Cyprian corpus-map rows"* among the **open items carried forward to later steps**, i.e. as work Doc_02 owes, not as a determination Doc_01 already made and Doc_02 is following.

This is the same defect class Round 15 rated MEDIUM at its own M1 (a characterization attributed to Doc_01 §2 that Doc_01 does not contain). It is pre-existing rather than a fix-pass regression — `git log -S` puts it in commit `4796ee3`, the Round 1 fix pass — and it has stood through sixteen review rounds. The two other quotations in the same sentence were checked and **are** exact: the corpus map's own note on the `npnf214` entry reads verbatim *"Donatism is included as shared ancestry rather than heresiology: the Donatists claimed this council's baptismal doctrine as their patrimony, so it is tradition claimed by both sides… Provisional on that double placement,"* and both rows' `author`/`confidence` values are as stated.

### M3. The M2 fix corrected the false Letter-185 claim at four artifacts; a structurally identical false claim in another of the same nineteen files' own headers is left standing, and that file's own Registry row already records it as false

`cic/texts/perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`, Content note, current state:

> The Passio S. Perpetuae **is not yet assigned to any world's own corpus map**; this file makes it available as a second-witness candidate for whichever world's build thread judges it relevant, without this file itself asserting that assignment.

Independently checked by re-parsing every atlas file: `tertullian-s-voice.yaml` carries **two** entries for *The Passion of the Holy Martyrs Perpetua and Felicitas* — one from `anf03_tertullian.xml`, and one whose `source_file` is **this very file**, `perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`, `role: tradition`, `confidence: assigned`. The work was assigned before this file was vendored, and this file is now assigned there too.

Both of the other two artifacts describing this file already say so, in terms that name the header's claim as the error:

- Registry row 204, Verification Note: *"Perpetua's Passion (pp. 60–95) is **already assigned** — to `tertullian-s-voice`, per Mark's own prior ruling — **contrary to this file's own accompanying task brief, which described it as "not yet assigned to any world's own corpus map"; independently checked before this row was written and found already assigned, corrected here rather than silently re-asserted.**"*
- `cic/corpus-map/_staging/perpetua-scillitan-martyrs-lat-grc_robinson1891.yaml`: *"(Contrary to this file's own accompanying task brief, which described Perpetua's Passion as 'not yet assigned to any world's corpus map' — independently checked before writing this entry and found already assigned, per the ruling cited above…"*

So the build thread identified the claim as false, corrected it in the Registry and in the staging file, and left the identical sentence standing in the vendored file's own header — the exact divergence Round 16's M2 found for CSEL 44 and this pass fixed there, at all four sites, in the same commit. A downstream build thread reading the file's own header (the artifact `INTAKE.md` makes authoritative for what a file is) is told Perpetua is unassigned and invited to place it, against Mark's own 2026-08-26 ruling.

---

## LOW

### L1. The M4 fix introduced a backwards cross-reference, in the same line that already points the same way correctly

Every `§N above` / `§N below` reference in Doc_02 was direction-checked programmatically against the section it sits in. **Exactly one fails**, and it is new this pass — the sentence written to correct M4, at §1 line 29:

> no complete English translation of the Retractationes is vendored, but substantial excerpts are, quoted inside NPNF's own editorial apparatus — the passage **this document's own §2 above quotes** ("who strive to defend themselves by the authority of the most blessed bishop and martyr Cyprian," from `npnf104`'s preface, itself quoting *Retractationes* II.18) is exactly this case

§1 runs to line 29; §2 begins at line 31. §2 is below. The same line, ninety words earlier, gets it right: *"the Retractationes (Knöll's CSEL 36, row 209, closing a gap named at **§2 below**)."* This is the defect class Round 15 rated LOW at its own L1 and whose fix Round 16 verified; it has recurred at a new site in the same section.

*(The substance of the M4 correction is verified and correct: `npnf104`'s `<div3 title="Preface.">` for *On Baptism* carries the passage verbatim, introduced as *"Concerning it Aug. in Retract. Book II. c. xviii., says"*; `npnf105` carries 18 `<div2 title="Extract from Augustin's Retractations.">` sections; and no English *Acta Proconsularia* exists anywhere in the vendored corpus — `anf05` returns zero hits for "proconsular", for "Galerius Maximus", and has no Acta div-title.)*

### L2. The C1 fix removed row 56's `****` but orphaned its closing `**`, leaving the only Registry row in the table with unbalanced bold markers

`**` occurrences counted programmatically across all 212 rows: **one row has an odd count — row 56, at 17.** Every other row is even. Traced across the three commits:

| commit | row 56 `**` count | `****` present |
|---|---|---|
| `c803529` | 16 | no |
| `d3db35a` (Round 15 fix) | 18 | **yes** |
| `0f7ca8a` (Round 16 C1 fix) | **17** | no |

The current text: *"…were independently checked this revision** | `**`Vols. I–III now vendored, rows 206–208 (2026-09-08, independent review Round 15)`**`, closing Manifest G5 in full; vols. IV–VI already vendored on the sibling Donatism branch (its own former G6); vol. VII not requested by either world.`**` The full seven-volume work: I. *Tertullien et les origines*…"*

The `****` that Round 16's C1 named was one delimiter of a balanced pair; removing two asterisks from the opening left the `world.**` closing with nothing to close. Bold parity is now inverted for the remainder of that cell — the seven-volume enumeration and the Persée/Internet Archive sentence render bold, and the two genuine bold spans that follow (`**Rights position resolved, not hedged:**`, `**This is a real, public-domain acquisition candidate…**`) render plain. Rows 40 and 41, the other two C1 sites, are both balanced and correct.

### L3. The new `lpc_Decision_Log.md` entry — written for Round 16's M5, and the authoritative record of both fix passes — miscounts three of its own figures

Checked against the review artifacts and the census history the entry describes:

1. > **All 17 findings (H1–H4, M1–M6, L1–L5, C1) were fixed in place; C2 … was deliberately left**

   The enumeration is 4+6+5+1 = **16**, and the sentence then states that the 17th was *not* fixed. Round 15's total was 17; 16 were fixed. The headline and the enumeration cannot both be right, and the clause that follows falsifies the headline.

2. > **All seventeen of Round 16's own findings (H1–H4, M1–M5, L1–L6, C1–C3) were fixed in the same pass this entry records**

   The enumeration is 4+5+6+3 = **18**, and `Doc02_Round16_Review.md`'s own verdict line reads "4 HIGH · 5 MEDIUM · 6 LOW · 3 COSMETIC" with eighteen `### ` finding headers. The list is right; "seventeen" is wrong by one. *(Round 16 itself supplied the seed: its scope paragraph says "Round 15's **seventeen** applied fixes (H1–H4, M1–M6, L1–L5, C1)" while enumerating sixteen. The entry inherited that figure rather than re-deriving it — the precise pattern the entry's own next paragraph names.)*

3. > a false "added this revision" / "English base unchanged" claim understating that **the 73→99 census growth spanned four passes, not one**

   Re-parsed from the census's own commit history: `0269b68` 73 → `cf1033e` 74 → `97419d7` 75 → `7ead600` 76 → `4911c02` 77 → working tree 99. The 73→99 growth spanned **five** passes; four of them are the *earlier* ones, which is what Doc_02 §1 itself now says correctly ("73 (2026-09-01) → 77, across four earlier additions … → 99 today"). Dropping "earlier" makes the compressed restatement off by one.

### L4. The L3 fix's decomposition names the Enchiridion inside the eleven differently-titled second witnesses, after the same sentence has already counted it among the two exact-title duplicates

§1 (line 13):

> the 99 also contains **two exact-title duplicates (the Enchiridion, the Scillitan Martyrs**, each counted once from an English source and once from a new Latin/Greek one) and **eleven further second-witness entries for works the original 73 already counted, catalogued under a differently-worded title** … nine of the eleven were added today (City of God in two parts, the Confessions, the two Epistulae files, the complete Enarrationes, **De Doctrina Christiana/Enchiridion**, the Codex Canonum, and the Vita Caecilii Cypriani)

Re-derived by set-differencing the current census against the 73-entry baseline at `0269b68`: the 2026-09-08 additions include `On Christian Doctrine (De Doctrina Christiana), Books I-IV` — a differently-worded second witness to the baseline's `On Christian Doctrine`, correctly one of the eleven — and, separately, `The Enchiridion (On Faith, Hope, and Love)`, whose title matches the baseline entry **exactly** and which is therefore one of the two duplicates the same sentence has just counted. The slash makes the Enchiridion appear in both buckets, against the sentence's own distinguishing criterion ("catalogued under a differently-worded title"). Round 16's L3 named this item as "*De Doctrina Christiana*" alone, correctly; the fix added the second half.

The eleven itself is right on every other member, independently re-derived: City of God I–XIII, City of God XIV–XXII, Confessions (CSEL 33), Epistulae 1–123, Epistulae 124–184A, Enarrationes complete, De Doctrina Christiana, Codex Canonum, Vita Caecilii Cypriani (nine today), plus Hartel CSEL 3 Pars I–II and Goldbacher CSEL 57 Pars IV (two on 2026-09-05).

### L5. Row 78 now supplies the identifier in its opening clause and, three clauses later, still says the identifier has not been located — the L4 fix rewrote the pointer and left the flat contradiction

Row 78's Verification Note, current state, in one cell:

> **Now vendored, row 209 (2026-09-08, independent review Round 15)** — closing Manifest G6; **the identifier given here (`sanctiaureliaugu36augu`; corrected from "below," independent review Round 16's own L4, since it is stated in this very clause, not below it) was located** by opening Getty-hosted CSEL-Augustine volumes directly by number … but **this specific volume's own identifier has not been located despite repeated searches across two rounds (Round 6's own M9)** — disclosed rather than filled with an invented placeholder

Round 16's L4 quoted that residual sentence and treated it as part of the deixis problem; the fix changed the pointer word and left the sentence. Row 90, the other L4 site, **was** reconciled — its new parenthetical explains that the identifier sits "at row 211, not stated in this row's own URL/Identifier column since this row records the request rather than the fulfillment," which makes the later "no Internet Archive identifier located" true of that column. Row 78 got no equivalent reconciliation, and rows 40 and 41 show the practice it is measured against: both had their older sentences *edited* to stay true ("Not vendored under this row's own number, and neither located at a specific URL this session"), not merely prefixed.

---

## COSMETIC

### C1. §2's two H2-correction clauses each misdescribe what they correct

- **Pontius bullet (line 54):** *"corrected here, independent review Round 16's own H2, from **this same paragraph's own Possidius entry below**, which had asserted the opposite."* The Possidius entry is not in this paragraph: it is a separate block seven lines below, with its own bolded lead-in and its own five bullets. The document's own established formula elsewhere is "corrected here … from an earlier draft that …"; pointing "from" a live sibling entry rather than a superseded draft reads as though the Possidius bullet still asserts the opposite, which it no longer does.
- **Possidius bullet (line 61):** *"corrected here … from an earlier draft's false claim that **Pontius's own Latin reaches this corpus 'only via' the English translation**."* The earlier draft's subject was Pontius's *Life*, not his Latin: *"which reaches this corpus only via a 19th-century English translation … with no facing Latin at all in the vendored volume."* As restated the proposition is incoherent — a Latin text cannot reach a corpus via an English translation — so the record of what was corrected does not match what was there.

Both bullets' substance is correct and mutually consistent; only their accounts of the correction are off.

### C2. Round 16's C3 (a silently OCR-normalized header quotation, in a paragraph declaring "no OCR error corrected") was fixed at the one file it named and stands unchanged at five others in the same nineteen-file batch

Every quoted string of ≥18 characters in all 19 headers was tested against its own file's de-hyphenated, whitespace-normalized body. Beyond the Harnack line the fix corrected, the same defect is present at least here:

| file | header quotes | file actually reads |
|---|---|---|
| `augustine_civitate-dei-14-22-…` | "…gratias congratulantes agant. **Amen**." | `gratias congratulantes agant. Arnen. 20` (l. 35611) |
| `codex-canonum-…bruns-pars1-1839` | "Post consulatum gloriosissimorum imperatorum, **Honorii** XII. et Theodosii VIII. augustorum" | `Post consulatum gloriosissimorum imperatorum Honmorii XII.` (l. 13570) |
| `prosper_chronica-minora-1-…` | "Aurelius Augustinus episcopus per omnia **excellentissimus** moritur **V**. kl. Sept., libris **Iuliani**…" | `per omnia cxcellentissimus` / `moritur Y. kl. Sept., libris luliani` (ll. 54206–08) |
| `augustine_enarrationes-…migne-pl36-37` | "**EXPLICIT TOMI QUARTI PARS PRIOR**"; "**PATROLOGIAE LATINAE TOMUS XXXVI**"; "**quae** certo constat non esse Augustini" | `KXPL1C1T TOMI QUAItTI PARS PRIOR.` (l. 73953); `PATRO LOGI Ai LATINJE TOMUS XXXYI.` (l. 13); `qnae certo constat non esse Augustini` (l. 140064) |
| `cyprian_opera-spuria-vita-pontius-…pars3` | "VITA CAECILII CYPRIANI (Pontio diacono **uulgo** adscripta)" | `(Pontio diacono iiiilgo adscripta).` (l. 40260) |

Each header's own Provenance note carries the same "nothing else altered, no OCR error corrected" sentence that made this a finding at Harnack. In every case the substance is confirmed present — this is about the quotations, not the claims they support.

### C3. The CSEL 44 file's Provenance note says the Getty back-cover material was stripped; it survives as the file's last content line — in the very file this pass edited

`cic/texts/augustine_epistulae-124-184a-lat_goldbacher-csel44.txt`, Provenance note (untouched this pass, while the Content note directly beneath it was rewritten for M2):

> front-cover scan noise stripped before the title page, **back-cover Getty Center Library barcode stripped after the final letter's apparatus**

The file's final lines, after Ep. 184A's explicit at line 40158, are two bare `.` lines, then **line 40168: `getty center library`**, then `1`. The identical Provenance sentence appears in `augustine_epistulae-1-123-lat_goldbacher-csel34.txt` and `augustine_retractationes-lat_knoll-csel36.txt`. This is the same shape as Round 15's C1 (the Harnack "was cut" claim contradicted by two surviving lines), which that round's fix pass resolved by disclosing the residue rather than by re-cutting the file.

### C4. §1's H4/M1 correction sentence carries an ambiguous double-object "before" and a "this Manifest" deixis inside a document that is not the Manifest

§1 (line 29):

> row 88 (the Codex Theodosianus, project-lead-supplied **outside this Manifest's own numbered list**, per `Source_Acquisition_Manifest.md`'s own record) was added 2026-09-02, **three days before row 191 and this world's actual first Latin-language vendored source**

On the natural reading, "before" takes two objects — row 191, *and* this world's first Latin-language vendored source — which would make row 88 precede the thing the clause is asserting it *is*. The intended reading (row 88 preceded row 191 by three days and is itself that first source) needs a comma and a verb. Both facts are correct on independent check: row 88's Added column reads 2026-09-02, row 191's 2026-09-05, and the census took the Codex Theodosianus at `cf1033e` (2026-09-03) before Hartel's CSEL 3 at `97419d7` (2026-09-05).

"this Manifest's own numbered list" is lifted verbatim from `Source_Acquisition_Manifest.md` line 81 and reads as a self-reference inside Doc_02. §1's other statement of the same fact, at line 13, gets it right: *"the Codex Theodosianus, project-lead-supplied **outside the Manifest's own numbered list**."*

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**H1 — the critical-edition contradiction, closed at both sections.** `grep -o "critical[a-z-]*"` over Doc_02 returns 14 "critical" and 2 "critical-edition"; every occurrence was read in context. §2's Augustine *Transmission History* entry no longer says "base Latin critical edition" — it now reads *"a specific **base Latin edition** is now vendored and directly checkable for the Confessions (CSEL 33, row 197, a modern critical edition), the general and Jerome-cluster correspondence (… rows 195–196, 193, modern critical editions), City of God (CSEL 40, rows 198–199, a modern critical edition), the Retractationes (CSEL 36, row 209, a modern critical edition), the Expositions on the Psalms (Migne PL 36–37, row 201, the 1861 Maurist printing, **not** a modern critical edition), and On Christian Doctrine and the Enchiridion (the Tauchnitz/Maurist text, row 200, likewise **not** a modern critical edition)."* That is now stronger than §1's disclosure rather than merely consistent with it: it labels each of the six individually. The two remaining "critical-edition" strings are both quotations of the superseded draft inside correction banners. **Correct and complete.** §2's "Not yet closed" row list is unchanged and still 15, 18, 19, 21, 22, 23, 25, 13, 14 — nine rows, none of them closed by any file in `cic/texts/`; and Round 16's C2 labelling defect is fixed, the composite range now reading *"the catechetical/creedal works and *De Trinitate*-and-related treatises (rows 15, 18, 25)"* with the Sermons, anti-Manichaean and anti-Pelagian corpora each carrying their own row.

**H2 — both bullets, checked separately.** The Pontius bullet now reads *"…also reaches this corpus in Latin, at its own source: the Vita Caecilii Cypriani inside Hartel's CSEL 3 Pars III (Registry row 194), corroborating the English translation directly rather than only through it."* The Possidius bullet now reads *"both figures' own Lives now have a vendored Latin source (Pontius's at Registry row 194, per the entry above), but on different footings."* Independently confirmed: `VITA CAECILII CYPRIANI` at line 40258 of `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`, its title-page parenthetical at 40260, and the census entry `Vita Caecilii Cypriani (attributed to Pontius the deacon) | pontius | tradition`. The two bullets are mutually consistent and neither now carries a "only via" negative. **Both halves fixed.**

**H3 — every census figure recomputed from raw YAML, not carried forward.** `latin-pastoral-congregational-christianity.yaml`: **99 entries, 97 distinct titles, `Counter({'tradition': 90, 'context': 9})`, and 88 distinct titles within the `tradition` set** — the figure §1 now states. Exactly two duplicate titles (`The Enchiridion (On Faith, Hope, and Love)`, `The Passion of the Scillitan Martyrs`), both inside the tradition set, so 90 − 2 = 88 reconciles. The nine `context` entries are Delehaye 1921, Harnack 1913, Monceaux I/II/III (1901/1902/1905), von Soden 1904, von Soden 1909, Prosper (Mommsen 1892) and the Codex Theodosianus — **seven of the nine modern secondary scholarship, 1901–1921**, exactly as §1 says. The comparators were re-derived across all 56 atlas files: **99 raw entries against 68** (`post-apostolic-house-church.yaml`, next-largest) and **90 `tradition`-role entries against 59** (`alexandria-catechetical.yaml` and `post-apostolic-house-church.yaml`, tied) — both figures exact, and Round 16's L2 scope mismatch resolved by giving each comparator on its own measure. lpc leads on all four counts attempted (99>68, 97>67, 90>59, 88>59), so "on every count attempted" holds. The 2026-09-01 baseline re-parsed at `0269b68`: 73 entries, 73 distinct titles, all `role: tradition` — "up from 73, all `tradition`" is exact.

**H4/M1 — priority, pass count, and G-item attribution.** Row 88's Added column is 2026-09-02, row 191's 2026-09-05; the census history is 73 (`0269b68`, 09-01) → 74 (`cf1033e`, 09-03, Codex Theodosianus) → 75 (`97419d7`, 09-05, Hartel/G1) → 76 (`7ead600`, 09-05, Possidius/G3) → 77 (`4911c02`, 09-05, Goldbacher/G4) → 99. "the first Latin exception" is gone from the document (zero hits). **Both sites now say four** and both now give the same window, 2026-09-02 through 2026-09-05, so Round 16's M1 defect 3 (two sites, two windows) is closed. The G-item attribution is now correct at line 13: *"the Codex Theodosianus, project-lead-supplied outside the Manifest's own numbered list, then `Source_Acquisition_Manifest.md`'s own G1/G3/G4 fulfillments in that order"* — matching the Manifest's own parenthetical and the commit order of the three fulfillments. Line 29's *"rows 191 (G1), 192 (G3), and 193 (G4) followed on 2026-09-05, in that order"* is exact against `git log`.

**M2 — the Letter 185 error, corrected at four artifacts and re-derived independently.** Registry row 196 now reads *"**Corrected here (independent review, Round 16): Letter 185 is NOT in this range** … Letter 185 is at its own Latin source in row 193."* The vendored file's Content note, the staging YAML `_staging/augustine_epistulae-124-184a-lat_goldbacher-csel44.yaml`, and the merged corpus-map note all now carry the same correction, and the merge was re-run (`corpus_map_merge.py --check` clean). Independently verified rather than trusted: `grep -n "CLXXXV"` in the CSEL 44 file returns **two** hits, both `CLXXXVII` cross-references at lines 20250 and 33417 — **no standing `CLXXXV` heading**, so row 196's careful hedge ("zero hits for 'CLXXXV' as a standalone heading") is exactly right; the file's last letter text is Ep. 184A's `Explicit epistola sci augu-/stini ad petru et habraham` at line 40158; and `augustine_epistulae-critical_goldbacher-csel57-pars4.txt` carries `EP. CLXXXV— CCLXX` at line 34 and the heading `CLXXXV.` at line 44. **Correct and complete.**

**M3 — row 204's two columns now agree, and the row's structure survived the edit.** Boundary Status now reads *"**Excluded** (both portions — corrected here, independent review Round 16's own M3, from an earlier draft's own self-contradicting 'Native (Scillitan Martyrs portion only)'…)"*, and Exclusion Reason still reads *"**Scillitan Martyrs: Excluded, Named Comparandum**, mirroring row 28 exactly … **Perpetua's Passion: Out-of-Boundary for this world by prior ruling**."* Across all 212 rows the Boundary Status column now takes exactly two values — `Native` (207) and `**Excluded**` (5) — with no hybrid remaining. Row 204 still parses to **11 columns / 12 pipes**, parentheses 15/15, `**` 18 (even). Doc_02 §1's *"mirroring row 28's own Excluded disposition exactly, not reopening it"* is now true of row 28, whose own Boundary Status is `**Excluded**`.

**M4 — the Retractationes/Acta distinction, both halves verified in the vendored volumes.** §1 now says *"no complete English translation of the Retractationes is vendored, but substantial excerpts are, quoted inside NPNF's own editorial apparatus,"* and separately that *"the Acta Proconsularia (inside row 194) has no English translation vendored anywhere in this corpus."* Both checked: the quoted Retractationes II.18 passage sits in `npnf104`'s `<div3 title="Preface.">` for *On Baptism*, introduced as the editor's own citation; `npnf105` carries 18 `Extract from Augustin's Retractations` sections. For the Acta, a corpus-wide `grep -ril "proconsular"` over every `.xml` and `.txt` in `cic/texts/` returns **no hit in `anf05`**, "Galerius Maximus" returns zero hits anywhere in the English corpus, and `anf05`'s div-titles carry only *"The Life and Passion of Cyprian, Bishop and Martyr. By Pontius the Deacon."* Row 209's own "not otherwise vendored **in English translation**" wording is untouched and survives the distinction, as Round 16 said it would.

**M5 — the Decision Log entry exists and its substantive claims check out.** The new 2026-09-08 entry covers both fix passes, names Round 16's M5 as the reason for its own lateness, and discloses Round 15's C2 non-fix with its reasoning. Its substantive claims were checked against the artifacts, not just against the review texts: Round 15's counts (4/6/5/2) are right; its seven "Not currently vendored" rows (40, 41, 56, 78, 89, 90, 99) match Round 15's H4 exactly; the row-196 and row-204 descriptions match what the diffs actually did; the C2 schema claim is consistent with `cic/texts/INTAKE.md`'s own template, which specifies "ISO 639-3 code" singular; and `texts_registry.py` still reports both files as `[lat]`, so the disclosed non-fix is accurately described as still standing. Only the three arithmetic figures at L3 above fail.

**L1, L4, L5, L6, C1, C2, C3 — all closed.** Programmatic per-line balance over Doc_02: **no line has unbalanced parentheses and no line has an odd `**` count** — the row-78 aside at §2 line 40 is repaired. Rows 78 and 90 no longer contain the string "identifier below"; both now name where the identifier actually is. All eight rows corrected in the Round 15 pass (40, 41, 56, 61, 78, 89, 90, 99) now carry an explicit round attribution — `grep -c "Round 15"` over the Registry returns **8**, up from 0. `grep -c "****"` returns **0** in both `Source_Registry.md` and `Doc_02_Source_Ecology.md`. The Harnack provenance note now quotes the OCR as it stands (`"Fortsetzung s. Seite III d. UraschlagR."`) with an explicit note that it is quoted as it reads. Row 56's residual bold-parity break is reported at L2; the `****` itself is gone.

**L6 — the Possidius softening, checked in both sections and against the vendored edition.** "not a subordinate's" survives in Doc_02 only inside the correction banner quoting the withdrawn draft. §2's replacement and §4's are consistent with each other and with the source: Weiskotten's introduction reads, verbatim, *"he was in all likelihood younger than his teacher and friend"* and *"he was probably not over thirty, as Augustine was then thirty-five"* (ll. 318–321), and *"In 397, probably within a short time after the death of Megalius, Bishop of Calama and Primate of Numidia, Possidius succeeded to this episcopate"* (ll. 325–328). §4's *"a bishop's own retrospective, written from decades of friendship that began as a younger monastic disciple's relationship to Augustine (§2 above qualifies the peer/subordinate contrast precisely) and matured into shared episcopal office by 397"* points correctly (§2 is above §4) and does not restate the withdrawn flat contrast. The "almost forty years" epilogue figure is present at line 307 of the same file. No contradiction between the two sections.

**Registry table integrity.** All 212 rows re-extracted by column position: numbers 1–212 complete, **no gap, no duplicate**, and **every one of the 212 rows parses to exactly 11 columns / 12 pipes** — including all twelve previously-touched rows (28, 39, 40, 41, 56, 61, 78, 89, 90, 99, 196, 204), each independently confirmed at 12 pipes with balanced parentheses.

**Engine scripts, both re-run this session.** `python cic/engine/texts_registry.py` → **exit 0**, *"OK: every vendored file has a header-verified rights line (public domain, or a recognized open licence), an ENTRIES row, and no ENTRIES row points at a missing file"*; 88 vendored files, 23 non-English sources. `python cic/engine/corpus_map_merge.py --check` → **exit 0**, *"528 distinct work(s) → 788 assignment(s) across 56 Atlas entry(ies) [check only, nothing written]"*.

**Doc_02 §1 and §2 quotations, swept programmatically.** Every quoted string of ≥20 characters in §1 and §2 was tested against `Source_Registry.md`, `Doc_01`, the Manifest, the corpus map and `INTAKE.md`, then each apparent miss was chased by hand. All resolve except M2's Doc_01 §7 attribution. Verified present verbatim: the corpus map's *"the direct root of the Carthaginian congregational tradition"* and its Optatus hedge *"because the entry choice is inferred from region and date — Mark may prefer another Latin home for a Numidian polemicist"*; Doc_01's *"arguing with Cyprian, disputing his ruling while claiming his communion"*, *"only as NPNF's own editorial note"* and *"not vendored in this corpus"*; the corpus map's `npnf214` council note; and, in the vendored texts, the Cyprian and Possidius loci quoted above.

**Every row number 191–212 is now referenced in Doc_02** (row 207 only inside the "206–208" range, which is how the Monceaux volumes are cited throughout), so Round 15's L4 gap for row 204 stays closed.

**Spot-checked vendored-file header content claims, beyond the two the review brief named.** Delehaye: `Chapitre I. Les passions historiques` and `Chapitre VI. Histoire, tradition, littérature` both present in the volume's own table of contents, confirming the "six chapters (I–VI)" range. von Soden's *Prosopographie*: line 24 reads `87 Yotanten des Konzils von Karthago am 1. September 256` — the "87 bishops" and the 1 September 256 date both confirmed. Confessions: `Magnus es, domine, et laudabilis ualde` at line 1877, `Liber Tertius Decimus` present, Index Scriptorum present. Retractationes: Praefatio, both books and `Index Locorum Retractatorum` all present. Codex Canonum: the 419 opening formula, the Breviarium Hipponense, Teleptensis and the Toledo councils all confirmed present. Enarrationes: the PL 36/PL 37 junction confirmed at line 73953, the doubtful Psalm 14 exposition and the Maurist footnote confirmed at line 140064. The only header-content defect found in this sweep is the Robinson claim at M3 above; the rest are accurate in substance, with the quotation-fidelity caveat at C2.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the fix pass and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** M3 concerns a vendored file's own header contradicting Mark's 2026-08-26 Perpetua ruling as the corpus map and Registry row 204 both already record it. The corrective is to bring the header into line with the ruling that already governs — reporting an existing determination, not making a new one, the same test §10 applies to Optatus. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing here changes `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022, or any governing document. C2 and C3 are findings that a file's own header does not match the file, not that the header convention changed. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round disagrees with the commissioning brief, the `0f7ca8a` commit message and the Decision Log on one point of fact — Round 16's finding total is 18, not 17 — and with Round 16's own scope paragraph on a second, that Round 15 applied "seventeen" fixes when it applied sixteen. Both were closed here by counting the review artifacts' own finding headers and verdict lines directly rather than preferring any account on authority. Neither requires the project lead. M2 puts a sixteen-round-old misattribution into the record, which no round has previously named; it is a correction to make, not a tension between reviews. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

Doc_02's status line and §10, and `Source_Registry.md`'s status line, still describe the Round 14 disposition of 2026-09-02, still read "Fourteen independent adversarial review rounds" over the sequence "(Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0)", and still point a reader to "`Doc02_Round1_Review.md` through `Doc02_Round14_Review.md`" while Doc_02 now carries in-text attributions to Rounds 15 and 16 and `Source_Registry.md` carries eight to Round 15. That is reported here as observed, checkable state, on the same footing Round 16 reported it. Whether and how those lines should change, and what disposition follows from this round's counts, is **not assessed here**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition. This review supplies only the input that rule takes: a finding count and a findings list.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 0 HIGH · 3 MEDIUM · 5 LOW · 4 COSMETIC.**
