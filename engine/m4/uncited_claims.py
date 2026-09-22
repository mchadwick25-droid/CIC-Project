"""R27 (Decision-Log.md Entry 51, 2026-09-22): every declarative claim
sentence in a voice turn must carry a citation, or be one of a short,
closed allowed-uncited list. Report-only in this build (Rulings-Pending.md
R27) - writes an audit event, never withholds or edits text (same
"reports, never edits" discipline engine.m4.output_check already rests
on); enforcement is a later, separately-ruled, flag-gated PR.

Runs on engine.m4.grounding_net.check_turn's own per-sentence output
(net_result["sentences"]) rather than a second sentence-splitter - two
independent splitters risking disagreement is a real correctness class of
bug this avoids by construction, the same "one implementation, owned
once" discipline engine.prose.claim_markers already follows. Scoped to
verdict == "ok" sentences only: a withheld sentence never reaches the
participant (engine.m4.turn.apply_net drops it), so there is nothing here
to check in one that was never shown.

The three allowed-uncited kinds reuse real, already fleet-calibrated
vocabulary rather than invented heuristics: engine.prose.SCAFFOLD_MARKERS
and SELF_NAMING_MARKER are the exact phrases
engine.m4.grounding_net.verdict_for_sentence already treats as honest-
limit/self-naming scaffolding, calibrated against 17 real live turns per
that module's own docstring.

claim_markers cannot be this module's own overall gate - verified
directly (Decision-Log.md Entry 51), not assumed: it returns nothing for
"Even a broken priest could not block his grace." (one of R26's own two
motivating sentences), because claim_markers was built for a narrower
job with the opposite polarity (empty means skip it; R27 means the
opposite - every declarative sentence needs a citation unless it's one
of the three kinds below). claim_markers is reused only inside kind 3
below, where its real, documented meaning ("no checkable claim") is
exactly the question being asked.
"""
import re

from engine.prose import SCAFFOLD_MARKERS, SELF_NAMING_MARKER, claim_markers

# R26's own new fixed sentence (Rulings-Pending.md R26, Decision-Log.md
# Entry 50), the literal directive text wired into the other_tradition
# first-ask path (engine.m4.turn._other_tradition_directive) - the voice
# is TOLD to say these words, so an exact (case-insensitive) match is the
# right bar here, not a guess.
R26_HONEST_LIMIT_SENTENCE = "our record doesn't mention that christian tradition"

# F1 (reviewer thread fix list, 2026-09-22, after the item-4 live battery):
# the fleet's own real honest-limit forms the battery's offense list
# actually showed - "How it ended among us is not in our record.",
# "Here is the honest limit.", "No rule of ours survives that explains the
# difference." - a closed list local to R27's own detection, deliberately
# NOT added to engine.prose.SCAFFOLD_MARKERS: that vocabulary also feeds
# engine.m4.grounding_net.verdict_for_sentence's own withhold/ok decision
# fleet-wide, and widening it would change more than this check's own
# exemption. Fixed phrases, no model call, same discipline SCAFFOLD_MARKERS
# already sets.
_RECORD_ABSENCE_PHRASES = (
    "not in our record",
    "our record does not",
    "our record is silent",
    "the honest limit",
)
# "survives"/"reached us" negations (fix list's own naming) - a record-
# absence claim doesn't always use one of the fixed phrases above ("No
# rule of ours survives that explains the difference." names nothing
# absent by the word "record" at all). A short-window regex, not a second
# model call: a negator and survives/reached-us within the same clause,
# so a genuine citable claim ("The letter survives in three copies.",
# no negator) is untouched.
_RECORD_ABSENCE_NEGATION = re.compile(
    r"\b(no|none|nothing|not|never)\b[^.!?]{0,40}\b(survives?|survived|reached us|reaches us)\b"
)

_FIRST_PERSON_OPENERS = {
    "i", "i'd", "i've", "i'll", "i'm",
    "we", "we'd", "we've", "we'll", "we're",
    "my", "our",
}
# F2 (same fix list): the opener-only check below misses a conditional
# offer whose MAIN clause is first-person - "If you name the conflict you
# mean, I will tell you plainly..." opens with "If", not "I". A fixed,
# closed set of clause markers, checked anywhere in the sentence rather
# than sentence-initial only; claim_markers(sentence) is still the real
# guard against exempting a sentence that also happens to contain one of
# these words while making a real claim elsewhere in it.
_FIRST_PERSON_CLAUSE_MARKERS = ("i will", "i can", "we will", "we can")

_WORD = re.compile(r"[A-Za-z']+")


def _is_question(sentence: str) -> bool:
    return sentence.rstrip(" \t\"'”’)]").endswith("?")


