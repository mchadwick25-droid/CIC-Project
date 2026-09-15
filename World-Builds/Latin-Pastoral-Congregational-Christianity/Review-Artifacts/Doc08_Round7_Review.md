# Doc_08 — Forces Document, `lpc_Force_Index.md`, and `scripts/gen_force_index.py`: Latin Pastoral-Congregational Christianity
## Round 7 Confirmatory Read — the generator's guards, reproduced and attacked

**Reviewer:** independent adversarial pass, no authorship of the material under review.
**Date:** 2026-09-15.
**Deliverables reviewed:** `Doc_08_Forces_Document.md` (474 lines), `lpc_Force_Index.md` (162 lines), `scripts/gen_force_index.py` (716 lines) — all three REVISED after Round 6 at commit `66e1488b` and unreviewed.
**Prior rounds:** Round 1 (4H 5M 3L 1C), Round 2 (3H 4M 3L 1C), Round 3 (4H 5M 4L 2C), Round 4 (3H 3M 5L 1C), Round 5 (2H 3M 3L 2C), Round 6 (1H 4M 4L 2C) — all SUBSTANTIAL REVISION REQUIRED. Each round's counts read off its own file at its own VERDICT heading, not off the Index's derived line (see **Checks I confirmed**). *The literal string is deliberately not written with its hash marks here, and* **M1** *says why.*
**Scope:** confirmatory, as Round 6 recommended. I did not re-review the forces analysis and nothing I found required me to.

*Simulated review — informational only, not an Article 31 substitute.*

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH, 5 MEDIUM, 5 LOW, 1 COSMETIC.**

**Said plainly, and the shape of it matters more than the count.**

- **The forces analysis is sound and clear to proceed to Doc_09. I add no qualification to Round 6's judgement and I did not spend this round re-litigating it.** Nothing I found touches the analysis. Third consecutive round with no HIGH against it.
- **Round 6's H1 is closed, properly and structurally.** Every review-status claim in Doc_08 now reads *six*, and I confirmed it with a phrase-independent sweep rather than by checking the two sentences Round 6 quoted. **M1 is closed in both directions. M2 is closed — I re-ran Round 6's exact defeating placement and it now halts. L1's first limb, L2, L3's main limb are closed. M3 is closed for three of its five named mutants.**
- **But I got a false force-gravity connection into the emitted Index with every guard clean, exit 0** — by writing a correction notice with a tag the stripper does not know. The tag I used, `[CORRECTION, …]`, is in live use **in this same world build**, in `Doc_05_Ecological_Reconstruction.md`. The control named *"(F) Unknown notice syntax"* tests a **known** syntax variant; the genuinely unknown ones walk straight through, and the coverage assertion that claims to catch them is circular — it defines "notice" with the same regex it is checking. That is Round 4's H1 class, reopened. **HIGH-1.**
- **And I got a false review-status claim into the emitted Index with no guard firing** — a `CLEARED` round rendered as `SUBSTANTIAL REVISION REQUIRED`, in the **Disposition**, from a hard-coded literal. Round 6's M4(b) named **two** verdict literals. The fix pass removed one. The surviving one is one round from firing — **this round, if this pair is ever cleared** — and the same rewrite left a **raw Python tuple visible in the committed Index today**: `(('1H 4M 4L 2C', 'SUBSTANTIAL REVISION REQUIRED'), SUBSTANTIAL REVISION REQUIRED)`. The Decision Log and Index §6 both state this defect is closed. **HIGH-2.**
- **Round 6's carried sentence held up under test and I am carrying it again:** *a control stated more broadly than it is implemented is worse than no control, because the next round will trust it.* Three more instances below — control (F)'s title, control (H)'s *"every claim form is matched,"* and control (G)'s *"emphasis-dense span"* test, which does not exist in the code at all.

**The distance to clearance is short and it is entirely mechanical:** one line in the Disposition render, one widened tag pattern plus one genuinely non-circular coverage assertion, and four wording narrowings. **No analysis work is outstanding.** But two HIGHs genuinely survive, and one of them is a live malformed artifact in the delivered file, so this is SUBSTANTIAL REVISION REQUIRED and not MINOR REVISION. **Six prior rounds of this verdict is a reason to have been more careful about grading, not a reason to reach for a seventh — so every finding below names the mutation, the exit code and the emitted line, and I say where I nearly got it wrong.**

---

## Method — what I actually ran

**An isolated mutation sandbox, so that no deliverable was touched.** I copied Doc_08, the Index, the six review artifacts and the generator into a scratch tree and drove the generator through its documented `argv[1]` base override. The sandbox reproduces the committed Index **byte-identically** (`md5 834054078c909f6764e3346b9d04bbdd`) before any mutation, which is what makes every later diff attributable. `git status` on the world directory is clean at the end of this review; I modified nothing.

**Portability and reproducibility, tested first.** Run from `/` against the real world directory, the committed generator reproduces the committed `lpc_Force_Index.md` **byte-for-byte**. `BASE` resolves from `__file__`; there is no session path in the file. The regeneration command is now recorded at Index line 144 and the file is mode `755`.

**All nine advertised controls reproduced, none sampled** — table under *Job 2*. Then **twenty-three mutations** beyond them, in five families: notice syntax and placement, review-history claim forms, verdict and fix-pass ordinals, count-bearing tables, and cell/ID filing. Two brute-force searches over insertion points rather than hand-chosen sites.

**Static reading as a second channel.** An AST pass over the generator for values computed and never rendered (none — see *the third defect*), a `git show 0e70a96a` diff of `verdict_counts` to establish when its contract changed, and a corpus-wide census of provenance-tag vocabularies across `World-Builds/`.

**Governing documents consulted:** the Forces Framework plain text (the *"This is not optional. All three layers are required for every force"* passage verified at line 141), the Constitution Articles named in the brief, `CLAUDE.md`, the record-native build process, and `lpc_Decision_Log.md` entries for Rounds 5 and 6.

---

## Job 1 — Round 6's eleven findings, closure status at the live text

