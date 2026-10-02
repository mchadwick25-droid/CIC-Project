# Doc_08 — Forces Document, `lpc_Force_Index.md`, and `scripts/gen_force_index.py`: Latin Pastoral-Congregational Christianity
## Round 6 Independent Adversarial Review — verification of the Round 5 fix pass, and the first review of the generator as a deliverable

**Reviewer:** independent adversarial pass, no authorship of the material under review.
**Date:** 2026-09-15.
**Deliverables reviewed:** `Doc_08_Forces_Document.md` (472 lines), `lpc_Force_Index.md` (158 lines), `scripts/gen_force_index.py` (602 lines) — all three REVISED after Round 5 at commit `0e70a96a` and unreviewed.
**Prior rounds:** Round 1 (4H 5M 3L 1C), Round 2 (3H 4M 3L 1C), Round 3 (4H 5M 4L 2C), Round 4 (3H 3M 5L 1C), Round 5 (2H 3M 3L 2C) — all SUBSTANTIAL REVISION REQUIRED.

*Simulated review — informational only, not an Article 31 substitute.*

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**1 HIGH, 4 MEDIUM, 4 LOW, 2 COSMETIC.**

**Said plainly, because five prior rounds of the same verdict is a reason to be careful, not a reason to reach for a sixth:**

- **The forces analysis is sound and I would clear it for Doc_09 today.** I found nothing against it. Round 5's judgement on this point holds and I add no qualification to it. Eight of the eight quotation-and-attribution spot checks, cross-file numerics, gravity completion, transmission entries and Layer-2 substance came back clean.
- **Round 5's H2 is fully closed.** The generator is in the repository, runs from any working directory, reproduces the committed Index byte-for-byte, and is named by path in both files.
- **Round 5's M1, M2, M3, L1, L2, L3, C1 and C2 are closed**, several of them thoroughly — M2 in particular is closed better than it was asked to be.
- **Round 5's H1 is not closed.** Two live false review-status statements remain in Doc_08's Disposition section, one of them inside the very sentence the Round 5 fix pass rewrote to correct this defect, the other in the paragraph whose own correction notice reads *"The discipline was adopted and then applied to two of the four sites that needed it."* This is the sixth consecutive round in which this class of statement has been found stale.
- **The new machine guard installed to end that recurrence does not see either of them**, and I got three further false review-status claims past it, including a masthead rewritten to *"REVISED after Round 2 … **Two** independent adversarial review rounds have been run."*
- **Three of the eight advertised controls are narrower than the Index states.** Two of those three I defeated with the exact scenario the control's own notice narrates, moved a few words.

**The distance to clearance is short — two sentences and four guard widenings — but a HIGH genuinely remains and the generator's guard claims genuinely overstate.** That is SUBSTANTIAL REVISION REQUIRED, not MINOR REVISION.

---

## Method — what I actually opened, ran and mutated

**Read in full:** all three deliverables; `Review-Artifacts/Doc08_Round5_Review.md`; the Round 5 fix commit `0e70a96a` (diff, per file); the Round 4 fix commit `02696d24` (for the provenance of the two stale sentences).

**Read at the destination, not through Doc_08's account of them:** `Doc_04_Gravity_Discovery.md` §3 (Candidate 2 and Candidate 6 Interaction and Persistence tests, lines 44–48 and 114–118) and §6 (the Interaction Matrix, lines 190–201); `L3A-Shared-Methodology` Forces Framework plain text; `Build/reference/method/CiC_Record_Native_World_Build_Process_V1_3.md` lines 150–162; `lpc_Decision_Log.md`'s Round 5 entry (lines 1245–1275); `Lexicon_Deployment_Index.md`; the Cyprian XML at `/tmp/claude-0/…/scratchpad/cyprian.xml`.

**Ran, rather than read:**

1. **The generator, from `/`**, on an untouched copy of the world directory — output diffed against the committed `lpc_Force_Index.md`: **byte-identical.**
2. **Sixteen mutants** of `Doc_08_Forces_Document.md`, each regenerated and the resulting Index inspected: the eight advertised controls A–H reproduced; three probes of the Layer-2 presence test; three probes of the round-count assertion; one notice-over-consumption probe at two placements; one cell-assignment probe.
3. **Five probes of `verdict_counts`** against synthetic Round 6 and Round 7 artifacts — differently phrased verdicts, a missing `## VERDICT` heading, a numbering gap, a duplicate file, and a predecessor's counts recited inside the parse window.
4. **A notice-coverage census** of both files: every bracketed provenance tag classified against the spans `strip_notices` actually removes, plus a check that no full-text notice match crosses a structural marker.
5. **A structural review-history sweep** — not a phrase list. Every fragment in Doc_08 containing a numeral or an ordinal word within ninety characters of *round*, *rounds*, *review* or *reviewed*, printed and read. Twenty-three fragments; two are false.
6. **A Layer-2 length census**, measuring each of the seventeen Layer 2 blocks with and without notice text, to see whether the presence check reads correction notices as source.
7. **Quotation verification** with `<note>` spans marked before tag-stripping and `<div1>`–`<div4>` `title=` attributes converted to surviving work sentinels.
8. **`git show` on both fix commits**, per file, to distinguish *stale* from *I searched for the wrong string*.

---

## Job 1 — Round 5's ten findings, closure status at the live text of all three files

