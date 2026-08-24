"""The Facilitator's own turns, owned by CODE - the four routing actions
that were real, tested routing outcomes with nothing behind them.

Same discipline as engine.m4.crisis_resources, and for the same reason: the
Facilitator speaks for the system, not for a world, so its words are not a
model's to compose and not a world's to hold. A fixed table, never a prompt.

CRAFT NOTE, and it is the same one crisis_resources carries. The text below
is honest, minimal and correct in what it claims, and it is NOT a finished,
Mark-approved participant-facing text. It exists so that a participant who
asks "are you an AI?" gets an answer instead of a facilitator note pointing
at a file path in a repository - which is what they got before this module,
on four of the seven routes the gate can take. Every string here is a
placeholder for the craft pass CiC-Program-Spec.md SS8 calls for ("designed
to the same craft bar as everything else - care, not clinic"). Flag this in
BUILD-HANDOFF before any world that actually opens ships these words.

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
        "Yes - you are talking to an AI. Here is how it works, plainly. Each world you can speak with "
        "is built from a fixed set of records drawn from sources that survive from that time and place, "
        "and the voice answering you may only say what those records carry. Every specific claim it "
        "makes is checked against the record it came from before you see it; anything it cannot ground, "
        "it is supposed to tell you it does not have rather than fill in. It is not a person, it is not "
        "the church, and it does not speak for anyone living."
    ),
)

# Rule 2: "a softer, safety-aware acknowledgment short of the full safety
# turn (no resources appended, no track opened)". Softer is the whole point -
# the safety call itself was uncertain, so this must not treat the person as
# a case, and must not treat the message as ordinary either.
CHECK_IN = FacilitatorTurn(
    kind="safety",
    text=(
        "Before we go on - that landed as though it might be carrying something real, and I would rather "
        "ask than assume. If it was, you can say so plainly here and we will take it at that weight. If "
        "it was not, say so and we will pick up where we were."
    ),
)

# Program-Spec SS8: Track B is "harmful-dynamic/dependency, accumulating
# across the session" - a dependency dynamic, not a crisis, so no resources
# (engine.m4.crisis_resources.resources_for_signal returns None for it by
# design) and "an explicit continue path back to the voice".
DEPENDENCY_CHECK = FacilitatorTurn(
    kind="safety",
    text=(
        "One thing worth saying out loud: this is a conversation with a set of records, and it cannot "
        "know you, miss you, or be owed anything by you. That is not a rebuke - it is the honest shape "
        "of what you are talking to, and it seemed worth naming rather than letting it blur. We can "
        "keep going whenever you would like."
    ),
)

# Rule 5: out_of_scope in {later_age, other_tradition} AND pressed - the
# participant has now asked twice, so the in-world answer has already been
# given and declined. The etic turn steps outside the world deliberately,
# which is the one place the Facilitator may speak about a world rather than
# let it speak for itself.
_ETIC_TEXT = {
    "later_age": (
        "You are asking about something that happened after this world's own horizon closed, so the "
        "voice cannot answer it from inside - it would have to invent. Stepping outside the world for "
        "a moment: what you are asking about belongs to a later period than the one these records come "
        "from, and this project deliberately does not have a world speak past its own end."
    ),
    "other_tradition": (
        "You are asking this world about a tradition that is not its own. It can tell you what it held "
        "and what it argued with, but it cannot speak for anyone else - and a world describing its "
        "neighbours in its own words is testimony about itself, not about them. If you want that other "
        "tradition's account, it needs its own voice, not this one's."
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


def dependency_check_turn() -> dict:
    return {"kind": DEPENDENCY_CHECK.kind, "text": DEPENDENCY_CHECK.text, "resources_appended": False}


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
        f"A word in your question - {displays} - came after this world's own time, so the voice will not "
        f"be handed it. In our sense: {senses} What it can speak to is the thing underneath the word, "
        "which is what I am passing to it."
    )
    return {"kind": "bridge", "text": text}, subjects
