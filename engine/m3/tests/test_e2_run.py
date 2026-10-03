"""engine.m3.e2_run's arm logic, with the gate, the voice turn and the
world load replaced by fakes, so nothing here reaches the network."""
from types import SimpleNamespace

import pytest

import engine.m3.e2_run as e2


class _Fake:
    """Voice turns in order; each one carries the offenses _offenses will report."""

    def __init__(self, drafts):
        self.drafts = list(drafts)
        self.corrections = []

    def turn(self, **kw):
        self.corrections.append(kw.get("correction"))
        text, hard, uncited = self.drafts.pop(0)
        event = {"text": text, "citations": [], "grounding": {"hard": hard, "uncited": uncited, "sentences": []}}
        return event, []


@pytest.fixture
def harness(monkeypatch):
    def setup(drafts):
        fake = _Fake(drafts)
        routing = SimpleNamespace(action="voice_pass_through", out_of_scope_class=None, directive=None)
        monkeypatch.setattr(e2, "run_gate", lambda **kw: SimpleNamespace(gate_result=SimpleNamespace(routing=routing), usage_records=[]))
        monkeypatch.setattr(e2, "_run_ordinary_voice_turn", fake.turn)
        monkeypatch.setattr(e2, "_offenses", lambda net, names: (net["hard"], net["uncited"]))
        monkeypatch.setattr(e2, "find_uncited_claims", lambda sentences: [])
        monkeypatch.setattr(e2, "_usd", lambda records: 0.0)
        monkeypatch.setattr(e2.protocol, "battery", lambda: [{"probe_id": "p1", "cell": "C-I"}])
        monkeypatch.setattr(e2.sealed_probes, "read_probe", lambda pid: {"text": "q"})
        monkeypatch.setattr(e2.evidence, "repository_records_by_id", lambda repo: {})
        monkeypatch.setattr(e2, "known_tradition_names", lambda registry, exclude_world_key: [])
        loader = SimpleNamespace(load=lambda *a, **kw: (SimpleNamespace(repository=None), None))
        registry = {"w": {"package": {"location": "x", "manifest_hash": "h"}}}
        rows, spent, aborted = e2.run_world("w", registry=registry, loader=loader, client=None, voice_model_id="v",
                                            safety_model_id="s", spent_before=0.0, max_usd=1.0, limit=None)
        return rows[0]["arms"], fake.corrections
    return setup


def test_a_clean_draft_is_never_regenerated(harness):
    arms, corrections = harness([("clean", [], [])])
    assert corrections == [None]
    assert arms["paragraph"]["regenerated"] is False and arms["sentence"]["regenerated"] is False
    assert arms["off"]["answer_text"] == arms["paragraph"]["answer_text"] == arms["sentence"]["answer_text"] == "clean"


def test_sentence_arm_names_every_uncited_sentence_and_its_retry_stands(harness):
    uncited = [{"sentence": "A.", "class": "uncited_claim"}, {"sentence": "B.", "class": "uncited_claim"}]
    arms, corrections = harness([("draft", [], uncited), ("retry", [], uncited)])
    assert arms["paragraph"]["regenerated"] is False
    assert arms["sentence"] == {**arms["sentence"], "answer_text": "retry", "regenerated": True}
    assert '"A."' in corrections[1] and '"B."' in corrections[1]


def test_paragraph_arm_hands_to_the_facilitator_when_the_retry_still_fails(harness):
    hard = [{"sentence": "P.", "class": "wholly_uncited_paragraph"}]
    arms, corrections = harness([("draft", hard, []), ("retry", hard, []), ("sentence retry", [], [])])
    assert arms["paragraph"]["handed_to_facilitator"] is True and arms["paragraph"]["answer_text"] == ""
    assert '"P."' in corrections[1] and '"P."' in corrections[2]
    assert arms["sentence"]["answer_text"] == "sentence retry"


def test_paragraph_arm_keeps_a_retry_that_clears(harness):
    hard = [{"sentence": "P.", "class": "wholly_uncited_paragraph"}]
    arms, _ = harness([("draft", hard, []), ("fixed", [], []), ("sentence retry", [], [])])
    assert arms["paragraph"]["handed_to_facilitator"] is False and arms["paragraph"]["answer_text"] == "fixed"


def test_records_only_mode_is_one_draft_carrying_the_instruction(monkeypatch):
    fake = _Fake([("inside", [], [])])
    routing = SimpleNamespace(action="voice_pass_through", out_of_scope_class=None, directive=None)
    monkeypatch.setattr(e2, "run_gate", lambda **kw: SimpleNamespace(gate_result=SimpleNamespace(routing=routing), usage_records=[]))
    monkeypatch.setattr(e2, "_run_ordinary_voice_turn", fake.turn)
    monkeypatch.setattr(e2, "find_uncited_claims", lambda sentences: [])
    monkeypatch.setattr(e2, "_usd", lambda records: 0.0)
    monkeypatch.setattr(e2.protocol, "battery", lambda: [{"probe_id": "p1", "cell": "C-I"}])
    monkeypatch.setattr(e2.sealed_probes, "read_probe", lambda pid: {"text": "q"})
    monkeypatch.setattr(e2.evidence, "repository_records_by_id", lambda repo: {})
    monkeypatch.setattr(e2, "known_tradition_names", lambda registry, exclude_world_key: [])
    loader = SimpleNamespace(load=lambda *a, **kw: (SimpleNamespace(repository=None), None))
    registry = {"w": {"package": {"location": "x", "manifest_hash": "h"}}}
    rows, _, _ = e2.run_world("w", registry=registry, loader=loader, client=None, voice_model_id="v", safety_model_id="s",
                              spent_before=0.0, max_usd=1.0, limit=None, mode="records-only")
    assert fake.corrections == [e2.RECORDS_ONLY]
    assert list(rows[0]["arms"]) == ["records_only"] and rows[0]["arms"]["records_only"]["answer_text"] == "inside"
