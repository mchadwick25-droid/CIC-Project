"""CO-P2-15 (Mark, 2026-07-28) - the five missing governed-CT term records
authored (CO-P2-03's Alexandria application).

Doc_06 SS2's firm-six CT terms minus the built Nous: Apokatastasis
(alexlex051), Catechetical School/Didaskaleion (059), Fall/Descent (074),
Homoousios/Consubstantial (081), Logikos/Rational Nature (090) - specified
in the master index and the SS2 authority table, never produced as
chunks/records. Authored here at Tier 2 (this world assigns no Tier 3),
full term@tier12 requiredness.

Grounding, per field discipline:
- the CONTEST content is Doc_06 SS2's authority table (verbatim-adjacent)
  + the S2.6 claim records that already did the contest analysis
  (alexclaim003 Homoousios, alexclaim004 Didaskaleion, alexclaim005 the
  Origen cluster) + the carried-contest parkings (022/023/039, 029);
- world_meaning/voice_surface speak from-inside per the built terms'
  register; the contested stratum is carried as the world carries it
  (relief-and-burden; treasure-and-unease; held-open institution);
- prior senses follow the S2.3 convention: UNVERIFIED-flagged where the
  build docs do not develop them;
- field_relations: associated-with links to the surfacing/cluster terms
  (mirrors added on the existing records); the four Origen-cluster CTs
  interlink (Doc_06's own 'theologically linked' one-contest finding);
- contested_claim_ids set at authoring (the FLAG-014 discipline);
- horizon guards in retrieval: the 543/553 condemnation and Chalcedon do
  not exist for the voice - DNRW clauses steer those to the in-world
  registers.

Closes: the last Related-Terms render defect (020 -> Apokatastasis); the
deployed guidance's dangling alexlex051 pointer; the term-side homes for
alexclaim003/004/005's remaining CT ids.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from s62_alx_source_rows import emit_record
from s62_alx_s25 import read_record

TERM_DIR = BACKEND / "wrs" / "records" / "alexandria_world" / "term"

COMMON = {"world_id": "alexandria-catechetical", "record_type": "term",
          "schema_version": 1, "jobs": [1, 2, 4, 6], "register": "emic",
          "review_state": "draft", "cache_stability": "static"}

CONF = {"citation_specificity": "B",
        "verification_state": "verified-via-authority",
        "verification_date": "2026-07-28",
        "evidentiary_weight": "corroborating"}

S = lambda *ids: [{"source_id": i} for i in ids]
E = lambda t, tid, note: {"type": t, "target_id": tid, "note": note}

CLUSTER_NOTE = ("CO-P2-15: the four Origen-cluster CT terms carry one "
                "theologically linked Meaning contest (Doc_06 SS2's own "
                "cross-references; governed at alexclaim005).")
SURF_NOTE = ("CO-P2-15: the governed contest this term carries is surfaced "
             "at the partner term (Doc_06 SS3's CT-surfacing convention).")

TERMS = [
 dict(
  id="alexlex081", term="Homoousios / Consubstantial",
  aliases=["homoousios", "consubstantial", "of one substance",
           "of one being with the Father", "the Nicene term"],
  quick_meaning=("For this world homoousios is the drawn line of 325: the "
                 "confession that the Son is of one substance with the "
                 "Father - not the highest creature, but God's own Word. It "
                 "is held as settlement, arrived at and felt: relief and "
                 "burden at once."),
  world_meaning=("The word was not always ours. Before the contest it was "
                 "not the confession's word at all; the Son's precise "
                 "standing was held loosely, argued, explored. Then brothers "
                 "within the household contested the very confession of the "
                 "Word - 'there was when he was not' - and what had been "
                 "held loosely had to be held within a drawn line. The line "
                 "was drawn at Nicaea: the Word is of one substance with the "
                 "Father. With him, not less than him.\n\n"
                 "We hold the settlement as settlement, not as a timeless "
                 "given. It came to us as rest and as burden together: the "
                 "Word confessed of one substance, and the freedom to "
                 "explore now bounded. The confession is carried wherever "
                 "Christ is named - the Christ confession asserts it, Son of "
                 "God carries its argument most directly, and the "
                 "Incarnation's restorative claim rests on it: only one who "
                 "is of one substance with the Father can give what the "
                 "Incarnation gives.\n\n"
                 "What the word carried in its own moment, and what it came "
                 "to carry afterward, are not simply the same - our own "
                 "registers keep the before and the after distinct rather "
                 "than reading the later, fuller sense back into the "
                 "bishops' intent (the Historical-scope + Meaning contest, "
                 "governed at alexclaim003; Doc_06 SS2)."),
  modern_hearing=("**Modern Hearing:**\n\"Homoousios\" as a technical creedal "
                  "formula - church jargon settled in a committee, an "
                  "abstract metaphysical label with no stakes for a life."),
  distortion_risk=("**World Hearing:**\nA line drawn in grief and relief "
                   "within living memory - the word that settled whether "
                   "the One the reading opens onto is God himself or a "
                   "creature; everything the formation promises hangs on "
                   "it, and the cost of the drawing is still felt."),
  period_sense=("The Nicene confession's term (from 325): the Son of one "
                "substance with the Father - the settlement of the Arian "
                "contest, held as relief-and-burden (Doc_08 2A-4 L2; "
                "alexclaim003)."),
  prior_sense=("Pre-Nicene ousia-language: 'substance' vocabulary from "
               "Greek philosophy, and earlier Christian uses of homoousios "
               "(including suspect Gnostic and Paul-of-Samosata-era uses "
               "the tradition debated) - noted from standard patristic "
               "lexica, UNVERIFIED against a registry source; the build "
               "docs develop only the Nicene sense."),
  modern_sense=("A creedal technicality: 'consubstantial' as liturgical "
                "boilerplate or an abstract metaphysical claim without "
                "existential weight."),
  conceptual_distance_note=("Modern hearers meet a settled formula; the "
                            "world holds a recently-drawn line with its "
                            "cost live (the freedom to explore now "
                            "bounded). The distance is temporal-emotional, "
                            "not merely conceptual: settlement vs. "
                            "settlement-being-made. Sharp gap: high "
                            "grounding criterion."),
  semantic_domain="christology",
  grounding_criterion="high",
  voice_surface=("The Word is of one substance with the Father - with him, "
                 "not less than him. That line was drawn among us, and it "
                 "came as rest and as burden together: the confession "
                 "settled, and the old freedom to explore now bounded. We "
                 "hold both, and we do not pretend the drawing cost "
                 "nothing."),
  confidence={**CONF, "evidentiary_weight": "load-bearing",
              "formation_confidence": "Widely Accepted"},
  retrieval={"tier": 2, "force_llm_vote": False,
             "retrieve_when": [
              "participant asks what homoousios or 'consubstantial' means, or why the creed uses it",
              "participant asks how the Arian controversy was settled, or what Nicaea decided",
              "conversation reaches the Son's relation to the Father as a contested or settled question",
              "participant asks whether the Nicene settlement was felt as victory or loss"],
             "do_not_retrieve_when": [
              {"condition_type": "sense-disambiguation",
               "text": ("the participant is asking about later conciliar history beyond c. 400 "
                        "(Chalcedon, the two-natures definition) - beyond this world's horizon; "
                        "the voice answers only the settlement it lived")},
              {"condition_type": "sense-disambiguation",
               "text": ("the Christ/Son-of-God/Incarnation chunks have already surfaced the "
                        "carried contest this turn (they reproduce it; alexlex022/023/039)")}]},
  sources=[
   {"source_id": "srcALX029", "locus": "The Nicene Creed (325) - the term's own locus",
    "author_gravity_note": ("The confession itself; the term's one "
                            "unambiguous native attestation within the "
                            "horizon.")},
   {"source_id": "srcALX003", "locus": "Athanasius, anti-Arian corpus",
    "author_gravity_note": ("The decades-long Nicene defense - how the "
                            "settlement was held, argued, and enforced from "
                            "Alexandria (bishop 328-373).")},
   {"source_id": "srcALX017", "locus": "Williams, Arius: Heresy and Tradition",
    "author_gravity_note": ("Secondary scholarship situating Arius within "
                            "the Origenian Alexandrian tradition - the "
                            "scope-and-meaning contest's modern side "
                            "(Doc_06 SS2).")}],
  field_relations=[
   E("associated-with", "alexlex022", SURF_NOTE + " Christ asserts the consubstantiality."),
   E("associated-with", "alexlex023", SURF_NOTE + " Son of God carries the ontological argument most directly."),
   E("associated-with", "alexlex039", SURF_NOTE + " The Incarnation's restorative claim rests on it."),
  ],
  contested_claim_ids=["alexclaim003"]),
 dict(
  id="alexlex059", term="Catechetical School / Didaskaleion",
  aliases=["the didaskaleion", "the catechetical school",
           "the school of Alexandria", "the teaching succession"],
  quick_meaning=("For this world the didaskaleion names its own teaching "
                 "life - teachers the community knew to be truly formed, "
                 "seekers who came to read beside them, and a reading "
                 "handed from one to the next. Whether that was a formal "
                 "institution with a succession of heads is a genuinely "
                 "open question the record cannot settle."),
  world_meaning=("What lived among us was accompanied reading: one who had "
                 "been given sight read beside another until that other "
                 "began to see for himself, and those who were formed "
                 "became teachers to others in turn. The community "
                 "remembers a line - Pantaenus, Clement, Origen, on to "
                 "Didymus - and remembers it with gratitude: the handing-on "
                 "mattered enough to keep the names.\n\n"
                 "Whether there stood behind that memory a formal "
                 "institution - a house with an office and a roll of "
                 "masters, one succeeding the next - was never a question "
                 "our own life stopped to ask, and it is genuinely "
                 "contested now: the succession's main narrator wrote "
                 "generations later, and the record has no second witness "
                 "to the institutional continuity he presents. What is "
                 "well-attested is the KIND of authority the teacher held "
                 "- grounded in demonstrated wisdom, enacted as "
                 "accompaniment - and that authority does not depend on "
                 "the institutional question being resolved (alexlex029's "
                 "carried contest; alexclaim004; Doc_01 SS1.2)."),
  modern_hearing=("**Modern Hearing:**\n\"The Catechetical School of "
                  "Alexandria\" as a settled historical institution - an "
                  "ancient university with founding date, faculty, and "
                  "succession neatly documented."),
  distortion_risk=("**World Hearing:**\nAccompanied reading remembered as a "
                   "living line of teachers - the reality is the "
                   "formation relationship and the community's memory of "
                   "its handing-on, with the institutional form held "
                   "open, not asserted."),
  period_sense=("The teaching tradition of Alexandria as its own community "
                "remembered it: formed teachers, seekers who came to read, "
                "a remembered succession of names (Doc_01 SS1.2; "
                "alexclaim004.claim)."),
  prior_sense=("Didaskaleion as ordinary Greek for a place of teaching - a "
               "schoolroom; the word itself carries no institutional "
               "grandeur - noted from standard lexica, UNVERIFIED against "
               "a registry source."),
  modern_sense=("A proto-university: formal institution, official heads, "
                "continuous succession - the reading van den Broek and van "
                "den Hoek deny for the period before Origen, and Scholten "
                "affirms only as a theological (not catechumen-training) "
                "school (Doc_06 SS2)."),
  conceptual_distance_note=("The modern frame asks an institutional "
                            "question (was the school real?); the world's "
                            "own register is the formation relationship "
                            "the question papers over. The contest is "
                            "Historical scope (Doc_06 SS2), Eusebius "
                            "HIGH Author-Gravity on the succession "
                            "particulars; the voice answers from the "
                            "attested authority-kind, never the "
                            "institutional claim. Sharp frame gap: high "
                            "grounding criterion."),
  semantic_domain="formation-institutions",
  grounding_criterion="high",
  voice_surface=("There were teachers among us the community knew to be "
                 "truly formed - you could see that they saw - and seekers "
                 "came to read beside them, and the reading passed from "
                 "one to the next. Whether a later tongue names that an "
                 "institution or something looser was never a question our "
                 "own life stopped to ask."),
  confidence={**CONF,
              "formation_confidence": "Contested"},
  retrieval={"tier": 2, "force_llm_vote": False,
             "retrieve_when": [
              "participant asks whether the catechetical school was a real institution, or about its succession of heads",
              "participant asks how the Alexandrian school was organized, founded, or run",
              "a scholarly framing of the school's historicity arrives (van den Broek / Scholten class)"],
             "do_not_retrieve_when": [
              {"condition_type": "sense-disambiguation",
               "text": ("the participant asks what studying under a teacher was LIKE - retrieve "
                        "alexstory001/alexlex029 territory (the formation relationship), not the "
                        "institutional contest")},
              {"condition_type": "sense-disambiguation",
               "text": ("the Teacher chunk has already surfaced the carried contest this turn "
                        "(alexlex029 reproduces it)")}]},
  sources=[
   {"source_id": "srcALX009", "locus": "Eusebius, Ecclesiastical History (the succession narrative)",
    "author_gravity_note": ("The main - often sole - source for the "
                            "succession; HIGH Author-Gravity risk, carried "
                            "on every succession particular (Doc_06 SS2).")},
   {"source_id": "srcALX021", "locus": "The Alexandrian Church: People and Institutions",
    "author_gravity_note": ("Institutional scholarship on what the "
                            "Alexandrian church's structures actually "
                            "were - the modern side of the scope contest.")},
   {"source_id": "srcALX001", "locus": "Clement (the teaching life's own witness)",
    "author_gravity_note": ("The teaching tradition attested from inside - "
                            "independent of the institutional frame.")},
   {"source_id": "srcALX007", "locus": "Gregory Thaumaturgus, Address of Thanksgiving",
    "author_gravity_note": ("The student-side account of the accompaniment "
                            "mode - what the 'school' was as lived.")}],
  field_relations=[
   E("associated-with", "alexlex029", SURF_NOTE + " Teacher is where a participant most directly meets this contest."),
   E("associated-with", "alexlex003", SURF_NOTE + " Catechesis is Doc_06 SS3's named reference point."),
  ],
  contested_claim_ids=["alexclaim004"]),
 dict(
  id="alexlex051", term="Apokatastasis",
  aliases=["apocatastasis", "universal restoration",
           "the restoration of all things", "restoration of all rational beings"],
  quick_meaning=("For this world apokatastasis names Origen's furthest "
                 "hope: that in the end every rational being - none lost - "
                 "is restored to the contemplation it was made for. The "
                 "world carries it as speculation offered, not settled "
                 "teaching: exploration under the Rule of Faith, held with "
                 "unease as well as love."),
  world_meaning=("There is a hope our boldest teacher reached for, further "
                 "out than the confessed faith required: that the end "
                 "answers the beginning - that as all rational beings came "
                 "from God's hand, so all, in the end, are drawn home; "
                 "that no creature is finally lost, and God is at last all "
                 "in all. He offered it as exploration, not decree - a "
                 "reading of what the goodness of God might mean at its "
                 "furthest reach.\n\n"
                 "We hold it the way we hold the rest of his boldest "
                 "reaching: carried and loved, and held with a more "
                 "careful hand than he held it. The broadly-shared "
                 "restorative conviction - that God's work restores what "
                 "fell - does NOT require this furthest extension; the "
                 "restoration the whole tradition confesses stands "
                 "separable from the universalist hope (the Restoration "
                 "term, alexlex020, carries that settled conviction; "
                 "Doc_06 SS2's own resolution). Whether the propositions "
                 "later condemned represent what he himself actually "
                 "taught is genuinely disputed and unresolved - and lies, "
                 "in any case, past the edge of our life (the Meaning "
                 "contest, governed at alexclaim005)."),
  modern_hearing=("**Modern Hearing:**\n\"Universalism\" as a modern doctrinal "
                  "position to adopt or refute - a settled teaching one "
                  "signs up for, mapped onto present-day debates."),
  distortion_risk=("**World Hearing:**\nA teacher's furthest hope, offered "
                   "speculatively under the Rule of Faith and carried by "
                   "the community as treasure-and-unease - not a position "
                   "held, but a reaching loved and held open."),
  period_sense=("Origen's speculative hope of the restoration of all "
                "rational beings to contemplation - offered as exploration "
                "under the Rule of Faith (Doc_06 SS2; alexclaim005; the "
                "world_meaning above)."),
  prior_sense=("Apokatastasis in older Greek usage: restoration or "
               "re-establishment - astronomical return of the stars to "
               "position, medical restoration to health, Stoic cosmic "
               "renewal - noted from standard lexica, UNVERIFIED against "
               "a registry source; Acts 3:21's 'restoration of all "
               "things' is the scriptural seed the build docs treat via "
               "the Restoration term."),
  modern_sense=("Universalism as a codified doctrine in present-day "
                "debate - with Origen cited as its patron and the 553 "
                "condemnation as its refutation, both read as settled."),
  conceptual_distance_note=("Moderns meet a doctrine with a verdict; the "
                            "world holds an open exploration with no "
                            "verdict yet fallen (the condemnation lies "
                            "beyond the horizon; the first controversy "
                            "erupts only at the very edge). Maximal "
                            "Author-Gravity: sole systematic source is "
                            "Origen (Doc_06 SS2). Relationship to "
                            "present-day traditions is part of the "
                            "governed contest. High grounding criterion."),
  semantic_domain="eschatology",
  grounding_criterion="high",
  voice_surface=("There is a hope one teacher among us reached for, "
                 "further out than the confession required: that in the "
                 "end nothing God made for himself is finally lost. We "
                 "love the reach of it. We hold it with a more careful "
                 "hand than he did. It is a hope offered, not a teaching "
                 "settled - and we have not closed it."),
  confidence={**CONF,
              "formation_confidence": "Contested"},
  retrieval={"tier": 2, "force_llm_vote": False,
             "retrieve_when": [
              "participant asks about universal salvation, universalism, or whether all are saved in the end",
              "participant asks about Origen's condemned teachings or his furthest speculations",
              "the Restoration term's territory deepens toward the universalist extension (alexlex020's own not-yet-built pointer)"],
             "do_not_retrieve_when": [
              {"condition_type": "sense-disambiguation",
               "text": ("the participant asks about the 553 condemnation as settled history - beyond "
                        "this world's horizon; the voice knows unease, not the verdict")},
              {"condition_type": "sense-disambiguation",
               "text": ("the participant means the broadly-confessed restorative conviction, not the "
                        "universalist extension - retrieve alexlex020 (Restoration) instead")}]},
  sources=[
   {"source_id": "srcALX002", "locus": "Origen, De principiis (the speculative stratum's sole systematic source)",
    "author_gravity_note": ("Maximal Author-Gravity: the hope exists in the "
                            "record as ONE teacher's offered exploration "
                            "(Doc_06 SS2).")},
   {"source_id": "srcALX015", "locus": "Chadwick (Origen scholarship)",
    "author_gravity_note": ("The modern continuity dispute - later "
                            "distorting systematization vs. meaningful "
                            "continuity; specialists genuinely divided.")},
   {"source_id": "srcALX012", "locus": "Jerome, Letters (Origenist controversy)",
    "author_gravity_note": ("The controversy's contemporary witness - with "
                            "this store's own caveat that his later "
                            "anti-Origenist position colors his "
                            "retrospective treatment.")}],
  field_relations=[
   E("associated-with", "alexlex020",
     "CO-P2-15: the separability pair - the confessed restorative conviction "
     "(020) stands WITHOUT the universalist extension (Doc_06 SS2's "
     "Restoration resolution); 020's not-yet-built pointer closed."),
   E("associated-with", "alexlex011", CLUSTER_NOTE),
   E("associated-with", "alexlex074", CLUSTER_NOTE),
   E("associated-with", "alexlex090", CLUSTER_NOTE),
  ],
  contested_claim_ids=["alexclaim005"]),
 dict(
  id="alexlex074", term="Fall / Descent",
  aliases=["the fall", "the descent of souls", "pre-cosmic fall",
           "the cooling of the noes"],
  quick_meaning=("For this world the Fall names both the confessed truth "
                 "that what God made well fell into sin and death, and - "
                 "in Origen's speculative stratum - a pre-cosmic account: "
                 "rational beings cooling from contemplation into embodied "
                 "souls. The first the world confesses; the second it "
                 "carries as contested inheritance."),
  world_meaning=("That the world we stand in is fallen - that death and "
                 "sin are not what we were made for - this the whole "
                 "tradition confesses; it is the ground the Incarnation's "
                 "remedy answers (Sin, Death, Salvation carry it). But "
                 "our boldest teacher reached further back: before this "
                 "world, rational beings held in contemplation of God; a "
                 "cooling, a turning-away; and embodied existence as, in "
                 "part, the form of the descent - the soul (psyche) named "
                 "from the cooling (psychesthai) of the nous.\n\n"
                 "That further account we hold as we hold the rest of his "
                 "furthest reaching: as exploration offered, not teaching "
                 "settled. Whether it is his own considered position or a "
                 "later systematization pressed onto him is genuinely "
                 "disputed - such that 'the Alexandrian Fall account' "
                 "cannot simply be stated as settled, in either direction "
                 "(Doc_06 SS2: Meaning + Application to this world; "
                 "governed at alexclaim005)."),
  modern_hearing=("**Modern Hearing:**\n\"The Fall\" as the settled Eden "
                  "narrative alone - Adam, the garden, original sin as "
                  "later doctrine codified it; any 'pre-cosmic fall' talk "
                  "sounds like settled heresy."),
  distortion_risk=("**World Hearing:**\nA confessed fallenness the whole "
                   "tradition reads at depth, and behind it a teacher's "
                   "speculative reaching about what fell and when - held "
                   "open, neither confessed nor condemned within the "
                   "world's own hearing."),
  period_sense=("The confessed fallenness of the world (the ground of the "
                "Incarnation's remedy) and Origen's speculative pre-cosmic "
                "descent of rational beings - the second carried as "
                "contested inheritance (Doc_06 SS2; alexclaim005)."),
  prior_sense=("Greek and Jewish antecedents - Platonic descent of the "
               "soul into body; Genesis read in Alexandria through Philo - "
               "noted from standard scholarship, UNVERIFIED against a "
               "registry source; the build docs develop the Genesis-at-"
               "depth reading via Scripture/Allegory, not here."),
  modern_sense=("Original sin as codified doctrine, or 'the Fall' as "
                "mythology to be demythologized - either way a settled "
                "verdict on a question this world held open."),
  conceptual_distance_note=("Moderns arrive with the question closed (one "
                            "way or the other); the world distinguishes "
                            "registers - confessed fallenness held firm, "
                            "the pre-cosmic account held open as one "
                            "teacher's exploration. The Application-to-"
                            "this-world contest (Doc_06 SS2) is exactly "
                            "about not flattening those registers. High "
                            "grounding criterion."),
  semantic_domain="cosmology-anthropology",
  grounding_criterion="high",
  voice_surface=("That we are fallen - that death and sin are not what we "
                 "were made for - this we confess without hesitation. What "
                 "fell, and when, and from what height: there one teacher "
                 "among us reached further back than the confession "
                 "required, and we carry his reaching as we carry him - "
                 "with love, and with a more careful hand."),
  confidence={**CONF,
              "formation_confidence": "Contested"},
  retrieval={"tier": 2, "force_llm_vote": False,
             "retrieve_when": [
              "participant asks about Origen's pre-existence or pre-cosmic fall teaching",
              "participant asks what 'the Alexandrian view of the Fall' was",
              "the Nous term's territory deepens toward what the soul originally was (alexlex011's speculative stratum)"],
             "do_not_retrieve_when": [
              {"condition_type": "sense-disambiguation",
               "text": ("the participant asks about sin, death, or fallenness as lived and confessed - "
                        "retrieve alexlex017/018/036 territory, not the speculative stratum")},
              {"condition_type": "sense-disambiguation",
               "text": ("the participant asks about the later condemnations as settled history - beyond "
                        "the horizon; the voice knows the unease, not the verdict")}]},
  sources=[
   {"source_id": "srcALX002", "locus": "Origen, De principiis I-II (the pre-cosmic account)",
    "author_gravity_note": ("The speculative stratum's source - offered as "
                            "exploration; its continuity with the condemned "
                            "propositions is the governed dispute.")},
   {"source_id": "srcALX015", "locus": "Chadwick (Origen scholarship)",
    "author_gravity_note": ("The own-position vs. later-systematization "
                            "scholarship; genuinely divided (Doc_06 SS2).")}],
  field_relations=[
   E("associated-with", "alexlex011",
     "CO-P2-15: the descent is the nous's descent - the same speculative "
     "stratum alexlex011's CT contest carries. " + CLUSTER_NOTE),
   E("associated-with", "alexlex051", CLUSTER_NOTE),
   E("associated-with", "alexlex090", CLUSTER_NOTE),
  ],
  contested_claim_ids=["alexclaim005"]),
 dict(
  id="alexlex090", term="Logikos / Rational Nature",
  aliases=["logikos", "rational natures", "rational beings", "the logika"],
  quick_meaning=("For this world logikos names what answers to the Logos "
                 "in every rational being: creatures made for the Word, "
                 "capable of knowing God. In Origen's speculative "
                 "framework it extends to a whole cosmology of rational "
                 "natures - held as contested inheritance, not confessed "
                 "teaching."),
  world_meaning=("Every being that can know God is logikos - made through "
                 "the Logos and made FOR him, so that reason at its root "
                 "is not cleverness but kinship: what in the creature "
                 "answers to the Word. This much stands close to the "
                 "confessed center (the Logos, the image of God, the nous "
                 "carry it in the built vocabulary).\n\n"
                 "Origen framed it further: a cosmology of rational "
                 "natures - the 'fallen rational natures' framework, "
                 "grades of rational beings, their descent and hoped-for "
                 "restoration. Whether that framework is his own or a "
                 "later systematization, and how it relates to the "
                 "condemned propositions, is the governed Meaning contest "
                 "(Doc_06 SS2; alexclaim005). And the term carries a "
                 "cross-build boundary: the desert tradition developed its "
                 "own technical use of the logikoi (the Evagrian "
                 "framework), which belongs to the Desert Christianity "
                 "build and is not this world's own attested vocabulary "
                 "(Doc_03 SS3's desert cluster; the alexgrav013 "
                 "not-advanced record carries the same flag at the "
                 "gravity layer)."),
  modern_hearing=("**Modern Hearing:**\n\"Rational\" as calculating "
                  "intelligence - IQ, logic, the capacity to argue; "
                  "'rational nature' sounds like a philosophy-seminar "
                  "category with no devotional weight."),
  distortion_risk=("**World Hearing:**\nKinship with the Word - to be "
                   "logikos is to be made for the Logos, so that knowing "
                   "God is the creature's native calling, not an "
                   "intellectual specialty."),
  period_sense=("What answers to the Logos in the creature: rational "
                "nature as kinship with the Word, capacity for knowing "
                "God (the Logos/image-of-God/nous cluster); extended in "
                "Origen's speculative framework to the cosmology of "
                "rational natures (Doc_06 SS2; alexclaim005)."),
  prior_sense=("Greek philosophical logikos: possessed of reason/logos - "
               "Stoic rational-animal vocabulary - noted from standard "
               "lexica, UNVERIFIED against a registry source; the build "
               "docs develop the Logos-kinship sense, not the Stoic "
               "frame."),
  modern_sense=("Rationality as calculative intelligence; 'rational "
                "nature' as a scholastic or philosophical classifier "
                "detached from formation."),
  conceptual_distance_note=("Modern 'rational' measures thinking power; "
                            "the world's logikos names what a creature is "
                            "FOR - the Logos-kinship that makes knowing "
                            "God the native calling. Origen-adjacent "
                            "Author-Gravity on the cosmological "
                            "framework; cross-build flag on the Evagrian "
                            "technical use (desert-attributed). High "
                            "grounding criterion."),
  semantic_domain="anthropology",
  grounding_criterion="high",
  voice_surface=("To be rational, among us, is not to be clever. It is to "
                 "be made through the Word and for him - so that in every "
                 "being that can know God, something answers to the Logos "
                 "the way an eye answers to light. That kinship is what "
                 "the whole formation calls on."),
  confidence={**CONF,
              "formation_confidence": "Widely Accepted"},
  retrieval={"tier": 2, "force_llm_vote": False,
             "retrieve_when": [
              "participant asks what 'rational nature' or logikos means in this tradition",
              "participant asks about Origen's rational-natures cosmology or the grades of rational beings",
              "conversation reaches why knowing God is possible for creatures at all (the Logos-kinship ground)"],
             "do_not_retrieve_when": [
              {"condition_type": "sense-disambiguation",
               "text": ("the participant means the Evagrian/desert technical logikoi framework - "
                        "cross-build territory, held open (Doc_01 SS3.3); the voice does not speak "
                        "the desert's developed discipline as its own")},
              {"condition_type": "sense-disambiguation",
               "text": ("the participant is asking about the nous as contemplative faculty - retrieve "
                        "alexlex011 (the built Tier-1 term) first")}]},
  sources=[
   {"source_id": "srcALX002", "locus": "Origen, De principiis (the rational-natures framework)",
    "author_gravity_note": ("Origen-adjacent Author-Gravity: the cosmological "
                            "framework is his; its continuity with the "
                            "condemned propositions is the governed "
                            "dispute (Doc_06 SS2).")},
   {"source_id": "srcALX001", "locus": "Clement (the Logos-kinship register)",
    "author_gravity_note": ("The broadly-Alexandrian ground: creatures made "
                            "for the Word, knowing God as native calling - "
                            "independent of the speculative cosmology.")}],
  field_relations=[
   E("associated-with", "alexlex011",
     "CO-P2-15: the nous is the faculty, logikos the nature - the same "
     "anthropological cluster. " + CLUSTER_NOTE),
   E("associated-with", "alexlex001",
     "CO-P2-15: logikos is kinship with the Logos - the term's confessed "
     "ground (the built Logos term carries the center)."),
   E("associated-with", "alexlex051", CLUSTER_NOTE),
   E("associated-with", "alexlex074", CLUSTER_NOTE),
  ],
  contested_claim_ids=["alexclaim005"]),
]

# mirrors to add on EXISTING records: target -> list of (new_id, note)
MIRRORS = {
 "alexlex022": [("alexlex081", SURF_NOTE)],
 "alexlex023": [("alexlex081", SURF_NOTE)],
 "alexlex039": [("alexlex081", SURF_NOTE)],
 "alexlex029": [("alexlex059", SURF_NOTE)],
 "alexlex003": [("alexlex059", SURF_NOTE)],
 "alexlex020": [("alexlex051",
                 "CO-P2-15: the separability pair mirrored - the "
                 "not-yet-built pointer this record carried since S2.2 "
                 "now resolves.")],
 "alexlex011": [("alexlex051", CLUSTER_NOTE), ("alexlex074", CLUSTER_NOTE),
                ("alexlex090", CLUSTER_NOTE)],
 "alexlex001": [("alexlex090",
                 "CO-P2-15: mirror - logikos as kinship with the Logos.")],
}

BODY = ("CO-P2-15 (Mark, 2026-07-28) - governed-CT term record authored "
        "(the CO-P2-03 Alexandria application): Doc_06 SS2's authority "
        "table is the contest source (verbatim-adjacent); the S2.6 claim "
        "records carry the contest analysis; world_meaning/voice_surface "
        "authored from-inside per the built terms' register; prior sense "
        "UNVERIFIED-flagged per the S2.3 convention. Tier 2 (this world "
        "assigns no Tier 3). No chunk file exists yet - the chunk view "
        "generates one at swap time. See wrs/migrate/s62_alx_s29_co15.py.")

MIRROR_BODY_NOTE = ("\n\nCO-P2-15 (2026-07-28): associated-with mirror(s) "
                    "added toward the newly-authored governed-CT term "
                    "record(s); see wrs/migrate/s62_alx_s29_co15.py.")


def main():
    for t in TERMS:
        rec = {**COMMON, **t}
        path = TERM_DIR / f"{t['id']}.md"
        emit_record(rec, BODY, path)
    changed = 0
    for rid, additions in MIRRORS.items():
        path = TERM_DIR / f"{rid}.md"
        rec, body = read_record(path)
        fr = rec.setdefault("field_relations", [])
        dirty = False
        for new_id, note in additions:
            if any(e.get("target_id") == new_id and
                   e.get("type") == "associated-with" for e in fr):
                continue
            fr.append({"type": "associated-with", "target_id": new_id,
                       "note": note})
            dirty = True
            changed += 1
        if dirty:
            if "CO-P2-15" not in body:
                body += MIRROR_BODY_NOTE
            emit_record(rec, body, path)
    print(f"CO-P2-15: {len(TERMS)} governed-CT term records authored "
          f"(051/059/074/081/090); {changed} mirror edges on "
          f"{len(MIRRORS)} existing records")


if __name__ == "__main__":
    main()
