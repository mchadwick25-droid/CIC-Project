"""The Facilitator's own turns, owned by CODE - real, tested routing
outcomes, never a model's improvisation.

Same discipline as engine.m4.crisis_resources, and for the same reason: the
Facilitator speaks for the system, not for a world, so its words are not a
model's to compose and not a world's to hold. A fixed table, never a prompt.

SYSTEM_NATURE, CHECK_IN, DEPENDENCY_CHECK, and both _ETIC_TEXT entries are
this module's own approved participant-facing text for those routing
outcomes, checked against `CiC_L3D_Facilitator_Governance_V3.6/V3.7` and
`CiC-Program-Spec.md` SS71/76-77/210.

DOOR gives the conversation screen its first-ever opening line -
`"door"` has been a valid facilitator_turn kind in engine.m4.events since
the event catalog was written, but nothing emitted one before this.

DEPENDENCY_CHECK's `{representative_name}` slot (and DOOR's
`{representative_name}`/`{role_label}`) are filled at call time from
`world.frame["representative"]["name"]`/`["role_label"]` - the same
registry-authored fields records/worlds.yaml carries per world (compiled
into compiled/frame.json by engine.m2.builders.build_frame_json) and
already used for the doorway screen. The Facilitator names itself plainly
as "the Facilitator" - no invented persona name for the Facilitator itself
- while the Representative is named by its own registry name, so the
participant can tell the two presences apart in the one moment they speak
in the same beat (SS4.3a).

DOOR's (and TABLE_DOOR's) world-name slot sources
`registry[world_key]["card_name"]`, not `world.frame["display_name"]`: the
two diverge for most built worlds (e.g. ijc's display_name "Imperial and
Juridical Christianity" vs. its card_name "Church and Empire", the name
every other participant-facing surface actually uses), and the Facilitator's
own words should align with the text the world uses everywhere else. See
door_turn's own docstring for the fallback rule.

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

from engine.m4 import citation_cards


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
        "an answer, each claim in it is checked to make sure its words come from the record it names. "
        "The record itself was checked against the sources when the world was built. Where the record "
        "is silent, the voice is built to say so, not to fill the gap. It isn't a person, it isn't the "
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
        "honest. You're about to speak with {representative_name}, {role_label} of {world_name}. Ask "
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
# design). The voice does not speak alongside this turn either - it stands
# alone, same as Track A's own crisis turn. Written to read correctly
# either way: "you're welcome to keep talking with {representative_name}"
# already meant the NEXT message, not this one.
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


def door_turn(*, representative_name: str, role_label: str, world_name: str) -> dict:
    """representative_name/role_label come from world.frame (registry-
    authored, compiled by engine.m2.builders.build_frame_json) - the same
    fields the doorway screen already showed before the participant clicked
    "Begin", not composed here.

    world_name is deliberately NOT world.frame["display_name"] - that field
    is the registry's scholarly name (e.g. "Imperial and Juridical
    Christianity"), never spoken elsewhere in plain voice; Arrival only
    surfaces it as a small, secondary "studied as..." line. Every other
    participant-facing surface (homepage tile, Atlas card, Arrival's own
    kicker) names the world by its registry card_name instead (e.g. "Church
    and Empire"), and the Facilitator's own words should align with that
    text - so callers pass registry[world_key]["card_name"], falling back
    to display_name only for an entry that has none (the fix fixture)."""
    text = DOOR.text.format(representative_name=representative_name, role_label=role_label, world_name=world_name)
    return {"kind": DOOR.kind, "text": text}


def etic_turn(out_of_scope_class: str) -> dict:
    text = _ETIC_TEXT.get(out_of_scope_class)
    if text is None:
        raise KeyError(
            f"no etic text for out_of_scope class {out_of_scope_class!r} - "
            f"routing only reaches etic_turn for {sorted(_ETIC_TEXT)}"
        )
    return {"kind": "threshold", "text": text}


def limit_turn(text: str) -> dict:
    """A pause at a limit that can be lifted: the words come from the
    caller, and the sitting stays open."""
    return {"kind": "limit", "text": text}


CAP_CLOSE_TEXT = "This is the Facilitator. This sitting has reached its limit for now. Nothing in it is lost."

SESSION_CAP = FacilitatorTurn(kind="close", text=CAP_CLOSE_TEXT)


def session_cap_turn(representative_name: str, limit_text: str | None = None) -> dict:
    """The sitting's turn cap, reached on a message that is not a crisis. One
    plain line serves every limit. With the Go Deeper module on, limit_text is
    the module's own line and the sitting stays open; without it the sitting
    closes with this one. representative_name is kept so callers do not change."""
    if limit_text is not None:
        return limit_turn(limit_text)
    return {"kind": SESSION_CAP.kind, "text": SESSION_CAP.text}


DAILY_CAP = FacilitatorTurn(kind="close", text=CAP_CLOSE_TEXT)


def daily_cap_turn(limit_text: str | None = None) -> dict:
    """The visitor's daily message cap, reached on a message that is not a
    crisis. Names no Representative, so the interview and the Table share it."""
    if limit_text is not None:
        return limit_turn(limit_text)
    return {"kind": DAILY_CAP.kind, "text": DAILY_CAP.text}


# --- Table variants (Artifact-7 SS1-2; C1: fixed
# templates parameterized by the seated worlds, never a live facilitator
# generation). DRAFT TEXT, not yet approved. The interview
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
    representative_name/role_label straight from that world's compiled
    frame.json and world_name per door_turn's own card_name/display_name
    rule - the same registry-authored fields the interview's door_turn
    fills its slots from, composed here only with punctuation."""
    parts = [f"{s['representative_name']}, {s['role_label']} of {s['world_name']}" for s in seated]
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


TABLE_SESSION_CAP = FacilitatorTurn(kind="close", text=CAP_CLOSE_TEXT)


def table_session_cap_turn(representative_names: list[str], limit_text: str | None = None) -> dict:
    """The Table's turn cap: the same one plain line as the interview's. The
    names are kept so callers do not change."""
    if limit_text is not None:
        return limit_turn(limit_text)
    return {"kind": TABLE_SESSION_CAP.kind, "text": TABLE_SESSION_CAP.text}


TABLE_SEAT_CORRECTION = FacilitatorTurn(
    kind="seat_correction",
    text=(
        "This is the Facilitator, stepping in for a moment - {representative_name}'s last answer didn't "
        "hold together the way it should have, so I'm setting it aside rather than passing it on to you. "
        "Ask again, or bring another voice into it - the Table is still open."
    ),
)


def table_seat_correction_turn(representative_name: str) -> dict:
    """The seat-identity guard's own fallback line:
    engine.m4.seat_identity_guard caught a generated turn writing itself as
    the Facilitator or another seated voice, regenerated once, and caught
    it again - so this voice's own text is never shown
    (engine.api.table_wiring writes that turn's voice_turn event with an
    empty text, same as any other genuinely empty stream; this facilitator
    turn is what the participant actually reads instead).

    Working default copy: the mechanism ships enforcing now, with this
    line standing in until its exact wording is confirmed."""
    return {"kind": TABLE_SEAT_CORRECTION.kind, "text": TABLE_SEAT_CORRECTION.text.format(representative_name=representative_name)}


TABLE_SEAT_CUT = FacilitatorTurn(
    kind="seat_correction",
    text=(
        "This is the Facilitator, stepping in for a moment - {representative_name} began speaking as if another "
        "voice at the Table, so I have stopped that answer there. What came before that point stands. Ask again, "
        "or bring another voice into it - the Table is still open."
    ),
)


def table_seat_cut_turn(representative_name: str) -> dict:
    """The streamed Table turn's guard line: the seat-identity guard caught a
    sentence after earlier sentences of the same answer were already shown,
    so the answer ends at its last shown sentence and this line follows it
    (System Hub decision 38)."""
    return {"kind": TABLE_SEAT_CUT.kind, "text": TABLE_SEAT_CUT.text.format(representative_name=representative_name)}


VOICE_REJECTED = FacilitatorTurn(
    kind="grounding_correction",
    text=(
        "This is the Facilitator, stepping in for a moment - {representative_name}'s last answer didn't "
        "hold together the way it should have, so I'm setting it aside rather than passing it on to you. "
        "Ask again, or ask something else - I'm still here."
    ),
)


def voice_rejected_turn(representative_name: str) -> dict:
    """The interview-mode analog of table_seat_correction_turn above, for
    a generated voice turn that hard-fails the uncited-claims enforcement
    paragraph-unit check (wholly_uncited_paragraph or neighbour_named),
    survives one named regeneration, and still hard-fails (the voice
    event's enforcement-exhausted flag is set, and that turn's own text is
    deliberately empty, the same convention the seat-identity guard's
    exhausted flag sets). Interview mode has no other seats to "bring
    into it" the way the Table line closes, so this is new, approved
    wording, not a reuse of TABLE_SEAT_CORRECTION."""
    return {"kind": VOICE_REJECTED.kind, "text": VOICE_REJECTED.text.format(representative_name=representative_name)}


def bridge_turn(terms: list[dict], fleet: dict[str, dict] | None = None) -> tuple[dict, str]:
    """Returns (facilitator_event, underlying_subject).

    The Facilitator speaks the modern sense; the voice receives the term-free
    underlying subject and never sees the participant's modern word
    (Program-Spec SS77). Both strings come from the fleet's own modern_term
    record - this function composes nothing.

    fleet resolves each fired term's own citation_cards.resolve_source_card
    - modern_sense, sources, and (a modern_term's own extra field)
    distinguishing_claim, exactly the same card shape every other cited
    record already gets - so a caller has something to show as a real,
    sourced card, not only the prose sentence above. `fleet` is the same
    dict every caller already has in scope (load_fleet_records()), passed
    through rather than reloaded here, since a modern_term's own sources[]
    point at fleet source records (_fleet.source.*), not this world's own
    repository. Optional: a caller may omit it, leaving
    facilitator_event["modern_terms"] as [] - the prose sentence alone is
    still a complete, correct bridge turn."""
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
    modern_term_cards = [
        card for t in terms
        if (card := citation_cards.resolve_source_card(t["id"], fleet)) is not None
    ] if fleet else []
    return {"kind": "bridge", "text": text, "modern_terms": modern_term_cards}, subjects
