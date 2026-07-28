"""S6.2 Alexandria close-out (b) - the pre-freeze re-sweep.

Rows the four S2.1b scholarship misses (the relative-recall/PRESS
findings, all S-row class: they alter the scholarship apparatus behind
confidence judgments, never what the voice may draw on) and records the
re-sweep disposition on the search record.

Honesty constraints:
- these four are NOT in the build docs (that absence IS the S2.1b
  finding), so unlike Desert's Cassian row there is no build-doc citation
  to anchor to; the REAL discovery channel is the S2.1b instrument
  itself -> discovery_channel: reviewer-supplied, discovery_instrument
  names the recall/PRESS check, discovery_date is its run date;
- verification_note states plainly that titles/dates are as the recall
  instrument carried them, not independently examined this session;
- licensed_for: confidence-judgment apparatus only - never voice content;
- the four S2.1a coverage limits (BIBP, L'Annee philologique, Oxford
  Bibliographies, CPG) REMAIN named limits - no database access this
  session; the search-record body records the re-sweep event and the
  standing limits rather than pretending saturation improved.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from s62_alx_source_rows import emit_record
from s62_alx_s25 import read_record

OUT = BACKEND / "wrs" / "records" / "alexandria_world" / "source"
SEARCH = (BACKEND / "wrs" / "records" / "alexandria_world" / "search_record"
          / "srcALXsearch001.md")

COMMON = {"world_id": "alexandria-catechetical", "record_type": "source",
          "schema_version": 1, "register": "etic", "review_state": "draft",
          "boundary_status": "Native", "disposition": "in-use",
          "source_type": "S", "attribution_status": "genuine",
          "level_of_description": "work", "language": "eng",
          "script": "Latn", "genre_form": "monograph",
          "discovery_channel": "reviewer-supplied",
          "discovery_instrument": ("S2.1b relative-recall + PRESS check "
                                   "(reviews/S6.2_ALX_s21b_coverage.md) - "
                                   "standard specialist expectations named "
                                   "independently of Doc_02's own list"),
          "discovery_date": "2026-07-27",
          "jobs": [1, 2],
          "added": "2026-07-28 (S6.2 pre-freeze re-sweep)"}

VNOTE = ("Rowed at the pre-freeze re-sweep from the S2.1b instrument's own "
         "finding; author/title/year as the recall table carried them, not "
         "independently examined this session - registry presence closes "
         "the coverage gap, the work itself remains to be consulted before "
         "any confidence judgment leans on its content.")

ROWS = [
 dict(id="srcALX034", work_author="Christopher Haas",
      work_title="Alexandria in Late Antiquity: Topography and Social Conflict (Johns Hopkins UP, 1997)",
      work_locus="1997",
      licensed_for=("Secondary scholarship (the S2.1b city-study gap): the "
                    "standard study of the city itself, whose social texture "
                    "the world's horizon lives in - confidence-judgment "
                    "apparatus only, never voice content."),
      verification_note=VNOTE),
 dict(id="srcALX035", work_author="Henri Crouzel",
      work_title="Origene (1985; ET Origen, 1989)",
      work_locus="1985/1989",
      licensed_for=("Secondary scholarship (the S2.1b per-figure-monograph "
                    "gap): the standard monograph on the figure whose "
                    "SYSTEMIC Author-Gravity screen governs the whole build "
                    "- confidence-judgment apparatus only, never voice "
                    "content."),
      verification_note=VNOTE),
 dict(id="srcALX036", work_author="Eric Osborn",
      work_title="Clement of Alexandria (Cambridge UP, 2005)",
      work_locus="2005",
      licensed_for=("Secondary scholarship (the S2.1b per-figure-monograph "
                    "gap): the standard monograph on the tradition's "
                    "founder-figure - confidence-judgment apparatus only, "
                    "never voice content."),
      verification_note=VNOTE),
 dict(id="srcALX037", work_author="Colin H. Roberts",
      work_title="Manuscript, Society and Belief in Early Christian Egypt (Schweich Lectures; OUP, 1979)",
      work_locus="1979",
      licensed_for=("Secondary scholarship (the S2.1b papyrological-classic "
                    "gap): the standard treatment of early Egyptian "
                    "Christian book culture - confidence-judgment apparatus "
                    "only, never voice content."),
      verification_note=VNOTE),
]

BODY = ("Rowed at the S6.2 pre-freeze re-sweep (2026-07-28) per the S2.1b "
        "disposition ('rowed there with real discovery data, or excluded "
        "with reasons') - the real discovery data is the S2.1b instrument "
        "itself. See wrs/migrate/s62_alx_presweep.py.")

SEARCH_NOTE = ("\n\nPre-freeze re-sweep (2026-07-28): the four S2.1b "
               "relative-recall/PRESS misses rowed as srcALX034-037 "
               "(Haas, Crouzel, Osborn, Roberts - the S-row scholarship-"
               "apparatus class; each verification_note declares the work "
               "not independently examined this session). The four named "
               "coverage limits (BIBP, L'Annee philologique, Oxford "
               "Bibliographies, CPG) STAND - no database access this "
               "session; saturation is NOT claimed improved beyond the "
               "recall-instrument closure. See "
               "wrs/migrate/s62_alx_presweep.py.")


def main():
    for r in ROWS:
        emit_record({**COMMON, **r}, BODY, OUT / f"{r['id']}.md")
    rec, body = read_record(SEARCH)
    if "Pre-freeze re-sweep (2026-07-28)" not in body:
        body += SEARCH_NOTE
        emit_record(rec, body, SEARCH)
    print(f"pre-freeze re-sweep: {len(ROWS)} scholarship rows "
          f"(srcALX034-037); search record annotated")


if __name__ == "__main__":
    main()
