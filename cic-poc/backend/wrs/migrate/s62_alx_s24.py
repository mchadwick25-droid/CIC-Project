"""S6.2/Alexandria - S2.4-equivalent: stories + figures + quotes.

10 story chunks (data/alexandria_world/story_chunks/) -> story records;
12 figure records; 1 quote record. Mechanical where the chunk carries
the content (Story Text, Tier Justification, Usage Guidance, retrieval
front matter - all verbatim); authored-in-script where Desert's S2.4
authored (attested_occasion, tellable_as, owner assignment, the
voice_surface telling-frame).

Conventions ported from Desert S2.4:
- narrative_tier = {tier, justification(verbatim)}
- voice_surface = telling-frame + "Usage guidance (chunk, verbatim):" + text
- composite owners per CO-P2-06: a composite/pattern story is owned by
  the community itself, never a persona (alexfig011; the Coptic-martyrs
  group figure alexfig012 for the collective martyr memory).
- quote fidelity per the Arsenius precedent: the theosis formula is a
  standard rendering with no vetted translation row -> license
  paraphrase-only, translation_used honestly unset.

FEC HANDLING, DECLARED: Alexandria's chunks carry Formation Ecology
Connection as a real section (what Desert lost and FLAG-004 recovered).
Its record home is gravity_links (CO-P2-04) - but the Alexandria
gravity records do not exist yet (S2.5-equivalent). The FEC text is
therefore parked VERBATIM in each story record's body under a named
delimiter; the S2.5-equivalent converts the parkings into typed
gravity_links exactly as CO-P2-04 shaped them. Nothing dropped, gate
integrity kept (no dangling gravity ids).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

CHUNKS = BACKEND / "data" / "alexandria_world" / "story_chunks"
OUT = BACKEND / "wrs" / "records" / "alexandria_world"

FEC_DELIM = ("[Formation Ecology Connection — parked at the S2.4-equivalent; "
             "becomes typed gravity_links (CO-P2-04 shape) when the "
             "S2.5-equivalent authors the gravity records]")

SOURCE_KEYS = [
    ("Gregory Thaumaturgus", "srcALX007"), ("Palladius", "srcALX010"),
    ("Eusebius", "srcALX009"), ("Life of Antony", "srcALX004"),
    ("Athanasius", "srcALX003"), ("Apophthegmata", "srcALX011"),
    ("Clement", "srcALX001"), ("Origen", "srcALX002"),
    ("Coptic martyr", "srcALX025"), ("papyri", "srcALX025"),
]

# per-story authored fields (occasion; owner; tellable_as; telling frame)
STORY = {
 "alexstory001": dict(owner="alexfig004", tellable_as="scene",
  occasion="Gregory's formal address of thanksgiving at the close of his years of study under Origen at Caesarea, c. 238 CE (Address of Thanksgiving; Nautin dating caveat carried).",
  frame="We keep a student's own account of what it was to sit under this teacher - we tell it with his name on it, as his own composed thanks, in the elevated register the occasion asked of him."),
 "alexstory002": dict(owner="alexfig005", tellable_as="scene",
  occasion="Palladius's personal visits to the blind teacher Didymus in Alexandria, recounted in the Lausiac History (c. 419-420) as direct testimony.",
  frame="Palladius tells us himself of visiting the blind teacher - we tell it as his own witnessed account, not ours."),
 "alexstory003": dict(owner="alexfig011", tellable_as="background-fact",
  occasion="The recurring persecution episodes (Severan c. 202, Decian 249-251, Diocletianic 303-311) as they bore on the school's life - a pattern across the horizon, not one event.",
  frame="We tell this as the pattern our own record attests across generations - named episodes, not one man's remembered day."),
 "alexstory004": dict(owner="alexfig011", tellable_as="background-fact",
  occasion="Sayings collected late 4th-5th c.; individual attributions moderate; world-attribution held open (cross-build provisional, Doc_01 §3.3).",
  frame="These sayings are kept collections whose desert-or-city belonging our own record holds open - we say so when we reach for them."),
 "alexstory005": dict(owner="alexfig010", tellable_as="scene",
  occasion="Athanasius's Life of Antony (c. 356-362), composed within living memory - the formation ideal credible, specific episodes hagiographic; cross-build constraint applies (Doc_01 §3.3).",
  frame="Athanasius wrote Antony's life within living memory - we tell it as his portrait, with the desert's own claim on this story held open beside ours."),
 "alexstory006": dict(owner="alexfig009", tellable_as="scene",
  occasion="The Markan foundation as first clearly asserted by Eusebius (HE 2.16, early 4th c.) - a later foundation-narrative carrying identity weight, not documented 1st-century history (Doc_01 §2.2).",
  frame="We tell the founding story as what it is among us - a received foundation-narrative, first written down generations later, carried for its weight, not its documentation."),
 "alexstory007": dict(owner="alexfig011", tellable_as="background-fact",
  occasion="The teacher-succession (Pantaenus - Clement - Origen - Heraclas - Dionysius - Didymus) as Eusebius scaffolds it - carrying the Didaskaleion historical-scope contest and Eusebius's HIGH institutional-claims screen (Doc_01 §1.2; srcALX009).",
  frame="We name our teachers in the order handed down - and we say plainly that the order's tidiness is its transmitter's, and that whether the school was an institution or a tradition is genuinely disputed."),
 "alexstory008": dict(owner="alexfig001", tellable_as="scene",
  occasion="Origen's rupture with bishop Demetrius (c. 231-234): ordination abroad, condemnation at Alexandria, departure to Caesarea - via Eusebius (HE VI) with his institutional screen active.",
  frame="We tell the parting of teacher and bishop as our record holds it - through Eusebius's telling, with his order-loving hand named."),
 "alexstory009": dict(owner="alexfig012", tellable_as="scene",
  occasion="The Coptic martyr memory - the Diocletianic persecution (303-311) remembered so deeply the Coptic church dates its calendar (Anno Martyrum) from Diocletian's accession (284).",
  frame="The martyrs we name are the community's own kept memory - a whole calendar begins from their era, and we tell it as the community's remembering."),
 "alexstory010": dict(owner="alexfig011", tellable_as="scene",
  occasion="Tier-4 composite: a typical catechumen's formation path assembled only from attested elements (catechumenal stages, scrutinies, baptism at Pascha); no single attested person - the composite is the community's own pattern (CO-P2-06 convention).",
  frame="This is no one person's remembered story - it is the shape of the path itself, assembled from what our record attests, and we say so when we tell it."),
}

FIGURES = [
 dict(id="alexfig001", names=[{"name": "Origen", "name_kind": "in-world"},
      {"name": "Origen of Alexandria (Origenes Adamantius)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["alexstory008"]),
 dict(id="alexfig002", names=[{"name": "Clement", "name_kind": "in-world"},
      {"name": "Clement of Alexandria", "name_kind": "scholarly"}],
      narratable=False, story_ids=[],
      accepted_refusal_note="Load-bearing as a voice (srcALX001) but no narratable scene survives in this inventory - asked for a Clement story, the voice declines honestly: his words are kept, his days are not."),
 dict(id="alexfig003", names=[{"name": "Athanasius", "name_kind": "in-world"},
      {"name": "Athanasius of Alexandria", "name_kind": "scholarly"}],
      narratable=True, story_ids=["alexstory005"]),
 dict(id="alexfig004", names=[{"name": "Gregory", "name_kind": "in-world"},
      {"name": "Gregory Thaumaturgus (the Wonderworker)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["alexstory001"]),
 dict(id="alexfig005", names=[{"name": "Didymus", "name_kind": "in-world"},
      {"name": "Didymus the Blind", "name_kind": "scholarly"}],
      narratable=True, story_ids=["alexstory002"]),
 dict(id="alexfig006", names=[{"name": "Palladius", "name_kind": "scholarly"}],
      narratable=True, story_ids=["alexstory002"],
      attribution_note="An outside witness, not an Alexandrian voice - his encounter with Didymus is personally-witnessed material (srcALX010's own distinction)."),
 dict(id="alexfig007", names=[{"name": "Demetrius", "name_kind": "in-world"},
      {"name": "Demetrius of Alexandria (bishop 189-232)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["alexstory008"]),
 dict(id="alexfig008", names=[{"name": "Pantaenus", "name_kind": "in-world"}],
      narratable=False, story_ids=[],
      accepted_refusal_note="Boundary-adjacent and thinly attested (Doc_01 §2.2) - named in the succession, but no tellable scene survives; asked for more, the voice says honestly that only the name and the place in the handing-down are kept."),
 dict(id="alexfig009", names=[{"name": "Mark", "name_kind": "in-world"},
      {"name": "Mark the Evangelist (foundation legend)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["alexstory006"],
      attribution_note="Narratable ONLY as the received foundation-narrative alexstory006 tells - a later legend carrying identity weight, never documented 1st-century history (Doc_01 §2.2)."),
 dict(id="alexfig010", names=[{"name": "Antony", "name_kind": "in-world"},
      {"name": "Antony of Egypt", "name_kind": "scholarly"}],
      narratable=True, story_ids=["alexstory005"],
      attribution_note="Cross-build figure: the desert world's own srcDES/desertfig001 material governs his desert formation; here he appears through Athanasius's portrait with the cross-build constraint (Doc_01 §3.3)."),
 dict(id="alexfig011", names=[{"name": "the Alexandrian Christian community itself", "name_kind": "in-world"}],
      narratable=True, story_ids=["alexstory003", "alexstory004", "alexstory007", "alexstory010"],
      attribution_note="Composite owner per CO-P2-06's standing convention: pattern and composite stories are owned by the community itself, never the persona."),
 dict(id="alexfig012", names=[{"name": "the martyrs of Egypt", "name_kind": "in-world"},
      {"name": "the Coptic martyrs (Diocletianic persecution)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["alexstory009"],
      attribution_note="A collective figure: the community's kept martyr memory (Anno Martyrum), not one attested individual."),
]

BUILD_RENDER_ROW = dict(
    id="srcALX033", world_id="alexandria-catechetical", record_type="source",
    schema_version=1, register="etic", review_state="draft",
    boundary_status="Native", disposition="in-use",
    work_author="this build (CiC Alexandria migration)",
    work_title="Build rendering of De incarnatione 54's formula as 'God became human so that humanity might become god'",
    work_locus="2026 (the deployed lexicon chunks' own rendering)",
    source_type="M", attribution_status="genuine", level_of_description="item",
    language="eng", script="Latn",
    discovery_channel="backward-snowball",
    discovery_instrument="S2.4-equivalent quote work (wrs/migrate/s62_alx_s24.py; the CO-P2-08 truthful-translation-row convention)",
    discovery_date="2026-07-27",
    licensed_for="translation_used row for alexq001 - the standard-rendering formula as the deployed chunks themselves carry it",
    verification_note="The truthful translation row per Desert's srcDES025 precedent: the rendering is the build's own standard-form English, not a published translation; the quote's license stays paraphrase-only.",
    added="2026-07-27 (S6.2 S2.4-equivalent)", jobs=[1, 2])

QUOTES = [
 dict(id="alexq001", speaker_or_author="alexfig003", translation_used="srcALX033",
      text_translation="God became human so that humanity might become god.",
      locus="Athanasius, On the Incarnation 54",
      license="paraphrase-only",
      confidence={"citation_specificity": "A",
                  "verification_state": "verified-via-authority",
                  "verification_date": "2026-07-27",
                  "evidentiary_weight": "load-bearing",
                  "formation_confidence": "Widely Accepted"}),
]


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
        body = re.sub(r"^-{3,}\s*$", "", m.group(2), flags=re.M).strip()
        secs[name] = body
    return fm, secs


def sources_for(source_line: str):
    out, seen = [], set()
    for key, sid in SOURCE_KEYS:
        if key.lower() in source_line.lower() and sid not in seen:
            seen.add(sid)
            out.append({"source_id": sid, "locus": source_line})
    return out or [{"source_id": "srcALX-UNRESOLVED", "locus": source_line}]


def main():
    drops = []
    for path in sorted(CHUNKS.glob("*.md")):
        fm, secs = parse_chunk(path)
        rid = path.stem.split("_")[0]
        meta = STORY[rid]
        tier = int(re.sub(r"[^\d]", "", fm.get("Tier", "1")) or 1)
        retrieve_when = [c.strip() for c in fm.get("Retrieve-When", "").split(";") if c.strip()]
        dnrw = [{"condition_type": "sense-disambiguation", "text": c.strip()}
                for c in fm.get("Do-Not-Retrieve-When", "").split(";") if c.strip()]
        rec = {
            "id": rid, "world_id": "alexandria-catechetical", "record_type": "story",
            "schema_version": 1, "jobs": [1, 2, 3], "register": "emic",
            "review_state": "draft", "cache_stability": "static",
            "title": fm.get("Story-Title", ""),
            "narrative_tier": {"tier": tier,
                               "justification": secs.get("Tier Justification", "")},
            "text": secs.get("Story Text", ""),
            "attested_occasion": meta["occasion"],
            "tellable_as": meta["tellable_as"],
            "owner_figure_id": meta["owner"],
            "voice_surface": (meta["frame"] + " Usage guidance (chunk, verbatim): "
                              + secs.get("Usage Guidance", "")),
            "retrieval": {"tier": tier, "retrieve_when": retrieve_when,
                          "do_not_retrieve_when": dnrw, "force_llm_vote": False},
            "sources": sources_for(fm.get("Source", "")),
        }
        body = (f"Migrated at the S6.2 S2.4-equivalent (2026-07-27) from "
                f"`data/alexandria_world/story_chunks/{path.name}` (mapping in "
                f"`wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage "
                f"Guidance verbatim; occasion/owner/frame authored per Desert S2.4 "
                f"conventions).")
        fec = secs.get("Formation Ecology Connection", "")
        if fec:
            body += "\n\n" + FEC_DELIM + " " + fec
        emit_record(rec, body, OUT / "story" / f"{rid}.md")
    for fig in FIGURES:
        rec = {"id": fig["id"], "world_id": "alexandria-catechetical",
               "record_type": "figure", "schema_version": 1, "jobs": [1, 3],
               "register": "etic", "review_state": "draft",
               "names": fig["names"], "narratable": fig["narratable"],
               "story_ids": fig["story_ids"]}
        for k in ("accepted_refusal_note", "attribution_note"):
            if fig.get(k):
                rec[k] = fig[k]
        emit_record(rec, "Authored at the S6.2 S2.4-equivalent (2026-07-27); "
                    "see wrs/migrate/s62_alx_s24.py.",
                    OUT / "figure" / f"{fig['id']}.md")
    emit_record(dict(BUILD_RENDER_ROW),
                "Authored at the S6.2 S2.4-equivalent (2026-07-27); the truthful "
                "translation row (CO-P2-08/srcDES025 convention).",
                OUT / "source" / "srcALX033.md")
    for q in QUOTES:
        rec = {"id": q["id"], "world_id": "alexandria-catechetical",
               "record_type": "quote", "schema_version": 1, "jobs": [1, 2, 3],
               "register": "emic", "review_state": "draft",
               **{k: v for k, v in q.items() if k != "id"}}
        emit_record(rec, "Authored at the S6.2 S2.4-equivalent (2026-07-27). The "
                    "standard English rendering of De incarnatione 54's formula; no vetted "
                    "translation row exists, so license is paraphrase-only and "
                    "translation_used stays honestly unset (the Desert Arsenius precedent, "
                    "srcDES025 class).",
                    OUT / "quote" / f"{q['id']}.md")
    print(f"wrote {len(STORY)} stories + {len(FIGURES)} figures + {len(QUOTES)} quote")


if __name__ == "__main__":
    main()
