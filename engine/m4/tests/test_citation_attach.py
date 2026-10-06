"""engine.m4.citation_attach with a fake client: nothing reaches the network."""
import json
from types import SimpleNamespace

import anthropic
import httpx

from engine.m4 import citation_attach as ca

RECORDS = {
    "w.dw.a": {"record_type": "doctrinal_witness", "text": "A is so."},
    "w.dw.b": {"record_type": "doctrinal_witness", "text": "B is so."},
}
PROMPT = "## A (cite as [[w.dw.a]])\nA is so.\n## B (cite as [[w.dw.b]])\nB is so.\n"
NET = {"sentences": [
    {"sentence": "A is so.", "tags": [], "verdict": "ok"},
    {"sentence": "B is so.", "tags": [], "verdict": "ok"},
    {"sentence": "C is cited.", "tags": ["w.dw.a"], "verdict": "ok"},
]}
USAGE = SimpleNamespace(input_tokens=1, output_tokens=1, cache_creation_input_tokens=0, cache_read_input_tokens=0)


class _Client:
    def __init__(self, proposal, verdicts, fail_on_verify=None):
        self.proposal, self.verdicts, self.fail_on_verify = proposal, list(verdicts), fail_on_verify
        self.calls = []
        self.messages = self

    def create(self, **kw):
        self.calls.append(kw)
        if kw["max_tokens"] == ca.VERIFY_MAX_TOKENS:
            if self.fail_on_verify is not None and len(self.calls) - 1 == self.fail_on_verify:
                raise anthropic.APIConnectionError(request=httpx.Request("POST", "https://x"))
            text = self.verdicts.pop(0)
        else:
            text = json.dumps(self.proposal)
        return SimpleNamespace(content=[SimpleNamespace(text=text)], usage=USAGE)


def _attach(client):
    return ca.attach_citations(client=client, model_id="haiku", prompt_text=PROMPT, repository_records=RECORDS,
                               net_result=NET, session_id="s1", world_key="w")


def test_only_carries_is_attached_and_only_uncited_claims_are_offered():
    client = _Client([{"id": "S1", "record_id": "w.dw.a"}, {"id": "S2", "record_id": "w.dw.b"}], ["carries", "partly"])
    added, usage, trail = _attach(client)
    assert added == [{"sentence": "A is so.", "record_ids": ["w.dw.a"], "attached": True}]
    assert "C is cited." not in client.calls[0]["messages"][0]["content"]
    assert [u.call_kind for u in usage] == ["citation_propose", "citation_verify", "citation_verify"]
    assert [t["verdict"] for t in trail] == ["carries", "partly"]


def test_an_id_the_prompt_does_not_offer_is_rejected_without_a_check_call():
    client = _Client([{"id": "S1", "record_id": "w.witness.c-e"}, {"id": "S2", "record_id": None}], [])
    added, usage, trail = _attach(client)
    assert added == [] and len(client.calls) == 1
    assert [t["verdict"] for t in trail] == ["rejected", "none"]


def test_an_api_error_keeps_what_was_verified_and_does_not_raise():
    client = _Client([{"id": "S1", "record_id": "w.dw.a"}, {"id": "S2", "record_id": "w.dw.b"}], ["carries"], fail_on_verify=2)
    added, _, trail = _attach(client)
    assert [a["sentence"] for a in added] == ["A is so."] and "error" in trail[-1]


def test_no_uncited_claims_means_no_calls():
    client = _Client([], [])
    net = {"sentences": [{"sentence": "C is cited.", "tags": ["w.dw.a"], "verdict": "ok"}]}
    assert ca.attach_citations(client=client, model_id="h", prompt_text=PROMPT, repository_records=RECORDS,
                               net_result=net, session_id="s1") == ([], [], [])
    assert client.calls == []


def test_citable_ids_are_prompt_ids_that_are_real_records():
    assert ca.citable_ids(PROMPT + "[[w.ghost]]", RECORDS) == ["w.dw.a", "w.dw.b"]


def _reset_guards(monkeypatch):
    monkeypatch.setattr(ca, "_slots", __import__("threading").BoundedSemaphore(ca.MAX_CONCURRENT))
    monkeypatch.setattr(ca, "_cooldown_until", 0.0)


def test_a_rate_limit_pauses_the_step_for_later_turns(monkeypatch):
    _reset_guards(monkeypatch)

    class Limited(_Client):
        def create(self, **kw):
            self.calls.append(kw)
            raise anthropic.RateLimitError("slow down", response=httpx.Response(429, request=httpx.Request("POST", "https://x")), body=None)

    added, _, trail = _attach(Limited([], []))
    assert added == [] and "error" in trail[-1]
    later = _Client([{"id": "S1", "record_id": "w.dw.a"}], ["carries"])
    added, usage, trail = _attach(later)
    assert later.calls == [] and trail == [{"skipped": "cooling down after a rate limit"}]


def test_a_turn_with_no_free_slot_skips_the_step(monkeypatch):
    _reset_guards(monkeypatch)
    for _ in range(ca.MAX_CONCURRENT):
        ca._slots.acquire()
    client = _Client([{"id": "S1", "record_id": "w.dw.a"}], ["carries"])
    added, _, trail = _attach(client)
    assert client.calls == [] and trail == [{"skipped": "concurrency cap reached"}]


def test_slots_are_released_after_each_turn(monkeypatch):
    _reset_guards(monkeypatch)
    for _ in range(ca.MAX_CONCURRENT + 1):
        added, _, _ = _attach(_Client([{"id": "S1", "record_id": "w.dw.a"}], ["carries"]))
        assert len(added) == 1


def test_check_calls_per_turn_are_capped(monkeypatch):
    _reset_guards(monkeypatch)
    monkeypatch.setattr(ca, "MAX_CHECKS_PER_TURN", 1)
    client = _Client([{"id": "S1", "record_id": "w.dw.a"}, {"id": "S2", "record_id": "w.dw.b"}], ["carries"])
    added, _, trail = _attach(client)
    assert len(client.calls) == 2 and trail[-1]["verdict"] == "skipped: check cap"
