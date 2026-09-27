# Doc_08 — `scripts/gen_force_index.py` and `lpc_Force_Index.md`: Latin Pastoral-Congregational Christianity

## Round 8 Second Confirmatory Read — the generator alone, reproduced and attacked

**Reviewer:** independent adversarial pass, no authorship of the material under review.
**Date:** 2026-09-15.
**Deliverables reviewed:** `scripts/gen_force_index.py` (791 lines) and `lpc_Force_Index.md` (162 lines). `Doc_08_Forces_Document.md` (476 lines) read **as generator input only** — its Document Log, its Disposition and its §§3–5/§7/§9 structure, because those are what the generator parses and asserts against. **I did not re-review the forces analysis, its Layer 2 prose or its quotations, and nothing I found required me to.** That scope is Round 7's own recommendation and the brief's instruction, and it was the right call twice over.
**Prior rounds:** Round 1 (4H 5M 3L 1C), Round 2 (3H 4M 3L 1C), Round 3 (4H 5M 4L 2C), Round 4 (3H 3M 5L 1C), Round 5 (2H 3M 3L 2C), Round 6 (1H 4M 4L 2C), Round 7 (2H 5M 5L 1C) — all SUBSTANTIAL REVISION REQUIRED. **Each round's counts and verdict read off its own artifact by hand**, not off the Index's derived line; see **Checks I confirmed**.

*Simulated review — informational only, not an Article 31 substitute.*

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH, 5 MEDIUM, 6 LOW, 1 COSMETIC.**

**Said plainly, because the brief asks for honesty in both directions and this build needs to be able to reach a clearance.**

- **The forces analysis is sound and clear to proceed to Doc_09.** Fourth consecutive round with no HIGH against it, and I did not open it. Round 6's judgement stands unqualified.
- **A great deal genuinely closed this round, and it closed structurally rather than at the sites a reviewer quoted.** Round 7's **H2** is fully closed — the Disposition renders `(2H 5M 5L 1C, SUBSTANTIAL REVISION REQUIRED)` from `_VC`, the raw Python tuple is gone, and I drove a synthetic `CLEARED` round through end-to-end and watched `VERDICT_LINE` degrade to a per-round list correctly. Round 7's **H1** is closed at all four mutants it named: `[CORRECTION, …]`, `[SUPERSEDED, …]`, `[Added, …]` and `[ADDED 2026-… ]` are now stripped, and the planted `3A-1` does not reach `G6`. **`DETECT` is genuinely non-circular** — it is a different pattern from `NOTICE`, it is case-insensitive, and I confirmed it halts on an all-lowercase notice the stripper ignores. Round 7's **M3** is closed at two of its three sites and the new `FIXPASS_NOTE` is a real improvement. **L1** is closed: the split is now one regression, five positive, four negative, and I reproduced all ten controls to check it. The generator **reproduces the committed Index byte-identically from `/` as the working directory** (md5 `268fd7ef…`).
- **But I still got all three of the results the brief names into the emitted Index with every guard clean, exit 0.**
  - **A false force-gravity connection**, ten different ways. The fix moved the closed list from the *tag* to the *separator*, and the separator is narrower than the tag list was. **`[FURTHER CORRECTION, Round 9.]` and `[SUPERSEDED, Round 9: …]` — both live in this world's own `lpc_Decision_Log.md` — walk straight through both the stripper and the detector.** So does a colon instead of a comma. **HIGH-1.**
  - **A false review-status claim.** A Round-7 artifact that returned SUBSTANTIAL REVISION REQUIRED is reported in the **Index's Disposition** as `CLEARED`, exit 0, no guard — because `verdict_counts` still reads the verdict from `t[i:i+200]`, a character count chosen by eye, in the same function whose *counts* limb was given a structural bound and whose §6 paragraph says so. **HIGH-2.**
  - **A wrong count.** Deleting **one trailing pipe** from a §4 row drops a connection out of both the parse *and* the row count, so the new guard's equality still holds; the Index prints **14 connections** against Doc_08 §9's certified *fifteen*. That is verbatim the outcome control **(J)** is advertised as preventing. **MEDIUM-1.**
- **Round 6's carried sentence held up again and I carry it a third time:** *a control stated more broadly than it is implemented is worse than no control, because the next round will trust it.* Control **(J)**, control **(H)**'s *"every claim form is matched"*, the header's *"hard-coded prose, re-verified by nothing"*, the code's *"any bracketed capitalised tag followed by a comma or a dash"*, and Round 7's **M5** — *"emphasis-dense"* and *"plus the force-ID pattern"*, both still describing tests that are not in the file.

**The distance to clearance is short and entirely mechanical.** One separator widening plus a genuinely open detector; one line in `verdict_counts`; one `len(conns)` comparison against a parsed §9; and five wording narrowings. **No analysis work is outstanding and none of this is a defect in the forces document.** But two HIGHs survive and one of them puts a false clearance into the section disposition is decided from, so this is SUBSTANTIAL REVISION REQUIRED and not MINOR REVISION. **Seven prior rounds of this verdict is a reason to have been harder on myself about grading, not a reason to reach for an eighth — so every finding below names the mutation, the exit code and the emitted line, and I say where my own checks were wrong.**

---

## Method — what I actually ran

1. **Byte-identity.** Copied the world folder to a scratch sandbox, ran `python3 <sandbox>/scripts/gen_force_index.py` with cwd `/`, diffed against the committed `lpc_Force_Index.md`. Identical, zero bytes different, md5 `268fd7ef81265047b671f09d26d919ff` both sides. Re-ran the unmutated sandbox before every batch as a harness self-check; it reproduced the committed file every time.
2. **A mutation harness** that copies the world folder fresh for each mutant, applies one edit with an assert-on-anchor-not-found guard, runs the generator from cwd `/`, and reports exit code plus the specific emitted rows. **41 mutants in total.** Every claim below names its mutant.
3. **Round 7's H1 scenarios re-run verbatim** — all four notice forms it defeated the stripper with — then **eleven new notice forms** aimed at the new pattern from the input side.
4. **All ten advertised controls reproduced individually**, including control (C) across all six tag forms it names and control (A) against the pre-fix draft at `9eccc532` recovered from git.
5. **Regex-level confirmation in isolation** for every stripper/detector claim, independent of the generator, so a finding never rests on one harness.
6. **A hand read of all seven review artifacts' own verdict blocks**, to check the derived review-history line against the files rather than against itself.
7. **A corpus census** of `**[TAG …]**` forms across `World-Builds/` to separate hypothetical notice syntaxes from ones already in use.
8. **A read of the whole generator** for computations without outputs and outputs without computations, per Round 7's finding of three of the latter.

---

## Job 1 — Round 7's thirteen findings, closure status at the live text

