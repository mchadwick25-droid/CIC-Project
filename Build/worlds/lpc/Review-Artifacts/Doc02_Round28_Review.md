# Doc_02 — Source Ecology and Source Registry: Latin Pastoral-Congregational Christianity
## Round 28 Independent Adversarial Review — scoped to the Round 28 revision of `Source_Registry.md` rows 65 and 44, its propagation into `Doc_02_Source_Ecology.md` §5, the REOPENED status lines in both documents, and the two sibling-branch vendored files the revision's new sourcing conclusions rest on

**Documents reviewed (committed state — `git status --porcelain` clean, 0 lines, at `0124a9f`, "lpc: renumber this revision Round 26 -> Round 28; disclose review-count conflict", 2026-09-09 02:24:18 UTC, on branch `lpc-round26-rows-65-44`; parent `37e3ee5`, "lpc Round 26 revision: correct Registry rows 65 and 44 sourcing conclusions", 2026-09-09 02:19:37 UTC; grandparent `1b91ef2`, the `lpc-own` / `claude/record-native-world-build-v2-yq11wl` head):**
- `World-Builds/Latin-Pastoral-Congregational-Christianity/Source_Registry.md` (329 lines, 36,264 words, 212 rows) — the front-matter Status line read in full; rows 44 and 65 read cell by cell against their own text at `1b91ef2` (`git show 1b91ef2:… | awk -F'|'`); all 212 rows re-parsed by column position for pipe count, row-number sequence and physical order; rows 12, 14, 37, 49, 50, 51, 53, 58, 59, 64, 65, 67, 88, 111, 164 read in full for cross-reference resolution and for the sibling-defect sweep at L5
- `Doc_02_Source_Ecology.md` (158 lines, 12,779 words) — the Status line (line 3) and §5's *Codex Theodosianus* bullet (line 97) read against their own text at `1b91ef2`; §1, §2 (line 44, the "post-411 Conference" phrase), §6, §9 and §10 read in full for dependency and contradiction
- `Source_Acquisition_Manifest.md` (81 lines, 5,289 words) — §1's G1–G9 entries, §2, §3's membership rule (line 69), the network-access paragraph and the sourcelibrary.org source-integrity warning (line 59) read in full
- `lpc_Decision_Log.md` (378 lines, 24,693 words) — all entry headings enumerated; the 2026-09-02 *Codex Theodosianus* entries (lines 93–111), the 2026-09-03 corpus-map migration entry (lines 189–193), the 2026-09-02 joint-disposition entry (line 121) and the three final 2026-09-08 entries (lines 318–378, including the Round 26 paragraph at line 362) read clause by clause
- `Review-Artifacts/Doc02_Round25_Review.md` (282 lines), `Doc02_Round26_Review.md` (188 lines) and `Doc02_Round27_Review.md` (251 lines) — read for verdicts, finding headings, and specifically for whether the matters this revision refers to Round 28 were already on the record; the full Review-Artifacts directory listing enumerated and cross-checked against `git ls-tree HEAD`
- **The two vendored files the revision's conclusions rest on, extracted from branch `don-lpc` (= `donatism-lpc-integration`) and read directly, not taken from any account of them:** `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt` (144,732 lines / 5,101,584 bytes) — provenance header read in full (lines 1–140); the *Gesta* span located by its own running heads; every one of the seven act numbers the revision names checked individually at its own line; an independent OCR-tolerant scan of the whole *Gesta* span for line-initial numbered acts naming Augustine; the `ACTORES VII` disputant table read in full at its own heading. `cic/texts/theodosianus-16_mommsen-meyer1905.txt` (94,020 lines / 3,545,940 bytes) — provenance header read in full; both title pages, Google's retained disclaimer page, *CTh* XVI.5.52 and *CTh* XVI.5.21 read directly in the body
- `World-Builds/Donatism/don_Decision_Log.md` at `don-lpc` (590 lines) — the 2026-09-01 "G3 acquisition attempts, five tried, none vendored" entry, the 2026-09-01 Boyd substitute entry, and the 2026-09-07 "G3 and G6 fully discharged" and *Gesta* entries read in full; `World-Builds/Donatism/Source_Registry.md` rows 14, 16 and 55 read in full
- `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml` **on this branch** — "The Correction of the Donatists" (= Letter 185) located by its own `div2`, Chapter 7 §25 extracted at `div3 n="7"` and read in full, for the fine the revision's row 44 now identifies
- `cic/corpus-map/donatism.yaml` (the *Codex Theodosianus* entry, lines 197–213), `cic/corpus-map/latin-pastoral-congregational-christianity.yaml` (the parallel entry, lines 1130–1144), `cic/texts/REGISTRY.yaml` (the `codex-theodosianus_latinlibrary.txt` entry, lines 955–967), `world-build-docs/_cross-world/download-queue-seed.yaml` and `DOWNLOAD-QUEUE.md` — all swept for live statements the two corrections falsify
- `cic_build_cycle_co022.skill`, `co023`, `co024` and `co024b` — all four unzipped and their `SKILL.md` texts diffed against one another; `co024b` is the widest (it alone carries the "Cross-document fact consistency" section and the coach-correction exception) and is read here as current, with CO-022's own definitions applied as the brief directs
- `git ls-tree main cic/texts/`, `git merge-base --is-ancestor don-lpc main`, `git merge-base --is-ancestor don-lpc HEAD`, and `ls cic/texts/` on this branch, to establish where the two vendored files actually exist

**Review date:** 2026-09-09
**Reviewer:** independent adversarial review thread. Did not draft the Round 28 revision, did not write the renumbering commit, did not perform any of the vendoring on either branch, and did not write Rounds 1–27.

**Two scope notes, stated plainly before anything else.**

*First — this artifact is `Doc02_Round28_Review.md`, not `Doc02_Round26_Review.md`.* This review was commissioned as "Round 26." `Doc02_Round26_Review.md` and `Doc02_Round27_Review.md` already exist on this branch as committed review artifacts of the 2026-09-08 banner-stripping rewrites, and writing to the Round 26 path would have destroyed one — against the discipline's own "review rounds exist as files, not claims." The collision was present in the revision as committed at `37e3ee5`, which numbered itself Round 26 in both edited documents; the build thread corrected it at `0124a9f` while this review was in progress, and the pre-existing `Doc02_Round26_Review.md` is confirmed byte-identical to its state at `1b91ef2` (md5 `c0bb75b…`, both). The collision is therefore recorded here as resolved in flight rather than as a finding — but the renumbering pass left one site behind (C1), and the count disclosure it added is itself the subject of L6 and L7.

*Second — what this round does and does not re-run.* This is a narrow, two-row revision. This round does not re-run the recall test, the PRESS question, the corpus-map census, or a whole-document content sweep of Doc_02. Four briefs instead. **First:** treat every factual claim the revision introduces as a claim to re-derive from the primary artifact — the two vendored files, the sibling build's own records, and the NPNF text already on this branch — rather than from the revision's account of them, and specifically test the quoted strings character by character rather than accept them as quotations. **Second:** test the revision's own central negative claim, that nothing depends on these corrections, by sweeping every file on this branch that names row 44, row 65, the *Codex Theodosianus* or the 411 Conference, including the machine-readable artifacts. **Third:** check the two rewritten Status lines against the sections they point at and against the review record they summarize. **Fourth:** adjudicate the review-round count question the revision refers to this reviewer, on evidence rather than on either document's own say-so. Nothing was carried forward from the commit messages, from the revision's own disclosures, or from Rounds 1–27.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 1 HIGH · 6 MEDIUM · 7 LOW · 4 COSMETIC.**

