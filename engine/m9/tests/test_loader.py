"""Against the real, committed fixture world - the same discipline
engine/m4/tests/test_world_loader.py already holds: prove the loader
against real, previously-authored data, not a synthetic stand-in."""
from engine.m1.loader import load_world_records

from engine.m9.loader import load_shelf, read_bucket_rows, read_pairs, read_vendored_files


def test_real_fixture_bucket_has_both_rows_with_cm_fields():
    rows = read_bucket_rows("fixture-synthetic")
    by_id = {r["row_id"]: r for r in rows}
    assert by_id["fixture-synthetic--witness-scroll"]["role"] == "tradition"
    ctx = by_id["fixture-synthetic--later-summary"]
    assert ctx["role"] == "context"
    assert ctx["voice_of"] == "fixture-synthetic-neighbour"
    assert ctx["documented_exchange"] == "confirmed"


def test_real_pairs_yaml_has_the_fixture_pair():
    pairs, parties = read_pairs()
    match = [p for p in pairs if {p.get("a"), p.get("b")} == {"fixture-synthetic", "fixture-synthetic-neighbour"}]
    assert len(match) == 1
    assert match[0]["relation"] == "mutual-awareness"
    assert "fixture-synthetic-neighbour" in parties


def test_real_vendored_files_include_the_two_fixture_texts():
    files = read_vendored_files()
    assert "fixture-synthetic_witness-scroll.txt" in files
    assert "fixture-synthetic_later-summary.txt" in files


def test_load_shelf_against_real_fixture_world():
    records = load_world_records("fix")
    shelf = load_shelf(world_key="fix", census_id="fixture-synthetic", records=records)
    assert shelf.census_id == "fixture-synthetic"
    assert "fixture-synthetic_witness-scroll.txt" in shelf.files
    assert "fixture-synthetic_later-summary.txt" in shelf.files
    # verbatim quotes' own words are really in the loaded, normalized unit text
    assert "did not see him" in shelf.units["fixture-synthetic_witness-scroll.txt"]
    # the absence source's own named file is loaded too, even though it's
    # the same on-shelf file here - the off-shelf path is exercised by the
    # real fleet once a world names a genuinely off-shelf absence file.
    assert "fixture-synthetic_witness-scroll.txt" in shelf.units
