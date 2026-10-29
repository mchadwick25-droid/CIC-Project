# Labelling runs, stage 1

Every run below is in plan (Claude Code subagents reading exported prompt files), with no metered call, except `specialist-tryout-1`, which Bedrock refused (see `../Specialist_and_Gold_Set.md`, Incident).

The prompts of a run are rebuilt exactly by `goldset/inplan.py export` on the stream named, with the goldset code at the commit given. The evidence packs depend on that code, so a later change to `goldset/evidence.py` does not change what a run's labeller saw.

| Run | Labeller | Stream | Lines | Goldset code at | Prompts exported | Replies checked | Result |
|---|---|---|---|---|---|---|---|
| `practice-inplan-1` | Claude Opus 5.5 | `data/stream-tryout.jsonl` | 40 (20 seeds, 20 controls) | de8206fe | 18:22:32 UTC | 18:25:10 UTC | 20/20 seeds, 20/20 controls; practice only |
| `lpc-1-specialist-inplan` | Claude Opus 5.5 | `data/stream-lpc-1.jsonl` | 320 (280 lpc, 20 seeds, 20 controls) | de8206fe; reply check from 8b4638cd | 18:26:24 UTC | 18:37:17 UTC | qualifies: 20/20 seeds, 20/20 controls |
| `lpc-1-second-inplan` | Claude Fable 5.1 | `data/stream-lpc-1-second.jsonl` | 56 lpc items | 8b4638cd | 18:40:13 UTC | 18:43:07 UTC | verdict agreement 0.945 (kappa 0.64), 3 disagreements |
| `fleet-2-specialist-inplan` | Claude Opus 5.5 | `data/stream-fleet-2.jsonl` | 437 (397 drawn from the ten other worlds by `data/draw-2.jsonl`, 20 seeds, 20 controls) | 3a4b1066 | 19:15:25 UTC | 19:28:40 UTC | retest: 20/20 seeds, 20/20 controls; 396 pool items labelled, 1 left unlabelled after its one retry (it quoted a pack note, not record text); class counts by draw in `class-counts.json` |
| `fleet-2-second-inplan` | Claude Fable 5.1 | `data/stream-fleet-2-second.jsonl` | 80 items, a fifth of the fleet-2 draw | 6dd57528 | 19:29:26 UTC | 19:34:24 UTC | verdict agreement 0.92 (kappa 0.75), 7 disagreements; packet 2 for Mark: 47 items (`adjudication-packet-2.json`) |

All times 2026-10-29. Mark's rulings on the adjudication packets (`lpc-1-second-inplan/adjudication-packet-1.json`, `fleet-2-second-inplan/adjudication-packet-2.json`, both built by `goldset/packet.py`) are kept in the packet page's store (https://claude.ai/artifact/GFuHi7zRwAWxAvrMinGhZy) until they are folded into the gold set.
