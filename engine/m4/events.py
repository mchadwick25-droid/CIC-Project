"""The event catalog (Artifact-3 SS2) - "exhaustive; adding a type is a
reviewed change." REQUIRED_KEYS is the payload floor per type; ENUMS are the
closed vocabularies the spec pins. validate() raises on a missing key or an
out-of-vocabulary value; it does not (and should not) validate business
logic like "does world_key exist" - that's the registry's job, not the log's.

Table mode (Artifact-7): mode gained "table" alongside
"interview", and session_started became the one MODE-SHAPED payload in the
catalog - an interview carries world_key/package_manifest_hash, a table
carries world_keys/package_manifest_hashes, and a payload carrying both
shapes (or a table outside 2-3 distinct worlds) fails validation. The
2-3 bound is enforced here at the log level deliberately: the design doc's
own construction note admits "no mechanism in the system prevents a fourth
world from being called" and leaves the ceiling to the Facilitator's
judgment - this schema is that mechanism (Artifact-7 SS1), the same way the
catalog already pins enums rather than trusting call sites. turn_selected
and round_closed are the round's audit surface (Artifact-7 SS2): who was
chosen to speak and why is never recoverable from voice_turn order alone.
"""

REQUIRED_KEYS: dict[str, set[str]] = {
    # session_started's mode-dependent keys (world_key vs world_keys, hash
    # vs hashes) are enforced by _validate_session_started_shape below, not
    # by this floor - this is the mode-independent floor only.
    "session_started": {"mode", "frame", "code_hash"},
    "participant_message": {"text", "client_msg_id"},
    "gate_decision": {"asks", "register", "out_of_scope", "modern_terms", "safety", "route", "directive", "degraded"},
    "facilitator_turn": {"kind", "text"},
    # output_defects is REQUIRED, not optional, so no path can reach a
    # participant without the finished text having been checked - the
    # catalog is where "unskippable" is actually enforceable. Empty list
    # is the clean case (engine.m4.output_check).
    "voice_turn": {"speaker", "text", "citations", "glosses", "figures_used", "quote_offers", "attempts_meta", "output_defects"},
    "retrieval_surfaced": {"chunk_ids"},
    "safety_state": {"track", "level", "accumulator"},
    "turn_committed": {"turn_no"},
    # Table rounds (Artifact-7 SS2). turn_selected precedes each table
    # voice_turn: world_key is the chosen speaker, reason the selector's
    # stated basis (or the deterministic fallback's, with degraded true).
    # round_closed is written exactly once per round; turns is the count of
    # voice turns the round actually produced (0 for a governed round).
    "turn_selected": {"round_no", "position", "world_key", "reason", "degraded"},
    "round_closed": {"round_no", "reason", "turns"},
    "session_resumed": {"device_hint"},
    "escalation_pressed": {"class"},
    "deletion_requested": set(),
    "session_closed": {"reason"},
    # The seat-identity guard's own audit surface, same idea as
    # turn_selected/round_closed above: a
    # generated turn writing itself as the Facilitator or another seated
    # voice is caught and regenerated (or, on a second catch, replaced by
    # a facilitator_turn) before it ever reaches voice_turn - not
    # recoverable from voice_turn alone, since the caught text is never
    # written there. One event per catch (attempt="first" then, only if
    # the regenerated attempt ALSO caught, attempt="regenerated") - never
    # one summary event per turn.
    "seat_identity_violation": {"round_no", "position", "world_key", "offending_prefix", "attempt"},
    # The uncited-claims enforcement's own audit surface: report-only, one
    # event per voice_turn that carried at least one uncited declarative
    # claim sentence - mode-agnostic (both interview and table), so no
    # round_no/position here the way seat_identity_violation carries
    # (table-only bookkeeping). offenses: list[{"sentence": str, "class":
    # str}]. paragraph_offenses is additive: the SAME shape, a second,
    # independent list - a wholly-uncited-paragraph or inherited-
    # ungrounded failure, never merged into offenses (which stays exactly
    # the sentence-level list it always was).
    "uncited_claims": {"speaker", "offenses", "paragraph_offenses"},
}

ENUMS: dict[tuple[str, str], set[str]] = {
    ("session_started", "mode"): {"interview", "table"},  # interview: Phase 1's single-voice mode; table: Artifact-7, the multi-voice extension spec O9 priced in
    ("round_closed", "reason"): {"selector_closed", "cap", "floor_unmet_exhausted"},  # Artifact-7 SS2
    # seat_correction: the Facilitator taking a turn back after
    # the seat-identity guard exhausted its one regeneration - a distinct
    # kind from "safety" (TABLE_DEPENDENCY_CHECK's own kind), which is
    # about a participant leaning on the conversation, not a generation
    # defect. grounding_correction: the same
    # "Facilitator takes a turn back" shape, this time for the
    # uncited-claims enforcement (engine.m4.facilitator_turns.voice_rejected_turn) - a
    # distinct kind from seat_correction because the underlying defect is
    # different (unsupported/uncited content, not identity impersonation),
    # even though the mechanism (regenerate once, then hand off) is the
    # same one reused.
    ("facilitator_turn", "kind"): {"door", "threshold", "safety", "bridge", "close", "seat_correction", "grounding_correction"},
    ("safety_state", "track"): {"A", "B"},
    ("escalation_pressed", "class"): {"later_age", "other_tradition"},
    ("session_closed", "reason"): {"participant", "idle", "cap"},
    ("seat_identity_violation", "attempt"): {"first", "regenerated"},
}


