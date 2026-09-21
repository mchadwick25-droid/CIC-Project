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
    claim is about those two files agreeing.

    The real registry can legitimately carry its OWN census-link findings
    (e.g. census-id/don, ACCEPTED_OPEN since don's 2026-09-16 admission -
    a world admitted but not yet census-synced is a real, disclosed,
    structurally expected gap, the same one gallic's own now-closed
    census-id/gallic entry named) - this test only asserts that nothing
    UNDOCUMENTED slips through, same filter test_the_fleet_carries_no_
    undocumented_drift already applies fleet-wide."""
    registry = cross_world.load_registry()
    worlds = cross_world.formation_world_keys(registry)
    broken = {**registry, "desert": {**registry["desert"], "census_id": None}}
    keys = {f.key for f in cross_world.check_census_link(registry=broken, worlds=worlds)}
    assert "census-id/desert" in keys
    assert "census-orphan/desert-monasticism" in keys
    live_keys = {f.key for f in cross_world.check_census_link(registry=registry, worlds=worlds)}
    assert live_keys <= set(cross_world.ACCEPTED_OPEN)


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


def test_a_world_missing_from_table_html_is_caught():
    """table.html carries its own hand-maintained WORLDS array for the
    Table's seat-picker, independent of both WORLD_ASSETS and the site's
    traditions pages - the exact gap that left gallic admitted, live, and
    working for Interview, but never offered as a Table seat for four days.
    Reproduced against the real file, not a fixture, so the check's own
    claim (every admitted world's census_id is in the real array) is
    actually tested, not just its parsing logic."""
    registry = cross_world.load_registry()
    worlds = cross_world.formation_world_keys(registry)
    broken = {**registry, "w7": {"census_id": "not-a-real-census-id-in-table-html"}}
    keys = {f.key for f in cross_world.check_table_html_worlds(registry=broken, worlds=worlds + ["w7"])}
    assert "table-html-world/w7" in keys
    assert not {f.key for f in cross_world.check_table_html_worlds(registry=registry, worlds=worlds)}


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


def test_register_profile_math_on_a_constructed_example():
    """`_register_profile`'s own arithmetic, pinned against hand-counted
    input rather than trusted from the fleet's own numbers alone: a
    three-word fragment, a quoted aside exempt from the plain band (the
    Register Bar's own rule), and one spaced dash."""
    texts = [
        'Too short.',
        'A longer sentence that runs on a while - and then keeps going, saying "a quoted run that should not count toward word length" before it finally stops.',
    ]
    p = cross_world._register_profile(texts)
    assert p["n"] == 2
    # word counts: "Too short." = 2; the second text, quoted span stripped
    # and its bare dash token excluded, = 17. median_low of [2, 17] is 2.
    assert p["median_words"] == 2
    # each text is one sentence (the quoted span's own period is gone with
    # it); the longer one is the 17-word one above.
    assert p["longest_sentence"] == 17
    assert p["fragment_ratio"] == 0.5
    # one spaced " - " across 2 + 17 = 19 total words.
    assert p["dash_per_100w"] == round(100 * 1 / 19, 2)


def test_register_profile_skips_a_field_no_record_in_the_world_uses():
    """A field with zero texts in a world (an unused optional field) must
    not print a false zero - `_field_texts` returning `[]` should mean the
    field is left out of the report entirely, not scored as empty."""
    assert cross_world._field_texts({}, "story", "tellable_as") == []


def test_observe_register_profile_runs_clean_on_the_real_fleet():
    """Report-only per this stage's own bar: must never raise, and every
    finding it emits stays an OBSERVATION, never a DEFECT that could fail
    a build ahead of R6's own ruling."""
    registry = cross_world.load_registry()
    worlds = cross_world.formation_world_keys(registry)
    records = {w: cross_world.load_world_records(w) for w in worlds}
    findings = cross_world.observe_register_profile(records=records, worlds=worlds)
    assert findings
    assert all(f.severity == cross_world.OBSERVATION for f in findings)
    assert any(f.scope == "hal" and "story.tellable_as" in f.message for f in findings)


def _voice_craft(guard: str) -> dict:
    return {"record_type": "voice_craft", "guard": guard}


def test_outside_help_guard_does_not_false_positive_on_felt_weight():
    """R19's own retrofit list depends on this scan being right. A first
    version matched the bare substring "weigh", which silently caught
    rzg's real guard text ("the felt weight of either") - honest-thinness
    prose with no distress-comparison content at all - and produced a
    wrong RULED list. Pinned here so that regression can't come back."""
    records = {"w": {"r1": _voice_craft("It does not give him the felt weight of either.")}}
    findings = cross_world.observe_outside_help_guard(records=records, worlds=["w"])
    assert findings[0].message == "voice_craft.guard does not carry don-style distress-comparison language"


def test_outside_help_guard_still_catches_a_real_match():
    """The fix must not overcorrect into never matching anything - "weigh"
    and its own real inflections, as a whole word, still fire."""
    records = {
        "measures": {"r1": _voice_craft("Never measured against our own dead.")},
        "weighs": {"r1": _voice_craft("A trouble is never weighed against a martyr's death.")},
        "weighing": {"r1": _voice_craft("No weighing of a living person's grief against ours.")},
    }
    findings = cross_world.observe_outside_help_guard(records=records, worlds=["measures", "weighs", "weighing"])
    assert all(f.message == "voice_craft.guard carries don-style distress-comparison language" for f in findings)


def test_observe_outside_help_guard_on_the_real_fleet_finds_only_don():
    """The corrected, real fleet state (2026-09-21, after the false-positive
    fix above): don is the only one of the 11 built worlds whose guard
    actually carries this language - rzg's earlier "carries" finding was
    the false positive test_outside_help_guard_does_not_false_positive_on_
    felt_weight now pins. This is R19's own real retrofit list: every OTHER
    world here is a gap."""
    registry = cross_world.load_registry()
    worlds = cross_world.formation_world_keys(registry)
    records = {w: cross_world.load_world_records(w) for w in worlds}
    findings = cross_world.observe_outside_help_guard(records=records, worlds=worlds)
    carries = {f.scope for f in findings if "carries" in f.message}
    assert carries == {"don"}


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
