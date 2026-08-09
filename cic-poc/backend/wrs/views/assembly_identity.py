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
]

# Worlds whose Phase-2 pass has SHIPPED: deployed is the assembly's own
# output, so byte-identity is the bar, exactly as for Desert. Hieronymian
# joined at the 2026-08-08 swap (checkpoint 4 green, Mark's read of record).
DEPLOYED_WORLDS = [
    # Re-swapped 2026-08-09 after checkpoint 5: the build WITH her
    # contestation renders, on the post-1A block. Her PENDING_RECHECKPOINT
    # entry is removed in this same commit - the resolution that registry
    # always said it required. Zero concessions (cp4 had one), readability
    # clean, fabrication 0.
    ("s62_hal_permanent_prompt", "Hieronymian (Albina)",
     BACKEND / "data" / "hieronymian_world" / "hal_Representative_Permanent_Prompt_Albina.txt"),
    # PAHC joined at the 2026-08-09 swap: checkpoint green on the full 1A
    # bar three times over, Mark's blind paired read of record (4-5 on all
    # six dimensions, all three arms), gloss firing fixed and verified.
    # Deployed prompt is GENERATED - DO NOT HAND-EDIT; rollback is git
    # revert of the swap commit.
    ("s62_pahc_permanent_prompt", "PAHC (Chloe)",
     BACKEND / "data" / "pahc_world" / "pahc_Representative_Permanent_Prompt_Chloe.txt"),
    # IJC joined at the 2026-08-09 swap: checkpoint 4 green on the full 1A
    # bar (readability hard edge PASS across all 14 emitted turns after the
    # four-checkpoint register cure: mid-band fleet rule + petitioner's
    # plain speech + pressure-does-not-formalize), zero concessions,
    # fabrication 0, Mark's swap call in session. GENERATED - DO NOT
    # HAND-EDIT; rollback is git revert of the swap commit.
    ("s62_ijc_permanent_prompt", "IJC (Marius)",
     BACKEND / "data" / "imperial_juridical_world" / "ijc_Representative_Permanent_Prompt_Marius.txt"),
    # SYR joined at the 2026-08-09 swap: checkpoint 1 clean on its FIRST run
    # under the full 1A bar - zero breaches in 14 turns, zero concessions,
    # below baseline on his documented failure measure's symptom.
    ("s62_syr_permanent_prompt", "SYR (Yausep)",
     BACKEND / "data" / "syriac_world" / "syr_Representative_Permanent_Prompt_Yausep.txt"),
    # ALX joined at the 2026-08-09 swap: checkpoint 1 green after Mark's
    # per-world failure-measure ruling (his record states his defect is
    # indirection, NOT length); readability clean across 14 turns, zero
    # concessions, and the documented defect reads cured - all eight turns
    # land the answer first.
    ("s62_alx_permanent_prompt", "Alexandria (Theon)",
     BACKEND / "data" / "alexandria_world" / "alex_Representative_Permanent_Prompt_Theon.txt"),
]

# A deployed world whose assembly has DELIBERATELY moved ahead of what is
# deployed, and which must not be swapped until its checkpoint is re-run.
# Keyed by label, value is the reason - a bare entry is not allowed, because
# the whole point is that the delta stays legible.
#
# This exists so the gate keeps its meaning. Without it the choice is a
# permanently-red gate, which trains everyone to ignore a real signal, or a
# silent swap of un-checkpointed voice content, which is worse. Instead the
# delta is declared here, reported loudly on every run WITH its size, and
# does not fail the build. Removing the entry is part of the swap.
# Emptied once on 2026-08-09 - every earlier declared delta was resolved the
# way this registry always said it must be, by re-running the checkpoint and
# swapping, never by quietly shipping or by deleting the entry (Desert's
# replaced demonstrations, Albina's contestation renders). Refilled the same
# day by the v2 pass rolling from the Chloe pilot to the other five worlds.
# Chloe is deliberately NOT here: her v2 material was already checkpointed
# and swapped, so her assembly stays byte-identical to deployed.
_V2 = ("v2 pass rolled from the Chloe pilot (worklist 4b + 5): an engagement "
       "demonstration authored for this world and selected into the assembly, "
       "displacing one prior demonstration from the cap-3 slot. ")
