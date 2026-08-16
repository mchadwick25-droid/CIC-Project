# 48-turn traffic sample, 2026-08-16

4 sessions x 12 newcomer questions, 2 worlds x 2 consecutive sessions.
48/48 turns returned HTTP 200. Raw log: 2026-08-16_48turn.log (484 lines).

```
world                       turns  fired  fire%  confirm%  incon.
post-apostolic-house-chur      22     16    73%       38%       0
syriac-edessa-nisibis          22     20    91%       20%       0
ALL                            44     36    82%       28%       0

COST at the measured fire rate (82%)
  two-stage as built     $0.00599/turn   $863/yr
  no screen, adjudicate  $0.00518/turn   $746/yr
  screen break-even fire rate: 60%

  fire rate 82%, 95% CI 68%-90% on 44 turns

VERDICT
  The screen fires more often (82%) than it can pay for (60%).
  It is costing $117/yr against adjudicating every turn,
  and every screen false-negative is a miss the adjudicator never sees.
  Either retune the screen below the break-even, or fold detection into
  the adjudicator and drop the stage. Both need this sample to justify.
  Confirm rate is 28% (95% CI 16%-44%) - 26 of 36 flags cleared.
  That is the screen's designed-in false-positive rate. Judge it against
  what a miss costs, not against the flag count.
```

```
440 calls | 5 session(s) | 48 representative turns

label                              calls    true $  as-if-summed    /turn
main_response                         48    0.6526        2.3902  0.01360
over_settling_adjudication            36    0.2293        0.5442  0.00478
relational_safety                     48    0.1141        0.1141  0.00238
drift_detection                       48    0.1073        0.1073  0.00224
over_settling_screen                  44    0.0978        0.0978  0.00204
repair_classifier                     44    0.0429        0.0429  0.00089
fabrication_adjudication               2    0.0425        0.0595  0.00088
negative_condition_story              28    0.0405        0.0405  0.00084
negative_condition_lexicon            26    0.0379        0.0379  0.00079
citation_grounding                    34    0.0343        0.0343  0.00071
frame_breaker                         48    0.0315        0.0315  0.00066
repair_adjudication                    4    0.0278        0.0278  0.00058
facilitator_handoff                    4    0.0114        0.0114  0.00024
figure_chronology                     16    0.0109        0.0109  0.00023
facilitator_reception                  4    0.0053        0.0053  0.00011
quotation_grounding                    4    0.0022        0.0022  0.00005
reroot_guidance                        2    0.0009        0.0009  0.00002
TOTAL                                440    1.4892        3.5587  0.03103

double-count factor if the three token fields are summed: 2.39x

CACHE
  read         1,129,978 tok    61.3% of input
  written         70,723 tok     3.8%
  uncached       641,697 tok    34.8%
  pooling factor (read/write):   16.0x   -- 1x means every write served exactly one read;
                               higher is better, and rises with concurrency

PROJECTION  $0.372/hour  $372/month  $4,468/year  @ 1,000 h/mo
```

---

# What else is in this directory

| file | what it records |
|---|---|
| `2026-08-16_48turn.log` | the raw traffic sample above - the source for every $/turn, fire-rate and cache figure in the review |
| `2026-08-16_over_settling_reps3.{md,json}` | the fold vs the two-stage pair, 56 turns x 3 draws, before temperature was pinned. First measurement that the check does not reproduce its own verdict on 29-43% of turns |
| `2026-08-16_over_settling_reps3_temp0.{md,json}` | the same replay with `monitoring_temperature=0`. Less noise, one stable regression left |
| `2026-08-16_turn48_diagnosis.{md,txt}` | that regression, opened up: the fold enumerates the claim and clears it, three draws out of three, always the same way. The reason the flag stays off |
