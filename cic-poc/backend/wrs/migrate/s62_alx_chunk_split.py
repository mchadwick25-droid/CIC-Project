"""S6.2/Alexandria - S2.2-equivalent: term records, mechanical half.

Splits each of the 45 chunks in data/alexandria_world/lexicon_chunks/
into a `term` record holding ONLY fields already present in the chunk.
Mechanical by construction (the script parses the committed chunk
files; nothing retyped). Ports wrs/migrate/lexicon_chunk_split.py
(Desert's S2.2) to Alexandria's own chunk format:

  ## Retrieval Front-Matter (fenced block)
    Term        -> term (verbatim)
    Aliases     -> aliases[] (comma-split)
    Tier        -> retrieval.tier
    Retrieve-When / Do-Not-Retrieve-When -> retrieval.*, clauses typed
        per SS3.2 with the same two legal drop classes as Desert
        (retired cross-world guard; em-dash sentinel -> typed null),
        each drop logged
    Tags        -> NOT migrated (RETIRED per CO-P2-09), logged
    Related-Terms -> NOT migrated here (untyped list; absorbed into
        typed field_relations at the S2.3-equivalent - front matter,
        outside the coverage sections)
    World-Code  -> not a record field (world_id carries it)
  ## Quick Meaning        -> quick_meaning (verbatim)
  ## World Meaning        -> world_meaning (verbatim)
  ## Ecological Function  -> PARKED verbatim inside world_meaning under
        the FLAG-002 delimiter (schema home = S2.3's typed
        field_relations), exactly Desert's parking
  ## Distortion Risk      -> the chunk carries EXPLICIT **Modern
        Hearing:** / **World Hearing:** subsections (richer than
        Desert's single paragraph), so the split is mechanical here:
        modern_hearing <- Modern Hearing block (verbatim);
        distortion_risk <- World Hearing block (verbatim)
  ## Key Sources          -> sources[] spans (Desert's split_key_sources
        port): every character lands in exactly one span, source_id
        resolved against srcALX001-032; Scripture citations carry no
        row by the Framework's own Scripture-is-native rule and land in
        the adjacent span (declared; the S2.3-equivalent refines)
  ## Related-Terms Reciprocity Note  -> PARKED verbatim in the record
        BODY under a named delimiter (FLAG-004 precedent: body is not
        schema-governed) - S2.3-equivalent absorbs into field_relations
        notes
  ## Carried Contest - * / ## CT Contest Type / ## Reported-Experience
        Status (6 sections across 5 chunks) -> PARKED verbatim in the
        record BODY under named delimiters - homes arrive with the
        contested_claim records (S2.6-equivalent) and S2.3 authoring

--coverage runs S1.3's content-coverage instrument (F7) per chunk
(body sections vs emitted fields + body parkings); --emit writes.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

CHUNKS = BACKEND / "data" / "alexandria_world" / "lexicon_chunks"
OUT = BACKEND / "wrs" / "records" / "alexandria_world" / "term"

STD_SECTIONS = ("Quick Meaning", "World Meaning", "Ecological Function",
                "Distortion Risk", "Key Sources",
                "Related-Terms Reciprocity Note")

# Key Sources name -> source row (leftmost match wins per span; more
# specific keys listed before generic ones so both get a chance at a hit)
SOURCE_KEYS = [
    ("On the Incarnation", "srcALX027"),
    ("Life of Antony", "srcALX004"),
    ("Quis Dives", "srcALX028"),
    ("Nicene Creed", "srcALX029"),
    ("Clement of Alexandria", "srcALX001"),
    ("Origen", "srcALX002"),
    ("Athanasius", "srcALX003"),
    ("Didymus", "srcALX005"),
    ("Dionysius", "srcALX006"),
    ("Gregory Thaumaturgus", "srcALX007"),
    ("Philo", "srcALX008"),
    ("Eusebius", "srcALX009"),
    ("Palladius", "srcALX010"),
    ("Apophthegmata", "srcALX011"),
    ("Jerome", "srcALX012"),
    ("Ignatius", "srcALX030"),
    ("Irenaeus", "srcALX031"),
    ("Tertullian", "srcALX032"),
    ("Chadwick", "srcALX015"),
    ("Rubenson", "srcALX018"),
    ("Brakke", "srcALX019"),
    ("Young", "srcALX013"),
    ("Wipszycka", "srcALX021"),
    ("Bagnall", "srcALX022"),
]

SENTINELS = {"—", "–", "-"}

PARK_RECIPROCITY = ("[Related-Terms Reciprocity Note — parked at the "
                    "S2.2-equivalent; absorbed into field_relations notes at "
                    "the S2.3-equivalent]")
PARK_SPECIAL = ("[{title} — parked at the S2.2-equivalent; home arrives "
                "with the contested_claim records (S2.6-equivalent) / S2.3 "
                "authoring]")


def parse_chunk(path: Path):
    text = path.read_text(encoding="utf-8")
    # front matter: the fenced block under ## Retrieval Front-Matter
    fmm = re.search(r"## Retrieval Front-Matter\s*\n+```\n(.*?)```", text, re.S)
    fm = {}
    if fmm:
        # keys are "Name:" at line start; values may wrap to continuation lines
        current = None
        for line in fmm.group(1).splitlines():
            m = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
            if m:
                current = m.group(1)
                fm[current] = m.group(2).strip()
            elif current and line.strip():
                fm[current] += " " + line.strip()
    # sections: ## headings
    secs = {}
    for m in re.finditer(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M):
        name = m.group(1).strip()
        if name == "Retrieval Front-Matter":
            continue
        body = m.group(2).strip()
        body = re.sub(r"^-{3,}\s*$", "", body, flags=re.M).strip()
        secs[name] = body
    return fm, secs


def classify_dnrw(text: str):
    t = text.strip()
    if t in SENTINELS:
        return "sentinel", t
    low = t.lower()
    if "different world" in low or "different formation world" in low or "cross-apply" in low:
        return "retired-cross-world", t
    if "not native to this world" in low or "retrojected" in low or "later byzantine" in low:
        return "anachronism-guard", t
    return "sense-disambiguation", t


def split_key_sources(ks_text: str):
    """Every character of the section lands in exactly one span. Hits are
    snapped to sentence starts; when two keys hit the SAME sentence
    ("Athanasius, *On the Incarnation*" matches both the generic author
    key and the specific work key), the more specific key - listed first
    in SOURCE_KEYS - owns the sentence (the collision previously left a
    1-character span and orphaned the sentence; caught by the coverage
    instrument on the first run, see the S2.2 gate artifact)."""
    hits = []
    for rank, (key, sid) in enumerate(SOURCE_KEYS):
        for m in re.finditer(re.escape(key), ks_text):
            b = ks_text.rfind(". ", 0, m.start())
            snapped = b + 2 if b != -1 else 0
            hits.append((snapped, rank, sid))
    if not hits:
        return [("srcALX-UNRESOLVED", ks_text)]
    # winner per sentence-start = most specific key
    by_pos = {}
    for snapped, rank, sid in sorted(hits):
        if snapped not in by_pos or rank < by_pos[snapped][0]:
            by_pos[snapped] = (rank, sid)
    # first surviving position per source id, in position order
    starts, seen = [], set()
    for snapped in sorted(by_pos):
        _rank, sid = by_pos[snapped]
        if sid in seen:
            continue
        seen.add(sid)
        starts.append((snapped, sid))
    starts[0] = (0, starts[0][1])  # leading text (e.g. Scripture) joins span 1
    spans = []
    for i, (pos, sid) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(ks_text)
        spans.append((sid, ks_text[pos:end].strip()))
    return spans


def split_distortion(dr_text: str):
    """Mechanical: the chunk's own explicit subsection labels."""
    mm = re.search(r"(\*\*Modern Hearing:\*\*\s*.*?)(?=\*\*World Hearing:\*\*|\Z)",
                   dr_text, re.S)
    wm = re.search(r"(\*\*World Hearing:\*\*\s*.*)", dr_text, re.S)
    # Desert convention: the label text is PART of the field value
    # (desertlex001's modern_hearing begins "Modern Hearing — ..."), and
    # the coverage instrument counts the label lines - carry the blocks
    # verbatim, labels included.
    modern = mm.group(1).strip() if mm else ""
    world = wm.group(1).strip() if wm else ""
    if not (modern or world):  # no labels: whole section -> distortion_risk
        return "", dr_text.strip()
    return modern, world


