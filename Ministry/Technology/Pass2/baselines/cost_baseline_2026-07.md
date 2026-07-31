# B-COST — cache-aware cost baseline, current system (2026-07)

Generated deterministically from the committed raw log by `scripts/cost_baseline_runner.py --report`. Fixed conversation set: `scripts/cost_baseline_conversations.json` (40 turns; sources cited there).
Pricing: standard rates as the primary figure; `billed` applies claude-sonnet-5's intro pricing ($2/$10 per MTok) in effect through 2026-08-31. Cache write = 1.25x input (5-min TTL); cache read = 0.1x.

**Totals: 689 LLM calls across 40 participant turns + 4 session starts.** input=2,547,246 output=91,567 cache_write=182,068 cache_read=1,095,867 tokens. **$3.3924 standard** ($2.7283 billed at current intro rates). Per participant turn: $0.0848 standard.

## Per call site (label x model)

| label | model | calls | input | output | cache_write | cache_read | $ std | $ billed |
|---|---|---|---|---|---|---|---|---|
| closing_reply_classifier | claude-haiku-4-5-20251001 | 6 | 892 | 75 | 0 | 0 | 0.0013 | 0.0013 |
| closing_turn_resources_offer | claude-sonnet-5 | 1 | 224 | 50 | 0 | 0 | 0.0014 | 0.0009 |
| closing_turn_resources_show | claude-sonnet-5 | 1 | 2,353 | 343 | 0 | 0 | 0.0122 | 0.0081 |
| closing_turn_sensed_close | claude-sonnet-5 | 1 | 230 | 12 | 0 | 0 | 0.0009 | 0.0006 |
| drift_detection | claude-haiku-4-5-20251001 | 48 | 81,392 | 4,677 | 0 | 0 | 0.1048 | 0.1048 |
| epistemology_bridge | claude-haiku-4-5-20251001 | 38 | 24,089 | 1,275 | 0 | 0 | 0.0305 | 0.0305 |
| fabrication_adjudication | claude-haiku-4-5-20251001 | 3 | 33,418 | 366 | 22,463 | 0 | 0.0409 | 0.0409 |
| facilitator_handoff | claude-sonnet-5 | 4 | 3,117 | 647 | 0 | 0 | 0.0191 | 0.0127 |
| facilitator_reception | claude-sonnet-5 | 4 | 912 | 116 | 0 | 0 | 0.0045 | 0.0030 |
| frame_breaker | claude-haiku-4-5-20251001 | 38 | 18,009 | 440 | 0 | 0 | 0.0202 | 0.0202 |
| main_response | claude-sonnet-5 | 64 | 1,312,866 | 18,415 | 104,872 | 868,636 | 1.9482 | 1.2988 |
| modern_term_bridge | claude-haiku-4-5-20251001 | 36 | 28,054 | 440 | 0 | 0 | 0.0303 | 0.0303 |
| modern_term_bridge_facilitator_turn | claude-sonnet-5 | 1 | 682 | 256 | 0 | 0 | 0.0059 | 0.0039 |
| over_settling_adjudication | claude-haiku-4-5-20251001 | 37 | 437,260 | 11,800 | 54,733 | 227,231 | 0.3054 | 0.3054 |
| over_settling_screen | claude-haiku-4-5-20251001 | 45 | 49,293 | 9,167 | 0 | 0 | 0.0951 | 0.0951 |
| relational_safety | claude-haiku-4-5-20251001 | 38 | 86,907 | 273 | 0 | 0 | 0.0883 | 0.0883 |
| retrieval_filter_lexicon | claude-haiku-4-5-20251001 | 122 | 176,656 | 20,209 | 0 | 0 | 0.2777 | 0.2777 |
| retrieval_filter_story | claude-haiku-4-5-20251001 | 138 | 180,324 | 18,559 | 0 | 0 | 0.2731 | 0.2731 |
| turn_selector | claude-haiku-4-5-20251001 | 29 | 59,585 | 2,527 | 0 | 0 | 0.0722 | 0.0722 |
| wind_down | claude-haiku-4-5-20251001 | 35 | 50,983 | 1,920 | 0 | 0 | 0.0606 | 0.0606 |

