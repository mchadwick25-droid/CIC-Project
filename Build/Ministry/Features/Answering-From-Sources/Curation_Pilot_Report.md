# Curation pilot report: possidius_vita-augustini_weiskotten1919

Drafter: Sonnet 5.5. File: `Sandbox/answering-library/curation/possidius_vita-augustini_weiskotten1919.yaml` (54,959 words).

## Time and effort

- Start 2026-10-29T23:59:11Z, finish about 2026-10-30T00:04Z (draft, checks, report). Roughly 5 minutes to a passing check.
- Check runs: 3 (baseline, after the first edit, after one line-number correction). Edit iterations: 2.
- Entries added or changed: 4 `fixes`, 0 explicit divisions, 0 `expected_gaps`. Also changed: 2 patterns (optional margin line number), 7 hand-listed lines added, 7 evidence entries added, status set to `drafted`.

## What was wrong

The two letter rules (Latin `letter-lat`, English `letter-eng`) in chapter 30 missed six sections:

- Latin 2 (4229), 9 (4563) and 10 (4611): a margin line number sits before the numeral. Fixed by making the pattern accept `^(?:\d{1,2} )?`.
- Latin 11 (4629, printed `ii.`) and English 11 (4667, printed `n.`): OCR damage, set by `fixes` with a quote on the line.
- Found by the checker's gaps and the check's own look-alike scan, not in the Opus findings: Latin 1 (4177, `20 i. Caritati`) and English 1 (4212, `i. I thought`). Both printed `i.` and were never divisions, so the letter's first section was folded into the chapter opening. Set by `fixes`.

Section 11: neither the Latin nor the English prints a clean `11`. The numeral is set because the Latin (`ii.`) and the English (`n.`) facing counterparts each stand between a printed 10 and a printed 12, and each reads as `11` damaged. That is two independent printed instances, not the sequence alone. The Opus reader should judge that call. Sections 1 are the same: Latin and English both print `i.` and the following sections are 2.

## Final check output

class after: curated. divisions 98 (92 body, 3 apparatus). Rule hits caput 31, chapter 31, letter-lat 14, letter-eng 14.
All checks PASS (uniqueness, coverage 100.0%, oversize 0 over 5000, rules and evidence, word completeness 55574 = 55574, 180 of 180 byte ranges exact). Series letter-lat and letter-eng: 14 readings each, first 1, last 14, no repeats, backward steps or gaps. RESULT: PASS.

Four `warn` lines remain (4177, 4629, 4212, 4667). They are the four fixed lines, which the look-alike scan still reports because the pattern does not read their numeral. They do not change the result.

## Remaining defect and judgment

None open. Only numbering was needed. The one judgment beyond numbering is the section 11 reading above. The tooling expressed everything; no checker change was needed.

## Estimate for similar files

A file whose defects are a small hand-listed series with margin numbers and OCR damage: about 5 to 10 minutes and 2 to 3 check runs. The cost is in reading the source lines around each gap, not in the YAML.
