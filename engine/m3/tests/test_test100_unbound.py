"""The unbound runner: prompts out, replies in, a final text and a count."""
import json

from engine.m1.loader import load_world_records
from engine.m3 import test100_unbound as tu

LIMIT = "lpc.limit.womens-own-voice"


def _setup(tmp_path):
    work = tmp_path / "run"
    (work / "answers").mkdir(parents=True)
    sentences = ["Bound claim.", "A fact with no citation.", "Here is what we can say.", "Nothing we carry speaks of him.", "Withheld one."]
    answer = {"text": " ".join(sentences), "net_sentences": [
        {"sentence": sentences[0], "tags": [LIMIT], "verdict": "ok"},
        {"sentence": sentences[1], "tags": [], "verdict": "ok"},
        {"sentence": sentences[2], "tags": [], "verdict": "ok"},
        {"sentence": sentences[3], "tags": [], "verdict": "ok"},
        {"sentence": sentences[4], "tags": [], "verdict": "withhold", "why": "x"},
    ], "reply_shape": {"placed": []}}
    (work / "answers" / "q1.json").write_text(json.dumps(answer), encoding="utf-8")
    shelf = tmp_path / "shelf"
    shelf.mkdir()
    (shelf / "f.txt").write_text("\n".join(["Origen believed the devil would be freed", "and the church condemned him", "Origen taught much"]))
    return work, [{"id": "q1", "group": "B", "wording": "What did Origen teach?"}], shelf


def _reply(work, stage, key, text):
    (work / "unbound" / stage / "replies" / f"{key}.txt").write_text(text, encoding="utf-8")


def test_a_full_round(tmp_path, monkeypatch):
    work, questions, shelf = _setup(tmp_path)
    monkeypatch.setattr(tu, "shelf_files", lambda world: frozenset({"f.txt"}))
    rows = tu._answers(questions, work, load_world_records("lpc"))
    assert tu.classify_export(rows, work) == {"prompts_written": 4, "withheld_by_the_net": 1}
    _reply(work, "classify", "q1.0", '{"kind": "world_claim", "denies": null}')
    _reply(work, "classify", "q1.1", '{"kind": "world_claim", "denies": null}')
    _reply(work, "classify", "q1.2", '{"kind": "connective", "denies": null}')
    _reply(work, "classify", "q1.3", '{"kind": "limit", "denies": "what Origen taught or whether the church condemned him"}')
    result = tu.classify_import(rows, work)
    assert result == {"rows": 5, "missing_replies": 0, "unreadable": 0, "world_claim": 1, "to_shelf_check": 1, "withheld_by_the_net": 1}
    _reply(work, "terms", "q1.3", '{"terms": ["Origen", "devil", "condemned"]}')
    assert tu.terms_import(rows, work, shelf_root=shelf) == {"shelf_prompts_written": 1, "missing_replies": 0, "unreadable": 0}
    prompt = (work / "unbound" / "shelf" / "prompts" / "q1.3.md").read_text()
    assert "devil would be freed" in prompt and "f.txt" in prompt
    _reply(work, "shelf", "q1.3", '{"covered": true, "where": "f.txt 1-3", "reason": "states it"}')
    summary = tu.final(rows, work)
    assert summary["withhold"] == 1 and summary["withhold_net"] == 1 and summary["withhold_shelf"] == 1 and summary["keep"] == 2
    assert (work / "unbound" / "final" / "q1.txt").read_text() == "Bound claim. Here is what we can say."


def test_missing_replies_keep_their_sentences_and_are_counted(tmp_path, monkeypatch):
    work, questions, shelf = _setup(tmp_path)
    monkeypatch.setattr(tu, "shelf_files", lambda world: frozenset({"f.txt"}))
    rows = tu._answers(questions, work, load_world_records("lpc"))
    tu.classify_export(rows, work)
    _reply(work, "classify", "q1.3", '{"kind": "limit", "denies": "what Origen taught"}')
    assert tu.classify_import(rows, work)["missing_replies"] == 3
    assert tu.terms_import(rows, work, shelf_root=shelf)["missing_replies"] == 1
    summary = tu.final(rows, work)
    assert summary["pending_classify"] == 3 and summary["pending_shelf"] == 1
    assert "Nothing we carry speaks of him." in (work / "unbound" / "final" / "q1.txt").read_text()
