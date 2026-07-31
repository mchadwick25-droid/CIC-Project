"""S6.2/PAHC - S2.2-equivalent: term records, mechanical half.

Splits the 13 chunks in data/pahc_world/lexicon_chunks/ into `term`
records holding ONLY fields already present in the chunk. PAHC format
differences from the HAL splitter, each declared:

1. FRONT MATTER is the SYR/ALX style: a '## Retrieval Front-Matter'
   section holding a code fence of key: value lines (with
   continuation); sections separated by '---' lines.
2. DISTORTION RISK carries **Modern Hearing:** / **World Hearing:**
   labels (the ALX class): modern_hearing gets the Modern paragraph,
   distortion_risk the World paragraph (label lines stripped, text
   verbatim).
3. THIN-FORMAT chunks pahclex012/013 (front matter + Quick Meaning +
   Distortion Risk only - the declared S2.1a finding): no
   world_meaning, no EF parking, no sources section; their evidentiary
   base (Pliny P07) rides sources[] from the front-matter Term context
   via the SOURCE_DEFAULTS table below, DECLARED (the registry world's
   thin chunks cite through their own body text, not a Key Sources
   section - srcPAHCP07 is both chunks' sole base per the S2.1a
   sweep).
4. ALIASES parse under VG-1a semantics AND the alias_safety gate's
   Rule A is answered AT BIRTH (the second born-clean world): the
   PREFLIGHT (this step, logged in the checkpoint) found 7 Rule-A
   surfaces; each is DROPPED at authoring with its justification in
   DROPS_RULEA below - 5 carried by this world's own confirmed
   glosses ('elder' by presbyteros->'an elder'; 'church' AND
   'assembly' by ekklesia->'the assembly, the church'; 'minister' by
   diakonos->'a deacon, one who serves'; 'the water' by the exact
   A-gloss 'the water'->'baptism'), 'communion' by the ALX
   bare-generic both-sides precedent (eucharist/thanksgiving/the
   Lord's Supper remain), 'association' by remaining reachability
   ('illegal club', 'collegium', term key 'hetaeria'). The deployed
   chunks keep their lines until the S2.8 swap; the drop table is the
   render-parity classification authority (declared for S2.8).
5. Strand A/B labels ride verbatim inside the sections they appear
   in; CT Contest Type sections (where present) park in bodies for
   S2.6; Tags retired per CO-P2-09, logged.
6. Source spans resolve by a name-key list to the registry ids
   (srcPAHCPnn); multi-citation sentences carry the first-cited row
   per the standing S2.2 span-granularity class (S2.3 refines).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

CHUNKS = BACKEND / "data" / "pahc_world" / "lexicon_chunks"
OUT = BACKEND / "wrs" / "records" / "pahc_world" / "term"

STD_SECTIONS = ("Quick Meaning", "World Meaning", "Ecological Function",
                "Distortion Risk", "Key Sources")

SOURCE_KEYS = [
    ("Ignatius", "srcPAHCP03"),
    ("1 Clement", "srcPAHCP02"),
    ("Hermas", "srcPAHCP05"),
    ("Didache", "srcPAHCP01"),
    ("Polycarp's own self-designation", "srcPAHCP04"),
    ("Polycarp, Letter to the Philippians", "srcPAHCP04"),
    ("Justin", "srcPAHCP06"),
    ("Pliny", "srcPAHCP07"),
]

# thin-format chunks: no Key Sources section; base per the S2.1a sweep
SOURCE_DEFAULTS = {
    "pahclex012": [{"source_id": "srcPAHCP07",
                    "author_gravity_note": (
                        "Thin-format chunk (S2.1a declared): hetaeria is "
                        "Pliny's own word for what Christians ceased when "
                        "his edict banned clubs - Letters 10.96, the "
                        "chunk's whole evidentiary base.")}],
    "pahclex013": [{"source_id": "srcPAHCP07",
                    "author_gravity_note": (
                        "Thin-format chunk (S2.1a declared): pertinacia "
                        "is Pliny's own word for what he punished - "
                        "Letters 10.96, the chunk's whole evidentiary "
                        "base.")}],
}

# Rule-A drops at birth (the preflight's 7 hits), each justified:
DROPS_RULEA = {
    "pahclex002": {"elder": "carried by the confirmed gloss presbyteros->'an elder'"},
    "pahclex003": {"church": "carried by the confirmed gloss ekklesia->'the assembly, the church'",
                   "assembly": "carried by the same ekklesia gloss"},
    "pahclex004": {"communion": ("bare blocklist generic, the ALX "
                                  "both-sides precedent; "
                                  "eucharist/thanksgiving/the Lord's "
                                  "Supper remain")},
    "pahclex005": {"minister": "carried by the confirmed gloss diakonos->'a deacon, one who serves'; 'servant'/'deacon' remain"},
    "pahclex011": {"the water": "carried by the exact A-gloss 'the water'->'baptism'; 'baptism' remains"},
    "pahclex012": {"association": "top-5000 generic; 'illegal club', 'collegium', and term key 'hetaeria' remain"},
}


def parse_chunk(path: Path):
    text = path.read_text(encoding="utf-8")
    fm = {}
    fmm = re.search(r"## Retrieval Front-Matter\s*\n+```\n(.*?)```", text, re.S)
    assert fmm, path.name
    current = None
    for line in fmm.group(1).splitlines():
        km = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if km:
            current = km.group(1)
            fm[current] = km.group(2).strip()
        elif current and line.strip():
            fm[current] += " " + line.strip()
    secs = {}
    for sm in re.finditer(r"^## (.+?)\s*$\n(.*?)(?=^## |\Z)", text, re.S | re.M):
        name = sm.group(1).strip()
        if name == "Retrieval Front-Matter":
            continue
        secs[name] = re.sub(r"^-{3,}\s*$", "", sm.group(2), flags=re.M).strip()
    return fm, secs


def parse_aliases_vg1a(value: str, rid: str, drops: list) -> list:
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
                                   "dropped whole (VG-1a)", c))
            continue
        c = chunk.strip(" /")
        if len(c) <= 1:
            continue
        rule_a = DROPS_RULEA.get(rid, {})
        if c.lower() in rule_a:
            drops.append((rid, "Rule-A drop AT BIRTH: " + rule_a[c.lower()], c))
            continue
        aliases.append(c)
    return aliases


def split_dr(dr_text: str):
    m = re.search(r"\*\*Modern Hearing:\*\*\s*(.*?)(?=\*\*World Hearing:\*\*|\Z)",
                  dr_text, re.S)
    w = re.search(r"\*\*World Hearing:\*\*\s*(.*)", dr_text, re.S)
    if m and w:
        return m.group(1).strip(), w.group(1).strip()
    return "", dr_text.strip()


def split_key_sources(ks_text: str):
    hits = []
    for rank, (key, sid) in enumerate(SOURCE_KEYS):
        for m in re.finditer(re.escape(key), ks_text):
            b = ks_text.rfind(". ", 0, m.start())
            snapped = b + 2 if b != -1 else 0
            hits.append((snapped, rank, sid))
    if not hits:
        return [("srcPAHC-UNRESOLVED", ks_text)]
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
    rid = path.stem.split("_")[0]                 # pahclex001
    tier = int(re.sub(r"[^\d]", "", fm.get("Tier", "1")) or 1)

    retrieve_when = [c.strip() for c in
                     fm.get("Retrieve-When", "").split(";") if c.strip()]
    dnrw = []
    for clause in [c.strip() for c in
                   fm.get("Do-Not-Retrieve-When", "").split(";") if c.strip()]:
        if clause in {"—", "–", "-"}:
            drops.append((rid, "em-dash sentinel -> typed null", clause))
            continue
        dnrw.append({"condition_type": "sense-disambiguation", "text": clause})
    if fm.get("Tags"):
        drops.append((rid, "Tags RETIRED per CO-P2-09", fm["Tags"]))

    ef = secs.get("Ecological Function", "")
    wm = secs.get("World Meaning", "")
    if ef:
        wm = (wm + "\n\n[Ecological Function - parked at the S2.2-equivalent; "
              "restructured into typed field_relations at the S2.3-equivalent "
              "per SS3.2 / FLAG-002]: " + ef)

    aliases = parse_aliases_vg1a(fm.get("Aliases", ""), rid, drops)
    modern, world_dr = split_dr(secs.get("Distortion Risk", ""))
    if secs.get("Key Sources"):
        sources = [{"source_id": sid, "author_gravity_note": note}
                   for sid, note in split_key_sources(secs["Key Sources"])]
    else:
        sources = SOURCE_DEFAULTS[rid]

    rec = {
        "id": rid, "world_id": "post-apostolic-house-church",
        "record_type": "term", "schema_version": 1, "jobs": [1, 2, 4, 6],
        "register": "emic", "review_state": "draft",
        "cache_stability": "static",
        "term": fm.get("Term", ""),
        "aliases": aliases,
        "quick_meaning": secs.get("Quick Meaning", ""),
        "world_meaning": wm,
        "distortion_risk": world_dr,
        "retrieval": {"tier": tier, "retrieve_when": retrieve_when,
                      "do_not_retrieve_when": dnrw, "force_llm_vote": False},
        "sources": sources,
    }
    if modern:
        rec["modern_hearing"] = modern

    parked = []
    for name, body in secs.items():
        if name in STD_SECTIONS or not body:
            continue
        parked.append(f"[{name} - parked at the S2.2-equivalent; home "
                      f"arrives with the contested_claim records "
                      f"(S2.6-equivalent) / S2.3 authoring] " + body)

    # coverage projects the ORIGINAL Distortion Risk section (labels
    # included) so the label lines/inline-label sentences match; the
    # record itself holds the mechanically split fields (the ALX
    # convention) - content identity is what the instrument certifies
    coverage_fields = {"quick_meaning": rec["quick_meaning"],
                       "world_meaning": rec["world_meaning"],
                       "distortion-risk-original(split into "
                       "modern_hearing+distortion_risk in the record)":
                           secs.get("Distortion Risk", "")}
    for i, s in enumerate(sources):
        if secs.get("Key Sources"):
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
            body = (f"Migrated at the S6.2/PAHC S2.2-equivalent (2026-07-31) "
                    f"from `data/pahc_world/lexicon_chunks/{path.name}` "
                    f"(mechanical split; mapping in "
                    f"`wrs/migrate/s62_pahc_s22.py`; aliases parsed under "
                    f"the VG-1a semantics with the preflighted Rule-A drops "
                    f"at birth - the second world born matching the runtime "
                    f"key space AND the gate). Related-Terms and authored "
                    f"fields arrive at S2.3.")
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
                  f"missing={len(r['missing'])}, dup={len(r['duplicated'])} "
                  f"-> {status}")
            for m in r["missing"][:2]:
                print(f"      MISSING: {m[:100]}")
        sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
