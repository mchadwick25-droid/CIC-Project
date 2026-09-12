# Post-Admission Source Finding (Philostorgius / *Opus Imperfectum*) — Round 5 Independent Adversarial Review

**Reviewed document:** `Post_Admission_Source_Finding_Philostorgius_OpusImperfectum_2026-09-09.md`
**Also reviewed:** `Open_Gaps_Tracking.md` item 16, in full including its indented sub-block, for consistency with the above
**Reviewer:** independent isolated agent (Opus), no drafting involvement in the reviewed document, in item 16, or in any prior review
**Branch reviewed:** `claude/ijc-philostorgius-opus-imperfectum-finding`, at `a3fdd20e` ("ijc: Round 4 adversarial review + fourth revision"). The document did not move under this review.
**Round 5 findings are numbered S1–S10.**
**Scope:** deliberately narrow, on Round 4's own recommendation and the commissioning brief's instruction. The argument is not re-litigated. §6, propagation, the Q1–Q17 fixes, the logged Q3 disagreement, fifth-generation errors in newly-written text, and the standing checks.
**Overall verdict: SUBSTANTIAL REVISION REQUIRED**

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

---

**Bottom line.** §6 — the section that has now gone stale twice — is, this round, **correct in every claim it makes**. I checked the escalation count and both its items, the number of rounds filed, which round is next, the logged-disagreement item and the standing note against the status line, §5, §7 and item 16 individually, and they agree. That is the first time in five rounds that the section gating self-disposition has been clean, and it should be said plainly.

**The Q3 disagreement is honest and I reproduced it exactly.** Reconstructing the original pattern as specified — `^\s*["\']([a-z0-9_-]+)["\']\s*:` under `re.M`, applied to `src[src.index('COVERAGE = {'):]`, i.e. to end of file — and differencing its 50 unique keys against the 60 distinct corpus keys in `cic/texts/` yields **exactly 22 keys**, and the 22 are **member for member the list Round 3 quoted from Round 2**, including all six `npnf1xx` entries Round 4 said such a regex could not have missed. Round 4's Q3 assumed a scope the original did not have. It does not stand, the document says so accurately, and it does not use the disagreement to wave anything away — it accepts the underlying criticism, restates the cause completely, and escalates the tension at §6. This is the rule in `cic-build-cycle` working as written.

**What has failed, for the fifth consecutive round, is propagation — and this time it failed in `Open_Gaps_Tracking.md`.** The Q5 correction and the Q2 correction both reached item 16's opening paragraph and stopped there. Item 16's indented sub-item (3), untouched by commit `a3fdd20e`, still carries the uncorrected claim *"stated wrongly three times across three revisions"* and still attributes the deletion to *"Mark's instruction of 2026-09-09"* with none of the unverifiability disclosure the rest of the revision was written to add. Round 4's Q1 caught the correction reaching everywhere except §6; Round 5 catches it reaching everywhere except one indented block of the same log entry that was itself edited in the same commit.

**And §7's own Round 4 entry misreports Round 4.** Its last bullet reads *"Q9 and seven LOWs — the repo-root grep figure is now given as an order of magnitude."* Q9 is a MEDIUM about missing review-artifact paths and was not acted on; Round 4 filed **eight** LOWs (Q10–Q17), not seven; and the change described is **Q16's**. So the entry written to record the fix for Q7 — the finding about misdescribing what was changed on low-severity findings — reproduces Q7 one generation later, against Round 4's own findings. That is the fourth generation of the same defect (F13 → R19 → Q7 → here).

---

## Part 1 — §6, verified claim by claim

