"""CO-P2-08 (Mark, 2026-07-27) - desertq002's translation_used, truthfully.

The Arsenius wording ("flee, be silent, be still") matched no published
rendering at S2.4's live quote-fidelity check - it is the BUILD'S OWN
rendering of the Latin 'fuge, tace, quiesce' as the project's documents
carry it. Mark's call: record that fact as a source row rather than
leave the field empty or borrow a citation. srcDES025 is the build's own
rendering, attributed to the build, with Ward's translation named as the
comparison edition the fidelity check ran against (divergent - which is
why the quote's license is and stays paraphrase-only).

Sets desertq002.translation_used -> srcDES025. Idempotent. desertq002 is
an s24 emission edited in place; if s24 re-runs, re-run this script.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

SRCDIR = BACKEND / "wrs" / "records" / "desert_world" / "source"
QUOTE = BACKEND / "wrs" / "records" / "desert_world" / "quote" / "desertq002.md"

ROW = {
 "world_id": "desert-monasticism", "record_type": "source",
 "schema_version": 1, "register": "etic", "review_state": "draft",
 "boundary_status": "Native", "disposition": "in-use",
 "id": "srcDES025",
 "work_author": "this build (CiC World #3 construction)",
 "work_title": ("Build rendering of Arsenius's counsel 'fuge, tace, "
                "quiesce' as 'flee, be silent, be still'"),
 "work_locus": "2026 (Doc_09a SS2.2; the assembled Permanent Prompt)",
 "source_type": "M",
 "attribution_status": "genuine",
 "level_of_description": "item",
 "language": "eng",
 "script": "Latn",
 "discovery_channel": "builder-prior-knowledge",
 "licensed_for": ("The translation_used anchor for desertq002 ONLY. This "
                  "is the build's own English rendering of the Latin "
                  "counsel, not a published edition - recorded as such "
                  "per CO-P2-08 (Mark, 2026-07-27). The S2.4 live "
                  "fidelity check compared it against Ward's published "
                  "rendering (srcDES021) and found it divergent, which "
                  "is why desertq002's license is and remains "
                  "paraphrase-only."),
 "verification_note": ("Quote-fidelity check performed live 2026-07-27 "
                       "(S2.4): no published rendering matched; the "
                       "wording is the build's own. Chicago-completeness "
                       "for what is actually the case."),
 "jobs": [1],
 "added": "2026-07-27 (CO-P2-08)",
}


def main() -> None:
    emit_record(dict(ROW),
                ("CO-P2-08 source row (2026-07-27): the build's own "
                 "rendering, attributed to the build - the truthful "
                 "translation_used anchor, not a borrowed citation."),
                SRCDIR / "srcDES025.md")
    text = QUOTE.read_text(encoding="utf-8")
    parts = text.split("---\n")
    fm = yaml.safe_load(parts[1])
    if fm.get("translation_used") != "srcDES025":
        fm["translation_used"] = "srcDES025"
        body = "---\n".join(parts[2:]).rstrip("\n")
        if "CO-P2-08" not in body:
            body += ("\n\nCO-P2-08 (2026-07-27): translation_used -> "
                     "srcDES025 (the build's own rendering, recorded as "
                     "such); license stays paraphrase-only.")
        QUOTE.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False,
                                                   allow_unicode=True,
                                                   width=100)
                         + "---\n" + body + "\n", encoding="utf-8")
    print("srcDES025 emitted; desertq002.translation_used set")


if __name__ == "__main__":
    main()
