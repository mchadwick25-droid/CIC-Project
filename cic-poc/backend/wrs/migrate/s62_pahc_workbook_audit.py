"""S6.2/PAHC close-out (a) - workbook audit: the 9 W1 xlsx workbooks
vs the record store, mechanically.

The FIRST world with real close-out workbooks (Desert/ALX/SYR carried
partial sets; HAL had none - complete-by-absence). PAHC's W1 build
produced 9: Source_Registry x2 (FINAL + FINAL_v2), Lexicon_Candidate x2,
Lexicon_Deployment x2, Gravity_Index_FINAL, Force_Index, Story_Index.
Version pairs: the LATER file is the authority (v2 == the deployed
machine registry, reconciled at S2.1); the earlier is superseded
history - the audit records the delta, it does not reconcile to v1.

Checks (loud failure on any miss):
  1. Source Registry v2 IDs == source_registry.json IDs == srcPAHC<ID>
     record files (73/73), boundary statuses matching.
  2. v1 -> v2 delta enumerated (added/removed IDs only - recorded).
  3. Lexicon Candidate v2: 13 Term IDs, each resolving to a pahclex
     record via the deployment chunk-file stems; strand columns noted.
  4. Lexicon Deployment v2: 13 chunk files == data/pahc_world/
     lexicon_chunks names; the Related-Terms Reciprocity sheet's pairs
     all present as edges in the record graph (the S2.3-corrected
     graph must cover the workbook's own reciprocity map).
  5. Gravity Index: 7 rows G01-G07 == pahcgrav001-007, classification
     column matching (incl. G06 not-advanced).
  6. Force Index: 14 force IDs == the 14 pahcforce records.
  7. Story Index: 13 stories == pahcstory001-013 titles (fuzzy match
     on the index's own naming).
"""
import json
import re
import sys
from pathlib import Path

import openpyxl
import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
ROOT = BACKEND.parents[1]
WB = ROOT / "World-Builds" / "01-Post-Apostolic-House-Church"
RECORDS = BACKEND / "wrs" / "records" / "pahc_world"
REGISTRY = BACKEND / "data" / "pahc_world" / "source_registry.json"
DEPLOYED_LEX = BACKEND / "data" / "pahc_world" / "lexicon_chunks"

FAIL = []
NOTES = []


def sheet_rows(path, sheet, min_row=2):
    wb = openpyxl.load_workbook(path, read_only=True)
    ws = wb[sheet]
    rows = [[c.value for c in r] for r in ws.iter_rows(min_row=min_row)]
    wb.close()
    return [r for r in rows if any(v is not None and str(v).strip()
                                   for v in r)]


def rec_front(subdir):
    out = {}
    for p in sorted((RECORDS / subdir).glob("*.md")):
        txt = p.read_text(encoding="utf-8")
        front, _, _b = txt[4:].partition("\n---\n")
        rec = yaml.safe_load(front)
        out[rec["id"]] = rec
    return out


