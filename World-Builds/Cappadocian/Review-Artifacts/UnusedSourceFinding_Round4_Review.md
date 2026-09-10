# Unused-Source Finding — Round 4 Independent Adversarial Review

**Document under review:** `World-Builds/Cappadocian/cappadocian_Unused_Source_Verification_2026-09-09.md` at **Revision 3**, together with the change set it dispositions (commit `7c3ae3d` on top of `f8d10ca`; 10 files in this commit, 20 against the base `f07eb91`).
**Reviewer stance:** Independent adversarial. Did not author the document, the change set, or any of the three prior reviews; no stake in its passing.
**Review date:** 2026-09-09.
**Branch reviewed:** `claude/cappadocian-unused-source-finding`.
**Prior reviews:** Round 1 (14 substantial, 4 cosmetic — substantial revision required); Round 2 (11 new substantial, 5 cosmetic, plus 5 of Round 1's not fully answered — substantial revision still required); Round 3 (7 new substantial, 5 cosmetic, plus 4 of Round 2's not fully answered — substantial revision still required, "but only just").
**Consulted:** the three prior reviews in full; `CAPPADOCIAN_BUILD_LEDGER.md` §50 with all three revision addenda; `cappadocian_Doc_02_Source_Ecology.md`; `cappadocian_Source_Registry.md`; `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md`; `cappadocian_Integrated_Ecology_Analysis.md`; `cic/texts/npnf214_seven-ecumenical-councils.xml`; `cic/texts/npnf208_basil-letters-select-works.xml`; `cic/corpus-map/_staging/npnf214_seven-ecumenical-councils.yaml`; `World-Builds/Cappadocian/scripts/wb_cappadocian_s21.py`; the eight touched records; the `cic-build-cycle` *Revision decision* rule as quoted in all three prior reviews.

---

## VERDICT: **SUBSTANTIAL REVISION STILL REQUIRED**

Three new substantial findings; of Round 3's twelve findings (7 substantial, 5 cosmetic), **four answered, two answered wrongly, two partially, four not answered**.

The credit first, and it is real. **Two of Round 3's three headline items landed properly and I confirmed both by opening the files.** The `basil-against-eunomius` precedent is genuinely gone from `cappadocian.source.amphilochius-iambics-to-seleucus.md`'s `divergence_note` — I rebuilt the package and the string `already corrected cappadocian.source.basil-against-eunomius` is no longer in `compiled/repository.json`. `wb_cappadocian_s21.py:1073` now emits the eleven-bishop form, matching the hand-corrected record's `work:` field word for word, and the script still compiles (`py_compile` clean). A repo-wide `grep -rn "Helladius, Otreius, Gregory of Nyssa, and Amphilochius" .` returns four hits, all of them quotations inside the three review artifacts — nothing live anywhere. `cappadocian_Integrated_Ecology_Analysis.md:139`, named by file and line in Round 1 and again in Round 2 and fixed in neither, is now fixed, and the replacement is accurate: "writes four of this world's own bishops into the empire's own communion test — the law names eleven eastern bishops and makes communion with them the condition of holding a church, not this world's men the test." That is Doc_01 §4a's and Doc_02 §2's bounded form, and the last of the three cleared master documents now agrees with the other two, which retires the escalation-category-2 trigger Round 3 raised. Doc_02 §1.4 now names Ep. 210 (Round 1's 8i, half of it), and the G1 manifest's Amphilochius gap is qualified rather than left unconditional (Round 1's 8h, closed). The broken "a roughly / extract" sentence is repaired.

**And I re-ran the whole battery and every number in §5 reproduces.** Build succeeds; 18 gates, 17 pass, `voice-perspective` the single failure on `cappadocian.dw.reading-scripture`'s "the world's first days"; `determinism-check` `pass: true`, `differing_paths: []`; coverage 26 substantive / 2 honest-limit / 0 empty; `staleness-check` `pass: false` with `cappadocian` the only stale world; `pytest engine/m1/tests engine/m2/tests` 34 passed, 0 failed. Package deleted. The Macrina quotation is still verbatim against `ix.ccv-p26` with **exactly one** substitution — a `,` replaced by a `.` at the bracket's close, precisely as disclosed — and `modern_rendering` scores **FK 5.55** against the `readability` ceiling of 10. Body **129**, bracketed **25 + 14 = 39**, rendered **90**: all three exact.

