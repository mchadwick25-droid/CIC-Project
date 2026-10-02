# Access and Monetization: Open Gaps

Append-only and numbered. A merged entry's number never changes. Cross-references cite subject and date, not a bare number.

## 1. Caps return an error before the safety gate runs (2026-10-02)

**Status:** OPEN. Found in the Opus round 1 review of the Access and Monetization research and re-verified against the source on 2026-10-02.

**What happens today.** Two paths refuse a participant's message before it reaches the safety gate in `run_turn`:

- `engine/api/anon_cap.py`: the anonymous daily cap middleware returns HTTP 429 on `POST /api/session/<id>/message` and `/continue` when the visitor's daily turn limit is used up. The request never reaches the route handler.
- `engine/api/wiring.py`: `handle_message` raises `SessionClosed` before `run_turn` is called, and the API turns it into a 409 for a closed session.

In both cases the message is never screened.

**What already works.** `engine/m4/turn.py` exempts acute crisis from the per-session turn cap (`SESSION_TURN_CAP`), so a message that is acute crisis is handled inside `run_turn`. The two paths above sit in front of it.

**Why it matters.** A paid-access ledger copying this pattern would turn a zero balance into a block on reaching the Facilitator. A participant in distress would meet a limit message instead of a redirect.

**Rule adopted for all access limits (Mark, 2026-10-02):** no balance, cap, paywall or purchase prompt may sit between a participant's message and the safety gate. A participant at zero balance, or at the end of the free allowance, can always reach the Facilitator. Purchase prompts stay hidden after a safety event. This extends the decided rule that the redirect belongs to the Facilitator and never to the Representative.

**Open:** the fix for the two existing paths is not made. It belongs with the design of the access ledger. The specifics of the draft AcuteDistress and HarmfulDynamic mechanism are not settled and are not assumed here.

## 2. Per-turn cost climbs with conversation depth, so a paid depth cap has no measured cost (2026-10-02)

**Status:** OPEN. Raised by Mark and checked against `engine/m8/reports/live-memory-growth-report.json` on 2026-10-02.

**What the measurement shows.** One real 10-turn session on Sonnet 4.5, voice, safety and reader calls included. Turn 2 cost $0.0174. Turn 10 cost $0.0331. The 10-turn conversation cost $0.2918, an average of $0.0292 a turn. The system prompt is cached and flat at 12,456 tokens. The uncached history grows from 1,306 tokens at turn 2 to 5,643 at turn 10, because `history_from_transcript` in `engine/api/wiring.py` replays the whole conversation on every turn.

**Projection, not a measurement.** A straight-line fit of turns 2 to 10, about +$0.0024 per added turn, extended: about $0.50 at 15 turns, $0.77 at 20 and $1.49 at 30. Total cost grows faster than the turn count.

**Caveats.** One session, one world (alx), short participant messages. Prompt cache lapse after a pause is not measured at this depth. A lapse would rewrite the 12.5k-token system prompt, about $0.05 by arithmetic from the rate card, and more than triple that turn.

**Consequence.** A pack priced from 10-turn cost is under-priced if buyers use deeper conversations. The paid depth and the price must be set together. The 5x markup question from the Opus round 1 review is worse with depth.

**Next step.** One measured run at the candidate paid depth, with realistic message lengths and a mid-conversation pause. See decision 11.
