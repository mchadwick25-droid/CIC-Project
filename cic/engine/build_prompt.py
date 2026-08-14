#!/usr/bin/env python3
"""The clean system's ONE permanent-prompt builder, for every world.

Carried from the old tree's proven per-world assemblers (six copies of
the same thin file) and their shared segment framework, collapsed to a
single world-generic engine: the per-world voice lives in each world's
craft RECORD, the assembly lives here, once.

Proof of non-corruption: `--parity FILE` byte-compares the built prompt
against a deployed prompt file and fails on any difference.

  python cic/engine/build_prompt.py --world syriac
  python cic/engine/build_prompt.py --world syriac --parity DEPLOYED.txt
"""
from __future__ import annotations

import argparse
import difflib
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # cic/
sys.path.insert(0, str(HERE))

from segments import ASSEMBLY_ORDER  # noqa: E402
from worlds import WORLDS  # noqa: E402


def load_records(records_root: Path, subdir: str) -> dict[str, dict]:
    out = {}
    d = records_root / subdir
    if not d.is_dir():
        return out
    for p in sorted(d.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        parts = text.split("---\n")
        rec = yaml.safe_load(parts[1])
        rec["_body"] = "---\n".join(parts[2:])
        out[rec["id"]] = rec
    return out


def build_context(world_key: str) -> dict:
    w = WORLDS[world_key]
    records_root = ROOT / "records" / w["records_dir"]
    craft = load_records(records_root, "craft")[w["craft_id"]]
    return {
        "terms": load_records(records_root, "term"),
        "stories": load_records(records_root, "story"),
        "claims": load_records(records_root, "contested_claim"),
        "figures": load_records(records_root, "figure"),
        "gravities": load_records(records_root, "gravity"),
        "world_core": load_records(records_root, "world_core")[w["world_core_id"]],
        "voice_profile": load_records(records_root, "voice_profile")[w["voice_profile_id"]],
        "sources": load_records(records_root, "source"),
        "demonstrations": load_records(records_root, "demonstration"),
        "ambient": load_records(records_root, "ambient"),
        "craft": craft["paragraphs"],
        "claim_renders": craft.get("claim_renders", {}),
    }


def est_tokens(text: str) -> int:
    return len(text) // 4


def check_readability(prompt: str, world_key: str) -> dict:
    """The reading-floor gate, enforced for rebuilt worlds."""
    try:
        from gates import readability_check
    except ModuleNotFoundError:
        print("[readability] SKIPPED - textstat not installed")
        return {}
    result = readability_check(prompt)
    rebuilt = WORLDS[world_key].get("rebuilt", False)
    if result["violations"]:
        level = "ENFORCED FAIL" if rebuilt else "warning (pre-rebuild text)"
        print(f"[readability] {level}: FK {result['fk_grade']}, FRE {result['fre']}")
        for v in result["violations"]:
            print(f"  - {v}")
        if rebuilt:
            raise SystemExit(f"readability gate failed for {world_key} (rebuilt=True)")
    else:
        print(f"[readability] pass: FK {result['fk_grade']}, FRE {result['fre']}")
    return result


def assemble(world_key: str) -> tuple[str, dict]:
    ctx = build_context(world_key)
    rendered, manifest_segments = [], []
    post_history = None
    for seg in ASSEMBLY_ORDER:
        text = seg["render"](ctx)
        entry = {
            "name": seg["name"],
            "cache_stability": seg["cache_stability"],
            "eviction_priority": seg["eviction_priority"],
            "sources": seg["sources"],
            "chars": len(text) if text else 0,
            "est_tokens": est_tokens(text) if text else 0,
        }
        if text:
            rendered.append(text)
        if seg.get("post_history"):
            post_history = seg["post_history"]
        manifest_segments.append(entry)

    prompt = "\n\n".join(rendered) + "\n"
    static_total = sum(s["est_tokens"] for s in manifest_segments
                       if s["cache_stability"] == "static")
    ground = next(s for s in manifest_segments if s["name"] == "world_ground")
    manifest = {
        "view": "permanent_prompt (clean engine, one builder for every world)",
        "world_id": WORLDS[world_key]["world_id"],
        "segments": manifest_segments,
        "post_history_guard": post_history,
        "budget": {
            "world_ground_est_tokens": ground["est_tokens"],
            "static_total_est_tokens": static_total,
        },
    }
    return prompt, manifest


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--world", required=True, choices=sorted(WORLDS))
    p.add_argument("--parity", help="deployed prompt file to byte-compare against")
    p.add_argument("--no-readability", action="store_true")
    args = p.parse_args()

    prompt, manifest = assemble(args.world)
    if not args.no_readability:
        manifest["readability"] = check_readability(prompt, args.world)

    out_dir = ROOT / "deploy" / args.world
    out_dir.mkdir(parents=True, exist_ok=True)
    w = WORLDS[args.world]
    (out_dir / w["prompt_filename"]).write_text(prompt, encoding="utf-8", newline="\n")
    (out_dir / "prompt_segment_manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\n")
    for s in manifest["segments"]:
        print(f"{s['name']:20s} {s['cache_stability']:8s} "
              f"ev={s['eviction_priority']} tokens~{s['est_tokens']}")
    print(f"wrote {out_dir / w['prompt_filename']}")

    if args.parity:
        deployed = Path(args.parity).read_text(encoding="utf-8")
        if prompt == deployed:
            print("PARITY: byte-identical to deployed")
            return 0
        print("PARITY: FAIL - built prompt differs from deployed:")
        for line in list(difflib.unified_diff(
                deployed.splitlines(), prompt.splitlines(),
                "deployed", "built", lineterm=""))[:40]:
            print("  " + line)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
