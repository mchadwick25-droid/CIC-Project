# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 24 Independent Adversarial Review — scoped to verifying the Round 23 fix pass (eleven findings addressed, one deliberately declined), a sixth spot-check of Round 19's declined C1, an independent re-run of the run-aware bold-nesting test, and a cold sweep extended across the whole of the two shared machine-readable artifacts Round 23 opened for the first time and the generated files they feed

**Documents reviewed (committed state — `git status --porcelain` clean, 0 lines, at `cc489ab`, "lpc: fix Round 23 review findings on Doc_02 revision (11 of 11)", 2026-09-08 10:20:18 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Doc_02_Source_Ecology.md` (156 lines by `wc -l`, as are all counts in this list; §1 through §10 read in full, cold)
- `Source_Registry.md` (329 lines; all 212 rows re-parsed by column position, all eleven columns, with two independent sweeps of the Licensed-For **and** Verification-Note columns under a wider pattern list than Round 23's own)
- `Source_Acquisition_Manifest.md` (89 lines, read in full)
- `lpc_Decision_Log.md` (341 lines, read in full — every entry, with the three 2026-09-05 intake entries read paragraph by paragraph against the vendored files, the Registry rows, the Manifest, **and** the two shared registries those entries name as steps of the same intake)
- `Review-Artifacts/Doc02_Round23_Review.md` (269 lines, read in full) and `Doc02_Round22_Review.md`, plus `git show cc489ab`, `git diff d35f00a..cc489ab` at word level on every changed line, and `git log --oneline -- world-build-docs/_cross-world/{download-queue-seed.yaml,DOWNLOAD-QUEUE.md}`
- **`cic/texts/REGISTRY.yaml` (all 88 entries parsed, every lpc-related `notes` field read in full against the Registry row and the vendored file header it describes), `cic/texts/README.md` (regenerated to a scratch copy and byte-compared against the committed one), `world-build-docs/_cross-world/download-queue-seed.yaml` (all 22 queue entries), and `world-build-docs/_cross-world/DOWNLOAD-QUEUE.md` (regenerated and diffed, then restored)** — the last of these read for the first time in this review sequence
- The vendored files opened directly: `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`, `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`, `augustine_epistulae-critical_goldbacher-csel57-pars4.txt`, `augustine_epistulae-124-184a-lat_goldbacher-csel44.txt`, `possidius_vita-augustini_weiskotten1919.txt`, `perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`, `prosper_chronica-minora-1-lat_mommsen1892.txt`, `harnack_vita-cypriani-commentary-lat-deu_1913.txt`
- All 57 `works`-bearing atlas files in `cic/corpus-map/`, plus `cic/corpus-map/tertullian-s-voice.yaml` read directly; both engine scripts
- **Two live archive.org fetches, full text plus metadata** — `sthascicaecilic01hartgoog` (2,147,270 bytes) and `CSEL57` (1,587,544 bytes) — run because this pass asserts a scan-provenance correction, an item identity, and a chrome-removal at a file's tail, and all three are checkable only against the source items themselves

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-05 or 2026-09-08 vendoring, did not write the Round 15–23 fix passes, and did not write Rounds 1–23.

**Scope, stated plainly.** Six briefs, run together. First: verify, independently and against primary artifacts, whether each of the eleven Round 23 findings the pass addressed is closed at **every** site named in **every** file named — and, since every one of the nine preceding fix passes introduced or left at least one checkable error while fixing what it targeted, look specifically for the three shapes this revision's history names (a fix that creates a new defect in the same sentence; a fix whose scope stops short of a sibling site; a claim written into a live document without re-derivation). Second: verify the two most complex corrections — the multi-file REGISTRY.yaml/README rewrite and the M1 Goldbacher provenance rewrite — at source, by re-fetching the archive.org items rather than trusting either the review or the pass. Third: verify Round 23's own declined C1 (the prior commit message's bold-line count) is genuinely a non-issue, by searching the whole repository for the wrong figure and independently recomputing the right one. Fourth: spot-check Round 19's declined C1 a sixth time. Fifth: independently reproduce the run-aware bold-nesting test and the YAML parses. Sixth: a cold sweep weighted, per the commissioning brief, toward the artifacts Round 23 established as in-scope — asking not only whether the three entries Round 23 named are fixed, but whether **other** lpc entries in the same two shared files carry the same class of staleness. Rounds 15–23 and the `cc489ab` commit message were treated as claims to re-derive, not as authority.

**Method — what was actually re-derived, not trusted.** A CommonMark render (markdown-it-py 4.2.0, `commonmark` preset) of every `**`-bearing line in all four documents (438 lines), with `<strong>` open/close counts, nesting, literal `**` survival and `****` compared line by line against a **run-aware** sequential pairing (a maximal run of two or three asterisks contributing exactly one delimiter). A fresh regex parser over all 212 Registry rows extracting all eleven columns by position, with row-number sequence, physical order, pipe count and per-row balance; then a whole-table sweep of every column under an eighteen-pattern list (`stays open`, `remains open`, `remain(s) unacquired`, `still unacquired`, `awaiting`, `not yet located`, `acquisition candidate`, `if acquired`, `currently lacks`, `open request`, `to be acquired`, `not currently vendored`, `has not been located`, `would add`, `not yet assigned`, `is not vendored`, `unvendored`). `yaml.safe_load` on both edited YAML files and on all 57 atlas files, with every census figure and comparator in Doc_02 §1 recomputed from raw YAML. `python cic/engine/texts_registry.py --write-readme` re-run against a scratch copy of the committed README and byte-compared. `python world-build-docs/_cross-world/gen_download_queue.py` re-run and diffed against the committed `DOWNLOAD-QUEUE.md`, then the file restored via `git checkout --`. Live archive.org metadata and full-text fetches, normalized-whitespace-compared against the vendored files at both ends. Direct reads of the Prosper file at 42580–42584 and 45876–45892, of the Hartel Pars III file at its title page (line 54), its index sections and its Praefatio/Vita/Acta boundaries, and of the CSEL 44 file's own letter headings. Both engine scripts re-run. Nothing was carried forward from Rounds 15–23, from `lpc_Decision_Log.md`, or from the commit message.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 2 HIGH · 4 MEDIUM · 4 LOW · 5 COSMETIC.**

**Nine of the eleven findings the pass addressed are genuinely closed, four of them exactly, and the two most complex corrections survive verification at source.** Round 23's M1 was re-derived from a live fetch rather than trusted, and it holds in every particular: `archive.org/details/CSEL57` matches the vendored Goldbacher file character for character at **both** ends (head: `M RIPTORVM ECCLESIASTICORVM … kdccccxi`; tail: `… 5 pro me] ppf (= prop- ter M`), its metadata carries no `sponsor`, no `scanningcenter` and no `source` field at all (it is a patron upload, `uploader: tedjaniszewski@gmail.com`), and a case-insensitive count of "google" over its 1,574,207 characters returns **zero**. The decision to leave the *Hartel* claim alone is equally right, and was checked the same way: `sthascicaecilic01hartgoog` carries `sponsor: Google` and `source: http://books.google.com/books?id=uuDN6Gn-9hgC`, its text contains "google" ten times, and it matches the vendored Hartel file at both ends. L3 is right on the facts and now independently confirmed twice over: that item's full text ends at `…om» Gr§(i, —` and contains the string `S. Thasci Caecili Cypriani Opera omnia` **zero** times in exact case — it is only the item's `title` metadata field — and the vendored file's tail now matches the source item's tail exactly. L1, L2, L4, C2 and C3 check out against every artifact they name; row 78 opens "Now vendored, row 209," Manifest G6 reads "G6 is now closed," rows 191/194 vendor the apparatus row 39 now says the corpus holds, and Registry row 33's three-journals-plus-one-MUSE-review distinction is now stated identically at Doc_02 §3 and Decision Log line 138.

**Round 23's own declined C1 is sound, and this pass's own count is right.** A repository-wide search finds the string "437 (now 440)" nowhere outside `Doc02_Round23_Review.md`'s own quotation of the commit message it was criticising; the only live "437" figures are Round 22's own review artifact and the Decision Log's Round 22 paragraph, both correct for the commit they describe. Independently recomputed at `cc489ab`: **438** `**`-bearing lines (Doc_02 66, Registry 200, Manifest 38, Decision Log 134) — the pass's own edits changed existing lines and added none — so the new commit message's "438" is exact.

**Where the recurrence went this time: into the rest of the two files Round 23 opened, and into the generated artifact one of them feeds.** Round 23's own diagnosis was that twenty-two rounds had swept `Source_Registry.md` and the vendored headers and never `cic/texts/REGISTRY.yaml`. This pass corrected the **three entries Round 23 quoted** in that file and swept none of the other nineteen lpc entries in it. Two of those nineteen carry claims that are flatly false and were corrected everywhere else in this build long ago: the CSEL 44 entry still says the file covers "Epistulae 124-184A, **including Letter 185**" — the exact claim **Round 16** found false and had corrected at the vendored file's own Content note ("this file does NOT include Letter 185 … an earlier draft of this note wrongly claimed it did"), at Registry row 196, and at Doc_02 — and the Robinson 1891 entry still says "**The Passio S. Perpetuae is not yet assigned to any world's own corpus map**," the exact claim **Round 17** found false and had corrected at the vendored file, at Registry row 204, and inside `cic/corpus-map/tertullian-s-voice.yaml` itself. Both are reproduced verbatim in the generated `cic/texts/README.md`. Separately, the H1 fix at `download-queue-seed.yaml` stopped at the seed: `gen_download_queue.py` was not re-run, and `world-build-docs/_cross-world/DOWNLOAD-QUEUE.md` — the shared, human-readable queue, in which lpc has exactly **one** row — still advertises "remaining volumes (CSEL 34/1, 34/2, 44, 58)" as ready to fetch. Every previous commit on this branch that touched the seed regenerated that index in the same commit; this one is the first that did not.

**And the Decision Log's own review-rounds entry was not extended.** The entry headed "2026-09-08 — Doc_02 revision: … one dated paragraph appended per round" holds exactly **eight** `**Round N**` paragraphs (15 through 22) after nine rounds; its escalation check still reads "any of the **eight** rounds' own findings"; its pattern paragraph still ends at Round 22; and Round 23's own deliberate non-fix (C1) is disclosed nowhere in the log the build's own practice designates for exactly that.

---

## HIGH

### H1. `cic/texts/REGISTRY.yaml` and the generated `cic/texts/README.md` carry two further false claims about lpc's own vendored files — one corrected at every other site since Round 16, the other since Round 17 — in the nineteen entries this pass edited three of and swept none of

**(a) The CSEL 44 entry asserts a letter range that contradicts itself, and that four other artifacts explicitly correct.**

`cic/texts/REGISTRY.yaml` line 1093, `notes` for `augustine_epistulae-124-184a-lat_goldbacher-csel44.txt`; reproduced verbatim at `cic/texts/README.md` line 159:

> Goldbacher's CSEL 44 (1904): Augustine's Epistulae 124-184A, **including Letter 185 (the Correction of the Donatists, Registry row 12) at its Latin source.**

Letter 185 is not in 124–184A, and the sentence says so in its own first clause. Re-derived from the vendored file directly: its letter headings run to `CLXXXIV A.` (line 39921) and stop; the file's single `^CLXXXV` hit (line 20250) is an apparatus cross-reference, `CLXXXVII, 39 in. seducebant…`, not a heading. `CLXXXV.` opens the *other* file, `augustine_epistulae-critical_goldbacher-csel57-pars4.txt`, at its line 44.

Every other artifact in this build already says so, in terms:
- the vendored file's own `Content note:` — *"**Corrected here (independent review, Round 16): this file does NOT include Letter 185** … an earlier draft of this note wrongly claimed it did. Letter 185 opens the NEXT part of Goldbacher's edition, CSEL 57 Pars IV (Registry row 193), not this Pars III file."*
- Registry **row 196** — *"**Corrected here (independent review, Round 16): Letter 185 is NOT in this range** — an earlier draft of this cell wrongly placed it here."*
- Registry **row 193**, which places Letter 185 as *"the first letter in this file's own range."*
- the Decision Log's own Round 16 paragraph, which records the correction as one of that round's four HIGH findings.

**(b) The Robinson 1891 entry asserts an assignment state the corpus map itself contradicts.**

`cic/texts/REGISTRY.yaml` line 1177; reproduced at `cic/texts/README.md` line 220:

> **The Passio S. Perpetuae is not yet assigned to any world's own corpus map; flagged as a candidate, not assigned here.**

`cic/corpus-map/tertullian-s-voice.yaml` carries two `The Passion of the Holy Martyrs Perpetua and Felicitas` entries (lines 6 and 23), the second with `source_file: perpetua-scillitan-martyrs-lat-grc_robinson1891.txt` and a note that itself quotes and corrects this very sentence — *"file's own accompanying task brief, which described Perpetua's Passion as 'not yet assigned…'"*. The vendored file's own `Content note:` says *"**Corrected here (independent review, Round 17): the Passio S. Perpetuae is NOT unassigned** — it is already assigned to `tertullian-s-voice` (Mark's own 2026-08-26 ruling)."* Registry row 204 and the Decision Log's own 2026-09-08 vendoring entry say the same. The registry entry is the one surviving statement of the brief's original error, and it sits in the file from which the corpus's index is generated.

