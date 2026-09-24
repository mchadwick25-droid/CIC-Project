# Doc_08 — Forces Document, and `lpc_Force_Index.md`: Latin Pastoral-Congregational Christianity
## Round 5 Independent Adversarial Review — verification of the Round 4 fix pass, and a cold read of everything it wrote

*Simulated review — informational only, not an Article 31 substitute.*

**Reviewed:** `Doc_08_Forces_Document.md` and `lpc_Force_Index.md`, both as they stand at commit `02696d24` (working tree clean; the delivered files are identical to HEAD).
**Prior rounds:** Round 1 (4H 5M 3L 1C), Round 2 (3H 4M 3L 1C), Round 3 (4H 5M 4L 2C), Round 4 (3H 3M 5L 1C) — all SUBSTANTIAL REVISION REQUIRED.
**Reviewer:** independent adversarial thread. No claim in the commissioning brief was inherited; two of its framings are corrected below.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH, 3 MEDIUM, 3 LOW, 2 COSMETIC.**

**Say the good part first, because it is the largest fact about this round.** For the first time in five rounds, **no HIGH finding touches the forces analysis.** The substantive defect that dominated Rounds 1–4 — the gravity relation of `2B-1` — is **closed, and closed correctly.** I re-derived it against `Doc_04_Gravity_Discovery.md` §3, §5 and §6 directly rather than through Doc_08's account of them, and the restoration of `2B-1` to §5's G6 list is right: the asymmetry Doc_08 asserts is genuinely in Doc_04, and is in fact attested at **two further unhedged loci in Doc_04 that Doc_08 does not cite**. §3, §5, §9 and the Index now agree about `2B-1` for the first time. The generator's notice-stripping fix works, its two hard guards fire, and **all four of the controls the Index advertises (A, B, C, D) reproduce exactly as described** when I ran them myself. The register-scan figures in §8 (six / zero) reproduce exactly. Six quotations spot-checked against the marked corpus are clean on both documented failure modes.

**The verdict rests entirely on the certification apparatus, and on one thing nobody has checked in five rounds.**

- **HIGH-1.** The review-history lines are stale again — at **seven sites**, four of them in the Index. Doc_08's masthead now says four rounds have been run and directs the reader to *"the Document Log and Disposition"*, both of which say three. §9's completion certification says *"independent review, which has not been run"* — a sentence that has been false since Round 1, has survived four review rounds and four fix passes, and **has never been raised by any of them, including me until I widened my sweep.** This is the third consecutive recurrence of Round 3's NEW-H3 / Round 4's H3, and the Round 4 fix pass wrote, in the notice that closed it, *"The discipline was adopted and then applied to two of the four sites that needed it"* — and then applied its own fix to two of seven.
- **HIGH-2, and this is the one I did not expect to find.** `gen_force_index.py` **does not exist anywhere in the repository.** It is not tracked, not on disk in the build directory, not named by path in either deliverable, and not recorded in `lpc_Decision_Log.md`. It exists only in a session-scoped scratchpad. Doc_08's Document Log calls it *"a saved, re-runnable generator"*; the Index's header says *"Generated from `Doc_08_Forces_Document.md` by `gen_force_index.py`"*; the Index's §6 says its four controls are *"all reproducible from the saved generator."* None of that is true of the build record. The entire derived-index integrity story — the thing that makes the Index a co-deliverable rather than a hand-written table — rests on an artifact that will not survive this session. **Five rounds of review, including this brief, have used the scratchpad copy and treated its existence as settled. That is precisely this build's signature mechanism: a check trusted because it returned something.**

**What would change the verdict.** Both HIGHs are hours of work, not analysis. Save the generator into the world directory (or `Ministry/Technology/`), name its path in both files, and make the seven review-history sites true — and this pair is at **MINOR REVISION**, with only the notice-syntax gap (M1) and the Doc_04 hedge (M2) left as anything more than tidying. The forces analysis underneath has converged and I would not ask for another round of it.

---

## Method — what I actually opened and ran

**Read in full:** both deliverables; `Doc08_Round4_Review.md`; `gen_force_index.py` (481 lines, line by line); `Doc_04_Gravity_Discovery.md` §§3–7; `L4-Templates/[world-code]_Forces_Document.md` §3 guidance and checklist; the Forces Framework plain text (`FF.txt`) at its Governing Principle, its three-layer rule and its gravity-connection rule; `CiC_Record_Native_World_Build_Process_V1_3.md`'s index-artifacts paragraph; the Constitution text; `Lexicon_Deployment_Index.md` §7 area; `CLAUDE.md`.

**Ran, all in an isolated sandbox with the generator's output path redirected so neither deliverable was touched:**

1. **Byte-identity.** The current generator against the live Doc_08 → output **byte-identical** to the delivered `lpc_Force_Index.md`. The Index is genuinely generated and has not been hand-edited.
2. **Independent re-derivation** of §5's eight gravity lists, raw and notice-stripped, by my own parser rather than theirs.
3. **Notice inventory.** All 36 bracketed provenance tags in Doc_08 and 12 in the Index, classified by whether the stripper's span actually covers them.
4. **Control A** — the current generator against the pre-fix draft at `9eccc532`.
5. **Controls B, C, D** — three mutants of the live Doc_08, one per claim.
6. **Guard tests** — six further mutants: a deleted force heading, a broken §5 gravity heading, an undefined force ID in §5, a bare-`]` notice terminator, an early-`]**` notice body, a mis-terminated notice on a gravity line.
7. **Two constructed defects** the §6 battery does not catch, both verified to return "No contradictions."
8. **The §8 register scan**, rebuilt from §8's own seven-marker description, in four variants.
9. **§6 control coverage** on the live text.
10. **Quotation spot-check** — six quotations, rebuilt from `cyprian.xml` and `npnf104` with `<note>` spans marked *before* tag-stripping and every `<div1>`–`<div4>` `title=` converted to a surviving sentinel, so each hit returns both a note verdict and its containing work; plus the Latin witness in `augustine_retractationes-lat_knoll-csel36.txt`.
11. **Cross-file numeric sweep** — §7's seventeen confidence labels against Index §2; §4's fifteen rows against Index §4; §9's ticks against the tables they point at.
12. **Repository search** for `gen_force_index.py` by `find`, by `git ls-files`, and by `git check-ignore`.

---

## Job 1 — Round 4's twelve findings, closure status at the live text of **both** files

