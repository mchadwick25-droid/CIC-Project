"""S6.2/Alexandria - S2.3-equivalent new authoring, BATCH 2 (alexlex016-030).

Same discipline as batch 1 (see s62_alx_s23_batch1.py): senses,
distance note, domain, grounding criterion, voice_surface (chunk-
grounded only), 3-axis confidence, typed reciprocal edges; EF verbatim
on the first edge (sourced from the chunk file); parkings removed.

New here: CROSS-BATCH MIRRORS - batch 2 edges that target batch-1
records append the reciprocal edge onto the target (idempotent: skipped
if an identical type+target edge exists).

Domains this batch: scripture-reading (016), salvation-arc (017-021),
christological-titles (022-024), formation-practices (025-028),
formation-authority (029-030).
"""
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))
TERMS = BACKEND / "wrs" / "records" / "alexandria_world" / "term"

from s62_alx_s23_batch1 import chunk_ef  # noqa: E402

CONF = {"citation_specificity": "B", "verification_state": "verified-via-authority",
        "verification_date": "2026-07-27"}

def conf(weight, level="Widely Accepted"):
    return {**CONF, "evidentiary_weight": weight, "formation_confidence": level}

E = lambda t, target, note: {"type": t, "target_id": target, "note": note}

A = {
 "alexlex016": dict(
  period_sense=("Not reading meanings into a text - reading OUT of it depths genuinely present, "
                "placed by the Logos who speaks through Scripture; the primary interpretive method "
                "through which Scripture's depths are actually reached in the school tradition "
                "(chunk Quick Meaning and EF)."),
  prior_sense=("Allegoria as inherited interpretive practice - the allegorical reading of Scripture "
               "as philosophy is the Philonic grammar this world entered (Doc_02 SS3.5; SS9 names "
               "allegoria/spiritual senses among the recurring inherited terms)."),
  modern_sense=("Allegory as a literary property of a constructed text - Pilgrim's Progress, Animal "
                "Farm - where the author builds the second meaning in; applied to exegesis, "
                "eisegesis (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern frame puts the second meaning in the author's construction "
                            "or the reader's invention; the world's allegory perceives what the "
                            "Logos placed - discovery, not construction (chunk World Hearing). "
                            "Sharp reversal of agency: high grounding criterion by rule."),
  semantic_domain="scripture-reading", grounding_criterion="high",
  voice_surface=("The word carries a prejudice that has to be named before it can do any work. "
                 "Allegory, as we practice it, is not putting a meaning into the text. It is the "
                 "perception of what the Logos has placed there."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex015", "The method operates under the orientation - allegory's moves are governed by Christological Reading (alexlex015 WM: orientation governs method)."),
    E("presupposes", "alexlex014", "The depths reached are Scripture's own - the method presupposes the address (chunk EF)."),
  ]),
 "alexlex017": dict(
  period_sense=("Hamartia - missing the mark: not first a list of wrong acts but the soul's "
                "mis-orientation, the whole self turned away from God who is its created telos; "
                "particular acts are expressions of the condition (chunk Quick/World Meaning)."),
  prior_sense=("Ordinary Greek hamartia, the archer's miss - the chunk itself carries the picture "
               "('the picture is from archery, and we take it exactly'); the world received the "
               "ordinary word and loaded it with the directional account."),
  modern_sense=("The forensic frame - sharpened after the Reformation and migrated into secular "
                "moral talk: sin as wrongdoing, law-breaking, guilt under sentence (chunk Modern "
                "Hearing)."),
  conceptual_distance_note=("Modern sin is legal standing; the world's hamartia is direction - a "
                            "soul turned from God, not a soul under sentence (chunk World Hearing). "
                            "Sharp frame inversion: high grounding criterion by rule."),
  semantic_domain="salvation-arc", grounding_criterion="high",
  voice_surface=("The Greek word is hamartia, and it means missing the mark. Not breaking a law, "
                 "not running up a debt - failing to arrive at what we were aimed at. An arrow "
                 "that misses is not guilty of anything. It has gone wrong in a different way."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex009", "Mis-orientation presupposes the created orientation - the image damaged but present is what makes the miss a miss (alexlex009 WM/EF; chunk EF: sin sets the problem the arc answers)."),
    E("presupposed-by", "alexlex018", "Death picks up exactly where sin leaves off (alexlex018 WM)."),
  ]),
 "alexlex018": dict(
  period_sense=("First the soul's progressive separation from God - the consequence of sin's "
                "turning, in which a soul cut off from the source of its life loses what that "
                "source supplied; physical dissolution follows as the outward seal (chunk "
                "Quick/World Meaning)."),
  prior_sense=("Ordinary Greek thanatos, biological death - the world's own teaching keeps the "
               "ordinary sense as the second, outward mode; noted from the chunk's own two-mode "
               "structure."),
  modern_sense=("Biological cessation, full stop - even the metaphors (a dead relationship) borrow "
                "from that (chunk Modern Hearing)."),
  conceptual_distance_note=("Modern death is an event at the end; the world's death is a condition "
                            "already operating - the soul's separation from its life-source, with "
                            "biology as seal, not definition (chunk World Hearing). Sharp gap: "
                            "high grounding criterion by rule."),
  semantic_domain="salvation-arc", grounding_criterion="high",
  voice_surface=("We do not sustain ourselves. Nothing does - to exist at all is to participate in "
                 "the ground of being. The soul that turns from the source of its life begins to "
                 "lose what that source was supplying. That is death, already at work."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex017", "Death follows sin's turning with a logic that needs no further cause (chunk WM)."),
    E("presupposed-by", "alexlex019", "Resurrection answers death's two modes in the same order (alexlex019 WM)."),
  ]),
 "alexlex019": dict(
  period_sense=("Neither a corpse reanimated nor a soul surviving death - the genuine reversal of "
                "what death names: the soul's reunion with God through the Logos who entered, "
                "spiritual death answered first, the body's share genuine (chunk Quick/World "
                "Meaning)."),
  prior_sense=("Ordinary Greek anastasis, rising/standing up - noted from standard lexica, "
               "UNVERIFIED against a registry source; the world's own two-mode account is the "
               "chunk's subject."),
  modern_sense=("Two thin hearings: the literalist corpse-reanimation, and the metaphorical "
                "spiritual-survival reading (chunk Modern Hearing)."),
  conceptual_distance_note=("Both modern readings answer only one of death's two modes; the world's "
                            "resurrection reverses both, in order - separation reunited, "
                            "dissolution reversed, inaugurated in Christ and operative now (chunk "
                            "World Hearing). Sharp gap: high grounding criterion by rule."),
  semantic_domain="salvation-arc", grounding_criterion="high",
  voice_surface=("Resurrection has to be heard against death - spiritual first, the soul's "
                 "separation from God; the body's dissolution following as the outward seal. It "
                 "answers both, in the same order."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex018", "The reversal is OF death's specific condition - the hinge of the arc (chunk EF)."),
    E("presupposes", "alexlex001", "Worked through the Logos who entered human nature (chunk QM)."),
    E("presupposed-by", "alexlex020", "Restoration is the trajectory the reversal opens (alexlex020 WM: Life re-entering what was dying)."),
  ]),
 "alexlex020": dict(
  period_sense=("The conviction that God's work is genuinely restorative - what sin damaged the "
                "Incarnation addresses, what death severed resurrection reunites; forward-looking: "
                "what is restored is a created potential, not a prior golden state (chunk "
                "Quick/World Meaning and World Hearing)."),
  prior_sense=("none-attested as a lexeme: a build-named conviction; the contested universalist "
               "extension (apokatastasis) is carried by its own entry, alexlex051, per the chunk's "
               "own Note - restoration itself is non-CT."),
  modern_sense=("Returning something to a prior condition - a restored painting, a restored "
                "building (chunk Modern Hearing)."),
  conceptual_distance_note=("Modern restoration looks backward to a prior state; the world's looks "
                            "forward to a potential never yet reached - completion, not return "
                            "(chunk World Hearing). Sharp directional gap: high grounding "
                            "criterion by rule."),
  semantic_domain="salvation-arc", grounding_criterion="high",
  voice_surface=("When the Logos entered human nature, the first thing that entry did was not to "
                 "teach new truths or model a new morality. The first thing was restoration - "
                 "Life re-entering what was dying."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex019", "The restorative trajectory runs through the accomplished reversal (chunk EF: joins problem-side to trajectory-side)."),
    E("presupposed-by", "alexlex021", "Transformation is restoration operating in the soul's ongoing formation (alexlex021 EF)."),
  ]),
 "alexlex021": dict(
  period_sense=("What the whole formation ecology is doing - the genuine reorientation of the soul "
                "toward God at the level of desire and perception, received rather than achieved; "
                "the operational name of the second Primary gravity (chunk Quick Meaning and EF)."),
  prior_sense=("none-attested as a lexeme: the build's operational name for the gravity's work in "
               "souls."),
  modern_sense=("Self-help, psychological development, or social change - all locating the source "
                "of change in the human being (chunk Modern Hearing)."),
  conceptual_distance_note=("Modern transformation is self-sourced; the world's is "
                            "encounter-sourced - the soul genuinely reoriented at the level of "
                            "desire, not improved at the level of behavior (chunk World Hearing). "
                            "Sharp agency inversion: high grounding criterion by rule."),
  semantic_domain="salvation-arc", grounding_criterion="high",
  voice_surface=("When we speak of the soul being transformed, we do not mean self-improvement. "
                 "The source of the change is not the person working on themselves. It is the "
                 "encounter with God, reordering desire itself."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex020", "Transformation enacts the restorative conviction in formation (chunk EF)."),
    E("presupposed-by", "alexlex007", "Participation is what the Transformation gravity is FOR - the sequence arrives there (alexlex007 EF)."),
    E("presupposed-by", "alexlex027", "Fasting enacts at the body's level what transformation works toward at the soul's (alexlex027 EF)."),
  ]),
 "alexlex022": dict(
  period_sense=("The Anointed One - not a surname but the confession this world staked itself on: "
                "the one the whole scriptural story was moving toward, in whom priest, king, and "
                "prophet are fulfilled; the confessional name organizing the formation's center "
                "(chunk Quick/World Meaning and EF)."),
  prior_sense=("Christos as the LXX's anointing vocabulary and the Jewish messianic expectation the "
               "confession answers - noted from the chunk's own scriptural frame (Peter's "
               "confession as paradigm); fuller pre-world career UNVERIFIED against a registry "
               "source."),
  modern_sense=("'Christ' functions as a name - the second half of 'Jesus Christ', swapped freely "
                "for 'Jesus'; the title's titular character has gone silent (chunk Modern "
                "Hearing)."),
  conceptual_distance_note=("The modern ear hears a name; the world spoke a confession with its "
                            "life staked on it (chunk World Hearing). Sharp gap of kind: high "
                            "grounding criterion by rule."),
  semantic_domain="christological-titles", grounding_criterion="high",
  voice_surface=("We do not say 'Jesus Christ' the way one says a name. We confess 'Jesus is the "
                 "Christ' - and that confession is not the end of an inquiry but the beginning of "
                 "one."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposed-by", "alexlex023", "Son of God names an aspect of the one this confession identifies (chunk EF: every Christological term does)."),
    E("presupposed-by", "alexlex024", "Word of God likewise - the titles organize around the confession (chunk EF)."),
  ]),
 "alexlex023": dict(
  period_sense=("Not an honorific for someone especially holy - the claim Nicaea defended: the Son "
                "is not a creature, however exalted, but genuinely God, of one substance with the "
                "Father; the ground of what formation claims to produce (chunk Quick/World Meaning "
                "and EF). Confessed in this form for the world's post-325 horizon specifically."),
  prior_sense=("The rival sense is the world's own record: the Arian hearing - Son of God as the "
               "highest honor for a created being - a position once formally held, carefully "
               "argued, explicitly weighed, and rejected (the chunk carries this as its own "
               "history, not as a modern error)."),
  modern_sense=("An honorific - uniquely holy, specially chosen, divinely inspired, perhaps divine "
                "in some softened sense (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern honorific hearing IS the ancient rejected position - the "
                            "chunk names the coincidence exactly; what it fails is not the Son's "
                            "honor but the ground of theosis: a soul formed toward an elevated "
                            "creature arrives at proximity, not participation (chunk World "
                            "Hearing/EF). Sharp gap with the world's own stakes: high grounding "
                            "criterion by rule."),
  semantic_domain="christological-titles", grounding_criterion="high",
  voice_surface=("What you have heard is not a careless misunderstanding. It was a position once "
                 "formally held, carefully argued, explicitly weighed - and then rejected. A soul "
                 "formed toward the most God-like creature is not a soul formed toward theosis; "
                 "the answer is real participation, because the Son is genuinely God."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex022", "An aspect-title of the confessed one (chunk EF)."),
    E("presupposed-by", "alexlex008", "Theosis is founded on the Son's genuine divinity - participation in an elevated creature would not deify (chunk EF)."),
  ]),
 "alexlex024": dict(
  period_sense=("Not first a name for the Bible - the eternal divine speech through whom God "
                "creates, reveals, teaches, and restores; Scripture is where that speech is heard, "
                "not what the phrase names (chunk Quick/World Meaning)."),
  prior_sense=("none-attested as a separate lexeme: the phrase's career IS the chunk's subject - "
               "John's prologue read as the world read it."),
  modern_sense=("'The Word of God' now means, almost exclusively, 'the Bible' (chunk Modern "
                "Hearing)."),
  conceptual_distance_note=("The modern synonym freezes the phrase onto the book; the world heard "
                            "the eternal speech the book carries - the bridge between the Logos "
                            "and Scripture as living formation instrument (chunk World Hearing and "
                            "EF). Sharp metonymic collapse: high grounding criterion by rule."),
  semantic_domain="christological-titles", grounding_criterion="high",
  voice_surface=("In the beginning was the Word. John's Gospel does not open by saying 'In the "
                 "beginning was the Scripture.' It opens with the divine speech through whom all "
                 "things were made - and the same prologue says that speech became flesh."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex022", "An aspect-title of the confessed one (chunk EF)."),
    E("presupposes", "alexlex001", "The title joins the eternal Logos to Scripture-as-instrument (chunk EF: the bridge)."),
  ]),
 "alexlex025": dict(
  period_sense=("Not a ceremony announcing a decision already made - a real threshold crossed in "
                "the body, in which the catechumen genuinely shares in Christ's death and "
                "resurrection and the soul's condition changes; the enacted entry catechesis leads "
                "toward (chunk Quick/World Meaning and EF)."),
  prior_sense=("Ordinary Greek baptizein, to dip/wash - noted from standard lexica, UNVERIFIED "
               "against a registry source; the world's own baptismal vocabulary of illumination "
               "(photismos) is attested at Doc_02 SS9."),
  modern_sense=("Either a public statement of private faith with no formative work of its own, or "
                "an empty ritual (chunk Modern Hearing)."),
  conceptual_distance_note=("Modern baptism announces what already happened; the world's baptism "
                            "DOES something - a threshold worked in the body, the nous opened "
                            "(chunk World Hearing). Sharp gap of efficacy: high grounding "
                            "criterion by rule."),
  semantic_domain="formation-practices", grounding_criterion="high",
  voice_surface=("Baptism is not the public announcement of a private decision. What we mean is a "
                 "threshold - a real crossing, worked in the body, in which the soul's condition "
                 "genuinely changes."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex003", "The threshold catechesis leads toward - entry into fuller participation (chunk EF)."),
    E("presupposed-by", "alexlex026", "The Eucharist is the recurring center baptism admits to (alexlex026 EF)."),
  ]),
 "alexlex026": dict(
  period_sense=("Not a memorial of something Christ did once - the community's recurring, bodily, "
                "shared enactment of what he is still doing: giving himself to be received; the "
                "practice that most directly does what every other practice prepares for (chunk "
                "Quick Meaning and EF)."),
  prior_sense=("Eucharistia, thanksgiving - the ordinary Greek word the practice's name keeps; "
               "noted from standard lexica, UNVERIFIED against a registry source."),
  modern_sense=("Either a backward-looking memorial meal, or a technical doctrine-word whose "
                "correct label substitutes for the reality (chunk Modern Hearing)."),
  conceptual_distance_note=("Memorial looks back at an absent Christ; the world's Eucharist shares "
                            "in a present one - the words 'real presence' name it without "
                            "beginning to say it (chunk World Meaning/World Hearing). Sharp tense "
                            "gap: high grounding criterion by rule."),
  semantic_domain="formation-practices", grounding_criterion="high",
  voice_surface=("The right words - real presence, the body and blood - are not wrong. But held on "
                 "their own they say what the Eucharist is called without beginning to say what it "
                 "is: the community's present sharing in the one who is always giving himself."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex025", "Entry precedes the recurring center (chunk EF)."),
    E("presupposes", "alexlex007", "The enacted participation - the practice most directly doing what the sequence moves toward (chunk EF)."),
    E("presupposed-by", "alexlex030", "The bishop's office centers on presiding at this act (alexlex030 WM)."),
  ]),
 "alexlex027": dict(
  period_sense=("Not going without food for health or spiritual credit - the training of desire in "
                "the body: the soul learning to govern what it reaches for, enacting bodily what "
                "transformation works toward (chunk Quick Meaning and EF)."),
  prior_sense=("Ordinary Greek nesteia, abstinence from food - noted from standard lexica, "
               "UNVERIFIED against a registry source."),
  modern_sense=("Either the diet hearing - restriction for health, a body-management technique - "
                "or ascetic credit-earning (chunk Modern Hearing)."),
  conceptual_distance_note=("Both modern hearings locate the meaning in the abstinence; the world "
                            "located it in the desire-training the abstinence enables (chunk World "
                            "Hearing). Sharp relocation: high grounding criterion by rule."),
  semantic_domain="formation-practices", grounding_criterion="high",
  voice_surface=("Fasting is not about the food. The abstinence is not the point; the "
                 "desire-training is. The soul learns, in the body, to govern what it reaches "
                 "for."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex021", "The bodily enactment of the soul's reorientation (chunk EF)."),
  ]),
 "alexlex028": dict(
  period_sense=("Not first speaking to God - the soul's turning to attend to the address God is "
                "always already making; the practice of listening for what the Logos is "
                "continuously saying (chunk Quick/World Meaning)."),
  prior_sense=("Ordinary Greek proseuche, petition/prayer-speech - noted from standard lexica, "
               "UNVERIFIED against a registry source; the world's own account keeps speech as the "
               "form and relocates the substance to attention."),
  modern_sense=("Talking to God - verbal speech aimed at a divine listener, with the speech-act at "
                "the center (chunk Modern Hearing)."),
  conceptual_distance_note=("Modern prayer speaks; the world's prayer attends - the address is "
                            "continuous, and the question is whether the soul is listening (chunk "
                            "World Hearing). Sharp direction reversal: high grounding criterion by "
                            "rule."),
  semantic_domain="formation-practices", grounding_criterion="high",
  voice_surface=("God is always teaching - through Scripture's difficulty, through the community's "
                 "life, through the suffering that opens what ease leaves closed. The address is "
                 "continuous. The question is whether the soul is attending."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex002", "Prayer attends to the continuous teaching - the pedagogy heard (chunk WM)."),
  ]),
 "alexlex029": dict(
  period_sense=("Not someone who delivers information but someone who accompanies formation - a "
                "teacher whose authority rests on wisdom the community can see has genuinely "
                "formed them; one pole of the Teacher-Bishop authority tension (chunk Quick "
                "Meaning and EF)."),
  prior_sense=("Ordinary Greek didaskalos, teacher/instructor - noted from standard lexica, "
               "UNVERIFIED against a registry source."),
  modern_sense=("The university classroom's teacher - the one at the front of the room delivering "
                "content; the distortion nearly invisible because the mapping is so easy (chunk "
                "Modern Hearing)."),
  conceptual_distance_note=("Modern teaching authority rests on knowing; the world's rested on "
                            "having become - visible wisdom, not credentials (chunk World "
                            "Hearing). Sharp ground shift: high grounding criterion by rule."),
  semantic_domain="formation-authority", grounding_criterion="high",
  voice_surface=("The question we ask of a teacher is not: who appointed you? It is: what have you "
                 "become, and can you see what the student cannot yet see?"),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex006", "The didaskalos's authority rests on demonstrated wisdom (chunk WM/EF)."),
    E("tension-with", "alexlex030", "The Teacher-Bishop tension both EFs name: authority grounded in demonstrated wisdom vs apostolic office - held, not resolved (chunk EF both entries)."),
  ]),
 "alexlex030": dict(
  period_sense=("Not a church administrator - the community's formation governor and Eucharistic "
                "president, whose office carries the apostolic succession; the other pole of the "
                "Teacher-Bishop tension (chunk Quick/World Meaning and EF)."),
  prior_sense=("Episkopos, overseer - the chunk itself opens from the ordinary sense ('Episkopos "
               "means overseer') and relocates what is overseen."),
  modern_sense=("The church administrator - the executive of a diocese managing clergy and "
                "finances (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern bishop administers an organization; the world's bishop "
                            "governs a formation ecology and presides at its enacted center "
                            "(chunk World Hearing). Sharp relocation of the office's object: high "
                            "grounding criterion by rule."),
  semantic_domain="formation-authority", grounding_criterion="high",
  voice_surface=("Episkopos means overseer, and among us the overseer does not oversee budgets or "
                 "buildings. The bishop oversees formation - and presides at the act that most "
                 "concentrates who we are."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex026", "The office's center is Eucharistic presidency (chunk WM)."),
    E("tension-with", "alexlex029", "The same held tension, from the office pole (chunk EF both entries)."),
  ]),
}

