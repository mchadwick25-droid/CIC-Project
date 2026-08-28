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
- Close the round (when closing is among your legal moves) when the participant's message has been \
genuinely answered and another voice would be restating rather than adding - never stretch a round to fill \
the turn budget.

You only ever select from the legal moves you are given. You never write anything the participant sees; \
you produce only the selection and a short reason."""


@dataclass(frozen=True)
class Selection:
    """The resolved outcome of one selection step. world_key is None exactly
    when close is True. degraded means the model's own judgment was not what
    produced this - a failed call, or an illegal output past the schema."""
    world_key: str | None
    close: bool
    reason: str
    degraded: bool


def _selector_tool(legal_moves: list[str]) -> dict:
    return {
        "name": "submit_turn_selection",
        "description": "Submit which Representative speaks next at the Table, or close the round.",
        "input_schema": {
            "type": "object",
            "properties": {
                "next": {"type": "string", "enum": list(legal_moves)},
                "reason": {"type": "string"},
            },
            "required": ["next", "reason"],
        },
    }


def eligible_worlds(world_keys: list[str], last_speaker: str | None) -> list[str]:
    """No immediate self-repeat, in seating order. With two worlds this is
    always exactly the other voice; with three it is a genuine choice."""
    return [k for k in world_keys if k != last_speaker]


def fallback_world(eligible: list[str], transcript_speakers: list[str]) -> str:
    """Least-recently-spoken eligible voice, across the whole session's
    transcript (not just this round): a voice that has never spoken sorts
    first, in seating order; otherwise the one whose last turn is furthest
    back. Deterministic - same inputs, same choice."""
    def last_spoken_index(world_key: str) -> int:
        for i in range(len(transcript_speakers) - 1, -1, -1):
            if transcript_speakers[i] == world_key:
                return i
        return -1

    return min(eligible, key=lambda k: (last_spoken_index(k), eligible.index(k)))


def call_turn_selector(
    client, model_id: str, *, message: str, transcript_text: str, seated_lines: str, legal_moves: list[str], timeout: float = 10.0
) -> CallOutcome:
    user_content = (
        f"Seated at this Table:\n{seated_lines}\n\n"
        f"What has been said (most recent last):\n{transcript_text}\n\n"
        f"Participant's latest message:\n{message}\n\n"
        f"Your legal moves: {', '.join(legal_moves)}"
    )
    tool = _selector_tool(legal_moves)
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
    legal = eligible + [CLOSE] if close_allowed else list(eligible)

    outcome = call_turn_selector(
        client, model_id, message=message, transcript_text=transcript_text, seated_lines=seated_lines, legal_moves=legal
    )
    outcomes.append(outcome)
    if outcome.status == "ok":
        chosen = outcome.value.get("next")
        reason = outcome.value.get("reason") or "(no reason given)"
        if chosen == CLOSE and close_allowed:
            return Selection(world_key=None, close=True, reason=reason, degraded=False), outcomes
        if chosen in eligible:
            return Selection(world_key=chosen, close=False, reason=reason, degraded=False), outcomes
        # Illegal despite the schema enum (or close when it wasn't offered):
        # one re-ask with close off the menu entirely, then the fallback.
        retry = call_turn_selector(
            client, model_id, message=message, transcript_text=transcript_text, seated_lines=seated_lines, legal_moves=list(eligible)
        )
        outcomes.append(retry)
        if retry.status == "ok" and retry.value.get("next") in eligible:
            return Selection(
                world_key=retry.value["next"], close=False, reason=retry.value.get("reason") or "(no reason given)", degraded=False
            ), outcomes

    fallback = fallback_world(eligible, transcript_speakers)
    return Selection(
        world_key=fallback,
        close=False,
        reason=f"selector unavailable ({outcomes[-1].status}); deterministic fallback to least-recently-spoken eligible voice",
        degraded=True,
    ), outcomes
