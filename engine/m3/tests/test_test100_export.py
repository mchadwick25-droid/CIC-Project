from engine.m3.test100_export import build_export, gate_rows

ANSWER = {
    "text": "He said so.", "raw_text": "He said so [[a.b]]. Gone [[c.d]].", "citation_entries": [{"sentence": "He said so.", "record_ids": ["a.b"]}],
    "net_sentences": [{"draft": "He said so [[a.b]].", "sentence": "He said so.", "verdict": "ok", "tags": ["a.b"], "why": "grounded"}],
    "reply_shape": {"removed": [{"draft": "Gone [[c.d]].", "sentence": "Gone.", "why": "no support"}]},
}


def test_gate_rows_have_the_replay_shape_for_shipped_and_removed_sentences():
    kept, removed = gate_rows("lpc", "q001", ANSWER)
    assert kept == {"world": "lpc", "probe_id": "q001", "draft": "He said so [[a.b]].", "shown": "He said so.", "verdict": "ok", "why": "grounded", "removed": False, "cited": True}
    assert removed["verdict"] == "withhold" and removed["removed"] is True and removed["shown"] is None and removed["draft"] == "Gone [[c.d]]."


def test_the_report_carries_each_question_as_a_probe_and_lists_the_unanswered(tmp_path):
    import json

    (tmp_path / "q001.json").write_text(json.dumps(ANSWER))
    questions = [{"id": "q001", "group": "B"}, {"id": "q002", "group": "B"}]
    report, rows, missing = build_export(questions, tmp_path, "lpc", "sha256:x")
    probe = report["worlds"]["lpc"]["per_probe"][0]
    assert probe["probe_id"] == "q001" and probe["transcript"]["raw_text"].startswith("He said")
    assert report["run_settings"]["package_manifest_hash"] == {"lpc": "sha256:x"} and len(rows) == 2 and missing == ["q002"]
