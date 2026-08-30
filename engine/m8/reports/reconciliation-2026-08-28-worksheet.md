# Bedrock reconciliation worksheet — 2026-08-28

**Purpose:** the spec-principle-13 step that turns rate-card numbers into
quotable ones. **Materially reconciled as of the 2026-08-30 outcome note**
at the bottom — Bedrock mirrors the Anthropic rate card within explained
slack, no rate-card mismatch. Recorded here in full, including the dead
ends, so the next thread doesn't redo the inventory work.

**Where actuals came from:** Mark's AWS account did not have full Cost
Explorer Group-By access (an IAM/billing-access gap, not yet resolved) —
the original plan of a Group-By-Usage-Type CSV across the two Bedrock
services couldn't be pulled. Two things it did have: AWS Cost Anomaly
Detection had already flagged 2026-08-28 as an anomaly on the Sonnet 4.5
(Bedrock Edition) service, giving real per-usage-type dollar figures for
that service/day (below); and the plain AWS Billing daily cost-and-usage
total (all services, no Group-By needed), which turned out to be enough
to cross-check Haiku by subtraction without ever needing a Haiku-specific
pull. See the outcome note for how that closed the loop.

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
| haiku + other AWS (implied) | $0.666 | $0.49 | +37% | day total − sonnet actual (below) |
| **day total (all AWS services)** | **$16.966** | **$12.56** | **+35%** | AWS Billing daily cost-and-usage total, 2026-08-28 |

**Where the day-total row came from:** Mark's account can't reach full
Cost Explorer Group-By yet, but *can* reach the simple daily
cost-and-usage total across all services — no Haiku-specific anomaly
was needed. 2026-08-28's total was **$16.96646776**. Subtracting the
Sonnet actual above ($16.30, from the anomaly's baseline + impact)
leaves **$0.666** for Haiku plus any other AWS service that day — and
the repo's own recorded Haiku usage for the day is $0.486, well inside
that. There is no room left in $0.666 for any material uncounted AWS
cost on 2026-08-28 specifically.

## Outcome note — 2026-08-30

**Materially reconciled. No evidence of a Bedrock rate-card mismatch.**
Two independent views of the same day land on the same overage, which
is the strongest evidence here: Sonnet-only actual-vs-expected is +35.0%
over; the whole-account daily total vs. the corrected repo total is
+35.1% over. Those matching almost exactly means one cause is showing up
both ways, not a Sonnet-specific pricing problem plus a separate,
unrelated account cost. That one cause is the one already identified:
six of the eight Table-battery files that day never recorded cache
tokens (a logging bug, not missing spend — the two comparable smoke runs
that *did* capture cache fields show ~30K write / ~60K read each), plus
the two still-unitemized live runs (`memory-integrity-desert.json`'s 6
real turns chief among them). Sonnet input/output land within 9–14% of
expected on their own, consistent with that.

2026-08-29 corroborates: actual day total $25.489 vs. repo-corrected
expected $19.828 is +28.6% over, same direction, same magnitude family,
and the same cache-field-omission pattern shows up in that day's
Table-battery files too.

**Not chased further:** an independently-pulled, Haiku-only actual
dollar figure (the $0.666 above is Haiku *plus* any other AWS service,
by subtraction, not a directly confirmed Haiku-only number) and a
usage-*amount* (not just $) check via the full CSV, which would allow a
direct per-token rate verification rather than this dollar-level one.
Neither changes the verdict; both would only sharpen it. If Mark gets
full Cost Explorer access later, worth a quick follow-up pull, but nothing
here is blocked on it.

**Side finding, out of scope for this reconciliation:** the daily-total
series shows an unexplained $8.79 spike on 2026-08-23, well before this
worksheet's window and with no corresponding `engine/m*/reports` activity
that day. Not investigated here — flagged for Mark in case it's worth a
separate look.

**Triggered by this note:** principle 13 is satisfied for these rates —
Bedrock mirrors the Anthropic rate card within the explained slack
(incomplete run inventory + the cache-logging bug), not a genuine pricing
gap. **The specific per-session $ figures quoted alongside this note were
wrong — see the 2026-08-30 correction below before quoting any of
them.**

**Not triggered by this note, on Mark's explicit instruction (2026-08-30
thread):** support.html is not touched and no donor-facing copy is
drafted. That's held on the separate, broader question — raised in the
same thread — of what "what it actually costs" should honestly include
(full AWS bill vs. Bedrock tokens vs. Claude Code build-session cost vs.
production hosting/infra), which this reconciliation does not answer and
was never scoped to answer. That conversation is still open and is
Mark's to resume separately.

## Correction — 2026-08-30 (later): the per-session $ figures were never verified

Mark asked directly whether the interview `$0.25/hr` figure was a blend of
all three quoted numbers or interview-specific. Checking the label
answered that (interview-specific, distinct from the two Table figures) —
but re-deriving it from real data to answer properly surfaced that **it
had never actually been verified against the current engine at all.** It
was carried forward, unchecked, from the pre-existing worksheet text
across every earlier note in this file, including the "accurate against
Bedrock's real per-token billing" line above. That claim was wrong for
the interview figure specifically.