| Round 7 | Status | Evidence |
|---|---|---|
| **H1** — closed tag list; circular coverage assertion | **Closed at its four named mutants; the class is reopened by a different limb.** `TAGS` → open pattern, `DETECT` genuinely distinct and case-insensitive. **But see H1 below:** ten forms defeat both. | 4 R7 mutants → `G6` stays at 3 forces; 10 new mutants → `G6` at 4 with `3A-1` |
| **H2** — hard-coded verdict literal; raw Python tuple | **Closed, both limbs.** `_VC[LATEST]` unpacked; no tuple repr; synthetic `CLEARED` renders as `CLEARED` in Disposition and degrades `VERDICT_LINE` to a per-round list. | `m3b` mutant, exit 0 |
| **M1** — `## VERDICT` anchored on first textual occurrence | **Half closed.** Anchor is now `^#{2,3} VERDICT` with `re.M` — no longer defeated by a backticked mention. **Not closed:** a heading quoted at line start inside a fence still wins, and the *counts* recital and the *verdict* window are both still first-match. | **H2** below |
| **M2** — control (H) is a phrase list | **Open.** All three of Round 7's surviving mutants still pass, plus three new ones. | **M2** below |
| **M3** — `LATEST` conflates artifact with fix pass | **Closed at two of three sites.** `LATEST_FIX_PASS` is read from the Document Log; *Revised:* and the Disposition are correct and `FIXPASS_NOTE` fires. **The Status line still renders `LATEST`.** | **M3** below |
| **M4** — no §4 row-count guard | **Guard added; narrower than stated.** De-bolding the source ID halts correctly. Three other one-character slips do not. | **M1** below |
| **M5** — two described tests that do not exist | **Open, both limbs, untouched.** `emphasis-dense` still at Index line 142 and script line 754; `plus the force-ID pattern` still at script line 79; `STRUCTURAL` has neither. | **M5** below |
| **L1** — control split miscounted | **Closed for the split** (one regression, five positive B–F, four negative G–J — I reproduced all ten and the arithmetic is right). **A new instance of the same miscount is in the same paragraph.** | **L1** below |
| **L2** — §9's hand-typed distribution read by nothing | **Open, untouched.** | **L4** below |
| **L3** — Decision Log escalation not carried | Out of scope this round (Decision Log / Doc_08 CO-022 prose). Restated in my CO-022 assessment so it is not lost a fourth time. | — |
| **L4** — Decision Log credits work not done | Out of scope. The H2 half is now genuinely true, so that sentence has become accurate by being caught up with. | — |
| **L5** — `argv[1]` unguarded; `ROUNDS[-1]` unguarded | **Half closed.** `ROUNDS[-1]` now appears once, guarded, at line 179. `--help` still dies in a raw `FileNotFoundError`. | **L5** below |
| **C1** — 2×7 quotation trimmed without marking | Out of scope (Doc_08 prose). Not assessed. | — |

**Seven of the thirteen are wholly or substantially closed, and the two HIGHs are the two that were hardest to close. That is real progress and I want it on the record before the findings.**

---

## HIGH

### H1 — The notice channel is still open as a class. Ten realistic notice forms defeat both the stripper *and* the broader detector and put a false force-gravity connection into the emitted Index, exit 0, with §6 printing "No contradictions" and labelling the anomaly *not a defect*. Two of the ten are live in this world's own `lpc_Decision_Log.md`. The fix moved the closed list from the tag to the separator, and the separator is narrower than the tag list was.

**Site.** `scripts/gen_force_index.py` lines 37–68 (`_SEP`, `_OPEN`, `NOTICE`, `OPENER`, `DETECT`) and lines 84–113 (`assert_notice_coverage`); `lpc_Force_Index.md` §6, controls **(C)** and **(F)** and the non-circularity claim; the script's own header comment at lines 30–38 and 57–65.

**What was fixed, and I credit it properly.** The tag vocabulary is no longer a closed list. `_OPEN` now accepts any bracketed capitalised word (or two), and `DETECT` is a genuinely *different* pattern — broader, case-insensitive, and with no terminator requirement — so it is no longer circular in the way Round 7 proved. I re-ran Round 7's four defeating mutants on §5's G6 line and **all four now strip correctly**, `G6` staying at `2A-3, 2B-1, 2B-4`. I also reproduced control (C) across all six tag forms the Index advertises, including the all-lowercase `[correction, …]`, which halts on `DETECT` exactly as claimed. **That part of the Round 7 fix is done and done well.**

**What replaced the closed list.** The tag is open; **the separator is not.** Both patterns now require one of exactly three things immediately after the tag:

```python
_SEP   = r"(?=,\s*\d{4}|\s+\d{4}|\s*—)"          # comma+YEAR, space+YEAR, or em dash
DETECT = ... r"(?:,\s*\d{4}|\s+\d{4}|\s*—|\s+-\s)"   # …plus a spaced hyphen
```

A notice whose tag is followed by anything else — a colon, a semicolon, a parenthesis, an en dash, or a comma followed by a **round number instead of a year** — is invisible to both. So is a **three-word** tag, and so is any single-word tag longer than **15 letters**, because `[A-Z][A-Za-z]{2,14}` caps it.

**Ten mutants, each one notice on §5's G6 line, each exit 0, each injecting `3A-1` into `G6`.**

| Mutant planted on §5's G6 line | Exit | `G6` row emitted |
|---|---|---|
| `**[CORRECTED: 2026-09-15 — … **3A-1** …]**` (colon) | **0** | `2A-3, 2B-1, 2B-4, 3A-1` — **4** |
| `**[CORRECTED; 2026-09-15 — …]**` (semicolon) | **0** | same |
| `**[CORRECTED (2026-09-15) — …]**` (parenthesised date) | **0** | same |
| `**[CORRECTED – 2026-09-15: …]**` (**en** dash, not em) | **0** | same |
| `**[CORRECTED, Round 7 — …]**` (round number, not a year) | **0** | same |
| `**[CORRECTED at R7 — …]**` | **0** | same |
| `**[FURTHER CORRECTION, Round 9.]**` — **live form** | **0** | same |
| `**[SUPERSEDED, Round 9: …]**` — **live form** | **0** | same |
| `**[CORRECTED AND MOVED, 2026-09-15 — …]**` (three words) | **0** | same |
| `**[REINTERPRETATION, 2026-09-15 — …]**` (16-letter tag) | **0** | same |
| `**[CO-022, 2026-09-15 — …]**` (hyphen/digits in tag) | **0** | same |

**Confirmed a second way, independent of the harness.** I evaluated `NOTICE.search` and `DETECT.search` directly on each string outside the generator. Every one returns `None` from both; the house form `**[CORRECTED, 2026-09-15 — …]**` returns a match from both. The two methods agree on all eleven.

**Nothing in the emitted Index warns a reader; one line affirmatively reassures them.** All hard guards pass (17 forces, 8 gravities, 15 connections). §6 prints **"No contradictions: no force's §3 Layer 3 asserts a gravity connection that §5's canonical list omits…"**. `3A-1`'s master-table row reads `Connected Gravities | G1, G6`. And §6's observation table gains a **sixth** row — *"`3A-1` | G6 | §5's list carries it; §3's Layer 3 does not assert it in a connection sentence"* — sitting among five genuine ones under the heading **"Observations — not defects."** A reader is told the anomaly is expected asymmetry. **This is Round 7's H1 output, reproduced exactly, one round later.**

**These are not hypothetical tags.** A census of `**[…]**` forms across `World-Builds/` that the *current* stripper cannot see returns, among others: **`[FURTHER CORRECTION, Round 9.]` — 5 occurrences**, **`[SUPERSEDED, Round 9: …]` — 5**, `[NO FINDING — VERIFIED SOUND]` — 18, `[MODERATE, requires fix]` — 3, `[COSMETIC, requires fix]` — 2, `[SUBSTANTIAL, fixed]` — 2. **The first two are in `lpc_Decision_Log.md`, in this world, at lines 678, 696 and three more.** Round 7 named `FURTHER CORRECTION` explicitly in its fix instruction (*"Widen `TAGS` to the vocabulary actually in use (`CORRECTION`, `FURTHER CORRECTION`, `SUPERSEDED` at minimum)"*). `CORRECTION` and `SUPERSEDED` are now handled **when followed by a year**; the live occurrences of both in this world are followed by *"Round 9"*, and are not.

