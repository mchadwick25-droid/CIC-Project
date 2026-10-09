"""Quotes are placed by code: what reaches a participant under a name is a
quote record's own modern_rendering, once, or nothing. Unit proofs on
shape_reply, then the same rules through a whole voice turn with a fake
client on the fixture world."""
import pytest

from engine.m4 import turn_prep
from engine.m4.quote_placement import (
    REASON_ALREADY_VOICED,
    REASON_ATTRIBUTION,
    REASON_ATTRIBUTION_LEAD,
    REASON_LEAD_IN,
    REASON_NOT_OFFERED,
    REASON_SECOND_QUOTE,
    REASON_STORY_RETOLD,
    REASON_TYPED_QUOTATION,
    PlacementContext,
    shape_reply,
    strip_markdown,
)
from engine.m4.rhythm import tally_from_transcript
from engine.m4.tests.test_rhythm import CANON, MESSAGE, _world
from engine.m4.tests.test_turn import FakeBedrockClient, _reader, _safety
from engine.m4.turn import run_voice_turn_for_world
from engine.m4.turn_prep import prepare_voice_turn_inputs
from engine.m5.routing import Directive

RENDERING = "There is no lie in what we taught. The Son is of one being with the Father."
OTHER_RENDERING = "The meal held the memory of Jesus for the community."
RECORDS = {
    "fix.quote.leo": {"id": "fix.quote.leo", "record_type": "quote", "speaker_or_author": "Leo", "modern_rendering": RENDERING},
    "fix.quote.other": {"id": "fix.quote.other", "record_type": "quote", "speaker_or_author": "Leo", "modern_rendering": OTHER_RENDERING},
    "fix.story.s": {"id": "fix.story.s", "record_type": "story", "tellable_as": "A story."},
}
OFFERED = PlacementContext(offered=frozenset({"fix.quote.leo"}))


def _shape(raw, context=OFFERED):
    return shape_reply(raw, repository_records=RECORDS, context=context)


def _reasons(result):
    return [r["why"] for r in result["removed"]]


# ---- placement ----------------------------------------------------------


def test_a_marker_yields_the_records_modern_rendering_byte_for_byte_with_its_citation():
    result = _shape("We read Leo's sermon. Leo put it plainly [[quote:fix.quote.leo]]. Then we turn on.")
    assert result["placed"] == ["fix.quote.leo"]
    assert RENDERING in result["text"]
    assert f"“{RENDERING}” [[fix.quote.leo]]" in result["text"]
    assert "Leo put it plainly:" in result["text"]
    assert result["text"].endswith("Then we turn on.")


def test_a_marker_alone_takes_the_sentence_before_it_as_its_lead_in():
    result = _shape("Leo put it plainly.\n\n[[quote:fix.quote.leo]]\n\nMore.")
    assert result["text"] == f"Leo put it plainly: “{RENDERING}” [[fix.quote.leo]]\n\nMore."


def test_words_after_a_marker_in_its_sentence_are_cut_and_the_next_sentence_stays():
    result = _shape("Leo put it plainly [[quote:fix.quote.leo]] and we hold it still. We go on.")
    assert "hold it still" not in result["text"] and result["text"].endswith("We go on.")


def test_a_marker_for_a_record_not_in_the_turns_evidence_yields_nothing_and_takes_its_sentence():
    result = _shape("We read it. Leo put it plainly [[quote:fix.quote.other]]. We go on.")
    assert OTHER_RENDERING not in result["text"] and "Leo put it" not in result["text"]
    assert result["text"] == "We read it. We go on."
    assert _reasons(result) == [REASON_NOT_OFFERED]


def test_a_marker_for_a_record_that_does_not_exist_or_is_not_a_quote_yields_nothing():
    context = PlacementContext(offered=frozenset({"fix.quote.leo", "fix.story.s"}))
    for marker in ("[[quote:fix.quote.nowhere]]", "[[quote:fix.story.s]]", "[[quote]]", "[[quote:fix.quote.leo"):
        result = _shape(f"Leo put it plainly {marker}. We go on." if marker != "[[quote:fix.quote.leo" else f"We go on. Leo put it {marker}", context)
        assert result["placed"] == [] and "[[quote" not in result["text"]


