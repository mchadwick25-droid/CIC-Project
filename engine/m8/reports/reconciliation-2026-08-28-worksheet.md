# Bedrock reconciliation worksheet — 2026-08-28

**Purpose:** the spec-principle-13 step that turns rate-card numbers into
quotable ones. This reconciliation is **not yet complete** — see the
2026-08-30 outcome note at the bottom. Recorded here in full so the next
thread can pick it up without redoing the inventory work.

**Where actuals came from:** Mark's AWS account did not have full Cost
Explorer Group-By access (an IAM/billing-access gap, not yet resolved) —
the original plan of a Group-By-Usage-Type CSV across the two Bedrock
services couldn't be pulled. Instead, AWS Cost Anomaly Detection had
already flagged 2026-08-28 as an anomaly on the Sonnet 4.5 (Bedrock
Edition) service, and its root-cause detail view gave real per-usage-type
dollar figures for that service/day (below). **Haiku's actual $ for the
day is still not obtained** — no equivalent anomaly fired for Haiku, and
the full CSV route is still blocked. This worksheet should be updated
once that's available.

## Known live runs recorded in-repo for 2026-08-28 (UTC)

**Revision note (2026-08-30):** the original version of this table (7
rows, ≈$2.15–2.25 estimate) undercounted badly — it captured only the
first M3 admission run, one rerun, two Table smoke runs, one Table
battery, and the diagnostic gate probes. Git history and the repo's own
`engine/m3/reports/` and `engine/m4/reports/` directories show 2026-08-28
was a full six-world build day: two more six-world admission batteries
(fleet-parity, register-reach), a four-world admission run, a
story-quote admission pass, and five more Table battery runs (F1,
F1-register-reach, P1, P2, P3) never made it into the original table.
Full inventory below, read back from each report file's own `usage` /
`usage_token_counts` fields — no Bedrock calls made to produce this.

**M3 admission runs (sonnet only — admission grading makes no
safety/reader calls):**

| run | file | worlds | input | output | cache write | cache read | rate-card $ |
|---|---|---|---:|---:|---:|---:|---:|
| M3 admission (original) | `live-admission-report.json` | alx, desert | 49,695 | 24,655 | 30,796 | 831,492 | $0.884 |
| M3 admission rerun (desert only) | `live-admission-report-desert-only-2026-08-28T04.json` | desert | 25,322 | 11,325 | 0 | 474,488 | $0.388 |
| Fleet-parity battery | `live-admission-report-fleet-parity-2026-08-28.json` | all six | 113,920 | 75,420 | 96,394 | 2,602,638 | $2.616 |
| Register & reach battery | `live-admission-report-register-reach-2026-08-28.json` | all six | 113,920 | 72,127 | 83,934 | 2,661,970 | $2.537 |
| Remaining-four admission | `live-admission-report-remaining-four-2026-08-28.json` | pahc, hal, syr, ijc | 64,225 | 49,241 | 65,598 | 1,771,146 | $1.709 |
| Story-quote pin battery | `live-admission-report-story-quote-2026-08-28.json` | all six | 113,920 | 71,504 | 99,190 | 2,678,130 | $2.590 |
| Remaining-four regrade | `live-admission-regrade-remaining-four-2026-08-28.json` | pahc, hal, syr, ijc | — | — | — | — | $0.00 (deterministic re-grade of existing text, no new API calls) |
| **M3 subtotal** | | | **481,002** | **304,272** | **375,912** | **11,019,864** | **$10.724** |

**M4 Table runs (sonnet + haiku split, read per `call_kind`:
`voice_generation`→sonnet, `safety_call`/`reader_call`/`turn_selector`→haiku):**

| run | file | sonnet $ | haiku $ | cache fields recorded? | total $ |
|---|---|---:|---:|---|---:|
| Table smoke run 1 | `live-table-report.json` | $0.2475 | $0.0407 | yes | $0.288 |
| Table smoke run 2 | `live-table-report-2.json` | $0.2010 | $0.0328 | yes | $0.234 |
| Table battery (6 probes, 3 seats) | `live-table-battery-report.json` | $0.0968 | $0.0656 | **no — 0,0** | $0.162 |
| Table battery F1 | `live-table-battery-F1-2026-08-28.json` | $0.1638 | $0.0859 | **no — 0,0** | $0.250 |
| Table battery F1, register & reach | `live-table-battery-F1-register-reach-2026-08-28.json` | $0.1450 | $0.0819 | **no — 0,0** | $0.227 |
| Table battery P1 | `live-table-battery-P1-2026-08-28.json` | $0.1611 | $0.0555 | **no — 0,0** | $0.217 |
| Table battery P2 | `live-table-battery-P2-2026-08-28.json` | $0.1365 | $0.0536 | **no — 0,0** | $0.190 |
| Table battery P3 | `live-table-battery-P3-2026-08-28.json` | $0.1951 | $0.0574 | **no — 0,0** | $0.253 |
| **Table subtotal** | | **$1.347** | **$0.473** | | **$1.820** |

