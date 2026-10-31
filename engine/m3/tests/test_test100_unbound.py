"""The unbound runner: prompts out, replies in, a final text and a count."""
import json

from engine.m1.loader import load_world_records
from engine.m3 import test100_unbound as tu
from engine.m4 import unbound_step as us

LIMIT = "lpc.limit.womens-own-voice"
STATED = "From our own two cities, in our years from 246 to 430, no text a woman wrote herself survives."


def _setup(tmp_path, limit_sentence="Nothing we carry speaks of him.", limit_tags=()):
    work = tmp_path / "run"
    (work / "answers").mkdir(parents=True)
    sentences = ["Bound claim.", "A fact with no citation.", "Here is what we can say.", limit_sentence, "Withheld one."]
    answer = {"text": " ".join(sentences), "net_sentences": [
        {"sentence": sentences[0], "tags": [LIMIT], "verdict": "ok"},
        {"sentence": sentences[1], "tags": [], "verdict": "ok"},
        {"sentence": sentences[2], "tags": [], "verdict": "ok"},
        {"sentence": sentences[3], "tags": list(limit_tags), "verdict": "ok"},
        {"sentence": sentences[4], "tags": [], "verdict": "withhold", "why": "x"},
    ], "reply_shape": {"placed": []}}
    (work / "answers" / "q1.json").write_text(json.dumps(answer), encoding="utf-8")
    return work, [{"id": "q1", "group": "B", "wording": "What did Origen teach?"}]


def _reply(work, key, text):
    (work / "unbound" / "classify" / "replies" / f"{key}.txt").write_text(text, encoding="utf-8")


def _classify(work, kinds):
    for n, kind in enumerate(kinds):
        _reply(work, f"q1.{n}", json.dumps({"kind": kind}))


def test_an_unbound_limit_is_withheld_and_the_fallback_stands_in_its_place(tmp_path):
    work, questions = _setup(tmp_path)
    records = load_world_records("lpc")
    rows = tu._answers(questions, work, records)
    assert tu.classify_export(rows, work) == {"prompts_written": 4, "withheld_by_the_net": 1}
    _classify(work, ["world_claim", "world_claim", "connective", "limit"])
    assert tu.classify_import(rows, work, records) == {
        "rows": 5, "missing_replies": 0, "unreadable": 0, "world_claim": 1, "limit_not_stated_by_a_record": 1, "talks_of_tags": 0, "withheld_by_the_net": 1}
    summary = tu.final(rows, work, records)
    assert summary["withhold"] == 1 and summary["withhold_net"] == 1 and summary["withhold_limit"] == 1 and summary["fallback_added"] == 1
    assert (work / "unbound" / "final" / "q1.txt").read_text() == f"Bound claim. Here is what we can say. {us.LIMIT_FALLBACK_ALONE}"


def test_a_limit_a_record_states_is_kept_and_no_fallback_is_added(tmp_path):
    work, questions = _setup(tmp_path, STATED, [LIMIT])
    records = load_world_records("lpc")
    rows = tu._answers(questions, work, records)
    tu.classify_export(rows, work)
    _classify(work, ["world_claim", "world_claim", "connective", "limit"])
    tu.classify_import(rows, work, records)
    summary = tu.final(rows, work, records)
    assert summary["keep"] == 3 and "withhold_limit" not in summary and "fallback_added" not in summary
    assert (work / "unbound" / "final" / "q1.txt").read_text() == f"Bound claim. Here is what we can say. {STATED}"


def test_a_withheld_limit_does_not_add_the_fallback_when_a_stated_limit_remains(tmp_path):
    work, questions = _setup(tmp_path)
    records = load_world_records("lpc")
    answer = json.loads((work / "answers" / "q1.json").read_text())
    answer["net_sentences"][0] = {"sentence": STATED, "tags": [LIMIT], "verdict": "ok"}
    answer["text"] = answer["text"].replace("Bound claim.", STATED)
    (work / "answers" / "q1.json").write_text(json.dumps(answer))
    rows = tu._answers(questions, work, records)
    tu.classify_export(rows, work)
    _classify(work, ["limit", "world_claim", "connective", "limit"])
    tu.classify_import(rows, work, records)
    summary = tu.final(rows, work, records)
    assert "fallback_added" not in summary and summary["withhold_limit"] == 1
    assert (work / "unbound" / "final" / "q1.txt").read_text() == f"{STATED} Here is what we can say."


