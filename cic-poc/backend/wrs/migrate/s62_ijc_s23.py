"""S6.2/IJC - S2.3-equivalent: author the 12 term records (senses,
confidence, voice_surface, field_relations, script/domain apparatus).

Grounding: every authored field is chunk-grounded (Quick Meaning /
World Meaning / Distortion Risk / Ecological Function / the parked
Plural-Voices and Reported-Experience sections) or marked UNVERIFIED
(prior_sense etymologies only).

Conventions carried:
- FLAG-002: each term's FIRST edge carries its chunk Ecological
  Function verbatim ("Chunk Ecological Function (verbatim, absorbed
  per FLAG-002): ..."); ijclex011/012 have no EF section (declared).
- THE DEPLOYED RECIPROCITY MAP IS ALREADY FULLY SYMMETRIC (21 pairs,
  0 missing mirrors - a fleet first; PAHC needed 6 added). Every
  deployed pair becomes a typed edge both directions; gate rules:
  presupposes/presupposed-by INVERSE; tension-with/
  associated-with SYMMETRIC; mechanism-behind (the schema enum's own
  word for the communio->primatus EF) answered by an
  associated-with back-edge.
- THE STRAND-VOICE DEVICE (the Plural-Voices parkings): 001 speaks
  Strand A, 002 Strand B, 005 Strand C - voice_surface carries the
  attribution explicitly; the parkings' own caution is kept (a
  lexicon-organization device, NOT a Representative identity
  decision - Step 10's own ground).
- THE RES ABSORPTION (003, 005): the Reported-Experience Status
  parkings stay verbatim in the bodies; their SUBSTANCE now governs
  the confidence dicts (003: single fragmentary source, Registry row
  23 at C -> citation_specificity C, evidentiary_weight qualified;
  005: single-author self-account, one narrow eyewitness corroborant
  -> citation letters carry the thinness; evidentiary_weight stays
  'load-bearing' - the schema enum has no 'qualified' value and these
  single sources ARE each term's whole load-bearing base, which is
  exactly what the RES parkings say; the C/B letters + the RES bodies
  carry the caution).
- original_script only for the Greek-language terms (002, 003, 006,
  010); the Latin terms are already in their own script.
- confidence.formation_confidence from each chunk's own posture
  (CT-bearing terms Contested; others Documented); citation letters
  follow the registry rows the term's sources carry.

In-place update via read/patch/write of the S2.2 records
(front-matter fields added; bodies untouched - the parkings ride).
"""
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
BACKEND = HERE.parents[1]

TERMS = BACKEND / "wrs" / "records" / "imperial_juridical_world" / "term"
VDATE = "2026-07-31"

EF_MARK = "Chunk Ecological Function (verbatim, absorbed per FLAG-002): "

EF = {
 "ijclex001": "*Primatus* is what *communio* protects and what *Tomus* asserts — a participant who understands this term also understands why being cut off from Rome specifically, and not merely from any bishop, carries the particular weight it does in this world's own record, and why a document issued from this specific see (a Tome) carries an authority its own content alone would not fully explain.",
 "ijclex002": "*Presbeia*, grounded in *Nea Rhōmē*'s own political-geographic fact, is the rival claim *primatus* must be understood alongside, never in isolation — a participant who understands this term also understands why this world's own record shows no single, settled answer to the question of which see ranks where, and why *communio* itself becomes contested precisely at the seam between these two claims.",
 "ijclex003": "*Homoios* is what *haeresis* is invoked against in this world's own record, but a participant who understands this term also understands why that invocation is never simple or one-directional here — the same juridical machinery that later condemns this formula once enforced it, and understanding *homoios* honestly is what keeps that history from being flattened into an always-settled contest.",
 "ijclex004": "*Communio* is the mechanism, not merely the topic, behind *primatus* and *presbeia* alike — a participant who understands this term understands that this world's own authority claims are not merely spoken assertions but enforceable through the specific, concrete instrument of who stands in fellowship with whom, and why a see's own decretal or canon carries the weight it does only because communion is the real thing being granted or withheld.",
 "ijclex005": "This formula names the one thing *communio* and *primatus* alone cannot fully account for — a limit on imperial command asserted from inside a single bishop's own sacramental office, not from a see's own accumulated institutional rank; a participant who understands this term understands why this world's own record shows real limits on the alliance between throne and altar even at the height of that alliance's own institutional confidence.",
 "ijclex006": "This term is the doctrinal content our councils and our Tomes exist to defend and assert — it does not organize our own institutional life independently, the way *primatus* or *communio* does, but it is what those institutions repeatedly act to protect.",
 "ijclex007": "The council is the shared mechanism through which *primatus*, *presbeia*, and *haeresis* alike are asserted and contested — it does not organize the ecology independently so much as it is the arena in which the world's own organizing claims are repeatedly brought to trial.",
 "ijclex008": "*Haeresis* is what *homoios* was named as, once our own settlement changed — a participant who understands this term understands that the same juridical machinery that names and excludes was, at another point in this world's own record, the machinery enforcing the very teaching later so named.",
 "ijclex009": "A Tome is *primatus* made into a document — a participant who understands this term understands why a letter's own doctrinal content and the standing of the see that sent it are, in this world's own record, never fully separable.",
 "ijclex010": "*Nea Rhōmē* is the specific geographic-political fact *presbeia*'s own rank-claim rests on — narrower than *presbeia* itself, which it supports rather than stands independently of."
}

