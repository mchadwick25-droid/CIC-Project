from goldset.evidence import CARD_ONLY_FIELDS, record_block, voiced_fields
from engine.m1.spoken_fields import SPOKEN_FIELDS

PACK_ROLES = ("voice-diet", "evidence-head")


def test_every_field_the_registry_says_the_voice_is_shown_is_in_the_pack():
    missing = []
    for record_type, fields in SPOKEN_FIELDS.items():
        for name, spoken in fields.items():
            if spoken.role not in PACK_ROLES or "." in name or name in CARD_ONLY_FIELDS.get(record_type, ()):
                continue
            record = {"id": f"t.{record_type}", "record_type": record_type, name: f"token-{record_type}-{name}"}
            if f"token-{record_type}-{name}" not in record_block(record):
                missing.append(f"{record_type}.{name}")
    assert not missing


def test_a_world_core_record_shows_the_framing_the_voice_speaks_from():
    record = {"id": "w.core", "record_type": "world_core", "horizon": "HORIZON-TEXT", "thinness": "THINNESS-TEXT",
              "cautions": "CAUTIONS-TEXT", "living_traditions": "LIVING-TEXT", "thin_topics": [{"topic": "THIN-TOPIC"}]}
    block = record_block(record)
    for token in ("HORIZON-TEXT", "THINNESS-TEXT", "CAUTIONS-TEXT", "LIVING-TEXT", "THIN-TOPIC"):
        assert token in block


def test_a_story_record_shows_its_tellings_and_the_answers_the_voice_receives():
    record = {"id": "w.story", "record_type": "story", "tellable_as": "TELLABLE", "telling": "TELLING", "telling_medium": "MEDIUM",
              "absent_detail": "ABSENT"}
    block = record_block(record)
    for token in ("TELLABLE", "TELLING", "MEDIUM", "ABSENT"):
        assert token in block


def test_a_record_shows_the_descriptor_the_voices_evidence_line_carries():
    record = {"id": "w.gravity", "record_type": "gravity", "description": "DESCRIPTION", "classification": "PRIMARY"}
    assert "classification:\nPRIMARY" in record_block(record)


def test_the_pack_shows_nothing_the_voice_is_never_shown():
    record = {
        "id": "w.story", "record_type": "story", "telling": "TELLING", "heart": "CARD-HEART", "modern_contrast": "CONTRAST",
        "modern_lens_note": "LENS", "sources": [{"source_id": "w.source.x", "locus": "cic/texts/x.txt, lines 1-2: a quoted passage"}],
    }
    block = record_block(record)
    assert "TELLING" in block
    for token in ("CARD-HEART", "CONTRAST", "LENS", "quoted passage"):
        assert token not in block


def test_a_type_whose_evidence_line_is_all_of_its_text_shows_all_of_it():
    record = {"id": "w.figure", "record_type": "figure", "names": [{"tag": "in-world", "name": "FIGURE-NAME"}], "dates": {"display": "DATES-DISPLAY"}}
    block = record_block(record)
    assert "FIGURE-NAME" in block and "DATES-DISPLAY" in block


def test_a_type_the_registry_does_not_know_still_gets_the_fixed_fields():
    assert "text" in voiced_fields({"id": "x", "record_type": "unheard_of"})