def test_missing_replies_keep_their_sentences_and_are_counted(tmp_path):
    work, questions = _setup(tmp_path)
    records = load_world_records("lpc")
    rows = tu._answers(questions, work, records)
    tu.classify_export(rows, work)
    _reply(work, "q1.3", '{"kind": "limit"}')
    assert tu.classify_import(rows, work, records)["missing_replies"] == 3
    summary = tu.final(rows, work, records)
    assert summary["pending_classify"] == 3
    assert "Nothing we carry speaks of him." not in (work / "unbound" / "final" / "q1.txt").read_text()


def test_a_sentence_the_verify_step_rewrote_and_used_is_classified_too(tmp_path):
    work, questions = _setup(tmp_path)
    (work / "verify" / "reread" / "replies").mkdir(parents=True)
    row = {"key": "q1.0", "question_id": "q1", "n": 0, "rewrite": "Our record is silent on it.", "bound": [LIMIT]}
    (work / "verify" / "rewrite.jsonl").write_text(json.dumps(row) + "\n")
    (work / "verify" / "reread" / "replies" / "q1.0.txt").write_text('{"supported": true, "problem": null, "reason": ""}')
    items = tu._answers(questions, work, load_world_records("lpc"))[0][2]
    assert [i["n"] for i in items][-1] == "0r" and items[-1]["sentence"] == "Our record is silent on it."
    assert items[-1]["records"] == [LIMIT]


def _verify_text(work, text):
    (work / "verify" / "final").mkdir(parents=True)
    (work / "verify" / "final" / "q1.txt").write_text(text, encoding="utf-8")


def _run(tmp_path, tags, sentences, verify_text, kinds):
    work, questions = _setup(tmp_path)
    answer = {"text": " ".join(sentences), "net_sentences": [{"sentence": s, "tags": list(t), "verdict": "ok"} for s, t in zip(sentences, tags)],
              "reply_shape": {"placed": []}}
    (work / "answers" / "q1.json").write_text(json.dumps(answer))
    if verify_text is not None:
        _verify_text(work, verify_text)
    records = load_world_records("lpc")
    rows = tu._answers(questions, work, records)
    tu.classify_export(rows, work)
    for n, kind in enumerate(kinds):
        _reply(work, f"q1.{n}", json.dumps({"kind": kind}))
    tu.classify_import(rows, work, records)
    return work, tu.final(rows, work, records)


def test_a_limit_the_verify_step_removed_is_not_read_and_the_fallback_still_lands(tmp_path):
    work, summary = _run(tmp_path, [[LIMIT], ()], ["Bound claim.", "Nothing we carry speaks of him."], "Bound claim. Nothing we carry speaks of him.",
                         ["world_claim", "limit"])
    assert (work / "unbound" / "final" / "q1.txt").read_text() == f"Bound claim. {us.LIMIT_FALLBACK_ALONE}"
    assert summary["fallback_added"] == 1


def test_a_kept_limit_that_no_longer_stands_in_the_text_does_not_stop_the_fallback(tmp_path):
    work, summary = _run(tmp_path, [[LIMIT], (), ()], [STATED, "Nothing we carry speaks of him.", "Bound claim."],
                         "Nothing we carry speaks of him. Bound claim.", ["limit", "limit", "connective"])
    assert (work / "unbound" / "final" / "q1.txt").read_text() == f"{us.LIMIT_FALLBACK} Bound claim."


def test_the_fallback_stands_where_the_first_withheld_limit_stands_in_the_text(tmp_path):
    work, _ = _run(tmp_path, [(), (), ()], ["Nothing we carry speaks of him.", "Bound claim.", "We have no more on it."],
                   "We have no more on it. Bound claim. Nothing we carry speaks of him.", ["limit", "connective", "limit"])
    assert (work / "unbound" / "final" / "q1.txt").read_text() == f"{us.LIMIT_FALLBACK} Bound claim."


def test_a_withheld_limit_that_reads_like_the_fallback_does_not_eat_it(tmp_path):
    work, _ = _run(tmp_path, [(), ()], ["Nothing we carry speaks of him.", "We do not have that here."],
                   "Nothing we carry speaks of him. We do not have that here.", ["limit", "limit"])
    assert (work / "unbound" / "final" / "q1.txt").read_text() == us.LIMIT_FALLBACK_ALONE


