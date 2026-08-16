# drift_detection: the $323/yr cut that was actually $1,305, and not recommended

`tools/cost/measure_drift_signal.py`, 2026-08-16, 56 recorded turns replayed
through `_detect_drift_signal` directly. Raw output in the commit that added
this file. Cost ~$0.12.

Prompted by the review's own route-to-$0.30 table, which listed
`drop drift_detection, $323/yr` as an available lever alongside
`relational_safety`. Tracing the code before touching anything found the
premise was wrong.

## The coupling

`_detect_drift_signal_impl` (`app/graph/nodes.py`) runs an 11-signal general
monitor (smoothing, generating, agreeing, over_producing, temporal_bleed,
flattening, fabrication, apologetics, first_person, self_narration,
declining_initiative). When that monitor comes back clean, it falls through
to `_over_settling_signal` — the two-stage screen-then-adjudicate mechanism
this review measured at an 82% fire rate and spent a full section defending.

```python
if not result.startswith("DRIFT_DETECTED"):
    return _over_settling_signal(response_text, world_id)
```

`_over_settling_signal` has exactly one call site in the entire codebase.
This is it. There is no other path to the over-settling check.

So `drift_detection`'s own `[llm_usage]` line ($0.00224/turn, $323/yr) prices
only the general-monitor call. The screen and adjudication calls it gates
are ledgered separately (`over_settling_screen` $0.00204/turn,
`over_settling_adjudication` $0.00478/turn) and would read as untouched if
you cut `drift_detection` by any means that doesn't also delete the call to
`_over_settling_signal` — but nothing else calls it, so cutting
`drift_detection` cuts all three:

```
0.00224 + 0.00204 + 0.00478 = 0.00906 /turn = $1,305/yr @ 12 turns/hr, 1000h/mo
```

Not $323. The ledger wasn't lying — each row is correctly priced for the
call it names — but "drop drift_detection" was never a $323/yr action the
code permits you to take in isolation.

## The second thing this changes

`drift_detection`'s general monitor also carries `FABRICATION` as one of its
eleven signal types, and it is the **only** place in the codebase that
screens for it on ordinary conversation. `_adjudicate_fabrication` — the
source-fed second pass that confirms or clears a fabrication candidate —
has no other caller either. Cutting `drift_detection` removes the system's
only defense against Facilitator Governance Section 11's cardinal failure:
a real historical figure attributed a saying or scene the record doesn't
give them, delivered to a participant as witness.

## What the replay found

The fire-rate logger (`app/drift_signal_logging.py`) existed but had never
been wired into a capture run — `run_traffic_sample.py`'s handler list
covered `[llm_usage]` and `[over_settling_decision]` but not
`[drift_signal]`. This replay is the first time it's been read.

```
56 turns, 6 fired (11%), 50 clean

SIGNAL BREAKDOWN
  over_settling      5   (9%)
  over_producing     1   (2%)

FABRICATION: 0/56 (0%)
```

Zero fabrication findings in this sample. That is not evidence the check is
safe to cut — 56 ordinary newcomer-question turns is nowhere near enough to
bound the miss rate on a failure mode this project already calls cardinal
and rare, and the asymmetry the whole `_adjudicate_fabrication` design is
built around (a missed fabrication costs far more than a false one) argues
against tuning it down on a small clean draw.

## The corrected arithmetic

The review's central claim — "$0.30/hour is not reachable by any
arrangement of these levers" — turns out to be wrong in the permissive
direction once the coupling is priced correctly:

```
baseline                                    0.03103 /turn   0.372 /hr
- groundedness shadow checks (free)        -0.00099
- relational_safety                        -0.00238
- drift_detection + gated over_settling    -0.00906
                                            --------
all levers taken                            0.01860 /turn   0.223 /hr
```

$0.30/hour **is** reachable — at the cost of deleting fabrication detection,
over-settling detection, and acute-distress detection simultaneously. That
is not a cost optimization at that point; it is turning off the safety and
integrity layer to hit a number. Taking only what costs no mechanism (the
shadow checks) lands at $0.360. $0.30 is not reachable without touching what
the app is for.

## Recommendation

Do not cut `drift_detection`. Not at $323/yr, which was never the real
price, and not at the real $1,305/yr either — the coupling means this was
never a standalone-monitor decision, and the fabrication-detection loss
alone is reason enough to leave it. If the eleven-signal bundle is ever
worth revisiting, the shape to test is the same one this review already
validated for over-settling: pull FABRICATION out into its own dedicated,
source-fed check the way OVER_SETTLING already was (the project's own
history — OVER_SETTLING used to be an twelfth signal in this same monitor
and, bundled, "caught nothing," which is exactly why it has its own screen
today). That is a redesign to measure, not a flag to flip, and nothing in
this review's evidence says it would find money worth the effort.
