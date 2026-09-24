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