| §6 claim | Checked against | Result |
|---|---|---|
| Representative identity/name/title: not touched | whole document | ✔ true |
| Portfolio-level or cross-world: **two** | §2.4 (a) and §5 item 4 (b) | ✔ both present and live |
| (b) "reaches more than one world" | §5 item 4: *"the mislabelling is not confined to this world … the per-world report covers most but not all of the built worlds"* | ✔ supported, and it no longer cites a count §5 has stopped giving. **Q1's specific complaint is fixed.** |
| "Corrected from 'one' at Round 2 (F10)" | §7 Round 2 entry, F10 bullet | ✔ matches |
| Governance/methodology: not touched | whole document | ✔ true |
| Unresolved tension: **one**, the logged Q3 disagreement, "recorded at §5 item 4" | §5 item 4 | ✔ present (but see **S7** — as rendered it falls outside item 4) |
| "three live judgment calls (recompile, corpus-map role, who owns the engine fix), escalated at §5" | §5 items 1, 2, 4 | ✔ accurate |
| "**Four** independent adversarial review rounds have been filed as files" | `Review-Artifacts/` on disk | ✔ four files exist |
| "every one returning SUBSTANTIAL REVISION REQUIRED" | all four review files | ✔ |
| "Rounds 3 and 4 both stated explicitly that the verdict was not on the finding's answer" | Round 3 header; Round 4 verdict *"Not on the answer"* | ✔ |
| "a **Round 5** is required before any disposition is considered" | status line, §7 close, item 16 | ✔ three-way agreement |
| "This thread does not score its own result … nothing here is Approved to proceed or Frozen" | whole document | ✔ |
| Standing note: stale "after Round 1 (Round 2, F11)" and "after Round 3 (Round 4, Q1, where it still claimed two rounds and a pending Round 3 while carrying a count §5 no longer stated)" | Round 2 F11; Round 4 Q1 | ✔ accurate on both, including the detail of what Q1 found |

**§6 passes.** One residue only, carried as **S4**: §6 names no review-artifact file paths, which Round 4's remedy #1 explicitly asked for and which `cic-build-cycle`'s Disposition section requires of the log.

## Part 2 — Propagation sweep

Every figure and round-number in both files grepped and traced.

**Agreement on the three things that must agree:**

| | rounds filed | next round | disposition |
|---|---|---|---|
| Status line (l. 3) | four | Round 5 | "Not disposed" |
| §6 (l. 223) | four | Round 5 | "none, and none is claimed" |
| §7 close (l. 292) | four | Round 5 | "none. DRAFT." |
| Item 16, opening ¶ | four | Round 5 | "no disposition is claimed" |

✔ All four agree. Round 1 tallies (four HIGH, eight MEDIUM, four LOW) and Round 2 tallies (two new HIGH, eight MEDIUM, six LOW) match between §7 and item 16 and match the review files' own headings.

**Corrected claims surviving verbatim elsewhere — the class Rounds 3 and 4 each found:**

- **Found, twice, in `Open_Gaps_Tracking.md` item 16 sub-item (3).** See **S1** and **S2**. Commit `a3fdd20e` changed exactly one line of that file — item 16's opening paragraph — and left the indented sub-block that repeats both corrected claims.
- Clean in the finding document itself: no surviving "six worlds", "all seven worlds", "14 keys", "18 files" or "22" presented as a current count. The historical figures at §7 (F5's *"all seven worlds"*, R1's recount) are correctly framed as what a superseded pass said. One residue at **S9**.
- The `36`/`38` repo-root figures at §7's H1 and H1-did-not-hold bullets are stated in the present tense while §1(1) has deliberately abandoned exact figures for that metric — **S9**, LOW.

## Part 3 — Round 4's Q1–Q17: does each fix hold?

