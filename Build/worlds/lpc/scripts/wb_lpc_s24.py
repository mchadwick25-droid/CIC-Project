"""B-4, lpc equivalent: Latin Pastoral-Congregational Christianity (`lpc`)
story + figure + quote records.

WHAT THIS SCRIPT DOES. Converts this world's already-built, already-reviewed
Story Inventory (Doc_09_Story_Inventory.md, eight independent adversarial
review rounds, Approved to proceed with one escalation carried open) and its
seven deployment-facing Story-Chunks (Story-Chunks/lpcstoryNNN_*.md) into
record-native `story` records under records/lpc/story/, per the live schema
(engine/m1/schemas.py) and gate battery (engine/m1/gates.py). It also authors
`figure` records for every named person this world's own build treats as
load-bearing enough to need a name-bridge (every central named subject of a
dedicated story, and the two mediating eyewitness-authors -- Pontius and
Possidius -- through whom six of the seven stories survive), and `quote`
records for a small, bounded, independently-verified set of lines this
world's own Representative Permanent Prompt (lpc_Representative_Permanent_
Prompt_Datus.txt) reaches for by name in its own "what our own life actually
gave us" paragraph (line 37). This is the direct methodological equivalent
of Build/worlds/don/scripts/wb_don_s24.py's own B-4 pass (read in full this
session, including its own later-migrated live form in records/don/story/,
records/don/figure/ and records/don/quote/, not only its original file) run
against `lpc`'s own inputs. B-1 (207 source records) and B-2/B-3 (19 term
records) are already done, committed and merged; this script does not touch
records/lpc/source/ or records/lpc/term/.

Read Build/worlds/lpc/scripts/wb_lpc_s21.py and wb_lpc_s22.py in full before this
script was written (not touched by it, not re-run by it) for the lpc-specific
docstring/code-pattern discipline they establish (HERE/REPO_ROOT/RECORDS_ROOT
layout, WORLD_ID as the long census slug, conf()/`_write()` shape) --
followed here exactly, alongside don's own s24 for the story/figure/quote-
specific conventions (RELATION_PAIRS as one master closed-graph list,
retrieval-tier-as-ranking-judgment, the AUTHORED/MECHANICAL field-by-field
discipline).

ONE LIVE-SCHEMA DIFFERENCE FROM DON'S OWN ORIGINAL s24, CONFIRMED BY DIRECT
READ OF THE CURRENT LIVE RECORDS, NOT ASSUMED FROM THE OLDER SCRIPT FILE.
don's own wb_don_s24.py (as a file) still writes `retrieval.do_not_retrieve_
when`; the live don records under records/don/story/ and records/don/quote/
have since been migrated to
`retrieval.prefer_instead` for the redirect half and envelope-level
`claim_guards` for the honesty-guard half, and `gate_retrieval_negatives_
structured` (engine/m1/gates.py) now hard-fails a populated `do_not_retrieve_
when`. This script writes the CURRENT live shape directly -- `prefer_instead`
for every Do-Not-Retrieve-When redirect, `claim_guards` where a chunk's own
Usage Guidance states a barred claim rather than a redirect -- rather than
reproducing don's own now-superseded original field name and then needing a
second pass to fix it. "No fix on a fix": this is that lesson applied at
authoring time, not a deviation from precedent.

INPUTS, mapped to OUTPUTS, precisely:
  - Doc_09_Story_Inventory.md Section 3 (Story Index) and Section 3.1 (By-
    Tier View) -> the authoritative tier assignment for every story record
    below. Tiers are NOT re-derived here; they are copied from Doc_09's own
    table (six Tier 1, zero Tier 2, one Tier 3, zero Tier 4 -- Doc_09's own
    closing line, and lpc_Story_Index.md's own independently-generated copy
    of the same count, read and cross-checked this session).
  - Story-Chunks/lpcstory001_election-of-cyprian.md through
    lpcstory007_the-psalms-on-the-wall.md (all seven files; the directory was
    listed directly this session, not assumed at seven) -> the seven `story`
    records' own narrative_tier_justification, tellable_as, text, absent_
    detail fields, mapped directly from each chunk's own "Story Text" (->
    text, recast into this world's own first-person "we" register -- see
    REGISTER below), "Tier Justification" (-> narrative_tier_justification,
    condensed), and "Usage Guidance"/"Absent Story Note" sections (->
    absent_detail). modern_contrast is NOT present in the Story-Chunk
    template (a later schema-only field, per schemas.py's own comment that
    it postdates the chunks) and is freshly authored here per story, grounded
    in that story's own already-established content, never in outside
    historical knowledge.
  - lpc_Representative_Permanent_Prompt_Datus.txt line 37 ("When a specific
    image, story, or teacher's word would make an answer vivid, we reach for
    what our own life actually gave us...") -> the bounded quote candidate
    set. Several images are named there; FOUR become `quote` records here --
    see "QUOTE SET, BOUNDED" below for the full accounting of what was named,
    what was built, and what was named but not built, and why.
  - Doc_01_World_Identification_Boundaries_Orientation.md SS2 (the two anchor
    figures' own conversion-to-office intervals, quoted directly: Cyprian's
    election "between roughly July 248 and April 249... by the acclamation
    of the Carthaginian people," Augustine "seized by the Hippo congregation
    and ordained presbyter, against his own wishes, in 391... under
    compulsion and constraint," Possidius Vita ch. IV/VIII) and SS7 (the
    conciliar-authority axis, quoting the 256 Council preface in full) ->
    lpc.figure.cyprian's, lpc.figure.augustine's and lpc.figure.possidius's
    own floruit/dates fields, and lpc.quote.bishop-of-bishops's and lpc.
    quote.clamour-and-tears's own grounding, independently re-confirmed this
    session against the vendored files rather than taken from Doc_01's own
    paraphrase alone (see QUOTE SET below).

REGISTER: story.text and story.tellable_as are written in this world's own
first-person "we"/"our" voice throughout (Cyprian and Augustine named as
"our bishop"/named individually, never as an outside third party), matching
the CURRENT live don story records' own register (confirmed by direct read
of records/don/story/don.story.passio-donati-sermon.md this session, whose
text opens "Every year... we gather to remember..."), not the third-person
"this community" register don's own original s24 file happened to use before
a later revision corrected it. Building first-person from the start is the
same "no fix on a fix" discipline named above, applied to voice rather than
to the retrieval-field migration. `gate_voice_perspective` (engine/m1/
gates.py) is checked directly against every story.text/tellable_as below:
neither "this world" nor "the world's own..." appears anywhere in either
field, in any of the seven stories.

FIGURE SET, AND WHY EACH ONE -- seven figures, each tied to one of the two
grounds don's own script names, not a blanket "every name in every chunk"
sweep (which would run past twenty names across the seven chunks: Numeria,
Candida, the eight Numidian bishops of lpcstory004, Numidicus's unnamed wife
and daughter, and others each appear in exactly one chunk and are not built):
  (a) the person is the central, named subject of at least one dedicated
      Doc_09 story: Cyprian (lpcstory001, 002, 006; also the author/subject
      of 003 and 004's own letters), Numidicus (lpcstory003), Celerinus and
      Lucian (lpcstory005, each a distinct named confessor writing in his own
      hand -- built as two figures, not one paired figure, because unlike
      this project's own paired-figure precedent for a single jointly-
      narrated martyrdom [cappadocian.figure.forty-of-sebaste; don.figure.
      isaac-and-maximianus], Celerinus and Lucian are two separately-attested
      authors, each with his own letter and his own named social location,
      not one account a third party narrates about both together), Augustine
      (lpcstory007, and the second of this world's own two anchor figures
      per Doc_09 SS1);
  (b) the person is the dominant mediating eyewitness-author through whom
      most of this world's own stories survive, per this step's own launch
      brief (matching don's own criterion (d) for Optatus/Augustine, though
      the shape here is friendly rather than hostile mediation): Pontius the
      Deacon, source for lpcstory001, 002 and 006 (three of the seven, all
      of Cyprian's own Phase One narrative material), and Possidius, bishop
      of Calama, the main source for lpcstory007 (the whole of Phase Two;
      Prosper's chronicle corroborates only the date of death and the
      siege) and, independently, the quote this script builds at lpc.quote.
      clamour-and-tears (see QUOTE SET below) -- this world's Author-Gravity
      problem for its two mediating witnesses is the mirror image of don's:
      Optatus and Augustine mediate hostilely; Pontius and Possidius mediate
      in praise, and Doc_09 SS2's own genre discipline (the Pontius/Delehaye
      tier-per-story rule) is built entirely around naming that mediation
      rather than letting it pass as neutral narration.
NOT built as figures, a disclosed bound rather than an oversight: Numeria and
Candida (lpcstory005 -- named, discussed, weighed and dispatched to peace by
two men writing to each other, but never narrating anything themselves;
Doc_09 SS7 items 3-4 make their own silence the sharpest documented absence
in this repository, and building a figure record around two people this
world's own build is explicit that nothing survives in their own words would
manufacture more presence for them than the record affords -- the opposite
of what Doc_09's own Absent Story discipline asks); Numidicus's wife and
daughter (lpcstory003 -- visible, and per Doc_09 SS7 item 4 explicitly never
audible; also unnamed, so no `names[]` entry could be built without inventing
one); the eight Numidian bishops Cyprian addresses by name in lpcstory004
(each named exactly once, with no further attested role); the schismatic
presbyters and named deponents inside the quote-set's own source material
(Felicissimus's faction, named only in the "ancient venom" passage's own
surrounding prose, not inside the quoted line itself, and appearing nowhere
in any of the seven Story-Chunks).

QUOTE SET, BOUNDED -- following don's own disclosed-narrowing discipline
exactly. The Permanent Prompt's own "what our own life actually gave us"
paragraph (line 37) names, in order: (1) the shepherd wounded in his own
flock's wound, wailing and weeping with it; (2) the crowd's own calling of a
man to office against a faction's ancient venom; (3) the crowd's own clamour
at a second bishop's own reluctant elevation; (4) a certificate written out
with a name on it, weighed against a wide door thrown open to unnamed people
at once; (5) "neither of us set himself up as a bishop of bishops," answered
at length a century and a third later; (6) what is given outside the church
at baptism, held two ways a century apart; (7) a preacher naming to his own
gathered people that their waiting is itself a prayer for him. This script
builds `quote` records for FIVE of these seven:
  1. BUILT (lpc.quote.shepherd-wounded-in-the-flock). Cyprian, *De Lapsis*
     SS4: "since it is the shepherd that is chiefly wounded in the wound of
     his flock... I wail with the wailing, I weep with the weeping."
     Located at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line
     43729 (the exact clause "wail with the wailing" -- not "wails," the
     Permanent Prompt's own light paraphrase) -- matching and grounding
     lpc.term.the-flock's own already-cited locus at De Lapsis 4.
  2. BUILT (lpc.quote.ancient-venom-against-my-episcopate). Cyprian, *Ep.*
     XXXIX SS1 (the ANF's own "Epistle XLI," section id iv.iv.xxxix):
     "retaining that ancient venom against my episcopate, that is, against
     your suffrage and God's judgment, they renew their old attack upon me."
     Located at line 32372 of the same vendored file -- the correct locus
     lpc.source.cyprian-epistles's own divergence_note names (as distinct
     from *Ep.* XL).
  3. BUILT (lpc.quote.bishop-of-bishops). Cyprian, opening the 256 Council of
     Carthage: "For neither does any of us set himself up as a bishop of
     bishops, nor by tyrannical terror does any compel his colleague to the
     necessity of obedience; since every bishop, according to the allowance
     of his liberty and power, has his own proper right of judgment, and can
     no more be judged by another than he himself can judge another."
     Located at line 56872 of the same vendored file, and corroborated at
     two further points in the same file where Augustine himself quotes the
     identical proposition back (lines 11292, 11626, 12207) while arguing
     against it at length -- the strongest-attested single line in this
     world's whole corpus, and already the sole cited locus of the existing
     lpc.term.bishop-of-bishops (records/lpc/term/, B-2/B-3, not touched by
     this script).
  4. BUILT (lpc.quote.clamour-and-tears). Possidius, *Vita Augustini* IV:
     "they demanded it with great zeal and clamor, while he wept freely."
     Located at line 1817 of cic/texts/possidius_vita-augustini_
     weiskotten1919.txt -- OUTSIDE lpcstory007's own declared XXVIII-XXXI
     span (the death and burial sequence), inside Chapter IV (Augustine's
     forced ordination as presbyter at Hippo, 391), the same file row 192
     already licenses and the same disclosed-reach-beyond-the-story's-own-
     span move don's own script names for its own Optatus Book III quote
     (that story draws from Book I). The translator's own endnote at this
     chapter (page 150) additionally quotes Augustine's own first-person
     Sermon CCCLV: "Apprehensus presbyter factus sum" ("I was seized and
     made a presbyter"), cited in this record's own body as corroboration,
     not substituted for Possidius's own third-person account as the
     record's `text`.
  5. NOT built (item 4 above, the certificate/wide-door image). This is a
     synthesized contrast between two attested practices (the confessors'
     own named libelli pacis, lpc.term.certificates-letters-of-peace, and a
     bishop's later general grant of peace to unnamed penitents at once),
     not a single locatable sentence any one source states -- there is no
     verbatim line to quote, only a pattern this world's own term records
     already carry in prose. Building a `quote` record here would require
     manufacturing a sentence no source says, which this step's own
     discipline forbids.
  6. NOT built (item 6 above, the two-answers-on-baptism contrast). Also
     synthesized, not a single quotable line -- it is the same shape of
     doctrinal contrast Doc_01 SS7 documents at length in prose (Cyprian's
     rebaptism position against Augustine's *validum sed infructuosum*
     ruling), and belongs, if built at all, to a future `contested_claim` or
     `doctrinal_witness` record, explicitly out of scope for this script.
  7. BUILT (lpc.quote.longing-expectation-is-a-prayer-for-me). Augustine,
     Sermon I [LI, Benedictine], on the agreement of Matthew and Luke's
     genealogies, delivered at the matins of the Nativity festival: "this
     your longing expectation is a prayer for me." Located at line 9398 of
     cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml
     by direct keyword search.
This is a disclosed narrowing to a five-item quote-record set out of seven
named images, not a silent one: two of the seven (items 5 and 6 above,
using this docstring's own numbering) are synthesized contrasts with no
single quotable sentence behind them and were not built; the remaining
five, each independently verified against its vendored source file, were.

RELATIONS -- CLOSED-GRAPH DISCIPLINE, following don's own script exactly.
records/lpc/gravity/, records/lpc/force/ and records/lpc/contested_claim/ do
not exist yet (later build steps); a `relations[]` entry pointing at an
lpc.term.* id would resolve under gate_referential (term records already
exist) but would then fail gate_reciprocity, because this script's own
constraints forbid touching records/lpc/term/ to add the required inverse
back. Every `relations[]` entry this script writes therefore points only at
another record this same script creates (story<->story, story<->figure,
story<->quote, figure<->figure, figure<->quote) -- a fully closed graph,
built and reciprocated by one master pair-list (RELATION_PAIRS below), so
every edge is declared on both ends by construction, not by hand-checking
each record afterward. Term connections (lpc.term.bishop-of-bishops, lpc.
term.the-flock, lpc.term.certificates-letters-of-peace, and others) are
named in each record's own prose body instead, matching don's own precedent
for term/gravity connections.

MECHANICAL vs AUTHORED, field by field:
  - id, world_id, record_type, schema_version, status, register, canon_cells:
    MECHANICAL. world_id="latin-pastoral-congressional-christianity" is a
    typo risk this script guards against directly (see WORLD_ID below --
    the actual value used is the correct
    "latin-pastoral-congregational-christianity", cross-checked byte-for-
    byte against an existing lpc/source record's own world_id field, not
    retyped from memory). status="draft" throughout (promotion to "ready" is
    a later stage, per don's own Stage 6a precedent -- not this script's).
    register="emic" throughout, matching every record type this pass builds
    (formation-facing story/figure/quote material) -- distinct from source
    records' own register="etic". canon_cells=[] throughout -- no canon-cell
    tagging work has happened for this world yet (unchanged from B-1/B-2's
    own note, and matching don's own wb_don_s2y being a distinct, later,
    unrun step for lpc).
  - narrative_tier: MECHANICAL -- copied directly from Doc_09 Section 3's own
    table. NOT re-derived by this script.
  - narrative_tier_justification, tellable_as, absent_detail: AUTHORED,
    condensed and adapted from each Story-Chunk's own already-reviewed prose
    (Tier Justification / Absent Story Note sections respectively).
  - text: AUTHORED, condensed from each Story-Chunk's own Story Text section
    and recast into this world's own first-person register (see REGISTER
    above), preserving every direct quotation from the vendored corpus
    exactly as the Story-Chunk already gives it -- no quotation is reworded,
    only the surrounding narration voice changes from third-person report to
    first-person memory.
  - modern_contrast: AUTHORED fresh per story (the field postdates the
    Story-Chunk template, per schemas.py's own comment), grounded in that
    story's own already-cited content, naming one specific modern assumption
    the story's own record complicates or reverses.
  - confidence.*: AUTHORED per record, translating each Story-Chunk's own
    free-text Tier Justification and Confidence line into the schema's
    enums. verification_state is held to verified-direct wherever this
    script independently re-located and re-read the story's own core quoted
    material against the raw vendored file THIS session (named per record in
    its own trailing body below, matching the specific line numbers found);
    verified-via-authority is used nowhere in this pass's stories, because
    every one of the seven core quotations was in fact independently
    re-checked this session (see the per-story body notes) -- a stronger
    position than don's own script reached for its nine stories, disclosed
    here rather than claimed by default.
  - sources[]: AUTHORED per record from each Story-Chunk's own Source field,
    resolved to the lpc.source.* ids B-1 already created (cross-checked
    against records/lpc/source/ directly by filename, not guessed).
  - names[], dates, narratable, bridge_line (figure only): AUTHORED per
    figure from the same Story-Chunk/Doc_01/Doc_09 material, never from this
    session's own outside knowledge of Cyprian or Augustine -- every date
    below traces to a passage read this build (cited inline in each figure's
    own body text).
  - text, speaker_or_author, license, modern_lens_note, modern_rendering
    (quote only): AUTHORED per quote. modern_rendering is a light
    modernization of the already-published ANF/Weiskotten translation this
    record's own `text` field quotes, never a fresh translation from this
    session's own reading of the Latin.
  - retrieval.tier (1-3, story/quote only): AUTHORED, a judgment call this
    script names rather than hides: tier 1 for the story/quote this script
    judges the more central, general-purpose retrieval candidate; tier 2 for
    a narrower or more specialized companion case (e.g. lpcstory006's Tier 3
    hagiographic register against lpcstory001/002/003/004/005/007's Tier 1
    documentary register).
  - retrieval.prefer_instead / claim_guards: AUTHORED per record, splitting
    each chunk's own Do-Not-Retrieve-When and Usage Guidance prose into its
    two live-schema homes -- an ordinary retrieval-scoping redirect goes to
    prefer_instead; a barred claim the Representative must never assert goes
    to claim_guards, phrased to include one of GUARD_MARKERS's own keywords
    (engine/prose.py) so gate_retrieval_negatives_structured's own mechanical
    check actually recognizes it as a guard rather than a stray redirect.

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells; touch records/lpc/term/,
records/lpc/source/, or records/lpc/world_core/ (existing records are read,
never edited); create lpc.gravity.*, lpc.force.*, lpc.contested_claim.*,
lpc.voice_craft.*, lpc.demonstration.*, lpc.doctrinal_witness.*, lpc.
honest_limit.*, or lpc.ambient.* records (later steps, explicitly out of
scope); build a story or figure record for the 133-year silence, the
Perpetua/Scillitan-martyr candidates, the healing miracles at Hippo, or the
411 Conference of Carthage (Doc_09 Section 6 names all four as considered
and not built, for reasons that remain unchanged by this script); promote
any record's status to "ready"; register `lpc` in records/worlds/ (a later
admission-track step); run the M2 compiler; touch any world other than lpc.
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[3]  # .../CIC-Project
RECORDS_ROOT = REPO_ROOT / "records" / "lpc"
STORY_CHUNKS_DIR = HERE.parents[0] / "Story-Chunks"

WORLD_ID = "latin-pastoral-congregational-christianity"
SCHEMA_VERSION = 2

WRITTEN: list[str] = []

# ---------------------------------------------------------------------------
# RELATION_PAIRS: the whole closed relation graph, each edge listed once as
# (id_a, id_b), all "associated-with" (the one symmetric relation type) --
# matching don's own s24 precedent exactly. Built and reciprocated from one
# list so every edge is declared on both ends by construction; main()'s own
# assertion catches any id here that this script did not actually emit.
RELATION_PAIRS: list[tuple[str, str]] = [
    ("lpc.story.election-of-cyprian", "lpc.figure.cyprian"),
    ("lpc.story.election-of-cyprian", "lpc.figure.pontius"),
    ("lpc.story.election-of-cyprian", "lpc.quote.ancient-venom-against-my-episcopate"),
    ("lpc.story.the-plague-and-the-enemies", "lpc.figure.cyprian"),
    ("lpc.story.the-plague-and-the-enemies", "lpc.figure.pontius"),
    ("lpc.story.numidicus", "lpc.figure.numidicus"),
    ("lpc.story.numidicus", "lpc.figure.cyprian"),
    ("lpc.story.hundred-thousand-sesterces", "lpc.figure.cyprian"),
    ("lpc.story.celerinus-writes-to-lucian", "lpc.figure.celerinus"),
    ("lpc.story.celerinus-writes-to-lucian", "lpc.figure.lucian"),
    ("lpc.story.the-death-of-cyprian", "lpc.figure.cyprian"),
    ("lpc.story.the-death-of-cyprian", "lpc.figure.pontius"),
    ("lpc.story.the-psalms-on-the-wall", "lpc.figure.augustine"),
    ("lpc.story.the-psalms-on-the-wall", "lpc.figure.possidius"),
    ("lpc.story.the-psalms-on-the-wall", "lpc.quote.clamour-and-tears"),
    ("lpc.figure.cyprian", "lpc.figure.pontius"),
    ("lpc.figure.cyprian", "lpc.figure.numidicus"),
    ("lpc.figure.cyprian", "lpc.figure.celerinus"),
    ("lpc.figure.cyprian", "lpc.figure.augustine"),
    ("lpc.figure.augustine", "lpc.figure.possidius"),
    ("lpc.figure.celerinus", "lpc.figure.lucian"),
    ("lpc.figure.cyprian", "lpc.quote.bishop-of-bishops"),
    ("lpc.figure.cyprian", "lpc.quote.ancient-venom-against-my-episcopate"),
    ("lpc.figure.cyprian", "lpc.quote.shepherd-wounded-in-the-flock"),
    ("lpc.figure.possidius", "lpc.quote.clamour-and-tears"),
    ("lpc.figure.augustine", "lpc.quote.clamour-and-tears"),
    ("lpc.figure.augustine", "lpc.quote.longing-expectation-is-a-prayer-for-me"),
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
               confidence, sources, retrieve_tier, retrieve_when, prefer_instead,
               claim_guards, body):
    rid = f"lpc.story.{slug}"
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
            "prefer_instead": prefer_instead,
        },
        "claim_guards": claim_guards,
        "relations": relations_for(rid),
        "narrative_tier": tier,
        "narrative_tier_justification": tier_just,
        "tellable_as": tellable_as,
        "text": text,
        "absent_detail": absent_detail,
        "modern_contrast": modern_contrast,
    }
    _write("story", rid, payload, body)


def emit_figure(slug, names, dates, narratable, bridge_line, confidence, sources, body,
                claim_guards=None):
    rid = f"lpc.figure.{slug}"
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
        "claim_guards": claim_guards or [],
        "names": names,
        "dates": dates,
        "narratable": narratable,
        "bridge_line": bridge_line,
        "relations": relations_for(rid),
    }
    _write("figure", rid, payload, body)


def emit_quote(slug, text, speaker_or_author, license_, modern_lens_note, modern_rendering,
               confidence, sources, retrieve_tier, retrieve_when, prefer_instead,
               claim_guards, body):
    rid = f"lpc.quote.{slug}"
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
            "prefer_instead": prefer_instead,
        },
        "claim_guards": claim_guards,
        "relations": relations_for(rid),
        "text": text,
        "speaker_or_author": speaker_or_author,
        "license": license_,
        "modern_lens_note": modern_lens_note,
        "modern_rendering": modern_rendering,
    }
    _write("quote", rid, payload, body)


# ===========================================================================
# STORIES (7) -- one per Story-Chunks/lpcstoryNNN_*.md, tiers copied from
# Doc_09 Section 3's own table.
# ===========================================================================

def build_stories() -> None:
    emit_story(
        "election-of-cyprian", 1,
        "Documented. Tier 1 (Doc_09 SS3), and the tier is assigned to this story rather than to its source. "
        "Pontius is an eyewitness with an identifiable social location -- our own bishop's own "
        "deacon -- writing within this world's horizon, which satisfies Tier 1's own author test. "
        "But Pontius is also writing hagiography, and Doc_02 SS4 flags that genre risk by name. "
        "What settles it for this story specifically is corroboration outside Pontius's own frame: "
        "in Ep. LXVII, Cyprian and thirty-six co-signatories argue that a bishop should be chosen "
        "'in the presence of the people, who have most fully known the life of each one,' pointing "
        "to a case they assume their readers already recognise -- the election-by-acclamation "
        "pattern is attested independently of the one biography that celebrates it. Carried rather "
        "than resolved: the specific claim that Cyprian was a neophyte rests on Pontius alone.",
        "How we came to read a recent convert's election, over his reluctance, as God's own "
        "judgment made plain",
        "Our own deacon Pontius, writing after his bishop had been executed, passed over most of "
        "what he could have said about Cyprian's early years and settled on one fact as enough. "
        "\"For the proof of his good works I think that this one thing is enough,\" he wrote: "
        "\"that by the judgment of God and the favour of the people, he was chosen to the office "
        "of the priesthood and the degree of the episcopate while still a neophyte, and, as it was "
        "considered, a novice.\"\n\n"
        "A neophyte. Newly baptised. Pontius did not soften this -- he pressed it, noting that "
        "Cyprian was \"still in the early days of his faith, and in the untaught season of his "
        "spiritual life.\" What we saw in him was not training. It was something we thought we "
        "could already see.\n\n"
        "Two things are claimed at once in that sentence, and for Pontius they are not in tension: "
        "the judgment of God, and the favour of the people. The second is how the first became "
        "visible to us -- and years afterward, writing to defend his own contested episcopate "
        "against a faction that had never accepted it, Cyprian himself would call that same "
        "acclamation by its proper name: our own suffrage, joined to God's own judgment.",
        "The specific claim that Cyprian was a neophyte rests on Pontius alone; no other witness "
        "of ours confirms or corrects it, and we do not claim more certainty about it than that "
        "one source supports. Pontius is writing in praise, and he says so himself.",
        "A modern listener may hear 'the people chose him' as describing a vote, with a candidacy "
        "and a count. We had none of that. What we had was a crowd whose favour we treated as "
        "evidence of God's own judgment, and a man who did not want the office in the first place.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.pontius-life-and-passion-of-cyprian",
          "locus": "SS5; cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line 27820",
          "license": "public-domain"},
         {"source_id": "lpc.source.cyprian-epistles",
          "locus": "Ep. LXVII, on the election of Sabinus, corroborating the acclamation pattern "
                   "independently of Pontius's own narrative",
          "license": "public-domain"}],
        1,
        ["participant asks how leaders were chosen among us",
         "participant asks whether ordinary people had any real say in who led them",
         "participant raises questions of authority, qualification, or whether a leader is 'ready'",
         "conversation reaches the pastoral office or collegial communion"],
        ["participant asks specifically about martyrdom or the end of Cyprian's own life -- ask "
         "about the death of Cyprian instead, which is differently tiered",
         "participant asks about modern church governance or ordination procedure, which this "
         "account cannot speak to"],
        [],
        "Mapped directly from Story-Chunks/lpcstory001_election-of-cyprian.md's own Story Text, "
        "Tier Justification and Usage Guidance sections, recast from third-person report into this "
        "world's own first-person register (see script docstring, REGISTER). The core quotation "
        "('by the judgment of God and the favour of the people... a neophyte') is independently "
        "re-located this session at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line "
        "27820 (the word 'neophyte' itself) and the surrounding lines through 27823 -- verification_"
        "state held at verified-direct on that basis. Ep. LXVII's own corroborating locus is carried "
        "from the chunk's own Tier Justification and not independently re-opened this session (its "
        "own quoted phrase, 'suffrage of the whole brotherhood', was located this session at the "
        "same vendored file, confirmed present); the closing sentence's own second reference to "
        "Cyprian's own words in Ep. XXXIX is this record's own addition, connecting forward to lpc."
        "quote.ancient-venom-against-my-episcopate (see QUOTE SET), and is not itself in the "
        "Story-Chunk.",
    )

    emit_story(
        "the-plague-and-the-enemies", 1,
        "Widely Accepted. Tier 1 at the narrative level, Widely Accepted rather than Documented (Doc_09 SS3). "
        "Pontius is a named eyewitness within the horizon, and the epidemic itself is independently "
        "attested -- Cyprian's own De mortalitate was written into it. The confidence is stepped "
        "down one band because the content of the address reaches us only through Pontius, "
        "reconstructing a sermon he heard, in a work written to praise the man who preached it -- a "
        "reported speech inside a biography of praise is not the same evidentiary object as a "
        "letter in the man's own hand. Not Tier 3: there is no miracle and no providential "
        "intervention, and the death-as-completion pattern absent because nobody dies here.",
        "How our bishop met a plague by teaching us to care for the very people persecuting us",
        "Pontius, writing as a deacon who was there, described the epidemic without any of the "
        "consolation he might have reached for. \"There broke out a dreadful plague,\" he wrote, "
        "\"and excessive destruction of a hateful disease invaded every house in succession of the "
        "trembling populace, carrying off day by day with abrupt attack numberless people, every "
        "one from his own house.\"\n\n"
        "What followed was not about the disease. It was about what the city did. \"All were "
        "shuddering, fleeing, shunning the contagion, impiously exposing their own friends\" -- "
        "bodies left where they fell, \"no longer bodies, but the carcases of many.\"\n\n"
        "Against that, our bishop called us together and preached. He began with mercy, and then "
        "went further. There was nothing remarkable, he told us, in caring for our own. Anyone does "
        "that. What would distinguish us was loving our enemies and praying for those persecuting "
        "us, in imitation of a God who \"continually makes His sun to rise, and from time to time "
        "gives showers to nourish the seed, exhibiting all these kindnesses not only to His people, "
        "but to aliens also.\" \"It becomes us,\" he said, \"to answer to our birth; and it is not "
        "fitting that those who are evidently born of God should be degenerate.\"\n\n"
        "And Pontius records what followed: relief given \"to all men, not to those only who are of "
        "the household of faith.\" The poor among us, who had no money to give, gave labour instead. "
        "Pontius reaches for a comparison and finds it wanting -- more was done, he writes, than is "
        "recorded of Tobias, who gathered up his own dead \"of his own race only.\"",
        "Whether the persecutors themselves were among those helped is not something Pontius says "
        "one way or the other, and no source outside him describes the relief operation at all. No "
        "pagan Carthaginian of ours left a word about being helped by us during this epidemic.",
        "A modern listener may hear 'love your enemies' as a maxim available anywhere. What is not "
        "available everywhere is the specific setting: said to a frightened congregation, in a city "
        "where the dead were left where they fell, by a bishop who would himself be executed eight "
        "years later.",
        conf("A", "verified-direct", "load-bearing", "Widely Accepted",
             "Widely Accepted rather than Documented because the address's own content reaches us "
             "only through Pontius reconstructing a remembered sermon in a work written to praise "
             "the man who preached it -- a reported speech inside a biography of praise, not a "
             "letter in the man's own hand (Story-Chunks/lpcstory002, Tier Justification)."),
        [{"source_id": "lpc.source.pontius-life-and-passion-of-cyprian",
          "locus": "SSSS9-10; cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines "
                   "27920-27980",
          "license": "public-domain"},
         {"source_id": "lpc.source.cyprian-minor-pastoral-treatises",
          "locus": "De Mortalitate, the corroborating treatise written into the same epidemic",
          "license": "public-domain"}],
        2,
        ["participant asks how we treated outsiders or enemies",
         "participant raises suffering, epidemic, or disaster",
         "participant asks what we did that was visibly different from those around us",
         "conversation reaches preaching and catechesis or the pastoral office"],
        ["participant is asking about martyrdom or persecution as such -- the plague was not a "
         "persecution, and treating it as one misreads this account",
         "participant asks about healing or miracle, which this account does not contain"],
        [],
        "Mapped directly from Story-Chunks/lpcstory002_the-plague-and-the-enemies.md, recast into "
        "first-person register. 'Dreadful plague' and 'a neophyte'-adjacent material independently "
        "re-located this session at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml (the "
        "epidemic description and Cyprian's own reported address, in the same Life and Passion "
        "Pontius text as lpcstory001, several thousand lines further on); verification_state held "
        "at verified-direct on that basis rather than only on the chunk's own prior citation.",
    )

    emit_story(
        "numidicus", 1,
        "Documented. Tier 1, Documented (Doc_09 SS3). This is Cyprian's own letter, written in his own hand as "
        "bishop, to his own congregation, about a man both he and they could identify -- the "
        "strongest evidentiary position any story in this repository occupies. There is no "
        "biographer between the reader and the event, no genre of praise, and no later tradition. "
        "The only caution worth stating is not about tier but about perspective: Cyprian is making "
        "a case for an appointment, and the letter's own rhetoric -- 'the common joy,' 'the "
        "greatest glory of our Church' -- is the rhetoric of advocacy.",
        "How we ordained a man on the strength of what he had endured, though he had not wanted "
        "to survive it",
        "Cyprian wrote to us with news he called 'the common joy.' He was appointing a presbyter, "
        "and he wanted us to know who the man was.\n\n"
        "Numidicus had watched a group of us die. He had exhorted them first -- Cyprian says he "
        "\"by his exhortation sent before himself an abundant number of martyrs, slain by stones "
        "and by the flames.\" Among the dead was his own wife. Cyprian's own phrasing about her is "
        "not a slip: he \"beheld with joy his wife abiding by his side, burned (I should rather say, "
        "preserved) together with the rest.\"\n\n"
        "Then Numidicus himself: \"half consumed, overwhelmed with stones, and left for dead.\" His "
        "daughter came looking for her father's body -- Cyprian says she sought it \"with the "
        "anxious consideration of affection\" -- and found him alive. Where she searched, the "
        "letter does not say. \"Was found half dead, was drawn out and revived.\"\n\n"
        "And Cyprian adds one clause that gives the whole letter its weight. Numidicus, he says, "
        "\"remained unwillingly from among the companions whom he himself had sent before.\" He had "
        "not wanted to survive. Cyprian knew this, wrote it down, and gave the reason he thought it "
        "happened: \"that the Lord might add him to our clergy.\"",
        "The three people this story is about left no word of their own. Numidicus's wife burned; "
        "his daughter searched for his body and found him alive; Numidicus himself did not want to "
        "have survived. What the wife thought she was doing, what the daughter found, and what "
        "Numidicus said when they revived him are unrecoverable, and nothing in our own corpus "
        "supplies them.",
        "A modern listener may hear 'burned, preserved' as a cruel word-game played on a real death. "
        "We did say that, and mean it: this world did not treat a martyr's death as a loss to be "
        "consoled but as a completion to be named correctly, even at the cost of sounding cold to "
        "an outsider.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Ep. XXXIV; cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines "
                   "32095-32115",
          "license": "public-domain"}],
        1,
        ["participant asks what persecution actually did to people",
         "participant asks how survivors were treated",
         "participant raises the cost of faithfulness, or survivor's guilt",
         "conversation reaches the pastoral office or ordination and validity"],
        ["participant is in acute grief or trauma and the physical detail would land badly -- ask "
         "about the psalms on the wall instead, which covers a gentler deathbed",
         "participant is asking about the lapsed generally rather than about Numidicus specifically "
         "-- ask about Celerinus's letter to Lucian instead, which carries the lapsed question "
         "directly"],
        [],
        "Mapped directly from Story-Chunks/lpcstory003_numidicus.md, recast into first-person "
        "register (Cyprian's own letter is already first-person in the chunk; the surrounding "
        "narration here is recast from 'Cyprian writes to the clergy and people of Carthage' to "
        "'Cyprian wrote to us'). 'Half consumed, overwhelmed with stones' independently re-located "
        "this session at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml; verification_state "
        "held at verified-direct on that basis.",
    )

    emit_story(
        "hundred-thousand-sesterces", 1,
        "Documented. Tier 1, Documented (Doc_09 SS3). Cyprian's own letter, first person, naming its eight "
        "recipients, stating an amount and a mechanism -- named author, exact social location, "
        "datable horizon, and a claim of the most ordinarily verifiable kind. One evidentiary "
        "discipline applies here: the "
        "ANF edition prints an Argument above the letter which is nineteenth-century editorial "
        "matter, not Cyprian; this record cites SS3 of the letter's own body, where Cyprian states "
        "the sum in his own voice, not the Argument that happens to carry the same true figure.",
        "How we sent a hundred thousand sesterces to ransom people most of us had never met",
        "Word reached us that fellow believers in the Numidian towns had been carried off by "
        "raiders. Cyprian's reply to the eight bishops who told us -- Januarius, Maximus, Proculus, "
        "Victor, Modianus, Nemesianus, Nampulus and Honoratus, whom he names one by one -- opens "
        "without composure: \"With excessive grief of mind, and not without tears.\"\n\n"
        "The argument he made was not about charity. It was about identity. Quoting Paul, that "
        "\"as many of you as have been baptized into Christ have put on Christ,\" he drew the "
        "conclusion directly: \"Christ is to be contemplated in our captive brethren, and He is to "
        "be redeemed from the peril of captivity who redeemed us from the peril of death.\"\n\n"
        "Then he said what the money was. \"We have then sent you a sum of one hundred thousand "
        "sesterces, which have been collected here in the Church over which by the Lord's mercy we "
        "preside, by the contributions of the clergy and people established with us, which you will "
        "there dispense with what diligence you may.\" And he thanked them, for being asked -- for "
        "offering us, in his own words, \"fruitful fields in which we might cast the seeds of our "
        "hope.\"",
        "We do not know whether the ransom worked. Cyprian never wrote again about the outcome, and "
        "the Numidian bishops' own reply, if there was one, does not survive. The story ends with "
        "the money leaving Carthage.",
        "A modern listener may reach at once for a currency conversion -- how much was that, really? "
        "Our own record licenses none. What it tells plainly is that it was collected from one "
        "congregation's clergy and people for the ransom of strangers, and that we do not know what "
        "proportion of anything it represented.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Ep. LIX SS3, the letter's own body text, not the ANF Argument; cic/texts/"
                   "anf05_hippolytus-cyprian-caius-novatian.xml, lines 36006-36090",
          "license": "public-domain"}],
        1,
        ["participant asks what we did with money",
         "participant asks whether churches helped people outside their own city",
         "participant raises practical mercy, ransom, or obligation to strangers",
         "conversation reaches collegial communion or the pastoral office"],
        ["participant is asking about modern charitable giving or church finance, which this story "
         "cannot be made to speak to without distortion",
         "participant is asking about slavery as an institution, which the letter does not address"],
        ["do not invent a modern-currency conversion for the hundred thousand sesterces -- no "
         "source of ours licenses one (Audollent, row 239, unlicensed, prints '25.000 francs' for "
         "this collection; do not use it), and the purchasing-power comparison is contested "
         "among specialists"],
        "Mapped directly from Story-Chunks/lpcstory004_hundred-thousand-sesterces.md, recast into "
        "first-person register. 'Hundred thousand sesterces' independently re-located this session "
        "at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line 36082 -- the same line "
        "this record's own sources[].locus field cites; verification_state held at "
        "verified-direct on that basis. The claim_guards entry converts the chunk's own 'the "
        "Representative should resist converting the sum into modern currency' Usage Guidance line "
        "into the live schema's own barred-claim field, per this script's own field-mapping "
        "discipline (see docstring).",
    )

    emit_story(
        "celerinus-writes-to-lucian", 1,
        "Documented. Tier 1, Documented (Doc_09 SS3). Two letters by named men with exact social locations -- "
        "confessors, one of them writing from prison -- within the horizon, transmitted in the "
        "corpus of the bishop who was arguing against what they did. That last fact is part of the "
        "tier argument: this material survives because Cyprian's own dossier preserved the case "
        "against himself. An attribution discipline matters here specifically: these letters are in "
        "Cyprian's corpus and are not by Cyprian.",
        "How two confessors, not our bishop, decided who could come back to us",
        "Celerinus was a confessor among us -- he had been imprisoned and had not denied Christ -- "
        "and he wrote to Lucian, another confessor, in prison. He did not write about himself. "
        "\"Know, nevertheless, that I am placed in the midst of a great tribulation,\" he began, and "
        "the tribulation was not his own captivity. His sister had sacrificed. \"I ask that you "
        "will grant my desire, and that you will grieve with me at the (spiritual) death of my "
        "sister, who in this time of devastation has fallen from Christ.\"\n\n"
        "She was not dead. She was alive, in Carthage, and what Celerinus grieved was a death he "
        "believed had happened to her soul -- which is why the letter carries a request. He asked "
        "Lucian to intervene, for her and for two other women, Numeria and Candida, whom Lucian "
        "also knew. He made the case for them: they had repented, and there were works to point to.\n\n"
        "Lucian's reply came back from the prison, and it granted what was asked. Before it did, it "
        "said what the prison had been like: by the emperor's command they \"were ordered to be put "
        "to death by hunger and thirst, and were shut up in two cells, that so they might weaken us "
        "by hunger and thirst.\" Then: \"But now we have attained the brightness itself.\" He greeted "
        "Numeria and Candida, and named the martyrs on whose authority he answered, and signed off "
        "exhausted, greeting others \"whose names I have not written, because I am already weary. "
        "Therefore they must pardon me.\"",
        "Celerinus's own sister has no story, and she is the person this one is about. She is "
        "unnamed -- her own brother does not name her. Numeria and Candida are not 'named lapsed "
        "women' either: Celerinus says the opposite of Candida, that she gave gifts for herself "
        "\"that she might not sacrifice\" -- her case is contested, not conceded. None of the three "
        "speaks for herself anywhere in our record.",
        "A modern listener may expect a bishop's own authority to be the only channel through which "
        "someone failed under pressure could be restored. Here it is two confessors, writing to "
        "each other from captivity, who decide -- and Cyprian's own dossier preserves the letters "
        "that argued against his own authority, rather than suppressing them.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Ep. XX (Celerinus to Lucian) and Ep. XXI (Lucian's reply); cic/texts/"
                   "anf05_hippolytus-cyprian-caius-novatian.xml, lines 30528-30720 -- widened "
                   "from an earlier draft's 30640-30720, which started about 70 lines after Ep. "
                   "XX's own opening (line 30528) and so did not cover the letter's own first "
                   "words, though the specifically re-verified detail this record cites "
                   "('put to death by hunger and thirst,' line 30706) was already correctly "
                   "inside it",
          "license": "public-domain"}],
        1,
        ["participant asks what happened to those who failed under persecution",
         "participant asks who had the authority to forgive",
         "participant raises a family member's lapse, shame, or a plea made on someone else's "
         "behalf",
         "conversation reaches penitential discipline or the confessor tension"],
        ["early in an encounter, before the participant has any sense of what the lapsed crisis "
         "was -- this story is unintelligible without that context first",
         "participant is asking about Cyprian's own position, which these letters do not represent "
         "and in part resist"],
        ["we must not resolve the confessor-authority tension by presenting the confessors as "
         "either usurpers or heroes",
         "no source of ours preserves anything Numeria, Candida, or Celerinus's own sister wrote or "
         "said -- do not invent words for any of the three"],
        "Mapped directly from Story-Chunks/lpcstory005_celerinus-writes-to-lucian.md, recast into "
        "first-person register (Celerinus/Lucian's own letters are already first-person; the "
        "surrounding narration is recast). 'Put to death by hunger and thirst' independently "
        "re-located this session at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line "
        "30706; verification_state held at verified-direct on that basis. Both claim_guards "
        "entries convert Usage Guidance lines the chunk already states ('the Representative must "
        "not resolve the tension...'; 'not one of these women speaks for herself') into the live "
        "schema's own barred-claim field.",
    )

    emit_story(
        "the-death-of-cyprian", 3,
        "Contested for the portrait; Inferential-Thin for details shaped by convention. "
        "Tier 3, and the tier turns on genre rather than on the author (Doc_09 SS3-4). Pontius "
        "meets Tier 1's own author test -- eyewitness deacon, identifiable location, within the "
        "horizon -- and lpcstory001/002 assign him Tier 1 on that basis. This story is different on "
        "the face of the text: the Zacchaeus parallel is an authorial aside, not a reader's "
        "inference, and the executioner's failing hand strengthened 'with power granted from "
        "above' is a providential intervention at the climax. CF V7.4's own genus clause ('resting "
        "on collected tradition rather than direct documentation') would exclude an eyewitness like "
        "Pontius; its hagiographic-convention clause describes this story exactly. Doc_09 assigns "
        "Tier 3 on the convention and against the genus clause, and carries the tension to the "
        "project lead as an open item rather than resolving it quietly -- unchanged here.",
        "How our tradition remembered the death of our first great bishop. We remember it as "
        "a life fully given, completed.",
        "This is how our own tradition remembered the death of our first great bishop -- an "
        "account written by his own deacon, in the form of a saint's life, showing what we believed "
        "a life fully given to the pastoral office could become. We offer it as that portrait, not "
        "as a report of what a bystander would have seen.\n\n"
        "In Pontius's telling, the crowd that came out for the execution could not all see, so "
        "people climbed. \"Persons who favoured him had climbed up into the branches of the "
        "trees.\" Pontius tells us what that resembled: \"that there might not even be wanting to "
        "him (what happened in the case of Zacchæus), that he was gazed upon from the "
        "trees.\"\n\n"
        "Then the bishop bound his own eyes. \"Having with his own hands bound his eyes, he tried "
        "to hasten the slowness of the executioner.\" The executioner could not do it easily -- the "
        "man needed, in Pontius's account, help from above: \"until the mature hour of "
        "glorification strengthened the hand of the centurion with power granted from above.\"\n\n"
        "The portrait we kept, then, is of a man more composed than the soldier killing him, in a "
        "crowd arranged like a scene from Scripture -- a life that ends the way we believed a "
        "formed life ends: ready before anyone else in the clearing is.",
        "What cannot be told is what the crowd made of it -- not one of them left an account of "
        "their own. What can be told is that the official version exists: the Acta Proconsularia, "
        "the court's own record of the proceedings, is vendored in this world's own corpus and "
        "Pontius himself points to it, but we have not read it. Reading it would likely move this "
        "story to Tier 1.",
        "A modern listener asking 'did that really happen?' deserves three things at once, not "
        "one: that Cyprian was certainly executed under Valerian in 258; that the account we have "
        "is written in praise by his own deacon, in a form that patterns deaths on Scripture; and "
        "that a strictly documentary record of the trial exists and we have not read it.",
        conf("B", "verified-direct", "load-bearing", "Contested",
             "Contested for the general portrait; Inferential-Thin for the specific details shaped "
             "by hagiographic convention (the Zacchaeus typology, the strengthened hand) -- CF "
             "V7.4's own Tier 3 confidence rule, and the tier assignment itself is disclosed as "
             "resting on the hagiographic-convention clause against the genus clause, an open "
             "escalation carried to the project lead rather than resolved here (Doc_09 SS8 item 7; "
             "Story-Chunks/lpcstory006, Tier Justification)."),
        [{"source_id": "lpc.source.pontius-life-and-passion-of-cyprian",
          "locus": "SSSS15-19; cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines "
                   "28100-28260",
          "license": "public-domain"},
         {"source_id": "lpc.source.acta-proconsularia-sancti-cypriani",
          "locus": "the strictly documentary witness, vendored in Latin only and not read in this "
                   "build; named here rather than silently omitted",
          "license": "public-domain"}],
        2,
        ["participant asks how we understood a life completed",
         "participant asks what we believed formation finally produced",
         "conversation reaches the pastoral office or the confessor tension"],
        ["participant wants to know what historically happened at Cyprian's own trial -- this "
         "account is not the right instrument, and the Acta has not been read"],
        ["this account must not be presented as historical fact that the executioner's hand was "
         "strengthened from above -- we report only that this is how the tradition told it"],
        "Mapped directly from Story-Chunks/lpcstory006_the-death-of-cyprian.md, recast into "
        "first-person register except the opening framing sentence, kept close to the chunk's own "
        "explicit 'this is how this world's tradition remembered' framing (recast to 'this is how "
        "our own tradition remembered', avoiding the literal phrase 'this world' per gate_voice_"
        "perspective). 'Bound his eyes' independently re-located this session at cic/texts/"
        "anf05_hippolytus-cyprian-caius-novatian.xml; verification_state held at verified-direct on "
        "that basis. retrieval.tier set to 2 (a specialized, hagiographic-register companion case "
        "to the six Tier 1 documentary stories), matching don's own precedent for its own Tier 3 "
        "story.",
    )

    emit_story(
        "the-psalms-on-the-wall", 1,
        "Documented. Tier 1, Documented (Doc_09 SS3). Possidius was a bishop in his own right, Augustine's "
        "friend for close to forty years, and -- decisively for the tier -- physically present: "
        "one of those Augustine 'asked of us who were present,' writing 'while we stood by and "
        "watched and prayed.' The distinction from lpcstory006, where both accounts are bishops' "
        "deaths written by admirers, is the presence or absence of the genre's own machinery: "
        "Pontius supplies a scriptural typology and a providential intervention; Possidius supplies "
        "sheets of paper on a wall, a request not to be disturbed, and an inventory of what the "
        "dead man did not own. The test applied is CF V7.4's own three Tier 3 markers, and this "
        "account carries none of them.",
        "How the one who spent his life adjudicating others' penitence was watched doing his own",
        "Possidius had been Augustine's friend for nearly forty years, and he was in the house.\n\n"
        "He records something Augustine had said often, in private conversation: that even after "
        "baptism, exemplary Christians and priests ought not depart this life without fitting "
        "repentance. Then he records what Augustine did with his own rule. \"And this he himself "
        "did in his last illness of which he died. For he commanded that the shortest penitential "
        "Psalms of David should be copied for him, and during the days of his sickness as he lay "
        "in bed he would look at these sheets as they hung upon the wall and read them; and he wept "
        "freely and constantly.\"\n\n"
        "About ten days before the end he asked to be left alone -- Possidius says he \"asked of us "
        "who were present that no one should come in to him, except only at the hours in which the "
        "physicians came to examine him or when nourishment was brought to him.\" The request was "
        "kept. Until that last illness he had not stopped preaching.\n\n"
        "And the end, in Possidius's own first person: \"With all the members of his body intact, "
        "with sight and hearing unimpaired, while we stood by and watched and prayed, 'he slept "
        "with his fathers,' as it is written, 'well-nourished in a good old age.'\" He made no "
        "will, because he had nothing to make one from. He ordered that the church's library and "
        "all its books be carefully preserved for those who came after. The city was under siege "
        "by the Vandals while this happened.",
        "Possidius is the only witness to the sickroom in the last weeks -- the psalms, the request, "
        "the ten days. The death itself is corroborated from outside Hippo, by its date and the siege "
        "around it, and Prosper adds only that Augustine was still answering Julian's books at the "
        "very end. What no second source gives is the interior of the sickroom. No one who fled "
        "Hippo wrote down what leaving the city was like, either.",
        "A modern listener may expect this told as a serene death. Possidius's own text does not "
        "support serenity: a man who spent his life teaching repentance wept freely and constantly "
        "for days, looking at psalms about sin -- the disproportion, if it looks like one, is the "
        "formation content, not an embarrassment to smooth over.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.possidius-vita-augustini-weiskotten1919",
          "locus": "SSSS28-31; cic/texts/possidius_vita-augustini_weiskotten1919.txt, lines "
                   "4900-5000",
          "license": "public-domain"},
         {"source_id": "lpc.source.prosper-epitoma-chronicon-mommsen1892",
          "locus": "the independent, outside-Hippo corroboration of the death's own date and the "
                   "siege around it, a. 430",
          "license": "public-domain"}],
        1,
        ["participant asks whether the people who taught repentance practised it",
         "participant raises dying, last illness, or preparing for death",
         "participant asks what happened as our own life closed",
         "conversation reaches penitential discipline or the pastoral office"],
        ["participant is asking about Augustine's own theology of grace, which this story does "
         "not carry",
         "immediately after the death of Cyprian -- two deathbeds in succession flattens both"],
        [],
        "Mapped directly from Story-Chunks/lpcstory007_the-psalms-on-the-wall.md, recast into "
        "first-person register. 'Shortest penitential Psalms' independently re-located this session "
        "at cic/texts/possidius_vita-augustini_weiskotten1919.txt, line 4925; verification_state "
        "held at verified-direct on that basis.",
    )


# ===========================================================================
# FIGURES (7)
# ===========================================================================

def build_figures() -> None:
    emit_figure(
        "cyprian",
        [{"name": "Cyprian, our bishop at Carthage", "tag": "in-world"},
         {"name": "Thascius Caecilius Cyprianus, bishop of Carthage (248/249-258)", "tag": "scholarly"}],
        {"display": "a trained rhetorician who turned from a public career to Christian life, "
                    "converted c. 246; ordained and elected bishop of Carthage between roughly "
                    "July 248 and April 249 by the acclamation of the Carthaginian people, over the "
                    "recorded opposition of five presbyters, while still newly baptised (Doc_01 SS2; "
                    "lpc.story.election-of-cyprian); banished to Curubis under the Valerianic "
                    "persecution; executed under the emperor Valerian in 258 (lpc.story.the-death-"
                    "of-cyprian)"},
        True,
        "our bishop, chosen while still a neophyte over his own reluctance. He taught us to "
        "care for our enemies during a plague. He was executed under Valerian.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.pontius-life-and-passion-of-cyprian",
          "locus": "the whole Life and Passion", "license": "public-domain"},
         {"source_id": "lpc.source.cyprian-epistles",
          "locus": "the whole corpus of his own letters", "license": "public-domain"}],
        "One of this world's own two anchor figures (Doc_09 SS1), central to four of the seven "
        "built stories (lpc.story.election-of-cyprian, lpc.story.the-plague-and-the-enemies, lpc."
        "story.numidicus as author, lpc.story.hundred-thousand-sesterces as author, lpc.story.the-"
        "death-of-cyprian) and the speaker of three of the four quotes this pass builds. Everything "
        "specific about his own early life beyond the bare conversion date reaches us through "
        "Pontius, his own admiring deacon (Doc_02 SS4); this record does not smooth that mediation "
        "into neutral narration.",
    )

    emit_figure(
        "augustine",
        [{"name": "Augustine, our bishop at Hippo", "tag": "in-world"},
         {"name": "Augustinius of Hippo Regius, presbyter 391, bishop 395/396-430", "tag": "scholarly"}],
        {"display": "converted 386, baptised 387; seized by the congregation at Hippo and ordained "
                    "presbyter against his own wishes in 391, weeping through it (Possidius, Vita "
                    "IV, independently re-located this session; Doc_01 SS2); designated coadjutor "
                    "and consecrated bishop of Hippo by Megalius, primate of Numidia, in 395/396, "
                    "again amid popular acclamation (Possidius, Vita VIII; Doc_01 SS2); died 430, "
                    "during the Vandal siege of Hippo (lpc.story.the-psalms-on-the-wall)"},
        True,
        "our bishop at Hippo, seized by our own acclaim for the office twice over his own "
        "reluctance. He spent his last days weeping over psalms of penitence while an army "
        "lay outside the walls.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.possidius-vita-augustini-weiskotten1919",
          "locus": "the whole Vita Augustini", "license": "public-domain"}],
        "The second of this world's own two anchor figures (Doc_09 SS1), central to the whole of "
        "Phase Two (lpc.story.the-psalms-on-the-wall, the only Phase Two story this pass builds) "
        "and the subject of lpc.quote.clamour-and-tears. Doc_01 SS2 finds the same congregational-"
        "acclamation-overriding-reluctance pattern recurring in his own career that lpc.story."
        "election-of-cyprian shows for Cyprian, at two separate points (the presbyterate in 391 and "
        "the episcopate in 395/396) rather than one -- this record names both rather than only the "
        "one lpcstory007 itself draws on.",
    )

    emit_figure(
        "pontius",
        [{"name": "Pontius, our bishop's own deacon", "tag": "in-world"},
         {"name": "Pontius the Deacon (fl. mid-3rd century)", "tag": "scholarly"}],
        {"display": "Cyprian's own deacon, present with him at his banishment to Curubis (lpc."
                    "source.pontius-life-and-passion-of-cyprian's own confidence note); wrote The "
                    "Life and Passion of Cyprian after his bishop's execution in 258, the first "
                    "Christian biography (Doc_09 SS2)"},
        True,
        "our bishop's own deacon, who stayed with him through exile. After the execution he "
        "wrote the account by which most of what we remember of Cyprian's own life reaches "
        "us.",
        conf("B", "verified-via-authority", "load-bearing", "Widely Accepted",
             "Widely Accepted rather than Documented: Pontius's own presence at Curubis is licensed "
             "for that specific fact but his own biography generally (SSSS2-4, Cyprian's conversion) "
             "has not been independently re-checked this session (lpc.source.pontius-life-and-"
             "passion-of-cyprian's own divergence_note)."),
        [{"source_id": "lpc.source.pontius-life-and-passion-of-cyprian",
          "locus": "the whole Life and Passion, and its own closing account of the author's "
                   "presence at the exile and the execution",
          "license": "public-domain"}],
        "The dominant mediating eyewitness for three of the seven built stories (lpc.story."
        "election-of-cyprian, lpc.story.the-plague-and-the-enemies, lpc.story.the-death-of-cyprian) "
        "-- all of Phase One's Cyprian-focused narrative material apart from Cyprian's own letters. "
        "Doc_09 SS2's own central tier judgement (assigning the tier per story rather than per "
        "source, since Pontius is both an eyewitness and a hagiographer) is built entirely around "
        "naming his own mediation rather than letting it pass as neutral narration; this figure "
        "record is the name-bridge that judgement itself presupposes.",
    )

    emit_figure(
        "possidius",
        [{"name": "Possidius, bishop of Calama", "tag": "in-world"},
         {"name": "Possidius of Calama (d. after 437)", "tag": "scholarly"}],
        {"display": "Augustine's own friend for nearly forty years; bishop of Calama in his own "
                    "right; physically present at Augustine's deathbed in 430, one of those "
                    "Augustine 'asked of us who were present' (lpc.story.the-psalms-on-the-wall); "
                    "wrote the Vita Augustini, the source for both lpc.story.the-psalms-on-the-wall "
                    "and lpc.quote.clamour-and-tears"},
        True,
        "the bishop of Calama who had been Augustine's friend for forty years, and who stood by "
        "him and prayed as he died",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.possidius-vita-augustini-weiskotten1919",
          "locus": "the whole Vita Augustini, and its own closing first-person account of "
                   "Augustine's own last illness and death",
          "license": "public-domain"}],
        "The main source for Phase Two's one built story, and its only witness to the sickroom "
        "(Prosper's chronicle corroborates only the date of death and the siege, and that Augustine "
        "was still answering Julian's books at the very end), and the source of lpc.quote."
        "clamour-and-tears -- the mirror of Pontius's own role for Phase One, a friendly rather "
        "than hostile mediating eyewitness whose own presence in the room (rather than only his "
        "own social location) is what the Tier Justification for lpc.story.the-psalms-on-the-wall "
        "rests its Tier 1 finding on. His own interventions and subscription also survive in the "
        "minutes of the 411 Conference (the PL XI Gesta), which this build has not read for his "
        "voice.",
    )

    emit_figure(
        "numidicus",
        [{"name": "Numidicus, our presbyter", "tag": "in-world"},
         {"name": "Numidicus of Carthage (fl. mid-3rd century)", "tag": "scholarly"}],
        {"display": "exhorted a group of Christians to martyrdom under persecution, among them his "
                    "own wife, who died with them; himself left half-consumed by fire and "
                    "overwhelmed with stones, found half dead by his own daughter and revived; "
                    "ordained presbyter by Cyprian afterward, though he had not wanted to survive "
                    "(Cyprian, Ep. XXXIV; lpc.story.numidicus)"},
        True,
        "a man who watched his own wife die with those he had exhorted to martyrdom. He was "
        "himself left for dead, and did not want to have survived.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Ep. XXXIV, the whole letter", "license": "public-domain"}],
        "The central named subject of lpc.story.numidicus, and this world's own clearest single "
        "case of ordination granted on the strength of what a man had endured rather than what he "
        "had studied -- the same criterion Doc_04 makes a Primary gravity (sacramental and "
        "ordination validity) applied here to one identifiable person in public. His own wife and "
        "daughter are visible in the same letter and never audible (Doc_09 SS7 item 4); neither is "
        "named, so neither is built as a figure of her own here.",
    )

    emit_figure(
        "celerinus",
        [{"name": "Celerinus, a confessor among us", "tag": "in-world"},
         {"name": "Celerinus of Carthage (fl. mid-3rd century)", "tag": "scholarly"}],
        {"display": "a confessor -- imprisoned under persecution and did not deny Christ; wrote to "
                    "Lucian, a fellow confessor in prison, asking that his own sister and two other "
                    "women be received back to communion (Ep. XX; lpc.story.celerinus-writes-to-"
                    "lucian)"},
        True,
        "a confessor who did not write about his own suffering, but about his sister's. He "
        "asked another confessor in prison to help restore her.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Ep. XX, the whole letter", "license": "public-domain"}],
        "One of two named confessors (with Lucian) whose own letters carry Doc_04's own Tensional "
        "gravity -- confessor-authority against episcopal-regulated peace -- in operation rather "
        "than in description, in the participants' own hands. His letter is preserved only because "
        "it survived inside Cyprian's own dossier, the bishop whose authority it in effect "
        "bypasses.",
    )

    emit_figure(
        "lucian",
        [{"name": "Lucian, a confessor among us", "tag": "in-world"},
         {"name": "Lucian of Carthage (fl. mid-3rd century)", "tag": "scholarly"}],
        {"display": "a confessor imprisoned under persecution, condemned to die by hunger and "
                    "thirst, who replied to Celerinus from the same prison, granting peace to "
                    "Celerinus's own sister and to Numeria and Candida (Ep. XXI; lpc.story."
                    "celerinus-writes-to-lucian)"},
        True,
        "a confessor who answered from a cell where he expected to die of hunger and thirst. "
        "He granted peace to three women he had never met in person.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Ep. XXI, the whole letter", "license": "public-domain"}],
        "The confessor whose own reply is the operative act of the tension lpc.story.celerinus-"
        "writes-to-lucian shows -- he, not Cyprian, grants the peace Celerinus asks for. Named "
        "separately from Celerinus rather than paired with him, since each is independently "
        "attested in his own letter and his own voice, not one account a third party narrates "
        "about both together.",
    )


# ===========================================================================
# QUOTES (4)
# ===========================================================================

def build_quotes() -> None:
    emit_quote(
        "bishop-of-bishops",
        "For neither does any of us set himself up as a bishop of bishops, nor by tyrannical "
        "terror does any compel his colleague to the necessity of obedience; since every bishop, "
        "according to the allowance of his liberty and power, has his own proper right of "
        "judgment, and can no more be judged by another than he himself can judge another. But let "
        "us all wait for the judgment of our Lord Jesus Christ, who is the only one that has the "
        "power both of preferring us in the government of His Church, and of judging us in our "
        "conduct there.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may hear this as an early anti-papal manifesto, or a constitutional "
        "principle about separated powers among equal branches. We mean neither. It is a working "
        "statement of how a council among us proceeds, said by the man presiding, inside a shared "
        "conviction that the episcopate is one undivided office rather than a hierarchy of ranks.",
        "No one of us stands over the other bishops, and none forces another to obey through fear. "
        "Each bishop has his own right to judge for himself, and answers for it only to Christ, who "
        "alone has the power to judge us all.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-seventh-council-of-carthage",
          "locus": "the 256 Council preface; independently re-located and re-read this session at "
                   "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line 56872",
          "license": "public-domain"},
         {"source_id": "lpc.source.augustine-on-baptism-against-the-donatists",
          "locus": "Augustine's own three independent quotations of the identical proposition "
                   "while arguing against it at length; cic/texts/npnf104_augustine-anti-"
                   "manichaean-anti-donatist.xml, lines 11292, 11626, 12207",
          "license": "public-domain"}],
        1,
        ["participant asks whether one bishop could overrule another",
         "participant asks about church government, councils, or the origins of papal authority",
         "participant asks how disputes between bishops were settled",
         "conversation reaches conciliar authority theory"],
        ["participant is asking about a bishop's own authority over his own congregation rather "
         "than about bishops' authority over each other -- ask about the flock instead"],
        [],
        "Named directly in the Permanent Prompt's own 'what our own life actually gave us' "
        "paragraph (line 37, and quoted at greater length at line 29): 'Neither of us set himself "
        "up as a bishop of bishops.' The line is also the sole cited locus of the already-built "
        "lpc.term.bishop-of-bishops (records/lpc/term/, B-2/B-3, read but not touched this pass) -- "
        "this record supplies a quote-record name-bridge and a modern_rendering for the same "
        "already-established text, not a duplicate finding. Independently re-located and re-read "
        "this session at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line 56872, and "
        "independently corroborated at three further points in the same vendored file where "
        "Augustine quotes the identical proposition back at Cyprian's own successors while arguing "
        "against it (lines 11292, 11626, 12207) -- the strongest cross-attested single line in "
        "this world's whole corpus, matching don's own precedent of preferring a quote independently "
        "corroborated by a second, differently-motivated witness over one attested only once.",
    )

    emit_quote(
        "ancient-venom-against-my-episcopate",
        "Since mindful of their conspiracy, and retaining that ancient venom against my "
        "episcopate, that is, against your suffrage and God's judgment, they renew their old "
        "attack upon me, and once more begin their sacrilegious machinations with their accustomed "
        "craft.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may hear 'ancient venom' as ordinary rhetorical exaggeration against a "
        "rival. Cyprian's own point is more specific: the hostility named here is not aimed at him "
        "personally so much as at the act by which he became bishop at all -- our own suffrage, "
        "joined to what he calls God's own judgment. Rejecting him, on his own reading, meant "
        "rejecting that acclamation itself.",
        "They still carry that old poison against me as bishop. That means against your own vote, "
        "and God's own judgment. So they attack me again, the same way as before.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Ep. XXXIX SS1; independently re-located and re-read this session at cic/texts/"
                   "anf05_hippolytus-cyprian-caius-novatian.xml, line 32372",
          "license": "public-domain"}],
        2,
        ["participant asks whether Cyprian's own election was ever accepted without dispute",
         "conversation reaches lpc.story.election-of-cyprian and needs Cyprian's own later word "
         "for the hostility that persisted after it"],
        ["participant is asking about the Felicissimus schism's own doctrinal content (this quote "
         "names the persistence of the hostility toward Cyprian's own election specifically, not "
         "the schism's own later grounds)"],
        [],
        "Named directly in the Permanent Prompt's own 'what our own life actually gave us' "
        "paragraph (line 37: 'a faction's ancient venom set against the plain suffrage of the "
        "people'), and at greater length at line 29 ('the crowd's own calling of a man to this "
        "office -- a faction's ancient venom set against the plain suffrage of the people, in one "
        "voice'). Independently re-located this session at cic/texts/anf05_hippolytus-cyprian-"
        "caius-novatian.xml, line 32372 -- the corrected locus (Ep. XXXIX, not Ep. XL) lpc.source."
        "cyprian-epistles's own divergence_note already names (a citation error stood in this "
        "world's build for six days before correction); this record independently re-verifies the "
        "corrected locus directly rather than trusting the correction on the source record's own "
        "say-so, per this step's own discipline for the small set of places a confidence rating "
        "depends on a specific line actually being where it is said to be. This quotation begins "
        "mid-sentence in the source ('...since mindful of their conspiracy...'); per Doc_09 SS2's "
        "own disclosed transcription convention, the first letter is capitalised here without an "
        "opening ellipsis, and no wording is altered.",
    )

    emit_quote(
        "shepherd-wounded-in-the-flock",
        "I grieve, brethren, I grieve with you; nor does my own integrity and my personal "
        "soundness beguile me to the soothing of my griefs, since it is the shepherd that is "
        "chiefly wounded in the wound of his flock. I join my breast with each one, and I share in "
        "the grievous burden of sorrow and mourning. I wail with the wailing, I weep with the "
        "weeping...",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may hear a bishop's grief for his flock as pastoral sentiment, a manner "
        "of speaking. Cyprian states it as a claim about his own office's own nature: a shepherd's "
        "own wound is not sympathy offered from outside the flock's own suffering, but the same "
        "wound, felt at its own worst point.",
        "I grieve with you, and I will not let my own safety comfort me out of it, because it is "
        "the shepherd who is hurt worst by the wound to his own flock. I carry each of you in my "
        "own chest. I wail with those who wail, I weep with those who weep.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-de-lapsis",
          "locus": "De Lapsis SS4; independently re-located and re-read this session at cic/texts/"
                   "anf05_hippolytus-cyprian-caius-novatian.xml, line 43729",
          "license": "public-domain"}],
        2,
        ["participant asks what it meant for us that a bishop was answerable for a whole flock",
         "participant asks how we spoke about a leader's own grief for those under his care",
         "conversation reaches the pastoral office and needs the image lpc.term.the-flock already "
         "names in prose, voiced directly"],
        ["participant wants the lapsed crisis's own doctrinal argument rather than this passage's "
         "own grief -- De Lapsis argues that case elsewhere; this quote is the grief that opens it"],
        [],
        "Named directly in the Permanent Prompt's own 'what our own life actually gave us' "
        "paragraph (line 37: 'the shepherd who is chiefly wounded in the wound of his own flock, "
        "and wails with the wailing and weeps with the weeping' -- the Prompt's own light "
        "paraphrase of 'wail with the wailing' as 'wails with the wailing'). Independently "
        "re-located this session at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line "
        "43729, and grounds the same locus lpc.term.the-flock (records/lpc/term/, read but not "
        "touched this pass) already cites at 'De Lapsis 4' in its own sources[] -- this record "
        "independently re-confirms that citation rather than only inheriting it. The trailing "
        "ellipsis marks a real elision: the source's own sentence continues, uninterrupted by a "
        "period, into 'I regard myself as prostrated with those that are prostrate,' which this "
        "quote does not carry -- ending the quotation at 'weeping' with an invented period, rather "
        "than the ellipsis actually used here, would have been a punctuation alteration this step's "
        "own discipline forbids.",
    )

    emit_quote(
        "clamour-and-tears",
        "The Catholics, already acquainted with the life and teaching of the holy Augustine, "
        "laid hands on him — for he was standing there among the people secure and unaware of "
        "what was about to happen... So they laid hands on him and, as is the custom in such "
        "cases, brought him to the bishop to be ordained, for all with common consent desired that "
        "this should be done and accomplished ; ancf they demanded it with great zeal and clamor, "
        "while he wept freely.",
        "lpc.figure.possidius",
        "verbatim",
        "A modern listener may hear 'they demanded it with clamor' and picture an orderly election. "
        "Possidius describes something closer to a seizure: a congregation physically laying hands "
        "on a man standing unaware among them and refusing to let him leave until the ordination "
        "was done, while he wept -- the same congregational-acclamation pattern lpc.story.election-"
        "of-cyprian shows for Cyprian, a century and a half earlier, recurring at Hippo for "
        "Augustine.",
        "We already knew Augustine's own life and teaching, so we took hold of him -- he was "
        "standing right there among us, with no idea what was coming. We brought him to the bishop "
        "to be ordained, because all of us together wanted it done. We demanded it, loudly, while "
        "he wept.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The vendored Weiskotten scan carries a single OCR artifact inside this quotation -- "
             "'ancf' for 'and' -- reproduced here exactly as the scan gives it (matching this "
             "record's own text against the raw file precisely, per this step's own discipline), "
             "not silently corrected; modern_rendering gives the plain sense ('We demanded it...') "
             "rather than reproducing the artifact."),
        [{"source_id": "lpc.source.possidius-vita-augustini-weiskotten1919",
          "locus": "Vita Augustini IV; independently re-located and re-read this session at cic/"
                   "texts/possidius_vita-augustini_weiskotten1919.txt, line 1817",
          "license": "public-domain"}],
        1,
        ["participant asks how Augustine came to be ordained",
         "conversation reaches lpc.story.the-psalms-on-the-wall and needs the same congregation's "
         "own earlier claim on him, at the office's own point of entry rather than its end",
         "participant asks whether the congregational-acclamation pattern lpc.story.election-of-"
         "cyprian shows recurs at Hippo"],
        ["participant wants Augustine's own later account of the same event in his own words -- "
         "this quote is Possidius's own narration; Augustine's own first-person account survives "
         "separately (Sermo CCCLV) and is named in this record's own body, not quoted here as the "
         "record's own text"],
        [],
        "Named directly in the Permanent Prompt's own 'what our own life actually gave us' "
        "paragraph (line 37: 'the crowd's own clamour at a second bishop's own reluctant "
        "elevation'), and at greater length at line 29. Independently re-located this session at "
        "cic/texts/possidius_vita-augustini_weiskotten1919.txt, line 1817 -- Chapter IV, Augustine's "
        "own ordination as presbyter in 391, OUTSIDE lpc.story.the-psalms-on-the-wall's own "
        "declared SSSS28-31 span (the death and burial sequence), inside the same file row 192 "
        "already licenses; the same disclosed reach-beyond-the-story's-own-span move don's own "
        "script names for its own Optatus Book III quote. The translator's own endnote at this "
        "chapter (page 150 of the vendored edition) additionally quotes Augustine's own first-"
        "person account, Sermo CCCLV i 2: 'Apprehensus presbyter factus sum, et per hunc gradum "
        "perveni ad episcopatum' ('I was seized and made a presbyter, and through this step I "
        "arrived at the episcopate') -- independently re-located this session and named here as "
        "corroboration, not substituted for Possidius's own third-person account as this record's "
        "own `text` field, which stays the narration actually quoted rather than a different "
        "witness's own words spliced in.",
    )

    emit_quote(
        "longing-expectation-is-a-prayer-for-me",
        "But now I imagine that none have come here, but they who desire to hear, and so I am "
        "not speaking to hearts that are deaf, and to minds that will disdain the word, but this "
        "your longing expectation is a prayer for me.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear this as a preacher's flattery of an attentive crowd. Augustine "
        "means something more exact: the congregation's own act of showing up and waiting to hear "
        "him is itself, for him, a form of intercession on his behalf -- not a compliment to them, "
        "but a claim about what their attention does for the man who has to speak.",
        "I know you're here because you want to hear this, not because you have to. So I'm not "
        "talking to people who won't listen. Your own waiting, right now, is itself a prayer for "
        "me.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "Independently re-located this session by direct keyword search of the vendored file "
             "-- corrects this script's own earlier draft, which had claimed the same search "
             "'did not locate' this quote. It does, in fact, occur verbatim at the cited line. "
             "The earlier claim is not repeated in this record; it is disclosed instead in this "
             "script's own docstring (QUOTE SET, item 7), as a fabrication-class error caught and "
             "corrected before commit, not carried forward."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon I [LI, Benedictine], 'Of the agreement of the evangelists Matthew and "
                   "Luke in the generations of the Lord,' delivered at the matins of the Nativity "
                   "festival; independently re-located this session at cic/texts/npnf106_augustine-"
                   "sermon-mount-harmony-gospels-homilies.xml, line 9398",
          "license": "public-domain"}],
        1,
        ["participant asks what preaching meant to this world, or what a congregation's own "
         "presence meant to a preacher",
         "conversation reaches lpc.term.preaching and needs a single concrete instance",
         "participant asks for an image of the bond between a congregation and the one who "
         "speaks to it, distinct from the office-and-discipline images this world reaches for "
         "more often"],
        ["participant wants a pastoral-discipline or penitential image instead -- this quote is "
         "about the bond of ordinary preaching, not about failure, office, or schism, and should "
         "not be reached for outside that register"],
        [],
        "Named directly in the Permanent Prompt's own 'what our own life actually gave us' "
        "paragraph, its final named image: 'A preacher naming, to the very people gathered in "
        "front of him, that their own waiting is itself a kind of prayer for him.' This is the "
        "fifth of the Permanent Prompt's seven candidate images to be built as a quote record -- "
        "the other two (the certificate/wide-door contrast and the two-answers-on-baptism "
        "contrast) remain synthesized prose without a single quotable sentence, disclosed as such "
        "in this script's own docstring rather than built. Sermon I is undated within this "
        "world's own construction record beyond 'delivered at the matins of the festival of the "
        "Lord's Nativity' (the sermon's own words) -- no further narrowing is attempted here.",
    )


def main() -> None:
    build_stories()
    build_figures()
    build_quotes()

    chunk_files = sorted(STORY_CHUNKS_DIR.glob("lpcstory*.md"))
    story_files = [w for w in WRITTEN if "/story/" in w]
    figure_files = [w for w in WRITTEN if "/figure/" in w]
    quote_files = [w for w in WRITTEN if "/quote/" in w]

    assert len(chunk_files) == 7, (
        f"expected 7 Story-Chunks files (Doc_09's own count), found {len(chunk_files)} -- "
        "re-check Build/worlds/lpc/Story-Chunks/ before trusting this script's own story count against it"
    )
    assert len(story_files) == len(chunk_files) == 7, (
        f"expected one story record per Story-Chunk (7), wrote {len(story_files)}"
    )
    assert len(figure_files) == 7, f"expected 7 figure records, wrote {len(figure_files)}"
    assert len(quote_files) == 5, f"expected 5 quote records (bounded set, see docstring), " \
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
