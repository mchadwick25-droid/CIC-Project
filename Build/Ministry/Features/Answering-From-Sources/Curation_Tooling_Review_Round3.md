# Curation tooling (look-alike test): review, round 3

Reviewer: Opus 5.5, a different reader from rounds 1 and 2. This is the last round. Subject: PR #1346, branch `claude/curation-tooling-round2`, head b7a1eb401. The PR replaces the look-alike matching of rounds 1 and 2 with one predicate. Files: `Sandbox/answering-library/answering_library/curation.py`, `tests/test_curation_tooling.py`, `Curation_Howto.md`, `Curation_Tooling_ExpectedGaps_Report.md`. No yaml is changed.

Line numbers below are in `curation.py` at b7a1eb401. The bar applied: a finding blocks only if, on a real curated file or a realistic input, the tool excuses a real printed head, drops real printed heads in meaningful numbers, crashes, or contradicts its Howto in a way that misleads a curator.

## Verdict

One blocking finding (A), small. The design holds. One predicate, `_lookalike`, is used by the scan of every `expected_gaps` entry, by `edition_unnumbered`, by `counterpart` (through `_carries_numeral`, line 1098) and by the hand-listed warning. A reason no longer removes a line from the scan, and `not_headings` is gone. Every failing input from rounds 1 and 2 now fails. The flood of round-2 finding D is gone, and the lowercase-stroke heads of round-2 finding C are found again. Finding A is one real damaged head on a real file that the shape set still misses, at a gap the file has open now.

## What was run