**Then the through-line runs for a fourth round, in the same shape, at the same rate.** Round 3's own count was "Round 1 found six such claims; Round 2 six more, three created by the Round 1 fixes; Round 3 three more, two created by the Round 2 fixes." Round 4 finds **three more, two of them created by the Round 3 fixes**:

- **`cappadocian_Source_Registry.md` row 11 was never touched.** It reads `Basil, Epp. 204 and 223` at `HEAD`, byte-identical to `f07eb91`, `88f9dd4`, `5cae808` and `f8d10ca`. The verification document's §1.5 lists "Source Registry rows 11 and 79" among occurrences corrected; ledger §50's Revision 3 addendum says "**Round 1's 8i and 8h closed at last**: Registry row 11 and Doc_02 §1.4 now name Ep. 210 alongside 204 and 223, matching the record"; the commit message says "Round 1's 8h and 8i closed at last (Registry row 11, Doc_02 s1.4, G1)." Three assertions, one `sed -n 50p` apart from being caught.
- **The false clause Round 3 named was relocated, not withdrawn.** §1.5 now reads "the G1 manifest (**which now carries the full eleven, making Doc_02 line 37's pointer to it true for the first time**)." The G1 manifest contains no bishop names and no "eleven" at all; Doc_02 line 37 points at **§2**, and returns the same md5 at all five commits. Both halves false, of a different file than last round. The ledger meanwhile states this claim was *withdrawn* — and misattributes it to Doc_02 §2, when Revision 2 attached it to Doc_02 §7.
- **The word count is wrong for the third consecutive revision**, and this time the error is used to license declining to reconcile with a figure that reconciles exactly. Details at New Finding 1; the short form is that `div2 17.23` is **240/242** words, not 279, and its closing "Note." is **51**, not 87.

The honesty of the pass has not slipped and is not in question. It still names its own regression, its own punctuation substitution, its own defect class, its own repeated failure, and it still claims no disposition. But Round 3's diagnosis — *the substance has been right since Revision 1; the pass's account of its own work has been wrong in every round* — is now true of four rounds rather than three, and Revision 3 has for the first time pushed a wrong measurement of a primary text into **compiled** content.

---

## PART ONE — WHAT I INDEPENDENTLY RAN OR READ

Nothing below rests on the document's or a prior review's account of it.

**The Amphilochius `div2`.** Read lines 44075–44103 of `cic/texts/npnf214_seven-ecumenical-councils.xml` (the `<div2 … id="xvii.xxiii">` through its `</div2>`; the next `div2`, `xvii.xxiv`, opens at 44104). Counted every constituent part programmatically under both markup-stripping conventions, then swept the end boundary line by line from 44103 to 44111 to find what convention could produce 279 and 87.

**The corpus map's convention.** Read the `_staging` row (`locus: div2 17.23 (~242 words)`) and its immediate neighbour (`div2 17.24 (~629 words)`), then measured `div2 17.24` the same way.

**The Macrina quotation.** Parsed the record's front matter, stripped markup from lines 37060–37068 of `npnf208`, and ran a character-level `SequenceMatcher` over the aligned window; computed `fk_grade` on `modern_rendering` with `engine.m1.fk`.

**Compile and gates.** `python -m engine.m2.cli build cappadocian` (package `2026-09-09T02-51-52Z`, since deleted); parsed `validation/gates-report.json` and `compiled/coverage.json`; `determinism-check cappadocian`; `staleness-check`; `pytest engine/m1/tests engine/m2/tests`; grepped `compiled/repository.json` for the withdrawn precedent, for `279`, and for `ledger SS47`.

**File-by-file verification of every fix Revision 3 claims.** `git show <commit>:<path>` at `f07eb91`, `88f9dd4`, `5cae808`, `f8d10ca` and `HEAD` for Registry row 11 and Doc_02 line 37; `sed -n` on Doc_02 lines 37, 42, 57 and 112; Registry rows 11, 79 and 117; G1 line 92; IEA line 139; the two edited records in full.

**The generator.** `python3 -m py_compile World-Builds/Cappadocian/scripts/wb_cappadocian_s21.py`; read the `emit_source(79, …)` call and compared each emitted field against the current record.

