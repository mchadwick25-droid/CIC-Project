"""The readability bar screen (Build-Plan.md Stage 2b): report-only FK-grade
measurement over every participant-facing ("voice-diet") field in a world,
using the same field set `engine/m1/spoken_fields.py` now declares in one
place instead of scattered across six/seven independent lists.

This is measurement, not a gate. It reports, it never fails a build or
blocks anything - promoting any of it to a gate, and where the ceiling
should sit, is a separate decision not yet made.
`gate_readability` (`engine/m1/gates.py`) already CI-gates a
narrower field set (term/honest_limit/quote/voice_craft) at a fixed FK <=
10 ceiling; this screen deliberately covers a wider set - every voice-diet
field, including `story.tellable_as` and `doctrinal_witness.text`, which
`gate_readability` does not grade (see that gate's own docstring on why
`text` fields stay ungraded by design) - without proposing to gate any of
it itself.

Same FK-grade formula `gate_readability` already uses (`engine.m1.fk.
fk_grade`), so a future ceiling ruling compares like with like.

Usage: `python -m engine.m1.bar_screen <world>` - writes
`Build/worlds/<world>/build/bar-screen-<date>.json` and prints a summary table.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

from engine.m1.fk import fk_grade
from engine.m1.loader import load_world_records
from engine.m1.registry import REPO_ROOT
from engine.m1.spoken_fields import fields_with_role


def _texts_for_field(record: dict, field_name: str) -> list[str]:
    """A field's spoken text, as a list of scorable strings - most fields
    are a single string; demonstration.exchange is a list of {speaker,
    text}, and only the representative's own words are this screen's
    concern (the participant-simulation turns are not the voice's own
    writing)."""
    value = record.get(field_name)
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, list) and record.get("record_type") == "demonstration" and field_name == "exchange":
        return [
            turn.get("text", "")
            for turn in value
            if isinstance(turn, dict) and turn.get("speaker") == "representative" and turn.get("text", "").strip()
        ]
    return []


def screen_world(world_key: str) -> dict:
    records = load_world_records(world_key)
    by_field: dict[str, list[dict]] = {}

    for rid, rec in sorted(records.items()):
        record_type = rec.get("record_type")
        for field_name in fields_with_role(record_type, "voice-diet"):
            for text in _texts_for_field(rec, field_name):
                words = text.split()
                sentences = [s for s in text.replace("!", ".").replace("?", ".").split(".") if s.strip()]
                longest_sentence_words = max((len(s.split()) for s in sentences), default=len(words))
                key = f"{record_type}.{field_name}"
                by_field.setdefault(key, []).append({
                    "record_id": rid,
                    "words": len(words),
                    "sentences": max(len(sentences), 1),
                    "longest_sentence_words": longest_sentence_words,
                    "fk_grade": round(fk_grade(text), 2),
                })

    summary = {}
    for key, entries in sorted(by_field.items()):
        grades = sorted(e["fk_grade"] for e in entries)
        n = len(grades)
        summary[key] = {
            "count": n,
            "fk_grade_median": grades[n // 2] if n else None,
            "fk_grade_max": max(grades) if grades else None,
            "longest_sentence_words_max": max((e["longest_sentence_words"] for e in entries), default=None),
            "worst_record": max(entries, key=lambda e: e["fk_grade"])["record_id"] if entries else None,
        }

    return {
        "world": world_key,
        "generated": date.today().isoformat(),
        "fields": summary,
        "records": by_field,
    }


def main(argv: list[str]) -> int:
    if len(argv) != 1:
        print("usage: python -m engine.m1.bar_screen <world>", file=sys.stderr)
        return 2
    world_key = argv[0]
    report = screen_world(world_key)

    out_dir = REPO_ROOT / "Build" / "worlds" / world_key / "build"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"bar-screen-{report['generated']}.json"
    out_path.write_text(json.dumps(report, indent=2, sort_keys=False) + "\n", encoding="utf-8")

    print(f"{world_key}: wrote {out_path.relative_to(REPO_ROOT)}")
    print(f"{'field':<32} {'n':>4} {'fk median':>10} {'fk max':>8} {'longest sent':>13}  worst record")
    for key, s in report["fields"].items():
        print(
            f"{key:<32} {s['count']:>4} {s['fk_grade_median']:>10} {s['fk_grade_max']:>8} "
            f"{s['longest_sentence_words_max']:>13}  {s['worst_record']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
