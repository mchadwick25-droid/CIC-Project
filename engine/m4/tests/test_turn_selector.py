"""The turn selector's code-enforced rules (Artifact-7 SS5): legal-move
computation, the schema enum carrying only legal moves, illegal-output
re-ask, deterministic fallback, and the degraded flag meaning what it says.
The model's judgment is faked throughout - what's under test is exactly the
part that must never depend on it."""
from types import SimpleNamespace

from engine.m4.turn_selector import (
    CLOSE,
    Selection,
    eligible_worlds,
    fallback_world,
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
        response = self._responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return SimpleNamespace(content=[_FakeToolUse("submit_turn_selection", response)], usage=_FAKE_USAGE)


def _select(client, *, world_keys=("alx", "desert", "pahc"), last_speaker=None, close_allowed=False, transcript_speakers=()):
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
    )


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
