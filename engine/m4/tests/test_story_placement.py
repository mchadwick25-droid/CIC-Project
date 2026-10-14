"""Stories are placed by code on a world that switches story placement on:
the voice writes one sentence naming the story's subject and a
[[story:id]] marker, and the reply carries the record's own reviewed
telling, word for word. Proofs on drafts the desert voice wrote in the
13 October eleven-world live test, through apply_net, then through a whole
voice turn on the fixture world with the switch on and off."""
import pytest

from engine.m1.loader import load_world_records
from engine.m2 import builders
from engine.m4 import turn_prep
from engine.m4.grounding_net import REASON_STORY_MISMATCH, WHY_STORY_PLACED, check_turn_with_paragraph_coverage, strip_tags
from engine.m4.quote_placement import REASON_STORY_RETOLD, PlacementContext
from engine.m4.story_placement import (
    REASON_SECOND_STORY,
    REASON_STORY_NOT_OFFERED,
    REASON_STORY_INTRO,
    REASON_STORY_PARAPHRASE,
    STORY_PLACE_LINE,
    place_stories,
)
from engine.m4.sentence_stream import SentenceStream
from engine.m4.tests.test_rhythm import CANON, MESSAGE, _world
from engine.m4.tests.test_turn import FakeBedrockClient, _reader, _safety
from engine.m4.turn import apply_net, run_voice_turn_for_world
from engine.m4.turn_prep import prepare_voice_turn_inputs
from engine.m4.world_loader import LoadedWorld
from engine.m5.routing import Directive

MOSES = "desert.story.moses-leaking-jug"
ANTONY_CALL = "desert.story.antony-call"
SARAH = "desert.story.sarah-answer"

# The desert voice's Moses reply of 13 October, as it wrote it: the story
# improvised from tellable_as ("summoned to judge", "the errors of another
# man", "the elders ... released the brother without punishment").
MOSES_IMPROVISED = (
    "One of us, Moses, was summoned to judge an erring brother at Scetis [[desert.story.moses-leaking-jug]]. "
    "He came carrying a leaking basket of sand behind him [[desert.story.moses-leaking-jug]]. "
    "When the others asked what he was doing, he said: my own sins run out behind me and I do not see them, "
    "yet I have come today to judge the errors of another man [[desert.story.moses-leaking-jug]]. "
    "The elders heard him and released the brother without punishment [[desert.story.moses-leaking-jug]]."
)
# The same reply's second paragraph, kept as the voice wrote it.
MOSES_AFTER = (
    "This is the same Moses we remember as having been a robber and, by report, a murderer before he came to us "
    "[[desert.dw.someone-like-me]]. He was received all the same [[desert.dw.someone-like-me]]."
)
MOSES_AFTER_SHOWN = (
    "This is the same Moses we remember as having been a robber and, by report, a murderer before he came to us. "
    "He was received all the same."
)
MOSES_INTRO = "Our sayings keep a story of Abba Moses at Scete [[story:desert.story.moses-leaking-jug]]."
MOSES_DRAFT = f"{MOSES_INTRO}\n\n{MOSES_AFTER}"

# The desert voice's Jesus reply of 13 October: its Antony sentence, which
# introduced the call story and tagged it, as a marker sentence.
ANTONY_LEAD = "But knowing this about him was not, for most of us, the main thing [[desert.dw.jesus]]."
ANTONY_INTRO = "One of us heard it read aloud in church and took it as meant for him [[story:desert.story.antony-call]]."


@pytest.fixture(scope="module")
def desert():
    return load_world_records("desert")


def _net(raw, records, context):
    text, citations, net_result = apply_net(raw, repository_records=records, thin_topics=None, placement=context)
    return text, citations, net_result


def _offer(*ids, told=()):
    return PlacementContext(offered_stories=frozenset(ids), told_stories=frozenset(told))


def _telling_shown(record):
    return strip_tags(record["telling"])


def _whys(net_result):
    return [r["why"] for r in net_result["reply_shape"]["removed"]]


# ---- placement on real desert drafts --------------------------------------


def test_a_marker_places_the_records_telling_word_for_word_after_the_voices_introduction(desert):
    text, citations, net_result = _net(MOSES_DRAFT, desert, _offer(MOSES))
    intro, rest = text.split("\n\n", 1)
    assert intro == "Our sayings keep a story of Abba Moses at Scete:"
    assert rest == f"{_telling_shown(desert[MOSES])}\n\n{MOSES_AFTER_SHOWN}"
    assert net_result["reply_shape"]["placed"] == [MOSES]
    assert net_result["reply_shape"]["removed"] == []