def test_a_quote_already_voiced_in_the_conversation_is_not_placed_again():
    context = PlacementContext(offered=frozenset({"fix.quote.leo"}), voiced=frozenset({"fix.quote.leo"}))
    result = _shape("Leo put it plainly [[quote:fix.quote.leo]]. We go on.", context)
    assert result["placed"] == [] and RENDERING not in result["text"]
    assert _reasons(result) == [REASON_ALREADY_VOICED]


def test_a_second_marker_in_one_reply_is_ignored():
    context = PlacementContext(offered=frozenset({"fix.quote.leo", "fix.quote.other"}))
    result = _shape("Leo put it plainly [[quote:fix.quote.leo]]. Leo added more [[quote:fix.quote.other]]. We go on.", context)
    assert result["placed"] == ["fix.quote.leo"]
    assert RENDERING in result["text"] and OTHER_RENDERING not in result["text"]
    assert REASON_SECOND_QUOTE in _reasons(result)


# ---- typed quotes and attributed words ----------------------------------


def test_a_quotation_matching_no_record_goes_with_its_lead_in():
    result = _shape('Leo wrote, "there was no deception and no mixture in any of it at all". We go on.')
    assert result["text"] == "We go on."
    assert _reasons(result) == [REASON_TYPED_QUOTATION]


def test_a_near_miss_retranslation_of_a_real_quote_goes_too():
    near_miss = "There is no deception in what we taught. The Son is of one substance with the Father."
    result = _shape(f'Leo put it this way, "{near_miss}" [[fix.quote.leo]]. We go on.')
    assert near_miss not in result["text"] and result["text"] == "We go on."


def test_even_the_exact_words_of_a_record_typed_by_the_voice_are_not_spoken():
    result = _shape(f'Leo put it this way, "{RENDERING}" [[fix.quote.leo]]. We go on.')
    assert RENDERING not in result["text"]


def test_a_quotation_standing_alone_takes_the_lead_in_sentence_before_it():
    for raw in (
        'Leo answered the charge in these words: "No deception and no mixture was ever in it at all." We go on.',
        'Leo answered the charge. "No deception and no mixture was ever in it at all." We go on.',
        'Leo answered the charge in these words:\n\n"No deception and no mixture was ever in it at all."\n\nWe go on.',
    ):
        assert _shape(raw)["text"] == "We go on.", raw


def test_words_the_participant_said_may_be_quoted_back():
    context = PlacementContext(echo_texts=("Why did the council say that the Son shares the Father's being?",))
    raw = 'You asked why the council would say "the Son shares the Father\'s being". We go on.'
    assert _shape(raw, context)["text"] == raw


def test_attributed_words_without_quotation_marks_are_removed_like_an_unverified_quotation():
    cases = [
        "Athanasius wrote: the Son was never made out of nothing by anyone. We go on.",
        "Athanasius says plainly: the Son was never made out of nothing. We go on.",
        "As Cassian wrote, discernment is the mother of every virtue. We go on.",
        "Cassian put it this way: discernment is the mother of every virtue. We go on.",
        "In his own words: the Son was never made out of nothing. We go on.",
        "According to Leo: there was never any lie in it. We go on.",
    ]
    for raw in cases:
        result = _shape(raw)
        assert result["text"] == "We go on.", raw
        assert _reasons(result) == [REASON_ATTRIBUTION], raw


def test_an_attribution_that_ends_in_a_colon_takes_the_unmarked_words_after_it():
    result = _shape("Athanasius says plainly:\n\nThe Son was never made out of nothing by anyone. We go on.")
    assert result["text"] == "We go on."
    assert _reasons(result) == [REASON_ATTRIBUTION_LEAD, REASON_ATTRIBUTION_LEAD]


def test_the_worlds_own_we_voice_is_not_an_attribution():
    raw = "We say it plainly: the Son is of one being with the Father. As we said, the matter is old."
    assert _shape(raw)["text"] == raw


def test_a_placed_quote_with_a_matching_lead_in_is_not_taken_for_an_attribution():
    result = _shape("Leo wrote [[quote:fix.quote.leo]].")
    assert result["placed"] == ["fix.quote.leo"] and result["removed"] == []


# ---- spoken prose ---------------------------------------------------------


def test_headings_bold_citation_headers_and_labels_never_reach_the_participant():
    raw = "# The Rule\n\n**Cassian, Institutes V.26**\n\nWe keep the fast *because* we are asked to [[fix.quote.leo]].\n\n**Sources**\n\n---\n\nWe go on."
    text = strip_markdown(raw)
    assert "Cassian" not in text and "#" not in text and "**" not in text and "Sources" not in text and "---" not in text
    assert "We keep the fast because we are asked to [[fix.quote.leo]]." in text
    assert _shape(raw)["text"].endswith("We go on.")


