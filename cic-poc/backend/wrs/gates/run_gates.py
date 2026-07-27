"""S1.3 gate runner (`wrs_gates`).

  python wrs/gates/run_gates.py --selftest
      The S1.3 checkpoint: every gate must PASS its clean fixture and FAIL
      every seeded-defect fixture; the readability/coverage/parroting
      instruments must land on their fixture expectations. Deterministic;
      exit 0 = checkpoint green; emits the markdown report on stdout.

  python wrs/gates/run_gates.py --records <dir> [--profile default|backfill]
                                 [--voice-material <file>]
      Run the record-set gates against real records (used from S2.1 onward).
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))

from wrs.gates import core, fixtures
from wrs.gates.content_coverage import check_coverage
from wrs.metrics.parroting import parroting_score

GATES = {
    "referential": lambda rs, vm: core.gate_referential_integrity(rs),
    "reciprocity": lambda rs, vm: core.gate_reciprocity(rs),
    "completion": lambda rs, vm: core.gate_field_completion(rs, "default"),
    "narratability": lambda rs, vm: core.gate_figure_narratability(rs, vm),
    "quote_recording": lambda rs, vm: core.gate_quote_fidelity_recording(rs),
    "sentinel": lambda rs, vm: core.gate_no_sentinel_conditions(rs),
}


def selftest() -> int:
    failures = []
    print("# wrs_gates self-test (S1.3 checkpoint)\n")

    clean = fixtures.clean_set()
    print("## Clean fixture set - every gate must pass\n")
    print("| gate | violations | status |")
    print("|---|---|---|")
    for name, fn in GATES.items():
        v = fn(clean, fixtures.CLEAN_VOICE_MATERIAL)
        ok = not v
        if not ok:
            failures.append(f"clean set failed {name}: {v}")
        print(f"| {name} | {len(v)} | {'PASS' if ok else 'FAIL (unexpected)'} |")

    print("\n## Seeded-defect sets - every gate must fail its seeds\n")
    print("| gate | seed | violations | status |")
    print("|---|---|---|---|")
    for name, seeds in fixtures.seeded_sets().items():
        fn = GATES[name]
        for label, rs in seeds:
            v = fn(rs, fixtures.CLEAN_VOICE_MATERIAL)
            caught = bool(v)
            if not caught:
                failures.append(f"seeded defect NOT caught: {name} / {label}")
            print(f"| {name} | {label} | {len(v)} | {'CAUGHT' if caught else 'MISSED'} |")

    print("\n## Readability instrument (values from parameters.yaml reading_floor)\n")
    ok_r = core.readability_check(fixtures.READABLE_TEXT)
    bad_long = core.readability_check(fixtures.UNREADABLE_LONG)
    bad_jarg = core.readability_check(fixtures.UNREADABLE_JARGON)
    print(f"- clean prose: FK {ok_r['fk_grade']}, FRE {ok_r['fre']} -> "
          f"{'PASS' if not ok_r['violations'] else 'FAIL (unexpected)'}")
    print(f"- Marius-reconstruction long-sentence passage: FK {bad_long['fk_grade']}, "
          f"FRE {bad_long['fre']} -> {'CAUGHT' if bad_long['violations'] else 'MISSED'}")
    print(f"- jargon-dense passage: FK {bad_jarg['fk_grade']}, FRE {bad_jarg['fre']} -> "
          f"{'CAUGHT' if bad_jarg['violations'] else 'MISSED'}")
    if ok_r["violations"]:
        failures.append(f"readable fixture failed: {ok_r}")
    if not bad_long["violations"] or not bad_jarg["violations"]:
        failures.append("a seeded unreadable fixture was not caught")

    print("\n## Content-coverage parity instrument (F7; S2.2's checkpoint program)\n")
    cc_ok = check_coverage(**{"chunk_body": fixtures.COVERAGE_CLEAN["chunk"],
                              "record_fields": fixtures.COVERAGE_CLEAN["fields"],
                              "logged_drops": fixtures.COVERAGE_CLEAN["drops"]})
    cc_lost = check_coverage(fixtures.COVERAGE_LOST["chunk"],
                             fixtures.COVERAGE_LOST["fields"], fixtures.COVERAGE_LOST["drops"])
    cc_dup = check_coverage(fixtures.COVERAGE_DUP["chunk"],
                            fixtures.COVERAGE_DUP["fields"], fixtures.COVERAGE_DUP["drops"])
    print(f"- clean migration: {cc_ok['covered']}/{cc_ok['total']} covered, "
          f"{len(cc_ok['missing'])} missing, {len(cc_ok['duplicated'])} duplicated -> "
          f"{'PASS' if not cc_ok['missing'] and not cc_ok['duplicated'] else 'FAIL (unexpected)'}")
    print(f"- silently-lost sentence: missing={len(cc_lost['missing'])} -> "
          f"{'CAUGHT' if cc_lost['missing'] else 'MISSED'}")
    print(f"- silently-duplicated sentence: duplicated={len(cc_dup['duplicated'])} -> "
          f"{'CAUGHT' if cc_dup['duplicated'] else 'MISSED'}")
    if cc_ok["missing"] or cc_ok["duplicated"]:
        failures.append("coverage clean fixture failed")
    if not cc_lost["missing"] or not cc_dup["duplicated"]:
        failures.append("a seeded coverage defect was not caught")

    print("\n## Parroting metric (F7; S5.1's instrument)\n")
    p_rec = parroting_score(fixtures.PARROT_SOURCE, fixtures.PARROT_RECITED)
    p_par = parroting_score(fixtures.PARROT_SOURCE, fixtures.PARROT_PARAPHRASE)
    print(f"- verbatim recitation: score {p_rec['score']} "
          f"({p_rec['overlapping']}/{p_rec['spoken_ngrams']} {p_rec['n']}-grams)")
    print(f"- faithful paraphrase: score {p_par['score']} "
          f"({p_par['overlapping']}/{p_par['spoken_ngrams']} {p_par['n']}-grams)")
    if not (p_rec["score"] == 1.0 and p_par["score"] == 0.0):
        failures.append(f"parroting fixture expectations not met: {p_rec['score']}, {p_par['score']}")
    else:
        print("- expectation (recited=1.0, paraphrase=0.0): MET")

    print("\n## Verdict\n")
    if failures:
        print("**SELF-TEST FAILED:**")
        for f in failures:
            print(" -", f)
        return 1
    print("**SELF-TEST GREEN** - all clean fixtures pass, all seeded defects "
          "caught, instruments on expectation. Gate-integrity rule now in "
          "force: gate code changes are their own steps.")
    return 0


def run_records(records_dir: str, profile: str, voice_material: str) -> int:
    from wrs.schema.validate import parse_front_matter
    records = {}
    for p in sorted(Path(records_dir).rglob("*.md")) + sorted(Path(records_dir).rglob("*.yaml")):
        rec = parse_front_matter(p)
        records[rec["id"]] = rec
    vm = Path(voice_material).read_text(encoding="utf-8") if voice_material else ""
    total = 0
    for name, fn in GATES.items():
        if name == "completion":
            v = core.gate_field_completion(records, profile)
        else:
            v = fn(records, vm)
        total += len(v)
        print(f"## {name}: {len(v)} violation(s)")
        for x in v:
            print(" -", x)
    print(f"\nTOTAL: {total} violation(s) across {len(records)} records (profile={profile})")
    return 1 if total else 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--selftest", action="store_true")
    p.add_argument("--records")
    p.add_argument("--profile", default="default", choices=["default", "backfill"])
    p.add_argument("--voice-material", default="")
    args = p.parse_args()
    if args.selftest:
        sys.exit(selftest())
    if args.records:
        sys.exit(run_records(args.records, args.profile, args.voice_material))
    p.print_help()


if __name__ == "__main__":
    main()
