# V7 live main run and repeat: `v7-b-alx-pahc-syr`, 2026-11-04

This folder holds arm B's main run on the remaining 26 probes per world (78 in all), then the repeat on the 14 drawn probes per world (42 in all).

**How it ran**
- The coordination thread approved the run after checking the sample.
- Each world ran its probes back to back, so the cached prompt stayed warm.
- Each command had its own cap: $2.60 for each main run and $1.276 for each repeat. That gives $3.876 per world, from the $11.629 left after the sample.
- The code, reading data, model and hashes were the same as the sample (`../sample/README.md`).

**Files**
- `v7-b-<world>-<main|repeat>.jsonl`: one record per answer, with `.summary.json` alongside.
- `<world>-<part>.stdout.txt`: the printed settings and the guard's announcement.
- `ledger-v7-b-alx-pahc-syr-main.jsonl`: the spend ledger.
- `<world>.main` and `<world>.repeat`: the probe lists.

## Spend (Verified, from the guard's priced totals)

| World | Main (26) | Repeat (14) |
|---|---|---|
| alx | $0.9343 | $0.4482 |
| pahc | $0.8100 | $0.4080 |
| syr | $0.8306 | $0.4034 |
| **All 120 turns** | | **$3.8345** |

- Adding the sample's $0.3710 brings the whole test to **$4.2055** of its $12 ceiling.
- No call failed, no turn needed a retry, and no command stopped on its cap.

## Per answer, all 120 turns (Verified)

| Measure | B, this run | A, fleet graded run 1 |
|---|---|---|
| Warm-turn cost | $0.0304 (n = 117) | $0.0216 |
| Fresh input tokens | 4,466 | about 2,500 |
| Output tokens | 593 | about 456 |
| Seconds to first text | 3.61 | about 2.7 |
| Total seconds | 15.71 | about 11.0 |
| Words in the answer | 313 | about 250 |

- The cost ratio is 1.41, above the plan's 1.3 rule (`../../Test_Plan.md` §9).
- Two things drive it: B's longer input (the reading context), and its longer answers.
- `whole_world_signal` fired once across the 120 turns.

The B answers for the decision are the sample's 6 plus the main run's 78, which is all 84 probes, with the 42 repeats as a second run.