**The generator's own self-description is broader than the code, and that is how this recurs.** Line 37: *"The pattern is now OPEN: **any bracketed capitalised tag followed by a comma or a dash** is a notice."* It is not. A comma alone does not qualify — `[FURTHER CORRECTION, Round 9.]` proves it — and a bare hyphen and an en dash do not either. A future fix pass reading that comment will believe the class is closed. It is the carried sentence again, this time inside the code.

**Why HIGH.** Identical reasoning to Round 7's H1, and I checked whether it had weakened. It has not. The delivered Index is **correct today** — I verified all 43 notices in the live Doc_08 are matched and stripped, and there is no wrong value in the committed file. The defect is in the **breadth of the guarantee** that both deliverables now rest their integrity claim on: Doc_08's Document Log records *"notices stripped before all derivation"* as the Round 4 fix; the Index advertises (C) and (F) and a non-circular assertion. **The class is closed for three separator forms someone happened to enumerate.** Every fix pass in this build writes new notices; seven have. The next one that reaches for the house form one document over — *"[FURTHER CORRECTION, Round 9.]"*, five live instances away — reopens Round 4's H1 silently, and §6 will print a row explaining it away.

**Fix.**
1. **Stop enumerating separators.** Treat `\[` + a capitalised or ALL-CAPS token of 2–30 characters (allowing digits, hyphens and up to three words) + any of `[,:;(\-–—]` or whitespace as a notice opener. The `[X]` recapitalisation convention is a single letter and still cannot match.
2. **Make `DETECT` open where `NOTICE` is closed, on the axis that actually matters.** It is now broader on *case* and on *terminator*; it is exactly as narrow as `NOTICE` on *separator*, which is the axis every one of these ten mutants exploits. Give `DETECT` no separator requirement at all — `\*\*\[[A-Z]` followed by 2+ letters and then any non-letter — and let it halt on anything that survives stripping. It will fire on new syntax the first time it is written, which is the only moment it is cheap to fix.
3. **Correct the comment at line 37** to state the separator set it actually implements, or delete the sentence.
4. **Narrow control (F)'s advertised scope** in the Index, as Round 7 asked and this round confirms is still needed: it tests the `**Heading. [TAG …]**` *form*, not the class of unknown syntaxes.

---

### H2 — A round that returned SUBSTANTIAL REVISION REQUIRED is reported in the Index's **Disposition** as `CLEARED`, exit 0, no guard. `verdict_counts` was given a structural window bound for its *counts* and left a 200-character window chosen by eye for its *verdict*, and §6 states the fix as complete. A second route reaches the same output through a heading quoted in a code fence.

**Site.** `gen_force_index.py` lines 188–219 (`verdict_counts`), specifically lines 210–215; rendered at lines 580 (`HISTORY`, `VERDICT_LINE`) and 785 (Disposition). `lpc_Force_Index.md` line 4, line 142 and line 162.

**What the code does.** The counts limb was genuinely fixed and I confirm it:

```python
rest = t[_h.end():]
nxt  = re.search(r"^#{2,3} ", rest, re.M)
window = rest[:nxt.start()] if nxt else rest[:1200]      # structural bound — good
...
vm = re.search(r"(CLEARED|MINOR REVISION|SUBSTANTIAL REVISION REQUIRED|REJECTED)",
               t[i:i + 200])                              # NOT the window. 200 chars, by eye.
```

The verdict is taken from a **fixed 200-character slice starting at the heading**, not from `window`, and it is a first-match search. Index §6 says of this exact function: *"The window now ends at the next heading — **a structural bound rather than a number chosen by eye**."* That sentence is true of `counts` and false of `verdict`, in the same function, four lines apart.

**Mutant, and it is the dangerous direction.** Round 7's artifact, verdict section rewritten in the ordinary shape a confirmatory read takes — a sentence about the previous round, then its own verdict:

```
(heading) VERDICT

Round 6 returned **CLEARED** on the analysis and I confirm that.

This round's verdict on the pair is **SUBSTANTIAL REVISION REQUIRED**.
```

Exit 0. Emitted, in `lpc_Force_Index.md`'s **Disposition**:

> **Not disposed.** … the most recent `Review-Artifacts/Doc08_Round7_Review.md` (2H 5M 5L 1C, **`CLEARED`**); this file is the Round 7 fix pass and is **unreviewed**.

**The Index reports the most recent round as having cleared the pair when it returned SUBSTANTIAL REVISION REQUIRED.** The counts beside it are correct, which makes the line read as derived and trustworthy.

**The reverse direction too, and the counts limb with it.** Two further mutants, both exit 0:

| Mutant in the Round 7 artifact's verdict section | Emitted in the Index |
|---|---|
| heading `VERDICT` (no verdict on it); *"Round 6 returned SUBSTANTIAL REVISION REQUIRED…"*; own verdict `CLEARED` below | Disposition: `(2H 5M 5L 1C, SUBSTANTIAL REVISION REQUIRED)`; review-history line reverts to **"all SUBSTANTIAL REVISION REQUIRED"** — the exact literal Round 7's H2 removed, regenerated from a misparse |
| heading `VERDICT: CLEARED`; *"Round 6 returned 1 HIGH, 4 MEDIUM, 4 LOW, 2 COSMETIC."*; own counts below | `Round 7 (**1H 4M 4L 2C**)` — **Round 6's counts under Round 7's label**, and the Disposition reads `(1H 4M 4L 2C, CLEARED)` |

The second is **Round 7's M1 verbatim**, still reproducible. The heading bound is real, but the recital sits *inside* the window and `re.search` takes the first match; changing where the window ends does not change which match wins. **Third consecutive fix at this one function that relocates the defect rather than closing it.**

**A second, independent route: a heading quoted in a code fence.** The anchor moved from `t.find("## VERDICT")` to `re.search(r"^#{2,3} VERDICT", t, re.M)`, which closes Round 7's backticked-mention case. It does not close a fenced block, because a fence's contents are still line-start text:

    ```
    (two hashes) VERDICT: CLEARED
    ```

Planted six lines above Round 7's real heading, exit 0, and the Index emits `Round 7 (counts not parsed, **CLEARED**)` in both the review-history line and the Disposition — **a false verdict lifted out of a quotation**, not merely a failed parse. **This is not a contrived file.** Three of the seven existing artifacts discuss this parser by name, and a review artifact documenting the defect is exactly the file that would quote the heading. Round 7 hit the weaker version of this in its own draft and re-worded rather than leave the trap; **I have written this finding without putting the bare heading string at line start anywhere outside my own real heading**, which is a workaround, not a fix, and the fact that two consecutive reviewers have had to apply it is the argument.

**Confirmed a second way.** For each mutant I read the modified artifact back and confirmed by hand which verdict word and which counts the file's own verdict section states, then compared against the emitted line. I also confirmed the unmutated run of the same sandbox reproduces the committed Index byte-identically, so the harness is not the variable.