| # | Round 6 finding | Status |
|---|---|---|
| **H1** | Two false review-status statements in Doc_08's Disposition | **CLOSED.** Both sentences now read *six*. Confirmed by a phrase-independent structural sweep — every numeral-or-number-word within 60 characters of *round/review/times/fix pass*, notices stripped first — which finds **no** remaining false claim. Doc_08's masthead, §9, Document Log and Disposition all agree on six, and six artifacts exist on disk. |
| **M1** | Layer-2 extract not stripping notices | **CLOSED, both directions.** `raw = strip_notices(m3.group(1))` is in place. Mutant A (1A-1's Layer 2 replaced by a long notice) now prints **STUB** and *"Every force carries a written Layer 2 — **NO** — 1 missing"*. Mutant B (real Layer 2 plus a notice quoting *"left unfilled"*) now prints **✓** — the false failure is gone. |
| **M2** | Over-consumption guard defeated by moving the malformed notice after `Connected forces:` | **CLOSED.** I re-ran **both** of Round 6's placements verbatim. Before `Connected forces:` → `FATAL`. After `Connected forces:` → `FATAL`. The new signature (*the span contains the next notice's opener*) is the right property and it fires. My own brute-force search over every realistic insertion point in the document found **one** surviving site, at §8 line 387, which consumes only prose no derivation reads. See **M5** for what is nonetheless overstated about it. |
| **M3** | Round-count assertion much narrower than stated | **PARTLY CLOSED — three of five mutants fixed.** Masthead rewritten to *"REVISED after Round 2 … **Two** independent adversarial review rounds"* → now `FATAL`, and it names **both** false claims. Lowercase *"two independent adversarial review rounds"* → now `FATAL`. Bold no longer defeats the match. **Still passing:** Round 6's Document-Log-rows-deleted mutant, and the ordinal/cardinal conflation. Plus two new bypasses. See **M2** below. |
| **M4** | `verdict_counts` window; hard-coded verdict; `LATEST` | **NOT CLOSED, in all three limbs.** (a) the recital still wins inside the new heading-bounded window — **M1** below; (b) one of the two hard-coded verdict literals removed, the other left in the Disposition — **HIGH-2**; (c) `LATEST` untouched — **M3** below. |
| **L1** | Force under the wrong `### CELL` heading | **FIRST LIMB CLOSED.** Round 6's exact mutation now halts: `FATAL: force(s) filed under a cell heading their ID contradicts`. **Second limb not done** — §9's hand-typed cell distribution is still read by nothing (**L2** below). |
| **L2** | Index §6 said *"Four checks"* and enumerated eight | **CLOSED as to the number, reopened as to the shape.** It now says **nine** and enumerates nine. The 1/6/2 split it states is wrong — see **L1** below. |
| **L3** | Regeneration command recorded nowhere; `argv[1]` unguarded; not executable | **TWO OF THREE.** Command recorded at Index line 144. File is `755`. `python3 scripts/gen_force_index.py --help` still dies in a raw `FileNotFoundError` traceback on `/--help/Doc_08_Forces_Document.md`. Fails safe; nothing written. |
| **L4** | Index-generator portfolio item recorded as *"carried at the Disposition"* and not there | **NOT CLOSED, at either end.** `lpc_Decision_Log.md` line 1269 still says *"Carried at the Disposition; not decided here."* Doc_08's CO-022 assessment still reads *"Portfolio-level or cross-world: **four items**"* and the strings *index generators are build artifacts* and *diffed before commit* appear nowhere in Doc_08. Unchanged since Round 6. |
| **C1** | 2×7 quotation trimmed without marking at both sites | **NOT CLOSED.** Doc_08 line 334 still reads *"…not 2's own continuation)"* and line 161 *"…not 2's own continuation."*; Doc_04 line 195 reads *"…not 2's own continuation **— see §3, §5**)"*. No ellipsis at either site. The Decision Log nonetheless records *"**C1, C2** applied"* — **L4** below. |
| **C2** | Control inventory miscounted as *"a regression, four positive, three negative"* | **CORRECTED TO A NEW WRONG SHAPE.** Now *"one regression, six positive, two negative"* in both the Index and the Decision Log. Correct is **1 / 5 / 3**. See **L1**. |

**Seven closed, one closed in part, three not closed.** The three not closed (M4, L4, C1) are the three that no reviewer had to re-quote — and the pattern Round 6 named four times over, *the fix lands where a reviewer pointed*, is visible once more in **M4(b)**: the finding named two literals, the fix pass removed the one the finding quoted in full.

---

## HIGH

### H1 — A correction notice written with a tag the stripper does not know is read as derivation input, and puts a false force-gravity connection into the emitted Index with every guard clean. The tag I used is in live use in this same world build. The control that advertises this class is called *"Unknown notice syntax"* and tests a known one.

**Site.** `scripts/gen_force_index.py` lines 30–37 (`TAGS`, `_OPEN`, `NOTICE`, `OPENER`) and lines 53–83 (`assert_notice_coverage`); `lpc_Force_Index.md` §6, controls **(C)** and **(F)**; `Doc_08_Forces_Document.md` Document Log row *"notices stripped before all derivation"* and the co-produced-output paragraph at line 12.

**What I found.** The stripper's tag vocabulary is a five-item closed list compiled **without** `re.IGNORECASE`:

```python
TAGS = r"CORRECTED|ADDED|MOVED HERE|MOVED|REVISED"
_OPEN = r"\[(?:" + TAGS + r")(?=,|\s*[—-])"
NOTICE = re.compile(r"\*{0,2}" + _OPEN + r".*?\]\*\*", re.S)
OPENER = re.compile(_OPEN)
```

`assert_notice_coverage` then closes with:

```python
left = OPENER.findall(strip_notices(t))
if left:
    sys.exit(f"FATAL: {len(left)} notice opener(s) survive stripping in {label} … "
             "A notice the stripper cannot see is derivation input. Refusing to emit.")
```

**That assertion cannot do what its own message says.** `OPENER` and `NOTICE` are built from the same `_OPEN` string. A notice the stripper cannot see is, by construction, also a notice `OPENER` cannot see. The check is circular: it can only detect notices it already knows how to strip. The generator's header comment claims the opposite — *"coverage is ASSERTED below rather than assumed."*

**Three mutants, each a single realistic notice on §5's G6 line, each successful.**

| Mutant planted on the G6 line | Exit | Emitted Index |
|---|---|---|
| `**[CORRECTION, 2026-09-15 — Round 6's review noted this list previously omitted **3A-1**; restored here.]**` | **0** | `G6` row: `2A-3`, `2B-1`, `2B-4`, **`3A-1`** — 4. `3A-1`'s master row: Connected Gravities **`G1, G6`** |
| `**[SUPERSEDED, 2026-09-15 — this list previously omitted **3A-1**.]**` | **0** | identical |
| `**[Added, 2026-09-15 — …]**` (title case, tag otherwise known) | **0** | identical |

A fourth, `**[ADDED 2026-09-15 — …]**` (the comma after the tag omitted), also emits cleanly. The comma/dash lookahead was added by the Round 6 fix pass to stop the detector firing on §8's prose *mention* of `[ADDED …]`; it is the right idea and it narrowed the opener at the same time.

**No guard fires, and the one trace is affirmatively labelled harmless.** All three hard guards pass (17 forces, 8 gravities, 15 connections). Control (C) passes — the tag is not `CORRECTED`. Control (F) passes — the form is not `**Heading. [ADDED …]**`. The §3/§5 reconciliation prints **no contradiction**; it prints a sixth **Observation** row, under the heading *"Observations — **not defects**,"* among five genuine ones, reading *"`3A-1` | G6 | §5's list carries it; §3's Layer 3 does not assert it in a connection sentence."* A reader is told the anomaly is expected asymmetry.

