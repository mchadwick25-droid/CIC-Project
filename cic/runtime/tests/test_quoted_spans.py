"""Quotation marks are necessary and not sufficient.

This build quotes for three different jobs, and only one of them is
citation. The grounding gate exists to ask whether a turn put words in
someone's mouth that this world never licensed, and the answer is
uninterpretable if glosses and emphasis are counted alongside quotations:
across the 54 turns of the 2026-08-17 second pass the extractor produced
28 spans, of which about five were citations.

The rules under test were derived from that corpus and then measured on
the first pass's 54 turns, which were never used for tuning and quote far
more scripture. There, 27 spans became 19 and every one of the seven
dropped was a one-to-three word emphasis fragment.

The property worth protecting is that direction of error: this gate may
only ever go quiet about things that were never citations. The
must_survive cases below are the real quotations both passes produced,
including the two shortest, which sit exactly on the four-word floor.

Pure string handling - no retrieval, no LLM, no key, no network.
"""
import pytest

from app.prompts.quote_index import extract_quoted_spans


def q(inner):
    return f'The teacher said "{inner}" and left it there.'


@pytest.mark.parametrize("span", [
    # Scripture and patristic quotation the first pass actually produced.
    "If you would be perfect, go, sell what you possess and give to the poor",
    "yet not what I will, but what you will.",
    "You are the Christ, the Son of the living God.",
    "that Christ died, was buried, was raised, according to the scriptures",
    "let no one having a dispute with his fellow join you, until they be "
    "reconciled",
    "the knowledge and faith and immortality you made known to us through "
    "Jesus your servant.",
    "do not give what is holy to the dogs,",
    "with the Father before the ages and appeared at the end of time.",
    # The two shortest genuine quotations found anywhere across both
    # passes. They sit exactly on the floor - a floor of five loses them.
    "Let this cup pass",
    "the blood of God,",
])
def test_real_quotations_survive(span):
    assert extract_quoted_spans(q(span)) == [span]


@pytest.mark.parametrize("span", [
    # GLOSS - the build's own three-tier convention, never a quotation.
    "discernment (Diakrisis)",
    "the thoughts that trouble the mind (Logismoi)",
    "similar to the Father (homoios)",
    # EMPHASIS - scare quotes on a phrase.
    "important",
    "three weeks",
    "the Gospel,",
    "a holy man.",
    "only-begotten",
    "just receive",
    "was this natural",
])
def test_gloss_and_emphasis_are_not_citations(span):
    assert extract_quoted_spans(q(span)) == []


def test_runaway_across_a_paragraph_break():
    """An unmatched opening quote pairs with a later unrelated one.

    Produced 66- and 199-word spans in the wild. A quotation does not
    contain a paragraph break.
    """
    text = ('He wondered "to keep peace in his own house. That is a silence '
            'we cannot close.\n\nWhat we can tell you is what happened" next.')
    assert extract_quoted_spans(text) == []


def test_runaway_starting_mid_sentence():
    text = ('It "was not addition of knowledge. It was the difference '
            'between hearing a road described and walking it." So we say.')
    assert extract_quoted_spans(text) == []


def test_multi_sentence_quotation_starting_capitalised_survives():
    """The counterpart the runaway rule must not swallow.

    Length and a sentence boundary are not themselves disqualifying - a
    genuine quotation of two sentences opens with a capital, which is the
    whole discriminator.
    """
    span = ("Sell what you have and give to the poor. Then come, follow me.")
    assert extract_quoted_spans(q(span)) == [span]


def test_dedup_and_empty():
    assert extract_quoted_spans("") == []
    assert extract_quoted_spans(None) == []
    span = "do not give what is holy to the dogs,"
    assert extract_quoted_spans(q(span) + " " + q(span)) == [span]
