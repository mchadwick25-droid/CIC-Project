"""Quotes are placed by code: what reaches a participant under a name is a
quote record's own modern_rendering, once, or nothing. Proofs through
apply_net (the one owner of the reply's shape), then the same rules through
a whole voice turn with a fake client on the fixture world."""
import pytest

from engine.m4 import turn_prep
from engine.m4.grounding_net import strip_markdown, strip_tags
from engine.m4.quote_placement import (
    REASON_ALREADY_VOICED,
    REASON_NOT_OFFERED,
    REASON_SECOND_QUOTE,
    REASON_STORY_RETOLD,
    PlacementContext,
    place_quotes,
)
from engine.m4.rhythm import tally_from_transcript
from engine.m4.tests.test_rhythm import CANON, MESSAGE, _world
from engine.m4.tests.test_turn import FakeBedrockClient, _reader, _safety
from engine.m4.turn import apply_net, run_voice_turn_for_world
from engine.m4.turn_prep import prepare_voice_turn_inputs
from engine.m5.routing import Directive

RENDERING = "There is no lie in what we taught. The Son is of one being with the Father."
OTHER_RENDERING = "The meal held the memory of Jesus for the community."
RECORDS = {
    "fix.figure.leo": {"id": "fix.figure.leo", "record_type": "figure", "names": [{"name": "Leo", "tag": "in-world"}]},
    "fix.quote.leo": {"id": "fix.quote.leo", "record_type": "quote", "speaker_or_author": "fix.figure.leo", "modern_rendering": RENDERING},
    "fix.quote.other": {"id": "fix.quote.other", "record_type": "quote", "speaker_or_author": "fix.figure.leo", "modern_rendering": OTHER_RENDERING},
    "fix.story.s": {"id": "fix.story.s", "record_type": "story", "tellable_as": "The man went out at night and broke the bread."},
    "fix.witness.w": {"id": "fix.witness.w", "record_type": "doctrinal_witness", "text": "We go on keeping the fast because we are asked to keep it."},
}
OFFERED = PlacementContext(offered=frozenset({"fix.quote.leo"}))
GO_ON = "We go on keeping the fast [[fix.witness.w]]."
GO_ON_SHOWN = "We go on keeping the fast."


def _net(raw, context=OFFERED, quotable_texts=None):
    text, _citations, net_result = apply_net(
        raw, repository_records=RECORDS, thin_topics=None, placement=context, quotable_texts=quotable_texts,
    )
    return text, net_result


def _whys(net_result):
    return [r["why"] for r in net_result["reply_shape"]["removed"]]


# ---- placement ----------------------------------------------------------


def test_a_marker_yields_the_records_modern_rendering_byte_for_byte_with_its_citation():
    text, net_result = _net(f"We read Leo's sermon [[fix.witness.w]]. Leo put it plainly [[quote:fix.quote.leo]]. {GO_ON}")
    assert net_result["reply_shape"]["placed"] == ["fix.quote.leo"]
    assert f"Leo put it plainly: “{RENDERING}”" in text
    assert text.endswith(GO_ON_SHOWN)
    placed = next(s for s in net_result["sentences"] if s.get("placed_quote"))
    assert placed["verdict"] == "ok" and placed["tags"] == ["fix.quote.leo"]


def test_a_marker_alone_takes_the_sentence_before_it_as_its_lead_in():
    shaped = place_quotes("Leo put it plainly.\n\n[[quote:fix.quote.leo]]\n\nMore.", repository_records=RECORDS, context=OFFERED)
    assert shaped["text"] == f"Leo put it plainly: “{RENDERING}” [[fix.quote.leo]]\n\nMore."


def test_words_after_a_marker_in_its_sentence_are_cut_and_the_next_sentence_stays():
    text, _r = _net(f"Leo put it plainly [[quote:fix.quote.leo]] and we hold it still. {GO_ON}")
    assert "hold it still" not in text and text.endswith(GO_ON_SHOWN)


def test_a_marker_for_a_record_not_in_the_turns_evidence_yields_nothing_and_takes_its_sentence():
    text, net_result = _net(f"Leo put it plainly [[quote:fix.quote.other]]. {GO_ON}")
    assert OTHER_RENDERING not in text and "Leo" not in text
    assert text == GO_ON_SHOWN
    assert _whys(net_result) == [REASON_NOT_OFFERED]


