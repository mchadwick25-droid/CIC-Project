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