**Both corrections are right to have been made, and the harder half of each is correct.** Row 65's core diagnosis holds exactly: the prior row did conflate Lancel's in-copyright Sources Chrétiennes edition with the *Gesta* themselves, and a public-domain Migne *Patrologia Latina* XI printing of the *Gesta Collationis Carthaginiensis* was vendored by the sibling Donatism build on 2026-09-07, on a rights basis the file's own provenance header states and which this corpus already accepts for `monumenta-vetera-donatistarum_migne-pl8.txt`. Augustine really is a named disputant in that file, really does speak in numbered acts, and Possidius of Calama really does appear — all three re-derived here directly against the file. Row 44's rights reasoning is likewise sound: `theodosianus-16_mommsen-meyer1905.txt` is genuinely the Mommsen–Meyer 1905 Weidmann *Voluminis I Pars Posterior* (both title pages read: `EDIDERVNT TH. MOMMSEN et PAVLVS M. MEYER … VOLVMINIS I PARS POSTERIOR … BEROLINI APVD WEIDMANNOS MDCCCCV`), Google's public-domain disclaimer page really is retained unstripped in the body, *CTh* XVI.5.52 really is headed `(412 lan. 30)` and really does read `circumcelliones argenti pondo decem` verbatim, and the sibling build's Decision Log really does record G3 **fully discharged on 2026-09-07**. Marking both documents REOPENED and not disposed is the correct CO-022 handling: both edits change sourcing conclusions, which is CO-022's own definition of substantial.

**Where the HIGH is: in the one new claim the revision made that its own primary sources contradict.** Row 44 and Doc_02 §5 now identify *CTh* XVI.5.52's circumcellion clause as "the ten-pounds-of-silver fine this row exists to underwrite for Augustine's own Letter 185 §25." Letter 185 §25 — read this round in the NPNF file already vendored on this branch, and already independently verified by this build across Doc_01's Rounds 6–9 per row 12's own Verification Note — cites no such thing. It cites "the law which Theodosius, of pious memory, enacted generally against heretics of all kinds, to the effect that any heretical bishop or clergyman, being found in any place, should be fined **ten pounds of gold**." That is *CTh* XVI, 5, 21 (392 Iun. 15), which is present in the same vendored file, twenty-eight laws earlier, reading `denis libris auri viritim`. The revision has taken a fact that discharges the *Donatism* build's own standing 16.5.52 citation gap and re-labelled it as discharging *this* world's Letter-185 need — a different law, a different emperor, a different metal, and a date eleven years after the events §25 narrates. This is the "borrowing from the wrong source tradition" shape the governing skill names in its own opening paragraph, arriving inside a correction pass.

**Where the MEDIUMs are: in everything outside the two files the revision opened.** The revision's sweep stopped at `Source_Registry.md` and `Doc_02_Source_Ecology.md`. Three live artifacts on **this** branch still assert what row 44 just corrected, one of them a machine-readable corpus-map file that cites "Source_Registry.md row 44 (lpc's own Registry)" by name as its ground (M2). The Manifest — the document whose entire job is routing acquisition decisions to the project lead — was not touched, and its §3 membership rule now classifies row 65 as needing no acquisition decision in the same breath the row calls the newly-vendorable *Gesta* "a real opportunity for a future Doc_04" (M3). The revision's account of the sibling build's five failed attempts flattens five into one and erases the only one carrying a standing cross-world security caution — a caution this world's own Manifest carries at line 59 (M1). The Status line the revision rewrote says "see §10"; §10 says the opposite of what the Status line says, and neither Round 27's twelve unfixed findings nor its verdict against these same two documents is disclosed anywhere (M5). No `lpc_Decision_Log.md` entry was written for a substantial revision, in a build whose log records every prior one (M6). And the Registry Status line's disclosure claims the discrepancy was not "silently overwritten" in the same edit that deleted one of its two conflicting data points (M4).

**And the quotation discipline slipped in the one place this document set has been strictest.** Neither of row 65's two quoted strings occurs in the file it quotes. "Augustinus Hipporegiensis" occurs zero times; the volume reads `Augustinus Uipporegiensis`. "Augustinus episcopus Ecclesiae catholicae dixit," offered as "the recorded form," occurs zero times; every instance is OCR-garbled (`Eccleshv catholicai dixil`, `Ecclesia; catholicm dixit`, `Ecclesios caUiolicai dixit`), and the act the revision numbers 158 is truncated at `158. Augustinus episcop` with no formula at all. The file's own provenance header warns, in terms, that "any specific quotation drawn from this file needs careful visual cross-check against its own surrounding context — more so than most other files in this corpus — before being relied on for a verbatim claim" (L1).

---

## HIGH

### H1 — Row 44 and Doc_02 §5 identify *CTh* XVI.5.52 as the statute behind the fine Augustine's Letter 185 §25 cites. §25 cites a ten-pounds-of-**gold** law of Theodosius I — *CTh* XVI.5.21 — which is in the same vendored file. The row's central new claim about its own Licensed-For is wrong.

**Where.** `Source_Registry.md` line 58 (row 44), Verification Note, the sentence beginning "**Directly material to this row's own Licensed-For:**":

> the sibling build independently located and read *CTh* XVI.5.52 in full in that file (headed "412 Ian. 30"), confirming it carries "circumcelliones argenti pondo decem" verbatim — **the ten-pounds-of-silver fine this row exists to underwrite for Augustine's own Letter 185 §25 (row 12).**

**What row 44's Licensed-For actually says this row is for** (unchanged by the revision, same line, column 7):

> The underlying imperial statute behind the Theodosian-law fine Augustine's own Letter 185 §25 cites (row 12)

**What Letter 185 §25 actually cites, re-derived this round from the file already on this branch.** `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml`, `div2 id="v.vi"` ("The Correction of the Donatists" = Letter 185), `div3 type="Chapter" n="7"`, paragraph 25 (file lines 19624–19628):

> **Chapter 7.—25.** However, before those laws were sent into Africa by which men are compelled to come in to the sacred Supper … this they thought might in some measure be effected, **if they would take the law which Theodosius, of pious memory, enacted generally against heretics of all kinds, to the effect that any heretical bishop or clergyman, being found in any place, should be fined ten pounds of gold**, and confirm it in more express terms against the Donatists, who denied that they were heretics …

The same paragraph closes "and envoys were sent to the court of the Count," with NPNF's own endnote 2521 dating the council "That of Carthage, held June 26 (more correctly, probably June 15th or 16th), **401**" — the same 401 footnote row 12's own Licensed-For already names.

**The law §25 describes, located directly in the file row 44 now points at.** `theodosianus-16_mommsen-meyer1905.txt` line 86855 and following:

> **XVI, 5, 21 (392 lun. 15).** IDBM AAA. tatiano p(raefecto) p(raetori)o. Id haereticis erroribus quoscumque constiterit vel ordinasse clericos vel suscepisse officium clericorum, **denis libris auri viritim** multandos esse censemus …

Theodosius I; heretical clergy generally; ten pounds of gold each. That is §25's law, exactly as Augustine describes it.

**What XVI.5.52 is instead.** Same file, line 87881 and its heading at 87862: `XVI, 5, 52 (412 lan. 30>` — Honorius and Theodosius II to Seleucus PPO, a graduated fine schedule *for Donatists specifically*, `inl(ustres) … auri pondo quinquaginta … decuriones auri pondo quinque, negotiatores auri pondo quinque, plebei auri pondo quinque, circumcelliones argenti pondo decem`. The sibling build's own Registry row 16 states the distinction explicitly: "with Circumcellions assessed a **silver (not gold)** fine unlike every other listed rank."

**Why this is HIGH and not MEDIUM.** Three things stack. (a) It is a **new** claim, introduced by this revision, not inherited staleness. (b) It is stated at the highest confidence register the row uses — "**Directly material to this row's own Licensed-For**" — and is the sentence that carries the whole practical payload of the row-44 correction, the reason a reader would go looking for the file. (c) It is refutable against a file **already vendored on this branch**, whose relevant chapter row 12's own Verification Note records as "directly re-verified at source across Doc_01's Rounds 6–9, including … **the Theodosian fine**." The Registry is the document a future Doc_03 and Doc_04 draw from; a reader who follows this row to XVI.5.52 expecting Augustine's fine will find a different law and, if they do not check, will propagate the misidentification into a document that quotes it.

