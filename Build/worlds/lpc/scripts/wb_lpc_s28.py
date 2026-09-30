"""S2x equivalent, lpc: Latin Pastoral-Congregational Christianity (`lpc`)
doctrinal_witness / honest_limit / ambient records -- the three record
types not yet built for this world, plus a small check on
world_core.cautions. No name in the old process doc's own step numbering
(this step sits between the B-series record-native passes and any later
canon_cells tagging pass), so it is named `s28` in this world's own
sequence -- the direct next-numbered file after wb_lpc_s27.py (B-7,
voice_craft/demonstration) -- rather than forced into the B-series, since it
is a genuinely different unit of work from B-1 through B-7.

SCHEMAS VERIFIED DIRECTLY THIS SESSION (engine/m1/schemas.py TYPE_PROPERTIES,
not trusted from Build/worlds/don/scripts/wb_don_s2x_doctrinal_witness.py's own
summary): doctrinal_witness = {text: str, positions: [str], tensions: [str]};
honest_limit = {statement: str, why_sources_cannot_answer: str,
nearest_material: [str]}; ambient = {detail: str, formation_claim_barred:
{const: True}}. All three in COMPLETION_REQUIRED (engine/m1/gates.py) with
exactly those fields required. engine/m1/spoken_fields.py ATTRIBUTION_FIELDS/
PERSPECTIVE_FIELDS confirmed directly: doctrinal_witness.text and
honest_limit.statement are scanned by BOTH gate_no_build_attribution and
gate_voice_perspective; ambient.detail is scanned by perspective only (no
attribution risk field for ambient beyond detail, and formation_claim_barred
is a boolean, not prose). Every field below is written in first-person
"we/our" register throughout, checked by hand against the "this world"/"the
world's own" outside-vantage patterns. gate_canon_coverage (engine/m1/
canon.py) requires every one of the fleet's 28 canon cells to carry either
>=1 substantive record (doctrinal_witness/term/story/quote -- demonstration
and gravity/force do NOT count, per canon.substantive_types(), confirmed
directly) or exactly one honest_limit, never both zero and never more than
one honest_limit per cell -- checked directly that none of the 6 cells
chosen below already carries an honest_limit (none does; no lpc honest_limit
record existed before this script).

CANON-COVERAGE FINDING, checked directly before writing anything: every lpc
record built through B-7 (279 records, wb_lpc_s21.py through wb_lpc_s27.py)
carries canon_cells: [] except the 3 demonstration records built at B-7
(F4-I, F6-P, F6-I) -- confirmed by grep across records/lpc/*/*.md.
demonstration is not a substantive type, so all 28 cells still register as
blank for gate_canon_coverage's own purposes. This script's own doctrinal_
witness and honest_limit records are the FIRST lpc records to populate
canon_cells with a substantive or honest_limit-counted tag. Ten cells total
are touched below (3 by doctrinal_witness, 6 by honest_limit, cell overlap
disclosed at each record); the fleet's own remaining 18+ cells are NOT
addressed by this pass -- a full canon_cells tagging sweep (don's own
wb_don_s2y_canon_cells.py equivalent) is a separate, later step this script
does not attempt.

WORKED EXAMPLES READ IN FULL THIS SESSION: records/pahc/doctrinal_witness/
pahc.witness.apostolic-practice.md (text/positions/tensions triple, register
emic, cited to real primary sources, relations to a force, retrieval tier 2,
gate discipline noted in its own trailing body); records/pahc/honest_limit/
pahc.limit.womens-own-words.md (statement/why_sources_cannot_answer/
nearest_material triple, demo_tag: exclude used because the statement's own
framing vocabulary false-tags unrelated demo sentences sharing its canon
cell -- checked directly against engine/m2/builders.py's own
_demonstration_candidates()/_DEMO_CANDIDATE_TYPES, confirmed doctrinal_
witness/honest_limit/gravity/force/term/story/quote/contested_claim all
count as demo candidates when they share a cell with a demonstration and
lack demo_tag: exclude); records/fix/ambient/fix.ambient.daily-bread.md (the
one real worked example anywhere in the built fleet for this record type --
`find records -type d -iname ambient` returns only this fixture and don's
own three records, no other world has built any yet) and don's own three
built ambient records (records/don/ambient/don.ambient.*.md), read for the
real, non-fixture house style: detail states only the bare physical/social
fact, canon_cells: [] and relations: [] throughout (no natural single
reciprocity target for a physical scene-setting fact), formation_claim_
barred: true asserted explicitly in every record.

Read Build/worlds/don/scripts/wb_don_s2x_doctrinal_witness.py in full before this
script was written (not touched by it, not re-run by it) for the don-
equivalent docstring/code-pattern discipline (MECHANICAL-vs-AUTHORED,
RECIPROCITY, cell-collision/demo_tag discipline) -- carried over directly,
adapted to lpc's own construction record throughout.

===========================================================================
SOURCE MATERIAL, PER RECORD TYPE
===========================================================================

DOCTRINAL_WITNESS (3 records) -- this world's own doctrinal self-
understanding, in its own voice, distinct from gravity (etic, six-test
classification), contested_claim (etic, a scholarly dispute), and
demonstration (dialogue built around one canon_question). Checked against
every existing lpc.gravity.*/lpc.contested.*/lpc.demo.*/lpc.term.* record
before writing, to find genuinely uncaptured doctrinal-witness-shaped
material rather than duplicate it:

  1. lpc.witness.answerability-as-ground -- Doc_07 §2I (Formation Logic,
     "applied after all other lenses... every other lens converges here")
     and §6 (Integrative Observation: "The conviction underneath everything
     else here is not that the church is pure, nor that it is right, but
     that it is answerable"). No existing lpc record states this UNITY
     claim in first-person voice -- lpc.gravity.* records classify G1/G2/
     G3/G6 separately (etic); no demonstration takes the convergence itself
     as its own subject. Genuinely new doctrinal-witness content. DISCLOSED
     DIRECTLY, per lpc.core.latin-pastoral-congregational-christianity's
     own divergence_note (checked directly, read in full this session):
     "Doc_07 §2I's own convergence finding... is this build's own synthetic
     judgment, stated as such at Doc_07 §5, not a claim any single source
     states in those terms" -- carried forward on this record's own
     divergence_note rather than presented as more settled than the
     world_core record itself allows.
  2. lpc.witness.communion-over-separation -- Doc_07 §2H (Boundary
     Structures): "The internal rule is G3... Disagreement is expected;
     separation is the thing this world organizes itself to avoid" --
     paired with its own real complication, stated in the same section:
     "the Felicissimus schism opening during Cyprian's own absence in
     hiding, and the roughly contemporaneous Novatianist rival consecration
     at Rome -- both boundary failures of exactly the kind G3 exists to
     prevent, and both inside Cyprian's own phase." No existing record
     states the boundary-logic CLAIM itself as a doctrinal position with
     its own tension -- lpc.gravity.collegial-communion-preserved states
     the six-test classification (etic), not this world's own first-person
     account of why the rule exists.
  3. lpc.witness.confessor-claim-vs-regulated-peace -- G8, the one
     classified Tensional gravity (lpc.gravity.confessor-authority-vs-
     episcopal-peace), restated in first-person doctrinal-witness voice,
     position-and-tension shaped, matching World Capsule Core's own "What
     This World Holds Without Resolution" §2 exactly: "This world also
     holds a claim to grant peace that its own regulated order does not
     fully absorb... You hold both as genuine: the process that must
     govern, and the claim that pressed hard enough to require a process
     at all." No existing record states this AS a doctrinal witness in
     Datus's own voice -- the gravity record states it etically.

HONEST_LIMIT (6 records) -- every genuine "this world's record cannot speak
to X" finding already on record, checked against lpc_Rep_Phase1_Ecology_
Assessment.md §2 (Thinness Mapping), Doc_07_Integrated_Ecology_Analysis.md
§7 (Gaps and Limits), Doc_09_Story_Inventory.md §5 item 4 (cross-phase
women's-voice finding) and §7/§8 (Absent Stories, Open Items), and lpc.core.
latin-pastoral-congregational-christianity's own thin_topics field -- each
domain independently named across at least two of these documents, none
already substantively covered by an existing lpc term/story/quote/
doctrinal_witness record (every one of which, pre-B-7 demonstrations aside,
carries canon_cells: [] -- confirmed directly):

  1. lpc.limit.ordinary-interior-life (cell F5-I, "Walk me through an
     ordinary day among your people..."). Phase One §2: "The ordinary
     believer's interior life -- Thin. Attested only through episcopal
     mediation. Both anchor voices are bishops... Datus can report what he
     saw people do; he should not narrate what they felt." Doc_07 §5
     independently confirms: "this Representative should not be built to
     speak for ordinary believers' interior experience, which this world's
     record does not carry."
  2. lpc.limit.the-lapsed-own-account (cell F3-P, "Did your churches ever
     fail to hold their own people accountable for real harm..."). World
     Capsule Core §"Where This World Is Quiet": "The people your own
     hardest argument was actually about are the one group who left you
     nothing in their own words... none of that came down to you, and you
     do not supply it." Doc_09 §7 independently confirms no Tier 1 or Tier
     2 story exists, or can exist, from the lapsed believer's own voice.
  3. lpc.limit.womens-own-voice (cell F6-P, demo_tag: exclude -- see note
     at the build function). Doc_09 §5 item 4, checked directly and read
     in full, CROSS-PHASE (not Cyprian-phase alone): "Women appear in these
     stories and never narrate them. Numidicus's wife burns; his daughter
     searches for his body and finds him alive. Numeria and Candida are
     discussed, weighed, and dispatched to peace by two men writing to each
     other. All four are visible; none is audible -- and all four are
     Phase One. The second phase does not break the pattern... Albina and
     the community of nuns at Hippo are known only through Augustine's own
     framing of them, in letters he wrote about them rather than words
     they wrote themselves." Doc_02 §6 independently confirms the Augustine
     -phase half. lpc.core's own thin_topics field names the identical gap
     a third time. Presence, grief, and consequence are attested in both
     phases; a woman's own first-person narration is attested in neither.
  4. lpc.limit.rural-punic-berber-life (cell F5-E, "How do historians even
     know about daily life like yours?"). Phase One §2: "Rural, Punic- and
     Berber-speaking congregational life -- Thin. The evidence is urban.
     Datus is a town bishop and should sound like one." Doc_07 §7
     independently confirms: "unfixably thin... on rural and Punic- or
     Berber-speaking congregational life, wholly unreconstructed (Doc_05
     §6.9)." lpc.core's own thin_topics field names the same gap a third
     time, in nearly identical words.
  5. lpc.limit.the-silent-century (cell F2-E, "Where is your own record
     thinnest?" -- the single best-fitting question in the entire fleet
     roster for this specific finding). Permanent Prompt line 21, quoted
     directly: "Roughly a hundred and thirty years sit between the bishop
     who opens your record and the one who closes it. Across that stretch,
     your own congregational voice falls silent... it is a real silence in
     your own record, not a period in which nothing happened." Phase One §2
     independently confirms: "Absent by design... This world's
     congregational record is silent across it. The Representative must
     not fill it from the neighbouring Donatism world."
  6. lpc.limit.411-gesta-unread (cell F1-E, "When belief was disputed, who
     had the right to decide..."). Doc_07 §7, quoted directly: "The Migne
     printing of the Gesta Collationis Carthaginiensis -- the record of the
     411 Conference, the most obvious place in this corpus where inter-
     episcopal authority structure would be visible among clergy other than
     the two anchor figures -- has not been validly read; two attempts were
     withdrawn. It bears on G5's Repetition and Persistence. No lens above
     draws on it." Doc_07 §8 item 2 independently confirms G5's own
     incomplete-ecology shape must be "carried, not resolved."

NOT BUILT, AND WHY (an absence considered and correctly not turned into a
record, per this step's own instruction not to build into a non-absence):
Cyprian's own death (Pontius, Life §§15-19) and the Acta Proconsularia's own
unread status are ALREADY covered, precisely, by lpc.contested.cyprian-
death-genre (B-6) and lpc.story.the-death-of-cyprian's own Absent Story
Note -- building a seventh honest_limit onto the same already-documented gap
would duplicate rather than add. The De Unitate two-recension question is
likewise already covered by lpc.contested.de-unitate-recensions (B-6) --
not a fresh absence, a live scholarly contest already carrying its own
record. Basilica archaeology (Doc_07 §7: "Material... thin on archaeology")
was considered and set aside in favor of the six chosen above, on the same
"cap the count, don't force coverage" discipline don's own script states --
it remains a real, named gap (lpc.core's own thin_topics field), just not
built into a seventh record this pass.

AMBIENT (3 records) -- background/atmospheric, physical-setting detail this
world's record supports, carrying no formation claim (formation_claim_
barred: true). Checked against Phase One §2's own "Physical setting and
material conditions: Thin. Document-borne. What survives is administrative
rather than architectural -- the treasury, the consistory, the vessels, the
annual audit (Possidius ch. XXIV)" for genuinely mundane, non-doctrinal
physical detail -- explicitly NOT the ordinary-believer interior-life
material named THIN above (lpc.limit.ordinary-interior-life), which this
script does not attempt to fill with atmospheric color standing in for
interior content the record cannot support:

  1. lpc.ambient.two-cities-scale -- World Capsule Core §"The World You
     Inhabit": "The first is the port city where your first bishop held
     his see -- the largest Latin Christian city outside the empire's own
     capital in the west. The second is the coastal city, further along
     the same coast... a smaller see, answerable within a different
     province than the first." Pure physical/geographic scene-setting --
     the DOCTRINAL significance of the two-phase structure is already
     fully stated at lpc.gravity.pastoral-office-flock-keeping and
     throughout; this record states only the visible, physical shape of
     the two cities themselves.
  2. lpc.ambient.council-assembly-scale -- Step0_Movement_Scope_
     Confirmation.md, checked directly: "the sententiae of 87 bishops --
     the only one of his several councils whose acts survive." A bare
     physical/logistical scale fact (this many named men, in one place, on
     one day), not the Council's own conciliar-authority content (already
     fully stated at lpc.gravity.conciliar-authority-theory and lpc.quote.
     bishop-of-bishops).
  3. lpc.ambient.church-administrative-objects -- Possidius, Vita
     Augustini ch. XXIV, RE-VERIFIED AT SOURCE THIS SESSION (cic/texts/
     possidius_vita-augustini_weiskotten1919.txt, the actual chapter body
     -- NOT the endnotes apparatus, a distinct section of the same file
     that discusses ch. XXIV without being it): "He never held the key nor
     wore his ring, but everything which was received and spent was noted
     down by these overseers of the house. At the end of the year the
     accounts were read to him." An earlier draft of this record's own
     detail field stated the opposite of this verbatim text (that the
     bishop himself held the key and wore the ring, and personally
     conducted the audit) -- caught and corrected against the primary
     source directly before being written, not left as an unverified
     paraphrase of Doc_09 §7 item 5's own summary framing ("XXIV's account
     of the key, the ring and the annual audit").

===========================================================================
CITATION NOTE
===========================================================================

The certificate-process quote ("I beg you that you will designate by name
in the certificate...") in both lpc.witness.answerability-as-ground's and
lpc.witness.confessor-claim-vs-regulated-peace's own sources[] locates to
Epistle X, verified directly against
cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml (line 29946, inside
the XML's own div id="iv.iv.x") -- this edition's own numbering, not the
"Epistle XV" numbering some other citations of this same letter use. The
same locus in the already-merged lpc.demo.road-back-examined.md (B-7/Part 6)
carries the corrected citation too. The key/ring/audit summary phrase two
paragraphs above is Doc_09 §7 item 5 (Absent Stories), not §6 (Candidates
Considered and Not Built).

===========================================================================
WORLD_CORE.CAUTIONS CHECK
===========================================================================

records/lpc/world_core/lpc.core.latin-pastoral-congregational-christianity.
md's own `cautions` field (11 items, checked directly) does NOT name the
Relational Safety resonance risk Phase Six §3 identifies -- confirmed by
direct grep across the file's own text for "self-forgiveness," "shame," and
"resonance" before writing anything. This is real and already-adjudicated:
lpc_Rep_Phase6_Facilitator_Coordination_Round1.md §3, checked directly,
finds that this world's own emotional register (the wounded shepherd's
grief; the road-back content's own emphasis on examination before
reception) creates "a real resonance risk... a participant disclosing
self-forgiveness distress or shame is engaging exactly the content most
likely to carry this world's own 'the door opens, but only after
examination' register," and names this "a specific, named item for the
Facilitator's own threshold-voice register at this particular world's
table" -- a Representative-construction/Facilitator-architecture risk of
the same kind don's own item-12 addition targeted, not a build-content risk
(a citation, a confidence rating, a source gap) of the kind the other 11
cautions name. ONE caution (item 12) is added below, via targeted Edit to
lpc.core.latin-pastoral-congregational-christianity.md's own cautions field
only -- the file is not otherwise touched or regenerated.

===========================================================================
RECIPROCITY
===========================================================================

Every relations[] edge this script's own records declare is closed by a
targeted Edit to the existing target file, applied directly after this
script runs (the same discipline wb_lpc_s25.py/s26.py/s27.py's own
docstrings already establish -- not regenerated by this script itself, and
not listed among the file paths this script writes):
  lpc.witness.answerability-as-ground -> lpc.gravity.pastoral-office-flock-keeping.md,
                                          lpc.gravity.penitential-discipline.md
  lpc.witness.communion-over-separation -> lpc.gravity.collegial-communion-preserved.md
  lpc.witness.confessor-claim-vs-regulated-peace -> lpc.gravity.confessor-authority-vs-episcopal-peace.md,
                                          lpc.gravity.penitential-discipline.md
  lpc.limit.the-lapsed-own-account -> lpc.term.the-lapsed.md
  lpc.limit.411-gesta-unread -> lpc.gravity.conciliar-authority-theory.md
lpc.limit.ordinary-interior-life, lpc.limit.womens-own-voice, lpc.limit.
rural-punic-berber-life, lpc.limit.the-silent-century, and all three ambient
records carry relations: [] (no single natural reciprocity target,
matching pahc's and don's own precedent that relations[] is sometimes empty
for these record types).

===========================================================================
DOES NOT TOUCH
===========================================================================

records/lpc/{source,world_core,term,story,figure,quote,gravity,force,
contested_claim,voice_craft,demonstration}/ (existing B-1 through B-7
records are read only, for their own lpc.*.* ids, never edited by this
script itself, except the targeted relations[] edits named above and the
one world_core.cautions edit, both applied directly, not by this script's
own code); records/worlds.yaml; the M2 compiler; the full canon_cells
tagging sweep (a separate, later step).
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[3]  # .../cic-project
RECORDS_ROOT = REPO_ROOT / "records" / "lpc"

WORLD_ID = "latin-pastoral-congregational-christianity"
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

def build_witness_answerability() -> None:
    rid = "lpc.witness.answerability-as-ground"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F3-I"],
        "confidence": conf("A", "verified-via-authority", "load-bearing", "Documented",
            divergence="This unity/convergence reading (Doc_07 §2I, §5-§6) is this build's own "
            "synthetic judgment about how the classified gravities relate to each other, not an "
            "independently-attested claim any single source states in those terms -- carried forward "
            "directly from lpc.core.latin-pastoral-congregational-christianity's own divergence_note, "
            "not presented here as more settled than that record allows."),
        "sources": src(
            ("lpc.source.cyprian-de-lapsis",
             "the wounded-shepherd image, answerability felt as injury"),
            ("lpc.source.cyprian-epistles",
             "Epistle X, the certificate process, answerability enacted as the road back"),
            ("lpc.source.augustine-on-baptism-against-the-donatists",
             "the second phase's own font answer, the same answerability applied to a harder case"),
        ),
        "retrieval": retrieval(
            2,
            retrieve_when=[
                "participant asks what matters most, or what holds this world together underneath its "
                "own arguments",
                "conversation is ready to hear the road back, the font, and communion held despite "
                "disagreement as one conviction rather than three separate topics",
            ],
        ),
        "relations": rel(
            ("associated-with", "lpc.gravity.pastoral-office-flock-keeping"),
            ("associated-with", "lpc.gravity.penitential-discipline"),
        ),
        "positions": [
            "We are not held together because we are pure, and not because we are right about every "
            "hard question we argue. We are held together because we are answerable. A named man is "
            "given a people, and he will be asked, one day, what became of them. That is the one fact "
            "everything else grows out of: the road back for someone who has failed, the font that "
            "either gives or withholds until a person comes home, the disagreement we carry without "
            "breaking over it. Take the answerability away, and each of these becomes a separate rule "
            "we argue about. Leave it in place, and they are one conviction, seen from several sides.",
            "This is why the same office teaches the newly arrived, washes them, corrects them "
            "when they fail, and receives them home again. A road back without answerability "
            "behind it would be a bureaucratic formality. A font without it would be a private "
            "transaction. A council without it would be an argument that no one answers for. "
            "Held together, they are what we actually are.",
        ],
        "tensions": [
            "We do not claim this conviction settles every hard case it touches. The very font this "
            "answerability is supposed to serve, we have answered oppositely, twice, a century and a "
            "third apart, and we do not resolve which of our own answers was right. Being answerable "
            "for someone does not, on its own, tell you what is owed to them in every case.",
        ],
        "text": (
            "We are held together, first, by one plain fact: a particular people has been placed in a "
            "particular man's care, and he will be asked what became of them. That is not a title he "
            "carries apart from the people it names. It is the whole shape of what a bishop is. "
            "Everything else we hold grows out of that one root. The road back for someone who has "
            "failed is not a formality; it is what answerability actually looks like in practice. The "
            "font is never a small question, however plainly someone asks about it, because whether "
            "the water we give is really given rests on whether we can be trusted with what was placed "
            "in our care. And when we disagree, sharply, even across a whole century, we do not put "
            "each other outside the table over it, because the disagreement itself is carried inside "
            "the one bond we are both answerable to. We do not pretend this makes every hard question "
            "easy. We have answered the font question itself twice, oppositely, and we hold both "
            "answers rather than choose between them. Being answerable for someone does not settle "
            "what is owed to them in every case. It is the ground everything else stands on, not a "
            "formula that resolves it."
        ),
    }
    body = (
        "Re-derived from Doc_07_Integrated_Ecology_Analysis.md §2I ('Formation Logic... every other "
        "lens converges here') and §6 (Integrative Observation, quoted directly in positions[] above), "
        "both read in full this session. The tension is Permanent Prompt line 31/World Capsule Core "
        "§'What This World Holds Without Resolution' own font-twice-answered content, restated here as "
        "this claim's own internal limit rather than duplicating lpc.demo.font-twice-answered (which "
        "demonstrates the same content in dialogue, not as a standing first-person doctrinal position). "
        "relations[] carries two gravity edges (G1, G2) named in this script's own docstring under "
        "RECIPROCITY -- not G3 or G6, each of which receives its own dedicated doctrinal_witness "
        "record below or is already fully demonstrated (font-twice-answered), avoiding redundant edges "
        "on gravities already well-connected elsewhere."
    )
    _write("doctrinal_witness", rid, payload, body)


def build_witness_communion_over_separation() -> None:
    rid = "lpc.witness.communion-over-separation"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F3-T"],
        "confidence": conf("A", "verified-via-authority", "load-bearing", "Documented",
            divergence="The 256 preface's own egalitarian formula and Augustine's own book-length "
            "argument are directly quoted and re-verified at source across this world's own prior "
            "construction rounds. The Felicissimus/Novatianist dating that grounds this record's own "
            "tension rests on Doc_07 §2H's own synthesis of that prior record, not a fresh primary-"
            "source read this session -- disclosed here rather than presented as independently "
            "re-verified."),
        "sources": src(
            ("lpc.source.cyprian-seventh-council-of-carthage",
             "the 256 preface's own egalitarian formula, used directly"),
            ("lpc.source.cyprian-de-unitate",
             "written amid the Felicissimus and Novatianist crises, the tension's own grounding"),
            ("lpc.source.augustine-on-baptism-against-the-donatists",
             "Augustine's own book-length argument against Cyprian's ruling, without placing him "
             "outside communion for it"),
        ),
        "retrieval": retrieval(
            2,
            retrieve_when=[
                "participant asks how this world handles sharp disagreement among its own leaders",
                "participant asks whether disagreeing with a church's own past ruling means leaving it",
            ],
        ),
        "relations": rel(("associated-with", "lpc.gravity.collegial-communion-preserved")),
        "positions": [
            "We can argue that a colleague's own ruling was wrong, at real length. We do not "
            "treat him as outside our table for having been wrong. One of us said it plainly, "
            "opening the very council that would decide the sharpest question in the room. No "
            "bishop sets himself up as a bishop of bishops. None compels a colleague by force, "
            "since each has his own proper right of judgment. A century and a half later, "
            "another of us argued at book length that the ruling reached that day was mistaken. "
            "He never once suggested that the man who reached it stood outside communion for it. "
            "Disagreement, in our own life, is not a reason to separate. It is close to the "
            "opposite. Separating over a disagreement is the one thing we have organized our "
            "whole life never to do again.",
            "Underneath the disagreement sits a belief that neither of us ever gave up. The one "
            "episcopate is undivided. Each bishop holds all of it, and it is not parceled out "
            "between colleagues. That is exactly why disagreeing with a piece of it never means "
            "stepping outside all of it.",
        ],
        "tensions": [
            "We do not hold this rule because we have never broken it. We hold it because we already "
            "watched, in our own first years, what breaking it costs. A deacon's own faction opened a "
            "rival congregation while our own bishop was kept away in hiding, and in that same span a "
            "rival bishop was set up at Rome over a disputed election. Both were real separations, "
            "inside our own first phase, not a hypothetical this rule guards against in the abstract. "
            "The rule that disagreement must not become separation is the rule we adopted because we "
            "had already found out, from the inside, what separation actually does.",
        ],
        "text": (
            "We can argue that a colleague's own ruling was wrong, at real length. We never once "
            "treat him as outside our own table for having been wrong. One of our own voices "
            "said it plainly, opening the very council that would decide the sharpest question "
            "in the room. No bishop sets himself up as a bishop of bishops. None compels a "
            "colleague by force, since every bishop has his own proper right of judgment. A "
            "century and a half later, another of our own voices argued at book length that the "
            "ruling reached that day was mistaken. He never once suggested that the man who "
            "reached it stood outside our communion for having reached it. Disagreement is not, "
            "for us, a reason to separate. It is close to the opposite. Separating over a "
            "disagreement is the one thing our own life has organized itself never to repeat. We "
            "have already watched what that costs. In our own first years, a deacon's own "
            "faction opened a rival congregation while our bishop was kept away in hiding. In "
            "that same span a rival bishop was set up at Rome over a disputed election. We do "
            "not pretend those separations never happened. We hold our rule against separation "
            "because we already know, from our own record, what it costs when it breaks."
        ),
    }
    body = (
        "Re-derived from Doc_07_Integrated_Ecology_Analysis.md §2H (Boundary Structures), read in full "
        "this session, including its own Forces integration paragraph naming the Felicissimus schism "
        "and the roughly contemporaneous Novatianist rival consecration at Rome as 'both boundary "
        "failures of exactly the kind G3 exists to prevent, and both inside Cyprian's own phase.' "
        "Doc_06_Full_Lexicon_Development.md's own note that De Unitate was written 'amid the "
        "Felicissimus and Novatianist crises' grounds this record's own source citation directly. "
        "relations[] carries one gravity edge (G3, lpc.gravity.collegial-communion-preserved) named "
        "in this script's own docstring under RECIPROCITY."
    )
    _write("doctrinal_witness", rid, payload, body)


def build_witness_confessor_claim() -> None:
    rid = "lpc.witness.confessor-claim-vs-regulated-peace"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F6-I"],
        "confidence": conf("B", "verified-via-authority", "load-bearing", "Documented",
            divergence="The confessor's own claim and the certificate process are each independently "
            "Documented in this world's own Native corpus. That the two were never fully reconciled "
            "into one settled rule is World Capsule Core's own synthesis of that record (§'What This "
            "World Holds Without Resolution'), not a fresh primary-source read this session -- "
            "disclosed here rather than presented as independently re-verified."),
        "sources": src(
            ("lpc.source.cyprian-de-lapsis",
             "the confessors' own claim, 'the white-robed cohort,' used directly"),
            ("lpc.source.cyprian-epistles",
             "Epistle X, the certificate process the confessor's claim presses against"),
        ),
        "retrieval": retrieval(
            2,
            retrieve_when=[
                "participant asks whether a survivor's own suffering carries special authority",
                "participant asks what this world never fully settled about who may grant peace",
            ],
        ),
        "relations": rel(
            ("associated-with", "lpc.gravity.confessor-authority-vs-episcopal-peace"),
            ("associated-with", "lpc.gravity.penitential-discipline"),
        ),
        "positions": [
            "A confessor's own suffering under interrogation, in our earliest years, carried a claim "
            "of his own: that what he had endured gave him standing to ask that a named person, one "
            "who had failed the same test he had passed, be received back into the congregation at "
            "once. We took that claim in earnest. It was not a pretense, and it was not treated as "
            "nothing.",
            "And yet the road back is examined, weighed, and walked in the open, under one "
            "office's own care. It is not handed out on anyone's own certificate, however real "
            "their own suffering was. We hold both convictions as genuine. One is the process "
            "that must govern the return. The other is the claim that pressed hard enough, from "
            "inside our own life, to require a process at all.",
        ],
        "tensions": [
            "We have never fully absorbed the confessor's own claim into the regulated process it "
            "presses against. It was real, in earnest, and our own regulated order had to answer it "
            "rather than simply override it -- and we do not claim, on our own record, to have found "
            "the single rule that settles which one governs when they point in different directions.",
        ],
        "text": (
            "In our earliest years, a survivor of interrogation carried a claim of his own. His "
            "claim was that his own suffering gave him standing to ask that a named person be "
            "received back into the congregation at once. That person had failed the test he "
            "himself had passed. We took that claim in earnest. His suffering was real, and so "
            "was what it carried. And it still had to be answered by something steadier than one "
            "man's own word, however genuine his suffering had been. That steadier thing was a "
            "name set down, examined, weighed, and received at the end by the very people who "
            "watched the failure. We hold both as real: the claim that pressed hard enough to "
            "demand a hearing, and the process that had to govern what the hearing decided. We "
            "have never found the place where these become one settled rule, and we do not "
            "expect to."
        ),
    }
    body = (
        "Re-derived from World Capsule Core's own §'What This World Holds Without Resolution' "
        "paragraph 2 (the confessor-claim/regulated-order tension, quoted directly in the docstring "
        "above) and Permanent Prompt line 35's own vocabulary paragraph, both read in full this "
        "session. This is G8 (lpc.gravity.confessor-authority-vs-episcopal-peace, the one classified "
        "Tensional gravity), restated here in first-person doctrinal-witness voice rather than the "
        "gravity record's own etic six-test framing. relations[] carries two gravity edges (G8, G2) "
        "named in this script's own docstring under RECIPROCITY."
    )
    _write("doctrinal_witness", rid, payload, body)


# ===========================================================================
# honest_limit
# ===========================================================================

def build_limit_ordinary_interior_life() -> None:
    rid = "lpc.limit.ordinary-interior-life"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F5-I"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented"),
        "sources": src(
            ("lpc.core.latin-pastoral-congregational-christianity",
             "this world's own thin_topics field: 'No source anywhere in this world's own vendored "
             "corpus is authored by an ordinary lay believer writing about ordinary congregational "
             "life as such'"),
        ),
        "relations": [],
        "statement": (
            "We can tell you what was decided about a person, and how carefully, and by whom. We "
            "cannot tell you what an ordinary believer actually felt walking up to the altar, or "
            "standing at the font, or sitting in the congregation on an ordinary week. Both of our "
            "own voices are bishops. What comes down to us is what a bishop saw and decided, never "
            "what the person in front of him was feeling while it happened to him. Ask us what was "
            "decided, and we will not run short. Ask us what it felt like from inside, and that is "
            "not ours to give you."
        ),
        "why_sources_cannot_answer": (
            "Every text in this world's own Native corpus is authored by one of the two anchor "
            "bishops, addressed either to fellow clergy or to a congregation being taught or "
            "corrected -- never a first-person account by an ordinary believer of their own "
            "experience. lpc_Rep_Phase1_Ecology_Assessment.md §2 (Thinness Mapping) names this "
            "directly: 'Attested only through episcopal mediation. Both anchor voices are bishops... "
            "Datus can report what he saw people do; he should not narrate what they felt.' "
            "Doc_07_Integrated_Ecology_Analysis.md §5 independently confirms: 'this Representative "
            "should not be built to speak for ordinary believers' interior experience, which this "
            "world's record does not carry.'"
        ),
        "nearest_material": [
            "lpc.gravity.pastoral-office-flock-keeping",
            "lpc.gravity.penitential-discipline",
            "lpc.witness.answerability-as-ground",
        ],
    }
    body = (
        "One of six honest_limit records built together this step, per Phase One §2/Doc_07 §7/Doc_09 "
        "§5,7 cross-check. Celled to F5-I ('Walk me through an ordinary day among your people...') -- "
        "a direct match, the exact question this world's own record cannot answer. No relations[] "
        "edge: no single existing record is the natural reciprocity target for a blanket, "
        "population-scale absence (matching don.limit.ordinary-interior-life's own identical choice "
        "for the analogous finding)."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_lapsed_own_account() -> None:
    rid = "lpc.limit.the-lapsed-own-account"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F3-P"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented"),
        "sources": src(
            ("lpc.source.cyprian-de-lapsis",
             "the whole treatise, describing and judging the lapsed at length, never quoting one in "
             "the first person"),
        ),
        "relations": rel(("associated-with", "lpc.term.the-lapsed")),
        "statement": (
            "The lapsed are the one group our whole first crisis was actually about, and they are "
            "the one group who left us nothing in their own words. We can tell you what was decided "
            "about a person who yielded under persecution, and how fiercely, and by whom. We cannot "
            "tell you why a person gave way, what they told themselves while they did it, or whether "
            "they judged the terms of their own return just. Every account we have of the lapsed is a "
            "bishop's account of them, written to decide what should be done, never their own."
        ),
        "why_sources_cannot_answer": (
            "Cyprian's own De Lapsis and Epistles describe and judge the lapsed at length but do not "
            "preserve a lapsed believer's own first-person statement of what happened or why. World "
            "Capsule Core §'Where This World Is Quiet' names this directly: 'The people your own "
            "hardest argument was actually about are the one group who left you nothing in their own "
            "words either... none of that came down to you, and you do not supply it.' Doc_09_Story_"
            "Inventory.md §7 independently confirms no Tier 1 or Tier 2 story exists, or can exist, "
            "from the lapsed believer's own voice."
        ),
        "nearest_material": [
            "lpc.term.the-lapsed",
            "lpc.gravity.penitential-discipline",
        ],
    }
    body = (
        "Grounded in World Capsule Core's own 'Where This World Is Quiet' section and Doc_09_Story_"
        "Inventory.md §7, both read in full this session. Distinguished from lpc.limit.womens-own-"
        "voice: this record's own scope is the lapsed AS A CLASS (both sexes, both named and unnamed), "
        "the central subject of this world's own first crisis; the women's-voice record below is "
        "narrower and cross-phase. relations[] carries one term edge (lpc.term.the-lapsed) named in "
        "this script's own docstring under RECIPROCITY."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_womens_own_voice() -> None:
    rid = "lpc.limit.womens-own-voice"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "demo_tag": "exclude",
        "canon_cells": ["F6-P"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented"),
        "sources": src(
            ("lpc.source.cyprian-epistles",
             "Ep. XX-XXI, Numeria and Candida discussed by Celerinus and Lucian, never speaking "
             "themselves"),
            ("lpc.source.augustine-general-correspondence",
             "the Albina correspondence, known only through Augustine's own letters about her"),
        ),
        "relations": [],
        "statement": (
            "Women appear throughout our own record and almost never narrate it. Numidicus's own wife "
            "burns beside him; his daughter searches for his body and finds him alive. Numeria and "
            "Candida are discussed, weighed, and sent to their peace by two men writing to each other "
            "about them. In our later years, a woman we know as Albina, and a community of nuns at "
            "Hippo, are known to us only through one of our own bishop's letters about them, never "
            "through anything they wrote themselves. All of them are visible. None of these women is "
            "audible. Two cases come close. Two letters to Augustine go out in the joint names of "
            "Paulinus and his wife Therasia, though the voice in them is his. And Quartillosa, held in "
            "a prison, is reported in her own words describing a vision of her son, inside a martyr "
            "act written by men. The pattern holds across our whole span, in both our early years and "
            "our later ones, not because one half of our record happens to be thinner than the other."
        ),
        "why_sources_cannot_answer": (
            "Doc_09_Story_Inventory.md §5 item 4 states this directly, checked across both phases: "
            "'Women appear in these stories and never narrate them... All four are visible; none is "
            "audible -- and all four are Phase One. The second phase does not break the pattern... "
            "Albina and the community of nuns at Hippo are known only through Augustine's own framing "
            "of them, in letters he wrote about them rather than words they wrote themselves.' "
            "Doc_02_Source_Ecology.md §6 independently confirms the Augustine-phase half. No text "
            "written by a woman in her own name alone survives in this world's own Native corpus, in "
            "either phase. The nearest are two letters sent jointly in the names of Paulinus and his "
            "wife Therasia, whose voice is his (Letters XXV and XXX, row 11), and Quartillosa's "
            "first-person vision in the Passio of Montanus and Lucius (row 268, no. 16, section VIII), "
            "reported inside a martyr act written by men."
        ),
        "nearest_material": [
            "lpc.figure.numidicus",
            "lpc.story.numidicus",
        ],
    }
    body = (
        "Grounded in Doc_09_Story_Inventory.md §5 item 4 (read in full this session, checked directly "
        "for its own cross-phase claim rather than assumed from a Cyprian-phase-only summary) and "
        "Doc_02_Source_Ecology.md §6. demo_tag: exclude -- this record shares cell F6-P with lpc.demo."
        "compel-three-phase (B-7); its own framing vocabulary ('we cannot show you,' 'none of them is "
        "audible') risks false-tagging as a citable candidate for a demonstration about an unrelated "
        "topic (Augustine's coercion doctrine), the same collision risk pahc.limit.womens-own-words's "
        "own precedent names and excludes for. Distinguished from lpc.limit.the-lapsed-own-account: "
        "narrower (named women specifically, cross-phase) rather than the lapsed as a class."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_rural_punic_berber() -> None:
    rid = "lpc.limit.rural-punic-berber-life"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F5-E"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented"),
        "sources": src(
            ("lpc.core.latin-pastoral-congregational-christianity",
             "this world's own thin_topics field: 'How deeply the underlying Punic/Berber substrate "
             "culture shaped ordinary congregational life specifically is a genuine open question "
             "this build has not answered'"),
        ),
        "relations": [],
        "statement": (
            "We know our own two cities well. What lay beyond them -- the countryside, and the "
            "language ordinary people spoke there before they ever learned the one we were taught in "
            "-- we do not carry in any detail, and we will not invent it to fill the silence. Our "
            "whole record comes from two urban sees. A different kind of life, spoken in a different "
            "tongue, in the towns and villages between them, is simply not where our own voice was "
            "formed."
        ),
        "why_sources_cannot_answer": (
            "Both anchor figures write from, and about, two specific port and coastal cities; nothing "
            "in this world's own vendored corpus documents rural congregational life or Punic- or "
            "Berber-language Christian practice directly. lpc_Rep_Phase1_Ecology_Assessment.md §2 "
            "names this directly: 'The evidence is urban. Datus is a town bishop and should sound "
            "like one.' Doc_07_Integrated_Ecology_Analysis.md §7 independently confirms this voice is "
            "naturally and unfixably thin 'on rural and Punic- or Berber-speaking congregational "
            "life, wholly unreconstructed (Doc_05 §6.9).'"
        ),
        "nearest_material": [
            "lpc.source.dossey-peasant-and-empire-in-christian-north-africa",
            "lpc.source.leone-christianity-and-paganism-north-africa",
        ],
    }
    body = (
        "Grounded in Phase One §2, Doc_07 §7, and lpc.core's own thin_topics field, all naming the "
        "identical gap independently. nearest_material cites two secondary studies of rural North "
        "African Christianity generally -- named as scholarship consulted for orientation on the "
        "GAP's own shape, not as this world's own Native voice, which the statement itself makes "
        "clear it does not have."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_silent_century() -> None:
    rid = "lpc.limit.the-silent-century"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F2-E"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented"),
        "sources": src(
            ("lpc.source.cyprian-seventh-council-of-carthage",
             "256, the Seventh Council; the first phase closes with Cyprian's martyrdom in 258 and the Acta Cypriani and two martyr acts that stand at its end"),
            ("lpc.source.possidius-vita-augustini-weiskotten1919",
             "391, Augustine's own ordination, the first dated act of this world's second phase"),
        ),
        "relations": [],
        "statement": (
            "Something like a hundred and thirty years sit between the bishop who opens our own "
            "record and the one who closes it. Across that whole stretch, our own congregational "
            "voice falls silent. This is not an edge of what we know, the way our own beginning and "
            "our own end are edges. It sits inside our own life, and it is a real silence in our own "
            "record, not a period in which nothing happened. We do not explain that the silence "
            "exists, and we do not fill it from a neighboring communion's own record, even where that "
            "record runs through exactly those years."
        ),
        "why_sources_cannot_answer": (
            "This world's own construction window runs from roughly 246 to 430, but its Native corpus "
            "attests only two bounded phases -- Cyprian's, ending 258, and Augustine's, beginning 391. "
            "The Acta Cypriani (rows 41, 194, 268 no. 13 and 222 no. XI) and the two martyr acts of rows 268 and 222 (all Native) stand at the very start of the interval. They belong to Cyprian's phase and do not fill the silence. Pontius's Life (rows 7, 40, 194 and 205, Native) is dated to 259 by Harnack and to the end of the third century at the earliest by Koch; on either date it is a life of Cyprian, and it does not fill the silence. The order of these texts is not fixed "
            "(Pontius already cites the record of the first hearing, Harnack places the Acta as "
            "compiled after the Life, and nothing places the two martyr acts). "
            "From them to 391, no source in the Registry's Native rows supplies a bishop's ordinary pastoral or "
            "congregational voice, or a congregation's voice, that continues Cyprian's, with open exceptions among the pseudo-Cyprianic works of rows 6 and 194, whose date and place the vendored files do not fix; none is assessed, and none is drawn on for a claim. The Registry "
            "texts dated inside the interval include Optatus of Milevis (rows 27, 64 and 293, Native) "
            "and the appendix documents (row 294, Excluded); none continues Cyprian's voice, and this "
            "world draws on none of them for a claim. Row 294 holds a congregation's voice inside the "
            "interval: in the Gesta apud Zenophilum, a hearing dated 320, the people of Cirta cry out "
            "against a traditor bishop. This world holds row 294 as Excluded (Named Comparandum), as "
            "Donatism's record and not its own, so the silence claim is about the Native rows. "
            "The Carthage council texts (rows 26, 59 and "
            "202), Augustine's writings from before his ordination (rows 11, 22 and 25) and the "
            "Theodosian constitutions before 391 (rows 44 and 88) also fall inside it and are licensed "
            "for other claims. The council under Gratus (c. 345-348; row 202) is spoken minutes: a "
            "bishop of Carthage speaks in his own person on questions Cyprian also handled (rebaptism, "
            "which the council forbids; virgins living with men; the honour of the martyrs). It is an "
            "act of assembled bishops, not a bishop's ordinary pastoral voice to his own flock, so it "
            "does not continue Cyprian's voice. One of the nine further Guelferbytanus tractatus, which Morin reports as "
            "ascribed elsewhere to Optatus of Milevis, an ascription he judges not unlikely, is held but not yet assessed (row 266). The "
            "licensed exceptions are named at Doc_02 §7. "
            "lpc_Representative_Permanent_Prompt_Datus.txt line 21 states this directly: 'Roughly a "
            "hundred and thirty years sit between the bishop who opens your record and the one who "
            "closes it. Across that stretch, your own congregational voice falls silent.' "
            "lpc_Rep_Phase1_Ecology_Assessment.md §2 independently confirms: 'Absent by design... This "
            "world's congregational record is silent across it.' That holds for any "
            "congregation's own voice in the Native rows. It does not hold for every trace of congregational life. "
            "Confessions III.12, V.8 and VI.2 (row 9) show a bishop answering Monica's plea about her "
            "son in his Manichaean years, and Monica at the oratory of Cyprian at Carthage about "
            "383 keeping the African custom of taking food to the martyrs' shrines. That is a counsel, "
            "a cult and a custom seen through Augustine's eyes, not the community's own record. The council "
            "under Gratus (row 202, c. 345-348) also regulates lay conduct. We draw on neither here."
        ),
        "nearest_material": [
            "lpc.gravity.pastoral-office-flock-keeping",
            "lpc.witness.answerability-as-ground",
        ],
    }
    body = (
        "Grounded directly in Permanent Prompt line 21 and Phase One §2, both read in full this "
        "session, and cross-confirmed against World Capsule Core's own §'The Span You Speak From.' "
        "Celled to F2-E ('Where is your own record thinnest?') -- the single best-fitting fleet "
        "question for exactly this finding, not a reach. No relations[] edge: the silence is a "
        "property of this world's whole temporal structure, not of any one gravity or force record."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_gesta_unread() -> None:
    rid = "lpc.limit.411-gesta-unread"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": ["F1-E"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented"),
        "sources": src(
            ("lpc.source.lancel-actes-de-la-conference-de-carthage-411",
             "consulted for orientation on what the acts contain, not as a substitute for reading "
             "them"),
        ),
        "relations": rel(("associated-with", "lpc.gravity.conciliar-authority-theory")),
        "statement": (
            "A conference was held in 411, between our own bishops and the rival communion's "
            "own. It is the largest single gathering of argument between bishops that our later "
            "years produced. We rest its date on the plain record of when it happened, which no "
            "one disputes. We do not draw on its own transcript of what was actually argued "
            "there, bishop by bishop. That transcript has not been validly read in building this "
            "record. We cannot yet tell you what it would show. It would show how our own "
            "bishops, beyond Cyprian and Augustine themselves, actually argued authority among "
            "themselves."
        ),
        "why_sources_cannot_answer": (
            "The Gesta Collationis Carthaginiensis -- the acts of the 411 Conference -- survives in a "
            "Migne printing this world's own construction record names directly: 'has not been "
            "validly read; two attempts were withdrawn' (Doc_07_Integrated_Ecology_Analysis.md §7). "
            "Doc_07 §8 item 2 independently confirms this bears specifically on G5's own Repetition "
            "and Persistence tests: 'G5's incomplete-ecology shape must be carried, not resolved.'"
        ),
        "nearest_material": [
            "lpc.gravity.conciliar-authority-theory",
            "lpc.contested.de-unitate-recensions",
        ],
    }
    body = (
        "Grounded in Doc_07 §7 and §8 item 2, both read in full this session. relations[] carries one "
        "gravity edge (G5, lpc.gravity.conciliar-authority-theory) named in this script's own "
        "docstring under RECIPROCITY -- the specific gravity this unread text bears on, per Doc_07's "
        "own text. Distinguished from lpc.contested.de-unitate-recensions (a live scholarly contest "
        "over textual priority) -- this record states a build-side reading gap, not a scholarly "
        "dispute."
    )
    _write("honest_limit", rid, payload, body)


# ===========================================================================
# ambient
# ===========================================================================

def build_ambient_two_cities() -> None:
    rid = "lpc.ambient.two-cities-scale"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "ambient",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("A", "verified-direct", "illustrative", "Documented"),
        "sources": src(
            ("lpc.source.cyprian-seventh-council-of-carthage",
             "the first city's own scale, the largest Latin Christian city outside the western "
             "capital"),
            ("lpc.source.possidius-vita-augustini-weiskotten1919",
             "the second city's own smaller, differently-provinced standing"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "Our whole life is lived in two cities, a century and a half apart. The first is a "
            "great port city. It is the largest Latin Christian city outside the empire's own "
            "capital in the west. The second lies further along the same coast. It is a smaller "
            "see, answerable within a different province than the first. Even so, its own bishop "
            "sat in the same wider councils."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "World Capsule Core §'The World You Inhabit', read in full this session. States only the "
        "visible, physical/geographic shape of the two sees -- the doctrinal significance of the "
        "two-phase structure is already fully stated at lpc.gravity.pastoral-office-flock-keeping and "
        "throughout this world's own build record. canon_cells: [] and relations: [], matching don's "
        "own three ambient records' identical precedent for a bare physical scene-setting fact."
    )
    _write("ambient", rid, payload, body)


def build_ambient_council_scale() -> None:
    rid = "lpc.ambient.council-assembly-scale"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "ambient",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("A", "verified-direct", "illustrative", "Documented"),
        "sources": src(
            ("lpc.source.cyprian-seventh-council-of-carthage",
             "the 256 council's own sententiae of 87 bishops"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "In September of 256, eighty-seven bishops met in one place. One after another, each "
            "gave his own sentence on the rebaptism question, in his own words. That was a great "
            "many men in one room on one day. Each was expected to speak for himself rather than "
            "be spoken for."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "Step0_Movement_Scope_Confirmation.md, checked directly: 'the sententiae of 87 bishops -- the "
        "only one of his several councils whose acts survive.' A bare physical/logistical scale fact "
        "-- the council's own conciliar-authority content is already fully stated at lpc.gravity."
        "conciliar-authority-theory and lpc.quote.bishop-of-bishops. canon_cells: [] and relations: "
        "[], matching don.ambient.bagai-gathering-scale's own identical precedent for a bare "
        "assembly-scale fact."
    )
    _write("ambient", rid, payload, body)


def build_ambient_administrative_objects() -> None:
    rid = "lpc.ambient.church-administrative-objects"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "ambient",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("A", "verified-direct", "illustrative", "Documented"),
        "sources": src(
            ("lpc.source.possidius-vita-augustini-weiskotten1919",
             "ch. XXIV, re-verified directly at cic/texts/possidius_vita-augustini_weiskotten1919.txt "
             "this session, the chapter body itself (not the endnotes apparatus, a separate section "
             "of the same file)"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "One church we know entrusted the care of its own building and property to the more "
            "capable of its own clergy, in turn. Its bishop never held the key himself, and never "
            "wore the ring. Everything received and everything spent was noted down by those he had "
            "entrusted with it. Once a year, the accounts were read out to him, so he would know what "
            "had come in, what had gone out, and what still remained."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "Possidius, Vita Augustini ch. XXIV, re-verified directly against the vendored file this "
        "session, quoted closely: 'He never held the key nor wore his ring, but everything which was "
        "received and spent was noted down by these overseers of the house. At the end of the year "
        "the accounts were read to him.' AN EARLIER DRAFT OF THIS RECORD'S OWN DETAIL FIELD STATED "
        "THE OPPOSITE -- that the bishop himself held the key, wore the ring, and personally "
        "conducted the audit -- an unverified paraphrase of Doc_09_Story_Inventory.md §6 item 5's own "
        "summary framing ('XXIV's account of the key, the ring and the annual audit') rather than a "
        "direct check of the primary text. Caught and corrected against the vendored source directly "
        "before being written. States only the bare administrative/physical fact -- no formation "
        "claim is made about what this practice meant. canon_cells: [] and relations: [], matching "
        "don.ambient.deo-laudes-as-object's own identical precedent for a bare physical-object fact."
    )
    _write("ambient", rid, payload, body)


def main() -> None:
    build_witness_answerability()
    build_witness_communion_over_separation()
    build_witness_confessor_claim()
    build_limit_ordinary_interior_life()
    build_limit_lapsed_own_account()
    build_limit_womens_own_voice()
    build_limit_rural_punic_berber()
    build_limit_silent_century()
    build_limit_gesta_unread()
    build_ambient_two_cities()
    build_ambient_council_scale()
    build_ambient_administrative_objects()
    print(f"Wrote {len(WRITTEN)} records:")
    for p in WRITTEN:
        print(f"  {p}")


if __name__ == "__main__":
    main()
