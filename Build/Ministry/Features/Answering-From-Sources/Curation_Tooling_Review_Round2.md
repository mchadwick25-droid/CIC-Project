# Curation tooling (expected_gaps reasons): review, round 2

Reviewer: Opus 5.5, a different reader from round 1. This is a targeted recheck against the round-1 findings in `Curation_Tooling_Review_Round1.md`. Subject: PR #1346, branch `claude/curation-tooling-round2`, head 14b4f6736. Files: `Sandbox/answering-library/answering_library/curation.py`, `tests/test_curation_tooling.py`, `Curation_Howto.md`, `Curation_Tooling_ExpectedGaps_Report.md`. No yaml is changed.

Line numbers below are in `curation.py` at 14b4f6736.

## Verdict

Blocking findings listed (4). Round-1 findings 1 and 2 are fixed for the inputs round 1 gave. Findings 3 and 4 are fixed for Bruder 1838 and for Gebhardt line 3671. But the new `not_headings` key can hide a real damaged head, including Gebhardt line 3729, and the new shape rule both drops real damaged heads that main finds and floods the scan on files whose patterns allow free tokens before the numeral.

## What was run

- `pytest tests` at the PR head, without `test_union.py` and `test_shelf_row_pointers.py`: 186 passed. The tests ran from an exported copy, with `cic/texts` linked read-only.
- `curate check` on all 52 curated files with main's code and with the PR head's code. Exit codes are identical: 32 exit 0, 20 exit 1. The printed output is byte-identical for all 52. This matches the report. No curation file has `expected_gaps` or `not_headings` yet, so these runs do not exercise the new code.
- Probes built with the tests' own `make` and `step` helpers and `cu.resolve`, on the inputs given in each finding.
- Gebhardt (`acta-martyrum-selecta_gebhardt1902`) with the yaml of commit a330439be and four variants of its `expected_gaps` entry at line 3821.
- Old against new look-alike sets over the whole body of every curated file, for every rule with `number`: main's `_lookalike(..., shaped=True)` against the head's `_lookalike(..., shaped="lead")`, and both against the unshaped test.

## Round-1 findings: status

| Round 1 | Status | Evidence |
|---|---|---|
| 1. `edition_unnumbered` names the damaged head | Fixed for the round-1 inputs; one bypass remains (blocking B) | `SERMO Il` named by the whole line or by `Il` alone: fails, and line 3 stays in the scan. Gebhardt `edition_unnumbered {line: 3729, quote: '25 VIL'}`: exit 1, 3729 refused and still listed. The named line inside an apparatus range is still refused. Two entries in one series: the first still fails while the second passes. A rule whose hand list leaves the line out: still refused. |
| 2. An unread reading is taken as a stretch with no neighbour | Fixed in the scan; `not_headings` can hide it (blocking A) | Round-1 input: fails. `previous_lines` now counts the unread reading as the neighbour, so `between: [1, 5]` is refused and `[3, 5]` fails on line 3. Two unread readings in a row: fails. `edition_unnumbered` naming the unread line: refused. |
| 3. Shape filter drops Bruder's damaged heads | Fixed for Bruder; regressions elsewhere (blocking C and D) | Bruder, every rule: unshaped 248 whole-file look-alikes, new 248, unshaped minus new 0. Main's shaped test kept 200 of the 248 over the whole file. All of `C. \T.`, `C. XVH.`, `C. IjXI.`, `C. XWI.`, `C. LXXX^'!!.` and the rest of the round-1 table are found. |
| 4. Line 3671 has no honest way out | 3671 is no longer flagged; `not_headings` is unsafe (blocking A) | Gebhardt with `leaf_missing` alone: fails on 3729 only. A `not_headings` entry for 3671 now fails as stale. |
| 5. `counterpart` verifies almost nothing | Fixed; now refuses its own documented case (non-blocking E) | Own-series reading, the entry's own line, and a division far from the step all fail. |
| 6. Fixes of another rule cover a line | Fixed | `fixed_lines` is gone. The hand-listed warning uses `rule.fixes` (line 862); the gap scan uses the fixes of the series' own rules (`_hidden_heads`). The round-1 input now fails on line 3. |
| 7. YAML booleans pass as integers | Fixed | `_is_int` rejects `bool` for the entry's `line`, `between`, a reason's `line` and a `not_headings` line. All give `CurationError`. |
| 8. Howto leaves out three behaviours | Fixed | Header lines, the language guard and the non-rule-id series are now in the Howto. |
| 9. Dropped stroke that leaves a valid numeral | Documented | Stated under Limits in the Howto and the report. |
| 11. Duplicate `Ι` | Fixed | `Ι` appears once in `_NUMERAL_LETTERS`. |