| # | Finding | Status |
|---|---|---|
| H1 | Notices were derivation input; the Index's G6 row contradicted §5; "cannot drift" in Doc_08 line 12 | **CLOSED IN SUBSTANCE, one limb outstanding.** The stripper is in and works; the G6 decision was made against Doc_04 §6 as instructed; §5, §3, §9 and the Index now agree. **Limb 3 — "delete or qualify 'so the two cannot drift'" at Doc_08 line 12 — was not done**, and is now falsified by a live drift. See **M3**. |
| H2 | Dropping `2B-1` falsified §5's Cross-Strand note | **CLOSED on the phase reading.** `2B-1` is back; G6 again reaches the first phase. The sentence still says *"both rows"*, and G6's three forces are all in the **Ongoing** row, so it remains false on the matrix reading Round 4 named. The G2-clause correction Round 4 asked for *"in the same edit"* was not made. See **L1**. |
| H3 | Masthead and closing sentence said the document was unreviewed | **NOT CLOSED — regressed, and wider than before.** The two quoted sites are fixed. The class is live at **seven** sites, four of them in the Index, one (§9, line 434) never raised in any round. See **H1**. |
| M1 | No disconnection test; "both directions are tested" was a literal | **CLOSED, and verifiably.** The third test exists (`DISCONNECT`, `NEGTAIL`, head/tail split) and I made it fire by mutation — Control B reproduces exactly. |
| M2 | §8's "zero across all seventeen" overstated; six hits at two entries | **CLOSED in substance.** The exemption is now stated, the six-hit figure printed, and both reproduce exactly on my independent scan. One clause of the accounting does not hold. See **L2**. |
| M3 | `DISCLAIM` suppressed a genuine 1B-1/G2 assertion via a bare `§5` match | **CLOSED.** The `§5` clause is withdrawn; the false `1B-1`/G2 observation row is gone; control coverage rose from 13/21 to **15/20** on my measurement. |
| L1 | §5 restated Doc_04's attestation wording for G5 as a forces finding | **CLOSED, and better than asked.** Now *"one first-phase (`1B-1`) and two second-phase (`2A-3`, `2B-4`), each of them indirect … carried here rather than independently reproduced."* I verified all three phase attributions against Doc_08's own Layer 1 text. |
| L2 | Index §4's summary line hard-coded two force IDs and a number-word | **CLOSED, mutation-verified.** Making `1B-3` the isolated force and adding a second produced *"**2 deliberate non-connections** (`1B-3`, `2A-2`)"* — right IDs, right plural. |
| L3 | "four have not" / "Five documents" in consecutive sentences | **CLOSED.** Now *"Four documents … Doc_04, Doc_05, Doc_06 and Doc_07 … This is the fifth."* |
| L4 | "7 of the 19" measured on a superseded draft, stated in the present tense | **CLOSED.** Now scoped to `561c2c35` and flagged as pre-dating the 2B-1 rewrite. |
| L5 | Index §5 gave the superseded account of the Round 1 H4 defect | **CLOSED.** Index §5 now reads *"**Two** … genuinely blank … and a third, **3B-1**, was written but self-declared 'left unfilled'"*, matching Doc_08 §§8–9. |
| C1 | "closes with 'Do not create new workbooks'" | **CLOSED in substance** (I confirmed both quoted strings verbatim at `CiC_Record_Native_World_Build_Process_V1_3.md` lines 156 and 160, and that the paragraph is headed **Index artifacts** and does close with that sentence). The repaired sentence is now ungrammatical. See **C1** below. |

**Ten closed, one closed with a limb outstanding, one not closed.** The one not closed is Round 4's H3, and it is not closed in the direction the brief warned about: **the fix landed at the two sites the review quoted and nowhere else, including four sites in the other file of the pair.**

---

## HIGH

### H1 — The review-history lines are stale at seven sites, Doc_08's masthead now points the reader at two of them, and one has been false since Round 1 without any round noticing

**Site.** `Doc_08_Forces_Document.md` line 14 (Status), line 434 (§9 completion status), lines 446–454 (Document Log), line 460 (Disposition, opening), line 462 (Disposition, review-history paragraph). `lpc_Force_Index.md` lines 3, 4, 5 and 156 — all four generator literals, at `gen_force_index.py` lines 302, 303, 304 and 474.

**What I found.**

Doc_08 line 14, corrected by the Round 4 fix pass, now reads:

> **Status:** **REVISED after Round 4 — the revision is unreviewed, and not self-disposed.** Four independent adversarial review rounds have been run; **see the Document Log and Disposition.**

The Document Log's last two rows are *"Round 3 independent adversarial review"* and *"Round 3 fix pass — this revision."* There is **no Round 4 review row and no Round 4 fix-pass row**, in a document that carries five `[CORRECTED … Round 4's …]` notices.

The Disposition's opening, line 460:

> **Not disposed. REVISED after Round 3; the revision is unreviewed.**

And line 462:

> **Three independent adversarial review rounds have been run against this document and `lpc_Force_Index.md`**, all three returning **SUBSTANTIAL REVISION REQUIRED**: Round 1 (4H 5M 3L 1C), Round 2 (3H 4M 3L 1C), Round 3 (4H 5M 4L 2C). **Every HIGH finding in Rounds 2 and 3 was a defect introduced by the preceding fix pass** …

**So the masthead sends the reader to two places to confirm "four rounds", and both say three.** That self-contradiction did not exist before the Round 4 fix pass; it was created by it.

**The Index is worse, because all four of its sites are untouched.** Round 4's H3 recorded, as a point in the Index's favour, that *"The Index, by contrast, now states the position correctly at every one of its four sites."* All four now say Round 3:

- line 3: *"**REVISED after Round 3** — the revision is unreviewed"*
- line 4: *"Round 1 …, Round 2 …, Round 3 … — **all three SUBSTANTIAL REVISION REQUIRED**"* — in a file that carries three `Round 4's …` correction notices
- line 5: *"**Revised:** 2026-09-15 (**Round 3 fix pass**)"*
- line 156: *"**Three independent rounds have been run**, the most recent `Review-Artifacts/Doc08_Round3_Review.md` … this file is the **Round 3 fix pass** and is **unreviewed**."*

`git show 02696d24 -- lpc_Force_Index.md` confirms: the Round 4 fix pass changed six lines of the Index and **none of them was a review-history literal.**

**And the site nobody has ever raised.** Doc_08 line 434, the closing sentence of §9's Completion Certification:

> **Doc_08 completion status: COMPLETE as to the checklist; NOT DISPOSED.** The checklist is a structural certification and this document meets it. **It is not a substitute for independent review, which has not been run.**