def test_a_marker_for_a_record_that_does_not_exist_or_is_not_a_quote_yields_nothing():
    context = PlacementContext(offered=frozenset({"fix.quote.leo", "fix.story.s"}))
    for marker in ("[[quote:fix.quote.nowhere]]", "[[quote:fix.story.s]]", "[[quote]]", "[[quote: fix.quote.leo"):
        text, net_result = _net(f"{GO_ON} Leo put it plainly {marker}", context)
        assert net_result["reply_shape"]["placed"] == [] and "[[" not in text and "quote" not in text, marker


def test_no_placement_context_places_nothing():
    text, net_result = _net(f"Leo put it plainly [[quote:fix.quote.leo]]. {GO_ON}", context=None)
    assert RENDERING not in text and net_result["reply_shape"]["placed"] == []


def test_a_quote_already_voiced_in_the_conversation_is_not_placed_again():
    context = PlacementContext(offered=frozenset({"fix.quote.leo"}), voiced=frozenset({"fix.quote.leo"}))
    text, net_result = _net(f"Leo put it plainly [[quote:fix.quote.leo]]. {GO_ON}", context)
    assert net_result["reply_shape"]["placed"] == [] and RENDERING not in text
    assert _whys(net_result) == [REASON_ALREADY_VOICED]


def test_a_quote_already_voiced_cannot_come_back_typed_or_paraphrased_under_its_speaker():
    context = PlacementContext(offered=frozenset({"fix.quote.leo"}), voiced=frozenset({"fix.quote.leo"}))
    for raw in (
        f'Leo put it this way, "{RENDERING}" [[fix.quote.leo]]. {GO_ON}',
        f"Leo said there was no lie in what was taught [[fix.quote.leo]]. {GO_ON}",
    ):
        text, _r = _net(raw, context, quotable_texts=[f"Leo put it plainly: “{RENDERING}”"][:0])
        assert text == GO_ON_SHOWN, raw


def test_a_second_marker_in_one_reply_is_ignored():
    context = PlacementContext(offered=frozenset({"fix.quote.leo", "fix.quote.other"}))
    text, net_result = _net(f"Leo put it plainly [[quote:fix.quote.leo]]. Leo added more [[quote:fix.quote.other]]. {GO_ON}", context)
    assert net_result["reply_shape"]["placed"] == ["fix.quote.leo"]
    assert RENDERING in text and OTHER_RENDERING not in text
    assert REASON_SECOND_QUOTE in _whys(net_result)


# ---- typed quotes and attributed words: the net's one quotation check ----


def test_a_quotation_matching_no_record_goes():
    text, net_result = _net(f'Leo wrote, "there was no deception and no mixture in any of it at all". {GO_ON}')
    assert text == GO_ON_SHOWN
    assert _whys(net_result) == ["quotation typed by the voice"]


def test_a_near_miss_retranslation_and_the_exact_words_typed_by_the_voice_both_go():
    near_miss = "There is no deception in what we taught. The Son is of one substance with the Father."
    for typed in (near_miss, RENDERING):
        text, _r = _net(f'Leo put it this way, "{typed}" [[fix.quote.leo]]. {GO_ON}')
        assert text == GO_ON_SHOWN, typed


def test_a_quotation_standing_alone_takes_the_lead_in_sentence_before_it():
    for raw in (
        f'Leo answered the charge in these words: "No deception and no mixture was ever in it at all." {GO_ON}',
        f'Leo answered the charge. "No deception and no mixture was ever in it at all." {GO_ON}',
        f'Leo answered the charge in these words:\n\n"No deception and no mixture was ever in it at all."\n\n{GO_ON}',
    ):
        assert _net(raw)[0] == GO_ON_SHOWN, raw


def test_words_the_participant_said_may_be_quoted_back():
    raw = 'You asked why the council would say "the Son shares the Father\'s being" [[fix.witness.w]].'
    text, _r = _net(raw, quotable_texts=["Why did the council say that the Son shares the Father's being?"])
    assert text == strip_tags(raw)


