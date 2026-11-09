import json

from engine.m6 import atlas_html

FIXTURE = """<!doctype html>
<html><head><script>
const DATA = {
 "movements": [
  {
   "id": "movement-a",
   "why": "Old why text.",
   "sources": [
    {
     "work": "Top-level Source",
     "type": "primary",
     "note": "Old top-level note."
    }
   ],
   "documentedStories": [
    {
     "title": "A Story",
     "sources": [
      {
       "work": "Nested Source",
       "type": "primary",
       "note": "Nested note - must never change when top-level sources is edited."
      }
     ]
    }
   ]
  },
  {
   "id": "movement-b",
   "why": "Movement B's why."
  }
 ],
 "edges": [
  {"from": "movement-a", "to": "movement-b", "type": "formed", "note": "An edge note."}
 ]
};
</script></head><body></body></html>
"""


def _write_fixture(tmp_path):
    path = tmp_path / "atlas-v3.html"
    path.write_text(FIXTURE, encoding="utf-8")
    return path


def test_read_movements_parses_embedded_data(tmp_path):
    path = _write_fixture(tmp_path)
    movements = atlas_html.read_movements(path)
    assert [m["id"] for m in movements] == ["movement-a", "movement-b"]


def test_read_edges_parses_embedded_data(tmp_path):
    path = _write_fixture(tmp_path)
    edges = atlas_html.read_edges(path)
    assert edges == [{"from": "movement-a", "to": "movement-b", "type": "formed", "note": "An edge note."}]


def test_apply_movement_updates_string_field(tmp_path):
    path = _write_fixture(tmp_path)
    n = atlas_html.apply_movement_updates(path, {"movement-a": {"why": "New why text."}})
    assert n == 1
    movements = atlas_html.read_movements(path)
    assert movements[0]["why"] == "New why text."
    assert movements[1]["why"] == "Movement B's why."  # untouched


def test_apply_movement_updates_never_touches_nested_field_of_same_name(tmp_path):
    """Regression test: a naive first-occurrence search for "sources" would
    find documentedStories[0].sources before the movement's own top-level
    sources, since it appears earlier in the object's serialized text order
    depends on field order - this fixture deliberately puts documentedStories
    before sources isn't the point; the point is depth, not order."""
    path = _write_fixture(tmp_path)
    new_sources = [{"work": "Replaced Source", "type": "primary", "note": "Replaced note."}]
    atlas_html.apply_movement_updates(path, {"movement-a": {"sources": new_sources}})
    movements = atlas_html.read_movements(path)
    m = movements[0]
    assert m["sources"] == new_sources
    assert m["documentedStories"][0]["sources"][0]["note"] == (
        "Nested note - must never change when top-level sources is edited."
    )


def test_apply_movement_updates_inserts_missing_field(tmp_path):
    path = _write_fixture(tmp_path)
    atlas_html.apply_movement_updates(path, {"movement-b": {"documentedStories": [{"title": "New Story"}]}})
    movements = atlas_html.read_movements(path)
    m = next(m for m in movements if m["id"] == "movement-b")
    assert m["documentedStories"] == [{"title": "New Story"}]
    assert m["why"] == "Movement B's why."  # untouched


def test_inserted_field_preserves_the_closing_brace_indentation(tmp_path):
    """Regression: an earlier version of _insert_field rstripped the
    whitespace before the object's own closing brace along with the
    trailing comma it was adding, then never put it back - every object
    that ever gained a new field this way lost its closing brace's own
    indentation, moving it and every following sibling line in the diff.
    movement-a is not the array's last object, so a lost/misplaced brace
    here would also break movement-b's own object boundary."""
    path = _write_fixture(tmp_path)
    atlas_html.apply_movement_updates(path, {"movement-a": {"newField": "hello"}})
    text = path.read_text(encoding="utf-8")
    assert '\n  },\n  {\n   "id": "movement-b"' in text


