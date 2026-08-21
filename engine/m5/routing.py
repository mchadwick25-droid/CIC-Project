"""The deterministic routing merge (Artifact-4 SS3) and directive assembly.
Both gate calls' OUTPUTS are plain dicts here - this module never makes a
model call itself; it takes whatever a safety/reader call produced (or, per
routing.py's caller in failure.py, None when a call failed) and applies the
priority-ordered merge. "The directive is assembled by code from the
schema - never free-composed by a model" (Artifact-4 SS3): assemble_directive
below is the one place a directive is built, and it only ever copies fields
out of the reader's own structured output.
"""
from dataclasses import dataclass, field

ACUTE_SIGNALS = {"ACUTE_DISTRESS", "HARMFUL_DYNAMIC_SIGNAL"}
PRESSABLE_CLASSES = {"later_age", "other_tradition"}


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


def assemble_directive(reader: dict) -> Directive:
    personal_wound = reader["register"] == "personal_wound"
    return Directive(
        asks=list(reader["asks"]),
        register_note="witness-before-answer licensed" if personal_wound else None,
        suspend_register_statement_1=personal_wound,
        ambiguity_options=list(reader.get("ambiguity_options") or []),
    )


def route(*, safety: dict | None, reader: dict, pressed: dict[str, bool], anachronistic_term_ids: set[str]) -> RoutingDecision:
    """safety=None means the safety call is unavailable this turn (failed/
    timed out) - callers get here via failure.py's fail-open path, never by
    skipping the safety call on purpose."""
    if safety is not None and safety["signal"] in ACUTE_SIGNALS:
        return RoutingDecision(action="safety_turn", reason=f"safety signal {safety['signal']}")

    if safety is not None and safety["signal"] == "AMBIGUOUS_LOW_CONFIDENCE":
        # Live safety-script batch 2 (2026-08-21, scenario s9) surfaced this
        # gap: an adversarial hypothetical-framed disclosure was correctly
        # classified AMBIGUOUS_LOW_CONFIDENCE, then fell through to ordinary
        # (non-safety) routing since AMBIGUOUS wasn't in ACUTE_SIGNALS. Mark's
        # ruling: give it its own softer route - a check-in turn, short of
        # the full safety turn - ranked above system_nature/bridge/etic so a
        # possible disclosure still gets a safety-aware response even when
        # the reader also reads the message as e.g. a system-nature question.
        return RoutingDecision(action="check_in_turn", reason="safety signal AMBIGUOUS_LOW_CONFIDENCE")

    if reader["out_of_scope"]["class"] == "system_nature":
        return RoutingDecision(action="system_nature_turn", reason="participant asked about the system's nature")

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
        )

    return RoutingDecision(action="voice_with_directive", reason="ordinary turn", directive=assemble_directive(reader))
