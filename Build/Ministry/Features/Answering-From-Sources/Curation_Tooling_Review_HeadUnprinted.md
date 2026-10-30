# Curation tooling (`head_unprinted` reason): review, round 1

Reviewer: Opus 5.5. Subject: PR #1365, branch `claude/curation-head-unprinted`, head a2081b98b. Files: `Sandbox/answering-library/answering_library/curation.py`, `tests/test_curation_tooling.py`, `Curation_Howto.md`, `Curation_Tooling_ExpectedGaps_Report.md`. No curation yaml is changed.

Line numbers below are in `curation.py` at a2081b98b.

## Verdict

No blocking findings. Three non-blocking notes.

## What was run

- Code and tests exported from the PR head and from origin/main into a scratch folder, with `cic/texts` linked read-only.
- `pytest tests` without `test_union.py` and `test_shelf_row_pointers.py`: 215 passed at the PR head, 209 on main. The difference is the six new tests.
- `curate check` on all 52 curated files with main's code and with the PR head's code. Exit codes are identical: 38 exit 0, 14 exit 1. The printed output is byte-identical for all 52. This matches the report.
- Optatus (`optatus_against-the-donatists`, yaml of origin/main) and Gebhardt (`acta-martyrum-selecta_gebhardt1902`, yaml of commit a330439be), each with variants of the reason, through `curate check --curation-dir`.
- Probes built with the tests' own `make` and `step` helpers and `cu.resolve`.

## Semantics

| Check | Code | Result |
|---|---|---|
| `A` is the previous reading, `B` the entry's line | 1113-1119: `(first, last)` must equal `(before, e["line"])` | `between: [1209, 1307]` on Optatus: exit 1, names the neighbours `[1233, 1307]`. |
| `N` strictly between `A` and `B` | 1135 | `line: 1233` and `line: 1307` (the neighbours) and `line: 1213` (outside): exit 1 each, "is not between the neighbours". |
| Quote on line `N` | 1133 | Correct quote on line 1256: exit 1, "quotes text that is not on line 1256". |
| `N` refused when it carries a numeral | 1148: the shared `_carries_numeral`, the predicate the scan uses. No second test. | Gebhardt `line: 3729, quote: '25 VIL'`: exit 1, reason refused. |
| A reason never removes a line from the window scan | `_hidden_heads` (1166) scans `before` to the entry's line and reads nothing from the reason | Gebhardt `head_unprinted {between: [3637, 3821], line: 3671, quote: 'xxi'}`: reason accepted, exit 1 with line 3729 (`25 VIL`) reported. With `line: 3729`: both the refusal and the scan report 3729. Line 3671 is not reported. |
| Wrong kind | `REASON_STEPS` (50), checked at 1110 | Repeat (new test) and backward step (probe): each fails, "does not explain a ... step; it explains gaps". |
| Malformed reason | `_reason` (193-223) | Missing `quote`, `between` or `line`; `line: true`; an extra key; an empty quote; reversed `between`; `head_unprinted` beside `leaf_missing`: exit 2 in each case. |

## Optatus real file

- Scratch copy of the origin/main yaml with the Book II chapter XXV entry's `leaf_missing {between: [1233, 1307]}` replaced by `head_unprinted {between: [1233, 1307], line: 1257, quote: 'upon whose head thou hast now endeavoured'}`: exit 0, class `curated`, `RESULT: PASS`.
- Line 1257 reads `He, upon whose head thou hast now endeavoured to lay thine hands,212 had, for a long time, been thy fellow and companion.` The quote is on that line.
- Line 1257 lies in division `book-second/ch24` (lines 1233-1306). The next division, `book-second/ch26`, starts at 1307.
- In Ziwsa's Latin (`optatus_libri-vii-lat_ziwsa1893-csel26-tei.txt`), chapter 24 ends `agnoscite uos animas euertisse.` and `<div n="25">` opens `Socius et comes uester iamdudum fuerat, cui nunc manus inferre conatus es`. The English at 1251-1257 runs `You have found deacons, priests, Bishops, you have made them as laymen. Recognise that you have 'overturned souls.'` and then `He, upon whose head...`. Line 1257 is the true start of chapter XXV.

## Tests

The six new tests assert what their names claim:

- `explains_a_numbered_text_with_no_printed_head`: no problem.
- `fails_on_a_missing_quote_a_line_outside_the_window_and_wrong_neighbours`: the quote message, the "not between" message for lines 1 and 5, and one problem naming `head_unprinted` and the entry for three wrong `between` pairs. The "outside the window" cases are the two neighbour lines, so this is the strictness test. The pair `(1, 9)` hits the "outside the file" branch; the assertion accepts any `head_unprinted` message.
- `refuses_a_line_that_carries_a_numeral_and_does_not_hide_it`: both the reason refusal and the scan's look-alike report on line 3.
- `does_not_hide_a_damaged_head_elsewhere_in_the_window`: exactly one problem, the look-alike on line 2; the reason on line 3 is accepted.
- `explains_only_a_gap`: a repeat fails. The backward step is not tested; the probe above shows it fails.
- `needs_all_three_keys`: each of the three two-key bodies raises `CurationError` naming `head_unprinted`.

## Howto and report

- The Howto row for `head_unprinted` matches the code: neighbours as for `leaf_missing`, quote on `N`, `N` strictly between, look-alike test. The example entry is the Optatus case run above and passes.
- The report's 52-file count (38 exit 0, 14 exit 1) and the Optatus replay match the runs above. One curation file has `expected_gaps` (Optatus), as the report says.
- No process narration or change history in `curation.py`, the tests or the Howto.

## Non-blocking notes

1. Gap width is not checked. On `CHAPTER XXIV.` then `CHAPTER XXVIII.` (three numerals missing), one `head_unprinted` naming one body line passes. `leaf_missing` and `edition_unnumbered` behave the same on main, so this PR adds no new hole. A gap of more than one numeral needs the curator to check by eye that every missing numeral is accounted for.
2. The checker cannot confirm that line `N` is where the unprinted chapter starts. It confirms only that the quote is on a body line inside the window. Whether 1257 is the start of XXV rests on the curator's reading of the edition (confirmed here against Ziwsa).
3. The Howto sentence on wrong kinds says the three gap forms "do not explain a repeat". The code also refuses them for a backward step. The table states "a gap" for each, so the sentence is incomplete, not misleading. The wording predates this PR.

The Optatus yaml on main still gives `leaf_missing` for the XXV step, though no leaf is missing. Switching it to `head_unprinted` is a yaml change outside this PR.
