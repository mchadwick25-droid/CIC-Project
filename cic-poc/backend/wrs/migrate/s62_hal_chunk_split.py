"""S6.2/HAL - S2.2-equivalent: term records, mechanical half.

Splits the 15 chunks in data/hieronymian_world/lexicon_chunks/ into
`term` records holding ONLY fields already present in the chunk. Ports
the SYR splitter to the HAL format; differences, each declared:

1. FRONT MATTER IS YAML-FENCED ('---' ... '---' with plain key: value
   lines + continuation), not the SYR/ALX code-fence block.
2. DISTORTION RISK is single-paragraph (the Desert style - no
   Modern/World Hearing labels anywhere in the corpus, grep-verified):
   whole section -> distortion_risk, modern_hearing never set.
3. ALIASES parse under the VG-1a semantics from the first record (the
   quote-aware, drop-qualified-segments split) - this world is the
   first authored entirely under the live alias_safety gate. The two
   FLAG-028 cases get their authoring decisions HERE, recorded:
   - hal_lex02 'The Vulgate (anachronistic retrospective label...)':
     the qualifier is the author's own anachronism flag (the
     Catholicos-class shape) - dropping the whole segment is CORRECT
     and the alias set is legitimately empty; reachability = the term
     key 'vulgata' (paren-stripped from 'Vulgata (translation
     project)'). RESOLVED, not deferred.
   - hal_lex07 'Letter (as formation medium)': dropped by the same
     rule AND 'letter' is a bare blocklist generic that would trip
     Rule A anyway - doubly correct; reachability = term key
     'epistula'. RESOLVED.
4. Source spans resolve by a name-key list (no inline registry
   numbers exist in this world's chunks); multi-citation sentences
   carry the first-cited row per the standing S2.2 span-granularity
   class (S2.3 refines).
5. No Force-LLM-Vote lines exist in this corpus (grep-verified);
   Tags retired per CO-P2-09, logged; the two special sections
   (hal_lex08's CT Contest Type / hal_lex11's Reported-Experience
   Status - verify which files at run time) park verbatim in bodies.

--coverage runs the S1.3 content-coverage instrument per chunk;
--emit writes.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

CHUNKS = BACKEND / "data" / "hieronymian_world" / "lexicon_chunks"
OUT = BACKEND / "wrs" / "records" / "hieronymian_world" / "term"

STD_SECTIONS = ("Quick Meaning", "World Meaning", "Ecological Function",
                "Distortion Risk", "Key Sources")

SOURCE_KEYS = [
    ("adversus Rufinum", "srcHAL005"),
    ("Apologia contra Hieronymum", "srcHAL007"),
    ("contra Hieronymum", "srcHAL007"),
    ("Ep. 112", "srcHAL009"),
    ("Augustine", "srcHAL009"),
    ("prefaces", "srcHAL023"),
    ("Praefatio", "srcHAL023"),
    ("commentaries", "srcHAL003"),
    ("Vita Malchi", "srcHAL004"),
    ("Vita Hilarionis", "srcHAL004"),
    ("Rebenich", "srcHAL015"),
    ("Cain", "srcHAL010"),
    ("Ep. 108", "srcHAL001"),
    ("Ep. 22", "srcHAL001"),
    ("Ep. 77", "srcHAL001"),
    ("Ep. 127", "srcHAL001"),
    ("Ep. 107", "srcHAL001"),
    ("Riparius", "srcHAL001"),
    ("Donatus", "srcHAL001"),
    ("epistolary", "srcHAL001"),
    ("corpus generally", "srcHAL001"),
    ("Genealogical claims", "srcHAL001"),
]

PARK_SPECIAL = ("[{title} - parked at the S2.2-equivalent; home arrives "
                "with the contested_claim records (S2.6-equivalent) / S2.3 "
                "authoring]")


def parse_chunk(path: Path):
    text = path.read_text(encoding="utf-8")
    fm = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    assert m, path.name
    current = None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if km:
            current = km.group(1)
            fm[current] = km.group(2).strip()
        elif current and line.strip():
            fm[current] += " " + line.strip()
    secs = {}
    for sm in re.finditer(r"^## (.+?)\s*\n(.*?)(?=^## |\Z)", text, re.S | re.M):
        body = re.sub(r"^-{3,}\s*$", "", sm.group(2), flags=re.M).strip()
        secs[sm.group(1).strip()] = body
    return fm, secs


def parse_aliases_vg1a(value: str, rid: str, drops: list) -> list:
    """The VG-1a runtime semantics applied at authoring: quoted glosses
    extracted; parenthetically-qualified segments dropped whole (each
    drop logged)."""
    if not value:
        return []
    aliases = []
    for phrase in re.findall(r'"([^"]*)"', value):
        c = phrase.strip(" ,")
        if len(c) > 1:
            aliases.append(c)
    remainder = re.sub(r'"[^"]*"', "", value)
    for chunk in re.split(r"[;,/]", remainder):
        if "(" in chunk or ")" in chunk:
            c = chunk.strip()
            if c:
                drops.append((rid, "parenthetically-qualified segment "
                                   "dropped whole (VG-1a semantics at "
                                   "authoring)", c))
            continue
        c = chunk.strip(" /")
        if len(c) > 1:
            aliases.append(c)
    return aliases


def classify_dnrw(text: str):
    t = text.strip()
    if t in {"—", "–", "-"}:
        return "sentinel", t
    low = t.lower()
    if ("anachronistic" in low or "retroject" in low
            or "modern translation-theory" in low or "not this world" in low):
        return "anachronism-guard", t
    return "sense-disambiguation", t


def split_key_sources(ks_text: str):
    hits = []
    for rank, (key, sid) in enumerate(SOURCE_KEYS):
        for m in re.finditer(re.escape(key), ks_text):
            b = ks_text.rfind(". ", 0, m.start())
            snapped = b + 2 if b != -1 else 0
            hits.append((snapped, rank, sid))
    if not hits:
        return [("srcHAL-UNRESOLVED", ks_text)]
    by_pos = {}
    for snapped, rank, sid in sorted(hits):
        if snapped not in by_pos or rank < by_pos[snapped][0]:
            by_pos[snapped] = (rank, sid)
    starts, seen = [], set()
    for snapped in sorted(by_pos):
        _r, sid = by_pos[snapped]
        if sid in seen:
            continue
        seen.add(sid)
        starts.append((snapped, sid))
    starts[0] = (0, starts[0][1])
    spans = []
    for i, (pos, sid) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(ks_text)
        spans.append((sid, ks_text[pos:end].strip()))
    return spans


def build_record(path: Path, drops: list):
    fm, secs = parse_chunk(path)
    stem = path.stem                       # hal_lex01_hebraica-veritas
    rid = "hallex" + stem.split("_")[1][3:]  # -> hallex01
    tier = int(re.sub(r"[^\d]", "", fm.get("Tier", "1")) or 1)

    retrieve_when = [c.strip() for c in fm.get("Retrieve-When", "").split(";") if c.strip()]
    dnrw = []
    for clause in [c.strip() for c in fm.get("Do-Not-Retrieve-When", "").split(";") if c.strip()]:
        kind, payload = classify_dnrw(clause)
        if kind == "sentinel":
            drops.append((rid, "em-dash sentinel -> typed null", payload))
        else:
            dnrw.append({"condition_type": kind, "text": payload})
    if fm.get("Tags"):
        drops.append((rid, "Tags RETIRED per CO-P2-09", fm["Tags"]))

    ef = secs.get("Ecological Function", "")
    wm = secs.get("World Meaning", "")
    if ef:
        wm = (wm + "\n\n[Ecological Function - parked at the S2.2-equivalent; "
              "restructured into typed field_relations at the S2.3-equivalent "
              "per SS3.2 / FLAG-002]: " + ef)

    aliases = parse_aliases_vg1a(fm.get("Aliases", ""), rid, drops)
    sources = [{"source_id": sid, "author_gravity_note": note}
               for sid, note in split_key_sources(secs.get("Key Sources", ""))]

    rec = {
        "id": rid, "world_id": "hieronymian-ascetic-literary",
        "record_type": "term", "schema_version": 1, "jobs": [1, 2, 4, 6],
        "register": "emic", "review_state": "draft",
        "cache_stability": "static",
        "term": fm.get("Term", ""),
        "aliases": aliases,
        "quick_meaning": secs.get("Quick Meaning", ""),
        "world_meaning": wm,
        "distortion_risk": secs.get("Distortion Risk", ""),
        "retrieval": {"tier": tier, "retrieve_when": retrieve_when,
                      "do_not_retrieve_when": dnrw, "force_llm_vote": False},
        "sources": sources,
    }

    parked = []
    for name, body in secs.items():
        if name in STD_SECTIONS or not body:
            continue
        parked.append(PARK_SPECIAL.format(title=name) + " " + body)

    coverage_fields = {"quick_meaning": rec["quick_meaning"],
                       "world_meaning": rec["world_meaning"],
                       "distortion_risk": rec["distortion_risk"]}
    for i, s in enumerate(sources):
        coverage_fields[f"sources[{i}].author_gravity_note"] = s["author_gravity_note"]
    for i, p in enumerate(parked):
        coverage_fields[f"body-parking[{i}]"] = p

    chunk_body = "\n".join(v for v in secs.values() if v)
    return rec, coverage_fields, chunk_body, parked


def main():
    emit = "--emit" in sys.argv
    coverage = "--coverage" in sys.argv
    drops, results = [], []
    from wrs.gates.content_coverage import check_coverage
    for path in sorted(CHUNKS.glob("*.md")):
        rec, fields, chunk_body, parked = build_record(path, drops)
        if emit:
            body = (f"Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) "
                    f"from `data/hieronymian_world/lexicon_chunks/{path.name}` "
                    f"(mechanical split; mapping in "
                    f"`wrs/migrate/s62_hal_chunk_split.py`; aliases parsed "
                    f"under the VG-1a semantics at authoring - this world's "
                    f"records are born matching the runtime key space). "
                    f"Related-Terms and authored fields arrive at S2.3.")
            if parked:
                body += "\n\n" + "\n\n".join(parked)
            emit_record(rec, body, OUT / f"{rec['id']}.md")
        if coverage:
            results.append((rec["id"], check_coverage(chunk_body, fields, [])))
    if emit:
        print(f"emitted {len(list(CHUNKS.glob('*.md')))} term records")
        print("\nDROPS/DECLARED LOG:")
        for rid, reason, text in drops:
            print(f"  {rid}: [{reason}] {text!r}")
    if coverage:
        print("\nCONTENT-COVERAGE PARITY:")
        bad = 0
        for rid, r in results:
            status = "PASS" if not r["missing"] and not r["duplicated"] else "FAIL"
            bad += status == "FAIL"
            print(f"  {rid}: {r['covered']}/{r['total']} covered, "
                  f"missing={len(r['missing'])}, dup={len(r['duplicated'])} -> {status}")
            for m in r["missing"][:2]:
                print(f"      MISSING: {m[:100]}")
        sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
