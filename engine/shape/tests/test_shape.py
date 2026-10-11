"""engine.shape: one segment for every world, pinned by its hash."""
import pytest

import engine.shape as shape
from engine.m1.loader import load_fleet_records
from engine.m10.deployed import SELF_REFERENCE_STEMS
from engine.m4.voice_request import build_voice_request


def test_the_segment_matches_its_pinned_hash():
    assert shape.shape_hash(shape.shape_text()) == shape.SHAPE_HASH


def test_a_changed_segment_refuses_to_load(monkeypatch):
    monkeypatch.setattr(shape, "SHAPE_HASH", "sha256:" + "0" * 64)
    shape.shape_text.cache_clear()
    try:
        with pytest.raises(shape.ShapeMismatch):
            shape.shape_text()
    finally:
        monkeypatch.undo()
        shape.shape_text.cache_clear()


def test_the_segment_names_no_world_and_ships_no_placeholder():
    text = shape.shape_text()
    assert "{world}" not in text and "world.term.example" not in text and "world.gravity.example" not in text


def test_the_segment_carries_every_self_reference_hardening_rule():
    text = shape.shape_text()
    assert all(pattern.search(text) for _, pattern in SELF_REFERENCE_STEMS)


def test_the_segment_holds_the_fleet_sections_in_order():
    text = shape.build_shape(load_fleet_records())
    heads = [line for line in text.splitlines() if line.startswith("## ")]
    assert heads == ["## Register", "## Pronoun rule", "## Citation contract", "## Stories and quotes", "## Limit discipline"]


def test_no_fleet_voice_record_builds_an_empty_segment():
    assert shape.build_shape({}) == ""


def test_every_voice_request_sends_the_segment_first_then_the_world_both_cached():
    system, _ = build_voice_request(system_prompt="WORLD", message="hi")
    assert [b["text"] for b in system] == [shape.shape_text(), "WORLD"]
    assert all(b["cache_control"] == {"type": "ephemeral"} for b in system)


def test_the_stories_and_quotes_section_asks_for_a_full_quote_a_retelling_and_no_bare_names():
    text = shape.shape_text()
    section = text.split("## Stories and quotes", 1)[1].split("\n## ", 1)[0]
    assert "one quote in full" in section and "modern rendering" in section
    assert "directive asks for a quote" in section
    assert "retelling" in section and "never merely named" in section
