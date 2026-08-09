"""The cross-world probe: same question, all six worlds.

Mark's own words (Voice Design, 2026-08-09): "This is probably your best
test. Ask the same question to three or four Representatives... You should
get answers that are equally understandable, equally conversational,
roughly similar in accessibility, but deeply different in what each world
notices. That's the proof that you've succeeded. The voice architecture is
shared. The witness is not."

So it measures two things at once, and they pull in opposite directions:

  CONVERGENCE (accessibility)  every world inside the B2 floor, with a
                               tight FK/FRE spread - the shared block and
                               the Writing Standard doing their work
  DIVERGENCE (witness)         low phrase overlap BETWEEN worlds, and each
                               world reaching for its own figures, its own
                               vocabulary, its own concerns

Both are needed. Converged and diverged is the success. Converged without
divergence is FLATTENING - six worlds that read alike. Diverged without
convergence means accessibility is only holding for some worlds.

Runs against DEPLOYED data/ by default, because all six worlds are live -
this tests the shipped fleet, not a candidate tree.

REPORT ONLY, per the Goodhart rule (Voice Design: "do not deliberately
demonstrate variety"). No threshold, never a bar. The score of record is
the human read.

Usage (from cic-poc/backend):
  ANTHROPIC_API_KEY="$CIC_ANTHROPIC_KEY" python scripts/cross_world_probe.py
"""
from __future__ import annotations

import argparse
import itertools
import json
import re
import statistics
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
SCRIPTS = BACKEND / "scripts"
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(SCRIPTS))

OUTDIR = BACKEND.parents[1] / "Ministry" / "Technology" / "Pass2" / "batteries"

# Questions every world can answer from its own formation, none of them
# owned by one world - the condition under which divergence is meaningful.
QUESTIONS = [
    "What does it mean to become a Christian, in your world?",
    "What did your people think a person is for?",
]


def _grams(text: str, n: int = 5) -> set:
    w = re.findall(r"[a-z']+", text.lower())
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default="2026-08-09")
    args = ap.parse_args()

    import phase2_checkpoint as cp
    ns = cp.load_probe_definitions()
    client, stream = ns["client"], ns["_stream_turn"]
    from wrs.gates.core import readability_check
    from app.world_manifest import WORLD_MANIFEST

    worlds = [(e.world_id, e.representative_message_name,
               e.representative_name) for e in WORLD_MANIFEST]

    results = []
    for qi, question in enumerate(QUESTIONS, 1):
        answers = {}
        for world_id, rep, name in worlds:
            r = client.post("/api/session/start", json={"world_id": world_id})
            r.raise_for_status()
            msgs, _ = stream(client, r.json()["session_id"], question,
                             r.json()["session_token"])
            text = next((m["content"] for m in msgs
                         if (m.get("name") or "").lower() == rep), "")
            answers[name] = text
            rr = readability_check(text) if len(text.split()) > 30 else {
                "fk_grade": None, "fre": None}
            print(f"  [q{qi}] {name:<10} {len(text.split()):>4}w  "
                  f"FK {rr['fk_grade']}  FRE {rr['fre']}", flush=True)

        real = {k: v for k, v in answers.items() if len(v.split()) > 30}
        reads = {k: readability_check(v) for k, v in real.items()}
        fks = [r["fk_grade"] for r in reads.values()]
        fres = [r["fre"] for r in reads.values()]
        pairs = list(itertools.combinations(real.items(), 2))
        overlaps = {f"{a[0]}|{b[0]}": round(
            len(_grams(a[1]) & _grams(b[1])) /
            max(len(_grams(a[1]) | _grams(b[1])), 1), 3) for a, b in pairs}
        # words unique to exactly one world's answer (its own concerns)
        vocab = {k: set(re.findall(r"[a-z']{4,}", v.lower())) for k, v in real.items()}
        distinct = {k: sorted(list(vocab[k] - set().union(
            *[vocab[o] for o in vocab if o != k])))[:10] for k in vocab}

        results.append({
            "question": question,
            "answers": answers,
            "readability": {k: {"fk": r["fk_grade"], "fre": r["fre"],
                                "breach": bool(r["violations"])}
                            for k, r in reads.items()},
            "fk_spread": round(max(fks) - min(fks), 2) if fks else None,
            "fk_range": [min(fks), max(fks)] if fks else None,
            "fre_min": min(fres) if fres else None,
            "breaches": [k for k, r in reads.items() if r["violations"]],
            "pairwise_phrase_overlap": overlaps,
            "overlap_mean": round(statistics.mean(overlaps.values()), 4) if overlaps else None,
            "overlap_max": max(overlaps.values()) if overlaps else None,
            "words": {k: len(v.split()) for k, v in real.items()},
            "distinctive_vocabulary": distinct,
        })

    out = {"scope": "DEPLOYED data/ - all six worlds live",
           "questions": results,
           "note": "REPORT ONLY - no threshold, never a bar (Goodhart rule). "
                   "Converged accessibility WITH diverged witness is the "
                   "success; converged without divergence is FLATTENING."}
    OUTDIR.mkdir(parents=True, exist_ok=True)
    path = OUTDIR / f"cross_world_probe_{args.date}.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                    encoding="utf-8")

    print("\n[cw] ========== CROSS-WORLD ==========")
    for r in results:
        print(f"[cw] {r['question']}")
        print(f"[cw]   CONVERGENCE: FK {r['fk_range']} (spread "
              f"{r['fk_spread']}), FRE min {r['fre_min']}, "
              f"breaches: {r['breaches'] or 'none'}")
        print(f"[cw]   DIVERGENCE : phrase overlap mean {r['overlap_mean']} "
              f"max {r['overlap_max']}")
        print(f"[cw]   words: {r['words']}")
        for k, v in r["distinctive_vocabulary"].items():
            print(f"[cw]     {k:<10} {', '.join(v[:7])}")
    print(f"[cw] written: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
