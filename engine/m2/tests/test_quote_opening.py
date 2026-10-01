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


def test_quote_opening_truncates_past_the_width():
    quote = {"id": "fix.quote.long", "text": "irrelevant",
             "modern_rendering": "A rendering that runs on well past the default sixty-character width limit."}
    opening = _quote_opening(quote, width=20)
    assert opening.startswith('"A rendering that ru')
    assert opening.endswith('..."')
