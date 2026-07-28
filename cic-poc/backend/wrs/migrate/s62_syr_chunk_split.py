"""S6.2/Syriac - S2.2-equivalent: term records, mechanical half.

Splits each of the 10 chunks in data/syriac_world/lexicon_chunks/ into a
`term` record holding ONLY fields already present in the chunk. Ports
wrs/migrate/s62_alx_chunk_split.py (Alexandria's S2.2) to the Syriac
chunk format - same section vocabulary, with three Syriac differences,
each declared:

1. SOURCE SPANS RESOLVE BY THE CHUNKS' OWN INLINE "Source Registry #N"
   citations (srcSYR{N:03d}) plus a name-key list for the sentences that
   cite scholarship without a registry number. The FLAG-025 correction
   is applied HERE, declared: syrlex002/syrlex007 cite Griffith 1991
   with the mis-pointer "(Source Registry #26)" - the specific
   "'Singles' in God's Service" name key outranks the #26 hit in the
   same sentence, so the span lands on srcSYR056 (the citation's true
   registry home per the S2.1a sweep). The deployed chunk text is NOT
   touched (the fix rides the S2.8 render).
2. THE TIER-3 CHUNKS (syrlex005 memra, syrlex008 mar) carry a COMBINED
   "**Modern Hearing / World Hearing:**" label - not mechanically
   splittable; the whole section lands in distortion_risk verbatim
   (modern_hearing unset), logged as a declared class. They also carry
   NO World Meaning / Ecological Function / Key Sources sections (the
   S2.1a coverage finding): world_meaning unset, sources[] empty -
   the S2.3-equivalent authors what the tier honestly needs.
3. syrlex009 "## CT Contest Type" and syrlex010 "## Standing
   Distortion-Risk Note" park verbatim in the record BODY under named
   delimiters (the ALX special-section pattern; homes arrive at the
   S2.6/S2.3-equivalents).

Everything else is the ALX port unchanged: front-matter parse,
Retrieve-When/Do-Not-Retrieve-When clause typing (two-value enum with
the sense-disambiguation fallback), Tags RETIRED per CO-P2-09 (logged),
Ecological Function parked inside world_meaning under the FLAG-002
delimiter, Reciprocity Note parked in the body, --coverage runs the
S1.3 content-coverage instrument per chunk.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

CHUNKS = BACKEND / "data" / "syriac_world" / "lexicon_chunks"
OUT = BACKEND / "wrs" / "records" / "syriac_world" / "term"

STD_SECTIONS = ("Quick Meaning", "World Meaning", "Ecological Function",
                "Distortion Risk", "Key Sources",
                "Related-Terms Reciprocity Note")

# name keys for citation sentences WITHOUT an inline registry number
# (rank order = specificity; a name-key hit outranks a registry-number
# hit in the same sentence - the FLAG-025 mechanism)
NAME_KEYS = [
    ("'Singles' in God's Service", "srcSYR056"),   # FLAG-025 correction
    ("Bible and Poetry", "srcSYR054"),
    ("Cambridge History of Early Christian Literature", "srcSYR055"),
    ("(Robert A. Kitchen)", "srcSYR058"),
    ("Papa bar Aggai", "srcSYR058"),
    ("Koltun-Fromm", "srcSYR031"),
    ("Lehto", "srcSYR030"),
    ("The Luminous Eye", "srcSYR029"),
    ("Harp of the Spirit", "srcSYR029"),
    ("Symbols of Church and Kingdom", "srcSYR027"),
    ("Revisiting the Daughters of the Covenant", "srcSYR032"),
    ("Malki", "srcSYR033"),
    ("GEDSH", "srcSYR051"),
]

SENTINELS = {"—", "–", "-"}

PARK_RECIPROCITY = ("[Related-Terms Reciprocity Note - parked at the "
                    "S2.2-equivalent; absorbed into field_relations notes at "
                    "the S2.3-equivalent]")
PARK_SPECIAL = ("[{title} - parked at the S2.2-equivalent; home arrives "
                "with the contested_claim records (S2.6-equivalent) / S2.3 "
                "authoring]")


def parse_chunk(path: Path):
    text = path.read_text(encoding="utf-8")
    fmm = re.search(r"## Retrieval Front-Matter\s*\n+```\n(.*?)```", text, re.S)
    fm = {}
    if fmm:
        current = None
        for line in fmm.group(1).splitlines():
            m = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
            if m:
                current = m.group(1)
                fm[current] = m.group(2).strip()
            elif current and line.strip():
                fm[current] += " " + line.strip()
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
    if ("not native to this world" in low or "retrojected" in low
            or "later syriac tradition" in low or "retrojection" in low):
        return "anachronism-guard", t
    return "sense-disambiguation", t


def split_key_sources(ks_text: str, chunk_id: str, drops: list):
    """ALX span logic, Syriac keys: hits = inline 'Source Registry #N'
    citations (-> srcSYR{N:03d}) at rank BELOW every name key, so a
    specific name key owns a sentence over the number it carries (the
    FLAG-025 mechanism, logged per application)."""
    hits = []
    for rank, (key, sid) in enumerate(NAME_KEYS):
        for m in re.finditer(re.escape(key), ks_text):
            b = ks_text.rfind(". ", 0, m.start())
            snapped = b + 2 if b != -1 else 0
            hits.append((snapped, rank, sid))
    num_rank = len(NAME_KEYS)
    for m in re.finditer(r"Source Registry #(\d+)", ks_text):
        sid = f"srcSYR{int(m.group(1)):03d}"
        b = ks_text.rfind(". ", 0, m.start())
        snapped = b + 2 if b != -1 else 0
        hits.append((snapped, num_rank, sid))
    if not hits:
        return [("srcSYR-UNRESOLVED", ks_text)]
    by_pos = {}
    for snapped, rank, sid in sorted(hits):
        if snapped not in by_pos or rank < by_pos[snapped][0]:
            by_pos[snapped] = (rank, sid)
        elif rank == num_rank and by_pos[snapped][0] < num_rank \
                and by_pos[snapped][1] != sid:
            drops.append((chunk_id,
                          "name-key outranked inline registry number in "
                          "the same sentence (FLAG-025 class where the "
                          "number is #26)",
                          f"{sid} -> {by_pos[snapped][1]}"))
    starts, seen = [], set()
    for snapped in sorted(by_pos):
        _rank, sid = by_pos[snapped]
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


def split_distortion(dr_text: str, chunk_id: str, drops: list):
    if dr_text.startswith("**Modern Hearing / World Hearing:**"):
        drops.append((chunk_id,
                      "combined Modern/World Hearing label - not "
                      "mechanically splittable; whole section -> "
                      "distortion_risk verbatim (declared combined-label "
                      "class: the two Tier-3 chunks AND syrlex003)",
                      dr_text[:60]))
        return "", dr_text.strip()
    mm = re.search(r"(\*\*Modern Hearing:\*\*\s*.*?)(?=\*\*World Hearing:\*\*|\Z)",
                   dr_text, re.S)
    wm = re.search(r"(\*\*World Hearing:\*\*\s*.*)", dr_text, re.S)
    modern = mm.group(1).strip() if mm else ""
    world = wm.group(1).strip() if wm else ""
    if not (modern or world):
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
        wm = (wm + "\n\n[Ecological Function - parked at the S2.2-equivalent; "
              "restructured into typed field_relations at the S2.3-equivalent "
              "per SS3.2 / FLAG-002]: " + ef)

    modern_hearing, distortion = split_distortion(
        secs.get("Distortion Risk", ""), rid, drops)
    if secs.get("Key Sources"):
        sources = [{"source_id": sid, "author_gravity_note": note}
                   for sid, note in split_key_sources(
                       secs["Key Sources"], rid, drops)]
    else:
        sources = []
        drops.append((rid, "no Key Sources section (Tier-3 thin format; "
                           "S2.1a coverage finding) - sources[] empty, "
                           "S2.3-equivalent authors what the tier needs",
                      f"tier={tier}"))

    rec = {
        "id": rid, "world_id": "syriac-edessa-nisibis", "record_type": "term",
        "schema_version": 1, "jobs": [1, 2, 4, 6], "register": "emic",
        "review_state": "draft", "cache_stability": "static",
        "term": fm.get("Term", ""),
        # quote-aware split: '"mystery," "symbol"' keeps the comma inside
        # the quoted alias (the render-parity instrument caught the naive
        # split migrating quoted commas - S2.8 in-step fix, declared)
        "aliases": [a.strip() for a in re.split(
            r',\s*(?=(?:[^"]*"[^"]*")*[^"]*$)', fm.get("Aliases", ""))
            if a.strip()],
        "quick_meaning": secs.get("Quick Meaning", ""),
        "world_meaning": wm,
        "distortion_risk": distortion,
        "retrieval": {"tier": tier, "retrieve_when": retrieve_when,
                      "do_not_retrieve_when": dnrw,
                      # syrlex004 carries an explicit Force-LLM-Vote: true
                      # with its own rationale (parked in the body below) -
                      # the first chunk in any world to set it; missed by
                      # the first emit (hardcoded False), caught at the
                      # S2.3 grounding read, declared in the S2.3 artifact
                      "force_llm_vote": fm.get("Force-LLM-Vote", "")
                                          .lower().startswith("true")},
        "sources": sources,
    }
    if modern_hearing:
        rec["modern_hearing"] = modern_hearing

    parked_body_parts = []
    if fm.get("Force-LLM-Vote"):
        parked_body_parts.append(
            "[Force-LLM-Vote rationale - the chunk's own front-matter "
            "text, carried verbatim (the flag itself is "
            "retrieval.force_llm_vote)]: " + fm["Force-LLM-Vote"])
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
            body = (f"Migrated at the S6.2/SYR S2.2-equivalent (2026-07-28) from "
                    f"`data/syriac_world/lexicon_chunks/{path.name}` (mechanical split; "
                    f"mapping in `wrs/migrate/s62_syr_chunk_split.py`). Related-Terms and "
                    f"new-authoring fields arrive at the S2.3-equivalent.")
            if parked:
                body += "\n\n" + "\n\n".join(parked)
            emit_record(rec, body, OUT / f"{rec['id']}.md")
        if coverage:
            r = check_coverage(chunk_body, fields, [])
            results.append((rec["id"], r))
    if emit:
        print(f"emitted {len(list(CHUNKS.glob('*.md')))} term records to {OUT}")
        print("\nDROPS/DECLARED LOG (each logged):")
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
