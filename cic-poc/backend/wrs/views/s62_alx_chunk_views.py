"""S6.2 S2.8-equivalent - Alexandria chunk views: regenerate the deployed
chunk formats from records (Pass 1 SS3.9; Desert chunk_views.py precedent,
ported to Alexandria's richer chunk format).

Writes into wrs/views/staging/alexandria_world/ - deployed files untouched
until the parities are green (blueprint S2.8 swap rule; the swap call is
Mark's at the S2.9-equivalent).

Round-trip design (the S2.2/S2.3/S2.4 migrations were built to preserve
this; the parity script classifies every difference):
- lexicon front matter: term/aliases/tier/retrieve-when from record
  fields; Related-Terms from RECORD-BACKED field_relations targets only
  (the deployed line's extra partners are the declared S2.9
  render-shortfall CO); Tags NOT rendered (retired, CO-P2-09).
- Quick Meaning <- quick_meaning; World Meaning <- world_meaning;
  Ecological Function <- the FLAG-002 verbatim text on the first
  field_relations edge note carrying the absorption marker;
  Distortion Risk <- modern_hearing + distortion_risk (labels in-value);
  Key Sources <- sources[].author_gravity_note spans concatenated in
  order (the S2.2 split put every character in exactly one span);
  Related-Terms Reciprocity Note + special sections <- the body parkings,
  verbatim.
- story chunks: title/tier from record; Source line <- sources[0].locus
  (verbatim by construction); Story Text <- text; Formation Ecology
  Connection <- gravity_links[0].note (CO-P2-04 - the FEC's record home);
  Tier Justification <- narrative_tier.justification; Usage Guidance <-
  voice_surface after the verbatim marker. The deployed Confidence line
  has NO record home - not rendered (parity classifies it; S2.9 CO
  candidate).
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

RECORDS = BACKEND / "wrs" / "records" / "alexandria_world"
STAGING = HERE / "staging" / "alexandria_world"
DEPLOYED_LEX = BACKEND / "data" / "alexandria_world" / "lexicon_chunks"
DEPLOYED_STORY = BACKEND / "data" / "alexandria_world" / "story_chunks"

EF_MARK = ("Chunk Ecological Function (verbatim, absorbed per "
           "FLAG-002): ")
USAGE_MARK = "Usage guidance (chunk, verbatim): "
PARK_RE = re.compile(
    r"\[([^\]]+?) — parked at the S2\.2-equivalent[^\]]*\]\s*", re.S)


def load_records(subdir):
    out = {}
    for p in sorted((RECORDS / subdir).glob("*.md")):
        txt = p.read_text(encoding="utf-8")
        assert txt.startswith("---\n"), p
        front, sep, body = txt[4:].partition("\n---\n")
        assert sep, p
        rec = yaml.safe_load(front)
        out[rec["id"]] = (rec, body.strip())
    return out


def parked_sections(body: str):
    """Extract the parked sections: [(title, text), ...] in body order."""
    hits = list(PARK_RE.finditer(body))
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
    parts = [fm_block([
        ("Term", rec.get("term", "")),
        ("World-Code", "alex"),
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
    for title, text in parked_sections(body):
        parts.append(f"## {title}\n\n{text}")
    return "\n\n---\n\n".join(parts) + "\n"


def render_story(rec):
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    locus = (rec.get("sources") or [{}])[0].get("locus", "")
    parts = [fm_block([
        ("Story-Title", rec.get("title", "")),
        ("World-Code", "alex"),
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
    j = vs.find(USAGE_MARK)
    usage = vs[j + len(USAGE_MARK):].strip() if j >= 0 else ""
    parts.append("## Usage Guidance\n\n" + usage)
    return "\n\n---\n\n".join(parts) + "\n"


def main():
    terms = load_records("term")
    stories = load_records("story")
    term_names = {rid: rec["term"] for rid, (rec, _b) in terms.items()}

    lex_out = STAGING / "lexicon_chunks"
    story_out = STAGING / "story_chunks"
    lex_out.mkdir(parents=True, exist_ok=True)
    story_out.mkdir(parents=True, exist_ok=True)

    # staged files keep the deployed filenames (retrieval-parity requirement)
    deployed_lex = {p.stem.split("_")[0]: p.name for p in DEPLOYED_LEX.glob("*.md")}
    deployed_story = {p.stem.split("_")[0]: p.name for p in DEPLOYED_STORY.glob("*.md")}

    # CO-P2-15: the five governed-CT records have no deployed chunk yet -
    # the view synthesizes their filenames (new-at-swap chunks, declared
    # in the parity artifact; the render-parity instrument iterates
    # deployed files, so these are additions, not diffs)
    NEW_SLUGS = {"alexlex051": "alexlex051_apokatastasis.md",
                 "alexlex059": "alexlex059_catechetical-school.md",
                 "alexlex074": "alexlex074_fall-descent.md",
                 "alexlex081": "alexlex081_homoousios.md",
                 "alexlex090": "alexlex090_logikos.md"}
    n_lex = n_story = 0
    for rid, (rec, body) in terms.items():
        name = deployed_lex.get(rid) or NEW_SLUGS.get(rid)
        assert name, f"{rid}: no deployed chunk filename and no declared slug"
        (lex_out / name).write_text(render_lexicon(rec, body, term_names),
                                    encoding="utf-8", newline="\n")
        n_lex += 1
    for rid, (rec, _body) in stories.items():
        name = deployed_story.get(rid)
        assert name, f"{rid}: no deployed chunk filename"
        (story_out / name).write_text(render_story(rec),
                                      encoding="utf-8", newline="\n")
        n_story += 1
    print(f"staged {n_lex} lexicon + {n_story} story chunk views -> {STAGING}")


if __name__ == "__main__":
    main()
