#!/usr/bin/env python3
"""Run the gates over a world's records in the clean system.

Carried from the old tree's gate runner at the clean-room setup.
gates.py is the proven gate module carried whole - the checks
that actually execute are the one part of the old system this rebuild
exists to preserve.

  python cic/engine/run_gates.py --world syriac
  python cic/engine/run_gates.py --world syriac --voice-material FILE
  python cic/engine/run_gates.py --selftest
"""
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # cic/
sys.path.insert(0, str(HERE))

import gates as core  # noqa: E402
from validate import parse_front_matter  # noqa: E402

GATES = {
    "referential": lambda r, vm: core.gate_referential_integrity(r),
    "reciprocity": lambda r, vm: core.gate_reciprocity(r),
    "completion": lambda r, vm: core.gate_field_completion(r),
    "narratability": lambda r, vm: core.gate_figure_narratability(r, vm),
    "quote_recording": lambda r, vm: core.gate_quote_fidelity_recording(r),
    "sentinel": lambda r, vm: core.gate_no_sentinel_conditions(r),
    "discovery_instrument": lambda r, vm: core.gate_discovery_instrument(r),
    "priority_review": lambda r, vm: core.gate_priority_review_trigger(r),
    "alias_safety": lambda r, vm: core.gate_alias_safety(r, vm),
    "distribution_health": lambda r, vm: core.gate_distribution_health(r),
    "confidence_source_crosscheck":
        lambda r, vm: core.gate_confidence_source_crosscheck(r),
    "mechanism_coverage": lambda r, vm: core.gate_mechanism_coverage(r),
    "texts_registry": lambda r, vm: core.gate_texts_registry(r),
}

# Gates whose real behaviour does not depend on the `records` dict the
# runner always passes - texts_registry checks cic/texts/ against its own
# ENTRIES manifest, which no world's own record set determines. Varying
# `records` cannot exercise a defect in a gate like this (the seeded-set
# trick every other gate's test relies on), so selftest() tests these
# through a separate, explicit path instead of the generic per-gate loop -
# see selftest()'s own comment at the exemption for why.
BESPOKE_TESTED = {"texts_registry"}


BASELINE_PATH = HERE / "gate_baseline.json"


def load_records(records_dir: Path) -> dict:
    records = {}
    for p in sorted(records_dir.rglob("*.md")):
        rec = parse_front_matter(p)
        records[rec["id"]] = rec
    return records


def gate_counts(records: dict, vm: str = "") -> dict:
    """{gate_name: violation count} - advisory findings excluded.

    The ratchet's unit. Advisory entries are split out here exactly as the
    printing path splits them, so a gate reporting behind _NOTE_PREFIX
    (mechanism_coverage today) can never trip the check - which is what
    keeps the advisory decision of 2026-08-15 true in CI and not just at
    the console.
    """
    out = {}
    for name, fn in GATES.items():
        violations, _notes = core.split_alias_reports(fn(records, vm))
        out[name] = len(violations)
    return out


def run_records(records_dir: Path, voice_material: str) -> int:
    records = load_records(records_dir)
    vm = Path(voice_material).read_text(encoding="utf-8") if voice_material else ""
    total = 0
    advisory_total = 0
    for name, fn in GATES.items():
        v = fn(records, vm)
        v, notes = core.split_alias_reports(v)
        total += len(v)
        advisory_total += len(notes)
        print(f"## {name}: {len(v)} violation(s)"
              + (f" (+{len(notes)} advisory)" if notes else ""))
        for x in v:
            print(" -", x)
        # Advisory findings are PRINTED, not just counted. split_alias_reports
        # has always documented them as "printed but never counted"; this
        # runner counted them and printed nothing, so the whole advisory
        # channel was write-only - a gate could report a real finding and the
        # operator would see a bare number. Fixed here so the channel is
        # usable by any gate that needs to report without blocking
        # (mechanism_coverage is the first).
        for x in notes:
            # "~" already marks the line advisory; the in-string prefix the
            # gate used to route it here would just repeat that.
            print(" ~", x[len(core._NOTE_PREFIX):].lstrip())
    print(f"\nTOTAL: {total} violation(s)"
          + (f", {advisory_total} advisory" if advisory_total else "")
          + f" across {len(records)} records")
    return 0


