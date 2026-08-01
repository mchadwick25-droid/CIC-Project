"""S6.2/IJC - S2.1-equivalent: source rows + ijccore001, MECHANICALLY
from the World-Builds MARKDOWN registry (the fleet's third registry
format: PAHC json / earlier-worlds Doc_02 prose / IJC md table).

Authority: World-Builds/Imperial-Juridical-Christianity/
Source_Registry.md - append-only, Round-2 CLEARED co-equal Step-2
output (reviewed and disposed WITH Doc_02), carrying its own DISCLOSED
confidence recalibration (first draft over-assigned A; A = actually
consulted this session, trained-knowledge rows are B or lower). All
assessment prose is carried VERBATIM, never re-derived.

Declared mappings (each a judgment this docstring owns):
- id: srcIJC01..srcIJC38 - two-digit, preserving the registry's own
  "row 24"-style citation currency.
- source_type enum P/S/M: row 14's registry hybrid "P/M" -> P with the
  hybrid marking carried verbatim in the note; row 22's
  "P (hagiographic)" -> P with the qualifier carried.
- Confidence LETTERS (A/B/C/D) carried verbatim in verification_note
  ("Registry-carried assessment fields, verbatim: confidence=B; ...");
  Excluded rows have none ("-").
- boundary_status Native/Excluded verbatim; rows 24-26 keep the
  registry's own exclusion_reason ("Named Comparandum").
- level_of_description: corpus for 14/24/25/26 (corpus-level rows);
  aggregate-attestation for 15 (decretal material, various) and 36
  (coinage category); item for 37/38 (single built structures); work
  otherwise.
- attribution_status: dubium for row 15 (the registry's own
  "contested authenticity"); genuine otherwise (row 23's FRAGMENTARY
  PRESERVATION is a survival fact, not an attribution doubt).
- discovery_channel: step0-seed-list for 27/28/29 (their own
  Verification Notes name the Step 0 source-matrix);
  builder-prior-knowledge otherwise (the standing backfill rule -
  original discovery unrecoverable by design).
- work_author: split at the first ", " where the prefix reads as a
  personal name (letters/periods/spaces, <45 chars); otherwise the
  FULL citation stays in work_title. script/work_locus are OMITTED -
  the registry carries no such columns (the loci ride inside the
  verbatim titles).
- language: the completion gate REQUIRES it and the registry has no
  column - filled per row from the works' own well-established
  languages (a migrator judgment, owned here, not registry-carried):
  grc for the Greek historians/canons/corpora, la for the Latin
  fathers/Code/inscriptions, en for modern scholarship EXCEPT row 31
  (Pietri, Roma Christiana - French, fr), zxx (ISO: no linguistic
  content) for the three material rows 36-38.
- Comparandum Note (col 9) appended verbatim to verification_note
  where present.

ijccore001: Doc_01's own content - time_window 312-451 with SS2's own
two-ground defense carried; horizon = the three sees + both
linguistic halves; formation_logic = SS3's own "ecology of office and
jurisdiction" phrase; THE STRAND-TRIPLE (first in fleet; Doc_01 SS4's
corrected three-strand finding) rides the BODY per the PAHC
precedent - the strands schema CO (PAHC-2) now has two data points.
Living Tradition Status: Doc_01 SS1's own "Not confirmed" (Article
29) - the freeze declaration must carry it for Mark, the PAHC
pattern. gravities[] empty until S2.5.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
ROOT = BACKEND.parents[1]
REGISTRY = (ROOT / "World-Builds" / "Imperial-Juridical-Christianity"
            / "Source_Registry.md")
OUT = BACKEND / "wrs" / "records" / "imperial_juridical_world"
WID = "imperial-juridical-christianity"
VDATE = "2026-07-31"

CORPUS_ROWS = {14, 24, 25, 26}
AGGREGATE_ROWS = {15, 36}
ITEM_ROWS = {37, 38}
DUBIUM_ROWS = {15}
STEP0_ROWS = {27, 28, 29}

LANGS = {1: "grc", 2: "grc", 3: "la", 4: "grc", 5: "la", 6: "la",
         7: "la", 8: "la", 9: "grc", 10: "grc", 11: "grc", 12: "la",
         13: "la", 14: "la", 15: "la", 16: "la", 17: "la", 18: "grc",
         19: "grc", 20: "grc", 21: "la", 22: "la", 23: "la", 24: "grc",
         25: "grc", 26: "la", 27: "en", 28: "en", 29: "en", 30: "en",
         31: "fr", 32: "en", 33: "en", 34: "en", 35: "en", 36: "zxx",
         37: "zxx", 38: "zxx"}

NAME_RE = re.compile(r"^[A-Z][A-Za-z.\-' ]{2,44}$")


def parse_rows():
    rows = []
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        if line.startswith("## Notes"):
            break
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 10 or not cells[0].isdigit():
            continue
        rows.append(cells)
    return rows


def main():
    rows = parse_rows()
    assert len(rows) == 38, f"expected 38 registry rows, parsed {len(rows)}"
    n = 0
    for cells in rows:
        num = int(cells[0])
        source, stype_raw, conf, bstat = cells[1], cells[2], cells[3], cells[4]
        excl, licensed, vnote, comparandum = (cells[5], cells[6], cells[7],
                                              cells[8])
        rid = f"srcIJC{num:02d}"
        stype = stype_raw.split("/")[0].split(" ")[0].strip()
        assert stype in ("P", "S", "M"), (num, stype_raw)
        level = ("corpus" if num in CORPUS_ROWS
                 else "aggregate-attestation" if num in AGGREGATE_ROWS
                 else "item" if num in ITEM_ROWS else "work")
        note_parts = [f"Registry-carried assessment fields, verbatim: "
                      f"type={stype_raw}; confidence={conf}; "
                      f"boundary={bstat}"]
        if vnote and vnote != "—":
            note_parts.append(f"Verification Note: {vnote}")
        if comparandum and comparandum != "—":
            note_parts.append(f"Comparandum Note: {comparandum}")
        rec = {
            "id": rid, "world_id": WID, "record_type": "source",
            "schema_version": 1, "register": "etic",
            "review_state": "draft", "disposition": "in-use",
            "source_type": stype, "boundary_status": bstat,
            "attribution_status": ("dubium" if num in DUBIUM_ROWS
                                   else "genuine"),
            "level_of_description": level,
            "work_title": source,
            "language": LANGS[num],
            "licensed_for": (licensed if licensed and licensed != "—"
                             else "(Excluded row - no license; see "
                                  "exclusion reason)"),
            "verification_note": ". ".join(note_parts),
            "discovery_channel": ("step0-seed-list" if num in STEP0_ROWS
                                  else "builder-prior-knowledge"),
            "added": f"{VDATE} (S6.2/IJC S2.1, mechanical from "
                     f"Source_Registry.md row {num})",
            "jobs": [1, 2],
        }
        m = re.match(r"^([^,*]+), ", source)
        if m and NAME_RE.match(m.group(1).strip()) and stype in ("P", "S"):
            rec["work_author"] = m.group(1).strip()
        if bstat == "Excluded" and excl and excl != "—":
            rec["exclusion_reason"] = excl
        emit_record(
            rec,
            ("Migrated at the S6.2/IJC S2.1-equivalent (2026-07-31), "
             "MECHANICALLY from World-Builds/Imperial-Juridical-"
             "Christianity/Source_Registry.md (the md-table registry - "
             "append-only, Round-2 CLEARED with Doc_02 as co-equal Step-2 "
             "outputs; its disclosed confidence recalibration carried "
             "verbatim). Original discovery unrecoverable by design "
             "(backfill rule); mapping judgments in "
             "wrs/migrate/s62_ijc_s21.py's docstring."),
            OUT / "source" / f"{rid}.md")
        n += 1

    core = {
        "id": "ijccore001", "world_id": WID, "record_type": "world_core",
        "schema_version": 1, "jobs": [1, 2, 4], "register": "etic",
        "review_state": "draft",
        "time_window": {
            "start_year": 312, "end_year": 451,
            "note": ("Doc_01 SS2's own two-ground defense carried whole: "
                     "312 = the Battle of the Milvian Bridge and the "
                     "alliance formalized in the Edict of Milan (313) - "
                     "'the event that first makes ecclesiastical office a "
                     "form of state-adjacent power at all.' 451 = the "
                     "Council of Chalcedon, defended on two independent "
                     "grounds beyond Leo's own closing role: the last of "
                     "the window's ecumenical councils, and the "
                     "Canon-28-vs-Leo collision that leaves the world's "
                     "central question - whose word finally binds - "
                     "STANDING OPEN at the close (the world ends inside "
                     "its own unresolved argument, like PAHC's).")},
        "horizon": ("Rome, Constantinople, Milan - the three sees whose "
                    "office-holders answer one another across BOTH "
                    "linguistic halves of the empire (Latin Rome/Milan, "
                    "Greek Constantinople - distinctive in the "
                    "portfolio); late Roman and early Byzantine imperial "
                    "elite culture; the empire's own fragmentation after "
                    "395 and the Homoian imperial-establishment decades "
                    "(Constantius II, Valens) inside the window (Doc_01 "
                    "SS2)."),
        "formation_logic": ("Doc_01 SS3's own phrase: 'an ecology of "
                            "office and jurisdiction' - bishops and "
                            "emperors repeatedly negotiating, asserting, "
                            "and contesting where final authority over "
                            "doctrine and discipline resides; canon law, "
                            "conciliar process, decretal and tome as the "
                            "formation instruments; authority dominant "
                            "among the five patterns, the other four "
                            "'present but structurally secondary' - a "
                            "world of office-holders, not congregants, "
                            "thinner on the uncredentialed believer's own "
                            "experience by its own admission (SS1)."),
        "gravities": [],
        "sources": [{"source_id": "srcIJC01"}, {"source_id": "srcIJC09"},
                    {"source_id": "srcIJC11"}, {"source_id": "srcIJC12"},
                    {"source_id": "srcIJC07"}],
    }
    core_body = (
        "Migrated at the S6.2/IJC S2.1-equivalent (2026-07-31) from "
        "Doc_01_World_Identification_Boundaries_Orientation.md (SS1-SS4) "
        "- Round-2 cleared (COSMETIC ONLY; Open_Gaps item 2). "
        "gravities[] deliberately empty until S2.5; "
        "pairing_guidance/cautions/telos/living_traditions arrive at "
        "S2.7a.\n\n"
        "THE STRAND-TRIPLE (Doc_01 SS4's corrected finding - the FIRST "
        "three-strand world in the fleet; rides this body per the PAHC "
        "precedent until the strands schema CO (PAHC-2, now two data "
        "points) lands. Article 21: strand is 'a finding, never a "
        "presupposed universal schema'):\n"
        "- STRAND A - Roman/Apostolic-Primacy: authority grounded in "
        "claimed apostolic succession from Peter, exercised through "
        "office, decretal, and canon law, independent of political "
        "proximity to the emperor. Damasus through Leo I.\n"
        "- STRAND B - Constantinopolitan/Imperial-Proximity: authority "
        "grounded in a see's political proximity to imperial power, not "
        "apostolic succession; seeded in Eusebius's court theology, "
        "evidenced in Canon 3 (381) and Canon 28 (451) and Leo's "
        "rejection of the latter.\n"
        "- STRAND C - Ambrosian/Sacramental-Independence: authority "
        "grounded in a bishop's sacramental and moral leverage over any "
        "ruler, regardless of his see's rank or pedigree; evidenced in "
        "Ambrose's confrontations with Theodosius and the Homoian "
        "court; does NOT persist as an independent claim-making stream "
        "to 451, carries real distinct forward legacy (Doc_01 SS4's own "
        "qualification, kept).\n"
        "All three share the common root in the initiating Constantinian "
        "alliance. Cross-strand gravity testing is S2.5's work per the "
        "Framework.\n\n"
        "LIVING TRADITION STATUS (Doc_01 SS1's own words): 'Not "
        "confirmed' - per Constitution Article 29 and the project's "
        "established practice; the freeze declaration must carry the "
        "determination for Mark (the PAHC pattern; note this world's "
        "determination is the portfolio's most charged - the "
        "Roman-primacy and Constantinopolitan claim-lines have direct "
        "present-day institutional claimants).")
    emit_record(core, core_body, OUT / "world_core" / "ijccore001.md")
    print(f"{n} source rows + ijccore001 -> {OUT}")


if __name__ == "__main__":
    main()
