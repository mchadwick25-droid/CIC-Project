#!/usr/bin/env python3
"""Build the blinded read pack for the four-cell table experiment (2026-08-10).

Four cells: (Sonnet, Haiku) x (current blocks, v4 blocks), all run through
table_checkpoint.py on the same fixed probe set. This script turns their
artifacts into:

  T2_read_pack_<date>.md   the BLINDED pack - eight conversations (two
                           seatings x four arms), shuffled with a fixed
                           seed, labeled T2-A..D / T3-A..D, with the
                           six-dimension scoresheet after each one.
  T2_read_key_<date>.md    the key - label -> arm, each arm's instrument
                           summary, and the decision arithmetic for the
                           ruled criterion (2026-08-10): Haiku ships if it
                           holds >= 90% of Sonnet's graded quality AND
                           every hard bar outright (hard bars are absolute
                           - fabrication 0, the B2 edge, the we-voice; a
                           bar cannot be 90% held).

Read the pack BEFORE the key. The score of record is the human read
(Goodhart rule, Voice Design 2026-08-09); the instrument numbers in the
key set the floor, never the grade.

Usage (from cic-poc/backend):
  python scripts/table_read_pack.py --date 2026-08-10
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
RUNS = BACKEND.parents[1] / "Ministry" / "Technology" / "Table" / "runs"
OUT = BACKEND.parents[1] / "Ministry" / "Technology" / "Table"

ARMS = {  # arm -> (model, blocks)
    "pre1A-table": ("Sonnet", "current blocks"),
    "haiku-current-table": ("Haiku", "current blocks"),
    "sonnet-v4-table": ("Sonnet", "v4 blocks"),
    "haiku-v4-table": ("Haiku", "v4 blocks"),
}
SHUFFLE_SEED = 20260810  # fixed: the pack must rebuild identically

SCORESHEET = """
> **Score this conversation before moving on.** 1-5 per dimension
> (5 = upper right). Score the conversation as a whole, not one voice.
>
> | dimension | 1-5 |
> |---|---|
> | Clear - could a newcomer follow it easily? | |
> | Deep - do you recognize careful scholarship? | |
> | On-point - did they answer what was actually asked? | |
> | Distinctly-this-world - could no other world have said this? | |
> | Transparent - do you see where it comes from? | |
> | Conversation - a real exchange, or statements filed in turn? | |
>
> One memorable thing from this conversation: ______________________
"""


def load_arm(arm: str, date: str) -> dict:
    p = RUNS / f"table_checkpoint_{arm}_{date}.json"
    if not p.exists():
        raise SystemExit(f"[rp] FAIL - missing artifact {p} - run that cell first")
    return json.loads(p.read_text(encoding="utf-8"))


def render_conversation(label: str, seating: dict) -> str:
    lines = [f"## Conversation {label}", ""]
    current_round = None
    for t in seating["turns"]:
        if t["round"] != current_round:
            current_round = t["round"]
            lines += [f"**Participant:** {t['probe']}", ""]
        speaker = t["speaker"] if t["speaker"] != "facilitator" else "Facilitator"
        lines += [f"**{speaker}:** {t['text']}", ""]
    lines.append(SCORESHEET)
    return "\n".join(lines)


def arm_summary(res: dict) -> str:
    hr, sh = res["hard_readability"], res["shape"]
    dv = res["divergence"]
    br = "; ".join(f"r{b['round']} {b['speaker']}: {b['breach']}"
                   for b in hr["breaches"]) or "none"
    tr = "; ".join(f"{v}: {t['turns_with_citations']}/{t['turns']} cited, "
                   f"{t['glosses_total']} glosses"
                   for v, t in res["transparency"].items())
    return (f"B2 breaches: {br} | measured turns {hr['measured_turns']}, "
            f"short {hr['unmeasured_short_turns']} | rep turns/round "
            f"{sh['rep_turns_per_round']} (mean {sh['mean_rep_turns_per_round']}) | "
            f"overlap mean {dv['overlap_mean']} max {dv['overlap_max']} | "
            f"borrowed vocab {len(dv['borrowed_vocabulary'])} | {tr}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    args = ap.parse_args()

    arms = {arm: load_arm(arm, args.date) for arm in ARMS}
    seating_keys = sorted(next(iter(arms.values()))["seatings"])

    rng = random.Random(SHUFFLE_SEED)
    pack, key = [], []
    pack += [f"# Table blind read pack — {args.date}", "",
             "Eight conversations: two seatings, four arms each, shuffled.",
             "Score each with its sheet BEFORE opening the key",
             f"(`T2_read_key_{args.date}.md`). The read is the score of",
             "record; the key holds the arm identities and the instrument",
             "numbers.", ""]
    key += [f"# Read key — {args.date}", "",
            "## The ruled criterion (Mark, 2026-08-10)",
            "Haiku ships if BOTH hold:",
            "1. **Hard bars outright** (absolute, never percentaged):",
            "   fabrication 0, the B2 edge per emitted turn, we-voice",
            "   discipline. A hard-bar failure disqualifies that arm.",
            "2. **Graded quality >= 90% of Sonnet's:** sum the six",
            "   dimensions per conversation; compare Haiku vs Sonnet",
            "   WITHIN the same block version (current vs current, v4 vs",
            "   v4), per seating and pooled. The v4-vs-v4 comparison is",
            "   the shipping decision; current-vs-current isolates the",
            "   model effect from the block effect.", ""]

    for sk in seating_keys:
        order = list(ARMS)
        rng.shuffle(order)
        for i, arm in enumerate(order):
            label = f"{sk}-{chr(ord('A') + i)}"
            res = arms[arm]["seatings"][sk]
            pack.append(render_conversation(label, res))
            model, blocks = ARMS[arm]
            key += [f"- **{label}** = `{arm}` ({model}, {blocks})",
                    f"  - {arm_summary(res)}"]
        key.append("")

    OUT.mkdir(parents=True, exist_ok=True)
    pack_path = OUT / f"T2_read_pack_{args.date}.md"
    key_path = OUT / f"T2_read_key_{args.date}.md"
    pack_path.write_text("\n".join(pack), encoding="utf-8")
    key_path.write_text("\n".join(key), encoding="utf-8")
    print(f"[rp] pack: {pack_path}")
    print(f"[rp] key : {key_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