def selftest() -> int:
    """Prove every gate can PASS a clean set and FAIL a seeded defect.

    gates.py's own docstring has promised this mode since the clean-room
    rebuild ("its --selftest mode runs every gate against the committed
    clean and seeded-defect fixtures"), and gate_fixtures.py has carried
    the fixtures the whole time with ZERO importers anywhere in the repo.
    So the file that states the rule - "A gate that never fails checks
    nothing" - was itself never run. This wires it.

    Three assertions, not two. The third is the one that keeps this honest
    as the fleet grows: every gate the runner executes must HAVE fixtures.
    Without it a new gate joins GATES, is never exercised, and the selftest
    still reports green - which is the same vacuous pass mechanism_coverage
    exists to catch, reappearing one level up. It caught exactly that on
    its first run: mechanism_coverage had no fixtures until this commit.

    BESPOKE_TESTED gates skip the generic loop and get an explicit test
    block below instead - not exempted from proof, tested a different way.
    texts_registry ignores the `records` dict entirely (it checks cic/texts/
    against its own ENTRIES manifest, which no world's records determine),
    so varying `records` between a clean and a seeded case cannot change
    its output at all - the generic loop's whole mechanism for proving a
    gate can fail simply does not apply to it. Silently letting it run
    through the generic loop anyway would look like a valid test while
    actually asserting nothing about the gate's real logic - the clean
    case would only ever be checking today's real, incidentally-clean
    cic/texts/ state, and the seeded case would use fixture `records` the
    gate never reads, so it could never observe a failure. Both problems
    disappear by testing the gate's own pure function directly instead.
    """
    import gate_fixtures as fx
    import texts_registry as tr

    seeded = fx.seeded_sets()
    # Gates whose clean set is not the shared one - their subject matter
    # postdates clean_set()'s own fixtures.
    clean_for = {"mechanism_coverage": fx.mechanism_coverage_clean()}
    failures, checked = [], 0

    missing = sorted(set(GATES) - set(seeded) - BESPOKE_TESTED)
    if missing:
        failures.append(f"gate(s) with NO fixtures at all: {', '.join(missing)} "
                        f"- a gate that is never exercised proves nothing")

    # DETECTION, not blocking. A finding counts whether it lands as a
    # violation or behind _NOTE_PREFIX: whether a gate blocks is a severity
    # decision (mechanism_coverage is advisory by Mark's 2026-08-15 call),
    # while whether it can SEE its defect is what a selftest exists to
    # prove. Counting violations alone made all three coverage seeds look
    # like passes on this mode's first run - an advisory gate would have
    # been permanently unprovable.
    for name, fn in GATES.items():
        if name in BESPOKE_TESTED:
            continue
        clean = clean_for.get(name, fx.clean_set())
        vm = fx.CLEAN_VOICE_MATERIAL
        findings = fn(clean, vm)
        checked += 1
        if findings:
            failures.append(f"{name}: clean set should PASS, got "
                            f"{len(findings)} finding(s): {findings[0]}")
        for label, records in seeded.get(name, []):
            findings = fn(records, vm)
            checked += 1
            if not findings:
                failures.append(f"{name}: seeded defect should FAIL but "
                                f"passed - {label}")

    # texts_registry, bespoke: test registry_problems() (the pure function)
    # directly, with literal data - no real file on disk, no dependency on
    # cic/texts/'s current actual state, exactly the property the generic
    # loop needed but could not get for this gate.
    _CLEAN_H = "Title: Fixture\nRights: Public Domain\n"
    _BAD_H = "Title: Fixture\n(no rights line)\n"
    _ENTRY = tr.TextEntry("fixture.txt", "test", "2026-08-15")
    tr_cases = [
        ("clean", (_ENTRY,), ["fixture.txt"], {"fixture.txt": _CLEAN_H}, False),
        ("orphaned ENTRIES row (declared, file missing)", (_ENTRY,), [], {}, True),
        ("undeclared file (present, no ENTRIES row)", (), ["fixture.txt"],
         {"fixture.txt": _CLEAN_H}, True),
        ("unverifiable rights line", (_ENTRY,), ["fixture.txt"],
         {"fixture.txt": _BAD_H}, True),
    ]
    for label, entries, discovered, headers, expect_problems in tr_cases:
        findings = tr.registry_problems(entries, discovered, headers)
        checked += 1
        if bool(findings) != expect_problems:
            failures.append(f"texts_registry: {label} - expected "
                            f"{'a finding' if expect_problems else 'no finding'}, "
                            f"got {findings!r}")

    print(f"selftest: {checked} case(s) across {len(GATES)} gate(s)")
    if failures:
        print(f"\nFAIL: {len(failures)} problem(s)")
        for f in failures:
            print("  -", f)
        return 1
    print("OK: every gate passes its clean set and fails every seeded defect")
    return 0


