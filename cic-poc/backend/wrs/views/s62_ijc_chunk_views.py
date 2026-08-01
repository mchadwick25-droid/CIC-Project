"""S6.2/IJC S2.8-equivalent - IJC chunk views: regenerate the deployed
chunk formats from records into wrs/views/staging/imperial_juridical_world/.

IJC format specifics, each declared:
- FRONT MATTER: fenced block with a BLANK LINE between every field
  (the fleet's third dialect); lexicon key column 20 wide, story 16
  wide (Do-Not-Retrieve-When exceeds both and takes a single space).
- LEXICON sections in the deployed per-chunk order, separated by
  `---` rules: Quick Meaning / World Meaning / [Plural-Voices Note] /
  Ecological Function / Distortion Risk (**Modern Hearing:** and
  **World Hearing:** each on its own line, text on the next) /
  [Key Sources] / [CT Contest Type] / [Reported-Experience Status] /
  Final Assembly Instruction. Optional sections render only where the
  record's body parkings carry them; EF renders from the first
  edge's FLAG-002 verbatim (011/012 have none by design).
- ALIASES: the staged lines are the S2.2 AUTHORED lists - the
  FLAG-035 fixes ('Arian' gone from 003; the in/out idiom and
  parenthetical qualifiers resolved) land in production AT THE SWAP;
  render parity classifies via the S2.2 authoring tables.
- Tags retired (CO-P2-09) - absent from staged lines.
- STORY: front matter (Story-Title/World-Code/Tier/Confidence/Source/
  Retrieve-When/Do-Not-Retrieve-When) + `---` + Story Text /
  Formation Ecology Connection / Tier Justification / Usage Guidance
  / Final Assembly Instruction; FEC from gravity_links[0]'s CO-P2-04
  note (body-parking fallback for ijcstory003, unlinked by design);
  Source = attested_occasion verbatim.
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

RECORDS = BACKEND / "wrs" / "records" / "imperial_juridical_world"
STAGING = HERE / "staging" / "imperial_juridical_world"
DEPLOYED_LEX = BACKEND / "data" / "imperial_juridical_world" / "lexicon_chunks"
DEPLOYED_STORY = BACKEND / "data" / "imperial_juridical_world" / "story_chunks"

EF_MARK = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "
USAGE_MARK = "Usage guidance (chunk, verbatim): "
FEC_LINK_MARK = "converted at S2.5): "
FEC_PARK_RE = re.compile(
    r"\[Formation Ecology Connection[^\]]*\]\s*(.*?)(?=\n\n\[|\Z)", re.S)
PARK_RE = re.compile(
    r"\[([A-Za-z -]+?) - parked (?:at the S2\.[24]-equivalent|verbatim as assembly provenance)[^\]]*\]\s*", re.S)


def load_records(subdir):
    out = {}
    for p in sorted((RECORDS / subdir).glob("*.md")):
        txt = p.read_text(encoding="utf-8")
        front, sep, body = txt[4:].partition("\n---\n")
        assert sep, p
        rec = yaml.safe_load(front)
        out[rec["id"]] = (rec, body.strip(), p)
    return out


def parked_sections(body):
    secs = {}
    for m in PARK_RE.finditer(body):
        start = m.end()
        nxt = body.find("\n\n[", start)
        text = body[start:nxt if nxt >= 0 else len(body)]
        for stop in ("\n\nMigrated at",):
            j = text.find(stop)
            if j >= 0:
                text = text[:j]
        secs[m.group(1).strip()] = text.strip()
    return secs


def fm_block(pairs, width):
    lines = []
    for k, v in pairs:
        if v is None or v == "":
            continue
        key = k + ":"
        lines.append(f"{key.ljust(width)}{v}" if len(key) < width
                     else f"{key} {v}")
    return ("## Retrieval Front-Matter\n\n```\n"
            + "\n\n".join(lines) + "\n```")


def render_lexicon(rec, body):
    rid = rec["id"]
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    parks = parked_sections(body)

    ef = ""
    for e in rec.get("field_relations") or []:
        note = e.get("note") or ""
        j = note.find(EF_MARK)
        if j >= 0:
            ef = note[j + len(EF_MARK):]
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

    parts = [fm_block([
        ("Term", rec.get("term", "")),
        ("World-Code", "ijc"),
        ("Tier", str(ret.get("tier", 1))),
        # comma-containing aliases keep the deployed quoting convention
        # so the runtime parse never splits them at the internal comma
        ("Aliases", ", ".join(f'"{a}"' if "," in a else a
                              for a in rec.get("aliases") or [])),
        ("Related-Terms", DEPLOYED_RELATED.get(rid, "")),
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


def render_story(rec, body):
    ret = rec.get("retrieval") or {}
    rw = "; ".join(ret.get("retrieve_when") or [])
    dnrw_items = [d["text"] for d in (ret.get("do_not_retrieve_when") or [])]
    dnrw = "; ".join(dnrw_items) if dnrw_items else "—"
    parks = parked_sections(body)
    links = rec.get("gravity_links") or []
    if links:
        note = links[0]["note"]
        j = note.find(FEC_LINK_MARK)
        fec = note[j + len(FEC_LINK_MARK):].strip() if j >= 0 else note
    else:
        m = FEC_PARK_RE.search(body)   # ijcstory003, unlinked by design
        fec = m.group(1).strip() if m else ""
        j = fec.find("\n\n[")
        if j >= 0:
            fec = fec[:j].strip()
    vs = rec.get("voice_surface", "")
    j = vs.find(USAGE_MARK)
    usage = vs[j + len(USAGE_MARK):].strip() if j >= 0 else vs

    parts = [fm_block([
        ("Story-Title", rec.get("title", "")),
        ("World-Code", "ijc"),
        ("Tier", str(ret.get("tier", 1))),
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


def _deployed_related():
    out = {}
    for p in DEPLOYED_LEX.glob("*.md"):
        t = p.read_text(encoding="utf-8")
        m = re.search(r"^Related-Terms:\s*(.*)$", t, re.M)
        out[p.stem.split("_")[0]] = m.group(1).strip() if m else ""
    return out


DEPLOYED_RELATED = _deployed_related()


def main():
    terms = load_records("term")
    stories = load_records("story")
    lex_out = STAGING / "lexicon_chunks"
    story_out = STAGING / "story_chunks"
    lex_out.mkdir(parents=True, exist_ok=True)
    story_out.mkdir(parents=True, exist_ok=True)

    deployed_lex = {p.stem.split("_")[0]: p.name
                    for p in DEPLOYED_LEX.glob("*.md")}
    deployed_story = {p.stem.split("_")[0]: p.name
                      for p in DEPLOYED_STORY.glob("*.md")}
    n = 0
    for rid, (rec, body, _p) in terms.items():
        (lex_out / deployed_lex[rid]).write_text(
            render_lexicon(rec, body), encoding="utf-8", newline="\n")
        n += 1
    for rid, (rec, body, _p) in stories.items():
        (story_out / deployed_story[rid]).write_text(
            render_story(rec, body), encoding="utf-8", newline="\n")
        n += 1
    print(f"staged {n} chunk views -> {STAGING}")


if __name__ == "__main__":
    main()
