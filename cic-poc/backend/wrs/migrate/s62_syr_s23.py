"""S6.2/Syriac - S2.3-equivalent: term authoring (single batch; 10 terms).

Adds the authored fields onto the S2.2 mechanical records: senses
(period/prior/modern + conceptual_distance_note), semantic_domain,
grounding_criterion, voice_surface, confidence block, original_script,
and typed field_relations. Conventions carried from Desert/ALX:

- FLAG-023: the fence-asserting reader (partition on "\\n---\\n" with
  asserts) - never the broken split("\\n---",2) pattern.
- FLAG-002: the chunk's Ecological Function text rides VERBATIM inside
  the FIRST field_relations edge note (extracted from the deployed
  chunk at run time - mechanical, nothing retyped).
- prior_sense honesty: 'none-attested' is an answer; builder inferences
  beyond the build docs carry an explicit UNVERIFIED flag.
- formation_confidence: the Article-17 enum, per-term, from each
  chunk's own confidence language (the CT sections where present).
- Symmetric types (associated-with / tension-with) asserted on BOTH
  records; directional types asserted once (the gates' SYMMETRIC rule).
- syrlex008 (Mar) and syrlex009 (Catholicos) carry NO field_relations
  BY THE CHUNKS' OWN DESIGN (008: 'No reciprocal cross-reference
  asserted'; 009: 'standalone by design') - an empty list here is the
  chunk's own decision, not an omission.

Relation map (each note grounded in the citing chunk's own text):
  004 presupposes 001      (madrasha performs the raza/shrara method)
  001 assoc 006 (sym)      (the Commentary applies the method to the text)
  002 assoc 007 (sym)      (near-synonyms kept deliberately distinct)
  003 material-source-of 002  (Dem 6 is a tahwitha - the primary source)
  003 material-source-of 007  (textual home of Dem 6:8, 7:20)
  003 material-source-of 010  (the anti-Jewish subset is ~4 of the 23)
  004 assoc 005 (sym)      (sister verse genres, distinguished)
"""
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

TERM_DIR = BACKEND / "wrs" / "records" / "syriac_world" / "term"
CHUNKS = BACKEND / "data" / "syriac_world" / "lexicon_chunks"

