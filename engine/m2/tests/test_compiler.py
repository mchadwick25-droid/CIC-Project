import json

from engine.m2.checks import determinism_twice
from engine.m2.compiler import compile_and_hash
from engine.m2.loader_stub import PackageRefused, verify_package_dict

FIXED_ARGS = dict(
    world_key="fix",
    package_id="TEST-FIXED-PACKAGE-ID",
    records_commit="TEST-FIXED-RECORDS-COMMIT",
    compiler_version="TEST-FIXED-COMPILER-VERSION",
)


def test_determinism_twice_byte_identical():
    diffs = determinism_twice(**FIXED_ARGS)
    assert diffs == []


def test_gates_report_is_clean_on_the_fixture_world():
    package, _ = compile_and_hash(**FIXED_ARGS)
    report = json.loads(package["validation/gates-report.json"])
    assert report["overall_pass"] is True, report


def test_stub_loader_accepts_a_correct_hash():
    package, digest = compile_and_hash(**FIXED_ARGS)
    verify_package_dict(package, digest)  # must not raise


def test_stub_loader_refuses_a_wrong_manifest_hash():
    package, _ = compile_and_hash(**FIXED_ARGS)
    try:
        verify_package_dict(package, "sha256:0000000000000000000000000000000000000000000000000000000000000000")
        assert False, "expected PackageRefused"
    except PackageRefused:
        pass


def test_stub_loader_refuses_a_tampered_file():
    package, digest = compile_and_hash(**FIXED_ARGS)
    tampered = dict(package)
    tampered["compiled/prompt.txt"] = tampered["compiled/prompt.txt"] + b"\ntampered"
    try:
        verify_package_dict(tampered, digest)
        assert False, "expected PackageRefused"
    except PackageRefused:
        pass


def test_prompt_and_capsule_and_chunks_carry_no_generated_by_header():
    package, _ = compile_and_hash(**FIXED_ARGS)
    assert b"generated-by" not in package["compiled/prompt.txt"]
    assert b"generated-by" not in package["compiled/capsule.md"]
    for path, content in package.items():
        if path.startswith("compiled/chunks/"):
            assert b"generated-by" not in content


def test_build_provenance_never_ships_in_repository_json():
    """The record store is the workshop, the
    compiled package is the instrument. search_record rows and the
    reviewer-facing fields (why_sources_cannot_answer, modern_lens_note)
    stay in the store - gates still validate them - and never ship.
    Measured before the change: ~250 instances of build language in the
    fleet's compiled packages, sitting inside the retrieval fallback's
    own full-text net."""
    import json

    from engine.m1.loader import load_world_records
    from engine.m2.compiler import compile_and_hash

    package, _digest = compile_and_hash(world_key="pahc", package_id="TEST", records_commit="TEST", compiler_version="TEST")
    shipped = json.loads(package["compiled/repository.json"])["records"]

    assert all(r.get("record_type") != "search_record" for r in shipped)
    for field in ("why_sources_cannot_answer", "modern_lens_note", "discovery_channel", "narrative_tier_justification"):
        assert all(field not in r for r in shipped), field

    # and the store still carries what the package strips - nothing was
    # cleaned at the wrong layer
    records = load_world_records("pahc")
    assert any(r.get("record_type") == "search_record" for r in records.values())
    assert any("why_sources_cannot_answer" in r for r in records.values())
    assert any("modern_lens_note" in r for r in records.values())
