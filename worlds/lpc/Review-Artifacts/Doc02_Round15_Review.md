# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 15 Independent Adversarial Review — scoped to the 2026-09-08 source-integration revision

**Documents reviewed (working-tree state, not a commit — `git status --porcelain` shows 50 uncommitted paths on top of `c803529`, branch `claude/record-native-world-build-v2-yq11wl`):**
- `worlds/lpc/Doc_02_Source_Ecology.md` (147 lines)
- `worlds/lpc/Source_Registry.md` (329 lines; 212 rows)
- `worlds/lpc/Source_Acquisition_Manifest.md` (85 lines; G1–G9)
- `worlds/lpc/lpc_Decision_Log.md` (316 lines; last four entries dated 2026-09-08 read in full)
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines), for the cross-document checks at §5 and §7
- The 19 newly-vendored files in `cic/texts/`, `cic/texts/REGISTRY.yaml` (88 entries), `cic/texts/INTAKE.md`, and `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` (99 entries)

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-08 vendoring, and did not write Rounds 1–14.

**Scope, stated plainly rather than left implicit.** This round is **not** a fifteenth full review of Doc_02. Its brief was to re-derive, against primary artifacts, only what the 2026-09-08 revision newly asserts, plus the cross-document consistency and stale-claim questions those new assertions raise. Everything untouched by that revision is treated as already cleared by Rounds 1–14 and was not re-litigated. Two consequences follow, both disclosed rather than assumed harmless:

1. **No fresh ten-item relative-recall test and no PRESS question were run this round.** `Source_Registry.md`'s own saturation statement should therefore **not** be incremented for Round 15, and this round adds no new distinct works to that running total. The V7.4 field-bibliography sweep proper remains unrun, exactly as §10 already discloses.
2. **This round makes no disposition assessment and no recommendation about Doc_02's status line or §10.** Per the task's own scoping and this project's CO-022 discipline, that determination belongs to the build thread. The status line and §10 still describe the Round 14 disposition; that fact is noted here as observed state, not assessed.

**Method — what was actually re-derived, not trusted.** Every count in this review was recomputed from the raw artifact this session: `yaml.safe_load` across all 56 atlas files in `cic/corpus-map/` (59 `.yaml` files less `AUTHOR-IDS.yaml`, `UNATTRIBUTED.yaml`, `WORKS.yaml`; `_staging/` excluded), a fresh regex parser over all 212 Registry rows, `git show` against four historical revisions of the corpus-map file to establish what the census actually held on each date, and direct `grep`/`sed` inspection inside the vendored text files themselves. No figure was carried forward from `lpc_Decision_Log.md`, from the Manifest, or from the task brief that commissioned this review.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 4 HIGH · 6 MEDIUM · 5 LOW · 2 COSMETIC.**

The underlying vendoring work is sound. All 19 files exist, are substantial, carry complete intake headers, and say what the Registry says they say; both engine scripts run clean; the Manifest's eight fulfillment paragraphs are accurate; the specific extraction hazard the build thread flagged (Arnobius bleed into the Cyprian Pars III file) is genuinely absent. **The findings below are almost entirely about how Doc_02 and `Source_Registry.md` now *describe* that work** — four claims that are checkably false as written, and a set of enumerations and pointer updates that were propagated to some sites and not others.

---

## HIGH

### H1. §2's "not yet closed" list names Registry row 16 (*On Christian Doctrine*) as having no vendored base Latin edition, three clauses after the same paragraph says it does — and the same clause omits two bodies it names in prose and two bodies that genuinely lack one

§2's Augustine *Transmission History* entry says, in one sentence pair:

> a specific base Latin critical edition is now vendored and directly checkable for … **On Christian Doctrine and the Enchiridion (the Tauchnitz/Maurist text, row 200)** … **Not yet closed, named rather than assumed innocuous:** no base Latin edition is vendored for the anti-Manichaean corpus, the anti-Pelagian corpus, the Tractates on John, the Sermons, or the catechetical/doctrinal-moral treatises grouped at **Registry rows 15–16, 18–19, 22–23, 25**