| | Round 4 finding | Verdict | Where |
|---|---|---|---|
| Q1 | HIGH — §6 stale a second time | **HOLDS** — §6 rewritten and correct in every claim (Part 1); standing note added and accurate | residue at S4 |
| Q2 | HIGH — verbatim project-lead quotation, no verifiable record | **HOLDS in the finding document. DOES NOT HOLD in `Open_Gaps_Tracking.md`** | **S1** |
| Q3 | HIGH — regex diagnosis false | **Does not stand — independently reproduced; the document is right and Round 4 is wrong** | Part 4 |
| Q4 | MEDIUM — Tier 1 bound inoperative | **HOLDS** — verified against `engine/m1/cross_world.py` (Part 4) | — |
| Q5 | MEDIUM — "three times across three revisions" | **HOLDS in the finding document. DOES NOT HOLD in item 16 sub-item (3)** | **S2** |
| Q6 | MEDIUM — pre-sorting an unfiled review's findings | **HOLDS** — withdrawn in §7 and gone from item 16, replaced by a plain record of the two process errors | — |
| Q7 | MEDIUM — Round 3 LOW tally misrepresented, R12/R13 mislabel | **HOLDS in part** — mislabel corrected to R13, "nine further LOWs" completeness implication removed; **DOES NOT HOLD** on the promise that the seven outstanding are "named here" — none are named | **S5** |
| Q8 | MEDIUM — Dekkers assigned to a third channel | **HOLDS** — now explicitly left unattributed, all three failed attributions listed, and both blocked hosts named | — |
| Q9 | MEDIUM — item 16 names one artifact path for multiple verdicts | **DOES NOT HOLD** — now four verdicts, still one path; §6 names none | **S4** |
| Q10 | LOW — 300–425 / 312–451 without locator | **DOES NOT HOLD** — unchanged, fourth consecutive round | S8 |
| Q11 | LOW — Candidate 6 a bare negative | **DOES NOT HOLD** — unchanged | S8 |
| Q12 | LOW — "Confidence A" shorthand in §7 and item 16 | **DOES NOT HOLD** — one instance in each file, unchanged | S8 |
| Q13 | LOW — README l. 168 quotation presented as complete | **DOES NOT HOLD** — unchanged | S8 |
| Q14 | LOW — un-indented block breaking out of §5's list | **DOES NOT HOLD, and worse** — grown from four paragraphs to five | **S7** |
| Q15 | LOW — §0's "paraphrased" overstates | **DOES NOT HOLD** — l. 13 unchanged | S8 |
| Q16 | LOW — repo-root figure stale | **HOLDS** — now "a few dozen files repo-wide", the right response to a self-referential metric — but mislabelled as Q17 | **S6** |
| Q17 | LOW — "no unsupported project-lead attribution … across all three rounds" sits above one | **Substantively moot** (the attribution it sat above is repaired), sentence unchanged and undisposed | S8 |

**Six of seventeen hold outright; one is correctly disputed; two hold in the finding document and fail in the tracking file; eight do not hold.**

## Part 4 — The logged Q3 disagreement, verified myself

**Reconstruction, run directly against `engine/m1/cross_world.py` at `a3fdd20e`:**

- Pattern `^\s*["\']([a-z0-9_-]+)["\']\s*:`, `re.M`, applied to `src[src.index('COVERAGE = {'):]` — end of file, not the `COVERAGE` block: **81 matches, 50 unique keys.**
- The same pattern scoped to the `COVERAGE` literal alone returns **13** keys — exactly Round 4's simulation, which confirms Round 4 computed what it said it computed.
- `cic/texts/` holds **65** `.xml`/`.txt` files under **60** distinct `corpus_key`s. 60 keys minus the 50 the unscoped pattern found = **22 keys**, namely: `anan-isho`, `anf10`, `basil`, `eunomius`, `evagrius`, `gregory-nazianzen`, `gregory-nyssa`, `julian`, `lucian`, `macarius`, `morison`, `nestle1904`, `npnf102`, `npnf103`, `npnf106`, `npnf108`, `npnf110`, `npnf114`, `pachomius`, `philostorgius`, `tacitus`, `webbe`.
- That is **identical, member for member and with no additions or omissions, to the twenty-two Round 3's R1 quoted from Round 2** — including the six `npnf1xx` keys Round 4 held such a pattern could not have produced, and excluding the twenty-five mid-line keys Round 4 held it could not have found. Both facts fall out of the pattern running past `BY_DESIGN` into `REGIONS` and the later dictionaries, where those keys sit line-initial.

**The document's reproduction is honest.** Its stated correction — that the pattern was *both* unscoped *and* line-anchored, and that the first attempt disclosed only the second half — is the correct and complete diagnosis, and it is now the checkable kind of claim the last four rounds have been asking this item for.

**And it is logged in the manner `cic-build-cycle` requires**, not used as an escape hatch. The disagreement is recorded explicitly at §5 rather than resolved by deferring to the most recent review; the review's *underlying* criticism (a mechanism asserted more confidently than checked) is accepted, not just conceded; the cause was rewritten rather than left standing; and §6 escalates it under the fourth escalation category rather than closing it. Nothing about the disagreement is used to reduce the force of any other Round 4 finding — Q1, Q2, Q4, Q5, Q6, Q7 and Q8 were all accepted on their merits.