Independent review has been run four times. This sentence is a flat falsehood at the document's own completion certification; it was false the moment Round 1 was filed; **four review rounds and four fix passes have read past it.** I found it only because I widened my sweep from the phrases prior rounds had used (`not reviewed`, `unreviewed`, `no reviewer`) to include `has not been run`. Round 4's own fix instruction for H3 proposed exactly such a sweep — *"grep -in 'not reviewed\|no reviewer\|unreviewed\|first-draft' both files and read every hit"* — and that pattern does not match line 434. **A sweep built from the phrasings already known is a sweep that finds what is already known.**

**Why this matters.** Constitution Article 30 and CO-022 make disposition turn on review status, and the Disposition paragraph is the single place a project lead reads to decide it. It currently states a false round count, a false review-history table, and a false completion note — while the masthead states the true one and points at the false ones. The two co-deliverables, which are *"reviewed and disposed of together"* by their own terms, now disagree about whether four rounds or three have been run. This is the third consecutive round in which this exact class of statement has been found stale, and the fix pass that closed the second occurrence wrote the diagnosis of its own recurrence into the document: *"The discipline was adopted and then applied to two of the four sites that needed it."*

**How I confirmed it, two ways.** (1) Direct read of each of the seven sites. (2) An independent sweep of both files for round-count and review-status claims, cross-read against the `Review-Artifacts/` directory listing and against `git log` (five Doc_08 commits: draft, Round 1 fix, Round 2 fix, Round 3 fix, Round 4 fix — and `Doc08_Round4_Review.md` committed inside the Round 4 fix commit, so the Log had the artifact in hand when it was written). (3) A `git show` of the Round 4 fix commit, confirming which lines were and were not touched.

**Fix.**
1. Doc_08: add the two missing Document Log rows (Round 4 review — SUBSTANTIAL REVISION REQUIRED, 3H 3M 5L 1C, all three HIGH defects of the preceding fix pass; Round 4 fix pass — this revision). Rewrite line 460 and line 462 to four rounds with Round 4's counts. Rewrite line 434's final clause to *"which has been run four times and is not complete until the current revision has been reviewed."*
2. Index: change the four literals in `gen_force_index.py` (lines 302, 303, 304, 474) and regenerate. They are the file's own declared "hard-coded prose, re-verified by nothing" — which is a reason to touch them first, not a licence to leave them.
3. **Replace the phrase-list sweep with a structural one.** The recurring failure is that each pass greps for the wording the last review quoted. Instead: enumerate every sentence in either file containing a round ordinal, a review-round count, or a disposition status word, and read all of them. On the current text that is a list of eleven sentences and takes two minutes.

---

### H2 — `gen_force_index.py` is not in the build record. Both deliverables claim it is, and the Index's four controls are advertised as "reproducible from the saved generator" that nobody outside this session can run

**Site.** `lpc_Force_Index.md` line 6 (*"Generated from `Doc_08_Forces_Document.md` by `gen_force_index.py`. Never hand-edited."*), line 8 (the derived/hard-coded disclosure, whose whole force depends on "re-running the generator"), line 138 (*"Four checks, **all reproducible from the saved generator**"*). `Doc_08_Forces_Document.md` line 12 (*"generated from this document's own prose by script"*) and line 450 (Document Log: *"Index regenerated by a **saved, re-runnable generator**"*).

**What I found.**

```
$ find /home/user/cic-project -name "gen_force_index.py"      → (nothing)
$ git ls-files | grep -i "gen_force\|force_index"
World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Force_Index.xlsx
World-Builds/Latin-Pastoral-Congregational-Christianity/lpc_Force_Index.md
$ git check-ignore -v World-Builds/…/gen_force_index.py       → (not ignored)
$ grep -n "gen_force_index" …/lpc_Decision_Log.md             → (nothing)
```

The generator exists at one path only: `/tmp/claude-0/…/scratchpad/gen_force_index.py`, a session-scoped directory. It is not ignored by `.gitignore` — it was simply never saved into the build. Neither deliverable names a path for it. The Decision Log, which records this world's build decisions in 442 KB of detail, does not mention it.

Meanwhile the Index stakes its entire standing on it: the header's disclosure is a contract about *"what re-running the generator actually re-verifies"*; §6's control battery is offered as *"all reproducible from the saved generator"*; the master table's derivation column says *"§5 list"* on the strength of a parse nobody outside this session can execute. Doc_08's Document Log calls it **saved**. It is not saved.

**Why this matters, and why it is HIGH rather than a housekeeping note.**

- **It voids a claim both files make about themselves.** "Never hand-edited" is a promise that is only meaningful if the generator can be re-run to check. Today it can be — by this session. Tomorrow the Index is an un-regenerable frozen table with a header asserting it is derived.
- **It makes the §6 controls unfalsifiable.** Round 3's lesson, written into the Index itself, was *"A control that has never been made to fail is not evidence that it can."* A control that no one can run is worse: it cannot be made to fail *or* to pass. Every one of the four checks I reproduced this round becomes unreproducible the moment this scratchpad is gone.
- **It blocks the downstream steps that need it.** Doc_09 and the Validation Layer will amend Doc_08; the Index must be regenerated when they do. There is nothing to regenerate it with.
- **It is exactly this build's signature failure mode.** Five review rounds — and the brief that commissioned this one — have pointed at the scratchpad path and treated the artifact's existence as settled because reading it returned something. The check proved something adjacent to the claim: *"the generator I was handed reproduces the Index"* is not *"the build record contains a generator."* Round 3's own Method section records running *"the saved generator `gen_force_index.py`"* — the word *saved* was carried, not verified, through three rounds.
- **The repository already has the convention.** `.gitignore` lines 32 and 36 document regeneration commands in-place (*"Regenerate with: python cic/engine/corpus_index.py --build"*). Nothing about this build required the generator to live outside the record.

**How I confirmed it, three ways.** `find` over the whole repository (filesystem), `git ls-files` (index), and `git check-ignore` (to rule out the file being present but hidden). All three agree. I also checked all four prior Doc_08 review artifacts for any mention: none raises it; Round 3's Method line is the closest and it assumes the opposite.

**Fix.**
1. Copy `gen_force_index.py` into the world directory (or `Ministry/Technology/`), commit it, and make its `BASE` path either relative or documented.
2. Name it by path in the Index header line 6 and in Doc_08 line 12 — *"generated by `World-Builds/…/gen_force_index.py`, committed alongside this document"*.
3. Record it in `lpc_Decision_Log.md` with the one-line command that regenerates the Index.
4. Only then is the Document Log's word **"saved"** true, and only then is §6's *"all reproducible"* a claim a reviewer can act on.

