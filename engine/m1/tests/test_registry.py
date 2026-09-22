

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
    alexandria's signoffs.json said the four per-world touchpoints did not
    apply to it. They apply, and none has happened."""
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


def test_signoffs_reports_the_worlds_own_actual_registry_state():
    """L-3 (witt go-live adversarial review, 2026-09-20): `state` used to be
    hardcoded to the literal string "built" regardless of the world's own
    real registry state - every admitted or open world's own signoffs.json
    contradicted itself. Confirmed present in witt's, rzg's, don's and
    gallic's packages alike before this fix."""
    from engine.m2.validation import build_signoffs
    import json
    built = json.loads(build_signoffs("witt", is_fixture=False, state="built"))
    assert "state=built" in built["note"] or "(built)" in built["note"]
    admitted = json.loads(build_signoffs("witt", is_fixture=False, state="admitted"))
    assert "admitted" in admitted["note"]
    assert "state=built" not in admitted["note"]
    # the default (no state passed) still reads "built" - the pre-fix
    # behaviour for any caller that hasn't been updated, not a silent
    # behaviour change for code this fix doesn't touch
    default = json.loads(build_signoffs("witt", is_fixture=False))
    assert "built" in default["note"]
    # the four touchpoints are still OUTSTANDING regardless of state
    for payload in (built, admitted, default):
        assert "OUTSTANDING, not waived" in payload["note"]