**Why HIGH.** Constitution Article 30 and CO-022 make disposition turn on review status, and the **Disposition section is the one place that decision is read from**. Round 6's H1 and Round 7's H2 were both graded HIGH on precisely this ground, and this is the same output — *a revision round reported as cleared* — reached by a different mechanism one round later, with a closure claim attached to it in §6. The delivered file is correct today only because all seven artifacts happen to state their own counts and verdict before any recital. **That is a formatting convention nobody has written down**, and Round 7 said so; it is still not written down, and the brief for this round instructed me to put my verdict "near the top", which is the convention being relied on and is not the same as requiring it.

**Fix.**
1. **One line:** take the verdict from `window`, not from `t[i:i+200]`.
2. **Make first-match into an ambiguity report,** in the idiom the file already uses twice: if the window contains more than one verdict word, or more than one `N HIGH … N COSMETIC` group, emit `verdict ambiguous — N candidates` / `counts ambiguous — N candidates` rather than picking one. The file already degrades gracefully to `counts not parsed`; extend the same instinct.
3. **Strip fenced blocks** (` ``` ` … ` ``` `) from `t` before anchoring, so a quoted heading cannot be an anchor.
4. **Write the convention down** in the Index's §6 and in the brief template: *a review artifact states its own counts and verdict before any recital of a previous round's.* A parser that depends on a convention should name it.

---

## MEDIUM

### M1 — Control (J) is stated as closing the silent-connection-drop class. **One missing trailing pipe** drops a connection out of the parse *and* out of the row count together, so the equality holds and the Index prints **14 connections** against Doc_08 §9's certified *fifteen* — verbatim the outcome (J) says it prevents. Deleting a whole row and duplicating a row are equally silent.

**Site.** `gen_force_index.py` lines 495–516 (`ROW_RE`, `conns`, `_sec4_rows`); `lpc_Force_Index.md` line 140 (control **J**) and line 100; `Doc_08_Forces_Document.md` §9.

**The guard, and what it compares.**

```python
_sec4_rows = [ln for ln in sec4.split("\n")
              if ln.strip().startswith("|") and ln.count("|") >= 5
              and not re.match(r"^\|[\s|:-]+\|$", ln.strip())
              and "From" not in ln.split("|")[1]]
if len(conns) != len(_sec4_rows): sys.exit(...)
```

It compares the parse against **its own idea of how many rows there are**. Any defect that removes a row from *both* counts passes. `ROW_RE` needs a trailing `|`; `_sec4_rows` needs five of them.

**Four mutants on `| **1B-1** | **2B-4** | enables | … |`, all exit 0:**

| Mutation | Emitted |
|---|---|
| **delete the trailing `\|`** (5 pipes → 4) | `(17 forces, **14 connections**, 8 gravities)`; §4 summary **"14 connections"**; `1B-1`'s master row loses `→ 2B-4`, `2B-4`'s loses `← 1B-1` |
| **delete the whole row** | `14 connections`, identically silent |
| **first cell reads `From **1B-1**`** | `14 connections` — the header-skip clause eats a data row |
| **duplicate the row** | `**16 connections**`; `1B-1` shows `→ 2B-4 (enables); → 2B-4 (enables)`; `2B-4` shows `← 1B-1 (enables); ← 1B-1 (enables)` |

In all four, **Doc_08 §9 still certifies *fifteen*** and nothing compares the two. The de-bolded **source** ID does halt, correctly, with the message quoted in (J); the de-bolded **destination** ID does not need to, and correctly does not.

**Confirmed a second way.** Independently of the exit line, I counted the `| \`` data rows the Index's own §4 table prints: 19 for the trailing-pipe mutant against 20 for the baseline, and 21 for the duplicate. The printed table, the summary sentence and the master-table cross-cell columns all agree with each other and all disagree with Doc_08 §9.

**Why this matters and why MEDIUM.** A missing trailing pipe is the single most common markdown table slip and this build has hit formatting slips in §4 before — it is why (J) exists. The Index's claim is unhedged: *"(J) a §4 row that fails to parse — a de-bolded force ID — **halts, instead of silently printing one connection fewer than Doc_08 certifies**."* It halts for the one slip the fix pass tested and not for three others that produce exactly the named outcome. I keep it MEDIUM rather than HIGH because the consequence is a count and a missing edge rather than a false relation, and because Round 7 graded the same class MEDIUM when there was no guard at all — but by Round 6's standard this is now *worse* than Round 7's M4, because a reader of §6 will believe the class is closed.

**Fix.** Do not compare the parse against a re-derivation of the same lines. **Compare it against Doc_08 §9's certification**, which is the independent statement: parse *"Cross-cell connections documented in Section 4 — fifteen"* and require `len(conns)` to equal it, in the §7 cross-check's idiom. That closes this finding and **L4** together, and it is the fix Round 7 already recommended. Add `assert len(conns) == len(set((c['src'],c['dst'],c['dir']) for c in conns))` to catch duplication.

### M2 — Control (H) is stated as *"every claim form is matched."* Six false review-status claims pass it, exit 0 — all three of Round 7's surviving mutants and three new ones. Verdict **words** and per-round **counts** inside Doc_08 are compared against nothing, though `_VC` holds the true values and the Index prints them 150 lines above.

**Site.** `gen_force_index.py` lines 122–169 (`assert_doc08_round_count`); `lpc_Force_Index.md` §6, control **(H)** and the (H) narrative at line 142.

**Six mutants, each a single edit to Doc_08, each exit 0 and each a false statement about this document's review history:**

| Mutant | Why it passes |
|---|---|
| Document Log's **Round 3 and Round 4 rows deleted** | `max(ords)` is still 7; a Log missing two rounds is invisible. **Round 6 reported this; Round 7 reported it again; unaddressed.** |
| Disposition rewritten to *"**Three rounds of** independent adversarial review have been run"* | the pattern needs `independent adversarial review rounds` in that word order. A rephrase is a claim form. **Round 7's mutant, unaddressed.** |
| Disposition rewritten to *"all seven returning **CLEARED**"* | verdict **words** in Doc_08 are compared against nothing. **Round 7's mutant, unaddressed.** |
| Document Log's Round 6 row rewritten to *"**CLEARED** — 0 HIGH"* | same — Log row verdicts are read by nothing |
| Disposition's `Round 7 (2H 5M 5L 1C)` rewritten to `Round 7 (0H 0M 1L 0C)` | per-round **counts** in Doc_08 are compared against nothing, though `_VC[7]` holds `2H 5M 5L 1C` and §-header line 4 prints it |
| §9 rewritten to *"has now been run **twice**"* | `WORDNUM` has `One…Ten`; `twice` is not a number word |

**The widening from Round 6 is real and I credit it** — emphasis is flattened, matching is case-insensitive, numerals and number-words both parse, `REVISED after Round N` is checked at every occurrence rather than by a maximum, and the FATAL names every disagreeing site rather than the first. It caught four of my other mutants cleanly, including a gap in the artifact sequence. **It is a good guard described as an exhaustive one.**

**The sharpest limb is the cheapest to close.** `_VC` already holds each artifact's true counts *and* verdict. Doc_08 restates both by hand, in its Document Log rows and in its Disposition paragraph, and **neither restatement is read.** That is the same shape as §7's confidence list and §3's gravity prose — both of which *do* get a cross-check — sitting untouched in the one place the document's review status is asserted.

