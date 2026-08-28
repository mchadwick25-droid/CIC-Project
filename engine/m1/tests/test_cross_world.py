"""The cross-world consistency check's own tests.

Two jobs, and the second is the one that matters. The first pins the fleet's
current state so a future world build cannot introduce a NEW inconsistency
quietly. The second proves the checks can actually see drift at all - a
consistency checker that passes on a tree where nothing is wrong tells you
nothing about whether it would have caught the thing it exists to catch.
"""
from engine.m1 import cross_world


def test_the_fleet_carries_no_undocumented_drift():
    """The exit-code contract. Every defect the fleet holds today is named in
    ACCEPTED_OPEN with the audit finding that owns it; anything else is a
    world that drifted after 2026-08-26 with nothing written up about it."""
    new = cross_world.new_defects(cross_world.run_all())
    assert new == [], "\n".join(f"  {f.key}: {f.message}" for f in new)


def test_every_accepted_open_entry_still_describes_a_real_finding():
    """The waiver list rots the moment a repair lands and nobody removes its
    entry - and a stale waiver is worse than no waiver, because it suppresses
    the check for a drift that could come back."""
    live = {f.key for f in cross_world.run_all() if f.severity == cross_world.DEFECT}
    stale = sorted(set(cross_world.ACCEPTED_OPEN) - live)
    assert stale == [], f"ACCEPTED_OPEN names findings that no longer fire - delete them: {stale}"


def test_the_desert_deep_link_defect_is_caught():
    """The defect this whole audit started from: `census_id: null` on one
    formation world, so its Atlas deep link could never match and every
    'Launch an Interview' click fell through to the world list. Reproduced
    against the real census file, not a fixture, because the check's whole
    claim is about those two files agreeing."""
    registry = cross_world.load_registry()
    worlds = cross_world.formation_world_keys(registry)
    broken = {**registry, "desert": {**registry["desert"], "census_id": None}}
    keys = {f.key for f in cross_world.check_census_link(registry=broken, worlds=worlds)}
    assert "census-id/desert" in keys
    assert "census-orphan/desert-monasticism" in keys
    assert not {f.key for f in cross_world.check_census_link(registry=registry, worlds=worlds)}


def test_a_world_addressing_a_record_type_its_own_way_is_caught():
    """gate_id_convention holds every id to `<world>.<type>.<slug>` but never
    compares the middle segment between worlds, which is how five worlds came
    to say `dw` and one `witness` with the whole battery green."""
    records = {
        "a": {"a.dw.one": {"id": "a.dw.one", "record_type": "doctrinal_witness"}},
        "b": {"b.dw.one": {"id": "b.dw.one", "record_type": "doctrinal_witness"}},
        "c": {"c.witness.one": {"id": "c.witness.one", "record_type": "doctrinal_witness"}},
    }
    findings = cross_world.check_id_type_tokens(records=records, worlds=["a", "b", "c"])
    assert [f.key for f in findings] == ["id-type-token/doctrinal_witness"]
    assert "c address" in findings[0].message and "`<world>.dw.*`" in findings[0].message


def test_a_world_left_out_of_the_frontend_asset_table_is_caught():
    """useWorlds().toEntry returns null for a world with no WORLD_ASSETS
    entry, which drops it from the world list with no error anywhere - a
    seventh world could be built, compiled, admitted and served by
    GET /api/worlds and simply never appear on screen."""
    keys = {f.key for f in cross_world.check_app_world_assets(worlds=cross_world.formation_world_keys() + ["w7"])}
    assert "app-world-assets/w7" in keys
    assert "app-world-order/w7" in keys


def test_a_participant_facing_field_carrying_a_record_id_is_caught():
    records = {
        "wld": {
            "wld.figure.x": {
                "id": "wld.figure.x",
                "record_type": "figure",
                "bridge_line": "A teacher of the school.",
                "dates": {"born": "c. 300 (see wld.source.some-edition)"},
            }
        }
    }
    findings = cross_world.check_participant_field_leaks(records=records, worlds=["wld"])
    assert [f.key for f in findings] == ["ui-field-leak/wld"]
    assert "wld.source.some-edition" in findings[0].message


def test_every_check_defined_in_the_module_is_wired_into_the_report():
    """A check that exists but is missing from CHECKS runs nowhere and fails
    nothing - the quietest way for this file to stop doing its job. Cheap
    guard, and this test is the only thing that would ever notice."""
    defined = {
        name for name, value in vars(cross_world).items()
        if callable(value) and (name.startswith("check_") or name.startswith("observe_"))
    }
    wired = {c.__name__ for c in cross_world.CHECKS}
    assert defined == wired, f"defined but not in CHECKS: {sorted(defined - wired)}"
