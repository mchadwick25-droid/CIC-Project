"""S6.2/Alexandria - S2.3-equivalent new authoring, BATCH 3 of 3 (alexlex031-045).

Same discipline as batches 1-2. Domains this batch: formation-authority
(031), formation-sequence (032, 037, 045), community-formation (033,
034, 043), scripture-reading (035), salvation-arc (036, 039),
formation-fruit (038, 042), divine-agency (040, 041, 044).
"""
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))
TERMS = BACKEND / "wrs" / "records" / "alexandria_world" / "term"

from s62_alx_s23_batch1 import chunk_ef  # noqa: E402
from s62_alx_s23_batch2 import load, save, MARK  # noqa: E402

CONF = {"citation_specificity": "B", "verification_state": "verified-via-authority",
        "verification_date": "2026-07-27"}

def conf(weight, level="Widely Accepted"):
    return {**CONF, "evidentiary_weight": weight, "formation_confidence": level}

E = lambda t, target, note: {"type": t, "target_id": target, "note": note}

A = {
 "alexlex031": dict(
  period_sense=("Not the Nicene Creed and not a doctrinal checklist - the received apostolic "
                "deposit carried across generations: what has always been taught, believed, and "
                "received; the constraint holding the Teacher-Bishop tension together, which both "
                "are accountable to and neither may override (chunk Quick/World Meaning and EF)."),
  prior_sense=("Received through the pre-Alexandrian rule-of-faith tradition the chunk's own Key "
               "Sources carry (Irenaeus's apostolic deposit, Tertullian's Prescription) - "
               "reception-formative texts rowed at the sweep (srcALX031/032)."),
  modern_sense=("Either the creed as a doctrinal checklist, or an anti-interpretive constraint "
                "(chunk Modern Hearing)."),
  conceptual_distance_note=("The modern object is a list to hold; the world's Rule is a living "
                            "formation inheritance within which interpretation works (chunk World "
                            "Hearing). Sharp gap of kind: high grounding criterion by rule."),
  semantic_domain="formation-authority", grounding_criterion="high",
  voice_surface=("What has always been taught, what has always been believed, what has always been "
                 "received - the Rule of Faith is the name for what that phrase points at. It "
                 "steadies us whenever interpretation threatens to drift."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposed-by", "alexlex029", "The teacher is accountable to the received inheritance (chunk EF)."),
    E("presupposed-by", "alexlex030", "The bishop guards what was received - the same accountability from the office pole (chunk EF)."),
  ]),
 "alexlex032": dict(
  period_sense=("Metanoia, a change of nous: not feeling sorry but the soul's highest faculty "
                "actually turned from what it was pointed at back toward God - the foundational "
                "response that opens the soul to formation (chunk Quick/World Meaning and EF)."),
  prior_sense=("Ordinary Greek metanoia, change of mind/afterthought - noted from standard lexica, "
               "UNVERIFIED against a registry source; the world's own reading loads the compound "
               "exactly (meta + nous, the chunk's opening move)."),
  modern_sense=("Feeling sorry - remorse or regret for wrong acts, measured by emotional intensity "
                "(chunk Modern Hearing)."),
  conceptual_distance_note=("Modern repentance is an emotion about the past; metanoia is a "
                            "reorientation of the soul's deepest perceptive faculty (chunk World "
                            "Hearing). Sharp relocation from feeling to direction: high grounding "
                            "criterion by rule."),
  semantic_domain="formation-sequence", grounding_criterion="high",
  voice_surface=("Meta-noia: a change of nous. Not a change of feeling, not a change of behavior - "
                 "a change in the soul's deepest faculty of perception, the capacity by which we "
                 "are oriented toward or away from God."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex011", "The turn happens IN the nous - metanoia is that faculty redirected (chunk WM)."),
    E("presupposed-by", "alexlex003", "Catechesis deepens what the turn opens - the person came for a transformation (alexlex003 WM; chunk EF: the directional change without which the sequence has nothing to deepen)."),
  ]),
 "alexlex033": dict(
  period_sense=("Martys, witness - not heroic self-sacrifice for a cause but the witness of a soul "
                "whose turning toward God has gone so deep that when persecution forces the "
                "choice, the orientation holds; the formation act showing the ecology reaches the "
                "whole community, not only its educated members (chunk Quick/World Meaning and "
                "EF)."),
  prior_sense=("The chunk's own etymology: the ordinary Greek martys, witness - a courtroom word "
               "the world kept exactly ('The word martyr means witness. Not hero. Not "
               "sacrifice.')."),
  modern_sense=("Either heroic ultimate sacrifice admired for courage, or (in current usage) "
                "someone with a persecution complex (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern martyr performs an extraordinary feat; the world's martyr "
                            "is the one in whom formation has simply held all the way down (chunk "
                            "World Hearing). Sharp gap of kind: high grounding criterion by "
                            "rule."),
  semantic_domain="community-formation", grounding_criterion="high",
  voice_surface=("The word martyr means witness. Not hero. Not sacrifice. Witness - the one whose "
                 "life, and in the decisive moment whose death, bears witness to the reality our "
                 "whole formation is organized around."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex037", "The witness is a turning gone deep - faith held to the end (chunk WM: a soul whose turning toward God has gone so deep)."),
  ]),
 "alexlex034": dict(
  period_sense=("The oikos - not the private nuclear family but the extended social and economic "
                "unit (householder, spouse, children, enslaved and freed persons, dependents) that "
                "is the primary formation environment for the community's majority (chunk "
                "Quick/World Meaning and EF)."),
  prior_sense=("Ordinary Greek oikos, the extended household unit - the chunk's own definition "
               "carries the social-historical sense directly."),
  modern_sense=("The nuclear family in its own private home, a sphere set apart from economy and "
                "public life (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern household is private and small; the oikos is a social and "
                            "economic unit spanning multiple positions, embedded in the community "
                            "- and it is where most formation happened for most believers (chunk "
                            "World Hearing/WM). Sharp scale-and-privacy gap: high grounding "
                            "criterion by rule."),
  semantic_domain="community-formation", grounding_criterion="high",
  voice_surface=("For most of us, the catechetical school is not where formation mainly happens. "
                 "The place where most formation occurs, for most believers, most of the time, is "
                 "the household."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex043", "The household is the majority's formation space within the called-out community (chunk EF)."),
  ]),
 "alexlex035": dict(
  period_sense=("Not analytical method applied to a text - the formation discipline through which "
                "the soul encounters the Logos who speaks through Scripture; the school "
                "tradition's primary formation mode, complementary to the sacramental, household, "
                "and witness channels (chunk Quick Meaning and EF)."),
  prior_sense=("none-attested as a lexeme: the entry names the world's own discipline; the "
               "inherited method within it is allegoria (alexlex016)."),
  modern_sense=("Analytical method applied to a text to determine its meaning - the interpreter as "
                "expert (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern interpreter produces a determination and is done; the "
                            "world's interpreter is being formed by the encounter (chunk World "
                            "Hearing). Sharp gap of purpose: high grounding criterion by rule."),
  semantic_domain="scripture-reading", grounding_criterion="high",
  voice_surface=("In common use, interpretation is what you do to a text that does not give up its "
                 "meaning at once - apply method, produce a determination. That is not the weight "
                 "we bring. Interpretation is the discipline through which the soul meets the "
                 "Logos who speaks."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposed-by", "alexlex016", "Allegory is the method within the discipline (alexlex016 EF; chunk EF)."),
    E("presupposes", "alexlex014", "The discipline is exercised on the address itself (chunk QM)."),
  ]),
 "alexlex036": dict(
  period_sense=("Not primarily acquittal from legal guilt - the healing, restoration, and "
                "reorientation of the soul toward God; what the entire formation ecology "
                "accomplishes, the second Primary gravity at the level of the whole ecology's "
                "purpose (chunk Quick/World Meaning and EF)."),
  prior_sense=("Ordinary Greek soteria, deliverance/health/rescue - noted from standard lexica, "
               "UNVERIFIED against a registry source; the healing register the world kept is "
               "closer to the ordinary sense than the later forensic frame."),
  modern_sense=("The forensic/judicial frame, sharpened after the Reformation: sin as crime, God "
                "as judge, salvation as the not-guilty verdict (chunk Modern Hearing)."),
  conceptual_distance_note=("The forensic frame addresses the wrong problem for this world: sin "
                            "here is directional, so salvation is healing and reorientation, not "
                            "acquittal (chunk World Hearing). Sharp frame gap: high grounding "
                            "criterion by rule."),
  semantic_domain="salvation-arc", grounding_criterion="high",
  voice_surface=("The word salvation carries a legal freight this world does not share. Sin here "
                 "is a directional condition, and the primary problem is not guilt. Salvation "
                 "genuinely changes what the soul is oriented toward - it heals."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex020", "Salvation-as-healing runs on the restorative conviction (chunk EF)."),
    E("presupposes", "alexlex039", "The healing enters through the Logos's incarnation (chunk QM)."),
  ]),
 "alexlex037": dict(
  period_sense=("Pistis - not intellectual assent to propositions but the soul's first genuine "
                "turning toward God in response to the Logos's address; the beginning of the "
                "formation journey, which every later stage continues (chunk Quick/World Meaning "
                "and EF)."),
  prior_sense=("Ordinary Greek pistis, trust/reliability - noted from standard lexica, UNVERIFIED "
               "against a registry source."),
  modern_sense=("Two inadequate hearings: intellectualist belief-assent to doctrines; or blind "
                "faith against evidence (chunk Modern Hearing)."),
  conceptual_distance_note=("Modern faith is a cognitive stance about propositions; the world's "
                            "pistis is the soul's orientation toward the one addressing it (chunk "
                            "World Hearing). Sharp relocation: high grounding criterion by rule."),
  semantic_domain="formation-sequence", grounding_criterion="high",
  voice_surface=("Pistis is the soul's first real response to the Logos's address. The catechumen "
                 "who does not yet understand deeply, who cannot yet perceive what the text holds "
                 "- but who genuinely orients toward what they hear - has faith."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposed-by", "alexlex003", "The sequence begins from the orientation faith names (chunk EF)."),
    E("presupposed-by", "alexlex033", "Witness is that orientation held all the way down (alexlex033 WM)."),
  ]),
 "alexlex038": dict(
  period_sense=("Agape - not primarily a feeling but the fruit of genuine formation: what wisdom "
                "looks like in the soul's relation to God and others once transformation has done "
                "its work; it cannot be commanded into existence (chunk Quick/World Meaning)."),
  prior_sense=("Ordinary Greek agapan/agape, to treat with regard - noted from standard lexica, "
               "UNVERIFIED against a registry source; the world's own scriptural grounding (1 "
               "Corinthians 13, 1 John 4) is carried in the chunk's Key Sources."),
  modern_sense=("First an emotion - warmth, affection, attachment rising toward particular people "
                "(chunk Modern Hearing)."),
  conceptual_distance_note=("Modern love is a feeling that arises; agape is what a formed soul "
                            "naturally expresses - fruit, not affect (chunk World Hearing). Sharp "
                            "relocation: high grounding criterion by rule."),
  semantic_domain="formation-fruit", grounding_criterion="high",
  voice_surface=("Love cannot be commanded into existence, and this is not a pastoral failure but "
                 "a truth about what love is. Agape is what the soul naturally expresses once "
                 "formation has genuinely worked."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex021", "The fruit of transformation's work in the soul (chunk EF)."),
  ]),
 "alexlex039": dict(
  period_sense=("The Logos - of one substance with the Father - genuinely entering human nature: "
                "not to give an example or deliver information but to restore what was dying from "
                "within; the pivotal act grounding the world's whole claim about transformation "
                "(chunk Quick/World Meaning and EF)."),
  prior_sense=("none-attested as a lexeme: the doctrine-name for the entry the world's own formula "
               "states; the formula itself is the world's received teaching (chunk WM: Clement and "
               "Origen before Athanasius)."),
  modern_sense=("The moral-example hearing (God became human to show how to live), or the "
                "information-delivery hearing (chunk Modern Hearing)."),
  conceptual_distance_note=("An example reaches the soul from outside; the world's Incarnation "
                            "restores from within - the difference between a model to imitate and "
                            "Life re-entering what was dying (chunk World Hearing). Sharp gap of "
                            "mechanism: high grounding criterion by rule."),
  semantic_domain="salvation-arc", grounding_criterion="high",
  voice_surface=("God became human so that humanity might become god. We do not receive this as a "
                 "careful proposition to be qualified into safety - it is the plain expression of "
                 "what the Incarnation is for."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex001", "The one who enters is the Logos through whom all things were made (chunk QM)."),
    E("presupposed-by", "alexlex008", "Theosis's formula is the Incarnation's purpose stated (alexlex008 WM)."),
    E("presupposed-by", "alexlex036", "Salvation-as-healing enters here (alexlex036 QM)."),
  ]),
 "alexlex040": dict(
  period_sense=("Mysterion - not what is unknown but what is known only from within: the depth of "
                "divine reality exceeding the surface of any approach; what governs formation's "
                "graduated character and preserves the always-more (chunk Quick/World Meaning and "
                "EF)."),
  prior_sense=("The Greek mystery-vocabulary of initiated knowledge stands behind the word - noted "
               "from standard accounts, UNVERIFIED against a registry source; the chunk's own "
               "definition ('accessible from within, not adequately sayable from without') is the "
               "world's received sense."),
  modern_sense=("Something not yet explained - a puzzle awaiting solution (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern mystery dissolves when solved; the world's mysterion "
                            "deepens as entered - inside-character, not information gap (chunk "
                            "World Hearing). Sharp inversion: high grounding criterion by rule."),
  semantic_domain="divine-agency", grounding_criterion="high",
  voice_surface=("Mysterion does not mean puzzle, or secret, or unsolved problem. It means a "
                 "sacred reality accessible from within - one that cannot be adequately said from "
                 "without."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposed-by", "alexlex003", "The graduated catechumenal shape enacts the mystery's from-within character (chunk EF: governs the graduated structure)."),
  ]),
 "alexlex041": dict(
  period_sense=("Oikonomia - household governance - God's overall governance of the plan of "
                "salvation: the encompassing arrangement God's saving work follows, not a rescue "
                "improvised after something went wrong; formation is a local share in it (chunk "
                "Quick/World Meaning and EF)."),
  prior_sense=("The chunk's own etymology: oikos + nomos, the ordinary Greek governance of a "
               "household - the received sense the theological usage extends."),
  modern_sense=("'Economy' as the financial economy - production, distribution, consumption "
                "(chunk Modern Hearing)."),
  conceptual_distance_note=("The modern economy is markets; the world's oikonomia is God's "
                            "household governance of creation toward its saving purpose (chunk "
                            "World Hearing). Sharp semantic drift: high grounding criterion by "
                            "rule."),
  semantic_domain="divine-agency", grounding_criterion="high",
  voice_surface=("Oikonomia - the governance of a household - is our word for the encompassing "
                 "plan God's saving work follows. Not a plan devised after something went wrong, "
                 "as though God improvised a rescue."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex002", "The economy's graduated character mirrors the divine pedagogy (chunk WM/Key Sources)."),
  ]),
 "alexlex042": dict(
  period_sense=("Arete - not excellence achieved through disciplined practice but the visible "
                "fruit of genuine transformation: what the soul looks like when formation has "
                "done its work; the concrete face of the transformation gravity (chunk "
                "Quick/World Meaning and EF)."),
  prior_sense=("The chunk carries the inherited sense whole: Greek arete as excellence, with "
               "Aristotle's virtue-as-the-mean named as the most systematic inherited account - "
               "received and re-grounded."),
  modern_sense=("Virtue as excellence of character built through habitual practice - achievement "
                "(chunk Modern Hearing)."),
  conceptual_distance_note=("The modern (and Aristotelian) virtue is what the person has achieved; "
                            "the world's is what formation has done to the person (chunk World "
                            "Hearing). Sharp agency inversion: high grounding criterion by rule."),
  semantic_domain="formation-fruit", grounding_criterion="high",
  voice_surface=("Arete came to us from the Greeks, where it meant excellence - a thing "
                 "functioning well according to its nature. Among us, virtue is not what the "
                 "person has achieved but what formation has done to the person."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex021", "The characterological expression of transformation's work (chunk EF)."),
  ]),
 "alexlex043": dict(
  period_sense=("Ekklesia, the called-out assembly - not a building or an institution with a "
                "membership roll but the formation community gathered around the Logos who gives "
                "himself to be shared; the environment within which the whole ecology operates "
                "(chunk Quick/World Meaning and EF)."),
  prior_sense=("The chunk's own etymology: ekklesia, the called-out assembly - the ordinary Greek "
               "civic-assembly word received and re-centered on the one who calls."),
  modern_sense=("Either a building or an institution - the place where Christians meet, or an "
                "organization with membership (chunk Modern Hearing)."),
  conceptual_distance_note=("The modern church is a place or organization; the ekklesia is the "
                            "assembly itself, constituted by its center, not its roll (chunk World "
                            "Hearing). Sharp gap of referent: high grounding criterion by rule."),
  semantic_domain="community-formation", grounding_criterion="high",
  voice_surface=("Ekklesia means the called-out assembly - not a building, not an organization. "
                 "The assembly of those called out from one life into another, gathered around "
                 "the Logos who called them."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("presupposes", "alexlex026", "Gathered around the one who gives himself to be shared - the Eucharistic center constitutes the assembly (chunk QM/WM)."),
    E("presupposed-by", "alexlex034", "The household is the majority's formation space within it (alexlex034 EF)."),
  ]),
 "alexlex044": dict(
  period_sense=("Not an occasional presence at special moments - the always-present agent of "
                "formation's transformative work: illumining perception, working the soul's "
                "reorientation; the divine person who makes the world's claims about "
                "transformation operative rather than aspirational (chunk Quick/World Meaning and "
                "EF)."),
  prior_sense=("Ordinary Greek pneuma, breath/wind/spirit - noted from standard lexica, UNVERIFIED "
               "against a registry source; the world's own post-Nicene defense of the Spirit's "
               "full divinity (Athanasius's Letters to Serapion) is carried in the chunks' Key "
               "Sources."),
  modern_sense=("Two opposite hearings: the charismatic (mainly present in extraordinary "
                "manifestations) and the functional-absence reading (chunk Modern Hearing)."),
  conceptual_distance_note=("Both modern hearings make the Spirit episodic; the world's Spirit is "
                            "the agent of the ordinary, continuous work (chunk World Hearing). "
                            "Sharp tempo inversion: high grounding criterion by rule."),
  semantic_domain="divine-agency", grounding_criterion="high",
  voice_surface=("The Spirit is not a visitor. The Spirit does not drop in on special occasions, "
                 "produce a manifestation, and depart until the next visitation. The Spirit is "
                 "the one through whom our ordinary, continuous work happens."),
  confidence=conf("load-bearing"),
  field_relations=[
    E("mechanism-behind", "alexlex021", "The agent through whom the transformation gravity is operative in the soul (chunk EF)."),
    E("presupposed-by", "alexlex021", "Typed mirror: transformation-as-operative presupposes the Spirit's agency (chunk EF)."),
  ]),
 "alexlex045": dict(
  period_sense=("Elpis - not optimism but the soul's sustaining orientation toward the divine life "
                "formation has been progressively opening yet not fully received; the posture "
                "that makes continued formation possible through the always-incomplete present "
                "(chunk Quick/World Meaning and EF)."),
  prior_sense=("Ordinary Greek elpis, expectation - noted from standard lexica, UNVERIFIED against "
               "a registry source."),
  modern_sense=("A forward-looking feeling - the expectation or wish that things will get better "
                "(chunk Modern Hearing)."),
  conceptual_distance_note=("Modern hope is a mood about outcomes; the world's elpis is an "
                            "orientation toward the horizon itself - not resilience psychology "
                            "(chunk World Hearing). Sharp relocation: high grounding criterion by "
                            "rule."),
  semantic_domain="formation-sequence", grounding_criterion="high",
  voice_surface=("Hope is not optimism. Theosis names the horizon no present stage has reached; "
                 "transformation names the work under way. Hope is the soul's sustaining "
                 "orientation toward what is opening but not yet fully received."),
  confidence=conf("corroborating"),
  field_relations=[
    E("presupposes", "alexlex008", "The orientation's object is the theosis horizon (chunk WM)."),
  ]),
}

