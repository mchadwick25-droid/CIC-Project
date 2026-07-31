"""S6.2/PAHC - S2.4-equivalent: stories + figures. NO quote record needed
as a separate emission - PAHC's verbatim quotations (the Ignatius
wheat/leopards lines, Polycarp's eighty-six years, the Didache prayers,
Justin's order, Tacitus's phrases) all ride INSIDE story texts with
their frames, the halstory08 pattern at fleet scale; declared.

13 story records + 8 figure records. Mechanical where the chunk
carries content (Story Text / Tier Justification / Usage Guidance /
Confidence line / front matter verbatim); authored-in-script
(attested_occasion, tellable_as, owner assignment, voice_surface
telling-frame).

PAHC decisions, each declared:
- SOURCES ARE MECHANICAL: every Source line carries inline Registry
  tags - sources_for() extracts them (composites get their full tag
  set); the S2.1 id-preservation paying off end-to-end.
- OUTSIDER FIGURES OWN THEIR OWN ACCOUNTS: Pliny (pahcfig006) owns
  story 004 and Tacitus (pahcfig007) owns story 005 - unlike the SYR
  flood-chronicle precedent (community-owned civic record), PAHC's
  outside witnesses are registry PRIMARY rows with lexicon load
  (ministrae/hetaeria/pertinacia are Pliny-vocabulary terms): this
  world's own build treats outside witnesses as primary voices, and
  the figures follow, narratable only inside their stories' frames
  (the Augustine/srcHAL009 two-sided-class precedent).
- COMPOSITE OWNERS (CO-P2-06): stories 009/010/012/013 (no individual
  subject) -> pahcfig008, the network itself; story 011 -> Ignatius
  per its own composite-in-method-not-subject shape (the halstory11
  precedent: built entirely from his own instructions).
- pahcfig002 is a COMMUNITY-VOICE figure: 'the church at Rome' - 1
  Clement is anonymous in its own text; the traditional Clement
  attribution and Hermas's named-Clement instruction (Vision 2.4.3)
  ride the attribution note, never asserted as authorship.
- NO figures for Lucian (story 013 explicitly refuses
  Peregrinus-as-protagonist and Lucian appears only as hostile
  observer), Nero, Trajan, Grapte - named-in-narrative, not
  narratable centers; declared.
- SCHEMA-GAP NOTE (S2.9 CO candidate, with the strand-field gap): the
  PAHC story chunks carry a SENSITIVITY-GUARD Do-Not-Retrieve-When
  class ('participant is in acute personal crisis around death...';
  'requires pastoral sensitivity'; story 004's vulnerability guard) -
  the schema's condition_type enum has no such member, so these ride
  as sense-disambiguation VERBATIM with the class named here and in
  the checkpoint, not silently flattened.
- FEC parked verbatim under the standing delimiter (S2.5 converts;
  note the FECs name STRAND-SCOPED gravities - 'G04 ... Strand A
  only' - the S2.5 layer carries the scoping); the five composites'
  Source Identification tables park verbatim.
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

CHUNKS = BACKEND / "data" / "pahc_world" / "story_chunks"
OUT = BACKEND / "wrs" / "records" / "pahc_world"
WID = "post-apostolic-house-church"

FEC_DELIM = ("[Formation Ecology Connection - parked at the S2.4-equivalent; "
             "becomes typed gravity_links (CO-P2-04 shape) when the "
             "S2.5-equivalent authors the gravity records]")

STORY = {
 "pahcstory001": dict(owner="pahcfig001", tellable_as="scene",
  occasion=("Ignatius's guarded journey toward the Roman arena (trad. c. "
            "107-117, under Trajan): the seven letters written in transit "
            "- delegations meeting him at Smyrna, the letter sent ahead "
            "to Rome begging no rescue, the one-bishop instruction "
            "pressed with a condemned man's urgency. The three-way "
            "authenticity dispute (Trajanic / 130s-140s redating / "
            "pseudepigraphic 160-180) carried at full strength per the "
            "chunk's own Tier Justification - the majority reading "
            "followed, the minority never erased."),
  frame=("We tell his journey in his own words where we have them - the "
         "ten leopards, the wheat of God - and we say plainly whose "
         "words they are: a condemned man writing in transit, arguing "
         "urgently for what he would not live to argue again. If you "
         "ask whether the letters are truly his and truly early, we "
         "tell you honestly that most who study them say yes, and some "
         "serious voices say later - we do not claim more than the "
         "record settles.")),
 "pahcstory002": dict(owner="pahcfig002", tellable_as="scene",
  occasion=("Rome's letter to Corinth (trad. c. 96; contested range "
            "80-140): presbyters removed without cause, and a sister "
            "church's long, scripture-laden appeal for their restoration "
            "- appealing, never commanding; anonymous in its own text, "
            "'Clement' a traditional attribution the letter itself does "
            "not make (the chunk's own confidence split)."),
  frame=("We tell how Rome wrote to Corinth - one church to another, "
         "with no power to compel and no bishop invoked, only the long "
         "argument that removing blameless presbyters tears what unity "
         "built. The letter names no author; later memory calls him "
         "Clement, and we pass that name on as memory, not as the "
         "letter's own word.")),
 "pahcstory003": dict(owner="pahcfig003", tellable_as="background-fact",
  occasion=("Polycarp's forwarding of the collected Ignatius letters to "
            "Philippi at their request (Philippians 13) - the "
            "correspondence network's ordinary, almost administrative "
            "operation; the Harrison two-letter-splice question carried "
            "as the chunk carries it (affects dating confidence, not "
            "the act's attestation)."),
  frame=("A small thing, told in a single line of his own letter: they "
         "asked for the letters, and he sent what his community had "
         "gathered. We tell it because it shows the network at its most "
         "ordinary - not a postal system, but one named man doing one "
         "requested kindness. And we note what he calls himself there: "
         "one of the presbyters, not bishop.")),
 "pahcstory004": dict(owner="pahcfig006", tellable_as="scene",
  occasion=("Bithynia-Pontus, c. 111-113: Pliny's own letter to Trajan "
            "- executions after warning, citizens reserved for Rome, "
            "two ministrae tortured for information, 'nothing else than "
            "depraved, excessive superstition' found; Trajan's rescript "
            "(no seeking out, no anonymous accusations) preserved with "
            "it. The sole non-Christian eyewitness account of a "
            "gathering, its oath, and its meal."),
  frame=("We tell this in the governor's own words, because they are "
         "the only outside eyes that ever looked closely at us and "
         "wrote down what they saw: the fixed day before dawn, the hymn "
         "to Christ as to a god, the oath against theft and adultery "
         "and broken trust, the ordinary and harmless meal. And we do "
         "not pass over what it cost: two women of ours, tortured for "
         "it. The word for them - ministrae - is his, not ours.")),
 "pahcstory005": dict(owner="pahcfig007", tellable_as="background-fact",
  occasion=("Rome, 64 CE, told c. 116: Tacitus's account of Nero's "
            "scapegoating after the fire - a great multitude convicted "
            "'not so much of arson as of hatred of the human race,' the "
            "theatrical cruelty, no Christian named. The Shaw/Jones "
            "dispute (whether a discrete fire-linked persecution of "
            "Christians as a named group occurred, or later memory "
            "retrojected) carried at full strength per the chunk."),
  frame=("We tell our own beginning-condition through an outsider's "
         "pen, because our own record keeps no account of it: the fire, "
         "the blame shifted onto us, the deaths made into spectacle. No "
         "name of ours survives from it. Whether it happened as one "
         "event or was remembered into one, even those who study it "
         "cannot settle - and we hold that openness rather than "
         "claiming a certainty no one has.")),
 "pahcstory006": dict(owner="pahcfig005", tellable_as="scene",
  occasion=("Rome, c. 153-157: Justin's own first-person account, "
            "addressed to emperor and Senate, of the Sunday gathering - "
            "reading, discourse, standing prayer, thanksgiving over "
            "bread and mixed cup 'according to his ability,' the Amen, "
            "the collection for orphans, widows, the sick, prisoners, "
            "strangers. Tier 1 by the chunk's own reasoned edge-case "
            "argument (a primary source reporting its own routine "
            "practice); Bradshaw's network-template caution carried."),
  frame=("We tell the Roman Sunday as Justin told it to the emperor "
         "himself: the day named for the sun, the reading for as long "
         "as time allows, the one presiding giving thanks according to "
         "his ability, the Amen, and the collection that ends as care "
         "for whoever is in need. One community's own account, offered "
         "to hostile ears - we do not stretch it into every "
         "household's template.")),
 "pahcstory007": dict(owner="pahcfig004", tellable_as="scene",
  occasion=("Rome, composite composition c. 90-150: Hermas's own "
            "reported visions - the Church as an elderly woman growing "
            "younger, the Shepherd, the one urgent post-baptismal "
            "repentance offered before the door closes; Clement and "
            "Grapte named to specific roles (Vision 2.4.3), Rome's "
            "plural-leadership pattern in the text's own address. The "
            "chunk's genre disclosure carried whole: Tier 1 attests the "
            "REPORTING, never the supernatural content as fact."),
  frame=("We tell what Hermas says he saw - the lady who is the Church, "
         "old because she was created before all things, growing "
         "younger as understanding grows; the message of one mercy "
         "still open after the water. We tell it as his own reported "
         "seeing, in the genre he gave it, and we do not turn a vision "
         "into a transcript.")),
 "pahcstory008": dict(owner="pahcfig003", tellable_as="scene",
  occasion=("Smyrna's letter to Philomelium (trad. c. 155-156; Eusebius "
            "167; chs. 20-22 widely held later additions): Polycarp's "
            "arrest, the eighty-six-years answer, the fire like a "
            "ship's sail, the dagger, the disputed dove, the bones "
            "'more precious than the finest gold' and the annual "
            "gathering at the tomb - the community's own martyrology, "
            "told in its own commemorative register (Tier 3 by the "
            "chunk's own genre analysis)."),
  frame=("This is how the community that knew him remembered Polycarp's "
         "end - the answer he gave ('eighty-six years I have served "
         "him, and he has done me no wrong'), the fire that the telling "
         "says would not touch him, the bones gathered like treasure "
         "and the yearly return to them. We tell it as the tradition's "
         "own witness to what it believed a formed life could become - "
         "a testimony to what it meant, not a transcript of what "
         "happened.")),
 "pahcstory009": dict(owner="pahcfig008", tellable_as="scene",
  occasion=("Tier-4 composite from the Didache's own sequential text "
            "(chs. 1-7): the Two Ways taught first - the Way of Life "
            "with its rule of restraint, the Way of Death by contrast - "
            "then the fasts, then the water (running, still, or poured "
            "threefold); every element traced in the chunk's own Source "
            "Identification table; never extended beyond the Didache's "
            "own single community (the chunk's own cap - the S2.1b "
            "watch item's story-side)."),
  frame=("This is no one person's remembered path - it is the path the "
         "Didache itself lays out, walked as a whole: the two roads "
         "set before the learner, the fast, the water. We say plainly "
         "that we tell it as the handbook's own sequence, and that "
         "whether every household prepared its members so, our record "
         "does not say.")),
 "pahcstory010": dict(owner="pahcfig008", tellable_as="scene",
  occasion=("Tier-4 composite from Didache 9-10 and 14: cup before "
            "bread, thanks for vine and knowledge and gathering, the "
            "baptized-only rule, the Maranatha, confession and "
            "reconciliation before the Lord's-day breaking of bread - "
            "and NO institution narrative anywhere in the order: 'a "
            "formation logic built without an institution narrative at "
            "all' (the chunk's own point; the diversity-first "
            "discipline, never merged with Justin's or Ignatius's "
            "orders)."),
  frame=("We tell this table as the handbook gives it: the cup first, "
         "the broken bread scattered on the mountains and gathered "
         "into one, the thanks for knowledge and for gathering, and "
         "at the end the community's own cry - Maranatha. No supper "
         "is retold at it, no body and blood given in memory; that is "
         "not a lack we apologize for but the shape this thanksgiving "
         "actually has, and we keep it distinct from the other tables "
         "our record holds.")),
 "pahcstory011": dict(owner="pahcfig001", tellable_as="scene",
  occasion=("Tier-4 composite built entirely from Ignatius's own "
            "instructions (Philadelphians 4; Smyrnaeans 8): one "
            "eucharist, one altar, one bishop; nothing without him; "
            "'composite in method, but not in subject' (the halstory11 "
            "precedent - one man's own program throughout); the same "
            "authenticity caveats as story 001, plus the open "
            "settled-practice-vs-aspirational-program question the "
            "chunk carries from Doc_01."),
  frame=("This is how it would have been in a household formed by his "
         "letters: one table, under one bishop, and no other counted "
         "valid. We tell it as his own instruction given flesh - and "
         "we carry the open question his letters cannot answer for "
         "us: whether he described an order already standing, or "
         "argued for one he feared would not stand without him.")),
 "pahcstory012": dict(owner="pahcfig008", tellable_as="scene",
  occasion=("The repository's most fully composite story (across "
            "P02/P03/P04/P05): a member's day under each of the two "
            "strands held side by side - the bishop-anchored day and "
            "the presbyter-council day - 'neither presented as more "
            "original, more correct, or more typical' (the chunk's own "
            "rule; Doc_05's inhabited-voice reconstruction carried "
            "into Tier-4 register)."),
  frame=("We tell both days together because our world lived both: in "
         "one household the day orients to the bishop's table and his "
         "word makes things secure; in another it orients to the "
         "elders together, holding office none may strip without "
         "cause. We do not choose between them in the telling, "
         "because our own letters never did.")),
 "pahcstory013": dict(owner="pahcfig008", tellable_as="scene",
  occasion=("Tier-4 composite from two OUTSIDE accounts pointed in "
            "opposite directions - Lucian's mockery (c. 165) "
            "preserving the prison-gate widows, the bribed officials, "
            "the delegates sent from Asia's cities, the money 'no "
            "small sums'; Tertullian's defense (c. 197) describing "
            "the voluntary monthly fund for the buried poor, orphans, "
            "the old, the imprisoned - the same pattern attested by "
            "mock and by defense; Peregrinus himself explicitly NOT "
            "narrated (the chunk's own refusal)."),
  frame=("We tell what even a mocker could not help preserving: that "
         "when one of ours was held under threat, widows waited at "
         "the gates from dawn, officials were bribed for entry, "
         "cities sent their own to comfort him, and the books were "
         "read aloud inside. A scoffer saw it and sneered; a defender "
         "described the fund behind it; between the two of them, the "
         "care itself stands attested. The man the scoffer mocked we "
         "do not narrate - his story was never ours to tell.")),
}

FIGURES = [
 dict(id="pahcfig001",
      names=[{"name": "Ignatius, bishop of Antioch", "name_kind": "in-world"},
             {"name": "Ignatius of Antioch (middle recension)", "name_kind": "scholarly"}],
      narratable=True,
      story_ids=["pahcstory001", "pahcstory003", "pahcstory011"],
      attribution_note=(
          "Strand A's dominant surviving voice - and this world's "
          "sharpest Author-Gravity concentration: the monarchical "
          "episkopos, the presbyterion, the one-eucharist instruction "
          "all rest on his letters alone (pahclex001/006's own "
          "single-witness cautions). EVERY telling carries the "
          "three-way authenticity dispute (Trajanic majority / "
          "130s-140s redating / pseudepigraphic minority) at the "
          "strength story 001's Tier Justification sets - never "
          "presented as settled if pressed.")),
 dict(id="pahcfig002",
      names=[{"name": "the church at Rome (the voice of the letter to "
                      "Corinth)", "name_kind": "in-world"},
             {"name": "1 Clement's anonymous corporate author "
                      "(traditionally 'Clement of Rome')", "name_kind": "scholarly"}],
      narratable=True, story_ids=["pahcstory002", "pahcstory007"],
      attribution_note=(
          "A COMMUNITY-VOICE figure, declared: the letter is anonymous "
          "in its own text and speaks as one church to another; "
          "'Clement' is a traditional attribution the text does not "
          "make - carried as later memory, never authorship. Hermas's "
          "Vision 2.4.3 names a Clement to a sending role among "
          "Rome's plural leaders (with Grapte to the widows and "
          "orphans) - the strand-B plural pattern this figure "
          "embodies; whether that Clement and the letter's "
          "traditional author are the same man, the record does not "
          "establish.")),
 dict(id="pahcfig003",
      names=[{"name": "Polycarp of Smyrna", "name_kind": "in-world"},
             {"name": "Polycarp (Letter to the Philippians; Martyrdom "
                      "of Polycarp)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["pahcstory003", "pahcstory008"],
      attribution_note=(
          "The figure who spans both registers: his own letter's "
          "modest self-naming ('one of the presbyters' - not bishop, "
          "though Ignatius addresses him as one; the world's own "
          "disclosed tension, never resolved) and the community's "
          "commemorative martyrology (Tier 3, genre named whenever "
          "told). The Harrison splice question rides story 003's "
          "dating confidence.")),
 dict(id="pahcfig004",
      names=[{"name": "Hermas", "name_kind": "in-world"},
             {"name": "Hermas (Shepherd of Hermas, Rome)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["pahcstory007"],
      attribution_note=(
          "A freedman of Rome reporting his own visions - Tier 1 for "
          "the REPORTING, with the genre disclosure carried in every "
          "telling (the vision content is never offered as "
          "supernatural fact); the composite-composition dating "
          "(90-150, possibly in stages) stays open.")),
 dict(id="pahcfig005",
      names=[{"name": "Justin", "name_kind": "in-world"},
             {"name": "Justin Martyr (First Apology)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["pahcstory006"],
      attribution_note=(
          "The Roman Sunday's eyewitness - his account addressed "
          "OUTWARD (emperor and Senate), fullest of the surviving "
          "orders and never thereby most representative (the "
          "pahclex004 methodological caution; Bradshaw's "
          "network-template caution on story 006).")),
 dict(id="pahcfig006",
      names=[{"name": "Pliny, the governor who questioned us", "name_kind": "in-world"},
             {"name": "Pliny the Younger (Letters 10.96-97)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["pahcstory004"],
      attribution_note=(
          "A cross-boundary OUTSIDER figure who owns his own account "
          "(the two-sided-class precedent, and beyond it: this "
          "world's build rows its outside witnesses as PRIMARY "
          "voices, and three lexicon terms - ministrae, hetaeria, "
          "pertinacia - are his vocabulary); narratable only within "
          "story 004's frame, with the under-torture honesty "
          "(pahclex009) governing every use of what he extracted.")),
 dict(id="pahcfig007",
      names=[{"name": "Tacitus, the historian who recorded the fire", "name_kind": "in-world"},
             {"name": "Tacitus (Annals 15.44)", "name_kind": "scholarly"}],
      narratable=True, story_ids=["pahcstory005"],
      attribution_note=(
          "The second outsider figure: his account of the Neronian "
          "scapegoating is the world's generative origin-condition "
          "told entirely from outside (no Christian named), with the "
          "Shaw/Jones discreteness dispute carried at full strength; "
          "narratable only within story 005's frame.")),
 dict(id="pahcfig008",
      names=[{"name": "the network itself - the ekklesiai in "
                      "correspondence", "name_kind": "in-world"},
             {"name": "the post-apostolic house-church network", "name_kind": "scholarly"}],
      narratable=True,
      story_ids=["pahcstory009", "pahcstory010", "pahcstory012",
                 "pahcstory013"],
      attribution_note=(
          "Composite/communal owner per CO-P2-06: the Two Ways path "
          "(009), the story-less table (010), the two-strands day "
          "(012 - built precisely to hold both without choosing), "
          "and the prisoner's-needs pattern (013 - two outside pens, "
          "mock and defense, attesting one practice). pahcstory011 "
          "is NOT here despite Tier 4: composite in method, not in "
          "subject - see pahcfig001 (the halstory11 precedent). NO "
          "figures for Lucian (013's own Peregrinus refusal), Nero, "
          "Trajan, or Grapte - named in narratives, not narratable "
          "centers; declared.")),
]


def parse_chunk(path: Path):
    text = path.read_text(encoding="utf-8")
    head, sep, rest = text.partition("\n---\n")
    assert sep, path.name
    fm, current = {}, None
    for line in head.splitlines():
        m = re.match(r"^([A-Za-z-]+):\s*(.*)$", line)
        if m:
            current = m.group(1)
            fm[current] = m.group(2).strip()
        elif current and line.strip():
            fm[current] += " " + line.strip()
    secs = {}
    for m in re.finditer(r"^## (.+?)\s*$\n(.*?)(?=^## |\Z)", rest, re.S | re.M):
        secs[m.group(1).strip()] = re.sub(
            r"^-{3,}\s*$", "", m.group(2), flags=re.M).strip()
    return fm, secs


def sources_for(source_line: str):
    # tags appear as 'Registry P07' or bare '(P02)' (story 012's
    # composite-across list) - both forms extracted
    tags = list(dict.fromkeys(
        re.findall(r"Registry ([PS]\d+)", source_line)
        + re.findall(r"\(([PS]\d+)\)", source_line)))
    assert tags, source_line
    return [{"source_id": "srcPAHC" + t, "locus": source_line}
            for t in tags]


def main():
    for path in sorted(CHUNKS.glob("*.md")):
        fm, secs = parse_chunk(path)
        rid = path.stem.split("_")[0]
        meta = STORY[rid]
        tier = int(re.sub(r"[^\d]", "", fm.get("Tier", "1")) or 1)
        retrieve_when = [c.strip() for c in
                         fm.get("Retrieve-When", "").split(";") if c.strip()]
        # the sensitivity-guard class rides as sense-disambiguation
        # VERBATIM (schema enum gap, declared in the module docstring)
        dnrw = [{"condition_type": "sense-disambiguation", "text": c.strip()}
                for c in fm.get("Do-Not-Retrieve-When", "").split(";")
                if c.strip()]
        rec = {
            "id": rid, "world_id": WID, "record_type": "story",
            "schema_version": 1, "jobs": [1, 2, 3], "register": "emic",
            "review_state": "draft", "cache_stability": "static",
            "title": fm.get("Story-Title", ""),
            "narrative_tier": {"tier": tier,
                               "justification": secs.get("Tier Justification", "")},
            "text": secs.get("Story Text", ""),
            "attested_occasion": meta["occasion"],
            "tellable_as": meta["tellable_as"],
            "owner_figure_id": meta["owner"],
            "voice_surface": (meta["frame"] + " Usage guidance (chunk, "
                              "verbatim): " + secs.get("Usage Guidance", "")),
            "confidence_line": fm.get("Confidence", ""),
            "retrieval": {"tier": tier, "retrieve_when": retrieve_when,
                          "do_not_retrieve_when": dnrw,
                          "force_llm_vote": False},
            "sources": sources_for(fm.get("Source", "")),
        }
        body = (f"Migrated at the S6.2/PAHC S2.4-equivalent (2026-07-31) "
                f"from `data/pahc_world/story_chunks/{path.name}` (mapping "
                f"in `wrs/migrate/s62_pahc_s24.py`; Story Text / Tier "
                f"Justification / Usage Guidance / Confidence line verbatim; "
                f"sources extracted mechanically from the Source line's own "
                f"Registry tags; occasion/owner/frame authored per the "
                f"fleet S2.4 conventions).")
        fec = secs.get("Formation Ecology Connection", "")
        if fec:
            body += "\n\n" + FEC_DELIM + " " + fec
        if secs.get("Source Identification"):
            body += ("\n\n[Source Identification - the composite's own "
                     "element-to-source table, parked verbatim (CO-P2-06 "
                     "composite convention)] " + secs["Source Identification"])
        (OUT / "story").mkdir(exist_ok=True)
        emit_record(rec, body, OUT / "story" / f"{rid}.md")
    for fig in FIGURES:
        rec = {"id": fig["id"], "world_id": WID, "record_type": "figure",
               "schema_version": 1, "jobs": [1, 3], "register": "etic",
               "review_state": "draft", "names": fig["names"],
               "narratable": fig["narratable"], "story_ids": fig["story_ids"]}
        for k in ("accepted_refusal_note", "attribution_note"):
            if fig.get(k):
                rec[k] = fig[k]
        (OUT / "figure").mkdir(exist_ok=True)
        emit_record(rec, "Authored at the S6.2/PAHC S2.4-equivalent "
                    "(2026-07-31); see wrs/migrate/s62_pahc_s24.py.",
                    OUT / "figure" / f"{fig['id']}.md")
    print(f"wrote {len(STORY)} stories + {len(FIGURES)} figures "
          f"(quotes ride story texts with frames - declared; no separate "
          f"quote record)")


if __name__ == "__main__":
    main()