**What makes it worse, not better, that the correct law is in the same file.** The revision had the vendored text available on `don-lpc` and read the file's header. `denis libris auri` is one grep away. The identification was not unavailable; it was not attempted.

**Fix shape.** Either drop the equation and let XVI.5.52 stand on its own footing (it is genuinely the Donatist-fine law and genuinely material to this world's Augustine-phase state-coercion material), or replace it with XVI.5.21 and say so, with the 392/401/412 chronology stated. Do not leave a row asserting that a 412 silver fine is the fine a 401 petition described.

---

## MEDIUM

### M1 — "the five failed attempts had all returned Mommsen's *Prolegomena*" is false. The second attempt returned something else entirely — the one failure carrying a standing cross-world security caution this world's own Manifest already records.

**Where.** Two sites, both introduced by this revision:
- `Source_Registry.md` line 58 (row 44): "**the five failed attempts had all returned Mommsen's *Prolegomena in Theodosianum* (Vol. I Pars Prior), a different volume**"
- `Doc_02_Source_Ecology.md` line 97 (§5): "**the failed attempts had returned a different volume, Mommsen's *Prolegomena***"

**What `don_Decision_Log.md`'s own entry says** (the record row 44 cites), heading "2026-09-01 — G3 acquisition attempts, five tried, none vendored":
- **Attempt 1** — the Prolegomena, item `theodosianilibri02code`.
- **Attempt 2 — "rejected on source-integrity grounds":** a DOCX from "sourcelibrary.org," found to be "an English paraphrase/interpretive 'translation' with inline glosses, not a transcription of the Latin critical edition; licensed CC BY-SA 4.0 by the site itself, not public domain; and carrying a long run of invisible zero-width Unicode characters embedded after nearly every paragraph throughout the entire file." Not the Prolegomena. Not Mommsen. Not even Latin.
- **Attempts 3–5** — "same wrong volume repeated," the Prolegomena again.

Four of five, not five of five.

**The sibling build's own Registry row 16 — the row row 44 names as its Discovery source — gets this right and the revision drops the limb.** Row 16 reads: "after five prior acquisition attempts … all resolved to the same wrong volume (the Prolegomena, not Book 16's own text) **or were rejected on source-integrity grounds**."

**Why this is MEDIUM rather than LOW.** The erased attempt is the one with a live, standing consequence. `don_Decision_Log.md` states it as a **"Standing caution for this and future worlds' acquisitions: sourcelibrary.org (and any similarly self-described 'for AI systems' text-processing intermediary) should not be used as a source for vendored text."** This world's own `Source_Acquisition_Manifest.md` line 59 carries that caution forward by name and grounds it in exactly this attempt. A row that now tells its reader all five failures were the same catalogue error, in the document of record, quietly removes the reason that caution exists. And the flattening was not required by anything — the correction is fully available in the two-limb form the sibling build itself uses.

### M2 — No sweep was run outside the two edited files. Three live artifacts on **this** branch still state what row 44 corrects; one of them is a machine-readable corpus-map file that cites row 44 by name as its ground, and it sits outside this build thread's editing authority with no flag raised.

**Where, all three verified live at `0124a9f`:**

**(a) `cic/corpus-map/donatism.yaml`, lines 197–213** — the *Codex Theodosianus* staging entry, `confidence: needs-ruling`:

> note: 'Not a claim this staging entry is positioned to argue well — flagged because **Source_Registry.md row 44 (lpc's own Registry) records that the sibling Donatism build's own Manifest carried a live G3 request for exactly this edition (Mommsen-Meyer, referenced there but not acquired after five attempts; that build settled for a substitute, Boyd's 1905 translation of the ecclesiastical edicts)**. …'

Every clause after "records that" is now false, and the entry's `needs-ruling` confidence rests on it.

**(b) `lpc_Decision_Log.md` line 99**, the 2026-09-02 *Codex Theodosianus* entry's "**Consequence**" paragraph: "Registry row 44 is corrected to name this specific edition and identifier …, state its licence plainly, and record it as Native, Confidence B, **not a vendoring candidate**." This log is append-only by its own convention, so the dated entry should stand — but nothing later in the log supersedes it, because the revision wrote no log entry at all (M6). The log's only statement about row 44's vendoring conclusion is now the withdrawn one.

**(c) `lpc_Decision_Log.md` line 193**, the 2026-09-03 corpus-map migration entry: "flagged, not asserted, because **Registry row 44 already records that build's own prior G3 request for this exact edition (five failed acquisition attempts, settled for a substitute)**" — the source of (a)'s wording, same defect.

**Why this is MEDIUM.** (a) is not prose a reader might contextualize; it is the note field a generated census and a future world-build read as state, and it names lpc's row 44 as its authority — so correcting row 44 without touching it leaves the two in direct contradiction, with the stale one machine-readable. Editing another world's corpus-map bucket is outside this build thread's authority, which is exactly why **Round 25's own precedent applies**: that pass "flagged, without fixing, four further instances found in other worlds' own corpus-map files, outside this build thread's own editing authority (both recorded in `lpc_Decision_Log.md`)," and Round 26's L4 restored that disclosure to Doc_02 §10 when a later pass dropped it. The remedy here was available, cheap, and already precedented. Nothing was flagged, and the revision discloses no sweep of any kind.

**This is also the exact shape this document set's own "pattern worth naming" tracks** — a fix whose scope stops at the file it opened — found at Rounds 20, 21, 23, 24, 25, 26 and 27 in turn. It is the seventh consecutive occurrence.

### M3 — `Source_Acquisition_Manifest.md` was not touched, and its §3 membership rule now mis-routes row 65: the Manifest classifies the *Gesta* as needing no acquisition decision from the project lead, in the same breath row 65 calls it a live vendorable opportunity.

**The rule, `Source_Acquisition_Manifest.md` line 69:**

> **every Native, Confidence-C-or-below Registry row whose Verification Note says "in copyright" and "consultation-only" or "not a vendoring candidate" is in this category** — cited by this build as a reference, **never committed to `cic/texts/`, needing no acquisition decision from the project lead**. Checking that rule against the table, not a fixed list here, is authoritative.

**Row 65 after the revision** is still Native, still Confidence C, and its Verification Note still reads "Lancel's own Sources Chrétiennes edition is **in copyright** and remains **consultation-only**." So by the Manifest's own authoritative test, row 65 remains in §3 — the never-vendored, no-decision-needed category.

**What the same row now also says:** a public-domain Migne printing of the *Gesta* is vendored on a sibling branch; it is "**Not present on this world's own branch, so not usable directly by this document without its own vendoring step**"; and "**What it opens:** a live, recorded primary route to Augustine's own voice at the 411 Conference … named here as a real opportunity for a future Doc_04."

A source that requires "its own vendoring step" on this branch and is named as a real opportunity **is** an acquisition decision — the precise thing the Manifest exists to route to the project lead, and the precise thing §3 membership declares unnecessary. The two documents now give opposite answers to "does the project lead need to decide anything about the 411 Conference acts?"

**The Manifest has a worked precedent for exactly this move and the revision did not apply it.** §3 line 69 ends: "**Two works were moved out of this category and into §1 as real, public-domain acquisition candidates once their own rights position was resolved rather than assumed: Monceaux's *Histoire littéraire* vols. I–III (G5) and Goldbacher's Augustine *Epistulae* (G4).**" That is the same transition row 65 has just undergone, already documented, one section away.

**Rated MEDIUM** on the same footing Round 26 rated its own M2 and Round 27 its M3 — a companion document left asserting the opposite of the document that was edited, on a rule the edited document's own change moves it across.

### M4 — The Registry Status line says the discrepancy was "deliberately not repaired" and "flagged … rather than silently overwritten," in the same edit that deleted the 2026-09-02 disposition date from the line's first clause.

**What line 3's first clause said at `1b91ef2`:**

