"""engine.m3.admission_conform: an admitted world needs a passing (or ruled)
live admission report on its pinned package hash, under the current shape."""
from engine.m3.admission_conform import check

REG = {"w": {"state": "admitted", "package": {"manifest_hash": "sha256:new"}},
       "b": {"state": "building", "package": {"manifest_hash": "sha256:x"}}}


SHAPE = "sha256:shape"


def _report(h, failed=(), shape=SHAPE):
    return {"path": "r.json", "world": "w", "manifest_hash": h, "shape_hash": shape, "pass_count": 28 - len(failed), "battery_size": 28, "failed": sorted(failed)}


def test_a_full_pass_on_the_pinned_hash_conforms():
    assert check(REG, [_report("sha256:new")], [], shape=SHAPE) == []


def test_a_report_on_an_older_package_does_not_count():
    failures = check(REG, [_report("sha256:old")], [], shape=SHAPE)
    assert len(failures) == 1 and "no live admission report" in failures[0]


def test_a_shortfall_needs_a_ruling_on_the_same_hash_and_probes():
    run = _report("sha256:new", failed=["c-t-probe-01"])
    assert "no ruling" in check(REG, [run], [], shape=SHAPE)[0]
    assert check(REG, [run], [{"world": "w", "manifest_hash": "sha256:new", "failing_probes": ["c-t-probe-01"]}], shape=SHAPE) == []
    assert check(REG, [run], [{"world": "w", "manifest_hash": "sha256:old", "failing_probes": ["c-t-probe-01"]}], shape=SHAPE) != []
    assert check(REG, [run], [{"world": "w", "manifest_hash": "sha256:new", "failing_probes": ["f1-e-probe-01"]}], shape=SHAPE) != []


def test_a_report_under_an_older_shape_does_not_count():
    failures = check(REG, [_report("sha256:new", shape="sha256:old-shape")], [], shape=SHAPE)
    assert len(failures) == 1 and f"under shape {SHAPE}" in failures[0]


def test_worlds_not_admitted_are_not_checked():
    assert check({"b": REG["b"]}, [], [], shape=SHAPE) == []


def test_a_report_on_the_same_compiled_files_counts_after_a_validation_only_repin():
    run = {**_report("sha256:old"), "compiled_hash": "sha256:compiled"}
    assert check(REG, [run], [], shape=SHAPE, compiled_of=lambda entry: "sha256:compiled") == []
    assert check(REG, [run], [], shape=SHAPE, compiled_of=lambda entry: "sha256:changed") != []


def test_a_ruling_on_the_same_compiled_files_covers_the_shortfall():
    run = {**_report("sha256:old", failed=["c-t-probe-01"]), "compiled_hash": "sha256:compiled"}
    ruling = {"world": "w", "compiled_hash": "sha256:compiled", "failing_probes": ["c-t-probe-01"]}
    assert check(REG, [run], [ruling], shape=SHAPE, compiled_of=lambda entry: "sha256:compiled") == []


def test_the_content_hash_ignores_provenance_the_validation_report_and_the_record_copy():
    from engine.m2.compiler import compile_world
    from engine.m2.manifest import compiled_content_hash
    one = compile_world(world_key="fix", package_id="A", records_commit="a", compiler_version="a")
    two = compile_world(world_key="fix", package_id="B", records_commit="b", compiler_version="b")
    assert one["compiled/frame.json"] != two["compiled/frame.json"]
    assert compiled_content_hash(one) == compiled_content_hash(two)
    moved = {**one, "validation/gates-report.json": b"{}", "records/x.json": b"{}"}
    assert compiled_content_hash(moved) == compiled_content_hash(one)
    assert compiled_content_hash({**one, "compiled/prompt.txt": b"changed"}) != compiled_content_hash(one)


def _package(root, files: dict[str, bytes], world="w"):
    import json as _json
    from engine.m2.canonical import sha256_prefixed
    root.mkdir(parents=True)
    for rel, content in files.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_bytes(content)
    manifest = {"world_key": world, "files": {rel: sha256_prefixed(c) for rel, c in files.items()}}
    (root / "manifest.json").write_text(_json.dumps(manifest))
    return manifest


def test_a_legacy_report_counts_through_its_package_binding(tmp_path):
    import json as _json
    from engine.m2.manifest import manifest_hash
    from engine.m3 import admission_conform as ac
    manifest = _package(tmp_path / "old", {"compiled/prompt.txt": b"the world"})
    bindings = tmp_path / "bindings.json"
    ac.bind([tmp_path / "old"], "abc123", path=bindings)
    old = manifest_hash(manifest)
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir()
    (reports_dir / "live-admission-report-w.json").write_text(_json.dumps({
        "run_settings": {"package_manifest_hash": {"w": old}, "shape_hash": SHAPE},
        "worlds": {"w": {"battery_size": 28, "pass_count": 28, "per_probe": []}},
    }))
    original = ac.REPO_ROOT
    ac.REPO_ROOT = tmp_path
    try:
        reports = ac.load_reports(reports_dir, bindings=ac.load_bindings(bindings))
    finally:
        ac.REPO_ROOT = original
    registry = {"w": {"state": "admitted", "package": {"manifest_hash": "sha256:new", "location": "x"}}}
    pinned = ac.load_bindings(bindings)[old]
    assert check(registry, reports, [], shape=SHAPE, compiled_of=lambda e: pinned) == []
    assert check(registry, reports, [], shape=SHAPE, compiled_of=lambda e: "sha256:other")


def test_bind_refuses_a_package_whose_files_do_not_match_its_manifest(tmp_path):
    import pytest
    from engine.m3 import admission_conform as ac
    _package(tmp_path / "old", {"compiled/prompt.txt": b"the world"})
    (tmp_path / "old" / "compiled" / "prompt.txt").write_bytes(b"changed")
    with pytest.raises(ValueError):
        ac.bind([tmp_path / "old"], "abc123", path=tmp_path / "bindings.json")


def test_the_command_reports_by_default_and_fails_only_when_enforced(monkeypatch, capsys):
    import sys
    from engine.m3 import admission_conform as ac
    monkeypatch.setattr(ac, "load_registry", lambda: {})
    monkeypatch.setattr(ac, "load_reports", lambda: [])
    monkeypatch.setattr(ac, "load_rulings", lambda: [])
    monkeypatch.setattr(ac, "check", lambda registry, reports, rulings: ["w: no live admission report"])
    monkeypatch.setattr(sys, "argv", ["admission_conform"])
    assert ac.main() == 0
    assert "stale world(s)" in capsys.readouterr().out
    monkeypatch.setattr(sys, "argv", ["admission_conform", "--enforce"])
    assert ac.main() == 1
    assert "enforced" in capsys.readouterr().out
    monkeypatch.setattr(ac, "check", lambda registry, reports, rulings: [])
    assert ac.main() == 0
