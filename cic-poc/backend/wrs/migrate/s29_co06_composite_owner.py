"""CO-P2-06 (Mark, 2026-07-27, Alternative A) - the composite-owner convention.

FLAG-003 resolved: Tier-4 composite stories get a synthetic owner figure
representing THE COMMUNITY ITSELF - never the Representative persona.
Mark's governing rationale, recorded verbatim-adjacent: the
Representative's name and role come out of the build and are the only
fabrications, made to build connection, and must NEVER be entered into
the world record; the Representative speaks for the entire world, not
one perspective, so its identity is not world content. (The persona
identity lives on voice_profile - a voice-construction record - per
CO-P2-05; no figure record for it exists or ever should.)

This script: emits desertfig013 (the composite-owner figure for the
Desert world's communal daily life) and points desertstory008's
owner_figure_id at it. The completion gate goes quiet because the rule
now matches the design - the field resolves to a real record - not
because the violation was suppressed. Idempotent.
"""
from __future__ import annotations

from pathlib import Path

import sys

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

FIGDIR = BACKEND / "wrs" / "records" / "desert_world" / "figure"
STORY8 = BACKEND / "wrs" / "records" / "desert_world" / "story" / "desertstory008.md"

FIGURE = {
 "id": "desertfig013",
 "world_id": "desert-monasticism",
 "record_type": "figure",
 "schema_version": 1,
 "jobs": [1, 3],
 "register": "etic",
 "review_state": "draft",
 "names": [
  {"name": "the desert communities themselves", "name_kind": "scholarly"},
 ],
 "narratable": True,
 "story_ids": ["desertstory008"],
 "attribution_note": (
  "Composite-owner convention (CO-P2-06, Mark, 2026-07-27, Alternative "
  "A): a synthetic figure standing for the community whose typical life "
  "a Tier-4 composite reconstructs - desertstory008 follows no one "
  "person's day by its own template rule. Deliberately NOT the "
  "Representative persona: per Mark's decision, the Representative's "
  "name and role are the build's only sanctioned fabrications, made to "
  "build connection, and are never entered into the world record - the "
  "Representative speaks for the entire world, not one perspective. "
  "This figure is not a person and is never named in voice material as "
  "an individual."),
}


def main() -> None:
    emit_record(dict(FIGURE),
                ("CO-P2-06 composite-owner figure (2026-07-27). Resolves "
                 "FLAG-003: SS11-A's owner requiredness now satisfiable "
                 "for Tier-4 composites without weakening the gate."),
                FIGDIR / "desertfig013.md")
    text = STORY8.read_text(encoding="utf-8")
    parts = text.split("---\n")
    fm = yaml.safe_load(parts[1])
    if fm.get("owner_figure_id") != "desertfig013":
        fm["owner_figure_id"] = "desertfig013"
        body = "---\n".join(parts[2:]).rstrip("\n")
        if "CO-P2-06" not in body:
            body += ("\n\nCO-P2-06 (2026-07-27, Alternative A): "
                     "owner_figure_id -> desertfig013 (the community "
                     "itself, per the composite-owner convention); "
                     "FLAG-003 resolved.")
        STORY8.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False,
                                                    allow_unicode=True,
                                                    width=100)
                          + "---\n" + body + "\n", encoding="utf-8")
    print("desertfig013 emitted; desertstory008.owner_figure_id set")


if __name__ == "__main__":
    main()
