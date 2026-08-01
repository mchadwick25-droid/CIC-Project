"""S6.2/PAHC - pre-freeze re-sweep: the S2.1b PRESS routings, rowed.

Three rows with REAL discovery data (the S2.1b PRESS named all three;
the SYR/HAL re-sweep precedent) + srcPAHCsearch002 (the re-sweep's own
search record under the V7.4 standard):

- srcPAHCS58 Bauer, Rechtglaeubigkeit und Ketzerei (1934) - the S2.1b
  round's one relative-recall MISS, and Doc_01's own STRAND-GROUND:
  the regional-diversity thesis under the strand-plural frame this
  whole world is built on. Rowing it names the intellectual ancestry
  the registry carried only implicitly.
- srcPAHCS59 Ste. Croix, "Why Were the Early Christians Persecuted?"
  (1963) - the standard legal-historical account of accusatory-process
  persecution: the scholarship class behind G03's
  name-and-accusation-on-any-ordinary-day shape (pahcgrav003,
  pahclex013's pertinacia debate rides its exchange with Sherwin-White).
- srcPAHCS60 Stark, The Rise of Christianity (1996) - the
  sociological growth/network account; the corroborator class for the
  correspondence-network and mutual-aid material (pahcgrav002,
  pahcstory013) at the social-mechanism level.

ID CONVENTION, declared: the registry currency ends at S57; S58-60
continue the S-sequence as RECORD-ONLY rows (the deployed
source_registry.json is the W1 build's artifact and is not
retro-edited). The workbook audit carries a declared allowance for
post-registry re-sweep rows (added-field marked).

DECLARED NON-ROWS (in srcPAHCsearch002, not silent):
- Sherwin-White's reply to Ste. Croix (1964) - named as the debate's
  other half in pahclex013's own material; the debate is carried by
  the pertinacia record's confidence apparatus, and the registry's
  own S-rows already carry the modern legal-historical digest class;
  one side is rowed as the PRESS named it, the exchange is cited
  where it lives.
- Bauer's 1971 English translation (Orthodoxy and Heresy) - an
  edition/translation of the rowed work, not a second work.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "pahc_world"
WID = "post-apostolic-house-church"

INSTRUMENT = ("S6.2/PAHC pre-freeze re-sweep (2026-07-31): the S2.1b "
              "relative-recall/PRESS routings executed "
              "(wrs/migrate/s62_pahc_resweep.py)")
CHANNEL_NOTE = (" - channel note: the S2.1b PRESS review supplied the "
                "naming (reviewer-supplied is the enum home for a "
                "review-instrument recall)")

ROWS = [
 {"id": "srcPAHCS58", "source_type": "S", "boundary_status": "Native",
  "attribution_status": "genuine", "level_of_description": "work",
  "language": "de", "script": "Latn",
  "work_author": "Walter Bauer",
  "work_title": ("Rechtglaeubigkeit und Ketzerei im aeltesten "
                 "Christentum (Tuebingen, 1934; Eng. tr. Orthodoxy "
                 "and Heresy in Earliest Christianity, 1971)"),
  "work_locus": "the regional-diversity thesis, whole-work level",
  "licensed_for": ("The STRAND-GROUND: the scholarly ancestry of "
                   "Doc_01's strand-plural frame (regional Christian "
                   "diversity prior to any normative center) - the "
                   "S2.1b round's one relative-recall MISS, absent "
                   "from the registry AND from Doc_02, grep-verified "
                   "then. Rowing it names the frame's ancestry; it "
                   "does NOT convert any strand claim into "
                   "Bauer's-thesis-as-established (the thesis is "
                   "itself heavily qualified by later scholarship, "
                   "and the world's strand discipline rests on the "
                   "primary rows, not on Bauer)."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b PRESS; not read for this migration - "
                        "rowed as the named ancestral work of its "
                        "class, the Wilson-Kastner/Krumeich caveat "
                        "pattern."),
  "discovery_channel": "reviewer-supplied",
  "discovery_instrument": INSTRUMENT + CHANNEL_NOTE,
  "discovery_date": "2026-07-31",
  "added": "2026-07-31 (S6.2/PAHC pre-freeze re-sweep)",
  "jobs": [1, 2]},
 {"id": "srcPAHCS59", "source_type": "S", "boundary_status": "Native",
  "attribution_status": "genuine", "level_of_description": "work",
  "language": "en", "script": "Latn",
  "work_author": "G. E. M. de Ste. Croix",
  "work_title": ("'Why Were the Early Christians Persecuted?', Past & "
                 "Present 26 (1963) 6-38"),
  "work_locus": "the article, whole-work level",
  "licensed_for": ("The standard legal-historical account of "
                   "accusatory-process persecution - the scholarship "
                   "class behind G03's shape (a name given, an "
                   "accusation made, on any ordinary day; no standing "
                   "police enforcement): pahcgrav003's modern ground, "
                   "and one half of the exchange pahclex013's "
                   "pertinacia-vs-nomen debate rides."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b PRESS; not read for this migration - "
                        "rowed as the named standard work. "
                        "Sherwin-White's 1964 reply is the debate's "
                        "other half - declared a non-row (see "
                        "srcPAHCsearch002)."),
  "discovery_channel": "reviewer-supplied",
  "discovery_instrument": INSTRUMENT + CHANNEL_NOTE,
  "discovery_date": "2026-07-31",
  "added": "2026-07-31 (S6.2/PAHC pre-freeze re-sweep)",
  "jobs": [1, 2]},
 {"id": "srcPAHCS60", "source_type": "S", "boundary_status": "Native",
  "attribution_status": "genuine", "level_of_description": "work",
  "language": "en", "script": "Latn",
  "work_author": "Rodney Stark",
  "work_title": ("The Rise of Christianity: A Sociologist Reconsiders "
                 "History (Princeton, 1996)"),
  "work_locus": "esp. the network-growth and mutual-aid chapters",
  "licensed_for": ("The sociological corroborator class for the "
                   "correspondence-network and mutual-aid material "
                   "(pahcgrav002, pahcstory013) at the "
                   "social-mechanism level - why letter-carried "
                   "translocal identity and costly mutual aid are "
                   "growth-bearing, as social mechanism. NEVER a "
                   "primary attestation of any practice (Stark's "
                   "quantitative projections are contested; the "
                   "practices rest on the primary rows)."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b PRESS; not read for this migration - "
                        "rowed as the named standard work of its "
                        "class, the caveat pattern."),
  "discovery_channel": "reviewer-supplied",
  "discovery_instrument": INSTRUMENT + CHANNEL_NOTE,
  "discovery_date": "2026-07-31",
  "added": "2026-07-31 (S6.2/PAHC pre-freeze re-sweep)",
  "jobs": [1, 2]},
]

SEARCH = {
    "id": "srcPAHCsearch002", "world_id": WID,
    "record_type": "search_record", "schema_version": 1,
    "register": "etic", "review_state": "draft", "jobs": [1],
    "sampling_strategy": (
        "Purposive (Booth's standard) - the PRE-FREEZE RE-SWEEP "
        "(2026-07-31): executes the S2.1b PRESS routings and "
        "re-states the standing limits; documents THIS re-sweep only "
        "(srcPAHCsearch001 documents the migration-time S2.1a "
        "sweep - the fleet's first clean sweep)."),
    "types_sought": [
        ("the three PRESS-named works (the Bauer strand-ground; the "
         "Ste. Croix legal-historical account; the Stark sociological "
         "corroborator)"),
        ("editions/translations and debate-partners adjacent to the "
         "three (the Bauer 1971 translation; the Sherwin-White "
         "reply)"),
    ],
    "approaches": {"press-routing-execution": 1,
                   "row-diff re-run": 1},
    "years_searched": {"from": 1934, "to": 2026},
    "languages_searched": ["en", "de"],
    "inclusion_exclusions": (
        "Included: the three PRESS routings, each rowed with its "
        "read-status caveat (rowed-as-named-standard-work, not "
        "read-in-full). Excluded with reasons: Sherwin-White 1964 "
        "(the pertinacia debate's other half - carried where the "
        "debate lives, in pahclex013's confidence apparatus; rowing "
        "one PRESS-named side does not owe the exchange a second "
        "row); Bauer 1971 English translation (an edition of the "
        "rowed work, not a second work)."),
    "terms_tried": [
        {"term": "the three S2.1b PRESS routings, executed as rows",
         "productive": True},
        {"term": "row-diff re-run after srcPAHCS58-60",
         "productive": False},
    ],
    "instruments": [
        INSTRUMENT,
        ("ID-CONVENTION NOTE: S58-60 continue the registry's "
         "S-currency as RECORD-ONLY rows; the deployed "
         "source_registry.json (the W1 artifact, reconciled == "
         "FINAL_v2.xlsx at world open) is not retro-edited. The "
         "workbook audit carries the declared allowance."),
        ("STANDING OPEN LIMITS, re-stated not satisfied: (1) BIBP / "
         "L'Annee philologique / Oxford Bibliographies remain "
         "unaccessed (the standing fleet limit); (2) the Ignatian "
         "authenticity debate's current state rests on the "
         "registry's own S-rows - no new sweep of the "
         "post-2015 literature was run; (3) the registry's "
         "Priority Review Queue items (47 rows flagged in the W1 "
         "workbook) remain the W1 build's own open review queue - "
         "carried, not closed, by this migration. These ride into "
         "the freeze declaration as declared limits, the SYR/HAL "
         "precedent."),
    ],
}

SEARCH_BODY = (
    "Saturation statement (V7.4; re-sweep scope): after rowing "
    "srcPAHCS58-60, the row-diff re-run finds no remaining chunk-cited "
    "or PRESS-named work without a row or a declared reason. The "
    "standing limits are re-stated as LIMITS (not satisfied searches) "
    "and ride into the freeze declaration.\n\n"
    "Provenance: wrs/migrate/s62_pahc_resweep.py (this file is the "
    "re-sweep log; all three rows carry real discovery data - the "
    "S2.1b PRESS naming, executed here).")


def main():
    for row in ROWS:
        rec = {"world_id": WID, "record_type": "source",
               "schema_version": 1, "register": "etic",
               "review_state": "draft", "disposition": "in-use", **row}
        emit_record(rec, ("Rowed at the S6.2/PAHC pre-freeze re-sweep "
                          "(2026-07-31) with real discovery data (the "
                          "S2.1b PRESS routing). See "
                          "wrs/migrate/s62_pahc_resweep.py and "
                          "srcPAHCsearch002."),
                    OUT / "source" / f"{row['id']}.md")
    emit_record(SEARCH, SEARCH_BODY,
                OUT / "search_record" / "srcPAHCsearch002.md")
    print("3 re-sweep rows + srcPAHCsearch002")


if __name__ == "__main__":
    main()
