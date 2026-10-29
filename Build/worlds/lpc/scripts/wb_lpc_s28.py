"""Latin Pastoral-Congregational Christianity (`lpc`): doctrinal_witness, honest_limit and
ambient records.

Builds the 3 doctrinal_witness, 6 honest_limit and 3 ambient records, under
records/lpc/doctrinal_witness/, records/lpc/honest_limit/ and records/lpc/ambient/.

SCHEMA AND GATES. doctrinal_witness = {text: str, positions: [str], tensions: [str]};
honest_limit = {statement: str, why_sources_cannot_answer: str, nearest_material: [str]};
ambient = {detail: str, formation_claim_barred: {const: True}}
(engine/m1/schemas.py TYPE_PROPERTIES; all three are in COMPLETION_REQUIRED in
engine/m1/gates.py with exactly those fields required). In engine/m1/spoken_fields.py,
doctrinal_witness.text and honest_limit.statement are scanned by both
gate_no_build_attribution and gate_voice_perspective, and ambient.detail is scanned by
perspective only. Every field is therefore written in first-person "we/our" register, with
none of the outside-vantage "this world" phrasing.

CANON COVERAGE. gate_canon_coverage (engine/m1/canon.py) requires each of the fleet's 28
canon cells to carry either at least one substantive record (doctrinal_witness, term,
story or quote; demonstration, gravity and force do not count) or exactly one
honest_limit. A cell never carries more than one honest_limit. The six honest_limit
records below sit in six different cells, and no other lpc honest_limit exists. These
records and the doctrinal_witness records set canon_cells; ten cells are touched in total
(3 by doctrinal_witness, 6 by honest_limit, with overlap stated at each record). The ambient
records carry canon_cells: [] and relations: [], as don's ambient records do.

HOUSE STYLE (from records/pahc/doctrinal_witness/pahc.witness.apostolic-practice.md,
records/pahc/honest_limit/pahc.limit.womens-own-words.md, records/fix/ambient/
fix.ambient.daily-bread.md and records/don/ambient/don.ambient.*.md). A doctrinal_witness is
a text/positions/tensions triple in emic register, cited to real primary sources, with a
relation to a gravity or force and retrieval tier 2. An honest_limit is a
statement/why_sources_cannot_answer/nearest_material triple. It carries demo_tag: exclude
when its framing vocabulary would false-tag unrelated demonstration sentences in the same
canon cell (engine/m2/builders.py _demonstration_candidates() counts doctrinal_witness,
honest_limit, gravity, force, term, story, quote and contested_claim as demo candidates when
they share a cell with a demonstration and lack demo_tag: exclude). An ambient detail states
only the bare physical or social fact, and formation_claim_barred is true in every record.

===========================================================================
SOURCE MATERIAL, PER RECORD TYPE
===========================================================================

DOCTRINAL_WITNESS (3 records). Each states this world's doctrinal self-understanding in its
own voice. It differs from gravity (etic, six-test classification), contested_claim (etic, a
scholarly dispute) and demonstration (dialogue built around one canon_question). None
duplicates an existing lpc.gravity.*, lpc.contested.*, lpc.demo.* or lpc.term.* record.

  1. lpc.witness.answerability-as-ground. Doc_07 §2I (Formation Logic, "applied after all
     other lenses... every other lens converges here") and §6 (Integrative Observation: "The
     conviction underneath everything else here is not that the church is pure, nor that it
     is right, but that it is answerable"). No existing lpc record states this unity claim in
     first-person voice. The lpc.gravity.* records classify G1, G2, G3 and G6 separately, and
     no demonstration takes the convergence as its subject. The world_core divergence_note
     says: "Doc_07 §2I's own convergence finding... is this build's own synthetic judgment,
     stated as such at Doc_07 §5, not a claim any single source states in those terms." This
     record's divergence_note carries that caveat.
  2. lpc.witness.communion-over-separation. Doc_07 §2H (Boundary Structures): "The internal
     rule is G3... Disagreement is expected; separation is the thing this world organizes
     itself to avoid". Its complication, from the same section: "the Felicissimus schism
     opening during Cyprian's own absence in hiding, and the roughly contemporaneous
     Novatianist rival consecration at Rome -- both boundary failures of exactly the kind G3
     exists to prevent, and both inside Cyprian's own phase." lpc.gravity.collegial-communion-
     preserved states the six-test classification (etic), not this world's first-person
     account of why the rule exists.
  3. lpc.witness.confessor-claim-vs-regulated-peace. G8, the one Tensional gravity
     (lpc.gravity.confessor-authority-vs-episcopal-peace), restated in first-person witness
     voice as a position and a tension. World Capsule Core's "What This World Holds Without
     Resolution" §2 says: "This world also holds a claim to grant peace that its own regulated
     order does not fully absorb... You hold both as genuine: the process that must govern,
     and the claim that pressed hard enough to require a process at all."

HONEST_LIMIT (6 records). Each is a "this world's record cannot speak to X" finding named in
at least two of lpc_Rep_Phase1_Ecology_Assessment.md §2 (Thinness Mapping),
Doc_07_Integrated_Ecology_Analysis.md §7 (Gaps and Limits), Doc_09_Story_Inventory.md §5
item 4 and §7 (Absent Stories), and the world_core thin_topics field. No existing lpc term,
story, quote or doctrinal_witness record covers any of them.

  1. lpc.limit.ordinary-interior-life (cell F5-I, "Walk me through an ordinary day among
     your people..."). Phase One §2: "The ordinary believer's interior life -- Thin.
     Attested only through episcopal mediation. Both anchor voices are bishops... Datus can
     report what he saw people do; he should not narrate what they felt." Doc_07 §5: "this
     Representative should not be built to speak for ordinary believers' interior
     experience, which this world's record does not carry."
  2. lpc.limit.the-lapsed-own-account (cell F3-P, "Did your churches ever fail to hold their
     own people accountable for real harm..."). World Capsule Core "Where This World Is
     Quiet": "The people your own hardest argument was actually about are the one group who
     left you nothing in their own words... none of that came down to you, and you do not
     supply it." Doc_09 §7 confirms that no Tier 1 or Tier 2 story exists, or can exist, from
     the lapsed believer's own voice.
  3. lpc.limit.womens-own-voice (cell F6-P, demo_tag: exclude; see the build function).
     Doc_09 §7 item 4, across both phases: "Women appear in these stories and never narrate
     them. Numidicus's wife burns; his daughter searches for his body and finds him alive.
     Numeria and Candida are discussed, weighed, and dispatched to peace by two men writing
     to each other. All four are visible; none is audible -- and all four are Phase One. The
     second phase does not break the pattern... Albina and the community of nuns at Hippo are
     known only through Augustine's own framing of them, in letters he wrote about them
     rather than words they wrote themselves." Doc_02 §6 confirms the Augustine-phase half,
     and the world_core thin_topics field names the same gap. Presence, grief and
     consequence are attested in both phases. No text a woman wrote herself survives in
     either phase. One woman's first-person account of a vision is reported in the Passio of
     Montanus and Lucius 8.
  4. lpc.limit.rural-punic-berber-life (cell F5-E, "How do historians even know about daily
     life like yours?"). Phase One §2: "Rural, Punic- and Berber-speaking congregational
     life -- Thin. The evidence is urban. Datus is a town bishop and should sound like one."
     Doc_07 §7: "unfixably thin... on rural and Punic- or Berber-speaking congregational
     life, wholly unreconstructed (Doc_05 §6.9)." The world_core thin_topics field names the
     same gap.
  5. lpc.limit.the-silent-century (cell F2-E, "Where is your own record thinnest?", the
     best-fitting question in the fleet roster for this finding). Permanent Prompt line 21:
     "Roughly a hundred and thirty years sit between the death of the bishop who opens your
     record and the ordination of the one who closes it. Across that stretch, your own ordinary
     pastoral voice falls silent... it is a silence in your own pastoral voice, not a period
     in which nothing happened." Phase
     One §2: "Absent by design... This world's congregational record is silent across it.
     The Representative must not fill it from the neighbouring Donatism world." The silence
     holds only for what this build has assessed. Nine tractatus in Morin 1917 are not yet
     assessed (OG-54), so the record's formation_confidence is Contested.
  6. lpc.limit.411-gesta-unread (cell F1-E, "When belief was disputed, who had the right to
     decide..."). Doc_07 §7: "The Migne printing of the Gesta Collationis Carthaginiensis --
     the record of the 411 Conference, the most obvious place in this corpus where
     inter-episcopal authority structure would be visible among clergy other than the two
     anchor figures -- has not been validly read; two attempts were withdrawn. It bears on
     G5's Repetition and Persistence. No lens above draws on it." Doc_07 §8 item 2: G5's
     incomplete-ecology shape must be "carried, not resolved."

NOT BUILT. Cyprian's death (Pontius, Life §§15-19) and the unread status of the Acta
Proconsularia are covered by lpc.contested.cyprian-death-genre and by the Absent Story Note
of lpc.story.the-death-of-cyprian, so a seventh honest_limit would repeat them. The De
Unitate two-recension question is covered by lpc.contested.de-unitate-recensions. Basilica
archaeology (Doc_07 §7: "Material... thin on archaeology") is a real, named gap in the
world_core thin_topics field. It has no record of its own, because the honest_limit count is
capped at six rather than forced to cover every gap, as in don.

AMBIENT (3 records). Each is physical-setting detail that this world's record supports and
that carries no formation claim (formation_claim_barred: true). Phase One §2 gives the
physical setting as "Thin. Document-borne. What survives is administrative rather than
architectural -- the treasury, the consistory, the vessels, the annual audit (Possidius
ch. XXIV)". The ambient records do not stand in for the ordinary-believer interior life
that lpc.limit.ordinary-interior-life says the record cannot support.

  1. lpc.ambient.two-cities-scale. World Capsule Core "The World You Inhabit": "The first
     is the port city where your first bishop held his see -- the largest Latin Christian
     city outside Rome. The second is the coastal city, further along the same coast... a smaller see, answerable within a different province
     than the first." This is geography only. The doctrinal significance of the two-phase
     structure is stated at lpc.gravity.pastoral-office-flock-keeping.
  2. lpc.ambient.council-assembly-scale. Step0_Movement_Scope_Confirmation.md: "the
     sententiae of 87 bishops -- the only one of his several councils whose acts survive."
     It is a bare scale fact (eighty-seven sentences, with presbyters, deacons and people
     present), not the
     Council's conciliar-authority content, which sits at lpc.gravity.conciliar-authority-
     theory and lpc.quote.bishop-of-bishops.
  3. lpc.ambient.church-administrative-objects. Possidius, Vita Augustini ch. XXIV
     (cic/texts/possidius_vita-augustini_weiskotten1919.txt, the chapter body and not the
     endnotes apparatus, a separate section of the same file): "He never held the key nor
     wore his ring, but everything which was received and spent was noted down by these
     overseers of the house. At the end of the year the accounts were read to him." The detail
     field follows this text and not the summary framing in Doc_09 §7 item 5 ("XXIV's account
     of the key, the ring and the annual audit").

===========================================================================
CITATION NOTE
===========================================================================

The certificate-process quote ("I beg you that you will designate by name in the
certificate...") in the sources[] of lpc.witness.answerability-as-ground and
lpc.witness.confessor-claim-vs-regulated-peace is Epistle X, in
cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml (line 29946, inside div
id="iv.iv.x"). That is this edition's numbering, not the "Epistle XV" that some other
citations of the same letter use. lpc.demo.road-back-examined cites it the same way. The
key, ring and audit phrase above is Doc_09 §7 item 5 (Absent Stories).

===========================================================================
RECIPROCITY
===========================================================================

Each relations[] edge below is mirrored on its target record:
  lpc.witness.answerability-as-ground -> lpc.gravity.pastoral-office-flock-keeping.md,
                                          lpc.gravity.penitential-discipline.md
  lpc.witness.communion-over-separation -> lpc.gravity.collegial-communion-preserved.md
  lpc.witness.confessor-claim-vs-regulated-peace -> lpc.gravity.confessor-authority-vs-episcopal-peace.md,
                                          lpc.gravity.penitential-discipline.md
  lpc.limit.the-lapsed-own-account -> lpc.term.the-lapsed.md
  lpc.limit.411-gesta-unread -> lpc.gravity.conciliar-authority-theory.md
The target records' side of each edge is set by wb_lpc_s25.py (OTHER_TYPE_EDGES_*) for the
gravity targets and is not written by this script. lpc.limit.ordinary-interior-life,
lpc.limit.womens-own-voice, lpc.limit.rural-punic-berber-life, lpc.limit.the-silent-century
and the three ambient records carry relations: [], since none has a single natural
reciprocity target.

NOT DONE HERE: editing records/lpc/{source,world_core,term,story,figure,quote,gravity,
force,contested_claim,voice_craft,demonstration}/, editing records/worlds/, running the M2
compiler, and a full canon_cells tagging sweep.
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


def src(*entries):
    """Each entry is (source_id, locus) or (source_id, locus, license); the license
    defaults to public-domain."""
    return [
        {"source_id": e[0], "locus": e[1], "license": e[2] if len(e) > 2 else "public-domain"}
        for e in entries
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
        "status": "ready",
        "register": "emic",
        "canon_cells": ["F3-I"],
        "confidence": conf("A", "verified-via-authority", "load-bearing", "Inferential-Thin",
            divergence="This unity/convergence reading (Doc_07 §2I, §5-§6) is this build's own "
            "synthetic judgment about how the classified gravities relate to each other, not an "
            "independently-attested claim any single source states in those terms -- carried forward "
            "directly from lpc.core.latin-pastoral-congregational-christianity's own divergence_note, "
            "not presented here as more settled than that record allows."),
        "sources": src(
            ("lpc.source.cyprian-de-lapsis",
             "On the Lapsed, S4, \"it is the shepherd that is chiefly wounded in the wound of his "
             "flock\" -- verified directly against "
             "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 43722-43727"),
            ("lpc.source.cyprian-epistles",
             "Epistle LXVI SS4, Ezekiel 34, \"I will require my flock at their hands,\" applied to "
             "the care bishops owe the lapsed -- verified directly against "
             "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 37340-37362"),
            ("lpc.source.cyprian-epistles",
             "Epistle X, the certificate process, answerability enacted as the road back -- "
             "verified directly against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, "
             "lines 29834-29945"),
            ("lpc.source.augustine-on-baptism-against-the-donatists",
             "Book II, Chapter 7, SS9-10, Cyprian's reasons judged \"truth-like rather than true\" "
             "against the custom a plenary Council confirmed -- verified directly against "
             "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, lines 12153-12169"),
            ("lpc.source.augustine-on-baptism-against-the-donatists",
             "Book V, Chapter 17, SS23, Augustine sets the Church's view against Cyprian's, while "
             "Cyprian \"remained\" in her entirety -- verified directly against "
             "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, lines 12993-12999"),
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
            "Ask what holds us together, and our answer is not that we are pure. Nor is it that we "
            "are right about every hard question we argue. Our answer is that we are answerable. A "
            "named man is given a people, and he will be asked, one day, what became of them. We "
            "see everything else growing out of that one fact: the road back for someone who has "
            "failed, the font that either gives or withholds until a person comes home, the "
            "disagreement between colleagues that we carry without breaking over it. Take the "
            "answerability away, and to us each of these becomes a separate rule we argue about. "
            "Leave it in place, and we see one conviction from several sides.",
            "As we see it, that is why one office teaches the newcomer, washes him, corrects him "
            "when he fails, and takes him home again. Take answerability away, and to us the road "
            "back becomes an empty form and the font a private exchange. In our eyes, a council "
            "would become an argument no one has to answer for. Held together, they are what we "
            "take ourselves to be.",
        ],
        "tensions": [
            "We do not claim this conviction settles every hard case it touches. The very font we "
            "take this answerability to serve, we have answered twice, in opposite ways, a century "
            "and a half apart. Our later bishop judged the earlier answer wrong, yet he never put "
            "the man who gave it outside our communion. Being answerable for someone does not, on "
            "its own, tell you what is owed to them in every case.",
        ],
        "text": (
            "As we understand ourselves, we are held together, first, by one plain fact: a "
            "particular people has been placed in a particular man's care, and he will be asked "
            "what became of them. That is not a title he carries apart from the people it names. To"
            " us, it is the whole shape of what a bishop is. We see everything else we hold growing"
            " out of that one root. The road back for someone who has failed is not a formality. To"
            " us, it is what answerability looks like in practice. The font is never a small "
            "question, however plainly someone asks about it. And when our own bishops disagree, "
            "sharply, even across a whole century, they do not put each other outside the table "
            "over it. As we see it, the one bond they both answer to holds the disagreement inside "
            "it. We do not pretend this makes every hard question easy. We have answered the font "
            "question twice, in opposite ways. Our later bishop judged the earlier answer wrong. "
            "But he never put the man who gave it outside our communion. Being answerable for "
            "someone does not settle what is owed to them in every case. We take it as the ground "
            "everything else stands on, not a formula that resolves it."
        ),
    }
    body = (
        "Taken from Doc_07_Integrated_Ecology_Analysis.md §2I ('Formation Logic... every other "
        "lens converges here') and §6 (Integrative Observation, the source positions[] above "
        "restates), both read in full. The tension is Permanent Prompt line 31/World Capsule Core "
        "§'What This World Holds Without Resolution' own font-twice-answered content, restated "
        "here as this claim's own internal limit rather than duplicating "
        "lpc.demo.font-twice-answered (which demonstrates the same content in dialogue, not as a "
        "standing first-person doctrinal position). relations[] carries two gravity edges (G1, G2) "
        "-- not G3 or G6, each of which receives its own dedicated doctrinal_witness record below "
        "or is already fully demonstrated (font-twice-answered), avoiding redundant edges on "
        "gravities already well-connected elsewhere."
    )
    _write("doctrinal_witness", rid, payload, body)


def build_witness_communion_over_separation() -> None:
    rid = "lpc.witness.communion-over-separation"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "ready",
        "register": "emic",
        "canon_cells": ["F3-T"],
        "confidence": conf("A", "verified-direct", "load-bearing", "Documented",
            divergence="The 256 preface, the De Unitate formula, Augustine's argument, and the "
                       "Felicissimus and Novatian separations are each read at source at the loci "
                       "below. That the rule against separation was held because of those "
                       "separations is Doc_07 SS2H's synthesis; the fields give both side by side "
                       "and do not state that causal link as fact."),
        "sources": src(
            ("lpc.source.cyprian-seventh-council-of-carthage",
             "the 256 preface: \"judging no man, nor rejecting any one from the right of "
             "communion, if he should think differently from us,\" and no one \"a bishop of "
             "bishops\" -- verified directly against "
             "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 56864-56878"),
            ("lpc.source.cyprian-de-unitate",
             "On the Unity of the Church, \"The episcopate is one, each part of which is held by "
             "each one for the whole\" -- verified directly against "
             "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 42286-42291"),
            ("lpc.source.cyprian-epistles",
             "Epistle XXXVII, Felicissimus tried \"to divide with the bishop a portion of the "
             "people\" while Cyprian acted through substitutes in his absence -- verified directly "
             "against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 32236-32306"),
            ("lpc.source.cyprian-epistles",
             "Epistle XXXIX, on the faction of Felicissimus: \"Whosoever gathereth elsewhere, "
             "scattereth\" -- verified directly against "
             "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 32476-32483"),
            ("lpc.source.cyprian-epistles",
             "Epistle XLVIII, Novatus \"appointed his attendant Felicissimus a deacon\" -- "
             "verified directly against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, "
             "lines 33214-33219"),
            ("lpc.source.cyprian-epistles",
             "Epistle XLI, the Novatian party at Rome \"has appointed a bishop for itself\" "
             "against Cornelius -- verified directly against "
             "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 32654-32690"),
            ("lpc.source.augustine-on-baptism-against-the-donatists",
             "Book V, Chapter 17, SS23, Augustine argues against Cyprian's ruling while Cyprian "
             "\"remained\" in the Church's entirety -- verified directly against "
             "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, lines 12993-12999"),
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
            "We can argue that a colleague's ruling was wrong, at length, and still keep him at "
            "our table. One of us said so when he opened the council that would settle the hardest "
            "question in the room. No bishop, he said, sets himself up as a bishop of bishops. "
            "None forces a colleague to obey, since each has his own proper right of judgment. He "
            "added that we judge no one, and reject no one from communion, for thinking "
            "differently from us. A century and a half later, another of us argued at book length "
            "that the ruling made that day was wrong. He never once suggested that the man who "
            "made it stood outside our communion. Disagreement with a colleague, in our own life, "
            "is not a reason to separate.",
            "Underneath the disagreement sits a belief our earlier bishop wrote down plainly. "
            "\"The episcopate is one, each part of which is held by each one for the whole.\" We "
            "read that as the reason a bishop can differ from a colleague without breaking "
            "communion.",
        ],
        "tensions": [
            "We do not hold this rule because we have never broken it. In our own first years, we "
            "watched what breaking it costs. A deacon's faction gathered apart while our bishop "
            "was away in hiding. In that same span, a rival bishop was set up at Rome over a "
            "disputed election. Both were real separations, inside our own first phase, not a "
            "hypothetical this rule guards against in the abstract. We hold the rule that "
            "disagreement must not become separation knowing, from the inside, what separation "
            "actually does.",
        ],
        "text": (
            "We can argue that a colleague's ruling was wrong, at length, and still keep him at "
            "our table. One of our bishops said so when he opened the council that would settle "
            "the hardest question in the room. No bishop, he said, sets himself up as a bishop of "
            "bishops. None forces a colleague to obey. Every bishop has his own proper right of "
            "judgment. At that same council, he said we judge no one, and reject no one from "
            "communion, for thinking differently from us. A century and a half later, another of "
            "our bishops argued at book length that the ruling made that day was wrong. He never "
            "once put the man who made it outside our communion. In our own first years, we had "
            "seen separation from the inside. A deacon's faction gathered apart while our bishop "
            "was away in hiding. In those same years, a rival bishop was set up at Rome over a "
            "disputed election. We do not pretend those separations never happened. We hold our "
            "rule against separation knowing, from our own record, what it costs when it breaks."
        ),
    }
    body = (
        "Taken from Doc_07_Integrated_Ecology_Analysis.md §2H (Boundary Structures), read in "
        "full, including its own Forces integration paragraph naming the Felicissimus schism and "
        "the roughly contemporaneous Novatianist rival consecration at Rome as 'both boundary "
        "failures of exactly the kind G3 exists to prevent, and both inside Cyprian's own phase.' "
        "Doc_06_Full_Lexicon_Development.md's own note that De Unitate was written 'amid the "
        "Felicissimus and Novatianist crises' grounds this record's own source citation directly. "
        "relations[] carries one gravity edge (G3, lpc.gravity.collegial-communion-preserved)."
    )
    _write("doctrinal_witness", rid, payload, body)


def build_witness_confessor_claim() -> None:
    rid = "lpc.witness.confessor-claim-vs-regulated-peace"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "doctrinal_witness",
        "schema_version": SCHEMA_VERSION,
        "status": "ready",
        "register": "emic",
        "canon_cells": ["F6-I"],
        "confidence": conf("B", "verified-via-authority", "load-bearing", "Documented",
            divergence="The confessor's own claim and the certificate process are each "
                       "independently Documented in this world's own Native corpus. That the two "
                       "were never fully reconciled into one settled rule is World Capsule Core's "
                       "own synthesis of that record (§'What This World Holds Without "
                       "Resolution'), not a fresh primary-source read -- disclosed here rather "
                       "than presented as independently re-verified."),
        "sources": src(
            ("lpc.source.cyprian-de-lapsis",
             "On the Lapsed, S2, the confessors greeted as \"the white-robed cohort of Christ's "
             "soldiers\" -- verified directly against "
             "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 43650-43657"),
            ("lpc.source.cyprian-epistles",
             "Epistle X, the confessors asked that peace be granted to certain of the lapsed once "
             "the Church could meet again, and Cyprian asks them to name each one -- verified "
             "directly against cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines "
             "29834-29945"),
            ("lpc.source.cyprian-epistles",
             "Epistle XI, the martyrs' wishes \"looked into in your presence, and with your "
             "judgment\" -- verified directly against "
             "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 29952-29992"),
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
            "In our earliest years, a confessor's suffering carried a claim of its own. Those who "
            "had held firm under questioning, and suffered for it, asked that some who had failed "
            "the same test be given peace. We took that claim in earnest. It was not a pretense, "
            "and it was not treated as nothing.",
            "And yet the road back is examined, weighed, and walked in the open, under one "
            "office's care. It is not handed out on anyone's certificate, however real their "
            "suffering was. We hold both convictions as genuine. One is the process that must "
            "govern the return. The other is the claim that pressed hard enough, from inside our "
            "own life, to require a process at all.",
        ],
        "tensions": [
            "We have never fully absorbed the confessor's own claim into the regulated process it "
            "presses against. It was real, in earnest, and our own regulated order had to answer it "
            "rather than simply override it -- and we do not claim, on our own record, to have found "
            "the single rule that settles which one governs when they point in different directions.",
        ],
        "text": (
            "In our earliest years, those who had confessed Christ and suffered for it made a "
            "claim of their own. Their suffering, they held, gave them standing to ask peace for "
            "some who had failed the test they passed. We took that claim in earnest. Their "
            "suffering was real, and so was what it carried. And it still had to be answered by "
            "something steadier than one man's word, however real his suffering had been: a name "
            "set down, then examined before the whole congregation and with its judgment. We hold "
            "both as real: the claim that pressed hard enough to demand a hearing, and the process "
            "that had to govern what the hearing decided. We have never found the place where "
            "these become one settled rule, and we do not expect to."
        ),
    }
    body = (
        "Taken from World Capsule Core's own §'What This World Holds Without Resolution' "
        "paragraph 2 (the confessor-claim/regulated-order tension) and Permanent Prompt line 35's "
        "own vocabulary paragraph, both read in full. This is G8 "
        "(lpc.gravity.confessor-authority-vs-episcopal-peace, the one classified Tensional "
        "gravity), restated here in first-person doctrinal-witness voice rather than the gravity "
        "record's own etic six-test framing. relations[] carries two gravity edges (G8, G2)."
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
        "status": "ready",
        "register": "emic",
        "canon_cells": ["F5-I"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented"),
        "sources": src(
            ("lpc.core.latin-pastoral-congregational-christianity",
             "this world's own thin_topics field: 'No source anywhere in this world's own vendored "
             "corpus is authored by an ordinary lay believer writing about ordinary congregational "
             "life as such'"),
            ("lpc.source.augustine-confessions",
             "Book IX, Chapter VI, SS14, Augustine's own weeping at his own baptism at Milan, 387, "
             "before he held any office -- the one first-person exception, disclosed rather than "
             "omitted -- verified directly against "
             "cic/texts/npnf101_augustine-confessions-letters.xml, lines 13731-13732"),
        ),
        "relations": [],
        "statement": (
            "We can tell you what was decided about a person, and how carefully, and by whom. We "
            "cannot tell you what an ordinary believer actually felt walking up to the altar, or "
            "standing at the font, or sitting in the congregation on an ordinary week. Almost "
            "never, that is. There is one real exception, and it is not really ordinary. "
            "Augustine's own Confessions describes his own baptism at Milan, before he was a "
            "bishop, in his own first person -- \"how greatly did I weep in Thy hymns and "
            "canticles.\" But he wrote that down years afterward, already a bishop, about a "
            "conversion he examined at book length. Both of our own voices are otherwise bishops. "
            "What comes down to us is mostly what a bishop saw and decided, not what an "
            "unremarkable person in front of him was feeling. Ask us what was decided, and we will "
            "not run short. Ask us what an ordinary believer felt from inside, and that -- with "
            "this one exception -- is still not ours to give you."
        ),
        "why_sources_cannot_answer": (
            "Every text in this world's own Native corpus is authored by Cyprian or Augustine, "
            "addressed either to fellow clergy or to a congregation being taught or corrected -- "
            "almost never a first-person account by a believer of their own experience. One real "
            "exception exists: Confessions IX.vi.14, Augustine's own account of his baptism at "
            "Milan in 387, before he held any office -- \"how greatly did I weep in Thy hymns and "
            "canticles, deeply moved by the voices of Thy sweet-speaking Church\" -- verified "
            "directly against cic/texts/npnf101_augustine-confessions-letters.xml, lines "
            "13731-13732. It does not resolve the general absence: it is a single, "
            "retrospectively written account, composed years later by a man who was by then a "
            "bishop and already the subject of intense attention, about his own baptism "
            "specifically -- not an anonymous or otherwise unremarkable believer's voice, and not "
            "describing an ordinary week rather than a singular occasion. "
            "lpc_Rep_Phase1_Ecology_Assessment.md §2 (Thinness Mapping) names this directly: "
            "'Attested only through episcopal mediation. Both anchor voices are bishops... Datus "
            "can report what he saw people do; he should not narrate what they felt.' "
            "Doc_07_Integrated_Ecology_Analysis.md §5 independently confirms: 'this "
            "Representative should not be built to speak for ordinary believers' interior "
            "experience, which this world's record does not carry.'"
        ),
        "nearest_material": [
            "lpc.gravity.pastoral-office-flock-keeping",
            "lpc.gravity.penitential-discipline",
            "lpc.witness.answerability-as-ground",
        ],
    }
    body = (
        "Grounded in Phase One §2, Doc_07 §7, and the Doc_09 §5 and §7 cross-check. Celled to "
        "F5-I ('Walk me through an ordinary day among your people...') -- a direct match, the "
        "exact question this world's own record cannot answer. No relations[] edge: no single "
        "existing record is the natural reciprocity target for a blanket, population-scale "
        "absence (matching don.limit.ordinary-interior-life's own identical choice for the "
        "analogous finding). Confessions IX.vi.14 is the one genuine first-person exception, "
        "disclosed here rather than left silent -- Augustine's own baptism, not an ordinary "
        "believer's."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_lapsed_own_account() -> None:
    rid = "lpc.limit.the-lapsed-own-account"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "ready",
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
        "Grounded in World Capsule Core's own 'Where This World Is Quiet' section and "
        "Doc_09_Story_Inventory.md §7, both read in full. Distinguished from "
        "lpc.limit.womens-own-voice: this record's own scope is the lapsed AS A CLASS (both "
        "sexes, both named and unnamed), the central subject of this world's own first crisis; "
        "the women's-voice record below is narrower and cross-phase. relations[] carries one term "
        "edge (lpc.term.the-lapsed)."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_womens_own_voice() -> None:
    rid = "lpc.limit.womens-own-voice"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "ready",
        "register": "emic",
        "demo_tag": "exclude",
        "canon_cells": ["F6-P"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented"),
        "sources": src(
            ("lpc.source.cyprian-epistles",
             "Ep. XX-XXI, Numeria and Candida discussed by Celerinus and Lucian, never speaking "
             "themselves"),
            ("lpc.source.cyprian-epistles",
             "Ep. XXXIV, Cyprian on Numidicus, whose wife was burned beside him and whose daughter "
             "sought his body and found him alive"),
            ("lpc.source.augustine-general-correspondence",
             "the Albina correspondence and Letter CCXI, to the nuns of Hippo, known only through "
             "Augustine's own letters to them and about them"),
            ("lpc.source.passio-montani-et-lucii",
             "Passio of Montanus and Lucius 8, Quartillosia's account of her vision in her own "
             "first person, in a text men wrote"),
        ),
        "relations": [],
        "statement": (
            "Women appear throughout our own record, but almost always in someone else's words. "
            "Numidicus's own wife burns beside him; his daughter searches for his body and finds "
            "him alive. Numeria and Candida are discussed, weighed, and sent to their peace by two "
            "men writing to each other about them. In our later years there is a woman we know as "
            "Albina, and a community of nuns at Hippo. We know them only through one of our own "
            "bishop's letters to them and about them. From our own two cities, in our years from 246 to 430, no text a woman wrote "
            "herself survives. That holds in our early years and our later ones. That is not because one half of our "
            "record is thinner than the other. Now and then a woman's spoken words reach us, set "
            "down by men. One martyr account gives a woman's vision in her own first person. "
            "Quartillosia was held in prison with the martyrs. Her husband and son had been put "
            "to death three days before. She told what she saw: her son, who had suffered, "
            "coming to the prison. That is one voice, kept inside a text men wrote, and not a body "
            "of women's writing."
        ),
        "why_sources_cannot_answer": (
            "Doc_09_Story_Inventory.md §7 item 4 states this, checked across both phases: the four "
            "women in the Phase One stories are visible and not audible, and in the second phase "
            "Albina and the community of nuns at Hippo are known only through Augustine's own framing "
            "of them, in letters he wrote about them rather than words they wrote themselves. "
            "Doc_02_Source_Ecology.md §6 independently confirms the Augustine-phase half. No text a "
            "woman wrote herself survives anywhere in this world's own Native corpus, in either "
            "phase. The nearest are letters Paulinus of Nola sent to Augustine in his own and his "
            "wife Therasia's names (Letters XXV, XXX and XCIV, headed \"from Paulinus and Therasia\"), "
            "which he writes largely in his own first person, and a few women's words that men set "
            "down, such as Quartillosia's account of her vision in the Passion of Montanus and Lucius "
            "8 (\"Vidi, inquit, filium meum\", "
            "cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt lines 5771-5785 "
            "and cic/texts/gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt lines 7655-7690; "
            "Source_Registry.md rows 269 and 270, Native; no English version is vendored), and "
            "Monica's words in the Confessions IX.10 and IX.11 "
            "(cic/texts/npnf101_augustine-confessions-letters.xml lines 14147-14168 and 14185-14195), which "
            "Doc_02_Source_Ecology.md §6 sets aside as Augustine's pre-clerical formation narrative."
        ),
        "nearest_material": [
            "lpc.figure.numidicus",
            "lpc.story.numidicus",
        ],
    }
    body = (
        "Grounded in Doc_09_Story_Inventory.md §7 item 4 (checked directly for its own "
        "cross-phase claim rather than assumed from a Cyprian-phase-only summary) and "
        "Doc_02_Source_Ecology.md §6. demo_tag: exclude -- this record shares cell F6-P with "
        "lpc.demo.compel-three-phase (B-7); its own framing vocabulary, which names what our "
        "record lacks, risks false-tagging as a citable candidate for a "
        "demonstration about an unrelated topic (Augustine's coercion doctrine), the same "
        "collision risk pahc.limit.womens-own-words's own precedent names and excludes for. "
        "Distinguished from lpc.limit.the-lapsed-own-account: narrower (named women specifically, "
        "cross-phase) rather than the lapsed as a class."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_rural_punic_berber() -> None:
    rid = "lpc.limit.rural-punic-berber-life"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "ready",
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
            "language many ordinary people spoke there, which was not the one we were taught in -- "
            "we do not carry in any detail, and we will not invent it to fill the silence. Our "
            "whole record comes from two urban sees. A different kind of life, spoken in a "
            "different tongue, in the towns and villages between them, is simply not where our own "
            "voice was formed."
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
        "status": "ready",
        "register": "emic",
        "canon_cells": ["F2-E"],
        "confidence": conf(
            "B", "verified-direct", "load-bearing", "Contested",
            "The silence holds only for what this build has assessed. Nine tractatus in Morin "
            "1917, one titled in a manuscript as a sermon of Optatus of Milevis, are not yet "
            "assessed (OG-54; Doc_01 SS5; Doc_08 Force 3B-2).",
        ),
        "sources": src(
            ("lpc.source.cyprian-seventh-council-of-carthage",
             "256, the last dated act of this world's first phase"),
            ("lpc.source.possidius-vita-augustini-weiskotten1919",
             "391, Augustine's own ordination, the first dated act of this world's second phase"),
        ),
        "relations": [],
        "statement": (
            "Between Cyprian's death in 258 and Augustine's ordination in 391, our own pastoral "
            "voice is quiet. About a hundred and thirty years lie between those two dates. A few "
            "old sermons may come from those years. We have not yet weighed them, so we do not "
            "lean on them or rule them out. That does not mean nothing happened in those years. "
            "It means we have no pastor's words of our own to give you for them."
        ),
        "why_sources_cannot_answer": (
            "This world's construction window runs from roughly 246 to 430. Its Native corpus, as "
            "this build has assessed it, attests two bounded phases: Cyprian's, ending 258, and "
            "Augustine's, beginning 391. No ordinary-pastoral voice from in between has been "
            "assessed. Nine tractatus in Morin 1917 "
            "(cic/texts/augustine_sermones-guelferbytani-lat_morin1917.txt, from line 10297) are "
            "headed as by Optatus of Milevis, Quodvultdeus and others of Augustine's school. A "
            "manuscript titles one a sermon of Optatus (lines 10849-10850). They are not yet "
            "assessed (OG-54), so the silence is Contested."
        ),
        "nearest_material": [
            "lpc.gravity.pastoral-office-flock-keeping",
            "lpc.witness.answerability-as-ground",
        ],
    }
    body = (
        "Grounded directly in Permanent Prompt line 21 and Phase One §2, and cross-confirmed "
        "against World Capsule Core's own §'The Span You Speak From.' Celled to F2-E ('Where is "
        "your own record thinnest?') -- the single best-fitting fleet question for exactly this "
        "finding, not a reach. No relations[] edge: the silence is a property of this world's "
        "whole temporal structure, not of any one gravity or force record."
    )
    _write("honest_limit", rid, payload, body)


def build_limit_gesta_unread() -> None:
    rid = "lpc.limit.411-gesta-unread"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "honest_limit",
        "schema_version": SCHEMA_VERSION,
        "status": "ready",
        "register": "emic",
        "canon_cells": ["F1-E"],
        "confidence": conf("B", "verified-direct", "load-bearing", "Documented"),
        "sources": src(
            ("lpc.source.lancel-actes-de-la-conference-de-carthage-411",
             "consulted for orientation on what the acts contain, not as a substitute for reading "
             "them", "in-copyright-consultation"),
        ),
        "relations": rel(("associated-with", "lpc.gravity.conciliar-authority-theory")),
        "statement": (
            "A conference was held in 411, between our own bishops and the rival communion's own. "
            "It is the largest single gathering of argument between bishops that our own later "
            "years produced. We rest its date on the ordinary, undisputed record of when it "
            "happened. We do not draw on its own transcript of what was actually argued there, "
            "bishop by bishop. That transcript has not been validly read in building this record. "
            "So we cannot tell you how our own bishops, beyond Cyprian and Augustine, argued "
            "authority."
        ),
        "why_sources_cannot_answer": (
            "The Gesta Collationis Carthaginiensis -- the acts of the 411 Conference -- survives "
            "in a Migne printing that has not been validly read in full. It is closed as a "
            "persistence question: it is kept for narrow, independently checkable facts only, and "
            "it is not asked to show how far G5 spread across the world. G5's weak fit with the "
            "forces acting on the world is carried, not resolved."
        ),
        "nearest_material": [
            "lpc.gravity.conciliar-authority-theory",
            "lpc.contested.de-unitate-recensions",
        ],
    }
    body = (
        "Grounded in Doc_07 §7 and §8 item 6. relations[] carries one gravity edge (G5, "
        "lpc.gravity.conciliar-authority-theory), the gravity whose evidence this reading gap "
        "touches. Distinguished from lpc.contested.de-unitate-recensions (a live scholarly "
        "contest over textual priority) -- this record states a build-side reading gap, not a "
        "scholarly dispute."
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
        "status": "ready",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("A", "verified-direct", "illustrative", "Documented"),
        "sources": src(
            ("lpc.source.cyprian-seventh-council-of-carthage",
             "preface, the council met at Carthage ('in unum Cartaginem conuenissent'); the city's "
             "scale restates Doc_01 §2 ('outside Rome itself'), which cites no primary locus"),
            ("lpc.source.possidius-vita-augustini-weiskotten1919",
             "the second city's own smaller, differently-provinced standing"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "Our whole life is lived in two cities, a century and a half apart. The first is a "
            "great port city, the largest Latin Christian city outside Rome. The second lies "
            "further along the same coast -- a smaller see, answerable within a different province "
            "than the first, though its own bishop sat in the same wider councils."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "World Capsule Core §'The World You Inhabit', read in full. States only the visible, "
        "physical/geographic shape of the two sees -- the doctrinal significance of the two-phase "
        "structure is already fully stated at lpc.gravity.pastoral-office-flock-keeping and "
        "throughout this world's own build record. canon_cells: [] and relations: [], matching "
        "don's own three ambient records' identical precedent for a bare physical scene-setting "
        "fact."
    )
    _write("ambient", rid, payload, body)


def build_ambient_council_scale() -> None:
    rid = "lpc.ambient.council-assembly-scale"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "ambient",
        "schema_version": SCHEMA_VERSION,
        "status": "ready",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("A", "verified-direct", "illustrative", "Documented"),
        "sources": src(
            ("lpc.source.cyprian-seventh-council-of-carthage",
             "the 256 council's own sententiae of 87 bishops; preface (kalendis Septembribus, "
             "bishops from Africa, Numidia and Mauretania, with presbyters, deacons and plebis "
             "maxima parte present); sententia 83 (Natalis of Oea votes for himself and for two "
             "absent bishops)"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "In September of 256, bishops from three provinces met at Carthage on the rebaptism "
            "question. Their record holds eighty-seven sentences, given one after another. Each "
            "bishop said what he judged. Two who could not come sent their vote with a colleague. "
            "Presbyters and deacons were there too, with most of the people."
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
        "status": "ready",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("A", "verified-direct", "illustrative", "Documented"),
        "sources": src(
            ("lpc.source.possidius-vita-augustini-weiskotten1919",
             "ch. XXIV, re-verified directly at "
             "cic/texts/possidius_vita-augustini_weiskotten1919.txt, the chapter body itself (not "
             "the endnotes apparatus, a separate section of the same file)"),
        ),
        "retrieval": retrieval(3),
        "relations": [],
        "detail": (
            "In one church we know, the bishop handed the care of its building and property to the "
            "more capable of his clergy, in turn. He never held the key himself, and never wore "
            "the ring. Everything received and everything spent was noted down by those he had "
            "entrusted with it. Once a year, the accounts were read out to him, so he would know "
            "what had come in, what had gone out, and what still remained."
        ),
        "formation_claim_barred": True,
    }
    body = (
        "Possidius, Vita Augustini ch. XXIV, re-verified directly against the vendored file, "
        "quoted closely: 'He never held the key nor wore his ring, but everything which was "
        "received and spent was noted down by these overseers of the house. At the end of the "
        "year the accounts were read to him.' The detail field rests on this text directly, not "
        "on the summary framing in Doc_09_Story_Inventory.md §6 item 5 ('XXIV's account of the "
        "key, the ring and the annual audit'). States only the bare administrative/physical fact "
        "-- no formation claim is made about what this practice meant. canon_cells: [] and "
        "relations: [], matching don.ambient.deo-laudes-as-object's own identical precedent for a "
        "bare physical-object fact."
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
