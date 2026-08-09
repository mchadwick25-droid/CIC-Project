"""S6.2/PAHC S2.8-equivalent - PAHC chunk views: regenerate the deployed
chunk formats from records.

Writes into wrs/views/staging/pahc_world/ - deployed files untouched
until the parities are green (the standing swap rule).

PAHC format specifics, each declared:
- LEXICON: the SYR/ALX-style '## Retrieval Front-Matter' code fence,
  sections separated by '---'; the Distortion Risk section
  round-trips as '**Modern Hearing:**' + modern_hearing +
  '**World Hearing:**' + distortion_risk (the record's
  distortion_risk field carries the World-Hearing text PLUS the
  Living Tradition Note and chunk-attested Confidence sub-blocks
  verbatim - the S2.2 split's content-preserving shape).
- THIN-FORMAT chunks (pahclex012/013): front matter + Quick Meaning +
  Distortion Risk only; their DR is inline-labeled single-line form.
- ALIASES: the S2.2 RULE-A DROP TABLE IS THE CLASSIFICATION
  AUTHORITY (declared at S2.2): the deployed lines still carry the 7
  born-dropped surfaces until this swap regenerates them.
- STORY: bare front matter (Story-Title/World-Code/Tier/Confidence/
  Source/Retrieve-When/Do-Not-Retrieve-When) closed by one '---';
  sections with no separators; Source lines verbatim from
  sources[0].locus (all sources share the one locus - the Registry-
  tag extraction preserved it); FEC from gravity_links[0] with the
  BODY-PARKING FALLBACK for pahcstory009/013 (their own FECs name no
  gravity); the composites' Source Identification tables re-rendered.
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

RECORDS = BACKEND / "wrs" / "records" / "pahc_world"
STAGING = HERE / "staging" / "pahc_world"
DEPLOYED_LEX = BACKEND / "data" / "pahc_world" / "lexicon_chunks"
DEPLOYED_STORY = BACKEND / "data" / "pahc_world" / "story_chunks"

EF_MARK = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "
USAGE_MARK = "Usage guidance (chunk, verbatim): "
FEC_LINK_MARK = "(the S2.4 parking, converted at S2.5): "
FEC_PARK_RE = re.compile(
    r"\[Formation Ecology Connection - parked at the S2\.4-equivalent"
    r"[^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
SRCID_PARK_RE = re.compile(
    r"\[Source Identification - [^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
PARK_RE = re.compile(
    r"\[([^\]]+?) - parked at the S2\.2-equivalent[^\]]*\]\s*", re.S)

THIN = {"pahclex012", "pahclex013"}


def _deployed_related():
    out = {}
    for p in DEPLOYED_LEX.glob("*.md"):
        t = p.read_text(encoding="utf-8")
        m = re.search(r"^Related-Terms:\s*(.*)$", t, re.M)
        out[p.stem.split("_")[0]] = m.group(1).strip() if m else ""
    return out


DEPLOYED_RELATED = _deployed_related()


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


def fm_block(pairs, width=22):
    lines = []
    for k, v in pairs:
        if v is None:
            continue
        key = k + ":"
        lines.append(f"{key.ljust(width)}{v}" if len(key) < width
                     else f"{key} {v}")
    return "## Retrieval Front-Matter\n\n```\n" + "\n".join(lines) + "\n```"


def render_lexicon(rec, body, term_names):
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
    dep_line = DEPLOYED_RELATED.get(rec["id"], "")
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
        j = note.find(EF_MARK)
        if j >= 0:
            ef = note[j + len(EF_MARK):].strip()
            break
    parts = [fm_block([
        ("Term", rec.get("term", "")),
        ("World-Code", "pahc"),
        ("Tier", str(ret.get("tier", 1))),
        ("Aliases", ", ".join(rec.get("aliases") or [])),
        ("Related-Terms", ", ".join(related) if related else None),
        ("Retrieve-When", rw),
        ("Do-Not-Retrieve-When", dnrw),
    ])]
    parts.append("## Quick Meaning\n\n" + rec.get("quick_meaning", ""))
    if rid not in THIN:
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
    for m in PARK_RE.finditer(body):
        start = m.end()
        nxt = body.find("\n\n[", start)
        text = body[start:nxt if nxt >= 0 else len(body)]
        for stop in ("\n\nMigrated at",):
            j = text.find(stop)
            if j >= 0:
                text = text[:j]
        parts.append(f"## {m.group(1).strip()}\n\n{text.strip()}")
    return "\n\n---\n\n".join(parts) + "\n"


def fm_story(pairs, width=16):
    lines = []
    for k, v in pairs:
        if v is None:
            continue
        key = k + ":"
        lines.append(f"{key.ljust(width)}{v}" if len(key) < width
                     else f"{key} {v}")
    return "\n".join(lines) + "\n\n---"


def render_story(rec, body):
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
    parts = [fm_story([
        ("Story-Title", rec.get("title", "")),
        ("World-Code", "pahc"),
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
        j = note.find(FEC_LINK_MARK)
        fec = note[j + len(FEC_LINK_MARK):].strip() if j >= 0 else note
    else:
        m = FEC_PARK_RE.search(body)   # the declared 009/013 fallback
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
        text = m.group(1).strip()
        j = text.find("\n\nMigrated at")
        if j >= 0:
            text = text[:j].strip()
        parts.append("## Source Identification\n\n" + text)
    return "\n\n".join(parts) + "\n"


def main():
    terms = load_records("term")
    stories = load_records("story")
    term_names = {rid: rec["term"] for rid, (rec, _b, _p) in terms.items()}

    lex_out = STAGING / "lexicon_chunks"
    story_out = STAGING / "story_chunks"
    lex_out.mkdir(parents=True, exist_ok=True)
    story_out.mkdir(parents=True, exist_ok=True)

    deployed_lex = {p.stem.split("_")[0]: p.name
                    for p in DEPLOYED_LEX.glob("*.md")}
    deployed_story = {p.stem.split("_")[0]: p.name
                      for p in DEPLOYED_STORY.glob("*.md")}

    n_lex = n_story = 0
    for rid, (rec, body, _p) in terms.items():
        name = deployed_lex.get(rid)
        assert name, rid
        (lex_out / name).write_text(render_lexicon(rec, body, term_names),
                                    encoding="utf-8", newline="\n")
        n_lex += 1
    for rid, (rec, body, _p) in stories.items():
        name = deployed_story.get(rid)
        assert name, rid
        (story_out / name).write_text(render_story(rec, body),
                                      encoding="utf-8", newline="\n")
        n_story += 1
    print(f"staged {n_lex} lexicon + {n_story} story chunk views -> "
          f"{STAGING}")


if __name__ == "__main__":
    main()
