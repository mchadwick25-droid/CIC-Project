"""S6.2/IJC - S2.5-equivalent: 7 gravity records + 10 force records
parsed from Doc_04/Doc_08's OWN text, + the CO-P2-04 FEC->gravity_links
conversion on the 6 stories.

GRAVITIES (Doc_04 SS3/SS4, verbatim-carried):
  ijcgrav001-006 = Candidates 1-6 (G-number aligned): Juridical
  Primacy-Claiming (Primary), Church-State Alliance and Its Limits
  (Primary), Orthodoxy-Enforcement Through Imperial Power (Primary,
  divergence carried forward to Doc_05/Doc_08 per the table's own
  note), Episcopal Independence from Imperial Command (Supporting,
  Strand-C-bound), Doctrinal/Christological Precision-Seeking
  (Supporting - CORRECTED from the first draft's wrongful
  disqualification, Doc_04's own disclosed Open-Item-3 correction
  carried), Sacramental/Moral vs Institutional/Positional Authority
  (Tensional). ijcgrav007 = the SS2 not-advanced candidate
  (institutional self-documentation - fails Dependency at generation;
  folded into Candidate 1's evidence base; recorded not-advanced per
  the PAHC G06 precedent, WITH Doc_04's own SS7.4 process finding
  that the 'did-not-reach-gravity-status' label lives only in the L4
  Template, not the Framework body).

FORCES (Doc_08 SS3, mechanically parsed): 10 forces across the
six-cell matrix; the three layers verbatim; layer4 = stasis:true
EXCEPT where Doc_08's own Section 4 states a later reshaping of that
force (1A-1 via Connection 3 - Western fragmentation reshapes the
alliance's later meaning for Strand A; 3B-2 as 2B-2's own mechanism
operating at the window's close). Connections = Section 4's six,
typed in the doc's own words (the schema's own
per-world-Doc_08-practice rule).

FEC CONVERSION (CO-P2-04): story FECs name their gravities -
001->grav002, 002->grav002 (the alliance's unsettled founding pair),
004->grav004 (worship as the lived mechanism of resistance),
005->grav001, 006->grav001. ijcstory003 (the bees) is
UNLINKED-BY-ITS-OWN-FEC (the PAHC 009/013 precedent): its FEC
grounds the story in memory-practice and Doc_05's thin human
ecology, naming no candidate gravity - asserted at run.
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
ROOT = BACKEND.parents[1]
WB = ROOT / "World-Builds" / "Imperial-Juridical-Christianity"
DOC04 = WB / "Doc_04_Gravity_Discovery.md"
DOC08 = WB / "Doc_08_Forces_Document.md"
OUT = BACKEND / "wrs" / "records" / "imperial_juridical_world"
WID = "imperial-juridical-christianity"

CLASSIFICATION = {1: "Primary", 2: "Primary", 3: "Primary",
                  4: "Supporting", 5: "Supporting", 6: "Tensional"}

TEST_KEYS = ["Repetition", "Dependency", "Formation", "Explanatory",
             "Persistence", "Interaction"]


# Doc_04 SS6 Interaction Matrix, each cell's own words (upper triangle
# + asymmetric pairs both stated where the matrix states them)
INTERACTIONS = {
 1: [("reinforcing", 2, "SS6: 2 is 1's own precondition."),
     ("reinforcing", 3, "SS6: Leo's Tome is both a primacy act and a doctrinal one."),
     ("reinforcing", 4, "SS6 asymmetric (DIRECTION: 4 reinforces 1, the enum symmetrizes, the note keeps it): 4's already-past legacy feeds 1's later confidence (Doc_01 SS4); no comparable relationship runs back."),
     ("reinforcing", 5, "SS6 (direction: 5 reinforces 1): precision-seeking reinforces the claims it serves."),
     ("competing", 6, "SS6: the tension competes with positional authority's claim to settle it.")],
 2: [("reinforcing", 1, "SS6 mirror."),
     ("reinforcing", 3, "SS6: 3 is a recurring specific use of 2."),
     ("reshaping", 4, "SS6 (direction: 4 reshapes 2): 4 demonstrates 2's real limits.")],
 3: [("reinforcing", 1, "SS6 mirror."),
     ("reinforcing", 2, "SS6 mirror."),
     ("reshaping", 4, "SS6 (direction: 4 reshapes 3; corrected from the first draft's 'reinforcing'): 4 shows the mechanism is not the only route to the outcome."),
     ("reinforcing", 5, "SS6 (direction: 5 reinforces 1): precision-seeking feeds enforcement's content.")],
 4: [("reinforcing", 1, "SS6 asymmetric (direction: 4 reinforces 1; corrected from 'reshapes'): the legacy feeds 1's confidence."),
     ("reshaping", 2, "SS6 mirror."),
     ("reshaping", 3, "SS6 mirror (corrected)."),
     ("reinforcing", 6, "SS6: 4 is 6's own clearest instance.")],
 5: [("reinforcing", 1, "SS6 mirror."),
     ("reinforcing", 3, "SS6 mirror.")],
 6: [("competing", 1, "SS6 mirror."),
     ("reinforcing", 4, "SS6 mirror.")],
}

FEC_MAP = {"ijcstory001": ["ijcgrav002"], "ijcstory002": ["ijcgrav002"],
           "ijcstory004": ["ijcgrav004"], "ijcstory005": ["ijcgrav001"],
           "ijcstory006": ["ijcgrav001"]}

CONNECTIONS = {
    "ijcforce1A1": [("enables-formatively", "ijcforce1B1",
                     "Doc_08 SS4 Connection 1: the alliance is only "
                     "formative because a functioning church already "
                     "existed to receive it.")],
    "ijcforce2A1": [("intensifying", "ijcforce2B1",
                     "Doc_08 SS4 Connection 2: policy oscillation "
                     "intensifies the internal authority contest."),
                    ("producing", "ijcforce3B1",
                     "Doc_08 SS4 Connection 4: the imperial-proximity "
                     "logic 2A-1 keeps alive produces, via the Strand "
                     "Determination, the Canon-28 collision.")],
    "ijcforce2A2": [("reshaping", "ijcforce1A1",
                     "Doc_08 SS4 Connection 3: Western fragmentation "
                     "reshapes the alliance's own later meaning for "
                     "Strand A specifically.")],
    "ijcforce3A1": [("reactive", "ijcforce3B1",
                     "Doc_08 SS4 Connection 5: Leo's rejection reacts "
                     "to Chalcedon's failed consensus.")],
    "ijcforce2B2": [("same-mechanism-later", "ijcforce3B2",
                     "Doc_08 SS4 Connection 6: the transmission "
                     "mechanism at two points in the window - 3B-2 is "
                     "2B-2's own mechanism at the close.")],
    # receiving-side back-edges (the linkage-reciprocity gate's rule;
    # each names its Connection)
    "ijcforce1B1": [("receives", "ijcforce1A1",
                     "Back-edge of SS4 Connection 1.")],
    "ijcforce2B1": [("receives", "ijcforce2A1",
                     "Back-edge of SS4 Connection 2.")],
    "ijcforce3B1": [("receives", "ijcforce2A1",
                     "Back-edge of SS4 Connection 4."),
                    ("receives", "ijcforce3A1",
                     "Back-edge of SS4 Connection 5.")],
    "ijcforce3B2": [("receives", "ijcforce2B2",
                     "Back-edge of SS4 Connection 6.")],
}
CONNECTIONS["ijcforce1A1"].append(
    ("receives", "ijcforce2A2", "Back-edge of SS4 Connection 3."))

LAYER4 = {
    "ijcforce1A1": {"elaboration": (
        "Doc_08 SS4 Connection 3's own reshaping: as Western imperial "
        "authority collapses (2A-2), the alliance this force founded "
        "changes meaning for Strand A - the emperor Rome allied with "
        "is decreasingly the power actually present in Rome, which is "
        "part of why the see's own claim migrates from "
        "imperial-adjacency toward apostolic inheritance.")},
    "ijcforce3B2": {"elaboration": (
        "Doc_08 SS4 Connection 6: not a new mechanism but 2B-2's own "
        "archival-selection mechanism operating at the window's close "
        "- the 451 schism's selection effect on what survives is the "
        "ongoing transmission force in its ending form.")},
}


def parse_doc04():
    txt = DOC04.read_text(encoding="utf-8")
    gravities = []
    blocks = re.split(r"^### Candidate ", txt, flags=re.M)[1:]
    for b in blocks:
        m = re.match(r"(\d+)(?: \[Tensional\])? — (.+?)$", b, re.M)
        num, name = int(m.group(1)), m.group(2).strip()
        tests = {}
        for key in TEST_KEYS:
            tm = re.search(rf"\*\*{key}[^:]*:\*\* (.*?)(?=\n- \*\*|\n\n\*\*Provisional|\Z)",
                           b, re.S)
            tests[key.lower()] = {"verdict": " ".join(
                (tm.group(1) if tm else "").split())[:900] + f" (Doc_04 Candidate {num})"}
        cc = re.search(r"\*\*Confidence/Gravity Cross-Check:\*\* (.*?)(?=\n- \*\*|\n\n\*\*Provisional|\Z)",
                       b, re.S)
        fc = re.search(r"\*\*Forces-connection notation[^:]*:\*\* (.*?)(?=\n- \*\*|\n\n\*\*Provisional|\Z)",
                       b, re.S)
        rows = re.search(r"\*Generated from:\* (.*?)$", b, re.M)
        row_nums = [int(x) for x in
                    re.findall(r"\b(\d+)\b", rows.group(1) if rows else "")
                    if 1 <= int(x) <= 38]
        gravities.append({
            "num": num, "name": name,
            "classification": CLASSIFICATION[num],
            "six_tests": tests,
            "confidence_crosscheck": " ".join(
                (cc.group(1) if cc else "").split())[:900],
            "interaction": " ".join(
                (fc.group(1) if fc else "").split())[:900],
            "sources": sorted({f"srcIJC{n:02d}" for n in row_nums}),
        })
    return gravities


def parse_doc08():
    txt = DOC08.read_text(encoding="utf-8")
    forces = []
    cell = None
    for m in re.finditer(
            r"^### (CELL [123][AB]) — (.+?)$|^#### Force ([123][AB]-\d): (.+?)$",
            txt, re.M):
        if m.group(1):
            cell = (m.group(1), m.group(2).strip())
            continue
        code, name = m.group(3), m.group(4).strip()
        start = m.end()
        nxt = re.search(r"^### |^#### |^## ", txt[start:], re.M)
        block = txt[start:start + nxt.start()] if nxt else txt[start:]
        layers = {}
        for lnum, key in ((1, "layer_historical_event"),
                          (2, "layer_worlds_own_experience"),
                          (3, "layer_formation_impact")):
            lm = re.search(rf"\*\*Layer {lnum}[^:]*:\*\* (.*?)(?=\n\n\*\*Layer|\n\n###|\Z)",
                           block, re.S)
            layers[key] = " ".join((lm.group(1) if lm else "").split())
        fid = "ijcforce" + code.replace("-", "")
        forces.append({"id": fid, "code": code, "name": name,
                       "cell": f"{cell[0][5:]} - {cell[1]}",
                       **layers})
    return forces


def read_record(path):
    txt = path.read_text(encoding="utf-8")
    front, _, body = txt[4:].partition("\n---\n")
    return yaml.safe_load(front), body


def write_record(path, front, body):
    fy = yaml.safe_dump(front, sort_keys=False, allow_unicode=True,
                        width=100)
    path.write_text(f"---\n{fy}---\n{body}", encoding="utf-8",
                    newline="\n")


def main():
    gravities = parse_doc04()
    assert len(gravities) == 6, len(gravities)
    for g in gravities:
        rid = f"ijcgrav{g['num']:03d}"
        rec = {"id": rid, "world_id": WID, "record_type": "gravity",
               "schema_version": 1, "jobs": [1, 2, 4], "register": "etic",
               "review_state": "draft",
               "name": f"{g['name']} (G{g['num']:02d})",
               "classification": g["classification"],
               "six_tests": g["six_tests"],
               "confidence_crosscheck": (
                   g["confidence_crosscheck"]
                   + " | Forces-connection notation (Doc_04, verbatim): "
                   + g["interaction"]),
               "interaction": [
                   {"type": ty, "target_id": f"ijcgrav{tn:03d}",
                    "note": note}
                   for ty, tn, note in INTERACTIONS[g["num"]]],
               "sources": [{"source_id": s} for s in g["sources"]]}
        emit_record(rec, ("Migrated at the S6.2/IJC S2.5-equivalent "
                          "(2026-07-31) from Doc_04_Gravity_Discovery.md "
                          "SS3/SS4 verbatim (Round-2 cleared; the "
                          "disclosed Open-Item corrections carried, "
                          "incl. Candidate 5's reinstatement and "
                          "Candidate 3's Strand-C retraction)."),
                    OUT / "gravity" / f"{rid}.md")
    # the SS2 not-advanced candidate (the PAHC G06 precedent)
    na = {"id": "ijcgrav007", "world_id": WID, "record_type": "gravity",
          "schema_version": 1, "jobs": [1, 2, 4], "register": "etic",
          "review_state": "draft",
          "name": ("Institutional self-documentation / juridical "
                   "record-keeping (G07 - did not advance)"),
          "classification": "not-advanced",
          "six_tests": {k.lower(): {"verdict": (
              "NOT ADVANCED to full six-test treatment (Doc_04 SS2): "
              "fails the Dependency Test at generation - documentary "
              "production is the INSTRUMENT of Candidates 1 and 3, "
              "never depended on for its own sake; advancing it would "
              "double-count one organizing force under two names.")}
              for k in TEST_KEYS},
          "confidence_crosscheck": (
              "Doc_04 SS2's own reasoning verbatim-adjacent; note the "
              "SS7.4 process finding - the 'did-not-reach-gravity-"
              "status' label exists only in the L4 Template, not the "
              "Framework body (reported to System Hub). Folded into "
              "Candidate 1's own evidence base (Doc_04 SS2)."),
          "interaction": [],
          "sources": [{"source_id": f"srcIJC{n:02d}"}
                      for n in range(9, 17)]}
    emit_record(na, ("Migrated at the S6.2/IJC S2.5-equivalent "
                     "(2026-07-31) from Doc_04 SS2."),
                OUT / "gravity" / "ijcgrav007.md")

    forces = parse_doc08()
    assert len(forces) == 10, len(forces)
    for f in forces:
        conns = [{"type": t, "target_id": tid, "note": note}
                 for t, tid, note in CONNECTIONS.get(f["id"], [])]
        rec = {"id": f["id"], "world_id": WID, "record_type": "force",
               "schema_version": 1, "jobs": [1, 2, 4], "register": "etic",
               "review_state": "draft",
               "name": f"{f['name']} ({f['code']})",
               "six_cell_position": f["cell"],
               "layer_historical_event": f["layer_historical_event"],
               "layer_worlds_own_experience":
                   f["layer_worlds_own_experience"],
               "layer_formation_impact": f["layer_formation_impact"],
               "layer4": LAYER4.get(f["id"], {"stasis": True}),
               "connections": conns,
               "sources": []}
        emit_record(rec, ("Migrated at the S6.2/IJC S2.5-equivalent "
                          "(2026-07-31) from Doc_08_Forces_Document.md "
                          "SS3 (layers verbatim) + SS4 (connections in "
                          "the doc's own words); layer4 rule in "
                          "wrs/migrate/s62_ijc_s25.py's docstring."),
                    OUT / "force" / f"{f['id']}.md")

    # CO-P2-04: FEC -> gravity_links
    FEC_RE = re.compile(
        r"\[Formation Ecology Connection[^\]]*\]\s*(.*?)(?=\n\n\[|\Z)",
        re.S)
    n_links = 0
    for sp in sorted((OUT / "story").glob("*.md")):
        front, body = read_record(sp)
        m = FEC_RE.search(body)
        fec = " ".join((m.group(1) if m else "").split())
        rid = front["id"]
        gids = FEC_MAP.get(rid, [])
        if not gids:
            assert "Candidate" not in fec.split("Doc_05")[0], (
                rid, "FEC names a candidate but is unmapped")
            continue
        front["gravity_links"] = [
            {"gravity_id": g,
             "note": ("CO-P2-04: the chunk's Formation Ecology "
                      "Connection, verbatim (the S2.4 parking, "
                      "converted at S2.5): " + fec)}
            for g in gids]
        n_links += len(gids)
        write_record(sp, front, body)
    print(f"7 gravities + 10 forces + {n_links} FEC->gravity_links "
          f"(ijcstory003 unlinked by its own FEC, asserted)")


if __name__ == "__main__":
    main()