**Q4 verified independently.** Direct parse of the module: `COVERAGE` has **44** keys, `AUTHORS` **41**, and `AUTHORS ⊂ COVERAGE` is **true with no exceptions** — a strict subset. `corpus_tier()` returns `"1 - named, never opened"` only when `named` is true, and `named` is derived from `_AUTHORS_BY_FILE`, built solely from files whose `corpus_key` is in `AUTHORS`. So no volume lacking a `COVERAGE` entry can ever render as Tier 1, exactly as §5 item 4 now states. The replacement mechanism it gives — already-sourced volumes dropping off a world's worklist — is the one Round 4 demonstrated. Correct and accepted.

## Part 5 — Fifth-generation errors in newly-written text

Restricted to what commit `a3fdd20e` actually wrote: the rewritten §6, the Q3 disagreement note and Q4 correction in §5 item 4, the Round 4 entry in §7, and the changed sentence of item 16.

- **§6:** clean (Part 1).
- **§5's Q3 note:** clean and verified. Its quotation of Round 4 ("13 keys and a cohort of 47") matches the review file.
- **§5's Q4 note:** clean and verified against the engine.
- **§7's Round 4 entry — does it accurately describe what was changed?** Mostly, with two failures. Q1–Q8's bullets are accurate against the review file and against the current text. **The Q9-and-LOWs bullet is not (S3), and the Round 3 entry's rewritten LOW bullet claims a naming it does not perform (S5).** One further inaccuracy: §7's Q7 summary says the LOW tally was corrected "and seven outstanding LOWs named"; the commit message repeats it. Neither is true.
- **§7's claim that Round 4 "recomputed §5 item 4's post-Round-3 figures … and found every one of them correct":** ✔ accurate — Round 4's Half A part 1 table verifies six figures and the fourteen-key list member for member.
- **§7's Half B and process-finding paragraphs:** ✔ accurate against Round 4's sections 4 and 5, including that Half B dissents from what was done.
- **Item 16's changed sentence:** accurate, and it is the sub-block *below* it that failed (S1, S2).

## Part 6 — Standing checks

- **Fabricated quotations:** none found. Every quotation in the newly-written text traces to the Round 4 file. Spot-check of the unchanged argument sections: `cic/texts/README.md` l. 168, `Source_Registry.md` rows 4 and 24, the Doc_02 §7 quotations and the Philostorgius chapter attributions are as three prior rounds verified them, and nothing in §1–§4 changed in this revision.
- **Project-lead attribution without a verifiable record:** repaired in the finding document (own voice, unverifiability disclosed, consistent with §0). **Surviving once in `Open_Gaps_Tracking.md` — S1.** A standing observation at **S10**: paraphrase-plus-disclosure is Round 4's prescribed mitigation, not satisfaction of the rule, which asks for a checkable record.
- **Claimed verification not performed:** none found. The two new verification claims (the regex re-run, the `AUTHORS`/`COVERAGE` subset) both reproduce exactly when run independently.
- **Self-scoring or pre-declared disposition:** none. §6 and §7 both refuse a disposition; the Q6 pre-sorting is withdrawn in both files and no equivalent has been reintroduced. §7's adoption of Round 4's scoping recommendation for Round 5 is a disclosed adoption of the *review's* recommendation, not a pre-judgment of its outcome.
- **No claim about the headline verdict changed in this revision.** The diff of `a3fdd20e` touches §0's status line, §1(1), §3.1's Dekkers sentence, §5 item 4, §6 and §7 only. §2.2, §2.3's six-candidate table, §2.4, §3.2 and §4 are untouched. Spot-check confirms the answer, the "supplemental" verdict, the Hilary-alone holding and the Doc_04/05/08/09 "unchanged" statements read exactly as Round 4 left them.

---

## Findings

### HIGH

**S1. Round 4's Q2 fix stops at item 16's opening paragraph. The indented sub-item (3) below it still attributes the deletion to the project lead with no unverifiability disclosure.**