---

## MEDIUM

### M1 — The notice stripper covers one of the two notice syntaxes this document uses. A force ID inside the other still reaches the tables, and the Index's control (C) is stated more broadly than the control tested

**Site.** `gen_force_index.py` lines 26–34 (`NOTICE`, `strip_notices`) and its comment at lines 74–80 (*"Notices are stripped before ANY derivation, everywhere, once"*); `lpc_Force_Index.md` line 138, control (C).

**What I found.**

`NOTICE = re.compile(r"\*\*\[(?:CORRECTED|ADDED|MOVED HERE|MOVED|REVISED)\b.*?\]\*\*")` requires the bracket to open **immediately after** `**`, and to close on `]**`. This document writes its provenance notices two ways:

- **Form A**, which the regex matches: `**[CORRECTED, 2026-09-15 — Round 4's H1:** … .**]**`
- **Form B**, which it does not: `**Checked rather than asserted, and the check's own scope stated. [REVISED, 2026-09-15 — Round 4's M2.]**` — the bold opens on the heading, not on the bracket.

I classified every bracketed provenance tag in both files against the spans the stripper actually removes:

```
Doc_08: 36 tags — 32 inside a stripped span, 4 NOT stripped (lines 395, 399, 405)
Index:  12 tags —  7 inside a stripped span, 5 NOT stripped (lines 10, 112, 134, 136)
```

**Today none of the four uncovered Doc_08 tags sits on a derivation-bearing line** — all are in §8, which feeds nothing. So there is **no wrong value in the delivered files.** The defect is that the injection vector Round 4's H1 was raised to close is still open on a syntax the document uses eleven times across the pair, and that both the generator's comment and the Index's control (C) assert coverage the code does not have.

**Demonstrated, not inferred.** Two mutants placed on §5's G7 line:

| Mutant | Notice form | Result |
|---|---|---|
| **H1** | terminated with a bare `]` instead of `]**` | G7's row becomes `` `2A-4`, `3A-1`, `3B-1` `` — **3** forces; `3A-1`'s master row becomes `G1, G7`; §6 prints "No contradictions"; **both hard guards clean** (17 forces, 8 gravities) |
| **H2** | body contains an early `]**` — e.g. a quoted `*[Supporting]***` — so the non-greedy match terminates inside the notice | **identical result** |

Mutant H2 is not hypothetical. Doc_08 §1 already quotes Doc_04's bracketed classification tag verbatim — *"Candidate 5 **[Supporting]** — Conciliar Authority Theory"* — **because Round 2's L2 directed that the bracket be quoted rather than dropped.** A future notice quoting that tag with bold immediately after the `]` breaks the strip. Doc_06's `[CT]` tags, quoted in §7, are the same shape.

The Index's control (C) reads: *"a bold force ID planted inside a `[CORRECTED …]` notice in §5 no longer reaches either table."* I reproduced it and it passes — **for Form A.** It is stated about notices in general.

**Why this matters.** This is the same mechanism as Round 4's H1, one syntax over, and the same as Round 1's confidence regex terminated by `**`. The build has now three times shipped a pattern that handles the instance in front of it and not the class. The guards do not help: force count and gravity count are both unchanged by an injected ID.

**Fix.** Drop the leading `\*\*` requirement and accept both terminators:
`NOTICE = re.compile(r"\*{0,2}\[(?:CORRECTED|ADDED|MOVED(?: HERE)?|REVISED)\b.*?\]\*{0,2}")`, still line-bounded. Then **add a fifth control**: assert that the notice-stripped text of §3, §4, §5 and §7 contains no bracketed provenance tag at all — a coverage assertion rather than a single positive instance. Re-run mutants H1 and H2 against it. And narrow control (C)'s wording in the Index to name the forms tested.

### M2 — Both places where Doc_08 quotes Doc_04 §6's Interaction Matrix silently drop the hedge Doc_04 attaches to exactly that cell — in the passage that reverses Round 3 and claims the judgement is Doc_04's rather than this document's

**Site.** `Doc_08_Forces_Document.md` line 334 (§5, the G6 reversal notice) and line 161 (§3, `2B-1` Layer 3), against `Doc_04_Gravity_Discovery.md` line 195 (§6 Interaction Matrix, row *2. Penitential Discipline*).

**What I found.**

Doc_04's cell, in full:

> Reinforcing (both are boundary/reintegration questions Cyprian reasons about consistently **— this document's own reading**)

Doc_08 quotes it twice, and both times the quotation closes where the hedge begins:

- §5: *"Reinforcing (both are boundary/reintegration questions **Cyprian** reasons about consistently)"* — parenthesis closed, no ellipsis.
- §3: *"both are boundary/reintegration questions **Cyprian** reasons about consistently,"*

**The dropped clause is not decoration.** *"— this document's own reading"* is Doc_04's own marker for cells it **infers** rather than evidences from the record, and it appears on exactly two cells in the entire eight-by-eight matrix (2×3 and 2×6). The companion cell Doc_08 sets against it — 2×7, *"Reshaped by … not 2's own continuation — see §3, §5"* — carries **no** such marker. So the asymmetry Doc_08 builds on is not simply "two different relations": it is an **unhedged** relation on the G7 side and a **self-declared inference** on the G6 side — and it is the G6 side Doc_08 uses to *add* a force connection.

Doc_08 §3 then writes: **"The asymmetry is Doc_04 §6's, not this document's."** With the hedge restored, the accurate statement is that the asymmetry is Doc_04's *reading*, which is a materially weaker warrant than the sentence conveys.

**Two things that cut the other way, and I record them because they matter to the grading.**

1. **The substance is corroborated, twice, at loci Doc_08 does not cite.** Doc_04 §3, Candidate 2's **Interaction** test (line 48): *"Reinforces Candidates 1, 3, 4, and 6; reshaped by Candidate 7 (Augustine's own phase-specific reworking of a structurally similar question, not this gravity continuing); competes with Candidate 8."* And Candidate 6's own Interaction test (line 116): *"Reinforces Candidates 1, 2, 3, and 5."* Neither carries the hedge. **The reversal is better supported than its own notice claims** — it just does not cite the support.
2. **Doc_04 §3's Persistence test itself points at §6** — *"What survives across the phase boundary is a family resemblance (**see §6**), not the same gravity restated"* (line 47). So the notice's narrative that the Round 3 argument *"rested on Doc_04 §5's Persistence test and never opened Doc_04 §6's Interaction Matrix"* is fair about what the Round 3 pass did, but loose about the loci: the Persistence test lives at **§3**, is restated at §5, and refers the reader to §6 in its own closing words.

