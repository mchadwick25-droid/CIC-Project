# Doc_02 — Source Ecology, Source Registry, and Source Acquisition Manifest: Latin Pastoral-Congregational Christianity
## Round 25 Independent Adversarial Review — scoped to verifying the Round 24 fix pass (all fifteen findings addressed), a seventh spot-check of Round 19's declined C1, an independent re-run of the run-aware bold-nesting test and of the new mid-token fold-break scan this pass introduced, and a cold sweep extended across both shared machine-readable artifacts, both generated derivatives, the four vendored files this pass rewrote, and the corpus-map staging files lpc's own 2026-09-08 vendoring wrote

**Documents reviewed (committed state — `git status --porcelain` clean, 0 lines, at `8c2a322`, "lpc: fix Round 24 review findings on Doc_02 revision (15 of 15)", 2026-09-08 10:56:55 UTC, on branch `claude/record-native-world-build-v2-yq11wl`):**
- `worlds/lpc/Doc_02_Source_Ecology.md` (156 lines by `wc -l`, as are all counts in this list; §1 through §10 read cold)
- `Source_Registry.md` (329 lines; all 212 rows re-parsed by column position, all eleven columns, plus a whole-table sweep of every column under a widened pattern list including, for the first time in this sequence, the *provenance-step* patterns — "usage notice," "chrome," "stripped" — rather than only acquisition-state patterns)
- `Source_Acquisition_Manifest.md` (89 lines, read in full)
- `lpc_Decision_Log.md` (344 lines, read in full — every entry, with the three 2026-09-05 intake entries read paragraph by paragraph against the vendored files, the Registry rows, the Manifest, and both shared registries, and with the two newly-written **Round 23** and **Round 24** paragraphs checked clause by clause against `Doc02_Round23_Review.md` and `Doc02_Round24_Review.md`)
- `Review-Artifacts/Doc02_Round24_Review.md` (323 lines, read in full) and `Doc02_Round23_Review.md`, plus `git show 8c2a322`, `git diff cc489ab..8c2a322` at word level on every changed line in every changed file, and `git show cc489ab:…` on the specific paragraphs this pass rewrote
- **`cic/texts/REGISTRY.yaml` (all 88 entries parsed; every lpc-related `notes` field read in full against the Registry row and the vendored file header it describes; all 88 swept twice, once for acquisition-state staleness and once for mid-token fold breaks in *both* directions), `cic/texts/README.md` (regenerated to a scratch copy and byte-compared), `worlds/_cross-world/download-queue-seed.yaml` (all 22 queue entries, every lpc `why` read in full), and `worlds/_cross-world/DOWNLOAD-QUEUE.md` (regenerated and byte-compared, then the tree confirmed clean)**
- The vendored files opened directly: `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`, `cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` (read at its two title pages, all four index headings, and its Praefatio/Vita/Acta/Index-operum boundaries), `augustine_epistulae-critical_goldbacher-csel57-pars4.txt`, `augustine_epistulae-124-184a-lat_goldbacher-csel44.txt`, `possidius_vita-augustini_weiskotten1919.txt`, `perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`, `prosper_chronica-minora-1-lat_mommsen1892.txt`
- `cic/corpus-map/tertullian-s-voice.yaml`, `cic/corpus-map/_staging/perpetua-scillitan-martyrs-lat-grc_robinson1891.yaml`, `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` and every other `works`-bearing atlas file; both engine scripts
- **Three live archive.org fetches, metadata plus full text** — `sthascicaecilic01hartgoog` (2,147,270 bytes), `CSEL57` (1,574,207 chars) and `sanctiaugustiniv00possrich` (386,678 chars) — run because this pass asserts a new item identity (M3) and *removes* a provenance step (L3) from two files, and both are checkable only against the source items themselves

**Review date:** 2026-09-08
**Reviewer:** independent adversarial review thread. Did not draft any of the four documents, did not perform the 2026-09-05 or 2026-09-08 vendoring, did not write the Round 15–24 fix passes, and did not write Rounds 1–24.

**Scope, stated plainly.** Five briefs, run together. First: verify, independently and against primary artifacts, whether each of the fifteen Round 24 findings is closed at **every** site named in **every** file named — and, since every one of the ten preceding fix passes introduced or left at least one checkable error while fixing what it targeted, look specifically for the three shapes this revision's history names (a fix that creates a new defect in the same sentence; a fix whose scope stops short of a sibling site; a claim written into a live document without re-derivation). Second: verify the two claims this pass could not have made without going outside the repository — the Hartel item identity (M3) and the *removal* of the public-domain-usage-notice claim (L3) — by fetching the three archive.org items and comparing their own text against the vendored files, rather than trusting either the review or the pass. Third: check the two newly-written Decision Log paragraphs (M2's fix) clause by clause against the review artifacts they describe, and the "pattern worth naming" and escalation paragraphs against the state they now claim. Fourth: independently reproduce the run-aware bold-nesting test, both YAML parses, and the mid-token fold-break scan this pass introduced — in both directions, not only the one the pass's own regex covers. Fifth: a cold sweep across the four documents, both shared YAML artifacts, both generated derivatives, the four vendored files this pass rewrote, and — new to this round — the corpus-map staging file lpc's own 2026-09-08 vendoring wrote for another world's bucket. Rounds 15–24 and the `8c2a322` commit message were treated as claims to re-derive, not as authority.

**Method — what was actually re-derived, not trusted.** A CommonMark render (markdown-it-py 4.2.0, `commonmark` preset) of every `**`-bearing line in all four documents (440 lines), with `<strong>` open/close counts, nesting, literal `**` survival and `****` compared line by line against a **run-aware** sequential pairing (a maximal run of two or three asterisks contributing exactly one delimiter). A fresh regex parser over all 212 Registry rows extracting all eleven columns by position, with row-number sequence, physical order and per-row pipe count. `yaml.safe_load` on both edited YAML files and on all `works`-bearing atlas files, with every census figure and comparator in Doc_02 §1 recomputed from raw YAML. Two independent fold-break scans of both YAML files: the pass's own (`[A-Za-z0-9][_/-]$`) **and** its mirror (a line ending in a word character whose successor line opens with `/`, `_`, `-` or closing punctuation), plus a walk of every *loaded* string value for the resulting `token_ token` / `token/ token` signature. `python cic/engine/texts_registry.py --write-readme` and `python worlds/_cross-world/gen_download_queue.py` both re-run against scratch copies and byte-compared, then the tree re-checked clean. Live archive.org metadata and full-text fetches, whitespace-normalized and compared against the vendored files at both ends and for the presence or absence of a public-domain notice. Direct reads of the Prosper file at 42580–42585 and 45876–45892; of the Hartel Pars III file at lines 25–80, 18617, 27256, 27335, 36057, 40258, 41413, 41629 and its tail; of the CSEL 44 file's own letter headings and the CSEL 57 file's first heading. Both engine scripts re-run from `/home/user/CIC-Project`. Nothing was carried forward from Rounds 15–24, from `lpc_Decision_Log.md`, or from the commit message.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 0 HIGH · 4 MEDIUM · 5 LOW · 5 COSMETIC.**