`Open_Gaps_Tracking.md` item 16, sub-item (3), line 113: *"**No count is given deliberately:** … and Mark's instruction of 2026-09-09 was to drop the enumeration and state the defect qualitatively — the precision was never load-bearing …"*

Item 16's opening paragraph, rewritten in the same commit, now reads *"Mark's resolution, 2026-09-09, given in session and restated here in this thread's own words rather than quoted (an off-repository instruction with no record a later reader can open)."* The disclosure exists. It exists ten lines above a second, undisclosed restatement of the same instruction in the same log entry. A reader who reaches sub-item (3) — which is the operative flagged item, the one an engine-fix ticket would be written from — reads a bare project-lead instruction of the kind `cic-build-cycle` holds to the same bar as Frozen, with no marker that it is unverifiable.

This is not a quotation any more (no quotation marks survive around it anywhere in either file — I grepped the repository for the instruction's wording and found it at §7 l. 275 and the Q2 bullet at l. 282 of the finding document and at item 16's opening paragraph, all three carrying the disclosure; at item 16 sub-item (3), which does not; in the Round 4 review file; and in the commit message). The residue is the *attribution without the disclosure*, in the one place a later reader is most likely to act on it. HIGH because it is a named CO-022 failure mode, because it survived the very revision written to close it, and because it survived inside a file that commit `a3fdd20e` edited.

**S2. Round 4's Q5 correction likewise stops at item 16's opening paragraph. Sub-item (3) still says "three times across three revisions" — the exact claim the finding document corrected.**

The finding document, §5 item 4, now reads *"stated them wrongly three times across two revisions (the third revision's figures were, on Round 4's own recomputation, correct — Q5)."* `Open_Gaps_Tracking.md` sub-item (3) still reads *"the scale figure was stated wrongly three times across three revisions, twice overstating the defect."*

Round 4 established, by direct recomputation of all six figures before their deletion, that the third revision's figures were correct. The tracking log — the artifact the project lead reads, and the one the skill's Disposition section designates as the record — still states the opposite, and still supplies the stronger warrant for the deletion that Q5 found unsupported.

This is textually the same defect as Round 3's R2 and Round 4's Q1: a corrected claim surviving verbatim in a location the correction did not reach. It is the fifth consecutive round in which this class has been found, and the second consecutive round in which the correction reached four places and missed the fifth. HIGH on the class, not on the magnitude of the arithmetic.

### MEDIUM

**S3. §7's Round 4 entry misreports Round 4's own findings: it merges a MEDIUM that was not acted on into a LOW disposition, undercounts the LOWs, and describes the wrong finding.**

§7, final bullet of the Round 4 entry: *"**Q9 and seven LOWs** — the repo-root grep figure is now given as an order of magnitude, since it is a self-referential metric this document changes by being written."*

Three errors in one sentence:

- **Q9 is a MEDIUM, not a LOW**, and it is about item 16 naming one review-artifact path while reporting multiple verdicts. It was not acted on (S4). Folding it into a bullet of fixes reports it as disposed.
- **Round 4 filed eight LOWs, Q10–Q17**, not seven.
- **The change described is Q16's**, not Q9's and not the LOW cohort's collectively. Q10–Q15 and Q17 receive no disposition at all — neither "fixed" nor "declined".

Round 2's F13, Round 3's R19 and Round 4's Q7 are all this same finding: a reader cannot tell declined from missed. This is its fourth generation, and it appears in the entry written to record the fix for the third.

**S4. Q9 does not hold. Item 16 names one review-artifact path against four reported verdicts; §6 names none.**

`cic-build-cycle`, Disposition: the log records *"where each review artifact file lives."* Item 16 links only `Review-Artifacts/PostAdmission_Source_Finding_Round1_Review.md` and then reports Round 2's, Round 3's and Round 4's outcomes with no paths. §6 says the four rounds are "filed as files in `Review-Artifacts/`" and names none of them. Round 3 filed this at LOW with one path missing; Round 4 raised it to MEDIUM with two missing; there are now three missing, and Round 4's remedy #1 named this explicitly (*"add the Round 2/Round 3 review paths to item 16 and to §6"*).

Raised rather than left at LOW because the same file already does this correctly for its own item 1, which links all three of its round artifacts — the house pattern exists ten screens above the entry that omits it, so this is not an unsettled convention.