def build_record(path: Path, drops: list):
    fm, secs = parse_chunk(path)
    rid = path.stem.split("_")[0]
    tier = int(re.sub(r"[^\d]", "", fm.get("Tier", "1")) or 1)

    retrieve_when = [c.strip() for c in fm.get("Retrieve-When", "").split(";") if c.strip()]
    dnrw = []
    for clause in [c.strip() for c in fm.get("Do-Not-Retrieve-When", "").split(";") if c.strip()]:
        kind, payload = classify_dnrw(clause)
        if kind == "sentinel":
            drops.append((rid, "em-dash-sentinel -> typed null (empty list)", payload))
        elif kind == "retired-cross-world":
            drops.append((rid, "RETIRED class: cross-world guard (Pass 1 SS3.2)", payload))
        else:
            dnrw.append({"condition_type": kind, "text": payload})
    if fm.get("Tags"):
        drops.append((rid, "Tags RETIRED per CO-P2-09", fm["Tags"]))

    ef = secs.get("Ecological Function", "")
    wm = secs.get("World Meaning", "")
    if ef:
        wm = (wm + "\n\n[Ecological Function — parked at the S2.2-equivalent; "
              "restructured into typed field_relations at the S2.3-equivalent "
              "per §3.2 / FLAG-002]: " + ef)

    modern_hearing, distortion = split_distortion(secs.get("Distortion Risk", ""))
    sources = [{"source_id": sid, "author_gravity_note": note}
               for sid, note in split_key_sources(secs.get("Key Sources", ""))]

    rec = {
        "id": rid, "world_id": "alexandria-catechetical", "record_type": "term",
        "schema_version": 1, "jobs": [1, 2, 4, 6], "register": "emic",
        "review_state": "draft", "cache_stability": "static",
        "term": fm.get("Term", ""),
        "aliases": [a.strip() for a in fm.get("Aliases", "").split(",") if a.strip()],
        "quick_meaning": secs.get("Quick Meaning", ""),
        "world_meaning": wm,
        "distortion_risk": distortion,
        "retrieval": {"tier": tier, "retrieve_when": retrieve_when,
                      "do_not_retrieve_when": dnrw, "force_llm_vote": False},
        "sources": sources,
    }
    if modern_hearing:
        rec["modern_hearing"] = modern_hearing

    # body parkings (FLAG-004 precedent): reciprocity note + special sections
    parked_body_parts = []
    if secs.get("Related-Terms Reciprocity Note"):
        parked_body_parts.append(
            PARK_RECIPROCITY + " " + secs["Related-Terms Reciprocity Note"])
    for name, body in secs.items():
        if name in STD_SECTIONS or not body:
            continue
        parked_body_parts.append(PARK_SPECIAL.format(title=name) + " " + body)

    coverage_fields = {"quick_meaning": rec["quick_meaning"],
                       "world_meaning": rec["world_meaning"],
                       "distortion_risk": rec["distortion_risk"],
                       "modern_hearing": rec.get("modern_hearing", "")}
    for i, s in enumerate(sources):
        coverage_fields[f"sources[{i}].author_gravity_note"] = s["author_gravity_note"]
    for i, p in enumerate(parked_body_parts):
        coverage_fields[f"body-parking[{i}]"] = p

    chunk_body = "\n".join(v for v in secs.values() if v)
    return rec, coverage_fields, chunk_body, parked_body_parts


