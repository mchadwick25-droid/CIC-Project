"""CO-P2-03 (Mark, 2026-07-27) - the eight missing Desert term records.

Authored from Doc_06 Parts 2-3 (read in full for this CO): the seven Tier
2 entries (Xeniteia, Apatheia, Theoria, Penthos, Nepsis, Synaxis,
Kellion) at full tier-1/2 field completion, and Antirrhesis at Tier 3
(quick_meaning + sources per the profile). Quick/World Meaning and
Distortion Risk text condensed-verbatim from Doc_06; retrieve_when is
authored here (participant-observable triggers only); voice_surface in
plain register asserting only documented content (the S2.3 review
lesson); prior senses not developed in the build's documents are marked
UNVERIFIED inline.

Puritas Cordis (Doc_06 3.2) is deliberately NOT authored: its only
source is Cassian, whose source row is pending CO-P2-10(c) - authoring
it now would mean fabricating a citation. Apatheia's Doc_06-named edge
to it is therefore deferred (noted in the record body), not silently
dropped.

Reciprocity: every typed edge added here gets its inverse/mirror
appended to the target tier-1 record file (idempotent append, marked
"CO-P2-03 mirror"). The tier-1 records are s23 emissions; if s23 is ever
re-run, re-run this script after it.

Source mapping (Doc_06 Key Sources -> srcDES rows): Doc_02 SS1.5
Apophthegmata = srcDES005 (+srcDES006 ammas where relevant); SS1.4
Evagrius = srcDES004; SS5.1 Kellia = srcDES009; Doc_01 SS10 Letters of
Antony = srcDES003 + Rubenson srcDES013; Doc_02 SS4 narrative sources
collectively = srcDES005/007/008.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

import yaml

from source_rows_from_doc02 import emit_record

OUT = BACKEND / "wrs" / "records" / "desert_world" / "term"

COMMON = {"world_id": "desert-monasticism", "record_type": "term",
          "schema_version": 1, "jobs": [1, 2, 4, 5, 6, 7],
          "register": "emic", "review_state": "draft",
          "cache_stability": "static"}


def C(fc):
    return {"citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": "2026-07-27",
            "evidentiary_weight": "corroborating",
            "formation_confidence": fc}


TERMS = [
 dict(
  id="desertlex010", term="Xeniteia (Exile / Estrangement)",
  aliases=["exile", "estrangement", "xeniteia"],
  quick_meaning=("Self-imposed estrangement from homeland, kin, and "
                 "familiar social bonds, pursued as a distinct ascetic "
                 "discipline."),
  world_meaning=("Treated as a discipline in its own right, not merely a "
                 "consequence of withdrawal. Most strongly attested in "
                 "Strand A/C material (the Apophthegmata); less "
                 "prominent, though not absent, in Strand B's more "
                 "settled communal framing (Doc_06 §2.1; Doc_03 §1.3)."),
  modern_hearing="Modern Hearing — travel, tourism, or relocation.",
  distortion_risk=("World Hearing — a deliberate severing of the "
                   "relational bonds that make a person recognizable to "
                   "themselves: estrangement as discipline, not "
                   "displacement."),
  period_sense=("A distinct ascetic discipline: self-imposed "
                "estrangement from homeland and kin, intensifying "
                "withdrawal by targeting social rather than geographic "
                "attachment (Doc_06 §2.1)."),
  prior_sense=("Ordinary Greek sense: the condition of living abroad as "
               "a stranger or foreigner. The build's own documents do "
               "not develop this prior sense — noted from standard "
               "lexica, UNVERIFIED against a registry source; flagged "
               "rather than asserted."),
  modern_sense=("Heard today, if at all, through the travel/relocation "
                "register (Doc_06 §2.1 Modern Hearing)."),
  conceptual_distance_note=("The modern ear hears movement between "
                            "places; the world meant severed bonds — the "
                            "discipline is relational, not geographic "
                            "(Doc_06 §2.1 World Hearing)."),
  semantic_domain="formation-acts",
  voice_surface=("Some among us left not only the village but the kin "
                 "who knew our names. That leaving was its own "
                 "discipline, distinct from the going out itself."),
  grounding_criterion="high",
  retrieval={"tier": 2,
             "retrieve_when": ["participant asks about leaving family or "
                                "homeland, cutting ties with kin, or why "
                                "ascetics abandoned their relationships"],
             "do_not_retrieve_when": [], "force_llm_vote": False},
  sources=[{"source_id": "srcDES005"}],
  confidence=C("Widely Accepted"),
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex001",
    "note": ("Doc_06 §2.1 Ecological Function (verbatim): A specific "
             "intensification of anachōrēsis (1.1), targeting social "
             "rather than geographic attachment specifically.")}]),

 dict(
  id="desertlex011", term="Apatheia (Passionlessness)",
  aliases=["passionlessness", "apatheia"],
  quick_meaning=("Freedom from disordered passion — in Evagrius's "
                 "systematic scheme, the achieved goal of the practical "
                 "stage of ascetic life."),
  world_meaning=("The state of freedom from disordered passion; in "
                 "Evagrius's systematic scheme, the achieved goal of the "
                 "practical (praktike) stage, preceding contemplation. "
                 "Strand-C-bound in this technical sense (Doc_06 §2.2; "
                 "Doc_04 gravity 9, Supporting on Persistence grounds). "
                 "Contested as to historical scope: whether Antony "
                 "himself possessed the philosophical literacy this "
                 "term's Origenist-influenced register presupposes "
                 "(Rubenson vs. Gould, Doc_01 §10; Doc_06 §2.2's "
                 "corrected [CT] note) — a dispute about one figure's "
                 "formation, not about whether the vocabulary belongs to "
                 "this world. Held as live, not settled."),
  modern_hearing=("Modern Hearing — near-certain false-cognate collapse "
                  "into 'apathy': indifference, not caring."),
  distortion_risk=("World Hearing — the opposite of indifference: the "
                   "hard-won capacity to engage fully without being "
                   "controlled by disordered reaction, achieved only "
                   "through sustained combat against the logismoi, not "
                   "a starting disposition."),
  period_sense=("In this world's Strand-C systematization: the achieved "
                "goal of the practical stage of ascetic life, preceding "
                "theōria (Doc_06 §2.2)."),
  prior_sense=("Broadly-shared Greek philosophical (Stoic) vocabulary "
               "for freedom from passion — Doc_06 §2.2 itself names the "
               "wider Stoic/philosophical currency; the desert entry "
               "documents specifically the systematized Evagrian sense."),
  modern_sense=("Heard today through 'apathy' — indifference (Doc_06 "
                "§2.2 Modern Hearing, the entry's own near-certain "
                "false-cognate warning)."),
  conceptual_distance_note=("A false cognate inverts the meaning "
                            "entirely: apathy names disengagement; "
                            "apatheia names full engagement freed from "
                            "disordered reaction. Sharp then-vs-now gap: "
                            "high grounding criterion by rule."),
  semantic_domain="interior-states",
  voice_surface=("The word does not mean not caring. Among those of us "
                 "who used it, it named the freedom won after long "
                 "combat with the thoughts — to meet what comes without "
                 "being ruled by it. It was one teacher's precise word, "
                 "not the whole desert's."),
  grounding_criterion="high",
  retrieval={"tier": 2,
             "retrieve_when": ["participant uses 'apatheia' or 'apathy' "
                                "about the tradition, or asks about "
                                "passionlessness or the goal of ascetic "
                                "practice"],
             "do_not_retrieve_when": [], "force_llm_vote": False},
  sources=[{"source_id": "srcDES004"},
           {"source_id": "srcDES003",
            "author_gravity_note": ("Letters of Antony — authenticity and "
                                     "Origenist-influence reading Contested "
                                     "(Doc_01 §10; Doc_02 §1.3, §9).")},
           {"source_id": "srcDES013",
            "author_gravity_note": ("Rubenson's reading of the Letters — "
                                     "the scope dispute with Gould over "
                                     "Antony's own literacy (Doc_06 §2.2 "
                                     "[CT]).")}],
  confidence=C("Widely Accepted"),
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex004",
    "note": ("Doc_06 §2.2 Ecological Function: the systematized "
             "resolution toward which gravity 2/9's spiritual combat is "
             "oriented within Strand C specifically — apatheia is "
             "achieved through sustained combat against the logismoi.")},
   {"type": "precondition-for", "target_id": "desertlex012",
    "note": ("Doc_06 §2.2: precedes and enables theōria — the "
             "praktike→apatheia→theōria sequence.")},
   {"type": "presupposed-by", "target_id": "desertlex012",
    "note": ("Inverse of theōria's presupposes edge (the same Doc_06 "
             "§2.2/2.3 sequence, both directions typed).")}]),

 dict(
  id="desertlex012", term="Theōria (Contemplation)",
  aliases=["contemplation", "theoria"],
  quick_meaning=("The contemplative stage of Evagrius's systematic "
                 "scheme, reached only after apatheia."),
  world_meaning=("In Evagrius's systematic scheme, the stage following "
                 "praktike and apatheia — subdivided into natural "
                 "contemplation and, at the highest stage, contemplation "
                 "of God. Strand-C-bound, single-author-concentrated "
                 "(Doc_06 §2.3; Doc_03 §1.7; Doc_04 §3)."),
  modern_hearing=("Modern Hearing — 'theory' as abstract intellectual "
                  "speculation."),
  distortion_risk=("World Hearing — a lived, disciplined mode of "
                   "perception achieved only after apatheia, not a "
                   "detached cognitive exercise."),
  period_sense=("The terminal stage of Strand C's systematized formation "
                "sequence, after the practical stage and apatheia "
                "(Doc_06 §2.3)."),
  prior_sense=("Ordinary Greek sense: looking at, beholding, "
               "speculation — the root of the modern 'theory'. The "
               "build's documents do not develop this prior sense — "
               "UNVERIFIED against a registry source; flagged rather "
               "than asserted."),
  modern_sense=("Heard today as 'theory' — abstract speculation (Doc_06 "
                "§2.3 Modern Hearing)."),
  conceptual_distance_note=("The shared root points opposite ways: "
                            "modern theory is detached thinking; this "
                            "world's theōria is disciplined perception "
                            "earned by practice. Sharp gap: high "
                            "grounding criterion."),
  semantic_domain="interior-states",
  voice_surface=("Those among us who used this word did not mean "
                 "thinking about God from a distance. They meant a way "
                 "of seeing that comes, if it comes, only after the "
                 "long practical work is done."),
  grounding_criterion="high",
  retrieval={"tier": 2,
             "retrieve_when": ["participant asks about contemplation, "
                                "mystical vision, or what the ascetic "
                                "practice ultimately leads to"],
             "do_not_retrieve_when": [], "force_llm_vote": False},
  sources=[{"source_id": "srcDES004"}],
  confidence=C("Widely Accepted"),
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex011",
    "note": ("Doc_06 §2.3: reached only after apatheia — the sequence's "
             "own ordering (inverse of apatheia's precondition-for "
             "edge).")}]),

 dict(
  id="desertlex013", term="Penthos (Mourning / Compunction)",
  aliases=["mourning", "compunction", "penthos"],
  quick_meaning=("Sorrowful, tearful awareness of one's own sin, "
                 "cultivated as a positive ascetic discipline."),
  world_meaning=("Cultivated as a positive discipline rather than a "
                 "state to escape. Attested across strands, particularly "
                 "prominent in the Apophthegmata (Doc_06 §2.4; Doc_03 "
                 "§1.8)."),
  modern_hearing=("Modern Hearing — grief or depression, something to "
                  "be resolved or treated."),
  distortion_risk=("World Hearing — a deliberately cultivated, "
                   "spiritually productive disposition, sought rather "
                   "than merely endured."),
  period_sense=("Sorrow over one's own condition as a cultivated good — "
                "a discipline sought, not a state suffered (Doc_06 "
                "§2.4)."),
  prior_sense=("Ordinary Greek sense: grief, mourning for the dead. The "
               "build's documents do not develop this prior sense — "
               "UNVERIFIED against a registry source; flagged rather "
               "than asserted."),
  modern_sense=("Heard today through the grief/depression register — a "
                "condition to treat (Doc_06 §2.4 Modern Hearing)."),
  conceptual_distance_note=("The modern frame treats sorrow as a "
                            "problem; this world cultivated it as a "
                            "discipline that keeps self-assessment "
                            "honest. Sharp gap: high grounding "
                            "criterion."),
  semantic_domain="interior-disciplines",
  voice_surface=("We did not treat our tears as something to be "
                 "cured. Sorrow over what we found in ourselves was "
                 "cultivated as a discipline, because it guarded the "
                 "watching against thinking too well of its own "
                 "progress."),
  grounding_criterion="high",
  retrieval={"tier": 2,
             "retrieve_when": ["participant asks about tears, mourning, "
                                "compunction, or sorrow over sin in the "
                                "tradition"],
             "do_not_retrieve_when": [], "force_llm_vote": False},
  sources=[{"source_id": "srcDES005"}],
  confidence=C("Widely Accepted"),
  field_relations=[
   {"type": "mechanism-behind", "target_id": "desertlex005",
    "note": ("Doc_06 §2.4 Ecological Function (verbatim): a companion "
             "discipline to diakrisis — sorrow over one's own condition "
             "disciplines the self-assessment discernment requires, "
             "guarding against the vainglorious assumption of one's own "
             "progress.")}]),

 dict(
  id="desertlex014", term="Nēpsis (Watchfulness)",
  aliases=["watchfulness", "nepsis", "vigilance"],
  quick_meaning=("Vigilant attentiveness to one's own interior "
                 "movements — the ongoing act of watching that "
                 "discernment draws on."),
  world_meaning=("Closely related to diakrisis but denoting the ongoing "
                 "act of watching rather than the resulting judgment. "
                 "Cross-strand in root (1 Peter 5:8) but most "
                 "systematically developed in Strand C. Not to be "
                 "conflated with the later, fully systematized "
                 "neptic/Philokalic tradition (Doc_06 §2.5; Doc_03 "
                 "§1.10)."),
  modern_hearing="Modern Hearing — generalized 'mindfulness.'",
  distortion_risk=("World Hearing — specifically oriented toward "
                   "detecting the logismoi at their earliest, most "
                   "manageable stage, before they take hold."),
  period_sense=("The ongoing act of interior watching that supplies "
                "discernment its raw material (Doc_06 §2.5)."),
  prior_sense=("Ordinary Greek sense: sobriety, being unintoxicated "
               "(the 1 Peter 5:8 register Doc_06 cites as the "
               "cross-strand root)."),
  modern_sense=("Heard today as generalized mindfulness (Doc_06 §2.5 "
                "Modern Hearing)."),
  conceptual_distance_note=("Mindfulness observes without agenda; this "
                            "world's watching is combat-oriented — "
                            "aimed at catching specific thoughts early. "
                            "Sharp gap: high grounding criterion."),
  semantic_domain="interior-disciplines",
  voice_surface=("The watching came first, before any judging. We "
                 "kept attention on our own interior movements so that "
                 "a thought could be seen early, while it was still "
                 "small enough to weigh."),
  grounding_criterion="high",
  retrieval={"tier": 2,
             "retrieve_when": ["participant asks about watchfulness, "
                                "vigilance, attention practice, or "
                                "compares the tradition to mindfulness"],
             "do_not_retrieve_when": [], "force_llm_vote": False},
  sources=[{"source_id": "srcDES004"}, {"source_id": "srcDES005"}],
  confidence=C("Widely Accepted"),
  field_relations=[
   {"type": "mechanism-behind", "target_id": "desertlex005",
    "note": ("Doc_06 §2.5 Ecological Function (verbatim): feeds "
             "diakrisis directly — watchfulness supplies the raw "
             "attentiveness that discernment then judges; without it, "
             "diakrisis has nothing current to assess.")}]),

 dict(
  id="desertlex015", term="Synaxis (The Gathering)",
  aliases=["the gathering", "synaxis"],
  quick_meaning=("The weekly communal gathering for vigil, liturgy, and "
                 "a shared meal, central to Strand C's semi-anchoritic "
                 "settlements."),
  world_meaning=("The weekly (Saturday-to-Sunday) communal gathering for "
                 "vigil, liturgy, and a shared meal, structurally "
                 "central to Strand C specifically. Strand B has "
                 "functionally comparable daily communal liturgy but on "
                 "a different, Rule-governed rhythm, not under this name "
                 "(Doc_06 §2.6; Doc_03 §1.13; Doc_05 §5)."),
  modern_hearing="Modern Hearing — a generic 'church service.'",
  distortion_risk=("World Hearing — the one weekly point at which an "
                   "otherwise solitary week became visibly communal; its "
                   "rarity, not its content, is what gave it structural "
                   "weight."),
  period_sense=("The one structurally regular point at which Strand C's "
                "otherwise solitary weekly rhythm became communal — "
                "organizing belonging and liturgical time for that "
                "strand (Doc_06 §2.6)."),
  prior_sense=("Ordinary Greek sense: a bringing-together, assembly. The "
               "build's documents do not develop this prior sense — "
               "UNVERIFIED against a registry source; flagged rather "
               "than asserted."),
  modern_sense=("Heard today as a church service among many in a week "
                "(Doc_06 §2.6 Modern Hearing)."),
  conceptual_distance_note=("A modern service is one meeting in a "
                            "social week; the synaxis was the single "
                            "communal seam in a solitary one — its "
                            "weight came from its rarity."),
  semantic_domain="communal-rhythms",
  voice_surface=("Once in the week we came together — the vigil, the "
                 "liturgy, the shared table. The other days were the "
                 "cell's. Because it was the one communal point in a "
                 "solitary week, that gathering carried great weight "
                 "among us."),
  grounding_criterion="high",
  retrieval={"tier": 2,
             "retrieve_when": ["participant asks about worship "
                                "gatherings, the weekly rhythm, liturgy, "
                                "or how often ascetics met"],
             "do_not_retrieve_when": [], "force_llm_vote": False},
  sources=[{"source_id": "srcDES005"}, {"source_id": "srcDES007"},
           {"source_id": "srcDES008"}],
  confidence=C("Widely Accepted"),
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex016",
    "note": ("Doc_06 §2.6/2.7: the gathering's structural weight "
             "presupposes the cell-based dispersed pattern it "
             "punctuates — the one weekly point at which the "
             "otherwise solitary (cell-dwelling) week became "
             "communal.")}]),

 dict(
  id="desertlex016", term="Kellion (The Cell)",
  aliases=["the cell", "kellion"],
  quick_meaning=("The individual or small-group dwelling unit that is "
                 "Strand C's basic architectural and organizational "
                 "building block."),
  world_meaning=("Strand C's basic architectural and organizational "
                 "building block, and the namesake of the Kellia "
                 "settlement itself. Independently corroborated "
                 "archaeologically: over 1,500 identified structures "
                 "ranging from single cells to multi-room hermitages "
                 "with attached oratories (Doc_06 §2.7; Doc_02 §5.1)."),
  modern_hearing="Modern Hearing — a generic monk's 'room.'",
  distortion_risk=("World Hearing — a deliberately spare, purpose-built "
                   "space whose separateness from neighboring cells was "
                   "itself formationally significant."),
  period_sense=("The physical unit Strand C's semi-anchoritic pattern "
                "requires — near enough to gather weekly, far enough "
                "apart that the rest of the week is solitary (Doc_06 "
                "§2.7)."),
  prior_sense=("Ordinary Greek/Latin sense: a small room, storeroom, "
               "cella. The build's documents do not develop this prior "
               "sense — UNVERIFIED against a registry source; flagged "
               "rather than asserted."),
  modern_sense=("Heard today as a bare room, or through the prison-cell "
                "register (Doc_06 §2.7 Modern Hearing: a generic "
                "monk's room)."),
  conceptual_distance_note=("The modern ear hears accommodation; the "
                            "world built separateness on purpose — the "
                            "cell's distance from its neighbors was "
                            "part of the formation, not an "
                            "architectural accident."),
  semantic_domain="material-setting",
  voice_surface=("The cell was not lodging. It was built spare on "
                 "purpose, and set apart from its neighbors on purpose "
                 "— near enough to gather once a week, far enough that "
                 "the week itself was solitary."),
  grounding_criterion="high",
  retrieval={"tier": 2,
             "retrieve_when": ["participant asks about the cell, where "
                                "ascetics lived, dwellings, or daily "
                                "living arrangements"],
             "do_not_retrieve_when": [], "force_llm_vote": False},
  sources=[{"source_id": "srcDES009"}],
  confidence=C("Widely Accepted"),
  field_relations=[
   {"type": "precondition-for", "target_id": "desertlex001",
    "note": ("Doc_06 §2.7 Ecological Function (verbatim): the physical "
             "unit anachōrēsis (1.1) and hēsychia (1.3) require to be "
             "practiced at all in Strand C's semi-anchoritic pattern — "
             "without it, this strand's specific balance of "
             "solitude-plus-proximity has no material form.")},
   {"type": "precondition-for", "target_id": "desertlex003",
    "note": ("Same Doc_06 §2.7 warrant, the hēsychia side: the cell is "
             "where Strand C's stillness is materially practicable.")}]),

 dict(
  id="desertlex017", term="Antirrhēsis (Talking Back)",
  aliases=["talking back", "antirrhesis"],
  quick_meaning=("The specific technique of verbally countering a "
                 "demonic logismos with a scriptural rebuttal at the "
                 "moment of temptation, systematized by Evagrius in his "
                 "Antirrhetikos."),
  modern_hearing=("Modern Hearing — 'talking back to' one's own "
                  "thoughts may register as a self-help or "
                  "cognitive-behavioral technique."),
  distortion_risk=("World Hearing — a specific scriptural-combat method, "
                   "single-author and single-text in origin, not this "
                   "world's general vocabulary (Doc_06 §3.1)."),
  retrieval={"tier": 3,
             "retrieve_when": ["participant asks specifically about "
                                "answering or rebutting thoughts/demons "
                                "with scripture"],
             "do_not_retrieve_when": [], "force_llm_vote": False},
  sources=[{"source_id": "srcDES004"}],
  confidence=C("Widely Accepted"),
  field_relations=[
   {"type": "presupposes", "target_id": "desertlex004",
    "note": ("Doc_06 §3.1: a technique for countering a demonic "
             "logismos at the moment of temptation — presupposes the "
             "logismoi framework it answers.")}]),
]

# reciprocal edges appended to existing tier-1 records: (target_file_id,
# edge dict) - inverse types where Pass 1 names them, mirrors otherwise
RECIPROCALS = [
 ("desertlex001", {"type": "presupposed-by", "target_id": "desertlex010",
   "note": "CO-P2-03 mirror: xeniteia intensifies withdrawal (Doc_06 §2.1)."}),
 ("desertlex004", {"type": "presupposed-by", "target_id": "desertlex011",
   "note": "CO-P2-03 mirror: apatheia is combat's systematized resolution (Doc_06 §2.2)."}),
 ("desertlex004", {"type": "presupposed-by", "target_id": "desertlex017",
   "note": "CO-P2-03 mirror: antirrhesis answers the logismoi (Doc_06 §3.1)."}),
 ("desertlex005", {"type": "mechanism-behind", "target_id": "desertlex013",
   "note": ("CO-P2-03 mirror (linkage reciprocity; no Pass 1 inverse for "
            "mechanism-behind): penthos disciplines diakrisis's "
            "self-assessment (Doc_06 §2.4).")}),
 ("desertlex005", {"type": "mechanism-behind", "target_id": "desertlex014",
   "note": ("CO-P2-03 mirror (linkage reciprocity): nepsis feeds "
            "diakrisis directly (Doc_06 §2.5).")}),
 ("desertlex016", {"type": "presupposed-by", "target_id": "desertlex015",
   "note": "CO-P2-03 mirror: the synaxis presupposes the cell pattern (Doc_06 §2.6)."}),
 ("desertlex001", {"type": "precondition-for", "target_id": "desertlex016",
   "note": ("CO-P2-03 mirror (linkage reciprocity): the cell is "
            "anachōrēsis's material form in Strand C (Doc_06 §2.7).")}),
 ("desertlex003", {"type": "precondition-for", "target_id": "desertlex016",
   "note": ("CO-P2-03 mirror (linkage reciprocity): the cell is "
            "hēsychia's material form in Strand C (Doc_06 §2.7).")}),
]


def main() -> None:
    for t in TERMS:
        rec = dict(COMMON)
        rec.update(t)
        body = ("CO-P2-03 term record (2026-07-27), authored from Doc_06 "
                "Part 2/3 (condensed-verbatim meanings; authored "
                "retrieve_when; plain-register voice_surface). "
                + ("Deferred edge: Doc_06 §2.2 also names Puritas Cordis "
                   "(3.2) as related - not typed here because the "
                   "Cassian source row is pending CO-P2-10(c)."
                   if t["id"] == "desertlex011" else ""))
        emit_record(rec, body.strip(), OUT / f"{t['id']}.md")
    # reciprocal edges on tier-1 records (idempotent)
    touched = 0
    for fid, edge in RECIPROCALS:
        p = OUT / f"{fid}.md"
        text = p.read_text(encoding="utf-8")
        parts = text.split("---\n")
        fm = yaml.safe_load(parts[1])
        rels = fm.setdefault("field_relations", [])
        if any(e.get("target_id") == edge["target_id"] and
               e.get("type") == edge["type"] for e in rels):
            continue
        rels.append(edge)
        body = "---\n".join(parts[2:])
        p.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False,
                                               allow_unicode=True, width=100)
                     + "---\n" + body, encoding="utf-8")
        touched += 1
    print(f"wrote {len(TERMS)} new term records; {touched} reciprocal "
          f"edges appended to tier-1 records")


if __name__ == "__main__":
    main()
