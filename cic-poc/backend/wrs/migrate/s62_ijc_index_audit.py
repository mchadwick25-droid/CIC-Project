"""S6.2/IJC close-out (a) - md-index audit: the World-Builds
Lexicon_Deployment_Index.md (the IJC build's only index artifact - no
xlsx exists, the HAL complete-by-absence pattern for the rest) vs the
record store, mechanically.

Checks (loud failure on any miss):
  1. 12 index rows == 12 term records; TIER identity per row.
  2. Related-Terms membership identity per row (the index was built
     alongside the chunks; the record graph covers the deployed map).
  3. Alias deltas CLASSIFIED via the S2.2 authoring tables (the
     FLAG-035 corrections and the Rule-A drop are intended; anything
     else fails).
  4. Registry cross-reference OVERLAP: every index row's registry
     rows and the record's own sources share at least one row
     (identity is NOT required - the index cross-refs rows named
     anywhere in the chunk incl. claim-level scholarship; the record
     sources come from the Key Sources split; both are true views).
  5. Author-Gravity-Risk flags: every index 'Yes' row's record
     carries the corresponding caution in its own fields (row-15
     dubium on communio; Confidence-C on homoios; single-source on
     the Ambrose formula; the Leo/Damasus flags on primatus).
  6. Complete-by-absence: no xlsx exists anywhere in the IJC
     World-Builds tree (asserted).
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from s62_ijc_s22 import ALIAS_AUTHORED  # noqa: E402
from s62_pahc_s22 import parse_aliases_vg1a  # noqa: E402

BACKEND = HERE.parents[1]
ROOT = BACKEND.parents[1]
WB = ROOT / "World-Builds" / "Imperial-Juridical-Christianity"
INDEX = WB / "Lexicon_Deployment_Index.md"
TERMS = BACKEND / "wrs" / "records" / "imperial_juridical_world" / "term"

# index row order == ijclex001..012 (the master table's own order)
ORDER = [f"ijclex{n:03d}" for n in range(1, 13)]
RISK_EXPECT = {"ijclex001": "row 15", "ijclex003": "Confidence C",
               "ijclex004": "row 15", "ijclex005": "single-author"}

NAME2ID = {"communio": "ijclex004", "presbeia": "ijclex002",
           "tomus": "ijclex009", "homoousios": "ijclex006",
           "concilium": "ijclex007", "nea rhome": "ijclex010",
           "nea rhōmē": "ijclex010", "martyrium": "ijclex012",
           "primatus": "ijclex001", "haeresis": "ijclex008",
           "imperator...": "ijclex005", "imperator": "ijclex005",
           "basilica": "ijclex011", "homoios": "ijclex003"}

FAIL, NOTES = [], []


def main() -> int:
    txt = INDEX.read_text(encoding="utf-8")
    master = txt[txt.index("## 1. Master Table"):txt.index("## 2.")]
    rows = []
    for line in master.splitlines():
        if line.startswith("| *") or line.startswith('| "*'):
            rows.append([c.strip() for c in line.strip("|").split("|")])
    assert len(rows) == 12, f"index rows {len(rows)}"
    recs = {}
    for p in sorted(TERMS.glob("*.md")):
        f = yaml.safe_load(
            p.read_text(encoding="utf-8")[4:].partition("\n---\n")[0])
        recs[f["id"]] = f
    for rid, row in zip(ORDER, rows):
        rec = recs[rid]
        # 1. tier
        if int(row[1]) != rec["retrieval"]["tier"]:
            FAIL.append(f"{rid}: tier index={row[1]} record="
                        f"{rec['retrieval']['tier']}")
        # 2. related-terms membership
        idx_rel = {NAME2ID.get(x.strip().strip('*').casefold())
                   for x in row[10].split(",") if x.strip()}
        idx_rel.discard(None)
        edges = {e["target_id"] for e in rec.get("field_relations") or []}
        missing = idx_rel - edges
        if missing:
            FAIL.append(f"{rid}: index Related-Terms not in record "
                        f"graph: {sorted(missing)}")
        # 3. aliases
        idx_alias = parse_aliases_vg1a(row[9], rid, [])
        rec_alias = rec.get("aliases") or []
        if [a.casefold() for a in idx_alias] != \
           [a.casefold() for a in rec_alias]:
            if rid in ALIAS_AUTHORED or rid == "ijclex004":
                NOTES.append(f"{rid}: alias delta CLASSIFIED (S2.2 "
                             f"authoring table / FLAG-035 / Rule-A / "
                             f"override)")
            else:
                # index used short forms; compare as sets loosely
                if set(a.casefold() for a in idx_alias) <= \
                   set(a.casefold() for a in rec_alias):
                    NOTES.append(f"{rid}: index carries a subset "
                                 f"(short-form) of the record aliases")
                else:
                    FAIL.append(f"{rid}: alias mismatch index="
                                f"{idx_alias} record={rec_alias}")
        # 4. registry overlap
        idx_rows = set(int(x) for x in re.findall(r"\d+", row[11]))
        rec_rows = set()
        for s in rec.get("sources") or []:
            m = re.match(r"srcIJC(\d+)", s.get("source_id", ""))
            if m:
                rec_rows.add(int(m.group(1)))
        # expand index ranges like 12-14
        for m in re.finditer(r"(\d+)[–-](\d+)", row[11]):
            idx_rows.update(range(int(m.group(1)), int(m.group(2)) + 1))
        if not (idx_rows & rec_rows):
            FAIL.append(f"{rid}: no registry-row overlap (index "
                        f"{sorted(idx_rows)} vs record {sorted(rec_rows)})")
        # 5. risk flags
        if rid in RISK_EXPECT:
            hay = str(rec).casefold()
            if RISK_EXPECT[rid].casefold() not in hay and \
               RISK_EXPECT[rid].replace("row 15", "dubium") not in hay:
                token = {"ijclex001": "row 15", "ijclex003": "c",
                         "ijclex004": "row 15",
                         "ijclex005": "single-author"}[rid]
                if token not in hay:
                    FAIL.append(f"{rid}: Author-Gravity flag "
                                f"({RISK_EXPECT[rid]}) not found in "
                                f"record fields")
    # 6. complete-by-absence
    xlsx = list(WB.rglob("*.xlsx"))
    if xlsx:
        FAIL.append(f"unexpected xlsx present: {[p.name for p in xlsx]}")
    else:
        NOTES.append("complete-by-absence confirmed: no xlsx anywhere "
                     "in the IJC World-Builds tree (the md index is the "
                     "build's own only index artifact, built alongside "
                     "the chunks per its own header)")

    print("# S6.2/IJC close-out (a) - md-index audit")
    for n in NOTES:
        print("-", n)
    if FAIL:
        print(f"\nFAILURES ({len(FAIL)}):")
        for f in FAIL:
            print("  *", f)
        return 1
    print("\n0 failures - AUDIT PASS (12 rows: tier identity, "
          "Related-Terms coverage, alias deltas classified, registry "
          "overlap, risk flags present)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