**This is not a hypothetical tag.** A census of `**[TAG,` forms across `World-Builds/` returns, besides the five the generator knows: **`CORRECTION` — 17 occurrences**, `SUPERSEDED` — 4, `FURTHER CORRECTION` — 3, plus `MODERATE`, `LOW`, `SUBSTANTIAL`, `COSMETIC`, `MEDIUM`. `**[CORRECTION, 2026-09-14 — Round 1's H1.]` and `**[CORRECTION, 2026-09-14 — Round 1's M1.]` are live in **this world's own `Doc_05_Ecological_Reconstruction.md`**; `**[FURTHER CORRECTION, Round 9.]` is live in `lpc_Decision_Log.md`. `CORRECTION` is used more often across the portfolio than `ADDED`, which the generator does know.

**The live document is clean and I say so.** Doc_08 today carries exactly 43 notices — 31 `CORRECTED`, 9 `ADDED`, 2 `REVISED`, 1 `MOVED HERE` — every one matched and stripped, and the only two unmatched openers are the §8 prose mentions, correctly excluded. **There is no wrong value in the delivered Index.** The defect is in the breadth of the guarantee, not in the current text.

**Why this matters.** Round 4's H1 — a correction notice read as derivation input, the delivered Index contradicting its own source with every control clean — was the most consequential defect in four rounds. The remedy was this stripper plus this assertion, and both deliverables now rest their integrity claim on it: Doc_08's Document Log records *"notices stripped before all derivation"* as the Round 4 fix; the Index advertises (C) and (F). **The class is closed only for the five tags someone happened to list.** Every fix pass in this build writes new notices; six of them have. The next one that reaches for the house tag one document over reopens a HIGH silently, and the Index will print an Observation row explaining it away.

**Why HIGH rather than MEDIUM.** Round 6 graded M2 MEDIUM on the reasoning that the reconciliation control still fired and printed contradiction rows, so the wrong Index was not silent. Here **no** control fires; the only output is a row labelled *not a defect*. And unlike M2 — a guard defeated by placement — this is a guard that is **definitionally incapable** of the thing its own error message promises. That is the Round 4 H1 class with a closure claim on top of it.

**Fix.**
1. Widen `TAGS` to the vocabulary actually in use (`CORRECTION`, `FURTHER CORRECTION`, `SUPERSEDED` at minimum) and compile `NOTICE`/`OPENER` with `re.IGNORECASE`.
2. **Then make the coverage assertion non-circular, because widening a list is not closing a class.** Assert on a pattern the stripper does *not* use: any `**[` followed by an ALL-CAPS or Capitalised word of 3–25 characters and then a comma or dash, anywhere in derivation input, that is not inside a span `strip_notices` removed → `FATAL: unrecognised provenance-notice syntax`. That fires on a new tag the first time it is written, which is the only moment it is cheap to fix.
3. Narrow **(F)** in the Index. Its title claims the class; call it *"a notice in the `**Heading. [ADDED …]**` form is stripped"* and add a line saying the tag vocabulary is a closed list and what closes it.

### H2 — The Disposition still hard-codes the verdict word. A `CLEARED` round renders as `SUBSTANTIAL REVISION REQUIRED`, in the section disposition is decided from. The same rewrite left a raw Python tuple in the committed Index, and the Decision Log records the defect as closed.

**Site.** `scripts/gen_force_index.py` line 710 (the Disposition render) against lines 148–177 (`verdict_counts`, `VERDICT_LINE`); `lpc_Force_Index.md` line 162; `lpc_Decision_Log.md` line ~1287; Index §6's controls-restatement paragraph.

**What I found, and the first half needs no test at all — it is in the delivered file.** `lpc_Force_Index.md` line 162, as committed:

> **Not disposed.** Reviewed and disposed of together with `Doc_08_Forces_Document.md`. **Six independent round(s) have been run**, the most recent `Review-Artifacts/Doc08_Round6_Review.md` **(('1H 4M 4L 2C', 'SUBSTANTIAL REVISION REQUIRED'), SUBSTANTIAL REVISION REQUIRED)**; this file is the Round 6 fix pass and is **unreviewed**.

That is a Python 2-tuple repr, in the Disposition of a delivered construction document, in a file whose header says *"Generated from `Doc_08_Forces_Document.md` by `gen_force_index.py`. Never hand-edited."*

**The cause is a contract change applied at one call site and not the other.** `git show 0e70a96a` shows `verdict_counts` previously returned a string. The Round 6 fix pass changed it to return `(counts, verdict)` and updated the `_VC` comprehension — but line 710 still calls `verdict_counts(ROUNDS[-1][1])` and interpolates the whole tuple, **and still appends the literal** `, SUBSTANTIAL REVISION REQUIRED)` beside it.

**Round 6's M4(b) named both literals.** Its text: *"The Index then hard-codes — **all SUBSTANTIAL REVISION REQUIRED** and ({counts}, SUBSTANTIAL REVISION REQUIRED)."* The first is fixed: `VERDICT_LINE` now reads each artifact's verdict and degrades to a per-round list when they differ. **The second is untouched.**

**Demonstrated, not inferred.** I built a synthetic `Doc08_Round7_Review.md` with `## VERDICT: CLEARED` and `0 HIGH, 0 MEDIUM, 2 LOW, 1 COSMETIC`, and updated Doc_08's review claims to seven so the round-count assertion would let the generator run. Exit 0. The emitted Index:

> **Review history …:** … Round 7 (0H 0M 2L 1C) — verdicts: Round 1: SUBSTANTIAL REVISION REQUIRED; … **Round 7: CLEARED**
>
> **Not disposed.** … the most recent `Review-Artifacts/Doc08_Round7_Review.md` **(('0H 0M 2L 1C', 'CLEARED'), SUBSTANTIAL REVISION REQUIRED)**; this file is the Round 7 fix pass …

**The same file states the verdict correctly in one line and falsely in another, twenty lines apart, and prints the true value inside the parentheses that precede the false one.**

**And the build record certifies the opposite.** `lpc_Decision_Log.md`, Round 6 fix-pass entry: *"The verdict **word** was also hard-coded as 'all SUBSTANTIAL REVISION REQUIRED'; **it is now read from each artifact, so a CLEARED round cannot be reported as a revision round by a literal nobody remembered to change.**"* That sentence is false, and a literal nobody remembered to change is exactly what produced the counter-example.

**Why this matters.** Constitution Article 30 and CO-022 make disposition turn on review status, and the Disposition section is the one place that decision is read from. Round 6's H1 — false review-status statements in Doc_08's Disposition — was graded HIGH for precisely this reason. This is the same class, in the paired file's Disposition, one round later, with a closure claim attached. It is latent by exactly one round: **it fires the moment this pair is cleared**, which is the trajectory 4 → 3 → 4 → 3 → 2 → 1 points at. And the tuple repr is not latent at all.

