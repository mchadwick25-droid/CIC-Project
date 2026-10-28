"""What a reply is once apply_net has taken sentences out of the voice's draft.

The net removes only the sentences it withholds: a sentence that leans on a
removed one stays, and a reply that lost most of what it cited stands as the
net left it. A reply that is emptied or ungrounded is replaced by the world's
answer record, which reaches the participant word for word, its own quotation
marks untouched. A quote record whose rendering carries quotation marks is
set with each mark once. Fixture records only; no model call."""
import pytest

from engine.m4 import grounding_net
from engine.m4.grounding_net import quotable_rendering
from engine.m4.quote_placement import PlacementContext
from engine.m4.turn import _record_reply, apply_net, settle_reply

WITNESS = "fix.witness.pity"
WITNESS_TEXT = (
    'Augustine began with pity. He wrote of virgins taken captive. Some, he said, killed themselves "to avoid such disgrace." '
    '"Who that has any human feeling," he asked, "would refuse to forgive them?" Then he gave the hard teaching. '
    '"He who kills himself is a homicide," he wrote.'
)
OTHER = "fix.witness.other"
RECORDS = {
    "fix.figure.augustine": {"id": "fix.figure.augustine", "record_type": "figure", "names": [{"name": "Augustine", "tag": "in-world"}]},
    WITNESS: {"id": WITNESS, "record_type": "doctrinal_witness", "text": WITNESS_TEXT},
    OTHER: {"id": OTHER, "record_type": "doctrinal_witness", "text": "We kept the fast on the fourth day and on the Sabbath eve."},
    "fix.term.fast": {"id": "fix.term.fast", "record_type": "term", "term": "fast", "plain_meaning": "The fast is the meal not eaten."},
    "fix.quote.wrapped": {
        "id": "fix.quote.wrapped", "record_type": "quote", "speaker_or_author": "fix.figure.augustine",
        "modern_rendering": "“Lay this body anywhere. Do not let the care of it trouble you at all.”",
    },
    "fix.quote.inner": {
        "id": "fix.quote.inner", "record_type": "quote", "speaker_or_author": "fix.figure.augustine",
        "modern_rendering": "The outward act can be a form. So the sacraments can give “the form of godliness” without its power.",
    },
}
TYPED = 'He wrote, "the community kept a different memory of Jesus at the meal altogether" [[fix.witness.other]].'


def _net(raw, **kwargs):
    return apply_net(raw, repository_records=RECORDS, thin_topics=None, placement=PlacementContext(), **kwargs)


def _whys(net_result):
    return [r["why"] for r in net_result["reply_shape"]["removed"]]


# ---- a sentence that leans on a removed one stays ---------------------------


def test_a_sentence_that_points_back_at_a_removed_cited_sentence_stays():
    raw = f"We kept the fast [[{OTHER}]]. {TYPED} That is what we remember. We kept it still [[{OTHER}]]."
    text, _c, net_result = _net(raw)
    assert text == "We kept the fast. That is what we remember. We kept it still."
    assert _whys(net_result) == ["quotation typed by the voice"]


def test_a_run_of_sentences_after_a_removed_one_stays():
    raw = f"We kept the fast [[{OTHER}]]. {TYPED} That is what we remember. But it was not easy. We kept it still [[{OTHER}]]."
    text, _c, net_result = _net(raw)
    assert text == "We kept the fast. That is what we remember. But it was not easy. We kept it still."
    assert len(_whys(net_result)) == 1


def test_a_removal_by_placement_leaves_the_sentence_after_it():
    context = PlacementContext(offered=frozenset({"fix.quote.wrapped"}), voiced=frozenset({"fix.quote.wrapped"}))
    raw = f"We kept the fast [[{OTHER}]]. Augustine wrote of it [[{OTHER}]] [[quote:fix.quote.wrapped]]. That is what we remember. We kept it still [[{OTHER}]]."
    text, _c, _n = apply_net(raw, repository_records=RECORDS, thin_topics=None, placement=context)
    assert text == "We kept the fast. That is what we remember. We kept it still."


def test_a_sentence_after_a_failed_quote_marker_stays():
    text, _c, _n = _net(f"We kept the fast [[{OTHER}]]. Augustine wrote [[quote:fix.missing]]. That is what he meant.")
    assert text == "We kept the fast. That is what he meant."


# ---- the answer record reaches the participant word for word --------------


def _fallback(draft, offered=None):
    def net(text, **kwargs):
        return apply_net(text, repository_records=RECORDS, thin_topics=None, placement=PlacementContext(), **kwargs)

    text, _c, net_result = net(draft)
    return settle_reply(draft, text, net_result, {"doctrinal_witness": [WITNESS]} if offered is None else offered, RECORDS, net)


def test_the_answer_record_is_shown_whole_with_its_own_quotation_marks():
    settled = _fallback(f'"He who kills himself is a homicide," he wrote [[{WITNESS}]].')
    assert settled["answer_record_fallback"] == WITNESS
    assert settled["net_result"]["reply_shape"]["removed"] == [
        r for r in settled["net_result"]["reply_shape"]["removed"] if r["why"] == "quotation typed by the voice"
    ]
    assert settled["text"] == " ".join(WITNESS_TEXT.split())
    assert "Who that has any human feeling" in settled["text"]
    assert all(c["record_ids"] == [WITNESS] for c in settled["citations"])


