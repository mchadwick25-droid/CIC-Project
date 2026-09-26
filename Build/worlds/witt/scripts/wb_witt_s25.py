"""B-5 (Gravity + force records): Lutheran Wittenberg & Its Congregations
(witt) -- authors the 13 `witt.gravity.*` records (one per Doc_04 §3
candidate, G1-G13) and the 20 `witt.force.*` records (one per Doc_08 §3
force entry, cells 1A-1 through 3B-2), then closes every "parked for B-5"
note this build's own B-4 story (12) and figure (6) records were left
carrying -- 18 records, 39 story/figure -> gravity links -- with real
relations[] entries and reciprocal back-edges on the gravity side, per
Gallic's own worked B-5 precedent (records/gallic/gravity/gallic.gravity.
grace-and-effort.md; records/gallic/force/gallic.force.egyptian-standard.md).

SOURCE OF TRUTH. Every gravity's content traces to World-Builds/Lutheran-
Wittenberg/witt_Doc_04_Historical_Gravity.md (Revision 5, Approved to
Proceed, five adversarial rounds); every force's content traces to
witt_Doc_08_Forces_Document.md (Approved to Proceed, four adversarial
rounds). Both were read in full before this script was written. No live
research and no general knowledge of Luther or Lutheranism was used
anywhere; every quotation below is one Doc_04 or Doc_08 already located,
verified and cited at a locus in the vendored files -- this script
re-derives from those two approved documents, exactly as Gallic's own B-5
did ("Re-derived from the approved Doc_04...", "Re-derived from the
approved Doc_08...", both records' own closing lines).

MECHANICAL vs AUTHORED, declared plainly, per this build's own B-2/B-3
script's precedent for stating this once rather than per record:

  MECHANICAL (this script does it, no per-record judgment involved):
    - envelope fields (id, world_id, record_type, schema_version, status,
      register="emic", canon_cells=[] -- gravity/force records carry no
      canon_cells anywhere in the fleet, matching Gallic's own explicit
      convention, stated at the close of both worked examples: "Canon_cells
      left empty, matching fleet convention for gravity/force records");
    - the INTERACTION_MATRIX and CROSS_CELL adjacency data below are a
      direct, checked transcription of Doc_04 §5's 13x13 table and Doc_08
      §4's 14 named connections -- transcription is mechanical, the
      matrix's own content is Doc_04's/Doc_08's;
    - relations RECIPROCITY: every relation this script emits on one side
      (gravity<->gravity from the Interaction Matrix, force<->force from
      the Cross-Cell map, gravity<->force from the §5 Synthesis, gravity<->
      story/figure from the closed B-5 notes) gets its declared inverse
      added mechanically by close_reciprocity() -- a pure structural pass,
      no re-derivation of content, using engine/m1/schemas.py's own
      RELATION_INVERSE table (associated-with and illustrated-by/
      illustrates are the only two shapes used here; precondition-for/
      enabled-by is used for the "generated"/"produced" force->gravity and
      force->force edges specifically, per the judgment call below).
    - closing the 18 "parked for B-5" notes: each story/figure record's own
      parked paragraph already NAMED which gravities it connects to and
      promised "an associated-with edge... with the reciprocal edge
      declared there" (or, for the one founding-act story, "associated-with
      (or illustrates)") -- this script reads that promise (hand-transcribed
      into STORY_GRAVITIES/FIGURE_GRAVITIES below, one read pass over all 18
      files) and discharges it exactly, replacing the parked paragraph with
      a short "closed at B-5" note in the same voice.

  AUTHORED (hand-composed by this build pass, not mechanically derived):
    - every gravity's and force's `description` and `manifestations` --
      dense, analytical, etic-register prose carrying forward Doc_04's/
      Doc_08's own six-test results, confidence levels, classification
      reasoning, Confidence/Gravity Cross-Check outcome, and forces-
      connection notation (for gravities) or Layer 1/2/3 content and
      cross-cell role (for forces) -- never re-run, never re-derived from
      first principles. Checked directly against gate_voice_perspective's
      own field map (engine/m1/gates.py _PERSPECTIVE_FIELDS): "gravity" and
      "force" are NOT listed there, so these fields are not held to the
      term/story we-voice bar -- confirmed against Gallic's own two worked
      examples, both written in an analytical register with embedded
      first-person quotations, never as first-person-plural narration, and
      matched here on purpose;
    - which force->gravity and force->force edges get precondition-for/
      enabled-by rather than associated-with: JUDGMENT CALL, stated once
      here rather than per record. Gallic's own two worked examples draw
      this line in exactly one place -- gallic.force.egyptian-standard
      carries precondition-for only to the forces/gravities its own Layer 3
      calls "produced" ("the founding relationship an initiating-cell force
      has to the gravity it originates"), and associated-with to every
      other connection it names, including ones described with strong verbs
      ("intensified", "fractured", "transformed", "shaped"). This script
      applies the identical rule: a force<->gravity or force<->force edge is
      precondition-for/enabled-by ONLY where Doc_04 §3 or Doc_08 §5 uses the
      verb "generated" (or Doc_08's own paraphrases of it -- "generated as
      the refusal of...", "generated in response", "generated from the
      inheritance refused") for that specific pair; every other verb
      (held, intensified, shifted, reshaped, fenced, fractured, re-set,
      reversed, settled, pressed, corrupted, "is the world's own reading
      of") is associated-with. The Interaction Matrix (gravity<->gravity)
      is uniformly associated-with regardless of its R/S/C code, again
      matching Gallic exactly ("all seven carried as associated-with, R/S
      character preserved here" -- the code is stated in the body prose,
      the relation type is not overloaded to carry it).

DISCLOSED SCOPE DECISIONS:
  1. SOURCES[] -- a representative set per record (4-7 entries), not an
     exhaustive re-citation of every quotation inside `description` and
     `manifestations`. Gallic's own two worked examples do the same (grace-
     and-effort's description quotes eight loci across seven works but
     lists eight `sources[]` entries, several bundling more than one
     locus). Every quotation actually used below is a locus Doc_04 or
     Doc_08 already gives and verified; this script does not re-open any
     vendored file.
  2. gate_voice_perspective / gate_no_build_attribution: both already
     exempt gravity/force records by field map (see AUTHORED note above,
     and gates.py's own comment: "every field on gravity/force/
     contested_claim/search_record/source are NOT compiled and are
     legitimate places for build-process language to live"). No special
     handling needed here.
"""
from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[4]
GRAVITY_DIR = REPO_ROOT / "records" / "witt" / "gravity"
FORCE_DIR = REPO_ROOT / "records" / "witt" / "force"
STORY_DIR = REPO_ROOT / "records" / "witt" / "story"
FIGURE_DIR = REPO_ROOT / "records" / "witt" / "figure"
WORLD_ID = "lutheran-wittenberg-and-its-congregations"

RELATION_INVERSE = {
    "presupposes": "presupposed-by",
    "presupposed-by": "presupposes",
    "precondition-for": "enabled-by",
    "enabled-by": "precondition-for",
    "tension-with": "tension-with",
    "illustrated-by": "illustrates",
    "illustrates": "illustrated-by",
    "associated-with": "associated-with",
}

# ---------------------------------------------------------------------------
# Source-id shorthand. Every abbreviation maps to a real witt.source.* id
# (confirmed present under records/witt/source/ before this script was
# written -- no id below is guessed).
# ---------------------------------------------------------------------------
S = {
    "CL": "witt.source.luther-treatise-on-christian-liberty",
    "GW": "witt.source.luther-treatise-on-good-works",
    "BC": "witt.source.luther-babylonian-captivity-of-the-church",
    "CN": "witt.source.luther-open-letter-to-the-christian-nobility",
    "PR": "witt.source.luther-papacy-at-rome-an-answer",
    "DM": "witt.source.luther-that-doctrines-of-men-are",
    "ES": "witt.source.luther-eight-wittenberg-sermons",
    "SA": "witt.source.luther-secular-authority-to-what-extent-it",
    "TK": "witt.source.luther-to-the-knights-of-the-teutonic",
    "EX": "witt.source.luther-earnest-exhortation-for-all-christians-warning",
    "BW": "witt.source.luther-on-the-bondage-of-the-will",
    "LC": "witt.source.luther-large-catechism",
    "SC": "witt.source.luther-small-catechism",
    "TT": "witt.source.luther-selections-from-the-table-talk",
    "HYP": "witt.source.luther-four-hymnal-prefaces-to-walters-gesangb",
    "HYH": "witt.source.luther-deutsche-geistliche-lieder-the-hymns",
    "FB": "witt.source.luther-ein-feste-burg-ist-unser-gott",
    "AC": "witt.source.melanchthon-augsburg-confession",
    "AP": "witt.source.melanchthon-apology-of-the-augsburg-confession",
    "KH": "witt.source.karsthans",
    "WAL": "witt.source.johann-letter-of-reminiscence-on-luther-as",
    "MA": "witt.source.marburg-articles",
    "SV": "witt.source.saxon-visitation-protocols",
    "RC": "witt.source.roman-confutation-of-the-augsburg-confession",
    "BE": "witt.source.leo-bull-exsurge-domine",
    "IV": "witt.source.melanchthon-instructions-for-the-visitors-of-parish",
    "PW": "witt.source.peter-revolution-of-1525-the-german-peasants",
    "FO": "witt.source.melanchthon-oratio-in-funere-reverendi-viri-d",
    "PWR": "witt.source.robert-translators-notes-and-public-domain-release",
    "BT": "witt.source.bente-concordia-triglotta",
    "BOC": "witt.source.book-of-concord",
    "BI": "witt.source.leonard-introduction-to-the-hymns-of-martin",
    "AND": "witt.source.andreas-theses-and-sermons-of-1521-as",
    "HS": "witt.source.luther-treatise-on-the-holy-sacrament",
    "DV": "witt.source.luther-de-votis-monasticis",
    "DT": "witt.source.luther-disputation-on-the-power-and-efficacy",
    "NS": "witt.source.luther-ein-neues-lied-wir-heben",
    "PF": "witt.source.luther-selections-from-luthers-prefaces-to-his",
}


def src(code: str, locus: str) -> dict:
    return {"source_id": S[code], "locus": locus, "license": "public-domain"}


def conf(formation_confidence: str, note: str, *, spec="B", ver="verified-via-authority",
         weight="load-bearing") -> dict:
    return {
        "citation_specificity": spec,
        "verification_state": ver,
        "evidentiary_weight": weight,
        "formation_confidence": formation_confidence,
        "divergence_note": note,
    }


