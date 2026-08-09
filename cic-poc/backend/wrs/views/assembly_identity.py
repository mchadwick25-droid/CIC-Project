"""Voice Rebuild Phase 0.3 (2026-08-08) - assembly-identity gate.

Blueprint 0.3's [G] item: "assembly-identity check wired (deployed file
== assembly output, per world, in CI or the gate runner)." Checkpoint 0's
bar is explicit that this means two different things per world:

- Desert: her S52 assembly (permanent_prompt.py) must be byte-identical
  to the currently deployed prompt (data/desert_world/..._Papnoute.txt).
  This is the "already true" bar Checkpoint 0 names, and it is a hard
  fail here - Desert's craft table is a verbatim transcription, so any
  drift is a real regression, not an expected difference.
- The other five worlds: identity with deployed is explicitly NOT
  expected yet (deployed stays hand-authored until each world's own
  Phase-2 pass authors fresh voice from records - and even PAHC's
  full-content careful port groups paragraphs by segment rather than
  preserving the deployed file's original interleaved paragraph order,
  so a diff against deployed is expected even where content matches
  word-for-word). What IS required of these five is STABILITY:
  assembling twice from the same records produces byte-identical output
  (deterministic by construction - see each assembler's own docstring).

Run: python wrs/views/assembly_identity.py
Exits nonzero if Desert drifts from deployed, or if any world's assembly
is not deterministic across two runs.
"""
from __future__ import annotations

import importlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(BACKEND))

DEPLOYED_DESERT = BACKEND / "data" / "desert_world" / "desert_Representative_Permanent_Prompt_Papnoute.txt"

# Worlds still awaiting their Phase-2 pass: stability only.
OTHER_WORLDS = [
    ("s62_pahc_permanent_prompt", "PAHC (Chloe)"),
    ("s62_alx_permanent_prompt", "Alexandria (Theon)"),
    ("s62_syr_permanent_prompt", "Syriac (Yausep)"),
    ("s62_ijc_permanent_prompt", "IJC (Marius)"),
]

# Worlds whose Phase-2 pass has SHIPPED: deployed is the assembly's own
# output, so byte-identity is the bar, exactly as for Desert. Hieronymian
# joined at the 2026-08-08 swap (checkpoint 4 green, Mark's read of record).
DEPLOYED_WORLDS = [
    ("s62_hal_permanent_prompt", "Hieronymian (Albina)",
     BACKEND / "data" / "hieronymian_world" / "hal_Representative_Permanent_Prompt_Albina.txt"),
]


def check_desert() -> bool:
    import permanent_prompt
    importlib.reload(permanent_prompt)
    prompt, _ = permanent_prompt.assemble()
    deployed = DEPLOYED_DESERT.read_text(encoding="utf-8")
    if prompt == deployed:
        print("[assembly-identity] Desert: PASS - byte-identical to deployed")
        return True
    print("[assembly-identity] Desert: FAIL - assembly drifted from deployed "
          f"({DEPLOYED_DESERT})")
    return False


def check_stable(module_name: str, label: str) -> bool:
    mod = importlib.import_module(module_name)
    importlib.reload(mod)
    prompt1, _ = mod.assemble()
    prompt2, _ = mod.assemble()
    if prompt1 == prompt2:
        print(f"[assembly-identity] {label}: PASS - deterministic "
              "(identity vs. deployed not expected pre-Phase-2)")
        return True
    print(f"[assembly-identity] {label}: FAIL - non-deterministic assembly")
    return False


def check_deployed(module_name: str, label: str, deployed_path: Path) -> bool:
    mod = importlib.import_module(module_name)
    importlib.reload(mod)
    prompt, _ = mod.assemble()
    deployed = deployed_path.read_text(encoding="utf-8")
    if prompt == deployed:
        print(f"[assembly-identity] {label}: PASS - byte-identical to deployed")
        return True
    print(f"[assembly-identity] {label}: FAIL - assembly drifted from deployed "
          f"({deployed_path})")
    return False


def main() -> int:
    results = [check_desert()]
    for module_name, label, deployed_path in DEPLOYED_WORLDS:
        results.append(check_deployed(module_name, label, deployed_path))
    for module_name, label in OTHER_WORLDS:
        results.append(check_stable(module_name, label))
    if all(results):
        print("\n[assembly-identity] all six worlds PASS")
        return 0
    print("\n[assembly-identity] FAIL - see above")
    return 1


if __name__ == "__main__":
    sys.exit(main())
