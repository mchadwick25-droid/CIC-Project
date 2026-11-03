# V7 specs, in dependency order

Each chunk is a day of work or less. Each spec gives the purpose, the files it may and must not touch, the test written first, done-when and cost.

Owners:
- **V7 lead:** the thread that wrote this plan.
- **Card thread:** a fresh Opus session, kept blind to the answers and the reviews.
- **Question thread:** used only if Mark takes the option.
- **Engine thread:** builds the code.

| Chunk | Spec | Owner | Model | Needs | Spend |
|---|---|---|---|---|---|
| V1 | Baseline A extracted; repeat draw; optional hard-case set | V7 lead (question thread for the option) | Sonnet for the extract; Opus for option questions | nothing | none |
| V2 | Run harness for B, on a test branch from `live` | engine thread | Opus | nothing | none to build |
| V3 | Reader harness and human packets | engine thread | Sonnet | V1, V2's output shape | none |
| V4a | Reading-card field: change order, schema, strip at compile | engine thread | Opus | nothing | none |
| V4b | alx reading cards, drafted and reviewed | card thread | Opus | V4a | none (allowance) |
| V5 | B behind a switch | engine thread | Opus | V4a | none |
| V6 | Dry run with helpers | V7 lead | Sonnet helpers draft; code runs | V2, V3, V5, V4b | none (allowance) |
| V7 | Live sample: 6 turns, $1 cap | V7 lead | production voice model | V6 clean; Mark confirms through coordination | about $0.15–0.28 |
| V8 | Live main run and repeat: 120 turns | V7 lead | production voice model | Mark confirms the sample | about $3.00–5.64; stops at $12 |
| V9 | Reading: model readers and human review | V7 lead | `judge-reader` helpers; human reviewers | V8 | none (allowance) |
| V10 | Decision report | V7 lead | Opus | V9 | none |

V1, V2 and V4a can start at once. No metered call happens before V7.
