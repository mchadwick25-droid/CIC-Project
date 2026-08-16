#!/usr/bin/env python3
"""The clean system's ONE capsule builder, for every world.

Carried from the old tree's proven per-world capsule assembler (its
capsule half; the 'generated prompt' half was superseded by the segment
assembly in build_prompt.py and stays behind). World-generic: ids and
the display name come from the world table.

  python cic/engine/build_capsule.py --world syriac
  python cic/engine/build_capsule.py --world syriac --parity DEPLOYED.md
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from build_prompt import load_records  # noqa: E402
from worlds import WORLDS  # noqa: E402

APPARATUS = re.compile(
    r"\s*\((?:[^)]*(?:Doc_|SS\d|Phase\s?\d|CO-0|CO-P2|Article\s?\d|"
    r"syrlex|syrdemo|syrstory|syrgrav|syrforce|syrclaim|srcSYR|RCF|"
    r"nodes\.py|Retest|retest|scorer|the S2\.\d|FLAG-\d|"
    r"Construction Notes|project-lead|the chunk|chunk |deployed prompt|guide parable|deletion test)[^)]*)\)")


def voice(text: str) -> str:
    out = APPARATUS.sub("", text or "")
    out = re.sub(r"\s{2,}", " ", out)
    return out.strip()


def build_capsule(world_key: str) -> str:
    w = WORLDS[world_key]
    records_root = ROOT / "records" / w["records_dir"]
    terms = load_records(records_root, "term")
    gravities = load_records(records_root, "gravity")
    stories = load_records(records_root, "story")
    core = load_records(records_root, "world_core")[w["world_core_id"]]

    parts = [f"# World Capsule Core - {w['capsule_display_name']} (generated view)"]
    # Prefer capsule_inhabit and each gravity's capsule_line (the Phase 2
    # voice fields); fall back to the older fields for any world without
    # them - carried behavior, unchanged.
    parts.append("## The World You Inhabit\n\n"
                 + voice(core.get("capsule_inhabit")
                         or re.sub(r"^Doc_01 [^:]*: ", "",
                                   core.get("formation_logic", ""))))
    order = {"Primary": 0, "Supporting": 1, "Tensional": 2}
    ranked = sorted((g for g in gravities.values()
                     if g.get("classification") in order),
                    key=lambda g: (order[g["classification"]], g["id"]))
    PLACE = {"Primary": "at the centre", "Supporting": "supporting",
             "Tensional": "a counter-current"}
    lines = []
    for g in ranked:
        line = voice(g.get("capsule_line") or "") or voice(
            g["six_tests"]["formation"]["verdict"])
        name = voice(g.get("capsule_name") or "") or re.sub(
            r"\s*\([^)]*\)", "", voice(g["name"])).strip()
        lines.append(f"- **{name}** ({PLACE[g['classification']]}): {line}")
    parts.append("## What Organizes Everything\n\n" + "\n".join(lines))
    # Per-world capsule term policy (each world's proven builder differed:
    # Syriac took tiers 1-2 uncapped; Alexandria tier 1 with world_meaning,
    # first 12). Carried as data on the world table, not as code forks.
    tp = w.get("capsule_terms", {"tiers": [1, 2], "require_world_meaning": False, "cap": None})
    vs_lines = []
    for tid in sorted(terms):
        t = terms[tid]
        if (t.get("retrieval") or {}).get("tier") not in tp["tiers"]:
            continue
        if tp["require_world_meaning"] and not t.get("world_meaning"):
            continue
        vs_lines.append(f"**{t['term']}** - {voice(t['quick_meaning'])}")
    if tp["cap"]:
        vs_lines = vs_lines[:tp["cap"]]
    parts.append("## The World's Own Words\n\n" + "\n\n".join(vs_lines))
    st_lines = []
    for sid in sorted(stories):
        s = stories[sid]
        if w.get("capsule_story_style") == "title-only":
            st_lines.append(f"- {voice(s.get('title', ''))}")
        else:
            vsurf = s.get("voice_surface", "").split(" Usage guidance")[0]
            st_lines.append(f"- {voice(s.get('title', ''))}: {voice(vsurf)}")
    parts.append("## What We Tell\n\n" + "\n".join(st_lines))
    return "\n\n".join(parts) + "\n"




def build_capsule_desert(world_key: str) -> str:
    """Desert's own capsule shape, carried verbatim from its proven builder:
    different header order, raw (un-voiced) fields, every term as its
    voice_surface line, and a Cautions close instead of What We Tell."""
    w = WORLDS[world_key]
    records_root = ROOT / "records" / w["records_dir"]
    core = load_records(records_root, "world_core")[w["world_core_id"]]
    gravities = load_records(records_root, "gravity")
    terms = load_records(records_root, "term")
    parts = [f"# World Capsule Core (generated view) - {w['capsule_display_name']}",
             "", "## The World You Inhabit", "",
             str(core.get("capsule_inhabit") or core.get("formation_logic", "")), "",
             "## What Organizes Everything", ""]
    order = {"Primary": 0, "Supporting": 1, "Tensional": 2}
    PLACE = {"Primary": "at the centre", "Supporting": "supporting",
             "Tensional": "a counter-current"}
    for g in sorted(gravities.values(),
                    key=lambda g: (order.get(g.get("classification"), 3), g["id"])):
        line = g.get("capsule_line") or (
            f"{g['six_tests']['formation']['verdict']}; "
            f"{g['six_tests']['explanatory']['verdict']}")
        place = PLACE.get(g.get("classification"), g.get("classification", ""))
        parts.append(f"- **{g['name']}** ({place}): {line}")
    parts += ["", "## The World's Own Words", ""]
    for t in terms.values():
        parts.append(f"- {t['term']}: {t.get('voice_surface', '')}")
    parts += ["", "## Cautions", ""]
    for c in core.get("cautions", []):
        parts.append(f"- {c}")
    return "\n".join(parts) + "\n"

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--world", required=True, choices=sorted(WORLDS))
    p.add_argument("--parity", help="deployed capsule file to byte-compare against")
    args = p.parse_args()
    if WORLDS[args.world].get("capsule_style") == "desert":
        capsule = build_capsule_desert(args.world)
    else:
        capsule = build_capsule(args.world)
    out_dir = ROOT / "deploy" / args.world
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / WORLDS[args.world]["capsule_filename"]
    out.write_text(capsule, encoding="utf-8", newline="\n")
    print(f"wrote {out}")
    if args.parity:
        deployed = Path(args.parity).read_text(encoding="utf-8")
        if capsule == deployed:
            print("PARITY: byte-identical to deployed")
            return 0
        print("PARITY: FAIL - built capsule differs from deployed")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
