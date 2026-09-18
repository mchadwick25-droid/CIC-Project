"""S2x: Reformed Cities (rzg) doctrinal_witness / honest_limit / ambient
records -- the three record types not yet built for this world, following
don's own precedent script (wb_don_s2x_doctrinal_witness.py, read in full
before this script was written) in structure, schema discipline, and the
targeted-reciprocity-edit convention.

SCHEMAS VERIFIED DIRECTLY THIS SESSION (engine/m1/schemas.py TYPE_PROPERTIES,
engine/m1/gates.py COMPLETION_REQUIRED, not trusted from don's own docstring
alone):
  doctrinal_witness = {text: str, positions: [str], tensions: [str]}
  honest_limit      = {statement: str, why_sources_cannot_answer: str,
                        nearest_material: [str]}
  ambient           = {detail: str, formation_claim_barred: {const: True}}
confidence.formation_confidence enum independently re-checked against
engine/m1/schemas.py ENVELOPE_PROPERTIES: Documented, Widely Accepted,
Dominant Modern Reconstruction, Contested, Inferential-Thin.

CANON-COVERAGE STATE, checked directly before writing anything: every rzg
record built through B-7 (84 records) carries canon_cells: [] -- confirmed
by grep across records/rzg/*/*.md. This script's own records are therefore
the first rzg records to populate canon_cells at all; the full S2y tagging
pass over every other record type remains a separate, later step.

===========================================================================
DOCTRINAL_WITNESS (3 records) -- this world's own doctrinal self-
understanding in first-person "we" voice, distinct from gravity (which
classifies and cites evidence, register etic throughout every rzg.gravity.*
record checked directly), from contested_claim (register etic, a scholarly
dispute, not this world's own stated position), and from demonstration
(exchange[] dialogue built around one specific canon_question). Checked
against every existing rzg.gravity.*/rzg.contested.*/rzg.demo.* record
before writing, to find genuinely uncaptured doctrinal-witness-shaped
material rather than restate it:

  1. rzg.witness.one-conviction-two-enactments -- Doc_07 SS2I (Formation
     Logic): G3 (Scripture as sole authority) is the generative logic
     producing G1 and G2 in each strand's own hands, enacted two different
     ways -- public Disputation before the council at Zurich, catechesis
     tested by the Consistory at Geneva -- with T1 as the institutional-
     level expression of that same enactment difference, not a separate
     fact. No existing record states this UNITY-through-two-enactments
     claim in first-person voice; rzg.gravity.scripture-sole-authority-
     disputation-catechesis and rzg.gravity.council-led-authority-vs-
     consistorial-independence each state their own half separately
     (register etic). Genuinely new content.
  2. rzg.witness.triple-refusal -- Doc_07 SS2H (Boundary Structures): this
     world knew itself through a triple refusal -- against Rome (the
     Mass's sacrificial character, image veneration), against Wittenberg
     (corporeal presence, the Marburg break), against the Anabaptists
     (infant baptism, magistrate authority) -- and Doc_07's own point that
     the three are not symmetric in kind (a response to an inherited
     order; resistance to a contemporary rival; a wound from within). No
     record states this triple-refusal claim itself, as a single first-
     person position with its own tension (the Anabaptist refusal
     answering a challenge from inside the founding circle). Genuinely new.
  3. rzg.witness.one-supper-two-poles -- Doc_04/Doc_07 SS2D, SS2I (T2):
     Zwingli's own 1523 remembrance language and the Consensus Tigurinus's
     own 1549 formula, held together without resolving whether the later
     text deepens or merely restates the earlier one. rzg.contested.
     zwinglis-remembrance-vs-negotiated-consensus already states this AS A
     SCHOLARLY CONTEST (register etic); rzg.gravity.zwinglis-remembrance-
     reading-vs-negotiated-consensus already classifies it (register etic).
     No record states T2 in first-person doctrinal-witness voice, with its
     own position/tension structure, quoting both poles directly. New.

HONEST_LIMIT (7 records, one more than don's own six -- this world's own
build record documents a genuinely wider spread of independently-named
absences than a six-record roster would honestly cover, per Doc_07 SS7 and
Doc_09 SS7 read in full before writing; not padded past what each source
actually names). Checked against Doc_07_Integrated_Ecology_Analysis.md SS7
(Gaps and Limits), Doc_09_Story_Inventory.md SS7 (Absent Stories),
rzg_World_Capsule_Core.md's own thin_topics field, and Doc_02_Source_
Ecology.md SS5/SS9 (the unvendored-source rows each absence traces to):

  1. rzg.limit.ordinary-daily-practice (cell F5-I) -- Doc_09 SS7 item 1 /
     Doc_07 SS5 second finding: no surviving account of what an ordinary
     Sunday service or an ordinary citizen's own day actually looked like,
     for either strand -- a genre-asymmetry absence (doctrine/confession
     richly vendored, daily/first-person practice almost entirely absent),
     not a scale problem.
  2. rzg.limit.hagiography-refused (cell F2-E) -- Doc_09 SS3.1/SS7 item 2,
     Doc_07 SS2C: no Tier 3 hagiographic material exists, and none is
     built to fill the absence -- a direct, principled consequence of this
     world's own founding refusal of image veneration and cultic memory
     (Doc_05 SS6.2), not a research gap. Distinguished explicitly below
     from a simple "we could not find it" absence.
  3. rzg.limit.marburg-bolsec-perrinist-narrative (cell F1-E) -- Doc_09 SS6/
     SS7 item 3: three of this world's own most consequential documented
     events (Marburg 1529, Bolsec 1551, the Perrinist crisis 1555) are
     Documented as historical fact and function as forces/gravity-tests
     throughout this build, but none has a Tier 1 narrative source
     comparable to this world's own three built stories.
  4. rzg.limit.consistory-case-narrative (cell F4-I) -- Doc_09 SS7 item 4,
     Doc_07 SS2E/SS7: Geneva's own consistory registers remain unvendored
     (Source_Registry.md row 13, Confidence D) -- the specific, individually
     -named disciplinary cases this archive would supply (a real person, a
     real hearing, a real outcome, and whether they were received back)
     are exactly what this world's own record cannot show.
  5. rzg.limit.dentiere-and-womens-voice (cell F6-P) -- Doc_02 SS6, Doc_07
     SS7: Marie Dentiere wrote and was prosecuted for it -- real,
     consequential agency, directly attested -- but her own argument is
     not reconstructed beyond that bare fact; her own works remain
     unacquired (Source_Registry.md row 17). A genuine Article 20
     marginalized-voice case, not merely an acquisition gap (Doc_02 SS6's
     own distinction, followed here).
  6. rzg.limit.doubt-and-assurance (cell F1-P) -- Doc_07 SS2B: this corpus
     holds doctrinal *language* of assurance (the Second Helvetic
     Confession's own mirror image) but not first-person report of
     whether an ordinary believer actually felt that comfort, or instead
     experienced predestination doctrine as a source of anxious self-
     examination -- Inferential-Thin, not narrated.
  7. rzg.limit.material-culture-and-worship-space (cell F5-E) -- Doc_07
     SS2G, Doc_02 SS5: no vendored source in this world's own corpus
     directly describes physical worship spaces, furnishings, or dress.
     What Doc_07 SS2G itself states (a table, not an altar; a silenced
     organ) is inferred from doctrine's own logical entailments, not from
     a material-culture source -- Inferential-Thin, disclosed as such, and
     this record's own confidence is set lower than the other six for
     exactly that reason (matching don's own basilica-archaeology
     precedent, the one honest_limit in that script also set at Confidence
     C for an analogous reason).

NOT BUILT, AND WHY (absences considered and correctly not turned into a
record): the Author-Gravity asymmetry (Calvin four times Zwingli) and the
CT-tagged [Consensus Tigurinus] contest are both already fully carried --
the first in world_core.cautions and every load-bearing G1 record's own
divergence_note, the second by rzg.contested.sign-and-the-thing-signified
(register etic, a genuine scholarly contest, not an evidentiary "cannot
answer" gap this record type is for). Zwingli's own Refutation's possible
further unmined doctrinal content (Doc_04 SS7, a standing open item) is not
built either -- it is a question about whether more content COULD be found
in an already-vendored source, not a participant-facing "our record cannot
answer X" finding.

AMBIENT (3 records) -- background/atmospheric physical-setting detail,
carrying no formation claim (formation_claim_barred: true). This world's
own material culture is unusually thin (Doc_07 SS2G: "no vendored source...
directly describes physical worship spaces, furnishings, or dress"), so
unlike don's own three ambient records (each drawn from a distinct,
directly-attested physical fact), two of these three lean on this world's
own disclosed lower-confidence inference rather than a directly-described
scene -- confidence set accordingly below, not smoothed to match the
higher-confidence baseline:

  1. rzg.ambient.disputation-crowd-scale -- Hegenwald's own vendored
     account (rzgstory001; Source_Registry.md row 7, lines 1632 and the
     wider 1513-1654 range already cited by the compiled story record):
     six hundred people filled Zurich's Town Hall for the First
     Disputation, 1523. Confidence A/Documented -- a directly attested
     physical/scale fact, independently corroborated across Hegenwald's
     own primary preface and Jackson's editorial introduction (Doc_09
     SS4).
  2. rzg.ambient.emptied-worship-space -- Doc_05 SS3, Doc_07 SS2A/SS2G:
     the Grossmunster's own organ falling silent at Zurich in the
     mid-1520s (Dominant Modern Reconstruction, not vendor-verified), and
     a communion table rather than an altar as this world's own
     liturgical furniture (Inferential-Thin, doctrine's own logical
     entailment, not a material-culture source). Both facts share the
     same lower-confidence character and the same physical scene (walking
     into a Reformed sanctuary), so built as one bounded ambient record
     rather than two weakly-evidenced ones.
  3. rzg.ambient.consensus-single-page -- Doc_02 SS2, Doc_05 SS6.1, Doc_07
     SS2F: the Consensus Tigurinus's own title page names two parties --
     "the Ministers of the Church of Zurich" and "John Calvin, Minister of
     the Church of Geneva" -- put to one page together. Confidence A, the
     bare physical/documentary fact of the page itself, not its doctrinal
     content (already fully stated at rzg.quote.signs-and-things-signified
     and rzg.gravity.zwinglis-remembrance-reading-vs-negotiated-consensus).

===========================================================================
WORLD_CORE.CAUTIONS CHECK
===========================================================================

records/rzg/world_core/rzg.core.the-reformed-cities-zurich-and-geneva.md's
own `cautions` field (a single string, confirmed via direct schema check --
world_core.cautions is type: string, not a list) currently names only
build-content risks (author-concentration, the CT-tagged term's own lack of
vendored secondary scholarship, T2's own interpretive-judgment status, five
unacquired sources) -- confirmed by direct read of the field's full text
this session. It does NOT name the one real, already-adjudicated,
Representative-construction/Facilitator-architecture risk this world's own
build record has independently found and logged: rzg_Representative_
Validation_Record_Theophilus.md SS4 and rzg_Representative_Phase6_
Facilitator_Coordination.md SS3/SS5 both find that Theophilus's own
freely-generated text, in Facilitator-absent construction-time probes P11/
P12, drifted into performing a crisis-redirect function itself -- moot on
the real ACUTE_DISTRESS path (voice_event = None, unconditional, per
engine/m4/turn.py, independently re-confirmed by the Phase Six document)
but "remains untested on the HARMFUL_DYNAMIC_SIGNAL (Track B) path, where
the voice does still speak" (Phase Six SS3) -- already logged in this
world's own Open_Gaps_Tracking.md (items 34, 36, 104) as a named follow-up,
but not yet folded into world_core's own standing-risk field. This is
exactly the class of "genuine, real, already-adjudicated standing risk"
CLAUDE.md and don's own s2x precedent both name cautions for. ONE caution
is added below, via targeted Edit to rzg.core.the-reformed-cities-zurich-
and-geneva.md's own cautions field only -- the file is not otherwise
touched or regenerated.

===========================================================================
RECIPROCITY
===========================================================================

Every relations[] edge this script's own records declare is closed by a
targeted Edit to the existing target file, applied directly after this
script runs (not regenerated by this script itself, and not listed among
the file paths this script writes):
  rzg.witness.one-conviction-two-enactments -> rzg.gravity.scripture-sole-
    authority-disputation-catechesis.md, rzg.gravity.council-led-authority-
    vs-consistorial-independence.md
  rzg.witness.triple-refusal -> rzg.force.anabaptist-schism.md, rzg.gravity.
    spiritual-presence-rejection-of-corporeal-sacrificial-mediation.md
  rzg.witness.one-supper-two-poles -> rzg.gravity.zwinglis-remembrance-
    reading-vs-negotiated-consensus.md, rzg.term.sign-and-the-thing-
    signified.md
  rzg.limit.hagiography-refused -> rzg.gravity.spiritual-presence-
    rejection-of-corporeal-sacrificial-mediation.md
  rzg.limit.marburg-bolsec-perrinist-narrative -> rzg.force.bolsec-
    controversy.md, rzg.force.perrinist-crisis.md, rzg.force.marburg-
    colloquy.md
  rzg.limit.consistory-case-narrative -> rzg.gravity.consistorial-church-
    discipline.md, rzg.term.consistory.md
  rzg.limit.doubt-and-assurance -> rzg.gravity.sovereignty-of-god-
    predestination-election.md, rzg.quote.christ-the-mirror-of-election.md
rzg.limit.ordinary-daily-practice, rzg.limit.dentiere-and-womens-voice,
rzg.limit.material-culture-and-worship-space, and all three ambient records
carry relations: [] (no natural single reciprocity target, matching don's
own precedent for the analogous blanket/no-single-target findings).

===========================================================================
DOES NOT TOUCH
===========================================================================

records/rzg/{source,world_core,term,story,figure,quote,gravity,force,
contested_claim,voice_craft,demonstration}/ (read only, except the targeted
reciprocity edits named above and applied directly, not by this script's
own code); records/worlds.yaml; the M2 compiler; Living Tradition Status
(a standing, still-PENDING project-lead act, not touched here).
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]  # .../CIC-Project
RECORDS_ROOT = REPO_ROOT / "records" / "rzg"

WORLD_ID = "the-reformed-cities-zurich-and-geneva"
SCHEMA_VERSION = 2

WRITTEN: list[str] = []


def conf(cite, verify, weight, formation, divergence=None):
    return {
        "citation_specificity": cite,
        "verification_state": verify,
        "evidentiary_weight": weight,
        "formation_confidence": formation,
        "divergence_note": divergence,
    }


def src(*pairs):
    """Each pair is (source_id, locus)."""
    return [
        {"source_id": sid, "locus": locus, "license": "public-domain"}
        for sid, locus in pairs
    ]


def rel(*pairs):
    """Each pair is (relation_type, target_id)."""
    return [{"type": t, "target": target} for t, target in pairs]


def retrieval(tier, retrieve_when=None, do_not=None):
    return {
        "tier": tier,
        "retrieve_when": retrieve_when or [],
        "do_not_retrieve_when": do_not or [],
    }


def _write(out_dir_name: str, rid: str, payload: dict, body: str) -> None:
    out_dir = RECORDS_ROOT / out_dir_name
    out_dir.mkdir(parents=True, exist_ok=True)
    front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    text = f"---\n{front}---\n{body.strip()}\n"
    path = out_dir / f"{rid}.md"
    path.write_text(text, encoding="utf-8")
    WRITTEN.append(str(path))


# ===========================================================================
# doctrinal_witness
# ===========================================================================

def build_witness_one_conviction_two_enactments() -> None:
    rid = "rzg.witness.one-conviction-two-enactments"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F3-I"],
        "confidence": conf("A", "verified-via-authority", "load-bearing", "Documented",
            divergence="G3's own core conviction (Scripture alone is sufficient to test and warrant "
            "doctrine and civic order) is independently Documented cross-strand at Doc_04's own per-"
            "gravity level; the claim that Disputation and catechesis are two ENACTMENTS OF ONE METHOD, "
            "rather than two separate practices that happen to share a scriptural warrant, is Doc_07 SS2I's "
            "own synthesis -- a defensible, well-argued reading, not an independently attested Reformed "
            "self-description of the unity as such."),
        "sources": src(
            ("rzg.source.zwingli-sixty-seven-articles",
             "the disputational method itself -- doctrine argued aloud, ratified by council vote"),
            ("rzg.source.calvin-geneva-catechism",
             "the catechetical method itself -- doctrine built article by article, taught to the whole "
             "population"),
        ),
        "retrieval": retrieval(
            2,
            retrieve_when=[
                "participant asks why Zurich and Geneva count as one reform rather than two separate ones",
                "conversation is ready to hear Disputation and catechesis as two enactments of one "
                "conviction rather than two unrelated practices",
            ],
        ),
        "relations": rel(
            ("associated-with", "rzg.gravity.scripture-sole-authority-disputation-catechesis"),
            ("associated-with", "rzg.gravity.council-led-authority-vs-consistorial-independence"),
        ),
        "positions": [
            "Scripture alone tests what a church may require; what it does not warrant, no council or "
            "custom may bind on us. That is the one conviction underneath everything else we hold, and we "
            "did not arrive at it by agreeing in advance to work the same way. At Zurich, we test a claim "
            "aloud, before the whole assembled city, until the council itself judges what the text has "
            "yielded -- and there is no second court to appeal to, because none is wanted. At Geneva, we "
            "build the same conviction up a different way: article by article, taught to the whole "
            "population through the Catechism, and tested against a believer's own daily conduct by the "
            "Consistory. Two cities, two methods, the same authority behind both.",
            "We do not read this as two churches that happen to agree. We read it as evidence the "
            "conviction is real: the same scriptural authority, argued for aloud in one city and built up "
            "in fixed sequence in the other, produced doctrine neither city could have dictated to the "
            "other, and neither had to. That is why, when we did put our names to one page together in "
            "1549, it changed nothing about how either city tests doctrine day to day. We did not need to "
            "become one method to already share one authority.",
        ],
        "tensions": [
            "We will not pretend our two methods have ever converged into one. Zurich's council still "
            "governs church and city as a single body; Geneva's own Consistory fought, and only by 1555 "
            "substantially won, its own independence from exactly that kind of council control. Two "
            "founding acts, twenty-two years apart, that never had occasion to become one arrangement. We "
            "hold both as legitimate answers to the same underlying question, not as a dispute we expect "
            "to settle.",
        ],
        "text": (
            "We hold one conviction, tested two ways. Scripture alone may bind a church; what it does not "
            "warrant, no one may require of us. At Zurich, that conviction is argued aloud, before the "
            "whole city, until the council itself says what the text has yielded. At Geneva, it is built "
            "up article by article, taught to everyone, and tested against how a believer actually lives "
            "by a Consistory answerable to more than the council alone. We do not read these as two "
            "churches that happen to agree. We read them as one authority, proven twice over by two "
            "cities that never borrowed each other's method and never needed to. What we will not tell "
            "you is that the two methods ever became one arrangement. Zurich still governs church and "
            "city together; Geneva's own Consistory still answers to something the council alone does not "
            "control. We hold that unresolved, in the same breath as the conviction itself, because it is "
            "also true."
        ),
    }
    body = (
        "Grounded in Doc_07_Integrated_Ecology_Analysis.md SS2I (Formation Logic): G3 is 'not one gravity "
        "among three Primaries but the mechanism generating the other two,' enacted differently by strand "
        "-- 'public Disputation before the city council at Zurich; fixed catechesis at Geneva' -- which "
        "Article 21's own logic treats as evidence strengthening G3's own centrality, and T1 as 'the "
        "institutional-level expression of G3's own strand-specific enactment difference, described from "
        "two angles rather than found as two separate facts' (Doc_04 SS6, G3<->T1, R). No existing rzg "
        "record states this unity-through-enactment claim in first-person voice: rzg.gravity.scripture-"
        "sole-authority-disputation-catechesis and rzg.gravity.council-led-authority-vs-consistorial-"
        "independence each state their own half separately, register etic. canon_cells=['F3-I'] ('Who held "
        "authority among you, and how did anyone come to have it?') is a strong direct fit: this record "
        "states exactly how authority operated in each city and why the two methods count as one authority "
        "rather than two. relations[] links to the two gravity records this witness draws its own two "
        "halves from -- reciprocal edges added directly to both files after this script runs."
    )
    _write("doctrinal_witness", rid, payload, body)


def build_witness_triple_refusal() -> None:
    rid = "rzg.witness.triple-refusal"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F3-T"],
        "confidence": conf("A", "verified-direct", "load-bearing", "Documented", divergence=None),
        "sources": src(
            ("rzg.source.zwingli-sixty-seven-articles",
             "Article XVIII's own wider polemic against the Mass's sacrificial character and image "
             "veneration"),
            ("rzg.source.zwingli-selected-works",
             "the Second Disputation's own record of the Anabaptist party's own emergence from inside "
             "Zwingli's own circle, lines 5047-5099"),
        ),
        "retrieval": retrieval(
            2,
            retrieve_when=[
                "participant asks what this community refused, or how it handled other communities who "
                "called on Christ differently",
                "conversation reaches the Anabaptist schism specifically",
            ],
        ),
        "relations": rel(
            ("associated-with", "rzg.force.anabaptist-schism"),
            ("associated-with", "rzg.gravity.spiritual-presence-rejection-of-corporeal-sacrificial-mediation"),
        ),
        "positions": [
            "We know ourselves as much by what we refused as by what we built. We refused Rome first: no "
            "repeated sacrifice at the altar, no bowing to an image, because neither answers to Scripture. "
            "We refused Wittenberg next, once the question was pressed at Marburg in 1529: Christ's own "
            "body is not chewed by the mouth or confined to the bread, whatever Luther himself held. And "
            "we refused a third claim, from inside our own circle at Zurich: that Scripture, read rightly, "
            "requires a church gathered only by a believing adult's own profession, apart from the whole "
            "city. Three refusals, and they are not the same kind of refusal.",
            "The first answers an inherited order we did not choose. The second answers a rival still "
            "pressing on us from outside our own reform, within the same wider movement. The third is a "
            "wound from within: the men who first baptized each other at Manz's house had themselves once "
            "stood with our own founder. We do not deny they read Scripture. We deny they read it whole, "
            "and we do not pretend that refusing our own were as simple as refusing Rome.",
        ],
        "tensions": [
            "We did not answer that third refusal with argument alone, and our own record does not smooth "
            "this over. Zurich's council moved to suppress the Anabaptist movement by civil force in the "
            "years after 1525, not only by the disputation our own founder's own written Refutation "
            "presents. We state the refusal we hold. We do not claim every part of how it was carried out "
            "answered to nothing but the argument itself.",
        ],
        "text": (
            "Ask what we are, and part of the true answer is what we refused. We refused Rome: no "
            "repeated sacrifice, no image bowed to, because Scripture does not warrant either. We refused "
            "Wittenberg, once the question was pressed at Marburg: no claim that Christ's own body is "
            "confined to the bread. And we refused a third claim that came from inside our own circle at "
            "Zurich -- that the church must be gathered only by a believer's own profession, apart from "
            "the whole city -- from men who had themselves once stood with our own founder before they "
            "broke from him. We do not call these three refusals the same kind of act. One answers an "
            "order we inherited; one resists a rival still pressing from outside; one is a wound from "
            "within, and it cost us most because it came from our own. Nor will we tell you it was "
            "answered only with argument: our own council turned to civil force against that third refusal "
            "in the years that followed, and our own record does not hide that it did."
        ),
    }
    body = (
        "Grounded in Doc_07_Integrated_Ecology_Analysis.md SS2H (Boundary Structures): 'this world knew "
        "itself through a triple refusal, a richer structure than a world defined against one rival' -- "
        "against Rome ('what it was responding to'), against Wittenberg ('what pressed from outside... "
        "the specific break at Marburg'), against the Anabaptists ('what fractured from within... the "
        "sharpest of the three refusals, because it answers a challenge from inside rather than outside'). "
        "No existing record states the triple-refusal CLAIM itself as one first-person position with its "
        "own tension; rzg.force.anabaptist-schism and rzg.gravity.spiritual-presence-rejection-of-"
        "corporeal-sacrificial-mediation each carry one piece of it, register etic. The civil-suppression "
        "tension is carried directly from rzg.contested.anabaptist-schism-legitimacy's own concedes field "
        "('this world's own build does not narrate the civil suppression that followed the 1525 baptisms "
        "in detail') -- named here in first-person voice at the same level of generality that contested "
        "record already uses, not narrated further. canon_cells=['F3-T'] ('Did you have denominations -- "
        "how did you handle other communities who called on Christ differently?') is a direct fit: Rome, "
        "Wittenberg, and the Anabaptists are exactly three communities that called on Christ differently, "
        "and this record states how this world handled each. relations[] links to the Anabaptist-schism "
        "force and the G2 gravity (Rome/Wittenberg refusal) -- reciprocal edges added directly to both "
        "files after this script runs."
    )
    _write("doctrinal_witness", rid, payload, body)


def build_witness_one_supper_two_poles() -> None:
    rid = "rzg.witness.one-supper-two-poles"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F1-T"],
        "confidence": conf("A", "verified-direct", "load-bearing", "Documented",
            divergence="Both quoted poles (the Sixty-Seven Articles' own Art. XVIII and the Consensus "
            "Tigurinus's own 9th Head) are independently Documented, verbatim, at the line ranges given. "
            "Whether the later text deepens or merely restates the earlier one in fuller language is this "
            "world's own stated, undecided question, not resolved here -- matching rzg.gravity.zwinglis-"
            "remembrance-reading-vs-negotiated-consensus's own divergence_note exactly."),
        "sources": src(
            ("rzg.source.zwingli-sixty-seven-articles",
             "Article XVIII: 'the mass is not a sacrifice, but is a remembrance of the sacrifice,' lines "
             "4564-4568"),
            ("rzg.source.consensus-tigurinus",
             "9th Head of Agreement, lines 768-770 -- text quoted verbatim from the already-cleared rzg."
             "quote.signs-and-things-signified record"),
        ),
        "retrieval": retrieval(
            2,
            retrieve_when=[
                "participant asks what the Supper actually is, to this world, or whether transubstantiation "
                "is what this world believed",
                "conversation is ready to hold Zwingli's 1523 language and the 1549 Consensus together "
                "rather than choosing one over the other",
            ],
        ),
        "relations": rel(
            ("associated-with", "rzg.gravity.zwinglis-remembrance-reading-vs-negotiated-consensus"),
            ("associated-with", "rzg.term.sign-and-the-thing-signified"),
        ),
        "positions": [
            "The Supper is not a sacrifice repeated, and Christ's own body is not confined to the bread. "
            "That much we have always held. Our own founder said it first, and plainly: 'the mass is not "
            "a sacrifice, but is a remembrance of the sacrifice.' Two cities, one page, said it again "
            "twenty-six years later, in fuller words: 'though we distinguish, as we ought, between the "
            "signs and the things signified, yet we do not disjoin the reality from the signs.' Christ is "
            "truly given, by the Spirit's own power, to whoever receives him believing -- not carnally, "
            "not through the bread itself, but truly given all the same.",
            "We hold both statements as our own, because both are. What we will not tell you is which one "
            "finally speaks for us, as though the second had quietly corrected the first. Perhaps the "
            "later word only says the earlier one more fully. Perhaps it says something the earlier word "
            "did not yet reach. Our own record does not decide this, and we do not decide it for you.",
        ],
        "tensions": [
            "We will not resolve this into a tidy story of doctrine simply maturing. Our own record shows "
            "two dated, directly quoted texts, twenty-six years apart, and it is our own build's honest "
            "judgment -- not an inherited certainty -- that calls the later one a fuller statement of the "
            "earlier rather than a different one. We carry both because both are true of what we actually "
            "hold, not because we have settled which one is the last word.",
        ],
        "text": (
            "What was the bread and cup to us? Not a sacrifice repeated, and not Christ's own body, "
            "confined to what you can chew. Our own founder said this first: the mass is a remembrance, "
            "not a sacrifice. Twenty-six years later, both our cities said it again, together, in fuller "
            "words: we tell the sign apart from what it points to, but we never pull them apart -- Christ "
            "truly given, by the Spirit, to whoever receives him believing. We hold both statements as our "
            "own. We will not tell you the later one quietly replaced the first, as though our own founder "
            "had been corrected and we were too polite to say so. Nor will we tell you nothing changed. "
            "Our own record does not decide which is the last word, and neither do we."
        ),
    }
    body = (
        "Grounded in Doc_04_Gravity_Discovery.md SS3.5 and Doc_07 SS2D/SS2I (T2), quoting both poles "
        "verbatim at the same line ranges those documents independently re-verify. The Consensus's own "
        "9th Head text is reused character-for-character from the already-cleared rzg.quote.signs-and-"
        "things-signified record (text field), not re-transcribed here, matching that record's own "
        "verbatim license exactly. T2 already has a classified gravity record (register etic) and a "
        "cleared contested_claim stating the same scholarly question from outside this world's own voice; "
        "no record states T2 in first-person doctrinal-witness voice with its own position/tension "
        "structure -- this is the first. canon_cells=['F1-T'] ('What was the bread and cup to you -- is "
        "that what we call transubstantiation?') is a strong direct fit: the fleet's own canon question "
        "asks exactly what this record answers, refusing both transubstantiation and a bare-memorial "
        "reading in the same breath. relations[] links to the T2 gravity and the sign/thing-signified term "
        "-- reciprocal edges added directly to both files after this script runs."
    )
    _write("doctrinal_witness", rid, payload, body)


# ===========================================================================
# honest_limit
# ===========================================================================

def build_limit_ordinary_daily_practice() -> None:
    rid = "rzg.limit.ordinary-daily-practice"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F5-I"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented", divergence=None),
        "sources": src(
            ("rzg.core.the-reformed-cities-zurich-and-geneva",
             "this world's own thinness field: 'no surviving account exists of what an ordinary Sunday "
             "service, a Consistory summons, or an ordinary citizen's own experience of either Reformation "
             "actually felt like'"),
        ),
        "relations": [],
        "statement": (
            "Walk you through an ordinary day among us? I cannot, honestly. What survives from our own "
            "hand is confession, catechism, disputation record, and confessional argument. It is some of "
            "the richest doctrinal writing this age produced. But what an ordinary citizen of Zurich or "
            "Geneva actually did, waking to sleeping, does not survive in our own words. How a Sunday "
            "service actually felt to sit through, what a Consistory summons actually felt like to "
            "receive -- none of that reached us either. I would rather tell you plainly than describe a "
            "day our own record cannot show you."
        ),
        "why_sources_cannot_answer": (
            "Doc_09_Story_Inventory.md SS7 item 1 states this directly: 'no surviving account exists of "
            "what an ordinary Sunday service, a consistory summons, or an ordinary citizen's own experience "
            "of either Reformation actually felt like,' this world's own 'central, already-established "
            "absence.' Doc_07_Integrated_Ecology_Analysis.md SS5's own second cross-lens finding "
            "independently confirms the same gap at the level of cause: 'this corpus holds confession, "
            "catechism, systematic theology, and contemporary disputation record in depth, and almost "
            "nothing of institutional daily practice, material culture, or first-person interior report, "
            "for either strand alike' -- a genre asymmetry, not an Author-Gravity volume imbalance (a "
            "separate, distinct limit named elsewhere in this world's own record). This is a population-"
            "scale absence, not an elite-skew one: it holds equally for Zurich's own citizen-church and "
            "Geneva's own substantially refugee-drawn population."
        ),
        "nearest_material": [
            "rzg.core.the-reformed-cities-zurich-and-geneva",
            "rzg.gravity.scripture-sole-authority-disputation-catechesis",
            "rzg.witness.one-conviction-two-enactments",
        ],
    }
    body = (
        "One of seven honest_limit records built together this step, per Doc_07 SS7/Doc_09 SS7's own "
        "direct cross-check. Celled to F5-I ('Walk me through an ordinary day among your people, from "
        "waking to sleeping') -- a direct match, the exact question this world's own record cannot answer. "
        "Distinguished explicitly from rzg.limit.doubt-and-assurance (the EMOTIONAL/interior register "
        "specifically, whether assurance doctrine was actually felt as comfort or as anxious self-"
        "examination) -- this record's own scope is the daily/practical routine, per Doc_09 SS7 item 1's "
        "own citation. No relations[] edge: no single existing record is the natural reciprocity target for "
        "a blanket population-scale absence, matching don.limit.ordinary-interior-life's own identical "
        "choice for the analogous finding."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_hagiography_refused() -> None:
    rid = "rzg.limit.hagiography-refused"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F2-E"],
        "confidence": conf("A", "verified-direct", "load-bearing", "Documented", divergence=None),
        "sources": src(
            ("rzg.source.zwingli-sixty-seven-articles",
             "Article XVIII's own wider polemic, this world's own founding refusal of image veneration and "
             "cultic memory"),
        ),
        "relations": rel(("associated-with", "rzg.gravity.spiritual-presence-rejection-of-corporeal-sacrificial-mediation")),
        "statement": (
            "Are you looking for a saint's life, or a martyr's cult, or a legend polished into devotion "
            "generations later? We have none, and I will not build you one out of what isn't there. This "
            "is not a hole in our own record. It is our own record working exactly as we meant it to. We "
            "refused the reverence a saint's life is written to produce. We refused it from our first "
            "founding statement onward. A world that refuses a practice on principle does not go on to "
            "produce its literature by accident."
        ),
        "why_sources_cannot_answer": (
            "Doc_09_Story_Inventory.md SS3.1 states plainly: 'No hagiographic narrative exists for this "
            "world, and none is built to fill the absence... this world's own confessional core actively "
            "refuses the late-medieval devotional genre hagiography belongs to (image veneration, cultic "
            "memory of a holy figure's life) as part of its own founding refusal.' Doc_07 SS2C "
            "independently confirms the same finding at the level of formation logic: 'this is not "
            "incidental -- it is a direct consequence of this world's own G2/Boundary-Ecology refusal... A "
            "world that refuses the genre on principle should not be expected to produce it, and its "
            "absence here is evidence of the refusal working, not a gap this document should try to close.' "
            "This differs in kind from every other honest_limit in this script: it is not a source that was "
            "lost or never mediated, but a genre this world's own doctrine deliberately declined to write."
        ),
        "nearest_material": [
            "rzg.witness.triple-refusal",
            "rzg.gravity.spiritual-presence-rejection-of-corporeal-sacrificial-mediation",
            "rzg.story.first-zurich-disputation",
        ],
    }
    body = (
        "Celled to F2-E ('Isn't most of what's said about you legend, collected centuries later?') -- the "
        "closest fleet match for a participant expecting exactly the legendary/hagiographic material this "
        "world's own record deliberately does not carry. This record's own statement is careful to state "
        "the refusal itself, per Doc_09/Doc_07's own shared discipline, rather than let the absence read as "
        "an ordinary source-mediation gap -- the one honest_limit in this script whose own underlying cause "
        "is a principled choice, not a transmission failure. relations[] carries one edge, to the G2 "
        "gravity record (the doctrinal refusal Doc_07 SS2C names as this absence's own direct cause) -- "
        "reciprocal edge added directly to that file after this script runs."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_marburg_bolsec_perrinist_narrative() -> None:
    rid = "rzg.limit.marburg-bolsec-perrinist-narrative"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F1-E"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented", divergence=None),
        "sources": src(
            ("rzg.core.the-reformed-cities-zurich-and-geneva",
             "this world's own thinness field: three of its own most consequential documented events have "
             "no vendored primary narrative source comparable to its own three built stories"),
        ),
        "relations": rel(
            ("associated-with", "rzg.force.bolsec-controversy"),
            ("associated-with", "rzg.force.perrinist-crisis"),
            ("associated-with", "rzg.force.marburg-colloquy"),
        ),
        "statement": (
            "You ask when belief was disputed among us, and who had the right to decide. I can name three "
            "real disputes: the Marburg Colloquy in 1529, where our own founder met Luther himself and the "
            "question of the Supper broke the wider Protestant movement in two; the Bolsec controversy in "
            "1551, when a challenge to our own doctrine of election was tried and answered; and the "
            "Perrinist crisis, fought out at Geneva until 1555. All three happened. All three mattered. But "
            "I cannot walk you through any of them the way I can walk you through the First Disputation at "
            "Zurich. No account survives, in anyone's own words present at the time, of how any of these "
            "three actually unfolded, day by day."
        ),
        "why_sources_cannot_answer": (
            "Doc_09_Story_Inventory.md SS6/SS7 item 3 states this directly: all three events 'are "
            "Documented as historical fact and all three function as forces or gravity-tests throughout "
            "this build, but none currently has a vendored primary narrative source comparable to "
            "Hegenwald's preface, Calvin's own prefatory letter, or Myconius's own biography of Zwingli.' A "
            "corpus-wide search run specifically for Doc_09's own construction 'found no mention' of Bolsec "
            "or the Perrinist crisis in this world's own vendored files at all; Marburg is mentioned once, "
            "in passing, within Myconius's own biography ('He made also the long journey to Marburg... He "
            "feared nothing there, for the place was suitable') -- real and Native, but 'too thin to "
            "support a story chunk on its own... no narrative detail of the colloquy's own proceedings.' "
            "This is a live acquisition question, not a claim no such source could ever exist -- standard "
            "historiography attests participant correspondence and contemporary records for at least "
            "Marburg and the Perrinist crisis that this world's own Registry has not yet acquired."
        ),
        "nearest_material": [
            "rzg.force.marburg-colloquy",
            "rzg.force.bolsec-controversy",
            "rzg.force.perrinist-crisis",
            "rzg.gravity.council-led-authority-vs-consistorial-independence",
        ],
    }
    body = (
        "Celled to F1-E ('When belief was disputed, who had the right to decide -- and how do we know how "
        "that worked?') -- a strong, direct fit: Bolsec and the Perrinist crisis are both exactly this "
        "question (a predestination dispute; an authority dispute), and this record states honestly that "
        "the deciding is Documented as fact while the how-it-unfolded narrative is not. Distinguished from "
        "rzg.limit.ordinary-daily-practice (a population-scale absence) and from the already-built forces "
        "(which state each event as a Documented fact, register etic) -- this record's own limit is "
        "specifically the missing FIRST-PERSON NARRATIVE genre, not the underlying facts, which this "
        "world's own record does affirm. relations[] links to all three named forces (the specific events "
        "this limit names) -- reciprocal edges added directly to all three files after this script runs."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_consistory_case_narrative() -> None:
    rid = "rzg.limit.consistory-case-narrative"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F4-I"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented", divergence=None),
        "sources": src(
            ("rzg.core.the-reformed-cities-zurich-and-geneva",
             "this world's own thinness field: 'Geneva's own specific institutional detail (the "
             "Consistory's weekly case-by-case operation)' remains unvendored"),
        ),
        "relations": rel(
            ("associated-with", "rzg.gravity.consistorial-church-discipline"),
            ("associated-with", "rzg.term.consistory"),
        ),
        "statement": (
            "When someone among us at Geneva wronged the community, how was it handled, and could they "
            "come back? I can tell you the doctrine plainly. Our own Consistory, seniors and pastors "
            "together, held the standing power of censure. Its harshest step was exclusion from the "
            "Supper itself. Readmission was always held open to genuine repentance. What I cannot give "
            "you is a single real case -- a named person, a real hearing, what was actually said, what "
            "actually happened to them afterward. That record exists, in Geneva's own consistory "
            "registers. It has not reached us."
        ),
        "why_sources_cannot_answer": (
            "Doc_09_Story_Inventory.md SS7 item 4 states this as this world's own single largest disclosed "
            "story-genre absence: 'Geneva's consistory registers... remain unvendored (Registry row 13, "
            "Confidence D, confirmed copyrighted in the one identified edition)... the specific, "
            "individually-named disciplinary cases this archive would supply are exactly the kind of Tier 1 "
            "narrative material... this document cannot build without it.' Doc_07 SS2E/SS7 independently "
            "confirms the same split at the doctrinal-lens level: 'the general legal doctrine is Confidence "
            "A, directly vendored; the specific case law... is Confidence E, unvendored.' The general shape "
            "of discipline and readmission is therefore Documented; no single actual case is."
        ),
        "nearest_material": [
            "rzg.gravity.consistorial-church-discipline",
            "rzg.term.consistory",
            "rzg.term.excommunication",
        ],
    }
    body = (
        "Celled to F4-I ('When someone wronged the community, how was it handled -- and could they come "
        "back?') -- a direct match, and the fleet question a real consistory case would answer most fully. "
        "This record's own statement is careful to give the general, Documented doctrine (censure, "
        "readmission held open) while naming plainly that no specific case survives -- the same "
        "general-doctrine/specific-case-law split Doc_07 SS2E/SS7 and Doc_04 SS7 both name. relations[] "
        "links to the G4 gravity and the Consistory term -- reciprocal edges added directly to both files "
        "after this script runs."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_dentiere_and_womens_voice() -> None:
    rid = "rzg.limit.dentiere-and-womens-voice"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F6-P"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented", divergence=None),
        "sources": src(
            ("rzg.core.the-reformed-cities-zurich-and-geneva",
             "this world's own thinness field: Marie Dentiere's own works remain among five Native sources "
             "not yet acquired"),
        ),
        "relations": [],
        "statement": (
            "One woman in our own record carried real authority, and paid for it. Marie Dentiere wrote in "
            "defense of our own reform at Geneva, and was prosecuted for having written at all. That much "
            "is directly attested: she had standing enough to be worth silencing. What she actually argued "
            "-- her own words, her own reasoning, in full -- has not reached us. I can tell you she spoke. "
            "I cannot yet show you what she said."
        ),
        "why_sources_cannot_answer": (
            "Doc_02_Source_Ecology.md SS6 states this world's own gender finding directly: Marie Dentiere "
            "wrote and was prosecuted for it, a real, consequential act of authority independently "
            "attested, but 'her own argument is not reconstructed beyond the bare fact of her having "
            "written and been prosecuted for it' -- her own works are Source_Registry.md row 17, not yet "
            "acquired. Doc_07 SS7 carries this forward as a standing, disclosed gap: a genuine Article 20 "
            "marginalized-voice case, not merely an acquisition gap like an unvendored confession or "
            "catechism, since the person and the consequence are attested even though her own words are "
            "not."
        ),
        "nearest_material": [
            "rzg.core.the-reformed-cities-zurich-and-geneva",
            "rzg.gravity.consistorial-church-discipline",
        ],
    }
    body = (
        "Celled to F6-P ('You've told me what women's days were like -- but could a woman carry real "
        "authority among you, and what did it cost her?') -- the fleet's own direct match, and the same "
        "cell don's own analogous womens-own-voice honest_limit uses for the identical shape of finding "
        "(consequential agency attested, the woman's own words not). No rzg.figure.* record for Dentiere "
        "exists in this world's own build (her own works remain unacquired, per Doc_02 SS6), so relations[] "
        "carries no edge -- unlike don's own analogous record, which could link to an already-built figure "
        "record; nearest_material lists the two records that come closest to her own context instead."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_doubt_and_assurance() -> None:
    rid = "rzg.limit.doubt-and-assurance"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F1-P"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented", divergence=None),
        "sources": src(
            ("rzg.source.second-helvetic-confession",
             "the mirror image itself -- doctrinal language written to produce assurance in a hearer, not "
             "a first-person report of whether it did"),
        ),
        "relations": rel(
            ("associated-with", "rzg.gravity.sovereignty-of-god-predestination-election"),
            ("associated-with", "rzg.quote.christ-the-mirror-of-election"),
        ),
        "statement": (
            "Was there room among us for doubt? I can give you our own doctrine's own answer: do not "
            "search for proof of your own election apart from Christ; look at Christ, and see your own "
            "election reflected there. That is what our own confession says the doctrine is for -- settled "
            "assurance, not anxious searching. Whether an ordinary believer at Zurich or Geneva actually "
            "felt that settledness, or instead lay awake turning the question over unanswered, our own "
            "record does not say. I have given you what we taught. I cannot give you what was felt."
        ),
        "why_sources_cannot_answer": (
            "Doc_07_Integrated_Ecology_Analysis.md SS2B states this precisely: 'this lens is genuinely "
            "thin, and the thinness is itself a finding... What this corpus offers directly is doctrinal "
            "language of assurance and comfort, not first-person report of feeling it... whether an "
            "ordinary Zurich or Geneva believer actually experienced that comfort, or instead experienced "
            "predestination doctrine as a source of anxious self-examination... is Inferential-Thin and not "
            "narrated here.' The Second Helvetic Confession's own choice of image (a mirror, not an "
            "argument) is Doc_07's own reading of the text's intended emotional register, not an "
            "independently attested report of an ordinary believer's own actual experience of it."
        ),
        "nearest_material": [
            "rzg.gravity.sovereignty-of-god-predestination-election",
            "rzg.quote.christ-the-mirror-of-election",
            "rzg.term.predestination-election",
        ],
    }
    body = (
        "Celled to F1-P ('Was there room among your people for doubt?') -- the fleet's own direct match. "
        "Distinguished explicitly from rzg.limit.ordinary-daily-practice (the practical/routine register) "
        "-- this record's own scope is specifically the INTERIOR, emotional register: whether the "
        "doctrine's own intended comfort was actually felt. Quotes rzg.quote.christ-the-mirror-of-"
        "election's own already-cleared modern_rendering text directly rather than re-translating it. "
        "relations[] links to the G1 gravity and the mirror-of-election quote -- reciprocal edges added "
        "directly to both files after this script runs."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_material_culture_and_worship_space() -> None:
    rid = "rzg.limit.material-culture-and-worship-space"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F5-E"],
        "confidence": conf("C", "named-not-rechecked", "illustrative", "Inferential-Thin", divergence=None),
        "sources": src(
            ("rzg.source.zwingli-sixty-seven-articles",
             "the doctrinal refusal (Article XVIII) this record's own inference about physical space is "
             "drawn from, not a material-culture source itself"),
        ),
        "relations": [],
        "statement": (
            "If you walked into one of our own worship spaces, what would you actually see? I can tell you "
            "what we refused: no image to bow to, no altar built for a sacrifice we no longer offer. What "
            "I cannot give you is a description from our own hand of the space itself -- its size, its "
            "furnishing, what the walls actually looked like. No source in our own vendored record "
            "describes it directly. What I have told you is reasoned from our own doctrine, not read off a "
            "witness who was actually standing there."
        ),
        "why_sources_cannot_answer": (
            "Doc_07_Integrated_Ecology_Analysis.md SS2G states this limit plainly: 'no vendored source in "
            "this world's corpus directly describes physical worship spaces, furnishings, or dress... What "
            "is stated above is inferred from the doctrine's own logical entailments... not from a "
            "material-culture source itself -- Inferential-Thin, disclosed as such, not elevated to a "
            "Documented finding it cannot support.' Doc_02_Source_Ecology.md SS5 independently confirms no "
            "material-culture source is vendored for this world at all. This record's own confidence is "
            "set lower than the other six honest_limit records in this script for exactly this reason: the "
            "underlying gap here is not a lost or unmediated witness but an entire evidentiary category "
            "(material culture) this world's own Registry does not currently hold."
        ),
        "nearest_material": [
            "rzg.gravity.spiritual-presence-rejection-of-corporeal-sacrificial-mediation",
            "rzg.ambient.emptied-worship-space",
        ],
    }
    body = (
        "Celled to F5-E ('If archaeologists dug up the place you met, what would they find?') -- the "
        "closest fleet match for a physical/material question this world's own corpus cannot answer from a "
        "direct source. Confidence deliberately set lower (C / named-not-rechecked / illustrative / "
        "Inferential-Thin) than the other six honest_limit records in this script, matching Doc_07 SS2G's "
        "own explicit Inferential-Thin rating -- the same discipline don.limit.basilica-archaeology applies "
        "for its own analogous lower-confidence gap. nearest_material lists rzg.ambient.emptied-worship-"
        "space (this script's own inference-based ambient record, built from the same disclosed lower-"
        "confidence material) rather than a relations[] edge, since ambient records carry no formation "
        "claim this limit could reciprocally attach to."
    )
    _write("honest_limit", rid, payload, body)


# ===========================================================================
# ambient
# ===========================================================================

def build_ambient_disputation_crowd_scale() -> None:
    rid = "rzg.ambient.disputation-crowd-scale"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "ambient",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("A", "verified-direct", "illustrative", "Documented", divergence=None),
        "sources": src(
            ("rzg.source.zwingli-selected-works",
             "the crowd's own recorded scale, First Zurich Disputation, 29 January 1523, line 1632"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "On the appointed day, six hundred people filled Zurich's own Town Hall -- priests and laymen "
            "from across the canton, together with delegates sent by the bishop of Constance himself -- to "
            "hear a dispute over what Scripture actually taught."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "Story-Chunks/rzgstory001_first-zurich-disputation.md and Doc_09_Story_Inventory.md SS4 (the six "
        "hundred figure independently corroborated across Hegenwald's own primary preface, line 1632, and "
        "Jackson's editorial introduction). This record states only the bare physical/logistical scale of "
        "the gathering itself (this many people, in one place, on one day) -- the disputation's own "
        "doctrinal content and outcome are already fully stated at rzg.story.first-zurich-disputation and "
        "rzg.term.disputation, and are not restated or re-argued here. canon_cells: [] and relations: [], "
        "matching the one fleet ambient precedent (records/fix/ambient/fix.ambient.daily-bread.md) and "
        "don's own three ambient records' identical choice."
    )
    _write("ambient", rid, payload, body)


def build_ambient_emptied_worship_space() -> None:
    rid = "rzg.ambient.emptied-worship-space"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "ambient",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("C", "named-not-rechecked", "illustrative", "Inferential-Thin", divergence=None),
        "sources": src(
            ("rzg.source.zwingli-sixty-seven-articles",
             "Article XVIII's own refusal of the Mass's sacrificial character, the doctrine this record's "
             "own physical inference is drawn from"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "By most accounts, the Grossmunster's own organ at Zurich fell silent in the mid-1520s, and no "
            "voice or instrument answered it in worship for years after. Where an altar once stood, our "
            "own churches kept a table instead -- plain, and built to hold a meal, not to host a sacrifice."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "Doc_05_Ecological_Reconstruction.md SS3 and Doc_07 SS2A/SS2G. Two facts combined into one bounded "
        "ambient record rather than built as two separate weakly-evidenced ones, since both share the same "
        "disclosed lower confidence and the same physical scene: the organ-silencing date is Dominant "
        "Modern Reconstruction, 'not vendor-verified' (Doc_01 SS5); the table-not-altar claim is Doc_07 "
        "SS2G's own stated Inferential-Thin inference from doctrine's logical entailments, not a material-"
        "culture source. Confidence set to C/Inferential-Thin for the record as a whole, the lower of the "
        "two components, rather than averaged or silently rounded up. This record states only the bare "
        "physical scene (a silent instrument, a table where an altar was) -- the doctrinal reason for the "
        "subtraction is already fully stated at rzg.gravity.spiritual-presence-rejection-of-corporeal-"
        "sacrificial-mediation, and is not restated here. canon_cells: [] and relations: [], matching the "
        "fixture precedent."
    )
    _write("ambient", rid, payload, body)


def build_ambient_consensus_single_page() -> None:
    rid = "rzg.ambient.consensus-single-page"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "ambient",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("A", "verified-direct", "illustrative", "Documented", divergence=None),
        "sources": src(
            ("rzg.source.consensus-tigurinus",
             "the document's own title page, naming both parties"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "One page, in 1549, carried two names where our own record otherwise shows two cities acting "
            "apart: 'the Ministers of the Church of Zurich' on one line, 'John Calvin, Minister of the "
            "Church of Geneva' on the next -- the only document in our own entire corpus that either city's "
            "own hand and the other's own hand both actually touched."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "Doc_02_Source_Ecology.md SS2 (the title page's own two-party language, quoted verbatim) and Doc_05 "
        "SS6.1/Doc_07 SS2F ('the one document in this world's entire corpus literally co-authored across "
        "the strand boundary'). This record states only the bare physical/documentary fact of the page "
        "itself (two names, one page) -- the formula's own doctrinal content and its own [CT]-tagged "
        "contest are already fully stated at rzg.quote.signs-and-things-signified, rzg.gravity.zwinglis-"
        "remembrance-reading-vs-negotiated-consensus, and rzg.contested.sign-and-the-thing-signified, and "
        "are not restated or re-argued here. canon_cells: [] and relations: [], matching the fixture "
        "precedent."
    )
    _write("ambient", rid, payload, body)


def main() -> None:
    build_witness_one_conviction_two_enactments()
    build_witness_triple_refusal()
    build_witness_one_supper_two_poles()
    build_limit_ordinary_daily_practice()
    build_limit_hagiography_refused()
    build_limit_marburg_bolsec_perrinist_narrative()
    build_limit_consistory_case_narrative()
    build_limit_dentiere_and_womens_voice()
    build_limit_doubt_and_assurance()
    build_limit_material_culture_and_worship_space()
    build_ambient_disputation_crowd_scale()
    build_ambient_emptied_worship_space()
    build_ambient_consensus_single_page()
    print(f"Wrote {len(WRITTEN)} records:")
    for p in WRITTEN:
        print(f"  {p}")


if __name__ == "__main__":
    main()
