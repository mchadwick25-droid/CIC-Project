"""A saying attributed without quotation marks must still be visible.

The grounding gate (check_quotation_grounding) judges whether a turn put
words in someone's mouth that this world never licensed. Until 2026-08-17
it saw quotation marks and nothing else, so a representative that wrote
"Antony taught: ..." instead of "Antony taught: '...'" walked straight
past it.

The generation audit that day found two such turns. Both are pinned here
as the cases that must never go quiet again:

  desert   a saying minted whole and hung on Antony, absent from every
           record in the world, against a permanent prompt that forbids
           exactly this in four separate places
  pahc     Pliny's real testimony with Pliny's name taken off it

The rest of the file guards the other direction. The rules distinguishing
a reported clause from a relative pronoun or a demonstrative were derived
from real false fires, and a later loosening that quietly reinstates them
should fail here rather than surface as noise in the Phase-0 logs.

Pure string handling - no retrieval, no LLM, no key, no network.
"""
import pytest

from app.prompts.quote_index import (
    extract_attributed_spans,
    extract_quoted_spans,
)

# The two audit findings, verbatim from the turns that produced them.
ANTONY = (
    "A true monk knows the difference. Antony taught: better a man who "
    "prays badly but knows himself weak, than one who works wonders and "
    "thinks he stands alone. That is the measure we keep."
)
PLINY = (
    "An outsider once looked into one of our meals expecting to find "
    "something dark and wrote back, almost disappointed, that it was "
    "ordinary food."
)


def test_minted_saying_is_seen():
    spans = extract_attributed_spans(ANTONY)
    assert len(spans) == 1
    assert "prays badly" in spans[0]
    assert "Antony" in spans[0]


def test_stripped_attribution_is_seen():
    spans = extract_attributed_spans(PLINY)
    assert len(spans) == 1
    assert "ordinary food" in spans[0]


def test_quotation_marks_alone_would_have_missed_both():
    """The regression that motivated the whole module.

    Not an incidental assertion: it is the reason extract_attributed_spans
    exists, and if a future change makes extract_quoted_spans catch these
    on its own, this test failing is the signal to re-examine whether the
    second extractor is still earning its keep.
    """
    assert extract_quoted_spans(PLINY) == []
    # The Antony turn's only quotation-marked span in the wild was a
    # lexicon gloss, not the invented saying.
    assert extract_quoted_spans(ANTONY) == []


@pytest.mark.parametrize("text", [
    # Relative pronoun, not a report - "a synod THAT had deposed".
    "Julius wrote back to a synod that had deposed Athanasius.",
    "Ignatius writes to a community that already has this order.",
    "It answers the question put to it, not every question that could be put.",
    # Demonstrative determiner - "that day", "that night", "that silence".
    "Our record tells us Antony heard it read, that day in church.",
    "He tells us the singing took root that night in the basilica.",
    # Subordinator.
    "He wrote as though that did not matter at all.",
    # An absence being declared is the opposite of a claim being made.
    "Our record does not tell us that he ever said such a thing.",
    "Ephrem nowhere writes that the weave had cost the Gospel anything.",
    # A record showing something is the turn reasoning, not attribution.
    "The letter shows that presbyters were removed from office.",
])
def test_quiet_where_it_should_be(text):
    assert extract_attributed_spans(text) == []


@pytest.mark.parametrize("text,fragment", [
    ("Ignatius says plainly that if Christ did not really suffer, his own "
     "chains are for nothing.", "chains are for nothing"),
    ("Arius taught that the Son is not truly God, only similar to the "
     "Father.", "not truly God"),
    ("Abba Arsenius was told: flee, be silent, be still.", "be still"),
])
def test_real_attributions_still_land(text, fragment):
    spans = extract_attributed_spans(text)
    assert len(spans) == 1
    assert fragment in spans[0]


def test_empty_and_dedup():
    assert extract_attributed_spans("") == []
    assert extract_attributed_spans(None) == []
    twice = ANTONY + " " + ANTONY
    assert len(extract_attributed_spans(twice)) == 1
