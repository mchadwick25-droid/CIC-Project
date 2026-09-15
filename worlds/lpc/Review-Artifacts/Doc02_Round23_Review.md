# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 23 Independent Adversarial Review — scoped to verifying the Round 22 fix pass (all ten findings), a fifth spot-check of Round 19's declined C1, an independent re-run of the run-aware bold-nesting test, and a cold sweep deliberately extended past the four documents to the artifacts they say they registered the same work in

**Documents reviewed (committed state — `git status --porcelain` clean, 0 lines, at `d35f00a`, "lpc: fix Round 22 review findings on Doc_02 revision (10 of 10)", 2026-09-08 09:46:26 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `worlds/lpc/Doc_02_Source_Ecology.md` (156 lines by `wc -l`, as are all counts in this list; §1 through §10 read in full, cold)
- `Source_Registry.md` (329 lines; all 212 rows re-parsed by column position — **every column**, with the Licensed-For column swept a second time under a wider pattern list than Round 22's own)
- `Source_Acquisition_Manifest.md` (89 lines, read in full)
- `lpc_Decision_Log.md` (340 lines, read in full — every entry, with the 2026-09-05 G1/G3/G4 intake entries read against the vendored files *and against the corpus registry those entries say they registered each file in*)
- `Doc_01_World_Identification_Boundaries_Orientation.md` (302 lines), consulted for the phrases Doc_02 attributes to it
- `Review-Artifacts/Doc02_Round21_Review.md` and `Doc02_Round22_Review.md`, plus `git show 6fd4973` (the Round 17 fix-pass commit) for the L2 attribution question
- All 19 vendored `cic/texts/*.txt` files carrying the OCR clause (programmatic extraction and byte-comparison of the clause across all 19), plus `possidius_vita-augustini_weiskotten1919.txt`, `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`, `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt`, `augustine_epistulae-critical_goldbacher-csel57-pars4.txt` and `prosper_chronica-minora-1-lat_mommsen1892.txt` opened directly
- **`cic/texts/REGISTRY.yaml`, `cic/texts/README.md`, and `worlds/_cross-world/download-queue-seed.yaml`** — read this round because the Decision Log's own 2026-09-05 intake entries name each of them as a step of the same intake whose provenance and acquisition-state claims Round 22's H1/M1/M2 corrected, and no round in this sequence has read them
- All 57 `works`-bearing atlas files in `cic/corpus-map/`; both engine scripts
- **Five live archive.org fetches** — item metadata and/or full `_djvu.txt` for `sanctiaugustiniv00possrich`, `CSEL57`, `sthascicaecilic01hartgoog`, `patrologiae_cursus_completus_lat_vol_036`, and metadata for `canonesapostolo00brungoog`, `diecyprianische00unkngoog`, `corpusscriptorum03cypruoft`, `sanctiaureliaugu34augu` — run because this pass asserts a scan-provenance correction and an item identity, and because the same class of claim sits unchecked on two sibling intakes

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-05 or 2026-09-08 vendoring, did not write the Round 15–22 fix passes, and did not write Rounds 1–22.

**Scope, stated plainly.** Five briefs, run together. First: verify, independently and against primary artifacts, whether each of Round 22's ten findings is closed by the `d35f00a` pass — and, since every one of the eight preceding fix passes introduced or left at least one checkable error while fixing what it targeted, look specifically for the three shapes this revision's history names (a fix that creates a new defect in the same sentence; a fix whose scope stops short of a sibling site; a claim written into a live document without re-derivation). Second: **verify the M1/M2 six-site provenance rewrite at source rather than trusting it** — re-fetch the archive.org item, re-derive the byte-for-byte match and the zero-"Google" count, and then ask the question Round 22 explicitly left open: whether the *sibling* intakes' identical "Google Books scan" descriptions hold. Third: spot-check Round 19's declined C1 a fifth time. Fourth: independently reproduce the run-aware sequential-pairing-versus-CommonMark bold-nesting test across all four documents. Fifth: a cold cross-document sweep, weighted per the commissioning brief toward the two blind-spot shapes Round 22's own findings exposed — a Registry column whose phrasing no sweep pattern had matched, and a provenance claim in an artifact no round had opened. Rounds 15–22 and the `d35f00a` commit message were treated as claims to re-derive, not as authority.

**Method — what was actually re-derived, not trusted.** A CommonMark render (markdown-it-py 4.2.0, `commonmark` preset) of every `**`-bearing line in all four documents (438 lines), with the rendered `<strong>` tree walked for nesting depth, unclosed spans, literal `**` survival and `****`, compared element by element against a **run-aware** sequential pairing of that line's own bold delimiters. A fresh regex parser over all 212 Registry rows extracting all eleven columns by position, with row-number sequence, physical order, pipe count and per-row `**`/backtick/parenthesis balance; then two independent sweeps of the Licensed-For column — one replicating Round 22's own pattern list, one widened to include `acquisition candidate`, `if acquired`, `currently lacks`, `open request`, `to be acquired`. A programmatic extraction of the OCR clause and its attribution from every vendored file, with the clause body byte-compared across all 19 after normalizing the attribution. `git show 6fd4973` re-run and each of its eight `cic/texts/` additions read, to test whether the L2 fix's "five files" is the right five. `yaml.safe_load` across all 57 atlas files, recomputing every census figure and comparator Doc_02 §1 states, and across `cic/texts/REGISTRY.yaml` and `worlds/_cross-world/download-queue-seed.yaml`. Direct reads of the Prosper file at 42580–42584 and 45876–45892, and of the Hartel Pars III file at line 54 and at its index sections. Live archive.org fetches, byte-compared against the vendored files at both ends. Both engine scripts re-run. Nothing was carried forward from Rounds 15–22, from `lpc_Decision_Log.md`, or from the commit message.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 1 HIGH · 3 MEDIUM · 4 LOW · 4 COSMETIC.**

**All ten of Round 22's findings are genuinely closed at the sites Round 22 named, and four of them are closed exactly.** H1's two Licensed-For clauses now state the current state and carry a dated correction note; a widened re-sweep of that column finds no surviving present-tense "stays open"/"remains unacquired" claim anywhere in the table except row 193's correctly-scoped CSEL 58 residue and the historical quotations inside the correction notes themselves. M1's identifier is now disclosed at all six sites Round 22 enumerated, and — checked at source rather than trusted — **the identity claim is true**: `sanctiaugustiniv00possrich`'s own full text (386,678 characters, exactly the figure Round 22 reported) matches the vendored file character for character at both ends. M2's "Google Books scan" correction is right on the facts: that item carries `sponsor: MSN`, `scanningcenter: rich`, `contributor: University of California Libraries`, `call_number: nrlf_ucb:GLAD-50452006`, and its full text returns **zero** case-insensitive occurrences of "Google." L1's two adjacency claims now resolve: the Manifest's headings are at lines 15 and 65, fifty apart as stated, and the Registry's line-295 pointer lands on the recall-test paragraph. L2 is mechanically exact — 5 files at "Round 17; extended, Round 18; extended, Round 19; extended, Round 20" and 14 at "Round 18; …", 19 in total, clause body byte-identical across all 19 — and `git show 6fd4973` confirms the right five: of the eight files that commit touched, three carry unrelated Round 17 notes (two Getty-barcode disclosures, one Perpetua-assignment fix), not the OCR clause. C1, C2, C3 and C4 all check out against the artifacts they describe, including C3's trigger-rule reasoning (rows 34 and 35 state conditional positive licences; row 38 states a negative, and the rule at Registry line 283 excludes exactly that).

**The bold-nesting class is still closed by construction, independently reproduced.** Across all **438** `**`-bearing lines in the four documents — one more than Round 22's 437, the line this pass added to the Decision Log — CommonMark's own delimiter pairing is identical to run-aware sequential pairing on **every single line**: zero mismatches, zero nested `<strong>` spans, zero unclosed spans, zero literal `**` surviving any render, zero `****`.

**Round 19's C1 is undisturbed** — `EPITOMA CHEONICON` at line 42582, `EPITOMA DE CHRONICON,` at line 45881. Fifth consecutive confirmation.

**Where the recurrence went this time: past the edge of the enumerated site list, into the artifacts the Decision Log's own intake procedure names.** Round 22 found its HIGH and one MEDIUM in places no round's sweep pattern had reached. This pass fixed exactly the sites Round 22 enumerated and did not ask what else says the same thing. `cic/texts/REGISTRY.yaml` — the corpus's own machine-readable registry of record, which `texts_registry.py` validates against and from which `cic/texts/README.md` is generated — carries, verbatim and uncorrected, **both** of Round 22's H1 clauses ("Pars III (spuria and indices) is not included and remains unacquired; G1 stays open for that part only"; "The remaining Goldbacher volumes (CSEL 34/1, 34/2, 44, 58) are not included and stay open") **and** the M1/M2 text ("a Google Books scan of the University of California, Berkeley's own copy (exact item identifier not stated when supplied, not guessed)"). A third instance of the corrected-away "archive.org/Google Books chrome" phrase survives inside the Decision Log's own G3 entry, four paragraphs above the bullet the pass corrected. And the question Round 22 explicitly declined to answer — whether the Hartel and Goldbacher intakes' own "Google Books scan" descriptions are correct — has two different answers, both derived here from live fetches: **Hartel's is right** (`sthascicaecilic01hartgoog`, `sponsor: Google`, `source: books.google.com`, carrying the 1965 Johnson Reprint title page the vendored file opens with, character for character), **Goldbacher's is wrong** (`CSEL57`, matched byte-for-byte at both ends against the vendored file, full text containing "Google" **zero** times) — the identical M2 defect at the sibling intake, one row over.

---

## HIGH

### H1. `cic/texts/REGISTRY.yaml` and the generated `cic/texts/README.md` carry, word for word and uncorrected, both of the present-tense "still open" acquisition claims Round 22 rated HIGH — in the corpus registry every other world's build thread reads

`cic/texts/REGISTRY.yaml`, `notes` field for `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`:

> …fulfilling most of that world's Source_Acquisition_Manifest G1 request. **Pars III (spuria and indices) is not included and remains unacquired; G1 stays open for that part only.**

Same file, `notes` for `augustine_epistulae-critical_goldbacher-csel57-pars4.txt`:

> …partially fulfilling Source_Acquisition_Manifest G4. **The remaining Goldbacher volumes (CSEL 34/1, 34/2, 44, 58) are not included and stay open.**

Both sentences are reproduced verbatim in `cic/texts/README.md` (lines 167 and 160), which `texts_registry.py --write-readme` generates from that YAML and which is the corpus's own human-readable index.

These are not paraphrases of Round 22's H1 — they are the same claim in nearly the same words, at two further sites. The Manifest says *"**G1 is now closed in full** — Pars I, II, and III of Hartel's CSEL 3 are all vendored"* and *"**G4 now stays open for CSEL 58 only**"*; Registry rows 194, 195 and 196 record the three closing acquisitions; the very Registry rows this pass edited (191 and 193) now say so in terms. Neither REGISTRY.yaml entry corrects itself anywhere — the mitigation Round 21 relied on to keep row 45 at MEDIUM, and whose absence Round 22 gave as its reason for rating rows 191/193 HIGH.

**Why this is HIGH rather than MEDIUM, on the calibration this sequence has already set.** Round 15 rated seven "still unvendored" rows HIGH. Round 22 rated two further sites of the same class HIGH, in the Registry, with the reasoning: *"in a disposed document, and **without** the self-correction that took row 45 down to MEDIUM."* Both conditions hold here, and one aggravating fact does not hold there: `cic/texts/README.md` is not an lpc document. It is the shared corpus's index, read by every world's build thread — the same audience `worlds/_cross-world/download-queue-seed.yaml` exists to serve, and the same audience the Decision Log's 2026-09-05 entry had in mind when it wrote that the queue was updated *"so another world's build thread checking this file sees the acquisition rather than a stale open request."* That reasoning applies with full force to the registry entry and the README, and it was not applied to them.

**A third, weaker site of the same class, recorded here rather than as its own finding.** `worlds/_cross-world/download-queue-seed.yaml`'s entry `queue[9]` is still titled *"S. Aureli Augustini Hipponiensis episcopi Epistulae, **remaining volumes (CSEL 34/1, 34/2, 44, 58)**"* at `status: not-yet-downloaded`, three of whose four volumes were downloaded on 2026-09-08 (`queue[10]`, `queue[11]`). The Decision Log's own 2026-09-05 G4 entry records narrowing that entry once, for exactly this reason, and the 2026-09-08 entry records marking the wrong G5 lead `superseded` rather than deleting it — so the file's own convention for this situation exists and was applied elsewhere in the same pass. This one is weaker than the two above because two sibling entries in the same file do record the acquisitions, so a reader of the queue is not left with only the false statement.

**Why twenty-two rounds missed all three, stated precisely.** Every sweep in this sequence — Round 15's H4, Round 18's and Round 19's L2 past-tensing passes, Round 21's M4 two-claim cell sweep, Round 22's own Licensed-For sweep — has been scoped to `Source_Registry.md`'s table, and latterly to the vendored files' own headers. None has been scoped to `cic/texts/REGISTRY.yaml`, even though the Decision Log's own 2026-09-05 intake entries list *"Registered in `cic/texts/REGISTRY.yaml`"* as a step of each intake and record `--write-readme` being re-run, and even though Round 22's own scope list included "both engine scripts" — the scripts, but not the data file they read.

---

## MEDIUM

### M1. The Goldbacher CSEL 57 intake carries the identical M2 defect at four sites — its source item is `archive.org/details/CSEL57`, matched byte-for-byte at both ends, and that item's full text contains the word "Google" zero times

Round 22 was explicit that it had not checked this: *"this round makes no claim about the Hartel (row 191) or Goldbacher (row 193) intakes, whose own source items were not checked here and whose 'Google Books scan' descriptions may well be correct."* The fix pass had working network access and the method fresh in hand from the Possidius derivation one row away. It did not extend it. This round did, and the answer for Goldbacher is that the description does not hold.

**The identity, derived, not asserted.** The vendored file's body opens (literal, in its own OCR form):

> `M RIPTORVM ECCLESIASTICORVM / LATINORVM / EDITVM CONSILIO ET IHPENSIS / ACADEMIAE LITTERARVM CAESAREAE / VINDOBONENSIS / VOL lvh. / S. AYRELI AVGVSTINI OPERVM SECTIO H. / S. AVGVSTINI EPISTVLAE / ti ucmion / AL GOLDBACHER. / VTNDOBONAE / F. TEMP8KT / LIPSLAE / 0. FRETTAG (o.m.b.h.) / kdccccxi`

`CSEL57_djvu.txt` (1,574,207 characters, fetched this round) opens with that string character for character, garble for garble — `M RIPTORVM`, `IHPENSIS`, `VOL lvh.`, `SECTIO H.`, `ti ucmion`, `TEMP8KT`, `LIPSLAE`, `0. FRETTAG`, `kdccccxi`. Both texts also **end** identically, at `3 in] me M in otn edd. praeter m et Vall. 5 pro me] ppf (= prop- / ter M`. This is the same both-ends test Round 22 applied to Possidius, and it settles the identity to the same standard.

**The claim that fails.** A case-insensitive count over that item's full text returns **zero** occurrences of "Google." Its archive.org metadata carries no `sponsor`, no `scanningcenter`, no `source` field pointing at `books.google.com` — unlike `canonesapostolo00brungoog` and `diecyprianische00unkngoog`, both of which carry `sponsor: Google` and a `books.google.com` source URL, and unlike `patrologiae_cursus_completus_lat_vol_036`, whose own text opens with Google's standard digitization notice. So all four of the following are wrong in the same way Round 22's M2 found for Possidius:

- `cic/texts/augustine_epistulae-critical_goldbacher-csel57-pars4.txt`, `Source:` — *"built from an archive.org-hosted 'Full text' / 'See other formats' view of **a Google Books scan**"*
- the same file's `Provenance note:` — *"**archive.org/Google Books site-navigation chrome and Google's own standard public-domain usage notice** were stripped from the head of the file"* (an extraction step described on material the source item does not contain — the same second-order claim Round 22 flagged for Possidius)
- Registry **row 193**, Verification Note — *"an archive.org 'Full text' view of **a Google Books scan**"*
- `cic/texts/REGISTRY.yaml` / `cic/texts/README.md` line 160 — the same sentence again, plus *"Google's PD usage notice stripped"*

The Decision Log's own 2026-09-05 G4 entry carries it a fifth time, in its action list: *"Extracted mechanically (**archive.org/Google Books chrome** cut…)"*.

**The identifier hedge is now closable too, and this is the useful half.** Row 193, the file header, REGISTRY.yaml/README and `download-queue-seed.yaml` `queue[12]` all hedge the identifier as *"very likely… `archive.org/details/CSEL57`… not independently confirmed against this specific file."* It is now confirmed, by the byte-for-byte match above. Nothing needs to be guessed.

Rated MEDIUM, on the same footing Round 22 rated the identical defect at the Possidius file: a pre-existing factual error in the provenance header `cic/texts/INTAKE.md` §4 makes the artifact of record, in a disposed document set, that no live substantive claim and no rights basis rests on (the public-domain basis everywhere stated is the 1911 imprint, unaffected). It is not rated higher only because the underlying acquisition, edition, range and rights are all correct and independently re-verified here.

### M2. The M1/M2 fix's own scope stopped at the sites Round 22 enumerated — a third "Google Books chrome" instance survives inside the same Decision Log entry, and both the corrected-away description and the corrected-away identifier hedge survive in the corpus registry

Round 22 listed four sites for M2 and six for M1. The pass corrected precisely those and swept for no others. Three further live instances remain:

**(a) `lpc_Decision_Log.md` line 240, inside the very entry the pass edited twice.** The G3 entry's "second scanning artifact" paragraph still reads:

> Stripped as a scanning artifact, disclosed in the file's own header, the same treatment as the **archive.org/Google Books chrome at the front**.

That is the same phrase, about the same file's front chrome, four paragraphs above the action-list bullet the pass rewrote to read *"archive.org site-navigation chrome and the library due-date slip cut — **not "Google Books chrome," per the M2 correction above**"*. The entry now corrects itself in one paragraph and repeats the error in another. Round 22 quoted the action-list instance and not this one; the fix followed the quotation rather than the entry.

**(b) and (c) `cic/texts/REGISTRY.yaml` line 1016 and `cic/texts/README.md` line 222**, the Possidius entry:

> Mechanically extracted from a docx Mark compiled from an archive.org "Full text" view of **a Google Books scan** of the University of California, Berkeley's own copy (**exact item identifier not stated when supplied, not guessed**); site-navigation chrome, **Google's PD usage notice**, and a scanned UC Berkeley circulation due-date slip … were all stripped as scanning artifacts…

This carries both corrections' opposites at once: the scan attribution M2 corrected, and the identifier hedge M1 replaced. So the count Round 22 stated — *"an identity five other sites in this document set explicitly say is unknown"* — was right for the four documents plus the vendored file, and is now short by two for the corpus as a whole; and the Decision Log's own new Round 22 paragraph, which says M2 was *"fixed at all four sites"*, is true of the four named and reads as completeness.

Rated MEDIUM as an internal contradiction across three sites, one of them inside the entry the fix itself edited — the same footing Round 22 used for its own M1, and the scope-propagation shape this run's own pattern paragraph names in terms.

### M3. Row 191's new correction text calls the phrase it replaced "a mischaracterization of Pars III's own actual contents" — the printed volume's own title page, and the vendored file's own `Title:` line, both say otherwise, and the replacement enumeration is the one that drops something

The H1 fix rewrote row 191's Licensed-For to read:

> **Covers Pars I and II only — Pars III (the *Opera Spuria*, the *Vita Caecilii Cypriani*, and the *Acta Proconsularia*) is now also vendored, as row 194 (2026-09-08), closing Manifest G1 in full (corrected here … from an earlier draft's own present-tense "Pars III… remains unacquired…", stale since that acquisition, and from **"(spuria and indices)," a mischaracterization of Pars III's own actual contents** — no index is what closes row 41 or Manifest §2, the Acta Proconsularia is).**

The acquisition-state half is right and is H1's actual fix. The second half is a new claim, and it is wrong.

`cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` line 54 is the printed volume's own title-page subtitle, quoted here in the file's own literal OCR form rather than normalized, per this document set's own standing disclosure practice:

> `(OPEEA SPVRIA. INDICES. PKAEFATIO)`

— i.e. *Opera spuria. Indices. Praefatio*, which is how Hartel's Pars III titles itself. The same file's own `Title:` line, written by this build thread, says the same thing:

> `S. Thasci Caecili Cypriani Opera Spuria, cum Indicibus et Praefatione (CSEL 3, Pars III); includes the Vita Caecilii Cypriani … and the Acta Proconsularia`

And the indices are physically in the file: a scriptural index running from roughly line 19467, and `Index nominum et rerum.` at line 27256, running to the file's own end at 42600.

So "(spuria and indices)" was **incomplete** — it omitted the Vita and the Acta — but it was not a mischaracterization: it named two of the three components the volume's own title page names. The replacement enumeration, meanwhile, drops the Indices and the Praefatio, which are two of those same three. The correction note therefore (i) mislabels an accurate-as-far-as-it-went description as an inaccurate one, and (ii) substitutes an enumeration that is incomplete in the other direction, in a sentence whose whole subject is what Pars III actually contains.

The three-item enumeration itself is not this pass's invention — row 39, row 194's Source column, and the Hartel Pars I–II file's own Content note all use it, and Round 22's H1 recommended it in terms (*"Row 194's own Source column names its actual contents"*). That is the point: the pass adopted a review's characterization of a third artifact without opening that artifact, which is the failure mode this build's Decision Log has tracked under its own name since its 2026-09-01 `donatism.yaml` entry. The finding is the "mischaracterization" verdict, not the enumeration.

Rated MEDIUM: a new, checkable, false claim written into a disposed document by the fix pass, in the same sentence as the fix, about the primary artifact the sentence is describing. Same footing as Round 21's M3 and Round 22's M1.

---

## LOW

### L1. Registry row 67's Licensed-For still calls Knöll's CSEL 36 "the real acquisition candidate," present tense, five days after it was acquired — a seventh site of a defect six rows were past-tensed for, in the column Round 22 swept

Row 67 (Mutzenbecher, CCSL 57), Licensed-For column, in full:

> The current scholarly critical edition of the work row 13's *Retractationes* II.18 citation holds only at second hand — **but not a vendoring candidate (in copyright); Knöll's CSEL 36 (row 78, added Round 5) is the public-domain edition of the same text and the real acquisition candidate — corrected here, Round 5's own M6, from an earlier draft that named only this in-copyright edition**

Row 78's own Verification Note opens **"Now vendored, row 209 (2026-09-08…)"** and closes *"**Was** a real acquisition candidate; **now acquired**"* — past-tensed by the Round 18 fix pass for exactly this reason. Row 209 records the vendored file, and Manifest G6 reads **"G6 is now closed."** Row 67 does not correct itself: its own Verification Note speaks only about row 67's own edition.

This is the same "acquisition candidate" staleness Round 18's and Round 19's L2 fixes past-tensed at rows 41, 78, 89, 90, 99 and 56 — all six in the **Verification Note**. This seventh instance sits in the **Licensed-For** column, and it survived Round 22's own Licensed-For sweep because that sweep's stated pattern list (`stays open`, `remains open`, `remain(s) unacquired`, `still unacquired`, `awaiting`, `not yet located`) does not match the words "acquisition candidate." Re-running the same sweep with that phrase added returns this row and no other live instance.

Rated LOW rather than HIGH, in a deliberate departure from Round 22's calibration and with the reason stated: what row 67 gets wrong is a characterization of *another row's* status, and the pointer it gives (row 78) resolves in one hop to text that corrects it in bold in its own first four words — where rows 191 and 193 asserted, in their own voice, that a Manifest request was open, and gave no pointer that led anywhere saying otherwise without an independent check.

### L2. Registry row 39's Licensed-For still says Hartel "would add a critical apparatus this corpus currently lacks" — the corpus has held it since 2026-09-05 and 2026-09-08

Row 39, Licensed-For:

> …an independent, 1868–71 critical edition that **would add a critical apparatus this corpus currently lacks**…

Rows 191 and 194 vendor exactly that apparatus, and row 39's own Verification Note opens by saying so — *"**Pars I and II now vendored as row 191 (2026-09-05); Pars III … now also vendored, as row 194 (2026-09-08)** … The full CSEL 3 edition (Pars I–III) is therefore now vendored in this corpus."* The H1 fix edited row 191's own pointer *to* row 39 and did not look at row 39's own Licensed-For, which is the sibling site of the same defect one column and thirteen table rows away.

Rated LOW, not higher, precisely because of that adjacent self-correction — the mitigation Round 21 named when it kept row 45 at MEDIUM, present here in the strongest form it has taken in this sequence (the correcting sentence is the first thing in the neighbouring cell).

### L3. The vendored Hartel Pars I–II file ends with a line that is not in its source item — the archive.org page's own title, surviving the chrome cut, undisclosed, while the file's own notes disclose chrome-stripping at the head only

`cic/texts/cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt` ends:

```
diaconos explicit z, om» Gr§(i, —
S. Thasci Caecili Cypriani Opera omnia
```

`sthascicaecilic01hartgoog_djvu.txt` — the source item, identified and byte-matched at both ends this round (see "What was checked and found clean" below) — ends at `…om» Gr§(i, —` and carries nothing after it. `S. Thasci Caecili Cypriani Opera omnia` is that archive.org item's own `title` metadata string, in mixed case; the exact-case string occurs **zero** times anywhere in the item's own text. It is site chrome that survived the extraction at the tail.

The file's own `Provenance note:` discloses stripping *"archive.org/Google Books site-navigation chrome and Google's own standard public-domain usage notice (both present **at the head** of what was supplied)"*, and its `Content note:` says the document *"ends cleanly at the close of Epistle 81, no truncation found."* Neither is false on its own terms — the claim is about the head, and about truncation — but between them they leave a reader with no notice that a non-text line closes the file. The identical defect was caught and fixed in the Possidius intake on the same day, at the other end of the file: the Decision Log's own G3 entry records *"A first extraction pass also let one stray line (the archive.org page's own title line…) slip past the front cut; caught and fixed before the file was finalized."* The check that produced that fix was run on one file's head and not on its sibling's tail.

Rated LOW rather than COSMETIC — Round 17's own C3 rated a comparable survival (a Getty Center Library back-cover barcode in two files) COSMETIC, and the two Goldbacher files still disclose that barcode in their own headers — because this is site chrome rather than a scan artifact of the physical book, and because the corpus's own convention, applied to the same class of line in the same batch, is to cut it.

### L4. "four independent scholarly-**journal** reviews" survives at Doc_02 §3 and Decision Log line 138 after the L3 fix removed exactly that characterization from Registry row 33

Registry row 33 now reads:

> confirmed consistently across **four independent scholarly reviews** (three in *Journal of Ecclesiastical History*, *Journal of Theological Studies*, and *Reviews in Religion & Theology*; **the fourth hosted on Project MUSE, itself a hosting platform rather than a journal** — corrected here … from an earlier draft's own "four independent scholarly-**journal** reviews," which affirmatively enumerated Project MUSE as one)

Doc_02 §3's Burns & Jensen bullet still reads *"WebSearch-verified in a 2026-09-02 post-disposition pass … across **four independent scholarly-journal reviews** and the publisher's own catalogue page — five sources in total."* `lpc_Decision_Log.md` line 138 still reads *"confirmed across five sources (**four scholarly-journal reviews** plus the publisher's own catalogue page)."*

The Registry now declines to call the fourth instrument a journal review; two sibling sites still do. The fix therefore left the three sites, which Round 21's own L5 had just reconciled to a single figure, disagreeing about what the fourth instrument is. Rated LOW, at the same level Round 22 rated the finding this one is the unpropagated remainder of.

---

## COSMETIC

### C1. The fix pass's own commit message reports the bold-nesting test over "437 (now 440)" lines; the count is 438

`git log -1 d35f00a`: *"The sequential-pairing-versus-CommonMark bold-nesting test was independently reproduced across all 437 (now **440**) bold-bearing lines in the four documents: zero mismatches."* Counting `**`-bearing lines across the four documents at each commit: **434** at `efc1a95` (Round 21's figure), **437** at `f0be10a` (Round 22's), **438** at `d35f00a` — Doc_02 66, Registry 200, Manifest 38, Decision Log 134. This pass's own edits added **one** such line, not three; the three Round 22 counted (two at the Manifest, one at the Decision Log) were the *Round 21* fix pass's, which is what Round 22 said.

Nothing in the four documents states the figure, and the test result the number describes is correct and independently reproduced here. It is recorded because the commit message is this pass's own account of what it verified, and because a self-reported count stated wrong is the single most frequently recurring finding in this revision's own history — Round 17, Round 18, Round 19 (L4), Round 20 (L2, C5), Round 21 (L5) and Round 22 (C2) each found at least one.

### C2. The Manifest's L1 fix leaves "— (Round 20's own L5):" dangling sixty words from the clause it attributes

`Source_Acquisition_Manifest.md` line 67 now reads:

> **Heading corrected here (independent review, Round 21's own L2), on the same reasoning as the §1 heading above it — corrected here, independent review Round 22's own L1, from an earlier draft's own "four lines above it," … (§1's heading is at line 15, §2's at line 65, fifty lines apart) — (Round 20's own L5): this section's own former "Not yet a confirmed acquisition candidate" heading…**

The attribution `(Round 20's own L5)` belongs to "the §1 heading," and did sit next to it before the interpolation. It now follows a dash, a sixty-word parenthetical correction and a second dash, and reads as attributing Round 20's L5 to nothing in particular before a colon. Purely presentational — the attribution is correct (Manifest line 17 credits the §1 heading fix to Round 20's own L5) and no claim is wrong.

### C3. Doc_02 §3's Brown bullet keeps an undated "WebSearch-verified this session" while two of the four bullets in the same block now date their checks explicitly

The C4 fix is right where it landed: the Lancel bullet now reads *"WebSearch-verified **in this document's own original 2026-09-01 drafting session** and … reconfirmed **in a separate 2026-09-02 post-disposition pass**."* Row 31's Discovery channel does record `WebSearch this session / 2026-09-01`, so the new dating is accurate.

But the block's first bullet, Brown, still reads *"bibliographic details **WebSearch-verified this session**."* Round 22's C4 named the residue exactly: *"one bullet in a four-bullet block now dates its check explicitly and its neighbour does not, in a section where 'this session' has needed disambiguation twice in two rounds."* The fix moved the boundary rather than closing it — two bullets now date, two do not. Brown's "this session" is, like Lancel's was, literally true of 2026-09-01 (the Decision Log's 2026-09-02 entry records rows 31, 32 and 33 as that day's resolved work, and row 36 as checked and needing none; row 30 is named among the five searched but is not recorded as updated), which is why this stays COSMETIC.

### C4. The Decision Log's Round 21 paragraph points at "the Manifest's own priority-ordering advice at line 85"; that paragraph is now at line 87

`lpc_Decision_Log.md` line 334: *"…and the Manifest's own priority-ordering advice **at line 85** carrying no superseding marker of its own."* At `efc1a95` the advice was indeed at Manifest line 85 — verified by `git show`. The Round 21 fix that closed C4 inserted two lines at §2 (line 67), above it, so the paragraph is now at line 87, and Manifest line 85 today holds the *"(Awaiting Mark's decision…)"* paragraph instead. Round 22 checked the new marker at line 87 and did not check the log's own back-reference to where it used to be.

The sentence is a past-tense description of what Round 21 found, so it is defensible as written; it is recorded because a hard line number in prose that has already drifted once is the same fragility Round 18 rated MEDIUM at Doc_02 §3, and because this pass introduced two more hard line numbers (Registry line 325's "line 295", the Manifest's "line 15"/"line 65") into documents that will keep being edited. Both of those are correct today and were verified; the practice is what is noted.

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**The M1 identity claim, re-derived from the live item rather than from the pass.** `https://archive.org/metadata/sanctiaugustiniv00possrich` returns `sponsor: MSN`, `scanningcenter: rich`, `contributor: University of California Libraries`, `call_number: nrlf_ucb:GLAD-50452006`, `collection: [cdl, americana, theses-and-dissertations]`, `creator: [Possidius, Saint; Weiskotten, Herbert Theberath, 1894-]`, `date: 1919`, `publisher: Princeton : Princeton University Press`, `possible-copyright-status: NOT_IN_COPYRIGHT`. Its `_djvu.txt` is **386,678 characters** — the exact figure Round 22 reported — and opens `SANCTI  AUGDSTINI  VITA / iCRIPTA  A  POSSIDIO  EPISCOPO / IC-NRLF / B    IDfl    7E3 / … / FRKSENTEO  TO  THE / PRINCF.TON  UNIVERSITY`, which is the vendored file's own first body lines character for character. It ends `…Zosimus  160 / r / RETURN  TO:  CIRCULATION  DEPARTMENT / 198  Main  Stacks … UNIVERSITY  OF  CALIFORNIA,  BERKELEY`; the vendored file ends at `Zosimus 160 / r`, immediately before the slip. A case-insensitive count of "google" over the item's full text returns **0**. The vendored file itself returns 2, both inside the pass's own new correction sentences in the header, none in the body. Every element of the M1 and M2 corrections holds at source.

**The two sibling "Google Books scan" claims Round 22 left open, and the two other named-identifier ones, all checked.** `sthascicaecilic01hartgoog` — `sponsor: Google`, `source: http://books.google.com/books?id=uuDN6Gn-9hgC` — carries both Pars I and Pars II title pages (`VOL, III. PARS L`, `VOL. III. PARS IL`) and the 1965 Johnson Reprint imprint page, and matches the vendored Hartel Pars I–II file character for character at its opening (`ACADEMIAE LITTEEARVM CAESAKEAE`, `EX EECENSIONE G. HAETELIL`, `APYD`, `Reprinted with the premission o£ the original publishers.`, `JoHNSON Reprint Corporation`, `Berkeley Square Housc`) and at its ending. **Row 191's "Google Books scan of the 1965 Johnson Reprint Corporation reprint" is correct**, and its identifier — hedged as *"not stated … and is not guessed"* at six sites — is derivable by the same method the pass used on Possidius, should a future pass want to close it. `canonesapostolo00brungoog` (`sponsor: Google`, Harvard) and `diecyprianische00unkngoog` (`sponsor: Google`, Harvard) both confirm their headers' claims. `patrologiae_cursus_completus_lat_vol_036` carries no sponsor metadata, but its own text opens with Google's standard digitization notice and a `HARVARD COLLEGE LIBRARY` bookplate, confirming the Migne file's *"(a Google Books scan, Harvard University copy)"*. Only the Goldbacher intake fails (M1 above).

**Bold-marker nesting, independently reproduced across all four documents, run-aware.** markdown-it-py 4.2.0 (`commonmark`), **438** `**`-bearing lines. Result: **zero** nested `<strong>` spans, **zero** unclosed spans, **zero** literal `**` surviving any render, **zero** `****`, and **zero** lines where CommonMark's delimiter pairing differs from run-aware sequential pairing. One honest note on reproduction: Round 22 reported that a plain two-character scan produces three false mismatches at Registry lines 26 and 36 and Manifest line 69; with a `line.count('**')` implementation those three lines come out clean, because a run of exactly three asterisks contributes exactly one non-overlapping `**` either way. The three lines do carry `***word***` runs, so Round 22's diagnosis of the hazard is right; the three-mismatch figure is an artifact of a particular counting implementation, not a property of the lines. The load-bearing result — run-aware pairing identical to CommonMark on every line — reproduces exactly.

**Round 19's C1 — spot-checked, undisturbed, a fifth time.** `prosper_chronica-minora-1-lat_mommsen1892.txt` line **42582** reads `EPITOMA CHEONICON`; line **45881** reads `EPITOMA DE CHRONICON,`, between the praefatio's last line at 45876 (`De reliquis libris quicquam addere supervacaneum est.`) and the chronicle's first entry at 45891 (`1 Adam cum e.sset annorum CCXXX, genuit Setli.`). Identical to Rounds 19, 20, 21 and 22. The declination stands on five consistent checks.

**H1 (Round 22's) — the Licensed-For column, re-swept twice.** Replicating Round 22's own pattern list across all 212 rows now returns only rows 191 and 193, and in both cases the hits are either the correctly-scoped CSEL 58 residue or the earlier-draft text quoted inside the new correction notes. Both rewrites check out against every artifact they name: Manifest G1 (*"G1 is now closed in full"*), Manifest G4 (*"G4 now stays open for CSEL 58 only"*), rows 194/195/196 (all `**Vendored**`), row 39, row 61 (*"only Pars V (CSEL 58…) remains unacquired"*), Doc_02 §9 item 1. Row 193's *"CSEL 34/1, 34/2, and 44 are now all also vendored, as rows 195 and 196"* is right: row 195 covers CSEL 34/1 and 34/2 in one file (`sanctiaureliaugu34augu`, both 1895 and 1898 title pages recorded), row 196 covers CSEL 44. A second sweep with a widened pattern list produced L1 and L2 above and nothing else.

**M1 and M2 (Round 22's) — the six and four sites, each opened.** The identifier is present and correctly attributed at the vendored file's `Source:` line, Registry rows 45 and 192, the Manifest's G3 fulfilment paragraph, and the Decision Log's G3 entry in both its main paragraph and its "What remains open" list, which no longer names it as outstanding. Row 45's replacement sentence no longer asserts an underived identity; it now states the derivation. The M2 correction is present at the file's `Source:` and `Provenance note:` lines, at row 192, and at the Decision Log's main paragraph and action bullet. The three further instances are M2 above.

**L2 (Round 22's) — the attribution, and whether five is the right five.** All 19 files carry the clause exactly once; 5 read "Round 17; extended, Round 18; extended, Round 19; extended, Round 20" and 14 read "Round 18; extended, Round 19; extended, Round 20"; with the attribution normalized, the clause body is **byte-identical across all 19**. `git show 6fd4973` touched eight `cic/texts/` files with a "Round 17" note, and the three not in the fixed five carry different notes — the Getty barcode disclosure (`…goldbacher-csel34.txt`, `…goldbacher-csel44.txt`) and the Perpetua assignment fix (`…robinson1891.txt`) — not the OCR clause. The five are the right five. `git diff f0be10a..d35f00a -- cic/texts/` touches exactly one line in each of those five and two in the Possidius file; no other vendored file was altered.

**L1 (Round 22's) — both line-number claims, and every other line pointer in the four documents.** Manifest `grep "^## "` returns headings at 15, 65, 71, 81; 65 − 15 = 50, so *"fifty lines apart"* is exact. Registry line 295 is the recall-test/PRESS paragraph converted to a standing rule at Round 20's L3, and line 325's new parenthetical correctly distinguishes it from the round-by-round record immediately above. Every other live line pointer was checked: Doc_02 §3's `Source_Registry.md` "line 8" resolves to the checkpoint rule (line 6 is the Disclosed-placement rule); the Manifest's line 11 and line 61 both hold superseding notes; the Decision Log's "Doc_02 line 25" and "line 29" both resolve. The one that does not is C4 above.

**C1–C4 (Round 22's).** The Decision Log heading now reads *"each finding real defects, most fixed,"* which matches its own pattern paragraph's *"every single round"* and its own record of two deliberately unfixed findings. The Round 21 paragraph now names M1 and C1, which is what Round 21's own verdict paragraph calls *"the two structural ones … closed exactly"* (M1 = Doc_02 line 29's bold nesting; C1 = row 42's literal asterisks). Doc_02 §9 item 3 now separates row 38 correctly: row 38's Licensed-For does state a negative (*"Not currently licensed for a specific claim"*), the rule at Registry line 283 excludes exactly that, rows 34 and 35 by contrast state conditional positive licences and do carry the flag in their own notes, and the two alternative flag sites the new text names — §5's closing sentence (*"Flagged for this document's own future refinement pass and for priority second-opinion review"*) and §9 item 2 (*"basilica archaeology, CIL VIII … flagged for priority second-opinion review"*) — both exist and both reach row 38's material. The Lancel dating matches row 31's Discovery channel.

**Registry table integrity, recomputed row by row.** All 212 rows re-extracted by column position: numbers **1–212 complete, no gap, no duplicate**; **every row exactly 12 pipes / 11 columns**; every row balanced on `**`, parentheses and backticks. The same three physical-order inversions (48→42, 193→60, 60→52) Rounds 20, 21 and 22 found, all covered by the front-matter Disclosed-placement rule. Excluded set re-parsed from the Boundary Status column: `{28, 29, 98, 128, 204}`, unchanged. The pass inserted and deleted no Registry lines, so the file is still 329 lines and every pre-existing line pointer into it still resolves.

**Census and comparator arithmetic, recomputed across every atlas file.** `latin-pastoral-congregational-christianity.yaml`: **99 entries, 97 distinct titles, `Counter({'tradition': 90, 'context': 9})`, 88 distinct titles inside the tradition set, `Counter({'assigned': 87, 'provisional': 12})`**; exactly two duplicate titles (*The Enchiridion (On Faith, Hope, and Love)*, *The Passion of the Scillitan Martyrs*), so 90 − 2 = 88 reconciles. Comparators re-derived per measure: 99 raw against **68** (`post-apostolic-house-church.yaml`), 90 `tradition` against **59** (`alexandria-catechetical.yaml` and `post-apostolic-house-church.yaml`, tied). The nine `context` entries are Delehaye, Harnack, Monceaux I/II/III, both von Sodens, Prosper and the Codex Theodosianus — seven of nine modern (1901–1921) secondary scholarship, exactly as §1 says. Every figure in Doc_02 §1's opening paragraph holds.

**Engine scripts, both re-run this session.** `python cic/engine/texts_registry.py` → **exit 0**, *"OK: every vendored file has a header-verified rights line (public domain, or a recognized open licence), an ENTRIES row, and no ENTRIES row points at a missing file"*; 88 vendored files, 23 non-English, `cic/texts/` at 211 MB (30% of the 700 MB planning trigger). `python cic/engine/corpus_map_merge.py --check` → **exit 0**, 528 works → 788 assignments across 56 Atlas entries, no error. (H1's REGISTRY.yaml defect is invisible to both: neither script validates the prose in a `notes` field.)

**Cross-references.** Every row number cited anywhere in Doc_02 resolves inside 1–212. Every directional `§N above` / `§N below` reference in Doc_02 direction-checked programmatically: **none fails**. The Decision Log's `Doc_02 revision:` heading occurs exactly once, carries no round numbers, and holds exactly eight `**Round N**` paragraphs (15 through 22), matching its own *"one dated paragraph appended per round"*; Doc_02 §2's pointer quotes two strings from it, both still present and unique.

**The Decision Log's own new Round 22 paragraph, checked against the Round 22 artifact.** Its counts (1/2/3/4), its 437-line figure and its 434 comparator, its account of the H1 rows and quoted clauses, its six-site and four-site enumerations, and its L1/L2/L3 and C1–C4 summaries all match Round 22's own text. The pattern paragraph's new Round 22 sentences are accurate to the findings they describe.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the fix pass and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** H1 raises a genuinely cross-world surface — `cic/texts/README.md` and `download-queue-seed.yaml` are shared artifacts other worlds' build threads read — but the finding is that lpc's own registry entries for lpc's own files misstate lpc's own acquisition state, which is lpc's to correct on its own record; nothing here decides anything for another world, and no other world's entries were examined or touched. M1, M2 and M3 concern the provenance and contents of files in this world's own intake. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing here proposes a change to `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022, or any governing document. H1 and M1 are findings that entries do not match the intake convention already in force; M3 is a finding that a correction note misdescribes a primary artifact; L3 is a finding that an extraction step the corpus's own convention prescribes was not completed at one file's tail. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round disagrees with no prior round on a point of fact, and agrees with Rounds 20, 21 and 22 against Round 19 on C1, reached by reopening the file at the lines named. It departs from Round 22 on one calibration question only — rating L1 LOW where Round 22's Licensed-For calibration would suggest higher — and states its reason in the finding rather than asserting it. The two places this round could have produced an unresolved tension are M1 and M3, and both are closed rather than left open: M1 by fetching the archive.org item and comparing its full text against the vendored file at both ends, M3 by opening the vendored Pars III file at its own title page and index sections. Both are now checkable facts, not competing accounts, and neither requires the project lead. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

`Doc_02_Source_Ecology.md`'s status line and §10, and `Source_Registry.md`'s status line, still describe the Round 14 disposition of 2026-09-02, still read "Fourteen independent adversarial review rounds" over the sequence "(Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0)", and still point a reader to "`Doc02_Round1_Review.md` through `Doc02_Round14_Review.md`" — while `Review-Artifacts/` holds twenty-two `Doc02_Round*_Review.md` files before this one, and both documents carry in-text attributions to Rounds 15 through 22 throughout. Reported here as observed, checkable state, on the same footing Rounds 16 through 22 reported it. Whether and how those lines should change, and what disposition follows from this round's counts, is **not assessed here**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition.

**Observed trend, stated as raw counts only and not otherwise characterized.** Across the nine rounds against this 2026-09-08 revision: Round 15 — 4/6/5/2 (17); Round 16 — 4/5/6/3 (18); Round 17 — 0/3/5/4 (12); Round 18 — 0/4/3/3 (10); Round 19 — 0/2/4/3 (9); Round 20 — 1/4/5/5 (15); Round 21 — 0/4/5/4 (13); Round 22 — 1/2/3/4 (10); Round 23 — 1/3/4/4 (12). Three observations bear on reading this round's counts, stated without weighing them. First: **not one of this round's four most serious findings is a defect in the four documents' handling of the ten items they were asked to fix** — all ten are closed at every site Round 22 named, and the H1/M1/M2 corrections survive verification against the live archive.org items rather than only against the commit. Second: the HIGH and two of the three MEDIUM findings sit **outside the four documents entirely**, in `cic/texts/REGISTRY.yaml`, its generated README, `download-queue-seed.yaml`, and one vendored file's tail — artifacts the Decision Log's own intake entries name as steps of the same intakes, and that no round in twenty-two has opened. Third: the one MEDIUM inside the four documents (M3) is again text the fix pass itself wrote while closing its target, and again it is a characterization adopted from the review that named the finding rather than re-derived from the artifact — the shape this build's Decision Log has been recording under its own name since 2026-09-01.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 1 HIGH · 3 MEDIUM · 4 LOW · 4 COSMETIC.**
