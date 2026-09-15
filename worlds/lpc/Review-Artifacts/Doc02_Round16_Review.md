# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 16 Independent Adversarial Review — scoped to verifying the Round 15 fix pass

**Documents reviewed (committed state — `git status --porcelain` clean at `d3db35a`, "lpc: fix Doc_02 revision per Round 15 independent adversarial review", 2026-09-08 06:20:36 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `worlds/lpc/Doc_02_Source_Ecology.md` (157 lines)
- `worlds/lpc/Source_Registry.md` (329 lines; 212 rows)
- `worlds/lpc/Source_Acquisition_Manifest.md` (85 lines)
- `worlds/lpc/lpc_Decision_Log.md` (316 lines)
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines), for the §5 and §1 cross-document checks
- `Review-Artifacts/Doc02_Round15_Review.md`, read in full before any other file
- The vendored files in `cic/texts/` bearing on each finding, `cic/corpus-map/latin-pastoral-congregational-christianity.yaml`, and all 56 atlas files in `cic/corpus-map/`

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-08 vendoring, did not write the Round 15 fix pass, and did not write Rounds 1–15.

**Scope, stated plainly.** This round is **not** a sixteenth full review of Doc_02. Its brief was to verify, independently and against primary artifacts, whether each of Round 15's seventeen applied fixes (H1–H4, M1–M6, L1–L5, C1) actually holds — classifying each as (a) correct and complete, (b) correct but not propagated, (c) not fixed, or (d) fixed but introducing a new error — plus a fresh read of the revised §1 and the two engine scripts. Round 15 itself was treated as a claim to re-derive, not as authority: where its own finding text proved subtly wrong in a way the fix now inherits, that is stated below.

**Method — what was actually re-derived, not trusted.** Every figure in this review was recomputed this session from the raw artifact. `yaml.safe_load` across all 56 atlas files in `cic/corpus-map/` (59 `.yaml` files less `AUTHOR-IDS.yaml`, `UNATTRIBUTED.yaml`, `WORKS.yaml`); `git show <commit>:cic/corpus-map/latin-pastoral-congregational-christianity.yaml` at all five historical revisions found by `git log --follow`, each re-parsed and set-differenced against its predecessor to establish exactly which entries were added on which date; a fresh regex parser over all 212 Registry rows extracting every column by position; direct `grep`/`sed` inside the vendored text files; and both engine scripts run. Nothing was carried forward from Round 15's tables, from `lpc_Decision_Log.md`, from the commit message, or from the task brief that commissioned this review — including the brief's own characterizations of what the fixes claim, several of which do not match the committed text.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 4 HIGH · 5 MEDIUM · 6 LOW · 3 COSMETIC.**

**Fifteen of the seventeen fixes hold on their own terms**, several of them exactly and completely: H1's corrected row list is right on every one of its nine rows, independently checked; H4's seven Registry rows and L3's row 61 all now lead with an accurate pointer; M1's Prosper/Doc_01 correction is exact on both limbs; M5 added real, substantive, source-accurate content in all three named sections; the H2/H3 census arithmetic (99 / 97 / 90 / 9 `context` / 2 duplicates / 7 modern secondary / 22 added today) is correct in every figure this reviewer recomputed. Both engine scripts still exit clean.

