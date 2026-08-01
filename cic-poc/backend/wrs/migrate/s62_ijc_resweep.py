"""S6.2/IJC - pre-freeze re-sweep: the S2.1b PRESS routings, rowed.

Three rows with REAL discovery data (the S2.1b PRESS named all three;
the SYR/HAL/PAHC precedent) + srcIJCsearch002:

- srcIJC39 Dagron 1974 (Naissance d'une capitale) - THE SHARPEST MISS:
  Strand B had NO dedicated secondary row while Strands A and C carry
  two-plus each; the standard study of Constantinople's rise, its
  330-451 span nearly this world's own window.
- srcIJC40 Drake 2000 (Constantine and the Bishops) - the standard
  political reading of the initiating alliance, beside Barnes (row 28).
- srcIJC41 Millar 2006 (A Greek Roman Empire, 408-450) - the eastern
  court in exactly the decades producing Ephesus 431, the 449 synod,
  and Chalcedon's imperial context.

ID CONVENTION: rows 39-41 continue the registry numbering as
RECORD-ONLY rows (the World-Builds md registry is the W-build's own
append-only artifact; this migration does not write into World-Builds
- the index audit's registry checks scope to rows 1-38). Declared in
srcIJCsearch002.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "imperial_juridical_world"
WID = "imperial-juridical-christianity"

INSTRUMENT = ("S6.2/IJC pre-freeze re-sweep (2026-07-31): the S2.1b "
              "relative-recall/PRESS routings executed "
              "(wrs/migrate/s62_ijc_resweep.py)")
CHANNEL_NOTE = (" - channel note: the S2.1b PRESS review supplied the "
                "naming (reviewer-supplied is the enum home)")

ROWS = [
 {"id": "srcIJC39", "source_type": "S", "boundary_status": "Native",
  "attribution_status": "genuine", "level_of_description": "work",
  "language": "fr",
  "work_author": "Gilbert Dagron",
  "work_title": ("Naissance d'une capitale: Constantinople et ses "
                 "institutions de 330 a 451 (Paris, 1974)"),
  "licensed_for": ("THE STRAND-B SCHOLARSHIP ROW (the S2.1b round's "
                   "sharpest miss - Strand B previously had no "
                   "dedicated secondary row while A and C carry "
                   "two-plus each): the standard study of "
                   "Constantinople's own rise and institutions, its "
                   "330-451 span nearly this world's own window; the "
                   "scholarly ground under presbeia / Nea Rhome's own "
                   "claim material."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b PRESS; not read for this migration - "
                        "rowed as the named standard work of its "
                        "class, the Wilson-Kastner/Krumeich caveat "
                        "pattern."),
  "discovery_channel": "reviewer-supplied",
  "discovery_instrument": INSTRUMENT + CHANNEL_NOTE,
  "discovery_date": "2026-07-31",
  "added": "2026-07-31 (S6.2/IJC pre-freeze re-sweep)",
  "jobs": [1, 2]},
 {"id": "srcIJC40", "source_type": "S", "boundary_status": "Native",
  "attribution_status": "genuine", "level_of_description": "work",
  "language": "en",
  "work_author": "H. A. Drake",
  "work_title": ("Constantine and the Bishops: The Politics of "
                 "Intolerance (Baltimore, 2000)"),
  "licensed_for": ("The standard political reading of the initiating "
                   "alliance (Cell 1A/1B; ijcgrav002's modern ground) "
                   "- standing beside Barnes's more Eusebius-centered "
                   "account (row 28), the two together bracketing the "
                   "alliance's modern historiography."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b PRESS; not read for this migration - "
                        "rowed as the named standard work."),
  "discovery_channel": "reviewer-supplied",
  "discovery_instrument": INSTRUMENT + CHANNEL_NOTE,
  "discovery_date": "2026-07-31",
  "added": "2026-07-31 (S6.2/IJC pre-freeze re-sweep)",
  "jobs": [1, 2]},
 {"id": "srcIJC41", "source_type": "S", "boundary_status": "Native",
  "attribution_status": "genuine", "level_of_description": "work",
  "language": "en",
  "work_author": "Fergus Millar",
  "work_title": ("A Greek Roman Empire: Power and Belief under "
                 "Theodosius II (408-450) (Berkeley, 2006)"),
  "licensed_for": ("The standard account of the eastern court in "
                   "exactly the decades producing Ephesus 431, the "
                   "449 synod, and Chalcedon's imperial context "
                   "(forces 3A-1/3B-1's modern ground)."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b PRESS; not read for this migration - "
                        "rowed as the named standard work."),
  "discovery_channel": "reviewer-supplied",
  "discovery_instrument": INSTRUMENT + CHANNEL_NOTE,
  "discovery_date": "2026-07-31",
  "added": "2026-07-31 (S6.2/IJC pre-freeze re-sweep)",
  "jobs": [1, 2]},
]

SEARCH = {
    "id": "srcIJCsearch002", "world_id": WID,
    "record_type": "search_record", "schema_version": 1,
    "register": "etic", "review_state": "draft", "jobs": [1],
    "sampling_strategy": (
        "Purposive (Booth's standard) - the PRE-FREEZE RE-SWEEP "
        "(2026-07-31): executes the S2.1b PRESS routings; documents "
        "THIS re-sweep only (srcIJCsearch001 documents the "
        "migration-time sweep - the fleet's second clean sweep)."),
    "types_sought": [
        "the three PRESS-named works (the Strand-B gap row; the "
        "alliance's political reading; the Theodosian-court east)",
    ],
    "approaches": {"press-routing-execution": 1, "row-diff re-run": 1},
    "years_searched": {"from": 1974, "to": 2026},
    "languages_searched": ["en", "fr"],
    "inclusion_exclusions": (
        "Included: the three PRESS routings, each rowed with its "
        "read-status caveat. ID-CONVENTION: rows 39-41 are "
        "RECORD-ONLY continuations of the registry numbering; the "
        "World-Builds md registry (append-only by its own rule) is "
        "the W-build's artifact and this migration does not write "
        "into World-Builds - the index audit's registry checks scope "
        "to rows 1-38."),
    "terms_tried": [
        {"term": "the three S2.1b PRESS routings, executed as rows",
         "productive": True},
        {"term": "row-diff re-run after srcIJC39-41",
         "productive": False},
    ],
    "instruments": [
        INSTRUMENT,
        ("STANDING OPEN LIMITS, re-stated not satisfied: (1) "
         "bibliographic databases (BIBP / L'Annee philologique / "
         "Oxford Bibliographies) remain unaccessed - the standing "
         "fleet limit; (2) the Damasine-decretal authenticity "
         "question rests where row 15 left it (dubium, Confidence D, "
         "priority-review flagged - never leaned on); (3) row 30 "
         "(Wessel, working-title recollection at C) remains flagged "
         "for second-opinion review before supporting any vivid "
         "claim. These ride into the freeze declaration."),
    ],
}

SEARCH_BODY = (
    "Saturation statement (V7.4; re-sweep scope): after rowing "
    "srcIJC39-41, the row-diff re-run finds no remaining chunk-cited "
    "or PRESS-named work without a row or a declared reason. The "
    "standing limits ride into the freeze declaration.\n\n"
    "Provenance: wrs/migrate/s62_ijc_resweep.py (the re-sweep log; "
    "all three rows carry real discovery data - the S2.1b PRESS "
    "naming, executed here).")


def main():
    for row in ROWS:
        rec = {"world_id": WID, "record_type": "source",
               "schema_version": 1, "register": "etic",
               "review_state": "draft", "disposition": "in-use", **row}
        emit_record(rec, ("Rowed at the S6.2/IJC pre-freeze re-sweep "
                          "(2026-07-31) with real discovery data (the "
                          "S2.1b PRESS routing). See "
                          "wrs/migrate/s62_ijc_resweep.py and "
                          "srcIJCsearch002."),
                    OUT / "source" / f"{row['id']}.md")
    emit_record(SEARCH, SEARCH_BODY,
                OUT / "search_record" / "srcIJCsearch002.md")
    print("3 re-sweep rows + srcIJCsearch002")


if __name__ == "__main__":
    main()
