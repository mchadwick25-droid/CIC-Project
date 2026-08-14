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
            slug = rec.get("chunk_slug") or _ambient_slug(rec.get("title", ""))
            (out / f"{rid}_{slug}.md").write_text(
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