def test_no_fallback_is_added_while_a_reply_for_the_answer_is_missing(tmp_path):
    work, questions = _setup(tmp_path)
    records = load_world_records("lpc")
    rows = tu._answers(questions, work, records)
    tu.classify_export(rows, work)
    _reply(work, "q1.0", '{"kind": "world_claim"}')
    _reply(work, "q1.1", '{"kind": "world_claim"}')
    _reply(work, "q1.3", '{"kind": "limit"}')
    tu.classify_import(rows, work, records)
    summary = tu.final(rows, work, records)
    assert "fallback_added" not in summary and summary["pending_classify"] == 1


def test_the_same_withheld_limit_twice_is_removed_both_times_and_the_fallback_stands_once(tmp_path):
    work, summary = _run(tmp_path, [(), (), ()], ["Nothing we carry speaks of him.", "Bound claim.", "Nothing we carry speaks of him."],
                         "Nothing we carry speaks of him. Bound claim. Nothing we carry speaks of him.", ["limit", "connective", "limit"])
    assert (work / "unbound" / "final" / "q1.txt").read_text() == f"{us.LIMIT_FALLBACK} Bound claim."


LONG = " ".join(["The council met and the bishops spoke in turn about the lapsed and the road back to the church."] * 3)


def test_a_long_answer_loses_a_withheld_limit_without_a_fallback(tmp_path):
    work, summary = _run(tmp_path, [[LIMIT], (), ()], [LONG, "Nothing we carry speaks of him.", "Here is what we can say."], None,
                         ["world_claim", "limit", "connective"])
    assert (work / "unbound" / "final" / "q1.txt").read_text() == f"{LONG} Here is what we can say."
    assert "fallback_added" not in summary


def test_the_fallback_that_leads_into_more_text_says_what_follows(tmp_path):
    work, _ = _run(tmp_path, [(), [LIMIT]], ["Nothing we carry speaks of him.", "Bound claim."], None, ["limit", "world_claim"])
    assert (work / "unbound" / "final" / "q1.txt").read_text() == f"{us.LIMIT_FALLBACK} Bound claim."


def test_a_sentence_that_names_a_confidence_level_is_withheld(tmp_path):
    work, summary = _run(tmp_path, [[LIMIT], [LIMIT]], [LONG, "We hold it at Widely Accepted."], None, ["world_claim", "world_claim"])
    assert (work / "unbound" / "final" / "q1.txt").read_text() == LONG
    assert summary["withhold_tags"] == 1


def _bind_run(tmp_path, bind_reply, check_reply):
    work, questions = _setup(tmp_path, "Another fact.")
    answer = json.loads((work / "answers" / "q1.json").read_text())
    answer["offered"] = [LIMIT, "lpc.witness.days-before-the-sun"]
    (work / "answers" / "q1.json").write_text(json.dumps(answer))
    records = load_world_records("lpc")
    rows = tu._answers(questions, work, records)
    tu.classify_export(rows, work)
    _classify(work, ["world_claim", "world_claim", "connective", "world_claim"])
    tu.classify_import(rows, work, records)
    (work / "unbound" / "bind" / "replies" / "q1.1.txt").write_text(bind_reply)
    (work / "unbound" / "bind" / "replies" / "q1.3.txt").write_text('{"action": "none", "record": null, "sentence": null}')
    result = tu.bind_import(rows, work, records)
    if check_reply is not None:
        (work / "unbound" / "bindcheck" / "replies" / "q1.1.txt").write_text(check_reply)
    return work, result, tu.final(rows, work, records)


def test_an_unbound_claim_is_bound_to_the_record_that_states_it_and_stays(tmp_path):
    reply = json.dumps({"action": "bind", "record": "lpc.witness.days-before-the-sun", "sentence": None})
    work, result, summary = _bind_run(tmp_path, reply, '{"supported": true, "problem": null, "reason": "ok"}')
    assert result == {"candidates": 2, "missing_replies": 0, "unreadable": 0, "bound_or_repaired": 1, "bound": 1, "repaired": 0}
    assert summary["bound_kept"] == 1 and summary["withhold"] == 1
    assert (work / "unbound" / "final" / "q1.txt").read_text() == "Bound claim. A fact with no citation. Here is what we can say."


