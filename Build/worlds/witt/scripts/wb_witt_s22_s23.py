"""B-2/B-3 (S2.2/S2.3): Lutheran Wittenberg & Its Congregations (witt) --
the mechanical lexicon split (B-2) and term authoring (B-3), combined into
one script because B-2's "split" step, for this world, IS the per-term
record boundary B-3 then fills -- there was no intermediate chunk-file
stage to split from (Doc_06 itself declines to produce deployment chunks,
per its own Discipline 1, and defers that to Phase B). This script
produces all 72 `witt.term.*` records under records/witt/term/, one per
Doc_06 §5 entry.

SOURCE OF TRUTH. Every term's content traces to World-Builds/Lutheran-
Wittenberg/witt_Doc_06_Full_Lexicon_Development.md (Revision 4, Approved to
Proceed, four adversarial rounds, 18 Tier 1 / 48 Tier 2 / 6 Tier 3), read in
full by the authoring pass before this script was written. No live
research and no general knowledge of Luther or Lutheranism was used; where
this script or its authored fields go beyond Doc_06's own words, the
extension is a direct, disclosed translation of Doc_06's content into this
world's own inhabited first-person voice (the "we"/"our"/"among us"
register witt.core.witt.md and witt_Representative_Permanent_Prompt_
Nikolaus.txt already established at B-1), never new content Doc_06 does
not itself carry.

MECHANICAL vs AUTHORED, declared plainly, per the process document's own
B-2/B-3 discipline:

  MECHANICAL (this script does it, no per-term judgment involved):
    - envelope fields (id, world_id, record_type, schema_version, status,
      register="emic", the confidence block's citation_specificity/
      verification_state/evidentiary_weight/formation_confidence -- these
      four are each set from a short, fixed, disclosed rule applied
      uniformly, not re-judged per term);
    - sources[] assembly: ROW_TO_ID below maps every Source Registry row
      number Doc_06 cites to the real `witt.source.*` id B-1 already
      minted (read directly off every witt/source/*.md record's own
      external_ids.witt_source_registry_row field -- confirmed 89/89,
      zero guessed ids);
    - retrieval.tier: copied directly from Doc_06's own final tier per
      entry (§1.3's table), never re-derived;
    - relations RECIPROCITY CLOSURE: each term below is hand-authored with
      its own outward relations (associated-with by default, tension-with
      where Doc_06's own entry states a tension), but the INVERSE back-
      edge on the target record is added mechanically by
      close_reciprocity() below, a pure structural pass with no content
      judgment (associated-with and tension-with are both symmetric per
      RELATION_INVERSE) -- see that function's own docstring for exactly
      what this does and does not claim;
    - the body paragraph's citation line (Doc_06 entry number, chunk
      would-be filename, tags, AG note, Registry rows) is assembled from
      each term's own stored `doc06_tags`/`ag_note`/`rows` fields, not
      independently composed per term.

  AUTHORED (hand-composed by this build pass, not mechanically derived):
    - world_word, false_friend, senses.{informational,evidential,personal,
      translational}, plain_meaning, quick_meaning, distortion_risk,
      canon_cells, retrieval.retrieve_when/do_not_retrieve_when, and each
      term's own `divergence_note` and per-row source loci. This is the
      real translation work: turning Doc_06's Level-2/Level-3 analytical
      prose (itself already a construction document, not runtime voice)
      into this world's own first-person "we" register, at the density
      this build's scope decision calls for (full depth for the 18 Tier 1
      + 6 Tier 3 terms; a genuinely complete but more economical depth for
      the 48 Tier 2 terms, matching Doc_06's own proportion of development
      between tiers). Confidence's `formation_confidence` is the one
      confidence-block field NOT mechanical in the pure sense -- Doc_02
      §14 / Doc_06 Discipline 8 states a fixed five-level calibration rule
      (doctrinal/confessional content and the founder's own registers are
      Documented; claimed parish practice is Widely Accepted; Table Talk
      is Contested as verbatim; reception is Inferential/Thin or
      Contested), and this script applies that EXTRACTED rule per term
      rather than re-judging confidence from scratch -- but which rule-
      branch a given term falls under (whether its central claim is
      doctrinal/confessional, or turns on claimed practice, or on
      reception) is a real per-term reading, stated in each term's own
      `formation_confidence` field below and explained in its
      `divergence_note`.

DISCLOSED SCOPE DECISIONS (stated once here, not repeated 72 times):

  1. RELATIONS -- single-pass effort, not a full reconciliation. Doc_06
     itself computed a 565-edge Related-Terms graph across its own 66
     Tier-1/Tier-2 entries by script AFTER all 72 entries existed (§7),
     with 274 reciprocal pairs reached by a dedicated candidate-return-link
     reading pass over 58 one-directional edges. This build authors each
     term's OWN outward relations directly from Doc_06's own Related Terms
     line for that entry (a real reading of Doc_06's content, not
     invented), and closes structural reciprocity mechanically (see
     above) -- but does NOT re-run Doc_06's own candidate-return-link
     judgment pass to add reciprocal links Doc_06 itself only reached by a
     dedicated second pass over the completed set. A full post-hoc
     relations reconciliation pass, in Doc_06's own sense, was not
     separately run here; this is disclosed in every term's own body
     paragraph, not left for a reader to discover.
  2. TIER-2 DEPTH -- genuinely complete, not padded to Tier-1 length.
     Doc_06's own Tier 2 entries are themselves compressed relative to its
     Tier 1 entries (its own §5 preamble: "Tier 2 entries carry the same
     sections compressed"). This script's Tier 2 term records follow that
     proportion: every required schema field is present and accurate, and
     `senses` is filled honestly for all four sub-fields, but at real
     economy rather than at Tier 1's density.
  3. CANON_CELLS -- a first-pass assignment, not a coverage audit. Each
     term is given 1-2 cells from the fleet's 28-cell taxonomy (six
     thematic F-numbers x four voice-suffixes E/I/P/T, plus C for Christ-
     specific content), judged from the term's own subject matter against
     the _fleet canon_question sample texts read before this pass (F1
     belief/theology, F2 scripture/reading, F3 authority/discipline, F4
     becoming-one-of-us/formation, F5 daily life/belonging, F6 self-
     critical/outsider view, C Christ specifically). This is a real
     per-term judgment call, not a mechanical derivation, and it is NOT a
     claim that every one of the 28 cells is now covered -- gate_canon_
     coverage is expected to still report empty cells until B-4/B-5 add
     gravity/story/quote records, exactly as the task brief anticipates.

ALIAS SAFETY (B-2's own birth condition, process doc §3 B-2 row). The
live engine/m1/gates.py `gate_alias_safety` (read in full before writing
this script) checks exactly one thing: no term's `false_friend` entry may
exactly match (case-folded) another term's `world_word` string. Every
`world_word` below is written as a distinguishing PHRASE (the term plus
its own defining tag, e.g. "grace / 'a gracious God'", never a bare
generic word standing alone), and every `false_friend` entry is a
descriptive misreading-phrase (following gallic.term.virtus's own
pattern), never a bare word. This satisfies the gate by construction, for
every one of the 72 terms, from birth -- no retrofit pass is needed,
matching the Hieronymian precedent the process document cites. (The gate
as implemented checks only within one call's own `records` argument, which
for this world's own validation run is `records/witt/` alone -- the
_fleet directory carries no `term` records to collide with.)
"""
from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[4]
OUT_DIR = REPO_ROOT / "records" / "witt" / "term"
WORLD_ID = "lutheran-wittenberg-and-its-congregations"

# MECHANICAL. Registry row number -> the real witt.source.* id B-1 already
# minted, read directly off every records/witt/source/*.md file's own
# external_ids.witt_source_registry_row field (confirmed 89/89 present,
# 2026-09-19). Never guessed.
ROW_TO_ID: dict[int, str] = {
    1: "witt.source.luther-selections-from-luthers-prefaces-to-his",
    2: "witt.source.luther-disputation-on-the-power-and-efficacy",
    3: "witt.source.luther-treatise-on-the-holy-sacrament",
    4: "witt.source.luther-discussion-of-confession",
    5: "witt.source.luther-fourteen-of-consolation",
    6: "witt.source.luther-treatise-on-good-works",
    7: "witt.source.luther-treatise-on-the-new-testament-that",
    8: "witt.source.luther-papacy-at-rome-an-answer",
    9: "witt.source.luther-treatise-concerning-the-blessed-sacrament",
    10: "witt.source.luther-treatise-concerning-the-ban",
    11: "witt.source.luther-open-letter-to-the-christian-nobility",
    12: "witt.source.luther-babylonian-captivity-of-the-church",
    13: "witt.source.luther-treatise-on-christian-liberty",
    14: "witt.source.luther-brief-explanation-of-the-ten-commandments",
    15: "witt.source.luther-eight-wittenberg-sermons",
    16: "witt.source.luther-that-doctrines-of-men-are",
    17: "witt.source.luther-argument-in-defense-of-all",
    18: "witt.source.luther-magnificat-translated-and-explained",
    19: "witt.source.luther-earnest-exhortation-for-all-christians-warning",
    20: "witt.source.luther-secular-authority-to-what-extent-it",
    21: "witt.source.luther-to-the-leipzig-goat",
    22: "witt.source.luther-reply-to-the-answer",
    23: "witt.source.luther-answer-to-the-superchristian-superspiritual",
    24: "witt.source.luther-to-the-knights-of-the-teutonic",
    25: "witt.source.luther-large-catechism",
    26: "witt.source.luther-small-catechism",
    27: "witt.source.luther-deutsche-geistliche-lieder-the-hymns",
    28: "witt.source.luther-four-hymnal-prefaces-to-walters-gesangb",
    29: "witt.source.luther-ein-feste-burg-ist-unser-gott",
    30: "witt.source.luther-ein-neues-lied-wir-heben",
    31: "witt.source.luther-selections-from-the-table-talk",
    32: "witt.source.johann-testimony-concerning-luthers-divine-discourses",
    34: "witt.source.luther-on-the-bondage-of-the-will",
    35: "witt.source.luther-martin-luthers-judgment-of-erasmus",
    36: "witt.source.erasmus-de-libero-arbitrio-diatribe",
    37: "witt.source.melanchthon-augsburg-confession",
    38: "witt.source.melanchthon-apology-of-the-augsburg-confession",
    39: "witt.source.roman-confutation-of-the-augsburg-confession",
    40: "witt.source.leo-bull-exsurge-domine",
    41: "witt.source.jerome-controversial-writings-against-luther",
    42: "witt.source.augustin-latin-and-german-tracts",
    43: "witt.source.andreas-theses-and-sermons-of-1521-as",
    44: "witt.source.karsthans",
    45: "witt.source.johann-letter-of-reminiscence-on-luther-as",
    46: "witt.source.johann-eyewitness-report-of-luthers-first-invocavit",
    47: "witt.source.cyriacus-preface-to-the-cithara-lutheri",
    48: "witt.source.luther-admonition-to-peace",
    61: "witt.source.luther-de-votis-monasticis",
    62: "witt.source.philadelphia-edition-vols-iv",
    63: "witt.source.philadelphia-vols-i-iii-general-introduction",
    87: "witt.source.philadelphia-vols-i-iii",
    94: "witt.source.luther-von-den-juden-und-ihren-l",
}

# MECHANICAL. Doc03 cluster number -> this record's own slug, so every
# term's `related`/`tension` list (authored against Doc_06's own Related
# Terms lines) resolves to a real id without hand-typing 72 ids twice.
SLUG_BY_NUM: dict[str, str] = {
    "1.1": "indulgence", "1.2": "repentance", "1.3": "contrition", "1.4": "satisfaction",
    "1.5": "purgatory", "1.6": "the-keys", "1.7": "the-cross",
    "2.1": "faith", "2.2": "justification", "2.3": "good-works", "2.4": "merit",
    "2.5": "grace", "2.6": "law-and-gospel", "2.7": "promise-and-testament",
    "2.8": "conscience", "2.9": "free-will", "2.10": "sin",
    "3.1": "the-word", "3.2": "gospel", "3.3": "scripture-against-tradition",
    "3.4": "doctrines-of-men", "3.5": "letter-and-spirit", "3.6": "christ-alone",
    "4.1": "catechism", "4.2": "household", "4.3": "what-does-this-mean",
    "4.4": "to-have-a-god-is-to-trust", "4.5": "fear-and-love-god", "4.6": "neighbor",
    "4.7": "the-devil", "4.8": "daily", "4.9": "hymn",
    "5.1": "sacrament", "5.2": "baptism", "5.3": "sacrament-of-the-altar",
    "5.4": "given-for-you", "5.5": "both-kinds", "5.6": "the-mass",
    "5.7": "transubstantiation", "5.8": "congregation", "5.9": "the-ban",
    "5.10": "confession-and-absolution", "5.11": "worthy-unworthy",
    "6.1": "spiritual-and-temporal-estate", "6.2": "we-are-all-priests", "6.3": "office",
    "6.4": "calling", "6.5": "pastor", "6.6": "christendom",
    "6.7": "pope-and-antichrist", "6.8": "sects-and-new-spirits", "6.9": "the-turk",
    "7.1": "the-two-governments", "7.2": "the-sword", "7.3": "obedience",
    "7.4": "insurrection", "7.5": "must-and-free",
    "8.1": "vows", "8.2": "chastity", "8.3": "marriage", "8.4": "spiritual-geysterey",
    "8.5": "perfection", "8.6": "fasting", "8.7": "saints", "8.8": "images",
    "9.1": "comfort", "9.2": "temptation", "9.3": "assurance", "9.4": "death",
    "9.5": "prayer", "9.6": "martyr", "9.7": "patience",
}

TERMS: list[dict] = [

# ============================== Cluster 1 ==================================
# Pardon, penalty, and the treasure -- the 1517 vocabulary (Doc_06 5.1)
dict(
    num="1.1", slug="indulgence", tier=2, doc03_tier=1, demoted=True,
    world_word="indulgence, or pardon -- a 'letter of pardon'",
    world_word_plain="indulgence / pardon",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented as the founding 1517 occasion and as our own confession's later account of "
        "what the practice had been. Carried at Tier 2, not Tier 1, because it organizes no "
        "formation activity of ours after 1520 -- the demotion is about ecological centrality, "
        "not evidential weakness; the Apology's own retelling (Ap 6365-6378, read entire this "
        "pass) is as confessional-voice a witness as anything in this lexicon."
    ),
    canon_cells=["F1-I"],
    rows=[1, 2, 12, 25, 38],
    row_loci={
        2: "the Ninety-Five Theses (Jacobs's English), Theses 21, 27, 36, 53",
        12: "Babylonian Captivity's account of satisfaction and the sacraments",
        25: "the Large Catechism, 3805-3807 -- indulgences remembered as a defunct practice",
        38: "the Apology XII and VI on satisfactions and indulgences, read entire this pass (Ap 6365-6378, 10406-10409)",
        1: "the 1539 preface, cited among this entry's Registry rows (Doc_06 SS5 entry 1.1)",
    },
    related=["1.2", "1.4", "1.5", "1.6", "2.4", "9.3", "3.2", "6.7"], tension=[],
    plain_meaning=(
        "An indulgence is a letter the pope's preachers sold, remitting the penalty a repentant "
        "sinner still owed -- never guilt, never purgatory, whatever the sellers claimed. It was "
        "the practice our first public argument, in 1517, was aimed against."
    ),
    false_friend=[
        "hearing 'indulgence' as self-gratification rather than a canonical remission of penalty",
        "assuming the purchase reached guilt or purgatory, when we said from the first Thesis it could not",
        "treating the word as a practice still live among us, not a defunct memory by 1529",
    ],
    senses=dict(
        informational=(
            "What the pope's preachers sold us was a letter remitting the penalty a repentant "
            "sinner still owed -- 'so soon as the penny jingles into the money-box,' we used to "
            "say of it. We never granted that the pope's pardon reached anything but 'the "
            "penalties of sacramental satisfaction, and these are appointed by man'; every truly "
            "repentant Christian, we said from the first, 'has a right to full remission of "
            "penalty and guilt, even without letters of pardon.' Giving to the poor, we said, "
            "does a better work than buying pardons. By 1520 we were calling the whole trade a "
            "'knavish trick'; by 1529 it was already a memory in our own household book -- the "
            "day 'the Pope with his letters and bulls dispensed indulgences' -- and by 1530 our "
            "own confession could explain what the word had once meant and how it came to be "
            "misunderstood as freeing souls from purgatory."
        ),
        evidential=(
            "The founding argument is the Ninety-Five Theses' own; our later confession, in the "
            "Apology, gives the word's own history in its own voice, one register answering the "
            "other rather than repeating it."
        ),
        personal=(
            "We do not hold indulgences as a doctrine we still reject in the abstract. We "
            "remember them as the occasion -- the transaction and the false assurance it sold -- "
            "against which our whole first public word was spoken, and as a word that had "
            "already become, in our own lifetime, a thing our own book explains to children "
            "rather than a trade any of us still sees."
        ),
        translational=(
            "If you hear 'indulgence' as buying forgiveness of guilt outright, you have the wrong "
            "target: what we refused was a purchased remission of penalty and a false assurance "
            "sold in a letter, not the idea that penalty for sin exists at all."
        ),
    ),
    quick_meaning=(
        "A papal letter remitting penalty, not guilt -- the practice our first public argument "
        "attacked in 1517, and by 1529 only a memory of a trade we no longer see."
    ),
    retrieve_when=["indulgence, pardon, or 'letters of pardon'", "whether we still sell or believe in indulgences",
                   "the Ninety-Five Theses' own target"],
    do_not_retrieve_when=["the participant means purgatory itself (retrieve purgatory)",
                           "the participant means merit or satisfaction generally (retrieve merit or satisfaction)"],
    doc06_tags="[SC][DR][TC][RT]",
    ag_note="none -- both voices (Ap 5011-5019, 6365-6378, 10406-10409)",
),

dict(
    num="1.2", slug="repentance", tier=1, doc03_tier=1,
    world_word="repentance -- 'the whole life of believers should be repentance'",
    world_word_plain="repentance / penance",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented at every register we speak in, from the first Thesis to the household's "
        "catechism: the confessional definition (two parts, terror and faith), the founding "
        "sentence, and the daily baptismal form are each attested in their own voice, not "
        "inferred from one another."
    ),
    canon_cells=["F1-I", "F4-P"],
    rows=[2, 12, 25, 26, 37, 38],
    row_loci={
        2: "the Ninety-Five Theses, Theses 1-2",
        12: "Babylonian Captivity's account of penance -- contrition, confession, satisfaction",
        37: "the Augsburg Confession XII, repentance's two parts",
        38: "the Apology XII, read to 5234 this pass -- contrition and faith, and 'before the writings of Luther appeared, the doctrine of repentance was very much confused'",
        26: "the Small Catechism on baptism -- daily drowning of the old Adam",
        25: "the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 1.2)",
    },
    related=["1.1", "1.3", "1.4", "1.6", "2.1", "2.6", "2.8", "5.2", "5.10", "9.3"], tension=[],
    plain_meaning=(
        "Repentance is not a sacrament a priest administers once; it is the whole turning of a "
        "believer's life, in two parts -- the conscience's terror under the Law, and its comfort "
        "by faith in the promise. Our baptism makes it daily."
    ),
    false_friend=[
        "'penance' heard as a punishment or penalty a priest hands down",
        "'repentance' heard as a single feeling of regret or a one-time conversion",
        "the Latin left untranslated as though the meaning were self-evident -- our own translators had to argue for 'repent' against 'do penance'",
    ],
    senses=dict(
        informational=(
            "The first thing we said in public was a sentence about this word: 'Our Lord and "
            "Master Jesus Christ, when He said Poenitentiam agite, willed that the whole life of "
            "believers should be repentance' -- and the second was that this could not mean 'the "
            "sacramental penance, confession and satisfaction, administered by the priests.' We "
            "used to speak of penance as having three parts, contrition, confession and "
            "satisfaction; we re-founded each one. By 1530 we held to two parts only: 'one is "
            "contrition, that is, terrors smiting the conscience through the knowledge of sin; "
            "the other is faith, which is born of the Gospel, or of absolution.' We even say the "
            "word had been dark before us: 'before the writings of Luther appeared, the doctrine "
            "of repentance was very much confused.' In the household it is daily and bodily -- "
            "baptism means 'the old Adam in us should be drowned by daily sorrow and repentance, "
            "and die with all sins and evil lusts, and, in turn, a new person daily come forth.'"
        ),
        evidential=(
            "Attested in every register we use, from the founding Theses through the household "
            "catechism to the confession signed before the Emperor; the Apology names the "
            "founder by name as the one who cleared the word's confusion."
        ),
        personal=(
            "This word explains, in one breath, why we kept private confession and refused the "
            "sale of pardons at the same time -- both answer to the same two-part shape, terror "
            "then comfort, that our whole doctrine runs on."
        ),
        translational=(
            "Do not hear 'repentance' as an episode of feeling sorry, and do not hear 'penance' "
            "as a penalty a priest assigns: we hold one word, a lifelong turning with two parts, "
            "daily in baptism and sacramental in absolution, never a work that earns anything."
        ),
    ),
    quick_meaning=(
        "The whole-life turning our first public Thesis names, in two parts -- the conscience's "
        "terror under the Law, and its comfort by faith -- and which our baptism makes daily."
    ),
    retrieve_when=["repentance or penance", "contrition, confession, or satisfaction as parts of penance",
                   "why we kept confession but refused indulgences", "what baptism means daily"],
    do_not_retrieve_when=["the participant means contrition alone (retrieve contrition)",
                           "the participant means the sacrament of confession's own mechanics (retrieve confession/absolution)"],
    doc06_tags="[SC][DR][TC][RT]",
    ag_note="none -- both voices, every register from the first Thesis to the Apology",
),

dict(
    num="1.3", slug="contrition", tier=2, doc03_tier=2,
    world_word="contrition -- 'the true terror of conscience'",
    world_word_plain="contrition",
    distortion_risk="medium", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the Augsburg Confession's and Apology's own definition, read entire this pass (Ap XII).",
    canon_cells=["F1-P"],
    rows=[2, 12, 37, 38],
    row_loci={
        38: "the Apology XII, read this pass -- 'the true terror of conscience'",
        37: "the Augsburg Confession XII",
        12: "Babylonian Captivity, on the schools' invented 'attrition'",
        2: "the Ninety-Five Theses, on the uncertainty of one's own contrition",
    },
    related=["1.2", "1.6", "2.8", "2.6"], tension=[],
    plain_meaning=(
        "Contrition is sorrow for sin -- but never a feeling we can manufacture or be sure of on "
        "our own. We call it 'the true terror of conscience,' and it is worth nothing without "
        "faith added to it."
    ),
    false_friend=["contrition as an adequate emotional condition for forgiveness -- 'if I'm sorry enough'"],
    senses=dict(
        informational=(
            "'No one is sure that his own contrition is sincere,' we said from the start, and "
            "that uncertainty is the point: the schools had invented a so-called 'attrition,' "
            "converted into contrition 'by virtue of the power of the keys' -- we hold instead "
            "that a contrite heart 'is found only where there is a lively faith in the promises "
            "and the threats of God.' Our confession defines it as 'terrors smiting the "
            "conscience through the knowledge of sin,' produced when sin is censured by God's "
            "own Word -- a terror human nature cannot endure unsustained."
        ),
        evidential="Attested in the founding Theses, the Babylonian Captivity, and the confession and Apology alike.",
        personal="Contrition never stands alone for us; it is the first half of repentance, and its worth is decided entirely by whether faith is added to it.",
        translational="Do not hear contrition as a feeling that earns forgiveness by its own intensity; we hold it worthless without faith, and never sure of itself.",
    ),
    quick_meaning="Sorrow for sin -- 'the true terror of conscience,' found only where faith is, never manufactured by the keys.",
    retrieve_when=["contrition or attrition", "whether feeling sorry enough is what matters"],
    do_not_retrieve_when=["the participant means repentance's whole shape (retrieve repentance)"],
    doc06_tags="[SC][TC][DR]", ag_note="none",
),

dict(
    num="1.4", slug="satisfaction", tier=2, doc03_tier=2,
    world_word="satisfaction -- two referents, ours refused and Christ's alone sufficient",
    world_word_plain="satisfaction (two referents)",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented in both senses; the alias problem itself (one English word for two opposite "
        "referents, ours and Christ's) is Doc_06's own finding, resolved inside the entry rather "
        "than smoothed away."
    ),
    canon_cells=["F1-I"],
    rows=[2, 37, 38],
    row_loci={
        37: "the Augsburg Confession IV, XV, XXIV",
        38: "the Apology XII and XXIV on satisfactions, read this pass (Ap 5003-5020, 8672-8673)",
        2: "the Ninety-Five Theses, on satisfactions relaxed by pardons",
    },
    related=["1.1", "1.2", "2.2", "2.4", "5.6"], tension=[],
    plain_meaning=(
        "One word, two opposite things: the satisfaction a sinner tries to make -- pilgrimages, "
        "rosaries, the third part of the old penance -- which we refuse; and the satisfaction "
        "Christ has already made for our sins, which is the ground of everything."
    ),
    false_friend=["the two referents collapsed into one doctrine, or heard as mere contentment"],
    senses=dict(
        informational=(
            "We refuse the first: 'these graces of pardon concern only the penalties of "
            "sacramental satisfaction, and these are appointed by man,' and 'human traditions "
            "instituted to propitiate God, to merit grace, and to make satisfaction for sins, are "
            "opposed to the Gospel.' We rest entirely on the second: Christ 'by His death, has "
            "made satisfaction for our sins,' and 'there has been only one propitiatory sacrifice "
            "in the world, namely, the death of Christ.'"
        ),
        evidential="Both senses attested in the confession itself, side by side -- the same word refusing one claim and resting on another.",
        personal="What we cannot make, Christ has made; keeping the two apart by whose satisfaction it is, not by any other distinction, is the whole of this word for us.",
        translational="A participant who hears 'satisfaction' in the sense we refuse (our own) inside a sentence about the sense we rest on (Christ's) has lost the argument entirely.",
    ),
    quick_meaning="One word for two opposite things: the penitent's own satisfaction, refused; and Christ's, sufficient and ours by faith.",
    retrieve_when=["satisfaction, in either sense", "what indulgences relaxed"],
    do_not_retrieve_when=["the participant means merit generally (retrieve merit)"],
    doc06_tags="[SC][TC][DR]",
    ag_note="cross-voice, one word, two referents (an alias problem, resolved here)",
),

dict(
    num="1.5", slug="purgatory", tier=2, doc03_tier=2,
    world_word="purgatory -- reasoned with, then denied, then buried",
    world_word_plain="purgatory",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented as a real change across our own texts, both voices, rather than a fixed "
        "position held from the first day -- the entry states the arc rather than flattening it "
        "(Doc_03 had proposed 'Luther-only'; Doc_06's own reading of Ap 5003-6377 found the "
        "confessional voice too, corrected this pass)."
    ),
    canon_cells=["F1-I"],
    rows=[2, 28, 38],
    row_loci={
        2: "the Ninety-Five Theses, Thesis 1517 reasoning that still allows purgatory's furniture",
        38: "the Apology, read this pass -- 'Scripture does not teach' purgatory (Ap 5003-5011, 6363-6365)",
        28: "the 1542 funeral preface -- purgatory among the 'popish horrors' abolished",
    },
    related=["1.1", "1.6", "9.4"], tension=[],
    plain_meaning=(
        "A state after death we still reasoned about in 1517; by 1531 our confession said "
        "flatly that Scripture does not teach it; by 1542 our founder's funeral preface counted "
        "it among the horrors done away with at our burials."
    ),
    false_friend=["assuming we never used the word, or that our founder denied it from his first day"],
    senses=dict(
        informational=(
            "In 1517 the word was still furniture: 'Hell, purgatory, and heaven seem to differ "
            "as do despair, almost-despair, and the assurance of safety,' and the only dispute "
            "was whether the pope's keys reached it. By 1531 we said flatly that eternal "
            "punishments commuted 'to the punishments of purgatory' is a scheme Scripture does "
            "not teach, and that the keys 'have not the power of binding and loosing except upon "
            "earth.' By 1542 our founder's own funeral preface counted purgatory among the "
            "things 'abolished, done away, and out-and-out made an end of' at our burials, "
            "against 'our doctrine of the resurrection, not that of purgatory with its pains and "
            "expiations.'"
        ),
        evidential="A real change traced across three periods and two voices, not a single fixed denial.",
        personal="This is a word whose arc is our own history: reasoned with, then denied, then buried -- and we state that change rather than pretend we never held the earlier position.",
        translational="Do not assume we never used the word purgatory or denied it from day one; we reasoned inside it in 1517 and had refused it by 1531.",
    ),
    quick_meaning="A state after death we still reasoned about in 1517, which by 1531 'Scripture does not teach,' and by 1542 is among the horrors buried with our dead.",
    retrieve_when=["purgatory", "what happened to the idea of purgatory over our own history"],
    do_not_retrieve_when=["the participant means indulgences themselves (retrieve indulgence)"],
    doc06_tags="[SC][RT][DR]",
    ag_note="none -- both voices (Ap 5003-5011, 6363-6365; Doc_03 had proposed 'Luther-only, cross-register')",
),

dict(
    num="1.6", slug="the-keys", tier=2, doc03_tier=1, demoted=True,
    world_word="the keys -- Christ's 'whatsoever thou shalt bind,' a ministry, not a power",
    world_word_plain="the keys / power of the keys",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented at every register cited; carried at Tier 2 because its two organizing claims "
        "-- the community's authority and the ministry of absolution -- are already other "
        "terms' own evidence (3.1's authority sense, 5.10's absolution), so this entry is not "
        "itself a generator, whatever its own evidential richness."
    ),
    canon_cells=["F3-I"],
    rows=[2, 11, 12, 37, 38],
    row_loci={
        11: "Christian Nobility -- 'the keys were not given to Peter alone, but to the whole community'",
        12: "Babylonian Captivity -- 'no mention at all of power, but of the ministry of him that absolves'",
        38: "the Apology XII, read this pass -- 'if the power of the keys does not console us before God, what, then, will pacify the conscience?'",
        2: "the Ninety-Five Theses, on the keys and purgatory",
        37: "the Augsburg Confession, cited among this entry's Registry rows (Doc_06 SS5 entry 1.6)",
    },
    related=["1.1", "1.3", "1.5", "3.1", "5.10", "6.2", "1.2", "3.3", "6.7"], tension=[],
    plain_meaning=(
        "Christ's word to bind and loose, given not to one man but to the whole community -- a "
        "ministry of the Word, not a power, and whose whole object is a conscience made sure."
    ),
    false_friend=["the keys heard as a papal or clerical power over people, rather than a ministry the whole community holds"],
    senses=dict(
        informational=(
            "'The keys were not given to Peter alone, but to the whole community... the keys "
            "were not ordained for doctrine or government, but only for the binding and loosing "
            "of sin.' What happens when they are used is not an exercise of power: 'He calls "
            "forth the faith of the penitent... Here there is no mention at all of power, but of "
            "the ministry of him that absolves'; to claim them for the pope alone is 'a wicked "
            "usurpation of power.' Our confession keeps the word and fixes its extent -- a power "
            "'to preach the Gospel, to remit and retain sins, and to administer Sacraments' -- "
            "and the Apology puts the stake plainly: 'if the power of the keys does not console "
            "us before God, what, then, will pacify the conscience?'"
        ),
        evidential="Attested across the founder's polemics and both confessional documents alike.",
        personal="We do not hold the keys as a power over us; we hold them as a promise that makes a terrified conscience sure -- which is why we say the pastor's absolving voice 'must be believed not otherwise than we would believe a voice from heaven.'",
        translational="Do not hear 'the keys' as a clerical or papal power held over people; we hold them as a ministry of the Word, given to the whole community, whose only object is sin and whose whole point is comfort.",
    ),
    quick_meaning="Christ's word 'whatsoever thou shalt bind' -- a promise that calls forth faith and a ministry the whole community holds, never a power, and never the pope's alone.",
    retrieve_when=["the keys, or the power of the keys", "who holds the authority to forgive sins among us"],
    do_not_retrieve_when=["the participant means confession's own two parts (retrieve confession/absolution)"],
    doc06_tags="[SC][TC][DR][RT]", ag_note="none",
),

