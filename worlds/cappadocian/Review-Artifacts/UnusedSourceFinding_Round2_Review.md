# Unused-Source Finding — Round 2 Independent Adversarial Review

**Document under review:** `worlds/cappadocian/cappadocian_Unused_Source_Verification_2026-09-09.md` at **Revision 1**, together with the whole change set it dispositions (commit `5cae808` on top of `88f9dd4`; 18 files against the base `f07eb91`).
**Reviewer stance:** Independent adversarial. Did not author the document, the change set, or the Round 1 review; no stake in its passing.
**Review date:** 2026-09-09.
**Branch reviewed:** `claude/cappadocian-unused-source-finding`.
**Prior review:** `Review-Artifacts/UnusedSourceFinding_Round1_Review.md` — 14 substantial, 4 cosmetic findings, verdict SUBSTANTIAL REVISION REQUIRED.
**Consulted:** `cic-build-cycle` SKILL.md (read in full — the four escalation categories verbatim, the *Revision decision* rule, and the *Naming and term propagation* rule); `cappadocian_Doc_04_Gravity_Discovery.md` §§3.1, 3.2, 9; `CAPPADOCIAN_BUILD_LEDGER.md` §§47, 50; `cappadocian_Source_Registry.md`; `cic/corpus-map/README.md` and the two `_staging` files; `engine/m1/gates.py`, `engine/m1/fk.py`.

---

## VERDICT: **SUBSTANTIAL REVISION STILL REQUIRED**

Eleven new substantial findings; five of Round 1's eighteen not fully answered.

Revision 1 is a real improvement and most of Round 1's hard corrections landed. I re-measured the Amphilochius extract myself and got **129 / 39 / 90** exactly; I re-ran the whole compile battery and every number in §5's table is right; the Macrina quotation is verbatim with exactly one punctuation substitution and no more; the Thaumaturgus corpus-map edit is correct in shape, role, confidence and note, and re-running the merge is byte-idempotent across all 56 bucket files. Those were the six hardest things to get right and they are right.

But the through-line Round 1 named — *a claim asserted about a file, a rule, or a command's output without running the check* — is still present, and now it is present in the fixes themselves:

- The corrected word count and the withdrawal of "verse" **did not reach two of the places they had to reach**, and both are places this pass itself edited: **Source Registry row 65**, which still says "an extract of his own **verse**" and still says the extract is "**verified directly**" when the record it points at is now `verified-via-authority`; and **`cappadocian.source.amphilochius-of-iconium-own-works.md`**, whose `edition` field — compiled, and sitting in `compiled/repository.json` in the package I built — still reads "One short extract of his own **verse**," and whose body still reads "a roughly **240-word** extract of his own **verse**." That record was not touched by Revision 1 at all, yet the verification document's §3 lists it under **Changed** and the Registry's own log says it was "corrected alongside."
- The cross-document sweep is still incomplete, and **one of the misses is a location Round 1 named explicitly by file and line** (`cappadocian_Integrated_Ecology_Analysis.md` line 139). I found three further live occurrences the sweep did not reach, one of them in a section (**Doc_02 §7**) that the verification document's own §1.2 names two paragraphs earlier as a place the law is carried. §1.5's claim that the correction "was propagated to every live occurrence the review found" is false, and §7's "no two documents are left disagreeing" is false.
- Revision 1 introduced a **new** unchecked citation of its own: it states in two places that Ep. 210's upbringing passage is in the letter's **§2**. It is in the letter's unnumbered opening section; the "2." marker stands more than a thousand characters later in the file.
- The Doc_04 argument now contradicts itself four lines apart — "the Primary/Supporting question **turns on one score**" (used to kill elevation) against "the Framework's classification is a **whole-battery judgment, not a Formation-score threshold**" (used to blunt downgrade). Doc_04 §3.1's own heading for that score is "**the decisive moderation**," which supports the first reading and not the second.
- The Confidence/Gravity Cross-Check "re-run" is going through the motions. It grades the evidence on a two-tier scale — *Documented-on-the-builder's-knowledge* → *Documented, with one instrument edition-verified* — that appears nowhere in Doc_04, and it could not have produced any answer but "no divergence," since Doc_04's own value for candidate 8 is *Documented* and still is.
- §1.3 and the ledger both rest an escalation on the claim that Doc_04 §9 Open Item 9's caveat is "**now, for the first time**, not wholly true." **62 records in this world already carry `verification_state: verified-direct`**, and the Registry's Confidence-A rule keys on direct verification by this build. The caveat has been stale for at least ten days. The escalation is still worth making; the "for the first time" is not true, and it was not checked.

The honesty of the revision is not in question — it names its own new regression (readability), its own new punctuation substitution, and its own withdrawn credit, and it does not claim a disposition. The execution still does not meet the standard the document sets for itself.

---

## PART ONE — WHAT I INDEPENDENTLY RAN OR READ

Everything in Part Two and Part Three rests on one of these, not on the document's account of it.

**The Amphilochius extract.** Read `div2 xvii.xxiii` in `cic/texts/npnf214_seven-ecumenical-councils.xml` in full (lines 44075–44103) with endnote 603. Counted programmatically: **body 129 words; two bracketed editorial stretches 25 + 14 = 39; remainder 90.** Counted the whole `div2` with markup stripped: **242.** Counted its parts: heading 14, "VIII." numeral, endnote 603 = 47, body 129, closing editorial "Note." paragraph 52. Ran `grep -c Amphilochius` on the file: **21 hits**, the first at line 1080 in the table of contents.

