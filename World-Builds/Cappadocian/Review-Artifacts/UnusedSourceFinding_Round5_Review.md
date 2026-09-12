# Unused-Source Finding — Round 5 Independent Adversarial Review

**Document under review:** `World-Builds/Cappadocian/cappadocian_Unused_Source_Verification_2026-09-09.md` at **Revision 4**, together with the change set it dispositions (commit `847f142` on top of `7c3ae3d`; 6 files in this commit, one of them the Round 4 review artifact itself).
**Reviewer stance:** Independent adversarial. Did not author the document, the change set, or any of the four prior reviews; no stake in its passing or its failing.
**Review date:** 2026-09-09.
**Branch reviewed:** `claude/cappadocian-unused-source-finding`.
**Prior reviews:** Round 1 (14 substantial, 4 cosmetic); Round 2 (11 new substantial, 5 cosmetic, plus 5 of Round 1's not fully answered); Round 3 (7 new substantial, 5 cosmetic, plus 4 of Round 2's); Round 4 (3 new substantial, 6 cosmetic, plus 8 of Round 3's twelve not fully answered). All four returned **substantial revision required**.
**Consulted:** the four prior reviews in full; `CAPPADOCIAN_BUILD_LEDGER.md` §50 with all four revision addenda; `cappadocian_Doc_02_Source_Ecology.md`; `cappadocian_Source_Registry.md`; `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md`; `cappadocian_Integrated_Ecology_Analysis.md`; `cappadocian_Doc_05_Ecological_Reconstruction.md`; `cappadocian_Forces_Document.md`; `cic/texts/npnf214_seven-ecumenical-councils.xml`; `cic/texts/npnf208_basil-letters-select-works.xml`; `cic/corpus-map/_staging/npnf214_seven-ecumenical-councils.yaml` and `cic/corpus-map/cappadocian-nicene-pastoral-monastic-tradition.yaml`; `World-Builds/Cappadocian/scripts/wb_cappadocian_s21.py`; the touched records; the `cic-build-cycle` skill, loaded and read in this session rather than quoted from a prior review.

---

## VERDICT: **NO SUBSTANTIAL REVISION REQUIRED**

**All three of Round 4's substantial findings are answered.** Two of them — the word count and Source Registry row 11 — are answered correctly, and I re-derived both from the primary material before reading what the document claims. The third is answered correctly *in the document* and misdescribed *in the ledger*: the clause was deleted, and the ledger says the finding "does not hold" when it held.

**Five items remain, all of the same species and none of them substantial under the skill's test.** They are enumeration errors and stale self-descriptions in the pass's account of itself. Not one of them changes a claim about a source, a confidence rating, a sourcing conclusion, or a scope boundary. **They may be applied directly without a further review cycle.**

**The measurement that has been wrong in every previous draft is now right.** Before opening Revision 4 I extracted the `<div2 id="xvii.xxiii">` element to its own matching close tag and counted every constituent part under both markup-stripping conventions:

| part | strip-with-space | strip-without-space |
|---|---|---|
| "VIII." numeral + heading + endnote 603 | **62** | 60 |
| **extract body** | **129** | **129** |
| "Note." label + closing Note prose | **51** | 51 |
| **whole `div2`** | **242** | 240 |

242 = 62 + 129 + 51, to the word, exactly as Revision 4 states. The control holds: `div2 17.24` measures **629** under the same convention (610 without), matching the corpus map's `~629` for the sibling row. The body decomposes to **39** bracketed words in two stretches (25 + 14, precisely the Old- and New-Testament book-lists) and **90** rendered. The figure is identical in all five places it now lives — Doc_02 §1.6, Registry row 117, `cappadocian.source.amphilochius-iambics-to-seleucus`'s `divergence_note`, the verification document §3, and, after a rebuild, `compiled/repository.json`. **No stale `279`, `87`, `63`, `~54` or `59 + 129` survives anywhere outside the review artifacts and the ledger's own history of its earlier drafts**, which is where they belong. Round 4 could not write "nothing compiled is wrong on a matter of fact about a primary text." Round 5 can.

**Registry row 11 is fixed and the cause is recorded.** It now reads `Basil, Epp. 204, 210 and 223`, matching `cappadocian.source.basil-macrina-the-elder-letters`'s `work:` field, and the row carries a note naming the mechanical cause — an unasserted string replace that searched for "Thaumaturgus' **own** teaching" where the row reads "Thaumaturgus' teaching" and returned success having changed nothing. Round 1's Finding 8i is closed after four revisions. The table survives the edit intact: all 139 rows still carry 11 pipes.

**The whole battery reproduces.** Build succeeds; 18 gates, 17 pass, `voice-perspective` the single failure with its one finding on `cappadocian.dw.reading-scripture`'s "the world's first days"; `determinism-check` `pass: true`, `differing_paths: []`; coverage **26 substantive / 2 honest-limit / 0 empty**; `staleness-check` `pass: false` with `cappadocian` the only stale world of eight; `pytest engine/m1/tests engine/m2/tests` **34 passed, 0 failed**; `py_compile` clean on the generator. Package deleted, working tree clean. The Macrina quotation is verbatim against the vendored `npnf208` with **exactly one** non-equal opcode — a `,` rendered as `.` at the close of the Newman bracket — precisely as disclosed, and `modern_rendering` scores **FK 5.55** against the `readability` ceiling of 10.

**And the through-line has not stopped; it has shrunk below the bar.** Round 4's closing sentence prescribed one mechanical step: *after the edits, re-read the passage that describes them, and for every file it names, open that file.* Revision 4 did that for the four files it corrected — and did not do it for `git show HEAD~1`, which is why the ledger says a review finding does not hold when one command shows it did. That is the fifth consecutive round in which this pass's report of itself is wrong. But it is one paragraph in a ledger addendum, the underlying edit it misdescribes is correct, the document it summarizes says the right thing, and nothing about the Cappadocian world moves. Under the skill's *Revision decision* rule read literally, that is not substantial, and I am not going to promote it in order to justify a sixth round.

---

## PART ONE — WHAT I INDEPENDENTLY RAN OR READ

Nothing below rests on the document's, the ledger's, or any prior review's account of it.

**The Amphilochius `div2`.** Extracted `<div2 … id="xvii.xxiii">` to its own matching `</div2>` by depth-counting rather than by slicing forward to the next element's id, then counted every constituent part under both stripping conventions. Repeated for `div2 17.24` as the control. Extracted the two bracketed stretches from the body and counted them separately.

**The corpus map.** Read both the `_staging` row (`locus: div2 17.23 (~242 words)`) and its sibling (`div2 17.24 (~629 words)`), and the live `cappadocian-nicene-pastoral-monastic-tradition.yaml` row.

**Cross-file consistency of the figure.** Grepped `279`, `87 words`, `63 words`, `~54`, `54 words`, `59 + 129` across `World-Builds/Cappadocian/`, `records/cappadocian/` and `cic/corpus-map/`; read the four corrected locations in full; rebuilt and grepped `compiled/repository.json` for both the old and the new figure.

**Registry row 11.** `sed -n 50p` at `HEAD`, against the record's front matter and `external_ids.cappadocian_source_registry_row`. Pipe-count integrity across all 139 table rows.

**The G1 claim.** `grep -n "eleven\|Nectarius\|Terennius\|Marmarius\|Optimus\|Pelagius\|Diodore\|line 37"` against `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md`; `git show HEAD~1:…Unused_Source_Verification_2026-09-09.md | grep -o "the G1 manifest (which[^)]*)"` and the same against `HEAD`; `git diff f07eb91 HEAD` on the G1 manifest in full.

**The completeness grep.** `grep -rn "Helladius, Otreius, Gregory of Nyssa, and Amphilochius" .` from the repository root, every hit inspected.

**The "considered and left" lines.** Read `Integrated_Ecology_Analysis.md` lines 139 and 161 and `Doc_05_Ecological_Reconstruction.md` §29 in full, then swept `World-Builds/Cappadocian/` and `records/cappadocian/` for the whole class of "381 / communion law / touchstone" phrasings to see whether the two named are the only two.

**Compile and gates.** `python -m engine.m2.cli build cappadocian` (package `2026-09-09T03-07-37Z`, since deleted); parsed `validation/gates-report.json` and `compiled/coverage.json` programmatically rather than by eye; `determinism-check cappadocian`; `staleness-check` across all eight worlds; `pytest engine/m1/tests engine/m2/tests`.

**The Macrina quotation.** Parsed the record's front matter, stripped markup from the whole of `npnf208`, normalized whitespace, located the passage and ran a character-level `SequenceMatcher` over the aligned window; computed `fk_grade` on `modern_rendering` with `engine.m1.fk`.

**Round 4's six cosmetics and Round 3's four leftovers.** Opened each named file at each named line.

**The skill.** Loaded `cic-build-cycle` in this session and read the *Revision decision*, *Review*, *Naming and term propagation* and *Cross-document fact consistency* rules from the skill's own text, not from a prior review's quotation of them.

---

## PART TWO — JOB 1: WAS EACH ROUND 4 FINDING ANSWERED?

### The three substantial

| # | Round 4 finding | Verdict | Evidence |
|---|---|---|---|
| 1 | The word count is wrong for the third revision running, and "these figures do not reconcile" is false | **ANSWERED, CORRECTLY** | Measured independently: 242 = 62 + 129 + 51 with-space, 240 without; `div2 17.24` = 629, confirming the convention from a second row. All four named locations carry the identical corrected figure plus the 629 control; the rebuilt `compiled/repository.json` carries `242 words -- 62 of numeral…` and zero occurrences of `279`. See Part Four item 1. |
| 2 | Registry row 11 was never edited, and three documents say it was | **ANSWERED, CORRECTLY** | Row 11 now reads `Epp. 204, 210 and 223`, matches the record it indexes, and carries a note stating the silent-no-op cause. Round 1's 8i closed. |
| 3 | The false "line 37's pointer" clause was relocated to the G1 manifest rather than withdrawn | **THE EDIT LANDED; THE LEDGER'S REBUTTAL OF IT IS WRONG** | The clause is gone from §1.5 at `HEAD` and §1.5 now narrates the relocation accurately. But ledger §50's Revision 4 addendum says the finding "does not hold" and that "the clause was deleted in Revision 3." `git show HEAD~1` returns the clause verbatim. See New Finding 1. |

### The six cosmetic

| # | Round 4 cosmetic | Verdict | Evidence |
|---|---|---|---|
| 1 | `**Status:**` line ends "and it awaits a Round 2 review" | **PARTIALLY ANSWERED** | The tail is now "and it awaits a further review round." The rest of the line still says "**Revision 3** … after **three** independent adversarial reviews," and §7 still says "this is Revision 3 answering Round 3." See New Finding 4. |
| 2 | §1.5's completeness sentence is broader than the grep supports | **PARTIALLY ANSWERED** | Reworded to "returns only quotations inside the review artifacts and this pass's own ledger entry." The grep returns **seven** hits: four review artifacts, the ledger, **and the verification document itself** at line 63. See New Finding 3. |
| 3 | `basil-macrina-the-elder-letters`'s `discovery_channel` still says "both cited letters" | **NOT ANSWERED** | Line 29 verbatim unchanged: "both cited letters were located in the vendored file." The record's `work:` names three. Compiled content. |
| 4 | The generator would still regenerate a superseded record | **NOT ANSWERED** | `emit_source(79, …)` still passes `"named-not-rechecked"` and the short pre-verification `edition` string. Read in full at lines 1069–1085. |
| 5 | "(ledger SS47)" reads as a mangled "§47" in a compiled field | **NOT ANSWERED** | `cappadocian.source.amphilochius-iambics-to-seleucus.md:31` verbatim unchanged. |
| 6 | Round 3's cosmetics 2, 3, 4 and 5 are all untouched | **NOT ANSWERED** | Checked each individually. §4's gloss disclosure still names only the two Round 1 glosses; §3/§6.7 still call ledger §47 "stale"; §1.5 still says "with Boyd's independent English note listing the same eleven"; §5 line 136's causal phrasing is verbatim unchanged, now in its **fourth** round. |

### The four Round 3 items Round 4 listed as outstanding

- **IEA:161 / Doc_05 §29 "considered and left" — ANSWERED, and the judgment is right.** §1.5 now records it explicitly, in the form Round 2 asked for and Round 3 and Round 4 repeated. I read both passages. IEA:161 says "the communion law naming its bishops as touchstones"; Doc_05 §29 says "the communion law naming the region's bishops as touchstones — Documented at work level." Neither names an individual bishop, neither characterises the law's mechanism, and neither asserts exclusivity — neither says this world's men *were* the test, which is the overstatement the correction removes. **Both are accurate summaries and neither needs correcting.** Two qualifications, both minor and both below the bar: the stated ground ("without naming bishops") means *without naming individual bishops*, since both passages do use the word; and the list of "two occurrences considered and left" is under-inclusive (New Finding 5).
- **Round 3 cosmetics 2, 3, 4 and 5 — still unanswered**, as above.

**Count: 2 of Round 4's 3 substantial answered correctly; 1 answered in the document and mis-narrated in the ledger. Of the 6 cosmetics, 0 fully answered, 2 partially, 4 not answered. Round 3's outstanding substantial half is answered; its four cosmetics are not.**

---

## PART THREE — JOB 2: NEW DEFECTS INTRODUCED OR LEFT BY REVISION 4

None of the five below is substantial. Each is stated with the file, the line, and the replacement text, so that applying them directly requires no further investigation.

### 1. [COSMETIC — but the most serious item here] Ledger §50's Revision 4 addendum dismisses Round 4's third finding on a grep that tests a different proposition, and asserts a file history that `git show` refutes in one command. It also contradicts the verification document in the same commit.

**Location:** `CAPPADOCIAN_BUILD_LEDGER.md` §50, Revision 4 addendum, third bullet.

> "**The third finding does not hold, and is recorded as checked rather than accepted.** Round 4 reported that the false 'Doc_02 line 37's pointer' clause had been *relocated* into the G1 manifest rather than withdrawn. Direct check: `grep -rn "eleven\|line 37\|full eleven"` against `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md` returns nothing, and G1 carries no bishop names or pointer claim at all. **The clause was deleted in Revision 3**; what misled the review was that the same sentence named G1 among the corrected occurrences."

Three things are wrong with this, and one is right.

**Right:** the grep does return nothing. I ran it. G1 contains no "eleven", no bishop names, and no pointer claim.

**Wrong, first:** that grep tests the wrong proposition. Round 4 never claimed the clause had been written *into the G1 file*. Its finding is located at "verification document §1.5 (line 63)" and it quotes §1.5's own sentence. "Relocated to the G1 manifest" means the clause's **antecedent** changed — from Doc_02 §7 in Revision 2 to the G1 manifest in Revision 3 — not that text was added to G1. A grep confirming G1 has no eleven is therefore evidence *for* Round 4's finding (the clause was false about G1), not against it.

**Wrong, second:** "The clause was deleted in Revision 3" is false, and one command shows it:

```
$ git show HEAD~1:World-Builds/Cappadocian/cappadocian_Unused_Source_Verification_2026-09-09.md \
    | grep -o "the G1 manifest (which[^)]*)"
the G1 manifest (which now carries the full eleven, making Doc_02 line 37's pointer to it true for the first time)

$ grep -o "the G1 manifest (which[^)]*)" World-Builds/Cappadocian/cappadocian_Unused_Source_Verification_2026-09-09.md
(no output)
```

`HEAD~1` **is** Revision 3. The clause was live in Revision 3 and was deleted in **Revision 4** — by this same commit, correctly.

**Wrong, third:** the document says the opposite of the ledger, in the same commit. §1.5 at `HEAD`: "**three claims made about this sweep in earlier revisions are withdrawn outright rather than relocated:** that Doc_02 §2 'makes line 37's pointer true for the first time' (line 37 points at §2 and was always correct; **a later revision moved this clause to the G1 manifest instead of deleting it, where both halves were false too — it is now simply gone**)." That is an accurate account and it concedes exactly what the ledger denies. The skill's *Cross-document fact consistency* rule is written against precisely this shape.

**Why this matters more than its size.** The skill carries a standing rule — "A review finding is never dismissed as a tooling or environment artifact … without independent re-verification that actually confirms the dismissal. The finding stands until that re-check happens and actually supports the dismissal, not on the strength of the dismissal being asserted, however specific or confident it sounds." Revision 4 invokes that rule by name in the same bullet ("Per this project's own rule, a review finding is not dismissed as an artifact without an independent re-check that actually supports the dismissal — that re-check is the grep above") while breaching it. A future thread reading §50 will learn that a grep against the wrong file counts as a re-check, in the ledger entry whose central lesson is that a self-report is not evidence.

**Why it is nonetheless not substantial.** No claim about a source, a text, a confidence rating, a sourcing conclusion, or a scope boundary changes. The edit itself is correct and landed. The document under review narrates it correctly. Nothing compiled depends on it. The replacement text is fully determined by the two commands above, so a sixth adversarial round would verify a paste rather than discover anything. This is my closest call in the review and I set out both sides of it at Part Five (b).

**Fix.** Replace the third bullet with: "**Round 4's third finding held, and is recorded as checked.** Round 4 reported that the false 'Doc_02 line 37's pointer' clause had been re-pointed at the G1 manifest rather than withdrawn. Re-checked directly: the clause is verbatim in the Revision 3 commit (`git show 7c3ae3d:…Unused_Source_Verification_2026-09-09.md`) and is deleted here; and `grep -n "eleven"` against `cappadocian_G1_Scope_and_Source_Acquisition_Manifest.md` returns nothing, so the clause was false about G1 as well — which is what Round 4 said. G1 appears in §1.5's corrected-occurrences list on the strength of two real 2026-09-09 edits to it (the Amphilochius-gap qualification at line 92 and the Theodosian-Code update at line 93), neither of which involved the four-name string."

### 2. [COSMETIC] The Revision 4 addendum's opening understates Round 4's own count of what it left unanswered, in the pass's favour.

**Location:** `CAPPADOCIAN_BUILD_LEDGER.md` §50, Revision 4 addendum, first line: "3 new substantial findings, and **4 of Round 3's 12 not fully answered**."

Round 4's Part Two states: "**Count: 4 of 12 answered; 2 answered wrongly (4, 6); 2 partially (3, 5); 4 not answered.**" Not-fully-answered is therefore **eight**, not four; four is the number *answered*. The error runs in the direction of understating the pass's own defect count, which is the one direction that matters here.

**Fix.** "…and 8 of Round 3's 12 not fully answered (4 answered, 2 answered wrongly, 2 partially, 4 not answered)."

### 3. [COSMETIC] §1.5's completeness claim, restated for the fourth round, still under-enumerates — this time by forgetting the file it is written in.

**Location:** verification document §1.5, line 63; ledger §50, Revision 4 addendum.

The document: "`grep -rn "Helladius, Otreius, Gregory of Nyssa, and Amphilochius" .` returns only quotations inside **the review artifacts and this pass's own ledger entry**."

Run from the repository root it returns seven hits: `Round1:153`, `Round2:208`, `Round3:23`, `Round3:121`, `Round4:16`, `CAPPADOCIAN_BUILD_LEDGER.md:863` — and **`cappadocian_Unused_Source_Verification_2026-09-09.md:63`**, the sentence making the claim, which contains the string because it quotes the command. The **ledger's** version of the same sentence is correct ("the review artifacts, this ledger, and the verification document's own statement of the command"); the document's is not.

The operative claim — that no live occurrence of the four-name framing survives — is **true**, and I confirmed it: every hit is a quotation, none is a live assertion. This is an enumeration error inside a true sentence, which is why it is cosmetic rather than substantial. It is the same sentence Round 3 and Round 4 each had to correct.

**Fix.** Use the ledger's wording verbatim, which is the *Cross-document fact consistency* rule's own remedy: carry the exact wording across.

### 4. [COSMETIC] The document still identifies itself as Revision 3 answering Round 3, and still says every finding from the first three reviews is answered when four of Round 3's cosmetics verifiably are not.

**Location:** verification document line 6 (`**Status:**`) and §7, first paragraph.

Line 6: "**Status:** Revision 3 (2026-09-09), after three independent adversarial reviews … Every finding from all three is answered below or in the files it named."
§7: "Three rounds have each returned **substantial revision required**; this is Revision 3 answering Round 3."

This is Revision 4, answering Round 4, whose review artifact sits in the same folder and whose findings §1.5 narrates by name. Revision 4 fixed the six-word tail Round 4 quoted and left the sentence around it a revision behind — the same shape as Round 4's Cosmetic 1, which is now in its fifth round. And "every finding from all three is answered" is false: I opened all four of Round 3's outstanding cosmetics and all four are verbatim unchanged.

**Fix.** "Revision 4 (2026-09-09), after four independent adversarial reviews — … and `_Round4_Review.md` (8 of Round 3's 12 not fully answered, plus 3 new). Every substantial finding from all four is answered below or in the files it named; the outstanding cosmetics are listed at §6." And in §7: "Four rounds have each returned **substantial revision required**; this is Revision 4 answering Round 4."

### 5. [COSMETIC] "Two occurrences were considered and deliberately left" names two of a class with at least four members.

**Location:** verification document §1.5.

The judgment is right (Part Two above). The enumeration is not. Sweeping the whole class of "381 / communion law / touchstone" phrasings across `World-Builds/Cappadocian/` and `records/cappadocian/` turns up at least two more of exactly the same shape, neither mentioned:

- `cappadocian_Doc_05_Ecological_Reconstruction.md` **§53** — "the region's bishops named as the empire's touchstones (Documented at work level)." This is the *strongest* of the elliptical forms, since it omits "among" and reads closest to the exclusivity the correction removes. Still true, still an acceptable summary, and consistent with the pass's own judgment on §29 — but it should be inside the list, not outside it.
- `cappadocian_Forces_Document.md` line 169 — "what its bishops did as the establishment's touchstones."

For the record, the live records are in better shape than the narrative documents: `cappadocian.force.theodosian-settlement`, `cappadocian.contested.homoian-nicene-reversal` and `cappadocian.gravity.contested-church` all use the bounded "**among** the East's touchstones," which is Doc_02 §2's corrected form. `cappadocian.dw.power-and-its-discipline` uses the elliptical form at three places and is the same acceptable-summary class.

**Fix.** "Four occurrences were considered and deliberately left," adding Doc_05 §53 and the Forces Document Layer-1 gaps line, with the same one-clause ground.

---

## PART FOUR — CHECKED AND CLEARED

Stated so the record shows what a fifth round examined and held, including things it could have taken on trust from four prior rounds and did not.

1. **The word count, from the file, under both conventions, with a control.** 242 = 62 + 129 + 51 with-space; 240 = 60 + 129 + 51 without; `div2 17.24` = 629 with-space against the map's `~629`. Two rows, two exact matches — the convention is identified, not inferred. The corpus map is correct and now described as correct.
2. **The load-bearing decomposition.** Body **129**; two bracketed stretches of **25** and **14**, total **39**, and they are exactly the Old- and New-Testament book-lists; **90** rendered. "A canon-list poem with the canon list taken out" is fair, and these numbers have not moved since Revision 1 and have now been measured independently by four reviewers.
3. **The figure is consistent everywhere it lives, including compiled content.** Doc_02 §1.6, Registry row 117, the record's `divergence_note`, verification §3, and `compiled/repository.json`. Zero live occurrences of `279`, `87 words`, `63 words` or `~54`; the only survivors are inside the review artifacts and the ledger's own dated history of its earlier drafts, which is exactly where a superseded figure belongs.
4. **Registry row 11 matches the record it indexes.** `Epp. 204, 210 and 223` against `Epistles 204, 210 and 223`; `external_ids.cappadocian_source_registry_row: 11`; Doc_02 §1.4 agrees. The *Naming and term propagation* gap Round 1 opened at Finding 8i is closed. Table integrity verified across all 139 rows.
5. **The relocated clause is gone and §1.5 narrates it honestly**, including conceding that a later revision moved it rather than deleting it. That paragraph is the most candid in the document.
6. **The completeness sweep's operative claim is true.** Seven grep hits, every one a quotation, none live.
7. **G1's two 2026-09-09 edits are both good and both accurate** — the Amphilochius gap properly qualified ("an honest gap *as a corpus*, but not absolutely — about 90 rendered words … at Source Registry row 117") and the Theodosian-Code entry updated with the unmerged-branch fact stated plainly.
8. **The Macrina quotation.** One non-equal opcode across the whole aligned window: `,` → `.` at the bracket's close, exactly as the record discloses at lines 87–90. Nothing added, dropped or reordered. `modern_rendering` at **FK 5.55** against a ceiling of 10.
9. **Every number in §5.** Build succeeds; 18 gates, 17 pass; `voice-perspective` the one failure with the one finding; `determinism-check` `pass: true`, empty `differing_paths`; coverage 26/2/0; `staleness-check` `pass: false`, `cappadocian` the only stale world of eight; `pytest` 34/0. Package deleted; `git status` clean.
10. **Ledger §50's round-by-round counts check out against the four review files.** 14, then 11, then 7, then 3 new substantial findings: verified by opening each. The addendum's one loose phrase — "Every round has independently re-verified the underlying substance and found it sound" — is not true of Round 1, which is what *corrected* the substance; but the same sentence's trailing clause ("have not moved since Revision 1") states it accurately, and the same entry elsewhere uses the precise form. Below the bar for a finding.
11. **The restraints all held for a fifth round.** `formation_confidence: Inferential-Thin` unchanged; no figure record manufactured for Macrina the Elder; the `voice-perspective` false positive still not quietly fixed; Doc_04 not revised and no gravity classification moved; row 65 corrected rather than deleted; row 117 at B; the new source record at `verified-via-authority`; the verification builds deleted rather than committed; the staleness failure left failing on purpose. Five rounds, no slippage on any of them.
12. **The document still claims no disposition**, still escalates the Amphilochius correction against its own interest, and §7's escalation analysis is tested category by category against the skill's actual text rather than a paraphrase.
13. **The Revision 4 addendum's closing paragraph does not overclaim.** It names the cost of four rounds plainly, does not claim the cosmetics were fixed, does not claim a disposition, and puts the question of whether a fifth round is worth running to the project lead. That is the right posture, and it is why the one bad bullet above stands out rather than blending in.

---

## PART FIVE — THE BOTTOM LINE

### (a) Is the substance sound?

**Yes — and for the first time in five rounds, without exception.**

The five candidate verifications, the Doc_04 supplemental judgment and its refusal to close Open Item 1, the Amphilochius correction and its grade (B / `verified-via-authority`), the Macrina quote and its C-E placement with both halves of the sentence carried, the Thaumaturgus corpus-map row and the Firmilian escalation, and the compile/gate/staleness posture are all correct, and are now four times independently re-verified. Nothing needs reverting.

Round 4 had to write one exception: the `div2`'s size was misstated in compiled content and the corpus map was wrongly called unreconcilable. **That exception is gone.** I measured the section from the file before reading the document's claim about it, confirmed the convention against a second row, and confirmed the corrected figure in the rebuilt package. The conclusion that carries the weight — about **90 rendered words** inside a **129-word** body of which **39** are the editor's brackets, a canon-list poem with the canon list removed — is exact, and it has been exact since Revision 1.

### (b) Cosmetic, or substantial? Applying the skill's rule literally.

The rule, from the skill's own text as loaded in this session:

> "A revision is **substantial** if it changes a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary — anything a careful reader would notice as actually different. A revision is **not substantial** if it's wording, tone, formatting, or a typo fix."

Tested item by item:

| item | claim's substance? | confidence rating? | sourcing conclusion? | scope boundary? |
|---|---|---|---|---|
| 1 — ledger's G1 rebuttal | no claim about the world, its sources or its texts changes; the edit is correct and correctly narrated in the document | no | no | no |
| 2 — "4 of 12" | a count of a review's own dispositions | no | no | no |
| 3 — grep enumeration | the operative claim is true; the list of quotation sites is short by one | no | no | no |
| 4 — Revision 3 / three reviews | the document's own version label | no | no | no |
| 5 — "two occurrences" | the judgment is right; the list is short by two | no | no | no |

**Nothing remaining meets the substantial bar. No substantial revision required. The five items above may be applied directly, without a further review cycle.**

The honest counter-argument, stated so it can be weighed rather than buried. Round 4 held that "false claims that a fix landed" are "the class the *Revision decision* rule cannot absorb, since applying such a fix 'directly' is exactly what produced them." That argument was right when it was made: there were three such items, one of them a wrong measurement of a primary text sitting in compiled content and in a cleared master document, another a Registry row that four documents said had been edited and that had never been touched. Each of those was a fact about the world or its sources.

It does not carry here, for four reasons I can show rather than assert. **First**, every fix Revision 4 claims actually landed — I opened each file at each line and rebuilt the package to check the compiled ones. **Second**, the one remaining mis-narration sits in a ledger addendum, not in the deliverable; the deliverable says the right thing about the very same edit. **Third**, no world content, confidence, sourcing conclusion or scope boundary is touched by any of the five. **Fourth**, the replacement text for all five is fully determined and set out above with the commands that establish it, so a sixth round would be verifying a paste, not discovering anything. The purpose of routing a substantial revision back through review is that the fix might itself be wrong or might ramify. Neither risk is present.

I want to be explicit that I looked for a reason to say the opposite, because four rounds of "substantial" create their own gravity. The strongest candidate is New Finding 1, and on a maximally literal reading — "changes a claim's substance," where the claim is "Round 4's third finding does not hold" — it clears the bar. I resolved it the other way because the rule's four categories are about the substance of what the document *asserts about its subject*, and because the alternative is a fifth adversarial round whose entire yield would be confirming that one ledger paragraph was rewritten to say what this review already establishes with two `git` commands. **If the project lead reads the rule the other way on New Finding 1, that is a defensible reading and I would not argue with it** — but it should be his call, made knowing that the substance is now clean, not a sixth round entered by default.

One condition on the clearance, and it is not optional: **New Finding 1 must actually be applied, not merely noted.** A ledger that records a review finding as "does not hold" when it held is the one item here that will mislead a future thread, and it is in the entry whose stated purpose is to teach that a self-report is not evidence. If the build thread disagrees with my adjudication of it, that is a genuine two-reviews-disagree situation and belongs in **escalation category 4** — logged as a disagreement and taken to the project lead — not settled by siding with whichever account is most recent, which is what the skill's *Revision decision* rule explicitly forbids.

### (c) What a reader should still know is imperfect, and what still needs the project lead

Clearing this does not make it finished. All of the following survive the five direct fixes:

- **The `div2`'s size has now been stated five different ways in five drafts** (~240; 59+129+~54=242; 63+129+87=279; and the correct 62+129+51=242). The current figure is right and I have measured it, but a reader meeting this number in Doc_02 or the Registry should know it has a history, and should trust the **129 / 39 / 90** decomposition above all, which has never moved and which four reviewers have now independently measured.
- **The world is stale on purpose, and nothing here is live.** The pin `packages/cappadocian/2026-09-04T16-41-51Z` contains none of these changes; `staleness-check` correctly fails. Nothing in this pass reaches the Representative until the project lead authorizes the recompile-and-re-pin at §6.1. The document says this well and it remains the most important sentence in it.
- **`wb_cappadocian_s21.py` is a superseded first-pass generator and a live foot-gun.** Re-running it would restore `named-not-rechecked` and the short pre-verification `edition` on row 79 and clobber much else. Only its `work` string has been brought into line. It is not in the compile path and nothing runs it — but nothing says so on its face either.
- **The compiled `modern_rendering` was edited twice and disclosed once.** §4 records the two Round 1 glosses; the Round 2 rewrite that dropped it from FK 11.3 to 5.55 is recorded in §5 as a regression but never as a second edit to a compiled field, in a document whose §5 says "Recorded rather than silently fixed."
- **`cappadocian.source.basil-macrina-the-elder-letters` says two things about how many letters it rests on.** `work:` names three; `discovery_channel` and the body still say "both cited letters." Compiled content, third round unfixed.
- **The two Latin witnesses may not be independent**, Boyd's vendored scan corrupts two of the eleven personal names, and the Latin quoted at §1.1 is normalized rather than transcribed. The first and third are disclosed carefully; the second is not disclosed at all, and §1.5's "Boyd's independent English note listing the same eleven" is still unqualified after three rounds of being flagged.
- **"(ledger SS47)" sits in a compiled field** as a mangled section sign.
- **Eight items at §6 still need the project lead**, and none of them has been seen by him: the recompile-and-re-pin spend authorization; the Firmilian corpus-map granularity ruling; the acknowledgement that a cleared document's sourcing conclusion (Registry row 65, Doc_02 §1.6) was wrong; the two Doc_04 open-list re-weightings (Open Item 1 toward Supporting, Open Item 9's stale caveat); the `voice-perspective` false positive belonging to another record's owner; the proposed standing availability-check, which would be a methodology change and is correctly proposed rather than adopted; ledger §47's stale precedent citation; and the `records_commit` stamp behaviour in `engine/m2/cli.py`.
- **This document is not indexed anywhere.** §6 says so and duplicates the open items into ledger §50 for that reason. That mitigation is only as good as the ledger, which is why New Finding 1 matters more than its size.