**Fix.** State (H) at its real coverage — *"the six claim forms enumerated in the assertion"* — **and** add the two comparisons that need no new machinery: every `Round N (…H …M …L …C)` group in Doc_08 against `_VC[N][0]`, and every verdict word adjacent to a `Round N` reference against `_VC[N][1]`. Add a contiguity check on `ROUNDS` so a gap halts with an accurate reason rather than incidentally.

### M3 — The Index's **Status line** still renders `LATEST`, so it asserts a fix pass that has not happened; and control (H) **compels a false claim in Doc_08** in the same window, because *"REVISED after Round N"* is asserted against the count of review artifacts rather than the fix-pass ordinal the generator already computes.

**Site.** `gen_force_index.py` line 579 against lines 236–242 (`LATEST_FIX_PASS`, `FIXPASS_NOTE`) and line 158 (`REVISED after Round\s+(\d+)` inside `assert_doc08_round_count`).

**First limb — Round 7's M3, third site.** `LATEST_FIX_PASS` was added and used at line 581 (*Revised:*) and line 785 (*this file is the Round N fix pass*), both now correct, with a genuinely good `FIXPASS_NOTE`. **Line 579 was not changed.** With a synthetic Round 8 artifact on disk and no Round 8 fix pass, the Index emits:

> **Status:** **REVISED after Round 8 — the revision is unreviewed…**
> **World file-code:** … **Revised:** 2026-09-15 (Round **7** fix pass) …
> **Not disposed.** … this file is the Round **7** fix pass … **Note:** the most recent review artifact is Round 8, but Doc_08's Document Log records no fix pass beyond Round 7…

The masthead — the first line a project lead reads — contradicts the note twenty lines below that exists to prevent exactly this.

**Second limb, and it is the more interesting one.** `assert_doc08_round_count` requires **every** occurrence of `REVISED after Round N` in Doc_08 to equal `NROUNDS`, the artifact count. But *"REVISED after Round N"* is a claim about **which fix pass produced the current revision**, not about how many reviews exist. I confirmed the consequence directly: with eight artifacts on disk and Doc_08 truthfully saying *"REVISED after Round 7"* — which is what it would be, since no Round 8 fix pass has run —

```
FATAL: Doc_08's review-history claims disagree with Review-Artifacts/:
  - 'REVISED after Round 7' vs 8 artifacts
  - 'REVISED after Round 7' vs 8 artifacts
```

**The only way to satisfy the guard is to write a statement that is false.** That is not a hypothetical window: it is the window this pair is in every time a review is filed, and it is the window it will be in the moment this artifact is committed. A fix pass that reaches for the obvious remedy — bump both sites to *"REVISED after Round 8"* — installs a false review-status claim in Doc_08's Disposition **at the guard's insistence**, which is the failure mode this build has the longest history with.

**Fix.** Render line 579 from `LATEST_FIX_PASS`, with `FIXPASS_NOTE` beside it as the other two sites already do. In `assert_doc08_round_count`, compare `REVISED after Round N` against the **fix-pass ordinal from the Document Log**, and compare the *count* claims against `NROUNDS`; where the artifacts are ahead of the Log, say so rather than halting.

### M4 — The open notice pattern halts the generator on ordinary scholarly prose. A bracketed source citation containing a year, or a bracketed editorial gloss with an em dash, is read as a correction notice; the FATAL then misnames the cause. It fails safe and the live document is clean — that is the right side of the trade, and the diagnostic should say what actually happened.

**Site.** `gen_force_index.py` lines 53–68 and lines 99–113.

**Three mutants, each one sentence of legitimate prose added to Doc_08, all exit 1:**

| Added text | Emitted FATAL |
|---|---|
| `…the Latin is Hartel's [CSEL 1868] text.` | *"a correction notice … **spans a structural marker** … It is almost certainly **missing its own terminator and is consuming real source**"* |
| `…Augustine's own retrospect [Retractationes — Prologus] is the witness.` | same |
| `…(See [Doc revision 2026] for the superseding note.)` | *"1 notice-like opener(s) survive stripping"* |

None of these is a notice. The first two are the citation forms a source-grounded document reaches for, and this world's Doc_08 already cites *"Registry row 209"* and *"Retractationes Prologus"* in prose. **The message a builder gets tells them to look for a malformed notice; there is no notice.**

**But I want to be exact about the harm, because the brief asked the right question and the answer is not the obvious one.** I looked for a case where over-stripping **silently removes real source** — the mirror defect, and the one that has already happened once in this build. **I could not construct one on this document, and there is a structural reason.** Every one of the 44 `]**` terminators in Doc_08 is owned by a notice opener within the preceding 2000 characters — I checked all 44 — so any over-broad opener that runs forward to a terminator necessarily pulls a second `OPENER` into its span, and `swallowed = len(OPENER.findall(span)) > 1` fires. **The opener-count test carries essentially all the weight here and it is the right test.** Round 7 said the same about it and I confirm it independently.

**One structural note that belongs with this finding.** `assert_notice_coverage` iterates `NOTICE.finditer(t)` over the **whole text** with `re.S`, while `strip_notices` applies the same pattern **line by line**. The guard therefore evaluates spans the stripper can never produce. That is conservative and I am not asking for it to be relaxed — but it means the guard's three branches (`swallowed`, `STRUCTURAL`, `len > 3000`) all emit the **same** message, which names only the second.

**Fix.** Report which branch fired, and say *"unrecognised bracketed construct read as a notice opener"* where the opener is not a known tag. Exempt a bracketed token whose following word is a known bibliographic marker, or simply require a notice opener to be ALL-CAPS or Title Case **and** be followed by `]` within the line — a citation is not.

### M5 — Round 7's M5 is untouched, both limbs. The Index still says control (G) halts on an *"emphasis-dense"* span and the code comment still says `STRUCTURAL` carries *"the force-ID pattern."* Neither exists in the file.

**Site.** `lpc_Force_Index.md` line 142; `gen_force_index.py` line 754 (the same string, emitted) and line 79 (the comment); `STRUCTURAL` at lines 81–82.

```python
STRUCTURAL = re.compile(
    r"Connected forces:|^\*\*G\d — |^\#{2,4} |^\*\*Layer [123] |^\| ", re.M)
...
swallowed = len(OPENER.findall(span)) > 1
if swallowed or STRUCTURAL.search(span) or len(span) > 3000:
```

No emphasis-density measure. No force-ID alternative. The implemented tests are: a second opener inside the span; a structural marker; a 3000-character ceiling. Round 7 named both strings, gave the line numbers, and offered a one-line fix for each. **Neither was applied, in the fix pass that rewrote the surrounding paragraph.** I verified with `grep`: `emphasis-dense` occurs once in each file, `force-ID pattern` once in the script, `STRUCTURAL` has neither.

**Why this stays MEDIUM rather than dropping to LOW.** It is the carried sentence in its purest form and it is load-bearing: a reader of §6 concludes a runaway notice is caught by three independent properties when it is caught by one plus two backstops. And the implemented test is **better** than the described one — the opener-count signature is the precise fingerprint of over-consumption, and I confirmed above that it is what holds the line. The file is under-claiming its best control and over-claiming two it does not have.

**Fix.** Delete *"or emphasis-dense"* from the Index and script, and *"plus the force-ID pattern"* from the comment. Replace with what (G) actually keys on: *"a notice span containing a second notice's opener — the signature of a match that ran past its own terminator."*

---

## LOW

### L1 — The controls paragraph enumerates the ten controls **twice**, and the second enumeration stops at (I). A reader counting from it gets nine — the same miscount the paragraph exists to correct, reinstalled in the paragraph correcting it.

