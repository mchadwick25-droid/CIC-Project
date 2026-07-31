"""S6.2/HAL - pre-freeze re-sweep: the S2.1b PRESS routings, rowed.

Three rows with REAL discovery data (the S2.1b PRESS named all three;
the SYR srcSYR062-064 precedent) + srcHALsearch002 (the re-sweep's own
search record under the V7.4 standard):

- srcHAL024 Brown, Through the Eye of a Needle (2012) - the standard
  study of senatorial wealth renunciation; gives the chunks' unnamed
  "general social-historical scholarship on senatorial households"
  aggregate (hal_lex05/10) a real referent, and is the independent
  corroborator class Doc_04's G2 correction names.
- srcHAL025 Letsch-Brunner, Marcella - Discipula et Magistra (1998) -
  the standard scholarly monograph on Marcella, the named pole of the
  bipolar structure; scholarly apparatus for the single most
  Author-Gravity-constrained material (hallex11/halclaim005).
- srcHAL026 Hilberg, CSEL 54-56 (1910-1918) - the critical edition of
  the Epistulae; the editions class (the ALX Howard/Lollar re-sweep
  precedent), and the concrete apparatus against which srcHAL001's own
  Marcella-correspondence-list caveat says the numbering must be
  verified.

DECLARED NON-ROWS (in srcHALsearch002, not silent):
- Perseus (hal_lex14's Ep. 77.6 verification vehicle) - a text
  PLATFORM, not a work; the editions-class work is the critical
  edition itself (srcHAL026); no row owed, named here.
- The two Doc_02-flagged verification items REMAIN OPEN LIMITS: the
  Marcella-list apparatus check (now concretely runnable against
  srcHAL026 + srcHAL010's apparatus, but requiring someone with the
  texts) and the Palladius passage hunt (srcHAL008's do-not-cite
  license stands until the passage is located). Rowing the tools is
  not running the check - the limits STAND, stated plainly.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "hieronymian_world"
WID = "hieronymian-ascetic-literary"

INSTRUMENT = ("S6.2/HAL pre-freeze re-sweep (2026-07-31): the S2.1b "
              "relative-recall/PRESS routings executed "
              "(wrs/migrate/s62_hal_resweep.py)")

ROWS = [
 {"id": "srcHAL024", "source_type": "S", "boundary_status": "Native",
  "attribution_status": "genuine", "level_of_description": "work",
  "language": "en", "script": "Latn",
  "work_author": "Peter Brown",
  "work_title": ("Through the Eye of a Needle: Wealth, the Fall of "
                 "Rome, and the Making of Christianity in the West, "
                 "350-550 AD (Princeton, 2012)"),
  "work_locus": "esp. the chapters on Roman senatorial renunciation",
  "licensed_for": ("The independent social-historical corroborator "
                   "for the senatorial-renunciation pattern - the "
                   "class Doc_04's G2 Round-1 correction names as the "
                   "ACTUAL independent attestation (the three letters "
                   "being one author's one genre); gives hal_lex05/10's "
                   "unnamed 'general social-historical scholarship on "
                   "senatorial households' aggregate a real referent."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b PRESS (the round's one relative-recall "
                        "MISS - absent from the rows AND from Doc_02 "
                        "itself, grep-verified then); not read "
                        "cover-to-cover for this migration - rowed as "
                        "the named standard work of its class, the "
                        "Wilson-Kastner/Krumeich caveat pattern."),
  "discovery_channel": "reviewer-supplied",
  "discovery_instrument": INSTRUMENT + " - channel note: the S2.1b PRESS review supplied the naming (reviewer-supplied is the enum home for a review-instrument recall)",
  "discovery_date": "2026-07-31",
  "added": "2026-07-31 (S6.2/HAL pre-freeze re-sweep)",
  "jobs": [1, 2]},
 {"id": "srcHAL025", "source_type": "S", "boundary_status": "Native",
  "attribution_status": "genuine", "level_of_description": "work",
  "language": "de", "script": "Latn",
  "work_author": "Silvia Letsch-Brunner",
  "work_title": ("Marcella - Discipula et Magistra: Auf den Spuren "
                 "einer romischen Christin des 4. Jahrhunderts "
                 "(de Gruyter, 1998)"),
  "work_locus": "the standard monograph, whole-work level",
  "licensed_for": ("Scholarly apparatus for the Marcella material - "
                   "the single most Author-Gravity-constrained "
                   "entry/story/claim set in this world (hallex11, "
                   "halstory07, halclaim005); a second scholarly "
                   "treatment standing beside Cain's readings "
                   "(srcHAL010/012), NEVER a second attestation of the "
                   "standing itself (which remains single-source, Ep. "
                   "127 - the discipline is unchanged)."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b PRESS (named there as the standard "
                        "Marcella monograph whose absence mattered "
                        "most); not read for this migration - rowed as "
                        "the named standard work, the caveat "
                        "pattern."),
  "discovery_channel": "reviewer-supplied",
  "discovery_instrument": INSTRUMENT + " - channel note: the S2.1b PRESS review supplied the naming (reviewer-supplied is the enum home for a review-instrument recall)",
  "discovery_date": "2026-07-31",
  "added": "2026-07-31 (S6.2/HAL pre-freeze re-sweep)",
  "jobs": [1, 2]},
 {"id": "srcHAL026", "source_type": "S", "boundary_status": "Native",
  "attribution_status": "genuine", "level_of_description": "work",
  "language": "la", "script": "Latn",
  "work_author": "Isidor Hilberg (ed.)",
  "work_title": ("Sancti Eusebii Hieronymi Epistulae, CSEL 54-56 "
                 "(Vienna, 1910-1918) - the critical edition of "
                 "Jerome's letters"),
  "work_locus": "the three-volume critical edition (work level: an edition-class work), apparatus level",
  "licensed_for": ("The editions class (the ALX Howard/Lollar "
                   "re-sweep precedent): the concrete critical "
                   "apparatus against which srcHAL001's own "
                   "Marcella-correspondence-list caveat says the "
                   "letter numbering must be verified. Rowing the "
                   "edition does NOT run that check - the check "
                   "remains an open limit until someone with the "
                   "texts runs it (srcHALsearch002)."),
  "verification_note": ("Rowed at the pre-freeze re-sweep from the "
                        "S2.1b PRESS (the editions-class routing, "
                        "same lane as the Perseus item - which is a "
                        "platform, not a work, and gets no row)."),
  "discovery_channel": "reviewer-supplied",
  "discovery_instrument": INSTRUMENT + " - channel note: the S2.1b PRESS review supplied the naming (reviewer-supplied is the enum home for a review-instrument recall)",
  "discovery_date": "2026-07-31",
  "added": "2026-07-31 (S6.2/HAL pre-freeze re-sweep)",
  "jobs": [1, 2]},
]

SEARCH = {
    "id": "srcHALsearch002", "world_id": WID,
    "record_type": "search_record", "schema_version": 1,
    "register": "etic", "review_state": "draft", "jobs": [1],
    "sampling_strategy": (
        "Purposive (Booth's standard) - the PRE-FREEZE RE-SWEEP "
        "(2026-07-31): executes the S2.1b PRESS routings and "
        "re-states the standing limits; documents THIS re-sweep only "
        "(srcHALsearch001 documents the migration-time S2.1a "
        "sweep)."),
    "types_sought": [
        ("the three PRESS-named works (senatorial-renunciation "
         "social history; the Marcella monograph; the critical "
         "edition of the Epistulae)"),
        ("editions/platforms cited by deployed chunks (the Perseus "
         "item)"),
    ],
    "approaches": {"press-routing-execution": 1,
                   "row-diff re-run": 1},
    "years_searched": {"from": 1975, "to": 2026},
    "languages_searched": ["en", "de"],
    "inclusion_exclusions": (
        "Included: the three PRESS routings, each rowed with its "
        "read-status caveat (rowed-as-named-standard-work, not "
        "read-in-full - the Wilson-Kastner/Krumeich pattern). "
        "Excluded with reasons: Perseus (hal_lex14's Ep. 77.6 "
        "verification vehicle - a text platform, not a work; the "
        "editions-class work is srcHAL026; no row owed)."),
    "terms_tried": [
        {"term": "the three S2.1b PRESS routings, executed as rows",
         "productive": True},
        {"term": "row-diff re-run after srcHAL024-026",
         "productive": False},
    ],
    "instruments": [
        INSTRUMENT,
        ("STANDING OPEN LIMITS, re-stated not satisfied: (1) the "
         "Marcella-correspondence-list apparatus check - srcHAL001's "
         "own caveat; now concretely runnable against srcHAL026 + "
         "srcHAL010's apparatus but NOT RUN (requires the physical/"
         "digital texts); (2) the Palladius passage hunt - "
         "srcHAL008's do-not-cite license STANDS until the "
         "Paula-circle passage is located; (3) BIBP / L'Annee "
         "philologique / Oxford Bibliographies remain unaccessed. "
         "These carry into the freeze declaration as declared "
         "limits, the SYR precedent."),
    ],
}

SEARCH_BODY = (
    "Saturation statement (V7.4; re-sweep scope): after rowing "
    "srcHAL024-026, the row-diff re-run finds no remaining "
    "chunk-cited or PRESS-named work without a row or a declared "
    "reason. The three standing verification limits are re-stated as "
    "LIMITS (not satisfied searches) and ride into the freeze "
    "declaration.\n\n"
    "Provenance: wrs/migrate/s62_hal_resweep.py (this file is the "
    "re-sweep log; all three rows carry real discovery data - the "
    "S2.1b PRESS naming, executed here).")


def main():
    for row in ROWS:
        rec = {"world_id": WID, "record_type": "source",
               "schema_version": 1, "register": "etic",
               "review_state": "draft", "disposition": "in-use", **row}
        emit_record(rec, ("Rowed at the S6.2/HAL pre-freeze re-sweep "
                          "(2026-07-31) with real discovery data (the "
                          "S2.1b PRESS routing). See "
                          "wrs/migrate/s62_hal_resweep.py and "
                          "srcHALsearch002."),
                    OUT / "source" / f"{row['id']}.md")
    emit_record(SEARCH, SEARCH_BODY,
                OUT / "search_record" / "srcHALsearch002.md")
    print("3 re-sweep rows + srcHALsearch002")


if __name__ == "__main__":
    main()
