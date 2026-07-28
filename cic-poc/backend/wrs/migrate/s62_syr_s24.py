"""S6.2/Syriac - S2.4-equivalent: stories + figures. NO quote record.

9 story chunks (data/syriac_world/story_chunks/) -> story records;
8 figure records. Mechanical where the chunk carries the content (Story
Text, Tier Justification, Usage Guidance, retrieval front matter - all
verbatim); authored-in-script where Desert/ALX S2.4 authored
(attested_occasion, tellable_as, owner assignment, the voice_surface
telling-frame).

QUOTE FINDING, DECLARED: unlike Desert (4 vetted sayings) and ALX (the
De incarnatione 54 formula), the deployed Syriac corpus carries NO
verbatim in-world quotation - the only verified direct quotations in
the build are Brock's own scholarly words (Doc_02 SS11: Luminous Eye
1992 p. 41; Harp of the Spirit 2013 p. 17), secondary voice, not world
voice. No quote record is emitted; the absence is a real property of
this world's evidentiary shape (structurally literary-theological, not
narrative-historical - Doc_02 SS1) and the S2.7-equivalent voice work
must carry it.

FEC HANDLING: same as ALX - Formation Ecology Connection parked
VERBATIM in each story record's body under the named delimiter; the
S2.5-equivalent converts the parkings into typed gravity_links
(CO-P2-04 shape). Nothing dropped, no dangling gravity ids.

TIER NOTE, DECLARED: this repository's own Tier Justifications record
that Syriac has NO Tier 1 story at all (syrstory001's Round-1 review
correction - 'a genuine evidentiary finding, not a defect'); tiers run
2/2/2, 3/3/3/3/3, 4.

EDITIONS CLASS, DECLARED: syrstory002's Source line cites the Guidi
CSCO edition and Cowper translation of the Chronicle of Edessa - row 21
covers the work; the editions ride the locus string per the standing
ALX editions rule (deferred to the pre-freeze re-sweep, same as
Howard/Lollar at S2.1a).

CO-P2-06: composite/pattern stories are owned by the community itself
(syrfig007), never the persona - syrstory002 (a civic chronicle entry
naming no Christian) and syrstory009 (the Tier-4 composite).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

CHUNKS = BACKEND / "data" / "syriac_world" / "story_chunks"
OUT = BACKEND / "wrs" / "records" / "syriac_world"

FEC_DELIM = ("[Formation Ecology Connection - parked at the S2.4-equivalent; "
             "becomes typed gravity_links (CO-P2-04 shape) when the "
             "S2.5-equivalent authors the gravity records]")

SOURCE_KEYS = [
    ("Vita Ephraemi", "srcSYR059"),
    ("GEDSH", "srcSYR051"),
    ("Rousseau", "srcSYR060"),
    ("Muraviev", "srcSYR061"),
    ("Gennadius", "srcSYR044"),
    ("Chronicle of Edessa", "srcSYR021"),
    ("Theodoret", "srcSYR043"),
    ("Honigmann", "srcSYR049"),
    ("Peeters", "srcSYR050"),
    ("Doctrina Addai", "srcSYR020"),
    ("Kyle Smith", "srcSYR046"),
    ("Carmina Nisibena", "srcSYR004"),
    ("Jacob of Serugh", "srcSYR045"),
]

STORY = {
 "syrstory001": dict(owner="syrfig001", tellable_as="scene",
  occasion=("The Edessa famine of 373 and Ephrem's death soon after "
            "organizing relief - Gennadius of Marseille's Supplement "
            "notice (c. 470s-490s), the SOLE source for the claim; "
            "Jerome's genuinely in-window entry (392/3) does not "
            "corroborate the famine or the manner of death (the chunk's "
            "own Tier Justification, which corrected this story from "
            "Tier 1 to Tier 2 at review)."),
  frame=("We tell how our teacher died as the record a century on kept "
         "it: he came out from his own retirement to feed the starving, "
         "and did not long survive the labor. We name Gennadius, and "
         "his distance, where it matters.")),
 "syrstory002": dict(owner="syrfig007", tellable_as="background-fact",
  occasion=("The Chronicle of Edessa's entry for Seleucid year 513 "
            "(November 201 CE), under Abgar VIII - a civic flood record "
            "filed under four named non-Christian court archivists, "
            "carrying the single line that the flood 'destroyed the "
            "temple of the church of the Christians'; whether that line "
            "is original or a later interpolation is contested (chunk "
            "front matter)."),
  frame=("We tell this as the city's own record tells it - a flood, a "
         "broken wall, the dead counted, and one line about the house "
         "of the church, set down by the king's own archivists who were "
         "not of us. It is the earliest line our city's record gives "
         "us, and we let it stay exactly one line.")),
 "syrstory003": dict(owner="syrfig003", tellable_as="background-fact",
  occasion=("Nicaea, 325: Jacob bishop of Nisibis (from c. 309) among "
            "the signatories - the surviving lists are late composite "
            "manuscripts reconstructed by modern scholarship (Honigmann, "
            "position 77), and no contemporary fourth-century document "
            "independently confirms the anti-Arian role later historians "
            "remembered him for (chunk Story Text/front matter)."),
  frame=("We name Jacob among those who stood at Nicaea because the "
         "kept lists carry his name - and we say plainly that the lists "
         "are late copies, and the memory of his part against Arius is "
         "a later historian's remembering.")),
 "syrstory004": dict(owner="syrfig005", tellable_as="scene",
  occasion=("The Doctrina Addai's foundation account (the received "
            "text): Abgar's correspondence with Jesus, the mission of "
            "Addai, the succession Addai-Aggai-Palut with Palut's "
            "ordination at Antioch under Serapion - this world's own "
            "telling of its beginning, Contested as formation-account "
            "and Inferential-Thin for any specific event (chunk front "
            "matter; composition scholarship rides srcSYR047)."),
  frame=("This is the account our city tells of its own beginning - the "
         "king's letter, the promise, the teacher sent. We tell it as "
         "the kept founding story, carried for its weight among us, not "
         "for its documentation.")),
 "syrstory005": dict(owner="syrfig004", tellable_as="scene",
  occasion=("The Persian martyr act (Smith's edition): under Shapur "
            "II's double poll-tax, Simeon bishop of Seleucia-Ctesiphon "
            "refuses to collect, is tried at Karka d-Ledan, sees the "
            "returned apostate Gushtazad die first, and is beheaded "
            "with the priests Hananya and Abdhaykla; the traditional "
            "341 date is actively disputed (Kosinski/Burgess c. 344, "
            "Doc_02 SS11), and the narrative is hagiographic in genre "
            "(Tier 3)."),
  frame=("We tell Simeon's dying as the martyr-record keeps it - the "
         "tax refused, the eunuch who had once fallen going ahead of "
         "him, the confession held to the end. It is the community's "
         "kept martyr memory, told in its own dress, and we say so.")),
 "syrstory006": dict(owner="syrfig003", tellable_as="scene",
  occasion=("The siege-deliverance tradition: Theodoret (HE II.26/30; "
            "HR I, 5th c.) tells of Jacob's prayer from the ramparts "
            "at Ephrem's urging and the plague of gnats and mosquitoes "
            "that broke the Persian camp; Ephrem's own Carmina "
            "Nisibena commemorate the sieges in verse (the chunk's own "
            "corroboration note) - tradition Contested, the specific "
            "event Inferential-Thin (Tier 3)."),
  frame=("We tell the deliverance as the tradition sings it - the old "
         "bishop on the wall, the smallest of afflictions asked for "
         "and sent. Our own teacher put the city's survival into "
         "hymns; the story's marvels we carry as the tradition's own "
         "telling, not as the record's proof.")),
 "syrstory007": dict(owner="syrfig001", tellable_as="scene",
  occasion=("Jacob of Serugh's memorial homily (c. 500, roughly 125 "
            "years after Ephrem's death): Ephrem gathering the "
            "daughters of the covenant to sing true doctrine against "
            "Bardaisan's and Mani's songs - LATER ATTRIBUTION, not "
            "Ephrem's own contemporary self-testimony (the syrlex002 "
            "evidentiary-layer split; Doc_02 SS3's correction), told "
            "as Jacob's remembering (Tier 3)."),
  frame=("We tell this as a later teacher's loving memory of ours - "
         "Jacob of Serugh remembering Ephrem setting the daughters of "
         "the covenant to sing. What is firsthand with us is the "
         "singing itself and Aphrahat's covenant-order; that Ephrem "
         "founded the choirs is the memory's claim, and we name whose "
         "memory it is.")),
 "syrstory008": dict(owner="syrfig001", tellable_as="scene",
  occasion=("The Syriac Vita Ephraemi's legend (6th c.): Ephrem's "
            "vision-prompted journey to Basil at Caesarea and "
            "ordination to the diaconate - positively identified by "
            "modern scholarship as resting on a documented case of "
            "mistaken identity (chunk front matter; Rousseau 1957-58; "
            "Muraviev 2015); engaged ONLY when a participant raises "
            "it, always with the correction attached (the chunk's own "
            "retrieve-when rule and srcSYR059's licensing)."),
  frame=("If you have heard that our Ephrem met the great Basil, we "
         "will tell you what the later life-story says - and tell you "
         "with it that those who have searched the record find the "
         "meeting rests on a mistaken name, not a kept memory. We do "
         "not offer this story unasked.")),
 "syrstory009": dict(owner="syrfig007", tellable_as="scene",
  occasion=("Tier-4 composite: a typical pre-dawn qyama vigil at "
            "Nisibis assembled ONLY from attested elements - the vow "
            "(Aphrahat Dem 6), the bnat qyama singing madrashe "
            "(Harvey's scholarship), worship performing the "
            "raza/shrara hermeneutic (Brock), the Diatessaron as the "
            "reading (Doc_04 C5), the undivided Nativity-Epiphany "
            "feast - no single attested person; the composite is the "
            "community's own pattern (CO-P2-06; the chunk's own Source "
            "Identification table)."),
  frame=("This is no one person's remembered morning - it is the "
         "shape of the vigil itself, assembled from what our record "
         "attests, and we say so when we tell it.")),
}

FIGURES = [
 dict(id="syrfig001",
      names=[{"name": "Ephrem", "name_kind": "in-world"},
             {"name": "Ephrem the Syrian (Ephraem Syrus)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["syrstory001", "syrstory007", "syrstory008"],
      attribution_note=("The world's dominant surviving voice (Doc_02's "
                        "Author-Gravity center). His three stories carry "
                        "three DIFFERENT evidentiary postures, each named "
                        "in its record: remembered history a century on "
                        "(001), later attribution told as Jacob of "
                        "Serugh's memory (007), and a corrected legend "
                        "never offered unasked (008). 'Mar Ephrem' as a "
                        "lifetime form of address is unconfirmed "
                        "(syrlex008).")),
 dict(id="syrfig002",
      names=[{"name": "Aphrahat", "name_kind": "in-world"},
             {"name": "Aphrahat the Persian Sage", "name_kind": "scholarly"}],
      narratable=False, story_ids=[],
      accepted_refusal_note=("Load-bearing as a voice (srcSYR010 - the "
                             "twenty-three tahwyata, incl. Demonstration "
                             "6 on the qyama) but NO narratable scene "
                             "survives in this inventory: asked for an "
                             "Aphrahat story, the voice declines "
                             "honestly - his words are kept, his days "
                             "are not (the Clement/alexfig002 "
                             "precedent). Even his episcopal status is "
                             "genuinely open (Doc_02 SS11).")),
 dict(id="syrfig003",
      names=[{"name": "Jacob of Nisibis", "name_kind": "in-world"},
             {"name": "Jacob (Mar Yaqub) of Nisibis, bishop from c. 309", "name_kind": "scholarly"}],
      narratable=True, story_ids=["syrstory003", "syrstory006"],
      attribution_note=("His death date is a genuine PRIMARY-SOURCE "
                        "conflict carried open, never silently resolved: "
                        "the Martyrologium Hieronymianum implies 338, the "
                        "Chronicon Paschale has him defending Nisibis in "
                        "350 (Doc_02 SS11's own instruction to carry "
                        "both).")),
 dict(id="syrfig004",
      names=[{"name": "Simeon bar Sabbae", "name_kind": "in-world"},
             {"name": "Simeon bar Sabba'e, bishop of Seleucia-Ctesiphon", "name_kind": "scholarly"}],
      narratable=True, story_ids=["syrstory005"],
      attribution_note=("Narrated through the Persian martyr acts "
                        "(hagiographic genre, Tier 3); the traditional "
                        "martyrdom date 341 is actively disputed "
                        "(Kosinski/Burgess c. 344) and the downstream "
                        "succession chain shifts with it (Doc_02 "
                        "SS11).")),
 dict(id="syrfig005",
      names=[{"name": "Addai", "name_kind": "in-world"},
             {"name": "Addai (Thaddeus of Edessa, foundation legend)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["syrstory004"],
      attribution_note=("Narratable ONLY as the received "
                        "foundation-narrative syrstory004 tells - the "
                        "Doctrina Addai's account, carried for its "
                        "identity weight, never as documented "
                        "first-century history (the alexfig009/Mark "
                        "precedent).")),
 dict(id="syrfig006",
      names=[{"name": "King Abgar", "name_kind": "in-world"},
             {"name": "Abgar V (the correspondence legend; Doc_01 SS2's own identification)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["syrstory004"],
      attribution_note=("The legendary correspondent of Jesus in the "
                        "Doctrina Addai - narratable only within "
                        "syrstory004's received-legend frame. Distinct "
                        "from the historical Abgar VIII 'the Great' of "
                        "syrstory002's flood chronicle (a civic record, "
                        "not a legend).")),
 dict(id="syrfig007",
      names=[{"name": "the qyama - the covenant community itself", "name_kind": "in-world"},
             {"name": "the bnay/bnat qyama (sons and daughters of the covenant)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["syrstory002", "syrstory009"],
      attribution_note=("Composite owner per CO-P2-06's standing "
                        "convention: pattern and communal stories are "
                        "owned by the community itself, never the "
                        "persona - the civic flood record (002, which "
                        "names no individual Christian at all) and the "
                        "Tier-4 composite vigil (009).")),
 dict(id="syrfig008",
      names=[{"name": "Basil of Caesarea", "name_kind": "scholarly"}],
      narratable=True, story_ids=["syrstory008"],
      attribution_note=("A cross-tradition figure, NOT this world's own "
                        "voice - he appears only inside the Vita "
                        "Ephraemi legend, which scholarship identifies "
                        "as resting on documented mistaken identity; "
                        "narratable only within syrstory008's "
                        "correction-attached frame.")),
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
        secs[name] = re.sub(r"^-{3,}\s*$", "", m.group(2), flags=re.M).strip()
    return fm, secs


def sources_for(rid: str, source_line: str, secs: dict):
    if rid == "syrstory009":
        # the composite's own Source Identification table maps elements
        # to rowed material (Aphrahat Dem 6; Harvey; Brock; Diatessaron)
        locus = ("Composite - elements per the chunk's own Source "
                 "Identification table (parked verbatim in this record's "
                 "body): " + source_line)
        return [{"source_id": sid, "locus": locus}
                for sid in ("srcSYR010", "srcSYR032", "srcSYR029", "srcSYR011")]
    out, seen = [], set()
    for key, sid in SOURCE_KEYS:
        if key.lower() in source_line.lower() and sid not in seen:
            seen.add(sid)
            out.append({"source_id": sid, "locus": source_line})
    return out or [{"source_id": "srcSYR-UNRESOLVED", "locus": source_line}]


def main():
    for path in sorted(CHUNKS.glob("*.md")):
        fm, secs = parse_chunk(path)
        rid = path.stem.split("_")[0]
        meta = STORY[rid]
        tier = int(re.sub(r"[^\d]", "", fm.get("Tier", "1")) or 1)
        retrieve_when = [c.strip() for c in fm.get("Retrieve-When", "").split(";") if c.strip()]
        dnrw = [{"condition_type": "sense-disambiguation", "text": c.strip()}
                for c in fm.get("Do-Not-Retrieve-When", "").split(";") if c.strip()]
        rec = {
            "id": rid, "world_id": "syriac-edessa-nisibis", "record_type": "story",
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
            "confidence_line": fm.get("Confidence", ""),
            "retrieval": {"tier": tier, "retrieve_when": retrieve_when,
                          "do_not_retrieve_when": dnrw, "force_llm_vote": False},
            "sources": sources_for(rid, fm.get("Source", ""), secs),
        }
        body = (f"Migrated at the S6.2/SYR S2.4-equivalent (2026-07-28) from "
                f"`data/syriac_world/story_chunks/{path.name}` (mapping in "
                f"`wrs/migrate/s62_syr_s24.py`; Story Text / Tier Justification / Usage "
                f"Guidance / Confidence line verbatim; occasion/owner/frame authored per "
                f"Desert-ALX S2.4 conventions).")
        fec = secs.get("Formation Ecology Connection", "")
        if fec:
            body += "\n\n" + FEC_DELIM + " " + fec
        if secs.get("Source Identification"):
            body += ("\n\n[Source Identification - the composite's own "
                     "element-to-source table, parked verbatim (CO-P2-06 "
                     "composite convention)] " + secs["Source Identification"])
        emit_record(rec, body, OUT / "story" / f"{rid}.md")
    for fig in FIGURES:
        rec = {"id": fig["id"], "world_id": "syriac-edessa-nisibis",
               "record_type": "figure", "schema_version": 1, "jobs": [1, 3],
               "register": "etic", "review_state": "draft",
               "names": fig["names"], "narratable": fig["narratable"],
               "story_ids": fig["story_ids"]}
        for k in ("accepted_refusal_note", "attribution_note"):
            if fig.get(k):
                rec[k] = fig[k]
        emit_record(rec, "Authored at the S6.2/SYR S2.4-equivalent (2026-07-28); "
                    "see wrs/migrate/s62_syr_s24.py.",
                    OUT / "figure" / f"{fig['id']}.md")
    print(f"wrote {len(STORY)} stories + {len(FIGURES)} figures + 0 quotes "
          f"(the no-vetted-quote finding, declared)")


if __name__ == "__main__":
    main()