def test_attributed_words_without_quotation_marks_are_removed_like_an_unverified_quotation():
    for raw in (
        "Athanasius wrote: the Son was never made out of nothing by anyone.",
        "Athanasius says plainly: the Son was never made out of nothing.",
        "As Cassian wrote, discernment is the mother of every virtue.",
        "Cassian put it this way: discernment is the mother of every virtue.",
        "In his own words: the Son was never made out of nothing.",
        "According to Leo: there was never any lie in it.",
        "Leo says, there was never any lie in what we taught.",
        "Leo: there was never any lie in what we taught.",
        "There was never any lie in what we taught — Leo.",
        "We keep «there was never any lie in what we taught».",
        "We keep „there was never any lie in what we taught“.",
    ):
        text, _r = _net(f"{raw}\n\n{GO_ON}")
        assert text == GO_ON_SHOWN, raw


def test_an_attribution_colon_takes_every_unplaced_sentence_after_it():
    text, _r = _net(f"Leo wrote: there was no lie. The Son is one with the Father. It was never otherwise.\n\n{GO_ON}")
    assert text == GO_ON_SHOWN
    text, _r = _net(f"Athanasius says plainly:\n\nThe Son was never made out of nothing. He is the Father's own.\n\n{GO_ON}")
    assert text == GO_ON_SHOWN


def test_put_it_this_way_then_unplaced_words_goes_and_a_placed_quote_stays():
    text, _r = _net(f"Leo put it this way. There was never any lie in what we taught.\n\n{GO_ON}")
    assert text == GO_ON_SHOWN
    text, net_result = _net(f"Leo put it this way. [[quote:fix.quote.leo]]\n\n{GO_ON}")
    assert net_result["reply_shape"]["placed"] == ["fix.quote.leo"] and RENDERING in text


def test_the_worlds_own_we_voice_is_not_an_attribution():
    raw = "We say it plainly: we go on keeping the fast [[fix.witness.w]]. As we said, we keep the fast [[fix.witness.w]]."
    assert _net(raw)[0] == strip_tags(raw)


def test_a_placed_quote_with_a_matching_lead_in_is_not_taken_for_an_attribution():
    text, net_result = _net("Leo wrote [[quote:fix.quote.leo]].")
    assert net_result["reply_shape"]["placed"] == ["fix.quote.leo"] and net_result["reply_shape"]["removed"] == []
    assert text == f"Leo wrote: “{RENDERING}”"


# ---- a quote's words reach a participant only as a placed quote: the syr world's own records ----

EPHREM_QUOTE = "syr.quote.ephrem-only-begotten-dwelling"
RETRANSLATED = "the Only-Begotten left his home with God and lived in the Virgin"
SYR_CLEAN = "He is the Physician, and his coming is medicine for a wounded people [[syr.dw.jesus]]."
SYR_CLEAN_SHOWN = "He is the Physician, and his coming is medicine for a wounded people."


@pytest.fixture(scope="module")
def syr_records():
    from engine.m1.loader import load_world_records

    return load_world_records("syr")


def _syr(raw, records, voiced=frozenset()):
    context = PlacementContext(offered=frozenset({EPHREM_QUOTE}), voiced=voiced)
    text, citations, net_result = apply_net(raw, repository_records=records, thin_topics=None, placement=context)
    return text, citations, net_result


def test_a_sentence_tagged_to_a_quote_not_yet_placed_is_dropped_whether_or_not_it_names_the_speaker(syr_records):
    for sentence in (
        f"He sang that {RETRANSLATED} [[{EPHREM_QUOTE}]].",
        f"The Syrian deacon taught that {RETRANSLATED} [[{EPHREM_QUOTE}]].",
        f"Ephrem taught that {RETRANSLATED} [[{EPHREM_QUOTE}]].",
    ):
        text, citations, net_result = _syr(f"{sentence}\n\n{SYR_CLEAN}", syr_records)
        assert text == SYR_CLEAN_SHOWN, sentence
        assert all(EPHREM_QUOTE not in c["record_ids"] for c in citations), sentence
        assert [r["why"] for r in net_result["reply_shape"]["removed"]] == ["tagged to a quote record that has not been placed"]


