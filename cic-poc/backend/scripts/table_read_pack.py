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
    "haiku-v4-guard-table": ("Haiku", "v4 blocks + guard-slot measure"),
}
SHUFFLE_SEED = 20260810  # fixed: the pack must rebuild identically

# Cell logs, for the 1B watchlist: post-adjudication fabrication signals
# mapped back to their round by log position (the drift record itself
# carries no turn reference - the known instrument gap from Albina's
# checkpoint, fix queued in the blueprint).
ARM_LOGS = {
    "pre1A-table": "pre1A_table_run.log",
    "haiku-current-table": "cell2_haiku_current.log",
    "sonnet-v4-table": "cell3_sonnet_v4.log",
    "haiku-v4-table": "cell4_haiku_v4.log",
    "haiku-v4-guard-table": "cell5_haiku_v4_guard.log",
}

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


def fabrication_watchlist(arm: str, logs_dir: Path, artifact: dict) -> list[str]:
    """Quote every turn implicated by a post-adjudication fabrication signal.

    The logged `[drift_signal] ... signal_type=fabrication` line survives
    only when the adjudicator did NOT rule the turn grounded (a grounded
    verdict logs nothing), so each line here is an adjudicated extrinsic
    (medium) or intrinsic (high) finding. The record carries no turn
    reference, so the signal is mapped to the most recent round marker
    above it in the log; both that round's turns by the flagged world are
    quoted so the ruling is made on the text, not the label.
    """
    import re
    log = logs_dir / ARM_LOGS.get(arm, "")
    if not log.exists():
        return [f"- (no log found for {arm}; watchlist unavailable)"]
    out = []
    current = {"seating": None, "round": None}
    seat_order = sorted(artifact["seatings"])
    seat_idx = -1
    for line in log.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.search(r"\[tc\] T[23] session", line)
        if m:
            seat_idx += 1
            current = {"seating": seat_order[min(seat_idx, len(seat_order) - 1)],
                       "round": None}
            continue
        m = re.match(r"\[tc\]   r(\d+):", line)
        if m:
            current["round"] = int(m.group(1))
            continue
        m = re.search(r"\[drift_signal\] world_id=(\S+) "
                      r"signal_type=fabrication severity=(\w+)", line)
        if m and current["seating"] is not None:
            wid, sev = m.group(1), m.group(2)
            res = artifact["seatings"][current["seating"]]
            kind = "INTRINSIC" if sev == "high" else "extrinsic"
            rnd = current["round"]
            turns = [t for t in res["turns"]
                     if t["round"] == rnd and wid.startswith(
                         t["speaker_msgname"].replace("_", "-")[:4]) or
                     (t["round"] == rnd and t["speaker"] != "facilitator")]
            world_turns = [t for t in res["turns"] if t["round"] == rnd]
            out.append(f"- **{arm} / {current['seating']} round {rnd}** — "
                       f"{wid}, adjudicated {kind} ({sev}). Turns that "
                       f"round:")
            for t in world_turns:
                out.append(f"    - {t['speaker']}: \"{t['text'][:400]}\"")
    return out or ["- none"]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", required=True)
    ap.add_argument("--logs-dir", default="/tmp/claude-0/-home-user-CIC-Project/"
                    "3d9fb418-a020-5b67-99ce-0a5eab1bced7/scratchpad")
    args = ap.parse_args()

    arms = {}
    for arm in ARMS:
        try:
            arms[arm] = load_arm(arm, args.date)
        except SystemExit:
            print(f"[rp] note: arm {arm} has no artifact yet - pack builds "
                  f"without it")
    if not arms:
        raise SystemExit("[rp] FAIL - no artifacts at all")
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
        order = [a for a in ARMS if a in arms]
        rng.shuffle(order)
        for i, arm in enumerate(order):
            label = f"{sk}-{chr(ord('A') + i)}"
            res = arms[arm]["seatings"][sk]
            pack.append(render_conversation(label, res))
            model, blocks = ARMS[arm]
            key += [f"- **{label}** = `{arm}` ({model}, {blocks})",
                    f"  - {arm_summary(res)}"]
        key.append("")

    logs_dir = Path(args.logs_dir)
    key += ["## Measured cost per arm (same 16 rounds; retries and all "
            "governance included)", "",
            "| arm | now (Sonnet intro) | Sept 1+ (Sonnet standard) | "
            "ceiling fires |", "|---|---|---|---|"]
    import re as _re
    _PAT = _re.compile(r"\[llm_usage\] label=(\S+) model=(\S+).*?input_tokens="
                       r"(\d+) output_tokens=(\d+) cache_creation_input_tokens="
                       r"(\d+) cache_read_input_tokens=(\d+)")
    _STD, _INTRO, _HAIKU = (3, 15, 3.75, .30), (2, 10, 2.50, .20), (1, 5, 1.25, .10)
    for arm in arms:
        log = logs_dir / ARM_LOGS.get(arm, "")
        if not log.exists():
            continue
        txt = log.read_text(encoding="utf-8", errors="replace")
        recs = [(m.group(2), int(m.group(3)), int(m.group(4)),
                 int(m.group(5)), int(m.group(6))) for m in _PAT.finditer(txt)]
        fires = txt.count("regenerating once")

        def _tot(sonnet):
            t = 0.0
            for model, i, o, cw, cr in recs:
                r = _HAIKU if "haiku" in model else sonnet
                t += ((i - cr - cw) * r[0] + o * r[1] + cw * r[2] + cr * r[3]) / 1e6
            return t
        key.append(f"| {arm} | ${_tot(_INTRO)/16:.4f}/round | "
                   f"${_tot(_STD)/16:.4f}/round | {fires} |")
    key.append("")
    key += ["## 1B watchlist — adjudicated fabrication signals, for ruling",
            "Each entry is a post-adjudication survivor (grounded verdicts",
            "log nothing). Precedent: Albina's flag was ruled a classifier",
            "false positive on the text evidence — rule each on its text.", ""]
    for arm in arms:
        key.append(f"### {arm}")
        key += fabrication_watchlist(arm, logs_dir, arms[arm])
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
