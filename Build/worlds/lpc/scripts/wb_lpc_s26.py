"""B-6 (S2.1), lpc equivalent: Latin Pastoral-Congregational Christianity
(`lpc`) contested_claim records.

WHAT THIS SCRIPT DOES. Produces this world's first `contested_claim`
records under records/lpc/contested_claim/, per the live schema
(engine/m1/schemas.py TYPE_PROPERTIES["contested_claim"]: claim, held_against,
concedes, divergence_partners -- confirmed by direct read this session, not
assumed) and gate battery (engine/m1/gates.py COMPLETION_REQUIRED
["contested_claim"] = ["claim", "held_against", "concedes"], confirmed by
direct read this session; divergence_partners is NOT gate-required but is
authored on every record below anyway, matching the fleet's own good-practice
convention). This is B-6 of the 9-step record-native build pipeline (B-1
through B-9); B-1 through B-5 (207 source + world_core records, 19 term
records, 7 story/figure/quote records, 8 gravity/17 force records) are
already done, committed, and merged. Read Build/worlds/lpc/scripts/wb_lpc_s21.py,
wb_lpc_s22.py, wb_lpc_s24.py and wb_lpc_s25.py in full before this script was
written (not touched by them, not re-run by this script) for lpc-specific
docstring/code-pattern discipline, and Build/worlds/don/scripts/wb_don_s26.py in
full this session as the direct methodological precedent for this record
type specifically (its own MECHANICAL-vs-AUTHORED, RECIPROCITY and PRIMARY-
GRAVITY COVERAGE technique all carried over here), alongside three fleet
worked examples read in full this session: records/pahc/contested_claim/
pahc.contested.two-strand-packaging.md, records/hal/contested_claim/
hal.contested.chronology.md, and records/desert/contested_claim/
desert.contested.antony-literacy.md.

WHAT COUNTS AS A CONTESTED CLAIM HERE, per don's own script (its own launch
brief and the three worked examples) and this world's own Doc_06 §3, which
draws the identical line independently: a genuine scholarly or textual
dispute (a manuscript/recension question, an authorship or attribution
question, a historiographical question turning on which reading is
credited) -- never simply two sides of this world's own in-world doctrinal
argument, which the gravities and any future doctrinal_witness records
already carry. Doc_06 §3 states this exactly: "Article 26 and LDF Part II
restrict [CT] to live scholarly contest within the relevant subfield, not
in-world disagreement... two bishops answering the rebaptism question
oppositely, confessors against their bishop, two incompatible conciliar
formulas. None of that is [CT]." This script does not build a
contested_claim record for any of those in-world disagreements (including
G5's own Egalitarian-vs-Hierarchical divergence, already carried on
lpc.gravity.conciliar-authority-theory's own confidence.divergence_note, and
explicitly NOT [CT] per Doc_03 §row for "bishop of bishops"/"plenary
Council").

CANDIDATES IDENTIFIED, checked directly against this world's own build
record rather than assumed:
  - Doc_03_Lexicon_Candidate_List.md's own [CT] legend (§ "Tags") states
    plainly: "[CT] is applied below only to 'compel them to come in'...,
    to 'grace'..., and to 'schism'... It is not applied to 'bishop of
    bishops,' 'plenary Council,' 'heresy,' or 'the one episcopate'..." --
    three terms, and Doc_06 §3 confirms "No term is added to or removed
    from that set." This script therefore builds one contested_claim
    record per term, the same 1-per-CT-term ratio don's own script found
    for its own single CT-tagged term (Circumcellion/Agonistici).
  - Doc_09_Story_Inventory.md's own Story Index (row lpcstory006, "The
    death of Cyprian," Tier 3, Confidence Contested) plus the chunk's own
    Tier Justification section, which states at full strength a genuine,
    currently-unresolved genre-classification contest ("A reasonable
    builder could argue Tier 1 here... Which clause governs when they
    point opposite ways is a Construction Framework question, not a
    question this build can settle") -- carried as an open escalation at
    Doc_09 §8 item 7 and NOT disposed of by the document's own
    Approved-to-proceed disposition ("the escalation at §8 item 7... remains
    open and is not disposed of by this approval"). This is not a [CT]
    term -- it is a genuine, textually-attested, currently-open dispute
    over how to classify one piece of already-built material, exactly
    the shape don's own don.contested.cirta-reserved-to-the-lord record
    took from a story chunk's own Usage Guidance rather than from a [CT]
    tag. Four records total, matching don's own four-record scope.

CANDIDATES CONSIDERED AND DECLINED, with reasoning (per this step's own
launch-brief discipline against silent gaps):
  - **Doc_02 §8's own "Contested" confidence-map items.** Three named
    there: (1) the extent of Punic/Berber substrate influence on ordinary
    congregational life -- an evidentiary-thinness finding (the record is
    silent on how much, not two named readings pulling apart), the same
    shape don's own script declined for Tyconius's formal standing, not
    a contested_claim's shape; (2) whether the lapsed-reconciliation
    gravity persists "in a different register" under Augustine or has
    lapsed -- Doc_01 §4-§5's own disclosed interpretive lean, closer to
    pahc's own "two-strand packaging" provisional-frame shape than to a
    scholarly dispute, and not built here for the same reason pahc's own
    record is the one already-built fleet precedent for that different
    shape, not this one; (3) Cyprian's egalitarian vs. Augustine's
    hierarchical conciliar-authority formula -- explicitly named by
    Doc_03 §"Tags" as in-world disagreement, NOT [CT], and already
    carried in full on lpc.gravity.conciliar-authority-theory's own
    confidence.divergence_note (G5). Building a contested_claim record
    from it here would duplicate that record's own already-reviewed
    field rather than adding a genuine second one.
  - **The Acta Proconsularia / Pontius's own Life pointer (Doc_09 §6 item 2,
    §8 item 1; lpcstory006's own Absent Story Note).** A documented absence (the
    Acta is vendored in Latin only and has not been read), not two named
    readings of a text both sides have -- the correct instrument for an
    absence of this shape is the existing honest_limit-style disclosure
    already carried on lpc.story.the-death-of-cyprian's own sources[]
    entry and Absent Story Note, not a fifth contested_claim record.

PRIMARY-GRAVITY COVERAGE, checked directly against Doc_04's own text rather
than assumed to require one record per Primary gravity (per don's own
script's own discipline): this world's four Primary gravities are G1
(Pastoral Office as Territorial Flock-Keeping), G2 (Penitential Discipline),
G3 (Collegial Communion Preserved), G6 (Sacramental/Ordination Validity).
None of the four records below relates directly to G1, G2, G3, or G6 --
checked, not an oversight. The De Unitate recension question (record 1)
bears on the Supporting term "schism," and Doc_01 §7/Doc_05 §"distinctive
interpretive object" both state directly that nothing in this world's own
construction rests on the disputed passage (De Unitate 5's episcopatus unus
est predates the Stephen controversy by design, per Doc_01's own finding);
the grace/Pelagius contest (record 2) bears on G7 (Supporting); the compel-
coercion contest (record 3) bears on a force Doc_04 §2 explicitly declined
to advance as a gravity at all; the Cyprian's-death genre contest (record 4)
bears on G1 and G8 only through the existing story record's own relations,
not through a fresh gravity-level claim this script makes. Net: zero of
this world's four Primary gravities receive a contested_claim via this
script, and that is a checked finding (no CT term or open escalation this
session's direct reads surfaced touches any Primary gravity's own extent,
dating, or character), not an unexamined gap -- matching the shape, though
not the specific outcome, of don's own PRIMARY-GRAVITY COVERAGE finding that
two of its four Primaries (G3, G5) received none either.

INPUTS, mapped to OUTPUTS, precisely:
  - Doc_01_World_Identification_Boundaries_Orientation.md's own "Episcopatus
    unus est (De Unitate 5) is not Cyprian's own answer to Stephen" paragraph
    (naming the two-recension "Primacy Text" question), Doc_03's own row 3
    (schism, [CT], "the genuine, named, unresolved textual-scholarship
    question... at row 3"), Doc_05's own "distinctive interpretive object"
    section, Doc_06 §3's own contest-type specification ("Application to
    this world, secondarily Historical scope... The North African case is
    the field's central example"), and records/lpc/term/lpc.term.schism.md's
    own already-authored, already-reviewed senses.informational paragraph
    -> `lpc.contested.de-unitate-recensions`. A genuine, three-generation,
    named-scholar textual/manuscript dispute over which of two surviving
    recensions of De Unitate 4-5 is prior (Chapman 1902-03 first identified
    and argued the interpolation thesis; van den Eynde 1933 restated the
    double-edition question; Bévenot's 1971 critical edition is this
    world's own Registry's named instrument for closing it, not yet read by
    this build) -- unlike don's own bishop-count record, this one remains
    genuinely, currently open; this script does not resolve it.
  - Doc_03's own row for "grace" ([CT], "Relationship to present-day
    traditions, secondarily Meaning"), Doc_06 §3's own contest-type
    specification, and records/lpc/term/lpc.term.grace.md's own already-
    authored senses.informational closing paragraph -> `lpc.contested.
    grace-pelagius-characterization`. A live historiographical contest over
    whether Augustine's own anti-Pelagian polemic accurately characterizes
    the position Pelagius himself held, refracted further through
    Reformation-era and later Catholic/Protestant appropriation of the
    same texts.
  - Doc_03's own row for "compel them to come in" ([CT], "Relationship to
    present-day traditions, secondarily Meaning"), Doc_06 §3's own contest-
    type specification, and records/lpc/term/lpc.term.compel-them-to-come-
    in.md's own already-authored senses.informational closing paragraph ->
    `lpc.contested.compel-coercion-development`. The single most-cited
    patristic warrant in the modern historiography of religious coercion --
    contested on how far the position is the ancestor of later inquisitorial
    practice, how far the pastoral-correction framing should be credited,
    and whether the three-phase development is a genuine change of mind or
    a retrospective self-presentation.
  - Doc_09_Story_Inventory.md's own Story Index row for lpcstory006, its own
    §8 item 7 (escalation carried open through Approval), and Story-Chunks/
    lpcstory006_the-death-of-cyprian.md's own Tier Justification section in
    full (read this session) -> `lpc.contested.cyprian-death-genre`. Whether
    Pontius's own eyewitness-deacon account of Cyprian's execution (Life
    §§15-19) is best classified by CF V7.4's Tier 1 genus clause (direct
    documentation by a named eyewitness) or by its Tier 3 hagiographic-
    convention clause (the Zacchaeus typology, the providential intervention
    at the climax) -- a live, unresolved, project-lead-reserved question
    this record documents rather than settles.

MECHANICAL vs AUTHORED, field by field (matching don's own script's own
discipline exactly):
  - id, world_id, record_type, schema_version, status, register,
    canon_cells: MECHANICAL. register="etic" throughout, matching don's own
    choice and all three fleet worked examples -- a contested_claim record
    states and weighs a scholarly or textual disagreement in this build's
    own analytic voice, not a formation participant's first-person voice.
    Confirmed directly against engine/m1/gates.py this session:
    "contested_claim" appears in neither _PERSPECTIVE_FIELDS nor
    _ATTRIBUTION_FIELDS (unchanged from don's own script's own finding, no
    schema/gate drift found on direct re-check). canon_cells=[] throughout
    -- this world has no canon work done yet (no records/lpc/canon_question/
    directory exists), matching every prior lpc record built so far.
  - claim, held_against, concedes: AUTHORED, each re-derived from a specific,
    cited section of Doc_01/03/05/06/09, a specific Story-Chunk file, or a
    specific already-built term record's own senses.informational field
    (never from this session's own outside knowledge of patristic
    historiography) -- see INPUTS above for the exact source each record
    draws on.
  - confidence.evidentiary_weight: "contested" throughout -- the schema's
    own dedicated value for exactly this record type's own subject matter,
    matching don's own script and all three fleet worked examples.
  - confidence.formation_confidence: "Contested" throughout, matching don's
    own script and two of the three fleet worked examples (hal, desert)
    rather than pahc's own "Inferential-Thin" -- each of this script's four
    records names a genuine, currently-unresolved reading contest as its
    own subject, not a single settled-but-thin fact.
  - confidence.divergence_note: null throughout, matching don's own script's
    own house rule for this record type -- the divergence IS the claim/
    held_against/concedes triad itself; a separate prose divergence_note
    would restate what those three fields already carry in full.
  - confidence.citation_specificity: "B" for de-unitate-recensions and
    grace-pelagius-characterization (each rests on this world's own already-
    completed Doc_03/Doc_06/term-record synthesis of a named-scholar or
    named-controversy contest, not this session's own fresh direct read of
    Chapman/van den Eynde/Bévenot or of Pelagius's own fragmentary corpus,
    neither vendored); "A" for compel-coercion-development (Letter 185 and
    Letter XCIII are both directly quoted and re-verified in this world's
    own already-built lpc.term.compel-them-to-come-in record, which this
    record draws on directly); "B" for cyprian-death-genre (rests on this
    world's own already-completed Doc_09 Tier Justification synthesis of
    Delehaye's genre scholarship, not a fresh direct read of Delehaye
    himself this session).
  - confidence.verification_state: "verified-via-authority" throughout --
    this script relies on Doc_01/03/05/06/09's and the existing lpc.term.*/
    lpc.story.* records' own already-completed, independently-reviewed
    research, not on this session re-opening the raw vendored primary
    texts or the in-copyright secondary literature itself, matching the
    identical distinction don's own script draws for its own non-quote
    records.
  - sources[] / divergence_partners[]: AUTHORED per record, resolved to the
    specific lpc.source.* ids (checked directly against records/lpc/source/,
    never guessed) that ground each side of the contest. divergence_partners
    names the real source ids whose ACCOUNTS diverge, per don's own script's
    own launch-instruction discipline, contrasted with cappadocian's and
    ijc's own misuse of the field as free prose -- not repeated here either.
  - relations[]: AUTHORED per record, "associated-with" throughout, matching
    don's own script and all three fleet worked examples' own choice of the
    one symmetric relation type over a directional pair, for the identical
    reason don's own docstring gives (several of these contested_claim<->
    term/gravity/force/story connections state a "bears on" or "is the same
    material read a different way" relationship, not a strict precondition
    or a single named tension-pole pair).

RECIPROCITY, applied per don's own script's own precedent (if a
contested_claim relates to an existing record via relations[], close the
inverse on that record too). Four existing records/lpc/{term,gravity,force,
story}/*.md files receive one added relations[] entry each, applied directly
by targeted edit after this script ran -- NOT regenerated by this script
itself, and not listed among the file paths this script writes, for the
identical reason don's own docstring gives (these are already-built,
already-committed, already-reviewed B-1 through B-5 records this step's own
scope does not authorize rewriting wholesale for a small additive change):
  - lpc.term.schism.md <- lpc.contested.de-unitate-recensions
  - lpc.term.grace.md AND lpc.gravity.grace-and-human-incapacity.md (G7) <-
    lpc.contested.grace-pelagius-characterization
  - lpc.term.compel-them-to-come-in.md AND lpc.force.illegal-to-established-
    shift.md <- lpc.contested.compel-coercion-development
  - lpc.story.the-death-of-cyprian.md <- lpc.contested.cyprian-death-genre

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells; touch records/lpc/{source,
world_core,term,story,figure,quote,search_record,gravity,force}/ (existing
B-1 through B-5 records are read only, for their own lpc.source.*/lpc.term.*/
lpc.gravity.*/lpc.force.* ids, never edited by this script itself -- the
four small reciprocal edits above are applied separately, by hand, after
this script runs); resolve the De Unitate recension question, the Pelagius-
characterization question, the compel-coercion historiographical question,
or the Cyprian's-death Tier 1/Tier 3 governance question in either
direction -- all four remain exactly as open as this world's own build
record already found them; build a contested_claim record for any in-world
disagreement between Cyprian and Augustine, per Doc_03's and Doc_06's own
explicit exclusion of that shape from [CT]; run the M2 compiler; register
`lpc` in records/worlds.yaml (B-9).
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

# Existing record ids this script's own relations[] point at (read only --
# see RECIPROCITY above for how the inverse edge is actually applied).
TERM_SCHISM = "lpc.term.schism"
TERM_GRACE = "lpc.term.grace"
TERM_COMPEL = "lpc.term.compel-them-to-come-in"
G7 = "lpc.gravity.grace-and-human-incapacity"
FORCE_SHIFT = "lpc.force.illegal-to-established-shift"
STORY_DEATH = "lpc.story.the-death-of-cyprian"


def conf(cite, verify, weight, formation, divergence=None):
    return {
        "citation_specificity": cite,
        "verification_state": verify,
        "evidentiary_weight": weight,
        "formation_confidence": formation,
        "divergence_note": divergence,
    }


def src(*items):
    """Each item is (source_id, locus) for a public-domain source, or
    (source_id, locus, None) to omit the license key entirely -- the
    correct fleet precedent (desert.contested.antony-literacy.md) for an
    in-copyright, consultation-only secondary source, rather than
    asserting a false "public-domain" value the source's own record
    explicitly contradicts."""
    out = []
    for item in items:
        sid, locus, *rest = item
        entry = {"source_id": sid, "locus": locus}
        if not rest:
            entry["license"] = "public-domain"
        elif rest[0] is not None:
            entry["license"] = rest[0]
        out.append(entry)
    return out


def rel(*targets):
    return [{"type": "associated-with", "target": t} for t in targets]


def _write(rid: str, payload: dict, body: str) -> None:
    out_dir = RECORDS_ROOT / "contested_claim"
    out_dir.mkdir(parents=True, exist_ok=True)
    front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    text = f"---\n{front}---\n{body.strip()}\n"
    path = out_dir / f"{rid}.md"
    path.write_text(text, encoding="utf-8")
    WRITTEN.append(str(path))


def emit(rid, claim, held_against, concedes, divergence_partners, confidence,
          sources, relations, body):
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "contested_claim",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "etic",
        "canon_cells": [],
        "confidence": confidence,
        "sources": sources,
        "relations": relations,
        "claim": claim,
        "held_against": held_against,
        "concedes": concedes,
        "divergence_partners": divergence_partners,
    }
    _write(rid, payload, body)


# ===========================================================================
# 1. DE UNITATE 4-5's TWO-RECENSION QUESTION ("the Primacy Text")
# ===========================================================================

def build_de_unitate_recensions() -> None:
    emit(
        "lpc.contested.de-unitate-recensions",
        claim=(
            "De Unitate 4-5 survives in a single authorial text. One form of chapters 4-5 is "
            "often called the 'Primacy Text'. It reads more kindly toward Roman primacy than the "
            "other form does. It is a later interpolation. A later hand added it to the words "
            "Cyprian first wrote. It is not evidence of anything Cyprian himself wrote or revised."
        ),
        held_against=[
            "Chapman's own foundational study (1902-03) first identified and argued the interpolation "
            "thesis at length, but the question he opened has not, on this world's own Registry's own "
            "account, been closed by scholarly consensus in the seven decades since -- van den Eynde's "
            "1933 restatement of the 'double edition' question shows the matter still argued three "
            "decades later, and this world's own Doc_03 (row 3) still carries it as 'a further, "
            "separately unresolved transmission fact,' not a settled interpolation finding.",
            "An alternative reading -- that Cyprian himself authored both recensions, at different "
            "moments or for different audiences, rather than one being a later hand's addition to the "
            "other -- remains live specifically because the instrument this world's own Registry names "
            "as capable of closing the question, Bévenot's 1971 Oxford critical edition (row 51), has "
            "not been read by this build: naming the edition does not itself close the question, per "
            "that source record's own divergence_note, which states this directly rather than implying "
            "resolution from acquisition alone.",
            "Whichever recension is prior, the passage in question (De Unitate 5's episcopatus unus "
            "est) is not, on this world's own Doc_01 finding, Cyprian's own answer to the later Stephen "
            "rebaptism controversy at all -- it predates that controversy by four to five years -- so "
            "a reading that treats either recension as evidence of Cyprian's own considered position on "
            "conciliar primacy specifically, rather than on schism and the one episcopate in general, "
            "risks importing a later dispute's own stakes into a passage written before that dispute "
            "existed.",
        ],
        concedes=(
            "That the treatise addresses schism and the one episcopate, and that it was written amid "
            "the Novatianist and Felicissimus crises around 251, is not in dispute -- this world's own "
            "Registry (row 3) licenses De Unitate for exactly that general subject matter, independent "
            "of which recension of chapters 4-5 is read. What remains genuinely open, and what this "
            "record does not resolve in either direction, is the recension question itself: this "
            "world's own construction (Doc_01, Doc_05) states plainly that nothing in its own reasoning "
            "rests on either recension's own specific wording, draws only on the treatise's general, "
            "undisputed subject matter, and names the recension question exactly as Doc_03 §'Tags' "
            "frames it -- a genuine, named, unresolved textual-scholarship contest, not a settled fact "
            "this record can report either way."
        ),
        divergence_partners=[
            "lpc.source.chapman-les-interpolations-dans-le-traite-de-unitate",
            "lpc.source.van-den-eynde-double-edition-de-unitate",
            "lpc.source.bevenot-de-lapsis-and-de-unitate-critical-edition",
        ],
        confidence=conf("B", "verified-via-authority", "contested", "Contested"),
        sources=src(
            ("lpc.source.cyprian-de-unitate",
             "the classic treatise on schism and the one episcopate; De Unitate 4-5, the disputed "
             "passage; De Unitate 5's episcopatus unus est, written c. 251, four to five years before "
             "the Stephen controversy"),
            ("lpc.source.chapman-les-interpolations-dans-le-traite-de-unitate",
             "the foundational 1902-03 study first identifying and arguing the two-recension "
             "interpolation thesis", None),
            ("lpc.source.van-den-eynde-double-edition-de-unitate",
             "'La double édition du De unitate de S. Cyprien' (1933), restating the textual problem "
             "three decades after Chapman", None),
            ("lpc.source.bevenot-de-lapsis-and-de-unitate-critical-edition",
             "the 1971 Oxford critical edition named by this world's own Registry as the instrument "
             "that would resolve which recension is prior -- not yet read by this build", None),
        ),
        relations=rel(TERM_SCHISM),
        body=(
            "Re-derived from Doc_01_World_Identification_Boundaries_Orientation.md's own 'Episcopatus "
            "unus est (De Unitate 5) is not Cyprian's own answer to Stephen' paragraph, Doc_03_Lexicon_"
            "Candidate_List.md's own row 3 (schism, [CT]), Doc_05_Ecological_Reconstruction.md's own "
            "'distinctive interpretive object' section, Doc_06_Full_Lexicon_Development.md §3's own "
            "contest-type specification ('Application to this world, secondarily Historical scope'), "
            "and records/lpc/term/lpc.term.schism.md's own already-authored senses.informational "
            "paragraph, all read directly this session. relations[] carries one term edge (lpc.term."
            "schism) named in this script's own docstring under RECIPROCITY -- not to any Primary "
            "gravity, per this script's own docstring, PRIMARY-GRAVITY COVERAGE (Doc_01 and Doc_05 both "
            "state directly that nothing in this world's own construction rests on the disputed "
            "passage). Unlike don.contested.bishop-count-411-conference, this contest remains genuinely, "
            "currently open -- this record does not adjudicate which recension is prior."
        ),
    )


# ===========================================================================
# 2. GRACE -- AUGUSTINE'S ANTI-PELAGIAN POLEMIC vs. WHAT PELAGIUS HELD
# ===========================================================================

def build_grace_pelagius() -> None:
    emit(
        "lpc.contested.grace-pelagius-characterization",
        claim=(
            "Augustine's own anti-Pelagian writings show what Pelagius himself held. They show "
            "it as it was. Pelagius held that a believer's own moral effort, with no help, is "
            "enough to obey what God commands. Later Catholics and Protestants used this same "
            "dispute to take opposing sides on grace and merit. They did so in the Reformation "
            "era and in modern times. Their use carries on an argument. Augustine himself set its "
            "terms correctly."
        ),
        held_against=[
            "This world's own build record names, without adjudicating it, a live modern scholarly "
            "reassessment of 'whether the position we argue against is the one Pelagius himself actually "
            "held' (records/lpc/term/lpc.term.grace.md, senses.informational) -- the entire evidentiary "
            "base for this world's own construction of the controversy is one voice (Augustine) within "
            "one evidence stream (his own anti-Pelagian corpus), and no Pelagian first-person answer "
            "survives in this world's own Native record to check that characterization against.",
            "The Reformation-era and later Catholic/Protestant appropriations of this same vocabulary "
            "('grace,' 'merit,' 'sufficiency') ran their own disputes through readings of Augustine that "
            "did not always distinguish what Augustine himself argued from what later controversialists "
            "needed him to have argued -- a listener arriving with this word today is, per this world's "
            "own lexicon entry, 'very often arriving from inside one of those later arguments,' not this "
            "world's own fifth-century one, which complicates treating the modern sense of the dispute "
            "as a straightforward continuation of Augustine's own original argument with Pelagius.",
            "Augustine's own anti-Pelagian corpus is itself polemical literature, written to win a "
            "sustained argument against a named living opponent -- the genre most likely, on this "
            "world's own general evidentiary discipline (Author Gravity), to sharpen or simplify an "
            "opponent's position for rhetorical effect, a risk this record names rather than assumes "
            "away simply because the corpus is Native and richly attested.",
        ],
        concedes=(
            "That Augustine argued this position, at length, across thirteen dedicated works, against a "
            "named opponent, is Documented at the highest confidence this world's own Registry assigns "
            "-- the anti-Pelagian corpus's own raw-frequency count for 'grace' (1,798 occurrences) is, "
            "by a wide margin, the single highest of any term in this world's own lexicon, and every "
            "quotation grounding this world's own construction is directly re-verified against that "
            "corpus. What this record does not resolve, and what this world's own build record "
            "consistently declines to characterize, is Pelagius's own actual position independent of "
            "Augustine's report of it, or how fairly the Reformation-era and modern reception of the "
            "controversy has continued Augustine's own terms rather than a later argument's own "
            "terms -- both genuinely open questions this world's own already-reviewed lexicon entry "
            "names and does not adjudicate, and which this record carries forward rather than settles."
        ),
        divergence_partners=[
            "lpc.source.augustine-anti-pelagian-corpus",
        ],
        confidence=conf("B", "verified-via-authority", "contested", "Contested"),
        sources=src(
            ("lpc.source.augustine-anti-pelagian-corpus",
             "the whole evidentiary base for this world's own construction of the controversy; a full "
             "sweep, scoped to its own thirteen works, returns 1,798 raw occurrences of 'grace' (1,665 "
             "markup-stripped) -- the single highest raw-frequency count in this world's own lexicon"),
        ),
        relations=rel(TERM_GRACE, G7),
        body=(
            "Re-derived from Doc_03_Lexicon_Candidate_List.md's own row for 'grace' ([CT], "
            "'Relationship to present-day traditions, secondarily Meaning'), Doc_06_Full_Lexicon_"
            "Development.md §3's own contest-type specification, and records/lpc/term/lpc.term.grace.md's "
            "own already-authored, already-reviewed senses.informational closing paragraph, all read "
            "directly this session. relations[] carries one term edge (lpc.term.grace) and one Supporting "
            "gravity edge (G7, lpc.gravity.grace-and-human-incapacity) named in this script's own "
            "docstring under RECIPROCITY -- not to any Primary gravity, per PRIMARY-GRAVITY COVERAGE "
            "above. This record does not characterize Pelagius's own position, adopt either side of the "
            "Reformation-era reception dispute, or adjudicate the historiographical reassessment "
            "question -- it names the contest, per this world's own already-reviewed term record's own "
            "explicit restraint on exactly this point."
        ),
    )


# ===========================================================================
# 3. "COMPEL THEM TO COME IN" -- CHANGE OF MIND OR RETROSPECTIVE
#    SELF-PRESENTATION?
# ===========================================================================

def build_compel_coercion() -> None:
    emit(
        "lpc.contested.compel-coercion-development",
        claim=(
            "Augustine's views on coercion developed in three phases. First, he held an early "
            "opinion against any compulsion (Letter XCIII §17). Next, he made a narrow and "
            "unsuccessful request for legal protection (Letter 185 §§25-26, earlier in his own "
            "time as bishop). Last, he gave a sustained defence of compulsion that was already "
            "in force. All this records a genuine change of mind. It came from his pastoral "
            "experience of the Donatist schism. It was not a story he told about himself in "
            "hindsight. Such a story would make a settled practice look like the result of "
            "principled rethinking."
        ),
        held_against=[
            "This world's own already-reviewed lexicon entry names, without adjudicating it, the live "
            "modern historiographical question of 'whether the three-phase development is a genuine "
            "change of mind or a retrospective self-presentation' (records/lpc/term/lpc.term.compel-"
            "them-to-come-in.md, senses.informational) -- every attestation of the earlier, contrary "
            "opinion reaches this world's own record only through Augustine's own later retrospective "
            "account of it (Letter XCIII §17), written after the later position was already argued, not "
            "through a surviving contemporaneous statement of the earlier view from the time he is said "
            "to have held it.",
            "This doctrine is known in this world's own corpus only through Augustine's own advocacy, in "
            "his own defence, with no Donatist first-person answer surviving in this world's own Native "
            "record -- he writes, on this world's own Doc_02 §2 finding, 'from a position of increasing "
            "institutional confidence relative to Donatism specifically,' which sharpens rather than "
            "dilutes the risk that the earlier-opinion account was shaped, in the telling, by the "
            "argument it now serves.",
            "The modern historiography of religious coercion treats this same warrant as the most-cited "
            "patristic ancestor of later inquisitorial practice -- a reception history this record does "
            "not adjudicate, but which this world's own lexicon entry names as running 'over how far "
            "this position is the ancestor of later inquisitorial practice, how far our own framing as "
            "pastoral correction should be credited,' a question genuinely distinct from, and not "
            "settled by, the three-phase sequence's own internal consistency.",
        ],
        concedes=(
            "The three-phase sequence itself -- Letter XCIII §17's own retrospective account of an "
            "earlier opinion; Letter 185 §§25-26's own narrow, unsuccessful solicitation of legal "
            "protection early in Augustine's episcopate; and the later, sustained defence -- is "
            "Documented and directly re-verified in this world's own already-built lexicon entry, which "
            "this world's own construction (Doc_01) is explicitly bound against compressing into one "
            "position. Cyprian's own corpus contains nothing corresponding to any phase of this "
            "development at all, since the controversy postdates him entirely. What remains genuinely "
            "open, and what this record does not resolve, is the two historiographical questions this "
            "world's own lexicon entry names and declines to adjudicate: whether the sequence itself "
            "records a real change of mind or a retrospective self-presentation, and how far the "
            "pastoral-correction framing should be credited against the reception history that reads "
            "this position as an ancestor of later coercive practice."
        ),
        divergence_partners=[
            "lpc.source.augustine-correction-of-the-donatists",
            "lpc.source.augustine-letter-93-to-vincentius",
        ],
        confidence=conf("A", "verified-via-authority", "contested", "Contested"),
        sources=src(
            ("lpc.source.augustine-correction-of-the-donatists",
             "Letter 185, §§25-26, the imperial-coercion defence, directly quoted and re-verified"),
            ("lpc.source.augustine-letter-93-to-vincentius",
             "Letter XCIII, §17, the retrospective account of the earlier, contrary opinion, directly "
             "quoted and re-verified"),
            ("lpc.source.shaw-sacred-violence",
             "the standard modern treatment of the Donatist/Circumcellion violence Augustine's own "
             "coercion argument responds to -- background context for the coercive-capacity axis, not "
             "itself evidence of this world's own internal life", None),
            ("lpc.source.humfress-orthodoxy-and-the-courts",
             "the standard modern legal-historical study of how late-antique ecclesiastical and civil "
             "courts actually interacted, licensed for the imperial-coercion material's own legal "
             "context", None),
        ),
        relations=rel(TERM_COMPEL, FORCE_SHIFT),
        body=(
            "Re-derived from Doc_03_Lexicon_Candidate_List.md's own row for 'compel them to come in' "
            "([CT], 'Relationship to present-day traditions, secondarily Meaning'), Doc_06_Full_Lexicon_"
            "Development.md §3's own contest-type specification, and records/lpc/term/lpc.term.compel-"
            "them-to-come-in.md's own already-authored, already-reviewed senses.informational closing "
            "paragraph, all read directly this session. relations[] carries one term edge (lpc.term."
            "compel-them-to-come-in) and one force edge (lpc.force.illegal-to-established-shift, matrix "
            "cell 2B) named in this script's own docstring under RECIPROCITY -- the force describes the "
            "same underlying legal-capacity shift this doctrine's own third phase exercises, not a "
            "duplicate treatment of the doctrine itself; the force's own text independently names Doc_04 "
            "§2's decision not to advance the shift as a gravity, which this record does not revisit. "
            "This record does not adjudicate the historiographical questions it names, does not endorse "
            "or condemn the doctrine, and does not characterize the Donatists, matching the identical "
            "restraint the lexicon entry it draws on already states."
        ),
    )


# ===========================================================================
# 4. THE DEATH OF CYPRIAN -- TIER 1 (EYEWITNESS) OR TIER 3 (HAGIOGRAPHIC
#    CONVENTION)? -- A RESERVED, OPEN ESCALATION, NOT RESOLVED HERE.
# ===========================================================================

def build_cyprian_death_genre() -> None:
    emit(
        "lpc.contested.cyprian-death-genre",
        claim=(
            "Pontius's own account of Cyprian's death (Life §§15-19) rightly belongs in Tier 1 "
            "of Construction Framework V7.4. Its genus clause reads: 'direct textual "
            "attestation... named author with identifiable social location... datable with "
            "reasonable confidence'. Pontius meets every part of that test. He is a named deacon "
            "who saw it himself. The account also casts events as echoes of Scripture. This is "
            "called typology. It sees God's plan in them. This is called providential framing. "
            "Both are ornament. They sit on a real public execution that we can date. Neither "
            "is evidence that we cannot trust the account as a witness's word."
        ),
        held_against=[
            "The account itself discloses its own patterning on Scripture as an authorial aside, not a "
            "reader's inference -- the Zacchaeus parallel ('that there might not even be wanting to him... "
            "what happened in the case of Zacchæus') is Pontius's own stated comparison -- and the "
            "executioner's failing hand 'strengthened... with power granted from above' is a providential "
            "intervention narrated at the account's own climax, exactly one of CF V7.4's own three named "
            "markers of hagiographic narrative ('the idealized portrait of a saint's life... the death as "
            "completion of a formed life').",
            "This world's own build record states, at full strength, that 'once the account tells you it "
            "is patterning itself on Scripture, the specific details can no longer be separated from the "
            "pattern by a reader who has no independent witness' -- and this build has read no independent "
            "witness. The Acta Proconsularia, the strictly documentary record of the trial "
            "Pontius himself points readers toward, is vendored in Latin only (rows 41 and 194; also "
            "printed in rows 268 and 222) and is unread. Augustine's feast-day sermons on Cyprian "
            "(Sermo 309-313, row 264, second-witness OCR only), which retell the passion, are also "
            "unread (Doc_09 §6 item 2, §8 item 1; Story-Chunks/lpcstory006, Absent Story Note).",
            "This world's own Doc_09 was independently reviewed and "
            "approved to proceed with this exact question named as an unresolved "
            "escalation rather than settled by that approval: 'the escalation at §8 item 7 -- which half "
            "of CF V7.4's Tier 3 definition governs when its genus clause and its hagiographic-convention "
            "clause point opposite ways at lpcstory006 -- remains open and is not disposed of by this "
            "approval.'",
        ],
        concedes=(
            "Pontius meets Tier 1's own author test on every element CF V7.4 names -- eyewitness deacon, "
            "identifiable social location, datable with reasonable confidence -- exactly as "
            "lpcstory001 and lpcstory002 are assigned Tier 1 on that same basis, and this world's own "
            "build record states this directly rather than obscuring it: 'on the genus clause read alone, "
            "this story cannot be Tier 3 at all.' What is genuinely, and explicitly, unresolved is which "
            "of CF V7.4's own two clauses governs when they point in opposite directions at one and the "
            "same account -- a question this world's own build record calls 'a Construction Framework "
            "question, not a question this build can settle,' carried to the project lead rather than "
            "adjudicated by either the chunk, the story record, or this one. This record does not resolve "
            "it either. The bare historical facts are not in dispute: Cyprian was certainly executed under "
            "Valerian in 258, and the account we have of it was written in praise by his own deacon, in a "
            "form that patterns deaths on Scripture -- both true at once, and neither settles which Tier "
            "clause the account itself belongs under."
        ),
        divergence_partners=[
            "lpc.source.pontius-life-and-passion-of-cyprian",
            "lpc.source.acta-proconsularia-sancti-cypriani",
        ],
        confidence=conf("B", "verified-via-authority", "contested", "Contested"),
        sources=src(
            ("lpc.source.pontius-life-and-passion-of-cyprian",
             "Life §§15-19; the Zacchaeus typology and the providential strengthening of the "
             "executioner's hand, both directly quoted and re-verified"),
            ("lpc.source.acta-proconsularia-sancti-cypriani",
             "the strictly documentary witness to the trial, vendored in Latin only and not read in "
             "this build; named here rather than silently omitted, per lpcstory006's own Absent Story "
             "Note"),
            ("lpc.source.delehaye-passions-des-martyrs-genres-litteraires",
             "the genre scholarship licensing this world's own hagiographic-convention assessment "
             "(Zacchaeus typology, providential intervention, the death as completion of a formed life)"),
            ("lpc.source.delehaye-cyprien-dantioche-et-cyprien-de-carthage",
             "the further, related hazard this world's own Registry records -- the later conflation of "
             "Cyprian of Carthage with Cyprian of Antioch, what an unguarded hagiographic tradition does "
             "to a figure over time", None),
        ),
        relations=rel(STORY_DEATH),
        body=(
            "Re-derived from Doc_09_Story_Inventory.md's own Story Index (row lpcstory006) and its own "
            "§8 item 7 and Disposition section, and Story-Chunks/lpcstory006_the-death-of-cyprian.md's "
            "own Tier Justification section, read in full this session -- its own text already states "
            "the contest directly and at full strength rather than leaving it implicit. relations[] "
            "carries one story edge (lpc.story.the-death-of-cyprian) named in this script's own "
            "docstring under RECIPROCITY, not a fresh gravity-level edge to G1 or G8 -- the story "
            "record's own existing relations[] already carries those, and this record's own subject is "
            "the genre-classification question specifically, one level more specific than either "
            "gravity. This record gives an already-argued, already-escalated contest its own dedicated "
            "contested_claim treatment, exactly as don.contested.cirta-reserved-to-the-lord did for a "
            "comparable story-chunk-level contest, rather than leaving it inside a chunk's own Tier "
            "Justification prose. This record does not resolve the CF V7.4 governance question named "
            "at Doc_09 §8 item 7 in either direction; that question remains reserved for the project "
            "lead, exactly where Doc_09's own Disposition leaves it, untouched by this record."
        ),
    )


def main() -> None:
    build_de_unitate_recensions()
    build_grace_pelagius()
    build_compel_coercion()
    build_cyprian_death_genre()
    print(f"Wrote {len(WRITTEN)} records:")
    for p in WRITTEN:
        print(f"  {p}")


if __name__ == "__main__":
    main()
