"""Bound drafting: what is decided from the draft itself, with no model call."""
from engine.m3.test100_bound import final_text
from engine.m4 import bound_draft as bd
from engine.m4 import grounding_net

RECORDS = {
    "w.witness.a": {"id": "w.witness.a", "record_type": "doctrinal_witness", "text": "We kept the creed first."},
    "w.limit.b": {"id": "w.limit.b", "record_type": "honest_limit", "statement": "We have no list of his letters."},
    "w.search.c": {"id": "w.search.c", "record_type": "search_record"},
}
CONNECTIVES = bd.connective_set(["Here is what we can say."])


def _entry(sentence, tags=(), verdict="ok", **more):
    return {"sentence": sentence, "tags": list(tags), "verdict": verdict, **more}


def test_marker_comes_off_the_spoken_text_and_is_read_as_the_label():
    parsed = grounding_net.parse_tagged("We kept the creed first [[w.witness.a]] [[as:paraphrase]].")
    assert parsed[0]["text"] == "We kept the creed first." and parsed[0]["tags"] == ["w.witness.a"]
    assert bd.label_of(parsed[0]["raw"]) == "paraphrase" and bd.label_of("no marker") is None


def test_a_bound_paraphrase_goes_on_to_verify_and_an_inference_never_ships():
    assert bd.decide(_entry("They kept it.", ["w.witness.a"]), "paraphrase", RECORDS, CONNECTIVES)[0] == "keep"
    assert bd.decide(_entry("They kept it.", ["w.witness.a"]), None, RECORDS, CONNECTIVES)[0] == "withhold_unlabelled"
    assert bd.decide(_entry("So it was trust.", ["w.witness.a"]), "inference", RECORDS, CONNECTIVES)[0] == "withhold_inference"


def test_no_binding_ships_only_as_a_question_or_a_reviewed_connective():
    assert bd.decide(_entry("Here is what we can say."), None, RECORDS, CONNECTIVES)[0] == "keep"
    assert bd.decide(_entry("here is what we can say"), None, RECORDS, CONNECTIVES)[0] == "keep"
    assert bd.decide(_entry("Would you like to hear more?"), None, RECORDS, CONNECTIVES)[0] == "keep"
    assert bd.decide(_entry("Nothing we carry speaks of him."), None, RECORDS, CONNECTIVES)[0] == "withhold_unbound"
    assert bd.decide(_entry("They kept it.", ["ctx.w.witness.a.1"]), "paraphrase", RECORDS, CONNECTIVES)[0] == "withhold_unbound"
    assert bd.decide(_entry("They kept it.", ["w.unknown.x"]), "paraphrase", RECORDS, CONNECTIVES)[0] == "withhold_unbound"
    assert bd.decide(_entry("They kept it.", ["w.search.c"]), "paraphrase", RECORDS, CONNECTIVES)[0] == "withhold_unbound"


def test_a_limit_sentence_bound_to_a_limit_record_is_judged_not_withheld_here():
    assert bd.decide(_entry("We have no list of his letters.", ["w.limit.b"]), "paraphrase", RECORDS, CONNECTIVES)[0] == "keep"


def test_talk_of_confidence_tags_is_withheld_and_net_withholds_stay_out():
    assert bd.decide(_entry("This is Widely Accepted among us.", ["w.witness.a"]), "paraphrase", RECORDS, CONNECTIVES)[0] == "withhold_tags"
    assert bd.decide(_entry("x", verdict="withhold", why="typed quotation"), None, RECORDS, CONNECTIVES)[0] == "withhold_net"


def test_items_read_the_label_from_each_sentences_own_draft():
    answer = {"net_sentences": [
        _entry("One.", ["w.witness.a"], draft="One [[w.witness.a]] [[as:paraphrase]]."),
        _entry("Two.", ["w.witness.a"], draft="Two [[w.witness.a]] [[as:inference]]."),
        _entry("Three.", ["w.witness.a"]),
    ]}
    rows = bd.items(answer, RECORDS, CONNECTIVES)
    assert [(r["n"], r["label"], r["decision"]) for r in rows] == [(0, "paraphrase", "keep"), (1, "inference", "withhold_inference"), (2, None, "withhold_unlabelled")]


def test_final_text_takes_withheld_sentences_out_and_keeps_the_rest():
    rows = [{"sentence": "Two sentences remain here and they are long enough to stand on their own as an answer, said plainly, with a few more words added so that the whole answer clears the floor of twenty five words.", "decision": "keep"},
            {"sentence": "Out.", "decision": "withhold_unbound"}]
    text, fallback = final_text("Two sentences remain here and they are long enough to stand on their own as an answer, said plainly, with a few more words added so that the whole answer clears the floor of twenty five words. Out.", rows)
    assert "Out." not in text and not fallback


def test_a_sentence_the_net_withheld_but_left_in_the_text_comes_out():
    rows = [{"sentence": "Macrina founded Annisa in 356.", "decision": "withhold_net"}, {"sentence": "Kept.", "decision": "keep"}]
    text, _fallback = final_text("Macrina founded Annisa in 356. Kept.", rows)
    assert "Macrina" not in text


def test_the_fallback_is_not_reported_when_the_first_sentence_cannot_be_found():
    rows = [{"sentence": "Gone.", "decision": "withhold_unbound"}]
    text, fallback = final_text('He said "Gone." Short.', rows)
    assert not fallback and bd.FALLBACK not in text and bd.FALLBACK_ALONE not in text


def test_an_identical_kept_sentence_is_not_removed_with_a_withheld_one():
    rows = [{"sentence": "Same.", "decision": "withhold_unbound"}, {"sentence": "Same.", "decision": "keep"}]
    text, _fallback = final_text("Same. Other words here. Same.", rows)
    assert text.count("Same.") >= 1


def test_the_fallback_stands_where_the_first_withheld_sentence_stood_when_too_little_is_left():
    rows = [{"sentence": "Nothing survives.", "decision": "withhold_unbound"}, {"sentence": "Short.", "decision": "keep"}]
    text, fallback = final_text("Nothing survives. Short.", rows)
    assert fallback and text == f"{bd.FALLBACK} Short."
    alone, fallback_alone = final_text("Nothing survives.", rows[:1])
    assert fallback_alone and alone == bd.FALLBACK_ALONE


def test_the_directive_lists_the_reviewed_connectives():
    lines = " ".join(bd.directive_lines(["Here is what we can say."]))
    assert '"Here is what we can say."' in lines and "[[as:paraphrase]]" in lines
    assert "none" in " ".join(bd.directive_lines([]))