**Site.** `lpc_Force_Index.md` line 140; `gen_force_index.py` lines 730–751.

The split is now **right** and I verified it by reproducing all ten: one regression (A), five positive (B–F), four negative (G, H, I, J), and G, H, I and J all exit 1. **Round 7's L1 is closed.** But the paragraph then says `**(A)** regression …` through `**(J)** a §4 row that fails to parse … halts`, inserts the parenthetical about the miscount's history, and then **restates (A) through (I) again with longer descriptions, omitting (J) entirely**. Programmatically: first enumeration `[A…J]`, second `[A…I]`. The parenthetical in between still reads *"Round 7 reproduced all **nine**."*

The duplication is itself the vector: two lists of the same thing in one paragraph is how the third one goes stale. The paragraph's own closing sentence is *"a number stated here is inherited downstream without being re-derived."*

**Fix.** Delete the second enumeration, or fold the longer descriptions into the first. Better, as Round 7 said: render the split from the lettered entries so it cannot go stale a fourth time.

### L2 — The header block says the Status line, the Review-history line and the Disposition are *"hard-coded prose, re-verified by nothing."* All three are now derived, and the line directly above says so.

**Site.** `lpc_Force_Index.md` lines 4 and 8; `gen_force_index.py` line 586.

Line 8: *"**Hard-coded prose, re-verified by nothing:** this whole header block — **including the Status line, the Review-history line, the Revised date and the Disposition** —"*. Line 4, four lines above: *"**Review history, counted from `Review-Artifacts/` rather than typed**"*. Of the four items enumerated, only the *Revised date* is still a literal; the Status line renders `LATEST`, the review-history line renders `HISTORY` and `VERDICT_LINE`, and the Disposition renders `NWORD`, `LATEST`, `LATEST_FIX_PASS`, `_VC[LATEST]` and `FIXPASS_NOTE`.

The error is in the safe direction — the file under-claims — but this is the paragraph whose entire purpose is stating precisely which claims are re-verified, it was *"made exhaustive at Round 3's NEW-M3"*, and a future editor told those lines are re-verified by nothing may reasonably hand-edit them in a file whose next line says *"Never hand-edited."*

**Fix.** Move the Status line, the Review-history line and the Disposition into the derived list and leave the Revised date in the hard-coded one.

### L3 — The generator's own header comment describes the notice pattern more broadly than it implements, in the sentence a future fix pass will read to decide the class is closed.

**Site.** `gen_force_index.py` line 37.

> *"The pattern is now OPEN: any bracketed capitalised tag followed by **a comma or a dash** is a notice."*

`_SEP` requires a comma **followed by a four-digit year**, whitespace followed by a four-digit year, or an **em** dash. A comma alone does not qualify, a bare hyphen does not, an en dash does not. This is the mechanism of **H1** stated as though it were absent. Listed separately because the fix is a comment edit and should not wait on the code fix.

### L4 — Round 7's L2 is untouched: Doc_08 §9's hand-typed cell distribution and its *"— fifteen"* connection certification are read by nothing.

**Site.** `Doc_08_Forces_Document.md` §9; `gen_force_index.py` (absent).

I rewrote §9 to *"1A (5), 1B (1), 2A (4), 2B (5), 3A (1), 3B (1) = **17 forces**"* and *"Cross-cell connections documented in Section 4 — **nine**"*, both flatly contradicting the document's own matrix and table, and regenerated. **Exit 0, no output of any kind.** The Index prints the correct derived distribution and *"15 connections"* beside a §9 asserting different values.

§9 remains the one place Doc_08 restates a derived relation by hand with no cross-check. §3's gravity prose has one (§6), §7's confidence list has one (§7). **Four lines in the same idiom close this and M1 together**, which is why Round 7 recommended folding them; I repeat the recommendation rather than inventing a new one.

### L5 — `argv[1]` is still an unguarded positional override. `python3 scripts/gen_force_index.py --help` dies in a raw `FileNotFoundError` traceback.

**Site.** `gen_force_index.py` line 20.

Round 7's other limb **is** closed — `ROUNDS[-1]` now occurs exactly once, at line 179, guarded by `if ROUNDS else 0`, and the Disposition renders from `_VC[LATEST]` rather than calling `verdict_counts` a second time. This limb is not: `BASE = pathlib.Path(sys.argv[1]).resolve()` accepts anything, so a mistyped flag resolves to a nonexistent directory and the script dies with a traceback naming a path the user never typed. It fails safe — nothing is written — and it is documented in the Index's regenerate line. Still a small trap in a file this careful.

**Fix.** A named `--base` with `argparse`, or `if not SRC.exists(): sys.exit(f"no Doc_08 at {SRC}")`.

### L6 — `assert_notice_coverage` and `strip_notices` operate on different units, so the guard evaluates spans the stripper cannot produce, and all three of its branches emit the same message.

**Site.** `gen_force_index.py` lines 70–71 against lines 99–105.

`strip_notices` splits on `\n` and applies `NOTICE` per line. `assert_notice_coverage` applies `NOTICE.finditer` to the whole text with `re.S`. A match that crosses a newline is therefore judged by a guard that the stripper would never have made — which is conservative and fine — but the FATAL always reads *"spans a structural marker … missing its own terminator and is consuming real source"* whichever of `swallowed`, `STRUCTURAL` or `len > 3000` fired. Two of my **M4** mutants produced that message with no notice present and no structural marker in the span.

**Fix.** Name the branch in the message; scan line-by-line in the guard as well, so guard and stripper see the same spans.

---

## COSMETIC

### C1 — `KNOWN_TAGS` has seven entries; the comment two lines above says *"The **five** known tags are kept only for the error messages."*

`gen_force_index.py` lines 38–39. `CORRECTION` and `SUPERSEDED` were appended by the Round 7 fix pass and the count above them was not updated. Nothing turns on it — the tuple is only interpolated into a FATAL message — but it is the same class of stale literal the file spends sixty lines warning about, in the file that warns about it.

---

## Job 2 — the ten controls, reproduced

| Control | Claim in Index §6 | My result |
|---|---|---|
| **(A)** Regression at `9eccc532` | three §3/§5 divergences, three stubs | **Confirmed exactly.** Recovered the pre-fix Doc_08 from git; emitted three contradiction rows — `1B-1`/G2, `2A-1`/G8, `2B-1`/G7 — and three STUB rows — `2B-5`, `3B-1`, `3B-2` — with *"3 force(s) MISSING a Layer 2."* |
| **(B)** False denial → contradiction row | positive | **Confirmed.** Added *"Neither §5's G6 list nor its G7 list carries it"* to 2B-1's Layer 3; emitted `` `2B-1` | **G6** | **Contradiction** — §3 Layer 3 asserts §5 does NOT carry this `` |
| **(C)** Notice injection, **six tag forms** | positive; lowercase halts | **Confirmed, all six.** `[CORRECTED, …]`, `[CORRECTION, …]`, `[Added, …]`, `[ADDED 2026-…]`, `[NOTE — …]` all strip and `3A-1` does not reach `G6`; `[correction, …]` halts on `DETECT`. **The claim is accurate as written — and see H1 for what it does not cover.** |
| **(D)** Omitted connection → contradiction row | positive | **Confirmed.** Removed `2B-1` from §5's G6 list; emitted `` **Contradiction** — §3 Layer 3 asserts this connection; §5's list omits it `` |
| **(E)** Layer-3 claim §4 does not carry | positive | **Confirmed.** Added *"This force connects to 3A-1 directly"* to 1B-3's Layer 3; emitted *"**1 disagreement(s):** `1B-3` names `3A-1`, §4 does not pair them."* |
| **(F)** `**Heading. [TAG …]**` stripped | positive | **Confirmed.** `**Note. [ADDED, 2026-09-15 — restored **3A-1**.]**` strips; `G6` stays at 3. |
| **(G)** Over-consumption halts | negative | **Confirmed.** A terminator-less `**[ADDED, 2026-09-15 — …` before `**2B-1**` exits 1. The `swallowed` test is doing the work; see **M5** for the two described tests that are not there. |
| **(H)** Review-status claim halts | negative | **Halts on four of my ten mutants and passes six.** See **M2**. Also **compels a false claim**; see **M3**. |
| **(I)** Cell/ID agreement halts | negative | **Confirmed.** `#### Force 3A-1:` → `3B-3:` exits 1 with *"3B-3 under CELL 3A"*. |
| **(J)** §4 row fails to parse → halts | negative | **Halts on the de-bolded source ID only.** Three other one-character slips pass silently and produce the exact outcome (J) names. See **M1**. |

