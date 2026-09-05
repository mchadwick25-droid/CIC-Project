"""The turn selector's code-enforced rules (Artifact-7 SS5): legal-move
computation, the schema enum carrying only legal moves, illegal-output
re-ask, deterministic fallback, and the degraded flag meaning what it says.
The model's judgment is faked throughout - what's under test is exactly the
part that must never depend on it."""
from types import SimpleNamespace

from engine.m4.turn_selector import (
    CLOSE,
    Selection,
    _resolve_engages,
    _selector_tool,
    eligible_worlds,
    fallback_world,
    round_facts,
    select_speaker,
)


class _FakeToolUse:
    def __init__(self, name, input_):
        self.type = "tool_use"
        self.name = name
        self.input = input_


_FAKE_USAGE = SimpleNamespace(input_tokens=10, output_tokens=5, cache_creation_input_tokens=0, cache_read_input_tokens=0)


class FakeSelectorClient:
    """Returns the scripted responses in order; records the legal-move enum
    each call carried so tests can assert what the model was even allowed
    to say."""

    def __init__(self, responses):
        self._responses = list(responses)
        self.seen_enums = []

    @property
    def messages(self):
        return self

    def create(self, *, model, max_tokens, system, tools, tool_choice, messages, timeout):
        self.seen_enums.append(list(tools[0]["input_schema"]["properties"]["next"]["enum"]))
        self.seen_contents = getattr(self, "seen_contents", [])
        self.seen_contents.append(messages[0]["content"])
        response = self._responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return SimpleNamespace(content=[_FakeToolUse("submit_turn_selection", response)], usage=_FAKE_USAGE)


def _select(client, *, world_keys=("alx", "desert", "pahc"), last_speaker=None, close_allowed=False, transcript_speakers=(), round_speakers=()):
    return select_speaker(
        client,
        "model-x",
        message="what is prayer?",
        transcript_text="(nothing yet)",
        seated_lines="- alx\n- desert\n- pahc",
        world_keys=list(world_keys),
        last_speaker=last_speaker,
        close_allowed=close_allowed,
        transcript_speakers=list(transcript_speakers),
        round_speakers=list(round_speakers),
    )


def test_round_facts_are_stated_not_inferred():
    # The R2-pos3 live finding: the selector claimed a voice "has not yet
    # responded" when it had spoken at position 1 of the round. The facts
    # are now computed in code and placed in the prompt.
    assert round_facts(["alx", "desert", "pahc"], []) == (
        "Spoken THIS round, in order: (no one - this is the round's opening turn). "
        "Not yet heard this round: alx, desert, pahc."
        " A round at this 3-seat table most often finishes well around turn 5 - a preference, never a "
        "rule: close as soon as the exchange is genuinely finished, and let it run longer only when a "
        "voice still has something real left to add."
    )
    assert round_facts(["alx", "desert"], ["alx", "desert", "alx"]) == (
        "Spoken THIS round, in order: alx (position 1); desert (position 2); alx (position 3). "
        "Not yet heard this round: (every voice has spoken this round)."
        " A round at this 2-seat table most often finishes well around turn 4 - a preference, never a "
        "rule: close as soon as the exchange is genuinely finished, and let it run longer only when a "
        "voice still has something real left to add."
    )


def test_round_facts_target_guidance_is_a_preference_not_a_rule():
    """Mark's ruling, 2026-09-05: the 4/5 "ultimate zone" is guidance in
    the selector's own reasoning, never a second code-enforced gate - the
    hard number is RoundConfig.cap_for (engine.m4.round), untouched here.
    A table size this project never seats (Artifact-7 SS1: 2-3 only) gets
    no target line at all rather than a guessed one."""
    two = round_facts(["alx", "desert"], [])
    three = round_facts(["alx", "desert", "pahc"], [])
    assert "around turn 4" in two and "a preference, never a rule" in two
    assert "around turn 5" in three and "a preference, never a rule" in three
    assert round_facts(["fix"], []) == (
        "Spoken THIS round, in order: (no one - this is the round's opening turn). "
        "Not yet heard this round: fix."
    )


def test_round_facts_reach_the_selector_prompt():
    client = FakeSelectorClient([{"next": "pahc", "reason": "unheard"}])
    _select(client, round_speakers=["alx", "desert"])
    content = client.seen_contents[0]
    assert "Round state (computed, trust it over your own reading):" in content
    assert "alx (position 1); desert (position 2)" in content
    assert "Not yet heard this round: pahc" in content