**Why this is HIGH, on the calibration Round 23 set one commit ago.** Round 23 rated the identical shape HIGH with two reasons: the entries do not correct themselves anywhere in their own cell (neither of these does), and `cic/texts/README.md` "is not an lpc document — it is the shared corpus's index, read by every world's build thread." Both hold here, and one aggravating fact is new: (a) is not a stale acquisition-state claim that time overtook, but a **factual error about which letters are inside a vendored file**, of the kind a build thread in another world would act on directly. Round 16 rated the same claim HIGH-adjacent when it found it, and Round 17 certified it closed "at all four artifacts" — a count that was right for the four it named and, as with Round 22's M2 before it, short for the corpus as a whole.

**Why this pass missed it, stated precisely.** Round 23's H1 named three entries in this file by quotation; the pass fixed those three and swept for nothing else. The CSEL 44 entry sits **two entries above** the Goldbacher CSEL 57 entry the pass rewrote in the same file, and the two are cross-referenced in the same generated README paragraph block (README lines 159 and 160, adjacent). The lesson Round 23's H1 stated — that no sweep had ever been scoped to this file — was applied to the three quoted sites and not to the file.

### H2. The H1 third-site fix stopped at the seed: `DOWNLOAD-QUEUE.md` was not regenerated, so the shared cross-world queue still advertises three already-vendored Goldbacher volumes as ready to fetch — in the only lpc row it contains