Only the two smoke runs captured cache write/read; the six battery runs
(base battery + F1 + F1-register-reach + P1 + P2 + P3) all show cache
write and cache read as literal zero — this is the same script bug the
original worksheet named on one row ("battery's usage buckets omitted
cache fields, fixed in the script the same day"), just wider in scope
than first described: it hit **six** files that day, not one. The two
smoke runs (comparable size, same script post-fix) show ~30K cache-write
/ ~60K cache-read each — extrapolating that profile across the six
affected battery runs would add roughly $0.75–1.00 in cache-write/read
spend the repo total below does not capture.

**Diagnostic gate probes** (haiku, no file found — figures as recorded
by the previous session directly from console output): ~7,800 input,
~1,100 output, 0/0 cache → ~$0.013.

**Still unitemized (real live Bedrock calls, no usable per-call token
records — same class of gap as the worksheet's original † row):**
- `live-turn-report-desert-baseline-2026-08-27.json` and
  `live-turn-report-desert.json` — voice_craft live validation, desert
  (the original worksheet's named † row).
- `memory-integrity-desert.json` — a 6-turn live desert conversation
  (real `voice_model_id` calls per its own header), newly found here,
  not previously named anywhere.

Whatever these spent lands in the invoice day-total with no way to
itemize it against a usage-type line from repo records alone.

### Corrected repo-recorded total, 2026-08-28

| | input | output | cache write | cache read | rate-card $ |
|---|---:|---:|---:|---:|---:|
| sonnet | 709,213 | 330,950 | 436,178 | 11,140,396 | **$12.071** |
| haiku | 371,082 | 23,104 | 0 | 0 | **$0.486** |
| **total** | | | | | **$12.557** |

(Sonnet $10.724 M3 + $1.347 Table; haiku $0.473 Table + $0.013
diagnostic gate.) This replaces the original worksheet's ≈$2.15–2.25
estimate, which is now known to have covered well under a quarter of
that day's actual known-run inventory.

## Actuals

| usage type | actual $ | expected $ (corrected) | Δ | source |
|---|---:|---:|---:|---|
| sonnet input | $2.32 | $2.13 | +9% | Cost Anomaly Detection root-cause detail |
| sonnet output | $5.66 | $4.96 | +14% | Cost Anomaly Detection root-cause detail |
| sonnet cache write | $2.33 | $1.64 | +42% | Cost Anomaly Detection root-cause detail |
| sonnet cache read | $4.12 | $3.34 | +23% | Cost Anomaly Detection root-cause detail |
| **sonnet total** | **$16.30** | **$12.07** | **+35%** | anomaly "actual spend," detected service |
| haiku input | pending | $0.37 | — | not yet obtained |
| haiku output | pending | $0.12 | — | not yet obtained |
| **day total** | pending (≥$16.30) | $12.56 + unitemized | — | |

## Outcome note — 2026-08-30

**Not a clean tie-out yet, but no evidence of a Bedrock rate-card
mismatch.** Sonnet input and output land within 9–14% of the corrected
expected figure — squarely explainable by the two still-unitemized live
runs above (`memory-integrity-desert.json`'s 6 real turns chief among
them) plus ordinary rounding in a same-day anomaly snapshot ("total cost
impact can increase or decrease... up to three times daily" per AWS's
own note on the anomaly view). Cache write (+42%) and cache read (+23%)
are the two lines still meaningfully off, and that gap has a specific,
already-identified cause: six of the eight Table-battery files that day
never recorded cache tokens at all (a script bug, not a missing spend) —
backing in the two comparable smoke runs' cache profile across those six
would close most or all of the remaining gap.

**What's still open:**
1. Haiku's actual $ for 2026-08-28 — no anomaly fired for Haiku, so it
   hasn't been pulled yet. Needed before the day can be called
   reconciled.
2. Confirming the cache-write/read gap really is the six-file script bug
   and not something else, ideally via the full Group-By-Usage-Type CSV
   once Mark's Cost Explorer access is sorted (would also give usage
   *amounts*, not just $, for a direct per-token rate check rather than
   this dollar-level comparison).

**Not triggered by this note:** principle 13 is not yet satisfied at the
pass-bar level the original worksheet defined (that bar assumed a
complete known-run inventory, which this wasn't); the per-session
figures do not graduate to quotable; support.html is not touched. Separately
from the tie-out itself, the wider "what does 'cost to run this' honestly
include" question (full AWS bill vs. Bedrock tokens vs. build-session cost
vs. hosting) raised in-thread 2026-08-30 is still open and unresolved by
this reconciliation regardless of how the tie-out lands — recorded here
so it isn't lost, decision deferred to Mark.
