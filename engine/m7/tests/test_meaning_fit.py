"""engine.m7.meaning_fit: the reviewer's packet is blind and complete, and
the score counts every use, never treating an ungraded one as accepted."""
import json

from engine.m7 import meaning_fit


def _report(raw: str) -> dict:
    return {"worlds": {"w": {"per_probe": [{"probe_id": "p1", "transcript": {"raw_text": raw}}]}}}


RECORDS = {
    "w.quote.a": {"id": "w.quote.a", "record_type": "quote", "modern_rendering": "We judge by Scripture.",
                  "use_note": {"means": "Scripture is the test.", "years": {"from": 1, "to": 2}, "status": "reviewed"}},
    "w.figure.b": {"id": "w.figure.b", "record_type": "figure"},
}


def test_only_sentences_tagged_with_a_citable_record_are_uses():
    uses = meaning_fit.uses_from_report(_report("We test it by Scripture [[w.quote.a]]. He spoke [[w.figure.b]]. Plain words."), "w", RECORDS)
    assert [(u["record_id"], u["sentence"]) for u in uses] == [("w.quote.a", "We test it by Scripture.")]
    assert uses[0]["use_note"]["means"] == "Scripture is the test."


def test_the_packet_hides_which_run_a_use_came_from_and_the_score_counts_every_use(tmp_path, monkeypatch):
    monkeypatch.setattr(meaning_fit, "load_world_records", lambda w: RECORDS)
    runs = {"before": _report("We test it by Scripture [[w.quote.a]]."), "after": _report("Scripture is our test [[w.quote.a]].")}
    assert meaning_fit.build_packet("w", runs, tmp_path, seed=1) == 2
    packet = json.loads((tmp_path / "packet.json").read_text())
    assert all("probe_id" not in u and "run" not in u for u in packet["uses"])
    key = json.loads((tmp_path / "key.json").read_text())
    first, second = sorted(key)
    (tmp_path / "verdicts.json").write_text(json.dumps({first: {"verdict": "misread", "reason": "x"}}))
    scores = meaning_fit.score(tmp_path)
    assert scores[key[first]]["misread"] == 1 and scores[key[first]]["misread_rate"] == 1.0
    assert scores[key[second]]["ungraded"] == 1 and scores[key[second]]["misread_rate"] is None