dict(
    num="1.7", slug="the-cross", tier=2, doc03_tier=2,
    world_word="the cross -- 'Cross, cross'; affliction borne, never chosen",
    world_word_plain="the cross",
    distortion_risk="medium", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the Theses' own close, the baptismal banner, and both confessional documents.",
    canon_cells=["F1-P"],
    rows=[2, 3, 37],
    row_loci={
        2: "the Ninety-Five Theses' own close, Theses against 'Peace, peace' where there is no cross",
        37: "the Augsburg Confession XXVI, the true mortification",
        3: "the 1519 baptism treatise -- the Holy Cross as our banner",
    },
    related=["5.2", "9.2", "8.5", "4.7"], tension=[],
    plain_meaning=(
        "The affliction a Christian bears -- sent, never chosen. Our Theses ended by blessing "
        "'Cross, cross' against those who cry 'Peace, peace,' and in baptism we are enrolled "
        "under the Holy Cross as our banner."
    ),
    false_friend=["'the cross' heard as a system ('theology of the cross') or as a voluntary austerity we chose"],
    senses=dict(
        informational=(
            "Our Ninety-Five Theses end on it: 'Blessed be all those prophets who say to the "
            "people of Christ, Cross, cross, and there is no cross!' -- against those who say "
            "'Peace, peace.' In baptism a Christian is enrolled under 'our Captain, under Whose "
            "banner (i.e., the Holy Cross) we continually fight against sin.' Our confession "
            "calls this teaching our own kind of mortification -- 'true, earnest, and unfeigned' "
            "-- against a chosen or self-imposed kind."
        ),
        evidential="Attested from the founding Theses through both confessional documents.",
        personal="We do not choose the cross as a discipline; it is sent, and it is the banner under which our baptism enrolls us for the whole of the fight against sin.",
        translational="Do not hear 'the cross' as a system or a method we teach; we mean affliction sent, not chosen -- a banner and a battle.",
    ),
    quick_meaning="Affliction we bear, never choose -- the banner of our baptism, and our Theses' own answer to those who cry 'Peace, peace.'",
    retrieve_when=["the cross, or bearing affliction", "whether we chose suffering as a discipline"],
    do_not_retrieve_when=["the participant means temptation broadly (retrieve temptation)"],
    doc06_tags="[SC][DR][RT]", ag_note="none",
),

# ============================== Cluster 2 ==================================
# Faith, works, and righteousness -- the justification cluster (Doc_06 5.2)
dict(
    num="2.1", slug="faith", tier=1, doc03_tier=1,
    world_word="faith -- trust that clings to God's promise, 'faith alone'",
    world_word_plain="faith / 'faith alone'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented in every register we use, from the founder's treatises to the household "
        "catechism to the confession signed at Augsburg -- the safest vocabulary in our whole "
        "lexicon, and also the one our own household book had to fence against its own radicals "
        "by 1529, which is carried here rather than smoothed into a single untroubled claim."
    ),
    canon_cells=["F1-I", "F1-P"],
    rows=[6, 12, 13, 15, 25, 37, 38],
    row_loci={
        6: "Good Works -- faith as 'the first and highest, the most precious of all good works'",
        12: "Babylonian Captivity -- 'faith alone is the saving and efficacious use of the Word of God'",
        13: "Christian Liberty's own paradox",
        15: "the Eight Wittenberg Sermons -- faith as the one 'must'",
        25: "the Large Catechism -- our own caveat against a bare 'faith alone' with nothing to stand on",
        37: "the Augsburg Confession IV, XX",
        38: "the Apology IV, read this pass to 1457 -- what faith is and is not",
    },
    related=["2.2", "2.3", "2.5", "2.7", "2.8", "2.6", "2.10", "3.1", "5.1", "5.11", "7.5", "4.4",
             "9.3", "1.2", "5.4", "6.8", "8.1", "9.2"], tension=[],
    plain_meaning=(
        "Faith is a taking hold of God's promise -- trust, not the mere knowledge of a story. It "
        "is the one thing we say justifies, without works, and the one thing we call a 'must' -- "
        "but never faith standing on nothing."
    ),
    false_friend=[
        "faith as belief-that, assent to propositions, or a private feeling",
        "'faith alone' heard as license -- that works do not matter",
        "faith heard as a thing one does to be saved, rather than a trust received from outside",
    ],
    senses=dict(
        informational=(
            "'Faith alone is the saving and efficacious use of the Word of God'; 'the first and "
            "highest, the most precious of all good works is faith in Christ,' and every other "
            "good work receives its goodness from it, like a loan. Our confession says it before "
            "the Emperor: 'men cannot be justified before God by their own strength, merits, or "
            "works, but are freely justified for Christ's sake, through faith.' It is not "
            "'merely a knowledge of history... but to assent to the promise of God'; it comes "
            "from outside -- 'faith is conceived from the Word'; 'faith cometh by hearing' -- and "
            "its object is always a promise. In the parish we preach it as received: 'whosoever "
            "will put his trust in Him, should be free from sin and a child of God,' with the "
            "immediate warning that 'a faith without love is not enough -- rather it is not "
            "faith at all.' In the sermons it is the one 'must': 'that which necessity requires, "
            "and which must ever be unyielding.' And in our own household catechism we state our "
            "own caveat against our own formula: our radicals 'assert that faith alone saves, "
            "and that works and external things avail nothing' -- but 'faith must have something "
            "which it believes... upon which it stands and rests.' Faith alone, but never faith "
            "in nothing: it stands on the Word, the water, the bread, the absolution."
        ),
        evidential=(
            "The most widely attested word in our whole lexicon -- founder's treatises, sermons, "
            "household catechism, and both confessional documents, with no register missing."
        ),
        personal=(
            "Nearly everything else we hold presupposes this word: what works receive their "
            "goodness from, what a sacrament is used by, why the conscience can be at rest, and "
            "what makes one worthy at the table. Our own confession can say the whole doctrine "
            "'is to be referred to that conflict of the terrified conscience.'"
        ),
        translational=(
            "Do not hear 'faith alone' as a license that works do not matter, and do not hear "
            "faith as private belief we produce in ourselves: we mean trust in a promise spoken "
            "from outside, received not produced, standing on Word and sacrament, followed "
            "necessarily by love and works that earn nothing -- and a formula we ourselves had "
            "to fence against our own radicals by 1529."
        ),
    ),
    quick_meaning=(
        "Trust that clings to God's promise -- the one thing we say justifies, without works, "
        "and the one thing we call a 'must'; never a bare formula standing on nothing."
    ),
    retrieve_when=["faith, or 'faith alone'", "whether works matter at all", "what faith is not -- belief in a story, a feeling, a work"],
    do_not_retrieve_when=["the participant means justification's own technical shape (retrieve justification)",
                           "the participant means the free will question (retrieve free will)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none -- both voices, every register",
),

dict(
    num="2.2", slug="justification", tier=1, doc03_tier=1,
    world_word="justification -- to be accounted righteous, 'for Christ's sake, through faith'",
    world_word_plain="justification / to justify",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented that both wordings occur in our own texts ('imputes for righteousness' and "
        "'the making of a righteous man'); Contested how the two relate, which our own texts "
        "hold together on purpose rather than resolve. [CT], provisional, two contest types "
        "(meaning within its historical context; relationship to present-day traditions): no "
        "secondary source is rowed in the Source Registry for either contest, and per Doc_06 "
        "SS2 this tag does not reach runtime vocabulary on Doc_06's word alone -- carried "
        "forward here as still provisional, not resolved by this authoring pass, which does not "
        "characterize any present-day tradition's reading."
    ),
    canon_cells=["F1-I", "C-I"],
    rows=[13, 34, 37, 38],
    row_loci={
        37: "the Augsburg Confession IV, XX -- 'this faith God imputes for righteousness in His sight'",
        38: "the Apology IV, read this pass to 1457 -- both wordings held together on purpose",
        13: "Christian Liberty",
        34: "Bondage of the Will (OCR-degraded), the 'grand hinge' remark to Erasmus",
    },
    related=["2.1", "2.3", "2.4", "2.5", "2.7", "2.8", "2.9", "2.10", "1.4", "9.3", "3.6"], tension=[],
    plain_meaning=(
        "God's act of accounting a sinner righteous -- and, in the same breath, of making one -- "
        "for Christ's sake, through faith. Our own confession calls this 'the chief topic of "
        "Christian doctrine.'"
    ),
    false_friend=[
        "justification as a legal fiction -- 'declared righteous but not changed'",
        "justification as a moral improvement one achieves by effort",
        "the word treated as a settled formula whose exact sense is obvious, when our own texts hold two wordings together on purpose",
    ],
    senses=dict(
        informational=(
            "'This faith God imputes for righteousness in His sight' -- and 'in this controversy "
            "the chief topic of Christian doctrine is treated.' Our own word for the ground is "
            "'the merits of another, namely, of Christ alone.' Remission of sins 'is something "
            "promised for Christ's sake. Therefore it cannot be received except by faith alone. "
            "For a promise cannot be received except by faith alone.' We say the word does two "
            "things at once, on purpose: 'by faith itself, we are for Christ's sake accounted "
            "righteous... and because \"to be justified\" means that out of unjust men just men "
            "are made, or born again, it means also that they are pronounced or accounted just. "
            "For Scripture speaks in both ways.' What we exclude is not works but confidence in "
            "works. The word's whole purpose, for us, is certainty: 'sure and firm consolation "
            "against the terrors of sin.'"
        ),
        evidential=(
            "Attested throughout the confessional voice's own Article IV, and in the founder's "
            "own words to Erasmus -- both voices, weighted toward the Apology's technical "
            "development."
        ),
        personal=(
            "Our whole doctrine turns on this word being able to give a terrified conscience "
            "something sure -- 'how will such persons sustain themselves in death who have heard "
            "nothing of this faith?'"
        ),
        translational=(
            "Do not resolve this word into either 'a legal fiction' or 'a moral improvement': we "
            "hold one act with two descriptions together on purpose, accounted and made, "
            "received by faith alone, for Christ's sake -- and our own texts leave exactly how "
            "the two relate an open question, not a settled formula."
        ),
    ),
    quick_meaning=(
        "God's act of accounting a sinner righteous -- and of making one -- 'for Christ's sake, "
        "through faith': our confession's 'chief topic of Christian doctrine.'"
    ),
    retrieve_when=["justification, or to be justified", "the chief topic of our doctrine",
                    "whether justification means declared righteous or made righteous"],
    do_not_retrieve_when=["the participant means faith itself as trust (retrieve faith)",
                           "the participant asks for a modern denomination's own reading of justification -- we characterize none"],
    doc06_tags="[SC][TC][DR][RT][CT]",
    ag_note="none by attestation; weighted to the Apology's technical development",
    ct=(
        "CT status carried from Doc_06 SS2.1: two contest types -- meaning within its historical "
        "context (how 'accounted' and 'made' relate) and relationship to present-day traditions "
        "(this entry characterizes none). Provisional: no secondary source is rowed in the "
        "Source Registry for either contest; Doc_06 names leads for the Registry owner "
        "(McGrath's Iustitia Dei; Mannermaa's Christ Present in Faith; the 1999 Joint "
        "Declaration) but cites none as a source. This authoring pass carries the tag forward "
        "as still provisional and does not resolve it."
    ),
),

dict(
    num="2.3", slug="good-works", tier=2, doc03_tier=1, demoted=True,
    world_word="good works -- everything God has commanded, done in faith",
    world_word_plain="good works",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented in both the founder's treatise and the confession's own answer to the standing charge that we forbid good works.",
    canon_cells=["F5-I"],
    rows=[2, 6, 13, 37, 38],
    row_loci={
        6: "Good Works -- opening only read (6713-6882); the treatise's own Decalogue exposition unread",
        37: "the Augsburg Confession, answering the charge that we forbid good works",
        38: "the Apology, 'confidence in the merit of love or of works is excluded in justification'",
        2: "the Ninety-Five Theses -- giving to the poor a better work than buying pardons",
        13: "Christian Liberty, cited among this entry's Registry rows (Doc_06 SS5 entry 2.3)",
    },
    related=["2.1", "2.2", "2.4", "6.4", "6.3", "8.5", "4.6"], tension=[],
    plain_meaning=(
        "Not the short medieval list of pious acts, but everything God has commanded -- trade, "
        "walking, eating, sleeping -- done in faith, and necessary only because God wills it, "
        "never a means of earning anything."
    ),
    false_friend=["'works' heard as charity or ritual, and 'faith alone' heard as their abolition"],
    senses=dict(
        informational=(
            "'There are no good works except those which God has commanded' -- not 'praying in "
            "church, fasting, and almsgiving,' which we say defines good works too narrowly, but "
            "what a Christian does 'when they work at their trade, walk, stand, eat, drink, "
            "sleep,' all good in faith and none good without it. Our confession answers the "
            "standing charge that we forbid good works: 'it is necessary to do good works, not "
            "that we should trust to merit grace by them, but because it is the will of God.' "
            "Love and works 'must follow faith'; they are not excluded from following, only "
            "confidence in their merit is excluded."
        ),
        evidential="Attested in the founder's own treatise and the confession's answer to the standing accusation against us.",
        personal="This is our answer to being called antinomians: the whole of ordinary life, commanded and therefore good in faith, worth nothing as a price.",
        translational="Do not hear 'works' as charity or ritual alone, and do not hear 'faith alone' as their abolition: we mean the whole of ordinary life, commanded and therefore good, necessary and worthless as a price.",
    ),
    quick_meaning="Not a short list of pious acts but the whole of ordinary life -- trade, walking, eating, sleeping -- done in faith and commanded by God.",
    retrieve_when=["good works", "whether faith alone means works do not matter"],
    do_not_retrieve_when=["the participant means merit specifically (retrieve merit)"],
    doc06_tags="[SC][DR][RT]", ag_note="none",
),

dict(
    num="2.4", slug="merit", tier=2, doc03_tier=2,
    world_word="merit -- meritum congrui / meritum condigni, denied to us, reserved to Christ",
    world_word_plain="merit",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the confession's own naming of the schools' Latin distinctions in order to reject them.",
    canon_cells=["F1-I"],
    rows=[2, 13, 27, 37, 38],
    row_loci={
        38: "the Apology, read this pass -- 'their feigning a distinction between meritum congrui and meritum condigni is only an artifice'",
        37: "the Augsburg Confession -- justified 'not by their own strength, merits, or works'",
        2: "the Ninety-Five Theses, denying indulgences as the merits of Christ and the saints",
        27: "the hymns -- 'Naught building on my merit'",
        13: "Christian Liberty, cited among this entry's Registry rows (Doc_06 SS5 entry 2.4)",
    },
    related=["2.2", "2.3", "1.4", "1.1", "8.1", "8.5", "2.9"], tension=[],
    plain_meaning=(
        "What we deny to every human work and reserve to Christ alone -- the scholastic "
        "distinctions named in their own Latin only so that we can refuse them."
    ),
    false_friend=["'merit' heard as deserving in a general sense, rather than the specific scholastic claim we refuse"],
    senses=dict(
        informational=(
            "We deny that indulgences are 'the merits of Christ and the Saints'; we deny that "
            "anyone is justified 'by their own strength, merits, or works.' We name the schools' "
            "own vocabulary only to reject it: 'their feigning a distinction between meritum "
            "congrui and meritum condigni is only an artifice in order not to appear openly to "
            "Pelagianize.' Faith brings us 'not confidence in one's own merits, but only "
            "confidence in the promise.' Merit is Christ's alone, 'the merits of another, namely, "
            "of Christ alone'; our own hymn sings, 'Naught building on my merit.'"
        ),
        evidential="Attested in the founding Theses, the confession, the Apology's own naming of the schools' Latin, and our hymnody.",
        personal="We refuse this word in its own technical Latin so plainly that even our hymns confess we build nothing on it.",
        translational="Do not hear 'merit' as deserving in general; we mean a technical claim that works earn grace, which we refuse in its own Latin and give entirely to Christ.",
    ),
    quick_meaning="What we deny to every human work and reserve to Christ alone -- the scholastic distinctions named in Latin only to be refused.",
    retrieve_when=["merit, or meritum congrui/condigni", "what earns grace, if anything"],
    do_not_retrieve_when=["the participant means satisfaction specifically (retrieve satisfaction)"],
    doc06_tags="[SC][TC][DR]", ag_note="none; the Latin is the adversaries' as our confession quotes it",
),

dict(
    num="2.5", slug="grace", tier=2, doc03_tier=1, demoted=True,
    world_word="grace -- 'a gracious God,' free favour received by faith",
    world_word_plain="grace / 'a gracious God'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the household catechism's own reason-clause and the founder's own altar-sentence.",
    canon_cells=["F1-P"],
    rows=[12, 15, 25, 26, 27, 37],
    row_loci={
        26: "the Small Catechism -- given 'not because I've earned it or deserved it'",
        25: "the Large Catechism -- the Creed 'brings pure grace'",
        15: "the Eight Wittenberg Sermons, cited among this entry's Registry rows (Doc_06 SS5 entry 2.5)",
        27: "the hymns -- 'God saw, in his eternal grace, my sorrow out of measure'",
        12: "Babylonian Captivity, cited among this entry's Registry rows (Doc_06 SS5 entry 2.5)",
        37: "the Augsburg Confession, baptism as offering grace",
    },
    related=["2.1", "2.2", "2.6", "2.8", "9.1"], tension=[],
    plain_meaning=(
        "God's free favour, given 'not because I've earned it or deserved it' -- what faith "
        "receives, and what makes us able to say, at the altar, 'I cannot doubt I have a "
        "gracious God.'"
    ),
    false_friend=["grace pictured as a substance infused into us, or as mere leniency, rather than a favour known in a person"],
    senses=dict(
        informational=(
            "In the household the word is learned as a reason: God gives everything 'because of "
            "His pure, fatherly and divine goodness and His mercy, not because I've earned it or "
            "deserved it.' In the catechism it is what the Creed brings, against what the "
            "Commandments only tell us to do: the Creed 'brings pure grace, and makes us godly "
            "and acceptable to God.' At the altar it becomes the one sentence our hope rests on: "
            "'I cannot doubt I have a gracious God.'"
        ),
        evidential="Attested across the household catechism, the sermons, and our own hymnody.",
        personal="This is the word for what faith receives and justification names as free -- not an organizer of its own beyond those two.",
        translational="Do not hear grace as a substance poured in or as leniency; we mean a favour freely given, received by faith, known as a gracious God -- a person, not a quantity.",
    ),
    quick_meaning="God's free favour, given 'not because I've earned it or deserved it' -- known at the altar as 'I cannot doubt I have a gracious God.'",
    retrieve_when=["grace, or 'a gracious God'", "whether grace is earned"],
    do_not_retrieve_when=["the participant means justification's technical shape (retrieve justification)"],
    doc06_tags="[SC][DR][RT]", ag_note="none",
),

dict(
    num="2.6", slug="law-and-gospel", tier=1, doc03_tier=1,
    world_word="Law and Gospel -- 'commands and promises,' the illness and the remedy",
    world_word_plain="Law and Gospel",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented at every register, 1520 through 1531; the [AS] comparative tag (whether "
        "neighbouring formation worlds share this exact grammar) stays Inferential/Thin, since "
        "no neighbour's own lexicon exists yet to compare against -- carried here as a standing "
        "caveat, not resolved."
    ),
    canon_cells=["F1-I", "F2-I"],
    rows=[13, 14, 20, 25, 38],
    row_loci={
        13: "Christian Liberty -- 'all the Scriptures of God are divided into two parts, commands and promises'",
        25: "the Large Catechism -- the Creed 'tells what God does for us' against the Commandments' 'what we ought to do'",
        38: "the Apology IV -- 'the Law worketh wrath... the Law always accuses and terrifies consciences'",
        20: "Secular Authority, Part One -- the Law's work of teaching us to recognize sin",
        14: "the Kurze Form -- the catechism's own order, illness then remedy",
    },
    related=["2.1", "2.7", "2.8", "1.2", "1.3", "3.1", "3.2", "3.5", "4.1", "9.3", "2.10", "2.5"], tension=[],
    plain_meaning=(
        "Our own way of reading the whole of Scripture as two things -- commands, showing what "
        "we ought to do and cannot; and promises, giving what the commands ask -- so that a "
        "person is first shown the illness, then the remedy."
    ),
    false_friend=[
        "'Law and Gospel' heard as a labelled theological method or system",
        "the pairing heard as Old Testament against New Testament",
        "the pairing heard as legalism against grace in general terms",
    ],
    senses=dict(
        informational=(
            "'All the Scriptures of God are divided into two parts -- commands and promises... "
            "the commands show us what we ought to do, but do not give us the power to do it,' "
            "while 'the promises of God give what the commands of God ask.' The Law has a work "
            "of its own -- 'to teach men to recognize sin, that they may be made humble unto "
            "grace' -- and 'the Law worketh wrath... the Law always accuses and terrifies "
            "consciences.' This is our own catechism's order too: the Commandments 'teach a man "
            "to know his illness,' the Creed 'teaches him where he may find the remedy.' It is "
            "never a topic of its own for us; it is the grammar in which faith, the Word, the "
            "catechism and the conscience are each spoken -- present everywhere we use it, "
            "nowhere taught as a subject by itself."
        ),
        evidential="Attested at every register we speak in, 1520 through 1531, from the founder's own treatises through the household catechism to the confession's own rule of reading.",
        personal="Nearly everything else we hold runs on this grammar -- repentance's two parts, the Word's whole authority, the catechism's own order, the conscience's whole sequence.",
        translational="Do not hear 'Law and Gospel' as a labelled system, or as Old Testament against New, or as legalism against grace in general: we mean two kinds of speech found throughout all of Scripture, read in order on a single person -- first the illness, then the remedy.",
    ),
    quick_meaning="Our own way of reading all of Scripture as two things -- commands, which show what we ought to do and cannot, and promises, which give what the commands ask.",
    retrieve_when=["Law and Gospel, or 'commands and promises'", "why we read Scripture the way we do",
                   "what the Law is for, if not to save"],
    do_not_retrieve_when=["the participant means the Gospel's own content specifically (retrieve Gospel)"],
    doc06_tags="[AS][TC][DR][RT]", ag_note="none -- both voices, 1520 and 1529 and 1531",
),

dict(
    num="2.7", slug="promise-and-testament", tier=1, doc03_tier=1,
    world_word="promise -- and, at the altar, 'a testament, a promise made by one about to die'",
    world_word_plain="promise / testament",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented; the [AS] tag (for 'testament' as our own name for the Supper, as a "
        "comparative claim about neighbouring worlds) stays Inferential/Thin, since no "
        "neighbour's own lexicon exists yet."
    ),
    canon_cells=["F1-I", "C-I"],
    rows=[4, 7, 12, 25, 37, 38],
    row_loci={
        7: "the New Testament preface -- 'a testament, as every one knows, is a promise made by one about to die'",
        12: "Babylonian Captivity -- 'what we call the mass is the promise of remission of sins made to us by God'",
        37: "the Augsburg Confession XIII -- sacraments as 'signs and testimonies of the will of God toward us'",
        38: "the Apology IV, XIII, read this pass -- 'wherever there is a promise faith is required'",
        25: "the Large Catechism -- prayer grounded on 'besides this command also a promise'",
        4: "Confession, cited among this entry's Registry rows (Doc_06 SS5 entry 2.7)",
    },
    related=["2.1", "2.2", "2.6", "5.1", "5.3", "5.6", "5.10", "9.5", "9.3", "3.1", "3.2", "5.4"], tension=[],
    plain_meaning=(
        "God's word that comes first and gives before any human work -- and, at the altar, a "
        "testament: a promise made by one about to die, so that the mass is God's promise of "
        "forgiveness, never a sacrifice we offer."
    ),
    false_friend=["'promise' heard as a hope for the future rather than a word spoken now to be taken by faith",
                  "'testament' heard as a book of the Bible rather than Christ's own bequest"],
    senses=dict(
        informational=(
            "Nothing begins with us: 'not that man begin lay the first stone, but that God "
            "alone, without any entreaty or desire of man, must first come and give him a "
            "promise.' At the altar the promise has a name: 'a testament, as every one knows, is "
            "a promise made by one about to die, in which he designates his bequest and appoints "
            "his heirs'; 'what we call the mass is the promise of remission of sins made to us "
            "by God.' A testament is received, not offered -- the whole difference between our "
            "mass and the sacrifice we refused. Our confession makes the pair a rule of "
            "everything: 'wherever there is a promise faith is required, and conversely,' and "
            "even prayer rests on it -- 'besides this command also a promise.'"
        ),
        evidential="Attested across the founder's New Testament preface, the sacramental treatises, and the confessional documents alike.",
        personal="Every practice we keep is grounded the same way -- a promise first, faith taking hold of it second; this is the logic under our whole sacramental life.",
        translational="Do not hear 'promise' as a hope for later, and do not hear 'testament' as a book of the Bible: we mean a word God speaks first, now, to be taken by faith, and, at the altar, Christ's own bequest received by heirs, never a work rendered to God.",
    ),
    quick_meaning="God's word that comes first and gives before any human work -- and, at the altar, Christ's own testament, received by faith, never offered as a sacrifice.",
    retrieve_when=["promise, or testament", "why the mass is not a sacrifice we offer"],
    do_not_retrieve_when=["the participant means the Sacrament of the Altar's whole doctrine (retrieve Sacrament of the Altar)"],
    doc06_tags="[AS][TC][DR][RT]", ag_note="none -- the testament argument is the founder's own; 'promise' is confessional too",
),

dict(
    num="2.8", slug="conscience", tier=1, doc03_tier=1,
    world_word="conscience -- 'terrified,' 'anxious,' 'captive'; the court where our doctrine is decided",
    world_word_plain="conscience",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the confession's own statement that its whole teaching lives here; the Apology's most repeated adjective, 'terrified,' occurs 29 times.",
    canon_cells=["F1-P"],
    rows=[4, 15, 16, 18, 25, 31, 37, 38],
    row_loci={
        37: "the Augsburg Confession XX -- 'this whole doctrine is to be referred to that conflict of the terrified conscience'",
        38: "the Apology IV, XII, read this pass",
        15: "the Eight Wittenberg Sermons -- liberty preached only to 'poor, humble, captive consciences'",
        16: "That Doctrines of Men Are to Be Rejected -- consciences burdened wrongly",
        25: "the Large Catechism -- false worship as what 'concerns the conscience alone'",
        31: "the Table Talk -- 'the pope is a mere tormentor of the conscience' (Contested as verbatim)",
        4: "Confession, cited among this entry's Registry rows (Doc_06 SS5 entry 2.8)",
        18: "the Magnificat, footnote only, cited among this entry's Registry rows (Doc_06 SS5 entry 2.8)",
    },
    related=["1.2", "1.3", "2.1", "2.2", "2.6", "3.4", "5.10", "5.11", "7.1", "7.5", "9.1", "9.3",
             "9.4", "2.5", "7.3"], tension=[],
    plain_meaning=(
        "The inner court where our whole doctrine is decided -- terrified by the Law, comforted "
        "by the promise, and for whose sake we hold that 'we must have many absolutions.'"
    ),
    false_friend=["conscience heard as a moral compass, an inner voice telling right from wrong to be followed"],
    senses=dict(
        informational=(
            "'God-fearing and anxious consciences find by experience that it brings the greatest "
            "consolation, because consciences cannot be set at rest through any works, but only "
            "by faith... this whole doctrine is to be referred to that conflict of the terrified "
            "conscience.' That is our confession's own statement of where its teaching lives. "
            "Under the Law the conscience is terrified -- 'the Law always accuses and terrifies "
            "consciences' -- and under the promise it is comforted -- 'we must have many "
            "absolutions, so that we may strengthen our timid consciences and despairing hearts "
            "against the devil and against God.' What binds it wrongly is our test for what is "
            "wicked: 'consciences are not to be burdened'; Christian liberty is preached 'only "
            "to poor, humble, captive consciences.' Even false worship is defined here: it "
            "'concerns the conscience alone that seeks in its own works help, consolation, and "
            "salvation.'"
        ),
        evidential="The Apology's most repeated adjective in this connection, 'terrified,' occurs 29 times; attested in every register we use.",
        personal="This is where every one of our doctrines lands -- G1 is referred to it, absolutions exist for it, liberty is preached to it, our two governments are distinguished for its comfort.",
        translational="Do not hear 'conscience' as a moral compass that guides right from wrong; we mean the place where a person stands accused and is made sure -- terrified by the Law, comforted by the promise, not a guide but a court.",
    ),
    quick_meaning="The inner court where our whole doctrine is decided -- terrified by the Law, comforted by the promise, for whose sake we hold 'many absolutions.'",
    retrieve_when=["conscience, terrified or anxious", "what the whole doctrine of faith is 'for'",
                   "what binds a conscience wrongly"],
    do_not_retrieve_when=["the participant means guilt as a feeling in general, outside our own theological frame"],
    doc06_tags="[SC][DR][TC][RT]",
    ag_note="none -- both voices; the Apology's most repeated adjective ('terrified,' 29 times)",
),

dict(
    num="2.9", slug="free-will", tier=2, doc03_tier=2,
    world_word="free will -- free for civil things, bound toward God; 'bondage,' 'assertion'",
    world_word_plain="free will / bondage",
    distortion_risk="high", weight="corroborating",
    formation_confidence="Documented",
    divergence_note=(
        "Documented at the confession's own statement (AC XVIII), the cleaner witness; weighted "
        "to a single OCR-degraded work (Bondage of the Will) for the sustained argument itself, "
        "disclosed rather than used to demote -- every further quotation from that work would "
        "need its own character-level re-check before being voiced as settled."
    ),
    canon_cells=["F1-I"],
    rows=[12, 27, 34, 37],
    row_loci={
        37: "the Augsburg Confession XVIII -- some liberty in civil righteousness, none toward God without the Spirit",
        34: "Bondage of the Will (OCR-degraded) -- the two kingdoms mutually militating, and 'we delight in assertions'",
        27: "the hymns -- 'Free-will against God's judgment fought, and dead to good remained'",
        12: "Babylonian Captivity, cited among this entry's Registry rows (Doc_06 SS5 entry 2.9)",
    },
    related=["2.2", "2.4", "2.10", "7.1", "4.7"], tension=[],
    plain_meaning=(
        "A will that can choose civil righteousness but has no power, without the Holy Ghost, to "
        "work the righteousness of God -- denied against Erasmus in a book that also defends the "
        "very posture of asserting a doctrine rather than holding it as an opinion."
    ),
    false_friend=["'free will' heard as a philosophical problem about determinism, or as denying all human choice whatever"],
    senses=dict(
        informational=(
            "Our confession grants the will 'some liberty to choose civil righteousness' and "
            "denies it 'power, without the Holy Ghost, to work the righteousness of God.' The "
            "founder's sustained argument locates the bondage in a war: 'there are two kingdoms "
            "in the world mutually militating against each other... Satan reigns in the one... "
            "in the other kingdom Christ reigns.' The argument's own manner is part of its "
            "content: 'allow us to be assertors, and to study and delight in assertions... the "
            "Holy Spirit is not a sceptic.'"
        ),
        evidential="The one sustained argument in our library, weighted to a single OCR-degraded work; the confession's own statement is the cleaner witness.",
        personal="This is the ground of our refusal of merit -- what cannot even begin toward God cannot earn anything from God.",
        translational="Do not hear 'free will' denied as denying every human choice: we mean a will free for civil things and bound toward God -- and a claim we insist on asserting, not holding lightly.",
    ),
    quick_meaning="A will free to choose civil righteousness but bound toward God without the Spirit -- denied against Erasmus, and asserted rather than merely opined.",
    retrieve_when=["free will, or bondage of the will", "the Erasmus debate"],
    do_not_retrieve_when=["the participant means predestination as a separate question, which our library does not develop"],
    doc06_tags="[SC][TC][DR]",
    ag_note="weighted to a single work (Bondage) whose OCR requires per-quotation re-check",
),

