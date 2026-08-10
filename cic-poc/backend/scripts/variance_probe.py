"""The variance probe: does the same question get the same answer twice?

Mark's palette test, made runnable (decisions/VR_1A_Conversation_Palette_
2026-08-09.md): "Suppose three people ask exactly the same question. They
shouldn't receive identical responses. One conversation might lean on
Scripture. Another on Chrysostom... That feels like talking with an
educated person rather than querying a database."

No existing battery can see this. Every committed battery asks each
question ONCE, so between-session sameness is invisible to all of them -
the checkpoint's 8-turn probe included. This runs the same question in N
fresh sessions and measures how much the answers overlap with EACH OTHER.

REPORT ONLY, BY DESIGN. Per the Goodhart rule (Voice Design, Mark
2026-08-09: "do not deliberately demonstrate variety"), no threshold is
invented and nothing here is a bar. Turning a variance number into a
target would produce a Representative performing variety, which is the
failure this probe exists to notice - not to optimize against. The score
of record stays the human read.

What it measures, per question, across its sessions:
  - figure overlap    which named people recur in every answer
  - key_line overlap  which record-carried quotable lines recur
  - phrase overlap    mean pairwise Jaccard over 5-grams (wording reuse)
  - opener overlap    do the answers even begin the same way
  - length spread     min/max words

Usage (from cic-poc/backend):
  ANTHROPIC_API_KEY="$CIC_ANTHROPIC_KEY" python scripts/variance_probe.py --world pahc
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

WORLDS = {"pahc": "post-apostolic-house-church",
          "ijc": "imperial-juridical-christianity",
          "alx": "alexandria-catechetical",
          "des": "desert-monasticism",
          "syr": "syriac-edessa-nisibis",
          "hal": "hieronymian-ascetic-literary"}

# Questions chosen so that MORE THAN ONE of the world's own witnesses could
# honestly answer - the only condition under which variance is even possible.
# A question with one true answer SHOULD get the same answer every time, and
# sameness there is fidelity, not a database. Deliberately not reused from
# the checkpoint battery: those probe voice, these probe choice.
QUESTIONS = [
    "What was it actually like to belong to your community?",
    "What did your people believe about how someone should treat a stranger?",
    "Tell me about a time your community faced something hard.",
]


def _grams(text: str, n: int = 5) -> set:
    w = re.findall(r"[a-z']+", text.lower())
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def _jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if (a or b) else 0.0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--world", required=True, choices=sorted(WORLDS))
    ap.add_argument("--sessions", type=int, default=3)
    ap.add_argument("--date", default="2026-08-09")
    args = ap.parse_args()
    world_id = WORLDS[args.world]

    import phase2_checkpoint as cp
    ns = cp.load_probe_definitions()
    client, stream = ns["client"], ns["_stream_turn"]

    from app.world_manifest import WORLD_MANIFEST
    entry = next(e for e in WORLD_MANIFEST if e.world_id == world_id)
    rep = entry.representative_message_name

    import yaml
    key_lines, figures = {}, set()
    root = BACKEND / "wrs" / "records" / f"{args.world}_world"
    for p in (root / "story").glob("*.md") if root.is_dir() else []:
        try:
            front = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
            if front.get("key_line"):
                key_lines[front["id"]] = front["key_line"]
            for m in re.findall(r"\b[A-Z][a-z]{3,}\b", front.get("title", "")):
                figures.add(m)
        except Exception:  # noqa: BLE001
            continue

    results = []
    for qi, question in enumerate(QUESTIONS, 1):
        answers = []
        for s in range(args.sessions):
            r = client.post("/api/session/start", json={"world_id": world_id})
            r.raise_for_status()
            msgs, errs = stream(client, r.json()["session_id"], question,
                                r.json()["session_token"])
            text = next((m["content"] for m in msgs
                         if (m.get("name") or "").lower() == rep), "")
            answers.append(text)
            print(f"  [q{qi} session {s + 1}] {len(text.split())}w", flush=True)

        real = [a for a in answers if a.strip()]
        pairs = list(itertools.combinations(real, 2))
        phrase = [_jaccard(_grams(a), _grams(b)) for a, b in pairs]
        names = [{f for f in figures if f in a} for a in real]
        keys = [{k for k, line in key_lines.items()
                 if re.sub(r"\s+", " ", line)[:60] in re.sub(r"\s+", " ", a)}
                for a in real]
        openers = [" ".join(a.split()[:6]).lower() for a in real]
        results.append({
            "question": question,
            "answers": answers,
            "words": [len(a.split()) for a in real],
            "phrase_overlap_mean": round(statistics.mean(phrase), 3) if phrase else None,
            "phrase_overlap_max": round(max(phrase), 3) if phrase else None,
            "figures_per_answer": [sorted(n) for n in names],
            "figures_in_every_answer": sorted(set.intersection(*names)) if names else [],
            "key_lines_per_answer": [sorted(k) for k in keys],
            "key_lines_in_every_answer": sorted(set.intersection(*keys)) if keys else [],
            "identical_openers": len(set(openers)) < len(openers),
        })

    out = {"world_id": world_id, "sessions_per_question": args.sessions,
           "questions": results,
           "note": "REPORT ONLY - no threshold, never a bar (Goodhart rule, "
                   "Voice Design 2026-08-09). The score of record is the "
                   "human read."}
    OUTDIR.mkdir(parents=True, exist_ok=True)
    path = OUTDIR / f"{args.world}_variance_probe_{args.date}.json"
    path.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                    encoding="utf-8")

    print("\n[vp] ============ VARIANCE ============")
    for r in results:
        print(f"[vp] {r['question'][:58]}")
        print(f"[vp]   words {r['words']} | phrase overlap mean "
              f"{r['phrase_overlap_mean']} max {r['phrase_overlap_max']}")
        print(f"[vp]   figures each answer: {r['figures_per_answer']}")
        print(f"[vp]   in EVERY answer: figures={r['figures_in_every_answer']} "
              f"key_lines={r['key_lines_in_every_answer']}")
        print(f"[vp]   identical openers: {r['identical_openers']}")
    print(f"[vp] written: {path}")
    print("[vp] Report only. High overlap is a finding to read, never a "
          "number to optimize.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
