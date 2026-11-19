# V7 live sample: `v7-b-alx-pahc-syr`, 2026-11-04

Arm B only: 2 probes per world, 6 turns. Mark approved it, relayed by the coordination thread: "yes, run the sample".

**Run settings.**
- Code: branch `v7/b-on-live` at cb585b75, which is `live` c869dd86 plus the V5 test-branch list.
- Reading data: `git archive 974314241 records`. Its lens notes equal A's records in all three worlds.
- Caps, one per command: alx $0.34, pahc $0.33, syr $0.33.
- Model: `us.anthropic.claude-sonnet-4-5-20250929-v1:0`, on Bedrock us-east-1, with max tokens 2048.
- Package, shape and seal hashes equal A's (`../../Set/A_run_settings.json`).

**What the files hold.**
- `<world>.stdout.txt`: the printed settings and the guard's announcement.
- `v7-b-<world>.jsonl` and `.summary.json`: one record per turn, and the run summary.
- `ledger-v7-b-alx-pahc-syr.jsonl`: the guard's hold and settle lines.

The answers are helper-free: the live model wrote them.

## Spend (Verified, from the guard's priced totals)

| World | Priced total | Cap |
|---|---|---|
| alx | $0.1382 | $0.34 |
| pahc | $0.1156 | $0.33 |
| syr | $0.1172 | $0.33 |
| **All** | **$0.3710** | $1.00 |

- No call failed. Each of the 6 turns took one attempt.
- The ledger has 6 holds and 6 settles.

## Per turn (Verified)

| World | Probe | Fresh input | Cache write | Cache read | Output | First text (s) | Total (s) | Priced | Additions (chars) | Words |
|---|---|---|---|---|---|---|---|---|---|---|
| alx | c-p-probe-01 | 5,754 | 18,368 | 0 | 541 | 8.0 | 19.1 | $0.1037 | 9,369 | 330 |
| alx | f4-e-probe-01 | 6,256 | 0 | 18,368 | 475 | 4.6 | 9.8 | $0.0345 | 11,564 | 206 |
| pahc | f1-i-probe-01 | 4,956 | 14,900 | 1,776 | 510 | 5.7 | 10.7 | $0.0868 | 6,667 | 292 |
| pahc | f2-t-probe-01 | 5,142 | 0 | 16,676 | 383 | 4.2 | 12.2 | $0.0288 | 9,104 | 191 |
| syr | f4-e-probe-01 | 3,847 | 16,441 | 1,776 | 481 | 9.3 | 14.5 | $0.0890 | 3,975 | 297 |
| syr | f6-t-probe-01 | 4,104 | 0 | 18,217 | 519 | 4.0 | 13.9 | $0.0281 | 9,390 | 277 |

`whole_world_signal` fired 0 times.

## What the numbers say

**Verified**
- The first turn in each world writes the cached world prompt, 15,000–18,000 tokens. That makes it cost three times a warm turn. This is why the sample spent more than the $0.17–0.30 estimated in `../../Test_Plan.md` §7.
- Warm B turns average $0.0305.
- A's warm turns in fleet graded run 1 average $0.0216: alx $0.0223, pahc $0.0215, syr $0.0211, computed from `../../Set/A_<world>.jsonl`.
- Warm B costs 1.41 times warm A. The extra cost is B's fresh input: about 4,000–6,000 tokens a turn, against A's 2,400–2,600.
- That is above the plan's success rule of 1.3 times A's cost (`../../Test_Plan.md` §9).

**Latency (Verified on 6 turns)**
- First text arrives in 4.0–9.3 s for B, against A's 2.6–2.8 s average.
- Total time is 9.8–19.1 s, against A's 10.6–11.8 s average.
- Six turns are too few to read latency closely.

**Stop rule for the remaining 120 turns**
- Scaling the sample's mean cost per turn gives $0.0618 × 120 = $7.42.
- With the cache kept warm, the expected cost is about 117 × $0.0305 + 3 × $0.095 = $3.85. Each world runs its probes back to back, so it pays one cold start.
- Both figures are under the $11 line, so the repeat is not cut.