**Fix.**
1. Line 710: unpack. `_c, _v = _VC[LATEST]` and render `({_c}, {_v})`. Do not call `verdict_counts` a second time at render — `_VC` already holds it.
2. Sweep the render block for every remaining verdict, count or round literal and derive or delete each one. Two minutes; do it as a class, not at the site this finding quotes.
3. Correct the Decision Log's Round 6 entry, which currently credits a fix that was half applied.

---

## MEDIUM

### M1 — `verdict_counts` still returns a predecessor's counts when the recital sits inside the verdict section, and its anchor is a substring search that any artifact mentioning the heading disables. The Round 6 fix moved the bug a second time and Index §6 states it as fixed.

**Site.** `gen_force_index.py` lines 148–170; `lpc_Force_Index.md` §6, the (D)-sibling paragraph.

Round 6 diagnosed the mechanism exactly: *"`re.search` takes the first match in the window whatever it belongs to; nothing ties the match to the artifact's own verdict."* The fix changed the **window bound** — from 1200 characters to the next `^#{2,3} ` heading — and left the selection rule alone. The Index now asserts: *"The window now ends at the next heading — a structural bound rather than a number chosen by eye."*

**A recital inside the verdict section still wins.** Synthetic Round 7 artifact:

```
## VERDICT: SUBSTANTIAL REVISION REQUIRED

Round 6 returned 1 HIGH, 4 MEDIUM, 4 LOW, 2 COSMETIC and all of it is closed.
This round finds 3 HIGH, 2 MEDIUM, 1 LOW, 0 COSMETIC.

## Method
```

Emitted: *"… Round 6 (1H 4M 4L 2C); **Round 7 (1H 4M 4L 2C)**"*. The predecessor's counts under the successor's label, in the line whose entire purpose is that it cannot go wrong — **which is verbatim the result Round 6 reported, after the fix intended to prevent it.**

**It works today by formatting convention, not by construction.** All six artifacts happen to state their own counts on the first non-blank line after the heading. Round 5's and Round 6's verdict sections both discuss prior rounds; neither happens to use the `N HIGH, N MEDIUM…` form before its own. That is luck, and the convention is not written down anywhere.

**Why this matters.** Third consecutive fix at one site that relocates the defect. The Index's claim is not hedged, so the next round will trust it.

**A second, sharper instance of the same defect, which I found by committing it.** The anchor is `t.find("## VERDICT")` — the **first textual occurrence** of that string anywhere in the file, not the first *heading*. **My own draft of this review mentioned the heading by name, in backticks, in its masthead — six lines above its real heading — and the generator's parser then returned `counts not parsed` and `verdict not parsed` for Round 7.** I re-worded my masthead rather than leave a trap in the build record, but the point stands and it is not hypothetical: **a review artifact is exactly the kind of file that quotes heading strings**, and three of the six existing artifacts discuss the parser itself. A fenced example or a prose mention silently disables the parse for that round, and the Index then prints `counts not parsed` in the line whose whole claim is that it is derived. Anchor on `re.search(r"^## VERDICT", t, re.M)`, not on `find`.

**Fix.** Take the **first** `N HIGH … N COSMETIC` match in the window **only if** no other such match precedes it in that window; otherwise report `counts ambiguous — N candidates`. Better: require the match to be on the first non-blank, non-heading line, and report `counts not parsed` otherwise. The file already degrades gracefully in two other places; extend the same instinct here.

### M2 — Control (H) is stated as *"every claim form is matched."* It is still a phrase list, and three false review-status claims pass it — including Round 6's own unfixed mutant.

**Site.** `gen_force_index.py` lines 88–140 (`assert_doc08_round_count`); `lpc_Force_Index.md` §6, control **(H)** and the (H) narrative.

The widening is real and I credit it: bold is flattened, matching is case-insensitive, numerals and number-words both parse, and *"REVISED after Round N"* is checked at **every** occurrence rather than by a maximum. Three of Round 6's five mutants now halt, and the FATAL names both false claims rather than the first.

**Three still pass, exit 0.**

| Mutant | Guard | Why |
|---|---|---|
| Document Log's **Round 3 and Round 4 rows deleted** | **passes** | `max(ords)` is still 6; a Log missing two rounds is invisible. **Round 6 reported this mutant; it was not addressed.** |
| Masthead rewritten to *"**Three** rounds of independent adversarial review have been run"* | **passes** | the pattern requires the words `independent adversarial review rounds` in that order. A rephrase is a claim form. |
| Disposition rewritten to *"all six returning **CLEARED**"* | **passes** | verdict **words** in Doc_08 are compared against nothing, though `_VC` holds every artifact's real verdict |

And the ordinal/cardinal conflation Round 6 named is untouched: `NROUNDS = len(ROUNDS)` against `LATEST = ROUNDS[-1][0]`. With `Doc08_Round7_Review.md` present and `Doc08_Round6_Review.md` absent, the Index heads *"REVISED after Round 7"* over *"Six independent round(s) have been run."*

**Why this matters.** Round 5's H1 was accepted on *"A number that is counted cannot be forgotten."* The number is counted; the claims about it are still read by a six-entry phrase list described as exhaustive.

**Fix.** Either state (H) at its real coverage — *"the six claim forms enumerated in the assertion"* — or make it structural: extract every sentence containing a round ordinal or a review-round count, compare each to the counted value, and print all disagreements. Add a verdict comparison: each `Round N (…)` row's verdict word in Doc_08 against `_VC[N][1]`. Add a contiguity check on `ROUNDS` so a gap halts with an accurate reason.

### M3 — `LATEST` still conflates *latest artifact* with *latest fix pass*, in the three sentences that assert what this file **is**. Round 6's M4(c), untouched.

**Site.** `gen_force_index.py` line 145, rendered at lines 514, 516 and 710.

`LATEST = ROUNDS[-1][0]` — the highest **review artifact** number — is rendered as the **fix-pass** ordinal in all three of:

> **Status:** **REVISED after Round {LATEST}** …
> **Revised:** 2026-09-15 (Round {LATEST} fix pass)
> this file is the **Round {LATEST} fix pass** and is **unreviewed**

With my synthetic Round 7 artifact on disk and **no Round 7 fix pass performed**, the Index asserts *"REVISED after Round 7"*, *"(Round 7 fix pass)"* and *"this file is the Round 7 fix pass."* All three false, by construction, in the window between a review being filed and its fix pass being applied. Round 6 ran this probe and reported it; nothing changed.

**Why this matters.** These are the Index's own statements about its review status, and they are the lines a project lead reads first. Round 6's fix instruction was explicit — *"Separate `LATEST_REVIEW` from `LATEST_FIX_PASS`"* — and no such separation exists in the file.