def _is_honest_limit(sentence_lower: str) -> bool:
    if R26_HONEST_LIMIT_SENTENCE in sentence_lower:
        return True
    if SELF_NAMING_MARKER in sentence_lower:
        return True
    if any(marker in sentence_lower for marker in SCAFFOLD_MARKERS):
        return True
    if any(phrase in sentence_lower for phrase in _RECORD_ABSENCE_PHRASES):
        return True
    return bool(_RECORD_ABSENCE_NEGATION.search(sentence_lower))


def _is_first_person_no_claim(sentence: str) -> bool:
    words = _WORD.findall(sentence)
    starts_first_person = bool(words) and words[0].lower() in _FIRST_PERSON_OPENERS
    lower = sentence.lower()
    has_first_person_clause = any(marker in lower for marker in _FIRST_PERSON_CLAUSE_MARKERS)
    if not starts_first_person and not has_first_person_clause:
        return False
    return not claim_markers(sentence)


def find_uncited_claims(sentences: list[dict]) -> list[dict]:
    """sentences: engine.m4.grounding_net.check_turn(...)["sentences"],
    each {"sentence": str, "tags": list[str], "verdict": str, "why": ...}.

    Returns a list of {"sentence": str, "class": "uncited_claim"} - one
    per declarative claim sentence carrying no citation and matching none
    of the three allowed-uncited kinds (a question, an honest-limit
    sentence, or first-person framing making no claim), in sentence
    order. Callers that know more context - a known-tradition name list,
    whether this turn was routed via other_tradition - may refine
    "uncited_claim" into "neighbour_named" or
    "own_doctrine_in_other_tradition_turn" via classify_neighbour_named/
    classify_other_tradition_turn below; this function stays pure,
    sentences in, offenses out, no registry or routing knowledge of its
    own."""
    offenses = []
    for sent in sentences:
        if sent["verdict"] != "ok" or sent["tags"]:
            continue
        text = sent["sentence"]
        if _is_question(text) or _is_honest_limit(text.lower()) or _is_first_person_no_claim(text):
            continue
        offenses.append({"sentence": text, "class": "uncited_claim"})
    return offenses


def classify_neighbour_named(offense: dict, known_tradition_names: list[str]) -> dict:
    """Upgrades a base "uncited_claim" offense to "neighbour_named" when
    its own sentence names another admitted world's own card_name or
    representative name. The caller supplies that list - built from the
    registry, the same source engine.api.table_wiring._labels and
    engine.m4.facilitator_turns.table_door_turn already draw theirs from -
    since this module has no registry access of its own."""
    lower = offense["sentence"].lower()
    if any(name.lower() in lower for name in known_tradition_names):
        return {**offense, "class": "neighbour_named"}
    return offense


def classify_other_tradition_turn(offense: dict, *, is_other_tradition_turn: bool) -> dict:
    """Upgrades a base "uncited_claim" offense to
    "own_doctrine_in_other_tradition_turn" when the whole turn was routed
    via the other_tradition out-of-scope classification
    (engine.m5.routing.PRESSABLE_CLASSES, RoutingDecision.
    out_of_scope_class) - routing context the caller already has
    (engine.m5.failure.resolve_gate's own result), not something this
    module re-derives."""
    if is_other_tradition_turn and offense["class"] == "uncited_claim":
        return {**offense, "class": "own_doctrine_in_other_tradition_turn"}
    return offense


def known_tradition_names(registry: dict, *, exclude_world_key: str) -> list[str]:
    """Every OTHER formation world's own card_name and representative
    name, straight from the registry - both fields already sit directly
    on a world's records/worlds/<code>.yaml entry (no package/frame load
    needed, so this is cheap enough to call every turn). Excludes the
    speaking world itself: naming your OWN tradition is not the R26
    violation shape."""
    names = []
    for key, entry in registry.items():
        if key == exclude_world_key or entry.get("kind") != "formation":
            continue
        if card_name := entry.get("card_name"):
            names.append(card_name)
        if rep_name := (entry.get("representative") or {}).get("name"):
            names.append(rep_name)
    return names


def build_uncited_claims_event(voice_event: dict, *, registry: dict, is_other_tradition_turn: bool) -> dict | None:
    """The full pipeline from a turn.py voice_event's own additive
    "uncited_claims" field (base "uncited_claim" offenses only) to the
    persisted uncited_claims event's payload, refined with both
    classify_* functions. Returns None when there is nothing to report -
    the clean case, and by far the common one - so callers can skip
    validate()/store.append() outright rather than persisting an empty
    event every turn."""
    offenses = voice_event.get("uncited_claims") or []
    if not offenses:
        return None
    names = known_tradition_names(registry, exclude_world_key=voice_event["speaker"])
    refined = [
        classify_other_tradition_turn(
            classify_neighbour_named(offense, names), is_other_tradition_turn=is_other_tradition_turn
        )
        for offense in offenses
    ]
    return {"speaker": voice_event["speaker"], "offenses": refined}