VDATE = "2026-07-28"


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
    "syrlex001": {
        "original_script": "ܐܪܙܐ",
        "period_sense": (
            "A raza is bound to the shrara (truth) it signifies and carries "
            "something of that truth's own hidden power - reading Scripture "
            "and creation by raza is perceiving a real connection already "
            "there for a formed eye, not decoding an arbitrary sign; richly "
            "developed as a whole theological method in Ephrem, present at "
            "genuinely lesser depth in Aphrahat (chunk Quick/World Meaning)."),
        "prior_sense": (
            "The build's own documented contrast object is Platonic/"
            "allegorical symbol-theory - the raza sense is defined AGAINST "
            "an inherited representational idea of symbol (Doc_03 SS1.1: 'a "
            "deliberate contrast with Platonic/allegorical symbol-theory'). "
            "The pre-Christian Aramaic raz ('secret/mystery') as the word's "
            "inherited surface is a builder note, UNVERIFIED against this "
            "build's own docs, which do not develop the etymology."),
        "modern_sense": (
            "'Symbol' or 'type' as an arbitrary or conventional stand-in, "
            "replaceable by another sign, related to its referent only by "
            "agreement - the way a word relates to its meaning (chunk "
            "Modern Hearing)."),
        "conceptual_distance_note": (
            "The modern ear files 'symbol' under representation-at-a-"
            "distance; this world heard participation - the raza carries "
            "the shrara's own hidden power, and 'just a metaphor' collapses "
            "a claim about real participation into literary decoration "
            "(chunk World Hearing). Sharp gap: high grounding criterion by "
            "rule."),
        "semantic_domain": "symbol-truth-method",
        "grounding_criterion": "high",
        "voice_surface": (
            "A raza is not a stand-in for the truth it points to. It is "
            "bound to that truth and carries something of its hidden power, "
            "so the one who reads rightly is not decoding a sign but being "
            "brought into contact with what it holds. The connections are "
            "already there, waiting for an eye formed to see them - in "
            "Scripture, and in the world's own furniture: light, water, "
            "oil, the vine."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Widely Accepted",
        },
        "relations": [
            {"type": "presupposed-by", "target_id": "syrlex004",
             "note_ef": ("The madrasha is the sung vehicle through which "
                         "this hermeneutic is chiefly performed (chunk "
                         "Reciprocity Note; Doc_04 C1)."),
             "chunk": "syrlex001_raza-shrara.md"},
            {"type": "associated-with", "target_id": "syrlex006",
             "note": ("The chunks' own mutual Related-Terms cross-reference "
                      "(both Reciprocity Notes attest the pair): Ephrem's "
                      "Commentary applies this same typological reading to "
                      "the harmonized Gospel text - association, no "
                      "hierarchy claimed (CO-P2-13 pattern).")},
        ],
    },
    "syrlex002": {
        "original_script": "ܩܝܡܐ",
        "period_sense": (
            "The lifelong, vowed, celibate order of 'sons and daughters of "
            "the covenant' - men and women resident among their own kin in "
            "town, keeping fast, watch, vigil, and reading inside ordinary "
            "community life rather than in desert withdrawal; already an "
            "established institution needing correction more than founding "
            "when Aphrahat addresses it in Demonstration 6 (chunk "
            "Quick/World Meaning)."),
        "prior_sense": (
            "Root qwm, 'stand' - to take the qyama is to have 'stood' for "
            "the covenant (Doc_03 SS1.2's own root note); the ordinary "
            "Aramaic senses of standing/covenant/pact are the inherited "
            "surface the institution's technical use specialized."),
        "modern_sense": (
            "'Vowed celibate order' heard as the desert monk or cloistered "
            "nun - withdrawal from ordinary society into a separate, often "
            "physically remote community under a formal monastic rule "
            "(chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "The modern reach for 'monk/nun/monastery' imports exactly what "
            "this world's asceticism was not: qyama members practiced their "
            "discipline INSIDE ordinary town life among kin, and the "
            "order's formal structure (rule, enclosure, hierarchy) is "
            "thinly and contestedly documented, not settled (chunk World "
            "Hearing). Sharp institutional gap: high grounding criterion."),
        "semantic_domain": "covenant-asceticism",
        "grounding_criterion": "high",
        "voice_surface": (
            "To take the qyama is to stand for a promise that does not "
            "end - not a season of youth to be outgrown. The bar qyama and "
            "bat qyama live among their own kin, unmarried, keeping the "
            "fast and the watch, present at the vigil and the reading: a "
            "town's own askesis, formed less by flight from the world than "
            "by refusal within it."),
        "confidence": {
            "citation_specificity": "A",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Widely Accepted",
        },
        "relations": [
            {"type": "associated-with", "target_id": "syrlex007",
             "note_ef": ("Near-synonym in Aphrahat's own usage (Dem 6:8, "
                         "7:20) - the two entries are read alongside each "
                         "other, deliberately NOT merged (both chunks' own "
                         "double-counting guard); association, no "
                         "hierarchy."),
             "chunk": "syrlex002_qyama.md"},
            {"type": "presupposes", "target_id": "syrlex003",
             "note": ("This entry's primary evidentiary source "
                      "(Demonstration 6) is itself one of Aphrahat's "
                      "taḥwyāṯā (chunk Reciprocity Note) - the Desert "
                      "material-source-of/presupposes pairing.")},
        ],
    },
    "syrlex003": {
        "original_script": "ܬܚܘܝܬܐ",
        "period_sense": (
            "Aphrahat's own genre-term for his twenty-three doctrinal "
            "treatises (Greek apodeixis; conventionally 'Demonstrations'), "
            "several built on the twenty-two-letter Syriac acrostic so the "
            "alphabet scaffolds the argument in memory; he also called the "
            "same works 'Letters' - the naming was not fixed to one term "
            "even in his own usage (chunk Quick/World Meaning)."),
        "prior_sense": (
            "The word's ordinary sense - a showing, a reasoned "
            "demonstration or proof, corresponding to the Greek apodeixis "
            "(the chunk's own gloss) - which Aphrahat's usage applies as a "
            "self-designation rather than transforms."),
        "modern_sense": (
            "'Demonstrations' assumed to be simply an English descriptor "
            "with no native-language equivalent, or assumed to be "
            "Aphrahat's only name for his own work (chunk combined "
            "Modern/World Hearing)."),
        "conceptual_distance_note": (
            "A naming-convention gap rather than a conceptual chasm: the "
            "corrective is that the corpus carries its own native name AND "
            "that Aphrahat's own naming was plural (taḥwyāṯā and "
            "'Letters'). Standard grounding: the entry is load-bearing for "
            "citation practice, not for a lived-concept distortion."),
        "semantic_domain": "genre-self-designation",
        "grounding_criterion": "standard",
        "voice_surface": (
            "Aphrahat called his own works taḥwyāṯā - demonstrations, a "
            "showing of the thing - and sometimes letters; each works "
            "through its subject in order, several strung on the "
            "twenty-two letters of the alphabet so that memory itself has "
            "a rail to hold the argument by."),
        "confidence": {
            "citation_specificity": "A",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "corroborating",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "material-source-of", "target_id": "syrlex002",
             "note_ef": ("Demonstration 6, the qyama entry's primary "
                         "evidentiary source, is itself one of Aphrahat's "
                         "taḥwyāṯā (both chunks' Reciprocity Notes)."),
             "chunk": "syrlex003_tahwyata.md"},
            {"type": "material-source-of", "target_id": "syrlex007",
             "note": ("The taḥwyāṯā are the textual home of the Iḥidaya "
                      "title as Aphrahat uses it (Dem 6:8, 7:20 - chunk EF "
                      "and both Reciprocity Notes).")},
            {"type": "material-source-of", "target_id": "syrlex010",
             "note": ("The anti-Jewish material is a subset of this same "
                      "corpus - roughly four of the twenty-three "
                      "Demonstrations (syrlex010's own scope statement; "
                      "its front-matter Related-Terms points here "
                      "one-directionally, typed at authoring rather than "
                      "left untyped).")},
            {"type": "presupposed-by", "target_id": "syrlex002",
             "note": ("Mirror of syrlex002's presupposes edge (Dem 6 is "
                      "one of the taḥwyāṯā).")},
            {"type": "presupposed-by", "target_id": "syrlex007",
             "note": ("Mirror of syrlex007's presupposes edge (Dem 6:8, "
                      "7:20 are the Iḥidaya title's textual home).")},
            {"type": "presupposed-by", "target_id": "syrlex010",
             "note": ("Mirror of syrlex010's presupposes edge (the "
                      "anti-Jewish subset presupposes the corpus).")},
        ],
    },
    "syrlex004": {
        "original_script": "ܡܕܪܫܐ",
        "period_sense": (
            "Ephrem's dominant vehicle for theological argument: a sung, "
            "metered, stanzaic, often acrostic hymn with refrains "
            "(ʿonyaṯa), performed rather than read - the argument itself "
            "carried through melody and repetition; a genre already "
            "established by Bardaisan and Mani, which Ephrem took up to "
            "answer them on their own ground (chunk Quick/World Meaning)."),
        "prior_sense": (
            "The genre's own pre-Ephrem life is the documented prior: "
            "Bardaisan had made the sung stanzaic hymn his own literary "
            "form in the third century, and Mani's hymnody worked in "
            "comparable terms - Ephrem contested rivals on ground they "
            "already occupied (chunk World Meaning; the chunk's own "
            "genre-level-only caution: no claim about matching a specific "
            "rival's meter or refrain-structure)."),
        "modern_sense": (
            "'Hymn' as decorative accompaniment - illustrating or "
            "celebrating a teaching that could equally well be stated in "
            "prose (chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "For Ephrem's audience the madrasha WAS the argument: meter "
            "and refrain a formation technology carrying the raza/shrara "
            "method into the body, and the genre-choice itself a contested "
            "claim staked against Bardaisan's and Mani's use of the same "
            "form (chunk World Hearing). Sharp gap: high grounding "
            "criterion by rule."),
        "semantic_domain": "sung-theology",
        "grounding_criterion": "high",
        "voice_surface": (
            "To transmit doctrine here is, in large part, to sing it. A "
            "madrasha does not set an argument beside other arguments; it "
            "carries the argument through a melody, returns it in the "
            "refrain, and lodges it in the body along with the tune. The "
            "form was not ours first - Bardaisan and Mani sang their own "
            "teaching in it - and taking it up was itself part of the "
            "contest."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "presupposes", "target_id": "syrlex001",
             "note_ef": ("The madrasha performs the raza/shrara hermeneutic "
                         "- the genre presupposes the method it carries "
                         "(chunk Reciprocity Note: 'the hermeneutic this "
                         "genre performs'; Doc_04 C1)."),
             "chunk": "syrlex004_madrasha.md"},
            {"type": "associated-with", "target_id": "syrlex005",
             "note": ("Sister verse genres, distinguished by meter, "
                      "occasion of use, and memra's later "
                      "genre-crystallization caveat (both chunks' "
                      "Reciprocity Notes attest the pair) - association, "
                      "no hierarchy.")},
        ],
    },
    "syrlex005": {
        "original_script": "ܡܐܡܪܐ",
        "period_sense": (
            "Within this world's own 200-410 window, a small, narrowly "
            "authenticated set of verse compositions by Ephrem in couplets "
            "and single syllabic meter (per Brock: the six memre 'On "
            "Faith' and the Nicomedia memra definitely his; a few others "
            "probably or less certainly genuine) - not yet the named "
            "'verse homily' genre of later tradition (chunk Quick Meaning "
            "and Distortion Risk)."),
        "prior_sense": (
            "The ordinary Syriac word for a discourse or utterance is the "
            "inherited surface - a builder note, UNVERIFIED against this "
            "build's own docs, which treat the term only at genre level "
            "(Doc_03 SS1.5)."),
        "modern_sense": (
            "'Memra' heard through later Syriac literature as an "
            "already-settled, named literary category standing alongside "
            "madrasha within this world's own period (chunk combined "
            "Modern/World Hearing)."),
        "conceptual_distance_note": (
            "A retrojection gap: the fully developed verse-homily genre is "
            "a fifth/sixth-century crystallization (Narsai, Jacob of "
            "Serugh), after this world's own 410 boundary, and not "
            "attested for Aphrahat at all - this world's own memra is a "
            "handful of authenticated Ephrem pieces in a bare metrical "
            "form. Standard grounding: genre-history correction, "
            "anachronism-guard shaped."),
        "semantic_domain": "verse-genre",
        "grounding_criterion": "standard",
        "voice_surface": (
            "A memra with us is a recited thing, couplets in one meter, "
            "and only a few are surely Ephrem's own. The great named genre "
            "of verse homilies that later teachers made famous is their "
            "harvest, not our field."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "corroborating",
            "formation_confidence": "Widely Accepted",
        },
        # the associated-with mirror of syrlex004 is asserted there and
        # mirrored here (symmetric type -> both records)
        "relations": [
            {"type": "associated-with", "target_id": "syrlex004",
             "note": ("Sister verse genre, distinguished by meter and - "
                      "for madrasha - sung/refrain structure against "
                      "memra's recited couplets (chunk Reciprocity Note); "
                      "symmetric mirror of syrlex004's edge.")},
        ],
    },
    "syrlex006": {
        "original_script": "ܐܘܢܓܠܝܘܢ ܕܡܚܠܛܐ",
        "period_sense": (
            "Throughout this world's core period 'the Gospel' meant a "
            "single continuous harmonized narrative - Tatian's Diatessaron "
            "(c. 172 CE), the standard lectionary text of Syriac-speaking "
            "churches for roughly two centuries; Aphrahat quotes it, "
            "Ephrem wrote a full Commentary on it, and Ephrem's own "
            "Commentary calls it simply 'the Gospel' (chunk Quick/World "
            "Meaning)."),
        "prior_sense": (
            "none-attested as an inherited concept - this is a title, not "
            "a transformed inheritance; the contrasting later label is "
            "da-Mepharreshe, the 'separated' four-Gospel form (chunk "
            "aliases), and the vernacular name's own earliest attestation "
            "is the entry's contest, not its prior."),
        "modern_sense": (
            "'The Gospels' assumed in the familiar fourfold plural sense, "
            "or the vernacular name assumed to be a settled, established "
            "label throughout the period (chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "The formation experience differs materially: hearing 'the "
            "Gospel' as one unfolding story versus four witnesses in "
            "tension (Doc_01's narrative-unity DMR). The NAME "
            "'da-Mhallete' is itself unsettled - not confirmed in use "
            "within the period (Theodoret's Greek account never uses the "
            "Syriac phrase; Crawford locates the earliest secure witness "
            "in a gloss on the Syriac Eusebius) - so the entry carries "
            "both the well-attested practice and the contested label. "
            "Standard grounding: the practice-gap is real but the "
            "correction is largely scholarly."),
        "semantic_domain": "harmonized-gospel",
        "grounding_criterion": "standard",
        "voice_surface": (
            "When we say the Gospel we mean one continuous story - the "
            "harmony Tatian wove - read at the lectern and commented by "
            "our teachers as a single unfolding. Whether our own tongues "
            "called it 'the Mixed' in those years, the record does not "
            "settle; Ephrem's Commentary calls it only the Gospel."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Contested",
        },
        "relations": [
            {"type": "associated-with", "target_id": "syrlex001",
             "note_ef": ("Symmetric mirror of syrlex001's edge: Ephrem's "
                         "Commentary applies the raza/shrara typological "
                         "method to this harmonized text (chunk "
                         "Reciprocity Note; Doc_04 C5-C1 link)."),
             "chunk": "syrlex006_ewangeliyon-da-mhallete.md"},
        ],
    },
    "syrlex007": {
        "original_script": "ܝܚܝܕܝܐ",
        "period_sense": (
            "One word carrying double duty held as one idea: the ascetic "
            "designation for the consecrated elite - single-minded, "
            "undivided in allegiance, living communally despite the "
            "surface sense of 'solitary' - and simultaneously the "
            "christological title for Christ as Only-Begotten (monogenes); "
            "in Aphrahat (Dem 6:8, 7:20) a near-synonym of bar/bat qyama "
            "(chunk Quick/World Meaning)."),
        "prior_sense": (
            "Root yḥd, 'one' (Doc_03 SS1.7) - the ordinary senses of "
            "onlyness/singleness that let the ascetic and christological "
            "uses share one root rather than coincide by accident."),
        "modern_sense": (
            "'Solitary' heard as physical isolation, or the "
            "ascetic/christological double sense heard as an odd accident "
            "of two unrelated meanings sharing a word (chunk Modern "
            "Hearing)."),
        "conceptual_distance_note": (
            "The shared root is load-bearing, not incidental: an "
            "ascetic's own singleness is heard as participating in "
            "Christ's own undividedness from the Father - and the "
            "iḥidaye lived communally, not in isolation. Later "
            "(fifth/sixth-century) drift toward 'monk' must not be read "
            "back (chunk World Hearing). Sharp gap: high grounding "
            "criterion by rule."),
        "semantic_domain": "single-one-christology",
        "grounding_criterion": "high",
        "voice_surface": (
            "Iḥidaya names the single one - undivided in allegiance, "
            "though living among others - and names the Only-Begotten "
            "himself. The name you are given tells you what your "
            "singleness is: a small likeness of his own undividedness "
            "from the Father."),
        "confidence": {
            "citation_specificity": "A",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "associated-with", "target_id": "syrlex002",
             "note_ef": ("Symmetric mirror of syrlex002's edge: "
                         "near-synonym in Aphrahat's own usage, kept as a "
                         "distinct entry - the double ascetic/"
                         "christological sense is this entry's own "
                         "contribution (chunk EF's own "
                         "anti-merge guard)."),
             "chunk": "syrlex007_ihidaya.md"},
            {"type": "presupposes", "target_id": "syrlex003",
             "note": ("The taḥwyāṯā are this title's attestation home "
                      "(Dem 6:8, 7:20 - chunk Reciprocity Note) - the "
                      "Desert material-source-of/presupposes pairing.")},
        ],
    },
    "syrlex008": {
        "original_script": "ܡܪܝ",
        "period_sense": (
            "An honorific title-prefix, 'my lord,' used across Syriac "
            "Christianity for bishops, saints, and revered teachers "
            "(roughly parallel to 'Saint') - broadly attested for this "
            "world, but NOT confirmed as attached to Ephrem's own name "
            "during his lifetime (chunk Quick Meaning)."),
        "prior_sense": (
            "The ordinary Aramaic address 'my lord' (mar + first-person "
            "suffix) - a secular honorific whose ecclesial use is a "
            "specialization of everyday deference, per the chunk's own "
            "gloss."),
        "modern_sense": (
            "'Mar Ephrem' assumed to be a form of address already in use "
            "during Ephrem's own lifetime or immediately after (chunk "
            "combined Modern/World Hearing)."),
        "conceptual_distance_note": (
            "A dating caution on a compound, not a conceptual gap: the "
            "honorific is real and low-controversy as a linguistic fact "
            "(Aphrahat called 'Mar Jacob, the Persian sage' in a 510 CE "
            "colophon - itself post-window), but the specific compound "
            "'Mar Ephrem' within the window is unconfirmed and may be a "
            "later veneration-driven convention. Low grounding: included "
            "for runtime recognizability, the chunk says, not because it "
            "organizes the ecology."),
        "semantic_domain": "honorific",
        "grounding_criterion": "low",
        "voice_surface": (
            "Mar is how we say 'my lord' - for a bishop, a holy one, a "
            "teacher whose word is weighed. Whether anyone said 'Mar "
            "Ephrem' while Ephrem lived, our record does not show."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "illustrative",
            "formation_confidence": "Widely Accepted",
        },
        "relations": [],  # the chunk's own design: no cross-reference
    },
    "syrlex009": {
        "period_sense": (
            "NOT this world's own contemporary vocabulary: no one in this "
            "world's period called their Persian episcopal leader "
            "'Catholicos' - leadership was real, local, and contested "
            "(Papa bar Aggai's primacy claim fiercely contested by Miles "
            "of Susa and Aqib-Alaha of Karka d'Baith Slok), and the tidy "
            "titled succession is later tradition's retrojection, resting "
            "in part on the Acts of Mari (6th-8th c.) (chunk Quick/World "
            "Meaning; the entry exists to carry this flag into "
            "retrieval)."),
        "prior_sense": (
            "The Greek adjective katholikos ('general/universal') behind "
            "the later office-title - the title's own history is "
            "posterior to this world, which is the entry's point; "
            "none-attested as this world's own usage."),
        "modern_sense": (
            "'Catholicos' assumed to be the settled title for Persian "
            "episcopal leadership throughout the period, with an "
            "unbroken, clearly-titled succession running back to the "
            "first century (chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "An anachronism flag rather than a translation gap: the "
            "title is anachronistic before the fifth century for this "
            "world's own period; succession narratives using it are "
            "later retrojections onto leadership that was real but "
            "contested and not yet centrally titled (chunk World "
            "Hearing; CT: Application to this world). High grounding: "
            "the entry's whole function is corrective."),
        "semantic_domain": "office-title-anachronism",
        "grounding_criterion": "high",
        "voice_surface": (
            "No one among us called any bishop 'Catholicos.' Our "
            "churches knew real leaders and real quarrels over "
            "precedence - Papa's claim, and those who withstood it - "
            "but the single named office came later, and was laid back "
            "over our years by those who came after."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "corroborating",
            "formation_confidence": "Contested",
        },
        "relations": [],  # standalone by the chunk's own design
    },
    "syrlex010": {
        "period_sense": (
            "Roughly four of Aphrahat's twenty-three Demonstrations are "
            "sustained argument against Jewish practice and "
            "interpretation (circumcision, Sabbath, dietary law, the "
            "dating of Passover, among others) - a real, attested thread "
            "of the record, surviving ONLY in Aphrahat's own voice with "
            "no independent contemporary Jewish source answering it "
            "(Koltun-Fromm's 'reconstructed conversation' framing, "
            "load-bearing) (chunk Quick/World Meaning)."),
        "prior_sense": (
            "none-attested - this is the build's own descriptive label "
            "for a corpus subset, not an inherited term with a prior "
            "sense; the record register is the corpus itself."),
        "modern_sense": (
            "Either dismissed as a minor historical footnote, or Mar "
            "Yausep's honest acknowledgment misread as tacit endorsement "
            "of hostility toward Jewish people or practice in the "
            "present - neither reading accurate (chunk Modern Hearing)."),
        "conceptual_distance_note": (
            "The record carries one side of a real, historically "
            "situated argument - not a settled verdict on Judaism, and "
            "not content with any bearing on how Jewish people or "
            "practice should be regarded today; the Representative names "
            "it as a real and regrettable feature of his community's "
            "record, never an argument to renew (chunk World Hearing + "
            "Standing Distortion-Risk Note, parked verbatim in this "
            "record's body). High grounding: sensitivity plus "
            "force_llm_vote gating."),
        "semantic_domain": "polemical-record",
        "grounding_criterion": "high",
        "voice_surface": (
            "Our record carries real contempt in it, argued in our own "
            "teacher's voice against Jewish practice, and no answering "
            "voice beside it. We own that as our own life's fault - "
            "named honestly, not softened, and not taken up again as a "
            "case to be won."),
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "verification_date": VDATE,
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Documented",
        },
        "relations": [
            {"type": "presupposes", "target_id": "syrlex003",
             "note": ("The four anti-Jewish Demonstrations are a subset "
                      "of the taḥwyāṯā corpus (this chunk's own "
                      "front-matter Related-Terms pointer, typed at "
                      "authoring) - the Desert material-source-of/"
                      "presupposes pairing.")},
        ],
    },
}


def main():
    n = 0
    for rid, data in AUTH.items():
        path = TERM_DIR / f"{rid}.md"
        front, body = read_record(path)
        for key in ("original_script", "period_sense", "prior_sense",
                    "modern_sense", "conceptual_distance_note",
                    "semantic_domain", "grounding_criterion",
                    "voice_surface", "confidence"):
            if key in data:
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
