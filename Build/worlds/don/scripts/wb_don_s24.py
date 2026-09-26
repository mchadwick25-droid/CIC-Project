"""B-4 (S2.1): Donatism (don) story + figure + quote records.

WHAT THIS SCRIPT DOES. Converts this world's already-built, already-reviewed
Story Inventory (Doc_09_Story_Inventory.md) and its nine deployment-facing
Story-Chunks (Story-Chunks/donstoryNNN_*.md) into record-native `story`
records under records/don/story/, per the live schema (engine/m1/schemas.py)
and gate battery (engine/m1/gates.py). It also authors `figure` records for
every named person this world's own build treats as load-bearing enough to
need a name-bridge (Doc_09's own story cast, plus the Doc_04/don_World_Profile
primate-succession backbone of G4, plus the two dominant hostile-mediating
authors named as the source in nearly every story's own Usage Guidance), and
`quote` records for the small, bounded set of primary lines this world's own
Representative Permanent Prompt (don_Representative_Permanent_Prompt_Fidelis.txt)
already names as its licensed Approved-Source vocabulary. This is B-4 of the
9-step record-native build pipeline (B-1 through B-9); B-1 (source +
world_core), B-1a (search_record), and B-2/B-3 (21 term records) are already
done and committed. Read Build/worlds/don/scripts/wb_don_s21.py and
wb_don_s22_s23.py in full before this script was written (not touched by it,
not re-run by it) for the docstring/code-pattern discipline this script
follows.

INPUTS, mapped to OUTPUTS, precisely:
  - Doc_09_Story_Inventory.md Section 3 (Story Index, tier/confidence/source
    per story) and Section 3.1 (By-Tier View) -> the authoritative tier
    assignment for every story record below. Tiers are NOT re-derived here;
    they are copied from Doc_09's own table (seven Tier 1, two Tier 3, zero
    Tier 2, zero Tier 4 -- Doc_09's own closing line).
  - Story-Chunks/donstory001_passio-donati-sermon.md through
    donstory009_tyconius-condemnation.md (all nine files; the directory was
    listed directly this session, not assumed at nine) -> the nine `story`
    records' own narrative_tier_justification, tellable_as, text,
    absent_detail fields, mapped directly from each chunk's own "Story Text"
    (-> text), "Tier Justification" (-> narrative_tier_justification,
    condensed), and "Usage Guidance"/"Tier Justification" caveats (->
    absent_detail) sections -- the same section-to-field mapping the launch
    brief names. modern_contrast is NOT present in the Story-Chunk template
    (a later schema-only field, per schemas.py's own comment that it postdates
    the chunks) and is freshly authored here per story, grounded in that
    story's own already-established content, not in outside historical
    knowledge.
  - don_Representative_Permanent_Prompt_Fidelis.txt's own Approved Source
    paragraph (line 31, the "reach for what our own life actually gave us"
    passage) -> the bounded quote set. Six items are named there: Petilian's
    argument, Donatus's retort, the Deo laudes/Bagai acclamation, the
    anniversary sermon, Macrobius's letter, and Emeritus's plea. Only FOUR
    become `quote` records here -- see "QUOTE SET, BOUNDED" below for why the
    other two (the anniversary sermon, Macrobius's letter) are deliberately
    not built as separate quote records.
  - Doc_04_Gravity_Discovery.md and don_World_Profile.md (line 219: "a
    primate at Carthage (Donatus, then Parmenian, then Primian)") -> the
    four-figure primate-succession backbone (Majorinus, Donatus, Parmenian,
    Primian) that G4 -- Parallel Institutional Hierarchy is built on, per the
    launch brief's own instruction to check these two documents for
    gravity-central figures without a dedicated story of their own.
  - Direct, independent re-verification this session (not assumed from any
    prior document's paraphrase) against the raw vendored files for all four
    quotes and the Emeritus figure's own plea: cic/texts/
    npnf104_augustine-anti-manichaean-anti-donatist.xml (Petilian, both the
    Prolegomena's summary at line 10280 and the actual translated text's own
    direct attribution at line 15788, "Book II, Chapter 3": '"Petilianus
    said: 'For what we look to is the conscience of the giver, to cleanse
    that of the recipient.'"'); cic/texts/optatus_against-the-donatists.txt
    (Donatus's retort, line 1904, Book III, Vassall-Phillips's own published
    translation); cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt
    (Emeritus's plea, line 126834, act 50: raw OCR "Magno irgnmento
    vc-rilas occullaiur" independently read as "Magno argumento veritas
    occultatur," matching Doc_02's own already-published cleaned Latin and
    English exactly); cic/texts/cil8-supplementum-numidiae_cagnat-schmidt1894.txt
    (the Deo laudes inscription, CIL VIII 17732, matching Doc_02's own
    citation).

QUOTE SET, BOUNDED -- the judgment call this script's own launch instructions
name explicitly and require named here. The Permanent Prompt's Approved
Source paragraph names six items; this script builds `quote` records for
only four of them:
  1. Petilian's argument ("the conscience of the giver...") -- BUILT
     (don.quote.petilian-conscience-of-the-giver). An established published
     translation exists (NPNF, vol. 4) and the exact quoted attribution
     ("Petilianus said: ...") was independently re-located this session.
  2. Donatus's retort ("Quid est imperatori cum ecclesia?") -- BUILT
     (don.quote.donatus-quid-est-imperatori). An established published
     translation exists (Vassall-Phillips, 1917) and the passage was
     independently re-located this session (Book III, line 1904).
  3. Emeritus's plea ("magno argumento veritas occultatur") -- BUILT
     (don.quote.emeritus-magno-argumento). No established published English
     translation of the Gesta exists, but Doc_02_Source_Ecology.md SS1 already
     supplies and uses a translation ("the truth is concealed by a great
     [rhetorical] device") -- that already-used rendering is what this
     record's modern_rendering is grounded in, per this step's own
     instruction not to invent a fresh translation from this session's own
     knowledge of the Latin. Doc_02's own OCR-quality caution for this file
     is carried into this record's divergence_note, not silently dropped.
  4. The Deo laudes / Bagai acclamation -- BUILT
     (don.quote.deo-laudes-acclamation). Epigraphic, independently
     catalogued (CIL VIII 17732), with an established translation already
     in this world's own build (Doc_02 SS5, Doc_03: "Praise to God").
  5. The anniversary sermon (donstory001, the Passio Donati) -- NOT built as
     a separate quote record. donstory001's own Tier Justification states
     plainly that "this sermon survives only in raw, uncorrected Latin OCR...
     no established published English translation was consulted for this
     chunk," and that its two short quoted phrases are "close, literal
     renderings of short, simple phrases -- not a claim of certified
     translation." Building a `quote` record (which requires a
     modern_rendering grounded in an actual, already-used translation) from
     a passage this world's own Story-Chunk itself declines to present as a
     certified verbatim quotation would manufacture the false confidence
     the Story-Chunk was written specifically to avoid. The full account
     remains fully available as don.story.passio-donati-sermon.
  6. Macrobius's letter (donstory003) -- NOT built as a separate quote
     record, for the identical reason: donstory003's own Tier Justification
     states "this letter survives only in raw, uncorrected Latin OCR... no
     established published English translation of it was consulted," and
     Isaac's own cry to his tormentors is deliberately rendered as reported
     speech rather than a quotation for exactly that reason. The full
     account remains fully available as
     don.story.macrobius-letter-isaac-maximianus.
This is a disclosed narrowing of the Permanent Prompt's own six-item list to
a four-item quote-record set, not a silent one -- the Permanent Prompt's own
prose already carries the anniversary sermon and Macrobius's letter as
narratable material (which the story records fully cover); it does not by
itself require each of the six to also become a standalone `quote` record,
and this script does not manufacture a translation this world's own build
never certified in order to force a sixth or fifth quote record into
existence.

FIGURE SET, AND WHY EACH ONE -- sixteen figures, each tied to one of three
grounds named in the launch brief, not a blanket "every name in every story"
sweep (which would run past thirty names across the nine chunks alone):
  (a) the person is the central, named subject of at least one dedicated
      Doc_09 story: Marculus (donstory002), Macrobius and the paired
      Isaac/Maximianus (donstory003), Lucilla (donstory004/005), Felix of
      Aptungi (donstory006), Tyconius (donstory009);
  (b) the person is load-bearing for a gravity's own institutional backbone
      without a dedicated story of their own, per Doc_04/don_World_Profile
      (the launch brief's own named check): the four successive Carthage
      primates Majorinus -> Donatus -> Parmenian -> Primian, the spine of
      G4 -- Parallel Institutional Hierarchy (don_World_Profile.md line 219);
      Caecilian, the rival bishop whose contested consecration is this
      world's own G1 founding fact, recurring across four stories
      (001, 004, 005, 006) without a dedicated story naming him as its own
      subject; Purpurius, named as the same recurring bishop-agitator across
      two stories (004 and 007, the second explicitly cross-referencing the
      first: "the same figure who would later mock Caecilian");
  (c) the person is one of this world's own bounded Approved-Source
      speakers who needs a name-bridge before their words can be voiced:
      Petilian and Emeritus, named together in Doc_02 SS3 as "the two
      principal Donatist champions" at the 411 Conference and each carrying
      one of the four built quotes;
  (d) the person is the dominant hostile-mediating author named, by name, as
      THE source in the Usage Guidance of most of these stories -- Optatus
      (source for 004, 005, 006, 007) and Augustine (source for 008, 009,
      and the transmitting author of the Petilian quote). Building figure
      records for the two names this world's own Author Gravity problem
      (Doc_01 SS7 item 1; Doc_02 SS1) is built around matches this project's
      own precedent (hal.figure.augustine, cappadocian.figure.julian: a
      hostile or opposing figure a Representative must still name and
      introduce gets a figure record in this project when load-bearing
      enough).
NOT built as figures, a disclosed bound rather than an oversight: every
other named person appearing exactly once in exactly one story (Leontius,
Ursatius, Marcellinus, Honoratus of Sicilibba in donstory001; Mensurius,
Botrus, Celestius in donstory004; Zenophilus, Nundinarius, Saturninus,
Victor, Castus, Crescentianus in donstory005; Constantine, Aelianus,
Ingentius, and the five named deponents in donstory006; Secundus of
Tigisis, "Secundus the Less," Victor of Garba, Felix of Rotarium, Nabor of
Centurio in donstory007; Maximian, Felicianus of Musti, Praetextatus of
Assuris, Optatus Gildonianus in donstory008). These names remain fully
available inside their own story's own `text` field; this script does not
build a name-bridge for a name this world's own record uses only once.

RELATIONS -- CLOSED-GRAPH DISCIPLINE. records/don/gravity/,
records/don/force/, and records/don/contested_claim/ do not exist yet (later
build steps); a `relations[]` entry pointing at a don.gravity.* or
don.term.* id would resolve under gate_referential (term records already
exist) but would then fail gate_reciprocity, because this script's own
constraints forbid touching records/don/term/ to add the required inverse
back. Every `relations[]` entry this script writes therefore points only at
another record this same script creates (story<->story, story<->figure,
story<->quote, figure<->figure, figure<->quote) -- a fully closed graph,
built and reciprocated by one master pair-list (RELATION_PAIRS below) so
every edge is declared on both ends by construction, not by hand-checking
each record afterward. Gravity/term/gravity-cell connections are named in
each record's own prose body instead, exactly where B-2/B-3's own term
records already name their own gravity connections in prose rather than in
relations[].

MECHANICAL vs AUTHORED, field by field:
  - id, world_id, record_type, schema_version, status, register, canon_cells:
    MECHANICAL. register="emic" throughout (formation-facing story/figure/
    quote material, matching hal/desert/cappadocian precedent -- distinct
    from source records' own register="etic"). canon_cells=[] throughout --
    no canon-cell tagging work has happened for this world yet (unchanged
    from B-1's own note).
  - narrative_tier: MECHANICAL -- copied directly from Doc_09 Section 3's
    own table. NOT re-derived by this script.
  - narrative_tier_justification, tellable_as, text, absent_detail: AUTHORED,
    condensed and adapted from each Story-Chunk's own already-reviewed prose
    (Tier Justification / Story Text / Usage Guidance sections respectively),
    not reworded from this session's own outside knowledge of Donatist
    history. `text` avoids the literal phrases "this world" and "the
    world's" throughout (gate_voice_perspective's own scoped fields), using
    "this community" or the specific named parties instead, matching what
    each Story-Chunk's own Story Text section already does.
  - modern_contrast: AUTHORED fresh per story (the field postdates the
    Story-Chunk template, per schemas.py's own comment), grounded in that
    story's own already-cited content, naming one specific modern assumption
    the story's own record complicates or reverses.
  - confidence.*: AUTHORED per record, translating each Story-Chunk's own
    free-text "Confidence:" line and Tier Justification into the schema's
    enums, following the same citation_specificity/verification_state
    calibration B-1's own script established, with one addition specific to
    this step: verification_state is held to verified-via-authority (not
    verified-direct) wherever this script is relying on Doc_09/the
    Story-Chunk's own already-completed verification rather than an
    independent re-check of the raw vendored file THIS session -- reserving
    verified-direct for the four places this script actually re-opened a
    primary text itself (the four quotes, and the Emeritus figure record,
    whose own plea this script independently re-located at
    cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt line
    126834 rather than only citing Doc_02's prior finding of it).
  - sources[]: AUTHORED per record from each Story-Chunk's own Source field,
    resolved to the don.source.* ids B-1 already created (cross-checked
    against Build/worlds/don/scripts/wb_don_s21.py's own emitted id
    list, not guessed).
  - names[], dates, narratable, bridge_line (figure only): AUTHORED per
    figure from the same Story-Chunk/Doc_02/don_World_Profile material,
    never from this session's own outside knowledge of Donatist history --
    every specific date or role claim below traces to a passage read this
    build (cited inline in each figure's own body text).
  - text, speaker_or_author, license, modern_lens_note, modern_rendering
    (quote only): AUTHORED per quote. modern_rendering is a light
    modernization of an already-published or already-used translation (NPNF,
    Vassall-Phillips, or Doc_02's own rendering), never a fresh translation
    from this session's own knowledge of the Latin, per this step's own
    constraint.
  - retrieval.tier (1-3, story/quote only): AUTHORED, a judgment call this
    script names rather than hides: tier 1 for the story/quote this script
    judges the more central, general-purpose retrieval candidate within its
    own cluster; tier 2 for the more specialized contrast/companion case
    within the same cluster (e.g. donstory002's fuller hagiographic register
    is tier 2 against donstory003's tier 1 documentary register for the same
    persecution, matching the "Do-Not-Retrieve-When" cross-references each
    chunk already states explicitly).

DISCREPANCIES / GAPS NAMED, not silently carried forward:
  - Doc_09 Section 6 names two candidates surfaced but NOT built as their
    own story chunks this build: Donatus's retort as a standalone story
    (folded instead into Doc_04 §3.6/T2 gravity-discovery prose -- this
    script's own don.quote.donatus-quid-est-imperatori record is the closest
    thing to a dedicated retrievable unit for it, matching Doc_09's own
    "flagged for a future pass if T1's own encounter usage is found to need
    a standalone retrievable story" note); and the Circumcellion mobilization
    under Axido and Fasir (the Octavensis killings, the priest Clarius) --
    a genuine discovery Doc_09 itself declines to build pending dedicated
    Article 23 handling. Neither is built as a story or figure record here;
    both remain open items for a future pass, exactly as Doc_09 leaves them.
  - Doc_09 Section 8 (Absent Stories) names three structural absences this
    script does not attempt to close: no ordinary Numidian believer's own
    voice exists at any tier; the 411 Conference of Carthage (this world's
    single largest recorded event) has no story built despite being
    vendored, blocked only on being written, not on being found; no
    Donatist-side account of the Bagai-era Circumcellion violence against
    Catholics survives. This script builds don.figure.emeritus and
    don.figure.petilian (both attested partly through the 411 Conference
    transcript) and don.quote.emeritus-magno-argumento (drawn directly from
    that transcript), but does NOT build a story chunk for the Conference
    itself -- Doc_09 explicitly did not build one, and inventing one here
    would be exactly the kind of undisclosed narrative construction this
    world's own "no Tier 5" rule and this step's own brief both forbid. The
    absence stands, named here rather than quietly worked around.
  - Doc_02's own OCR-quality caution for the Migne PL11 Gesta scan ("notably
    poor even by this corpus's own standards") is carried forward into
    don.figure.emeritus's and don.quote.emeritus-magno-argumento's own
    divergence_note, not smoothed into an unqualified Documented rating.

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells; touch records/don/term/,
records/don/source/, or records/don/world_core/ (existing B-1/B-2/B-3
records are read, never edited); create don.gravity.*, don.force.*, or
don.contested_claim.* records (later steps); build a story or figure record
for the 411 Conference of Carthage, the Circumcellion/Axido-Fasir material,
or any name appearing only once in exactly one Story-Chunk (see "FIGURE SET"
above); register `don` in records/worlds.yaml (B-9); run the M2 compiler;
touch any world other than don.
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]  # .../cic-project
RECORDS_ROOT = REPO_ROOT / "records" / "don"
STORY_CHUNKS_DIR = HERE.parents[0] / "Story-Chunks"

WORLD_ID = "don"
SCHEMA_VERSION = 2

WRITTEN: list[str] = []

# ---------------------------------------------------------------------------
# RELATION_PAIRS: the whole closed relation graph, each edge listed once as
# (type_a_to_b, id_a, id_b). Every entry here uses "associated-with", the one
# symmetric relation type (RELATION_INVERSE maps it to itself) -- the loose,
# contextual connection every one of these pairs actually is, matching
# desert/cappadocian precedent for story<->figure/story<->story linking.
# Building both directions from one list, rather than writing each side by
# hand twice, is what keeps this a closed graph: every id below must appear
# as a story/figure/quote this script actually emits, or the assertion in
# main() catches the mismatch before any file is written.
RELATION_PAIRS: list[tuple[str, str]] = [
    ("don.story.passio-donati-sermon", "don.figure.caecilian"),
    ("don.story.passio-donati-sermon", "don.figure.donatus"),
    ("don.story.passio-marculi", "don.figure.marculus"),
    ("don.story.passio-marculi", "don.story.macrobius-letter-isaac-maximianus"),
    ("don.story.macrobius-letter-isaac-maximianus", "don.figure.macrobius"),
    ("don.story.macrobius-letter-isaac-maximianus", "don.figure.isaac-and-maximianus"),
    ("don.story.lucilla-consecration-dispute", "don.figure.lucilla"),
    ("don.story.lucilla-consecration-dispute", "don.figure.caecilian"),
    ("don.story.lucilla-consecration-dispute", "don.figure.majorinus"),
    ("don.story.lucilla-consecration-dispute", "don.figure.purpurius"),
    ("don.story.lucilla-consecration-dispute", "don.figure.optatus"),
    ("don.story.lucilla-consecration-dispute", "don.story.gesta-apud-zenophilum"),
    ("don.story.gesta-apud-zenophilum", "don.figure.lucilla"),
    ("don.story.gesta-apud-zenophilum", "don.figure.optatus"),
    ("don.story.acta-purgationis-felicis", "don.figure.felix-of-aptungi"),
    ("don.story.acta-purgationis-felicis", "don.figure.caecilian"),
    ("don.story.acta-purgationis-felicis", "don.figure.optatus"),
    ("don.story.acta-purgationis-felicis", "don.story.council-of-cirta"),
    ("don.story.council-of-cirta", "don.figure.purpurius"),
    ("don.story.council-of-cirta", "don.figure.optatus"),
    ("don.story.bagai-reconciliation", "don.figure.primian"),
    ("don.story.bagai-reconciliation", "don.figure.augustine"),
    ("don.story.bagai-reconciliation", "don.quote.deo-laudes-acclamation"),
    ("don.story.bagai-reconciliation", "don.story.tyconius-condemnation"),
    ("don.story.tyconius-condemnation", "don.figure.tyconius"),
    ("don.story.tyconius-condemnation", "don.figure.parmenian"),
    ("don.story.tyconius-condemnation", "don.figure.augustine"),
    ("don.figure.donatus", "don.figure.majorinus"),
    ("don.figure.donatus", "don.figure.parmenian"),
    ("don.figure.parmenian", "don.figure.primian"),
    ("don.figure.parmenian", "don.figure.tyconius"),
    ("don.figure.majorinus", "don.figure.lucilla"),
    ("don.figure.majorinus", "don.figure.caecilian"),
    ("don.figure.caecilian", "don.figure.felix-of-aptungi"),
    ("don.figure.petilian", "don.figure.emeritus"),
    ("don.figure.petilian", "don.figure.augustine"),
    ("don.figure.macrobius", "don.figure.isaac-and-maximianus"),
    ("don.figure.purpurius", "don.figure.caecilian"),
    ("don.figure.petilian", "don.quote.petilian-conscience-of-the-giver"),
    ("don.figure.donatus", "don.quote.donatus-quid-est-imperatori"),
    ("don.figure.emeritus", "don.quote.emeritus-magno-argumento"),
    ("don.figure.optatus", "don.quote.donatus-quid-est-imperatori"),
    ("don.figure.augustine", "don.quote.petilian-conscience-of-the-giver"),
]


def relations_for(rid: str) -> list[dict]:
    out = []
    for a, b in RELATION_PAIRS:
        if a == rid:
            out.append({"type": "associated-with", "target": b})
        elif b == rid:
            out.append({"type": "associated-with", "target": a})
    return out


def conf(cite, verify, weight, formation, divergence=None):
    if formation == "Documented" and divergence is None:
        assert verify == "verified-direct", (
            "would trip gate_confidence_crosscheck: Documented + null divergence_note requires "
            "verified-direct"
        )
    return {
        "citation_specificity": cite,
        "verification_state": verify,
        "evidentiary_weight": weight,
        "formation_confidence": formation,
        "divergence_note": divergence,
    }


def _write(record_type: str, rid: str, payload: dict, body: str) -> None:
    out_dir = RECORDS_ROOT / record_type
    out_dir.mkdir(parents=True, exist_ok=True)
    front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    text = f"---\n{front}---\n{body.strip()}\n"
    path = out_dir / f"{rid}.md"
    path.write_text(text, encoding="utf-8")
    WRITTEN.append(str(path))


def emit_story(slug, tier, tier_just, tellable_as, text, absent_detail, modern_contrast,
               confidence, sources, retrieve_tier, retrieve_when, do_not_retrieve_when, body):
    rid = f"don.story.{slug}"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "story",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": confidence,
        "sources": sources,
        "retrieval": {
            "tier": retrieve_tier,
            "retrieve_when": retrieve_when,
            "do_not_retrieve_when": do_not_retrieve_when,
        },
        "relations": relations_for(rid),
        "narrative_tier": tier,
        "narrative_tier_justification": tier_just,
        "tellable_as": tellable_as,
        "text": text,
        "absent_detail": absent_detail,
        "modern_contrast": modern_contrast,
    }
    _write("story", rid, payload, body)


def emit_figure(slug, names, dates, narratable, bridge_line, confidence, sources, body):
    rid = f"don.figure.{slug}"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "figure",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": confidence,
        "sources": sources,
        "names": names,
        "dates": dates,
        "narratable": narratable,
        "bridge_line": bridge_line,
        "relations": relations_for(rid),
    }
    _write("figure", rid, payload, body)


def emit_quote(slug, text, speaker_or_author, license_, modern_lens_note, modern_rendering,
               confidence, sources, retrieve_tier, retrieve_when, do_not_retrieve_when, body):
    rid = f"don.quote.{slug}"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "quote",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": confidence,
        "sources": sources,
        "retrieval": {
            "tier": retrieve_tier,
            "retrieve_when": retrieve_when,
            "do_not_retrieve_when": do_not_retrieve_when,
        },
        "relations": relations_for(rid),
        "text": text,
        "speaker_or_author": speaker_or_author,
        "license": license_,
        "modern_lens_note": modern_lens_note,
        "modern_rendering": modern_rendering,
    }
    _write("quote", rid, payload, body)


# ===========================================================================
# STORIES (9) -- one per Story-Chunks/donstoryNNN_*.md, tiers copied from
# Doc_09 Section 3's own table.
# ===========================================================================

def build_stories() -> None:
    emit_story(
        "passio-donati-sermon", 3,
        "Tier 3 (Doc_09 SS3): authorship is genuinely contested between two vendored "
        "authorities -- Mabillon dates the persecution to c. 340 without naming an author; "
        "Monceaux dates it to 12 March 317 (composed c. 320) and proposes, without asserting as "
        "settled, that the preacher was Donatus the Great himself -- which rules out Tier 1's own "
        "named-author requirement outright. It is a single sermon, not a collected anthology, so "
        "Tier 2 does not fit either. Tier 3 is the precise fit: material 'attributed to specific "
        "figures or moments but resting on collected tradition,' and the strongest evidence for "
        "that fit is the annual commemoration itself, independently attested by the sermon's own "
        "words ('in solemni et anniversaria commemoratione') regardless of who first delivered it "
        "(Story-Chunks/donstory001, Tier Justification).",
        "The sermon read every year at the martyrs' own grave, remembering what was done at "
        "Carthage in the name of unity",
        "Every year, on the twelfth of March -- \"the fourth of the Ides of March,\" in the "
        "sermon's own reckoning -- this community gathers to remember what was done at Carthage in "
        "the name of unity.\n\n"
        "The account it tells is not soft. Imperial agents -- Leontius, a count, and Ursatius, a "
        "duke -- came under orders to enforce a single church, with the bishop Caecilian and the "
        "tribune Marcellinus standing behind them. Soldiers seized a basilica. What had been a "
        "house of prayer became, in the sermon's own bitter phrase, a place of feasting and "
        "license. A boy, a catechumen not yet baptized, lay dying inside it and begged those "
        "around him for help. Whether he received what he asked is not the point the sermon "
        "lingers on; that he asked it, in that place, at that hour, is.\n\n"
        "A bishop named Honoratus of Sicilibba felt a tribune's sword graze his throat and lived. "
        "Others did not. The sermon says they were killed inside the basilica itself -- not by the "
        "sword, but by clubs, while they knelt at prayer with their eyes closed, trusting the "
        "ground they stood on. Every age, every sex, the account insists. They were buried where "
        "they fell, within the building's own walls, because there was nowhere else and no one to "
        "stop it. A bishop arriving from Advocata to see what was happening was killed before he "
        "could so much as drink water offered to him.\n\n"
        "This is what is read aloud, every twelfth of March, to a congregation that was not there "
        "and cannot verify every particular -- and reads it anyway, because the day itself is how "
        "this community has chosen to keep faith with what it believes happened to its own.",
        "This sermon's own precise date and author are not established -- Mabillon and Monceaux "
        "disagree by two decades and do not agree on an author at all. No established published "
        "English translation of the sermon exists (it survives only in raw, uncorrected Latin "
        "OCR); this record follows Story-Chunks/donstory001's own discipline of rendering the "
        "narrative in indirect, reported form for this reason, rather than presenting an "
        "uncertified translation as a verbatim quotation.",
        "A modern reader tends to think of a religious anniversary as a private, optional "
        "observance one can skip a year without consequence. This sermon's own community treated "
        "the twelfth of March as a mandatory, communal act of formation -- a day the whole "
        "community was expected to keep, together, aloud, not a private choice -- and it is that "
        "yearly repetition, not any one person's private memory, that kept a persecution decades "
        "past from becoming merely historical.",
        conf("B", "verified-via-authority", "load-bearing", "Contested",
             "Formation_confidence held at Contested, not Documented, because the sermon's own "
             "authorship and precise date are reported from two disagreeing vendored authorities "
             "(Mabillon, c. 340, no author; Monceaux, 317/320, possibly Donatus the Great) that "
             "this record does not resolve between (Story-Chunks/donstory001, Tier Justification; "
             "Doc_02 SS4, SS8)."),
        [{"source_id": "don.source.passio-donati-sermon",
          "locus": "the whole sermon; cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt, "
                   "lines 88-664",
          "license": "public-domain"},
         {"source_id": "don.source.monceaux-histoire-litteraire-tome5",
          "locus": "the Passio Donati chapter's own dating/authorship argument, contested against "
                   "Mabillon's apparatus",
          "license": "public-domain"}],
        2,
        ["participant asks how this community commemorates its own dead or marks anniversaries "
         "of persecution",
         "participant asks whether this community has liturgical practices distinct from the "
         "Catholic mainstream",
         "participant asks what being formed by martyrdom felt like from the inside, rather than "
         "as an outside description"],
        ["participant is asking for a neutral historical narrative of who did what to whom at a "
         "specific dated event (don.story.acta-purgationis-felicis or don.story.council-of-cirta "
         "serve that need more precisely)",
         "the conversation needs a story with a securely named, undisputed author"],
        "Mapped directly from Story-Chunks/donstory001_passio-donati-sermon.md's own Retrieval "
        "Front-Matter, Story Text, Tier Justification, and Usage Guidance sections, per this "
        "step's own field-mapping instruction. absent_detail and the indirect-speech rendering of "
        "the boy's cry and Honoratus's own wounding both preserve the chunk's own explicit "
        "certified-translation caveat rather than upgrading it. The contested authorship candidacy "
        "of Donatus the Great is carried into relations[] (don.figure.donatus) as an association, "
        "not an attribution -- the chunk's own Usage Guidance is explicit that 'the Representative "
        "should not attribute this sermon to Donatus the Great as settled fact.'",
    )

    emit_story(
        "passio-marculi", 3,
        "Tier 3 (Doc_09 SS3): anonymous, near-contemporary composition carrying, in textbook "
        "form, the three markers Tier 3's own definition names for hagiographic narrative -- the "
        "miracle sequence (the cup/crown/palm vision, the unbroken fall, the guiding light), the "
        "idealized portrait (a man who had already renounced worldly advancement before "
        "persecution arrived), and the death as completion of a formed life (the vision shown "
        "before the death, then delivered exactly as shown). The general portrait (that Marculus "
        "died at Macarius's hands, resisting a persecution operation) is Contested-confidence, "
        "corroborated even by the hostile Optatus/Augustine material; the specific visionary and "
        "miraculous details are Inferential/Thin, per Tier 3's own confidence rule for "
        "genre-shaped detail (Story-Chunks/donstory002, Tier Justification).",
        "Marculus's own death at the cliff of Novapetra, shown in advance what completing a "
        "formed life would look like",
        "The tradition remembers Marculus as a man who had already given up what the world offers "
        "before persecution ever reached him -- a life of unusual virtue, a refusal of worldly "
        "advancement, given instead to the church.\n\n"
        "When Macarius's persecution came into Numidia, ten bishops were sent either to persuade "
        "Marculus's own community to submit or to join the resistance themselves instead. "
        "Marculus was seized at a place called Vegesela. He was bound to columns and flogged, and "
        "the tradition insists he bore it without visible pain, praising God the whole time. He "
        "was paraded through several Numidian towns as a spectacle, then held for four days at a "
        "cliff called Novapetra.\n\n"
        "In that waiting, the tradition says, he fasted, and he was given a vision: a cup, a "
        "crown, and a palm, shown to him together, the way the community remembers such things "
        "being shown to those about to complete a formed life. Before dawn, he was thrown from the "
        "cliff. The tradition holds that his body did not break on the fall, and that a light "
        "settled over the place afterward, bright enough that the brethren could find him and "
        "take him for burial before anyone could stop them.\n\n"
        "This is how the tradition remembers Marculus: not as a man who died, but as a man shown, "
        "in advance, what completing his own formation would look like -- and then given exactly "
        "that.",
        "The cliff-top vision, the unbroken fall, and the guiding light are the tradition's own "
        "testimony to what it believed formation produced, not a claim about what a modern "
        "observer would have seen. The hostile Catholic side does not accept this death as "
        "martyrdom at all, on two separate grounds: Optatus argues the deaths were deserved "
        "punishment for schism; Augustine, separately, disputes whether Marculus was thrown or "
        "threw himself.",
        "A modern reader tends to assume a 'miracle account' and a 'documentary account' of the "
        "same event are mutually exclusive registers -- one credulous, one reliable. This world's "
        "own corpus places both side by side, deliberately, about the same 347-348 persecution "
        "(this story and don.story.macrobius-letter-isaac-maximianus), treating them as different "
        "kinds of evidence for different kinds of claims rather than competing versions of one "
        "truth.",
        conf("A", "verified-via-authority", "load-bearing", "Contested",
             "General portrait Contested (corroborated even by hostile Optatus/Augustine "
             "material that the death occurred); specific visionary and miraculous detail "
             "Inferential-Thin, per Tier 3's own confidence rule (Story-Chunks/donstory002, Tier "
             "Justification)."),
        [{"source_id": "don.source.passio-marculi",
          "locus": "the whole Passio; cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt, "
                   "lines 664-1359",
          "license": "public-domain"},
         {"source_id": "don.source.optatus-against-donatists",
          "locus": "'Against the alleged Donatist martyrs,' arguing the deaths deserved "
                   "punishment for schism",
          "license": "public-domain"},
         {"source_id": "don.source.augustine-answer-to-letters-of-petilian",
          "locus": "II.45-46, disputing whether the deaths qualify as martyrdom",
          "license": "public-domain"}],
        2,
        ["participant asks what a martyr's death was believed to look like, or what dying well "
         "meant within this tradition",
         "participant asks about the Macarian persecution (347-348) specifically",
         "conversation needs this tradition's own fullest hagiographic-register account, distinct "
         "from the more documentary don.story.macrobius-letter-isaac-maximianus"],
        ["participant wants a historically cautious, minimally-embellished account of the same "
         "persecution (don.story.macrobius-letter-isaac-maximianus serves that need)",
         "participant is asking whether the Catholic side accepted this as genuine martyrdom (it "
         "did not, on two separate grounds)"],
        "Mapped directly from Story-Chunks/donstory002_passio-marculi.md. The corroborating-but-"
        "disputing hostile sources (Optatus, Augustine) are carried in sources[] exactly as the "
        "chunk's own Source field lists them, not smoothed into a single citation.",
    )

    emit_story(
        "macrobius-letter-isaac-maximianus", 1,
        "Tier 1 (Doc_09 SS3): Macrobius names himself, identifies his own office (bishop) and the "
        "specific congregation he addresses, and writes close in time (347-348) to the events "
        "described -- every element Tier 1 requires, and the element that donstory001 and "
        "donstory002 both lack. This is a disclosed departure from Doc_05 SS11's own handoff, "
        "which grouped all three Macarian-persecution martyr texts together as 'Tier 2/3 "
        "material'; this text alone, of the three, carries a named author writing in his own "
        "voice to a real, identified audience (Story-Chunks/donstory003, Tier Justification).",
        "Macrobius's own letter to his Carthage congregation, telling them what happened to Isaac "
        "and Maximianus",
        "Macrobius wrote to his own congregation at Carthage as their bishop, in the aftermath of "
        "what he had witnessed, to tell them what had happened to two of their own.\n\n"
        "Maximianus, a soldier of Christ in the tradition's own description, was chosen to face "
        "the Roman proconsul first. The night before, at a shared meal, wine in his cup seemed to "
        "take the shape of a ring, shining with the mingled colors of blood and light -- an omen, "
        "Macrobius wrote, of what the next day would ask of him. He was beaten with leaded whips, "
        "then with rods. Isaac was flogged alongside him, and in the middle of it he called out to "
        "the men doing the flogging, naming them traditores and telling them to come and see what "
        "their so-called unity's madness had brought them to. He did not survive the beating.\n\n"
        "Maximianus, still living, had his own vision that night: he saw himself in combat, first "
        "against the emperor's own ministers, and then against the emperor himself, who in the "
        "dream struck out one of his eyes -- and then a bright youth appeared and crowned him. The "
        "Roman proconsul, wanting neither of them venerated as relics afterward, ordered both "
        "bodies thrown into the sea, weighted down with jars filled with sand.\n\n"
        "The sea would not keep them. Macrobius's letter says the bodies rose and were driven back "
        "toward shore again and again, for six days, until finally both were delivered up whole to "
        "the congregation waiting for them, who took them and buried them with the same rites and "
        "the same joy they would have given the living.\n\n"
        "Macrobius closes his letter by turning to his own congregation directly: what happened to "
        "Isaac and Maximianus, he tells them, is what may yet be asked of any of them.",
        "The wine-cup omen and Maximianus's combat-vision are Macrobius's own reported "
        "interpretation of these events, not independently verified occurrences. Isaac's own cry "
        "to his tormentors is rendered here as reported speech, not verbatim quotation: no "
        "established published English translation of this letter exists (it survives only in "
        "raw, uncorrected Latin OCR), and this record does not present an improvised rendering as "
        "a certified verbatim quotation.",
        "A modern reader may assume a bishop writing to comfort a grieving congregation would "
        "soften what happened. Macrobius's letter does the opposite: it closes by telling the "
        "living that the same fate may be asked of any of them -- using a specific, recent death "
        "as a direct formation instrument for those still alive, not a private consolation kept "
        "separate from what it asks of them next.",
        conf("A", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Widely Accepted to Documented at the narrative level (a named author, his own "
             "office, a real congregation, close in time to the events); Widely Accepted to "
             "Contested for the supernatural framing elements specifically (the omen, the "
             "vision), consistent with Tier 1's own allowance for author-perspective caveats "
             "(Story-Chunks/donstory003, Tier Justification)."),
        [{"source_id": "don.source.passio-isaac-et-maximiani",
          "locus": "the whole letter, preserved twice in the vendored file from two source "
                   "manuscripts; cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt, "
                   "lines 1367-2609",
          "license": "public-domain"}],
        1,
        ["participant asks for this tradition's own most directly-attested account of a specific "
         "martyrdom, with a named author writing close to the events",
         "participant asks about the Macarian persecution from a source closer to documentary "
         "than hagiographic register",
         "conversation needs a contrast case against don.story.passio-marculi's fuller "
         "hagiographic register"],
        ["participant wants the fullest hagiographic-convention martyrdom account "
         "(don.story.passio-marculi serves that need more precisely)",
         "participant's question is about the anniversary sermon's own commemoration practice "
         "rather than this specific pair of deaths"],
        "Mapped directly from Story-Chunks/donstory003_macrobius-letter-isaac-maximianus.md. "
        "Slug shortened from the chunk's own filename stem (already matches).",
    )

    emit_story(
        "lucilla-consecration-dispute", 1,
        "Tier 1 (Doc_09 SS3): direct textual attestation (Optatus I.16-20) naming every "
        "participant (Lucilla, Caecilian, Felix, Mensurius, Botrus, Celestius, Purpurius, "
        "Majorinus), datable to the founding dispute of 311/312, with Tier 1's own required "
        "caveat for hostile authorship named explicitly rather than smoothed over: Optatus's "
        "characterization of Lucilla's motive as personal spite is his own hostile framing, not "
        "an independently established fact (Story-Chunks/donstory004, Tier Justification).",
        "The rebuke, the mishandled treasury, and the rival consecration that actually started "
        "the schism",
        "Before there was a schism, there was a rebuke, delivered in public, to a woman who did "
        "not forget it.\n\n"
        "Lucilla, a wealthy laywoman of Carthage, had a habit before receiving the chalice: she "
        "would kiss the bone of a martyr she kept with her. The archdeacon Caecilian rebuked her "
        "for it -- the man had not yet even been formally acknowledged as a martyr, Caecilian "
        "said, and the practice was improper. Optatus records that Lucilla left \"full of "
        "wrath.\"\n\n"
        "Around the same time, persecution reached Carthage again. A deacon named Felix went into "
        "hiding in the house of the bishop, Mensurius. Mensurius, expecting his own exile, "
        "entrusted the church's gold and silver to a group of respected laymen, the \"seniors,\" "
        "and gave an old woman a written inventory of everything, for safekeeping until it could "
        "be recovered.\n\n"
        "When the persecution passed and Mensurius did not return, the church had to choose a new "
        "bishop. Two candidates who had expected the office -- Botrus and Celestius -- were passed "
        "over. Caecilian was elected instead. The seniors who had quietly kept more of the "
        "treasury than they should have, the two disappointed men, and Lucilla, still carrying her "
        "grievance, found they had a common cause.\n\n"
        "At a crowded assembly in the Carthage basilica, Caecilian demanded that his accusers step "
        "forward and say plainly what they charged him with. One of them, Purpurius, mocked him "
        "openly rather than answer. No proof was ever produced. What followed instead was a rival "
        "consecration -- Majorinus, a member of Lucilla's own household, was made bishop in "
        "Caecilian's place, Optatus writes, \"at her instigation, and through her bribes.\"",
        "Optatus's own characterization of personal spite as Lucilla's true motive is his own "
        "hostile framing, not an independently established fact; no surviving Donatist-authored "
        "account of these specific events exists to confirm or correct it.",
        "A modern reader tends to assume a church schism begins over abstract doctrine debated by "
        "theologians in a council hall. This world's own founding dispute began with a personal "
        "rebuke over an unauthorized relic-kiss, a mishandled treasury, and two men passed over "
        "for an office they wanted -- the doctrine came after, to explain a rupture that had "
        "already happened for entirely human reasons.",
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "The bare sequence of events (rebuke, treasury, passed-over candidates, contested "
             "election, rival consecration) is Documented; the specific motive Optatus assigns to "
             "Lucilla (personal spite) is his own hostile framing, presented as such rather than "
             "as fact (Story-Chunks/donstory004, Tier Justification)."),
        [{"source_id": "don.source.optatus-against-donatists",
          "locus": "Book I, chapters 16-20; cic/texts/optatus_against-the-donatists.txt, "
                   "lines 197-237",
          "license": "public-domain"},
         {"source_id": "don.source.lucilla-and-second-woman-maximianist",
          "locus": "Lucilla herself, cross-referenced",
          "license": "public-domain"}],
        1,
        ["participant asks how the schism actually began, at the level of specific named people "
         "and grievances, rather than only doctrine",
         "participant asks about women's roles in the founding dispute",
         "conversation reaches the founding-moment forces and needs the specific human dispute "
         "those forces trace back to"],
        ["participant wants the later legal resolution of the same treasury grievance "
         "(don.story.gesta-apud-zenophilum is the courtroom sequel and should be retrieved "
         "alongside it, not instead of it)",
         "participant is asking about the traditio accusation against Felix of Aptungi "
         "specifically (don.story.acta-purgationis-felicis covers that separate strand)"],
        "Mapped directly from Story-Chunks/donstory004_lucilla-consecration-dispute.md.",
    )

    emit_story(
        "gesta-apud-zenophilum", 1,
        "Tier 1 at its strongest available in this corpus (Doc_09 SS3): a literal court "
        "transcript, named deponents, a precise date (320), and a historically credible claim "
        "independently corroborated by a second primary source (Augustine's Letter XLIII) written "
        "from the opposing side, decades later, with no evident coordination between the two "
        "accounts (Story-Chunks/donstory005, Tier Justification).",
        "The formal inquiry into what happened to Lucilla's money, seven years after the fact",
        "In 320, before the consular official Zenophilus, a formal inquiry was opened into what "
        "had actually happened to the church's own money.\n\n"
        "Witnesses were called and questioned directly, under record: Nundinarius, a deacon; "
        "Saturninus; Victor; Castus; Crescentianus. The specific question Zenophilus put to them "
        "was pointed and financial, not doctrinal -- had four hundred pieces of silver, received "
        "from Lucilla, actually reached the poor, as had been claimed, or had it gone "
        "elsewhere?\n\n"
        "The transcript preserves the exchange as it happened: names given, questions asked, "
        "answers recorded. This is not a later writer's summary of what he understood to have "
        "occurred; it is the proceeding itself, set down as it was heard.\n\n"
        "Decades afterward, Augustine would refer back to this very episode in a letter of his "
        "own, recalling that Nundinarius, the same deacon, \"in the heat of passion revealed many "
        "secrets,\" among them that the founding of a rival altar in Carthage had been made "
        "possible by money that had come from Lucilla. Two witnesses, writing on opposite sides of "
        "the schism and decades apart, describe the same underlying fact.",
        "None beyond what the transcript itself does not cover -- the proceeding does not explain "
        "why the money was misapplied in the first place, only that it was investigated and that "
        "a deacon later admitted knowledge of it.",
        "A modern reader might assume ancient religious disputes left no paper trail beyond one "
        "side's own later argument. This proceeding is the opposite -- a formal, cross-examined "
        "transcript, corroborated decades later by a hostile witness who had every reason to let "
        "the matter drop and did not.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "don.source.optatus-appendix-of-documents",
          "locus": "Gesta apud Zenophilum; cic/texts/optatus_against-the-donatists.txt, "
                   "lines 6194-6880",
          "license": "public-domain"},
         {"source_id": "don.source.augustine-donatist-correspondence-eleven-letters",
          "locus": "Letter XLIII, corroborating Nundinarius's own disclosure; cic/texts/"
                   "npnf101_augustine-confessions-letters.xml, lines 28040-28069",
          "license": "public-domain"}],
        2,
        ["participant asks for this tradition's most documentary, least narrated evidence -- an "
         "actual court transcript rather than a later narrative account",
         "participant asks whether the traditio-era financial disputes were ever formally "
         "investigated",
         "conversation needs a story corroborated by two independent sources rather than one"],
        ["participant wants the earlier, more narrative account of how the dispute first arose "
         "(don.story.lucilla-consecration-dispute is the origin story this proceeding investigates)",
         "participant is asking about the forgery investigation into Felix of Aptungi specifically "
         "(don.story.acta-purgationis-felicis covers that separate 314 proceeding)"],
        "Mapped directly from Story-Chunks/donstory005_gesta-apud-zenophilum.md. "
        "citation_specificity/verification_state held at A/verified-direct, matching the chunk's "
        "own 'among the strongest Tier 1 candidates' framing and its own corroboration claim.",
    )

    emit_story(
        "acta-purgationis-felicis", 1,
        "Tier 1 of the strongest kind available in this corpus (Doc_09 SS3): a formal judicial "
        "proceeding, ordered by the emperor himself, conducted by a named Roman official, with "
        "named deponents giving testimony under record, resulting in a documented confession and "
        "a stated verdict -- every element of Tier 1's own definition satisfied at full strength "
        "(Story-Chunks/donstory006, Tier Justification).",
        "How the accusation against Felix of Aptungi collapsed under a forger's own confession",
        "The whole schism turned, at its root, on a single accusation: that Felix, the bishop of "
        "Aptungi who had consecrated Caecilian as bishop of Carthage, had himself been a traditor "
        "-- that he had handed over the scriptures during the persecution, and so had no standing "
        "to consecrate anyone, which would make Caecilian's own office invalid from its very first "
        "day.\n\n"
        "Constantine himself ordered the matter investigated. The proconsul Aelianus opened a "
        "formal inquiry and took testimony under record from named witnesses: Alfius Caecilianus, "
        "Maximus, Apronianus, Claudius Saturianus, Superius, and a notary named Ingentius. At the "
        "center of the case was a letter -- supposedly written by Felix himself, and read aloud in "
        "the proceeding -- that seemed to prove the accusation.\n\n"
        "Under questioning, and under the threat of torture, Ingentius broke. He confessed that he "
        "himself had forged the letter, and that he had done so as an agent working for the "
        "Donatist party, moving through Numidia and Mauritania in that service. With the forgery "
        "exposed, the case against Felix collapsed. The proceeding records his vindication as "
        "complete -- \"finally and triumphantly,\" in the text's own words.",
        "The proceeding settles only the specific charge against Felix through Ingentius's forged "
        "letter; it does not settle every allegation raised across the broader traditio dispute of "
        "this world's founding decade.",
        "A modern reader might expect a movement's own founding accusation, once formally "
        "investigated, to be either quietly dropped or triumphantly proven. This world's own "
        "record does neither -- it preserves, in its opponent's own archive, the moment its own "
        "founding case collapsed under cross-examination, and treats the honest preservation of "
        "that collapse as part of its own record rather than something to manage around.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "don.source.optatus-appendix-of-documents",
          "locus": "Acta Purgationis Felicis, Appendix I; cic/texts/"
                   "optatus_against-the-donatists.txt, lines 5467-5585",
          "license": "public-domain"}],
        1,
        ["participant asks how the traditio accusation against Felix of Aptungi was actually "
         "investigated and resolved",
         "participant asks for the strongest available Tier 1 evidence on the schism's founding "
         "legal question",
         "conversation needs the specific judicial record behind the traditio-purity doctrine"],
        ["participant is asking about the Lucilla/treasury strand specifically "
         "(don.story.lucilla-consecration-dispute and don.story.gesta-apud-zenophilum cover that "
         "separate thread)",
         "participant wants this world's own account of why the traditio question mattered "
         "doctrinally, rather than the specific 315 investigation into one man's own conduct"],
        "Mapped directly from Story-Chunks/donstory006_acta-purgationis-felicis.md. "
        "citation_specificity/verification_state A/verified-direct matches the chunk's own "
        "framing ('every element... satisfied at the fullest strength this corpus offers').",
    )

    emit_story(
        "council-of-cirta", 1,
        "Tier 1 (Doc_09 SS3): a council proceeding with named, identifiable participants (Secundus "
        "of Tigisis, Purpurius, 'Secundus the Less'), narrated within a genre (a synodal record) "
        "that carries real historical credibility even reported by a later opponent. The "
        "council's own exact date is itself disputed in this world's own Source Registry, named "
        "here rather than smoothed into false precision -- a datable-with-reasonable-confidence "
        "claim can still carry an honestly disputed exact date without falling out of Tier 1, "
        "provided the event's occurrence and substance are not themselves in serious doubt "
        "(Story-Chunks/donstory007, Tier Justification).",
        "The council where the movement's own founders first faced the traditor question among "
        "themselves, and set it aside",
        "Before Caecilian's consecration ever became the dispute it became, a council of Numidian "
        "bishops met at Cirta to consecrate a successor of their own.\n\n"
        "Secundus of Tigisis, presiding, put the question to those gathered: had any of them, "
        "under the persecution, handed over the scriptures? One by one, several admitted that they "
        "had. Then Purpurius -- the same figure who would later mock Caecilian in the Carthage "
        "basilica -- turned the question back on Secundus himself, taunting him for having been "
        "released only after remaining a long time among the soldiers; the room began to mutter "
        "that he too must have betrayed the sacred books to win that release.\n\n"
        "Secundus, unsettled, took advice from his own brother's son, called \"Secundus the "
        "Less,\" who counselled him to remit the whole affair to God rather than press it further. "
        "Secundus then turned to the three bishops present who had not themselves been accused -- "
        "Victor of Garba, Felix of Rotarium, and Nabor of Centurio -- and asked their own "
        "judgment. They answered that a case of this kind ought to be reserved to the Lord. \"Sit "
        "down, all,\" Secundus said. \"Thanks be to God,\" the assembly answered, and did. No one "
        "present was found guilty; no one was cleared. The room simply agreed not to finish the "
        "question it had started.",
        "Optatus's own characterization of the bishops' 'reserved to the Lord' ruling as evasion "
        "rather than principled restraint is his own hostile interpretation; no surviving "
        "Donatist-authored account of this council exists to confirm an alternative reading.",
        "A modern reader tends to assume a movement's own founders held its later, hardened "
        "principles from the very beginning, without complication. This council shows the "
        "opposite -- the same bishops whose own later movement would make traditor status an "
        "absolute, disqualifying category first chose, together, to set that same question aside "
        "among themselves rather than press it to a verdict.",
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "The bare facts (the council met, the traditor question was raised, several "
             "admitted responsibility, the exchange, the closing 'Thanks be to God') are "
             "Documented; the council's own precise date is disputed in the Source Registry "
             "itself (305 vs. 307 or later), named rather than resolved (Story-Chunks/"
             "donstory007, Tier Justification)."),
        [{"source_id": "don.source.optatus-appendix-of-documents",
          "locus": "Acts of the Council of Cirta (305)",
          "license": "public-domain"},
         {"source_id": "don.source.optatus-against-donatists",
          "locus": "Book I, chapter 14, narrating the council; cic/texts/"
                   "optatus_against-the-donatists.txt, lines 181-192",
          "license": "public-domain"}],
        2,
        ["participant asks whether the movement's own early leaders held themselves to the same "
         "traditor standard they applied to Caecilian and Felix",
         "participant asks about the internal complexity of the ministerial-purity question "
         "before it hardened into the schism's own defining doctrine"],
        ["participant wants a story where this world's own founding figures come through as "
         "straightforwardly vindicated -- this account emphasizes the bishops' own mutual "
         "vulnerability, and using it uncritically would misrepresent what the source says"],
        "Mapped directly from Story-Chunks/donstory007_council-of-cirta.md.",
    )

    emit_story(
        "bagai-reconciliation", 1,
        "Tier 1 of high confidence (Doc_09 SS3): the council's own decree is quoted directly (not "
        "merely summarized) in a datable primary source, the participants are named (Maximian, "
        "Primian, Felicianus of Musti, Praetextatus of Assuris, Optatus Gildonianus), and the "
        "sequence of events is corroborated across two separate works by the same author (On "
        "Baptism and Answer to the Letters of Petilian), a stronger evidentiary base than a single "
        "citation (Story-Chunks/donstory008, Tier Justification).",
        "How the movement's own leadership reconciled with the Maximianists it had just condemned "
        "in its harshest language",
        "In 393, a deacon named Maximian was elected as a rival primate at Cebarsussi, in direct "
        "defiance of Primian, the sitting Donatist primate of Carthage. It was, in miniature, the "
        "same act this movement's own founders had once taken against Caecilian: a rival "
        "consecration, answering a grievance with a new bishop rather than submission to the one "
        "already in place.\n\n"
        "The mainstream response was neither quiet nor measured. A much larger council -- three "
        "hundred and ten bishops -- met at Bagai in 394 and condemned the Maximianists in language "
        "that did not soften what it meant: the decree describes the schismatics as shipwrecked "
        "men \"dashed by the waves of truth upon the sharp rocks,\" their bodies covering the "
        "shore, so thoroughly that \"they fail to find so much as burial.\"\n\n"
        "And then, having said this, the council did something its own decree's language did "
        "nothing to prepare a listener for. When Felicianus of Musti and Praetextatus of Assuris "
        "-- two of the condemned Maximianist bishops -- were brought back into the fold, it was "
        "done without rebaptism and without reordination. A general named Optatus Gildonianus "
        "enforced the reconciliation with military force. The very men whose ordination the "
        "council had just described in the imagery of shipwreck and unburied death were received "
        "back into full office, exactly as they had been ordained under the schism the council had "
        "just condemned in the harshest terms it had at hand.\n\n"
        "Augustine seized on the contradiction directly and made it the center of his own case: if "
        "reordination could be waived here, on the mainstream Donatist party's own authority, then "
        "the absolute logic that invalidly-ordained clergy must always be rebaptized and "
        "reordained, without exception, did not hold even for the party that preached it most "
        "fiercely.",
        "Whether this reconciliation exposes the movement's own rebaptism doctrine as inconsistent, "
        "or represents a defensible pastoral exception, is not resolved by the record itself and is "
        "not resolved here.",
        "A modern reader might assume that a movement demanding absolute doctrinal consistency "
        "would apply that standard uniformly, without exception. This world's own institutional "
        "history shows its leadership choosing reconciliation and continuity of office over its "
        "own stated rebaptism principle, in the one internal crisis where applying it fully would "
        "have cost the movement most.",
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "This account survives entirely through Augustine, who quotes the Bagai decree "
             "specifically to build his own adversarial argument; this does not cast doubt on the "
             "decree's own wording, which he quotes rather than paraphrases, but the story arrives "
             "already embedded in his argument, a framing difference named rather than treated as "
             "neutral narration (Story-Chunks/donstory008, Tier Justification)."),
        [{"source_id": "don.source.augustine-on-baptism-against-donatists",
          "locus": "I.1.2, I.5.7; cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, "
                   "lines 10834-10911",
          "license": "public-domain"},
         {"source_id": "don.source.augustine-answer-to-letters-of-petilian",
          "locus": "quoting the Bagai decree; cic/texts/"
                   "npnf104_augustine-anti-manichaean-anti-donatist.xml, lines 11509-11527, "
                   "15505-15514",
          "license": "public-domain"}],
        1,
        ["participant asks how this movement's own leadership actually handled a challenge to its "
         "own rebaptism/reordination logic when the challenge came from inside the movement "
         "itself",
         "participant asks about internal schism-within-schism dynamics",
         "conversation reaches the internal Purity-Rigor-vs-Institutional-Reception tension and "
         "needs the specific episode it is built on"],
        ["participant wants a story about this movement's relationship to the Roman state "
         "specifically (Donatus's own retort serves that different tension more precisely)",
         "participant is asking about the martyr tradition rather than internal institutional "
         "discipline"],
        "Mapped directly from Story-Chunks/donstory008_bagai-reconciliation.md.",
    )

    emit_story(
        "tyconius-condemnation", 1,
        "Tier 1 (Doc_09 SS7, correcting this document's own earlier judgment): Augustine's Contra "
        "Epistulam Parmeniani I.1 is a near-contemporary primary source (Augustine writing c. 400, "
        "roughly two decades after the c. 380 condemnation) squarely within this world's own "
        "construction-window horizon, not fifteen centuries removed as an earlier draft wrongly "
        "concluded. Augustine's report of Parmenian's letter and its rebuke is stated directly, "
        "without a reporting hedge, and is Documented at that level; the specific mechanism of "
        "what followed -- a conciliar condemnation, rather than some other form of exclusion -- "
        "carries Augustine's own explicit hedge ('perhibent,' 'it is reported'), preserved rather "
        "than smoothed into unqualified fact (Story-Chunks/donstory009, Tier Justification).",
        "How Tyconius's own argument from Scripture undid him inside his own party",
        "Tyconius made an argument from Scripture too well-supported to simply dismiss, and it "
        "undid him from the inside.\n\n"
        "He argued, at length and with abundant scriptural support, that the Christians of Africa "
        "belonged to a church spread across the whole world -- connected, not by anything peculiar "
        "to Africa, but by communion with that same worldwide body. Anyone actually listening to "
        "the case he built from the text could see where it led: if that was true, the African "
        "churches still in communion with the wider world had not lost anything by staying there, "
        "and those who had cut themselves off from that communion -- Tyconius's own party among "
        "them -- were the ones who had actually separated themselves from something real.\n\n"
        "Parmenian, the movement's own bishop at Carthage, and the other leaders around him saw "
        "exactly where this argument pointed, and they did not follow it. Parmenian wrote to "
        "Tyconius directly, rebuking him for preaching that the church extended across the whole "
        "world, and warning him not to dare do it again. Tyconius did not recant, and did not "
        "leave. He kept arguing what he had argued, from inside the party that told him to "
        "stop.\n\n"
        "What came after the letter is less certain, and the tradition itself marks it as less "
        "certain: it is reported -- not witnessed outright, but reported -- that Tyconius was "
        "afterward condemned by a council of his own communion. He was never received back. He "
        "did not go over to the other side either. He simply remained, for whatever years he had "
        "left, the head of a schismatic church so small that he may have been the only one left "
        "in it.",
        "The specific mechanism of Tyconius's condemnation (a conciliar sentence rather than some "
        "other form of exclusion) carries Augustine's own explicit reporting hedge and is not "
        "claimed as directly witnessed fact; how his condemned work nonetheless survived and "
        "influenced Augustine's own later hermeneutics is not explained by any source this record "
        "draws on.",
        "A modern reader might assume that a losing argument, once condemned, simply disappears. "
        "Tyconius's argument was condemned by his own party and yet outlived that condemnation, "
        "shaping how a Catholic bishop a generation later would read Scripture -- a case where "
        "being formally cut off did not mean being forgotten.",
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Documented for Parmenian's letter of rebuke and the fact of a subsequent "
             "condemnation; the specific mechanism carries Augustine's own explicit reporting "
             "hedge ('perhibent') and is presented with that hedge intact (Story-Chunks/"
             "donstory009, Tier Justification)."),
        [{"source_id": "don.source.petschenig-scripta-contra-donatistas",
          "locus": "Contra Epistulam Parmeniani I.1; cic/texts/"
                   "augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt, "
                   "lines 2145-2200",
          "license": "public-domain"},
         {"source_id": "don.source.monceaux-histoire-litteraire-tome5",
          "locus": "aftermath narration, corroborating context, not primary basis; lines 8520-8570",
          "license": "public-domain"}],
        2,
        ["participant asks what happened to Tyconius after he wrote the Liber Regularum",
         "participant asks whether this movement tolerated internal theological dissent",
         "participant asks why Tyconius's own writing survived and influenced later Christian "
         "thought despite his own party rejecting him"],
        ["participant wants an account of Tyconius's own positive theological content rather than "
         "the institutional consequence of asserting it",
         "participant is asking about a story where this movement's own leadership reconciles "
         "with an internal dissenter (don.story.bagai-reconciliation is the story where that "
         "happens, and this story is its structural opposite: here, reconciliation is never "
         "offered)"],
        "Mapped directly from Story-Chunks/donstory009_tyconius-condemnation.md, including Doc_09 "
        "Section 7's own disclosed self-correction of an earlier wrong judgment (this record does "
        "not repeat the earlier error).",
    )


# ===========================================================================
# FIGURES (16)
# ===========================================================================

def build_figures() -> None:
    emit_figure(
        "donatus",
        [{"name": "Donatus", "tag": "in-world"},
         {"name": "Donatus the Great / Donatus of Carthage (primate c. 313-347)", "tag": "scholarly"}],
        {"floruit": "succeeded Majorinus as primate of Carthage from c. 313 (Doc_01 SS2); primate "
                    "of the party from 313-347 per Monceaux's own dating discussion (Doc_02 SS4); "
                    "the movement's own name derives from him (world_core, Doc_01 SS2)",
         "died": "not established in this world's own vendored corpus beyond the 313-347 primacy "
                 "window"},
        True,
        "the second primate of Carthage, from whom this movement's own name comes, remembered "
        "for one line to the emperor's own ministers: what has the emperor to do with the Church?",
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Widely Accepted for the primacy and the retort (attested via Optatus, a hostile "
             "source, independently re-verified this session for the quote itself -- see "
             "don.quote.donatus-quid-est-imperatori); the possibility that he personally preached "
             "the donstory001 sermon is Monceaux's own proposal, explicitly not adopted as "
             "settled by Doc_09 or this record."),
        [{"source_id": "don.source.optatus-against-donatists",
          "locus": "Book III, line 1904 (the retort); world_core (the movement's own name)",
          "license": "public-domain"}],
        "Author-Gravity note: everything this record states about Donatus beyond the name he gave "
        "the movement reaches this world through Optatus, its own later opponent, writing decades "
        "after Donatus's own primacy (Doc_02 SS1). The retort itself (don.quote.donatus-"
        "quid-est-imperatori) was independently re-located and re-read this session directly "
        "against the vendored file, addressed by Optatus to Parmenian ('your father') rather than "
        "reported in Donatus's own surviving hand. Monceaux's proposal that Donatus himself "
        "preached the donstory001 commemorative sermon is carried in relations[] as an "
        "association with don.story.passio-donati-sermon, not as an attribution -- that story's "
        "own Usage Guidance is explicit that the Representative should not treat the proposal as "
        "settled fact.",
    )

    emit_figure(
        "majorinus",
        [{"name": "Majorinus", "tag": "in-world"},
         {"name": "Majorinus (rival bishop of Carthage, consecrated 311/312, d. c. 313)",
          "tag": "scholarly"}],
        {"floruit": "consecrated as the first rival bishop of Carthage, 311/312, succeeding "
                    "Caecilian's contested election; succeeded himself, from c. 313, by Donatus "
                    "(Doc_01 SS2, don.story.lucilla-consecration-dispute)"},
        True,
        "the first rival bishop set up against Caecilian - a member of Lucilla's own household, "
        "the record's hostile telling says, raised by her bribes",
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Optatus's own characterization of the consecration as bribery-driven is his hostile "
             "framing, not adopted as fact here, matching don.story.lucilla-consecration-"
             "dispute's own Tier Justification."),
        [{"source_id": "don.source.optatus-against-donatists",
          "locus": "Book I, chapters 16-20",
          "license": "public-domain"}],
        "The founding act of the parallel episcopal line this world's own institutional history "
        "traces forward from (don_World_Profile.md line 219 names the Carthage primate "
        "succession as Donatus, then Parmenian, then Primian -- this record supplies the "
        "immediate predecessor that succession itself presupposes). Reconstructed only to the "
        "bound Optatus's own hostile text supports, per Doc_02 SS6's own Article 20 "
        "bounded-reconstruction finding for Lucilla's own household connection: nothing beyond "
        "the bare consecration and its funding is asserted of his own character or motives.",
    )

    emit_figure(
        "parmenian",
        [{"name": "Parmenian", "tag": "in-world"},
         {"name": "Parmenian (primate of Carthage after Donatus, d. by 393)", "tag": "scholarly"}],
        {"floruit": "succeeded Donatus as primate of Carthage (don_World_Profile.md line 219); "
                    "wrote to rebuke Tyconius directly, warning him not to preach a "
                    "worldwide-church argument again, c. 380 (Doc_02 SS4, Doc_04 SS2); no longer "
                    "primate by 393, when Primian held the see"},
        True,
        "the primate who wrote to Tyconius directly, warning him not to preach it again",
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "The rebuke itself is Documented via Augustine's direct report; Parmenian's own "
             "further career beyond this episode and his own succession by Primian rests on "
             "don_World_Profile.md's own primate-succession statement, not independently "
             "re-verified against a primary text this session."),
        [{"source_id": "don.source.petschenig-scripta-contra-donatistas",
          "locus": "Contra Epistulam Parmeniani I.1, Augustine's report of the rebuke",
          "license": "public-domain"}],
        "The middle figure in the G4 primate-succession backbone don_World_Profile.md line 219 "
        "names (Donatus, then Parmenian, then Primian) -- load-bearing for that institutional "
        "spine even though, unlike Majorinus and Primian, he has his own dedicated story "
        "(don.story.tyconius-condemnation), which is why this record is built per the launch "
        "brief's own instruction to name gravity-central figures whether or not they already have "
        "one.",
    )

    emit_figure(
        "primian",
        [{"name": "Primian", "tag": "in-world"},
         {"name": "Primian (primate of Carthage, fl. 393-394)", "tag": "scholarly"}],
        {"floruit": "sitting Donatist primate of Carthage in 393, when the deacon Maximian was "
                    "elected a rival primate at Cebarsussi in defiance of his own office; "
                    "presided over the mainstream response, the 394 Council of Bagai's own "
                    "condemnation and subsequent reception of the Maximianist bishops "
                    "(don.story.bagai-reconciliation)"},
        True,
        "the sitting primate at Carthage when a deacon named Maximian set himself up as a rival "
        "bishop",
        conf("B", "verified-via-authority", "load-bearing", "Documented",
             "The 393/394 sequence (the Cebarsussi rival consecration, the Bagai condemnation, "
             "the reception without rebaptism) is Documented via Augustine's own directly-quoted "
             "decree (don.story.bagai-reconciliation); this record relies on that already-"
             "established reading rather than an independent re-check of the primary text this "
             "session."),
        [{"source_id": "don.source.augustine-on-baptism-against-donatists",
          "locus": "I.1.2, I.5.7, narrating the Maximianist schism and its reconciliation",
          "license": "public-domain"}],
        "The third named primate in don_World_Profile.md line 219's own Carthage succession "
        "(Donatus, then Parmenian, then Primian), and the figure whose own institutional choice -- "
        "reconciliation without rebaptism or reordination -- is this world's own documented "
        "Purity-Rigor-vs-Institutional-Reception tension in practice (don.story.bagai-"
        "reconciliation).",
    )

    emit_figure(
        "petilian",
        [{"name": "Petilian", "tag": "in-world"},
         {"name": "Petilian of Constantina (Donatist bishop of Cirta)", "tag": "scholarly"}],
        {"floruit": "bishop of Constantina/Cirta; his own letters answered by Augustine in three "
                    "books, c. 400-403; named by Monceaux, alongside Emeritus, as one of the two "
                    "principal Donatist champions at the 411 Conference of Carthage (Doc_02 SS3)"},
        True,
        "this world's own fullest surviving voice, known to us only through the words our own "
        "opponent chose to answer",
        conf("C", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Recoverable only through Augustine's own selection and refutation -- no independent "
             "text of Petilian's letters survives outside this quotation (don.source.petilian-of-"
             "constantina-letters-quoted, Registry row 12, Confidence C). The specific proposition "
             "quoted at don.quote.petilian-conscience-of-the-giver was independently re-located "
             "and directly re-read this session at its own point of direct attribution within "
             "Augustine's translated text (not only the Prolegomena's summary of it)."),
        [{"source_id": "don.source.petilian-of-constantina-letters-quoted",
          "locus": "Petilian's own letters, quoted throughout Augustine's Answer",
          "license": "public-domain"},
         {"source_id": "don.source.augustine-answer-to-letters-of-petilian",
          "locus": "Book II, Chapter 3 ('Petilianus said: ...'); cic/texts/"
                   "npnf104_augustine-anti-manichaean-anti-donatist.xml, line 15788",
          "license": "public-domain"}],
        "Doc_02 SS3 names Petilian and Emeritus together as 'the two principal Donatist champions' "
        "at the 411 Conference, each carrying a distinctly-mediated evidentiary channel -- "
        "Petilian only through hostile quotation, Emeritus through the Conference's own court "
        "transcript. This is the reasoning behind building both as figures even though only "
        "Petilian's letters carry a dedicated source record of their own.",
    )

    emit_figure(
        "emeritus",
        [{"name": "Emeritus", "tag": "in-world"},
         {"name": "Emeritus of Caesarea (Donatist bishop, fl. 394-418)", "tag": "scholarly"}],
        {"floruit": "drafted the sentence of the Council of Bagai, 394 (Monceaux, Doc_02 SS3, "
                    "implying established authority within the party by that date); at the height "
                    "of his reputation at the 411 Conference of Carthage, where he is independently "
                    "confirmed speaking in at least ten separate numbered acts; older and "
                    "embittered by 418, at a further, separate dialogue with Augustine, Gesta cum "
                    "Emerito (not itself vendored or checked this session)"},
        True,
        "the bishop of Caesarea who stood, with Petilian, as this movement's own two champions "
        "before the tribunal at Carthage in 411",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The Conference transcript (cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_"
             "migne.txt) carries this world's own worst-on-record OCR quality for a text of this "
             "significance (Doc_02 SS1); the act 50 plea (don.quote.emeritus-magno-argumento) was "
             "independently re-located and re-read this session directly against the raw file "
             "(line 126834), matching Doc_02's own prior finding, but the surrounding scan should "
             "still be treated as a careful reading of a difficult scan, not a settled "
             "critical-edition text, until visually cross-checked (Doc_02 SS1)."),
        [{"source_id": "don.source.migne-pl11-collatio-carthaginiensis",
          "locus": "act 50 ('Emeritus episcopus dixit. Magno argumento veritas occultatur...'), "
                   "and at least nine further numbered interventions (acts 20, 24, 26, 99, 108, "
                   "121, 253, 266, 268); line 126834",
          "license": "public-domain"},
         {"source_id": "don.source.gesta-collationis-carthaginiensis",
          "locus": "the Conference as an event",
          "license": "public-domain"}],
        "This is a genuinely different category of Donatist voice than Petilian's own quoted "
        "letters: not preserved inside a hostile polemicist's own selective refutation, but "
        "recorded contemporaneously by an imperial notary whose institutional loyalty ran to "
        "neither party (Doc_02 SS1). Every one of Emeritus's own recognitions at the acts this "
        "world's build has checked closes with an explicit procedural reservation ('salva "
        "appellatione recognovi' at acts 50, 253, 266) -- signing under protest, not unconditional "
        "acceptance, a real recurring detail this record does not flatten.",
    )

    emit_figure(
        "tyconius",
        [{"name": "Tyconius", "tag": "in-world"},
         {"name": "Tyconius (Donatist exegete, condemned c. 380)", "tag": "scholarly"}],
        {"floruit": "wrote the Liber Regularum, this movement's own strongest surviving "
                    "theological writing (don.source.tyconius-liber-regularum); rebuked by "
                    "Parmenian for arguing the church extended across the whole world; condemned "
                    "by a council of his own communion, c. 380, per Augustine's own report "
                    "(don.story.tyconius-condemnation)"},
        True,
        "the one among us whose argument from Scripture was too well-supported to simply dismiss "
        "- and who was cut off for making it anyway",
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "The Liber Regularum's own existence and identity (Burkitt's 1894 edition) is "
             "independently confirmed; the condemnation's own specific mechanism carries "
             "Augustine's own explicit reporting hedge, per don.story.tyconius-condemnation's own "
             "Tier Justification, and is not claimed here as more settled than that story states."),
        [{"source_id": "don.source.tyconius-liber-regularum",
          "locus": "the whole work",
          "license": "public-domain"}],
        "Doc_04's own D-B gravity candidate ('Tyconius's universalist hermeneutics/ecclesiology') "
        "is tested and not advanced specifically because his own party's council condemned him "
        "and no following continued his approach -- this record and don.story.tyconius-"
        "condemnation together supply the concrete narrative that finding rests on. His own "
        "formal standing within the Donatist communion after the condemnation is deliberately "
        "left open by Doc_01 SS4, not resolved here.",
    )

    emit_figure(
        "caecilian",
        [{"name": "Caecilian", "tag": "in-world"},
         {"name": "Caecilian of Carthage (bishop from 311/312)", "tag": "scholarly"}],
        {"floruit": "archdeacon of Carthage, rebuked Lucilla for kissing an unrecognized martyr's "
                    "bone; elected bishop of Carthage 311/312 in a contested process, consecrated "
                    "by Felix of Aptungi -- the election this whole world's founding dispute turns "
                    "on"},
        True,
        "the archdeacon whose own contested election as bishop of Carthage this movement's whole "
        "history turns on",
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted", None),
        [{"source_id": "don.source.optatus-against-donatists",
          "locus": "Book I, chapters 16-20",
          "license": "public-domain"},
         {"source_id": "don.source.optatus-appendix-of-documents",
          "locus": "the Acta Purgationis Felicis, investigating his own consecrator's standing",
          "license": "public-domain"}],
        "Recurs across four of the nine built stories (don.story.passio-donati-sermon, "
        "don.story.lucilla-consecration-dispute, don.story.gesta-apud-zenophilum, don.story."
        "acta-purgationis-felicis) without ever being the dedicated subject of one of his own -- "
        "exactly the load-bearing-without-a-dedicated-story case the launch brief names. Every "
        "fact recorded here reaches this world through Optatus, this movement's own later "
        "opponent (Doc_01 SS7 item 1).",
    )

    emit_figure(
        "felix-of-aptungi",
        [{"name": "Felix", "tag": "in-world"},
         {"name": "Felix of Aptungi (Catholic bishop, consecrator of Caecilian)", "tag": "scholarly"}],
        {"floruit": "bishop of Aptungi; consecrated Caecilian as bishop of Carthage, 311/312; "
                    "accused of traditio, the accusation this world's whole founding dispute rests "
                    "on; investigated and vindicated by Constantine's own ordered inquiry, "
                    "314/315 (don.story.acta-purgationis-felicis)"},
        True,
        "the bishop whose own hand consecrated Caecilian - and whose standing to do that is the "
        "accusation this movement's whole founding dispute turns on",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "don.source.optatus-appendix-of-documents",
          "locus": "Acta Purgationis Felicis, Appendix I; cic/texts/"
                   "optatus_against-the-donatists.txt, lines 5467-5585",
          "license": "public-domain"}],
        "The single most direct piece of judicial evidence this world's corpus holds on the "
        "founding traditor question: every subsequent institutional development this world's "
        "history contains depends on whether the accusation against Felix could actually be "
        "sustained, and the imperially-ordered answer, on this record, is that it could not "
        "(don.story.acta-purgationis-felicis's own Formation Ecology Connection).",
    )

    emit_figure(
        "lucilla",
        [{"name": "Lucilla", "tag": "in-world"},
         {"name": "Lucilla of Carthage (wealthy laywoman, fl. c. 305-320)", "tag": "scholarly"}],
        {"floruit": "rebuked by Caecilian, before he became bishop, for kissing a not-yet-"
                    "recognized martyr's bone; her own money (four hundred pieces of silver) "
                    "funded Majorinus's rival consecration, 311/312 (don.story.lucilla-"
                    "consecration-dispute); the same money was the subject of a formal judicial "
                    "inquiry in 320 (don.story.gesta-apud-zenophilum)"},
        True,
        "the wealthy laywoman rebuked in public for kissing a martyr's bone before this movement "
        "had a name",
        conf("B", "verified-via-authority", "load-bearing", "Documented",
             "Reconstructed only to the bound Optatus's own hostile text supports, per Doc_02 "
             "SS6's own Article 20 bounded-reconstruction finding: a named woman of means with the "
             "standing to make a rival consecration happen, nothing beyond that bound asserted of "
             "her own motivations or character."),
        [{"source_id": "don.source.lucilla-and-second-woman-maximianist",
          "locus": "Optatus I.16; Augustine, Letter XLIII SS26",
          "license": "public-domain"},
         {"source_id": "don.source.optatus-against-donatists",
          "locus": "Book I, chapters 16-20",
          "license": "public-domain"}],
        "One of only two named women anywhere in this world's own vendored corpus (Doc_01 SS7 "
        "item 1), and one of the very few figures with a named-and-corroborated presence across "
        "two separate stories, seven years apart (the 311/312 consecration; the 320 inquiry). "
        "Optatus's own hostile characterization of her motive as personal spite is carried in "
        "don.story.lucilla-consecration-dispute's own text as his framing, not adopted as fact "
        "here.",
    )

    emit_figure(
        "marculus",
        [{"name": "Marculus", "tag": "in-world"},
         {"name": "Marculus (Benedictus Martyr Marculus, d. 347/348)", "tag": "scholarly"}],
        {"floruit": "seized at Vegesela during the Macarian persecution; flogged and paraded "
                    "through Numidian towns; held four days at the cliff of Novapetra; thrown "
                    "from the cliff before dawn, 347/348 (don.story.passio-marculi)"},
        True,
        "the bishop thrown from a cliff at Novapetra, remembered as shown, in advance, exactly "
        "what his own death would look like",
        conf("A", "verified-via-authority", "load-bearing", "Contested",
             "General portrait Contested (corroborated even by the hostile Optatus/Augustine "
             "material that the death occurred); the visionary and miraculous detail -- the "
             "cup/crown/palm vision, the unbroken fall -- Inferential-Thin, matching don.story."
             "passio-marculi's own Tier Justification exactly."),
        [{"source_id": "don.source.passio-marculi",
          "locus": "the whole Passio",
          "license": "public-domain"}],
        "This world's own clearest single example of the hagiographic register Tier 3's own "
        "definition anticipates -- the idealized portrait, the miracle sequence, the death as "
        "completion of a formed life -- and a figure the hostile Catholic tradition explicitly "
        "does not accept as a genuine martyr, on two separate grounds this record does not "
        "resolve (don.story.passio-marculi's own Formation Ecology Connection).",
    )

    emit_figure(
        "macrobius",
        [{"name": "Macrobius", "tag": "in-world"},
         {"name": "Macrobius, Donatist bishop (fl. 347-348)", "tag": "scholarly"}],
        {"floruit": "bishop, wrote to his own Carthage congregation in the aftermath of the "
                    "347-348 Macarian persecution, naming himself and his own office directly "
                    "(don.story.macrobius-letter-isaac-maximianus); named elsewhere in this "
                    "world's own vendored corpus as 'the Donatists' own hidden bishop in the city "
                    "of Rome' (Source_Registry.md row 20)"},
        True,
        "the bishop who wrote to his own Carthage congregation with the news of two more of our "
        "own dead",
        conf("A", "verified-via-authority", "load-bearing", "Widely Accepted", None),
        [{"source_id": "don.source.passio-isaac-et-maximiani",
          "locus": "the whole letter; cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt, "
                   "lines 1367-2609",
          "license": "public-domain"}],
        "The one named author, among the three Macarian-persecution martyr texts, who identifies "
        "himself and his own office and writes close in time to a real, named audience -- exactly "
        "the distinguishing feature that earns don.story.macrobius-letter-isaac-maximianus its "
        "Tier 1 classification against donstory001/002's own Tier 3.",
    )

    emit_figure(
        "isaac-and-maximianus",
        [{"name": "Isaac and Maximianus", "tag": "in-world"},
         {"name": "Isaac and Maximianus, martyrs of the Macarian persecution (d. 347/348)",
          "tag": "scholarly"}],
        {"floruit": "347/348, tortured and killed under the Macarian persecution, their bodies "
                    "thrown into the sea and recovered after six days (don.story.macrobius-"
                    "letter-isaac-maximianus)"},
        True,
        "two of our own dead, remembered together the way Macrobius's own letter names them "
        "together - a name given like a sign, and a soldier who saw the fight before he fought it",
        conf("A", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Widely Accepted for the bare narrative (torture, death, the sea, recovery); Isaac's "
             "own cry to his tormentors is preserved in don.story.macrobius-letter-isaac-"
             "maximianus as reported speech rather than verbatim quotation, since no established "
             "published English translation of the letter exists."),
        [{"source_id": "don.source.passio-isaac-et-maximiani",
          "locus": "the whole letter",
          "license": "public-domain"}],
        "Paired figure, following this project's own precedent for two people the vendored source "
        "itself always names and treats together (compare cappadocian.figure.forty-of-sebaste): "
        "Macrobius's letter narrates Isaac and Maximianus as one martyrdom account, not two "
        "independently developed lives, and this record follows that attested shape rather than "
        "inventing two separate figure records the evidence does not differentiate beyond their "
        "two distinct deaths (Isaac killed by the flogging itself; Maximianus surviving to be "
        "thrown into the sea).",
    )

    emit_figure(
        "optatus",
        [{"name": "Optatus", "tag": "in-world"},
         {"name": "Optatus of Milevis (Catholic bishop, fl. c. 366-393)", "tag": "scholarly"}],
        {"floruit": "wrote Against the Donatists in a first edition c. 366-367, revised c. 385 "
                    "(don.source.optatus-against-donatists); this movement's own earliest "
                    "substantial narrative source, hostile and external but contemporary"},
        True,
        "our own later opponent, whose account is where most of what survives of our own early "
        "history actually comes from",
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted", None),
        [{"source_id": "don.source.optatus-against-donatists",
          "locus": "the whole work",
          "license": "public-domain"},
         {"source_id": "don.source.optatus-appendix-of-documents",
          "locus": "the Appendix of Documents",
          "license": "public-domain"}],
        "Named, by name, as the source through which four of the nine built stories survive "
        "(don.story.lucilla-consecration-dispute, don.story.gesta-apud-zenophilum, don.story."
        "acta-purgationis-felicis, don.story.council-of-cirta) -- this world's own Author Gravity "
        "problem (Doc_01 SS7 item 1; Doc_02 SS1) is, concretely, the fact that Optatus's own "
        "selecting hand stands between this world and nearly all of its own founding-era history. "
        "Naming him as a figure, the same way this project's own precedent names a hostile or "
        "opposing voice a Representative must still introduce (cappadocian.figure.julian), keeps "
        "that mediation visible rather than letting his own framing pass as neutral narration.",
    )

    emit_figure(
        "augustine",
        [{"name": "Augustine", "tag": "in-world"},
         {"name": "Augustine of Hippo (Catholic bishop, 354-430)", "tag": "scholarly"}],
        {"born": "354, Thagaste",
         "floruit": "bishop of Hippo from 395/396; wrote the bulk of his anti-Donatist corpus "
                    "c. 400-420, from On Baptism and Answer to the Letters of Petilian (c. 400-403) "
                    "through Contra Gaudentium (c. 420), his own last anti-Donatist work "
                    "(don.source.augustine-contra-gaudentium)"},
        True,
        "the bishop of Hippo who answered us longer and more relentlessly than anyone else, and "
        "through whose own hostile quotation most of what survives of our own arguments comes "
        "down to us",
        conf("A", "verified-via-authority", "load-bearing", "Documented",
             "Augustine's own dates and bibliography (354-430; bishop from 395/396; the c. "
             "400-420 anti-Donatist corpus) are Documented via this world's own already-"
             "established source records (don.source.augustine-answer-to-letters-of-petilian and "
             "siblings); this record relies on those already-verified findings rather than an "
             "independent re-check of his biography this session."),
        [{"source_id": "don.source.augustine-answer-to-letters-of-petilian",
          "locus": "the whole three-book work",
          "license": "public-domain"},
         {"source_id": "don.source.augustine-on-baptism-against-donatists",
          "locus": "the whole seven-book work",
          "license": "public-domain"}],
        "Named, by name, as the source through which don.story.bagai-reconciliation and don."
        "story.tyconius-condemnation both survive, and the transmitting author of don.quote."
        "petilian-conscience-of-the-giver -- the same Author Gravity concentration named on don."
        "figure.optatus's own record, at even greater scale (Doc_02 SS1's own extensive Author "
        "Gravity concentration finding names Augustine as the single largest concentration in "
        "this world's entire vendored corpus).",
    )

    emit_figure(
        "purpurius",
        [{"name": "Purpurius", "tag": "in-world"},
         {"name": "Purpurius (Donatist bishop, fl. 305-312)", "tag": "scholarly"}],
        {"floruit": "present at the Council of Cirta, c. 305, where he turned the traditor "
                    "question back on the presiding bishop Secundus of Tigisis (don.story.council-"
                    "of-cirta); present at Caecilian's own contested election assembly, 311/312, "
                    "where he mocked Caecilian openly rather than answer his demand for a plain "
                    "accusation (don.story.lucilla-consecration-dispute)"},
        True,
        "the bishop who mocked Caecilian to his face at the assembly - and who had himself, years "
        "earlier, deflected the very traditor question back onto the man who first raised it",
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted", None),
        [{"source_id": "don.source.optatus-against-donatists",
          "locus": "Book I, chapters 14 (Cirta) and 16-20 (the Carthage assembly)",
          "license": "public-domain"}],
        "The same named figure across two stories seven years apart, a continuity don.story."
        "council-of-cirta's own text states explicitly ('the same figure who would later mock "
        "Caecilian in the Carthage basilica') rather than one this record infers on its own -- "
        "this recurrence, across founding-era stories with no dedicated story of his own, is why "
        "this record exists per the launch brief's own criterion (b).",
    )


# ===========================================================================
# QUOTES (4)
# ===========================================================================

def build_quotes() -> None:
    emit_quote(
        "petilian-conscience-of-the-giver",
        "\"Conscientia namque (sancte) dantis attenditur, quae (qui) abluat accipientis.\" "
        "\"Nam qui fidem (sciens) a perfido sumpserit, non fidem percipit, sed reatum.\" "
        "\"What we look for is the conscience of the giver (him who gives in holiness), to "
        "cleanse that of the recipient.\" \"For he who (wittingly) receives faith from the "
        "faithless receives not faith, but guilt.\"",
        "don.figure.petilian",
        "verbatim",
        "A modern reader may hear \"the conscience of the giver\" as a claim about the "
        "minister's own private, subjective sincerity -- whether he personally feels holy. "
        "Petilian's own argument is narrower and more structural than that: it is about whether "
        "the minister's own hand was tainted by a specific, checkable act (surrendering "
        "scripture under persecution), not about an unknowable inner feeling.",
        "What matters is the giver's own character - that's what makes the one receiving it "
        "clean. Someone who knowingly takes their faith from a faithless hand doesn't receive "
        "faith at all - only guilt.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             None),
        [{"source_id": "don.source.augustine-answer-to-letters-of-petilian",
          "locus": "Book II, Chapter 3, SS6 ('Petilianus said: ...'); independently re-located "
                   "and re-read this session against cic/texts/npnf104_augustine-anti-manichaean-"
                   "anti-donatist.xml, line 15788 -- distinct from the Prolegomena's own earlier "
                   "summary of the same proposition at line 10280",
          "license": "public-domain"}],
        1,
        ["participant asks what this movement actually believed made a sacrament valid or "
         "invalid",
         "participant asks for this movement's own core doctrine in its own words, not a "
         "paraphrase",
         "conversation reaches the traditor-purity doctrine and needs its own founding "
         "statement"],
        ["participant wants Augustine's own counter-argument rather than Petilian's own "
         "proposition (this record quotes only Petilian's own words, not Augustine's reply, "
         "though don.figure.augustine is linked as the transmitting author)"],
        "This proposition is named directly in the Permanent Prompt's own Approved Source "
        "paragraph ('What Petilian argued: that what is sought is the conscience of the giver, "
        "to cleanse that of the recipient'). Independently re-checked this session at its point "
        "of direct textual attribution within Augustine's own translated Answer (Book II, "
        "Chapter 3), not only at the Prolegomena's earlier summary of the same words (line "
        "10280) -- the same proposition recurs at least a dozen further times across Books II-III "
        "as Augustine returns to it, confirming this is the argument's own settled, repeated "
        "form, not a one-off paraphrase. The Latin's own parenthetical variants ('sancte', "
        "'sciens') are the NPNF edition's own bracketed textual-variant markers, reproduced here "
        "as found rather than silently resolved. modern_rendering is a light modernization of the "
        "NPNF's own published translation, not a fresh rendering from this session's own reading "
        "of the Latin.",
    )

    emit_quote(
        "donatus-quid-est-imperatori",
        "\"Quid est imperatori cum ecclesia?\" (\"What has the Emperor to do with the "
        "Church?\")",
        "don.figure.donatus",
        "verbatim",
        "A modern reader may hear this as a general church-state-separation principle, the kind "
        "any modern secular democracy might affirm. Donatus's own context is narrower and more "
        "pointed: he said it specifically to reject the emperor's own claim to arbitrate which "
        "church was the true one, in the moment an imperial almoner arrived offering material aid "
        "-- and this same movement petitioned that identical emperor's machinery for its own "
        "advantage at three other named points across its own history, a qualification this "
        "record does not smooth away.",
        "What business does the emperor have with the church?",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "don.source.optatus-against-donatists",
          "locus": "Book III; cic/texts/optatus_against-the-donatists.txt, line 1904",
          "license": "public-domain"}],
        1,
        ["participant asks whether this movement believed the state had any standing to decide "
         "who the true church was",
         "conversation reaches the Principled-Refusal-vs-Pragmatic-Recourse tension and needs "
         "the founding quotation it is built on"],
        ["participant is asking about the Council of Cirta as an example of this movement's own "
         "rigor or resolve -- Cirta is a real complication in this movement's own early history, "
         "not a confirming example, and this quote should not be offered as if it resolved that "
         "different, harder question"],
        "Named directly in the Permanent Prompt's own Approved Source paragraph ('The retort "
        "Donatus himself is remembered to have given the emperor's own claim on the church'). "
        "Independently re-located this session at Optatus, Against the Donatists, Book III (line "
        "1904) -- Optatus addresses the passage to Parmenian directly ('when they came to "
        "Donatus, your father...'), so the retort survives inside Optatus's own polemic against "
        "Donatus's own successor, not in Donatus's own hand. modern_rendering lightly modernizes "
        "Vassall-Phillips's own 1917 published translation, already close to plain modern English.",
    )

    emit_quote(
        "emeritus-magno-argumento",
        "\"Magno argumento veritas occultatur; ut cum ad inquisitionem nostram modicum quid ex "
        "parte adversa prolatum sit, cetera sileantur.\"",
        "don.figure.emeritus",
        "verbatim",
        "A modern reader may hear a procedural objection like this as a stalling tactic, a lawyer "
        "avoiding the real question. Emeritus's own point is closer to the opposite: he is "
        "refusing to let the case proceed to its substance at all until the opposing advocates "
        "disclose their own names, rank, and mandate to the court -- treating procedural standing "
        "itself as the truth the other side is trying to keep hidden, not a distraction from it.",
        "A clever trick can hide the truth. We answer in full. They give us just a little bit, "
        "and call the rest closed.",
        conf("A", "verified-direct", "load-bearing", "Widely Accepted",
             "Widely Accepted rather than Documented: this world's own build already names the "
             "vendored Migne PL11 scan's OCR quality as \"notably poor even by this corpus's own "
             "standards\" (Doc_02 SS1). This record's own Latin and English match Doc_02's own "
             "already-published rendering exactly, independently re-confirmed this session by "
             "reading the raw file directly at line 126834 ('Emeritus episcopus dtxii. Magno "
             "irgnmento vc-rilas occullaiur...'), but the underlying scan should still be treated "
             "as a careful reading of a difficult scan, not a settled critical-edition text, "
             "until visually cross-checked, per Doc_02's own standing caution."),
        [{"source_id": "don.source.migne-pl11-collatio-carthaginiensis",
          "locus": "act 50, 411 Conference of Carthage; independently re-read this session "
                   "against cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt, "
                   "line 126834",
          "license": "public-domain"}],
        2,
        ["participant asks how a Donatist bishop argued procedure before an imperially-convened "
         "tribunal",
         "conversation reaches the 411 Conference of Carthage and needs a specific, directly-"
         "quoted moment of a Donatist bishop's own voice, not only a description of the event"],
        ["participant wants the Conference's own outcome or scale (this quote is one procedural "
         "objection at one act, not a summary of the whole three-day proceeding, which this world's "
         "own build has not yet read in full -- Doc_09 SS8 item 2)"],
        "Named directly in the Permanent Prompt's own Approved Source paragraph ('Emeritus of "
        "Caesarea's own plea before the tribunal at Carthage, that the truth was hidden by a "
        "great device'). This is the one quote record this script independently re-locates in the "
        "raw vendored file rather than only citing Doc_02's own prior finding of it, per this "
        "step's own discipline of re-opening a primary text directly wherever this build's own "
        "confidence rating depends on it.",
    )

    emit_quote(
        "deo-laudes-acclamation",
        "DEO LAVDES",
        "the Donatist community at Bagai and Thamugadi (CIL VIII 17732, an anonymous epigraphic "
        "acclamation, not an individually attributed utterance)",
        "verbatim",
        "A modern reader may hear a two-word acclamation as a minor liturgical detail, "
        "interchangeable with any other phrase of praise. This world's own editors' note on the "
        "same stone says otherwise: \"Deo laudes\" functioned as this movement's own sign and "
        "token, set deliberately against the Catholic \"Deo gratias\" -- the two phrases marked "
        "which church a speaker belonged to, the way a password or a uniform would.",
        "Praise to God.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "Independently re-confirmed this session directly against the vendored CIL VIII "
             "Numidia supplement file: the file's own header names this scan's OCR quality as "
             "expecting \"substantial letter substitution and garbling throughout\" for this "
             "dense 19th-century epigraphic reference work generally, but inscription 17732's own "
             "specific reading and its editors' own identifying note were independently located "
             "and match Doc_02's own prior citation exactly, and the attestation is corroborated "
             "by three further catalogued inscriptions (nos. 17368, 18669, 20482) in the same "
             "volume."),
        [{"source_id": "don.source.deo-laudes-acclamation-cil8",
          "locus": "CIL VIII 17732, found on two pillars near Bagai (now preserved at Khenchela); "
                   "independently re-checked this session against cic/texts/"
                   "cil8-supplementum-numidiae_cagnat-schmidt1894.txt, line 4566",
          "license": "public-domain"},
         {"source_id": "don.source.cil8-numidia-supplement",
          "locus": "the corroborating inscriptions, nos. 17368, 18669, 20482",
          "license": "public-domain"}],
        2,
        ["participant asks whether this movement had its own distinct liturgical vocabulary, "
         "separate from the Catholic mainstream",
         "participant asks for evidence of this movement's own worship that does not pass through "
         "a hostile author's own pen"],
        ["participant wants a spoken doctrinal argument rather than a liturgical acclamation "
         "(don.quote.petilian-conscience-of-the-giver serves that different need)"],
        "Named directly in the Permanent Prompt's own Approved Source paragraph ('The acclamation "
        "Deo laudes, cut into stone at Bagai, where the rival says Deo gratias instead'). This "
        "world's own one clearly non-Augustine-mediated, non-Optatus-mediated anchor -- epigraphic, "
        "stone, no hostile literary framing at any point (Doc_04 SS3, the Cross-Voice Test). "
        "Linked in relations[] to don.story.bagai-reconciliation on the strength of their shared "
        "location (Bagai), not a claim that the acclamation itself dates to the 394 council.",
    )


def main() -> None:
    build_stories()
    build_figures()
    build_quotes()

    chunk_files = sorted(STORY_CHUNKS_DIR.glob("donstory*.md"))
    story_files = [w for w in WRITTEN if "/story/" in w]
    figure_files = [w for w in WRITTEN if "/figure/" in w]
    quote_files = [w for w in WRITTEN if "/quote/" in w]

    assert len(chunk_files) == 9, (
        f"expected 9 Story-Chunks files (Doc_09's own count), found {len(chunk_files)} -- "
        "re-check Build/worlds/don/Story-Chunks/ before trusting this script's own story "
        "count against it"
    )
    assert len(story_files) == len(chunk_files) == 9, (
        f"expected one story record per Story-Chunk (9), wrote {len(story_files)}"
    )
    assert len(figure_files) == 16, f"expected 16 figure records, wrote {len(figure_files)}"
    assert len(quote_files) == 4, f"expected 4 quote records (bounded set, see docstring), " \
        f"wrote {len(quote_files)}"

    # Reciprocity self-check: every RELATION_PAIRS id must be a record this
    # script actually emitted (story/figure/quote), so relations_for() never
    # silently produces a one-sided edge against an id that doesn't exist.
    all_ids = {Path(p).stem for p in WRITTEN}
    for a, b in RELATION_PAIRS:
        assert a in all_ids, f"RELATION_PAIRS references {a!r}, never emitted"
        assert b in all_ids, f"RELATION_PAIRS references {b!r}, never emitted"

    print(f"Wrote {len(WRITTEN)} records: {len(story_files)} story, {len(figure_files)} figure, "
          f"{len(quote_files)} quote.")
    for path in WRITTEN:
        print(f"  {path}")


if __name__ == "__main__":
    main()
