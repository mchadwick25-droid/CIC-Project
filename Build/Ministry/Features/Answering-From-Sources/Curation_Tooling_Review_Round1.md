# Curation tooling (expected_gaps reasons): review, round 1

Reviewer: Opus 5.5. Subject: PR #1343, merge commit 83f18f30f (parent 8eda5a31f). Files: `Sandbox/answering-library/answering_library/curation.py`, `curate.py` (docstring), `tests/test_curation_tooling.py`, `Curation_Howto.md`, `Curation_Tooling_ExpectedGaps_Report.md`.

Line numbers below are in `curation.py` as it stands on main after the merge.

## Verdict

Blocking findings listed (4). The tooling does not yet meet brief item (1): a damaged printed numeral can still be excused, in three separate ways, and one false positive on a real file has no honest way to be accounted for.

## What was run

- `pytest tests/test_curation_tooling.py tests/test_curation.py` with main's code: 91 passed.
- Probes built with the tests' own `make` helper and `cu.resolve`, on the inputs given in each finding.
- `curate check acta-martyrum-selecta_gebhardt1902` with main's code and the yaml of commit a330439be: fails, and lists line 3729 (`25 VIL Καὶ μετ’ ὀλίγας…`) and line 3671 (`xxi χκαταγαγών…`). The same holds with `reason: {leaf_missing: {between: [3637, 3821]}}` added.
- Old against new look-alike set on `augustine_doctrina-christiana-enchiridion-lat_bruder1838` (finding 3).
- The before/after comparison of the report, on 13 of the 52 files with the parent's code and main's code: acta-martyrum-selecta_gebhardt1902, possidius_vita-augustini_weiskotten1919, augustine_doctrina-christiana-enchiridion-lat_bruder1838, optatus_against-the-donatists, koch_cathedra-petri-deu_1930, augustine_retractationes-lat_knoll-csel36, augustine_civitate-dei-1-13-lat_hoffmann-csel40-1, augustine_epistulae-1-123-lat_goldbacher-csel34, augustine_sermones-1-340-lat_migne-pl38, bardenhewer_geschichte-altkirchlichen-literatur-band2-cyprian-slice-deu_2e-aufl1914, duchesne_histoire-ancienne-de-leglise-tome3-fra_2e-ed1910, koch_cyprian-und-der-roemische-primat-deu_1910, monceaux_histoire-litteraire-afrique-chretienne-tome3_1905. Exit codes are the same for all 13. The look-alike counts match the report: Gebhardt 63 in 2 warnings to 59 in 1 (dropped lines 3729, 4043, 5132, 5558); Possidius 4 in 2 to 0; the other 11 are unchanged. Apart from the hand-listed warning, the output is the same line for line.

## Checked and correct

- Window bounds. `range(max(before, h_end), e["line"] - 1)` covers exactly the lines strictly between the neighbours. A damaged head on the line right after the previous reading, or right before the entry, is found.
- Backward and repeat steps. The window runs from the previous readable reading to the entry. A damaged head inside it is found (`SERMO I / SERMO Il / SERMO I` and `III / Vl / II` both fail).
- Several entries in one series. Each entry is checked against its own neighbours. A gap step whose window holds a damaged head still fails while a later clean entry passes.
- Group restart. `previous_lines` and `series_anomalies` both reset when the group changes. An entry that names a neighbour from the earlier group fails with the right neighbours named.
- Apparatus ranges. These are 0-based on both sides of the comparison (`load`, line 407, and the scan).
- Odd yaml. A reason that is null, a string, a list, a float line or has unknown keys gives a `CurationError` (exit 2). Nothing crashes.
- The hand-listed warning: the counts per kind, the detail lines underneath, and the skip for fixed lines all behave as the Howto says.
- Code discipline: the new code and tests carry docstrings only. They hold no process narration or change history. No yaml was edited.

## Blocking findings

### 1. `edition_unnumbered` can name the damaged head itself

`_reason_problems`, lines 1036–1040, checks only that the quote is on line N and that N lies between the neighbours. `_hidden_heads`, line 1053, then takes N out of the scan. Nothing checks that line N really lacks a numeral.