The pass fixed `world-build-docs/_cross-world/download-queue-seed.yaml` line 187, narrowing `queue[9]`'s title to *"remaining volume (CSEL 58 only -- 34/1, 34/2, and 44 downloaded 2026-09-08, see entries below)"*. Correct, and verified against rows 195/196 and Manifest G4.

`world-build-docs/_cross-world/DOWNLOAD-QUEUE.md` line 18 was not regenerated and still reads:

> | S. Aureli Augustini Hipponiensis episcopi Epistulae, **remaining volumes (CSEL 34/1, 34/2, 44, 58)** | Alois Goldbacher (ed.) … | `lpc` | https://archive.org/details/corpusscriptorum58auguuoft | pd-us-by-date | lpc build thread, live web search, 2026-09-01 (vol. 58 only) |

Re-running `python world-build-docs/_cross-world/gen_download_queue.py` produces exactly one changed line — that one — confirming the seed edit is the whole of the drift and the regeneration step was simply skipped. (The file was restored to its committed state afterwards; `git status --porcelain` is clean.)

**Why this is HIGH rather than a mechanical footnote.** Three things compound:

1. **The mitigation Round 23 relied on to rate the seed instance "weaker" does not exist here.** Round 23 wrote that the seed entry is weaker "because two sibling entries in the same file do record the acquisitions, so a reader of the queue is not left with only the false statement." `DOWNLOAD-QUEUE.md` lists **only** `not-yet-downloaded` items — its header says "everything confirmed ready to fetch, in one list," and it renders seven candidate rows, of which exactly one is lpc's. A reader of the generated queue *is* left with only the false statement.
2. **This file is the audience the fix was for.** The Decision Log's own 2026-09-05 G1 entry gives the reason the queue is maintained at all: *"so another world's build thread checking this file sees the acquisition rather than a stale open request."* That is precisely the failure here, in the artifact that build thread would actually open.
3. **The pass knew the pattern and applied it once.** It regenerated `cic/texts/README.md` from `REGISTRY.yaml` for the exactly parallel case, and said so in its commit message. `git log` on the two queue files shows every prior commit that touched the seed (`c803529`, `4911c02`, `7ead600`) regenerated `DOWNLOAD-QUEUE.md` in the same commit; `cc489ab` is the first on this branch that did not.

The commit message states *"Fixed at all three."* Two of the three are fixed at the file that feeds the reader; the third is fixed only at the file that feeds the generator.

---

## MEDIUM

### M1. The corrected-away "Google Books chrome" phrase survives at the fifth site Round 23's own M1 enumerated — the Decision Log's G4 action list — while the pass fixed the identical phrase in the G3 entry one entry above it

Round 23's M1 named five sites for the Goldbacher scan-provenance error, four in a bullet list and the fifth in a sentence of its own:

> The Decision Log's own 2026-09-05 G4 entry carries it a fifth time, in its action list: *"Extracted mechanically (**archive.org/Google Books chrome** cut…)"*.

`lpc_Decision_Log.md` line 269 today, unchanged:

