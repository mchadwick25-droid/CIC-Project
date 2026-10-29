"""The Converse seam: no client without an approved live test, and an
approved client counts every vendor's call against the cap the same way.
No network: the Bedrock runtime is a recording fake."""
import json
import sys
from types import SimpleNamespace

import pytest

from engine.provider import bedrock_converse, guard

GPT = "us.openai.gpt-6.1-sol"


@pytest.fixture(autouse=True)
def _clean_guard(monkeypatch, tmp_path):
    monkeypatch.setenv(guard.LEDGER_ENV, str(tmp_path / "ledger.jsonl"))
    monkeypatch.setattr(guard, "_emit", lambda text: None)
    guard.reset_for_tests()
    yield
    guard.reset_for_tests()


@pytest.fixture
def runtime(monkeypatch):
    calls = []

    def converse(**request):
        calls.append(request)
        return {
            "output": {"message": {"role": "assistant", "content": [{"reasoningContent": {"x": 1}}, {"text": '{"verdict": "supported"}'}]}},
            "usage": {"inputTokens": 1000, "outputTokens": 200, "totalTokens": 1200},
            "stopReason": "end_turn",
        }

    built = []
    monkeypatch.setattr(bedrock_converse.boto3, "client", lambda *a, **kw: (built.append((a, kw)), SimpleNamespace(converse=converse))[1])
    return SimpleNamespace(calls=calls, built=built)


def test_without_both_flags_no_client_is_built(runtime, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog"])
    with pytest.raises(SystemExit):
        bedrock_converse.make_client("us-east-1")
    assert runtime.built == [] and runtime.calls == []


def test_an_approved_call_is_shaped_counted_and_ledgered(runtime, monkeypatch, tmp_path):
    monkeypatch.setattr(sys, "argv", ["prog", "--live-test", "converse proof", "--cap-usd", "1.00"])
    client = bedrock_converse.make_client("us-east-1")
    reply = client.messages.create(
        model=GPT, max_tokens=500, system="s", messages=[{"role": "user", "content": "q"}],
        additional_model_request_fields={"reasoning": {"effort": "high"}},
    )
    assert [b.text for b in reply.content] == ['{"verdict": "supported"}']
    sent = runtime.calls[0]
    assert sent["modelId"] == GPT and sent["system"] == [{"text": "s"}] and sent["inferenceConfig"] == {"maxTokens": 500}
    assert sent["messages"] == [{"role": "user", "content": [{"text": "q"}]}]
    assert sent["additionalModelRequestFields"] == {"reasoning": {"effort": "high"}}
    assert runtime.built[0][1]["config"].retries["max_attempts"] == 1
    expected = 1000 * 2.20 / 1e6 + 200 * 11.00 / 1e6
    assert guard.priced_total() == pytest.approx(expected)
    events = [json.loads(line)["event"] for line in (tmp_path / "ledger.jsonl").read_text().splitlines()]
    assert events == ["hold", "settle"]


def test_the_cap_stops_a_call_before_it_is_made(runtime, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog", "--live-test", "converse proof", "--cap-usd", "0.001"])
    client = bedrock_converse.make_client("us-east-1")
    with pytest.raises(guard.LiveTestCapReached):
        client.messages.create(model=GPT, max_tokens=4000, messages=[{"role": "user", "content": "q"}])
    assert runtime.calls == []


def test_a_model_with_no_approved_price_is_refused(runtime, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["prog", "--live-test", "converse proof", "--cap-usd", "1.00"])
    client = bedrock_converse.make_client("us-east-1")
    with pytest.raises(guard.LiveTestGuardError):
        client.messages.create(model="us.openai.gpt-6.1-terra", max_tokens=10, messages=[{"role": "user", "content": "q"}])
    assert runtime.calls == []
