"""S4.5 - modern_term records (Pass 1 §3.11), the declared mapping.

Source: data/modern_term_bridge/definitions.json (today's world-agnostic
dictionary) carried forward VERBATIM field-for-field, plus the two §3.11
additions authored here:

- distinguishing_claim: the specific formula that separates the narrow,
  period-specific sense from the universal root word - §9.4's structural
  fix (the classifier can rule NONE because no distinguishing formula is
  present, not because one hand-written example said so).
- native_subject_map: per-world map of the underlying subject's native
  record, migrated worlds only (Desert). Mapped CONSERVATIVELY: an entry
  exists only where a real record genuinely answers the underlying
  subject; absence is honest (the bridge's "your world held nothing like
  it" path is a feature, not a gap).

FLAG-009 parking: `period_originated` (spoken by the runtime - the
Facilitator's "{period}" beat) and `contested_today` exist in
definitions.json but have no home in §3.11's field table or the schema
(unevaluatedProperties: false). Per the FLAG-002/FLAG-004 precedent they
are parked VERBATIM in each record's markdown body (commentary, not
validated) under a marked delimiter; the view generator
(wrs/views/modern_term_definitions.py) reads the parking; the schema
home awaits Mark's Change Order.

Deterministic: same inputs -> byte-identical records.

Usage (from cic-poc/backend):
  python wrs/migrate/s45_modern_term_records.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(BACKEND))

import yaml

SRC = BACKEND / "data" / "modern_term_bridge" / "definitions.json"
OUT = BACKEND / "wrs" / "records" / "facilitator" / "modern_term"

# §3.11: the specific claim separating the narrow sense from the root
# word. Authored against each term's own modern_sense.
DISTINGUISHING = {
    "penal-substitution-atonement":
        "Atonement framed as punishment-transfer: Christ bore, in the "
        "sinner's place, the penalty God's justice required. The "
        "distinguishing move is the penal-substitution mechanism itself, "
        "not the universal conviction that Christ's death saves.",
    "personal-relationship-with-jesus":
        "Faith framed as an individual's own one-to-one personal "
        "relationship with Jesus that one has and cultivates. The "
        "distinguishing move is the individualized relationship frame, "
        "not the universal language of belonging to Christ.",
    "sola-fide":
        "Faith ALONE, explicitly excluding what one does: the "
        "faith-versus-works opposition itself ('alone', 'not by works'). "
        "The distinguishing move is the exclusion, not the universal "
        "subject of faith.",
    "sola-scriptura":
        "Scripture ALONE as final authority, explicitly above or against "
        "church tradition and office. The distinguishing move is the "
        "exclusive-authority claim, not the universal reverence for "
        "Scripture.",
    "the-trinity-technical":
        "The conciliar technical formula - one substance (ousia), three "
        "persons, homoousios. The distinguishing move is the "
        "fourth-century metaphysical vocabulary, not merely speaking of "
        "Father, Son, and Holy Spirit together.",
    "original-sin-developed":
        "Sin INHERITED from Adam as a fallen nature - and, in the harder "
        "forms, inherited guilt - that one is born with. The "
        "distinguishing move is the inheritance doctrine, not the "
        "universal observation that all people sin.",
    "transubstantiation":
        "The bread and wine's inner reality CHANGES into the body and "
        "blood while the appearances remain - the change-of-substance "
        "metaphysics. The distinguishing move is that mechanism, not the "
        "universal conviction that the meal is holy or that Christ is "
        "present in it.",
    "born-again":
        "'Born again' as a conversion-identity label: a datable personal "
        "conversion event that marks one a born-again Christian. The "
        "distinguishing move is the identity-marker usage, not the "
        "ancient rebirth language itself (John 3 belongs to every era).",
    "the-rapture":
        "Believers caught up to Christ BEFORE a final tribulation - the "
        "two-stage, secret-return schema. The distinguishing move is that "
        "schema, not the universal expectation that Christ will return.",
    "purgatory":
        "A defined intermediate STATE of purification after death for "
        "the saved-but-not-yet-cleansed. The distinguishing move is the "
        "doctrine of that state, not the older practices of praying for "
        "the dead or hoping mercy reaches them.",
}

# §3.11: per-world native record for the underlying subject - migrated
# worlds only (Desert), conservative (entry only where a record really
# answers the subject; absence is honest).
NATIVE_MAP = {
    "sola-fide": {"desert-monasticism": "desertlex018"},         # puritas cordis - how a person comes to stand right before God
    "sola-scriptura": {"desert-monasticism": "desertclaim003"},  # where authority rested: elder vs office
    "original-sin-developed": {"desert-monasticism": "desertlex004"},  # logismoi - the world's own account of sin's roots and reach
    "born-again": {"desert-monasticism": "desertlex001"},        # anachoresis - what changed when a life turned
    "personal-relationship-with-jesus": {"desert-monasticism": "desertlex002"},  # apotage - the life given over
    "transubstantiation": {"desert-monasticism": "desertlex015"},  # synaxis - where the desert's shared meal lived
    # penal-substitution-atonement, the-trinity-technical, the-rapture,
    # purgatory: no Desert record genuinely answers the subject - honest
    # absence, the bridge's "nothing like it" path.
}

PARK_DELIM = ("[period_originated / contested_today - parked at S4.5 per "
              "FLAG-009: spoken by the runtime but absent from SS3.11's "
              "field table and the schema; the generated view reads this "
              "parking; schema home awaits Mark's Change Order]")


def main() -> None:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    for i, t in enumerate(data["terms"], start=1):
        tid = t["term_id"]
        front = {
            "id": f"facmt{i:03d}",
            "world_id": "facilitator",
            "record_type": "modern_term",
            "schema_version": 1,
            "jobs": [6, 7],
            "register": "etic",
            "review_state": "draft",
            "term": tid,
            "display_terms": t["display_terms"],
            "origin_year": t["origin_year"],
            "modern_sense": t["modern_sense"],
            "underlying_subject": t["underlying_subject"],
            "distinguishing_claim": DISTINGUISHING[tid],
            "native_subject_map": NATIVE_MAP.get(tid, {}),
        }
        body = (
            f"\n{PARK_DELIM}\n\n"
            f"period_originated: {t['period_originated']}\n"
            f"contested_today: {json.dumps(t['contested_today'])}\n"
        )
        text = ("---\n"
                + yaml.safe_dump(front, sort_keys=False, allow_unicode=True,
                                 width=100)
                + "---\n" + body)
        path = OUT / f"facmt{i:03d}.md"
        path.write_text(text, encoding="utf-8", newline="\n")
        print(f"wrote {path.name}  ({tid})")


if __name__ == "__main__":
    main()
