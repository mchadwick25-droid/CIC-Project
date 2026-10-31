# Curation tooling: expected_gaps reasons and the look-alike test

Facts from `python -m answering_library.curate check` over the 52 files under `Sandbox/answering-library/curation`, and from the real-file replays below.

## What `check` does

- Every `expected_gaps` entry carries a `reason` with exactly one of `leaf_missing`, `counterpart`, `edition_unnumbered`, `as_printed`, `head_unprinted`. A missing reason, an unverifiable one, or one of the wrong kind for the step fails the check (exit 1) and names the series and line. A malformed reason (free text, an unknown form, wrong keys, a YAML boolean as a line) is a load error (exit 2).
- One look-alike test (see the Howto) decides whether a line the pattern does not read is a head of the series. The scan of every `expected_gaps` entry, `counterpart`, `edition_unnumbered`, `head_unprinted` and the hand-listed warning all use it. A reading of the series whose numeral could not be read, between the neighbours, also fails the entry.
- Only fixes of the series' own rules cover a line, in the scan and in the warning.
- The hand-listed warning prints the count per kind, then one line per look-alike.

## Existing excusals

One curation file has an `expected_gaps` entry: `optatus_against-the-donatists` (step at line 1307, `leaf_missing`). It passes, and no curation yaml is edited. CI runs no step over `answering_library`, so nothing goes red.

## Real-file replays

- Optatus (`optatus_against-the-donatists`), step at line 1307 with `head_unprinted {between: [1233, 1307], line: 1257, quote: 'upon whose head thou hast now endeavoured'}` in a scratch copy of the yaml: PASS. The yaml on main (with `leaf_missing`) also PASSes.

- Gebhardt, yaml of commit a330439be, entry at line 3821 for series `perpetua-greek`, with no reason, with `leaf_missing {between: [3637, 3821]}`, with `edition_unnumbered {line: 3729, quote: '25 VIL'}` and with `counterpart {line: 3729}`: FAIL in each case, with line 3729 (`25 VIL Καὶ μετ’ ὀλίγας…`) reported. Line 3671 (`xxi χκαταγαγών…`) is not reported.
- Raulx 1869 with `expected_gaps: [{series: p3, line: 3330, quote: 'XV.', reason: {leaf_missing: {between: [3261, 3330]}}}]`: FAIL, with line 3286 (`Xiy. Le mémoire des catholiques n'avait`) reported.
- `augustine_doctrina-christiana-enchiridion-lat_bruder1838`: 43 look-alike lines inside the rules' `lines` and 276 over the whole file, the same as with no shape test at all.
- Real damaged heads found over the whole body: Petschenig 30005 and 31480, Zycha 1066 and 6391, Goldbacher 4368, Raulx 664, 9976 and 12864, Harnack 2742 (9 of 9).

## Counts over the 52 files, whole body, every rule with `number` (rule-line pairs)

| Test | Pairs |
|---|---|
| Any token at the numeral position (no shape test) | 905,008 |
| Numeral-shaped token required in every case | 67,234 |
| The look-alike test | 71,688 |

The look-alike test adds 4,454 pairs over the numeral-shaped-token-only test (lines with a required head word, such as Bruder's `C.`, and lowercase-stroke heads such as `Vil.` that the stricter set refused), and it is 833,320 fewer than the no-shape count. The lowercase stroke `y` adds one line over the 52 files (Raulx 3286), counted under the ten Raulx rules.

## 52-file run

- Exit codes: 38 exit 0, 14 exit 1.
- Look-alike lines in the hand-listed warnings: 4,293 over the 52 files. Per file, the largest are Petschenig 642, Goldbacher 880, 783 and 433, Optatus 1,287, Zycha CSEL 41 84 and 58, Acta martyrum selecta (Gebhardt 1902) 8, Knoll CSEL 33 5. The lines that are reported are heads and body text that starts like one; the lines the test leaves out are body text and references (`om. gemens A`, `Gen. 1 und 2.`, `ziehen.`).

## Limits

- A body line that fits the test is reported; the cure is a `fix` or an `ocr_map` entry for a real head, or a change to the rule's pattern or `lines`/apparatus ranges for text that is not a head.
- A stroke dropped from a numeral that leaves another valid numeral cannot be detected by any text check.
