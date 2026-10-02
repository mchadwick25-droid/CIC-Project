"""The Table's turn selector (Artifact-7 SS5): before each table voice
turn, one small forced-tool-use call chooses the next speaker or closes the
round. Judgment lives in the model's prompt; the RULES live here, in code,
and are never delegated to it:

- no immediate self-repeat (the last speaker is simply not a legal move);
- "close" is not offered below the round floor;
- an illegal or failed selection falls back deterministically to the
  least-recently-spoken eligible voice, and the turn_selected event carries
  degraded=true with the fallback stated in its reason - a selector outage
  degrades allocation judgment, never the grounding or safety of the turns
  themselves (the cap, and every gate decision, are the round loop's own).

The legal moves are enforced twice: baked into the tool schema's enum (the
model cannot even type an illegal key) and re-checked on the way out (a
schema is a guardrail, not a guarantee). Deliberately self-contained rather
than importing engine.m5.live_calls' private helper: the sealed safety
machinery shares nothing with iterated machinery (spec principle 5), and
that separation is worth twenty duplicated lines.

Selection guidance in the prompt follows Table Process V1.0 SS2: "most
directly positioned" first, with the breadth-of-voice preference - favor a
voice that has not yet spoken this round when the question is genuinely
open to all, without making rotation a rule.

REPRESENTATIONAL FAIRNESS ON RETURN PICKS: a reviewer's finding, across
every real transcript reviewed with
the same 3-seat trio, the two traditions carrying more elaborated,
cross-referencing technical vocabulary (Cappadocian, Alexandrian - both
argue theosis in their own terms) kept getting the return/final-word
picks; the thinner, earlier-period voice (the house-churches) was heard
once, in its first pass, and never brought back - not because its own
record had nothing left to add, but because two voices sharing the same
vocabulary makes a more visible "continue this" thread than a voice whose
real contribution is practice, embodiment, or its own admitted
uncertainty. Small, non-randomized sample (same worlds, same broad
question, informal repeats) - real enough to name directly in the prompt
rather than wait for a designed study, and not a hard quota: rotation is
still never forced - random or opportunistic
selection is fine.
"""
from dataclasses import dataclass

from anthropic import APIError, APITimeoutError

from engine.m5.failure import CallOutcome

CLOSE = "close"

SELECTOR_SYSTEM_PROMPT = """You are the turn selector for a Table conversation: a participant in \
conversation with two or three Representatives, each a voice formed by a different early-Christian \
formation world. Given the participant's latest message and what has been said at the Table since, choose \
which Representative speaks next, or close the round when it has genuinely finished.

How to choose, in order:
- Choose the Representative most directly positioned to respond to what was just said - addressed by name, \
asked directly, or holding the formation the moment genuinely calls for.
- When the participant's question is genuinely open to all voices ("what do each of you think"), prefer a \
Representative who has not yet spoken this round over returning to one who has, all else being roughly \
equal - the participant should witness the same question received by genuinely different ways of thinking. \
This is a preference, not a rotation: a Representative with a real, specific response to what was just \
said is still the right choice over an as-yet-silent one when the moment calls for it.
- A round does not need to include every Representative every time. If the question was specific to one or \
two voices, the others staying silent is a correct outcome, not a failure.
- A tradition with a thinner, less systematized record is not a tradition with nothing left to add on a \
return. Two voices sharing the same technical vocabulary (a shared term, a shared argument) makes an obvious \
thread to continue - but a voice whose real contribution is lived practice, embodiment, or its own honestly \
admitted uncertainty has just as real a thread worth returning to, even when it does not announce itself in \
matching language. Do not let how much doctrinal apparatus a world argues out decide who gets brought back. \
If the same one or two voices keep getting the return picks, ask whether that is genuinely the moment \
calling for it, or just the easier thread to see.
- Close the round (when closing is among your legal moves) when the participant's message has been \
genuinely answered and another voice would be restating rather than adding - never stretch a round to fill \
the turn budget.

When you choose a Representative who has already spoken this round - a return, not their first turn - also \
set `engages` to the ONE prior speaker (this round) their return is meant to respond to: the specific \
alignment or contrast their next turn should focus on, not a survey of everyone who has spoken. Leave \
`engages` unset when `next` is a Representative's first turn this round, or when you are closing.

You only ever select from the legal moves you are given. You never write anything the participant sees; \
you produce only the selection and a short reason."""


