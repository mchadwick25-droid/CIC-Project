"""A sentence code composed around a placed quote cites that quote alone. Any
other tag the voice wrote on its lead-in was not checked against the sentence,
so it never reaches a citation."""
import pytest

from engine.m1.loader import load_world_records
from engine.m4.quote_placement import PlacementContext
from engine.m4.turn import apply_net

QUOTE = "lpc.quote.a-dreadful-plague-broke-out"
OTHER = "lpc.figure.pontius"


@pytest.fixture(scope="module")
def records():
    return load_world_records("lpc")


def _ship(draft, records):
    return apply_net(draft, repository_records=records, thin_topics=None, placement=PlacementContext(offered=frozenset({QUOTE})))


def _cited_ids(citations):
    return {rid for c in citations for rid in c["record_ids"]}


def test_a_lead_in_with_only_the_quote_cites_the_quote(records):
    _text, citations, net = _ship(f"Pontius said it this way [[quote:{QUOTE}]].", records)
    assert _cited_ids(citations) == {QUOTE}
    assert [s["verdict"] for s in net["sentences"] if s.get("placed_quote")] == ["ok"]


@pytest.mark.parametrize("extra", ["made.up.record", OTHER, "lpc.story.numidicus"])
def test_a_tag_the_voice_added_to_the_lead_in_is_not_cited(records, extra):
    _text, citations, net = _ship(f"Pontius said it this way [[{extra}]] [[quote:{QUOTE}]].", records)
    assert _cited_ids(citations) == {QUOTE}
    placed = [s for s in net["sentences"] if s.get("placed_quote")]
    assert placed and placed[0]["verdict"] == "ok" and placed[0]["tags"] == [QUOTE]
