"""What a world is told when it runs past its own measure.

This fires on roughly a third of turns - 19 of 54 in the 2026-08-17
generation pass - so its wording is load-bearing, and the wording it had
was working against the readability the rest of the system spends effort
on. "Fewer sentences, not less said" asks the model to keep every point
and compress the container, which produces short sentences built out of
unfamiliar words: good Flesch-Kincaid, bad Dale-Chall.

The replacement asks for the opposite trade - drop material, keep the
words plain - and was A/B'd against the old text on the nine real
over-ceiling drafts. Compliance held at 9/9 on both arms, Dale-Chall
improved on 7 of 9, and the mean answer came back at 163 words against
127, because the old wording had been cutting far below the ceiling it
was asked to meet rather than to it.

These tests pin the shape of that instruction, not the prose. A future
edit is free to rewrite the sentence; it is not free to go back to asking
for the same content in fewer words, or to stop naming the two numbers
the model needs to act on.

Pure string handling - no LLM, no key, no network.
"""
from app.graph.nodes import LENGTH_CORRECTIVE_TEMPLATE


def rendered(words=250, ceiling=150):
    return LENGTH_CORRECTIVE_TEMPLATE.format(words=words, ceiling=ceiling)


def test_it_names_both_numbers():
    """The model cannot act on "too long" - it needs the overrun and the
    bar, and the loop feeds it the SHORTEST draft seen so far, not the
    original, so the count has to come from the template's own slot."""
    text = rendered(words=312, ceiling=250)
    assert "312" in text
    assert "250" in text


def test_it_asks_for_less_said_not_tighter_packing():
    """The whole point of the change.

    The old text - "fewer sentences, not less said" - is an instruction
    to preserve content and compress wording. If that idea comes back,
    the readability regression comes back with it.
    """
    lowered = rendered().lower()
    assert "leaving something out" in lowered
    assert "not less said" not in lowered
    assert "fewer sentences" not in lowered


def test_it_protects_word_choice_explicitly():
    """Brevity must not be bought with denser vocabulary.

    Dale-Chall measures the share of words outside a familiar list, and
    that is the axis a length instruction most easily damages, because
    the cheapest way to shorten a sentence is a longer word.
    """
    lowered = rendered().lower()
    assert "plain" in lowered
    assert "denser words" in lowered or "denser" in lowered


def test_it_does_not_invite_cutting_far_below_the_measure():
    """The old wording panicked - told 200, it returned 88.

    The instruction says "inside that measure", not "well under it" or
    "as short as possible", because a world losing a third of its answer
    to a ceiling that never asked for it is its own kind of failure.
    """
    lowered = rendered().lower()
    assert "inside that measure" in lowered
    for greedy in ("as short as", "as brief as", "much shorter", "well under"):
        assert greedy not in lowered


def test_template_renders_without_stray_placeholders():
    text = rendered()
    assert "{" not in text and "}" not in text