@dataclass(frozen=True)
class Selection:
    """The resolved outcome of one selection step. world_key is None exactly
    when close is True. degraded means the model's own judgment was not what
    produced this - a failed call, or an illegal output past the schema.

    engages (a structural fix for a repeat failure mode: raising
    the round floor after a full-table-synthesis close only moved where the
    same collision happened, since a return turn was always structurally
    exposed to every prior voice at once with nothing scoping it to one).
    None exactly when world_key is a Representative's FIRST turn this round
    (nothing to engage yet) or when close is True; otherwise the ONE prior
    speaker this return is engaging - resolved (never left to a hopeful
    prompt alone) by _resolve_engages on every path, model pick, retry,
    forced move, and fallback alike."""
    world_key: str | None
    close: bool
    reason: str
    degraded: bool
    engages: str | None = None


def _selector_tool(legal_moves: list[str], round_speakers: list[str]) -> dict:
    properties = {
        "next": {"type": "string", "enum": list(legal_moves)},
        "reason": {"type": "string"},
    }
    if round_speakers:
        # De-duplicated, in the order each first spoke this round (not the
        # model's own) - a plain legal-values list, same discipline as
        # `next`'s own enum.
        already_spoken = list(dict.fromkeys(round_speakers))
        properties["engages"] = {
            "type": "string",
            "enum": already_spoken,
            "description": (
                "Required when `next` names a Representative who has already spoken this round: which "
                "ONE of their own prior turns this pick's next turn specifically responds to. Leave unset "
                "when `next` is a Representative's first turn this round, or when closing."
            ),
        }
    return {
        "name": "submit_turn_selection",
        "description": "Submit which Representative speaks next at the Table, or close the round.",
        "input_schema": {
            "type": "object",
            "properties": properties,
            "required": ["next", "reason"],
        },
    }


def _resolve_engages(chosen: str, round_speakers: list[str] | None, requested: str | None) -> str | None:
    """None when `chosen` is a first-time speaker this round - nothing to
    engage yet, whatever the model (or a forced/fallback move, which never
    asks it at all) supplied. Otherwise the model's own requested target
    when it names a real prior speaker other than `chosen` itself;
    deterministically the most recent OTHER speaker in the round if the
    field was left unset or named `chosen` or a stranger. eligible_worlds'
    own no-immediate-self-repeat rule guarantees round_speakers[-1] differs
    from `chosen` on every call path (forced move, real pick, retry, and
    fallback all draw `chosen` from `eligible`, which excludes the last
    speaker), so a return is never left unscoped - by an omitted field, a
    self-reference, or a mechanical pick that never consulted a model."""
    round_speakers = round_speakers or []
    if chosen not in round_speakers:
        return None
    if requested in round_speakers and requested != chosen:
        return requested
    return round_speakers[-1]


def eligible_worlds(world_keys: list[str], last_speaker: str | None) -> list[str]:
    """No immediate self-repeat, in seating order. With two worlds this is
    always exactly the other voice; with three it is a genuine choice."""
    return [k for k in world_keys if k != last_speaker]


