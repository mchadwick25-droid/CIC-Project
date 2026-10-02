"""A reply is never shown, stored or graded cut off mid-sentence.

The cases below are the endings seen in a live 15-turn alx run, where seven
replies stopped at the 1,024-token ceiling.
"""
from types import SimpleNamespace

import pytest

from engine.m4.completeness import ends_on_full_stop, trim_to_complete_sentence
from engine.m4.generation import VOICE_MAX_TOKENS, stream_voice_turn
from engine.m4.output_check import check_output
from engine.m4.streaming import stream_voice_turn_sentences
from engine.m4.tests.test_streaming import REPOSITORY
from engine.m4.tests.test_turn import FakeBedrockClient, _reader, _safety, _world
from engine.m4.turn import run_turn

FINISHED = "We kept the teaching close. A student learns by living it [[fix.witness.who-is-jesus]]."


@pytest.mark.parametrize("text", [
    "We kept the teaching close.",
    "Is that the question you are asking?",
    "He said, \"let truth win in the open.\"",
    "We kept it close [[fix.witness.who-is-jesus]].",
    "We kept it close. [[fix.witness.who-is-jesus]]",
    "We kept it close.\n",
])
def test_finished_text_is_recognised(text):
    assert ends_on_full_stop(text)


@pytest.mark.parametrize("text", [
    "",
    "   ",
    "what you do in it now is what shapes the soul",
    "let truth win in the open. At our worst—",
    "We kept it close. Then they said, \"let truth win in the open. At our",
    "We kept it close. A student learns by living it [[fix.witness.who-",
    "We kept it close, and",
])
def test_cut_off_text_is_recognised(text):
    assert not ends_on_full_stop(text)


def test_trim_returns_finished_text_whole():
    assert trim_to_complete_sentence(FINISHED) == (FINISHED, "")


def test_trim_cuts_back_to_the_last_finished_sentence():
    cut = "We kept the teaching close. A student learns by living it. What you do in it now is what shapes"
    kept, dropped = trim_to_complete_sentence(cut)
    assert kept == "We kept the teaching close. A student learns by living it."
    assert dropped == " What you do in it now is what shapes"
    assert kept + dropped == cut


def test_trim_never_leaves_a_quotation_open():
    cut = 'We kept it close. They wrote, "Hold fast. Let truth win in the open. At our worst'
    kept, dropped = trim_to_complete_sentence(cut)
    assert kept == "We kept it close."
    assert ends_on_full_stop(kept)
    assert kept + dropped == cut


def test_trim_drops_a_dangling_tag_with_its_sentence():
    cut = "We kept it close. A student learns by living it [[fix.witness.who-"
    assert trim_to_complete_sentence(cut)[0] == "We kept it close."


def test_trim_of_a_single_unfinished_sentence_is_empty():
    assert trim_to_complete_sentence("what you do in it now") == ("", "what you do in it now")


class _Ctx:
    def __init__(self, chunks, stop_reason):
        self._chunks, self._stop_reason = chunks, stop_reason

    def __enter__(self):
        usage = SimpleNamespace(input_tokens=1, output_tokens=1, cache_creation_input_tokens=0, cache_read_input_tokens=0)
        final = SimpleNamespace(usage=usage, stop_reason=self._stop_reason)
        return SimpleNamespace(text_stream=iter(self._chunks), get_final_message=lambda: final)

    def __exit__(self, *exc):
        return False


class _Messages:
    def __init__(self, chunks, stop_reason):
        self._chunks, self._stop_reason = chunks, stop_reason
        self.max_tokens_seen = []

    def stream(self, *, model, max_tokens, system=None, messages, timeout=None):
        self.max_tokens_seen.append(max_tokens)
        return _Ctx(self._chunks, self._stop_reason)


def _client(chunks, stop_reason):
    return SimpleNamespace(messages=_Messages(chunks, stop_reason))


CUT_CHUNKS = ["We kept the teaching close. ", "A student learns by living it. ", "What you do in it now is what shapes the soul"]