**No HIGH finding, for the first time since Round 21 — and the two HIGH-rated fixes this pass was commissioned for are genuinely and completely closed.** `cic/texts/REGISTRY.yaml`'s CSEL 44 and Robinson 1891 entries now state the corrected facts, both carry a dated correction naming what they replaced, and `cic/texts/README.md` regenerates byte-identically from the YAML (H1). `worlds/_cross-world/DOWNLOAD-QUEUE.md` regenerates byte-identically from the seed, and its one lpc row now advertises CSEL 58 alone (H2). Both engine scripts pass, the Registry table is intact at 212 rows, and the whole eighteen-pattern acquisition-state sweep across all 212 rows and all 88 registry entries returns no live false claim. The three archive.org identities this build now publishes — `sthascicaecilic01hartgoog`, `CSEL57`, `sanctiaugustiniv00possrich` — were each re-fetched this round and each matches its vendored file character for character at both ends, and the new Hartel derivation (M3) holds in every particular, including the `sponsor: Google` / `books.google.com` / `date: 1868` / `NOT_IN_COPYRIGHT` metadata the file's own header now cites.

**Where the recurrence went this time: into the sites a review *listed* but did not *quote*, and into the fix pass's own replacement prose.** Round 24's M3 named the surviving hedge at six places and said, in terms, that the Decision Log's 2026-09-05 G1 entry carries it **twice**. One of the two is fixed; the other (line 210) still says the identifier is "left as an open item in the file's own header and in the Registry row below, to be filled in if supplied" — a sentence now false about both artifacts the same commit rewrote. Round 24's L3 named the unsupported "public-domain usage notice" claim at "both files' `REGISTRY.yaml`/README entries"; the pass fixed those and the two vendored files and left the same claim standing at `Source_Registry.md` **rows 192 and 193**, so the Registry of record now contradicts the file headers of the same commit. Round 24's C4 enumerated **five** pointers by file and line; four are fixed, Doc_02 line 23 is not, and both the commit message and the new Decision Log paragraph record "all five fixed."

**And the new prose written to close the findings carries three fresh, checkable errors.** The Pars III file's rewritten `Content note:` — written specifically because the old one was incomplete — says the volume's title page names **five** components while quoting the three it actually names in the same parenthesis, omits the third of the file's three indices (≈20% of the file), and ends its "in sequence" list at the *Acta* when a further ~970-line `INDEX OPERVM` follows it. The Decision Log twice says a correction this build made on **2026-09-08** was made "years ago." And the identifier-confirmation notes cite two different, wrong Round 24 finding numbers at three sites for the same fact.

---

## MEDIUM

### M1. The L3 fix removed the unsupported "public-domain usage notice" claim from the two vendored files and both `REGISTRY.yaml` entries and left it standing at `Source_Registry.md` rows 192 and 193 — so the Registry of record now contradicts the file headers rewritten in the same commit

Round 24's L3 found that "archive.org site-navigation chrome **and a public-domain usage notice** were stripped" describes an extraction step performed on material the source items do not contain, and named the residue at four places: the Goldbacher file, the Possidius file, "and in both files' `REGISTRY.yaml`/README entries."

All four are fixed, and correctly. `augustine_epistulae-critical_goldbacher-csel57-pars4.txt`'s `Provenance note:` now reads *"archive.org site-navigation chrome **was** stripped from the head of the file … the 'public-domain usage notice' that same earlier draft claimed was stripped is dropped here too, independent review Round 24's own L3, since the source item's own text carries no such notice."* The Possidius file and `REGISTRY.yaml` lines 1035 and 1065 carry the parallel correction.

`Source_Registry.md` line 249 (**row 192**) does not:

> Site-navigation chrome, **a public-domain usage notice**, and a scanned UC Berkeley circulation due-date slip bound into the back of the physical volume (a library artifact, not part of the work) were all stripped, doubled inter-word spacing normalized, nothing else altered.

`Source_Registry.md` line 250 (**row 193**) does not:

> Site-navigation chrome **and a public-domain usage notice** stripped, doubled inter-word spacing normalized, nothing else altered.

**Re-derived at source this round rather than taken from Round 24.** `https://archive.org/download/CSEL57/CSEL57_djvu.txt` (1,574,207 characters) begins, with nothing before it, `M RIPTORVM ECCLESIASTICORVM / LATINORVM / EDITVM CONSILIO ET IHPENSIS / ACADEMIAE LITTERARVM CAESAREAE VINDOBONENSIS / VOL lvh.` — whitespace-normalized, **identical to the vendored file's own body opening for the first 200 characters**, and identical at the last 150 characters too. `sanctiaugustiniv00possrich_djvu.txt` (386,678 characters) begins `SANCTI AUGDSTINI VITA iCRIPTA A POSSIDIO EPISCOPO IC-NRLF …` — again identical to the vendored file's own opening 200 characters. Neither item's text contains the phrase "public domain" anywhere; a case-insensitive count of "google" returns **0** in both. (The *Hartel* item, by contrast, does carry Google's standard notice — 2,953 normalized characters of it before the vendored file's own opening — which is why row 191's identical clause is correct and was rightly left alone.)

**Why this is MEDIUM rather than LOW, where Round 24 put the same claim.** Round 24 rated L3 LOW and stated its limit honestly: "what Mark's compiled docx contained cannot be re-derived from here, so the claim is unsupported rather than proven false." That limit still holds. What has changed is that the claim is now stated **two ways inside one commit**: the vendored file's own header says the notice "cannot be verified from here and is not claimed," and the Registry row describing that same file says it "was stripped." A reader consulting the Registry of record and the artifact it records gets opposite answers, and the Registry is the document a future Doc_03 draws from. This is the same shape Round 23's M2 (three un-swept instances of a corrected-away phrase) and Round 24's L1 were rated at; the internal contradiction between two artifacts the same commit edited is what moves it up.

### M2. The Decision Log's G1 entry still hedges the Hartel identifier as open at the second of the two sites Round 24's M3 explicitly named — and now states, falsely, that the vendored file's own header and Registry row 191 leave it open

