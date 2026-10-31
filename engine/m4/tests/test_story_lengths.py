"""A story record with shorter reviewed tellings places the length the voice
names in its marker, checked by code: a missing or unknown length is medium,
a short or medium telling that does not fit the room in the reply falls to
the next shorter, and a full telling is not checked for room. The tellings are
built here from a desert story's own sentences."""
import pytest

from engine.m1.loader import load_world_records
from engine.m4.grounding_net import _placed_story_verdict, strip_tags
from engine.m4.quote_placement import PlacementContext
from engine.m4.story_placement import (
    REPLY_WORD_ROOM,
    STORY_LENGTH_LINE,
    choose_length,
    place_stories,
    story_lines,
    story_texts,
    with_placeable_stories,
)
from engine.m4.turn import apply_net

STORY = "desert.story.moses-leaking-jug"
INTRO = "Our sayings keep a story of Abba Moses at Scete"
SHORT = "Our sayings tell of a brother at Scete who committed an offence. Abba Moses came, carrying a basket of sand that leaked."
MEDIUM = SHORT + "\n\nThe sand was his own sins, running down behind him."


@pytest.fixture(scope="module")
def records():
    base = load_world_records("desert")
    return {**base, STORY: {**base[STORY], "telling_short": SHORT, "telling_medium": MEDIUM}}


def _context():
    return PlacementContext(offered_stories=frozenset({STORY}), told_stories=frozenset())


def _placed(records, named="", before=""):
    marker = f"[[story:{STORY}:{named}]]" if named else f"[[story:{STORY}]]"
    return place_stories(f"{before}{INTRO} {marker}.", repository_records=records, context=_context())


def _shown(text):
    return " ".join(strip_tags(text).split())


def test_the_texts_a_story_has_are_its_full_telling_and_any_shorter_ones(records):
    assert set(story_texts(records[STORY])) == {"short", "medium", "full"}
    assert set(story_texts(load_world_records("desert")[STORY])) == {"full"}


def test_a_marker_without_a_length_places_the_medium_telling(records):
    shaped = _placed(records)
    assert shaped["placed_lengths"] == {STORY: "medium"}
    assert MEDIUM.split("\n\n")[1] in _shown(shaped["text"])


@pytest.mark.parametrize("named,expected", [("short", "short"), ("medium", "medium"), ("full", "full"), ("FULL", "full"), ("long", "medium"), ("", "medium")])
def test_the_length_the_marker_names_is_placed_and_an_unknown_one_is_medium(records, named, expected):
    assert _placed(records, named)["placed_lengths"] == {STORY: expected}


def test_a_full_marker_places_the_whole_telling(records):
    shown = _shown(_placed(records, "full")["text"])
    assert _shown(records[STORY]["telling"]) in shown


def test_a_short_marker_places_only_the_short_telling(records):
    shown = _shown(_placed(records, "short")["text"])
    assert _shown(SHORT) in shown and "running down behind him" not in shown


def test_a_story_without_shorter_tellings_places_its_full_telling_whatever_the_marker_names():
    base = load_world_records("desert")
    for named in ("short", "medium", "full", ""):
        draft = f"{INTRO} [[story:{STORY}{':' + named if named else ''}]]."
        shaped = place_stories(draft, repository_records=base, context=_context())
        assert shaped["placed_lengths"] == {STORY: "full"}
        assert _shown(base[STORY]["telling"]) in _shown(shaped["text"])


def test_a_medium_that_does_not_fit_the_room_falls_to_short_and_a_full_is_not_checked(records):
    padding = " ".join(["word"] * (REPLY_WORD_ROOM - 20)) + "."
    medium_fits = _placed(records, "medium")
    assert medium_fits["placed_lengths"] == {STORY: "medium"}
    crowded = _placed(records, "medium", before=f"{padding}\n\n")
    assert crowded["placed_lengths"] == {STORY: "short"}
    still_full = _placed(records, "full", before=f"{padding}\n\n")
    assert still_full["placed_lengths"] == {STORY: "full"}


def test_a_short_telling_that_does_not_fit_is_still_placed_since_nothing_is_shorter(records):
    assert choose_length(records[STORY], "short", room=1) == "short"


def test_every_sentence_of_a_shorter_telling_passes_the_net_and_is_cited_to_the_record(records):
    draft = f"{INTRO} [[story:{STORY}:short]]."
    _text, citations, net = apply_net(draft, repository_records=records, thin_topics=None, placement=_context())
    placed = [s for s in net["sentences"] if s.get("placed_story")]
    assert placed and all(s["verdict"] == "ok" and s["tags"] == [STORY] for s in placed)
    assert " ".join(s["sentence"] for s in placed) == _shown(SHORT)
    assert net["reply_shape"]["story_lengths"] == {STORY: "short"}


def test_the_net_takes_a_sentence_from_any_of_the_tellings_and_refuses_one_from_none(records):
    kept = _placed_story_verdict("Abba Moses came, carrying a basket of sand that leaked.", [STORY], records, STORY)
    refused = _placed_story_verdict("He wept for joy at once.", [STORY], records, STORY)
    assert kept["verdict"] == "ok" and refused["verdict"] == "withhold"


def test_the_offer_lists_each_length_with_its_words_and_the_length_line_only_when_there_is_a_choice(records):
    evidence = {"candidates": [{"id": STORY, "record_type": "story", "head": "Moses and the basket"}]}
    offers = [c for c in with_placeable_stories(evidence, records)["candidates"] if c.get("placeable")]
    assert offers[0]["lengths"] == {name: len(text.split()) for name, text in story_texts(records[STORY]).items()}
    lines = story_lines(offers)
    assert "short" in lines[0] and "medium" in lines[0] and "full" in lines[0] and STORY_LENGTH_LINE in lines
    base = load_world_records("desert")
    only_full = [c for c in with_placeable_stories(evidence, base)["candidates"] if c.get("placeable")]
    assert STORY_LENGTH_LINE not in story_lines(only_full) and "words" not in story_lines(only_full)[0]
