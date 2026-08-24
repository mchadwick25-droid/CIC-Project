"""The Facilitator's own turns, owned by CODE - the four routing actions
that were real, tested routing outcomes with nothing behind them.

Same discipline as engine.m4.crisis_resources, and for the same reason: the
Facilitator speaks for the system, not for a world, so its words are not a
model's to compose and not a world's to hold. A fixed table, never a prompt.

STATUS, 2026-08-24: SYSTEM_NATURE, CHECK_IN, DEPENDENCY_CHECK, and both
_ETIC_TEXT entries are Mark-approved participant-facing text - picked from
drafted options after an analysis pass against CiC_L3D_Facilitator_
Governance_V3.6/V3.7 and CiC-Program-Spec.md SS71/76-77/210. This replaces
the earlier placeholder text a participant asking "are you an AI?" (and
three of the other six routes) used to receive.

DEPENDENCY_CHECK's `{representative_name}` slot is filled at call time by
engine.m4.turn from `world.frame["representative"]["name"]` - the same
registry-authored name/role_label pair records/worlds.yaml carries per
world (compiled into compiled/frame.json by engine.m2.builders.
build_frame_json) and already used for the doorway portrait caption. Mark's
own ruling: the Facilitator names itself plainly as "the Facilitator" - no
invented persona name for the Facilitator itself - while the Representative
is named by its own registry name, so the participant can tell the two
presences apart in the one moment they speak in the same beat (SS4.3a).

One thing below is NOT yet finished, flagged rather than hidden:

- bridge_turn's frame now deliberately speaks the term's own
  `underlying_subject` to the participant, not only to the voice - a
  considered visibility change Mark approved the same day this note was
  written, not an oversight of the general "the Facilitator does not
  narrate its own mechanics" rule.

What is NOT placeholder, and must not be rewritten as though it were: the
bridge turn speaks the modern term's own `modern_sense` and hands the voice
its own `underlying_subject`, both straight out of the fleet's modern_term
record. That is authored fleet data doing exactly the job it was authored
for (Artifact-4 SS3 rule 4, Program-Spec SS77), not this module's prose.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class FacilitatorTurn:
    kind: str  # one of engine.m4.events' facilitator_turn kinds
    text: str


# Artifact-4 SS3 rule 3, and Program-Spec SS76 in as many words: "The
# Facilitator answers 'are you an AI?' plainly - we use AI, and here is how."
# Plainly means plainly: what it is, what it may not do, and where the words
# come from, with no reassurance the system has not earned.
SYSTEM_NATURE = FacilitatorTurn(
    kind="threshold",
    text=(
        "Yes - we use AI here, and I'd rather tell you plainly than let you wonder. Each world you can "
        "speak with is built from a fixed set of records - sources that actually survive from that time "
        "and place - and the voice answering you may only say what those records carry. Before you see "
        "an answer, every specific claim in it is checked against the record it came from; what it can't "
        "ground, it's built to tell you it doesn't have, not to invent. It isn't a person, it isn't the "
        "church, and it doesn't speak for anyone living.\n\n"
        "That's the honest shape of it - whenever you're ready, let's keep going."
    ),
)

# Rule 2: "a softer, safety-aware acknowledgment short of the full safety
# turn (no resources appended, no track opened)". Softer is the whole point -
# the safety call itself was uncertain, so this must not treat the person as
# a case, and must not treat the message as ordinary either.
CHECK_IN = FacilitatorTurn(
    kind="safety",
    text=(
        "Can I check something before we go on? What you just said could have been about something real "
        "and hard, or it could have just been a way of speaking - and I didn't want to guess which. If "
        "it's the first, say so plainly and I'll take it that way. If not, just say so and we'll pick up "
        "right where we were."
    ),
)

# Program-Spec SS8: Track B is "harmful-dynamic/dependency, accumulating
# across the session" - a dependency dynamic, not a crisis, so no resources
# (engine.m4.crisis_resources.resources_for_signal returns None for it by
# design) and "an explicit continue path back to the voice".
DEPENDENCY_CHECK = FacilitatorTurn(
    kind="safety",
    text=(
        "I want to say something gently, before we go on - this is the Facilitator, not "
        "{representative_name}. Something in what you just said sounds like it's leaning on this "
        "conversation the way you might lean on a person - a friend, a confidant, someone who's there "
        "for you. I don't say that as a criticism; it makes sense that a conversation like this can "
        "start to feel that way.\n\n"
        "But I want to be honest with you about what this actually is: {representative_name} is a way "
        "of meeting a historical world, not a person who can be there for you the way a real friend, "
        "counselor, or community can. I'd rather say that plainly than let you find it out the harder "
        "way.\n\n"
        "The people already in your life - or, if none feel reachable right now, a crisis line or other "
        "real human support - are the ones who can actually be there for you the way this can't.\n\n"
        "None of this means the conversation has to end, or that you did anything wrong. You're welcome "
        "to keep talking with {representative_name}. I just wanted to say this honestly, the way I'd "
        "want someone to say it to me."
    ),
)

# Rule 5: out_of_scope in {later_age, other_tradition} AND pressed - the
# participant has now asked twice, so the in-world answer has already been
# given and declined. The etic turn steps outside the world deliberately,
# which is the one place the Facilitator may speak about a world rather than
# let it speak for itself.
_ETIC_TEXT = {
    "later_age": (
        "That question reaches past where this world's own witnesses stop. Answering it honestly would "
        "mean inventing what happened later, not remembering it - and this voice only speaks from inside "
        "what it actually lived through. That's not a refusal so much as the honest edge of it: there's "
        "a real period this world simply never reached."
    ),
    "other_tradition": (
        "You're asking this world about a tradition that isn't its own. It can tell you what it held and "
        "what it argued with, but it can't speak for anyone else - a world describing its neighbours in "
        "its own words is testimony about itself, not about them. If you want that other tradition's own "
        "account, it needs its own voice, not this one's."
    ),
}


def system_nature_turn() -> dict:
    return {"kind": SYSTEM_NATURE.kind, "text": SYSTEM_NATURE.text}


def check_in_turn() -> dict:
    """No resources, no track opened - Artifact-4 SS3 rule 2, and
    crisis_resources.resources_for_signal already refuses to hand any over
    for AMBIGUOUS_LOW_CONFIDENCE, so the two modules agree by construction
    rather than by comment."""
    return {"kind": CHECK_IN.kind, "text": CHECK_IN.text, "resources_appended": False}


def dependency_check_turn(representative_name: str) -> dict:
    """representative_name comes from world.frame["representative"]["name"]
    (records/worlds.yaml's own registry entry) - the same name every world's
    doorway portrait already carries, not composed here."""
    text = DEPENDENCY_CHECK.text.format(representative_name=representative_name)
    return {"kind": DEPENDENCY_CHECK.kind, "text": text, "resources_appended": False}


def etic_turn(out_of_scope_class: str) -> dict:
    text = _ETIC_TEXT.get(out_of_scope_class)
    if text is None:
        raise KeyError(
            f"no etic text for out_of_scope class {out_of_scope_class!r} - "
            f"routing only reaches etic_turn for {sorted(_ETIC_TEXT)}"
        )
    return {"kind": "threshold", "text": text}


def bridge_turn(terms: list[dict]) -> tuple[dict, str]:
    """Returns (facilitator_event, underlying_subject).

    The Facilitator speaks the modern sense; the voice receives the term-free
    underlying subject and never sees the participant's modern word
    (Program-Spec SS77). Both strings come from the fleet's own modern_term
    record - this function composes nothing.
    """
    if not terms:
        raise ValueError("bridge_turn called with no modern_term records - routing only reaches it when a term fired")
    senses = " ".join(t["modern_sense"].strip() for t in terms if t.get("modern_sense"))
    subjects = " ".join(t["underlying_subject"].strip() for t in terms if t.get("underlying_subject"))
    displays = ", ".join(sorted({d for t in terms for d in (t.get("display_terms") or [])}))
    text = (
        f"Something in your question - {displays} - belongs to a later way of speaking than this world "
        f"knew. In our sense: {senses} Let me translate that into terms this world would actually "
        f"recognize before I put it to the voice: {subjects}"
    )
    return {"kind": "bridge", "text": text}, subjects
