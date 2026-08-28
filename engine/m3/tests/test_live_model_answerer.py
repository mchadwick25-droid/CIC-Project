"""Hermetic tests for engine.m3.generation.LiveModelAnswerer - no live
model call, a fake streaming client (same fake-client shape as
engine/m4/tests/test_turn.py's own FakeBedrockClient, stream-only here
since LiveModelAnswerer makes no tool-use calls at all - a sealed probe
already IS the ask, there is no reader/safety gate to classify or route).
"""
from types import SimpleNamespace

from engine.m3.generation import LiveModelAnswerer
from engine.m4.world_loader import LoadedWorld

_FAKE_USAGE = SimpleNamespace(input_tokens=100, output_tokens=50, cache_creation_input_tokens=0, cache_read_input_tokens=0)


class _FakeStreamCtx:
    def __init__(self, chunks):
        self._chunks = chunks

    def __enter__(self):
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: SimpleNamespace(usage=_FAKE_USAGE))

    def __exit__(self, *exc):
        return False


class _FakeMessages:
    def __init__(self, stream_chunks):
        self._stream_chunks = stream_chunks
        self.captured_stream_calls = []  # [(system, messages), ...]

    def stream(self, *, model, max_tokens, system=None, messages, timeout=None):
        self.captured_stream_calls.append((system, messages))
        return _FakeStreamCtx(self._stream_chunks)


class FakeClient:
    def __init__(self, stream_chunks=()):
        self.messages = _FakeMessages(stream_chunks)


ASK_TEXT = "Who was Jesus, to you and your people? What did your community actually know about him?"
CANON_QUESTIONS = {
    "fleet.canon.q1": {"id": "fleet.canon.q1", "record_type": "canon_question", "cell": "C-I", "text": ASK_TEXT},
}
WITNESS = {"id": "fix.witness.who-is-jesus", "record_type": "doctrinal_witness", "text": "We did not claim to have seen him ourselves."}
LIMIT = {"id": "fix.limit.who-is-jesus", "record_type": "honest_limit", "statement": "We cannot say more than our own record allows."}
_EMPTY_CELL = {"doctrinal_witness": [], "terms": [], "stories": [], "quotes": [], "honest_limit": [], "gravities": [], "forces": [], "contested_claims": []}


def _world(coverage):
    return LoadedWorld(
        world_key="fix",
        manifest_hash="sha256:test",
        prompt_text="## Identity\nVera, Witness.",
        capsule_text="capsule",
        repository={"records": [WITNESS, LIMIT]},
        quotes={"quotes": []},
        figures={},
        coverage=coverage,
        frame={},
    )


def test_answer_assembles_evidence_and_returns_grounded_citations():
    coverage = {"C-I": {**_EMPTY_CELL, "doctrinal_witness": ["fix.witness.who-is-jesus"]}}
    world = _world(coverage)
    client = FakeClient(stream_chunks=["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."])
    answerer = LiveModelAnswerer(world=world, canon_questions=CANON_QUESTIONS, client=client, model_id="m")

    result = answerer.answer("C-I", ASK_TEXT)

    assert result.text == "We did not claim to have seen him ourselves."
    assert result.citations == ["fix.witness.who-is-jesus"]
    assert result.source_record_id == "fix.witness.who-is-jesus"
    assert result.source_record_type == "doctrinal_witness"

    system, messages = client.messages.captured_stream_calls[0]
    assert system[0]["text"] == world.prompt_text  # the compiled prompt stays the cached system prefix, untouched per turn
    assert "## Ground for this turn" in messages[0]["content"]
    assert "[[fix.witness.who-is-jesus]]" in messages[0]["content"]
    assert ASK_TEXT in messages[0]["content"]


def test_answer_degrades_to_the_matched_cells_honest_limit_when_nothing_grounds():
    coverage = {"C-I": {**_EMPTY_CELL, "honest_limit": ["fix.limit.who-is-jesus"]}}
    world = _world(coverage)
    client = FakeClient(stream_chunks=["We enjoy talking about many things."])
    answerer = LiveModelAnswerer(world=world, canon_questions=CANON_QUESTIONS, client=client, model_id="m")

    result = answerer.answer("C-I", ASK_TEXT)

    assert "We cannot say more than our own record allows." in result.text
    assert result.citations == []
    assert result.source_record_id is None
    assert result.source_record_type is None


def test_answer_with_no_coverage_at_all_still_returns_a_result_not_an_exception():
    # Unlike FixtureRecordAnswerer.answer (which raises NoCoverageError
    # when a cell has neither a demonstration, substantive record, nor
    # honest_limit), a live answerer always gets SOME text back from the
    # model - it degrades to the fleet floor line rather than a coverage
    # exception, since a real generation call always produces something.
    world = _world({})
    client = FakeClient(stream_chunks=["We enjoy talking about many things."])
    answerer = LiveModelAnswerer(world=world, canon_questions=CANON_QUESTIONS, client=client, model_id="m")

    result = answerer.answer("C-I", ASK_TEXT)

    from engine.m4.evidence import FLEET_FLOOR_LINE

    assert FLEET_FLOOR_LINE in result.text
