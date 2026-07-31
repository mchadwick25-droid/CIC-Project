"""S6.2/PAHC - S2.1-equivalent: source rows + world_core.

THE FLEET'S FIRST MACHINE-REGISTRY WORLD: PAHC's own build already
formalized its registry as data/pahc_world/source_registry.json (73
rows, RECONCILED identical-ordered to
CiC_W1_Source_Registry_FINAL_v2.xlsx at the world-open survey - 73/73,
0 name mismatches). The 73 source records are generated MECHANICALLY
from that json, field-for-field, with NOTHING retyped:

- id: 'srcPAHC' + the registry's own id (srcPAHCP01 ... srcPAHCS57) -
  the registry ids are the deployed chunks' own citation currency
  ('Registry P07' inline in story Source lines), so the key is
  preserved mechanically for the S2.2 span resolver.
- source_type: Primary->P, Secondary->S, Material-External->M.
- boundary_status Native/Excluded verbatim (the schema enum matches
  the registry's own vocabulary); the NINE Excluded rows are kept as
  records with their exclusion_reason (disposition stays 'in-use' -
  the SYR precedent: an exclusion record is in use AS an exclusion).
- licensed_for verbatim; the registry's confidence_level /
  citation_reliability / priority_review_flag / notes ride
  verification_note as a labeled composite (no field invented, none
  dropped).
- discovery_channel: builder-prior-knowledge on all 73 (the HAL S2.1
  convention - the completion gate requires the field; the original
  build's actual discovery process is unrecoverable by design, and
  the registry is the build's own product, not a discovery log; no
  instrument/date fabricated).

Doc_02 AUTHORITY, pinned at the world-open survey:
CiC_W1_Doc02_Source_Ecology_FINAL.md (contains all of v3.docx PLUS
the Step-9 2026-07-08 additions SS1.7/SS1.8); the docx chain is
historical. The registry already carries the Step-9 rows (S56, S57
present) - cross-checked.

pahccore001 (from Doc_01 FINAL.md, read this step):
- time_window 70-200 with Doc_01 SS2.1's own honesty carried: 70 CE
  is the inherited constitutional floor, 'comparatively weak as an
  internal marker' - the lived post-apostolic transition 'firms up
  gradually across 64-100 CE'; the c. 200 close rests on SS2.2's
  three convergent fronts (monepiscopacy dominant; the
  apologetic/systematic mode arguing FROM succession; Alexandria's
  own teaching-formation gravity emerging as the documented handoff
  to World #2).
- STRAND NOTE - the first strand-PLURAL world in the migrated fleet:
  Doc_01 SS6 records internal strands rather than declaring
  strand-singular (the Bauer/Ehrman regional-differentiation
  literature is the documented ground; SS3's porous-boundary and
  SS4's non-uniformity cautions read together by Doc_04's own
  instruction).
- formation_logic: household- and correspondence-based pastoral
  formation (Doc_01 SS8.2's own contrast phrase vs Alexandria).
- gravities [] until the S2.5-equivalent (the registry's G01/G03
  labels in deployed chunks are Doc_04's naming scheme).
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "pahc_world"
WID = "post-apostolic-house-church"
REGISTRY = BACKEND / "data" / "pahc_world" / "source_registry.json"

TYPE_MAP = {"Primary": "P", "Secondary": "S", "Material-External": "M"}


def source_rows():
    rows = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert len(rows) == 73, len(rows)
    out = []
    for r in rows:
        vn = (f"Registry-carried assessment fields, verbatim: "
              f"confidence_level={r['confidence_level']}; "
              f"citation_reliability={r['citation_reliability']}; "
              f"priority_review_flag={r['priority_review_flag']}."
              + (f" Notes: {r['notes']}" if r.get("notes") else ""))
        if r["boundary_status"] == "Excluded" and r.get("exclusion_reason"):
            vn += f" EXCLUSION REASON (registry, verbatim): {r['exclusion_reason']}"
        rec = {
            "id": "srcPAHC" + r["id"], "world_id": WID,
            "record_type": "source", "schema_version": 1,
            "register": "etic", "review_state": "draft",
            "disposition": "in-use",
            "source_type": TYPE_MAP[r["source_type"]],
            "boundary_status": r["boundary_status"],
            "attribution_status": "genuine",
            "level_of_description": "work",
            "language": "grc" if r["id"].startswith("P") else "en",
            "script": "Latn",
            "work_author": r["author_voice"],
            "work_title": r["source_name_short_citation"],
            "work_locus": r["date_or_period"],
            "licensed_for": r["licensed_for"] or
                            "(registry licensed_for empty - Excluded row)",
            "verification_note": vn,
            # the HAL S2.1 convention: the original build's channel is
            # unrecoverable; builder-prior-knowledge is the backfill
            # enum home for registry-era rows
            "discovery_channel": "builder-prior-knowledge",
            "added": "2026-07-31 (S6.2/PAHC S2.1, mechanical from "
                     "data/pahc_world/source_registry.json)",
            "jobs": [1, 2],
        }
        out.append(rec)
    return out


CORE = {
    "id": "pahccore001", "world_id": WID, "record_type": "world_core",
    "schema_version": 1, "jobs": [1, 2, 4], "register": "etic",
    "review_state": "draft",
    "time_window": {
        "start_year": 70, "end_year": 200,
        "note": (
            "Doc_01 SS2's own honesty carried whole: 70 CE is the "
            "inherited Step-0 constitutional floor - 'comparatively "
            "weak as an internal marker' for this world's own "
            "transition, which 'most plausibly firms up gradually "
            "across 64-100 CE, not at a single crisp date' (the "
            "Ways-That-Never-Parted literature dissolves any "
            "clean-break date rather than substituting one; Contested, "
            "SS2.1's own tag). The c. 200 close rests on three "
            "convergent fronts (SS2.2/SS8): monepiscopacy become the "
            "dominant authority pattern over the collegial-presbyter "
            "default; the apologetic/systematic mode (Irenaeus, "
            "Tertullian) arguing FROM apostolic succession as already "
            "established; and Alexandria's teaching-relationship "
            "formation gravity independently emerging in the closing "
            "years - the documented handoff to World #2 (SS8.2: "
            "overlap c. 190-200, 'a genuine, evidence-supported "
            "handoff rather than a contradiction')."),
    },
    "horizon": (
        "The Roman-Mediterranean correspondence network: Antioch, the "
        "Asia Minor road and sea routes (Ignatius's guarded journey; "
        "Smyrna, Ephesus, Philadelphia), Rome, Corinth, Philippi, "
        "Bithynia-Pontus (Pliny's province) - house-church communities "
        "inside Roman imperial infrastructure, connected by letter and "
        "courier; persecution local, sporadic, improvised, never yet "
        "systematic (Doc_01 SS3/SS4, with the collegia-law analogy "
        "left unsettled per SS4's own caution)."),
    "formation_logic": (
        "Doc_01 SS8.2's own contrast phrase: household- and "
        "correspondence-based pastoral formation - catechesis via "
        "community letter and adaptable handbook (the Two Ways; the "
        "Didache's living instructions), the letter read aloud as the "
        "community's formation event, table and baptism ordering "
        "common life, authority still being actively built through "
        "pastoral correspondence rather than argued from settled "
        "succession."),
    # strand structure rides the record BODY verbatim (the schema's
    # world_core field set has no strand home; declared, not dropped)
    "_strand_body": (
        "STRAND NOTE - THE FIRST STRAND-PLURAL WORLD IN THE MIGRATED "
        "FLEET: Doc_01 "
        "SS6 records internal strands rather than declaring "
        "strand-singular - regional connectedness justifies one world; "
        "regional differentiation (Bauer 1934, extended by "
        "Ehrman/Robinson-Koester; counter-critiques operate inside the "
        "same regionally-differentiated framework) requires recording "
        "strands within it. SS2.1's porous Jewish-Christian boundary "
        "caveat and SS4's non-uniformity caveat are 'to be read "
        "together' by Doc_04's own instruction. Live rival movements "
        "(Marcionite, Valentinian, Montanist) are contemporary "
        "in-window neighbors, not settled heresies (SS8.3) - the "
        "boundary drawn in real time, never inherited."),
    "gravities": [],
    "sources": [{"source_id": "srcPAHCP01"}, {"source_id": "srcPAHCP03"},
                {"source_id": "srcPAHCP07"}],
}


def main():
    (OUT / "source").mkdir(parents=True, exist_ok=True)
    (OUT / "world_core").mkdir(parents=True, exist_ok=True)
    rows = source_rows()
    for rec in rows:
        emit_record(rec, ("Migrated at the S6.2/PAHC S2.1-equivalent "
                          "(2026-07-31), MECHANICALLY from "
                          "data/pahc_world/source_registry.json (the "
                          "fleet's first machine-registry world; the "
                          "json reconciled identical to "
                          "CiC_W1_Source_Registry_FINAL_v2.xlsx at the "
                          "world-open survey). Original discovery "
                          "unrecoverable by design (backfill rule)."),
                    OUT / "source" / f"{rec['id']}.md")
    strand = CORE.pop("_strand_body")
    emit_record(CORE, (strand + "\n\nMigrated at the S6.2/PAHC S2.1-equivalent "
                       "(2026-07-31) from "
                       "CiC_W1_Doc01_World_Identification_FINAL.md "
                       "(read in full this step; Doc_02 authority = "
                       "FINAL.md per the world-open survey). See "
                       "wrs/migrate/s62_pahc_s21.py."),
                OUT / "world_core" / "pahccore001.md")
    n_ex = sum(1 for r in rows if r["boundary_status"] == "Excluded")
    print(f"emitted {len(rows)} source rows ({n_ex} Excluded) + pahccore001")


if __name__ == "__main__":
    main()
