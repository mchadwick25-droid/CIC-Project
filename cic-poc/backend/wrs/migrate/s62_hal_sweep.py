"""S6.2/HAL - S2.1a-equivalent: discovery sweep + search record.

THE SWEEP (the ALX On-the-Incarnation class): all 27 deployed chunks
read (15 lexicon Key Sources sections + 12 story front-matter Source
lines), each citation adjudicated against the 22 S2.1 rows.

ONE genuine miss, rowed with REAL discovery data:
- srcHAL023: Jerome's prefaces (Praefationes) as a corpus - cited as
  THE PRIMARY SOURCE by hal_lex01 (the Hebraica veritas principle's
  own articulation) and hal_lex13 (whose whole entry is the genre:
  'dozens survive... by its very genre a single-voice, self-justifying
  source type'). The prefaces travel physically inside the Vulgate and
  commentary volumes (srcHAL002/003) but function as a distinct cited
  CLASS at corpus level, which no row covered.

DECLARED NON-ROWS (in srcHALsearch001, not silent):
- Perseus critical text (hal_lex14's 'verified directly against
  critical text (Perseus)' for Ep. 77.6) - the editions/translations
  class, deferred to the pre-freeze re-sweep per the standing fleet
  rule (the ALX Howard/Lollar precedent).
- 'General social-historical scholarship on senatorial households'
  (hal_lex05, hal_lex10) - an UNNAMED aggregate; no work named, no row
  possible without manufacturing one; the S2.1b PRESS question is the
  instrument that names the standard works if any belong.
- Every other citation resolves: Epp. 22/77/107/108/127 + Riparius ->
  srcHAL001; prefaces-as-Vulgate-apparatus context -> 002/003;
  Jerome-Augustine -> 009; the two Apologiae -> 005/007; the vitae ->
  004; Rebenich/Cain -> 015/010; composites -> their own Source
  Identification tables (S2.4's job).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "hieronymian_world"
WID = "hieronymian-ascetic-literary"

SWEEP_INSTRUMENT = ("S2.1a deployed-chunk Key-Sources sweep (all 27 HAL "
                    "chunks: 15 lexicon Key Sources sections + 12 story "
                    "Source lines, diffed against the S2.1 rows; "
                    "wrs/migrate/s62_hal_sweep.py)")

ROW = {
    "world_id": WID, "record_type": "source", "schema_version": 1,
    "register": "etic", "review_state": "draft", "disposition": "in-use",
    "id": "srcHAL023", "source_type": "P", "boundary_status": "Native",
    "attribution_status": "genuine", "level_of_description": "corpus",
    "language": "lat", "script": "Latn",
    "work_author": "Jerome",
    "work_title": ("The Praefationes (prefaces) to the Vulgate books and "
                   "the biblical commentaries - dozens survive; the "
                   "primary source for the Hebraica veritas principle's "
                   "own articulation"),
    "work_locus": "c. 382-405",
    "licensed_for": ("Voice and confidence work for the world's defining "
                     "textual-authority principle - ALWAYS with "
                     "hal_lex13's own genre caveat attached: 'by its very "
                     "genre, a single-voice, self-justifying source type; "
                     "it cannot independently corroborate its own "
                     "claims.'"),
    "verification_note": ("Rowed at the S2.1a sweep: cited as the PRIMARY "
                          "source by hal_lex01 and hal_lex13, but no S2.1 "
                          "row covered the prefaces as a corpus-level "
                          "cited class (they travel physically inside "
                          "srcHAL002/003's volumes - a containment "
                          "relation, not a citation identity)."),
    "discovery_channel": "backward-snowball",
    "discovery_instrument": SWEEP_INSTRUMENT,
    "discovery_date": "2026-07-31",
    "added": "2026-07-31 (S6.2/HAL S2.1a sweep)",
    "jobs": [1, 2],
}

SEARCH = {
    "id": "srcHALsearch001", "world_id": WID,
    "record_type": "search_record", "schema_version": 1,
    "register": "etic", "review_state": "draft", "jobs": [1],
    "sampling_strategy": (
        "Purposive, not comprehensive (Booth's standard) - EXPLICITLY "
        "SCOPED AS A MIGRATION-TIME SEARCH (2026-07-31, S6.2/HAL "
        "S2.1a), documenting this sweep only, never the original "
        "build's own discovery process (unrecoverable by design per "
        "the backfill rule). Third sweep under the governing V7.4 Step "
        "2 standard (ALX/SYR precedents)."),
    "types_sought": [
        ("works load-bearing in the deployed chunks' own Key Sources / "
         "story Source lines but absent from the S2.1 rows"),
        ("critical editions and standard translations (deferred to the "
         "pre-freeze re-sweep, fleet rule)"),
    ],
    "approaches": {"deployed-chunk-key-sources-sweep": 1,
                   "row-diff": 1},
    "years_searched": {"from": 1975, "to": 2026},
    "languages_searched": ["en"],
    "inclusion_exclusions": (
        "Included: every chunk-cited work no row covered at "
        "work-or-corpus level (one found: the Praefationes corpus). "
        "Excluded: works inside existing corpus rows (all Epistulae "
        "citations incl. the Riparius letter -> srcHAL001; the two "
        "Apologiae -> 005/007; the vitae -> 004; the Augustine "
        "correspondence -> 009; Rebenich/Cain -> 015/010); the Perseus "
        "critical-text verification (editions class, pre-freeze "
        "re-sweep); the UNNAMED 'general social-historical scholarship "
        "on senatorial households' aggregate (hal_lex05/10 - no work "
        "named, none manufactured; the S2.1b PRESS names candidates "
        "if any belong); composite stories' Source Identification "
        "tables (S2.4's own layer)."),
    "terms_tried": [
        {"term": ("Key Sources sections + story Source lines, all 27 "
                  "deployed HAL chunks (diff vs rows)"), "productive": True},
        {"term": "row-diff re-run after adding srcHAL023",
         "productive": False},
    ],
    "instruments": [
        ("deployed-chunk Key-Sources sweep (the productive instrument; "
         "wrs/migrate/s62_hal_sweep.py)"),
        ("NOT ACCESSED, logged as coverage limits of this "
         "migration-time sweep: BIBP; L'Annee philologique; Oxford "
         "Bibliographies; PLUS this world's own two Doc_02-flagged "
         "verification items, which STAND as open until someone with "
         "the texts runs them - the Marcella-correspondence list vs "
         "Cain's critical apparatus (srcHAL001's own caveat) and the "
         "Palladius passage hunt (srcHAL008's do-not-cite license). "
         "Re-run before world-freeze."),
    ],
}

SEARCH_BODY = (
    "Saturation statement (V7.4 Step 2; migration-time scope): the "
    "row-diff re-run after adding srcHAL023 found no remaining row-less "
    "citation at work or corpus level across all 27 chunks. The named "
    "coverage limits (BIBP; L'Annee philologique; Oxford "
    "Bibliographies) and this world's own two Doc_02-flagged "
    "verification items (the Marcella-list apparatus check; the "
    "Palladius passage location) are recorded as LIMITS, not satisfied "
    "searches; the pre-freeze re-sweep must address them.\n\n"
    "Sweep provenance: wrs/migrate/s62_hal_sweep.py (this file is the "
    "sweep log; srcHAL023 carries real discovery data, unlike the "
    "migrated srcHAL001-022 whose historical discovery is "
    "unrecoverable by design).")


def main():
    emit_record(ROW, ("Rowed at the S6.2/HAL S2.1a sweep (2026-07-31) "
                      "with real discovery data. See "
                      "wrs/migrate/s62_hal_sweep.py and srcHALsearch001."),
                OUT / "source" / "srcHAL023.md")
    (OUT / "search_record").mkdir(exist_ok=True)
    emit_record(SEARCH, SEARCH_BODY,
                OUT / "search_record" / "srcHALsearch001.md")
    print("1 sweep row + srcHALsearch001")


if __name__ == "__main__":
    main()