def main():
    emit = "--emit" in sys.argv
    coverage = "--coverage" in sys.argv
    drops = []
    results = []
    from wrs.gates.content_coverage import check_coverage
    for path in sorted(CHUNKS.glob("*.md")):
        rec, fields, chunk_body, parked = build_record(path, drops)
        if emit:
            body = (f"Migrated at the S6.2 S2.2-equivalent (2026-07-27) from "
                    f"`data/alexandria_world/lexicon_chunks/{path.name}` (mechanical split; "
                    f"mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and "
                    f"new-authoring fields arrive at the S2.3-equivalent.")
            if parked:
                body += "\n\n" + "\n\n".join(parked)
            emit_record(rec, body, OUT / f"{rec['id']}.md")
        if coverage:
            r = check_coverage(chunk_body, fields, [])
            results.append((rec["id"], r))
    if emit:
        print(f"emitted {len(list(CHUNKS.glob('*.md')))} term records to {OUT}")
        print("\nDROPS LOG (legal classes only, each logged):")
        for rid, reason, text in drops:
            print(f"  {rid}: [{reason}] {text!r}")
    if coverage:
        print("\nCONTENT-COVERAGE PARITY (S1.3 instrument, per chunk):")
        bad = 0
        for rid, r in results:
            status = "PASS" if not r["missing"] and not r["duplicated"] else "FAIL"
            if status == "FAIL":
                bad += 1
            print(f"  {rid}: {r['covered']}/{r['total']} covered, "
                  f"missing={len(r['missing'])}, duplicated={len(r['duplicated'])} -> {status}")
            for m in r["missing"][:2]:
                print(f"      MISSING: {m[:100]}")
            for d in r["duplicated"][:2]:
                print(f"      DUP: {d['sentence'][:70]} in {d['fields']}")
        sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
