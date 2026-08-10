#!/usr/bin/env python3
"""Fixture for speaker-label repair, driven by the REAL leaked turns.

Every "must repair" case below is copied from a committed run artifact
(Ministry/Technology/Table/runs/), not invented - including the
ventriloquism case where Chloe wrote Papnoute's dialogue inside her own
turn, and the cascade turn where Mar Yausep then narrated the failure to
the participant.

The "must NOT touch" cases are the ones that decide whether this repair
is safe to run on every turn: ordinary prose containing a colon, a
representative naming another representative mid-sentence (which is the
block's own "name what they actually said" instruction working), and a
turn whose entire body is another voice's - where truncating would emit
an empty message and corrupt every later turn that reads it.

Usage (from cic-poc/backend):
  python scripts/speaker_label_repair_fixture.py
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND))
os.environ.setdefault("MOCK_LLM", "true")
os.environ.setdefault("ANTHROPIC_API_KEY", "sk-ant-fixture-not-used")

from app.speaker_label_repair import repair_speaker_labels  # noqa: E402

CHLOE, PAPNOUTE, YAUSEP = "Chloe", "Papnoute", "Mar Yausep"
failures: list[str] = []


def case(label: str, text: str, own: str, others: list[str], want: str) -> None:
    got = repair_speaker_labels(text, own, others, world_id="test")
    if got.strip() != want.strip():
        failures.append(label)
        print(f"  FAIL {label}\n    got : {got[:120]!r}\n    want: {want[:120]!r}")
    else:
        print(f"  ok   {label}")


def main() -> int:
    print("[slr] MUST REPAIR - real leaked turns from the run artifacts")
    case("leading self-label (ship-regression T2 r3)",
         "Chloe: You are reading truly.  We gather what can be spared",
         CHLOE, [PAPNOUTE], "You are reading truly.  We gather what can be spared")
    case("leading OTHER's label (ship-regression T3 r1 - Chloe labelled as Yausep)",
         "Mar Yausep: You named something I have watched in our own streets.",
         CHLOE, [PAPNOUTE, YAUSEP], "You named something I have watched in our own streets.")
    case("ventriloquism - Chloe writes Papnoute's lines (haiku-current T2)",
         "Chloe: You are reading truly.\n\nWe gather what can be spared at the table.\n\n"
         "Papnoute: The sickness we saw was the keeping. Not the bread itself.",
         CHLOE, [PAPNOUTE, YAUSEP],
         "You are reading truly.\n\nWe gather what can be spared at the table.")
    case("ventriloquism without a leading label",
         "We kept the door open.\n\nPapnoute: We left it behind.",
         CHLOE, [PAPNOUTE], "We kept the door open.")
    case("label with no leading space, mid-text",
         "Our record holds it.\nMar Yausep: Ours does not.",
         CHLOE, [YAUSEP], "Our record holds it.")

    print("[slr] MUST NOT TOUCH")
    case("ordinary colon in prose",
         "We taught two ways: the way of life and the way of death.",
         CHLOE, [PAPNOUTE],
         "We taught two ways: the way of life and the way of death.")
    case("naming another rep mid-sentence (the block's own instruction)",
         "What strikes me in what Papnoute said is the cost of leaving.",
         CHLOE, [PAPNOUTE],
         "What strikes me in what Papnoute said is the cost of leaving.")
    case("a name at line start WITHOUT a colon",
         "We differ here.\nPapnoute would say the cell teaches it faster.",
         CHLOE, [PAPNOUTE],
         "We differ here.\nPapnoute would say the cell teaches it faster.")
    case("an unseated name is not an impersonation boundary",
         "We read them aloud.\nIgnatius: wheat of God, ground by the teeth of beasts.",
         CHLOE, [PAPNOUTE],
         "We read them aloud.\nIgnatius: wheat of God, ground by the teeth of beasts.")
    case("whole turn is another voice - NOT truncated to empty",
         "Papnoute: We left the table behind, and did not look back.",
         CHLOE, [PAPNOUTE],
         "We left the table behind, and did not look back.")
    case("clean turn untouched",
         "We were never told what became of him.",
         CHLOE, [PAPNOUTE], "We were never told what became of him.")
    case("empty stays empty", "", CHLOE, [PAPNOUTE], "")

    print("[slr] REGRESSION - the real corpus, repaired")
    import json, re, glob
    NAMES = r"(Chloe|Papnoute|Mar Yausep|Marius|Theon|Albina)"
    total = repaired = 0
    for p in sorted(glob.glob(str(BACKEND.parents[1] / "Ministry" / "Technology"
                                  / "Table" / "runs" / "table_checkpoint_*.json"))):
        art = json.load(open(p, encoding="utf-8"))
        seated = {n for res in art["seatings"].values()
                  for n in {t["speaker"] for t in res["turns"]} - {"facilitator"}}
        for res in art["seatings"].values():
            for t in res["turns"]:
                if t["speaker"] == "facilitator":
                    continue
                total += 1
                out = repair_speaker_labels(
                    t["text"], t["speaker"], sorted(seated - {t["speaker"]}))
                if out != t["text"]:
                    repaired += 1
                if re.match(r"^\s*" + NAMES + r"\s*:", out) or re.search(r"\n\s*" + NAMES + r"\s*:", out):
                    failures.append(f"leak survived repair in {art['arm']}")
                    print(f"  FAIL leak survived in {art['arm']}: {out[:90]!r}")
                if not out.strip():
                    failures.append(f"repair emptied a turn in {art['arm']}")
                    print(f"  FAIL emptied a turn in {art['arm']}")
    print(f"  ok   {repaired} of {total} real representative turns repaired, "
          f"no leak survived, none emptied")

    print()
    if failures:
        print(f"[slr] FAIL - {len(failures)} case(s)")
        return 1
    print("[slr] PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
