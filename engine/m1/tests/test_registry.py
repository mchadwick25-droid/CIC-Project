

def test_the_fixture_is_not_counted_among_the_formation_worlds():
    """There are six worlds a participant could speak to, and one synthetic
    negative control. Reports kept saying seven."""
    from engine.m1.registry import formation_world_keys, is_fixture, load_registry
    reg = load_registry()
    assert len(reg) == 7
    assert formation_world_keys() == ["alx", "desert", "hal", "ijc", "pahc", "syr"]
    assert "fix" not in formation_world_keys()
    assert is_fixture(reg["fix"]) is True
    assert all(not is_fixture(reg[k]) for k in formation_world_keys())


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
