# Access and Monetization: hand-off

Written 2026-10-02 at the end of the first thread, for whoever picks this up. Read this first, then `Decision-Log.md` (22 entries, Mark's decisions) and `Open_Gaps_Tracking.md` (8 entries).

## What this module is

A one-time, pay-as-you-go access system for the conversation engines. No subscription. The Church Family Tree stays free with no cap. Build a Table is excluded from packs until its cost is measured.

## Decided (see Decision-Log.md for the reasoning)

- Free: 3 conversations of 3 turns, tracked by the signed visitor cookie. Funded from contributions as a separate bucket.
- Paid: up to 7 turns per conversation. Packs: $7 for 5, $15 for 13, $30 for 30. Units never expire. No auto-reload. Donations are separate from paid access.
- A unit is held when a conversation starts, captured when the first Representative reply is stored, and returned if no reply lands.
- The Facilitator speaks the close and any offer. A Representative never speaks the ask. Buyers are adults, and a parent may buy for a youth.
- A payment is never linked to conversation text.
- The pilot is a priced demand test with real checkout. Counsel and an accountant review before any live checkout. The echo, the blank wait and cut-off replies are fixed before paid launch.
- Scope: pay analysis and the pay-as-you-go build only (entry 21). The funding thread is not a gate (entry 22).

## Built

`Sandbox/access-ledger/` (Python, 74 tests, Stripe test mode, no prices in logic): append-only ledger with holds, hosted Checkout creation, signed-webhook processor with refunds and disputes, daily reconciliation, HTTP service, pack catalogue.
`Sandbox/access-ui/` (React and TypeScript scaffold only): package, config and lockfile. No component is written.
`Integration_Plan.md`: seven hook points in the engine. Nothing in `engine/` was changed.

## Research and measurements kept here

- `Research/`: six Fable research reports, Opus review round 1 (design) and the Opus market buy-in review.
- `Measurements/`: scripted runs and their data (`run15.json`, `sample3_full.json`, `probe_restate.json`) and the scripts that made them.
- `Prototypes/`: the pricing model, the end-of-free screens, the decision brief and the recorded transcripts as HTML. They were published as private artifacts and are kept here as source.

## Known flaws in this thread's work

- The measurement scripts called `engine.m4.turn.run_turn` directly. They did not go through the running app, and the early ones saved only the reply text. The market buy-in review judged sourcing from those stripped transcripts, so its finding that the sourcing is not visible is unreliable. `sample3_full.json` keeps the citations, glosses and figures the engine returns.
- The cut-off finding (Open_Gaps entry 4) was measured on the direct path. Whether the running app cuts replies the same way is not confirmed. A message with that finding was sent to the CIC build assessment and cleanup thread without that caveat having been tested.
- Costs come from one scripted conversation, priced at the rate card. The repo's own reconciliation found the real AWS bill ran 1.35 times the rate card on one day. Conversion rates are guesses from other industries.
- Competitor prices and the pastor survey figures rest on search summaries because many pages were blocked. They need re-checking.
- The engine flagged 8, 13 and 22 sentences in three replies as claims with no source tied to them. Not judged here.
- One 15-turn run was lost to a detached process and re-run. The aborted run's log is `Measurements/run15_aborted.log`.
- A live-app test (`Measurements/live_api_run.py`) was started and stopped before any model call completed. It needs the header `Authorization: Session <code>`.

## Not done

- No engine change. The three launch-gate defects (echo, blank wait with streaming unread, cut-off replies) are with other threads.
- The end-of-free screens are a prototype only. No participant-facing copy has been through approval.
- The church and class pool, the repricing trigger, and the lost-cookie recovery path are open.

## Working rules Mark set during this thread

No paid run and no message to another thread without his explicit yes in the moment. Answer a question and stop. Stay on the pay analysis and build.