dict(
    num="2.10", slug="sin", tier=2, doc03_tier=1, demoted=True,
    world_word="sin -- 'born with sin,' an inherited condition, not a discrete bad act",
    world_word_plain="sin / original sin",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented at the Augsburg Confession's own definition (AC II), read as this entry's "
        "coverage; the Apology's own Article II (150-541) remains unread by this build, and the "
        "catechisms' own scattered treatment of the word was not separately gathered under this "
        "headword -- a real coverage gap, disclosed rather than smoothed, not a finding of "
        "silence."
    ),
    canon_cells=["F1-I"],
    rows=[26, 37],
    row_loci={
        37: "the Augsburg Confession II -- 'born with sin, that is, without the fear of God, without trust in God, and with concupiscence'",
        26: "the Small Catechism -- baptism drowning the old Adam daily",
    },
    related=["2.1", "2.2", "2.6", "2.9", "4.4", "5.2"], tension=[],
    plain_meaning=(
        "Not a discrete bad act but an inherited condition -- born without the fear of God, "
        "without trust in God, and with disordered desire -- which faith, not effort, answers."
    ),
    false_friend=["sin heard as a single wrong act, or as a feeling of guilt"],
    senses=dict(
        informational=(
            "'Since the fall of Adam all men begotten in the natural way are born with sin, that "
            "is, without the fear of God, without trust in God, and with concupiscence; and that "
            "this disease, or vice of origin, is truly sin.' We condemn those who deny this and "
            "who argue a person can be justified by strength and reason alone. In the household "
            "the condition has a daily remedy: 'the old Adam in us should be drowned by daily "
            "sorrow and repentance.' Sin here is a state we are born into, whose two marks -- no "
            "fear, no trust -- are exactly what the First Commandment asks for."
        ),
        evidential="Attested at the confession's own definition; our reading of the fuller Apology treatment of this word remains incomplete.",
        personal="This is the presupposition under our whole doctrine of faith -- the diagnosis the Law performs, and what baptism's daily drowning acts on.",
        translational="Do not hear sin as one discrete wrong act or a guilty feeling; we mean an inherited disease of origin -- no fear, no trust, disordered desire -- that only faith answers.",
    ),
    quick_meaning="Not a discrete bad act but an inherited condition -- born without fear or trust toward God -- which faith, not effort, answers.",
    retrieve_when=["sin, or original sin", "what 'born with sin' means among us"],
    do_not_retrieve_when=["the participant means a single wrongful act they are asking about morally, not doctrinally"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="Melanchthon-only as read; the founder's own texts use 'sin' constantly without a single defining locus found in what was read -- a coverage gap",
),

# ============================== Cluster 3 ==================================
# The Word, the Scriptures, and the doctrines of men -- interpretation (Doc_06 5.3)
dict(
    num="3.1", slug="the-word", tier=1, doc03_tier=1,
    world_word="the Word -- God's own speech, the Gospel of Christ, 'the Word must do it'",
    world_word_plain="the Word / Word of God",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at six of the eight coded registers the founder speaks in (two absent); the best-attested term in our whole lexicon.",
    canon_cells=["F2-I", "F2-P"],
    rows=[1, 11, 13, 15, 16, 20, 25, 26, 29, 37],
    row_loci={
        13: "Christian Liberty -- 'one thing and one only is necessary... the most holy Word of God, the Gospel of Christ'",
        25: "the Large Catechism -- 'accedat verbum ad elementum et fit sacramentum'",
        15: "the Eight Wittenberg Sermons -- 'I did nothing; the Word did it all'",
        11: "Christian Nobility -- Scripture's own authority against pope, councils, fathers",
        16: "That Doctrines of Men Are to Be Rejected, cited among this entry's Registry rows (Doc_06 SS5 entry 3.1)",
        1: "the 1539 preface -- 'the Bible has come to lie forgotten in the dust under the bench'",
        37: "the Augsburg Confession V, VII, XXVIII",
        29: "the hymns, Hymn XXVI -- 'one little word can fell him'",
        26: "the Small Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 3.1)",
        20: "Secular Authority, cited among this entry's Registry rows (Doc_06 SS5 entry 3.1)",
    },
    related=["2.1", "2.6", "2.7", "3.2", "3.3", "3.4", "3.5", "3.6", "4.1", "4.7", "4.9", "5.1",
             "5.8", "6.3", "6.8", "7.5", "1.6", "7.4"], tension=[],
    plain_meaning=(
        "God's own speech, the Gospel of Christ -- the one thing necessary; the power that makes "
        "a sacrament when joined to water or bread; the authority above pope, councils and "
        "fathers; and the agent that does the whole work of our reform while we sit still."
    ),
    false_friend=[
        "'the Word' heard as the Bible-as-book, a text one reads and interprets alone",
        "'the Word did it all' heard as modesty rather than a claim about who acts",
        "the Word heard as a doctrine of inspiration rather than a living, external speech-act",
    ],
    senses=dict(
        informational=(
            "'One thing and one only is necessary for Christian life, righteousness and "
            "liberty. That one thing is the most holy Word of God, the Gospel of Christ.' The "
            "Word is not talk: 'God's Word is not like some other silly prattle... but... the "
            "power of God.' It begets us -- 'the mother that begets and bears every Christian "
            "through the Word of God' -- and it makes sacraments: 'when the Word is joined to "
            "the element or natural substance, it becomes a Sacrament.' Its authority stands "
            "above every human one: 'the Bible has come to lie forgotten in the dust under the "
            "bench'; 'the keys were not given to Peter alone, but to the whole community.' And "
            "the Word acts, on its own, in our reform: 'his word should do the work alone, "
            "without our work... we have the jus verbi, but not the executio'; 'the Word must do "
            "this thing, and not we poor sinners'; 'I did nothing; the Word did it all.'"
        ),
        evidential="The best-attested word in our whole lexicon, in six of eight registers we speak in; the two absent are named rather than papered over.",
        personal="This is the agent hub of our whole ecology: the thing that 'must do it' everywhere we look -- our sacraments, our catechism, our office, our liberty, our song.",
        translational="Do not hear 'the Word' as a book we read alone, or 'the Word did it all' as modesty: we mean a living, external speech-act of God that begets, makes sacraments, drives off the devil and reforms churches on its own -- heard, not merely read, and the reason a preacher may not use force.",
    ),
    quick_meaning="God's own speech, the Gospel of Christ -- the power that makes a sacrament, the authority above every human office, and the agent that 'must do it' while we sit still.",
    retrieve_when=["the Word of God", "why we would not force reform with a sword",
                   "what makes a sacrament a sacrament", "authority over pope, councils, or fathers"],
    do_not_retrieve_when=["the participant means Scripture's authority specifically against named human traditions (retrieve Scripture against Fathers, Councils and pope)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none -- both voices; the best-attested term in the lexicon",
),

dict(
    num="3.2", slug="gospel", tier=2, doc03_tier=1, demoted=True,
    world_word="the Gospel -- 'the true treasure of the Church,' risen again in our own day",
    world_word_plain="the Gospel",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the founding Theses and the confession's own definition of the Church by this word.",
    canon_cells=["F1-I"],
    rows=[2, 13, 19, 25, 28, 37],
    row_loci={
        2: "the Ninety-Five Theses, Thesis 62 -- 'the true treasure of the Church is the Most Holy Gospel'",
        37: "the Augsburg Confession VII -- the Church as 'the congregation of saints, in which the Gospel is rightly taught'",
        28: "the hymnal prefaces -- 'the blessed Gospel, which by God's grace hath again risen'",
        19: "Earnest Exhortation, cited among this entry's Registry rows (Doc_06 SS5 entry 3.2)",
        13: "Christian Liberty, cited among this entry's Registry rows (Doc_06 SS5 entry 3.2)",
        25: "the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 3.2)",
    },
    related=["2.6", "2.7", "3.1", "5.8", "1.1"], tension=[],
    plain_meaning=(
        "The good news of Christ -- 'the true treasure of the Church' -- the promise half of "
        "Scripture, and the light we believe has risen again in our own day."
    ),
    false_friend=["'the Gospel' heard as the four biblical books, or as Christianity in general"],
    senses=dict(
        informational=(
            "'The true treasure of the Church is the Most Holy Gospel of the glory and the grace "
            "of God' -- set against the pope's treasury of pardons. It is what our own Church is "
            "defined by: 'the congregation of saints, in which the Gospel is rightly taught.' We "
            "believe we have recovered it: 'the blessed Gospel, which by God's grace hath again "
            "risen.'"
        ),
        evidential="Attested from the founding Theses through the confession's own definition of the Church.",
        personal="This is the treasure the indulgence-sellers had buried, and a light we experienced as risen again in our own lifetime.",
        translational="Do not hear 'the Gospel' as the four books or Christianity in general; we mean the specific promise of forgiveness for Christ's sake.",
    ),
    quick_meaning="'The true treasure of the Church' -- the promise of forgiveness for Christ's sake, which we believe has risen again in our own day.",
    retrieve_when=["the Gospel specifically as content, not as 'the Bible'"],
    do_not_retrieve_when=["the participant means the Word broadly (retrieve the Word)",
                           "the participant means Law and Gospel as the reading-grammar (retrieve Law and Gospel)"],
    doc06_tags="[SC][DR][RT]", ag_note="none",
),

dict(
    num="3.3", slug="scripture-against-tradition", tier=2, doc03_tier=1, demoted=True,
    world_word="Scripture against Fathers, Councils and pope -- 'under the bench'",
    world_word_plain="Scripture against Fathers, Councils and pope",
    distortion_risk="high", weight="corroborating",
    formation_confidence="Documented",
    divergence_note=(
        "Documented in two distinct registers -- Luther-only for the sharp form ('under the "
        "bench'), confirmed; Melanchthon's milder, additive form attested separately -- carried "
        "as two voices, not smoothed into one."
    ),
    canon_cells=["F2-I"],
    rows=[1, 11, 16, 23, 31, 37],
    row_loci={
        1: "the 1539 preface -- 'the Bible has come to lie forgotten in the dust under the bench'",
        11: "Christian Nobility -- 'if we are all priests... why should we not also have the power to test and judge'",
        37: "the Augsburg Confession -- doctrine that varies 'from the Scriptures, or from the Church Catholic, or from the Church of Rome as known from its writers'",
        23: "Answer to Emser, cited among this entry's Registry rows (Doc_06 SS5 entry 3.3)",
        16: "That Doctrines of Men Are to Be Rejected, cited among this entry's Registry rows (Doc_06 SS5 entry 3.3)",
        31: "the Table Talk, cited among this entry's Registry rows (Doc_06 SS5 entry 3.3)",
    },
    related=["3.1", "3.4", "3.5", "6.2", "6.7", "1.6"], tension=[],
    plain_meaning=(
        "The rule that every other writing points to Scripture and is judged by it -- said "
        "sharply by the founder ('under the bench') and additively by the confession ('the "
        "Scriptures, or... the Church Catholic')."
    ),
    false_friend=["'Scripture alone' heard as a slogan meaning the Fathers and councils are worthless -- no such Latin formula occurs in any of our own texts"],
    senses=dict(
        informational=(
            "'All other writings should point to the Scriptures, as John pointed to Christ'; "
            "'the Bible has come to lie forgotten in the dust under the bench.' Against those "
            "who claim to be the only masters of Scripture: 'if we are all priests... why should "
            "we not also have the power to test and judge what is correct or incorrect in "
            "matters of faith?' Our confession keeps the rule and changes its pitch: doctrine "
            "with 'nothing that varies from the Scriptures, or from the Church Catholic, or from "
            "the Church of Rome as known from its writers.'"
        ),
        evidential="The sharp form is the founder's own, single-register; the confession attests a milder, additive form separately.",
        personal="We hold the Fathers as witnesses to be judged by Scripture's light, not as authorities in their own right.",
        translational="Do not hear 'Scripture alone' as a fixed slogan dismissing every other voice; we state the rule two ways -- one sharp, one additive -- and never as a Latin formula.",
    ),
    quick_meaning="The rule that every writing points to Scripture and is judged by it -- said sharply ('under the bench') and additively ('the Scriptures, or the Church Catholic').",
    retrieve_when=["Scripture's authority over Fathers, councils, or the pope", "'under the bench'"],
    do_not_retrieve_when=["the participant means the Word's broader power (retrieve the Word)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="Luther-only, cross-register, for the sharp form; Melanchthon attests the milder, additive form",
),

dict(
    num="3.4", slug="doctrines-of-men", tier=2, doc03_tier=1, demoted=True,
    world_word="doctrines of men -- human traditions, refused only when made a merit or a 'must'",
    world_word_plain="doctrines of men / human traditions",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the treatise whose own title names this word, and at the Apology XV, read entire this pass.",
    canon_cells=["F1-I"],
    rows=[2, 11, 12, 16, 37, 38],
    row_loci={
        16: "That Doctrines of Men Are to Be Rejected -- the treatise's own title and rule",
        37: "the Augsburg Confession -- traditions 'instituted to propitiate God, to merit grace... are opposed to the Gospel'",
        38: "the Apology XV, read entire this pass -- traditions kept 'without superstition as civil customs'",
        11: "Christian Nobility, cited among this entry's Registry rows (Doc_06 SS5 entry 3.4)",
        12: "Babylonian Captivity, cited among this entry's Registry rows (Doc_06 SS5 entry 3.4)",
        2: "the Ninety-Five Theses, cited among this entry's Registry rows (Doc_06 SS5 entry 3.4)",
    },
    related=["3.1", "3.3", "2.8", "7.5", "8.6", "8.1", "8.7", "6.7", "8.8"], tension=[],
    plain_meaning=(
        "Teaching and commandment made by human beings and bound on the conscience -- fasting "
        "rules, orders' vows, compelled confession -- rejected on Christ's own word, but only "
        "when made to merit grace or bind the conscience, never simply for existing."
    ),
    false_friend=["assuming we rejected all tradition and ceremony, rather than only what claims to merit or compel"],
    senses=dict(
        informational=(
            "Our own treatise's title names it plainly: 'that doctrines of men are to be "
            "rejected.' Its rule: 'it is wicked to make a necessity and a commandment of that "
            "which is free.' Our confession draws the line exactly at the conscience: 'human "
            "traditions instituted to propitiate God, to merit grace, and to make satisfaction "
            "for sins, are opposed to the Gospel.' The Apology adds: 'no tradition was "
            "instituted by the holy Fathers with the design that it should merit the remission "
            "of sins... but for the sake of good order in the Church'; we 'cheerfully maintain "
            "the old traditions' and observe them 'without superstition as civil customs.'"
        ),
        evidential="Attested at the treatise's own title and the Apology's defense of Article XV, read entire this pass.",
        personal="This is where we draw our boundary against the papacy and, from the other side, against those who would refuse all order: kept for order, refused only as a merit or a 'must.'",
        translational="Do not assume we rejected all tradition and ceremony; we mean tradition kept for order and cheerfully, refused only where it is made a mediator, a merit, or a 'must' on the conscience.",
    ),
    quick_meaning="Human tradition kept for order and cheerfully -- refused only where made a merit or a 'must' bound on the conscience.",
    retrieve_when=["doctrines of men, or human traditions", "what tradition we kept versus refused"],
    do_not_retrieve_when=["the participant means a specific instance (fasting, vows, images) rather than the general rule (retrieve that specific term)"],
    doc06_tags="[SC][TC][DR][RT]", ag_note="none; the Apology XV read entire this pass",
),

dict(
    num="3.5", slug="letter-and-spirit", tier=2, doc03_tier=2,
    world_word="the letter and the spirit -- the plain sense IS the spiritual sense",
    world_word_plain="the letter and the spirit",
    distortion_risk="medium", weight="corroborating",
    formation_confidence="Documented",
    divergence_note="Documented at a single work, single register (Answer to Emser), disclosed rather than smoothed into a broader claim.",
    canon_cells=["F2-I"],
    rows=[23, 63],
    row_loci={23: "Answer to Emser, 'The Letter and the Spirit' section only"},
    related=["3.1", "2.6", "3.3", "3.6"], tension=[],
    plain_meaning=(
        "Against a hidden 'spiritual' sense laid secretly over the plain one, the rule that the "
        "literal sense is 'the sense accepted by Christ, God the Holy Spirit, and all the angels "
        "and saints.'"
    ),
    false_friend=["'the letter and the spirit' heard as legalism against freedom"],
    senses=dict(
        informational=(
            "Answering a claim of a hidden 'external sense and a secret sense,' we hold that the "
            "literal sense is 'the sense accepted by Christ, God the Holy Spirit, and all the "
            "angels and saints,' and 'in this way we must interpret all the Scriptures, even the "
            "ancient types.' A clear text is what a Christian must stand on alone."
        ),
        evidential="Attested at a single work, a single register -- disclosed rather than claimed broader.",
        personal="For us the plain sense is not a lesser sense to be transcended; it is the spiritual sense itself.",
        translational="Do not hear 'the letter and the spirit' as legalism against freedom; we mean a rule of reading -- no hidden layer beneath the plain one.",
    ),
    quick_meaning="Against a hidden 'spiritual' sense, the rule that the plain, literal sense of Scripture is itself the spiritual sense.",
    retrieve_when=["the letter and the spirit", "whether Scripture has a hidden meaning beneath the plain one"],
    do_not_retrieve_when=["the participant means Law and Gospel as two kinds of speech (retrieve Law and Gospel) -- this is one sense, not two kinds"],
    doc06_tags="[SC][TC]", ag_note="Luther-only, single-register (the Answer to Emser)",
),

dict(
    num="3.6", slug="christ-alone", tier=2, doc03_tier=2,
    world_word="Christ alone -- 'Hear ye Him, Him, Him,' the one Teacher and Mediator",
    world_word_plain="Christ alone",
    distortion_risk="medium", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at both the founder's own sermon and the confession's naming of Christ as sole Mediator.",
    canon_cells=["C-P"],
    rows=[13, 16, 37],
    row_loci={
        16: "That Doctrines of Men Are to Be Rejected -- 'Hear ye Him, Him, Him'",
        37: "the Augsburg Confession -- 'the one Christ as the Mediator, Propitiation, High Priest, and Intercessor'",
        13: "Christian Liberty, cited among this entry's Registry rows (Doc_06 SS5 entry 3.6)",
    },
    related=["3.1", "2.2", "8.7", "3.5"], tension=[],
    plain_meaning=(
        "The one Teacher the Father appointed -- 'Hear ye Him, Him, Him' -- and the one "
        "Mediator, so that all Scripture points to Christ alone."
    ),
    false_friend=["a bare slogan (solus Christus) rather than a rule of hearing and a tone"],
    senses=dict(
        informational=(
            "Christ 'alone has been made our Teacher by the Father... He did not say, Hear ye "
            "St. Bernard, St. Gregory, etc., but, Hear ye Him, Him, Him'; 'all the Scriptures "
            "point to Christ alone.' Our confession names 'the one Christ as the Mediator, "
            "Propitiation, High Priest, and Intercessor.'"
        ),
        evidential="Attested at a founder's sermon and the confession's own list of Christ's offices.",
        personal="We hear Christ's own words as a friend's: 'a good Friend, and his words are full of love.'",
        translational="Do not hear this as a bare slogan; we mean a rule of hearing -- one Teacher, one Mediator -- spoken in a friend's tone, not a formula's.",
    ),
    quick_meaning="The one Teacher the Father appointed, and the one Mediator -- so that all Scripture points to Christ alone.",
    retrieve_when=["Christ alone, or the one Mediator", "whether saints or teachers besides Christ mediate for us"],
    do_not_retrieve_when=["the participant means the saints' own status (retrieve saints)"],
    doc06_tags="[SC][RT]", ag_note="none",
),

# ============================== Cluster 4 ==================================
# Catechesis and the household -- the formation cluster (Doc_06 5.4)
dict(
    num="4.1", slug="catechism", tier=1, doc03_tier=1,
    world_word="the catechism -- 'the three parts,' 'the five parts,' said word for word for life",
    world_word_plain="catechism / 'the three parts'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented as prescription -- the catechism program itself, to the hour -- and "
        "Inferential/Thin as any household's or parish's actual practice, with the reading of "
        "reception Contested (the Strauss/Scribner/Kittelson debate, rowed R70-R72). This "
        "record carries Reported-Experience Status: reported as our own self-understanding, "
        "not assessed for historical accuracy at the household level; the confidence tag above "
        "applies to the documented program, not to any claim about what any household actually "
        "did."
    ),
    canon_cells=["F4-I", "F4-P"],
    rows=[14, 25, 26, 31, 37, 38],
    row_loci={
        25: "the Large Catechism, preface, First Commandment entire, Creed I and III, Prayer entire, Sacrament and Conclusion",
        26: "the Small Catechism, whole file",
        14: "the Kurze Form -- preface and Commandments; its Creed and Prayer unread",
        38: "the Apology XV -- 'with us the pastors and ministers of the churches are compelled publicly... to instruct and hear the youth'",
        31: "the Table Talk, cited among this entry's Registry rows (Doc_06 SS5 entry 4.1; Contested as verbatim)",
        37: "the Augsburg Confession, cited among this entry's Registry rows (Doc_06 SS5 entry 4.1)",
    },
    related=["4.2", "4.3", "4.4", "4.5", "4.8", "4.9", "2.6", "3.1", "5.11", "6.5", "9.5", "5.1",
             "4.6", "4.7", "7.5"], tension=[],
    plain_meaning=(
        "'Instruction for children, what every Christian must needs know' -- the Ten "
        "Commandments, the Creed and the Lord's Prayer, containing everything in Scripture, "
        "with the two sacraments' words added to make five parts. Every household is to say it "
        "word for word, morning, table and night, for life."
    ),
    false_friend=[
        "a catechism heard as a children's textbook, learned once and set aside",
        "the catechism heard as a doctrinal summary rather than a lifelong daily practice",
        "the catechism heard as a denominational identity document",
    ],
    senses=dict(
        informational=(
            "'Of old it was called in Greek catechism, i.e., instruction for children, what "
            "every Christian must needs know'; the three parts 'contain fully and completely "
            "everything that is in the Scriptures,' and with the sacraments they are 'five parts "
            "of the entire Christian doctrine,' 'a Short Summary and Epitome of the Entire Holy "
            "Scriptures.' It is to be said, not owned: our founder reports himself reading it "
            "'every morning, and whenever I have time,' calling himself 'a child who is being "
            "taught the Catechism,' who 'must remain a child and pupil of the Catechism, and am "
            "glad so to remain.' The book exists because of a failure we report of ourselves: "
            "'many pastors and preachers are very negligent in this,' and the common people "
            "'throw the book into a corner.' Our confession claims the practice before the "
            "Emperor: 'with us the pastors and ministers of the churches are compelled publicly "
            "to instruct and hear the youth; and this ceremony produces the best fruits.'"
        ),
        evidential=(
            "Documented as the whole of our 1529 output, in the founder's own voice and the "
            "confession's; whether any household or parish actually kept it is a different "
            "question our library does not answer from inside any household's own report."
        ),
        personal=(
            "This is our own word for the whole of Scripture made sayable and repeatable -- "
            "never finished, examined weekly, sung at work, the gate to the Sacrament, and "
            "written because we believed our own people were not holding what they had heard."
        ),
        translational=(
            "Do not hear 'catechism' as a children's textbook learned once, or as a badge of "
            "denominational identity: we mean the whole of Scripture in three sayable parts, "
            "recited daily for life by every Christian, examined weekly, and never finished -- "
            "we ourselves remain, by our own word, pupils of it."
        ),
    ),
    quick_meaning=(
        "'Instruction for children, what every Christian must needs know' -- the three parts "
        "said word for word, morning, table and night, for the whole of life, never finished."
    ),
    retrieve_when=["the catechism, or 'the three parts'/'the five parts'", "what every household is to know",
                   "why the catechism was written -- what failure prompted it"],
    do_not_retrieve_when=["the participant means the household as an institution rather than the book (retrieve household)",
                           "the participant means one specific part's own content (retrieve that part, e.g. to have a god)"],
    doc06_tags="[SC][TC][RT]",
    ag_note="none for the practice; the household mechanism is the household entry's own",
    res=(
        "reported as our own self-understanding, not assessed for historical accuracy; "
        "the catechism program sits under the same divergence as household -- formationally "
        "central and prescriptively documented to the hour, while whether any household or "
        "parish actually held it is Inferential/Thin."
    ),
),

dict(
    num="4.2", slug="household", tier=1, doc03_tier=1,
    world_word="the household -- father, wife, children, servants; the catechism's own site",
    world_word_plain="household / 'father of a family'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented as prescription -- the household program exactly as our own catechisms set "
        "it down -- and Inferential/Thin as any actual house's practice; Luther-only, "
        "cross-register, for the mechanism itself (our confession never uses the word "
        "'household' at all). This record carries Reported-Experience Status: our formation "
        "is centrally this site by our own account, while whether any household held it is not "
        "something our library answers."
    ),
    canon_cells=["F4-I", "F5-P"],
    rows=[25, 26, 31],
    row_loci={
        26: "the Small Catechism, whole file -- 'the simple way a father should present them to his household'",
        25: "the Large Catechism -- weekly examination and the day's three prayers",
        31: "the Table Talk -- 'we are very cold and careless in praying' (Contested as verbatim)",
    },
    related=["4.1", "4.8", "4.6", "6.2", "6.1", "6.4", "8.3", "9.5", "5.11", "6.5", "7.3", "7.1", "8.2"],
    tension=[],
    plain_meaning=(
        "The formation site our catechisms address: a house of father, wife, children, servants "
        "and maids, in which the father presents each part, examines everyone weekly, leads the "
        "day's three prayers, and withholds food until the parts are said."
    ),
    false_friend=[
        "'household' heard as the modern nuclear family",
        "the father's examination and food-withholding heard as domestic abuse rather than a formation duty commanded of him",
        "the program described here heard as a fact about how any actual house lived",
    ],
    senses=dict(
        informational=(
            "Every part of our little book is headed the way a father should present it -- "
            "'the simple way a father should present them to his household.' 'It is the duty of "
            "every father of a family to question and examine his children and servants at "
            "least once a week and to ascertain what they know of it'; the parts are recited "
            "morning, table and night, 'and until they repeat them, they should be given "
            "neither food nor drink.' Why the house: because through baptism we are all "
            "consecrated to the priesthood, so a father is a priest in his own house, and "
            "because the three parts must be known by 'the ordinary Christian, who cannot read "
            "the Scriptures.' The household's economy, its table, its prince, its own coldness "
            "in prayer, are each confessed there too."
        ),
        evidential="Luther-only, cross-register, for the mechanism itself -- our confession never once uses this word; the catechization practice generally is both voices.",
        personal="This is our own chosen site of formation: the place where the Word is recited, the Sacrament prepared for, the conscience examined, the prince prayed for, the devil driven off.",
        translational="Do not hear 'household' as the modern nuclear family, and do not hear the father's weekly examination as abuse: we mean a stratified house of kin and servants under one head answerable to God, prescribed as the place where every Christian is formed -- stated as a duty, unattested as any actual house's practice.",
    ),
    quick_meaning=(
        "The formation site our catechisms address -- father, wife, children, servants -- "
        "examined weekly, prayed together three times daily, the parish's own gate and seedbed."
    ),
    retrieve_when=["household, or 'father of a family'", "who examines whom, and how often",
                   "the shape of a Christian house among us"],
    do_not_retrieve_when=["the participant means the catechism's own content rather than its household setting (retrieve catechism)"],
    doc06_tags="[AS][RT][DR]",
    ag_note="Luther-only, cross-register, for the mechanism -- confirmed",
    res=(
        "reported as our own self-understanding, not assessed for historical accuracy; the "
        "household is formationally central -- our own chosen site -- while whether any "
        "household held it is Inferential/Thin. We speak the program as we set it down and "
        "keep the two axes apart."
    ),
),

dict(
    num="4.3", slug="what-does-this-mean", tier=3, doc03_tier=2, demoted=True,
    world_word="'What does this mean?' -- the catechism's own question form",
    world_word_plain="'What does this mean?'",
    distortion_risk="medium", weight="illustrative",
    formation_confidence="Documented",
    divergence_note="Documented as the catechism's own recurring form; Luther-only, single register (catechesis), a genuinely thin entry Doc_06 itself folds under the catechism proper.",
    canon_cells=["F4-I"],
    rows=[25, 26],
    row_loci={26: "the Small Catechism -- the question after every commandment, article and petition"},
    related=[], tension=[],
    plain_meaning="The question that follows every commandment, article and petition in our little book -- the form in which a child holds doctrine, staged as the father's own voice.",
    false_friend=["hearing this as a quiz to be passed rather than a father's own voice staged for a child"],
    senses=dict(
        informational="'What does this mean?' follows every part of our catechism, staged as though a father asked, 'My dear, what sort of a God have you?' -- a form, not a separate doctrine.",
        evidential="Attested only within the catechisms themselves, in one register.",
        personal="This is how a child, or 'the simple-minded,' among us is expected to hold doctrine -- by answering, not merely reciting.",
        translational="Do not hear this as a quiz; we mean a father's own voice, staged, asking a child to say what a truth means for them.",
    ),
    quick_meaning="The question following every commandment, article and petition in our little book -- doctrine held by answering, staged as a father's own voice to a child.",
    retrieve_when=["the catechism's own question-and-answer form"],
    do_not_retrieve_when=["the participant means the catechism's content broadly (retrieve catechism)"],
    doc06_tags="[SC][RT]", ag_note="Luther-only, single-register (catechesis)",
),

dict(
    num="4.4", slug="to-have-a-god-is-to-trust", tier=2, doc03_tier=1, demoted=True,
    world_word="'to have a god is to trust' -- the First Commandment's own definition",
    world_word_plain="'to have a god is to trust'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the Large Catechism's First Commandment exposition, read entire this pass (LC 521-680); Luther-only, cross-register, confirmed.",
    canon_cells=["F1-I"],
    rows=[25, 26, 31],
    row_loci={
        25: "the Large Catechism, First Commandment, now read entire -- 'a god means that from which we are to expect all good'",
        26: "the Small Catechism -- 'we must fear, love, and trust God more than anything else'",
        31: "the Table Talk -- 'as the Faith is, so is also God' (Contested as verbatim)",
    },
    related=["2.1", "4.1", "4.5", "2.10", "8.7"], tension=[],
    plain_meaning=(
        "Our catechism's own definitional move: a god is 'that from which we are to expect all "
        "good and to which we are to take refuge in all distress,' so that to have a god is "
        "nothing else than to trust -- and 'the confidence and faith of the heart alone make "
        "both God and an idol.'"
    ),
    false_friend=["'god' heard as a being whose existence is at issue, or 'idol' heard only as a carved statue"],
    senses=dict(
        informational=(
            "'A god means that from which we are to expect all good and to which we are to take "
            "refuge in all distress, so that to have a God is nothing else than to trust and "
            "believe Him from the whole heart'; 'the confidence and faith of the heart alone "
            "make both God and an idol.' Mammon, we say, is 'the most common idol on earth.' We "
            "ask: does the heart cleave to God alone, or to something else it expects more good "
            "from -- 'then you have an idol, another god.'"
        ),
        evidential="Luther-only, cross-register, confirmed -- the confession echoes the same logic once, but not this definition.",
        personal="Every commandment after the first follows from this one being kept -- where the heart trusts rightly, the rest follow.",
        translational="Do not hear 'god' as a question of existence, or 'idol' as only a statue: we mean whatever the heart cleaves to for good -- money most commonly -- so that this commandment is about trust, and everyone has some god.",
    ),
    quick_meaning="A god is 'that from which we are to expect all good' -- so that to have a god is simply to trust, and everyone trusts something.",
    retrieve_when=["what makes something a 'god' or an 'idol' for us", "Mammon"],
    do_not_retrieve_when=["the participant means faith's own definition broadly (retrieve faith)"],
    doc06_tags="[AS][DR][RT]", ag_note="Luther-only, cross-register -- confirmed",
),