Registry row 16 is **`Augustine, *On Christian Doctrine* (Books I–IV)`** — checked directly against the table. Registry row 200's own Licensed-For column reads: *"Latin original standing behind the already-vendored NPNF translations of both **On Christian Doctrine (row 16)** and the Enchiridion (row 17)."* The document therefore places row 16 in both the closed and the not-closed set in consecutive clauses. This is the precise, checkable claim the round was asked to check precisely, and it is false as written.

Two further defects in the same row list, independently checked against the table:

- **Row 21 is omitted.** Row 21 is `Augustine, *Tractates on the Gospel of John* (124 tractates), *Ten Homilies on the First Epistle of John*, *Our Lord's Sermon on the Mount*, *The Harmony of the Gospels*` — the Tractates are named in the sentence's own prose, but row 21 does not appear in the row range, which jumps 19 → 22.
- **The anti-Donatist corpus is omitted entirely.** Rows 13 (*On Baptism, Against the Donatists*, Confidence **A**) and 14 (*Answer to the Letters of Petilian*) have no vendored Latin edition — independently confirmed: `cic/texts/` contains no Latin *De Baptismo* or *Contra Litteras Petiliani* file, and `grep -i "baptismo\|petilian" cic/texts/REGISTRY.yaml` returns no vendored edition. The NPNF volume carrying them is `npnf104_augustine-anti-manichaean-anti-donatist.xml` — the *same volume* whose anti-Manichaean half §2 does name. Row 13 is the row from which §2's own Cyprian *Transmission History* entry quotes Augustine's continuous words at Book III ch. 2 §2, so the "further translating hand" caveat this entry exists to state applies to it with full force.

Correct list, on the Registry's own rows: 15, 18, 19, 21, 22, 23, 25, plus 13 and 14. Not 16.

### H2. §1's qualifier on the 73 → 99 census growth is falsified on both of its limbs

§1 states:

> **The growth from 73 to 99 is original-language second-witness material added this revision (below), not newly-discovered English tradition-voice content — the English evidentiary base itself is unchanged.**

**Limb 1 — "added this revision" — is false for 4 of the 26.** The census file's own history, recomputed by `git show <commit>:cic/corpus-map/latin-pastoral-congregational-christianity.yaml` and re-parsed at each point:

