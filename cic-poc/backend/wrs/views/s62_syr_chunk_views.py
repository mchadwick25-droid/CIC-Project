"""S6.2/SYR S2.8-equivalent - Syriac chunk views: regenerate the deployed
chunk formats from records (the ALX s62_alx_chunk_views.py port).

Writes into wrs/views/staging/syriac_world/ - deployed files untouched
until the parities are green (blueprint S2.8 swap rule; the swap call is
the S2.9-equivalent decision stage's, autonomous per contract note 3).

Syriac differences from the ALX port, each declared:
- World-Code: syr. Parked-section markers use the S2.2 splitter's
  HYPHEN form ('- parked at the S2.2-equivalent'), not ALX's em-dash.
- Force-LLM-Vote: syrlex004/010 carry retrieval.force_llm_vote true
  with the rationale parked in the record body - rendered back as the
  chunk's own Force-LLM-Vote front-matter line (rationale verbatim).
- FLAG-025 CORRECTION APPLIED AT THIS STEP (the flag's own routing:
  'the chunk-text pointer correction rides the S2.8 render'): the
  --fix-flag025 pass rewrites the two records' span text
  '(Source Registry #26, cross-checked)' -> '(Source Registry #56)'
  (srcSYR056 = the citation's true home, extended-registry numbering)
  in syrlex002/syrlex007 - a DECLARED record correction under the
  flag, logged; the deployed chunks then regenerate corrected.
- Tier-3 thin chunks (005/008): World Meaning / EF / Key Sources
  sections skipped when the record honestly has none.
- Story FEC: gravity_links[0].note after the CO-P2-04 marker where
  links exist; for syrstory002/006/008 (the declared no-gravity FECs)
  the section renders from the S2.4 BODY PARKING - the S2.5
  checkpoint's declared fallback requirement, implemented here.
- syrstory009's Source Identification section renders from its body
  parking after Usage Guidance (chunk order preserved).
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

RECORDS = BACKEND / "wrs" / "records" / "syriac_world"
STAGING = HERE / "staging" / "syriac_world"
DEPLOYED_LEX = BACKEND / "data" / "syriac_world" / "lexicon_chunks"
DEPLOYED_STORY = BACKEND / "data" / "syriac_world" / "story_chunks"

EF_MARK = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "
USAGE_MARK = "Usage guidance (chunk, verbatim): "
FEC_LINK_MARK = "(the S2.4 parking, converted at S2.5): "
FEC_PARK_RE = re.compile(
    r"\[Formation Ecology Connection - parked at the S2\.4-equivalent[^\]]*\]\s*(.*?)(?=\n\n\[|\Z)",
    re.S)
SRCID_PARK_RE = re.compile(
    r"\[Source Identification - [^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
PARK_RE = re.compile(
    r"\[([^\]]+?) - parked at the S2\.2-equivalent[^\]]*\]:?\s*", re.S)
FLLM_RE = re.compile(
    r"\[Force-LLM-Vote rationale[^\]]*\]:\s*(.*?)(?=\n\n\[|\n\n[A-Z]|\Z)", re.S)

FLAG025_OLD = "(Source Registry #26, cross-checked)"
FLAG025_NEW = "(Source Registry #56)"


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


def fix_flag025():
    # parsed-YAML rewrite: the flat text replace missed syrlex002's
    # line-wrapped YAML scalar on the first pass (caught in-step)
    n = 0
    for rid in ("syrlex002", "syrlex007"):
        p = RECORDS / "term" / f"{rid}.md"
        t = p.read_text(encoding="utf-8")
        assert t.startswith("---\n"), p
        front_txt, sep, body = t[4:].partition("\n---\n")
        assert sep, p
        front = yaml.safe_load(front_txt)
        changed = False
        for s in front.get("sources") or []:
            note = s.get("author_gravity_note") or ""
            if FLAG025_OLD in note:
                s["author_gravity_note"] = note.replace(FLAG025_OLD,
                                                        FLAG025_NEW)
                changed = True
        if changed:
            marker = ("\n\n[FLAG-025 correction applied at the "
                      "S2.8-equivalent (2026-07-28): the span text's "
                      "mis-pointer '(Source Registry #26, cross-checked)' "
                      "corrected to '(Source Registry #56)' - srcSYR056, "
                      "the citation's true registry home per the S2.1a "
                      "sweep; the deployed chunk regenerates corrected "
                      "from this record.]")
            if "[FLAG-025 correction applied" not in body:
                body = body.rstrip() + marker + "\n"
            fy = yaml.safe_dump(front, sort_keys=False, allow_unicode=True,
                                width=100, default_flow_style=False)
            p.write_text(f"---\n{fy}---\n{body}", encoding="utf-8")
            n += 1
    print(f"FLAG-025 correction applied to {n} record(s)")


def parked_sections(body: str):
    hits = list(PARK_RE.finditer(body))
    out = []
    for i, m in enumerate(hits):
        start = m.end()
        end = hits[i + 1].start() if i + 1 < len(hits) else len(body)
        text = body[start:end]
        for stop in ("\n\n[FLAG-025", "\n\nMigrated at", "\n\nS2.5", "\n\nS2.6"):
            j = text.find(stop)
            if j >= 0:
                text = text[:j]
        title = m.group(1)
        if title.startswith("Related-Terms Reciprocity Note"):
            title = "Related-Terms Reciprocity Note"
        if title.startswith("Force-LLM-Vote"):
            continue  # rendered as front matter, not a section
        out.append((title, text.strip()))
    return out


def fm_block(pairs):
    lines = [f"{k+':':<22}{v}" for k, v in pairs if v is not None]
    return "## Retrieval Front-Matter\n\n```\n" + "\n".join(lines) + "\n```"


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
            related.append(term_names[t])
    ef = ""
    for e in rec.get("field_relations") or []:
        note = e.get("note") or ""
        j = note.find(EF_MARK)
        if j >= 0:
            ef = note[j + len(EF_MARK):].strip()
            break
    fllm = None
    if ret.get("force_llm_vote"):
        m = FLLM_RE.search(body)
        fllm = m.group(1).strip() if m else "true"
    parts = [fm_block([
        ("Term", rec.get("term", "")),
        ("World-Code", "syr"),
        ("Tier", str(ret.get("tier", 1))),
        ("Aliases", ", ".join(rec.get("aliases") or [])),
        ("Related-Terms", ", ".join(related) if related else "(none — see note)"),
        ("Retrieve-When", rw),
        ("Do-Not-Retrieve-When", dnrw),
        ("Force-LLM-Vote", fllm),
    ])]
    parts.append("## Quick Meaning\n\n" + rec.get("quick_meaning", ""))
    wm = rec.get("world_meaning", "")
    # strip the EF parking from world_meaning (it renders as its own section)
    if wm:
        j = wm.find("\n\n[Ecological Function - parked")
        if j >= 0:
            wm = wm[:j].strip()
        if wm:
            parts.append("## World Meaning\n\n" + wm)
    if ef:
        parts.append("## Ecological Function\n\n" + ef)
    elif rec.get("world_meaning", "").find("[Ecological Function - parked") >= 0:
        # EF parked in world_meaning (the no-edge records 009/010)
        m = re.search(r"\[Ecological Function - parked[^\]]*\]:\s*(.*)",
                      rec["world_meaning"], re.S)
        if m:
            parts.append("## Ecological Function\n\n" + m.group(1).strip())
    dr = "\n\n".join(x for x in (rec.get("modern_hearing", ""),
                                 rec.get("distortion_risk", "")) if x)
    parts.append("## Distortion Risk\n\n" + dr)
    if rec.get("sources"):
        key_sources = " ".join(s.get("author_gravity_note", "").strip()
                               for s in rec.get("sources") or [])
        if key_sources.strip():
            parts.append("## Key Sources\n\n" + key_sources.strip())
    for title, text in parked_sections(body):
        parts.append(f"## {title}\n\n{text}")
    return "\n\n---\n\n".join(parts) + "\n"


def render_story(rec, body):
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    locus = (rec.get("sources") or [{}])[0].get("locus", "")
    if rec["id"] == "syrstory009":
        # the composite's deployed Source line is its own text, carried
        # in every source link's shared locus prefix - strip the
        # composite marker the S2.4 sources_for added
        j = locus.find("): ")
        if j >= 0:
            locus = locus[j + 3:]
    parts = [fm_block([
        ("Story-Title", rec.get("title", "")),
        ("World-Code", "syr"),
        ("Tier", str(ret.get("tier", 1))),
        # Key-Line / Signature: palette supply-side (worklist 4b), rolled to
        # this world 2026-08-09. Verbatim from the record's own text.
        ("Signature", "yes" if rec.get("signature") else None),
        ("Key-Line", ('"' + rec["key_line"] + '"') if rec.get("key_line") else None),
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
        m = FEC_PARK_RE.search(body)  # the declared 002/006/008 fallback
        if m:
            fec = m.group(1).strip()
            for stop in ("\n\n[Source Identification", "\n\nMigrated at"):
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
    m = SRCID_PARK_RE.search(body)
    if m:
        srcid = m.group(1).strip()
        j = srcid.find("\n\nMigrated at")
        if j >= 0:
            srcid = srcid[:j].strip()
        parts.append("## Source Identification\n\n" + srcid)
    return "\n\n---\n\n".join(parts) + "\n"


def main():
    if "--fix-flag025" in sys.argv:
        fix_flag025()
    terms = load_records("term")
    stories = load_records("story")
    term_names = {rid: rec["term"] for rid, (rec, _b, _p) in terms.items()}

    lex_out = STAGING / "lexicon_chunks"
    story_out = STAGING / "story_chunks"
    lex_out.mkdir(parents=True, exist_ok=True)
    story_out.mkdir(parents=True, exist_ok=True)

    deployed_lex = {p.stem.split("_")[0]: p.name for p in DEPLOYED_LEX.glob("*.md")}
    deployed_story = {p.stem.split("_")[0]: p.name for p in DEPLOYED_STORY.glob("*.md")}

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