## Per conversation

| conversation | turns | calls | input | output | cache_write | cache_read | $ std | $/turn std |
|---|---|---|---|---|---|---|---|---|
| C1_house_church | 10 | 130 | 350,387 | 14,407 | 0 | 153,649 | 0.4193 | 0.0419 |
| C2_desert | 10 | 153 | 518,170 | 15,612 | 27,580 | 282,619 | 0.5964 | 0.0596 |
| C3_alexandria_paused | 10 | 135 | 528,584 | 20,192 | 48,312 | 184,829 | 0.7921 | 0.0792 |
| C4_three_world_table | 10 | 271 | 1,150,105 | 41,356 | 106,176 | 474,770 | 1.5846 | 0.1585 |

## Per turn

| conversation | turn | calls | input | output | cache_write | cache_read | $ std | elapsed_s | paused_before_s |
|---|---|---|---|---|---|---|---|---|---|
| C1_house_church | 0 | 2 | 810 | 201 | 0 | 0 | 0.0054 |  | 0 |
| C1_house_church | 1 | 16 | 41,848 | 2,210 | 0 | 22,058 | 0.0472 | 49.82 | 0 |
| C1_house_church | 2 | 17 | 43,346 | 1,698 | 0 | 22,058 | 0.0464 | 35.34 | 0 |
| C1_house_church | 3 | 16 | 43,719 | 2,351 | 0 | 22,058 | 0.0493 | 43.34 | 0 |
| C1_house_church | 4 | 12 | 35,900 | 1,257 | 0 | 14,453 | 0.0487 | 21.45 | 0 |
| C1_house_church | 5 | 16 | 49,790 | 2,049 | 0 | 22,058 | 0.0563 | 35.69 | 0 |
| C1_house_church | 6 | 12 | 38,858 | 1,387 | 0 | 14,453 | 0.0521 | 27.39 | 0 |
| C1_house_church | 7 | 16 | 50,220 | 2,135 | 0 | 22,058 | 0.0572 | 33.63 | 0 |
| C1_house_church | 8 | 12 | 35,022 | 665 | 0 | 14,453 | 0.0339 | 13.9 | 0 |
| C1_house_church | 9 | 5 | 4,433 | 75 | 0 | 0 | 0.0058 | 4.45 | 0 |
| C1_house_church | 10 | 6 | 6,441 | 379 | 0 | 0 | 0.0171 | 13.43 | 0 |
| C2_desert | 0 | 2 | 811 | 174 | 0 | 0 | 0.0050 |  | 0 |
| C2_desert | 1 | 16 | 55,389 | 1,376 | 20,777 | 13,718 | 0.1107 | 29.88 | 0 |
| C2_desert | 2 | 11 | 25,323 | 816 | 0 | 13,718 | 0.0264 | 18.3 | 0 |
| C2_desert | 3 | 14 | 54,939 | 1,472 | 6,803 | 27,436 | 0.0638 | 29.84 | 0 |
| C2_desert | 4 | 14 | 36,209 | 1,552 | 0 | 20,777 | 0.0340 | 29.84 | 0 |
| C2_desert | 5 | 17 | 57,703 | 1,413 | 0 | 34,495 | 0.0582 | 29.51 | 0 |
| C2_desert | 6 | 15 | 59,488 | 1,722 | 0 | 34,495 | 0.0661 | 31.02 | 0 |
| C2_desert | 7 | 15 | 56,984 | 1,594 | 0 | 34,495 | 0.0577 | 30.88 | 0 |
| C2_desert | 8 | 16 | 59,184 | 1,946 | 0 | 34,495 | 0.0659 | 36.6 | 0 |
| C2_desert | 9 | 16 | 56,079 | 1,832 | 0 | 34,495 | 0.0544 | 34.86 | 0 |
| C2_desert | 10 | 17 | 56,061 | 1,715 | 0 | 34,495 | 0.0542 | 36.55 | 0 |
| C3_alexandria_paused | 0 | 2 | 955 | 152 | 0 | 0 | 0.0051 |  | 0 |
| C3_alexandria_paused | 1 | 8 | 30,211 | 1,284 | 15,737 | 0 | 0.1057 | 21.77 | 0 |
| C3_alexandria_paused | 2 | 15 | 53,180 | 2,723 | 8,419 | 15,737 | 0.0795 | 47.87 | 0 |
| C3_alexandria_paused | 3 | 13 | 51,235 | 1,711 | 0 | 24,156 | 0.0590 | 30.18 | 0 |
| C3_alexandria_paused | 4 | 14 | 54,893 | 2,168 | 0 | 24,156 | 0.0685 | 38.05 | 0 |
| C3_alexandria_paused | 5 | 13 | 53,556 | 2,199 | 0 | 24,156 | 0.0661 | 39.04 | 0 |
| C3_alexandria_paused | 6 | 13 | 54,540 | 1,907 | 24,156 | 0 | 0.1283 | 37.84 | 330 |
| C3_alexandria_paused | 7 | 15 | 59,653 | 1,923 | 0 | 24,156 | 0.0726 | 35.25 | 0 |
| C3_alexandria_paused | 8 | 15 | 58,925 | 2,322 | 0 | 24,156 | 0.0737 | 38.25 | 0 |
| C3_alexandria_paused | 9 | 13 | 56,300 | 1,852 | 0 | 24,156 | 0.0686 | 39.83 | 0 |
| C3_alexandria_paused | 10 | 14 | 55,136 | 1,951 | 0 | 24,156 | 0.0650 | 35.42 | 0 |
| C4_three_world_table | 0 | 2 | 1,453 | 236 | 0 | 0 | 0.0079 |  | 0 |
| C4_three_world_table | 1 | 47 | 205,495 | 7,084 | 64,757 | 57,159 | 0.4196 | 125.5 | 0 |
| C4_three_world_table | 2 | 20 | 91,502 | 1,887 | 0 | 48,227 | 0.1100 | 46.14 | 0 |
| C4_three_world_table | 3 | 30 | 103,218 | 4,721 | 10,961 | 35,230 | 0.1385 | 86.49 | 0 |
| C4_three_world_table | 4 | 27 | 102,565 | 4,038 | 8,204 | 38,862 | 0.1249 | 71.48 | 0 |
| C4_three_world_table | 5 | 27 | 124,191 | 4,134 | 0 | 62,891 | 0.1439 | 72.46 | 0 |
| C4_three_world_table | 6 | 41 | 178,016 | 7,107 | 11,068 | 77,994 | 0.2240 | 119.64 | 0 |
| C4_three_world_table | 7 | 53 | 226,064 | 8,385 | 11,186 | 100,052 | 0.2705 | 143.67 | 0 |
| C4_three_world_table | 8 | 24 | 117,601 | 3,764 | 0 | 54,355 | 0.1453 | 73.18 | 0 |
| C4_three_world_table | 9 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.45 | 0 |
| C4_three_world_table | 10 | 0 | 0 | 0 | 0 | 0 | 0.0000 | 0.32 | 0 |

## Cache-TTL observation (deliberate >5-min pause)

Conversation `C3_alexandria_paused`, pause of 330s before turn 6 (cache TTL is 5 min):

| turn | main_response cache_read | cache_write | input |
|---|---|---|---|
| 5 | 15,737 | 0 | 23,762 |
| 6 | 0 | 15,737 | 23,360 |
| 7 | 15,737 | 0 | 24,649 |

Expected shape: the post-pause turn shows cache_read collapsing toward 0 and cache_write re-paying the prefix; neighbors show warm reads. The table above is the measurement, not the claim.