| commit | date | works |
|---|---|---|
| `0269b68` | 2026-09-01 | **73** |
| `cf1033e` (Codex Theodosianus staged) | 2026-09-03 | 74 |
| `97419d7` (Hartel CSEL 3 Pars I–II) | 2026-09-05 | 75 |
| `7ead600` (Weiskotten's Possidius) | 2026-09-05 | 76 |
| `4911c02` (Goldbacher CSEL 57 Pars IV) | 2026-09-05 | **77** |
| working tree (this revision) | 2026-09-08 | **99** |

This revision added **22**, not 26. Four were added on 2026-09-03 and 2026-09-05, in prior passes this document's own §9 item 1 separately records.

**Limb 2 — "the English evidentiary base itself is unchanged" — is falsified by Registry row 192.** Weiskotten's 1919 Possidius (census entry 76, added 2026-09-05) is a **bilingual** edition whose complete English translation is present. Row 192's own Verification Note says so explicitly: *"A genuinely bilingual edition — because the complete English translation is present throughout, this row's Confidence is **A**, the ordinary-primary-evidence footing, not the second-witness-only footing rows 88, 191, and the Nestle 1904 Greek New Testament carry."* The Manifest's own G3 calls it *"new primary-narrative content this world does not otherwise have any of."* The English base did change inside the 73 → 99 window, by exactly one work — and it is the work H-finding M5 below shows Doc_02 still does not mention outside its acquisition list.

### H3. The 99 figure is offered as the measure of this world's "primary-source base," but 9 of the 99 are `role: context` entries — 7 of them modern (1901–1921) secondary scholarship — where the 73-entry baseline had none

§1's opening sentence uses the census figure as the measure of the evidentiary claim itself:

> this world holds the largest and most direct **primary-source base** of any confirmed world in the portfolio to date, **among what is currently vendored** (99 works in its own corpus-map census as of 2026-09-08 — up from 73 at this document's own original drafting …)

Independently re-parsed from the two census files:

- **2026-09-01 (`0269b68`): 73 entries, 73 distinct titles, no duplicates, and `Counter({'tradition': 73})` — every single entry `role: tradition`.**
- **Working tree: 99 entries, 97 distinct titles, `Counter({'tradition': 90, 'context': 9})`.**

The nine `context` entries are: Delehaye 1921, Harnack 1913, Monceaux I/II/III (1901/1902/1905), von Soden 1904, von Soden 1909, Prosper (Mommsen 1892), and the Codex Theodosianus. **Seven of the nine are twentieth-century secondary monographs** — Doc_02's own §3 classifies four of them as exactly that, "distinct in kind" from primary sources. Counting Delehaye's 1921 genre study and Monceaux's 1901 literary history inside a figure presented as this world's "largest and most direct primary-source base" is a category error the 73 baseline did not contain and the document does not disclose.

Two further measurement mismatches the sentence does not caveat, both independently derived:

- **The 99 double-counts.** Two titles appear twice: `The Enchiridion (On Faith, Hope, and Love)` and `The Passion of the Scillitan Martyrs`, each once from an English source file and once from a new Latin/Greek one. The 73 had zero duplicates.
- **At least nine further new entries are second witnesses to works already inside the 73, catalogued under different titles** — e.g. `Augustine's Confessions (Knoll's critical edition, CSEL 33)` alongside `The Confessions`; `Augustine's City of God, Books I–XIII` and `Books XIV–XXII` alongside `City of God`; `On Christian Doctrine (De Doctrina Christiana), Books I–IV` alongside `On Christian Doctrine`; `The Code of Canons of the African Church (Codex Canonum…)` alongside `The Code of Canons of the African Church (Council of Carthage, 419)`; `Vita Caecilii Cypriani` alongside `The Life and Passion of Cyprian, Bishop and Martyr`.

**What survives this finding, stated so the fix is not over-corrected:** the superlative itself holds even on the stricter count. Second-largest is `post-apostolic-house-church.yaml` at 68 (recomputed; §1's "the second-largest now at 68" is exactly right), and lpc leads on distinct titles (97), on `tradition`-only entries (90), and on any reasonable collapse of second witnesses (~83–85). It is the *composition* of the 99 and the *comparability* of 99 to 73 that need a caveat, not the "largest atlas file" claim.

### H4. Seven Registry rows that name works now vendored still read "Not currently vendored" — including row 78, which §2 cites as evidence that it *is* vendored, and row 41, which §9 item 8 declares "Resolved"

The build thread updated three pre-existing rows to point at the new files — rows 28, 39, and 61 all now carry an explicit pointer paragraph. **Seven others were missed.** Verification Note openings, extracted programmatically:

| row | still says | now vendored as |
|---|---|---|
| 40 | "**Not currently vendored**, and neither located at a specific URL this session" | row 205 (Harnack) |
| 41 | "**Not currently vendored and not independently located at a specific URL this session**" | inside row 194 (Acta Proconsularia) |
| 56 | "**Not currently vendored.**" | rows 206–208 (Monceaux I–III) |
| 78 | "Not currently vendored. … this specific volume's own identifier **has not been located despite repeated searches across two rounds**" | row 209 (Knöll, CSEL 36) |
| 89 | "Not currently vendored." | row 210 (von Soden, *Briefsammlung*) |
| 90 | "Not currently vendored. … **no Internet Archive identifier located despite a search**" | row 211 (von Soden, *Prosopographie*) |
| 99 | "Not currently vendored." | row 212 (Delehaye) |

Two of these are load-bearing contradictions with Doc_02's own current text:

- **§2 says of row 78:** *"78 (Knöll's CSEL 36, public domain — **now actually vendored, row 209, 2026-09-08, closing the gap §2's own Augustine entry above names**)."* Row 78 itself says the opposite, and says the identifier was never found — when row 209 records it (`sanctiaureliaugu36augu`) and the Manifest's G6 fulfillment paragraph names it.
- **§9 item 8 says of row 41:** *"**Resolved 2026-09-08.** Registry row 41 (the *Acta Proconsularia Sancti Cypriani*, Cyprian's own trial record) was named from general field knowledge, not independently located at a specific URL … no further acquisition is needed."* Row 41 still says it is not vendored and not located.

Rows 28, 39, and 61 establish that in-place pointer updates are this Registry's own practice for exactly this situation, so this is incomplete propagation, not a deliberate append-only constraint. A downstream builder reading row 78 or row 40 today would conclude the work is unavailable and go looking for it.

---

## MEDIUM

### M1. §5's new Prosper paragraph attributes to Doc_01 §2 a characterization Doc_01 does not contain anywhere

§5 states:

> the 439 entry documents **what Doc_01 §2 calls the wider siege's own eventual outcome**, external to this world's own close

Doc_01 was searched in full (302 lines): **zero hits** for "eventual outcome," zero for "wider siege," and zero for "439." Doc_01 §2's actual ending-point text reads: *"**Ending point (430):** Augustine's death at Hippo, 28 August 430, during the Vandal siege of the city … the Vandal invasion (crossing from Spain in 429, besieging Hippo as Augustine lay dying) is external, violent pressure on this world's own congregational life at its end."* Nothing there characterizes any later outcome.

The substantive point is also wrong independently of the attribution: Prosper's 439 entry records the **Vandal capture of Carthage**, a different city nine years later, not the outcome of the siege of Hippo. The vendored text itself confirms the entry's content (c. 1339, line 54558: *"Aetio rebus quae in Gallia componebantur intento Gisiricus, de cuius amicitia nihil metuebatur, [XIIII kal. Nov.] Carthaginem dolo pacis invadit omnesque opes eius excruciatis diverso tormentorum genere civibus in ius suum vertit"*) — Carthage, by treachery, not Hippo.

### M2. §1 and §2 call rows 200 and 201 "critical editions" against those rows' own emphatic "NOT a modern critical edition"

§1: *"**Latin critical-edition second witnesses** are now vendored for: … On Christian Doctrine and the Enchiridion (Bruder's 1838 Tauchnitz text, row 200); the Expositions on the Psalms, complete (Migne's PL 36–37, row 201) … and the Code of Canons of the African Church (Bruns's 1839 edition, row 202)."
§2: *"a specific **base Latin critical edition** is now vendored and directly checkable for … On Christian Doctrine and the Enchiridion (the Tauchnitz/Maurist text, row 200), the Expositions on the Psalms (Migne PL 36–37, row 201)."*

Row 200's own Verification Note: *"**NOT a modern critical edition** — Bruder's own preface states plainly this is not a critical text; **disclosed rather than treated as equivalent to CSEL 80**."* Row 201's: *"**NOT a modern critical edition** (CCSL 38–40 is the modern standard; not vendored, in copyright)."* Row 202 makes no critical-edition claim for Bruns either. Both rows go out of their way to make this disclosure, and both of Doc_02's summarising sentences undo it at the document level — which matters, since the gap §2 is closing was specifically framed as a *critical-apparatus* gap.

### M3. §1's "single partial exception" claim is wrong under either reading of its own reference date

> At Step 2's own original drafting, this world's entire primary-source base was English-only (the vendored 19th-century ANF/NPNF translations), **with a single partial exception (Cyprian's CSEL 3, Pars I–II, row 191, fulfilled 2026-09-05)**.

- Read literally (state as of the drafting date, 2026-09-01): there was **no** exception. Row 191 was vendored 2026-09-05, four days later, as its own Registry row and the Manifest's G1 paragraph both state. The census on 2026-09-01 was 73 entries, all `role: tradition`, all from ANF/NPNF sources.
- Read as "state immediately before this revision" (2026-09-08): row 191 was **not** the single exception. Row 88 (`codex-theodosianus_latinlibrary.txt`, Latin, project-lead-supplied 2026-09-02, staged into the census 2026-09-03), row 193 (Goldbacher CSEL 57 Pars IV, Latin, 2026-09-05) and row 192 (Weiskotten's Possidius, bilingual, 2026-09-05) were all vendored first. Row 192's own note names rows 88 and 191 *together* as carrying "the second-witness-only footing," so the Registry itself already contradicts the "single" count.

### M4. §1's blanket "available for cross-checking a specific English rendering" is false for row 209, and drops the half of INTAKE.md's rule that covers exactly that case

> **Every one of these is a second witness per `cic/texts/INTAKE.md`'s own governing rule — never itself primary evidence for a Representative, since this project's evidence language is English — available for cross-checking a specific English rendering, not a new class of citable claim.**

The list "these" governs explicitly includes *"the Retractationes (Knöll's CSEL 36, row 209)."* Row 209's own Licensed-For column says: *"the Retractationes **are not otherwise vendored in English translation anywhere in this corpus**."* Independently confirmed: the eight vendored NPNF Augustine volumes (`npnf101`–`npnf108`) contain no Retractationes. There is no English rendering to cross-check.

`cic/texts/INTAKE.md`'s actual rule already accommodates this and Doc_02's paraphrase drops it: *"original-language texts … as second witnesses — never primary evidence for a Representative (this project's evidence language is English), but legitimate, rights-clean material for when two English translations disagree, **or when no English translation exists at all yet**."* The same applies to the *Acta Proconsularia* inside row 194, which row 194 itself describes as *"not previously vendored in any form."*

### M5. Possidius's *Life of Augustine* (row 192) — vendored, Confidence A, complete English translation, `role: tradition` in this world's census — appears nowhere in §1's formation-narrative paragraph, §2's Author Gravity assessment, or §4

`grep "192\|Possidius\|Weiskotten"` over Doc_02 returns **one** hit: §9 item 1's acquisition list ("G3 (Possidius's *Vita Augustini*, row 192, closed 2026-09-05)"). It is absent from:

- **§1, "Formation-narrative evidence"** — names only Pontius's *Life of Cyprian*.
- **§2, Author Gravity** — has entries for Cyprian, Augustine, and Pontius; none for Possidius.
- **§4, Formation Narrative Sources** — assesses Pontius, then "Cyprian's own letters as formation-narrative-adjacent material," then "No Tier 5 material identified." Nothing else.

The Manifest's own G3 named §4 as the site this acquisition would repair: *"Possidius was Augustine's own companion for decades and the author of the Augustine-side counterpart to Pontius's already-vendored *Life of Cyprian* — **a real gap this world's own formation-narrative work (Doc_02 §4) currently carries with only one of its two anchor figures' own companion-biographies**"*, with *"Value if acquired: **closes the one-sided formation-narrative gap named at Doc_02 §4 and §9**."* The acquisition closed on 2026-09-05; §4 still carries the gap, and §9 no longer names it. This revision rewrote §9 item 1 to record row 192 as closed without propagating the consequence to the section whose subject it is.

This is the single most consequential substantive omission this round found. The corpus map confirms the work is fully in scope: `Sancti Augustini Vita (Life of Augustine) | possidius | tradition | assigned | possidius_vita-augustini_weiskotten1919.txt`.

### M6. §3's "Four older, public-domain secondary works are now vendored in full" omits Harnack (row 205) — there are five, and Harnack appears nowhere in §3

§3's new paragraph enumerates Monceaux I–III (rows 206–208, one work in three volumes), von Soden's *Briefsammlung* (210), von Soden's *Prosopographie* (211), and Delehaye (212) — four works, seven rows. Registry row 205 is **Type S, Confidence C**, vendored in the same pass, and its Licensed-For reads *"Not currently licensed for any specific claim — a modern critical study and commentary on the already-vendored Vita Cypriani."* It belongs in the Secondary Scholarship Assessment on the paragraph's own stated criterion. `grep -c "Harnack"` over Doc_02 returns **1** — §9 item 1's acquisition list only.

The omission is not cosmetic in this instance: Harnack's is a study of the *Vita Cypriani* specifically, and §3's paragraph closes by licensing Delehaye "for this section's own Author Gravity assessment of Pontius's *Life*" — Harnack is the other newly-available instrument for precisely that assessment. Its exclusion also makes the census-composition problem at H3 harder to see, since Harnack is one of the seven `role: context` secondary works inside the 99.

*(Secondary observation, not counted as a separate finding: the same paragraph opens "Confidence C, **not currently licensed for a specific claim**" and then says Delehaye is "**licensed for** this section's own Author Gravity assessment," matching row 212's Licensed-For column. The two are reconcilable — licensed but not yet drawn on — but the paragraph states the blanket negative before the exception rather than after.)*

---

## LOW

### L1. §2's Cyprian entry points "above" at something that is below it

§2's *Cyprian — Transmission History* bullet: *"now actually vendored, row 209, 2026-09-08, closing the gap **§2's own Augustine entry above** names."* The Cyprian bullet is Doc_02 line 40; the Augustine *Transmission History* entry that names the gap is line 47. The pointer runs the wrong way. (§1's parallel pointer, "closing a gap named at §2 below," is correct.) This is the directional-pointer defect class `lpc_Decision_Log.md` records Round 7 fixing in that log's own text.

### L2. §9 item 1's "no acquisition decision remains" list omits G8, which the same item lists among the eight now closed

§9 item 1 names eight closed items — *"G1 …, G2 …, G3 …, G5 …, G6 …, G7 …, **G8** (von Soden's *Prosopographie*, row 211), and G9"* — then says: *"**No acquisition decision remains for the project lead to make on G1, G2, G3, G5, G6, G7, or G9.**"* Seven, not eight. `Source_Acquisition_Manifest.md`'s own closing status update (line 85) carries the identical seven-item list with the identical omission, so this is a propagated defect rather than a divergence between the two documents. It is the stale-enumeration failure mode §9 item 6 itself exists to warn about.

### L3. Registry row 61's Verification Note still opens "**Not currently vendored.**"

Row 61 (Goldbacher's *Epistulae*, all five parts) *was* given a pointer update — its note ends *"Pars IV (CSEL 57) vendored 2026-09-05 as row 193; Pars I … and Pars II … now also vendored together as row 195, and Pars III (CSEL 44) as row 196 … Only CSEL 58 (praefatio and indices) remains unacquired."* But the note's **first sentence** is still "**Not currently vendored.**", now false for four of the five parts. Row 39 handles the same situation correctly, by leading with the update rather than appending it: *"**Pars I and II now vendored as row 191 … Pars III … now also vendored, as row 194**…"*. A reader scanning first sentences gets the wrong answer from row 61 and the right one from row 39.

### L4. Registry row 204 (Robinson 1891) is disclosed nowhere in Doc_02

Row 204 is the only one of the 19 newly-vendored files that Doc_02 never mentions — `grep` over the document returns no "204," no "Robinson," and no reference to the new Latin/Greek witness. Its two natural sites were both edited or left standing this revision without it: §1's Named-Comparandum paragraph on the *Passion of the Scillitan Martyrs* (row 28), and §6's paragraph on Perpetua (which says the *Passion of Perpetua* "predates this world's own c. 246 start (the same ground row 28 is excluded on)"). Registry row 28's *own* note **was** updated — *"**A Latin/Greek second witness for this same excluded entry is now vendored, row 204 (2026-09-08) — mirroring this row's own role and confidence exactly; the Excluded disposition is unaffected.**"* — so the disclosure exists in the Registry and not in the document whose §1 revision paragraph claims to enumerate what was added. Nothing turns on it substantively (both texts remain excluded/out-of-boundary, correctly), but the omission is inconsistent with how the other 18 files were handled.

### L5. `lpc_Decision_Log.md`'s 2026-09-08 "Ten sources" entry miscounts its own file tally

The entry states: *"logged as Source_Registry.md rows 194 and 197–204 (row 195/196 cover **an eleventh and twelfth file** from this same batch — see the next entry)."* Rows 194 and 197–204 are **nine** rows, one file each — verified against the Registry and against `cic/texts/`. Rows 195 and 196 are therefore the **tenth and eleventh** files, not the eleventh and twelfth. (The entry's headline "Ten sources" is defensible on a different unit — counting CSEL 40 Pars I–II as one source gives ten — but the file count in the parenthetical does not reconcile with it either way.) No substantive claim depends on the number.

---

## COSMETIC

### C1. The Harnack file's own provenance header says the preceding advertisement list "was cut," but two lines of it survive

`cic/texts/harnack_vita-cypriani-commentary-lat-deu_1913.txt` header: *"The immediately preceding material in the bound scan (a Hinrichs publisher's advertisement list of other, unrelated Texte und Untersuchungen volumes) **was cut as front matter**."* The first two content lines after the header separator are `1909. (Bd. 34, 2b) M. 2 —` and `Fortsetzung s. Seite III d. UraschlagR.` — residue of exactly that list, immediately above the `DAS LEBEN CYPRIANS` title page. The Heft's own content is complete and correctly bounded; only the header's account of the trim is slightly overstated.

### C2. Two files carry a `Language:` field narrower than their own content note

`harnack_…_1913.txt` declares `Language: lat` (and is reported as `[lat]` by `texts_registry.py`) while its own content note says *"the bulk of this file is German-language scholarly commentary … not itself Cyprianic primary text"* and its filename says `lat-deu`. `perpetua-scillitan-martyrs-lat-grc_robinson1891.txt` likewise declares `lat` while its filename and Registry row 204 both say Latin/Greek. Neither affects any claim; both make the generated non-English inventory slightly less accurate than the files themselves are.

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**Census arithmetic.** All 56 atlas files in `cic/corpus-map/` re-parsed with `yaml.safe_load` this session. `latin-pastoral-congregational-christianity.yaml` carries exactly **99** entries under `works:` — the figure §1 states, independently re-derived, not carried forward. It is **the largest atlas file**, and the next-largest is `post-apostolic-house-church.yaml` at **68**, exactly as §1 says. The superlative survives every stricter recount attempted (97 distinct titles; 90 `tradition`-role entries).

**Registry table integrity.** All 212 rows extracted programmatically: numbers 1–212 complete, **no gap, no duplicate**. Every new row number Doc_02 cites — 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 205, 206, 207, 208, 209, 210, 211, 212 — exists and, apart from the row-16 and row-78/41 problems at H1 and H4, says what Doc_02 says it says. Each new row names a vendored path that exists on disk.

**Cyprian CSEL 3 Pars III — the flagged extraction hazard.** `grep -c "ARNOBII"` returns **0**, as claimed. Pushed further than the claim: case-insensitive `arnob` returns **1** hit and `adversus nationes` **1** hit, both inside the file's *own intake header* describing the excision (line 8); `reifferscheid` returns **2**, one in the same header and one at line 40247 inside **Hartel's own praefatio acknowledgments** (*"dicaui, deinde Carolo Halm, Augusto Reifferscheid…"*) — legitimate CSEL 3 front matter, not Arnobius text. The file is 42,600 lines / 1.3 MB and ends inside Hartel's apparatus, not mid-word.

**§9 item 8's Acta Proconsularia claim, verified in the text.** The Vita's heading `VITA CAECILII CYPRIANI (Pontio diacono uiilgo adscripta)` is at line 40258; the Acta follows at line **41413** as `ACTA PEOCONSVLARIA` (OCR R→E, which is why a literal "PROCONSVLARIA" grep misses it), opening *"…tertio kalendarum Septembrium Carthagiue in secretario Paternus proconsul Cypriano episcopo dixit"* and running through *"Cyprianus episcopus dixit: Deo gratias"* at line 41577. §9 item 8's "immediately following the Vita" is accurate.

**Bruder 1838 — every claimed locus verified.** All three of row 200's boundary quotations are present in the body and were missed by exact-phrase grep only because the extraction line-wraps them: *De Doctrina Christiana*'s close `quantulacumque potui facul-/tate, disserui.` at lines 8960–61, followed by the two footnotes to Esther 4:16 and Wisdom 7:16 exactly as described; the Enchiridion's title block at lines 8973–83; its opening `l/ici non potest, dilectissime fili Laurenti` at 8987; its close `fide, spe et caritate conscripsi.` at 12774. The header's "two earlier, unrelated occurrences" warning is also accurate — Bruder's preface at lines 263/289 and the quoted *Retractationes* II.63 excerpt at lines 1628–30. Zero hits for "CSEL," "Green," "1963," or "copyright," as row 200 claims.

**Prosper — both end-window entries verified in the text.** Augustine's death: line 54206, *"Aurelius Augustinus episcopus per omnia cxcellentissimus moritur Y. kl. Sept., libris luliani inter impetus obsidentium Wandalorum…"*, under the year heading `Theodosio XIII et Valentiniano III. a. [4]30` at line 54198. The Carthage entry: c. 1339 at line 54558; its year is fixed independently by the volume's own additamentum at line 55224, *"ad a. 439 c. 1339 [Gisiricus, de cuius amicitia nihil metuebatur] XIIII kal. Nov. [Carthaginem dolo pacis invadit]."* §5's `role: context` claim is exact — the corpus map carries Prosper as `prosper | context | assigned`.

**Harnack.** 305 KB, header states Hartel's CSEL 3 text with noted deviations plus the first German translation, matching row 205. Title page present.

**Engine scripts, both run.** `python cic/engine/texts_registry.py` → exit 0, *"OK: every vendored file has a header-verified rights line (public domain, or a recognized open licence), an ENTRIES row, and no ENTRIES row points at a missing file"*; 88 registry entries (matching the Decision Log's "rows now 88 total, up from 69"); 23 non-English sources listed, all 19 new files among them. `python cic/engine/corpus_map_merge.py --check` → exit 0, *"528 distinct work(s) → 788 assignment(s) across 56 Atlas entry(ies) [check only, nothing written]"*, no error.

**File integrity.** All 19 files present in `cic/texts/`, none empty, none obviously truncated: sizes from 305 KB (Harnack) to 6.05 MB (Enarrationes), each carrying the full nine-field intake header (Title / Creator / Publisher / Publication Date / Rights / Language / Source / Provenance note / Content note) and each header consistent with its Registry row.

**Manifest.** G1, G2, G4, G5, G6, G7, G8, and G9 each carry a dated "Fulfilled 2026-09-08" paragraph (G4's reading "Further fulfilled"); G3's "Fulfilled 2026-09-05" is intact; the network-access paragraph and the "Decision from the project lead" section are both superseded-in-place rather than rewritten, exactly as the Decision Log describes. Row numbers cited in each fulfillment paragraph match the Registry. G4's residual — CSEL 58 only — is stated identically in the Manifest, in Doc_02 §1 and §9 item 1, and in the Decision Log. Apart from L2's G8 omission, the three accounts reconcile.

**§7's century-gap disclosure survives the new material.** §7 claims *"no primary source named at §1 above, and no row in `Source_Registry.md`, dates from within this 133-year gap"* (258–391). Checked against all 19 new sources: Prosper's *Epitoma Chronicon* was composed in the 430s–450s and its edition is 1892; Robinson's texts are 180 CE and 203 CE; the seven secondary works are 1892–1921; every CSEL/PL/Bruns/Bruder volume is a modern edition of a text dated outside the gap. **No revision needed at §7.** (Worth noting for a future pass, not as a finding: Prosper's chronicle *narrates* years inside the gap without dating from it, so §7's claim holds precisely as worded.)

**§8's Confidence Map needs nothing from Prosper.** The two events row 203 attests — Augustine's death in 430, and the Vandal invasion — are already in §8's top tier ("Documented / Widely Accepted … Augustine's death during the siege of Hippo 430"). A contemporary chronicle witness strengthens the evidentiary footing without moving the confidence band, and §5 already marks row 203 as not drawn on for any claim. No change required.

**Doc_01 carries no census figure**, so the 73 → 99 revision creates no conflict with it. The only Doc_01 cross-check that failed is the misattributed characterization at M1.

**Corpus-map roles.** Prosper `context` (as §5 claims); Possidius `tradition`/`assigned`; the Scillitan Martyrs' new entry `tradition`/`provisional`, mirroring the existing ANF09 entry exactly as row 204 claims; the Retractationes `tradition`/`assigned`. All independently re-parsed.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the 2026-09-08 revision and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** The new material touches two cross-world matters — Prosper's Mommsen volume being shared with the sibling Donatism build (row 203 flags it `context`/`needs-ruling` there without asserting on that thread's behalf) and Perpetua's *Passion* remaining assigned to `tertullian-s-voice` per Mark's own 2026-08-26 ruling (row 204 mirrors rather than reassigns). Both **report** an existing determination rather than making a new one, the same test §10 already applies to Optatus. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing in the revision or in this round's findings changes `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022, or any governing document. M4 is a finding that Doc_02 *paraphrased* INTAKE.md incompletely, not that INTAKE.md changed. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close on its own / two reviews disagreeing.** This round disagrees with no prior round. Rounds 1–14 reviewed a pre-2026-09-08 state and none of their findings is reopened here; every finding above is against text added or left stale on 2026-09-08. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

Doc_02's status line and §10 still describe the Round 14 disposition of 2026-09-02. Whether that line should now be amended, re-dated, or left alone is **not assessed by this round**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition. This review supplies only the input that rule takes: a finding count and a findings list.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 4 HIGH · 6 MEDIUM · 5 LOW · 2 COSMETIC.**