**Interview: `$0.25/hr` is wrong. Corrected figure: ≈ $0.35/hr.**
`engine/m8/reports/live-memory-growth-report.json` is a real, full
10-turn Bedrock session (the session cap, `SESSION_TURN_CAP = 10`) —
`turn_dollars` per turn already includes voice + safety + reader calls.
Session total: $0.2918 → $0.02918/turn. Priced at this engine's own
declared pacing convention (`engine/m8/cost.py`,
`TURNS_PER_HOUR_CONVENTION = 12`, sourced from `CiC-Program-Spec.md`
SS7): $0.02918 × 12 = **$0.350/hr**. The 2-turn snapshot in
`live-cost-report.json` gives an even higher $0.45–0.53/hr (fewer turns
to amortize the first turn's cache-write over) — nothing in the real data
supports $0.25.

**Where `$0.25/hr` actually came from:** it is not a measurement of this
engine at all. `Ministry/Technology/Pass3/cost_floor_model.py` and
`provider_repricing.py` both use "$0.25–1.00/hr" repeatedly, but as a
**target band** from an earlier cost-reduction modeling exercise — and
that same script's own output states the *modeled* current/baseline cost
lands around $1.35/hr solo and $2.08/hr Table even after several stacked
code-level cuts, with the target band only reachable by moving
representative generation off Sonnet entirely (not done). It also uses a
different turns-per-hour convention (30/hr solo, 6/hr "reflective") than
this engine's declared 12/hr — not a comparable unit even on its own
terms. The worksheet's `$0.25/hr` looks like that target band leaking
into a "measured" slot it never belonged in.

**Table: `$0.12`/round and `$0.58`/5-round-session hold up better —
plausible, not tightly verified.** Real data: `live-table-report.json`
and `live-table-report-2.json`, two independent real 2-round, 2-seat
Table sessions (`engine/m4/live_table_run.py`):

| | round 1+2 total (sonnet+haiku) | simple $/round |
|---|---:|---:|
| smoke run 1 | $0.288 | $0.144 |
| smoke run 2 | $0.234 | $0.117 |
| pooled | $0.522 / 4 rounds | **$0.131** |

$0.131/round (simple average) is close to the quoted $0.12 — reasonable
given only two small sessions to average over. The 5-round figure needs
a different model, though: cache-write (~$0.113, the system-prompt cost)
is paid once per session, not once per round, so a 5-round session
should cost less than 5× the round average, not the same. Modeling it as
one-time setup + a per-round marginal cost (input/output/cache-read),
averaged across the two runs: setup ≈ $0.113, marginal ≈ $0.074/round →
5-round session ≈ $0.113 + 5×$0.074 = **≈$0.48–0.58** depending on which
run's marginal rate is used — consistent with the quoted $0.58, at the
higher end of the real range.

**Caveat on both Table figures:** derived from two small, same-world-pair
(alx/desert), 2-seat sessions — not independently measured at 5 rounds or
at the "3 seats" seat-count the actual battery runs use. Treat as
order-of-magnitude confirmed, not independently re-measured at the
specific round-count/seat-count combination being quoted.

**Corrected quotable set, if quoting any of these:**
- Interview: **≈$0.35/hr** (was $0.25/hr — wrong, corrected).
- Table compact round: **≈$0.12–0.13** (holds up, small-sample caveat).
- Table full 5-round session: **≈$0.48–0.58** (holds up at the upper end
  of a modeled range, small-sample caveat).

None of this changes the reconciliation's own verdict (Bedrock mirrors
the rate card) — it's a separate correction to the per-session figures
that were riding alongside that verdict without ever being independently
checked.

## Further correction — 2026-08-30 (same day, third pass): Table's 5-round figure walked back to unquotable

Mark, from memory, put a different number on multi-voice Table cost — ~$0.75, recalled from
whenever a $0.25/hr interview figure was also in circulation — and reasoned that if the interview
figure corrected up 40% (0.25→0.35), Table should scale the same way (~$1.00). **That specific
scaling logic doesn't transfer** — the interview correction wasn't a measurement that scaled, it
was a mislabeled non-measurement (an old target-band figure) swapped for a real one; there's no
reason the same ratio applies to an unrelated number. **But checking the instinct against real
data found a genuine problem with the $0.48–0.58 figure above anyway:** it's a model (one-time
cache-write setup + a flat per-round marginal cost), extrapolated from a real 2-round sample —
and it assumes marginal cost stays flat round to round. It doesn't. This project already has hard
evidence per-turn cost climbs as conversation history accumulates (`live-memory-growth-report.json`
— the exact finding that got `SESSION_TURN_CAP` set to 10 for interviews); a Table round almost
certainly has the same dynamic, likely worse, since Table history carries every seated voice's
turns, not one. The flat-marginal model above almost certainly undercounts a real 5-round session.

**Mark confirmed on request: his $0.75 recollection was also never verified against a real test —
an estimate, same category as the wrong $0.25/hr figure, not measured data.** So neither number
(this worksheet's $0.48–0.58 model, or Mark's $0.75 recollection) should be treated as quotable.
**Table full-session figure downgraded from "holds up, small-sample caveat" to genuinely unknown**
until a real, complete 5-round Table session is run end to end and its actual cost read off it —
the same way the interview figure got its $0.35. The compact-round figure (≈$0.12–0.13) is
unaffected — it's a single-round cost, not exposed to the multi-round history-growth problem.

**Consequence for support.html (same day, on Mark's explicit approval):** the cost paragraph now
states $0.35/hr for interview (real, checked) and states the Table's multi-voice mechanism (why it
costs more) with **no dollar figure** for the full-session case, rather than publish either
unverified number as fact. Replace once a real full 5-round session is actually measured.