def test_a_retranslation_of_a_quote_not_yet_placed_is_dropped_however_it_is_framed(syr_records):
    for sentence in (
        f"Ephrem sang: {RETRANSLATED}.",
        f"Ephrem sings, {RETRANSLATED}.",
        f"Ephrem chanted, {RETRANSLATED}.",
        f"Ephrem proclaimed: {RETRANSLATED}.",
        f"To quote Ephrem: {RETRANSLATED}.",
        f"Ephrem's words: {RETRANSLATED}.",
        f"Ephrem writes in his hymn on the Nativity: {RETRANSLATED}.",
        f"Ephrem gives it like this: {RETRANSLATED}.",
        f"Ephrem said — {RETRANSLATED}.",
        "The Only-Begotten left his home with God and lived in the Virgin (Ephrem).",
        "The Only-Begotten left his home with God and lived in the Virgin ~ Ephrem.",
        f"ephrem wrote: {RETRANSLATED}.",
        f"The hymn says: {RETRANSLATED}.",
        f"Ephrem wrote *{RETRANSLATED}*.",
        f"Ephrem wrote 「{RETRANSLATED}」.",
        f"Ephrem wrote 『{RETRANSLATED}』.",
    ):
        assert _syr(f"{sentence}\n\n{SYR_CLEAN}", syr_records)[0] == SYR_CLEAN_SHOWN, sentence


def test_a_retranslation_running_on_past_an_inline_attribution_into_the_next_paragraph_is_dropped(syr_records):
    raw = (
        "Ephrem wrote: the Only-Begotten left his home with God.\n\n"
        "He came to live in the Virgin, so that by a shared manner of birth he might become brother to many.\n\n"
        f"{SYR_CLEAN}"
    )
    assert _syr(raw, syr_records)[0] == SYR_CLEAN_SHOWN


def test_lower_case_names_and_corner_brackets_are_read_as_what_they_are(syr_records):
    _text, _c, net_result = _syr(f"ephrem wrote: {RETRANSLATED}.", syr_records)
    assert net_result["reply_shape"]["removed"][0]["why"] == "words attributed without a placed quote"
    _text, _c, net_result = _syr(f"Ephrem wrote 「{RETRANSLATED}」.", syr_records)
    assert net_result["reply_shape"]["removed"][0]["why"] == "quotation typed by the voice"


def test_the_placed_quote_and_a_refer_back_in_the_same_reply_both_stay(syr_records):
    text, _c, net_result = _syr(
        f"Ephrem put it plainly [[quote:{EPHREM_QUOTE}]].\n\nThat is how we sing of his coming [[{EPHREM_QUOTE}]]. {SYR_CLEAN}",
        syr_records,
    )
    assert net_result["reply_shape"] == {"placed": [EPHREM_QUOTE], "removed": []}
    assert syr_records[EPHREM_QUOTE]["modern_rendering"].split()[-1] in text
    assert text.endswith(f"That is how we sing of his coming. {SYR_CLEAN_SHOWN}")


def test_referring_back_to_a_quote_already_voiced_is_unchanged(syr_records):
    voiced = frozenset({EPHREM_QUOTE})
    text, citations, _r = _syr(f"We have sung already of the brother of many [[{EPHREM_QUOTE}]]. {SYR_CLEAN}", syr_records, voiced)
    assert text == f"We have sung already of the brother of many. {SYR_CLEAN_SHOWN}"
    assert citations[0]["record_ids"] == [EPHREM_QUOTE]
    text, _c, net_result = _syr(f"Ephrem has sung already of the brother of many [[{EPHREM_QUOTE}]]. {SYR_CLEAN}", syr_records, voiced)
    assert text == SYR_CLEAN_SHOWN
    assert net_result["reply_shape"]["removed"][0]["why"] == "quote record's speaker named without its placed quote"


