"""Decision 59, check 3: a reply that reproduces a demonstration record is a
recitation. Hermetic: synthetic records, a fake client, no model call."""
from engine.m4.recitation import DIRECTIVE_LINE, HOLD_WORDS, RECITATION_WORDS, DemonstrationIndex, reply_words
from engine.m4.sentence_stream import SentenceStream
from engine.m4.tests.test_turn import FakeBedrockClient, _reader, _safety, _world
from engine.m4.turn import run_voice_turn_for_world
from engine.m4.world_loader import LoadedWorld

DEMO_WORDS = (
    "we kept a quiet table by the river road and every evening the old ones taught the young ones "
    "to share bread before anyone spoke of what the day had cost them and then we sang"
).split()
DEMO_TEXT = " ".join(DEMO_WORDS).capitalize() + "."
DEMO = {
    "id": "fix.demo.table", "record_type": "demonstration",
    "exchange": [
        {"speaker": "participant", "text": "What was your table like?"},
        {"speaker": "representative", "text": DEMO_TEXT},
    ],
}
WITNESS = {"id": "fix.witness.who-is-jesus", "record_type": "doctrinal_witness", "text": "We did not claim to have seen him ourselves."}
RECORDS = {r["id"]: r for r in (DEMO, WITNESS)}


def _run(prefix_words, run_words):
    return " ".join(prefix_words + run_words)


def test_a_run_of_twenty_demonstration_words_is_a_recitation():
    index = DemonstrationIndex(RECORDS)
    assert len(DEMO_WORDS) > RECITATION_WORDS
    assert index.is_recited("Plainly put, " + " ".join(DEMO_WORDS[:RECITATION_WORDS]) + " and nothing more.")


def test_nineteen_matching_words_are_not_a_recitation():
    index = DemonstrationIndex(RECORDS)
    assert not index.is_recited(" ".join(DEMO_WORDS[: RECITATION_WORDS - 1]) + " in another place entirely.")


def test_tags_and_marks_do_not_hide_a_recitation():
    index = DemonstrationIndex(RECORDS)
    tagged = " ".join(DEMO_WORDS[:10]) + " [[fix.witness.who-is-jesus]], " + '"' + " ".join(DEMO_WORDS[10:22]) + '".'
    assert index.is_recited(tagged)


def test_a_run_a_record_also_carries_is_the_record_speaking_not_a_recitation():
    quoted = {"id": "fix.quote.table", "record_type": "quote", "text": " ".join(DEMO_WORDS[5:30]), "modern_rendering": " ".join(DEMO_WORDS[5:30])}
    index = DemonstrationIndex({**RECORDS, quoted["id"]: quoted})
    assert not index.is_recited(" ".join(DEMO_WORDS[5:30]))
    assert index.is_recited(" ".join(DEMO_WORDS[:RECITATION_WORDS]))


def test_a_world_with_no_demonstration_never_recites():
    assert not DemonstrationIndex({"fix.witness.who-is-jesus": WITNESS}).is_recited(DEMO_TEXT)


def test_hold_start_marks_a_run_that_may_still_grow():
    index = DemonstrationIndex(RECORDS)
    words = ["so", "the", "old", "story", "goes"] + DEMO_WORDS[: HOLD_WORDS + 2]
    assert index.hold_start(words) == 5
    assert index.hold_start(["nothing", "like", "it", "at", "all"] * 4) is None
    assert index.hold_start(DEMO_WORDS[: HOLD_WORDS - 1]) is None


def test_a_streamed_recitation_is_held_back_from_its_first_sentence():
    stream = SentenceStream(repository_records=RECORDS, world_key="fix")
    raw = DEMO_TEXT + " That is how it was. And it was good."
    events = [e for i in range(0, len(raw), 6) for e in stream.feed(raw[i : i + 6])]
    assert events == []
    assert stream.released == 0