**The Macrina quote.** Diffed the record's `text` word-by-word against `ix.ccv-p26` (lines 37060–37068). Located the section markers of Letter CCX (`ix.ccxi`) by regex on the raw XML. Confirmed endnote 2769 ("Macrina, at her residence at Annesi"), the §3 Thaumaturgus/Musonius passage and its two endnotes, and the prolegomena endnote 21 at line 952 ("*Epp*. cciv., ccx., ccxxiii.").

**Compile and gates.** `python -m engine.m2.cli staleness-check`; `build cappadocian` (package `2026-09-09T02-08-33Z`, since deleted); read `validation/gates-report.json` in full; `determinism-check cappadocian`; counted `compiled/coverage.json` statuses; `pytest engine/m1/tests engine/m2/tests`. Read `engine/m1/gates.py` for `FK_CEILING` and computed `fk_grade` on both the current and the pre-revision `modern_rendering`. Grepped `compiled/repository.json` and `compiled/prompt.txt` to establish which record fields reach compiled content.

**Corpus map.** Read both `_staging` rows and the regenerated bucket rows. Re-ran `python cic/engine/corpus_map_merge.py` and checked `git status` afterwards.

**Cross-document sweep, run independently.** Grepped `worlds/cappadocian/`, `records/cappadocian/`, `cic/corpus-map/` and all seven deployment chunks for: the bishop-name sets, "eleven bishops," "empire's own standard / legal touchstone / touchstones," "240," "verse," "Epp. 204," "Ep. 210."

**Rules.** Read `cic-build-cycle` SKILL.md's escalation categories and *Naming and term propagation* rule verbatim rather than from either document's paraphrase.

---

## PART TWO — JOB 1: WAS EACH ROUND 1 FINDING ANSWERED?