# Re-translations of quotes from across the fleet, in the voice's own framing.
FLEET_RETRANSLATIONS = (
    ("pahc", "On the day named for the sun, all who live in town or country gather in one place, and the memoirs of the apostles or the prophets' writings are read as long as there is time."),
    ("desert", "From the fear of the Lord comes compunction, from compunction renunciation, from owning nothing humility is born, and from humility the death of desires."),
    ("alx", "These books are fountains of salvation, so whoever thirsts may be filled with the living words in them; let no one add to them or take anything from them."),
    ("gallic", "The Lord Jesus never promised to return in purple with a shining crown; I will not believe Christ has come unless he shows the marks of his wounds from the cross."),
    ("ijc", "I told them I cannot give up the basilica, but neither may I fight."),
    ("cappadocian", "My grandmother, the well-known Macrina, raised me; she taught me the words of the blessed Gregory, which she had kept as memory carried them down to her day."),
    ("witt", "Baptism is necessary for salvation; through it God offers grace, children should be baptized, and we reject the Anabaptists who say children are saved without it."),
    ("hal", "You are lying: you follow Cicero, not Christ, for where your treasure is, your heart will be too."),
)


def test_retranslations_of_quotes_across_the_fleet_are_dropped():
    from engine.m1.loader import load_world_records

    for world, sentence in FLEET_RETRANSLATIONS:
        records = load_world_records(world)
        text, _c, net_result = apply_net(sentence, repository_records=records, thin_topics=None, placement=PlacementContext())
        assert text == "", sentence
        assert [r["why"] for r in net_result["reply_shape"]["removed"]] == ["gives a quote record's words without placing it"]


# ---- spoken prose -----------------------------------------------------------


def test_headings_bold_citation_headers_and_labels_never_reach_the_participant():
    raw = f"# The Rule\n\n**Cassian, Institutes V.26**\n\nWe keep the fast *because* we are asked to [[fix.witness.w]].\n\n**Sources**\n\n---\n\n{GO_ON}"
    text = strip_markdown(raw)
    assert "Cassian" not in text and "#" not in text and "**" not in text and "Sources" not in text and "---" not in text
    assert "We keep the fast because we are asked to [[fix.witness.w]]." in text
    assert _net(raw)[0].endswith(GO_ON_SHOWN)


def test_an_inline_bold_citation_locus_goes_and_other_emphasis_keeps_its_words():
    assert strip_markdown("The rule is plain **Cassian, Institutes V.26** and **never** broken.") == "The rule is plain and never broken."


def test_record_ids_and_markers_with_underscores_survive_markdown_stripping():
    raw = "We held it [[fix.witness.some_id_here]] and _kept_ it [[quote:fix.quote.some_id]]."
    assert strip_markdown(raw) == "We held it [[fix.witness.some_id_here]] and kept it [[quote:fix.quote.some_id]]."


def test_strip_tags_removes_quote_markers_too():
    assert strip_tags("Leo put it plainly [[quote:fix.quote.leo]] and [[fix.witness.w]].") == "Leo put it plainly and."
    assert strip_tags("Leo put it plainly. [[quote:fix.quote.le") == "Leo put it plainly."


# ---- stories -------------------------------------------------------------------


def test_a_story_already_told_keeps_one_reference_and_loses_the_retelling():
    context = PlacementContext(told_stories=frozenset({"fix.story.s"}))
    raw = "We told that before [[fix.story.s]]. The man went out at night [[fix.story.s]]. He broke the bread [[fix.story.s]]. We go on."
    shaped = place_quotes(raw, repository_records=RECORDS, context=context)
    assert shaped["text"] == "We told that before [[fix.story.s]]. We go on."
    assert [r["why"] for r in shaped["removed"]] == [REASON_STORY_RETOLD, REASON_STORY_RETOLD]


def test_a_story_not_yet_told_is_left_alone():
    raw = "The man went out at night [[fix.story.s]]. He broke the bread [[fix.story.s]]."
    assert place_quotes(raw, repository_records=RECORDS, context=OFFERED)["text"] == raw


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


def _record(record_id):
    return next(r for r in _world().repository["records"] if r["id"] == record_id)


def _rendering(record_id):
    return _record(record_id)["modern_rendering"]


def _speaker(record_id):
    return _record(record_id)["speaker_or_author"]


_CLEAN = "The community kept the memory of Jesus at the meal [[fix.witness.w]]."
_CLEAN_SHOWN = "The community kept the memory of Jesus at the meal."
_WITHHELD = "Athanasius of Alexandria opposed the council."