**The three review files.** Read Round 1, Round 2 and Round 3 in full, including their closing pattern paragraphs, to check the ledger's counts against them rather than against Round 3's summary of them.

---

## PART TWO — JOB 1: WAS EACH ROUND 3 FINDING ANSWERED?

### The seven substantial

| # | Round 3 finding | Verdict | Evidence |
|---|---|---|---|
| 1 | The `basil-against-eunomius` precedent still stood in a compiled `divergence_note` | **ANSWERED** | `grep -n basil-against-eunomius records/…amphilochius-iambics-to-seleucus.md` returns nothing; I rebuilt and the string is absent from `compiled/repository.json`. The surviving precedent (`cappadocian.quote.basil-against-delaying-baptism`) is the correct one. One blemish created by the edit — Cosmetic 5 below. |
| 2 | §1.5 reports a grep result the grep does not produce; `wb_cappadocian_s21.py:1073` still carried the four-name string | **ANSWERED** | Line 1073 now emits "eleven eastern bishops … among them four of this world's own circle (Amphilochius of Iconium; Helladius of Caesarea, Otreius of Melitene, Gregory of Nyssa)" — matching the record's `work:` exactly. Script compiles. Repo-wide grep returns only the three review artifacts. The document's sentence is still literally over-broad — Cosmetic 2. |
| 3 | `Integrated_Ecology_Analysis.md:139` untouched after two revisions | **PARTIALLY ANSWERED** | Line 139 is fixed and the replacement is accurate and correctly cited to Doc_02 §2 "corrected 2026-09-09." The trigger-2 contradiction Round 3 raised is gone. **Not done:** the second half of Round 3's fix, which was Round 2's request repeated — "say on the record that 161 and Doc_05 §29 were considered and left as acceptable summary." Nothing in §1.5, §6 or ledger §50 records that judgment. Third round of asking. |
| 4 | The corrected decomposition is wrong; the Note is 51 words, and 59/242 mix two conventions | **ANSWERED WRONGLY, and worse than before** | Replaced with 279 = 63 + 129 + 87, which is wrong on three of four parts, and with a declaration that the corpus map's figure is irreconcilable, which is false. See New Finding 1. |
| 5 | Status line and §7 say "Revision 1" and await a review that has returned | **PARTIALLY ANSWERED** | §7 is fully corrected ("this is Revision 3 answering Round 3 … No disposition is claimed until a review returns without calling for substantial revision"). The `**Status:**` line at line 6 now says Revision 3 and cites all three reviews — and still ends "**and it awaits a Round 2 review.**" The ledger says this was "Corrected." |
| 6 | §1.5's two claims about Doc_02 §7 and Doc_02 line 37 are both wrong | **ANSWERED WRONGLY** | The Doc_02 §7 half is fixed correctly and I verified line 112 ("the count and the four names of ours, pointing to §2"). The line-37 half was **moved to the G1 manifest**, where it is false in both halves. See New Finding 3. |
| 7 | Record `work:` now cites 204/210/223 against Registry row 11's and Doc_02 §1.4's 204/223 | **NOT ANSWERED, and asserted answered** | Doc_02 §1.4 (line 42) is fixed. **Registry row 11 (line 50) is byte-identical to the base commit.** Round 1's 8i is still open after three revisions. See New Finding 2. |

### The five cosmetic

| # | Round 3 cosmetic | Verdict | Evidence |
|---|---|---|---|
| 1 | "a roughly / extract" broken sentence | **ANSWERED** | `amphilochius-of-iconium-own-works.md` line 40 now reads "That was false at the time it was written: an extract of his own argument…" |
| 2 | The Round 2 `modern_rendering` edit is disclosed nowhere | **NOT ANSWERED** | §4 line 115 still names only the two Round 1 glosses ("your own city"; "with them"). Neither §4, nor §5's regression paragraph, nor ledger §50 records that a compiled field was edited a second time, in a document whose §5 says "Recorded rather than silently fixed." |
| 3 | "Stale" is the wrong word for ledger §47, which was wrong when written | **NOT ANSWERED** | §3 (line 91) and §6.7 (line 158) are verbatim unchanged; §3 still paraphrases §47 rather than quoting it. |
| 4 | "all eleven names" overstates the vendored Boyd, whose scan corrupts two personal names | **NOT ANSWERED** | §1.5 line 65 is verbatim unchanged: "with Boyd's independent English note listing the same eleven." |
| 5 | §5's causal phrasing — extending `text` cannot move `modern_rendering` | **NOT ANSWERED, third round** | Line 136 is verbatim unchanged. Round 2 Cosmetic 5, Round 3 Cosmetic 5, still standing. |