def test_an_inline_bold_citation_locus_goes_and_other_emphasis_keeps_its_words():
    assert strip_markdown("The rule is plain **Cassian, Institutes V.26** and **never** broken.") == "The rule is plain and never broken."


def test_record_ids_with_underscores_survive_markdown_stripping():
    raw = "We held it [[fix.witness.some_id_here]] and _kept_ it."
    assert strip_markdown(raw) == "We held it [[fix.witness.some_id_here]] and kept it."


# ---- stories ---------------------------------------------------------------


def test_a_story_already_told_keeps_one_reference_and_loses_the_retelling():
    context = PlacementContext(told_stories=frozenset({"fix.story.s"}))
    raw = "We told that before [[fix.story.s]]. The man went out at night [[fix.story.s]]. He broke the bread [[fix.story.s]]. We go on."
    result = _shape(raw, context)
    assert result["text"] == "We told that before [[fix.story.s]]. We go on."
    assert _reasons(result) == [REASON_STORY_RETOLD, REASON_STORY_RETOLD]


def test_a_story_not_yet_told_is_left_alone():
    raw = "The man went out at night [[fix.story.s]]. He broke the bread [[fix.story.s]]."
    assert _shape(raw)["text"] == raw


# ---- through a whole voice turn -------------------------------------------


@pytest.fixture(autouse=True)
def _canon(monkeypatch):
    monkeypatch.setattr(turn_prep, "load_fleet_records", lambda: CANON)


def _directive():
    return Directive(asks=[{"order": 1, "text": MESSAGE}], kind="who")


def _offered(rhythm=None):
    prepared = prepare_voice_turn_inputs(world=_world(), participant_message=MESSAGE, directive=_directive(), rhythm=rhythm)
    return prepared.offered_ids["quote"]


def _turn(scripts, *, rhythm=None, sentence_enforce=False, **extra):
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_scripts=scripts)
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(), participant_message=MESSAGE, directive=_directive(),
        session_id="test-session", rhythm=rhythm, sentence_enforce=sentence_enforce, **extra,
    )
    return voice_event, client


def _rendering(record_id):
    return next(r for r in _world().repository["records"] if r["id"] == record_id)["modern_rendering"]


def test_a_placed_marker_reaches_the_participant_as_the_records_rendering_and_is_marked_as_a_quote():
    quote_id = _offered()[0]
    voice_event, client = _turn([[f"Ignatius put it plainly [[quote:{quote_id}]]."]], sentence_enforce=True)
    assert len(client.messages.captured_stream_calls) == 1
    assert _rendering(quote_id) in voice_event["text"]
    assert "[[" not in voice_event["text"]
    assert voice_event["reply_shape"]["placed"] == [quote_id]
    assert [e["record_id"] for e in voice_event["transparency"]["elements"] if e["kind"] == "quote"] == [quote_id]
    assert voice_event["grounding"]["sentences"][0]["verdict"] == "ok"


def test_a_marker_for_a_record_outside_this_turns_evidence_places_nothing():
    outside = "fix.witness.w"
    voice_event, _client = _turn([[f"Ignatius put it plainly [[quote:{outside}]]. The community kept the memory of Jesus at the meal [[fix.witness.w]]."]])
    assert voice_event["reply_shape"]["placed"] == []
    assert "Ignatius" not in voice_event["text"]
    assert voice_event["text"] == "The community kept the memory of Jesus at the meal."


def test_a_voice_that_types_a_quote_reaches_the_participant_without_it():
    voice_event, _client = _turn([[
        'Ignatius wrote, "the community kept a different memory of Jesus at the meal altogether". '
        "The community kept the memory of Jesus at the meal [[fix.witness.w]]."
    ]])
    assert voice_event["text"] == "The community kept the memory of Jesus at the meal."
    assert voice_event["reply_shape"]["removed"][0]["why"] == REASON_TYPED_QUOTATION


def test_attributed_words_without_marks_never_reach_the_participant_through_a_turn():
    voice_event, _client = _turn([[
        "Ignatius wrote: the community kept a different memory of Jesus at the meal altogether. "
        "The community kept the memory of Jesus at the meal [[fix.witness.w]]."
    ]])
    assert voice_event["text"] == "The community kept the memory of Jesus at the meal."