def test_a_placed_marker_reaches_the_participant_as_the_records_rendering_and_is_marked_as_a_quote():
    quote_id = _offered()[0]
    voice_event, client = _turn([[f"{_speaker(quote_id)} put it plainly [[quote:{quote_id}]]."]], sentence_enforce=True)
    assert len(client.messages.captured_stream_calls) == 1
    assert _rendering(quote_id) in voice_event["text"]
    assert "[[" not in voice_event["text"]
    assert voice_event["reply_shape"]["placed"] == [quote_id]
    assert [e["record_id"] for e in voice_event["transparency"]["elements"] if e["kind"] == "quote"] == [quote_id]
    assert voice_event["grounding"]["sentences"][0]["verdict"] == "ok"


def test_a_marker_for_a_record_outside_this_turns_evidence_places_nothing():
    voice_event, _client = _turn([[f"Ignatius put it plainly [[quote:fix.witness.w]]. {_CLEAN}"]])
    assert voice_event["reply_shape"]["placed"] == []
    assert voice_event["text"] == _CLEAN_SHOWN


def test_a_voice_that_types_a_quote_reaches_the_participant_without_it():
    voice_event, _client = _turn([[
        f'Ignatius wrote, "the community kept a different memory of Jesus at the meal altogether". {_CLEAN}'
    ]])
    assert voice_event["text"] == _CLEAN_SHOWN
    assert voice_event["reply_shape"]["removed"][0]["why"] == "quotation typed by the voice"


def test_attributed_words_without_marks_never_reach_the_participant_through_a_turn():
    voice_event, _client = _turn([[
        f"Ignatius wrote: the community kept a different memory of Jesus at the meal altogether.\n\n{_CLEAN}"
    ]])
    assert voice_event["text"] == _CLEAN_SHOWN


def test_a_header_and_a_bold_citation_block_never_reach_the_participant_through_a_turn():
    voice_event, _client = _turn([[f"## The meal\n\n**Ignatius, Letter to the Smyrnaeans VII.1**\n\n{_CLEAN}"]])
    assert voice_event["text"] == _CLEAN_SHOWN


def test_a_quote_placed_in_round_two_cannot_be_placed_in_full_in_round_four():
    quote_id = _offered()[0]
    first, _c = _turn([[f"{_speaker(quote_id)} put it plainly [[quote:{quote_id}]]."]], sentence_enforce=True)
    assert first["reply_shape"]["placed"] == [quote_id]
    transcript = [
        {"speaker": "participant", "text": "q1"}, {"speaker": "fix", "text": "a1", "transparency": {"elements": []}},
        {"speaker": "participant", "text": "q2"}, {"speaker": "fix", **first},
        {"speaker": "participant", "text": "q3"}, {"speaker": "fix", "text": "a3", "transparency": {"elements": []}},
    ]
    tally = tally_from_transcript(transcript)
    assert tally.round_no == 4 and tally.quotes_voiced == {quote_id: 2}
    assert not tally.quote_placeable(quote_id) and tally.quote_placeable("fix.quote.zzz")
    again, client = _turn(
        [[f"{_speaker(quote_id)} put it plainly [[quote:{quote_id}]]. {_CLEAN}"], [_CLEAN]],
        rhythm=tally, sentence_enforce=True,
    )
    assert len(client.messages.captured_stream_calls) == 2
    assert again["reply_shape"]["placed"] == []
    assert _rendering(quote_id) not in again["text"]
    assert again["text"] == _CLEAN_SHOWN


def test_two_markers_in_one_reply_place_only_the_first():
    first_id, second_id, *_ = _offered() + [None]
    if second_id is None:
        pytest.skip("the fixture offers one quote")
    voice_event, _c = _turn([[
        f"{_speaker(first_id)} put it plainly [[quote:{first_id}]].\n\n{_speaker(second_id)} added [[quote:{second_id}]]."
    ]])
    assert voice_event["reply_shape"]["placed"] == [first_id]
    assert _rendering(second_id) not in voice_event["text"]


# ---- sentence enforcement ----------------------------------------------------


def test_a_withheld_sentence_triggers_one_regeneration_and_a_clean_retry_ships():
    voice_event, client = _turn([[f"{_CLEAN} {_WITHHELD}"], [_CLEAN]], sentence_enforce=True)
    assert len(client.messages.captured_stream_calls) == 2
    assert voice_event["text"] == _CLEAN_SHOWN
    assert voice_event["sentence_enforcement"]["regenerated"] is True
    assert voice_event["sentence_enforcement"]["still_flagged"] == []
    assert _WITHHELD in str(client.messages.captured_stream_calls[1])