APPEND = {
 "alexlex029": [E("presupposes", "alexlex031", "The teacher answers to the received inheritance (alexlex031 EF).")],
 "alexlex030": [E("presupposes", "alexlex031", "The bishop guards the same received inheritance (alexlex031 EF).")],
 "alexlex011": [E("presupposed-by", "alexlex032", "Metanoia is a change OF nous (alexlex032 WM).")],
 "alexlex003": [E("presupposes", "alexlex032", "The person came having turned - catechesis deepens the turn (alexlex032 EF)."),
                E("presupposes", "alexlex037", "The sequence begins from faith's orientation (alexlex037 EF)."),
                E("presupposes", "alexlex040", "The graduated shape enacts the mystery's from-within character (alexlex040 EF).")],
 "alexlex016": [E("presupposes", "alexlex035", "The method works within the formation discipline (alexlex035 EF).")],
 "alexlex020": [E("presupposed-by", "alexlex036", "Salvation-as-healing runs on the restorative conviction (alexlex036 EF).")],
 "alexlex001": [E("presupposed-by", "alexlex039", "The Incarnation is the Logos's own entry (alexlex039 QM).")],
 "alexlex008": [E("presupposes", "alexlex039", "The formula is the Incarnation's purpose stated (alexlex039 WM)."),
                E("presupposed-by", "alexlex045", "Hope's object is the theosis horizon (alexlex045 WM).")],
 "alexlex021": [E("presupposed-by", "alexlex038", "Agape is transformation's fruit (alexlex038 EF)."),
                E("presupposed-by", "alexlex042", "Arete is its characterological expression (alexlex042 EF)."),
                E("presupposes", "alexlex044", "Transformation operates through the Spirit's agency (alexlex044 EF - linkage mirror of its mechanism-behind edge).")],
 "alexlex014": [E("presupposed-by", "alexlex035", "Interpretation is the discipline exercised on the address (alexlex035 QM).")],
 "alexlex002": [E("presupposed-by", "alexlex041", "The economy's graduated character mirrors the pedagogy (alexlex041 WM).")],
 "alexlex026": [E("presupposed-by", "alexlex043", "The Eucharistic center constitutes the assembly (alexlex043 WM).")],
}


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
    print(f"authored batch 3: {len(A)} records; cross-batch mirrors appended: {appended}")


if __name__ == "__main__":
    apply()
