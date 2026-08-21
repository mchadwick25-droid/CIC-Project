"""Crisis resources appended by CODE, never recalled by a model (Build-
Blueprint.md principle 5, CiC-Program-Spec.md SS8/O5: "crisis resources are
appended by code, never recalled by a model"). This is the one place that
text exists in this codebase - a fixed dict, not a prompt, not something any
model call is ever asked to produce or paraphrase.

CRAFT NOTE for whoever picks this up: the actual resource text below is a
standard, well-known, publicly-published baseline (988, Crisis Text Line) -
real and correct, but a placeholder for the actual craft pass CiC-Program-
Spec.md SS8 calls for ("designed to the same craft bar as everything else -
care, not clinic"). This is fine for stage-5's purpose (proving the
append-by-code MECHANISM, never conditioned on the voice's own generation
succeeding) against a fixture world that never opens to a real participant -
it is NOT a finished, Mark-approved participant-facing text. Flag this
again in BUILD-HANDOFF before any world that actually opens ships this
literal text.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class CrisisResources:
    track: str  # "A" (acute) - Track B (harmful-dynamic) does not append these
    text: str


ACUTE_DISTRESS_RESOURCES = CrisisResources(
    track="A",
    text=(
        "If you are in crisis or thinking about suicide, you can reach the 988 Suicide & Crisis Lifeline "
        "any time, day or night - call or text 988 in the US, or chat at 988lifeline.org. You can also "
        "text HOME to 741741 to reach the Crisis Text Line. If you are outside the US, "
        "findahelpline.com lists crisis lines by country. You do not have to be in danger to reach out."
    ),
)


def resources_for_signal(signal: str) -> CrisisResources | None:
    """Only ACUTE_DISTRESS gets a resources block - Track B (HARMFUL_DYNAMIC_
    SIGNAL) is a dependency dynamic, not a crisis, and check_in_turn
    (AMBIGUOUS_LOW_CONFIDENCE) is deliberately softer than the full safety
    turn (Artifact-4 SS3 rule 2) - resources are Track A's alone."""
    if signal == "ACUTE_DISTRESS":
        return ACUTE_DISTRESS_RESOURCES
    return None


def append_crisis_resources_turn(*, signal: str, stream_text: str | None, stream_failed: bool) -> dict:
    """The literal proof point for the stage-5 gate item "crisis append
    asserted including the empty-stream case": this function's return does
    NOT depend on stream_text's content or on stream_failed - only on
    signal. A caller passes whatever the voice's companion generation call
    actually produced (real text, empty text because the stream yielded
    zero tokens, or None because the call errored outright) and the
    resources still append identically either way - this is what "appended
    by code, never conditioned on a model call succeeding" means as a
    property that's actually checkable, not just asserted.

    Purposely takes no client and makes no call itself - the caller
    (engine.m4.turn.run_turn) is the only place a real stream is attempted;
    this function is pure so the empty-stream case is testable without any
    mock at all, the same "pure decision, separate from the live call"
    split as engine.m5.routing/live_calls.
    """
    resources = resources_for_signal(signal)
    if resources is None:
        return {"kind": "safety", "text": None, "resources_appended": False}
    empty_stream = stream_failed or not stream_text or not stream_text.strip()
    return {"kind": "safety", "text": resources.text, "resources_appended": True, "empty_stream": empty_stream}
