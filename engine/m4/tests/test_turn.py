"""Hermetic (no live model call) tests for engine.m4.turn.run_turn's
dispatch: does the right routing action reach the right generation path,
and - the one that matters most - does a GENUINELY empty stream (a fake
client returning zero text_stream chunks, not the force_empty_stream test
hook) still produce a crisis-resources append. force_empty_stream exists
for evidence scripts where forcing it is cheaper than trying to provoke a
real model into silence; this file proves the real code path handles a
real empty stream identically, via the fake client's stream_chunks=().
"""
from types import SimpleNamespace

import pytest

from engine.m4.turn import UnhandledRoutingAction, run_turn
from engine.m4.world_loader import LoadedWorld


class _FakeToolUse:
    def __init__(self, name, input_):
        self.type = "tool_use"
        self.name = name
        self.input = input_


_FAKE_USAGE = SimpleNamespace(input_tokens=100, output_tokens=50, cache_creation_input_tokens=0, cache_read_input_tokens=0)


class _FakeStreamCtx:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: SimpleNamespace(usage=_FAKE_USAGE))

    def __exit__(self, *exc):
        return False


class _FakeMessages:
    def __init__(self, *, safety_response, reader_response, citations_response, stream_chunks):
        self._responses = {
            "submit_safety_classification": safety_response,
            "submit_reader_output": reader_response,
            "submit_citations": citations_response,
        }
        self._stream_chunks = stream_chunks

    def create(self, *, model, max_tokens, tools, tool_choice, messages, system=None, timeout=None):
        name = tool_choice["name"]
        return SimpleNamespace(content=[_FakeToolUse(name, self._responses[name])], usage=_FAKE_USAGE)

    def stream(self, *, model, max_tokens, system=None, messages):
        return _FakeStreamCtx(self._stream_chunks)


class FakeBedrockClient:
    def __init__(self, *, safety_response, reader_response, citations_response=None, stream_chunks=()):
        self.messages = _FakeMessages(
            safety_response=safety_response,
            reader_response=reader_response,
            citations_response=citations_response or {"drawn_on": [], "consulted": []},
            stream_chunks=stream_chunks,
        )


def _reader(**overrides):
    base = {"asks": [{"order": 1, "text": "who was Jesus"}], "register": "informational", "clarity": "clear", "ambiguity_options": [], "out_of_scope": {"class": "none"}, "modern_terms": []}
    base.update(overrides)
    return base


def _safety(signal="NO_SIGNAL"):
    return {"signal": signal, "acute_level": "none", "risk_subject": "not_applicable", "dynamic_tags": [], "confidence": "high"}


def _world():
    return LoadedWorld(
        world_key="fix",
        manifest_hash="sha256:test",
        prompt_text="## Identity\nVera, Witness.",
        capsule_text="capsule",
        repository={"records": [{"id": "fix.witness.who-is-jesus", "text": "We did not claim to have seen him ourselves."}]},
        quotes={"quotes": [{"id": "fix.quote.private-teaching", "license": "do-not-voice", "text": "not for the voice to speak"}]},
        figures={},
        coverage={},
        frame={},
    )


def test_acute_distress_with_real_stream_text_appends_resources_not_empty():
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS"), reader_response=_reader(), stream_chunks=["I hear you. ", "That sounds heavy."])
    result = run_turn(
        session_id="test-session",
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="I don't want to be here anymore.", pressed={}, anachronistic_term_ids=set(),
    )
    assert result.routing_action == "safety_turn"
    assert result.facilitator_events[0]["resources_appended"] is True
    assert result.facilitator_events[0]["empty_stream"] is False
    assert result.voice_event is not None
    assert result.voice_event["text"] == "I hear you. That sounds heavy."


def test_acute_distress_with_genuinely_empty_stream_still_appends_resources():
    """The real code path, not the force_empty_stream hook: the fake
    client's stream yields zero chunks, exactly like a real model call that
    completes but produces no tokens."""
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS"), reader_response=_reader(), stream_chunks=[])
    result = run_turn(
        session_id="test-session",
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="I don't want to be here anymore.", pressed={}, anachronistic_term_ids=set(),
    )
    assert result.facilitator_events[0]["resources_appended"] is True
    assert result.facilitator_events[0]["empty_stream"] is True
    assert result.voice_event is None  # nothing worth showing as a voice turn - the append still happened


