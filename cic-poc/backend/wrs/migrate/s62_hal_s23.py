"""S6.2/HAL - S2.3-equivalent: term authoring (single batch; 15 terms).

Adds the authored fields onto the S2.2 mechanical records: senses
(period/prior/modern + conceptual_distance_note), semantic_domain,
grounding_criterion, voice_surface, confidence block, and typed
field_relations. Ports the SYR s62_syr_s23.py pattern. Conventions:

- FLAG-023 fence-asserting reader; FLAG-002 chunk-EF-verbatim on the
  FIRST field_relations edge note (extracted at run time).
- NO original_script field for this world, DECLARED: the terms are
  Latin in Latin script - the `term` field IS the original; the three
  Greek etyma (nosocomium, monachus, grammaticus) are named as Greek
  loans in prose where the chunks themselves say so, but no Greek-script
  form is fabricated (none appears in this build's own docs).
- THE STEP-3 REQUIREMENT (addendum SS4.4/SS8.2): the 13 HAL
  confirmed-gloss originals are read IN VIEW at authoring - GLOSS_MAP
  below records the original -> record-id resolution, and main()
  ASSERTS it against the live CONFIRMED_GLOSSES and the live term
  fields, so the future term_id backfill is a mechanical read of this
  table. 12 of 13 resolve 1:1; the B-category circumlocution ('the
  month named for the harvest' -> 'August') has NO term record BY
  DESIGN - it is a Facilitator-phrase gloss, not a lexicon term.
- prior_sense honesty: 'none-attested' is an answer; builder inferences
  beyond the build docs carry an explicit UNVERIFIED flag.
- formation_confidence: the Article-17 enum, per-term, from each
  chunk's own confidence language.
- hallex15 (Monachus) carries NO field_relations: both of its
  front-matter Related-Terms (Monasterium duplex, Praeceptor) name
  never-built terms - the ALX not-yet-built-partner class, declared
  here and in the checkpoint, not silently dropped. Same for the
  Xenodochium references on hallex03/14 and Praeceptor on hallex12.
  Its parked EF stays in world_meaning (no first edge to ride).
- hal_lex11's single-source discipline gets its authored home here:
  the Marcella standing rests on Jerome's own memorial letter (Ep.
  127) - a single-voice source, srcHAL001's Marcella-list caveat and
  srcHAL012's unverified-pairing flag both bearing on it; carried in
  period_sense + confidence, with the parked Reported-Experience
  Status text remaining verbatim in the record body.

Relation map (each note grounded in the citing chunk's own text;
INVERSE mirrored typed, SYMMETRIC mirrored same-type,
material-source-of backed by presupposes - the Desert pairing):
  02 presupposes 01          (the project is the principle's material product)
  01 presupposes 13          (the prefaces are where the principle is argued)
  13 material-source-of 01   (+ presupposed-by mirror)
  01 presupposes 12          (grammar training under the philological labor)
  02 assoc 13 (sym)          (nearly every translated book carried its preface)
  02 assoc 07 (sym)          (dedications/covering letters, book by book)
  03 material-source-of 06   (+ mirrors: 06 presupposes 03)
  14 presupposes 03          (the hospital presupposes renounced wealth)
  03 assoc 04, 03 assoc 05, 04 assoc 05 (sym; formation categories)
  03 presupposes 10, 06 presupposes 10  (matrona standing = precondition)
  06 assoc 07 (sym)          (patronage conducted through letters)
  11 presupposes 05          (the standing exercised from within vidua)
  11 tension-with 06 (sym)   (the one Tensional gravity's counter-current)
  11 assoc 07 (sym)          (clergy bring questions; direction by letter)
  07 assoc 01 (sym)          (the Augustine exchange conducted by letter)
  08 assoc 01, 08 assoc 06, 08 assoc 09 (sym; the controversies)
"""
import sys
from pathlib import Path
import re

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))

TERM_DIR = BACKEND / "wrs" / "records" / "hieronymian_world" / "term"
CHUNKS = BACKEND / "data" / "hieronymian_world" / "lexicon_chunks"

VDATE = "2026-07-31"

# The Step-3 in-view table: confirmed-gloss original -> term record id.
# None = no term record BY DESIGN (Facilitator-phrase circumlocution).
GLOSS_MAP = {
    "Vulgata": "hallex02",
    "the month named for the harvest": None,
    "Hebraica veritas": "hallex01",
    "Renuntiatio": "hallex03",
    "Virginitas": "hallex04",
    "Vidua": "hallex05",
    "Patrocinium": "hallex06",
    "Epistula": "hallex07",
    "Matrona": "hallex10",
    "Grammaticus": "hallex12",
    "Praefatio": "hallex13",
    "Nosocomium": "hallex14",
    "Monachus": "hallex15",
}


def read_record(path: Path):
    """FLAG-023 fence-asserting reader."""
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), path
    rest = text[4:]
    front, sep, body = rest.partition("\n---\n")
    assert sep, path
    return yaml.safe_load(front), body


def write_record(path: Path, front: dict, body: str):
    fy = yaml.safe_dump(front, sort_keys=False, allow_unicode=True,
                        width=100, default_flow_style=False)
    path.write_text(f"---\n{fy}---\n{body}", encoding="utf-8")


def chunk_ef(chunk_name: str) -> str:
    text = (CHUNKS / chunk_name).read_text(encoding="utf-8")
    m = re.search(r"^## Ecological Function\s*\n(.*?)(?=^## |\Z)",
                  text, re.S | re.M)
    if not m:
        return ""
    return re.sub(r"^-{3,}\s*$", "", m.group(1), flags=re.M).strip()