CONF = {"citation_specificity": "B",
        "verification_state": "verified-via-authority",
        "verification_date": VDATE,
        "evidentiary_weight": "load-bearing"}


def conf(fc, cite="B", weight="load-bearing"):
    c = dict(CONF)
    c["formation_confidence"] = fc
    c["citation_specificity"] = cite
    c["evidentiary_weight"] = weight
    return c


A = {
 "ijclex001": dict(
  semantic_domain="juridical ecclesiology - see-rank and succession",
  modern_sense=("'Papal primacy' as a settled doctrine with defined "
                "content, or cynically as institutional power-grab dressed "
                "in religion (chunk Modern Hearing: the two registers "
                "assumed separable)."),
  period_sense=("The standing Rome holds because Peter held it first - an "
                "inheritance guarded and defended, where the spiritual "
                "warrant IS the juridical warrant (Damasus and Leo alike); "
                "settled-when-received-at-this-see, not "
                "settled-when-voted."),
  prior_sense=("Latin primatus - 'first place, pre-eminence' generally, a "
               "civic-rank word before its ecclesial narrowing; a builder "
               "note, UNVERIFIED against this build's own docs."),
  grounding_criterion="high",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "Julius's 341 letter (the claim's earliest attested "
                       "instance), Leo's Tome and Canon-28 rejections, "
                       "Damasus's epigraphic corpus - the contested "
                       "decretal block excluded per the chunk's own "
                       "Author-Gravity note (Registry row 15)." + " | DISTANCE: " + "Near-false-friend with the modern 'papacy': "
                            "the claim is real and in-window, its later "
                            "settled form is not - the CT contest rides "
                            "pahc-style ending-not-read-back discipline."),
  confidence=conf("Contested"),
  voice_surface=("STRAND A'S OWN VOICE (the Plural-Voices device - a "
                 "lexicon-organization fact, never a Representative "
                 "identity decision): 'primatus names the standing Rome "
                 "holds because Peter himself held it first here - not an "
                 "honor Rome asks for, but an inheritance Rome guards "
                 "and, where it must, defends.' The rival claim speaks in "
                 "presbeia's own entry, not flattened into agreement "
                 "here."),
  edges=[
   ("tension-with", "ijclex002",
    EF_MARK + EF["ijclex001"] + " The A/B strand contest itself: rank by "
    "apostolic inheritance vs rank by imperial proximity; symmetric both "
    "ways."),
   ("associated-with", "ijclex004",
    "Communio is what protects primatus (the EF's own phrase) - the "
    "juridical instrument behind the claim; symmetric."),
   ("presupposed-by", "ijclex009",
    "A Tome's authority presupposes this see's standing - 'primatus made "
    "into a document'; inverse pair with ijclex009's presupposes."),
   ("associated-with", "ijclex006",
    "The doctrinal content the see's instruments defend (the Tome "
    "carries the homoousian settlement); symmetric."),
   ("tension-with", "ijclex007",
    "The letter vs the council: 'a claim is settled when received at "
    "this see, not when a council votes' - the world's own "
    "story-title tension (The Letter That Outranked a Council); "
    "symmetric."),
   ("tension-with", "ijclex010",
    "New Rome's premise vs old Rome's inheritance - the rank contest's "
    "geographic ground; symmetric."),
   ("associated-with", "ijclex012",
    "The martyr cult as this see's own standing made visible in stone "
    "(Damasus's project); symmetric."),
  ]),
 "ijclex002": dict(
  original_script="πρεσβεῖα",
  semantic_domain="juridical ecclesiology - see-rank by imperial proximity",
  modern_sense=("'Constantinople's honor' heard as empty ceremony or as "
                "naked politics - the religious register assumed "
                "hollow (chunk Modern Hearing)."),
  period_sense=("A see's rank follows the throne it stands beside - New "
                "Rome second because the emperor sits there, 'and that is "
                "reason enough'; the empire's own defense of orthodoxy "
                "itself a religious fact on this strand's own "
                "understanding."),
  prior_sense=("Greek presbeia - 'seniority, precedence, an embassy's "
               "dignity' - the ordinary rank-word Canon 3 puts to "
               "juridical work; a builder note, UNVERIFIED."),
  grounding_criterion="high",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "Canon 3 (381) and Canon 28 (451) as the claim's "
                       "own conciliar form; Leo's rejection as direct "
                       "evidence the claim was contested AT THE TIME (the "
                       "chunk's own CT note)." + " | DISTANCE: " + "The claim survives primarily in conciliar "
                            "acts, not an individual advocate's corpus - "
                            "the chunk's own contrast with primatus; the "
                            "S2.1b Dagron gap rides here."),
  confidence=conf("Contested"),
  voice_surface=("STRAND B'S OWN VOICE (the Plural-Voices device): 'a "
                 "see's rank follows the throne it stands beside - "
                 "Constantinople is second only because it is where the "
                 "emperor now sits, New Rome beside old Rome, and that is "
                 "reason enough.' Neither entry speaks for the world as a "
                 "whole."),
  edges=[
   ("tension-with", "ijclex001",
    EF_MARK + EF["ijclex002"] + " Symmetric mirror of the A/B contest."),
   ("presupposes", "ijclex010",
    "The rank claim rests on the New-Rome premise (the EF's own "
    "'grounded in Nea Rhome's political-geographic fact'); inverse pair "
    "- ijclex010 carries presupposed-by."),
   ("associated-with", "ijclex004",
    "Rank exercised through communion standing - whose fellowship "
    "counts; symmetric."),
   ("associated-with", "ijclex006",
    "The orthodoxy the empire defends is the same settlement both "
    "strands claim to guard; symmetric."),
   ("presupposes", "ijclex007",
    "The claim exists IN canon form - Canon 3, Canon 28: without the "
    "council there is no presbeia claim to cite; inverse pair with "
    "ijclex007."),
  ]),
 "ijclex003": dict(
  original_script="ὅμοιος",
  semantic_domain="doctrinal formula - Trinitarian confession",
  modern_sense=("'Arianism' as an always-heretical fringe safely outside "
                "the church - the flattening the chunk exists to refuse "
                "(chunk Modern Hearing)."),
  period_sense=("The confession that the Son is 'like' the Father without "
                "further claim about shared being - THE EMPIRE'S OWN "
                "CONFESSION for real stretches (Constantius II, Valens), "
                "enforced by the same legal machinery that enforced every "
                "other confession this world held; not a rival always "
                "safely outside."),
  prior_sense=("Greek homoios - the ordinary adjective 'like, similar'; "
               "the Dated Creed (359) is its formula-home; a builder "
               "note, UNVERIFIED."),
  grounding_criterion="standard",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "Auxentius's letter on Ulfila (Registry row 23, "
                       "Confidence C - the ONE near-primary Homoian "
                       "self-testimony, fragmentary) + Hanson's modern "
                       "reconstruction (row 33); the RES parking's own "
                       "single-source honesty governs this record's "
                       "confidence." + " | DISTANCE: " + "'Arian' deliberately NOT an alias (FLAG-035; "
                            "the chunk's own instruction) - the label is "
                            "the flattening, not the referent."),
  confidence=conf("Documented", cite="C"),
  voice_surface=("'A formula our own imperial church itself held, by "
                 "imperial command, for a real stretch of years within "
                 "living memory - not merely a rival teaching we always "
                 "stood safely outside of.' The seriousness of a "
                 "once-enforced confession, never a cartoon."),
  edges=[
   ("tension-with", "ijclex006",
    EF_MARK + EF["ijclex003"] + " The two formulas' direct rivalry - "
    "like-the-Father vs of-one-being; symmetric."),
   ("associated-with", "ijclex008",
    "What haeresis was later invoked against - and what the same "
    "machinery once enforced (the EF's own both-directions point); "
    "symmetric."),
  ]),
 "ijclex004": dict(
  semantic_domain="juridical instrument - fellowship as enforceable status",
  modern_sense=("'Communion' as private spiritual fellowship or the "
                "eucharistic act alone - the institutional force "
                "invisible (chunk Modern Hearing)."),
  period_sense=("To be in communion with a see is to stand where it "
                "stands; being cut off is a public, consequential fact - "
                "the actual instrument by which authority claims become "
                "real rather than merely spoken; juridical and "
                "sacramental inseparably."),
  prior_sense=("Latin communio - 'sharing, mutual participation'; the "
               "ordinary word made a juridical status; a builder note, "
               "UNVERIFIED."),
  grounding_criterion="high",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "Leo's letters (Tome + Canon-28 rejections) using "
                       "communion-standing as the operative category "
                       "throughout - the chunk's own more-securely-"
                       "attested anchor, the contested Damasine decretals "
                       "held aside (row 15)." + " | DISTANCE: " + "The alias 'communion' is a documented "
                            "generic exception (alias_generic_override_"
                            "note; the alexlex022 precedent)."),
  confidence=conf("Documented"),
  voice_surface=("'To be in communion with a see is to stand where that "
                 "see stands; to be cut off from it is not a private "
                 "grief but a public, consequential fact.'"),
  edges=[
   ("mechanism-behind", "ijclex001",
    EF_MARK + EF["ijclex004"] + " The mechanism behind the primacy "
    "claim (the EF's own word)."),
   ("associated-with", "ijclex001",
    "Mirror of ijclex001's associated-with (the reciprocity gate's "
    "symmetric-type rule); the mechanism-behind edge above carries "
    "the substance."),
   ("associated-with", "ijclex002",
    "Symmetric mirror: rank exercised through fellowship-standing."),
   ("associated-with", "ijclex008",
    "The boundary's two sides: communio the inclusion instrument, "
    "haeresis the exclusion instrument - one juridical machinery; "
    "symmetric."),
   ("associated-with", "ijclex005",
    "Communion discipline is the sacramental lever the Ambrosian "
    "formula wields against a crowned communicant; symmetric."),
   ("associated-with", "ijclex009",
    "A Tome's reception IS a communion event - received into "
    "fellowship or refused; symmetric."),
   ("associated-with", "ijclex011",
    "The 386 standoff: the church's own space held as communion-space "
    "against imperial demand; symmetric."),
  ]),
 "ijclex005": dict(
  semantic_domain="church-state boundary formula - sacramental independence",
  modern_sense=("'Separation of church and state' - two institutions kept "
                "apart; exactly what the formula does NOT propose (chunk "
                "Modern/World Hearing)."),
  period_sense=("The emperor stands WITHIN the Church, not above it - "
                "fully inside its life, subject to its discipline as any "
                "believer; the claim is location, not separation: one of "
                "the two, because he stands inside the other, answers to "
                "the altar."),
  prior_sense=("Ambrose's own Latin: 'Imperator enim intra Ecclesiam, non "
               "supra Ecclesiam est' (Sermo contra Auxentium, 386) - the "
               "formula IS the source; wording carried per Registry row "
               "7's own verification note."),
  grounding_criterion="standard",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "Ambrose's own sermon preached during the standoff "
                       "+ Augustine's Confessions 9.7 as narrow eyewitness "
                       "corroboration of the event (the RES parking's own "
                       "single-author honesty governs confidence)." + " | DISTANCE: " + "Strand C does not persist as a claim-stream "
                            "to 451 (Doc_01 SS4's own qualification) - "
                            "bounded, single-crisis evidentiary base."),
  confidence=conf("Documented", cite="B"),
  voice_surface=("STRAND C'S OWN VOICE (the Plural-Voices device - the "
                 "third distinct voice): 'our bishop said this to an "
                 "imperial court demanding a basilica, and meant that no "
                 "crown, however real its power, can command what "
                 "belongs to the altar.'"),
  edges=[
   ("associated-with", "ijclex004",
    EF_MARK + EF["ijclex005"] + " Symmetric mirror: the communion lever."),
   ("associated-with", "ijclex011",
    "The formula and its ground: preached in the contested basilica "
    "during the vigil itself; symmetric."),
  ]),
 "ijclex006": dict(
  original_script="ὁμοούσιος",
  semantic_domain="doctrinal formula - Trinitarian confession",
  modern_sense=("'Consubstantial' as a settled creedal word whose "
                "acceptance was immediate - the decades of resistance "
                "invisible (chunk World Hearing's own counterpoint)."),
  period_sense=("Of one and the same being as the Father - not merely "
                "like him; the word itself remaining genuinely contested, "
                "held, resisted, at times set aside by imperial command, "
                "for decades after first confessed."),
  prior_sense=("Greek homoousios - 'of the same substance/being'; "
               "pre-Nicene history (Paul of Samosata's condemnation "
               "context) is a builder note, UNVERIFIED."),
  grounding_criterion="high",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "Nicaea's own creed (row 9) + Leo's Tome assuming "
                       "and building on the settlement (row 12)." + " | DISTANCE: " + "The CT contest: whether the word's eventual "
                            "victory was doctrinal necessity or imperial "
                            "enforcement is contested between present "
                            "traditions; not resolved here."),
  confidence=conf("Contested"),
  voice_surface=("'We hold the Son to be of one and the same being as "
                 "the Father - not merely like him, but sharing, "
                 "undivided, the very being that makes the Father God.'"),
  edges=[
   ("tension-with", "ijclex003",
    EF_MARK + EF["ijclex006"] + " Symmetric mirror of the formula "
    "rivalry."),
   ("associated-with", "ijclex001",
    "Symmetric mirror: the content the see's instruments defend."),
   ("associated-with", "ijclex002",
    "Symmetric mirror: the settlement both strands claim to guard."),
   ("presupposed-by", "ijclex009",
    "The Tome builds on this settlement (the EF's own 'what those "
    "institutions act to protect'); inverse pair with ijclex009's "
    "presupposes."),
  ]),
 "ijclex007": dict(
  semantic_domain="juridical mechanism - conciliar process",
  modern_sense=("'Church council' as a parliament whose vote settles "
                "matters - reception assumed automatic (chunk World "
                "Hearing's counterpoint)."),
  period_sense=("Where bishops gather under imperial summons to settle "
                "what the whole church must hold - and what a council "
                "settles does not always stay settled: reception by the "
                "sees whose communion matters is a separate, sometimes "
                "withheld, act."),
  prior_sense=("Latin concilium - any convened assembly, civic or "
               "sacred; a builder note, UNVERIFIED."),
  grounding_criterion="high",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "The three conciliar acts rows (9, 10, 11) - the "
                       "world's own initiating, middle, and closing "
                       "councils." + " | DISTANCE: " + "'council' dropped at birth under Rule A - "
                            "the surface rides the confirmed gloss 'a "
                            "council (concilium)'."),
  confidence=conf("Documented"),
  voice_surface=("'A council is where bishops gather, under imperial "
                 "summons, to settle what the whole church must hold - "
                 "and, in our own record, what a council settles does "
                 "not always stay settled.'"),
  edges=[
   ("tension-with", "ijclex001",
    EF_MARK + EF["ijclex007"] + " Symmetric mirror: the "
    "letter-vs-council tension."),
   ("presupposed-by", "ijclex002",
    "Symmetric inverse: the presbeia claim exists in canon form - the "
    "council is its arena."),
   ("associated-with", "ijclex008",
    "Councils are where haeresis is named - the arena's exclusion "
    "verdicts; symmetric."),
   ("tension-with", "ijclex009",
    "The Tome received AT a council yet claiming an authority not "
    "FROM the council - Canon 28's counter-claim is the same tension "
    "from the other side; symmetric."),
  ]),
 "ijclex008": dict(
  semantic_domain="juridical category - doctrinal exclusion",
  modern_sense=("'Heresy' as purely theological error, church-internal - "
                "the legal force invisible (chunk Modern Hearing)."),
  period_sense=("A teaching placed outside what the church AND NOW THE "
                "LAW ITSELF will recognize - theological and "
                "legal-juridical senses simultaneous and mutually "
                "constituting, not sequential."),
  prior_sense=("Greek hairesis - 'choice, school, sect' (the neutral "
               "doxographic sense); Latin haeresis inherits it already "
               "narrowed; a builder note, UNVERIFIED."),
  grounding_criterion="high",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "Theodosian Code Book 16 (the legal use, row 16) + "
                       "the conciliar canons (the doctrinal use, row 9)." + " | DISTANCE: " + "The CT contest: whether law-backed doctrinal "
                            "exclusion was corruption or consolidation "
                            "is a live inter-tradition contest; the "
                            "homoios case keeps the term honest (the "
                            "machinery once enforced what it later "
                            "named)."),
  confidence=conf("Contested"),
  voice_surface=("'Haeresis names a teaching placed outside what the "
                 "church, and now the law itself, will recognize - a "
                 "juridical exclusion as much as a theological one, in "
                 "our own record.'"),
  edges=[
   ("associated-with", "ijclex003",
    EF_MARK + EF["ijclex008"] + " Symmetric mirror of the "
    "enforced-then-condemned honesty."),
   ("associated-with", "ijclex004",
    "Symmetric mirror: the one machinery's two instruments."),
   ("associated-with", "ijclex007",
    "Symmetric mirror: named in the arena."),
  ]),
 "ijclex009": dict(
  semantic_domain="juridical instrument - the doctrinal letter",
  modern_sense=("'Tome' as just a long book; or Leo's Tome as one "
                "theological opinion among many (chunk Modern "
                "Hearing)."),
  period_sense=("A doctrinal letter carrying the full weight of the see "
                "that issues it - what makes a Tome a Tome is the "
                "standing of the issuing see, not its length: the same "
                "words from a see without that standing would not "
                "function the same way."),
  prior_sense=("Greek tomos - 'a cut, a section, a roll of papyrus'; the "
               "bookish sense the modern ear keeps; a builder note, "
               "UNVERIFIED."),
  grounding_criterion="high",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "Leo's Tome to Flavian (row 12) and its Chalcedon "
                       "reception - with the Canon-28 non-reception as "
                       "the same event's other half (rows 11, 13)." + " | DISTANCE: " + "The reception/non-reception split IS the "
                            "world's closing open question - the "
                            "ending-not-read-back discipline rides every "
                            "use."),
  confidence=conf("Documented"),
  voice_surface=("'A Tome is a doctrinal letter carrying the full weight "
                 "of the see that issues it - ours went ahead of us to "
                 "Chalcedon and was received there as though we "
                 "ourselves had spoken.'"),
  edges=[
   ("presupposes", "ijclex001",
    EF_MARK + EF["ijclex009"] + " 'Primatus made into a document' - "
    "inverse pair with ijclex001's presupposed-by."),
   ("presupposes", "ijclex006",
    "The Tome assumes and builds on the homoousian settlement; inverse "
    "pair with ijclex006's presupposed-by."),
   ("associated-with", "ijclex004",
    "Symmetric mirror: reception as communion event."),
   ("tension-with", "ijclex007",
    "Symmetric mirror: received at the council, authority not from "
    "it."),
  ]),
 "ijclex010": dict(
  original_script="Νέα Ῥώμη",
  semantic_domain="political-geographic premise - the new capital",
  modern_sense=("'Byzantium/Istanbul trivia' - a renaming; the juridical "
                "work the name does invisible (chunk Modern Hearing)."),
  period_sense=("'We are New Rome - not old Rome's rival, but old Rome's "
                "own successor in the place where the empire itself now "
                "actually governs' - the stated premise of a real, "
                "contested juridical claim (Canon 3, Canon 28), not "
                "decoration."),
  prior_sense=("Constantinople dedicated 330 as Constantine's capital; "
               "the name's official standing vs honorific currency is a "
               "builder note, UNVERIFIED."),
  grounding_criterion="high",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "Canon 3 (row 10) and Canon 28 (row 11) - the "
                       "claim's own two canonical instances." + " | DISTANCE: " + "Narrower than presbeia, which it supports "
                            "rather than stands independently of (the "
                            "EF's own scoping)."),
  confidence=conf("Documented"),
  voice_surface=("'We are New Rome - not old Rome's rival, but old "
                 "Rome's own successor in the place where the empire "
                 "itself now actually governs.'"),
  edges=[
   ("presupposed-by", "ijclex002",
    EF_MARK + EF["ijclex010"] + " Inverse pair with presbeia's "
    "presupposes."),
   ("tension-with", "ijclex001",
    "Symmetric mirror: the geographic ground of the rank contest."),
  ]),
 "ijclex011": dict(
  semantic_domain="material culture - contested sacred space",
  modern_sense=("'Basilica' as an architectural style term or any big "
                "church (chunk Modern Hearing)."),
  period_sense=("Not only a building - the physical ground on which the "
                "question of who commands the church's own space, "
                "emperor or bishop, was actually fought and, that night "
                "in 386, held."),
  prior_sense=("Roman civic basilica - the law-court/market hall form "
               "adapted for Christian assembly; a builder note, "
               "UNVERIFIED."),
  grounding_criterion="high",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "The Milan basilica complex itself (row 38) + Old "
                       "St. Peter's as the alliance's monumental "
                       "expression (row 37) - material rows; the standoff "
                       "texts ride ijclex005's sources (the S2.2 "
                       "source-defaults declaration)." + " | DISTANCE: " + "No Key Sources section by design - "
                            "material-culture evidence class (S2.1a)."),
  confidence=conf("Documented"),
  voice_surface=("'For us, a basilica is not only a building - it is the "
                 "physical ground on which the question of who commands "
                 "the church's own space, emperor or bishop, was "
                 "actually fought and, that night, held.'"),
  edges=[
   ("associated-with", "ijclex005",
    "Symmetric mirror: the sermon and its ground (no chunk EF by "
    "design - S2.2 declaration)."),
   ("associated-with", "ijclex004",
    "Symmetric mirror: communion-space against imperial demand."),
  ]),
 "ijclex012": dict(
  semantic_domain="material culture - martyr cult as institution",
  modern_sense=("'Martyr shrine' as devotional site only - the "
                "institutional work invisible (chunk Modern Hearing)."),
  period_sense=("Where the dead who kept the faith under persecution are "
                "honored - and, in this see's hands specifically, where "
                "that honor is made to speak for the see's own standing: "
                "folded into and largely subordinate to the "
                "primacy-claiming project."),
  prior_sense=("Greek martyrion - 'testimony, witness'; the "
               "building-sense (shrine over a martyr's grave) is late "
               "antique; a builder note, UNVERIFIED."),
  grounding_criterion="high",
  conceptual_distance_note=("GROUNDING (the enum's free-text companion, carried here): " + "Damasus's epigraphic corpus (row 14, P/M hybrid "
                       "carried verbatim) - the martyr cult as "
                       "institutional self-presentation." + " | DISTANCE: " + "A DIFFERENT WEIGHTING than a world where "
                            "martyr-cult is itself the organizing center "
                            "(the chunk's own cross-world caution - the "
                            "PAHC/Desert contrast lives here)."),
  confidence=conf("Documented"),
  voice_surface=("'A martyr's shrine is where the dead who kept the "
                 "faith under persecution are honored - and, in our own "
                 "see's hands specifically, where that honor is also "
                 "made to speak for this see's own standing.'"),
  edges=[
   ("associated-with", "ijclex001",
    "Symmetric mirror: the standing made visible in stone (no chunk EF "
    "by design - S2.2 declaration)."),
  ]),
}