dict(
    num="4.5", slug="fear-and-love-god", tier=3, doc03_tier=2, demoted=True,
    world_word="'fear and love God' -- the formula opening every commandment's explanation",
    world_word_plain="'fear and love God'",
    distortion_risk="low", weight="illustrative",
    formation_confidence="Documented",
    divergence_note="Documented as the Small Catechism's own recurring formula; a low-distortion form entry, its content belonging to the First Commandment and to faith.",
    canon_cells=["F4-I"],
    rows=[25, 26, 37],
    row_loci={26: "the Small Catechism -- 'We must fear and love God, so that...' opens every commandment"},
    related=[], tension=[],
    plain_meaning="The formula that opens every explanation of the Commandments in our household book -- anchoring each one back to the First Commandment's own content, trust.",
    false_friend=["hearing this as a pious phrase rather than the First Commandment restated ten times"],
    senses=dict(
        informational="'We must fear and love God, so that...' opens the explanation of every commandment in our Small Catechism; our confession's own 'Christian perfection is to fear God from the heart, and yet to conceive great faith' belongs to this same formula.",
        evidential="Attested throughout the Small Catechism's own repeated structure.",
        personal="Ten times over, this formula reminds us that every commandment is finally a question of what the heart trusts.",
        translational="Do not hear this as pious filler; we mean the First Commandment restated at every single commandment.",
    ),
    quick_meaning="The formula opening every commandment's explanation in our household book -- the First Commandment restated ten times.",
    retrieve_when=["'fear and love God,' the catechism's recurring formula"],
    do_not_retrieve_when=["the participant means the First Commandment's own definition (retrieve 'to have a god is to trust')"],
    doc06_tags="[SC][RT]", ag_note="none",
),

dict(
    num="4.6", slug="neighbor", tier=2, doc03_tier=2,
    world_word="the neighbor -- whom the second table protects, and the measure of liberty",
    world_word_plain="neighbor",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented for the word's household sense (Apology 2312-2318, 3067, 9908-9909, read this pass); the 1522 measure-of-liberty sense is the founder's own.",
    canon_cells=["F5-I"],
    rows=[14, 15, 25, 26, 38],
    row_loci={
        26: "the Small Catechism -- the second table's guard over 'money or property,' 'reputation,' 'wife, servant, maid, animals'",
        15: "the Eight Wittenberg Sermons -- 'we must not look upon ourselves... but upon our neighbor'",
        38: "the Apology, read this pass -- 'love towards one's neighbor'",
        14: "the Kurze Form, cited among this entry's Registry rows (Doc_06 SS5 entry 4.6)",
        25: "the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 4.6)",
    },
    related=["2.3", "7.5", "4.1", "4.2", "8.6"], tension=[],
    plain_meaning=(
        "The person the second table of the Commandments protects -- whose property, "
        "reputation, household and animals the commandments guard -- and, in 1522, the measure "
        "of what our own liberty may do."
    ),
    false_friend=["'neighbor' heard as the person next door in general, or as humanity in the abstract"],
    senses=dict(
        informational=(
            "The Commandments' second table teaches what we owe 'to other men, that is, to his "
            "neighbor'; our household catechism guards the neighbor's 'money or property,' "
            "'reputation,' 'wife, servant, maid, animals.' In the sermons the neighbor is the "
            "rule of our own pace of reform: 'we must not look upon ourselves... but upon our "
            "neighbor,' and a change made 'with offence to your neighbor' is disordered however "
            "right in itself."
        ),
        evidential="Attested in the household catechism and, for the specific 1522 sense, the founder's own sermons.",
        personal="This is the object our liberty is measured against -- the specific other whom my freedom must not destroy.",
        translational="Do not hear 'neighbor' as the person next door in general; we mean the specific other the second table names and whom our liberty must not harm.",
    ),
    quick_meaning="The person the second table protects, and the measure of what our liberty may do -- not humanity in general, but the specific other.",
    retrieve_when=["neighbor", "the second table of the Commandments", "what liberty must not do to others"],
    do_not_retrieve_when=["the participant means good works broadly (retrieve good works)"],
    doc06_tags="[SC][RT][DR]", ag_note="none for the word; the 1522 measure-of-liberty sense is the founder's own",
),

dict(
    num="4.7", slug="the-devil", tier=1, doc03_tier=1,
    world_word="the devil -- 'the old evil foe,' 'a liar and murderer,' our daily adversary",
    world_word_plain="the devil",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented at every register we use; the apocalyptic reading of our whole adversary "
        "frame is a modern reconstruction, unread and not built on here -- disclosed as a "
        "separate, weaker claim from the devil's own daily attestation."
    ),
    canon_cells=["F1-P"],
    rows=[1, 15, 25, 26, 29, 31, 37],
    row_loci={
        25: "the Large Catechism -- 'the devil is called the master of a thousand arts'",
        26: "the Small Catechism -- morning prayer 'so that the evil enemy will not gain power over me'",
        29: "the hymns, Hymn XXVI -- 'the old evil foe... one little word can fell him'",
        15: "the Eight Wittenberg Sermons -- 'here we battle not against pope or bishop, but against the devil'",
        31: "the Table Talk -- 'the devil driveth on his servants continually' (Contested as verbatim)",
        1: "the 1539 preface, cited among this entry's Registry rows (Doc_06 SS5 entry 4.7)",
        37: "the Augsburg Confession, cited among this entry's Registry rows (Doc_06 SS5 entry 4.7)",
    },
    related=["3.1", "4.1", "4.9", "9.2", "9.4", "9.5", "6.7", "6.8", "6.9", "2.9", "7.1", "7.5",
             "1.7", "5.3", "6.6"], tension=[],
    plain_meaning=(
        "A personal adversary we name in every register -- 'the master of a thousand arts,' 'a "
        "liar and murderer,' 'the old evil foe' -- against whom the Word, the sacrament and the "
        "catechism are our daily defense."
    ),
    false_friend=[
        "'the devil' heard as a metaphor or a figure of speech for evil in general",
        "the apocalyptic reading of our whole frame heard as our own self-understanding, when it is a modern reconstruction we do not build on",
    ],
    senses=dict(
        informational=(
            "'The devil is called the master of a thousand arts. But what shall we call God's "
            "Word, which drives away and brings to naught this master of a thousand arts.' He is "
            "'nothing else than what the Scriptures call him, a liar and murderer'; 'the devil "
            "never sleeps, and continually molests.' Our 1529 hymn sings him: 'the old evil foe, "
            "means us deadly woe... one little word can fell him.' We read our own troubles "
            "through him: of the 1522 disorder, 'here we battle not against pope or bishop, but "
            "against the devil.' The defense is daily and bodily -- the morning prayer 'so that "
            "the evil enemy will not gain power over me'; speaking, singing or thinking the "
            "commandments as 'the true holy water and holy sign from which he flees.'"
        ),
        evidential="Attested at every register we speak in -- sermon, catechism, hymn, table and confession -- with no register missing.",
        personal="This is the constant frame under nearly everything we do: formation, for us, is arming, and this adversary is who we arm against.",
        translational="Do not hear 'the devil' as a metaphor for evil in general, and do not assume the apocalyptic reading of our whole movement is our own self-understanding -- that reading is a modern reconstruction we do not build on. We mean a literal, daily, personal adversary named identically in every register we speak.",
    ),
    quick_meaning="A personal, daily adversary -- 'the old evil foe,' 'a liar and murderer' -- against whom the Word, the sacrament and the catechism are our constant defense.",
    retrieve_when=["the devil", "temptation as his attack", "what defends against him"],
    do_not_retrieve_when=["the participant asks for a scholarly apocalyptic reading of our movement as a whole -- we do not build on that reading"],
    doc06_tags="[SC][DR][RT]",
    ag_note="none -- both voices, every register; the apocalyptic frame is unread and not built on here",
),

dict(
    num="4.8", slug="daily", tier=2, doc03_tier=2,
    world_word="daily -- the rhythm our catechism imposes: bread, drowning, forgiveness, three prayers",
    world_word_plain="daily",
    distortion_risk="medium", weight="corroborating",
    formation_confidence="Documented",
    divergence_note="Documented as our catechism's own prescribed rhythm; Luther-only, single-register (catechesis), disclosed.",
    canon_cells=["F5-P"],
    rows=[25, 26],
    row_loci={
        26: "the Small Catechism -- daily bread as a whole household economy in one petition",
        25: "the Large Catechism -- daily forgiveness obtained in the Church",
    },
    related=["4.1", "4.2", "5.2", "9.5", "7.1", "4.9", "8.3"], tension=[],
    plain_meaning=(
        "The rhythm our catechisms impose on a life: bread asked for daily, the old Adam "
        "drowned daily, forgiveness obtained daily, the three parts said at rising, table and "
        "bed."
    ),
    false_friend=["'daily bread' heard as simply food, or 'daily' heard as a devotional habit chosen by the pious rather than a rule of the house"],
    senses=dict(
        informational=(
            "'Daily bread' is 'everything that nourishes our body and meets its needs' -- food, "
            "drink, clothing, house, cattle, a devout spouse, faithful rulers, good weather, "
            "peace -- a whole household economy, and a prince, in one petition. Baptism means "
            "the old Adam is drowned 'by daily sorrow and repentance'; in the Church 'we shall "
            "daily obtain... nothing but the forgiveness of sin.' The day itself is set: the "
            "sign of the cross at rising, folded hands at table, the mirror of the morning at "
            "night -- the three parts 'when they arise in the morning when they sit down to "
            "their meals, and when they retire at night.'"
        ),
        evidential="Luther-only, single-register (catechesis) -- disclosed rather than claimed as confessional too.",
        personal="This is the form our whole formation was meant to take: not an occasional practice but a daily rhythm, the household's own answer to the canonical hours it calls 'babbling.'",
        translational="Do not hear 'daily bread' as merely food, or 'daily' as an optional devotion: we mean a whole household economy in one petition, and a day whose three hours belong to the house by rule.",
    ),
    quick_meaning="The rhythm our catechism imposes on a life -- bread, drowning, forgiveness, and the three parts said at rising, table and bed.",
    retrieve_when=["'daily bread,' or the daily rhythm of prayer", "what shape a Christian day takes among us"],
    do_not_retrieve_when=["the participant means the Lord's Prayer's full content (retrieve prayer)"],
    doc06_tags="[SC][RT]", ag_note="Luther-only, single-register (catechesis)",
),

dict(
    num="4.9", slug="hymn", tier=1, doc03_tier=2, promoted=True,
    world_word="hymn -- German song, 'to make a good beginning,' teaching the unlearned",
    world_word_plain="hymn / German singing",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented at the hymnal prefaces and the confessional statement of purpose alike; "
        "evidential weakness disclosed, not used to hold down the tier: no hymn text beyond a "
        "few openings has been read in this build, every English line is a single translator's "
        "rendering, and no tune or parish record is in our library -- what any parish actually "
        "sang is Inferential/Thin. This record carries Reported-Experience Status for the same "
        "reason."
    ),
    canon_cells=["F5-I", "F5-P"],
    rows=[25, 26, 27, 28, 37, 38, 45, 47],
    row_loci={
        27: "the hymn texts (Bacon's composite English; tunes absent from the file)",
        28: "the four hymnal prefaces -- 'to make a good beginning and to encourage others'",
        45: "Walter's late reminiscence -- 'he kept me three weeks long at Wittenberg... until the first German Mass was sung'",
        37: "the Augsburg Confession XXIV -- German hymns 'added to teach the people'",
        38: "the Apology XV, XXIV, read this pass",
        47: "Spangenberg's preface, cited among this entry's Registry rows (Doc_06 SS5 entry 4.9)",
        25: "the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 4.9)",
        26: "the Small Catechism -- 'go about your work and perhaps sing a song'",
    },
    related=["3.1", "4.1", "4.7", "4.8", "5.6", "9.4", "6.8", "6.9", "9.6", "6.5"], tension=[],
    plain_meaning=(
        "Song in our own German, written 'to make a good beginning' and 'added to teach the "
        "people' -- the way the Word reached those who could not read, a household work-song, "
        "and old tunes carrying new words."
    ),
    false_friend=[
        "hymns heard as mere ornament or mood in a service",
        "the German hymn heard as a total break with Latin, when we kept both side by side",
        "'A Mighty Fortress' heard as a battle-anthem sung defiantly at Worms -- our own translator's footnote refuses that legend",
    ],
    senses=dict(
        informational=(
            "'To make a good beginning and to encourage others who can do it better, I have "
            "myself, with some others, put together a few hymns, in order to bring into full "
            "play the blessed Gospel' -- so that our young people might turn from carnal songs. "
            "Our confession says what the songs are for: 'the parts sung in Latin are "
            "interspersed here and there with German hymns, which have been added to teach the "
            "people,' keeping Latin 'on account of those who are learning.' In the house: 'with "
            "joy go about your work and perhaps sing a song.' The hymn carries our memory too -- "
            "at burial 'no dirges nor lamentations, but comforting songs,' old tunes kept with "
            "new words: 'the notes and melodies are of great price; it were pity to let them "
            "perish; but the words to them were unchristian and uncouth, so let these perish.'"
        ),
        evidential="Attested at the hymnal prefaces, the confession, and one late reminiscence (Walter) -- the fullest non-founder voice in our library, though evidentially thin (no tune, one witness, decades on).",
        personal="This is the register with the widest reach among our own people -- teaching set to old tunes so the unlearned may learn or pray while the learned keep their Latin.",
        translational="Do not hear our hymns as mere ornament, or the German hymn as abolishing Latin, or 'A Mighty Fortress' as a defiant anthem at Worms: we mean teaching set to memorable tunes, a household work-song, a burial comfort, and a weapon against the devil.",
    ),
    quick_meaning="Song in our own German, written to teach the unlearned and comfort the household -- old tunes carrying new words, Latin kept for those who learn it.",
    retrieve_when=["hymns, or singing in German", "what our hymns were for", "'A Mighty Fortress'"],
    do_not_retrieve_when=["the participant wants a specific hymn's full text -- our library holds only openings and fragments"],
    doc06_tags="[SC][RT][DR]",
    ag_note="none -- both voices, plus the fullest non-founder attestation in the build",
    res=(
        "reported as our own self-understanding, not assessed for historical accuracy; the "
        "hymn's formative work is central by our own account and by the register's reach, "
        "while what was actually sung, where, and to what tune is thinly attested -- one late "
        "participant, no tune, no parish record."
    ),
),

# ============================== Cluster 5 ==================================
# Word, sign, and faith -- the sacramental cluster (Doc_06 5.5)
dict(
    num="5.1", slug="sacrament", tier=1, doc03_tier=1,
    world_word="sacrament -- 'when the Word is joined to the element, it becomes a Sacrament'",
    world_word_plain="sacrament",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at both voices; the Apology XIII was read entire this pass to settle the rule of counting.",
    canon_cells=["F1-I", "F4-I"],
    rows=[3, 9, 12, 25, 37, 38],
    row_loci={
        9: "Concerning the Blessed Sacrament (1519) -- the sign, its significance, and the faith required",
        3: "Concerning Baptism (1519), cited among this entry's Registry rows (Doc_06 SS5 entry 5.1)",
        12: "Babylonian Captivity -- 'I must deny that there are seven sacraments'",
        25: "the Large Catechism -- 'accedat verbum ad elementum et fit sacramentum'",
        37: "the Augsburg Confession XIII -- sacraments 'instituted to awaken and confirm faith'",
        38: "the Apology XIII, read entire this pass -- 'Baptism, the Lord's Supper, and Absolution... are truly Sacraments'",
    },
    related=["2.1", "2.7", "3.1", "5.2", "5.3", "5.4", "5.6", "5.7", "5.8", "5.10", "5.11", "6.8", "4.1"],
    tension=[],
    plain_meaning=(
        "God's promise joined to a visible sign and received by faith -- 'when the Word is "
        "joined to the element... it becomes a Sacrament.' Two, or three counting absolution, "
        "not seven, and none of them works without faith."
    ),
    false_friend=[
        "'sacrament' heard as a ritual that works simply by being performed",
        "a sacrament heard as a mere symbol with no promise attached",
        "the number seven assumed as given, rather than a question we settled by a rule",
    ],
    senses=dict(
        informational=(
            "In 1519 a sacrament has three parts: 'the sacrament, or sign... the significance "
            "of this sacrament... the faith required by both.' In 1520 the count falls: 'I must "
            "deny that there are seven sacraments, and hold for the present to but three -- "
            "baptism, penance and the bread.' What makes one is stated in Latin and then in "
            "German: 'accedat verbum ad elementum et fit sacramentum... when the Word is joined "
            "to the element or natural substance, it becomes a Sacrament.' Our confession's "
            "rule: sacraments are 'signs and testimonies of the will of God toward us... "
            "instituted to awaken and confirm faith'; the Apology gives the rule of counting -- "
            "'rites which have the command of God and to which the promise of grace has been "
            "added' -- and so 'Baptism, the Lord's Supper, and Absolution, which is the "
            "Sacrament of Repentance, are truly Sacraments.' How a sacrament is used is by "
            "faith, and only by faith: 'faith clings to the water, and believes that it is "
            "Baptism.'"
        ),
        evidential="Attested at both voices, from the 1519 treatises through the confession and the Apology XIII, read entire this pass.",
        personal="This is the second pole of our own doctrine of promise: God's promise made visible in an element, useless to us apart from the faith that takes it.",
        translational="Do not hear 'sacrament' as a ritual that works on its own, or as a mere symbol: we mean a promise made visible -- Word plus element -- that does nothing without the faith that takes it, two or three in number by God's own command.",
    ),
    quick_meaning="God's promise joined to a visible sign and received by faith -- two, or three counting absolution, never seven, and none working without faith.",
    retrieve_when=["sacrament, in general", "how many sacraments we count, and why", "what makes something a sacrament"],
    do_not_retrieve_when=["the participant means one specific sacrament's own content (retrieve baptism, or Sacrament of the Altar, or confession/absolution)"],
    doc06_tags="[SC][TC][DR][RT]", ag_note="none -- both voices",
),

dict(
    num="5.2", slug="baptism", tier=2, doc03_tier=1, demoted=True,
    world_word="baptism -- 'die Taufe,' water within God's command, a death begun that lasts",
    world_word_plain="baptism",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the treatise's opening and the household catechism; treated by Doc_06 as its closest call in the whole tier-reassignment, since baptism is genuinely rich evidence carried mostly under the sacrament entry above.",
    canon_cells=["F4-I"],
    rows=[3, 11, 15, 25, 26, 37],
    row_loci={
        3: "Concerning Baptism (1519), opening only -- 'the life of a Christian, from baptism to the grave, is nothing else than the beginning of a blessed death'",
        26: "the Small Catechism -- the old Adam drowned daily",
        25: "the Large Catechism, opening only -- 'faith clings to the water, and believes that it is Baptism'",
        11: "Christian Nobility -- 'through baptism all of us are consecrated to the priesthood'",
        37: "the Augsburg Confession, cited among this entry's Registry rows (Doc_06 SS5 entry 5.2)",
        15: "the Eight Wittenberg Sermons -- baptism among the 'many absolutions'",
    },
    related=["5.1", "1.2", "4.8", "6.2", "8.1", "6.8", "9.4", "5.10", "1.7", "2.10"], tension=[],
    plain_meaning=(
        "Water 'contained within God's command and united with God's Word' -- a sign whose "
        "meaning, the old Adam drowned daily, 'lasts so long as we live,' and the ground on "
        "which all of us are priests."
    ),
    false_friend=["baptism heard as a one-time naming rite or a personal decision made once"],
    senses=dict(
        informational=(
            "'The life of a Christian, from baptism to the grave, is nothing else than the "
            "beginning of a blessed death'; the old Adam 'should be drowned by daily sorrow and "
            "repentance... and a new person daily come forth.' It is not plain water: 'here "
            "stand God's commandment and institution, lest we doubt that Baptism is divine'; "
            "'faith clings to the water, and believes that it is Baptism.' It consecrates: "
            "'through baptism all of us are consecrated to the priesthood.' And it comforts, "
            "counted among our 'many absolutions.'"
        ),
        evidential="Attested at the founder's own baptism treatise and both catechisms.",
        personal="This is a death begun once and repeated every morning -- the ground of every one of us being a priest, and a comfort we reach for even on our deathbed.",
        translational="Do not hear baptism as a one-time naming rite: we mean a death begun that is repeated every morning, the ground of every Christian's priesthood, and a comfort for the deathbed.",
    ),
    quick_meaning="Water within God's own command and Word -- a death begun that lasts our whole life, and the ground of every Christian's priesthood.",
    retrieve_when=["baptism, or 'die Taufe'", "what baptism means for daily life, not only at the font"],
    do_not_retrieve_when=["the participant means the sacrament's general definition (retrieve sacrament)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none",
),

dict(
    num="5.3", slug="sacrament-of-the-altar", tier=1, doc03_tier=1,
    world_word="the Sacrament of the Altar -- Christ's body and blood 'in and under' bread and wine",
    world_word_plain="the Sacrament of the Altar / Lord's Supper",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented for the doctrine itself, at every register; the organizing weight of the "
        "bodily presence as our own boundary against the Reformed churches is real (Doc_01 SS7) "
        "but is not shown by our own library's evidence and is left untagged rather than "
        "claimed -- the Marburg controversy itself is not in our library beyond one word, and "
        "this entry states the doctrine as our catechism states it, without narrating the "
        "Colloquy."
    ),
    canon_cells=["C-I", "F4-I"],
    rows=[9, 12, 25, 26, 37, 38],
    row_loci={
        26: "the Small Catechism -- 'the true body and blood of our Lord Jesus Christ under bread and wine'",
        25: "the Large Catechism, entire -- 'in and under the bread and wine'; the examination gate and its freedom",
        37: "the Augsburg Confession X, XXIV -- 'the Body and Blood of Christ are truly present'",
        9: "Concerning the Blessed Sacrament (1519) -- 'synaxis or communio, that is, fellowship'",
        12: "Babylonian Captivity -- the sacrament as Christ's testament",
        38: "the Apology XXIV, cited among this entry's Registry rows (Doc_06 SS5 entry 5.3)",
    },
    related=["2.7", "5.1", "5.4", "5.5", "5.6", "5.7", "5.8", "5.11", "6.8", "7.5", "4.7", "9.1",
             "5.10", "5.9"], tension=[],
    plain_meaning=(
        "'The true body and blood of our Lord Jesus Christ, in and under the bread and wine,' "
        "given 'for you' -- Christ's testament received by faith, a food for the daily battle, "
        "to which none are admitted unexamined and none are compelled."
    ),
    false_friend=[
        "the Supper heard as a memorial meal only",
        "the presence heard as a metaphysical theory ('consubstantiation') -- a word we do not use",
        "the doctrine heard as a boundary-marker whose whole point is who is excluded",
    ],
    senses=dict(
        informational=(
            "'The true body and blood of our Lord Jesus Christ under bread and wine'; the "
            "larger book says 'in and under the bread and wine which we Christians are "
            "commanded by the Word of Christ to eat and to drink.' We do not dispute the how: "
            "'I rejoice greatly that the simple faith of this sacrament is still to be found at "
            "least among the common people; for as they do not understand, neither do they "
            "dispute'; 'I will take my reason captive to the obedience of Christ.' Its benefit "
            "is the words: 'put yourself into this YOU, that He may not speak to you in vain.' "
            "It is food for a fight: 'a food of souls, which nourishes and strengthens the new "
            "man,' 'a daily pasture and sustenance.' Its gate and its freedom are stated "
            "together: 'none are admitted except they be first examined,' yet 'no one should by "
            "any means be coerced or compelled, lest we institute a new murdering of souls.'"
        ),
        evidential="Attested at both catechisms, the confession, and the founder's own sacramental treatises, entire in the Large Catechism.",
        personal="Christ's body and blood are truly there for us, taken on his word without an explanation of the how -- a testament received, not a work offered, food for the daily battle.",
        translational="Do not hear the Supper as a memorial meal, or its presence-doctrine as a rival theory to be argued, or the whole matter as chiefly about who is excluded: we mean Christ's body and blood truly there, 'in and under,' a testament received on his word, with an examined gate and no compulsion at the door.",
    ),
    quick_meaning="'The true body and blood of our Lord Jesus Christ, in and under the bread and wine' -- Christ's testament received by faith, food for the daily battle.",
    retrieve_when=["the Sacrament of the Altar, the Lord's Supper, or 'the bread'", "'in and under'",
                   "who may or may not come to the table"],
    do_not_retrieve_when=["the participant wants our own account of the Marburg Colloquy or the Reformed controversy -- our library does not narrate it"],
    doc06_tags="[AS][TC][DR][RT]", ag_note="none -- both voices",
),

dict(
    num="5.4", slug="given-for-you", tier=2, doc03_tier=1, demoted=True,
    world_word="'given for you' -- the sacrament's whole benefit in two words",
    world_word_plain="'given for you'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented as quotation of the institution (Apology 5159-5162, read this pass); the 'put yourself into this YOU' development is the founder's own.",
    canon_cells=["F1-P"],
    rows=[12, 25, 26, 38],
    row_loci={
        26: "the Small Catechism -- 'the words, \"for you\" demand a heart that fully believes'",
        25: "the Large Catechism -- 'put yourself into this YOU, that He may not speak to you in vain'",
        38: "the Apology, read this pass -- 'the words of the Lord's Supper clearly testify... this is My body, which is given for you'",
        12: "Babylonian Captivity, cited among this entry's Registry rows (Doc_06 SS5 entry 5.4)",
    },
    related=["5.3", "2.7", "2.1", "5.11", "5.1"], tension=[],
    plain_meaning=(
        "The two words in the institution that our catechisms make the sacrament's whole "
        "benefit: 'the words, \"for you\" demand a heart that fully believes.'"
    ),
    false_friend=["'for you' heard as a bare liturgical formula rather than an address demanding belief"],
    senses=dict(
        informational=(
            "'Given for you' and 'shed for you to forgive sins' -- 'anyone who believes these "
            "words has what they say.' 'These words... are not preached to wood and stone, but "
            "to me and you... put yourself into this YOU, that He may not speak to you in vain.' "
            "In the testament argument, the 'you' is the heir who accepts and believes the "
            "promise."
        ),
        evidential="Attested as quotation of the institution words in the Apology, and developed at length in the Large Catechism.",
        personal="This is the moment the promise becomes mine, personally -- the whole benefit of the sacrament collapsed into two words.",
        translational="Do not hear 'for you' as a liturgical formula; we mean the moment the promise becomes yours, demanding a heart that believes it.",
    ),
    quick_meaning="The two words that carry the sacrament's whole benefit for us: 'the words, \"for you\" demand a heart that fully believes.'",
    retrieve_when=["'given for you,' or 'for you' as address"],
    do_not_retrieve_when=["the participant means the Supper's whole doctrine (retrieve Sacrament of the Altar)"],
    doc06_tags="[SC][RT][DR]", ag_note="none as quotation of the institution; the 'put yourself into this YOU' development is the founder's own",
),

dict(
    num="5.5", slug="both-kinds", tier=2, doc03_tier=2,
    world_word="both kinds -- bread and cup for the laity, 'the commandment of the Lord'",
    world_word_plain="both kinds / the cup",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented across three periods (1519, 1522, 1530), each a different pace on the same doctrine.",
    canon_cells=["F4-I"],
    rows=[9, 12, 15, 37],
    row_loci={
        12: "Babylonian Captivity -- 'drink ye all of it' as 'not by way of permission but of command'",
        15: "the Eight Wittenberg Sermons -- the cup 'necessary... nevertheless it must not be made compulsory'",
        37: "the Augsburg Confession -- both kinds as 'the commandment of the Lord'",
        9: "Concerning the Blessed Sacrament, cited among this entry's Registry rows (Doc_06 SS5 entry 5.5)",
    },
    related=["5.3", "7.5", "5.6", "6.8", "8.8"], tension=[],
    plain_meaning=(
        "Bread and cup together for the laity -- in 1520 the sacrament's 'first captivity,' in "
        "1522 necessary yet 'not... made compulsory,' in 1530 'the commandment of the Lord.'"
    ),
    false_friend=["hearing this as a minor liturgical detail rather than a test case for how a right thing must be done"],
    senses=dict(
        informational=(
            "'Drink ye all of it' is, we say, 'not by way of permission but of command,' and "
            "withholding the cup was the sacrament's first captivity. In 1522 the cup is "
            "'necessary... nevertheless it must not be made compulsory nor a general law' -- "
            "our own congregation had forced into a law what should have waited on the Word. By "
            "1530 it is simply 'the commandment of the Lord.'"
        ),
        evidential="Attested across three distinct periods of our own history -- 1519, 1522, 1530.",
        personal="This became our own test case for how a right thing must be done -- by the Word, not by a law forced ahead of it.",
        translational="Do not hear this as a minor liturgical detail; we mean Christ's own command to the laity, and the test of whether even a right change may be compelled.",
    ),
    quick_meaning="Bread and cup together for the laity -- necessary as Christ's command, but never, we insisted, a law forced by compulsion.",
    retrieve_when=["both kinds, or the cup for the laity"],
    do_not_retrieve_when=["the participant means the Supper's whole doctrine broadly (retrieve Sacrament of the Altar)"],
    doc06_tags="[SC][TC][RT]", ag_note="none",
),

dict(
    num="5.6", slug="the-mass", tier=2, doc03_tier=1, demoted=True,
    world_word="the mass -- kept as testament, refused as sacrifice, its public form re-founded",
    world_word_plain="the mass",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented across three periods inside one voice and between two voices -- 1520's "
        "abolition-logic, 1522's 'I let it live,' and 1530's 'retained... with the highest "
        "reverence' -- a real, demonstrated plurality across time this entry states rather than "
        "flattens, carried at full Tier 2 depth with the [PV] marker per Doc_06's own reading."
    ),
    canon_cells=["F1-I"],
    rows=[7, 12, 15, 28, 37, 38],
    row_loci={
        12: "Babylonian Captivity -- the mass as 'the promise of remission of sins made to us by God,' against its 'third captivity' as sacrifice",
        15: "the Eight Wittenberg Sermons -- 'the private mass must be abolished... I heartily wish it would be abolished everywhere'",
        37: "the Augsburg Confession -- 'the Mass is retained among us, and celebrated with the highest reverence'",
        38: "the Apology XXIV, read across three passes this build -- the division between sacrament and sacrifice",
        7: "the New Testament preface, cited among this entry's Registry rows (Doc_06 SS5 entry 5.6)",
        28: "the hymnal material, cited among this entry's Registry rows (Doc_06 SS5 entry 5.6)",
    },
    related=["5.3", "2.7", "1.4", "4.9", "5.11", "7.5", "7.1", "5.5", "5.1"], tension=[],
    plain_meaning=(
        "The word we keep and re-found: the mass as God's promise of forgiveness, not a "
        "sacrifice or a 'good work' we offer to God. We abolished the private mass and kept the "
        "'evangelical mass for all the people,' with German hymns and an examined congregation."
    ),
    false_friend=[
        "assuming we abolished the mass outright, or that 'mass' is the wrong word for what we kept",
        "assuming our 1520 and 1530 statements must contradict each other, rather than tracking one doctrine across changing public form",
    ],
    senses=dict(
        informational=(
            "'What we call the mass is the promise of remission of sins made to us by God'; its "
            "'third captivity' was the opinion 'that the mass is a good work and a sacrifice.' "
            "In 1522 we hold the same doctrine at a different pace: 'the mass is an evil thing... "
            "because it is performed as a sacrifice and work of merit. Therefore it must be "
            "abolished... the private mass must be abolished... and I heartily wish it would be "
            "abolished everywhere and only the evangelical mass for all the people be retained' "
            "-- but 'the Word must do this thing, and not we poor sinners,' so 'I let it live in "
            "God's name.' By 1530: 'the Mass is retained among us, and celebrated with the "
            "highest reverence. Nearly all the usual ceremonies are also preserved'; 'private "
            "Masses were discontinued.' The Apology draws the argument's own division: a "
            "sacrament is what God gives us; a sacrifice is what we render God -- 'there has "
            "been only one propitiatory sacrifice in the world, namely, the death of Christ.'"
        ),
        evidential="Attested across three periods and, where the pace differs, both voices -- the doctrine unchanged, its public form documented as changing.",
        personal="This word carries our own history of restraint: refusing to force a right reform ahead of the Word, even against our own impatience.",
        translational="Do not assume we abolished the mass, or that our earlier and later statements contradict each other: we mean the mass kept as a testament and refused as a sacrifice, its private form abolished and its public form retained 'with the highest reverence' -- one doctrine, a documented change of public form.",
    ),
    quick_meaning="The mass kept as God's promise, refused as a sacrifice -- private masses abolished, the public, evangelical mass retained with German hymns.",
    retrieve_when=["the mass", "whether we abolished the mass", "sacrifice versus sacrament"],
    do_not_retrieve_when=["the participant means the Supper's doctrine of presence specifically (retrieve Sacrament of the Altar)"],
    doc06_tags="[SC][DR][TC][RT][PV]", ag_note="none; the Apology XXIV's sacrifice argument read this pass",
),

