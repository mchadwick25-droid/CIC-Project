"""The readability bar screen's own tests (Build-Plan.md Stage 2b).

Report-only, so the tests are about shape and coverage, not a ceiling -
this module has none to check."""
from engine.m1 import bar_screen
from engine.m1.registry import formation_world_keys, load_registry


def test_texts_for_field_reads_a_plain_string_field():
    record = {"record_type": "story", "tellable_as": "A short retelling."}
    assert bar_screen._texts_for_field(record, "tellable_as") == ["A short retelling."]


def test_texts_for_field_skips_blank_and_missing_fields():
    assert bar_screen._texts_for_field({"record_type": "story"}, "tellable_as") == []
    assert bar_screen._texts_for_field({"record_type": "story", "tellable_as": "   "}, "tellable_as") == []


def test_texts_for_field_takes_only_the_representative_side_of_a_demonstration():
    record = {
        "record_type": "demonstration",
        "exchange": [
            {"speaker": "participant", "text": "What do you believe?"},
            {"speaker": "representative", "text": "We hold that Christ is fully God and fully man."},
        ],
    }
    assert bar_screen._texts_for_field(record, "exchange") == [
        "We hold that Christ is fully God and fully man."
    ]


def test_screen_world_shape_on_a_real_formation_world():
    """Smoke test standing in for "runs on all ten" (Build-Plan.md Stage
    2b's own acceptance criterion) - alx here, the full fleet run by hand
    when this stage ships (worlds/<code>/build/bar-screen-<date>.json
    committed for all ten, not just this one)."""
    report = bar_screen.screen_world("alx")
    assert report["world"] == "alx"
    assert report["fields"]
    for key, summary in report["fields"].items():
        assert "." in key
        assert summary["count"] > 0
        assert summary["fk_grade_median"] is not None
        # worst_record must be a real record id that appears in this
        # field's own entries.
        assert any(e["record_id"] == summary["worst_record"] for e in report["records"][key])


def test_screen_world_only_covers_voice_diet_fields():
    """voice_craft is "instruction" role, not "voice-diet" - it should
    never appear in a bar screen (this tool measures what a participant
    reads, not standing guidance to the model)."""
    report = bar_screen.screen_world("alx")
    assert not any(key.startswith("voice_craft.") for key in report["fields"])


def test_all_ten_formation_worlds_screen_without_error():
    registry = load_registry()
    for world_key in formation_world_keys(registry):
        report = bar_screen.screen_world(world_key)
        assert report["world"] == world_key
        assert report["fields"], f"{world_key}: no voice-diet fields found at all"
