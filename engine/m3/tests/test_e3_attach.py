"""engine.m3.e3_attach's attach step with a fake client, so nothing here
reaches the network."""
import json
from types import SimpleNamespace

import engine.m3.e3_attach as e3


class _Client:
    def __init__(self, proposal, verdicts):
        self.proposal = proposal
        self.verdicts = list(verdicts)
        self.verified = []
        self.messages = self

    def create(self, **kw):
        usage = SimpleNamespace(input_tokens=1, output_tokens=1, cache_creation_input_tokens=0, cache_read_input_tokens=0)
        if kw["max_tokens"] == e3.VERIFY_MAX_TOKENS:
            self.verified.append(kw["messages"][0]["content"])
            text = self.verdicts.pop(0)
        else:
            text = json.dumps(self.proposal)
        return SimpleNamespace(content=[SimpleNamespace(text=text)], usage=usage)


TABLE = SimpleNamespace(input_per_token=0, output_per_token=0, cache_write_per_token=0, cache_read_per_token=0, source="t")
RECORDS = {"w.dw.a": {"record_type": "doctrinal_witness", "text": "A is so."}, "w.dw.b": {"record_type": "doctrinal_witness", "text": "B is so."}}
TRANSCRIPT = {
    "answer_text": "A is so. B is so. C is so.",
    "citation_entries": [],
    "uncited_claim_sentences": ["A is so.", "B is so.", "C is so."],
}


def _run(proposal, verdicts, monkeypatch):
    monkeypatch.setattr(e3, "estimate_cost", lambda usage, table: SimpleNamespace(dollars=0.0))
    client = _Client(proposal, verdicts)
    out, _ = e3.attach(client, "m", TABLE, prompt_text="P", valid_ids=sorted(RECORDS), records=RECORDS, transcript=TRANSCRIPT)
    return out, client


def test_only_a_carries_verdict_is_attached_and_the_text_is_unchanged(monkeypatch):
    proposal = [{"id": "S1", "record_id": "w.dw.a"}, {"id": "S2", "record_id": "w.dw.b"}, {"id": "S3", "record_id": None}]
    out, _ = _run(proposal, ["carries", "partly\n\nthe record adds"], monkeypatch)
    assert out["answer_text"] == TRANSCRIPT["answer_text"]
    assert out["citation_entries"] == [{"sentence": "A is so.", "record_ids": ["w.dw.a"], "attached": True}]
    assert out["uncited_claim_sentences"] == ["B is so.", "C is so."]


def test_an_id_outside_the_valid_list_is_rejected_without_a_verify_call(monkeypatch):
    out, client = _run([{"id": "S1", "record_id": "w.witness.c-e"}], [], monkeypatch)
    assert client.verified == []
    assert out["citation_entries"] == [] and out["attach_trail"][0]["verdict"] == "rejected"


def test_first_word_reads_the_verdict_past_trailing_text():
    assert e3.first_word("Carries.\n\nThe record states it.") == "carries"
    assert e3.first_word("") == ""


def test_malformed_proposals_are_rejected_never_attached(monkeypatch):
    out, client = _run([{"id": "w.dw.a", "record_id": "w.dw.a"}, "junk"], [], monkeypatch)
    assert client.verified == [] and out["citation_entries"] == []


def test_parse_proposals_tolerates_trailing_text():
    assert e3.parse_proposals('[{"id": "S1", "record_id": null}]\n[{"extra": 1}]') == [{"id": "S1", "record_id": None}]
    assert e3.parse_proposals("no json here") == []