**The unanswered question Round 4 asked and this pass did not answer.** Round 4's H1 fix said: *"either add `2B-1` back on that ground … or state why a gravity-to-gravity interaction is not a force route."* Doc_04 §6 relates **Candidate 2 to Candidate 6** — gravity to gravity. §5's lists relate **forces to gravities**. The step from *"G2 reinforces G6 in Cyprian's phase"* to *"the force `2B-1` connects to G6"* is Doc_08's own inference, and it is a reasonable one — `2B-1` is the force §5 names as producing G2 — but it is **not** Doc_04 §6's, and §3's sentence says it is.

**Why this matters.** The build's two documented failure modes are both about quotation discipline. This is a third instance of the same instinct in a new place: a source trimmed so that the claim resting on it looks better founded than the source makes it — in the single paragraph in this document that reverses a prior decision.

**Fix.** Restore *"— this document's own reading"* inside both quotations, or mark the elision. Add the two corroborating Doc_04 §3 Interaction lines, which carry no hedge and make the point more strongly. Replace *"The asymmetry is Doc_04 §6's, not this document's"* with something true of both legs — e.g. *"Doc_04 records the two relations differently (§3's Interaction tests for Candidates 2 and 6; §6's matrix, where the 2×6 cell is marked as Doc_04's own reading), and this document takes the force route from G2's producing force to G6 as its own step."*

### M3 — Doc_08 line 12 still says the two files "cannot drift", the one limb of Round 4's H1 fix not applied, and there is now a live drift between them to prove otherwise

**Site.** `Doc_08_Forces_Document.md` line 12, against `lpc_Force_Index.md` lines 8 and 10, and against Doc_08 line 14 versus Index line 3.

**What I found.** Line 12 is unchanged at all five commits:

> **Co-produced output:** `lpc_Force_Index.md` … **generated from this document's own prose by script** so the two cannot drift.

Round 4's H1 fix instruction, limb 3, was explicit: *"In Doc_08 line 12, delete or qualify 'so the two cannot drift.' The Index's own header already says what is true; the source document should not say something stronger."* The Round 4 diff shows line 12 untouched.

It is not merely stronger than the Index's statement; it is **false today, demonstrably, between these two files.** Doc_08 line 14: *"REVISED after Round 4."* Index line 3: *"REVISED after Round 3."* The Index's own header (line 8) explains why this is possible: *"**Hard-coded prose, re-verified by nothing:** this whole header block — **including the Status line, the Review-history line, the Revised date and the Disposition**."* And the Index's line 10 opens by recording that the earlier generator's *"'cannot drift' claim was false."*

So Doc_08's masthead asserts an integrity property that the Index formally retracted at Round 1, narrowed again at Round 2, and that H1 above proves is currently violated.

**Why this matters.** Line 12 is the sentence that tells a reader of Doc_08 how much to trust the Index. It is over-promising in the one direction the pair has actually failed four times.

**Fix.** *"…generated from this document's own prose by script, so that **every derived table** in it is re-checked against this document on each run. The Index's own header states exactly what is and is not derived; its header prose, including its status and review-history lines, is not."*

---

## LOW

### L1 — §5's Cross-Strand note still says "both rows", and G6's three forces are all in the same row

**Site.** `Doc_08_Forces_Document.md` line 344 (§5, Cross-Strand Gravity Note).

The sentence reads: *"the forces connected to G2 and G8 are phase-one forces; the force producing G7 is a phase-two force; **G1, G3, G4 and G6 connect to forces in both rows.**"*

With `2B-1` restored, G6's forces are `2A-3`, `2B-1`, `2B-4`. On the **phase** reading the clause now holds — `2B-1` carries the first-phase relation, which is exactly what the G6 notice four lines above argues for. On the **matrix-row** reading it does not: all three sit in the **Ongoing** row. Checked against the other three: G1 spans three rows, G3 two, G4 two. **G6 is the only member of the list that fails the row test, and "rows" is the document's own matrix vocabulary** while the two clauses either side of it say "phase-one" and "phase-two". Round 4's H2 named the both-readings problem; the fix repaired the reading and left the word.

Round 4's H2 also asked, *"in the same edit"*, for the first clause to be corrected: G2's connected forces include `2B-1`, whose Layer 1 spans both phases (*"The lapsed under Cyprian; ordinary post-baptismal sin and schism-tempted believers under Augustine"*). That correction was not made. It is defensible as written — the document consistently treats `2B-1`'s **gravity relations** to G2 and G6 as first-phase, which §3 line 161 now says in terms — but it is defensible only by a reading the sentence does not supply.

**Fix.** Change "rows" to "phases", and add six words to the G2 clause: *"the forces connected to G2 and G8 are phase-one forces (`2B-1` spans both phases as a force; its G2 relation is first-phase, per §3)"*.

### L2 — §8's accounting of the six-hit register-scan residue does not hold at `3B-1`

**Site.** `Doc_08_Forces_Document.md` line 399 (§8), against lines 252 and 270 (the two Reported-Experience paragraphs).

§8 says: *"Scanned without that exemption the figure is six hits at two entries, `3B-1` and `3B-2` … Of those six, the template-mandated marker text accounts for all but **one `[ADDED …]` provenance clause per entry**."*

I rebuilt the seven-marker scan from §8's own description and ran it in four variants. **The two headline figures reproduce exactly**: six hits at two blocks as described, zero across all seventeen with the Reported-Experience paragraph exempted. The residue attribution does not:

| Variant | Result |
|---|---|
| As §8 describes it | **6 hits at 2 blocks** — `3B-1` and `3B-2`, three markers each (`§` reference, layer-scheme self-ref, evidentiary meta) |
| Reported-Experience paragraph exempted entirely | **0 across all seventeen** |
| `[ADDED …]` clauses removed, marker text kept | **5 hits at 2 blocks** — `3B-2` loses its layer-scheme hit |

Confirmed a second way by direct reading rather than by regex: `3B-1`'s template-only marker text contains the string *"Layer 2"* (*"applies to the whole **Layer 2** above"*); `3B-2`'s does not (*"applies to the sentence beginning…"*). So the `[ADDED …]` clause at `3B-1` produces **no** marker hit that the template text does not already produce, and the clause at `3B-2` produces exactly **one**. "One per entry" overstates by one entry.