Round 24's M3 listed where the hedge stood: *"Registry **row 191**'s Verification Note …, `cic/texts/REGISTRY.yaml` line 997 and `README.md` line 167, `download-queue-seed.yaml` `queue[6]`, the Manifest's G1 fulfilment paragraph, and the Decision Log's 2026-05-05 G1 entry **(twice)**."*

Five of those six are closed, and closed well. `lpc_Decision_Log.md` line 226 (the G1 "What remains open" paragraph) was rewritten by the M4 fix and now names the identifier as confirmed. The other occurrence, at **line 210**, is untouched:

> **What was actually received…** The exact archive.org item identifier was not stated by the project lead and was not guessed, per this project's own no-invented-identifiers discipline — **left as an open item in the file's own header and in the Registry row below, to be filled in if supplied.**

The first clause is a true statement about 2026-09-05 and can stand. The second is a present-tense claim about two other artifacts, and this commit made it false at both: `cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`'s `Source:` line now reads *"is now independently confirmed rather than guessed — confirmed here, independent review Round 24's own M3: `sthascicaecilic01hartgoog`,"* and Registry row 191 (line 248) carries the same. Nor was it "filled in if supplied" — it was derived.

**What makes this the scope-propagation shape rather than an oversight of scale.** The structurally identical paragraph one entry below, in the G3 entry (line 236), already carries exactly the treatment this one needs, written by the Round 22 fix pass: *"The exact archive.org item identifier was not stated when supplied and was not guessed at the time. **Corrected here, independent review Round 22's own M1 and M2: the identifier is now independently confirmed — `sanctiaugustiniv00possrich`, matched byte-for-byte at both ends.**"* The pattern was available, one entry away, and Round 24 had said in terms that this entry carries the hedge twice.

Rated MEDIUM on the same footing Round 24 rated M3 and M4 — a present-tense claim about acquisition/identification state that a later event falsified, inside a dated entry whose own later siblings do record the closure, so a reader of the log in order is not left with only the false statement.

### M3. The L2 fix's replacement enumeration is itself wrong in two new ways and short in a third — the file's title page names three components, not five; the "in sequence" list ends at the *Acta* when a further ~970-line index follows; and one of the file's three indices is missing

The L2 fix rewrote `cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt` line 9:

> Content note: Corrected here, independent review Round 24's own L2, from an earlier draft's own "three components in sequence," which omitted **two of the five the volume's own title page names (OPERA SPVRIA. INDICES. PRAEFATIO)** and which occupy roughly half the file. This file carries, in sequence: (1) Cyprian's own spuria …, (2) the volume's own scriptural index and its *Index nominum et rerum* …, (3) the editorial *Praefatio*, (4) the *Vita Caecilii Cypriani* …, and **(5) the *Acta Proconsularia*** …

**(a) The title page names three, not five, and the sentence quotes all three in its own parenthesis.** Read directly: the file carries two title pages, at line 27 (`YOL. III. PARS III. APPENDIX.` / `S. THASCI CAECILI CYPEIANI OPEEA SPVRIA CVM INDICIBVS ET PKAEFATIONE`) and at lines 52–54 (`PARS III.` / `(OPEEA SPVRIA. INDICES. PKAEFATIO)`). Both name the same three things. The five-item list is derived from the file's physical contents — which is correct and is exactly what row 191's own rewrite says ("per the printed volume's own title page, *Opera Spuria. Indices. Praefatio* — the *Opera Spuria*, the *Vita*, and the *Acta* bound in among the spuria, **plus** the volume's own scriptural and name/subject indices and its editorial praefatio"). The Content note collapses the derivation into the title page and thereby asserts something the line it quotes disproves.

**(b) The file does not end at the *Acta*.** Component boundaries, read directly across all 42,600 lines: Appendix/spuria from line 78; `I. INDEX SCEIPTORVM.` at **18617**; `Index nominum et rerum.` at **27256**; `III. INDEX YBEBOKVM ET LOC^TIONVM.` at **27335**; `PRAEFATIO.` at **36057**; `VITA CAECILII CYPRIANI` at **40258**; `ACTA PEOCONSVLARIA.` at **41413**; and then **`INDEX OPERVM` at 41629**, running to the file's last line at 42600 — a further ≈971 lines (≈2.3% of the file) after the note's own final component. A reader told the file "carries, in sequence … (5) the *Acta Proconsularia*" is told the file ends where it does not.

**(c) One of the three indices is missing from item (2).** The note names "the volume's own scriptural index and its *Index nominum et rerum*" — two of three. The third, `INDEX VERBORVM ET LOCVTIONVM` (line 27335), runs to 36056: **8,722 lines, ≈20% of the file**, larger than either of the two the note does name.

**Why this is MEDIUM.** This is Round 23's own M3 verdict recurring at the site Round 24's L2 sent the fix to: *"substituted an enumeration that was itself incomplete in the other direction."* Round 23 rated that MEDIUM; Round 24 rated the surviving short enumeration LOW because it was merely short. This one is not merely short — limb (a) asserts something the quoted line contradicts, and limb (b) is a checkably wrong statement about where the file ends, in the header of the file it describes. The build now carries three different enumerations of the same volume: three components (Registry row 194 line 259, row 39, `REGISTRY.yaml`'s Pars III entry, the Pars I–II file's own Content note, `download-queue-seed.yaml` `queue[7]`), six (row 191), and this five.

### M4. The two newly-written Decision Log paragraphs say a correction this build made on 2026-09-08 was made "years ago" — twice

`lpc_Decision_Log.md` line 340, new text (the **Round 24** paragraph):

> … a self-contradicting Letter-185 claim the vendored file, Registry row 196, and this log's own Round 16 paragraph **corrected years ago** …

`lpc_Decision_Log.md` line 342, new text (the pattern paragraph):

> … at two further false claims each **corrected elsewhere in this build years ago** …

Both are false, and the log itself is the disproof. Every round in this sequence — 15 through 24 — carries **Review date: 2026-09-08** in its own artifact; the entry these two paragraphs sit inside is headed `### 2026-09-08 — Doc_02 revision: independent adversarial review rounds…`; the intakes the corrections touch are dated 2026-09-05 and 2026-09-08; the whole document set is eight days old (drafted 2026-09-01). Round 16's Letter-185 correction and Round 17's Perpetua correction were made **the same day** as the Round 24 finding that they had not been swept into `REGISTRY.yaml`. A repository-wide grep confirms "years ago" occurs nowhere else in this world's folder, in any vendored file, or in either shared artifact — both instances are new prose from this pass.

Round 24's own text says neither of these things: its H1 heading reads "one corrected at every other site since **Round 16**, the other since **Round 17**," and its summary says "corrected everywhere else in this build **long ago**." The exaggeration was introduced in the transcription.