def ef_note(lead: str, chunk_name: str) -> str:
    ef = chunk_ef(chunk_name)
    assert ef, chunk_name
    return (lead + " Chunk Ecological Function (verbatim, absorbed per "
            "FLAG-002): " + ef)


AUTH = {
    "hallex01": {
        "period_sense": (
            "The conviction that the Hebrew text of scripture, not the "
            "long-used Greek, carries the truth closest to what God said - "
            "held not as neutral method but as a costly, actively contested "
            "commitment: it meant years with a Hebrew teacher outside the "
            "faith, telling congregations that a familiar word was now "
            "another, and answering, repeatedly, the charge of tampering "
            "with what the church already trusted (chunk Quick/World "
            "Meaning)."),
        "prior_sense": (
            "The contrast object is the church's own received practice: the "
            "Greek translation 'long used in Latin worship' - venerable, "
            "loved, constantly quoted - whose authority the phrase "
            "deliberately relativizes (chunk World Meaning). As a fixed "
            "two-word phrase it is this world's own polemical coinage, not "
            "a transformed inheritance - a builder note, UNVERIFIED against "
            "this build's own docs, which do not develop the phrase's "
            "history."),
        "modern_sense": (
            "'Of course you translate from the original language' - heard "
            "as a straightforwardly correct scholarly method, with the "
            "period resistance filed under ignorance or reaction (chunk "
            "Modern Hearing)."),
        "conceptual_distance_note": (
            "The modern ear hears settled method; this world heard a claim "
            "with real stakes for the church's continuity - serious "
            "churchmen (Augustine) resisted it for serious reasons, and "
            "adopting it meant conceding that the text the whole Latin "
            "church prayed from had drifted from its source (chunk World "
            "Hearing). Sharp gap: high grounding criterion by rule."),
        "semantic_domain": "hebrew-textual-authority",
        "grounding_criterion": "high",
        "voice_surface": (
            "To hold to the Hebrew truth is to believe that when the word "
            "passed from Hebrew into Greek, something of its precision was "
            "lost - and that a scholar who returns to the Hebrew recovers "
            "what the Greek, however venerable, cannot fully carry. We did "
            "not hold this comfortably. It cost us a teacher hired from "
            "outside our faith, the anger of congregations over a gourd "
            "become a vine, and the standing charge of tampering with what "
            "the church already trusted."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Widely Accepted",
        },
        "relations": [
            {"type": "presupposed-by", "target_id": "hallex02",
             "note_ef": ("The translation project is this principle's "
                         "material product (hal_lex02's own EF: 'The "
                         "material product of Hebraica veritas')."),
             "chunk": "hal_lex01_hebraica-veritas.md"},
            {"type": "presupposes", "target_id": "hallex13",
             "note": ("The prefaces are 'where the Hebraica veritas "
                      "commitment is actually argued, book by book, not "
                      "merely asserted' (hal_lex13 World Meaning) - the "
                      "Desert material-source-of/presupposes pairing; "
                      "srcHAL023 is the corpus row.")},
            {"type": "presupposes", "target_id": "hallex12",
             "note": ("The classical grammar training 'is what made the "
                      "later philological labor possible at all' (hal_lex12 "
                      "World Meaning) - the documented foundation under the "
                      "contested Hebrew-fluency claims.")},
            {"type": "associated-with", "target_id": "hallex07",
             "note": ("The Augustine dispute over this principle was "
                      "'conducted' as letters (hal_lex07 World Meaning: 'a "
                      "furious exchange with a former friend turned "
                      "theological opponent'; srcHAL009) - association, no "
                      "hierarchy (CO-P2-13 pattern); symmetric mirror on "
                      "hallex07.")},
            {"type": "associated-with", "target_id": "hallex08",
             "note": ("Symmetric mirror of hallex08's edge: the Origenist "
                      "rupture 'reshapes the Hebraica veritas project' "
                      "(hal_lex08 EF) - the Augustine dispute is its "
                      "downstream test.")},
        ],
    },
    "hallex02": {
        "period_sense": (
            "A decades-long working project, not a finished thing: the "
            "Gospels revised in Rome under papal commission, then at "
            "Bethlehem the Hebrew scriptures rendered afresh book by book, "
            "each with its own defending preface - still contested, still "
            "incomplete in parts, within this world's own span. The name "
            "'the Vulgate' and the standard-text status belong to a much "
            "later church (chunk Quick/World Meaning)."),
        "prior_sense": (
            "The ordinary Latin vulgatus, 'common, widespread, publicly "
            "known' - the surface the much later name applies; within this "
            "world's span the project had no such settled name at all - a "
            "builder note, UNVERIFIED against this build's own docs, which "
            "carry only the anachronism flag itself."),
        "modern_sense": (
            "'The Vulgate' assumed to exist within this world's own time "
            "as an already-standard, church-wide text (chunk Modern "
            "Hearing)."),
        "conceptual_distance_note": (
            "A retrojection gap in the memra/Catholicos class: the finished "
            "name and status are read back onto an ongoing, partial, "
            "contested labor - one translator's project, defended preface "
            "by preface, not yet anyone's standard (chunk World Hearing). "
            "Standard grounding: the correction is a dating/status guard, "
            "and the record's own alias set is empty for exactly this "
            "reason (the S2.2 FLAG-028 resolution; reachability = term key "
            "'vulgata')."),
        "semantic_domain": "translation-project",
        "grounding_criterion": "standard",
        "voice_surface": (
            "What later ages call the Vulgate was, with us, a labor still "
            "under way - the Gospels corrected in Rome under Damasus, then "
            "book after book of the Hebrew scriptures at Bethlehem, each "
            "sent out with its own preface answering the objections we "
            "knew would come. We did not have a finished Bible; we had a "
            "working life."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "presupposes", "target_id": "hallex01",
             "note_ef": ("The organizing commitment behind the whole "
                         "project (hal_lex01 EF names Vulgata as what "
                         "Hebraica veritas organizes)."),
             "chunk": "hal_lex02_vulgata.md"},
            {"type": "associated-with", "target_id": "hallex13",
             "note": ("Nearly every translated book 'came with its own "
                      "short, combative essay attached' (hal_lex13 World "
                      "Meaning) - the prefaces travel inside the project's "
                      "volumes (srcHAL023's containment relation) - "
                      "association, no hierarchy.")},
            {"type": "associated-with", "target_id": "hallex07",
             "note": ("The project was 'dedicated, book by book, to the "
                      "women who requested and funded it' (this chunk's "
                      "EF) - the dedications and covering letters are "
                      "epistulae; symmetric mirror on hallex07.")},
        ],
    },
    "hallex03": {
        "period_sense": (
            "A sustained public unmaking of one's former position, not a "
            "single private gesture: property sold or redirected, marriage "
            "prospects closed, plain dress announcing the change to a Rome "
            "that judged - praised by the church and sometimes suspected "
            "of excess, with grief and material need following those who "
            "gave the most (chunk Quick/World Meaning)."),
        "prior_sense": (
            "The ordinary Latin renuntiatio - a formal announcement of "
            "withdrawal, the giving-up of an office or claim - the civic "
            "surface the ascetic use specializes; a builder note, "
            "UNVERIFIED against this build's own docs."),
        "modern_sense": (
            "A private spiritual discipline, comparable to modern "
            "voluntary simplicity or minimalism (chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "The modern frame is private lifestyle choice; this world's "
            "renunciation was public, family-disrupting, and socially "
            "contested, with real material and relational costs - a "
            "senator's daughter was SEEN to renounce (chunk World "
            "Hearing). Sharp gap: high grounding criterion by rule."),
        "semantic_domain": "wealth-renunciation",
        "grounding_criterion": "high",
        "voice_surface": (
            "To renounce among us was not to simplify one's life; it was "
            "to unmake one's place. The land sold or turned to other "
            "hands, the marriage that would have bound two houses "
            "declined, the plain dress that told everyone who had known "
            "you before that something fundamental had changed - all of "
            "it public, all of it judged, and for those who gave the "
            "most, grief and want followed."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Widely Accepted",
        },
        "relations": [
            {"type": "material-source-of", "target_id": "hallex06",
             "note_ef": ("Renounced wealth is what a patron sustains a "
                         "scholar's work WITH - 'the material source of "
                         "patrocinium' in this chunk's own EF words."),
             "chunk": "hal_lex03_renuntiatio.md"},
            {"type": "presupposed-by", "target_id": "hallex06",
             "note": ("Mirror of hallex06's presupposes edge (the Desert "
                      "material-source-of/presupposes pairing).")},
            {"type": "presupposed-by", "target_id": "hallex14",
             "note": ("Mirror of hallex14's presupposes edge: this chunk's "
                      "EF names renuntiatio as 'presupposed by "
                      "xenodochium and nosocomium'. NOTE: the xenodochium "
                      "half of that EF sentence names a never-built term - "
                      "the not-yet-built-partner class, declared, no edge "
                      "possible.")},
            {"type": "associated-with", "target_id": "hallex04",
             "note": ("This chunk's EF: 'central to virginitas and vidua "
                      "as their practical expression' - association, no "
                      "hierarchy (the categories are formation states, "
                      "renunciation their enacted form).")},
            {"type": "associated-with", "target_id": "hallex05",
             "note": ("Same EF sentence, the vidua half - the "
                      "second-half-of-life renunciation 'chosen again' "
                      "(hal_lex05 World Meaning); symmetric both ways.")},
            {"type": "presupposes", "target_id": "hallex10",
             "note": ("Matrona standing 'is precisely what made "
                      "large-scale renunciation possible at all' "
                      "(hal_lex10 World Meaning) - the social-historical "
                      "precondition.")},
        ],
    },
    "hallex04": {
        "period_sense": (
            "Consecrated, lifelong sexual continence held as the highest "
            "form of Christian formation available to a woman - understood "
            "as a foretaste of the redeemed life, defended with sharp "
            "rhetorical force against marriage itself, and provoking real "
            "controversy even within the household that most prized it "
            "(chunk Quick/World Meaning)."),
        "prior_sense": (
            "The ordinary Latin status word for maidenhood - a condition, "
            "not a vocation; the consecrated, eschatological sense is "
            "this world's own specialization - a builder note, UNVERIFIED "
            "against this build's own docs."),
        "modern_sense": (
            "Straightforward, uncontroversial praise of celibacy (chunk "
            "Modern Hearing)."),
        "conceptual_distance_note": (
            "The modern ear hears gentle counsel; this world's advocacy "
            "was a genuinely severe, contested rhetorical position that "
            "drew criticism in its own time for its harshness toward "
            "marriage (chunk World Hearing). Sharp gap: high grounding "
            "criterion by rule."),
        "semantic_domain": "consecrated-virginity",
        "grounding_criterion": "high",
        "voice_surface": (
            "Virginity with us was not the absence of marriage but a "
            "state nearer to what the redeemed life will finally be - a "
            "foretaste kept now. To choose it was to choose against the "
            "shape a senatorial daughter's life was expected to take, and "
            "we defended the choice with words sharp enough that even our "
            "own household flinched."),
        "confidence": {
            "citation_specificity": "A",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "associated-with", "target_id": "hallex03",
             "note_ef": ("Symmetric mirror of hallex03's edge: "
                         "renunciation is this state's practical "
                         "expression (hal_lex03 EF)."),
             "chunk": "hal_lex04_virginitas.md"},
            {"type": "associated-with", "target_id": "hallex05",
             "note": ("This chunk's EF: 'Distinguishes Eustochium's "
                      "formation category from Paula's, Marcella's, and "
                      "Fabiola's (vidua)' - sister formation categories, "
                      "deliberately kept distinct; symmetric both ways.")},
        ],
    },
    "hallex05": {
        "period_sense": (
            "The status of a Christian widow who declines remarriage - "
            "against real family and social pressure, sometimes a "
            "specific suitor - and takes up fasting, plain dress, and in "
            "at least one case recognized scriptural authority within her "
            "own household; a deliberate turning-away from a life already "
            "lived once, with continentia inseparable from the status "
            "itself (chunk Quick/World Meaning)."),
        "prior_sense": (
            "The ordinary Latin vidua, simply 'widow' - a bereavement "
            "status, not a vocation; the vowed-ascetic specialization is "
            "this world's own - a builder note, UNVERIFIED against this "
            "build's own docs."),
        "modern_sense": (
            "Widowed continence as a lesser, merely-negative absence of "
            "remarriage (chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "The modern frame reads absence; this world saw an actively "
            "chosen ascetic vocation with its own discipline and, for at "
            "least one of these women, real recognized standing (chunk "
            "World Hearing). The gap is real but the corrective is a "
            "category upgrade, not a participation/representation chasm: "
            "standard grounding."),
        "semantic_domain": "ascetic-widowhood",
        "grounding_criterion": "standard",
        "voice_surface": (
            "A widow among us who refused the second marriage her family "
            "pressed on her was not declining a life; she was choosing "
            "one - fasting, plain dress, the discipline of self-mastery "
            "lived out in a particular house. Not virginity's lifelong "
            "abstention from the start, but a turning-away chosen in "
            "life's second half, and its own real vocation."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Widely Accepted",
        },
        "relations": [
            {"type": "associated-with", "target_id": "hallex03",
             "note_ef": ("Symmetric mirror of hallex03's edge: "
                         "renunciation as this category's practical "
                         "expression, second-half-of-life form."),
             "chunk": "hal_lex05_vidua.md"},
            {"type": "associated-with", "target_id": "hallex04",
             "note": ("Symmetric mirror of hallex04's edge: the "
                      "distinguished sister formation categories "
                      "(Eustochium's vs Paula's/Marcella's/Fabiola's).")},
            {"type": "presupposed-by", "target_id": "hallex11",
             "note": ("Mirror of hallex11's presupposes edge: this "
                      "chunk's own EF - 'Marcella's specific standing "
                      "(see exegesis-as-practiced-authority) is exercised "
                      "from within this category, not virginity.'")},
        ],
    },
    "hallex06": {
        "period_sense": (
            "The voluntary, wealth-based relationship by which an "
            "aristocratic patron sustains a scholar's work - this world's "
            "ACTUAL authority structure, standing in place of church "
            "office: a presbyter's whole labor depending on whether a "
            "widow's fortune continued to back him, leaving him genuinely "
            "vulnerable when papal favor died and rumor turned (chunk "
            "Quick/World Meaning)."),
        "prior_sense": (
            "The standard Roman patron-client institution - patrocinium "
            "as the empire's ordinary machinery of protection and "
            "obligation - which this world inherits whole and turns to "
            "the sustaining of scholarship; the chunk's own framing "
            "presents the Christian use as a redirection of a thoroughly "
            "Roman form, not an invention."),
        "modern_sense": (
            "'Patronage' as a minor financial detail, secondary to the "
            "'real' spiritual or scholarly authority (chunk Modern "
            "Hearing)."),
        "conceptual_distance_note": (
            "The modern ear demotes funding to background; this world's "
            "patronage WAS the authority structure - not funding FOR "
            "authority but the actual substance of it (chunk World "
            "Hearing, near-verbatim). Sharp gap: high grounding "
            "criterion by rule."),
        "semantic_domain": "patronage-authority",
        "grounding_criterion": "high",
        "voice_surface": (
            "Ask where authority lived among us and the honest answer is "
            "not a bishop's seat. It lived in trust and in wealth freely "
            "given - a scholar's travel, his Hebrew teacher, the roofs "
            "over his community, all resting on whether a widow's "
            "fortune continued to back him. When the pope who favored "
            "him died and rumor turned, he had no office to fall back "
            "on; only reputation, and a patron's continued goodwill."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Widely Accepted",
        },
        "relations": [
            {"type": "presupposes", "target_id": "hallex03",
             "note_ef": ("Renounced wealth is this relationship's "
                         "material source (hal_lex03 EF; the Desert "
                         "material-source-of/presupposes pairing)."),
             "chunk": "hal_lex06_patrocinium.md"},
            {"type": "presupposes", "target_id": "hallex10",
             "note": ("Matrona standing is the precondition - 'the "
                      "social-historical precondition for renunciation "
                      "and patronage' (hal_lex10 EF).")},
            {"type": "associated-with", "target_id": "hallex07",
             "note": ("The patronage relationship was conducted across "
                      "the Rome/Bethlehem split by letter (hal_lex07 "
                      "World Meaning: direction, argument, and "
                      "community-maintenance delivered as epistulae) - "
                      "association, no hierarchy; symmetric mirror on "
                      "hallex07.")},
            {"type": "associated-with", "target_id": "hallex08",
             "note": ("Symmetric mirror of hallex08's edge: the "
                      "Origenist controversy was 'conducted through, and "
                      "threatening, the patronage network' (hal_lex08 "
                      "EF).")},
            {"type": "tension-with", "target_id": "hallex11",
             "note": ("Symmetric mirror of hallex11's edge: the one "
                      "Tensional gravity's counter-current - authority "
                      "held through demonstrated learning apart from "
                      "both office AND wealth, 'a difference in "
                      "position' within the ecology this term "
                      "organizes (hal_lex11 EF).")},
        ],
    },
    "hallex07": {
        "period_sense": (
            "The letter as this world's actual formation apparatus, not "
            "its paperwork: when the scholar and the household he "
            "directed no longer shared a city, spiritual direction, "
            "scriptural argument, and the community's own oneness were "
            "delivered and maintained as epistulae - a hard letter of "
            "exhortation, a commentary under a covering dedication, a "
            "furious exchange with a former friend (chunk Quick/World "
            "Meaning)."),
        "prior_sense": (
            "The ordinary Latin epistula, the empire's everyday letter - "
            "news, business, maintained relationships across distance; "
            "the formation-medium sense is this world's own "
            "intensification of a completely ordinary form - a builder "
            "note, UNVERIFIED against this build's own docs."),
        "modern_sense": (
            "Letters as secondary evidence ABOUT the community's life - "
            "a documentary window onto formation happening elsewhere "
            "(chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "The modern ear files the letters under sources; this world "
            "lived them as events - 'the letter was itself a formation "
            "event, not a report of one' (chunk World Hearing, "
            "verbatim). Sharp gap: high grounding criterion by rule. "
            "The record's alias set is empty by the S2.2 FLAG-028 "
            "resolution ('letter' is a bare blocklist generic); "
            "reachability = term key 'epistula'."),
        "semantic_domain": "epistolary-formation",
        "grounding_criterion": "high",
        "voice_surface": (
            "When Rome and Bethlehem could no longer hear each other's "
            "voices, the letter became the room we met in. Direction "
            "was given there, scripture argued there, a community "
            "physically split in two remained one project there. A hard "
            "letter of exhortation was not news about our formation; it "
            "was the formation itself, arriving sealed."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "associated-with", "target_id": "hallex02",
             "note_ef": ("Symmetric mirror of hallex02's edge: the "
                         "translation project's dedications, book by "
                         "book, are epistulae."),
             "chunk": "hal_lex07_epistula.md"},
            {"type": "associated-with", "target_id": "hallex06",
             "note": ("Symmetric mirror of hallex06's edge: patronage "
                      "conducted by letter across the bipolar "
                      "geography this chunk's EF says the genre "
                      "'bridges by definition'.")},
            {"type": "associated-with", "target_id": "hallex01",
             "note": ("Symmetric mirror of hallex01's edge: the "
                      "Augustine exchange over textual authority was "
                      "conducted as letters (srcHAL009).")},
            {"type": "associated-with", "target_id": "hallex11",
             "note": ("Symmetric mirror of hallex11's edge: exegetical "
                      "direction at distance rode this medium - 'how an "
                      "argument about scripture was actually conducted' "
                      "(this chunk's World Meaning).")},
        ],
    },
    "hallex08": {
        "period_sense": (
            "The 390s dispute over Origen's teachings as this world "
            "actually underwent it: a community that had inherited much "
            "of its way of reading scripture from a teacher whose "
            "specific conclusions it then renounced urgently and "
            "publicly - a former translating-partner become fiercest "
            "opponent, a bishop to be maneuvered against, and at stake "
            "'which teacher's account of Jerome's own faithfulness "
            "would be believed' (chunk Quick/World Meaning)."),
        "prior_sense": (
            "The inherited debt itself is the prior: this world's own "
            "exegetical method carried Origen's stamp before the "
            "renunciation - 'inherited, without quite meaning to, a "
            "good deal of its own way of reading scripture' (chunk "
            "World Meaning) - so the controversy's prior sense is the "
            "unproblematic teacher the name later made dangerous."),
        "modern_sense": (
            "A purely abstract theological disagreement - souls, "
            "resurrection bodies - with the personal and political "
            "stakes trimmed away (chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "The rupture was 'simultaneously doctrinal, personal, and "
            "political - the three were not separable within it' (chunk "
            "World Hearing, verbatim). The corrective is a "
            "reintegration of dimensions, not a lived-concept reversal: "
            "standard grounding. The chunk's CT Contest Type section "
            "stays parked in this record's body for the S2.6 claims.")
        ,
        "semantic_domain": "origenist-controversy",
        "grounding_criterion": "standard",
        "voice_surface": (
            "We had learned to read scripture, more than we liked to "
            "admit, from a teacher whose conclusions we then had to "
            "renounce - publicly, urgently, while a friend who had once "
            "translated beside us became the fiercest voice against us. "
            "The quarrel was never only doctrine. It was about which "
            "account of our own faithfulness would be believed."),
        "confidence": {
            "citation_specificity": "A",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "associated-with", "target_id": "hallex09",
             "note_ef": ("The two controversies anchor G6 together "
                         "(hal_lex09 EF: 'Anchors G6 alongside "
                         "Origenism') - association, no hierarchy."),
             "chunk": "hal_lex08_origenism.md"},
            {"type": "associated-with", "target_id": "hallex01",
             "note": ("This chunk's EF: the controversy 'reshapes the "
                      "Hebraica veritas project (the Augustine dispute "
                      "is a downstream test of related textual-"
                      "authority commitments)'.")},
            {"type": "associated-with", "target_id": "hallex06",
             "note": ("This chunk's EF: 'conducted through, and "
                      "threatening, the patronage network - Pammachius "
                      "and Marcella are named addressees of Jerome's "
                      "own polemic.'")},
        ],
    },
    "hallex09": {
        "period_sense": (
            "The dispute over grace, free will, and human capacity for "
            "sinlessness as this world underwent it in 416: not an "
            "argument won or lost on paper but a mob at the Bethlehem "
            "monastery's own doors - buildings burned and, by report, "
            "at least one member of the community dead (chunk "
            "Quick/World Meaning; the 'by report' qualifier is the "
            "chunk's own and is preserved, not firmed up)."),
        "prior_sense": (
            "none-attested - a dispute-name, not an inherited concept; "
            "the record register is the event and its pressure on this "
            "world's final years, not a transformed prior sense."),
        "modern_sense": (
            "An abstract soteriological dispute - grace versus free "
            "will - disconnected from real-world consequence (chunk "
            "Modern Hearing)."),
        "conceptual_distance_note": (
            "This world experienced the controversy, at least once, as "
            "physical violence at its own door (chunk World Hearing) - "
            "an ending-adjacent external force on the community's last "
            "years, not a seminar topic. Standard grounding: the "
            "corrective restores consequence, not a different concept."),
        "semantic_domain": "pelagian-controversy",
        "grounding_criterion": "standard",
        "voice_surface": (
            "In the year 416 the argument stopped being an argument. "
            "Whatever mixture of conviction and grievance had gathered "
            "around the dispute came to our own doors: the monastery "
            "attacked, buildings burned, and - as it was reported - "
            "one of our own dead. We knew this controversy not as a "
            "debate to be won but as a danger that had found where we "
            "lived."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "associated-with", "target_id": "hallex08",
             "note_ef": ("Symmetric mirror of hallex08's edge: joint "
                         "G6 anchors, the two controversies pressing "
                         "on this world from outside."),
             "chunk": "hal_lex09_pelagianism.md"},
        ],
    },
    "hallex10": {
        "period_sense": (
            "The Roman aristocratic status category - inherited wealth, "
            "senatorial connection, real household authority - occupied "
            "by Paula, Marcella, and Fabiola before and alongside their "
            "renunciation; the standing did not disappear at "
            "renunciation but was precisely what made large-scale "
            "founding possible, and the three women's circumstances "
            "were individually distinct, not one interchangeable type "
            "(chunk Quick/World Meaning)."),
        "prior_sense": (
            "The prior IS the sense: this world uses the empire's own "
            "status category as-is - the term names an inherited social "
            "position, not a transformed concept; what the world adds "
            "is only what the standing was then FOR."),
        "modern_sense": (
            "'Aristocratic Roman woman' as a single, undifferentiated "
            "social type (chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "The record's own guard is against flattening: real, "
            "individually distinct family situations, wealth levels, "
            "and positions within one broad category - 'this world's "
            "own record does not let their differences be flattened' "
            "(chunk World Meaning). Standard grounding: a "
            "differentiation guard, not a concept gap."),
        "semantic_domain": "aristocratic-status",
        "grounding_criterion": "standard",
        "voice_surface": (
            "Before any of these women renounced, each already "
            "commanded a household whose decisions mattered materially "
            "to many others - and no two of them from the same "
            "circumstances. That standing is not what they gave up; it "
            "is what they gave WITH. A monastery, a hostel, a hospital "
            "- none of it rises from nothing."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "corroborating",
            "formation_confidence": "Widely Accepted",
        },
        "relations": [
            {"type": "presupposed-by", "target_id": "hallex03",
             "note_ef": ("Mirror of hallex03's presupposes edge: this "
                         "standing is renunciation's precondition."),
             "chunk": "hal_lex10_matrona.md"},
            {"type": "presupposed-by", "target_id": "hallex06",
             "note": ("Mirror of hallex06's presupposes edge: the same "
                      "precondition under patronage (this chunk's EF: "
                      "'the social-historical precondition for "
                      "renunciation and patronage').")},
        ],
    },
    "hallex11": {
        "period_sense": (
            "Recognition as authoritative on disputed scriptural "
            "questions through demonstrated learning, exercised in "
            "person, apart from any clerical office - the standing at "
            "least one woman (Marcella) held in her own right: after "
            "the teacher left for the Holy Land, clergy came to her "
            "own house with the questions they could no longer bring "
            "to him. SINGLE-SOURCE DISCIPLINE (the authored home of "
            "the S2.2 parking): this standing is attested in Jerome's "
            "own memorial letter (Ep. 127) - a single-voice source; "
            "srcHAL001's Marcella-list caveat and srcHAL012's "
            "unverified Ep.24/127-pairing flag both bear on this "
            "entry, and the claim is held as real but "
            "single-attested, never independently corroborated."),
        "prior_sense": (
            "none-attested - this is the build's own descriptive label "
            "for a practice (the syrlex010 class), not an inherited "
            "term; the register is the practiced standing itself."),
        "modern_sense": (
            "Either overclaimed as full independent theological "
            "authority equivalent to ordained office, or dismissed as "
            "merely social, informal, and therefore unimportant (chunk "
            "Modern Hearing - a DOUBLE distortion, both directions "
            "wrong)."),
        "conceptual_distance_note": (
            "A real, recognized, but non-office-based form of "
            "authority - neither equivalent to ordination nor mere "
            "influence; 'its own distinct thing, understood on its own "
            "terms within this world's authority logic' (chunk World "
            "Hearing). The chunk's EF records the strand-test result "
            "honestly: a difference in POSITION, not in KIND, from the "
            "dominant authority mode. Sharp double-sided gap: high "
            "grounding criterion. The parked Reported-Experience "
            "Status text remains verbatim in this record's body."),
        "semantic_domain": "practiced-exegetical-authority",
        "grounding_criterion": "high",
        "voice_surface": (
            "There was a house in Rome where clergy brought the "
            "questions they could not settle - and the one who "
            "answered held no office at all. Her standing was real: "
            "earned by demonstrated learning, exercised in person, "
            "recognized by the very men whose ordination gave them "
            "what she did not have. We say this carefully, for it "
            "comes to us in one voice only - the teacher's own "
            "letter, written in her memory."),
        "confidence": {
            "citation_specificity": "A",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "presupposes", "target_id": "hallex05",
             "note_ef": ("The standing is exercised from within the "
                         "vidua category, not virginity (hal_lex05 "
                         "EF, near-verbatim)."),
             "chunk": "hal_lex11_exegesis-practiced-authority.md"},
            {"type": "tension-with", "target_id": "hallex06",
             "note": ("This chunk's EF: 'the evidentiary core of this "
                      "world's one Tensional gravity - a genuine "
                      "counter-current within the ecology' against the "
                      "patronage authority structure; tested and found "
                      "a difference in position, not in kind - the "
                      "tension is real and the honesty about its "
                      "limits rides with it. Symmetric both ways.")},
            {"type": "associated-with", "target_id": "hallex07",
             "note": ("The standing's exercise at distance rode the "
                      "letter (hal_lex07's medium) - association, no "
                      "hierarchy; symmetric mirror on hallex07.")},
        ],
    },
    "hallex12": {
        "period_sense": (
            "The stage of classical Latin grammatical and literary "
            "training - under the specific teacher Aelius Donatus, "
            "whose name the student kept decades later, 'my teacher' - "
            "that instilled the discipline of close attention to a "
            "text's precise wording underneath all the later "
            "philological labor (chunk Quick/World Meaning)."),
        "prior_sense": (
            "The prior IS the sense: the grammaticus was the empire's "
            "standard second-stage schoolmaster - an inherited "
            "institution this world attended, not a concept it "
            "transformed; what the world adds is what the training "
            "later made possible."),
        "modern_sense": (
            "The early grammar training and the later Hebrew-mastery "
            "claims conflated into one equally-certain achievement "
            "(chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "Two genuinely different confidence levels held apart: "
            "the grammar training is solidly attested; the Hebrew "
            "fluency it supposedly enabled is separately, and "
            "seriously, contested (chunk World Hearing, near-"
            "verbatim) - this entry is the documented, non-Contested "
            "foundation UNDER the contested claims (chunk EF). "
            "Standard grounding: a confidence-disambiguation guard. "
            "Front-matter Related-Term 'Praeceptor' names a "
            "never-built term - declared, no edge possible."),
        "semantic_domain": "classical-education",
        "grounding_criterion": "standard",
        "voice_surface": (
            "Before there was a translator of Hebrew there was a boy "
            "at grammar school, parsing Latin under Donatus - a "
            "teacher whose name he kept all his life. Whatever is "
            "argued about the Hebrew, this much is not argued: the "
            "habit of weighing a text word by word was learned there "
            "first."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "corroborating",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "presupposed-by", "target_id": "hallex01",
             "note_ef": ("Mirror of hallex01's presupposes edge: the "
                         "training under the philological commitment."),
             "chunk": "hal_lex12_grammaticus.md"},
        ],
    },
    "hallex13": {
        "period_sense": (
            "Jerome's prefaces to his translations and commentaries - "
            "'not incidental front matter': short, combative essays, "
            "one per book, explaining why this rendering differs, "
            "anticipating the objection, sometimes naming the objector "
            "- the genre where the Hebraica veritas commitment is "
            "actually argued, book by book, under real pressure (chunk "
            "Quick/World Meaning)."),
        "prior_sense": (
            "The ordinary Latin praefatio - a spoken or written "
            "opening, a foreword - the neutral surface this world's "
            "combative, self-justifying use sharpens - a builder note, "
            "UNVERIFIED against this build's own docs."),
        "modern_sense": (
            "A preface as neutral scholarly apparatus - skippable "
            "front matter before the real text (chunk Modern "
            "Hearing)."),
        "conceptual_distance_note": (
            "'A preface was an argument, addressed to real critics, "
            "not a neutral introduction' (chunk World Hearing, "
            "verbatim) - and the genre is directly load-bearing for "
            "the world's central textual-authority gravity (chunk "
            "EF). High grounding: the gap decides whether a "
            "participant hears this world defending itself in its own "
            "voice or files the defense under apparatus. The corpus "
            "row (srcHAL023) carries the genre's own caveat: a "
            "single-voice, self-justifying source type."),
        "semantic_domain": "preface-genre",
        "grounding_criterion": "high",
        "voice_surface": (
            "Nearly every book we sent out went with a short, "
            "combative essay at its head - why this rendering differs "
            "from the one you know, what the objection will be, and "
            "sometimes the objector's name. Read one and you have "
            "heard us defending ourselves in our own voice, under "
            "real pressure, in real time."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "material-source-of", "target_id": "hallex01",
             "note_ef": ("The primary evidentiary basis for the "
                         "Hebraica veritas principle (this chunk's EF, "
                         "near-verbatim; srcHAL023 is the corpus "
                         "row) - the Desert material-source-of/"
                         "presupposes pairing."),
             "chunk": "hal_lex13_praefatio.md"},
            {"type": "presupposed-by", "target_id": "hallex01",
             "note": ("Mirror of hallex01's presupposes edge (the "
                      "principle argued in, and evidenced by, this "
                      "genre).")},
            {"type": "associated-with", "target_id": "hallex02",
             "note": ("Symmetric mirror of hallex02's edge: the "
                      "prefaces travel attached to the translation "
                      "project's own books.")},
        ],
    },
    "hallex14": {
        "period_sense": (
            "The hospital Fabiola founded in Rome for the sick - the "
            "first such foundation, distinct from the travelers' "
            "hospice (xenodochium); the sick gathered in from the "
            "streets and cared for under one roof, before anything "
            "was built at Bethlehem; the Greek word left untranslated "
            "in Latin even by the scholar who elsewhere insisted on "
            "translation precision (chunk Quick/World Meaning)."),
        "prior_sense": (
            "A Greek loan (the chunk's own note: the word 'came into "
            "Latin from Greek and was left there, untranslated') - "
            "the prior is the Greek term for a place of care for the "
            "sick, new enough in Latin that this founding is what "
            "domesticated it; no Greek-script form appears in this "
            "build's docs and none is fabricated here."),
        "modern_sense": (
            "Conflated with the travelers' hospice, or assumed to "
            "have a modern hospital's institutional scale and "
            "staffing (chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "A genuinely novel act of charitable founding - real, "
            "Rome-based, distinct from any Bethlehem institution - "
            "'on a scale not independently verified' (chunk World "
            "Hearing, the caveat preserved verbatim). Standard "
            "grounding: an anti-conflation and scale guard. "
            "Front-matter Related-Term 'Xenodochium' names a "
            "never-built term - declared, no edge possible; the "
            "Perseus critical-text verification of Ep. 77.6 is the "
            "pre-freeze re-sweep's editions-class item.")
        ,
        "semantic_domain": "charitable-foundation",
        "grounding_criterion": "standard",
        "voice_surface": (
            "Before any of us built at Bethlehem, Fabiola had already "
            "done the newer thing in Rome: gathered the sick in from "
            "the streets and cared for them under one roof - the "
            "first house of its kind. Even the word for it stayed "
            "Greek on our tongues, as if Latin had not yet caught up "
            "with what she had done."),
        "confidence": {
            "citation_specificity": "A",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "corroborating",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "presupposes", "target_id": "hallex03",
             "note_ef": ("The founding presupposes renounced wealth "
                         "(hal_lex03's EF names nosocomium among what "
                         "renuntiatio is presupposed by)."),
             "chunk": "hal_lex14_nosocomium.md"},
        ],
    },
    "hallex15": {
        "period_sense": (
            "The standard term for a male ascetic - the ordinary word "
            "for the men of the communities visited on the journey to "
            "the Holy Land and of the Bethlehem household itself; a "
            "simple, well-worn term, in deliberate contrast to the "
            "much more differentiated vocabulary this world worked "
            "out for its women (virgo, vidua) (chunk Quick/World "
            "Meaning)."),
        "prior_sense": (
            "A Greek loan into Latin (monachus, from the Greek for a "
            "solitary or single one) already ordinary by this world's "
            "time - the inherited surface used as-is, not "
            "transformed; a builder note on the etymology, UNVERIFIED "
            "against this build's own docs, which treat the term only "
            "as standard vocabulary."),
        "modern_sense": (
            "Modern 'monk' - which the chunk itself judges a "
            "reasonable mapping (chunk Modern Hearing: 'likely "
            "unproblematic')."),
        "conceptual_distance_note": (
            "Broadly consistent with modern usage; low distortion "
            "risk relative to nearly every other entry in this "
            "lexicon (chunk World Hearing, near-verbatim). Low "
            "grounding by the chunk's own assessment - the entry's "
            "work is naming 'the unnamed monastic multitudes' the "
            "sources reference but never individuate (chunk EF). "
            "Both front-matter Related-Terms (Monasterium duplex, "
            "Praeceptor) name never-built terms - declared; this "
            "record carries no field_relations and its parked EF "
            "remains in world_meaning (no first edge to ride)."),
        "semantic_domain": "male-asceticism",
        "grounding_criterion": "low",
        "voice_surface": (
            "For the men we had one plain word - monachus, a monk - "
            "worn smooth by use. It is our women for whom the "
            "language grew careful and exact; the men it names in "
            "multitudes, and mostly leaves unnamed."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "illustrative",
            "formation_confidence": "Widely Accepted",
        },
        "relations": [],  # both Related-Terms never built - declared above
    },
}