**Fix.** Take the fix-pass ordinal from Doc_08's Document Log (`Round (\d+) fix pass` rows), keep `LATEST_REVIEW` from the artifacts, and render *"reviewed through Round N; this file is the Round M fix pass"* when they differ. Note this also removes the coupling that makes the round-count halt (below) look like a defect.

### M4 — The §4 connection count has no guard. One de-bolded force ID silently drops a cross-cell connection, and the Index prints a count that contradicts Doc_08 §9's certification.

**Site.** `gen_force_index.py` lines 441–448 (`ROW_RE`, `conns`) and line 608; `Doc_08_Forces_Document.md` §9 (*"Cross-cell connections documented in Section 4 — fifteen"*).

Three hard guards exist: 17 forces, 8 gravities, and *"§5 names force X, which §3 does not define."* **There is no guard on `len(conns)`.** `ROW_RE` requires the source ID bolded: `^\|\s*\*\*(\d[AB]-\d)\*\*\s*\|`.

I removed the bold from **one** ID in §4 — `| 1B-1 |` instead of `| **1B-1** |`, a single formatting slip of exactly the kind this build has hit repeatedly:

```
exit 0
wrote … (17 forces, 14 connections, 8 gravities)
Index §4 summary: **14 connections**, including 1 deliberate non-connection (`2A-2`) …
Index §1: `1B-1`'s row loses "→ 2B-4"; `2B-4`'s row loses "← 1B-1"
Doc_08 §9: "Cross-cell connections documented in Section 4 — fifteen"
```

No guard, no contradiction, no observation. The §3-vs-§4 cross-check (control E) cannot see it: the missing pair only makes the table *smaller*, and E fires on Layer-3 claims §4 does not carry — 1B-1's Layer 3 makes no such claim about 2B-4.

**Why this matters.** *"A silently short index is the failure mode this guard exists for"* is the generator's own comment on the 8-gravity assertion. The §4 table is the third countable relation and the only one without the assertion. Doc_08 §9 certifies the number by hand, so the deliverable pair can disagree about it with every control clean — and the Index, being derived, will look like the authority.

**Fix.** `if len(conns) != 15: sys.exit(...)`, in the same form as the other two. Better, and it closes **L2** as well: read §9's certification line (*"— fifteen"*, and the `1A (n), 1B (n) …` distribution) and compare it to the derived values, printing disagreements the way §7's cross-check does.

### M5 — Two tests are described that do not exist: the Index says (G) halts on an *"emphasis-dense"* span, and the code comment says `STRUCTURAL` carries *"the force-ID pattern."* Neither is in the file.

**Site.** `lpc_Force_Index.md` line 142; `gen_force_index.py` lines 47–51.

The Index's account of the (G) rewrite:

> **(G)** … — it now also halts on an implausibly long or **emphasis-dense** span, which is what over-consumption actually looks like.

The comment above `STRUCTURAL`:

> Any marker a notice must not swallow, **plus the force-ID pattern**: a notice that contains several force IDs is almost certainly eating a gravity list.

```python
STRUCTURAL = re.compile(
    r"Connected forces:|^\*\*G\d — |^\#{2,4} |^\*\*Layer [123] |^\| ", re.M)
…
swallowed = len(OPENER.findall(span)) > 1
if swallowed or STRUCTURAL.search(span) or len(span) > 3000:
```

There is **no** emphasis-density measure and **no** force-ID alternative. The implemented tests are: a second opener inside the span, a structural marker, and a 3000-character ceiling. Both descriptions come from Round 6's *proposed* fix (*"a force-ID token, a gravity token, or more than one `**…**` span it did not open"*); the implementer chose the opener test instead — which is the better test — and the prose kept describing the version that was not built.

**Why this matters.** It is the carried sentence in its purest form, and it is load-bearing: a reader of §6 concludes that a runaway notice is caught by three independent properties when it is caught by one, plus two backstops. My own brute-force search found the opener test carries essentially all of the weight — the 3000-character ceiling never fires on anything realistic, and `STRUCTURAL` is what fires only when the span crosses a line.

**Fix.** Delete *"or emphasis-dense"* from the Index and *"plus the force-ID pattern"* from the comment, or implement them. Say what (G) actually keys on: *"a notice span that contains a second notice's opener — the signature of a match that ran past its own terminator."* That is a better claim than the one being made.

---

## LOW

### L1 — The control inventory is miscounted again, in the paragraph that announces the correction. (I) halts; the paragraph says two controls halt and then describes three.

**Site.** `lpc_Force_Index.md` line 140; `lpc_Decision_Log.md` line 1291; and the brief for this round.

> There are **nine**: one regression, **six positive controls, and two negative controls that halt the generator**. *(An earlier version of this paragraph … said "a regression, four positive, three negative." The miscount is corrected here.)*
>
> … **(G)** … **halts the generator**. **(H)** … **halts the generator**. **(I) Cell/ID agreement** — a force filed under a `### CELL` heading its own ID contradicts **halts the generator**.

Nine is right. The split is not: three of the nine halt, so it is **one regression, five positive (B–F), three negative (G, H, I)**. I reproduced (I) and it exits 1 with `FATAL: force(s) filed under a cell heading their ID contradicts`. The Decision Log repeats the 1/6/2 split at line 1291, and **the brief that commissioned this review reproduces it as *"six positive (B–F, I), two negative that halt it (G, H)"*** — the same miscount travelling from the build record into the commissioning brief, for the second round running. Round 6 flagged that exact propagation path as C2.

**Fix.** *"one regression, five positive, and three negative controls that halt the generator."* Better: render the split from the lettered entries so it cannot go stale a third time.

### L2 — Doc_08 §9's hand-typed cell distribution is still read by nothing. Round 6's L1 had two limbs; one was built.

**Site.** `Doc_08_Forces_Document.md` line 421; `gen_force_index.py` (absent).

I rewrote §9's certification to *"1A (5), 1B (1), 2A (4), 2B (5), 3A (1), 3B (1) = **17 forces**"* — flatly contradicting the document's own matrix — and regenerated. Exit 0, no output of any kind. The Index prints the correct derived distribution beside a §9 that asserts a different one.

The first limb (ID-versus-heading) is built and works. The second — *"read §9's `1A (n), 1B (n), …` line and compare it to the derived counts, in the same spirit as the §7 cross-check"* — is the one that closes the general hole, and §9 remains the one place Doc_08 restates a derived relation by hand without a cross-check. §3's gravity prose and §7's confidence list both have one.

**Fix.** Four lines, in the §7 cross-check's idiom: parse the distribution, compare, print disagreements rather than resolving them. Fold in the *"fifteen"* connection count (**M4**) at the same time.

### L3 — Round 6's L4 is untouched at both ends. The Decision Log still records an escalation the deliverable still does not carry.

**Site.** `lpc_Decision_Log.md` line 1269; `Doc_08_Forces_Document.md` CO-022 assessment.