**S5. §7's rewritten Round 3 LOW bullet claims to name the seven outstanding LOWs and names none.**

*"Seven of Round 3's ten LOWs remain untouched and are named here as outstanding rather than absorbed (Round 4, Q7 …)."* They are R12, R14, R15, R16, R17, R20 and R21 — Round 4 lists them. The bullet lists none. The mislabel Q7 caught (R12 for R13) is correctly fixed and the false completeness implication is correctly removed; the substitute assertion is that the outstanding ones are named, and that assertion is false about its own sentence. Same class as S3, one entry higher up the same section.

### LOW

**S6. §1(1) credits the order-of-magnitude change to "Round 4, Q17". It is Q16.** Q17 is the clean-list sentence about project-lead attribution. Exactly the mislabel class Q7 raised about R12/R13, in text written in the same revision that fixed that one.

**S7. Q14 does not hold and has worsened; as rendered, §5 item 4 ends four paragraphs before the document thinks it does.**

The column-0 block inside item 4 has grown from four paragraphs to **five** — lines 198, 200, 202, 204 and 206 — while lines 194, 196, 208 and 210 sit at four spaces. Two consequences beyond the presentational one Round 4 recorded:

- Under CommonMark the list is terminated at line 198, so lines **208 and 210 — four-space-indented paragraphs following a column-0 paragraph — render as indented code blocks.** Those two paragraphs carry Mark's 2026-08-26 *"ranked, but not ignored"* standard, the `engine/m4`-never-opens-`cic/texts/` mechanism, and the statement that engine code is outside a build thread's write scope. The most load-bearing prose in the item renders as preformatted text.
- §6's pointer *"a logged disagreement … recorded at §5 item 4"* is, as rendered, false: line 204 falls outside item 4. The claim is true of the source file and false of the document a reader sees.

Held at LOW because nothing substantive is misstated and the fix is four whitespace edits, but flagged because it is now the third round on the same finding (R20 → Q14 → here) and it has degraded each time.