def _fleet_counts() -> dict:
    """{world_key: {gate: count}} across every world worlds.py declares."""
    from worlds import WORLDS
    return {
        key: gate_counts(load_records(ROOT / "records" / w["records_dir"]))
        for key, w in sorted(WORLDS.items())
    }


def check_against_baseline() -> int:
    """A RATCHET, not an absolute floor - the CI mode.

    The six built worlds carry ~194 violations between them, every one of
    them pre-existing and none of them introduced by the change under test.
    A runner that exits non-zero on any violation would be red on its first
    run and every run after, and a permanently-red check is one people learn
    to ignore - worse than no check, because it also launders real
    regressions into familiar noise.

    So this fails on REGRESSION only: a gate whose count rose above the
    committed baseline for that world, or a world with no baseline at all.
    Existing violations are recorded, visible, and do not block; new ones
    cannot land silently. Improvements are reported and never fail - but the
    baseline is not lowered automatically, because a count that drops on its
    own and is then quietly re-consumed is exactly the drift a ratchet
    exists to stop. Lowering it is a deliberate --update-baseline commit.
    """
    if not BASELINE_PATH.exists():
        print(f"no baseline at {BASELINE_PATH.name} - "
              f"run: python cic/engine/run_gates.py --update-baseline")
        return 1

    baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))["worlds"]
    current = _fleet_counts()

    regressions, unbaselined, improvements = [], [], []
    for world, gates_now in current.items():
        if world not in baseline:
            unbaselined.append(world)
            continue
        for gate, n in sorted(gates_now.items()):
            was = baseline[world].get(gate)
            if was is None:
                regressions.append(f"{world}/{gate}: {n} (no baseline for "
                                   f"this gate - new gate needs a baseline)")
            elif n > was:
                regressions.append(f"{world}/{gate}: {was} -> {n} (+{n - was})")
            elif n < was:
                improvements.append(f"{world}/{gate}: {was} -> {n}")

    for world, gates_now in sorted(current.items()):
        total = sum(gates_now.values())
        mark = "  NO BASELINE" if world in unbaselined else ""
        print(f"{world:<22}{total:>4} violation(s){mark}")

    if improvements:
        print(f"\n{len(improvements)} improvement(s) - baseline not lowered "
              f"automatically; commit them with --update-baseline:")
        for x in improvements:
            print("  +", x)

    if unbaselined:
        print(f"\n{len(unbaselined)} world(s) with no recorded baseline: "
              f"{', '.join(unbaselined)}")
        print("  A new world must have its gate state recorded, not inherited "
              "silently. Run --update-baseline and commit the result.")

    if regressions:
        print(f"\nFAIL: {len(regressions)} gate(s) worse than baseline")
        for x in regressions:
            print("  -", x)
        return 1

    if unbaselined:
        return 1
    print("\nOK: no gate is worse than its recorded baseline")
    return 0


def update_baseline() -> int:
    current = _fleet_counts()
    blob = {
        "note": "Per-world, per-gate violation counts as of the date below - "
                "the ratchet floor for run_gates.py --check. Advisory "
                "findings (_NOTE_PREFIX) are excluded by construction and "
                "can never trip the check. Regenerate deliberately, never to "
                "make a failing run pass: the gate-integrity rule at the top "
                "of gates.py governs this file too.",
        "generated": "2026-08-15",
        "worlds": current,
    }
    BASELINE_PATH.write_text(
        json.dumps(blob, indent=1, sort_keys=False) + "\n", encoding="utf-8")
    total = sum(sum(g.values()) for g in current.values())
    print(f"wrote {BASELINE_PATH.name}: {len(current)} world(s), "
          f"{total} violation(s) recorded as the ratchet floor")
    return 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--world")
    p.add_argument("--records")
    p.add_argument("--voice-material")
    p.add_argument("--check", action="store_true",
                   help="CI mode: fail if any gate is worse than its "
                        "recorded baseline (exit 1). Existing violations "
                        "do not fail.")
    p.add_argument("--update-baseline", action="store_true",
                   help="rewrite gate_baseline.json from the current fleet "
                        "state - a deliberate, committed act")
    p.add_argument("--selftest", action="store_true",
                   help="prove every gate passes a clean fixture and fails "
                        "its seeded defects (exit 1 on any failure)")
    args = p.parse_args()
    if args.selftest:
        return selftest()
    if args.update_baseline:
        return update_baseline()
    if args.check:
        return check_against_baseline()
    if args.records:
        return run_records(Path(args.records), args.voice_material)
    if args.world:
        return run_records(ROOT / "records" / args.world, args.voice_material)
    p.error("pass --world, --records, --check or --update-baseline")


if __name__ == "__main__":
    sys.exit(main())