- `pytest tests` without `test_union.py` and `test_shelf_row_pointers.py`: 208 passed. `tests/test_curation_tooling.py` and `tests/test_curation.py`: 121 passed. The tests ran from an exported copy, with `cic/texts` linked read-only.
- `curate check` on all 52 curated files with main's code and the PR's code.
- Probes built with the tests' own `make` and `step` helpers and `cu.resolve`.
- Gebhardt (`acta-martyrum-selecta_gebhardt1902`) with the yaml of commit a330439be and four variants of its line-3821 entry.
- `requires_head_word` on every distinct numbered-rule pattern in the 52 files (54 patterns).
- Old against new look-alike sets over the whole body of all 52 files, for every rule with `number`: main's test with no shape filter, main's `shaped=True` test (#1343), and the PR's test. Main's yaml set was used for both, so the one yaml that differs (Bruder, changed on main by #1352) is compared like for like.

## Round-1 and round-2 failing inputs

| Input | Result |
|---|---|
| Gebhardt a330439be, entry 3821, no reason | FAIL: no reason, and 3729 (`25 VIL Καὶ…`) reported |
| same, `leaf_missing {between: [3637, 3821]}` | FAIL: 3729 reported |
| same, `edition_unnumbered {line: 3729, quote: '25 VIL'}` | FAIL: reason refused, 3729 still reported |
| same, `counterpart {line: 3729}` | FAIL: reason refused, 3729 still reported |
| Gebhardt line 3671 (`xxi χκαταγαγών…`) | not reported in any variant |
| `SERMO I / t / SERMO Il / t / SERMO III`: no reason, `leaf_missing`, `edition_unnumbered` naming the whole line or `Il`, `counterpart` on an explicit division at line 3 | FAIL in each case, line 3 reported |
| `SERMO IlX.` unread reading: `leaf_missing [1, 5]`, `[3, 5]`, `edition_unnumbered`, `counterpart`; two unread readings in a row | FAIL in each case, line 3 reported as "a reading of the series whose numeral could not be read" |
| Bruder pattern, `C. X§I.` named by `edition_unnumbered` or by `counterpart` on a division | FAIL: reason refused, line 3 still reported |
| Two entries in one series, damage in the first window, then in the second | FAIL on the damaged window each time |
| Damaged head inside an apparatus range | not reported (apparatus is excluded, as the Howto says) |
| `edition_unnumbered` naming a damaged head inside an apparatus range | refused |
| Fix of another rule on the damaged line (round-1 finding 6) | FAIL, line 3 reported |
| YAML booleans as lines | `CurationError` |

## `requires_head_word` on the 54 patterns

The parse (`_prefix_items`, `_requires_word`, lines 609–638) returned:

- True, and right: every `CAP…`, `CAPUT`, `CHAPTER`, `CHAPITRE`, `APPENDIX`, `Anhang`, `Q…` pattern; every `SERMO` alternation; Bruder's `^(?:Caput|[CGO0]\.) ?`; `^(?:C|G)[A-Za-z\\.']{1,6}?…`; `[Aa][Pp][VvYy][Tt]`; the two Migne sermon patterns that start with `[S5K$]` or `[S5$]`. A required one-of-letters class counts as a word, as the Howto implies.
- False, and right: every pattern whose prefix is only optional groups, free-token classes or a margin number (Petschenig `s1`, Zycha `s0`, Knoll `caput1`, Goldbacher `ep`, Gebhardt, Raulx `p0`, Optatus, Koch, the Harnack and von Soden section rules). `^§\.? ?` and `^\(` are False because `§` and `(` are not letters; their numerals are digits, so nothing is lost.
- False, and arguably wrong: Migne PL33 `letter`, `^(?=(?:E|K)\S*S[TI1][O0UV]\S*[\s,])(?P<w>[A-Za-z0-9.!|]{5,9}),?\s+…(?P<n>…)`. The head word EPISTOLA is required only through a lookahead, which the parse does not read. See non-blocking note B.

No pattern returns True for a free prefix, so the flood cannot come back from a mis-parse on the current files.

## Whole-file look-alike sets, 52 files

Rule-line pairs over the whole body, every rule with `number`:

| Test | Pairs | Distinct lines |
|---|---|---|
| No shape filter | 904,992 | 54,082 |
| Main's shaped test (#1343) | 67,241 | 9,337 |
| The PR's test | 71,675 | 9,874 |

Hand-listed warnings, lines inside the rules' `lines`: 34,361 with main's code, 4,292 with the PR's.

Bruder: 41 rule-line lines and 248 whole-file lines with the branch's yaml; 43 and 274 with main's newer yaml. The PR's test drops none of them in either case. The 9 round-2 table lines (Petschenig 30005, 31480; Zycha 1066, 6391; Goldbacher 4368; Raulx 664, 9976, 12864; Harnack 2742) are all found.

Lines the unfiltered test reports and the PR's does not: 44,208 distinct lines in 19 files. I filtered them to tokens that are mostly numeral letters (206 lines) and read each one, including all 16 files whose warning shrank. What they are:

- Body text, citations and apparatus sigla: nearly all (`Vel. Spr. 21, 1.`, `Cic. Tusc.`, `MOPQVedd.`, `Christi,`, `Carthage,`).
- Title pages and front matter: `VOL. LIII`, `CORPVS`, `EPISTVLAE.`, `MDCCCLXXXXVIII.`.
- Real damaged heads that the file already reads as division starts, so none goes unseen: Goldbacher CSEL 57 `CLXXXVB.`, `CCVTJI.`, `CCIJV.`, `ccLvra.`, `10 CCIAT`, `CCLXJIL`; Migne PL33 `EPISTOLA CLXXXVIf`, `EPISTOLA CCXYt.`, `EPISTOLA CaVI`.
- Heads of other works, outside the rule's `lines` and outside any window of its series: Knopf `«IX.`, `«=XII.`, `JII.`, `©=IV.` under `pionius-chapter`; Zycha and Petschenig work titles (`Vim. DE MENDACIO.`, `II.II. Contra litterae Petiliani`) under section rules whose numeral is arabic.
- One real head of its own series, not read, at an open gap: Raulx 3286 `Xiy.` (finding A).

Lines main's shaped test reports and the PR's does not: 103, all lowercase-only tokens (`illi` 26, `i` 21, `v` 15, `l` 14, `xxi` 4, …). This is the intended effect. Lines the PR adds over main's shaped test: 6,150 pairs. They include real damaged heads (`XLYI`, `XYI`, `XXVni`, `VIIH`, `PRIHUM.`) and OCR debris (`*`, `(`, `5)`, `H`).

The trade is acceptable for scholarly use: the noise removed is about 833,000 pairs, and one real unread head is lost.

## 52-file exit codes

Identical to main for each yaml set. With the branch's yaml: 32 exit 0, 20 exit 1, as the report says. With main's yaml (after #1352): 33 exit 0, 19 exit 1, for both codes; Bruder's output is byte-identical between the two codes. Output differs only inside the hand-listed warnings.

## Blocking finding

### A. A real damaged head with a lowercase `y` is not a look-alike, and `leaf_missing` excuses the gap after it

`_LOWER_STROKES` (line 53) is `ijlnr`. Uppercase `Y` is a stroke (line 52), but lowercase `y`, which OCR also prints for `V`, is not.

- On the real file. `augustine_oeuvres-completes-tome13-donatistes-slice-fra_raulx1869`, series `p3`, has an open gap now: `(3330, 13, 15)`. Line 3286 is `Xiy. Le mémoire des catholiques n'avait`, the head XIV, inside `p3`'s `lines`. Main's yaml plus `expected_gaps: [{series: p3, line: 3330, quote: 'XV.', reason: {leaf_missing: {between: [3261, 3330]}}}]`: the entry passes with the PR's code. Line 3286 is not reported, and the hand-listed warning for `p3` lists nothing. This is the move a curator would make for this gap.
- Correct behaviour. Line 3286 is reported between the neighbours, and the entry fails until the head is read with a `fix` or an `ocr_map` entry. Adding `y` to `_LOWER_STROKES` does this: with it, the same check fails on line 3286 and the `p3` warning lists it. Over all 52 files, adding `y` adds this one line and no other. Add a test built from `Xiy. Le mémoire`, and add `y` to the Howto's list of lowercase strokes.

## Non-blocking notes

B. **A head word required only through a lookahead is not seen (low).** `_requires_word` (line 620) does not look inside `ASSERT` items, so Migne PL33 `letter` parses False and its numeral needs the shape test. Effect on the real file: three damaged heads (`CLXXXVIf`, `CCXYt.`, `CaVI`) leave the look-alike set, but all three are already division starts (ep187, ep216, ep256). No head goes unseen today.

C. **The Howto and the code differ on the shape set (low).** The Howto says a numeral-shaped token has "at least one uppercase numeral letter". The code needs one only to admit the lowercase strokes. A token of only digits, `T U H Y W F` and debris also counts (`TU es`, `HY`, `12. cf. Ps.`, `(1) note`, `F. Iulius` are reported in probes). The code's behaviour is the more useful one, since `11.` for `II.` is found. The Howto also says a lowercase-only token counts when "the rule ignores case". The code then adds only `v x c d m`, and `i j l` still need an uppercase letter, so under `flags: i` the tokens `xxl`, `vil`, `vli`, `iil` and `xxj` are not look-alikes. I found no such head on the real files (the `flags: i` rules are Goldbacher `ep` and the Hoffmann `CAP…T` rules, which require a head word). Make the Howto describe what the code does, or admit `i l` when the rule ignores case.

D. **`counterpart` does not check the value (low).** A counterpart line that is a reading of another series is accepted at once (line 1145). The scan still runs over the whole window, so a counterpart cannot hide a damaged head; the probe with a damaged `IIl.` in the window fails. But any reading of another series in the window passes, including one with a different number (a series-`g` `I.` was accepted for a missing series-`s` II). So a missing leaf can be recorded as a counterpart. That mislabels the kind of gap; it does not hide a printed head. The Howto states this behaviour openly.

E. **The report's figures are for the branch's yaml (low).** After #1352, main's Bruder yaml gives 33 pass and 19 fail, and Bruder 43 and 274 look-alike lines. The report's "gebhardt_acta 59 to 8" is the file `acta-martyrum-selecta_gebhardt1902`, not `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902`.

F. **Information.** The parse imports `re._parser` and `re._constants`, CPython internals that exist from Python 3.11 (tests ran on 3.13). Uppercase `J` and lowercase `m` are not strokes. Adding `J` would add about 25 lines, nearly all initials (`J. Marquardt`), and its real heads are already read. Adding `m` would add 11 lines, mostly apparatus sigla. Neither is needed.

## Tests

The new tests assert the failing inputs above. They cover `SERMO Il` under every reason form, the `25 VIL` line on Gebhardt's pattern, the unread reading, `C. X§I.` under both reasons, 25 Bruder heads, the 14 lowercase-stroke heads of round 2, lowercase body words, Petschenig's free-prefix pattern against `SERMO`, the parallel-series counterpart, a fix of another rule, and YAML booleans. The real-file Gebhardt case is covered by synthetic lines built from it, not by the file itself.

## Code discipline

The code and tests carry docstrings only. The Howto describes current behaviour with no change history. The report's "before this work" comparisons sit in `Build/Ministry`, where such notes belong. No yaml is edited.
