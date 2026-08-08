"""Voice Rebuild Phase 0.3 (2026-08-08) - PAHC's real §5.1 Permanent
Prompt assembly, generalized from wrs/views/permanent_prompt.py
(Desert's S52 assembler) onto the now-generic segments/ framework.
Replaces the DELIBERATELY TEMPORARY s62_pahc_capsule_prompt_views.py's
prompt half for this purpose (that script's capsule half is unaffected
- capsule reconciliation is a separate Phase 0.3 item).

PAHC (Chloe)'s own craft table lives in segments/craft_pahc.py - a
verbatim port of her currently deployed prompt (see that file's own
docstring for exactly what it does and does not carry: no grounding_
anchor, no quick_reach, no contested-claim renders, no demonstrations -
all confirmed absent from her deployed file, not omitted by oversight).

Outputs:
  staging/pahc_world/pahc_Representative_Permanent_Prompt_S52.txt
  staging/pahc_world/pahc_prompt_segment_manifest.json

Usage (from cic-poc/backend):
  python wrs/views/s62_pahc_permanent_prompt.py
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

RECORDS = BACKEND / "wrs" / "records" / "pahc_world"
STAGING = HERE / "staging" / "pahc_world"

from segments import ASSEMBLY_ORDER  # noqa: E402
from segments.craft_pahc import PAHC_CLAIM_RENDERS, PAHC_CRAFT  # noqa: E402
from segments.rebuilt_status import REBUILT  # noqa: E402

WORLD_ID = "post-apostolic-house-church"


def load_records(subdir: str) -> dict[str, dict]:
    """Same flat-dict shape as chunk_views.py's own load_records
    (Desert's), reimplemented per-world per this codebase's established
    convention (five other view types already do this: chunk_views,
    capsule_prompt_views, probe_parity, prompt_coverage, render_parity,
    retrieval_parity)."""
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
        "world_core": load_records("world_core")["pahccore001"],
        "voice_profile": load_records("voice_profile")["pahcvoice001"],
        "sources": load_records("source"),
        "demonstrations": load_records("demonstration"),
        "craft": PAHC_CRAFT,
        "claim_renders": PAHC_CLAIM_RENDERS,
    }


def est_tokens(text: str) -> int:
    return len(text) // 4


def check_readability(prompt: str) -> dict:
    """Voice Rebuild Phase 0.3: the fleet-wide reading_floor
    (wrs/parameters.yaml) wired at assembly time. Warn-only until
    REBUILT[WORLD_ID] is True (segments/rebuilt_status.py) - enforcing
    against un-rebuilt text would go red on content only Phase 2 fixes."""
    try:
        from wrs.gates.core import readability_check
    except ModuleNotFoundError:
        print("\n[readability] SKIPPED - textstat not installed in this environment")
        return {}
    result = readability_check(prompt)
    rebuilt = REBUILT.get(WORLD_ID, False)
    if result["violations"]:
        level = "ENFORCED FAIL" if rebuilt else "warning (not yet enforced - pre-rebuild text)"
        print(f"\n[readability] {level}: FK {result['fk_grade']}, FRE {result['fre']}")
        for v in result["violations"]:
            print(f"  - {v}")
        if rebuilt:
            raise SystemExit(f"readability gate failed for {WORLD_ID} (rebuilt=True)")
    else:
        print(f"\n[readability] pass: FK {result['fk_grade']}, FRE {result['fre']}")
    return result


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
        "world_id": "post-apostolic-house-church",
        "segments": manifest_segments,
        "post_history_guard": post_history,
        "budget": {
            "world_ground_est_tokens": ground["est_tokens"],
            "world_ground_budget": "3000-5000 (§5.1; today's capsule folded in)",
            "static_total_est_tokens": static_total,
        },
        "quick_reach": "absent - confirmed not present in Chloe's deployed prompt (craft_pahc.py's own note)",
    }
    return prompt, manifest


def main() -> None:
    prompt, manifest = assemble()
    manifest["readability"] = check_readability(prompt)
    STAGING.mkdir(parents=True, exist_ok=True)
    (STAGING / "pahc_Representative_Permanent_Prompt_S52.txt").write_text(
        prompt, encoding="utf-8", newline="\n")
    (STAGING / "pahc_prompt_segment_manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\n")
    for s in manifest["segments"]:
        print(f"{s['name']:20s} {s['cache_stability']:8s} "
              f"ev={s['eviction_priority']} tokens~{s['est_tokens']}")
    print(f"world_ground ~{manifest['budget']['world_ground_est_tokens']} "
          f"tokens; static total ~{manifest['budget']['static_total_est_tokens']}")


if __name__ == "__main__":
    main()
