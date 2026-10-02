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

## 3. Measured cost of a 15-turn conversation and the prompt-cache lapse (2026-10-02)

**Status:** OPEN. Follows entry 2. A scratch run, not committed: 15 scripted turns, world alx, Sonnet 4.5 voice and Haiku 4.5 safety on Bedrock (us-east-1), one 6-minute pause after turn 7, priced with the repo's own cost function (Anthropic rate card, not an AWS invoice).

**Result.** Total $0.706 for 15 turns. Turn 1 $0.025, turn 7 $0.043, turn 14 $0.063. Uncached history grew from 1,105 to 12,564 tokens by turn 14. The cached system prompt is now 15,040 tokens (12,456 in the August run). After the 6-minute pause the cache had lapsed: turn 8 cost $0.094 against about $0.046 expected. The first 10 turns cost $0.42 including that rewrite.

**Against entry 2's projection.** About $0.50 was projected for 15 turns. The measured $0.706 is about 40% higher, because participant messages and replies were longer than in the August run. The August 10-turn figure ($0.29) was a best case.

**Caveats.** One world, one scripted conversation, one pause, fixed message text. Not a sample of real participants.

## 4. Replies end mid-sentence at the 1,024-token output limit (2026-10-02)

**Status:** OPEN. Found in the run of entry 3.

**What happens.** 7 of 15 replies (turns 6, 7, 9, 11, 12, 13, 14) end mid-sentence, for example turn 7 ends "At our worst—". Most replies run 550 to 830 words. Output hit exactly 1,024 tokens on 8 turns. `max_tokens` defaults to 1024 in both `engine/m4/generation.py` and `engine/m4/streaming.py`, and `wiring.handle_message` calls the same `run_turn`.

**Why it matters here.** The access design's protection rule says a cut-off reply never costs a unit. If cut-off replies are this common in deep conversations, the rule would be waived often, or the limit has to change first. Raising the limit raises cost and works against the readability target, so this is also a voice-length question.

**Open:** whether production truncates the same way. The scratch run used `run_turn` directly, so the production display path is not confirmed.

## 5. Representative sometimes repeats the participant's words instead of answering (2026-10-02)

**Status:** OPEN. Raised by Mark after the 3-turn sample.

**What happens.** When the first message opens with a first-person statement ("I grew up in a church where nobody asked hard questions. Who was Jesus to your people?"), some replies open by repeating it. Across the six replies seen to that message, one echoed it in the first person ("I grew up in a church&hellip; I want to know:"), two repeated it in the second person ("You grew up in a church where nobody asked hard questions. Then you belong with us."), and three answered cleanly. Two replies to the same question without the opener, and two to the opener as a statement with no question mark, were clean.

**Rule broken.** The alx prompt says the first sentence answers the first ask. No instruction asks for restating.

**Not known.** The rate (small sample, one world), whether it happens in other worlds, and when it began. Replies are not stored in git, so history cannot date it. The route in each case was `voice_with_directive`, so this turn's private directive from `engine/m4/turn_prep.py` is involved or at least present. Cause not confirmed.

**Next:** run the same probe in two more worlds before any change to a prompt or directive.

## 6. Restating of the participant's words: Mark is removing it (2026-10-02)

**Status:** IN PROGRESS, owned by Mark and the voice work, not this module. Follows entry 5.

**Direction (Mark):** the Representative no longer restates the participant's question or statements before answering. Entry 5 stays open until a re-run shows replies open with the answer.

**What this module needs from it:** a re-run of the same turn-1 probe (the opener message with and without a question) and the 3-turn free sample after the change, since the free allowance's first impression depends on it. The 3-turn sample's cost also changes if replies get shorter (entry 12).

**Not done here:** no prompt, directive or engine file was edited by this module.

## 7. Replies arrive in one block after 17 to 34 seconds (2026-10-02)

**Status:** OPEN. Raised by the Opus market buy-in review and checked in the code on 2026-10-02.

**What happens.** `engine/api/config.py` defines `streaming_enabled` (`CIC_API_STREAMING`), and no other file reads it. The message endpoint returns a full reply, so a participant sees nothing until the whole reply is ready. The 15-turn run measured 17 to 34 seconds per turn.

**Why it matters here.** The free allowance's first impression is a 25-second wait for a long reply. The buy-in review names this, the echo (entry 5) and reply length (entry 12) as the three defects to fix before a paid launch.

## 8. Cut-off replies handed to the build assessment and cleanup thread (2026-10-02)

**Status:** HANDED OFF. Follows entries 4 and 7.

**Direction (Mark):** a sentence is never cut off. The cut-off is a build issue, so it goes to the CIC build assessment and cleanup thread (session `session_01AmzAo9RfEp4W8U5pd1RVx2`) to solve. This module continues the analysis and the Sandbox build.

**Sent to that thread:** the measured cut-offs (replies 6 and 7 of the first 7 end mid-sentence at the 1,024-token limit), the two code locations that default `max_tokens` to 1024, the small cost of finishing the replies (about $0.012 per 7-turn conversation), decisions 12 and 20, and the two related launch-gate defects (the restating, and streaming with no reader of its flag).

**Not confirmed:** whether the live display path shows the cut text as the direct `run_turn` call did. That thread is asked to verify before changing code.

**Closes when:** that thread reports a fix and a test that fails on a mid-sentence ending, and a re-run of the 7-turn sample shows every reply ending on a full stop.
