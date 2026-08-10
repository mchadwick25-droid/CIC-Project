"""Build each world's figure_registry.json - the name bridge's data.

WHY. Mark's read of the live site, 2026-08-09, measured by
scripts/transparency_reach.py: the transparency gap is dominated not by hard
words but by NAMES. A reader meets Aphrahat, Gushtazad, Pachomius, Blaesilla,
Chalcedon and has nothing at all. The gloss system structurally cannot help -
`confirmed_glosses` is a VOCABULARY table and names were never in its scope.

Every world already carries figure records with an in-world name, a scholarly
name, and (added 2026-08-09) a `bridge_line`: one plain sentence saying who
this was, derived only from that record's own material. Those records are
already loaded into every Representative's assembled prompt. What they have
never had is a path to the PARTICIPANT. This module builds that path's data.

WHAT IT IS NOT. This registry never enters a prompt. It cannot change a
single word a Representative says - it is read after generation, by the
detector, to decorate text that already exists. That is why writing it into
data/ is not a swap of voice content: no checkpoint's subject matter moves.
`assembly_identity` is byte-identical across this change by construction, and
the commit that ships it asserts so.

WHAT SHIPS AND WHAT DOES NOT. Only figures with a `bridge_line` appear.
Composite and community figures ("the network itself", "the qyama - the
covenant community itself") are deliberately excluded: they are not names a
reader hits, and a pill on them would be noise. A figure whose record does not
support a plain honest sentence gets no line and therefore no pill - the
absence is correct, never a stub, and never invented.

Usage (from cic-poc/backend):
  python -m wrs.views.figure_registry            # write staging + data
  python -m wrs.views.figure_registry --dry-run  # report only
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

# world record dir -> (deployed data dir, staging dir). Both come from the
# world manifest at run time; this table is only the records-side name, which
# the manifest does not carry.
RECORD_DIRS = {
    "post-apostolic-house-church": "pahc_world",
    "imperial-juridical-christianity": "imperial_juridical_world",
    "alexandria-catechetical": "alexandria_world",
    "desert-monasticism": "desert_world",
    "syriac-edessa-nisibis": "syriac_world",
    "hieronymian-ascetic-literary": "hieronymian_world",
}

# Apparatus that must never reach a participant - the same class the leak gate
# blocks in serialized chunks. A bridge_line is participant-facing text, so it
# is held to that bar here rather than trusted.
#
# Matched on WORD BOUNDARIES, not as bare substrings: the first run of this
# builder rejected "He recorded Nero blaming Christians for the fire" because
# "recorded" contains "record". A check that fires on ordinary English trains
# people to disable it.
_APPARATUS = (r"Doc_0", r"\bTier\b", r"src[A-Z]{3}", r"CO-P2", r"S\d\.\d",
              r"Author-Gravity", r"\bchunks?\b", r"\brecords?\b",
              r"\bStrand\b", r"§", r"\bnarratable\b", r"\bregister\b")


_TITLES = {"Abba", "Amma", "Mar", "King", "Pope", "Saint", "St"}


def _match_forms(names: list) -> list:
    """The surface forms a Representative might actually say.

    Figure records store descriptive names - "Ambrose, bishop of Milan",
    "Pliny, the governor who questioned us", "Athanasius of Alexandria" - but
    a Representative in conversation says "Ambrose". The first run of the
    detector matched nothing at all for IJC for exactly this reason. So each
    stored name also yields its leading proper-noun run.

    Descriptive openers ("the church at Rome", "the network itself") are left
    whole: their leading run is "the", which is not a name.

    A bare given name is DROPPED when this figure's own name carries a title -
    "Moses (of Scetis)" would otherwise contribute "Moses" and put an
    Abba-Moses panel on any mention of the Moses of Exodus. Same for Amma
    Sarah, Mar Yausep, King Abgar. The titled form still matches; only the
    ambiguous bare one goes.
    """
    titled = {n.split()[-1] for n in names
              if n and n.split() and n.split()[0] in _TITLES}
    forms: list = []
    for n in names:
        n = (n or "").strip()
        if not n:
            continue
        forms.append(n)
        short = re.split(r",| of | \(| the | who | as ", n)[0].strip()
        if short in titled:
            continue
        # 3 is deliberate, not sloppy: "Leo" is a real figure name and was
        # silently dropped at a 4-character floor. Word-boundary matching
        # plus the capital-letter test keeps a three-letter proper noun safe.
        if (short and short != n and len(short) >= 3
                and short[:1].isupper() and short not in forms):
            forms.append(short)
    # longest first so a specific name is preferred over a shared given name
    return sorted(dict.fromkeys(forms), key=len, reverse=True)


def build(world_id: str) -> list[dict]:
    import yaml
    rec_dir = BACKEND / "wrs" / "records" / RECORD_DIRS[world_id] / "figure"
    out: list[dict] = []
    for p in sorted(rec_dir.glob("*.md")):
        fm = yaml.safe_load(p.read_text(encoding="utf-8").split("---", 2)[1])
        line = (fm.get("bridge_line") or "").strip()
        if not line:
            continue
        for bad in _APPARATUS:
            if re.search(bad, line):
                raise SystemExit(
                    f"[figreg] {fm['id']}: bridge_line carries apparatus "
                    f"language {bad!r} - participant-facing text must not. "
                    f"Fix the record.")
        names = [n.get("name", "") for n in (fm.get("names") or [])]
        in_world = next((n.get("name") for n in (fm.get("names") or [])
                         if n.get("name_kind") == "in-world"), None)
        out.append({
            "figure_id": fm["id"],
            "display_name": in_world or (names[0] if names else fm["id"]),
            "names": _match_forms(names),
            "bridge_line": line,
            "narratable": bool(fm.get("narratable")),
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    from app.world_manifest import WORLD_MANIFEST
    total = 0
    for entry in WORLD_MANIFEST:
        if entry.world_id not in RECORD_DIRS:
            continue
        registry = build(entry.world_id)
        total += len(registry)
        blob = json.dumps(registry, indent=1, ensure_ascii=False) + "\n"
        staging = BACKEND / "wrs" / "views" / "staging" / entry.data_dir_name
        deployed = BACKEND / "data" / entry.data_dir_name
        print(f"[figreg] {entry.world_id:<34} {len(registry):>2} bridged "
              f"figures")
        if args.dry_run:
            continue
        staging.mkdir(parents=True, exist_ok=True)
        (staging / "figure_registry.json").write_text(blob, encoding="utf-8")
        if deployed.is_dir():
            (deployed / "figure_registry.json").write_text(blob,
                                                           encoding="utf-8")
    print(f"[figreg] {total} bridged figures across the fleet"
          f"{' (dry run - nothing written)' if args.dry_run else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
