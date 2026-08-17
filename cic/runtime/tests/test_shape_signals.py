"""The two shape signals must survive the hand-synced lists.

BURIED_ANSWER and ACCUMULATION replace what the word ceiling was trying
and failing to do. They are the shape failures a length gate cannot see:
a long turn whose answer sits in its opening is fine, a short one that
circles for half its length is not, and a turn can stack four sources
into two hundred words or rest on one across four hundred.

They are reported, not gated - queued as guidance that corrects the next
turn, the way FABRICATION and OVER_SETTLING already work, rather than
regenerating the current one under pressure.

This file exists because of a specific trap. nodes.py carries a
hand-written `valid_signals` list, and a signal absent from it is not
dropped - it is silently rewritten to "smoothing". A new signal can be
fully specified in the monitoring prompt, fire correctly on real traffic,
and be recorded as something else entirely, with nothing anywhere
reporting a problem. The same class of hand-synced list is what
world_manifest.py was built to end.

Pure list and string checks - no LLM, no key, no network.
"""
import pytest

from app.graph.nodes import _SIGNAL_PRIORITY, signal_rank
from app.prompts.facilitator_prompts import FACILITATOR_MONITORING_PROMPT

SHAPE_SIGNALS = ["buried_answer", "accumulation"]


@pytest.mark.parametrize("signal", SHAPE_SIGNALS)
def test_signal_is_specified_in_the_monitoring_prompt(signal):
    assert signal.upper() in FACILITATOR_MONITORING_PROMPT


@pytest.mark.parametrize("signal", SHAPE_SIGNALS)
def test_signal_survives_the_valid_signals_whitelist(signal):
    """The trap this file exists for.

    An unlisted signal is not discarded - it is relabelled "smoothing",
    so the failure is invisible in every log and every count.
    """
    import inspect

    import app.graph.nodes as nodes

    source = inspect.getsource(nodes._detect_drift_signal_impl)
    assert f'"{signal}"' in source, (
        f"{signal} is missing from valid_signals - it will be silently "
        f"rewritten to 'smoothing'")


@pytest.mark.parametrize("signal", SHAPE_SIGNALS)
def test_signal_has_a_place_in_the_ordering(signal):
    """Absent from _SIGNAL_PRIORITY a signal still works, but sorts below
    everything named, so it loses every tie to any listed signal."""
    assert signal in _SIGNAL_PRIORITY


def test_shape_ranks_below_the_untrue_signals():
    """Ordering is by seriousness, not by prompt order.

    A turn that buries its answer is a shape problem; one that invents a
    saying put something untrue in front of a participant. If both fire,
    fabrication is the one the representative must hear about.
    """
    for signal in SHAPE_SIGNALS:
        assert signal_rank("fabrication", "medium") < signal_rank(signal, "medium")
        assert signal_rank("over_settling", "medium") < signal_rank(signal, "medium")


def test_the_prompt_separates_buried_answer_from_over_producing():
    """The distinction that makes the signal worth having.

    OVER_PRODUCING is about giving too much. BURIED_ANSWER is about
    withholding the answer until late, which a brief and disciplined turn
    can do just as easily as an exhaustive one. Collapsed together, the
    new signal adds nothing.
    """
    assert "NOT the same as OVER_PRODUCING" in FACILITATOR_MONITORING_PROMPT


def test_the_prompt_states_shape_is_not_length():
    """Both signals exist because a word count could not see them, and
    the prompt has to say so or the model will reach for length anyway."""
    assert "This is NOT about length" in FACILITATOR_MONITORING_PROMPT
