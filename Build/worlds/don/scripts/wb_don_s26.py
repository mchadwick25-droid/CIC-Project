"""B-6 (S2.1): Donatism (don) contested_claim records.

WHAT THIS SCRIPT DOES. Produces this world's first `contested_claim`
records under records/don/contested_claim/, per the live schema
(engine/m1/schemas.py TYPE_PROPERTIES["contested_claim"]: claim, held_against,
concedes, divergence_partners -- confirmed by direct read this session, not
assumed) and gate battery (engine/m1/gates.py COMPLETION_REQUIRED
["contested_claim"] = ["claim", "held_against", "concedes"], confirmed by
direct read this session; divergence_partners is NOT gate-required but is
authored on every record below anyway, matching the fleet's own good-practice
convention). This is B-6 of the 9-step record-native build pipeline (B-1
through B-9); B-1 through B-5 (sources/world_core, search_record, 21 term
records, 9 story/16 figure/4 quote records, 8 gravity/13 force records) are
already done, committed, and pushed. Read Build/worlds/don/scripts/
wb_don_s21.py through wb_don_s25.py in full before this script was written
(not touched by it, not re-run by it) for the docstring/code-pattern
discipline this script follows, and two real fleet worked examples read in
full this session: records/pahc/contested_claim/pahc.contested.two-strand-
packaging.md, records/hal/contested_claim/hal.contested.chronology.md, and
records/desert/contested_claim/desert.contested.antony-literacy.md.

WHY THIS RECORD TYPE MATTERS MORE THAN B-1 THROUGH B-5. Per this step's own
launch brief: Phase Eight (Representative Construction's Table Readiness
Round) was found blocked because Donatism has no `contested_claim` records at
all, and this record type is what a genuine Table Readiness Round draws its
divergence question from. This script's four records are built to be that
raw material -- a genuine scholarly or textual dispute this world's own
build record already argued out, not a restatement of "the Donatists
believed X and Catholics believed Y" (that belongs to `doctrinal_witness`
records and the gravities themselves, not here).

WHAT COUNTS AS A CONTESTED CLAIM HERE, per the two worked examples read in
full and this step's own launch brief: a scholarly or textual dispute (a
dating question, an authorship/attribution question, a character/reputation
question turning on which source is trusted) -- never simply two sides of
this world's own doctrinal argument, which the gravities and any future
`doctrinal_witness` records already carry. Four candidates were tested and
built; two more were tested and declined (see "CANDIDATES CONSIDERED AND
DECLINED" below); the Primary-gravity minimum (`cic-build-cycle`'s own
established precedent, per this step's own launch brief) is checked against
Doc_04's own text directly, not assumed to require one record per gravity --
see "PRIMARY-GRAVITY COVERAGE" below for exactly which of G1/G2/G3/G5 Doc_04
actually names a scholarly contest for, and which it does not.

INPUTS, mapped to OUTPUTS, precisely:
  - `Doc_02_Source_Ecology.md` SS1's own "Bishop-count correction at the 411
    Conference" paragraph (added 2026-09-09) and `don_Decision_Log.md`'s own
    "World-build bishop-count correction (284 -> 279)" entry (2026-09-09,
    grepped by section header, not read in full at 745 lines) -> `don.
    contested.bishop-count-411-conference`. A clean, already-resolved,
    well-documented textual/manuscript dispute (284 vs. 279 Donatist bishops
    seated at the 411 Conference of Carthage), with a specific, checkable
    resolution (279, per the *Gesta*'s own Migne-apparatus tally,
    `cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`, line
    73363) and a named residual caveat (the located tally is Migne's own
    editorial/summary apparatus, not necessarily the acta's own verbatim
    tally list, on an independently-flagged poor-OCR-quality scan) that the
    correction itself does not erase.
  - `Doc_03_Lexicon_Candidate_List.md` SS4 ("Contested-Tradition (CT)
    Candidate and Its Contest") and `Doc_04_Gravity_Discovery.md` SS3.5 (D-A)
    -> `don.contested.circumcellion-character`. The one [CT]-tagged term in
    this world's entire 21-term roster (Agonistici/Circumcellion), Doc_03's
    own legend defining CT as "contested tradition (live scholarly contest)"
    -- Frend's older, fuller-acceptance reading of the hostile portrait
    against Shaw's *Sacred Violence* corrective (Registry row 24), a live,
    named-scholar contest over the group's own character and scale, not its
    bare existence. **This record documents the Frend/Shaw contest only --
    see "THE TWO RESERVED QUESTIONS" below for exactly how the adjacent
    Axido/Fasir material was, and was not, touched.**
  - `Doc_01_World_Identification_Boundaries_Orientation.md` SS4 (Strand
    Determination) and `Doc_02_Source_Ecology.md` SS1's own "Maximianist
    schism's rebaptism-theology evidence" paragraph (specifically its own
    second paragraph, on the Cresconius-account Donatist apologia) ->
    `don.contested.maximianist-reception`. A genuine scholarly contest this
    world's own build record already argued out: does the mainstream party's
    reception of returning Maximianist clergy without reordination or
    rebaptism prove a shared formation pattern (Doc_01 SS4's own reading,
    grounding the strand-singular finding), or does a specific, bounded
    synodal dispensation -- the Cresconius-account Donatist apologia's own
    reading, that Bagai "had granted a season of delay during which all who
    returned should be held innocent" -- mean the episode need not
    generalize that far?
  - `Story-Chunks/donstory007_council-of-cirta.md` in full -> `don.contested.
    cirta-reserved-to-the-lord`. The story chunk's own Usage Guidance already
    states the contest directly: Optatus's own characterization of the 305
    council's "reserved to the Lord" ruling as evasion (he tells the story to
    argue the movement's own founders were traditores absolving one another)
    against this world's own plausible alternative reading (an act of mercy
    or of realistic humility about what could be verified) -- named there as
    a real, unresolved complication for this world's own founding self-image,
    not adopted at face value in either direction. This is genuinely distinct
    from the Circumcellion/Axido-Fasir material -- a different council, a
    different source (Optatus alone, not the Circumcellion petition
    material), and a different kind of contest (what a specific ruling
    MEANT, not a group's own character and scale).

CANDIDATES CONSIDERED AND DECLINED, with reasoning (per this step's own
launch instruction against silent gaps):
  - **Doc_03's CT legend and the roster of 21 terms.** Checked directly:
    exactly one term (Agonistici/Circumcellion) carries [CT] in this world's
    entire candidate roster (Doc_03 SS1, SS4) -- no other term was tagged CT
    and "parked." This is not a gap this script is leaving silent; it is
    Doc_03's own text, confirmed by direct read, not assumed.
  - **Tyconius's own condemned position (D-B in Doc_04).** Doc_04 SS2 tests
    and explicitly does NOT advance D-B as a gravity (fails Repetition,
    Persistence, Dependency -- a single condemned voice with no following).
    A genuine open question exists about his own formal ecclesiastical
    standing at the time of condemnation (Doc_01 SS4: "no clerical office is
    attested for him... a determination that does not require, and does not
    take, a position on his own formal standing within the communion, which
    is left deliberately open") -- but this is a documented EVIDENTIARY GAP
    (the record is silent), not two named sources or readings pulling apart
    from each other, which is what a contested_claim record requires per the
    two worked fleet examples read in full this session (hal.contested.
    chronology, desert.contested.antony-literacy: a real dispute between
    specific readings, not an unresolved absence). Doc_01 SS4's own "left
    deliberately open" language is itself the correct disposition for a gap
    of this shape; forcing a contested_claim record onto it would manufacture
    a dispute this world's own record does not actually contain.
  - **The Council of Rome (313) / Council of Arles (314) rejection.** Doc_01
    SS5 and Doc_04 SS3.7 both treat the Donatist party's rejection of these
    verdicts as a settled, undisputed fact (recorded even by hostile sources
    reporting their own side's actions) -- no named alternative reading of
    WHAT HAPPENED or of the rejection's own basic character is argued
    anywhere in this world's own build record. A candidate needs a real,
    textually-attested divergence to build against, not an assumption that
    any hostile-mediated fact is automatically "contested" in this record
    type's own sense -- this one is not.
  - **G3 (Martyr-Cult Identity) and G5 (Refusal of Imperial Legitimacy) as
    Primary-gravity contested_claim subjects.** See "PRIMARY-GRAVITY
    COVERAGE" immediately below.

PRIMARY-GRAVITY COVERAGE, checked directly against Doc_04's own text rather
than assumed to require one record per Primary gravity (per this step's own
launch instruction: "check Doc_04's own text for anywhere it names a
scholarly disagreement... rather than assuming one exists for all four"):
  - **G1 (Ministerial Purity) and G2 (Rebaptism as Boundary-Marking
    Practice)** -- both covered by `don.contested.maximianist-reception`.
    Doc_04's own Interaction Matrix (SS6) names G1<->T2 and G2<->T2 as X
    (reshaping) specifically because the Maximianist reception precedent
    "directly reshapes G1's own internal consistency" and "as with G1,
    directly tested and complicated" for G2 -- the contested reading of what
    that reception PROVES bears on both Primaries directly, not only on T2.
  - **G3 (Martyr-Cult Identity)** -- **no scholarly contest identified.**
    Doc_04 SS3.3 names this gravity's Confidence/Gravity Cross-Check result
    as "CONSISTENT, and the least Author-Gravity-encumbered Primary in this
    document" -- explicitly the opposite of a contested finding. No named
    scholar or alternative reading disputes this gravity's own extent,
    dating, or character anywhere in Doc_01, Doc_02, Doc_03, or Doc_04. This
    script does not force a contested_claim record onto a gravity Doc_04
    itself finds unusually well-corroborated.
  - **G5 (Refusal of Imperial/State Religious Legitimacy)** -- **no
    scholarly contest identified bearing on G5's OWN extent, dating, or
    character.** Doc_04 SS3.7's own flagged divergence (core episodes
    Documented; the "principled refusal" synthesis partly this document's
    own reading) is the same Author-Gravity-mediation shape already carried
    on the gravity record's own confidence.divergence_note field -- a
    source-mediation finding, not a scholarly dispute between named readings
    of what G5 itself covers. The one place a genuine contest touches this
    gravity's own neighborhood is D-A's own Frend/Shaw contest (D-A <-> G5 is
    a named, narrow Interaction Matrix edge, since D-A is "the direct object
    of specific imperial legislation... itself part of G5's own evidentiary
    base," Doc_04 SS6) -- but that contest is about D-A's OWN character and
    scale, not about G5's. `don.contested.circumcellion-character` is
    therefore related to D-A only, not to G5, matching the precision Doc_04
    itself draws between the two gravities' own distinct interaction.
  Net: two of this world's four Primary gravities (G1, G2) receive a
  contested_claim via `don.contested.maximianist-reception`; the other two
  (G3, G5) do not, because Doc_04's own text does not identify a scholarly
  contest bearing on either one's own extent, dating, or character -- this
  is a checked finding, not an unexamined gap.

THE TWO RESERVED QUESTIONS -- HOW EACH WAS HANDLED, STATED AFFIRMATIVELY
(per this step's own launch instruction: say so even where the answer is
"no record here touches it," don't just omit mention):

  1. **Axido/Fasir (Constitution Article 23).** `don_Decision_Log.md`'s
     Phase Five Round 2 entry flags this as a live, project-lead-reserved
     question: whether the movement's own petition material naming
     Circumcellion leaders Axido and Fasir "leaders of the saints" (against
     the hostile "marauders" reading) constitutes deployable "mediation
     through a figure of contested standing." **No record built by this
     script names Axido or Fasir, quotes their petition, or takes any
     position on their own individual reputation or on the deployment
     question itself.** `don.contested.circumcellion-character` documents
     the Frend/Shaw contest over the Circumcellion/*agonistici* GROUP's own
     general character and scale -- the same contest Doc_03 SS4 and Doc_04
     SS3.5 already carry at the gravity/lexicon level, neither of which
     names Axido or Fasir either. This script's own claim/held_against/
     concedes fields for that record are worded at the group level
     throughout and the record's own body text states explicitly that it
     does not resolve, and should not be read as resolving, the Axido/Fasir
     Article 23 question -- that question remains reserved for the project
     lead, exactly where `don_Decision_Log.md` leaves it, untouched by this
     script in either direction.
  2. **Article 29 Limb 2 (Cyprian/Augustine/rebaptism-question mediation).**
     `don_Decision_Log.md`'s 2026-09-08 entry records Limb 1 ratified, Limb 2
     left open by the project lead's own deliberate choice, on whether
     Cyprian, Augustine, or the rebaptism question count as "mediation
     through a figure of contested standing" among present-day traditions.
     **No record built by this script touches Cyprian's or Augustine's own
     standing as a source in that sense.** `don.contested.maximianist-
     reception` and `don.contested.cirta-reserved-to-the-lord` both cite
     Augustine's and Optatus's own primary texts extensively, and Augustine's
     own hostile-mediation role is central to both records' own held_against/
     concedes reasoning -- but this is the ORDINARY Author Gravity discipline
     already governing this world's entire build (Doc_01 SS7 item 1; Doc_02
     SS1-SS2), asking whether a claim's specific content is independently
     corroborated beyond a hostile source's own framing, a question this
     world's build has asked of every record type so far. It is a different
     question from Article 29 Limb 2's own present-day-mediation question
     (whether this world's reconstruction, by running substantially through
     Cyprian/Augustine/the rebaptism question, itself touches a tradition
     continuing into the present through a figure of contested standing).
     This script does not conflate the two, does not reason toward Limb 2 in
     either direction, and leaves it exactly where `don_World_Profile.md` SS9
     records it: PARTIALLY RESOLVED, Limb 2 OPEN, reserved for the project
     lead.

MECHANICAL vs AUTHORED, field by field:
  - id, world_id, record_type, schema_version, status, register, canon_cells:
    MECHANICAL. register="etic" throughout, matching all three fleet worked
    examples read in full this session -- a contested_claim record states
    and weighs a scholarly or textual disagreement in this build's own
    analytic voice, not a formation participant's first-person voice.
    Confirmed directly against engine/m1/gates.py this session:
    "contested_claim" appears in neither _PERSPECTIVE_FIELDS nor
    _ATTRIBUTION_FIELDS, so "this world's own..." build-thread phrasing
    (used freely below, matching hal/desert's own precedent) is not a gate
    risk here the way it would be in a story or term record's own voice-
    scoped fields. canon_cells=[] throughout -- this world has no canon
    work done yet (no records/don/canon_question/ directory exists),
    matching every prior don record built so far.
  - claim, held_against, concedes: AUTHORED, in every case re-derived from
    a specific, cited section of Doc_01/02/03/04/09 or a specific Story-
    Chunk file (never from this session's own outside knowledge of Donatist
    historiography) -- see INPUTS above for the exact section each record
    draws on.
  - confidence.evidentiary_weight: "contested" throughout -- the schema's
    own dedicated value for exactly this record type's own subject matter,
    matching all three fleet worked examples.
  - confidence.formation_confidence: "Contested" throughout, matching two of
    the three fleet worked examples (hal.contested.chronology, desert.
    contested.antony-literacy) rather than pahc's own "Inferential-Thin" --
    each of this script's four records names a genuine, currently-unresolved
    reading contest as its own subject, not a single settled-but-thin fact.
  - confidence.divergence_note: null throughout, matching two of the three
    fleet worked examples (hal, desert) rather than pahc's own populated
    field -- for this record type specifically, the divergence IS the
    claim/held_against/concedes triad itself; a separate prose divergence_
    note would restate what those three fields already carry in full,
    rather than naming a genuinely separate divergence the way gravity/
    force's own divergence_note does (per wb_don_s25.py's own house rule for
    THOSE record types, which this script does not carry over here).
  - confidence.citation_specificity: "A" where a specific text/locus grounds
    the claim directly (bishop-count: one located manuscript line;
    Maximianist reception: extensively-quoted primary-text passages; Cirta:
    one cited primary passage, Optatus I.14); "B" for circumcellion-
    character, since that record rests on this world's own already-completed
    Doc_03/Doc_04 synthesis of the Frend/Shaw contest rather than this
    session's own fresh direct read of either scholar's own text.
  - confidence.verification_state: "verified-via-authority" throughout --
    this script relies on Doc_01/02/03/04/09's and don_Decision_Log.md's own
    already-completed, independently-reviewed research and correction work,
    not on this session re-opening the raw vendored primary texts or the
    Frend/Shaw secondary literature itself, matching the same distinction
    wb_don_s25.py's own docstring already draws for non-quote records.
  - sources[] / divergence_partners[]: AUTHORED per record, resolved to the
    specific don.source.* ids (checked directly against records/don/source/,
    never guessed) that ground each side of the contest. divergence_partners
    names the real source ids whose ACCOUNTS diverge (per this step's own
    launch instruction, contrasted explicitly with cappadocian's and ijc's
    own misuse of this field as free prose, which this script does not
    repeat) -- never a bare id list disconnected from what sources[] and the
    record's own claim/held_against fields already establish.
  - relations[]: AUTHORED per record (see RECIPROCITY below), "associated-
    with" throughout, matching all three fleet worked examples' own choice
    of the one symmetric relation type over a directional pair (RELATION_
    TYPES's precondition-for/enabled-by, tension-with, etc. were considered
    and set aside for the same reason wb_don_s25.py's own docstring gives for
    its own force<->force edges: several of these contested_claim<->gravity
    connections state a "bears on," "reshapes," or "is the same episode
    viewed from a different angle" relationship rather than a strict
    precondition or a single named tension-pole pair).

RECIPROCITY, applied per this step's own launch instruction ("if a
contested_claim relates to a gravity via relations[], close the inverse on
the gravity record too"). Five existing records/don/gravity/*.md files
receive one added relations[] entry each, applied directly by targeted edit
after this script ran -- NOT regenerated by this script itself, and not
listed among the file paths this script writes. Reasoning for that split:
these five gravity records are already-built, already-committed, already-
reviewed (B-5) records this step's own launch brief does not authorize
rewriting wholesale for a small additive change; reconstructing all five in
full here (duplicating wb_don_s25.py's own ~1500-line generation) to add one
relations[] line each would risk silent drift from the committed, reviewed
text. Each edit adds exactly one dict to that file's own relations[] list
and touches nothing else:
  - don.gravity.parallel-institutional-hierarchy.md (G4) <- don.contested.
    bishop-count-411-conference
  - don.gravity.circumcellion-agonistici.md (D-A) <- don.contested.
    circumcellion-character
  - don.gravity.purity-rigor-vs-institutional-reception.md (T2) <- don.
    contested.maximianist-reception
  - don.gravity.ministerial-purity.md (G1) <- don.contested.maximianist-
    reception AND <- don.contested.cirta-reserved-to-the-lord
  - don.gravity.rebaptism-boundary-marking.md (G2) <- don.contested.
    maximianist-reception

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells; touch records/don/{source,
world_core,term,story,figure,quote,search_record,force}/ (existing B-1
through B-5 records are read only, for their own don.source.*/don.gravity.*
ids, never edited by this script itself); name, characterize, or quote
Axido or Fasir, or resolve the Article 23 question about them (see THE TWO
RESERVED QUESTIONS above); reason toward, narrow, or guess at Article 29
Limb 2 in either direction (same section); build a contested_claim record
for G3 or G5 where Doc_04's own text names no scholarly contest bearing on
either (see PRIMARY-GRAVITY COVERAGE above); build one for Tyconius's own
formal standing, which is a documented evidentiary gap, not a dispute
between named readings (see CANDIDATES CONSIDERED AND DECLINED above); run
the M2 compiler; register `don` in records/worlds.yaml (B-9).
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]  # .../cic-project
RECORDS_ROOT = REPO_ROOT / "records" / "don"

WORLD_ID = "don"
SCHEMA_VERSION = 2

WRITTEN: list[str] = []

# Gravity ids this script's own relations[] point at (read only -- see
# RECIPROCITY above for how the inverse edge is actually applied).
G1 = "don.gravity.ministerial-purity"
G2 = "don.gravity.rebaptism-boundary-marking"
G4 = "don.gravity.parallel-institutional-hierarchy"
DA = "don.gravity.circumcellion-agonistici"
T2 = "don.gravity.purity-rigor-vs-institutional-reception"


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


def rel(*targets):
    return [{"type": "associated-with", "target": t} for t in targets]


# ===========================================================================
# 1. BISHOP-COUNT CORRECTION AT THE 411 CONFERENCE (279 vs. 284)
# ===========================================================================

def build_bishop_count() -> None:
    emit(
        "don.contested.bishop-count-411-conference",
        claim=(
            "The 411 Conference of Carthage's own bishop count is a simple, settled fact, "
            "available without complication directly from the *Gesta*'s own text: 279 Donatist "
            "bishops seated against 286 Catholic."
        ),
        held_against=[
            "This figure was not settled through most of this world's own construction history. "
            "An unverified '284 Donatist' figure propagated silently since this world's earliest "
            "construction document (Step0_Movement_Scope_Confirmation.md, written before the "
            "Gesta Collationis Carthaginiensis itself was vendored) through Doc_01, Doc_02, Doc_04, "
            "Doc_05, Doc_07, Doc_08, Doc_09, Lexicon-Chunks/donlex015, and multiple Representative-"
            "phase documents, never checked against the primary source directly until 2026-09-09.",
            "The corrected figure rests on one located tally, at one line (73363) of a 19th-century "
            "Migne scan this world's own Registry independently flags as 'notably poor OCR quality "
            "even by this corpus's own standards' -- legible despite that, but not a manuscript-"
            "certain reading placed beyond all doubt by the correction alone.",
            "The located tally ('...licis 286, et ex Donalislarum parte 279') is Migne's own "
            "editorial/summary apparatus surrounding the acts, not necessarily the acta's own "
            "verbatim tally list -- a distinction Doc_02 SS1's own correction paragraph carries "
            "explicitly as a caveat, not one the correction itself resolves away.",
        ],
        concedes=(
            "279 Donatist against 286 Catholic is the best-attested figure available and the one "
            "every current site in this world's own build now carries. The correction away from 284 "
            "is not itself in serious doubt: the scan's 'Donalislarum' is a recognizable, checkable "
            "OCR error for 'Donatistarum,' not a guess, and the 286 Catholic figure was already "
            "correct throughout. What remains genuinely open is only the finer-grained certainty "
            "the 'simple, settled fact' framing implies -- this is the one located tally, from an "
            "editorial apparatus, on a scan of independently-flagged poor quality, not a cross-"
            "checked or independently-corroborated figure the way, for example, the Deo laudes "
            "acclamation's own epigraphic text is."
        ),
        divergence_partners=[
            "don.source.migne-pl11-collatio-carthaginiensis",
            "don.source.gesta-collationis-carthaginiensis",
        ],
        confidence=conf("A", "verified-via-authority", "contested", "Contested"),
        sources=src(
            ("don.source.migne-pl11-collatio-carthaginiensis",
             "cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt, line 73363: "
             "'...licis 286, et ex Donalislarum parte 279'"),
            ("don.source.gesta-collationis-carthaginiensis",
             "the acts' own numbered interventions (e.g. acts 20, 24, 26, 50, 99, 108, 121, 253, "
             "266, 268, Emeritus's own recorded interventions), the transcript this tally summarizes"),
        ),
        relations=rel(G4),
        body=(
            "Re-derived from Doc_02_Source_Ecology.md SS1's own 'Bishop-count correction at the "
            "411 Conference' paragraph (added 2026-09-09) and don_Decision_Log.md's own "
            "'World-build bishop-count correction (284 -> 279)' entry (grepped by header, not read "
            "in full at 745 lines -- the relevant paragraphs were read in full). relations[] carries "
            "the one gravity edge (G4, don.gravity.parallel-institutional-hierarchy) named in this "
            "script's own docstring under RECIPROCITY -- G4's own manifestations[] field already "
            "states this corrected figure directly. This record does not touch Cyprian, Augustine, "
            "or the rebaptism question, and does not bear on Article 29 Limb 2 in any way -- see "
            "this script's own docstring, THE TWO RESERVED QUESTIONS, item 2."
        ),
    )


# ===========================================================================
# 2. CIRCUMCELLION/AGONISTICI CHARACTER (Frend vs. Shaw) -- Axido/Fasir NOT
#    named, characterized, or resolved anywhere in this record.
# ===========================================================================

def build_circumcellion_character() -> None:
    emit(
        "don.contested.circumcellion-character",
        claim=(
            "The Circumcellion/*agonistici* group's hostile literary characterization -- itinerant, "
            "socially marginal, prone to violence -- substantially reflects the group's own actual "
            "character and scale, rather than being substantially a polemical construction of its "
            "Catholic and imperial opponents."
        ),
        held_against=[
            "Shaw's *Sacred Violence* (Registry row 24), this world's own standard corrective, reads "
            "the same hostile portrait as considerably overstated against the group's own genuinely "
            "independent core: its bare existence, attested directly in imperial legislation (CTh "
            "16.5.52) by name and by a distinct silver-denominated fine no other listed rank carries.",
            "The group's own reported self-designation, *agonistici* ('contestants'), reaches this "
            "world's record only through Augustine's own report of it -- reliable reportage per this "
            "world's own build documents (Doc_02 SS6), but not evidentially on par with the "
            "independently-attested bare-existence claim, and confirming nothing on its own about "
            "the group's typical conduct.",
            "No Donatist-voiced or non-mediated text in this world's own vendored corpus corroborates "
            "the group's character, scale, or typical conduct at all -- Doc_04 SS5's own declared "
            "Cross-Voice Test names this candidate as the one that 'most clearly fails a strict "
            "cross-voice standard for anything beyond bare existence and self-designation,' precisely "
            "the 'artificially confirmed' risk that test exists to catch.",
        ],
        concedes=(
            "The group's bare existence, and the imperial state's own targeted concern with it, are "
            "not in dispute -- CTh 16.5.52's own text independently names and fines them, on grounds "
            "no hostile literary framing mediates. What is genuinely, and by this world's own build "
            "documents' own explicit finding, unresolved is everything about the group's typical "
            "character, scale, and conduct beyond that bare fact: this record does not adopt Frend's "
            "fuller acceptance of the hostile portrait as settled, and does not resolve the contest in "
            "Shaw's favor either, since neither reading is independently corroborated in a non-"
            "hostile-mediated source (Doc_03 SS4; Doc_04 SS3.5, the sharpest Confidence/Gravity "
            "Cross-Check divergence in that document, split across three separate evidentiary tiers). "
            "**This record is scoped to the group's own general character and scale. It does not "
            "name, quote, or characterize Axido or Fasir specifically, and does not resolve, narrow, "
            "or take any position on the separately-reserved Constitution Article 23 question about "
            "them (whether the movement's own petition material naming them 'leaders of the saints' "
            "constitutes deployable mediation through a figure of contested standing) -- that "
            "question remains reserved for the project lead, per don_Decision_Log.md's Phase Five "
            "Round 2 entry, untouched by this record in either direction.**"
        ),
        divergence_partners=[
            "don.source.codex-theodosianus-book-16",
            "don.source.optatus-against-donatists",
        ],
        confidence=conf("B", "verified-via-authority", "contested", "Contested"),
        sources=src(
            ("don.source.codex-theodosianus-book-16",
             "16.5.52: 'circumcelliones argenti pondo decem' -- the one rank fined in silver rather "
             "than gold"),
            ("don.source.boyd-ecclesiastical-edicts-theodosian-code",
             "corroborating secondary account of the surrounding legislative sequence; explicitly "
             "not licensed for the group's own character claims, Doc_02 SS3"),
            ("don.source.optatus-against-donatists",
             "the hostile literary characterization this contest tests, per Doc_03 SS4/Doc_04 SS3.5"),
        ),
        relations=rel(DA),
        body=(
            "Re-derived from Doc_03_Lexicon_Candidate_List.md SS4 (the one [CT]-tagged term in "
            "this world's 21-term roster) and Doc_04_Gravity_Discovery.md SS3.5 (D-A), both read in "
            "full this session. relations[] carries the one gravity edge (D-A, don.gravity."
            "circumcellion-agonistici) named in this script's own docstring under RECIPROCITY -- not "
            "to G5, per this script's own docstring, PRIMARY-GRAVITY COVERAGE (the Frend/Shaw contest "
            "bears on D-A's own character, not on G5's own extent, dating, or character directly). "
            "**Axido/Fasir handling:** see this script's own docstring, THE TWO RESERVED QUESTIONS, "
            "item 1, in full -- this record was deliberately scoped at the group level throughout "
            "specifically so it would not need to touch that reserved question, and it does not."
        ),
    )


# ===========================================================================
# 3. MAXIMIANIST RECEPTION -- WHAT THE NO-REORDINATION/NO-REBAPTISM RECEPTION
#    ACTUALLY PROVES.
# ===========================================================================

def build_maximianist_reception() -> None:
    emit(
        "don.contested.maximianist-reception",
        claim=(
            "The mainstream (Primianist) Donatist party's own reception of returning Maximianist "
            "clergy without repeating either ordination or baptism is decisive evidence that the two "
            "Donatist bodies shared one formation pattern all along -- proof against Maximianist "
            "strand status (Doc_01 SS4), not merely a rhetorical embarrassment Augustine happened to "
            "exploit."
        ),
        held_against=[
            "A later Donatist apologetic account, reported in a scholarly summary of Augustine's "
            "*Contra Cresconium* (Doc_02 SS1, Registry rows 17, 31), held that the reception rested "
            "on a specific, bounded synodal dispensation -- the Bagai council itself 'had granted a "
            "season of delay during which all who returned should be held innocent' -- rather than on "
            "any general recognition that Maximianist orders and baptism were substantively valid "
            "independent of schism status. On that reading, the episode reflects a one-time act of "
            "ecclesiastical leniency, not a demonstration that the two parties always held "
            "functionally identical formation patterns.",
            "Every attestation of the reception's own justification reaches this record through "
            "Augustine's own report and refutation of the Donatist account, not through any surviving "
            "Maximianist or mainstream-Donatist first-hand statement of it (Doc_02 SS1: 'no "
            "Maximianist or mainstream-Donatist first-hand account of that justification survives "
            "independent of his report and refutation of it') -- the same Author Gravity concentration "
            "this world's whole evidentiary base is flagged for (Doc_01 SS7 item 1) qualifies the "
            "'evidence against strand status' reading as much as it qualifies any other claim resting "
            "on Augustine's own argumentative framing.",
            "Augustine's own primary text states the reception 'settles the whole question in "
            "dispute, and removes all controversy' (*On Baptism* I.5.7) -- a hostile advocate's own "
            "characterization of the episode's evidentiary weight, offered in the course of an "
            "argument against the Donatists, not a neutral historian's or a Donatist voice's own "
            "assessment of what the episode proves.",
        ],
        concedes=(
            "The reception itself -- no reordination, no repeated baptism -- is not itself disputed "
            "anywhere in this world's own vendored record: it is common ground even in the "
            "Cresconius-account Donatist apologia Augustine reports (the dispute there is over how to "
            "justify the reception, not over whether it happened), and it is independently "
            "corroborated across multiple works in Augustine's own primary text (*On Baptism* I.1.2, "
            "I.5.7; *Answer to the Letters of Petilian*; Letter 51 to Crispinus). Doc_01 SS4's own "
            "strand-singular finding does not rest on this contested episode alone -- it separately "
            "finds no distinct formation emphasis, practice, or ecological orientation dividing the "
            "two bodies on several other grounds -- so this contest, even fully credited to the "
            "alternative reading, would not by itself overturn that finding. What remains genuinely "
            "open is only the reception's own specific evidentiary weight: whether it demonstrates the "
            "two parties held identical formation patterns as a matter of settled doctrine (the "
            "reading Doc_01 SS4 adopts, and which this record does not reopen) or reflects a bounded "
            "act of dispensation that need not generalize that far -- a contest this record names "
            "rather than treats as beyond dispute."
        ),
        divergence_partners=[
            "don.source.augustine-contra-cresconium",
            "don.source.augustine-on-baptism-against-donatists",
        ],
        confidence=conf("A", "verified-via-authority", "contested", "Contested"),
        sources=src(
            ("don.source.augustine-on-baptism-against-donatists",
             "I.1.2, I.5.7 -- 'settles the whole question in dispute, and removes all controversy'"),
            ("don.source.augustine-answer-to-letters-of-petilian",
             "describing Optatus Gildonianus 'sucking back Felicianus and Prætextatus once again "
             "within their pale'"),
            ("don.source.augustine-contra-cresconium",
             "the Cresconius-account Donatist apologia -- 'the Synod had granted a season of delay "
             "during which all who returned should be held innocent'"),
            ("don.source.augustine-letter-51-to-crispinus",
             "'you restored some of them without re-ordination, and accepted their baptism as valid'"),
            ("don.source.augustine-psalmus-contra-partem-donati",
             "'Why rebaptize us... when you do not repeat the rite upon your once expelled but now "
             "restored Maximianists?'"),
        ),
        relations=rel(T2, G1, G2),
        body=(
            "Re-derived from Doc_01_World_Identification_Boundaries_Orientation.md SS4 (Strand "
            "Determination) and Doc_02_Source_Ecology.md SS1's own 'Maximianist schism's rebaptism-"
            "theology evidence' paragraph and its own following paragraph on the Cresconius-account "
            "apologia, both read in full this session. relations[] carries three gravity edges (T2, "
            "G1, G2) named in this script's own docstring under RECIPROCITY and PRIMARY-GRAVITY "
            "COVERAGE -- Doc_04 SS6's own Interaction Matrix names G1<->T2 and G2<->T2 as X "
            "(reshaping) specifically because this episode reshapes both Primaries' own internal "
            "consistency, not only T2's own standing as a Tensional gravity. **Article 29 Limb 2 "
            "handling:** this record's own extensive citation of Augustine's primary text is ordinary "
            "Author Gravity discipline (Doc_01 SS7 item 1), not a touch on Augustine's own standing "
            "as a source in the Article 29 Limb 2 sense -- see this script's own docstring, THE TWO "
            "RESERVED QUESTIONS, item 2, in full."
        ),
    )


# ===========================================================================
# 4. THE COUNCIL OF CIRTA (305) -- WHAT "RESERVED TO THE LORD" MEANT.
# ===========================================================================

def build_cirta() -> None:
    emit(
        "don.contested.cirta-reserved-to-the-lord",
        claim=(
            "The Council of Cirta's (305) 'reserved to the Lord' ruling on the traditor question -- "
            "no one present found guilty, no one cleared -- was an act of evasion: an implicit "
            "admission of guilt the assembled bishops declined to name outright, exactly as Optatus "
            "tells the story to argue."
        ),
        held_against=[
            "This world's own later tradition would plausibly describe the same ruling differently -- "
            "as an act of mercy, or of realistic humility about what could actually be verified under "
            "the conditions the Diocletianic persecution had just imposed -- rather than as a cover "
            "for guilt (Story-Chunks/donstory007_council-of-cirta.md, Usage Guidance).",
            "The bare sequence of events does not itself establish evasive intent: three bishops not "
            "themselves accused (Victor of Garba, Felix of Rotarium, Nabor of Centurio) were "
            "specifically the ones asked for judgment and specifically the ones who recommended "
            "reservation -- a structural detail at least as consistent with a considered judicial "
            "choice (no untainted judge present felt able to rule on an unverifiable charge) as with "
            "collective evasion by the interested parties themselves.",
            "The only surviving account of this council is Optatus's own (Against the Donatists "
            "I.14) -- this world's own later opponent, telling the story specifically to argue that "
            "the movement's founders were traditores absolving one another. No Donatist-authored or "
            "Donatist-voiced account of this specific council survives to confirm any alternative "
            "reading of the ruling's own meaning directly.",
        ],
        concedes=(
            "The bare facts of what happened at Cirta are Documented and not in dispute: the council "
            "met; the traditor question was put to those gathered; several admitted responsibility; "
            "Purpurius's counter-taunt against Secundus; the nephew's advice to remit the matter to "
            "God; the three unaccused bishops' own judgment that the case ought to be reserved to the "
            "Lord; Secundus's 'Sit down, all'; the assembly's 'Thanks be to God' in response; no "
            "verdict either way. What is genuinely contested is not any of this sequence but its own "
            "MEANING -- evasion, as Optatus's own hostile frame has it, or principled restraint, as "
            "this world's own plausible alternative reading has it -- and this record does not resolve "
            "that question, since no surviving Donatist-authored account of this council exists to "
            "settle it either way (matching donstory007's own Usage Guidance precisely: 'the "
            "Representative should be prepared to sit with that complication rather than resolve it "
            "toward whichever side is more comfortable')."
        ),
        divergence_partners=[
            "don.source.optatus-against-donatists",
            "don.source.optatus-appendix-of-documents",
        ],
        confidence=conf("A", "verified-via-authority", "contested", "Contested"),
        sources=src(
            ("don.source.optatus-against-donatists",
             "Against the Donatists I.14 (cic/texts/optatus_against-the-donatists.txt, lines "
             "181-192) -- the narrated account"),
            ("don.source.optatus-appendix-of-documents",
             "the Acts of the Council of Cirta (305) themselves, part of Optatus's own Appendix, "
             "the documentary layer the narration in Book I draws on"),
        ),
        relations=rel(G1),
        body=(
            "Re-derived from Story-Chunks/donstory007_council-of-cirta.md, read in full this "
            "session -- its own Formation Ecology Connection section already ties this material "
            "directly to G1 ('Ministerial Purity / Traditor-Free Sacramental Validity... but as a "
            "complicating case rather than a simple illustration'), and its own Usage Guidance "
            "already states this exact contest ('Optatus's own characterization... should not be "
            "adopted uncritically... while being honest that no surviving Donatist-authored account "
            "of this specific council exists to confirm that alternative reading directly') -- this "
            "record gives that already-argued contest its own dedicated contested_claim treatment "
            "rather than leaving it inside a story chunk's own Usage Guidance prose, per this step's "
            "own launch brief. relations[] carries one gravity edge (G1) named in this script's own "
            "docstring under RECIPROCITY. Distinct from don.contested.circumcellion-character: a "
            "different council, a different sole source (Optatus alone, no CTh 16.5.52 or Registry-"
            "row-24 material involved), and a different kind of contest (what a specific ruling "
            "MEANT, not a group's own character and scale) -- not a duplicate treatment of the same "
            "underlying material. Does not touch Article 29 Limb 2: Optatus is not one of the two "
            "figures (Cyprian, Augustine) that gate names, and the ruling's own meaning is not a "
            "present-day-tradition-mediation question."
        ),
    )


def main() -> None:
    build_bishop_count()
    build_circumcellion_character()
    build_maximianist_reception()
    build_cirta()
    print(f"Wrote {len(WRITTEN)} records:")
    for p in WRITTEN:
        print(f"  {p}")


if __name__ == "__main__":
    main()