PENDING_RECHECKPOINT: dict[str, str] = {
    "Desert": _V2 + (
        "desertdemo010 (Abba Moses and the leaking jug, told at the fleet's "
        "tightest measure with its own key_line quoted and a question back), "
        "plus four story records gaining key_line/signature which now render "
        "into the retrieved chunk headers. Displaces desertdemo009."),
    "Hieronymian (Albina)": _V2 + (
        "haldemo010 (the Ciceronian dream, its single-interested-witness "
        "limit carried in the telling, key_line quoted, question back), plus "
        "halstory08 gaining key_line/signature. Displaces haldemo007 from the "
        "third slot; haldemo010 deliberately carries that record's "
        "caveat-in-the-telling function forward on different material."),
    "IJC (Marius)": _V2 + (
        "ijcdemo009 (the vigil in the basilica, told as a story with the "
        "attested/not-attested line drawn inside the telling, question back). "
        "No key_line: this world's story records carry zero quoted lines, and "
        "none was invented. Displaces ijcdemo006."),
    "SYR (Yausep)": _V2 + (
        "syrdemo008 (the Abgar-Addai founding account told as this world's "
        "own account of itself, held there under 'so you made it up', "
        "question back) - and NO quoted line anywhere, because this world's "
        "guard holds that no line of its teaching survives word for word. A "
        "key_line briefly applied to syrstory004 was backed out for the same "
        "reason. Displaces syrdemo007."),
    "Alexandria (Theon)": _V2 + (
        "alexdemo008 (Leonidas and Origen under persecution, the weaker "
        "particulars weighed inside the telling, answer-first throughout, "
        "question back). No key_line: this world's ten story records carry "
        "zero quoted lines, and none was invented. Displaces alexdemo007."),
}


def check_desert() -> bool:
    import permanent_prompt
    importlib.reload(permanent_prompt)
    prompt, _ = permanent_prompt.assemble()
    deployed = DEPLOYED_DESERT.read_text(encoding="utf-8")
    if prompt == deployed:
        if "Desert" in PENDING_RECHECKPOINT:
            print("[assembly-identity] Desert: FAIL - declared in "
                  "PENDING_RECHECKPOINT but assembly is byte-identical to "
                  "deployed. Resolve the registry.")
            return False
        print("[assembly-identity] Desert: PASS - byte-identical to deployed")
        return True
    if "Desert" in PENDING_RECHECKPOINT:
        delta = len(prompt.split()) - len(deployed.split())
        print(f"[assembly-identity] Desert: PENDING RE-CHECKPOINT (declared, "
              f"not a regression) - assembly is {delta:+d} words vs deployed. "
              f"DO NOT SWAP until the checkpoint is re-run.\n"
              f"    reason: {PENDING_RECHECKPOINT['Desert']}")
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
        if label in PENDING_RECHECKPOINT:
            print(f"[assembly-identity] {label}: FAIL - declared in "
                  "PENDING_RECHECKPOINT but assembly is byte-identical to "
                  "deployed. Either the swap happened and the entry was not "
                  "removed, or the delta was reverted. Resolve the registry.")
            return False
        print(f"[assembly-identity] {label}: PASS - byte-identical to deployed")
        return True
    if label in PENDING_RECHECKPOINT:
        delta = len(prompt.split()) - len(deployed.split())
        print(f"[assembly-identity] {label}: PENDING RE-CHECKPOINT "
              f"(declared, not a regression) - assembly is {delta:+d} words "
              f"vs deployed. DO NOT SWAP until the checkpoint is re-run.\n"
              f"    reason: {PENDING_RECHECKPOINT[label]}")
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
