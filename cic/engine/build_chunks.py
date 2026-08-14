#!/usr/bin/env python3
"""The clean system's ONE chunk builder, for every world.

Renderers carried verbatim from the old tree's proven chunk view (the
Syriac S2.8 render, itself the ALX port); world code and file naming
come from the world table and each record's own chunk_slug field. The
FLAG-025 fixer stayed behind - the records already carry its correction.

  python cic/engine/build_chunks.py --world syriac
  python cic/engine/build_chunks.py --world syriac --parity DEPLOYED_DATA_DIR
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from worlds import WORLDS  # noqa: E402


def load_records(records_root, subdir):
    out = {}
    d = records_root / subdir
    if not d.is_dir():
        return out
    for p in sorted(d.glob("*.md")):
        txt = p.read_text(encoding="utf-8")
        assert txt.startswith("---\n"), p
        front, sep, body = txt[4:].partition("\n---\n")
        assert sep, p
        rec = yaml.safe_load(front)
        out[rec["id"]] = (rec, body.strip(), p)
    return out


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


def render_lexicon(rec, body, term_names, world_code):
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
        ("World-Code", world_code),
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


def render_story(rec, body, world_code):
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
        ("World-Code", world_code),
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


def render_ambient(rec, world_code):
    # Redesign step 5 (2026-08-14): the Native-Ambient chunk. The register
    # marking rides IN the chunk - both as a front-matter line and as a
    # closing voice rule - so retrieval delivers the texture already
    # wrapped in its own permission: common life of the place, never a
    # named voice's own act, never a formation claim.
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    regs = "; ".join(
        f"Source Registry #{int(s['source_id'][6:])}"
        for s in rec.get("sources") or [])
    parts = [fm_block([
        ("Ambient-Title", rec.get("title", "")),
        ("World-Code", world_code),
        ("Register", "Native-Ambient - the common life of the place, "
                     "not the teaching of a named voice"),
        ("Tier", str(ret.get("tier", 3))),
        ("Domain", rec.get("ambient_domain", "")),
        ("Sources", regs),
        ("Retrieve-When", rw),
        ("Do-Not-Retrieve-When", dnrw),
    ])]
    # Quick Meaning feeds the embedded retrieval surface (S3.1 R1 rule:
    # surface, not body). Derived, not authored: the text minus its fixed
    # common-life marking sentence, cut at a word boundary.
    text = rec.get("text", "")
    marking = "Common life of the place, not the teaching of any one voice."
    gist = text[len(marking):].strip() if text.startswith(marking) else text
    if len(gist) > 240:
        gist = gist[:240].rsplit(" ", 1)[0] + "…"
    parts.append("## Quick Meaning\n\n" + gist)
    parts.append("## Ambient Text\n\n" + text)
    parts.append("## Period Note\n\n" + rec.get("period_note", ""))
    parts.append(
        "## Voice Rule\n\n"
        "Offer this as the shared background of the place - what anyone in "
        "these streets would have known - and say so. Never put it in a "
        "named person's mouth or life, never let it anchor a claim about "
        "what formed us; when it touches something our own record teaches, "
        "the record's own voice takes over.")
    # NO '---' section separators here, deliberately: the runtime lexicon
    # parser treats everything before the second '---' as front matter and
    # drops it from the content payload - with plain headings the WHOLE
    # chunk (marking, text, period note, voice rule) rides as payload.
    return "\n\n".join(parts) + "\n"


def _ambient_slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return "-".join(s.split("-")[:5])




# --------------------------------------------------------------
# Alexandria chunk style, carried verbatim from its proven view
# (each world's deployed chunk FORMAT evolved separately; the
# renderer variant is selected per world by chunk_style)
# --------------------------------------------------------------
ALX_EF_MARK = ("Chunk Ecological Function (verbatim, absorbed per "
           "FLAG-002): ")
ALX_USAGE_MARK = "Usage guidance (chunk, verbatim): "
ALX_PARK_RE = re.compile(
    r"\[([^\]]+?) — parked at the S2\.2-equivalent[^\]]*\]\s*", re.S)


def parked_sections_alx(body: str):
    """Extract the parked sections: [(title, text), ...] in body order."""
    hits = list(ALX_PARK_RE.finditer(body))
    out = []
    for i, m in enumerate(hits):
        start = m.end()
        end = hits[i + 1].start() if i + 1 < len(hits) else len(body)
        text = body[start:end]
        # trim trailing migration notes (S2.5/S2.6 appends)
        for stop in ("\n\nS2.5-equivalent (", "\n\nS2.6-equivalent (",
                     "\n\nCO-P2-13 (", "\n\nMigrated at"):
            j = text.find(stop)
            if j >= 0:
                text = text[:j]
        title = m.group(1)
        if title.startswith("Related-Terms Reciprocity Note"):
            title = "Related-Terms Reciprocity Note"
        out.append((title, text.strip()))
    return out


def render_lexicon_alx(rec, body, term_names, world_code):
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
        j = note.find(ALX_EF_MARK)
        if j >= 0:
            ef = note[j + len(ALX_EF_MARK):].strip()
            break
    parts = [fm_block([
        ("Term", rec.get("term", "")),
        ("World-Code", world_code),
        ("Tier", str(ret.get("tier", 1))),
        ("Aliases", ", ".join(rec.get("aliases") or [])),
        ("Related-Terms", ", ".join(related)),
        ("Retrieve-When", rw),
        ("Do-Not-Retrieve-When", dnrw),
    ])]
    parts.append("## Quick Meaning\n\n" + rec.get("quick_meaning", ""))
    parts.append("## World Meaning\n\n" + rec.get("world_meaning", ""))
    if ef:
        parts.append("## Ecological Function\n\n" + ef)
    dr = "\n\n".join(x for x in (rec.get("modern_hearing", ""),
                                 rec.get("distortion_risk", "")) if x)
    parts.append("## Distortion Risk\n\n" + dr)
    key_sources = " ".join(s.get("author_gravity_note", "").strip()
                           for s in rec.get("sources") or [])
    parts.append("## Key Sources\n\n" + key_sources.strip())
    for title, text in parked_sections_alx(body):
        parts.append(f"## {title}\n\n{text}")
    return "\n\n---\n\n".join(parts) + "\n"


def render_story_alx(rec, world_code):
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    locus = (rec.get("sources") or [{}])[0].get("locus", "")
    parts = [fm_block([
        ("Story-Title", rec.get("title", "")),
        ("World-Code", world_code),
        ("Tier", str(ret.get("tier", 1))),
        # Key-Line / Signature: palette supply-side (worklist 4b), rolled to
        # this world 2026-08-09. Verbatim from the record's own text.
        ("Signature", "yes" if rec.get("signature") else None),
        ("Key-Line", ('"' + rec["key_line"] + '"') if rec.get("key_line") else None),
        ("Confidence", rec.get("confidence_line") or None),  # CO-P2-16
        ("Source", locus),
        ("Retrieve-When", rw),
        ("Do-Not-Retrieve-When", dnrw),
    ])]
    parts.append("## Story Text\n\n" + rec.get("text", ""))
    links = rec.get("gravity_links") or []
    if links:
        parts.append("## Formation Ecology Connection\n\n" + links[0]["note"])
    parts.append("## Tier Justification\n\n"
                 + (rec.get("narrative_tier") or {}).get("justification", ""))
    vs = rec.get("voice_surface", "")
    j = vs.find(ALX_USAGE_MARK)
    usage = vs[j + len(ALX_USAGE_MARK):].strip() if j >= 0 else ""
    parts.append("## Usage Guidance\n\n" + usage)
    return "\n\n---\n\n".join(parts) + "\n"




# ==============================================================
# Per-world chunk styles, carried verbatim from each proven view
# ==============================================================
EF_MARKER_desert = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "


FEC_DELIM_desert = ("[Formation Ecology Connection — parked at S2.8 per FLAG-004; "
             "awaiting S2.9 restructure]")
SRC_DELIM_desert = ("[Source Identification — parked at S2.8 per FLAG-004; SS3.3's "
             "tier-4 rule names sources[] as the home; awaiting S2.9]")


def _parked_desert(body: str, delim: str) -> str:
    if delim not in body:
        return ""
    tail = body.split(delim, 1)[1]
    # section runs until the next parking delimiter or end of body
    for other in (FEC_DELIM_desert, SRC_DELIM_desert):
        if other != delim and other in tail:
            tail = tail.split(other, 1)[0]
    return tail.strip()


def _ef_text_desert(term: dict) -> str:
    """Ecological Function, recovered verbatim from the FLAG-002 parking."""
    for edge in term.get("field_relations", []):
        note = edge.get("note", "")
        if EF_MARKER_desert in note:
            return note.split(EF_MARKER_desert, 1)[1].strip()
    return ""


def _related_terms_desert(term: dict, terms: dict[str, dict]) -> str:
    """Record-backed Related Terms only (partner terms with no record are
    an S2.9 CO; the diff classifies the shortfall)."""
    seen, names = set(), []
    for edge in term.get("field_relations", []):
        tid = edge.get("target_id")
        if tid and tid in terms and tid not in seen:
            seen.add(tid)
            # chunk Related Terms use the bare term name (before any gloss),
            # with no spaces around slashes (deployed style)
            names.append(terms[tid]["term"].split(" (")[0].replace(" / ", "/"))
    return ", ".join(names)


def render_lexicon_desert(rec, body, term_names, world_code, terms=None):
    term = rec
    r = term.get("retrieval", {})
    rw = "; ".join(r.get("retrieve_when", []))
    dnrw_items = [c["text"] for c in r.get("do_not_retrieve_when", [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    distortion = f"{term.get('modern_hearing', '')} {term.get('distortion_risk', '')}".strip()
    key_sources = " ".join(
        s.get("author_gravity_note", "").strip()
        for s in term.get("sources", []) if s.get("author_gravity_note"))
    lines = [
        "---",
        f"Term: {term['term']}",
        f"World-Code: {world_code}",
        f"Tier: [{r.get('tier', '')}]",
        f"Aliases: {', '.join(term.get('aliases', []))}",
        f"Related Terms: {_related_terms_desert(term, terms)}",
        f"Retrieve-When: {rw}",
        f"Do-Not-Retrieve-When: {dnrw}",
        "---",
        "",
        f"**Quick Meaning:** {term.get('quick_meaning', '')}",
        "",
        f"**World Meaning:** {term.get('world_meaning', '')}",
        "",
        f"**Ecological Function:** {_ef_text_desert(term)}",
        "",
        f"**Distortion Risk:** {distortion}",
        "",
        f"**Key Sources:** {key_sources}",
    ]
    return "\n".join(lines) + "\n"


def render_story_desert(rec, body, world_code):
    story = rec
    r = story.get("retrieval", {})
    rw = "; ".join(r.get("retrieve_when", []))
    dnrw_items = [c["text"] for c in r.get("do_not_retrieve_when", [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    srcs = story.get("sources", [])
    confidence = srcs[0].get("author_gravity_note", "") if srcs else ""
    source_line = ""
    for s in srcs[1:]:
        note = s.get("author_gravity_note", "")
        if note.startswith("Source line (chunk): "):
            source_line = note[len("Source line (chunk): "):]
    # voice_surface = telling-formula + " Usage guidance (chunk, verbatim): " + usage
    usage = ""
    vs = story.get("voice_surface", "")
    m = re.search(r"Usage guidance \(chunk, verbatim\): (.*)", vs, re.S)
    if m:
        usage = m.group(1).strip()
    parts = [
        "## Retrieval Front-Matter",
        "",
        "```",
        f"Story-Title:    {story['title']}",
        f"World-Code:     {world_code}",
        f"Tier:           {story['narrative_tier']['tier']}",
        # Key-Line / Signature: palette supply-side (worklist 4b), rolled to
        # this world 2026-08-09. Verbatim from the record's own text.
        *( [f"Signature:      yes"] if story.get("signature") else [] ),
        *( [f'Key-Line:       "{story["key_line"]}"'] if story.get("key_line") else [] ),
        f"Confidence:     {confidence}",
        f"Source:         {source_line}",
        f"Retrieve-When:  {rw}",
        f"Do-Not-Retrieve-When: {dnrw}",
        "```",
        "",
        "---",
        "",
        "## Story Text",
        "",
        story.get("text", ""),
        "",
        "---",
        "",
        "## Formation Ecology Connection",
        "",
        # CO-P2-04: the FEC prose lives verbatim on the first
        # gravity_links note (typed home; parking retired)
        (story.get("gravity_links") or [{}])[0].get("note",
            _parked_desert(story.get("_body", ""), FEC_DELIM_desert)),
        "",
        "---",
        "",
        "## Tier Justification",
        "",
        story["narrative_tier"].get("justification", ""),
        "",
        "---",
        "",
        "## Usage Guidance",
        "",
        usage,
    ]
    # CO-P2-04: Source Identification renders from the per-element
    # sources[] entries (SS3.3 tier-4 rule); parking retired
    element_entries = []
    for s in story.get("sources", []):
        note = s.get("author_gravity_note", "")
        if note.startswith("Element from Story Text: ") and "|| Source: " in note:
            element_entries.append(note)
    if element_entries:
        lines = ["", "---", "", "## Source Identification", ""]
        for i, note in enumerate(element_entries):
            el = note.split("Element from Story Text: ", 1)[1].split(" || ", 1)[0]
            src = note.split("|| Source: ", 1)[1]
            src = src.split(" (SS3.3 tier-4 rule backfill", 1)[0]
            block = f"**Element from Story Text:** {el}\n**Source:** {src}"
            lines.append(block)
            lines.append("")
        # trailing removal Note rides on the last element entry
        last = element_entries[-1]
        if "|| Note: " in last:
            lines.append(f"**Note:** {last.split('|| Note: ', 1)[1]}")
        while lines and lines[-1] == "":
            lines.pop()
        parts += lines
    else:
        src_ident = _parked_desert(story.get("_body", ""), SRC_DELIM_desert)
        if src_ident:
            parts += ["", "---", "", "## Source Identification", "", src_ident]
    return "\n".join(parts) + "\n"




def deployed_name_desert(rid: str, deployed_dir: Path, term: str = "") -> str:
    for p in ():
        if p.stem.split("_")[0] == rid:
            return p.name
    # New record with no deployed counterpart (CO-P2-03 onward): derive a
    # slug from the bare term name, matching the deployed convention
    # (desertlex010_xeniteia.md)
    slug = re.sub(r"[^a-z0-9]+", "-",
                  term.split(" (")[0].lower()
                      .replace("ō", "o").replace("ē", "e")).strip("-")
    if not slug:
        raise FileNotFoundError(f"no deployed chunk for {rid} and no term")
    return f"{rid}_{slug}.md"




EF_MARK_pahc = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "
USAGE_MARK_pahc = "Usage guidance (chunk, verbatim): "
FEC_LINK_MARK_pahc = "(the S2.4 parking, converted at S2.5): "
FEC_PARK_RE_pahc = re.compile(
    r"\[Formation Ecology Connection - parked at the S2\.4-equivalent"
    r"[^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
SRCID_PARK_RE_pahc = re.compile(
    r"\[Source Identification - [^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
PARK_RE_pahc = re.compile(
    r"\[([^\]]+?) - parked at the S2\.2-equivalent[^\]]*\]\s*", re.S)

THIN_pahc = {"pahclex012", "pahclex013"}


def fm_block_pahc(pairs, width=22):
    lines = []
    for k, v in pairs:
        if v is None:
            continue
        key = k + ":"
        lines.append(f"{key.ljust(width)}{v}" if len(key) < width
                     else f"{key} {v}")
    return "## Retrieval Front-Matter\n\n```\n" + "\n".join(lines) + "\n```"


def render_lexicon_pahc(rec, body, term_names, world_code):
    rid = rec["id"]
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    # RELATED-TERMS DISPLAY CONVENTION (the PAHC lesson, twinned with
    # HAL's token-leak lesson): the deployed line is the chunk
    # authors' CURATED DISPLAY membership - the record graph is richer
    # (symmetric by gate law) and rendering every edge leaks
    # query-relevant tokens onto the wrong chunk (measured: 'prophetes'
    # on the episkopos view demoted PAHC-TH-03's golden must). The
    # view keeps the deployed display list VERBATIM, mechanically
    # asserted to be a SUBSET of the record graph (the S2.3 correction
    # guarantees coverage); the graph remains the queryable truth.
    dep_line = rec.get("chunk_related_line", "")
    edge_targets = {e.get("target_id")
                    for e in rec.get("field_relations") or []}
    for name in [x.strip() for x in dep_line.split(",") if x.strip()]:
        hits = [rid_ for rid_, tname in term_names.items()
                if name.lower() in tname.lower()
                or tname.lower().startswith(name.lower())]
        assert any(h in edge_targets for h in hits) or not hits, (
            rec["id"], name)
    related = [x.strip() for x in dep_line.split(",") if x.strip()]
    ef = ""
    for e in rec.get("field_relations") or []:
        note = e.get("note") or ""
        j = note.find(EF_MARK_pahc)
        if j >= 0:
            ef = note[j + len(EF_MARK_pahc):].strip()
            break
    parts = [fm_block_pahc([
        ("Term", rec.get("term", "")),
        ("World-Code", world_code),
        ("Tier", str(ret.get("tier", 1))),
        ("Aliases", ", ".join(rec.get("aliases") or [])),
        ("Related-Terms", ", ".join(related) if related else None),
        ("Retrieve-When", rw),
        ("Do-Not-Retrieve-When", dnrw),
    ])]
    parts.append("## Quick Meaning\n\n" + rec.get("quick_meaning", ""))
    if rid not in THIN_pahc:
        wm = rec.get("world_meaning", "")
        j = wm.find("\n\n[Ecological Function - parked")
        if j >= 0:
            wm = wm[:j].strip()
        if wm:
            parts.append("## World Meaning\n\n" + wm)
        if ef:
            parts.append("## Ecological Function\n\n" + ef)
        dr = ("**Modern Hearing:**\n" + rec.get("modern_hearing", "")
              + "\n\n**World Hearing:**\n" + rec.get("distortion_risk", ""))
        parts.append("## Distortion Risk\n\n" + dr)
        key_sources = " ".join(s.get("author_gravity_note", "").strip()
                               for s in rec.get("sources") or []
                               if s.get("author_gravity_note"))
        if key_sources.strip() and not key_sources.startswith("Thin-format"):
            parts.append("## Key Sources\n\n" + key_sources.strip())
    else:
        # thin format: inline-labeled single-line DR halves
        dr = ("**Modern Hearing:** " + rec.get("modern_hearing", "")
              + "\n\n**World Hearing:** " + rec.get("distortion_risk", ""))
        parts.append("## Distortion Risk\n\n" + dr)
    for m in PARK_RE_pahc.finditer(body):
        start = m.end()
        nxt = body.find("\n\n[", start)
        text = body[start:nxt if nxt >= 0 else len(body)]
        for stop in ("\n\nMigrated at",):
            j = text.find(stop)
            if j >= 0:
                text = text[:j]
        parts.append(f"## {m.group(1).strip()}\n\n{text.strip()}")
    return "\n\n---\n\n".join(parts) + "\n"


def fm_story_pahc(pairs, width=16):
    lines = []
    for k, v in pairs:
        if v is None:
            continue
        key = k + ":"
        lines.append(f"{key.ljust(width)}{v}" if len(key) < width
                     else f"{key} {v}")
    return "\n".join(lines) + "\n\n---"


def render_story_pahc(rec, body, world_code):
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    locus = (rec.get("sources") or [{}])[0].get("locus", "")
    # Key-Line / Signature: the palette supply-side (worklist 4b, Mark's
    # license 2026-08-09, piloted on this world). key_line is a verbatim
    # quotable line lifted from the record's OWN text - never authored at
    # render time - so the voice can quote with validity and zero
    # fabrication risk; signature marks the world's most distinctive
    # stories for the curator's first reach. Both render into the chunk
    # header the story indexer serializes, so they arrive with retrieval.
    parts = [fm_story_pahc([
        ("Story-Title", rec.get("title", "")),
        ("World-Code", world_code),
        ("Tier", str(ret.get("tier", 1))),
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
        j = note.find(FEC_LINK_MARK_pahc)
        fec = note[j + len(FEC_LINK_MARK_pahc):].strip() if j >= 0 else note
    else:
        m = FEC_PARK_RE_pahc.search(body)   # the declared 009/013 fallback
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
    j = vs.find(USAGE_MARK_pahc)
    usage = vs[j + len(USAGE_MARK_pahc):].strip() if j >= 0 else ""
    parts.append("## Usage Guidance\n\n" + usage)
    m = SRCID_PARK_RE_pahc.search(body)
    if m:
        text = m.group(1).strip()
        j = text.find("\n\nMigrated at")
        if j >= 0:
            text = text[:j].strip()
        parts.append("## Source Identification\n\n" + text)
    return "\n\n".join(parts) + "\n"




EF_MARK_hal = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "
USAGE_MARK_hal = "Usage guidance (chunk, verbatim): "
FEC_LINK_MARK_hal = "(the S2.4 parking, converted at S2.5): "
FEC_PARK_RE_hal = re.compile(
    r"\[Formation Ecology Connection - parked at the S2\.4-equivalent"
    r"[^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
SRCID_PARK_RE_hal = re.compile(
    r"\[Source Identification - [^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
ABSENT_PARK_RE_hal = re.compile(
    r"\[Absent Story Note - [^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
PARK_RE_hal = re.compile(
    r"\[([^\]]+?) - parked at the S2\.2-equivalent[^\]]*\]\s*", re.S)

NEVER_BUILT_hal = {"hallex03": ["Xenodochium"],
               "hallex12": ["Praeceptor"],
               "hallex14": ["Xenodochium"],
               "hallex15": ["Monasterium duplex", "Praeceptor"]}


def _unused_load_records(subdir):
    out = {}
    for p in sorted((RECORDS / subdir).glob("*.md")):
        txt = p.read_text(encoding="utf-8")
        assert txt.startswith("---\n"), p
        front, sep, body = txt[4:].partition("\n---\n")
        assert sep, p
        rec = yaml.safe_load(front)
        out[rec["id"]] = (rec, body.strip(), p)
    return out


def parked_sections_hal(body: str):
    hits = list(PARK_RE_hal.finditer(body))
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


def fm_lexicon_hal(pairs):
    # width-20 alignment with a guaranteed single space (the
    # Do-Not-Retrieve-When key is 21 chars - '<20' alone would butt the
    # value against the colon, which the runtime indexer must not see)
    lines = [f"{(k + ':').ljust(20)}{v}" if len(k) + 1 < 20
             else f"{k}: {v}" for k, v in pairs if v is not None]
    return "---\n" + "\n".join(lines) + "\n\n---"


def fm_story_hal(pairs):
    lines = [f"{k+':':<16}{v}" for k, v in pairs if v is not None]
    return "\n".join(lines) + "\n\n---"


def render_lexicon_hal(rec, body, term_names, world_code):
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
        j = note.find(EF_MARK_hal)
        if j >= 0:
            ef = note[j + len(EF_MARK_hal):].strip()
            break
    if not ef:
        # EF parked in world_meaning (hallex15, no edges - declared)
        m = re.search(r"\[Ecological Function - parked[^\]]*\]:\s*(.*)",
                      rec.get("world_meaning", ""), re.S)
        if m:
            ef = m.group(1).strip()
    parts = [fm_lexicon_hal([
        ("Term", rec.get("term", "")),
        ("World-Code", world_code),
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
    for title, text in parked_sections_hal(body):
        parts.append(f"## {title}\n\n{text}")
    # the front-matter fence already closes with '---'; sections join
    # with the deployed inter-section separator (no doubled fence)
    return parts[0] + "\n\n" + "\n\n---\n\n".join(parts[1:]) + "\n"


def render_story_hal(rec, body, world_code):
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    locus = (rec.get("sources") or [{}])[0].get("locus", "")
    j = locus.find("): ")
    if locus.startswith("Composite - elements per") and j >= 0:
        locus = locus[j + 3:]
    # Key-Line / Signature: the palette supply-side (worklist 4b), rolled to
    # this world 2026-08-09. key_line is a verbatim quotable line lifted from
    # the record's OWN text - never authored at render time - so the voice can
    # quote with validity and zero fabrication risk; signature marks this
    # world's most distinctive stories for the curator's first reach.
    parts = [fm_story_hal([
        ("Story-Title", rec.get("title", "")),
        ("World-Code", world_code),
        ("Tier", str(ret.get("tier", 1))),
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
        j = note.find(FEC_LINK_MARK_hal)
        fec = note[j + len(FEC_LINK_MARK_hal):].strip() if j >= 0 else note
    else:
        m = FEC_PARK_RE_hal.search(body)  # the declared 08/09/10 fallback
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
    j = vs.find(USAGE_MARK_hal)
    usage = vs[j + len(USAGE_MARK_hal):].strip() if j >= 0 else ""
    parts.append("## Usage Guidance\n\n" + usage)
    for regex, title in ((SRCID_PARK_RE_hal, "Source Identification"),
                         (ABSENT_PARK_RE_hal, "Absent Story Note")):
        m = regex.search(body)
        if m:
            text = m.group(1).strip()
            for stop in ("\n\n[Absent Story", "\n\nMigrated at"):
                j = text.find(stop)
                if j >= 0:
                    text = text[:j].strip()
            parts.append(f"## {title}\n\n{text}")
    return "\n\n".join(parts) + "\n"




EF_MARK_ijc = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "
USAGE_MARK_ijc = "Usage guidance (chunk, verbatim): "
FEC_LINK_MARK_ijc = "converted at S2.5): "
FEC_PARK_RE_ijc = re.compile(
    r"\[Formation Ecology Connection[^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
PARK_RE_ijc = re.compile(
    r"\[([A-Za-z -]+?) - parked (?:at the S2\.[24]-equivalent|verbatim as assembly provenance)[^\]]*\]\s*", re.S)


def parked_sections_ijc(body):
    secs = {}
    for m in PARK_RE_ijc.finditer(body):
        start = m.end()
        nxt = body.find("\n\n[", start)
        text = body[start:nxt if nxt >= 0 else len(body)]
        for stop in ("\n\nMigrated at",):
            j = text.find(stop)
            if j >= 0:
                text = text[:j]
        secs[m.group(1).strip()] = text.strip()
    return secs


def fm_block_ijc(pairs, width):
    lines = []
    for k, v in pairs:
        if v is None or v == "":
            continue
        key = k + ":"
        lines.append(f"{key.ljust(width)}{v}" if len(key) < width
                     else f"{key} {v}")
    return ("## Retrieval Front-Matter\n\n```\n"
            + "\n\n".join(lines) + "\n```")


def render_lexicon_ijc(rec, body, term_names, world_code):
    rid = rec["id"]
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    parks = parked_sections_ijc(body)

    ef = ""
    for e in rec.get("field_relations") or []:
        note = e.get("note") or ""
        j = note.find(EF_MARK_ijc)
        if j >= 0:
            ef = note[j + len(EF_MARK_ijc):]
            # the EF verbatim runs to the edge-note's own addendum
            for stop in (" The A/B strand contest", " Symmetric mirror",
                         " The mechanism behind", " Inverse pair",
                         " The two formulas", " What haeresis",
                         " 'Primatus made", " The doctrinal",
                         " The council is"):
                k = ef.find(stop, 1)
                if k > 0:
                    ef = ef[:k]
            break

    parts = [fm_block_ijc([
        ("Term", rec.get("term", "")),
        ("World-Code", world_code),
        ("Tier", str(ret.get("tier", 1))),
        # comma-containing aliases keep the deployed quoting convention
        # so the runtime parse never splits them at the internal comma
        ("Aliases", ", ".join(f'"{a}"' if "," in a else a
                              for a in rec.get("aliases") or [])),
        ("Related-Terms", rec.get("chunk_related_line", "")),
        ("Retrieve-When", rw),
        ("Do-Not-Retrieve-When", dnrw),
    ], 20)]
    parts.append("## Quick Meaning\n\n" + rec.get("quick_meaning", ""))
    wm = rec.get("world_meaning", "")
    j = wm.find("\n\n[Ecological Function - parked")
    if j >= 0:
        wm = wm[:j].strip()
    parts.append("## World Meaning\n\n" + wm)
    if "Plural-Voices Note" in parks:
        parts.append("## Plural-Voices Note\n\n"
                     + parks["Plural-Voices Note"])
    if ef:
        parts.append("## Ecological Function\n\n" + ef.strip())
    dr = ("**Modern Hearing:**\n" + rec.get("modern_hearing", "")
          + "\n\n**World Hearing:**\n" + rec.get("distortion_risk", ""))
    parts.append("## Distortion Risk\n\n" + dr)
    key_sources = " ".join(s.get("author_gravity_note", "").strip()
                           for s in rec.get("sources") or []
                           if s.get("author_gravity_note")
                           and not s["author_gravity_note"].startswith(
                               "No Key Sources by design")
                           and not s["author_gravity_note"].startswith(
                               "Old St. Peter's"))
    if key_sources.strip():
        parts.append("## Key Sources\n\n" + key_sources.strip())
    for name in ("CT Contest Type", "Reported-Experience Status",
                 "Final Assembly Instruction"):
        if name in parks:
            parts.append(f"## {name}\n\n" + parks[name])
    return "\n\n---\n\n".join(parts) + "\n"


def render_story_ijc(rec, body, world_code):
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    parks = parked_sections_ijc(body)
    links = rec.get("gravity_links") or []
    if links:
        note = links[0]["note"]
        j = note.find(FEC_LINK_MARK_ijc)
        fec = note[j + len(FEC_LINK_MARK_ijc):].strip() if j >= 0 else note
    else:
        m = FEC_PARK_RE_ijc.search(body)   # ijcstory003, unlinked by design
        fec = m.group(1).strip() if m else ""
        j = fec.find("\n\n[")
        if j >= 0:
            fec = fec[:j].strip()
    vs = rec.get("voice_surface", "")
    j = vs.find(USAGE_MARK_ijc)
    usage = vs[j + len(USAGE_MARK_ijc):].strip() if j >= 0 else vs

    parts = [fm_block_ijc([
        ("Story-Title", rec.get("title", "")),
        ("World-Code", world_code),
        ("Tier", str(ret.get("tier", 1))),
        # Key-Line / Signature: palette supply-side (worklist 4b), rolled to
        # this world 2026-08-09. Verbatim from the record's own text.
        ("Signature", "yes" if rec.get("signature") else None),
        ("Key-Line", ('"' + rec["key_line"] + '"') if rec.get("key_line") else None),
        ("Confidence", rec.get("confidence_line") or None),
        ("Source", rec.get("attested_occasion", "")),
        ("Retrieve-When", rw),
        ("Do-Not-Retrieve-When", dnrw),
    ], 16)]
    parts.append("## Story Text\n\n" + rec.get("text", ""))
    if fec:
        parts.append("## Formation Ecology Connection\n\n" + fec)
    parts.append("## Tier Justification\n\n"
                 + (rec.get("narrative_tier") or {}).get("justification", ""))
    parts.append("## Usage Guidance\n\n" + usage)
    if "Final Assembly Instruction" in parks:
        parts.append("## Final Assembly Instruction\n\n"
                     + parks["Final Assembly Instruction"])
    return "\n\n---\n\n".join(parts) + "\n"






def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--world", required=True, choices=sorted(WORLDS))
    ap.add_argument("--parity", help="deployed data dir to byte-compare chunk sets against")
    args = ap.parse_args()
    w = WORLDS[args.world]
    world_code = w["world_code"]
    records_root = ROOT / "records" / w["records_dir"]

    terms = load_records(records_root, "term")
    stories = load_records(records_root, "story")
    ambient = load_records(records_root, "ambient")
    term_names = {rid: rec["term"] for rid, (rec, _b, _p) in terms.items()}

    out_root = ROOT / "deploy" / args.world
    counts = {}
    style = w.get("chunk_style", "syr")
    if style == "alx":
        lex_render = lambda rec, body: render_lexicon_alx(rec, body, term_names, world_code)
        story_render = lambda rec, body: render_story_alx(rec, world_code)
    elif style == "desert":
        full = {rid: dict(rec, _body=body) for rid, (rec, body, _p) in terms.items()}
        lex_render = lambda rec, body: render_lexicon_desert(dict(rec, _body=body), body, term_names, world_code, terms=full)
        story_render = lambda rec, body: render_story_desert(dict(rec, _body=body), body, world_code)
    elif style == "pahc":
        lex_render = lambda rec, body: render_lexicon_pahc(rec, body, term_names, world_code)
        story_render = lambda rec, body: render_story_pahc(rec, body, world_code)
    elif style == "hal":
        lex_render = lambda rec, body: render_lexicon_hal(rec, body, term_names, world_code)
        story_render = lambda rec, body: render_story_hal(rec, body, world_code)
    elif style == "ijc":
        lex_render = lambda rec, body: render_lexicon_ijc(rec, body, term_names, world_code)
        story_render = lambda rec, body: render_story_ijc(rec, body, world_code)
    else:
        lex_render = lambda rec, body: render_lexicon(rec, body, term_names, world_code)
        story_render = lambda rec, body: render_story(rec, body, world_code)
    for sub, items, render in (
            ("lexicon_chunks", terms, lex_render),
            ("story_chunks", stories, story_render),
            ("ambient_chunks", ambient,
             lambda rec, body: render_ambient(rec, world_code))):
        out = out_root / sub
        out.mkdir(parents=True, exist_ok=True)
        n = 0
        for rid, (rec, body, _p) in items.items():
            if rec.get("chunk_filename"):
                fname = rec["chunk_filename"]
            else:
                slug = rec.get("chunk_slug") or _ambient_slug(rec.get("title", ""))
                fname = f"{rid}_{slug}.md"
            (out / fname).write_text(
                render(rec, body), encoding="utf-8", newline="\n")
            n += 1
        counts[sub] = n
    print("built " + ", ".join(f"{v} {k}" for k, v in counts.items()))

    if args.parity:
        import filecmp
        deployed = Path(args.parity)
        bad = []
        for sub in counts:
            d_old, d_new = deployed / sub, out_root / sub
            old_files = sorted(p.name for p in d_old.glob("*.md"))
            new_files = sorted(p.name for p in d_new.glob("*.md"))
            if old_files != new_files:
                bad.append(f"{sub}: file sets differ "
                           f"(only-old={set(old_files)-set(new_files)}, "
                           f"only-new={set(new_files)-set(old_files)})")
                continue
            for name in old_files:
                if not filecmp.cmp(d_old / name, d_new / name, shallow=False):
                    bad.append(f"{sub}/{name}: bytes differ")
        if bad:
            print("PARITY: FAIL")
            for b in bad:
                print("  " + b)
            return 1
        print(f"PARITY: byte-identical to deployed "
              f"({sum(counts.values())} files across {len(counts)} sets)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
