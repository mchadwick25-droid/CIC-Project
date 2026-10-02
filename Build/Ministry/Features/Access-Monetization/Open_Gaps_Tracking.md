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
