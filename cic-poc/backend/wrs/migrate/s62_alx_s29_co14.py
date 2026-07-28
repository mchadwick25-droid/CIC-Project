"""CO-P2-14 (Mark, 2026-07-28) - the 42 records' one-directional
completion items COMPLETED as symmetric `associated-with` pairs.

Doc_06 SS4's flag-don't-hide lists ("terms this record lists that do not
list it back") were the original build's own declared open work -
deployment-layer reciprocity-completion items. Option 1 of the decision:
complete them, mechanically, as the association type CO-P2-13 added (no
hierarchy invented; the completion is exactly the mutualization Doc_06
flagged as pending).

Rules:
- source of truth: each record body's parked Reciprocity Note
  **One-directional** list, verbatim from the chunk;
- pairs already carrying ANY edge between the two records (typed core or
  CO-P2-13 associations) are skipped;
- references to not-yet-built records (the Doc_06 governed-CT entries
  with no term record - e.g. Apokatastasis alexlex051 from
  020_restoration) are SKIPPED AND DECLARED, routed to decision 3 of the
  queue (the missing governed-CT term records), never silently dropped;
- full accounting printed and reconciled against Doc_06's own sheet
  figure (153 one-directional link-entries);
- idempotent; fence-asserting reader.
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

ONEDIR_RE = re.compile(
    r"\*\*One-directional\*\*[^:]*:\s*(.*?)(?:\.\s*\*\*Not yet built|\*\*Not yet built|\Z)",
    re.S)

NOTE = ("CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4's one-directional "
        "completion item, COMPLETED as the symmetric association the "
        "flag-don't-hide discipline held it open for - the chunk's own "
        "cross-reference, mutualized per the build's declared intent.")

BODY_NOTE = ("\n\nCO-P2-14 (2026-07-28): the Reciprocity Note's "
             "one-directional completion items completed as associated-with "
             "pairs; see wrs/migrate/s62_alx_s29_co14.py.")


def canon(name: str) -> str:
    return re.sub(r"\s*/\s*", "/", name.strip()).casefold()


def main():
    records = {}
    for p in sorted(TERM_DIR.glob("*.md")):
        rec, body = read_record(p)
        records[rec["id"]] = [rec, body, p]

    name_to_id = {}
    for rid, (rec, _b, _p) in records.items():
        name_to_id[canon(rec["term"])] = rid
    for rid, (rec, _b, _p) in records.items():
        for seg in rec["term"].split("/"):
            name_to_id.setdefault(canon(seg), rid)
    for rid, (rec, _b, _p) in records.items():
        for a in rec.get("aliases") or []:
            name_to_id.setdefault(canon(a), rid)

    total_links = 0
    unbuilt = []
    pairs = set()
    records_with_lists = 0
    for rid, (rec, body, _p) in records.items():
        m = ONEDIR_RE.search(body)
        if not m:
            continue
        raw = " ".join(m.group(1).split()).rstrip(".")
        if raw.lower() in ("none", "none yet", ""):
            continue
        records_with_lists += 1
        for n in [x.strip() for x in raw.split(",") if x.strip()]:
            total_links += 1
            tid = name_to_id.get(canon(n))
            if tid is not None:
                pairs.add(tuple(sorted((rid, tid))))
                continue
            # compound shorthand (e.g. 'Image/Likeness' = Image of God +
            # Likeness of God): resolve each slash-segment; all-or-nothing.
            # The chunks' one attested short-form pair is declared here
            # explicitly (the terms' full names carry no bare segment):
            SHORT = {"image": "alexlex009", "likeness": "alexlex012"}
            seg_ids = [name_to_id.get(canon(s)) or SHORT.get(canon(s))
                       for s in n.split("/")]
            if len(seg_ids) > 1 and all(seg_ids):
                for sid in set(seg_ids):
                    pairs.add(tuple(sorted((rid, sid))))
            else:
                unbuilt.append((rid, n))

    def has_any_edge(a, b):
        return any(e.get("target_id") == b
                   for e in records[a][0].get("field_relations") or [])

    covered = {p for p in pairs if has_any_edge(p[0], p[1]) or has_any_edge(p[1], p[0])}
    todo = sorted(pairs - covered)

    changed = 0
    for a, b in todo:
        for src, dst in ((a, b), (b, a)):
            rec, body, path = records[src]
            fr = rec.setdefault("field_relations", [])
            if any(e.get("target_id") == dst and e.get("type") == "associated-with"
                   for e in fr):
                continue
            fr.append({"type": "associated-with", "target_id": dst, "note": NOTE})
            if "CO-P2-14" not in body:
                body = body + BODY_NOTE
            records[src] = [rec, body, path]
            changed += 1
    dirty = {src for a, b in todo for src in (a, b)}
    for rid in sorted(dirty):
        rec, body, path = records[rid]
        emit_record(rec, body, path)

    print(f"CO-P2-14 accounting: {records_with_lists} records carry "
          f"one-directional lists; {total_links} link-entries parsed "
          f"(Doc_06's sheet: 153); {len(pairs)} distinct resolvable pairs; "
          f"{len(covered)} already covered by typed/associated edges; "
          f"{len(todo)} pairs completed ({changed} directional edges this run); "
          f"{len(unbuilt)} not-yet-built reference(s) DECLARED and routed to "
          f"decision 3: {unbuilt}")


if __name__ == "__main__":
    main()
