import json
import sqlite3

from engine.m3 import shown_check

GROUND = "- [[alx.dw.apostolic]] dw — a\n- [[alx.passage.0123456789ab]] passage (OUTSIDE OUR VOICE) — text\n"


def _request(work, key, ground_in_prompt, lines_in_system=3):
    pending = work / "pending"
    pending.mkdir(parents=True, exist_ok=True)
    system = pending / "system-x.txt"
    system.write_text("line\n" * lines_in_system, encoding="utf-8")
    request = {"kind": "voice", "reply_schema": None, "system_files": [str(system)], "messages": [{"role": "user", "text": GROUND}]}
    (pending / f"{key}.request.json").write_text(json.dumps(request), encoding="utf-8")
    (pending / f"{key}.prompt.txt").write_text(ground_in_prompt, encoding="utf-8")


def test_a_prompt_that_shows_every_offered_id_passes_and_reports_where_the_passage_sits(tmp_path):
    _request(tmp_path, "q001.voice.1", GROUND)
    result = shown_check.check_voice(tmp_path)[0]
    assert result["offered"] == 2 and result["missing"] == [] and result["too_long"] == []
    assert result["passage_positions"] == ["2 of 2"]


def test_an_offered_id_missing_from_the_prompt_file_fails(tmp_path):
    _request(tmp_path, "q001.voice.1", "- [[alx.dw.apostolic]] dw — a\n")
    assert shown_check.check_voice(tmp_path)[0]["missing"] == ["alx.passage.0123456789ab"]


def test_a_file_too_long_to_be_read_whole_fails(tmp_path):
    _request(tmp_path, "q001.voice.1", GROUND, lines_in_system=shown_check.MAX_LINES + 5)
    assert shown_check.check_voice(tmp_path)[0]["too_long"] == ["system-x.txt"]


def test_main_exits_1_when_a_request_fails_and_0_when_all_pass(tmp_path):
    _request(tmp_path, "q001.voice.1", "nothing")
    assert shown_check.main(["voice", "--work", str(tmp_path)]) == 1
    _request(tmp_path, "q001.voice.1", GROUND)
    assert shown_check.main(["voice", "--work", str(tmp_path)]) == 0


def test_a_rater_item_cut_short_of_the_whole_passage_fails(tmp_path):
    db = tmp_path / "i.sqlite"
    connection = sqlite3.connect(db)
    connection.execute("CREATE TABLE passages (passage_id TEXT, text TEXT)")
    connection.execute("INSERT INTO passages VALUES ('p1', 'one two three four five')")
    connection.commit()
    connection.close()
    items = [{"id": "a", "passage_id": "p1", "passage": "one two three four five"}, {"id": "b", "passage_id": "p1", "passage": "one two three"},
             {"id": "c", "passage_id": "gone", "passage": "x"}]
    failures = shown_check.check_items(items, db)
    assert [f["id"] for f in failures] == ["b", "c"]