dict(
    num="5.7", slug="transubstantiation", tier=3, doc03_tier=3,
    world_word="transubstantiation -- 'a monstrous word,' refused without theorizing an alternative",
    world_word_plain="transubstantiation",
    distortion_risk="medium", weight="illustrative",
    formation_confidence="Documented",
    divergence_note="Documented at a single work, single register (Babylonian Captivity) -- the weakest evidentiary base among our sacramental entries, disclosed rather than smoothed.",
    canon_cells=["F1-I"],
    rows=[12],
    row_loci={12: "Babylonian Captivity -- 'a monstrous word for a monstrous idea'"},
    related=[], tension=[],
    plain_meaning="The scholastic account of the presence, refused by us as 'a monstrous word for a monstrous idea' -- while we permit others to hold it, 'only let them not press us to accept their opinions as articles of faith.'",
    false_friend=["assuming our own presence-doctrine is a rival theory of the same kind, rather than a refusal to theorize the how at all"],
    senses=dict(
        informational="We call it 'a monstrous word for a monstrous idea,' and hold instead 'the simple faith... that Christ's body and blood are truly contained in whatever is there.'",
        evidential="A single work, single register -- the weakest evidentiary base of any term in our lexicon.",
        personal="We tolerate this as another's opinion; we do not press our own account of the how as its replacement.",
        translational="Do not hear our own presence-doctrine as a rival theory to transubstantiation; we refuse to theorize the how at all.",
    ),
    quick_meaning="'A monstrous word for a monstrous idea' -- refused, while we tolerate others holding it and refuse to theorize an alternative of our own.",
    retrieve_when=["transubstantiation specifically"],
    do_not_retrieve_when=["the participant means the presence doctrine generally (retrieve Sacrament of the Altar)"],
    doc06_tags="[SC][TC]", ag_note="Luther-only, single-register (Babylonian Captivity)",
),