**Note against my own finding, and against Round 4's.** Round 4's equivalent variant reported 6 with notices stripped, where I get 5. The likely cause is that Round 4's stripping regex required `**]**` and `3B-2`'s notice ends `.]**` — so it was not stripped and its *"Layer 2"* survived. That is the same terminator defect the Round 4 fix pass then corrected in the generator. Either way, the markers are defined in §8 in **words**, not regexes, so any attribution at this resolution is method-dependent; that is why this is LOW and why I report both numbers.

**Fix.** *"Of those six, all but one are produced by template-mandated marker text; the exception is `3B-2`'s `[ADDED …]` provenance clause, retained deliberately so the marker's own history is auditable at its site."*

### L3 — Nothing in the control battery compares §3's Layer-3 prose against §4's cross-cell table, and the one force with a known §4 gap is the one whose prose is never cross-read

**Site.** `gen_force_index.py` lines 258–275 (§4 parse) and 212–252 (the §6 battery); `lpc_Force_Index.md` line 13 and the `1B-3` master row.

§6 exists because §5's lists and §3's prose are two statements of the same relation and could disagree. **The same is true of §4's table and §3's prose, and nothing checks it.** §4 is parsed once and inverted; no control reads a Layer 3 for cross-cell assertions.

Demonstrated: I added one sentence to §3's `1B-3` Layer 3 — *"It is also the direct precondition for **2B-5**'s translation apparatus, which could not have rendered a vocabulary that did not exist"* — and regenerated. The Index still prints `*(no §4 row)*` for `1B-3`, §4's map is unchanged, and §6 prints **"No contradictions."** No control noticed a cross-cell claim in §3 that §4 does not carry.

This is not idle: the Index's own line 13 records that *"`1B-3` is the only force in the matrix that §4 neither connects nor deliberately isolates — carried as an open observation for review, not resolved here."* The one force whose §4 status is flagged as unresolved is the one whose prose no control reads.

**Why this matters.** This is the same shape as the §3/§5 gravity gap — two derivations of one relation, only one of them checked — which took four rounds to close. I found no live instance; I am reporting the hole, not a breach.

**Fix.** A fourth test: extract force-ID tokens from each Layer 3, subtract the force's own §4 row set, and print the remainder as observations (the same asymmetric treatment §6 already gives gravities). It is about fifteen lines and it would have caught this class before it arrived.

---

## COSMETIC

### C1 — The repaired workbook sentence is ungrammatical

`Doc_08_Forces_Document.md` line 466: *"`CiC_Record_Native_World_Build_Process_V1_3.md` **states that** the per-world `.xlsx` workbooks are **RETIRED for new builds** and **whose** index-artifacts paragraph closes with *'Do not create new workbooks.'*"* — "states that … and whose" does not parse. It is the literal application of Round 4's C1 fix wording into a clause that could not take it. The substance is exact; I verified both quoted strings at lines 156 and 160 of the source and that the paragraph is headed **Index artifacts**.

**Fix.** *"… are **RETIRED for new builds**, in an index-artifacts paragraph that closes with…"*

### C2 — Index §6 says "Both directions are tested" three lines above a paragraph headed "Three tests now, not one"

`lpc_Force_Index.md` line 122 (the derived no-contradiction literal, `gen_force_index.py` line 424) against line 134. The clause was accurate when there were two tests and the finding it reports is now genuinely derived; only the count is stale.

**Fix.** "All three directions are tested; see below."

---

## Additional checks that returned clean, and which of them I tested hardest

**The `2B-1` / G6 relation — tested hardest, because it is the finding this round was commissioned to re-open.** Verdict: **the reversal is right, and the pair is now internally consistent about it for the first time in five rounds.**

- §5 line 332 lists `2A-3`, `2B-4`, `2B-1` in the list proper. §3 line 161 asserts *"connects to G2 and to G6 — both first-phase relations — and **not** to G7."* §5's G7 list does not carry it. The Index's `2B-1` master row reads `G2, G6`; its G6 by-gravity row reads `2A-3`, `2B-1`, `2B-4`, count **3**. Four statements, one relation, no disagreement.
- Against Doc_04 directly, not through Doc_08's account of it: §6's matrix row (line 195) does make the 2×6 and 2×7 relations asymmetric; §3's Candidate 2 Interaction test (line 48) says the same without a hedge; §3's Candidate 6 Interaction test (line 116) says it from the other side; §3's Candidate 6 Persistence test says *"Passes. Visible in both phases"*, which is what a first-phase force connection restores. **The brief's premise on this point is correct**, and Doc_08's first-phase / second-phase characterisation of the two cells is a fair gloss of *"Cyprian reasons about consistently"* and *"Augustine's own phase-specific reworking."* My one reservation is M2.
- **G7's single-force-origin finding stands.** Its list is untouched (`2A-4`, `3B-1`), `2A-4` remains the sole origin, and the notice's new footing — *"stands on the 'Reshaped by' relation rather than on a symmetry that does not exist"* — is the correct footing.
- **§6's Author-Gravity convergence claim stands.** It depends on G7 alone, which did not change. I verified its factual leg independently: `Lexicon_Deployment_Index.md` line 129 states *"8 of 19 entries carry an Author Gravity note"*, which is what Doc_08 §6 reports.

**The generator's four controls — reproduced in full, not sampled.** All four came out exactly as the Index describes:

| Control | Claim | My result |
|---|---|---|
| **A** Regression at `9eccc532` | reports `1B-1`/G2, `2A-1`/G8, `2B-1`/G7 | **exactly those three**, plus 3 STUB flags on the master table |
| **B** False denial | rewriting §3 to deny G6 produces a contradiction row | *"**Contradiction** — §3 Layer 3 asserts §5 does NOT carry this; §5's list does carry it"* |
| **C** Notice injection | a bold ID in a `[CORRECTED …]` notice reaches neither table | planted `**3A-1**` in §5's G2 notice; `3A-1`'s gravities stayed `G1` — **passes, for Form A notices** (see M1) |
| **D** Omitted connection | removing `2B-1` from §5's G6 list produces a contradiction row | *"§3 Layer 3 asserts this connection; §5's list omits it"*, and G6 drops to 2 |

**The two hard guards fire.** Deleting a `#### Force` heading → `FATAL: parsed 16 forces, expected 17. Refusing to emit a short index.` Breaking a §5 gravity heading → `FATAL: parsed 7 gravities (['G1'…'G8' minus G7]), expected 8.` A third guard I did not expect also fires: a §5 force ID that §3 does not define → `FATAL: §5 names force 4A-9, which §3 does not define.`