**Count: 4 of 12 answered; 2 answered wrongly (4, 6); 2 partially (3, 5); 4 not answered (7, and cosmetics 2, 3, 4, 5).**

---

## PART THREE — JOB 2: NEW DEFECTS INTRODUCED OR LEFT BY REVISION 3

### 1. [SUBSTANTIAL] The word count is wrong for the third revision running — and the new "these figures do not reconcile" verdict is false. The corpus map's ~242 is exactly the `div2`, its convention is reproducible from the file, and the 279 figure was taken by reading past the end of the section into the next one.

**Location:** verification document §3 (line 89); Doc_02 §1.6 (line 51); Source Registry row 117 (line 217); `cappadocian.source.amphilochius-iambics-to-seleucus.md` `divergence_note` — **compiled**; ledger §50 Revision 3 addendum.

> "a direct measurement of the same `div2` (tags stripped, whitespace split, from element `xvii.xxiii` to `xvii.xxiv`) gives **279** — 63 words of numeral, heading and the editor's method note, the **129-word extract body**, and 87 words of closing editorial 'Note.' … **The two figures do not reconcile, and this pass stopped trying to make them:** they use different counting conventions and the corpus map's is not documented."

Measured from the file, every part, under both conventions. The section runs from `<div2 … id="xvii.xxiii">` at line 44075 to its `</div2>` at line 44103; `xvii.xxiv` opens at 44104.

| part | strip-with-space | strip-without-space |
|---|---|---|
| "VIII." numeral | 1 | 1 |
| heading + endnote 603 | 61 | 59 |
| **extract body** | **129** | **129** |
| "Note." label | 1 | 1 |
| closing Note prose | 50 | 50 |
| **whole `div2`** | **242** | **240** |

So: head (numeral + heading + note) is **62 or 60**, not 63. The closing "Note." is **51**, not 87. The whole section is **242 or 240**, not 279. Only the body is right.

**And the corpus map reconciles exactly — its convention is not undocumented, it is reproducible.** `~242` is the whole `div2` under strip-with-space, to the word. I checked the convention against the next row of the same file rather than inferring it: the corpus map records `div2 17.24 (~629 words)` for the Canonical Answers of Timothy, and that section measures **629** under strip-with-space (610 without). Two rows, two exact matches. Round 3 had already handed this pass the whole reconciliation, including a token-level diff identifying the two orphaned punctuation marks (`<i>Synodicon</i>,` and `<i>Epitome</i>.`) that separate 240 from 242. Revision 3 discarded a correct, supplied reconciliation and substituted a wrong measurement plus a refusal to reconcile.

**Where 279 comes from.** Sweeping the end boundary line by line: 44103 → 240/242; 44105 → 241/243; 44106 → 247/249; 44107 → 260/262; 44108 → 270/272; 44109 → 274/276; 44110 → 280/282. The 279-family appears only once the count has run past `</div2>` and into `xvii.xxiv` — "IX.", the Timothy of Alexandria heading, and endnote 604. The same over-run inflates the "closing Note" block from 51 to 85–91, which is where 87 sits. The stated method ("from element `xvii.xxiii` to `xvii.xxiv`") is the error in plain sight: the section ends *before* `xvii.xxiv`, not at it.

**Is declining to reconcile the honest call?** No. Declining to reconcile is honest when two good-faith measurements genuinely disagree and the reason cannot be established. Here there is no disagreement: the corpus map measured the section correctly, and this pass measured a different span. The paragraph is headed "**measured rather than estimated**" in a document whose central correction is that a number was reported without being measured, and it now tells a reader that a correct index figure is unreliable. A reader needs the opposite sentence.

**Why it is substantial and not arithmetic pedantry.** It is a claim's substance about a primary text, it stands in a **cleared master document** (Doc_02 §1.6) and in the Source Registry, and it is now in **compiled** content — I grepped the built package and `compiled/repository.json` contains `gives 279`. Round 3's Part Five could say "nothing compiled is wrong on a matter of fact about a primary text." After Revision 3 that is no longer true.

