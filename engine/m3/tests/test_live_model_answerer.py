"""Hermetic tests for engine.m3.generation.LiveModelAnswerer - no model call.
A fake client answers the two gate calls with fixed tool output and streams a
fixed draft, so what is under test is the path: that a sealed probe goes
through the gate, the directive and the settled reply exactly as a
conversation's first message does.
"""
import copy
from pathlib import Path
from types import SimpleNamespace

import pytest

from engine.m1.registry import load_registry
from engine.m3.generation import AnswerUnavailable, LiveModelAnswerer, LivePathSettings, production_settings
from engine.m4.generation import _TRANSPORT_ERRORS
from engine.m4.turn_prep import CONCISION_DIRECTIVE
from engine.m4.world_loader import LoadedWorld
from engine.provider.guard import LiveTestCapReached

_USAGE = SimpleNamespace(input_tokens=100, output_tokens=50, cache_creation_input_tokens=0, cache_read_input_tokens=0)
SETTINGS = LivePathSettings(
    voice_model_id="voice-model", safety_model_id="safety-model",
    r27_enforce=False, self_revision_enabled=False, citation_attach_enabled=False,
)


def _tool_use(name, value):
    return SimpleNamespace(type="tool_use", name=name, input=copy.deepcopy(value))


def safety(signal="NO_SIGNAL", **overrides):
    base = {"signal": signal, "acute_level": "none", "risk_subject": "not_applicable", "check_in_reason": "not_applicable",
            "dynamic_tags": [], "confidence": "high"}
    return {**base, **overrides}


def reader(**overrides):
    base = {"asks": [{"order": 1, "text": "who was Jesus"}], "register": "informational", "clarity": "clear",
            "ambiguity_options": [], "out_of_scope": {"class": "none"}, "modern_terms": []}
    return {**base, **overrides}


class _StreamContext:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        text = "".join(self._chunks)
        message = SimpleNamespace(usage=_USAGE, content=[SimpleNamespace(type="text", text=text)], stop_reason="end_turn")
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: message)

    def __exit__(self, *exc):
        return False


class FakeClient:
    def __init__(self, *, safety_value=None, reader_value=None, draft=(), drops=0, cap_after=None):
        self._responses = {
            "submit_safety_classification": safety_value or safety(),
            "submit_reader_output": reader_value or reader(),
        }
        self._draft = draft
        self._drops = drops
        self._cap_after = cap_after
        self.stream_calls = []
        self.messages = self

    def create(self, *, model, max_tokens, tools, tool_choice, messages, system=None, timeout=None):
        name = tool_choice["name"]
        return SimpleNamespace(content=[_tool_use(name, self._responses[name])], usage=_USAGE)

    def stream(self, *, model, max_tokens, system=None, messages, timeout=None):
        if self._cap_after is not None and len(self.stream_calls) >= self._cap_after:
            raise LiveTestCapReached("cap")
        self.stream_calls.append({"model": model, "system": system, "messages": messages})
        if self._drops:
            self._drops -= 1
            raise _TRANSPORT_ERRORS[0]("peer closed connection without sending complete message body")
        return _StreamContext(self._draft)


WITNESS = {"id": "fix.witness.who-is-jesus", "record_type": "doctrinal_witness", "text": "We did not claim to have seen him ourselves."}
LIMIT = {"id": "fix.limit.who-is-jesus", "record_type": "honest_limit", "statement": "We cannot say more than our own record allows."}
ASK_TEXT = "Who was Jesus, to you and your people?"
_EMPTY_CELL = {"doctrinal_witness": [], "terms": [], "stories": [], "quotes": [], "honest_limit": [], "gravities": [], "forces": [], "contested_claims": []}


def _world(coverage=None):
    return LoadedWorld(
        world_key="fix",
        manifest_hash="sha256:test",
        prompt_text="## Identity\nVera, Witness.",
        capsule_text="capsule",
        repository={"records": [WITNESS, LIMIT]},
        quotes={"quotes": []},
        figures={},
        coverage=coverage if coverage is not None else {"C-I": {**_EMPTY_CELL, "doctrinal_witness": ["fix.witness.who-is-jesus"]}},
        frame={"time_window": {"start": 30, "end": 400}, "representative": {"name": "Vera"}},
    )


def _answerer(client, world=None, settings=SETTINGS):
    return LiveModelAnswerer(world=world or _world(), registry=load_registry(), client=client, settings=settings)