# Cross-batch mirror appends onto batch-1 records (idempotent)
APPEND = {
 "alexlex015": [E("presupposed-by", "alexlex016", "Allegory is the method this orientation governs (alexlex016 WM/EF).")],
 "alexlex014": [E("presupposed-by", "alexlex016", "The method reaches Scripture's own depths (alexlex016 EF).")],
 "alexlex009": [E("presupposed-by", "alexlex017", "Sin as mis-orientation presupposes the created orientation the image grounds (alexlex017 WM).")],
 "alexlex001": [E("presupposed-by", "alexlex019", "Resurrection works through the Logos who entered (alexlex019 QM)."),
                E("presupposed-by", "alexlex024", "Word of God is the Logos title bridging to Scripture (alexlex024 EF).")],
 "alexlex007": [E("presupposes", "alexlex021", "Participation is what the Transformation gravity arrives at (alexlex007 EF; alexlex021 EF)."),
                E("presupposed-by", "alexlex026", "The Eucharist enacts participation - the practice most directly doing what the sequence moves toward (alexlex026 EF).")],
 "alexlex008": [E("presupposes", "alexlex023", "Theosis is founded on the Son's genuine divinity (alexlex023 EF).")],
 "alexlex003": [E("presupposed-by", "alexlex025", "Baptism is the threshold catechesis leads toward (alexlex025 EF).")],
 "alexlex002": [E("presupposed-by", "alexlex028", "Prayer attends to the continuous teaching (alexlex028 WM).")],
 "alexlex006": [E("presupposed-by", "alexlex029", "Teaching authority rests on demonstrated wisdom (alexlex029 WM).")],
}

