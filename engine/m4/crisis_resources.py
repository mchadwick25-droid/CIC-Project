"""Crisis resources appended by CODE, never recalled by a model (Build-
Blueprint.md principle 5, CiC-Program-Spec.md SS8/O5: "crisis resources are
appended by code, never recalled by a model"). This is the one place that
text exists in this codebase - a fixed dict, not a prompt, not something any
model call is ever asked to produce or paraphrase.

STATUS, 2026-08-24: ACUTE_DISTRESS_RESOURCES.text below is Mark-approved
participant-facing text, replacing the earlier placeholder that named 988
and the Crisis Text Line by number. That placeholder was never actually
correct against this project's own standing decision: Mark ruled on
2026-08-05 (`Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`,
CO-022) that the Facilitator's crisis redirect names no specific
organization, hotline, or number ("Option A" of
`CiC_L3D_RelationalSafety_ResourceNaming_Decision_Options.md`) - a
portfolio-level decision this module's text simply hadn't inherited yet.
The text below is Option A-compliant, drafted from
`CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md` SS5.1's
own A1 script.

Two things not yet finished, flagged rather than hidden:

- "[Representative]" is a literal, intentional placeholder - nothing here
  threads a world's display name in yet. A separate, small code change
  (a parameter on append_crisis_resources_turn and its call site in
  engine.m4.turn), raised but not done in this pass.
- This is SS5.1's "A1" register (initial disclosure) only. SS5.1 also
  drafts a more direct "A2" register for explicit-plan/imminent-risk
  escalation and a lighter "continuation" turn for a second Track A firing
  in the same session - both approved in wording, neither wired, because
  append_crisis_resources_turn has no acute_level or session-state
  parameter to select between them yet. A1's text is used for every acute
  signal today, which is honest but not the fuller intended shape.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class CrisisResources:
    track: str  # "A" (acute) - Track B (harmful-dynamic) does not append these
    text: str


ACUTE_DISTRESS_RESOURCES = CrisisResources(
    track="A",
    text=(
        "I want to step in for a moment - this is the Facilitator speaking, not [Representative]. What "
        "you just told me matters, and I don't want to let it pass by without saying something honest "
        "about it.\n\n"
        "This conversation is built to give you a real meeting with a historical world, and it can hold "
        "a lot - hard questions, hard history, real grief. But it isn't built to be the place that "
        "carries you through what you're describing right now, and I'd rather tell you that plainly "
        "than let you find it out the hard way.\n\n"
        "Please reach out to someone real - a person you trust, a crisis line, or emergency services "
        "where you are - before we go any further.\n\n"
        "You're not being sent away, and you haven't done anything wrong by telling me this. If you "
        "want to keep talking - to me, right now, or back with [Representative] when you're ready - "
        "that's completely open. I just didn't want to stay quiet about what you said."
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