def test_a_probe_runs_the_gate_the_directive_and_the_voice_like_a_first_message():
    client = FakeClient(draft=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."])

    result = _answerer(client).answer("C-I", ASK_TEXT)

    assert result.text == "We did not claim to have seen him ourselves."
    assert result.citations == ["fix.witness.who-is-jesus"]
    assert result.source_record_type == "doctrinal_witness"
    system = client.stream_calls[0]["system"]
    assert CONCISION_DIRECTIVE in system[-1]["text"]
    assert "who was Jesus" in system[-1]["text"]
    assert "## Ground for this turn" in client.stream_calls[0]["messages"][-1]["content"]
    turn = result.live_turn
    assert turn.routing_action == "voice_with_directive"
    assert turn.gate["directive"]["asks"] == [{"order": 1, "text": "who was Jesus"}]
    assert [call["raw_text"] for call in turn.voice_calls] == ["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."]
    assert {record["call_kind"] for record in turn.usage} == {"safety_call", "reader_call", "voice_generation"}
    assert turn.sends == 1


def test_a_probe_the_gate_routes_to_the_facilitator_is_answered_by_the_facilitator():
    client = FakeClient(safety_value=safety("ACUTE_DISTRESS", acute_level="a1"), draft=["never used"])

    result = _answerer(client).answer("C-I", "I don't want to be here anymore.")

    assert result.live_turn.routing_action == "safety_turn"
    assert result.live_turn.voice_event is None
    assert result.text and "not Vera" in result.text
    assert result.citations == []
    assert client.stream_calls == []


def test_an_ungrounded_draft_is_settled_as_a_conversation_settles_it():
    client = FakeClient(draft=["We enjoy talking about many things [[fix.witness.who-is-jesus]]."])

    result = _answerer(client).answer("C-I", ASK_TEXT)

    assert result.text == "We did not claim to have seen him ourselves."
    assert result.live_turn.voice_event["answer_record_fallback"] is not None


def test_a_send_that_fails_is_sent_again_and_a_second_failure_is_unanswered():
    draft = ["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."]
    recovered = FakeClient(draft=draft, drops=1)
    result = _answerer(recovered).answer("C-I", ASK_TEXT)
    assert result.live_turn.sends == 2
    assert result.citations == ["fix.witness.who-is-jesus"]
    assert len(result.live_turn.voice_calls) == 1

    with pytest.raises(AnswerUnavailable):
        _answerer(FakeClient(draft=draft, drops=2)).answer("C-I", ASK_TEXT)


def test_the_live_test_cap_is_never_swallowed_as_a_failed_send():
    with pytest.raises(LiveTestCapReached):
        _answerer(FakeClient(draft=["x"], cap_after=0)).answer("C-I", ASK_TEXT)


def test_production_settings_are_the_render_service_pins():
    settings = production_settings()

    assert settings["voice_model_pattern"] == "us.anthropic.claude-sonnet-4-5-20250929-v1:0"
    assert settings["safety_model_pattern"] == "us.anthropic.claude-haiku-4-5-20251001-v1:0"
    assert settings["self_revision_enabled"] is False
    assert settings["r27_enforce"] is False
    assert settings["citation_attach_enabled"] is False


def test_production_settings_leave_unset_flags_at_the_engines_own_defaults(tmp_path):
    path = Path(tmp_path) / "render.yaml"
    path.write_text(
        "services:\n  - name: cic-engine\n    envVars:\n"
        "      - key: CIC_API_VOICE_MODEL_PATTERN\n        value: v\n"
        "      - key: CIC_API_SAFETY_MODEL_PATTERN\n        value: s\n"
    )

    settings = production_settings(path)

    assert settings["self_revision_enabled"] is True
    assert settings["r27_enforce"] is False
    assert settings["citation_attach_enabled"] is False


def _stub_run_turn(monkeypatch, outcome):
    from engine.m3 import generation

    calls = []

    def run(**kwargs):
        calls.append(kwargs)
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    monkeypatch.setattr(generation, "run_turn", run)
    return calls


def _turn_result(action, reason="r"):
    from engine.m4.turn import TurnResult

    return TurnResult(routing_action=action, routing_reason=reason, facilitator_events=[{"kind": "safety", "text": "fixed line"}])


def test_a_failed_gate_is_a_failed_send_not_an_answer(monkeypatch):
    calls = _stub_run_turn(monkeypatch, _turn_result("safety_unread_turn", "safety call failed"))

    with pytest.raises(AnswerUnavailable, match="gate call failed"):
        _answerer(FakeClient()).answer("C-I", ASK_TEXT)

    assert len(calls) == 2


def test_a_guard_refusal_or_a_routing_fault_stops_the_run(monkeypatch):
    from engine.m4.turn import UnhandledRoutingAction
    from engine.provider.guard import LiveTestGuardError

    for error in (LiveTestGuardError("no approved price"), UnhandledRoutingAction("eighth route")):
        calls = _stub_run_turn(monkeypatch, error)
        with pytest.raises(type(error)):
            _answerer(FakeClient()).answer("C-I", ASK_TEXT)
        assert len(calls) == 1


def test_a_probe_with_no_voice_reply_is_graded_as_not_passed():
    from engine.m3 import harness

    answerer = _answerer(FakeClient(safety_value=safety("ACUTE_DISTRESS", acute_level="a1")))

    result = harness.run_battery("fix", {}, answerer=answerer, limit=1)[0]

    assert result.passed is False
    assert result.error == "no voice reply: routed to safety_turn"


def test_a_voice_the_uncited_claims_rule_sets_aside_is_answered_by_the_facilitators_turn_as_in_production():
    from engine.m4.facilitator_turns import voice_rejected_turn

    settings = LivePathSettings(
        voice_model_id="voice-model", safety_model_id="safety-model",
        r27_enforce=True, self_revision_enabled=False, citation_attach_enabled=False,
    )
    client = FakeClient(draft=["The sea was rough that night and the bishop was afraid of the crossing."])

    result = _answerer(client, settings=settings).answer("C-I", ASK_TEXT)

    assert result.live_turn.voice_event["r27_enforcement_exhausted"] is True
    assert result.text == voice_rejected_turn("Vera")["text"]
    assert result.citations == []
    assert result.citation_entries == []
