from goldset.evidence import record_block, voiced_fields
from engine.m1.spoken_fields import SPOKEN_FIELDS

PACK_ROLES = ("voice-diet", "evidence-head")


def test_every_field_the_registry_says_the_voice_is_shown_is_in_the_pack():
    missing = []
    for record_type, fields in SPOKEN_FIELDS.items():
        for name, spoken in fields.items():
            if spoken.role not in PACK_ROLES or "." in name:
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


def test_a_story_record_shows_its_tellings_and_its_structured_answers():
    record = {"id": "w.story", "record_type": "story", "tellable_as": "TELLABLE", "telling": "TELLING", "telling_medium": "MEDIUM",
              "heart": "HEART", "absent_detail": "ABSENT", "modern_contrast": "CONTRAST"}
    block = record_block(record)
    for token in ("TELLABLE", "TELLING", "MEDIUM", "HEART", "ABSENT", "CONTRAST"):
        assert token in block


def test_a_record_shows_where_it_rests_in_its_sources():
    record = {"id": "w.quote", "record_type": "quote", "modern_rendering": "RENDERING",
              "sources": [{"source_id": "w.source.pontius", "locus": "cic/texts/pontius.txt, lines 10-12"}]}
    block = record_block(record)
    assert "w.source.pontius, cic/texts/pontius.txt, lines 10-12" in block


def test_a_type_the_registry_does_not_know_still_gets_the_fixed_fields():
    assert "text" in voiced_fields({"id": "x", "record_type": "unheard_of"})
