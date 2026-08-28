import pytest

from engine.m4.events import EventValidationError, validate


def test_valid_session_started_passes():
    validate(
        "session_started",
        {"world_key": "fix", "mode": "interview", "frame": None, "code_hash": "x", "package_manifest_hash": "y"},
    )


def test_missing_key_rejected():
    with pytest.raises(EventValidationError):
        validate("participant_message", {"text": "hi"})  # missing client_msg_id


def test_unknown_type_rejected():
    with pytest.raises(EventValidationError):
        validate("not_a_real_event", {})


def test_bad_enum_rejected():
    # "panel" not "table": table joined the mode enum with Artifact-7, so
    # the out-of-vocabulary example had to become a genuinely unknown mode.
    # (The old payload - interview keys with mode "table" - still fails,
    # but as a mode-shape mismatch; test_table_schema covers that.)
    with pytest.raises(EventValidationError):
        validate(
            "session_started",
            {"world_key": "fix", "mode": "panel", "frame": None, "code_hash": "x", "package_manifest_hash": "y"},
        )


def test_guidance_events_always_rejected():
    with pytest.raises(EventValidationError):
        validate("guidance_anything", {})
