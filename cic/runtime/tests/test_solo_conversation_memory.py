"""Solo (Deep Interview) Representatives must receive the conversation.

Before the fix these tests guard, _prepare_representative_turn built the
public transcript every turn and discarded it in single-world mode: the
injection was gated on is_multi_world. A solo turn was sent exactly two
messages - the cached system prompt and the participant's latest line -
so the Representative could see neither its own prior turns nor the
participant's, and every continuity instruction in _HOW_YOU_ENGAGE was
unexecutable by construction.

What each test is actually protecting:

  carries_history        the fix itself
  not_in_static_prompt   the COST property - if the record ever drifts
                         into the cached block it invalidates the prefix
                         on every turn, which is a large silent bill
  multi_world_unchanged  the multi-world path is untouched (this fix is
                         an elif on a branch that path takes first)
  first_turn_clean       no empty scaffolding when there is no history
  cost_is_flat           the 2+10 window caps growth, so per-turn cost
                         does not rise with conversation length
  elision_marker         documents the KNOWN LIMITATION rather than
                         pretending it away: past the window, the middle
                         of a conversation is not visible

These assert on prompt assembly only. No API key, no network, no model
call. See conftest.py for why that is a deliberate constraint.
"""
import pytest
from langchain_core.messages import AIMessage, HumanMessage

SOLO_WORLD = "desert-monasticism"
SOLO_REP = "papnoute"
SECOND_WORLD = "alexandria-catechetical"

SOLO_HEADING = "# This Conversation So Far"
MULTI_HEADING = "# The Public Transcript"

OPENING_HUMAN = "I grew up in a church that treated doubt as a sin."
OPENING_REP = "Doubt was the weather we worked in, not a fault in the one who felt it."
LATEST_HUMAN = "Is that different from what you said about naming it aloud?"


def _exchange(n):
    """n prior exchanges, then a final participant message."""
    msgs = []
    for i in range(n):
        human = OPENING_HUMAN if i == 0 else f"Participant question {i}."
        rep = OPENING_REP if i == 0 else f"Representative answer {i}."
        msgs.append(HumanMessage(content=human))
        msgs.append(AIMessage(content=rep, name=SOLO_REP))
    msgs.append(HumanMessage(content=LATEST_HUMAN))
    return msgs


def test_solo_turn_carries_conversation_history(prepared):
    """The fix. A solo Representative sees the conversation it is in."""
    ctx = prepared(_exchange(4), [SOLO_WORLD])
    dynamic = ctx["dynamic_prompt"]

    assert SOLO_HEADING in dynamic, "solo turn has no conversation record"
    assert OPENING_HUMAN in dynamic, "participant's own earlier words missing"
    assert OPENING_REP in dynamic, "Representative cannot see its own prior turn"


def test_history_is_not_in_the_cached_static_prompt(prepared):
    """Cost guard. The record changes every turn; if it ever lands in the
    cached static block it invalidates the prefix on every single turn.
    That failure is silent - the conversation still reads fine and the
    bill quietly multiplies - so it needs a test rather than a comment."""
    ctx = prepared(_exchange(4), [SOLO_WORLD])

    assert SOLO_HEADING not in ctx["static_prompt"]
    assert OPENING_REP not in ctx["static_prompt"]
    assert SOLO_HEADING in ctx["dynamic_prompt"]


def test_multi_world_framing_is_unchanged(prepared):
    """The solo branch is an elif; multi-world takes the first branch and
    must be untouched. A Table has other voices present and says so - the
    solo framing ('you are not meeting them for the first time') would be
    wrong there."""
    ctx = prepared(_exchange(4), [SOLO_WORLD, SECOND_WORLD])
    dynamic = ctx["dynamic_prompt"]

    assert MULTI_HEADING in dynamic, "multi-world transcript framing lost"
    assert SOLO_HEADING not in dynamic, "solo framing leaked into a Table"


def test_first_turn_adds_no_history_block(prepared):
    """Nothing has been said yet, so no scaffolding for an empty record."""
    ctx = prepared([HumanMessage(content=OPENING_HUMAN)], [SOLO_WORLD])

    assert SOLO_HEADING not in ctx["dynamic_prompt"]


def test_latest_message_still_reaches_the_continuation(prepared):
    """The record is additive. The participant's current message must
    still arrive the way it always did."""
    ctx = prepared(_exchange(4), [SOLO_WORLD])

    assert LATEST_HUMAN in ctx["continuation"]


@pytest.mark.parametrize("exchanges", [12, 20, 40])
def test_history_cost_is_flat_with_conversation_length(prepared, exchanges):
    """The 2+10 block-truncation window caps the record, so per-turn cost
    stays flat instead of rising with the conversation. Measured at ~534
    tokens for a real 12-exchange conversation; the ceiling here is
    deliberately loose so ordinary copy edits do not trip it."""
    from app.graph.nodes import TRANSCRIPT_RECENT_WINDOW, TRANSCRIPT_STABLE_PREFIX

    ctx = prepared(_exchange(exchanges), [SOLO_WORLD])
    block = ctx["dynamic_prompt"].split(SOLO_HEADING, 1)[1]
    rendered_lines = [ln for ln in block.split("\n\n") if ln.strip()]

    ceiling = TRANSCRIPT_STABLE_PREFIX + TRANSCRIPT_RECENT_WINDOW + 6
    assert len(rendered_lines) <= ceiling, (
        f"{exchanges} exchanges rendered {len(rendered_lines)} lines; the "
        f"window should cap this near {TRANSCRIPT_STABLE_PREFIX}+"
        f"{TRANSCRIPT_RECENT_WINDOW}. If this fails, per-turn cost has "
        f"started growing with conversation length."
    )


def test_long_conversations_mark_the_elided_middle(prepared):
    """KNOWN LIMITATION, asserted so it stays visible.

    The window keeps the opening turns and the recent ones and elides the
    middle. A participant on turn 30 referring to something from turn 5
    still gets a Representative that cannot see it. This test does not
    call that acceptable - it pins the current behaviour so that widening
    the window is a deliberate change with a failing test attached,
    rather than something that drifts."""
    ctx = prepared(_exchange(30), [SOLO_WORLD])
    block = ctx["dynamic_prompt"]

    assert "earlier turn(s) not shown" in block, (
        "elision marker missing - either the window changed or the "
        "participant is being shown an unbounded transcript"
    )
    assert OPENING_HUMAN in block, "stable prefix lost the opening framing"