def test_force_empty_stream_hook_matches_the_real_empty_case():
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS"), reader_response=_reader(), stream_chunks=["would never be seen"])
    result = run_turn(
        session_id="test-session",
        voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set(), force_empty_stream=True,
    )
    assert result.facilitator_events[0]["resources_appended"] is True
    assert result.facilitator_events[0]["empty_stream"] is True
    assert result.voice_event is None


def test_harmful_dynamic_signal_raises_unhandled_not_silently_dropped():
    client = FakeBedrockClient(safety_response=_safety("HARMFUL_DYNAMIC_SIGNAL"), reader_response=_reader())
    with pytest.raises(UnhandledRoutingAction):
        run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set())


def test_ambiguous_low_confidence_check_in_turn_raises_unhandled():
    client = FakeBedrockClient(safety_response=_safety("AMBIGUOUS_LOW_CONFIDENCE"), reader_response=_reader())
    with pytest.raises(UnhandledRoutingAction):
        run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="msg", pressed={}, anachronistic_term_ids=set())


def test_ordinary_turn_calls_voice_generation_and_citations():
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(),
        citations_response={"drawn_on": ["fix.witness.who-is-jesus"], "consulted": []},
        stream_chunks=["We did not claim to have seen him ourselves."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="who was Jesus", pressed={}, anachronistic_term_ids=set())
    assert result.routing_action == "voice_with_directive"
    assert result.voice_event["text"] == "We did not claim to have seen him ourselves."
    assert result.voice_event["citations"] == ["fix.witness.who-is-jesus"]  # grounded: excerpt actually present in the text
    assert result.voice_event["do_not_voice_violation"] is None


def test_every_real_call_this_turn_makes_is_attributed_to_the_session():
    """M8's stage-6 gate item, exercised end to end: an ordinary turn makes
    four real calls (safety, reader, voice generation, citations) - every
    one must land in usage_records tagged with the caller's session_id,
    zero unattributed."""
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"),
        reader_response=_reader(),
        citations_response={"drawn_on": ["fix.witness.who-is-jesus"], "consulted": []},
        stream_chunks=["We did not claim to have seen him ourselves."],
    )
    result = run_turn(session_id="participant-session-42", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="who was Jesus", pressed={}, anachronistic_term_ids=set())
    assert len(result.usage_records) == 4
    assert {r.call_kind for r in result.usage_records} == {"safety_call", "reader_call", "voice_generation", "citations_call"}
    assert all(r.session_id == "participant-session-42" for r in result.usage_records)
    assert all(r.is_attributed for r in result.usage_records)


def test_crisis_turn_usage_records_are_also_attributed():
    client = FakeBedrockClient(safety_response=_safety("ACUTE_DISTRESS"), reader_response=_reader(), stream_chunks=["I hear you."])
    result = run_turn(session_id="crisis-session-1", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="I don't want to be here anymore.", pressed={}, anachronistic_term_ids=set())
    assert len(result.usage_records) == 3  # safety, reader, voice_generation_crisis - no citations call on the crisis path
    assert all(r.session_id == "crisis-session-1" for r in result.usage_records)


def test_do_not_voice_quote_verbatim_is_flagged_on_a_real_turn():
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=["I should not have said this: not for the voice to speak."],
    )
    result = run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="tell me the secret", pressed={}, anachronistic_term_ids=set())
    assert result.voice_event["do_not_voice_violation"] == "fix.quote.private-teaching"


def test_system_nature_out_of_scope_raises_unhandled():
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(out_of_scope={"class": "system_nature"}))
    with pytest.raises(UnhandledRoutingAction):
        run_turn(session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m", world=_world(), participant_message="are you an AI?", pressed={}, anachronistic_term_ids=set())
