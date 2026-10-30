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

## Limits to know

- The look-alike scan for an `expected_gaps` entry reads every line between the neighbours, not only a rule's `lines`, because a damaged heading is usually a line the hand list did not name. It only counts a line when the token in the numeral position is a short run of numeral letters, digits, the letters OCR confuses with them and the characters in the rule's `ocr_map`. A non-heading that fits this shape (such as `xxi` at line 3671 above) must be accounted for by a `fixes` entry with a quote or an `edition_unnumbered` or `counterpart` line.
- The scan covers the series' own rule; for the `divisions` series it covers every rule that has `number`.
