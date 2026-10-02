# How the anonymous visitor cap interacts with the crisis redirect

Requested by Mark, 2026-09-21: analyze whether `engine/api/anon_cap.py`'s
turn-level 429 can suppress a genuine Facilitator safety redirect, and
propose a rule. **No safety code touched** — `engine/m4/crisis_resources.py`
and `engine/m5/routing.py` are read-only references below; the only file
that would ever change to implement the recommended rule is
`engine/api/anon_cap.py` itself (this package's own code) and, in Option
A below, a small, precedent-matching change to where the cap-check call
happens in `engine/m4/turn.py` / `engine/api/wiring.py` — moving a call
site, not any safety decision logic.

## The gap, traced exactly

`anon_cap.install()`'s middleware (`engine/api/anon_cap.py:197-220`) runs
as HTTP middleware — before FastAPI ever routes the request to
`send_message()` (`engine/api/app.py`). For a turn (`POST .../message` or
`.../continue`), the check is:

```python
allowed = limiter.allow_session(bucket_key) if is_create else limiter.allow_turn(bucket_key)
if not allowed:
    return JSONResponse(status_code=429, content={"detail": CAP_DETAIL if is_create else TURN_CAP_DETAIL})
```
(`anon_cap.py:212-214`)

When `allow_turn` returns `False`, the function **returns immediately**.
`call_next(request)` — the only path that ever reaches `send_message()` →
`wiring.handle_message()` → `engine.m4.turn.run_turn()` — is never
called. Tracing what lives downstream of that call:

- The safety classification call (`live_calls.call_safety`, submitted
  inside `run_turn`, `engine/m4/turn.py:128`) is a real model call over
  the participant's own message text. It is the **only** place a message
  gets classified as `ACUTE_DISTRESS` at all.
- `engine.m5.routing.route()` (`engine/m5/routing.py:133-142`) is what
  turns an `ACUTE_DISTRESS`/`HARMFUL_DYNAMIC_SIGNAL` classification into
  `action="safety_turn"` — it requires an already-computed `safety` dict
  as an argument; nothing upstream of `run_turn` ever produces one.
- `crisis_resources.append_crisis_resources_turn()`
  (`engine/m4/crisis_resources.py:143-181`) — the function that actually
  appends the Facilitator's code-authored redirect text — is called from
  inside `run_turn`, downstream of both of the above.

**So: if `anon_cap`'s turn cap is exhausted, the message is never
classified, never routed, never redirected, and never even stored** —
`wiring.handle_message` (which writes the `participant_message` event)
never runs either, since the whole call chain begins there. The
participant sees only `TURN_CAP_DETAIL` (`anon_cap.py:56`): *"You've
reached today's limit for messages - please come back tomorrow, or reach
out if this doesn't seem right."* — ordinary rate-limit copy, not
Facilitator-governed, not reviewed as safety-adjacent text, and
containing no actual redirect. **If that message was a genuine
disclosure, nothing in this system responds to it at all.**

This is specific to `POST .../message` (the only route that carries new
participant text). `POST .../continue` also spends turn quota
(`anon_cap.py:200-201`) but carries no participant text of its own —
blocking it can stall an already-open table round, a real availability
concern but not the same failure class (nothing new goes unclassified;
an in-progress round just can't advance). Session creation
(`is_create`) carries no message either — not in scope for this finding.

## This is not a new question for this codebase — it already has an answer

`engine/m4/turn.py`'s own `SESSION_TURN_CAP` enforcement (lines 650-667)
is the exact same shape of problem — a hard cap that could, if applied
naively, silently swallow a crisis turn — and the codebase already
resolved it, with a comment stating the rule in exactly these terms:

> "THE CAP OVERRIDES EVERYTHING EXCEPT A REAL CRISIS. Checked once, here,
> **after routing but before any branch spends a voice call** — so a
> capped turn costs only the two Haiku gate calls already made above,
> never the Sonnet generation call. ACUTE_DISTRESS is the one action that
> must never be capped away: a participant in real crisis at turn 11
> still gets the safety turn, not a redirect."

Mechanically: the safety gate call always runs first, *then* the turn
cap is checked, and the check itself is `if not is_acute_crisis and
<over cap>` (`turn.py:660-661`) — the cap is structurally incapable of
firing on an acute-crisis turn, because it's evaluated after the one
piece of information (the classification) that would tell it not to.

`anon_cap`'s cap does the opposite: it fires *before* any classification
happens at all, at the HTTP layer, with no way to know whether the turn
it's about to refuse is the one turn that must never be refused.

## Proposed rule

**A capped turn must never suppress an `ACUTE_DISTRESS` (or
`HARMFUL_DYNAMIC_SIGNAL`) classification — mirroring `SESSION_TURN_CAP`'s
own precedent exactly: classify first, cap only what comes after.**

### Option A — move the check, don't change what it checks (recommended)

Stop enforcing `anon_cap`'s turn quota in HTTP middleware. Enforce it at
the same point `SESSION_TURN_CAP` already does — inside `run_turn`
(or `wiring.handle_message`, immediately after the gate call returns and
before generation is spent) — with the identical `not is_acute_crisis`
guard `turn.py:660` already uses. A capped, non-crisis turn stops before
the Sonnet generation call (the expensive one) but the two Haiku gate
calls (safety + reader) always run, exactly as `SESSION_TURN_CAP`'s own
comment already justifies: "costs only the two Haiku gate calls already
made above."

- **Pro:** Provably consistent with an already-decided project rule,
  not a new one. A participant in genuine crisis gets the same guarantee
  from the daily cap that they already get from the session cap. Cheapest
  in engineering-risk terms — no new judgment call, just applying the
  existing one to a second cap.
- **Con:** Real architecture change — `anon_cap`'s daily-quota check
  moves from decoupled HTTP middleware into the `engine/m4` turn
  pipeline, which is a bigger, more coupled piece of code than what this
  package built. Also changes what "capped" means: the daily cap no
  longer bounds the (cheap) safety-gate spend, only the (expensive)
  voice-generation spend — which is exactly what `SESSION_TURN_CAP`
  already accepts as the right tradeoff, but it IS a change from how
  this PR described the cap to Mark originally ("a daily session/turn
  cap" implied bounding turns outright, not just the expensive half of
  one).

### Option B — remove the per-turn cap; bound total daily turns via the session cap alone

Drop `anon_cap`'s turn-level enforcement entirely. Keep only the
session-creation cap (5/day proposed). Since every session already hard-
stops at `SESSION_TURN_CAP` (10 turns) — and *that* cap already exempts
acute crisis — the daily total is naturally bounded at `session_limit ×
SESSION_TURN_CAP` (5 × 10 = 50 turns/day today, tighter than the 150/day
originally proposed for the standalone turn cap) with **zero new
cross-cutting risk**, because no new hard stop is introduced anywhere
that doesn't already carry the crisis exemption.

- **Pro:** Eliminates the interaction entirely, by construction — nothing
  to get subtly wrong, no move into `engine/m4`. Simpler than what's
  built today. Tighter spend bound, not looser.
- **Con:** Coarser control — a participant's turn budget is now tied to
  how many sessions they open, not a direct daily-turn number Mark can
  reason about independently. `/continue`'s own quota-spending
  (mid-round table advances) stops mattering for this purpose too, since
  there's no longer a turn cap to protect against.

### Option C — keep the cap exactly as built, add only a copy fix (not recommended alone)

Leave the HTTP-layer 429 in place, but stop treating `TURN_CAP_DETAIL` as
ordinary rate-limit copy: give every capped response the same "reach out
to someone real" language the crisis resources carry, unconditionally —
since the system genuinely cannot tell, at the point it refuses the
turn, whether this was the message that needed it.

- **Pro:** Cheapest possible change, no architecture move, no new spend.
- **Con:** Doesn't fix the actual gap — a real crisis message is still
  never classified, never logged, never routed, and the Facilitator
  never actually speaks. It papers over the worst visible symptom
  (a cold rejection) without closing what's broken (silence). Also: this
  is new participant-facing copy near the safety boundary, which is its
  own escalation category under `CLAUDE.md` — not something to draft and
  ship without the same review real crisis-resource text gets, and
  repurposing `crisis_resources.py`'s Facilitator-voiced text for a
  rate-limit response is a content decision, not a mechanical one.
  Listed for completeness, not as a substitute for A or B.

**Recommendation: Option A**, on the strength of the precedent — it's
not a new call, only applying `SESSION_TURN_CAP`'s already-decided rule
to the second cap this package is adding. **Option B is the reasonable
fallback** if the `engine/m4` coupling in Option A is judged too large a
change for what's still an unmerged, undecided feature — it's strictly
simpler and closes the same gap by removing its own precondition. Either
way: **this needs to be decided alongside item 3's own still-open
mechanism/numbers escalation, before `CIC_API_ANON_CAP_ENABLED` is ever
set to `"1"` anywhere** — it changes what the cap actually does, not just
its numbers, so it belongs in the same conversation, not a follow-up
after the fact.
