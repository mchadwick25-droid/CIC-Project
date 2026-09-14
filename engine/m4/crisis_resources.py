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
`reference/L3D-Encounter-Methodology/CiC_L3D_RelationalSafety_ResourceNaming_Decision_Options.md`) - a
portfolio-level decision this module's text simply hadn't inherited yet.
The text below is Option A-compliant, drafted from
`reference/L3D-Encounter-Methodology/CiC_L3D_AcuteDistress_HarmfulDynamic_Mechanism_Proposal_DRAFT.md` SS5.1's
own A1 script.

The `{representative_name}` slot is filled at call time by engine.m4.turn
from `world.frame["representative"]["name"]` - the same registry-authored
name records/worlds.yaml carries per world, compiled into
compiled/frame.json (engine.m2.builders.build_frame_json) and already used
for the doorway portrait caption. Mark's own ruling: the Facilitator names
itself plainly as "the Facilitator" - no invented persona name for the
Facilitator itself - while the Representative is named by its own registry
name, so the participant can tell the two presences apart in the one
moment they speak in the same beat (SS4.3a).

STATUS, 2026-08-24 (later same day): A2 (explicit-plan/imminent-risk
escalation) and the continuation turn (a second Track A firing in the same
session) are wired now too. resources_for_signal selects among the three
using acute_level (Artifact-4 SS1's Call A schema field) and already_fired
(True once engine.m4.projection's SessionState.safety.track_a_last is not
None - i.e. an earlier turn this session already recorded a Track A
safety_state). already_fired always wins: SS4.4/SS4.6's "sustained
attention" means a later turn gets the lighter continuation regardless of
whether it re-reads as a1 or a2. This reads existing state (the accumulator
already writes track_a_last - see engine.m5.safety_accumulation) and adds
no new routing: engine.m5.routing still decides only whether a turn is a
safety_turn at all, never which of the three scripts it gets.

ACUTE_DISTRESS_CONTINUATION deliberately drops SS5.1's own bracketed
"[brief, concrete acknowledgment of what the participant just said]" - this
module composes nothing and calls no model (the one guarantee this file
exists to keep), so it cannot generate a message-specific acknowledgment
without either a live call (forbidden for this text) or echoing the
participant's raw words back verbatim at exactly the highest-stakes moment
this architecture has (untested, and not what SS5.1 itself proposed). The
continuation line below is generic on purpose; flagging this rather than
silently dropping the bracket unremarked, since it is a real simplification
of the approved draft, not just a formatting choice.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class CrisisResources:
    track: str  # "A" (acute) - Track B (harmful-dynamic) does not append these
    text: str


ACUTE_DISTRESS_RESOURCES = CrisisResources(
    track="A",
    text=(
        "I want to step in for a moment - this is the Facilitator speaking, not {representative_name}. "
        "What you just told me matters, and I don't want to let it pass by without saying something "
        "honest about it.\n\n"
        "This conversation is built to give you a real meeting with a historical world, and it can hold "
        "a lot - hard questions, hard history, real grief. But it isn't built to be the place that "
        "carries you through what you're describing right now, and I'd rather tell you that plainly "
        "than let you find it out the hard way.\n\n"
        "Please reach out to someone real - a person you trust, a crisis line, or emergency services "
        "where you are - before we go any further.\n\n"
        "You're not being sent away, and you haven't done anything wrong by telling me this. If you "
        "want to keep talking - to me, right now, or back with {representative_name} when you're ready "
        "- that's completely open. I just didn't want to stay quiet about what you said."
    ),
)


ACUTE_DISTRESS_A2 = CrisisResources(
    track="A",
    text=(
        "I need to stop here and be straightforward with you - this is the Facilitator speaking. What "
        "you just described is something I take completely seriously, and it's beyond anything I can "
        "responsibly hold with you inside this conversation.\n\n"
        "Please reach out to someone real right now - a person you trust, a crisis line, or emergency "
        "services where you are - before we go any further.\n\n"
        "I'm not going anywhere while you decide what to do next, and neither is this conversation - it "
        "will still be here. But right now, the most important thing isn't the historical world we've "
        "been exploring together. It's what you just told me."
    ),
)

ACUTE_DISTRESS_CONTINUATION = CrisisResources(
    track="A",
    text="I'm still right here with you. The offer I made a moment ago still stands, whenever you're ready for it.",
)


def resources_for_signal(signal: str, *, acute_level: str, already_fired: bool) -> CrisisResources | None:
    """Only ACUTE_DISTRESS gets a resources block - Track B (HARMFUL_DYNAMIC_
    SIGNAL) is a dependency dynamic, not a crisis, and check_in_turn
    (AMBIGUOUS_LOW_CONFIDENCE) is deliberately softer than the full safety
    turn (Artifact-4 SS3 rule 2) - resources are Track A's alone.

    already_fired outranks acute_level: SS4.4's "sustained attention" is a
    property of the SESSION (has Track A already spoken once), not of this
    turn's own escalation reading - a session already in a heightened-
    attention state gets the lighter continuation turn even if this
    particular message reads a2."""
    if signal != "ACUTE_DISTRESS":
        return None
    if already_fired:
        return ACUTE_DISTRESS_CONTINUATION
    if acute_level == "a2":
        return ACUTE_DISTRESS_A2
    return ACUTE_DISTRESS_RESOURCES


def append_crisis_resources_turn(
    *, signal: str, stream_text: str | None, stream_failed: bool, representative_name: str,
    acute_level: str, already_fired: bool,
) -> dict:
    """The literal proof point for the stage-5 gate item "crisis append
    asserted including the empty-stream case": this function's return does
    NOT depend on stream_text's content or on stream_failed - only on
    signal (and now acute_level/already_fired, still never on the stream).
    A caller passes whatever the voice's companion generation call actually
    produced (real text, empty text because the stream yielded zero tokens,
    or None because the call errored outright) and the resources still
    append identically either way - this is what "appended by code, never
    conditioned on a model call succeeding" means as a property that's
    actually checkable, not just asserted.

    Purposely takes no client and makes no call itself - the caller
    (engine.m4.turn.run_turn) is the only place a real stream is attempted;
    this function is pure so the empty-stream case is testable without any
    mock at all, the same "pure decision, separate from the live call"
    split as engine.m5.routing/live_calls.

    representative_name comes from world.frame["representative"]["name"]
    (records/worlds.yaml's own registry entry) - the same name every
    world's doorway portrait already carries, not composed here.

    acute_level ("a1"|"a2", Artifact-4 SS1) and already_fired (True once
    SessionState.safety.track_a_last is not None) select among A1/A2/
    continuation (resources_for_signal, above). Both required, no default -
    a caller that forgets one should get a TypeError, not a silently-wrong
    a1-always fallback at exactly the place this file exists to keep
    honest.
    """
    resources = resources_for_signal(signal, acute_level=acute_level, already_fired=already_fired)
    if resources is None:
        return {"kind": "safety", "text": None, "resources_appended": False}
    text = resources.text.format(representative_name=representative_name)
    empty_stream = stream_failed or not stream_text or not stream_text.strip()
    return {"kind": "safety", "text": text, "resources_appended": True, "empty_stream": empty_stream}