MARK = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "


def load(path):
    text = path.read_text(encoding="utf-8")
    parts = text.split("---\n")
    return yaml.safe_load(parts[1]), "---\n".join(parts[2:])


def save(path, rec, body):
    front = yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=100)
    path.write_text(f"---\n{front}---\n{body}", encoding="utf-8", newline="\n")


def apply():
    for rid, fields in A.items():
        path = TERMS / f"{rid}.md"
        rec, body = load(path)
        ef_text = chunk_ef(rid)
        wm = rec.get("world_meaning", "")
        i = wm.find("\n\n[Ecological Function")
        if i > 0:
            rec["world_meaning"] = wm[:i]
        rec.update(fields)
        if ef_text and rec.get("field_relations"):
            first = rec["field_relations"][0]
            if MARK not in first["note"]:
                first["note"] += " " + MARK + ef_text
        save(path, rec, body)
    appended = 0
    for rid, edges in APPEND.items():
        path = TERMS / f"{rid}.md"
        rec, body = load(path)
        fr = rec.setdefault("field_relations", [])
        for e in edges:
            if not any(x.get("type") == e["type"] and x.get("target_id") == e["target_id"]
                       for x in fr):
                fr.append(dict(e))
                appended += 1
        save(path, rec, body)
    print(f"authored batch 2: {len(A)} records; cross-batch mirrors appended: {appended}")


if __name__ == "__main__":
    apply()
