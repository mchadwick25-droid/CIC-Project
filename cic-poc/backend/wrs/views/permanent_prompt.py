"""S5.2 - the real §5.1 Permanent Prompt assembly (replaces the
deliberately-temporary S2.8 generator for the PROMPT side; the capsule's
world-ground content now lives inside the assembly's own world_ground
segment).

Every part named, sourced from records, carrying eviction_priority and
cache_stability, ordered by change frequency (static -> session -> turn)
- §5.1's table made literal in wrs/views/segments/. Outputs:

  staging/desert_Representative_Permanent_Prompt_S52.txt  (assembled static prompt)
  staging/desert_prompt_segment_manifest.json             (the specified assembly)

The manifest carries per segment: cache_stability, eviction_priority,
record sources, characters, and an estimated token count - plus the
§5.1 world-ground budget check (3,000-5,000 tokens) and the post-history
guard text the runtime wires closest to generation.

What never enters generation context (§5.1): world_meaning scholarly
bodies, key_sources apparatus, Author-Gravity notes, gravity codes,
Modern Hearing analysis - the segment renders read voice-register fields
only, through the shared apparatus-stripping helper.

Deterministic: same records -> byte-identical outputs.

Usage (from cic-poc/backend):
  python wrs/views/permanent_prompt.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(BACKEND))

from chunk_views import load_records, STAGING  # noqa: E402
from segments import ASSEMBLY_ORDER  # noqa: E402


def build_context() -> dict:
    return {
        "terms": load_records("term"),
        "stories": load_records("story"),
        "claims": load_records("contested_claim"),
        "figures": load_records("figure"),
        "gravities": load_records("gravity"),
        "world_core": load_records("world_core")["desertcore001"],
        "voice_profile": load_records("voice_profile")["desertvoice001"],
        "sources": load_records("source"),
        "demonstrations": load_records("demonstration"),
    }


def est_tokens(text: str) -> int:
    # the standing chars/4 estimate - reported, never billed
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
            entry["runtime_supplied"] = seg["cache_stability"] != "static"
        if seg.get("post_history"):
            post_history = seg["post_history"]
        manifest_segments.append(entry)

    prompt = "\n\n".join(rendered) + "\n"
    ground = next(s for s in manifest_segments if s["name"] == "world_ground")
    static_total = sum(s["est_tokens"] for s in manifest_segments
                      if s["cache_stability"] == "static")
    manifest = {
        "view": "permanent_prompt (S5.2, Pass 1 §5.1)",
        "world_id": "desert-monasticism",
        "segments": manifest_segments,
        "post_history_guard": post_history,
        "budget": {
            "world_ground_est_tokens": ground["est_tokens"],
            "world_ground_budget": "3000-5000 (§5.1; today's capsule folded in)",
            "static_total_est_tokens": static_total,
        },
        "quick_reach": "deliberately absent - S5.3 (R7), gated on B-PARROT per F3",
    }
    return prompt, manifest


def main() -> None:
    prompt, manifest = assemble()
    STAGING.mkdir(parents=True, exist_ok=True)
    (STAGING / "desert_Representative_Permanent_Prompt_S52.txt").write_text(
        prompt, encoding="utf-8", newline="\n")
    (STAGING / "desert_prompt_segment_manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\n")
    for s in manifest["segments"]:
        print(f"{s['name']:20s} {s['cache_stability']:8s} "
              f"ev={s['eviction_priority']} tokens~{s['est_tokens']}")
    print(f"world_ground ~{manifest['budget']['world_ground_est_tokens']} "
          f"tokens; static total ~{manifest['budget']['static_total_est_tokens']}")


if __name__ == "__main__":
    main()
