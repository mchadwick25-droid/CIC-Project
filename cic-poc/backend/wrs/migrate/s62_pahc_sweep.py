"""S6.2/PAHC - S2.1a-equivalent: discovery sweep + search record.

THE SWEEP: all 26 deployed chunks read (13 lexicon Key Sources
sections - 11 with the section, 2 THIN-FORMAT chunks
(pahclex012/013, front-matter + Quick Meaning + Distortion Risk only,
the SYR Tier-3 thin class; their evidentiary base is Pliny P07 via
their own front matter) - plus 13 story Source lines), each citation
adjudicated against the 73 S2.1 rows.

RESULT - THE FLEET'S FIRST CLEAN SWEEP: ZERO miss rows. Every story
Source line carries an inline registry tag (Registry P01-P16 class,
all rowed); every lexicon Key Sources citation resolves by name to a
registered P-row (Ignatius->P03, 1 Clement->P02, Hermas->P05,
Didache->P01, Polycarp->P04, Justin->P06, Pliny->P07). The
machine-registry world's own build discipline is what the sweep
instrument was built to catch the absence of - and here there is
nothing to catch. Verified mechanically below (the script re-runs the
tag check; the name-resolution table is recorded in the checkpoint).

DECLARED NON-ROWS (in srcPAHCsearch001, not silent):
- Epistle of Barnabas 18-20: named by pahclex007's own note as "not
  part of this world's own defined source set" - the chunk itself
  draws the boundary; no row owed, the boundary honored.
- Hermas, Mandate 11: named by pahclex008's note as a topical
  parallel whose correspondence "is not established by this world's
  own sources" - and Hermas the work IS rowed (P05); the
  parallel-passage caveat rides the chunk, not a new row.
- The Roberts-Donaldson/ANF translation (pahclex010's verification
  citation) - the editions/translations class, deferred to the
  pre-freeze re-sweep per the standing fleet rule.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "pahc_world"
DATA = BACKEND / "data" / "pahc_world"
WID = "post-apostolic-house-church"

SWEEP_INSTRUMENT = ("S2.1a deployed-chunk sweep (all 26 PAHC chunks: 11 "
                    "lexicon Key Sources sections + 2 thin-format chunks "
                    "+ 13 story Source lines, diffed against the 73 "
                    "machine-registry rows; "
                    "wrs/migrate/s62_pahc_sweep.py)")

SEARCH = {
    "id": "srcPAHCsearch001", "world_id": WID,
    "record_type": "search_record", "schema_version": 1,
    "register": "etic", "review_state": "draft", "jobs": [1],
    "sampling_strategy": (
        "Purposive, not comprehensive (Booth's standard) - EXPLICITLY "
        "SCOPED AS A MIGRATION-TIME SEARCH (2026-07-31, S6.2/PAHC "
        "S2.1a), documenting this sweep only, never the original "
        "build's own discovery process (unrecoverable by design per "
        "the backfill rule). Fourth sweep under the governing V7.4 "
        "Step 2 standard (ALX/SYR/HAL precedents)."),
    "types_sought": [
        ("works load-bearing in the deployed chunks' own Key Sources / "
         "story Source lines but absent from the S2.1 rows"),
        ("critical editions and standard translations (deferred to the "
         "pre-freeze re-sweep, fleet rule)"),
    ],
    "approaches": {"deployed-chunk-citation-sweep": 1,
                   "registry-tag-verification": 1},
    "years_searched": {"from": 1975, "to": 2026},
    "languages_searched": ["en"],
    "inclusion_exclusions": (
        "Included: every chunk-cited work checked at work level - "
        "RESULT: ZERO misses, the fleet's first clean sweep (the "
        "machine-registry world's own build discipline: story Source "
        "lines carry inline registry tags; lexicon citations resolve "
        "by name to registered P-rows). Excluded with reasons: the "
        "Epistle of Barnabas 18-20 (pahclex007's OWN note declares it "
        "outside this world's defined source set - the chunk draws "
        "the boundary, honored not re-litigated); Hermas Mandate 11 "
        "(pahclex008's topical-parallel caveat; the work itself is "
        "rowed as P05); the Roberts-Donaldson/ANF translation "
        "(pahclex010's verification citation - editions class, "
        "pre-freeze re-sweep)."),
    "terms_tried": [
        {"term": ("story Source-line registry tags, all 13 stories "
                  "(mechanical: every 'Registry Pnn' tag has a row)"),
         "productive": False},
        {"term": ("lexicon Key Sources name-resolution, all 11 "
                  "sectioned chunks + 2 thin-format front matters"),
         "productive": False},
    ],
    "instruments": [
        SWEEP_INSTRUMENT,
        ("NOT ACCESSED, logged as coverage limits of this "
         "migration-time sweep: BIBP; L'Annee philologique; Oxford "
         "Bibliographies. The registry's own priority_review_flag "
         "queue (49 flagged rows in the FINAL_v2 workbook) is the "
         "build's own review instrument, already absorbed row-by-row "
         "via the verbatim assessment fields. Re-run before "
         "world-freeze."),
    ],
}

SEARCH_BODY = (
    "Saturation statement (V7.4 Step 2; migration-time scope): the "
    "citation sweep found ZERO row-less citations at work level across "
    "all 26 chunks - the fleet's first clean sweep, a product of the "
    "original build's own machine registry (story chunks cite by "
    "inline registry tag; the registry was already reconciled "
    "json==xlsx at the world-open survey). The named coverage limits "
    "(BIBP; L'Annee philologique; Oxford Bibliographies) are recorded "
    "as LIMITS, not satisfied searches; the pre-freeze re-sweep must "
    "address them plus the ANF/Roberts-Donaldson editions item.\n\n"
    "Sweep provenance: wrs/migrate/s62_pahc_sweep.py (this file is the "
    "sweep log; it emits no source rows because none were owed - the "
    "mechanical tag-check re-runs on every invocation).")


def verify_tags():
    reg_ids = {r["id"] for r in json.loads(
        (DATA / "source_registry.json").read_text(encoding="utf-8"))}
    cited = set()
    for p in sorted((DATA / "story_chunks").glob("*.md")):
        cited |= set(re.findall(r"Registry ([PS]\d+)",
                                p.read_text(encoding="utf-8")))
    for p in sorted((DATA / "lexicon_chunks").glob("*.md")):
        cited |= set(re.findall(r"Registry ([PS]\d+)",
                                p.read_text(encoding="utf-8")))
    missing = cited - reg_ids
    assert not missing, missing
    return len(cited)


def main():
    n = verify_tags()
    (OUT / "search_record").mkdir(exist_ok=True)
    emit_record(SEARCH, SEARCH_BODY,
                OUT / "search_record" / "srcPAHCsearch001.md")
    print(f"clean sweep verified ({n} distinct registry tags cited, all "
          f"rowed; 0 miss rows) + srcPAHCsearch001")


if __name__ == "__main__":
    main()
