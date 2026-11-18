# Batch 4 recording: credit balance

Read from the ElevenLabs subscription endpoint (`character_count`).

| When (UTC, 2026-11-18) | character_count | Note |
|---|---|---|
| Before batch 4 | 329,650 | |
| First read after the runs | 339,730 | 10,080 used; behind the request charges |
| Recheck, 19:41 | 343,269 | 13,619 used |

The request headers charged 13,619 credits: Macrina 969, Nicaea 1,446 and the other nine 11,204. The recheck matches that exactly. The first read was taken before the account had caught up, so the batch cost 13,619 credits, under the 15,000 cap.