dict(
    num="5.8", slug="congregation", tier=1, doc03_tier=1,
    world_word="fellowship / congregation -- Gemeinde, not 'Church' as building or institution",
    world_word_plain="fellowship / congregation of saints",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at both voices; the German glosses (Gemeinde, Christenheit) are the founder's own, given in the text itself, not an editor's layer.",
    canon_cells=["F4-I", "F5-I"],
    rows=[8, 9, 10, 12, 25, 37, 87],
    row_loci={
        9: "Concerning the Blessed Sacrament -- 'the fellowship of all saints, whence it derives its common name synaxis or communio'",
        25: "the Large Catechism, Creed Third Article -- 'eine christliche Gemeinde oder Sammlung... holy Christendom'",
        37: "the Augsburg Confession VII -- 'the congregation of saints, in which the Gospel is rightly taught and the Sacraments are rightly administered'",
        10: "Concerning the Ban -- excommunication as exclusion from this fellowship",
        8: "Papacy at Rome footnotes, cited among this entry's Registry rows (Doc_06 SS5 entry 5.8)",
        12: "Babylonian Captivity, cited among this entry's Registry rows (Doc_06 SS5 entry 5.8)",
        87: "the translators' own glossing footnotes on Gemeinde and Kirche (layer)",
    },
    related=["5.1", "5.3", "5.9", "5.11", "6.6", "6.5", "6.3", "6.7", "3.1", "3.2", "8.7"], tension=[],
    plain_meaning=(
        "What the sacrament signifies and what the Creed names -- not 'church' as building or "
        "institution, but an assembly, a community, a Gemeinde: 'the congregation of saints, in "
        "which the Gospel is rightly taught and the Sacraments are rightly administered.'"
    ),
    false_friend=[
        "'church' heard as a building, a denomination, or an institution with officers",
        "'communion' heard as a private act rather than a shared belonging",
    ],
    senses=dict(
        informational=(
            "The sacrament's significance 'is the fellowship of all saints, whence it derives "
            "its common name synaxis or communio' -- pictured as a city sharing 'the name, "
            "honor, freedom, trade,' and 'all the danger of fire and flood.' The Creed's article "
            "is glossed in our own German inside the text: ecclesia 'properly means in German "
            "eine Versammlung, an assembly'; the article means 'eine christliche Gemeinde oder "
            "Sammlung... or, best of all and most clearly, holy Christendom.' This body 'is the "
            "mother that begets and bears every Christian through the Word of God.' Our "
            "confession defines it by its marks: 'the congregation of saints, in which the "
            "Gospel is rightly taught and the Sacraments are rightly administered' -- located "
            "where those marks are, not by hierarchy."
        ),
        evidential="Attested at both voices, with the German glosses given by the founder himself, in the text.",
        personal="We define ourselves by marks -- Word and sacrament rightly held -- not by building or office; membership is knowing the three parts and coming to the table.",
        translational="Do not hear 'church' as a building or institution, or 'communion' as a private act: we mean an assembly of people under Christ, known by Word and sacrament, entered by knowing three parts, kept by coming to the table together.",
    ),
    quick_meaning="An assembly, not a building -- 'the congregation of saints, in which the Gospel is rightly taught,' the mother that bears every Christian through the Word.",
    retrieve_when=["church, congregation, fellowship, or Gemeinde", "what makes us the Church, and where it is found"],
    do_not_retrieve_when=["the participant means Christendom's wider, inclusive extent specifically (retrieve Christendom)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none -- both voices; the German glosses are the founder's own, in the text",
),

dict(
    num="5.9", slug="the-ban", tier=2, doc03_tier=2,
    world_word="the ban -- exclusion from the visible fellowship only, for correction, without force",
    world_word_plain="the ban / excommunication",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the founder's own treatise on the ban and the confession's own condemnation of 'ruthless excommunications.'",
    canon_cells=["F3-I"],
    rows=[10, 15, 37],
    row_loci={
        10: "Concerning the Ban -- 'exclusion from this fellowship,' the lesser and greater ban",
        15: "the Eight Wittenberg Sermons -- 'exclude him and put him under the ban before the whole assembly'",
        37: "the Augsburg Confession -- condemning 'ruthless excommunications'; the power kept 'without human force, simply by the Word'",
    },
    related=["5.8", "7.2", "6.5", "5.3"], tension=[],
    plain_meaning=(
        "Exclusion from the outward fellowship of the sacrament only -- never from the inner "
        "fellowship 'which no ban can touch' -- used for correction, stopping short of death, "
        "by the Word alone."
    ),
    false_friend=["excommunication heard as damnation, or as a political weapon"],
    senses=dict(
        informational=(
            "The ban is 'exclusion from this fellowship' -- the visible one; the inner, "
            "spiritual fellowship is one 'no ban can touch.' There is a lesser and a greater "
            "ban; the spiritual estate's 'sword is not to be of iron, but the sword of the "
            "Spirit.' In 1522 the pastor is to 'exclude him and put him under the ban before the "
            "whole assembly... for the sake of the congregation, until he comes to himself and "
            "is received back again.' Our confession condemns 'ruthless excommunications' and "
            "keeps the power 'without human force, simply by the Word.'"
        ),
        evidential="Attested at the founder's own treatise and the confession's condemnation of its abuse.",
        personal="This fences only the visible table, for correction and restoration, never for death and never by force.",
        translational="Do not hear excommunication as damnation or a political weapon; we mean a fence around the visible table only, for correction, without force -- and a practice our founder himself said was no longer being kept.",
    ),
    quick_meaning="Exclusion from the visible table only, for correction, without force -- never from the inner fellowship, and stopping short of death.",
    retrieve_when=["the ban, or excommunication"],
    do_not_retrieve_when=["the participant means the temporal sword's own power (retrieve the sword)"],
    doc06_tags="[SC][TC][DR]", ag_note="none",
),

dict(
    num="5.10", slug="confession-and-absolution", tier=2, doc03_tier=1, demoted=True,
    world_word="confession and absolution -- two parts, kept as a treasure, never compelled",
    world_word_plain="confession / absolution",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the household catechism, the founder's own personal testimony, and the confession before the Emperor alike.",
    canon_cells=["F1-P"],
    rows=[4, 15, 26, 37, 38],
    row_loci={
        26: "the Small Catechism -- confession's two parts: admitting sin, receiving absolution",
        15: "the Eight Wittenberg Sermons -- 'I will let no man take private confession away from me'",
        37: "the Augsburg Confession -- 'Private Absolution ought to be retained'",
        38: "the Apology, read this pass -- 'if the power of the keys does not console us before God, what, then, will pacify the conscience?'",
        4: "Discussion of Confession, opening only, cited among this entry's Registry rows (Doc_06 SS5 entry 5.10)",
    },
    related=["1.2", "1.6", "2.8", "5.1", "5.2", "5.3", "5.11", "9.1", "6.5", "2.7"], tension=[],
    plain_meaning=(
        "Two parts -- admitting one's sin, and receiving forgiveness 'from the confessor, as if "
        "from God Himself' -- kept as a treasure ('I will let no man take private confession "
        "away from me'), never compelled, never a catalogue of every sin."
    ),
    false_friend=["assuming we abolished confession, or that 'absolution' is a word belonging only to the papacy"],
    senses=dict(
        informational=(
            "'Confession has two parts: first, a person admits his sin; second, a person "
            "receives absolution or forgiveness from the confessor, as if from God Himself, "
            "without doubting it.' We refuse compulsion -- 'I refuse to go to confession just "
            "because the pope wishes it' -- and refuse to give it up: 'I will let no man take "
            "private confession away from me, and I would not give it up for all the treasures "
            "in the world... the devil would have slain me long ago, if the confession had not "
            "sustained me.' 'We must have many absolutions, so that we may strengthen our timid "
            "consciences and despairing hearts.' Before the Emperor: 'Private Absolution ought "
            "to be retained,' enumeration of sins 'not necessary.'"
        ),
        evidential="Attested at both catechisms, the founder's own personal testimony, and the confession before the Emperor.",
        personal="This is one of the most-loved of our 'many absolutions' -- kept freely, not because compelled, and precious enough that our own founder credits it with sustaining him against the devil.",
        translational="Do not assume we abolished confession or that 'absolution' belongs only to the papacy: we mean private confession kept as a comfort, freed from compulsion and enumeration, heard 'as if from God Himself.'",
    ),
    quick_meaning="Two parts -- admitting sin, receiving forgiveness 'as if from God Himself' -- kept as a comfort we would not give up, never compelled.",
    retrieve_when=["confession, or absolution", "whether we kept or abolished confession"],
    do_not_retrieve_when=["the participant means the keys' own broader authority (retrieve the keys)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none",
),

dict(
    num="5.11", slug="worthy-unworthy", tier=2, doc03_tier=2,
    world_word="worthy / unworthy -- believing the words 'given for you,' examined on the three parts",
    world_word_plain="worthy / unworthy",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at both catechisms and the confession's own gate before the Emperor.",
    canon_cells=["F4-P"],
    rows=[25, 26, 37, 38],
    row_loci={
        26: "the Small Catechism -- 'anyone who believes these words, \"given for you\"... is really worthy and well prepared'",
        25: "the Large Catechism -- 'those alone are called unworthy who neither feel their infirmities nor wish to be considered sinners'",
        37: "the Augsburg Confession -- 'none are admitted except they be first examined'",
        38: "the Apology, cited among this entry's Registry rows (Doc_06 SS5 entry 5.11)",
    },
    related=["5.3", "5.4", "4.1", "5.10", "2.8", "2.1", "5.8", "4.2", "5.1", "5.6", "8.6"], tension=[],
    plain_meaning=(
        "Worthiness redefined as believing the words 'given for you,' so that the unworthy are "
        "only 'those who neither feel their infirmities nor wish to be considered sinners' -- "
        "and the practice that 'none are admitted except they be first examined.'"
    ),
    false_friend=["worthiness heard as moral fitness, or examination heard as a test of purity"],
    senses=dict(
        informational=(
            "'Anyone who believes these words, \"given for you\"... is really worthy and well "
            "prepared'; 'I come, not upon any worthiness, but upon Thy Word.' The old scruple is "
            "named and refused: 'the old way under the Pope, in which a person tortured himself "
            "to be so perfectly pure that God could not find the least blemish in us... one week "
            "trails another.' 'Those alone are called unworthy who neither feel their "
            "infirmities nor wish to be considered sinners.' The gate is kept -- 'none are "
            "admitted except they be first examined' -- yet 'no one should by any means be "
            "coerced or compelled.'"
        ),
        evidential="Attested at both catechisms and the confession's own statement of practice before the Emperor.",
        personal="This closes the household's weekly examination and the parish's own gate into one thing: what the three parts teach us to believe, tested before the table.",
        translational="Do not hear worthiness as moral fitness or examination as a purity test: we mean worthiness as believing the words, and examination as the three parts -- the unworthy are only those untroubled by their own sin.",
    ),
    quick_meaning="Worthiness is believing the words 'given for you'; examination is of the three parts -- the unworthy are the untroubled, not the imperfect.",
    retrieve_when=["worthiness, or examination before the Sacrament"],
    do_not_retrieve_when=["the participant means the household's own weekly examination generally, apart from the Sacrament (retrieve household)"],
    doc06_tags="[SC][DR][RT]", ag_note="none",
),

# ============================== Cluster 6 ==================================
# Priest, office, estate, calling -- the priesthood-of-all-believers cluster (Doc_06 5.6)
dict(
    num="6.1", slug="spiritual-and-temporal-estate", tier=2, doc03_tier=1, demoted=True,
    world_word="spiritual and temporal estate -- 'pure invention' refused, the word kept for marriage and rule",
    world_word_plain="spiritual estate / temporal estate",
    distortion_risk="high", weight="corroborating",
    formation_confidence="Documented",
    divergence_note="Documented at the founder's own treatise; Luther-only, cross-register, for the spiritual/temporal pairing itself -- confirmed, our confession's own words are 'states' and 'estates of life,' not this exact pairing.",
    canon_cells=["F3-I"],
    rows=[10, 11, 14, 19, 24, 25, 38],
    row_loci={
        11: "Christian Nobility -- 'it is pure invention that pope, bishops, priests and monks are to be called the spiritual estate'",
        25: "the Large Catechism -- marriage as 'the most common and noblest estate'",
        38: "the Apology, read this pass -- 'states of perfection, i.e., holier and higher states than the rest, such as marriage, rulership'",
        10: "Concerning the Ban, cited among this entry's Registry rows (Doc_06 SS5 entry 6.1)",
        14: "the Kurze Form, cited among this entry's Registry rows (Doc_06 SS5 entry 6.1)",
        19: "Earnest Exhortation, cited among this entry's Registry rows (Doc_06 SS5 entry 6.1)",
        24: "To the Knights of the Teutonic Order, cited among this entry's Registry rows (Doc_06 SS5 entry 6.1)",
    },
    related=["6.2", "6.3", "6.4", "8.3", "8.4", "7.1", "4.2"], tension=[],
    plain_meaning=(
        "The division of Christians into a 'spiritual' estate (pope, bishops, priests, monks) "
        "and a 'temporal' one -- called 'pure invention' by us, then kept as a word for every "
        "holy station: marriage 'the most common and noblest estate,' fatherhood and motherhood "
        "an estate too."
    ),
    false_friend=["'estate' heard as property, or 'spiritual' heard as inward or pious"],
    senses=dict(
        informational=(
            "'It is pure invention that pope, bishops, priests and monks are to be called the "
            "spiritual estate... all Christians are truly of the spiritual estate, and there is "
            "among them no difference at all but that of office.' The temporal power too 'has "
            "become a member of the body of Christendom, and is of the spiritual estate, though "
            "its work is of a temporal nature.' Then we reuse the word for what remains: "
            "marriage is 'not a peculiar estate, but the most common and noblest estate, which "
            "pervades all Christendom.' Our confession's own words are 'states of perfection... "
            "such as marriage, rulership' -- the refused claim, in the confessional voice's own "
            "phrasing."
        ),
        evidential="Luther-only, cross-register, for this exact pairing; the confession's own vocabulary differs slightly ('states,' 'estates of life').",
        personal="A station, not a rank -- and the refusal that clergy hold a higher one, with the word kept for marriage, parenthood, rule and trade as equally holy stations.",
        translational="Do not hear 'estate' as property, or 'spiritual' as inward piety: we mean a station -- and the refusal that clergy are a higher one, with marriage, parenthood, rule and trade named as holy stations of equal standing.",
    ),
    quick_meaning="Not clergy over laity, but a station -- 'no difference at all but that of office' -- with the word kept for marriage, parenthood and rule as holy stations too.",
    retrieve_when=["spiritual estate, or temporal estate", "whether clergy hold a higher station than others"],
    do_not_retrieve_when=["the participant means the priesthood-of-all-believers claim itself (retrieve we-are-all-priests)"],
    doc06_tags="[AS][DR][TC][RT]", ag_note="Luther-only, cross-register, for the pairing -- confirmed",
),

dict(
    num="6.2", slug="we-are-all-priests", tier=1, doc03_tier=1,
    world_word="'we are all priests' -- consecrated in baptism, no estate difference, only office",
    world_word_plain="'we are all priests'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented, weighted to Luther for the formula itself, with the Apology's own sacrifice argument (8712-8724, read this pass) attesting the same substance from the confessional voice.",
    canon_cells=["F3-I", "F4-P"],
    rows=[11, 12, 30, 37, 38],
    row_loci={
        11: "Christian Nobility, opening only -- 'through baptism all of us are consecrated to the priesthood'",
        38: "the Apology XIII, XXIV, read this pass -- 'an holy priesthood, to offer up spiritual sacrifices'",
        37: "the Augsburg Confession XIV -- 'no one should publicly teach in the Church... unless he be regularly called'",
        30: "the hymns, Hymn V -- 'true priests of God's own making'",
        12: "Babylonian Captivity, cited among this entry's Registry rows (Doc_06 SS5 entry 6.2)",
    },
    related=["6.1", "6.3", "6.4", "6.5", "5.2", "4.2", "3.3", "1.6", "9.6", "7.1", "8.3"], tension=[],
    plain_meaning=(
        "Through baptism every one of us is consecrated a priest -- so that there is 'no "
        "difference at all but that of office.' A father is a priest in his house, a prince a "
        "priest in his own; but no one may exercise the public office unless called."
    ),
    false_friend=[
        "'the priesthood of all believers' heard as a slogan for religious individualism or lay preaching without any call",
        "the phrase heard as merely a spiritual dignity with no practical consequence",
    ],
    senses=dict(
        informational=(
            "'Through baptism all of us are consecrated to the priesthood'; 'whoever comes out "
            "of the water of baptism can boast that he is already consecrated priest, bishop "
            "and pope, though it is not seemly that every one should exercise the office.' 'If "
            "we are all priests... why should we not also have the power to test and judge what "
            "is correct or incorrect in matters of faith?' What remains among priests is office, "
            "not rank: 'a priest in Christendom is nothing else than an office-holder... when "
            "deposed, he is a peasant or a townsman like the rest.' The father is a priest in "
            "his house; the temporal rulers 'are priests and bishops.' But the public office has "
            "a fence, in our own voice: 'no one must put himself forward... without our consent "
            "and election'; 'no one should publicly teach in the Church or administer the "
            "Sacraments unless he be regularly called.'"
        ),
        evidential="Weighted to Luther for the exact formula 'we are all priests'; the Apology attests the same substance in its own sacrifice argument.",
        personal="This is the claim from which every station of office, calling and estate draws for us -- one priesthood, exercised where we stand, fenced only at the public pulpit.",
        translational="Do not hear this as a slogan for individualism or lay preaching without a call: we mean a consecration given to every Christian in baptism, exercised in one's own house and station, with the public office reserved to those regularly called -- one priesthood, many offices, no higher estate.",
    ),
    quick_meaning="Every Christian consecrated a priest in baptism -- 'no difference at all but that of office' -- exercised at home, fenced only at the public pulpit.",
    retrieve_when=["'we are all priests,' or the priesthood of all believers", "who may preach or administer the sacraments publicly"],
    do_not_retrieve_when=["the participant means the office's own definition apart from this claim (retrieve office)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none, weighted to Luther for the formula",
),

dict(
    num="6.3", slug="office", tier=2, doc03_tier=1, demoted=True,
    world_word="office -- the only difference among us; 'when deposed, a peasant like the rest'",
    world_word_plain="office / office-holder",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the founder's own argument against the indelible character, and the confession's own use for the two powers.",
    canon_cells=["F3-I"],
    rows=[11, 12, 25, 37],
    row_loci={
        11: "Christian Nobility -- 'a priest in Christendom is nothing else than an office-holder'",
        37: "the Augsburg Confession -- the sword as 'another office than the ministry of the Gospel'",
        25: "the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 6.3)",
        12: "Babylonian Captivity, cited among this entry's Registry rows (Doc_06 SS5 entry 6.3)",
    },
    related=["6.2", "6.1", "6.4", "6.5", "7.2", "3.1", "2.3", "5.8"], tension=[],
    plain_meaning=(
        "The only difference among Christians: a priest is 'nothing else than an office-holder,' "
        "who 'when deposed... is a peasant or a townsman like the rest' -- and every trade has "
        "its own office too."
    ),
    false_friend=["'office' heard as a position of rank or a physical room"],
    senses=dict(
        informational=(
            "'There is among them no difference at all but that of office.' 'A priest in "
            "Christendom is nothing else than an office-holder. While he is in office, he has "
            "precedence... when deposed, he is a peasant or a townsman like the rest' -- against "
            "the claim of an indelible clerical character. 'A cobbler, a smith, a farmer, each "
            "has the work and office of his trade.' Even God's Spirit, we say, has 'His office.'"
        ),
        evidential="Attested at the founder's own argument and the confession's continued use of the word for the two governments' distinct powers.",
        personal="This word refuses any permanent clerical rank: a function held for a time, held by pastor, cobbler and prince alike.",
        translational="Do not hear 'office' as rank or a physical position: we mean a function held for a time, by which alone Christians differ -- never an indelible character.",
    ),
    quick_meaning="A function held for a time, not a rank -- 'when deposed, a peasant like the rest'; every trade has its own office too.",
    retrieve_when=["office, or office-holder", "whether ordination confers a permanent status"],
    do_not_retrieve_when=["the participant means the priesthood claim itself (retrieve we-are-all-priests)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none",
),

dict(
    num="6.4", slug="calling", tier=2, doc03_tier=1, demoted=True,
    world_word="calling -- every station commanded by God, and 'regularly called' for the pulpit",
    world_word_plain="calling / 'regularly called'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented, weighted to the confessional register (Melanchthon); by attestation the founder's own texts say 'office' and 'estate' rather than 'calling' as often -- disclosed as a real vocabulary difference between voices, not smoothed.",
    canon_cells=["F3-I", "F5-I"],
    rows=[15, 31, 37, 38],
    row_loci={
        37: "the Augsburg Confession -- 'estates of life and what works in every calling be pleasing to God'",
        38: "the Apology XXVII, read entire this pass -- 'callings are personal... perfection with us is that every one with true faith should obey his own calling'",
        15: "the Eight Wittenberg Sermons -- 'I was regularly called by the Council to preach in this place'",
        31: "the Table Talk -- 'matrimony proceedeth freely in every state and calling' (Contested as verbatim)",
    },
    related=["6.2", "6.3", "6.1", "6.5", "8.5", "2.3", "8.3", "7.1", "4.2", "6.8", "8.4"], tension=[],
    plain_meaning=(
        "Every station of life -- father, mother, prince, preacher -- as a work commanded by God "
        "and pleasing to Him, against monks who 'put it far above all other kinds of life'; and, "
        "of the ministry specifically, the rule that no one teaches publicly 'unless he be "
        "regularly called.'"
    ),
    false_friend=["'calling' heard as a career one chooses or feels personally drawn to", "'vocation' heard as a religious profession specifically"],
    senses=dict(
        informational=(
            "Our confession claims we 'have taught to good purpose concerning all estates and "
            "duties of life, as to what estates of life and what works in every calling be "
            "pleasing to God' -- against monks who 'put it far above all other kinds of life "
            "ordained of God.' The Apology's closing word: 'callings are unlike... callings are "
            "personal... perfection with us is that every one with true faith should obey his "
            "own calling.' Of the ministry: 'no one should publicly teach in the Church or "
            "administer the Sacraments unless he be regularly called,' which our founder says of "
            "himself -- 'I was regularly called by the Council to preach in this place.'"
        ),
        evidential="Weighted to the confessional register; the founder's own texts more often say 'office' or 'estate' for this same ground.",
        personal="This word redefines the ministry as vocation, not merely institution: a station commanded, not chosen -- and holier in no case than another.",
        translational="Do not hear 'calling' as a career chosen or a religious profession: we mean a station commanded -- fatherhood, rule, preaching -- personal, not chosen, and, for the pulpit, a regular call from the community.",
    ),
    quick_meaning="Every station -- father, mother, prince, preacher -- as work God commands and is pleased by; for the pulpit, a regular call from the community.",
    retrieve_when=["calling, or 'regularly called'", "whether any station is holier than another"],
    do_not_retrieve_when=["the participant means office as a structural term rather than calling as vocation (retrieve office)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none by attestation, weighted to the confessional register",
),

dict(
    num="6.5", slug="pastor", tier=2, doc03_tier=2,
    world_word="pastor / preacher -- the office the catechism addresses and rebukes",
    world_word_plain="pastor / preacher",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented as the catechism's own address to pastors, its own rebuke, and the confession's account of clerical marriage.",
    canon_cells=["F3-I"],
    rows=[15, 25, 26, 31, 37, 38],
    row_loci={
        25: "the Large Catechism -- addressed 'to all pastors and preachers, that they should daily exercise themselves in the catechism'",
        26: "the Small Catechism -- 'what hearers owe their pastors'",
        37: "the Augsburg Confession -- 'our priests were desirous to avoid these open scandals, they married wives'",
        31: "the Table Talk -- 'shepherds of souls are worthy of double honour' (Contested as verbatim)",
        38: "the Apology XV, cited among this entry's Registry rows (Doc_06 SS5 entry 6.5)",
        15: "the Eight Wittenberg Sermons, cited among this entry's Registry rows (Doc_06 SS5 entry 6.5)",
    },
    related=["6.3", "6.4", "6.2", "4.1", "5.9", "5.10", "8.3", "4.2", "4.9", "5.8", "7.3"], tension=[],
    plain_meaning=(
        "The office-holder our catechism addresses and rebukes -- to read, catechize, examine, "
        "absolve, exclude, and be honoured and fed -- married, called, and, in our own report, "
        "often negligent."
    ),
    false_friend=["the pastor heard as a settled professional clergyman rather than a called, married, often-underpaid office-holder we ourselves rebuke in print"],
    senses=dict(
        informational=(
            "Our Large Catechism is addressed 'to all pastors and preachers, that they should "
            "daily exercise themselves in the catechism,' and rebukes them: 'very negligent... "
            "some from great and high art... but others from sheer laziness'; 'shameful "
            "gluttons... who ought to be more properly swineherds and dog-tenders than "
            "care-takers of souls and pastors.' They are owed honour and a living -- 'what "
            "hearers owe their pastors' -- and they starve where nobles let parishes decay. They "
            "are married: 'our priests were desirous to avoid these open scandals, they married "
            "wives.'"
        ),
        evidential="Attested at the catechism's own address and rebuke, and the confession's account of clerical marriage.",
        personal="This is the one office we rebuke, in print, in our own most-used household book -- never merely praised.",
        translational="Do not hear 'pastor' as a settled professional clergyman: we mean a called, married office-holder, often poor, told daily to read a page and rebuked by name for not doing so.",
    ),
    quick_meaning="The called, married office-holder our catechism addresses and rebukes for negligence -- owed honour and a living, never a settled professional class.",
    retrieve_when=["pastor, or preacher", "clerical marriage", "what a pastor owes his congregation, and is owed"],
    do_not_retrieve_when=["the participant means calling as a general concept (retrieve calling)"],
    doc06_tags="[SC][RT][DR]", ag_note="none",
),

dict(
    num="6.6", slug="christendom", tier=2, doc03_tier=1, demoted=True,
    world_word="Christendom -- Christenheit, the whole body wider than Rome's own confirmation",
    world_word_plain="Christendom",
    distortion_risk="high", weight="corroborating",
    formation_confidence="Documented",
    divergence_note="Documented, weighted to Luther for the preference of this word over 'Church'; one confessional use is attested (Apology 5626, read this pass, in the bracketed German text).",
    canon_cells=["F5-I"],
    rows=[6, 8, 11, 25, 38, 87],
    row_loci={
        11: "Christian Nobility -- Christendom including 'Muscovites, Russians, Greeks, Bohemians,' 'perhaps better Christians than we are'",
        25: "the Large Catechism -- 'holy Christendom (eine heilige Christenheit)'",
        8: "Papacy at Rome -- Christendom that cannot be reduced 'to one man'",
        38: "the Apology, read this pass -- 'this cause, which is not only ours, but that of all Christendom'",
        6: "Good Works, cited among this entry's Registry rows (Doc_06 SS5 entry 6.6)",
        87: "the translators' own glossing footnotes on our avoidance of 'Kirche' (layer)",
    },
    related=["5.8", "6.7", "4.7", "7.1", "6.9"], tension=[],
    plain_meaning=(
        "Our own preferred word for the whole body of Christians -- wider than Rome's "
        "confirmation, including 'Muscovites, Russians, Greeks, Bohemians' -- the Creed's 'one "
        "holy Christian Church,' which cannot be reduced to one man."
    ),
    false_friend=["'Christendom' heard as a political order or a civilization"],
    senses=dict(
        informational=(
            "Christendom includes those who 'merely do not have their priests and bishops "
            "confirmed by Rome' -- 'Muscovites, Russians, Greeks, Bohemians' -- who 'agree with "
            "us in holding to the same baptism, Sacrament, Gospel, and all the articles of "
            "faith' and are 'not heretics and apostates, but perhaps better Christians than we "
            "are.' It cannot be reduced 'to one man.' The Creed's article, in our own German, is "
            "best rendered 'holy Christendom (eine heilige Christenheit).' Our confession says, "
            "once, 'this cause, which is not only ours, but that of all Christendom.'"
        ),
        evidential="Weighted to Luther as our preferred word over 'Kirche'; the confessional voice attests it once, in bracketed German text.",
        personal="This word refuses to let us collapse the whole body of Christians into our own movement, or into any one man's confirmation of it.",
        translational="Do not hear 'Christendom' as a political order or civilization; we mean the whole assembly of Christians, wider than any pope's confirmation, named in preference to 'Church.'",
    ),
    quick_meaning="Our own preferred name for the whole body of Christians, wider than Rome's confirmation -- 'the one holy Christian Church,' not reducible to one man.",
    retrieve_when=["Christendom", "whether Christians outside our own confirmation still count as Christians to us"],
    do_not_retrieve_when=["the participant means our own local congregation specifically (retrieve congregation)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none, weighted to Luther",
),

dict(
    num="6.7", slug="pope-and-antichrist", tier=2, doc03_tier=1, demoted=True,
    world_word="the pope -- named at rising pitch, 'Antichrist' in polemic, 'the Church of Rome' in confession",
    world_word_plain="pope / papacy / 'Antichrist'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented in two distinct registers, demonstrably differing on the adversary's own "
        "name -- 'the Church of Rome' (1530, confessional) against 'Antichrist' (1520-21, "
        "1539-45, polemical) -- a real plurality across registers, carried here as [PV] rather "
        "than flattened into either."
    ),
    canon_cells=["F3-I"],
    rows=[1, 8, 11, 12, 25, 31, 37, 38],
    row_loci={
        11: "Christian Nobility -- 'the Romanists' and their 'three walls'",
        8: "Papacy at Rome -- 'the papacy is the mighty hunting of the Roman bishop'",
        37: "the Augsburg Confession -- 'the Church of Rome as known from its writers'",
        38: "the Apology, read this pass -- 'the Papacy also will be a part of the kingdom of Antichrist if it thus defends human services as justifying'",
        31: "the Table Talk -- 'the Pope is a mere tormentor of the conscience' (Contested as verbatim)",
        1: "the 1539 preface, cited among this entry's Registry rows (Doc_06 SS5 entry 6.7)",
        12: "Babylonian Captivity, cited among this entry's Registry rows (Doc_06 SS5 entry 6.7)",
        25: "the Large Catechism -- 'under the Papacy, where faith was entirely put under the bench'",
    },
    related=["4.7", "6.6", "5.8", "3.3", "3.4", "1.1", "1.6", "6.9", "6.8", "7.1"], tension=[],
    plain_meaning=(
        "The adversary named at rising pitch -- 'the Romanists' behind three walls, the papacy "
        "as 'Antichrist' in our polemics -- and, in our confession before the Emperor, 'the "
        "Church of Rome as known from its writers': one adversary, two registers of naming."
    ),
    false_friend=[
        "'Antichrist' heard as a fixed doctrine about the papal office as such, rather than a conditional charge",
        "the confessional courtesy ('the Church of Rome') heard as a retraction of the polemical naming",
    ],
    senses=dict(
        informational=(
            "Our polemics name him louder each year: 'the Romanists' and their 'three walls'; "
            "'the papacy is the mighty hunting of the Roman bishop'; in the catechism he is the "
            "past -- 'under the Papacy, where faith was entirely put under the bench.' At table: "
            "'the Pope is a mere tormentor of the conscience.' Before the Emperor the same "
            "adversary is 'the Church of Rome as known from its writers' -- and the Apology "
            "states the plainest test: 'the Papacy also will be a part of the kingdom of "
            "Antichrist if it thus defends human services as justifying.'"
        ),
        evidential="Attested at every register, both voices -- the confessional register (1530) and the polemical (1520-21, 1539-45) demonstrably differing on the adversary's own name.",
        personal="We name one adversary two ways depending on the room we are speaking in -- neither register cancels the other, and neither should be flattened into the whole of what we mean.",
        translational="Do not hear 'Antichrist' as a fixed doctrine about the papal office in general, or the confessional courtesy as a retraction: we mean one adversary named in two pitches, with the sharpest test being conditional -- Antichrist's kingdom if human traditions are made to justify.",
    ),
    quick_meaning="One adversary, two names depending on the room -- 'Antichrist' in our polemics, 'the Church of Rome as known from its writers' before the Emperor.",
    retrieve_when=["the pope, papacy, or 'Antichrist'", "why we speak of the pope differently in different settings"],
    do_not_retrieve_when=["the participant means the devil generally, of whom the pope is one instrument (retrieve the devil)"],
    doc06_tags="[SC][DR][RT][PV]", ag_note="none -- every register, both voices",
),

dict(
    num="6.8", slug="sects-and-new-spirits", tier=2, doc03_tier=2,
    world_word="sects -- 'new spirits,' fanatics, and the Anabaptists named by the confession",
    world_word_plain="sects / 'new spirits' / Anabaptists",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the founder's own generic naming and the confession's own specific condemnation.",
    canon_cells=["F3-I"],
    rows=[7, 25, 28, 34, 37, 38],
    row_loci={
        25: "the Large Catechism -- 'our new spirits, to mock at Baptism, omit from it God's Word'",
        37: "the Augsburg Confession -- 'the Anabaptists and others who think that the Holy Ghost comes to men without the external Word'",
        38: "the Apology, read this pass -- the same charge restated in its own words, and Muentzer named",
        7: "the New Testament preface, cited among this entry's Registry rows (Doc_06 SS5 entry 6.8; editorial layer)",
        28: "the hymnal prefaces, cited among this entry's Registry rows (Doc_06 SS5 entry 6.8)",
        34: "Bondage of the Will, one word only ('Sacramentarians')",
    },
    related=["3.1", "5.2", "5.3", "6.4", "2.1", "4.7", "6.7", "7.4", "4.9", "5.1", "5.5", "8.8"], tension=[],
    plain_meaning=(
        "Our own generic names for the radicals -- 'new spirits,' 'fanatics,' 'enthusiasts' -- "
        "and our confession's own named condemnation of 'the Anabaptists and others who think "
        "that the Holy Ghost comes to men without the external Word.'"
    ),
    false_friend=["'enthusiast' and 'fanatic' heard as temperament words, or 'Anabaptist' heard as a neutral label rather than a specific theological charge"],
    senses=dict(
        informational=(
            "'Our new spirits, to mock at Baptism, omit from it God's Word'; 'sects clamoring "
            "that Baptism is an external thing'; 'the prating of nearly all the fanatical "
            "spirits.' Our confession names them: 'the Anabaptists and others who think that the "
            "Holy Ghost comes to men without the external Word, through their own preparations "
            "and works.' The Apology restates the charge and reports that 'through such "
            "commendations Muentzer was deceived, and thereby many Anabaptists were led astray.'"
        ),
        evidential="Attested at the founder's own generic polemics and the confession's specific, named condemnation.",
        personal="This is a specific theological charge we make -- the Spirit apart from the external Word -- against people our own authorities also helped suppress, whose own account is not ours to give.",
        translational="Do not hear 'enthusiast' or 'fanatic' as temperament words, or 'Anabaptist' as neutral: we mean a specific charge -- the Spirit claimed apart from the external Word -- and names given to people our own side helped suppress.",
    ),
    quick_meaning="Our own names for the radicals -- 'new spirits,' fanatics -- charged specifically with claiming the Spirit apart from the external Word.",
    retrieve_when=["sects, new spirits, fanatics, enthusiasts, or Anabaptists"],
    do_not_retrieve_when=["the participant wants the radicals' own account of themselves -- our library does not carry it"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none",
),

dict(
    num="6.9", slug="the-turk", tier=3, doc03_tier=3,
    world_word="the Turk -- named with pope and Jews as outside Christianity, one of the devil's instruments",
    world_word_plain="the Turk",
    distortion_risk="medium", weight="illustrative",
    formation_confidence="Documented",
    divergence_note="Documented at the household prayer's own petition and the confession's naming of the 'most atrocious, hereditary, and ancient enemy'; a thin entry, more Doc_08's material than the lexicon's own.",
    canon_cells=["F1-I"],
    rows=[7, 25, 31, 37],
    row_loci={
        25: "the Large Catechism -- 'vanquish the Turks and all enemies'",
        37: "the Augsburg Confession, the Diet's own 'most atrocious, hereditary, and ancient enemy'",
        31: "the Table Talk -- 'I will pray... as long as I live' (Contested as verbatim)",
        7: "the New Testament preface, cited among this entry's Registry rows (Doc_06 SS5 entry 6.9)",
    },
    related=[], tension=[],
    plain_meaning="The external enemy named with pope and Jews as outside Christianity -- 'heathen, Turks, Jews, or false Christians and hypocrites' -- against whom our household prays and nothing more.",
    false_friend=["'the Turk' heard as a political or ethnic enemy in the modern sense"],
    senses=dict(
        informational="We name the Turk with 'heathen, Turks, Jews, or false Christians and hypocrites'; our confession calls him the 'most atrocious, hereditary, and ancient enemy,' and our household prays to 'vanquish the Turks and all enemies.'",
        evidential="A thin entry -- met in our library by a petition and nothing bodily.",
        personal="One of the devil's three instruments in our own frame, met by us with prayer, not with any bodily account.",
        translational="Do not hear 'the Turk' as a political or ethnic category in the modern sense; we mean one of the devil's instruments, met by a household petition.",
    ),
    quick_meaning="One of the devil's instruments in our own frame, named alongside pope and Jews as outside Christianity -- met by us with prayer, not narrative.",
    retrieve_when=["the Turk specifically"],
    do_not_retrieve_when=["the participant means the devil generally (retrieve the devil)"],
    doc06_tags="[SC][RT]", ag_note="none",
),

# ============================== Cluster 7 ==================================
# The two governments -- sword, obedience, liberty (Doc_06 5.7)
dict(
    num="7.1", slug="the-two-governments", tier=1, doc03_tier=1,
    world_word="the two governments -- God's spiritual rule by the Word, and secular rule by the sword",
    world_word_plain="the two governments",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented that our own usages differ across texts (\"two classes\"/\"two governments\" "
        "in one work, a different Christ-against-Satan \"two kingdoms\" in another); Contested "
        "whether a single later-named doctrine should be read across both. [CT], provisional, "
        "contest type: historical scope. No secondary source is rowed in the Source Registry "
        "for this contest; carried forward as still provisional, not resolved by this authoring "
        "pass, which does not characterize any present-day tradition's use of the later label."
    ),
    canon_cells=["F3-I"],
    rows=[15, 20, 29, 34, 37],
    row_loci={
        20: "Secular Authority, Part One only -- 'God has ordained the two governments'",
        37: "the Augsburg Confession -- 'the power of the Church and the power of the sword'",
        15: "the Eight Wittenberg Sermons -- 'we have the jus verbi, but not the executio'",
        34: "Bondage of the Will (OCR-degraded) -- the other 'two kingdoms,' Christ against Satan",
        29: "the hymns, Hymn XXVI -- 'the kingdom ours remaineth'",
    },
    related=["7.2", "7.3", "7.4", "6.1", "6.2", "6.4", "4.2", "4.8", "5.6", "2.8", "2.9", "4.7",
             "6.6", "6.7", "7.5"], tension=[],
    plain_meaning=(
        "God's two governments -- the spiritual, which by the Word under Christ makes "
        "Christians, and the secular, which by the sword restrains the wicked -- both God's own, "
        "neither to be confounded with the other. In a different book, we also speak of 'two "
        "kingdoms' of Christ and Satan at war, which is not the same pair."
    ),
    false_friend=[
        "'the two kingdoms doctrine' heard as a settled system, as though we taught it as one fixed technical term",
        "the doctrine heard as separating church and state in the modern sense, or as giving the state a free hand",
        "our two 'two kingdoms' pairings (church/civil, and Christ/Satan) merged into one",
    ],
    senses=dict(
        informational=(
            "'We must divide all the children of Adam into two classes; the first belong to the "
            "kingdom of God, the second to the kingdom of the world.' Since not all the world is "
            "made of real Christians, 'God has ordained the two governments; the spiritual, "
            "which by the Holy Spirit under Christ makes Christians and pious people, and the "
            "secular, which restrains the unchristian and wicked.' Our confession draws the same "
            "line and says why: 'for the comforting of men's consciences, [we] were constrained "
            "to show the difference between the power of the Church and the power of the sword,' "
            "both 'held in reverence and honor, as the chief blessings of God on earth.' We feel "
            "the distinction from within as the Word's own limit: 'we have the jus verbi, but "
            "not the executio,' which is why a right reform had to obtain the aid of the "
            "authorities. A second, different pairing uses the same English words: 'there are "
            "two kingdoms in the world mutually militating against each other... Satan reigns in "
            "the one... in the other kingdom Christ reigns' -- a spiritual-warfare pairing, not "
            "the church/civil one."
        ),
        evidential="Attested at both voices; the treatise's own main part on the limits of obedience remains unread by this build, disclosed as a real gap.",
        personal="This distinction keeps the conscience from being ruled by the sword, and the sword from being the Church's instrument -- felt at every meal, in the daily bread's own prayer for the prince.",
        translational="Do not hear 'the two kingdoms doctrine' as a settled system, or assume it separates church and state as moderns do: we mean two governments, both God's, distinguished so the conscience is not ruled by the sword nor the sword by the Word -- and a second, different 'two kingdoms' of Christ and Satan that must not be merged with the first.",
    ),
    quick_meaning="God's two governments -- spiritual rule by the Word, secular rule by the sword -- both God's own, distinguished so the conscience is never governed by force.",
    retrieve_when=["the two governments, or 'two kingdoms'", "why we would not force reform with the sword",
                   "the prince's own role among us"],
    do_not_retrieve_when=["the participant wants a modern political-theology reading of 'two kingdoms' -- we characterize no present-day tradition's use of the term"],
    doc06_tags="[AS][TC][DR][RT][CT]", ag_note="none -- both voices",
    ct=(
        "CT status carried from Doc_06 SS2.2: contest type historical scope -- whether the "
        "later systematic label 'two kingdoms doctrine' applies as broadly to our founder's own "
        "usage as claimed. Provisional: no secondary source is rowed in the Source Registry; "
        "Doc_06 names leads for the Registry owner (Cargill Thompson's 1969 article; Wright's "
        "2010 study) but cites neither as a source. This authoring pass carries the tag forward "
        "as still provisional and does not resolve it."
    ),
),

dict(
    num="7.2", slug="the-sword", tier=2, doc03_tier=1, demoted=True,
    world_word="the sword -- temporal power ordained of God, reaching pope and monk alike",
    world_word_plain="the sword / secular authority",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the founder's own treatise and the confession's own list of lawful civil ordinances.",
    canon_cells=["F3-I"],
    rows=[10, 11, 20, 37],
    row_loci={
        20: "Secular Authority -- 'so Paul interprets the secular sword, Romans xiii... not a terror to good works, but to the evil'",
        11: "Christian Nobility -- the temporal power bears 'sword and rod with which to punish the evil and to protect the good'",
        37: "the Augsburg Confession -- 'lawful civil ordinances are good works of God'",
        10: "Concerning the Ban, cited among this entry's Registry rows (Doc_06 SS5 entry 7.2)",
    },
    related=["7.1", "7.3", "7.4", "5.9", "6.3"], tension=[],
    plain_meaning=(
        "The power ordained of God that bears 'sword and rod with which to punish the evil and "
        "to protect the good,' reaching pope and monk alike -- which the spiritual estate may "
        "never wield, since its own sword is 'the sword of the Spirit.'"
    ),
    false_friend=["'the sword' heard as violence sanctioned by religion, or 'secular' heard as non-religious"],
    senses=dict(
        informational=(
            "The temporal power 'bears sword and rod with which to punish the evil and to "
            "protect the good' and 'is ordained of God to punish evil-doers,' reaching 'pope, "
            "bishops, priests, monks, nuns or anybody else.' The spiritual estate's own 'sword "
            "is not to be of iron, but the sword of the Spirit.' Our confession: 'lawful civil "
            "ordinances are good works of God,' and Christians may serve as soldiers, swear "
            "oaths, and marry."
        ),
        evidential="Attested in the founder's own treatises and the confession's own list of what Christians may lawfully do.",
        personal="This power is God's own ordinance for peace, held by the ruler and by no cleric -- honoured and prayed for, never the Church's own instrument.",
        translational="Do not hear 'the sword' as violence blessed by religion, or 'secular' as non-religious: we mean God's own ordinance for external peace, held by the temporal ruler alone.",
    ),
    quick_meaning="God's own ordinance for peace, held by the temporal ruler alone and reaching pope and monk alike -- never the Church's instrument.",
    retrieve_when=["the sword, or secular authority", "whether the Church may wield force"],
    do_not_retrieve_when=["the participant means the two governments' whole doctrine (retrieve the two governments)"],
    doc06_tags="[SC][TC][DR][RT]", ag_note="none",
),

dict(
    num="7.3", slug="obedience", tier=2, doc03_tier=2,
    world_word="obedience -- owed to parents and magistrates as to God, save only when commanded to sin",
    world_word_plain="obedience",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the household catechism's own honour-clause and the confession's own limit-clause.",
    canon_cells=["F3-P"],
    rows=[11, 25, 26, 31, 37],
    row_loci={
        25: "the Large Catechism -- honour 'a far higher thing... than to love one'",
        26: "the Small Catechism -- 'for earthly authorities' and 'for those under authority'",
        37: "the Augsburg Confession -- 'bound to obey their own magistrates and laws save only when commanded to sin'",
        31: "the Table Talk -- 'all that govern are called Fathers' (Contested as verbatim)",
        11: "Christian Nobility, cited among this entry's Registry rows (Doc_06 SS5 entry 7.3)",
    },
    related=["7.1", "7.2", "4.2", "6.5", "2.8"], tension=[],
    plain_meaning=(
        "Owed to parents, masters and magistrates as to God's own ordering -- 'all that govern "
        "are called Fathers' -- and limited at exactly one point: 'save only when commanded to "
        "sin.'"
    ),
    false_friend=["obedience heard as servility, or the limit-clause heard as a general right of resistance"],
    senses=dict(
        informational=(
            "The Fourth Commandment's 'honor' is 'a far higher thing... than to love one,' "
            "extended to 'all that govern'; parents are to be regarded 'as in God's stead... "
            "however lowly, poor, frail, and queer they may be.' Our confession: 'Christians are "
            "necessarily bound to obey their own magistrates and laws save only when commanded "
            "to sin; for then they ought to obey God rather than men.'"
        ),
        evidential="Attested at both catechisms and the confession's own limit-clause.",
        personal="A majesty hidden in parents and rulers, honoured even where they are 'lowly, poor, frail, and queer' -- limited at the one point where obeying them would be sin.",
        translational="Do not hear obedience as servility, and do not hear the limit-clause as a general right of resistance: we mean honour of a majesty hidden in ordinary people, limited only where obedience would mean sin.",
    ),
    quick_meaning="Honour owed to parents, masters and magistrates as to God's own ordering -- limited at exactly one point: 'save only when commanded to sin.'",
    retrieve_when=["obedience", "when we may or must disobey"],
    do_not_retrieve_when=["the participant means the sword's own institutional power (retrieve the sword)"],
    doc06_tags="[SC][DR][RT]", ag_note="none",
),

dict(
    num="7.4", slug="insurrection", tier=2, doc03_tier=2,
    world_word="insurrection -- 'the common man,' 1522's own vocabulary, bound to that year",
    world_word_plain="insurrection / 'the common man' (1522 only)",
    distortion_risk="high", weight="corroborating",
    formation_confidence="Documented",
    divergence_note=(
        "Documented for 1521-22 only, Luther-only, cross-register, period-bound -- confirmed; "
        "the 1531 Apology retrospect (Ap 10002-10006) names Muentzer but is not the 1522 "
        "vocabulary itself. Bar, stated plainly: the 1525 tract's own language is not in our "
        "library and is barred from being voiced as ours (Named Comparandum, Source Registry "
        "row 94); nothing here characterizes 1525 beyond its documented existence."
    ),
    canon_cells=["F3-I"],
    rows=[11, 15, 19, 48],
    row_loci={
        19: "Earnest Exhortation, opening only -- 'the common man has been brooding over the injury he has suffered'",
        15: "the Eight Wittenberg Sermons -- 'I did nothing; I left it to the Word'",
        11: "Christian Nobility, cited among this entry's Registry rows (Doc_06 SS5 entry 7.4)",
        48: "Admonition to Peace, context only, cited among this entry's Registry rows (Doc_06 SS5 entry 7.4)",
    },
    related=["7.1", "7.2", "7.5", "3.1", "6.8", "9.5"], tension=[],
    plain_meaning=(
        "The unrest we addressed at the turn of 1522 -- the common man who 'would indeed have "
        "good reason to lay about him with flails and cudgels' -- met with our refusal of force "
        "and our confidence that 'God will watch over His Word.'"
    ),
    false_friend=["the reputation of the later 1525 tract projected back onto this 1522 vocabulary -- that tract's own language is not ours to voice"],
    senses=dict(
        informational=(
            "'The common man has been brooding over the injury he has suffered in property, in "
            "body and in soul, and has become provoked... and would indeed have good reason to "
            "lay about him with flails and cudgels, as the peasants are threatening to do' -- "
            "yet there is 'no fear whatever that there will be an insurrection' because 'God "
            "will watch over His Word.' In the sermons: 'I could have brought great bloodshed "
            "upon Germany... but what would it have been? A fool's play. I did nothing; I left "
            "it to the Word.'"
        ),
        evidential="Luther-only, cross-register, period-bound to 1521-22 -- confirmed; the 1531 Apology retrospect names Muentzer but is not this vocabulary.",
        personal="This is our own sympathy for common grievance held together with our refusal of force -- a stance we can attest only for this one narrow window.",
        translational="Do not project the later 1525 tract's reputation onto this 1522 vocabulary; we mean sympathy for common grievance and a refusal of force, attested only for 1521-22 -- the 1525 tract's own language is not something we can voice.",
    ),
    quick_meaning="Our 1522 stance toward common unrest -- sympathy for real grievance, refusal of force, and confidence that 'God will watch over His Word.'",
    retrieve_when=["insurrection, or 'the common man,' specifically in 1522"],
    do_not_retrieve_when=["the participant asks about the 1525 Peasants' War tract itself -- its own wording is not in our library and is not ours to voice"],
    doc06_tags="[SC][DR][RT][PV]", ag_note="Luther-only, cross-register, period-bound to 1521-22 -- confirmed",
),

dict(
    num="7.5", slug="must-and-free", tier=1, doc03_tier=1,
    world_word="'must' and 'free' -- Christian liberty measured entirely by the weak brother",
    world_word_plain="'must' and 'free'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note=(
        "Documented for the texts themselves; Widely Accepted for the 1522 outcome (our "
        "editor's own account, not independently attested elsewhere); reception is 'one "
        "congregation, once, editorial' and not claimed more broadly."
    ),
    canon_cells=["F5-P"],
    rows=[13, 15, 16, 25, 37, 38],
    row_loci={
        13: "Christian Liberty, opening only -- 'a Christian man is a perfectly free lord of all... a perfectly dutiful servant of all'",
        15: "the Eight Wittenberg Sermons, all eight -- 'take note of these two things, must and free'",
        37: "the Augsburg Confession -- holy-days 'observed without sin... nevertheless consciences are not to be burdened'",
        38: "the Apology, read this pass -- 'the use of liberty is to be so controlled that the inexperienced may not be offended'",
        25: "the Large Catechism -- 'no one should by any means be coerced or compelled, lest we institute a new murdering of souls'",
        16: "That Doctrines of Men Are to Be Rejected, cited among this entry's Registry rows (Doc_06 SS5 entry 7.5)",
    },
    related=["3.1", "2.1", "2.8", "4.6", "3.4", "5.3", "5.5", "5.6", "8.1", "8.3", "8.6", "8.8",
             "7.1", "7.4", "4.7", "4.1", "9.7"], tension=[],
    plain_meaning=(
        "Our 1522 sermons' own governing distinction: the 'must' is what necessity requires, "
        "faith above all; the 'free' is what one may use or not, so long as it profits one's "
        "brother. A liberty preached only to captive consciences, bound by love to the weak, "
        "and turned by 1529 against those who called their own neglect 'liberty.'"
    ),
    false_friend=[
        "Christian liberty heard as autonomy -- freedom from rules, the right to do whatever Scripture permits regardless of others",
        "our 1529 rebuke of lazy liberty heard as a retraction of the 1522 liberty",
    ],
    senses=dict(
        informational=(
            "'A Christian man is a perfectly free lord of all, subject to none. A Christian man "
            "is a perfectly dutiful servant of all, subject to all.' 'Take note of these two "
            "things, \"must\" and \"free.\" The \"must\" is that which necessity requires, and "
            "which must ever be unyielding; as, for instance, the faith... but \"free\" is that "
            "in which I have choice, and may use or not, yet in such wise that it profit my "
            "brother and not me. Now do not make a \"must\" out of what is \"free.\"' The free "
            "things are named -- leaving monasteries, priests marrying, images -- and the rule "
            "for them is the neighbour: 'we must not look upon ourselves... but upon our "
            "neighbor... have patience with him for a time.' By 1529 the same word is the "
            "charge: some 'pretend that it is a matter of liberty and not necessary... go so far "
            "that they become quite brutish'; 'if you wish such liberty, you may just as well "
            "have the liberty to be no Christian.' Our confession settles the free things as "
            "liberty in rites, 'consciences are not to be burdened, as though such observance "
            "was necessary to salvation'; the Apology: 'the use of liberty is to be so "
            "controlled that the inexperienced may not be offended.'"
        ),
        evidential="Attested at all eight of the 1522 sermons and both confessional documents; the pairing's exact phrasing is single-register (the Sermons), the underlying liberty both voices.",
        personal="This is the sharpest tension we carry: the Word licenses, love restrains, and then, when restraint has produced sloth, the same word 'liberty' becomes our own charge against ourselves.",
        translational="Do not hear Christian liberty as autonomy, and do not hear our 1529 rebuke as retracting 1522's liberty: we mean a liberty of captive consciences, measured entirely by the weak brother -- a 'must' that never yields and a 'free' that is never made a law.",
    ),
    quick_meaning="The 'must' that never yields (faith) and the 'free' that must never be made a law -- Christian liberty measured entirely by the weak brother.",
    retrieve_when=["'must' and 'free,' or Christian liberty", "the weak in faith", "whether liberty means doing whatever one wants"],
    do_not_retrieve_when=["the participant means one specific 'free' thing on its own (retrieve fasting, images, marriage, or vows as fits)"],
    doc06_tags="[AS][DR][TC][RT]",
    ag_note="none for 'liberty'; Luther-only, single-register (the Sermons) for the 'must'/'free' pairing itself",
),

# ============================== Cluster 8 ==================================
# Vows, chastity, marriage -- the monastic and marital cluster (Doc_06 5.8)
dict(
    num="8.1", slug="vows", tier=2, doc03_tier=1, demoted=True,
    world_word="vows -- void where made to merit, kept where lawful",
    world_word_plain="vow / monastic vows",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the confession and the Apology XXVII, read entire this pass; the whole-book source it reiterates (De Votis Monasticis) is itself not vendored, disclosed as a named absence.",
    canon_cells=["F5-I"],
    rows=[12, 16, 24, 25, 37, 38, 61],
    row_loci={
        37: "the Augsburg Confession -- 'no man's law, no vow, can annul the commandment and ordinance of God'",
        38: "the Apology XXVII, read entire this pass -- 'we hold that lawful vows ought to be observed'",
        24: "To the Knights of the Teutonic Order -- 'such a vow is nothing at all and is not to be kept, unless a man have God's special grace'",
        61: "De Votis Monasticis -- named absence; not vendored, referenced only as the Apology's own reiterated book",
        12: "Babylonian Captivity, cited among this entry's Registry rows (Doc_06 SS5 entry 8.1)",
        16: "That Doctrines of Men Are to Be Rejected, cited among this entry's Registry rows (Doc_06 SS5 entry 8.1)",
        25: "the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 8.1)",
    },
    related=["8.3", "8.2", "8.4", "8.5", "2.4", "3.4", "5.2", "7.5", "2.1", "8.6"], tension=[],
    plain_meaning=(
        "The binding promise we declare void wherever it is made to merit -- once taught to be "
        "'equal to Baptism,' a 'state of perfection' -- so that 'no man's law, no vow, can "
        "annul the commandment and ordinance of God.'"
    ),
    false_friend=["assuming we condemned all vows, or all monks, rather than only vows made to merit or extorted from the unwilling"],
    senses=dict(
        informational=(
            "'No man's law, no vow, can annul the commandment and ordinance of God.' We recall "
            "what was taught: vows 'equal to Baptism,' 'a state of perfection' that merited "
            "forgiveness -- vows 'commonly taken have been wicked services, and, consequently, "
            "are void.' The Apology names what makes a vow unlawful: the opinion that 'he who "
            "vows thinks that he merits the remission of sins before God' -- lawful vows, by "
            "contrast, we hold ought to be observed, and the exercises themselves (obedience, "
            "poverty, celibacy) are, as exercises, 'adiaphora' saints have used 'without "
            "impiety.'"
        ),
        evidential="Attested at the confession and the Apology XXVII, read entire this pass; the book Melanchthon reiterates on this subject is itself not in our library.",
        personal="We refuse vows made to merit, made equal to baptism, or extorted from the unwilling or the too-young; the exercises themselves we count indifferent.",
        translational="Do not assume we condemned all vows or all monastic life; we mean lawful vows kept, and unlawful ones -- those made to merit, made equal to baptism, extorted, or made against a gift one lacks -- declared void.",
    ),
    quick_meaning="Lawful vows kept; unlawful ones -- made to merit, made equal to baptism, or extorted -- declared void; the monastic exercises themselves indifferent.",
    retrieve_when=["vows, or monastic vows", "whether we condemned monastic life as such"],
    do_not_retrieve_when=["the participant means chastity specifically (retrieve chastity)"],
    doc06_tags="[SC][DR][TC][RT]", ag_note="none; the Apology XXVII read entire this pass",
),

dict(
    num="8.2", slug="chastity", tier=2, doc03_tier=2,
    world_word="chastity -- the monastic word turned inside out: true chastity is marriage",
    world_word_plain="chastity",
    distortion_risk="high", weight="corroborating",
    formation_confidence="Documented",
    divergence_note="Documented for the argument at large, both voices; Luther-only, single-register, for the exact coinage 'unchaste chastity.'",
    canon_cells=["F5-I"],
    rows=[24, 25, 37, 38],
    row_loci={
        24: "To the Knights of the Teutonic Order -- 'give up your unchaste chastity and to marry'",
        25: "the Large Catechism -- 'where nature has its course... it is not possible to remain chaste without marriage'",
        37: "the Augsburg Confession -- 'it is not unknown to what extent perpetual chastity is in the power of man'",
        38: "the Apology, cited among this entry's Registry rows (Doc_06 SS5 entry 8.2)",
    },
    related=["8.3", "8.1", "8.4", "4.2"], tension=[],
    plain_meaning=(
        "The monastic word turned inside out: the knights are told to 'give up your unchaste "
        "chastity and to marry,' to 'lay aside false chastity and take upon them the true "
        "chastity of wedlock.' Where nature has its course, chastity outside marriage 'is not "
        "possible' for most."
    ),
    false_friend=["'chastity' heard as celibacy, and our argument heard as lowering a standard rather than naming what nature makes necessary"],
    senses=dict(
        informational=(
            "The exhortation's own title: to 'lay aside false chastity and take upon them the "
            "true chastity of wedlock'; 'give up your unchaste chastity and to marry.' Our "
            "catechism states the ground as nature: 'where nature has its course, as it is "
            "implanted by God, it is not possible to remain chaste without marriage,' with 'some "
            "exceptions (although few).' Our confession: 'it is not unknown to what extent "
            "perpetual chastity is in the power of man'; the Apology: 'all do not have the gift "
            "of continence.'"
        ),
        evidential="The exact coinage 'unchaste chastity' is single-register (the knights' exhortation); the broader argument is both voices.",
        personal="True chastity, for us, is marriage for all but the few with a special gift -- the monastic vow of the rest is what we call 'unchaste chastity.'",
        translational="Do not hear 'chastity' as celibacy or our argument as lowering a standard: we mean true chastity is marriage for nearly everyone, and the vow of the rest 'unchaste chastity.'",
    ),
    quick_meaning="True chastity is marriage for all but the few with a special gift -- the monastic vow of the rest, we say, is 'unchaste chastity.'",
    retrieve_when=["chastity, or celibacy"],
    do_not_retrieve_when=["the participant means vows generally (retrieve vows)"],
    doc06_tags="[AS][DR][RT]", ag_note="none for the argument; Luther-only, single-register for the coinage",
),

dict(
    num="8.3", slug="marriage", tier=1, doc03_tier=1,
    world_word="marriage -- 'the most common and noblest estate, which pervades all Christendom'",
    world_word_plain="marriage / matrimony",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at every register -- catechesis, exhortation, table, confession; the household is documented from the father's own side only, no woman's voice on this term is in our library.",
    canon_cells=["F5-I", "F5-P"],
    rows=[9, 24, 25, 26, 31, 37, 38],
    row_loci={
        25: "the Large Catechism -- 'not a peculiar estate, but the most common and noblest estate, which pervades all Christendom'",
        26: "the Small Catechism -- the Sixth Commandment's household explanation",
        37: "the Augsburg Confession -- 'God ordained marriage to be a help against human infirmity'",
        31: "the Table Talk -- 'the patiences are so many, that my whole life is nothing but patience' (Contested as verbatim)",
        38: "the Apology, read this pass -- 'the law of nature in men cannot be removed by vows or enactments'",
        24: "To the Knights of the Teutonic Order, cited among this entry's Registry rows (Doc_06 SS5 entry 8.3)",
        9: "Concerning the Blessed Sacrament, cited among this entry's Registry rows (Doc_06 SS5 entry 8.3; editorial-layer dedicatee)",
    },
    related=["8.1", "8.2", "8.4", "6.1", "6.4", "6.5", "4.2", "4.8", "7.5", "9.7", "6.2"], tension=[],
    plain_meaning=(
        "'The most common and noblest estate, which pervades all Christendom' -- ordained by "
        "God at creation, necessary for nearly everyone, forbidden to no priest, and the "
        "household in which our own formation is to happen."
    ),
    false_friend=[
        "marriage heard as a private romantic bond",
        "our teaching heard as merely permitting clergy to marry, rather than naming marriage the noblest estate of all",
    ],
    senses=dict(
        informational=(
            "God 'created man and woman separately... not for lewdness, but that they should "
            "legitimately live together, be fruitful, beget children, and nourish and train "
            "them to the honor of God.' Marriage is 'not a peculiar estate, but the most common "
            "and noblest estate, which pervades all Christendom,' before which 'both "
            "ecclesiastical and civil estates must humble themselves.' Our confession makes a "
            "pastor's marriage a public cause: 'our priests were desirous to avoid these open "
            "scandals, they married wives'; 'it is to be expected that the churches shall at "
            "some time lack pastors if marriage is any longer forbidden... men, and that, "
            "priests, are cruelly put to death, contrary to the intent of the Canons, for no "
            "other cause than marriage.' Our own founder's marriage reaches us as patience: 'I "
            "must have patience with Kate my wife... my whole life is nothing but patience.'"
        ),
        evidential="Attested at every register we use -- catechesis, exhortation, table, confession; documented only from the father's side, no woman's own voice on this term is in our library.",
        personal="The noblest estate of all, before which even the clerical and civil estates bow -- and the household in which our whole formation is meant to happen.",
        translational="Do not hear marriage as a private romantic bond, or our teaching as merely permitting clergy to marry: we mean the noblest and commonest estate of all, ordained at creation, the household of formation, a public cause for which priests were killed.",
    ),
    quick_meaning="'The most common and noblest estate, which pervades all Christendom' -- ordained at creation, and the household where our own formation happens.",
    retrieve_when=["marriage, or the married estate", "clerical marriage", "whether marriage or celibacy is holier"],
    do_not_retrieve_when=["the participant wants a woman's own voice on marriage among us -- our library holds none"],
    doc06_tags="[SC][DR][RT]", ag_note="none -- both voices, catechesis, exhortation, conversation, confession",
),

dict(
    num="8.4", slug="spiritual-geysterey", tier=2, doc03_tier=2,
    world_word="'spiritual' -- Geysterey, a claimed status mocked in our own scare-quotes",
    world_word_plain="'spiritual' / 'spirituality'",
    distortion_risk="high", weight="corroborating",
    formation_confidence="Documented",
    divergence_note="Documented at the founder's own text and its own translator's footnote giving the German lemma Geysterey directly from the text.",
    canon_cells=["F5-I"],
    rows=[11, 16, 24, 25, 37, 38],
    row_loci={
        24: "To the Knights of the Teutonic Order -- 'few people will become monks and \"spiritual,\" because the Gospel is beginning to shine' (Geysterey, footnote-supplied German)",
        16: "That Doctrines of Men Are to Be Rejected -- 'this one saying of Christ mightily condemns all orders and spiritual rules'",
        37: "the Augsburg Confession -- 'the exalted title of being the spiritual life and the perfect life'",
        38: "the Apology, cited among this entry's Registry rows (Doc_06 SS5 entry 8.4)",
        11: "Christian Nobility, cited among this entry's Registry rows (Doc_06 SS5 entry 8.4)",
        25: "the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 8.4)",
    },
    related=["6.1", "8.1", "8.5", "8.2", "6.4", "8.3"], tension=[],
    plain_meaning=(
        "The claimed status of monks and clergy, in scare-quotes in our own text -- 'few people "
        "will become monks and \"spiritual,\" because the Gospel is beginning to shine, and it "
        "reveals that \"spirituality\"' -- and the orders whose rules 'contradict Christ.'"
    ),
    false_friend=["'spiritual' heard as inward, devout, or non-material, rather than a claimed status we mock"],
    senses=dict(
        informational=(
            "'Few people will become monks and \"spiritual,\" because the Gospel is beginning to "
            "shine, and it reveals that \"spirituality\"' -- our own translator supplies the "
            "German lemma from the text itself, Geysterey. 'This one saying of Christ mightily "
            "condemns all orders and spiritual rules.' Our confession names the claim: 'the "
            "exalted title of being the spiritual life and the perfect life' -- and the works "
            "such a life produces, we say, are not 'as noble and good as if God should pick up a "
            "straw.'"
        ),
        evidential="Attested at the founder's own text, whose translator supplies the German lemma directly from what the text itself carries.",
        personal="We mock this claimed status openly, in scare-quotes, against which every calling stands equally holy.",
        translational="Do not hear 'spiritual' as inward devotion or non-materiality; we mean a claimed status over other Christians, mocked by us in scare-quotes.",
    ),
    quick_meaning="A claimed status of monks and clergy, mocked by us in scare-quotes -- against which every calling among us stands equally holy.",
    retrieve_when=["'spiritual' or 'spirituality' as a claimed monastic status"],
    do_not_retrieve_when=["the participant means the spiritual estate as a structural pairing (retrieve spiritual estate/temporal estate)"],
    doc06_tags="[AS][DR][TC]", ag_note="none",
),

dict(
    num="8.5", slug="perfection", tier=2, doc03_tier=2,
    world_word="perfection -- refused as a monastic rank, redefined as growth in one's own calling",
    world_word_plain="perfection",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented, weighted to Melanchthon -- the Augsburg Confession and, now, the Apology XXVII entire, this pass.",
    canon_cells=["F5-I"],
    rows=[20, 37, 38],
    row_loci={
        37: "the Augsburg Confession -- 'Christian perfection is to fear God from the heart, and yet to conceive great faith... and to serve our calling'",
        38: "the Apology XXVII, read entire this pass -- 'perfection is growth in the fear of God... and in devotion to one's calling'",
        20: "Secular Authority, cited among this entry's Registry rows (Doc_06 SS5 entry 8.5)",
    },
    related=["8.1", "8.4", "6.4", "2.3", "4.5", "2.4", "1.7"], tension=[],
    plain_meaning=(
        "The monastic claim to keep 'counsels' above the commandments and so to be in 'a state "
        "of perfection' -- refused and redefined: perfection is 'to fear God from the heart, "
        "and yet to conceive great faith... and to serve our calling.'"
    ),
    false_friend=["'perfection' heard as moral flawlessness, or as a spiritual elite's own achievement"],
    senses=dict(
        informational=(
            "Monks taught that their life kept 'not only the precepts, but also the so-called "
            "\"evangelical counsels,\"' a 'state of perfection.' We redefine it: 'Christian "
            "perfection is to fear God from the heart, and yet to conceive great faith... and "
            "meanwhile, to be diligent in outward good works, and to serve our calling.' 'They "
            "who believe and love the most are the perfect ones, whether outwardly they be male "
            "or female, prince or peasant, monk or layman.' The Apology adds the story of "
            "Anthony sent to a shoemaker who 'prayed in a few words for the entire state, and "
            "then attended to his trade.'"
        ),
        evidential="Weighted to the confessional voice -- the Augsburg Confession and the Apology XXVII, entire, this pass.",
        personal="Perfection for us is not an elite's achievement but growth in fear, faith and one's own calling -- the farmer's as much as any monk's.",
        translational="Do not hear 'perfection' as moral flawlessness or an elite's own rank: we mean growth in fear, faith and one's own calling -- the farmer's as much as the monk's, with no counsels above the commandments.",
    ),
    quick_meaning="Not moral flawlessness but growth in fear, faith and one's own calling -- the farmer's perfection as real as any monk's.",
    retrieve_when=["perfection, or 'evangelical counsels'"],
    do_not_retrieve_when=["the participant means vows specifically (retrieve vows)"],
    doc06_tags="[SC][DR][TC]", ag_note="weighted to Melanchthon",
),

dict(
    num="8.6", slug="fasting", tier=2, doc03_tier=3, promoted=True,
    world_word="fasting -- a free bodily discipline, refused only as a compelled 'must'",
    world_word_plain="fasting / meats",
    distortion_risk="high", weight="corroborating",
    formation_confidence="Documented",
    divergence_note="Documented at the household catechism and the confession's own defense; promoted from Doc_03's Tier 3 for its own paired Distortion Risk once fully developed.",
    canon_cells=["F5-P"],
    rows=[16, 25, 26, 37, 38],
    row_loci={
        26: "the Small Catechism -- fasting 'excellent disciplines for the body'",
        37: "the Augsburg Confession -- 'we do not condemn fasting in itself, but the traditions which prescribe certain days and certain meats'",
        38: "the Apology, read this pass -- bodily exercises to 'curb the flesh,' not to justify",
        16: "That Doctrines of Men Are to Be Rejected -- 'no one needs to pay butter-money or buy butter-letters'",
        25: "the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 8.6)",
    },
    related=["7.5", "3.4", "4.6", "5.11", "8.1"], tension=[],
    plain_meaning=(
        "Bodily discipline kept as 'free and voluntary, both as to the day and as to the food' "
        "-- 'excellent disciplines for the body' -- and refused only as commanded: 'it is "
        "allowable to eat milk, butter, eggs, cheese and meat every day... and no one needs to "
        "pay butter-money or buy butter-letters.'"
    ),
    false_friend=["assuming we abolished fasting, or made eating meat a badge of our own identity"],
    senses=dict(
        informational=(
            "'It is allowable to eat milk, butter, eggs, cheese and meat every day, whether it "
            "be Sunday or Friday, Lent or Advent; and no one needs to pay butter-money or buy "
            "butter-letters.' But the discipline itself is kept: 'fasting and other physical "
            "preparations are excellent disciplines for the body,' and 'we do not condemn "
            "fasting in itself, but the traditions which prescribe certain days and certain "
            "meats.' The Apology: exercises are undertaken 'not because they are services that "
            "justify, but in order to curb the flesh.' At the table the line is drawn by the "
            "neighbour: if it would harm you or you are sick, eat what you like, 'and if any one "
            "takes offence, let him be offended' -- but toward the weak, 'we must bear patiently "
            "with them and not use our liberty.'"
        ),
        evidential="Attested at both catechisms, the confession's own defense of the practice, and the Apology, read this pass.",
        personal="Fasting stays with us as a free bodily discipline against complacency, its calendar of required meats refused as a 'must,' and its actual use governed by the weak neighbour.",
        translational="Do not assume we abolished fasting or made eating meat a badge: we mean fasting kept as a free bodily discipline, the calendar of required meats refused, and the freedom to eat governed by the weak neighbour.",
    ),
    quick_meaning="Fasting kept as a free bodily discipline against complacency; the calendar of required meats refused as a compelled 'must.'",
    retrieve_when=["fasting, or meats and fast-days", "whether we abolished fasting"],
    do_not_retrieve_when=["the participant means Christian liberty broadly (retrieve 'must' and 'free')"],
    doc06_tags="[SC][RT][DR]", ag_note="none",
),

dict(
    num="8.7", slug="saints", tier=2, doc03_tier=2,
    world_word="saints -- remembered and imitated, never invoked; Christ alone the Mediator",
    world_word_plain="saints",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the household catechism's own catalogue and the confession's own refusal of invocation.",
    canon_cells=["F1-I"],
    rows=[2, 25, 30, 31, 37, 38],
    row_loci={
        25: "the Large Catechism -- 'if he was afraid of fire, he chose St. Lawrence as his helper in need'",
        37: "the Augsburg Confession -- 'the memory of saints may be set before us, that we may follow their faith and good works'",
        38: "the Apology, read this pass -- 'from invocation the next step was to images'",
        31: "the Table Talk -- 'Fie on thee, Leonard' (Contested as verbatim)",
        2: "the Ninety-Five Theses, cited among this entry's Registry rows (Doc_06 SS5 entry 8.7)",
        30: "Hymn V, cited among this entry's Registry rows (Doc_06 SS5 entry 8.7)",
    },
    related=["4.4", "3.6", "5.8", "8.8", "9.6", "3.4"], tension=[],
    plain_meaning=(
        "The saints as helpers in need -- 'if he was afraid of fire, he chose St. Lawrence as "
        "his helper in need' -- refused as invocation while 'the memory of saints may be set "
        "before us, that we may follow their faith and good works.'"
    ),
    false_friend=["assuming we rejected the saints outright, rather than refusing only their invocation"],
    senses=dict(
        informational=(
            "Our catechism's catalogue of the old way: 'if he was afraid of fire, he chose St. "
            "Lawrence as his helper in need; if he dreaded pestilence, he made a vow to St. "
            "Sebastian or Rochio' -- the trust that makes an idol. Our confession refuses the "
            "invocation and keeps the memory: Scripture 'teaches not the invocation of saints,' "
            "but 'the memory of saints may be set before us, that we may follow their faith and "
            "good works,' with Christ alone as Mediator. The Apology traces the decline: "
            "'mention of the saints seems to have been admitted with a design that is "
            "endurable... afterwards invocation followed... from invocation the next step was "
            "to images.'"
        ),
        evidential="Attested at the household catechism's own catalogue and the confession's refusal, with the Apology's own account of the decline.",
        personal="We remember and imitate the saints without asking anything of them -- the 'helper in need' replaced entirely by the one Mediator.",
        translational="Do not assume we rejected the saints outright; we mean the saints remembered and imitated, not invoked -- the 'helper in need' replaced by Christ alone.",
    ),
    quick_meaning="The saints remembered and imitated, never invoked -- the 'helper in need' replaced entirely by Christ, the one Mediator.",
    retrieve_when=["saints, or invocation of the saints"],
    do_not_retrieve_when=["the participant means Christ's own unique role specifically (retrieve Christ alone)"],
    doc06_tags="[SC][DR][RT]", ag_note="none",
),

dict(
    num="8.8", slug="images", tier=2, doc03_tier=3, promoted=True,
    world_word="images -- 'neither here nor there,' free to keep or remove, never by compulsion",
    world_word_plain="images",
    distortion_risk="high", weight="corroborating",
    formation_confidence="Documented",
    divergence_note="Documented at both voices (Apology 7610-7616, 8946, 9001, read this pass); promoted from Doc_03's Tier 3 once the Third and Fourth Sermons were read and gave it a real paired Distortion Risk.",
    canon_cells=["F5-I"],
    rows=[15, 16, 28, 38],
    row_loci={
        15: "the Third and Fourth Sermons -- 'images are neither here nor there, neither evil nor good, we may have them or not, as we please'",
        38: "the Apology, read this pass -- 'from invocation the next step was to images'",
        28: "the funeral preface -- costly shrines mocked against 'dead men's bones'",
        16: "That Doctrines of Men Are to Be Rejected, cited among this entry's Registry rows (Doc_06 SS5 entry 8.8)",
    },
    related=["7.5", "8.7", "3.4", "6.8", "5.5"], tension=[],
    plain_meaning=(
        "One of the 1522 'unnecessary things' -- 'we are free to have them or not'; 'neither "
        "here nor there, neither evil nor good' -- to be abolished 'if they are going to be "
        "worshiped, otherwise not,' and never by compulsion."
    ),
    false_friend=["assuming we smashed images, or forbade them outright"],
    senses=dict(
        informational=(
            "'Images are unnecessary, and we are free to have them or not, although it would be "
            "much better if we did not have them. I am not partial to them'; they 'ought to be "
            "abolished if they are going to be worshiped, otherwise not'; 'we would do better to "
            "give a poor man a gold-piece than to give God a golden image.' No compulsion or law "
            "must be made of leaving them. Our funeral preface mocks 'costly shrines of gold and "
            "silver, and images set with gems and jewels; but within are dead men's bones.' The "
            "Apology tells the same descent as saints: 'from invocation the next step was to "
            "images; these also were worshiped.'"
        ),
        evidential="Attested at both voices -- the Third and Fourth Sermons and the Apology, read this pass.",
        personal="A free thing among us -- the 1522 crisis's own test case, and the boundary against those who would remove images by force.",
        translational="Do not assume we smashed or forbade images outright: we mean images held indifferent, kept or removed freely, removed only where worshipped, and never by compulsion.",
    ),
    quick_meaning="Images held indifferent -- kept or removed freely, removed only where worshipped, and never by compulsion.",
    retrieve_when=["images, icons, or iconoclasm"],
    do_not_retrieve_when=["the participant means saints or their invocation as the primary subject (retrieve saints)"],
    doc06_tags="[SC][RT][DR]", ag_note="none -- both voices",
),

# ============================== Cluster 9 ==================================
# Comfort, trial, and death -- the pastoral register (Doc_06 5.9)
dict(
    num="9.1", slug="comfort", tier=2, doc03_tier=1, demoted=True,
    world_word="comfort -- 'the greatest consolation,' what the doctrine of faith brings",
    world_word_plain="comfort / consolation",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the confession's own opening statement and the Apology's own opening and closing of its chief article; the founder's dedicated consolation treatise (Fourteen of Consolation) remains unread.",
    canon_cells=["F1-P"],
    rows=[3, 15, 25, 27, 28, 37, 38],
    row_loci={
        37: "the Augsburg Confession -- 'consciences cannot be set at rest through any works, but only by faith'",
        38: "the Apology, opening and closing its chief article -- 'this alone brings sure and firm consolation to pious minds'",
        15: "the Eight Wittenberg Sermons -- the 'many absolutions' for 'comfort or strengthening for our conscience'",
        27: "the hymns -- 'his precious word assureth me; my solace, my sure rock is he'",
        3: "Concerning Baptism -- 'a gracious covenant of comfort'",
        28: "the funeral preface, cited among this entry's Registry rows (Doc_06 SS5 entry 9.1)",
    },
    related=["2.8", "9.3", "5.10", "2.5", "5.3", "9.4", "9.2"], tension=[],
    plain_meaning=(
        "What the doctrine of faith brings to anxious consciences -- 'the greatest consolation' "
        "-- and what absolution, baptism, the Supper and our burial hymns are all for."
    ),
    false_friend=["'comfort' heard as mere reassurance or emotional support rather than the setting-at-rest of an accused conscience"],
    senses=dict(
        informational=(
            "'God-fearing and anxious consciences find by experience that it brings the "
            "greatest consolation, because consciences cannot be set at rest through any works, "
            "but only by faith.' Our chief article opens on 'necessary and most abundant "
            "consolation to devout consciences' and closes, 'this alone brings sure and firm "
            "consolation to pious minds.' Our 'many absolutions' are for 'comfort or "
            "strengthening for our conscience'; baptism is 'a gracious covenant of comfort'; our "
            "hymn sings, 'his precious word assureth me; my solace, my sure rock is he.'"
        ),
        evidential="Attested at the confession's opening statement and the Apology's own chief article, both opened and closed on this word.",
        personal="This is what every sacrament and absolution exists to give us -- the setting-at-rest of a terrified conscience by a promise, not a feeling we work up ourselves.",
        translational="Do not hear 'comfort' as mere reassurance; we mean the setting-at-rest of a terrified conscience by a promise -- the thing every sacrament and absolution exists to give.",
    ),
    quick_meaning="'The greatest consolation' -- the setting-at-rest of a terrified conscience by a promise, which every sacrament and absolution exists to give.",
    retrieve_when=["comfort, or consolation", "what our whole doctrine is 'for'"],
    do_not_retrieve_when=["the participant means assurance/certainty specifically as a separate word (retrieve assurance)"],
    doc06_tags="[SC][DR][RT]", ag_note="none",
),

dict(
    num="9.2", slug="temptation", tier=2, doc03_tier=2,
    world_word="temptation -- Bekoerunge, three kinds: of the flesh, the world, and the devil",
    world_word_plain="temptation / trial",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the household catechism's own three-part definition, with the one original-language gloss the founder himself supplies for this word (Bekoerunge, LC 3632-3634).",
    canon_cells=["F5-P"],
    rows=[13, 15, 25, 26, 31, 38],
    row_loci={
        25: "the Large Catechism -- 'temptation, however, or (as our Saxons in olden times used to call it) Bekoerunge, is of three kinds'",
        26: "the Small Catechism -- praying against 'the Devil, the world and our bodily desires'",
        31: "the Table Talk -- 'need teacheth to pray' (Contested as verbatim)",
        38: "the Apology, read this pass -- faith 'nourished in a manifold way in temptations'",
        13: "Christian Liberty, cited among this entry's Registry rows (Doc_06 SS5 entry 9.2)",
        15: "the Eight Wittenberg Sermons, cited among this entry's Registry rows (Doc_06 SS5 entry 9.2)",
    },
    related=["4.7", "9.5", "9.1", "1.7", "9.4", "2.1"], tension=[],
    plain_meaning=(
        "The threefold assault our catechisms name -- 'of the flesh, of the world and of the "
        "devil' -- which no Christian escapes, and in which prayer and faith are learned: 'need "
        "teacheth to pray.'"
    ),
    false_friend=["'temptation' heard narrowly as the urge toward one specific sin"],
    senses=dict(
        informational=(
            "'Temptation, however, or (as our Saxons in olden times used to call it) "
            "Bekoerunge, is of three kinds, namely, of the flesh, of the world and of the "
            "devil' -- 'the young suffer especially from the flesh... they that attain to "
            "middle life and old age, from the world... strong Christians, from the devil.' "
            "'Without trouble, trials, and vexations, prayer cannot rightly be made... the "
            "common saying is \"need teacheth to pray.\"' Faith 'is nourished in a manifold way "
            "in temptations.'"
        ),
        evidential="Attested at both catechisms, the founder's own original-language gloss for this word, and the Apology, read this pass.",
        personal="A lifelong, age-graded assault in which faith and prayer are actually formed -- 'every one must fight his own battle.'",
        translational="Do not hear 'temptation' as one specific urge to sin; we mean a lifelong threefold assault -- flesh, world, devil -- expected at every age, in which faith and prayer are formed.",
    ),
    quick_meaning="A lifelong, threefold assault -- 'of the flesh, of the world and of the devil' -- in which prayer and faith are formed, not avoided.",
    retrieve_when=["temptation, or trial", "why hardship comes, in our own understanding"],
    do_not_retrieve_when=["the participant means the devil specifically as an agent (retrieve the devil)"],
    doc06_tags="[SC][DR][RT]", ag_note="none -- both voices",
),

dict(
    num="9.3", slug="assurance", tier=2, doc03_tier=1, demoted=True,
    world_word="assurance -- 'I cannot doubt I have a gracious God,' against praying 'conditionally'",
    world_word_plain="assurance / 'sure' / 'certain'",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at the confession's own logic of promise and the household's own prayer for certainty.",
    canon_cells=["F1-P"],
    rows=[2, 4, 6, 15, 26, 27, 31, 37, 38],
    row_loci={
        37: "the Augsburg Confession, cited among this entry's Registry rows (Doc_06 SS5 entry 9.3)",
        38: "the Apology, read this pass -- 'if the matter were to depend upon our merits, the promise would be uncertain and useless'",
        26: "the Small Catechism -- 'that I should be certain that such prayers are acceptable'",
        31: "the Table Talk -- 'we always prayed in Popedom conditionaliter, conditionally, and therefore uncertainly' (Contested as verbatim)",
        2: "the Ninety-Five Theses -- 'the assurance of salvation by letters of pardon is vain'",
        6: "Good Works, cited among this entry's Registry rows (Doc_06 SS5 entry 9.3)",
        27: "the hymns -- 'grief drove me to despair'",
        15: "the Eight Wittenberg Sermons, cited among this entry's Registry rows (Doc_06 SS5 entry 9.3)",
        4: "Discussion of Confession, cited among this entry's Registry rows (Doc_06 SS5 entry 9.3)",
    },
    related=["2.8", "2.2", "2.7", "9.1", "9.5", "1.1", "2.1", "1.2", "2.6"], tension=[],
    plain_meaning=(
        "The certainty we say our doctrine gives, which the old way withheld -- 'I cannot doubt "
        "I have a gracious God' -- against praying 'conditionally, and therefore uncertainly,' "
        "and against despair."
    ),
    false_friend=["'assurance' heard as self-confidence or presumption, rather than a certainty grounded outside the self"],
    senses=dict(
        informational=(
            "'The assurance of salvation by letters of pardon is vain.' The one who has taken "
            "the Sacrament 'cannot doubt I have a gracious God'; the household prays 'that I "
            "should be certain that such prayers are acceptable.' Our confession makes remission "
            "sure: 'if the matter were to depend upon our merits, the promise would be uncertain "
            "and useless, because we never could determine when we would have sufficient "
            "merit.' The old way is remembered as doubt: 'we always prayed in Popedom "
            "conditionaliter, conditionally, and therefore uncertainly.' The antonym is despair "
            "-- 'grief drove me to despair,' our own hymn sings."
        ),
        evidential="Attested at the founding Theses, both catechisms, the confession's own logic, and the founder's own hymn.",
        personal="This is the whole purpose of our doctrine, for us: a certainty grounded outside ourselves, in a promise 'that cannot fail or deceive me.'",
        translational="Do not hear 'assurance' as self-confidence or presumption; we mean a certainty grounded outside the self, in a promise, against the self-torture of endless doubt.",
    ),
    quick_meaning="The certainty our doctrine gives -- 'I cannot doubt I have a gracious God' -- against praying 'conditionally, and therefore uncertainly.'",
    retrieve_when=["assurance, or being 'sure'/'certain'", "the old way's doubt versus our own certainty"],
    do_not_retrieve_when=["the participant means comfort broadly rather than certainty specifically (retrieve comfort)"],
    doc06_tags="[SC][DR][RT]", ag_note="none",
),

dict(
    num="9.4", slug="death", tier=2, doc03_tier=2,
    world_word="death -- the last battle, fought alone, faith teaching us to call it sleep",
    world_word_plain="death",
    distortion_risk="high", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented for death as the terror faith overcomes, both voices (Apology 1439-1442, 5550, 8577-8579, read this pass); Luther-only for the sleep/burial register specifically.",
    canon_cells=["F1-P"],
    rows=[3, 15, 26, 28, 38],
    row_loci={
        15: "the Eight Wittenberg Sermons -- 'every one must fight his own battle with death by himself, alone'",
        28: "the 1542 funeral preface -- death 'as a deep, sound, sweet sleep,' 'no dirges nor lamentations, but comforting songs'",
        38: "the Apology, read this pass -- 'the terrors of sin and death must be overcome by faith'",
        26: "the Small Catechism -- praying for 'a blessed death'",
        3: "Concerning Baptism, cited among this entry's Registry rows (Doc_06 SS5 entry 9.4)",
    },
    related=["9.1", "9.2", "4.7", "4.9", "5.2", "1.5", "2.8"], tension=[],
    plain_meaning=(
        "The battle each of us must fight alone, which faith is to learn to despise 'as a deep, "
        "sound, sweet sleep,' buried with 'no dirges nor lamentations, but comforting songs,' in "
        "a churchyard renamed a resting-place."
    ),
    false_friend=["death heard as an end faced by private inner resolve, and burial heard as private grief"],
    senses=dict(
        informational=(
            "'The challenge of death comes to us all, and no one can die for another. Every one "
            "must fight his own battle with death by himself, alone.' Our founder's funeral "
            "preface: we 'should exercise and wont ourselves in faith to despise death, to look "
            "on it as a deep, sound, sweet sleep, the coffin no other than the bosom of our Lord "
            "Christ.' 'No dirges nor lamentations, but comforting songs'; churchyards named "
            "'Cemeteries,' 'resting and sleeping places' -- yet 'it is meet and right to give "
            "care and honor to the burial of the dead.'"
        ),
        evidential="Attested for death as the terror faith overcomes at both voices; the sleep and burial register is specifically the founder's own.",
        personal="The last battle, faced alone, on a text -- and a burial we sing, honour, and strip of masses for the soul.",
        translational="Do not hear death as faced by private inner resolve, or burial as private grief: we mean the last battle, faced alone but on a promise, a sleep and a couch, a burial sung and honoured.",
    ),
    quick_meaning="The last battle, fought alone, which faith teaches us to call 'a deep, sound, sweet sleep' -- buried with comforting songs, not lament.",
    retrieve_when=["death, or burial", "how we face death, or how we bury our dead"],
    do_not_retrieve_when=["the participant means purgatory specifically (retrieve purgatory)"],
    doc06_tags="[SC][DR][RT]", ag_note="none for death as the terror faith overcomes; Luther-only for the sleep/burial register",
),

dict(
    num="9.5", slug="prayer", tier=2, doc03_tier=2,
    world_word="prayer -- commanded as strictly as any commandment, promised an answer, given a form",
    world_word_plain="prayer",
    distortion_risk="medium", weight="load-bearing",
    formation_confidence="Documented",
    divergence_note="Documented at both voices; the one non-founder voice in our library speaks about this very practice (the household's own question about its own coldness in prayer).",
    canon_cells=["F5-P"],
    rows=[14, 15, 25, 26, 31, 37, 38],
    row_loci={
        25: "the Large Catechism, Third Part entire -- 'prayer is therefore as strictly and earnestly commanded as all other commandments'",
        26: "the Small Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 9.5)",
        31: "the Table Talk -- 'Sir! how is it, that in Popedom they pray so often with great vehemence, but we are very cold and careless in praying?' (Contested as verbatim)",
        37: "the Augsburg Confession -- 'he that knows that he has a Father gracious to him through Christ... calls upon God'",
        38: "the Apology, read this pass -- prayer 'most truly can be called a sacrament'",
        14: "the Kurze Form's own Lord's Prayer, unread by this build",
        15: "the Eight Wittenberg Sermons, cited among this entry's Registry rows (Doc_06 SS5 entry 9.5)",
    },
    related=["4.8", "4.2", "4.1", "2.7", "9.3", "9.2", "4.7", "7.4", "6.9", "9.7"], tension=[],
    plain_meaning=(
        "Commanded as strictly as any commandment, promised an answer, and given its form in "
        "the Lord's Prayer -- the household's daily frame, the community's own 'wall of iron,' "
        "and the practice whose own coldness we report of ourselves."
    ),
    false_friend=["prayer heard as spontaneous, private, optional devotion, with set forms as lesser"],
    senses=dict(
        informational=(
            "'Prayer is therefore as strictly and earnestly commanded as all other "
            "commandments'; it has a promise -- 'at Thy commandment and promise, which cannot "
            "fail or deceive me' -- and a given form, since 'God anticipates us, and Himself "
            "arranges the words and form of prayer for us.' It is our community's own defense: "
            "'the prayer of a few godly men intervened like a wall of iron on our side.' Its old "
            "form was doubt: 'we always prayed in Popedom conditionaliter.' And the one sentence "
            "we have from the household's other side is about it: 'Sir! how is it, that in "
            "Popedom they pray so often with great vehemence, but we are very cold and careless "
            "in praying?'"
        ),
        evidential="Attested at both voices, and by the one non-founder voice in our whole library, who asks a question about this very practice.",
        personal="Prayer is our community's own defense and the household's frame -- and, by our own report, the one practice we ourselves confess we hold coldly.",
        translational="Do not hear prayer as spontaneous, optional devotion with set forms as lesser: we mean a commanded duty with a promised answer and a given form -- and a practice whose own coldness we report about ourselves.",
    ),
    quick_meaning="Commanded as strictly as any commandment, promised an answer, given its form in the Lord's Prayer -- our own community's 'wall of iron.'",
    retrieve_when=["prayer, or the Lord's Prayer", "whether prayer must follow a set form"],
    do_not_retrieve_when=["the participant means temptation as the occasion for prayer specifically (retrieve temptation)"],
    doc06_tags="[SC][RT]", ag_note="none -- both voices; the one non-founder voice in the library is about this very practice",
),

dict(
    num="9.6", slug="martyr", tier=3, doc03_tier=3,
    world_word="martyr -- 'the two youths,' our one martyrology, 'true priests of God's own making'",
    world_word_plain="martyr",
    distortion_risk="medium", weight="illustrative",
    formation_confidence="Documented",
    divergence_note="Documented at a single hymn, single register, in a translator's English -- the weakest evidentiary base of any entry in our whole lexicon, disclosed plainly.",
    canon_cells=["F1-P"],
    rows=[30],
    row_loci={30: "Hymn V -- 'two young monks... burnt at Brussels by the Sophists of Louvain'"},
    related=["6.2", "8.7"], tension=[],
    plain_meaning=(
        "Our library's one martyrology -- two young monks, 'John' and 'Henry,' 'burnt at "
        "Brussels by the Sophists of Louvain,' who 'for God's dear Word... shed their blood' "
        "and, stripped of 'monkish garb,' were made 'true priests of God's own making.'"
    ),
    false_friend=["hearing this as a martyr-cult, or as a bare fact-record, rather than a ballad naming what faithfulness under ultimate pressure looks like to us"],
    senses=dict(
        informational="Our hymn's own heading names two young monks 'burnt at Brussels by the Sophists of Louvain,' who 'for God's dear Word... shed their blood,' and, stripped of 'monkish garb,' were made 'true priests of God's own making.'",
        evidential="A single hymn, a single register, in one translator's English -- the weakest evidentiary base of any term we hold.",
        personal="This ballad is our one statement of what a faithful life looks like under ultimate pressure.",
        translational="Do not hear this as a martyr-cult or a bare record; we mean a ballad, our own one statement of faithfulness under ultimate pressure.",
    ),
    quick_meaning="Our one martyr ballad -- two young monks burnt at Brussels, stripped of their habits, made 'true priests of God's own making.'",
    retrieve_when=["martyrs, or the two youths burnt at Brussels"],
    do_not_retrieve_when=["the participant wants a broader account of persecution among us -- our library holds only this one ballad"],
    doc06_tags="[SC][RT]", ag_note="Luther-only, single-register (Hymn V), in a translator's English -- the weakest evidentiary base of any entry",
),

dict(
    num="9.7", slug="patience", tier=3, doc03_tier=3,
    world_word="patience -- the fourth of the 1522 sermon's 'chief things'; a whole life's own patience",
    world_word_plain="patience",
    distortion_risk="low", weight="illustrative",
    formation_confidence="Documented",
    divergence_note="Documented for the word generally, both voices (Apology 1524, 2545, 4506, read this pass); the household sentence naming it 'my whole life' is the founder's own.",
    canon_cells=["F5-P"],
    rows=[15, 25, 31, 38],
    row_loci={
        15: "the Eight Wittenberg Sermons -- 'patience works and produces hope,' 'have patience with him for a time'",
        31: "the Table Talk -- 'the patiences are so many, that my whole life is nothing but patience' (Contested as verbatim)",
        38: "the Apology, read this pass -- patience among the fruits of the Spirit",
        25: "the Large Catechism, cited among this entry's Registry rows (Doc_06 SS5 entry 9.7)",
    },
    related=["7.5", "8.3", "9.5"], tension=[],
    plain_meaning="The fourth of our 1522 sermon's 'chief things' -- the strong's bearing with the weak -- a fruit of the Spirit in our confession's own lists, and our founder's own household confession: 'my whole life is nothing but patience.'",
    false_friend=["'patience' heard as a mere temperament rather than the whole shape of a formed life -- persecution, pace, and marriage together"],
    senses=dict(
        informational="'Patience works and produces hope'; 'have patience with him for a time, suffer his weakness and help him bear it.' Our confession lists it among the fruits of the Spirit; our own founder's household confession names it the whole of a life: 'the patiences are so many, that my whole life is nothing but patience.'",
        evidential="Attested at the 1522 sermons, the Apology's own list of the Spirit's fruits, and the founder's own household saying.",
        personal="This word carries the whole of a formed life for us -- persecution borne, pace kept with the weak, and marriage endured together.",
        translational="Do not hear 'patience' as mere temperament; we mean the whole shape of a formed life -- persecution, pace with the weak, and marriage -- named 'nothing but patience.'",
    ),
    quick_meaning="The strong's own bearing with the weak, and a fruit of the Spirit -- our founder's own word for the whole of a formed life: 'nothing but patience.'",
    retrieve_when=["patience"],
    do_not_retrieve_when=["the participant means bearing with the weak specifically inside liberty (retrieve 'must' and 'free')"],
    doc06_tags="[SC][RT]", ag_note="none for the word; the household sentence is the founder's own",
),
]  # END TERMS


def build_confidence(t: dict) -> dict:
    """MECHANICAL assembly (see module docstring: the branch-selection is
    the one authored judgment; the assembly itself is fixed). citation_
    specificity is 'A' uniformly -- every quotation in every entry below
    carries a precise locus (a line range in a named vendored file), per
    Doc_06's own Discipline 4 and its script-verified quotation base
    (§10). verification_state is 'verified-via-authority' uniformly, not
    'verified-direct': this authoring pass relied on Doc_06's own report
    that it re-ran every quotation against the ten vendored files by
    script after drafting (§10), rather than re-opening the ten files
    itself -- an honest distinction the B-1 script's own confidence
    builder already draws for source records citing an unopened file."""
    return {
        "citation_specificity": "A",
        "verification_state": "verified-via-authority",
        "evidentiary_weight": t["weight"],
        "formation_confidence": t["formation_confidence"],
        "divergence_note": t["divergence_note"],
    }


def build_sources(t: dict) -> list[dict]:
    """MECHANICAL: resolves each cited Registry row to its real witt.
    source.* id via ROW_TO_ID; the per-row locus text is AUTHORED (each
    term's own `row_loci` dict, composed from Doc_06's own Key Sources/Key
    Texts lines for that entry)."""
    out = []
    for row in t["rows"]:
        out.append({
            "source_id": ROW_TO_ID[row],
            "locus": t["row_loci"].get(row, f"per Doc_06 §5 entry {t['num']}'s own Key Sources line"),
            "license": "public-domain",
        })
    return out


def build_relations_initial(t: dict) -> list[dict]:
    """AUTHORED content (which terms relate, and how), MECHANICAL lookup
    (num -> slug via SLUG_BY_NUM). Default associated-with; tension-with
    only where `tension` names the target."""
    rels = []
    for num in t.get("tension", []):
        rels.append({"type": "tension-with", "target": f"witt.term.{SLUG_BY_NUM[num]}"})
    for num in t.get("related", []):
        if num in t.get("tension", []):
            continue
        rels.append({"type": "associated-with", "target": f"witt.term.{SLUG_BY_NUM[num]}"})
    return rels


def close_reciprocity(records: dict[str, dict]) -> None:
    """MECHANICAL, structural only -- no content judgment. For every
    relation A --type--> B this batch authored, ensures B carries the
    declared inverse back to A (associated-with and tension-with are both
    symmetric, per engine/m1/schemas.py RELATION_INVERSE, so the back-edge
    added here is always the SAME type, never inferred or reinterpreted).
    This closes engine/m1/gates.py's gate_reciprocity by construction
    within this batch of 72 records. It is explicitly NOT Doc_06's own
    §7 reconciliation pass (which read every one-directional edge and
    judged, by hand, whether the target's own content actually
    presupposes the link before adding it) -- see the module docstring's
    disclosed-scope item 1. Mutates `records` in place."""
    inverse = {"associated-with": "associated-with", "tension-with": "tension-with"}
    for rid, rec in list(records.items()):
        for rel in list(rec.get("relations") or []):
            target = rel["target"]
            inv_type = inverse.get(rel["type"])
            if inv_type is None or target not in records:
                continue
            target_rec = records[target]
            already = any(
                r.get("type") == inv_type and r.get("target") == rid
                for r in (target_rec.get("relations") or [])
            )
            if not already:
                target_rec.setdefault("relations", []).append({"type": inv_type, "target": rid})


def build_body(t: dict) -> str:
    """MECHANICAL assembly of an AUTHORED-once-per-term citation line,
    following gallic.term.*'s own body-note pattern (build provenance,
    below the closing fence, never in frontmatter)."""
    lines = [
        f"Built from Doc_06 §5 entry {t['num']} ({t['world_word_plain']}, "
        + (
            f"Tier {t['tier']} ↑ from Doc_03's estimate of {t['doc03_tier']}"
            if t.get("promoted")
            else f"Tier {t['tier']} ↓ from Doc_03's estimate of {t['doc03_tier']}"
            if t.get("demoted")
            else f"Tier {t['tier']}, confirmed at Doc_03's own estimate"
        )
        + f"). Register emic. Doc_06 tags: {t['doc06_tags']}. "
        f"Author Gravity: {t['ag_note']}. Source Registry rows cited: "
        f"{', '.join('R' + str(r) for r in t['rows'])}. "
        f"Quotations carried from Doc_06's own script-verified base (§10), not independently "
        f"re-opened against the vendored files by this authoring pass."
    ]
    if t.get("ct"):
        lines.append(t["ct"])
    if t.get("res"):
        lines.append(
            "Reported-Experience Status (Doc_06 §5 entry " + t["num"] + "): " + t["res"]
        )
    lines.append(
        "Relations above are this batch's own reading of Doc_06's own Related Terms line for "
        "this entry, closed for structural reciprocity by this script's close_reciprocity() "
        "(see module docstring, disclosed-scope item 1) -- not Doc_06's own §7 candidate-"
        "return-link reconciliation pass, which was not separately re-run here."
    )
    if t.get("note"):
        lines.append(t["note"])
    return "\n\n".join(lines)


# AUTHORED, added in a second pass after the first run of engine/m1/gates.py's
# gate_readability flagged 90 findings: the original plain_meaning/quick_meaning
# prose above (composed to read well as connected paragraphs, with quoted
# phrases and em-dash/semicolon-linked clauses) scored above FK_CEILING=10 on
# many terms -- gate_readability's own fk_grade() (engine/m1/fk.py) splits
# sentences ONLY on '.', '!', '?', so a long, semicolon- or dash-linked
# sentence counts as one very long sentence for the formula, regardless of
# how it would actually be read aloud. This is a genuine readability defect
# in the original text, not a false positive: CLAUDE.md's own accessibility
# standard (short sentences, ~12-20 words average) asks for exactly the
# short, plain-period sentences this override supplies, and only for the two
# fields the gate and the runtime actually compile into short, spoken
# blurbs (plain_meaning, quick_meaning) -- the four senses.* fields, which
# the gate does not check, keep their original fuller, quotation-dense prose
# unchanged, since Level 2/3 depth there is exactly what this build's scope
# decision calls for. AUTHORED content (a genuine rewrite, not a mechanical
# transform), stored by slug so build_record() can substitute it in place of
# each term's own original two fields.
READABILITY_OVERRIDES: dict[str, dict[str, str]] = {
    "indulgence": dict(
        plain_meaning="An indulgence is a letter that once promised less penalty for sin, in exchange for money. We do not sell these anymore. By 1517 we were already arguing against the whole trade.",
        quick_meaning="A paid letter promising less penalty for sin. We attacked this practice in 1517. By 1529 it was only a memory.",
    ),
    "repentance": dict(
        plain_meaning="Repentance is not one ritual handled by a priest. It is a whole life turned toward God. It has two parts: fear under God's Law, then trust in his promise.",
        quick_meaning="A whole-life turning, not a single ritual. First comes fear under the Law. Then comes trust in the promise.",
    ),
    "contrition": dict(
        plain_meaning="Contrition is sorrow for sin. Sorrow alone means nothing to us. It only counts when faith stands beside it.",
        quick_meaning="Sorrow for sin. Worthless to us without faith.",
    ),
    "satisfaction": dict(
        plain_meaning="One word carries two very different things for us. Our own satisfaction for sin does nothing, and we refuse it. Christ's satisfaction for our sins is enough, and we rest on that alone.",
        quick_meaning="One word, two things: ours, refused; Christ's, enough.",
    ),
    "purgatory": dict(
        plain_meaning="In 1517 we still argued about purgatory. By 1531 we said Scripture does not teach it. By 1542 we buried our dead without it.",
        quick_meaning="A belief we reasoned with early on, then denied, then dropped from our own burials.",
    ),
    "the-keys": dict(
        plain_meaning="The keys are Christ's own words to forgive or hold sin. They belong to the whole community, not to one man. Using them is not a show of power. It is a promise spoken to comfort someone.",
        quick_meaning="Christ's own words to forgive sin, held by the whole community, not by one man.",
    ),
    "the-cross": dict(
        plain_meaning="The cross is suffering God sends us, not suffering we choose. Our baptism enrolls us under this banner. We fight sin our whole life under it.",
        quick_meaning="Suffering God sends, not suffering we choose. Our baptism's own banner.",
    ),
    "faith": dict(
        plain_meaning="Faith is trust that holds onto God's own promise. It is not simply believing a story is true. This trust alone makes us right with God, apart from our works. But faith never stands on nothing. It rests on the Word and the sacraments.",
        quick_meaning="Trust that holds God's promise. It alone makes us right with God, and it always rests on something outside us.",
    ),
    "justification": dict(
        plain_meaning="Justification is God's act of naming a sinner righteous. In the same breath, God also makes that sinner righteous. Both happen through faith, for Christ's sake alone. This is the center of our whole teaching.",
        quick_meaning="God's act of naming us righteous, and of making us so, through faith, for Christ's sake.",
    ),
    "good-works": dict(
        plain_meaning="Good works are not just prayer, fasting, and giving alms. They are ordinary things done in faith: working, walking, eating, sleeping. We do them because God commands them, never to earn anything.",
        quick_meaning="Ordinary life, done in faith. Commanded by God, never a way to earn favor.",
    ),
    "merit": dict(
        plain_meaning="Merit is what we deny to every human work. No one earns grace by their own effort. Only Christ has merit, and we rest on his alone.",
        quick_meaning="What no human work can earn. Only Christ has merit.",
    ),
    "grace": dict(
        plain_meaning="Grace is God's free favor toward us. We do not earn it or deserve it. Faith receives it, and at the altar we say, 'I cannot doubt I have a gracious God.'",
        quick_meaning="God's free favor, not earned. Received by faith alone.",
    ),
    "law-and-gospel": dict(
        plain_meaning="We read all of Scripture as two kinds of speech. The Law commands what we ought to do, but gives no power to do it. The Gospel promises what the Law demands. First comes the diagnosis, then the cure.",
        quick_meaning="Scripture as command and promise. First the diagnosis, then the cure.",
    ),
    "promise-and-testament": dict(
        plain_meaning="A promise is God's own word, given first, before we do anything. At the altar, that promise is a testament: a gift left by someone about to die. We simply receive it. We never offer it back to God as a sacrifice.",
        quick_meaning="God's word, given first. At the altar, a gift we receive, never a sacrifice we offer.",
    ),
    "conscience": dict(
        plain_meaning="Conscience is the inner court where our whole teaching plays out. Under God's Law, it feels terror. Under God's promise, it finds comfort. It is not a guide that tells us right from wrong. It is a court that stands accused, then is set free.",
        quick_meaning="The inner court terrified by the Law and comforted by the promise. Not a guide -- a court.",
    ),
    "free-will": dict(
        plain_meaning="Our will is free enough to choose ordinary, civil good. But it cannot choose the righteousness God asks for. Only the Holy Spirit gives that power. We argued this hard against Erasmus.",
        quick_meaning="Free to choose ordinary good. Powerless, on its own, to reach God.",
    ),
    "sin": dict(
        plain_meaning="Sin, for us, is not one bad act. It is a condition we are born into: no fear of God, no trust in God, and disordered desire. Only faith answers it.",
        quick_meaning="An inherited condition, not one bad act. No fear, no trust in God. Faith alone answers it.",
    ),
    "the-word": dict(
        plain_meaning="The Word is God's own speech, the Gospel of Christ. It is the one thing we truly need. Joined to water or bread, it makes a sacrament. It even does the work of reform on its own, while we simply preach it.",
        quick_meaning="God's own speech. It makes our sacraments, and does the work of reform on its own.",
    ),
    "gospel": dict(
        plain_meaning="The Gospel is the good news of Christ. We call it the true treasure of the church. We believe this treasure was buried for a time, and that it has now risen again in our own day.",
        quick_meaning="The good news of Christ: forgiveness for his sake. Our own treasure, risen again.",
    ),
    "scripture-against-tradition": dict(
        plain_meaning="Scripture judges every other writing, including popes, councils, and church fathers. We say this two ways. Our founder says it sharply: the Bible had been left to gather dust. Our confession says it more gently, alongside the wider church.",
        quick_meaning="Scripture judges popes, councils, and fathers. Said sharply by one voice, gently by another.",
    ),
    "doctrines-of-men": dict(
        plain_meaning="Doctrines of men are rules people made up and then bound on the conscience. We do not reject every human custom. We reject only the ones that claim to earn grace, or that force belief.",
        quick_meaning="Human rules bound on the conscience. Rejected only when they claim to earn grace.",
    ),
    "letter-and-spirit": dict(
        plain_meaning="We do not believe Scripture hides a secret meaning under its plain words. The plain sense is the spiritual sense. A clear text is what a Christian must stand on.",
        quick_meaning="The plain sense of Scripture is the spiritual sense. No hidden layer beneath it.",
    ),
    "christ-alone": dict(
        plain_meaning="Christ alone is our teacher and our mediator. We do not listen to saints or scholars instead of him. Every page of Scripture points to him.",
        quick_meaning="Christ alone: our one teacher, our one mediator.",
    ),
    "catechism": dict(
        plain_meaning="The catechism is instruction every Christian needs: the Ten Commandments, the Creed, and the Lord's Prayer. Together they hold everything in Scripture. Every household says them daily, for life. No one ever outgrows them, not even our founder.",
        quick_meaning="The three parts every Christian must know, said daily for life. Never outgrown, never finished.",
    ),
    "household": dict(
        plain_meaning="The household is where our catechism is taught. A father questions his family and servants every week. He leads prayer three times a day. This is how ordinary people learn the faith.",
        quick_meaning="The house where the catechism is taught: father, wife, children, servants, examined weekly.",
    ),
    "what-does-this-mean": dict(
        plain_meaning="This question follows every part of our catechism. It asks a child to explain what a teaching means, not just to repeat it from memory.",
        quick_meaning="The question after every part of our catechism. Not memory. Meaning.",
    ),
    "to-have-a-god-is-to-trust": dict(
        plain_meaning="Our catechism teaches that a god is whatever we trust for good in hard times. To have a god simply means to trust something completely. Whatever the heart clings to for help, that is its true god.",
        quick_meaning="A god is whatever the heart trusts for good. To have a god is simply to trust.",
    ),
    "fear-and-love-god": dict(
        plain_meaning="Every commandment in our catechism opens with the same words: we must fear and love God. This ties each commandment back to trust, the First Commandment's own lesson.",
        quick_meaning="The formula opening every commandment: fear and love God. It always returns to trust.",
    ),
    "neighbor": dict(
        plain_meaning="The neighbor is the specific person the second half of the Commandments protects: their body, their property, their good name. Our own freedom must never harm this person.",
        quick_meaning="The specific person the Commandments protect. Our freedom must never harm them.",
    ),
    "the-devil": dict(
        plain_meaning="The devil is a real, personal enemy, not a figure of speech. We name him in every part of our life: sermon, hymn, prayer, and confession. The Word, our sacraments, and our catechism are all daily defenses against him.",
        quick_meaning="A real, personal enemy. Our Word, sacraments, and catechism are our daily defense.",
    ),
    "daily": dict(
        plain_meaning="Our catechism sets a daily rhythm. We pray at rising, at meals, and at night. Baptism drowns our old self daily. Forgiveness is renewed daily too.",
        quick_meaning="The rhythm our catechism sets: prayer at rising, at meals, at night. Renewed every day.",
    ),
    "hymn": dict(
        plain_meaning="Hymns are songs in our own language, written to teach ordinary people who cannot read Latin. We sing them at work, at burial, and inside our services. Old tunes often carry new, Christian words.",
        quick_meaning="Songs in our own language, teaching those who cannot read Latin.",
    ),
    "sacrament": dict(
        plain_meaning="A sacrament is God's promise joined to a visible sign, like water or bread. We count two, or three counting confession, never seven. None of them work for us without faith.",
        quick_meaning="God's promise joined to a visible sign. Two or three, never seven. Useless without faith.",
    ),
    "baptism": dict(
        plain_meaning="Baptism is water joined to God's own command and word. It marks a death that lasts our whole life: our old self drowned, a new self rising daily. It also makes us all priests.",
        quick_meaning="Water joined to God's word. A death begun once, renewed every day.",
    ),
    "sacrament-of-the-altar": dict(
        plain_meaning="At this table, Christ's body and blood are truly present, in and under bread and wine. We do not explain how. We simply take him at his word. This meal feeds us for our daily struggle.",
        quick_meaning="Christ's body and blood, truly present, given for us. Food for our daily struggle.",
    ),
    "given-for-you": dict(
        plain_meaning="These two words carry the whole benefit of the Supper: forgiveness given for you, personally. They demand a heart that actually believes them.",
        quick_meaning="Two words. They carry the Supper's whole benefit: forgiveness, given for you.",
    ),
    "both-kinds": dict(
        plain_meaning="Both kinds means bread and cup together for everyone at the table, not bread alone for ordinary people. We call it Christ's own command. Still, we would not force it on anyone by law.",
        quick_meaning="Bread and cup together for everyone. Christ's command, never a forced law.",
    ),
    "the-mass": dict(
        plain_meaning="We kept the mass, but changed what it means. It is God's promise of forgiveness, never a sacrifice we offer back to God. We ended private masses and kept public worship, with great reverence.",
        quick_meaning="Kept as God's promise, refused as a sacrifice. Private masses ended; public worship remains.",
    ),
    "transubstantiation": dict(
        plain_meaning="We call this a monstrous word for a monstrous idea. We refuse to explain how Christ is present in the bread. We simply trust that he is.",
        quick_meaning="A monstrous word, we say. We trust the presence; we do not explain it.",
    ),
    "congregation": dict(
        plain_meaning="Our congregation is not a building. It is an assembly of believers gathered around the Word and the sacraments. We know each other by these marks, not by any building or office.",
        quick_meaning="An assembly, not a building. Known by the Word and the sacraments rightly held.",
    ),
    "the-ban": dict(
        plain_meaning="The ban excludes someone from our table, never from God's own mercy. We use it only to correct, and only by speaking the Word, never by force.",
        quick_meaning="Exclusion from the table, for correction, by the Word alone, never by force.",
    ),
    "confession-and-absolution": dict(
        plain_meaning="Confession has two parts: admitting our sin, then hearing forgiveness as though from God himself. We treasure this practice. We never force it, and we never demand a full list of every sin.",
        quick_meaning="Admitting sin, then hearing forgiveness as though from God himself. A treasured comfort.",
    ),
    "worthy-unworthy": dict(
        plain_meaning="Worthiness at the table means simply believing the words 'given for you.' The truly unworthy are people who feel no need for forgiveness at all. We examine people on the three parts before they come, but we never force anyone.",
        quick_meaning="Worthiness means believing the words 'given for you,' not being sinless.",
    ),
    "spiritual-and-temporal-estate": dict(
        plain_meaning="We once divided Christians into a spiritual estate, clergy, and a temporal one, everyone else. We call this a pure invention. Instead, we say every station -- marriage, parenthood, ruling -- is equally holy.",
        quick_meaning="A division we call pure invention. Every station of life is equally holy.",
    ),
    "we-are-all-priests": dict(
        plain_meaning="Baptism makes every one of us a priest. There is no rank among us, only different tasks. A father is a priest in his own home. Still, no one may preach in public without being properly called.",
        quick_meaning="Baptism makes every believer a priest. Public preaching still needs a proper call.",
    ),
    "office": dict(
        plain_meaning="An office is a task, not a permanent rank. A pastor removed from office becomes an ordinary person again, like anyone else. Every trade has its own office too.",
        quick_meaning="A task held for a time, never a permanent rank.",
    ),
    "calling": dict(
        plain_meaning="A calling is any station God gives us: father, mother, ruler, or preacher. None of these is holier than the rest. For preaching specifically, we also require a proper, public call.",
        quick_meaning="A God-given station. Father, ruler, or preacher. None holier than another.",
    ),
    "pastor": dict(
        plain_meaning="A pastor is called and usually married. Our own catechism openly rebukes lazy pastors. We also say a congregation owes its pastor honor and a decent living.",
        quick_meaning="A called, married leader. We honor him. We also rebuke him, in print, when lazy.",
    ),
    "christendom": dict(
        plain_meaning="Christendom is our word for the whole body of Christians, wider than any single pope's approval. It even includes believers outside Rome's own confirmation. We say it cannot be reduced to one man.",
        quick_meaning="The whole body of Christians, wider than Rome's own confirmation.",
    ),
    "pope-and-antichrist": dict(
        plain_meaning="We name the pope two ways. In our sharp preaching, we call him Antichrist. In our formal confession before the Emperor, we call him only the Church of Rome. Both names point to the same adversary.",
        quick_meaning="The same adversary, named two ways: 'Antichrist' in preaching, 'the Church of Rome' in confession.",
    ),
    "sects-and-new-spirits": dict(
        plain_meaning="We call the radicals new spirits, fanatics, or enthusiasts. Our specific charge against them is this: they claim the Spirit apart from God's own external Word. Our confession names the Anabaptists directly.",
        quick_meaning="Our own names for the radicals, charged with claiming the Spirit apart from the Word.",
    ),
    "the-turk": dict(
        plain_meaning="We name the Turk as an outside enemy, alongside the pope and unbelief. Our household simply prays against him. We give no other account of him.",
        quick_meaning="An outside enemy we pray against, one of the devil's own instruments.",
    ),
    "the-two-governments": dict(
        plain_meaning="God rules us two ways. Through the Word, he rules the spiritual kingdom, and makes us Christians. Through the sword, he rules the civil kingdom, and restrains evil. We keep both, and confuse neither with the other.",
        quick_meaning="God's two rules: the Word governs Christians, the sword restrains evil. Never confused.",
    ),
    "the-sword": dict(
        plain_meaning="The sword is the civil ruler's own power to punish evil and protect the good. God gave it, not the church. Even the pope himself stands under it.",
        quick_meaning="The ruler's power to punish evil. God's own gift, never the church's.",
    ),
    "obedience": dict(
        plain_meaning="We owe obedience to parents and rulers as though to God himself. This obedience has one limit: we never obey when we are told to sin.",
        quick_meaning="Obedience owed to parents and rulers, limited only when they command sin.",
    ),
    "insurrection": dict(
        plain_meaning="In 1522, common people were angry, and we understood why. Still, we refused violence and trusted God to watch over his own Word. This describes only that one year, not our later history.",
        quick_meaning="Our 1522 stance: sympathy for real grievance, but a refusal of violence.",
    ),
    "must-and-free": dict(
        plain_meaning="Faith is a 'must' that never bends. Everything else is 'free,' ours to use or not. We measure our freedom by love for the weaker believer beside us. Freedom, for us, is never simply doing as we please.",
        quick_meaning="Faith never bends. Everything else is free, measured by love for the weak.",
    ),
    "vows": dict(
        plain_meaning="We honor lawful vows, freely made. We reject vows forced on people, or ones that claim to earn forgiveness. No vow can override God's own command.",
        quick_meaning="We honor free, lawful vows. We reject forced ones, or vows that claim to earn merit.",
    ),
    "chastity": dict(
        plain_meaning="For us, true chastity means marriage for nearly everyone. We say the monastic vow of celibacy is, for most people, actually unchaste. Only a few are given a special gift for the single life.",
        quick_meaning="True chastity, we say, is marriage for nearly everyone.",
    ),
    "marriage": dict(
        plain_meaning="Marriage is the most common estate, and, we say, the noblest one too. God ordained it at creation, before any monk's vow existed. Our own pastors are married. Priests were once killed simply for marrying.",
        quick_meaning="The most common and, we say, the noblest estate. Ordained by God at creation.",
    ),
    "spiritual-geysterey": dict(
        plain_meaning="We mock the old claim that monks and clergy hold a special 'spiritual' status. Every calling, we say, is equally holy in God's eyes.",
        quick_meaning="A claimed clergy status we mock. Every calling is equally holy.",
    ),
    "perfection": dict(
        plain_meaning="We reject the old idea that monks reach a higher, more perfect life. True perfection, for us, means growing in faith while doing our own ordinary work.",
        quick_meaning="Not a monk's higher life, but growth in faith within one's own ordinary work.",
    ),
    "fasting": dict(
        plain_meaning="We keep fasting as a free, useful discipline for the body. We reject any law that forces certain foods on certain days. Love for our weaker neighbor still guides how we use this freedom.",
        quick_meaning="A free bodily discipline, kept freely; forced food-laws, refused.",
    ),
    "saints": dict(
        plain_meaning="We remember the saints and try to follow their example. We do not pray to them for help. Christ alone is our mediator.",
        quick_meaning="Remembered and imitated, never prayed to. Christ alone is our mediator.",
    ),
    "images": dict(
        plain_meaning="Images in worship are neither commanded nor forbidden, for us. We may keep them or remove them freely. We remove them only where people begin to worship them, and never by force.",
        quick_meaning="Neither commanded nor forbidden. Kept or removed freely, never by force.",
    ),
    "comfort": dict(
        plain_meaning="Comfort is what faith gives to a troubled conscience. No amount of good works can give this rest. Only faith in God's promise can.",
        quick_meaning="What faith gives a troubled conscience. Never earned by works.",
    ),
    "temptation": dict(
        plain_meaning="Our catechism names three kinds of temptation: the flesh, the world, and the devil. Every age faces its own kind. Need itself, we say, teaches us to pray.",
        quick_meaning="Three kinds we name: flesh, world, devil. Need itself teaches us to pray.",
    ),
    "assurance": dict(
        plain_meaning="We say faith gives real certainty, not endless doubt. Under the old way, people prayed only 'if it be God's will,' never sure. We say instead, 'I cannot doubt I have a gracious God.'",
        quick_meaning="Real certainty from faith, not endless doubt. 'I cannot doubt I have a gracious God.'",
    ),
    "death": dict(
        plain_meaning="Death is a battle each of us must face alone. Faith teaches us to call it a deep, sweet sleep. We bury our dead with comfort, not despair.",
        quick_meaning="A battle faced alone. Faith teaches us to call it a sweet sleep.",
    ),
    "prayer": dict(
        plain_meaning="Prayer is commanded, just like any other commandment. God even gives us its very words in the Lord's Prayer. We confess, honestly, that we often pray too coldly.",
        quick_meaning="Commanded, not optional. God even gives us its own words.",
    ),
    "martyr": dict(
        plain_meaning="We tell of two young monks burned for their faith. Stripped of their monkish robes, we say, they became true priests, made by God alone.",
        quick_meaning="Two young monks burned for their faith, made priests by God alone.",
    ),
    "patience": dict(
        plain_meaning="Patience means bearing with a weaker believer, and bearing with life's own hardships. Our own founder once said his whole life was nothing but patience.",
        quick_meaning="Bearing with the weak, and with life itself. 'My whole life is nothing but patience.'",
    ),
}


def build_record(t: dict) -> dict:
    override = READABILITY_OVERRIDES.get(t["slug"], {})
    payload = {
        "id": f"witt.term.{t['slug']}",
        "world_id": WORLD_ID,
        "record_type": "term",
        "schema_version": 2,
        "status": "draft",
        "register": "emic",
        "canon_cells": t["canon_cells"],
        "confidence": build_confidence(t),
        "sources": build_sources(t),
        "retrieval": {
            "tier": t["tier"],
            "retrieve_when": t["retrieve_when"],
            "do_not_retrieve_when": t["do_not_retrieve_when"],
        },
        "relations": build_relations_initial(t),
        "plain_meaning": override.get("plain_meaning", t["plain_meaning"]),
        "world_word": t["world_word"],
        "false_friend": t["false_friend"],
        "senses": t["senses"],
        "quick_meaning": override.get("quick_meaning", t["quick_meaning"]),
        "distortion_risk": t["distortion_risk"],
    }
    if t.get("prior_sense"):
        payload["prior_sense"] = t["prior_sense"]
    return payload


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    assert len(TERMS) == 72, f"expected 72 terms, found {len(TERMS)}"
    records: dict[str, dict] = {}
    for t in TERMS:
        records[f"witt.term.{t['slug']}"] = build_record(t)
    close_reciprocity(records)
    written = []
    for t in TERMS:
        rid = f"witt.term.{t['slug']}"
        payload = records[rid]
        body = build_body(t)
        front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
        text = f"---\n{front}---\n{body.strip()}\n"
        path = OUT_DIR / f"{rid}.md"
        path.write_text(text, encoding="utf-8")
        written.append(str(path))
    print(f"Wrote {len(written)} term records:")
    for p in written:
        print(f"  {p}")


if __name__ == "__main__":
    main()
