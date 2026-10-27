"""Each offered quote comes with its speaker's name, the one the placed-quote
check looks for in the marker's sentence, so the voice can name the right
speaker before generation instead of the check dropping the quote after it.
No model call."""
import re
from functools import lru_cache

import pytest

from engine.m1.loader import RECORDS_ROOT, load_world_records
from engine.m4 import evidence, grounding_net, turn_prep
from engine.m4.tests import live11_replay
from engine.m5.routing import Directive

_MARKER = re.compile(r"\[\[\s*quote\s*:\s*([a-z0-9_.-]+)\s*\]\]")


@lru_cache(maxsize=None)
def _fleet_quotes():
    out = []
    for world_dir in sorted(p for p in RECORDS_ROOT.iterdir() if (p / "quote").is_dir()):
        records = load_world_records(world_dir.name)
        index = grounding_net.QuotationIndex(records)
        for record in (r for r in records.values() if r.get("record_type") == "quote"):
            offered = turn_prep._offered_speaker(evidence._with_quote_index({"id": record["id"], "record_type": "quote"}, records))
            out.append((record, records, index, offered))
    return out


def test_every_quote_record_is_offered_with_a_speaker_name():
    quotes = _fleet_quotes()
    assert len(quotes) == 455
    for record, _records, _index, offered in quotes:
        assert offered and offered != "unattributed", record["id"]
        # a name a person writes, not a record id or a note after the name
        assert not re.search(r"\b[a-z]+\.[a-z]+\.", offered) and "--" not in offered, (record["id"], offered)


@pytest.mark.parametrize("verb", ["wrote", "said", "put it this way", "answered"])
def test_the_check_accepts_the_offered_name_in_the_markers_sentence(verb):
    for record, records, index, offered in _fleet_quotes():
        composed = f"{offered} {verb}: “{grounding_net.quotable_rendering(record)}” [[{record['id']}]]"
        assert grounding_net.placed_quote_refusal(composed, records, index, record["id"]) is None, (record["id"], offered)


@pytest.mark.parametrize("quote_id, name", [
    ("syr.quote.chronicle-flood-line", "The Chronicle of Edessa"),
    ("syr.quote.palladius-hospitaller", "Palladius of Galatia"),
    ("syr.quote.sozomen-melodies", "Sozomen"),
    ("syr.quote.theodoret-gnats", "Theodoret of Cyrus"),
])
def test_a_quote_whose_speaker_is_a_source_is_offered_by_its_authors_name(quote_id, name):
    # their speaker field is a source record's id; the offered name is the
    # source's author, or its work when the author is anonymous
    records = load_world_records("syr")
    assert grounding_net.QuotationIndex(records).speaker_name(records[quote_id]) == name


def test_the_directive_lists_each_quote_with_the_name_to_write():
    records = live11_replay.records("syr")
    turn = next(t for t in live11_replay.turns("retest") if t["world"] == "syr" and t["q"] == 4)
    candidates = [evidence._with_quote_index({"id": rid, "record_type": "quote"}, records)
                  for rid in turn["voice_event"]["offered_ids"]["quote"]]
    text = turn_prep._build_turn_directive(Directive(asks=[{"text": "Why did your people believe this?"}], kind="why"),
                                           quote_offers=candidates)
    assert "[[quote:syr.quote.nativity-this-is-the-day]], its sentence naming Ephrem (" in text
    assert "by the name listed with it, exactly as listed" in text
    assert "A quote whose sentence does not name its speaker that way is not placed." in text


def test_an_unnamed_lead_in_is_still_refused():
    # the check is not loosened: the offered name has to be written
    record, records, index, offered = next(q for q in _fleet_quotes() if q[0]["id"] == "desert.quote.christ-worketh-them-not-we")
    for lead in ("One of us told the philosophers:", "It is Christ who works them, by means of those who believe in him:"):
        composed = f"{lead} “{record['modern_rendering']}” [[{record['id']}]]"
        assert grounding_net.placed_quote_refusal(composed, records, index, record["id"]) == grounding_net.REASON_SPEAKER_UNNAMED
    assert offered == "Antony"


def _dropped_for_the_name(run):
    """The quotes the replay drops only because the lead-in did not name
    the speaker, and whether the offered name would have placed them."""
    out = []
    for turn, result in live11_replay.run_all(run):
        records = live11_replay.records(turn["world"])
        index = grounding_net.QuotationIndex(records)
        for cut in result["first_net"]["reply_shape"]["removed"]:
            found = _MARKER.search(cut["draft"])
            if not found or cut["why"] != grounding_net.REASON_SPEAKER_UNNAMED:
                continue
            record = records[found.group(1)]
            offered = turn_prep._offered_speaker(evidence._with_quote_index({"id": record["id"], "record_type": "quote"}, records))
            composed = f"{offered} wrote: “{record['modern_rendering']}” [[{record['id']}]]"
            out.append((turn["world"], turn["q"], record["id"],
                        grounding_net.placed_quote_refusal(composed, records, index, record["id"]) is None))
    return out


@pytest.mark.parametrize("run, replies", [("eleven-world-test", 9), ("retest", 2)])
def test_every_quote_dropped_for_its_name_places_with_the_offered_name(run, replies):
    dropped = _dropped_for_the_name(run)
    assert all(placed for *_where, placed in dropped)
    assert len({(world, q) for world, q, _rid, _placed in dropped}) == replies


@pytest.mark.parametrize("world, quote_id, lead", [
    # a single word of the offered name is not the name: places, offices
    # and common words stay refused (the independent review's probes)
    ("alx", "alx.quote.clement-bee", "In Alexandria a teacher wrote:"),
    ("syr", "syr.quote.palladius-hospitaller", "Galatia remembers it this way:"),
    ("syr", "syr.quote.theodoret-gnats", "Cyrus wrote:"),
    ("syr", "syr.quote.chronicle-flood-line", "The chronicle wrote:"),
])
def test_one_word_of_the_offered_name_does_not_stand_for_it(world, quote_id, lead):
    records = load_world_records(world)
    index = grounding_net.QuotationIndex(records)
    record = records[quote_id]
    composed = f"{lead} \u201c{record['modern_rendering']}\u201d [[{quote_id}]]"
    assert grounding_net.placed_quote_refusal(composed, records, index, quote_id) == grounding_net.REASON_SPEAKER_UNNAMED