| # | Round 5 finding | Status at the delivered text |
|---|---|---|
| **H1** | Review history stale at seven sites, including §9's *"which has not been run"* | **NOT CLOSED.** All seven named sites are corrected, and §9's line 434 is corrected well. **Two further sites, both in the Disposition section, are false — one of them inside a sentence the fix pass rewrote.** See **H1** below. |
| **H2** | Generator not in the repository | **CLOSED, thoroughly.** At `scripts/gen_force_index.py`, tracked, `BASE` resolved from `__file__`, named by path at Doc_08 line 12 and Index lines 5–6, recorded in the Decision Log. Runs from any cwd and reproduces the committed Index exactly. One residue at **L3**. |
| **M1** | Notice stripper covered one of two syntaxes | **CLOSED for the file that is parsed.** My census: **43 provenance tags in Doc_08, 43 inside a stripped span, 0 openers surviving.** The coverage assertion is real and fires. (The Index has one uncovered tag; the Index is output, never input, so this is not a defect.) New residues at **M1** and **M2** below concern *where* stripping is applied, not *which syntaxes*. |
| **M2** | Doc_04 §6 hedge dropped from both quotations | **CLOSED, and better than asked.** Hedge restored verbatim at §5 and §3; the two unhedged Doc_04 §3 corroboration loci are now cited; the gravity-to-force step is stated as this document's own inference. Verified verbatim against source — see the verification section. One cosmetic residue at **C1**. |
| **M3** | *"cannot drift"* at line 12 | **CLOSED.** Line 12 now states the narrower claim and names the drift that falsified the old one. |
| **L1** | *"both rows"* / G6 | **CLOSED.** Now *"both phases"*, and the G2 clause carries the six-word qualification Round 4's H2 asked for. |
| **L2** | Six-hit residue attribution at `3B-1` | **CLOSED, and correct.** Now *"five hits, not four — 3B-2 loses one, 3B-1 loses none."* I reproduced the underlying fact independently: with `[ADDED …]` clauses removed, `3B-1`'s marker text contains *"Layer 2"* and `3B-2`'s does not. |
| **L3** | No §3-vs-§4 control | **CLOSED.** Implemented at generator lines 383–403, printed at Index §6, and it fires — control (E) reproduced. |
| **C1** | Ungrammatical workbook sentence | **CLOSED.** Now *"…are **RETIRED for new builds**, in an index-artifacts paragraph that closes with…"*. Both quoted strings and the paragraph heading verified at source. |
| **C2** | *"Both directions are tested"* | **CLOSED.** Now *"All three directions are tested; see below."* |

**Nine closed, one not.** The one not closed is H1, and it is not closed in the direction the brief and Round 5 both warned about: **the fix landed at the seven sites the review enumerated and nowhere else.** Round 5's own fix instruction anticipated this — *"Replace the phrase-list sweep with a structural one … enumerate every sentence in either file containing a round ordinal, a review-round count, or a disposition status word, and read all of them"* — and that instruction was not followed. It takes two minutes; I ran it and it finds both sites immediately.

---

## HIGH

### H1 — Two review-status statements in Doc_08's Disposition section are false. One survived inside the sentence the Round 5 fix pass rewrote to correct exactly this defect; the other sits directly above a correction notice about a review-status claim *"false since Round 1."* The new machine assertion sees neither.

**Site.** `Doc_08_Forces_Document.md` line 466 (Disposition, review-history paragraph, final clause) and line 472 (Disposition, the build-cycle paragraph).

**What I found.**

Line 466, as delivered, reads in part:

> **Five independent adversarial review rounds have been run against this document and `lpc_Force_Index.md`**, all five returning **SUBSTANTIAL REVISION REQUIRED**: Round 1 (4H 5M 3L 1C), … Round 5 (2H 3M 3L 2C). … **[CORRECTED, 2026-09-15 — Round 5's H1:** this paragraph said *three* rounds while the masthead said four … **Seven sites carried a stale review history; the Round 4 fix pass corrected the two a reviewer had quoted.**]** **All findings from all three rounds are addressed above or in the Index**, each correction marked in place.

The sentence immediately following the correction notice that diagnoses partial application **is itself a partially applied correction.** `git show 02696d24` shows the pre-fix line read *"**Three** independent adversarial review rounds … all **three** returning … All findings from all **three** rounds are addressed."* The Round 5 fix pass changed the first two occurrences and left the third, **within a single rewritten line.** A project lead reading this paragraph is told that findings from Rounds 4 and 5 may not be addressed, two sentences after being told there were five rounds.

Line 472, bolded, in the build-cycle paragraph:

> **Four documents in this world — Doc_04, Doc_05, Doc_06 and Doc_07 — are complete, independently reviewed, and awaiting a disposition only the project lead can give. This is the fifth, and it has now been through four review rounds.**

`git show 02696d24` shows this sentence was written by the **Round 4** fix pass, where *"four review rounds"* was true. The Round 5 fix pass did not touch the paragraph. It is now false by one. It sits immediately above the correction notice reading *"a review-status claim false since Round 1, in the revision that adopted a standing discipline about exactly these lines. **The discipline was adopted and then applied to two of the four sites that needed it.**"*

**The guard installed this round to end the recurrence does not see either sentence.** `gen_force_index.py` lines 66–78 assert Doc_08's hand-maintained round count against `Review-Artifacts/`. Run on the live document, its two branches see:

```
log-row claims found:        [1, 2, 3, 4, 5]   max = 5   ✓ agrees with 5 artifacts
word-number claims it sees:  ['Five']          — one, at line 466's opening
what it does not see:        '…addressed above or in the Index' → "all three rounds"
                             '…This is the fifth, and it has now been through four review rounds'
                             '**Five** independent adversarial review rounds' (masthead, line 14)
```

The word branch requires `\b(One|…|Ten)\s+independent adversarial review rounds`. Line 14 writes `**Five** independent` — **the bold markers break `\s+`, so the Status line, the single most-read review-status line in the document and the one H1 was originally about, is not covered at all.** The generator's own code comments warn about this trap twice (*"This build has hit the '**bold** defeats the regex' trap before, so it is normalised once, here"*) and the new assertion does not normalise.

**Why this matters.** Constitution Article 30 and CO-022 make disposition turn on review status, and the Disposition section is the single place that decision is made from. It now states the correct headline count in three places and a false one in two others, one of which is bolded as a summary of the document's position. This is the sixth consecutive round in which this class has been found stale, and the fourth in which the fix landed only where a reviewer had pointed.

**How I confirmed it, four ways, before writing it.** (1) Direct read of both sentences in the delivered file. (2) A **structural** sweep — every fragment containing a numeral or ordinal word within ninety characters of *round/rounds/review/reviewed*, twenty-three fragments, all read; the two false ones fall out and nothing else does. (3) `git show 02696d24` and `git show 0e70a96a` per file, which establish that line 466's clause survived a rewrite of its own line and that line 472 was written true at Round 4 and left untouched at Round 5 — this is the step that distinguishes *stale* from *I searched for the wrong string*. (4) The objective ground truth: five `Doc08_Round*_Review.md` artifacts on disk, five review rows in the Document Log, `Five` at line 14, `Five` at line 466's opening, `five times` at line 434.

**Fix.**
1. Line 466: *"All findings from all **five** rounds are addressed above or in the Index."*
2. Line 472: *"This is the fifth, and it has now been through **five** review rounds."*
3. **Do not add a seventh phrase to a phrase list.** Widen the assertion structurally (see **M3**): normalise `**` out of the text before matching; accept lowercase ordinals and numerals; match `\b(ordinal|numeral)\s+(independent adversarial )?(review )?rounds?\b`; and add a check on the ordinal in *"REVISED after Round N"* and *"the most recent … Doc08_Round N"*. On the current text that is a dozen lines and it catches every site in this finding.

---

## MEDIUM

### M1 — The Layer-2 presence check is the one derivation notices are *not* stripped from, contradicting the generator's own stated rule. A blank Layer 2 padded with a correction notice passes; a real Layer 2 beside a notice that *quotes* a stub phrase fails.

**Site.** `gen_force_index.py` lines 165–188 (the Layer 2 extraction and stub test) against its own comment at lines 74–80 (*"Notices are stripped before ANY derivation, everywhere, once"*); `lpc_Force_Index.md` §1's Layer 2 column and §5's *"Every force carries a written Layer 2 — **YES** — all 17"*; `Doc_08_Forces_Document.md` §9's checklist tick and §8's From-Within certification.

**What I found.** Every other derivation in the generator runs on `strip_notices(...)`. This one does not:

```python
m3 = re.search(r"\*\*Layer 2 — World's Own Experience\.\*\*(.*?)(?=\*\*Layer 3)", body, re.S)
raw = m3.group(1) if m3 else ""          # body, not strip_notices(body)
…
f["stub"] = (len(f["layer2"]) < 40) or any(pat in low for pat in (…))
```

Both limbs of the stub test therefore read correction-notice text as though it were the world's voice. **This is already live, harmlessly:** measuring all seventeen blocks with and without notice text, `3B-1` measures 1187 characters of which **259 are notice**, and `3B-2` measures 925 of which **115 are notice**. Both clear the floor on their real content, so **there is no wrong value in the delivered Index.**

**It is exploitable in both directions, and I ran both.**

| Mutant | Result |
|---|---|
| `1A-1`'s Layer 2 replaced entirely by a ~250-character `[CORRECTED …]` notice | Master table prints **✓**; §5 prints *"Every force carries a written Layer 2 — **YES** — all 17"*; summary prints *"every force carries a written Layer 2"* |
| Same, with a short notice (below the 40-char floor) | **STUB**, 1 missing — confirming the mechanism is the notice text clearing the floor, not something else |
| `1A-1`'s **real, complete** Layer 2 kept, with a notice appended that quotes *"left unfilled"* | **STUB**, *"1 force(s) MISSING a Layer 2"* — a false failure against a sound entry |

**The third is the likely accident, not the first.** This document's house style is to record corrections in place, and its notices quote precisely the strings the stub detector looks for — *"left unfilled"*, *"Not applicable at this layer…"*, *"deliberately unfilled"* — at Index §5 and Doc_08 §8 and §9 today. The next fix pass that records such a notice inside a Layer 2 block will make the Index contradict Doc_08 §9's tick, and the Index will look like the authority.

**Why this matters.** This is Round 2's H3 — a presence test that certified a blank Layer 2 — reopened through the channel Round 4's H1 established. The From-Within Principle certification at Doc_08 §8 and §9's checklist both rest on this column, and the Forces Framework's *"This is not optional. All three layers are required for every force"* is the rule being certified.

**Fix.** One character of change: `raw = m3.group(1)` → `raw = strip_notices(m3.group(1))`, *before* the Construction-record split. Then make the generator's comment true by adding an assertion that no derivation input contains a notice opener — it already has `OPENER` and `assert_notice_coverage`; apply the same test to each extracted Layer 2. Re-run all three mutants above.

### M2 — Control (G) does not close the notice-over-consumption class. The exact scenario its own notice narrates — *"silently cutting G2 from four forces to two"* — still succeeds when the malformed notice is placed one clause later.

**Site.** `gen_force_index.py` lines 36–58 (`STRUCTURAL`, `assert_notice_coverage`); `lpc_Force_Index.md` §6, control **(G)**.

**What I found.** The guard refuses to emit when a notice match contains `Connected forces:`, a line-initial `**G\d — `, or a line-initial `#### `/`### `. Placement decides whether it sees anything.

| Placement of a malformed `**[ADDED, … .]` (bare `]`, no `**`) on §5's G2 line | Result |
|---|---|
| **Before** `Connected forces:` | `FATAL: a correction notice … spans a structural marker … Refusing to emit.` — control (G) as advertised |
| **After** `Connected forces:`, before the first force ID | **Index emitted, exit 0.** `G2` prints **`2B-1`, `2B-2` — 2 forces**, down from four. All three hard guards clean: 17 forces, 8 gravities, 15 connections |

The span runs forward to the `]**` that terminates the real `[ADDED, 2026-09-15 — Round 2's H2:…]**` notice further along the same line, eating `**1A-1**` and `**1B-1**` between them. That is the described failure, reproduced, against the guard installed to stop it.

**What saves it, and I record this because it bears on the grading.** The §3/§5 reconciliation control *does* fire, printing two contradiction rows (`1A-1`/G2 and `1B-1`/G2). So the wrong Index is not silent — but it is presented as *"2 contradiction(s). Each is a finding for a reviewer, not a defect this file resolves,"* i.e. as findings against Doc_08's prose rather than as a parse failure. A reader chasing those two rows would go to §3, find the assertions genuine, and have no reason to suspect §5's line was eaten.

**Why this matters.** The notice-as-derivation-input class has produced a HIGH in two separate rounds. It is now guarded by a structural-marker test that is a proxy for the property that matters — *did this match consume real source* — and the proxy is defeated by moving the plant three words. This is the build's named mechanism: **a check that proves something adjacent to the claim, then is trusted because it returned something.** The literal words of control (G) are true; the implication a reader takes from them is not.

**Fix.** Test the property directly rather than by proxy. A notice match that contains a force-ID token, a gravity token, or more than one `**…**` span it did not open is over-consuming regardless of where it starts — refuse on that. Cheaper and stronger: require the terminator to be well-formed at all, i.e. also accept a bare `]` as a terminator (`\]\*{0,2}`), which removes the forward-running match entirely; the line-bounded strip then makes over-consumption impossible rather than detectable. Narrow (G)'s wording in the Index to the placements actually tested.

### M3 — The round-count assertion, and control (H) that advertises it, are much narrower than stated. Three false review-status claims pass, including a masthead rewritten to Round 2.

**Site.** `gen_force_index.py` lines 66–78 (`assert_doc08_round_count`); `lpc_Force_Index.md` §6, control **(H)**: *"a Doc_08 that claims a different number of rounds than `Review-Artifacts/` contains halts the generator."*

**What I found.** Three mutants, each a flatly false review-status claim, each regenerated successfully with no warning:

| Mutant | Guard | Resulting Index |
|---|---|---|
| Masthead rewritten: *"**REVISED after Round 2** … **Two** independent adversarial review rounds have been run"* | **passes** | Index Status prints *"REVISED after Round 5"* — reproducing the Doc_08-vs-Index drift H1 was raised about |
| Document Log's **Round 3 and Round 4 rows deleted** | **passes** | `max(claims)` is still 5; a Log missing two rounds is invisible |
| *"**two** independent adversarial review rounds"* (lowercase) | **passes** | word branch is capital-initial only |

And the two live sentences in **H1** pass it as well — *"all three rounds"* and *"four review rounds"* match neither branch.

The mechanism in each case is the same: the assertion tests **one phrasing of one claim** (`Round N independent adversarial review|fix pass`, and capital-initial ordinal + the exact ten-word phrase) and is described as testing the claim. Worse, `max(claims)` is an **ordinal** and `NROUNDS` is a **cardinal**; they coincide only when the artifacts are numbered 1..N with no gaps or duplicates. Two further probes exercise the conflation: a numbering gap (Round 7 present, Round 6 absent) yields an Index headed *"REVISED after Round 7"* with *"**Six** independent round(s) have been run"*; a duplicate `Doc08_Round05_Review.md` yields `FATAL: … Review-Artifacts/ holds 7`, a halt with a misleading reason.

**What does work, and is worth keeping.** Adding a `Round 6 independent adversarial review` row with only five artifacts on disk halts correctly. The asymmetry is the point: the guard is good at *forward* drift (the Log ahead of the artifacts) and blind to *backward* drift (the Log, masthead or Disposition behind them) — and backward drift is the failure this build has actually committed, six times.

**Why this matters.** Round 5's H1 fix was accepted on the strength of this guard: *"A number that is counted cannot be forgotten."* The number is counted; the claims about it are still written in prose the counter does not read.

**Fix.** Normalise `**`, `*` and `` ` `` out of the text before matching; case-fold; accept numerals and ordinals; match the family `\b(ordinal|numeral)\s+(independent adversarial )?(review )?(rounds?|times)\b` and `REVISED after Round (\d+)` and `Round (\d+) fix pass` and `the most recent .*Doc08_Round(\d+)`; compare **every** hit to the counted value and print all disagreements rather than the first. Then re-run all five mutants above, plus the two live sentences. Restate control (H) in the Index to name what it covers.

### M4 — The Index's "derived" review-history line is only half derived: `verdict_counts` is anchored to a character window rather than to the artifact's own verdict, and the verdict itself is hard-coded.

**Site.** `gen_force_index.py` lines 88–104 (`verdict_counts`, `HISTORY`, `LATEST`) and lines 302–304 and 594 (the rendered lines); `lpc_Force_Index.md` lines 3–5 and the Disposition.

**What I found.** Three distinct weaknesses at one site.

**(a) The anchoring moved the recitation bug rather than removing it.** The docstring states the problem exactly — *"A first version searched the whole file and returned Round 1's counts for every round, because each later artifact recites its predecessors' counts before stating its own."* The fix takes the first `HIGH…MEDIUM…LOW…COSMETIC` match within 1200 characters of the first `## VERDICT` heading. That works on the five artifacts that exist (I measured: the match lands at +45 to +55 characters in every one) **because none of them happens to recite a predecessor in that form inside the window — not because anything prevents it.** I wrote a synthetic Round 6 artifact whose verdict section reads *"Round 5 returned 2 HIGH, 3 MEDIUM, 3 LOW, 2 COSMETIC and all of it is closed"* before its own *"1 HIGH, 0 MEDIUM, 2 LOW, 1 COSMETIC"*, and the Index printed:

> Round 5 (2H 3M 3L 2C); **Round 6 (2H 3M 3L 2C)**

— the predecessor's counts under the successor's label, silently, in the line whose whole purpose is that it cannot go wrong. `re.search` takes the first match in the window whatever it belongs to; nothing ties the match to the artifact's own verdict.

**(b) The verdict word is not derived at all.** `verdict_counts` reads only the four numbers; the heading line it anchors on carries the verdict and is discarded. The Index then hard-codes *"— **all SUBSTANTIAL REVISION REQUIRED**"* and *"({counts}, SUBSTANTIAL REVISION REQUIRED)"*. My synthetic Round 6 artifact says `## VERDICT: MINOR REVISION`; the Index reported it as SUBSTANTIAL REVISION REQUIRED. **This will be false the first time a round returns anything else** — which, on the trajectory of Rounds 4 → 5 → 6, is not a remote hypothetical.

**(c) `LATEST` is the highest artifact number, and it is used as the *fix-pass* ordinal.** The rendered lines say *"**REVISED after Round {LATEST}**"*, *"Revised: … (Round {LATEST} fix pass)"* and *"this file is the Round {LATEST} fix pass and is **unreviewed**"*. In the window between a review being filed and its fix pass being applied — which is where this pair sits right now, and where it will sit the moment this artifact is committed — those three statements become false by construction. My probe confirms it: with a Round 6 artifact on disk and no Round 6 fix pass, the Index asserts it *is* the Round 6 fix pass.

**What is genuinely good here, and I record it.** Degradation is graceful where it matters: an artifact with no `## VERDICT` heading reports *"no VERDICT heading"*, and one whose counts are spelled in words reports *"counts not parsed"*. Neither guesses. That is the right instinct and it should be extended to (a) and (b).

**Operational note for the fix pass.** Once this artifact is committed, `Review-Artifacts/` holds six and Doc_08's Log names five, so **the generator will refuse to emit until Doc_08's Document Log gains its Round 6 row.** That is the guard working as designed; it is stated here so the halt is not mistaken for a defect.

**Fix.** Parse from the VERDICT *heading line* — capture the verdict word off `## VERDICT[:\s]*(.+)` and search for the counts only up to the next `##` heading or the next `## VERDICT`, not a character budget; report *"counts not parsed"* rather than a neighbour's. Render the verdict per round instead of a blanket literal. Separate `LATEST_REVIEW` from `LATEST_FIX_PASS`, taking the latter from Doc_08's Document Log, and let the Status line say *"reviewed through Round 6; this file is the Round 5 fix pass"* when those differ.

---

## LOW

### L1 — Nothing ties a force to the cell it is filed under, and nothing compares the Index's derived cell distribution to Doc_08 §9's hand-typed one. Demonstrated defect; all eight controls clean.

**Site.** `gen_force_index.py` lines 126–150 (`CELL_RE` / `FORCE_RE` parse); `Doc_08_Forces_Document.md` line 421 (§9 checklist).

This is the defect the brief asked me to construct — one that none of the eight controls catches. I moved `#### Force 2A-2`'s block so that it sits under `### CELL 1B` instead of `### CELL 2A`, changing nothing else, and regenerated:

```
master row:  | **2A-2** | Initiating / Internal | …
summary:     **17 forces** — 1A (2), 1B (4), 2A (3), 2B (5), 3A (1), 3B (2)
Doc_08 §9:   — 1A (2), 1B (3), 2A (4), 2B (5), 3A (1), 3B (2) = **17 forces**
§6:          No contradictions.  No disagreements.  (observations unchanged)
```

Exit 0. No guard, no contradiction, no observation, no cross-cell disagreement. The force's own ID says Ongoing/External and its row says Initiating/Internal, and §9's certification of the cell distribution — a **third** hand-maintained restatement of a derived relation, alongside §7's confidence list and §3's gravity prose, both of which *are* cross-checked — is the one nothing reads.

**Fix.** Two assertions, about four lines each: `FATAL` if a force's ID prefix does not match the `### CELL` heading it was parsed under; and read §9's `1A (n), 1B (n), …` line and compare it to the derived counts, in the same spirit as the §7 cross-check. The second closes the general hole; the first closes the specific one.

### L2 — Index §6 says *"Four checks"* and then enumerates eight.

**Site.** `lpc_Force_Index.md` line 138 (`gen_force_index.py` line 561).

> **What was run to satisfy the author that these controls work…** **Four checks**, all reproducible from the saved generator. **(A) Regression** … **(H) Negative control, review history.**

Eight lettered controls follow; the closing sentence of the same paragraph correctly says *"controls E through H each caught something on their first run."* The Round 5 fix pass added (E)–(H) and did not touch the sentence that counts them — the same mechanism as Round 5's C2 (*"Both directions are tested"* above *"Three tests now, not one"*), one round later, in the same paragraph. The word *"saved"* is now true and needs no change.

**Fix.** *"Eight checks, all reproducible from `scripts/gen_force_index.py`."* Better: render the count from the number of lettered entries so it cannot go stale a third time.

### L3 — Round 5's H2 fix landed three limbs of four: the regeneration command is recorded nowhere, and the `argv[1]` override is unguarded.

**Site.** `scripts/gen_force_index.py` line 20; `lpc_Decision_Log.md` lines 1253, 1271; `Doc_08_Forces_Document.md` line 12; `lpc_Force_Index.md` lines 5–6.

Round 5's H2 fix had four limbs. Three are done well. The fourth — *"Record it in `lpc_Decision_Log.md` with the one-line command that regenerates the Index"* — is half done: the Decision Log records the generator's existence, path and rationale at length, but **the command appears nowhere in any of the three deliverables or the Decision Log.** I searched all four for `python`, `python3` and `Regenerate with`: no hits. The repository's own convention, which Round 5 cited, is to state it (`.gitignore`: *"Regenerate with: python cic/engine/corpus_index.py --build"*).

Two smaller residues at the same site:

- `BASE = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else …` takes **any** first argument as a base directory. `python3 gen_force_index.py --help` resolves `BASE` to `./--help` and dies in a raw `FileNotFoundError` traceback. It fails safe — nothing is written — but the override cannot be distinguished from a mistyped flag, and an undocumented positional override is itself a small trap. A named flag (`--base`) with an `argparse` error, or a check that `SRC` exists with a readable message, costs three lines.
- The file carries `#!/usr/bin/env python3` and is committed mode `644`, so `./scripts/gen_force_index.py` does not run.

**What I verified positively:** the script runs correctly from an unrelated working directory (I ran it from `/`) and reproduces the committed Index **byte-identically**; and the sibling precedent the code comment cites, `World-Builds/Donatism/scripts/`, does exist.

**Fix.** Add the command to the Decision Log entry and to the Index header line 5 — one line, e.g. `python3 scripts/gen_force_index.py` run from the world directory. Guard `argv[1]` or name it. `chmod +x`.

### L4 — The index-generator portfolio item the Round 5 fix pass recorded as *"carried at the Disposition"* is not at the Disposition.

**Site.** `Doc_08_Forces_Document.md` line 470 (CO-022 assessment) against `lpc_Decision_Log.md` line ~1269.

The Decision Log's Round 5 entry states: *"**One portfolio item added, at Round 5's recommendation:** index generators are build artifacts and belong in the repository — committed, named by path in the document they derive, and diffed before commit. **Carried at the Disposition;** not decided here."*

Doc_08's CO-022 assessment still reads *"Portfolio-level or cross-world: **four items**, none decided here"* and lists the same four inherited items. The strings `index generator` (as a portfolio item) and `diffed before commit` do not appear in Doc_08 at all — `index generator` occurs once, in the review-history paragraph, describing Round 5's H2.

This matters because CO-022 escalation is the mechanism by which a portfolio-level question reaches the project lead, and because the item is a good one: this is the only world in twelve whose index deliverable is produced by a build-authored generator, and the portfolio has no convention for where such a thing lives or whether a regenerated index must be diffed before commit. Nothing in Doc_08 is *false* here — its own count and list are internally consistent — so this is LOW; but the build record asserts an escalation the deliverable does not carry.

**Fix.** Add it as the fifth portfolio item at line 470, or correct the Decision Log entry to say it was recommended and not carried.

---

## COSMETIC

### C1 — The 2×7 quotation is still trimmed without marking, at both sites — the habit M2 was raised about, one cell over.

`Doc_08_Forces_Document.md` line 334 (§5) and line 161 (§3) quote Doc_04 §6's 2×7 cell as *"Reshaped by (7 is Augustine's own phase-specific reworking of a structurally similar question, not 2's own continuation)"* and *"…not 2's own continuation."* The source (Doc_04 line 195) reads *"…not 2's own continuation **— see §3, §5**)"*. The parenthesis is again closed where the source continues, with no ellipsis — this time dropping a cross-reference rather than a hedge, so nothing material turns on it, and Doc_08 now cites Doc_04 §3 on its own account anyway. §3's companion quotation also substitutes a comma for the source's closing parenthesis, which is ordinary punctuation-inside-quotes practice and not a defect.

**Fix.** Add `…` before the closing parenthesis at both sites, or quote the tail.

### C2 — The control inventory is miscounted as *"a regression, four positive, three negative"* in the Decision Log and in the brief that commissioned this review.

`lpc_Decision_Log.md` line ~1267: *"The Index's §6 now records eight … regression against `9eccc532`, **four positive controls, and three negative** ones that halt the generator."* The Index enumerates **one regression (A), five positive (B, C, D, E, F) and two negative (G, H)** — and only G and H halt; B, C, D and F are positive controls that assert the tables are *unaffected* or that a disagreement *is printed*. The brief for this round reproduces the same 1/4/3 split, which is how I noticed it. Eight is right; the shape is not.

---

## Additional checks that returned clean, and which of them I tested hardest

**The eight advertised controls, all reproduced, none sampled.**

| Control | Claim | My result |
|---|---|---|
| **(A)** Regression at `9eccc532` | reports `1B-1`/G2, `2A-1`/G8, `2B-1`/G7 | **exactly those three**, plus 3 STUB flags (`2B-5`, `3B-1`, `3B-2`) |
| **(B)** False denial | rewriting §3 to deny G6 produces a contradiction row | **2 rows** — `2B-1`/G2 and `2B-1`/G6, *"§3 Layer 3 asserts §5 does NOT carry this"* |
| **(C)** Notice injection, Form A | a bold ID in a `[CORRECTED …]` notice reaches neither table | planted `**3A-1**` in §5's G2 notice: `3A-1` stays `G1`, G2 stays four forces |
| **(D)** Omitted connection | removing `2B-1` from §5's G6 list produces a contradiction row | *"§3 Layer 3 asserts this connection; §5's list omits it"* |
| **(E)** Cross-cell | a Layer-3 claim §4 does not carry produces a disagreement | *"**1 disagreement(s):** `2B-1` names `1B-3`, §4 does not pair them"* |
| **(F)** Unknown notice syntax | `**Heading. [ADDED …]**` is stripped and its planted ID does not reach the tables | planted `**3A-1**` inside a Form-B notice on §5's G7 line: G7 stays `2A-4`, `3B-1`; `3A-1` stays `G1` |
| **(G)** Notice over-consumption | the generator refuses when a notice spans a structural marker | **fires as stated** for a plant before `Connected forces:` — and see **M2** for the placement that defeats it |
| **(H)** Review history | a Doc_08 claiming a different round count halts the generator | **fires** for a Round 6 log row against five artifacts — and see **M3** for three false claims that pass |

**All three hard guards fire.** Deleting a `#### Force` heading → `FATAL: parsed 16 forces, expected 17`. Breaking a §5 gravity heading → `FATAL: parsed 7 gravities … expected 8`. A §5 force ID §3 does not define → `FATAL: §5 names force 4A-9, which §3 does not define.`

**Notice coverage, measured rather than assumed.** Every bracketed provenance tag in `Doc_08_Forces_Document.md` classified against the spans `strip_notices` actually removes: **43 of 43 inside a removed span, 0 openers surviving**, and no full-text notice match crosses a structural marker. Round 5's M1 census was 32 of 36; the widened pattern plus the coverage assertion closes it for the file that is parsed. (The Index shows 13 of 14, at the `**[CORRECTED, …] text …**` form where the bracket closes mid-sentence; the Index is never an input, so this is not a defect — but it is the form that would defeat the stripper if it ever appeared in Doc_08, and the coverage assertion would then halt, which is the right outcome.)

**Regeneration is exact.** The committed generator, run from `/` on an untouched copy of the world directory, produced a `lpc_Force_Index.md` **byte-identical to the committed one**. `BASE` resolves from `__file__` with no session path anywhere in the file. H2's central claim is true.

**M2's restoration verified verbatim at source — tested hardest of the Job-1 items, because it is the one that turns on quotation discipline.**

| Doc_08's quotation | Doc_04 locus | Verdict |
|---|---|---|
| *"Reinforcing (both are boundary/reintegration questions Cyprian reasons about consistently — this document's own reading)"* | §6, line 195, cell 2×6 | **verbatim** |
| *"Reinforces Candidates 1, 3, 4, and 6; reshaped by Candidate 7… not this gravity continuing"* | §3, line 48 (Candidate 2, Interaction) | **verbatim**, elision marked |
| *"Reinforces Candidates 1, 2, 3, and 5."* | §3, line 116 (Candidate 6, Interaction) | **verbatim** |
| *"Reshaped by (7 is Augustine's own phase-specific reworking …, not 2's own continuation)"* | §6, line 195, cell 2×7 | verbatim to the elision; see **C1** |

**And Doc_08's claim about the hedge's scarcity is true, checked two ways.** *"this document's own reading"* occurs **twice inside the matrix, both on row 2** (cells 2×3 and 2×6) and **three times in the whole of Doc_04**, the third at §3 line 44. So *"it sits on exactly two cells in the whole matrix — while the 2×7 cell set against it carries none"* is exact. I add an observation in the document's favour that it does not claim: the **mirror cell 6×2** reads a plain *"Reinforcing"* with no hedge, so Doc_04 states the same relation unhedged in the matrix itself as well as at §3.

**Quotation fidelity — four spot-checks, both documented failure modes applied.** `<note>` spans marked before tag-stripping; `<div1>`–`<div4>` `title=` attributes converted to surviving sentinels.

| Quotation | Site | Apparatus? | Containing work |
|---|---|---|---|
| "these thirteen letters sent forth at various times…" | 2B-5 | outside | *To the Presbyters and Deacons Assembled at Rome* — Cyprian |
| "you always read my letters to the very distinguished clergy…" | 2B-5 | outside (the `<note>` opens immediately after the quotation's last word) | *To Cornelius, Concerning Fortunatus and Felicissimus* — Cyprian |
| "thousands of certificates were daily given…" | 2B-2 | outside | *To the Presbyters and Deacons Assembled at Rome* — Cyprian |
| "by the judgment of God and the favour of the people…" | 1B-2 | outside | *The Life and Passion of Cyprian* — **Pontius the Deacon**, and Doc_08 attributes it correctly: *"A deacon who knew him put it from outside"* |

All clean. The second is worth noting for the discipline it shows: the quotation ends at the exact character where the editorial note begins.

**Governing-document quotations verified verbatim.** FF's *"This is not optional. All three layers are required for every force."* (FF.txt line 141); FF's *"[A] gravity that cannot be connected to the forces acting on the world is a gravity whose ecology is incomplete."* (two occurrences, lines 176 and 200). `CiC_Record_Native_World_Build_Process_V1_3.md` line 160 closes an **Index artifacts** paragraph with *"Do not create new workbooks."* and line 156 carries *"RETIRED for new builds"*.

**Round 5's L2 arithmetic confirmed independently of any regex.** With `[ADDED …]` clauses removed from the Reported-Experience paragraphs, `3B-1`'s marker-only text contains the string *"Layer 2"* and `3B-2`'s does not — so the provenance clauses account for **one** marker hit in total, which is exactly what Doc_08 §8 now says.

**Cross-file numerics.** 17 forces / 8 gravities / 15 connections from the generator, matching §9's ticks and Index §§1–4; §7's cross-check prints *"Agreement: all 17 forces carry the same confidence in Doc_08 §7 as in their own §3 entry"*; §6 prints no contradictions, no cross-cell disagreements, and five observations, all of which I re-derived; Index §5 shows a dedicated transmission force in both 2B and 3B.

**The Round 4 artifact's missing constitutional marking was added.** `Doc08_Round4_Review.md` now carries *"Simulated review — informational only, not an Article 31 substitute"* with a notice recording why it was added retroactively. Round 5's governance observation is closed.

---

## Job 2's harder question — a defect none of the eight controls catches

**Constructed, run, and fully silent: L1's cell-assignment defect.** A force filed under the wrong `### CELL` heading changes its Index row and the derived cell distribution, contradicts Doc_08 §9's hand-typed certification of that distribution, and passes all eight controls, all three hard guards, both reconciliation checks and the cross-cell check with no output of any kind. It is the same shape as the §3/§5 gravity gap and the §3/§4 cross-cell gap — **two statements of one relation, only one of them read** — at the one remaining site where Doc_08 restates a derived relation by hand.

**Two more, both run, both reported above:** the Layer-2 notice channel (**M1**) and the over-consumption placement (**M2**). And the class that keeps recurring, which is not constructible but observable: **the Index's hard-coded prose is still checked by nothing, and the Round 5 fix converted only the review-history *numbers* to derived, leaving the verdict word, the fix-pass ordinal and the control count as literals** (**M4**, **L2**). Round 5 wrote that the *"re-verified by nothing"* declaration *"has been treated for three rounds as a discharge rather than as a standing risk register."* It still is. The two-line assertion Round 5 proposed — that the Index's Status literal names the same round as Doc_08's — would have caught the masthead mutant in **M3**; it was not built.

---

## Checks I confirmed before trusting, and my own defective ones

**Confirmed before reporting: H1.** A staleness finding is the kind that dies on a bad grep, and thirty-two failing checks in this build have been defects in the check. I confirmed H1 **four** ways before writing it: direct reading of both sentences; a **structural** sweep that does not depend on any phrase (numeral-or-ordinal within ninety characters of *round/review*, all twenty-three hits read); `git show` of both fix commits per file, which is the decisive step because it distinguishes *stale* from *I searched for the wrong string* — line 466's clause visibly survived a rewrite of its own line, line 472 was written true at Round 4 and never touched; and the objective ground truth of five artifacts on disk against five Log rows.

**Confirmed before reporting: M1.** I did not rest on the mutant. I first measured all seventeen Layer 2 blocks with and without notice text and found two already contaminated (`3B-1` by 259 characters, `3B-2` by 115), which establishes the mechanism independently of any injection. Then three mutants in both directions — long notice → false pass, short notice → STUB, real Layer 2 plus a stub-quoting notice → false fail — because a single mutant that produces the result you expect is a check that returned something.

**My first defective check, and it would have been three fabricated HIGH findings.** My quotation harness normalised whitespace with `re.sub(r'[ \t]+', ' ', x)` — spaces and tabs, not newlines — and reported *"NOT FOUND"* for three Cyprian quotations that are in the corpus verbatim. Had I trusted it I would have reported three misattributions or fabrications against sound quotations. The XML wraps sentences across lines; with `\s+` all four are found immediately, outside `<note>` spans, in the right works. **The check returned something and proved something adjacent — "this sentence does not appear on a single line of the XML" — which is this build's exact mechanism, committed by its reviewer, again.** I caught it only because a clean *"NOT FOUND"* on three separate quotations at once is implausible in a corpus five rounds have verified.

**My second defective check.** My first over-consumption probe planted a malformed notice, the generator emitted cleanly, and I was one sentence from writing *"control (G)'s guard is dead."* It is not dead: moved three words earlier, before `Connected forces:`, it fires exactly as advertised. The true finding is narrower and I rewrote it as **M2** — the guard covers the placements that span a marker and not the class. I ran both placements before grading.

**A third, smaller.** My notice-coverage census initially flagged the Index as having an uncovered tag and I nearly graded it. The Index is never read by the generator; it is output. Nothing derives from it, so there is nothing to poison. Recorded above as a non-defect.

---

## Is the deliverable adequate to proceed to Doc_09?

**The analysis is — without qualification. The certification apparatus is one edit away, and the generator's guard claims need narrowing.**

What Doc_09 needs from this pair is the force→gravity grounding and the transmission findings, and both are sound: all eight gravities connect, every connection derives from one source, the `2B-1`/G6 relation is correct against Doc_04 §§3 and 6 and consistent across all four statements of it, all seventeen forces carry a real written Layer 2, the two transmission entries are real entries with named agents, and the quotations hold on both documented failure modes. **I would not ask for a seventh round of the forces analysis and I would begin Doc_09 now.**

**The pair should still not go to the project lead for disposition**, for one narrow and now-familiar reason: the Disposition section is where that decision is made, and two of its sentences state a false review position. That is a two-minute edit, not a revision.

**And the generator, reviewed as a deliverable for the first time, is good work with three overstated guarantees.** It is committed, portable, reproducible, degrades gracefully in two places where it could have guessed, and four of its eight controls caught real defects on their first run. What it should not do is describe proxies as though they were the properties they proxy — control (G) for over-consumption, control (H) for review-status truth, and the "derived" review-history line for a review history that is still half typed. **A control stated more broadly than it is implemented is worse than no control, because the next round will trust it.** That is the single sentence I would carry forward from this review.

**Recommendation:** fix H1 (two words), M1 (one function call), and narrow the wording of controls (G) and (H) to what they test — then widen them, in that order. M3, M4, L1 and L2 are generator work and can travel together. L3, L4 and the cosmetics can be applied without further review. **Re-submit for a confirmatory read of the generator's guards, not a seventh full round.**

---

## CO-022 escalation assessment

**Category 1 — Representative identity, title, or voice: does not apply.** This document makes no identity, title or voice decision. Doc_08's own assessment says so and is correct.

**Category 2 — Portfolio-level or cross-world: Doc_08's four items stand, and the fifth is missing.** I re-read the four and found them accurately stated: the corpus-wide editorial-apparatus question with eight local instances; the *Boundary Structures* / *Boundary Ecology* inconsistency; the Key Texts / Key Sources template mismatch; the Doc_07 pre-M4 lens structure. The Markdown-versus-workbook line is correctly closed at source, verified at `CiC_Record_Native_World_Build_Process_V1_3.md` lines 156 and 160. **The index-generator item that Round 5 raised and the Decision Log records as carried is not in the assessment** — see **L4**. It should be, and I restate it here so it is not lost a second time: *index generators are build artifacts; the portfolio has no convention for where they live, whether they are deliverables, or whether a regenerated index must be diffed before commit.* Not decided here.

**Category 3 — Governance or methodology: Doc_08's five items stand, unchanged.** The three-way divergence on the Forces Framework's three-layer rule across this world, Donatism and Alexandria remains open and is properly framed at §8; two of the three readings sit in disposed documents. The **Construction-record notes** block — defined by no template, used by no sibling — is correctly carried with it. I add nothing and subtract nothing.

**Category 4 — Unresolved tensions: one open**, the 411 *Gesta*, relied on for nothing here. I confirmed no force in the matrix draws on it.

**Never self-assigning Frozen status: observed.** Neither file self-certifies, neither claims Frozen, and all three deliverables say so in terms. Six rounds, held every time.

**A governance observation that is not an escalation.** Committing this artifact will put six review files in `Review-Artifacts/` against a Document Log naming five, and the generator will refuse to emit until Doc_08's Log is updated. That is the halt working as intended, but it means **the Index cannot be regenerated during the window between a review being filed and its fix pass being applied.** Worth a deliberate decision rather than a discovery: either the Log row is added when the review is filed, or the assertion should warn rather than halt when the artifacts are *ahead* of the Log.

---

## On the brief that commissioned this review

Three corrections, per the instruction not to inherit its claims.

1. **The brief describes Index §6's eight controls as *"a regression, four positive, three negative."* They are one regression, five positive (B–F) and two negative (G, H), and only the two negatives halt.** The same 1/4/3 split appears in `lpc_Decision_Log.md`, which is evidently where the brief took it from — a small live demonstration of a miscount travelling from the build record into the document that commissions its review. Recorded as **C2**.

2. **The brief states that all four of Round 5's named remedies "were attempted" and asks whether they landed. Three landed. The seven-review-history-sites remedy landed at the seven sites and nowhere else** — which is the fourth consecutive round in which a fix has been applied to the quoted sites rather than to the class, and which Round 5's own fix instruction explicitly told the fix pass how to avoid.

3. **The brief's framing of the notice-stripper question — *"The failure that motivated the last guard was a malformed notice eating source between terminators"* — is accurate, and pointing me at it was the right instinct: it is where I found M2.** But the brief, like the Index, treats that guard as having closed the class. It has not.

Otherwise the brief's ordering of risk was good, and two of its instructions did real work: *"Check all three files"* is what turned the review-history question into a structural sweep rather than a site list, and *"Reproduce all eight"* is what separated the three controls that are narrower than advertised from the five that are exactly as advertised.

---

## The cross-thread matter, verified independently and reported as an observation only

**Confirmed. Commit `a6c48e26` made four citations false on this branch, and I did not edit them.**

That commit — *"Fix stale `Build/Ministry/Technology` citations to `Build/reference/method/` (path rename in #204)"*, from another session — rewrote one citation each in `Doc07_Round1_Review.md`, `Doc07_Round2_Review.md`, `Doc08_Round2_Review.md` and `Doc08_Round4_Review.md`, changing `Build/Ministry/Technology/CiC_World_Build_Completion_Standard_V1.3.md` and `Build/Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_3.md` to `Build/reference/method/…`.

Checked three ways:

```
ls reference/                 → No such file or directory
ls Build/reference/method/          → No such file or directory
git ls-files 'reference/*'    → (nothing)
ls Build/Ministry/Technology/       → 16 files + 4 dirs, incl. both cited files
git ls-files Build/Ministry/Technology → 16+ tracked files, incl. both cited files
git ls-tree -d main, origin/main, don-lpc, lpc-own, lpc-src,
   origin/claude/record-native-world-build-v2-yq11wl
                              → every branch has Ministry, none has reference
```

**No branch reachable from this working copy contains `Build/reference/method/`.** Whatever PR #204 renamed has not landed anywhere this branch can see. The four artifacts now cite a path that does not exist, and the paths they previously cited do.

**Scope, stated precisely because it bears on how urgent this is.** All four affected files are **review artifacts**, not deliverables. **None of the three deliverables under review cites either path.** Doc_08 refers to `CiC_Record_Native_World_Build_Process_V1_3.md` by bare filename with no directory, at line 470 — so the deliverables are unaffected either way. The damage is confined to the Method/sources sections of four historical review records, where it makes a verification claim unreproducible: a reader following `Build/reference/method/CiC_World_Build_Completion_Standard_V1.3.md` §F finds nothing.

Reported, not fixed, per instruction. The remedy is a decision for whoever owns the rename: either land #204 on this branch, or revert `a6c48e26` here.

---

## What I tested hardest, and what would change my verdict

**Tested hardest:** the eight advertised controls, all reproduced rather than sampled, then attacked for coverage rather than for existence — which is where three of the four MEDIUMs came from; the Layer-2 presence check, in three directions; the round-count assertion, with five mutants; `verdict_counts`, with five synthetic artifacts; and the review-history question, swept structurally rather than by phrase and confirmed four ways including by git.

**Lightest touch, disclosed:** quotation fidelity, spot-checked at four of the eleven per the brief's instruction, with the time spent on Job 2. Rounds 4 and 5 verified all eleven by both methods and I found no reason to doubt that.

**What would change this verdict to CLEARED or MINOR REVISION:**

1. **H1's two words**, plus the structural — not phrasal — widening of the assertion in **M3**, verified against the five mutants listed there and against the two live sentences.
2. **M1's one function call**, with the three mutants re-run.
3. **(G) and (H) restated in the Index to name what they cover**, and then widened. Restating alone is enough to clear the overstatement; widening is what closes the class.
4. **M4's verdict word and fix-pass ordinal derived or removed**, so the "counted, not typed" line is true of the whole line.

L1–L4 and the cosmetics would not hold up a clearance. If items 1–4 come back done, I would expect the next read to be confirmatory and short, and I would expect it to be the last.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**1 HIGH, 4 MEDIUM, 4 LOW, 2 COSMETIC.**

**The forces analysis is adequate to proceed to Doc_09 and I say so without qualification.** The HIGH and all four MEDIUMs are against the certification apparatus and the newly-committed generator, not against the analysis. **This is the second consecutive round in which no HIGH touches the forces content, and the first in which the generator has been reviewed as a deliverable in its own right.**

*Simulated review — informational only, not an Article 31 substitute.*

*End of Round 6 review.*