**S8. Six of Round 4's eight LOWs are unchanged and undisposed.** Q10 (300–425 / 312–451 asserted without its locator, now fourth consecutive round — Round 4 supplies both locators, vendored file line 50 and `records/worlds.yaml` line 152); Q11 (Candidate 6's bare negative); Q12 ("Confidence A" shorthand, one instance in each file); Q13 (the `cic/texts/README.md` line 168 quotation presented as complete); Q15 (§0 line 13's near-verbatim "paraphrase", third consecutive round); Q17 (the clean-list sentence, now substantively moot but untouched and unacknowledged). Declining a LOW is a perfectly good answer and this review does not ask for any of them to be fixed. Saying nothing is the defect, and it is the same one as S3 and S5.

**S9. §7 states the repo-root `untranslated` figure as current fact in two places while §1(1) has deliberately abandoned exact figures for that metric.** *"H1 — a claimed repo-wide grep that returns 36 files"* and *"Count corrected 36 → 38"*. Round 4's Q16 measured 39 case-sensitive / 40 case-insensitive, and the metric increments with every review artifact filed. The framing is historical and therefore defensible, but the H1 bullet's present tense presents a superseded number as the current one, in the same document that explains two hundred lines earlier why it will no longer do that.

**S10. Standing observation, not a defect introduced by this revision: paraphrase-plus-disclosure is a mitigation of the project-lead attribution rule, not compliance with it.** `cic-build-cycle` asks for *"a real, checkable record, not a claim"*, held to the same bar as Frozen. The finding document now does everything a build thread can do unilaterally — own voice, marked off-repository, marked unverifiable, consistent with §0's treatment of the commissioning brief — and Round 4 prescribed exactly this remedy. But Round 4 also offered a second and cleaner route: restate the deletion as the build thread's own decision, which it is entitled to make, since an enumeration is not a claim, a confidence rating, a sourcing conclusion or a scope boundary. Only the project lead can close this by producing a record; recorded so a later reader does not read the disclosure as having discharged the rule.

---

## What checked out clean

- **§6 in full** — every claim, against the status line, §5, §7 and item 16. First clean pass in five rounds for the section that gates self-disposition, and the standing note it now carries is accurate about both prior failures.
- **The Q3 disagreement** — independently reproduced to the exact figure and the exact 22-key list; honestly stated; correctly logged and escalated rather than used to blunt anything else.
- **The Q4 correction** — verified against `engine/m1/cross_world.py` by direct parse. `AUTHORS` (41) is a strict subset of `COVERAGE` (44); the Tier 1 pre-emption genuinely cannot reach this cohort.
- **Q6** — the pre-sorting of an unfiled review's findings is withdrawn in the finding document and gone from item 16, replaced by a plain record of both process errors against the thread's own interest.
- **Q8** — the Dekkers dating is left unattributed, all three prior misattributions are listed with the round that caught each, and both egress-blocked hosts are named.
- **Rounds filed / next round / disposition** — four-way agreement across the status line, §6, §7 and item 16's opening paragraph.
- **The headline verdict and its supporting sections** — untouched by this revision, as the diff confirms. Not re-litigated here, per scope.
- **No fabricated quotation, no fabricated verification claim, no self-scoring, no pre-declared disposition** anywhere in the newly-written text.

## Disposition readiness, and whether a sixth round is warranted

**The remaining defects are not purely cosmetic, so I cannot return COSMETIC ONLY.** S1 breaches a rule the skill holds at its highest bar, in the artifact the project lead actually reads. S2 leaves an uncorrected factual claim about the document's own error history standing in that same artifact, after the correction was made in the finding document. S3 and S5 misreport what a filed review found and what was done about it. Those are substance, not wording.

**But a sixth adversarial round of the present kind would add very little, and I would say so to anyone proposing one.** Everything outstanding is mechanically checkable and none of it requires judgment:

1. Edit `Open_Gaps_Tracking.md` item 16 sub-item (3): "three revisions" → "two revisions", and carry the same unverifiability disclosure the opening paragraph already has (S1, S2).
2. Rewrite §7's last Round 4 bullet to say what was actually done: Q16 fixed; Q9 outstanding; Q10–Q15 and Q17 declined, listed by number (S3, S8).
3. Name the seven outstanding Round 3 LOWs in the bullet that says they are named (S5).
4. Add the Round 2, 3 and 4 artifact paths to item 16 and to §6 (S4).
5. Q17 → Q16 at §1(1) (S6); four whitespace edits in §5 (S7).

That is a checklist, not a review. My recommendation to the project lead: apply those, then verify with a **mechanical diff pass** rather than a sixth adversarial round — every string changed in the fix grepped across both files, and every sentence of the form "this document says X elsewhere" checked against where it says it. Items 1 and 4 in particular sit squarely inside the technical-correction exception `cic-build-cycle` grants a coach thread (a propagation fix and a cross-reference fix, changing no substantive claim, disclosed with a dated correction note), which is a defensible route to closing this without another full cycle. **S10 is the lead's own to answer and no number of review rounds can close it.**

The pattern worth Mark's attention is unchanged from Round 4's and is now sharper: five rounds, five failures of the same class, and this round it moved out of the finding document and into the tracking log. Both times the correction reached four locations and missed the fifth. The defect is not carelessness about numbers — the argument has been independently re-derived five times and has never moved — it is that this document's corrections are applied by hand, location by location, with no mechanical sweep behind them. That is a process gap, not a document gap, and it will keep producing a finding a round until something greps.

---

## Overall verdict

**SUBSTANTIAL REVISION REQUIRED.**

Not on the answer, for the third consecutive round — and this time not on §6 either, which is clean. The revision is required because the fix for Round 4's two HIGH findings reached the finding document and stopped one paragraph short inside `Open_Gaps_Tracking.md`, leaving both an uncorrected factual claim and an undisclosed project-lead attribution in the log entry the project lead reads; and because §7's own record of Round 4 reports a MEDIUM as disposed that was not acted on, undercounts that round's LOWs, and attributes a fix to the wrong finding.

Recorded plainly, because it has now been established five independent times: on the substantive historical question this document is right, its §6 is finally accurate, its handling of the Q3 disagreement is exactly what the skill asks for, and the corrections it now needs are a checklist rather than a round.