def test_a_reply_stopped_at_the_ceiling_is_cut_back_to_a_finished_sentence():
    client = _client(CUT_CHUNKS, "max_tokens")
    outcome = stream_voice_turn(client, "m", system_prompt="s", message="hi")
    result = outcome.value
    assert result.truncated
    assert ends_on_full_stop(result.text)
    assert result.text == "We kept the teaching close. A student learns by living it."
    assert result.dropped == " What you do in it now is what shapes the soul"


def test_a_reply_the_model_finished_is_left_alone():
    client = _client(["We kept the teaching close. ", "A student learns by living it."], "end_turn")
    result = stream_voice_turn(client, "m", system_prompt="s", message="hi").value
    assert not result.truncated
    assert result.text == "We kept the teaching close. A student learns by living it."


def test_the_ceiling_is_well_above_the_longest_reply_seen():
    client = _client(["Fine."], "end_turn")
    stream_voice_turn(client, "m", system_prompt="s", message="hi")
    assert client.messages.max_tokens_seen == [VOICE_MAX_TOKENS]
    assert VOICE_MAX_TOKENS >= 2048


def _turn(client):
    return run_turn(
        session_id="test-session", voice_client=client, voice_model_id="m", safety_client=client, safety_model_id="m",
        world=_world(), participant_message="who was Jesus", pressed={}, anachronistic_term_ids=set(),
    )


class _CutClient(FakeBedrockClient):
    """The fixture client, with the voice stream stopping at the ceiling."""

    def __init__(self, chunks, stop_reason):
        super().__init__(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_chunks=chunks)
        voice = _Messages(chunks, stop_reason)
        gates = self.messages

        def stream(**kwargs):
            return voice.stream(**kwargs)

        gates.stream = stream


def test_a_participant_never_sees_a_reply_that_stops_mid_sentence():
    chunks = [
        "We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]. ",
        "We kept what we were handed. What you do with it now is what shapes the soul",
    ]
    result = _turn(_CutClient(chunks, "max_tokens"))
    text = result.voice_event["text"]
    assert ends_on_full_stop(text), text
    assert text == "We did not claim to have seen him ourselves. We kept what we were handed."
    assert "shapes the soul" not in text
    assert result.voice_event["attempts_meta"]["voice_truncated"] is True
    assert not [d for d in result.voice_event["output_defects"] if d["family"] == "cutoff"]


def test_an_untruncated_turn_reports_no_truncation():
    result = _turn(_CutClient(["We did not claim to have seen him ourselves [[fix.witness.who-is-jesus]]."], "end_turn"))
    assert result.voice_event["attempts_meta"]["voice_truncated"] is False


def test_the_output_check_flags_a_reply_that_stops_mid_sentence():
    findings = check_output("We kept it close. What you do in it now is what shapes the soul")
    assert [f["family"] for f in findings if f["family"] == "cutoff"] == ["cutoff"]
    assert not [f for f in check_output("We kept it close. What you do in it now shapes the soul.") if f["family"] == "cutoff"]


def _sentence_stream(chunks, stop_reason):
    client = _client(chunks, stop_reason)
    return list(stream_voice_turn_sentences(
        client, "m", system_prompt="s", message="hi", repository_records=REPOSITORY, world_key="fix",
    ))


def test_the_sentence_stream_never_emits_a_cut_off_tail():
    chunks = ["We did not claim to have seen him ourselves. ", "We kept what we were handed. What you do with it now shapes"]
    events = _sentence_stream(chunks, "max_tokens")
    done = events[-1]
    assert done["type"] == "done"
    assert done["truncated"] is True
    assert ends_on_full_stop(done["answer_text"])
    assert "shapes" not in done["answer_text"]


def test_the_sentence_stream_keeps_a_last_sentence_that_did_finish():
    chunks = ["We did not claim to have seen him ourselves. ", "We kept what we were handed."]
    done = _sentence_stream(chunks, "max_tokens")[-1]
    assert done["truncated"] is True
    assert done["answer_text"].endswith("We kept what we were handed.")