def test_an_unbound_claim_is_repaired_to_the_scope_the_record_carries(tmp_path):
    reply = json.dumps({"action": "repair", "record": "lpc.witness.days-before-the-sun", "sentence": "Augustine wrote that the days came before the sun."})
    work, _result, summary = _bind_run(tmp_path, reply, '{"supported": true, "problem": null, "reason": "ok"}')
    assert summary["repaired_kept"] == 1
    assert (work / "unbound" / "final" / "q1.txt").read_text() == "Bound claim. Augustine wrote that the days came before the sun. Here is what we can say."


def test_a_bound_claim_the_read_finds_unsupported_is_withheld_after_all(tmp_path):
    reply = json.dumps({"action": "bind", "record": "lpc.witness.days-before-the-sun", "sentence": None})
    work, _result, summary = _bind_run(tmp_path, reply, '{"supported": false, "problem": "added_detail", "reason": "x"}')
    assert "bound_kept" not in summary and summary["withhold"] == 2
    assert (work / "unbound" / "final" / "q1.txt").read_text() == "Bound claim. Here is what we can say."


def test_no_support_leaves_the_claim_withheld(tmp_path):
    work, result, summary = _bind_run(tmp_path, '{"action": "none", "record": null, "sentence": null}', None)
    assert result["bound_or_repaired"] == 0 and summary["withhold"] == 2


def test_a_bound_limit_that_stays_stops_the_fallback_for_a_withheld_one(tmp_path):
    work, questions = _setup(tmp_path)
    answer = {"text": f"{STATED} Nothing we carry speaks of him.", "offered": [LIMIT],
              "net_sentences": [{"sentence": STATED, "tags": [], "verdict": "ok"}, {"sentence": "Nothing we carry speaks of him.", "tags": [], "verdict": "ok"}],
              "reply_shape": {"placed": []}}
    (work / "answers" / "q1.json").write_text(json.dumps(answer))
    records = load_world_records("lpc")
    rows = tu._answers(questions, work, records)
    tu.classify_export(rows, work)
    _classify(work, ["limit", "limit"])
    tu.classify_import(rows, work, records)
    (work / "unbound" / "bind" / "replies" / "q1.0.txt").write_text(json.dumps({"action": "bind", "record": LIMIT, "sentence": None}))
    (work / "unbound" / "bind" / "replies" / "q1.1.txt").write_text('{"action": "none", "record": null, "sentence": null}')
    tu.bind_import(rows, work, records)
    (work / "unbound" / "bindcheck" / "replies" / "q1.0.txt").write_text('{"supported": true, "problem": null, "reason": "ok"}')
    summary = tu.final(rows, work, records)
    assert "fallback_added" not in summary and (work / "unbound" / "final" / "q1.txt").read_text() == STATED


def test_the_bindcheck_prompt_shows_the_sentence_before_it(tmp_path):
    work, questions = _setup(tmp_path, "Another fact.")
    answer = json.loads((work / "answers" / "q1.json").read_text())
    answer["offered"] = [LIMIT, "lpc.witness.days-before-the-sun"]
    (work / "answers" / "q1.json").write_text(json.dumps(answer))
    records = load_world_records("lpc")
    rows = tu._answers(questions, work, records)
    tu.classify_export(rows, work)
    _classify(work, ["world_claim", "world_claim", "connective", "world_claim"])
    tu.classify_import(rows, work, records)
    (work / "unbound" / "bind" / "replies" / "q1.1.txt").write_text(json.dumps({"action": "bind", "record": "lpc.witness.days-before-the-sun", "sentence": None}))
    (work / "unbound" / "bind" / "replies" / "q1.3.txt").write_text('{"action": "none", "record": null, "sentence": null}')
    tu.bind_import(rows, work, records)
    prompt = (work / "unbound" / "bindcheck" / "prompts" / "q1.1.md").read_text()
    assert "SENTENCE BEFORE IT" in prompt and "Bound claim." in prompt


def test_an_unreadable_bindcheck_keeps_the_sentence_and_withholds_the_fallback(tmp_path):
    work, _result, summary = _bind_run(tmp_path, json.dumps({"action": "bind", "record": "lpc.witness.days-before-the-sun", "sentence": None}), "garbage")
    assert summary["unreadable"] == 1 and "fallback_added" not in summary
