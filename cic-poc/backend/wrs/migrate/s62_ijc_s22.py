"""S6.2/IJC - S2.2-equivalent: mechanical split of the 12 deployed
lexicon chunks into term records, under Rule-A-at-birth (the live
alias_safety gate; 11 confirmed IJC glosses in view).

IJC format specifics, declared:
- Front matter: fenced block with BLANK LINES between fields (the
  fleet's third front-matter dialect); parsed per-line.
- Sections separated by `---` rules; the IJC-specific inventory
  (Plural-Voices Note x3, CT Contest Type x4, Reported-Experience
  Status x2, Final Assembly Instruction x12, Key Sources x10) is
  PARKED VERBATIM in record bodies until each finds its typed home
  (Plural-Voices -> S2.3 voice/strand apparatus; CT Contest Type ->
  S2.6 contested claims; RES -> S2.3 confidence apparatus; Final
  Assembly Instruction -> assembly provenance, stays parked).
- Distortion Risk: **Modern Hearing:** / **World Hearing:** labeled
  halves -> modern_hearing / distortion_risk (the PAHC convention);
  coverage projects the ORIGINAL section.
- Tags RETIRED per CO-P2-09 (recorded drops).

ALIAS AUTHORING TABLES (the FLAG-035 corrections + the one Rule-A
drop; every deployed surface accounted for, none silently lost - the
FLAG-028 lesson):
- ijclex003: deployed line's negation idiom (`not "Arian"`) parses to
  an 'Arian' key - the EXACT mapping the chunk forbids (FLAG-035).
  Authored aliases: Homoian, "like the Father", the Dated Creed
  formula. 'Arian' DELIBERATELY NOT carried (the chunk's own
  instruction; the guidance lives in Distortion Risk).
- ijclex004: `being in/out of communion` parses to junk key 'being
  in' (FLAG-035); `communion (as juridical status)` dropped whole by
  the VG-1a parenthetical rule. Authored: communion, in communion,
  out of communion, ecclesiastical fellowship (the juridical-status
  sense is the record's own content). Bare 'communion' is a top-5000
  generic THE GATE ITSELF caught on first emit (the deployed line
  never exposed it - the parenthetical drop hid it; the authoring
  reintroduced it deliberately): carried under an
  alias_generic_override_note (the alexlex022 'the Christ'
  documented-exception precedent) - the term's English name IS
  'communion', no confirmed gloss carries the surface, and this
  world has no rival eucharistic term for the word to collide with.
- ijclex007: 'council' is the preflight's ONE RULE-A HIT (top-5000
  generic) - DROPPED AT BIRTH; the surface is carried by the
  confirmed gloss 'a council (concilium)' (the A-gloss route, the
  PAHC 'the water' precedent). Authored: synod, ecumenical council.
- ijclex010: `Nea Rhome (unmarked transliteration)` dropped whole by
  the parenthetical rule - a REAL retrieval surface (the FLAG-028
  class). Authored: New Rome, Constantinople as New Rome, Nea Rhome.
- ijclex012: `martyr cult (as used in this world specifically)`
  dropped whole - same class. Authored: martyr shrine, martyr cult.
All other alias lines carried via the VG-1a parse unchanged.

Usage:
  python wrs/migrate/s62_ijc_s22.py --emit
  python wrs/migrate/s62_ijc_s22.py --coverage
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

from source_rows_from_doc02 import emit_record          # noqa: E402
from s62_pahc_s22 import parse_aliases_vg1a, split_dr   # noqa: E402

CHUNKS = BACKEND / "data" / "imperial_juridical_world" / "lexicon_chunks"
OUT = (BACKEND / "wrs" / "records" / "imperial_juridical_world" / "term")
WID = "imperial-juridical-christianity"

# alias authoring tables (docstring owns the reasoning)
ALIAS_AUTHORED = {
    "ijclex003": (["Homoian", "like the Father", "the Dated Creed formula"],
                  "FLAG-035: negation idiom parsed to the forbidden 'Arian' "
                  "key; 'Arian' deliberately not carried"),
    "ijclex004": (["communion", "in communion", "out of communion",
                   "ecclesiastical fellowship"],
                  "FLAG-035: 'in/out of' idiom parsed to junk key; "
                  "parenthetical qualifier recovered"),
    "ijclex007": (["synod", "ecumenical council"],
                  "RULE-A DROP AT BIRTH: 'council' (top-5000 generic) - "
                  "surface carried by the confirmed gloss 'a council "
                  "(concilium)'"),
    "ijclex010": (["New Rome", "Constantinople as New Rome", "Nea Rhome"],
                  "VG-1a parenthetical drop recovered: 'Nea Rhome' is a "
                  "real retrieval surface (the FLAG-028 class)"),
    "ijclex012": (["martyr shrine", "martyr cult"],
                  "VG-1a parenthetical drop recovered: 'martyr cult' is a "
                  "real retrieval surface"),
}

DROPS_RULEA = {"ijclex007": {"council": (
    "top-5000 generic (the preflight's one hit); the surface reaches "
    "participants through the confirmed gloss 'a council (concilium)' - "
    "the A-gloss route, the PAHC 'the water' precedent")}}

# Key Sources phrase -> source id (order = precedence, the PAHC shape)
SOURCE_KEYS = [
    ("Julius I's letter", "srcIJC04"),
    ("Tome to Flavian", "srcIJC12"),
    ("letters rejecting Canon 28", "srcIJC13"),
    ("rejection of Canon 28", "srcIJC13"),
    ("epigraphic corpus", "srcIJC14"),
    ("decretal material", "srcIJC15"),
    ("Canon 3 of the Council of Constantinople", "srcIJC10"),
    ("Canon 3 of Constantinople", "srcIJC10"),
    ("Canon 28 of the Council of Chalcedon", "srcIJC11"),
    ("Canon 28 of Chalcedon", "srcIJC11"),
    ("Auxentius of Durostorum", "srcIJC23"),
    ("Sermo contra Auxentium", "srcIJC07"),
    ("Confessions", "srcIJC08"),
    ("Acts and Canons of Nicaea", "srcIJC09"),
    ("Nicaea, Constantinople (381), and Chalcedon", "srcIJC09"),
    ("Theodosian Code", "srcIJC16"),
    ("conciliar canons", "srcIJC09"),
    ("Leo I's own letters", "srcIJC13"),
    ("Leo I's Tome", "srcIJC12"),
]

# ijclex011/012 carry no Key Sources by design (S2.1a): material-culture
# terms whose evidence classes are the registry's own material rows.
SOURCE_DEFAULTS = {
    "ijclex011": [{"source_id": "srcIJC38",
                   "author_gravity_note": (
                       "No Key Sources by design (S2.1a): the basilica "
                       "term's evidence is the Milan basilica complex "
                       "itself (registry row 38) plus the 386 standoff "
                       "texts already carried by "
                       "imperator-intra-ecclesiam's own sources.")},
                  {"source_id": "srcIJC37",
                   "author_gravity_note": (
                       "Old St. Peter's (row 37): the Constantinian "
                       "monumental expression the chunk's World Meaning "
                       "describes.")}],
    "ijclex012": [{"source_id": "srcIJC14",
                   "author_gravity_note": (
                       "No Key Sources by design (S2.1a): the martyrium "
                       "term's evidence is Damasus's epigraphic corpus "
                       "(row 14) - the martyr cult as institutional "
                       "self-presentation, the chunk's own core claim.")}],
}

PARKED_SECTIONS = ("Plural-Voices Note", "CT Contest Type",
                   "Reported-Experience Status",
                   "Final Assembly Instruction")


def parse_chunk(path: Path):
    txt = path.read_text(encoding="utf-8")
    fm = {}
    fence = re.search(r"```\n(.*?)```", txt, re.S)
    for line in (fence.group(1) if fence else "").splitlines():
        m = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
        elif line.strip() and fm:
            fm[list(fm)[-1]] += " " + line.strip()
    secs = {}
    for sm in re.finditer(
            r"^## (?!Retrieval Front-Matter)(.+?)$\n(.*?)(?=^## |\Z)",
            txt[fence.end():] if fence else txt, re.S | re.M):
        body = re.sub(r"^-{3,}\s*$", "", sm.group(2), flags=re.M).strip()
        secs[sm.group(1).strip()] = body
    return fm, secs


def split_key_sources(ks_text: str):
    hits = []
    for rank, (key, sid) in enumerate(SOURCE_KEYS):
        for m in re.finditer(re.escape(key), ks_text):
            b = ks_text.rfind(". ", 0, m.start())
            snapped = b + 2 if b != -1 else 0
            hits.append((snapped, rank, sid))
    if not hits:
        return [("srcIJC-UNRESOLVED", ks_text)]
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
    rid = path.stem.split("_")[0]
    tier = int(re.sub(r"[^\d]", "", fm.get("Tier", "1")) or 1)

    retrieve_when = [c.strip() for c in
                     fm.get("Retrieve-When", "").split(";") if c.strip()]
    dnrw = []
    for clause in [c.strip() for c in
                   fm.get("Do-Not-Retrieve-When", "").split(";")
                   if c.strip()]:
        if clause in {"—", "–", "-"}:
            drops.append((rid, "em-dash sentinel -> typed null", clause))
            continue
        dnrw.append({"condition_type": "sense-disambiguation",
                     "text": clause})
    if fm.get("Tags"):
        drops.append((rid, "Tags RETIRED per CO-P2-09", fm["Tags"]))

    ef = secs.get("Ecological Function", "")
    wm = secs.get("World Meaning", "")
    if ef:
        wm = (wm + "\n\n[Ecological Function - parked at the "
              "S2.2-equivalent; restructured into typed field_relations "
              "at the S2.3-equivalent per SS3.2 / FLAG-002]: " + ef)

    if rid in ALIAS_AUTHORED:
        aliases, why = ALIAS_AUTHORED[rid]
        drops.append((rid, f"ALIAS LINE AUTHORED ({why})",
                      fm.get("Aliases", "")))
    else:
        aliases = parse_aliases_vg1a(fm.get("Aliases", ""), rid, drops)

    modern, world_dr = split_dr(secs.get("Distortion Risk", ""))
    if secs.get("Key Sources"):
        sources = [{"source_id": sid, "author_gravity_note": note}
                   for sid, note in split_key_sources(secs["Key Sources"])]
    else:
        sources = SOURCE_DEFAULTS[rid]

    rec = {
        "id": rid, "world_id": WID,
        "record_type": "term", "schema_version": 1, "jobs": [1, 2, 4, 6],
        "register": "emic", "review_state": "draft",
        "cache_stability": "static",
        "term": fm.get("Term", ""),
        "aliases": aliases,
        "quick_meaning": secs.get("Quick Meaning", ""),
        "world_meaning": wm,
        "distortion_risk": world_dr,
        "retrieval": {"tier": tier, "retrieve_when": retrieve_when,
                      "do_not_retrieve_when": dnrw,
                      "force_llm_vote": False},
        "sources": sources,
    }
    if modern:
        rec["modern_hearing"] = modern
    if rid == "ijclex004":
        rec["alias_generic_override_note"] = (
            "'communion' is deliberately generic: the term IS communio "
            "- its English name is the bare word, no confirmed gloss "
            "carries the surface, and this world has no rival "
            "eucharistic term to collide with (the alexlex022 "
            "precedent; gate-caught on first emit, documented not "
            "suppressed).")
    if rid in DROPS_RULEA:
        for surf, why in DROPS_RULEA[rid].items():
            drops.append((rid, f"RULE-A DROP AT BIRTH ({why})", surf))

    parked = []
    for name in PARKED_SECTIONS:
        body = secs.get(name, "")
        if body:
            parked.append(f"[{name} - parked at the S2.2-equivalent; "
                          f"typed home per the splitter docstring] " + body)

    coverage_fields = {"quick_meaning": rec["quick_meaning"],
                       "world_meaning": rec["world_meaning"],
                       "distortion-risk-original(split into "
                       "modern_hearing+distortion_risk in the record)":
                           secs.get("Distortion Risk", "")}
    for i, s in enumerate(sources):
        if secs.get("Key Sources"):
            coverage_fields[f"sources[{i}].author_gravity_note"] = \
                s["author_gravity_note"]
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
            body = (f"Migrated at the S6.2/IJC S2.2-equivalent (2026-07-31) "
                    f"from `data/imperial_juridical_world/lexicon_chunks/"
                    f"{path.name}` (mechanical split; mapping and alias "
                    f"authoring tables in `wrs/migrate/s62_ijc_s22.py` - "
                    f"the FLAG-035 corrections and the one Rule-A birth "
                    f"drop declared there; the third world born matching "
                    f"the runtime key space AND the gate). Related-Terms "
                    f"and authored fields arrive at S2.3.")
            if parked:
                body += "\n\n" + "\n\n".join(parked)
            emit_record(rec, body, OUT / f"{rec['id']}.md")
        if coverage:
            results.append((rec["id"],
                            check_coverage(chunk_body, fields, [])))
    if emit:
        print(f"emitted {len(list(CHUNKS.glob('*.md')))} term records")
        print("\nDROPS/DECLARED LOG:")
        for rid, reason, text in drops:
            print(f"  {rid}: [{reason}] {text!r}")
    if coverage:
        print("\nCONTENT-COVERAGE PARITY:")
        bad = 0
        for rid, r in results:
            status = ("PASS" if not r["missing"] and not r["duplicated"]
                      else "FAIL")
            bad += status == "FAIL"
            print(f"  {rid}: {r['covered']}/{r['total']} covered, "
                  f"missing={len(r['missing'])}, dup={len(r['duplicated'])} "
                  f"-> {status}")
            for m in r["missing"][:2]:
                print(f"      MISSING: {m[:100]}")
        sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