class EventValidationError(ValueError):
    pass


# The two mode shapes, stated once. Each mode's keys are REQUIRED for that
# mode and FORBIDDEN for the other - a payload that carries both shapes is
# ambiguous about what session it started and fails loudly (Artifact-7 SS1).
_MODE_KEYS = {
    "interview": {"world_key", "package_manifest_hash"},
    "table": {"world_keys", "package_manifest_hashes"},
}


def _validate_session_started_shape(payload: dict) -> None:
    mode = payload.get("mode")
    if mode not in _MODE_KEYS:
        return  # the enum check below owns the unknown-mode error
    required, forbidden = _MODE_KEYS[mode], set().union(*(v for k, v in _MODE_KEYS.items() if k != mode))
    missing = required - set(payload)
    if missing:
        raise EventValidationError(f"session_started mode={mode!r} payload missing required keys: {sorted(missing)}")
    present_forbidden = forbidden & set(payload)
    if present_forbidden:
        raise EventValidationError(
            f"session_started mode={mode!r} payload carries the other mode's keys: {sorted(present_forbidden)} - a payload must be exactly one shape"
        )
    if mode == "table":
        world_keys = payload["world_keys"]
        if not isinstance(world_keys, list) or not (2 <= len(world_keys) <= 3) or len(set(world_keys)) != len(world_keys):
            # One world is an interview, not a table; four is forbidden by
            # schema, not left to judgment - this line IS the mechanism the
            # design doc's construction note said did not exist.
            raise EventValidationError(f"session_started world_keys must be 2-3 distinct keys, got {world_keys!r}")
        hashes = payload["package_manifest_hashes"]
        if not isinstance(hashes, dict) or set(hashes) != set(world_keys):
            raise EventValidationError(
                f"session_started package_manifest_hashes keys {sorted(hashes) if isinstance(hashes, dict) else hashes!r} must match world_keys {sorted(world_keys)} exactly"
            )


# The ENUMS mechanism above validates one scalar payload value per
# (event_type, field) pair - it has no way to reach into a list of dicts.
# uncited_claims' own offenses[].class needs exactly that, so it gets its
# own small shape check rather than stretching ENUMS to cover a shape it
# was never built for.
_UNCITED_CLAIM_CLASSES = {"uncited_claim", "neighbour_named", "own_doctrine_in_other_tradition_turn"}
# paragraph_offenses' own closed set,
# distinct from _UNCITED_CLAIM_CLASSES above - a paragraph-level failure
# is never one of the sentence-level classes, and vice versa.
_PARAGRAPH_OFFENSE_CLASSES = {"wholly_uncited_paragraph", "inherited_ungrounded"}


def _validate_offense_list_shape(field_name: str, offenses, allowed_classes: set[str]) -> None:
    if not isinstance(offenses, list):
        raise EventValidationError(f"uncited_claims.{field_name} must be a list, got {offenses!r}")
    for offense in offenses:
        if not isinstance(offense, dict) or set(offense) != {"sentence", "class"}:
            raise EventValidationError(f"uncited_claims.{field_name} entry must be exactly {{'sentence', 'class'}}, got {offense!r}")
        if offense["class"] not in allowed_classes:
            raise EventValidationError(f"uncited_claims.{field_name} class {offense['class']!r} not in {sorted(allowed_classes)}")


def _validate_uncited_claims_shape(payload: dict) -> None:
    _validate_offense_list_shape("offenses", payload["offenses"], _UNCITED_CLAIM_CLASSES)
    _validate_offense_list_shape("paragraph_offenses", payload["paragraph_offenses"], _PARAGRAPH_OFFENSE_CLASSES)


def validate(event_type: str, payload: dict) -> None:
    if event_type.startswith("guidance_"):
        # reserved; no live guidance exists under principle 2 (spec SS3 catalog note) -
        # accepted as a type family, never actually emitted by any code in this build.
        raise EventValidationError("guidance_* events are reserved and must never be emitted (spec principle 2)")
    if event_type not in REQUIRED_KEYS:
        raise EventValidationError(f"unknown event_type {event_type!r} - the catalog is exhaustive (Artifact-3 SS2)")
    missing = REQUIRED_KEYS[event_type] - set(payload)
    if missing:
        raise EventValidationError(f"{event_type} payload missing required keys: {sorted(missing)}")
    if event_type == "session_started":
        _validate_session_started_shape(payload)
    if event_type == "uncited_claims":
        _validate_uncited_claims_shape(payload)
    for field, allowed in ENUMS.items():
        etype, key = field
        if etype == event_type and payload.get(key) not in allowed:
            raise EventValidationError(f"{event_type}.{key} = {payload.get(key)!r} not in {sorted(allowed)}")