def fallback_world(eligible: list[str], transcript_speakers: list[str]) -> str:
    """Least-recently-spoken eligible voice, across the whole session's
    transcript (not just this round): a voice that has never spoken sorts
    first; otherwise the one whose last turn is furthest back. Deterministic
    - same inputs, same choice - genuinely, not just in practice: the tie-
    break among never-spoken voices is alphabetical on the world_key itself,
    never `eligible`'s own incoming order. It used to be
    the latter, and "same choice" was only ever true because every caller
    happened to pass `eligible` in a stable seating order - the moment
    table_wiring started reshuffling that order per call to fix responses
    always coming in the same order, this function's
    own documented guarantee broke silently. A tie-break keyed to the
    caller's incoming order was never really deterministic; it was
    borrowing determinism from a caller invariant this function had no way
    to enforce."""
    def last_spoken_index(world_key: str) -> int:
        for i in range(len(transcript_speakers) - 1, -1, -1):
            if transcript_speakers[i] == world_key:
                return i
        return -1

    return min(eligible, key=lambda k: (last_spoken_index(k), k))


# TARGET LENGTH: for 2 voices and a participant, the max turns is 5, 4
# being the ultimate zone; for 3 voices the cap is 6, 5 being the
# ultimate zone.
# Deliberately a SECOND, softer number from the hard cap the round loop
# itself enforces (engine.m4.round.RoundConfig.cap_for) - no hard cap or
# post-conversation monitoring, just a small increased
# pressure placed as guidance here,
# in the selector's own reasoning, never a second code-enforced gate. Only
# two table sizes exist (Artifact-7 SS1: world_keys 2-3), so this is a
# plain lookup of two authored numbers, not a formula.
_TARGET_TURNS_BY_SEATS = {2: 4, 3: 5}


def round_facts(world_keys: list[str], round_speakers: list[str]) -> str:
    """Code-computed round state, stated to the selector outright (Artifact-7
    SS5's "eligibility facts computed in code") rather than left for it to
    infer from a flat transcript window. This closes a real defect found on
    a live run: the selector's R2-pos3 reason opened with "Theon has not yet
    responded to this round's question" when Theon had spoken at position 1
    of that round - the decision itself was defensible, but a turn_selected
    event's reason is an audit surface (M7), and a false factual sentence in
    it is a defect. The model no longer has to reconstruct round boundaries
    it was never told.

    Carries the target-length guidance too - a preference
    stated as a fact about this table's usual shape, not a rule, and never
    seen by the participant either way (this whole string is selector-only
    reasoning input, same as the rest of this function)."""
    if round_speakers:
        spoken = "; ".join(f"{k} (position {i + 1})" for i, k in enumerate(round_speakers))
    else:
        spoken = "(no one - this is the round's opening turn)"
    unheard = [k for k in world_keys if k not in round_speakers]
    target = _TARGET_TURNS_BY_SEATS.get(len(world_keys))
    target_line = (
        f" A round at this {len(world_keys)}-seat table most often finishes well around turn {target} - "
        "a preference, never a rule: close as soon as the exchange is genuinely finished, and let it run "
        "longer only when a voice still has something real left to add."
        if target else ""
    )
    return (
        f"Spoken THIS round, in order: {spoken}. "
        f"Not yet heard this round: {', '.join(unheard) if unheard else '(every voice has spoken this round)'}."
        f"{target_line}"
    )


def call_turn_selector(
    client, model_id: str, *, message: str, transcript_text: str, seated_lines: str, legal_moves: list[str],
    round_facts_text: str = "", round_speakers: list[str] | None = None, timeout: float = 10.0
) -> CallOutcome:
    facts_block = f"Round state (computed, trust it over your own reading):\n{round_facts_text}\n\n" if round_facts_text else ""
    user_content = (
        f"Seated at this Table:\n{seated_lines}\n\n"
        f"What has been said (most recent last):\n{transcript_text}\n\n"
        f"{facts_block}"
        f"Participant's latest message:\n{message}\n\n"
        f"Your legal moves: {', '.join(legal_moves)}"
    )
    tool = _selector_tool(legal_moves, round_speakers or [])
    try:
        response = client.messages.create(
            model=model_id,
            max_tokens=300,
            system=SELECTOR_SYSTEM_PROMPT,
            tools=[tool],
            tool_choice={"type": "tool", "name": tool["name"]},
            messages=[{"role": "user", "content": user_content}],
            timeout=timeout,
        )
    except APITimeoutError:
        return CallOutcome(status="timeout")
    except APIError as e:
        return CallOutcome(status="error", value={"error": str(e)})

    tool_uses = [b for b in response.content if b.type == "tool_use" and b.name == tool["name"]]
    if not tool_uses:
        return CallOutcome(status="parse_failure", value={"raw": [b.model_dump() for b in response.content]})
    return CallOutcome(status="ok", value=tool_uses[0].input, raw_usage=getattr(response, "usage", None))


