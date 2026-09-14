"""S5.5 render-half check - the Brief render live, verified.

The blueprint gives S5.5's checkpoint as M-per-document (the governing-
document pointer wordings, Mark's); this script is the render half's own
re-runnable verification, per rule 2's demand that a next session can
re-derive the result mechanically.

Checks:
  1. determinism - both outputs render byte-identically twice;
  2. deployed views current (--check byte-match);
  3. content coverage - every S2.7a caution row lands WHOLE in both the
     Brief and the runtime cautions text, in record order;
  4. FLAG-015 parking - the Evagrius sentence verbatim under its marked
     delimiter (no silent loss vs the hand string it replaces);
  5. wiring - the manifest serves the render for Desert, hand strings
     for unmigrated worlds, and fails open byte-for-byte when the render
     file is absent;
  6. both facilitator handoff prompts build carrying the rendered text.

Usage (from cic-poc/backend):
  python ../../Ministry/Technology/Pass2/gates/S5.5_brief_render_check.py
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

GATES_DIR = Path(__file__).resolve().parent
BACKEND = GATES_DIR.parents[3] / "cic-poc" / "backend"
for p in (str(BACKEND), str(BACKEND / "wrs" / "views")):
    if p not in sys.path:
        sys.path.insert(0, p)

from facilitation_brief import (  # noqa: E402
    build_brief, build_cautions_text, FLAG015_EVAGRIUS, FLAG015_DELIM,
    DATA_DIR)

ok = True
lines: list[str] = []


def case(name: str, passed: bool, detail: str = "") -> None:
    global ok
    ok = ok and passed
    lines.append(f"- {name}: {'PASS' if passed else 'FAIL'}"
                 + (f" - {detail}" if detail else ""))


def main() -> int:
    lines.append("# S5.5 render-half check")
    lines.append("")

    brief1, brief2 = build_brief(), build_brief()
    caut1, caut2 = build_cautions_text(), build_cautions_text()
    case("determinism", brief1 == brief2 and caut1 == caut2,
         "double render byte-identical")

    chk = subprocess.run(
        [sys.executable, str(BACKEND / "wrs" / "views" / "facilitation_brief.py"),
         "--check"], capture_output=True, text=True, cwd=str(BACKEND))
    case("deployed views current", chk.returncode == 0,
         (chk.stdout or chk.stderr).strip().splitlines()[-1])

    from chunk_views import load_records
    cautions = [c.strip() for c in
                load_records("world_core")["desertcore001"].get("cautions", [])]
    case("caution rows land whole in runtime text",
         all(c in caut1 for c in cautions), f"{len(cautions)} rows")
    case("caution rows land whole in Brief",
         all(c in brief1 for c in cautions), f"{len(cautions)} rows")
    order_ok = True
    pos = -1
    for c in cautions:
        p = caut1.find(c)
        order_ok = order_ok and p > pos
        pos = p
    case("record order preserved", order_ok)
    case("FLAG-015 parking verbatim in both",
         FLAG015_DELIM in caut1 and FLAG015_EVAGRIUS in caut1
         and FLAG015_DELIM in brief1 and FLAG015_EVAGRIUS in brief1,
         "Evagrius sentence + delimiter")

    import app.world_manifest as wm
    desert = next(e for e in wm.WORLD_MANIFEST
                  if e.world_id == "desert-monasticism")
    case("manifest serves the render for Desert",
         "FLAG-015" in desert.facilitator_cautions
         and "diagnostic fusion" in desert.facilitator_cautions)
    others = [e for e in wm.WORLD_MANIFEST
              if e.world_id != "desert-monasticism"]
    case("unmigrated worlds keep hand strings",
         all("FLAG-015" not in e.facilitator_cautions for e in others),
         f"{len(others)} worlds")
    case("fail-open byte-for-byte",
         wm._rendered_cautions("no_such_world", "HAND") == "HAND")

    from app.prompts.facilitator_prompts import (
        get_facilitator_handoff_prompt, get_multi_world_handoff_prompt)
    p1 = get_facilitator_handoff_prompt("desert-monasticism")
    p2 = get_multi_world_handoff_prompt(
        ["desert-monasticism", "syriac-edessa-nisibis"])
    case("single-world handoff prompt carries render",
         "diagnostic fusion" in p1 and "Evagrius" in p1)
    case("multi-world handoff prompt builds with mixed sources",
         "diagnostic fusion" in p2)

    lines.append("")
    lines.append(f"Verdict: {'GREEN' if ok else 'RED'}")
    sys.stdout.write("\n".join(lines) + "\n")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