> **Status:** **Approved to proceed** (self-disposed by the build thread together with `Doc_02_Source_Ecology.md`, **2026-09-02**; see that document's own §10 for the full disposition entry).

**What it says now:**

> The prior disposition — **Approved to proceed**, self-disposed together with `Doc_02_Source_Ecology.md`; see that document's own §10 — stood on the pre-Round-26 text and does not carry over.

**And what the revision's own disclosure, in the same line, claims about that:**

> **A pre-existing discrepancy in this line, observed at Round 28 and deliberately not repaired here:** **this line dated the joint disposition 2026-09-02** and reported "Fourteen independent adversarial review rounds" … **Flagged for Round 28 rather than silently overwritten.**

**Re-derived by count.** `2026-09-02` occurs on old line 3 exactly once (in the deleted first clause) and on new line 3 exactly once (inside the disclosure's own past-tense self-description). The line's independent assertion of the date is gone. A reader who takes the disclosure at its word and looks for the 2026-09-02 date the line is said to state will not find one.

**Why this is MEDIUM.** It is not a stale sentence; it is a false description of the edit's own scope, written by the edit, in a Status line — and Status lines are precisely where this document set's discipline says "a status line inside the document is not evidence of anything on its own." Half the discrepancy was repaired and reported as unrepaired. Either repair it and say so, or restore the date and leave the flag standing; the current text does neither cleanly.

### M5 — Both documents are reopened without disclosing that Round 27 returned SUBSTANTIAL REVISION REQUIRED against these same two documents and that none of its twelve findings is fixed or logged — and Doc_02 §10, which the new Status line points the reader to, still asserts the superseded disposition and calls Round 25 "the most recent."

**Three live contradictions, all inside `Doc_02_Source_Ecology.md`:**

1. **Line 3 vs. §10 on whether the document is disposed.** Line 3: "**REOPENED** — … **Not currently disposed.** … No disposition will be self-applied on the strength of this revision's own author judging it sound; **see §10**." §10, unedited by this revision: "This document, `Source_Registry.md`, and `Source_Acquisition_Manifest.md` **are self-disposed by the build thread to Approved to proceed, 2026-09-08**, for the text as revised that day." §10 contains no mention of Round 28, of the reopening, or of anything the sentence pointing at it promises. The pointer resolves to the opposite claim.
2. **§10 on which round is last.** "**Round 25, the most recent**, found 0 HIGH, 4 MEDIUM, 5 LOW, 5 COSMETIC." Rounds 26 and 27 have both run and both sit in `Review-Artifacts/`.
3. **§10's disposition rests on a review record that has since moved.** §10 grounds the 2026-09-08 disposition on the project lead's direct instruction to close the cycle after Round 25. Two further rounds ran after that instruction, both returning **SUBSTANTIAL REVISION REQUIRED**: Round 26 (0 HIGH, 2 MEDIUM, 6 LOW, 4 COSMETIC — fixed, per `lpc_Decision_Log.md` line 362) and **Round 27 (0 HIGH, 3 MEDIUM, 5 LOW, 4 COSMETIC — not fixed, and not recorded in `lpc_Decision_Log.md` at all)**. The log's final entry ends by commissioning Round 27 and saying its "findings are to be shown before any fix is applied." Nothing after that exists.

**Why this belongs to this round rather than the last one.** Items 2 and 3 are pre-existing. **Item 1 is this revision's own**: it wrote a Status line that asserts a state §10 contradicts and then cited §10 as the authority for it. And the revision's scoping decision — reopen for rows 65 and 44 — was made on top of a document set carrying **twelve known, unfixed findings from Round 27**, including M2 and M3 against `Source_Registry.md`'s Status line, the very line this revision rewrote. Round 27's M3 concerns the first clause of Registry line 3; this revision rewrote that clause without citing, fixing, or acknowledging the finding. A reviewer of this revision is being asked to clear text that a review artifact in the same folder has already found defective at the same site.

**Fix shape.** §10 must be brought into line with the Status line (a reopening paragraph, and "most recent" corrected), and the revision must state where Round 27's twelve findings stand — fixed, deferred, or declined — rather than leaving the reader to discover from the artifact folder that the last completed round found the documents wanting.

### M6 — No `lpc_Decision_Log.md` entry was written for a substantial revision, in a build whose log records every prior one.

**What the log contains.** Twenty-six dated entries, including entries for changes markedly smaller than this one: "Sixth post-disposition Doc_01 edit (dropping the running count)," "First three post-disposition `Source_Registry.md` edits: resolving self-flagged bibliographic uncertainty on rows 31, 32, 33 via WebSearch," and a full entry for each of the two banner-stripping passes. The final entry is dated 2026-09-08 and ends by commissioning Round 27.

**What this revision added to it.** Nothing. `git show 37e3ee5 --stat` and `git show 0124a9f --stat` each touch exactly two files, neither of them the log.

**Why it matters here specifically, beyond bookkeeping.** Both corrections rest entirely on records held on **another branch** (`don_Decision_Log.md`, the Donatism Registry, and two vendored files not present on this one). The Registry rows now assert those facts; nothing on this branch records who checked them, when, against what, or that the check was made at all. `Source_Registry.md`'s own Status line states the convention: findings are "documented in `Review-Artifacts/` and, where a finding was itself wrong or two reviews disagreed with each other, in `lpc_Decision_Log.md`." A sourcing conclusion reversed on cross-branch evidence is exactly the case the log exists for. It is also where M2's corpus-map flag and M5's Round-27 status belong.

---

## LOW

### L1 — Neither of row 65's two quoted strings occurs in the file it quotes. Both are silent OCR normalizations presented as quotations, against that file's own explicit warning.

**Claim (a).** Row 65: "listed as **\"Augustinus Hipporegiensis\"** among the seven Catholic disputants."
**File.** `grep -c "Hipporegiensis"` → **0**. Whitespace-normalized `"Augustinus Hipporegiensis"` → **0**. What the volume actually prints, at line 113083 under the heading `NOMLAA ET SEDES / EPISCOPORUM XVIII UTRIUSQUE PARTIS QUI ELECTI SUNT AD COLLATIONEM IIABLNDAM` → `ACTORES VII. / EX PARTE CATHOLICORUM`:

> `Augustinus  Uipporegiensis.`

Initial `U`, not `H` — the standard `H`/`U` substitution this scan makes throughout.

**Claim (b).** Row 65: "speaks in at least seven numbered acts … **in the recorded form \"Augustinus episcopus Ecclesiae catholicae dixit.\"**"
**File.** Whitespace-normalized, case-insensitive, that exact string occurs **0** times. Every actual instance is garbled, and differently each time: `50. Augustinus episcopus Eccleshv catholicai dixil.` · `53. Augustinus episcopus Ecclesia; catholicm dixit.` · `160. Augustinus episcopus Ecclesios caUiolicai dixit.` · `187. Augustinus episcopus Ecclesiw calhoticw dixit.` · `201. Augustinus episcopus Ecclesice calliolicw dixit.` · `272. Augustinus episcoptts Ecclesiaj cailiolicoe dixit.` And the act the row numbers 158, at line 121763, carries **no formula at all** — it reads, in full, `158. Augustinus episcop` before the line breaks off into the mandate text.

**Why this is a finding and not pedantry.** The file's own provenance header, which the revision read (it quotes that header's rights basis), states: "Raw, uncorrected 19th-century Migne scan OCR, **notably poor in this particular scan** … **Any specific quotation drawn from this file needs careful visual cross-check against its own surrounding context — more so than most other files in this corpus — before being relied on for a verbatim claim.**" Presenting a normalized reading inside quotation marks, in a row whose whole point is that the content was "**independently verified this session, directly against that file**," is the one thing that header asks not to be done. The underlying substance is correct and is confirmed here; the presentation is not.

**Fix shape.** Either mark them as normalized (`"Augustinus [H]ipporegiensis"`, "the recorded form, normalized from this scan's OCR, is *Augustinus episcopus Ecclesiae catholicae dixit*") or quote what the file prints.

### L2 — "at least seven" understates by half. An OCR-tolerant scan of the same span returns fourteen numbered acts, and act 158 is the weakest of the seven the row names.

**The row's list:** 50, 53, 158, 160, 187, 201, 272 — "Seven is a floor, not a count: the scan's OCR garbles the speech formula heavily, so a stricter search returns fewer and a looser one may return more."

**Independently re-derived this round.** A single line-initial pattern over the *Gesta* span (file lines 112,700–131,400), tolerating the scan's ordinary `u`/`v`, `s`/`l`, `i`/`l` substitutions, returns **fourteen** numbered acts in which Augustine speaks:

> **50, 53, 98, 158, 160, 162, 187, 189, 201, 206, 257, 265, 267, 272**

with, e.g., `98. Auguslinns episcopus Kcciesioz calhoticw dixil.` (line 127457), `162. Auguslinus episcopus Ecclesiw catholica? dixit.` (128449), `206. Augusiinus episcoput Errlrtiaz catholini' dixit.` (129059), `265. Augutlimu episcoput Eccletim catholkw dixtt.` (130239). All fourteen are line-initial, inside the *Gesta* running heads (`GESTA COLLATIONIS CARTHAGINENSIS` at 121906, 127700, 128343, 130382), and all still a floor — mid-line instances and heavier garblings are not counted.

**Verdict on the hedge, since the brief asks directly.** The hedge is **honest in direction and inadequate in magnitude**. It is not an overclaim: all seven named acts are real, each was checked individually here, and each is genuinely Augustine speaking. But "seven" is not a floor derived from a search that tried; it is the output of a search that did not tolerate the OCR the same sentence says it must. A reader is told a verification pass established seven when the same pass, run once more with a two-character allowance, establishes fourteen — and the row's rhetorical force ("a live, recorded primary route to Augustine's own voice") is materially stronger at fourteen.

**One sub-point on 158.** It is a genuine act (bracketed by `157. PtUUamt tpiucpit dixii` and `139. PeiHktnat epitcopuÂ» dixit`, the latter an OCR'd 159), and Augustine genuinely speaks — but what follows is his mandate subscription, and the line carries none of the formula the row says these seven share. Of the seven named, it is the one that does not support the sentence it is cited in.

### L3 — "now exists in the shared corpus" is not true of any shared location. The file is on neither `main` nor this branch; it exists only on an unmerged sibling branch — as the same cell says four sentences later.

**Where.** Row 65: "**What it opens:** a live, recorded primary route to Augustine's own voice at the 411 Conference **now exists in the shared corpus**."

**Verified this round.** `git ls-tree main cic/texts/` → no `pl11-*` and no `theodosianus-16-*`. `ls cic/texts/` on this branch → 50 `.txt` files, neither present. `git merge-base --is-ancestor don-lpc main` → **NO**. `git merge-base --is-ancestor don-lpc HEAD` → **NO**. Both files exist only at `don-lpc` (= `donatism-lpc-integration`), unmerged in either direction.

The same cell states the correct position two sentences later — "**Not present on this world's own branch, so not usable directly by this document without its own vendoring step**" — so the row contradicts itself within one cell. Row 44 carries the identical "not present on this world's own branch" clause and makes no "shared corpus" claim; row 65 should match it.

### L4 — Row 44's Source cell still names a **1954 photostat reprint** while the correction now rests on a **1905** printing and argues public domain "by its 1905 date." The two imprints are not reconciled.

**Source cell, unchanged:** "*Theodosiani libri XVI cum Constitutionibus Sirmondianis*, 2nd ed. (Berlin: Weidmann, **1954 photostat reprint of the 1905 edition**), full text (all 16 books)."

**Verification Note, added by this revision:** "The vendored `theodosianus-16_mommsen-meyer1905.txt` named above is a Google Books scan of **the original 1905 Weidmann volume**, carrying Google's own public-domain finding … and **independently public domain by its 1905 date**."

**Verified against the file:** both title pages read `BEROLINI / APVD WEIDMANNOS / MDCCCCV`. It is the 1905 original, not the 1954 reprint.

The by-date reasoning the row now relies on is correct for the object vendored and would **not** hold for the object the Source cell names. A reader checking "is this row's named source public domain?" is handed a 1954 imprint and a 1905 argument. The row should say which physical printing it is now about, as row 88 does for its own edition-provenance gap.

### L5 — The revision corrected one instance of the edition-vs-work conflation and ran no sweep for the same shape. Row 59 presents it unfixed, and this defect class has a documented precedent in this build's own review history.

**The corrected shape**, per row 65: a modern in-copyright critical edition marked "not a vendoring candidate," where the underlying ancient text's earlier printings carry a different rights position that was never checked.

**Re-derived this round across all 212 rows.** Eight Type-P rows still carry "not a vendoring candidate." Five of the eight are clean, and three of those five are clean *because a prior round already caught this exact defect*:
- **Row 64** (Labrousse, Optatus SC 412–413) names the alternative: "**Karl Ziwsa's public-domain CSEL 26 (1893) critical Latin text is already vendored on the sibling Donatism build's own branch … and is the edition of first resort for row 27**."
- **Row 67** (Mutzenbecher, *Retractationes* CCSL 57) names it: "**Knöll's CSEL 36 (row 78, added Round 5) is the public-domain edition of the same text and was the real acquisition candidate, now acquired and vendored as row 209**" — the fix that `Doc02_Round5_Review.md`'s **M6** commissioned, headed in that artifact: "*Row 67 answers H1's own gap with an in-copyright edition and calls it 'not a vendoring candidate,' without naming the public-domain critical edition…*"
- Rows 49 and 50 (Divjak, Dolbeau) are genuinely correct — newly discovered letters and sermons with no earlier printing to have.

**Row 59 is not clean.** Munier (ed.), *Concilia Africae a. 345 – a. 525*, CCSL 149 (Brepols, 1974), Type P, Confidence C, Native:

> **Not currently vendored.** … In copyright; consultation-only, **not a vendoring candidate**. Flagged for priority second-opinion review before it supports any specific claim

— licensed for row 26's Apiarius-affair claim, with no earlier printing of the African conciliar corpus named or ruled out, in a Registry that already vendors Hartel's CSEL 3 and already carries two rows (27, 42) for the 256 Council of Carthage. This finding does not assert that a public-domain edition exists; it asserts that row 59 has the identical structure row 65 just had, that the revision ran no sweep, and that the sweep is a lookup the revision's own Registry already models at two rows.

**Why LOW rather than MEDIUM.** Row 59 licenses a claim row 26 already concedes rests on secondary characterization, so nothing turns on it today; and the revision's scope was legitimately two rows. What is missing is the *disclosure* — the revision states no sweep and names no residual, in a build where Round 25's own fix pass established running a full-corpus sweep for each finding's underlying claim as the standing practice.

### L6 — The review-count discrepancy is presented as "observed at Round 28 … found the conflict while editing this line," with no citation of the record. `Doc02_Round27_Review.md` reports both limbs of it and states that Rounds 16 through 23 each reported it too.

**What the revision says**, at `Source_Registry.md` line 3 and `Doc_02_Source_Ecology.md` line 3: "A pre-existing discrepancy in this line, **observed at Round 28**…" · "None of the three was authored by Round 28, **which found the conflict while editing this line**."

**What was already on the record, in the same folder.** `Doc02_Round27_Review.md`, M3's closing note:

> *(Note, so the record is accurate: the Status line's own "**Approved to proceed** … 2026-09-02", stated without a supersession marker while Doc_02 §10 disposes all three documents to 2026-09-08, and its "**Fourteen independent adversarial review rounds**" over a record now at twenty-six, are both **pre-existing** staleness this commit did not introduce and **which Rounds 16 through 23 each reported as observed state**.)*

Both limbs — the date and the count — named, graded as pre-existing, and attributed across eight prior rounds. Round 27's M3 proper is *also* about the first clause of the same line, and this revision rewrote that clause.

**Why this is a finding.** The revision refers a long-standing, repeatedly-reported open item to a fresh reviewer as though it were newly noticed, and does so without opening the two most recent review artifacts in its own `Review-Artifacts/` folder — the folder whose existence the discipline's "review rounds exist as files, not claims" rule is about. The disclosure is honest about *authorship* ("None of the three was authored by Round 28") and wrong about *discovery*. Citing Round 27's M3 would have cost one clause and would have handed the reviewer the eight-round history for free.

### L7 — The two disclosure paragraphs written in the same commit disagree with each other about the same discrepancy: two-way versus three-way, and "rounds 15–25" versus "rounds 15-27."

**`Source_Registry.md` line 3:** frames it as a **two-way** conflict (this line's fourteen/2026-09-02 versus Doc_02's twenty-five/2026-09-08), and scopes the question as "a factual question about **rounds 15–25's own scope**."

**`Doc_02_Source_Ecology.md` line 3:** frames it as **three-way** (twenty-five here, fourteen at the Registry, twenty-seven artifacts on disk), and scopes it as "a factual question about **rounds 15-27's own scope**."

The Registry paragraph was written at `37e3ee5` and updated at `0124a9f`; the Doc_02 paragraph was written at `0124a9f`. The renumbering commit rewrote the Registry's Round numbers and left its framing and scope at the pre-`0124a9f` state, so the two now describe the same problem at two different sizes. This is `co024b`'s "Cross-document fact consistency" rule exactly — the same specific claim stated in two documents of the same build, drawn from the same underlying material, not matching, and the difference not disclosed.

---

## COSMETIC

### C1 — The renumbering pass left one site: `Source_Registry.md` line 3 still says "stood on the **pre-Round-26** text."

Every other round reference on that line is now Round 28 (five occurrences). This one was missed, and it is the worst one to miss, because **Round 26 is a real, different round on this branch** — `Doc02_Round26_Review.md`, the Doc_02 banner-strip verification. "Pre-Round-26 text" now names an actual, earlier state that is not the state meant. Should read "pre-Round-28."

### C2 — Row 44 quotes the law's heading as `"412 Ian. 30"`; the file prints `(412 lan. 30>`.

Minor and inherited — the string is the sibling build's own normalization, carried across accurately from `don_Decision_Log.md` and don Registry row 16 — but row 44 presents it as the heading "in the text's own heading" while the scan reads `lan.` with a lowercase L and an unbalanced closing bracket. Same class as L1, at a fraction of the weight, and correctly attributed to the sibling build rather than claimed as this session's own read.

### C3 — Row 65 does not say where in the volume the seven-disputant list sits, and it is not in the acts.

The `ACTORES VII` table is in the *Gesta* section's own preliminary matter, at file line 113083, under the heading `NOMLAA ET SEDES / EPISCOPORUM XVIII UTRIUSQUE PARTIS QUI ELECTI SUNT AD COLLATIONEM IIABLNDAM`, following Dupin's and Dallaeus's prefaces and preceding the numbered acts. The row's two content claims are therefore evidence of different kinds — a delegate roster and recorded speech — and the row presents them in one breath. The substance is unaffected (Augustine's membership among the seven *actores* is independently confirmed by his speaking in fourteen acts), and a one-clause locator would close it.

### C4 — "closing that build's own Registry row 14" overstates what row 14 records.

Don Registry row 14, read this round, withdraws the wrong determination and then **holds Confidence at B, not A**: "the file's own text has not yet been read in full or excerpted to a clean boundary, and this row's own Author Gravity assessment has not yet been performed against it." The vendoring closed the row's erroneous *rights* finding, not the row. "Withdrawing" or "correcting" would be exact; "closing" is not.

---

## Adjudication: the review-round count, referred here by the revision

**Three numbers are in play, and a fourth is implied.** `Source_Registry.md` line 3: "**Fourteen** independent adversarial review rounds," with a disposition dated **2026-09-02** and a pointer to "`Doc02_Round1_Review.md` through `Doc02_Round14_Review.md`." `Doc_02_Source_Ecology.md` line 3 and §10: "**Twenty-five** … (Rounds 1–14 against the original 2026-09-01 text; Rounds 15–25 against the 2026-09-08 revision)," disposition **2026-09-08**. `Review-Artifacts/`: **twenty-seven** `Doc02_Round*_Review.md` files.

**Evidence available, and one that is not.** The repository is **shallow** (`.git/shallow` present; `git rev-list --count` returns 1 on `lpc-own`, `don-lpc` and `main` alike), and every commit the review artifacts cite — `1e01153`, `acb3396`, `9c1cc01`, `7bdb759`, `8c2a322`, `cc489ab` — is absent. **`git log` cannot be used as evidence here**, and any adjudication resting on it would be unfounded. The adjudication below rests instead on the artifacts themselves, which are dated and self-describing, and on the Decision Log.

**Findings.**

1. **Twenty-seven rounds have run, and all twenty-seven exist as files.** `git ls-tree HEAD` confirms all twenty-seven `Doc02_Round*_Review.md` are tracked at HEAD, numbered 1–27 with no gap and no duplicate. The sequence is internally consistent: Round 26's own header states its reviewer "did not write Rounds 1–25"; Round 27's states "did not write Rounds 1–26." Rounds 26 and 27 are Doc02-series rounds against this same document set — Round 26 against `Doc_02_Source_Ecology.md` plus the Decision Log, Round 27 against `Source_Acquisition_Manifest.md` and `Source_Registry.md` — so they count on exactly the terms the Doc_02 sentence uses ("against this document, `Source_Registry.md`, and `Source_Acquisition_Manifest.md` in total").

2. **The Registry's "Fourteen / 2026-09-02" is the most wrong of the three, and is stale by thirteen rounds and six days.** It is a verbatim survival of the original joint disposition, which `lpc_Decision_Log.md` line 121 records under the heading "**2026-09-02** — Doc_02, `Source_Registry.md`, and `Source_Acquisition_Manifest.md` self-disposed to Approved to proceed, after **Round 14** independent adversarial review returned no finding at all." It was correct on 2026-09-02. It was superseded on 2026-09-08, when Doc_02 §10 disposed **all three documents by name** to Approved to proceed, 2026-09-08. The Registry line was never updated, carries no supersession marker, and — after this revision — no longer even states the date it claims to state (M4).

3. **Doc_02's "twenty-five" was correct when authored and is now stale by two.** Round 25 was the last round when the sentence was last written; Rounds 26 and 27 both ran the same day (their own headers date them 2026-09-08, against commits timestamped 12:08:05 and 13:23:10 UTC respectively). §10's "Round 25, the most recent" is stale by the same two.

4. **The revision did not make either line stale, and did not author either sentence.** That much of its disclosure is accurate and verified. What it did do is edit both lines while leaving both stale sentences standing verbatim, and delete one of the two conflicting data points from one of them without saying so.

**Adjudication.** **Twenty-seven** is the correct count of independent adversarial review rounds run against this document set, and **2026-09-08** is the correct date of the disposition both Status lines describe. Neither current number is right. The Registry line should be brought to the Doc_02 form — a date of 2026-09-08, a count that matches the artifact folder, and a pointer through `Doc02_Round27_Review.md` — or, better and in keeping with the same line's own stated remedy for hand-maintained figures ("**Row count: see the table's own final row number, not a figure stated here** — a hand-maintained count is not trustworthy even under close attention; the fix is to stop stating one, not to try harder"), should stop stating a count and point at `Review-Artifacts/` instead. That remedy is already written into the line, one clause away from the number that keeps going stale, and has now gone stale for a ninth time across Rounds 16–23, 27 and 28.

**One caution attached to any repair.** A count is not the whole of it. Rounds 26 and 27 **both returned SUBSTANTIAL REVISION REQUIRED**, and Round 27's twelve findings are unfixed and unlogged (M5). Raising "fourteen" to "twenty-seven" without saying that would replace a stale number with a number that implies a clean record it does not have.

---

## What was checked and found clean

**Row 65's substantive core — every element re-derived directly against `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`, not from the sibling build's account:**
- The file genuinely contains the *Gesta*, not a summary or a table of contents. Running heads `GESTA COLLATIONIS CARTHAGINENSIS` located at file lines 121906, 127700, 128343 and 130382, with Dallaeus's own preface to the Collatio at 112750 and Balduin's *Historia* following; numbered acts present in continuous sequence with recorded speech.
- **Augustine is a named disputant**, listed among exactly **seven** Catholic *actores* — `ACTORES VII. / EX PARTE CATHOLICORUM`: Aurelius (Carthage), Alypius (Thagaste), Augustinus (Hippo Regius), Vincentius, Fortunatus, Fortunatianus, Possidius. Seven, counted. **Possidius of Calama is present** (`Possidius Calamensis`), as the revision states — and, not claimed by the row, he also speaks in his own right at acts **29, 142 and 168** (`Possidius episcopus Ecclesiae catholicae dixit`).
- **All seven act numbers the revision names were checked individually at their own file lines** — 50 (126795), 53 (126873), 158 (121763), 160 (128392), 187 (128715), 201 (129008), 272 (130297) — and every one is a genuine numbered act in which Augustine speaks. None is fabricated; none is a misattribution to another speaker; none is an index or contents entry. (The count is a floor and the quotations are normalized — L1, L2.)
- **Migne PL XI's rights basis holds and is honestly stated.** The header's `Rights: Public Domain` / `Rights basis:` block grounds it in the series' 1840s–1850s compilation and names the in-corpus precedent (`monumenta-vetera-donatistarum_migne-pl8.txt`, "1844 compilation date alone") — exactly what row 65 restates. The header also discloses, rather than papering over, that "this specific volume's own front matter did not carry a clearly OCR-legible year in this scan," so the date is a series-level inference. Row 65's "on the same by-date basis this corpus already accepts for its other Migne PL volumes" is a faithful restatement, neither stronger nor weaker than the header.
- **The sibling build's Registry row 14 really did say what the revision quotes.** Row 14's preserved original note: "Not currently vendored, and no public-domain edition identified. **Confirmed unavailable in the public domain**, recorded not requested." Its 2026-09-07 update states the determination "was wrong, made without working network access to actually check it" — the revision's characterization, verified.
- **The vendoring date is right.** `don_Decision_Log.md` heading "**2026-09-07** — Prompted by Mark asking 'do you have all the sources you need now?': a prior 'confirmed unavailable' finding (Registry row 14, the *Gesta Collationis Carthaginiensis*) turns out to have been wrong," with the vendoring recorded in the same entry.

**Row 44's rights and identity claims — every element re-derived directly against `theodosianus-16_mommsen-meyer1905.txt`:**
- **Genuinely the 1905 edition.** Two title pages in the body: `THEODOSIANI / LIBRI XVI / CVM CONSTITVTIONIBVS SIRMONDIANIS / ET / LEGES NOVELLAE AD THEODOSIANVM PERTINENTES … EDIDERVNT / TH. MOMMSEN et PAVLVS M. MEYER … VOLVMINIS I PARS POSTB^RIOIl / BEROLINI / APVD weidmannos / MDCCCCV`, and a second at `VOLVMINIS I PARS rOSTERIOR / TEXTVS CVM APPARATV / BEROLINI / APVD WEIDMANNOS / MDCCCCV`.
- **Genuinely public domain, on both grounds the row states.** Google's disclaimer page is retained unstripped in the body at file lines 79–113 ("It has survived long enough for the copyright to expire and the book to enter the public domain"), exactly as the header claims and the row repeats; and MDCCCCV = 1905 independently settles it. The row's contrast with the OTA copy's CC BY-NC-SA licence is sound: a licence on a transcription is a different object from a scan of a public-domain printing.
- **`CTh` XVI.5.52 is where and as claimed.** Heading at line 87862: `XVI, 5, 52 (412 lan. 30>`; the clause at line 87881: `que, circumcelliones argenti pondo decem.` — verbatim, inside the graduated fine schedule, under `DE HAERETICIS`, addressed `IDBM AA. sELBvco p(raefecto) p(raetori)o`.
- **G3 really was fully discharged on 2026-09-07.** `don_Decision_Log.md`: "**G3 (*Codex Theodosianus* Book 16, Mommsen & Meyer 1905) — fully discharged.**" The revision's Boyd clause is accurate to the source: the log reads "G3 no longer needs the Boyd 1905 substitute as its sole primary-text route, though Boyd remains a valid corroborating secondary source."
- **The correct item identifier.** `theodosianilibr01sirmgoog`, as row 44 states, distinct from `theodosianilibri02code` / `theodosianilibri00codeuoft` (the Prolegomena).

**The revision's negative claim about Doc_02, tested rather than accepted:**
- **Doc_02 §2's "post-411 Conference" phrase genuinely does not depend on row 65.** Line 44 reads "(post-405 Edict of Unity, post-411 Conference)" — a date-relative position marker inside a Representativeness bullet about Augustine's institutional confidence. Nothing in it turns on any reading of the acts. The revision is right.
- **`411` occurs at only two places in Doc_02** (lines 44 and 107, the latter Letter CXXVI's own a.d. 411 date, unrelated). §1, §6 and §9 were read in full and carry no dependency on rows 65 or 44 beyond §5's bullet, which was propagated. §9's eleven open items were read individually; none turns on either row.
- **Doc_01 and `Step0_Movement_Scope_Confirmation.md`** swept for `411`, `Theodosian`, `Gesta` and `Conference of Carthage`; no dependency found.
- **Registry rows that touch either row resolve correctly.** Row 12 exists and says what row 44 claims. Row 37 exists and states the "not present on this world's own branch, so not usable directly by this document without its own vendoring step" position both edited rows cite it for — verbatim. Row 88 exists and is the Latin Library copy row 44 describes. Row 111 (Alexander 1973) remains correctly "in copyright; consultation-only" and its licensing of row 65's material is unaffected. Row 164 (Humfress) licenses "rows 44/88" and is unaffected.
- **Where the files actually are** — established, not assumed: neither is on `main`, neither is on this branch, `don-lpc` is not an ancestor of either. The revision's "Not present on this world's own branch" is correct at both rows (though L3 sits against it in the same cell).

**Structural and table integrity — independently re-derived, all clean:**
- **212 table rows, numbered 1–212, no gap, no duplicate.** Exactly **12 pipe characters on every one of the 213 table lines** — no stray `|` anywhere in the two rewritten cells, which are the largest cells in the table.
- **Physical-order breaks are exactly the three the front matter discloses.** The parser returns breaks at 48→42, 193→60 and 60→52, matching the disclosed-placement rule's own "(48, 52, 60 among them)". Unchanged by this revision.
- **Bold-marker nesting** (run-aware sequential pairing over every `*`-run of length 2 or 3), **backtick balance**, **parenthesis balance** and **bracket balance** all clean on every line of both edited files, including the two very long rewritten rows and both rewritten Status lines.
- Both edited rows keep their eleven columns, their `#`, Type, Confidence, Boundary Status, Exclusion Reason, Comparandum, Added and Discovery cells byte-identical to `1b91ef2`.

**CO-022 discipline, checked directly:**
- **No new attribution to the project lead.** Row 44's two project-lead attributions ("Per the project lead's own decision this session"; "supplied directly by the project lead") are carried over verbatim from `1b91ef2` and are both backed by verifiable dated records — `lpc_Decision_Log.md` lines 93–101 ("2026-09-02 — Project-lead decision: the *Codex Theodosianus* file supplied this session is referenced, not vendored") and lines 103–111 ("2026-09-02 — Project-lead action: a second, vendored copy … supplied directly"). The revision adds none of its own. This is the one recurring failure mode CO-022 names that this revision does not exhibit.
- **The confidence hold is correct and correctly reasoned.** Row 44 keeps Confidence **B** and states why against the Registry's own calibration rule: the row is still not vendored here and its Licensed-For content has not been read against a file on this branch, so "B" ("a specific work or locus is named accurately but was not independently re-checked against the vendored text this session") is the right letter and A would not be earned. Row 65 keeps **C**, correctly — the Lancel edition it names remains unread.
- **Both documents are correctly marked not disposed.** No disposition is self-applied; the Registry line correctly states the prior disposition "does not carry over"; neither document claims Frozen or Approved to proceed for the revised text.
- **The substantiality judgment is right.** Both edits change a sourcing conclusion, which is CO-022's own listed trigger. Treating this as substantial rather than cosmetic, and requiring a fresh round, is the correct call and is not over-scoped.
- **The pre-existing `Doc02_Round26_Review.md` is untouched**, byte-identical to its committed state at `1b91ef2` (md5 `c0bb75bc41281fc10cab35cac301ba6f`, both). Nothing in the artifact folder was overwritten by the revision or by this review.

**Considered and declined as findings:**
- *Google's retained notice asks for "non-commercial use."* Row 44 contrasts the vendored scan's rights position with the OTA copy's CC BY-NC-SA, and one might read the Google request as the same restriction. It is not: a scanning partner's request is not a licence over a work that is public domain by date, and the row grounds the conclusion on 1905 independently. No finding.
- *The `ACTORES VII` table is editorial apparatus rather than the acts' own text.* True (C3 records the locator gap), but Augustine's membership among the seven is independently established by his speaking in fourteen numbered acts, so the substance does not depend on the table. Not a finding beyond C3.
- *`Source_Acquisition_Manifest.md`'s network-access paragraph still asserts a block that `lpc_Decision_Log.md`'s 2026-09-08 entry says is resolved.* Real, live, and squarely Round 27's **M1**, already on the record and outside this revision's scope. Not re-raised here.
- *Rows 64 and 67 carrying "not a vendoring candidate."* Both name their public-domain alternative correctly (see L5). Clean.

---

## CO-022 escalation-category assessment

Run against all four categories, against what this revision actually does and against the state it leaves behind — not against what it says about itself.

**1. Representative identity, name, or title decisions — does not apply.** Neither edited row, neither Status line, nor §5 touches Representative identity, naming or titling. No Representative exists for this world yet; Doc_02 §6's own routing note correctly defers Article 23 characterization questions to a future document.

**2. Portfolio-level or cross-world strategic decisions — does not apply as made, but is the category the revision came closest to and did not name.** The test is whether the document *decides* something for a reason external to this world's own ecology. It does not: row 65 explicitly declines to exercise the opening it identifies ("named here as a real opportunity for a future Doc_04, **not exercised in this pass**"), and row 44 explicitly declines to raise Confidence or to vendor. Both corrections are grounded in this world's own evidentiary position. **But** both now rest wholly on artifacts held on an unmerged sibling branch, and whether the two files should be vendored onto this branch — or `don-lpc` merged — is a cross-world resource question this revision surfaces and leaves unnamed as such. Recording it explicitly as a portfolio-level question awaiting the project lead, rather than as a Doc_04 to-do inside a Registry cell, would be the disciplined handling. Not an escalation as the text currently stands; one clause from becoming one.

**3. Governance or methodology decisions — does not apply to the revision, but a governance question is now live in the documents it edited.** The revision changes no build-process rule. However, `Doc_02_Source_Ecology.md` §10 grounds the 2026-09-08 disposition of all three documents on the project lead's direct instruction to close the cycle after Round 25, and **two further adversarial rounds have since returned SUBSTANTIAL REVISION REQUIRED against those same documents, the later of which (Round 27, twelve findings) is unfixed and unrecorded**. Whether a disposition issued by direct instruction survives two subsequent adverse rounds is a question about how this build's own process works, and it is not a question a build thread or a reviewer settles. **Named here for the project lead.** It is not created by this revision; it is made visible by it, because this revision is the first pass to reopen those documents since.

**4. Unresolved tensions the pipeline cannot close on its own — APPLIES, on two distinct grounds.**

- **(a) A live falsehood in a shared artifact outside this build thread's editing authority.** `cic/corpus-map/donatism.yaml`'s *Codex Theodosianus* entry states, in a machine-readable note field, that the Mommsen–Meyer edition was "referenced there but not acquired after five attempts; that build settled for a substitute," and sets `confidence: needs-ruling` on that basis — citing "Source_Registry.md row 44 (lpc's own Registry)" by name as its authority. Row 44 now says the opposite. The file is another world's corpus-map bucket; re-homing or re-noting it is outside this build thread's authority, exactly as Doc_02 §10 and Round 25's own precedent establish. **This is CO-022's fourth category in its plainest form — a contradiction between two artifacts that this build thread cannot close from where it stands — and it should be recorded in `lpc_Decision_Log.md` and put to the project lead or a coach pass, not left standing.** The revision neither fixed it (correctly) nor flagged it (incorrectly).
- **(b) A document internally contradicting itself about its own disposition.** `Doc_02_Source_Ecology.md` line 3 says the document is REOPENED and not disposed, and points the reader to §10; §10 says the document is self-disposed to Approved to proceed, 2026-09-08. Both sentences are live in one document. This one *is* closable by the pipeline — it is M5's fix — and so is named here as a defect to repair rather than an escalation, but if the repair is deferred it becomes one.

**On the review-count question specifically.** The revision referred it to this reviewer rather than resolving it unilaterally. That was the right instinct — it is a factual question about the record, and the thread that had just edited the line was not the right one to settle it. It is adjudicated above on evidence, and it does **not** require escalation: the record is unambiguous once the artifact folder is counted. What the revision should also have done, and did not, is cite `Doc02_Round27_Review.md`'s M3 and its eight-round history (L6), which would have made clear that this is a ninth recurrence of a known defect rather than a new discovery.

---

## Restated verdict

**SUBSTANTIAL REVISION REQUIRED — 1 HIGH · 6 MEDIUM · 7 LOW · 4 COSMETIC.**

Both corrections were right to make, and their hard parts survive independent re-derivation: the *Gesta* really is vendored and public domain, Augustine really is a named disputant who speaks in the acts, Possidius really is there, the Mommsen–Meyer 1905 text volume really is the right volume and really is public domain, XVI.5.52 really does read *circumcelliones argenti pondo decem*, and G3 really was fully discharged on 2026-09-07. The prior conclusions this revision withdraws were genuinely wrong, and withdrawing them was overdue.

What fails is the reasoning built on top of the verified facts and the sweep that should have followed them. **H1** puts a false statute identification into the Registry of record, refutable against a file already vendored on this branch and already verified by this build — the payload sentence of the row-44 correction. **M1** misreports the sibling build's own acquisition history in a way that erases a standing security caution this world's Manifest carries. **M2** and **M3** leave four artifacts on this branch — one of them machine-readable and citing row 44 by name — asserting what the revision just withdrew, with no sweep run and no flag raised for the one that lies outside this thread's authority. **M4**, **M5** and **M6** concern the record itself: an edit that misdescribes its own scope, a Status line that contradicts the section it points at, twelve unfixed findings from the last completed round left undisclosed, and no Decision Log entry for a substantial revision whose entire evidentiary basis lives on another branch.

The propagation shape is the seventh consecutive occurrence of the failure this document set's own "pattern worth naming" paragraph tracks. The quotation slips (L1) are the first of their kind in this sequence and are worth naming as a new shape: not a fact deleted alongside a banner, but a fact *normalized into* a quotation mark.

One escalation category applies. **CO-022 category 4** is triggered by the stale, row-44-citing note in `cic/corpus-map/donatism.yaml`, which this build thread cannot correct and has not flagged; it should be recorded in `lpc_Decision_Log.md` and put to the project lead or a coach pass. A second, related governance question — whether a disposition issued by the project lead's direct instruction after Round 25 survives Rounds 26 and 27 both returning SUBSTANTIAL REVISION REQUIRED, with Round 27's findings unfixed — is named for the project lead rather than decided here.

Neither `Doc_02_Source_Ecology.md` nor `Source_Registry.md` is eligible for any disposition on this text. Both should stay REOPENED, as the revision itself already marks them.

*This artifact is `Doc02_Round28_Review.md`. It was commissioned as Round 26; `Doc02_Round26_Review.md` and `Doc02_Round27_Review.md` are existing committed review records of the 2026-09-08 banner-stripping rewrites and were not written to, read-only-verified as unchanged, and are cited above.*