**The count and the split are right: ten, one regression, five positive, four negative.** I re-derived it from the exit codes rather than from the paragraph.

### The three results the brief asked for, all obtained

- **A false force-gravity connection** — ten notice forms, two of them live in this world's build record. **H1.**
- **A wrong count** — one missing trailing pipe. **M1.**
- **A false review-status claim** — a revision round reported as `CLEARED` in the Disposition, and a verdict lifted out of a code fence. **H2.**

### Computations without outputs, outputs without live computations

Round 7 found three of the latter. I audited every derived value in the render block against its computation.

- **No computation without an output.** Round 6's deleted `xc_mismatch` output block is restored and live (I confirmed it fires, control E). `disconnect_claims`, `l3claims`, `s7_missing`, `s7_conflict`, `_misfiled`, `_iso`, `_coin`, `FIXPASS_NOTE`, `LATEST_FIX_PASS` and `VERDICT_LINE` are all computed and all rendered or asserted.
- **Four outputs without live computations**, all reported above: *"emphasis-dense"* and *"plus the force-ID pattern"* (**M5**), *"hard-coded prose, re-verified by nothing … the Status line, the Review-history line … and the Disposition"* (**L2**), and *"The window now ends at the next heading — a structural bound rather than a number chosen by eye"*, which is true of the counts and false of the verdict in the same function (**H2**).

### Reproducibility from an arbitrary working directory

**Confirmed.** Copied the world folder to a scratch path, ran the generator from cwd `/`, diffed: **zero bytes different**, md5 `268fd7ef81265047b671f09d26d919ff` on both. `BASE` resolves from `__file__`; no session path is baked in. I repeated the unmutated run before each mutation batch as a control and it reproduced the committed file every time.

---

## Checks I confirmed before trusting, and my own defective ones

**The brief is right that a failing check in this build is more often defective than the document is wrong, and it caught me twice.**

**Two defective checks of my own, both disclosed:**

1. **My control-(E) assertion was wrong and briefly made (E) look like it produced six findings.** I searched the emitted Index for the substring `disagreement`, which matches the §6 explanatory prose and the header block as well as the finding line. It reported *"6 rows matching"* on a run where the real answer was one. **Had I reported it, it would have been a fabricated finding of exactly the recital shape this generator exists to prevent** — a match belonging to commentary, counted as a finding. I re-ran it anchored on the *"Cross-cell cross-check"* line and the true result is one disagreement, correctly formed. The parallel with Round 7's own disclosed defect is close enough to be worth stating: **a substring search over a file that discusses its own findings will find the discussion.**
2. **My first control-(H) harness crashed on a missing anchor** because I wrote the claim string with markdown emphasis in a place Doc_08 does not use it. That was a harness bug, not a finding, and it is the reason I made the harness assert on anchor-not-found rather than silently no-op — a silent no-op would have reported *"(H) passes"* on a mutant that was never applied, which is the most dangerous false negative available in this setup.

**Confirmations I ran before reporting:**

- **H1 confirmed two ways.** Eleven end-to-end mutant runs *and* direct evaluation of `NOTICE.search` / `DETECT.search` on each string outside the generator. The two methods agree on all eleven, including the positive control (the house form matches both). Separately, the census that says `[FURTHER CORRECTION, Round 9.]` is live was run against `World-Builds/` directly and I opened `lpc_Decision_Log.md` lines 678 and 696 and read them.
- **H2 confirmed two ways.** For each mutant I read the modified artifact back and identified by hand what its verdict section states, then compared to the emitted line — rather than trusting the emitted line to tell me what it parsed.
- **M1 confirmed two ways.** The exit banner's connection count *and* an independent count of the `| \`` data rows the Index's §4 table actually prints (19 vs 20 vs 21), plus a check that Doc_08 §9 still says *fifteen* in each mutant.
- **The review-history line, confirmed against the artifacts by hand.** I read each of the seven artifacts' own verdict block: Round 1 (4H 5M 3L 1C), 2 (3H 4M 3L 1C), 3 (4H 5M 4L 2C), 4 (3H 3M 5L 1C), 5 (2H 3M 3L 2C), 6 (1H 4M 4L 2C), 7 (2H 5M 5L 1C), all SUBSTANTIAL REVISION REQUIRED. **The Index's derived line matches every one.** Note that two of the seven state their counts with `·` separators and two with commas, and the parser handles both — worth recording, because it means the `\D{1,4}` tolerance is load-bearing.
- **The live Doc_08 is clean under the current stripper.** All 43 notices — 31 `CORRECTED`, 9 `ADDED`, 2 `REVISED`, 1 `MOVED HERE` — are matched and stripped; no legitimate text is swallowed; all 44 `]**` terminators are owned. **There is no wrong value in the committed Index.** H1, H2, M1 and M2 are all defects in the breadth of a guarantee, not in the delivered text, and I say so as plainly as I state the findings.
- **The harness itself.** Every batch began with an unmutated copy that reproduced the committed Index byte-identically, so a difference is always attributable to the mutation.

---

## Is the deliverable adequate to proceed to Doc_09?

**The forces analysis is, without qualification.** I did not re-open it, the brief told me not to, and nothing I found gave me a reason to. **Fourth consecutive round with no HIGH against the analysis.** What Doc_09 needs from this pair is the force→gravity grounding and the transmission findings, and I confirmed the derived side of both mechanically: all eight gravities connect with no empty row, all seventeen forces carry a written Layer 2 under the stub test, the two dedicated transmission forces are present in 2B and 3B, §7's hand-maintained confidence list agrees with §3 at all seventeen, and the §3/§5 and §3/§4 cross-checks both report clean against the live text. **Begin Doc_09.**

**The pair should still not go to the project lead for disposition**, for one reason and it is narrow: **the Index's Disposition section can state a false review status** — a revision round reported as cleared — and the Disposition is the section a disposition decision is read from. That is **H2**, it is one line of code, and it is the only thing on this list I would call blocking. **H1** is the more important finding for the build's long-run integrity but it is latent: the delivered Index is correct today and the exposure is to the next notice someone writes.

