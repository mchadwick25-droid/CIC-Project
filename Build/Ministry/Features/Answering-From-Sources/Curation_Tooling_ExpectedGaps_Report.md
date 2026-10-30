# Curation tooling: expected_gaps reasons and the look-alike test

Facts from `python -m answering_library.curate check` over the 52 files under `Sandbox/answering-library/curation`, and from the real-file replays below.

## What `check` does

- Every `expected_gaps` entry carries a `reason` with exactly one of `leaf_missing`, `counterpart`, `edition_unnumbered`, `as_printed`. A missing reason, an unverifiable one, or one of the wrong kind for the step fails the check (exit 1) and names the series and line. A malformed reason (free text, an unknown form, wrong keys, a YAML boolean as a line) is a load error (exit 2).
- One look-alike test (see the Howto) decides whether a line the pattern does not read is a head of the series. The scan of every `expected_gaps` entry, `counterpart`, `edition_unnumbered` and the hand-listed warning all use it. A reading of the series whose numeral could not be read, between the neighbours, also fails the entry.
- Only fixes of the series' own rules cover a line, in the scan and in the warning.
- The hand-listed warning prints the count per kind, then one line per look-alike.

## Existing excusals

No curation file has an `expected_gaps` entry, so none fails the new rule and no curation yaml is edited. CI runs no step over `answering_library`, so nothing goes red.

## Real-file replays

- Gebhardt, yaml of commit a330439be, entry at line 3821 for series `perpetua-greek`, with no reason, with `leaf_missing {between: [3637, 3821]}`, with `edition_unnumbered {line: 3729, quote: '25 VIL'}` and with `counterpart {line: 3729}`: FAIL in each case, with line 3729 (`25 VIL Καὶ μετ’ ὀλίγας…`) reported. Line 3671 (`xxi χκαταγαγών…`) is not reported.
- `augustine_doctrina-christiana-enchiridion-lat_bruder1838`: 41 look-alike lines inside the rules' `lines` and 248 over the whole file, the same as with no shape test at all (248 lines, 1,240 rule-line pairs for the five rules).
- Real damaged heads found over the whole body: Petschenig 30005 and 31480, Zycha 1066 and 6391, Goldbacher 4368, Raulx 664, 9976 and 12864, Harnack 2742 (9 of 9).

## Counts over the 52 files, whole body, every rule with `number` (rule-line pairs)

| Test | Pairs |
|---|---|
| Any token at the numeral position (no shape test) | 904,872 |
| Numeral-shaped token required in every case | 67,227 |
| The look-alike test | 71,542 |

The look-alike test adds 4,315 pairs over the numeral-shaped-token-only test (lines with a required head word, such as Bruder's `C.`, and lowercase-stroke heads such as `Vil.` that the stricter set refused), and it is 833,330 fewer than the no-shape count.

## 52-file re-run

- Exit codes: 32 exit 0, 20 exit 1, the same files as before this work.
- Output differs only in the hand-listed warning. Look-alike lines in those warnings: 34,367 before this work, 4,290 now. Files with changed counts: gebhardt_acta 59 to 8, Knoll CSEL 33 106 to 5, Zycha CSEL 41 (two files) 4,351 to 84 and 4,456 to 58, Goldbacher (three files) 1,278 to 880, 1,176 to 783, 793 to 433, Raulx 1,532 to 7, Petschenig 19,126 to 642, Knopf 71 to 19, Migne PL33 9 to 5, Optatus 1,289 to 1,287; Krueger 1893, Harnack Mission, Koch 1910 and Robinson 1891 drop to none. The lines that drop out are body text and references (`om. gemens A`, `Gen. 1 und 2.`, `ziehen.`).

## Limits

- A body line that fits the test is reported; the cure is a `fix` or an `ocr_map` entry for a real head, or a change to the rule's pattern or `lines`/apparatus ranges for text that is not a head.
- A stroke dropped from a numeral that leaves another valid numeral cannot be detected by any text check.
