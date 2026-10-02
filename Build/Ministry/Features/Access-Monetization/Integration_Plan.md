# Access ledger: integration plan

Where `Sandbox/access-ledger/` plugs into the engine. Nothing here is built in `engine/`. Each hook is an engine change that goes through review, and nothing goes live before the launch gates (Decision-Log entries 9 and 19).

## Hook points

| # | Where | What the ledger does |
|---|---|---|
| 1 | `engine/api/app.py` `create_session_endpoint`, before `wiring.create_session` | `AccessService.start_conversation(visitor_id, session_id)` holds one unit. If not admitted, no Representative session is created and the response carries the packs for the threshold sheet. |
| 2 | `engine/api/wiring.py` `handle_message`, after the `voice_turn` event is stored | `first_reply_stored(session_id)` captures the unit. Idempotent. |
| 3 | Idle scheduler (`engine.m4.idle_close`) or a separate job | `Ledger.release_idle_holds(older_than)` returns units for conversations that never got a reply. |
| 4 | `engine/m4/turn.py` session cap (`SESSION_TURN_CAP`, 10 today) | The cap comes from the session: 3 for a free conversation, 7 for a paid one, from `Started.turn_cap`. |
| 5 | `engine/api/anon_cap.py` | The daily session count overlaps the free allowance and is replaced by it. The per-IP burst limiter stays. See Decision-Log entry 6. |
| 6 | `engine/api/app.py`, new route | Mounts the Stripe webhook (`apply_event` behind `verify_signature`) and the checkout route. |
| 7 | Render config | New SQLite file `access.db` on the existing disk, added to the daily backup. `STRIPE_SECRET_KEY` (test key until counsel clears live), `STRIPE_WEBHOOK_SECRET`. |

The engine calls `AccessService` in process, so there is no HTTP hop between them. The HTTP module in the sandbox is for the webhook and for a separate deployment if one is ever wanted.

## Safety invariant (Decision-Log entry 1)

- The ledger is consulted at conversation start and at the first stored reply, never per message. An open conversation continues with no ledger call.
- Today `anon_cap.py` returns 429 and a closed session returns 409 before the safety gate runs (Open_Gaps_Tracking entry 1). Hooks 1 and 5 must not repeat that.
- Tests required with the hook: a zero-balance visitor with an open conversation can still send a message that reaches the safety gate; no purchase prompt is returned after a safety event.

## Open: the zero-balance safety path

At creation there is no participant message yet, so refusing a start blocks nothing that was typed. The gap is a visitor in distress with no balance and no open conversation: the threshold sheet has no text box, so there is no way to reach the Facilitator.

Proposed, not decided: at zero balance the start screen still offers a Facilitator-only session. It holds no unit and has no Representative. Each message goes through the safety gate. If it is not a safety matter, the Facilitator answers with the threshold text and the packs. This extends the rule that the redirect belongs to the Facilitator. The draft AcuteDistress and HarmfulDynamic mechanism is not settled and is not assumed here.

## Open: unfinished conversations

A held unit that never gets a reply is released after an idle period. The research recommended that an unfinished conversation stay resumable for at least 7 days. Releasing the unit and resuming later means a second hold when the visitor returns. The idle period and the resume window are not set.

## Out of scope at pilot

Table sessions keep their own round cap and are not sold in packs until their cost is measured. The church and class pool is a later increment.