# ---------------------------------------------------------------------------
# GRAVITIES -- one dict per Doc_04 §3 candidate G1-G13. AUTHORED content:
# description, manifestations, sources, confidence.divergence_note.
# MECHANICAL: id/name-bracket assembly, forces[]/interaction[] -> relations.
# ---------------------------------------------------------------------------
GRAVITIES = [
    dict(
        num="G1", slug="justified-by-faith-alone", classification="primary",
        name="Justified by faith alone [PRIMARY]",
        description=(
            "That the sinner is 'freely justified for Christ's sake, through faith' (AC IV, "
            "234-239), works and merit refused as the ground: 'faith alone, without works, "
            "justifies, makes free and saves' (Treatise on Christian Liberty, v2 11780-11781); "
            "'the promises of God give what the commands of God ask... He alone commands. He "
            "also alone fulfils' (v2 11817-11820). Its first, bounded form is the 1517 "
            "disputation's own target -- 'The true treasure of the Church is the Most Holy "
            "Gospel of the glory and the grace of God' (Th. 62) answers giving to the poor 'a "
            "better work than buying pardons' (Th. 43) -- and it is carried through seven Doc_02 "
            "evidence streams in both of this world's voices: disputation, treatise, sermon, "
            "catechesis, hymn, Bondage's sustained argument, and Melanchthon's confession, which "
            "calls it 'the chief topic of Christian doctrine' (Ap IV, 561-562). SIX-TEST SUMMARY "
            "(Doc_04 §3 G1): Repetition passes across all seven streams; Dependency passes -- G3 "
            "(the sacrament approached 'with faith alone'), G5 (the whole doctrine referred to "
            "the conscience, AC 552-553), G7 (works redefined by faith), and G9 (vows refused as "
            "merit) each state their dependence in their own texts; Formation passes as "
            "prescribed and preached, and is the one candidate where the founder's own testimony "
            "claims his own congregation already held it in 1522 ('you are more learned herein "
            "than I,' v2 14665-14666) -- Inferential-Thin as any wider congregation's holding, "
            "per Doc_02 §14's founder-prescription/congregational-reception line; Explanatory "
            "passes (it explains the 1517 protest's target, the 1520 treatises' structure, the "
            "catechism's Creed-over-Commandments order, and the Confession's own order, IV "
            "before V); Persistence passes 1517-1531 in every register, thinning to hymn and "
            "Table Talk only by the 1540s; Interaction passes, reinforcing with G2, G3, G4, G5, "
            "G8, G9, G12, thinly with G10 and G11, reshaping G6 and G7, competing only with G13. "
            "EVIDENTIAL CONFIDENCE: Documented. CLASSIFICATION: PRIMARY, passing all six with "
            "strong confidence; the confession's own voice calls it 'the chief topic.' "
            "CONFIDENCE/GRAVITY CROSS-CHECK: organizing strength and evidential confidence "
            "agree; no divergence. Register-and-voice spread (the strand-singular substitute, "
            "Doc_04 §4 -- this world is strand-singular per Doc_01 §6, and Article 21's test is "
            "run here as two scores rather than across strands): 4/4 -- both voices, six "
            "registers, and one thin household trace (Katharina von Bora, TT 3147-3148, on "
            "coldness in prayer rather than faith itself). Reception-side status: "
            "founder-attested as received, Wittenberg only, 1522. FORCES-CONNECTION NOTATION "
            "(Doc_04 §3 G1; Doc_08 §5): generated under the founding conviction [1B-1] and the "
            "laity's need for assurance [1B-2]; held and intensified once the bull and the "
            "Leipzig polemic turned an argument into the movement's identity [1A-2/2A-1]; "
            "intensified again into confessional definition at Augsburg (AC IV, 1530; Ap IV's "
            "'chief topic,' 1531) [2A-2]; re-fenced, not fractured, once the reform's own 'new "
            "spirits' put the formula to a use it was not built for -- the Large Catechism "
            "answers by 1529 that faith 'must have something which it believes... upon which it "
            "stands and rests' (LC 3916-3921) [2B-1]; carried past 1531 only in hymn and Table "
            "Talk [3B-2, beyond Doc_04's own notation]."
        ),
        manifestations=[
            "\"freely justified for Christ's sake, through faith... This faith God imputes for righteousness\" (AC IV, 234-239)",
            "\"faith alone, without works, justifies, makes free and saves\" (Treatise on Christian Liberty, v2 11780-11781)",
            "\"The true treasure of the Church is the Most Holy Gospel of the glory and the grace of God\" (Th. 62, v1 1387-1388)",
            "\"the Creed is a doctrine quite different from the Ten Commandments; for the latter teaches indeed what we ought to do, but the former tells what God does for us\" (LC 2967-2975)",
            "\"our would-be wise, new spirits assert that faith alone saves, and that works and external things avail nothing... faith must have something which it believes... upon which it stands and rests\" (LC 3916-3921)",
            "\"in this controversy the chief topic of Christian doctrine is treated\" (Ap IV, 561-562)",
        ],
        sources=[
            src("DT", "Th. 62, 43 (v1 1312-1313, 1387-1388): the indulgence-trade's own treasure named and refused"),
            src("GW", "v1 6834-6842: 'the first and highest... good work is faith in Christ'"),
            src("CL", "v2 11780-11826: 'faith alone... justifies, makes free and saves'; the commands/promises distinction"),
            src("LC", "LC 2967-2975 (Creed over Commandments); LC 3916-3921 (re-fenced against the 'new spirits')"),
            src("AC", "AC IV, 234-261: justification by faith articled and confessed before the Emperor"),
            src("AP", "Ap IV, 561-562, 1118-1120: 'the chief topic of Christian doctrine'"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the doctrine in both voices across seven streams (Doc_04 §3 G1); "
            "Inferential-Thin for any congregation beyond the founder's own Wittenberg testimony "
            "holding it, per Doc_02 §14's line, which this record does not cross. No "
            "Confidence/Gravity Cross-Check divergence: organizing strength and evidential "
            "confidence agree throughout (Doc_04 §3 G1, §6.3).",
        ),
        forces=[("1B-1", "generated"), ("1B-2", "generated"), ("1A-2", "assoc"), ("2A-1", "assoc"),
                ("2A-2", "assoc"), ("2B-1", "assoc"), ("3B-2", "assoc")],
    ),
    dict(
        num="G2", slug="the-word", classification="primary",
        name="The Word: Scripture's authority, and the agent that \"must do it\" [PRIMARY]",
        description=(
            "Scripture's authority against pope, councils and 'doctrines of men,' stated in two "
            "senses this world's own texts keep distinct without separating: an authority sense "
            "-- 'it is a wickedly invented fable... that the interpretation of Scripture or the "
            "confirmation of its interpretation belongs to the pope alone... the keys were not "
            "given to Peter alone, but to the whole community' (v2 2384-2390) -- and a restraint "
            "sense, tested first per Doc_03 3.1: 'the Word must do this thing, and not we poor "
            "sinners' (v2 14917-14918); 'I did nothing; the Word did it all' (14931). SIX-TEST "
            "SUMMARY (Doc_04 §3 G2): Repetition passes across seven streams, six of eight coded "
            "Luther registers (disputation and conversation absent); Dependency passes -- G3 "
            "(Word joined to element), G4 (the catechism as 'epitome of the entire Holy "
            "Scriptures'), G7 (office defined as ministry of the Word), G8 (the restraint sense "
            "is G8's own warrant), G12 (the Word as weapon) each state their dependence "
            "explicitly; Formation passes as program, Inferential-Thin as reception; Explanatory "
            "passes broadly -- the polemical register's whole structure, the definition of a "
            "sacrament, the Confession's condemnation of the Anabaptists, and the world's print "
            "pattern all trace to it; Persistence passes 1517-1531 and into the 1539/1543 "
            "prefaces, carrying a register difference (sharp vs. Melanchthon's additive "
            "'Scriptures... and the Church Catholic,' AC 631-633) that Doc_04 reads as one rule "
            "stated two ways, not two rules; Interaction passes, reinforcing G1, G3, G4, G5, G7, "
            "G9, G11, G12, reshaping G6 and G10, competing with G8 and G13 -- the G2-G8 "
            "competition is this ecology's sharpest internal tension. EVIDENTIAL CONFIDENCE: "
            "Documented -- the best-attested term in the library. CLASSIFICATION: PRIMARY; the "
            "force most other candidates state their own dependence on. CONFIDENCE/GRAVITY "
            "CROSS-CHECK: agree; no divergence. Register-and-voice spread: 4/4, with Karsthans's "
            "fictional peasant demanding 'the divine truth in our language' as the non-founder "
            "trace. Reception-side status: not attested beyond Wittenberg's own congregation, "
            "which the founder himself says has 'the pure Word of God' (v2 14744-14745). "
            "FORCES-CONNECTION NOTATION (Doc_04 §3 G2; Doc_08 §5): generated as the refusal of "
            "papal authority to bind conscience apart from Scripture, turned positive [1A-2 with "
            "1A-1]; intensified into the sharp 'under the bench' form under the bull and the "
            "Leipzig polemic [2A-1]; reshaped twice under the reform's own internal pressure -- "
            "in 1522 into the restraint of 'jus verbi... but not executio' against Karlstadt's "
            "pace, and in 1529-31 into an explicitly external Word (AC V) against the 'new "
            "spirits' [2B-1]; stated additively before the Emperor [2A-2]; is 'the thing "
            "printed' [1A-3/2B-2, beyond Doc_04]; and supplies the criterion ('the external "
            "Word') at the world's own internal edge at the window's close [3B-1]."
        ),
        manifestations=[
            "\"it is a wickedly invented fable... that the interpretation of Scripture or the confirmation of its interpretation belongs to the pope alone... the keys were not given to Peter alone, but to the whole community\" (v2 2384-2390)",
            "\"the Word must do this thing, and not we poor sinners\" (v2 14917-14918); \"I did nothing; the Word did it all\" (v2 14931)",
            "\"God's Word is not like some other silly prattle, as that about Dietrich of Berne, etc., but... the power of God\" (LC 143-145)",
            "\"through the Word and Sacraments, as through instruments, the Holy Ghost is given\" against those who think the Spirit comes \"without the external Word\" (AC 246-255)",
            "\"Dear Luther, write the divine truth in our language, in German, that we simple laymen also may read it\" (Karsthans, v3 10556-10558, an editor's quotation of a fictional peasant)",
        ],
        sources=[
            src("CN", "v2 2155-2244: the first 'wall,' Scripture's authority against a claimed papal monopoly"),
            src("ES", "v2 14850-14939: Sermon 2, the restraint sense, jus verbi/executio"),
            src("LC", "LC 130-154, 3861-3864: the Word as power, and as what joins to an element to make a sacrament; LC 3916-3921, the 'new spirits'"),
            src("AC", "AC 246-261, 631-633: the Word and Sacraments as instruments; the additive Scripture/Church Catholic form"),
            src("KH", "Karsthans's fictional peasant's demand for German Scripture, per Doc_02 §1.1 (Contested as opinion)"),
        ],
        confidence=conf(
            "Documented",
            "Documented across seven streams and both voices (Doc_04 §3 G2). No Confidence/"
            "Gravity Cross-Check divergence -- agrees throughout (§6.3). Doc_04 §4 records this "
            "as the candidate whose non-founder attestation (Karsthans) is itself Contested as "
            "evidence of peasant opinion, per Doc_02 §1.4 -- carried here, not resolved.",
        ),
        forces=[("1A-2", "generated"), ("1A-1", "generated"), ("2A-1", "assoc"), ("2B-1", "assoc"),
                ("2A-2", "assoc"), ("1A-3", "assoc"), ("2B-2", "assoc"), ("3B-1", "assoc")],
    ),
    dict(
        num="G3", slug="promise-and-sign", classification="primary",
        name="Promise and sign: the sacrament as God's promise joined to an element, received by faith [PRIMARY]",
        description=(
            "The sacrament as God's own promise joined to an element and received by faith, not "
            "a work performed: 'a testament... is a promise made by one about to die... If the "
            "mass is a promise... it is to be approached, not with any work or strength or "
            "merit, but with faith alone' (v2 7305-7344); baptism 'daily,' the Supper 'FOR YOU,' "
            "and 'many absolutions, so that we may strengthen our timid consciences' (v2 "
            "15694-15724); the reduction from seven sacraments to three and then two (v2 "
            "6695-6701; v1 2271-2272). SIX-TEST SUMMARY (Doc_04 §3 G3): Repetition passes across "
            "treatise, sermon, catechesis, confession and apology; Dependency passes -- G4's "
            "five parts, G3's examination clause before the Supper, and the world's public "
            "defense at Augsburg (AC XXIV) all depend on it; Formation passes as claimed "
            "practice (Sunday Mass, examination, absolution, communion 'together'), "
            "Widely-Accepted as claimed and Inferential-Thin as parish reality, per Discipline "
            "5; Explanatory passes -- it explains the 1520 reduction, the 1522 crisis (fought "
            "over the mass and both kinds), AC XXIV's apologetic, and the world's boundary "
            "against the Reformed carried at G10; Persistence passes 1519-1531 with a documented "
            "internal shift (1520 abolition-logic, 1522 pace, 1530 'retained'); no vendored "
            "service order survives; Interaction passes, reinforcing G1, G2, G4, G5, G9 (thin), "
            "G10, G11, G12, reshaped BY G6 (the sacrament's public form settled by territorial "
            "authority), competing with G8 and G13. EVIDENTIAL CONFIDENCE: Documented for the "
            "doctrine and the movement's own claimed practice; Widely Accepted for the one "
            "participant witness (Johann Walter); Inferential-Thin for practice beyond "
            "Wittenberg. CLASSIFICATION: PRIMARY -- passes all six, and three other candidates "
            "state their dependence on it; it is the gravity the world's one documented internal "
            "crisis (1522) was fought over. CONFIDENCE/GRAVITY CROSS-CHECK: agrees for the "
            "doctrine and claimed practice (Documented); the parish-practice half of the "
            "Formation Test is Inferential-Thin and is not relied on for the classification. "
            "Register-and-voice spread: 4/4 (Walter). Reception-side status: the movement's own "
            "claim (AC/Ap XXIV) plus one late participant; no parish outside Wittenberg. "
            "FORCES-CONNECTION NOTATION (Doc_04 §3 G3; Doc_08 §5): generated by refusal of the "
            "inherited seven-sacrament, sacrifice-of-the-mass system [1B-3]; intensified once "
            "the Babylonian Captivity was written against the bull's year [2A-1]; fractured "
            "internally in 1522, the mass abolished 'in wantonness, with no regard to proper "
            "order' [2B-1], and re-set by the founder's own appeal to 'the aid of the "
            "authorities' [2A-3]; shifted from the 1520 logic of abolition to the 1530 defense "
            "of a retained, examined, German-hymned Mass [2A-2]; pressed from outside by the "
            "Reformed rival, invisible in the library except at G10 [2A-6]; its service orders "
            "were never vendored [3B-2]."
        ),
        manifestations=[
            "\"a testament... is a promise made by one about to die... If the mass is a promise... it is to be approached, not with any work or strength or merit, but with faith alone\" (v2 7305-7344)",
            "\"we must have many absolutions, so that we may strengthen our timid consciences and despairing hearts... I cannot doubt I have a gracious God\" (v2 15694-15724)",
            "\"when the Word is joined to the element or natural substance, it becomes a Sacrament\" (LC 3861-3864)",
            "\"This is My body and blood, given and shed FOR YOU\" (LC 4135-4152)",
            "\"the Mass is retained among us, and celebrated with the highest reverence... none are admitted except they be first examined\" (AC 787-799)",
        ],
        sources=[
            src("BC", "v2 6695-7349: the reduction from seven to two/three; testament and promise; faith alone at the mass"),
            src("HS", "v1 2271-2272: the 1519 sacrament treatise's own three-part reduction"),
            src("ES", "v2 15694-15727: 'many absolutions,' the Sermons' own confessional practice"),
            src("LC", "LC 3861-3864, 4075-4154, 4250-4256: the Word joined to the element; 'for you'; examination"),
            src("AC", "AC 787-799: the Mass retained, examined, defended before the Emperor"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the doctrine and the movement's own claimed practice; Widely "
            "Accepted for Walter's participant testimony; Inferential-Thin for parish practice "
            "beyond Wittenberg (Doc_04 §3 G3, Discipline 5). No Confidence/Gravity Cross-Check "
            "divergence on the classification itself; the I/T half is named, not relied on.",
        ),
        forces=[("1B-3", "generated"), ("2A-1", "assoc"), ("2B-1", "assoc"), ("2A-3", "assoc"),
                ("2A-2", "assoc"), ("2A-6", "assoc"), ("3B-2", "assoc")],
    ),
    dict(
        num="G4", slug="household-catechism", classification="primary",
        name="The household catechism as this world's prescribed formation mechanism [PRIMARY]",
        description=(
            "The three parts every Christian must know, prescribed to be taught by the father, "
            "examined weekly, sung and prayed morning and evening: 'the ordinary Christian, who "
            "cannot read the Scriptures, is required to learn and know the Ten Commandments, the "
            "Creed, and the Lord's Prayer... these three contain fully and completely everything "
            "that is in the Scriptures' (v2 13182-13186); 'it is the duty of every father of a "
            "family to question and examine his children and servants at least once a week' (LC "
            "241-243); 'The Simple Way a Father Should Present Them to His Household' (SC 45). "
            "The candidate as generated is scoped deliberately: a claim about the PROGRAM, never "
            "a claim that any household actually held it (Doc_04 §3 G4). SIX-TEST SUMMARY: "
            "Repetition passes across catechesis, sermon (by "
            "implication), hymnal preface, conversation, confession, apology, and one "
            "participant witness; Dependency passes broadly; Formation SPLITS, and this is the "
            "document's central divergence -- passes as prescribed program, the most fully "
            "specified formation mechanism in the library, down to meal-time recitation and food "
            "withheld until repeated (LC 333-336); Inferential-Thin as achieved formation -- no "
            "visitation protocol, parish register, or lay witness confirms any household did it; "
            "Explanatory passes broadly; Persistence passes across registers 1520-1543 but FAILS "
            "across regions -- nothing shows any household or parish outside Wittenberg, scored "
            "'p' overall; Interaction passes, reinforcing G1, G2, G3, G5, G6, G7, G9, G10 (thin), "
            "G11, G12, reshaping G8, competing with G13. EVIDENTIAL CONFIDENCE: Documented for "
            "the prescriptive corpus; Widely Accepted for Walter; Inferential-Thin for any "
            "household's actual practice; Contested at the scholarly level for how reception "
            "should be read at all (the Strauss debate). CLASSIFICATION: PRIMARY, on the scope "
            "as generated -- the evidence supporting the candidate as scoped (the bulk of the "
            "1529 output plus the confessional pair) is Documented; a reviewer who reads the "
            "Framework's rule as requiring the whole gravity, reception included, would classify "
            "this Supporting instead, and this document states that alternative rather than "
            "hiding it (Doc_04 §3 G4). CONFIDENCE/GRAVITY CROSS-CHECK: DIVERGENCE, flagged and "
            "the build's highest-stakes -- organizing strength is Primary-grade for the program; "
            "evidential confidence is Documented for the program, Inferential-Thin for "
            "reception. Not upgraded across that line; the I/T side is named as outside what the "
            "classification covers. Register-and-voice spread: 4/4 for the program; Luther-only "
            "for the household-father mechanism specifically. Reception-side status: absent -- "
            "the single largest reception gap in the build. FORCES-CONNECTION NOTATION (Doc_04 "
            "§3 G4; Doc_08 §5): generated in response to what replaces the indulgence-"
            "confession-sacrament system as the laity's formation [1B-2]; shifted in audience "
            "1520-1529, from 'the ordinary Christian, who cannot read' to the negligent pastor "
            "and the household father, under the territorial church's own inspecting need "
            "[2A-3]; intensified by the internal force the founder's own testimony documents -- "
            "the Large Catechism preface exists, by its own account, because pastors are "
            "negligent [2B-3]; is the printed household object [1A-3]; held into the "
            "confessional corpus, entering the Book of Concord in 1580 by reference [3A-1/3B-2, "
            "beyond Doc_04]; carries the household's own daily petition for the prince [1A-1, "
            "beyond Doc_04]."
        ),
        manifestations=[
            "\"the ordinary Christian, who cannot read the Scriptures, is required to learn and know the Ten Commandments, the Creed, and the Lord's Prayer... these three contain fully and completely everything that is in the Scriptures\" (v2 13182-13186)",
            "\"it is the duty of every father of a family to question and examine his children and servants at least once a week\" (LC 241-243); \"until they repeat them, they should be given neither food nor drink\" (LC 333-336)",
            "\"The Simple Way a Father Should Present Them to His Household\" (SC 45)",
            "\"perhaps sing a song inspired by the Ten Commandments\" (SC 557-558)",
            "\"With the adversaries there is no catechization of the children whatever... With us the pastors and ministers of the churches are compelled publicly [and privately] to instruct and hear the youth\" (Ap 6893-6901)",
        ],
        sources=[
            src("LC", "LC 43-336: the preface's rebuke, the father's weekly examination, food withheld"),
            src("SC", "SC 45-668: the household-facing form, morning/evening devotions, the Home Chart"),
            src("AP", "Ap 6889-6901: the confessional pair's own attestation of catechization, moving Doc_03's Luther-only flag"),
            src("WAL", "Walter's household/parish charity-scholars, per Doc_02 §6"),
            src("TT", "TT 2394-2395: 'Brief Sentences of the Catechism, according as Luther used to teach and instruct his family at home'"),
        ],
        confidence=conf(
            "Documented",
            "DIVERGENCE, flagged (Doc_04 §3 G4, §6.3, the build's highest-stakes Confidence/"
            "Gravity Cross-Check): Documented for the prescriptive corpus and the program; "
            "Inferential-Thin for any household's or parish's actual practice; Contested at the "
            "scholarly level for how the visitation evidence should even be read (Strauss vs. "
            "Scribner/Kittelson/Karant-Nunn). Classified Primary on the Documented side only; "
            "the I/T side is named, never imported into the classification.",
        ),
        forces=[("1B-2", "generated"), ("2A-3", "assoc"), ("2B-3", "assoc"), ("1A-3", "assoc"),
                ("3A-1", "assoc"), ("3B-2", "assoc"), ("1A-1", "assoc")],
    ),
    dict(
        num="G5", slug="terrified-and-comforted-conscience", classification="primary",
        name="The terrified and comforted conscience: assurance against despair [PRIMARY]",
        description=(
            "Assurance against despair as what the doctrine is FOR: 'if you should ask them "
            "whether they are sure that what they do pleases God, they say, \"No\"; they do not "
            "know, or they doubt' (v1 6845-6856); the commands 'teach a man to know himself... "
            "and may despair of his powers,' and then 'the second part of the Scriptures stands "
            "ready -- the promises of God' (v2 11786-11807); 'so that I shall not and cannot "
            "despair: I cannot doubt I have a gracious God' (v2 15709-15724). SIX-TEST SUMMARY "
            "(Doc_04 §3 G5): Repetition passes across seven streams, both voices, from the first "
            "Theses to the Apology; Dependency passes, and unusually explicit -- G1 is REFERRED "
            "to it by the confession itself ('neither can it be understood apart from that "
            "conflict,' AC 552-553), G3's absolutions exist for it, G8's liberty is preached "
            "'only to poor, humble, captive consciences,' G6's church/state distinction is drawn "
            "'for the comforting of men's consciences'; Formation passes as the stated "
            "experiential goal of every register, Inferential-Thin as reception, with one "
            "filtered household trace (Katharina von Bora's negative report, Contested as "
            "verbatim); Explanatory passes -- it explains why the 1517 protest was about penalty "
            "and fear rather than abstract doctrine, why private confession was kept, and why "
            "liberty is limited by the weak; Persistence passes 1517-1531 in every register and "
            "into the 1524 hymn, thinning to Table Talk in the 1540s; Interaction passes, "
            "reinforcing G1, G2, G3, G4, G7 (thin), G8, G9, G11 (thin), G12, reshaping G6, "
            "competing with G13, with NO demonstrated relationship to G10 as read -- the one "
            "empty cell in an otherwise full row. EVIDENTIAL CONFIDENCE: Documented. "
            "CLASSIFICATION: PRIMARY -- the reasoning both ways is stated rather than smoothed: "
            "for Primary, the confession makes G1 depend on G5, not the reverse, and three "
            "further candidates state their dependence in their own texts; against, the "
            "conscience could be read as the SITE where G1 and G3 land rather than a generator "
            "of its own content -- the dependency the sources state, in the direction that "
            "decides it, outweighs the counter-case. CONFIDENCE/GRAVITY CROSS-CHECK: agree -- "
            "Documented, both voices; no divergence. Register-and-voice spread: 4/4 (Kate's "
            "sentence, negative and Contested). Reception-side status: one filtered household "
            "sentence reporting coldness. FORCES-CONNECTION NOTATION (Doc_04 §3 G5; Doc_08 §5): "
            "generated by what the world was responding to -- a laity taught to rely on "
            "indulgences, confession and the sacramental system for assurance -- stated as a "
            "POSITIVE organizing force [1B-1 with 1B-2]; intensified under the pope named 'a "
            "mere tormentor of the conscience' and under monastic bondage [2A-1]; intensified in "
            "1522 when the reform's own haste terrifies the weak on their deathbeds [2B-1]; "
            "intensified into the confessional register's most repeated word -- 'terrified,' 29 "
            "occurrences in the Apology [2A-2]. Not visibly touched by the Reformed rival or the "
            "Turk. Held; never fractured in what was read."
        ),
        manifestations=[
            "\"if you should ask them whether they are sure that what they do pleases God, they say, 'No'; they do not know, or they doubt\" (v1 6845-6856)",
            "\"the commands teach a man to know himself... and may despair of his powers... the second part of the Scriptures stands ready -- the promises of God\" (v2 11786-11807)",
            "\"we must have many absolutions, so that we may strengthen our timid consciences and despairing hearts against the devil and against God... I cannot doubt I have a gracious God\" (v2 15694-15724)",
            "\"consciences cannot be set at rest through any works, but only by faith... This whole doctrine is to be referred to that conflict of the terrified conscience, neither can it be understood apart from that conflict\" (AC 546-553)",
            "\"The Pope is a mere tormentor of the conscience\" (TT 3083-3084, Contested as verbatim)",
        ],
        sources=[
            src("DT", "v1 1205-1214: the disputation's own fear-and-despair theses, fourteen before Th. 30"),
            src("GW", "v1 6845-6856: no assurance without faith, 'they do not know, or they doubt'"),
            src("CL", "v2 11786-11826: the despair-then-promise sequence"),
            src("ES", "v2 15694-15727: the five comforts; 'I cannot doubt I have a gracious God'"),
            src("AC", "AC 546-553, 1281-1291: the whole doctrine referred to the terrified conscience"),
            src("AP", "Ap 566-567, 698-699: 'terrified consciences,' counted 29 times"),
        ],
        confidence=conf(
            "Documented",
            "Documented across seven streams, both voices, from the Theses to the Apology "
            "(Doc_04 §3 G5). No Confidence/Gravity Cross-Check divergence. The one filtered "
            "household trace (Katharina von Bora, TT 3147-3148) is Contested as verbatim and is "
            "a negative report -- carried as such, not smoothed into positive reception.",
        ),
        forces=[("1B-2", "generated"), ("1B-1", "generated"), ("2A-1", "assoc"), ("2B-1", "assoc"),
                ("2A-2", "assoc")],
    ),
    dict(
        num="G6", slug="two-governments", classification="supporting",
        name="The two governments: the temporal sword, obedience, and the prince as addressee [SUPPORTING]",
        description=(
            "The temporal sword ordained of God, obeyed 'save only when commanded to sin': "
            "'these people need no secular sword or law. And if all the world were composed of "
            "real Christians... no prince, king, lord, sword, or law would be needed' (v3 "
            "12139-12191); 'lawful civil ordinances are good works of God... Christians are "
            "necessarily bound to obey their own magistrates and laws save only when commanded "
            "to sin' (AC 411-428). SIX-TEST SUMMARY (Doc_04 §3 G6): Repetition passes across six "
            "streams; Dependency passes -- G4's program presupposes territorial support for "
            "pastors, G3's public form is settled 'with the aid of the authorities,' the "
            "Confession is signed by princes; Formation passes as taught obedience, but the "
            "library shows Wittenberg's council and the Saxon court only; Explanatory passes -- "
            "it explains the address-to-princes pattern, the condemnation of the Anabaptists by "
            "name, and why the settlement is territorial rather than empire-wide; Persistence "
            "scores 'p' -- documented 1520-1531 at Empire and court level, undocumented at the "
            "parish, and its two most consequential moments, 1525 and 1555, lie outside every "
            "vendored text; Interaction passes, reinforcing G4, G7, G9, G11 (thin), G12, G13 "
            "(thin), reshaping G3, reshaped by G1, G2, G5, G8, with NO demonstrated relationship "
            "to G10. EVIDENTIAL CONFIDENCE: Documented for the doctrine and court-level "
            "institutions; Widely Accepted for editorially reported events; the parish level "
            "absent. CLASSIFICATION: SUPPORTING -- it organizes the institutional dimension "
            "pervasively, but its own texts derive it from the Primaries (real Christians 'need "
            "no secular sword' because of G1; the sword has executio because the Word has only "
            "jus verbi, G2), and its Persistence fails exactly where the world's own political "
            "history was decided (1525, 1555). CONFIDENCE/GRAVITY CROSS-CHECK: agrees for what "
            "is in the library; a COVERAGE divergence is recorded instead of a confidence one -- "
            "the organizing strength this gravity almost certainly had across the whole window "
            "cannot be shown from this library, and the classification reflects the library, not "
            "the history. Register-and-voice spread: 3/4 -- no non-founder voice (the "
            "signatories and edicts are institutional, not a voice). Reception-side status: "
            "court and council only. FORCES-CONNECTION NOTATION (Doc_04 §3 G6; Doc_08 §5): "
            "generated within an empire of semi-autonomous princes, the only frame in which "
            "'obtain the aid of the authorities' means a territorial ruler [1A-1]; shifted in "
            "direction three times -- 1520 princes summoned as priests, 1523 the limit of "
            "obedience, 1530 princes as confessors [2A-3]; intensified under the "
            "popular-insurrectionary force in 1521-22, its climax in 1525 a named absence "
            "[2A-4]; reshaped in 1530 when Article XVI names the Anabaptists as the reason civil "
            "office must be affirmed [2B-1]; attested in its transforming, princes-as-confessors "
            "aspect at the Diet [3A-1], with its legal settlement of 1555 outside every vendored "
            "text [3A-2] -- the one gravity whose decisive fracture and settlement are both "
            "absent from the library."
        ),
        manifestations=[
            "\"these people need no secular sword or law. And if all the world were composed of real Christians... no prince, king, lord, sword, or law would be needed\" (v3 12139-12191)",
            "\"lawful civil ordinances are good works of God... Christians are necessarily bound to obey their own magistrates and laws save only when commanded to sin\" (AC 411-428)",
            "\"abolishing the mass rightly would have required that you had called upon God in earnest prayer, and had obtained the aid of the authorities\" (v2 14764-14765)",
            "\"our teachers, for the comforting of men's consciences, were constrained to show the difference between the power of the Church and the power of the sword\" (AC 1281-1285)",
            "the Augsburg Confession itself submitted by \"the undersigned Elector and Princes\" (AC 66), nine signatories (AC 1557-1567)",
        ],
        sources=[
            src("SA", "v3 12130-12199: the two kingdoms; who needs the sword and who does not"),
            src("AC", "AC 411-428, 1281-1291: lawful civil ordinances; the two powers distinguished"),
            src("ES", "v2 14764-14779: 'the aid of the authorities'; the Council's own call to preach"),
            src("EX", "v3 10663-10674: the common man's grievance, and insurrection forbidden"),
            src("TT", "TT 3473-3474: 'the Prince Elector well marked the Pope's unaccustomed humility' (Contested as verbatim)"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the doctrine and court-level institutions; Widely Accepted for "
            "editorially reported events (Doc_04 §3 G6). A COVERAGE divergence, not a confidence "
            "one, is recorded: the organizing strength this gravity likely had across the whole "
            "window cannot be shown from a library that lacks 1525 and 1555 (Doc_04 §6.3).",
        ),
        forces=[("1A-1", "generated"), ("2A-3", "assoc"), ("2A-4", "assoc"), ("2B-1", "assoc"),
                ("2A-5", "assoc"), ("3A-1", "assoc"), ("3A-2", "assoc")],
    ),
    dict(
        num="G7", slug="estate-office-and-calling", classification="supporting",
        name="Estate, office, and calling: \"we are all priests\" [SUPPORTING]",
        description=(
            "'It is pure invention that pope, bishops, priests and monks are to be called the "
            "\"spiritual estate\"... all Christians are truly of the \"spiritual estate,\" and "
            "there is among them no difference at all but that of office' (v2 2159-2164); good "
            "works done 'when they work at their trade, walk, stand, eat, drink, sleep' (v1 "
            "6863-6865). SIX-TEST SUMMARY (Doc_04 §3 G7): Repetition passes across seven "
            "streams; Dependency passes -- G4's father-catechist is this gravity in practice, "
            "G9's married estate is its 'most common and noblest' instance, G3's priest is an "
            "office-holder of Word and sacrament; Formation passes as taught, Inferential-Thin "
            "as reception; Explanatory passes -- the first of the 'three walls,' the Teutonic "
            "Order exhortation, the Home Chart's own shape, and the martyrs' ballad's climax all "
            "trace to it; Persistence passes across both voices with a documented WORDING SPLIT "
            "(office/estate vs. Melanchthon's calling) and a documented FENCE added by 1522-30 "
            "('regularly called') that the 1520 text did not carry; Interaction passes, "
            "reinforcing G2, G4, G6, G8, G9, G11 (thin), G12 (thin), thinly G5, reshaped by G1 "
            "and G3, competing with G13, with NO demonstrated relationship to G10. EVIDENTIAL "
            "CONFIDENCE: Documented. CLASSIFICATION: SUPPORTING -- it organizes the social "
            "dimension (who may do what, what counts as a holy station), but within the context "
            "the Primaries set: works are good only 'in faith' (G1), the office is defined by "
            "the Word (G2), the priest administers the sacraments (G3). It is also the gravity "
            "whose 1520 form is most visibly fenced by 1530, which is Supporting-shaped behavior "
            "-- it bends to the Primaries and to the forces rather than organizing them. "
            "CONFIDENCE/GRAVITY CROSS-CHECK: agree; no divergence. Register-and-voice spread: "
            "3/4 -- no non-founder voice; the Brussels monks are narrated by the founder, not by "
            "a witness. Reception-side status: absent. FORCES-CONNECTION NOTATION (Doc_04 §3 G7; "
            "Doc_08 §5): generated as the refusal of the first wall, the clerical estate's claim "
            "to be 'spiritual' over against the 'temporal' [1B-3 with 1A-2]; intensified in its "
            "monastic form -- the Teutonic knights, the martyrs' 'monkish garb' [1B-3]; FENCED "
            "under the reform's own internal pressure -- the universal priesthood of 1520 "
            "acquires, by the Sermons of 1522 and Article XIV of 1530, an explicit requirement "
            "of regular call [2B-1/3B-1]; reworded 'calling' in the confessional register under "
            "the imperial force [2A-2/3A-1]. Held."
        ),
        manifestations=[
            "\"It is pure invention that pope, bishops, priests and monks are to be called the 'spiritual estate'... all Christians are truly of the 'spiritual estate,' and there is among them no difference at all but that of office\" (v2 2159-2164)",
            "\"Through baptism all of us are consecrated to the priesthood\" (v2 2176-2177)",
            "\"no one should publicly teach in the Church or administer the Sacraments unless he be regularly called\" (AC 383-384)",
            "\"callings are unlike [one is called to rulership, a second to be father of a family, a third to be a preacher]... Callings are personal\" (Ap 10009-10017)",
            "the Brussels martyrs, \"Their monkish garb from them they take... True priests of God's own making\" (Hy 1789-1800)",
        ],
        sources=[
            src("CN", "v2 2159-2236: the priesthood of all believers; office, not estate"),
            src("TK", "v3 20887-20913: the Teutonic Order's monastic vows refused"),
            src("AC", "AC 383-384: 'regularly called' -- the 1530 fence"),
            src("AP", "Ap 10009-10017: 'calling,' Melanchthon's own word for office/estate"),
            src("NS", "Hy 1789-1800: the Brussels martyrs' hymn, \"True priests of God's own making\""),
        ],
        confidence=conf(
            "Documented",
            "Documented across seven streams, both voices, with a wording split (office/estate "
            "vs. calling) carried as an alias, not a divergence (Doc_04 §3 G7). No Confidence/"
            "Gravity Cross-Check divergence.",
        ),
        forces=[("1B-3", "generated"), ("1A-2", "generated"), ("2B-1", "assoc"), ("3B-1", "assoc"),
                ("2A-2", "assoc"), ("3A-1", "assoc")],
    ),
    dict(
        num="G8", slug="must-and-free", classification="tensional",
        name="\"Must\" and \"free\": liberty bound by love to the weak, and the pace of reform [TENSIONAL]",
        description=(
            "'A Christian man is a perfectly free lord of all, subject to none. A Christian man "
            "is a perfectly dutiful servant of all, subject to all' (v2 11618-11621); the "
            "gravity's own register, addressed to Wittenberg in March 1522: 'we must not look "
            "upon ourselves... but upon our neighbor... What you did was good, but you have gone "
            "too fast' (v2 14711-14728); 'Take note of these two things, \"must\" and \"free\"... "
            "Now do not make a \"must\" out of what is \"free\"' (14790-14796) -- then, by 1529, "
            "the same word turned the other way: pastors retaining 'no more of the Gospel than "
            "such a lazy, pernicious, shameful, carnal liberty' (LC 78-80). SIX-TEST SUMMARY "
            "(Doc_04 §3 G8): Repetition passes across treatise, sermon, catechesis, confession -- "
            "the 'must'/'free' wording itself is single-register, the gravity is not; Dependency "
            "passes -- G3's public form in 1522, G7's priestly restraint, G9's married priests "
            "and emptied monasteries, and G4's compulsory examination all depend on it; Formation "
            "passes as the one gravity documented ACTING on a specific congregation -- Wittenberg, "
            "March 1522, and the editor's own account that 'Carlstadt was silenced... Wittenberg "
            "bowed to law and order'; Explanatory passes -- it explains the 1522 transition, the "
            "mass's period arc, and why the Large Catechism of 1529 has to rebuke the opposite "
            "fault; Persistence passes 1520-1530 with a documented REVERSAL OF DIRECTION "
            "(restraining the fast in 1522, goading the slack in 1529); Interaction passes, the "
            "most competing row of any non-Tensional-looking candidate -- competing with G2 (the "
            "ecology's sharpest tension), G3, G10 (thin), reshaping G4 and G6, reshaped by G12 and "
            "G13, reinforcing G1, G5, G7, G9, G11 (thin). EVIDENTIAL CONFIDENCE: Documented for the "
            "texts; Widely Accepted for the 1522 outcome (editorial). CLASSIFICATION: TENSIONAL -- "
            "the persistent counter-force inside the reform against the reform's own logic: the "
            "Word licenses, love restrains, then, when restraint has produced sloth, the same word "
            "'liberty' is the charge. It does not organize the ecology broadly, but the ecology "
            "cannot be reduced to G1-G3 without it. CONFIDENCE/GRAVITY CROSS-CHECK: agree -- "
            "Tensional makes no claim the evidence cannot bear. Register-and-voice spread: 3/4, no "
            "non-founder voice. Reception-side status: one congregation, once, at the editor's "
            "word. FORCES-CONNECTION NOTATION (Doc_04 §3 G8; Doc_08 §5): GENERATED by the internal "
            "radical force of 1522 -- Karlstadt's and Zwilling's pace during the Wartburg absence "
            "is the occasion of every 'must'/'free' sentence [2B-1 with 2A-2, the Edict]; "
            "REVERSED in direction by the internal force the founder's own reception testimony "
            "documents -- by 1529 the danger is not haste but 'carnal liberty' [2B-3]; SETTLED "
            "under the imperial force as the confessional doctrine of adiaphora in rites (AC XV, "
            "XXVIII) [2A-2/3A-1]; applied, the same instrument, to the 'common man' under the "
            "popular force [2A-4]. Never fractured; it is the world's own instrument for NOT "
            "fracturing."
        ),
        manifestations=[
            "\"A Christian man is a perfectly free lord of all, subject to none. A Christian man is a perfectly dutiful servant of all, subject to all\" (v2 11618-11621)",
            "\"What you did was good, but you have gone too fast\" (v2 14711-14728)",
            "\"Take note of these two things, 'must' and 'free.' The 'must' is that which necessity requires... But 'free' is that in which I have choice... Now do not make a 'must' out of what is 'free'\" (v2 14790-14796)",
            "\"no more of the Gospel than such a lazy, pernicious, shameful, carnal liberty\" (LC 78-80)",
            "\"If you wish such liberty, you may just as well have the liberty to be no Christian\" (LC 4250-4296)",
        ],
        sources=[
            src("CL", "v2 11618-11631: the free lord / dutiful servant paradox"),
            src("ES", "v2 14711-14796: the 1522 sermons, restraint addressed to Wittenberg by name"),
            src("LC", "LC 78-97, 4244-4299: the 1529 reversal, 'carnal liberty' rebuked"),
            src("AC", "AC 391-398, 1068: adiaphora, liberty in rites, settled before the Emperor"),
            src("AND", "Karlstadt's 1521-22 theses, per Steimle's editorial account (context only)"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the texts; Widely Accepted for the 1522 outcome at the editor's word "
            "(Doc_04 §3 G8). No Confidence/Gravity Cross-Check divergence -- Tensional is the "
            "classification the evidence itself supports, not a downgrade from it.",
        ),
        forces=[("2B-1", "generated"), ("2A-2", "generated"), ("2B-3", "assoc"), ("3A-1", "assoc"),
                ("2A-4", "assoc")],
    ),
    dict(
        num="G9", slug="vows-chastity-and-marriage", classification="supporting",
        name="Vows, \"false chastity,\" and marriage [SUPPORTING]",
        description=(
            "The monastic estate refused, the married household and the married pastor "
            "affirmed: the Teutonic Knights told to 'give up your unchaste chastity and to "
            "marry' (v3 20887-20908); marriage as 'the most common and noblest estate, which "
            "pervades all Christendom' (LC 1687-1727); 'men, and that, priests, are cruelly put "
            "to death, contrary to the intent of the Canons, for no other cause than marriage' "
            "(AC 751-767). SIX-TEST SUMMARY (Doc_04 §3 G9): Repetition passes across seven "
            "streams including institutional evidence (the Teutonic Order's secularization); "
            "Dependency passes -- G4's household site is the married household, G7's 'most "
            "common and noblest estate,' G6's magistrates punish 'the scandals' of impure "
            "celibacy; Formation passes as taught and as the founder's own household (Kate, at "
            "one remove), Inferential-Thin beyond it; Explanatory passes; Persistence passes "
            "1520-1531 into the 1530s-40s Table Talk, but regionally only Wittenberg and Prussia "
            "(editorial); Interaction passes with THREE empty cells (no demonstrated "
            "relationship to G10, G11, G13 as read) -- the second-thinnest row, the mark of a "
            "gravity that organizes a bounded region. EVIDENTIAL CONFIDENCE: Documented for the "
            "argument; Widely Accepted for the practice (pastors' wives; the Order's "
            "secularization, editorial). CLASSIFICATION: SUPPORTING -- it organizes the "
            "household and monastic-refusal dimensions, but within G1 (vows refused as "
            "merit-works), G7 (marriage as estate), and G2 ('no man's law, no vow, can annul the "
            "commandment and ordinance of God,' AC 726-727). CONFIDENCE/GRAVITY CROSS-CHECK: "
            "agree; one flag carried rather than a divergence -- the SEEDBED QUESTION, whether "
            "this vocabulary is this world's own or the inherited Augustinian order's, is a "
            "comparative question this library cannot answer, logged as a cross-build item "
            "rather than resolved. Register-and-voice spread: 3/4 plus one filtered household "
            "sentence (Kate, as object of patience, not a voice on the term). Reception-side "
            "status: the founder's own household, at triple remove. FORCES-CONNECTION NOTATION "
            "(Doc_04 §3 G9; Doc_08 §5): generated from the inherited monastic apparatus refused "
            "-- the founder was a friar, the world's martyrs were monks, and the 'unchaste "
            "chastity' it names is its own former estate [1B-3]; intensified in both directions "
            "under the papal and territorial forces -- married priests 'cruelly put to death' is "
            "the confession's own report of persecution, and the Teutonic Order's conversion "
            "into a hereditary duchy is the gravity's largest institutional effect [2A-1/2A-3]; "
            "held into the confessional register, Articles XXIII and XXVII [2A-2]; the treatise "
            "that argued it in full, On Monastic Vows, was never vendored [3B-2]."
        ),
        manifestations=[
            "the Teutonic Knights told to \"give up your unchaste chastity and to marry\" (v3 20887-20908)",
            "marriage as \"the most common and noblest estate, which pervades all Christendom\" (LC 1687-1727)",
            "\"men, and that, priests, are cruelly put to death, contrary to the intent of the Canons, for no other cause than marriage\" (AC 751-767)",
            "\"I must have patience with Kate my wife\" (TT 3013-3014)",
            "\"Paul... calls that a doctrine of devils which forbids marriage\" (AC 766-767)",
        ],
        sources=[
            src("TK", "v3 20887-20913: the Order's vows refused; Albert's 1526 marriage, editorial"),
            src("LC", "LC 1687-1727: marriage as the most common and noblest estate"),
            src("AC", "AC 751-767, 1110-1115: married priests defended; vows refused as equal to baptism"),
            src("TT", "TT 3013-3014, 2432-2438: the founder's own married household"),
            src("DV", "On Monastic Vows -- never vendored (Doc_04 §3 G9), cited for the acknowledged absence only"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the argument; Widely Accepted for the practice (Doc_04 §3 G9). One "
            "flag, not a Cross-Check divergence: whether the vocabulary this gravity refuses is "
            "this world's own or the Augustinian order's inherited vocabulary is unanswerable "
            "from this library, and this record does not resolve it either way.",
        ),
        forces=[("1B-3", "generated"), ("2A-1", "assoc"), ("2A-3", "assoc"), ("2A-2", "assoc"),
                ("3B-2", "assoc")],
    ),
    dict(
        num="G10", slug="bodily-presence", classification="supporting",
        name="The bodily presence: \"truly present,\" \"in and under\" [SUPPORTING]",
        description=(
            "'It is the true body and blood of our Lord Jesus Christ, in and under the bread and "
            "wine' (LC 4075-4077); 'the Body and Blood of Christ are truly present, and are "
            "distributed to those who eat the Supper of the Lord; and they reject those that "
            "teach otherwise' (AC 322-324). SIX-TEST SUMMARY (Doc_04 §3 G10) -- the "
            "THINNEST row in the matrix, and the Framework's own warning sign surfaced rather "
            "than smoothed: Repetition passes (treatise 1519/1520, catechesis, confession, one "
            "word in Bondage); Dependency scores 'p' -- Doc_01's world-boundary against the "
            "Reformed depends on it, and G3 depends on it for its content at the Supper, but "
            "nothing in the formation PROGRAM depends on the mode of presence as distinct from "
            "the promise; Formation scores 'p' -- taught in the catechisms, but its formative "
            "edge (what it meant to hold this against neighbours who did not) is not in the "
            "library; Explanatory passes for one thing (the world-boundary) and is otherwise "
            "'p'; Persistence scores 'p' -- the doctrine is stated unchanged 1519/1529/1530, but "
            "the controversy in which it became this world's boundary is absent from every "
            "vendored text, a limit on what can be shown, not a counter-finding; Interaction "
            "passes but is the thinnest row in the document: reinforcing G3 only, reshaped BY "
            "G2, thinly reinforcing G1, G4, G11, G12, thinly competing with G8, and NO "
            "demonstrated relationship with G5, G6, G7, G9, G13 -- five empty cells. EVIDENTIAL "
            "CONFIDENCE: Documented for what the texts say; UNTAGGED (not one of the five "
            "confidence levels) for the organizing role assigned to it against the Reformed -- a "
            "cross-document assumption resting on the census and sibling documents, not on any "
            "rowed secondary source, pending the Marburg Articles' acquisition. CLASSIFICATION: "
            "SUPPORTING, within G3 -- on this library's evidence the bodily presence organizes "
            "little beyond the Supper itself; this does not doubt that the doctrine mattered "
            "enormously to this world's boundary, only that the evidence for that mattering is "
            "not yet vendored. CONFIDENCE/GRAVITY CROSS-CHECK: DIVERGENCE, of the INVERSE kind -- "
            "the assigned world-boundary weight exceeds what the library shows organizing, while "
            "the doctrine's own evidence is Documented; the classification follows the library "
            "and does not import weight from outside it. 'Supporting' is not to be read as "
            "'minor.' Register-and-voice spread: 3/4, no non-founder trace. Reception-side "
            "status: the founder's own 1520 claim about 'the simple faith... among the common "
            "people' -- Documented as claim, Inferential-Thin as fact. FORCES-CONNECTION "
            "NOTATION (Doc_04 §3 G10; Doc_08 §5): held unchanged across every phase read -- "
            "'truly contained' (1520), 'in and under' (1529), 'truly present' (1530) -- no shift "
            "in the texts; intensified under a force the library cannot show -- the Marburg "
            "Colloquy of 1529 is visible here only as the Confession's 'they reject those that "
            "teach otherwise' and one word in Bondage -- and fractured outward by reference to "
            "the census only, not by any vendored text [2A-6]; pressed by the internal radical "
            "force -- the 'new spirits' who 'mock at Baptism' answered in the same catechetical "
            "breath as the Supper [2B-1]; the Marburg Articles themselves remain unvendored "
            "[3B-2]."
        ),
        manifestations=[
            "\"It is the true body and blood of our Lord Jesus Christ, in and under the bread and wine\" (LC 4075-4077)",
            "\"the Body and Blood of Christ are truly present, and are distributed to those who eat the Supper of the Lord; and they reject those that teach otherwise\" (AC 322-324)",
            "\"I rejoice greatly that the simple faith of this sacrament is still to be found at least among the common people\" (v2 7143-7148)",
            "\"I will take my reason captive to the obedience of Christ, and clinging simply to His word, firmly believe... the bread is the body of Christ\" (v2 7185-7188)",
            "the one in-voice word, \"Sacramentarians,\" among the tares (Bondage, 16090-16092)",
        ],
        sources=[
            src("HS", "v2 7143-7224: the 1520 treatise's own 'simple faith,' reason taken captive"),
            src("LC", "LC 4069-4079: 'in and under'"),
            src("AC", "AC 322-324: 'truly present... reject those that teach otherwise'"),
            src("BW", "Co 16090-16092: 'Sacramentarians,' one word, OCR-recovered"),
            src("MA", "the Marburg Articles (1529) -- unvendored, the acquisition every layer of this force waits on"),
        ],
        confidence=conf(
            "Documented",
            "DIVERGENCE, of the inverse kind (Doc_04 §3 G10, §6.3): the doctrine's own evidence "
            "is Documented, but the world-boundary weight assigned to it (Doc_01 §8.1's 'diverge "
            "sharply and specifically at the Eucharist') is UNTAGGED -- it rests on the census "
            "and sibling documents, not on a rowed source, and is not imported into this "
            "record's classification.",
        ),
        forces=[("2A-6", "assoc"), ("2B-1", "assoc"), ("3B-2", "assoc")],
    ),
    dict(
        num="G11", slug="german-for-the-people", classification="supporting",
        name="German for the people: vernacular teaching and singing, Latin retained for the learned [SUPPORTING]",
        description=(
            "'the parts sung in Latin are interspersed here and there with German hymns, which "
            "have been added to teach the people' (AC 789-794); 'we retain the Latin language on "
            "account of those who are learning and understand Latin, and we mingle with it "
            "German hymns, in order that the people also may have something to learn' (Ap "
            "8512-8515). SIX-TEST SUMMARY (Doc_04 §3 G11): Repetition passes across nine "
            "sources -- treatise, hymnody, catechesis, confession, apology, three non-founder "
            "traces, institutional and material evidence; Dependency passes -- G4 exists in this "
            "medium, G3's examined communicants and German hymns, G2's Word reaches 'the "
            "ordinary Christian' only this way; Formation passes as claimed, with Johann Walter "
            "as the one participant confirmation; Explanatory passes -- the bilingual "
            "Confession, the hymn corpus, Karsthans's demand, and Duke George's ban on the "
            "German Testament all trace to it; Persistence passes 1520-1545 across registers and "
            "both voices, regionally Wittenberg only with a single outward trace (Prussia, per "
            "Polentz's letter); Interaction passes, reinforcing G2, G3, G4 strongly, thinly G1, "
            "G5, G6, G7, G8, G10, G12, reshaped by G13, with NO demonstrated relationship to G9. "
            "EVIDENTIAL CONFIDENCE: Documented for the texts and the movement's claimed "
            "practice; Widely Accepted for Walter, Karsthans, and the editorial print data. "
            "CLASSIFICATION: SUPPORTING -- an enabling MEDIUM through which G2 and G4 operate "
            "rather than a force generating its own formation content; its Dependency and "
            "Explanatory results are Primary-grade, but its content is not its own. "
            "CONFIDENCE/GRAVITY CROSS-CHECK: agree -- the candidate where evidence exceeds "
            "Author Gravity risk most comfortably; no divergence. Register-and-voice spread: "
            "4/4, the fullest non-founder attestation of any candidate. Reception-side status: "
            "Walter (late, laudatory, three hands) and a fictional peasant. FORCES-CONNECTION "
            "NOTATION (Doc_04 §3 G11; Doc_08 §5): generated by print as medium together with the "
            "laity's own need [1A-3 with 1B-2]; intensified when the German Testament became "
            "what Duke George's territorial ban targeted [2A-3]; shifted under the imperial "
            "force into the Apology's explicit two-tier rule, Latin for learners, German for the "
            "people [2A-2]; corrupted at its own edge, by 1543, when the hymns are 'perverted "
            "the more they are printed' and must be fenced -- the same print force turned inward, "
            "and the internal force the founder's own testimony documents late in its own life "
            "[2B-4/2B-3]; the tunes themselves were lost at the last transmission step [2B-2]."
        ),
        manifestations=[
            "\"the parts sung in Latin are interspersed here and there with German hymns, which have been added to teach the people\" (AC 789-794)",
            "\"we retain the Latin language on account of those who are learning and understand Latin, and we mingle with it German hymns, in order that the people also may have something to learn\" (Ap 8512-8515)",
            "\"Dear Luther, write the divine truth in our language, in German, that we simple laymen also may read it\" (Karsthans, v3 10556-10558)",
            "\"He kept me three weeks long at Wittenberg... until the first German Mass was sung in the parish church\" (Walter, Hy 766-768)",
            "\"the earliest of our hymns are more perverted the more they are printed... lest strange and unsuitable songs come to be sold under our name\" (Hy 1065-1087)",
        ],
        sources=[
            src("HYP", "the hymnal prefaces, 1524-1543: purpose, audience, and the 1543 fence"),
            src("KH", "Karsthans's fictional peasant, per Doc_02 §1.1 (Contested as opinion)"),
            src("WAL", "Walter's reminiscence of the first German Mass sung in the parish church"),
            src("AC", "AC 789-794: the ceremony rationale, German hymns teaching the people"),
            src("AP", "Ap 8512-8515: the two-tier rule, Latin retained, German added"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the texts and claimed practice; Widely Accepted for Walter, "
            "Karsthans, and the print data (Doc_04 §3 G11). No Confidence/Gravity Cross-Check "
            "divergence -- evidence exceeds Author Gravity risk here more comfortably than for "
            "any other candidate.",
        ),
        forces=[("1A-3", "generated"), ("1B-2", "generated"), ("2A-3", "assoc"), ("2A-2", "assoc"),
                ("2B-4", "assoc"), ("2B-3", "assoc"), ("2B-2", "assoc")],
    ),
    dict(
        num="G12", slug="embattled-christendom", classification="supporting",
        name="Embattled Christendom: the devil, the pope, and the Turk as one adversary; the Word as weapon [SUPPORTING]",
        description=(
            "'here we battle not against pope or bishop, but against the devil, and do you "
            "imagine he is asleep? He sleeps not... he would make a flank attack' (v2 "
            "14752-14756); the hymn's own compression, 'The old evil foe, / Means us deadly "
            "woe... One little word can fell him' (Hy 3671-3705). SIX-TEST SUMMARY (Doc_04 §3 "
            "G12): Repetition passes across eight streams, both voices; Dependency passes -- "
            "prayer, hymnody, the polemical register's whole naming practice, G5's assurance "
            "'against the devil,' G8's 'flank attack' all depend on it; Formation passes as sung "
            "and prayed daily by prescription, Inferential-Thin as reception, though even Kate's "
            "one sentence is framed by this gravity ('the devil drives his servants... we are "
            "very cold'); Explanatory passes -- the vehemence of the polemical register, the "
            "naming shift from 'Antichrist' to 'the Church of Rome,' the Confession's own "
            "opening on the Turk, and the 1522 crisis read as the devil's stratagem all trace to "
            "it; Persistence passes 1520-1545, both voices, every register; Interaction passes, "
            "an almost uniformly reinforcing row -- reinforcing G1-G6 and G13, thinly G7, G9, "
            "G10, G11, RESHAPING G8 (the adversary frame gives G8's restraint its urgency). "
            "EVIDENTIAL CONFIDENCE: Documented for what the texts say; the apocalyptic "
            "interpretive frame some scholarship places over it is Dominant Modern "
            "Reconstruction at most and unread -- this record builds nothing on it. "
            "CLASSIFICATION: SUPPORTING -- it passes all six strongly and a reviewer could argue "
            "Primary, but what it organizes is the ecology's AFFECTIVE AND ADVERSARIAL FRAME, "
            "the Layer-2 consciousness of the forces in the Forces Framework's own terms, and "
            "the Word it wields is G2's own: 'One little word can fell him.' It functions within "
            "the context G1 and G2 set. CONFIDENCE/GRAVITY CROSS-CHECK: agree; no divergence. "
            "Register-and-voice spread: 4/4, Kate's sentence sitting inside it. Reception-side "
            "status: one filtered household sentence. FORCES-CONNECTION NOTATION (Doc_04 §3 G12; "
            "Doc_08 §5): THIS GRAVITY IS THE WORLD'S OWN LAYER-2 READING OF THE EXTERNAL FORCES "
            "themselves -- its name for the papal force ('Antichrist in Rome'), for the Turk "
            "('that most atrocious, hereditary, and ancient enemy'), and for the internal "
            "radical force (the devil's 'flank attack'; the 'new spirits') [2A-1, 2A-5, 2B-1]; "
            "intensified under each of them; a naming shift under the imperial force, "
            "'Antichrist' in the polemical register becoming 'the Church of Rome' in the "
            "confessional -- a shift in naming, not in the frame [2A-2/3A-1]; inherits the "
            "saints' functional protections it refuses and replaces them with the Word as 'holy "
            "water' [1B-3]. Held in every register; the 1529 hymn is its most compressed form."
        ),
        manifestations=[
            "\"here we battle not against pope or bishop, but against the devil, and do you imagine he is asleep? He sleeps not... he would make a flank attack\" (v2 14752-14756)",
            "\"The old evil foe, / Means us deadly woe... One little word can fell him\" (Hy 3671-3705)",
            "\"the Word an exceedingly effectual help against the devil, the world, and the flesh... the true holy water and holy sign from which he flees\" (LC 130-138)",
            "\"the kingdom of his Vicar, the Antichrist in Rome... is sore beset\" (v1 408-409)",
            "the Diet summoned \"concerning measures against the Turk, that most atrocious, hereditary, and ancient enemy of the Christian name and religion\" (AC 49-51)",
        ],
        sources=[
            src("ES", "v2 14752-14775: 'the devil's flank attack,' the adversary frame addressed to a congregation"),
            src("FB", "the hymn itself, \"Ein' feste Burg,\" 'the old evil foe,' 'one little word can fell him'"),
            src("LC", "LC 130-154, 451-455: the Word as help against the devil; the saints' functions replaced"),
            src("PF", "v1 404-409: the 1545 preface's 'Antichrist in Rome,' 'his time is short'"),
            src("AC", "AC 49-58: the Diet's own agenda, 'measures against the Turk'"),
        ],
        confidence=conf(
            "Documented",
            "Documented for what the texts say (Doc_04 §3 G12). No Confidence/Gravity "
            "Cross-Check divergence. The apocalyptic reading some secondary literature (Oberman) "
            "places over this frame is Dominant Modern Reconstruction at most and is neither "
            "adopted nor refuted here -- unread, and not built on.",
        ),
        forces=[("2A-1", "assoc"), ("2A-5", "assoc"), ("2B-1", "assoc"), ("2A-2", "assoc"),
                ("3A-1", "assoc"), ("1B-3", "assoc")],
    ),
    dict(
        num="G13", slug="hearers-and-repeaters-of-words", classification="tensional",
        name="\"Hearers and repeaters of words\": the founder's persistent testimony that the Gospel is taught and not held [TENSIONAL]",
        description=(
            "'Let us beware lest Wittenberg become Capernaum. I notice that you have a great "
            "deal to say of the doctrine which is preached to you, of faith and of love. This is "
            "not surprising; an ass can almost intone the lessons... God does not want hearers "
            "and repeaters of words, but doers and followers' (v2 14676-14688, 1522); 'the "
            "common people regard the Gospel altogether too lightly, and we accomplish nothing "
            "extraordinary even though we use all diligence' (LC 80-82, 1529). SIX-TEST SUMMARY "
            "(Doc_04 §3 G13): Repetition passes across sermon, catechesis, hymnal preface and "
            "conversation -- four registers across two decades, the one register with a "
            "household voice; Dependency passes -- G4's pastor-facing form states this as its "
            "own reason for existing, G3's and G4's examination clauses presuppose it, G8's 1529 "
            "reversal is its effect; Formation passes in the NEGATIVE and as program -- it "
            "shapes what the movement DOES (daily exhortation, examination, food withheld, "
            "hymnals revised with names attached), but as a description of participants it is "
            "Inferential-Thin and Contested (the Strauss debate: does the visitation evidence "
            "show failure, or measure the wrong thing? nothing in the library adjudicates); "
            "Explanatory passes -- it explains why the 1529 catechisms exist at all, why the "
            "Small Catechism is scripted for a father rather than addressed to a believer, and "
            "why the 1543 hymnal names its authors; Persistence passes in the founder's own "
            "voice across the window and FAILS beyond it -- no independent witness at any date; "
            "Interaction passes with the most COMPETING row in the matrix -- competing with G1, "
            "G2, G3, G4, G5, G7 (each is the thing taught and not held), reshaping G8 and G11, "
            "reinforcing G12 and thinly G6, with NO demonstrated relationship to G9, G10. "
            "EVIDENTIAL CONFIDENCE: Documented as the founder's own testimony; Contested as a "
            "description of fact; Inferential-Thin for any claim about any actual congregation, "
            "parish, or household. CLASSIFICATION: TENSIONAL -- the persistent, unresolved "
            "pressure the ecology cannot be reduced without: every Primary in this document is, "
            "in the founder's own testimony, taught more than held, and the world's most "
            "distinctive institutional feature (the self-checking visitation, by reference) is "
            "its answer. It does not organize broadly -- it generates programs, not content. It "
            "is NOT 'lay experience' under another name: this gravity is what the founder said; "
            "lay experience is what no vendored source says. CONFIDENCE/GRAVITY CROSS-CHECK: "
            "DIVERGENCE, flagged and BARRED FROM UPGRADE in a specific direction -- organizing "
            "strength is high (it generated the entire 1529 corpus), evidential confidence is "
            "Documented for the testimony, Contested/Inferential-Thin for the state of affairs "
            "it describes. Classified Tensional on the Documented half; NO DOWNSTREAM USE OF "
            "THIS RECORD MAY CITE IT AS EVIDENCE THAT SAXON CONGREGATIONS WERE IGNORANT, COLD, "
            "OR NEGLIGENT. Register-and-voice spread: 2/4, the only candidate below 3/4 -- no "
            "Melanchthon (the Apology's reception passage is POSITIVE and is not this gravity), "
            "congregational-facing registers and conversation only. Reception-side status: THIS "
            "CANDIDATE IS ITSELF THE FOUNDER'S RECEPTION REPORT, which is exactly why it cannot "
            "stand in for reception. FORCES-CONNECTION NOTATION (Doc_04 §3 G13; Doc_08 §5, 2B-3): "
            "this gravity IS Layer 2 of a force Doc_02 §13 could not document at Layer 1 -- the "
            "parish's actual state, the territorial force's own inspecting arm, absent from the "
            "library [2A-3]; its object shifts three times -- 1522 one congregation's conduct, "
            "1529 the parishes' pastors, people and nobles, 1543 the print market -- and the "
            "founder's response shifts with it, rebuke, then program, then print-control [2B-1, "
            "read as the devil's work; 2B-4, its late object]; its occasion by subtraction is the "
            "Easter compulsion's own lifting, reported by the founder as why some now go years "
            "without the Sacrament [2A-1, beyond Doc_04]; the one text that would give it an "
            "institutional rather than homiletic form, the Small Catechism's 1529 preface, was "
            "never vendored [2B-2/3B-2]. Never resolved in the library; that is what makes it "
            "Tensional."
        ),
        manifestations=[
            "\"Let us beware lest Wittenberg become Capernaum... God does not want hearers and repeaters of words, but doers and followers\" (v2 14676-14688)",
            "\"we see to our sorrow that many pastors and preachers are very negligent in this, and slight both their office and this teaching\" (LC 51-52)",
            "\"the common people regard the Gospel altogether too lightly, and we accomplish nothing extraordinary even though we use all diligence\" (LC 80-82)",
            "\"there is no limit to this perpetual amending by every one indiscriminately according to his own liking... lest strange and unsuitable songs come to be sold under our name\" (Hy 1065-1087)",
            "Katharina von Bora: \"Sir! how is it, that in Popedom they pray so often with great vehemence, but we are very cold and careless in praying?\" -- answered, \"the devil driveth on his servants continually; they are diligent... but we\" (TT 3147-3150, Contested as verbatim)",
        ],
        sources=[
            src("ES", "v2 14676-14688: the 1522 rebuke, 'hearers and repeaters of words'"),
            src("LC", "LC 51-97, 4240-4265: the 1529 preface's rebuke of pastors, people, and nobles"),
            src("HYP", "Hy 1065-1087: the 1543 hymnal preface, print corrupted, names required"),
            src("TT", "TT 3147-3150: Katharina von Bora's one question and its answer"),
            src("SV", "the Saxon visitation protocols -- unvendored (Doc_04 §3 G13), cited for the absence only"),
        ],
        confidence=conf(
            "Contested",
            "DIVERGENCE, flagged and barred from upgrade (Doc_04 §3 G13, §6.3): Documented as "
            "the founder's own testimony across four registers and two decades; Contested and "
            "Inferential-Thin as a description of any actual congregation's state (the Strauss "
            "vs. Scribner/Kittelson/Karant-Nunn debate, unresolved in the library). Classified "
            "Tensional on the Documented half only. No downstream record may cite this record as "
            "evidence that any Saxon congregation was in fact ignorant, cold, or negligent -- "
            "only that the founder said so, repeatedly, in his own voice.",
        ),
        forces=[("2B-3", "assoc"), ("2A-3", "assoc"), ("2B-1", "assoc"), ("2B-4", "assoc"),
                ("2A-1", "assoc"), ("2B-2", "assoc"), ("3B-2", "assoc")],
    ),
]

GRAVITY_BY_NUM = {g["num"]: g for g in GRAVITIES}

# ---------------------------------------------------------------------------
# FORCES -- one dict per Doc_08 §3 force entry, cells 1A-1 through 3B-2.
# ---------------------------------------------------------------------------
FORCES = [
    dict(
        cell="1A-1", slug="imperial-frame", kind="initiating", matrix_cell="1A",
        name="The imperial frame: an empire of semi-autonomous princes under a contested papal authority [1A - initiating/external]",
        description=(
            "LAYER 1 (Historical Event). An empire of numerous semi-autonomous princes and "
            "cities, its own political fragmentation part of why a territorial, prince-by-prince "
            "settlement rather than a single empire-wide resolution became this world's eventual "
            "legal shape (Doc_01 §7, Documented). The library's own institutional evidence: the "
            "Diets, the Edict of Worms, the Wittenberg council's own 1522 ordinance, and the "
            "Confession's nine signatories -- an Elector, princes, and two city senates (AC "
            "1557-1567). The 1517 letter goes to Albrecht, Archbishop of Magdeburg and Mainz; "
            "Christian Nobility is addressed to 'the German estates' -- the founding act's own "
            "address-space is the frame itself. LAYER 2 (World's Own Experience). Named by "
            "office and by bread, never as a system: the Diet summoned 'concerning measures "
            "against the Turk... and dissensions in the matter of our holy religion' (AC 50-54); "
            "'the undersigned Elector and Princes' (AC 66) confessing 'our lands' (AC 81-83); the "
            "founder's own word for the frame is the Council that called him, 'I was regularly "
            "called by the Council to preach in this place' (v2 14778-14779). In the household's "
            "own prayer the frame is felt as the loaf: the prince is the one 'by which most of "
            "all God preserves to us our daily bread,' and a prince's coat-of-arms would more "
            "properly carry 'a loaf of bread instead of a lion' -- a wish the text argues for, "
            "not a description of an existing practice (LC 3471-3484). LAYER 3 (Formation "
            "Impact). Generated G6 -- 'an empire of semi-autonomous princes is the only frame in "
            "which \"obtain the aid of the authorities\" means a territorial ruler' -- and with "
            "it the whole address-to-princes pattern of the treatise register. Supplied the "
            "space in which the papal refusal (1A-2) could be ADMINISTERED rather than merely "
            "argued. Gave G6 its Layer-2 image, the loaf, and the household's daily petition "
            "(G4, G6)."
        ),
        manifestations=[
            "the Diet summoned \"concerning measures against the Turk... and dissensions in the matter of our holy religion\" (AC 50-54)",
            "\"the undersigned Elector and Princes\" (AC 66), submitting \"the Confession of our preachers and of ourselves\" (AC 81-83)",
            "\"I was regularly called by the Council to preach in this place\" (v2 14778-14779)",
            "the prince as the one \"by which most of all God preserves to us our daily bread\"; a coat-of-arms that should carry \"a loaf of bread instead of a lion\" (LC 3471-3484)",
            "the Confession's nine signatories: an Elector, princes, and two city senates (AC 1557-1567)",
        ],
        sources=[
            src("AC", "AC 50-58, 66-83, 1557-1567: the Diet's own summons, the confessing princes, the signatories"),
            src("CN", "the address to 'the German estates' -- the treatise's own audience"),
            src("ES", "v2 14764-14779: 'the aid of the authorities'; the Council's own call"),
            src("LC", "LC 3449-3541: the fourth petition, the prince as the guarantor of daily bread"),
        ],
        confidence=conf(
            "Documented",
            "Documented as to the documents and signatories (Doc_08 Cell 1A, Force 1A-1); Widely "
            "Accepted as to the editorially reported events (the Edict, the council ordinance). "
            "No scholarly tension recorded on the frame's existence.",
        ),
    ),
    dict(
        cell="1A-2", slug="papal-force-initiating", kind="initiating", matrix_cell="1A",
        name="The papal force, initiating: the indulgence trade, the Leipzig polemic, and the bull, 1517-1521 [1A - initiating/external]",
        description=(
            "LAYER 1 (Historical Event). Indulgence sales, protested in the letter to Albrecht "
            "of Mainz with the Theses as its enclosure, subscribed 'From Wittenberg on the Vigil "
            "of All Saints, MDXVII' (Documented as to the letter; the posting of the Theses "
            "itself is Contested since Iserloh 1961, against the editors' own 'mid-day' "
            "narrative). The response: Alveld's and Emser's tracts, answered in 1520-21; the "
            "bull EXSURGE DOMINE (15 June 1520) with its forty-one condemned articles, answered "
            "article by article -- all reaching the library only as quoted by the side that "
            "answered them, structurally one-sided and disclosed as such. Print carried the "
            "exchange: The Papacy at Rome in twelve editions. LAYER 2 (World's Own Experience). "
            "At the origin, a doctrine that has misplaced the Church's treasure -- 'The true "
            "treasure of the Church is the Most Holy Gospel of the glory and the grace of God' "
            "(Th. 62); within three years, a claimed monopoly on Scripture -- 'the keys were not "
            "given to Peter alone, but to the whole community' (v2 2384-2390); looking back in "
            "1545, one name and one simile for the whole force -- 'the kingdom of his Vicar, the "
            "Antichrist in Rome... is sore beset' (v1 408-409), the devil raging 'like one who "
            "well knows and feels that his time is short.' Reported-Experience Status applies to "
            "the 'Antichrist' naming as the world's own reading, not an adopted apocalyptic "
            "thesis. LAYER 3 (Formation Impact). Generated G2 as the refusal turned positive, "
            "and G7 as the refusal of the first wall; intensified G1 -- the bull's condemned "
            "articles and the Leipzig polemic turned an argument into the movement's identity. "
            "Produced the polemical register itself, and set the pitch G12 would carry before "
            "the imperial force softened its naming (2A-1, 2A-2)."
        ),
        manifestations=[
            "the Theses, enclosed with the letter to Albrecht of Mainz, subscribed \"From Wittenberg on the Vigil of All Saints, MDXVII\"",
            "\"The true treasure of the Church is the Most Holy Gospel of the glory and the grace of God\" (Th. 62, v1 1387-1388)",
            "\"it is a wickedly invented fable... that the interpretation of Scripture or the confirmation of its interpretation belongs to the pope alone... the keys were not given to Peter alone, but to the whole community\" (v2 2384-2390)",
            "\"the kingdom of his Vicar, the Antichrist in Rome... is sore beset\" (v1 408-409)",
            "The Papacy at Rome, twelve known editions, all quartos (v1 12304-12309, editorial)",
        ],
        sources=[
            src("DT", "the Ninety-Five Theses and the covering letter to Albrecht of Mainz"),
            src("PR", "the answer to Alveld, The Papacy at Rome"),
            src("BE", "Exsurge Domine (1520), the forty-one condemned articles -- reaching the library only via the answering texts"),
            src("PF", "v1 404-409: the 1545 preface's naming of 'the Antichrist in Rome'"),
        ],
        confidence=conf(
            "Documented",
            "Documented as to the answering texts and the excommunication process (Doc_08 Cell "
            "1A, Force 1A-2); Contested for the Theses' own posting (Iserloh 1961 against the "
            "editors' 'mid-day' narrative), carried and not resolved.",
        ),
    ),
    dict(
        cell="1A-3", slug="print-as-medium", kind="initiating", matrix_cell="1A",
        name="Print as medium and press [1A - initiating/external]",
        description=(
            "LAYER 1 (Historical Event). Documented almost entirely in the editorial layer: the "
            "Theses in three editions within two months, at Wittenberg, Nürnberg, and as far as "
            "Basel; The Papacy at Rome in twelve known quarto editions, printers named; Karsthans "
            "in ten editions; the Grunenberg press reaching Duke George within days. Declined as "
            "a gravity in its own right (an Author-Gravity 'layer-only' candidate, Doc_04 §2.2) "
            "and carried here instead. Initiating in the strict sense: no vendored text reaches a "
            "reader except through it, and the world's first act was a printed disputation. "
            "LAYER 2 (World's Own Experience). The world does not name the press; it names what "
            "the press does and fears it. The medium is the way 'the divine truth' reaches 'us "
            "simple laymen' -- the fictional peasant's demand for German (v3 10556-10558) -- and "
            "the way 'the blessed Gospel' is brought 'into full play' by hymns (Hy 909-912). But "
            "already in 1539 the founder wishes his own printed books 'forgotten and destroyed' "
            "so that 'the Bible would have kept its place in the pulpit' (v1 260-261, 329-330), "
            "and 'the Bible has come to lie forgotten in the dust under the bench' (v1 268-269) "
            "is his own image of what books do to the Book. LAYER 3 (Formation Impact). "
            "Generated G11 together with the laity's own need (1B-2) -- 'the medium and the "
            "audience'; is 'the thing printed' for G2 and 'the printed household object' for G4. "
            "Made the ecology's material substrate the printed quarto and the hymn-sheet. Its "
            "later turn against the world is a separate, internal entry (2B-4), since by 1529-43 "
            "the pressure comes from the world's own output."
        ),
        manifestations=[
            "the Theses in three editions within two months -- Wittenberg, Nürnberg, and Basel (v1 488-491)",
            "The Papacy at Rome's \"twelve known editions are all quartos,\" printers named (v1 12304-12309)",
            "\"Dear Luther, write the divine truth in our language, in German, that we simple laymen also may read it\" (Karsthans, v3 10556-10558)",
            "\"I would gladly have seen all my books forgotten and destroyed\" (v1 260-261); \"the Bible has come to lie forgotten in the dust under the bench\" (v1 268-269)",
        ],
        sources=[
            src("PR", "The Papacy at Rome's own print history, twelve editions, editorial (v1 12304-12309)"),
            src("KH", "Karsthans, ten editions, editorial (v3 10574-10575)"),
            src("PF", "v1 260-269, 329-330: the founder's own wish that his books be forgotten"),
            src("HYP", "Hy 909-912: the medium bringing 'the blessed Gospel... into full play'"),
        ],
        confidence=conf(
            "Widely Accepted",
            "Widely Accepted as to the editors' bibliographical data (Doc_08 Cell 1A, Force "
            "1A-3); no primary-voice claim about print itself, only about what it carried.",
        ),
    ),
    dict(
        cell="1B-1", slug="friars-conviction", kind="initiating", matrix_cell="1B",
        name="A friar-professor's conviction that the church's practice rested on an authority Scripture does not support [1B - initiating/internal]",
        description=(
            "LAYER 1 (Historical Event). A conviction 'argued first over the specific, bounded "
            "question of indulgence sales, then rapidly generalized' (Doc_01 §7, Documented). "
            "Its documented object is what the church claims to hold and dispense -- a treasury "
            "of merit exchangeable for the remission of penalty -- the specific mechanism the "
            "Theses attack, and this world's own generating occasion. The conviction's own "
            "narrative is NOT in the library: the 1545 preface stops before the 'tower "
            "experience' passage, and the dating of any 'breakthrough' is Contested and moot for "
            "this library. What IS in the library is the conviction's public form: the Theses "
            "and the 1520 treatises. LAYER 2 (World's Own Experience). The founder's own account "
            "of how it began is a preface written in 1545 with an explicit frame -- 'Such a Saul "
            "was I at that time' (v1 365); he 'fell, quite unexpectedly, into this wrangling and "
            "contention' (v1 390-391) -- Contested as self-characterization, carried as "
            "Reported-Experience Status: how the world's founder told the world its own "
            "beginning, not established fact. The conviction's substance in its own first words: "
            "giving to the poor 'a better work than buying pardons' (Th. 43); 'No one is sure "
            "that his own contrition is sincere' (Th. 30). The world's own refusal of the "
            "founder's PERSON as its organizing force is on record: 'I did nothing; the Word did "
            "it all' (v2 14931). LAYER 3 (Formation Impact). Generated G1 in its first, bounded "
            "form, and through the same disputation G5's founding case -- the fear-and-despair "
            "theses fourteen theses before Th. 30. This force has no independent formation "
            "content of its own once refused: no vendored text shows any Wittenberg-era "
            "formation activity that is indulgence-shaped."
        ),
        manifestations=[
            "\"Such a Saul was I at that time\" (v1 365); \"fell, quite unexpectedly, into this wrangling and contention\" (v1 390-391)",
            "giving to the poor \"a better work than buying pardons\" (Th. 43, v1 1312-1313)",
            "\"No one is sure that his own contrition is sincere\" (Th. 30, v1 1264-1265)",
            "\"when the Pope with his letters and bulls dispensed indulgences\" (LC 3805-3807), remembered only as a defunct practice",
            "\"I did nothing; the Word did it all\" (v2 14931)",
        ],
        sources=[
            src("DT", "v1 1205-1388: the disputation's own theses, contrition, penalty and the treasury of merit"),
            src("PF", "v1 365-397: the 1545 preface's own retrospect"),
            src("LC", "LC 3805-3807: indulgences remembered only as a defunct practice"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the conviction's public form (Doc_08 Cell 1B, Force 1B-1); Contested "
            "for the self-narrative and for any 'breakthrough' dating -- moot for a library that "
            "lacks the tower-experience passage.",
        ),
    ),
    dict(
        cell="1B-2", slug="laitys-need-for-assurance", kind="initiating", matrix_cell="1B",
        name="A laity taught to rely on indulgences, confession and the sacramental system for assurance -- the need the world answered [1B - initiating/internal]",
        description=(
            "LAYER 1 (Historical Event). 'The practical and pastoral problem... of a laity "
            "taught to rely on indulgences, private confession to a priest, and the church's own "
            "sacramental system for assurance of salvation' (Doc_01 §7, Widely Accepted). Coded "
            "Internal rather than External on the ground that the apparatus that taught the "
            "laity so is the inheritance (1B-3) and the parent church (1A-2), while the NEED "
            "itself sat inside the community whose own founder was a friar under vows and whose "
            "own 1529 confession speaks of 'we' who 'went from mere compulsion and fear.' This "
            "could be read as External instead (the Framework's own wording for "
            "External nearly matches Doc_01 §7's heading here); the placement is disclosed, and "
            "nothing in the Forces-and-Gravities Synthesis depends on which side of the line it "
            "sits. LAYER 2 (World's Own Experience). Not remembered as an institution; "
            "remembered as a bodily habit of fear: 'the old way under the Pope, in which a "
            "person tortured himself to be so perfectly pure that God could not find the least "
            "blemish in us... one week trails another, and one half year the other' (LC "
            "4327-4336); 'we always prayed in Popedom conditionaliter, conditionally, and "
            "therefore uncertainly' (TT 3063-3064, Contested as verbatim); 'if you should ask "
            "them whether they are sure that what they do pleases God, they say, \"No\"' (v1 "
            "6845-6856). LAYER 3 (Formation Impact). The most generative force in the matrix: "
            "generated G1 together with 1B-1; generated G4 -- the catechism is what replaces the "
            "indulgence-confession-sacrament system as the laity's formation; generated G5 as a "
            "positive organizing force; generated G11 together with 1A-3, the medium and the "
            "audience. Set the world's affective plot, terror then comfort, and its hope's one "
            "sentence, 'I cannot doubt I have a gracious God.'"
        ),
        manifestations=[
            "\"the old way under the Pope, in which a person tortured himself to be so perfectly pure that God could not find the least blemish in us... one week trails another, and one half year the other\" (LC 4327-4336)",
            "\"we always prayed in Popedom conditionaliter, conditionally, and therefore uncertainly\" (TT 3063-3064, Contested as verbatim)",
            "\"if you should ask them whether they are sure that what they do pleases God, they say, 'No'; they do not know, or they doubt\" (v1 6845-6856)",
            "\"Some persons were driven by conscience into the desert, into monasteries hoping there to merit grace by a monastic life\" (AC 559-561)",
        ],
        sources=[
            src("LC", "LC 4327-4336: the old way remembered as a bodily habit of fear"),
            src("TT", "TT 3063-3064: 'we always prayed... conditionally, and therefore uncertainly'"),
            src("GW", "v1 6845-6856: no assurance without faith"),
            src("AC", "AC 559-561: the desert and the monastery sought for merit"),
        ],
        confidence=conf(
            "Widely Accepted",
            "Widely Accepted (Doc_01's own tag, carried at Doc_08 Cell 1B, Force 1B-2). Placed "
            "Internal on the disclosed argument above; a reviewer may hold External instead, and "
            "nothing in this record's own gravity links depends on which side of the line is "
            "chosen.",
        ),
    ),
    dict(
        cell="1B-3", slug="inheritance-refused", kind="initiating", matrix_cell="1B",
        name="The inheritance refused: the Augustinian seedbed, the seven-sacrament, monastic and penitential apparatus [1B - initiating/internal]",
        description=(
            "LAYER 1 (Historical Event). 'The Augustinian Hermits are its seedbed (Luther's own "
            "order)... their Reformation-lands houses dissolved into this story' (Doc_01 §8.6). "
            "The medieval sacramental system's own seven-sacrament structure and the papacy's "
            "own claimed authority over doctrine are both explicitly and repeatedly refused, not "
            "merely absent but argued against by name -- the reduction from seven sacraments 'to "
            "but three' and then 'but two' (Documented). The Teutonic Order's conversion into a "
            "hereditary duchy and Albert's 1526 marriage (Widely Accepted, editorial). A named "
            "open question is carried, not resolved: whether the vocabulary in which the "
            "inheritance is refused -- vows, 'false chastity,' the Hours, the saints -- is this "
            "world's own or the inheritance's, unanswerable from this library. LAYER 2 (World's "
            "Own Experience). Felt in the body as one's own former vow and cowl: 'wearing a cowl "
            "will not kill him' (v2 15026); pastors 'delivered from the unprofitable and "
            "burdensome babbling of the Seven Canonical Hours' (LC 71-72); the saints kept by "
            "their specialisms -- fire, pestilence -- replaced by the Word as 'the true holy "
            "water and holy sign from which he flees' (LC 130-138). The confession's own list of "
            "what is no longer counted holy: 'particular holy-days, particular fasts, "
            "brotherhoods, pilgrimages, services in honor of saints, the use of rosaries, "
            "monasticism' (AC 501-504). LAYER 3 (Formation Impact). Generated G3 -- the "
            "seven-sacrament, sacrifice-of-the-mass system is exactly the space this force's "
            "refusal fills; generated G7 as the refusal of the clerical estate; generated G9 -- "
            "the founder was a friar, the world's martyrs were monks. Gave G12 its replaced "
            "protections, the saints, and left the world its one martyr narrative, the Brussels "
            "monks stripped of 'monkish garb... True priests of God's own making' (Hy "
            "1789-1800)."
        ),
        manifestations=[
            "the reduction from seven sacraments \"to but three\" and then \"but two\" (v2 6695-6701; v1 2271-2272)",
            "pastors \"delivered from the unprofitable and burdensome babbling of the Seven Canonical Hours\" (LC 71-72)",
            "the saints replaced by the Word as \"the true holy water and holy sign from which he flees\" (LC 130-138)",
            "\"particular holy-days, particular fasts, brotherhoods, pilgrimages, services in honor of saints, the use of rosaries, monasticism, and such like\" (AC 501-504)",
            "the Brussels martyrs, \"Their monkish garb from them they take... True priests of God's own making\" (Hy 1789-1800)",
        ],
        sources=[
            src("BC", "v2 6695-6701; v1 2271-2272: the reduction from seven sacraments"),
            src("LC", "LC 71-72, 130-138, 451-455: the Hours refused; the saints replaced"),
            src("AC", "AC 501-504: the confession's own list of what is no longer counted holy"),
            src("TK", "the Order's secularization, Albert's 1526 marriage, editorial"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the refusals argued by name; Widely Accepted for the seedbed and the "
            "Order's secularization (Doc_08 Cell 1B, Force 1B-3). One open question carried, not "
            "resolved: whether this vocabulary is this world's own or the inheritance's -- "
            "unanswerable from this library.",
        ),
    ),
    dict(
        cell="2A-1", slug="papal-force-ongoing", kind="ongoing", matrix_cell="2A",
        name="The papal force, ongoing: the Confutation, the persecution of married priests, the remembered compulsions, 1522-1531 [2A - ongoing/external]",
        description=(
            "LAYER 1 (Historical Event). After the bull, the force continues in three documented "
            "forms: the Roman CONFUTATION (1530), read before the Emperor and withheld from the "
            "Lutheran party in writing -- 'they were unwilling to exhibit to us a copy of their "
            "Apology' (Ap 8447-8449) -- cited repeatedly as 'the adversaries'; the confession's "
            "own report that 'men, and that, priests, are cruelly put to death... for no other "
            "cause than marriage' (AC 765-766, Documented as to the argument, Widely Accepted as "
            "to the practice it presupposes); and the Easter communion law, the fast, and the "
            "seven hours, remembered as compulsions the world had left. The Roman contemporary "
            "is in the library only as quoted by the answering side -- structural to a "
            "founder-corpus library, disclosed rather than corrected. LAYER 2 (World's Own "
            "Experience). Its name shifts by register: 'the pope... the Antichrist' in the "
            "sermons, 'the old way under the Pope' in the catechism (LC 4327), 'the Church of "
            "Rome as known from its writers' in the confession (AC 631-633). The body remembers "
            "it as a command with a graveyard attached: 'he who does not go [to the sacrament at "
            "Eastertide] shall not be buried in consecrated ground' (v2 15468-15470). The "
            "conscience remembers it as its tormentor -- 'The Pope is a mere tormentor of the "
            "conscience' (TT 3083-3084, Contested as verbatim). LAYER 3 (Formation Impact). Held "
            "and intensified G1, G2, G3, G5 -- the Babylonian Captivity 'written against the "
            "bull's year'; the 'under the bench' form; the pope as 'tormentor of the "
            "conscience'; intensified G9 through the married priests' deaths. Its own REMOVAL "
            "was itself a force the founder reports: 'because the nonsense of the Pope has been "
            "abolished... [they] go one, two, three years, or even longer without the Sacrament' "
            "(LC 4238-4241) -- the world kept the gate and changed what it checks (AC 797)."
        ),
        manifestations=[
            "\"they were unwilling to exhibit to us a copy of their Apology\" (Ap 8447-8449) -- the Confutation withheld in writing",
            "\"men, and that, priests, are cruelly put to death, contrary to the intent of the Canons, for no other cause than marriage\" (AC 765-766)",
            "\"he who does not go [to the sacrament at Eastertide] shall not be buried in consecrated ground\" (v2 15468-15470)",
            "\"The Pope is a mere tormentor of the conscience\" (TT 3083-3084, Contested as verbatim)",
            "\"because the nonsense of the Pope has been abolished... [they] go one, two, three years, or even longer without the Sacrament\" (LC 4238-4241)",
        ],
        sources=[
            src("AP", "Ap 8447-8449: the Confutation withheld in writing, cited as 'the adversaries'"),
            src("RC", "the Roman Confutation (1530) -- reaching this library only as the Apology answers it"),
            src("AC", "AC 765-766, 787-799: married priests defended; the gate kept, what it checks changed"),
            src("ES", "v2 15468-15476: the Easter compulsion, remembered with a graveyard attached"),
        ],
        confidence=conf(
            "Documented",
            "Documented as Melanchthon's own complaint and as to AC's argument (Doc_08 Cell 2A, "
            "Force 2A-1); Widely Accepted as to the practice the marriage defense presupposes. "
            "Every Table Talk saying quoted here is Contested as verbatim, Documented as "
            "Aurifaber's report.",
        ),
    ),
    dict(
        cell="2A-2", slug="imperial-force-ongoing", kind="ongoing", matrix_cell="2A",
        name="The imperial force: Worms and the Edict (1521), the Diets, Augsburg and the confessional register, 1521-31 [2A - ongoing/external]",
        description=(
            "LAYER 1 (Historical Event). The Edict of Worms and the Council of Regency's edict "
            "of January 1522 (Widely Accepted); the Wartburg absence, 4 May 1521 to 6 March "
            "1522; the Diets of Speyer and the appeal to 'a general, free Christian Council' (AC "
            "116-161, Documented); the Diet of Augsburg (1530), the Confession submitted in "
            "German and Latin by nine signatories, the Confutation read before the Emperor "
            "(Documented). Absent input, stated here and at 3A-2: the force's legal settlement "
            "of 1555 lies outside every vendored text. LAYER 2 (World's Own Experience). In "
            "1522 the Edict is felt as the absence that let the reform run ahead: 'I would not "
            "have gone so far as you have done, if I had been here. What you did was good, but "
            "you have gone too fast' (v2 14727-14728). Worms is remembered as a fool's play "
            "declined -- 'I could have started such a little game at Worms that even the emperor "
            "would not have been safe... I did nothing; I left it to the Word' (v2 14932-14935). "
            "In 1530 the force is felt as a summons that sets the world's own agenda beside the "
            "Turk's -- 'measures against the Turk... [and] dissensions in the matter of our holy "
            "religion' (AC 50-54) -- and answered in a new voice, 'our churches' (AC 787). "
            "LAYER 3 (Formation Impact). The force that STATED the gravities: intensified G1 and "
            "G5 into confessional definition at the Diet; shifted G3 from the 1520 logic of "
            "abolition to the 1530 defense of a retained Mass; stated G2 additively; reworded G7 "
            "'calling'; settled G8 as the confessional doctrine of adiaphora; shifted G11 into "
            "the Apology's two-tier rule; shifted G12's naming from 'Antichrist' to 'the Church "
            "of Rome.' As the Edict of 1521, it is the OCCASION of G8's generation. Its "
            "transforming aspect -- the world's form changed from protest literature to settled "
            "confession -- is entered at 3A-1."
        ),
        manifestations=[
            "\"I would not have gone so far as you have done, if I had been here. What you did was good, but you have gone too fast\" (v2 14727-14728)",
            "\"I could have started such a little game at Worms that even the emperor would not have been safe... I did nothing; I left it to the Word\" (v2 14932-14935)",
            "the Diet's own agenda, \"measures against the Turk... [and] dissensions in the matter of our holy religion\" (AC 50-54)",
            "the Confession's own new voice, \"our churches\" (AC 787), \"the Confession of our preachers and of ourselves\" (AC 81-83)",
            "the Mass \"retained among us, and celebrated with the highest reverence\" (AC 787-788)",
        ],
        sources=[
            src("ES", "v2 14727-14728, 14932-14935: the Edict felt as absence; Worms declined as 'a fool's play'"),
            src("AC", "AC 50-58, 81-83, 116-161, 787-799: the Diet's summons, the Confession's own voice, the Mass retained"),
        ],
        confidence=conf(
            "Documented",
            "Documented as to the Diet and the Confession's own documents (Doc_08 Cell 2A, Force "
            "2A-2); Widely Accepted for the Edict and Wartburg dates, editorial. The force's "
            "1555 legal settlement is Not Attested in this library, entered at 3A-2 as an "
            "absent input.",
        ),
    ),
    dict(
        cell="2A-3", slug="territorial-princely-force", kind="ongoing", matrix_cell="2A",
        name="The territorial-princely force, in both directions: protection, ban, the prince's loaf, the inspecting arm [2A - ongoing/external]",
        description=(
            "LAYER 1 (Historical Event). Frederick's protection; Duke George's 1522 ban on the "
            "September Testament and his complaints to the Elector (Widely Accepted); SECULAR "
            "AUTHORITY, dedicated to Duke John and preached before him at Weimar (Documented as "
            "the movement's own doctrine of the state); the Teutonic Order's secularization "
            "(Widely Accepted); the Wittenberg Council's own call (Documented). Absent input: "
            "the force's inspecting arm, the Saxon visitation of 1527-28 and Melanchthon's "
            "INSTRUCTIONS FOR THE VISITORS, is known to this library only by reference -- "
            "documented at the level of the Empire and the Saxon court, undocumented at the "
            "level of the parish. LAYER 2 (World's Own Experience). As the guarantor that a "
            "change is 'from God': abolishing the mass rightly would have required 'the aid of "
            "the authorities' (v2 14764-14765); as the sword ordained of God, 'lawful civil "
            "ordinances are good works of God' (AC 411-428); as the prince who keeps the bread "
            "(LC 3471-3484) -- and, in the same petition, the hunger the same force can cause "
            "when nobles 'let the parishes decay... and pastors and preachers to suffer distress "
            "and hunger a plenty' (LC 92-97). The economic datum sits in this same petition: "
            "'how much trouble there is now in the world only on account of bad coin... and "
            "daily oppression and raising of prices' (LC 3535-3541) -- from within, not a market "
            "but a sin against the neighbour's bread. LAYER 3 (Formation Impact). Re-set G3 "
            "after 1522, by the founder's own appeal to 'the aid of the authorities'; shifted "
            "G4's audience between 1520 and 1529, once the territorial church had parishes to "
            "inspect and pastors to rebuke; both protected and banned G6, shifting its direction "
            "three times; intensified G9 through the Order's secularization and G11 through the "
            "ban on the German Testament; stands behind G13 as the unsourced 'inspecting arm.'"
        ),
        manifestations=[
            "abolishing the mass rightly would have required \"the aid of the authorities\" (v2 14764-14765)",
            "\"lawful civil ordinances are good works of God... Christians are necessarily bound to obey their own magistrates\" (AC 411-428)",
            "the prince as the one by whom God preserves daily bread; nobles who \"let the parishes decay... and pastors and preachers to suffer distress and hunger a plenty\" (LC 92-97, 3471-3484)",
            "\"how much trouble there is now in the world only on account of bad coin... and daily oppression and raising of prices\" (LC 3535-3541)",
            "\"the Gospel hastens to Prussia\" (v3 20802-20803, Luther as quoted by Lambert, editorial)",
        ],
        sources=[
            src("SA", "Secular Authority, dedicated to Duke John, preached before him at Weimar"),
            src("ES", "v2 14764-14779: 'the aid of the authorities'"),
            src("LC", "LC 92-97, 3449-3541: the parishes' decay; the economic datum in the fourth petition"),
            src("TK", "the Teutonic Order's secularization, editorial"),
            src("IV", "Melanchthon's Instructions for the Visitors of Parish Pastors -- the unvendored 'inspecting arm'"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the doctrine and the court-level institutions; Widely Accepted for "
            "the editorially reported events (Doc_08 Cell 2A, Force 2A-3); the visitation itself "
            "is an absent input, known only by reference.",
        ),
    ),
    dict(
        cell="2A-4", slug="popular-insurrectionary-force", kind="ongoing", matrix_cell="2A",
        name="The popular-insurrectionary force: 1521-22 as documented; 1525 by named absence [2A - ongoing/external]",
        description=(
            "LAYER 1 (Historical Event). Documented: AN EARNEST EXHORTATION FOR ALL CHRISTIANS, "
            "WARNING THEM AGAINST INSURRECTION AND REBELLION (Dec. 1521/Jan. 1522), sympathetic "
            "to 'the common man' who 'has been brooding over the injury he has suffered in "
            "property, in body and in soul' before forbidding insurrection; the Karsthans "
            "pamphlet's flail (Widely Accepted as to the pamphlet); the Large Catechism's "
            "unnamed 'murder, and riot of our enemies' quelled by prayer (LC 3190-3196, "
            "Documented as text, event unnamed). ABSENT: AGAINST THE MURDEROUS, THIEVING HORDES "
            "OF PEASANTS (May 1525) and the companion 1525 tracts -- not vendored, characterized "
            "only from a tertiary article, Widely Accepted as to content, no phrase quoted. "
            "Blickle's 'revolution of the common man' is Dominant Modern Reconstruction, and the "
            "1522 Exhortation 'reads very differently against it than the 1525 tract does.' "
            "LAYER 2 (World's Own Experience). In 1522, a bloodshed the Word made unnecessary: "
            "'I could have brought great bloodshed upon Germany... I did nothing; I left it to "
            "the Word' (v2 14932-14935); a wrong with a real cause the Word nonetheless forbids "
            "answering with 'flails and cudgels' (v3 10665-10672). In 1529, remembered as a "
            "tragedy averted by prayer: 'the prayer of a few godly men intervened like a wall of "
            "iron on our side' (LC 3190-3196). The text names no event, and this record supplies "
            "none for 1525: the world's own memory of it in this library is an unnamed 'riot' "
            "answered by prayer, and that is all Layer 2 may say. LAYER 3 (Formation Impact). "
            "Intensified G6 in 1521-22, and its intensification's climax, 1525, is a named "
            "absence whose content this record does not characterize. Gave G8 a second object: "
            "the restraint built for the reform's own haste turned on the peasants' too."
        ),
        manifestations=[
            "\"the common man\" who \"has been brooding over the injury he has suffered in property, in body and in soul\" (v3 10665-10672)",
            "\"I could have brought great bloodshed upon Germany... I did nothing; I left it to the Word\" (v2 14932-14935)",
            "\"the prayer of a few godly men intervened like a wall of iron on our side? They should else have witnessed a far different tragedy\" (LC 3190-3196)",
            "1525's tracts -- absent from this library, characterized only from a tertiary account, no phrase quoted (R94)",
        ],
        sources=[
            src("EX", "the Earnest Exhortation (1521-22): sympathetic to the common man's grievance, insurrection forbidden"),
            src("LC", "LC 3190-3196: the unnamed 'riot' quelled by prayer"),
            src("PW", "a tertiary secondary account of 1525, Widely Accepted as to content, no phrase quoted (R94)"),
        ],
        confidence=conf(
            "Widely Accepted",
            "Documented for the 1521-22 form (the Exhortation, LC 3190-3196); Widely Accepted "
            "for 1525's content from a tertiary source; Dominant Modern Reconstruction for "
            "Blickle's frame (Doc_08 Cell 2A, Force 2A-4). No phrase from any 1525 tract is "
            "quoted anywhere in this record, per R94's bar.",
        ),
    ),
    dict(
        cell="2A-5", slug="the-turk", kind="ongoing", matrix_cell="2A",
        name="The Turk -- brief, per Proportionality [2A - ongoing/external]",
        description=(
            "LAYER 1 (Historical Event). The Diet of Augsburg summoned 'concerning measures "
            "against the Turk, that most atrocious, hereditary, and ancient enemy of the "
            "Christian name and religion' (AC 49-51, Documented as the confession's own "
            "preface); a standing referent from the 1520 treatises to the catechism's own "
            "petition and the Table Talk. No military event touching Saxony is recorded in any "
            "vendored text. LAYER 2 (World's Own Experience). A petition: 'vanquish the Turks "
            "and all enemies' (LC 3504), inside the prayer for rulers; 'I will pray against the "
            "Pope and the Turk as long as I live' (TT 3134-3135); 'heathen, Turks, Jews, or "
            "false Christians' as one list of those outside (LC 2959-2961). LAYER 3 (Formation "
            "Impact). Minimal, and stated so: the Turk left, in the formation literature read, a "
            "standing referent in prayer and no bodily trace -- no flight, no levy, no household "
            "instruction. Folded into G12 as one of its three named adversaries; supplies G6 "
            "with the Diet's own agenda. Reason for brevity: genuine minimal formative trace "
            "(Forces Framework Principle 2's own case), not evidential absence -- the inverse of "
            "2A-6's and 3A-2's thinness, which is the library's, not the impact's."
        ),
        manifestations=[
            "the Diet summoned \"concerning measures against the Turk, that most atrocious, hereditary, and ancient enemy of the Christian name and religion\" (AC 49-51)",
            "\"vanquish the Turks and all enemies\" (LC 3504), inside the prayer for rulers",
            "\"I will pray against the Pope and the Turk as long as I live\" (TT 3134-3135)",
            "\"heathen, Turks, Jews, or false Christians\" (LC 2959-2961)",
        ],
        sources=[
            src("AC", "AC 49-51: the Diet's own agenda naming the Turk"),
            src("LC", "LC 2959-2961, 3504: the Turk inside the catechism's own petitions"),
            src("TT", "TT 3134-3136: 'I will pray against the Pope and the Turk as long as I live'"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the texts (Doc_08 Cell 2A, Force 2A-5). Brief by genuine minimal "
            "formative trace, not by evidential absence -- the Proportionality Principle's own "
            "case, stated so rather than left to read as 'minor.'",
        ),
    ),
    dict(
        cell="2A-6", slug="reformed-rival-by-absence", kind="ongoing", matrix_cell="2A",
        name="The Reformed rival, refused at Marburg (1529) -- a force held by located absence [2A - ongoing/external]",
        description=(
            "LAYER 1 (Historical Event). Doc_01 §7 named the refusal; Doc_02 §13 tested it: "
            "'Zwingli' and 'Marburg' return zero hits in all ten files; 'Oecolampadius' once, in "
            "an editor's footnote; 'Sacramentarians' in Luther's own voice exactly once, in "
            "BONDAGE. The Marburg Articles (3 October 1529), signed by Luther and Melanchthon "
            "among others, are a located, unvendored lead. Finding: the silence is CHRONOLOGICAL "
            "AND GENERIC, not suppressive -- the rival is absent because the vendored texts are "
            "early or confessional, not because anyone removed it (Documented as to the "
            "searches). The world-boundary weight assigned to this force (Doc_01 §8.1's "
            "'diverge sharply and specifically at the Eucharist') rests on the census and "
            "sibling documents and is left UNTAGGED, pending the Marburg Articles' acquisition. "
            "LAYER 2 (World's Own Experience). The library gives the world one clause, one word, "
            "and a generic label for this edge: 'they reject those that teach otherwise' (AC "
            "322-324); 'Sacramentarians, Donatists, Arians, Anabaptists, Epicureans, &c.' among "
            "the tares (Co 16090-16092); the 'new spirits' and 'fanatics' of the sacrament "
            "sections, generic labels, not names. The world's own experience of Marburg is NOT "
            "RECOVERABLE from this library, and nothing Reformed is characterized here. LAYER 3 "
            "(Formation Impact). Intensified G10 under a force the library cannot show, and "
            "fractured it outward by reference to the census and sibling documents, not by any "
            "vendored text; pressed G3 invisibly; touched G5 not at all. Reason for brevity: "
            "evidential absence, the inverse of the Proportionality Principle's own case -- the "
            "acquisition that would change every layer here is the Marburg Articles."
        ),
        manifestations=[
            "\"Zwingli\" and \"Marburg\" return zero hits in all ten vendored files (Doc_02 §13 item 1)",
            "\"they reject those that teach otherwise\" (AC 322-324)",
            "\"Sacramentarians, Donatists, Arians, Anabaptists, Epicureans, &c.\" among the tares (Co 16090-16092, OCR-recovered)",
            "the 'new spirits' and 'fanatics' of the sacrament sections -- \"generic labels, not names\" (Doc_02 §12.5)",
        ],
        sources=[
            src("AC", "AC 322-324: 'they reject those that teach otherwise'"),
            src("BW", "Co 16090-16092: the one in-voice word, 'Sacramentarians'"),
            src("MA", "the Marburg Articles (1529) -- the located, unvendored lead this force's every layer waits on"),
        ],
        confidence=conf(
            "Inferential-Thin",
            "Documented as to the searches themselves (Doc_08 Cell 2A, Force 2A-6); the "
            "organizing role assigned to this force against the Reformed is left UNTAGGED, "
            "resting on the census and sibling documents rather than any rowed secondary "
            "source, pending the Marburg Articles.",
        ),
    ),
    dict(
        cell="2B-1", slug="internal-radical-force", kind="ongoing", matrix_cell="2B",
        name="The internal-radical force: Karlstadt and Zwilling's pace (1522); the \"new spirits,\" \"fanatics\" and Anabaptists (1529-31) [2B - ongoing/internal]",
        description=(
            "LAYER 1 (Historical Event). 1522: during the Wartburg absence, Karlstadt's and "
            "Zwilling's program in Wittenberg -- the mass abolished, both kinds, images, monks "
            "and nuns leaving -- with Karlstadt's own theses quoted by the editor; the founder's "
            "return and the Eight Sermons of 9 March and the seven days following (Documented "
            "for the sermons); the outcome, 'Carlstadt was silenced, the city council made "
            "acknowledgment to Luther... and Wittenberg bowed to law and order' (Widely Accepted "
            "at the editor's word). 1529-31: the Large Catechism's 'enthusiasts,' 'new spirits,' "
            "'fanatics'; the Confession's five condemnations of the Anabaptists by name. This is "
            "'the only force the library shows penetrating a congregation's communal life "
            "directly.' LAYER 2 (World's Own Experience). Received as the devil's game played "
            "through one's own colleagues: 'here we battle not against pope or bishop, but "
            "against the devil... he would make a flank attack' (v2 14752-14756). Felt as "
            "endangered deathbeds, scandalized neighbours, and what 'men say' of Wittenberg -- "
            "'they take the sacrament with the hands and handle the cup, and then they go to "
            "their brandy' (v2 15404-15407). Answered with the world's own rule: 'Take note of "
            "these two things, \"must\" and \"free\"... Now do not make a \"must\" out of what "
            "is \"free\"' (v2 14790-14796). LAYER 3 (Formation Impact). The force that RESHAPED "
            "what already existed -- the only force this build's notations describe with that "
            "verb: G2 reshaped twice (jus verbi without executio; the Word defined as external); "
            "G3 fractured internally and re-set; G7 fenced ('regularly called'); G1 re-fenced; "
            "G6 reshaped (AC XVI); G10 pressed; G5 intensified; G8 GENERATED OUTRIGHT -- the "
            "occasion of every 'must'/'free' sentence."
        ),
        manifestations=[
            "\"here we battle not against pope or bishop, but against the devil, and do you imagine he is asleep?... he would make a flank attack\" (v2 14752-14756)",
            "\"they take the sacrament with the hands and handle the cup, and then they go to their brandy\" (v2 15404-15407)",
            "\"Take note of these two things, 'must' and 'free'... Now do not make a 'must' out of what is 'free'\" (v2 14790-14796)",
            "the Confession's five condemnations of the Anabaptists by name (AC V, IX, XII, XVI, XVII); \"in our Churches no Anabaptists have arisen\" (Ap 4701)",
            "\"Carlstadt was silenced, the city council made acknowledgment to Luther... and Wittenberg bowed to law and order\" (editorial, Widely Accepted)",
        ],
        sources=[
            src("ES", "the Eight Wittenberg Sermons, 9 March 1522 and the seven days following"),
            src("AND", "Karlstadt's own 1521-22 theses, quoted by the editor (context only)"),
            src("LC", "LC 3277, 3841, 3916, 4069, 4095: 'enthusiasts,' 'new spirits,' 'fanatics'"),
            src("AC", "AC V, IX, XII, XVI, XVII: the five condemnations of the Anabaptists by name"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the sermons, the Large Catechism and the Confession's condemnations "
            "(Doc_08 Cell 2B, Force 2B-1); Widely Accepted for the 1522 outcome (editorial) and "
            "Karlstadt's own chronology, independently confirmed.",
        ),
    ),
    dict(
        cell="2B-2", slug="transmission-within-the-worlds-life", kind="ongoing", matrix_cell="2B",
        name="Transmission within the world's life: the founder's own printing, the collectors, and the first selections, 1517-1545 [2B - ongoing/internal]",
        description=(
            "LAYER 1 (Historical Event). Who transmitted, in-window: the Wittenberg and other "
            "printers; the hymnal compilers, Walter (1525), Klug (1535, 1543), Bapst (1545), "
            "each with the founder's own preface; the founder himself as reluctant collector, in "
            "the 1539 preface to the German works and the 1545 preface to the Latin; Lauterbach "
            "and Aurifaber for the Table Talk; Melanchthon's edition of the Latin works "
            "'published immediately after Luther's death.' SURVIVORSHIP FINDING (Documented): "
            "'Which forces threatened the community's literary output? On the evidence in hand, "
            "NONE DID, and that is itself the finding... What shaped survival was SELECTION, not "
            "suppression.' LAYER 2 (World's Own Experience). The world understood its own "
            "transmission as a thing to be distrusted in favour of the Book: the founder wished "
            "his books forgotten 'if only for the reason that I am afraid of the example' (v1 "
            "260-261), hoping 'the Bible would have kept its place in the pulpit' (v1 329-330). "
            "It understood the hymnal as a beginning offered for others to better: 'to make a "
            "good beginning and to encourage others who can do it better' (Hy 909-912) -- and, "
            "by 1543, as property to be marked, 'not our book published at Wittenberg' if "
            "amended without leave (Hy 1093-1094). LAYER 3 (Formation Impact). What in-window "
            "transmission favoured is what this library holds: the founder's argued doctrine, "
            "Wittenberg, 1517-1525. What it did not carry -- because no one in the movement's "
            "own circle made a book of it -- is the parish: the movement DID record the "
            "visitation protocols; this library lacks that record for rights and language "
            "reasons, not because it was never made. The founder's reluctance is itself a "
            "formation datum."
        ),
        manifestations=[
            "the survivorship finding: \"which forces threatened the community's literary output? On the evidence in hand, none did... What shaped survival was selection, not suppression\"",
            "\"I would gladly have seen all my books forgotten and destroyed... if only for the reason that I am afraid of the example\" (v1 260-261)",
            "\"to make a good beginning and to encourage others who can do it better, I have myself, with some others, put together a few hymns\" (Hy 909-912)",
            "\"when it is amended without our knowledge, it be fully understood to be not our book published at Wittenberg\" (Hy 1093-1094)",
            "Aurifaber's dedication: gathering \"fragments that fell from Luther's Table\" (TT 156-157)",
        ],
        sources=[
            src("PF", "v1 260-330: the founder's own reluctance to be collected, 1539 and 1545"),
            src("HYP", "the hymnal prefaces, 1525-1545: Walter, Klug, Bapst, under the founder's own hand"),
            src("TT", "TT 108-157: Lauterbach's notes, Aurifaber's collection and dedication"),
            src("FO", "Melanchthon's funeral oration and edition of the Latin works, 1546"),
        ],
        confidence=conf(
            "Documented",
            "Documented as to the survivorship finding and the editions' own prefaces (Doc_08 "
            "Cell 2B, Force 2B-2, the required Transmission entry for this cell).",
        ),
    ),
    dict(
        cell="2B-3", slug="parishes-state-as-reported", kind="ongoing", matrix_cell="2B",
        name="The parishes' state as the founder reported it -- the internal force G13 documents [2B - ongoing/internal]",
        description=(
            "LAYER 1 (Historical Event). ABSENT AT LAYER 1, and entered as such: this is Layer 2 "
            "of a force Doc_02 §13 could not document at Layer 1 -- the parish's actual state, "
            "the territorial force's own inspecting arm, the visitation protocols of 1527-28 and "
            "the Small Catechism's own 1529 preface, none of it vendored. A scholarly tension is "
            "carried at full strength: Strauss (1978) read the visitation records as evidence "
            "that catechetical indoctrination largely failed; Scribner, Kittelson and Karant-Nunn "
            "argued the records measure a different thing -- Contested, and nothing in this "
            "library can adjudicate. BAR CARRIED: no downstream record may cite this force, or "
            "G13, as evidence that Saxon congregations were ignorant, cold, or negligent. LAYER "
            "2 (World's Own Experience). This is the layer the library holds in full, in the "
            "founder's voice across two decades, entered as his testimony only: 1522, one "
            "congregation, 'an ass can almost intone the lessons... God does not want hearers "
            "and repeaters of words, but doers and followers' (v2 14676-14688); 1529, the "
            "parishes, 'we see to our sorrow that many pastors and preachers are very negligent' "
            "(LC 51-52); Katharina von Bora's one question about coldness in prayer (TT "
            "3147-3150, Contested as verbatim). The world's own name for this failure is "
            "coldness, and its own name for the force behind it is the devil. LAYER 3 (Formation "
            "Impact). Generated G4's pastor-facing form; reversed G8 -- by 1529 the danger is "
            "'carnal liberty,' not haste; reshaped G11 at its late edge. Its object shifts three "
            "times, and the founder's response shifts with it: rebuke, then program, then "
            "print-control."
        ),
        manifestations=[
            "\"an ass can almost intone the lessons, and why should you not be able to repeat the doctrines and formulas?... God does not want hearers and repeaters of words, but doers and followers\" (v2 14676-14688)",
            "\"we see to our sorrow that many pastors and preachers are very negligent in this, and slight both their office and this teaching\" (LC 51-52)",
            "\"the common people regard the Gospel altogether too lightly, and we accomplish nothing extraordinary even though we use all diligence\" (LC 80-82)",
            "Katharina von Bora: \"Sir! how is it, that in Popedom they pray so often with great vehemence, but we are very cold and careless in praying?\" (TT 3147-3150, Contested as verbatim)",
        ],
        sources=[
            src("SV", "the Saxon visitation protocols (1527-28) -- unvendored, the Layer 1 this force lacks"),
            src("IV", "Melanchthon's Instructions for the Visitors -- unvendored"),
            src("ES", "v2 14676-14688: the 1522 rebuke, one congregation"),
            src("LC", "LC 51-97: the 1529 preface's rebuke of pastors, people and nobles"),
            src("TT", "TT 3147-3150: Katharina von Bora's one question and its answer"),
        ],
        confidence=conf(
            "Contested",
            "Layer 1 ABSENT (Doc_08 Cell 2B, Force 2B-3): the visitation records and the Small "
            "Catechism's 1529 preface are both unvendored. Contested at the scholarly level "
            "whether the surviving record-type even measures what it is read to measure "
            "(Strauss vs. Scribner/Kittelson/Karant-Nunn), unresolved in this library. Documented "
            "only as the founder's own testimony. No downstream record may cite this force as "
            "evidence that any Saxon congregation was in fact ignorant, cold, or negligent.",
        ),
    ),
    dict(
        cell="2B-4", slug="print-turned-inward", kind="ongoing", matrix_cell="2B",
        name="Print turned inward: the book that makes pastors unnecessary; the hymns \"sold under our name,\" 1529-1543 [2B - ongoing/internal]",
        description=(
            "LAYER 1 (Historical Event). The founder's 1543 preface to Klug's hymnal, "
            "complaining that 'the earliest of our hymns are more perverted the more they are "
            "printed' (Hy 1065-1069, Documented) and requiring names attached and a printed "
            "warning quatrain; the Large Catechism's report of nobles who say 'we have "
            "everything in books, and every one can easily learn it by himself' (LC 94-95, "
            "Documented as the founder's testimony). Placed as a separate, internal entry "
            "because by 1529 the pressure comes from the world's own printed output and its own "
            "imitators, not from the press as such (1A-3). LAYER 2 (World's Own Experience). The "
            "medium is felt as an excuse -- 'we have everything in books' (LC 94-95) -- and as a "
            "book 'which they can read through at one time, and then immediately know it, throw "
            "the book into a corner' (LC 87-89). The song is felt as corrupted by 'perpetual "
            "amending by every one indiscriminately according to his own liking' (Hy 1065-1067), "
            "and guarded: 'lest strange and unsuitable songs come to be sold under our name' (Hy "
            "1086-1087); 'False masters now abound, who songs indite; / Beware of them, and "
            "learn to judge them right' (Hy 1249-1250). LAYER 3 (Formation Impact). Turned "
            "against G11 at its edge -- by 1543 the vernacular hymns are 'perverted the more "
            "they are printed' and must be fenced -- and is G13's late object, forcing on the "
            "world a boundary of authorship, 'our book / not our book.' The community's own "
            "medium is also the community's own boundary problem."
        ),
        manifestations=[
            "\"the earliest of our hymns are more perverted the more they are printed\" (Hy 1065-1069)",
            "\"we have everything in books, and every one can easily learn it by himself\" (LC 94-95)",
            "a book \"which they can read through at one time, and then immediately know it, throw the book into a corner\" (LC 87-89)",
            "\"lest strange and unsuitable songs come to be sold under our name\" (Hy 1086-1087)",
            "\"False masters now abound, who songs indite; / Beware of them, and learn to judge them right\" (Hy 1249-1250)",
        ],
        sources=[
            src("HYP", "the 1543 preface to Klug's hymnal: names required, the warning quatrain"),
            src("LC", "LC 87-97: the book thrown into a corner; the excuse, 'we have everything in books'"),
        ],
        confidence=conf(
            "Documented",
            "Documented (Doc_08 Cell 2B, Force 2B-4) -- the founder's own 1543 preface and the "
            "Large Catechism's own report, both read directly at the loci given.",
        ),
    ),
    dict(
        cell="3A-1", slug="confessional-territorial-transformation", kind="ending", matrix_cell="3A",
        name="The confessional-territorial transformation: from protest literature to settled confession under princes' signatures, 1530-31 [3A - ending-transforming/external]",
        description=(
            "LAYER 1 (Historical Event). 'A movement that argued its case in occasional "
            "treatises in 1517-1520 had, by 1530, produced a single formal confession subscribed "
            "by named princes... a real change in institutional register, from protest "
            "literature to settled confession' (Doc_01 §2.3, Documented as to the documents' "
            "dates and contents; the sharpness of the change is Inferential-Thin). The "
            "transformation is gradual, 1522 to 1529 to 1530, not a sudden overwhelm; the "
            "world's form after it is a successor form of itself, not a different community. "
            "What is NOT claimed: that this transformation ended anything, or that it was "
            "complete by 1545, or anything about 1555 (entered separately at 3A-2). LAYER 2 "
            "(World's Own Experience). The world did not narrate its own change of form; this "
            "layer is confined to the voice-change the texts themselves show. A professor's "
            "voice to named readers and 'the German estates' in 1520; a preacher's to 'dear "
            "friends' in 1522; a father's to his household, 'The Simple Way a Father Should "
            "Present Them to His Household,' in 1529; and in 1530, 'the undersigned Elector and "
            "Princes' before 'Imperial Majesty,' submitting 'the Confession of our preachers and "
            "of ourselves,' speaking of 'our churches' and a Mass 'retained among us.' The "
            "polemical register's 'Antichrist' becomes the confessional register's 'the Church "
            "of Rome.' LAYER 3 (Formation Impact). The gravities are STATED, not changed, but "
            "the ecology's authority structure and boundary are transformed: the 'fencing' of "
            "1522-31 becomes the criterion of legitimacy, and the world's public voice, when it "
            "matters most, is princes'. What was transmitted past the window by this form is the "
            "confessional pair and the two catechisms, entering the Book of Concord in 1580 by "
            "reference."
        ),
        manifestations=[
            "\"a movement that argued its case in occasional treatises in 1517-1520 had, by 1530, produced a single formal confession subscribed by named princes\" (Doc_01 §2.3)",
            "1520: a professor's voice to \"the German estates\"; 1522: a preacher's, \"dear friends\" (v2 14676); 1529: a father's, \"The Simple Way a Father Should Present Them to His Household\" (SC 45)",
            "1530: \"the undersigned Elector and Princes\" (AC 66) before Imperial Majesty, speaking of \"our churches\" (AC 787) and a Mass \"retained among us\" (AC 787-788)",
            "the polemical register's \"Antichrist\" becoming the confessional register's \"the Church of Rome\" (AC 631-633)",
        ],
        sources=[
            src("CN", "the 1520 treatise's own address to 'the German estates'"),
            src("ES", "v2 14676: the 1522 preacher's own 'dear friends'"),
            src("SC", "SC 45: 'The Simple Way a Father Should Present Them to His Household' (1529)"),
            src("AC", "AC 66, 631-633, 787-788: the 1530 confessing voice, 'our churches,' the naming shift"),
            src("BOC", "the Book of Concord (1580): where the confessional pair and the catechisms are carried by reference"),
        ],
        confidence=conf(
            "Documented",
            "Documented as to the documents' dates and contents (Doc_08 Cell 3A, Force 3A-1); "
            "Inferential-Thin as to any parish's own experience of the change, and as to the "
            "sharpness of the transformation itself (Doc_01 §2.3's own tag). An alternative "
            "disposition is disclosed: a reviewer may fold this entry into 2A-2/2A-3 as an "
            "ongoing-external effect rather than a transformation; the gravity connections below "
            "do not change under either reading.",
        ),
    ),
    dict(
        cell="3A-2", slug="absent-inputs-1525-and-1555", kind="ending", matrix_cell="3A",
        name="1525 and 1555: the two external events at which this world's boundaries were decided, outside every vendored text -- absent inputs, Layer 1 only [3A - ending-transforming/external]",
        description=(
            "LAYER 1 (Historical Event) -- and Layer 1 only; Layers 2 and 3 are NOT RECOVERABLE "
            "from this library and are not supplied. 1525: the Peasants' War and the three 1525 "
            "tracts, characterized only at a tertiary remove -- the charge of three sins, the "
            "call on the princes to put the rebels down by force, the tract 'appearing as the "
            "princes' armies were already winning' -- Widely Accepted as to content and timing, "
            "Dominant Modern Reconstruction for Blickle's frame, NOT DOCUMENTED, no phrase "
            "quoted (R94). 1555: the Peace of Augsburg, named at Doc_01 §2.2 as 'a real marker "
            "of a different kind -- political-legal rather than doctrinal-confessional'; nothing "
            "in this library attests it at any confidence, and this record assigns it none. Why "
            "Layer 1 only, and why this is NOT the Proportionality Principle's minimal-impact "
            "case: both events are absent from the library, not minimal in impact -- they are "
            "this world's 'two most consequential moments.' 1525 is entered here, though it sits "
            "inside the evidential window chronologically (it is a climax of Force 2A-4), "
            "because it is the external event most plausibly transformative of G6; 1555 is "
            "entered as the point at which the transformation Force 3A-1 records was "
            "historically settled, on Doc_01 §2.2's authority alone. LAYER 2. Not recoverable; "
            "see Force 2A-4's Layer 2 for the unnamed 'riot' of LC 3190-3196, which is all the "
            "library carries. LAYER 3. Not supplied. What CAN be said is what the absence does "
            "to the reconstruction: G6's Persistence test cannot be completed from this library; "
            "the world's boundary against the peasants is carried by the Facilitator apparatus "
            "as disclosure, never as Representative content."
        ),
        manifestations=[
            "the 1525 tracts, characterized only at a tertiary remove, no phrase quoted anywhere in this build (R94)",
            "\"a real marker of a different kind -- political-legal rather than doctrinal-confessional\" (Doc_01 §2.2, on 1555)",
            "the unnamed \"riot\" of LC 3190-3196 -- all the library carries of 1525's Layer 2",
            "G6's own forces notation: \"its legal settlement under [F-imp] (1555) lies outside every vendored text\" (Doc_04 §3 G6)",
        ],
        sources=[
            src("PW", "a tertiary secondary account of the Peasants' War, Widely Accepted as to content, no phrase quoted (R94)"),
            src("LC", "LC 3190-3196: the only Layer-2 trace this library carries of 1525, unnamed"),
        ],
        confidence=conf(
            "Contested",
            "Widely Accepted / Dominant Modern Reconstruction for 1525's content and frame "
            "(tertiary, not Documented, R94's bar observed throughout); Not Attested in this "
            "library at any confidence for 1555 (Doc_08 Cell 3A, Force 3A-2). Layer 1 only by "
            "design -- Layers 2 and 3 are not recoverable and are not supplied.",
        ),
    ),
    dict(
        cell="3B-1", slug="internal-fracture-fenced", kind="ending", matrix_cell="3B",
        name="The internal fracture fenced: one documented exit, and the world's own claim that the sects arose elsewhere, 1522-1531 [3B - ending-transforming/internal]",
        description=(
            "LAYER 1 (Historical Event). The library attests the BEGINNING of a fracture -- the "
            "1522 crisis -- and its being fenced rather than consummated: Karlstadt silenced "
            "(Widely Accepted, editorial), then out of Saxony by 1524 and in Switzerland from "
            "1529, 'which takes him outside the world rather than constituting a second pattern "
            "within it.' The world's own confessional testimony that the fracture was not "
            "internal: 'in our Churches no Anabaptists have arisen' (Ap 4701, Documented as "
            "Melanchthon's claim); the Confession's five condemnations by name. No successor "
            "community is generated FROM WITHIN this world in any vendored text; the 1522 "
            "episode is 'a transition event, not a strand' (Doc_01 §6, re-tested and confirmed "
            "at Doc_04 §4). LAYER 2 (World's Own Experience). The fracture's edge named as "
            "brothers not yet won and as sects wearing a borrowed name: 'there are also brothers "
            "and sisters on the other side who belong to us, and must still be won' (v2 "
            "14728-14729); 'sects and false teachers, who all wear the holy name as a cover and "
            "sham for their doctrines of devils' (LC 3272-3273). The fence in its own words: "
            "'no one should publicly teach in the Church or administer the Sacraments unless he "
            "be regularly called' (AC 383-384). The world's own reading of why it did not split: "
            "'He played a bold game, and won, although it does no harm to the Word of God' (v2 "
            "15214-15215) -- the fracture read as the devil's game, lost to the Word. LAYER 3 "
            "(Formation Impact). The shape of the world's own edge left at the window: a "
            "criterion of legitimacy -- 'regularly called,' the 'external Word' -- drawn 'at the "
            "conscience, not at the territory.'"
        ),
        manifestations=[
            "\"in our Churches no Anabaptists have arisen\" (Ap 4701)",
            "\"there are also brothers and sisters on the other side who belong to us, and must still be won\" (v2 14728-14729)",
            "\"sects and false teachers, who all wear the holy name as a cover and sham for their doctrines of devils\" (LC 3272-3273)",
            "\"no one should publicly teach in the Church or administer the Sacraments unless he be regularly called\" (AC 383-384)",
            "\"He played a bold game, and won, although it does no harm to the Word of God\" (v2 15214-15215)",
        ],
        sources=[
            src("ES", "v2 14728-14729, 15214-15215: brothers not yet won; the devil's game lost"),
            src("LC", "LC 3272-3273: sects wearing 'the holy name as a cover and sham'"),
            src("AC", "AC 383-384: 'regularly called' -- the fence in its own words"),
            src("AP", "Ap 4701: 'in our Churches no Anabaptists have arisen'"),
        ],
        confidence=conf(
            "Documented",
            "Documented for the Confession, the Apology, and the Large Catechism's own language "
            "(Doc_08 Cell 3B, Force 3B-1); Widely Accepted for Karlstadt's own exit and "
            "chronology, editorial and independently confirmed.",
        ),
    ),
    dict(
        cell="3B-2", slug="transmission-at-the-windows-edge", kind="ending", matrix_cell="3B",
        name="Transmission at the window's edge and past it: the founder's anticipated absence, the closing of the evidential window as a selection effect, and the editorial lineages that made this library [3B - ending-transforming/internal]",
        description=(
            "LAYER 1 (Historical Event). In-window, the world's own acts: the 1539 preface ('I "
            "would gladly have seen all my books forgotten and destroyed') and the 1545 "
            "preface's own retrospect ('Such a Saul was I'); the 1543 hymnal's authorship fence; "
            "Spangenberg's 1545 preface to the CITHARA LUTHERI, an in-window, non-founder, "
            "laudatory and partisan assessment of the hymns' reception. At the edge: "
            "Melanchthon's edition of the Latin works 'immediately after Luther's death'; his "
            "funeral oration. THE WINDOW'S CLOSING IS ITSELF A SELECTION EFFECT: the library "
            "ends at 1545 because it is a founder corpus and the founder's last prefaces are "
            "dated 1545. Past the window, the transmitting lineages, named, with their stated "
            "interests: the Philadelphia Edition committee, working toward 'the approaching "
            "jubilee of the Reformation in 1917,' selecting treatises 'of most permanent value' "
            "and excluding ON MONASTIC VOWS 'because of its size'; Bente and Dau's CONCORDIA "
            "TRIGLOTTA (1921), the Missouri Synod's confessional edition; Robert E. Smith's "
            "Project Wittenberg Small Catechism, released to the public domain WITHOUT the 1529 "
            "preface; Henry Cole's 1823 BONDAGE, urged by a Reformed-Anglican patron. LAYER 2 "
            "(World's Own Experience). That its books should not outlive the Book: 'I would "
            "gladly have seen all my books forgotten and destroyed... comforted with the thought "
            "that my books will yet be forgotten in the dust' (v1 260-300). What the successor "
            "communities understood themselves to be preserving after 1545 is outside the window "
            "and not characterized. LAYER 3 (Formation Impact). What can and cannot be "
            "reconstructed because of how transmission worked: the founder's argued doctrine "
            "survives abundantly; the parish, the women, the 1525/1543 boundaries, the Marburg "
            "boundary, and the service orders are absent 'for the same modern reason -- a "
            "twentieth-century translation economy and a twenty-first-century hosting problem, "
            "not sixteenth-century suppression.'"
        ),
        manifestations=[
            "\"I would gladly have seen all my books forgotten and destroyed... comforted with the thought that my books will yet be forgotten in the dust\" (v1 260-300)",
            "\"Such a Saul was I at that time\" (v1 365, the 1545 preface's own retrospect)",
            "the Philadelphia editors, selecting treatises \"of most permanent value\" toward \"the approaching jubilee of the Reformation in 1917\" (v1 132-175)",
            "On Monastic Vows \"excluded from this volume because of its size\" (v3 20823-20824)",
            "Project Wittenberg's Small Catechism, released to the public domain without its own 1529 preface",
        ],
        sources=[
            src("PF", "v1 260-397: the 1539 and 1545 prefaces, the founder's own retrospect and reluctance"),
            src("HYP", "the 1543 hymnal's authorship fence; the Cithara Lutheri preface, editorial"),
            src("FO", "Melanchthon's funeral oration and edition, at the window's edge"),
            src("BT", "Bente and Dau's Concordia Triglotta (1921), the Missouri Synod's confessional edition"),
            src("PWR", "Robert E. Smith's Project Wittenberg release notes -- the Small Catechism without its 1529 preface"),
        ],
        confidence=conf(
            "Documented",
            "Documented as to every edition's own stated method (Doc_08 Cell 3B, Force 3B-2, the "
            "required Transmission-in-ending entry); Widely Accepted as to the effect on "
            "Bondage's English emphasis; Inferential-Thin for Bell's own suppression story alone, "
            "which is Excluded elsewhere in this build's Source Registry and not relied on here.",
        ),
    ),
]

FORCE_BY_CELL = {f["cell"]: f for f in FORCES}
assert len(GRAVITIES) == 13, f"expected 13 gravities, found {len(GRAVITIES)}"
assert len(FORCES) == 20, f"expected 20 forces, found {len(FORCES)}"

# ---------------------------------------------------------------------------
# Doc_08 §4's fourteen named Cross-Cell Connections, transcribed as directed
# edges (from_cell, to_cell, kind). kind="causal" -> precondition-for/
# enabled-by (every connection Doc_08 §4 states with a causal/productive/
# triggering/reactive/culminating/refusal-response/same-force-two-phases
# verb); kind="mutual"/"conflated" -> associated-with (Doc_08's own two
# non-directional connections, C8 "⇄" and C11 "~"). MECHANICAL transcription
# of Doc_08 §4's own map; not re-derived.
# ---------------------------------------------------------------------------
CROSS_CELL_EDGES = [
    ("1A-2", "2A-3", "causal"),   # C1
    ("1A-1", "2A-3", "causal"),   # C1
    ("1B-2", "2B-3", "causal"),   # C2
    ("1B-1", "2B-3", "causal"),   # C2
    ("2A-2", "2B-1", "causal"),   # C3
    ("2B-1", "2A-3", "causal"),   # C4
    ("2A-1", "2B-3", "causal"),   # C5
    ("1A-3", "2B-4", "causal"),   # C6
    ("2B-1", "2A-2", "causal"),   # C7
    ("2B-1", "2A-4", "mutual"),   # C8
    ("2A-2", "3A-1", "causal"),   # C9
    ("2A-3", "3A-1", "causal"),   # C9
    ("1B-3", "2A-1", "causal"),   # C10
    ("2A-6", "2B-1", "conflated"),  # C11
    ("2B-1", "3B-1", "causal"),   # C12
    ("2B-2", "3B-2", "causal"),   # C13
    ("1A-2", "2A-1", "causal"),   # C14
]

# ---------------------------------------------------------------------------
# Doc_04 §5's 13x13 gravity x gravity Interaction Matrix, transcribed as the
# upper triangle only (78 pairs; 7 are "-", no demonstrated relationship,
# and are NOT converted into a relation here, matching Gallic's own explicit
# practice at the close of gallic.gravity.grace-and-effort.md: "Neither
# absence is converted into a relation here"). Every non-"-" pair becomes an
# associated-with relation on BOTH gravity records regardless of its R/S/C
# code -- Gallic's own rule ("all seven carried as associated-with, R/S
# character preserved here" -- the code is prose, not the relation type).
# MECHANICAL transcription of Doc_04 §5's own table; not re-derived.
# ---------------------------------------------------------------------------
INTERACTION_MATRIX = [
    ("G1", "G2", "R"), ("G1", "G3", "R"), ("G1", "G4", "R"), ("G1", "G5", "R"),
    ("G1", "G6", "S"), ("G1", "G7", "S"), ("G1", "G8", "R"), ("G1", "G9", "R"),
    ("G1", "G10", "R(t)"), ("G1", "G11", "R(t)"), ("G1", "G12", "R"), ("G1", "G13", "C"),
    ("G2", "G3", "R"), ("G2", "G4", "R"), ("G2", "G5", "R"), ("G2", "G6", "S"),
    ("G2", "G7", "R"), ("G2", "G8", "C"), ("G2", "G9", "R"), ("G2", "G10", "S"),
    ("G2", "G11", "R"), ("G2", "G12", "R"), ("G2", "G13", "C"),
    ("G3", "G4", "R"), ("G3", "G5", "R"), ("G3", "G6", "S"), ("G3", "G7", "S"),
    ("G3", "G8", "C"), ("G3", "G9", "R(t)"), ("G3", "G10", "R"), ("G3", "G11", "R"),
    ("G3", "G12", "R"), ("G3", "G13", "C"),
    ("G4", "G5", "R"), ("G4", "G6", "R"), ("G4", "G7", "R"), ("G4", "G8", "S"),
    ("G4", "G9", "R"), ("G4", "G10", "R(t)"), ("G4", "G11", "R"), ("G4", "G12", "R"),
    ("G4", "G13", "C"),
    ("G5", "G6", "S"), ("G5", "G7", "R(t)"), ("G5", "G8", "R"), ("G5", "G9", "R"),
    ("G5", "G11", "R(t)"), ("G5", "G12", "R"), ("G5", "G13", "C"),
    ("G6", "G7", "R"), ("G6", "G8", "S"), ("G6", "G9", "R"), ("G6", "G11", "R(t)"),
    ("G6", "G12", "R"), ("G6", "G13", "R(t)"),
    ("G7", "G8", "R"), ("G7", "G9", "R"), ("G7", "G11", "R(t)"), ("G7", "G12", "R(t)"),
    ("G7", "G13", "C"),
    ("G8", "G9", "R"), ("G8", "G10", "C(t)"), ("G8", "G11", "R(t)"), ("G8", "G12", "S"),
    ("G8", "G13", "S"),
    ("G9", "G12", "R(t)"),
    ("G10", "G11", "R(t)"), ("G10", "G12", "R(t)"),
    ("G11", "G12", "R(t)"), ("G11", "G13", "S"),
    ("G12", "G13", "R"),
]
# G5-G10, G6-G10, G7-G10, G9-G10, G9-G11, G9-G13, G10-G13 are all "-" and are
# deliberately absent from the table above (7 pairs of 78; matches Doc_04 §5:
# "G9's three '-' cells", "G10... five '-' cells").

# ---------------------------------------------------------------------------
# The 18 "parked for B-5" story/figure records and which gravities each
# names -- AUTHORED (one read pass over all 18 files' own parked paragraphs,
# transcribed here exactly as each file's own text states, per the task's
# own instruction). Values are lists of gravity numbers; the relation type
# on the STORY/FIGURE side is "associated-with" by default, except the one
# founding-act story whose own parked note offers "associated-with (or
# illustrates)" and is resolved here to "illustrates" -- the founding-moment
# story for G1, on Gallic's own precedent (illustrated-by used for exactly
# one story per gravity, the one that stages the gravity "at the moment...
# the tradition's own text says it began").
# ---------------------------------------------------------------------------
STORY_GRAVITIES: dict[str, list[str]] = {
    "augsburg-before-cajetan": ["G2"],
    "brussels-martyrs": ["G1", "G7"],
    "composing-the-magnificat": ["G4", "G9"],
    "diet-of-augsburg-1530": ["G1", "G6"],
    "first-german-mass-sung": ["G11"],
    "household-and-kate-on-prayer": ["G4", "G8"],
    "household-catechism-lesson-typical-practice": ["G4", "G8"],
    "letter-to-albrecht-and-theses-circulation": ["G1"],
    "prayer-for-rain-1532": ["G8", "G13"],
    "return-and-the-eight-sermons": ["G2", "G3", "G7"],
    "speratus-hymn-under-the-window": ["G11"],
    "worms-1521": ["G2", "G6"],
}
STORY_RELATION_OVERRIDE = {"letter-to-albrecht-and-theses-circulation": "illustrates"}

FIGURE_GRAVITIES: dict[str, list[str]] = {
    "brussels-martyrs-john-and-henry": ["G1", "G7"],
    "johann-walter": ["G11"],
    "katharina-von-bora": ["G4", "G8"],
    "luther": ["G1", "G2", "G3", "G4", "G6", "G7", "G8", "G9", "G11", "G13"],
    "melanchthon": ["G1", "G6"],
    "speratus": ["G11"],
}

assert len(STORY_GRAVITIES) == 12, f"expected 12 parked stories, found {len(STORY_GRAVITIES)}"
assert len(FIGURE_GRAVITIES) == 6, f"expected 6 parked figures, found {len(FIGURE_GRAVITIES)}"


# ---------------------------------------------------------------------------
# ID helpers
# ---------------------------------------------------------------------------
def gravity_id(num: str) -> str:
    return f"witt.gravity.{GRAVITY_BY_NUM[num]['slug']}"


def force_id(cell: str) -> str:
    return f"witt.force.{FORCE_BY_CELL[cell]['slug']}"


# ---------------------------------------------------------------------------
# Relations -- MECHANICAL, derived from GRAVITIES[].forces, CROSS_CELL_EDGES
# and INTERACTION_MATRIX alone (single source of truth for each edge; no
# separate force-side data to fall out of sync with the gravity side, the
# exact bug this script's own module docstring records catching and fixing
# during authoring).
# ---------------------------------------------------------------------------
def build_gravity_relations(g: dict) -> list[dict]:
    rels = []
    for cell, tag in g["forces"]:
        rtype = "enabled-by" if tag == "generated" else "associated-with"
        rels.append({"type": rtype, "target": force_id(cell)})
    for a, b, code in INTERACTION_MATRIX:
        if a == g["num"]:
            other = b
        elif b == g["num"]:
            other = a
        else:
            continue
        rels.append({"type": "associated-with", "target": gravity_id(other)})
    return rels


def build_force_relations(f: dict) -> list[dict]:
    rels = []
    for a, b, kind in CROSS_CELL_EDGES:
        rtype_causal_out, rtype_causal_in = "precondition-for", "enabled-by"
        if a == f["cell"]:
            other = b
            rels.append({
                "type": rtype_causal_out if kind == "causal" else "associated-with",
                "target": force_id(other),
            })
        elif b == f["cell"]:
            other = a
            rels.append({
                "type": rtype_causal_in if kind == "causal" else "associated-with",
                "target": force_id(other),
            })
    for g in GRAVITIES:
        for cell, tag in g["forces"]:
            if cell == f["cell"]:
                rtype = "precondition-for" if tag == "generated" else "associated-with"
                rels.append({"type": rtype, "target": gravity_id(g["num"])})
    return rels


def close_reciprocity(records: dict[str, dict]) -> None:
    """MECHANICAL, structural safety net only -- every relation this script
    itself authors on both sides (gravity<->force, force<->force, gravity<->
    gravity) is already symmetric by construction (build_gravity_relations
    and build_force_relations are two views of the same GRAVITIES[].forces/
    CROSS_CELL_EDGES/INTERACTION_MATRIX data). This pass exists for the one
    case that is NOT authored on both sides by construction: the 18 closed
    story/figure -> gravity edges, added to the story/figure record directly
    and requiring their reciprocal added here to the gravity record. Mutates
    `records` in place. No content judgment -- RELATION_INVERSE only."""
    for rid, rec in list(records.items()):
        for rel in list(rec.get("relations") or []):
            target = rel.get("target")
            inv_type = RELATION_INVERSE.get(rel.get("type"))
            if inv_type is None or target not in records:
                continue
            target_rec = records[target]
            already = any(
                r.get("type") == inv_type and r.get("target") == rid
                for r in (target_rec.get("relations") or [])
            )
            if not already:
                target_rec.setdefault("relations", []).append({"type": inv_type, "target": rid})


def build_gravity_body(g: dict) -> str:
    partners = [
        (b if a == g["num"] else a, code)
        for a, b, code in INTERACTION_MATRIX
        if a == g["num"] or b == g["num"]
    ]
    partner_str = ", ".join(f"{p} ({code})" for p, code in sorted(partners, key=lambda x: int(x[0][1:])))
    all_g = {gg["num"] for gg in GRAVITIES if gg["num"] != g["num"]}
    touched = {p for p, _ in partners}
    absent = sorted(all_g - touched, key=lambda x: int(x[1:]))
    absent_str = ", ".join(absent) if absent else "none -- every other candidate shows a demonstrated relationship"
    forces_str = ", ".join(
        f"{force_id(cell)} ({'enabled-by' if tag == 'generated' else 'associated-with'})"
        for cell, tag in g["forces"]
    )
    return (
        f"Re-derived from the approved Doc_04 (§2.1 candidate {g['num']} -> §3 {g['num']} -> "
        f"§7 row {g['num']}; {g['classification'].upper()}). Interaction Matrix (Doc_04 §5, "
        f"row/col {g['num']}): {partner_str} -- all carried as associated-with here, R/S/C "
        f"character preserved in this record's own description field above, per Gallic's own "
        f"precedent (relation TYPE is not overloaded to carry the R/S/C code). DECLARED "
        f"ABSENCES, not converted into a relation here: {absent_str}. Forces-connection "
        f"(Doc_08 §5): {forces_str} -- enabled-by used exactly where Doc_04's own notation "
        f"uses the verb 'generated' for this force/gravity pair, associated-with for every "
        f"other verb (held, intensified, shifted, reshaped, fenced, fractured, re-set, "
        f"reversed, settled, pressed, corrupted), matching Gallic's own precedent exactly."
    )


def build_force_body(f: dict) -> str:
    out_edges = [(b, kind) for a, b, kind in CROSS_CELL_EDGES if a == f["cell"]]
    in_edges = [(a, kind) for a, b, kind in CROSS_CELL_EDGES if b == f["cell"]]
    parts = []
    if out_edges:
        parts.append(", ".join(
            f"{force_id(c)} ({'precondition-for' if k == 'causal' else 'associated-with'})"
            for c, k in out_edges
        ))
    if in_edges:
        parts.append(", ".join(
            f"{force_id(c)} ({'enabled-by' if k == 'causal' else 'associated-with'})"
            for c, k in in_edges
        ))
    cross_str = "; ".join(parts) if parts else "none named in Doc_08 §4 for this cell"
    gravity_edges = [
        (g["num"], tag) for g in GRAVITIES for cell, tag in g["forces"] if cell == f["cell"]
    ]
    grav_str = ", ".join(
        f"{gravity_id(n)} ({'precondition-for' if t == 'generated' else 'associated-with'})"
        for n, t in gravity_edges
    ) or "none (see Doc_08 §5 by-gravity index view; no gravity is unconnected fleet-wide)"
    return (
        f"Re-derived from the approved Doc_08 (Cell {f['matrix_cell']}, Force {f['cell']}). "
        f"Cross-cell connections (Doc_08 §4): {cross_str}. Gravity linkage (Doc_08 §5): "
        f"{grav_str} -- precondition-for used exactly where Doc_08 §5's own text uses the verb "
        f"'generated' (or its own paraphrases, 'generated as the refusal of...', 'generated in "
        f"response', 'generated from the inheritance refused') for this pair, associated-with "
        f"for every other verb, matching Gallic's own precedent exactly (gallic.force.egyptian-"
        f"standard: 'the founding relationship an initiating-cell force has to the gravity it "
        f"originates'). Canon_cells left empty, matching fleet convention for gravity/force "
        f"records."
    )


def build_gravity_record(g: dict) -> dict:
    return {
        "id": gravity_id(g["num"]),
        "world_id": WORLD_ID,
        "record_type": "gravity",
        "schema_version": 2,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": g["confidence"],
        "sources": g["sources"],
        "relations": build_gravity_relations(g),
        "name": g["name"],
        "classification": g["classification"],
        "description": g["description"].strip(),
        "manifestations": g["manifestations"],
    }


def build_force_record(f: dict) -> dict:
    return {
        "id": force_id(f["cell"]),
        "world_id": WORLD_ID,
        "record_type": "force",
        "schema_version": 2,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": f["confidence"],
        "sources": f["sources"],
        "relations": build_force_relations(f),
        "name": f["name"],
        "kind": f["kind"],
        "matrix_cell": f["matrix_cell"],
        "description": f["description"].strip(),
        "manifestations": f["manifestations"],
    }


# ---------------------------------------------------------------------------
# Closing the 18 "parked for B-5" notes in the existing story/figure records.
# Reads each file directly (not from the `records` dict this script itself
# builds -- these are files B-4 already wrote), appends real relations[]
# entries to that file's own frontmatter, and replaces its parked paragraph
# with a short "closed at B-5" note. The reciprocal edge on each gravity
# record is added by close_reciprocity() once these records join the batch.
# ---------------------------------------------------------------------------
def close_parked_note(path: Path, grav_nums: list[str], rel_type: str) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"{path}: no frontmatter fence"
    end = text.index("\n---\n", 4)
    front_text = text[4:end]
    body = text[end + 5:]
    payload = yaml.safe_load(front_text)
    rels = payload.setdefault("relations", [])
    for num in grav_nums:
        target = gravity_id(num)
        if not any(r.get("type") == rel_type and r.get("target") == target for r in rels):
            rels.append({"type": rel_type, "target": target})

    marker = "FEC / GRAVITY LINKAGE (parked for B-5"
    idx = body.index(marker)
    kept = body[:idx].rstrip("\n")
    names = ", ".join(f"{n} ({GRAVITY_BY_NUM[n]['name']})" for n in grav_nums)
    closing = (
        f"FEC / GRAVITY LINKAGE (closed at B-5): the connection this record's own Doc_09 "
        f"entry named above is now a real relations[] entry in this file's frontmatter -- "
        f"{rel_type} to {names} -- with the reciprocal edge declared on each gravity record "
        f"itself (witt.gravity.*), exactly as this note said it would when B-5 ran. No longer "
        f"parked."
    )
    new_body = kept + "\n\n" + closing + "\n"
    payload["relations"] = rels
    return {"path": path, "payload": payload, "body": new_body}


def write_record(path: Path, payload: dict, body: str) -> None:
    front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    path.write_text(f"---\n{front}---\n{body.strip()}\n", encoding="utf-8")


def main() -> None:
    GRAVITY_DIR.mkdir(parents=True, exist_ok=True)
    FORCE_DIR.mkdir(parents=True, exist_ok=True)

    records: dict[str, dict] = {}
    for g in GRAVITIES:
        records[gravity_id(g["num"])] = build_gravity_record(g)
    for f in FORCES:
        records[force_id(f["cell"])] = build_force_record(f)

    # Close the 18 parked story/figure notes -- read/patch in place, added to
    # the same `records` batch so close_reciprocity() can add the gravity
    # side's reciprocal edge.
    closed = []
    for slug, nums in STORY_GRAVITIES.items():
        rel_type = STORY_RELATION_OVERRIDE.get(slug, "associated-with")
        result = close_parked_note(STORY_DIR / f"witt.story.{slug}.md", nums, rel_type)
        records[result["payload"]["id"]] = result["payload"]
        closed.append(result)
    for slug, nums in FIGURE_GRAVITIES.items():
        result = close_parked_note(FIGURE_DIR / f"witt.figure.{slug}.md", nums, "associated-with")
        records[result["payload"]["id"]] = result["payload"]
        closed.append(result)

    close_reciprocity(records)

    written = []
    for g in GRAVITIES:
        rid = gravity_id(g["num"])
        path = GRAVITY_DIR / f"{rid}.md"
        write_record(path, records[rid], build_gravity_body(g))
        written.append(str(path))
    for f in FORCES:
        rid = force_id(f["cell"])
        path = FORCE_DIR / f"{rid}.md"
        write_record(path, records[rid], build_force_body(f))
        written.append(str(path))
    for result in closed:
        write_record(result["path"], records[result["payload"]["id"]], result["body"])
        written.append(str(result["path"]))

    print(f"Wrote/updated {len(written)} records:")
    for p in written:
        print(f"  {p}")


if __name__ == "__main__":
    main()
