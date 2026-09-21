"""The Facilitator's own turns, owned by CODE - the four routing actions
that were real, tested routing outcomes with nothing behind them.

Same discipline as engine.m4.crisis_resources, and for the same reason: the
Facilitator speaks for the system, not for a world, so its words are not a
model's to compose and not a world's to hold. A fixed table, never a prompt.

SYSTEM_NATURE, CHECK_IN, DEPENDENCY_CHECK, and both
_ETIC_TEXT entries are approved participant-facing text - picked from
drafted options after an analysis pass against CiC_L3D_Facilitator_
Governance_V3.6/V3.7 and CiC-Program-Spec.md SS71/76-77/210. This replaces
the earlier placeholder text a participant asking "are you an AI?" (and
three of the other six routes) used to receive.

DOOR is also approved - picked
from a two-draft choice (the fuller "door metaphor" draft was
not carried into code) logged in Ministry/Technology/
CiC_FrontEnd_Decision_Log.md. Closes a different gap than the six routing
turns above: those replace placeholder text an existing route already
produced, where DOOR gives the conversation screen its first-ever opening
line - `"door"` has been a valid facilitator_turn kind in engine.m4.events
since the event catalog was written, but nothing ever emitted one.

DEPENDENCY_CHECK's `{representative_name}` slot (and DOOR's
`{representative_name}`/`{role_label}`/`{display_name}`) are filled at
call time from `world.frame["representative"]["name"]`/`["role_label"]`
and `world.frame["display_name"]` - the same registry-authored fields
records/worlds.yaml carries per world (compiled into compiled/frame.json
by engine.m2.builders.build_frame_json) and already used for the doorway
screen. The Facilitator names itself plainly as "the
Facilitator" - no invented persona name for the Facilitator itself - while
the Representative is named by its own registry name, so the participant
can tell the two presences apart in the one moment they speak in the same
beat (SS4.3a).

One thing below is NOT yet finished, flagged rather than hidden:

- bridge_turn's frame now deliberately speaks the term's own
  `underlying_subject` to the participant, not only to the voice - a
  considered visibility change, not an oversight of the general "the Facilitator does not
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

# Program-Spec SS71: "the one voice belonging to no world, visible at door,
# thresholds, and close." The doorway SCREEN (Doorway.tsx) already gives the
# fuller orientation - mission, thinness, living-tradition distinction,
# starter questions - before a participant ever clicks "Begin"; this turn's
# job is the handoff into the conversation itself, kept short on purpose
# (spec principle 14, "witness, not a home": the Facilitator does minimal
# scaffolding here, not a warm monologue the doorway already covered).
DOOR = FacilitatorTurn(
    kind="door",
    text=(
        "Welcome - I'm the Facilitator. I don't belong to any world; I'm just here to keep this space "
        "honest. You're about to speak with {representative_name}, {role_label} of {display_name}. Ask "
        "anything you like - {representative_name} answers only from what's actually known of this "
        "world, and will tell you plainly when the record runs out."
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
# design). Amendment 2026-09-20: the voice no longer speaks alongside this
# turn either - it stands alone, same as Track A's own crisis turn. Written
# to read correctly either way: "you're welcome to keep talking with
# {representative_name}" already meant the NEXT message, not this one.
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


def door_turn(*, representative_name: str, role_label: str, display_name: str) -> dict:
    """All three slots come from world.frame (registry-authored, compiled by
    engine.m2.builders.build_frame_json) - the same fields the doorway
    screen already showed before the participant clicked "Begin", not
    composed here."""
    text = DOOR.text.format(representative_name=representative_name, role_label=role_label, display_name=display_name)
    return {"kind": DOOR.kind, "text": text}


def etic_turn(out_of_scope_class: str) -> dict:
    text = _ETIC_TEXT.get(out_of_scope_class)
    if text is None:
        raise KeyError(
            f"no etic text for out_of_scope class {out_of_scope_class!r} - "
            f"routing only reaches etic_turn for {sorted(_ETIC_TEXT)}"
        )
    return {"kind": "threshold", "text": text}


SESSION_CAP = FacilitatorTurn(
    kind="close",
    text=(
        "This is the Facilitator stepping in - we've reached the end of what one sitting with "
        "{representative_name} is built to hold: ten exchanges.\n\n"
        "I want to be honest with you about why there's a limit, not just that there is one. Every "
        "exchange here is a real, billed call to the model speaking with you - it costs actual money to "
        "run, every time, for every conversation. Ten is where we can hold that line honestly right now.\n\n"
        "This conversation is closed, but nothing in it is lost - it stayed exactly what it was while it "
        "lasted. If it was worth having, and you're able, this project runs on people who support it "
        "directly - churchinconversation.com/support.html has more on that, and what the giving actually "
        "goes toward. We're also working toward a paid option built specifically to let a conversation "
        "like this run longer, for anyone who wants to go deeper than ten exchanges gives.\n\n"
        "Either way, you're welcome to start fresh - with {representative_name} again, or with one of "
        "this project's other worlds and voices."
    ),
)


def session_cap_turn(representative_name: str) -> dict:
    """DRAFT TEXT, not yet approved - see this module's own note
    on what that approval process looks like for every other facilitator
    text here. Wired in now so the mechanism (reference/Redesign-Spec/Artifact-6-
    Operations.md's "per-session turn cap", DECIDABLE default 40, resolved
    to 10) is complete and tested; the copy itself is
    swappable without touching engine.m4.turn's routing.

    Names its own cost honestly - honest about cost, each round adding to
    the cost, still gracious but meant to inspire giving - rather than only
    naming the limit, and points to
    cic-website/support.html, the project's own already-published Get
    Involved page (Faithways Studio, Inc.), rather than inventing new
    giving mechanics here. Deliberately carries no specific dollar figure:
    support.html's own published rate ($2-5/hour) was measured for the
    multi-voice Table experience, not the single-Representative path this
    turn cap governs (engine/m8/live_cost_run.py measured roughly $0.25/hour
    for that path) - a real discrepancy to reconcile before either number
    appears in participant-facing text, not something to paper over here by
    picking one. Also names a future paid option for longer conversations -
    not yet built, stated as a direction, not a
    promise of a date or price.

    representative_name comes from world.frame["representative"]["name"],
    same source and same reason as dependency_check_turn above."""
    text = SESSION_CAP.text.format(representative_name=representative_name)
    return {"kind": SESSION_CAP.kind, "text": text}


# --- Table variants (Artifact-7 SS1-2; C1: fixed
# templates parameterized by the seated worlds, never a live facilitator
# generation). DRAFT TEXT, not yet approved - same wired-now/
# swappable-copy discipline session_cap_turn documents. The interview
# texts above are untouched; a table session simply calls these instead
# where the interview's text names exactly one representative.


def names_or_phrase(names: list[str]) -> str:
    """"Clement", "Clement or Papnoute", "Clement, Papnoute, or Ephrem" -
    for dropping a table's representatives into a text slot that reads
    naturally with an or-joined singular ("this is the Facilitator, not
    Clement or Papnoute"). Used to fill crisis_resources' approved
    {representative_name} slot for a table WITHOUT altering that approved
    text itself."""
    if not names:
        raise ValueError("names_or_phrase needs at least one representative name")
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} or {names[1]}"
    return f"{', '.join(names[:-1])}, or {names[-1]}"


TABLE_DOOR = FacilitatorTurn(
    kind="door",
    text=(
        "Welcome - I'm the Facilitator. I don't belong to any world; I'm just here to keep this space "
        "honest. You've come to a Table with {seated_sentence} - voices from genuinely different ways of "
        "following Jesus, present together. Ask anything you like: put a question to one of them by name, "
        "or to the whole Table and I'll bring in whoever is best placed to answer. Each voice answers "
        "only from what's actually known of its own world, and will tell you plainly when its record "
        "runs out."
    ),
)


def table_door_turn(seated: list[dict]) -> dict:
    """seated: one dict per world in seating order, each carrying
    representative_name/role_label/display_name straight from that world's
    compiled frame.json - the same registry-authored fields the interview's
    door_turn fills its slots from, composed here only with punctuation."""
    parts = [f"{s['representative_name']}, {s['role_label']} of {s['display_name']}" for s in seated]
    if len(parts) == 2:
        seated_sentence = f"{parts[0]}, and {parts[1]}"
    else:
        seated_sentence = f"{'; '.join(parts[:-1])}; and {parts[-1]}"
    return {"kind": TABLE_DOOR.kind, "text": TABLE_DOOR.text.format(seated_sentence=seated_sentence)}


TABLE_DEPENDENCY_CHECK = FacilitatorTurn(
    kind="safety",
    text=(
        "I want to say something gently, before we go on - this is the Facilitator, not one of the "
        "voices at this Table. Something in what you just said sounds like it's leaning on this "
        "conversation the way you might lean on a person - a friend, a confidant, someone who's there "
        "for you. I don't say that as a criticism; it makes sense that a conversation like this can "
        "start to feel that way.\n\n"
        "But I want to be honest with you about what this actually is: the voices here are ways of "
        "meeting historical worlds, not people who can be there for you the way a real friend, "
        "counselor, or community can. I'd rather say that plainly than let you find it out the harder "
        "way.\n\n"
        "The people already in your life - or, if none feel reachable right now, a crisis line or other "
        "real human support - are the ones who can actually be there for you the way this can't.\n\n"
        "None of this means the conversation has to end, or that you did anything wrong. You're welcome "
        "to keep talking with {names_phrase}. I just wanted to say this honestly, the way I'd want "
        "someone to say it to me."
    ),
)


def table_dependency_check_turn(representative_names: list[str]) -> dict:
    text = TABLE_DEPENDENCY_CHECK.text.format(names_phrase=names_or_phrase(representative_names))
    return {"kind": TABLE_DEPENDENCY_CHECK.kind, "text": text, "resources_appended": False}


TABLE_SESSION_CAP = FacilitatorTurn(
    kind="close",
    text=(
        "This is the Facilitator stepping in - we've reached the end of what one sitting at this Table "
        "is built to hold.\n\n"
        "I want to be honest with you about why there's a limit, not just that there is one. Every "
        "turn here is a real, billed call to the model speaking with you - several voices at a Table "
        "means several of them per exchange - and this is where we can hold that line honestly right "
        "now.\n\n"
        "This conversation is closed, but nothing in it is lost - it stayed exactly what it was while "
        "it lasted. If it was worth having, and you're able, this project runs on people who support "
        "it directly - churchinconversation.com/support.html has more on that, and what the giving "
        "actually goes toward.\n\n"
        "Either way, you're welcome to start fresh - at this Table again with {names_phrase}, with any "
        "one of these voices on its own, or with one of this project's other worlds."
    ),
)


def table_session_cap_turn(representative_names: list[str]) -> dict:
    """Same DRAFT status, same honesty-about-cost direction, and the same
    deliberate absence of a dollar figure as session_cap_turn - see its
    docstring; the discrepancy it documents (support.html's published rate
    was measured for the Table, the interview cap's for the single path)
    cuts the other way here and is still unreconciled."""
    text = TABLE_SESSION_CAP.text.format(names_phrase=names_or_phrase(representative_names))
    return {"kind": TABLE_SESSION_CAP.kind, "text": text}


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
