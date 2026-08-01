"""S6.2/IJC - S2.4-equivalent: 6 story records + 9 figures from the
deployed story chunks (mechanical split + declared ownership map).

ACCOUNT-OWNERSHIP (the PAHC Pliny/Tacitus precedent - the figure who
OWNS the account owns the story):
  story001 (the vision/alliance)      -> Eusebius (fig002) - his Vita account, Constantine's oath reported
  story002 (the dream)                -> Lactantius (fig003) - his earlier, divergent account
  story003 (the bees)                 -> Paulinus (fig005) - the hagiographic portrait, written at Augustine's request
  story004 (the basilica vigil)       -> Ambrose (fig004) - his own sermon during the standoff
  story005 (the letter/council)       -> Julius I (fig006) - his own letter, PRESERVED by Athanasius (fig009's whole role)
  story006 (the Tome)                 -> Leo I (fig007) - his own Tome and rejection letters

FIGURES (9): Constantine (fig001, SUBJECT of 1-2, owns no account),
Eusebius (fig002), Lactantius (fig003), Ambrose (fig004), Paulinus
(fig005), Julius I (fig006), Leo I (fig007), Damasus (fig008 - no
story chunk; his material is the epigraphic corpus riding
primatus/martyrium; narratable via the lexicon material), Athanasius
(fig009 - PRESERVER ONLY: his corpus is Excluded per Registry row 24;
the single quoted letter is Native; narratable False - he is the
transmission channel, never this world's own voice).
DECLARED SKIP: Augustine gets NO figure record - his corpus is
Excluded (row 26), his one eyewitness passage rides story004's source
note under its narrow license; a figure record would invite exactly
the boundary creep rows 8/26 exist to prevent.

Mechanical: Story Text / Tier Justification / Usage Guidance
(voice_surface with the USAGE_MARK) split from chunks; Confidence
lines verbatim; FEC PARKED in bodies (converted to gravity_links at
S2.5 per CO-P2-04); sources from the S2.1a Source-line map;
tellable_as 'scene' throughout (each chunk narrates one bounded
scene/arc).
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
CHUNKS = BACKEND / "data" / "imperial_juridical_world" / "story_chunks"
OUT = BACKEND / "wrs" / "records" / "imperial_juridical_world"
WID = "imperial-juridical-christianity"
USAGE_MARK = "Usage guidance (chunk, verbatim): "
FEC_MARK = ("[Formation Ecology Connection - parked at the "
            "S2.4-equivalent; converted to gravity_links at the "
            "S2.5-equivalent per CO-P2-04] ")

STORIES = {
 "ijcstory001": dict(sources=["srcIJC02"], owner="ijcfig002"),
 "ijcstory002": dict(sources=["srcIJC03"], owner="ijcfig003"),
 "ijcstory003": dict(sources=["srcIJC22"], owner="ijcfig005"),
 "ijcstory004": dict(sources=["srcIJC07", "srcIJC08"],
                     owner="ijcfig004"),
 "ijcstory005": dict(sources=["srcIJC04"], owner="ijcfig006"),
 "ijcstory006": dict(sources=["srcIJC12", "srcIJC13", "srcIJC11"],
                     owner="ijcfig007"),
}

FIGURES = [
 dict(id="ijcfig001", narratable=True,
      names=[{"name": "Constantine", "name_kind": "in-world"},
             {"name": "Constantine I (r. 306-337)",
              "name_kind": "scholarly"}],
      story_ids=["ijcstory001", "ijcstory002"],
      attribution_note=(
          "The SUBJECT of both founding stories, the OWNER of neither "
          "account: what Constantine himself saw or believed survives "
          "only through Eusebius's oath-reported telling and "
          "Lactantius's earlier, divergent one - the two accounts' "
          "divergence is itself registry-carried (row 3's own license). "
          "The initiating alliance's centre of gravity; every strand's "
          "common root (ijccore001).")),
 dict(id="ijcfig002", narratable=True,
      names=[{"name": "Eusebius of Caesarea", "name_kind": "in-world"},
             {"name": "Eusebius of Caesarea (c. 260-339)",
              "name_kind": "scholarly"}],
      story_ids=["ijcstory001"],
      attribution_note=(
          "Owns story001's account (Vita Constantini - Constantine's "
          "vision as Eusebius reports hearing it from the emperor under "
          "oath, years later). Also Strand B's theological seed (the "
          "court theology; 'bishop of those outside', row 2's own "
          "license) and the alliance's founding narrator (rows 1-2). "
          "His own pro-Constantinian shaping is the Author-Gravity to "
          "carry at every telling.")),
 dict(id="ijcfig003", narratable=True,
      names=[{"name": "Lactantius", "name_kind": "in-world"},
             {"name": "Lactantius (c. 250-325)",
              "name_kind": "scholarly"}],
      story_ids=["ijcstory002"],
      attribution_note=(
          "Owns story002's account (De Mortibus Persecutorum 44 - the "
          "dream before the battle, written earlier and closer to the "
          "event than Eusebius's version; the divergence between the "
          "two founding accounts is the point, held open, never "
          "harmonized - row 3's own license).")),
 dict(id="ijcfig004", narratable=True,
      names=[{"name": "Ambrose, bishop of Milan",
              "name_kind": "in-world"},
             {"name": "Ambrose of Milan (c. 339-397)",
              "name_kind": "scholarly"}],
      story_ids=["ijcstory003", "ijcstory004"],
      attribution_note=(
          "Strand C's whole voice: owns story004's account (his own "
          "Sermo contra Auxentium, preached during the standoff - a "
          "single author's account of his own confrontation, "
          "corroborated narrowly by Augustine's eyewitness passage, "
          "row 8's narrow license; the RES honesty rides ijclex005). "
          "SUBJECT of story003 (the bees) - that account is Paulinus's, "
          "not his.")),
 dict(id="ijcfig005", narratable=True,
      names=[{"name": "Paulinus of Milan", "name_kind": "in-world"},
             {"name": "Paulinus of Milan (Vita Ambrosii, c. 412-413)",
              "name_kind": "scholarly"}],
      story_ids=["ijcstory003"],
      attribution_note=(
          "Owns story003's account (the bee-swarm legend) - "
          "hagiographic by genre, written at Augustine's request some "
          "fifteen-twenty years after Ambrose's death; Tier 3 "
          "formation-narrative material ONLY, never documented "
          "biography (row 22's own license at Confidence C).")),
 dict(id="ijcfig006", narratable=True,
      names=[{"name": "Julius, bishop of Rome", "name_kind": "in-world"},
             {"name": "Julius I (bp. 337-352)",
              "name_kind": "scholarly"}],
      story_ids=["ijcstory005"],
      attribution_note=(
          "Owns story005's account (his 341 letter to the Eusebian "
          "party - Strand A's earliest attested instance, a generation "
          "before Damasus). DOUBLY MEDIATED: the letter survives only "
          "inside Athanasius's own apologetic quotation (row 4's own "
          "comparandum discipline; ijcfig009 is the channel).")),
 dict(id="ijcfig007", narratable=True,
      names=[{"name": "Leo, bishop of Rome", "name_kind": "in-world"},
             {"name": "Leo I (bp. 440-461)", "name_kind": "scholarly"}],
      story_ids=["ijcstory006"],
      attribution_note=(
          "Owns story006's account (the Tome to Flavian + the letters "
          "rejecting Canon 28) - Strand A's fullest voice and the "
          "world's own closing episode; the reception/non-reception "
          "split at Chalcedon is the open question the world ends "
          "inside.")),
 dict(id="ijcfig008", narratable=True,
      names=[{"name": "Damasus, bishop of Rome", "name_kind": "in-world"},
             {"name": "Damasus I (bp. 366-384)",
              "name_kind": "scholarly"}],
      story_ids=[],
      attribution_note=(
          "NO story chunk - his material is the epigraphic corpus (row "
          "14, P/M hybrid): the martyr inscriptions as Strand A's "
          "public self-presentation, riding "
          "primatus/martyrium/communio. The decretal material under "
          "his name is contested (row 15, Confidence D, dubium) and "
          "NEVER narrated as his; narratable via the lexicon material "
          "within that discipline.")),
 dict(id="ijcfig009", narratable=False,
      names=[{"name": "Athanasius of Alexandria",
              "name_kind": "scholarly"}],
      story_ids=[],
      attribution_note=(
          "PRESERVER ONLY - the transmission channel for Julius's "
          "letter (quoted in Apologia contra Arianos 21-35), never "
          "this world's own voice: his corpus belongs natively to the "
          "Desert and Alexandrian worlds (row 24, Excluded, Named "
          "Comparandum - 'do not extend Native status to the "
          "surrounding Athanasian material'). narratable False by that "
          "boundary; DECLARED here so the boundary is a record, not "
          "an omission. (Augustine gets no figure at all - row 26; "
          "his one eyewitness passage rides story004's source note.)")),
]


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


def main():
    n = 0
    for path in sorted(CHUNKS.glob("*.md")):
        rid = path.stem.split("_")[0]
        fm, secs = parse_chunk(path)
        meta = STORIES[rid]
        tier = int(re.sub(r"[^\d]", "", fm.get("Tier", "1")) or 1)
        dnrw = [{"condition_type": "sense-disambiguation", "text": c.strip()}
                for c in fm.get("Do-Not-Retrieve-When", "").split(";")
                if c.strip()]
        rec = {
            "id": rid, "world_id": WID, "record_type": "story",
            "schema_version": 1, "jobs": [1, 2, 4], "register": "emic",
            "review_state": "draft", "cache_stability": "static",
            "title": fm.get("Story-Title", ""),
            "text": secs.get("Story Text", ""),
            "confidence_line": fm.get("Confidence", ""),
            "attested_occasion": fm.get("Source", ""),
            "tellable_as": "scene",
            "owner_figure_id": meta["owner"],
            "narrative_tier": {
                "tier": tier,
                "justification": secs.get("Tier Justification", "")},
            "voice_surface": (USAGE_MARK
                              + secs.get("Usage Guidance", "")),
            "gravity_links": [],
            "retrieval": {
                "tier": tier,
                "retrieve_when": [c.strip() for c in
                                  fm.get("Retrieve-When", "").split(";")
                                  if c.strip()],
                "do_not_retrieve_when": dnrw,
                "force_llm_vote": False},
            "sources": [{"source_id": s} for s in meta["sources"]],
        }
        body = (f"Migrated at the S6.2/IJC S2.4-equivalent (2026-07-31) "
                f"from `data/imperial_juridical_world/story_chunks/"
                f"{path.name}` (mechanical split; ownership map in "
                f"`wrs/migrate/s62_ijc_s24.py`).\n\n"
                + FEC_MARK
                + secs.get("Formation Ecology Connection", "")
                + "\n\n[Final Assembly Instruction - parked verbatim as "
                  "assembly provenance] "
                + secs.get("Final Assembly Instruction", ""))
        emit_record(rec, body, OUT / "story" / f"{rid}.md")
        n += 1
    for f in FIGURES:
        rec = {"id": f["id"], "world_id": WID, "record_type": "figure",
               "schema_version": 1, "jobs": [1, 2], "register": "etic",
               "review_state": "draft", "names": f["names"],
               "narratable": f["narratable"],
               "story_ids": f["story_ids"],
               "attribution_note": f["attribution_note"]}
        emit_record(rec, ("Authored at the S6.2/IJC S2.4-equivalent "
                          "(2026-07-31); ownership and boundary "
                          "reasoning in wrs/migrate/s62_ijc_s24.py."),
                    OUT / "figure" / f"{f['id']}.md")
    print(f"{n} story records + {len(FIGURES)} figures")


if __name__ == "__main__":
    main()
