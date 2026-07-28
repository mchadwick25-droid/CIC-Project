"""S6.2/Syriac - S2.1-equivalent: world_core + source rows.

UNLIKE Desert and Alexandria, Syriac arrives with a DEPLOYED structured
registry (data/syriac_world/source_registry.json, 53 rows with id/source/
type/confidence/boundary_status/exclusion_reason/licensed_for/
verification_note/comparandum_note/added) - the Source Registry Template's
own columns, already runtime data. The migration is therefore mechanical
over that registry (nothing retyped), with Doc_02_Source_Ecology.md as
the narrative authority the R checkpoint reads against:

- work_title = the registry `source` string VERBATIM (no author/title
  parse - a mechanical split would garble rows like the bnay-qyama
  attestation row; the composite citation IS the registry's own record).
- type -> source_type (P/S/M, all in the schema enum).
- boundary_status: Native/Excluded verbatim; the ONE 'Native (Contested)'
  row (12, Odes of Solomon) normalizes to the schema's Native with the
  contest carried VERBATIM in the record (Doc_02 SS8's own wording) -
  declared, not silent; widening the enum would be a CO this row does
  not need (the contest is provenance, which the record text carries).
- exclusion_reason / comparandum_note / licensed_for / verification_note:
  verbatim. Excluded rows with empty licensed_for get the explicit
  not-licensed statement (the field is gate-required; an empty string
  would read as an oversight rather than a decision).
- registry confidence grade (A-E): carried in each record body verbatim
  (no schema field exists for it; ALX precedent keeps grades out of
  frontmatter).
- attribution_status / level_of_description / language / script /
  genre_form: per-id declared maps below, each assignment traceable to
  Doc_02's own prose (e.g. Chronicle of Edessa anonymous; the Odes
  pseudonymous with language 'und' because Doc_02 carries original
  language as disputed; the Diatessaron 'und' likewise + aggregate-
  attestation because no manuscript survives; the baptistery 'zxx' no
  linguistic content). genre_form set only where an enum value honestly
  fits (the ALX rule), unset otherwise.
- Backfill rule (SS3.1): migrated rows carry NO discovery_instrument/
  discovery_date; the registry's own `added` value rides verbatim.

world_core syrcore001 from Doc_01: time_window 200-410 (the SS2 Round-2
revision - 410 Synod of Seleucia-Ctesiphon as the institutional-
structural change; 373 Ephrem's death an internal hinge, NOT the
boundary; 363 Nisibis cession an internal transition); formation_logic
verbatim from Doc_01 SS1; gravities [] until the S2.5-equivalent.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from s62_alx_source_rows import emit_record

REGISTRY = BACKEND / "data" / "syriac_world" / "source_registry.json"
OUT = BACKEND / "wrs" / "records" / "syriac_world"
DOC01 = "World-Builds/Syriac-Christianity-Edessa-Nisibis/Doc_01_World_Identification_Boundaries_Orientation.md"
DOC02 = "World-Builds/Syriac-Christianity-Edessa-Nisibis/Doc_02_Source_Ecology.md"

COMMON = {"world_id": "syriac-edessa-nisibis", "record_type": "source",
          "schema_version": 1, "register": "etic", "review_state": "draft",
          "disposition": "in-use"}

# ---- per-id declared maps (assignments traceable to Doc_02 prose) ----
# language: ISO 639-3. Default: P-rows syr, S-rows eng; exceptions here.
LANG = {  # exceptions only
 "11": "und",  # Diatessaron: original language (Syriac vs Greek) unresolved (Doc_02 SS2)
 "12": "und",  # Odes: "provenance, date, and original language are all disputed" (Butts, Doc_02 SS2)
 "15": "und",  # Marcion: works lost, known via hostile sources (Doc_02 SS8)
 "16": "und",  # Mani: multi-lingual corpus known indirectly
 "17": "grc", "18": "grc", "19": "grc",  # Eusebius / Epiphanius / Africanus
 "22": "zxx",  # material evidence: no linguistic content
 "40": "fra",  # Le Boulluec (French original; Eng. trans. noted in the row)
 "42": "und",  # composite: Bar Hebraeus (syr) + Brock encyclopedia entry (eng)
 "43": "grc",  # Theodoret
 "44": "lat",  # Gennadius
 "50": "fra",  # Peeters (French) + Burgess - lead item French
}
SCRIPT_BY_LANG = {"syr": "Syrc", "grc": "Grek", "lat": "Latn", "eng": "Latn",
                  "fra": "Latn", "und": "Zyyy", "zxx": "Zxxx"}

ATTRIB = {  # default genuine; exceptions with Doc_02 warrant
 "9": "dubium",        # Commentary on the Diatessaron: possibly a disciple's compilation (Lange, Doc_02 SS2)
 "12": "pseudonymous", # Odes 'of Solomon'
 "13": "genuine",      # institutional attestation via named sources
 "20": "anonymous",    # Doctrina Addai
 "21": "anonymous",    # Chronicle of Edessa (Doc_02 SS5)
}

LEVEL = {  # default work
 "11": "aggregate-attestation",  # no manuscript survives; triangulated from witnesses
 "13": "aggregate-attestation",  # the qyama institution across Aphrahat Dem. 6 + Ephrem
 "22": "item",                   # the excavated baptistery
 "26": "corpus", "29": "corpus", "37": "corpus", "40": "corpus",
 "41": "corpus", "47": "corpus", "50": "corpus", "51": "aggregate-attestation",
 "42": "aggregate-attestation", "53": "aggregate-attestation",
 "1": "work", "10": "work",
}

GENRE = {  # only where an enum value honestly fits (ALX rule)
 "2": "polemic",       # Contra Haereses
 "7": "polemic",       # Prose Refutations
 "8": "commentary", "9": "commentary",
 "21": "chronicle",
 "23": "monograph", "25": "monograph", "27": "monograph", "28": "monograph",
 "30": "monograph", "31": "monograph", "34": "monograph", "35": "monograph",
 "38": "monograph", "48": "monograph", "52": "monograph",
 "24": "journal-article", "32": "journal-article", "33": "journal-article",
 "36": "journal-article", "49": "journal-article",
 "39": "reference-work", "51": "reference-work", "53": "reference-work",
 "45": "hagiography", "46": "hagiography",
 # 43 (Theodoret HE + Historia Religiosa) deliberately UNSET: the row is a
 # composite of church history and hagiographic lives - no single enum
 # value honestly fits (R catch at S2.1)
 "44": "reference-work",  # De Viris Illustribus supplement
}

NOT_LICENSED = ("EXCLUDED - not licensed for any voice use "
                "({reason}, carried from the registry row verbatim); "
                "retained as a registry row so the boundary decision "
                "stays checkable (Doc_02 SS8).")

ODES_CONTEST = ("Registry boundary_status reads 'Native (Contested)' - "
                "normalized to the schema's Native with the contest "
                "carried here VERBATIM per Doc_02 SS8: 'because Edessene "
                "provenance is only one proposed origin among several "
                "genuinely live scholarly positions, this document does "
                "not assert unqualified Native status. The Registry "
                "records the Odes as Native/Contested rather than "
                "cleanly Native, at Confidence D, with the qualification "
                "carried forward rather than resolved by assertion.' ")

CORE = {
 "id": "syrcore001", "world_id": "syriac-edessa-nisibis",
 "record_type": "world_core", "schema_version": 1, "register": "etic",
 "review_state": "draft", "jobs": [1, 2],
 "time_window": {"start_year": 200, "end_year": 410},
 "horizon": ("Doc_01 SS2 (Round-2 revision, condensed-verbatim): beginning "
             "c. 200 CE - the defensible point for actually attested "
             "community life (a church building attested at Edessa by 201, "
             "destroyed in that year's flood per the Chronicle of Edessa), "
             "with Bardaisan's career (170s-180s onward) the earliest "
             "individually attested activity, addressed as "
             "boundary-adjacent rather than the world's own starting "
             "figure; the Doctrina Addai/Abgar legend is the world's own "
             "foundation myth, not a historical beginning point. End 410 "
             "CE - the Synod of Seleucia-Ctesiphon, the actual "
             "institutional-structural change (metropolitan episcopal "
             "structure under Sasanian recognition); 373 (Ephrem's death) "
             "is a significant internal hinge, NOT the boundary; the 363 "
             "cession of Nisibis and the relocation to Edessa is an "
             "internal transition (same tradition, same personnel, new "
             "political jurisdiction); 424's independence declaration "
             "belongs to the successor world."),
 "formation_logic": ("Doc_01 SS1 (verbatim): \"A hymnic, symbolic, and "
                     "exegetical mode of Christian formation, carried in "
                     "Syriac (a dialect of Aramaic), organized "
                     "institutionally around a pre-monastic covenantal "
                     "ascetic order (the bnay qyama / bnat qyama, "
                     "'sons/daughters of the covenant') rather than around "
                     "emerging monarchical episcopal office as the primary "
                     "formation structure, and oriented scripturally "
                     "around a harmonized single-narrative Gospel text "
                     "(the Diatessaron) rather than the four discrete "
                     "Gospels of Greek-speaking Christianity.\""),
 "gravities": [],
 "sources": [{"source_id": "srcSYR001"}, {"source_id": "srcSYR010"}],
}


def main():
    rows = json.loads(REGISTRY.read_text(encoding="utf-8"))
    assert len(rows) == 53, len(rows)
    n = 0
    for r in rows:
        rid = f"srcSYR{int(r['id']):03d}"
        stype = r["type"]
        default_lang = "syr" if stype in ("P", "M") else "eng"
        lang = LANG.get(r["id"], default_lang)
        boundary = r["boundary_status"]
        contested_note = ""
        if boundary == "Native (Contested)":
            boundary = "Native"
            contested_note = ODES_CONTEST
        licensed = (r.get("licensed_for") or "").strip()
        if not licensed:
            licensed = NOT_LICENSED.format(
                reason=r.get("exclusion_reason") or "excluded")
        rec = {**COMMON,
               "id": rid,
               "jobs": [1, 2],
               "work_title": r["source"],
               "source_type": stype,
               "boundary_status": boundary,
               "attribution_status": ATTRIB.get(r["id"], "genuine"),
               "level_of_description": LEVEL.get(r["id"], "work"),
               "language": lang,
               "script": SCRIPT_BY_LANG[lang],
               "licensed_for": licensed,
               # backfillable channel per the ALX convention: primary/material
               # corpus rows were builder-prior-knowledge at the Doc_02 pass;
               # scholarship rows arrived via the field bibliography
               "discovery_channel": ("builder-prior-knowledge"
                                     if stype in ("P", "M")
                                     else "field-bibliography"),
               "added": r.get("added", "")}
        if GENRE.get(r["id"]):
            rec["genre_form"] = GENRE[r["id"]]
        vnote = (r.get("verification_note") or "").strip()
        if contested_note:
            vnote = (contested_note + vnote).strip()
        if vnote:
            rec["verification_note"] = vnote
        if r.get("exclusion_reason"):
            rec["exclusion_reason"] = r["exclusion_reason"]
        if (r.get("comparandum_note") or "").strip():
            rec["comparandum_note"] = r["comparandum_note"].strip()
        body = (f"Migrated at S6.2/Syriac S2.1-equivalent (2026-07-28) from "
                f"`data/syriac_world/source_registry.json` row id {r['id']} "
                f"(the deployed Source Registry Template data - fields "
                f"verbatim; per-id attribution/level/language/genre "
                f"assignments declared in `wrs/migrate/s62_syr_source_rows.py` "
                f"with Doc_02 warrants). Registry confidence grade: "
                f"{r['confidence']} (verbatim; no schema field - ALX "
                f"precedent keeps grades in the body). Narrative authority: "
                f"`{DOC02}`.")
        emit_record(rec, body, OUT / "source" / f"{rid}.md")
        n += 1
    emit_record(CORE,
                (f"Migrated at S6.2/Syriac S2.1-equivalent (2026-07-28) from "
                 f"`{DOC01}` (SS1 formation logic verbatim; SS2 temporal "
                 f"scope condensed-verbatim incl. the Round-2 410 revision). "
                 f"gravities[] deliberately empty until the S2.5-equivalent "
                 f"authors the gravity records; pairing_guidance/cautions "
                 f"arrive at the S2.7a-equivalent."),
                OUT / "world_core" / "syrcore001.md")
    print(f"wrote {n} source records + syrcore001 -> {OUT}")


if __name__ == "__main__":
    main()
