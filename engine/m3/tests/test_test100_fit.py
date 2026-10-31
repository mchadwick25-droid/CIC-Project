import json

from engine.m3.test100_fit import export, import_replies, placed_items

RECORDS = {
    "t.story.one": {"id": "t.story.one", "record_type": "story", "telling": "Full.", "telling_short": "Short.", "use_note": {"means": "m", "not_for": []}},
    "t.quote.one": {"id": "t.quote.one", "record_type": "quote", "modern_rendering": "Spoken.", "use_note": {"means": "m", "not_for": []}},
    "t.witness.one": {"id": "t.witness.one", "record_type": "doctrinal_witness"},
}
QUESTION = {"id": "q001", "group": "B", "wording": "What did he say?"}


def _answers(tmp_path):
    answers = tmp_path / "answers"
    answers.mkdir()
    (answers / "q001.json").write_text(json.dumps({
        "text": "He said so.",
        "reply_shape": {"placed": ["t.story.one", "t.quote.one", "t.witness.one", "t.gone.one"], "story_lengths": {"t.story.one": "short"}},
    }))
    return answers


def test_only_placed_quotes_and_stories_are_judged_at_the_length_told(tmp_path):
    items = placed_items([QUESTION, {"id": "q002", "group": "B", "wording": "x"}], _answers(tmp_path), RECORDS, tmp_path)
    assert [(i["key"], i["length"]) for i in items] == [("q001.t.story.one", "short"), ("q001.t.quote.one", None)]
    assert "Short." in items[0]["request"]["user"] and "What did he say?" in items[0]["request"]["user"]


def test_export_writes_one_prompt_per_item_and_import_reads_the_replies(tmp_path):
    items = placed_items([QUESTION], _answers(tmp_path), RECORDS, tmp_path)
    assert export(items, tmp_path) == 2
    assert (tmp_path / "fit" / "prompts" / "q001.t.story.one.md").read_text().startswith("SYSTEM\n")
    (tmp_path / "fit" / "replies" / "q001.t.story.one.txt").write_text('{"fit": "off_point", "reason": "x", "limit_stated": false}')
    (tmp_path / "fit" / "replies" / "q001.t.quote.one.txt").write_text("unreadable")
    rows = import_replies(items, tmp_path)
    assert [(r["record_id"], r["decision"]) for r in rows] == [("t.story.one", "drop"), ("t.quote.one", "keep")]
    assert rows[1]["judgement"] is None
