"""The event catalog (Artifact-3 SS2) - "exhaustive; adding a type is a
reviewed change." REQUIRED_KEYS is the payload floor per type; ENUMS are the
closed vocabularies the spec pins (mode is literally just "interview" in
Phase 1 - the Table is a separate future product, spec O9). validate()
raises on a missing key or an out-of-vocabulary value; it does not (and
should not) validate business logic like "does world_key exist" - that's
the registry's job, not the log's.
"""

REQUIRED_KEYS: dict[str, set[str]] = {
    "session_started": {"world_key", "mode", "frame", "code_hash", "package_manifest_hash"},
    "participant_message": {"text", "client_msg_id"},
    "gate_decision": {"asks", "register", "out_of_scope", "modern_terms", "safety", "route", "directive", "degraded"},
    "facilitator_turn": {"kind", "text"},
    "voice_turn": {"speaker", "text", "citations", "glosses", "figures_used", "quote_offers", "attempts_meta"},
    "retrieval_surfaced": {"chunk_ids"},
    "safety_state": {"track", "level", "accumulator"},
    "turn_committed": {"turn_no"},
    "session_resumed": {"device_hint"},
    "escalation_pressed": {"class"},
    "deletion_requested": set(),
    "session_closed": {"reason"},
}

ENUMS: dict[tuple[str, str], set[str]] = {
    ("session_started", "mode"): {"interview"},  # the only mode Phase 1 ships (spec O9: Table is a separate product)
    ("facilitator_turn", "kind"): {"door", "threshold", "safety", "bridge", "close"},
    ("safety_state", "track"): {"A", "B"},
    ("escalation_pressed", "class"): {"later_age", "other_tradition"},
    ("session_closed", "reason"): {"participant", "idle", "cap"},
}


class EventValidationError(ValueError):
    pass


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
    for field, allowed in ENUMS.items():
        etype, key = field
        if etype == event_type and payload.get(key) not in allowed:
            raise EventValidationError(f"{event_type}.{key} = {payload.get(key)!r} not in {sorted(allowed)}")
