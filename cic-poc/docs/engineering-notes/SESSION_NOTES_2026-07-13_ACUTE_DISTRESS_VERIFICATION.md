# Live Verification — Acute-Distress/Harmful-Dynamic Mechanism — 2026-07-13

**Scope:** verifying the relational-safety mechanism merged from `origin/claude/cic-poc-acute-distress-mechanism` (commit `4efa085`) into `claude/cic-poc-backend-facilitator-upgrade`, per `SESSION_NOTES_2026-07-13_ACUTE_DISTRESS.md`'s own disclosure that it had only been `py_compile`-checked, never live-tested.

**Verdict: two real bugs found and fixed. With the fixes, the mechanism now behaves correctly against the design doc's own worked examples plus a set of adversarial variants, tested via direct API calls against the live backend (not just casual click-through).**

---

## Bugs found (both fixed in this pass, not by the original implementing thread)

### 1. CRITICAL — every first-time crisis disclosure got the wrong (vague) response

**Symptom, reproduced live 3× via the actual `/api/session/{id}/message/stream` endpoint:** a brand-new session's very first Acute-Distress disclosure — including an explicit-plan A2 case ("I already have a plan for how I'd do it...") — got the *continuation* script ("I'm still here with you... What I offered a moment ago still stands") instead of the full check-in script. Same for the first-ever Harmful-Dynamic fire. The continuation script explicitly references "what I offered a moment ago," which never actually happened on a first-ever fire — it read as broken/incoherent, and worse, skipped the substantive safety content entirely: for A2 specifically, it never asked "is there anyone tonight you could reach."

**Root cause:** in `main.py`, both endpoints applied `rs_updates` onto `state` (via `setattr`) *before* calling `stream_relational_safety_response(state, ...)`. That function determined "is this a fresh fire" by reading `state.track_a_active` / `state.track_b_active` / `state.track_a_severity` directly — but by the time it ran, those fields were already the *post-update* values (already `True`/`"A2"`), so "is this already active" always evaluated true. The full `FACILITATOR_ACUTE_DISTRESS_A1_PROMPT` / `_A2_PROMPT` / `FACILITATOR_HARMFUL_DYNAMIC_PROMPT` were effectively dead code — unreachable in the live flow, only exercisable by calling the function in isolation with hand-built state (which is how the bug went undetected by `py_compile` checks).

**Fix:** `stream_relational_safety_response` now takes explicit `pre_track_a_active`, `pre_track_a_severity`, `pre_track_b_active` parameters, used for the fresh-fire/continuation decision instead of re-deriving from the (already-mutated) `state` object. Both call sites in `main.py` (`/message` and `/message/stream`) now snapshot those three values before applying `rs_updates`, and pass them through explicitly. `cic-poc/backend/app/graph/nodes.py`, `cic-poc/backend/app/main.py`.

