"""CO-P2-13 (Mark, 2026-07-28) - the 37 untyped mutual pairs typed as
symmetric `associated-with` edges, mechanically from the chunks' own data.

Source of truth: each term record body's Related-Terms Reciprocity Note
parking (verbatim from the chunk) - specifically its **Mutual** list
("each lists this term back"). The emission is MECHANICAL by design:
option 1 of the S2.3 close-out's three routes, decided by Mark - the
association is exactly what the chunks attest (mutual cross-reference, no
claimed direction or hierarchy), so no authoring judgment is smuggled in.

Rules:
- a pair is emitted only if BOTH sides' Mutual lists carry each other
  (mutuality re-verified from both parkings, not trusted one-sided);
- pairs already carrying ANY typed edge between the two records (either
  direction) are the S2.3 typed core - skipped;
- the close-out manifest counted 37 such pairs; the script asserts the
  count and stops loudly on drift;
- idempotent (existing associated-with edges are recognized, not doubled);
- read-modify-write via the FLAG-023 fence-asserting reader.

Individual pairs remain upgradeable to real types later by CO - the
standing invitation recorded in the register entry.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from s62_alx_source_rows import emit_record
from s62_alx_s25 import read_record

TERM_DIR = BACKEND / "wrs" / "records" / "alexandria_world" / "term"

MUTUAL_RE = re.compile(r"\*\*Mutual\*\* \(each lists this term back\):\s*(.*?)(?:\.|\*\*One-directional)", re.S)

NOTE = ("CO-P2-13 (Mark, 2026-07-28): the chunks' own mutual Related-Terms "
        "cross-reference, typed as symmetric association - no hierarchy "
        "claimed (both sides' Reciprocity Notes, verbatim in the record "
        "bodies, attest the pair).")

BODY_NOTE = ("\n\nCO-P2-13 (2026-07-28): the Reciprocity Note's mutual "
             "cross-references now carry typed associated-with edges; see "
             "wrs/migrate/s62_alx_s29_co13.py.")


def canon(name: str) -> str:
    return re.sub(r"\s*/\s*", "/", name.strip()).casefold()


def main():
    records = {}
    for p in sorted(TERM_DIR.glob("*.md")):
        rec, body = read_record(p)
        records[rec["id"]] = [rec, body, p]

    # resolution order: full term names win; then the slash-segments of
    # compound names (the chunks' Related-Terms lists use the short form,
    # e.g. 'Wisdom' for 'Wisdom / Sophia'); aliases last
    name_to_id = {}
    for rid, (rec, _b, _p) in records.items():
        name_to_id[canon(rec["term"])] = rid
    for rid, (rec, _b, _p) in records.items():
        for seg in rec["term"].split("/"):
            name_to_id.setdefault(canon(seg), rid)
    for rid, (rec, _b, _p) in records.items():
        for a in rec.get("aliases") or []:
            name_to_id.setdefault(canon(a), rid)

    # mutual lists per record, from the parked Reciprocity Note
    mutual = {}
    for rid, (rec, body, _p) in records.items():
        m = MUTUAL_RE.search(body)
        names = []
        if m:
            raw = " ".join(m.group(1).split())
            if raw.lower() not in ("none", "none attested", "none yet"):
                names = [n.strip() for n in raw.split(",") if n.strip()]
        ids = set()
        for n in names:
            tid = name_to_id.get(canon(n))
            assert tid, f"{rid}: mutual name unresolved: {n!r}"
            ids.add(tid)
        mutual[rid] = ids

    # mutuality re-verified from both sides
    pairs = set()
    for rid, ids in mutual.items():
        for tid in ids:
            if rid in mutual.get(tid, set()):
                pairs.add(tuple(sorted((rid, tid))))

    def has_edge(a, b):
        for e in records[a][0].get("field_relations") or []:
            if e.get("target_id") == b and e.get("type") != "associated-with":
                return True
        return False

    typed_core = {p for p in pairs if has_edge(p[0], p[1]) or has_edge(p[1], p[0])}
    todo = sorted(pairs - typed_core)
    assert len(todo) == 37, (
        f"expected the close-out manifest's 37 untyped mutual pairs, found "
        f"{len(todo)} - stop and re-diagnose, do not emit")

    changed = 0
    for a, b in todo:
        for src, dst in ((a, b), (b, a)):
            rec, body, path = records[src]
            fr = rec.setdefault("field_relations", [])
            if any(e.get("target_id") == dst and e.get("type") == "associated-with"
                   for e in fr):
                continue  # idempotent re-run
            fr.append({"type": "associated-with", "target_id": dst, "note": NOTE})
            if "CO-P2-13" not in body:
                body = body + BODY_NOTE
            records[src] = [rec, body, path]
            changed += 1
    for rid, (rec, body, path) in records.items():
        emit_record(rec, body, path)
    print(f"CO-P2-13: {len(pairs)} mutual pairs re-verified both-sided; "
          f"{len(typed_core)} already in the typed core; 37 emitted as "
          f"associated-with ({changed} directional edges written this run)")


if __name__ == "__main__":
    main()
