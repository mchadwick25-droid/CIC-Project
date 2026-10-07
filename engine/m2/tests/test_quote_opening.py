"""Hermetic tests for builders._quote_opening: the speakable form shown in
build_prompt's "Quotes we hold" index is ALWAYS modern_rendering, never
`text` (item 3, the modern_rendering-required gate). No compiled package
on disk required.
"""
import pytest

from engine.m2.builders import _quote_opening


def test_quote_opening_uses_modern_rendering():
    quote = {"id": "fix.quote.has-rendering", "text": "The archaic original, never voiced.",
             "modern_rendering": "The modern spoken form."}
    assert _quote_opening(quote) == '"The modern spoken form."'


def test_quote_opening_with_no_modern_rendering_fails_loudly_not_silently_on_text():
    """gate_quote_recording requires every quote to carry modern_rendering,
    so this should be unreachable in real fleet data - pinned here so a
    future change can't quietly reintroduce the old `or text` fallback and
    have a quote missing its rendering silently index the archaic original
    instead."""
    quote = {"id": "fix.quote.no-rendering", "text": "The archaic original, never voiced.",
             "modern_rendering": None}
    with pytest.raises(ValueError, match="no modern_rendering"):
        _quote_opening(quote)


RENDERING = "A rendering that runs on well past the default sixty-character width limit."


def _long(rendering=RENDERING):
    return {"id": "fix.quote.long", "text": "irrelevant", "modern_rendering": rendering}


def test_quote_opening_cuts_at_the_last_word_boundary_before_the_width():
    # Character 20 falls inside "runs"; the cut backs up to the space before it.
    assert _quote_opening(_long(), width=20) == '"A rendering that..."'


def test_quote_opening_keeps_a_word_that_ends_exactly_at_the_width():
    # "A rendering that" is 16 characters and the next character is a space.
    assert _quote_opening(_long(), width=16) == '"A rendering that..."'


def test_quote_opening_never_ends_inside_a_word():
    for width in range(2, len(RENDERING)):
        kept = _quote_opening(_long(), width=width)[1:-4]
        assert RENDERING.startswith(kept)
        assert len(kept) <= width
        if " " in RENDERING[:width]:
            assert RENDERING[len(kept)] == " "


def test_quote_opening_hard_cuts_a_single_word_longer_than_the_width():
    assert _quote_opening(_long("Supercalifragilistic and more"), width=10) == '"Supercalif..."'