> - Extracted mechanically (**archive.org/Google Books chrome cut**; no trailing library-artifact this time, checked directly against the document's own true end; doubled inter-word spacing normalized; nothing else altered).

The claim is false on the same evidence the pass itself accepted and this round re-derived: `CSEL57` carries no Google metadata of any kind and its full text contains "google" zero times. The entry now contradicts the vendored file's own header, Registry row 193, and `REGISTRY.yaml` — all three rewritten by this pass — while stating the error in its own action list.

What makes this the scope-propagation shape rather than an oversight of scale is that the pass fixed **the structurally identical line** in the G3 entry, twenty-nine lines above, in the same commit: line 245 now reads *"archive.org site-navigation chrome and the library due-date slip cut — **not "Google Books chrome," per the M2 correction above**"*. The same edit, on the same kind of line, in the neighbouring entry, was not carried across — and Round 23 had quoted the surviving one in terms.

Rated MEDIUM, on exactly the footing Round 22 and Round 23 rated the same defect at the Possidius and G3 sites: a false provenance statement in the artifact of record, in a document set already disposed, on which no live substantive claim and no rights basis rests.

### M2. No Round 23 paragraph was appended to the Decision Log's review-rounds entry — leaving that entry's own heading, its escalation check, and its pattern paragraph all describing eight rounds after nine have run, and Round 23's deliberate non-fix disclosed nowhere in the record designated for it

`lpc_Decision_Log.md` line 318 heads the entry:

> ### 2026-09-08 — Doc_02 revision: independent adversarial review rounds against the 2026-09-08 source-integration revision, **one dated paragraph appended per round**, each finding real defects, most fixed …

Programmatically counted from that heading to the end of the file: **eight** `**Round N**` paragraphs, at lines 322, 324, 326, 328, 330, 332, 334, 336 — Rounds 15 through 22. Round 23 ran, produced 12 findings, and has no paragraph. Three consequences follow inside the same entry:

- **The heading's own claim is now false.** This is the third time this heading has gone stale in the way it describes: Round 20's M4 renamed it for claiming "two rounds" over six, and Round 21's L3 made it stateless for the same reason. Round 23's own clean-check verified the entry "holds exactly eight `**Round N**` paragraphs (15 through 22), matching its own 'one dated paragraph appended per round'" — that match is what this pass broke.
- **The escalation check (line 340) still reads** *"No CO-022 category applies to any of the **eight** rounds' own findings or to this entry."* Round 23's own escalation assessment (four categories, all cleared) is adopted nowhere.
- **The pattern paragraph (line 338) still ends at Round 22** and closes *"This fix pass responds by fixing the specific findings named above"* — a sentence that now describes the previous fix pass, in an entry appended to by the current one.

And the disclosure this build's own practice treats as non-optional is missing: Round 23's C1 was **deliberately not fixed**. The log's own handling of Round 19's C1 states the rule plainly — *"left as written, and logged here rather than silently declined, per this build's own standing rule."* Round 15's C2 non-fix was likewise logged, and Round 16's own M5 was precisely the finding that a fix pass's record had not been written. Here the reasoning is sound (verified above) and unrecorded outside the review artifact.

Rated MEDIUM rather than HIGH on the same mitigation logic Round 21 used for row 45 and Round 23 used for the seed entry: the record of Round 23 does exist and is committed, at `Review-Artifacts/Doc02_Round23_Review.md`, in the same commit — so a reader following the entry's own pointer to `Review-Artifacts/` finds the round. What is missing is the log's own account of it, and the three self-descriptions inside the entry that the omission falsifies. Round 16's M5 (a missing fix-pass record) and Round 20's M4 (a heading claiming the wrong round count) were each MEDIUM; this is both at once, and stays there.

### M3. The L3 correction note asserts a fact about "the archive.org item's own page-title metadata string" while the same file header's `Source:` line, two lines above it, says the item is unidentified and deliberately not guessed — the identity is derivable, and this round derives it

The L3 fix is right, and the removal is right. `cic/texts/cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`'s new `Provenance note:` reads:

> Corrected here, independent review Round 23's own L3: a further line of site chrome — **the archive.org item's own page-title metadata string**, "S. Thasci Caecili Cypriani Opera omnia," which survived the extraction at the file's own tail rather than its head — was found and removed…

That sentence can only be written by someone who knows *which* archive.org item. Two lines above it, the same header's `Source:` line says:

> The exact archive.org item identifier **was not stated when the file was supplied — to be added here once confirmed**, per this corpus's own no-guessed-identifier discipline.

The header therefore asserts a fact drawn from an item's metadata and, in the adjacent field, says the item is unknown. The same hedge stands unchanged at five further sites: Registry **row 191**'s Verification Note (*"the exact archive.org item identifier was not stated when the file was supplied and is not guessed"*), `cic/texts/REGISTRY.yaml` line 997 and `README.md` line 167, `download-queue-seed.yaml` `queue[6]`, the Manifest's G1 fulfilment paragraph, and the Decision Log's 2026-09-05 G1 entry (twice).

This is the shape Round 22 rated MEDIUM in its own M1 — *"an identity five other sites in this document set explicitly say is unknown and deliberately not guessed"* — recurring in text this pass wrote while closing a different finding.

**And, as with Round 22's M1, the useful half is that the identity holds and is now derived rather than asserted.** Live fetch this round: `https://archive.org/metadata/sthascicaecilic01hartgoog` returns `title: S. Thasci Caecili Cypriani Opera omnia`, `sponsor: Google`, `source: http://books.google.com/books?id=uuDN6Gn-9hgC&oe=UTF-8`, `date: 1868`, `possible-copyright-status: NOT_IN_COPYRIGHT`. Its `_djvu.txt` carries Google's standard digitization notice, immediately after which the text runs `CORPVS SCRIPTORVM ECCLESIASTICORVM LATINORVM … ACADEMIAE LITTEEARVM CAESAKEAE … VOL, III. PARS L … EX EECENSIONE G. HAETELIL … MDCCCLXVIII. Reprinted with the premission o£ the original publishers.` — which is the vendored file's own body opening, character for character, garble for garble. Both texts end identically at `…Ad presbyteros et diaconos explicit z, om» Gr§(i, —`. The exact-case string `S. Thasci Caecili Cypriani Opera omnia` occurs **zero** times in the item's own text; it is the `title` metadata field and nothing else. Round 23 flagged that this identity was closable "should a future pass want to close it"; the pass instead wrote a sentence that depends on it while leaving six sites saying it is open.

Rated MEDIUM: a new, checkable claim written into a disposed document set by the fix pass, in the same sentence as the fix, in direct tension with the adjacent field of the same header.

### M4. The Decision Log's G1 and G4 "What remains open" paragraphs still state acquisition positions false since 2026-09-08, while the G3 entry's identical paragraph was corrected in place by the Round 22 fix pass

Three consecutive intake entries carry a closing paragraph with the same heading. One was corrected; two were not.

**G3 (line 254), corrected:** *"**What remains open.** The exact archive.org identifier **is no longer open** — resolved above, independent review Round 22's own M1 (`sanctiaugustiniv00possrich`), corrected here from an earlier draft of this entry that still listed it as outstanding."*

**G1 (line 226), uncorrected:** *"**What remains open.** **Pars III (spuria and indices) of Hartel's edition, unaffected by this fulfillment.** The exact archive.org identifier this scan derives from, **if the project lead can supply it**, to complete the file's own Source line."* — Pars III has been vendored as row 194 since 2026-09-08 and Manifest G1 reads *"G1 is now closed in full"*; the identifier no longer requires the project lead, since network access has been confirmed working since the entry three above this one and the item is derivable (M3 above).

**G4 (line 277), uncorrected:** *"**What remains open.** G1's own Pars III, **G4's own remaining four volumes**, the exact archive.org identifiers for **both this file and the Hartel/Possidius intakes** if the project lead can supply them…"* — three of the four volumes are rows 195–196; the Possidius identifier was confirmed by the Round 22 fix pass and is stated four paragraphs above in this same log; the CSEL 57 identifier was confirmed by this very pass at three other sites.

This is Round 22's own H1 class — a present-tense claim that a real acquisition is still open, in a document whose neighbouring sibling paragraph corrects itself — at two sites no sweep has reached, because every sweep in this sequence has been scoped to `Source_Registry.md`'s columns, to the vendored headers, and (since Round 23) to `REGISTRY.yaml`, never to the Decision Log's own intake entries. Rated MEDIUM rather than HIGH because these paragraphs sit inside dated entries whose own later siblings (the 2026-09-08 entries, and the Manifest's G-item fulfilment paragraphs) do record the closures, so a reader of the log in order is not left with only the false statement — the mitigation Round 23 applied to the seed and Round 21 to row 45.

---

## LOW

### L1. The Goldbacher identifier confirmation reached three of the four sites Round 23's M1 named, and neither of the two sibling sites the Round 22 fix pass had set the convention for

Round 23's M1 was explicit about where the hedge sits: *"Row 193, the file header, REGISTRY.yaml/README and `download-queue-seed.yaml` `queue[12]` all hedge the identifier as 'very likely… `archive.org/details/CSEL57`… not independently confirmed against this specific file.' It is now confirmed."*