**The findings below are of two kinds.** Two fixes were applied at one of the two sites the review named, leaving the document self-contradicting (H1, and the propagation half of H2/H3's own arithmetic). Four fixes introduced a *new* checkably-false claim the build thread did not have before (H2, H4, M1, M3, L6) — three of them in the very sentences written to correct a false claim of the same kind. Two further defects are Round 15 misses now surfaced by re-checking the artifacts its fixes point at (M2, M3).

---

## HIGH

### H1. M2 was fixed at §1 and not at §2 — §2 still calls Bruder's and Migne's editions "a specific base Latin critical edition," and §1 now announces the opposite correction, so the two sections directly contradict each other

Round 15's M2 quoted **two** sites. §1's has been fixed, with an explicit correction banner:

> **Two of these are the Maurist text, not a modern critical edition — corrected here (Round 15's own M2) from an earlier draft that called all of them "critical-edition second witnesses" against those two rows' own emphatic disclosure to the contrary:** On Christian Doctrine and the Enchiridion (Bruder's 1838 Tauchnitz printing of the Maurist text, row 200, whose own Verification Note states plainly it is "NOT a modern critical edition") and the Expositions on the Psalms (Migne's 1861 printing, row 201, same disclosure) are both pre-critical texts…

§2's Augustine *Transmission History* entry, in the current file (line 47), is **unchanged**:

> a specific **base Latin critical edition** is now vendored and directly checkable for the Confessions (CSEL 33, row 197), the general and Jerome-cluster correspondence (CSEL 34/1–2, 44, 57 Pars IV, rows 195–196, 193), City of God (CSEL 40, rows 198–199), **On Christian Doctrine and the Enchiridion (the Tauchnitz/Maurist text, row 200), the Expositions on the Psalms (Migne PL 36–37, row 201)**, and the Retractationes (CSEL 36, row 209).

`grep -o "critical" Doc_02_Source_Ecology.md` returns the phrase "base Latin critical" once, at line 47, still governing rows 200 and 201. Verified against the diff `c803529..d3db35a`: that clause was not touched.

This is worse than the pre-fix state, not merely unimproved. Before the fix, §1 and §2 were consistently wrong; now §1 states that two of these are *not* critical editions and §2, five lines later, states that a critical edition *is* vendored for them. It is the same both-limbs-in-one-document defect Round 15 rated HIGH at its own H1, and it lands in the sentence whose whole purpose is to report that the critical-apparatus gap has been closed.

### H2. §2's new Possidius *Transmission History* bullet — written this pass for M5 — asserts that Pontius's *Life* "reaches this corpus only via a 19th-century English translation," which the same revision's own row 194 falsifies and which §1 of the same document contradicts three sections earlier

The new bullet (line 61):

> *Transmission History:* Vendored as a genuinely bilingual edition (Weiskotten's 1919 Latin text with a complete facing English translation, Registry row 192) — a different transmission footing than Pontius's *Life*, **which reaches this corpus only via a 19th-century English translation (Migne-based, per the entry above) with no facing Latin at all in the vendored volume.**

Pontius's *Life* reaches this corpus in Latin as well, vendored **in this same 2026-09-08 pass**:

- §1 of this document, line 29: *"Latin-language second witnesses are now vendored for: the whole Cyprianic corpus, letters and treatises alike, **including the spuria and the Vita** (Hartel's CSEL 3, complete, rows 191 and 194)."*
- Registry row 194's own Licensed-For: *"**The Vita specifically** as this world's own Cyprian-side formation-narrative material, corroborating the already-vendored ANF05 English translation (row 7) **at its own Latin source**."*
- Independently confirmed in the file: `cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` carries the heading `VITA CAECILII CYPRIANI` at line 40258, and the file's own content note names the Vita as component (2) of three.
- The corpus map carries it as its own census entry, added today: `Vita Caecilii Cypriani (attributed to Pontius the deacon) | pontius | tradition`.

The bullet's whole rhetorical work — the Possidius/Pontius contrast that justifies treating Possidius as a distinct transmission footing — rests on a negative that this revision itself abolished. §2's own Pontius *Transmission History* bullet (line 54) was also left unrevised and still describes the *Life* as transmitting only "inside this same volume and edition" (ANF05), with no mention of row 194.

### H3. §1's primary-source-base parenthetical pairs the `tradition`-only entry count (90) with the **all-roles** distinct-title count (97), under a banner that has just excluded exactly what makes 97 larger than 88

The revised opening (line 13):

> this world holds the largest and most direct primary-source base of any confirmed world in the portfolio to date, **among what is currently vendored, on its own primary-source (`role: tradition`) count** (90 `tradition`-role census entries as of 2026-09-08, **97 distinct titles counting each once** — up from 73, all `tradition`, at this document's own original drafting…)

Recomputed directly from `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` this session:

| measure | value |
|---|---|
| entries, all roles | 99 |
| distinct titles, all roles | **97** |
| entries, `role: tradition` | 90 |
| **distinct titles, `role: tradition`** | **88** |
| entries, `role: context` | 9 |

The 97 is the whole-census figure. It counts Delehaye 1921, Harnack 1913, Monceaux I–III, both von Sodens, Prosper and the Codex Theodosianus — the nine `role: context` entries the *same sentence's own correction*, two clauses later, says "does not belong inside a 'primary-source base' figure at all." Offered as the "counting each once" refinement of a figure explicitly scoped to `role: tradition`, 97 is the wrong number by nine; the correct primary-source distinct-title count is **88** (90 tradition entries less the two exact-title duplicates, both of which fall inside the tradition set).

This is a new defect. The pre-fix sentence cited only the raw 99; the fix introduced the 90/97 pair and mismatched their scopes.

### H4. The M3 fix newly asserts that row 191 was "the first Latin exception" — row 88 is, by three days, and Round 15's own M3 said so

The rewritten passage (line 29):

> row 191 (**the first Latin exception**) did not exist until 2026-09-05, four days later, so there was no exception at all at drafting, and by 2026-09-08 … four Latin or bilingual sources already existed (rows 88, 191, 192, 193), not "a single" one.

Registry row 88 is `codex-theodosianus_latinlibrary.txt` — Latin (its header carries `Language: lat`; `texts_registry.py` reports it under non-English sources), Boundary Status Native, **Added: 2026-09-02, `lpc` build thread**, Discovery: *"Project lead direct supply / 2026-09-02."* Row 191's Added column reads **2026-09-05**. Row 88 therefore precedes row 191 as this world's first Latin-language vendored source by three days, and reached the census first as well: `git show cf1033e:` (2026-09-03) shows the Codex Theodosianus as census entry 74, while `97419d7:` (2026-09-05) adds Hartel's CSEL 3 as entry 75.

Round 15's own M3 named row 88 and its 2026-09-02 date explicitly. The corrected sentence lists row 88 among the four two clauses later, so the document simultaneously knows row 88 exists and calls row 191 first. The sentence exists to correct a false "single exception" claim and reintroduces a false "first" claim in the same breath.

*(Round 15 is not wholly right here either, and the fix was correct to avoid its wording: Round 15's M3 said rows 88, 193 and 192 "were all vendored first." Only row 88 was. Rows 192 and 193 carry the same Added date as row 191, 2026-09-05, and in census-commit order row 191 (`97419d7`) precedes both. The fix's neutral "four … already existed" is the right formulation; only "the first Latin exception" needs to go.)*

---

## MEDIUM

### M1. The "three earlier passes" count is wrong at both of the two sites that state it, the two sites disagree with each other on the date range, and one of them attributes a non-Manifest addition to Manifest G1/G3/G4

§1, line 13:
> The growth was not a single event: 73 (2026-09-01) → 77, across **three earlier passes (2026-09-03 through 2026-09-05, `Source_Acquisition_Manifest.md`'s own G1/G3/G4 fulfillments — §9 item 1 below)** → 99 today.

§1, line 29:
> four (rows 88, 191, 192, 193) already existed before this revision began, added in **three earlier passes between 2026-09-02 and 2026-09-05**

The census's actual history, each revision re-parsed and set-differenced this session:

| commit | date | works | entry added |
|---|---|---|---|
| `0269b68` | 2026-09-01 | 73 | — |
| `cf1033e` | 2026-09-03 | 74 | Codex Theodosianus (`context`) — row 88 |
| `97419d7` | 2026-09-05 | 75 | Hartel CSEL 3 Pars I–II — row 191 (G1) |
| `7ead600` | 2026-09-05 | 76 | Possidius *Vita* — row 192 (G3) |
| `4911c02` | 2026-09-05 | 77 | Goldbacher CSEL 57 Pars IV — row 193 (G4) |

Three defects follow, all checkable:

1. **73 → 77 is four additions across four passes, not three.** Both sites say three.
2. **The 2026-09-03 addition is not a Manifest G-item.** Row 88 was project-lead-supplied outside the numbered list — the Manifest says so itself, in its own parenthetical: *"the same pattern Mark has already followed directly this session for the *Codex Theodosianus* (Registry rows 44 and 88), **outside this Manifest's own numbered list**."* Line 13 attributes the whole 73→77 window to "G1/G3/G4 fulfillments," which are all three dated 2026-09-05.
3. **The two sites give different windows for the same set** — "2026-09-03 through 2026-09-05" at line 13 (census-staging dates) versus "between 2026-09-02 and 2026-09-05" at line 29 (Registry Added dates) — without either naming which clock it is on. The cross-reference "§9 item 1 below" supports neither: §9 item 1 records G3 as closed 2026-09-05 and does not mention the Codex Theodosianus at all.

### M2. Registry row 196's Licensed-For, and the CSEL 44 file's own intake header, both claim Letter 185 is inside CSEL 44 — it is not, and row 193 says the opposite (a Round 15 miss, not a fix defect)

Row 196's title states its own range: *"Pars III (**Epistulae CXXIV–CLXXXIV A**), CSEL 44."* Its Licensed-For then says:

> Part of the edition row 61 names — the Latin original behind the already-vendored NPNF translation for this letter range, **including Letter 185 (row 12) at its own Latin source**

The vendored file's own Content note repeats it: *"Covers Epistulae 124-184A, **including Letter 185 (the Correction of the Donatists … cited at Registry row 12) at its Latin critical-text source**."*

Independently checked in the files:
- `grep -c "CLXXXV\b" cic/texts/augustine_epistulae-124-184a-lat_goldbacher-csel44.txt` → **0**. The file's last letter heading is `CLXXXIV A`, and its final line of text is `Explicit epistola sci augustini ad petru et habraham` — Ep. 184A, *Ad Petrum et Abraham*.
- `cic/texts/augustine_epistulae-critical_goldbacher-csel57-pars4.txt` carries `EP. CLXXXV— CCLXX` at line 34 and the heading `CLXXXV.` at line 44.
- Registry row 193 states it correctly: *"including **Letter 185 itself (row 12), the first letter in this file's own range**."*

Letter 185 (*The Correction of the Donatists*) is among the most load-bearing texts in this world's construction — Doc_01's entire state-coercion finding rests on it, and §1 of this document cites it twice. A downstream builder following row 196 to its Latin source is sent to a file that does not contain it. Round 15 certified that "every new row number Doc_02 cites … says what Doc_02 says it says"; it did not check the new rows against each other or against their own stated ranges.

### M3. Registry row 204's Boundary Status column says "Native" while its own Exclusion Reason and Licensed-For columns say Excluded — and Doc_02's new L4 disclosure now asserts the Excluded reading as the row's own

The L4 fix added, at §1 line 27:

> (**a Latin/Greek second witness to this same excluded text is now vendored, row 204, added this revision — mirroring row 28's own Excluded disposition exactly, not reopening it**)

Row 204's columns, extracted by position this session:

| column | value |
|---|---|
| Boundary Status | **`Native` (Scillitan Martyrs portion only — see Boundary Status note)** |
| Exclusion Reason | **"Scillitan Martyrs: Excluded, Named Comparandum**, mirroring row 28 exactly…" |
| Licensed For | "N/A — **excluded/out-of-boundary for lpc on both counts**…" |

The Boundary Status cell restricts a *Native* classification to the Scillitan Martyrs portion; the Exclusion Reason cell says the Scillitan Martyrs portion is *Excluded*. The two cells contradict each other about the same portion of the same file. Across all 212 rows the Boundary Status column takes exactly three values — `Native` (207), `**Excluded**` (4), and this one hybrid — so row 204 is the sole row where the column and the Exclusion Reason disagree.

Round 15's L4 said only that row 204 was undisclosed in Doc_02 and that "both texts remain excluded/out-of-boundary, correctly"; it did not read the Boundary Status column. The fix has now imported that unexamined reading into Doc_02 as an "exactly" claim. Either the row's Boundary Status should read `**Excluded**` for the Scillitan portion, or Doc_02's "exactly" must be softened — but as the two documents stand, one of them is wrong.

### M4. §1's M4 carve-out overstates its own headline example: an English rendering of the Retractationes *is* vendored in this corpus, and §2 of this same document uses it

The rewritten clause:

> the Retractationes (row 209) and the Acta Proconsularia (inside row 194) are both original-language-only, **with no English translation vendored anywhere in this corpus to cross-check against** — real, new, citable content on that basis, not merely a check on an existing rendering.

The Acta Proconsularia half is exactly right: `grep -io "proconsular"` over `anf05_hippolytus-cyprian-caius-novatian.xml` returns **0** hits, and re-checked across rows 194–212, no other newly-vendored file lacks an English counterpart that the fix misses (row 202's Code of Canons sits behind NPNF2-14/row 26; row 204's Scillitan Martyrs behind ANF09/row 28; row 194's spuria behind ANF05/row 6, as the corpus map's own note for that entry states; rows 205–208 and 210–212 are `context` secondary works the sentence does not govern).

The Retractationes half is not. `cic/texts/npnf105_augustine-anti-pelagian-writings.xml` carries a dozen-plus `<div2 title="Extract from Augustin's Retractations.">` sections in English, and `npnf104` carries the specific passage this document itself quotes — verified present verbatim this session: *"who strive to defend themselves by the authority of the most blessed bishop and martyr Cyprian."* §2 of Doc_02 draws on exactly that rendering, and row 209's own Licensed-For exists to close it: *"Closes, at its own public-domain source, a citation row 13 previously disclosed as held only at second hand, **via an NPNF editor's own quotation of Retractationes II.18**."*

There *is* an English rendering to cross-check, it is the one this world's construction actually uses, and row 209's own value proposition is that cross-check. Row 209's careful wording ("not otherwise vendored **in English translation**") survives this; Doc_02's blanket "no English translation vendored anywhere in this corpus to cross-check against" does not.

### M5. No `lpc_Decision_Log.md` entry records the Round 15 fix pass, against the practice this document's own status line asserts — and Round 15's C2 non-fix is disclosed in no artifact at all

`grep -n "^### " lpc_Decision_Log.md` shows the last entry as *"2026-09-08 — G1 closed in full; G4 narrowed to one small residual…"*. The Round 15 fix pass (commit `d3db35a`, six files changed) has no entry. The only Decision Log change this pass was an in-place edit to an existing entry for L5.

Doc_02's own status line, and `Source_Registry.md`'s, both state the practice this omits: *"each round's findings were worked through in a following fix pass, documented in `Review-Artifacts/` and, where a finding was itself wrong or two reviews disagreed with each other, in `lpc_Decision_Log.md`."*

Two consequences, both checkable:

- **Round 15's C2 is disclosed nowhere.** `grep` across `lpc_Decision_Log.md`, `Source_Registry.md`, `Doc_02_Source_Ecology.md`, and the two files' own headers returns no mention of the `Language:`-field narrowness, no statement that it was considered and left, and no statement of the schema constraint behind that choice. `texts_registry.py` still reports both files as `[lat]`. A non-fix that exists only in a build thread's conversation is not a disclosed non-fix.
- **Observed state, deliberately not assessed:** Doc_02 now carries **12** in-text attributions to "Round 15" while its own status line reads "Fourteen independent adversarial review rounds" over the sequence "(Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0)", and `Source_Registry.md` says the same with zero "Round 15" mentions anywhere in its text. Whether and how those lines should change is a disposition question this round does not touch (see the closing note).

---

## LOW

### L1. The L1 fix left §2's row-78 aside with an unbalanced parenthesis

Line 40 now reads: *"…and 78 (Knöll's CSEL 36, public domain — **now actually vendored, row 209, 2026-09-08, closing the gap §2's own Augustine entry below names** (corrected here, independent review Round 15's own L1, from an earlier draft that pointed "above" at an entry that is in fact below this one) both now carry, corrected here from…"*

The directional fix itself is correct and verified: the Cyprian *Transmission History* bullet is line 40, the Augustine entry it points at is line 47, so "below" is right. But the inserted nested parenthetical replaced the closing `)` of the row-78 aside. Counted programmatically: the pre-fix line at `c803529` balances at **0**; the post-fix line balances at **+1**, one `(` never closed. The reader cannot tell where the row-78 aside ends and the main clause resumes.

### L2. "the second-largest now at 68" is the raw-entry figure, quoted inside a parenthetical that has just disowned the raw count as the right measure

Re-parsed across all 56 atlas files this session, lpc leads on all three counts and the superlative holds — but the runner-up figure differs by measure:

| count | lpc | second-largest |
|---|---|---|
| raw entries | 99 | 68 (`post-apostolic-house-church.yaml`) |
| distinct titles | 97 | 67 (`post-apostolic-house-church.yaml`) |
| `role: tradition` | 90 | 59 (`alexandria-catechetical.yaml` / `post-apostolic-house-church.yaml`, tied) |

The revised sentence now leads with 90 and 97, says "the largest … **on every count attempted**" (true), and then gives "68" — which is the comparator on the one count the sentence's own correction rejects. Pre-fix, 99 and 68 at least measured the same thing.

### L3. "roughly nine further second-witness entries" was adopted from Round 15's floor figure rather than re-derived; across the window the sentence actually scopes, the number is eleven

The sentence says *"the 99 also contains … roughly nine further second-witness entries for works the original 73 already counted."* Round 15's H3 said "**at least** nine" — a floor, and a floor computed over today's 22 additions only.

Set-differenced against the 73-entry census this session, the second witnesses to already-counted works inside the 99 are: City of God I–XIII, City of God XIV–XXII, Confessions (CSEL 33), Epistulae 1–123, Epistulae 124–184A, Enarrationes complete, *De Doctrina Christiana*, Codex Canonum, and *Vita Caecilii Cypriani* (nine, added today) — **plus** Hartel CSEL 3 Pars I–II and Goldbacher CSEL 57 Pars IV, both second witnesses to entries in the 73 and both inside the 99 since 2026-09-05. Eleven, not nine. The full decomposition of the 26 additions is 2 exact duplicates + 11 second witnesses + 13 genuinely new works (Acta Proconsularia, Opera Spuria, Retractationes, Possidius, Codex Theodosianus, and the seven secondary studies plus Prosper).

This is the recurring pattern `lpc_Decision_Log.md` already tracks: a review artifact's own figure adopted into a live document without independent re-derivation.

### L4. Rows 78 and 90's new pointer sentences refer to "the identifier below," which in one row sits above and in the other does not exist

Row 78: *"**Now vendored, row 209 (2026-09-08)** — closing Manifest G6; **the identifier below** (`sanctiaureliaugu36augu`) was located by opening Getty-hosted CSEL-Augustine volumes directly by number…"* — the identifier is given inline in that very clause, and the text *below* it still reads *"this specific volume's own identifier **has not been located** despite repeated searches across two rounds."*

Row 90: *"…closing Manifest G8 — **the identifier below** was found by searching for the serial's own title rather than the short article's."* Row 90 contains no identifier anywhere: its URL/Identifier column is `—`, and the text below reads *"**no Internet Archive identifier located** despite a search this session."* The identifier (`quellenundforsch12deutuoft`) is in row 211, not below.

The superseded-in-place pattern is the right one and the pointer sentences are otherwise correct; only their internal deixis fails.

### L5. The eight Registry rows corrected this pass carry no round attribution, against this Registry's own uniform practice

`grep -c "Round 15" Source_Registry.md` returns **0**, though `git diff c803529..d3db35a` shows eight rows changed (40, 41, 56, 61, 78, 89, 90, 99). Every comparable in-place correction elsewhere in this Registry names the round that found it — row 56 (*"corrected here (Round 4's…"*), row 61 (*"Round 4's own PRESS disposition #1"*), row 13 (*"corrected here a second time (Round 4's own H1)"*), row 23, row 25, and others. Doc_02, the Manifest, and the Decision Log all attribute their Round 15 fixes; the Registry alone does not, which makes its own provenance trail discontinuous at exactly the rows Round 15 forced.

### L6. The new Possidius entries state the peer-not-subordinate contrast more flatly than the one source the build thread reports having consulted supports

§2: *"Represents a peer bishop's own retrospective account of a fellow bishop and close friend, **not a subordinate's** (contrast Pontius, a deacon writing of his own superior)."* §4 repeats it: *"a peer bishop's own retrospective, **not a subordinate's**."*

Both entries also disclose that the work has not been read — §2: *"not yet independently read this session beyond the specific passages the vendoring pass sampled for OCR quality."* The one part of the work that *was* sampled, Weiskotten's own introduction, says (read directly this session, `possidius_vita-augustini_weiskotten1919.txt` lines 300–330): Possidius entered Augustine's monastery at Hippo c. 391 "probably not over thirty, as Augustine was then thirty-five," was "in all likelihood younger than **his teacher and friend**," and only became bishop of Calama in 397, succeeding Megalius. The contrast at time of composition is defensible; "not a subordinate's," stated twice without qualification, is not what the vendored edition's own account of the relationship supports, and it bears directly on the idealization risk both entries otherwise name well.

*(Everything else in the Possidius material checks out against source: "bishop of Calama" and the ~forty-year friendship are both in the file — Possidius's own epilogue is quoted there as "almost forty years"; "for decades alongside Augustine's own episcopate" is 397–430, correct; Confidence A and the bilingual description match row 192 exactly; and Doc_01 §5's two quoted phrases, "only as NPNF's own editorial note" and "not vendored in this corpus," are verbatim, in §5, and the NPNF Megalius note is confirmed present in `npnf101`.)*

---

## COSMETIC

### C1. Three of the eight corrected Registry rows open with four asterisks

Rows 40, 41 and 56 each begin `****…**` — e.g. row 41: `****Now vendored, inside row 194 (2026-09-08)** — Hartel's CSEL 3 Pars III…`. The opening delimiter is four asterisks against a two-asterisk close, so the leading `**` renders as literal text. Rows 61, 78, 89, 90 and 99 (and pre-existing rows 28 and 39) all use `**` correctly. Introduced this pass.

### C2. §2's corrected row list attaches three rows to a label that does not describe them

The H1 fix produced the right *set* — 15, 18, 19, 21, 22, 23, 25, 13, 14, each independently confirmed below — but reads: *"the anti-Manichaean corpus, the anti-Pelagian corpus, the Tractates on John and related exegetical works (row 21…), the Sermons, **the catechetical/doctrinal-moral treatises grouped at Registry rows 15, 18–19, 22–23, 25**…"* Rows 19, 22 and 23 are the Sermons, the anti-Manichaean corpus and the anti-Pelagian corpus — each named separately in the same sentence — so the composite row range is hung off a label describing only rows 15, 18 and 25. Pre-existing in structure; the fix reproduced it while adding row 21 as a parenthetical outside the range.

### C3. The C1 header fix silently normalizes the OCR of the line it quotes, in a paragraph that says no OCR error was corrected

`harnack_vita-cypriani-commentary-lat-deu_1913.txt`'s provenance note now discloses the residue accurately in substance — *"two trailing lines of that same list (a final catalogue entry and the words 'Fortsetzung s. Seite III d. **Umschlags**')"* — and the file does carry exactly two such lines. But the line as it stands in the file reads `Fortsetzung s. Seite III d. UraschlagR.` The same paragraph ends *"nothing else altered, **no OCR error corrected**."*

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**H1 — the corrected row list, checked exhaustively rather than only for row 16's removal.** The current list is 15, 18, 19, 21, 22, 23, 25, 13, 14; row 16 is gone. For each of those nine rows, the claim that no base Latin edition is vendored was verified against the actual contents of `cic/texts/`: the Latin Augustine files present are `confessiones-lat_knoll-csel33`, `civitate-dei-1-13` and `-14-22_hoffmann-csel40`, `doctrina-christiana-enchiridion-lat_bruder1838`, `enarrationes-in-psalmos-lat_migne-pl36-37`, `epistulae-1-123-lat_goldbacher-csel34`, `epistulae-124-184a-lat_goldbacher-csel44`, `epistulae-critical_goldbacher-csel57-pars4`, and `retractationes-lat_knoll-csel36`. None of them covers *De Baptismo* (13), *Contra Litteras Petiliani* (14), *De Catechizandis Rudibus* (15), the creedal works (18), the Sermons (19), the Tractates on John and related exegetical works (21), the anti-Manichaean corpus (22), the anti-Pelagian corpus (23), or *De Trinitate* and the grouped doctrinal-moral treatises (25). The complement was checked too, so the list is neither over- nor under-inclusive: every remaining Augustine row in the 9–25 range **is** closed — row 9 by 197, rows 10–11 by 195/196, row 12 by 193 (CSEL 57, whose range opens at Letter 185), rows 16–17 by 200, row 20 by 201, row 24 by 198–199. **This fix is correct and complete.**

**H2/H3 — every census figure the fix states, recomputed from the raw YAML.** 99 entries; 97 distinct titles; `Counter({'tradition': 90, 'context': 9})`; exactly two duplicate titles (`The Enchiridion (On Faith, Hope, and Love)`, `The Passion of the Scillitan Martyrs`); the nine `context` entries are Delehaye, Harnack, Monceaux ×3, von Soden ×2, Prosper and the Codex Theodosianus, of which **seven** are modern (1901–1921) secondary scholarship, exactly as §1 now says. The 2026-09-01 baseline re-parsed at `0269b68`: **73 entries, 73 distinct titles, `Counter({'tradition': 73})`, and every source_file an ANF/NPNF English volume** — so "entirely English-only on 2026-09-01" is exact. Today's additions, set-differenced against `4911c02`: **22**, of which 14 `tradition` (all Latin/Greek originals) and 8 `context`, with nothing removed — so "Of today's own 22 additions, all are original-language second-witness or `context`-role material" holds. The superlative holds on all three counts (99>68, 97>67, 90>59). H2's limb-2 correction — Possidius's row 192 as new English primary-narrative content inside the 73→99 window — is accurate against row 192's Confidence A and its bilingual Verification Note.

**H4 and L3 — all eight rows.** Rows 40, 41, 56, 78, 89, 90, 99 and 61 each now open with a bold, dated pointer to the fulfilling row, and each pointer's target was checked: 40→205, 41→inside 194, 56→206–208, 78→209, 89→210, 90→211, 99→212, 61→193/195/196 with CSEL 58 correctly named as the sole residual. No row in the set still leads with a bare "Not currently vendored." **Both fixes hold**, subject to L4's deixis defect and C1's markdown defect.

**M1 — the Prosper correction, both limbs.** Doc_01 searched in full: **zero** hits for "eventual outcome," "wider siege," "439," "Prosper," and "Carthaginem." Doc_01 §2's ending-point bullet (line 27) states the 430 boundary on general historical grounds with no primary source cited, exactly as §5 now says. In the vendored text, Augustine's death is at line 54206 under the heading `Theodosio XIII et Valentiniano III. a. -130` (line 54198); the Carthage entry is c. 1339 at line 54558 (`Gisiricus … Carthagineni dolo pacis iiivadit`), fixed to 439 by Mommsen's own additamentum at line 55225 (`ad a. 4o'J c. 1339`). The two entries are now correctly separated, the 439 entry correctly identified as a different city nine years later, and the misattributed characterization correctly withdrawn with its own disclosure. **Correct and complete.**

**M5 — real content, in all three places, source-accurate.** §1 gained a substantive Formation-narrative paragraph, §2 a full five-dimension Author Gravity entry, §4 a full Authorship/Proximity/Genre/Formation-ecology/Author-Gravity-risk assessment. Doc_01's two quoted phrases are verbatim and in §5; the NPNF Megalius note is present in `npnf101`; Possidius's see (Calama), the ~forty-year friendship, and the 397 succession to Megalius are all confirmed in the vendored edition. Subject only to L6 and H2 above.

**M6 — Harnack.** Now named in §3 with an accurate description ("a critical study, commentary, and German translation of the already-vendored Vita Cypriani"), matching row 205's Licensed-For and the file's own header, which quotes Harnack's preface confirming his is the first German translation and that his Latin is Hartel's text with noted deviations. The count correction four→**five** works is right: Monceaux I–III (one work, three rows), von Soden ×2, Harnack, Delehaye — five works, seven rows. The fix also resolved Round 15's uncounted secondary observation by adding "(Delehaye excepted, below)" to the blanket negative.

**L2 — propagated to both documents.** Doc_02 §9 item 1 and the Manifest's closing status update both now name eight items (G1, G2, G3, G5, G6, G7, **G8**, G9), each with its own correction note.

**L5 — the Decision Log ordinals, independently recounted.** Rows 194 and 197–204 are nine rows, and each names exactly one file on disk; rows 195 and 196 name one file each, making them the tenth and eleventh — as the corrected text now says. The entry's "Ten sources" headline reconciles against its own context (ten sibling-session *sources*, one of which — Goldbacher's *Epistulae* — this thread vendored as two files), so no residual defect there.

**C1 — the Harnack header.** Now discloses the two surviving advertisement lines, which are genuinely two and genuinely present at the file's head (`1909. (Bd. 34, 2b) M. 2 —` and the *Fortsetzung* line), immediately above the `DAS LEBEN CYPRIANS` title page. Subject only to C3.

**Registry table integrity.** All 212 rows re-extracted programmatically: numbers 1–212 complete, **no gap, no duplicate, no row number appearing twice**. All 13 columns present on every row checked.

**Engine scripts, both re-run this session.** `python cic/engine/texts_registry.py` → **exit 0**, *"OK: every vendored file has a header-verified rights line (public domain, or a recognized open licence), an ENTRIES row, and no ENTRIES row points at a missing file"*; 23 non-English sources listed. `python cic/engine/corpus_map_merge.py --check` → **exit 0**, *"528 distinct work(s) → 788 assignment(s) across 56 Atlas entry(ies) [check only, nothing written]"*.

**The flagged extraction hazard, re-verified rather than carried forward from Round 15.** `grep -c "ARNOBII" cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` → **0**. The Vita's heading is at line 40258 and the Acta at line 41413 (`ACTA PEOCONSVLARIA.`, OCR R→E), both where §9 item 8 and row 194 say they are.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the fix pass and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** The fix pass changed no cross-world placement. M3's row-204 column conflict is a within-Registry consistency question about a row that mirrors, rather than reasserts, Mark's own 2026-08-26 Perpetua ruling; M2's row-196 error is internal to this world's own Registry. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing in the fix pass or in these findings changes `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022, or any governing document. M5's Decision Log gap is a finding that an existing practice was not followed, not that the practice changed. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round disagrees with Round 15 on two narrow points of fact, both stated above and both resolved here against the primary artifact rather than by preferring either round's authority: Round 15's M3 said rows 88, 192 and 193 "were all vendored first" relative to row 191, when only row 88 was (H4's parenthetical); and Round 15's H3 offered "at least nine" second witnesses as a floor over today's additions, which the fix converted into a point estimate for the whole 73→99 window (L3). Neither disagreement is unresolvable, and neither requires the project lead: both were closed by re-parsing the census's own commit history. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

Doc_02's status line and §10, and `Source_Registry.md`'s status line, still describe the Round 14 disposition of 2026-09-02 and still read "Fourteen independent adversarial review rounds." Whether those lines should now be amended, re-dated, or left alone — and what disposition follows from this round's counts — is **not assessed here**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition. The staleness is reported at M5 as observed state, alongside the Decision Log gap, because it is a checkable record-consistency fact; the decision about it is not this round's to make. This review supplies only the input that rule takes: a finding count and a findings list.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 4 HIGH · 5 MEDIUM · 6 LOW · 3 COSMETIC.**
