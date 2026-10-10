"""The deterministic routing merge (Artifact-4 SS3) and directive assembly.
Both gate calls' OUTPUTS are plain dicts here - this module never makes a
model call itself; it takes whatever a safety/reader call produced (or, per
routing.py's caller in failure.py, None when a call failed) and applies the
priority-ordered merge. "The directive is assembled by code from the
schema - never free-composed by a model" (Artifact-4 SS3): assemble_directive
below is the one place a directive is built, and it only ever copies fields
out of the reader's own structured output.
"""
import re
from dataclasses import dataclass, field, replace

from .anachronism import mentions_term

ACUTE_SIGNALS = {"ACUTE_DISTRESS", "HARMFUL_DYNAMIC_SIGNAL"}
PRESSABLE_CLASSES = {"later_age", "other_tradition"}

# Reader-side classification of `system_nature` was found unreliable:
# "What exactly did your
# founder write in his 1543 book about Jewish people?" was classified
# system_nature on every phrasing tried, live, on witt - a message that
# names no system, bot, or "how were you built"-shaped question at all.
# live_calls.py's own READER_SYSTEM_PROMPT already states system_nature
# applies "ONLY when the participant is explicitly asking what THIS SYSTEM
# technically is or how it works" - so the reader was not missing an honest
# option (the correct answer, "none", was and is available), it returned
# the wrong one. `system_nature` was the one class that lets a Haiku-class
# model produce a non-answer without the shape of a refusal, and nothing
# downstream ever checked whether the claim was even plausible given the
# words actually used - a single reader field was treated as dispositive.
# This is the routing-side half of the fix (the reader's own prompt got
# the other half, in live_calls.py's own READER_SYSTEM_PROMPT): a
# deterministic backstop, not a classifier of its own. It does not decide
# what system_nature MEANS - live_calls.py's prompt still owns that - it
# only refuses to trust the reader's claim when the participant's own
# message contains none of the question shapes the reader was actually
# told to use ("are you an AI?", "is this a bot?", "how were you built?",
# "is this real or a script?"). Deliberately modeled on those four
# examples rather than a loose word list: a bare word like "real" or
# "built" appears constantly in ordinary historical-theological content
# ("was the temple really built", "is the resurrection real"), so this
# requires the SHAPE of those examples (a yes/no question addressed to
# "you" or "this") before trusting the classification - "checking is
# downstream and exact" (engine/m4/output_check.py's own phrase for the
# identical discipline applied to generated text, not a reader field).
# Deliberately does not include a bare "ai" token: this project's own
# formation worlds include Old Testament content, and "Ai" (Joshua 7-8) is
# a real place name that would otherwise collide with it.
_SYSTEM_NATURE_SHAPE = re.compile(
    r"\b(?:are|is|were|was)\b[^.?!]{0,30}\b(?:you|this)\b[^.?!]{0,30}\b"
    r"(?:a\.?i\.?|bot|chatbot|robot|real|fake|human|script(?:ed)?|"
    r"program(?:med)?|built|made|created|coded|simulated|"
    r"artificial|algorithm|software|llm)\b",
    re.IGNORECASE,
)


def _plausible_system_nature(message: str) -> bool:
    return bool(_SYSTEM_NATURE_SHAPE.search(message or ""))


@dataclass(frozen=True)
class Directive:
    asks: list[dict] = field(default_factory=list)
    register_note: str | None = None
    suspend_register_statement_1: bool = False
    ambiguity_options: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class RoutingDecision:
    action: str  # safety_turn | check_in_turn | system_nature_turn | bridge_turn | etic_turn | voice_with_directive | voice_pass_through
    reason: str
    directive: Directive | None = None
    # A structured field, not a
    # `reason` string to parse - set only on a voice_with_directive first
    # ask of a PRESSABLE_CLASSES member (e.g. "other_tradition"), so a
    # caller that needs to know can check this directly rather than
    # matching against reason's own free text, which is allowed to change
    # wording without that being a routing-behavior change.
    out_of_scope_class: str | None = None


def assemble_directive(reader: dict) -> Directive:
    personal_wound = reader["register"] == "personal_wound"
    return Directive(
        asks=list(reader["asks"]),
        register_note="witness-before-answer licensed" if personal_wound else None,
        suspend_register_statement_1=personal_wound,
        ambiguity_options=list(reader.get("ambiguity_options") or []),
    )