**Fix.** In all four locations: "the whole `div2` runs to **240** words as ordinarily counted, or **242** under the tags-stripped-to-a-space convention the corpus map uses — 60 (62) words of section numeral, editor's heading and method note, the **129-word extract body**, and a **51-word** closing editorial 'Note.' on the four scriptural canons. The corpus map's `~242` is that section measured the second way; its sibling row's `~629` for `div2 17.24` measures 629 the same way, which is how the convention was identified." Then delete the "do not reconcile" sentence.

---

### 2. [SUBSTANTIAL] Source Registry row 11 was never edited, and three separate documents say it was. Round 1's Finding 8i is open after three revisions, and a record still cites different sources from the Registry row that indexes it.

**Location:** `cappadocian_Source_Registry.md` line 50; asserted fixed at verification document §1.5, ledger §50 Revision 3 addendum, and the commit message.

Row 11 at `HEAD`:

```
| 11 | Basil, Epp. 204 and 223 (Macrina the Elder, transmission of Gregory Thaumaturgus' teaching) | P | B | Native | …
```

I took the md5 of that line at `f07eb91`, `88f9dd4`, `5cae808`, `f8d10ca` and `HEAD`. Identical at all five. Nothing in this pass has ever touched it.

Against `cappadocian.source.basil-macrina-the-elder-letters.md`, whose `external_ids.cappadocian_source_registry_row` is **11**:

```
work: Basil, Epistles 204, 210 and 223 (Macrina the Elder, transmission of Gregory
  Thaumaturgus' own teaching). Epistle 204 alone joins the two; 210 carries each
  separately; 223 corroborates
```

This is precisely the gap the skill's *Naming and term propagation* rule is written against — "a fix that lands in the narrative document without the index being updated to match is not a complete fix" — and it is the third round it has been named (Round 1 Finding 8i; Round 2 NOT ANSWERED; Round 3 New Finding 7). It is worse than it was in one respect: Doc_02 §1.4 has now been corrected, so the Registry row is the sole survivor of the old citation and the sole disagreement with the record it indexes.

**And it is asserted fixed in three places.** §1.5: "Occurrences corrected: … Source Registry rows 11 and 79." Ledger §50: "**Round 1's 8i and 8h closed at last**: Registry row 11 and Doc_02 §1.4 now name Ep. 210 alongside 204 and 223, matching the record." Commit message: "Round 1's 8h and 8i closed at last (Registry row 11, Doc_02 s1.4, G1)." The `git diff HEAD~1` on `cappadocian_Source_Registry.md` is a single hunk, on row 117.