- Failing input. Lines `["SERMO I", "t", "SERMO Il", "t", "SERMO III"]`. Rule `^SERMO (?P<n>[IVX]+)$`. Entry `{series: s, line: 5, quote: 'SERMO III', reason: {edition_unnumbered: {line: 3, quote: 'SERMO Il'}}}`. Result: no problems. The damaged II is excused by a quoted line, which is the case brief item (1) exists to stop.
- On the real file. With Gebhardt at a330439be and `reason: {edition_unnumbered: {line: 3729, quote: '25 VIL'}}`, line 3729 drops out of the failure. The check still fails only because the false positive at 3671 remains (finding 4).
- Correct behaviour. When the rule's loosened pattern matches line N with a token in the numeral position, an `edition_unnumbered` reason naming N fails, and N stays in the scan.

### 2. A reading the series could not read is taken as a neighbour-free stretch

A numeral that `to_int` cannot read has value None. `previous_lines` (line 608) skips it, so the gap is measured from the reading before it. The rule's pattern matches the line, so `_lookalike` returns None. The unreadable numeral is never a look-alike, and an unread reading is only an `info` line, never a problem.

- Failing input. Rule `^SERMO (?P<n>[IVXLCl1]+)\.`, locus `sermo{n}`. Lines `["SERMO I. a", "t", "SERMO IlX. b", "t", "SERMO III. c"]`. Sequence `[(1, 1), (3, None), (5, 3)]`. Entry at line 5 with `leaf_missing: {between: [1, 5]}`. Result: no problems.
- Correct behaviour. A reading of the series between the neighbours whose value is None is an unaccounted look-alike, and the entry fails. A reading the series could not read is a damaged printed numeral, not a missing leaf.

### 3. The shape filter drops most of the real damaged heads in Bruder 1838

`_numeral_shaped` (line 581) admits only `IVXLCDMivxl`, digits, `|`, `!`, a few Greek and Cyrillic look-alikes and the rule's `ocr_map`. On `augustine_doctrina-christiana-enchiridion-lat_bruder1838` the five rules share one pattern, `^(?:Caput|[CGO0]\.) ?(?P<c>[IVXLCl1]+)[.,]?\s`. Over the body, the unshaped look-alike test finds 41 lines and the shaped test keeps 8 of them, so 33 are dropped. They are real chapter heads, for example:

| Line | Text |
|---|---|
| 1991 | `C. \T. Diximusnc aliquid…` |
| 2724 | `C. XWI. (^uapropter…` |
| 3942 | `C. XVH. Non enim audiendi…` |
| 4343, 5960, 8694 | `C. XXVT. …` |
| 5310 | `C. \T1. Et si quando…` |
| 5499 | `C. XU. Quae autem…` |
| 5975 | `C. XXVTI. Quando autem…` |
| 7640 | `C. XY. Agit itaque…` |
| 8820 | `C. XXVTII. Talis doctor…` |
| 9751 | `C. XXU. Porro autem…` |
| 10905 | `C. IjXI. Haec ergo…` |
| 11637 | `C. LXXXn. Xam et ipsa…` |
| 12390 | `C. CVUI. Nam neijue…` |