def directive_without_terms(reader: dict, display_terms: list[str]) -> Directive | None:
    """The directive for a bridged turn: everything assemble_directive
    builds, minus every ask and every ambiguity reading that carries the
    barred word.

    The bridge hands the voice the term-free underlying subject and nothing
    else (Program-Spec SS77), which is right about the word and was wrong
    about the rest of the message: a participant who asked two things in one
    sentence lost the second one entirely, because the bridge route carries
    no directive at all. Measured, not theorised - the bridge became much
    easier to reach once the modern term was read out of the message
    directly, so this stopped being a corner case.

    Returns None when nothing survives the filter, which is the ordinary
    single-ask bridge: that leaves the voice exactly the underlying subject
    it got before, rather than a directive announcing it has no asks.
    """
    directive = assemble_directive(reader)
    asks = [a for a in directive.asks if not mentions_term(a.get("text") or "", display_terms)]
    options = [o for o in directive.ambiguity_options if not mentions_term(o, display_terms)]
    if not asks and not options:
        return None
    return replace(directive, asks=asks, ambiguity_options=options)


def route(
    *, safety: dict | None, reader: dict | None, pressed: dict[str, bool], anachronistic_term_ids: set[str], message: str
) -> RoutingDecision:
    """safety=None means the safety call is unavailable this turn (failed/
    timed out) - callers get here via failure.py's fail-open path, never by
    skipping the safety call on purpose.

    reader=None means the reader call failed/timed out but safety alone was
    decisive (ACUTE_DISTRESS, HARMFUL_DYNAMIC_SIGNAL, or AMBIGUOUS_LOW_CONFIDENCE
    - failure.py's _SAFETY_DECISIVE_SIGNALS). Safe only because those three
    branches below return before this function ever dereferences `reader`;
    every other branch requires a real reader dict and failure.py never calls
    route() with reader=None unless one of those three signals is already
    confirmed present.

    message is the participant's own text this turn - required, not
    defaulted, so a caller that hasn't been updated fails loudly (a
    TypeError) rather than silently routing every system_nature claim
    through _plausible_system_nature("") and never trusting it (B-2). Unused
    on the reader=None path above, since that path always returns before
    reaching the message-dependent system_nature branch - still required in
    the signature so every caller passes a real value uniformly."""
    if safety is not None and safety["signal"] in ACUTE_SIGNALS:
        reason = f"safety signal {safety['signal']}"
        risk_subject = safety.get("risk_subject")
        if safety["signal"] == "ACUTE_DISTRESS" and risk_subject and risk_subject != "not_applicable":
            # Doesn't change the route (still safety_turn either way) - carried
            # through so the safety turn's content and the audit trail can
            # address who the disclosed risk actually belongs to, rather than
            # always assuming the participant themselves. See Artifact-4 SS1.
            reason = f"{reason} (risk_subject={risk_subject})"
        return RoutingDecision(action="safety_turn", reason=reason)

    if safety is not None and safety["signal"] == "AMBIGUOUS_LOW_CONFIDENCE":
        # Live safety-script batch 2 (scenario s9) surfaced this
        # gap: an adversarial hypothetical-framed disclosure was correctly
        # classified AMBIGUOUS_LOW_CONFIDENCE, then fell through to ordinary
        # (non-safety) routing since AMBIGUOUS wasn't in ACUTE_SIGNALS. The
        # fix: give it its own softer route - a check-in turn, short of
        # the full safety turn - ranked above system_nature/bridge/etic so a
        # possible disclosure still gets a safety-aware response even when
        # the reader also reads the message as e.g. a system-nature question.
        return RoutingDecision(action="check_in_turn", reason="safety signal AMBIGUOUS_LOW_CONFIDENCE")

    if reader["out_of_scope"]["class"] == "system_nature":
        if _plausible_system_nature(message):
            return RoutingDecision(action="system_nature_turn", reason="participant asked about the system's nature")
        # B-2: the reader's own claim doesn't hold up against the words the
        # participant actually used - fall through to the rest of this
        # function's own priority order instead of trusting it. Not
        # silently dropped: engine.m4.turn's own gate_decision event still
        # carries the reader's raw output, so this override is visible in
        # the audit trail even though it changes nothing this function
        # returns to the caller directly.

    term_ids = {t["term_id"] for t in reader.get("modern_terms") or []}
    if term_ids & anachronistic_term_ids:
        return RoutingDecision(action="bridge_turn", reason="anachronistic modern term(s) present")

    out_of_scope_class = reader["out_of_scope"]["class"]
    if out_of_scope_class in PRESSABLE_CLASSES:
        if pressed.get(out_of_scope_class, False):
            return RoutingDecision(action="etic_turn", reason=f"{out_of_scope_class} pressed")
        return RoutingDecision(
            action="voice_with_directive",
            reason=f"{out_of_scope_class}, first ask - in-world answer",
            directive=assemble_directive(reader),
            out_of_scope_class=out_of_scope_class,
        )

    return RoutingDecision(action="voice_with_directive", reason="ordinary turn", directive=assemble_directive(reader))
