"""What a reply is once apply_net has taken sentences out of the voice's draft.

A removed sentence that cites a record takes with it the sentences just after
it that lean on it; a reply that lost HOLLOWED_SHARE or more of the cited
sentences it carried is replaced by the world's answer record; and that
record reaches the participant word for word, its own quotation marks
untouched. A quote record whose rendering carries quotation marks is set
with each mark once. Fixture records only; no model call."""
import pytest

from engine.m4 import grounding_net
from engine.m4.grounding_net import REASON_FOLLOWS_REMOVAL, leans_on_previous, quotable_rendering
from engine.m4.quote_placement import PlacementContext
from engine.m4.turn import HOLLOWED_SHARE, _hollowed, _record_reply, apply_net, settle_reply

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


# ---- sentences that lean on a removed one ---------------------------------


def test_a_sentence_that_points_back_at_a_removed_cited_sentence_goes_with_it():
    raw = f"We kept the fast [[{OTHER}]]. {TYPED} That is what we remember. We kept it still [[{OTHER}]]."
    text, _c, net_result = _net(raw)
    assert text == "We kept the fast. We kept it still."
    assert _whys(net_result) == ["quotation typed by the voice", REASON_FOLLOWS_REMOVAL]


def test_a_run_of_leaning_sentences_goes_until_one_that_stands():
    raw = f"We kept the fast [[{OTHER}]]. {TYPED} That is what we remember. But it was not easy. We kept it still [[{OTHER}]]."
    text, _c, net_result = _net(raw)
    assert text == "We kept the fast. We kept it still."
    assert _whys(net_result).count(REASON_FOLLOWS_REMOVAL) == 2


def test_a_sentence_that_names_someone_stands_after_a_removed_one():
    raw = f"We kept the fast [[{OTHER}]]. {TYPED} This is the same Augustine we remember. He was received."
    text, _c, net_result = _net(raw)
    assert text == "We kept the fast. This is the same Augustine we remember. He was received."
    assert REASON_FOLLOWS_REMOVAL not in _whys(net_result)


def test_a_removed_sentence_that_cites_nothing_leaves_its_neighbours_alone():
    typed = 'He wrote, "the community kept a different memory of Jesus at the meal altogether".'
    raw = f"We kept the fast [[{OTHER}]]. {typed} That is what we remember."
    text, _c, net_result = _net(raw)
    assert text == "We kept the fast. That is what we remember."
    assert REASON_FOLLOWS_REMOVAL not in _whys(net_result)


def test_a_fragment_after_a_removed_cited_sentence_goes():
    raw = f"We kept the fast [[{OTHER}]]. {TYPED} Almost never. We kept it still [[{OTHER}]]."
    text, _c, _n = _net(raw)
    assert text == "We kept the fast. We kept it still."


def test_leaning_is_an_opener_that_points_back_or_a_fragment_that_names_no_one():
    assert leans_on_previous("That condition was his.")
    assert leans_on_previous("Neither bishop tells us of any one child [[fix.witness.other]].")
    assert leans_on_previous("But he wrote that down.")
    assert leans_on_previous("Almost never.")
    assert not leans_on_previous("He was received all the same.")
    assert not leans_on_previous("This is the same Moses we remember as a robber.")
    assert not leans_on_previous("")


def test_a_removal_by_placement_takes_the_leaning_sentence_after_it_too():
    context = PlacementContext(offered=frozenset({"fix.quote.wrapped"}), voiced=frozenset({"fix.quote.wrapped"}))
    raw = f"We kept the fast [[{OTHER}]]. Augustine wrote of it [[{OTHER}]] [[quote:fix.quote.wrapped]]. That is what we remember. We kept it still [[{OTHER}]]."
    text, _c, net_result = apply_net(raw, repository_records=RECORDS, thin_topics=None, placement=context)
    assert text == "We kept the fast. We kept it still."
    assert REASON_FOLLOWS_REMOVAL in _whys(net_result)


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


# ---- a reply that lost most of what it cited ------------------------------


def test_a_reply_that_lost_two_fifths_of_its_cited_sentences_is_replaced_by_the_answer_record():
    assert HOLLOWED_SHARE == pytest.approx(0.4)
    draft = (
        f"Augustine began with pity [[{WITNESS}]]. He wrote of virgins taken captive [[{WITNESS}]]. "
        f'Some, he said, killed themselves "to avoid such disgrace" and more words besides [[{WITNESS}]]. '
        f'"Who that has any human feeling," he asked, "would refuse to forgive them?" [[{WITNESS}]] '
        f'"He who kills himself is a homicide," he wrote [[{WITNESS}]].'
    )
    settled = _fallback(draft)
    assert settled["answer_record_fallback"] == WITNESS
    assert settled["text"] == " ".join(WITNESS_TEXT.split())


def test_a_reply_that_lost_a_smaller_share_stands_as_the_net_left_it():
    draft = (
        f"Augustine began with pity [[{WITNESS}]]. He wrote of virgins taken captive [[{WITNESS}]]. "
        f"We kept the fast [[{OTHER}]]. We kept it on the fourth day [[{OTHER}]]. "
        f'"He who kills himself is a homicide," he wrote [[{WITNESS}]].'
    )
    settled = _fallback(draft)
    assert settled["answer_record_fallback"] is None
    assert settled["text"].startswith("Augustine began with pity. He wrote of virgins taken captive. We kept the fast.")


def test_a_hollowed_reply_with_no_answer_record_to_show_stands():
    typed = TYPED.replace(OTHER, "fix.term.fast")
    draft = f"The fast is the meal not eaten [[fix.term.fast]]. {typed} {typed}"
    settled = _fallback(draft, offered={})
    assert settled["answer_record_fallback"] is None and settled["citations"] is None
    assert settled["text"] == "The fast is the meal not eaten."


def test_a_story_told_again_is_cut_by_design_and_does_not_count_as_a_loss():
    removed = [{"sentence": "x", "why": "story already told in this conversation", "draft": "x [[fix.story.s]]"}] * 5
    net_result = {"reply_shape": {"removed": removed}, "sentences": [{"tags": ["fix.story.s"]}]}
    assert not _hollowed(net_result)


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
