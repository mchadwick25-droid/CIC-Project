from engine.m6.census_atlas_sync import LIVE_STATUS, compare_edges, sync_atlas


def _census():
    return {
        "movements": [
            {
                "id": "non-built-a",
                "status": "Pre-Survey Candidate",
                "chip": "psc",
                "living": False,
                "why": "Census's own why text.",
                "sources": [{"work": "A Book", "type": "primary"}],
                "documentedStories": [{"title": "A Story"}],
            },
            {
                "id": "built-a",
                "status": LIVE_STATUS,
                "chip": "live",
                "living": True,
                "entry": {"representativeName": "Census's Representative"},
                "why": "Census's built-world why text.",
                "sources": [{"work": "Built World Source", "type": "primary"}],
                "floorNote": "Census's built-world floorNote - should NOT reach atlas.",
            },
            {
                "id": "no-atlas-counterpart",
                "status": "Pre-Survey Candidate",
                "why": "Nobody reads this in the fixture below.",
            },
        ]
    }


def _atlas_movements():
    return [
        {
            "id": "non-built-a",
            "status": "Floor Question (register)",
            "chip": "fq",
            "living": True,
            "why": "Stale atlas why text.",
            "sources": [{"work": "Old Book", "type": "primary"}],
            "documentedStories": None,
        },
        {
            "id": "built-a",
            "status": "Pre-Survey Candidate",
            "chip": "psc",
            "living": False,
            "why": "Built-world why - Atlas doesn't carry this field, must stay untouched.",
            "sources": [{"work": "Stale Built World Source", "type": "primary"}],
        },
        {
            "id": "atlas-only-movement",
            "why": "Not in the census fixture - must be left alone.",
        },
    ]


def test_non_built_world_mirrors_every_field():
    new_movements, changes = sync_atlas(_census(), _atlas_movements())
    m = next(m for m in new_movements if m["id"] == "non-built-a")
    assert m["why"] == "Census's own why text."
    assert m["sources"] == [{"work": "A Book", "type": "primary"}]
    assert m["documentedStories"] == [{"title": "A Story"}]


def test_built_world_only_mirrors_sources_not_why_or_floornote():
    new_movements, changes = sync_atlas(_census(), _atlas_movements())
    m = next(m for m in new_movements if m["id"] == "built-a")
    assert m["sources"] == [{"work": "Built World Source", "type": "primary"}]
    # why is a NON_BUILT_WORLD_FIELDS-only field - a built world's Atlas
    # entry never gets it touched, even though census.json carries one
    assert m["why"] == "Built-world why - Atlas doesn't carry this field, must stay untouched."
    # floorNote isn't even present on this atlas movement - must not be inserted
    assert "floorNote" not in m


def test_movement_missing_from_census_is_left_alone():
    new_movements, changes = sync_atlas(_census(), _atlas_movements())
    m = next(m for m in new_movements if m["id"] == "atlas-only-movement")
    assert m == {"id": "atlas-only-movement", "why": "Not in the census fixture - must be left alone."}


def test_movement_missing_from_atlas_produces_no_change_and_no_crash():
    # "no-atlas-counterpart" exists only in census - sync_atlas must not
    # invent a new Atlas movement for it.
    new_movements, changes = sync_atlas(_census(), _atlas_movements())
    ids = {m["id"] for m in new_movements}
    assert "no-atlas-counterpart" not in ids
    assert all(c["id"] != "no-atlas-counterpart" for c in changes)


def test_no_op_when_already_in_sync():
    census = _census()
    first_pass, _ = sync_atlas(census, _atlas_movements())
    _, changes = sync_atlas(census, first_pass)
    assert changes == []


def test_changes_record_old_and_new_values():
    _, changes = sync_atlas(_census(), _atlas_movements())
    why_change = next(c for c in changes if c["id"] == "non-built-a" and c["field"] == "why")
    assert why_change["old"] == "Stale atlas why text."
    assert why_change["new"] == "Census's own why text."


def test_original_inputs_are_not_mutated():
    census = _census()
    atlas_movements = _atlas_movements()
    sync_atlas(census, atlas_movements)
    assert atlas_movements[0]["why"] == "Stale atlas why text."


def test_structural_fields_sync_for_a_non_built_world():
    new_movements, _ = sync_atlas(_census(), _atlas_movements())
    m = next(m for m in new_movements if m["id"] == "non-built-a")
    assert m["status"] == "Pre-Survey Candidate"
    assert m["chip"] == "psc"
    assert m["living"] is False


def test_structural_fields_sync_for_a_built_world_too():
    """status/chip/living/entry are identity fields, not the prose content
    BUILT_WORLD_FIELDS excludes for a built world - they sync regardless of
    build status, the same as for a non-built world."""
    new_movements, _ = sync_atlas(_census(), _atlas_movements())
    m = next(m for m in new_movements if m["id"] == "built-a")
    assert m["status"] == LIVE_STATUS
    assert m["chip"] == "live"
    assert m["living"] is True
    assert m["entry"] == {"representativeName": "Census's Representative"}
    # sources (an actual BUILT_WORLD_FIELDS field) still syncs as before
    assert m["sources"] == [{"work": "Built World Source", "type": "primary"}]
    # why (a NON_BUILT_WORLD_FIELDS-only field) still stays untouched
    assert m["why"] == "Built-world why - Atlas doesn't carry this field, must stay untouched."


def _edge(**over):
    base = {"from": "a", "to": "b", "type": "formed", "confidence": "Documented", "note": "A note."}
    base.update(over)
    return base


def test_compare_edges_agrees_when_identical():
    assert compare_edges({"edges": [_edge()]}, [_edge()]) == []


def test_compare_edges_ignores_order():
    other = _edge(**{"from": "c", "to": "d"})
    assert compare_edges({"edges": [_edge(), other]}, [other, _edge()]) == []


def test_compare_edges_reports_a_differing_note_with_atlas_value_as_old():
    changes = compare_edges({"edges": [_edge(note="Census note.")]}, [_edge(note="Atlas note.")])
    assert changes == [{"id": "a > b (formed)", "field": "note", "old": "Atlas note.", "new": "Census note."}]


def test_compare_edges_reports_a_differing_confidence():
    changes = compare_edges({"edges": [_edge(confidence="Contested")]}, [_edge()])
    assert [(c["field"], c["old"], c["new"]) for c in changes] == [("confidence", "Documented", "Contested")]


def test_compare_edges_reports_an_edge_only_in_the_census():
    changes = compare_edges({"edges": [_edge()]}, [])
    assert changes == [{"id": "a > b (formed)", "field": "edge", "old": None, "new": _edge()}]


def test_compare_edges_reports_an_edge_only_in_the_atlas():
    changes = compare_edges({"edges": []}, [_edge()])
    assert changes == [{"id": "a > b (formed)", "field": "edge", "old": _edge(), "new": None}]


def test_compare_edges_keys_on_type_so_two_types_between_one_pair_stay_distinct():
    census = {"edges": [_edge(), _edge(type="argued against", note="Other.")]}
    assert compare_edges(census, [_edge(), _edge(type="argued against", note="Other.")]) == []
    changes = compare_edges(census, [_edge()])
    assert [c["id"] for c in changes] == ["a > b (argued against)"]


def test_compare_edges_does_not_mutate_inputs():
    census = {"edges": [_edge(note="Census note.")]}
    atlas_edges = [_edge(note="Atlas note.")]
    compare_edges(census, atlas_edges)
    assert atlas_edges == [_edge(note="Atlas note.")]
    assert census == {"edges": [_edge(note="Census note.")]}