**§6 control coverage improved measurably.** On my own sentence-splitter: **20** Layer-3 sentences name a gravity, **15** are examined, **2** are suppressed by `DISCLAIM` and both suppressions are correct (`2A-1`'s *"attested only within it"* is an attestation claim; `2B-1`'s *"The asymmetry is Doc_04 §6's…"* is a sentence about Doc_04's matrix, not a §3 connection assertion), and **3** carry no `CONNECT` verb, of which two are correctly excluded. Round 4 measured 13 of 21 with three wrong suppressions. M3 is genuinely closed.

**Quotation fidelity — spot-checked rather than re-run, per the brief, with the time spent on Job 2.** Six quotations, rebuilt from source with `<note>` spans marked before tag-stripping and `<div1>`–`<div4>` `title=` attributes converted to surviving sentinels:

| Quotation (opening words) | Site | Apparatus? | Containing work |
|---|---|---|---|
| "it is the shepherd that is chiefly wounded…" | 1A-1 | outside | Treatise III (*On the Lapsed*) — Cyprian |
| "thousands of certificates were daily given…" | 2B-2 | outside | Epistle XIV — Cyprian |
| "your suffrage and God's judgment" | 1B-2 | outside | Epistle XXXIX — Cyprian |
| "by the judgment of God and the favour of the people…" | 1B-2 | outside | *The Life and Passion of Cyprian* — **Pontius the Deacon** (and Doc_08 attributes it correctly, *"A deacon who knew him put it from outside"*) |
| "even of the plenary Councils, the earlier are often corrected…" | 2B-4 | outside | *On Baptism, Against the Donatists*, Bk. II ch. 3 — Augustine |
| "cum quadam iudiciaria seueritate" | 2B-5 / 3B-1 | n/a (Latin witness) | *Retractationes* — one occurrence in CSEL 36 |

All clean on both documented failure modes. No new misattribution surfaced.

**Governing-document quotations, verified verbatim.** FF's *"This is not optional. All three layers are required for every force"* (FF.txt line 141); FF's name-the-absence limb, quoted in full at §8 (line 34); FF's *"A gravity that cannot be connected to the forces acting on the world is a gravity whose ecology is incomplete"* (lines 176, 200); the L4 template's Proportionality carve-out (lines 105–106); and the template's placement of the Reported-Experience marker **inside** Layer 2 (lines 99–102, 180–183, 666–667) — so §8's exemption is legitimate, not a convenience.

**Cross-file numerics.** §7's seventeen confidence labels are the same seventeen force IDs as Index §2's Documented + Widely Accepted lists, force by force. §4's fifteen rows equal Index §4's fifteen rows. §8's "fifteen connections" and §9's "1A (2), 1B (3), 2A (4), 2B (5), 3A (1), 3B (2) = 17" match the Index's derived line. §9's every tick points at something that exists.

**Two residues I record rather than grade.** (1) Index §6 still prints `` `2A-2` | G4 `` as an observation whose text says §3's Layer 3 *"does not assert it in a connection sentence"*, while §3's `2A-2` closes *"crisis metabolized into formation content **through G4**"* — a mechanism statement with no connection verb. Round 4 graded this "arguable" and I agree; the row is true about sentence form and misleading about content, and Round 4's alternative wording (*"the control did not recognise an assertion of it"*) would still be the better fix. (2) The `CONNECT` verb list still misses ordinary connection verbs — I confirmed that *"**G6** depends on this force for its Latin vocabulary of validity"* placed in §3's `1B-3` Layer 3, with §5's G6 list omitting `1B-3`, returns **"No contradictions."** The Index discloses this weakness in general terms at line 140, so I do not grade it; but it is a live gap and not a theoretical one.

---

## Job 2's harder question — a defect these four controls would not catch

Two, both constructed and run, neither hypothetical:

1. **A cross-cell claim in §3 that §4 does not carry** (see **L3**). Every control passes; the Index prints `*(no §4 row)*` for the force making the claim. This is the §3/§5 gravity defect with "§4" substituted for "§5", and it is unguarded.
2. **A gravity connection asserted in §3 with a verb outside `CONNECT`, omitted from §5** — *"G6 depends on this force"* returns "No contradictions." Disclosed, but the disclosure is doing a lot of work: the control's whole purpose is to be a second opinion on §5, and a second opinion that only recognises twenty-one verbs is a second opinion about vocabulary.

And the largest one, which is not a construction but the live finding: **nothing checks the Index's own hard-coded prose against anything.** The Index says so itself — *"Hard-coded prose, re-verified by nothing"* — and that declaration has been treated for three rounds as a discharge rather than as a standing risk register. It is the reason H1 recurs. The declaration should be paired with a check: a two-line assertion that the Status literal names the same round as Doc_08's Status line would have caught H1 in this round, the last one, and the one before.

---

## A check I confirmed before trusting it, and two of my own that were defective

**Confirmed before reporting: the seven stale review-history sites.** A staleness finding is exactly the kind that dies on a bad grep. I confirmed it three ways before writing it: (1) opening and reading each of the seven sites; (2) an independent sweep for round ordinals and disposition words across both files, cross-read against the `Review-Artifacts/` listing; (3) `git show 02696d24` for each file, which shows the Round 4 fix pass touching the masthead and the closing sentence and no other review-history line in either file. The third is the decisive one, because it distinguishes "stale" from "I searched for the wrong string."

**Also confirmed before reporting: the register-scan residue (L2).** My scan said 5 where Round 4's said 6, which is precisely the situation this build keeps getting wrong. I did not trust my regex: I printed the two Reported-Experience paragraphs with their `[ADDED …]` clauses removed and read them. `3B-1`'s template text contains *"Layer 2"*; `3B-2`'s does not. The finding rests on that reading, not on the scan, and I report both numbers and the likely cause of the difference.

**My first defective check.** Testing the guard that rejects a §5 force ID `§3` does not define, I injected `**4C-9**` into G7's list and the generator emitted a clean index. I was one sentence from reporting a dead guard. The guard is fine: `GRAV_RE`'s token pattern is `\d[AB]-\d`, so `4C-9` was never read as a force ID in the first place — my mutant tested the tokenizer, not the guard. Re-run with `**4A-9**` it fires correctly: `FATAL: §5 names force 4A-9, which §3 does not define.` **The check proved something adjacent to the claim and returned something, which is this build's exact failure mechanism, committed by its reviewer.**

**My second defective check.** My first notice-coverage probe counted notice *openers* against notice *matches* per line and found them equal (32 = 32), which I briefly read as "the stripper covers every notice." It does not: equal counts say nothing about whether each match ends where the notice ends, and nothing at all about notices the opener pattern never sees. Re-framed as "for each bracketed provenance tag, is it inside a removed span?", the answer is 32 of 36 in Doc_08 and 7 of 12 in the Index — which is M1. **A count that balances is not a coverage proof.**

---

## Is the deliverable adequate to proceed to Doc_09?

**The analysis is. The certification is not.**

What Doc_09 needs from this pair is the force→gravity grounding and the transmission findings. Both are now sound: all eight gravities connect, every connection is derived from one source, the `2B-1`/G6 relation is correct against Doc_04 and consistent across all four statements of it, all seventeen forces carry a written Layer 2, the two transmission entries are real entries with named agents, and the quotations hold. **I would not block Doc_09's drafting on the content of this pair**, and I would not ask for a sixth round of the forces analysis.

**But the pair should not be handed to the project lead for disposition in this state**, for one narrow reason: the Disposition paragraph and §9's completion certification are the two places a disposition decision is made from, and both currently state a false review position. A project lead reading line 434 is told independent review has not been run; reading line 460 is told three rounds have been run; reading line 14 is told four. That is not a defect of analysis, but disposition is the one act that turns on it.

**And H2 is a gate on everything downstream.** Doc_09 and the Validation Layer will amend Doc_08. The Index must be regenerated when they do, and there is currently nothing in the build record to regenerate it with.

**Recommendation:** fix H1 and H2 — a short, mechanical pass — and re-submit for a confirmatory read rather than a full round. M1 and M2 should travel in the same pass. L1–L3 and the two cosmetics can be applied without further review.

---

## CO-022 escalation assessment

**Category 1 — Representative identity, title, or voice: does not apply.** This document makes no identity, title or voice decision. Doc_08's own assessment says so and is correct.

**Category 2 — Portfolio-level or cross-world: Doc_08's four items stand, and I add one.** I re-read the four and found them accurately stated: the corpus-wide editorial-apparatus question with eight local instances; the *Boundary Structures* / *Boundary Ecology* inconsistency; the Key Texts / Key Sources template mismatch; the Doc_07 pre-M4 lens structure. The Markdown-versus-workbook line is correctly closed at source (verified at `CiC_Record_Native_World_Build_Process_V1_3.md` lines 156 and 160).

**New item, and it belongs here rather than as a local finding once H2 is fixed:** this is the only world in the portfolio whose index deliverable is produced by a build-authored generator, and the portfolio has no convention for where such a generator lives, whether it is a deliverable, or whether a regenerated index must be diffed before commit. The Round 3 fix pass regenerated the Index, got identical tables back and did not read them — which is how Round 4's H1 shipped. **Carried as a portfolio question: index generators are build artifacts and should be committed, named by path in the artifact they produce, and accompanied by a "diff before commit" step.** Not decided here.

**Category 3 — Governance or methodology: Doc_08's five items stand, unchanged.** The three-way divergence on FF's three-layer rule across this world, Donatism and Alexandria remains open and is properly framed at §8; two of the three readings sit in disposed documents, which is what makes it a portfolio question rather than a local one. The **Construction-record notes** block — defined by no template, used by no sibling — is correctly carried with it. I add nothing and subtract nothing.

**Category 4 — Unresolved tensions: one open**, the 411 *Gesta*, relied on for nothing here. Correctly stated, and I confirmed that no force in the matrix draws on it.

**Never self-assigning Frozen status:** observed. Neither file self-certifies, neither claims Frozen, and both say so in terms. That discipline has held in all five rounds and is worth recording as held.

**One governance observation that is not an escalation.** `Doc08_Round4_Review.md` is the only Doc_08 review artifact that does not carry the Constitution's mandatory *"Simulated review — informational only, not an Article 31 substitute"* marking (Rounds 1–3 carry it; Round 4 does not). That is a defect in a review artifact rather than in either deliverable, so it is not a finding against Doc_08 — but the marking is constitutional and should be added retroactively.

---

## On the brief that commissioned this review

Two corrections, per the instruction not to inherit its claims.

1. **The brief states that `2B-1` was restored "on the ground that Doc_04 §6's Interaction Matrix makes the Candidate 2→6 and 2→7 relations asymmetric" and asks me to verify that reading. The reading is right, and the brief — like the document — omits that Doc_04 marks the 2×6 cell as *"this document's own reading."*** That omission is M2, and it travelled from the document into the brief unremarked, which is a small demonstration of how the elision works.

2. **The brief points me at `/tmp/…/scratchpad/gen_force_index.py` as "the script", and in doing so reproduces the assumption that makes H2 possible.** The script at that path is not the build's generator; it is a copy in a session-scoped directory. Reading it answers "does this code produce this Index" and not "does the build record contain a generator." Five rounds have asked the first question. Nobody asked the second.

Otherwise the brief's framing was accurate and its ordering of risk was good: the `2B-1` reversal and the notice stripper were the right two places to look hardest, and the instruction to check **both** files was the instruction that found H1.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH, 3 MEDIUM, 3 LOW, 2 COSMETIC.**

**What I tested hardest:** the `2B-1`/G6 reversal against Doc_04 §§3, 5 and 6 directly; the notice stripper, against nine mutants; the four advertised controls, all reproduced; the two hard guards, both made to fire; the §8 register scan, in four variants; and the review-history sweep, confirmed three ways including by git.

**What changed this round.** For the first time, **the forces analysis is not where the defects are.** The document's substance has converged: the six-cell matrix, the three layers, the cross-cell table, the gravity synthesis and the transmission dimension are sound, internally consistent, and correctly grounded in Doc_04 and in the sources. The `2B-1` question that ran through four rounds is settled, and settled on the right evidence. If the remaining findings were only the LOWs and the cosmetics, this review would say MINOR REVISION and mean it.

They are not. The verdict turns on two things, and both are about the record rather than the reasoning: **a document that tells a project lead, at its own completion certification, that independent review "has not been run" after four rounds; and a derived index whose generator is not in the build.** The second has been invisible to five rounds of review because every round, including this brief, was handed a working copy and stopped asking. Neither requires another look at the forces analysis.

**What would change the verdict to CLEARED or MINOR REVISION:** commit the generator and name its path in both files; make the seven review-history sites true; widen the notice regex and add a coverage assertion; restore the Doc_04 hedge. That is one fix pass, and I would expect the next round to be a confirmatory read.

*Simulated review — informational only, not an Article 31 substitute.*