**I looked hard for a reason to say MINOR REVISION and I want to say why I could not.** Round 7's two HIGHs are genuinely closed — properly, structurally, and at the mechanism rather than at the quoted sites — and a large part of its MEDIUM and LOW list closed with them. If this round had found only M1–M5 and the LOWs I would have said MINOR REVISION without hesitation, and I drafted that verdict before running the verdict-recital mutant. What stopped me is that **a round returning SUBSTANTIAL REVISION REQUIRED can be printed as `CLEARED` in the Disposition, exit 0**, and that **`[FURTHER CORRECTION, Round 9.]` — a form with five live occurrences in this world's own build record — still injects a false gravity connection**. Those are the two failure modes this generator exists to prevent, and neither is a judgement call.

---

## CO-022 escalation assessment

**Category 1 — Representative identity, title, or voice: does not apply.** Nothing under review this round makes an identity, title or voice decision. Doc_08's own assessment says so and is correct.

**Category 2 — Portfolio-level or cross-world: Doc_08's four items stand; the fifth is still missing, now for the third round.** I did not re-audit the four (out of scope), but I confirm the one that touches the generator. **The index-generator item Round 5 raised, Round 6 restated as L4, Round 7 restated a third time, and `lpc_Decision_Log.md` line 1269 records as *"Carried at the Disposition"*, is still not in Doc_08's CO-022 assessment.** I restate it a fourth time so it is not lost again: *index generators are build artifacts; the portfolio has no convention for where they live, whether they are deliverables in their own right, or whether a regenerated index must be diffed before commit.* **Not decided here.**

**I second Round 7's candidate, and this round supplies the evidence that turns it from a candidate into an item.** *Provenance-notice syntax is a cross-world convention with no owner.* Round 7 raised it on the ground that four tags are in use across `World-Builds/`. **The Round 7 fix pass responded by abandoning tag enumeration entirely — which was the right instinct — and the defect immediately reappeared on the separator axis**, because `[FURTHER CORRECTION, Round 9.]` and `[SUPERSEDED, Round 9: …]`, both live in this world, use a comma-and-round-number where the pattern expects a comma-and-year. **A build-authored script that must distinguish correction notices from source text has no specification to code against, and two consecutive fix passes have now guessed at one and been wrong.** That is a portfolio question with a demonstrated cost, and it will recur in any world that derives an index from marked-up prose. **Not decided here; recorded for the project lead with the evidence attached.**

**Category 3 — Governance or methodology: Doc_08's five items stand; I add nothing and subtract nothing.** Out of scope this round; the three-way divergence on the Forces Framework's three-layer rule and the undefined **Construction-record notes** block are correctly carried at §8.

**Category 4 — Unresolved tensions: one open**, the 411 *Gesta*. Not re-assessed; no generator control touches it.

**Never self-assigning Frozen status: observed.** Neither deliverable self-certifies, neither claims Frozen, and the Index's Disposition says *"Not disposed … Not self-certified. Not Frozen."* Eight rounds, held every time. **I note with some weight that H2 is the finding that could break this**: a Disposition rendering `CLEARED` from a misparse is self-certification arriving by accident rather than by claim, and it would be printed in the sentence that currently says the opposite.

---

## Known interactions — mentioned, not graded

1. **Committing this artifact puts eight files in `Review-Artifacts/` against a Document Log naming seven**, so `assert_doc08_round_count` will halt the generator until the next fix pass updates Doc_08. **That is the guard working as designed** and Rounds 6 and 7 both flagged the same window. I confirmed the exact behaviour by building an eight-artifact sandbox: it halts, and it names each disagreeing site rather than the first — a genuine improvement over the Round 6 version. **I add one warning that is not decorative:** the guard will also demand that Doc_08's two *"REVISED after Round 7"* sites be changed to *"Round 8"*, and **there will be no Round 8 fix pass at that moment**. Making that change to satisfy the guard installs a false review-status claim. **Fix M3 before, or at the same time as, updating the round count** — otherwise the guard walks the next fix pass into exactly the defect Round 6's H1 was.
2. **`verdict_counts` anchors on `## VERDICT` at line start.** This artifact's only line-start occurrences of that string are its own two real headings, top and bottom, both carrying the verdict. I have deliberately written every discussion of the parser without putting the bare heading at line start, including inside code blocks — see **H2**, where the fenced-quote route is the finding, and where I say that having to do this is the argument rather than the remedy.

---

## On the brief that commissioned this review

Per the instruction not to inherit its claims, I checked them. **No corrections. Three confirmations — the first brief in this sequence I found nothing wrong with.**

1. **"The Index now advertises ten controls: one regression (A), five positive (B–F), four negative (G, H, I, J) that halt the run." Confirmed, by reproducing all ten and reading the exit codes**, not by reading the paragraph. Round 7's L1 said the split had been wrong three times and had travelled into two consecutive briefs; **that propagation has stopped.** The only residue is that the Index's own paragraph enumerates the controls a second time and omits (J) — recorded as **L1**, and the brief did not inherit it.
2. **"HIGH counts: 4, 3, 4, 3, 2, 1, 2 — all SUBSTANTIAL REVISION REQUIRED." Confirmed exactly**, read off each artifact's own verdict block by hand and matching Doc_08's Document Log row for row.
3. **"Rounds 5, 6 and 7 all judged the forces analysis adequate to proceed to Doc_09." Confirmed**, and at each round's own strength: Round 5 *"The analysis is. The certification is not."*; Round 6 *"without qualification"*; Round 7 *"without qualification, and I did not need this round to establish it."* The brief does not overstate it.

**And its four specific pointers all did work, which is worth recording because it is the reason this round found anything.** *"Re-run Round 7's exact defeating scenarios, then try to defeat the new versions"* is what let me close H1's first limb honestly instead of assuming, and then find the second. *"What legitimate text does the open pattern now swallow?"* produced **M4** and, more usefully, the finding that over-stripping **cannot** be silent on this document because every terminator is owned — which is a credit to the code that I would not have established otherwise. *"Find a way to drop or duplicate a connection without tripping the §4 guard"* is **M1**, and I would not have looked at the trailing pipe without it. *"Does any control's computation exist without its output, or any output without a live computation?"* is how I found the half-fixed window claim that became **H2**.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**2 HIGH, 5 MEDIUM, 6 LOW, 1 COSMETIC.**

**What I tested hardest, and what I would tell the next round.** I spent most of this round on the notice channel and on `verdict_counts`, because those are where Round 7's HIGHs were and because the brief was right that they are where a false connection and a false review status get in. **The notice channel is better than it was and still open**: the tag list is gone, the detector is genuinely non-circular, and the fix then recreated the same closed-list defect one field to the right. **`verdict_counts` is half fixed for the third consecutive round**, and the half that was left is the half that writes into the Disposition. **The §4 guard is new, real, and narrower than its sentence.** Everything else I found is wording that outruns code, which this file is unusually good at diagnosing in retrospect and has not yet learned to catch in prospect.

**The honest shape of it:** this is not an eighth round of the same verdict. Round 7's two HIGHs are closed at the mechanism, seven of its thirteen findings are closed, the Index reproduces byte-identically from anywhere, and **the forces analysis has been clear for four rounds running.** What remains are two demonstrated ways to put a false statement into a delivered file, both mechanical, neither touching the analysis. **Fix H2's one line and H1's separator set and I would expect the next round to clear this.**

*Simulated review — informational only, not an Article 31 substitute.*

*End of Round 8 review.*