Line 1269 still reads *"**One portfolio item added, at Round 5's recommendation:** index generators are build artifacts and belong in the repository … **Carried at the Disposition;** not decided here."* Doc_08's CO-022 assessment still reads *"Portfolio-level or cross-world: **four items**, none decided here"* and lists the same four. Neither of the two remedies Round 6 offered was taken. The item is a good one and this is the only world of twelve whose index deliverable is produced by a build-authored generator, so it is worth carrying properly rather than losing twice. I restate it in my own CO-022 assessment below so it survives a third round.

**Fix.** Add it as the fifth portfolio item, or correct the Decision Log to say it was recommended and not carried.

### L4 — The Decision Log's Round 6 entry records work that was not done, in two places.

**Site.** `lpc_Decision_Log.md`, Round 6 fix-pass entry.

Two claims in that entry are false against the live files:

- *"**C1, C2** applied."* **C1 was not applied** — the 2×7 quotation is still closed where Doc_04 continues, at both sites (see **Cosmetic C1**).
- *"The verdict word … **is now read from each artifact, so a CLEARED round cannot be reported as a revision round by a literal nobody remembered to change.**"* Disproved at **H2**.

This build's own Decision Log names this failure mode at line 1003, about a different document: *"**a prior review credited with work it did not do** … Crediting a prior review with work it did not perform is self-certification wearing someone else's name — one of the four failure modes CO-022 was written to close."* The same shape, one fix pass crediting itself.

**Fix.** Correct both sentences. A fix-pass entry that overstates is how the next round's brief acquires a false premise — which is how this round's brief acquired **L1**.

### L5 — Two robustness residues in the generator: the `argv[1]` override is still unguarded, and `ROUNDS[-1]` is unguarded where `LATEST` is guarded.

**Site.** `gen_force_index.py` lines 20, 145, 710.

- `python3 scripts/gen_force_index.py --help` resolves `BASE` to `/--help` and dies in a raw `FileNotFoundError` traceback. Fails safe — nothing written — but an undocumented positional override indistinguishable from a mistyped flag is a small trap, and Round 6 asked for it.
- `LATEST = ROUNDS[-1][0] if ROUNDS else 0` is carefully guarded; line 710's `verdict_counts(ROUNDS[-1][1])` is not. With an empty `Review-Artifacts/` the run dies in `IndexError: list index out of range` **after** all parsing and all guards have passed — I hit this on my first attempt at the (A) regression, before copying the artifacts in. Same line as **H2**; fixing that one fixes this.

**Fix.** A named `--base` flag with an `argparse` error, or an `if not SRC.exists(): sys.exit(...)` with a readable message. Guard `ROUNDS[-1]` the way `LATEST` is guarded.

---

## COSMETIC

### C1 — Round 6's C1 is open. The 2×7 quotation is still trimmed without marking, at both sites, and the Decision Log records it as applied.

`Doc_08_Forces_Document.md` line 334 (§5) and line 161 (§3) quote Doc_04 §6's 2×7 cell as ending *"…not 2's own continuation)"* / *"…not 2's own continuation."*; `Doc_04_Gravity_Discovery.md` line 195 reads *"…not 2's own continuation **— see §3, §5**)"*. Nothing material turns on the dropped cross-reference — Doc_08 cites Doc_04 §3 on its own account two clauses later — which is why this stays COSMETIC for a second round. Add `…` before the close at both sites, or quote the tail. See **L4** for the record-keeping half.

---

## Job 2 — the nine controls, reproduced

| Control | Claim in Index §6 | My result |
|---|---|---|
| **(A)** Regression at `9eccc532` | all three §3/§5 divergences Round 1 found by hand | **Exactly those three** — `1B-1`/G2, `2A-1`/G8, `2B-1`/G7 — plus 3 STUB flags (`2B-5`, `3B-1`, `3B-2`). As advertised. |
| **(B)** False denial | §3 claiming §5 does not carry `G6` produces a contradiction row | **2 rows**, `2B-1`/G2 and `2B-1`/G6, *"§3 Layer 3 asserts §5 does NOT carry this; §5's list does carry it."* As advertised. |
| **(C)** Notice injection | a bold force ID planted inside a `[CORRECTED …]` notice does not reach the tables | Planted `**3A-1**` in §5's G6 `[CORRECTED …]` notice: `G6` stays 3 forces, `3A-1` stays `G1`. As advertised — **for that tag.** See **H1.** |
| **(D)** Omitted connection | removing `2B-1` from §5's G6 list while §3 asserts it produces a contradiction row | **1 row**, *"§3 Layer 3 asserts this connection; §5's list omits it."* As advertised. |
| **(E)** Cross-cell | a Layer-3 claim §4's table does not carry produces a §3-vs-§4 row | *"**1 disagreement(s):** `2B-1` names `1B-3`, §4 does not pair them."* As advertised, and the output block Round 6 found deleted is present and live. |
| **(F)** Unknown notice syntax | `**Heading. [ADDED …]**` is stripped and its planted ID does not reach the tables | Form-B notice with `**3A-1**` appended to §5's G7 line: `G7` stays `2A-4`, `3B-1`; `3A-1` stays `G1`. **The stated scenario passes; the stated class does not — H1.** |
| **(G)** Notice over-consumption | a malformed notice missing its terminator halts the generator | **Fires in both of Round 6's placements** — before and after `Connected forces:`. Brute-forced every realistic insertion point: one survivor, in §8 prose no derivation reads. **Stated too broadly in the narrative — M5.** |
| **(H)** Review history | a Doc_08 whose round claims disagree with `Review-Artifacts/` halts the generator | Fires on the masthead, the Status line, lowercase and numerals. **Three false claims still pass — M2.** |
| **(I)** Cell/ID agreement | a force filed under a `### CELL` heading its own ID contradicts halts the generator | `FATAL: force(s) filed under a cell heading their ID contradicts: 2A-2 under CELL 1B …` **Fires. And it halts, which makes the inventory's 1/6/2 split wrong — L1.** |

**All three hard guards re-confirmed.** Deleting a `#### Force` heading → `FATAL: parsed 16 forces, expected 17`. Breaking a §5 gravity heading → `FATAL: parsed 7 gravities … expected 8`. **And one countable relation has no guard at all — M4.**

### The single most valuable result: three things got into the emitted Index with no guard firing

1. **A false force-gravity connection** — `G6` gains `3A-1`, `3A-1`'s row gains `G6`, exit 0, one Observation row labelled *not a defect*. Via a `[CORRECTION, …]` notice. **H1.**
2. **A false review-status claim** — a `CLEARED` round rendered `SUBSTANTIAL REVISION REQUIRED` in the Disposition, exit 0. **H2.**
3. **A wrong count** — `**14 connections**` against Doc_08 §9's certified *fifteen*, from one de-bolded ID, exit 0. **M4.**