---

## CLOSING VERDICT

**No substantial revision required.** Five cosmetic items remain, each named above by file, line and replacement text; they may be applied directly without a further review cycle. The document has not reached any disposition — it is eligible for one, and per the skill that decision belongs to the build thread only after the escalation categories are tested, which §7 does, and which sends the Amphilochius correction, the Firmilian split and the two Doc_04 items to the project lead regardless.

What changed between Round 4 and Round 5 is not the pattern's disappearance but its size. The four earlier rounds each found the pass asserting something about a file, a command or a measurement that opening the file would have disproved — and each time the thing asserted was a fact about a primary text, a Registry row, or a cleared master document. Revision 4 finally got all of those right: the section is 242 words and the corpus map was correct all along; row 11 names three letters and matches the record it indexes; the false clause is deleted; the quote is verbatim; the battery reproduces to the number. What is left is one ledger paragraph that says a review finding did not hold, when `git show HEAD~1` shows it did — and four short lists that are each one or two entries short, including one that forgets the document it is written in.

That is a real defect and it is the fifth consecutive instance of the same species. It is also, finally, not a claim about anything in the world this build exists to represent. The lesson the ledger already draws is the right one and worth carrying forward verbatim: *a self-report is not evidence, and an unasserted string replace is a silent no-op.* The fifth-round successor to it is narrower still, and it is the one command this revision did not run: **before you tell a ledger that a review was wrong, check out the commit the review was reviewing.**