def verify_gloss_map():
    """The Step-3 in-view assertion: every confirmed-gloss original
    resolves against the live gloss list AND the live term fields."""
    from app.prompts.confirmed_glosses import CONFIRMED_GLOSSES
    live = {g.original for g in
            CONFIRMED_GLOSSES["hieronymian-ascetic-literary"]}
    assert live == set(GLOSS_MAP), (live ^ set(GLOSS_MAP))
    for original, rid in GLOSS_MAP.items():
        if rid is None:
            continue
        front, _ = read_record(TERM_DIR / f"{rid}.md")
        assert original.lower() in front["term"].lower(), (original, rid)
    n = sum(1 for v in GLOSS_MAP.values() if v)
    print(f"gloss map verified in view: {n}/13 resolve to term records; "
          f"1 Facilitator-phrase circumlocution (no term record by design)")


def main():
    verify_gloss_map()
    n = 0
    for rid, data in AUTH.items():
        path = TERM_DIR / f"{rid}.md"
        front, body = read_record(path)
        for key in ("period_sense", "prior_sense", "modern_sense",
                    "conceptual_distance_note", "semantic_domain",
                    "grounding_criterion", "voice_surface", "confidence"):
            front[key] = data[key]
        rels = []
        for r in data["relations"]:
            note = r.get("note", "")
            if "note_ef" in r:
                note = ef_note(r["note_ef"], r["chunk"])
            rels.append({"type": r["type"], "target_id": r["target_id"],
                         "note": note})
        front["field_relations"] = rels
        write_record(path, front, body)
        n += 1
    print(f"authored {n} term records")


if __name__ == "__main__":
    main()
