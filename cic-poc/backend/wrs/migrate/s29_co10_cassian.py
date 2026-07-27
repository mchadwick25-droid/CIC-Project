"""CO-P2-10 (Mark, 2026-07-27, all recommendations) - items (c)+(d).

(c) The Cassian source row (srcDES026): the build documents cite John
Cassian repeatedly and load-bearingly - Doc_01 SS2.3 (his Institutes/
Conferences through the 420s as part of the world's own closing/
codification marker), Doc_08 Force 3B-ii (the transmission sequel),
Doc_03 SS1.18 (the apatheia -> puritas cordis substitution), Doc_09c SS4
(living-tradition line "via Cassian's transmission") - but Doc_02's
source ecology never rowed him, which S2.1's relative-recall check
caught as its one miss (9/10). Butler/Guy deferred per the same
decision until something needs to cite them.

Unblocked by (c): desertlex018 (Puritas Cordis, Tier 3) - deferred at
CO-P2-03 precisely because this row didn't exist - authored from Doc_06
SS3.2 verbatim, with the apatheia edge Doc_06 names (deferred then,
typed now) and its reciprocal.

(d) is resolved by (c): the relative-recall miss closes because the row
now exists. Idempotent.
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
TERMDIR = BACKEND / "wrs" / "records" / "desert_world" / "term"

CASSIAN = {
 "world_id": "desert-monasticism", "record_type": "source",
 "schema_version": 1, "register": "etic", "review_state": "draft",
 "boundary_status": "Native", "disposition": "in-use",
 "id": "srcDES026",
 "work_author": "John Cassian",
 "work_title": ("De institutis coenobiorum (Institutes); Collationes "
                "(Conferences)"),
 "work_locus": "c. 420s (within the world's closing window, Doc_01 SS2.3)",
 "source_type": "P",
 "attribution_status": "genuine",
 "level_of_description": "corpus",
 "language": "lat",
 "script": "Latn",
 "discovery_channel": "cited-in-another-row",
 "licensed_for": ("Transmission-history evidence: the world's own closing/"
                  "codification marker (Doc_01 SS2.3), the Western "
                  "transmission sequel (Doc_08 Force 3B-ii), the living-"
                  "tradition line (Doc_09c SS4), and the apatheia -> "
                  "puritas cordis substitution (Doc_03 SS1.18; Doc_06 "
                  "SS3.2). Added per CO-P2-10(c) - the build documents "
                  "cite this corpus load-bearingly; Doc_02's ecology "
                  "never rowed it (S2.1 relative-recall's one miss, now "
                  "closed)."),
 "verification_note": ("Authorship, works, and c. 420s dating are the "
                       "build documents' own repeated, Widely Accepted "
                       "citations (Doc_01/Doc_03/Doc_08/Doc_09c) - rowed "
                       "from them, not newly researched."),
 "jobs": [1, 2],
 "added": "2026-07-27 (CO-P2-10c)",
}

PURITAS = {
 "world_id": "desert-monasticism", "record_type": "term",
 "schema_version": 1, "jobs": [1, 2, 4, 5, 6, 7],
 "register": "emic", "review_state": "draft", "cache_stability": "static",
 "id": "desertlex018",
 "term": "Puritas Cordis (Purity of Heart)",
 "aliases": ["purity of heart", "puritas cordis"],
 "quick_meaning": ("John Cassian's Latin rendering of apatheia for a "
                   "Western audience, anchored in Matthew 5:8 — a "
                   "deliberate substitution, not a literal translation, "
                   "made because apatheia's Stoic-sounding claim had "
                   "become theologically controversial."),
 "modern_hearing": ("Modern Hearing — a generic devotional phrase, "
                    "unmoored from any specific technical content."),
 "distortion_risk": ("World Hearing — a deliberate, disclosed "
                     "substitution for apatheia, carrying that term's "
                     "full technical content while avoiding its "
                     "Stoic-sounding controversy; belongs to this "
                     "world's reception history via Cassian (writing in "
                     "the 420s, at the edge of the c. 430 closing "
                     "boundary) rather than its own core vocabulary "
                     "(Doc_06 §3.2)."),
 "retrieval": {"tier": 3,
               "retrieve_when": ["participant uses 'purity of heart' as "
                                  "a technical term or asks how the "
                                  "desert tradition reached the West"],
               "do_not_retrieve_when": [], "force_llm_vote": False},
 "sources": [{"source_id": "srcDES026",
              "author_gravity_note": ("Cassian's own substitution, "
                                       "disclosed in his corpus (Doc_03 "
                                       "SS1.18; Doc_06 SS3.2).")}],
 "confidence": {"citation_specificity": "B",
                 "verification_state": "verified-via-authority",
                 "verification_date": "2026-07-27",
                 "evidentiary_weight": "corroborating",
                 "formation_confidence": "Widely Accepted"},
 "field_relations": [
  {"type": "presupposes", "target_id": "desertlex011",
   "note": ("Doc_06 §3.2: a deliberate, disclosed substitution for "
            "apatheia (2.2), carrying its full technical content — the "
            "edge deferred at CO-P2-03 pending this record's source row, "
            "typed now per CO-P2-10(c).")}],
}


def main() -> None:
    emit_record(dict(CASSIAN),
                ("CO-P2-10(c) source row (2026-07-27): rowed from the "
                 "build documents' own load-bearing citations; closes "
                 "S2.1 relative-recall's one miss. Butler/Guy deferred."),
                SRCDIR / "srcDES026.md")
    emit_record(dict(PURITAS),
                ("CO-P2-10(c) term record (2026-07-27): Doc_06 SS3.2 "
                 "verbatim-condensed; deferred at CO-P2-03 until the "
                 "Cassian row existed - no fabricated citation, then or "
                 "now."),
                TERMDIR / "desertlex018.md")
    # reciprocal on apatheia (deferred edge, both directions typed)
    p = TERMDIR / "desertlex011.md"
    text = p.read_text(encoding="utf-8")
    parts = text.split("---\n")
    fm = yaml.safe_load(parts[1])
    rels = fm.setdefault("field_relations", [])
    if not any(e.get("target_id") == "desertlex018" for e in rels):
        rels.append({"type": "presupposed-by", "target_id": "desertlex018",
                     "note": ("CO-P2-10(c) mirror: puritas cordis is "
                              "Cassian's disclosed substitution for this "
                              "term (Doc_06 §2.2/§3.2) - the edge "
                              "deferred at CO-P2-03, typed now.")})
        body = "---\n".join(parts[2:]).rstrip("\n")
        body += ("\n\nCO-P2-10(c) (2026-07-27): the deferred Puritas "
                 "Cordis edge is now typed (srcDES026 exists).")
        p.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False,
                                               allow_unicode=True, width=100)
                     + "---\n" + body + "\n", encoding="utf-8")
    print("srcDES026 + desertlex018 emitted; apatheia reciprocal typed")


if __name__ == "__main__":
    main()
