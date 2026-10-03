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
