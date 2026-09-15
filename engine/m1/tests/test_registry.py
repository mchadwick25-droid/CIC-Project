

def test_the_fixture_is_not_counted_among_the_formation_worlds():
    """The registry holds exactly one synthetic negative control (the
    fixture) plus however many real formation worlds are currently admitted
    - a count that grows over the project's life. A hardcoded total here
    ("seven worlds") is what caused this test itself to need fixing every
    time a world was added (six, then seven, now eight); assert the
    invariant - exactly one fixture, everything else is formation - instead,
    so admitting a ninth world never requires touching this test again."""
    from engine.m1.registry import KIND_FORMATION, formation_world_keys, is_fixture, kind_of, load_registry
    reg = load_registry()
    fixture_keys = [k for k, v in reg.items() if is_fixture(v)]
    assert fixture_keys == ["fix"], "exactly one synthetic fixture, keyed 'fix'"
    assert formation_world_keys(reg) == sorted(k for k in reg if k != "fix")
    assert len(formation_world_keys(reg)) == len(reg) - 1
    assert "fix" not in formation_world_keys(reg)
    assert is_fixture(reg["fix"]) is True
    assert all(not is_fixture(reg[k]) for k in formation_world_keys(reg))
    assert all(kind_of(reg[k]) == KIND_FORMATION for k in formation_world_keys(reg))


def test_a_formation_world_is_not_told_its_touchpoints_are_waived():
    """Every world's package used to carry the fixture's own note, so
    alexandria's signoffs.json said Mark's four touchpoints did not apply
    to it. They apply, and none has happened."""
    from engine.m2.validation import build_signoffs
    import json
    real = json.loads(build_signoffs("alx", is_fixture=False))
    assert "OUTSTANDING, not waived" in real["note"]
    assert "synthetic fixture world" not in real["note"]
    fixture = json.loads(build_signoffs("fix", is_fixture=True))
    assert "synthetic fixture world" in fixture["note"]
    # neither ever claims a touchpoint happened
    for payload in (real, fixture):
        assert payload["identity_touchpoint"] is None and payload["admission_read"] is None
