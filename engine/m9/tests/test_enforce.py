"""engine/m9/enforce.py's own tests: the two fleet-wide hygiene checks in
the same spirit as engine/m1/tests/test_cross_world.py's own pair, plus the
mechanical rules (SS4.2) proven against small, hand-built `by_world` dicts
rather than the real fleet, so each rule is isolated from every other one.
"""
from engine.m9 import enforce


def test_the_fleet_carries_no_undocumented_drift():
    """Every finding either battery produces against the real, built fleet
    today is named in ACCEPTED_OPEN with the count this run actually found."""
    problems = enforce.hygiene_problems(enforce.collect_findings())
    assert problems == [], "\n".join(f"  {p}" for p in problems)


def test_every_accepted_open_entry_still_describes_a_real_finding():
    """A stale waiver - the repair landed and nobody removed the entry -
    suppresses a check for drift that could come right back."""
    by_world = enforce.collect_findings()
    live = set()
    for world_key, checks in by_world.items():
        for name, findings in checks.items():
            if findings:
                live.add(f"{name}/{world_key}")
    stale = sorted(set(enforce.ACCEPTED_OPEN) - live)
    assert stale == [], f"ACCEPTED_OPEN names findings that no longer fire - delete them: {stale}"


def test_unlisted_finding_is_red():
    assert "m9:a-check-nobody-has-waived/don" not in enforce.ACCEPTED_OPEN
    by_world = {"don": {"m9:a-check-nobody-has-waived": ["a new, unwritten-up finding"]}}
    problems = enforce.hygiene_problems(by_world, today="2026-09-15")
    assert any("unwaived" in p for p in problems)


def test_count_must_match_exactly_fewer_is_stale_more_is_new_drift():
    accepted_count = enforce.ACCEPTED_OPEN["m1:reciprocity/don"].count

    fewer = {"don": {"m1:reciprocity": ["x"] * (accepted_count - 1)}}
    problems = enforce.hygiene_problems(fewer, today="2026-09-15")
    assert any("stale" in p for p in problems)

    more = {"don": {"m1:reciprocity": ["x"] * (accepted_count + 1)}}
    problems = enforce.hygiene_problems(more, today="2026-09-15")
    assert any("new drift" in p for p in problems)


def test_expired_deadline_is_red():
    accepted = enforce.ACCEPTED_OPEN["m1:reciprocity/don"]
    by_world = {"don": {"m1:reciprocity": ["x"] * accepted.count}}
    problems = enforce.hygiene_problems(by_world, today="2099-01-01")
    assert any("deadline" in p and "passed" in p for p in problems)


def test_waiver_naming_a_non_grandfathered_world_is_red(monkeypatch):
    assert "zzz" not in enforce.GRANDFATHERED_WORLDS
    monkeypatch.setattr(enforce, "ACCEPTED_OPEN", {
        "m9:source-kind/zzz": enforce.Waiver(count=1, deadline="2099-01-01", owner="test - a waiver naming an un-grandfathered world"),
    })
    by_world = {"zzz": {"m9:source-kind": ["a finding"]}}
    problems = enforce.hygiene_problems(by_world, today="2026-09-15")
    assert any("not grandfathered" in p for p in problems)


def test_fixture_is_never_grandfathered_no_special_case_needed(monkeypatch):
    """fix must be 100% clean by construction - if it ever isn't, that is
    exactly the drift this gate exists to catch, with no carve-out for it."""
    assert "fix" not in enforce.GRANDFATHERED_WORLDS
    monkeypatch.setattr(enforce, "ACCEPTED_OPEN", {
        "m9:source-kind/fix": enforce.Waiver(count=1, deadline="2099-01-01", owner="test - fix must never be waived"),
    })
    by_world = {"fix": {"m9:source-kind": ["should never happen"]}}
    problems = enforce.hygiene_problems(by_world, today="2026-09-15")
    assert any("not grandfathered" in p for p in problems)


def test_voicing_pair_carve_out_demotes_new_world_findings_to_report_only(monkeypatch):
    """R-4: while PAIRS.yaml has no real pair, a new world's voicing-pair
    findings are report-only, never blocking - every other check still is."""
    monkeypatch.setattr(enforce, "_voicing_pair_carve_out_active", lambda: True)
    monkeypatch.setattr(enforce, "ACCEPTED_OPEN", {})
    assert "zzz" not in enforce.GRANDFATHERED_WORLDS
    by_world = {"zzz": {"m9:voicing-pair": ["a", "b"]}}
    assert enforce.hygiene_problems(by_world, today="2026-09-15") == []
    observed = enforce.report_only(by_world)
    assert any("zzz" in line for line in observed)


def test_voicing_pair_carve_out_never_shields_a_grandfathered_world():
    """The carve-out is for worlds that cannot clear voicing-pair themselves
    yet, not a general amnesty - a grandfathered world's own findings are
    still governed by the normal waiver mechanism."""
    by_world = {"don": {"m9:voicing-pair": ["a new, unwaived finding"]}}
    problems = enforce.hygiene_problems(by_world, today="2026-09-15")
    assert any("unwaived" in p for p in problems)


def test_voicing_pair_carve_out_ends_itself_once_a_real_pair_exists(monkeypatch):
    monkeypatch.setattr(enforce, "_voicing_pair_carve_out_active", lambda: False)
    by_world = {"zzz": {"m9:voicing-pair": ["a real, blocking finding now"]}}
    problems = enforce.hygiene_problems(by_world, today="2026-09-15")
    assert any("unwaived" in p for p in problems)


def test_readability_floor_is_reported_but_never_blocks_or_needs_a_waiver(monkeypatch):
    """gate_readability_floor's own findings (FK < 8, reported not failed)
    must never turn into a hygiene problem - a permanent carve-out, unlike
    R-4's temporary one, so it needs no ACCEPTED_OPEN entry at all."""
    assert "m1:readability-floor/don" not in enforce.ACCEPTED_OPEN
    monkeypatch.setattr(enforce, "ACCEPTED_OPEN", {})
    by_world = {"don": {"m1:readability-floor": ["don.term.x: plain_meaning scores FK grade 3.0, below the band floor of 8 (reported, not failed)"]}}
    assert enforce.hygiene_problems(by_world, today="2026-09-15") == []
    observed = enforce.report_only(by_world)
    assert any("m1:readability-floor/don" in line for line in observed)
