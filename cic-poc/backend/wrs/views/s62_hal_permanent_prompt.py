"""Voice Rebuild Phase 0.3 (2026-08-08) - Hieronymian's real §5.1
Permanent Prompt assembly, generalized from
wrs/views/permanent_prompt.py (Desert's S52 assembler) onto the
now-generic segments/ framework. Replaces the DELIBERATELY TEMPORARY
s62_hal_capsule_prompt_views.py's prompt half for this purpose (that
script's capsule half is unaffected - capsule reconciliation is a
separate Phase 0.3 item).

Hieronymian's craft table (segments/craft_hal.py) is deliberately empty
this phase - see that file's own docstring. This assembler is the real,
durable engineering (record paths, ids, the S52 pattern wired
correctly); Phase 2 authors this world's voice fresh from its own
records.

Outputs:
  staging/hieronymian_world/hal_Representative_Permanent_Prompt_S52.txt
  staging/hieronymian_world/hal_prompt_segment_manifest.json

Usage (from cic-poc/backend):
  python wrs/views/s62_hal_permanent_prompt.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(BACKEND))

RECORDS = BACKEND / "wrs" / "records" / "hieronymian_world"
STAGING = HERE / "staging" / "hieronymian_world"

from segments import ASSEMBLY_ORDER  # noqa: E402
from segments.craft_hal import HAL_CLAIM_RENDERS, HAL_CRAFT  # noqa: E402


def load_records(subdir: str) -> dict[str, dict]:
    out = {}
    for p in sorted((RECORDS / subdir).glob("*.md")):
        text = p.read_text(encoding="utf-8")
        parts = text.split("---\n")
        rec = yaml.safe_load(parts[1])
        rec["_body"] = "---\n".join(parts[2:])
        out[rec["id"]] = rec
    return out


def build_context() -> dict:
    return {
        "terms": load_records("term"),
        "stories": load_records("story"),
        "claims": load_records("contested_claim"),
        "figures": load_records("figure"),
        "gravities": load_records("gravity"),
        "world_core": load_records("world_core")["halcore001"],
        "voice_profile": load_records("voice_profile")["halvoice001"],
        "sources": load_records("source"),
        "demonstrations": load_records("demonstration"),
        "craft": HAL_CRAFT,
        "claim_renders": HAL_CLAIM_RENDERS,
    }


def est_tokens(text: str) -> int:
    return len(text) // 4


def assemble() -> tuple[str, dict]:
    ctx = build_context()
    rendered, manifest_segments = [], []
    post_history = None
    for seg in ASSEMBLY_ORDER:
        text = seg["render"](ctx)
        entry = {
            "name": seg["name"],
            "cache_stability": seg["cache_stability"],
            "eviction_priority": seg["eviction_priority"],
            "sources": seg["sources"],
        }
        if text:
            rendered.append(text)
            entry["chars"] = len(text)
            entry["est_tokens"] = est_tokens(text)
        else:
            entry["chars"] = 0
            entry["est_tokens"] = 0
        if seg.get("post_history"):
            post_history = seg["post_history"]
        manifest_segments.append(entry)

    prompt = "\n\n".join(rendered) + "\n"
    ground = next(s for s in manifest_segments if s["name"] == "world_ground")
    static_total = sum(s["est_tokens"] for s in manifest_segments
                      if s["cache_stability"] == "static")
    manifest = {
        "view": "permanent_prompt (S5.2 pattern, Phase 0.3 generalization)",
        "world_id": "hieronymian-ascetic-literary",
        "segments": manifest_segments,
        "post_history_guard": post_history,
        "budget": {
            "world_ground_est_tokens": ground["est_tokens"],
            "world_ground_budget": "3000-5000 (§5.1; today's capsule folded in)",
            "static_total_est_tokens": static_total,
        },
        "quick_reach": "absent - craft table empty this phase (craft_hal.py)",
    }
    return prompt, manifest


def main() -> None:
    prompt, manifest = assemble()
    STAGING.mkdir(parents=True, exist_ok=True)
    (STAGING / "hal_Representative_Permanent_Prompt_S52.txt").write_text(
        prompt, encoding="utf-8", newline="\n")
    (STAGING / "hal_prompt_segment_manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\n")
    for s in manifest["segments"]:
        print(f"{s['name']:20s} {s['cache_stability']:8s} "
              f"ev={s['eviction_priority']} tokens~{s['est_tokens']}")
    print(f"world_ground ~{manifest['budget']['world_ground_est_tokens']} "
          f"tokens; static total ~{manifest['budget']['static_total_est_tokens']}")


if __name__ == "__main__":
    main()