Three are closed. `download-queue-seed.yaml` line 250 is not:

> Mark supplied a compiled docx from an archive.org "Full text" view, **very likely the same item already identified below though not independently confirmed against this specific file.**

The claim "not independently confirmed" is now untrue — the byte-match is in this pass's own commit message. Two further sites, not named by Round 23 but treated by the Round 22 fix pass as within scope for the Possidius equivalent, keep the same wording: the Manifest's G4 *"Partially fulfilled 2026-09-05"* paragraph (*"very likely matching the item already identified above (not independently confirmed)"*) and the Decision Log's G4 context paragraph at line 260 (*"though the specific item behind this particular copy was not independently confirmed"*). The Manifest's **G3** paragraph, one entry above G4, carries exactly the treatment these need — *"**independently confirmed later, independent review Round 22's own M1: `sanctiaugustiniv00possrich`, matched byte-for-byte at both ends**"* — written by the previous fix pass.

Rated LOW rather than MEDIUM because the residue under-claims rather than over-claims: a reader is told less than is known, not something false about the source. It is recorded because `queue[12]` is a shared cross-world artifact, was named by the finding, and is listed nowhere in this pass's own commit message, which enumerates M1's sites as "the vendored file, Registry row 193, and REGISTRY.yaml/README."

### L2. The M3 enumeration fix reached row 191 alone — the vendored Pars III file's own `Content note:` still says the file "carries three components," omitting the indices and praefatio that occupy roughly half of it

The M3 fix is right where it landed. Row 191 now names all of it: *"Pars III (per the printed volume's own title page, *Opera Spuria. Indices. Praefatio* — the *Opera Spuria*, the *Vita Caecilii Cypriani*, and the *Acta Proconsularia* bound in among the spuria, plus the volume's own scriptural and name/subject indices and its editorial praefatio)."*

`cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` line 9 does not:

> Content note: **This file carries three components in sequence:** (1) Cyprian's own spuria …, (2) the Vita Caecilii Cypriani …, and (3) the Acta Proconsularia …

Re-derived by direct read of the file (42,600 lines): the spuria/Appendix runs from line 78; the indices run from roughly 19467 (a scriptural index) through `Index nominum et rerum.` at 27256 and on; `PRAEFATIO.` opens at 36057; `VITA CAECILII CYPRIANI` at 40258; `ACTA PEOCONSVLARIA.` at 41413. The two components the note omits therefore occupy lines ~19467–40257 — **roughly 49% of the file**, sitting physically between the note's own components (1) and (2). The same file's `Title:` line, two lines above, names them correctly (*"Opera Spuria, cum Indicibus et Praefatione … includes the Vita … and the Acta"*), so the header contradicts itself.

The same short enumeration survives at Registry row 194's Source column, at row 39's Verification Note, at the Hartel Pars I–II file's own `Content note:` (*"Does NOT include CSEL 3 Pars III (spuria, the Vita Caecilii Cypriani, and the Acta Proconsularia)"*), at `REGISTRY.yaml`/README's Pars III entry, and at `download-queue-seed.yaml` `queue[6]` (*"Pars III (spuria/indices)"*). Round 23 named the first three and deliberately declined to make them findings, because its own finding was the "mischaracterization" verdict, not the enumeration. That was right then; it is a live inconsistency now that row 191 has been rewritten to hold the complete list and its five siblings have not — and the Pars III file's own note is the one that states something checkably wrong about the file it heads, not merely something short.

### L3. The M1 fix removed "Google's own standard" from the chrome disclosure but kept the claim that "a public-domain usage notice" was stripped — from a source item whose own text carries none

The rewritten `Provenance note:` on `augustine_epistulae-critical_goldbacher-csel57-pars4.txt` reads:

> Mechanically extracted from the supplied docx — **archive.org site-navigation chrome and a public-domain usage notice were stripped from the head of the file** — corrected here, independent review Round 23's own M1, from an earlier draft's own "archive.org/Google Books… chrome and Google's own standard public-domain usage notice"…

Round 23's M1 flagged the whole clause, not only its Google half: *"an extraction step described on material the source item does not contain — the same second-order claim Round 22 flagged for Possidius."* Checked at source this round: `CSEL57_djvu.txt` begins, with nothing before it, `M RIPTORVM ECCLESIASTICORVM / LATINORVM / EDITVM CONSILIO ET IHPENSIS …` — the title page. There is no usage notice of any kind in the item, and its metadata carries no rights boilerplate. The residual half of the claim is therefore still an extraction step described on material the source does not contain; only its attribution was corrected.

The identical residue stands at the Possidius file (`possidius_vita-augustini_weiskotten1919.txt`, `Provenance note:`, *"archive.org site-navigation chrome and a public-domain usage notice (at the head of what was supplied) were stripped"*), written by the Round 22 fix pass, and in both files' `REGISTRY.yaml`/README entries.

Rated LOW and stated with its limit: what Mark's compiled docx contained cannot be re-derived from here, so the claim is unsupported rather than proven false. It is recorded because the four documents' own standard, applied throughout this run, is that a provenance statement is checkable against the source item, and because Round 23 named the whole clause while the fix corrected half of it.

### L4. Three mid-token line-fold breaks introduced into `REGISTRY.yaml` by this pass propagate into the generated README as broken text, one of them a broken archive.org identifier

`REGISTRY.yaml` uses folded scalars (`>-`), in which a single newline becomes a space. Three lines this pass wrote break a token across the fold, so the loaded value — and therefore `README.md` — carries a space inside it:

| `REGISTRY.yaml` | loaded / README text | README line |
|---|---|---|
| line 988, `…own present-` / `tense "is not included…"` | `an earlier draft's own present- tense` | 167 |
| line 1024, `…(archive.org/details/` / `sanctiaugustiniv00possrich, …)` | `archive.org/details/ sanctiaugustiniv00possrich` | 222 |
| line 1045, `…and Source_Acquisition_` / `Manifest G4 now stays open…` | `Source_Acquisition_ Manifest G4` | 160 |

All three are new: a scan of `REGISTRY.yaml` at `d35f00a` for lines ending in a word character followed by `_`, `-` or `/` returns only the file's own comment header at line 39; at `cc489ab` it returns lines 988, 1024 and 1045.

The identifier one carries the most weight — the file whose own governing discipline is that identifiers are never guessed now publishes one, in the shared corpus index, in a form that cannot be pasted into a URL. Rated LOW rather than COSMETIC for that reason alone; the other two are presentational.

---

## COSMETIC

### C1. Row 191's new title-page quotation is silently normalized, in a Registry whose two other OCR quotations carry an explicit per-row disclosure for exactly this

