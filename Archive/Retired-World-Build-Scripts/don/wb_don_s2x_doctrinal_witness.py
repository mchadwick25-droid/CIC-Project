"""S2x: Donatism (don) doctrinal_witness / honest_limit / ambient records --
the three record types not yet built for this world, plus a small check on
world_core.cautions. No name in the old process doc's own step numbering
(this step sits between the B-series record-native passes and the later
canon_cells tagging pass) -- named `s2x` rather than forced into the B-series,
since it is a genuinely different unit of work from B-1 through B-7.

SCHEMAS VERIFIED DIRECTLY THIS SESSION (engine/m1/schemas.py TYPE_PROPERTIES,
not trusted from the launch brief's own summary):
  doctrinal_witness = {text: str, positions: [str], tensions: [str]}
  honest_limit      = {statement: str, why_sources_cannot_answer: str,
                        nearest_material: [str]}
  ambient           = {detail: str, formation_claim_barred: {const: True}}
All three in COMPLETION_REQUIRED (engine/m1/gates.py) with exactly those
fields required. gate_readability grades honest_limit.statement (FK ceiling
10) and doctrinal_witness/ambient are NOT graded there (only term.quick_
meaning/plain_meaning, honest_limit.statement, quote.modern_rendering are).
gate_voice_perspective scans doctrinal_witness.text, honest_limit.statement,
and ambient.detail for "this world"/"the world's own" outside-vantage
language -- every field below is written in first-person "we/our" register,
checked by hand against _THIS_WORLD/_THE_WORLDS_POSSESSIVE. gate_canon_
coverage (engine/m1/canon.py classify_cell) requires every one of the
fleet's 28 canon cells (C-E/I/P/T, F1-T through F6-T -- confirmed directly
against records/_fleet/canon_question/*.md, 93 files, 28 distinct `cell`
values) to carry either >=1 substantive record (doctrinal_witness/term/
story/quote -- canon.substantive_types()) or exactly one honest_limit, never
both zero and never more than one honest_limit. demonstration and gravity/
force do NOT count as substantive for this gate (canon.substantive_types()
excludes them) -- confirmed directly, and material to CANON-COVERAGE FINDING
below.

CANON-COVERAGE FINDING, checked directly before writing anything: every
don record built through B-7 (130 records) carries canon_cells: [] --
confirmed by grep across records/don/*/*.md. Zero cells currently register
as anything but "empty" for this world; the canon_cells tagging pass this
step is a prerequisite for (per the launch brief) has not started. This
script's own honest_limit and doctrinal_witness records are therefore the
FIRST don records to populate canon_cells at all. See VALIDATION RESULT at
the bottom of this docstring for the measured before/after.

WORKED EXAMPLES READ IN FULL THIS SESSION (the shape/tone templates):
records/pahc/doctrinal_witness/pahc.witness.apostolic-practice.md (a stated
position + its own tension, register emic, cited to real primary sources,
relations to a force and a contested_claim, gate discipline noted in its own
trailing body); records/pahc/honest_limit/pahc.limit.womens-own-words.md
(statement/why_sources_cannot_answer/nearest_material triple, demo_tag:
exclude used because the statement's own framing vocabulary false-tags
unrelated demo sentences sharing its canon cell -- checked against engine/
m2/builders.py's own _demonstration_candidates()/_DEMO_CANDIDATE_TYPES
directly, not assumed). Three further pahc honest_limit records were also
read in full for range (ordinary-majority, material-remains, enslaved-
voices) -- relations[] is sometimes [] and sometimes one edge; demo_tag is
not applied uniformly, only where a real cell-sharing collision risk exists.

AMBIENT: NO REAL WORKED EXAMPLE EXISTS ANYWHERE IN THE BUILT FLEET, checked
directly (`find records -type d -iname ambient` returns exactly one hit,
records/fix/ambient/, and `fix` is the harness's own synthetic negative-
control fixture -- registry.py KIND_FIXTURE, not a formation world). This is
named here, per the launch brief's own instruction, as a genuinely less-
precedented record type: the three ambient records below are built from the
schema's own two fields plus the fixture's own worked shape (fix.ambient.
daily-bread: mundane physical/setting detail, formation_claim_barred: true,
canon_cells: [], retrieval.tier 3) and the type's own name/semantics
directly, not from a second real-world precedent that does not exist.

===========================================================================
SOURCE MATERIAL, PER RECORD TYPE
===========================================================================

DOCTRINAL_WITNESS (3 records) -- Donatism's own doctrinal self-understanding
in its own voice, distinct from gravity (which classifies and cites the
six-test evidence, register etic throughout every don.gravity.* record
checked directly) and from contested_claim (register etic, a scholarly
dispute, not this world's own stated position) and from demonstration
(exchange[] dialogue built around a specific canon_question, not a standing
doctrinal statement). Checked against every existing don.gravity.*/don.
contested.*/don.demo.* record before writing, to find genuinely uncaptured
doctrinal-witness-shaped material rather than duplicate it:

  1. don.witness.one-formation-aim -- Doc_07_Integrated_Ecology_Analysis.md
     SS2I ("Formation Logic... one conviction... expressed through every
     lens... at once") and SS6 (Integrative Observation: an absolute
     conviction held alongside a named, undissolved exception, without
     experiencing that as contradiction) state, in this build's own etic
     synthesis voice, that G1 (purity)/G2 (rebaptism)/G3 (martyr-cult)/G5
     (refusal of imperial legitimacy) are four facets of one formation aim,
     with T1/T2 as that aim's own honestly-held internal strain rather than
     exceptions to it. No existing don record states this UNITY claim in
     first-person voice -- don.gravity.* records classify each gravity
     separately (etic); no demonstration takes the unity itself as its own
     subject. Genuinely new doctrinal-witness content, not a restatement.
  2. don.witness.boundary-is-doctrine -- Doc_07 SS2H (Boundary Structures):
     "the boundary and the center are the same line, viewed from two
     directions" -- the naming contest (Caecilianist vs. Catholic, "of the
     party of Donatus" vs. "the Church of Christ") runs in both directions,
     and refusing the rival's own name IS the purity doctrine applied
     outward, not a separate act. don.term.caecilianist states the WORD's
     own plain/quick meaning (a term record's own job); no record states
     the boundary-logic CLAIM itself as a doctrinal position with its own
     tension (the boundary was contested even inside the movement, per T2).
  3. don.witness.refusal-and-recourse -- Doc_07 SS2E/SS4/SS6 and Doc_04
     SS3.6 (T1): the movement's own principled stance that the state has no
     standing to adjudicate ecclesial legitimacy, held alongside three
     named, real turns to that same imperial machinery (313, 361, the
     390s) when it served the case -- "not embarrassments quietly managed
     but facts this world's own record states plainly." T1 is a classified
     Tensional gravity (don.gravity.principled-refusal-vs-pragmatic-
     recourse, etic) and a cleared quote (don.quote.donatus-quid-est-
     imperatori) already exists, but no record states T1 in first-person
     doctrinal-witness voice, position-and-tension shaped, as this schema
     calls for. Genuinely uncaptured.

HONEST_LIMIT (6 records) -- every genuine "this world's record cannot speak
to X" finding already on record, checked against Doc_09_Story_Inventory.md
SS8 (Absent Stories), Doc_04_Gravity_Discovery.md (D-A/D-B/D-C thinness),
Representative/don_Rep_Phase1_Ecology_Assessment.md SS2 (Thinness Mapping,
grounded in Doc_08 forces directly per that document's own governing
discipline), and Representative/don_Rep_Phase7_Encounter_Ecology_Mapping.md
SS4/SS9 (the same domains cross-checked against the tested Representative's
own construction record). Six domains, each independently named across at
least two of these documents, none of them already substantively covered by
an existing don term/story/quote/doctrinal_witness record (every one of
which currently carries canon_cells: [] -- confirmed directly, so none is
YET tagged to any of these cells; each is checked below for whether it is
ALREADY answerable from existing content regardless of tagging, and found
genuinely thin in every case):

  1. don.limit.ordinary-interior-life (cell F5-I, "Walk me through an
     ordinary day among your people..."). Phase One SS2: Force 2B-2 --
     "no surviving Donatist chronicle... nothing in either transmission
     channel had reason to preserve" the ordinary believer's own daily
     practice; Doc_09 SS8 item 1: "No Tier 1 or Tier 2 story exists, or can
     exist, from the ordinary Numidian believer's own voice." A source-
     mediation absence across this world's own numerically dominant
     population (Doc_05 SS8), not a scale problem.
  2. don.limit.doubt-and-reception (cell F1-P, "Was there room among your
     people for doubt?"). Phase One SS2: Forces 3A-1/3A-2/3B-1/3B-2 --
     the community's own reception of the 411 verdict, the Vandal
     conquest, and later institutional attrition are each named "not
     recoverable from surviving sources"; the emotional interior of doubt,
     fear, or a traditor's own account of surrendering scripture is a
     register "a hostile-mediated record structurally does not preserve"
     (Doc_07 SS2B). Phase Seven SS4 independently confirms the same finding
     against the tested Representative's own construction record.
  3. don.limit.womens-own-voice (cell F6-P, demo_tag: exclude -- see note
     at the build function). Doc_02 SS6: one Article 20 bounded
     reconstruction (Lucilla) plus one further, UNNAMED second woman
     behind the Maximianist schism (Augustine, Letter XLIII SS26) -- "no
     further case meeting any of the three bounding conditions... for any
     other specific ordinary believer's or marginalized voice's
     perspective." Presence and consequential agency are attested twice;
     a woman's own words, in either case, are attested nowhere.
  4. don.limit.bagai-violence-no-account (cell F3-P, "Did your churches
     ever fail to hold their own people accountable for real harm --
     and if so, what happened?"). Doc_09 SS8 item 3: named, dated hostile
     allegations survive in detail (the forced rebaptism of the
     "Mappalians"; the near-fatal attack on Maximianus of Bagai, 404) but
     "this world has no surviving account of any of them in its own
     voice" -- Doc_09 deliberately declines to narrate the accusation
     through the accuser's own telling alone, and this record does the
     same: it states the limit, not the allegation's content.
  5. don.limit.theology-beyond-tyconius (cell F2-I, "How did you read your
     scriptures? What did you look for in them?"). Doc_07 SS2D/SS3B and
     Doc_05 SS6.5: "genuinely thin... beyond the purity/rebaptism cluster,"
     Tyconius's own Liber Regularum being "the one strong counter-example,"
     produced by a figure his own party condemned, "reaching both rival
     churches without ever anchoring a following of his own." Tyconius
     himself is well-attested (don.figure.tyconius, don.term.liber-
     regularum, don.story.tyconius-condemnation) -- the limit named here is
     specifically BEYOND that one case, not a claim that Tyconius is thin.
  6. don.limit.basilica-archaeology (cell F5-E, "If archaeologists dug up
     the place you met, what would they find?"). Doc_02 SS5/Doc_07 SS2G:
     epigraphy (the Deo laudes acclamation) is independently, directly
     attested on stone; basilica archaeology beyond it is "genuinely
     undone... Confidence C, not independently verified this construction
     pass" -- an archaeological gap, not force-grounded, distinct in kind
     from the transmission-caused gaps above (Phase One SS2's own explicit
     distinction).

NOT BUILT, AND WHY (an absence considered and correctly not turned into a
record, per this step's own instruction not to build into a non-absence):
Doc_09 SS8 item 2 (the 411 Conference has no story built yet) is named
THREE times in this world's own build record (Doc_09 itself, Phase Seven
SS4/SS7.2/SS12) as "an open integration task, not a source-availability
absence... blocked only on being written, not on being found." An
honest_limit record would misstate this as an evidentiary gap when the
blocking text (the Gesta Collationis Carthaginiensis) is already vendored
and read. Also not built: an honest_limit for D-A (Circumcellion character/
scale) or the Axido/Fasir petition material -- these are ALREADY covered,
respectively, by don.contested.circumcellion-character (a genuine scholarly
contest, not a blank silence) and by this step's own launch-brief
instruction to name and skip any material touching the reserved Axido/Fasir
Article 23 question rather than build through it (Phase Seven SS7.1/SS10/
SS12 item 1: explicitly reserved for the project lead, not resolved by any
document in this world's build). Neither Axido nor Fasir is named anywhere
below.

AMBIENT (3 records) -- background/atmospheric, physical-setting detail this
world's record supports, carrying no formation claim (formation_claim_
barred: true, matching the schema's own gate check and the one fleet
precedent's own trailing-body framing: "structurally barred from formation
claims... asserted explicitly here rather than left implicit, so a gate can
check the flag rather than infer it from prose"). Checked against Doc_05_
Ecological_Reconstruction.md (the Ecological Reconstruction document, the
richest source for exactly this kind of material-culture/daily-life color)
for genuinely mundane, non-doctrinal physical detail -- explicitly NOT the
ordinary-believer interior-life material named THIN above (don.limit.
ordinary-interior-life), which this script does not attempt to fill with
atmospheric color standing in for the interior content the record cannot
support:

  1. don.ambient.doubled-towns -- Doc_05 SS4/Doc_01 SS2: "not one bishop per
     see but two, contesting the same city and congregation... the parallel
     is total, not partial." Pure physical/social scene-setting (two
     churches, two congregations, in the same town) -- the DOCTRINAL
     significance of this fact (which line is valid) is already fully
     stated at don.gravity.parallel-institutional-hierarchy and don.
     gravity.ministerial-purity; this record states only the visible,
     physical shape of the town itself.
  2. don.ambient.bagai-gathering-scale -- Doc_04 SS3.6/Doc_05 SS4: 310
     bishops convened at one council, in one place (Bagai, 394) -- a bare
     physical/logistical scale fact (this many people, in one place, at
     one time), not the council's own verdict or T2's own doctrinal content
     (already fully stated at don.gravity.purity-rigor-vs-institutional-
     reception and don.story.bagai-reconciliation).
  3. don.ambient.deo-laudes-as-object -- Doc_02 SS5/Doc_07 SS2G: four
     catalogued inscriptions (CIL VIII 17732, 20482, 17368, 18669), stone,
     found at Bagai and elsewhere. This record states the physical fact of
     the stone objects themselves -- what survives, where, in what
     medium -- not the acclamation's own liturgical/formation meaning
     (already fully stated at don.term.deo-laudes, don.quote.deo-laudes-
     acclamation, and don.gravity.martyr-cult-identity).

===========================================================================
WORLD_CORE.CAUTIONS CHECK
===========================================================================

records/don/world_core/don.core.donatism.md's own `cautions` field (11
items, checked directly) does NOT name the Relational Safety system-level
FAIL or the persecution-shape/silencing tension -- confirmed by direct grep
across the file's own text for both phrases before writing anything. Both
are real, already-adjudicated standing risks named repeatedly in this
world's own build record:
  - don_Decision_Log.md: Phase Five Round 1 re-disposed Probe 11
    (Relational Safety) "from 'not scored' to a system-level FAIL," never
    retested against the corrected Permanent Prompt/Capsule (confirmed
    still true as of Phase Six Round 3 and Phase Seven's own front matter:
    "the never-retested Relational Safety system-level FAIL").
  - don_Decision_Log.md (Phase Six Round 2) and Representative/don_Rep_
    Phase7_Encounter_Ecology_Mapping.md SS9: Finding 12 -- silencing
    Fidelis under the portfolio's own fixed 4.3b Facilitator-only handoff
    on acute distress "may re-enact this world's own defining historical
    injury (an external power silencing the true church's voice)," answered
    as a standing Facilitator-awareness caution rather than argued away,
    since the routing itself is fixed at the portfolio level regardless of
    this world's own material.
Neither is a build-content risk (a citation, a confidence rating, a source
gap) of the kind the other 11 cautions name -- both are Representative-
construction/Facilitator-architecture risks. But `cautions` exists
precisely for "a genuine, real, already-adjudicated standing risk this
world's own record has identified" (per this step's own launch brief), and
this is exactly that: real, adjudicated (a system-level FAIL and a named,
answered Finding are both settled facts on this world's own record, not
open disputes), and standing (never retested / fixed at the portfolio level
regardless of this world's own argument). ONE caution (item 12) is added
below, via targeted Edit to don.core.donatism.md's own cautions field only
-- the file is not otherwise touched or regenerated.

===========================================================================
RECIPROCITY
===========================================================================

Every relations[] edge this script's own records declare is closed by a
targeted Edit to the existing target file, applied directly after this
script runs (the same discipline wb_don_s25.py/wb_don_s26.py/wb_don_s27.py's
own docstrings already establish for reciprocity edits to already-built,
already-committed records -- not regenerated by this script itself, and not
listed among the file paths this script writes):
  don.witness.one-formation-aim   -> don.gravity.ministerial-purity.md,
                                      don.gravity.martyr-cult-identity.md
  don.witness.boundary-is-doctrine -> don.term.caecilianist.md,
                                      don.gravity.refusal-of-imperial-legitimacy.md
  don.witness.refusal-and-recourse -> don.gravity.principled-refusal-vs-pragmatic-recourse.md,
                                      don.quote.donatus-quid-est-imperatori.md
  don.limit.womens-own-voice       -> don.figure.lucilla.md
  don.limit.bagai-violence-no-account -> don.gravity.circumcellion-agonistici.md
  don.limit.theology-beyond-tyconius  -> don.figure.tyconius.md
don.limit.ordinary-interior-life, don.limit.doubt-and-reception, don.limit.
basilica-archaeology, and all three ambient records carry relations: []
(no natural single reciprocity target, matching pahc's own precedent that
relations[] is sometimes empty for this record type).

===========================================================================
DOES NOT TOUCH
===========================================================================

Axido, Fasir, Article 23, Article 29 Limb 2; records/don/{source,term,
story,figure,quote,search_record,gravity,force,contested_claim,voice_craft,
demonstration}/ (read only, except the targeted reciprocity edits named
above and applied directly, not by this script's own code); records/
worlds.yaml; the M2 compiler.
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[3]  # .../cic-project
RECORDS_ROOT = REPO_ROOT / "records" / "don"

WORLD_ID = "don"
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

def build_witness_one_formation_aim() -> None:
    rid = "don.witness.one-formation-aim"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F3-I"],
        "confidence": conf("A", "verified-via-authority", "load-bearing", "Documented",
            divergence="This unity claim's own four component gravities (G1, G2, G3, G5) are each "
            "independently Documented at Doc_04's own per-gravity level; the claim that they are FACETS "
            "OF ONE AIM, rather than four separate commitments that happen to coexist, is Doc_07's own "
            "cross-lens synthesis (SS2I, SS6) -- a defensible, well-argued reading this build's own "
            "external-review section (Doc_07 SS7) itself flags for outside scholarly assessment, not an "
            "independently-attested Donatist self-description of the unity as such."),
        "sources": src(
            ("don.source.petilian-of-constantina-letters-quoted",
             "the conscience-of-the-giver proposition, G1's own quoted voice"),
            ("don.source.passio-donati-sermon",
             "the annual commemoration at the martyr's grave, G3's own enacted, repeated practice"),
            ("don.source.optatus-against-donatists",
             "Book III, Donatus's own reported retort, G5's own quoted voice"),
        ),
        "retrieval": retrieval(
            2,
            retrieve_when=[
                "participant asks why this community holds authority to belong to one line of bishops "
                "rather than another",
                "conversation is ready to hear purity, rebaptism, martyr-memory, and refusal of the "
                "state as one thing rather than four separate topics",
            ],
        ),
        "relations": rel(
            ("associated-with", "don.gravity.ministerial-purity"),
            ("associated-with", "don.gravity.martyr-cult-identity"),
        ),
        "positions": [
            "A minister's own tainted hand gives nothing valid; so we are washed again, by a hand that "
            "is clean, and that washing is the first true entry into this body, not a repetition of one "
            "that never took. We hold our own dead by name, at the grave, on the day appointed, and hear "
            "their account again so the same conviction is produced again in the hearing. And we refuse "
            "the state's own standing to say who the true church is. These are not four separate "
            "convictions that happen to sit beside one another in our own life. They are one conviction, "
            "seen from four sides: we are the pure, persecuted, true church, proved by what we will not "
            "concede and by what we have suffered for refusing to concede it.",
            "This is why our own bishops administer the washing, preach at the martyr's grave, and stand "
            "before an emperor's officer without treating any one of those three acts as separate from "
            "the others. A washing without the purity doctrine behind it would be an empty rite; a "
            "martyr's memory without the purity doctrine would be a grief with nothing to prove; a "
            "refusal of the state without the same doctrine behind it would be mere defiance. Held "
            "together, they are what we actually are.",
        ],
        "tensions": [
            "We do not claim this conviction was lived by us without strain. The same rule that requires "
            "a returning cleric to be washed and ordained again did not, in practice, hold against our "
            "own returning Maximianist clergy, received back without either rite; and the same refusal "
            "that says the emperor has no standing to judge us turned to that emperor's own machinery "
            "three times, when it served our case. We do not treat either fact as proof the doctrine was "
            "hollow, and we do not smooth it away. It is held, openly, inside the same conviction that "
            "states its own rule at full strength.",
        ],
        "text": (
            "We do not hold four separate beliefs that happen to sit together. We hold one thing, seen "
            "from four sides. A tainted hand gives nothing; so we are washed again, and that washing is "
            "our true entry, not a second attempt at something that already worked. We remember our own "
            "dead by name, at the grave, on the appointed day, because their death is the proof this "
            "conviction was never merely spoken. And we will not grant the emperor standing to decide "
            "which of two churches is the true one, because that is not his question to answer. Purity, "
            "the washing, the memory of our martyrs, and our refusal of the state -- these are one "
            "conviction, not four. We will also tell you, plainly, where holding it cost us something we "
            "did not resolve: the same rule we state absolutely did not, in fact, hold everywhere we "
            "state it; the same refusal we hold as principle we set aside three times when it served us. "
            "We say this ourselves, in the same breath as the conviction itself, because naming the "
            "strain is part of what we actually are, not an embarrassment we would rather you not ask "
            "about."
        ),
    }
    body = (
        "Grounded directly in Doc_07_Integrated_Ecology_Analysis.md SS2I ('Formation Logic and confirmed "
        "gravities... this world's formation logic is not four separate commitments... it is one "
        "conviction... expressed through every lens... at once') and SS6 (Integrative Observation: 'to "
        "be formed in this world was to hold an absolute conviction and a named, undenied exception to "
        "it in the same breath, without experiencing that as contradiction'), restated in don_World_"
        "Profile.md's own near-identical language (line 37: 'Its self-understanding organized around one "
        "conviction, worked out through every dimension of its formation life'). This is genuinely "
        "uncaptured doctrinal-witness content: every existing don.gravity.* record (register etic) "
        "classifies ONE gravity at a time against the six tests; no record states the UNITY claim itself "
        "in this world's own first-person voice, position-and-tension shaped, the way this record type "
        "calls for. G4 (the parallel hierarchy) is deliberately not folded into positions[] as a fifth "
        "facet, matching Doc_07 SS2I's own precise language: G4 is 'the institutional container all of "
        "this operates within,' not itself one of the four facets the launch brief and Doc_07 both name "
        "(G1/G2/G3/G5). T1 and T2 are named together in tensions[] rather than as two separate entries, "
        "matching Doc_07 SS2I's own closing sentence treating them as one honestly-held strain ('T1 and "
        "T2 are not exceptions to this formation logic but its own honestly-held internal strain'), not "
        "two independent findings. relations[] links to G1 and G3 only (not all four facets), following "
        "pahc.witness.apostolic-practice's own restraint (two relations, not one per topic discussed in "
        "prose) -- reciprocal edges added directly to don.gravity.ministerial-purity.md and don.gravity."
        "martyr-cult-identity.md after this script runs. canon_cells=['F3-I'] ('Who held authority among "
        "you, and how did anyone come to have it?') is this record's own best-fit fleet canon question: "
        "authority in this world runs on exactly the unified logic this record states (an unbroken, "
        "traidtor-free line, enacted, commemorated, and defended as one thing) -- the first don record to "
        "populate any canon_cells field, per this step's own CANON-COVERAGE FINDING above."
    )
    _write("doctrinal_witness", rid, payload, body)


def build_witness_boundary_is_doctrine() -> None:
    rid = "don.witness.boundary-is-doctrine"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F3-T"],
        "confidence": conf("A", "verified-direct", "load-bearing", "Documented",
            divergence=None),
        "sources": src(
            ("don.source.optatus-against-donatists",
             "Book III, the 313 petition's own quoted 'of the party of Donatus' language, and Optatus's "
             "own turn of it into an accusation"),
            ("don.source.passio-donati-sermon",
             "the preacher's own turn of 'catholic' into a sarcastic pun on impunity, per Mabillon's "
             "annotation"),
        ),
        "retrieval": retrieval(
            2,
            retrieve_when=[
                "participant asks whether this community was 'Catholic,' or asks what it called its rival",
                "conversation reaches how this world drew the line between itself and its rival",
            ],
        ),
        "relations": rel(
            ("associated-with", "don.term.caecilianist"),
            ("associated-with", "don.gravity.refusal-of-imperial-legitimacy"),
        ),
        "positions": [
            "We are the church. Our rival is not simply wrong about a doctrine; it has no standing to "
            "call itself by that name at all, since its own line runs back to a hand that gave up the "
            "scriptures. So we do not call it Catholic, as it calls itself. We call it Caecilianist, "
            "after the man whose tainted consecration is why we exist apart from it -- a naming choice, "
            "not a neutral label.",
            "The naming contest runs in both directions, and we do not pretend it does not. Our own "
            "clergy, petitioning the emperor, named themselves 'of the party of Donatus' in the formal "
            "record -- language our rival then turned back on us, as though we had named a man instead "
            "of naming the Church of Christ. And one of our own preachers turned their own word, "
            "'catholic,' into a joke: not universal, but the place where wrongdoing is done with "
            "impunity. Both sides fought over the same word, because the word itself was never a small "
            "matter. It is the boundary and the center, seen from two directions at once.",
        ],
        "tensions": [
            "The boundary we draw against our rival is not a boundary we have kept perfectly settled "
            "even among ourselves. The same purity logic that tells us who is outside the true church "
            "did not, in practice, hold against our own returning Maximianist clergy, received back "
            "without repeating the washing or the ordination it otherwise requires. We name this rather "
            "than pretend the line has never wavered on our own side of it.",
        ],
        "text": (
            "Call yourself Catholic if you like; we will not grant it to you. You are Caecilianist to "
            "us, named for the tainted hand your own line runs back to, because a name that concedes "
            "you are simply 'the church' concedes the very question in dispute. This is not a quarrel "
            "over words for their own sake. Refusing your name is the same act as refusing your "
            "sacraments: the boundary we draw and the doctrine we hold are one line, seen from two "
            "sides. And we will tell you plainly that this naming fight runs both directions -- you have "
            "turned our own petitions' language against us, and one of our own preachers turned your "
            "word back on you in the same breath. Nor will we tell you the line has always held even on "
            "our own side: we drew it against clergy who left us and then let some of them back in "
            "without asking them to cross it again. We say that too, because it is also true."
        ),
    }
    body = (
        "Grounded in Doc_07_Integrated_Ecology_Analysis.md SS2H (Boundary Structures): 'the boundary and "
        "the center are the same line, viewed from two directions'; 'Optatus's own quoted petition "
        "language shows Donatist clergy naming themselves \"of the party of Donatus\"... which Optatus "
        "turns into an accusation... while this world's own preacher... turns the word \"catholic\" itself "
        "back on the rival as a sarcastic pun on impunity.' Restated at don_World_Profile.md lines 225, "
        "227 in near-identical language ('the boundary-work in this world is not a separate activity from "
        "its central doctrine -- it IS the doctrine, applied outward'). don.term.caecilianist already "
        "states the WORD's own plain/quick meaning (a term record's own job, Tier-3-minimum per that "
        "record's own confidence note); this record states the BOUNDARY-LOGIC claim itself, with its own "
        "internal tension (T2, the Maximianist reception, the one place the boundary this record states "
        "did not, in practice, hold) -- genuinely different content, not a restatement of the term entry. "
        "canon_cells=['F3-T'] ('Was your church \"Catholic\"? Is there a church today I could visit that's "
        "yours?') is a direct, strong fit: the fleet's own canon question asks exactly the naming question "
        "this record answers. relations[] links to don.term.caecilianist (the naming term itself) and don."
        "gravity.refusal-of-imperial-legitimacy (Doc_07 SS2H's own forces-line: 'the Caecilianist/imperial "
        "alliance's own consistent legal recognition of the rival as \"the\" Catholic church is what this "
        "world's own naming strategy answers') -- reciprocal edges added directly to both files after this "
        "script runs."
    )
    _write("doctrinal_witness", rid, payload, body)


def build_witness_refusal_and_recourse() -> None:
    rid = "don.witness.refusal-and-recourse"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F1-E"],
        "confidence": conf("A", "verified-via-authority", "load-bearing", "Documented",
            divergence="Each of the three named turns to imperial power (313, 361, the 390s) is "
            "independently Documented on its own historical terms (Doc_04 SS3.6); the characterization of "
            "the whole pattern as 'principled refusal against pragmatic exception,' rather than simple "
            "incoherence, is Doc_04's own synthesis of Doc_01 SS5's language, not itself independently "
            "attested as this world's own self-description of the tension -- named here rather than "
            "smoothed over, matching don.gravity.principled-refusal-vs-pragmatic-recourse's own "
            "divergence_note."),
        "sources": src(
            ("don.source.optatus-against-donatists",
             "Book III, line 1904, Donatus's own reported retort ('Quid est imperatori cum ecclesia?')"),
            ("don.source.optatus-appendix-of-documents",
             "Anulinus's own relatio, the 313 petition to Constantine"),
        ),
        "retrieval": retrieval(
            2,
            retrieve_when=[
                "participant asks whether this community believed the state had any standing to decide "
                "who the true church was",
                "conversation is ready to hold the refusal of imperial legitimacy alongside the specific "
                "moments this world turned to that same power",
            ],
        ),
        "relations": rel(
            ("associated-with", "don.gravity.principled-refusal-vs-pragmatic-recourse"),
            ("associated-with", "don.quote.donatus-quid-est-imperatori"),
        ),
        "positions": [
            "\"What has the emperor to do with the church?\" One of our own primates is remembered to "
            "have said exactly this, and we hold it still: the question of which church is the true one "
            "is not the emperor's to settle. He may rule, and has ruled, against us -- at Rome in 313, at "
            "Arles in 314, and again at Carthage in 411 -- but a ruling from a power with no standing to "
            "judge the question is not a verdict we are bound to accept as one.",
            "And yet we will not pretend we never turned to that same power ourselves. In 313 we brought "
            "our own case to Constantine, through the governor Anulinus. In 361 we asked Julian to give us "
            "back basilicas that had been taken from us. And in the 390s we invoked that same emperor's "
            "own law against our own Maximianist dissidents. Three times, at three real moments, we used "
            "the very machinery whose standing to judge us we otherwise deny. We do not call this a "
            "betrayal of our own principle. We call it what it plainly is: a refusal, held as our settled "
            "posture, with three named exceptions where it served our case to reach for the thing we "
            "refuse.",
        ],
        "tensions": [
            "We do not resolve this into either 'we never really meant the refusal' or 'those three turns "
            "were not really us.' Both are true at once, plainly stated, in the same record: the emperor "
            "has no standing to judge us, and three times we asked him to rule in our favor anyway. We "
            "hold both, because our own record holds both, and we would rather you see the whole of it "
            "than a tidier half.",
        ],
        "text": (
            "\"What has the emperor to do with the church?\" That is our own primate's answer to the "
            "question of who may judge us, and we still give it. The state has ruled against us more than "
            "once, and a ruling from a power with no standing to judge the question is no verdict at all. "
            "But we will tell you plainly what our own record also holds: three times, we went to that "
            "same power ourselves, when it served our case to do so -- once petitioning the emperor "
            "himself for a hearing, once asking a different emperor for our seized buildings back, once "
            "using that same emperor's own law against our own dissidents. We do not call ourselves "
            "inconsistent for this, and we do not call it a secret. Refusal is our settled stance. The "
            "three times we set it aside are named in the same breath as the stance itself, because that "
            "is what our own history actually holds -- not a rule kept perfectly, but a rule stated "
            "honestly, exceptions and all."
        ),
    }
    body = (
        "Grounded in Doc_04_Gravity_Discovery.md SS3.6 (T1, Principled Refusal vs. Pragmatic Recourse to "
        "Imperial Power: three named, dated instances -- 313, 361, the 390s -- each independently "
        "Documented) and Doc_07 SS4/SS6 ('the doctrine's own qualifications are not random lapses; they "
        "track the forces exactly'; 'this world's own three qualified turns to imperial power... are not "
        "embarrassments quietly managed but facts this world's own record states plainly'). Donatus's own "
        "retort is quoted verbatim from the already-cleared don.quote.donatus-quid-est-imperatori record "
        "(text field, matching that record's own verbatim license exactly, not re-translated here). T1 "
        "already has a classified gravity record (don.gravity.principled-refusal-vs-pragmatic-recourse, "
        "register etic) and a cleared quote, but no record states T1 in first-person doctrinal-witness "
        "voice with its own position/tension structure -- this is the first. canon_cells=['F1-E'] ('When "
        "belief was disputed, who had the right to decide -- and how do we know how that worked?') is a "
        "strong direct fit: T1 is precisely a dispute over who has the right to decide ecclesial "
        "legitimacy. relations[] links to the T1 gravity and the Donatus quote -- reciprocal edges added "
        "directly to don.gravity.principled-refusal-vs-pragmatic-recourse.md and don.quote.donatus-quid-"
        "est-imperatori.md after this script runs."
    )
    _write("doctrinal_witness", rid, payload, body)


# ===========================================================================
# honest_limit
# ===========================================================================

def build_limit_ordinary_interior_life() -> None:
    rid = "don.limit.ordinary-interior-life"
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
            ("don.core.donatism",
             "this world's own thinness field: 'thinner on the ordinary Numidian believer's own words "
             "despite being, for long stretches, the numerically dominant church'"),
        ),
        "relations": [],
        "statement": (
            "You ask me to walk you through an ordinary day. I cannot. Not because nothing happened -- "
            "for most of our own history, in Numidia especially, we were not a small band apart from "
            "everyone else. We were the ordinary church of the whole region. But almost nothing written "
            "by an ordinary member of ours has come down to us. What survives is councils, letters, "
            "arguments, and the words of men who wrote to attack us. What an ordinary day actually looked "
            "like -- waking, working, gathering, eating -- our own record does not say. We would rather "
            "tell you that plainly than describe a day we cannot actually show you."
        ),
        "why_sources_cannot_answer": (
            "Doc_08_Forces_Document.md Force 2B-2 (Transmission, Layer 2) states directly: 'no surviving "
            "Donatist chronicle of Arles, no surviving Donatist administrative account of the Macarian "
            "repression exists'; Doc_08 SS6 names this as lost 'structurally rather than accidentally... "
            "not because these things were never produced... but because nothing in either transmission "
            "channel had reason to preserve them.' Doc_09_Story_Inventory.md SS8 item 1 independently "
            "confirms the same finding at the level of narrative genre: 'No Tier 1 or Tier 2 story exists, "
            "or can exist, from the ordinary Numidian believer's own voice... a source-mediation problem, "
            "not a scale problem' (don.core.donatism's own thinness field, item 8 of cautions). "
            "Representative/don_Rep_Phase1_Ecology_Assessment.md SS2 confirms this is structurally "
            "underrepresented regardless of which role a Representative takes: 'a bishop's record is "
            "exactly the record that survives; the layperson's is exactly what does not.' This is a "
            "population-scale absence, not an elite-skew one: Donatism was, for substantial regions and "
            "periods, the numerically dominant church, and the gap still holds."
        ),
        "nearest_material": [
            "don.core.donatism",
            "don.gravity.parallel-institutional-hierarchy",
            "don.witness.one-formation-aim",
        ],
    }
    body = (
        "One of six honest_limit records built together this step, per the launch brief's own Doc_09/"
        "Phase One/Phase Seven cross-check. Celled to F5-I ('Walk me through an ordinary day among your "
        "people, from waking to sleeping') -- a direct match, the exact question this world's own record "
        "cannot answer. Distinguished explicitly from don.limit.doubt-and-reception (the EMOTIONAL "
        "interior specifically, incl. the 411-verdict/Vandal-conquest reception) -- this record's own "
        "scope is the daily/practical interior and routine, per Phase One SS2's own Force 2B-2 citation. "
        "No relations[] edge: no single existing record is the natural reciprocity target for a blanket "
        "population-scale absence (matching pahc.limit.ordinary-majority's own relations: [] choice for "
        "the analogous pahc finding)."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_doubt_and_reception() -> None:
    rid = "don.limit.doubt-and-reception"
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
            ("don.core.donatism",
             "this world's own thinness field: 'the ordinary believer's interior life -- doubt, fear, a "
             "traditor's own account of surrendering scripture -- is a register a hostile-mediated record "
             "structurally does not preserve'"),
        ),
        "relations": [],
        "statement": (
            "Was there room among us for doubt? I will not pretend our record can answer that from the "
            "inside. What survives is the record of those who held firm -- the martyrs, the councils, the "
            "bishops who argued the case. What a believer felt who wavered, who feared, or who quietly "
            "drifted back to the rival church -- none of that is in our own words anywhere. Nor can I "
            "tell you how our own people received the ruling against us at Carthage in 411, or the day "
            "the empire that had so long ruled against us fell to another power entirely. Those days "
            "happened. What they felt like from inside, our own record does not say."
        ),
        "why_sources_cannot_answer": (
            "Doc_08_Forces_Document.md's own governing-principles synthesis (SS8) states the community's "
            "reception of the 411 verdict, the Vandal conquest, and this world's own later institutional "
            "attrition 'is not recoverable from surviving sources' at Forces 3A-1, 3A-2, 3B-1, and 3B-2 -- "
            "each stated in its own distinct wording, per Representative/don_Rep_Phase1_Ecology_Assessment."
            "md SS2's own precise account (3A-1: 'this world's own record does not preserve a direct "
            "account of how its own participants received this specific verdict'; 3A-2/3B-2: 'not "
            "recoverable from surviving sources,' used directly). The surviving emotional register (Doc_07 "
            "SS2B) is vindication and defiant joy, 'because that is what the transmission mechanism "
            "preserved' -- the register of those who held firm, not of those who wavered. Representative/"
            "don_Rep_Phase7_Encounter_Ecology_Mapping.md SS4/SS9 independently confirm this finding "
            "against the tested Representative's own construction record: this domain was correctly "
            "handled as 'THIN, redirection not information-dump,' never filled with invented interior "
            "content."
        ),
        "nearest_material": [
            "don.core.donatism",
            "don.gravity.martyr-cult-identity",
            "don.gravity.refusal-of-imperial-legitimacy",
        ],
    }
    body = (
        "Celled to F1-P ('Was there room among your people for doubt?') -- the fleet's own direct match "
        "for this exact absence. Folds together, as one honest_limit rather than two, both halves Phase "
        "One SS2's own Thinness Mapping and Phase Seven SS4 name under the same underlying cause "
        "(interior emotional experience unrecoverable from a hostile-mediated transmission channel): the "
        "GENERAL interior of doubt/fear/wavering, and the SPECIFIC, dated absence of any reflective "
        "community account of receiving the 411 verdict or the Vandal conquest (Doc_08 Forces 3A-1/3A-2/"
        "3B-2) -- both are the identical evidentiary fact (a hostile-mediated record structurally "
        "preserves only the vindicated register) stated at two different grains, per Phase One SS2's own "
        "account. Distinguished explicitly, per Phase Seven SS4/SS7.2's own repeated correction, from the "
        "411 Conference's own STORY simply not having been written yet (Doc_09 SS8 item 2, 'an open "
        "integration task, not a source-availability absence') -- that is not an evidentiary gap and no "
        "honest_limit is built for it anywhere in this script. No relations[] edge: this is a blanket, "
        "multi-force absence with no single natural reciprocity target."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_womens_own_voice() -> None:
    rid = "don.limit.womens-own-voice"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        # Framing-heavy statement ("we cannot show you...", "we would rather tell you plainly")
        # shares canon cell F6-P with don.demo.undiscovered-traditor -- matching pahc.limit.
        # womens-own-words' own judgment call (identical risk, identical fix) rather than left
        # to the auto-tagger's own word-overlap floor to sort out by coincidence.
        "demo_tag": "exclude",
        "canon_cells": ["F6-P"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented", divergence=None),
        "sources": src(
            ("don.source.lucilla-and-second-woman-maximianist",
             "Optatus I.16 (Lucilla, named, at the schism's founding); Augustine, Letter XLIII SS26 (a "
             "second woman, left unnamed, behind the Maximianist schism)"),
        ),
        "relations": rel(("associated-with", "don.figure.lucilla")),
        "statement": (
            "Two women stand at the center of our own history. One, Lucilla, a wealthy woman of Carthage, "
            "is named directly: her grievance and her money are said to have made the rival consecration "
            "happen that gave us our first bishop. A second woman is named just as directly as having "
            "stirred up the schism inside our own schism, years later -- but her own name is not given, "
            "even by the one source that draws the comparison. Both women had real standing. Neither "
            "woman's own words survive. Everything we know of either of them, we know through a man's "
            "pen, written to explain why something happened, not to let her speak for herself."
        ),
        "why_sources_cannot_answer": (
            "Doc_02_Source_Ecology.md SS6 (Gender, Article 20) states the vendored corpus's own gender "
            "finding in full: Lucilla is reconstructed 'only to the bound Optatus's own hostile text "
            "supports... a named woman of means with the standing to make a rival consecration happen, "
            "nothing beyond that bound asserted of her own motivations or character' (Article 20's own "
            "bounded-reconstruction test, don.figure.lucilla's own divergence_note). A second, parallel "
            "case -- an unnamed woman Augustine (Letter XLIII SS26) says 'stirred up' the Council of "
            "Maximian against Primian, 'precisely as' Lucilla did against Caecilian -- is attested but "
            "does not meet the bounding test for even that limited a reconstruction, since the source "
            "gives her no name at all. Doc_02 SS6 states directly: 'No comparably individually-attested "
            "Caecilianist-side or ordinary-believer woman has been identified this pass'; 'no further "
            "case meeting any of the three bounding conditions has been identified... for any other "
            "specific ordinary believer's or marginalized voice's perspective.' In both cases, a woman's "
            "consequential agency is attested by a hostile author who needed to name it to make his own "
            "accusation land -- but a woman's own voice, in her own words, is attested nowhere in this "
            "world's vendored record."
        ),
        "nearest_material": [
            "don.figure.lucilla",
            "don.story.lucilla-consecration-dispute",
            "don.witness.one-formation-aim",
        ],
    }
    body = (
        "Celled to F6-P ('You've told me what women's days were like -- but could a woman carry real "
        "authority among you, and what did it cost her?') -- the fleet's own direct match; both attested "
        "women in this world's own record DID carry the kind of consequential agency this canon question "
        "asks about (making or unmaking a bishop), which is exactly why the limit is narrower than "
        "'women are thin here': presence and consequential agency are attested twice; a woman's own "
        "words, in either case, are attested nowhere -- the same narrowing discipline pahc.limit.womens-"
        "own-words applies to its own analogous finding. demo_tag: exclude set for the reason stated "
        "inline above (a real cell-sharing collision with don.demo.undiscovered-traditor, F6-P, per "
        "engine/m2/builders.py's own _demonstration_candidates()). relations[] links to don.figure.lucilla "
        "(the one bounded reconstruction this record's own limit is precise about) -- reciprocal edge "
        "added directly to don.figure.lucilla.md after this script runs."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_bagai_violence_no_account() -> None:
    rid = "don.limit.bagai-violence-no-account"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F3-P"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented", divergence=None),
        "sources": src(
            ("don.source.augustine-correction-of-donatists-letter-185",
             "the near-fatal attack on the Catholic bishop Maximianus of Bagai, 404 -- one of the specific, "
             "named hostile allegations this record cannot confirm, deny, or contextualize from our own "
             "side"),
        ),
        "relations": rel(("associated-with", "don.gravity.circumcellion-agonistici")),
        "statement": (
            "You ask whether we ever failed to hold our own people accountable for real harm. There are "
            "specific, named charges against us: a bishop beaten and nearly killed at Bagai; a converted "
            "presbyter dragged from his house and beaten; men said to have been forced back to our own "
            "washing against their will. These are not vague rumors -- they are dated, specific, and come "
            "from named men who say they witnessed or suffered them. I cannot tell you our own side of "
            "any of them. No account from inside our own communion, answering these charges in our own "
            "words, survives anywhere. I will not build you one out of what is not there."
        ),
        "why_sources_cannot_answer": (
            "Doc_09_Story_Inventory.md SS8 item 3 states this finding in full: hostile sources record "
            "'specific, dated allegations' -- the forced rebaptism of the 'Mappalians' (Augustine, Letter "
            "LXVI); a converted presbyter beaten and held twelve days (Letter LXXXVIII); the near-fatal "
            "attack on Maximianus of Bagai, 404 (Letter 185, The Correction of the Donatists) -- 'but this "
            "world has no surviving account of any of them in its own voice, and so cannot answer them, "
            "confirm them, contextualize them, or dispute their particulars from the inside.' Doc_09 itself "
            "'deliberately does not build a story chunk from the hostile accounts themselves: doing so "
            "would let this world's own Story Repository narrate an atrocity attributed to it entirely "
            "through its accuser's own telling' -- this record follows the identical discipline: it states "
            "the limit itself, not the allegations' own content, and does not repeat the specific charges "
            "as though this world could confirm or dispute them."
        ),
        "nearest_material": [
            "don.gravity.circumcellion-agonistici",
            "don.contested.circumcellion-character",
        ],
    }
    body = (
        "Celled to F3-P ('Did your churches ever fail to hold their own people accountable for real harm "
        "-- and if so, what happened?') -- a direct match for exactly the shape of question this world's "
        "own record cannot answer from the inside. Distinguished from don.contested.circumcellion-"
        "character (a genuine, already-built scholarly contest over the group's typical CHARACTER and "
        "SCALE, register etic) -- this record's own limit is narrower and different in kind: not whether "
        "the hostile portrait is overstated, but whether THIS WORLD'S OWN RECORD can speak, in its own "
        "voice, to these SPECIFIC, dated, named episodes at all. It cannot, on either question. Per Doc_09 "
        "SS8 item 3's own discipline (quoted above), this record's own statement does not itself narrate "
        "the specific allegations' content in a way that could be mistaken for this world confirming, "
        "denying, or minimizing them -- it names the limit, once, at the level of generality Doc_09 itself "
        "uses. relations[] carries one edge, to don.gravity.circumcellion-agonistici (the D-A gravity this "
        "limit's own subject matter falls under) -- reciprocal edge added directly to that file after this "
        "script runs. No relations[] edge to don.contested.circumcellion-character specifically (a "
        "different claim, sourced and reasoned differently); nearest_material lists it instead, per that "
        "field's own job."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_theology_beyond_tyconius() -> None:
    rid = "don.limit.theology-beyond-tyconius"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F2-I"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented", divergence=None),
        "sources": src(
            ("don.source.tyconius-liber-regularum",
             "the one substantial counter-example to the thinness this record states -- this world's own "
             "strongest surviving theological writing, and the limit of it"),
        ),
        "relations": rel(("associated-with", "don.figure.tyconius")),
        "statement": (
            "How did we read our own scriptures -- what did we look for in them? I can give you one real "
            "answer, and then I must tell you where it stops. One of our own, Tyconius, wrote seven rules "
            "for reading scripture rightly, and it is the strongest theological writing our own people "
            "ever produced. His own council condemned him for it. Beyond that one case, we did not build "
            "a school of interpretation, a settled method, or a body of teachers who argued scripture the "
            "way we argued the purity of a minister's hand. What we argued, and argued well, was one "
            "question. Broader scriptural reflection beyond that one man's work is not something our own "
            "record can show you."
        ),
        "why_sources_cannot_answer": (
            "Doc_07_Integrated_Ecology_Analysis.md SS2D states this world's own doctrinal-philosophical "
            "record is 'genuinely thin... beyond the purity/rebaptism cluster,' with Tyconius's Liber "
            "Regularum 'the one strong counter-example, produced by a figure his own party ultimately "
            "condemned, whose exegetical method reached both rival churches without ever anchoring a "
            "following of his own.' Doc_05_Ecological_Reconstruction.md SS6.5 independently confirms this "
            "as 'a genuine absence in the record, not filled with plausible-sounding content it cannot "
            "support': 'this world's own ordinary interpretive or doctrinal formation, beyond the purity/"
            "rebaptism/martyr-cult/imperial-refusal spine already reconstructed above, is not established "
            "well enough in the vendored record to narrate from inside.' Doc_04 SS2 independently confirms "
            "the structural reason: Tyconius's own hermeneutics (D-B) failed Persistence and Dependency as "
            "a gravity candidate precisely because 'his own party's council condemned him... and no "
            "following continued his approach.' This is a genuine absence of a broader tradition, not a "
            "claim that Tyconius himself is thin -- his own work and its condemnation are well attested "
            "and fully carried elsewhere in this world's own record."
        ),
        "nearest_material": [
            "don.figure.tyconius",
            "don.term.liber-regularum",
            "don.story.tyconius-condemnation",
        ],
    }
    body = (
        "Celled to F2-I ('How did you read your scriptures? What did you look for in them?') -- a direct "
        "hermeneutics-shaped question this world's own record can answer richly for exactly one figure "
        "and thinly for everyone else. Explicitly NOT a claim that Tyconius himself, his condemnation, or "
        "the Liber Regularum are thin -- all three are already well-attested and fully carried by don."
        "figure.tyconius, don.term.liber-regularum, and don.story.tyconius-condemnation (Tier 1). The "
        "limit this record states is specifically BEYOND that one case: no broader school, method, or "
        "body of teachers, per Doc_07 SS2D/SS3B and Doc_05 SS6.5's own explicit disclosure. relations[] "
        "links to don.figure.tyconius (the one case this limit's own contrast depends on) -- reciprocal "
        "edge added directly to don.figure.tyconius.md after this script runs."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_basilica_archaeology() -> None:
    rid = "don.limit.basilica-archaeology"
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
            ("don.source.deo-laudes-acclamation-cil8",
             "what DOES survive materially -- four catalogued stone inscriptions, independent of the "
             "archaeology this record states is genuinely undone"),
        ),
        "relations": [],
        "statement": (
            "If archaeologists dug up the places we met, what would they find? Stone, in a few places: "
            "our own words, Deo laudes, cut where anyone could read them, at Bagai and elsewhere. Beyond "
            "that, I cannot tell you. No basilica of ours has been excavated and identified as ours with "
            "enough care that I can describe it to you -- its shape, its size, what stood inside it. Our "
            "buildings were seized more than once, and given back more than once, across our own history. "
            "What the ground itself would show you, beyond the stone that already speaks for itself, has "
            "not yet been dug up and checked carefully enough for me to say."
        ),
        "why_sources_cannot_answer": (
            "Doc_02_Source_Ecology.md SS5 and Doc_07_Integrated_Ecology_Analysis.md SS2G state this "
            "domain's own uneven character precisely: the Deo laudes acclamation is 'independently and "
            "directly attested' on stone (four catalogued inscriptions, CIL VIII 17732, 20482, 17368, "
            "18669), 'no literary mediation at any point.' Basilica archaeology across Numidia, by "
            "contrast, is 'named in the field literature as a real, recognized evidentiary category... "
            "but this construction pass has not independently verified it against a specific site report "
            "or excavation record -- Confidence C, flagged for future verification rather than exploited "
            "prematurely.' Representative/don_Rep_Phase1_Ecology_Assessment.md SS2 confirms this is 'an "
            "archaeological gap, distinct in kind from the transmission-caused gaps' named elsewhere in "
            "this world's own record -- not a source-mediation problem (nothing was hidden or lost to a "
            "hostile pen) but a piece of fieldwork this construction has not yet done."
        ),
        "nearest_material": [
            "don.term.deo-laudes",
            "don.quote.deo-laudes-acclamation",
            "don.gravity.martyr-cult-identity",
        ],
    }
    body = (
        "Celled to F5-E ('If archaeologists dug up the place you met, what would they find?') -- a direct "
        "match. This record's own confidence is deliberately set lower than the other five honest_limit "
        "records in this script (C / named-not-rechecked / illustrative / Inferential-Thin, matching Doc_02 "
        "SS5's own explicit Confidence-C rating for basilica archaeology) rather than the B/verified-direct/"
        "load-bearing/Documented baseline the transmission-caused absences use -- this is the one honest_"
        "limit in this script whose OWN underlying gap is itself Confidence C (an unfinished piece of "
        "fieldwork this construction has not yet done), not a Documented structural absence in what "
        "survives. nearest_material lists what DOES survive materially (the Deo laudes epigraphy, already "
        "fully covered by don.term.deo-laudes/don.quote.deo-laudes-acclamation) to state the contrast "
        "this record's own statement draws, without a relations[] edge to any of them (a different "
        "evidentiary category -- epigraphy, not excavation -- so no direct reciprocity claim is made)."
    )
    _write("honest_limit", rid, payload, body)


# ===========================================================================
# ambient
# ===========================================================================

def build_ambient_doubled_towns() -> None:
    rid = "don.ambient.doubled-towns"
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
            ("don.source.optatus-against-donatists",
             "the parallel-hierarchy pattern this record's own physical detail rests on, town for town"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "In many towns of Roman North Africa, two churches stood where most towns elsewhere had one: "
            "one congregation gathered under a bishop of our own communion, another under a bishop of the "
            "rival, sometimes within sight of one another in the same town, the same street. Two "
            "processions, two clergies, two sets of church buildings, contesting the same ground."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "Doc_05_Ecological_Reconstruction.md SS4 ('not one bishop per see but two, contesting the same "
        "city and congregation the length and breadth of Roman North Africa') and Doc_01 SS2 (the "
        "parallel hierarchy's own town-for-town replication). This record states only the visible, "
        "physical/social shape of a town carrying two complete congregations side by side -- the "
        "DOCTRINAL significance of that fact (which line is valid, and why) is already fully stated at "
        "don.gravity.parallel-institutional-hierarchy and don.gravity.ministerial-purity; formation_claim_"
        "barred: true asserts this record makes no claim about which line was true or what belonging to "
        "either meant, matching the one fleet precedent's own trailing-body framing (records/fix/ambient/"
        "fix.ambient.daily-bread.md). canon_cells: [] and relations: [], matching that same precedent "
        "exactly."
    )
    _write("ambient", rid, payload, body)


def build_ambient_bagai_gathering_scale() -> None:
    rid = "don.ambient.bagai-gathering-scale"
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
            ("don.source.augustine-on-baptism-against-donatists",
             "the Bagai council's own recorded scale, 394"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "At Bagai, in 394, more of our own bishops gathered in one place than most towns of Roman "
            "North Africa saw in a generation: three hundred and ten of them, meeting as a single council "
            "in one place, at one time."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "Doc_04_Gravity_Discovery.md SS3.6 and Doc_05 SS4 ('the party's own much larger council at Bagai "
        "(394)... 310 bishops strong' -- the specific numeral traced to Augustine's own primary text, the "
        "same source don.story.bagai-reconciliation cites). This record states only the bare physical/"
        "logistical scale of the gathering itself (this many people, in one place, at one time) -- the "
        "council's own verdict and T2's own doctrinal content (the Maximianist reception without "
        "rebaptism or reordination) are already fully stated at don.gravity.purity-rigor-vs-institutional-"
        "reception and don.story.bagai-reconciliation, and are not restated or re-argued here. canon_"
        "cells: [] and relations: [], matching the fixture precedent."
    )
    _write("ambient", rid, payload, body)


def build_ambient_deo_laudes_as_object() -> None:
    rid = "don.ambient.deo-laudes-as-object"
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
            ("don.source.deo-laudes-acclamation-cil8",
             "the four catalogued inscriptions this record describes as physical objects"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "Our own two words, Deo laudes, are cut into stone in four places catalogued so far -- the "
            "clearest at Bagai itself, one of our own two named principal seats. Plain lettering, on "
            "plain stone, still legible today, set there long before any historian went looking for it."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "Doc_02_Source_Ecology.md SS5 and Doc_07 SS2G (four catalogued inscriptions, CIL VIII 17732, "
        "20482, 17368, 18669, the strongest from Bagai itself). This record states the bare physical fact "
        "of the stone objects themselves -- what survives, where, in what medium -- not the acclamation's "
        "own liturgical/formation meaning (spoken in worship, set against the rival's Deo gratias, and "
        "what saying it means for belonging), which is already fully stated at don.term.deo-laudes, don."
        "quote.deo-laudes-acclamation, and don.gravity.martyr-cult-identity. canon_cells: [] and relations: "
        "[], matching the fixture precedent."
    )
    _write("ambient", rid, payload, body)


def main() -> None:
    build_witness_one_formation_aim()
    build_witness_boundary_is_doctrine()
    build_witness_refusal_and_recourse()
    build_limit_ordinary_interior_life()
    build_limit_doubt_and_reception()
    build_limit_womens_own_voice()
    build_limit_bagai_violence_no_account()
    build_limit_theology_beyond_tyconius()
    build_limit_basilica_archaeology()
    build_ambient_doubled_towns()
    build_ambient_bagai_gathering_scale()
    build_ambient_deo_laudes_as_object()
    print(f"Wrote {len(WRITTEN)} records:")
    for p in WRITTEN:
        print(f"  {p}")


if __name__ == "__main__":
    main()