def test_an_ordinary_reply_streams_when_demonstrations_exist():
    stream = SentenceStream(repository_records=RECORDS, world_key="fix")
    raw = (
        "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]. "
        "That is the whole of it, and we hold to it still, as our elders did before us. And more follows."
    )
    events = [e for i in range(0, len(raw), 6) for e in stream.feed(raw[i : i + 6])]
    assert [e["text"] for e in events] == [
        "We did not claim to have seen him ourselves.",
        "That is the whole of it, and we hold to it still, as our elders did before us.",
    ]


def test_nothing_streams_until_the_reply_could_hold_a_recitation():
    stream = SentenceStream(repository_records=RECORDS, world_key="fix")
    raw = "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]. That is all. And more follows."
    assert [e for i in range(0, len(raw), 6) for e in stream.feed(raw[i : i + 6])] == []


def test_a_world_without_demonstrations_streams_at_once():
    stream = SentenceStream(repository_records={"fix.witness.who-is-jesus": WITNESS}, world_key="fix")
    raw = "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]. That is all. And more follows."
    assert len([e for i in range(0, len(raw), 6) for e in stream.feed(raw[i : i + 6])]) == 2


def _recitation_world() -> LoadedWorld:
    world = _world()
    return LoadedWorld(**{**world.__dict__, "repository": {"records": [*world.repository["records"], DEMO]}})


def _turn(scripts, **kwargs):
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_scripts=scripts)
    event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_recitation_world(), participant_message="who was Jesus",
        directive=None, session_id="test-session", **kwargs,
    )
    return event, client


CLEAN = "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."


def test_a_recited_reply_is_regenerated_once_with_the_directive_line():
    event, client = _turn([[DEMO_TEXT], [CLEAN]])
    calls = client.messages.captured_stream_calls
    assert len(calls) == 2
    first, second = (_system_text(system) for system, _messages in calls)
    assert DIRECTIVE_LINE not in first
    assert second.rstrip().endswith(DIRECTIVE_LINE)
    assert event["text"] == "We did not claim to have seen him ourselves."
    assert event["recited_demonstration"] is False
    assert event["attempts_meta"]["recitation_regenerated"] is True


def test_a_second_recitation_passes_through_and_is_recorded_without_a_third_call():
    event, client = _turn([[DEMO_TEXT], [DEMO_TEXT + " Again."]])
    assert len(client.messages.captured_stream_calls) == 2
    assert event["recited_demonstration"] is True
    assert event["text"] == DEMO_TEXT + " Again."
    assert event["attempts_meta"]["recitation_regenerated"] is True


def test_nineteen_matching_words_trigger_nothing():
    reply = " ".join(DEMO_WORDS[: RECITATION_WORDS - 1]) + " and that is where it ends."
    event, client = _turn([[reply]])
    assert len(client.messages.captured_stream_calls) == 1
    assert event["recited_demonstration"] is False
    assert event["attempts_meta"]["recitation_regenerated"] is False


def test_twenty_matching_words_trigger_exactly_one_regeneration():
    reply = " ".join(DEMO_WORDS[:RECITATION_WORDS]) + " and that is where it ends."
    event, client = _turn([[reply], [CLEAN]])
    assert len(client.messages.captured_stream_calls) == 2
    assert event["recited_demonstration"] is False


def test_a_reply_already_streamed_is_never_regenerated_over():
    shown = []
    first = (
        "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]], and we have held to that word "
        "for as long as any of us can remember. " + DEMO_TEXT
    )
    event, client = _turn([[first]], on_sentence=shown.append)
    assert len(client.messages.captured_stream_calls) == 1
    assert event["recited_demonstration"] is True
    assert len(shown) == 1


def test_a_held_recitation_is_regenerated_before_anything_is_shown():
    shown = []
    event, client = _turn([[DEMO_TEXT + " Then it ended."], [CLEAN]], on_sentence=shown.append)
    assert shown == []
    assert len(client.messages.captured_stream_calls) == 2
    assert event["recited_demonstration"] is False


def _system_text(system) -> str:
    if isinstance(system, str):
        return system
    return "".join(block.get("text", "") for block in system)
