"""The verify runner: prompts out, replies in, a final text and a count."""
import json

from engine.m1.loader import load_world_records
from engine.m3 import test100_verify as tv

LIMIT = "lpc.limit.womens-own-voice"
GOOD = "Women reach us in men's words."
BAD = "No text a woman wrote survives."
HELD = "A claim with only a context tag."


def _setup(tmp_path):
    work = tmp_path / "run"
    (work / "answers").mkdir(parents=True)
    answer = {
        "text": f"{GOOD} {BAD}\n\n{HELD}",
        "net_sentences": [
            {"sentence": GOOD, "tags": [LIMIT], "verdict": "ok"},
            {"sentence": BAD, "tags": [LIMIT], "verdict": "ok"},
            {"sentence": HELD, "tags": ["ctx.x.1"], "verdict": "ok"},
        ],
        "reply_shape": {"placed": []},
    }
    (work / "answers" / "q1.json").write_text(json.dumps(answer), encoding="utf-8")
    return work, [{"id": "q1", "group": "B", "wording": "Did women write?"}]


def _reply(work, stage, key, text):
    (work / "verify" / stage / "replies" / f"{key}.txt").write_text(text, encoding="utf-8")


def test_a_full_round(tmp_path):
    work, questions = _setup(tmp_path)
    records = load_world_records("lpc")
    rows = tv._answers(questions, work, records)
    assert tv.export(rows, work, records) == {"prompts_written": 2, "held_out_no_valid_binding": 1}
    _reply(work, "read", "q1.0", '{"supported": true, "problem": null, "reason": "ok"}')
    _reply(work, "read", "q1.1", '{"supported": false, "problem": "dropped_scope", "reason": "years dropped"}')
    assert tv.import_read(rows, work, records) == {"rows": 3, "unreadable": 0, "to_rewrite": 1, "held_out": 1}
    assert (work / "verify" / "rewrite" / "prompts" / "q1.1.md").exists()
    _reply(work, "rewrite", "q1.1", "In our years, no text a woman wrote survives.")
    assert tv.import_rewrite(work, records) == {"rewrites": 1, "refused_or_dropped": 0, "to_reread": 1}
    _reply(work, "reread", "q1.1", '{"supported": true, "problem": null, "reason": "ok"}')
    summary = tv.final(rows, work)
    assert summary["kept"] == 1 and summary["rewritten_kept"] == 1 and summary["held_out"] == 1 and summary["problems"] == {"dropped_scope": 1}
    assert (work / "verify" / "final" / "q1.txt").read_text() == f"{GOOD} In our years, no text a woman wrote survives."


def test_a_rewrite_still_unsupported_is_taken_out(tmp_path):
    work, questions = _setup(tmp_path)
    records = load_world_records("lpc")
    rows = tv._answers(questions, work, records)
    tv.export(rows, work, records)
    _reply(work, "read", "q1.0", '{"supported": true, "problem": null, "reason": ""}')
    _reply(work, "read", "q1.1", '{"supported": false, "problem": "added_detail", "reason": "x"}')
    tv.import_read(rows, work, records)
    _reply(work, "rewrite", "q1.1", "Still too much.")
    tv.import_rewrite(work, records)
    _reply(work, "reread", "q1.1", '{"supported": false, "problem": "added_detail", "reason": "x"}')
    summary = tv.final(rows, work)
    assert summary["taken_out"] == 1
    assert (work / "verify" / "final" / "q1.txt").read_text() == GOOD