The M3 fix quotes the printed volume: *"per the printed volume's own title page, *Opera Spuria. Indices. Praefatio*."* The file's own line 54 reads, literally:

```
(OPEEA SPVRIA. INDICES. PKAEFATIO)
```

— `OPEEA` for *Opera*, `PKAEFATIO` for *Praefatio*, small caps throughout. Round 19's C3 found precisely this at rows 194 and 204 and Round 20's C3 broadened the fix, so both rows now carry a bolded per-row note (*"quoted here in normalized form, disclosed rather than left silent (independent review, Round 19's own C3; broadened, Round 20's own C3) …"*). Row 191 carries none, in a clause whose entire subject is what the title page says. Round 23's own M3 quoted the line in literal form and said why (*"per this document set's own standing disclosure practice"*); the fix adopted the reading and dropped the practice.

### C2. The C4 fix's new pointer "the Manifest's own L2 fix, below" points backwards

`lpc_Decision_Log.md` line 334, new text: *"(at line 85 when Round 21 found this; **the Manifest's own L2 fix, below**, has since inserted two lines above it, so the same paragraph is now two lines further down…)"*.

The attribution and the arithmetic are both right — verified by `git show`: the Manifest was 87 lines at `efc1a95` and 89 at `f0be10a`, and the only insertion in between is a two-line hunk at line 65, the §2 heading correction, which is Round 21's L2. But L2 is described **earlier** in the same paragraph (in its "Five LOW" clause) than C4 is (in its "Four COSMETIC" clause), so "below" sends a reader the wrong way — the same class as Round 17's own L1 (a backwards cross-reference introduced by a fix).

### C3. The C3 fix moved the undated-"this session" boundary in Doc_02 §3 from two bullets to one rather than closing it