def test_no_immediate_self_repeat():
    assert eligible_worlds(["alx", "desert", "pahc"], "desert") == ["alx", "pahc"]
    assert eligible_worlds(["alx", "desert"], "alx") == ["desert"]
    assert eligible_worlds(["alx", "desert"], None) == ["alx", "desert"]


def test_fallback_prefers_never_spoken_then_least_recent():
    # pahc has never spoken - it wins over both that have.
    assert fallback_world(["alx", "desert", "pahc"], ["alx", "desert", "alx"]) == "pahc"
    # All have spoken: desert's last turn is furthest back.
    assert fallback_world(["alx", "desert"], ["desert", "alx", "alx"]) == "desert"
    # Deterministic tie-break: seating order among never-spoken.
    assert fallback_world(["alx", "desert"], []) == "alx"


def test_forced_move_skips_the_model():
    # Two seats, floor unmet, one eligible voice: there is no judgment to
    # exercise, so no call is made (any call would pop an empty script and
    # fail this test) and the reason is code-written - both live runs showed
    # the model confabulating a justification when asked anyway.
    client = FakeSelectorClient([])
    selection, outcomes = _select(client, world_keys=("alx", "desert"), last_speaker="alx")
    assert selection.world_key == "desert" and not selection.close and not selection.degraded
    assert "forced move" in selection.reason
    assert outcomes == []


def test_single_eligible_with_close_allowed_still_consults():
    # One eligible voice but closing is legal: speak-or-close is a genuine
    # choice, so the model is consulted.
    client = FakeSelectorClient([{"next": CLOSE, "reason": "answered"}])
    selection, outcomes = _select(client, world_keys=("alx", "desert"), last_speaker="alx", close_allowed=True)
    assert selection.close
    assert len(outcomes) == 1
    assert client.seen_enums == [["desert", CLOSE]]


def test_legal_selection_passes_through():
    client = FakeSelectorClient([{"next": "desert", "reason": "asked directly"}])
    selection, outcomes = _select(client)
    assert selection == Selection(world_key="desert", close=False, reason="asked directly", degraded=False)
    assert len(outcomes) == 1
    # The schema enum carried exactly the legal moves - close not offered
    # below the floor.
    assert client.seen_enums == [["alx", "desert", "pahc"]]


def test_close_allowed_and_taken():
    client = FakeSelectorClient([{"next": CLOSE, "reason": "genuinely answered"}])
    selection, _ = _select(client, close_allowed=True)
    assert selection.close and selection.world_key is None and not selection.degraded
    assert client.seen_enums == [["alx", "desert", "pahc", CLOSE]]


def test_self_repeat_excluded_from_enum():
    client = FakeSelectorClient([{"next": "alx", "reason": "follows up"}])
    _select(client, last_speaker="desert")
    assert client.seen_enums == [["alx", "pahc"]]


def test_illegal_output_reasked_without_close():
    # The model answers with the last speaker despite the enum (schema is a
    # guardrail, not a guarantee) - one re-ask, close off the menu.
    client = FakeSelectorClient([
        {"next": "desert", "reason": "again me"},
        {"next": "alx", "reason": "second thought"},
    ])
    selection, outcomes = _select(client, last_speaker="desert", close_allowed=True)
    assert selection == Selection(world_key="alx", close=False, reason="second thought", degraded=False)
    assert len(outcomes) == 2
    assert client.seen_enums == [["alx", "pahc", CLOSE], ["alx", "pahc"]]


def test_failed_call_falls_back_deterministically():
    from anthropic import APITimeoutError

    client = FakeSelectorClient([APITimeoutError(request=None)])
    selection, outcomes = _select(client, transcript_speakers=["alx"])
    assert selection.degraded
    assert not selection.close
    # desert and pahc never spoke; desert is first in seating order.
    assert selection.world_key == "desert"
    assert "fallback" in selection.reason
    assert outcomes[0].status == "timeout"


def test_illegal_twice_falls_back():
    client = FakeSelectorClient([
        {"next": "desert", "reason": "again"},
        {"next": "desert", "reason": "insisting"},
    ])
    selection, outcomes = _select(client, last_speaker="desert", transcript_speakers=["desert", "alx"])
    assert selection.degraded
    assert selection.world_key == "pahc"  # never spoken beats alx
    assert len(outcomes) == 2


