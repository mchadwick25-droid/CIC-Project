# Bedrock reconciliation worksheet — 2026-08-28

**Purpose:** the spec-principle-13 step that turns rate-card numbers into
quotable ones. The token side below is complete; when the Bedrock actuals
post (Cost Explorer lags ~1-2 days), fill the "actual" column and the
comparison is done. One clean tie-out also validates the M8 rate card
itself, after which the support.html price copy can be corrected from
measured truth (it still carries the old poc's $2-5/hr Table figure;
the new engine's Table runs far below it).

**Where to pull actuals:** AWS Cost Explorer → filter Service = Amazon
Bedrock, Region = us-east-1, date = 2026-08-28 (UTC — check the 27th and
29th too; the day boundary may split), group by Usage Type. The usage
types split by model and token class (input / output / cache-write /
cache-read), which maps 1:1 onto the columns below.

## Known live runs recorded in-repo for 2026-08-28 (UTC)

Token counts read back from each run's own usage records.

| run | thread | model class | input | output | cache write | cache read | rate-card est. |
|---|---|---|---:|---:|---:|---:|---:|
| M3 admission (alx + desert) | PR #72 | sonnet | 49,721 | 25,387 | 30,133 | 813,591 | $0.89 |
| M3 admission rerun (desert only) | PR #72 | sonnet | 25,322 | 11,325 | 0 | 474,488 | $0.39 |
| Table smoke run 1 | this branch | mixed | 49,337 | 6,032 | 30,133 | 60,266 | $0.29 |
| Table smoke run 2 | this branch | mixed | 37,715 | 3,678 | 30,133 | 60,266 | $0.23 |
| Table battery (6 probes, 3 seats) | this branch | mixed | 69,535 | 5,672 | unrecorded* | unrecorded* | $0.16 + ~$0.20* |
| Diagnostic gate probes (2× haiku ×2) | this branch | haiku | ~7,800 | ~1,100 | 0 | 0 | ~$0.01 |
| voice_craft live validation (desert) | PR #72 | sonnet | not itemized in report† | | | | † |

\* The battery's usage buckets omitted cache fields (fixed in the script
the same day); the allowance is derived from the smoke runs' per-voice-call
cache profile.
† `live-turn-report-desert.json` / `-baseline` do not itemize usage in a
sweep-readable shape; whatever they spent lands in the invoice day-total
and belongs to the PR #72 thread's row. Expect the actual day-total to sit
somewhat above the table's sum for this reason.

**Rate-card day estimate for the rows above: ≈ $2.15–2.25** (Anthropic
published API rates, fetched 2026-08-25, per `live-cost-report.json`'s
own price_table_source note; Bedrock has historically mirrored these but
that is exactly what this reconciliation verifies).

## To fill when actuals post

| usage type (from Cost Explorer) | actual $ | expected $ | Δ |
|---|---:|---:|---:|
| sonnet input | | | |
| sonnet output | | | |
| sonnet cache write | | | |
| sonnet cache read | | | |
| haiku input | | | |
| haiku output | | | |
| **day total** | | ≈ $2.15–2.25 + † | |

**Pass bar:** each usage-type line within a few percent of expected (the
unrecorded-cache allowance and † rows are the known slack). On a clean
tie-out: (1) principle 13 is satisfied for these rates — the per-session
figures (compact table round ≈ $0.12, full 5-round session ≈ $0.58,
interview ≈ $0.25/hr) graduate to quotable; (2) correct support.html's
$2-5/hr Table figure from measured truth; (3) record the reconciliation
in this file and the decision log.