def test_a_typed_quotation_triggers_the_same_one_regeneration():
    typed = 'Ignatius wrote, "the community kept a different memory of Jesus at the meal altogether".'
    voice_event, client = _turn([[f"{_CLEAN} {typed}"], [_CLEAN]], sentence_enforce=True)
    assert len(client.messages.captured_stream_calls) == 2
    assert voice_event["text"] == _CLEAN_SHOWN
    assert "[[quote:" in str(client.messages.captured_stream_calls[1])


def test_a_sentence_still_withheld_after_the_one_regeneration_is_dropped():
    voice_event, client = _turn([[f"{_CLEAN} {_WITHHELD}"], [f"{_CLEAN} {_WITHHELD}"]], sentence_enforce=True)
    assert len(client.messages.captured_stream_calls) == 2
    assert voice_event["text"] == _CLEAN_SHOWN
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
    assert voice_event["text"] == _CLEAN_SHOWN
    assert voice_event["sentence_enforcement"]["regenerated"] is False


def test_enforcement_is_on_by_default():
    client = FakeBedrockClient(safety_response=_safety("NO_SIGNAL"), reader_response=_reader(), stream_scripts=[[_WITHHELD], [_CLEAN]])
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_world(), participant_message=MESSAGE, directive=_directive(),
        session_id="test-session",
    )
    assert len(client.messages.captured_stream_calls) == 2
    assert voice_event["text"] == _CLEAN_SHOWN


# ---- every quote record in the fleet ------------------------------------------

# The shared sentence splitter cannot keep these renderings in one sentence,
# so a marker for one places nothing and removes its sentence.
UNPLACEABLE = {
    "cappadocian.quote.macrina-refuses-remarriage",
    "gallic.quote.archebius-carried-off-to-panephysis",
    "gallic.quote.archebius-see-the-old-men",
    "gallic.quote.gallus-on-the-forced-communion-and-the-angel",
    "gallic.quote.paphnutius-accused-and-the-book-found",
    "gallic.quote.the-fathers-and-the-angels-twelve",
    "ijc.quote.ammianus-sicininus-massacre",
    "ijc.quote.lactantius-dream",
    "syr.quote.palladius-hospitaller",
    "syr.quote.warned-before-baptism",
}


def test_every_quote_record_in_the_fleet_places_word_for_word_except_the_registered_ten():
    from engine.m1.loader import RECORDS_ROOT, load_world_records

    unplaced = set()
    for world_dir in sorted(p for p in RECORDS_ROOT.iterdir() if (p / "quote").is_dir()):
        records = load_world_records(world_dir.name)
        for record in (r for r in records.values() if r.get("record_type") == "quote"):
            context = PlacementContext(offered=frozenset({record["id"]}))
            text, _c, net_result = apply_net(
                f"We read it [[quote:{record['id']}]].", repository_records=records, thin_topics=None, placement=context,
            )
            rendering = " ".join(record["modern_rendering"].split())
            if net_result["reply_shape"]["placed"] != [record["id"]] or rendering not in " ".join(text.split()):
                unplaced.add(record["id"])
    assert unplaced == UNPLACEABLE


def test_no_quote_records_gist_is_taken_for_its_words_anywhere_in_the_fleet():
    """The voice is shown each offered quote's gist (use_note.means) and may
    echo it."""
    from engine.m1.loader import RECORDS_ROOT, load_world_records

    refused = []
    for world_dir in sorted(p for p in RECORDS_ROOT.iterdir() if (p / "quote").is_dir()):
        records = load_world_records(world_dir.name)
        for record in (r for r in records.values() if r.get("record_type") == "quote"):
            gist = (record.get("use_note") or {}).get("means")
            if not gist:
                continue
            context = PlacementContext(offered=frozenset({record["id"]}))
            _t, _c, net_result = apply_net(gist, repository_records=records, thin_topics=None, placement=context)
            whys = {r["why"] for r in net_result["reply_shape"]["removed"]}
            if whys & {"gives a quote record's words without placing it", "tagged to a quote record that has not been placed"}:
                refused.append(record["id"])
    assert refused == []