**Why this is MEDIUM rather than a stylistic quibble.** This log exists to be the authoritative, checkable chronology of the build — it has been corrected across five separate rounds for post-disposition edit counts, for insertion-order errors, for stale round enumerations, and for two ordinals it stated two ways. A claim that a defect stood uncorrected "for years" in a build eight days old is the same class of error, stated twice, in the paragraph written to close a MEDIUM finding about this entry's own record-keeping, and it materially misdescribes how long the blind spot Round 23 and Round 24 diagnosed actually persisted.

---

## LOW

### L1. C4 was fixed at four of the five pointers Round 24 named by file and line; Doc_02 line 23 is untouched, and both the commit message and this log's own new Round 24 paragraph record "all five fixed"

Round 24's C4 was explicit about the sites: *"The log dates **four** entries 2026-09-01 (lines 11, 31, 41, 53), and five live pointers name that date with no title: **Doc_02 lines 15 and 23, `Source_Registry.md` lines 14, 40 and 275.**"*

Four are fixed, each by quoting its target entry's own heading — Doc_02 line 15, and Registry lines 14, 40 and 275. `git diff cc489ab..8c2a322` on the two files shows exactly four such replacements, and Doc_02 shows only two changed lines in total (15 and 67).

Doc_02 **line 23** still reads, inside the Optatus paragraph:

> … (see the escalation section, §10 below, and **`lpc_Decision_Log.md`, 2026-09-01**).

That is the exact form C4 was about, at the exact line C4 named. The commit message states *"C4: five ambiguous 'lpc_Decision_Log.md, 2026-09-01 entry' pointers, disambiguated by quoting each target entry's own heading,"* and `lpc_Decision_Log.md` line 340 now records *"(C4, **all five** fixed)."*

Rated LOW rather than COSMETIC: the underlying ambiguity is cosmetic and Round 24 rated it so, but the record's claim of completeness is not — the same shape as Round 24's own L1 (three of four sites closed, with the commit message enumerating only the three).

### L2. The newly-written Round 23 Decision Log paragraph opens with two summary claims its own body contradicts

`lpc_Decision_Log.md` line 338, both clauses new this pass:

**(a)** *"— all ten of **Round 22's own findings** genuinely closed, the two hardest (**the Goldbacher not-a-Google-scan finding** and the Possidius identity) surviving re-derivation from a live archive.org fetch."* Round 22's not-a-Google-scan finding was its **M2**, about **Possidius**; its M1 was the Possidius identity. The Goldbacher not-a-Google-scan finding is Round 23's own **new M1** — as this same paragraph says, five sentences later: *"Checking whether the sibling Hartel and Goldbacher intakes carried the identical 'Google Books scan' defect Round 22 found at Possidius (**a question Round 22 explicitly declined to answer**) found … Goldbacher's genuinely wrong … (M1, fixed)."* Round 23's own "What was checked and found clean" section confirms which pair it re-derived: *"Every element of the **M1 and M2** corrections holds at source"* — both Possidius.

**(b)** *"Its own findings **moved entirely past the four core documents** into artifacts no round in twenty-two had opened."* The same sentence's own continuation lists Round 23's M3 (Registry **row 191**), L1 (**row 67**), L2 (**row 39**), L4 (**Doc_02 §3** and **this log** line 138), C2 (the **Manifest**), C3 (**Doc_02 §3**) and C4 (**this log**). Round 23's own disposition note states the correct version: *"the HIGH and two of the three MEDIUM findings sit **outside** the four documents entirely … the one MEDIUM **inside** the four documents (M3)."*

