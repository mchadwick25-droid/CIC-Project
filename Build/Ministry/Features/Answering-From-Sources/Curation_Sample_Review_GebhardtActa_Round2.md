# Curation sample review, round 2: Gebhardt Acta

Reviewer: Opus 5.5, targeted recheck of the round-1 finding only. Date: 2026-10-30.
File: `Sandbox/answering-library/curation/acta-martyrum-selecta_gebhardt1902.yaml`, against `cic/texts/acta-martyrum-selecta_gebhardt1902.txt`.
Round 1: `Curation_Sample_Review_GebhardtActa.md` (needs-redo: the Greek Perpetua VII head at line 3729 was missed, and an `expected_gaps` entry at 3821 covered for it). Fix: PR #1339.

## Verdict

`sampled-ok`.

## What was checked

| Check | Result |
|---|---|
| 3729 hand-listed in `perpetua-greek` | Yes, `[3729, 3729]`, between 3637 and 3821. |
| Fix on 3729 | `{line: 3729, set: {c: 'VII'}, quote: '25 VIL Καὶ'}`. The line reads `25 VIL Καὶ μετ’ ὀλίγας ἡμέρας προσευχομένων ἡμῶν`. The quote is on the line. |
| Evidence for 3729 | `{line: 3729, quote: '25 VIL Καὶ'}`, on the line. |
| `expected_gaps` | Removed. No other entry remains. |
| Yaml diff, 400af38e7 (PR #1338 merge) to f3c288931 (current origin/main) | Only: the 3729 line added to `lines`, the 3729 fix, the 3729 evidence entry, the `expected_gaps` block removed, and status `needs-redo` to `drafted`. Nothing loosened. |
| `check` (code exported from origin/main) | PASS. Class curated, 89 divisions (87 body, 2 apparatus), coverage 100.0%, oversize 0, 218 of 218 byte ranges exact, words 65892 = 65892. |
| Series | perpetua-latin 21 readings, 1 to 21, no gaps. perpetua-greek 21 readings, 1 to 21, no gaps or repeats. pionius 23 readings, 1 to 23, no gaps. |
| `sample` | PASS. |
| New Greek VII division | Starts at 3729, address `piece7/grc-ch7`. It runs to 3799; the Greek continuation at 3765 now sits in it, not in `lat-ch7`. Next division is `piece7/lat-ch8` at 3800. |
| Numeral backing for VII | Latin VII at 3709 (`VII. Post dies paucos, dum uniuersi oramus`); running heads VII at 3698 and 3746; the sister scan `gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt` line 4048 prints `25 VII. Kai usr” ökiyas nueoas`. Backed by a second printed instance, not by sequence. |
| Greek VIII at 3821 | Still set to VIII (printed `25 VII Kai`), backed by Latin VIII at 3800 and running head VIII at 3789. |
| Redo report's corrected statements | Match the file and the check output (line numbers 3698, 3709, 3746, sister 4048; 218 byte ranges; 21 Greek hits; no gaps). |
| Vendored text | Unchanged between the two commits. |

## Notes

- `check` still warns that 3729 and 4043 do not match the pattern. Both are carried by `fixes`, so the warning is expected.
- The `pionius` warn lines (verse numbers, apparatus lines, running heads) are unchanged from round 1 and do not affect the result.