def test_every_placed_sentence_is_verified_against_its_record_and_cited_to_it(desert):
    _text, citations, net_result = _net(MOSES_DRAFT, desert, _offer(MOSES))
    placed = [s for s in net_result["sentences"] if s.get("placed_story")]
    assert placed and all(s["verdict"] == "ok" and s["why"] == WHY_STORY_PLACED and s["tags"] == [MOSES] for s in placed)
    assert " ".join(s["sentence"] for s in placed) == " ".join(_telling_shown(desert[MOSES]).split())
    cited = [c["sentence"] for c in citations if c["record_ids"] == [MOSES]]
    assert cited[0] == "Our sayings keep a story of Abba Moses at Scete:"
    assert cited[1:] == [s["sentence"] for s in placed]


def test_the_improvised_details_of_the_live_reply_do_not_reach_the_participant(desert):
    text, _c, _r = _net(MOSES_DRAFT, desert, _offer(MOSES))
    for invented in ("summoned to judge", "errors of another man", "without punishment"):
        assert invented not in text
    assert "basket with a hole in it, filled it with sand" in text


def test_the_speech_inside_a_placed_telling_is_never_cut_as_a_typed_quotation(desert):
    text, _c, net_result = _net(MOSES_DRAFT, desert, _offer(MOSES))
    assert '"This sand is my sins, running down behind me, and I cannot see them.' in text
    assert not [s for s in net_result["sentences"] if s.get("placed_story") and s["verdict"] != "ok"]


def test_a_marker_closing_a_sentence_in_a_paragraph_ends_the_paragraph_and_the_reply_goes_on(desert):
    draft = f"{ANTONY_LEAD} {ANTONY_INTRO} Following Jesus meant that: total giving [[desert.dw.jesus]]."
    text, _c, net_result = _net(draft, desert, _offer(ANTONY_CALL))
    paragraphs = text.split("\n\n")
    assert paragraphs[0] == (
        "But knowing this about him was not, for most of us, the main thing. "
        "One of us heard it read aloud in church and took it as meant for him:"
    )
    assert "\n\n".join(paragraphs[1:-1]) == _telling_shown(desert[ANTONY_CALL])
    assert paragraphs[-1] == "Following Jesus meant that: total giving."
    assert net_result["reply_shape"]["placed"] == [ANTONY_CALL]


def test_a_marker_standing_alone_takes_the_sentence_before_it_as_its_introduction(desert):
    draft = "Our sayings keep a story of Abba Moses at Scete.\n\n[[story:desert.story.moses-leaking-jug]]"
    shaped = place_stories(draft, repository_records=desert, context=_offer(MOSES))
    assert shaped["text"].startswith(f"Our sayings keep a story of Abba Moses at Scete [[{MOSES}]]:\n\n")


def test_every_desert_telling_placed_passes_the_net_sentence_for_sentence(desert):
    for record_id, record in sorted(desert.items()):
        if record.get("record_type") != "story" or not record.get("telling"):
            continue
        subject = record["use_note"]["means"].split(",")[0].rstrip(".")
        draft = f"{subject} [[story:{record_id}]]."
        text, _c, net_result = _net(draft, desert, _offer(record_id))
        assert net_result["reply_shape"]["placed"] == [record_id], record_id
        assert _telling_shown(record) in text, record_id
        placed = [s for s in net_result["sentences"] if s.get("placed_story")]
        assert placed and all(s["verdict"] == "ok" for s in placed), record_id


# ---- what places nothing --------------------------------------------------


def test_with_placement_off_a_marker_places_nothing_and_takes_its_sentence(desert):
    text, _c, net_result = _net(MOSES_DRAFT, desert, PlacementContext())
    assert text == MOSES_AFTER_SHOWN
    assert net_result["reply_shape"]["placed"] == []
    assert _whys(net_result) == [REASON_STORY_NOT_OFFERED]


def test_a_story_without_a_telling_is_never_placed(desert):
    kellia = "desert.story.kellia-day"
    assert not desert[kellia].get("telling")
    text, _c, net_result = _net(f"Our sayings picture a day at Kellia [[story:{kellia}]]. {MOSES_AFTER}", desert, _offer(kellia))
    assert text == MOSES_AFTER_SHOWN and _whys(net_result) == [REASON_STORY_NOT_OFFERED]


def test_a_story_the_conversation_already_told_is_not_placed_again(desert):
    text, _c, net_result = _net(MOSES_DRAFT, desert, _offer(MOSES, told={MOSES}))
    assert text == MOSES_AFTER_SHOWN and _whys(net_result) == [REASON_STORY_RETOLD]