### The third fix-pass-created defect, of the kind the fix pass reported two of

The brief asked whether any control's **computation** now exists without its **output**, or any output without a live computation. I checked both directions.

**Computation without output: none.** An AST pass over all 716 lines finds no name assigned and never read, and every key set on a force dict (`cell`, `conf`, `conf2`, `grav`, `layer2`, `stub`, `transmission`) is read at render. The cross-cell control's output block, deleted and restored at Round 6, is present and fires. That direction is clean and I record it as a positive result.

**Output without live computation: three, and one of them is HIGH.**

1. **The Disposition's verdict literal — H2.** `verdict_counts` changed contract from `str` to `(str, str)` at the Round 6 fix pass; `_VC` was updated, line 710 was not. The result is a tuple repr **in the committed file** plus a hard-coded verdict beside the derived one. **This is the same accident as the two the fix pass caught — a rewrite applied at one of two sites — except that its own suite did not catch this one, because the suite has no check on the emitted Index's text.**
2. **The Index's *"emphasis-dense span"* test — M5.** Output describing a computation that does not exist.
3. **The code comment's *"force-ID pattern"* in `STRUCTURAL` — M5.** Same.

**The lesson is narrow and worth recording:** the control suite mutates **inputs** and inspects **outputs**, and the two defects it caught were both input-side. Neither it nor any guard reads the emitted Index for well-formedness. A four-line assertion — *no `(` immediately followed by `'` in the rendered output; no `[` `]` tuple punctuation in a prose line* — would have caught the tuple before commit.

### `LATEST` — checked, and it can still mislead

Round 6's M4(c) is unaddressed in every limb: no `LATEST_FIX_PASS`, no Document Log read, and the cardinal/ordinal conflation intact. Demonstrated at **M3** and **M2**. This is the one Round 6 finding whose fix instruction was fully specified and not attempted at all.

### Reproducibility from an arbitrary working directory

**Confirmed, byte-identically, twice.** Run from `/` against the real world directory: output `md5 834054078c909f6764e3346b9d04bbdd`, identical to the committed file. Run from `/` against an isolated copy through the `argv[1]` override: identical again. `BASE` resolves from `__file__`; no session path anywhere in the file; `git status` on the world directory is clean after the review.

---

## Checks I confirmed before trusting, and my own defective ones

**H1, confirmed three ways before writing it.** (1) The mutation itself, run three times with three different unrecognised syntaxes, each producing the same wrong `G6` row. (2) **Independently of any mutation:** direct reading of `TAGS`, `_OPEN`, `NOTICE` and `OPENER` establishes that the coverage assertion's detector and the stripper are the *same pattern*, so the assertion's claim is circular as a matter of construction, not of test outcome. (3) A corpus census establishing that `[CORRECTION, …]` is not a tag I invented — and then, because a census is a grep, **I opened `Doc_05_Ecological_Reconstruction.md` and read two live instances** rather than trusting the count. I also verified the negative: Doc_08 **today** carries 43 notices, all four tag forms covered, all matched, zero surviving openers — so I am reporting a breadth failure, not a live wrong value, and I say so in the finding.

**H2, confirmed without any check at all, which is the strongest form available.** The tuple repr is in the committed file; I read line 162. Then `git show 0e70a96a` to establish *when* the contract changed and that the Disposition call site predates it. Then the `CLEARED` simulation, which is the part that needed a harness. Three channels, only one of them a script I wrote.

**M4, confirmed two ways.** The mutation, and then an independent count: Doc_08 §4's table has 15 data rows by eye and §9 certifies *fifteen*, so `14 connections` is wrong against two statements, not one.

**The review-history line, confirmed against the artifacts by hand.** I did not take the Index's derived counts on trust. I read each of the six artifacts' own verdict blocks: 4H5M3L1C, 3H4M3L1C, 4H5M4L2C, 3H3M5L1C, 2H3M3L2C, 1H4M4L2C, all six SUBSTANTIAL REVISION REQUIRED. The Index's line, Doc_08's Disposition list and the brief's `4, 3, 4, 3, 2, 1` all agree with the files. **The line is correct today** — M1 is a latent defect, not a live wrong value.

**My first defective check, and it would have been a fabricated finding against `verdict_counts`.** To verify the review-history line independently I ran a naive whole-file grep for the first `N HIGH, N MEDIUM, N LOW, N COSMETIC` in each artifact. It returned *4H 5M 3L 1C* for Round 2 and *4H 5M 3L 1C* for Round 3 — neither of which is that round's own count. For about a minute I had a finding that the Index's history line was wrong in two places. **My grep had reproduced, exactly, the recital bug the generator's anchoring exists to prevent** — it was reading each artifact's recital of a predecessor. The generator is right and my check was wrong. Two consequences: I re-did it anchored to each `## VERDICT` heading and read the six blocks by eye; and the episode is the reason I believe **M1** matters, because the trap is real enough to catch a reviewer who had just read the code that avoids it.

**My second defective check, and I nearly reported four bypasses of control (G).** My first brute-force search over notice-plant sites reported 44 "viable" over-consumption sites across 32 lines. Reading the spans it returned showed that almost all of them planted the malformed notice **inside an existing notice's opening bracket** — between `[` and `CORRECTED`, or between `MOVED` and `HERE` — which is not a defect anyone would write, and which only evaded the second-opener test because the real `[` had been left outside the span. I re-ran the search restricted to whitespace boundaries and the count fell from 44 to **2**, one of which was the same `[MOVED|HERE` artefact and the other of which consumes §8 prose that no derivation reads. **The honest result is that (G) has no realistic bypass in this document, and I have graded M2 CLOSED on the strength of a search I first had to fix.**

**A third, smaller.** My first attempt at control (F) planted the Form-B notice at the *start* of §5's G7 line, which pushed the `**G7 — ` heading off line-start and produced `FATAL: parsed 7 gravities`. I nearly recorded that as (F) failing. It was my mutation breaking the line structure, not the control. Moved to the end of the line, (F) passes exactly as advertised. **A FATAL from a guard is not evidence that the guard under test fired.**

**What I tested hardest, and why.** Control (G), because Round 6 defeated it and a claimed fix to a previously-defeated guard is the highest-value thing in a confirmatory read — I ran both of Round 6's placements verbatim *and* a brute-force search over every insertion point in the file before grading it closed. And the review-history derivation, because it is the one relation whose correctness I could establish from ground truth on disk without running anything the build wrote.

---

## Is the deliverable adequate to proceed to Doc_09?

**The analysis is, without qualification, and I did not need this round to establish it.** Round 6's judgement stands and I add nothing to it. I re-confirmed only what a confirmatory read needs: the generator reproduces the committed Index byte-identically; all eight gravities connect and no row is empty; §7's cross-check prints *"Agreement: all 17 forces carry the same confidence in Doc_08 §7 as in their own §3 entry"*; §6 prints no contradictions and no cross-cell disagreements; both transmission entries are present as their own named forces in 2B and 3B; all seventeen Layer 2 entries pass the stub test, now with notices stripped. **I would begin Doc_09 today and I would not ask for an eighth round of the forces analysis.**