def test_apply_movement_updates_preserves_surrounding_formatting(tmp_path):
    path = _write_fixture(tmp_path)
    atlas_html.apply_movement_updates(path, {"movement-a": {"why": "New why text."}})
    text = path.read_text(encoding="utf-8")
    # the untouched movement-b block, and the file's surrounding HTML, must
    # be byte-identical to the original fixture
    assert '"id": "movement-b"' in text
    assert text.startswith("<!doctype html>")
    assert text.rstrip().endswith("</html>")


def test_apply_movement_updates_no_writes_when_no_matching_ids(tmp_path):
    path = _write_fixture(tmp_path)
    before = path.read_text(encoding="utf-8")
    n = atlas_html.apply_movement_updates(path, {"nonexistent-id": {"why": "irrelevant"}})
    assert n == 0
    assert path.read_text(encoding="utf-8") == before


def test_apply_movement_updates_empty_updates_is_a_no_op(tmp_path):
    path = _write_fixture(tmp_path)
    before = path.read_text(encoding="utf-8")
    n = atlas_html.apply_movement_updates(path, {})
    assert n == 0
    assert path.read_text(encoding="utf-8") == before


def test_written_file_is_still_valid_json_at_the_data_array(tmp_path):
    path = _write_fixture(tmp_path)
    atlas_html.apply_movement_updates(
        path,
        {"movement-a": {"documentedStories": [{"title": "Replaced", "sources": []}]}},
    )
    movements = atlas_html.read_movements(path)
    assert json.dumps(movements)  # round-trips cleanly


def test_write_edges_replaces_array_and_reports_change(tmp_path):
    path = _write_fixture(tmp_path)
    new_edges = [{"id": "movement-a--movement-b", "from": "movement-a", "to": "movement-b",
                  "type": "influenced", "note": "A note with [brackets] inside."}]
    assert atlas_html.write_edges(path, new_edges) is True
    assert atlas_html.read_edges(path) == new_edges
    assert atlas_html.read_movements(path)[0]["id"] == "movement-a"
    assert atlas_html.write_edges(path, new_edges) is False


def test_write_roster_keeps_held_rows_byte_for_byte_and_drops_the_rest(tmp_path):
    path = _write_fixture(tmp_path)
    before = path.read_text(encoding="utf-8")
    held_b = before[before.index('{\n   "id": "movement-b"'):before.index('\n ],\n "edges"')]
    new_row = {"id": "movement-c", "kind": "cross-church movement", "names": ["one", "two"]}
    assert atlas_html.write_roster(path, [{"id": "movement-b"}, new_row]) is True
    after = path.read_text(encoding="utf-8")
    assert [m["id"] for m in atlas_html.read_movements(path)] == ["movement-b", "movement-c"]
    assert atlas_html.read_movements(path)[1] == new_row
    assert held_b in after
    assert "Old why text." not in after
    assert '  {\n   "id": "movement-c",\n   "kind": "cross-church movement",\n   "names": [\n    "one",' in after
    assert atlas_html.read_edges(path)[0]["from"] == "movement-a"


def test_write_roster_with_the_same_rows_is_a_no_op(tmp_path):
    path = _write_fixture(tmp_path)
    assert atlas_html.write_roster(path, atlas_html.read_movements(path)) is False
    assert path.read_text(encoding="utf-8") == FIXTURE


def test_write_eras_replaces_the_eras_array(tmp_path):
    path = tmp_path / "atlas.html"
    path.write_text(FIXTURE.replace(' "movements": [', ' "eras": [\n  {\n   "num": 1\n  }\n ],\n "movements": ['), encoding="utf-8")
    assert atlas_html.read_eras(path) == [{"num": 1}]
    assert atlas_html.write_eras(path, [{"num": 1, "dates": "1906-c. 2010"}]) is True
    assert atlas_html.read_eras(path) == [{"num": 1, "dates": "1906-c. 2010"}]
    assert atlas_html.write_eras(path, [{"num": 1, "dates": "1906-c. 2010"}]) is False
    assert atlas_html.read_movements(path)[0]["id"] == "movement-a"