def read_record(path: Path):
    txt = path.read_text(encoding="utf-8")
    assert txt.startswith("---\n")
    front, sep, body = txt[4:].partition("\n---\n")
    assert sep
    return yaml.safe_load(front), body


def write_record(path: Path, front: dict, body: str):
    fy = yaml.safe_dump(front, sort_keys=False, allow_unicode=True,
                        width=100)
    path.write_text(f"---\n{fy}---\n{body}", encoding="utf-8",
                    newline="\n")


def main():
    n_edges = 0
    for rid, a in A.items():
        path = TERMS / f"{rid}.md"
        front, body = read_record(path)
        for k in ("original_script", "semantic_domain", "modern_sense",
                  "period_sense", "prior_sense", "grounding_criterion",
                  "conceptual_distance_note", "confidence",
                  "voice_surface"):
            if k in a:
                front[k] = a[k]
        front["field_relations"] = [
            {"type": t, "target_id": tid, "note": note}
            for t, tid, note in a["edges"]]
        n_edges += len(a["edges"])
        front["contested_claim_ids"] = []
        write_record(path, front, body)
    print(f"12 term records authored: senses/confidence/voice/"
          f"{n_edges} typed edges (21 symmetric pairs, the deployed "
          f"map complete)")


if __name__ == "__main__":
    main()