The other dropped tokens are `XFil.`, `IV^.`, `XV\`, `XXV^`, `XXVHl.`, `XXV'11.`, `XV''!!!.`, `XIjV.`, `\LV`, `IjII.`, `LVHl.`, `IjXVI.`, `LXXX[.`, `rjXXXni.`, `TjXXXIV.` and `LXXX^'!!.`. All of them substitute T, H, U, Y, W, F, j, n, r, `\`, `^`, `'` or `[` for numeral strokes. The 8 kept are `ill.` (2), `Vil.`, `Xil.`, `XXXV'.`, `iV.`, `Vill.` and `XXiX.`.

If any step in this file were excused with an `expected_gaps` entry, 33 of these heads could lie in its window unseen. Probes on the tests' own rule show the same misses: `Hl`, `XIj`, `IX*`, `VII)`, `[VII]`, `XVÌ` and lowercase `cxl` are not flagged.

Correct behaviour. Each of the 33 lines is reported when it lies between an entry's neighbours. One way to get there: apply the shape test only where the loosened numeral group is the line's first token. Where the pattern puts a literal head word (`Caput`, `C.`) before the numeral, that word already makes the line a head and needs no shape test. Another way: widen the admitted set to the substitutions above. In either case, add a test built from these Bruder lines.

### 4. A false-positive look-alike has no honest way to be accounted for

Line 3671 of Gebhardt (`xxi χκαταγαγών us…`) is Greek body text. Lowercase `x` and `i` are in `_NUMERAL_LETTERS`, so `xxi` passes as numeral-shaped against the uppercase-only pattern `^(?:\d{1,2} )?(?P<c>[IVX]+)[.,]? `.

The scan offers only three ways to account for a line, and each one records something false about a non-heading:

- a `fix` with a quote, which makes the line a heading of the rule;
- `edition_unnumbered`, which asserts the edition prints a head there;
- `counterpart`, which needs the line to be a head.

The language guard does not help: the line is Greek and the rule is the Greek rule. Furniture and apparatus would remove or relabel body text. The report's "Limits" section tells curators to use exactly these routes for such a line. Following that advice writes an invented heading into a curation record, which CLAUDE.md's "never invent" forbids.

Correct behaviour. There is a verifiable way to say "this line is not a heading", with a line and a quote on that line, for example extending `not_subheadings` or adding an equivalent list that the scan honours. Separately, the filter should not admit lowercase letters for a rule whose numeral class is uppercase and whose flags are case-sensitive, unless `ocr_map` names them. Until then, the report's advice should be withdrawn.

## Non-blocking findings

5. **`counterpart` verifies almost nothing (medium).** Line 1033 accepts any division start or any line of any series anywhere in the file, including the step's own previous reading. The test at `test_counterpart_must_be_a_division_or_matched_head` asserts `counterpart: {line: 1}` passes. The Howto says "a head the series read", but the code accepts heads of every series (line 975). An explicit division declared on a damaged head also lets `counterpart` name it and take it out of the scan. Correct behaviour: the counterpart line is a head of a different series or a division in the other language, and it lies within or next to the step's window.
6. **Fixes of another rule cover a line (low).** `fixed_lines` (line 826) holds every fix of every rule. A forced fix (with a quote) on an unrelated rule therefore removes a damaged head of the series from both the hand-listed warning and the gap scan. Failing input: the finding-1 lines, plus rule `{id: p, pattern: '^ZZZ (?P<x>\S+)$', fixes: [{line: 3, quote: 'SERMO Il', set: {x: '1'}}]}`, plus `leaf_missing: {between: [1, 5]}`. Result: no problems. For the gap scan, only a fix of a rule of that series should count.
7. **YAML booleans pass as integers (low).** `isinstance(True, int)` holds, so `line: true` or `between: [true, 3]` loads as line 1 (lines 198 and 203). The same is true of the entry's own `line`, which predates this PR. Correct behaviour: reject `bool`.
8. **The Howto leaves out three behaviours (low).** The scan also skips header lines and lines outside the rule's language guard. For a named explicit-division series that is not a rule id, the scan covers every rule with `number`, not only those of the `divisions` series.
9. **A dropped stroke that leaves a valid numeral cannot be detected (information).** Example: `II` printed where `III` was meant. The repeat can be excused with `as_printed` and the following gap with `leaf_missing`. No text check can tell this from a real repeat, so the Howto's limits should say so.
10. **CI does not run these tests (information, existing).** CI does not run `Sandbox/answering-library/tests`. The report says so for the checker. It holds for these tests as well.
11. **Duplicate character (trivial).** `Ι` appears twice in `_NUMERAL_LETTERS`.

## Report claims

The figures in the report are accurate on the 13-file sample, and the Gebhardt rerun reproduces as described. The "Limits" advice on line 3671 is wrong (finding 4). The report does not mention that the shape filter misses most of the damage in Bruder 1838 (finding 3).