def select_speaker(
    client,
    model_id: str,
    *,
    message: str,
    transcript_text: str,
    seated_lines: str,
    world_keys: list[str],
    last_speaker: str | None,
    close_allowed: bool,
    transcript_speakers: list[str],
    round_speakers: list[str] | None = None,
) -> tuple[Selection, list[CallOutcome]]:
    """One selection step, rules enforced. Returns the resolved Selection
    and every CallOutcome made along the way (0, 1, or 2 - the caller
    records usage from them; a fallback with no successful call still cost
    whatever the failed attempts cost).

    close_allowed is the round loop's own floor/cap judgment - this function
    neither knows nor cares why closing is or isn't on the table this step.
    """
    eligible = eligible_worlds(world_keys, last_speaker)
    outcomes: list[CallOutcome] = []
    if not close_allowed and len(eligible) == 1:
        # FORCED MOVE - no selector call: with closing off the table and
        # one eligible voice,
        # there is no judgment to exercise, and both live runs showed the
        # model, asked anyway, confabulating a justification ("Theon has
        # not yet spoken this round" about a voice that opened the round) -
        # even with the round facts stated. A forced move gets a
        # code-written reason the M7 audit can trust, and at a two-seat
        # table this also removes two of every three selector calls.
        return Selection(
            world_key=eligible[0],
            close=False,
            reason="only eligible voice this position - no immediate self-repeat, and the round floor is not yet met (forced move, no selector call)",
            degraded=False,
            engages=_resolve_engages(eligible[0], round_speakers, None),
        ), outcomes
    legal = eligible + [CLOSE] if close_allowed else list(eligible)
    facts = round_facts(world_keys, round_speakers or [])

    outcome = call_turn_selector(
        client, model_id, message=message, transcript_text=transcript_text, seated_lines=seated_lines, legal_moves=legal,
        round_facts_text=facts, round_speakers=round_speakers,
    )
    outcomes.append(outcome)
    if outcome.status == "ok":
        chosen = outcome.value.get("next")
        reason = outcome.value.get("reason") or "(no reason given)"
        if chosen == CLOSE and close_allowed:
            return Selection(world_key=None, close=True, reason=reason, degraded=False), outcomes
        if chosen in eligible:
            engages = _resolve_engages(chosen, round_speakers, outcome.value.get("engages"))
            return Selection(world_key=chosen, close=False, reason=reason, degraded=False, engages=engages), outcomes
        # Illegal despite the schema enum (or close when it wasn't offered):
        # one re-ask with close off the menu entirely, then the fallback.
        retry = call_turn_selector(
            client, model_id, message=message, transcript_text=transcript_text, seated_lines=seated_lines, legal_moves=list(eligible),
            round_facts_text=facts, round_speakers=round_speakers,
        )
        outcomes.append(retry)
        if retry.status == "ok" and retry.value.get("next") in eligible:
            retried = retry.value["next"]
            return Selection(
                world_key=retried, close=False, reason=retry.value.get("reason") or "(no reason given)", degraded=False,
                engages=_resolve_engages(retried, round_speakers, retry.value.get("engages")),
            ), outcomes

    fallback = fallback_world(eligible, transcript_speakers)
    return Selection(
        world_key=fallback,
        close=False,
        reason=f"selector unavailable ({outcomes[-1].status}); deterministic fallback to least-recently-spoken eligible voice",
        degraded=True,
        engages=_resolve_engages(fallback, round_speakers, None),
    ), outcomes
