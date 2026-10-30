# Curation tooling: expected_gaps reasons, look-alike skip, warn summary

Facts from re-running `python -m answering_library.curate check` on every file under `Sandbox/answering-library/curation` (52 files), once with the code on main and once with this change.

## What changed in `check`

1. Every `expected_gaps` entry needs a `reason` with exactly one of four forms: `leaf_missing`, `counterpart`, `edition_unnumbered`, `as_printed`. A missing reason, a reason that does not verify, a reason of the wrong kind for the step, and an unaccounted look-alike heading between the step's neighbours each fail the check (exit 1) with a message that names the series and line of the entry. A malformed reason (free text, an unknown form, wrong keys) is a load error (exit 2).
2. The hand-listed look-alike warning skips any line that a `fixes` entry in the same curation covers.
3. The hand-listed look-alike warning prints the count of each kind on one line, then each line beneath it.

## Existing excusals that fail the new rule

None. No curation file on main has an `expected_gaps` entry. The two commits that ever had one (a330439be, d31089190, both for `acta-martyrum-selecta_gebhardt1902`) were redone without it. Nothing needed a reason added, and no curation yaml was edited.

The historical case was re-run from commit a330439be (`expected_gaps: [{series: perpetua-greek, line: 3821, quote: '25 VII Kai'}]`) with a scratch copy outside the repo:

- Without a reason: FAIL, "expected_gaps for series 'perpetua-greek' at line 3821 has no reason".
- With `leaf_missing: {between: [3637, 3821]}` (the true neighbours): FAIL, because line 3729, `25 VIL Καὶ μετ’ ὀλίγας ἡμέρας…`, is a look-alike heading of the series between them. The scan also lists line 3671 (`xxi χκαταγαγών…`), which is not a heading.

CI does not run the checker over curated files (no workflow step references `answering_library`), so nothing goes red. If a later redo batch adds entries, each is held to the rule at its own `check` run.

## Files whose results changed

Exit codes are the same for all 52 files: 32 exit 0, 20 exit 1 (the same 20 as before). The only output changes are in the hand-listed look-alike warning:

| File | Look-alike lines before | After | Why |
|---|---|---|---|
| `acta-martyrum-selecta_gebhardt1902` | 63 in 2 warnings | 59 in 1 warning | Lines 3729 and 4043 (rule `perpetua-greek`) and two lines of rule `pionius` are covered by `fixes`; the `perpetua-greek` warning disappears. |
| `possidius_vita-augustini_weiskotten1919` | 4 in 2 warnings | 0 | Lines 4177, 4629, 4212 and 4667 are covered by `fixes`. |

Total look-alike lines over all files: 34,367 before, 34,359 after. Warning lines per file are otherwise unchanged. Files with the same look-alike counts print the new layout (count per kind, then one line per look-alike).

Files that exit 1 on main and still do (unchanged by this change): augustine_de-fide-et-symbolo-de-opere-monachorum-et-al-lat_zycha-csel41, augustine_doctrina-christiana-enchiridion-lat_bruder1838, augustine_epistulae-1-123-lat_goldbacher-csel34, augustine_epistulae-124-184a-lat_goldbacher-csel44, augustine_epistulae-critical_goldbacher-csel57-pars4, augustine_epistulae-maurist-order-lat_migne-pl33, augustine_oeuvres-completes-tome13-donatistes-slice-fra_raulx1869, augustine_opera-sect-v-pars-iii-lat_zycha1900-csel41, augustine_retractationes-lat_knoll-csel36, augustine_sermones-1-340-lat_migne-pl38, augustine_sermones-341-396-et-appendix-lat_migne-pl39, augustine_sermones-ad-populum-lat_migne-gaume1841-t5, augustine_sermones-inediti-lat_caillau1842, augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910, benson_cyprian-his-life-his-times-his-work_1897, harnack_mission-und-ausbreitung-des-christentums-band2-deu_2e-aufl1906, koch_cathedra-petri-deu_1930, koch_cyprianische-untersuchungen-deu_1926, optatus_against-the-donatists, ribbeck_donatus-und-augustinus-erste-haelfte-deu_1857.

## Round 2 (review findings 1 to 4)

Changes: `edition_unnumbered` and `counterpart` refuse a line that carries a numeral; an unreadable reading between the neighbours fails the entry; the numeral-shape test applies only where the numeral is the first token of the heading (so a head word such as `Caput` or `C.` needs no test) and lowercase letters no longer count for a case-sensitive rule; `not_headings` lists a line that is not a heading; `counterpart` must be a head outside the series near the step; only fixes of the series' own rules count; YAML booleans are rejected as line numbers.

Replays on the real files, with the new code:

- Gebhardt a330439be yaml with `edition_unnumbered {line: 3729, quote: '25 VIL'}`: FAIL. Line 3729 is refused as a head with a numeral and stays in the scan. With `leaf_missing` or no reason: FAIL on line 3729. Line 3671 (`xxi χκαταγαγών…`) is no longer flagged.
- `augustine_doctrina-christiana-enchiridion-lat_bruder1838`: 41 look-alike lines in the rules' `lines` with the unshaped test and 41 with the new test; none dropped. Over the whole file the unshaped test finds 248 lines and the new test 248. The hand-listed warnings count 4, 5, 9, 8 and 15 lines (41 in all).

Re-run of all 52 curated files with the round-2 code: exit codes are the same as on the code before PR #1343 (32 exit 0, 20 exit 1). Output is identical to the round-1 output for every file. Look-alike lines in hand-listed warnings: 34,367 before PR #1343, 34,359 after PR #1343 and after round 2. Still no curation file has `expected_gaps` or `not_headings`.

## Limits to know

- The scan for an `expected_gaps` entry reads every line between the neighbours, not only a rule's `lines`, because a damaged heading is usually a line the hand list did not name. Where the numeral leads the heading it must be a short run of numeral letters, digits and the strokes OCR puts in their place. A body line that still fits is listed in `not_headings` with a quote, which records only that the line is not a heading.
- A stroke dropped from a numeral that leaves another valid numeral (`II` printed where `III` was meant) cannot be detected by any text check.
- The scan covers the series' own rule; for a series that is not a rule id it covers every rule that has `number`.
