"""The judge needs a verdict for "this was never a citation".

Scored against 42 hand-labelled spans from both generation passes. With
only MATCH and NONE available, 37 of 42 reached a reviewer as findings -
2 real fabrications and 35 other things, because a turn quoting its own
inference has no verdict that fits and falls to NONE. Adding
NOT_A_CITATION took that to 15 of 42 with both fabrications still caught:
10 of 12 paraphrased positions and 4 of 4 fragments correctly set aside.

The cost, recorded rather than hidden: 7 of 24 genuine citations were
also called NOT_A_CITATION. Those are short formulas and reported speech
crediting an unnamed source. It matters because a real citation of an
unlicensed source SHOULD surface as NONE - that is the signal telling
someone to license the quote - and calling it NOT_A_CITATION hides the
gap instead.

These tests cover the deterministic halves only: the verdict parser and
the context slice. Whether the judge rules well is a scored measurement,
not a unit test, and it needs an API key the suite must never require.
"""
import pytest

from app.graph.nodes import _QUOTATION_GROUNDING_LINE_PATTERN, _span_context


def parse(line):
    m = _QUOTATION_GROUNDING_LINE_PATTERN.match(line)
    if not m:
        return None
    return (m.group(1).upper(), m.group(2).upper(), m.group(3))


@pytest.mark.parametrize("line,expected", [
    ("A. MATCH: 3", ("A", "MATCH", "3")),
    ("B. NONE", ("B", "NONE", None)),
    ("C. NOT_A_CITATION", ("C", "NOT_A_CITATION", None)),
    ("d. not_a_citation", ("D", "NOT_A_CITATION", None)),
    ("  E.  NOT_A_CITATION  ", ("E", "NOT_A_CITATION", None)),
])
def test_every_verdict_parses(line, expected):
    assert parse(line) == expected


def test_commentary_is_ignored():
    assert parse("Here are my rulings:") is None


def test_bare_match_without_a_number_is_not_a_match():
    """The caller treats MATCH with no candidate number as unmatched.

    Pinned because a judge that answers "A. MATCH" with nothing after it
    has not identified anything, and reading that as grounded would clear
    a span on the strength of a malformed line.
    """
    letter, verdict, number = parse("A. MATCH")
    assert verdict == "MATCH"
    assert number is None


def test_context_surrounds_a_quoted_span():
    """A quoted span carries none of its own attribution.

    "You are the Christ..." says nothing about Peter, who is named
    outside the quotation marks - and judged on the span alone the model
    called plain scripture NOT_A_CITATION.
    """
    turn = ('When the question came, Peter answered him plainly: "You are '
            'the Christ, the Son of the living God." That is the confession '
            'Rome was built on.')
    context = _span_context(turn, "You are the Christ, the Son of the living God.")
    assert "Peter answered" in context


def test_context_for_an_attributed_rendering():
    """An attributed span is a rendering, not a substring of the turn.

    extract_attributed_spans returns "...wrote back ... that it was
    ordinary food." which appears nowhere in the source text, so the
    clause tail has to serve as the anchor.
    """
    turn = ("An outsider looked into one of our meals and wrote back, almost "
            "disappointed, that it was ordinary food. Nothing more.")
    context = _span_context(turn, "...wrote back, almost disappointed,  "
                                  "that it was ordinary food.")
    assert "An outsider" in context


def test_context_is_empty_when_nothing_anchors():
    assert _span_context("A turn about something else entirely.",
                         "a span that is simply not present") == ""


def test_context_collapses_newlines():
    turn = "He said this.\n\n\"the blood of God,\" and then stopped."
    assert "\n" not in _span_context(turn, "the blood of God,")