**The pair should still not go to the project lead for disposition**, for one reason: the Index's Disposition section contains a malformed machine artifact and a hard-coded verdict that will be false the first time this pair is cleared — and the Disposition is where the disposition decision is read from. That is one line of code.

**The generator, on its second review as a deliverable, is better than it was and still describes itself too broadly.** Five of Round 6's findings against it are properly closed, two of them (M1, M2) closed better than asked. What it should stop doing is naming a control after the class and implementing the instance: (F) is called *"Unknown notice syntax"* and tests a known one; (H) says *"every claim form is matched"* and matches six; (G)'s narrative names a test that is not in the file. **A control stated more broadly than it is implemented is worse than no control, because the next round will trust it** — Round 6's sentence, kept verbatim for the second round, because this round found three more instances of it and one of them is a HIGH.

**Recommendation.** Fix **H2** (one line), then **H1** (widen the tag list *and* replace the circular assertion with a non-circular one — the second half is the one that matters). **M1–M5** are generator work and travel together; **M4** and **L2** are the same four lines. **L1, L3, L4, L5 and C1** need no review. Then **re-submit as a second confirmatory read of the generator alone.** Doc_08's prose and the forces analysis need no further review and should not be re-opened.

---

## CO-022 escalation assessment

**Category 1 — Representative identity, title, or voice: does not apply.** This document makes no identity, title or voice decision. Doc_08's own assessment says so and is correct.

**Category 2 — Portfolio-level or cross-world: Doc_08's four items stand; the fifth is still missing, for the second round.** I re-read the four and they are accurately stated. The Markdown-versus-workbook line is correctly closed at source. **The index-generator item that Round 5 raised, that Round 6 restated as L4, and that `lpc_Decision_Log.md` line 1269 records as *"Carried at the Disposition,"* is still not in Doc_08's assessment.** I restate it a third time so it is not lost again: *index generators are build artifacts; the portfolio has no convention for where they live, whether they are deliverables in their own right, or whether a regenerated index must be diffed before commit.* Not decided here.

**I add one candidate, and I flag it as a candidate rather than asserting it.** **Provenance-notice syntax is a cross-world convention with no owner.** `H1` turns on the fact that `**[CORRECTED, …]**`, `**[CORRECTION, …]**`, `**[SUPERSEDED, …]**` and `**[FURTHER CORRECTION, …]**` are all in use across `World-Builds/` — including three of them inside this world — and that a build-authored script which must distinguish correction notices from source text has no specification to code against. That is a portfolio question, not an `lpc` question, and it will recur in any world that derives an index from marked-up prose. **Not decided here; recorded for the project lead.**

**Category 3 — Governance or methodology: Doc_08's five items stand, unchanged.** The three-way divergence on the Forces Framework's three-layer rule across this world, Donatism and Alexandria remains open and properly framed at §8; two of the three readings sit in disposed documents. The **Construction-record notes** block, defined by no template and used by no sibling build, is correctly carried with it. I add nothing and subtract nothing.

**Category 4 — Unresolved tensions: one open**, the 411 *Gesta*, relied on for nothing here. Confirmed: no force in the matrix draws on it.

**Never self-assigning Frozen status: observed.** Neither deliverable self-certifies, neither claims Frozen, and all three say so in terms. Seven rounds, held every time.

**The known interaction, mentioned and not graded, as the brief directs.** Committing this artifact puts seven files in `Review-Artifacts/` against a Document Log naming six, so the generator will halt on `assert_doc08_round_count` until Doc_08 is updated. **That is the guard working as designed.** Round 6 flagged the same window. I note only that **M3**'s fix would dissolve it: once the fix-pass ordinal is read from the Document Log rather than inferred from the artifact count, the Index can be regenerated truthfully in the window between a review being filed and its fix pass being applied, and the assertion can warn rather than halt when the artifacts are *ahead* of the Log.

---

## On the brief that commissioned this review

Per the instruction not to inherit its claims, I checked them. **Two corrections and one confirmation.**

1. **The brief's control split is wrong, and it is inherited.** It describes *"one regression (A), six positive (B–F, I), two negative that halt it (G, H)."* **(I) halts the generator** — I reproduced it. The correct split is one regression, five positive (B–F), three negative (G, H, I). The count of **nine** is right. The brief took the 1/6/2 split from `lpc_Decision_Log.md` line 1291, which took it from Index §6 line 140 — the second consecutive round in which a miscount has travelled from the build record into the brief that commissions its review. Recorded as **L1**.

2. **The brief says "Rounds 1–6, HIGH counts 4, 3, 4, 3, 2, 1 — all SUBSTANTIAL REVISION REQUIRED." Confirmed exactly**, read off each artifact's own verdict block rather than off any derived line, and matching Doc_08's Document Log row for row.

3. **The brief's claim that Round 6 cleared the analysis is accurate**, and stated at Round 6's own strength: *"The analysis is — without qualification … I would not ask for a seventh round of the forces analysis and I would begin Doc_09 now."* The brief does not overstate it. Its instruction to treat this as a confirmatory read of the guards was the right call, and its three specific pointers all did work: *"re-run the exact scenario Round 6 used"* is what let me close **M2** honestly instead of guessing; *"check for a third defect of that kind"* is what found **H2**; and *"try to get a false force-gravity connection into the Index"* is what found **H1**, because it sent me at the notice channel from the input side rather than the guard side.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH, 5 MEDIUM, 5 LOW, 1 COSMETIC.**

**The forces analysis is adequate to proceed to Doc_09 and I say so without qualification — third consecutive round with no HIGH against it, and I did not re-open it.** Both HIGHs and all five MEDIUMs are against the certification apparatus and the generator. **HIGH-1** is a false force-gravity connection injected into the emitted Index through a correction-notice tag the stripper does not know, with every guard clean, behind an assertion that is circular by construction — Round 4's H1 class, reopened. **HIGH-2** is a hard-coded verdict word in the Index's Disposition, which renders a `CLEARED` round as `SUBSTANTIAL REVISION REQUIRED` and has already left a raw Python tuple in the committed file — the surviving half of a two-site finding whose fix landed at the site the reviewer quoted.

**Both are mechanical and neither is analysis work. If this were only M1–M5 and the LOWs I would have said MINOR REVISION, and I looked hard for a reason to** — I re-ran Round 6's defeating scenarios rather than assuming the fixes held, brute-forced the over-consumption guard rather than accepting one clean mutant, and threw away two of my own checks that would have produced findings against sound work. **The two HIGHs survived all of it.**

*Simulated review — informational only, not an Article 31 substitute.*

*End of Round 7 review.*