Rated LOW on the calibration Round 19's L4 (a Decision Log paragraph miscounting the round it describes) and Round 22's C2 (a Decision Log paragraph misnaming which pair of a round's findings closed exactly) established for this exact class.

### L3. The identifier-confirmation notes cite the wrong Round 24 finding number at three sites, and two different wrong numbers among them

The Goldbacher/CSEL 57 identifier confirmation is Round 24's **L1**. Three sites now attribute it as follows:

| site | attribution |
|---|---|
| `Source_Acquisition_Manifest.md` line 35 (G4) | "independent review Round 24's own **L1 and M1**" |
| `lpc_Decision_Log.md` line 260 (G4 Context) | "independent review Round 24's own **L1 and M1**" |
| `download-queue-seed.yaml` `queue[12]` | "independent review Round 24's own **L1 and M3**" |

Round 24's **M1** is the surviving "Google Books chrome" phrase in this log's G4 action list — a different defect in a different artifact. Round 24's **M3** is the *Hartel* identity, a different file entirely. Neither is about the CSEL 57 identifier, and the two YAML/markdown sites disagree with each other about which one to blame. All three would be right with "L1" alone (or with "Round 23's own M1," which is where the identity was first derived and which the vendored file's own `Source:` line and Registry row 193 both correctly say).

Rated LOW, not COSMETIC, because it is an attribution error in three separate artifacts including a shared cross-world one, and because the sequence has fixed the same class at Round 21's L1 and Round 22's C2.

### L4. The M4 fix's own new sentence credits the Possidius identifier to Round 24's M3 while its own parenthesis credits it correctly, and reintroduces a positional pointer that is off by two entries

`lpc_Decision_Log.md` line 277, wholly rewritten by this pass:

> … and all three identifiers — this file's own (`archive.org/details/CSEL57`), Hartel's (`sthascicaecilic01hartgoog`), and Possidius's (`sanctiaugustiniv00possrich`, **confirmed by the entry three above this one**) — are now independently confirmed, **the last two by Round 24's own M3**.

Two errors, in one sentence:

1. **"the last two by Round 24's own M3"** is false of the Possidius identifier, which was confirmed by **Round 22's own M1** — as this same log says at line 236 (*"Corrected here, independent review Round 22's own M1 and M2: the identifier is now independently confirmed — `sanctiaugustiniv00possrich`"*), and as the same sentence's own parenthesis implicitly concedes by pointing at that entry rather than at M3.
2. **"the entry three above this one"** does not resolve. `grep "^### "` gives the log's entry starts: the G1 entry at line 206, the **G3 entry at line 230**, the G4 entry (this one) at line 258. The G3 entry is the entry **immediately** above. Separately, the "Two more Decision Log pointer/count defects found by Round 6" entry retired exactly this language for exactly this reason: *"this log's own directional language ('above,' 'below,' 'the next entry,' 'the most recent entry,' 'the entry after this one') is retired in favor of dated, titled pointers."*

Rated LOW on the same footing as Round 22's L1 (two wrong adjacency claims in new correction text).

### L5. `cic/corpus-map/_staging/perpetua-scillitan-martyrs-lat-grc_robinson1891.yaml`, and the generated `tertullian-s-voice.yaml` it feeds, name the wrong vendored file as the source of the already-present English Perpetua entry — in another world's own corpus-map bucket

The H1(b) fix is right, and its supporting claim checks out: `cic/corpus-map/tertullian-s-voice.yaml` does carry two `The Passion of the Holy Martyrs Perpetua and Felicitas` entries, and the second is `role: tradition`, `confidence: assigned`, `source_file: perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`, exactly as `REGISTRY.yaml` now says.

That second entry's own `note`, written by lpc's own 2026-09-08 vendoring and reproduced verbatim in the generated atlas file, says:

> Latin/Greek second witness for the ALREADY-PRESENT English-language entry in tertullian-s-voice.yaml (**source_file anf09_gospel-of-peter-diatessaron-origen-commentaries.xml**), per Mark's own 2026-08-26 ruling …

The already-present entry, seventeen lines above it in the same generated file, is `source_file: **anf03_tertullian.xml**`, `locus: div2 6.6 under div1 'Ethical.' (printed as an Appendix)`. Checked directly: `anf09_gospel-of-peter-diatessaron-origen-commentaries.xml` contains the string "Perpetua" three times, all in editorial footnotes (*"the Passion of S. Perpetua and the visions contained in the History of Barlaam and Josaphat"*, and two similar), and carries no such work; `anf03_tertullian.xml` carries it as the printed Appendix. The `anf09` identifier is evidently carried over from the sibling *Scillitan Martyrs* assignment directly above it in the same staging file, where it is correct.

Rated LOW rather than higher: the assignment itself is right, the atlas file's own correct entry sits seventeen lines above the wrong cross-reference, and no lpc claim rests on it. It is recorded because it is a checkably false statement about which vendored file carries a work, in a shared cross-world artifact for a world other than lpc, written by lpc's own vendoring, and no round 1 through 24 has opened the staging file it comes from. `Source_Registry.md` row 204 (line 269) and the vendored file's own `Content note:` do **not** repeat the error — both name only the ruling, not a source file.

---

## COSMETIC

### C1. The new fold-break scan is one-directional, and one instance of the same defect class survives in `REGISTRY.yaml` — visible in the generated README, where the same publisher pair is rendered both ways

The scan this pass introduced (`[A-Za-z0-9][_/-]$`, line by line) is genuinely effective in the direction it covers. Reproduced from scratch this round on both files: **`REGISTRY.yaml` returns one hit, line 39 — a `#` comment, not a folded scalar — and `download-queue-seed.yaml` returns none.** All three REGISTRY.yaml instances Round 24's L4 named, and all four pre-existing seed instances the pass swept up alongside them, are genuinely gone, and a walk of every loaded string value confirms no `token_ token` / `token/ token` signature survives from them.

The mirror direction is not covered. `REGISTRY.yaml` lines 683–684:

```
    Basil of Caesarea, 'The Ascetic Works of Saint Basil', trans. W. K. L. Clarke, D.D. (SPCK
    / Macmillan, 1925, Translations of Christian Literature Ser. I) - supplied as …
```

The fold makes the loaded value `(SPCK / Macmillan, 1925`, and `cic/texts/README.md` line 163 publishes it that way — while line 181, for `macarius_fifty-spiritual-homilies_mason1921.txt`, has the same publisher pair unbroken as `(SPCK/Macmillan, 1921)`. Pre-existing, not lpc's own entry, and no claim is harmed; recorded because the pass's own commit message states `REGISTRY.yaml` was "swept for the same defect class," and the class includes both directions.

### C2. Registry row 194's *other* OCR quotation is silently normalized, in the same cell whose Vita-heading quotation carries the disclosure

Row 194 (line 259) opens its verification with *"title page (**"VOL. III. PARS III. APPENDIX"**) and the Vita's own heading … directly verified"* and then discloses, in bold, exactly one normalization: *"the file's own OCR reads 'iiiilgo' for 'uulgo,' and the heading itself runs across two lines with a closing period this quotation drops."* The file's line 27 reads, literally, `YOL. III. PARS III. APPENDIX.` — `YOL` for *VOL*, and a closing period the quotation also drops. This is precisely the defect Round 19's C3, Round 20's C3 and Round 24's C1 have each fixed once, at row 194's Vita heading, at row 204's consular formula, and (this pass) at row 191's title page; the remaining instance is in the same cell as the first of those.

### C3. The lpc row this pass published into `DOWNLOAD-QUEUE.md` carries a "see entries below" that resolves in the seed and not in the generated index

The H2 fix is correct and complete — `gen_download_queue.py` now reproduces the committed file byte for byte. The title it publishes is:

> S. Aureli Augustini Hipponiensis episcopi Epistulae, remaining volume (CSEL 58 only -- 34/1, 34/2, and 44 downloaded 2026-09-08, **see entries below**)

In `download-queue-seed.yaml` that resolves: `queue[10]` and `queue[11]` sit below `queue[9]`. `DOWNLOAD-QUEUE.md` renders only `not-yet-downloaded` rows, so the two entries pointed at are not in it; the only row below lpc's is a `desert` wants-register item. The substantive content ("34/1, 34/2, and 44 downloaded 2026-09-08") is self-contained and correct, so nothing is misstated — this is the same navigational class as Round 24's C5, one artifact further downstream. (`queue[12]`'s own C5 fix is right and was verified: `queue[9]` is indeed three entries up. It keeps a relative count alongside the stable name, which will go stale on the next insertion the way the phrase it replaced did.)

### C4. The same instance of the corrected-away "Google Books chrome" phrase is given two different ordinals inside the same Decision Log entry

Line 269 (the G4 action list) and line 340 (the new Round 24 paragraph) both call it *"a **fifth** surviving instance."* Line 342 (the pattern paragraph, also new this pass) calls it *"a **fourth** instance of an already-three-times-corrected phrase."* Both are defensible on different counting bases — sites enumerated by Round 23's M1 versus rounds of correction — but the entry's own neighbouring usage (line 240: *"a **third** surviving instance of the M2 correction above"*) is site-counting, and this log has twice retired running ordinals precisely because they were stated two ways in one commit ("Pattern instances found by Round 4"; "Two more Decision Log pointer/count defects found by Round 6").

### C5. Two residual undated "this session" bullets in the very Doc_02 §3 block the C3 fix declares consistent; and the Hartel file header calls itself a "row"

**(a)** The C3 fix is right on its facts — row 32's Discovery channel reads `WebSearch / 2026-09-01; re-verified via WebSearch (ISBN/catalogue cross-check) / 2026-09-02`, exactly matching the bullet's new "original 2026-09-01 drafting session" plus "separate 2026-09-02 post-disposition pass." Its parenthetical then claims consistency "with the Brown, Lancel, and Burns & Jensen bullets, which now date their own checks the same way." Two bullets further down the same list, Fahey (line 69) and Rebillard (line 70) both still read *"not independently checked or WebSearch-verified **this session**"* — the identical undated phrase that has now needed disambiguation in four consecutive rounds (Round 21's C3, Round 22's C4, Round 23's C3, Round 24's C3). Weaker than those, since both state a negative; recorded because the boundary has moved four times and the block is one list.

**(b)** `cic/texts/cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt`'s new `Source:` line closes with *"whose own metadata carries the 1868 date and NOT_IN_COPYRIGHT status **this row's own rights basis** states independently."* The sentence is correct in substance (verified: `date: 1868`, `possible-copyright-status: NOT_IN_COPYRIGHT`) but was evidently written for Registry row 191, where the identical clause also appears; a vendored file's header has a `Rights:` line, not a row.

---

## What was checked and found clean

Recorded at the same length as the findings, since a clean result in this project is checked with the same rigour as a dirty one.

**H1, both entries, and the README regeneration.** `cic/texts/REGISTRY.yaml` line 1103 now reads *"Goldbacher's CSEL 44 (1904): Augustine's Epistulae 124-184A. **Does NOT include Letter 185** … corrected here, independent review Round 24's own H1, from an earlier draft's own self-contradicting 'including Letter 185,' which the file's own letter headings (running only to CLXXXIV A.) already disprove."* Re-derived from the vendored file directly rather than from the correction: `augustine_epistulae-124-184a-lat_goldbacher-csel44.txt`'s letter headings run `CLXXXIV.` (line 39721), `CLXXXIV A.` (line 39921) and stop; its single `^CLXXXV` hit at line 20250 is the apparatus cross-reference `CLXXXVII, 39 in. seducebant…`; `CLXXXV.` opens `augustine_epistulae-critical_goldbacher-csel57-pars4.txt` at its line 44. Line 1192 now reads *"The Passio S. Perpetuae **is already assigned** -- to tertullian-s-voice, per Mark's own 2026-08-26 ruling,"* verified against `cic/corpus-map/tertullian-s-voice.yaml` (two entries, lines 6 and 23; the second `role: tradition`, `confidence: assigned`, `source_file: perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`). Both corrections are reproduced at `README.md` lines 159 and 220. `python cic/engine/texts_registry.py --write-readme` re-run against a scratch copy: **no diff**, and `git status --porcelain` clean afterwards.

**H2, and the generated queue.** `python worlds/_cross-world/gen_download_queue.py` re-run and byte-compared: **no diff**. `DOWNLOAD-QUEUE.md`'s one lpc row now reads *"remaining volume (CSEL 58 only -- 34/1, 34/2, and 44 downloaded 2026-09-08…)"*, matching `queue[9]`, Registry rows 195/196, Manifest G4, row 61 and Doc_02 §9 item 1. Header count reconciles: "**7 candidate(s)**: 6 proactively verified, 1 surfaced reactively" over six proactive rows and one wants row. (Its "see entries below" is C3 above.)

**M3's Hartel identity, re-derived from the live item rather than from the pass.** `https://archive.org/metadata/sthascicaecilic01hartgoog` returns `title: S. Thasci Caecili Cypriani Opera omnia`, `sponsor: Google`, `source: http://books.google.com/books?id=uuDN6Gn-9hgC&oe=UTF-8`, `date: 1868`, `publisher: Vindobonae [Vienna, Austria] : Apud C. Geroldi filium`, `possible-copyright-status: NOT_IN_COPYRIGHT`. Its `_djvu.txt` is **2,147,270 bytes**; whitespace-normalized, it opens with Google's standard public-domain digitization notice (2,953 characters of it), after which the text runs `CORPVS SCRIPTORVM ECCLESIASTICORVM LATINORVM … ACADEMIAE LITTEEARVM CAESAKEAE … VOL, III. PARS L … EX EECENSIONE G. HAETELIL … Reprinted with the premission o£ the original publishers.` — the vendored file's own body opening **character for character, garble for garble** — and both texts end identically at `…Ad presbyteros et diaconos explicit z, om» Gr§(i, —`. The exact-case string `S. Thasci Caecili Cypriani Opera omnia` occurs **zero** times in the item's own text and matches only its `title` metadata field, independently re-confirming Round 23's L3 removal as well. Every element of the M3 derivation holds, and it is now stated consistently at five of the six sites (the sixth is M2 above): the vendored file's `Source:` line, Registry row 191, `REGISTRY.yaml` line 998 / README line 167, `download-queue-seed.yaml` `queue[6]` (whose previously-`null` `url` is now `https://archive.org/details/sthascicaecilic01hartgoog`), and the Manifest's G1 fulfilment paragraph.

**L1's Goldbacher identity, and the seed/Manifest/log sites it reached.** `https://archive.org/metadata/CSEL57` returns `identifier: CSEL57`, `title: S. Augustini epistulae (CSEL 57)`, `date: 1911`, `uploader: tedjaniszewski@gmail.com`, and **no** `sponsor`, `scanningcenter`, `source` or `contributor` field at all. Its `_djvu.txt` is 1,574,207 characters, contains **zero** case-insensitive "google", and is identical to the vendored file's own body at both ends. All three hedges Round 24's L1 named are closed (`queue[12]`, the Manifest's G4 paragraph, the Decision Log's G4 Context paragraph at line 260) — the finding-number attributions on those three are L3 above; the fact each asserts is right.

**Round 19's C1 — spot-checked, undisturbed, a seventh time.** `prosper_chronica-minora-1-lat_mommsen1892.txt` line **42582** reads `EPITOMA CHEONICON`; line **45881** reads `EPITOMA DE CHRONICON,`, between the praefatio's last line at 45876 (`De reliquis libris quicquam addere supervacaneum est.`) and the chronicle's first entry at 45891 (`1 Adam cum e.sset annorum CCXXX, genuit Setli.`). Identical to Rounds 19, 20, 21, 22, 23 and 24. The declination stands on seven consistent checks.

**Bold-marker nesting, independently reproduced across all four documents, run-aware.** markdown-it-py 4.2.0 (`commonmark`), **440** `**`-bearing lines — Doc_02 **66**, Registry **200**, Manifest **38**, Decision Log **136**. That is the pass's own figure exactly, and the +2 over Round 24's 438 is accounted for: the Decision Log gained the two new `**Round N**` paragraphs and no other document changed a bold-bearing line count. Result: **zero** nested `<strong>` spans, **zero** unclosed spans, **zero** literal `**` surviving any render, **zero** `****`, and **zero** lines where CommonMark's delimiter pairing differs from run-aware sequential pairing. The class remains closed by construction, now for a fifth consecutive round.

**Both edited YAML files parse, and the fold-break class is closed in the direction the pass checked.** `yaml.safe_load` succeeds on `cic/texts/REGISTRY.yaml` (88 entries, every one with `filename`/`supplied_by`/`date_added`/`notes`) and on `worlds/_cross-world/download-queue-seed.yaml` (22 queue entries). Round 24's three named REGISTRY.yaml instances are gone and their README renderings are correct (`present-tense`, `archive.org/details/sanctiaugustiniv00possrich`, `Source_Acquisition_Manifest`), and the four pre-existing seed instances the pass swept up alongside them (`spuria/indices`, `letter-numbering`, `actually-verified`, `passio/formation-biography`) are gone too — each verified present at `cc489ab` and absent at `8c2a322`. (The mirror direction is C1 above.)

**Registry table integrity, recomputed row by row.** All 212 rows re-extracted by column position: numbers **1–212 complete, no gap, no duplicate**; **every row exactly 12 pipes / 11 columns**. The same three physical-order inversions (48→42, 193→60, 60→52) Rounds 20–24 found, all covered by the front-matter Disclosed-placement rule. The pass inserted and deleted no Registry lines, so the file is still 329 lines and every pre-existing line pointer into it still resolves — Registry line 295 is still the recall-test paragraph, line 325 the round-by-round accounting, and the Manifest's line 11, line 61 and line 87 all still hold superseding notes.

**The acquisition-state sweep, widened and re-run across every artifact.** An eighteen-pattern list (`stays open`, `remains open`, `remain(s)/still unacquired`, `awaiting`, `not yet located`, `acquisition candidate`, `if acquired`, `currently lacks`, `open request`, `to be acquired`, `not currently vendored`, `has not been located`, `not yet assigned`, `is not vendored`, `unvendored`, `not guessed`, `not independently confirmed`, `very likely`) run across all 212 Registry rows, all 88 `REGISTRY.yaml` entries, all 22 seed entries, the Manifest and Doc_02 returns **no live false claim**: every hit is either earlier-draft text quoted inside a correction note, the correctly-scoped CSEL 58 residue, the consultation-only boilerplate on in-copyright rows, or a superseded paragraph explicitly marked as historical record. G4's state — CSEL 58 alone open — is stated identically at Registry rows 61, 193, 195/196, Manifest G4 (three paragraphs), Doc_02 §9 item 1, `REGISTRY.yaml`'s CSEL 34 and CSEL 44 entries, `queue[9]`–`queue[12]` and `DOWNLOAD-QUEUE.md`.

**Census and comparator arithmetic, recomputed across every atlas file.** `latin-pastoral-congregational-christianity.yaml`: **99 entries, 97 distinct titles, `Counter({'tradition': 90, 'context': 9})`, 88 distinct titles inside the tradition set, `Counter({'assigned': 87, 'provisional': 12})`**; exactly two duplicate tradition titles (*The Enchiridion (On Faith, Hope, and Love)*, *The Passion of the Scillitan Martyrs*), so 90 − 2 = 88 reconciles. Comparators re-derived per measure: 99 raw against **68** (`post-apostolic-house-church.yaml`), 90 `tradition` against **59** (`post-apostolic-house-church.yaml` and `alexandria-catechetical.yaml`, tied). Every figure in Doc_02 §1's opening paragraph holds.

**Engine scripts, both re-run this session from `/home/user/CIC-Project`.** `python cic/engine/texts_registry.py` → **exit 0**, *"OK: every vendored file has a header-verified rights line …, an ENTRIES row, and no ENTRIES row points at a missing file"*; 88 vendored files, 23 non-English, `cic/texts/` at 211 MB (30% of the 700 MB planning trigger). `python cic/engine/corpus_map_merge.py --check` → **exit 0**, 528 works → 788 assignments across 56 Atlas entries, no error. Neither script validates prose in a `notes` field, so M1, M3 and L5 are invisible to both — the blind spot Rounds 23 and 24 named, still open by design.

**M1 (Round 24's), and the phrase's remaining live occurrences.** `lpc_Decision_Log.md` line 269 now reads *"archive.org site-navigation chrome cut — not 'Google Books chrome,' per the M2 correction above (corrected here, independent review Round 24's own M1…)"*. A repository-wide grep for "Google Books" across the four documents, all vendored files, both YAML artifacts and both generated files returns only correct uses: the Hartel file and row 191 (where `sponsor: Google` is confirmed), the Migne, Bruns and von Soden 1904 files (all three verified `…goog` items), the Morison file, and quoted earlier-draft text inside correction notes.

**M4 (Round 24's), the G1 and G4 "What remains open" paragraphs.** Line 226 now correctly records Pars III vendored as row 194 and the identifier confirmed; line 277 correctly records three of four G4 volumes vendored as rows 195–196 with CSEL 58 alone open. Both facts check out against the Manifest, rows 194/195/196 and `queue[10]`/`queue[11]`. (The two attribution errors inside line 277 are L4 above.)

**C1, C2 and C5 (Round 24's).** Row 191 now carries the per-row normalization disclosure, and it is accurate to the file: line 54 reads `(OPEEA SPVRIA. INDICES. PKAEFATIO)`. The Round 21 paragraph's "below" is now *"described earlier in this same paragraph's own 'Five LOW' clause above"* — verified: the Manifest's L2 fix is described in the Five LOW clause, the C4 item in the Four COSMETIC clause after it. `queue[12]`'s cross-reference now names its target and resolves (`queue[9]`, three entries up).

**The Decision Log's own Round 24 paragraph, checked against the Round 24 artifact.** Its counts (2/4/4/5), its "nine of the eleven findings the pass addressed," its H1/H2 and M1–M4 accounts, its L1–L4 and C1–C5 summaries, and its "six independent confirmations" for Round 19's C1 all match Round 24's own text. The escalation paragraph is correctly updated from "eight rounds" to **ten**, from "H1/M1/M2" to **H1/H2/M1–M4**, from "four" confirmations to **six**, and now names Round 24's M3 alongside Round 22's M1 as the second instance of an under-derived identity claim checked at source by the round that found it. (Its "years ago" is M4; its Round 23 paragraph's opening is L2; its C4 completeness claim is L1; its ordinal is C4.)

**Cross-references and directional language.** Every `rows? N` citation in Doc_02 resolves inside 1–212. Every `§N above` / `§N below` reference direction-checked programmatically against the section each sits in: **none fails**. The Decision Log's `Doc_02 revision:` heading occurs exactly once and Doc_02 §2's pointer quotes strings from it that are still present and unique. The seed's own relative pointers all resolve as written (`queue[6]`→`queue[5]`/`queue[7]`, `queue[9]`→`queue[10]`/`queue[11]`, `queue[14]`→`queue[13]`, `queue[16]`→`queue[14]`/`queue[15]`).

**The other lpc entries in `REGISTRY.yaml` and `download-queue-seed.yaml`, read in full.** Beyond H1's two, the remaining seventeen lpc `REGISTRY.yaml` entries check out against their Registry rows and file headers — the CSEL 33/40-1/40-2 and Bruns entries each record the copyright-trap items they excluded; Harnack's TU citation matches row 205; the Monceaux Tome I entry records the `histoirelittra00moncuoft` lead correction; the Codex Theodosianus entry states the Latin Library rights basis and edition gap exactly as row 88 does; `CSEL 58 remains open` in the CSEL 34 and CSEL 44 entries is correct. In the seed, `queue[5]`/`queue[13]` are correctly `superseded` rather than deleted, and every `downloaded` lpc entry names an identifier matching its Registry row.

**The disposition status lines, reported as observed and not assessed.** `Doc_02_Source_Ecology.md`'s status line and §10, and `Source_Registry.md`'s status line, still read "Fourteen independent adversarial review rounds" over "(Rounds 1–14: 6/2/1/1/0/0/0/0/0/0/0/0/0/0)" and still point to "`Doc02_Round1_Review.md` through `Doc02_Round14_Review.md`," while `Review-Artifacts/` now holds twenty-four `Doc02_Round*_Review.md` files before this one and both documents carry in-text attributions to Rounds 15 through 24. Reported here as observed, checkable state, on the same footing Rounds 16 through 24 reported it; not assessed, per CO-022's rule that the build thread applies its own disposition.

---

## CO-022 escalation-category assessment

**1. Representative identity, name, or title.** Untouched by the fix pass and by this round. **Clear.**

**2. Portfolio-level or cross-world strategic decisions.** L3 and L5 land on shared artifacts other worlds' build threads read — `download-queue-seed.yaml` and `cic/corpus-map/tertullian-s-voice.yaml`. In each case the finding is that an lpc-authored note about lpc's own file misstates an attribution or a cross-reference; nothing here decides anything for another world, no other world's assignments were examined or altered, and both corrections are lpc's to make on its own record (L5's text lives in lpc's own `_staging/` file). M1–M4, C1–C5 and the remaining LOW findings concern this world's own documents, intakes and vendored files. **Not an escalation.**

**3. Governance or methodology decisions.** Nothing here proposes a change to `Source_Registry_Template.md`, `cic/texts/INTAKE.md`, CO-022 or any governing document. M1 and M2 are findings that a fix's scope stopped short of a site the prior review named; M3 is a finding that a header misdescribes the file it heads; M4, L1–L4 and C4 are findings that newly-written record-keeping prose misstates dates, counts, attributions or completeness; L5, C1, C2, C3 and C5 are conformance findings against conventions already in force (the corpus map's own source-file join, the fold-break sweep the pass itself declared, the Registry's own OCR-disclosure convention, the seed's own pointer discipline, Doc_02 §3's own dating convention). All are conformance findings against rules already in force. **Not an escalation.**

**4. Unresolved tensions the pipeline cannot close / two reviews disagreeing.** This round disagrees with no prior round on a point of fact. It agrees with Rounds 20–24 against Round 19 on C1, reached by reopening the file at the lines named. It departs from Round 24 on one calibration question only — rating the surviving usage-notice claim MEDIUM where Round 24 rated the same claim LOW — and states its reason in the finding (the claim is now stated two opposite ways inside one commit, which it was not when Round 24 found it). The three places this round could have produced an unresolved tension are M1, M3 and L5, and all three are closed rather than left open: M1 by fetching both source items and confirming their own text carries no notice and matches the vendored files at both ends; M3 by reading the Pars III file's two title pages and all eight of its component boundaries directly; L5 by counting `Perpetua` occurrences in `anf03` and `anf09` and reading the atlas file's own two entries. None requires the project lead. **Not an escalation.**

**No escalation category applies.**

---

## Note on disposition — deliberately not assessed

Whether and how the status lines described above should change, and what disposition follows from this round's counts, is **not assessed here**, per the task's own scoping and CO-022's rule that the build thread applies its own disposition.

**Observed trend, stated as raw counts only and not otherwise characterized.** Across the eleven rounds against this 2026-09-08 revision: Round 15 — 4/6/5/2 (17); Round 16 — 4/5/6/3 (18); Round 17 — 0/3/5/4 (12); Round 18 — 0/4/3/3 (10); Round 19 — 0/2/4/3 (9); Round 20 — 1/4/5/5 (15); Round 21 — 0/4/5/4 (13); Round 22 — 1/2/3/4 (10); Round 23 — 1/3/4/4 (12); Round 24 — 2/4/4/5 (15); Round 25 — 0/4/5/5 (14).

Four observations bear on reading this round's counts, stated without weighing them.

First: **both HIGH findings are genuinely and completely closed, and the two generated derivatives are now provably in sync.** `cic/texts/README.md` and `worlds/_cross-world/DOWNLOAD-QUEUE.md` were each regenerated to a scratch copy this round and byte-compared against the committed file: no diff in either, with the tree left clean. The derived-artifact failure Round 24 named third among its observations does not recur.

Second: **the recurrence has moved from the sites a review *quotes* to the sites a review *lists*.** Round 24's M3 said the hedge stands at the G1 entry "twice"; one was fixed. Round 24's L3 said the residue stands "in both files' `REGISTRY.yaml`/README entries"; those were fixed and the two Registry rows describing the same files were not. Round 24's C4 gave five file-and-line coordinates; four were fixed and the record says five. In all three cases the unfixed site is named in the finding but not set out in a block quotation.

Third: **the fix pass's own replacement prose is again the largest single source of new findings** — M3, M4, L2, L3, L4 and C4 are all defects in text this pass wrote while closing something else, which is the shape this log has tracked under its own name since 2026-09-01 and which Rounds 18 through 24 each found in turn.

Fourth: **the one finding neither of those describes is the first this sequence has produced from a corpus-map staging file** (L5) — an artifact written by lpc's own 2026-09-08 vendoring, feeding a shared atlas file for a different world, that no round in twenty-four has opened. It is the same widening that produced Round 23's H1 at `REGISTRY.yaml` and Round 24's H2 at `DOWNLOAD-QUEUE.md`, one artifact further out.

**Verdict restated: SUBSTANTIAL REVISION REQUIRED — 0 HIGH · 4 MEDIUM · 5 LOW · 5 COSMETIC.**