| # | Round 1 finding | Verdict | Evidence |
|---|---|---|---|
| 1 | "Roughly 240 words" wrong by ~2.7x | **PARTIALLY ANSWERED** | I measured 129/39/90 — the revision's figure is exactly right, and it now stands correctly in the verification doc §3, Doc_02 §1.6, Registry row 117, `figure.amphilochius`, and the new source record. It does **not** stand in `source.amphilochius-of-iconium-own-works.md` line 40 ("roughly 240-word extract"), untouched. See New Finding 1. Separately, the decomposition offered for the ~240 figure is arithmetically wrong in all three places it appears — New Finding 9. |
| 2 | Extract is not verse and contains no enumeration | **PARTIALLY ANSWERED** | Corrected in the doc, Doc_02 §1.6, row 117, the figure record and the new source record ("his epitome is prose"; "It is not verse in this rendering either"). Still uncorrected in **Registry row 65** ("an extract of his own verse") and in `source.amphilochius-of-iconium-own-works.md` at **both** line 20 (`edition`, compiled) and line 40 (body). See New Findings 1 and 2. |
| 3 | Row 117 Confidence A violates the Registry's own A–B rule | **ANSWERED** | Row 117 is now `B`, and its Verification Note quotes the operative second clause of the rule and names rows 11/66/69 as the consistency check. The Registry's line-14 claim that no Confidence-A row violates the rule is true again. |
| 4 | `verified-direct` contradicts the ledger §47 precedent | **ANSWERED** | `verification_state: verified-via-authority` on line 11 of the new record, with the reason in the divergence note. (The precedent it *cites* is wrong — New Finding 7 — but the grade itself is right.) |
| 5 | "Three review rounds could not have caught it" is false | **ANSWERED** | Withdrawn in the doc §3 and in the Registry log. I confirmed rows 60 and 78 both locate their sources "within `cic/texts/npnf214_...xml`," and that a single grep on that file returns 21 hits including the heading. The rewritten standing check ("never assert a text does not exist without grepping the volumes the Registry already cites") is the right lesson. |
| 6 | §5's staleness claim false as delivered | **ANSWERED** | I re-ran everything. `staleness-check`: `pass: false`, cappadocian stale on the eight touched records — matches. Build succeeds. Gates: **18 total, 17 pass, 1 fail**, the failure `voice-perspective` with the single finding on `cappadocian.dw.reading-scripture` — matches. `determinism-check cappadocian`: `pass: true, differing_paths: []` — matches. Coverage: 26 substantive / 2 honest_limit — matches. **Pre-existing claim holds**: `git diff f07eb91 HEAD` on that record is empty, and the flagged string is only in that one file. **Readability claim is consistent**: `FK_CEILING = 10`; the pre-revision `modern_rendering` scores 9.62, the current one **5.55 exactly as claimed**, and appending a literal rendering of the added clauses to the old text takes it to 11.0 — the claimed 11.3 is the right shape. One stale line remains, see Cosmetic 2. |
| 7 | Registry cites ledger §50, which did not exist | **ANSWERED** | `## 50.` exists at line 797 and is substantive. The four deferred items now have a home outside the one document, which is what the finding asked for. |
| 8 | The cross-document sweep was not run | **PARTIALLY ANSWERED** | **(a) answered** — the law record's `work` now says eleven. **(b) answered** — row 79's Licensed-For cell and note rewritten. **(c) answered** — Doc_01 §4a rewritten, and rewritten well ("written into the empire's communion test; they were not themselves that test"). **(d) answered** — Doc_02 §2 now carries all eleven and the "made the empire's standard" conclusion is bounded. **(f) answered** — Forces Document Layer 1 now names eleven and four, and discloses the prior omission. **(g) answered** — Doc_02 line 37's pointer is now true. **(e) NOT ANSWERED** — `cappadocian_Integrated_Ecology_Analysis.md` line 139 still reads "makes this world's own bishops the empire's legal touchstone"; that file is not in the change set and is not in §1.5's sweep list, with no statement that it was considered. **(h) NOT ANSWERED** — the G1 manifest was edited, but only its Theodosian-Code bullet; line 92 still lists "Amphilochius of Iconium's genuine works" among the honest gaps unqualified. **(i) NOT ANSWERED** — Registry row 11 and Doc_02 §1.4 still cite "Epp. 204 and 223" with no note of Ep. 210; neither was edited and neither is mentioned. Plus three further live occurrences the sweep did not reach — New Finding 8. |
| 9 | Doc_04 answers only the elevation question | **PARTIALLY ANSWERED** | The downgrade analysis is now present and reaches a stated conclusion; the baptism/festival objection is engaged rather than routed around, and engaged seriously ("it reaches directly into the sites and ministers of two of the six instruments"); the Cross-Check is addressed rather than ignored; Doc_04 is correctly not revised. But the argument now contradicts its own premise (New Finding 5), the Cross-Check re-run is a no-op dressed as a check in invented vocabulary (New Finding 10), and the Open Item 9 claim is overstated in a way that was checkable and not checked (New Finding 6). The Open Item 9 *reading* is correct — I read it: "Systemic caveat (unchanged): nothing in this build has been verified against editions or external scholarship." |
| 10 | Open Item 2 credit does not do the work | **ANSWERED** | Withdrawn in §1.4 and in the record's body ("WHAT THAT IS NOT ... this record no longer claims that it is"), with the tightening argument and the Gravities 6/8 point both carried. This is the cleanest answer in the revision. |
| 11 | C-E quote truncated one clause before a difficulty | **ANSWERED** | I diffed the extended `text` word-by-word against lines 37060–37068: **verbatim, with exactly one substitution** — source `fathers,]`, record `fathers.` — which is precisely what the record discloses; nothing else differs, nothing added, dropped or reordered, and the stated line range is exact. The new `tensions` line does **real** work rather than papering over: it names both halves and qualifies the flat `positions` line ("true of the deposit and not of every one of us who received it"). The shortened `modern_rendering` drops nothing material and both glosses Round 1 flagged are gone. Two small new glosses replace them — Cosmetic 4. |
| 12 | Scope-discipline argument misreads the skill | **ANSWERED** | §2.1 concedes the misreading, quotes the skill's enumerated governance-file list, names the inconsistency with its own `records/` edits, and distinguishes "touches a shared file" from category 2's actual test. The Firmilian half is sustained on the granularity/precedent ground, and I confirmed the letters-corpus granularity rule exists in the `anf05` staging file at lines 181–182. |
| 13 | The Thaumaturgus edit as specified was wrong | **ANSWERED, and verified** | A **second row** was added: `atlas_ids: [cappadocian-nicene-pastoral-monastic-tradition]`, `role: tradition`, `confidence: provisional`, century-gap and no-3rd-c-Pontus-entry reasons both in the note, the `anatolian-church-third-century` row untouched — matching the two sibling rows exactly. I re-ran `corpus_map_merge.py`: it reports `valid.` and produces **zero** diff, so the committed generated files are exactly what the generator emits. Only the Cappadocian bucket changed; no other bucket file moved. The "two rows, not three atlas ids" correction on the Cyprian epistles was also made. |
| 14 | Ep. 210 is mischaracterized | **PARTIALLY ANSWERED** | The body of `source.basil-macrina-the-elder-letters` is now right on substance — I confirmed the "tradition of Gregory the truly great ... blessed Musonius, whose teaching is still ringing in your ears" passage, both endnote identifications, and the Ep. 204 cross-reference. But the **section number is wrong** (New Finding 3) and the record's own `work:` field still calls Ep. 210 "a thinner third witness," contradicting its body (New Finding 4). |
| 15 | Prolegomena cites three letters, not two | **ANSWERED** | Corrected in §4 and in the record. Verified at line 952, endnote `n="21"`: "*Epp*. cciv., ccx., ccxxiii." |
| 16 | Latin block normalized without saying so | **ANSWERED** | §1.5 now states the block is "lightly normalized (abbreviations expanded inconsistently between the two texts), not a transcription of either witness verbatim." |
| 17 | Two witnesses presented as independent | **ANSWERED** | §1.5 and the record's `edition` field both now carry the Latin Library Confidence-C header, the OCR quality problem, and the possible non-independence. This is a good, unflattering disclosure. |
| 18 | Structural and counting slips | **ANSWERED** | div3-inside-div2 fixed; `corpus_map_merge.py` named as the generator; ordinal corrected to fourth with the three priors named; the printed-heading fusion now described as "adjacent apparatus rather than one printed line"; both `modern_rendering` glosses corrected; the `records_commit` stamp behaviour recorded in §5 and carried to ledger §50 item 6. |

**Count: 13 of 18 fully answered; 5 partially answered (1, 2, 8, 9, 14); none answered wrongly outright, though Finding 14 contains a new wrong answer inside a right one.**

