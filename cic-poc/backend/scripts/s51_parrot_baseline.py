"""S5.1 - B-PARROT: the parroting baseline (blueprint S5.1; G + B).

Measures Pass 1 §5.3's n-gram overlap (wrs/metrics/parroting.py, built at
S1.3 per F7 - n=6, deterministic, no LLM) for every sampled live
representative turn against that world's own always-in-context prompt
material, in two declared configurations:

  prompt_only   - the world's deployed Permanent Prompt file (the
                  blueprint's letter: "the six deployed prompt files")
  prompt_capsule- Permanent Prompt + World Capsule (the stricter
                  companion: both are always-present static material a
                  Representative could recite)

Sample: every representative spoken turn recoverable from
cic-poc/backend/transcripts/ (the legacy per-session JSON transcripts
AND the S4.2+ event logs), deduplicated, deterministically ordered, then
capped at MAX_PER_WORLD turns per world by seeded shuffle (seed "s51").
transcripts/ is gitignored (pilot data), so the sampled turns themselves
are committed beside the baseline (B-PARROT_sample.jsonl) - the B is
re-derivable from committed material alone (session-contract rule 2).

Outputs (committed under Ministry/Technology/Pass2/baselines/):
  B-PARROT.json         - per-world stats (mean/max/std, both configs)
  B-PARROT_sample.jsonl - the sampled turns with per-turn scores

G: the whole run is deterministic - double-run byte-identical.

Usage (from cic-poc/backend):
  python scripts/s51_parrot_baseline.py
"""
from __future__ import annotations

import json
import random
import statistics
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))

from app.config import settings  # noqa: E402
from app.world_manifest import WORLD_MANIFEST  # noqa: E402
from wrs.metrics.parroting import parroting_score  # noqa: E402

TRANSCRIPTS = BACKEND / "transcripts"
OUTDIR = BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "baselines"
MAX_PER_WORLD = 20
N = 6

REP_NAME_TO_WORLD = {}
for entry in WORLD_MANIFEST:
    rep = entry.representative_name.lower().replace(" ", "_")
    REP_NAME_TO_WORLD[rep] = entry.world_id


def collect_turns() -> dict[str, list[str]]:
    """world_id -> unique representative turn texts, deterministic order."""
    turns: dict[str, dict[str, None]] = {e.world_id: {} for e in WORLD_MANIFEST}

    # legacy per-session JSON transcripts (overwrite-style files)
    for p in sorted(TRANSCRIPTS.glob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        msgs = data.get("messages") or []
        wids = data.get("world_ids") or ([data.get("world_id")]
                                          if data.get("world_id") else [])
        for m in msgs:
            name = (m.get("name") or "").lower()
            wid = REP_NAME_TO_WORLD.get(name)
            if wid is None and len(wids) == 1 and name and name != "facilitator":
                wid = wids[0]
            if wid and m.get("content"):
                turns.setdefault(wid, {})[str(m["content"]).strip()] = None

    # S4.2+ event logs
    for p in sorted((TRANSCRIPTS / "events").glob("*.jsonl")):
        try:
            lines = p.read_text(encoding="utf-8").splitlines()
        except Exception:
            continue
        for line in lines:
            try:
                ev = json.loads(line)
            except Exception:
                continue
            if ev.get("type") != "spoken_message":
                continue
            payload = ev.get("payload") or {}
            name = (payload.get("name") or "").lower()
            wid = REP_NAME_TO_WORLD.get(name)
            if wid and payload.get("text"):
                turns.setdefault(wid, {})[str(payload["text"]).strip()] = None

    return {wid: list(d.keys()) for wid, d in turns.items()}


def main() -> None:
    sources = {}
    for entry in WORLD_MANIFEST:
        wc = settings.get_world_config(entry.world_id)
        prompt = wc.permanent_prompt_path.read_text(encoding="utf-8")
        capsule = wc.world_capsule_path.read_text(encoding="utf-8")
        sources[entry.world_id] = {"prompt_only": prompt,
                                   "prompt_capsule": prompt + "\n\n" + capsule}

    all_turns = collect_turns()
    rng = random.Random("s51")
    results, sample_rows = {}, []
    for wid in sorted(all_turns):
        pool = sorted(all_turns[wid])
        rng.shuffle(pool)
        sample = pool[:MAX_PER_WORLD]
        per_config: dict[str, list[float]] = {"prompt_only": [],
                                              "prompt_capsule": []}
        for turn in sample:
            row = {"world_id": wid, "turn": turn}
            for cfg, src in sources[wid].items():
                s = parroting_score(src, turn, n=N)
                row[cfg] = s
                per_config[cfg].append(s["score"])
            sample_rows.append(row)
        if not sample:
            results[wid] = {"turns_sampled": 0}
            continue
        results[wid] = {"turns_sampled": len(sample)}
        for cfg, scores in per_config.items():
            results[wid][cfg] = {
                "mean": round(statistics.mean(scores), 4),
                "max": round(max(scores), 4),
                "std": round(statistics.pstdev(scores), 4),
            }

    doc = {
        "baseline": "B-PARROT",
        "step": "S5.1",
        "instrument": "wrs/metrics/parroting.py",
        "n": N,
        "max_per_world": MAX_PER_WORLD,
        "sample_seed": "s51",
        "source_definitions": {
            "prompt_only": "the world's deployed Permanent Prompt file",
            "prompt_capsule": "Permanent Prompt + World Capsule (stricter companion)",
        },
        "worlds": results,
    }
    OUTDIR.mkdir(parents=True, exist_ok=True)
    (OUTDIR / "B-PARROT.json").write_text(
        json.dumps(doc, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8", newline="\n")
    with (OUTDIR / "B-PARROT_sample.jsonl").open("w", encoding="utf-8",
                                                 newline="\n") as f:
        for row in sample_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    for wid in sorted(results):
        r = results[wid]
        if r["turns_sampled"]:
            print(f"{wid}: n={r['turns_sampled']} prompt_only mean="
                  f"{r['prompt_only']['mean']} max={r['prompt_only']['max']} "
                  f"std={r['prompt_only']['std']}")
        else:
            print(f"{wid}: no sampled turns")


if __name__ == "__main__":
    main()
