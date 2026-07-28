"""S6.2 S2.6-equivalent - Alexandria contested_claim records + term-side links.

Record set (5): the Completion Standard's minimum is the world's
Primary-gravity claims - C1 (alexclaim001) and C2 (alexclaim002) - plus
the three contests the S2.3 close-out manifest routed here: Homoousios
(alexclaim003, the governed alexlex081 contest surfaced by the christology
cluster), the Didaskaleion (alexclaim004, the governed alexlex059 contest
surfaced at Teacher), and the Origen inheritance (alexclaim005). The
Origen-cluster CTs - Nous alexlex011, Apokatastasis alexlex051, Logikos
alexlex090, Fall/Descent alexlex074 - share ONE underlying contest per
Doc_06 SS2's own cross-references (the Nous entry: "the same Meaning
contest carried by Apokatastasis, to which it is theologically linked"):
whether Origen's speculative stratum is the same position as the
553-condemned propositions. One world-level claim record covers it
(inheritance-and-unease is a WORLD-LEVEL feature per Doc_04 T3, recorded
as a property of the ecology); the per-term contest text remains governed
at Doc_06 SS2's authority table and the term parkings. alexlex033's
Reported-Experience Status is applied as confidence calibration inside
alexclaim002's concedes - the closeout routed it as calibration input,
NOT a contest, and it gets no claim of its own and no term-side link.

Field discipline (Desert S2.6 carried):
- claim: what the world actually holds, in its own terms - drawn from the
  chunks' World Meaning/parkings, Doc_04's gravity language, and Doc_08's
  Layer-2 texts, not invented.
- held_against[]: ONLY contests documented in the record, named
  challenger, sourced. Alexandria's are richer than Desert's: real
  documented rivals (Gnostic teachers, Neoplatonic schools, Arius) plus
  the record's own limits (the stratum asymmetry; Eusebius's single-
  narrator mediation; the divided-scholarship Meaning contest) read
  against the claims.
- concedes: the world's genuine unsettledness as data - every hedge from
  Doc_04's cross-checks and Doc_06 SS2 carried, none smoothed.
- pressure_response: the record's own documented response patterns
  (formation-for-all against the Gnostic rival, 2A-1 L2; the
  descending-Word answer, 2A-2 L2; relief-and-burden, 2A-4 L2; the
  registers-kept-distinct discipline from the Homoousios parkings; the
  authority-does-not-depend-on-the-institution move from alexlex029's
  parking) - no invented aphorisms.
- divergence_partners[]: mapped against the five partner worlds' OWN
  Doc_04 classification summaries, re-read for this step (PAHC SS5: two
  Primaries G02 correspondence network + G07 Eucharist, G01 authority
  consolidation Supporting/Contested, G05 boundary-drawing Tensional,
  G06 household did-not-reach; HAL SS3: G1 hebraica veritas, G2 ascetic
  self-impoverishment, G3 patronage-as-authority Primary, G6 controversy
  Supporting; IJC SS4: juridical primacy / church-state alliance /
  orthodoxy-enforcement Primary, 6 sacramental-vs-positional Tensional;
  Syriac SS4: C1 typological method + C2 covenanted ascetic life Primary,
  C3 heresiological self-definition + C5 Diatessaron Supporting, C4
  authority-structure ambiguity Tensional; Desert: the live record store).
  partner_claim_id IS set toward Desert where its own contested_claim
  records carry the genuine counterpart (desertclaim001 withdrawal,
  desertclaim003 elder authority, desertclaim006 scriptural engagement) -
  the schema's "once it exists" condition is met, Desert being migrated;
  the REVERSE enrichment (Desert records pointing back here) stays S6.3
  work, not this step's Touches. Partners without a counterpart record
  carry note-only mappings.

Term-side: contested_claim_ids populated at claim-authoring time on the
twelve terms the claims ride (the routed surfacing set + the terms each
Primary claim's own text names) - closing the FLAG-014 sequencing gap FOR
ALEXANDRIA at the step where Desert left it open (Desert's own backfill
remains FLAG-014's open CO, a Mark call - no Desert term is touched).
Read-modify-write goes through the FLAG-023 fence-asserting reader.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

import yaml
from s62_alx_source_rows import emit_record
from s62_alx_s25 import read_record

OUT = BACKEND / "wrs" / "records" / "alexandria_world"

COMMON = {"world_id": "alexandria-catechetical", "record_type": "contested_claim",
          "schema_version": 1, "jobs": [8], "register": "emic",
          "review_state": "draft"}

S = lambda *ids: [{"source_id": i} for i in ids]

CLAIMS = [
 dict(id="alexclaim001",
      sources=S("srcALX001", "srcALX002", "srcALX003", "srcALX013"),
      claim="Scripture is the deep formative reality: the text has depths that open only to the prepared soul, and reading at depth - allegory, interpretation, the whole discipline of the school - is itself how the reader is formed. The reader is transformed by the reading, not merely informed; the deep reading this world prizes is a capacity of the soul, not merely a skill of the eyes - the text's depths are perceived, not decoded. Philosophical training clears the ground and Scripture is read last, at the deepest register, once the soul is prepared to receive it; the teaching tradition, the worship-lectionary, and catechetical formation all organize around the book.",
      held_against=[
        {"challenge": "The Gnostic teachers of the same city - Valentinian and Basilidean movements sharing the school's own formal features (teachers, sophisticated Scripture engagement, gnosis claims) - read the same text toward a knowing reserved for a secret few and a rejection of the body and its Maker. The nearness was the danger: rivals speaking the same words and meaning something the community could not accept, the ecology's most sustained early/mid-horizon boundary challenge (Doc_08 2A-1).",
         "challenger": "the Valentinian and Basilidean teachers - rivals inside the same city, speaking the same words",
         "sources": S("srcALX008")},
        {"challenge": "The world's own surviving record, read against its stratum: every stream attesting Scripture-at-depth is literate, Greek-speaking, and educated, while the ecology's majority was non-literate, Coptic-speaking, and rural. Multi-stream agreement within one stratum is not ecology-wide confirmation (the Cross-Stratum Test, Doc_04 SS5 - the central finding); the papyrological and archaeological record documents the majority's observable channels (baptism, assembly, the calendar), not depth-reading.",
         "challenger": "the world's own evidence base, read against its stratum asymmetry (Doc_04 SS5; OG-4)",
         "sources": S("srcALX025", "srcALX026")}],
      concedes="The systematized multilevel allegorical method is Origen-concentrated - capped at Dominant Modern Reconstruction for any ecology-wide method claim (Doc_04 SS3.1, Discipline One). Whether Scripture-at-depth organized the whole ecology's formation, and not the school's alone, our record cannot establish: ecology-wide primacy is held OPEN, not asserted (Doc_04 SS5, deferred to Article 31 external review), and the non-literate majority's formation is a named gap the record must not fill.",
      pressure_response="Answers the rival reader by reading - meeting the challenger on the shared text and out-reading him (the Contra Celsum pattern), saying plainly what true knowing is and that it is for all, not a secret few (Doc_08 2A-1 L2); and holds depth-reading accountable to the Rule of Faith, the boundary within which speculation stays exploration (the Rule as what apostolic teaching actually said, alexlex031). The response register is pedagogical, not polemical: the school's answer to a bad reading is a better one.",
      divergence_partners=[
        {"world_id": "desert-monasticism",
         "partner_claim_id": "desertclaim006",
         "note": "Their own claim record: Scripture engaged practically and occasionally - deployed within sayings measured to a specific disciple's situation, not expounded systematically; hearing issues in doing. Reading-as-curriculum vs. text-as-portable-word - a genuine divergence, documented on both sides of the live store."},
        {"world_id": "syriac-edessa-nisibis",
         "note": "Their Doc_04 Primary C1 is the Symbolic/Typological Theological Method - a genuinely different deep-reading discipline (type and symbol, not multilevel allegory) - and their Supporting C5 holds the Diatessaron as normative Gospel: even the given text-form differs from this world's given Greek text (the Septuagint, Doc_08 1A-2)."},
        {"world_id": "hieronymian-ascetic-literary",
         "note": "Their Doc_04 Primary G1 is hebraica veritas - the authority of the corrected Hebrew text. Scripture's depth sought through textual-critical return to the original vs. this world's given Greek text (the Septuagint, 'not chosen, but given' - Doc_08 1A-2) read for perceived depths."},
        {"world_id": "post-apostolic-house-church",
         "note": "Their Doc_04's two Primaries are the translocal correspondence network (G02) and eucharistic practice (G07): Scripture circulating as letters read in assembly, formation organized around the meal and the correspondence network - no reading-at-depth curriculum in their gravity set (their G06 household candidate did not reach gravity status, per their own SS5)."},
        {"world_id": "imperial-juridical-christianity",
         "note": "Their Doc_04 Primary 3 is orthodoxy-enforcement through imperial power: the text's permitted meaning bounded and enforced juridically - against this world's school, where the same text is opened speculatively under the Rule of Faith."}]),
 dict(id="alexclaim002",
      sources=S("srcALX001", "srcALX002", "srcALX003", "srcALX015", "srcALX017", "srcALX029"),
      claim="Formation is the transformation of the soul toward God: to believe is only the beginning - the soul was made to KNOW God, to be changed by that knowing, and to go on being drawn deeper because the One it seeks cannot be exhausted. The change is an actual remaking of the person (purification, illumination, union - the active process, distinct from theosis, the endpoint), and the ascent this world knows runs through a Word who came DOWN - through flesh and sacrament and shared life, not the soul climbing alone.",
      held_against=[
        {"challenge": "The Neoplatonic schools - as the shared Platonic current matured under Plotinus and Porphyry into an articulate institutional rival with its own teachers and students - offered the same ascent with no Word made flesh at its end: purification and return to the One without Incarnation, sacraments, or community (Doc_08 2A-2). Fellow-seekers become rival school; the difference had to be said plainly.",
         "challenger": "the Neoplatonic schools (Plotinus, Porphyry) - the ascent without Incarnation",
         "sources": S("srcALX015")},
        {"challenge": "Arius - from within the community - taught the Son as the highest creature ('there was when he was not'), contesting the transformation claim's ground from within: the controversy forced the claim's Incarnation-grounded configuration into dominance, promoting an already-available account under pressure (Doc_08 2A-4 L3; Doc_04 SS3.2 persistence: the mechanism SHIFTS at Nicaea under Arian pressure).",
         "challenger": "Arius and the Arian party - brothers contesting the very confession of the Word",
         "sources": S("srcALX017", "srcALX003", "srcALX029")}],
      concedes="The contemplative-ascent mechanism is Origen-concentrated (Dominant Modern Reconstruction, Doc_04 SS3.2); the practice-cluster that makes this a Primary is the URBAN contemplative-ascetic-prayer set only - the intensified desert versions are excluded (Discipline Two). And the world's own picture of completed formation at its outer edge - the martyr's witness - reaches us as the community's belief about what the martyr underwent, not first-person access: the martyr's interior is held at Inferential-Thin and deliberately not narrated from inside (Reported-Experience Status, alexlex033). The majority's interior formation is likewise registered by observable channels only (OG-4).",
      pressure_response="Says the difference plainly, in its own terms: the ascent the community knows runs through a Word who came down - through flesh and sacrament and shared life, not the soul climbing alone (Doc_08 2A-2 L2). And when the contest came from within, held the settlement as relief and burden at once - the Word confessed of one substance, the freedom to explore now bounded (Doc_08 2A-4 L2) - rather than as triumph.",
      divergence_partners=[
        {"world_id": "desert-monasticism",
         "partner_claim_id": "desertclaim001",
         "note": "The axis their own claim record already maps from its side: withdrawal itself as the formation - departure, solitude, and interior combat as the curriculum - vs. this world's transformation located in the city, the school, and the catechumenate. Formation without departure vs. departure as formation; documented on both sides of the live store."},
        {"world_id": "syriac-edessa-nisibis",
         "note": "Their Doc_04 Primary C2 is the Covenanted Ascetic Life: transformation lived as covenant-standing within the town congregation - ascetics who stay, inside the assembly, not a contemplative-ascent curriculum nor a departure."},
        {"world_id": "hieronymian-ascetic-literary",
         "note": "Their Doc_04 Primaries locate formation in ascetic self-impoverishment (G2) conducted within patronage-as-authority networks (G3): renunciation inside elite literary society - transformation enacted socially and materially, not as the soul's staged ascent."},
        {"world_id": "post-apostolic-house-church",
         "note": "Their Doc_04 Primary G07 is liturgical practice (Eucharist): formation through the shared meal and the network of congregations - a communal-practice register with no soul-ascent vocabulary in their gravity set."},
        {"world_id": "imperial-juridical-christianity",
         "note": "Their Doc_04 Primaries are juridical primacy and the church-state alliance: a formation ecology built on civic and imperial order, where right standing and enforced orthodoxy - not the transformed soul - are the organizing register."}]),
 dict(id="alexclaim003",
      sources=S("srcALX003", "srcALX029", "srcALX017"),
      claim="We confess the Son as of one substance (homoousios) with the Father - the Nicene confession, held since 325 as settlement: relief and burden at once, the Word confessed of one substance and the freedom to explore now bounded. The confession is carried wherever Christ is named - the Christ confession asserts the consubstantiality, Son of God carries the ontological argument most directly, and the Incarnation's restorative claim rests on the consubstantiality of the one who enters flesh.",
      held_against=[
        {"challenge": "Arius taught the Son as the highest creature - 'there was when he was not' - and the challenge came not from outside but from within: brothers contesting the very confession of the Word, so that what had been held loosely now had to be held within a drawn line (Doc_08 2A-4).",
         "challenger": "Arius (c. 256-336) and the Arian party",
         "sources": S("srcALX017", "srcALX003")},
        {"challenge": "The governed Historical-scope + Meaning contest (Doc_06 SS2, alexlex081): what 'consubstantial' meant to the Nicene bishops in 325 versus its later post-Nicene reception - how precisely the term was fixed at 325, and how far its later, fuller sense may be read back into the bishops' intent. It bears directly on how Athanasius's usage is read.",
         "challenger": "the term's own reception history, read by modern patristics against its moment",
         "sources": S("srcALX029", "srcALX017")}],
      concedes="What the word carried in its own moment is not simply what it came to carry: the pre-Nicene and post-Nicene registers must be kept distinct, because before 325 the Son's precise ontological status was genuinely open and argued - Origen's formulations of the Logos's relation to human nature were among the disputed questions Nicaea addressed. The settlement is held as settlement, not as a timeless given (the christology parkings, alexlex022/023/039, verbatim discipline).",
      pressure_response="Relief-and-burden, not triumph: the confession is held with its cost acknowledged - the freedom to explore now bounded - and the two registers are kept distinct rather than harmonized: pre-Nicene openness is narrated as open, the post-325 confession as settled, and the later sense is not read back into the bishops' intent (Doc_08 2A-4 L2; the alexlex081 contest as carried in all three surfacing parkings).",
      divergence_partners=[
        {"world_id": "imperial-juridical-christianity",
         "note": "Their Doc_04 Primary 3 is orthodoxy-enforcement through imperial power - the same Nicene instrument held as juridical mechanism, with the enforced content in the Homoian decades flagged DMR in their own cross-check. The confession as enforced boundary vs. the confession as relief-and-burden: same settlement, different possession."},
        {"world_id": "desert-monasticism",
         "note": "Their Doc_04's ten candidates include no doctrinal-confession gravity at all: the Nicene contest reaches their world through the bishop's authority and, later, as external conciliar action (their Doc_08's First-Origenist-Controversy force) - allegiance received, not ontology argued. The confession organizes this world's late horizon; it does not organize theirs."},
        {"world_id": "syriac-edessa-nisibis",
         "note": "Their Doc_04 Primary C1 is the symbolic/typological method: their christological register works in type and symbol, with boundary-drawing operating as heresiological self-definition (their Supporting C3) - not the ontological homoousios argument this world's late horizon turns on."},
        {"world_id": "post-apostolic-house-church",
         "note": "Their horizon closes before the Arian contest exists; boundary-drawing is present as their Tensional G05 (against rival movements), but the intra-communal ontological question was not yet drawn - the Son's status genuinely open in exactly the sense this world's own pre-Nicene register preserves."},
        {"world_id": "hieronymian-ascetic-literary",
         "note": "Their Doc_04 G6 (controversy/doctrinal dispute) is Supporting, operating as pressure on textual and patronage authority (the Origenist rupture, the Augustine dispute) - doctrinal contest as an instrument within literary authority-relations, not the confession-boundary that reorganizes the whole ecology's late horizon."}]),
 dict(id="alexclaim004",
      sources=S("srcALX009", "srcALX021", "srcALX001", "srcALX002"),
      claim="Our teaching descends in a remembered line - Pantaenus, Clement, Origen, on to Didymus - teacher to student across generations, the school alongside the church. The teacher's authority is grounded in demonstrated wisdom and enacted as accompaniment: trusted because others saw that he saw, the interpretive tradition passing only through the relationship that opens the student's own seeing (Doc_08 2B-3 Mechanism One).",
      held_against=[
        {"challenge": "The governed Historical-scope contest (Doc_06 SS2, alexlex059): whether the Alexandrian didaskaleion was a formal institution with a continuous teaching succession, or a looser teaching tradition retrospectively formalized by Eusebius. Van den Broek (1995) and van den Hoek (1997) deny a formal institution before Origen; Scholten (1995) affirms an institution but as a theological school rather than a catechumen-training school (Doc_01 SS1.2).",
         "challenger": "modern historical scholarship on the school's institutional status (van den Broek; van den Hoek; Scholten)",
         "sources": S("srcALX009", "srcALX021")},
        {"challenge": "The succession's main source is Eusebius - a single narrator writing generations later, carrying HIGH Author-Gravity risk: the succession particulars are his narrative frame, and the record has no independent second witness to the institutional continuity he presents.",
         "challenger": "the record's own single-narrator dependence (Eusebius, HIGH Author-Gravity)",
         "sources": S("srcALX009")}],
      concedes="Whether a formal institution with continuous succession existed before Origen, our own record cannot establish. What is well-attested is the KIND of authority the teacher held - grounded in demonstrated wisdom and enacted as accompaniment - and that authority does not depend on the institutional question being resolved (alexlex029's parked contest, carried verbatim). The succession particulars remain Eusebius-mediated throughout.",
      pressure_response="Does not assert a settled, orderly institution behind the teacher. Answers from the attested kind of authority - the demonstrated-wisdom, accompaniment-enacted kind - and holds the institutional question open rather than resolving it; the Teacher-Bishop tension is likewise held as a real tension, not dissolved (alexlex029; Doc_04 T1, Eusebius screen applied: structural coexistence carries the weight, the Origen-Demetrius episode stays illustration).",
      divergence_partners=[
        {"world_id": "desert-monasticism",
         "partner_claim_id": "desertclaim003",
         "note": "Their own claim record: spiritual authority (abba, amma) earned through recognized discernment and transmitted through direct personal relationship, not conferred by office. Kindred in the person-borne mechanism, divergent in the claim: their record asserts NO school and no succession-memory - person-to-person authority against this world's remembered institutional line, and their tradition never formalized a didaskaleion for scholarship to contest."},
        {"world_id": "post-apostolic-house-church",
         "note": "Their Doc_04 G01 (authority consolidation toward the monepiscopal office) is Supporting and flagged Contested in their own cross-check - the contested authority story of their world is the office's emergence, not a teaching succession; no teacher-school line exists in their gravity set."},
        {"world_id": "imperial-juridical-christianity",
         "note": "Their Doc_04 Primary 1 is juridical primacy-claiming: authority as jurisdiction - office, precedent, and enforceable claim - a register in which demonstrated-wisdom authority of this world's teacher kind is not an organizing force."},
        {"world_id": "hieronymian-ascetic-literary",
         "note": "Their Doc_04 Primary G3 is patronage-as-authority: standing built through patronage networks and literary reputation - a third kind of authority against both this world's teacher and its bishop, with no school succession."},
        {"world_id": "syriac-edessa-nisibis",
         "note": "Their Doc_04 Tensional C4 is authority-structure ambiguity - their own unresolved authority shape, held as a tension as this world holds Teacher-Bishop; but no didaskaleion-succession claim exists on their side to contest."}]),
 dict(id="alexclaim005",
      sources=S("srcALX002", "srcALX015", "srcALX012"),
      claim="We hold Origen's speculative teaching - the nous as what the soul originally was, the descent, the hoped-for restoration - as exploration offered under the Rule of Faith, not as settled dogma: inheritance and unease held together within the horizon (Doc_04 T3 - a world-level feature of the ecology). The teacher whose seeing the school most prized is carried forward and loved and, in part, set outside the line (Doc_08 3B-3 L2). What is not at issue is the broadly-attested account of the nous as the soul's contemplative faculty.",
      held_against=[
        {"challenge": "The condemnations: specific propositions - pre-existence, apokatastasis, grades of rational natures - were condemned at the Second Council of Constantinople (543/553; the precise conciliar status is itself debated), the terminus of the Origenist controversies whose first eruption falls at this world's own late edge (399-400 - Doc_04 T3's late-horizon evidence; Doc_08 3B-3: the Origen inheritance transmitted under contest).",
         "challenger": "the anti-Origenist reaction and the post-horizon conciliar condemnation",
         "sources": S("srcALX002", "srcALX012")},
        {"challenge": "The governed Meaning contest (Doc_06 SS2: Nous alexlex011, Apokatastasis alexlex051, Logikos alexlex090, Fall/Descent alexlex074 - one linked contest): whether the condemned propositions accurately represent Origen's own position. Patristics specialists are genuinely divided - later distorting systematization vs. meaningful continuity - and the sole systematic source is Origen himself (maximal Author-Gravity).",
         "challenger": "the divided modern scholarship on the continuity question",
         "sources": S("srcALX002", "srcALX015")}],
      concedes="Whether Origen's own speculative stratum is the same theological position as what was condemned, we cannot say - the dispute is unresolved (alexlex011's parked contest, verbatim). And the unease was already real within our own horizon: the drawn homoousian line shows the freedom to explore already bounded before any council named him - 'the Alexandrian Fall account' cannot simply be stated as settled (Doc_06 SS2, Fall/Descent).",
      pressure_response="Distinguishes before defending: the nous as the soul's contemplative faculty is not contested and is answered for plainly; the restorative conviction is held separable from the universalist extension - Athanasius is the standing demonstration that a full restoration theology does not require it (Doc_06 SS2's Restoration resolution); and the speculative stratum is presented as what it was - exploration offered, its continuity with the condemned propositions left unresolved because the record leaves it unresolved.",
      divergence_partners=[
        {"world_id": "desert-monasticism",
         "note": "Documented on both sides: this world transmits the Origen inheritance toward the desert as its most direct formation heir (Doc_08 3B-3), and their own record carries the First Origenist Controversy as an ending-external force (their Doc_08 3A-i: Theophilus's 399 Festal Letter, the 400 synod, the Tall Brothers' expulsion) with Evagrius's post-553 pseudonymous survival as the downstream sequel (their 3B-ii). The same inheritance, held differently: there it ended a strand's intellectual leadership; here it is treasure-and-unease within the ecology's own self-understanding. No counterpart claim record exists on their side (their six claims do not include an Origen-inheritance claim) - note-only mapping."},
        {"world_id": "hieronymian-ascetic-literary",
         "note": "Their Doc_04 G6 (controversy) names the Origenist rupture among its organizing disputes, and Jerome's later anti-Origenist position is this store's own explicit caveat on his testimony (srcALX012's verification note). The same contested inheritance, held there as a weapon and a wound within literary authority-relations; held here as the school's own treasure-and-unease."},
        {"world_id": "imperial-juridical-christianity",
         "note": "Their Doc_04 Primary 3 (orthodoxy-enforcement through imperial power) names the instrument-class the Origen condemnations ultimately ran through - conciliar decision carried by imperial authority. The specific 543/553 application lies beyond both worlds' horizons and is flagged as such; the divergence documented on their side is the instrument itself as an organizing force, which this world's ecology never made its own."}]),
]

# ---- term-side links (FLAG-014 closed for Alexandria at authoring time) ----
TERM_LINKS = {
    "alexlex014": ["alexclaim001"],  # Scripture - the claim's own subject
    "alexlex016": ["alexclaim001"],  # Allegory - named in the claim text
    "alexlex035": ["alexclaim001"],  # Interpretation - named in the claim text
    "alexlex021": ["alexclaim002"],  # Transformation - the claim's own subject
    "alexlex010": ["alexclaim002"],  # Soul/Psyche - named in the claim text
    "alexlex008": ["alexclaim002"],  # Theosis - named as the endpoint distinction
    "alexlex022": ["alexclaim003"],  # Christ - routed surfacing carrier (081)
    "alexlex023": ["alexclaim003"],  # Son of God - routed surfacing carrier (081)
    "alexlex039": ["alexclaim003"],  # Incarnation - routed surfacing carrier (081)
    "alexlex029": ["alexclaim004"],  # Teacher - routed surfacing carrier (059)
    "alexlex003": ["alexclaim004"],  # Catechesis - Doc_06 SS3's named reference point (059)
    "alexlex011": ["alexclaim005"],  # Nous - the routed CT contest site
}

TERM_NOTE = ("\n\nS2.6-equivalent (2026-07-27): contested_claim_ids populated at "
             "claim-authoring time (the FLAG-014 sequencing gap closed for this "
             "world); see wrs/migrate/s62_alx_s26.py for the linking rationale.")

BODY = ("S6.2 S2.6-equivalent contested_claim record (2026-07-27). Claim text "
        "from the world's own record (chunk parkings carried verbatim where "
        "quoted; Doc_04 gravity language; Doc_08 Layer-2 texts); held_against "
        "traced to documented contests only (named rivals, the record's own "
        "limits, the Doc_06 SS2 governed contests); divergence_partners mapped "
        "against the five partner worlds' own Doc_04 classification summaries, "
        "re-read for this step. partner_claim_id set toward Desert where its "
        "live claim records carry the genuine counterpart (the schema's "
        "'once it exists' condition is met); the reverse enrichment stays at "
        "S6.3. See the script docstring for the full field discipline.")


def main():
    for c in CLAIMS:
        emit_record({**COMMON, **c}, BODY, OUT / "contested_claim" / f"{c['id']}.md")
    linked = 0
    for tid, claim_ids in TERM_LINKS.items():
        path = OUT / "term" / f"{tid}.md"
        rec, body = read_record(path)
        if rec.get("contested_claim_ids") == claim_ids:  # idempotent re-run
            linked += 1
            continue
        assert "contested_claim_ids" not in rec, f"{tid}: unexpected existing links"
        # insert after retrieval to keep frontmatter ordering stable-ish; yaml
        # dict order is emission order, append is fine
        rec["contested_claim_ids"] = claim_ids
        new_body = body if TERM_NOTE.strip() in body else body + TERM_NOTE
        assert new_body != body or rec.get("contested_claim_ids"), tid
        emit_record(rec, new_body, path)
        linked += 1
    print(f"wrote {len(CLAIMS)} contested_claim records; "
          f"term-side contested_claim_ids on {linked} terms")


if __name__ == "__main__":
    main()
