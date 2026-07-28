"""S6.2/SYR close-out (b) - the pre-freeze re-sweep.

The S2.1b disposition ('rowed there with real discovery data, or
excluded with reasons') discharged, the ALX s62_alx_presweep.py
pattern: the three PRESS/recall findings rowed as srcSYR062-064 with
the S2.1b instrument as the real discovery data; the search record
appended with the re-sweep note.

- srcSYR062 Acts of Thomas: P, Native (an early-3rd-century Edessene
  composition, squarely in-window and in-milieu), licensed for
  REGISTRY COMPLETENESS ONLY - it is not part of the deployed
  formation corpus and the build docs never engaged it; any content
  use is a project-lead decision (recorded as such, not smuggled in).
- srcSYR063 Liber Graduum: Excluded/Out-of-Boundary - carrying Doc_02
  SS1's own already-made decision INTO the registry ('falls partly
  outside this world's own 410 boundary in its final form and is not
  treated as a primary founding source here, though it is named for
  completeness' - verbatim in the verification_note).
- srcSYR064 Griffith 1995 'Asceticism in the Church of Syria': S row,
  the standard treatment of the proto-monastic distinctiveness claim.

COVERAGE LIMITS STAND: no database access this session - BIBP,
L'Annee philologique, Oxford Bibliographies, the Hugoye cumulative
index, and the systematic GEDSH pass remain named limits; saturation
is NOT claimed improved. srcSYR061's journal-language 'und' also
stands (no verification access).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

OUT = BACKEND / "wrs" / "records" / "syriac_world"

COMMON = {"world_id": "syriac-edessa-nisibis", "record_type": "source",
          "schema_version": 1, "register": "etic", "review_state": "draft",
          "disposition": "in-use",
          "discovery_channel": "reviewer-supplied",
          "discovery_instrument": ("S2.1b relative-recall + PRESS check "
                                   "(reviews/S6.2_SYR_s21b_coverage.md) - "
                                   "standard specialist expectations named "
                                   "independently of Doc_02's own list"),
          "discovery_date": "2026-07-28",
          "added": "2026-07-28 (S6.2/SYR pre-freeze re-sweep)",
          "jobs": [1, 2]}

ROWS = [
 {**COMMON, "id": "srcSYR062", "source_type": "P",
  "boundary_status": "Native", "attribution_status": "anonymous",
  "level_of_description": "work", "language": "syr", "script": "Syrc",
  "work_title": "The Acts of Thomas (with the Hymn of the Pearl), early 3rd c., Edessa",
  "work_locus": "early 3rd c.",
  "licensed_for": ("REGISTRY COMPLETENESS ONLY: among the earliest "
                   "substantial Syriac Christian compositions, in-window "
                   "and in-milieu, its encratite-ascetic register "
                   "adjacent to the world's ihidayutha/qyama territory - "
                   "but NOT part of the deployed formation corpus and "
                   "never engaged by the build docs (absent from the "
                   "entire build, the S2.1b check's one genuine "
                   "discovery). Any content use is a project-lead "
                   "decision; this row closes the registry gap, nothing "
                   "more."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b instrument's own finding; standard "
                        "identification carried as the recall table "
                        "expects it, not independently examined this "
                        "session.")},
 {**COMMON, "id": "srcSYR063", "source_type": "P",
  "boundary_status": "Excluded", "exclusion_reason": "Out-of-Boundary",
  "attribution_status": "anonymous", "level_of_description": "corpus",
  "language": "syr", "script": "Syrc",
  "work_title": "Liber Graduum (Book of Steps)",
  "work_locus": "late 4th-early 5th c. (final form partly post-410)",
  "licensed_for": ("Not licensed for retrieval or voice content: "
                   "excluded per Doc_02 SS1's own decision, now carried "
                   "in the registry itself rather than prose alone (the "
                   "S2.1b finding)."),
  "verification_note": ("Doc_02 SS1 verbatim: one of 'only three "
                        "substantial fourth-century Syriac literary "
                        "corpora' surviving from this world's range, "
                        "which 'falls partly outside this world's own "
                        "410 boundary in its final form and is not "
                        "treated as a primary founding source here, "
                        "though it is named for completeness.' The "
                        "registry now holds the exclusion with "
                        "reasons.")},
 {**COMMON, "id": "srcSYR064", "source_type": "S",
  "boundary_status": "Native", "attribution_status": "genuine",
  "level_of_description": "work", "language": "eng", "script": "Latn",
  "work_author": "Sidney Griffith",
  "work_title": ("\"Asceticism in the Church of Syria: The Hermeneutics "
                 "of Early Syrian Monasticism,\" in Asceticism, ed. "
                 "Wimbush/Valantasis (Oxford UP, 1995)"),
  "work_locus": "1995",
  "licensed_for": ("Secondary scholarship (the S2.1b PRESS gap): a "
                   "standard treatment of exactly this world's "
                   "proto-monastic distinctiveness claim - "
                   "confidence-judgment apparatus only, never voice "
                   "content."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b PRESS answer; author/title/collection as "
                        "the specialist expectation carries them, not "
                        "independently examined this session.")},
]

RESWEEP_NOTE = (
    "\n\nPre-freeze re-sweep (2026-07-28): the three S2.1b "
    "relative-recall/PRESS findings rowed as srcSYR062-064 (the Acts of "
    "Thomas registry-completeness row; the Liber Graduum Excluded row "
    "carrying Doc_02 SS1's own decision into the registry; Griffith "
    "1995) - each verification_note declares the work not independently "
    "examined this session. The FIVE named coverage limits (BIBP; "
    "L'Annee philologique; Oxford Bibliographies; the Hugoye cumulative "
    "index; the systematic GEDSH pass) STAND - no database access this "
    "session; srcSYR061's journal-language 'und' also stands; "
    "saturation is NOT claimed improved beyond the recall-instrument "
    "closure. See wrs/migrate/s62_syr_presweep.py.")


def main():
    for rec in ROWS:
        emit_record(rec, ("Rowed at the S6.2/SYR pre-freeze re-sweep "
                          "(2026-07-28) per the S2.1b disposition; see "
                          "wrs/migrate/s62_syr_presweep.py."),
                    OUT / "source" / f"{rec['id']}.md")
    sr = OUT / "search_record" / "srcSYRsearch001.md"
    t = sr.read_text(encoding="utf-8")
    if "Pre-freeze re-sweep (2026-07-28)" not in t:
        sr.write_text(t.rstrip() + RESWEEP_NOTE + "\n", encoding="utf-8")
    print("3 pre-freeze rows + search-record note")


if __name__ == "__main__":
    main()