---

## PART THREE — JOB 2: NEW DEFECTS INTRODUCED OR LEFT BY REVISION 1

### 1. [SUBSTANTIAL] `cappadocian.source.amphilochius-of-iconium-own-works.md` still carries both corrected claims — in compiled content — and was never touched by Revision 1, though two documents say it was.

**Location:** `records/cappadocian/source/cappadocian.source.amphilochius-of-iconium-own-works.md` lines 19–20 (`edition`) and line 40 (body).

```
edition: No open English edition of his works as a corpus has been located. One short extract of
  his own verse -- the canon-list passage from the Iambics to Seleucus -- is vendored ...
```
```
...a roughly
240-word extract of his own verse to Seleucus, on the canon of Scripture, sits in the already-vendored
```

`git diff HEAD~1 HEAD --name-only` does not contain this file. Both of Round 1's corrections — the word count and the withdrawal of "verse" — are absent from it.

**Why it is substantial and not a stray.** The `edition` field is **compiled**. I grepped the package I built: `compiled/repository.json` contains the string `"One short extract of his own verse"` verbatim. This is not a documentation artefact; it is content the Representative's repository carries. (The body's "240-word" is not compiled — front matter only — but it is still a live record claim.)

**And two live documents assert it was fixed.** The verification document §3's **Changed** list names `cappadocian.source.amphilochius-of-iconium-own-works` among the records corrected. The Registry's sixth-pass log entry says "the two affected WRS records (`cappadocian.source.amphilochius-of-iconium-own-works`, `cappadocian.figure.amphilochius`) corrected alongside," and then, three paragraphs later, "All corrected above." The figure record *was* corrected, thoroughly and well. This one was corrected in the first change set for a different defect (the availability claim) and was never revisited when the word count and the verse characterization were fixed everywhere else.

**Fix.** Correct both fields, and correct the Registry log's and §3's claims about what was done.

---

### 2. [SUBSTANTIAL] Source Registry row 65 still says "verse," and says the extract is "verified directly" — contradicting row 117 and the record row 117 points at.

**Location:** `cappadocian_Source_Registry.md` line 124 (row 65).

> "an extract of his own **verse** (*From the Iambics… to Seleucus*, on the canon of Scripture) was already sitting in the vendored `cic/texts/npnf214_...` … That extract is now row 117, **verified directly**."

Two errors, both introduced by the first change set and both surviving a revision written specifically to remove them:

- **"verse"** is the characterization Round 1 Finding 2 asked to be dropped "from every description of the held text." Row 117, four rows-groups below, now says the opposite in the same file: "his epitome is prose, not verse."
- **"verified directly"** is now false of the thing it describes. The record is `verification_state: verified-via-authority`; row 117's own Verification Note deliberately avoids the phrase, opening "**Located and read in full** 2026-09-09." Row 65 is the only place in the Registry that still calls this extract directly verified, and it does so in the same file that explains at length why it is not.

Row 65 is a row this pass rewrote. The sweep did not come back to it.

**Fix.** "an extract of his own work (the NPNF editor's prose epitome of it)"; and "That extract is now row 117, read in full and recorded at `verified-via-authority`."

---

### 3. [SUBSTANTIAL] The Ep. 210 upbringing passage is in the letter's unnumbered opening section, not §2. This is a new claim, made twice in Revision 1, and it was not checked.

**Location:** verification document §4 ("its §2 has the upbringing"); `records/cappadocian/source/cappadocian.source.basil-macrina-the-elder-letters.md` ("Its section 2 has the upbringing").

**What the file shows.** In `cic/texts/npnf208_basil-letters-select-works.xml`, within the `ix.ccxi` element, the string "here I was brought up by my grandmother" stands at offset **1643** from the element's start. The section markers are `<p class="c21" id="ix.ccxi-p7">2.&nbsp;` at offset **3421** and `<p class="c21" id="ix.ccxi-p9">3.&nbsp;` at offset **6005**. The passage therefore sits in the letter's opening, unnumbered block — section 1 by NPNF's own convention, the same convention under which the Macrina passage in Ep. 204 is correctly cited as §6. There is no "1." marker to catch the eye, which is exactly why the claim needed a check.

The §3 attribution in the same sentence *is* correct — I confirmed the Thaumaturgus/Musonius passage sits after the "3." marker. So the record is right about the harder half and wrong about the easier one.

**Why this is substantial rather than cosmetic.** Round 1 named the defect class as "a claim the document asserted about a file … without running the check," and this is a wholly new instance of it, created by the revision, in a locus citation — the one category of claim this project treats as load-bearing. It is also in a `verified-direct` record whose `discovery_channel` says the letters were "located in the vendored file and read in full."

**Fix.** "Its opening section has the upbringing," or drop the section number.

---

### 4. [SUBSTANTIAL] `cappadocian.source.basil-macrina-the-elder-letters` now says two opposite things about Ep. 210 — the exact defect shape of Round 1's Finding 8a, inside a record this pass rewrote to answer Round 1's Finding 14.

**Location:** the same record, `work:` (line 18–19) against its body (line 53ff.).

```
work: >-
  Basil, Epistles 204 and 223, with Epistle 210 as a thinner third witness ...
```
against
```
A THIRD PASSAGE THIS ROW DID NOT NAME, and it is stronger than a first reading suggested.
... the row's citation is extended to name 210 as a real third witness on both axes rather
than dismissed as merely thinner.
```