`not_headings` schema: a string line, a missing quote, an unknown key, line 0, a non-list value and a bare string entry each give `CurationError` (exit 2). A quote that is not on the line fails. A line outside the file fails. A stale entry fails.

Code discipline: the new code and tests carry docstrings only. They hold no process narration or change history.

## Blocking findings

### A. `not_headings` hides a real damaged head and an unread reading

Lines 1007 and 1028 drop every look-alike whose line is listed in `not_headings`. The only checks on an entry (lines 1035–1041) are that its quote is on the line and that some scan reported the line. Nothing checks that the line is not a head.

- On the real file. Gebhardt at a330439be, the line-3821 entry given `reason: {leaf_missing: {between: [3637, 3821]}}`, plus `not_headings: [{line: 3729, quote: '25 VIL'}]`: `curate check` exits 0. Line 3729 is `25 VIL Καὶ μετ’ ὀλίγας ἡμέρας…`, the damaged head VII.
- Failing input. Lines `["SERMO I", "t", "SERMO Il", "t", "SERMO III"]`, rule `^SERMO (?P<n>[IVX]+)$`, entry at line 5 with `leaf_missing: {between: [1, 5]}`, `not_headings: [{line: 3, quote: 'SERMO Il'}]`. Result: no problems.
- Failing input, unread reading. Rule `^SERMO (?P<n>[IVXLCl1]+)\.`, lines `["SERMO I. a", "t", "SERMO IlX. b", "t", "SERMO III. c"]`, entry at line 5 with `leaf_missing: {between: [3, 5]}`, `not_headings: [{line: 3, quote: 'IlX'}]`. Result: no problems. The line is a reading of the series itself.
- Correct behaviour. A `not_headings` entry fails when its line is a reading of any series, or when the token at a series' numeral position is numeral-shaped under the strict test, the same one `_carries_numeral` applies to `edition_unnumbered`. The entry is then open only to a line flagged through a head word with a token that is not numeral-like, for example `C. Iulius`. Add tests with 3729 `25 VIL` and with an unread reading.

### B. `edition_unnumbered` and `counterpart` can still name a head that the scan reports

`_carries_numeral` (line 1079) asks `_lookalike(..., shaped=True)`, the strict shape test. The scan (`_hidden_heads`) asks `shaped="lead"`, which skips the shape test when a head word comes first. A line with a head word and a token outside the strict set is therefore reported by the scan but not refused as a reason. `_hidden_heads` then takes it out of the scan.