def test_a_reply_places_one_story_at_most(desert):
    draft = f"{MOSES_INTRO}\n\nAmma Sarah used to say a word to her brothers [[story:{SARAH}]]."
    text, _c, net_result = _net(draft, desert, _offer(MOSES, SARAH))
    assert net_result["reply_shape"]["placed"] == [MOSES]
    assert _telling_shown(desert[SARAH]) not in text
    assert _whys(net_result) == [REASON_SECOND_STORY]


def test_an_introduction_naming_someone_the_story_does_not_goes_and_the_story_is_still_placed(desert):
    draft = f"As Athanasius told it, Moses judged a brother [[story:{MOSES}]].\n\n{MOSES_AFTER}"
    text, _c, net_result = _net(draft, desert, _offer(MOSES))
    assert "Athanasius" not in text
    assert text == f"{_telling_shown(desert[MOSES])}\n\n{MOSES_AFTER_SHOWN}"
    assert net_result["reply_shape"]["placed"] == [MOSES]
    assert _whys(net_result) == [REASON_STORY_INTRO]


def test_an_introduction_that_opens_on_another_name_goes(desert):
    text, _c, net_result = _net(f"Antony said this of Moses [[story:{MOSES}]].", desert, _offer(MOSES))
    assert text == _telling_shown(desert[MOSES]) and _whys(net_result) == [REASON_STORY_INTRO]


def test_an_introduction_naming_an_accented_or_capitalised_stranger_goes(desert):
    for intro in ("One of us, Moses, learned it from Évagrios", "Our sayings keep Abba MOSES and ARSENIUS"):
        text, _c, net_result = _net(f"{intro} [[story:{MOSES}]].", desert, _offer(MOSES))
        assert _whys(net_result) == [REASON_STORY_INTRO], intro


def test_a_possessive_name_of_the_storys_own_person_holds(desert):
    for intro, story in (("We keep Antony's call", ANTONY_CALL), ("We keep Amma Sarah’s saying", SARAH)):
        text, _c, net_result = _net(f"{intro} [[story:{story}]].", desert, _offer(story))
        assert net_result["reply_shape"]["removed"] == [], intro
        assert text.startswith(f"{intro}:"), intro


def test_an_introduction_naming_the_community_alone_holds(desert):
    text, _c, net_result = _net(f"Here is one of ours [[story:{MOSES}]].", desert, _offer(MOSES))
    assert text.startswith("Here is one of ours:\n\n") and net_result["reply_shape"]["removed"] == []


def test_an_introduction_naming_no_one_and_not_the_community_goes(desert):
    text, _c, net_result = _net(f"Consider this [[story:{MOSES}]].", desert, _offer(MOSES))
    assert text == _telling_shown(desert[MOSES]) and _whys(net_result) == [REASON_STORY_INTRO]


def test_the_net_refuses_a_placed_sentence_that_is_not_in_the_records_telling(desert):
    altered = "Our sayings tell of a brother at Scete who committed a grave crime [[desert.story.moses-leaking-jug]]."
    key = " ".join(strip_tags(altered).split())
    result = check_turn_with_paragraph_coverage(altered, desert, placed={key: MOSES})
    assert result["sentences"][0]["verdict"] == "withhold"
    assert result["sentences"][0]["why"] == REASON_STORY_MISMATCH


def test_the_voice_writing_a_telling_sentence_again_never_cuts_it_from_the_placed_telling(desert):
    virgin = "desert.story.virgin-who-hid-athanasius"
    draft = (
        f"Our sayings keep a story of the virgin who hid Athanasius in Alexandria [[story:{virgin}]].\n\n"
        "She hid him. That was her courage [[desert.dw.someone-like-me]]."
    )
    text, _c, net_result = _net(draft, desert, _offer(virgin))
    assert _telling_shown(desert[virgin]) in text
    assert net_result["reply_shape"]["placed"] == [virgin]


def test_a_quote_marker_after_a_placed_story_never_takes_a_telling_sentence_as_its_lead_in(desert):
    draft = f"{MOSES_INTRO}\n\n[[quote:desert.quote.moses-sins-run-out]]"
    context = PlacementContext(offered=frozenset({"desert.quote.moses-sins-run-out"}), offered_stories=frozenset({MOSES}))
    text, _c, net_result = _net(draft, desert, context)
    assert _telling_shown(desert[MOSES]) in text
    assert "said nothing more to him:" not in text
    assert MOSES in net_result["reply_shape"]["placed"]


def test_a_second_story_marker_after_a_placed_story_leaves_the_telling_whole(desert):
    draft = f"{MOSES_INTRO}\n\n[[story:{SARAH}]]"
    text, _c, net_result = _net(draft, desert, _offer(MOSES, SARAH))
    assert text.endswith(_telling_shown(desert[MOSES]))
    assert _whys(net_result) == [REASON_SECOND_STORY]