def test_a_header_and_a_bold_citation_block_never_reach_the_participant_through_a_turn():
    voice_event, _client = _turn([[
        "## The meal\n\n**Ignatius, Letter to the Smyrnaeans VII.1**\n\nThe community kept the memory of Jesus at the meal [[fix.witness.w]]."
    ]])
    assert voice_event["text"] == "The community kept the memory of Jesus at the meal."


def test_a_quote_placed_in_round_two_cannot_be_placed_in_full_in_round_four():
    quote_id = _offered()[0]
    first, _c = _turn([[f"Ignatius put it plainly [[quote:{quote_id}]]."]], sentence_enforce=True)
    assert first["reply_shape"]["placed"] == [quote_id]
    transcript = [
        {"speaker": "participant", "text": "q1"}, {"speaker": "fix", "text": "a1", "transparency": {"elements": []}},
        {"speaker": "participant", "text": "q2"}, {"speaker": "fix", **first},
        {"speaker": "participant", "text": "q3"}, {"speaker": "fix", "text": "a3", "transparency": {"elements": []}},
    ]
    tally = tally_from_transcript(transcript)
    assert tally.round_no == 4 and tally.quotes_voiced == {quote_id: 2}
    assert not tally.quote_placeable(quote_id) and tally.quote_placeable("fix.quote.zzz")
    again, _c = _turn(
        [[f"Ignatius put it plainly [[quote:{quote_id}]]. The community kept the memory of Jesus at the meal [[fix.witness.w]]."]],
        rhythm=tally, sentence_enforce=True,
    )
    assert again["reply_shape"]["placed"] == []
    assert _rendering(quote_id) not in again["text"]
    assert again["text"] == "The community kept the memory of Jesus at the meal."


def test_two_markers_in_one_reply_place_only_the_first():
    first_id, second_id, *_ = _offered() + [None]
    if second_id is None:
        pytest.skip("the fixture offers one quote")
    voice_event, _c = _turn([[f"Ignatius put it plainly [[quote:{first_id}]]. Polycarp added [[quote:{second_id}]]."]])
    assert voice_event["reply_shape"]["placed"] == [first_id]
    assert _rendering(second_id) not in voice_event["text"]


# ---- sentence enforcement ----------------------------------------------------

_CLEAN = "The community kept the memory of Jesus at the meal [[fix.witness.w]]."
_WITHHELD = "Athanasius of Alexandria opposed the council."


def test_a_withheld_sentence_triggers_one_regeneration_and_a_clean_retry_ships():
    voice_event, client = _turn([[f"{_CLEAN} {_WITHHELD}"], [_CLEAN]], sentence_enforce=True)
    assert len(client.messages.captured_stream_calls) == 2
    assert voice_event["text"] == "The community kept the memory of Jesus at the meal."
    assert voice_event["sentence_enforcement"]["regenerated"] is True
    assert voice_event["sentence_enforcement"]["still_flagged"] == []
    assert _WITHHELD in str(client.messages.captured_stream_calls[1])


def test_a_sentence_still_withheld_after_the_one_regeneration_is_dropped():
    voice_event, client = _turn([[f"{_CLEAN} {_WITHHELD}"], [f"{_CLEAN} {_WITHHELD}"]], sentence_enforce=True)
    assert len(client.messages.captured_stream_calls) == 2
    assert voice_event["text"] == "The community kept the memory of Jesus at the meal."
    assert voice_event["sentence_enforcement"]["sentences_dropped"] == [_WITHHELD]
    assert voice_event["sentence_enforcement_exhausted"] is False


def test_a_reply_in_which_every_sentence_is_still_withheld_is_set_aside_not_shown():
    voice_event, client = _turn([[_WITHHELD], [_WITHHELD]], sentence_enforce=True)
    assert len(client.messages.captured_stream_calls) == 2
    assert voice_event["text"] == ""
    assert voice_event["sentence_enforcement_exhausted"] is True
    assert voice_event["r27_enforcement_exhausted"] is False


def test_a_clean_turn_costs_no_extra_call_with_enforcement_on():
    voice_event, client = _turn([[_CLEAN]], sentence_enforce=True)
    assert len(client.messages.captured_stream_calls) == 1
    assert voice_event["text"] == "The community kept the memory of Jesus at the meal."
    assert voice_event["sentence_enforcement"]["regenerated"] is False
