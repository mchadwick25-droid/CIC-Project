"""The per-answer log joins what each shadow stage wrote."""
import json

from engine.m3 import test100_log as log


def _read(status):
    return {"question_id": "q1", "status": status, "units": [], "unsupported": {}, "dropped": []}


def test_how_an_answer_ended_is_what_the_check_recorded_not_a_guess_from_its_text():
    endings = {"q1": "rewritten", "q2": "abstained_too_little"}
    assert log.ending(endings, "q1", "We do not have that here. Then more.") == "rewritten"
    assert log.ending(endings, "q2", "We do not have that here.") == "abstained_too_little"
    assert log.ending(endings, "q3", "text") == "incomplete" and log.ending(endings, "q1", None) == "incomplete"


def test_a_record_is_written_per_answer_with_its_stages(tmp_path):
    (tmp_path / "answers").mkdir()
    (tmp_path / "answers" / "q1.json").write_text(json.dumps({"text": "Shown.", "raw_text": "Draft.", "offered": ["a.b.c"], "sub_question": "C1.S1"}), encoding="utf-8")
    (tmp_path / "bound").mkdir()
    (tmp_path / "bound" / "items.jsonl").write_text(json.dumps({"question_id": "q1", "n": 0, "sentence": "Shown.", "tags": ["a.b.c"], "label": "paraphrase", "decision": "keep", "reason": None, "placed": False, "placed_id": None}) + "\n", encoding="utf-8")
    (tmp_path / "check" / "final").mkdir(parents=True)
    (tmp_path / "check" / "read.jsonl").write_text(json.dumps(_read("clean")) + "\n", encoding="utf-8")
    (tmp_path / "check" / "endings.json").write_text(json.dumps({"q1": "clean"}), encoding="utf-8")
    (tmp_path / "check" / "final" / "q1.txt").write_text("Shown.", encoding="utf-8")
    summary = log.run([{"id": "q1", "group": "B", "wording": "A question?"}], tmp_path)
    record = json.loads((tmp_path / "log" / "q1.json").read_text())
    assert summary == {"answers": 1, "clean": 1, "named_a_sub_question": 1}
    assert record["sub_question"] == "C1.S1" and record["sentences"][0]["label"] == "paraphrase" and record["ending"] == "clean"
