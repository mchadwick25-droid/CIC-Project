"""CI guard for canon/sealed_probes/README.md's access rule: no world-build
code path may reference the sealed plaintext. Scans the world-build tooling
directories (grows as new ones are added - the list is explicit, never a
glob over all of engine/, per Build-Blueprint.md SS6's "a guard pointed at
the wrong tree" landmine) for any mention of the sealed plaintext path.
Cheapest possible guard: no models, no network, just grep - matching this
repo's own stated CI values (.github/workflows/ci.yml).
"""
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# World-build code paths: M1 (gates), M2 (compiler), and this stage's own
# canon-seeding directory (whose seed_admission_paraphrases.py legitimately
# WRITES plaintext/ as the sealing tool - excluded by name below, not by
# directory, so a future file in engine/canon/ that tries to READ it still
# trips the guard). engine/m3 (the admission harness, stage 4) is
# deliberately NOT in this list - it is the one authorized reader
# (canon/sealed_probes/README.md), via engine/m3/sealed_probes.py.
WORLD_BUILD_DIRS = [REPO_ROOT / "engine" / "m1", REPO_ROOT / "engine" / "m2", REPO_ROOT / "engine" / "canon"]
EXCLUDED_FILES = {"seed_admission_paraphrases.py", "check_seal_isolation.py"}
FORBIDDEN_SUBSTRING = "sealed_probes/plaintext"


def find_violations() -> list[str]:
    violations = []
    for directory in WORLD_BUILD_DIRS:
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*.py")):
            if path.name in EXCLUDED_FILES:
                continue
            text = path.read_text(encoding="utf-8")
            if FORBIDDEN_SUBSTRING in text or "sealed_probes" + chr(92) + "plaintext" in text:
                violations.append(str(path.relative_to(REPO_ROOT)))
    return violations


def main() -> int:
    violations = find_violations()
    if violations:
        print("seal isolation violated - these world-build files reference the sealed plaintext path:")
        for v in violations:
            print(f"  {v}")
        return 1
    print("seal isolation OK: no world-build code path references canon/sealed_probes/plaintext")
    return 0


if __name__ == "__main__":
    sys.exit(main())
