# Batch 8 recording: credit balance

Approved run: "Batch 8: the twelve" (Mark, 2026-11-21, "Approve, cap 24,500", then after hearing the Francis sample "sounds right record the other eleven"; cap 24,500 credits). Read from the ElevenLabs subscription endpoint (`character_count`). Settings, as each log prints them: voice `onegjDE2z0mQtp1g0HK7`, model `eleven_v4`, `mp3_44100_64`, stability 0.95, similarity 0.68, style 0, speaker boost on, `[pause]` between paragraphs, 7 respellings. Constantine was not re-recorded.

| Run | Item | Characters sent | Credits charged | Length |
|---|---|---|---|---|
| 1, the sample | Francis of Assisi | 3,778 | 1,832 | 4:13 |
| 2 | Bernard of Clairvaux | 3,759 | 1,823 | 4:17 |
| 2 | Thomas Aquinas | 3,730 | 1,808 | 4:09 |
| 2 | Jan Hus | 4,281 | 2,076 | 4:57 |
| 2 | Catherine of Siena | 3,788 | 1,837 | 4:27 |
| 2 | Gregory Palamas | 3,977 | 1,928 | 4:35 |
| 2 | Huldrych Zwingli | 3,857 | 1,870 | 4:23 |
| 2 | Thomas Cranmer | 3,749 | 1,818 | 4:22 |
| 2 | Teresa of Ávila | 3,747 | 1,817 | 4:22 |
| 2 | Ambrose of Milan | 4,105 | 1,990 | 4:32 |
| 2 | Jerome | 3,875 | 1,879 | 4:18 |
| 2 | Leo of Rome | 3,874 | 1,878 | 4:34 |
| **Total** | 12 stories, 12 requests | 46,520 | **22,556** | |

Run 2 went one story per request (`batch8-run2-<slug>.log`): a single eleven-story command was stopped by the session's permission check before it started, and nothing was charged for it.

| When (UTC, 2026-11-21) | character_count |
|---|---|
| Before batch 8 | 484,151 |
| After run 1 | 485,983 |
| After run 2 | 506,707 |

The balance moved by 22,556, matching the request charges exactly, under the 24,500 cap.