**Verified after fix:** live A2 first-disclosure now correctly produces the full script (identifies as Facilitator, takes it seriously, doesn't instruct, asks how they are, asks the one non-directive "is there someone tonight" question, closes with an open door). Live Harmful-Dynamic first-fire now correctly names the specific pattern and explains the Representative's real limit; a follow-up turn correctly gets the light-touch continuation instead of repeating the full script.

### 2. Compound-tag parsing — a single-message multi-tag Harmful-Dynamic signal silently failed to fire

**Symptom:** the classifier prompt's own worked example ("You're the only one who actually gets it, I look forward to this more than anything else in my day") is documented in the prompt itself as mapping to *three* tags at once (`CONFIDANT_LANGUAGE + AFFIRMATION_DEPENDENCE + RETURN_COMPULSION`). Reproduced 3/3 live: the LLM followed the prompt's own example and returned a single compound string (`"CONFIDANT_LANGUAGE,AFFIRMATION_DEPENDENCE,RETURN_COMPULSION"` or `"...+...+..."` depending on the run). The code treated this as one opaque tag, which never exactly matched any entry in the immediate-fire or pooled-tag sets — so a message containing `RETURN_COMPULSION`, which is supposed to fire Track B *immediately* on its own, silently failed to fire at all when it co-occurred with other tags in the same message. This is the same compound-label failure class already found and fixed once earlier this session in the drift-signal whitelist, recurring in the new mechanism.

**Fix:** `classify_relational_safety` now parses every known tag token out of the classifier's `detail` string (splitting on `+`/`,`/`/`/"AND"`, falling back to substring search) rather than treating it as one opaque string, and returns a `tags` list alongside the original single `tag` field for backwards compatibility. `update_relational_safety_state` now accumulates every tag from the turn individually and checks the immediate-fire/pooled-threshold logic against each one. `cic-poc/backend/app/graph/nodes.py`.

**Verified after fix:** the same three-tag message now correctly logs all three tags individually and fires Track B immediately (via the `RETURN_COMPULSION` component), both via direct function calls and confirmed reproducible.

---

## What was tested and passed (16/16 direct-call assertions, plus live end-to-end confirmation)

- Design doc's own contrastive pair: `HISTORICAL_OTHERNESS_DISORIENTATION` vs `ACUTE_DISTRESS` — including the case where the distinguishing context is in a *prior* turn, not the current message.
- `ACUTE_DISTRESS` A1 and A2 classification, including explicit-plan/means language.
- `HARMFUL_DYNAMIC_SIGNAL` single-tag and compound-tag cases.
- `AMBIGUOUS_LOW_CONFIDENCE` / `DISTRESS_ADJACENT`.
- **Anti-false-positive rule**: a long, deep, curious 6-turn-plus conversation, an ordinary historical/theological question, and genuine warmth toward the Representative all correctly classified `NO_SIGNAL` — turn count/depth/enthusiasm alone never trips a signal.
- **A1 → A2 escalation** within one session (severity only overwrites upward).
- **De-escalation**: an active Track A does *not* clear after one `NO_SIGNAL` turn, and *does* clear after two consecutive `NO_SIGNAL` turns (`track_a_active`, `track_a_severity`, `relational_safety_deescalation_count` all reset correctly).
- **Track B pooled threshold**: one `CONFIDANT_LANGUAGE`/`AFFIRMATION_DEPENDENCE` tag does not fire; a second pooled tag crosses the threshold and fires.
- **Track B immediate tag**: a single `RETURN_COMPULSION` tag fires on its own, no pooling required.
- **Live end-to-end** (real streaming endpoint, real sessions): fresh A2 disclosure → full A2 script with the "is there someone tonight" question; fresh Harmful-Dynamic fire → full pattern-naming script; follow-up turn → correct light-touch continuation, not a repeat of the full script.

## Known, disclosed-but-not-fixed inconsistency (not blocking, flagging for awareness)

`state.py`'s field comment for `relational_safety_deescalation_count` says de-escalation counts "two consecutive turns classified `NO_SIGNAL` or `HISTORICAL_OTHERNESS_DISORIENTATION`," but the actual code in `update_relational_safety_state` only increments/clears on `NO_SIGNAL` — `HISTORICAL_OTHERNESS_DISORIENTATION` is deliberately treated as non-clearing per `nodes.py`'s own inline comment ("can co-occur with genuine ongoing distress"). Confirmed live: an active Track A does not de-escalate across repeated `HISTORICAL_OTHERNESS_DISORIENTATION` turns. The code's behavior is the more conservative of the two and was left as-is; the `state.py` docstring is simply stale and should be corrected to match the code the next time that file is touched.

## Not yet tested

- Multi-world tables (this pass only used a single-world session).
- The non-streaming `/message` endpoint's relational-safety branch specifically (the streaming endpoint was exercised live; `/message`'s branch received the same code fix and passed the same direct-call unit tests, but was not separately exercised end-to-end through its own HTTP path).
- Any interaction between relational-safety firing and the frame-breaker check on the same turn (the two are coded as mutually exclusive with frame-breaker taking priority, but no adversarial message was constructed to actually test that boundary).
