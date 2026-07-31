"""S6.2/HAL S2.8-equivalent - HAL chunk views: regenerate the deployed
chunk formats from records (the SYR s62_syr_chunk_views.py port).

Writes into wrs/views/staging/hieronymian_world/ - deployed files
untouched until the parities are green (blueprint S2.8 swap rule; the
swap call is the S2.9-equivalent decision stage's).

HAL differences from the SYR port, each declared:
- LEXICON front matter is a YAML-style fence at the top of the file
  ('---' ... '---', aligned key: value lines), NOT a '## Retrieval
  Front-Matter' code fence; lexicon sections are separated by '---'
  lines. STORY front matter is a BARE key: value block closed by one
  '---'; story sections have no separators.
- record id <-> deployed filename: 'hal_lex03_x' -> hallex03,
  'hal_story03a_x' -> halstory03a (the 'hal_' prefix means
  stem.split('_')[0] is NOT the rid - the S2.2/S2.4 derivation
  reused).
- Tags: RETIRED at S2.2 (CO-P2-09) - never rendered; render parity
  classifies the deployed-only lines.
- Aliases: records born under VG-1a semantics at authoring (S2.2) -
  the generated line joins record aliases; parity compares both lines
  through the runtime parse (identical key space = equivalent).
- Related-Terms: generated from the S2.3 typed field_relations
  (built terms only, first-seen order); the deployed lists' three
  never-built names (Xenodochium, Praeceptor, Monasterium duplex) are
  the declared not-yet-built-partner class - parity classifies them.
- Distortion Risk: single-paragraph (modern_hearing never set).
- Story FEC: gravity_links[0].note after the CO-P2-04 marker where
  links exist; for halstory08/09/10 (the declared no-gravity FECs,
  incl. the FLAG-029 vocabulary-variance case) the section renders
  from the S2.4 BODY PARKING - the S2.5 checkpoint's declared
  fallback, implemented here.
- Composite Source lines ('Composite - see Source Identification
  below') recovered by stripping the S2.4 locus prefix at '): '.
- The two parked specials (hal_lex08 CT Contest Type; hal_lex11
  Reported-Experience Status) and the composites' Source
  Identification + Absent Story Note sections render back from their
  body parkings, chunk order preserved.
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

RECORDS = BACKEND / "wrs" / "records" / "hieronymian_world"
STAGING = HERE / "staging" / "hieronymian_world"
DEPLOYED_LEX = BACKEND / "data" / "hieronymian_world" / "lexicon_chunks"
DEPLOYED_STORY = BACKEND / "data" / "hieronymian_world" / "story_chunks"

EF_MARK = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "
USAGE_MARK = "Usage guidance (chunk, verbatim): "
FEC_LINK_MARK = "(the S2.4 parking, converted at S2.5): "
FEC_PARK_RE = re.compile(
    r"\[Formation Ecology Connection - parked at the S2\.4-equivalent"
    r"[^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
SRCID_PARK_RE = re.compile(
    r"\[Source Identification - [^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
ABSENT_PARK_RE = re.compile(
    r"\[Absent Story Note - [^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
PARK_RE = re.compile(
    r"\[([^\]]+?) - parked at the S2\.2-equivalent[^\]]*\]\s*", re.S)

NEVER_BUILT = {"hallex03": ["Xenodochium"],
               "hallex12": ["Praeceptor"],
               "hallex14": ["Xenodochium"],
               "hallex15": ["Monasterium duplex", "Praeceptor"]}


def rid_of(path: Path) -> str:
    return "hal" + path.stem.split("_")[1]      # hal_lex03_x -> hallex03


def fix_flag028():
    """DECLARED record correction under FLAG-028 (its own routing:
    're-author the benign cases as unqualified aliases where safe, or
    carry them via the confirmed-gloss path, with the gate preventing
    regressions either way'): hallex02's alias re-authored as the
    unqualified 'The Vulgate'. The S2.8 retrieval parity MEASURED the
    regression the flag predicted - the deployed alias line's English
    surface was doing live cross-encoder work on HAL-RT-01 (recall
    1.0 -> 0.5 without it). Safety: 'vulgate' is neither in
    ALIAS_GENERIC_BLOCKLIST_V1 nor a Rule-B collision (term key
    'vulgata' is distinct); the author's anachronism guard survives in
    full in the record's own quick_meaning / world_meaning /
    distortion_risk prose - the alias map governs retrieval
    reachability, not voice usage (voice governance is the prompt's
    and the records' own layer). The alias_safety gate re-run must
    stay 0."""
    p = RECORDS / "term" / "hallex02.md"
    t = p.read_text(encoding="utf-8")
    assert t.startswith("---\n"), p
    front_txt, sep, body = t[4:].partition("\n---\n")
    assert sep, p
    front = yaml.safe_load(front_txt)
    if front.get("aliases") == ["The Vulgate"]:
        print("FLAG-028 correction already applied (idempotent)")
        return
    assert front.get("aliases") == [], front.get("aliases")
    front["aliases"] = ["The Vulgate"]
    marker = ("\n\n[FLAG-028 correction applied at the S2.8-equivalent "
              "(2026-07-31): alias re-authored as the unqualified 'The "
              "Vulgate' after retrieval parity MEASURED the reachability "
              "regression the flag predicted (HAL-RT-01 recall 1.0 -> "
              "0.5 staged vs deployed - the qualified alias line's "
              "English surface was doing live cross-encoder work). The "
              "S2.2 empty-set reading held that the author's "
              "parenthetical was an anachronism flag; the flag's "
              "guard survives in full in this record's own prose "
              "(quick_meaning / world_meaning / distortion_risk) - the "
              "alias map is retrieval reachability, not voice usage. "
              "Gate-safe: no blocklist hit, no Rule-B collision; "
              "alias_safety re-run 0.]")
    if "[FLAG-028 correction applied" not in body:
        body = body.rstrip() + marker + "\n"
    fy = yaml.safe_dump(front, sort_keys=False, allow_unicode=True,
                        width=100, default_flow_style=False)
    p.write_text(f"---\n{fy}---\n{body}", encoding="utf-8")
    print("FLAG-028 correction applied to hallex02")


def load_records(subdir):
    out = {}
    for p in sorted((RECORDS / subdir).glob("*.md")):
        txt = p.read_text(encoding="utf-8")
        assert txt.startswith("---\n"), p
        front, sep, body = txt[4:].partition("\n---\n")
        assert sep, p
        rec = yaml.safe_load(front)
        out[rec["id"]] = (rec, body.strip(), p)
    return out


def parked_sections(body: str):
    hits = list(PARK_RE.finditer(body))
    out = []
    for i, m in enumerate(hits):
        start = m.end()
        end = hits[i + 1].start() if i + 1 < len(hits) else len(body)
        text = body[start:end]
        for stop in ("\n\nMigrated at", "\n\nS2.5", "\n\nS2.6"):
            j = text.find(stop)
            if j >= 0:
                text = text[:j]
        out.append((m.group(1).strip(), text.strip()))
    return out


def fm_lexicon(pairs):
    # width-20 alignment with a guaranteed single space (the
    # Do-Not-Retrieve-When key is 21 chars - '<20' alone would butt the
    # value against the colon, which the runtime indexer must not see)
    lines = [f"{(k + ':').ljust(20)}{v}" if len(k) + 1 < 20
             else f"{k}: {v}" for k, v in pairs if v is not None]
    return "---\n" + "\n".join(lines) + "\n\n---"


def fm_story(pairs):
    lines = [f"{k+':':<16}{v}" for k, v in pairs if v is not None]
    return "\n".join(lines) + "\n\n---"


def render_lexicon(rec, body, term_names):
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    related, seen = [], set()
    for e in rec.get("field_relations") or []:
        t = e.get("target_id")
        if t and t not in seen and t in term_names:
            seen.add(t)
            # the deployed Related-Terms convention uses SHORT display
            # names (lex13's own line says 'Vulgata', never 'Vulgata
            # (translation project)') - paren-stripped term heads; the
            # full-term first render leaked qualifier tokens into the
            # front matter and measurably displaced HAL-RT-01's CE
            # ranking (the 'translation project' token boosting lex07
            # past lex02 on a translation query - caught at retrieval
            # parity, fixed here)
            related.append(re.sub(r"\s*\([^)]*\)", "",
                                  term_names[t]).strip())
    ef = ""
    for e in rec.get("field_relations") or []:
        note = e.get("note") or ""
        j = note.find(EF_MARK)
        if j >= 0:
            ef = note[j + len(EF_MARK):].strip()
            break
    if not ef:
        # EF parked in world_meaning (hallex15, no edges - declared)
        m = re.search(r"\[Ecological Function - parked[^\]]*\]:\s*(.*)",
                      rec.get("world_meaning", ""), re.S)
        if m:
            ef = m.group(1).strip()
    parts = [fm_lexicon([
        ("Term", rec.get("term", "")),
        ("World-Code", "hal"),
        ("Tier", str(ret.get("tier", 1))),
        ("Aliases", ", ".join(rec.get("aliases") or [])),
        ("Related-Terms", ", ".join(related) if related else "(none)"),
        ("Retrieve-When", rw),
        ("Do-Not-Retrieve-When", dnrw),
    ])]
    parts.append("## Quick Meaning\n\n" + rec.get("quick_meaning", ""))
    wm = rec.get("world_meaning", "")
    j = wm.find("\n\n[Ecological Function - parked")
    if j >= 0:
        wm = wm[:j].strip()
    if wm:
        parts.append("## World Meaning\n\n" + wm)
    if ef:
        parts.append("## Ecological Function\n\n" + ef)
    parts.append("## Distortion Risk\n\n" + rec.get("distortion_risk", ""))
    key_sources = " ".join(s.get("author_gravity_note", "").strip()
                           for s in rec.get("sources") or [])
    if key_sources.strip():
        parts.append("## Key Sources\n\n" + key_sources.strip())
    for title, text in parked_sections(body):
        parts.append(f"## {title}\n\n{text}")
    # the front-matter fence already closes with '---'; sections join
    # with the deployed inter-section separator (no doubled fence)
    return parts[0] + "\n\n" + "\n\n---\n\n".join(parts[1:]) + "\n"


def render_story(rec, body):
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    locus = (rec.get("sources") or [{}])[0].get("locus", "")
    j = locus.find("): ")
    if locus.startswith("Composite - elements per") and j >= 0:
        locus = locus[j + 3:]
    parts = [fm_story([
        ("Story-Title", rec.get("title", "")),
        ("World-Code", "hal"),
        ("Tier", str(ret.get("tier", 1))),
        ("Confidence", rec.get("confidence_line") or None),
        ("Source", locus),
        ("Retrieve-When", rw),
        ("Do-Not-Retrieve-When", dnrw),
    ])]
    parts.append("## Story Text\n\n" + rec.get("text", ""))
    links = rec.get("gravity_links") or []
    fec = ""
    if links:
        note = links[0]["note"]
        j = note.find(FEC_LINK_MARK)
        fec = note[j + len(FEC_LINK_MARK):].strip() if j >= 0 else note
    else:
        m = FEC_PARK_RE.search(body)  # the declared 08/09/10 fallback
        if m:
            fec = m.group(1).strip()
            for stop in ("\n\n[Source Identification", "\n\n[Absent Story",
                         "\n\nMigrated at"):
                j = fec.find(stop)
                if j >= 0:
                    fec = fec[:j].strip()
    if fec:
        parts.append("## Formation Ecology Connection\n\n" + fec)
    parts.append("## Tier Justification\n\n"
                 + (rec.get("narrative_tier") or {}).get("justification", ""))
    vs = rec.get("voice_surface", "")
    j = vs.find(USAGE_MARK)
    usage = vs[j + len(USAGE_MARK):].strip() if j >= 0 else ""
    parts.append("## Usage Guidance\n\n" + usage)
    for regex, title in ((SRCID_PARK_RE, "Source Identification"),
                         (ABSENT_PARK_RE, "Absent Story Note")):
        m = regex.search(body)
        if m:
            text = m.group(1).strip()
            for stop in ("\n\n[Absent Story", "\n\nMigrated at"):
                j = text.find(stop)
                if j >= 0:
                    text = text[:j].strip()
            parts.append(f"## {title}\n\n{text}")
    return "\n\n".join(parts) + "\n"


def main():
    if "--fix-flag028" in sys.argv:
        fix_flag028()
    terms = load_records("term")
    stories = load_records("story")
    term_names = {rid: rec["term"] for rid, (rec, _b, _p) in terms.items()}

    lex_out = STAGING / "lexicon_chunks"
    story_out = STAGING / "story_chunks"
    lex_out.mkdir(parents=True, exist_ok=True)
    story_out.mkdir(parents=True, exist_ok=True)

    deployed_lex = {rid_of(p): p.name for p in DEPLOYED_LEX.glob("*.md")}
    deployed_story = {rid_of(p): p.name for p in DEPLOYED_STORY.glob("*.md")}

    n_lex = n_story = 0
    for rid, (rec, body, _p) in terms.items():
        name = deployed_lex.get(rid)
        assert name, f"{rid}: no deployed chunk filename"
        (lex_out / name).write_text(render_lexicon(rec, body, term_names),
                                    encoding="utf-8", newline="\n")
        n_lex += 1
    for rid, (rec, body, _p) in stories.items():
        name = deployed_story.get(rid)
        assert name, f"{rid}: no deployed chunk filename"
        (story_out / name).write_text(render_story(rec, body),
                                      encoding="utf-8", newline="\n")
        n_story += 1
    print(f"staged {n_lex} lexicon + {n_story} story chunk views -> {STAGING}")


if __name__ == "__main__":
    main()
