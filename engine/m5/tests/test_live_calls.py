from types import SimpleNamespace

from anthropic import APITimeoutError

from engine.m5 import live_calls


class _Messages:
    def __init__(self, response=None, raise_timeout=False):
        self.response = response
        self.raise_timeout = raise_timeout
        self.calls = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        if self.raise_timeout:
            raise APITimeoutError(request=SimpleNamespace(method="POST", url="https://bedrock"))
        return self.response


class _Client:
    def __init__(self, messages):
        self.messages = messages
        self.options = []

    def with_options(self, **options):
        self.options.append(options)
        return self


def _tool_response(value):
    block = SimpleNamespace(type="tool_use", name=live_calls._SAFETY_TOOL["name"], input=value)
    return SimpleNamespace(content=[block], usage=None)


def test_safety_call_waits_fifteen_seconds_and_retries_once():
    client = _Client(_Messages(response=_tool_response({"signal": "NO_SIGNAL"})))
    outcome = live_calls.call_safety(client, "m", message="hello", recent_window=[], accumulator={})
    assert outcome.status == "ok"
    assert client.messages.calls[0]["timeout"] == live_calls.SAFETY_TIMEOUT_SECONDS == 15.0
    assert client.options == [{"max_retries": live_calls.SAFETY_MAX_RETRIES}]
    assert live_calls.SAFETY_MAX_RETRIES == 1


def test_safety_call_reports_a_timeout_as_a_failed_outcome():
    client = _Client(_Messages(raise_timeout=True))
    outcome = live_calls.call_safety(client, "m", message="hello", recent_window=[], accumulator={})
    assert outcome.failed and outcome.status == "timeout"


def test_reader_call_keeps_its_own_short_timeout():
    client = _Client(_Messages(response=SimpleNamespace(content=[], usage=None)))
    live_calls.call_reader(client, "m", message="hello")
    assert client.messages.calls[0]["timeout"] == 4.0
    assert client.options == []
