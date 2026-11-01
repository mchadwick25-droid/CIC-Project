"""The answer check: one read of the answer, one rewrite from what survives, abstain otherwise."""
import json

import pytest

from engine.m1.loader import load_world_records
from engine.m3 import test100_check as runner
from engine.m4 import answer_check as ac
from engine.m4 import bound_draft as bd

LIMIT = "lpc.limit.womens-own-voice"
WITNESS = "lpc.witness.days-before-the-sun"
QUOTE = "lpc.quote.love-and-do-what-thou-wilt"
CONNECTIVES = bd.connective_set(["Here is what we can say."])


@pytest.fixture(scope="module")
def records():
    return load_world_records("lpc")


def _unit(sentence, recs=(), placed_id=None):
    return {"sentence": sentence, "records": list(recs), "placed": bool(placed_id), "placed_id": placed_id, "tags": list(recs)}


def _answer():
    return [
        _unit("We keep to the older books on the first days.", [WITNESS]),
        _unit("No woman's own writing reaches us.", [LIMIT]),
        _unit("Love, and do what you will.", [QUOTE], QUOTE) | {"records": []},
        _unit("Here is what we can say."),
    ]


def test_one_request_per_answer_lists_sentences_with_their_bindings_and_each_record_once(records):
    request = ac.check_request("What did they say?", _answer(), records, {QUOTE: "Record: x\nThe passage: p"})
    user = request["user"]
    assert f"1. [bound to {WITNESS}]" in user and f"2. [bound to {LIMIT}]" in user
    assert f"3. [PLACED {QUOTE}]" in user and "4. [JOINING]" in user
    assert user.count(f"Record {WITNESS} [") == 1 and f"PLACED {QUOTE}\nRecord: x" in user
    assert "unresolved_referent" in request["system"] and "off_point" in request["system"]


def _reply(sentences, placed=()):
    return json.dumps({"sentences": sentences, "placed": list(placed)})


def test_the_reply_is_read_per_sentence_and_joining_or_placed_entries_are_ignored(records):
    answer = _answer()
    reply = _reply([
        {"n": 1, "supported": True, "problem": None, "reason": "ok"},
        {"n": 2, "supported": False, "problem": "widened_scope", "reason": "years"},
        {"n": 4, "supported": False, "problem": "other", "reason": "x"},
    ], [{"id": QUOTE, "fit": "off_point", "reason": "other question", "limit_stated": False}])
    parsed = ac.parse_check(reply, answer, records)
    assert parsed["sentences"][0]["supported"] and not parsed["sentences"][1]["supported"] and 3 not in parsed["sentences"]
    result = ac.outcome(answer, parsed, records)
    assert list(result["unsupported"]) == [1] and result["dropped"] == [QUOTE] and result["unreadable"] == 0


def test_a_sentence_or_placement_with_no_judgement_is_kept_and_counted(records):
    answer = _answer()
    parsed = ac.parse_check(_reply([{"n": 1, "supported": True, "problem": None, "reason": ""}]), answer, records)
    result = ac.outcome(answer, parsed, records)
    assert result["unsupported"] == {} and result["dropped"] == [] and result["unreadable"] == 2
    assert ac.parse_check("no object here", answer, records) is None


def test_the_confidence_cap_applies_to_a_read_sentence(records):
    answer = [_unit("We hold it at Widely Accepted.", ["lpc.gravity.collegial-communion-preserved", "lpc.witness.answerability-as-ground"])]
    parsed = ac.parse_check(_reply([{"n": 1, "supported": True, "problem": None, "reason": "ok"}]), answer, records)
    assert parsed["sentences"][0]["problem"] == "stronger_force"


def test_survivors_leave_out_unsupported_sentences_and_dropped_placements(records):
    answer = _answer()
    result = {"unsupported": {1: {}}, "dropped": [QUOTE], "unreadable": 0}
    assert [u["sentence"] for u in ac.survivors(answer, result)] == ["We keep to the older books on the first days.", "Here is what we can say."]
    request = ac.rewrite_request("Q?", answer, result, records)
    assert f"KEPT [bound to [[{WITNESS}]]" in request["user"] and "REMOVED No woman's own writing reaches us." in request["user"]