- Failing input. Rule `^(?:Caput|[CGO0]\.) ?(?P<c>[IVXLCl1]+)[.,]?\s` (Bruder's), lines `["C. I. a", "t", "C. X§I. b", "t", "C. III. c"]`, entry at line 5 with `edition_unnumbered: {line: 3, quote: 'C. X§I.'}`. Result: no problems. With `leaf_missing: {between: [1, 5]}` the same line 3 fails as a look-alike.
- Same with `counterpart: {line: 3}` and an explicit division at line 3: no problems.
- Correct behaviour. The reason check and the scan use one test. A line the scan would report as a look-alike of the series cannot be named by `edition_unnumbered` or `counterpart`, and stays in the scan.

### C. Lowercase strokes in a leading numeral are no longer found: real heads that main finds are dropped

`_NUMERAL_LETTERS` (line 48) holds no lowercase letter except `l`. The strokes `i j n r` (line 50) count only when a head word comes first (line 629, `lower_strokes=shaped is True or not leads`). So for a rule whose numeral leads the line, any token with a lowercase `i` or `j` is not a look-alike.

- Failing input. Rule `^(?:\d{1,2} )?(?P<n>[IVX]+)[.,]? ` (Gebhardt's), lines `["I. a", "t", "Vil. Kai body", "t", "IV. d"]`, entry at line 5 with `leaf_missing: {between: [1, 5]}`. Result: no problems. Main reports line 3. The same holds for `VIi.`, `XIi.`, `ill.`, `Xil.`, `iV.`, `Vill.`, `XXiX.`, `XIj` and `IjXI.` as the leading token.
- On the real files, lines main's shaped test reports and the head's does not, whole body. These are printed heads:

| File | Line | Text |
|---|---|---|
| augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910 | 30005 | `Ilil. Contra litteras Petiliani` |
| augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910 | 31480 | `Iill. Contra litteras Petiliani` |
| augustine_de-fide-et-symbolo-de-opere-monachorum-et-al-lat_zycha-csel41 | 1066 | `Illi. DE CONTINENTIA.` |
| augustine_opera-sect-v-pars-iii-lat_zycha1900-csel41 | 6391 | `15 XXilll. Neque enim dictum est…` |
| augustine_epistulae-critical_goldbacher-csel57-pars4 | 4368 | `CLXXXVIIi.` |
| augustine_oeuvres-completes-tome13-donatistes-slice-fra_raulx1869 | 664, 9976, 12864 | `Xlil. Qu'il considère…`, `Vil. On continua…`, `XXXiX. Dès lors…` |
| harnack_vita-cypriani-commentary-lat-deu_1913 | 2742 | `iV. Die Ausführung. 49` |

  In all, 702 rule-line pairs drop out (many are the same line under several rules of one file). Many of the rest are body text such as Gebhardt 3671 `xxi`, which is the intended effect.
- Correct behaviour. A damaged leading numeral with lowercase strokes is still found, while an all-lowercase body word such as `xxi` is not. One way: admit the lowercase strokes `i j l` in a leading token that also holds at least one uppercase numeral letter, and keep refusing a token with no uppercase numeral letter unless the rule ignores case or its `ocr_map` names the letters. Add tests built from the lines in the table.

### D. Any text before the numeral counts as a head word, which floods the scan

`leads` (line 628) is true only when nothing but a margin number comes before the numeral. Any other prefix the loosened pattern matched skips the shape test, and the loosened numeral group is `\S{1,15}`. The Howto says this applies "where a literal head word comes first (`Caput`, `C.`)". The code applies it to every prefix, including the free tokens many patterns allow before the numeral.

- On the real files, look-alike lines the head reports over the whole body that main did not: 430,090 rule-line pairs over all 52 files. Examples:
  - Petschenig, rule `s1`, pattern `^(?:\S{1,3} ){0,2}(?:[A-Za-z1^.]{1,10}[.,:]? ){0,2}(?P<s>\d{1,3})[.,:] ?…`: 13,574 more lines, nearly all body text (`de baptismo Iohannis, quod solet…`, `collegii consortio iungerentur…`).
  - Zycha CSEL 41, rule `s0`: 1,030 more lines (`cem aduersantur, ut non ea…`).
  - Knoll CSEL 33, rule `caput1`: 76 more lines, mostly apparatus (`2] cf. Ps. 85, 11.`).
- Effect. An `expected_gaps` entry on these files would list hundreds of body lines between almost any two neighbours. The only way out is a `not_headings` entry for each one. Given finding A, mass `not_headings` entries are exactly where a real damaged head would go unseen.
- Bruder is not part of this problem: its 248 whole-file look-alikes all begin with `C.`, and they are either damaged chapter heads or table-of-contents lines (`C. 26. Necessaria et commoda…`), which belong in an apparatus range.
- Correct behaviour. The shape test is skipped only when the pattern requires a literal word before the numeral group (`Caput`, `C.`, `SERMO`), as the Howto says. A prefix made only of optional groups or free-token classes does not count as a head word. Add a test with Petschenig's `s1` pattern and a body line.

## Non-blocking findings

E. **`counterpart` refuses the same-shaped head of a parallel series (medium).** `_carries_numeral` applies the series' rules to the named line without their `lines` ranges or language guard. Rules `s` (lines `[[1,1],[4,4]]`) and `g` (lines `[[2,3],[5,5]]`), both `^(?P<n>[IVX]+)\. `, lines `["I. a", "I. a", "II. b", "III. c", "III. c"]`, entry `s` at line 4 with `counterpart: {line: 3}`. Line 3 is a reading of series `g`. Result: refused as "a numeral in the series' numeral position". Main accepts it. In a parallel edition where both languages print the numeral the same way, `counterpart` cannot be used. Correct behaviour: a line that is a reading of another series is not refused for carrying that series' numeral. Whether its value must equal the missing number is a design choice to make.

F. **The report's Bruder figures are accurate, but the report is silent on C and D (low).** "41 and 41" (rule lines) and "248 and 248" (whole file) reproduce. The report does not mention that leading lowercase-stroke heads are dropped in other files, or that the whole-file look-alike count grows by about 430,000 rule-line pairs.

## Report claims checked

- 32 pass and 20 fail on all 52 files, identical to main: confirmed, with identical output.
- Gebhardt `edition_unnumbered {line: 3729}`: exit 1, refused, and 3729 stays in the scan: confirmed. `leaf_missing`: exit 1 on 3729: confirmed. Line 3671 no longer flagged: confirmed.
- Bruder 41/41 and 248/248: confirmed.
