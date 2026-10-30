import json

from engine.m3.test100_score import build_sheet, measure

ANSWER = {
    "id": "q001", "group": "B", "text": "He said so. We held to it.", "citations": ["a", "b"], "routing_action": "voice_with_directive",
    "raw_text": "He said so. We held to it.",
    "net_sentences": [{"sentence": "He said so.", "placed_quote": "q.one"}, {"sentence": "We held to it.", "placed_story": "s.one"}],
    "reply_shape": {"removed": [{"why": "no support"}, {"why": "no support"}, {"why": "typed"}], "repaired": [{"record": "q.one"}]},
}


def test_the_measured_columns_come_from_the_answer():
    row = measure({"id": "q001", "group": "B", "cluster": "C3"}, ANSWER, lambda raw, shown: 0)
    assert (row["cuts"], row["quotes_placed"], row["stories_placed"], row["leadins_repaired"], row["citations"]) == (3, 1, 1, 1, 2)
    assert row["cut_reasons"] == "no support x2; typed x1"
    assert row["cluster"] == "C3" and row["words"] == 7


def test_an_unanswered_question_is_listed_not_scored(tmp_path):
    (tmp_path / "q001.json").write_text(json.dumps(ANSWER))
    questions = [{"id": "q001", "group": "B"}, {"id": "q002", "group": "B"}]
    rows, missing = build_sheet(questions, tmp_path)
    assert [r["id"] for r in rows] == ["q001"] and missing == ["q002"]