def test_the_improvised_live_reply_is_withheld_where_the_story_could_have_been_placed(desert):
    text, _c, net_result = _net(f"{MOSES_IMPROVISED}\n\n{MOSES_AFTER}", desert, _offer(MOSES))
    assert text == MOSES_AFTER_SHOWN
    assert _whys(net_result) == [REASON_STORY_PARAPHRASE] * 4


def test_the_improvised_live_reply_is_unchanged_on_a_world_that_does_not_place_stories(desert):
    text, _c, net_result = _net(MOSES_IMPROVISED, desert, PlacementContext())
    assert "summoned to judge an erring brother" in text
    assert REASON_STORY_PARAPHRASE not in _whys(net_result) and net_result["reply_shape"]["placed"] == []


def test_the_voice_may_speak_of_a_story_once_it_is_placed(desert):
    after = "That is how we learned to look at our own faults first [[desert.story.moses-leaking-jug]]."
    text, _c, net_result = _net(f"{MOSES_INTRO} {after}", desert, _offer(MOSES))
    assert text.endswith("That is how we learned to look at our own faults first.")
    assert net_result["reply_shape"]["removed"] == []


# ---- the switch, the evidence block and the stream ------------------------


def test_the_frame_carries_the_switch_only_for_a_world_that_turns_it_on():
    base = {"representative": {"name": "Vera"}, "display_name": "Fix"}
    assert b"story_placement" not in builders.build_frame_json({}, {}, base)
    assert b'"story_placement":true' in builders.build_frame_json({}, {}, {**base, "story_placement": True}).replace(b" ", b"")


@pytest.fixture
def _canon(monkeypatch):
    monkeypatch.setattr(turn_prep, "load_fleet_records", lambda: CANON)


TELLING = 'The community told how Jesus broke bread at the meal. He said, "Do this to remember me," and they did.'


def _placing_world(on=True):
    world = _world()
    records = [
        {**r, "telling": TELLING, "use_note": {"means": "Jesus broke bread at the meal."}} if r["id"] == "fix.story.s" else r
        for r in world.repository["records"]
    ]
    frame = {**world.frame, **({"story_placement": True} if on else {})}
    return LoadedWorld(**{**world.__dict__, "repository": {"records": records}, "frame": frame})


def _directive():
    return Directive(asks=[{"order": 1, "text": MESSAGE}], kind="what_happened")


def test_a_placing_world_offers_its_stories_by_marker_in_the_evidence_and_the_directive(_canon):
    prepared = prepare_voice_turn_inputs(world=_placing_world(), participant_message=MESSAGE, directive=_directive())
    assert prepared.offered_stories == ["fix.story.s"]
    assert "- [[story:fix.story.s]] story" in prepared.user_message and "cite as [[fix.story.s]]" in prepared.user_message
    assert "[[story:fix.story.s]]" in prepared.turn_directive and STORY_PLACE_LINE in prepared.turn_directive


def test_a_world_without_the_switch_offers_no_story_for_placement_even_with_a_telling(_canon):
    off = prepare_voice_turn_inputs(world=_placing_world(on=False), participant_message=MESSAGE, directive=_directive())
    assert off.offered_stories == []
    assert "- [[fix.story.s]] story" in off.user_message
    assert "[[story:" not in off.user_message and "[[story:" not in (off.turn_directive or "")


def test_a_whole_turn_on_a_placing_world_shows_the_telling_and_marks_the_story_told(_canon):
    client = FakeBedrockClient(
        safety_response=_safety("NO_SIGNAL"), reader_response=_reader(),
        stream_scripts=[["The community told of Jesus at the meal [[story:fix.story.s]]."]],
    )
    voice_event, _usage = run_voice_turn_for_world(
        voice_client=client, voice_model_id="m", world=_placing_world(), participant_message=MESSAGE,
        directive=_directive(), session_id="test-session",
    )
    assert TELLING in voice_event["text"].replace("\n\n", " ")
    assert "[[" not in voice_event["text"]
    assert voice_event["reply_shape"]["placed"] == ["fix.story.s"]
    assert "fix.story.s" in {e["record_id"] for e in voice_event["transparency"]["elements"] if e["kind"] == "story"}


def test_the_stream_holds_back_a_sentence_carrying_a_story_marker(desert):
    stream = SentenceStream(repository_records=desert, world_key="desert", thin_topics=None)
    released = stream.feed(f"{ANTONY_LEAD} {ANTONY_INTRO} Following Jesus meant total giving [[desert.dw.jesus]]. ")
    assert not any("[[story:" in (e.get("raw") or "") or "took it as meant" in (e.get("text") or "") for e in released)
