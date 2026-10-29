"""Sentences a removal leaves without their referent are reported, and the text
stays as the net left it. Also: a witness's own words still stand, and a quote
record's words still go unless code placed them. Fixture records only; no model call."""
from engine.m4.orphan_guard import orphaned_sentences
from engine.m4.quote_placement import PlacementContext
from engine.m4.turn import apply_net

WITNESS = "fix.witness.keep"
OTHER = "fix.witness.other"
RECORDS = {
    "fix.figure.augustine": {"id": "fix.figure.augustine", "record_type": "figure", "names": [{"name": "Augustine", "tag": "in-world"}]},
    WITNESS: {
        "id": WITNESS, "record_type": "doctrinal_witness",
        "text": "We keep what was handed to us whole, and we add nothing to it of our own.",
    },
    OTHER: {"id": OTHER, "record_type": "doctrinal_witness", "text": "We kept the fast on the fourth day and on the Sabbath eve."},
    "fix.quote.rest": {
        "id": "fix.quote.rest", "record_type": "quote", "speaker_or_author": "fix.figure.augustine",
        "modern_rendering": "You made us for yourself, and our heart is restless until it rests in you.",
    },
}
TYPED = 'He wrote, "the community kept a different memory of Jesus at the meal altogether" [[fix.witness.other]].'


def _net(raw):
    return apply_net(raw, repository_records=RECORDS, thin_topics=None, placement=PlacementContext())


def test_a_paragraph_opening_pronoun_after_a_cut_is_reported_and_kept():
    raw = f"We kept the fast [[{OTHER}]].\n\n{TYPED} That is what we remember [[{OTHER}]]. We kept it still [[{OTHER}]]."
    text, _c, net_result = _net(raw)
    assert text == "We kept the fast.\n\nThat is what we remember. We kept it still."
    assert net_result["reply_shape"]["orphaned"] == ["That is what we remember."]


def test_a_pronoun_with_a_kept_sentence_before_it_in_its_paragraph_is_not_reported():
    raw = f"We kept the fast [[{OTHER}]]. {TYPED} That is what we remember [[{OTHER}]]. We kept it still [[{OTHER}]]."
    _t, _c, net_result = _net(raw)
    assert net_result["reply_shape"]["orphaned"] == []


def test_a_paragraph_opening_pronoun_with_nothing_cut_is_not_reported():
    raw = f"We kept the fast [[{OTHER}]].\n\nThat is what we remember [[{OTHER}]]."
    _t, _c, net_result = _net(raw)
    assert net_result["reply_shape"]["orphaned"] == []


def test_a_sentence_after_a_cut_that_opens_with_a_name_is_not_reported():
    raw = f"We kept the fast [[{OTHER}]].\n\n{TYPED} Augustine kept it too [[{OTHER}]]."
    _t, _c, net_result = _net(raw)
    assert net_result["reply_shape"]["orphaned"] == []


def test_the_report_lists_only_what_the_arguments_name():
    removed = [{"sentence": "Gone.", "draft": "Gone [[x]]."}]
    kept = [{"sentence": "He stayed.", "draft": "He stayed.", "verdict": "ok"}]
    assert orphaned_sentences("Gone [[x]].\n\nHe stayed.", removed, kept) == ["He stayed."]
    assert orphaned_sentences("Gone [[x]].\n\nHe stayed.", [], kept) == []


def test_a_witness_sentence_with_its_own_inline_words_survives():
    raw = f'The rule is plain: "keep what was handed to us whole" [[{WITNESS}]].'
    text, _c, net_result = _net(raw)
    assert "keep what was handed to us whole" in text
    assert net_result["reply_shape"]["removed"] == []


def test_a_sentence_giving_a_quote_records_words_without_placing_it_still_goes():
    raw = f"We keep the fast [[{OTHER}]]. You made us for yourself, and our heart is restless until it rests in you [[{OTHER}]]."
    text, _c, net_result = _net(raw)
    assert "restless" not in text
    assert [r["why"] for r in net_result["reply_shape"]["removed"]] == ["gives a quote record's words without placing it"]