Brown is now dated — *"bibliographic details WebSearch-verified **in this document's own original 2026-09-01 drafting session** (dated explicitly here, independent review Round 23's own C3, **for consistency with the Lancel and Burns & Jensen bullets below**…)"* — and the date is right (row 31's Discovery channel reads `WebSearch this session / 2026-09-01`; the Decision Log's 2026-09-02 entry records rows 31–33 as that day's resolved work).

The parenthetical names three of the block's four bullets. The fourth, Burns (line 67), still reads *"not independently re-read **this session**; publisher and title **WebSearch-verified**, and the publication year … resolved by the same check"* — no date on the check itself, only an indirect pointer to "Registry row 32's own 2026-09-02 update." Round 22's C4 found this pattern at 1-of-4 dated, Round 23's C3 at 2-of-4; it is now 3-of-4. Stays COSMETIC for the reason Round 23 gave: what Burns's bullet says is true, only undated, in a section where "this session" has now needed disambiguation three times in three rounds.

### C4. Five "`lpc_Decision_Log.md`, 2026-09-01 entry" pointers are ambiguous among the four entries the log dates 2026-09-01 — the unswept sibling of Round 19's C2 and Round 20's C2

Round 19's C2 found Doc_02 §2's pointer to *"`lpc_Decision_Log.md`'s 2026-09-08 entry"* ambiguous among four same-date entries; Round 20's C2 fixed it at Doc_02 §9 item 1 by quoting the entry's own title. Doc_02 line 54 uses the same good practice for another entry (*"the one beginning 'independent adversarial review rounds against the 2026-09-08…'"*).

The log dates **four** entries 2026-09-01 (lines 11, 31, 41, 53), and five live pointers name that date with no title: Doc_02 lines 15 and 23, `Source_Registry.md` lines 14, 40 and 275. Each is resolvable from surrounding context — the Cyprian-citation ones point unmistakably at the Epistle XXXIX entry, the Optatus one at the `donatism.yaml` entry — which is why this is COSMETIC and not higher, and why it is weaker than the case Round 19 found (where all four same-date entries concerned the same day's vendoring). It is recorded because it is the un-swept remainder of a defect two rounds have now fixed one pointer at a time.

### C5. `download-queue-seed.yaml` `queue[12]`'s "see the entry immediately above" no longer resolves

`queue[12]` (CSEL 57) reads *"Fulfills the CSEL-57 portion of lpc's own G4 (**see the entry immediately above for the remaining volumes**)."* When written on 2026-09-05 that was `queue[9]`, the remaining-volumes entry. The 2026-09-08 pass inserted two entries between them (`queue[10]` CSEL 34/1–2, `queue[11]` CSEL 44), so "the entry immediately above" is now the CSEL 44 acquisition. The neighbouring `queue[9]`, edited by this pass, gets its own directional language right ("see entries below" → `queue[10]`, `queue[11]`). Purely navigational; no claim is wrong.

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**The M1 provenance rewrite, re-derived from the live item rather than from the pass or from Round 23.** `https://archive.org/metadata/CSEL57` returns `identifier: CSEL57`, `title: S. Augustini epistulae (CSEL 57)`, `date: 1911`, `uploader: tedjaniszewski@gmail.com`, and **no** `sponsor`, `scanningcenter`, `source` or `contributor` field at all — a patron upload, not an institutional or Google scan. Its `_djvu.txt` is 1,574,207 characters and contains **zero** case-insensitive occurrences of "google." Whitespace-normalized, its first 200 characters and its last 200 characters are **identical** to the vendored file's own body at both ends (`M RIPTORVM ECCLESIASTICORVM … S. AVGVSTINI EPISTVLAE` / `…3 in] me M in otn edd. praeter m et Vall. 5 pro me] ppf (= prop- ter M`). Every element of the M1 correction — the not-a-Google-scan finding, the identifier, and the both-ends method — holds at source. Registry row 193, the vendored file's `Source:` and `Provenance note:`, and `REGISTRY.yaml`/README all now state it consistently.

**The decision *not* to correct the Hartel intake, re-derived the same way.** `sthascicaecilic01hartgoog` carries `sponsor: Google`, `source: http://books.google.com/books?id=uuDN6Gn-9hgC&oe=UTF-8`, `date: 1868`; its text carries Google's standard notice (ten "google" hits) and then runs into the vendored file's own opening character for character, including `ACADEMIAE LITTEEARVM CAESAKEAE`, `VOL, III. PARS L`, `EX EECENSIONE G. HAETELIL` and `Reprinted with the premission o£ the original publishers.`; both texts end identically. Row 191's *"a Google Books scan of the 1965 Johnson Reprint Corporation reprint"* is correct and was correctly left alone.

**L3, verified against the source item rather than against the diff.** The vendored Hartel Pars I–II file now ends at `diaconos explicit z, om» Gr§(i, —`; `sthascicaecilic01hartgoog_djvu.txt` ends at the same characters and carries nothing after them; the removed line's exact-case string occurs **zero** times in that item's own text and matches its `title` metadata field exactly. The removal is correct, changes no content, and is disclosed at the file's own `Provenance note:`. (The disclosure's own second-order problem is M3 above.)

**H1's REGISTRY.yaml rewrites, and the README regeneration.** Both `notes` fields now state the closed state and carry a dated correction naming what they replaced. `cic/texts/README.md` was regenerated to a scratch copy via `python cic/engine/texts_registry.py --write-readme` and byte-compared against the committed file: **no diff** — the generated index is genuinely in sync with the YAML, and `git status --porcelain` was clean afterwards. The seed's `queue[9]` title is fixed and checks out against rows 195/196 and Manifest G4. (The generated queue index is H2 above.)

**M2 (Round 23's), all three sites.** Decision Log line 240 now reads *"the same treatment as the archive.org site-navigation chrome at the front (corrected here, independent review Round 23's own M2…)"*; `REGISTRY.yaml` line 1023 and README line 222 now read *"an Internet Archive scan of the University of California, Berkeley's own copy — corrected here from an earlier draft's own 'a Google Books scan' and 'not guessed': the item (archive.org/details/…sanctiaugustiniv00possrich, identity confirmed by a byte-for-byte match against the vendored file at both ends) carries sponsor MSN and scanningcenter rich…"*. Closed at all three.

**M3 (Round 23's), the verdict it was about.** Row 191 no longer calls "(spuria and indices)" a mischaracterization; it now names the volume's title-page components and the Vita and Acta together, and describes the earlier three-item list as *"itself incomplete, dropping the very indices and praefatio it had just called out."* Both halves are accurate against the file (title page at line 54; indices from ~19467; `PRAEFATIO.` at 36057; Vita at 40258; Acta at 41413). (Its normalized quotation is C1, and the unswept siblings are L2.)

**L1 and L2 (Round 23's).** Row 67 now reads *"was the real acquisition candidate, now acquired and vendored as row 209 (2026-09-08), closing Manifest G6"* — verified against row 78 (*"Now vendored, row 209"*), row 209 (`augustine_retractationes-lat_knoll-csel36.txt`) and Manifest G6 (*"G6 is now closed"*). Row 39 now reads *"adds a critical apparatus this corpus now holds, vendored in full as rows 191 and 194"* — verified against rows 191/194 and the same row's own Verification Note. Re-running the widened Licensed-For sweep across all 212 rows returns no further live present-tense instance: every remaining hit is either quoted earlier-draft text inside a correction note, row 193's correctly-scoped CSEL 58 residue, or the consultation-only "Not currently vendored" boilerplate on in-copyright rows 71–190, which is accurate.

**L4 and C2 (Round 23's).** Registry row 33, Doc_02 §3 and Decision Log line 138 now all distinguish three named journals from a fourth MUSE-hosted review, and all three state five sources in total. The Manifest's §2 heading note is restructured so `(Round 20's own L5)` sits directly after "the §1 heading above it," and its factual content is verified: `grep "^## "` returns headings at 15, 65, 71, 81, so 65 − 15 = 50 lines apart, and Manifest line 17 does credit the §1 heading fix to Round 20's L5.

**C4 (Round 23's), including its arithmetic.** The Manifest at `efc1a95` was 87 lines with the priority-ordering paragraph at 85; at `f0be10a` it is 89 with that paragraph at 87, and the only intervening insertion is the two-line §2 hunk. "Two lines further down" is exact, and dropping the bare line number in favour of describing the drift is the right fix. (Its "below" is C2 above.)

**Round 23's C1 declination, independently tested three ways.** A repository-wide search for `437` across `World-Builds/`, `cic/` and `world-build-docs/` returns: `Doc02_Round23_Review.md` (quoting the commit message it criticised), `Doc02_Round22_Review.md` (its own correct figure at `f0be10a`), the Decision Log's Round 22 paragraph (the same correct figure), and unrelated numeric hits in `cic/texts/STRUCTURE.md` and two corpus-map files. The string "now 440" appears only in Round 23's own quotation. **No live document states the wrong figure**, so the reasoning that a past commit message cannot be corrected without amending history holds without residue. The new commit message's replacement figure was recomputed independently rather than read: **438**.

**Bold-marker nesting, independently reproduced across all four documents, run-aware.** markdown-it-py 4.2.0 (`commonmark`), **438** `**`-bearing lines — Doc_02 66, Registry 200, Manifest 38, Decision Log 134, unchanged from `d35f00a` because this pass edited existing bold-bearing lines and added none. Result: **zero** nested `<strong>` spans, **zero** unclosed spans, **zero** literal `**` surviving any render, **zero** `****`, and **zero** lines where CommonMark's delimiter pairing differs from run-aware sequential pairing. The class remains closed by construction, now for a fourth consecutive round.

**Both edited YAML files parse.** `yaml.safe_load` on `cic/texts/REGISTRY.yaml` (88 entries, all with `filename`/`supplied_by`/`date_added`/`notes`) and on `world-build-docs/_cross-world/download-queue-seed.yaml` (22 queue entries) both succeed. (The fold-break defects at L4 are valid YAML producing wrong strings, which is why parsing does not catch them.)

**Round 19's C1 — spot-checked, undisturbed, a sixth time.** `prosper_chronica-minora-1-lat_mommsen1892.txt` line **42582** reads `EPITOMA CHEONICON`; line **45881** reads `EPITOMA DE CHRONICON,`, between the praefatio's last line at 45876 (`De reliquis libris quicquam addere supervacaneum est.`) and the chronicle's first entry at 45891 (`1 Adam cum e.sset annorum CCXXX, genuit Setli.`). Identical to Rounds 19, 20, 21, 22 and 23. The declination stands on six consistent checks.

**Registry table integrity, recomputed row by row.** All 212 rows re-extracted by column position: numbers **1–212 complete, no gap, no duplicate**; **every row exactly 12 pipes / 11 columns**. The same three physical-order inversions (48→42, 193→60, 60→52) Rounds 20–23 found, all covered by the front-matter Disclosed-placement rule. The pass inserted and deleted no Registry lines, so the file is still 329 lines and every pre-existing line pointer into it still resolves — Registry line 295 is still the recall-test paragraph, and the Manifest's line 11 and line 61 still hold superseding notes.

**Census and comparator arithmetic, recomputed across every atlas file.** `latin-pastoral-congregational-christianity.yaml`: **99 entries, 97 distinct titles, `Counter({'tradition': 90, 'context': 9})`, 88 distinct titles inside the tradition set, `Counter({'assigned': 87, 'provisional': 12})`**; exactly two duplicate titles (*The Enchiridion*, *The Passion of the Scillitan Martyrs*), so 90 − 2 = 88 reconciles. Comparators re-derived per measure: 99 raw against **68** (`post-apostolic-house-church.yaml`), 90 `tradition` against **59** (`alexandria-catechetical.yaml` and `post-apostolic-house-church.yaml`, tied). Every figure in Doc_02 §1's opening paragraph holds.

**Engine scripts, both re-run this session from `/home/user/CIC-Project`.** `python cic/engine/texts_registry.py` → **exit 0**, *"OK: every vendored file has a header-verified rights line …, an ENTRIES row, and no ENTRIES row points at a missing file"*; 88 vendored files, 23 non-English, `cic/texts/` at 211 MB (30% of the 700 MB planning trigger). `python cic/engine/corpus_map_merge.py --check` → **exit 0**, no error. Neither script validates prose in a `notes` field, so H1 is invisible to both — the same blind spot Round 23 named.

**Cross-references and directional language in Doc_02.** Every `rows? N` citation in Doc_02 resolves inside 1–212 (max cited: 212). Every `§N above` / `§N below` reference direction-checked programmatically against the section each sits in: **none fails**. The Decision Log's `Doc_02 revision:` heading occurs exactly once and Doc_02 §2's pointer quotes strings from it that are still present and unique.

**The other nineteen lpc entries in `REGISTRY.yaml`, read in full against their Registry rows and file headers.** Beyond the two at H1, they check out: the CSEL 33/40-1/40-2 and Bruns entries each record the specific copyright-trap items they excluded (`sanctiaureliaugu0033augu`, `corpusscriptorum0040unse`, `canonesapostolo01brungoog`), verifiable against their file headers; Harnack's TU citation (`3. Reihe, 9. Band, Heft 3 [= XXXIX, 3]`) matches Registry row 205 and the vendored file's own title line; Monceaux Tome I records the `histoirelittra00moncuoft` lead correction; von Soden 1909 and Delehaye match rows 211 and 212; the Codex Theodosianus entry states the Latin Library rights basis and edition gap exactly as row 88 and the 2026-09-02 Decision Log entry do. `CSEL 58 remains open` in the CSEL 34 and CSEL 44 entries is correct.

**The other lpc entries in `download-queue-seed.yaml`.** `queue[5]`/`queue[13]` are correctly `superseded` rather than deleted; `queue[6]`, `queue[7]`, `queue[8]`, `queue[10]`, `queue[11]`, `queue[12]`, `queue[14]`–`queue[21]` are all `downloaded` and each names an identifier that matches its Registry row. `queue[9]` is the only lpc row still `not-yet-downloaded`, correctly, for CSEL 58.

**The disposition status lines, reported as observed and not assessed.** `Doc_02_Source_Ecology.md`'s status line and §10, and `Source_Registry.md`'s status line, still read "Fourteen independent adversarial review rounds" over "(Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0)" and still point to "`Doc02_Round1_Review.md` through `Doc02_Round14_Review.md`," while `Review-Artifacts/` now holds twenty-three `Doc02_Round*_Review.md` files before this one and both documents carry in-text attributions to Rounds 15 through 23. Reported here as observed, checkable state, on the same footing Rounds 16 through 23 reported it; not assessed, per CO-022's rule that the build thread applies its own disposition.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the fix pass and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** H1 and H2 both land on shared artifacts other worlds' build threads read — `cic/texts/README.md` and `world-build-docs/_cross-world/DOWNLOAD-QUEUE.md`. But in each case the finding is that lpc's own entries, describing lpc's own files and lpc's own acquisition state, misstate them; nothing here decides anything for another world, no other world's entries were examined or altered, and the corrections are lpc's to make on its own record. M1–M4 and every LOW and COSMETIC concern this world's own documents and intakes. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing here proposes a change to `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022 or any governing document. H1 is a finding that two registry entries do not match what the corpus's own records already say; H2 is a finding that a generation step the branch's own history performs every time was skipped once; M2 is a finding that a logging convention the entry's own heading states was not followed; M3 and L2 are findings that a header contradicts its neighbouring field. All are conformance findings against rules already in force. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round disagrees with no prior round on a point of fact. It agrees with Rounds 20–23 against Round 19 on C1, reached by reopening the file at the lines named, and it agrees with Round 23's C1 declination after independently testing the premise it rests on. It departs from Round 23 on no calibration question; where it rates something lower than Round 23's precedent might suggest (M2, M4), it states the mitigation in the finding. The three places this round could have produced an unresolved tension are H1(a), M3 and L3, and two of the three are closed rather than left open: H1(a) by reading the vendored file's own letter headings directly, and M3 by fetching the archive.org item and matching it against the vendored file at both ends. The third, L3, is stated as unsupported rather than false, with the reason it cannot be settled from here given in the finding. Neither requires the project lead. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

Whether and how the status lines described above should change, and what disposition follows from this round's counts, is **not assessed here**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition.

**Observed trend, stated as raw counts only and not otherwise characterized.** Across the ten rounds against this 2026-09-08 revision: Round 15 — 4/6/5/2 (17); Round 16 — 4/5/6/3 (18); Round 17 — 0/3/5/4 (12); Round 18 — 0/4/3/3 (10); Round 19 — 0/2/4/3 (9); Round 20 — 1/4/5/5 (15); Round 21 — 0/4/5/4 (13); Round 22 — 1/2/3/4 (10); Round 23 — 1/3/4/4 (12); Round 24 — 2/4/4/5 (15).

Four observations bear on reading this round's counts, stated without weighing them.

First: **nine of the eleven findings the pass addressed are closed at the sites Round 23 named, and the two hardest corrections in the run so far survive re-derivation from the live source items rather than only from the commit** — the Goldbacher not-a-Google-scan finding, the `CSEL57` identity, the decision to leave Hartel's claim standing, and the tail-chrome removal were each re-checked against archive.org this round and each held exactly.

Second: **both HIGH findings and one MEDIUM are the same shape as Round 23's own H1 — a correction that reached the sites a review quoted and not the file those sites live in.** Round 23 diagnosed that no sweep had ever been scoped to `cic/texts/REGISTRY.yaml`; the pass corrected the three entries Round 23 quoted inside it. The two remaining false claims there are not new drift: one has been contradicted by the vendored file since Round 16, the other since Round 17, and both are reproduced in the generated index.

Third: **the derived-artifact half of a fix is now its own failure site.** `cic/texts/README.md` was regenerated and is in sync; `world-build-docs/_cross-world/DOWNLOAD-QUEUE.md` was not, and is the first such omission in this branch's history of touching that seed. The two are the same operation on two files.

Fourth: **the one finding that is neither of those is an omission rather than an error** — the Decision Log's review-rounds entry was not extended for the first time since the convention was established at Round 16, leaving that entry's own heading, escalation check and pattern paragraph each describing a state one round behind, and leaving Round 23's deliberate non-fix disclosed only in the review artifact.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 2 HIGH · 4 MEDIUM · 4 LOW · 5 COSMETIC.**
