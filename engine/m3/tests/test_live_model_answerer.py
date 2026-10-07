"""Hermetic tests for engine.m3.generation.LiveModelAnswerer - no live
model call, a fake streaming client (same fake-client shape as
engine/m4/tests/test_turn.py's own FakeBedrockClient, stream-only here
since LiveModelAnswerer makes no tool-use calls at all - a sealed probe
already IS the ask, there is no reader/safety gate to classify or route).
"""
from types import SimpleNamespace

from engine.m3.generation import LiveModelAnswerer
from engine.m4.world_loader import LoadedWorld
from engine.shape import shape_text

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
    assert [b["text"] for b in system] == [shape_text(), world.prompt_text]  # shape then world, untouched per turn
    assert "## Ground for this turn" in messages[0]["content"]
    assert "[[fix.witness.who-is-jesus]]" in messages[0]["content"]
    assert ASK_TEXT in messages[0]["content"]


def test_an_ungrounded_answer_is_graded_as_written_no_appended_floor_line():
    """Admission grades exactly what the voice wrote: an ungrounded answer
    stands as itself, with no citations - so a weak answer is seen as
    weak, not papered over."""
    coverage = {"C-I": {**_EMPTY_CELL, "honest_limit": ["fix.limit.who-is-jesus"]}}
    world = _world(coverage)
    client = FakeClient(stream_chunks=["We enjoy talking about many things."])
    answerer = LiveModelAnswerer(world=world, canon_questions=CANON_QUESTIONS, client=client, model_id="m")

    result = answerer.answer("C-I", ASK_TEXT)

    assert result.text == "We enjoy talking about many things."
    assert "We cannot say more than our own record allows." not in result.text
    assert result.citations == []
    assert result.source_record_id is None
    assert result.source_record_type is None


def test_answer_with_no_coverage_at_all_still_returns_a_result_not_an_exception():
    # Unlike FixtureRecordAnswerer.answer (which raises NoCoverageError
    # when a cell has neither a demonstration, substantive record, nor
    # honest_limit), a live answerer always gets SOME text back from the
    # model - and returns it as written (production parity), rather than
    # raising a coverage exception or appending any floor line.
    world = _world({})
    client = FakeClient(stream_chunks=["We enjoy talking about many things."])
    answerer = LiveModelAnswerer(world=world, canon_questions=CANON_QUESTIONS, client=client, model_id="m")

    result = answerer.answer("C-I", ASK_TEXT)

    assert result.text == "We enjoy talking about many things."


def test_admission_text_shape_is_productions_own_apply_net_verbatim():
    """The parity guarantee itself: a raw answer carrying one grounded
    sentence and one sentence whose tag resolves to nothing must come back
    from the answerer EXACTLY as engine.m4.turn.apply_net shapes it - the
    fabricating sentence retained in the text (checks gate decoration,
    never the text) with its tag stripped, and excluded from citations."""
    from engine.m4.turn import apply_net

    raw = (
        "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]. "
        "Our founder wrote twelve books about it [[fix.invented.record]]."
    )
    coverage = {"C-I": {**_EMPTY_CELL, "doctrinal_witness": ["fix.witness.who-is-jesus"]}}
    world = _world(coverage)
    client = FakeClient(stream_chunks=[raw])
    answerer = LiveModelAnswerer(world=world, canon_questions=CANON_QUESTIONS, client=client, model_id="m")

    result = answerer.answer("C-I", ASK_TEXT)

    from engine.m4 import evidence as m4_evidence

    repository_records = m4_evidence.repository_records_by_id(world.repository)
    expected_text, expected_entries, _ = apply_net(
        raw, repository_records=repository_records, thin_topics=m4_evidence.thin_topics_for(repository_records)
    )

    assert result.text == expected_text
    assert "twelve books" in result.text  # retained, tag stripped - never deleted
    assert "[[" not in result.text
    assert result.citations == sorted({rid for e in expected_entries for rid in e["record_ids"]})
    assert "fix.invented.record" not in result.citations
