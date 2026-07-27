"""S2.2 - Desert term records, mechanical half (blueprint S2.2).

Splits each of the 9 chunks in data/desert_world/lexicon_chunks/ into a
`term` record holding ONLY fields already present in the chunk. Mechanical
by construction: the script parses the committed chunk files; no content is
retyped by hand. Declared mapping:

  front matter Term        -> term            (verbatim)
  front matter Aliases     -> aliases[]       (comma-split)
  front matter Tier [n]    -> retrieval.tier
  front matter Retrieve-When -> retrieval.retrieve_when[] (semicolon-split;
                              participant-observable triggers kept verbatim)
  front matter Do-Not-Retrieve-When -> retrieval.do_not_retrieve_when[],
                              TYPED per Pass 1 SS3.2, with the two retired
                              classes DROPPED AND LOGGED (the only legal
                              drops) and the em-dash sentinel becoming a
                              typed null (empty list) with the sentinel
                              logged:
                                - cross-world guard   -> RETIRED (per-world
                                  indexes make the invariant structural)
                                - em-dash sentinel    -> typed null
                                - anachronism wording -> anachronism-guard
                                - else                -> sense-disambiguation
  **Quick Meaning:**       -> quick_meaning   (verbatim)
  **World Meaning:**       -> world_meaning   (verbatim)
  **Ecological Function:** -> PARKED verbatim inside world_meaning under a
                              marked delimiter (FLAG-002: its schema home is
                              S2.3's typed field_relations; parking keeps
                              S2.2's coverage parity honest and visible)
  **Distortion Risk:**     -> distortion_risk (whole section verbatim - the
                              chunk carries Modern/World Hearing as one
                              paragraph; splitting it into modern_hearing is
                              S2.3 refinement, not mechanical work)
  **Key Sources:**         -> sources[] with author_gravity_note carrying
                              each source's own span of the section verbatim
                              (name + title + confidence clause), source_id
                              resolved against the S2.1 registry rows
  front matter Related Terms -> NOT migrated here (untyped list; absorbed
                              into typed field_relations at S2.3 - front
                              matter, so outside the five coverage sections)
  front matter Tags        -> NOT migrated (no Pass 1 SS3.2 field; logged
                              for S2.9)

--coverage mode runs S1.3's content-coverage instrument (F7) per chunk
against the emitted record's fields; --emit writes the records.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

CHUNKS = BACKEND / "data" / "desert_world" / "lexicon_chunks"
OUT = BACKEND / "wrs" / "records" / "desert_world" / "term"

SECTIONS = ("Quick Meaning", "World Meaning", "Ecological Function",
            "Distortion Risk", "Key Sources")

# Key Sources name -> S2.1/S2.1a source row (leftmost match wins per span)
SOURCE_KEYS = [
    ("Evagrius Ponticus", "srcDES004"),
    ("Athanasius of Alexandria", "srcDES001"),
    ("Apophthegmata Patrum", "srcDES005"),
    ("Pachomian", "srcDES002"),
    ("Palladius", "srcDES007"),
    ("Historia Monachorum", "srcDES008"),
    ("Kellia excavations", "srcDES009"),
    ("Nepheros", "srcDES010"),
    ("Letters of Antony", "srcDES003"),
    ("Rubenson", "srcDES013"),
    ("Goehring", "srcDES015"),
    ("Rousseau", "srcDES016"),
    ("Brakke", "srcDES012"),
    ("ammas", "srcDES006"),
]

SENTINELS = {"—", "–", "-"}


def parse_chunk(path: Path):
    text = path.read_text(encoding="utf-8")
    fm_text, body = text.split("---", 2)[1:3]
    fm = {}
    for line in fm_text.strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    secs = {}
    for name in SECTIONS:
        m = re.search(rf"\*\*{name}:\*\*\s*(.*?)(?=\n\s*\*\*|\Z)", body, re.S)
        secs[name] = m.group(1).strip() if m else ""
    return fm, secs


def classify_dnrw(text: str):
    """Type one Do-Not-Retrieve-When clause per the SS3.2 rules; returns
    (kind, payload) where kind in {'sentinel','retired-cross-world',
    'anachronism-guard','sense-disambiguation'}."""
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
    """Split the Key Sources section into per-source spans by the earliest
    occurrence of each known source key; every character of the section
    lands in exactly one span (coverage-exact)."""
    hits = []
    for key, sid in SOURCE_KEYS:
        for m in re.finditer(re.escape(key), ks_text):
            hits.append((m.start(), key, sid))
    hits.sort()
    # keep first hit per span start ordering; drop hits that fall inside the
    # previous span's opening name (duplicate keys resolve to earliest)
    spans = []
    seen_ids = set()
    starts = []
    for pos, key, sid in hits:
        if sid in seen_ids:
            continue
        seen_ids.add(sid)
        starts.append((pos, sid))
    starts.sort()
    if not starts:
        return [("srcDES-UNRESOLVED", ks_text)]
    # Snap each span start back to the preceding sentence boundary so a
    # sentence like "The Kellia excavations (...)" lands whole in its span
    # (the coverage instrument caught the orphaned leading words on the
    # first run - see the S2.2 gate artifact).
    adjusted = []
    prev = 0
    for pos, sid in starts:
        b = ks_text.rfind(". ", 0, pos)
        snapped = b + 2 if b != -1 else 0
        snapped = max(snapped, prev)
        adjusted.append((snapped if adjusted else 0, sid))
        prev = adjusted[-1][0] + 1
    for i, (pos, sid) in enumerate(adjusted):
        end = adjusted[i + 1][0] if i + 1 < len(adjusted) else len(ks_text)
        spans.append((sid, ks_text[pos:end].strip()))
    return spans


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
            drops.append((rid, "RETIRED class: cross-world guard (per-world indexes make the invariant structural - Pass 1 SS3.2)", payload))
        else:
            dnrw.append({"condition_type": kind, "text": payload})

    ef = secs["Ecological Function"]
    wm = secs["World Meaning"]
    if ef:
        wm = (wm + "\n\n[Ecological Function — parked at S2.2; restructured "
              "into typed field_relations at S2.3 per §3.2 / FLAG-002]: " + ef)

    sources = [{"source_id": sid, "author_gravity_note": note}
               for sid, note in split_key_sources(secs["Key Sources"])]

    rec = {
        "id": rid, "world_id": "desert-monasticism", "record_type": "term",
        "schema_version": 1, "jobs": [1, 2, 4, 6], "register": "emic",
        "review_state": "draft", "cache_stability": "static",
        "term": fm.get("Term", ""),
        "aliases": [a.strip() for a in fm.get("Aliases", "").split(",") if a.strip()],
        "quick_meaning": secs["Quick Meaning"],
        "world_meaning": wm,
        "distortion_risk": secs["Distortion Risk"],
        "retrieval": {"tier": tier, "retrieve_when": retrieve_when,
                       "do_not_retrieve_when": dnrw, "force_llm_vote": False},
        "sources": sources,
    }
    coverage_fields = {"quick_meaning": rec["quick_meaning"],
                       "world_meaning": rec["world_meaning"],
                       "distortion_risk": rec["distortion_risk"]}
    for i, s in enumerate(sources):
        coverage_fields[f"sources[{i}].author_gravity_note"] = s["author_gravity_note"]
    chunk_body = "\n".join(secs[n] for n in SECTIONS)
    return rec, coverage_fields, chunk_body


def main():
    emit = "--emit" in sys.argv
    coverage = "--coverage" in sys.argv
    drops = []
    results = []
    from wrs.gates.content_coverage import check_coverage
    for path in sorted(CHUNKS.glob("*.md")):
        rec, fields, chunk_body = build_record(path, drops)
        if emit:
            emit_record(rec,
                        f"Migrated at S2.2 (2026-07-26) from `data/desert_world/lexicon_chunks/{path.name}` "
                        f"(mechanical split; mapping in `wrs/migrate/lexicon_chunk_split.py`). "
                        f"Related-Terms and new-authoring fields arrive at S2.3.",
                        OUT / f"{rec['id']}.md")
        if coverage:
            r = check_coverage(chunk_body, fields, [])
            results.append((rec["id"], r))
    if emit:
        print(f"emitted {len(list(CHUNKS.glob('*.md')))} term records to {OUT}")
        print("\nDROPS LOG (the only legal drop classes, each logged):")
        for rid, reason, text in drops:
            print(f"  {rid}: [{reason}] {text!r}")
        print("\nNOT MIGRATED BY DESIGN: front-matter Related Terms (-> S2.3 "
              "field_relations), Tags (no SS3.2 field; S2.9 list), "
              "Force-LLM-Vote (absent from all Desert chunks).")
    if coverage:
        print("\nCONTENT-COVERAGE PARITY (S1.3 instrument, per chunk):")
        bad = 0
        for rid, r in results:
            status = "PASS" if not r["missing"] and not r["duplicated"] else "FAIL"
            if status == "FAIL":
                bad += 1
            print(f"  {rid}: {r['covered']}/{r['total']} covered, "
                  f"missing={len(r['missing'])}, duplicated={len(r['duplicated'])} -> {status}")
            for m in r["missing"][:3]:
                print(f"      MISSING: {m[:110]}")
            for d in r["duplicated"][:3]:
                print(f"      DUP: {d['sentence'][:80]} in {d['fields']}")
        sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
