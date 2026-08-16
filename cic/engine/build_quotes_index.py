"""Build each world's quotes.json - Tier 2's quotation-attribution index.

WHY. The second-round Opus review (2026-08-15) found a live-generated turn
give Papnoute an Evagrius line - "prayer is the laying aside of thoughts,
not the piling up of words" - with no record home anywhere in the build.
The fabrication guard that should have caught it only ever checked NAMES
(the Poemen finding); a real, unattributed quotation slipped through
because nothing checked quoted TEXT against the world's own licensed
quote records. This module builds that check's ground truth: a flat,
per-world index of every quote record already vetted for this world,
in the shape a batched grounding judge can compare a generated turn's
quoted spans against - the same numbered-candidate pattern
filter_grounded_citations (app/graph/nodes.py) already runs in production
for the citation panel, applied here to quoted text instead.

WHAT IT IS NOT. This index is not a public artifact and does not enter a
Representative's prompt. It is read once, after generation, by a backend
grounding check - never rendered to a participant, never exposed by any
browse/search route. That distinction matters because of the rights gate
build_repository.py already enforces (FLAG-013): `quote.text_translation`
is third-party-derived text, and PUBLIC display of it requires an explicit
`display_permitted: true` on its provenance source row. That gate governs
the browsable repository; it does not apply here, because nothing here is
displayed - only compared, internally, and the comparison's OUTPUT is a
verdict (matched / unmatched), not the quote text itself. If this index
is ever wired into anything participant- or public-facing, the rights
gate must be re-applied there; do not assume this file's existence means
that check has already been done.

WHAT SHIPS. Every quote record for the world, regardless of `license`.
A do-not-voice quote is deliberately included, not excluded: a future
turn matching one is not "properly grounded," it is a second, sharper
kind of miss (the model voiced something explicitly forbidden), and the
check consuming this index needs the record present to recognize that
case rather than seeing an unmatched span and reporting only the milder
finding. `license` rides on every entry precisely so that distinction is
the grounding check's to make, not this builder's.

A world with no quote records yet gets an empty list, not an absent file
- matching every other per-world builder in this engine. Nothing here is
per-world logic; a new world with its own quote/ directory is covered by
this builder unchanged, the same guarantee every other generic build
script in cic/engine/ already makes.

Usage:
  python cic/engine/build_quotes_index.py                 # write all admitted worlds
  python cic/engine/build_quotes_index.py --world desert   # one world
  python cic/engine/build_quotes_index.py --dry-run        # report only
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent  # cic/
sys.path.insert(0, str(HERE))

# One world authority: worlds.py.
from worlds import WORLDS as _W  # noqa: E402

RECORD_DIRS = {w["world_id"]: (k, w["records_dir"]) for k, w in _W.items()}


def build(world_id: str) -> list[dict]:
    import yaml
    rec_dir = ROOT / "records" / RECORD_DIRS[world_id][1] / "quote"
    out: list[dict] = []
    if not rec_dir.exists():
        return out
    for p in sorted(rec_dir.glob("*.md")):
        fm = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
        confidence = fm.get("confidence") or {}
        out.append({
            "quote_id": fm["id"],
            "speaker_figure_id": (fm.get("speaker_or_author") or "").strip(),
            "text_translation": (fm.get("text_translation") or "").strip(),
            "locus": (fm.get("locus") or "").strip(),
            "license": fm.get("license", ""),
            "verification_state": confidence.get("verification_state", ""),
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--world", help="single world key, e.g. desert (default: all admitted worlds)")
    args = ap.parse_args()

    items = sorted(RECORD_DIRS.items())
    if args.world:
        items = [(wid, kd) for wid, kd in items if kd[0] == args.world]
        if not items:
            raise SystemExit(f"[quotes] unknown world {args.world!r}")

    total = 0
    for world_id, (key, _rdir) in items:
        index = build(world_id)
        total += len(index)
        blob = json.dumps(index, indent=1, ensure_ascii=False) + "\n"
        print(f"[quotes] {world_id:<34} {len(index):>2} licensed quote(s)")
        if args.dry_run:
            continue
        out = ROOT / "deploy" / key
        out.mkdir(parents=True, exist_ok=True)
        (out / "quotes.json").write_text(blob, encoding="utf-8")
    print(f"[quotes] {total} licensed quotes across the admitted worlds"
          f"{' (dry run - nothing written)' if args.dry_run else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
