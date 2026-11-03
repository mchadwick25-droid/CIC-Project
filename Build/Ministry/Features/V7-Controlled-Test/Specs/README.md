# V7 specs, in dependency order

Each chunk is one day of work or less. Each spec gives the purpose, the files it may and must not touch, the test written first, done-when, and cost.

Owners:
- The **V7 lead** is the thread that wrote this plan.
- The **question thread** and the **card thread** are fresh Opus sessions. Each is kept blind to the other's output.
- The **engine thread** builds the code.

| Chunk | Spec | Owner | Model | Needs | Spend |
|---|---|---|---|---|---|
| V1 | Question set and trap notes, frozen | question thread | Opus writes the questions; code freezes them | D3 frozen, for the D3 draw | none |
| V2 | Run harness for the three arms | engine thread | Opus | nothing | none to build |
| V3 | Reader harness and human packets | engine thread | Sonnet | V2's output shape | none |
| V4a | Reading-card field: change order, schema, strip at compile | engine thread | Opus | nothing | none |
| V4b | alx reading cards, drafted and reviewed | card thread | Opus | V4a, and V1 frozen first | none (allowance) |
| V5 | B behind a switch | engine thread | Opus | V4a | none |
| V6 | Dry run with helpers | V7 lead | Sonnet helpers draft; code runs | V2, V3, V5, V4b | none (allowance) |
| V7 | Live sample, 12 turns, $2 cap | V7 lead | production models | V6 clean; Mark's confirmation through coordination | about $0.60 |
| V8 | Live main run, 480 turns | V7 lead | production models | Mark confirms the sample | about $11–24, inside $30 |
| V9 | Reading: model readers and human review | V7 lead | `judge-reader` helpers, plus human reviewers | V8 | none (allowance) |
| V10 | Decision report | V7 lead | Opus | V9 | none |

V1 and V2 can start at once, along with V4a, and V5 can follow V4a while the cards are written. No metered call happens before V7.
