"""The live filler answers the requests a run wrote to disk and nothing else; no model is called here."""
import json
from types import SimpleNamespace

from engine.m3 import live_fill


class _Stream:
    def __init__(self, text):
        self.text_stream = iter([text[:3], text[3:]])

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


class _Messages:
    def __init__(self):
        self.calls = []

    def stream(self, **kw):
        self.calls.append(("stream", kw))
        return _Stream("We hold it [[x.y]] [[as:paraphrase]].")

    def create(self, **kw):
        self.calls.append(("create", kw))
        if kw.get("tools"):
            return SimpleNamespace(content=[SimpleNamespace(type="tool_use", input={"signal": "NO_SIGNAL"})])
        return SimpleNamespace(content=[SimpleNamespace(type="text", text='{"sentences": []}')])


def _client():
    return SimpleNamespace(messages=_Messages())


def _request(path, kind):
    path.parent.mkdir(parents=True, exist_ok=True)
    system = path.parent / "system-a.txt"
    system.write_text("SYSTEM TEXT", encoding="utf-8")
    path.write_text(json.dumps({"kind": kind, "reply_schema": {"type": "object"} if kind != "voice" else None, "system_files": [str(system)],
                                "messages": [{"role": "user", "text": "Question?"}]}), encoding="utf-8")


def test_pending_jobs_skip_answered_requests_and_other_questions(tmp_path):
    _request(tmp_path / "pending" / "q001.voice.1.request.json", "voice")
    _request(tmp_path / "pending" / "q002.voice.1.request.json", "voice")
    _request(tmp_path / "pending" / "q003.submit_reader_output.1.request.json", "submit_reader_output")
    (tmp_path / "replies").mkdir()
    (tmp_path / "replies" / "q002.voice.1.txt").write_text("done", encoding="utf-8")
    assert [j["key"] for j in live_fill.pending_jobs(tmp_path, None)] == ["q001.voice.1", "q003.submit_reader_output.1"]
    assert [j["key"] for j in live_fill.pending_jobs(tmp_path, ["q003"])] == ["q003.submit_reader_output.1"]


def test_a_voice_request_is_streamed_and_a_gate_request_is_a_forced_tool_call(tmp_path):
    _request(tmp_path / "pending" / "q001.voice.1.request.json", "voice")
    _request(tmp_path / "pending" / "q001.submit_reader_output.1.request.json", "submit_reader_output")
    client = _client()
    out = {j["key"]: live_fill.answer_pending(client, j, "voice-model", "gate-model") for j in live_fill.pending_jobs(tmp_path, None)}
    assert out["q001.voice.1"].startswith("We hold it")
    assert json.loads(out["q001.submit_reader_output.1"]) == {"signal": "NO_SIGNAL"}
    kinds = {kw["model"]: (name, kw) for name, kw in client.messages.calls}
    assert kinds["voice-model"][0] == "stream" and kinds["voice-model"][1]["max_tokens"] == live_fill.VOICE_MAX_TOKENS
    assert kinds["gate-model"][1]["tool_choice"] == {"type": "tool", "name": "submit_reader_output"}
    assert kinds["voice-model"][1]["system"][-1]["cache_control"] == {"type": "ephemeral"}


def test_a_check_prompt_is_split_into_system_and_user_and_answered_with_the_voice_model(tmp_path):
    prompts = tmp_path / "check" / "read" / "prompts"
    prompts.mkdir(parents=True)
    (prompts / "q001.md").write_text("SYSTEM\nJudge it.\n\nUSER\nQUESTION\nWhy?\n", encoding="utf-8")
    client = _client()
    (job,) = live_fill.check_jobs(tmp_path, "read", None)
    assert live_fill.answer_check(client, job, "read", "voice-model") == '{"sentences": []}'
    call = client.messages.calls[0][1]
    assert call["system"] == "Judge it." and call["messages"][0]["content"].startswith("QUESTION") and call["max_tokens"] == live_fill.CHECK_MAX_TOKENS["read"]
