import json

import pytest

from engine.m3.reply_client import PendingReply, ReplyFileClient
from engine.m3.test100 import _outside_repo

TOOL = {"name": "submit_x", "input_schema": {"type": "object"}}


def _client(tmp_path):
    return ReplyFileClient(question_id="q001", reply_dir=tmp_path / "replies", pending_dir=tmp_path / "pending")


def test_a_tool_call_without_a_reply_is_left_pending_with_its_request(tmp_path):
    with pytest.raises(PendingReply) as pending:
        _client(tmp_path).messages.create(system="sys", tools=[TOOL], messages=[{"role": "user", "content": "hello"}])
    assert pending.value.key == "q001.submit_x.1"
    request = json.loads((tmp_path / "pending" / "q001.submit_x.1.request.json").read_text())
    assert request["reply_schema"] == {"type": "object"}
    prompt = (tmp_path / "pending" / "q001.submit_x.1.prompt.txt").read_text()
    assert "hello" in prompt and "system-" in prompt


def test_a_tool_call_answers_from_its_reply_file(tmp_path):
    (tmp_path / "replies").mkdir()
    (tmp_path / "replies" / "q001.submit_x.1.json").write_text('{"a": 1}')
    response = _client(tmp_path).messages.create(system="sys", tools=[TOOL], messages=[{"role": "user", "content": "hi"}])
    assert response.content[0].type == "tool_use" and response.content[0].input == {"a": 1}


def test_a_voice_call_streams_its_reply_text_and_counts_each_call(tmp_path):
    (tmp_path / "replies").mkdir()
    (tmp_path / "replies" / "q001.voice.1.txt").write_text("First draft.")
    client = _client(tmp_path)
    with client.messages.stream(system=[{"type": "text", "text": "s"}], messages=[{"role": "user", "content": "q"}]) as stream:
        assert "".join(stream.text_stream) == "First draft."
    with pytest.raises(PendingReply) as pending:
        client.messages.stream(system="s", messages=[{"role": "user", "content": "q"}])
    assert pending.value.key == "q001.voice.2"


def test_a_reply_that_is_not_json_is_an_error_not_a_pending_call(tmp_path):
    (tmp_path / "replies").mkdir()
    (tmp_path / "replies" / "q001.submit_x.1.json").write_text("not json")
    with pytest.raises(ValueError):
        _client(tmp_path).messages.create(system="s", tools=[TOOL], messages=[{"role": "user", "content": "q"}])


def test_the_work_directory_may_not_be_inside_the_repository():
    with pytest.raises(SystemExit):
        _outside_repo(__import__("pathlib").Path("engine/m3"))


def test_offered_ids_are_the_records_a_voice_request_offers_in_order_without_repeats():
    from engine.m3.reply_client import offered_ids

    request = {"kind": "voice", "messages": [{"role": "user", "text": "## Ground\n- [[a.b.c]] witness, x\n- [[d.e.f]] limit, y\nQ?\n- [[a.b.c]] again"}]}
    assert offered_ids(request) == ["a.b.c", "d.e.f"]
    assert offered_ids({"kind": "submit_reader_output", "messages": request["messages"]}) == []


def test_offered_ids_read_a_quote_or_story_marker_as_the_record_it_names():
    from engine.m3.reply_client import offered_ids

    text = "- [[quote:lpc.quote.a-dreadful-plague-broke-out]] x\n- [[story:lpc.story.celerinus-writes-to-lucian]] y\n- [[lpc.story.celerinus-writes-to-lucian]] z"
    assert offered_ids({"kind": "voice", "messages": [{"role": "user", "text": text}]}) == [
        "lpc.quote.a-dreadful-plague-broke-out", "lpc.story.celerinus-writes-to-lucian"]


def test_offered_ids_read_a_quote_or_story_marker_as_the_record_it_names():
    from engine.m3.reply_client import offered_ids

    text = "- [[quote:lpc.quote.a-dreadful-plague-broke-out]] x\n- [[story:lpc.story.celerinus-writes-to-lucian]] y\n- [[lpc.story.celerinus-writes-to-lucian]] z"
    assert offered_ids({"kind": "voice", "messages": [{"role": "user", "text": text}]}) == [
        "lpc.quote.a-dreadful-plague-broke-out", "lpc.story.celerinus-writes-to-lucian"]
