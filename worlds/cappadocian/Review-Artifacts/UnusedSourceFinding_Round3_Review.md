# Unused-Source Finding — Round 3 Independent Adversarial Review

**Document under review:** `worlds/cappadocian/cappadocian_Unused_Source_Verification_2026-09-09.md` at **Revision 2**, together with the whole change set it dispositions (commit `f8d10ca` on top of `5cae808`; 19 files against the base `f07eb91`).
**Reviewer stance:** Independent adversarial. Did not author the document, the change set, the Round 1 review or the Round 2 review; no stake in its passing.
**Review date:** 2026-09-09.
**Branch reviewed:** `claude/cappadocian-unused-source-finding`.
**Prior reviews:** `Review-Artifacts/UnusedSourceFinding_Round1_Review.md` (14 substantial, 4 cosmetic — substantial revision required); `Review-Artifacts/UnusedSourceFinding_Round2_Review.md` (11 new substantial, 5 cosmetic, plus 5 of Round 1's not fully answered — substantial revision still required).
**Consulted:** `cic-build-cycle` SKILL.md read verbatim at `/root/.claude/skills/synced/7b788bfc-.../cic-build-cycle/SKILL.md` (the four escalation categories, the *Revision decision* rule, the *Naming and term propagation* rule, the *Review* and *Disposition* rules); `cappadocian_Doc_04_Gravity_Discovery.md` §§3.1, 3.2, 4, 9; `CAPPADOCIAN_BUILD_LEDGER.md` §§47, 50 including the Revision 2 addendum; `cappadocian_Source_Registry.md`; `engine/m1/gates.py`, `engine/m1/fk.py`, `engine/m1/schemas.py`; `cic/corpus-map/` and its `_staging` files; the three Latin/English witnesses on the unmerged branch `donatism-lpc-integration`.

---

## VERDICT: **SUBSTANTIAL REVISION STILL REQUIRED**

Seven new substantial findings (three of them narrow); of Round 2's sixteen findings, **twelve answered, one answered wrongly, three not or only partly answered**.

Let me put the credit first, because it is large and it is measured, not taken on the document's word.

**Everything this pass claims about a primary text is true.** I counted the Amphilochius `div2` myself and got body **129**, bracketed **25 + 14 = 39**, rendered **90** — exactly the document's figures. I read Ep. 210 in the file: the upbringing passage sits at offset **1750** from the element start and the `2.` marker at **3421/3498**, so "unnumbered opening section" is right and Revision 1's "§2" was wrong. Its §3 does carry the Thaumaturgus/Musonius chain, between the `3.` and `4.` markers. I diffed the Macrina quotation character-by-character against `ix.ccv-p26`: **verbatim, one substitution, `,]` → `.`**, exactly as disclosed, and the revised `modern_rendering` is faithful (the "handed down to us" and "that man" glosses Round 2 flagged are both gone) and scores **FK 5.55** against a ceiling of 10. I fetched `donatism-lpc-integration` and read all three Theodosian witnesses: the eleven names, the "no western bishop" point, the expulsion clause, the Latin Library file's own Confidence-C header, Mommsen's OCR damage (`conunemoratio`, `pxae-cepti`, `Njsseno`), and Boyd's note — which is exactly at **p. 46 n. 1**, as cited. I re-ran the whole compile battery: **build succeeds; 18 gates, 17 pass, `voice-perspective` the one failure on `cappadocian.dw.reading-scripture`; `determinism-check` `pass: true`; coverage 26 substantive / 2 honest-limit / 0 empty; `staleness-check` `pass: false` with `cappadocian` stale on the eight touched records; `pytest engine/m1/tests engine/m2/tests` 34 passed, 0 failed.** Every number in §5 is right. I re-ran `corpus_map_merge.py`: `valid.`, zero diff. And §1.3's new "five-level vocabulary" is not invented — `engine/m1/schemas.py` lines 47–52 give exactly five: Documented, Widely Accepted, Dominant Modern Reconstruction, Contested, Inferential-Thin. Round 2's own "four tiers" was the loose statement, not this document's.

**And then the through-line is still live, for the third round running, in the same shape.** Round 1 named it: *a claim asserted about a file, a rule, or a command's output without running the check.* Round 2 sharpened it: *never assert that a fix landed without opening the file it landed in.* Revision 2 asserts three more:

- **§3 says the `basil-against-eunomius` precedent citation "is withdrawn."** It is withdrawn from the document's prose. It is still standing, verbatim, in `cappadocian.source.amphilochius-iambics-to-seleucus.md`'s `divergence_note` at line 27 — *"which is the same condition this world already corrected `cappadocian.source.basil-against-eunomius` and `cappadocian.quote.basil-against-delaying-baptism` for."* That is a **compiled** field; I built the package and found the string in `compiled/repository.json`. This is Round 2's Finding 7, and it is answered the way Revision 1 answered Round 1's Findings 1 and 2: in the document, not in the file.
- **§1.5 states the sweep's completeness as a command result** — "a grep for the four-name string across `worlds/cappadocian/` and `records/cappadocian/` now returns nothing." I ran that grep. It returns `worlds/cappadocian/scripts/wb_cappadocian_s21.py:1073`, which is the *generator* that emitted the very record this pass hand-corrected, still carrying `"Helladius, Otreius, Gregory of Nyssa, and Amphilochius"` as row 79's `work` value.
- **§1.5 also states that Doc_02 §7 "now carries the full eleven, making Doc_02 line 37's pointer to it true for the first time."** Doc_02 §7 (line 112) carries the *count* eleven, four names, and a pointer to §2. Doc_02 line 37's pointer reads "see **§2** for the law's own full citation and bishop list," and it reads that identically at `f07eb91`, `88f9dd4` and `HEAD~1` — it never pointed at §7 and was never made true by anything done to §7.

Beyond that: the decomposition Revision 2 was told to fix is wrong again, in a different way (New Finding 4); the document's own status line and disposition section still say "Revision 1" and "awaits a Round 2 review" that has already returned (New Finding 5); and the one occurrence Round 1 named by file *and line* — `cappadocian_Integrated_Ecology_Analysis.md:139` — is untouched after two revisions and unmentioned in either (New Finding 3).

The honesty of the pass is not in question and has not slipped. It still names its own regression, its own punctuation substitution, its own withdrawn credit, its own repeated defect class, and it still claims no disposition. What has not changed across three rounds is that the checks the document reports are not always the checks it ran.

---

## PART ONE — WHAT I INDEPENDENTLY RAN OR READ

Everything in Parts Two and Three rests on one of these, not on the document's or a prior review's account of it.

**The Amphilochius section.** Read `div2 xvii.xxiii` (lines 44075–44103) of `cic/texts/npnf214_seven-ecumenical-councils.xml` in full with endnote 603. Counted every part programmatically under two markup-stripping conventions, and diffed the token lists between them to find where they differ.

**Ep. 210.** Located the `ix.ccxi` element boundaries by regex, measured the byte offset of "here I was brought up by my grandmother" and of every `N.` section marker in the letter, and read the §3 passage in context with both endnotes.

**The Macrina quote.** Extracted lines 37060–37068, stripped markup, and ran a character-level `SequenceMatcher` against the record's `text`. Computed `fk_grade` on the current and the pre-Revision-2 `modern_rendering` with `engine.m1.fk`, and read `engine/m1/gates.py` lines 365–390 to confirm which fields the `readability` gate actually grades.

**The Theodosian witnesses.** `git ls-remote` found `donatism-lpc-integration`; fetched it and read `codex-theodosianus_latinlibrary.txt` (CTh.16.1.3 at line 6887, plus the file's own header), `theodosianus-16_mommsen-meyer1905.txt` (lines 83672–83683), and `boyd_ecclesiastical-edicts-theodosian-code_1905.txt` (the note, and the running head that dates it to p. 46).

**Compile and gates.** `python -m engine.m2.cli staleness-check`; `build cappadocian` twice (packages `2026-09-09T02-33-09Z` and `2026-09-09T02-35-51Z`, both deleted); read `validation/gates-report.json` in full; counted `compiled/coverage.json` statuses; `determinism-check cappadocian`; `pytest engine/m1/tests engine/m2/tests`; grepped `compiled/repository.json` to establish which record fields reach compiled content.

**Corpus map.** Read both Thaumaturgus `_staging` rows; re-ran `python cic/engine/corpus_map_merge.py` and checked `git status` afterwards.

**Cross-document sweep, run independently.** Grepped `worlds/cappadocian/` (all file types, not just `.md`), `records/cappadocian/`, `cic/corpus-map/`, and all seven deployment chunks (`cappadocianctx001-002`, `cappadocianlex001-003`, `cappadocianstory001-002`) for: the four-name string, "eleven," "touchstone," "legal standard," "verse," "240," "Epp. 204," "Ep. 210," "Optimus."

**Counts and rules.** `grep -rl "verification_state: verified-direct" records/cappadocian/ | wc -l` → **62**; the dates inside those records; `git diff --name-only f07eb91 HEAD -- records/` → **8**; `engine/m1/schemas.py`'s `formation_confidence` enum; `cic-build-cycle` SKILL.md's escalation categories, *Revision decision*, *Review*, *Disposition* and *Naming and term propagation* rules read verbatim.

---

## PART TWO — JOB 1: WAS EACH ROUND 2 FINDING ANSWERED?

### The eleven substantial

| # | Round 2 finding | Verdict | Evidence |
|---|---|---|---|
| 1 | `amphilochius-of-iconium-own-works` still says "verse" and "240-word," untouched though two documents say otherwise | **ANSWERED** | `edition` now reads "One short extract of his own argument … about 90 rendered words in the editor's prose epitome, not verse"; the body's "240-word" is gone. §3's Changed list and the Registry's sixth-pass log ("All corrected above") are now true statements. One new blemish created by the edit — Cosmetic 1 below. |
| 2 | Registry row 65 still says "verse" and "verified directly" | **ANSWERED** | Row 65 (line 124) now reads "in the editor's prose epitome, not verse" and "now row 117, at Confidence B and `verified-via-authority`." Row 65 and row 117 no longer contradict each other or the record. |
| 3 | Ep. 210's upbringing is in the unnumbered opening, not §2 | **ANSWERED, and I re-verified it** | Record and verification doc §4 both now read "unnumbered opening section." Measured: the passage is at offset **1750**, the `2.` marker at **3498**, the `3.` marker at **6082**; the Thaumaturgus/Musonius chain is at **6481–6619**, i.e. genuinely in §3. Both halves right. |
| 4 | `work:` still called Ep. 210 "a thinner third witness" against its own body | **ANSWERED** | `work:` now reads "Epistles 204, 210 and 223 … Epistle 204 alone joins the two; 210 carries each separately; 223 corroborates" — which is the body's own finding, compactly. But this widens a gap Round 1 already named: see New Finding 7. |
| 5 | §1.3 contradicts itself four lines apart on whether classification turns on one score | **ANSWERED** | The reconciliation is real and checkable: "That is not the same as saying classification is a Formation-score threshold … for *this* candidate, with the other five tests already strong, the Formation score is where the question actually sits." I verified both supports — Doc_04 line 64 is headed "On Candidate 8's Formation score (**the decisive moderation**)," and line 125's matrix row reads "strong ×5; Formation moderate." *Not addressed:* Round 2's closing note that the second of the "two reasons" (Open Item 1 is "not a build thread's to close") is a statement about authority, not evidential weight. It stands unchanged. |
| 6 | "for the first time, not wholly true" is false | **ANSWERED** | Now: "**That caveat is not wholly true, and this pass is not the first thing to make it untrue** — 62 records … some since 2026-08-31 … stale for over a week and this pass merely adds to the pile." I counted: **62**, with 10 records carrying a 2026-08-31 date and one 2026-08-30. Exactly right, and the escalation is retained without the false credit. |
| 7 | The `basil-against-eunomius` precedent is the wrong record, corrected in the wrong direction | **PARTIALLY ANSWERED — the document withdrew it; the record did not** | §3 explains the error correctly and in the right terms ("the work is absent from the vendored file altogether, rather than present as an editor's selection"). But `cappadocian.source.amphilochius-iambics-to-seleucus.md` line 27 still cites it, in a **compiled** `divergence_note`. See New Finding 1. |
| 8 | The sweep's completeness claim is false; four live occurrences remain | **NOT ANSWERED** | Doc_02 §7 (line 112) is fixed and fixed well. The three other occurrences Round 2 listed are untouched, unmentioned, and one of them (`Integrated_Ecology_Analysis.md:139`) was named by file and line in Round 1 as well. Round 2's fix said: complete the sweep, *or* record the ones judged acceptable — "what is not acceptable is asserting completeness." Revision 2 did neither; it substituted a narrower assertion, which is itself false. See New Findings 2 and 3. |
| 9 | The ~240 decomposition does not add up | **ANSWERED WRONGLY** | The omitted closing "Note." is now included, which was the substance of the finding. But the new decomposition is wrong: the closing Note is **51** words (50 + the label), not "~54," and "59" and "242" come from two different counting conventions. See New Finding 4. |
| 10 | The Cross-Check "re-run" grades on invented tiers and could not have failed | **ANSWERED, and answered well** | Rewritten into Doc_04's own vocabulary, and it says the hard thing: "**that outcome was not in doubt, and it would be dishonest to present it as a test that could have failed.**" The "project's fixed five-level vocabulary" is correct — `engine/m1/schemas.py` gives exactly five levels. This is the strongest single fix in the revision. |
| 11 | Category 4 tested against a paraphrase | **ANSWERED** | §7 now quotes the skill's three triggers and matches SKILL.md line 59 word for word, notes that the third carries no "unresolved" qualifier, withdraws the paraphrase, and escalates the Amphilochius correction on it. Only trigger 3 is actually disposed of, though, and trigger 2 now fires — see New Finding 6. |

### The five cosmetic

| # | Round 2 cosmetic | Verdict | Evidence |
|---|---|---|---|
| 1 | "seven files under `records/`" should be eight | **ANSWERED** | §2.1 now says eight. `git diff --name-only f07eb91 HEAD -- records/` returns exactly 8. |
| 2 | §5's pytest line is stale at 33/1 | **ANSWERED** | Now "34 passed, 0 failed," with the fresh-clone self-heal explained. I ran it: `34 passed in 20.04s`. |
| 3 | "Optimus of Antioch (in Pisidia)" is an undisclosed editorial identification | **ANSWERED** | Doc_02 §2 now reads "Optimus of Antioch for proconsular Asia and the Asian diocese." The Latin in both witnesses reads only *Optimo episcopo Antiocheno*. The addition is gone rather than defended, which is the right call. |
| 4 | Two glosses removed from `modern_rendering`, two added | **ANSWERED IN THE FILE, DISCLOSED NOWHERE** | Now "Wherever I found people walking by the rule of godliness that had been handed down, those I took for my fathers" — plural restored, "to us" gone. Faithful, and FK unchanged at 5.55. But neither §4, nor §5, nor ledger §50's addendum records that a compiled field was edited, in a document whose own §5 says "Recorded rather than silently fixed." See Cosmetic 2. |
| 5 | §5's causal phrasing — extending `text` cannot move `modern_rendering` | **NOT ANSWERED** | Line 136 is verbatim unchanged. `engine/m1/gates.py` lines 376–381 add only `modern_rendering` to `checks` for quote records; `text` is never graded. |

**Count: 12 of 16 answered; 1 answered wrongly (9); 1 partially (7); 2 not answered (8, and cosmetic 5).**

**Also still open from Round 1, through two revisions and unmentioned in both:** Finding 8e (`Integrated_Ecology_Analysis.md:139`), Finding 8h (`cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md:92` still lists "Amphilochius of Iconium's genuine works" among the honest gaps, unqualified, when a genuine extract is now recorded at row 117), and Finding 8i (Registry row 11 and Doc_02 §1.4 still cite only "Epp. 204 and 223"). Round 2 marked all three NOT ANSWERED. None was addressed and none was declined on the record.

---

## PART THREE — JOB 2: NEW DEFECTS INTRODUCED OR LEFT BY REVISION 2

### 1. [SUBSTANTIAL] The withdrawal of the `basil-against-eunomius` precedent did not land in the record, which still asserts it — in compiled content. Third round, same shape.

**Location:** `records/cappadocian/source/cappadocian.source.amphilochius-iambics-to-seleucus.md`, `divergence_note` lines 25–28.

```
Verification state is verified-via-authority rather than verified-direct for
that reason: the vendored file was opened and read directly, but what it
carries is the NPNF editor's own selection and epitome, which is the same
condition this world already corrected cappadocian.source.basil-against-eunomius
and cappadocian.quote.basil-against-delaying-baptism for.
```

`git diff HEAD~1 HEAD` on this file shows only the word-count paragraph changed. The precedent sentence is untouched.

**Why it is substantial and not a stray.** It is a **compiled** field. I built the package and grepped: `compiled/repository.json` contains `already corrected cappadocian.source.basil-against-eunomius`. And the claim is false in the way Round 2 established and this document now agrees it is false — `cappadocian.source.basil-against-eunomius` is at `verification_state: unverified`, and its own `divergence_note` says it "previously claimed the treatise text was verified-via-authority" and was corrected *away* from that grade, for the opposite condition (absence from the file, not presence inside an editor's selection). The Representative's repository therefore carries, as the stated justification for one record's confidence grade, a precedent that stands for the opposite proposition.

**And the document says otherwise.** §3: "**The citation is withdrawn here**, and ledger §47's own statement of the precedent is now stale and should be corrected by whoever owns that entry." A reader takes that as the correction having been made. It was made in the prose only.

**Fix.** Delete `cappadocian.source.basil-against-eunomius` from the record's `divergence_note`, leaving `cappadocian.quote.basil-against-delaying-baptism`, which is the correct precedent. Then re-check §3's "withdrawn here."

---

### 2. [SUBSTANTIAL] §1.5's completeness claim is stated as a command result and the command does not return what it says. The four-name string is live in `worlds/cappadocian/` — in the generator of the record this pass hand-corrected.

**Location:** verification document §1.5; ledger §50 Revision-2 addendum, third bullet, in identical words.

> "the completeness claim is restated as what it is: a grep for the four-name string across `worlds/cappadocian/` and `records/cappadocian/` now returns nothing."

I ran it:

```
$ grep -rn "Helladius, Otreius, Gregory of Nyssa, and Amphilochius" \
      worlds/cappadocian/ records/cappadocian/
worlds/cappadocian/Review-Artifacts/UnusedSourceFinding_Round2_Review.md:208
worlds/cappadocian/Review-Artifacts/UnusedSourceFinding_Round1_Review.md:153
worlds/cappadocian/scripts/wb_cappadocian_s21.py:1073
```

The two review artifacts are quotations and are fine. The third is not. `wb_cappadocian_s21.py` line 1073 is inside the `emit_source(79, "imperial-communion-law-of-381", …)` call, and the string is the **`work:` value** it writes into `records/cappadocian/source/cappadocian.source.imperial-communion-law-of-381.md` — the exact field Round 1's Finding 8a made this pass correct, and the exact string Round 1 quoted.

**What is and is not being claimed here.** The script's own docstring describes it as this world's first record-authoring pass, and the record has been hand-edited well past what the script emits, so re-running it would clobber far more than this line; whether it is worth editing is a judgment call this pass is entitled to make. What it is not entitled to do is report a grep result that the grep does not produce, in the specific sentence written to replace a completeness claim that a prior review found false — twice. If the sweep was in fact run over `--include=*.md` only, or over narrative documents only, that is what the sentence has to say.

**Fix.** Either correct the script's line, or state the claim as run: "a grep of the narrative documents and records under `worlds/cappadocian/` and `records/cappadocian/` returns nothing; the string survives in `scripts/wb_cappadocian_s21.py`, a superseded first-pass generator, left as a historical artefact."

---

### 3. [SUBSTANTIAL] `cappadocian_Integrated_Ecology_Analysis.md:139` still carries the exact overstatement this pass corrected everywhere else. Named by file and line in Round 1, again in Round 2, fixed in neither revision, mentioned in neither.

**Location:** `worlds/cappadocian/cappadocian_Integrated_Ecology_Analysis.md` line 139.

> "Imperial law reaches the world both as protection and as instrument of pressure: the 381 communion law (CTh 16.1.3) **makes this world's own bishops the empire's legal touchstone** (Doc_02 §2)…"

Against Doc_01 §4a, as this pass rewrote it:

> "So this world's own bishops were **written into** the empire's communion test; **they were not themselves that test.**"

And against Doc_02 §2, as this pass rewrote it:

> "a claim that should be made in that bounded form, **not as 'the world's own men *made* the empire's standard,' which four names out of eleven on a proconsul's list will not carry**"

Line 139 is the unbounded form, and it cites Doc_02 §2 — the very section that now says the unbounded form is not supportable. Both files are cleared master documents.

Of Round 2's other two, I judge `Integrated_Ecology_Analysis.md:161` ("the communion law naming its bishops as touchstones") and `Doc_05:29` ("naming the region's bishops as touchstones") **defensible as loose summary** — they say the law names bishops as touchstones, which it does. Line 139 is different in kind: it says the law makes this world's bishops *the* legal touchstone, which is the claim the pass's central correction exists to retire.

**Fix.** One clause: "names four of this world's own bishops among the eleven whose communion the empire made the test." And say on the record that 161 and Doc_05 §29 were considered and left as acceptable summary — which is what Round 2 asked for and did not get.

---

### 4. [SUBSTANTIAL — narrow] The corrected decomposition is wrong again. The closing "Note." is 51 words, not ~54; and 59 + 129 + 54 = 242 only by mixing two counting conventions and dropping the "VIII." numeral.

**Location:** verification document §3; Doc_02 §1.6; Registry row 117; `cappadocian.source.amphilochius-iambics-to-seleucus.md` `divergence_note` (compiled); ledger §50 addendum.

Measured, every part, both ways:

| part | strip-with-space | strip-without-space |
|---|---|---|
| "VIII." numeral | 1 | 1 |
| heading + endnote 603 | 61 | **59** |
| extract body | **129** | **129** |
| "Note." + closing paragraph | **51** | **51** |
| **whole `div2`** | **242** | **240** |

The two conventions differ by exactly two tokens, and I diffed the token lists to find them: `<i>Synodicon</i>,` and `<i>Epitome</i>.` — inserting a space when stripping tags orphans the comma and the full stop as separate "words." So **240 is the honest human word count**; 242 (the corpus map's figure, and Round 2's) is that count plus two punctuation marks.

Whichever convention is chosen, the document's figures do not decompose the section:

- **"~54" is wrong.** The closing editorial "Note." is 50 words of prose plus its one-word label — **51** — under both conventions. 54 is not a measurement; it is the residual 242 − 59 − 129.
- **"59" is right only under the convention that makes the whole 240**, and it excludes the "VIII." numeral, which the pass's own earlier accounting counted separately. Under the convention that yields 242, the same part is 61 (62 with the numeral).
- Correct statements: **60 + 129 + 51 = 240** (honest count), or **62 + 129 + 51 = 242** (the corpus map's convention).

This is the third statement of this figure and the second attempt at this decomposition, in a paragraph headed "**measured rather than estimated**," in a document whose central correction is that a number was reported without being measured. The magnitude is small; the location is not.

**Fix.** "…the whole `div2` runs to 240 words as ordinarily counted (the corpus map's ~242 counts two orphaned punctuation marks): 60 words of section numeral, editor's heading and method note, the 129-word extract body, and a 51-word closing editorial 'Note.' on the four scriptural canons." Correct in all four content locations, one of which is compiled.

---

### 5. [SUBSTANTIAL — administrative] The document says it is Revision 1 and awaiting a Round 2 review that has already returned and called for substantial revision — while citing that same review twice in its own body.

**Location:** the `**Status:**` line (line 6) and §7's first paragraph (line 165).

> **Status:** Revision 1 (2026-09-09), after an independent adversarial review of the first draft returned substantial revision required with 14 substantial findings… **it awaits a Round 2 review.**

> …this is **Revision 1** answering it… **No disposition is claimed until a Round 2 review returns without calling for substantial revision.**

Meanwhile §1.5 reads "**the Round 2 review** found Doc_02 §7 (line 112) still carrying the four-name form," §7's own category-4 bullet says "**Revision 1** tested against a paraphrase … that paraphrase is withdrawn," and ledger §50 carries a heading "**Revision 2 (same day), answering a Round 2 adversarial review**."

The document therefore states, in the two places a reader looks for its standing, that a review exists which its body proves has already come back — and sets a disposition condition ("until a Round 2 review returns") that is already spent. The skill's *Disposition* rule says a status line inside the document is not evidence of anything on its own, which is exactly why it must not be wrong: this is the one part of the document a coach thread or the project lead reads to know where the work stands.

**Fix.** Status: "Revision 2 (2026-09-09), answering Round 1 (14 substantial / 4 cosmetic) and Round 2 (11 substantial / 5 cosmetic), both of which returned substantial revision required." §7: "…this is Revision 2 answering Round 2. No disposition is claimed until a review returns without calling for substantial revision."

---

### 6. [SUBSTANTIAL — narrow] §1.5's two claims about Doc_02 §7 and Doc_02 line 37 are both wrong, and both were checkable in one `sed`.

**Location:** verification document §1.5, the parenthetical inside the "Occurrences corrected" list.

> "Doc_02 §7 (**which now carries the full eleven**, making **Doc_02 line 37's pointer to it** true for the first time)"

Doc_02 line 112 (§7), as revised, reads: "the 381 communion law, **whose eleven named bishops include four of this world's own** (Amphilochius of Iconium; Helladius of Caesarea, Otreius of Melitene, Gregory of Nyssa) — **see §2 for the full list** and the law's own mechanism." It carries the *count*, four names, and a pointer elsewhere. It does not carry the full eleven, and it correctly does not try to.

Doc_02 line 37 reads: "named in the imperial communion law of 381 — **see §2** for the law's own full citation and bishop list." It points at **§2**, not §7, and `git show f07eb91:…`, `88f9dd4:…` and `HEAD~1:…` all return that line byte-identical. It was made true by Revision 1's rewrite of §2 (Round 1 Finding 8g, which Round 2 marked answered), and §7 had nothing to do with it.

Small, but this is a sentence written to replace a false completeness claim, and both halves of it are new assertions about lines in a file that nobody opened.

**Fix.** "Doc_02 §7 (which now carries the count, this world's four, and a pointer to §2's full list)."

---

### 7. [SUBSTANTIAL — narrow] Correcting the record's `work:` field widened, rather than closed, an inconsistency Round 1 named at Finding 8i and Round 2 marked NOT ANSWERED.

**Location:** `cappadocian.source.basil-macrina-the-elder-letters.md` `work:` against `cappadocian_Source_Registry.md` row 11 (line 50) and `cappadocian_Doc_02_Source_Ecology.md` §1.4 (line 42).

The record now reads `Basil, Epistles 204, 210 and 223`. Its own `external_ids.cappadocian_source_registry_row` points at row 11, which reads `Basil, Epp. 204 and 223 (Macrina the Elder, transmission of Gregory Thaumaturgus' teaching)`. Doc_02 §1.4 reads `(Epp. 204, 223)`. The volume's prolegomena — which this pass verified at line 952, endnote 21 — cites all three.

Before Revision 2, record and Registry row agreed on 204/223 and differed only in how they described 210. Now the citation itself differs between a record and the Registry row that indexes it, and between a record and the document it is built from. That is exactly what the skill's *Naming and term propagation* rule is written against: *"A fix that lands in the narrative document without the index being updated to match is not a complete fix."*

The same rule leaves `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md:92` — "Epiphanius' *Panarion* … and **Amphilochius of Iconium's genuine works**" among the honest gaps, unqualified — standing after a pass that put an extract of those genuine works into the Registry at row 117. Round 1 Finding 8h; Round 2 NOT ANSWERED; still unmentioned.

**Fix.** Row 11 and Doc_02 §1.4 to "Epp. 204, 210 and 223"; G1 line 92 to "…and Amphilochius of Iconium's genuine works *as a corpus* (one extract is held — row 117)."

---

### And one that the escalation analysis now has to reach

**§7's category 4 disposes of trigger 3 and leaves trigger 2 undisposed, and trigger 2 now fires.** The skill's second trigger is *"a contradiction between two already-cleared master documents."* With New Finding 3 standing, `cappadocian_Integrated_Ecology_Analysis.md` and `cappadocian_Doc_01_World_Identification.md` / `cappadocian_Doc_02_Source_Ecology.md` say opposite things about whether the 381 law made this world's bishops the empire's legal test — three cleared master documents, two positions. §7 quotes the trigger and then does not test the change set against it. Fixing New Finding 3 removes the trigger; leaving it means the bullet has to say so.

---

### COSMETIC

1. **A broken sentence, created by Revision 2's own edit.** `cappadocian.source.amphilochius-of-iconium-own-works.md` line 40 now reads "That was false at the time it was written: **a roughly** / extract of his own argument to Seleucus on the canon of Scripture…" — "240-word" was removed and "roughly" left behind.
2. **The `modern_rendering` edit is disclosed nowhere.** Round 2's Cosmetic 4 was applied to a compiled field and recorded in neither §4, nor §5's regression paragraph, nor ledger §50. §4 still names only the two Round 1 glosses ("your own city"; "with them") as corrected. In a pass whose stated discipline is "recorded rather than silently fixed," a silently fixed compiled field is worth one clause.
3. **"Stale" is the wrong word for ledger §47.** §3 says §47's precedent citation "no longer holds" and §6.7 calls it "stale." `cappadocian.source.basil-against-eunomius` was corrected away from `verified-via-authority` on **2026-08-31**; ledger §47 is dated **2026-09-02**. It was wrong when written, not made wrong later. The escalation is right either way — §47 cites the record as "the precedent already set for **this exact genre of gap**," and the gap is a different genre — but the characterization should match the dates. (§47's actual words are "corrected the same way for a different work," which the document paraphrases as "corrected *to* `verified-via-authority`"; quoting §47 rather than paraphrasing it would settle the ambiguity in the direction the escalation needs.)
4. **"All eleven names" is slightly more than the vendored Boyd supports.** §1.5: "What three witnesses agree on — the clause's substance and all eleven names, with Boyd's independent English note listing the same eleven — is solid." Boyd's note names the same eleven *sees*, but the vendored scan renders two of the persons as "**Necrarius** of Alexandria" (for Timothy) and "**George** of Nyssa," alongside "Olreius of Meletus" and "Marmoria of Martianopolis." The document discloses Mommsen's OCR damage carefully and says nothing about Boyd's. "the same eleven sees, with two personal names OCR-corrupted" would be exact. (The citation itself is exact: I found the note under the running head "46 EDICTS OF THE THEODOSIAN CODE.")
5. **§5's causal phrasing, unchanged from Round 2's Cosmetic 5.** Extending `text` cannot move `modern_rendering`; `gates.py` never grades `text`. The rewrite of the rendering was a separate authorial choice, and the regression follows from that.

---

## PART FOUR — CHECKED AND CLEARED

Stated so the record shows what was examined and held. Several of these are things a third round could easily have taken on trust from the first two; I did not.

1. **The word measurement.** Body **129**; bracketed stretches **25 + 14 = 39**; rendered **90**. Exact. The two replaced stretches are precisely the Old- and New-Testament book-lists. Endnote 603 says what the document says it says, including "I have substituted my own **Epitome**." "A canon-list poem with the canon list taken out" is a fair description and an honest one.
2. **Prose, not verse — and now consistently so.** I grepped `worlds/cappadocian/`, `records/cappadocian/` and `cic/corpus-map/` for "verse." Every surviving hit is legitimate: Nazianzen's *verse autobiography* (correct, and correctly left alone in `cappadocian.figure.gregory-of-nazianzus`), the antiphonal "verse against verse" in Doc_05 and story002, the scriptural "verse" in two records, the explicit negations in the corrected files, and unrelated worlds' Tertullian rows. **"240" is gone from every Cappadocian location.**
3. **Ep. 210, both halves.** Independently measured; see Part Two #3.
4. **The Macrina quotation.** Character-level diff against `ix.ccv-p26`: one substitution, `,]` → `.`, exactly as disclosed. Nothing added, dropped or reordered. Line range 37060–37068 exact.
5. **The revised `modern_rendering`.** Faithful — "people … those I took for my fathers" restores the plural of "whomsoever … those I set down as fathers," and "that had been handed down" renders "delivered" without the "to us" Round 2 flagged. **FK 5.55**, ceiling 10. Identical FK to the pre-Revision-2 text, so no readability regression was introduced by the fix.
6. **Every number in §5.** Build succeeds. 18 gates; 17 pass; `voice-perspective` the only failure, one finding, on `cappadocian.dw.reading-scripture`'s "the world's first days." `determinism-check` `pass: true`, `differing_paths: []`. Coverage **26 substantive / 2 honest-limit / 0 empty**. `staleness-check` `pass: false`, `cappadocian` stale on exactly the eight touched records. `pytest` **34 passed, 0 failed**. The insistence that the staleness failure "must not be fixed" remains the most useful sentence in the document.
7. **The corpus-map row.** Both Thaumaturgus rows read exactly as described — second row, `atlas_ids: [cappadocian-nicene-pastoral-monastic-tradition]`, `role: tradition`, `confidence: provisional`, century-gap and no-3rd-c-Pontus reasons in the note, sibling untouched. `corpus_map_merge.py` re-run reports `valid.` and produces a **zero** diff. Nothing here was disturbed by Revision 2.
8. **The Theodosian witnesses, read at source.** `donatism-lpc-integration` exists on the remote and carries all four files; the three named ones are not on `main`, so §1.2's first correction stands. CTh.16.1.3 in the Latin Library text carries all eleven names and the *quos commemoratio specialis expressit* expulsion clause; Mommsen–Meyer carries the same list with `episc(opo)` expansions and visible OCR damage (`conunemoratio`, `pxae-cepti`, `Njsseno`) exactly where the document says; the Latin Library header says "**NOT STATED by the source site**," "**Confidence C**," "do not rely on this file alone for a claim that turns on a constitution's exact wording," and the Mommsen-numbering descent point — all four disclosures quoted accurately. Boyd p. 46 n. 1 exists, lists the eleven sees, and adds independently "**there is no mention of any western bishops**," which supports the document's own second correction.
9. **Doc_04, read rather than taken from the document.** §3.1 line 64 is headed "the decisive moderation"; the §4 matrix row for candidate 8 reads "strong ×5; Formation moderate"; §3.2's entry rates evidence *Documented*; Open Item 1 (line 209) is "flagged for external review"; Open Item 9 (line 217) reads exactly as quoted. Every support §1.3 rests on is where it says it is.
10. **The five-level confidence vocabulary.** `engine/m1/schemas.py` lines 47–52. Five, not four. §1.3's rewritten Cross-Check is right and Round 2's objection on this point does not survive.
11. **62 `verified-direct`.** Counted. Ten of those records carry a 2026-08-31 date and one 2026-08-30, so "some since 2026-08-31" is exact and "stale for over a week" is right.
12. **Registry row 117 and row 65 now agree** with each other, with the record, and with Doc_02 §1.6 — on the epitome, on prose, on Confidence B, and on `verified-via-authority`. The A–B rule quotation is the operative clause, and rows 11/66/69 are named as the consistency check.
13. **No deployment-chunk edit is owed.** I grepped all seven independently. Only `story001` names Amphilochius, as the correspondent who asked for *On the Holy Spirit* — untouched by anything here.
14. **The Registry's sixth-pass log is now accurate.** "the two affected WRS records … corrected alongside" and "All corrected above" are both true statements as of Revision 2, which is what Round 2's Finding 1 required alongside the file fix.
15. **The restraints all held again.** `formation_confidence: Inferential-Thin` unchanged on the figure record; no figure record for Macrina the Elder, with the reason stated; the `voice-perspective` false positive not quietly fixed; Doc_04 not revised; row 65 corrected rather than deleted; the verification builds deleted rather than committed. Every one of these is right, and none of them slipped between revisions.
16. **The escalation posture.** Adding the Amphilochius correction to §6 as a category-4 item, on the skill's actual third trigger, against the pass's own interest, is the right call and is well argued: "That it resolves cleanly is a reason the project lead's decision should be easy, not a reason to skip asking."

---

## PART FIVE — THE BOTTOM LINE

### (a) Is the substance of this pass sound?

**Yes. Unreservedly, and I checked all of it rather than taking it from the two prior reviews.**

- **The five verifications are correct.** CTh 16.1.3 is present in two Latin witnesses plus an independent English discussion, and the eleven-not-four correction is right in both directions the document states it. Firmilian and the Thaumaturgus *Canonical Epistle* are where the document says. The Amphilochius extract is real, is at `div2 17.23`, is 90 rendered words inside a 129-word body, and is the editor's prose epitome rather than the poem. The Macrina-the-Elder datum is in Epp. 204, 210 and 223, with Ep. 210 carrying both halves separately, and the prolegomena cites three letters.
- **The Doc_04 supplemental judgment is sound.** "Supplemental; Open Item 1 marginally re-weighted toward Supporting and left open; Doc_04 not revised" is the right answer, argued from Doc_04's own text, with the baptism/festival objection engaged rather than routed around, and with the Cross-Check re-run described honestly as an outcome that was never in doubt. Escalating rather than actioning is right.
- **The Amphilochius correction is right in every operative particular** — Confidence B against the Registry's own A–B rule, `verified-via-authority` against this world's own mapping rule, row 65 narrowed rather than deleted, `Inferential-Thin` deliberately unchanged, the availability claim named rather than quietly rewritten. Only the precedent *citation* inside the record is wrong (New Finding 1), and that is a sentence, not the grade.
- **The Macrina quote is safe to keep.** Verbatim, one disclosed substitution, the Newman-bracket boundary correctly located and correctly explained, the C-E fit argued with the objection rather than around it, and the `tensions` line on the witness record doing real work.
- **The corpus-map row is correct and idempotent**, and the Firmilian split is correctly escalated rather than made.

Nothing in the change set needs to be reverted. Nothing compiled is wrong on a matter of fact about a primary text.

### (b) Is the remaining defect set cosmetic or substantial?

**Substantial — but only just, and for a reason that is about the pattern rather than about any single item's weight.**

Applying the skill's own test — *"substantial if it changes a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary — anything a careful reader would notice as actually different"*:

- New Finding 1 leaves a **false sourcing justification in compiled content** and a document claiming it was removed. Substantive on both halves.
- New Finding 2 reports a **command result the command does not produce**, in the sentence written to replace a false completeness claim that two prior reviews rejected.
- New Finding 3 leaves **three cleared master documents disagreeing** on the pass's own headline correction, and thereby leaves an escalation category untested.
- New Finding 7 leaves **a record and the Registry row that indexes it citing different sources**, against the skill's explicit propagation rule.

Findings 4, 5 and 6 are each a single-line fix, and Findings 5's and 6's substance is administrative. If Findings 1, 2, 3 and 7 were the whole list, a fair reading of the *Revision decision* rule might allow them as direct fixes. They are not the whole list, and that is the point: **this is the third consecutive round in which a review has had to report that a correction the document says was made was not made in the file.** Round 1 found six such claims. Round 2 found six more, three of them created by the fixes for Round 1. Round 3 finds three more, two of them created by the fixes for Round 2. The failure rate of "asserted as done" is not improving, and it is not distributed randomly — it lands on precisely the sentences a revision writes about its own completeness.

So the finding I would put to the project lead is not any of the seven. It is this: **the substance of this pass has been right since Revision 1 and has survived three adversarial rounds intact, while the pass's account of its own work has been wrong in every round.** That is a process defect, not a scholarship defect, and the remedy is procedural — before the next revision claims a fix landed, open the file; before it reports a grep, paste the grep; before it decomposes a number, count every part of it.

**One more round is required, and it should be a short one.** Every finding above names a file, a line, and the replacement text. A revision that makes those seven edits and then re-runs its own claimed greps — rather than describing them — should return clean.

---

## CLOSING VERDICT

**Substantial revision still required.** Seven new substantial findings (Nos. 4, 6 and 7 narrow) and five cosmetic. Of Round 2's sixteen: twelve answered, one answered wrongly, one partially, two not answered. Three of Round 1's findings (8e, 8h, 8i) remain open after two revisions and have never been either fixed or declined on the record.

What Revision 2 got right should not be lost in the count, and it is more than the count suggests. The Ep. 210 locus, the "for the first time" withdrawal, the §1.3 reconciliation, the Cross-Check rewrite, the category-4 retest, the row 65 and own-works corrections, the pytest number, the `modern_rendering` faithfulness, and the escalation of the Amphilochius correction against the pass's own interest are all correct, and several are better than what was asked for. The Cross-Check paragraph in particular now says the thing that is hardest to say — that its own result was never in doubt — and Round 2's objection to its vocabulary turns out to have been the looser claim of the two.

The lesson each round has drawn has been the right lesson and has then been applied one step short of where it reaches. Round 1: *never assert a text does not exist without grepping the volumes the Registry already cites.* Round 2: *never assert a fix landed without opening the file it landed in.* Round 3's is the same sentence with one word changed: **never report the output of a command you have described instead of run.** The three findings at the head of this review are one grep, one `sed -n 139p`, and one `git diff` away from having been caught by the pass itself.
