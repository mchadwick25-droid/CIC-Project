"""B-6 (S2.6): Reformed Cities (rzg) contested_claim records.

WHAT THIS SCRIPT DOES. Produces this world's first `contested_claim`
records under records/rzg/contested_claim/, per the live schema
(TYPE_PROPERTIES["contested_claim"]: claim, held_against, concedes,
divergence_partners) and gate battery (COMPLETION_REQUIRED["contested_claim"]
= [claim, held_against, concedes]). Follows don's own precedent
(wb_don_s26.py, read in full before this script was written, plus two real
fleet worked examples read in full this session: don.contested.church-of-
the-martyrs.md and don.contested.bishop-count-411-conference.md) exactly
in register (etic - a contested_claim states what is contested FROM
OUTSIDE this world's own voice, unlike term/story/gravity's own emic
register) and structure.

WHY THIS RECORD TYPE MATTERS. Per don's own s26 docstring, quoting its own
launch brief: Table Readiness depends on a world actually having
contested_claim records to draw from - a Representative who has never had
to hold ground against a real counter-reading is untested in exactly the
way a genuine encounter will test it.

THREE RECORDS, NOT MORE, MATCHING THIS WORLD'S OWN ACTUALLY-CONTESTED
GROUND. Unlike don's own 52-finding reciprocity gap that made contested_claim
this world's own most urgent record type, rzg's own build already names its
live contests explicitly and narrowly (Doc_03 SS4, Doc_04 SS3.5, Doc_06 SS2)
- padding this record type past what is genuinely contested would invent
controversy this world's own record does not actually carry:
  1. Sign and the Thing Signified (rzglex008) - the one [CT]-tagged term in
     this world's own roster (Doc_03 SS4, Article 26), Contest Type: Meaning.
  2. T2 (Zwingli's 'Remembrance' Reading vs. the Negotiated Consensus) -
     Doc_04 SS3.5's own open judgment call, explicitly not resolved by any
     document in this world's build.
  3. The Anabaptist schism's own legitimacy (Force 2B-1) - a genuine, live
     historiographical contest (radical-Reformation historians read the
     Reformed magisterial refusal of believers'-baptism ecclesiology very
     differently than this world's own record does), directly evidenced in
     this world's own vendored Zwingli corpus and Doc_05 SS2's own emic
     framing of the schism.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_ROOT = REPO_ROOT / "records" / "rzg"

WORLD_ID = "the-reformed-cities-zurich-and-geneva"
SCHEMA_VERSION = 2


def _yaml_dump(payload: dict) -> str:
    return yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False)


def _write(path: Path, payload: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + _yaml_dump(payload) + "---\n" + body.strip() + "\n", encoding="utf-8")


CLAIMS: list[dict] = [
    dict(
        slug="sign-and-the-thing-signified",
        canon_cells=[],
        sources=[
            {"source_id": "rzg.source.consensus-tigurinus", "locus": "9th Head of Agreement, lines 768-770, and the document's own title page", "license": "public-domain"},
        ],
        relations=[
            {"type": "associated-with", "target": "rzg.term.sign-and-the-thing-signified"},
            {"type": "associated-with", "target": "rzg.gravity.spiritual-presence-rejection-of-corporeal-sacrificial-mediation"},
        ],
        claim=(
            "The Consensus Tigurinus's own 1549 formula - 'though we distinguish, as we ought, "
            "between the signs and the things signified, yet we do not disjoin the reality from the "
            "signs' - represents a genuine theological synthesis of Zwingli's earlier memorial view "
            "and Calvin's own developed spiritual-presence doctrine into one coherent position, not "
            "merely a form of words both parties could sign without either fully conceding."
        ),
        held_against=[
            "A live contest in Reformation historiography reads the same formula as deliberately "
            "elastic language - careful enough that Zurich's own more Zwingli-shaped signatories and "
            "Calvin could each sign it while privately holding closer to their own prior position, "
            "diplomatic accommodation rather than doctrinal breakthrough.",
            "No secondary scholarship on the Consensus Tigurinus specifically is vendored for this "
            "world (Doc_03 SS4), so this world's own characterization of the contest rests on the "
            "builder's own general knowledge of Reformation historiography, not a specific cited "
            "source - a real limit on how far this record can adjudicate the question rather than "
            "merely state that it exists.",
            "The formula's own two signatories left no surviving joint commentary explaining what "
            "each privately understood the language to concede - what is actually vendored is the "
            "signed text itself, not a record of the negotiation that produced it.",
        ],
        concedes=(
            "The suspicion that this was more diplomacy than doctrine cannot be closed by this "
            "world's own vendored record. What can be said: the document's own two signatories did "
            "not treat it as empty diplomacy at the time - each stood behind it as their own "
            "confession, not a mere accommodation - but that is evidence of sincerity, not proof "
            "against the elastic-language reading, since a diplomatically useful formula and a "
            "sincerely-held one are not mutually exclusive. This world's own record carries both "
            "readings forward, tagged, rather than resolving to one (Doc_06 SS2)."
        ),
        divergence_partners=[],
    ),
    dict(
        slug="zwinglis-remembrance-vs-negotiated-consensus",
        canon_cells=[],
        sources=[
            {"source_id": "rzg.source.zwingli-sixty-seven-articles", "locus": "Article XVIII, lines 4565-4569", "license": "public-domain"},
            {"source_id": "rzg.source.consensus-tigurinus", "locus": "9th Head of Agreement, lines 768-770", "license": "public-domain"},
        ],
        relations=[
            {"type": "associated-with", "target": "rzg.gravity.zwinglis-remembrance-reading-vs-negotiated-consensus"},
            {"type": "associated-with", "target": "rzg.term.memorial-commemoration"},
        ],
        claim=(
            "The Consensus Tigurinus's own 1549 statement of the Supper deepens and completes "
            "Zwingli's own 1523 remembrance doctrine rather than replacing or substantially revising "
            "it - the same conviction, more fully stated, not a different one."
        ),
        held_against=[
            "The two texts are read by some as marking a real theological shift, not a mere "
            "development: Zwingli's own 1523 language ('the mass is not a sacrifice, but is a "
            "remembrance of the sacrifice') states a chiefly commemorative view, while the 1549 "
            "formula's own insistence that 'we do not disjoin the reality from the signs' affirms "
            "something Zwingli's own earlier statement does not itself assert - a real communication "
            "of the thing signified, not only a remembering of it.",
            "This world's own build history records this question as genuinely unresolved rather "
            "than settled in either direction: Doc_03's own drafting found no basis in Doc_02 for "
            "characterizing the relationship one way or the other, and Doc_04's own gravity discovery "
            "states plainly that 'the degree to which the Consensus's own formula softens or modifies "
            "Zwingli's own original emphasis... is this document's own interpretive judgment, not an "
            "inherited finding.'",
        ],
        concedes=(
            "This world's own vendored record does not adjudicate which reading is correct, and this "
            "claim itself is this world's own stated preference, not a settled finding. What is not "
            "in question: both texts are genuinely ours, both are directly quoted and dated, and the "
            "institutional/textual separation between them (1523 and 1549, Zurich alone and both "
            "cities together) is real. We hold both because both are true of our own record, without "
            "needing to decide which one finally speaks for us."
        ),
        divergence_partners=[],
    ),
    dict(
        slug="anabaptist-schism-legitimacy",
        canon_cells=[],
        sources=[
            {"source_id": "rzg.source.zwingli-selected-works", "locus": "the 1527 Refutation of the Tricks of the Baptists", "license": "public-domain"},
        ],
        relations=[
            {"type": "associated-with", "target": "rzg.force.anabaptist-schism"},
            {"type": "associated-with", "target": "rzg.gravity.scripture-sole-authority-disputation-catechesis"},
        ],
        claim=(
            "The 1525 Swiss Brethren baptisms, and the broader Anabaptist movement they began, "
            "misread Scripture: a church gathered only by voluntary adult profession, rather than "
            "coextensive with a Christian city's own whole population, unmakes the very unity of "
            "church and city our own reform was built to strengthen, not divide."
        ),
        held_against=[
            "Those who took this step were themselves formed within our own founding circle - Conrad "
            "Grebel and Felix Manz were both formerly of our founder's own reform circle at Zurich - "
            "and understood themselves to be applying the identical scriptural-authority method (Sola "
            "Scriptura) our own reform itself established, pressed further rather than abandoned.",
            "Radical-Reformation historiography generally reads the magisterial Reformed refusal of "
            "believers'-baptism ecclesiology as a failure of the Reformed movement's own stated "
            "principle - if Scripture alone is to test every inherited practice, a reading of "
            "Scripture that removes infant baptism specifically should be answered on scriptural "
            "grounds alone, not suppressed as a civil and ecclesiastical threat to the city's own "
            "unity.",
            "Zurich's own council did not merely argue against the Anabaptists; it moved to suppress "
            "the movement by civil force in the years that followed the 1525 baptisms, a response "
            "this world's own vendored record (Zwingli's 1527 Refutation) frames as answering error "
            "with argument but which the broader historical record shows was not confined to argument "
            "alone.",
        ],
        concedes=(
            "We do not deny they read Scripture - we deny they read it whole, and that denial is "
            "itself a theological judgment about the relationship between church and city, not a "
            "neutral fact Scripture alone settles without a further interpretive commitment we bring "
            "to it. The Anabaptist party's own claim to be applying our own founding method "
            "consistently, only further, is not answered by this world's own vendored record beyond "
            "restating our own disagreement with where that consistency led. This world's own build "
            "does not narrate the civil suppression that followed the 1525 baptisms in detail, and "
            "this record does not supply that detail from outside this world's own vendored corpus."
        ),
        divergence_partners=[],
    ),
]


def emit(c: dict) -> Path:
    rid = f"rzg.contested.{c['slug']}"
    payload = {
        "id": rid, "world_id": WORLD_ID, "record_type": "contested_claim", "schema_version": SCHEMA_VERSION,
        "status": "draft", "register": "etic", "canon_cells": c["canon_cells"],
        "confidence": {
            "citation_specificity": "B", "verification_state": "verified-via-authority",
            "evidentiary_weight": "contested", "formation_confidence": "Contested",
            "divergence_note": None,
        },
        "sources": c["sources"], "relations": c["relations"],
        "claim": c["claim"], "held_against": c["held_against"],
        "concedes": c["concedes"], "divergence_partners": c["divergence_partners"],
    }
    path = OUT_ROOT / "contested_claim" / f"{rid}.md"
    body = (
        "Built from this world's own already-reviewed construction documents (Doc_03 SS4/Doc_06 SS2 for "
        "the CT term; Doc_04 SS3.5 for T2's own open judgment call; Doc_08 Force 2B-1 and Doc_05 SS2 for "
        "the Anabaptist schism), per Doc_03/Doc_04's own explicit disclosure that these are this world's "
        "own genuinely open questions, not settled findings this record adjudicates. register: etic, "
        "matching don's own precedent - a contested_claim states what is contested from outside this "
        "world's own voice, distinct from term/story/gravity's own emic register."
    )
    _write(path, payload, body)
    return path


def main() -> int:
    written = [emit(c) for c in CLAIMS]
    assert len(CLAIMS) == 3
    for p in written:
        print(p.relative_to(REPO_ROOT))
    print(f"\n{len(written)} contested_claim records written.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