The body explicitly repudiates the word the front matter still uses, and `work` is a compiled field. Round 1's Finding 8a was "One record, two answers" about `work` versus `divergence_note` on the law record; that instance was fixed and this one was created in its place.

**Fix.** `work: Basil, Epistles 204 and 223, with Epistle 210 as a third witness carrying both halves of the datum separately`.

---

### 5. [SUBSTANTIAL] §1.3 kills the elevation case with one rule and blunts the downgrade case with its negation, four lines apart — and Doc_04's own text supports the first.

**Location:** verification document §1.3, the paragraphs at "The elevation case fails" and "Two reasons it is not decisive."

> "Doc_04's Primary/Supporting question for this gravity **turns on one score**: the **Formation** test…"

> "…the Framework's classification is a **whole-battery judgment, not a Formation-score threshold**."

These cannot both be load-bearing. The first is what makes the elevation case fail (corroboration cannot move a score already at maximum on the other five). The second is what makes the downgrade case non-decisive (a fact that sharpens "situational" lands inside the annotation, because Formation is not a threshold). The document uses whichever proposition disposes of the case in front of it. This is precisely the asymmetry Round 1's Finding 9 identified — "the document never turns the argument around" — reappearing in the answer to it, now as an explicit contradiction rather than an omission.

**And Doc_04 itself takes the first side.** §3.1's paragraph on this candidate is headed "**On Candidate 8's Formation score (the decisive moderation).**" The document cites §3.1 for the six-instrument list in the same breath and does not mention that §3.1 calls the moderation decisive — which cuts directly against the second reason.

**Fix.** Pick one. If the classification is a whole-battery judgment, then the elevation case has to be argued on the battery, not on "already at maximum." If Formation is decisive, then the second reason has to go and the downgrade case is stronger than "marginally."

*Note on the second of the two reasons:* "Open Item 1 is explicitly flagged for external review — it is not a build thread's to close, in either direction" is correct as fact (I read Open Item 1; it says "flagged for external review"). But it is a statement about **authority**, not about **evidential weight**, and it is offered as one of "two reasons it is not decisive." A build thread's lack of standing to close an item is not evidence that the law fails to settle it. Presented this way it pads a thin argument with a procedural fact.

---

### 6. [SUBSTANTIAL] "That caveat is now, for the first time, not wholly true" is false, and the check that would have shown it is one `grep`.

**Location:** verification document §1.3 ("**That caveat is now, for the first time, not wholly true**"); carried in softer form to ledger §50.

Doc_04 §9 Open Item 9 reads: "Systemic caveat (unchanged): **nothing in this build has been verified against editions or external scholarship**; all citations are from the builder's internal knowledge at work level."

`grep -rl "verification_state: verified-direct" records/cappadocian/ | wc -l` returns **62**. Sixty-two of this world's records already assert direct verification against a vendored edition. The Source Registry's own A–B rule (line 14) is written entirely around "sources this build session itself directly verified — the files Mark supplied 2026-08-30/31." Ledger §47 records verbatim verification of a quote against `npnf208`. Doc_04's own Revision 1 is dated 2026-08-30, and the caveat was already inaccurate by 2026-08-31 at the latest.

So the finding worth escalating is real — Open Item 9 overstates the build's unverified state — but it is **not new, not this pass's discovery, and not caused by CTh 16.1.3**. Stated as "for the first time," it credits this pass with surfacing something ten days stale, and it is an assertion about the state of a corpus of records that a single grep would have corrected. That is the through-line defect, in the finding the document escalates most confidently.

**Fix.** "Open Item 9's blanket caveat has been inaccurate since the 2026-08-30/31 vendoring passes — 62 records now carry `verified-direct` — and this pass adds edition-verification of one of Gravity 3's own instruments. Escalated for narrowing."

---

### 7. [SUBSTANTIAL] The precedent the new source record cites for `verified-via-authority` is the wrong record, corrected in the wrong direction, for a different condition.

**Location:** `cappadocian.source.amphilochius-iambics-to-seleucus.md`, `divergence_note` lines 25–27:

> "…which is the same condition this world already corrected `cappadocian.source.basil-against-eunomius` **and** `cappadocian.quote.basil-against-delaying-baptism` for."

