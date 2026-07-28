"""S6.2/Alexandria - S2.3-equivalent new authoring, BATCH 1 (alexlex001-015).

Authors onto the mechanical records: the four sense fields,
conceptual_distance_note, semantic_domain, grounding_criterion,
voice_surface, 3-axis confidence, and typed reciprocal field_relations
(absorbing the EF parkings' content into edge notes; parkings removed
where absorbed). Every claim traces to the chunk's own sections or a
named Doc_02 section; prior senses not developed in the build's own
documents are marked UNVERIFIED (Desert S2.3 precedent) or given as
none-attested where that is the honest answer.

Voice discipline (FLAG-005/CO-P2-03 lessons applied at authoring time):
voice_surface uses only the world's own images and statements from the
chunk's World Meaning - nothing minted, no invented aphorisms, no
persona claims.

Batch discipline (blueprint SS4): batch 1 of 3; two review rounds on
this first batch. Edges are batch-internal only (targets alexlex001-015);
cross-batch edges arrive with their target batches.

Deterministic re-application: reads each record, replaces the authored
fields, preserves everything else including the body (minus absorbed
EF parking).
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
TERMS = BACKEND / "wrs" / "records" / "alexandria_world" / "term"

CONF = {"citation_specificity": "B", "verification_state": "verified-via-authority",
        "verification_date": "2026-07-27"}

def conf(weight, level="Widely Accepted"):
    return {**CONF, "evidentiary_weight": weight, "formation_confidence": level}

E = lambda t, target, note: {"type": t, "target_id": target, "note": note}

A = {
 "alexlex001": dict(
  period_sense=("The eternal Word and Reason of God through whom all things were made, through whom "
                "God teaches, through whom Scripture speaks, and toward whom the soul is drawn back - "
                "identified with Christ, so that learning, Scripture, worship, and formation are one "
                "movement toward a single reality; the ground of reality itself, not one doctrine "
                "among many (chunk Quick/World Meaning)."),
  prior_sense=("Greek philosophy's cosmic reason and, decisively for this world, Philo's Logos as "
               "divine intermediary - the inherited grammar this world entered rather than built "
               "(Doc_02 SS3.5: allegorical reading, the Logos as intermediary, named as inheritance)."),
  modern_sense=("A technical concept from Hellenistic metaphysics the early church adopted for "
                "intellectual credibility - one doctrine among many, mainly for specialists (chunk "
                "Modern Hearing)."),
  conceptual_distance_note=("The modern ear files the Logos under 'doctrine'; this world lived it as "
                            "the ground under everything - the reality within which everything else is "
                            "believed, learned, prayed, and undergone, so that meeting truth anywhere "
                            "is already meeting the Logos (chunk World Hearing). Sharp gap: high "
                            "grounding criterion by rule."),
  semantic_domain="logos-center", grounding_criterion="high",
  voice_surface=("The Logos is not a borrowed abstraction. At the root of everything is the Word "
                 "through whom all things were made and in whom all things hold together. There are "
                 "not two roads, one for the mind and one for the heart - there is one Word, and to "
                 "think truly and to be formed truly are the same road walked at different depths."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposed-by", "alexlex002", "Divine pedagogy is the Logos teaching continuously - the EF names the Logos as the theological ground of both Primary gravities (chunk EF, Doc_04 C4)."),
    E("presupposed-by", "alexlex004", "Illumination is worked by the Logos through Scripture and formation (chunk QM)."),
    E("presupposed-by", "alexlex014", "Scripture is formative because it is where the Logos speaks (chunk EF)."),
    E("presupposed-by", "alexlex015", "Christological Reading is grounded in the Logos-Centered Unity: the Logos who speaks through the text is the Christ the reader meets (chunk EF)."),
    E("presupposed-by", "alexlex008", "Theosis runs through the Logos's incarnation - God became human so that humanity might become god (chunk WM)."),
  ]),
 "alexlex002": dict(
  period_sense=("The conviction that God is always teaching - Scripture's resistance, the practices "
                "of formation, suffering itself, and the slow deepening of understanding are all one "
                "curriculum under one Teacher who is always ahead (chunk Quick/World Meaning)."),
  prior_sense=("Carried into this world through paideia - Graeco-Roman formation-through-education - "
               "transformed from human curriculum to divine activity (Doc_02 SS9 names paideia/divine "
               "pedagogy among the recurring inherited terms; fuller pre-world development UNVERIFIED "
               "against a registry source)."),
  modern_sense=("'God's teaching style' - a method or technique, a supplement added to faith for "
                "those interested in growth (chunk Modern Hearing)."),
  conceptual_distance_note=("Modern hearing makes pedagogy one optional activity of God's among many; "
                            "this world heard ALL of creation, Scripture, community, and suffering as "
                            "the curriculum - nothing outside the teaching (chunk World Hearing). "
                            "Sharp gap: high grounding criterion by rule."),
  semantic_domain="logos-center", grounding_criterion="high",
  voice_surface=("Behind the catechist and the teacher and the bishop - behind even the hardship that "
                 "breaks open a heart argument could not reach - the same Teacher is at work. The "
                 "Logos who made all things did not fall silent afterward."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex001", "The pedagogy is the Logos's own continuing speech - remove the Logos and 'God teaches through everything' loses its subject (chunk WM/EF)."),
    E("presupposed-by", "alexlex003", "Catechesis is divine pedagogy's human-scale enactment - the EF: pedagogy makes the gravities intelligible as one divine activity (chunk EF)."),
  ]),
 "alexlex003": dict(
  period_sense=("The long, community-held, Scripture-formed process through which a person is "
                "gradually shaped into Christian life - begun from who the person is, not what they "
                "know; a transformation undertaken, not a doctrine-list accepted (chunk Quick/World "
                "Meaning)."),
  prior_sense=("Ordinary Greek katechein, to instruct by word of mouth - noted from standard lexica, "
               "UNVERIFIED against a registry source; the build's own documents develop the world's "
               "practice, not the word's earlier career."),
  modern_sense=("'Catechism' as a booklet of doctrinal questions and answers to memorize - "
                "information transfer, completed on recitation (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern object is a text mastered; the world's practice is a person "
                            "formed - someone who can repeat everything but whose desire is unreordered "
                            "has not yet begun (chunk World Hearing). Sharp gap: high grounding "
                            "criterion by rule."),
  semantic_domain="formation-sequence", grounding_criterion="high",
  voice_surface=("When someone comes to us and asks to enter, we do not sit them down for an "
                 "examination. They have come for a transformation, and that is what we begin. "
                 "Catechesis does not begin with what a person knows - it begins with who they are."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposed-by", "alexlex004", "Catechesis initiates the movement illumination carries forward - the EF names it the entry mechanism of the whole ecology (chunk EF)."),
    E("presupposes", "alexlex002", "The practice enacts the divine teaching - remove the conviction that God is always teaching and catechesis loses its ground (chunk EF)."),
    E("presupposes", "alexlex013", "Formation is invitation, not programming: it works through the soul's genuine response - remove autexousia and catechesis becomes manipulation (alexlex013 WM)."),
  ]),
 "alexlex004": dict(
  period_sense=("Not learning more facts but coming to SEE differently - a real change in the soul's "
                "perception, worked by the Logos through Scripture and formation; given, not "
                "generated; an advance in what the soul can perceive, not in what it knows about "
                "(chunk Quick/World Meaning)."),
  prior_sense=("The world's own baptismal vocabulary carried it as photismos - baptismal illumination "
               "(Doc_02 SS9 names photismos among the recurring terms; the chunk's Key Sources name "
               "the baptismal tradition). Pre-Christian philosophical light-imagery UNVERIFIED "
               "against a registry source."),
  modern_sense=("Either the historical Enlightenment, or a generic private insight - an intellectual "
                "achievement or a subjective feeling of clarity the person produces (chunk Modern "
                "Hearing)."),
  conceptual_distance_note=("Modern illumination is produced by the one illumined; this world's is "
                            "received - the change is in perception, not feeling, and the light is "
                            "given (chunk World Hearing). Sharp inversion of agency: high grounding "
                            "criterion by rule."),
  semantic_domain="formation-sequence", grounding_criterion="high",
  voice_surface=("A person can master the whole science of optics and sit in the dark; a child in "
                 "the sunlight, who knows none of it, sees. Illumination is that second thing - not "
                 "an advance in what the soul knows about, but in what it can perceive."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex003", "The entry process opens what illumination then works in - the sequence's own order (chunk EF: the hinge connecting the catechetical stage onward)."),
    E("presupposes", "alexlex001", "Worked by the Logos - the light is his (chunk QM)."),
    E("presupposes", "alexlex011", "What illumination most directly reaches is the nous - the mind's eye it opens (alexlex011 QM/EF)."),
    E("presupposed-by", "alexlex005", "Gnosis is what the soul does with what illumination lets it see (chunk EF)."),
  ]),
 "alexlex005": dict(
  period_sense=("Not secret teaching and not information mastered - the transformative knowing of God "
                "that illumination produces: knowing that changes the knower, inseparable from love, "
                "open to every believer, shown in a visibly reshaped life (chunk Quick/World Meaning "
                "and World Hearing)."),
  prior_sense=("Ordinary Greek gnosis, knowing/knowledge - and, pressing on the world from beside it, "
               "the rival esoteric claim of the Gnostic schools this world's own 'true gnostic' "
               "vocabulary answered (Doc_02 SS9 and Stream 12: gnosis/'true gnostic' named among the "
               "inherited-and-contested terms; the Gnostic challenge as an ongoing force)."),
  modern_sense=("Two problems at once: 'knowledge' as propositional content separable from the "
                "knower; and 'Gnostic' as esoteric, dualist, body-denying elitism (chunk Modern "
                "Hearing)."),
  conceptual_distance_note=("The modern ear hears either information or heresy; the world meant "
                            "contact with real divine being that changes the knower - the fruit of "
                            "formation, not a possession (chunk World Hearing). Sharp, doubled gap "
                            "(the Gnostic false-cognate rides beside the information false-cognate): "
                            "high grounding criterion by rule."),
  semantic_domain="formation-sequence", grounding_criterion="high",
  voice_surface=("There is a kind of knowing that leaves the knower unchanged - facts held as a "
                 "possession, mastered and set down. That is exactly what gnosis is not. Gnosis is "
                 "the knowing that changes the one who knows."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex004", "Gnosis works with what illumination lets the soul see (chunk EF: the stage between illumination and wisdom)."),
    E("presupposed-by", "alexlex006", "Wisdom is what genuine knowledge accumulates into across a life (alexlex006 EF)."),
  ]),
 "alexlex006": dict(
  period_sense=("What formation produces in a person over a lifetime - not a body of knowledge held "
                "but a condition of the soul, visible in how one perceives, loves, speaks, and lives; "
                "grown, never acquired (chunk Quick/World Meaning)."),
  prior_sense=("Ordinary and philosophical Greek sophia - and the personified Wisdom of Proverbs 8-9 "
               "and the Wisdom of Solomon, received by this world as anticipating the Logos (the "
               "chunk's own Key Sources carry the Proverbs/Wisdom reception; pre-world philosophical "
               "usage UNVERIFIED against a registry source)."),
  modern_sense=("Accumulated practical insight - the wisdom of age or folk sense - or theoretical "
                "knowledge in the academic sense (chunk Modern Hearing)."),
  conceptual_distance_note=("Modern wisdom accumulates from experience; this world's grows from "
                            "formation - what a soul looks like when genuine knowledge of God has "
                            "reached through the whole life (chunk World Hearing). Real gap, "
                            "moderate register: the modern sense is thin rather than inverted."),
  semantic_domain="formation-sequence",
  voice_surface=("Wisdom cannot be acquired. It can only be grown. No course of study ends in it; no "
                 "doctrinal mastery produces it. What produces wisdom is what the whole formation has "
                 "been working toward from the beginning."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex005", "Wisdom is gnosis reached through a whole life - the sequence's own order (chunk EF)."),
    E("presupposed-by", "alexlex007", "Participation expresses what wisdom has become - the EF ties wisdom to what participation expresses (chunk EF)."),
  ]),
 "alexlex007": dict(
  period_sense=("What the whole formation sequence arrives at - not nearness to God but real sharing "
                "in the divine life itself, placed carefully between two refused failures: the soul "
                "that merely approaches across an unclosed gap, and the soul dissolved into God "
                "(chunk Quick/World Meaning)."),
  prior_sense=("Platonic methexis - participation of particulars in forms - as the inherited "
               "philosophical frame; noted from standard accounts of the tradition, UNVERIFIED "
               "against a registry source."),
  modern_sense=("Involvement - taking part in activities, being included, contributing. Not false, "
                "but far too shallow (chunk Modern Hearing, its own words)."),
  conceptual_distance_note=("Modern participation is social involvement; the world meant ontological "
                            "sharing - a branch drawing life from the vine, not propped against it "
                            "(chunk World Hearing). Sharp gap in kind: high grounding criterion by "
                            "rule."),
  semantic_domain="formation-sequence", grounding_criterion="high",
  voice_surface=("When we say the soul participates in the divine life, we are not reaching for a "
                 "metaphor. Something real is shared - as a branch draws its life from the vine, not "
                 "as a branch propped against it."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex006", "Participation expresses the condition wisdom names (chunk EF: mechanism and goal of the Transformation gravity)."),
    E("presupposed-by", "alexlex008", "Theosis is participation's horizon - restored likeness through real sharing (alexlex008 QM)."),
  ]),
 "alexlex008": dict(
  period_sense=("The horizon toward which the whole formation life moves - not that the soul becomes "
                "God, but that through the Logos's incarnation and real participation the person is "
                "drawn into genuine divine life without the Creator-creature distinction collapsing; "
                "the formula held as long-received: God became human so that humanity might become "
                "god (chunk Quick/World Meaning)."),
  prior_sense=("The pagan apotheosis of heroes and emperors stands nearby as the false cognate the "
               "world's own careful usage guards against - noted from standard accounts, UNVERIFIED "
               "against a registry source; the world's own formula is attested in its record (chunk "
               "WM: Clement's gnostikos 'becoming god', Athanasius ch. 54)."),
  modern_sense=("'Aren't you saying humans become God?' - heard as pantheism or hubris, collapsing "
                "the Creator-creature distinction (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern ear hears the distinction collapsing; the world's theosis "
                            "PRESUPPOSES it - genuine participation without absorption, dissolution, "
                            "or confusion (chunk World Hearing). Sharp gap on the exact point the "
                            "formula turns on: high grounding criterion by rule."),
  semantic_domain="formation-sequence", grounding_criterion="high",
  voice_surface=("The formula is audacious and is best stated plainly: God became human so that "
                 "humanity might become god. It must be heard exactly - the creature genuinely "
                 "shares the divine life, and remains creature."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex007", "Theosis is what real participation opens onto (chunk EF: anchors the sequence's eschatological horizon)."),
    E("presupposes", "alexlex001", "The formula runs through the incarnate Logos (chunk WM/Key Sources)."),
  ]),
 "alexlex009": dict(
  period_sense=("The indelible mark in every human being that makes formation possible - not a "
                "quality earned or lost but the ontological ground of the soul's capacity for God, "
                "damaged by sin yet present, which is why the person can be restored (chunk "
                "Quick/World Meaning and World Hearing)."),
  prior_sense=("Grounded directly in the Genesis text ('in our image, according to our likeness' - "
               "the chunk's own foundational citation); no separate pre-world lexical career is "
               "developed in the build's documents - none-attested is the honest answer."),
  modern_sense=("A moral and political claim - intrinsic dignity and rights because humans bear "
                "God's image. Not false, but it relocates the image (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern reading makes the image a status conferring rights; the world "
                            "read it as capacity - the reason formation, illumination, and real "
                            "participation are possible at all (chunk World Hearing). Real gap of "
                            "location rather than inversion; the dignity reading is downstream, not "
                            "wrong."),
  semantic_domain="anthropology",
  voice_surface=("Everything we say about the human person rests on one conviction: we are made in "
                 "the image of God. Not a graceful way of saying we are impressive among the animals "
                 "- the ground of the soul's capacity for God."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposed-by", "alexlex012", "The likeness is the image's goal - given mark, grown resemblance (alexlex012 WM: the two Genesis words held distinct)."),
    E("presupposed-by", "alexlex010", "The soul is the image-bearer - its whole anthropology stands on the image (alexlex010 QM; chunk EF: the foundational claim the cluster presupposes)."),
  ]),
 "alexlex010": dict(
  period_sense=("Not a ghost inhabiting a body - the whole human person understood as a being made "
                "for God: the image-bearer, animated through the body, oriented toward God by "
                "nature; the subject every formation practice addresses (chunk Quick/World Meaning "
                "and EF)."),
  prior_sense=("Ordinary Greek psyche, life/soul, with the Platonic soul-body frame standing close "
               "enough that the world's own teaching had to refuse the prison-of-the-soul reading "
               "(chunk WM refuses it explicitly); pre-world usage beyond that refusal UNVERIFIED "
               "against a registry source."),
  modern_sense=("Two opposite readings, both failing: the popular-religious inner ghost that "
                "survives death as the 'real self'; or the reductive reading where soul is a poetic "
                "fiction (chunk Modern Hearing)."),
  conceptual_distance_note=("Both modern readings miss the orientation that defines the term: the "
                            "soul is the whole person as oriented toward God - neither "
                            "ghost-in-a-machine nor metaphor (chunk World Hearing). Sharp doubled "
                            "gap: high grounding criterion by rule."),
  semantic_domain="anthropology", grounding_criterion="high",
  voice_surface=("It is easy to picture the soul as an inner resident - a spirit lodged in flesh, "
                 "waiting to be freed from its prison. That is not what psyche means for us, and it "
                 "is precisely the account we refused."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex009", "The soul's capacity for God IS the image borne (chunk QM)."),
    E("presupposed-by", "alexlex011", "The nous is the soul's highest faculty - its deepest part (alexlex011 QM/WM)."),
  ]),
 "alexlex011": dict(
  period_sense=("The highest faculty of the soul - the capacity for direct, non-discursive "
                "perception of divine reality, the mind's eye that illumination opens and "
                "contemplation deepens; a seeing rather than a working-out (chunk Quick/World "
                "Meaning)."),
  prior_sense=("Greek philosophical nous - intellect/mind as the highest cognitive faculty - the "
               "inherited frame this world re-tasked toward perception of God; noted from standard "
               "lexica, UNVERIFIED against a registry source."),
  modern_sense=("'Intellect' as abstract reasoning or raw cleverness - forming the nous would then "
                "mean education or doctrinal mastery (chunk Modern Hearing)."),
  conceptual_distance_note=("Modern intellect argues; the world's nous perceives - more like sight or "
                            "contact than argument, and its formation is purification, not schooling "
                            "(chunk World Hearing). Sharp gap: high grounding criterion by rule."),
  semantic_domain="anthropology", grounding_criterion="high",
  voice_surface=("Beneath the mind that reasons from one thing to the next, the soul has a faculty "
                 "of a different kind: a seeing rather than a working-out. This is the nous - the "
                 "part of us illumination most directly reaches."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex010", "The nous is the soul's own depth, not a separate organ (chunk QM)."),
    E("presupposed-by", "alexlex004", "Illumination opens the mind's eye - the faculty it most directly reaches (chunk WM)."),
  ]),
 "alexlex012": dict(
  period_sense=("What the Image of God becomes through formation - not a separate gift but the image "
                "progressively restored and fulfilled, visible in the quality of a person's "
                "perceiving, loving, and living; the image is given, the likeness is grown (chunk "
                "Quick/World Meaning)."),
  prior_sense=("Grounded in the Genesis pair itself - eikon and homoiosis held distinct by the "
               "world's own exegesis (chunk WM quotes the two words); no separate pre-world lexical "
               "career developed - none-attested."),
  modern_sense=("'Becoming like God' as moral imitation - modeling conduct on the divine example, a "
                "behavioral program (chunk Modern Hearing)."),
  conceptual_distance_note=("The moral qualities the modern hearing notices are real, the world says "
                            "so - but they are fruit, not program: the likeness is the image "
                            "restored through formation, not conduct imitated (chunk World Hearing). "
                            "Real gap of mechanism; moderate register."),
  semantic_domain="anthropology",
  voice_surface=("There are two words in the text, and they are not synonyms. The image is what "
                 "every one of us is simply by being human. The likeness is what formation grows "
                 "that image toward."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex009", "The likeness is the image's goal - nothing to grow without the given mark (chunk WM)."),
  ]),
 "alexlex013": dict(
  period_sense=("Genuine self-determination - the soul's capacity for real response that makes "
                "formation formation rather than manipulation; God forms through the soul's freedom, "
                "never around it (chunk Quick/World Meaning)."),
  prior_sense=("Stoic and broader Hellenistic autexousia/self-determination as the inherited "
               "philosophical vocabulary; noted from standard lexica, UNVERIFIED against a registry "
               "source."),
  modern_sense=("Freedom as freedom FROM - constraint, direction not chosen; the free person as the "
                "autonomous one who sets their own ends (chunk Modern Hearing)."),
  conceptual_distance_note=("Modern freedom is absence of direction; the world's autexousia is "
                            "capacity FOR response within formation - the soul genuinely answers, "
                            "which is exactly why formation is invitation and not programming (chunk "
                            "World Hearing/EF). Sharp inversion of valence: high grounding criterion "
                            "by rule."),
  semantic_domain="anthropology", grounding_criterion="high",
  voice_surface=("If the soul had no genuine freedom - no real power to respond or refuse - then "
                 "what we practice would be manipulation: the soul remade without its part in the "
                 "remaking. What came of that would not be growth."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposed-by", "alexlex003", "Catechesis works through genuine response - the EF: freedom sets the ecology's mode as invitation (chunk EF)."),
  ]),
 "alexlex014": dict(
  period_sense=("Not a historical document recording what God once said - the living address of the "
                "Logos speaking now, through the text, to the soul formed to hear; read as "
                "encounter, held in a formative relationship (chunk Quick/World Meaning)."),
  prior_sense=("none-attested as a lexical prior: the entry's frame is the world's reading practice, "
               "not a pre-world career of the word - the practice's own inheritance (allegorical "
               "reading of Scripture as philosophy) is the Philonic grammar (Doc_02 SS3.5)."),
  modern_sense=("Either fixed divine propositions to believe, or ancient human documents to analyze "
                "- both making Scripture a text FROM the past (chunk Modern Hearing)."),
  conceptual_distance_note=("Both modern readings freeze the text in the past; the world read a "
                            "present address - the task is not correct interpretation but formed "
                            "hearing (chunk World Hearing). Sharp gap in tense: high grounding "
                            "criterion by rule."),
  semantic_domain="scripture-reading", grounding_criterion="high",
  voice_surface=("The reading Scripture asks for here is not study but encounter. Study produces "
                 "information and stops. To read Scripture is to come before one who is genuinely "
                 "speaking - now, to you."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex001", "Scripture forms because the Logos speaks in it (chunk EF: the primary vehicle of the first Primary gravity)."),
    E("presupposed-by", "alexlex015", "Christological Reading is the orientation that makes Scripture-as-address operable (alexlex015 EF)."),
  ]),
 "alexlex015": dict(
  period_sense=("An orientation, not a method: the conviction that Scripture at every level is the "
                "address of the Logos who is Christ - what governs the interpretive moves and gives "
                "them their purpose; what the text does to a reader formed to hear it (chunk "
                "Quick/World Meaning and World Hearing)."),
  prior_sense=("none-attested: a build-named orientation of this world's own practice, not an "
               "inherited lexeme."),
  modern_sense=("Eisegesis - reading a later Christian meaning into texts that do not carry it "
                "(chunk Modern Hearing)."),
  conceptual_distance_note=("The modern worry runs reader-to-text (imposition); the world's claim "
                            "runs text-to-reader (address) - the Logos who speaks through Scripture "
                            "is the Christ the formed reader meets (chunk World Hearing). Sharp "
                            "reversal of direction: high grounding criterion by rule."),
  semantic_domain="scripture-reading", grounding_criterion="high",
  voice_surface=("Allegory is a method - moves a reader makes. This is not that. It is the "
                 "orientation that governs the moves: the one who speaks through the text is the "
                 "one the reader is being formed to meet."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex014", "The orientation operates the world's Scripture-as-address conviction (chunk EF)."),
    E("presupposes", "alexlex001", "Grounded in the Logos-Centered Unity (chunk EF, Doc_04 C4)."),
  ]),
}


def chunk_ef(rid: str) -> str:
    """EF verbatim from the SOURCE CHUNK (the migration source of record)
    - idempotent by construction, immune to record-state history (an
    earlier two-run sequence lost the record-side EF text; caught by the
    marker check, root cause: a silent no-op patch + dict-replacement of
    field_relations)."""
    chunks = BACKEND / "data" / "alexandria_world" / "lexicon_chunks"
    hits = list(chunks.glob(f"{rid}_*.md"))
    if not hits:
        return ""
    text = hits[0].read_text(encoding="utf-8")
    m = re.search(r"^## Ecological Function\s*\n(.*?)(?=^## |\Z)", text,
                  re.S | re.M)
    if not m:
        return ""
    body = re.sub(r"^-{3,}\s*$", "", m.group(1), flags=re.M).strip()
    return body


def apply():
    changed = 0
    for rid, fields in A.items():
        path = TERMS / f"{rid}.md"
        text = path.read_text(encoding="utf-8")
        parts = text.split("---\n")
        rec = yaml.safe_load(parts[1])
        body = "---\n".join(parts[2:])
        # absorb the EF parking per Desert's FLAG-002 resolution: the EF
        # text rides VERBATIM on the first field_relations edge note
        # (never summarized-away), then the parking leaves world_meaning
        ef_text = chunk_ef(rid)
        wm = rec.get("world_meaning", "")
        i = wm.find("\n\n[Ecological Function")
        if i > 0:
            rec["world_meaning"] = wm[:i]
        rec.update(fields)
        MARK = ("Chunk Ecological Function (verbatim, absorbed per "
                "FLAG-002): ")
        if ef_text and rec.get("field_relations"):
            rec["field_relations"][0]["note"] += " " + MARK + ef_text
        front = yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=100)
        path.write_text(f"---\n{front}---\n{body}", encoding="utf-8", newline="\n")
        changed += 1
    print(f"authored batch 1: {changed} records")


if __name__ == "__main__":
    apply()