def test_the_answer_record_placed_by_code_is_checked_against_the_record_word_for_word():
    record_text = _record_reply(RECORDS[WITNESS])
    _t, _c, net_result = _net(record_text, answer_record=WITNESS)
    assert all(s["verdict"] == "ok" and s.get("placed_answer") == WITNESS for s in net_result["sentences"])
    changed = record_text.replace("Augustine began with pity", "Augustine began with anger")
    text, _c, net_result = _net(changed, answer_record=WITNESS)
    assert "anger" not in text
    assert _whys(net_result)[0] == grounding_net.REASON_PLACED_MISMATCH


# ---- a reply that lost most of what it cited stands as the net left it ------


def test_a_reply_that_lost_two_fifths_of_its_cited_sentences_stands_as_the_net_left_it():
    draft = (
        f"Augustine began with pity [[{WITNESS}]]. He wrote of virgins taken captive [[{WITNESS}]]. "
        f'Some, he said, killed themselves "to avoid such disgrace" and more words besides [[{WITNESS}]]. '
        f'"Who that has any human feeling," he asked, "would refuse to forgive them?" [[{WITNESS}]] '
        f'"He who kills himself is a homicide," he wrote [[{WITNESS}]].'
    )
    settled = _fallback(draft)
    assert settled["answer_record_fallback"] is None
    assert settled["text"].startswith("Augustine began with pity. He wrote of virgins taken captive.")


def test_two_removals_among_three_cited_sentences_leave_the_rest_of_the_reply():
    raw = f"We kept the fast [[{OTHER}]]. {TYPED} {TYPED}"
    settled = _fallback(raw, offered={"doctrinal_witness": [OTHER]})
    assert settled["answer_record_fallback"] is None
    assert settled["text"] == "We kept the fast."


# ---- quotation marks in a rendering ---------------------------------------


def test_a_rendering_wrapped_in_quotation_marks_is_set_with_each_mark_once():
    context = PlacementContext(offered=frozenset({"fix.quote.wrapped"}))
    text, _c, net_result = apply_net(
        "Augustine wrote of his mother [[quote:fix.quote.wrapped]].", repository_records=RECORDS, thin_topics=None, placement=context,
    )
    assert net_result["reply_shape"]["placed"] == ["fix.quote.wrapped"]
    assert text == "Augustine wrote of his mother: “Lay this body anywhere. Do not let the care of it trouble you at all.”"
    assert "““" not in text and "””" not in text


def test_a_quotation_inside_a_rendering_takes_single_marks():
    context = PlacementContext(offered=frozenset({"fix.quote.inner"}))
    text, _c, net_result = apply_net(
        "Augustine wrote [[quote:fix.quote.inner]].", repository_records=RECORDS, thin_topics=None, placement=context,
    )
    assert net_result["reply_shape"]["placed"] == ["fix.quote.inner"]
    assert text == "Augustine wrote: “The outward act can be a form. So the sacraments can give ‘the form of godliness’ without its power.”"


@pytest.mark.parametrize("rendering, expected", [
    ("“One thing.”", "One thing."),
    ("“One thing.” And another “quoted” thing.", "‘One thing.’ And another ‘quoted’ thing."),
    ("A plain rendering, with the Lord’s name.", "A plain rendering, with the Lord’s name."),
    ('"Straight marks"', "Straight marks"),
    ("", ""),
])
def test_quotable_rendering(rendering, expected):
    assert quotable_rendering({"modern_rendering": rendering}) == expected


# ---- the answer record chosen for an emptied reply ----------------------------


def test_an_emptied_reply_still_falls_back_to_the_record_the_draft_cited_when_none_was_offered():
    typed = TYPED.replace(OTHER, WITNESS)
    settled = _fallback(f"{typed} {typed}", offered={})
    assert settled["answer_record_fallback"] == WITNESS


def test_with_no_offered_witness_the_answer_record_is_the_one_the_draft_cited_most():
    typed = TYPED.replace(OTHER, WITNESS)
    raw = f"{typed} We kept the fast [[{OTHER}]]. We kept it long [[{OTHER}]]. We kept it still [[{OTHER}]]."
    from engine.m4.turn import _answer_record_fallback
    assert _answer_record_fallback(raw, {}, RECORDS) == OTHER
    assert _answer_record_fallback(f"{typed} {typed} We kept the fast [[{OTHER}]].", {}, RECORDS) == WITNESS


def test_an_emptied_reply_is_replaced_by_the_offered_witness_the_draft_tagged_before_its_most_cited_one():
    typed_witness = TYPED.replace(OTHER, WITNESS)
    raw = f"{typed_witness} {typed_witness} {TYPED}"
    settled = _fallback(raw, offered={"doctrinal_witness": [OTHER]})
    assert settled["answer_record_fallback"] == OTHER