**Fix.** Row 11's work column to `Basil, Epp. 204, 210 and 223 (Macrina the Elder, transmission of Gregory Thaumaturgus' teaching)`, with a dated note matching Doc_02 §1.4's. Then re-check the three claims that say it is done.

---

### 3. [SUBSTANTIAL] The false "Doc_02 line 37's pointer" clause was moved to a different file rather than withdrawn, and is false about that file too. The ledger simultaneously reports it withdrawn and misattributes it.

**Location:** verification document §1.5 (line 63); ledger §50 Revision 3 addendum, fifth bullet.

Revision 2 said "Doc_02 §7 (which now carries the full eleven, making Doc_02 line 37's pointer to it true for the first time)." Round 3 established that both halves were false. Revision 3 fixed the Doc_02 §7 half — and re-attached the second half to a new antecedent:

> "…`World-Builds/Cappadocian/scripts/wb_cappadocian_s21.py` line 1073, **the G1 manifest (which now carries the full eleven, making Doc_02 line 37's pointer to it true for the first time)**, Doc_02 §2's own 'the world's own men made the empire's standard' conclusion…"

Both halves are false of the G1 manifest as well:

- `grep -n "eleven\|Nectarius\|Terennius\|Marmarius\|Optimus\|Pelagius\|Diodore" cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md` returns **nothing**. G1 carries no bishop names and no count. Revision 3's only edit to it is the Amphilochius-gap qualification at line 92, which is a good fix and unrelated.
- Doc_02 line 37 reads "see **§2** for the law's own full citation and bishop list," md5-identical at all five commits. It has never pointed at G1.

For completeness, because the sentence next to it makes a similar claim and I checked it too: **"Doc_02 §2 (which now carries all eleven names and the law's mechanism)" is TRUE.** Line 57 carries Nectarius, Timothy, Pelagius, Diodore, Amphilochius, Optimus, Helladius, Otreius, Gregory, Terennius and Marmarius, the expulsion mechanism, and "No western bishop is named." So Doc_02 §7's pointer to §2 and line 37's pointer to §2 are both true, and were made true by Revision 1's rewrite of §2 — exactly as Round 3 said.

**And the ledger reports the opposite of what happened.** Ledger §50: "**Two claims about the sweep are withdrawn**: that Doc_02 **§2** 'makes line 37's pointer true for the first time' (line 37 points at §2 and was already correct, byte-identical across every commit in this pass), and the completeness claim above." Three errors in one bullet: the claim was attached to Doc_02 **§7**, not §2; it was not withdrawn but relocated; and the completeness claim was not withdrawn either — §1.5's "a grep … now returns nothing" is byte-identical to Revision 2's.

**Fix.** Delete the clause: "…the G1 manifest, Doc_02 §2's own conclusion…". Then correct the ledger bullet to say what was actually done — the *Doc_02 §7* claim was corrected, the line-37 claim is deleted rather than relocated, and the completeness sentence was made true by fixing the script rather than withdrawn.

---

### COSMETIC

1. **The `**Status:**` line still ends "and it awaits a Round 2 review."** Line 6 opens correctly ("Revision 3 … after three independent adversarial reviews") and then closes with the sentence Round 3 named. §7 is fully correct, so the document contradicts itself about its own standing, and ledger §50 says the line was "Corrected." One clause: "…and it awaits a Round 4 review."
2. **§1.5's completeness sentence is still stated more broadly than the grep supports.** "a grep for the four-name string across `World-Builds/Cappadocian/` and `records/cappadocian/` now returns nothing" — it returns three review artifacts under the first of those paths. Round 3 ruled quotations acceptable and I agree; the ledger words it correctly ("nothing outside the review artifacts"), and the document should use the ledger's wording.
3. **`cappadocian.source.basil-macrina-the-elder-letters.md`'s `discovery_channel` still says "both cited letters."** Its `work:` now names three. A compiled field left behind by Revision 2's `work:` edit, in the same record. "all three cited letters."
4. **The generator would still regenerate a superseded record.** Row 79's `work` now matches, but `emit_source(79, …)` still passes `named-not-rechecked` and the short pre-verification `edition`, so a re-run would undo this pass's central corrections to that record. The ledger's "a re-run of that script no longer regenerates the wrong value" is true of the one string and misleading about the file; one clause naming the script as a superseded first-pass generator would settle it.
5. **"(ledger SS47)" reads as a mangled "§47" in a compiled field.** The record is otherwise ASCII-consistent, so this is a house-style question rather than an error, but it is compiled content: `compiled/repository.json` carries the literal string `ledger SS47`.
6. **Round 3's cosmetics 2, 3, 4 and 5 are all untouched** and are listed in Part Two rather than repeated here. Number 5 (§5's causal phrasing) is now in its third round unanswered and is a one-clause fix.

---

## PART FOUR — CHECKED AND CLEARED

Stated so the record shows what was examined and held, including things a fourth round could have taken on trust from the first three.

1. **The precedent withdrawal actually landed.** The record's `divergence_note` now cites only `cappadocian.quote.basil-against-delaying-baptism`, which is the correct precedent, and the compiled package no longer carries the wrong one. §3's "The citation is withdrawn here" is now a true statement.
2. **The generator fix landed and is faithful.** Line 1073's new string matches the record's `work:` field exactly; `py_compile` is clean; the repo-wide grep is live-clean.
3. **IEA:139 is fixed and the replacement is accurate.** It matches Doc_01 §4a's "written into … not themselves that test" and Doc_02 §2's bounded form, and it cites Doc_02 §2 correctly with the correction date. The three cleared master documents now agree, so escalation trigger 2 no longer fires and §7's category-4 bullet does not need to reach it.
4. **Doc_02 §2 does carry all eleven names, the addressee, the mechanism and "No western bishop is named."** Verified at line 57. Doc_02 §7 (line 112) carries the count, this world's four, and a pointer to §2 — the shape Round 3 asked for.
5. **G1's Amphilochius gap is properly qualified** (Round 1's 8h): "remain an honest gap *as a corpus*, but not absolutely — about 90 rendered words … at Source Registry row 117."
6. **Doc_02 §1.4 names Ep. 210** with the correct discrimination (unnumbered opening carries the upbringing; §3 the transmission; only 204 joins them).
7. **The body/bracket/rendered measurement.** Body **129**; the two bracketed stretches **25** and **14**, total **39**; rendered **90**. The two replaced stretches are exactly the Old- and New-Testament book-lists. "A canon-list poem with the canon list taken out" is fair and honest. These are the load-bearing figures and they have been right since Revision 1.
8. **The Macrina quotation.** Character-level diff against the vendored text: one opcode, `,` → `.`, at the close of the Newman bracket, exactly as disclosed. Nothing added, dropped or reordered. `modern_rendering` at **FK 5.55**, ceiling 10, so no readability regression survives.
9. **Every number in §5.** Build succeeds; 18 gates, 17 pass, `voice-perspective` the one failure with the one finding on "the world's first days"; `determinism-check` `pass: true` with an empty `differing_paths`; coverage 26/2/0; `staleness-check` `pass: false`, `cappadocian` the only stale world; `pytest` 34 passed, 0 failed. The insistence that the staleness failure "must not be fixed" remains the best sentence in the document.
10. **Ledger §50's pattern counts survive checking against the three review files.** Round 1's closing paragraph does say "every one of the six most serious findings above" and enumerates exactly six. Round 2's closing paragraph does say Revision 1 "made six new claims of exactly this kind" and enumerates its New Findings 1, 2, 3, 7, 6 and 8. Round 3 does find three and does attribute two of them to the Round 2 fixes. The "three of them created by the Round 1 fixes" attribution in the middle clause is Round 3's own gloss rather than Round 2's, and Round 2's material would arguably support four — an error in the direction of understating the pass's own defect count, but a small one, and the counts as stated are sourced and defensible. **This is not where the ledger overclaims; New Findings 2 and 3 are.**
11. **The restraints all held again.** `formation_confidence: Inferential-Thin` unchanged; no figure record for Macrina the Elder; the `voice-perspective` false positive still not quietly fixed; Doc_04 not revised; row 65 corrected rather than deleted; row 117 at B; the new source record at `verified-via-authority`; the verification build deleted rather than committed. Four rounds, no slippage on any of them.
12. **The document still claims no disposition**, still escalates the Amphilochius correction against its own interest, and §7 now states the disposition condition correctly.

---

## PART FIVE — THE BOTTOM LINE

### (a) Is the substance still sound?

**Yes, in every operative particular — with one new exception that Revision 3 introduced.**

The five verifications, the Doc_04 supplemental judgment, the Amphilochius grade (B / `verified-via-authority`), the Macrina quote and its C-E placement, the corpus-map row, and the escalation posture are all correct and are now three times independently re-verified. Nothing needs reverting. The Amphilochius conclusion that carries weight — about **90 rendered words** inside a **129-word** body, of which **39** are the editor's brackets, being a canon-list poem with the canon list removed — is exact, and I measured it myself.

The exception: **the `div2`'s overall size is now misstated in compiled content**, and the corpus map is wrongly described as unreconcilable. That is a fact about a primary text, in the Representative's repository, in a cleared master document and in the Source Registry. It does not touch the conclusion, and it is a smaller error than the two it replaced — but Round 3 was able to write "nothing compiled is wrong on a matter of fact about a primary text," and Round 4 cannot.

### (b) Cosmetic, or substantial?

**Substantial. Not "only just" this time, and not on the strength of the pattern — on the strength of the individual items, applied literally against the skill's test.**

*"Substantial if it changes a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary — anything a careful reader would notice as actually different."*

- **New Finding 1** changes a **claim's substance**: three of four stated measurements of a primary text are wrong, the whole-section figure by 37–39 words, and the document tells a reader that a correct index figure cannot be reconciled when it reconciles to the word. Fixing it changes what four documents say, one of them compiled. This is not wording, tone, formatting, or a typo.
- **New Finding 2** is a **sourcing conclusion**: a record and the Registry row that indexes it cite different sources for the same datum, which is what the *Naming and term propagation* rule exists to prevent, and three documents assert it was fixed. A reader consulting row 11 gets the wrong citation for this world's "single most valuable non-male-mediated female datum."
- **New Finding 3** is a **claim's substance** about two named files, false in both halves, in the sentence that documents the sweep's completeness — the same sentence a review has now had to correct in three consecutive rounds.

Any one of those three would clear the bar on its own. Round 3's remainder could fairly have been argued down to direct fixes; this one cannot, because the largest item is a wrong measurement of a primary text sitting in compiled content, and because two of the three findings are false claims that a fix landed — the class the *Revision decision* rule cannot absorb, since applying such a fix "directly" is exactly what produced them.

I want to be explicit that I looked for a reason to say the opposite. The battery all reproduces. The quote is verbatim. The load-bearing counts are exact. Both of Round 3's headline compiled-content items landed properly. If the word count had been right, or had honestly said "I measured 240/242 and the corpus map agrees," I would have called the remainder administrative and said so plainly. It is not right, and its error is of the same species as the one it was told to fix.

**One more round, and it should be very short.** Three edits, all of them named here by file and line with replacement text, plus six cosmetics. What would make Round 5 different from Rounds 2, 3 and 4 is not more care in the fixing — the fixing has been careful each time — but a single mechanical step: **after the edits, re-read the passage that describes them, and for every file it names, open that file.** Rounds 2, 3 and 4 have each been won by `sed -n <line>p` and `git show <commit>:<path>`, run against the revision's own account of itself.

### (c) If it were cleared, what should a reader still know is imperfect?

I am not clearing it. Stated anyway, because these will survive the fix of the three findings above and a reader should have them:

- **The `div2`'s size has been stated four different ways in four drafts** (~240, then 59+129+~54=242, then 63+129+87=279, and the correct 60/62+129+51=240/242). Whatever number ends up in the file, a reader should know its history and should trust the **129 / 39 / 90** decomposition, which has never moved and which three reviewers have now independently measured.
- **`wb_cappadocian_s21.py` is a superseded first-pass generator.** Re-running it would restore `named-not-rechecked` and the pre-verification `edition` on row 79 and clobber much else. It is not part of the compile path and nothing runs it, but its existence is a live foot-gun and only its `work` string has been brought into line.
- **The world is stale on purpose.** The pin `packages/cappadocian/2026-09-04T16-41-51Z` does not contain any of these changes; `staleness-check` correctly fails; nothing here is live until Mark authorizes the recompile-and-re-pin. The document says this well and it is the most important thing in it.
- **The compiled `modern_rendering` was edited twice and disclosed once.** The Round 1 glosses are recorded in §4; the Round 2 rendering rewrite is recorded nowhere.
- **The two Latin witnesses may not be independent**, Boyd's vendored scan corrupts two of the eleven personal names, and the Latin quoted at §1.1 is normalized rather than transcribed. The document discloses the first and third carefully and the second not at all.
- **Six deferred items still need the project lead**, including two Doc_04 open-list re-weightings and ledger §47's precedent citation, and none of them has been seen by him.

---

## CLOSING VERDICT

**Substantial revision still required.** Three new substantial findings and six cosmetic. Of Round 3's twelve: four answered, two answered wrongly, two partially, four not answered. Round 1's Finding 8i is open after three revisions; Round 2's Cosmetic 5 is open after two.

What Revision 3 got right is genuinely more than the count suggests, and two of its three hardest items — a precedent withdrawn from compiled content, and a generator that would have regenerated a corrected value — landed cleanly and I verified both by building the package. The `Integrated_Ecology_Analysis.md:139` fix closes a finding that survived two prior revisions and retires an escalation trigger with it. G1's gap qualification and Doc_02 §1.4's Ep. 210 close two of Round 1's three long-open items.

But the sentence Round 3 wrote as its lesson — *never report the output of a command you have described instead of run* — has an exact fourth-round successor, and it is narrower still: **when a review tells you a clause about a named file is false, delete the clause; do not re-point it at a different file.** The G1/line-37 claim, the Registry row 11 claim, and the 279-word measurement are one `grep`, one `sed -n 50p`, and one careful reading of where `</div2>` sits away from having been caught by the pass itself — and in the third case, away from discovering that the figure it declared irreconcilable reconciles exactly.
