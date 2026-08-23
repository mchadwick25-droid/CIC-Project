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


# ---------------------------------------------------------------------------
# The compile-time gate (PR #24 review).
#
# compile_world embedded validation/demonstration-net.json and returned a
# full package regardless of what it said, and cmd_build printed a
# manifest_hash and exited 0 - so a package citing records it does not
# contain could be built, registered and merged, which is the exact silent
# failure the check was added to close. No test exercised this path at all.
# ---------------------------------------------------------------------------
import pytest

from engine.m2.compiler import compile_world
from engine.m2.demo_net import DemonstrationNetFailure, raise_on_unresolvable


def test_an_unresolvable_tag_refuses_the_compile_rather_than_shipping_it():
    """The original defect, as the gate now sees it: [[world.term.example]]
    is a placeholder that reached live model input in all seven worlds."""
    report = {"findings": [{"kind": "unresolvable_tag", "record_id": "world.term.example",
                            "detail": "prompt.txt cites [[world.term.example]], which is not a record in this package"}]}
    with pytest.raises(DemonstrationNetFailure) as exc:
        raise_on_unresolvable(report, "alx")
    assert "world.term.example" in str(exc.value)
    assert "alx" in str(exc.value)


def test_a_withheld_sentence_is_reported_but_does_not_refuse_the_compile():
    """Deliberately asymmetric. A withheld demonstration sentence can be a
    genuine content question - syr's heresiological sentence has no single
    record clearing the floor - and the honest fix is a human decision about
    records or wording. A compiler that refuses to build until someone makes
    that call turns the check into something to switch off."""
    report = {"findings": [{"kind": "withheld_sentence", "demonstration_id": "syr.demo.x",
                            "tags": [], "why": "specific claim with no citation tag", "sentence": "..."}]}
    raise_on_unresolvable(report, "syr")  # must not raise


def test_the_real_fixture_world_compiles_and_carries_a_passing_report():
    package = compile_world(
        world_key="fix", package_id="test", records_commit="test", compiler_version="test"
    )
    report = json.loads(package["validation/demonstration-net.json"])
    assert report["pass"] is True
    assert report["unresolvable_tag_count"] == 0