def test_a_rewrite_with_bindings_and_a_label_on_every_sentence_is_accepted(records):
    kept = ac.survivors(_answer(), {"unsupported": {1: {}}, "dropped": [], "unreadable": 0})
    reply = f"We keep to the older books on the first days [[{WITNESS}]] [[as:paraphrase]]. [[quote:{QUOTE}]] Here is what we can say."
    out = ac.parse_rewrite(reply, kept, records, CONNECTIVES)
    assert [u["sentence"] for u in out] == ["We keep to the older books on the first days.", "Love, and do what you will.", "Here is what we can say."]
    assert out[1]["placed_id"] == QUOTE and out[0]["records"] == [WITNESS]


@pytest.mark.parametrize("reply", [
    "", "A claim with no id.", f"A claim [[{WITNESS}]] [[as:inference]].", f"A claim [[{WITNESS}]].",
    f'He said "no" [[{WITNESS}]] [[as:paraphrase]].', f"[[quote:lpc.quote.never-kept]]",
    f"A claim [[{WITNESS}]] [[as:paraphrase]]. Then [[quote:lpc.quote.never-kept]].",
])
def test_a_rewrite_that_breaks_the_grammar_is_refused(records, reply):
    kept = ac.survivors(_answer(), {"unsupported": {1: {}}, "dropped": [QUOTE], "unreadable": 0})
    assert ac.parse_rewrite(reply, kept, records, CONNECTIVES) is None


def test_a_placement_that_was_dropped_cannot_come_back_in_the_rewrite(records):
    kept = ac.survivors(_answer(), {"unsupported": {}, "dropped": [QUOTE], "unreadable": 0})
    assert ac.parse_rewrite(f"[[quote:{QUOTE}]]", kept, records, CONNECTIVES) is None


def _work(tmp_path, status, **more):
    row = {"question_id": "q1", "status": status, "units": _answer(), "unsupported": {"1": {"supported": False, "problem": "other", "reason": ""}}, "dropped": []}
    (tmp_path / "check").mkdir(parents=True)
    (tmp_path / "check" / "read.jsonl").write_text(json.dumps(row) + "\n", encoding="utf-8")
    return row


def test_final_abstains_when_too_little_survives(tmp_path, records):
    _work(tmp_path, "too_little")
    summary = runner.final([({"id": "q1"}, _answer())], tmp_path, records)
    assert summary["abstained_too_little"] == 1
    assert (tmp_path / "check" / "final" / "q1.txt").read_text() == bd.FALLBACK_ALONE


def test_final_uses_an_accepted_rewrite_only_when_its_read_passes(tmp_path, records):
    row = _work(tmp_path, "rewrite")
    rewrite = [_unit("We keep to the older books on the first days.", [WITNESS])]
    (tmp_path / "check" / "rewrite.jsonl").write_text(json.dumps({**row, "rewrite": rewrite}) + "\n", encoding="utf-8")
    rows = [({"id": "q1"}, _answer())]
    assert runner.final(rows, tmp_path, records)["pending_reread"] == 1
    reread = tmp_path / "check" / "reread" / "replies"
    reread.mkdir(parents=True)
    (reread / "q1.txt").write_text(_reply([{"n": 1, "supported": True, "problem": None, "reason": ""}]), encoding="utf-8")
    assert runner.final(rows, tmp_path, records)["rewritten"] == 1
    assert (tmp_path / "check" / "final" / "q1.txt").read_text() == "We keep to the older books on the first days."
    (reread / "q1.txt").write_text("no object", encoding="utf-8")
    assert runner.final(rows, tmp_path, records)["abstained_rewrite_failed_read"] == 1
    (reread / "q1.txt").write_text(_reply([]), encoding="utf-8")
    assert runner.final(rows, tmp_path, records)["abstained_rewrite_failed_read"] == 1
    (reread / "q1.txt").write_text(_reply([{"n": 1, "supported": False, "problem": "other", "reason": ""}]), encoding="utf-8")
    summary = runner.final(rows, tmp_path, records)
    assert summary["abstained_rewrite_failed_read"] == 1
    assert (tmp_path / "check" / "final" / "q1.txt").read_text() == bd.FALLBACK_ALONE


def test_final_abstains_when_the_rewrite_was_refused(tmp_path, records):
    row = _work(tmp_path, "rewrite")
    (tmp_path / "check" / "rewrite.jsonl").write_text(json.dumps({**row, "rewrite": None}) + "\n", encoding="utf-8")
    assert runner.final([({"id": "q1"}, _answer())], tmp_path, records)["abstained_rewrite_refused"] == 1