The quote record is right — ledger §47 corrects it from `verified-direct` to `verified-via-authority` for exactly this condition (content resting on a citing authority's own selection). **`cappadocian.source.basil-against-eunomius` is not.** Its current `verification_state` is **`unverified`**, and its own `divergence_note` says why:

> "this record previously claimed the treatise text was **verified-via-authority** within `cic/texts/npnf208_...`. Direct inspection of that file's own div1 structure … found **no division containing the three-book treatise's own translated text**."

So that record was corrected *away from* `verified-via-authority`, not to it, and for the opposite condition — the text is not in the file at all, rather than being present in an editor's selection. Citing it as precedent for the grade chosen here inverts what it stands for. Round 1's Finding 4 turned on getting this precedent right; the fix names it and then names one more, unchecked.

**Fix.** Drop `basil-against-eunomius` from the sentence, or characterize it correctly as a different defect (falsely claimed presence, corrected to `unverified`).

---

### 8. [SUBSTANTIAL] §1.5's "every live occurrence the review found" and §7's "no two documents are left disagreeing" are both false. I found four more live occurrences, one named by Round 1 and one in a section §1.2 points at.

The `cic-build-cycle` rule, read verbatim: *"Whenever a name or term changes, check every file it appears in — narrative document, index spreadsheet, deployment lexicon chunk — before treating the change as complete."*

Untouched, live, and carrying the framing the pass corrected elsewhere:

- **`cappadocian_Integrated_Ecology_Analysis.md` line 139** — "the 381 communion law (CTh 16.1.3) **makes this world's own bishops the empire's legal touchstone**." This is Round 1 Finding **8e**, named by file and line. The file is not in the change set and is not in §1.5's list, and no reason is given for leaving it.
- **`cappadocian_Doc_02_Source_Ecology.md` line 112 (§7)** — "the 381 communion law **naming Helladius, Otreius, Gregory of Nyssa, and Amphilochius**." Four names, in the same file whose §2 the pass rewrote to eleven. The verification document's own §1.2 point 3 names "Doc_02 §2/**§7**/§9" as places the law is carried, two paragraphs before §1.5 claims the sweep is complete.
- **`cappadocian_Integrated_Ecology_Analysis.md` line 161** — "the communion law naming its bishops as touchstones."
- **`cappadocian_Doc_05_Ecological_Reconstruction.md` line 29** — "the communion law naming the region's bishops as touchstones."

Add New Findings 1 and 2 (Registry row 65 and the own-works record contradicting row 117 and the new source record on "verse" and "verified directly") and §7's assertion that "no two documents are left disagreeing" is false on its face.

**Fix.** Run the sweep to completion — or, for the ones judged acceptable as loose summary, say so on the record. What is not acceptable is asserting completeness. (I also grepped all seven deployment chunks: **no chunk edit is owed**, which the revision still does not say it checked.)

---

### 9. [SUBSTANTIAL — narrow] The decomposition of the ~240 figure does not add up, and it now stands in three places.

**Location:** verification document §3 ("the section is ~240 words *including* the editor's heading and his note on his own method"); Doc_02 §1.6; Registry row 117 ("that counts the editor's heading and his note on his own method").

My part-by-part count of the whole `div2`: heading **14**, the "VIII." numeral **1**, endnote 603 (the note on his own method) **47**, body **129** = **191**. The whole element is **242**. The missing ~51 words are the editor's **separate closing "Note." paragraph** — "We have thus four [five if we accept the Laodicean list as genuine,] different canons of Holy Scripture…" — which is neither the heading nor the method note, and which Round 1's own Finding 1 enumerated explicitly when it broke the corpus map's `~242` down.

So the sentence written to explain where 240 came from accounts for 191 of it. It is a small number, but it is the third statement of this same figure, in a passage headed "**measured rather than estimated**," in a document whose central correction is that a number was reported without being measured.

**Fix.** "…that counts the editor's heading, his note on his own method, and his separate closing note on the four (or five) canons."

---

### 10. [SUBSTANTIAL — narrow] The Confidence/Gravity Cross-Check "re-run" grades on a scale Doc_04 does not have, and could not have returned anything but "no divergence."

**Location:** verification document §1.3, "The Confidence/Gravity Cross-Check, re-run because its input changed."

> "the evidential-confidence side moves from *Documented-on-the-builder's-knowledge* to *Documented, with one instrument edition-verified*"

Neither label exists in Doc_04. §3.2's entry for candidate 8 reads, in full: "organizing strength strong; evidence **Documented**. Eligible for Primary as the world's situation-gravity…" The Cross-Check's mechanism is a comparison of organizing strength against the evidence tier; this world's tiers are Documented / Widely Accepted / Contested / Inferential-Thin. Verifying one instrument against two Latin editions does not move *Documented*, and the document says the organizing-strength side is unchanged. With neither side moving, "the two do not diverge" is the only reachable output, and it was reachable without opening Doc_04.

Round 1 asked for one of two things: "re-run the Cross-Check for Gravity 3 and record 'no change, and here is why,' **or** say plainly that it was not re-run and why that is acceptable." What is delivered is the form of the first with the content of neither — a coined intermediate tier presented in the register of a graded finding. Compare §3.2's genuinely informative entries (candidates 7, 11, 12), each of which names a specific divergence or specific reason there is none.

**Fix.** Say it in Doc_04's own vocabulary: "Evidence tier for candidate 8 is *Documented* and stays *Documented*; edition-verification of one instrument raises the floor under that tier without changing it; organizing strength unchanged; no divergence, and none was available to be found."

---

### 11. [SUBSTANTIAL — narrow] §7 tests escalation category 4 against a paraphrase that adds a condition the skill's own text does not impose.

**Location:** verification document §7, category 4 bullet.

> "it does *not* trigger category 4, because **category 4 is about tensions that stay unresolved**, and this one resolves"

The skill's text, verbatim: *"**Unresolved tensions the pipeline can't close on its own** — two reviews disagreeing with each other, a contradiction between two already-cleared master documents, **or a finding that cuts against an earlier decision**."*

The heading carries "unresolved"; the three enumerated triggers do not repeat it, and the third — "a finding that cuts against an earlier decision" — describes the Amphilochius correction exactly: a finding that cuts against Doc_02 §1.6's and Registry row 65's cleared sourcing conclusion. The second — "a contradiction between two already-cleared master documents" — also arguably fits, since Doc_02 §1.6 and the shared corpus map contradicted each other for nine days.

I am not asserting that category 4 must fire here; the reading that the heading governs the list is defensible and the pass may well be right. What is not acceptable is that the test is run against a restatement of the rule rather than the rule. This is the same move Round 1's Finding 3 caught in row 117's Confidence-A justification — quoting the half of a rule that disposes of the question. A document that has just been corrected for that should quote category 4 in full and argue the third clause explicitly.

**Fix.** Quote all three triggers and dispose of each. (Given New Finding 8, the "no two documents are left disagreeing" clause of this same bullet is in any case false as delivered.)

---

### COSMETIC

1. **§2.1: "this same pass edits seven files under `records/cappadocian/`."** `git diff --name-only f07eb91 HEAD` lists **eight** — Revision 1 added `cappadocian.contested.homoian-nicene-reversal.md`. The number was true of the first change set and was carried forward uncounted.
2. **§5's pytest line is stale.** "33 passed, 1 failed" sits in a section headed "measured after the change, not before it." Re-running now: **34 passed, 0 failed**. The document does explain the self-healing mechanism in the same sentence, and Round 1 cleared the explanation — but as delivered, the one number in §5 a reader cannot reproduce is the one presented without a reproduction caveat.
3. **Doc_02 §2 now prints "Optimus of Antioch (in Pisidia)."** The Latin quoted at §1.1 reads only *Optimo episcopo Antiocheno*; §1.2 says only "Optimus for Asiana." The Pisidian identification is almost certainly right, but it is an editorial identification added in a revision whose whole subject is not asserting more than the file carries, and it is nowhere disclosed as one.
4. **Two glosses removed from `modern_rendering`, two added.** "the rule of godliness **handed down to us**" (the text has only "delivered") and "I took **that man** for a father" (the text has plural "those I set down as fathers"). Both defensible; both are the same category of unnoticed drift Round 1 flagged, and the fix pass did not notice them while fixing the other two.
5. **§5's causal phrasing.** "Extending the Macrina quotation to its full stop (§4) pushed `modern_rendering` to Flesch–Kincaid grade 11.3." Extending `text` cannot move `modern_rendering` — the gate deliberately never grades `text` (`gates.py` lines 348–364). Extending the rendering to match was a separate authorial choice, and the regression follows from that choice, not from the quotation.

---

## PART FOUR — CHECKED AND CLEARED

Stated so the record shows what was examined and held.

1. **The word count, measured independently.** 129 body / 39 bracketed / 90 rendered — my count matches the revision's exactly, including the 25+14 split of the two bracketed stretches. The whole `div2` is 242, which is where the corpus map's `~242 words` comes from.
2. **The prose/epitome characterization.** Endnote 603 says what the revision says it says; the editor's own word is "Epitome"; the two replaced stretches are exactly the book-lists. "A canon-list poem with the canon list taken out" is a fair and useful description.
3. **Row 117 at Confidence B**, with the operative half of the A–B rule quoted and the rows-11/66/69 consistency check named.
4. **`verified-via-authority` on the new record** — the right grade on this world's own rule, whatever the precedent citation says.
5. **The withdrawal of "could not have."** Rows 60 and 78 both cite `npnf214`; `grep -c Amphilochius` on that file returns 21, the first hit in the table of contents at line 1080.
6. **Every number in §5's post-change column.** Build succeeds; 18 gates, 17 pass; `voice-perspective` the only failure, on `cappadocian.dw.reading-scripture`'s "the world's first days," a record `git diff f07eb91 HEAD` shows untouched; `determinism-check cappadocian` `pass: true`; coverage 26/2/0; `staleness-check` `pass: false` with cappadocian stale on the eight touched records. The insistence that the staleness failure "must not be fixed" is right and is the most useful sentence in §5.
7. **The readability regression and its fix.** `FK_CEILING = 10`; the current `modern_rendering` scores **5.55**, matching the claim to two decimals; the pre-revision rendering scores 9.62 and takes a literal extension to 11.0, so an 11.3 intermediate is exactly the right magnitude. Disclosing a self-inflicted regression rather than silently fixing it is the discipline working.
8. **The Macrina quotation is verbatim.** Word-for-word against lines 37060–37068, one substitution (`fathers,]` → `fathers.`), disclosed and no more. The stated line range is exact. The Newman bracket boundary is where the record says.
9. **The `tensions` line does real work.** It states both halves and explicitly qualifies the flat `positions` line rather than restating it. Leaving `positions` unedited and carrying the qualification in `tensions` is a legitimate choice among the three Round 1 offered.
10. **Ep. 210's substance.** "the tradition of Gregory the truly great … up to the blessed Musonius, whose teaching is still ringing in your ears," both endnote identifications (Thaumaturgus; Musonius bp. of Neocaesarea d. 368), the endnote "Macrina, at her residence at Annesi," and the Ep. 204 cross-reference — all present as described. Only the section number is wrong.
11. **The prolegomena's three letters.** Line 952, endnote 21, "*Epp*. cciv., ccx., ccxxiii."
12. **The digamy off-by-one precedent** the quote record cites is real — that record does carry the printed-heading-versus-`div`-id drift note.
13. **The corpus-map edit, fully.** Row shape, `role`, `confidence`, note content, sibling untouched, generated bucket regenerated by the real generator. `corpus_map_merge.py` re-run produces `valid.` and a **zero** diff across all 56 entries — nothing changed that should not have. The note's claim that this world already holds the volume's two other Thaumaturgus works is correct.
14. **The `.gitignore` claim.** Lines 44–45 are `packages/*/*/**` and `!packages/*/*/manifest.json` — the exception the document names.
15. **The Review-Artifacts convention.** Alexandria, Imperial-Juridical and Syriac all have the directory; Cappadocian's is new, as ledger §50 says.
16. **The Firmilian escalation.** The letters-corpus granularity rule is stated in the `anf05` staging file (lines 181–182), and the `npnf214` "Split 2026-08-26 on Mark's ruling" precedent is real. Escalating rather than acting is right, and the specified edit is specific enough for someone else to execute.
17. **No deployment-chunk edit is owed.** I grepped all seven; only `story001` names Amphilochius, as the correspondent who asked for *On the Holy Spirit*, which nothing here touches.
18. **The Open Item 2 withdrawal**, in both the document and the compiled record body — complete, and it carries the "tightens rather than relieves" argument rather than merely deleting the credit.
19. **The restraints held.** `formation_confidence: Inferential-Thin` unchanged on the figure record; no figure record for Macrina the Elder; the `voice-perspective` false positive not quietly fixed; Doc_04 not revised; row 65 corrected rather than deleted. Every one of these is the right call and several would have been easy to get wrong.
20. **Ledger §50 exists and is substantive.** It is honest about the second-order defect ("the same defect committed inside its own correction"), it names the withdrawn exculpation, and it carries all six deferred items. Its overclaims are the ones at New Findings 1, 2 and 6, not a general inflation.

---

## PART FIVE — ON THE DISPOSITION AT §7

**The posture is right.** "No disposition is claimed until a Round 2 review returns without calling for substantial revision" is exactly what the `cic-build-cycle` *Revision decision* rule requires: *"If substantial: revise, then send the revised version through Review again. Repeat for as many rounds as it takes."* Nothing is claimed that has not been earned, and the "Not Frozen, not proposed for Frozen, the project lead has not seen it" framing is correct and correctly repeated in the ledger.

**The category-by-category analysis is a real improvement over the first draft's one-clause assertions, and three of the four tests are sound.**

- **Category 1** — correct and obviously so.
- **Category 2** — correct, and the best-argued of the four. The Firmilian/Thaumaturgus asymmetry is defended on the category's own text ("decided for a reason external to this specific world's own ecology") rather than on the "touches a shared file" test the first draft substituted, and the Thaumaturgus edit's rationale genuinely is Doc_02 §1.6 and Doc_01 §4.
- **Category 3** — correct. The A–B rule was not changed (row 117 went to B rather than the rule going to "when a verification happened"), and the proposed standing check is proposed rather than adopted, which is the right side of the line.
- **Category 4** — **the weakest.** It is tested against a paraphrase that adds "stay unresolved" to all three triggers (New Finding 11), and its supporting clause "no two documents are left disagreeing" is false as delivered (New Finding 8, plus New Findings 1, 2 and 4 — three records or rows currently disagreeing with each other inside the change set itself). The two Doc_04 escalations under this category are right to be escalated; one of them rests on a false "for the first time" (New Finding 6).

**One structural point about the escalations themselves.** Both Doc_04 items are escalated under category 4 as things the pipeline cannot close. Open Item 9's inaccuracy is not really an unresolved tension — it is a stale factual caveat in a live document, correctable in one clause by whoever next revises Doc_04, and it was already stale before this pass touched anything. Escalating it is harmless; describing it as a category-4 tension this pass surfaced is not accurate.

---

## CLOSING VERDICT

**Substantial revision is still called for.**

New Findings 1, 2, 3, 4, 7 and 8 are corrections of fact or of the change set's own internal consistency and must be made before disposition: two records and one Registry row currently contradict each other or the file they describe, one locus citation is wrong, one precedent citation is inverted, and one completeness claim is false. New Findings 5, 6, 10 and 11 require an argument to be redone or a claim withdrawn. New Finding 9 is arithmetic. The five cosmetics can be applied directly.

Round 1 findings 1, 2, 8, 9 and 14 are not fully answered; the other thirteen are.

What Revision 1 got right is substantial and should not be lost in the count. The measurement is right — I did it independently and got the same numbers. The quotation is verbatim and the disclosure of its single punctuation substitution is exemplary. The corpus-map edit is correct in a way the first draft's specification was not, and the generator confirms it. The withdrawn exculpation, the withdrawn Open Item 2 credit, the self-reported readability regression and the refusal to claim a disposition are all the discipline working as designed.

The pattern worth naming, since both documents name patterns: Round 1 said the defect class was *asserting something about a file, a rule, or a command's output without running the check*. Revision 1 ran most of the checks it was told to run — and then made six new claims of exactly this kind without running any: that a record had been corrected when it had not (New Finding 1); that an extract was "verified directly" when its own record says otherwise (New Finding 2); that a passage sits in §2 when it sits in §1 (New Finding 3); that a precedent record was corrected to a grade it was corrected away from (New Finding 7); that a caveat became untrue "for the first time" today when 62 records had already made it untrue (New Finding 6); and that every live occurrence had been swept when four remain, one of them named in the review being answered (New Finding 8). The lesson the document draws for the Registry — *never assert that a text does not exist without grepping the volumes the Registry already cites* — generalizes further than it has yet been applied: never assert that a fix landed without opening the file it landed in.
