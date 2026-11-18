"""S1-01 free measures on the saved shipped answers of fleet graded run 1, per
world, with no model call: readability per turn, words, build-talk and
malformed-tag leaks, and a horizon scan.

Usage: python saved_scores.py <dir of the world json files> <out.json>
"""
import json
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT))

from engine.m1.registry import load_registry  # noqa: E402
from engine.m4.output_check import check_horizon  # noqa: E402
from engine.m7.turn_readability import score_turn  # noqa: E402

FILES = {"alx": "alx.json", "desert": "desert.json", "don": "don.json", "gallic": "gallic.json", "hal": "hal.json",
         "ijc": "ijc.json", "lpc": "lpc.json", "pahc": "pahc.json", "syr": "syr.json", "witt": "witt.json",
         "rzg": "rzg-attempt2.json"}
BUILD_TALK = re.compile(r"this turn|the records I am holding|vendored|THIN GROUND|\[\[|\]\]|the ground (given|for this)", re.IGNORECASE)


def main(fleet_dir: Path, out: Path) -> None:
    registry = load_registry()
    rows = {}
    for world, filename in FILES.items():
        probes = json.loads((fleet_dir / filename).read_text(encoding="utf-8"))["worlds"][world]["per_probe"]
        end = (registry[world].get("time_window") or {}).get("end")
        answers = [p["transcript"]["answer_text"] for p in probes]
        scored = [s for s in (score_turn(a) for a in answers) if s.scored]
        words = [len(a.split()) for a in answers]
        rows[world] = {
            "answers": len(answers),
            "words_mean": round(statistics.fmean(words)),
            "words_max": max(words),
            "over_220_words": sum(w > 220 for w in words),
            "fk_mean": round(statistics.fmean(s.fk for s in scored), 1),
            "fre_mean": round(statistics.fmean(s.fre for s in scored), 1),
            "fre_below_60": sum(s.fre < 60 for s in scored),
            "build_talk_or_raw_tags": sum(bool(BUILD_TALK.search(a)) for a in answers),
            "horizon_flags": sum(bool(check_horizon(a, end)) for a in answers) if end else None,
        }
        print(world, rows[world])
    out.write_text(json.dumps(rows, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(Path(sys.argv[1]), Path(sys.argv[2]))