# --- engages: a return turn's own scoped engagement target (2026-09-05,
# structural fix for a repeat "closes on a full-table synthesis" failure -
# see engine.api.table_wiring._table_engagement_directive's own docstring
# for the live case that drove it). A first-time speaker never carries
# one; a returning speaker always resolves to exactly one prior speaker,
# on every path - a real model choice, or deterministically when no model
# was asked (a forced move) or its answer can't be trusted (an omission,
# a self-reference, or a name outside the round, and the full fallback
# path alike).


def test_selector_tool_schema_carries_engages_only_once_someone_has_spoken():
    opening = _selector_tool(["alx", "desert", "pahc"], [])
    assert "engages" not in opening["input_schema"]["properties"]

    mid_round = _selector_tool(["alx", "desert", "pahc"], ["alx", "desert"])
    assert mid_round["input_schema"]["properties"]["engages"]["enum"] == ["alx", "desert"]


def test_resolve_engages_directly():
    # A first-time speaker: nothing to engage yet, whatever was requested.
    assert _resolve_engages("pahc", ["alx", "desert"], "alx") is None
    assert _resolve_engages("pahc", [], None) is None
    # A return with a real, distinct requested target: passed through.
    assert _resolve_engages("alx", ["alx", "desert", "pahc"], "desert") == "desert"
    # A return with no requested target, a self-reference, or a stranger:
    # deterministically the most recent OTHER speaker in the round.
    assert _resolve_engages("alx", ["alx", "desert", "pahc"], None) == "pahc"
    assert _resolve_engages("alx", ["alx", "desert", "pahc"], "alx") == "pahc"
    assert _resolve_engages("alx", ["alx", "desert", "pahc"], "syr") == "pahc"


def test_forced_move_return_resolves_engages_to_the_last_speaker():
    """A forced move (2026-08-28) never asks the model, but the return it
    forces still needs a scoped engagement target - at a 2-seat table the
    only other voice already IS the one it just heard from."""
    client = FakeSelectorClient([])
    selection, _ = _select(client, world_keys=("alx", "desert"), last_speaker="desert", round_speakers=["alx", "desert"])
    assert selection.world_key == "alx" and not selection.degraded
    assert selection.engages == "desert"


def test_selector_supplied_engages_passes_through():
    client = FakeSelectorClient([{"next": "alx", "reason": "circling back", "engages": "desert"}])
    selection, _ = _select(
        client, world_keys=("alx", "desert", "pahc"), last_speaker="pahc", close_allowed=True,
        round_speakers=["alx", "desert", "pahc"],
    )
    assert selection.world_key == "alx" and selection.engages == "desert"


def test_selector_omitted_engages_falls_back_to_most_recent_other_speaker():
    client = FakeSelectorClient([{"next": "alx", "reason": "circling back"}])  # no "engages" key at all
    selection, _ = _select(
        client, world_keys=("alx", "desert", "pahc"), last_speaker="pahc", close_allowed=True,
        round_speakers=["alx", "desert", "pahc"],
    )
    assert selection.world_key == "alx" and selection.engages == "pahc"  # round_speakers[-1]


def test_selector_self_referential_engages_falls_back():
    client = FakeSelectorClient([{"next": "alx", "reason": "circling back", "engages": "alx"}])
    selection, _ = _select(
        client, world_keys=("alx", "desert", "pahc"), last_speaker="pahc", close_allowed=True,
        round_speakers=["alx", "desert", "pahc"],
    )
    assert selection.world_key == "alx" and selection.engages == "pahc"


def test_first_pass_pick_never_carries_an_engages_value():
    # The model names a target anyway (a schema slip, not enforced against
    # a first-timer) - discarded, since there is nothing to engage yet.
    client = FakeSelectorClient([{"next": "pahc", "reason": "unheard", "engages": "alx"}])
    selection, _ = _select(client, round_speakers=["alx", "desert"])
    assert selection.world_key == "pahc" and selection.engages is None


def test_failed_call_fallback_resolves_engages_when_the_fallback_is_a_return():
    from anthropic import APITimeoutError

    client = FakeSelectorClient([APITimeoutError(request=None)])
    selection, outcomes = _select(
        client, world_keys=("alx", "desert", "pahc"), last_speaker="pahc",
        transcript_speakers=["alx", "desert", "pahc"], round_speakers=["alx", "desert", "pahc"],
    )
    assert selection.degraded
    assert selection.world_key == "alx"  # furthest-back eligible voice, per fallback_world
    assert selection.engages == "pahc"  # round_speakers[-1]