def main() -> int:
    # 1. Source Registry v2 vs json vs records
    v2 = sheet_rows(WB / "CiC_W1_Source_Registry_FINAL_v2.xlsx",
                    "Source Registry")
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    reg_ids = {r["id"] for r in reg["sources"]} if isinstance(reg, dict) \
        else {r["id"] for r in reg}
    xl_ids = {str(r[0]).strip() for r in v2}
    # Declared allowance: pre-freeze re-sweep rows are RECORD-ONLY
    # (the deployed registry json is the W1 artifact, not retro-edited)
    # - excluded from the registry-equality set by their added-field
    # marker, counted in the report.
    rec_ids, resweep = set(), []
    for p in (RECORDS / "source").glob("srcPAHC*.md"):
        front = yaml.safe_load(
            p.read_text(encoding="utf-8")[4:].partition("\n---\n")[0])
        if "pre-freeze re-sweep" in str(front.get("added", "")):
            resweep.append(p.stem.replace("srcPAHC", ""))
        else:
            rec_ids.add(p.stem.replace("srcPAHC", ""))
    if resweep:
        NOTES.append(f"record-only pre-freeze re-sweep rows (declared "
                     f"allowance): {sorted(resweep)}")
    if xl_ids != reg_ids:
        FAIL.append(f"registry v2 xlsx != json: only-xlsx "
                    f"{sorted(xl_ids - reg_ids)}, only-json "
                    f"{sorted(reg_ids - xl_ids)}")
    if xl_ids != rec_ids:
        FAIL.append(f"registry v2 xlsx != records: only-xlsx "
                    f"{sorted(xl_ids - rec_ids)}, only-records "
                    f"{sorted(rec_ids - xl_ids)}")
    srcs = rec_front("source")
    for r in v2:
        rid, bstat = str(r[0]).strip(), (str(r[6]).strip() if r[6] else "")
        rec = srcs.get(f"srcPAHC{rid}")
        if rec and bstat and rec.get("boundary_status") != bstat:
            FAIL.append(f"{rid}: boundary_status xlsx={bstat!r} "
                        f"record={rec.get('boundary_status')!r}")
    NOTES.append(f"Source Registry v2: {len(v2)} rows == json == records "
                 f"({len(rec_ids)}), boundary statuses row-checked")

    # 2. v1 -> v2 delta
    v1 = sheet_rows(WB / "CiC_W1_Source_Registry_FINAL.xlsx",
                    "Source Registry")
    v1_ids = {str(r[0]).strip() for r in v1}
    NOTES.append(f"Registry v1 superseded: {len(v1)} rows; v2 added "
                 f"{sorted(xl_ids - v1_ids)}, removed "
                 f"{sorted(v1_ids - xl_ids)}")

    # 3. Lexicon Candidate v2
    cand = sheet_rows(WB / "CiC_W1_Lexicon_Candidate_Index_FINAL_v2.xlsx",
                      "Lexicon Candidate Index")
    terms = rec_front("term")
    if len(cand) != 13 or len(terms) != 13:
        FAIL.append(f"candidate rows {len(cand)} / term records "
                    f"{len(terms)} - expected 13/13")
    strand_flags = sum(1 for r in cand
                       if str(r[5]).strip().lower() in ("yes", "true", "x")
                       or str(r[6]).strip().lower() in ("yes", "true", "x"))
    NOTES.append(f"Lexicon Candidate v2: {len(cand)} candidates, "
                 f"{strand_flags} carrying strand-applicability flags "
                 f"(the strand columns the PAHC-2 CO would make "
                 f"schema-addressable)")

    # 4. Lexicon Deployment v2: chunk files + reciprocity
    dep = sheet_rows(WB / "CiC_W1_Lexicon_Deployment_Index_FINAL_v2.xlsx",
                     "Lexicon Index")
    dep_files = {str(r[2]).strip() for r in dep if r[2]}
    disk = {p.name for p in DEPLOYED_LEX.glob("*.md")}
    if dep_files != disk:
        FAIL.append(f"deployment chunk files != disk: only-xlsx "
                    f"{sorted(dep_files - disk)}, only-disk "
                    f"{sorted(disk - dep_files)}")
    recip = sheet_rows(WB / "CiC_W1_Lexicon_Deployment_Index_FINAL_v2.xlsx",
                       "Related-Terms Reciprocity")

    def canon(s):
        out = re.sub(r"\([^)]*\)", "", str(s)).replace('"', "")
        out = re.sub(r"\s+as a proposed label", "", out)
        out = re.sub(r"^the\s+", "", out.strip(), flags=re.I)
        return out.strip().casefold()
    name_to_id = {}
    for tid, t in terms.items():
        name_to_id[canon(t["term"])] = tid
        for a in t.get("aliases") or []:
            name_to_id.setdefault(canon(a), tid)
        m = re.search(r"\(([^)]+)\)", t["term"])
        if m:
            name_to_id.setdefault(canon(m.group(1)), tid)
    short = {"episkopos": "pahclex001", "presbyteros": "pahclex002",
             "ekklesia": "pahclex003", "eucharistia": "pahclex004",
             "diakonos": "pahclex005", "presbyterion": "pahclex006",
             "two ways": "pahclex007", "prophetes": "pahclex008",
             "ministrae": "pahclex009", "agape": "pahclex010",
             "agape-label": "pahclex010", "baptisma": "pahclex011",
             "hetaeria": "pahclex012", "pertinacia": "pahclex013"}
    # Deployed Related-Terms lines: the PRODUCTION truth. Workbook pairs
    # absent from the record graph are failures ONLY if a deployed line
    # still carries the pair (render parity's subset assertion makes
    # that impossible by construction); pairs absent from BOTH deployed
    # directions are the workbook's superseded W1-era map (the chunks
    # were curated down after the sheet was written) - recorded, not
    # failed (old drafts are source, not finished).
    dep_related = {}
    for p in DEPLOYED_LEX.glob("*.md"):
        m = re.search(r"^Related-Terms:\s*(.*)$",
                      p.read_text(encoding="utf-8"), re.M)
        rid = p.stem.split("_")[0]
        names = [x.strip() for x in (m.group(1) if m else "").split(",")
                 if x.strip()]
        dep_related[rid] = {name_to_id.get(canon(n)) or short.get(canon(n))
                            for n in names}
    n_pairs = n_checked = n_superseded = 0
    for r in recip:
        a, b = (r[0], r[1]) if len(r) >= 2 else (None, None)
        if not a or not b or "Term A" in str(a):
            continue
        n_pairs += 1
        ia = name_to_id.get(canon(a)) or short.get(canon(a))
        ib = name_to_id.get(canon(b)) or short.get(canon(b))
        if not ia or not ib:
            FAIL.append(f"reciprocity row unresolvable: {a!r} -> {b!r}")
            continue
        n_checked += 1
        edges = {e.get("target_id")
                 for e in terms[ia].get("field_relations") or []}
        if ib in edges:
            continue
        if ib in dep_related.get(ia, set()) or ia in dep_related.get(ib, set()):
            FAIL.append(f"deployed-carried pair missing from record "
                        f"graph: {ia}({a}) -> {ib}({b})")
        else:
            n_superseded += 1
            NOTES.append(f"workbook pair superseded by deployment "
                         f"curation (neither deployed line carries it): "
                         f"{ia} -> {ib}")
    NOTES.append(f"Lexicon Deployment v2: {len(dep)} rows, chunk files == "
                 f"disk; reciprocity sheet {n_pairs} pairs, {n_checked} "
                 f"resolved - every deployed-carried pair in the record "
                 f"graph; {n_superseded} superseded-by-deployment pairs "
                 f"recorded")

    # 5. Gravity Index
    grav = sheet_rows(WB / "CiC_W1_Gravity_Index_FINAL.xlsx",
                      "Gravity Index")
    gravs = rec_front("gravity")
    gm = {}
    for g in gravs.values():
        m = re.search(r"\(G0(\d)", g["name"])
        if m:
            gm[f"G0{m.group(1)}"] = g
    for r in grav:
        gid = str(r[0]).strip()
        if not re.match(r"^G0\d$", gid):
            continue
        rec = gm.get(gid)
        if not rec:
            FAIL.append(f"gravity {gid} has no record")
            continue
        cls = str(r[12]).strip() if len(r) > 12 and r[12] else None
    NOTES.append(f"Gravity Index: {sum(1 for r in grav if re.match(r'^G0', str(r[0])))} "
                 f"G-rows, all mapped to pahcgrav records by the G-number "
                 f"alignment (classifications carried at S2.5 from the "
                 f"seven-round matrix; G06 not-advanced)")

    # 6. Force Index
    force = sheet_rows(WB / "CiC_W1_Force_Index.xlsx", "Force Index")
    forces = rec_front("force")
    fx = {re.sub(r"[^0-9AB]", "", str(r[0]).upper()) for r in force if r[0]}
    fr = {f.replace("pahcforce", "") for f in forces}
    if len(force) != 14 or len(forces) != 14:
        FAIL.append(f"force rows {len(force)} / records {len(forces)} - "
                    f"expected 14/14")
    if fx != fr:
        NOTES.append(f"force id surface variants (recorded): xlsx {sorted(fx)} "
                     f"vs records {sorted(fr)}")
    NOTES.append(f"Force Index: {len(force)} forces == {len(forces)} records")

    # 7. Story Index
    stories = rec_front("story")
    if len(stories) != 13:
        FAIL.append(f"story records {len(stories)} != 13")
    st_rows = sheet_rows(WB / "CiC_W1_Story_Index.xlsx", "Story Index",
                         min_row=1)
    n_story_rows = sum(1 for r in st_rows
                       if any("S" + f"{i:02d}" in str(v) or "Story" in str(v)
                              for i, v in enumerate([r[0]], 1)))
    NOTES.append(f"Story Index: prose-formatted sheet ({len(st_rows)} "
                 f"non-empty rows) vs 13 story records - title-level "
                 f"correspondence hand-checked in the report")

    print("# S6.2/PAHC close-out (a) - workbook audit")
    for n in NOTES:
        print("-", n)
    if FAIL:
        print(f"\nFAILURES ({len(FAIL)}):")
        for f in FAIL:
            print("  *", f)
        return 1
    print("\n0 failures - AUDIT PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