def test_import_reads_each_answer_once_decides_its_status_and_writes_the_fit_rows(tmp_path, records):
    units = _answer()
    reply_dir = tmp_path / "check" / "read" / "replies"
    reply_dir.mkdir(parents=True)
    (reply_dir / "q1.txt").write_text(_reply(
        [{"n": 1, "supported": True, "problem": None, "reason": ""}, {"n": 2, "supported": False, "problem": "widened_scope", "reason": "years"}],
        [{"id": QUOTE, "fit": "off_point", "reason": "x", "limit_stated": False}],
    ), encoding="utf-8")
    summary = runner.import_read([({"id": "q1"}, units)], tmp_path, records)
    assert summary["answers"] == 1 and summary["too_little"] == 1 and "to_rewrite" not in summary
    fit = [json.loads(line) for line in (tmp_path / "check" / "fit.jsonl").read_text().splitlines()]
    assert fit[0]["record_id"] == QUOTE and fit[0]["decision"] == "drop"
    assert runner.import_read([({"id": "q2"}, units)], tmp_path, records)["pending_read"] == 1


def test_a_placed_story_comes_back_whole_in_the_rewrite(records):
    story = "lpc.story.numidicus"
    answer = [_unit("First story sentence.", [story], story), _unit("Second story sentence.", [story], story), _unit("A claim.", [WITNESS])]
    kept = ac.survivors(answer, {"unsupported": {2: {}}, "dropped": [], "unreadable": 0})
    out = ac.parse_rewrite(f"[[story:{story}]]", kept, records, CONNECTIVES)
    assert [u["sentence"] for u in out] == ["First story sentence.", "Second story sentence."]


def test_the_world_answer_record_is_not_judged_for_fit_and_a_story_is_judged_once(records):
    witness_id = "lpc.witness.days-before-the-sun"
    story = "lpc.story.numidicus"
    answer = [_unit("Answer record words.", [witness_id], witness_id), _unit("S one.", [story], story), _unit("S two.", [story], story)]
    parsed = {"sentences": {}, "placed": {story: {"fit": "off_point", "reason": "", "limit_stated": False}}}
    result = ac.outcome(answer, parsed, records)
    assert result["dropped"] == [story] and result["unreadable"] == 0


def test_a_lead_in_goes_with_the_quote_that_was_dropped(records):
    answer = [_unit("Our founder put it this way.", [QUOTE]), _unit("Love, and do what you will.", [QUOTE], QUOTE), _unit("A claim.", [WITNESS])]
    kept = ac.survivors(answer, {"unsupported": {}, "dropped": [QUOTE], "unreadable": 0})
    assert [u["sentence"] for u in kept] == ["A claim."]


def test_a_rewrite_that_states_an_absence_its_records_do_not_is_refused(records):
    kept = [_unit("We keep to the older books.", [LIMIT])]
    assert ac.parse_rewrite(f"We have no sermon of our own on those opening lines [[{LIMIT}]] [[as:paraphrase]].", kept, records, CONNECTIVES) is None


def test_a_rewrite_that_keeps_a_placement_is_read_without_asking_about_it_again(tmp_path, records):
    row = _work(tmp_path, "rewrite")
    rewrite = [_unit("We keep to the older books on the first days.", [WITNESS]), _unit("Love, and do what you will.", [], QUOTE)]
    (tmp_path / "check" / "rewrite.jsonl").write_text(json.dumps({**row, "rewrite": rewrite}) + "\n", encoding="utf-8")
    reread = tmp_path / "check" / "reread" / "replies"
    reread.mkdir(parents=True)
    (reread / "q1.txt").write_text(_reply([{"n": 1, "supported": True, "problem": None, "reason": ""}], []), encoding="utf-8")
    summary = runner.final([({"id": "q1"}, _answer())], tmp_path, records)
    assert summary["rewritten"] == 1 and "abstained_rewrite_failed_read" not in summary


def test_the_rewrite_request_teaches_the_tag_form_and_shows_ids_in_it(records):
    request = ac.rewrite_request("Q?", _answer(), {"unsupported": {1: {}}, "dropped": [], "unreadable": 0}, records)
    assert "double square brackets" in request["system"] and "[[lpc.witness.example]]" in request["system"]
    assert f"KEPT [bound to [[{WITNESS}]]]" in request["user"]
