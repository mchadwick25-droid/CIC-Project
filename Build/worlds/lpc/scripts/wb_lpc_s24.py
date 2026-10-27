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
    set. Several images are named there; SIX become `quote` records here --
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
      of Calama, the principal source for lpcstory007 (the whole of Phase Two)
      and, independently, the quote this script builds at lpc.quote.
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
builds `quote` records for SIX of these seven:
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
  5. BUILT with the host quotes below (item 4 above, the certificate/
     wide-door image): lpc.quote.such-a-one-with-his-friends. Cyprian, Ep.
     X section 4: "For it opens a wide door to say, 'Such a one with his
     friends'", at line 29942 of the ANF file.
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
This is a disclosed narrowing, not a silent one: item 6 above is a
synthesized contrast with no single quotable sentence behind it and is not
built; the other six, each verified against its vendored source file, are.

SERMON QUOTES. Eighteen further `quote` records quote Augustine's sermons on
selected lessons (Source Registry row 19), three per gravity for the pastoral
office, penitential discipline, collegial communion, sacramental validity,
preaching and catechesis, and grace and human incapacity.
Each `text` is the NPNF English word for word; each `modern_rendering` is the
Opus rendering as written; each `sources[].locus` gives the NPNF and Maurist
sermon numbers, the section, the file lines and the PL 38 Latin lines. Each
carries one `associated-with` edge to the gravity record it bears, and s25
declares the inverse edge. Their canon cells are assigned by s2y.

COMMENTARY QUOTES. Fifteen further `quote` records quote Augustine's
commentary on Scripture: four passages from the Expositions on the Psalms,
six from the Tractates on John, two from the Homilies on the First Epistle of
John and three from the Sermon on the Mount. Each bears one of the world's
gravities. Each `text` is the NPNF English word for word; each
`modern_rendering` is the Opus rendering as written; each
`sources[].locus` gives the work and section, the NPNF file lines and, where
a Latin text is vendored, the Latin file lines. No Latin of the Sermon on the
Mount is vendored, and its three records say so. Each carries one
`associated-with` edge to the gravity record it bears, and s25 declares the
inverse edge. Their canon cells are assigned by s2y and their use notes by
s2u.

DISCLOSURE QUOTES. Seventeen further `quote` records give what the bishops held on
hell, judgment, the dead, infants, outsiders and suicide, the hard parts included. Eight
are from Augustine's Enchiridion (chapters 69, 70, 93, 110 in two parts, 111
and 112 in two parts), one is from Augustine's On the Merits and Forgiveness of
Sins (unbaptized infants), one is from the Confessions (Monica's request), three
are from Cyprian's letters (two to Fidus on infants, one to Jubaianus on
heretics), two are from Cyprian's To Demetrianus (the fire that has no end, and
the time for repentance) and two are from City of God I.17 (the forgiveness of
the virgins and the death of Judas). Each `text` is the NPNF or ANF English word
for word. A scripture reference note is left out and not marked. An editor's
bracketed note inside a passage is likewise left out and not marked, and the body
says so. Each `modern_rendering` is the Opus rendering as written, except the
three newest records, which carry the placeholder RENDERING-PENDING until Opus
writes them. Each `sources[].locus` gives the work and section, the English file
lines and the Latin file lines. Each carries an `associated-with` edge to the
`doctrinal_witness` record it bears, and that witness file declares the inverse
edge. Their
canon cells are assigned by s2y and their use notes by s2u.

PENITENT-IN-PERIL QUOTES. Two further `quote` records, both from Cyprian's letters,
give the provision for a penitent in peril of sickness: confession before a presbyter or
a deacon (Epistle XII) and the council's clause that such penitents be assisted and have
peace (Epistle LII). Each `text` is the ANF English word for word. Their `modern_rendering`
is the placeholder RENDERING-PENDING until Opus writes it. Each carries an `associated-with`
edge to lpc.witness.peace-for-the-dying-penitent, which declares the inverse edge. Their
canon cells are assigned by s2y and their use notes by s2u.

HOST QUOTES. Twenty-nine further `quote` records hold each real source
quotation that a story, gravity, force or term record carries. The host
paraphrases the quotation in plain words and declares an `associated-with`
edge to the quote record. Each `text` is the vendored source word for word:
the ANF, NPNF or Weiskotten English, or, for the Acta Proconsularia, the
Latin of whichever vendored edition reads cleanly at that passage. Each
body gives the file and lines. Story edges are declared here; gravity and
force edges are mirrored in s25 and the term edge in s22. Their canon cells
are assigned by s2y.

RELATIONS -- CLOSED-GRAPH DISCIPLINE. Every `relations[]` entry this script
writes points at another record this same script creates (story<->story,
story<->figure, story<->quote, figure<->figure, figure<->quote), except the
eighteen sermon quotes, whose gravity edges are reciprocated by s25, and the
seventeen disclosure quotes, whose witness edges are reciprocated in the
witness files. The
graph is built and reciprocated by one master pair-list (RELATION_PAIRS
below), so every edge is declared on both ends by construction. Term
connections (lpc.term.bishop-of-bishops, lpc.term.the-flock,
lpc.term.certificates-letters-of-peace, and others) are named in each
record's own prose body instead.

MECHANICAL vs AUTHORED, field by field:
  - id, world_id, record_type, schema_version, status, register, canon_cells:
    MECHANICAL. world_id="latin-pastoral-congressional-christianity" is a
    typo risk this script guards against directly (see WORLD_ID below --
    the actual value used is the correct
    "latin-pastoral-congregational-christianity", cross-checked byte-for-
    byte against an existing lpc/source record's own world_id field, not
    retyped from memory). status="ready" throughout: every record here has
    cleared its review before it ships.
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
    modernization of the published ANF/NPNF/Weiskotten translation the
    record's own `text` field quotes, following the Latin edition only where
    the English misleads, as that record's divergence_note says. Where the
    `text` field is the Latin itself (the Acta Proconsularia, which has no
    vendored English), modern_rendering translates that Latin.
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
and not built, for reasons that remain unchanged by this script); register `lpc` in records/worlds/ (a later
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
    ("lpc.story.the-plague-and-the-enemies", "lpc.witness.restless-heart-and-the-unrepentant-enemy"),
    ("lpc.story.numidicus", "lpc.figure.numidicus"),
    ("lpc.story.numidicus", "lpc.figure.cyprian"),
    ("lpc.story.hundred-thousand-sesterces", "lpc.figure.cyprian"),
    ("lpc.story.hundred-thousand-sesterces", "lpc.witness.almsgiving-quenches-sin"),
    ("lpc.story.celerinus-writes-to-lucian", "lpc.figure.celerinus"),
    ("lpc.story.celerinus-writes-to-lucian", "lpc.figure.lucian"),
    ("lpc.story.the-death-of-cyprian", "lpc.contested.cyprian-death-genre"),
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
    ("lpc.quote.ye-belong-to-my-care", "lpc.gravity.pastoral-office-flock-keeping"),
    ("lpc.quote.stewards-and-future-bishops", "lpc.gravity.pastoral-office-flock-keeping"),
    ("lpc.quote.good-works-the-comfort-of-our-dangers", "lpc.gravity.pastoral-office-flock-keeping"),
    ("lpc.quote.bind-him-justly", "lpc.gravity.penitential-discipline"),
    ("lpc.quote.reprove-and-forgive-the-surgeons-knife", "lpc.gravity.penitential-discipline"),
    ("lpc.quote.peter-the-sick-man-and-the-physician", "lpc.gravity.penitential-discipline"),
    ("lpc.quote.one-good-shepherd-not-many", "lpc.gravity.collegial-communion-preserved"),
    ("lpc.quote.apart-in-heart-united-in-body", "lpc.gravity.collegial-communion-preserved"),
    ("lpc.quote.going-out-without-violating-unity", "lpc.gravity.collegial-communion-preserved"),
    ("lpc.quote.the-branch-cut-from-the-vine", "lpc.gravity.sacramental-ordination-validity"),
    ("lpc.quote.pardon-through-a-wicked-clergyman", "lpc.gravity.sacramental-ordination-validity"),
    ("lpc.quote.consider-who-was-there", "lpc.gravity.sacramental-ordination-validity"),
    ("lpc.quote.the-creed-first-then-the-prayer", "lpc.gravity.preaching-and-catechesis"),
    ("lpc.quote.let-your-creed-be-a-mirror", "lpc.gravity.preaching-and-catechesis"),
    ("lpc.quote.the-sermon-and-the-readings-are-daily-bread", "lpc.gravity.preaching-and-catechesis"),
    ("lpc.quote.two-hear-one-scorns-one-rises", "lpc.gravity.grace-and-human-incapacity"),
    ("lpc.quote.what-is-done-by-you-he-does-in-you", "lpc.gravity.grace-and-human-incapacity"),
    ("lpc.quote.no-one-has-the-love-of-god-from-himself", "lpc.gravity.grace-and-human-incapacity"),
    ("lpc.quote.the-old-man-nailed-to-the-cross-speaks", "lpc.gravity.grace-and-human-incapacity"),
    ("lpc.quote.david-himself-hath-been-sent-to-thee", "lpc.gravity.penitential-discipline"),
    ("lpc.quote.dash-the-little-ones-against-the-rock", "lpc.gravity.preaching-and-catechesis"),
    ("lpc.quote.they-first-dwelt-together-in-unity", "lpc.gravity.collegial-communion-preserved"),
    ("lpc.quote.peter-may-baptize-but-this-is-he-that-baptizeth", "lpc.gravity.sacramental-ordination-validity"),
    ("lpc.quote.the-word-is-added-to-the-element", "lpc.gravity.sacramental-ordination-validity"),
    ("lpc.quote.believe-and-thou-hast-eaten-already", "lpc.gravity.grace-and-human-incapacity"),
    ("lpc.quote.the-wretched-woman-and-mercy", "lpc.gravity.penitential-discipline"),
    ("lpc.quote.the-flight-of-the-mind-is-fear", "lpc.gravity.pastoral-office-flock-keeping"),
    ("lpc.quote.let-it-be-the-office-of-love-to-feed-the-flock", "lpc.gravity.pastoral-office-flock-keeping"),
    ("lpc.quote.love-and-do-what-thou-wilt", "lpc.gravity.penitential-discipline"),
    ("lpc.quote.they-went-out-from-us-but-were-not-of-us", "lpc.gravity.collegial-communion-preserved"),
    ("lpc.quote.many-have-learned-to-offer-the-other-cheek", "lpc.gravity.preaching-and-catechesis"),
    ("lpc.quote.all-sins-against-us-are-to-be-forgiven", "lpc.gravity.penitential-discipline"),
    ("lpc.quote.judge-not-nor-despair-of-a-return", "lpc.gravity.penitential-discipline"),
    ("lpc.story.election-of-cyprian", "lpc.quote.chosen-while-still-a-neophyte"),
    ("lpc.story.the-plague-and-the-enemies", "lpc.quote.a-dreadful-plague-broke-out"),
    ("lpc.story.the-plague-and-the-enemies", "lpc.quote.it-becomes-us-to-answer-to-our-birth"),
    ("lpc.story.the-plague-and-the-enemies", "lpc.quote.good-done-to-all-not-only-the-household"),
    ("lpc.story.numidicus", "lpc.quote.numidicus-remained-unwillingly"),
    ("lpc.story.hundred-thousand-sesterces", "lpc.quote.grief-and-not-without-tears"),
    ("lpc.story.hundred-thousand-sesterces", "lpc.quote.christ-redeemed-in-our-captive-brethren"),
    ("lpc.story.hundred-thousand-sesterces", "lpc.quote.a-hundred-thousand-sesterces"),
    ("lpc.story.celerinus-writes-to-lucian", "lpc.quote.grieve-with-me-for-my-sister"),
    ("lpc.story.celerinus-writes-to-lucian", "lpc.quote.shut-up-in-two-cells"),
    ("lpc.story.celerinus-writes-to-lucian", "lpc.quote.the-case-set-before-the-bishop"),
    ("lpc.story.celerinus-writes-to-lucian", "lpc.quote.because-i-am-already-weary"),
    ("lpc.story.the-death-of-cyprian", "lpc.quote.the-people-kept-watch-at-the-door"),
    ("lpc.story.the-death-of-cyprian", "lpc.quote.the-whole-people-of-the-brethren-came"),
    ("lpc.story.the-death-of-cyprian", "lpc.quote.walled-in-by-a-mingled-multitude"),
    ("lpc.story.the-death-of-cyprian", "lpc.quote.a-standard-bearer-of-the-sect"),
    ("lpc.story.the-death-of-cyprian", "lpc.quote.thanks-be-to-god"),
    ("lpc.story.the-death-of-cyprian", "lpc.quote.let-us-too-be-beheaded-with-him"),
    ("lpc.story.the-death-of-cyprian", "lpc.quote.he-covered-his-eyes-with-his-own-hand"),
    ("lpc.story.the-death-of-cyprian", "lpc.quote.the-trees-and-the-trembling-executioner"),
    ("lpc.story.the-death-of-cyprian", "lpc.quote.o-blessed-people-of-the-church"),
    ("lpc.story.the-psalms-on-the-wall", "lpc.quote.the-psalms-hung-upon-the-wall"),
    ("lpc.story.the-psalms-on-the-wall", "lpc.quote.he-slept-with-his-fathers"),
    ("lpc.quote.chosen-while-still-a-neophyte", "lpc.force.congregational-acclamation-overriding-preference"),
    ("lpc.quote.ancient-venom-against-my-episcopate", "lpc.force.congregational-acclamation-overriding-preference"),
    ("lpc.quote.shepherd-wounded-in-the-flock", "lpc.force.decian-persecution-libelli-system"),
    ("lpc.quote.bishop-of-bishops", "lpc.gravity.collegial-communion-preserved"),
    ("lpc.quote.bishop-of-bishops", "lpc.gravity.conciliar-authority-theory"),
    ("lpc.quote.earlier-councils-corrected-by-later", "lpc.force.augustine-engagement-cyprian-conciliar-acts"),
    ("lpc.quote.earlier-councils-corrected-by-later", "lpc.gravity.conciliar-authority-theory"),
    ("lpc.quote.boast-in-nothing-since-nothing-is-our-own", "lpc.gravity.grace-and-human-incapacity"),
    ("lpc.quote.thousands-of-certificates-daily", "lpc.force.confessors-claim-to-grant-peace"),
    ("lpc.quote.thirteen-letters-sent-to-rome", "lpc.force.transmission-institutionally-dominant-side"),
    ("lpc.quote.the-paper-itself", "lpc.force.transmission-institutionally-dominant-side"),
    ("lpc.quote.such-a-one-with-his-friends", "lpc.term.certificates-letters-of-peace"),
    ("lpc.quote.the-life-and-the-death-shall-both-be-without-end", "lpc.witness.punishment-without-end"),
    ("lpc.quote.very-many-make-moan-over-the-eternal-punishment", "lpc.witness.punishment-without-end"),
    ("lpc.quote.a-respite-from-their-torments", "lpc.witness.punishment-without-end"),
    ("lpc.quote.left-doubtful-a-kind-of-purgatorial-fire", "lpc.witness.judged-on-the-life-lived-here"),
    ("lpc.quote.not-to-purchase-impunity", "lpc.witness.judged-on-the-life-lived-here"),
    ("lpc.quote.all-the-merit-or-demerit-is-acquired-in-this-life", "lpc.witness.judged-on-the-life-lived-here"),
    ("lpc.quote.thank-offerings-for-the-very-good", "lpc.witness.remembered-at-the-altar"),
    ("lpc.quote.remember-me-at-the-lords-altar", "lpc.witness.remembered-at-the-altar"),
    ("lpc.quote.the-mildest-punishment-of-all", "lpc.witness.infants-and-the-sin-of-another"),
    ("lpc.quote.the-mildest-condemnation-of-all", "lpc.witness.infants-and-the-sin-of-another"),
    ("lpc.quote.not-to-be-refused-to-any-one-born-of-man", "lpc.witness.infants-and-the-sin-of-another"),
    ("lpc.quote.not-his-own-sins-but-the-sins-of-another", "lpc.witness.infants-and-the-sin-of-another"),
    ("lpc.quote.no-salvation-out-of-the-church", "lpc.witness.no-salvation-outside-the-church"),
    ("lpc.quote.an-ever-burning-gehenna", "lpc.witness.no-salvation-outside-the-church"),
    ("lpc.quote.an-ever-burning-gehenna", "lpc.witness.punishment-without-end"),
    ("lpc.quote.no-repentance-is-too-late", "lpc.witness.no-salvation-outside-the-church"),
    ("lpc.quote.who-that-has-any-human-feeling-would-refuse-to-forgive-them", "lpc.witness.no-one-may-take-his-own-life"),
    ("lpc.quote.no-place-for-a-healing-penitence", "lpc.witness.no-one-may-take-his-own-life"),
    ("lpc.quote.before-even-a-deacon", "lpc.witness.peace-for-the-dying-penitent"),
    ("lpc.quote.penitents-in-peril-of-sickness-should-be-assisted", "lpc.witness.peace-for-the-dying-penitent"),
    ("lpc.quote.before-even-a-deacon", "lpc.quote.penitents-in-peril-of-sickness-should-be-assisted"),
]


# Edge targets that live in records this script does not emit (the hand-maintained
# doctrinal_witness records, the s26 contested_claim records, the s25 gravity and force
# records and the s22 term records).
EXTERNAL_RELATION_TYPES = {"witness", "contested", "gravity", "force", "term"}


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
        "status": "ready",
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
        "status": "ready",
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
        "status": "ready",
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
        "How we came to treat a recent convert's own election, over his reluctance, as God's own "
        "judgment made visible",
        "Our own deacon Pontius, writing after his bishop had been executed, passed over most of "
        "what he could have said about Cyprian's early years and settled on one fact as enough. "
        "That one fact, he wrote, was proof enough of his good works: by God's judgment and the "
        "people's favour, he was chosen bishop while still a neophyte, and, as people thought, a "
        "novice.\n\n"
        "A neophyte. Newly baptised. Pontius did not soften this -- he pressed it, noting that "
        "Cyprian was still in the first days of his faith, untaught as yet in the life of the "
        "spirit. What we saw in him was not training. It was something we thought we "
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
         "about the death of Cyprian instead",
         "participant asks about modern church governance or ordination procedure, which this "
         "account cannot speak to"],
        [],
        "Derived from Story-Chunks/lpcstory001_election-of-cyprian.md, recast from third-person "
        "report into first-person register. The core quotation ('by the judgment of God and the "
        "favour of the people... a neophyte') is at "
        "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line 27820 (the word 'neophyte') and "
        "the lines through 27823. The phrase 'suffrage of the whole brotherhood' from Ep. LXVII is "
        "present in the same file. The closing sentence's second reference to Cyprian's own words in "
        "Ep. XXXIX is this record's own addition, connecting to "
        "lpc.quote.ancient-venom-against-my-episcopate, and is not in the chunk.",
    )

    emit_story(
        "the-plague-and-the-enemies", 1,
        "Widely Accepted. Tier 1 at the narrative level, Widely Accepted rather than Documented "
        "(Doc_09 SS3). Pontius is a named eyewitness within the horizon, and the epidemic itself is "
        "independently attested -- Cyprian's own De mortalitate was written into it. The confidence "
        "is stepped down one band because the content of the address reaches us only through "
        "Pontius, reconstructing a sermon he heard, in a work written to praise the man who preached "
        "it -- a reported speech inside a biography of praise is not the same evidentiary object as "
        "a letter in the man's own hand. Not Tier 3: there is no miracle and no providential "
        "intervention, and the death-as-completion pattern is absent because nobody dies here.",
        "How our bishop met a plague by teaching us to love even our enemies, and to help "
        "everyone, not only our own",
        "Pontius, writing as a deacon who was there, described the epidemic without any of the "
        "consolation he might have reached for. A dreadful plague broke out, he wrote, and went "
        "from house to house through a frightened city, carrying off countless people every day, "
        "each from his own home.\n\n"
        "What followed was not about the disease. It was about what the city did. People "
        "shuddered and fled from the contagion, and wickedly put out their own people -- "
        "bodies left where they fell, no longer bodies but the corpses of many.\n\n"
        "Against that, our bishop called us together and preached. He began with mercy, and then "
        "went further. There was nothing remarkable, he told us, in caring for our own. Anyone does "
        "that. What would distinguish us was loving our enemies and praying for those persecuting "
        "us, in imitation of a God who makes His sun rise and sends rain to feed the seed, and "
        "shows these kindnesses to strangers as well as to His own. We ought, he said, to live up "
        "to our birth: those who are plainly born of God should not fall short of it.\n\n"
        "And Pontius records what followed: relief given to everyone, not only to those of the "
        "household of faith. The poor among us, who had no money to give, gave labour instead. "
        "Pontius reaches for a comparison and finds it wanting -- more was done, he writes, than is "
        "recorded of Tobias, who gathered up the dead of his own race only.",
        "Whether the persecutors themselves were among those helped is not something Pontius says "
        "one way or the other, and no source outside him describes the relief operation at all. No "
        "pagan Carthaginian of ours left a word about being helped by us during this epidemic.",
        "A modern listener may hear 'love your enemies' as a maxim available anywhere. What is not "
        "available everywhere is the specific setting: said to a frightened congregation, in a city "
        "where the dead were left where they fell, by a bishop who would himself be executed a few "
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
        "Derived from Story-Chunks/lpcstory002_the-plague-and-the-enemies.md, recast into "
        "first-person register. The epidemic description and Cyprian's reported address are in the "
        "Life and Passion of Cyprian by Pontius, in "
        "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, several thousand lines after the "
        "passage lpcstory001 uses.",
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
        "How our bishop added to our presbyters a confessor who had not wanted to survive",
        "Cyprian wrote to us with news that he said belonged to the joy of us all. He was adding a presbyter to "
        "our clergy, and he wanted us to know who the man was.\n"
        "\n"
        "Numidicus had watched a group of us die. He had exhorted them first -- Cyprian says that "
        "by his urging he sent a great number of martyrs ahead of him, killed by stones and by "
        "fire. Among the dead was his own wife. Cyprian's own phrasing about her is "
        "not a slip: Numidicus watched with joy as his wife, standing by his side, was burned "
        "with the others -- or, as Cyprian corrects himself, preserved.\n"
        "\n"
        "Then Numidicus himself: half burned, buried under stones and left for dead. "
        "His daughter came looking for her father's body -- Cyprian says she searched with the "
        "anxious care of love -- and found him alive. Where she searched, the "
        "letter does not say. He was found half dead, pulled out and revived.\n"
        "\n"
        "And Cyprian adds one clause that gives the whole letter its weight. Numidicus, he says, "
        "stayed behind against his will, when the companions he himself had sent ahead went on. He "
        "had not wanted to survive. Cyprian knew this, wrote it down, and gave the reason he "
        "thought it happened: the Lord meant to add him to our clergy.",
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
        ["participant is asking about the lapsed generally rather than about Numidicus specifically "
         "-- ask about Celerinus's letter to Lucian instead, which carries the lapsed question "
         "directly"],
        [],
        "Derived from Story-Chunks/lpcstory003_numidicus.md, recast into first-person register (the "
        "chunk gives Cyprian's letter in the first person; the surrounding narration changes from "
        "'Cyprian writes to the clergy and people of Carthage' to 'Cyprian wrote to us'). 'Half "
        "consumed, overwhelmed with stones' is in "
        "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml.",
    )

    emit_story(
        "hundred-thousand-sesterces", 1,
        "Documented. First-person testimony from Cyprian's own letter, naming its eight recipients, "
        "stating an amount and a mechanism -- named author, exact social location, datable horizon, "
        "and a claim of the most ordinarily verifiable kind. One citation discipline is worth "
        "flagging directly: the ANF edition prints an Argument above the letter, which is "
        "nineteenth-century editorial matter, not Cyprian's own words. This record cites SS3 of the "
        "letter's own body, where Cyprian states the sum in his own voice, rather than the Argument, "
        "which happens to carry the same true figure.",
        "How we sent a hundred thousand sesterces to ransom our captive brethren",
        "Word reached us that our brethren and sisters had been carried off, captive among "
        "barbarians. Cyprian's reply to the eight bishops who told us -- Januarius, Maximus, "
        "Proculus, Victor, Modianus, Nemesianus, Nampulus and Honoratus, whom he names one by one "
        "-- opens without composure: he read their letter, he says, in great grief and not "
        "without tears.\n"
        "\n"
        "The argument he made was not about charity. It was about identity. Quoting Paul, that "
        "all who have been baptized into Christ have put on Christ, he drew the conclusion "
        "directly: Christ is to be seen in our captive brethren, and the one who redeemed us from "
        "death is now to be redeemed from captivity.\n"
        "\n"
        "Then he said what the money was. He sent one hundred thousand sesterces, collected in our "
        "church from the gifts of our clergy and people, for the bishops to hand out there as "
        "carefully as they could. And he thanked them, for being asked "
        "-- for offering us, as he put it, fruitful fields in which to sow the seeds of our "
        "hope.",
        "We do not know whether the ransom worked. Cyprian never wrote again about the outcome, "
        "and the eight bishops' own reply, if there was one, does not survive. The story ends with "
        "the money leaving Carthage.",
        "A modern listener may reach at once for a currency conversion -- how much was that, "
        "really? Our own record licenses none. What it tells plainly is that it was collected from "
        "one congregation's clergy and people for the ransom of captive brethren, and that we do "
        "not know what proportion of anything it represented.",
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
         "source of ours licenses one, and the purchasing-power comparison is contested among "
         "specialists"],
        "Recast into first-person register from Cyprian's own Epistle LIX. \"Hundred thousand "
        "sesterces\" is verified directly at cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, "
        "line 36082, the same line this record's own sources[].locus field cites. The claim_guards "
        "entry bars inventing a modern-currency conversion for the sum, which no source of ours "
        "licenses.",
    )

    emit_story(
        "celerinus-writes-to-lucian", 1,
        "Documented. Tier 1, Documented (Doc_09 SS3). Two letters by named men with exact social locations -- "
        "confessors, one of them writing from prison -- within the horizon, transmitted in the "
        "corpus of the bishop who was arguing against what they did. That last fact is part of the "
        "tier argument: this material survives because Cyprian's own dossier preserved the case "
        "against himself. An attribution discipline matters here specifically: these letters are in "
        "Cyprian's corpus and are not by Cyprian.",
        "How one confessor asked another, not a bishop, to grant peace to women who had fallen",
        "Celerinus was a confessor among us -- he had been imprisoned and had not denied Christ -- "
        "and he wrote to Lucian, another confessor, in prison. He told Lucian of his own "
        "confession. Then he came to his grief: he told Lucian he was in the midst of great "
        "trouble. His sister had sacrificed. He asked Lucian to grant his wish and grieve with "
        "him over her death, a death of the spirit, for in that time of ruin she had fallen away "
        "from Christ.\n"
        "\n"
        "She was not dead. What Celerinus grieved was a death he believed had happened to her soul "
        "-- which is why the letter carries a request. He asked Lucian to intervene, for her and "
        "for two other women, Numeria and Candida, whom Lucian also knew. He made the case for "
        "them: they had repented, and there were works to point to.\n"
        "\n"
        "Lucian's reply came back from the prison, and it granted what was asked. Before it did, "
        "it said what the prison had been like: by the emperor's command they had been sentenced "
        "to die of hunger and thirst, and shut up in two cells to weaken them that way. Then he "
        "wrote that now they had reached the brightness itself. He greeted Numeria and Candida, and named the martyrs on whose authority he "
        "answered. He asked that the two women have peace, once each case had been set before the "
        "bishop and the sin openly confessed. He signed off exhausted, greeting others whose names "
        "he had not written because he was already too tired, and asking them to forgive him.",
        "Celerinus's own sister has no story, and she is the person this one is about. She is "
        "unnamed -- her own brother does not name her. Numeria and Candida are not 'named lapsed "
        "women' either: Celerinus says the opposite of Candida, that she gave gifts for herself "
        "\"that she might not sacrifice\" -- her case is contested, not conceded. None of the three "
        "speaks for herself anywhere in our record.",
        "A modern listener may expect a bishop's authority to be the only channel by which someone "
        "who failed under pressure could be restored. Here one confessor asks another, in prison, "
        "for peace, and the other gives it in the martyrs' name. Yet his own reply says each case "
        "is to be set before the bishop. Cyprian's own dossier keeps both letters rather than "
        "hiding them.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Ep. XX (Celerinus to Lucian) and Ep. XXI (Lucian's reply); "
                   "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 30528-30720",
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
         "said -- do not invent words for any of the three",
         "do not tell Lucian's grant without his own condition, that each case be set before the "
         "bishop and confession made"],
        "Derived from Story-Chunks/lpcstory005_celerinus-writes-to-lucian.md, recast into "
        "first-person register (the letters of Celerinus and Lucian are already first-person; the "
        "surrounding narration is recast). 'Put to death by hunger and thirst' is at "
        "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, line 30706. Both claim_guards "
        "entries turn Usage Guidance lines of the chunk ('the Representative must not resolve the "
        "tension...'; 'not one of these women speaks for herself') into the schema's barred-claim "
        "field.",
    )

    emit_story(
        "the-death-of-cyprian", 1,
        "Widely Accepted. Tier 1 on the core that Pontius and the Acta Proconsularia both attest "
        "(Doc_09 SS3-4). Pontius meets Tier 1's author test: a named deacon with an identifiable "
        "place in the community, within the horizon, with Cyprian on the last night. The Acta is an "
        "early Christian compilation built around the hearing records, its compiler unnamed and its "
        "edition one (Hartel's, in three printings), so it corroborates a named author and does not "
        "carry the author test alone. The details only Pontius gives are marked as his and carry "
        "Contested confidence, or Inferential-Thin where hagiographic convention shapes them. The "
        "two texts differ on who tied the cloths over Cyprian's eyes.",
        "How two early texts tell the death of our great bishop Cyprian, and where they differ",
        "This is how two early texts tell the death of our great bishop. One is by his deacon, "
        "Pontius, who wrote it in the form of a saint's life. The other is the Acta Proconsularia, "
        "an early Christian compilation built around the records of his hearings. Its compiler is "
        "unnamed. Where both texts agree, we say so plainly. Where only one speaks, we say which.\n"
        "\n"
        "The night before the sentence, Cyprian was held in an officer's house. Pontius says that "
        "he and the other friends were with him, as usual. The people stayed outside. "
        "Pontius writes that they kept watch before the officer's door, anxious that nothing "
        "should be done in the night without their knowing. The Acta tells it more "
        "briefly, and it adds one detail: when the whole people of the brethren came there, "
        "Cyprian had the young women guarded, since the whole people had stayed in the street "
        "before the officer's door.\n"
        "\n"
        "In the morning a great crowd went with him. Pontius says he went out walled in on every "
        "side by a mixed crowd. The Acta says that a large crowd gathered at Sextus's place, as "
        "the proconsul Galerius Maximus had ordered.\n"
        "\n"
        "The proconsul read the sentence from a tablet. Pontius reports that it named Cyprian the "
        "standard-bearer of the sect and an enemy of the gods, an example to his own people, and "
        "said that with his blood discipline would begin to be made firm. The "
        "Acta gives the sentence in nearly the same words. On the sentence the two texts are not "
        "independent witnesses. Only the Acta gives Cyprian's answer: he gave thanks to God.\n"
        "\n"
        "Then the crowd of the brethren called out. The Acta gives their words: they asked to be "
        "beheaded with him. It goes on to say that an uproar rose among the brethren because of "
        "this, and a large crowd followed him. Pontius does not quote the "
        "cry. He says the people all wished that the whole congregation might suffer together "
        "and share a like glory, and he calls them blessed because they suffered with their "
        "bishop in words spoken aloud.\n"
        "\n"
        "Only the Acta tells what came before the blow. Cyprian was led out into the field of "
        "Sextus. There he took off his cloak. He knelt on the ground and bowed down in prayer to "
        "the Lord. He took off his tunic and handed it to the deacons. He stood in his linen "
        "garment and began to wait for the executioner. When the executioner came, Cyprian told "
        "his own people to give him twenty-five gold pieces. The brethren laid linen cloths and "
        "hand-cloths before him.\n"
        "\n"
        "Both texts say he covered his own eyes, and they differ on the cloths. Pontius says that "
        "he bound his eyes with his own hands and tried to hurry the executioner. The Acta "
        "says he covered his eyes with his own hand, and that when he could not tie the strips of "
        "cloth himself, the presbyter Julianus and the subdeacon Julianus tied them for him. We do "
        "not choose between the two.\n"
        "\n"
        "Only the Acta tells the burial. So the blessed Cyprian suffered martyrdom. Because the "
        "pagans were curious, his body was laid nearby. By night it was taken up from there with "
        "candles and torches. With prayer and great triumph, it was brought to the grounds of the "
        "procurator Macrobius Candidianus. These lie on the Mappalian road, beside the pools.\n"
        "\n"
        "Pontius adds things the Acta does not mention, and they are his. He says the ground was "
        "level, with trees planted thickly all around, so that it gave a fine view. People who "
        "could not see had climbed into the branches, so that even this was not lacking to him: "
        "as with Zacchaeus, he was gazed at from the trees. He writes that the executioner could "
        "barely grip the blade with the trembling fingers of his failing right hand, until the "
        "hour of glory came and strengthened the centurion's hand with power from above. The "
        "Latin of that sentence can be read two ways. The Acta calls the executioner a spiculator "
        "and says nothing of any strengthening. We tell that part as Pontius's reading.",
        "What cannot be told is what any one person in the crowd made of it, because no spectator "
        "left an account of his own. What the crowd said as a body, the Acta records: Et nos cum "
        "ipso decollemur. Pontius himself points the reader to the Acts, at the end of his account "
        "of the banishment hearing of 257.",
        "A modern listener asking \"did that really happen?\" deserves three things at once. Cyprian "
        "was executed under Valerian and Gallienus on 14 September 258. Two early texts agree on the "
        "core of how it happened. And they disagree on one detail, who tied the cloths over his eyes.",
        conf("B", "verified-direct", "load-bearing", "Widely Accepted",
             "Widely Accepted rather than Documented, because the corroborating text is an early "
             "compilation whose compiler is unnamed, and vendored scholarship argues over how it "
             "relates to Pontius. The details only Pontius gives (the trees, the comparison to "
             "Zacchaeus, the trembling fingers, the hand strengthened from above) carry Contested "
             "confidence, and Inferential-Thin where hagiographic convention shapes them. The two "
             "texts differ on who tied the cloths over Cyprian's eyes. Which clause of CF V7.4's "
             "Tier 3 definition governs when they conflict is an open governance question (Doc_09 "
             "SS8 item 7), and this story does not rest on it."),
        [{"source_id": "lpc.source.pontius-life-and-passion-of-cyprian",
          "locus": "SSSS15-19; cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines "
                   "28161-28303; Latin in "
                   "cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt, lines "
                   "41243-41366",
          "license": "public-domain"},
         {"source_id": "lpc.source.acta-proconsularia-sancti-cypriani",
          "locus": "Acta 2-6, an early compilation with an unnamed compiler, in one edition (Hartel) "
                   "printed three times; "
                   "cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt, lines "
                   "4877-4958, quoted here; the same text in the Hartel volume, lines 41509-41626, "
                   "and in Gebhardt no. XI",
          "license": "public-domain"}],
        2,
        ["participant asks how we understood a life completed",
         "participant asks how Cyprian died, or how his people met his death",
         "participant asks what we believed formation finally produced",
         "conversation reaches the pastoral office or the confessor tension"],
        ["participant wants a transcript of Cyprian's trial -- the Acta is a Christian compilation "
         "built around the hearing records, and is not a court transcript"],
        ["this account must not be presented as historical fact that the executioner's hand was "
         "strengthened from above -- we report only that this is how Pontius told it",
         "the two texts differ on who tied the cloths over Cyprian's eyes -- we state the "
         "difference and do not resolve it"],
        "Derived from Story-Chunks/lpcstory006_the-death-of-cyprian.md, recast into first-person "
        "register. Quotations from Pontius are in "
        "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, lines 28160-28303, and the English "
        "renderings of the Acta are this build's own.",
    )

    emit_story(
        "the-psalms-on-the-wall", 1,
        "Documented. Tier 1, Documented (Doc_09 SS3). Possidius was a bishop in his own right, "
        "Augustine's friend for close to forty years, and -- decisively for the tier -- physically "
        "present: one of those Augustine 'asked of us who were present,' writing 'while we stood by "
        "and watched and prayed.' Like lpcstory006, this is a bishop's death written by an admirer. "
        "The difference is the presence or absence of the genre's own machinery: Pontius supplies a "
        "scriptural typology and a providential intervention, which lpcstory006 marks as his alone; "
        "Possidius supplies sheets of paper on a wall, a request not to be disturbed, and an "
        "inventory of what the dead man did not own. The test applied is CF V7.4's own three Tier 3 "
        "markers, and this account carries none of them.",
        "How the man who taught that even good Christians must repent before death did it himself",
        "Possidius had been Augustine's friend for nearly forty years, and he was in the house.\n\n"
        "He records something Augustine had said often, in private conversation: that even after "
        "baptism, exemplary Christians and priests ought not depart this life without fitting "
        "repentance. Then he records what Augustine did with his own rule. He did it himself in "
        "the last illness of which he died. He had the penitential Psalms of David, which are "
        "very few, copied out, and as he lay sick in bed he looked at the sheets hung on the wall, read "
        "them, and wept freely and constantly.\n\n"
        "About ten days before the end he asked to be left alone -- Possidius says he asked those "
        "of us who were there to let no one in, except when the doctors came to examine him or "
        "when food was brought. The request was "
        "kept. Until that last illness he had not stopped preaching.\n\n"
        "And the end, in Possidius's own first person: his body whole, his sight and hearing "
        "sound, he slept with his fathers, as Scripture says, well nourished in a good old age, "
        "while we stood by, watching and praying. He made no "
        "will, because he had nothing to make one from. He ordered that the church's library and "
        "all its books be carefully preserved for those who came after. The city was under siege "
        "by the Vandals while this happened.",
        "Possidius is the only witness to the last weeks -- the psalms, the request, the ten days. "
        "The death itself is corroborated from outside Hippo, by its date and the siege around it, "
        "but what no second source gives is the interior of the sickroom. No one who fled Hippo "
        "wrote down what leaving the city was like, either.",
        "A modern listener may expect this told as a serene death. Possidius's own text does not "
        "support serenity: a man who taught repentance wept freely and constantly for days, "
        "looking at psalms about sin -- the disproportion, if it looks like one, is the formation "
        "content, not an embarrassment to smooth over.",
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
        "Derived from Story-Chunks/lpcstory007_the-psalms-on-the-wall.md, recast into first-person "
        "register. 'Shortest penitential Psalms' is at "
        "cic/texts/possidius_vita-augustini_weiskotten1919.txt, line 4925.",
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
        "Our bishop, chosen while still new to the faith, over his own reluctance. During a plague "
        "he taught us to love even our enemies. He was put to death under Valerian.",
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
        "Our bishop at Hippo. The people seized him and brought him to be made a presbyter while he "
        "wept. Later "
        "they pressed him into the bishop's office over his own refusal. He spent his last days "
        "weeping over psalms of penitence, while an army lay outside the walls.",
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
        "Our bishop's own deacon. He went with him into exile, and after the execution he wrote "
        "the account of his life and death.",
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
        "the bishop of Calama who had been Augustine's friend for almost forty years, and who "
        "stood by him and prayed as he died",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.possidius-vita-augustini-weiskotten1919",
          "locus": "the whole Vita Augustini, and its own closing first-person account of "
                   "Augustine's own last illness and death",
          "license": "public-domain"}],
        "The principal source for Phase Two's one built story, and its only witness to the sickroom "
        "(Prosper's Chronicon corroborates the death, its date and the siege, and adds that he was "
        "still answering Julian, but says nothing of the sickroom), and the source of "
        "lpc.quote.clamour-and-tears -- the mirror of Pontius's own role for Phase One, a friendly "
        "rather than hostile mediating eyewitness whose own presence in the room (rather than only "
        "his own social location) is what the Tier Justification for "
        "lpc.story.the-psalms-on-the-wall rests its Tier 1 finding on.",
    )

    emit_figure(
        "numidicus",
        [{"name": "Numidicus, our presbyter", "tag": "in-world"},
         {"name": "Numidicus of Carthage (fl. mid-3rd century)", "tag": "scholarly"}],
        {"display": "exhorted a group of Christians to martyrdom under persecution, among them his "
                    "own wife, who died with them; himself left half-consumed by fire and "
                    "overwhelmed with stones, found half dead by his own daughter and revived; "
                    "added by Cyprian afterward to the presbyters of Carthage, though he had not "
                    "wanted to survive (Cyprian, Ep. XXXIV; lpc.story.numidicus)"},
        True,
        "a man who watched his own wife die with those he had exhorted to martyrdom, was himself "
        "left for dead, and did not want to have survived",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Ep. XXXIV, the whole letter", "license": "public-domain"}],
        "The central named subject of lpc.story.numidicus, and this world's own clearest single "
        "case of a man added to the presbyterate on the strength of what he had endured rather "
        "than what he had studied -- the same criterion Doc_04 makes a Primary gravity "
        "(sacramental and ordination validity) applied here to one identifiable person in public. "
        "His own wife and daughter are visible in the same letter and never audible (Doc_09 SS7 "
        "item 4); neither is named, so neither is built as a figure of her own here.",
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
        "A confessor who wrote to another confessor in prison. He wept for his sister, who had "
        "sacrificed, and asked him to help restore her.",
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
                    "thirst, who replied to Celerinus from prison, granting peace to Numeria and "
                    "Candida once their case was set before the bishop (Ep. XXI; "
                    "lpc.story.celerinus-writes-to-lucian)"},
        True,
        "A confessor who answered from a prison cell. He and others there had been ordered to die "
        "of hunger and thirst. He sent peace to Numeria and Candida, two women he knew well, once "
        "each case was set before the bishop.",
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
# QUOTES (5)
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
        "None of us sets himself up as a bishop over other bishops, and none of us uses a tyrant's "
        "terror to force a colleague into obedience. Every bishop has his own right to judge, in "
        "keeping with the freedom and power allowed to him. He can no more be judged by another "
        "bishop than he himself can judge another. Instead, let us all wait for the judgment of our "
        "Lord Jesus Christ. He is the only one who has the power both to place us in the government "
        "of His Church and to judge how we conduct ourselves there.",
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
        "For they have not forgotten their conspiracy. They still carry that old venom against my "
        "office as bishop, which means against your suffrage and against God's judgment. They are "
        "renewing their old attack on me, and once again they are starting their sacrilegious "
        "plots with their usual cunning.",
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
        "I grieve, brothers, I grieve with you. My own integrity and my personal soundness do not "
        "lure me into soothing my griefs. That is because it is the shepherd who is wounded most "
        "deeply when his flock is wounded. I hold each one of you close to my heart, and I share the "
        "heavy burden of sorrow and mourning. I wail with those who wail, I weep with those who "
        "weep...",
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
        "The Catholics already knew the life and teaching of the holy Augustine, and they seized "
        "him. He was standing there among the people, feeling safe and unaware of what was about to "
        "happen... So they seized him and, as is the custom in such cases, brought him to the bishop "
        "to be ordained. They did this because all of them, with one accord, wanted it done and "
        "carried through. They demanded it with great eagerness and loud shouting, while he wept "
        "freely.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The vendored Weiskotten scan carries a single OCR artifact inside this quotation -- "
             "'ancf' for 'and' -- reproduced here exactly as the scan gives it (matching this "
             "record's own text against the raw file precisely, per this step's own discipline), not "
             "silently corrected; modern_rendering gives the plain sense ('they demanded it...') "
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
        "But now I imagine that no one has come here except those who want to hear. So I am not "
        "speaking to deaf hearts, or to minds that will look down on the word. Instead, this longing "
        "expectation of yours is a prayer for me.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "Independently re-located this session by direct keyword search of the vendored file "
             "-- corrects this script's own earlier draft, which had claimed the same search "
             "'did not locate' this quote. It does, in fact, occur verbatim at the cited line. "
             "The earlier claim is not repeated in this record; it is disclosed instead in this "
             "script's own docstring (QUOTE SET, item 7), as a fabrication-class error caught and "
             "corrected before commit, not carried forward."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon I [LI, Benedictine], 'Of the agreement of the evangelists Matthew and "
                   "Luke in the generations of the Lord' -- delivered some time after the Nativity "
                   "festival's own matins, not at the matins itself; the sermon's own opening "
                   "recalls that at matins Augustine had put off the question he now resolves (\"it "
                   "was in the matins of the festival of the Lord's Nativity, that I put off the "
                   "question which I had proposed for resolution\"); independently re-located this "
                   "session at "
                   "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, line 9398",
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
        "paragraph, its final named image: 'A preacher naming, to the very people gathered in front "
        "of him, that their own waiting is itself a kind of prayer for him.' This is the fifth of "
        "the Permanent Prompt's seven candidate images to be built as a quote record -- the other "
        "two (the certificate/wide-door contrast and the two-answers-on-baptism contrast) remain "
        "synthesized prose without a single quotable sentence, disclosed as such in this script's "
        "own docstring rather than built. Sermon I's own delivery date is undated within this "
        "world's own construction record beyond the sermon's own words placing it after the Nativity "
        "festival's matins, at which Augustine had deferred this same question. No further narrowing "
        "of the actual delivery date is attempted here.",
    )


# ===========================================================================
# SERMON QUOTES (18) -- Augustine's sermons on selected lessons, one per passage.
# ===========================================================================

def build_sermon_quotes() -> None:
    emit_quote(
        "ye-belong-to-my-care",
        "Ye are in communion with the members of the Apostles, ye are in communion with the "
        "memories of the Holy Martyrs, who are spread over the whole world, and ye belong to "
        "my cure, that I may render a good account of you. Now my whole account, what it is ye "
        "know. “Lord, Thou knowest that I have spoken, Thou knowest that I have not kept "
        "silence, Thou knowest in what spirit I have spoken, Thou knowest that I have wept "
        "before Thee, when I spake, and was not heard.”",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'my care' as a professional's caseload. Augustine ties it "
        "to an account he must give: his hearers belong to his care so that he may give a good "
        "account of them, and the account he names is that he spoke, did not keep silent, and "
        "wept before God when he was not heard. 'Shrines' are the martyrs' memorial places; "
        "the English 'memories' hides that.",
        "You share communion with the members of the Apostles. You share communion with the "
        "shrines of the holy martyrs, who are spread over the whole world. And you belong to my "
        "care, "
        "so that I may give a good account of you. You know what my whole account is. “Lord, "
        "You know that I have spoken. You know that I have not kept silent. You know in what "
        "spirit I have spoken. You know that I have wept before You when I spoke and was not "
        "heard.”",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. modern_rendering follows the "
             "Latin of PL 38 where the English misleads: 'memories of the Holy Martyrs' "
             "renders memoriis, which in African Latin of this period names a martyr's shrine "
             "or memorial chapel, and 'cure' renders curam, which here means care or charge."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 87 (NPNF numbering; Maurist 137), section 15; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 20796-20797; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 53418-53424 "
                    "(the sermon starts at line 52829)",
          "license": "public-domain"}],
        1,
        ["participant asks what a bishop owed the people in his care",
         "participant asks what it meant for a bishop to give an account of his hearers",
         "participant asks how a bishop spoke of his own answerability to the people in front "
         "of him"],
        ["participant wants a bishop's grief for a wounded flock rather than his account of it "
         "-- lpc.quote.shepherd-wounded-in-the-flock gives that"],
        ["The passage does not give a date, a place or an occasion for the sermon; do not "
         "invent one.",
         "The sentence before it in the same section, which calls the hearers a Catholic "
         "people not divided from unity, is not in the passage and must not be supplied as if "
         "quoted.",
         "The closing prayer is Augustine's own wording and must not be presented as a "
         "Scripture quotation."],
        "Augustine, Sermon 87 in the NPNF numbering (137 in the Maurist numbering), section "
        "15. English in the NPNF translation at "
        "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, lines "
        "20796-20797. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines "
        "53418-53424 (OCR text; the sermon starts at line 52829). The first sentence of "
        "section 15 and the Ezekiel watchman argument that follows the passage in the same "
        "paragraph are left out. In the English, 'cure' is the older sense of 'care' (Latin "
        "curam), and 'memories' translates memoriis, which names martyrs' shrines in the Latin "
        "of this period. The Latin has the bishop's plural, 'our care' and 'we may render'; "
        "the English has the singular. The sermon carries the gravity "
        "lpc.gravity.pastoral-office-flock-keeping in the bishop's own voice.",
    )

    emit_quote(
        "stewards-and-future-bishops",
        "For how many are there among this people who shall some day be dispensers! I too was "
        "once where ye now are; and I who am seen now to be measuring out to my fellowservants "
        "their food from this higher place, a few years since in a lower place was receiving "
        "food with my fellow-servants. I am speaking now a Bishop to lay-men; but I know that "
        "in speaking to them I am speaking to many who will some day be bishops also.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'dispensers' as machines or pharmacists. The Latin word, "
        "dispensatores, means stewards who hand out the household's rations, and Augustine "
        "uses it of the work of the office. He sets the distance between bishop and hearers as "
        "small: he once sat where they sit, and he says he is speaking to many who will one "
        "day be bishops.",
        "For how many among this people will one day be stewards! I too was once where you are "
        "now. Now I am seen measuring out food to my fellow servants from this higher place. A "
        "few years ago I was in a lower place, receiving food with my fellow servants. I am "
        "speaking now as a bishop to lay people. But I know that I am speaking to many who "
        "will one day be bishops too.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 51 (NPNF numbering; Maurist 101), section 4; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 16779-16780; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 42457-42464 "
                    "(the sermon starts at line 42253)",
          "license": "public-domain"}],
        2,
        ["participant asks whether a bishop came from the ordinary people he led",
         "participant asks how a bishop described the work of feeding his hearers",
         "participant asks how Augustine saw the lay people in front of him"],
        ["participant asks how Augustine himself came to be ordained -- "
         "lpc.quote.clamour-and-tears is Possidius's account of that"],
        ["The passage does not say when or how Augustine was ordained; 'a few years since' is "
         "his own phrase and the file gives no date for the sermon, so nothing about his "
         "ordination may be drawn from it.",
         "The passage does not describe an ordination rite and must not be used to show one."],
        "Augustine, Sermon 51 in the NPNF numbering (101 in the Maurist numbering), section 4. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "lines 16779-16780. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, "
        "lines 42457-42464 (OCR text; the sermon starts at line 42253). The passage opens in "
        "the middle of an argument. In the English, 'dispensers' translates dispensatores, the "
        "stewards of the household who give out rations; 'from this higher place' is the "
        "raised seat from which he speaks. The Latin has the plural, 'we were' and 'we "
        "received'; the English has the singular. 'Bishop to lay-men' is exact. The sermon "
        "carries the gravity lpc.gravity.pastoral-office-flock-keeping.",
    )

    emit_quote(
        "good-works-the-comfort-of-our-dangers",
        "But why do we, who are unwilling to be despised by you, speak to you, except that we "
        "may have joy of your good conversation? Let your good works be the solace of our "
        "perils. Live well, that ye may not die ill.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'good conversation' as pleasant talk. The Latin, bonis "
        "moribus, means a good way of life. Augustine says why he speaks to his hearers at "
        "all: for joy in how they live. He asks their good works as comfort in the dangers of "
        "his office, and does not say what those dangers are.",
        "We do not want you to look down on us. Why do we speak to you, except to take joy "
        "in your good way of life? Let your good works comfort us in our dangers. Live well, "
        "so that you do not die badly.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. modern_rendering follows the "
             "Latin of PL 38 where the English misleads: 'good conversation' renders bonis "
             "moribus, a good way of life. 'Despised' (sperni) is rendered 'look down on' for "
             "plainness."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 52 (NPNF numbering; Maurist 102), section 1; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 16873-16874; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 42699-42703 "
                    "(the sermon starts at line 42681)",
          "license": "public-domain"}],
        2,
        ["participant asks why a bishop preached to his people at all",
         "participant asks what a bishop hoped for from the lives of his hearers",
         "participant asks what a congregation owed the one who spoke to it"],
        ["participant wants the bond of a congregation's waiting on a preacher -- "
         "lpc.quote.longing-expectation-is-a-prayer-for-me gives that"],
        ["The passage does not say what the dangers of the office are; do not add a gloss.",
         "The sentences before it in the same section, about the Lord's words 'He that "
         "despiseth you, despiseth Me' and standing in the Apostles' place, are not in the "
         "passage and must not be supplied as if quoted."],
        "Augustine, Sermon 52 in the NPNF numbering (102 in the Maurist numbering), section 1. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "lines 16873-16874. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, "
        "lines 42699-42703 (OCR text; the sermon starts at line 42681). The passage opens in "
        "the middle of an argument. The plural 'we' is the bishop speaking for his office and "
        "the plural 'you' is the congregation. In the Latin, pericula nostra are dangers; the "
        "paragraph goes on to dying well, and no gloss on the dangers is given. The sermon "
        "carries the gravity lpc.gravity.pastoral-office-flock-keeping.",
    )

    emit_quote(
        "bind-him-justly",
        "Thou hast begun to hold thy brother for a publican; “thou bindest him on earth;” but "
        "see that thou bind him justly. For unjust bonds justice doth burst asunder. But when "
        "thou hast corrected, and been “reconciled to thy brother,” thou hast “loosed him on "
        "earth.” And when “thou shalt have loosed him on earth, he shall be loosed in heaven "
        "also.”",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'bindest him on earth' as a church court, and 'publican' "
        "as a pub-keeper. Augustine is reading Matthew 18 about one believer correcting a "
        "brother: the Latin publicanum is a tax collector, and the binding must be just, since "
        "justice breaks unjust chains. When the brother is corrected and peace is made, the "
        "binding is undone.",
        "You have begun to treat your brother as a tax collector. You bind him on earth. But "
        "see that you bind him justly. For justice bursts unjust chains. But once you have "
        "corrected him and made peace with your brother, you have loosed him on earth. And "
        "when you have loosed him on earth, he will be loosed in heaven too.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. In it, 'reconciled to thy "
             "brother' stands in quotation marks as if it were Scripture. The Latin, "
             "concordaveris cum fratre tuo, is Augustine's own wording, and modern_rendering "
             "drops the marks."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 32 (NPNF numbering; Maurist 82), section 7; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "line 14225; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 35544-35549 "
                    "(the sermon starts at line 35316)",
          "license": "public-domain"}],
        2,
        ["participant asks how a wrong done by one believer to another was handled",
         "participant asks what binding and loosing meant when a brother was corrected",
         "participant asks whether a brother who had been bound could be loosed again"],
        ["participant asks how lapsed Christians were brought back after persecution -- "
         "lpc.term.reconciliation-penitential-discipline and the Cyprian-phase material give "
         "that"],
        ["The passage does not describe formal public penance, excommunication or a bishop "
         "readmitting a penitent, and must not be used as evidence that the sermons show any "
         "of them.",
         "It needs the Matthew 18 steps Augustine quotes just before it; 'hold thy brother for "
         "a publican' refers to them and must not be read without them."],
        "Augustine, Sermon 32 in the NPNF numbering (82 in the Maurist numbering), section 7. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "line 14225. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines "
        "35544-35549 (OCR text; the sermon starts at line 35316). Augustine is reading Matthew "
        "18:15-18; the steps of Matthew 18:17 are quoted at lines 14218-14219 and the sentence "
        "after the passage is left out. In the Latin, ligas and solvisti are bind and loose, "
        "vincula are chains, and publicanum is a tax collector. The sermon carries the gravity "
        "lpc.gravity.penitential-discipline.",
    )

    emit_quote(
        "reprove-and-forgive-the-surgeons-knife",
        "Let us reprove with words, and if need be with scourges; but let us withal forgive "
        "the sin, and cast away the remembrance of it from the heart. For therefore did the "
        "Lord add, “from your hearts,” that though through affection discipline be exercised, "
        "gentleness might not depart out of the heart. For what is so kind and gentle as the "
        "surgeon with his knife?",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'scourges' as a church penalty. In the sermon they belong "
        "to an illustration about unruly boys who beg to be let off a beating, which Augustine "
        "then applies to brethren. His point is that correction is to be given out of love, "
        "with the sin forgiven in the heart, as a surgeon cuts out of kindness.",
        "Let us rebuke with words, and with blows if need be. But let us also forgive the sin "
        "and cast the fault out of our hearts. The Lord added “from your hearts” for this "
        "reason: when discipline is given out of love, gentleness must not leave the heart. "
        "For what "
        "is as kind and gentle as a surgeon with his knife?",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. modern_rendering follows the "
             "Latin of PL 38 where the English departs from it: 'cast away the remembrance of "
             "it from the heart' renders culpam de corde abjiciamus, cast the fault out of the "
             "heart, and the Latin does not ask for forgetting; 'though through affection' "
             "renders si per charitatem, when discipline is given out of love."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 33 (NPNF numbering; Maurist 83), section 8; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "line 14444; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 36195-36201 "
                    "(the sermon starts at line 35885)",
          "license": "public-domain"}],
        2,
        ["participant asks how correction was meant to feel to the one who gave it",
         "participant asks how someone could reprove a brother and still forgive him",
         "participant asks what discipline given out of love looked like"],
        ["participant asks how one believer treated a brother who would not listen -- "
         "lpc.quote.bind-him-justly gives the Matthew 18 reading"],
        ["The blows belong to an illustration about unruly boys and must not be read as a "
         "church penalty.",
         "The passage does not describe formal public penance, excommunication or how "
         "discipline was carried out in the church, and must not be used as evidence of any "
         "of them."],
        "Augustine, Sermon 33 in the NPNF numbering (83 in the Maurist numbering), section 8. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "line 14444. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines "
        "36195-36201 (OCR text; the sermon starts at line 35885). The passage begins inside "
        "line 14444. The illustration about unruly boys is at lines 14437-14443. The "
        "NPNF title prints Matthew 17:21 where the Latin witnesses read Matthew 18; this does "
        "not touch the passage. In the Latin, verberibus are blows, pium is one word for kind "
        "and gentle, and medicus ferens ferramentum is a doctor carrying his blade. The sermon "
        "carries the gravity lpc.gravity.penitential-discipline.",
    )

    emit_quote(
        "peter-the-sick-man-and-the-physician",
        "Peter then was at that time the invalid, and the Lord the Physician. The former "
        "declared that he had strength, when he had not; but the Lord touching the pulse of "
        "his heart, declared that he should deny Him thrice. And so it came to pass, as the "
        "Physician foretold, not as the sick presumed. Therefore, after His resurrection the "
        "Lord questioned him, not as being ignorant with what a heart he would confess the "
        "love of Christ, but that he might by a threefold confession of love, efface the "
        "threefold denial of fear.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'invalid' as lasting disability. The Latin infirmus means "
        "weak or sick: Peter is the sick man and the Lord the doctor, who feels the pulse of "
        "his heart. After the resurrection the Lord asks Peter three times, so that a "
        "threefold confession of love wipes out the threefold denial made in fear.",
        "At that time Peter was the sick man, and the Lord was the doctor. Peter said he had "
        "strength when he did not. But the Lord felt the pulse of his heart and said Peter "
        "would deny Him three times. And it happened as the doctor foretold, not as the sick "
        "man presumed. So after His resurrection the Lord questioned him. It was not that He "
        "did not know the heart with which Peter would confess his love for Christ. He asked "
        "so that Peter could confess his love three times. In this way he would wipe out the "
        "three denials he made in fear.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 87 (NPNF numbering; Maurist 137), section 3; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 20614-20615; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 52934-52947 "
                    "(the sermon starts at line 52829)",
          "license": "public-domain"}],
        2,
        ["participant asks how a man who had failed was put right again",
         "participant asks how Peter's denial was answered",
         "participant asks why the Lord asked Peter three times whether he loved Him"],
        ["participant asks how lapsed Christians were brought back after persecution -- "
         "lpc.term.the-lapsed and the Cyprian-phase material give that"],
        ["The passage does not say that Peter was restored to feed the flock; that comes in "
         "section 4 of the sermon and must not be supplied here.",
         "The passage does not describe a penitential rite or a bishop restoring a penitent."],
        "Augustine, Sermon 87 in the NPNF numbering (137 in the Maurist numbering), section 3. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "lines 20614-20615. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, "
        "lines 52934-52947 (OCR text; the sermon starts at line 52829). The passage reads John "
        "21 against the denial in Luke 22; those references are notes outside the passage, at "
        "lines 20610 and 20613. In the Latin, tangens venam cordis ejus is touching the pulse "
        "of his heart, and deleret trinam negationem timoris is wiping out the threefold "
        "denial made out of fear. The sermon carries the gravity "
        "lpc.gravity.penitential-discipline.",
    )

    emit_quote(
        "one-good-shepherd-not-many",
        "It was then as impressing on good shepherds this unity, that our Lord was unwilling "
        "to mention many shepherds. For it is not, as I have said already, that Peter was not "
        "a good shepherd, and Paul, the rest of the Apostles, and the holy Bishops who were "
        "after them, and blessed Cyprian. All these were good shepherds; and notwithstanding "
        "to good shepherds, He commended not good shepherds, but a good Shepherd.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear a roll of approved authorities. Augustine names Peter, "
        "Paul, the other Apostles, the holy bishops after them, and blessed Cyprian, and says "
        "all of them were good shepherds. His point is unity: even so, the Lord spoke of one "
        "good Shepherd and not of many.",
        "So it was to press this unity on good shepherds that our Lord would not name many "
        "shepherds. As I have said already, it is not that Peter was not a good shepherd. The "
        "same holds for Paul, the rest of the Apostles, the holy bishops who came after them, "
        "and blessed Cyprian. All these were good shepherds. And yet to good shepherds He "
        "commended not good shepherds, but a good Shepherd.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 88 (NPNF numbering; Maurist 138), section 3; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "line 20848; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 53554-53561 "
                    "(the sermon starts at line 53471)",
          "license": "public-domain"}],
        2,
        ["participant asks how Augustine spoke of Cyprian",
         "participant asks why the Lord spoke of one Shepherd and not of many",
         "participant asks how good shepherds were held in one unity"],
        ["participant asks whether one bishop could overrule another -- "
         "lpc.quote.bishop-of-bishops gives Cyprian's own words"],
        ["The passage names Cyprian only among the good shepherds; it does not say anything "
         "about rebaptism or any dispute between bishops, and must not be used to show that "
         "Augustine and Cyprian agreed or differed on practice.",
         "The passage does not show bishops disagreeing with bishops.",
         "It depends on John 10:14, 'I am the good Shepherd', which the next sentence quotes "
         "and the passage leaves out."],
        "Augustine, Sermon 88 in the NPNF numbering (138 in the Maurist numbering), section 3. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "line 20848. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines "
        "53554-53561 (OCR text; the sermon starts at line 53471). An editor's footnote about "
        "the Carthage conference sits at line 20847, just before the passage, and is not part "
        "of it. 'Blessed Cyprian' translates beatusque Cyprianus in the Latin. Cyprian is "
        "named in running text in only two places in these sermons, lines 20827 and 20848, "
        "both in this sermon. The sermon carries the gravity "
        "lpc.gravity.collegial-communion-preserved in its congregational form.",
    )

    emit_quote(
        "apart-in-heart-united-in-body",
        "The Winnower will come, who shall divide the bad from the good. There will then be a "
        "bodily separation too, which a spiritual separation now precedes. In heart be always "
        "separated from the bad, in body be united with them for a time, only with caution. "
        "Yet be not negligent in correcting those who belong to you, who in any way appertain "
        "to your charge, by admonition, or instruction, by exhortation, or by threats.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear this as permission to put up with wrongdoing, or as a call "
        "to leave. Augustine tells his hearers to stay in the one Church and bear with the bad "
        "until the Winnower comes: apart from them in heart, joined to them in body, with "
        "caution. They are still to correct those in their care.",
        "The Winnower will come and divide the bad from the good. Then there will be a bodily "
        "separation too. A separation in spirit comes before it now. In heart, always keep "
        "apart from the bad. In body, stay joined with them for a time, but with caution. Yet "
        "do not neglect to correct your own people, those who in any way are in your care. Do "
        "it by warning, by teaching, by urging, or by threats.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 38 (NPNF numbering; Maurist 88), section 19; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 15138-15139; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 38364-38370 "
                    "(the sermon starts at line 37663)",
          "license": "public-domain"}],
        2,
        ["participant asks whether one should leave a church that holds bad members",
         "participant asks how to live in one communion with wrongdoers",
         "participant asks who was responsible for correcting those in their charge"],
        ["participant asks about bishops and their communion with one another -- "
         "lpc.quote.bishop-of-bishops gives Cyprian's own words"],
        ["The passage is addressed to lay hearers about bad members inside the Church; it does "
         "not show bishops disagreeing with bishops and must not be used as evidence of a "
         "dispute among bishops.",
         "The threshing-floor image in the sentence just before it is not in the passage and "
         "must not be supplied as if quoted."],
        "Augustine, Sermon 38 in the NPNF numbering (88 in the Maurist numbering), section 19. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "lines 15138-15139. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, "
        "lines 38364-38370 (OCR text; the sermon starts at line 37663). The passage begins at "
        "the end of line 15138. A Scripture reference note follows at line 15141, outside the "
        "passage. In the Latin, ventilator is the winnower, and ad curam vestram is the same "
        "word for care that the bishop uses of his own flock; here it is used of those in the hearers' "
        "own charge. The sermon carries the gravity "
        "lpc.gravity.collegial-communion-preserved in its congregational form, the "
        "stay-in-one-Church side.",
    )

    emit_quote(
        "going-out-without-violating-unity",
        "Thou art displeased at a man’s sin, thou hast not “touched the unclean thing.” Thou "
        "hast reproved, rebuked, admonished him, hast administered, if the case required it, a "
        "suitable discipline, and such as doth not violate unity; then thou hast “gone out "
        "from thence.”",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'gone out from thence' as leaving the Church. Augustine "
        "teaches the opposite: to go out from the wicked is to reprove, rebuke and warn them, "
        "and to use whatever discipline the case needs, in a way that does not break unity. "
        "The discipline he means is fitted to each person's rank and condition.",
        "If someone's sin displeases you, you have not touched the unclean thing. You have "
        "reproved him, rebuked him and warned him. If the case required it, you have used "
        "fitting discipline, of a kind that does not break unity. Then you have gone out from "
        "there.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 38 (NPNF numbering; Maurist 88), section 23; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "line 15208; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 38536-38542 "
                    "(the sermon starts at line 37663)",
          "license": "public-domain"}],
        2,
        ["participant asks what it meant to separate from the wicked without leaving the "
         "Church",
         "participant asks how a hearer could rebuke a sinner and keep the peace",
         "participant asks what discipline that does not break unity looked like"],
        ["participant asks about bishops and their communion with one another -- "
         "lpc.quote.bishop-of-bishops gives Cyprian's own words"],
        ["The discipline in this passage is tied to rank: the sentence before it says going "
         "out is done 'according to each one's grade and condition' (NPNF line 15205). The "
         "passage does not give every hearer the same power to discipline, and must not be "
         "read as if it did.",
         "The passage quotes 'go ye out from thence' without its source and without the "
         "reading it answers; it does not name the Donatists, and the Isaiah context must not "
         "be omitted when it is told.",
         "The passage does not show bishops disagreeing with bishops."],
        "Augustine, Sermon 38 in the NPNF numbering (88 in the Maurist numbering), section 23. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "line 15208. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines "
        "38536-38542 (OCR text; the sermon starts at line 37663). The sentences before the "
        "passage, at lines 15204-15207, quote 'Depart ye, go ye out from thence, and touch "
        "not the unclean thing' (Isaiah), say 'we' understand the departure spiritually and "
        "'they' bodily, and define going out as doing what belongs to rebuking the wicked as "
        "far as can be done, according to each one's grade and condition, with the maintenance "
        "of peace. The translator's Latin gloss, Persona, sits inside the last of them. In the "
        "Latin, congruam disciplinam is a fitting discipline and quae unitatem non violet is "
        "'that does not break unity'. The sermon carries the gravity "
        "lpc.gravity.collegial-communion-preserved in its congregational form.",
    )

    emit_quote(
        "the-branch-cut-from-the-vine",
        "For the visible form of the branch may exist even when separated from the vine; but "
        "the invisible life of the root cannot be had, but in the vine. Wherefore the bodily "
        "sacraments, which even they who are separated from the Unity of Christ’s Body bear "
        "and celebrate, may give “the form of godliness;” but the invisible and spiritual "
        "power of godliness cannot in any wise be in them, just as sensation does not "
        "accompany a man’s limb, when it is amputated from the body.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'schismatic sacraments are empty', which is close to the "
        "Donatist position Augustine is arguing against. His claim in the same section is "
        "narrower. The washing given outside the Church's unity is not repeated when a person "
        "comes in; what comes only inside is the unity of the Spirit and the life of "
        "godliness. A branch cut from the vine keeps its shape but not its life.",
        "The visible form of a branch can exist even when it is separated from the vine. But "
        "the unseen life of the root can only be had in the vine. So the bodily sacraments can "
        "give “the form of godliness.” Even those who are separated from the unity of Christ’s "
        "Body carry and celebrate them. But the unseen, spiritual power of godliness cannot be "
        "in them at all. In the same way, feeling does not stay with a person's limb when it "
        "is cut off from the body.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 21 (NPNF numbering; Maurist 71), section 32; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 12936-12937; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 32254-32262 "
                    "(the sermon starts at line 30996)",
          "license": "public-domain"}],
        2,
        ["participant asks what was missing from a baptism given outside the Church",
         "participant asks what a baptism given outside the Church lacked, if it was not given "
         "again",
         "participant asks what Augustine meant by the form of godliness without its power"],
        ["participant asks how Cyprian and Augustine gave opposite answers on baptism outside "
         "the Church -- lpc.demo.font-twice-answered gives that"],
        ["This passage must be paired with the sentence at NPNF line 12932: for those baptized "
         "among schismatics or heretics, 'the washing of the flesh is not repeated in their "
         "case'. Without it the passage can be heard as saying the rite outside is void, which "
         "it does not say.",
         "The passage says 'form' and 'power' and does not use the word valid; 'validity' is "
         "the project's term and must not be put in Augustine's mouth.",
         "The sermon does not show a formal ordination or a dispute between bishops."],
        "Augustine, Sermon 21 in the NPNF numbering (71 in the Maurist numbering), section 32. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "lines 12936-12937. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, "
        "lines 32254-32262 (OCR text; the sermon starts at line 30996). 'Wherefore' points "
        "back to the sentence at lines 12926-12932 about baptisms among schismatics and "
        "heretics. That sentence and the next read: 'the washing of the flesh is not repeated in their "
        "case. For \"this form of godliness\" was not wanting to them even when they were "
        "without; but there is added to them \"the Unity of the Spirit in the bond of peace,\" "
        "which cannot be given but within.' Translators' notes break the first of them, and another "
        "sentence and a note stand between them and the passage, so they are not part of it. In the Latin, forma pietatis and virtus pietatis are the form and the "
        "power of godliness (2 Timothy 3:5), and corporalia Sacramenta are the bodily "
        "sacraments. 'In them' (in eis) could mean the separated people or the sacraments, and "
        "both the English and the rendering keep that open. The sermon carries the gravity "
        "lpc.gravity.sacramental-ordination-validity.",
    )

    emit_quote(
        "pardon-through-a-wicked-clergyman",
        "And so a word is spoken against the Holy Spirit, when men never come from the "
        "dispersion to the congregation which has received the Holy Spirit for the remission "
        "of sins. Unto which congregation if any come without hypocrisy, though it be through "
        "the ministry of a wicked clergyman, a reprobate and a hypocrite, so he be a Catholic "
        "minister, he shall receive remission of sins in this Holy Spirit.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'Catholic' as Roman Catholic. Here it means the Church "
        "held together in communion across the world, in contrast to the scattered. Augustine "
        "says a person who comes to that gathering with a heart that is not false receives "
        "forgiveness of sins in the Holy Spirit, even through a wicked cleric, so long as the "
        "minister is a Catholic one.",
        "So a word is spoken against the Holy Spirit when people never come in from the "
        "scattering. They never come to the gathering that has received the Holy Spirit for "
        "the forgiveness of sins. Someone may come to that gathering without pretense. He may "
        "even come through a wicked cleric, a worthless man and a hypocrite, who is still a "
        "Catholic minister. That person will receive forgiveness of sins in this Holy Spirit.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. modern_rendering follows the "
             "Latin of PL 38 where the English departs from it: 'through the ministry of a "
             "wicked clergyman' renders per malum clericum, through a bad cleric, and "
             "'ministry' is the translator's addition; 'so he be a Catholic minister' renders "
             "sed tamen catholicum ministrum, a concession inside the description, not a "
             "condition set beside it."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 21 (NPNF numbering; Maurist 71), section 37; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 13008-13009; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 32485-32492 "
                    "(the sermon starts at line 30996)",
          "license": "public-domain"}],
        2,
        ["participant asks whether a wicked minister could still give forgiveness",
         "participant asks whether the worth of the minister decided what the people received",
         "participant asks what it meant to come to the Church without pretense"],
        ["participant asks what was missing from a baptism given outside the Church -- "
         "lpc.quote.the-branch-cut-from-the-vine gives that"],
        ["'Catholic' in this passage must not be read as 'Roman Catholic'; it means the Church "
         "in communion across the world, and a gloss is needed if the term is shown to a "
         "participant.",
         "The passage does not name the Donatists.",
         "The passage does not say how a clergyman was ordained or removed, and the sermons do "
         "not show a formal ordination.",
         "The passage comes near the end of a long argument on the sin against the Holy Spirit "
         "(Matthew 12:32); it needs that frame and must not be told without it."],
        "Augustine, Sermon 21 in the NPNF numbering (71 in the Maurist numbering), section 37. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "lines 13008-13009. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, "
        "lines 32485-32492 (OCR text; the sermon starts at line 30996). The sermon reads "
        "Matthew 12:32 as lifelong refusal to come from the scattering to the gathering that "
        "has received the Holy Spirit for the forgiveness of sins, and runs over thirty-eight "
        "sections; the passage is near its end. A translator's gloss, Area, follows at line "
        "13011, outside the passage. In the Latin, dispersione and congregationem are the "
        "scattering and the gathering, reprobum et fictum is worthless and false, and corde "
        "non ficto is with a heart that is not false. The sermon carries the gravity "
        "lpc.gravity.sacramental-ordination-validity in its minister's-worth form.",
    )

    emit_quote(
        "consider-who-was-there",
        "But He who is everywhere was there. He who is everywhere was there, in whose Name I "
        "believed. Thou coming I know not whence, yea, rather not coming, but wishing that I "
        "should come to thee, fixed in this place, sayest to me, ‘Thou wast not baptized duly, "
        "seeing I was not there.’ Consider who was there.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may take the 'I' for Augustine baptizing, or being baptized. It is "
        "a baptized believer answering a Donatist who says 'Thou wast not baptized duly, "
        "seeing I was not there', and Augustine voices the answer: the One in whose name he "
        "believed was there, and that One is everywhere.",
        "But He who is everywhere was there. He who is everywhere was there, the One in whose "
        "name I believed. You come from who knows where. No, you do not even come; you want me "
        "to come to you. You stay put here and tell me, ‘You were not baptized properly, "
        "because I was not there.’ Look at who was there.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 79 (NPNF numbering; Maurist 129), section 7; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "line 19722; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 50696-50701 "
                    "(the sermon starts at line 50446)",
          "license": "public-domain"}],
        2,
        ["participant asks how a believer answered the claim that his baptism was not proper "
         "because the speaker was not there",
         "participant asks whose act a baptism was in the end",
         "participant asks how Augustine answered the Donatists on baptism"],
        ["participant asks how Cyprian and Augustine gave opposite answers on baptism outside "
         "the Church -- lpc.demo.font-twice-answered gives that"],
        ["The speaker is a baptized believer answering a Donatist, as Augustine voices him; "
         "the passage does not say who baptized the speaker and must not be read as "
         "Augustine's own account of baptizing or being baptized.",
         "The Donatist's words are only quoted inside the reply and must not be presented as "
         "Augustine's own position.",
         "The sermons do not show a formal ordination or a dispute between bishops."],
        "Augustine, Sermon 79 in the NPNF numbering (129 in the Maurist numbering), section 7. "
        "English at cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
        "line 19722. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines "
        "50696-50701 (OCR text; the sermon starts at line 50446). The sentence begins inside a "
        "quotation whose opening mark is earlier, at lines 19717-19718; the closing mark is at "
        "line 19726 after a note. The passage ends before 'What was said to John?' and the "
        "John 1:33 reference at lines 19723-19725. In the Latin, recte baptizatus is baptized "
        "rightly or properly, hic positus is placed here, staying put, and in cujus nomen is "
        "in whose name. The sermon carries the gravity "
        "lpc.gravity.sacramental-ordination-validity.",
    )


    emit_quote(
        "the-creed-first-then-the-prayer",
        "Because then he said, “how shall they call upon Him in whom they have not believed?” "
        "ye have not first learnt the Lord’s Prayer, and after that the Creed; but first the "
        "Creed, where ye might know what to believe, and afterwards the Prayer, where ye might "
        "know whom to call upon. The Creed then has respect to the faith, the Lord’s Prayer to "
        "prayer; because it is he who believeth, that is heard when he calleth.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'learnt' as schoolwork. The Latin, accepistis, is 'you "
        "received', and Augustine uses it of what the candidates were given. He explains the "
        "order: they received the Creed first, so that they would know what to "
        "believe, and the Lord's Prayer after it, so that they would know whom to call on. "
        "'Has respect to' means 'belongs to'.",
        "He said, “How will they call on Him in whom they have not believed?” That is why you "
        "did not receive the Lord’s Prayer first and the Creed after it. You received the "
        "Creed first, so that in it you would know what to believe. Then you received the "
        "Prayer, so that in it you would know whom to call on. So the Creed belongs to faith, "
        "and the Lord’s Prayer to prayer. For it is the one who believes who is heard when he "
        "calls.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. modern_rendering follows the "
             "Latin of PL 38 where the English misleads: 'ye have not first learnt' renders "
             "non accepistis, 'you did not receive'; 'has respect to' renders pertinet ad, "
             "'belongs to'; and 'where ye might know' renders ubi sciretis, 'so that in it you "
             "would know'."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 6 (NPNF numbering; Maurist 56), section 1; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 10642-10643; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 26187-26199 "
                    "(the sermon starts at line 26159)",
          "license": "public-domain"}],
        1,
        ["participant asks why the Creed was given to the candidates before the Lord's Prayer",
         "participant asks what the Creed was for and what the Lord's Prayer was for",
         "participant asks how Augustine tied believing to praying"],
        ["participant asks how a candidate was meant to keep the Creed after the teaching "
         "ended -- lpc.quote.let-your-creed-be-a-mirror gives that"],
        ["The first sentence quotes Paul (Rom. x. 14), who is not named in the passage; the "
         "speaker must name him in conversation, since the sentence that names him is left out.",
         "The sermon is on the Lord's Prayer, spoken to the Competentes, the people preparing "
         "for baptism. It is not a sermon on the Creed itself and must not be presented as one.",
         "The modern rendering uses 'received' (accepistis) for the Creed and the Prayer; it "
         "does not describe a formal handing-over ceremony, and none may be supplied unless "
         "the sermon itself gives it."],
        "Augustine, Sermon 6 in the NPNF numbering (56 in the Maurist numbering), section 1. "
        "English in the NPNF translation at "
        "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, lines "
        "10642-10643. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines "
        "26187-26199 (OCR text; the sermon starts at line 26159). The sentence before the "
        "passage, at line 10642, quotes Romans x. 14-15 in full; the Romans x. 13 reference is "
        "in a note at line 10641, outside the passage. The same order of Creed first and "
        "Prayer after is repeated in NPNF 7 section 1, NPNF 8 section 1 and NPNF 9 section 1. "
        "In the Latin, accepistis is 'you received' and is the rite's own word, paired with "
        "'give back' (the pair is used openly in Sermon 58, PL 38 line 27711, reddituri "
        "estis, non Orationem, sed Symbolum); pertinet ad is 'belongs to'; exauditur is 'is heard and answered'. A "
        "page-foot note block (PL 38 lines 26192-26197) falls inside the Latin range between "
        "invo- and caretis, and the passage starts with the last word of line 26187, Quia. The "
        "scripture reference before the passage reads 'Rom. x, 13-13' in the OCR, probably "
        "13-15. The sermon carries the gravity lpc.gravity.preaching-and-catechesis in its "
        "catechetical form.",
    )

    emit_quote(
        "let-your-creed-be-a-mirror",
        "Call thy faith to mind, look into thyself, let thy Creed be as it were a mirror to "
        "thee. Therein see thyself, whether thou dost believe all which thou professest to "
        "believe, and so rejoice day by day in thy faith. Let it be thy wealth, let it be in a "
        "sort the daily clothing of thy soul.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may not know 'professest'. The Latin, confiteris, is to declare "
        "openly; here what the hearer declares is the Creed. Augustine tells the candidate to "
        "look at the Creed as a mirror, to check whether he believes all that he declares, and "
        "to treat it as his wealth and daily clothing. 'Soul' is NPNF's word; the Latin here "
        "says 'mind'.",
        "Call your faith to mind. Look into yourself. Let your Creed be like a mirror to you. "
        "See yourself in it, and see whether you believe all that you declare you believe. And "
        "rejoice in your faith every day. Let it be your wealth. Let it be, in a way, the "
        "daily clothing of your mind.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. modern_rendering follows the "
             "Latin of PL 38 where the English shifts it: 'clothing of thy soul' renders "
             "indumenta mentis tuae, 'clothing of your mind', since Augustine says mens here "
             "and turns to anima only in the next sentence, which the passage leaves out; "
             "'professest' renders confiteris, rendered 'declare' because 'confess' now "
             "suggests admitting guilt; and NPNF's 'so' in 'and so rejoice' is not in the "
             "Latin."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 8 (NPNF numbering; Maurist 58), section 13; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "line 11171; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 27719-27724 "
                    "(the sermon starts at line 27271)",
          "license": "public-domain"}],
        2,
        ["participant asks how a candidate for baptism was told to keep the Creed after "
         "learning it",
         "participant asks what Augustine meant by the Creed as a mirror",
         "participant asks how a believer was told to keep up faith day by day"],
        ["participant asks why the Creed came before the Lord's Prayer -- "
         "lpc.quote.the-creed-first-then-the-prayer gives that"],
        ["The sermon is on the Lord's Prayer, spoken to the Competentes, the people preparing "
         "for baptism. It is not a sermon on the Creed itself and must not be presented as one.",
         "The passage does not give the words of the Creed or say how often it is said; the "
         "sentence before it, which gives the times, is not in the passage and must not be "
         "supplied as if quoted.",
         "'Mind' in the modern rendering follows the Latin; NPNF has 'soul', and the speaker "
         "must not present one as the other."],
        "Augustine, Sermon 8 in the NPNF numbering (58 in the Maurist numbering), section 13. "
        "English in the NPNF translation at "
        "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, line 11171. "
        "Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 27719-27724 "
        "(OCR text; the sermon starts at line 27271). The sentence before the passage, at line "
        "11170, tells the candidate to say the Creed on rising and before sleep, and gives the "
        "reason that repetition keeps forgetfulness out; it is left out. The sentence after "
        "it, on the Apostle's 'unclothed' and 'naked', is cut off by notes at lines "
        "11172-11177 and is also left out. In the Latin, Commemora fidem tuam is 'call your "
        "faith to mind', which in context (commemorate vos ipsos, PL 38 line 27716) means "
        "reciting the Creed to oneself; tanquam speculum is 'like a mirror'; confiteris is an "
        "OCR reading ('condieris'), and the sense and NPNF both require it. The sermon carries "
        "the gravity lpc.gravity.preaching-and-catechesis in its catechetical form.",
    )

    emit_quote(
        "the-sermon-and-the-readings-are-daily-bread",
        "Again, what I am handling before you now is “daily bread;” and the daily lessons "
        "which ye hear in church, are daily bread, and the hymns ye hear and repeat are daily "
        "bread. For all these are necessary in our state of pilgrimage.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'handling' as touching objects and 'pilgrimage' as a trip "
        "to a shrine. The Latin, tracto, is expounding Scripture in a sermon, and "
        "peregrinationi is living away from one's homeland. Augustine names three things as "
        "daily bread: his own preaching, the readings in church, and the hymns, and says they "
        "are needed while we are far from home.",
        "And what I am explaining to you now is daily bread. The readings you hear in church "
        "every day are daily bread. The hymns you hear and sing are daily bread. For we need "
        "these while we are far from home.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. modern_rendering follows the "
             "Latin of PL 38 where the English misleads: 'handling' renders tracto, "
             "'explaining'; 'state of pilgrimage' renders peregrinationi nostrae, 'while we "
             "are far from home', since 'state of' is NPNF's addition and 'pilgrimage' narrows "
             "the Latin; 'Again' renders Et, 'And'; NPNF's 'all' in 'all these' is not in the "
             "Latin; 'repeat' renders dicitis, rendered 'sing'; and the quotation marks on "
             "'daily bread' are NPNF's."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 7 (NPNF numbering; Maurist 57), section 7; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "line 10894; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 27006-27028 "
                    "(the sermon starts at line 26785)",
          "license": "public-domain"}],
        2,
        ["participant asks what Augustine called daily bread besides the Eucharist",
         "participant asks how Augustine spoke of his own preaching",
         "participant asks why the readings and hymns in church mattered to believers"],
        ["participant asks how Augustine described the work of feeding his hearers -- "
         "lpc.quote.stewards-and-future-bishops gives that"],
        ["'Daily bread' here is the petition of the Lord's Prayer, and 'Again' follows the "
         "Eucharist sense given in the lines before the passage; the passage must not be used "
         "to say the Eucharist was not daily bread.",
         "'Far from home' needs the frame that heaven is home; the passage does not state it, "
         "and the speaker must supply it as the sense of the Latin peregrinatio without adding "
         "detail.",
         "The sermon is to the Competentes on the Lord's Prayer, not a sermon on the Creed, "
         "and the passage does not say how often hymns were sung."],
        "Augustine, Sermon 7 in the NPNF numbering (57 in the Maurist numbering), section 7. "
        "English in the NPNF translation at "
        "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, line 10894. "
        "Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 27006-27028 "
        "(OCR text; the sermon starts at line 26785). The lines before the passage "
        "(10889-10894) give the Eucharist as the spiritual daily bread, so 'Again' opens a "
        "further sense, which the passage itself states. A Latin gloss note ('Codex') falls "
        "later in line 10894, after the passage. In the Latin, tracto is the usual word for "
        "expounding Scripture in a sermon, peregrinatio is living away from one's homeland, "
        "and the next sentence (quando venerimus, 'when we get there') shows heaven as home. "
        "The passage starts with the last word of PL 38 line 27006, Et, and ends on line 27028 "
        "after a page break, with peregrina- (line 27010) resuming as tioni nostrae and "
        "apparatus notes at lines 27013-27025 between them. The passage is short, 43 words. "
        "The sermon carries the gravity lpc.gravity.preaching-and-catechesis.",
    )

    emit_quote(
        "two-hear-one-scorns-one-rises",
        "But wonderful it is, that when Christ Crucified is preached, two hear, one despiseth, "
        "the other ascendeth. Let him that despiseth, impute it to himself; let not him that "
        "ascendeth, arrogate it to himself. For he hath heard from the True Master; “No man "
        "cometh unto Me, except it were given unto him of My Father.”",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'wonderful' as delightful and 'True Master' as an owner. "
        "The Latin, Mirum, is 'strange', and Augustine is puzzled, not pleased; veraci "
        "Magistro is the truthful Teacher. When Christ crucified is preached, two hear, one "
        "scorns and one rises. The one who rises is not to claim it, since no one comes to "
        "Christ unless it is given him by the Father.",
        "But it is a strange thing. When Christ crucified is preached, two people hear. One "
        "scorns it, and the other rises. Let the one who scorns blame himself. Let the one who "
        "rises not claim it for himself. For he has heard the truthful Teacher say, “No one "
        "comes to Me unless it is given to him by My Father.”",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. modern_rendering follows the "
             "Latin of PL 38 where the English misleads: 'wonderful' renders Mirum, 'a strange "
             "thing'; 'impute it to himself' renders imputet sibi, 'blame himself'; "
             "'despiseth' and 'ascendeth' render contemnit and ascendit, 'scorns' and 'rises'; "
             "and 'True Master' renders veraci Magistro, 'the truthful Teacher'."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 81 (NPNF numbering; Maurist 131), section 3; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "line 19899; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 51152-51156 "
                    "(the sermon starts at line 51045)",
          "license": "public-domain"}],
        1,
        ["participant asks why one hearer of the preaching believes and another does not",
         "participant asks what Augustine said a believer must not claim for himself",
         "participant asks how Augustine used 'No man cometh unto Me, except it were given "
         "unto him of My Father'"],
        ["participant asks how a person's own acts stand under God's working -- "
         "lpc.quote.what-is-done-by-you-he-does-in-you gives that"],
        ["The last sentence quotes John vi. 65 without naming the Gospel; the speaker must not "
         "supply more than the verse the passage gives.",
         "The passage does not name the Pelagians and must not be read as a reply to them; "
         "'Against the Pelagians' is NPNF's own title for the sermon.",
         "The passage does not say why one hearer rises and the other scorns, and must not be "
         "extended into a doctrine of election.",
         "'Rises' (ascendit) is the sermon's image for coming to faith and does not mean the "
         "resurrection."],
        "Augustine, Sermon 81 in the NPNF numbering (131 in the Maurist numbering), section 3. "
        "English in the NPNF translation at "
        "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, line 19899. "
        "Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 51152-51156 "
        "(OCR text; the sermon starts at line 51045). The sermon was delivered at the Table of "
        "the martyr Cyprian (sermon heading, lines 19865-19867). A page-break tag (NPNF p. "
        "502) falls inside line 19899 and is stripped. Section 3 goes on at lines 19900-19915 "
        "with Philippians ii. 12-13; that is cut by notes and is left out. The section's next "
        "clause in the Latin, Gaudeat, quia datum est ('let him rejoice that it has been "
        "given'), would complete the thought but is outside the passage. The Latin passage "
        "follows an editor's chapter heading at PL 38 lines 51151-51152. In the Latin, Mirum "
        "est is 'it is strange', arroget sibi is 'claim it for himself' and datum fuerit is "
        "'has been given'. The sermon carries the gravity "
        "lpc.gravity.grace-and-human-incapacity.",
    )

    emit_quote(
        "what-is-done-by-you-he-does-in-you",
        "Why do I say then, “Thy will be done in heaven and in earth,” and do not say, “Thy "
        "will be done by heaven and earth?” Because what is done by thee, He Himself doeth in "
        "thee. Never is anything done by thee which He Himself doeth not in thee. Sometimes, "
        "indeed, He doeth in thee what is not done by thee; but never is anything done by "
        "thee, if He do it not in thee.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'He doeth in thee what is not done by thee' as God forcing "
        "a person. Augustine is explaining the petition 'Thy will be done in heaven and in "
        "earth'. God's will is done 'in you' whether you will it or not; it is done 'by you' "
        "when you do it as well. Nothing is done by the one who prays that God does not also do in him.",
        "Why then do I say, “Your will be done in heaven and on earth,” and not, “Your will be "
        "done by heaven and earth”? Because what is done by you, He Himself does in you. "
        "Nothing is ever done by you that He Himself does not do in you. Sometimes, indeed, He "
        "does in you what is not done by you. But nothing is ever done by you unless He does "
        "it in you.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 6 (NPNF numbering; Maurist 56), section 7; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 10700-10701; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 26351-26356 "
                    "(the sermon starts at line 26159)",
          "license": "public-domain"}],
        2,
        ["participant asks what Augustine meant by 'Thy will be done' in the Lord's Prayer",
         "participant asks how Augustine spoke of what a person does and what God does in him",
         "participant asks why Augustine said nothing is done by us unless God does it in us"],
        ["participant asks why one hearer believes and another scorns -- "
         "lpc.quote.two-hear-one-scorns-one-rises gives that"],
        ["The passage needs its lead-in: in the lines before it (PL 38 lines 26340-26351, from "
         "Fiet enim voluntas Dei in te, etsi non fit a te), 'in you' is God's will done in "
         "everyone, saved or lost, and 'by you' is God's will done by you as well. Without that lead-in, "
         "'He does in you what is not done by you' can be heard as compulsion, and the speaker "
         "must supply it.",
         "The sermon is to the Competentes, the people preparing for baptism, on the Lord's "
         "Prayer. It is not an argument with Pelagians and must not be read as a reply to them.",
         "The opening question is Augustine's own, put to the Competentes, not an objection "
         "raised by a hearer."],
        "Augustine, Sermon 6 in the NPNF numbering (56 in the Maurist numbering), section 7. "
        "English in the NPNF translation at "
        "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, lines "
        "10700-10701. Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines "
        "26351-26356 (OCR text; the sermon starts at line 26159). The lines before the passage "
        "(NPNF lines 10693-10700) set out that God's will is done in the saved and in the "
        "lost; the passage opens in the middle of that argument ('Why do I say then'). In the "
        "Latin, a te and in te are exact and the whole argument rests on that pair; "
        "Augustine's form has no sicut ('as') in 'in coelo et in terra'. The NPNF English "
        "follows the Latin closely throughout, with nothing added or narrowed. The longest "
        "sentence is the opening question, made of two quoted petitions, and cannot be split "
        "without losing the contrast. The sermon carries the gravity "
        "lpc.gravity.grace-and-human-incapacity as catechesis on prayer.",
    )

    emit_quote(
        "no-one-has-the-love-of-god-from-himself",
        "Finally, when he had said, “The love of God hath been shed abroad in our hearts;” "
        "that no man might think that he hath this love of God of himself, he added "
        "immediately, “By the Holy Spirit, who hath been given to us.” Therefore, that thou "
        "mayest love God, let God dwell in thee, and love Himself in thee, that is, to His "
        "love let Him move thee, enkindle, enlighten, arouse thee.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'Finally' as the last point in a list and 'shed abroad' as "
        "spilled. The Latin, Denique, is 'indeed', and diffusa est is 'poured out'. Augustine "
        "reads Paul's words so that no one thinks his love for God comes from himself, and "
        "asks that God live in the believer, love Himself through him, and move him to love.",
        "Indeed, he had said, “The love of God has been poured out in our hearts.” Then he "
        "added at once, “through the Holy Spirit, who has been given to us.” He did this so "
        "that no one would think his love for God came from himself. So if you are to love "
        "God, let God live in you and love Himself through you. That is, let Him move you to "
        "His love. Let Him kindle you, give you light and stir you up.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. modern_rendering follows the "
             "Latin of PL 38 where the English misleads or shifts: 'Finally' renders Denique, "
             "'Indeed'; 'shed abroad' renders diffusa est, 'poured out'; 'love Himself in "
             "thee' renders amet se de te, literally 'love Himself from you', rendered "
             "'through you'; and 'enkindle, "
             "enlighten, arouse' renders accendat, illuminet, excitet, 'kindle, give light, "
             "stir up'. The purpose clause is moved after the two quotations so each sentence "
             "holds one thought."),
        [{"source_id": "lpc.source.augustine-sermons-on-selected-lessons",
          "locus": "Sermon 78 (NPNF numbering; Maurist 128), section 4; English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "line 19486; Latin at "
                    "cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 50082-50088 "
                    "(the sermon starts at line 49959)",
          "license": "public-domain"}],
        2,
        ["participant asks where Augustine said the love of God in a believer comes from",
         "participant asks how Augustine read 'The love of God hath been shed abroad in our "
         "hearts'",
         "participant asks what Augustine meant by God dwelling in a person and moving him to "
         "love"],
        ["participant asks why one hearer believes and another scorns -- "
         "lpc.quote.two-hear-one-scorns-one-rises gives that"],
        ["'He' is Paul (Rom. v. 5), named neither in the passage nor in the Latin sentence; "
         "the speaker must name him in conversation.",
         "The passage does not name the Pelagians and must not be read as a reply to them; the "
         "sermon is on John v. 31 and Galatians v. 16-17 (the flesh against the Spirit).",
         "The passage is one argument about where the love of God comes from and does not set "
         "out a whole doctrine of grace."],
        "Augustine, Sermon 78 in the NPNF numbering (128 in the Maurist numbering), section 4. "
        "English in the NPNF translation at "
        "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, line 19486. "
        "Latin at cic/texts/augustine_sermones-1-340-lat_migne-pl38.txt, lines 50082-50088 "
        "(OCR text; the sermon starts at line 49959). The line begins right after a short "
        "scripture-reference note (2 Cor. iv. 7, line 19485) that belongs to the earlier "
        "sentence, not this one. The Latin starts mid-line at PL 38 line 50082 after (II Cor. "
        "iv, 7), and carries the reference (Rom. v, 5) that the English line omits. In the "
        "Latin, Denique is 'indeed, in short', a se sibi esse quod diligit Deum is that his "
        "loving God comes from himself, habitet is 'live', and accendat, illuminet and excitet "
        "are 'set alight, give light, rouse'. The sermon carries the gravity "
        "lpc.gravity.grace-and-human-incapacity.",
    )


# ===========================================================================
# COMMENTARY QUOTES (15) -- Augustine's expositions of the Psalms, his tractates on John
# and the First Epistle of John, and his commentary on the Sermon on the Mount, one per
# passage.
# ===========================================================================

def build_commentary_quotes() -> None:
    emit_quote(
        "the-old-man-nailed-to-the-cross-speaks",
        "“O God, my God, look upon me, why hast Thou forsaken me far from my salvation?” "
        "(ver. 1). Far removed from my salvation: for “salvation is far from sinners.” "
        "“The words of my sins.” For these are not the words of righteousness, but of my "
        "sins. For it is the old man nailed to the Cross that speaks, ignorant even of the "
        "reason why God hath forsaken him: or else it may be thus, The words of my sins "
        "are far from my salvation.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear this only as Christ's own cry of distress, or as proof that "
        "God abandoned him. In the section before, Augustine hears the crucified Christ speaking "
        "for 'the old man', our old self, nailed to the Cross with him. So 'the words of my sins' "
        "are that old self's words, not Christ's own sins. The verse is Psalm 21 in the Latin "
        "Psalter, which reads differently from the English Bible.",
        "“O God, my God, look on me. Why have You forsaken me, far from my salvation?” (verse 1). Far from my salvation, because “salvation is far from sinners.” “The words of my sins.” These are not the words of righteousness. They are the words of my sins. For it is the old self nailed to the Cross that speaks. It does not even know why God has forsaken it. Or it may be read this way: the words of my sins are far from my salvation.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. Augustine comments on the "
             "Latin Psalter, made from the Greek, so the verse he quotes differs from the "
             "English Bible: it begins 'look upon me' and ends 'the words of my sins', "
             "where the Hebrew has 'the words of my roaring'. A variants note in the PL 36 "
             "text, at line 1156, gives the Hebrew reading."),
        [{"source_id": "lpc.source.augustine-expositions-on-the-psalms",
          "locus": "Exposition on Psalm 22 (NPNF Psalm XXII; Psalm 21 in the Vulgate and "
                    "in PL 36), section 2 (also section 2 in PL 36, where the OCR misprints it as 3); English at "
                    "cic/texts/npnf108_augustine-exposition-psalms.xml, lines 3289-3295; "
                    "Latin at "
                    "cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt, "
                    "lines 12992-13000",
          "license": "public-domain"}],
        2,
        ["participant asks about Psalm 22:1, 'My God, my God, why have you forsaken me'",
         "participant asks whose voice Augustine heard in Christ's cry from the cross",
         "participant asks why Augustine called the words of this Psalm 'the words of my "
         "sins'"],
        [],
        ["The passage does not say that Christ himself sinned or was forsaken by God; it "
         "says the old man nailed to the Cross is the one who speaks.",
         "Section 1, which says the Lord speaks 'sustaining also the person of the old "
         "man', is not in the passage and must not be supplied as if quoted.",
         "The passage does not date or place the exposition; the bracketed editor's note "
         "at line 3275, drawn from a different exposition, is outside it."],
        "Augustine, Exposition on Psalm 22 (Psalm 21 in the Vulgate and in PL 36), section "
        "2 in the NPNF numbering (also section 2 in PL 36, where the OCR misprints it as 3). English in the NPNF "
        "translation at cic/texts/npnf108_augustine-exposition-psalms.xml, lines "
        "3289-3295. Latin at "
        "cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt, lines "
        "12992-13000 (OCR text). A footnote at line 3291 and a Bible cross-reference at "
        "line 3294 sit inside the line range and are not part of the passage. Section 1 "
        "(lines 3278-3284), where Augustine says the Lord Jesus Christ speaks in the "
        "person of the Crucified, is left out, as is everything after the passage in "
        "section 2. In the Latin, verba delictorum meorum is 'the words of my sins' and "
        "Vetus enim homo confixus cruci loquitur is 'for the old man nailed to the Cross "
        "speaks'.",
    )

    emit_quote(
        "david-himself-hath-been-sent-to-thee",
        "Whoever thou art that hast sinned, and hesitatest to exercise penitence for thy "
        "sin, despairing of thy salvation, hear David groaning. To thee Nathan the prophet "
        "hath not been sent, David himself hath been sent to thee. Hear him crying, and "
        "with him cry: hear him groaning, and with him groan; hear him weeping, and mingle "
        "tears; hear him amended, and with him rejoice. If from thee sin could not be "
        "excluded, be not hope of pardon excluded.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may expect a sermon that scolds the sinner. Augustine sends the "
        "sinner who fears to repent to David as a companion: hear him groan, weep and "
        "rejoice, and do the same with him. 'Penitence' renders the Latin poenitentia, repentance; the passage does not say whether the Church's formal penance is meant.",
        "Whoever you are who have sinned: you hold back from repenting of your sin, because you despair of your salvation. Hear David groaning. Nathan the prophet has not been sent to you. David himself has been sent to you. Hear him crying out, and cry out with him. Hear him groaning, and groan with him. Hear him weeping, and add your tears to his. Hear him set right, and rejoice with him. If sin could not be kept out of you, do not let hope of pardon be kept out.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. Its 'exercise penitence' renders agere poenitentiam, which in Augustine can mean to repent or to undergo the Church's penance; the passage does not say which. An editor's bracketed note at line 9116, outside the text field, calls the earlier 'do penance' 'feeble'; that is the editor's judgment, not the author's."),
        [{"source_id": "lpc.source.augustine-expositions-on-the-psalms",
          "locus": "Exposition on Psalm 51 (NPNF Psalm LI; Psalm 50 in the Vulgate and in "
                    "PL 36), section 5; English at "
                    "cic/texts/npnf108_augustine-exposition-psalms.xml, lines 9114-9117; "
                    "Latin at "
                    "cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt, "
                    "lines 43058-43065",
          "license": "public-domain"}],
        2,
        ["participant asks about Psalm 51, David's sin and his confession",
         "participant asks what Augustine told someone who had fallen and was afraid to "
         "repent",
         "participant asks whether a great sinner could still hope for forgiveness"],
        ["participant asks how lapsed Christians were brought back after persecution -- "
         "lpc.term.the-lapsed and the Cyprian-phase material give that"],
        ["The passage does not describe a penitential rite, a penance set by a bishop or "
         "readmission to communion; it is an appeal to the hearer to repent with David.",
         "'Whoever thou art that hast sinned' is a general address; the passage names no "
         "lapsed group and gives no date or occasion for the exposition.",
         "Nathan's rebuke is named but not told; the story of David and Nathan is in the "
         "Psalm's title and in 2 Samuel, not in this passage."],
        "Augustine, Exposition on Psalm 51 (Psalm 50 in the Vulgate and in PL 36), section "
        "5 in the NPNF numbering. English in the NPNF translation at "
        "cic/texts/npnf108_augustine-exposition-psalms.xml, lines 9114-9117. Latin at "
        "cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt, lines "
        "43058-43065 (OCR text). An editor's bracketed note at line 9116 sits inside the "
        "line range and is not part of the passage. The sentences before it in section 5, "
        "on those who have not yet fallen and on sin with despair being 'certain death', "
        "and the next sentences, on Nathan the prophet and the king's humility, are left "
        "out. In the Latin, Quisquis peccasti is 'whoever thou art that hast sinned' and "
        "intercludi is 'to be shut out'. The meaning of agere poenitentiam, whether to repent or to undergo the Church's penance, is contested: the passage does not settle it, and the rendering's 'repenting' must not be read as ruling out the Church's penance.",
    )

    emit_quote(
        "dash-the-little-ones-against-the-rock",
        "How shall they repay her? As she hath served us. Let her little ones be choked in "
        "turn: yea let her little ones in turn be dashed, and die. What are the little "
        "ones of Babylon? Evil desires at their birth. For there are, who have to fight "
        "with inveterate lusts. When lust is born, before evil habit giveth it strength "
        "against thee, when lust is little, by no means let it gain the strength of evil "
        "habit; when it is little, dash it. But thou fearest, lest though dashed it die "
        "not; “Dash it against the Rock; and that Rock is Christ.”",
        "lpc.figure.augustine",
        "verbatim",
        "A modern reader meets a verse that seems to bless the killing of infants. "
        "Augustine reads 'the little ones of Babylon' as evil desires at their birth. He "
        "says to dash a desire against the Rock while it is still little, before habit "
        "gives it strength, and the Rock is Christ.",
        "How shall they repay her? As she has treated us. Let her little ones be choked in their turn. Yes, let her little ones in their turn be dashed, and die. What are the little ones of Babylon? Evil desires at their birth. For some people have to fight with old, deep-rooted cravings. When a craving is born, evil habit has not yet given it strength against you. While it is little, do not let it gain the strength of evil habit. While it is little, dash it. But you fear that, though dashed, it may not die. “Dash it against the Rock; and that Rock is Christ.”",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. Augustine comments on the "
             "Latin Psalter, where Psalm 136 ends 'Blessed is he who shall hold and dash "
             "thy little ones against the rock'. 'Choked' renders offocentur, 'be "
             "smothered', and 'dashed' renders elidantur, 'be struck down'. The closing "
             "words echo 1 Corinthians 10:4, which the Latin cites."),
        [{"source_id": "lpc.source.augustine-expositions-on-the-psalms",
          "locus": "Exposition on Psalm 137 (NPNF Psalm CXXXVII; Psalm 136 in the Vulgate "
                    "and in PL 37), section 12 (section 21 in the PL text); English at "
                    "cic/texts/npnf108_augustine-exposition-psalms.xml, lines 27121-27122; "
                    "Latin at "
                    "cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt, "
                    "lines 126347-126369",
          "license": "public-domain"}],
        1,
        ["participant asks about Psalm 137:9, 'happy is he who dashes your little ones "
         "against the rock'",
         "participant asks how Augustine read the verse about dashing the little ones",
         "participant asks how Augustine's people read the harsh verses of the Psalms"],
        [],
        ["The passage does not say that the verse has no literal sense, and it says "
         "nothing of the Psalm's first writer or setting; it gives what Augustine says the "
         "little ones are.",
         "It does not say that a desire dies when it is dashed; it says one may fear that "
         "it will not die, and answers that it must be dashed against the Rock, which is "
         "Christ.",
         "The paragraph before it, on how Babylon taught children from infancy, and the "
         "verse itself, quoted earlier in the section, are outside the passage.",
         "The passage names no audience; the speaker must not say Augustine spoke it to those "
         "preparing for baptism or to any other group."],
        "Augustine, Exposition on Psalm 137 (Psalm 136 in the Vulgate and in PL 37), "
        "section 12 in the NPNF numbering (section 21 in the PL text). English in the NPNF "
        "translation at cic/texts/npnf108_augustine-exposition-psalms.xml, lines "
        "27121-27122. Latin at "
        "cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt, lines "
        "126347-126369 (OCR text). The Latin is broken by a page break: lines "
        "126357-126366 are editorial footnotes printed in the middle of the sentence and "
        "are not part of the passage. The sentences before the passage in section 12, from "
        "the verse itself through Babylon's teaching of infants, are left out; the NPNF "
        "text marks a gap just before the first sentence with an ellipsis. In the Latin, "
        "nascentes malae cupiditates is 'evil desires at their birth' (the OCR reads malx "
        "rapiditates), parvuli is 'little ones' and petra is 'rock'.",
    )

    emit_quote(
        "they-first-dwelt-together-in-unity",
        "All were from thence, and they first dwelt together in unity; who sold all they "
        "had, and laid the price of their goods at the Apostles’ feet, as is read in the "
        "Acts of the Apostles. And distribution was made to each one as he had need, and "
        "none called anything his own, but they had all things common. And what is "
        "“together in unity”? They had, he says, one mind and one heart God-wards. So they "
        "were the first who heard, Behold how good and how pleasant is it, that brethren "
        "dwell together. They were the first to hear, but heard it not alone.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'dwell together in unity' as a general wish for "
        "harmony. Augustine says the first to live it were the first believers, who sold "
        "their goods and had 'one mind and one heart God-wards', and that they were the "
        "first to hear the verse but not the only ones. 'God-wards' is the Latin in Deum, "
        "'towards God'.",
        "All came from there, and they were the first to live together in unity. They sold all they had, and laid the price of their goods at the Apostles’ feet, as we read in the Acts of the Apostles. Each was given what he needed. No one called anything his own; they held all things in common. And what is “together in unity”? They had, he says, one mind and one heart toward God. So they were the first to hear, See how good and how pleasant it is for brothers to live together. They were the first to hear it, but they did not hear it alone.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-expositions-on-the-psalms",
          "locus": "Exposition on Psalm 133 (NPNF Psalm CXXXIII; Psalm 132 in the Vulgate "
                    "and in PL 37), section 2; English at "
                    "cic/texts/npnf108_augustine-exposition-psalms.xml, lines 26754-26763; "
                    "Latin at "
                    "cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt, "
                    "lines 123237-123247",
          "license": "public-domain"}],
        2,
        ["participant asks about Psalm 133:1, 'how good and how pleasant it is for "
         "brethren to dwell together in unity'",
         "participant asks who first lived in unity, according to Augustine",
         "participant asks how Augustine described the unity of the first believers"],
        ["participant asks how bishops and good shepherds were held in one unity -- "
         "lpc.quote.one-good-shepherd-not-many gives that"],
        ["'Thence' in 'All were from thence' is the Jewish people, named in the sentences "
         "before the passage; the passage alone does not say so.",
         "The passage does not mention bishops, a college of bishops or communion between "
         "churches; it is about the shared life of the first believers.",
         "The sentences before it, which say the verse 'begat the Monasteries', and the "
         "next section, on the name of monks, are outside the passage."],
        "Augustine, Exposition on Psalm 133 (Psalm 132 in the Vulgate and in PL 37), "
        "section 2. English in the NPNF translation at "
        "cic/texts/npnf108_augustine-exposition-psalms.xml, lines 26754-26763. Latin at "
        "cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt, lines "
        "123237-123247 (OCR text). Three Bible cross-references (Acts iv. 34, 35; Acts ii. "
        "45; Acts iv. 32) sit inside the line range, at lines 26756, 26759 and 26762, and "
        "are not part of the passage. The sentences before the passage in section 2, from "
        "the verse as a trumpet through the Jewish origin of the Apostles and of the five "
        "hundred and the hundred and twenty, are left out. In the Latin, anima una et cor "
        "unum in Deum is 'one soul and one heart toward God', which the NPNF renders 'one "
        "mind and one heart God-wards'. The passage is tied to the gravity lpc.gravity.collegial-communion-preserved only loosely: it speaks of the unity of the first believers, not of bishops keeping communion through disagreement.",
    )

    emit_quote(
        "peter-may-baptize-but-this-is-he-that-baptizeth",
        "What then did he learn from the dove, that he may not afterwards be found a liar "
        "(which God forbid we should think), if it be not this, that there was to be a "
        "certain peculiarity in Christ, such that, although many ministers, be they "
        "righteous or unrighteous, should baptize, the virtue of baptism would be "
        "attributed to Him alone on whom the dove descended, and of whom it was said, "
        "“This is He that baptizeth with the Holy Ghost”? Peter may baptize, but this is "
        "He that baptizeth; Paul may baptize, yet this is He that baptizeth; Judas may "
        "baptize, still this is He that baptizeth.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may think a baptism's worth depends on the one who gives it. "
        "Augustine says no: whoever baptizes, even Judas, it is Christ who baptizes. The "
        "Latin says the holiness of baptism is credited to him alone. 'Peculiarity' is the "
        "Latin proprietas, a thing that belongs to Christ alone.",
        "What then did he learn from the dove, so that he would not later be found a liar? (God forbid we should think it.) It can only be this. There was to be something that belongs to Christ alone. Many ministers would baptize, whether righteous or unrighteous. But the holiness of baptism would be credited to Him alone. The dove came down on Him, and it was said of Him, “This is He who baptizes with the Holy Spirit.” Peter may baptize, but this is He who baptizes. Paul may baptize, yet this is He who baptizes. Judas may baptize, still this is He who baptizes.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. Its 'virtue of baptism' "
             "renders sanctitas Baptismi, the holiness of baptism, and 'peculiarity' "
             "renders proprietatem, a property that belongs to Christ alone."),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Tractate 6 on the Gospel of John (NPNF Tractate VI), section 7; "
                    "English at cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, "
                    "lines 1420-1421; Latin at "
                    "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
                    "lines 7937-7945",
          "license": "public-domain"}],
        1,
        ["participant asks about John 1:33, 'the same is he which baptizeth with the Holy "
         "Ghost'",
         "participant asks whether the worth of a baptism depended on the minister",
         "participant asks who it is that really baptizes, according to Augustine"],
        ["participant asks whether pardon could come through an unworthy clergyman -- "
         "lpc.quote.pardon-through-a-wicked-clergyman gives that"],
        ["The passage names Judas as an example; it does not say that Judas baptized "
         "anyone, only that if he did, it would still be Christ who baptizes.",
         "It does not name the Donatists or any dispute, and the word 'valid' does not "
         "appear; the passage rests on John 1:33 and the dove.",
         "It speaks only of whose baptism it is; it does not say the minister's own sin is of no account to the minister. Section 15, outside it, says baptism held apart from the Church's unity harms the one who receives it; that is about the recipient, not the minister, and must not be cited for the minister."],
        "Augustine, Tractate 6 on the Gospel of John (NPNF Tractate VI), section 7. "
        "English in the NPNF translation at "
        "cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, lines 1420-1421. Latin "
        "at "
        "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
        "lines 7937-7945 (OCR text). The passage is the end of section 7. The sentences "
        "before it, on what John learned from the dove and on how he already knew the "
        "Lord, are left out. In the Latin the closing sentence reads Petrus baptizet, hic "
        "est qui baptizat; Paulus baptizet, hic est qui baptizat; Judas baptizet, hic est "
        "qui baptizat. The passage carries the gravity "
        "lpc.gravity.sacramental-ordination-validity.",
    )

    emit_quote(
        "the-word-is-added-to-the-element",
        "Why does He not say, Ye are clean through the baptism wherewith ye have been "
        "washed, but “through the word which I have spoken unto you,” save only that in "
        "the water also it is the word that cleanseth? Take away the word, and the water "
        "is neither more nor less than water. The word is added to the element, and there "
        "results the Sacrament, as if itself also a kind of visible word.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'sacrament' as only a ceremony. Augustine says the "
        "water is plain water until the word is added, and then there is a sacrament, 'a "
        "kind of visible word'. The 'element' is the water, and the word is what cleanses "
        "even in the water.",
        "Why does He not say, You are clean through the baptism with which you have been washed? Why does He say instead, “through the word which I have spoken to you”? It can only be that in the water too, it is the word that cleanses. Take away the word, and the water is nothing more or less than water. The word is added to the element, and the sacrament comes to be. It is as if it too were a kind of visible word.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Tractate 80 on the Gospel of John (NPNF Tractate LXXX), section 3; "
                    "English at cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, "
                    "line 10111; Latin at "
                    "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
                    "lines 37171-37176",
          "license": "public-domain"}],
        2,
        ["participant asks about John 15:3, 'now ye are clean through the word which I "
         "have spoken'",
         "participant asks how Augustine explained what makes a sacrament",
         "participant asks why the water of baptism was more than water"],
        [],
        ["The passage gives no formula and does not say which words must be spoken in "
         "baptism.",
         "It does not define sacrament for every rite; it speaks of the water of baptism, "
         "and the foot-washing of John 13:10, in the next sentence, is not part of it.",
         "It does not say the word works by being said; later in the same section, outside "
         "the passage, Augustine says it works 'not because it is uttered, but because it "
         "is believed'."],
        "Augustine, Tractate 80 on the Gospel of John (NPNF Tractate LXXX), section 3. "
        "English in the NPNF translation at "
        "cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, line 10111. Latin at "
        "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
        "lines 37171-37176 (OCR text). Section 3 opens with John 15:3 itself, 'Now ye are "
        "clean through the word which I have spoken unto you', which is left out, and "
        "everything after 'a kind of visible word' is left out. In the Latin, Detrahe "
        "verbum, et quid est aqua nisi aqua? is 'take away the word, and what is water but "
        "water?'. The passage carries the gravity "
        "lpc.gravity.sacramental-ordination-validity.",
    )

    emit_quote(
        "believe-and-thou-hast-eaten-already",
        "“Jesus answered and said unto them, This is the work of God, that ye believe on "
        "Him whom He has sent.” This is then to eat the meat, not that which perisheth, "
        "but that which endureth unto eternal life. To what purpose dost thou make ready "
        "teeth and stomach? Believe, and thou hast eaten already.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'eat the meat' as a command about flesh and bread. "
        "'Meat' is the older word for food, the Latin cibus. Augustine reads the Lord's "
        "words about food that lasts as a call to believe: this is the work of God, that "
        "you believe on the one he sent, and to believe is to have eaten already.",
        "“Jesus answered and said to them, This is the work of God, that you believe in Him whom He has sent.” This, then, is to eat the food: not the food that perishes, but the food that lasts to eternal life. Why do you get your teeth and stomach ready? Believe, and you have eaten already.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. 'Meat' is the older English "
             "word for food, as in the Latin cibus; it does not mean flesh."),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Tractate 25 on the Gospel of John (NPNF Tractate XXV), section 12; "
                    "English at cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, "
                    "lines 4496-4497; Latin at "
                    "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
                    "lines 20107-20111",
          "license": "public-domain"}],
        2,
        ["participant asks about John 6:29, 'this is the work of God, that ye believe on "
         "him whom he hath sent'",
         "participant asks what Augustine meant by 'believe, and thou hast eaten'",
         "participant asks how Augustine read the Lord's talk of food that lasts"],
        [],
        ["The passage does not speak of the Eucharist or of eating the flesh and drinking "
         "the blood; it speaks of the food that lasts to eternal life, and the bread of "
         "the Eucharist is not mentioned.",
         "It does not say that works are unnecessary; the next sentences, outside the "
         "passage, say faith is 'distinguished from works' and then call faith itself a "
         "work.",
         "The sentences after it, which say 'Nor did He say, This is your work', that "
         "whoever glories may glory in the Lord, are outside the passage and must not be "
         "supplied as if quoted."],
        "Augustine, Tractate 25 on the Gospel of John (NPNF Tractate XXV), section 12. "
        "English in the NPNF translation at "
        "cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, lines 4496-4497. Latin "
        "at "
        "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
        "lines 20107-20111 (OCR text). The passage is the middle of section 12. The "
        "sentences before it, which quote John 6:27-28, and everything after 'Believe, and "
        "thou hast eaten already', are left out. In the Latin, Ut quid paras dentes et "
        "ventrem? is 'why do you make ready teeth and stomach?'. The passage carries the "
        "gravity lpc.gravity.grace-and-human-incapacity through its reading of believing "
        "as 'the work of God'; the sentences just after it state the point more plainly "
        "and are not in the passage.",
    )

    emit_quote(
        "the-wretched-woman-and-mercy",
        "This is the voice of Justice: Let her, the sinner, be punished, but not by "
        "sinners: let the law be fulfilled, but not by the transgressors of the law. This "
        "certainly is the voice of justice: by which justice, those men pierced through as "
        "if by a dart, looking into themselves and finding themselves guilty, “one after "
        "another all withdrew.” The two were left alone, the wretched woman and Mercy. But "
        "the Lord, having struck them through with that dart of justice, deigned not to "
        "heed their fall, but, turning away His look from them, “again He wrote with His "
        "finger on the ground.”",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may expect Augustine to dwell on the woman's sin. He says the "
        "voice of justice sent the accusers back to look at themselves, and when they had "
        "all gone out, only two were left: the wretched woman and Mercy. 'Mercy' is the "
        "Latin misericordia, and the Lord stays with her.",
        "This is the voice of Justice: Let her, the sinner, be punished, but not by sinners. Let the law be carried out, but not by those who break the law. This certainly is the voice of justice. By that justice those men were pierced as if by a dart. They looked into themselves and found themselves guilty, and “one after another they all went away.” The two were left alone, the wretched woman and Mercy. The Lord had struck them through with that dart of justice. But He did not think their fall worth watching. He turned His gaze away from them, and “again He wrote with His finger on the ground.”",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. The capital 'M' in 'Mercy' is "
             "the translator's; the Latin misericordia is the plain word for mercy. 'Dart' "
             "renders telum, a thrown weapon."),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Tractate 33 on the Gospel of John (NPNF Tractate XXXIII), section 5; "
                    "English at cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, "
                    "lines 5444-5447; Latin at "
                    "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
                    "lines 23617-23626",
          "license": "public-domain"}],
        1,
        ["participant asks about John 8:1-11, the woman taken in adultery",
         "participant asks what Augustine meant by 'the wretched woman and Mercy'",
         "participant asks how Augustine held justice and mercy together"],
        [],
        ["The passage does not say the woman was forgiven, restored or sent away; it ends "
         "with the Lord writing on the ground again, and 'Neither do I condemn thee' comes "
         "in the next section.",
         "It does not describe any church procedure for adultery or penance.",
         "The capital 'M' in 'Mercy' is the translator's; the Latin gives misericordia as "
         "a plain word."],
        "Augustine, Tractate 33 on the Gospel of John (NPNF Tractate XXXIII), section 5. "
        "English in the NPNF translation at "
        "cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, lines 5444-5447. Latin "
        "at "
        "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
        "lines 23617-23626 (OCR text). The sentences before the passage in section 5, "
        "which give the Lord's answer 'He that is without sin of you, let him first cast a "
        "stone at her' and say what the writing on the ground means, are left out. In the "
        "Latin, Relicti sunt duo, misera et misericordia is 'two were left, the wretched "
        "woman and mercy'. The passage carries the gravity "
        "lpc.gravity.penitential-discipline.",
    )

    emit_quote(
        "the-flight-of-the-mind-is-fear",
        "At present, he who seeketh his own, not the things that are Jesus Christ’s, in "
        "order not to lose what he follows after, the advantages of human friendship, and "
        "incur the annoyances of human enmity, keeps quiet and does not administer rebuke. "
        "See, the wolf has caught a sheep by the throat; the devil has enticed a believer "
        "into adultery: thou holdest thy peace—thou utterest no reproof. O hireling, thou "
        "hast seen the wolf coming and hast fled! Perhaps he answers and says: See, I am "
        "here; I have not fled. Thou hast fled, because thou hast been silent; thou hast "
        "been silent, because thou hast been afraid. The flight of the mind is fear.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'hireling' as only a paid worker. Augustine says the "
        "hireling is the one who seeks his own, and shows him in a leader who sees a "
        "believer fall into sin and says nothing, to keep his friends. Saying 'I am here' is not enough: fear is 'the flight of the mind'.",
        "As things are now, the one who seeks his own, not the things of Jesus Christ, keeps quiet and gives no rebuke. He does not want to lose what he is after, the benefits of human friendship. He does not want to bring on himself the troubles of human enmity. See, the wolf has caught a sheep by the throat: the devil has lured a believer into adultery. You hold your peace. You give no reproof. O hireling, you have seen the wolf coming, and you have fled! Perhaps he answers, Look, I am here; I have not fled. You have fled, because you have kept silent. You have kept silent, because you were afraid. The flight of the mind is fear.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Tractate 46 on the Gospel of John (NPNF Tractate XLVI), section 8; "
                    "English at cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, "
                    "lines 7236-7237; Latin at "
                    "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
                    "lines 29570-29578",
          "license": "public-domain"}],
        2,
        ["participant asks about John 10:11-13, the good shepherd and the hireling",
         "participant asks what Augustine meant by a leader who flees when he sees the "
         "wolf",
         "participant asks what a leader owed a believer who was sinning"],
        ["participant asks how a bishop spoke of the account he must give for his people "
         "-- lpc.quote.ye-belong-to-my-care gives that"],
        ["The passage does not say that every paid or office-holding person is a hireling; "
         "the hireling is the one who seeks 'his own, not the things that are Jesus "
         "Christ's'.",
         "The sentences before it, about rebuking and excommunicating an offender, are "
         "outside the passage; it speaks only of silence out of fear.",
         "It names no bishop or place and does not date the sermon."],
        "Augustine, Tractate 46 on the Gospel of John (NPNF Tractate XLVI), section 8. "
        "English in the NPNF translation at "
        "cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, lines 7236-7237. Latin "
        "at "
        "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
        "lines 29570-29578 (OCR text). The first sentences of section 8, which say the "
        "hireling does not venture to rebuke an offender and fears that an excommunicated "
        "man will turn enemy, are left out; so are the sentences after 'The flight of the mind is fear', which contrast standing in body with fleeing in spirit and quote Colossians 2:5. In the Latin, Fuga "
        "animi, timor est is 'the flight of the mind is fear', and tacet, non corripit is "
        "'he is silent and does not rebuke'. The passage carries the gravity "
        "lpc.gravity.pastoral-office-flock-keeping.",
    )

    emit_quote(
        "let-it-be-the-office-of-love-to-feed-the-flock",
        "Let it be the office of love to feed the Lord’s flock, if it was the signal of "
        "fear to deny the Shepherd. Those who have this purpose in feeding the flock of "
        "Christ, that they may have them as their own, and not as Christ’s, are convicted "
        "of loving themselves, and not Christ, from the desire either of boasting, or "
        "wielding power, or acquiring gain, and not from the love of obeying, serving, and "
        "pleasing God.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'office' as a post or a rank. The Latin officium is a "
        "duty. Augustine says feeding the Lord's flock is the duty of love, set against "
        "Peter's denial out of fear, and he warns that anyone who feeds the flock as his "
        "own, for boasting, power or gain, loves himself and not Christ.",
        "Let it be the duty of love to feed the Lord’s flock, if it was the mark of fear to deny the Shepherd. Some feed the flock of Christ with this aim: to have the sheep as their own, and not as Christ’s. They are shown to love themselves, and not Christ. They act from the wish to boast, or to hold power, or to make gain. They do not act from the love of obeying, serving and pleasing God.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Tractate 123 on the Gospel of John (NPNF Tractate CXXIII), section 5; "
                    "English at cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, "
                    "line 13429; Latin at "
                    "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
                    "lines 46148-46154",
          "license": "public-domain"}],
        1,
        ["participant asks about John 21:15-17, 'Feed my sheep'",
         "participant asks what it meant to feed the Lord's flock",
         "participant asks what Augustine said was wrong in a leader who feeds the flock "
         "for his own gain"],
        ["participant asks how Peter was put right after denying the Lord -- "
         "lpc.quote.peter-the-sick-man-and-the-physician gives that"],
        ["The passage does not say that Peter was given authority over the other apostles "
         "or the whole Church; it speaks of the duty of those who feed Christ's flock.",
         "It names no bishop, priest or rank; 'those who have this purpose' is anyone who "
         "feeds Christ's sheep.",
         "The words 'Lovest thou me? Feed my sheep' come in the next sentences, outside "
         "the passage, which does not quote them."],
        "Augustine, Tractate 123 on the Gospel of John (NPNF Tractate CXXIII), section 5. "
        "English in the NPNF translation at "
        "cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, line 13429. Latin at "
        "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
        "lines 46148-46154 (OCR text). The first sentence of section 5, on the Lord asking "
        "three times and the threefold confession answering the threefold denial, is left "
        "out; so are the sentences after 'pleasing God', which explain the words 'Lovest "
        "thou me? Feed my sheep' and list the 'lovers of their own selves'. In the Latin, "
        "Sit amoris officium, pascere dominicum gregem is 'let it be the duty of love to "
        "feed the Lord's flock'. The passage carries the gravity "
        "lpc.gravity.pastoral-office-flock-keeping.",
    )

    emit_quote(
        "love-and-do-what-thou-wilt",
        "A father beats a boy, and a boy-stealer caresses. If thou name the two things, "
        "blows and caresses, who would not choose the caresses, and decline the blows? If "
        "thou mark the persons, it is charity that beats, iniquity that caresses. See what "
        "we are insisting upon; that the deeds of men are only discerned by the root of "
        "charity. For many things may be done that have a good appearance, and yet proceed "
        "not from the root of charity. For thorns also have flowers: some actions truly "
        "seem rough, seem savage; howbeit they are done for discipline at the bidding of "
        "charity. Once for all, then, a short precept is given thee: Love, and do what "
        "thou wilt: whether thou hold thy peace, through love hold thy peace; whether thou "
        "cry out, through love cry out; whether thou correct, through love correct; "
        "whether thou spare, through love do thou spare: let the root of love be within, "
        "of this root can nothing spring but what is good.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'do what thou wilt' as leave to do anything. Augustine "
        "puts the line at the end of an argument that the root decides the deed: a father "
        "beats a boy out of love, and a boy-stealer caresses him out of wrong. So the rule "
        "is to let love be the root, and then whether you keep silent, cry out, correct or "
        "spare, you do it through love.",
        "A father beats a boy, and a slave-dealer caresses him. Name the two things, blows and caresses: who would not choose the caresses and refuse the blows? Look at the persons: it is love that beats, and wickedness that caresses. See what we are pressing on you. People’s deeds are told apart only by the root of love. For many things may be done that look good, and yet do not come from the root of love. Thorns have flowers too. Some actions seem rough, even savage. Yet they are done to train and correct, at love’s bidding. So once and for all, you are given a short rule: Love, and do what you will. If you keep silent, keep silent from love. If you cry out, cry out from love. If you correct, correct from love. If you spare, spare from love. Let the root of love be within you. From this root nothing can grow but what is good.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. 'Boy-stealer' renders mango, "
             "a dealer in slaves who fawns on a boy to take him. 'Charity' renders "
             "caritas, while the short command uses the verb dilige and 'love' is "
             "dilectio."),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Homily 7 on the First Epistle of John (NPNF Homily VII), section 8; "
                    "English at cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, "
                    "lines 15529-15531; Latin at "
                    "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
                    "lines 50812-50829",
          "license": "public-domain"}],
        1,
        ["participant asks about Augustine's 'Love, and do what thou wilt', from his homily on 1 John 4",
         "participant asks what Augustine meant by 'love, and do what you want'",
         "participant asks how Augustine said a harsh act could come from love"],
        ["participant asks how Augustine said to correct and yet forgive -- "
         "lpc.quote.reprove-and-forgive-the-surgeons-knife gives that"],
        ["The line is not a licence: the passage says deeds are known by their root, and "
         "that from the root of love nothing can spring but what is good.",
         "The passage does not describe church discipline or excommunication; 'correct' "
         "and 'spare' are named only as acts that love may do.",
         "The two sentences before it, which say that where deeds differ we find a man "
         "'made fierce' by love and 'winningly gentle' by wrong, are outside the passage.",
         "The father who beats a boy is Augustine's image of correction from love; it must not be used to excuse striking a child or anyone else today."],
        "Augustine, Homily 7 on the First Epistle of John (NPNF Homily VII), section 8. "
        "English in the NPNF translation at "
        "cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, lines 15529-15531. "
        "Latin at "
        "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
        "lines 50812-50829 (OCR text). The passage is the second half of section 8. The "
        "two sentences before it, which say that where deeds differ we find a man made "
        "fierce by love and winningly gentle by wrong, are left out, and so is everything "
        "after 'what is good'. In "
        "the Latin the precept reads Dilige, et quod vis fac, and radix sit intus "
        "dilectionis, non potest de ista radice nisi bonum existere is 'let the root of "
        "love be within; from that root nothing can spring but good'. The passage carries "
        "the gravity lpc.gravity.penitential-discipline in its form of correction from "
        "love.",
    )

    emit_quote(
        "they-went-out-from-us-but-were-not-of-us",
        "“They went out from us; but,” be not sad, “they were not of us.” How provest thou "
        "this? If they had been of us, they would doubtless have continued with us. Hence "
        "therefore ye may see, that many who are not of us, receive with us the "
        "Sacraments, receive with us baptism. receive with us what the faithful know they "
        "receive, Benediction, the Eucharist, and whatever there is in Holy Sacraments: "
        "the communion of the very altar they receive with us, and are not of us. "
        "Temptation proves that they are not of us. When temptation comes to them as if "
        "blown by a wind they fly abroad; because they were not grain.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'they were not of us' as a harsh verdict on people who "
        "left. Augustine offers it as comfort to those who grieve. He says that many who are not 'of us' share the same baptism and the same altar, and that temptation shows it, as a wind shows what was not grain.",
        "“They went out from us; but,” do not be sad, “they were not of us.” How do you prove this? If they had been of us, they would surely have stayed with us. From this you can see that many who are not of us receive the sacraments with us. They receive baptism with us. They receive with us what the faithful know they receive: the blessing, the Eucharist, and whatever there is in the holy sacraments. They receive the communion of the very altar with us, and they are not of us. Temptation proves that they are not of us. When temptation comes, they fly off as if blown by a wind, because they were not grain.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Homily 3 on the First Epistle of John (NPNF Homily III), section 5; "
                    "English at cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, "
                    "lines 14469-14472; Latin at "
                    "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
                    "lines 48396-48407",
          "license": "public-domain"}],
        2,
        ["participant asks about 1 John 2:19, 'They went out from us, but they were not of "
         "us'",
         "participant asks how Augustine comforted people when others left the church",
         "participant asks how someone could share the sacraments and still not be 'of us'"],
        ["participant asks how Augustine said to live with bad members inside one church "
         "-- lpc.quote.apart-in-heart-united-in-body gives that"],
        ["The passage gives no verdict on any named person or group; the sentence after it "
         "says the final sorting comes in the day of judgment.",
         "It does not name the Donatists; the homily names them in a later section, in "
         "section 7.",
         "An editor's note at line 14471, on a manuscript reading of 'Benediction, the "
         "Eucharist', is inside the line range and is not part of the passage.",
         "The same section, outside the passage, says that those who went out and return are not antichrists, and that whoever changes for the better is in the body; the passage must not be used as a verdict on anyone who has left."],
        "Augustine, Homily 3 on the First Epistle of John (NPNF Homily III), section 5. "
        "English in the NPNF translation at "
        "cic/texts/npnf107_augustine-homilies-john-soliloquies.xml, lines 14469-14472. "
        "Latin at "
        "cic/texts/augustine_in-ioannis-evangelium-tractatus-lat_migne-garnier1902-t3-pt2.txt, "
        "lines 48396-48407 (OCR text). The sentences before the passage in section 5 are "
        "left out, and so is everything after 'because they were not grain', which says "
        "the final sorting comes at the fanning of the threshing-floor in the day of "
        "judgment. The editor's note at line 14471 reads 'Two mss. Benedictionem "
        "Eucharistiae' and is not part of the passage. In the Latin, grana is 'grain' (the "
        "OCR runs several words together in this stretch), and the sacraments named are "
        "Baptismum, Benedictionem and Eucharistiam. The passage carries the gravity "
        "lpc.gravity.collegial-communion-preserved.",
    )

    emit_quote(
        "many-have-learned-to-offer-the-other-cheek",
        "For many have learned how to offer the other cheek, but do not know how to love "
        "him by whom they are struck. But in truth, the Lord Himself, who certainly was "
        "the first to fulfil the precepts which He taught, did not offer the other cheek "
        "to the servant of the high priest when smiting Him thereon; but, so far from "
        "that, said, “If I have spoken evil, hear witness of the evil; but if well, why "
        "smitest thou me?” Yet was He not on that account unprepared in heart, for the "
        "salvation of all, not merely to be smitten on the other cheek, but even to have "
        "His whole body crucified.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern reader may take 'turn the other cheek' as a rule to accept any blow. "
        "Augustine says many have learned to offer the other cheek but not to love the one "
        "who strikes. He adds that the Lord himself, struck, did not offer the other cheek "
        "but answered, yet was ready in heart to be crucified. The command is about "
        "readiness of heart, not a show.",
        "For many have learned how to offer the other cheek, but do not know how to love the one who strikes them. But in truth the Lord Himself was surely the first to keep the commands He taught. Yet He did not offer the other cheek to the high priest’s servant who struck Him there. Far from it, He said, “If I have spoken evil, bear witness of the evil; but if well, why do you strike me?” Yet He was not, for that reason, unready in heart for the salvation of all. He was ready not only to be struck on the other cheek, but even to have His whole body crucified.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. No Latin of De sermone Domini "
             "in monte is vendored in the Library, so the English was not checked against the Latin. NPNF's 'hear witness' is a misprint for 'bear witness', which the rendering uses; the note at line 1668 gives Augustine's Latin reading, Exprobra de malo, 'charge me with the evil'."),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Our Lord's Sermon on the Mount, Book I, chapter XIX, section 58; "
                    "English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 1666-1672; no Latin of this work is vendored",
          "license": "public-domain"}],
        1,
        ["participant asks about Matthew 5:39, 'turn the other cheek'",
         "participant asks whether a Christian had to accept every blow without answering",
         "participant asks how Augustine said Jesus himself acted when he was struck"],
        [],
        ["The passage does not take up self-defence or lawsuits and must not be given as Augustine's ruling on them; later sections, outside it, say correction out of love is not forbidden.",
         "It does not say the Lord answered in anger; it says he was ready in heart for "
         "more.",
         "It does not take up lawsuits, the coat or the mile; those come in the next "
         "sections, 59 to 61.",
         "The passage must not be used to tell anyone to stay where they are being harmed or to accept a blow now."],
        "Augustine, Our Lord's Sermon on the Mount, Book I, chapter XIX, section 58. "
        "English in the NPNF translation at "
        "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, lines "
        "1666-1672. Two notes sit inside the line range and are not part of the passage: "
        "one at line 1668 giving the Latin readings of John 18:23 (Exprobra de malo; "
        "Vulgate, testimonium perhibe de malo), and a Bible reference at line 1671. The "
        "earlier part of section 58, on what the right cheek means and on Paul as a Roman "
        "citizen, is left out. No Latin of De sermone Domini in monte is vendored in the "
        "Library, so no Latin lines are given and the English was not checked against the "
        "Latin. The passage carries the gravity lpc.gravity.preaching-and-catechesis through its teaching on the Lord's precept.",
    )

    emit_quote(
        "all-sins-against-us-are-to-be-forgiven",
        "But, on the other hand, by that precept whereby we are enjoined to pray for our "
        "enemies, it is not for those who ask pardon that we are enjoined to pray. For "
        "those who are already in such a state of mind are no longer enemies. By no "
        "possibility, however, could one truthfully say that he prays for one whom he has "
        "not pardoned. And therefore we must confess that all sins which are committed "
        "against us are to be forgiven, if we wish those to be forgiven by our Father "
        "which we commit against Him.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear this as a rule about being nice. Augustine says that "
        "anyone who prays for his enemies must truly have pardoned them, and that all sins "
        "committed against us are to be forgiven, if we want the sins we commit against "
        "the Father forgiven. Section 28, just before, explains that 'debts' means every sin done against us.",
        "On the other hand, the command to pray for our enemies does not tell us to pray for those who ask pardon. People already in that state of mind are no longer enemies. But no one could truthfully say that he prays for someone he has not pardoned. So we must admit that every sin committed against us is to be forgiven. That holds if we want our Father to forgive the sins we commit against Him.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. No Latin of De sermone Domini "
             "in monte is vendored in the Library, so the English was not checked against "
             "the Latin."),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Our Lord's Sermon on the Mount, Book II, chapter VIII, section 29; "
                    "English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 2333-2334; no Latin of this work is vendored",
          "license": "public-domain"}],
        2,
        ["participant asks about Matthew 6:12, 'forgive us our debts, as we forgive our "
         "debtors'",
         "participant asks what Augustine said about forgiving enemies in the Lord's "
         "Prayer",
         "participant asks whether praying for an enemy meant truly forgiving him"],
        ["participant asks how Augustine said to correct and yet forgive -- "
         "lpc.quote.reprove-and-forgive-the-surgeons-knife gives that"],
        ["The passage does not speak of money debts; section 28, outside it, says 'debts' in the petition covers every way anyone sins against us, a withheld money debt included.",
         "It does not say that forgiving means the offender goes uncorrected; section 28, just before it, allows a creditor to press gently for what is owed so as to bring the debtor to what is right.",
         "It does not describe penance or readmission to communion; it speaks of the "
         "petition in the Lord's Prayer.",
         "The passage must not be used to press anyone to forgive, or to keep company with, a person who is harming them now."],
        "Augustine, Our Lord's Sermon on the Mount, Book II, chapter VIII, section 29. "
        "English in the NPNF translation at "
        "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, lines "
        "2333-2334. The first sentence of section 29, on those who ask pardon, and the "
        "last sentence, 'For the subject of revenge has been sufficiently discussed "
        "already, as I think', are left out; the passage begins at 'But, on the other "
        "hand' and ends before the last sentence. No Latin of De sermone Domini in monte "
        "is vendored in the Library, so no Latin lines are given and the English was not "
        "checked against the Latin. The passage carries the gravity "
        "lpc.gravity.penitential-discipline.",
    )

    emit_quote(
        "judge-not-nor-despair-of-a-return",
        "Let us not therefore reprove those things about which we do not know with what "
        "intention they are done; nor let us so reprove those things which are manifest, "
        "as that we should despair of a return to a right state of mind; and thus we shall "
        "avoid the judgment of which in the present instance it is said, “Judge not, that "
        "ye be not judged.”",
        "lpc.figure.augustine",
        "verbatim",
        "A modern reader may take 'Judge not' as a ban on every moral judgment. Augustine "
        "names two limits: do not reprove what you cannot know the intention of, and do "
        "not reprove plain faults as if the person could never change. Hope of a return to "
        "a right mind is not to be given up.",
        "So let us not rebuke things when we do not know the intention behind them. And let us not rebuke plain faults in such a way that we give up hope of the person’s return to a right mind. In this way we shall avoid the judgment of which it is said here, “Judge not, that you be not judged.”",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. No Latin of De sermone Domini "
             "in monte is vendored in the Library, so the English was not checked against "
             "the Latin."),
        [{"source_id": "lpc.source.augustine-tractates-on-john-and-related-exegesis",
          "locus": "Our Lord's Sermon on the Mount, Book II, chapter XVIII, section 61; "
                    "English at "
                    "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, "
                    "lines 2888-2889; no Latin of this work is vendored",
          "license": "public-domain"}],
        2,
        ["participant asks about Matthew 7:1, 'Judge not, that ye be not judged'",
         "participant asks what Augustine said 'Judge not' forbids and does not forbid",
         "participant asks how to reprove a fault without giving up on the person"],
        ["participant asks how Augustine said to correct and yet forgive -- "
         "lpc.quote.reprove-and-forgive-the-surgeons-knife gives that"],
        ["The passage does not forbid judging what is plainly wrong; sections 59 and 60, "
         "outside it, say manifest sins may be judged.",
         "The examples that come before it in section 61, a man who will not fast because "
         "of his stomach and a plain glutton and drunkard, are not in the passage.",
         "It does not describe a church court, excommunication or penance.",
         "The passage must not be used to tell anyone to keep hoping for, or to stay near, a person who is harming them now."],
        "Augustine, Our Lord's Sermon on the Mount, Book II, chapter XVIII, section 61. "
        "English in the NPNF translation at "
        "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml, lines "
        "2888-2889. The first sentences of section 61 are left out: the statement that "
        "there are two things in which we must beware of rash judgment, and the two "
        "examples, the man excused from fasting by his stomach and the manifest glutton "
        "and drunkard. The passage is the closing sentence of the section. No Latin of De "
        "sermone Domini in monte is vendored in the Library, so no Latin lines are given "
        "and the English was not checked against the Latin. The passage carries the "
        "gravity lpc.gravity.penitential-discipline in its form of reproof that keeps hope "
        "of a return.",
    )


# ===========================================================================
# DISCLOSURE QUOTES (17) -- what the bishops held on hell, judgment, the dead, infants and
# suicide, the hard parts included, one per passage.
# ===========================================================================

NPNF102 = "cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml"
NPNF103 = "cic/texts/npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml"
NPNF105 = "cic/texts/npnf105_augustine-anti-pelagian-writings.xml"
ENCH_LAT = "cic/texts/augustine_doctrina-christiana-enchiridion-lat_bruder1838.txt"
COG_LAT = "cic/texts/augustine_civitate-dei-1-13-lat_hoffmann-csel40-1.txt"
DEMETR_LAT = "cic/texts/cyprian_ad-demetrianum-lat_hartel1868-csel3-tei.txt"


def build_disclosure_quotes() -> None:
    emit_quote(
        "the-life-and-the-death-shall-both-be-without-end",
        "After the resurrection, however, when the final, universal judgment has been completed, "
        "there shall be two kingdoms, each with its own distinct boundaries, the one Christ’s, the "
        "other the devil’s; the one consisting of the good, the other of the bad,—both, however, "
        "consisting of angels and men. The former shall have no will, the latter no power, to sin, "
        "and neither shall have any power to choose death; but the former shall live truly and "
        "happily in eternal life, the latter shall drag a miserable existence in eternal death "
        "without the power of dying; for the life and the death shall both be without end. But among "
        "the former there shall be degrees of happiness, one being more pre-eminently happy than "
        "another; and among the latter there shall be degrees of misery, one being more endurably "
        "miserable than another.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may expect a vague warning. Augustine sets out two kingdoms after the "
        "final judgment. In the second, the bad 'drag a miserable existence in eternal death' and "
        "cannot die. So the life of one kingdom and the death of the other 'shall both be "
        "without end'. He also says there are 'degrees of misery', some 'more endurably miserable "
        "than another'.",
        "After the resurrection, when the final judgment of all has been completed, there will be two kingdoms. Each will have its own clear boundaries. One is Christ’s, the other the devil’s. One is made up of the good, the other of the bad. Both are made up of angels and human beings. The first will have no will to sin, and the second no power to sin. Neither will have any power to choose death. The first will live truly and happily in eternal life. The second will drag out a wretched existence in eternal death, without the power of dying. For both the life and the death will be without end. Among the first there will be degrees of happiness, one happier than another. Among the second there will be degrees of misery, one more bearable than another.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-the-enchiridion",
          "locus": f"Enchiridion, chapter 111 (chapter CXI in the Latin); English at {NPNF103}, lines "
                   f"23591-23604; Latin at {ENCH_LAT}, lines 12467-12478",
          "license": "public-domain"}],
        1,
        ["participant asks whether we believed in hell and what it was",
         "participant asks whether the punishment of the lost would ever end",
         "participant asks whether all the lost were thought to suffer alike"],
        [],
        ["The passage does not say who will be among the lost; it names only 'the good' and 'the "
         "bad', 'both, however, consisting of angels and men', and the speaker must not name any "
         "person or group as lost.",
         "The speaker must not say the punishment ends or fades; the passage says the life and the "
         "death 'shall both be without end'.",
         "The passage does not describe the torments or say where they are; the speaker must not "
         "supply a description as if quoted.",
         "If a participant speaks of a person close to them who has died, the speaker must not say "
         "or suggest that this person is among the lost.",
         "The record says nothing about suicide; the speaker must not join it with "
         "lpc.witness.no-one-may-take-his-own-life to say or suggest what became of anyone who died "
         "that way.",
         "The passage carries no date for the Enchiridion, and the speaker must not supply one."],
        "Augustine, Enchiridion, chapter 111 (chapter CXI in the Latin text). English in the NPNF "
        f"translation at {NPNF103}, lines 23591-23604. Latin (Bruder, 1838) at {ENCH_LAT}, lines "
        "12467-12478 (OCR text, with misreads). The passage is the whole of chapter 111. In the "
        "Latin, in aeterna morte sine moriendi potestate is 'in eternal death without the power of "
        "dying' and utrique sine fine is 'both without end'. The passage carries the witness "
        "lpc.witness.punishment-without-end.",
    )

    emit_quote(
        "very-many-make-moan-over-the-eternal-punishment",
        "It is in vain, then, that some, indeed very many, make moan over the eternal punishment, "
        "and perpetual, unintermitted torments of the lost, and say they do not believe it shall be "
        "so; not, indeed, that they directly oppose themselves to Holy Scripture, but, at the "
        "suggestion of their own feelings, they soften down everything that seems hard, and give a "
        "milder turn to statements which they think are rather designed to terrify than to be "
        "received as literally true.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may think doubt about hell is a modern thing. Augustine says some, "
        "'indeed very many', in his own time did not believe the punishment of the lost would be "
        "eternal. He says they did not set themselves against Scripture. They 'soften down "
        "everything that seems hard'. He calls this 'in vain'.",
        "So it is in vain that some, indeed very many, lament the eternal punishment and the endless, unbroken torments of the lost. They say they do not believe it will be so. They do not set themselves directly against Holy Scripture. But, prompted by their own feelings, they soften everything that seems hard. They give a milder sense to sayings they think were meant more to frighten than to be taken as literally true.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. Its 'make moan over' renders the Latin "
             "miserantur, which means pity or feel compassion for. The people he answers feel pity for "
             "the lost, and he says that pity is 'in vain'."),
        [{"source_id": "lpc.source.augustine-the-enchiridion",
          "locus": "Enchiridion, chapter 112 (chapter CXII in the Latin), opening sentence; English at "
                   f"{NPNF103}, lines 23613-23620; Latin at {ENCH_LAT}, lines 12480-12497",
          "license": "public-domain"}],
        1,
        ["participant asks whether anyone among us doubted that the punishment of the lost would last "
         "forever",
         "participant asks how Augustine answered people who found eternal punishment too hard to "
         "believe"],
        [],
        ["The passage does not say how many held the doubt or where; it says 'some, indeed very many'.",
         "The speaker must not say Augustine allowed the doubters to be right; he calls their pity "
         "'in vain'.",
         "The passage does not say what reasons Augustine answers with; they come after it in chapter "
         "112, and the speaker must not supply them as if quoted here.",
         "If a participant speaks of a person close to them who has died, the speaker must not say "
         "or suggest that this person is among the lost.",
         "The record says nothing about suicide; the speaker must not join it with "
         "lpc.witness.no-one-may-take-his-own-life to say or suggest what became of anyone who died "
         "that way.",
         "The passage carries no date for the Enchiridion, and the speaker must not supply one."],
        "Augustine, Enchiridion, chapter 112 (chapter CXII in the Latin text), the first sentence. "
        f"English in the NPNF translation at {NPNF103}, lines 23613-23620. Latin (Bruder, 1838) at "
        f"{ENCH_LAT}, lines 12480-12497 (OCR text, with misreads; a page break and footnotes at lines "
        "12482-12490 sit inside the range and are not part of the passage). In the Latin, Frustra "
        "itaque nonnulli, immo quam plurimi is 'in vain, then, some, indeed very many', and humano "
        "miserantur adfectu is 'they pity from human feeling'. The rest of chapter 112 is left out. "
        "The passage carries the witness lpc.witness.punishment-without-end.",
    )

    emit_quote(
        "a-respite-from-their-torments",
        "But let them suppose, if the thought gives them pleasure, that the pains of the damned are, "
        "at certain intervals, in some degree assuaged. For even in this case the wrath of God, that "
        "is, their condemnation (for it is this, and not any disturbed feeling in the mind of God "
        "that is called His wrath), abideth upon them; that is, His wrath, though it still remains, "
        "does not shut up His tender mercies; though His tender mercies are exhibited, not in "
        "putting an end to their eternal punishment, but in mitigating, or in granting them a "
        "respite from, their torments;",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may take this as Augustine softening the doctrine. He lets the doubters "
        "suppose, 'if the thought gives them pleasure', that the pains of the damned are eased at "
        "times. He says God's wrath still stays on them. God's mercy is shown 'not in putting an end "
        "to their eternal punishment, but in mitigating, or in granting them a respite from, their "
        "torments'.",
        "But let them suppose, if the thought pleases them, that the pains of the damned are eased in some degree, at certain intervals. Even then the wrath of God stays upon them, that is, their condemnation. It is this that is called His wrath, not any troubled feeling in the mind of God. His wrath remains, yet it does not lock away His tender mercies. But His tender mercies are not shown by ending their eternal punishment. They are shown by easing their torments, or by granting them a respite from them.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-the-enchiridion",
          "locus": "Enchiridion, chapter 112 (chapter CXII in the Latin), the sentences on mitigation; English "
                   f"at {NPNF103}, lines 23632-23641; Latin at {ENCH_LAT}, lines 12508-12516",
          "license": "public-domain"}],
        2,
        ["participant asks whether Augustine allowed that the lost might get some relief",
         "participant asks whether the punishment of the lost could ever be eased or end"],
        [],
        ["The passage does not say the punishment ends; it says God's mercy is shown 'not in putting "
         "an end to their eternal punishment'.",
         "The speaker must not give the relief as Augustine's settled teaching; he allows it as a "
         "supposition 'if the thought gives them pleasure', and in chapter 113, outside the passage, "
         "he says the death of the wicked 'shall abide for ever'.",
         "The passage does not say how long any relief lasts or how often it comes beyond 'at certain "
         "intervals'.",
         "If a participant speaks of a person close to them who has died, the speaker must not say "
         "or suggest that this person is among the lost.",
         "The record says nothing about suicide; the speaker must not join it with "
         "lpc.witness.no-one-may-take-his-own-life to say or suggest what became of anyone who died "
         "that way.",
         "The passage carries no date for the Enchiridion, and the speaker must not supply one."],
        "Augustine, Enchiridion, chapter 112 (chapter CXII in the Latin text), from 'But let them "
        f"suppose' to 'their torments;'. English in the NPNF translation at {NPNF103}, lines "
        f"23632-23641. Latin (Bruder, 1838) at {ENCH_LAT}, lines 12508-12516 (OCR text, with "
        "misreads). Two scripture-reference notes inside the range, one after 'abideth upon them;' "
        "and one after 'in His anger', are not part of the passage and are left out. The sentences "
        "before it (the 'vessels of mercy' and the reading of 'these shall go away into everlasting "
        "punishment') and after it (the greatness of being lost out of the kingdom of God) are left "
        "out. In the Latin, sed levamen adhibendo, vel interponendo cruciatibus is 'but by applying "
        "relief, or putting a break between the torments'. The passage carries the witness "
        "lpc.witness.punishment-without-end.",
    )

    emit_quote(
        "left-doubtful-a-kind-of-purgatorial-fire",
        "And it is not impossible that something of the same kind may take place even after this "
        "life. It is a matter that may be inquired into, and either ascertained or left doubtful, "
        "whether some believers shall pass through a kind of purgatorial fire, and in proportion as "
        "they have loved with more or less devotion the goods that perish, be less or more quickly "
        "delivered from it. This cannot, however, be the case of any of those of whom it is said, "
        "that they “shall not inherit the kingdom of God,” unless after suitable repentance their "
        "sins be forgiven them.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may take 'purgatorial fire' for the later Church doctrine of purgatory. "
        "Augustine does not teach that here. He says whether some believers pass through such a fire "
        "'may be inquired into, and either ascertained or left doubtful'. He adds that it cannot "
        "help those who 'shall not inherit the kingdom of God' unless they repent and are forgiven.",
        "And it is not impossible that something of the same kind may happen even after this life. Whether some believers will pass through a kind of purging fire may be asked. It may be found out, or it may stay unknown. Some would be freed from it more quickly, some more slowly. The more they loved the goods that perish, the more slowly they would be freed. But this cannot be the case for any of those of whom it is said that they “shall not inherit the kingdom of God.” The one exception is if, after fitting repentance, their sins are forgiven them.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. Its 'left doubtful' renders the Latin "
             "latere, which means to lie hidden, so the sense is that the matter may be found out or may "
             "stay unknown."),
        [{"source_id": "lpc.source.augustine-the-enchiridion",
          "locus": "Enchiridion, chapter 69 (chapter LXIX in the Latin), first three sentences; English at "
                   f"{NPNF103}, lines 22301-22310; Latin at {ENCH_LAT}, lines 11202-11209",
          "license": "public-domain"}],
        1,
        ["participant asks whether we believed in purgatory",
         "participant asks what Augustine said about a purifying fire after death"],
        [],
        ["The passage does not teach purgatory as settled; its words are 'may be inquired into, and "
         "either ascertained or left doubtful', and the speaker must not say Augustine taught it as a "
         "doctrine.",
         "'Something of the same kind' looks back to chapter 68, outside the passage, where a "
         "believer who loses what he loved is saved 'so as by fire'; the speaker must not supply that "
         "as if quoted.",
         "The passage does not say what the fire is, how long it lasts or which believers pass "
         "through it beyond 'some'.",
         "The passage carries no date for the Enchiridion, and the speaker must not supply one."],
        "Augustine, Enchiridion, chapter 69 (chapter LXIX in the Latin text), the first three "
        f"sentences. English in the NPNF translation at {NPNF103}, lines 22301-22310. Latin (Bruder, "
        f"1838) at {ENCH_LAT}, lines 11202-11209 (OCR text, with misreads). A scripture-reference "
        "note after 'kingdom of God,' sits inside the range and is left out. The last sentence of "
        "chapter 69, on almsgiving and the sheep and the goats, is left out. In the Latin, ignem "
        "quemdam purgatorium is 'a certain purgatorial fire' and aut inveniri, aut latere is 'either "
        "be found out, or lie hidden'. The passage carries the witness "
        "lpc.witness.judged-on-the-life-lived-here.",
    )

    emit_quote(
        "not-to-purchase-impunity",
        "We must beware, however, lest any one should suppose that gross sins, such as are committed "
        "by those who shall not inherit the kingdom of God, may be daily perpetrated, and daily "
        "atoned for by almsgiving. The life must be changed for the better; and almsgiving must be "
        "used to propitiate God for past sins, not to purchase impunity for the commission of such "
        "sins in the future. For He has given no man license to sin, although in His mercy He may "
        "blot out sins that are already committed, if we do not neglect to make proper satisfaction.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear almsgiving as a payment that buys off sin. Augustine says the "
        "life 'must be changed for the better'. Almsgiving serves 'to propitiate God for past sins, "
        "not to purchase impunity' for sins to come. God may still blot out sins already committed "
        "'if we do not neglect to make proper satisfaction'.",
        "We must take care, though. No one should suppose that grave sins may be committed every day and atoned for every day by almsgiving. These are sins such as those committed by people who will not inherit the kingdom of God. The life must be changed for the better. Almsgiving must be used to seek God’s mercy for past sins. It must not be used to buy freedom from punishment for committing such sins in the future. For He has given no one leave to sin. Yet in His mercy He may blot out sins already committed, if we do not neglect to make proper amends.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-the-enchiridion",
          "locus": "Enchiridion, chapter 70 (chapter LXX in the Latin), the whole chapter; English at "
                   f"{NPNF103}, lines 22327-22335; Latin at {ENCH_LAT}, lines 11218-11227",
          "license": "public-domain"}],
        2,
        ["participant asks whether giving to the poor could pay for sin",
         "participant asks whether Augustine thought a person could sin freely and then give alms to "
         "cancel it"],
        ["participant asks how Cyprian taught that almsgiving cures sin -- "
         "lpc.witness.almsgiving-quenches-sin gives that"],
        ["The passage does not say what any sin costs or how much to give; the speaker must not set a "
         "price, since it says the life 'must be changed for the better'.",
         "The speaker must not say Augustine thought almsgiving counts for nothing; the passage says "
         "God 'may blot out sins that are already committed, if we do not neglect to make proper "
         "satisfaction'.",
         "The passage does not say what 'gross sins' are beyond 'those who shall not inherit the "
         "kingdom of God', and the speaker must not supply a list.",
         "The passage carries no date for the Enchiridion, and the speaker must not supply one."],
        "Augustine, Enchiridion, chapter 70 (chapter LXX in the Latin text). English in the NPNF "
        f"translation at {NPNF103}, lines 22327-22335. Latin (Bruder, 1838) at {ENCH_LAT}, lines "
        "11218-11227 (OCR text, with misreads; the footnotes after the chapter are not part of it). "
        "The passage is the whole of chapter 70. A scripture-reference note after 'license to sin,' "
        "sits inside the range and is left out. In the Latin, non ad hoc emendus quodam modo, ut ea "
        "semper liceat impune committere is 'not to be bought, as it were, so that those sins may "
        "always be done with impunity'. The passage carries the witness "
        "lpc.witness.judged-on-the-life-lived-here.",
    )

    emit_quote(
        "the-mildest-punishment-of-all",
        "And neither the first death, which takes place when the soul is compelled to leave the "
        "body, nor the second death, which takes place when the soul is not permitted to leave the "
        "suffering body, would have been inflicted on man had no one sinned. And, of course, the "
        "mildest punishment of all will fall upon those who have added no actual sin, to the "
        "original sin they brought with them; and as for the rest who have added such actual sins, "
        "the punishment of each will be the more tolerable in the next world, according as his "
        "iniquity has been less in this world.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may not expect to hear this said so plainly. Augustine says 'the mildest "
        "punishment of all' will fall on those who have 'added no actual sin, to the original sin "
        "they brought with them'. He says the punishment of the rest will be 'more tolerable' the "
        "less iniquity they added in this world. He calls it punishment.",
        "Neither the first death nor the second would have been laid on humankind if no one had sinned. The first death happens when the soul is forced to leave the body. The second happens when the soul is not allowed to leave the suffering body. And, of course, the mildest punishment of all will fall on some. They are those who have added no sin of their own to the original sin they were born with. Others have added sins of their own. In the next world each one’s punishment will be more bearable, the less his wickedness was in this world.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-the-enchiridion",
          "locus": "Enchiridion, chapter 93 (chapter XCIII in the Latin), the whole chapter; English at "
                   f"{NPNF103}, lines 22998-23007; Latin at {ENCH_LAT}, lines 11867-11875",
          "license": "public-domain"}],
        1,
        ["participant asks what happens to babies who died unbaptized",
         "participant asks how Augustine judged those who die with only original sin",
         "participant asks whether punishment in the next world was the same for everyone"],
        ["participant asks specifically about babies who died unbaptized -- "
         "lpc.quote.the-mildest-condemnation-of-all gives that"],
        ["The passage does not name infants or mention baptism; the speaker must not say it does. "
         "Chapter 43 of the same book says infants 'die only to original sin' in baptism, and uses "
         "the same words, 'the sin which they brought with them'.",
         "The speaker must not call the punishment anything but punishment; the passage's word is "
         "'the mildest punishment of all'.",
         "The passage does not describe the punishment or say where it is, and it does not use the "
         "word limbo; the speaker must not supply either.",
         "The passage carries no date for the Enchiridion, and the speaker must not supply one."],
        "Augustine, Enchiridion, chapter 93 (chapter XCIII in the Latin text). English in the NPNF "
        f"translation at {NPNF103}, lines 22998-23007. Latin (Bruder, 1838) at {ENCH_LAT}, lines "
        "11867-11875 (OCR text, with misreads; the Latin prints Mitissinia for Mitissima). The "
        "passage is the whole of chapter 93. In the Latin, Mitissima sane omnium poena is 'the "
        "mildest punishment of all' and praeter peccatum, quod originale traxerunt is 'apart from "
        "the original sin they drew with them'. For infants, see chapter 43 (English at lines "
        "21502-21507; Latin at lines 10419-10425), which says that in baptism 'infants die only to "
        "original sin; those who are older die also to all the sins which their evil lives have "
        "added to the sin which they brought with them'. The passage carries the witness "
        "lpc.witness.infants-and-the-sin-of-another.",
    )

    emit_quote(
        "the-mildest-condemnation-of-all",
        "It may therefore be correctly affirmed, that such infants as quit the body without being "
        "baptized will be involved in the mildest condemnation of all. That person, therefore, "
        "greatly deceives both himself and others, who teaches that they will not be involved in "
        "condemnation;",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may expect Augustine to be silent or gentle about babies who die "
        "unbaptized. He is neither. He says 'such infants as quit the body without being baptized "
        "will be involved in the mildest condemnation of all'. He says whoever teaches that they "
        "will not be condemned 'greatly deceives both himself and others'.",
        "So it may rightly be said that infants who leave the body unbaptized will share the mildest condemnation of all. And so a person who teaches that they will not be condemned greatly deceives both himself and others.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. A page-break tag inside 'such infants' is "
             "stripped. The NPNF chapter title, 'Unbaptized Infants Damned, But Most Lightly', and "
             "its endnote are the editor's and are not part of the passage."),
        [{"source_id": "lpc.source.augustine-anti-pelagian-corpus",
          "locus": "On the Merits and Forgiveness of Sins, Book I, chapter 21 (XVI in the older "
                   f"numbering); English at {NPNF105}, line 2558",
          "license": "public-domain"}],
        1,
        ["participant asks what happened to babies who died unbaptized"],
        [],
        ["The NPNF chapter title, 'Unbaptized Infants Damned, But Most Lightly', is the editor's, "
         "not Augustine's; the speaker must not quote it as his.",
         "The passage does not say what the condemnation is or where; it does not use the word "
         "limbo, and the speaker must not supply either.",
         "The speaker must not soften 'condemnation'; the mildest condemnation is still "
         "condemnation.",
         "The passage speaks of no one child; if a participant speaks of a child of their own or "
         "close to them who died, the speaker must not apply the passage to that child."],
        "Augustine, On the Merits and Forgiveness of Sins, Book I, chapter 21 (XVI in the older "
        f"numbering), the first two sentences of the chapter's text. English in the NPNF translation "
        f"at {NPNF105}, line 2558. No Latin of this work is vendored (a filename search of "
        "cic/texts/ found none). A page-break tag inside 'such infants' is stripped. The NPNF "
        "chapter title, 'Unbaptized Infants Damned, But Most Lightly', and the editor's endnote "
        "275, which cross-refers to Enchiridion 93 and Contra Julianum V.11, are the editor's and "
        "are not part of the passage. The words after it, on the apostle's 'Judgment from one "
        "offence to condemnation', are left out. The passage names the unbaptized infants that "
        "Enchiridion 93 leaves unnamed, and is read with lpc.quote.the-mildest-punishment-of-all. "
        "The passage carries the witness lpc.witness.infants-and-the-sin-of-another.",
    )

    emit_quote(
        "all-the-merit-or-demerit-is-acquired-in-this-life",
        "Nor can it be denied that the souls of the dead are benefited by the piety of their living "
        "friends, who offer the sacrifice of the Mediator, or give alms in the church on their "
        "behalf. But these services are of advantage only to those who during their lives have "
        "earned such merit, that services of this kind can help them. For there is a manner of life "
        "which is neither so good as not to require these services after death, nor so bad that such "
        "services are of no avail after death; there is, on the other hand, a kind of life so good "
        "as not to require them; and again, one so bad that when life is over they render no help. "
        "Therefore, it is in this life that all the merit or demerit is acquired, which can either "
        "relieve or aggravate a man’s sufferings after this life. No one, then, need hope that after "
        "he is dead he shall obtain merit with God which he has neglected to secure here.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may think prayers or gifts could still change a person's fate after "
        "death. Augustine says the living do help the dead, but only those who 'during their lives "
        "have earned such merit'. He says 'it is in this life that all the merit or demerit is "
        "acquired'. No one need hope to gain after death what he 'neglected to secure here'.",
        "Nor can it be denied that the souls of the dead are helped by the devotion of their living friends. Those friends offer the sacrifice of the Mediator, or give alms in the church on their behalf. But these services help only those who earned, during their lives, the kind of merit that lets such services help them. For there is a way of life that is not so good that it needs no such help after death. Nor is it so bad that such help is of no use after death. There is also a kind of life so good that it does not need them. And there is one so bad that, when life is over, they give no help. So all merit or blame is gained in this life. It can either ease or worsen a person’s sufferings after this life. No one, then, should hope to gain after death the merit with God that he neglected to secure here.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-the-enchiridion",
          "locus": f"Enchiridion, chapter 110 (chapter CX in the Latin), first part; English at {NPNF103}, lines "
                   f"23550-23564; Latin at {ENCH_LAT}, lines 12430-12448",
          "license": "public-domain"}],
        2,
        ["participant asks whether prayers or gifts for the dead could change their fate",
         "participant asks whether a person could earn merit after death",
         "participant asks on what a person is judged"],
        [],
        ["The speaker must not say the living can save a person who lived badly; the passage says "
         "that for a life 'so bad' the services 'render no help'.",
         "The passage does not say what the 'sacrifice of the Mediator' is beyond those words, or how "
         "the dead are helped.",
         "The passage does not mention purgatory, and the speaker must not supply it.",
         "The passage carries no date for the Enchiridion, and the speaker must not supply one."],
        "Augustine, Enchiridion, chapter 110 (chapter CX in the Latin text), from the opening to "
        f"'neglected to secure here.'. English in the NPNF translation at {NPNF103}, lines "
        f"23550-23564. Latin (Bruder, 1838) at {ENCH_LAT}, lines 12430-12448 (OCR text, with "
        "misreads; a page header and footnote marks at lines 12444-12447 sit inside the range and "
        "are not part of the passage). The rest of chapter 110, from 'And accordingly it is plain' "
        "to 'the different kinds of lives that men lead in the body?', is left out. The closing "
        "sentences are at lpc.quote.thank-offerings-for-the-very-good. In the Latin, hic omne "
        "meritum comparatur is 'here all merit is acquired'. The passage carries the witness "
        "lpc.witness.judged-on-the-life-lived-here.",
    )

    emit_quote(
        "thank-offerings-for-the-very-good",
        "When, then, sacrifices either of the altar or of alms are offered on behalf of all the "
        "baptized dead, they are thank-offerings for the very good, they are propitiatory offerings "
        "for the not very bad, and in the case of the very bad, even though they do not assist the "
        "dead, they are a species of consolation to the living. And where they are profitable, their "
        "benefit consists either in obtaining a full remission of sins, or at least in making the "
        "condemnation more tolerable.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may expect every prayer for the dead to do the same work. Augustine says "
        "offerings at the altar and alms for 'the baptized dead' do three different things. They are "
        "'thank-offerings for the very good' and 'propitiatory offerings for the not very bad'. For "
        "'the very bad' they are only 'a species of consolation to the living'.",
        "So sacrifices, either of the altar or of alms, are offered for all the baptized dead. For the very good they are offerings of thanks. For the not very bad they are offerings that seek mercy. For the very bad they do not help the dead, but they are a kind of comfort to the living. And where they do help, the help is either a full forgiveness of sins, or at least a more bearable condemnation.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-the-enchiridion",
          "locus": "Enchiridion, chapter 110 (chapter CX in the Latin), closing sentences; English at "
                   f"{NPNF103}, lines 23575-23582; Latin at {ENCH_LAT}, lines 12457-12465",
          "license": "public-domain"}],
        1,
        ["participant asks whether we prayed or gave offerings for the dead",
         "participant asks what our offerings for the dead were meant to do"],
        ["participant asks whether a dead person's merit could still change -- "
         "lpc.quote.all-the-merit-or-demerit-is-acquired-in-this-life gives that"],
        ["The passage speaks of 'the baptized dead' only; it does not say what offerings do for "
         "anyone unbaptized.",
         "The speaker must not say offerings help the very bad; the passage says 'even though they do "
         "not assist the dead'.",
         "The passage does not say what the service was, what words it used or when it was held, and "
         "the speaker must not supply them.",
         "The passage carries no date for the Enchiridion, and the speaker must not supply one."],
        "Augustine, Enchiridion, chapter 110 (chapter CX in the Latin text), from 'When, then, "
        f"sacrifices' to the end of the chapter. English in the NPNF translation at {NPNF103}, lines "
        f"23575-23582. Latin (Bruder, 1838) at {ENCH_LAT}, lines 12457-12465 (OCR text, with "
        "misreads). A page-break tag inside the word 'sacrifices' at line 23575 is stripped. In the "
        "Latin, pro valde bonis gratiarum actiones sunt is 'for the very good they are "
        "thanksgivings' and pro non valde malis propitiationes sunt is 'for the not very bad they "
        "are propitiations'. The passage carries the witness lpc.witness.remembered-at-the-altar.",
    )

    emit_quote(
        "remember-me-at-the-lords-altar",
        "“Lay this body anywhere, let not the care for it trouble you at all. This only I ask, that "
        "you will remember me at the Lord’s altar, wherever you be.”",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may expect a dying mother's last wish to be about her burial. Monica, as "
        "Augustine reports her, says to lay her body anywhere and not to trouble about it. She asks "
        "one thing: to be remembered 'at the Lord's altar, wherever you be'.",
        "“Lay this body anywhere. Do not let the care of it trouble you at all. I ask only this: that you remember me at the Lord’s altar, wherever you are.”",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-confessions",
          "locus": "Confessions, Book IX, chapter XI, section 27; English at "
                   "cic/texts/npnf101_augustine-confessions-letters.xml, lines 14192-14195; Latin at "
                   "cic/texts/augustine_confessiones-lat_knoll-csel33.txt, lines 14839 and 14889-14890",
          "license": "public-domain"}],
        1,
        ["participant asks what Monica asked for as she was dying",
         "participant asks how we remembered the dead at the altar",
         "participant asks what we did when someone was dying"],
        [],
        ["The passage does not say where Monica was buried or what became of her body; the speaker "
         "must not supply it.",
         "The passage does not say these are her exact words, and the speaker must not call them "
         "that; the next sentence, outside the passage, says she spoke 'in such words as she could'.",
         "The passage does not say what was said or done at the altar, and the speaker must not "
         "supply it."],
        "Augustine, Confessions, Book IX, chapter XI, section 27. English in the NPNF translation at "
        "cic/texts/npnf101_augustine-confessions-letters.xml, lines 14192-14195. Latin (Knoell, CSEL "
        "33) at cic/texts/augustine_confessiones-lat_knoll-csel33.txt, lines 14839 and 14889-14890; "
        "the page's apparatus and a page break lie between those lines and are not part of the "
        "passage. The words are Monica's as Augustine remembers and reports them. Monica's death "
        "is dated 387 by the chronological table in the vendored NPNF volume "
        "(cic/texts/npnf101_augustine-confessions-letters.xml, lines 3258-3260); Confessions "
        "IX.xi.28 (line 14225) says she died in \"the fifty-sixth year of her age, and the "
        "thirty-third of mine.\" The sentences "
        "before them in section 27, on her fever and on her words 'shall you bury your mother', are "
        "left out, as is the sentence after. In the Latin, ponite hoc corpus ubicumque is 'lay this "
        "body anywhere' and ut ad domini altare memineritis mei is 'that you remember me at the "
        "Lord's altar'. The passage carries the witness lpc.witness.remembered-at-the-altar.",
    )

    emit_quote(
        "not-to-be-refused-to-any-one-born-of-man",
        "But in respect of the case of the infants, which you say ought not to be baptized within "
        "the second or third day after their birth, and that the law of ancient circumcision should "
        "be regarded, so that you think that one who is just born should not be baptized and "
        "sanctified within the eighth day, we all thought very differently in our council. For in "
        "this course which you thought was to be taken, no one agreed; but we all rather judge that "
        "the mercy and grace of God is not to be refused to any one born of man.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may think the question was whether to baptize babies at all. In this "
        "letter the question is how soon. Fidus thought a newborn should not be baptized before the "
        "eighth day, as in circumcision. The council answered that no one agreed, and that God's "
        "mercy and grace are 'not to be refused to any one born of man'.",
        "As for the case of infants: you say they should not be baptized on the second or third day after birth. You say the law of the old circumcision should be kept. So you think a newborn should not be baptized and made holy before the eighth day. In our council we all thought very differently. No one agreed with the course you thought should be taken. Instead, we all judge that the mercy and grace of God must not be refused to any human being who is born.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Epistle LVIII, to Fidus, section 2 (Epistle LXIV in the Oxford numbering; Hartel 64); "
                   f"English at {ANF05}, lines 35891-35898; Latin at {EPIST_LAT}, lines 11715-11722",
          "license": "public-domain"}],
        2,
        ["participant asks whether we baptized babies",
         "participant asks how soon after birth a child could be baptized",
         "participant asks what the council under Cyprian decided about infants"],
        ["participant asks why infants were baptized at all -- "
         "lpc.quote.not-his-own-sins-but-the-sins-of-another gives the council's reason"],
        ["The passage does not say why infants are baptized; that comes in section 5, quoted at "
         "lpc.quote.not-his-own-sins-but-the-sins-of-another, and the speaker must not give the "
         "reason as if it were stated here.",
         "The passage does not give a date or a place for the council; the speaker must not supply "
         "either. Section 1, outside the passage, gives the number as sixty-six.",
         "The passage does not say what happens to a child who dies unbaptized, and the speaker must "
         "not supply it."],
        "Cyprian and his colleagues in council, Epistle LVIII to Fidus (ANF numbering; Epistle LXIV "
        f"in the Oxford edition and in Hartel), section 2. English in the ANF translation at {ANF05}, "
        f"lines 35891-35898. Latin (Hartel, CSEL 3) at {EPIST_LAT}, lines 11715-11722 (the Latin "
        "section 2 ends at line 11730). A scripture-reference note inside the range and a page-break "
        "tag inside the word 'within' are not part of the passage. The words 'we all thought', 'we "
        "all rather judge' are the council's, since section 1 begins 'Cyprian, and others his "
        "colleagues who were present in council, in number sixty-six, to Fidus their brother'. "
        "Section 2 continues after the passage with 'For as the Lord says in His Gospel' and is left "
        "out. In the Latin, nulli hominum nato misericordiam Dei et gratiam denegandam is 'that "
        "God's mercy and grace are not to be denied to any person born'. The passage carries the "
        "witness lpc.witness.infants-and-the-sin-of-another.",
    )

    emit_quote(
        "not-his-own-sins-but-the-sins-of-another",
        "But again, if even to the greatest sinners, and to those who had sinned much against God, "
        "when they subsequently believed, remission of sins is granted—and nobody is hindered from "
        "baptism and from grace—how much rather ought we to shrink from hindering an infant, who, "
        "being lately born, has not sinned, except in that, being born after the flesh according to "
        "Adam, he has contracted the contagion of the ancient death at its earliest birth, who "
        "approaches the more easily on this very account to the reception of the forgiveness of "
        "sins—that to him are remitted, not his own sins, but the sins of another.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may expect this to say infants are guilty. The council says the newborn "
        "'has not sinned', except that, born 'according to Adam', he 'has contracted the contagion "
        "of the ancient death'. So what is forgiven him is 'not his own sins, but the sins of "
        "another'. The words 'original sin' and 'guilt' do not appear.",
        "Even the greatest sinners, who had sinned much against God, are granted forgiveness of sins when they later believe. No one is kept from baptism and grace. How much more, then, should we shrink from keeping back an infant! Being newly born, he has not sinned, except in one way. Born in the flesh as Adam’s child, he caught the infection of the ancient death at his very first birth. For this very reason he comes the more easily to receive the forgiveness of sins. What is forgiven him is not his own sins, but the sins of another.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. An ANF editor's bracketed note, with verses "
             "by George Canning, sits inside section 5 after 'according to Adam,'. It is not Cyprian's. "
             "It is not part of the passage and is left out."),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Epistle LVIII, to Fidus, section 5 (Epistle LXIV in the Oxford numbering; Hartel 64); "
                   f"English at {ANF05}, lines 35962-35981; Latin at {EPIST_LAT}, lines 11822-11850",
          "license": "public-domain"}],
        1,
        ["participant asks whether babies were born guilty",
         "participant asks what we believed about original sin",
         "participant asks why babies were baptized if they had no sins of their own"],
        ["participant asks only how soon after birth a child was baptized -- "
         "lpc.quote.not-to-be-refused-to-any-one-born-of-man gives that"],
        ["The passage does not use the words 'original sin' or 'guilt'; the speaker must not supply "
         "them as if quoted.",
         "The passage does not say what happens to an infant who dies unbaptized, and the speaker "
         "must not supply it.",
         "The editor's bracketed note inside section 5, with verses by George Canning, is not "
         "Cyprian's; the speaker must not attribute it to him."],
        "Cyprian and his colleagues in council, Epistle LVIII to Fidus (ANF numbering; Epistle LXIV "
        "in the Oxford edition and in Hartel), section 5, from 'But again, if even to the greatest "
        f"sinners' to the end of the sentence. English in the ANF translation at {ANF05}, lines "
        f"35962-35981. Latin (Hartel, CSEL 3) at {EPIST_LAT}, lines 11822-11828 and 11849-11850; the "
        "page's footnote apparatus and a page break at lines 11830-11848 lie between them and are "
        "not part of the passage. An ANF editor's bracketed note inside the sentence, with verses by "
        "George Canning, is not Cyprian's. It is not part of the passage and is left out. A "
        "scripture-reference note earlier in section 5 is outside the passage. In the Latin, "
        "contagium mortis antiquae prima natiuitate contraxit is 'he drew the contagion of the "
        "ancient death at his first birth' and non propria sed aliena peccata is 'not his own sins "
        "but another's'. The passage carries the witness lpc.witness.infants-and-the-sin-of-another.",
    )

    emit_quote(
        "no-salvation-out-of-the-church",
        "Can the power of baptism be greater or of more avail than confession, than suffering, when "
        "one confesses Christ before men and is baptized in his own blood? And yet even this baptism "
        "does not benefit a heretic, although he has confessed Christ, and been put to death outside "
        "the Church, unless the patrons and advocates of heretics declare that the heretics who are "
        "slain in a false confession of Christ are martyrs, and assign to them the glory and the "
        "crown of martyrdom contrary to the testimony of the apostle, who says that it will profit "
        "them nothing although they were burnt and slain. But if not even the baptism of a public "
        "confession and blood can profit a heretic to salvation, because there is no salvation out "
        "of the Church, how much less shall it be of advantage to him, if in a hiding-place and "
        "a cave of robbers, stained with the contagion of adulterous water, he has not only not put "
        "off his old sins, but rather heaped up still newer and greater ones!",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may expect a gentle line about outsiders. Cyprian is writing about "
        "heretics who confess Christ, not about people who never heard of him. He says even baptism "
        "in a heretic's own blood does not benefit him, 'because there is no salvation out of the "
        "Church'. He then says a heretic baptized 'in a hiding-place and a cave of robbers' is "
        "'stained with the contagion of adulterous water'.",
        "Can the power of baptism be greater or worth more than confession and suffering? That is when someone confesses Christ before others and is baptized in his own blood. Yet even this baptism does not help a heretic, though he confessed Christ and was put to death outside the Church. Only the defenders and advocates of heretics say otherwise. They declare that heretics killed in a false confession of Christ are martyrs. They give them the glory and crown of martyrdom against the word of the apostle. He says it will profit them nothing, even if they were burned and killed. Not even the baptism of public confession and blood can help a heretic to salvation, because there is no salvation outside the Church. How much less will it help him in a hiding-place and a den of robbers, stained with the infection of adulterous water! There he has not only failed to put off his old sins. He has piled up still newer and greater ones.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. An ANF editor's bracketed note follows 'out "
             "of the Church,' and says the maxim 'has been terribly misunderstood and cruelly abused'. It "
             "is not Cyprian's. It is not part of the passage and is left out."),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Epistle LXXII, to Jubaianus, section 21 (Epistle LXXIII in the Oxford numbering; Hartel "
                   f"73); English at {ANF05}, lines 38899-38919; Latin at {EPIST_LAT}, lines 15200-15231",
          "license": "public-domain"}],
        1,
        ["participant asks whether we believed there was salvation outside the Church",
         "participant asks what 'no salvation outside the Church' meant to us",
         "participant asks whether a martyr who was a heretic was saved"],
        [],
        ["The passage's subject is heretics who confess Christ and die outside the Church; it does "
         "not mention people who never heard of Christ or belong to other religions, and the speaker "
         "must not say it does.",
         "The passage does not say what Augustine held on this question; the speaker must not supply "
         "it as if quoted.",
         "The editor's bracketed note after 'out of the Church,' is not Cyprian's; the speaker must "
         "not attribute it to him.",
         "The passage does not give a date for the letter, and the speaker must not supply one."],
        "Cyprian, Epistle LXXII to Jubaianus (ANF numbering; Epistle LXXIII in the Oxford edition "
        "and in Hartel), section 21, from 'Can the power of baptism be greater' to 'newer and "
        f"greater ones!'. English in the ANF translation at {ANF05}, lines 38899-38919. Latin "
        f"(Hartel, CSEL 3) at {EPIST_LAT}, lines 15200-15231 (OCR text; the first lines are misread, "
        "and footnote apparatus at lines 15208-15222 and a page break at line 15224 sit inside the "
        "range and are not part of the passage). Two notes sit inside the passage. The "
        "scripture-reference note after 'burnt and slain.' is left out. The ANF editor's bracketed "
        "note after 'out of the Church,' is not Cyprian's. It is not part of the passage and is "
        "left out. In the Latin, quia salus extra ecclesiam non est is 'because there is no "
        "salvation outside the Church'. The passage carries the witness "
        "lpc.witness.no-salvation-outside-the-church.",
    )

    emit_quote(
        "an-ever-burning-gehenna",
        "What will then be the glory of faith? what the punishment of faithlessness? When the day of "
        "judgment shall come, what joy of believers, what sorrow of unbelievers; that they should "
        "have been unwilling to believe here, and now that they should be unable to return that they "
        "might believe! An ever-burning Gehenna will burn up the condemned, and a punishment "
        "devouring with living flames; nor will there be any source whence at any time they may have "
        "either respite or end to their torments.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may expect Cyprian to speak only of heretics and schismatics. Here he "
        "writes to Demetrianus, a pagan who blamed and persecuted Christians. He says an "
        "'ever-burning Gehenna will burn up the condemned'. He says there will be no 'respite or end "
        "to their torments'.",
        "What then will be the glory of faith? What will be the punishment of unbelief? When the day of judgment comes, what joy for believers, what sorrow for unbelievers! They were unwilling to believe here, and now they cannot return to believe. An ever-burning Gehenna will burn up the condemned, a punishment that devours with living flames. There will be no source from which they may ever have either respite or end to their torments.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-minor-pastoral-treatises",
          "locus": "To Demetrianus (An Address to Demetrianus, ANF Treatise V), section 24; English at "
                   f"{ANF05}, lines 46246-46253; Latin at {DEMETR_LAT}, lines 914-919",
          "license": "public-domain"}],
        1,
        ["participant asks whether we believed outsiders were going to hell",
         "participant asks what Cyprian taught would happen to those who would not believe"],
        [],
        ["The addressee is a pagan who persecuted Christians, and the passage speaks of those who "
         "heard and would not believe; it does not speak of people who never heard of Christ, and "
         "the speaker must not say it does.",
         "The sentences after the passage, on bodies kept 'in infinite tortures' and the persecutor "
         "seen 'for ever', are left out, and the speaker must not supply them as if quoted.",
         "The passage names no person as lost, and the speaker must not name any person or group as "
         "lost.",
         "If a participant speaks of a person close to them who has died, the speaker must not say "
         "or suggest that this person is among the lost.",
         "The record says nothing about suicide; the speaker must not join it with "
         "lpc.witness.no-one-may-take-his-own-life to say or suggest what became of anyone who died "
         "that way.",
         "The passage carries no date for the treatise, and the speaker must not supply one."],
        "Cyprian, To Demetrianus (An Address to Demetrianus, ANF Treatise V), section 24, from 'What "
        "will then be the glory of faith?' to 'end to their torments.'. English in the ANF "
        f"translation at {ANF05}, lines 46246-46253. Latin (Hartel, CSEL 3) at {DEMETR_LAT}, lines "
        "914-919. The section number '24.' at the start of the English is not part of the passage. "
        "Section 23 before it, in which Christ 'will call down on them that believe not, eternal "
        "punishments in the fires of Gehenna', and the sentences after it, on souls and bodies and "
        "the persecutor seen for ever, are left out. In the Latin, cremabit addictos ardens semper "
        "gehenna is 'an ever-burning Gehenna will burn up the condemned' and nec erit unde habere "
        "tormenta uel requiem possint aliquando uel finem is 'nor will there be any source whence "
        "they may at any time have respite or end to their torments'. The passage is read with "
        "lpc.quote.no-repentance-is-too-late, which speaks of the time still left. The passage "
        "carries the witnesses lpc.witness.no-salvation-outside-the-church and "
        "lpc.witness.punishment-without-end.",
    )

    emit_quote(
        "no-repentance-is-too-late",
        "When you have once departed thither, there is no longer any place for repentance, and no "
        "possibility of making satisfaction. Here life is either lost or saved; here eternal safety "
        "is provided for by the worship of God and the fruits of faith. Nor let any one be "
        "restrained either by his sins or by his years from coming to obtain salvation. To him who "
        "still remains in this world no repentance is too late.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may hear only the threat in Cyprian's words to Demetrianus. Here he turns "
        "to an offer. After death, he says, 'there is no longer any place for repentance'. But 'To "
        "him who still remains in this world no repentance is too late'.",
        "When you have once gone there, there is no longer any place for repentance, and no way of making amends. Here life is either lost or saved. Here eternal safety is provided for by the worship of God and the fruits of faith. Let no one be held back, either by his sins or by his years, from coming to obtain salvation. To anyone who still remains in this world, no repentance is too late.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-minor-pastoral-treatises",
          "locus": "To Demetrianus (An Address to Demetrianus, ANF Treatise V), section 25, from 'When "
                   f"you have once departed thither'; English at {ANF05}, lines 46296-46303; Latin at "
                   f"{DEMETR_LAT}, lines 1001-1006",
          "license": "public-domain"}],
        2,
        ["participant asks whether we believed outsiders were going to hell",
         "participant asks whether it was ever too late to repent"],
        ["participant asks what Cyprian said awaits those who would not believe -- "
         "lpc.quote.an-ever-burning-gehenna gives that"],
        ["The addressee is a pagan who persecuted Christians, and the passage speaks to a man still "
         "living who may yet turn; it does not speak of people who never heard of Christ, and the "
         "speaker must not say it does.",
         "The speaker must not give 'no longer any place for repentance' without 'no repentance is "
         "too late'; the warning and the offer stand together.",
         "The passage names no person as lost or saved, and the speaker must not name any person or "
         "group as either.",
         "If a participant speaks of a person close to them who has died, the speaker must not say "
         "or suggest that this person is among the lost.",
         "The record says nothing about suicide; the speaker must not join it with "
         "lpc.witness.no-one-may-take-his-own-life to say or suggest what became of anyone who died "
         "that way.",
         "The passage carries no date for the treatise, and the speaker must not supply one."],
        "Cyprian, To Demetrianus (An Address to Demetrianus, ANF Treatise V), section 25, from "
        "'When you have once departed thither' to 'no repentance is too late.'. English in the ANF "
        f"translation at {ANF05}, lines 46296-46303 (the range ends on the line that holds "
        f"'is too late.'). Latin (Hartel, CSEL 3) at {DEMETR_LAT}, lines 1001-1006 (a page break at "
        "line 997 lies before the range). The sentences before it, with Cyprian's pointing the "
        "persecutor to 'the ways of salvation', and the sentences after it, on seeking God's mercy "
        "even at the end of life, are left out. In the Latin, quando istinc recessum fuerit, nullus "
        "iam paenitentiae locus est is 'when one has departed from here, there is no longer any "
        "place for repentance' and in isto adhuc mundo manenti paenitentia nulla sera est is 'for "
        "one still remaining in this world no repentance is too late'. The passage is read with "
        "lpc.quote.an-ever-burning-gehenna. The passage carries the witness "
        "lpc.witness.no-salvation-outside-the-church.",
    )

    emit_quote(
        "who-that-has-any-human-feeling-would-refuse-to-forgive-them",
        "And consequently, even if some of these virgins killed themselves to avoid such disgrace, "
        "who that has any human feeling would refuse to forgive them? And as for those who would not "
        "put an end to their lives, lest they might seem to escape the crime of another by a sin of "
        "their own, he who lays this to their charge as a great wickedness is himself not guiltless "
        "of the fault of folly. For if it is not lawful to take the law into our own hands, and slay "
        "even a guilty person, whose death no public sentence has warranted, then certainly he who "
        "kills himself is a homicide, and so much the guiltier of his own death, as he was more "
        "innocent of that offence for which he doomed himself to die.",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may expect either a bare rule against suicide or only pity. Augustine "
        "gives both in one passage. First he asks who 'that has any human feeling would refuse to "
        "forgive' virgins who killed themselves 'to avoid such disgrace'. Then he says that 'he who "
        "kills himself is a homicide'.",
        "So even if some of these virgins killed themselves to escape such disgrace, who with any human feeling would refuse to forgive them? Others would not end their lives, so as not to seem to escape another’s crime by a sin of their own. Whoever charges them with great wickedness for this is himself not free of the fault of folly. It is not lawful to take the law into our own hands and kill even a guilty person, whose death no public sentence has ordered. If so, then surely whoever kills himself commits homicide. He is the guiltier of his own death, the more innocent he was of the offence for which he condemned himself to die.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-city-of-god",
          "locus": "City of God, Book I, chapter 17, from the opening to the end of the second sentence of the "
                   f"argument; English at {NPNF102}, lines 2431-2441; Latin at {COG_LAT}, lines 2717-2725",
          "license": "public-domain"}],
        1,
        ["participant asks what Augustine taught about suicide",
         "participant asks what Augustine taught about Christian women in the sack of Rome who killed "
         "themselves"],
        [],
        ["The passage does not say what became of any person who died by suicide, and the speaker "
         "must not make any claim about the eternal fate of any such person.",
         "The passage does not say anything about burial or funeral practice, and the speaker must "
         "not supply it.",
         "The speaker must not give the hard teaching without the first sentence, 'who that has any "
         "human feeling would refuse to forgive them?'; the compassion and the teaching stand "
         "together.",
         "This record is for questions about history and teaching; the speaker must not use it as "
         "advice to anyone now.",
         "The passage names no place or year; the 'virgins' are those of chapter 16, in captivity, "
         "and the speaker must not supply more."],
        f"Augustine, City of God, Book I, chapter 17. English in the NPNF translation at {NPNF102}, "
        f"lines 2431-2441. Latin (Hoffmann, CSEL 40) at {COG_LAT}, lines 2717-2725. The passage is "
        "the first three sentences of chapter 17. The words after it, on Judas, are at "
        "lpc.quote.no-place-for-a-healing-penitence and are meant to be read with it. 'These "
        "virgins' and 'such disgrace' look back to chapter 16, outside the passage, on the violation "
        "of virgins in captivity. In the Latin, quis humanus adfectus eis nolit ignosci is 'what "
        "human feeling would be unwilling that they be forgiven' and profecto etiam qui se ipsum occidit "
        "homicida est is 'surely he who kills himself is also a homicide'. This record is retrieved "
        "only for historical or teaching questions about what Augustine taught. The passage carries "
        "the witness lpc.witness.no-one-may-take-his-own-life.",
    )

    emit_quote(
        "no-place-for-a-healing-penitence",
        "Do we justly execrate the deed of Judas, and does truth itself pronounce that by hanging "
        "himself he rather aggravated than expiated the guilt of that most iniquitous betrayal, "
        "since, by despairing of God’s mercy in his sorrow that wrought death, he left to himself no "
        "place for a healing penitence?",
        "lpc.figure.augustine",
        "verbatim",
        "Augustine uses Judas as his example. He says that by hanging himself Judas 'rather "
        "aggravated than expiated the guilt' of his betrayal. By 'despairing of God's mercy', Judas "
        "'left to himself no place for a healing penitence'. Augustine says this of Judas, not of "
        "everyone who takes his own life.",
        "Do we rightly abhor the deed of Judas? Does truth itself declare that by hanging himself he added to the guilt of that most wicked betrayal, rather than atoning for it? For in a sorrow that brought death he despaired of God’s mercy. So he left himself no room for a repentance that heals.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.augustine-city-of-god",
          "locus": f"City of God, Book I, chapter 17, the sentence on Judas; English at {NPNF102}, lines "
                   f"2442-2446; Latin at {COG_LAT}, lines 2725-2730",
          "license": "public-domain"}],
        2,
        ["participant asks what Augustine taught about Judas's death"],
        ["participant asks what Augustine said about the virgins, rather than about Judas -- "
         "lpc.quote.who-that-has-any-human-feeling-would-refuse-to-forgive-them gives that"],
        ["The passage does not say what became of Judas after death, and the speaker must not make "
         "any claim about the eternal fate of any person who died by suicide.",
         "The speaker must not say Augustine called every person who took his own life a Judas or "
         "said that all of them despaired of God's mercy; he says it of Judas.",
         "The speaker must not give this passage without the compassion in "
         "lpc.quote.who-that-has-any-human-feeling-would-refuse-to-forgive-them; Augustine asks who "
         "would refuse to forgive the virgins in the same chapter.",
         "This record is for questions about history and teaching; the speaker must not use it as "
         "advice to anyone now."],
        "Augustine, City of God, Book I, chapter 17, the Judas sentence. English in the NPNF "
        f"translation at {NPNF102}, lines 2442-2446. Latin (Hoffmann, CSEL 40) at {COG_LAT}, lines "
        "2725-2730. The sentences before it, with the forgiveness of the virgins and 'he who kills "
        "himself is a homicide', are at "
        "lpc.quote.who-that-has-any-human-feeling-would-refuse-to-forgive-them. The sentences after "
        "it, on Judas passing from this life 'chargeable not only with the death of Christ, but with "
        "his own', are left out. In the Latin, Dei misericordiam desperando is 'by despairing of "
        "God's mercy' and nullum sibi salubris paenitentiae locum reliquit is 'he left himself no "
        "place for a healing repentance'. This record is retrieved only for historical or teaching "
        "questions about what Augustine taught. The passage carries the witness "
        "lpc.witness.no-one-may-take-his-own-life.",
    )


PENITENT_PERIL_EPIST_LAT = "cic/texts/cyprian_epistulae-lat_hartel1871-csel3-tei.txt"


def build_penitent_peril_quotes() -> None:
    emit_quote(
        "before-even-a-deacon",
        "I think that our brethren must be dealt with;—that they who have received certificates from "
        "the martyrs, and may be assisted by their privilege with God, if they should be seized with "
        "any misfortune and peril of sickness, should, without waiting for my presence, before any "
        "presbyter who might be present, or if a presbyter should not be found and death begins to "
        "be imminent, before even a deacon, be able to make confession of their sin, that, with the "
        "imposition of hands upon them for repentance, they should come to the Lord with the peace "
        "which the martyrs have desired, by their letters to us, to be granted to them.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may think a penitent who fell ill had to wait for the bishop. Cyprian "
        "says those holding a martyr's certificate need not wait. They may confess 'before any "
        "presbyter who might be present', or, if none is found and death is near, 'before even a "
        "deacon'. Then they 'come to the Lord with the peace'.",
        "I think we must come to the help of our brothers in this way. Some have received letters of peace from the martyrs, and may be helped by the martyrs' standing with God. If misfortune and the danger of sickness seize them, they should not wait for me to be present. They should be able to confess their sin before any presbyter who is there. If no presbyter can be found and death begins to draw near, they may confess before even a deacon. Then hands are laid on them for repentance. In this way they may come to the Lord with the peace the martyrs asked for them in their letters to us.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Epistle XII (Oxford numbering Ep. XVIII; Hartel Ep. 18), section 1, from 'I think "
                   f"that our brethren must be dealt with'; English at {ANF05}, lines 30064-30073; "
                   f"Latin at {PENITENT_PERIL_EPIST_LAT}, lines 2807 and 2827-2834",
          "license": "public-domain"}],
        1,
        ["participant asks what was done for a penitent who fell ill before the road back was finished",
         "participant asks whether a sick penitent had to wait for the bishop",
         "participant asks who could hear a dying penitent's confession"],
        [],
        ["The passage speaks of those who hold a martyr's certificate; the speaker must not say it "
         "covers every penitent or every one of the lapsed. The council's wider wording is at "
         "lpc.quote.penitents-in-peril-of-sickness-should-be-assisted.",
         "The passage says the confession may be made before a presbyter or a deacon; it does not "
         "say who laid on hands or who gave the peace, and the speaker must not say a deacon "
         "absolved or reconciled anyone.",
         "The passage gives a rule for the sick; it does not say that anyone used it, how many did, "
         "or what became of any who died, and the speaker must not supply it.",
         "The passage names no year; it says only that summer has begun. The speaker must not "
         "supply a date."],
        "Cyprian, Epistle XII in the ANF numbering (Epistle XVIII in the Oxford edition and in "
        "Hartel, CSEL 3), to his presbyters and deacons, section 1, from 'I think that our brethren "
        f"must be dealt with' to 'to be granted to them.'. English in the ANF translation at {ANF05}, "
        "lines 30064-30073 (the range ends on the line that holds 'granted to them.'; the "
        "editor's note that follows it is left out). Latin (Hartel, CSEL 3) at "
        f"{PENITENT_PERIL_EPIST_LAT}, line 2807, where the sentence opens at occurrendum puto "
        "fratribus nostris, and lines 2827-2834, where it ends; apparatus lines and a page break lie "
        "between them. In the Latin, apud presbyterum quemcumque praesentem is 'before any "
        "presbyter who is present' and apud diaconum quoque exomologesin facere delicti sui possint "
        "is 'they may make confession of their sin before a deacon too'. The passage is read with "
        "lpc.quote.penitents-in-peril-of-sickness-should-be-assisted. The passage carries the "
        "witness lpc.witness.peace-for-the-dying-penitent.",
    )

    emit_quote(
        "penitents-in-peril-of-sickness-should-be-assisted",
        "when it was decided in the council that penitents in peril of sickness should be assisted, "
        "and have peace granted to them",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may think the church had no rule for a penitent who fell ill. Cyprian "
        "points to one. He says it 'was decided in the council that penitents in peril of sickness "
        "should be assisted, and have peace granted to them'.",
        "It was decided in the council that penitents in danger from sickness should be helped, and should be granted peace.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        [{"source_id": "lpc.source.cyprian-epistles",
          "locus": "Epistle LII (Oxford numbering Ep. LVI; Hartel Ep. 56), section 2, the clause on "
                   f"penitents in peril of sickness; English at {ANF05}, lines 34210-34211; Latin "
                   f"at {PENITENT_PERIL_EPIST_LAT}, lines 8585-8586",
          "license": "public-domain"}],
        2,
        ["participant asks what was done for a penitent who fell ill before the road back was finished",
         "participant asks whether a council ever ruled on sick penitents"],
        ["participant asks who could hear a dying penitent's confession -- "
         "lpc.quote.before-even-a-deacon gives that"],
        ["The passage names no council, year or place, and the speaker must not supply them.",
         "The passage is one clause; it does not say who may give the peace, what the penitent must "
         "do first, or how the rule was kept, and the speaker must not supply it.",
         "The clause is given in a letter to Fortunatus and his colleagues, in an argument about "
         "those overcome by torture; the speaker must not present it as the letter's main subject.",
         "The passage does not say what became of any penitent who died, and the speaker must not "
         "make any claim about it."],
        "Cyprian, Epistle LII in the ANF numbering (Epistle LVI in the Oxford edition and in Hartel, "
        "CSEL 3), to Fortunatus and his other colleagues, section 2, the clause 'when it was decided "
        "in the council that penitents in peril of sickness should be assisted, and have peace "
        f"granted to them'. English in the ANF translation at {ANF05}, lines 34210-34211. The "
        "words before it, 'For', and the words after it, on those who ought to receive peace first, "
        f"are left out. Latin (Hartel, CSEL 3) at {PENITENT_PERIL_EPIST_LAT}, lines 8585-8586. In the "
        "Latin, cum in concilio placuerit paenitentiam agentibus in infirmitatis periculo subueniri "
        "et pacem dari is 'since it pleased the council that penitents in peril of sickness be "
        "helped and peace be given'. The passage is read with lpc.quote.before-even-a-deacon. The "
        "passage carries the witness lpc.witness.peace-for-the-dying-penitent.",
    )


# ===========================================================================
# QUOTES HELD APART FROM HOST PROSE (29) -- each real source quotation that a
# story, gravity, force or term carries is its own record here, and the host
# paraphrases it and points to it.
# ===========================================================================

ANF05 = "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml"
VITA_LAT = "cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt"
EPIST_LAT = "cic/texts/cyprian_epistulae-lat_hartel1871-csel3-tei.txt"
KNOPF = "cic/texts/knopf_ausgewaehlte-maertyrerakten-lat-grc-deu_krueger1929.txt"
GEBHARDT = "cic/texts/gebhardt_acta-martyrum-selecta-lat-grc-deu_1902.txt"
POSSIDIUS = "cic/texts/possidius_vita-augustini_weiskotten1919.txt"
ACTA_SPEAKER = "The Acta Proconsularia of Cyprian"


def _src(source_id: str, locus: str) -> list[dict]:
    return [{"source_id": source_id, "locus": locus, "license": "public-domain"}]


def build_host_quotes() -> None:
    # --- lpc.story.election-of-cyprian ------------------------------------
    emit_quote(
        "chosen-while-still-a-neophyte",
        "For the proof of his good works I think that this one thing is enough, that by the "
        "judgment of God and the favour of the people, he was chosen to the office of the "
        "priesthood and the degree of the episcopate while still a neophyte, and, as it was "
        "considered, a novice. Although still in the early days of his faith, and in the untaught "
        "season of his spiritual life, a generous disposition so shone forth in him, that although "
        "not yet resplendent with the glitter of office, but only of hope, he gave promise of "
        "entire trustworthiness for the priesthood that was coming upon him.",
        "lpc.figure.pontius",
        "verbatim",
        "A modern listener may hear 'priesthood' as the office of a parish priest. Pontius's "
        "word, sacerdotium, here names the bishop's own office, which is why the rendering says "
        "'the sacred office'. A neophyte is someone newly baptized. Pontius presses the point: "
        "Cyprian was chosen before he had any training, on the strength of what people could "
        "already see in him.",
        "I think this one fact is enough to prove his good works. By the judgment of God and the "
        "favour of the people, he was chosen for the sacred office and the rank of bishop. He was "
        "still newly baptized and, as people thought, a beginner. He was still in the first days "
        "of his faith, in the untaught season of his spiritual life. Yet a noble nature shone out "
        "in him. He did not yet shine with the glow of office, only with the glow of hope. Even "
        "so, he gave every promise that he could be trusted with the sacred office coming to him.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. modern_rendering follows Hartel's "
             "Latin where the English misleads: 'priesthood' renders sacerdotium, here the "
             "bishop's office, given as 'the sacred office'; 'neophyte' renders neophytus, "
             "'newly baptized'; 'novice' renders nouellus, 'a beginner'; and 'a generous "
             "disposition' renders generosa indoles, 'a noble nature'."),
        _src("lpc.source.pontius-life-and-passion-of-cyprian",
             f"Life of Cyprian, section 5; English at {ANF05}, lines 27817-27825; Latin at "
             f"{VITA_LAT}, lines 40550-40562"),
        2,
        ["participant asks how Pontius described Cyprian's election",
         "participant asks whether a newly baptized man could be made bishop",
         "participant asks what 'the judgment of God and the favour of the people' meant"],
        ["participant wants the whole story of how Cyprian was chosen -- "
         "lpc.story.election-of-cyprian gives that",
         "participant wants Cyprian's own words on his election -- "
         "lpc.quote.ancient-venom-against-my-episcopate gives that"],
        ["The passage does not say how the people made their favour known; the speaker must "
         "not supply a vote, a count or a ceremony.",
         "Pontius is writing in praise of his own bishop; the speaker must not present his "
         "judgment of Cyprian's character as an outside witness's."],
        f"Pontius, Life and Passion of Cyprian, section 5. English in the ANF translation at "
        f"{ANF05}, lines 27817-27825. Latin in Hartel's edition at {VITA_LAT}, lines 40550-40562 "
        "(OCR text). The section's opening sentence, that it would be tedious to list all his "
        "deeds, is left out. The passage carries the story lpc.story.election-of-cyprian and the "
        "force lpc.force.congregational-acclamation-overriding-preference.",
    )

    # --- lpc.story.the-plague-and-the-enemies ------------------------------
    emit_quote(
        "a-dreadful-plague-broke-out",
        "Afterwards there broke out a dreadful plague, and excessive destruction of a hateful "
        "disease invaded every house in succession of the trembling populace, carrying off day by "
        "day with abrupt attack numberless people, every one from his own house. All were "
        "shuddering, fleeing, shunning the contagion, impiously exposing their own friends, as if "
        "with the exclusion of the person who was sure to die of the plague, one could exclude "
        "death itself also. There lay about the meanwhile, over the whole city, no longer bodies, "
        "but the carcases of many, and, by the contemplation of a lot which in their turn would "
        "be theirs, demanded the pity of the passers-by for themselves.",
        "lpc.figure.pontius",
        "verbatim",
        "A modern listener may hear 'their own friends' as companions. The Latin, suos, means "
        "their own people, family and household; in the English of the translation, 'friends' "
        "still meant kin. Pontius is describing a city where people put out their own sick and "
        "left the dead in the streets.",
        "Afterwards a dreadful plague broke out. The huge destruction of a hateful disease invaded "
        "the houses of the trembling people, one after another. Day by day, with sudden attack, it "
        "carried off countless people, each from his own house. Everyone shuddered and fled, and "
        "shunned the contagion. They wickedly put out their own people, as if shutting out the "
        "one sure to die of the plague could shut out death itself. Meanwhile, all over the city, "
        "there lay no longer bodies but the corpses of many. They made the passers-by think of the "
        "same fate, which would be theirs in turn. So they begged pity from them for themselves.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. modern_rendering follows Hartel's "
             "Latin where the English misleads: 'their own friends' renders suos, 'their own "
             "people', and 'exposing' renders exponere, 'put out'."),
        _src("lpc.source.pontius-life-and-passion-of-cyprian",
             f"Life of Cyprian, section 9; English at {ANF05}, lines 27939-27949; Latin at "
             f"{VITA_LAT}, lines 40782-40791"),
        2,
        ["participant asks what the plague in Cyprian's Carthage was like",
         "participant asks how the city treated its sick and dying in the epidemic"],
        ["participant asks what the church did in the plague -- "
         "lpc.quote.good-done-to-all-not-only-the-household gives that",
         "participant wants the whole account of the plague -- "
         "lpc.story.the-plague-and-the-enemies gives that"],
        ["The passage does not say how many died or name the disease; the speaker must not "
         "supply a death toll or a diagnosis."],
        f"Pontius, Life and Passion of Cyprian, section 9. English in the ANF translation at "
        f"{ANF05}, lines 27939-27949. Latin in Hartel's edition at {VITA_LAT}, lines 40782-40791 "
        "(OCR text). The section's first sentence, 'Still, if it seem well, let me glance at the "
        "rest', is left out. The passage carries the story lpc.story.the-plague-and-the-enemies.",
    )

    emit_quote(
        "it-becomes-us-to-answer-to-our-birth",
        "God continually makes His sun to rise, and from time to time gives showers to nourish "
        "the seed, exhibiting all these kindnesses not only to His people, but to aliens also. "
        "And if a man professes to be a son of God, why does not he imitate the example of his "
        "Father? “It becomes us,” said he, “to answer to our birth; and it is not fitting that "
        "those who are evidently born of God should be degenerate, but rather that the "
        "propagation of a good Father should be proved in His offspring by the emulation of His "
        "goodness.”",
        "lpc.figure.pontius",
        "verbatim",
        "A modern listener may hear 'aliens' as beings from elsewhere and 'degenerate' as "
        "depraved. Here 'aliens' are strangers, people outside the church, and to be "
        "'degenerate' is to fall short of one's birth. Pontius is reporting the sermon Cyprian "
        "preached in the plague: God is kind to outsiders, so His children must be too.",
        "God makes His sun rise without ceasing. From time to time He gives rain to feed the "
        "seed. He shows all these kindnesses not only to His own people, but to strangers too. If "
        "a man claims to be a son of God, why does he not follow his Father's example? “It is "
        "right for us,” he said, “to live up to our birth. Those who are clearly born of God "
        "should not fall short of their birth. Instead, the good Father's line should be proved "
        "in His children, as they strive to match His goodness.”",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. Hartel's Latin text has only non "
             "suis tantum, 'not only to His own'; the words 'but to aliens also' (sed etiam "
             "alienis) stand only in the older printed editions his apparatus cites, which the "
             "English follows. "
             "modern_rendering keeps them, as the text field does. It follows the Latin where "
             "the English misleads: 'aliens' is 'strangers', and degeneres, 'degenerate', is to "
             "fall short of one's birth."),
        _src("lpc.source.pontius-life-and-passion-of-cyprian",
             f"Life of Cyprian, section 9; English at {ANF05}, lines 27967-27975; Latin at "
             f"{VITA_LAT}, lines 40837-40843"),
        2,
        ["participant asks why Cyprian told his people to help those outside the church",
         "participant asks what Cyprian preached during the plague",
         "participant asks what it meant to be born of God"],
        ["participant asks what the people then did -- "
         "lpc.quote.good-done-to-all-not-only-the-household gives that"],
        ["The words are Pontius's report of a sermon he heard, not a text of Cyprian's own; the "
         "speaker must not present them as a sermon Cyprian wrote down.",
         "The passage does not say the persecutors themselves were helped; the speaker must not "
         "supply that."],
        f"Pontius, Life and Passion of Cyprian, section 9. English in the ANF translation at "
        f"{ANF05}, lines 27967-27975. Latin in Hartel's edition at {VITA_LAT}, lines 40837-40843 "
        "(OCR text). The sentences before it, in which Cyprian urges love of enemies after the "
        "pattern of Matthew v. 44-45, are left out. The passage carries the story "
        "lpc.story.the-plague-and-the-enemies.",
    )

    emit_quote(
        "good-done-to-all-not-only-the-household",
        "Thus what is good was done in the liberality of overflowing works to all men, not to "
        "those only who are of the household of faith. Something more was done than is recorded "
        "of the incomparable benevolence of Tobias. He must forgive, and forgive again, and "
        "frequently forgive; or, to speak more truly, he must of right concede that, although "
        "very much might be done before Christ, yet that something more might be done after "
        "Christ, since to His times all fulness is attributed. Tobias collected together those "
        "who were slain by the king and cast out, of his own race only.",
        "lpc.figure.pontius",
        "verbatim",
        "A modern listener may not know Tobias, who is Tobit in the Book of Tobit. He buried the "
        "dead of his own people whom the king had killed and thrown out. Pontius claims that "
        "more was done in the plague at Carthage, because the help went to everyone.",
        "So good was done, in a flood of generous works, to all people, not only to those of the "
        "household of faith. More was done than is recorded of the matchless kindness of Tobias. "
        "Tobias must forgive, and forgive again, and often forgive. Or, to speak more truly, he "
        "must rightly grant this. Much could be done before Christ, but something more could be "
        "done after Christ, since all fullness belongs to His times. Tobias gathered those whom "
        "the king had killed and thrown out, but only those of his own race.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.pontius-life-and-passion-of-cyprian",
             f"Life of Cyprian, section 10; English at {ANF05}, lines 27990-27999; Latin at "
             f"{VITA_LAT}, lines 40854-40895"),
        2,
        ["participant asks whether the church helped people outside it in the plague",
         "participant asks how the plague relief compared with older examples of mercy"],
        ["participant asks what Cyprian preached to start the relief -- "
         "lpc.quote.it-becomes-us-to-answer-to-our-birth gives that"],
        ["The passage does not say who received help or how much; the speaker must not supply "
         "names, numbers or the persecutors among them."],
        f"Pontius, Life and Passion of Cyprian, section 10. English in the ANF translation at "
        f"{ANF05}, lines 27990-27999. Latin in Hartel's edition at {VITA_LAT}, lines 40854-40895 "
        "(OCR text). The sentences before it, on the poor giving their labour, are left out; the "
        "story lpc.story.the-plague-and-the-enemies tells them in plain words. Tobias is Tobit "
        "(Tobit i-ii). The passage carries the story lpc.story.the-plague-and-the-enemies.",
    )

    # --- lpc.story.numidicus -------------------------------------------------
    emit_quote(
        "numidicus-remained-unwillingly",
        "That which belongs, dearest brethren, both to the common joy and to the greatest glory "
        "of our Church ought to be told to you; for you must know that I have been admonished and "
        "instructed by divine condescension, that Numidicus the presbyter should be appointed in "
        "the number of Carthaginian presbyters, and should sit with us among the clergy,—a man "
        "illustrious by the brightest light of confession, exalted in the honour both of virtue "
        "and of faith; who by his exhortation sent before himself an abundant number of martyrs, "
        "slain by stones and by the flames, and who beheld with joy his wife abiding by his side, "
        "burned (I should rather say, preserved) together with the rest. He himself, half "
        "consumed, overwhelmed with stones, and left for dead,—when afterwards his daughter, with "
        "the anxious consideration of affection, sought for the corpse of her father,—was found "
        "half dead, was drawn out and revived, and remained unwillingly from among the companions "
        "whom he himself had sent before. But the reason of his remaining behind, as we see, was "
        "this: that the Lord might add him to our clergy, and might adorn with glorious priests "
        "the number of our presbyters that had been desolated by the lapse of some.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may hear 'divine condescension' as God talking down. Here it means "
        "God's gracious kindness. 'Burned, I should rather say preserved' is not a cold word "
        "game: for Cyprian a martyr's death completes a life. The 'lapse of some' is the fall of "
        "presbyters who gave way in the persecution.",
        "Dearest brothers, you must be told news that belongs both to our common joy and to the "
        "greatest glory of our Church. You should know that God, in His kindness, has warned and "
        "taught me to add Numidicus the presbyter to the presbyters of Carthage. He is to sit "
        "with us among the clergy. He is a man made famous by the brightest light of confession, "
        "raised high in honour for virtue and for faith. By his urging he sent a great number of "
        "martyrs ahead of himself, killed by stones and by fire. With joy he watched his wife, "
        "who stayed at his side, burned with the others. I should rather say she was preserved. "
        "He himself was half burned, buried under stones and left for dead. Afterwards his "
        "daughter, with the anxious care of love, searched for her father's body. He was found "
        "half dead, pulled out and revived. Against his will, he stayed behind the companions he "
        "himself had sent ahead. But the reason he stayed behind, as we see, was this. The Lord "
        "meant to add him to our clergy. He meant to fill with glorious priests the ranks of our "
        "presbyters, left thin by the fall of some.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. Hartel prints remansit inuitus, "
             "'remained unwillingly'; his apparatus records inuictus, 'unconquered', from one "
             "manuscript and the older printed editions, and the ANF gives it as a note. modern_rendering follows Hartel's "
             "text. 'Divine condescension' renders dignatione diuina, God's gracious favour."),
        _src("lpc.source.cyprian-epistles",
             f"Epistle XXXIV (Oxford Ep. 40); English at {ANF05}, lines 32096-32115; Latin at "
             f"{EPIST_LAT}, lines 5642-5679"),
        1,
        ["participant asks who Numidicus was",
         "participant asks how Cyprian spoke of a survivor of martyrdom",
         "participant asks how a confessor came to be made a presbyter"],
        ["participant wants the whole story of Numidicus -- lpc.story.numidicus gives that"],
        ["The passage does not say where Numidicus's daughter searched or found him; the speaker "
         "must not supply a place.",
         "The passage does not give the wife's or the daughter's names or words; do not invent "
         "them."],
        f"Cyprian, Epistle XXXIV in the ANF numbering (40 in the Oxford numbering). English in "
        f"the ANF translation at {ANF05}, lines 32096-32115. Latin in Hartel's edition at "
        f"{EPIST_LAT}, lines 5642-5679. The greeting before the passage is left out, and so is "
        "the rest of the letter, on Numidicus's later promotion. A translator's note on "
        "'unwillingly' and an editor's comment sit inside the passage in the source and are "
        "stripped. The passage carries the story lpc.story.numidicus.",
    )

    # --- lpc.story.hundred-thousand-sesterces -------------------------------
    emit_quote(
        "grief-and-not-without-tears",
        "With excessive grief of mind, and not without tears, dearest brethren, I have read your "
        "letter which you wrote to me from the solicitude of your love, concerning the captivity "
        "of our brethren and sisters.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may hear this as a formal opening. It is the first thing Cyprian says "
        "to the eight Numidian bishops, before any argument: he read their news of captured "
        "brothers and sisters in grief and in tears.",
        "With great grief of mind, and not without tears, dearest brothers, I have read your "
        "letter. You wrote it to me out of your loving concern, about the captivity of our "
        "brothers and sisters.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.cyprian-epistles",
             f"Epistle LIX (Oxford Ep. 62), section 1; English at {ANF05}, lines 36009-36012; "
             f"Latin at {EPIST_LAT}, lines 10802-10805"),
        2,
        ["participant asks how Cyprian answered the news of the captives",
         "participant asks how a bishop showed grief for people in another church"],
        ["participant asks why the captives had to be ransomed -- "
         "lpc.quote.christ-redeemed-in-our-captive-brethren gives that"],
        ["The passage does not say who took the captives or where; the speaker must not supply "
         "a people or a place."],
        f"Cyprian, Epistle LIX in the ANF numbering (62 in the Oxford numbering), section 1. "
        f"English in the ANF translation at {ANF05}, lines 36009-36012. Latin in Hartel's edition "
        f"at {EPIST_LAT}, lines 10802-10805. The greeting naming the eight bishops comes just "
        "before it and is left out. The passage carries the story "
        "lpc.story.hundred-thousand-sesterces.",
    )

    emit_quote(
        "christ-redeemed-in-our-captive-brethren",
        "For as the Apostle Paul says, “As many of you as have been baptized into Christ have put "
        "on Christ,” Christ is to be contemplated in our captive brethren, and He is to be "
        "redeemed from the peril of captivity who redeemed us from the peril of death; so that He "
        "who took us out of the jaws of the devil, who abides and dwells in us, may now Himself "
        "be rescued and redeemed from the hands of barbarians by a sum of money—who redeemed us "
        "by His cross and blood—who suffers these things to happen for this reason, that our "
        "faith may be tried, whether each one of us will do for another what he would wish to be "
        "done for himself, if he himself were held captive among barbarians.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may hear 'redeemed' only in its church sense. Cyprian uses both "
        "senses at once: Christ redeemed us by His blood, and now Christ, present in the "
        "captives, is to be redeemed with money. The ransom is the point of the letter.",
        "For the Apostle Paul says, “As many of you as have been baptized into Christ have put on "
        "Christ.” So Christ is to be seen in our captive brothers. He who redeemed us from the "
        "danger of death is to be redeemed from the danger of captivity. He took us out of the "
        "devil's jaws, and He stays and lives in us. Now He Himself is to be rescued and redeemed "
        "from the hands of barbarians with a sum of money. He redeemed us by His cross and blood. "
        "He lets these things happen for this reason, that our faith may be tested. Will each of "
        "us do for another what he would want done for himself, if he were held captive among "
        "barbarians?",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.cyprian-epistles",
             f"Epistle LIX (Oxford Ep. 62), section 2; English at {ANF05}, lines 36034-36046; "
             f"Latin at {EPIST_LAT}, lines 10842-10851"),
        1,
        ["participant asks why the church paid to ransom captives",
         "participant asks how Cyprian saw Christ in people in need"],
        ["participant asks how much was sent -- lpc.quote.a-hundred-thousand-sesterces gives "
         "that"],
        ["The words in inner quotation marks are Galatians iii. 27; the speaker must not present "
         "them as Cyprian's own."],
        f"Cyprian, Epistle LIX in the ANF numbering (62 in the Oxford numbering), section 2. "
        f"English in the ANF translation at {ANF05}, lines 36034-36046. Latin in Hartel's "
        f"edition at {EPIST_LAT}, lines 10842-10851. A scripture-reference note (Gal. iii. 27) "
        "inside the passage is stripped. The section goes on to the danger to the captive "
        "virgins, which is left out. The passage carries the story "
        "lpc.story.hundred-thousand-sesterces.",
    )

    emit_quote(
        "a-hundred-thousand-sesterces",
        "Finally, we give you the warmest thanks that you have wished us to be sharers in your "
        "anxiety, and in so great and necessary a work—that you have offered us fruitful fields "
        "in which we might cast the seeds of our hope, with the expectation of a harvest of the "
        "most abundant fruits which will proceed from this heavenly and saving operation. We have "
        "then sent you a sum of one hundred thousand sesterces, which have been collected here in "
        "the Church over which by the Lord’s mercy we preside, by the contributions of the clergy "
        "and people established with us, which you will there dispense with what diligence you "
        "may.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may want the sum in today's money. Our sources give no such figure. "
        "What Cyprian says plainly is where it came from: the clergy and people of one church, "
        "collected for captives in another province. He thanks the Numidian bishops for the "
        "chance to give.",
        "Finally, we give you our warmest thanks. You wanted us to share in your concern, and in "
        "so great and needed a work. You offered us fruitful fields in which to sow the seeds of "
        "our hope. We expect a harvest of the richest fruit from this heavenly work that brings "
        "salvation. So we have sent you a sum of one hundred thousand sesterces. It was "
        "collected here in the Church over which, by the Lord's mercy, we preside. It came from "
        "the gifts of the clergy and people who live among us. You will hand it out there as "
        "carefully as you can.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.cyprian-epistles",
             f"Epistle LIX (Oxford Ep. 62), section 3; English at {ANF05}, lines 36072-36089; "
             f"Latin at {EPIST_LAT}, lines 10888-10896"),
        1,
        ["participant asks how much money Cyprian's church sent for the captives",
         "participant asks where the ransom money came from",
         "participant asks why Cyprian thanked the bishops who asked for money"],
        ["participant wants the whole story of the ransom -- "
         "lpc.story.hundred-thousand-sesterces gives that"],
        ["The speaker must not convert the sum into modern money; no source of ours supports a "
         "conversion.",
         "The passage does not say whether the ransom freed anyone; the speaker must not supply "
         "an outcome."],
        f"Cyprian, Epistle LIX in the ANF numbering (62 in the Oxford numbering), section 3. "
        f"English in the ANF translation at {ANF05}, lines 36072-36089. Latin in Hartel's "
        f"edition at {EPIST_LAT}, lines 10888-10896. Two editor's notes inside the passage, one "
        "of them a modern-currency estimate, are stripped and are not part of the quotation. "
        "The passage carries the story lpc.story.hundred-thousand-sesterces.",
    )

    # --- lpc.story.celerinus-writes-to-lucian -------------------------------
    emit_quote(
        "grieve-with-me-for-my-sister",
        "Know, nevertheless, that I am placed in the midst of a great tribulation; and, as if you "
        "were present with me, I remember your former love day and night, God only knows. And "
        "therefore I ask that you will grant my desire, and that you will grieve with me at the "
        "(spiritual) death of my sister, who in this time of devastation has fallen from Christ; "
        "for she has sacrificed and provoked our Lord, as seems manifest to us.",
        "lpc.figure.celerinus",
        "verbatim",
        "A modern listener may take 'the death of my sister' as a burial. She was alive. "
        "Celerinus grieves a death of the spirit: she had offered sacrifice in the persecution "
        "and so, as he saw it, fallen away from Christ.",
        "Know, however, that I am in the middle of great trouble. As if you were here with me, I "
        "remember your old love day and night; God alone knows. And so I ask you to grant my "
        "wish. Grieve with me over my sister's death, a death of the spirit. In this time of "
        "ruin she has fallen away from Christ. For she has sacrificed and angered our Lord, as "
        "seems clear to us.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. '(spiritual)' is the translator's "
             "word; the Latin has only in morte sororis meae, 'at the death of my sister'. "
             "modern_rendering keeps the translator's sense as 'a death of the spirit', because "
             "the bare word would mislead. 'Provoked' renders exacerbauit, 'angered'."),
        _src("lpc.source.cyprian-epistles",
             f"Epistle XX (Oxford Ep. 21), Celerinus to Lucian, section 2; English at {ANF05}, "
             f"lines 30569-30575; Latin at {EPIST_LAT}, lines 3119-3124"),
        2,
        ["participant asks how Celerinus spoke of his sister's fall",
         "participant asks how a family member grieved someone who lapsed"],
        ["participant wants Lucian's answer -- lpc.quote.the-case-set-before-the-bishop gives "
         "that"],
        ["The passage does not name the sister; do not invent a name for her.",
         "The letter is by Celerinus, kept in Cyprian's collection; the speaker must not "
         "present it as Cyprian's."],
        f"Celerinus to Lucian, Epistle XX in the ANF numbering (21 in the Oxford numbering), "
        f"section 2. English in the ANF translation at {ANF05}, lines 30569-30575. Latin in "
        f"Hartel's edition at {EPIST_LAT}, lines 3119-3124. The section goes on to his Easter "
        "tears and the case of Numeria and Candida, which is left out. The passage carries the "
        "story lpc.story.celerinus-writes-to-lucian.",
    )

    emit_quote(
        "shut-up-in-two-cells",
        "You see, then, brother, how (I have done this) in part of what Paulus bade me, as what we "
        "in all cases decreed when we were in this tribulation, wherein by the command of the "
        "emperor we were ordered to be put to death by hunger and thirst, and were shut up in two "
        "cells, that so they might weaken us by hunger and thirst. Moreover, the fire from the "
        "effect of our torture was so intolerable that nobody could bear it. But now we have "
        "attained the brightness itself.",
        "lpc.figure.lucian",
        "verbatim",
        "A modern listener may expect a clear sentence. Lucian wrote from prison, and the ANF "
        "translator calls the Latin confused. What is clear is the sentence on the confessors: "
        "death by hunger and thirst, in two cells. 'The brightness itself' is the glory he "
        "believes they have reached by confessing.",
        "So you see, brother, how I have done this. It is partly what Paulus told me, and partly "
        "what we all decided for everyone while we were in this trouble. In it, by the emperor's "
        "command, we were ordered to be put to death by hunger and thirst. We were shut up in two "
        "cells, so that they might weaken us by hunger and thirst. Besides, the fire that came "
        "with our torture was so unbearable that no one could endure it. But now we have reached "
        "the brightness itself.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. '(I have done this)' is the "
             "translator's supply; the Latin of the first sentence is broken in Hartel's text, "
             "and the ANF notes another reading of the fire clause, 'by the smoke of fire'. "
             "modern_rendering follows the English as printed, and 'decreed' renders censuimus, "
             "'decided'."),
        _src("lpc.source.cyprian-epistles",
             f"Epistle XXI (Oxford Ep. 22), Lucian to Celerinus, section 2; English at {ANF05}, "
             f"lines 30702-30711; Latin at {EPIST_LAT}, lines 3298-3305"),
        2,
        ["participant asks what prison was like for the confessors in Carthage",
         "participant asks how the confessors were treated under Decius"],
        ["participant wants to know who could grant peace to the lapsed -- "
         "lpc.quote.the-case-set-before-the-bishop gives that"],
        ["The passage does not say what 'the brightness' is; the speaker must not supply a "
         "vision or a death.",
         "The letter is by Lucian, kept in Cyprian's collection; the speaker must not present "
         "it as Cyprian's."],
        f"Lucian to Celerinus, Epistle XXI in the ANF numbering (22 in the Oxford numbering), "
        f"section 2. English in the ANF translation at {ANF05}, lines 30702-30711. Latin in "
        f"Hartel's edition at {EPIST_LAT}, lines 3298-3305. The first part of the section, "
        "Paulus's charge to Lucian, is left out. A translator's note inside the passage is "
        "stripped. The passage carries the story lpc.story.celerinus-writes-to-lucian.",
    )

    emit_quote(
        "the-case-set-before-the-bishop",
        "And therefore, brother, as here, since the Lord has begun to give peace to the Church "
        "itself, according to the precept of Paulus, and our tractate, the case being set forth "
        "before the bishop, and confession being made, I ask that not only these may have peace, "
        "but also (all) those whom you know to be very near to our heart.",
        "lpc.figure.lucian",
        "verbatim",
        "A modern listener may hear 'confession' as a private act before a priest. The Latin is "
        "exomologesis, the sinner's open confession before the church. Lucian grants peace in "
        "the martyrs' name, but on a condition: each case goes before the bishop first.",
        "And so, brother, I ask that it be done as it is here. When the Lord has begun to give "
        "peace to the Church itself, let each case be set before the bishop and the sin openly "
        "confessed. This is as Paulus commanded and as we ruled. Then let not only these women "
        "have peace, but also those whom you know to be dear to our heart.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. modern_rendering follows Hartel's "
             "Latin where the English misleads: cum Dominus coeperit is 'when the Lord has "
             "begun', not 'since'; facta exomologesi is the sin 'openly confessed'; tractatum, "
             "'tractate', is the confessors' own ruling; hae and quas are feminine, 'these "
             "women' and 'those'; and '(all)' is the translator's supply, left out."),
        _src("lpc.source.cyprian-epistles",
             f"Epistle XXI (Oxford Ep. 22), Lucian to Celerinus, section 2; English at {ANF05}, "
             f"lines 30728-30732; Latin at {EPIST_LAT}, lines 3338-3342"),
        1,
        ["participant asks what Lucian granted to the lapsed women",
         "participant asks what condition the confessors set on the peace they gave",
         "participant asks whether a confessor could forgive without the bishop"],
        ["participant wants the whole exchange between Celerinus and Lucian -- "
         "lpc.story.celerinus-writes-to-lucian gives that"],
        ["The speaker must not tell Lucian's grant without its condition, that each case goes "
         "before the bishop.",
         "The passage does not say what the bishop then decided; the speaker must not supply "
         "an outcome for Numeria and Candida."],
        f"Lucian to Celerinus, Epistle XXI in the ANF numbering (22 in the Oxford numbering), "
        f"section 2. English in the ANF translation at {ANF05}, lines 30728-30732. Latin in "
        f"Hartel's edition at {EPIST_LAT}, lines 3338-3342. A page-break tag inside the passage "
        "is stripped. 'These' are Numeria and Candida, named earlier in the section. The passage "
        "carries the story lpc.story.celerinus-writes-to-lucian.",
    )

    emit_quote(
        "because-i-am-already-weary",
        "We greet Saturus with his family, Bassianus and all the clergy, Uranius, Alexius, "
        "Quintianus, Colonica, and all whose names I have not written, because I am already "
        "weary. Therefore they must pardon me.",
        "lpc.figure.lucian",
        "verbatim",
        "A modern listener may pass over a list of greetings. This one ends with a prisoner "
        "who has been starved for days saying he is too tired to write more names.",
        "We greet Saturus and his family. We greet Bassianus and all the clergy, and Uranius, "
        "Alexius, Quintianus and Colonica. We greet all those too whose names I have not written. "
        "I did not write them because I am already tired. So they must forgive me.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.cyprian-epistles",
             f"Epistle XXI (Oxford Ep. 22), Lucian to Celerinus, section 3; English at {ANF05}, "
             f"lines 30738-30741; Latin at {EPIST_LAT}, lines 3350-3353"),
        3,
        ["participant asks how Lucian's letter from prison ends",
         "participant asks what the confessors' own letters sound like"],
        ["participant wants what the prison was like -- lpc.quote.shut-up-in-two-cells gives "
         "that"],
        ["The passage does not say who Saturus or the others were; the speaker must not supply "
         "their roles."],
        f"Lucian to Celerinus, Epistle XXI in the ANF numbering (22 in the Oxford numbering), "
        f"section 3. English in the ANF translation at {ANF05}, lines 30738-30741. Latin in "
        f"Hartel's edition at {EPIST_LAT}, lines 3350-3353. The greetings before it and the "
        "farewell after it are left out. The passage carries the story "
        "lpc.story.celerinus-writes-to-lucian.",
    )

    # --- lpc.story.the-death-of-cyprian -------------------------------------
    emit_quote(
        "the-people-kept-watch-at-the-door",
        "A gentle custody, however, had him in charge when taken and placed for one night in the "
        "officer’s house; so that we, his associates and friends, were as usual in his company. "
        "The whole people in the meantime, in anxiety that nothing should be done throughout the "
        "night without their knowledge, kept watch before the officer’s door.",
        "lpc.figure.pontius",
        "verbatim",
        "A modern listener may picture a prison cell. Cyprian spent his last night in an "
        "officer's house, under a light guard, with his friends around him. 'The whole people' "
        "is the Christian congregation of Carthage, keeping watch in the street.",
        "He was taken and placed for one night in the officer's house, but a gentle guard kept "
        "him there. So we, his companions and friends, were with him as usual. Meanwhile the "
        "whole people kept watch before the officer's door. They were anxious that nothing should "
        "be done during the night without their knowing.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.pontius-life-and-passion-of-cyprian",
             f"Life of Cyprian, section 15; English at {ANF05}, lines 28181-28186; Latin at "
             f"{VITA_LAT}, lines 41246-41250"),
        2,
        ["participant asks where Cyprian spent his last night",
         "participant asks what the congregation did the night before Cyprian's death"],
        ["participant asks what the Acta says of that night -- "
         "lpc.quote.the-whole-people-of-the-brethren-came gives that"],
        ["The passage does not say how many kept watch; the speaker must not supply a number."],
        f"Pontius, Life and Passion of Cyprian, section 15. English in the ANF translation at "
        f"{ANF05}, lines 28181-28186. Latin in Hartel's edition at {VITA_LAT}, lines 41246-41250 "
        "(OCR text). 'The officer' is the princeps of the Latin. The passage carries the story "
        "lpc.story.the-death-of-cyprian.",
    )

    emit_quote(
        "the-whole-people-of-the-brethren-came",
        "illuc uniuersus populus fratrum conuenit, et cum hoc sanctus Cyprianus conperisset, "
        "custodiri puellas praecepit, quoniam omnes in uico ante ianuam hospitii principis "
        "manserant.",
        ACTA_SPEAKER,
        "verbatim",
        "A modern listener may wonder why young women needed guarding. The Acta does not say "
        "from what. It says only that the whole Christian people gathered in the street outside "
        "the officer's lodging, and that Cyprian had the young women among them guarded.",
        "The whole people of the brothers came there. When holy Cyprian learned of this, he "
        "ordered the young women to be guarded. He did so because all of them had stayed in the "
        "street, before the door of the officer's lodging.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the Latin of Knopf and Krueger's edition (1929). Hartel's "
             "printing has comperisset for conperisset, and records castigari, 'restrained', as "
             "another reading for custodiri, 'guarded'. modern_rendering is a translation of the "
             "Latin; the Acta has no English in this world's vendored texts."),
        _src("lpc.source.acta-proconsularia-sancti-cypriani",
             f"Acta Proconsularia 1.6; Latin at {KNOPF}, lines 4877-4881; the same text in "
             f"{VITA_LAT}, lines 41513-41516, and {GEBHARDT}, lines 6583-6586"),
        2,
        ["participant asks what the Acta says about the night before Cyprian's death",
         "participant asks how Cyprian cared for his people while under arrest"],
        ["participant wants Pontius's account of that night -- "
         "lpc.quote.the-people-kept-watch-at-the-door gives that"],
        ["The passage does not say what the young women were guarded from; the speaker must "
         "not supply a danger.",
         "The Acta is an early compilation with an unnamed compiler, not a court transcript; "
         "the speaker must not call it one."],
        f"Acta Proconsularia of Cyprian, 1.6. Latin in Knopf and Krueger's edition at {KNOPF}, "
        f"lines 4877-4881. The same text is in Hartel's edition at {VITA_LAT}, lines "
        f"41513-41516, and in Gebhardt's at {GEBHARDT}, lines 6583-6586; those two OCR files "
        "carry line numbers and misreads inside the passage. The English is a translation "
        "made for this record. The passage carries the story lpc.story.the-death-of-cyprian.",
    )

    emit_quote(
        "walled-in-by-a-mingled-multitude",
        "He went out from the house of the officer, though he was the officer of Christ and God, "
        "and was walled in on all sides by the ranks of a mingled multitude. And such a "
        "numberless army hung upon his company, as if they had come with an assembled troop to "
        "assault death itself.",
        "lpc.figure.pontius",
        "verbatim",
        "A modern listener may miss the word play. In Latin the officer is a princeps, and "
        "Pontius calls Cyprian a princeps of Christ and God. The 'mingled multitude' is a mixed "
        "crowd, Christians and pagans together.",
        "He went out from the officer's house, though he was himself an officer of Christ and "
        "God. On every side he was walled in by the ranks of a mixed crowd. So huge an army clung "
        "to him as he went. It was as if they had come as a gathered troop to storm death itself.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.pontius-life-and-passion-of-cyprian",
             f"Life of Cyprian, section 16; English at {ANF05}, lines 28205-28209; Latin at "
             f"{VITA_LAT}, lines 41268-41272"),
        2,
        ["participant asks who went with Cyprian to his trial",
         "participant asks how many people followed Cyprian on his last day"],
        ["participant asks what the Acta says of the crowd -- "
         "lpc.quote.let-us-too-be-beheaded-with-him gives that"],
        ["The passage does not give a number for the crowd; the speaker must not supply one."],
        f"Pontius, Life and Passion of Cyprian, section 16. English in the ANF translation at "
        f"{ANF05}, lines 28205-28209. Latin in Hartel's edition at {VITA_LAT}, lines 41268-41272 "
        "(OCR text). The passage carries the story lpc.story.the-death-of-cyprian.",
    )

    emit_quote(
        "a-standard-bearer-of-the-sect",
        "And thus, therefore, the judge reads from his tablet the sentence which lately in the "
        "vision he had not read,—a spiritual sentence, not rashly to be spoken,—a sentence worthy "
        "of such a bishop and such a witness; a glorious sentence, wherein he was called a "
        "standard-bearer of the sect, and an enemy of the gods, and one who was to be an example "
        "to his people; and that with his blood discipline would begin to be established.",
        "lpc.figure.pontius",
        "verbatim",
        "A modern listener may hear 'discipline' as punishment. The proconsul meant that "
        "Cyprian's death would restore Roman order. Pontius turns each charge into praise: "
        "Cyprian did bear Christ's standard, did teach against idols, and did set his people an "
        "example. 'Witness' is the old sense of martyr.",
        "And so the judge read the sentence from his tablet, the one he had not read in the "
        "vision a little before. It was a spiritual sentence, not to be spoken lightly. It was a "
        "sentence worthy of such a bishop and such a witness. It was a glorious sentence. In it "
        "Cyprian was called a standard-bearer of the sect and an enemy of the gods. He was to be "
        "an example to his own people, and with his blood discipline would begin to be made "
        "firm.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.pontius-life-and-passion-of-cyprian",
             f"Life of Cyprian, section 17; English at {ANF05}, lines 28231-28237; Latin at "
             f"{VITA_LAT}, lines 41312-41317"),
        2,
        ["participant asks what Cyprian was sentenced for",
         "participant asks how Pontius read the proconsul's sentence"],
        ["participant asks how Cyprian answered the sentence -- lpc.quote.thanks-be-to-god "
         "gives that"],
        ["The vision is Cyprian's dream a year before his death, told earlier in the Life; the "
         "passage does not say more of it, and the speaker must not supply its details."],
        f"Pontius, Life and Passion of Cyprian, section 17. English in the ANF translation at "
        f"{ANF05}, lines 28231-28237. Latin in Hartel's edition at {VITA_LAT}, lines "
        "41312-41317 (OCR text). The present tense 'reads' is the translator's; the Latin legit "
        "can be either tense. The Acta gives the sentence in nearly the same words. The passage "
        "carries the story lpc.story.the-death-of-cyprian.",
    )

    emit_quote(
        "thanks-be-to-god",
        "Thascium Cyprianum gladio animadverti placet. Cyprianus episcopus dixit: Deo gratias.",
        ACTA_SPEAKER,
        "verbatim",
        "A modern listener may hear 'Thanks be to God' as relief or irony. In the Acta it is "
        "Cyprian's whole answer to his death sentence, the words of the church's own prayer.",
        "It is decided that Thascius Cyprian be put to death by the sword. Bishop Cyprian said, "
        "“Thanks be to God.”",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the Latin of Knopf and Krueger's edition (1929), which spells "
             "animadverti where Hartel and Gebhardt print animaduerti. modern_rendering is a "
             "translation of the Latin; the Acta has no English in this world's vendored texts."),
        _src("lpc.source.acta-proconsularia-sancti-cypriani",
             f"Acta Proconsularia 4.3; Latin at {KNOPF}, lines 4910-4911; the same text in "
             f"{VITA_LAT}, lines 41577-41579, and {GEBHARDT}, lines 6624-6626"),
        1,
        ["participant asks how Cyprian answered his death sentence",
         "participant asks what Cyprian's last recorded words at his trial were"],
        ["participant asks how the crowd answered the sentence -- "
         "lpc.quote.let-us-too-be-beheaded-with-him gives that"],
        ["Only the Acta gives this answer; the speaker must not attribute it to Pontius.",
         "The Acta is an early compilation with an unnamed compiler, not a court transcript; "
         "the speaker must not call it one."],
        f"Acta Proconsularia of Cyprian, 4.3. Latin in Knopf and Krueger's edition at {KNOPF}, "
        f"lines 4910-4911. The same text is in Hartel's edition at {VITA_LAT}, lines "
        f"41577-41579, and in Gebhardt's at {GEBHARDT}, lines 6624-6626; those two OCR files "
        "carry misreads and line numbers inside the passage. The words before the sentence, "
        "'and having said this he read the decree from the tablet', are left out. Thascius is "
        "Cyprian's own first name. The English is a translation made for this record. The "
        "passage carries the story lpc.story.the-death-of-cyprian.",
    )

    emit_quote(
        "let-us-too-be-beheaded-with-him",
        "Post hanc uero sententiam turba fratrum dicebat: Et nos cum ipso decollemur. propter hoc "
        "tumultus fratrum exortus est et multa turba eum prosecuta est.",
        ACTA_SPEAKER,
        "verbatim",
        "A modern listener may hear this cry as a riot. In the Acta it is the brothers asking to "
        "die with their bishop. The uproar follows, and the crowd walks with him to the place of "
        "execution.",
        "After this sentence the crowd of the brothers kept saying, “Let us be beheaded with him "
        "too.” Because of this an uproar rose among the brothers, and a large crowd followed him.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the Latin of Gebhardt's edition (1902), the vendored witness "
             "that reads cleanly here. modern_rendering is a translation of the Latin; the Acta "
             "has no English in this world's vendored texts."),
        _src("lpc.source.acta-proconsularia-sancti-cypriani",
             f"Acta Proconsularia 5.1; Latin at {GEBHARDT}, lines 6628-6631; the same text in "
             f"{KNOPF}, lines 4913-4917, and {VITA_LAT}, lines 41581-41583"),
        1,
        ["participant asks how the Christians of Carthage reacted to Cyprian's sentence",
         "participant asks what the crowd cried out at Cyprian's trial"],
        ["participant asks how Pontius tells the same moment -- "
         "lpc.quote.o-blessed-people-of-the-church gives that"],
        ["Pontius does not quote this cry; the speaker must not attribute it to him.",
         "The passage does not say anyone else was executed; the speaker must not supply that."],
        f"Acta Proconsularia of Cyprian, 5.1. Latin in Gebhardt's edition at {GEBHARDT}, lines "
        f"6628-6631. The same text is in Knopf and Krueger's edition at {KNOPF}, lines "
        f"4913-4917, and in Hartel's at {VITA_LAT}, lines 41581-41583; those two OCR files carry "
        "misreads inside the passage. The English is a translation made for this record. The "
        "passage carries the story lpc.story.the-death-of-cyprian.",
    )

    emit_quote(
        "he-covered-his-eyes-with-his-own-hand",
        "postea uero beatus Cyprianus manu sua oculos sibi texit. qui cum lacinias manuales "
        "ligare sibi non potuisset, Iulianus presbyter et Iulianus subdiaconus ei ligauerunt.",
        ACTA_SPEAKER,
        "verbatim",
        "A modern listener may expect one version of the scene. The two early texts differ here. "
        "Pontius says Cyprian bound his eyes with his own hands. The Acta says he covered them "
        "with his hand, and two clergy, both named Julianus, tied the cloths.",
        "Then the blessed Cyprian covered his eyes with his own hand. He could not tie the "
        "strips of cloth on himself. So the presbyter Julianus and the subdeacon Julianus tied "
        "them for him.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the Latin of Knopf and Krueger's edition (1929). "
             "modern_rendering is a translation of the Latin; the Acta has no English in this "
             "world's vendored texts. Pontius, Life section 18, says instead that Cyprian bound "
             "his eyes with his own hands (lpc.quote.the-trees-and-the-trembling-executioner)."),
        _src("lpc.source.acta-proconsularia-sancti-cypriani",
             f"Acta Proconsularia 5.5; Latin at {KNOPF}, lines 4923-4927; the same text in "
             f"{GEBHARDT}, lines 6639-6642, and {VITA_LAT}, lines 41592-41594"),
        2,
        ["participant asks who tied the cloth over Cyprian's eyes",
         "participant asks how the two accounts of Cyprian's death differ"],
        ["participant wants Pontius's version of the same moment -- "
         "lpc.quote.the-trees-and-the-trembling-executioner gives that"],
        ["The two texts differ on who tied the cloths; the speaker must not resolve the "
         "difference or merge the two."],
        f"Acta Proconsularia of Cyprian, 5.5. Latin in Knopf and Krueger's edition at {KNOPF}, "
        f"lines 4923-4927. The same text is in Gebhardt's edition at {GEBHARDT}, lines "
        f"6639-6642, and in Hartel's at {VITA_LAT}, lines 41592-41594; those two OCR files carry "
        "misreads inside the passage. The English is a translation made for this record. The "
        "passage carries the story lpc.story.the-death-of-cyprian.",
    )

    emit_quote(
        "the-trees-and-the-trembling-executioner",
        "Now the place itself where he was about to suffer is level, so that it affords a noble "
        "spectacle, with its trees thickly planted on all sides. But as, by the extent of the "
        "space beyond, the view was not attainable to the confused crowd, persons who favoured "
        "him had climbed up into the branches of the trees, that there might not even be wanting "
        "to him (what happened in the case of Zacchæus), that he was gazed upon from the trees. "
        "And now, having with his own hands bound his eyes, he tried to hasten the slowness of "
        "the executioner, whose office was to wield the sword, and who with difficulty clasped "
        "the blade in his failing right hand with trembling fingers, until the mature hour of "
        "glorification strengthened the hand of the centurion with power granted from above to "
        "accomplish the death of the excellent man, and at length supplied him with the "
        "permitted strength.",
        "lpc.figure.pontius",
        "verbatim",
        "A modern listener may take the strengthened hand as a reported fact. It is Pontius's "
        "reading. He also sets the scene to echo Zacchaeus, who climbed a tree to see Jesus. "
        "The Acta tells none of this, and says the cloths over Cyprian's eyes were tied by two "
        "clergy.",
        "The place where he was to suffer is level, so it gives a fine view, with trees planted "
        "thickly on every side. But the space was large, and the confused crowd could not see. "
        "Those who supported him had climbed into the branches of the trees. So even this was "
        "not lacking to him, as happened with Zacchaeus: he was gazed at from the trees. And now "
        "he had bound his eyes with his own hands. He tried to hurry the slow executioner, whose "
        "work was to use the sword. The man could hardly grip the blade in his failing right "
        "hand, with trembling fingers. Then the ripe hour of glory came. It strengthened the "
        "centurion's hand with power given from above, to carry out the death of this excellent "
        "man. At last it gave him the strength that had been allowed.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. Where the English has 'level', "
             "Hartel prints his own conjecture conuallis, 'a valley', and records aequalis, "
             "'level', as the reading the English follows; modern_rendering keeps 'level'. "
             "'Glorification' renders clarificationis, the hour of his glory as a martyr."),
        _src("lpc.source.pontius-life-and-passion-of-cyprian",
             f"Life of Cyprian, section 18; English at {ANF05}, lines 28254-28267; Latin at "
             f"{VITA_LAT}, lines 41330-41359"),
        2,
        ["participant asks where Cyprian was executed",
         "participant asks how Pontius tells the moment of Cyprian's death"],
        ["participant wants the Acta's version of the blindfold -- "
         "lpc.quote.he-covered-his-eyes-with-his-own-hand gives that"],
        ["The speaker must not present the strengthening of the hand from above as fact; it "
         "is how Pontius tells it.",
         "The speaker must not merge Pontius's account of the blindfold with the Acta's; they "
         "differ."],
        f"Pontius, Life and Passion of Cyprian, section 18. English in the ANF translation at "
        f"{ANF05}, lines 28254-28267. Latin in Hartel's edition at {VITA_LAT}, lines "
        "41330-41359 (OCR text). The section's first sentence, on the soldiers who went with "
        "him, is left out. Two clauses of the Latin can be read more than one way, and the ANF "
        "speaks of both the executioner and the centurion. The passage carries the story "
        "lpc.story.the-death-of-cyprian.",
    )

    emit_quote(
        "o-blessed-people-of-the-church",
        "O blessed people of the Church, who as well in sight as in feeling, and, what is more, "
        "in outspoken words, suffered with such a bishop as theirs; and, as they had ever heard "
        "him in his own discourses, were crowned by God the Judge! For although that which the "
        "general wish desired could not occur, viz., that the entire congregation should suffer "
        "at once in the fellowship of a like glory, yet whoever under the eyes of Christ "
        "beholding, and in the hearing of the priest, eagerly desired to suffer, by the "
        "sufficient testimony of that desire did in some sort send a missive to God, as his "
        "ambassador.",
        "lpc.figure.pontius",
        "verbatim",
        "A modern listener may hear 'the priest' as a parish priest. Pontius means the bishop, "
        "Cyprian. He counts the people's longing to die with their bishop as a kind of "
        "martyrdom: a letter sent ahead to God.",
        "O blessed people of the Church! In sight and in feeling, and what is more in words "
        "spoken aloud, they suffered with such a bishop as theirs. As they had always heard him "
        "say in his own sermons, they were crowned by God the Judge. The common wish was that "
        "the whole congregation should suffer at once, sharing a like glory. That could not "
        "happen. Yet some, under the watching eyes of Christ and in the hearing of the bishop, "
        "truly longed to suffer. Through that longing, a fit witness, each of them sent a kind "
        "of letter to God, as his envoy.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. modern_rendering follows Hartel's "
             "Latin where the English misleads: 'the priest' renders sacerdotis, here the "
             "bishop; 'discourses' renders tractante, his preaching; and 'missive' and "
             "'ambassador' render legationis litteras, an envoy's letter."),
        _src("lpc.source.pontius-life-and-passion-of-cyprian",
             f"Life of Cyprian, section 18; English at {ANF05}, lines 28267-28276; Latin at "
             f"{VITA_LAT}, lines 41359-41367"),
        2,
        ["participant asks how the people of Carthage met Cyprian's death",
         "participant asks whether the congregation wanted to die with their bishop"],
        ["participant asks what the crowd actually cried -- "
         "lpc.quote.let-us-too-be-beheaded-with-him gives that"],
        ["The passage does not say anyone else died that day; the speaker must not supply "
         "other deaths."],
        f"Pontius, Life and Passion of Cyprian, section 18. English in the ANF translation at "
        f"{ANF05}, lines 28267-28276. Latin in Hartel's edition at {VITA_LAT}, lines "
        "41359-41367 (OCR text). The passage carries the story lpc.story.the-death-of-cyprian.",
    )

    # --- lpc.story.the-psalms-on-the-wall -----------------------------------
    emit_quote(
        "the-psalms-hung-upon-the-wall",
        "And this he himself did in his last illness of which he died. For he commanded that the "
        "shortest penitential Psalms of David should be copied for him, and during the days of "
        "his sickness as he lay in bed he would look at these sheets as they hung upon the wall "
        "and read them ; and he wept freely and constantly. And that his attention might not be "
        "interrupted by anyone, about ten days before he departed from the body he asked of us "
        "who were present that no one should come in to him, except only at the hours in which "
        "the physicians came to examine him or when nourishment was brought to him. This, "
        "accordingly, was observed and done, and he had all that time free for prayer. Up to the "
        "very moment of his last illness he preached the Word of God in the church incessantly, "
        "vigorously and powerfully, with a clear mind and sound judgment.",
        "lpc.figure.possidius",
        "verbatim",
        "A modern listener may expect a calm deathbed. Possidius gives a man who had taught "
        "that even good Christians must repent before death, doing it himself: reading psalms "
        "of repentance on the wall and weeping. 'This' is that repentance, named in the "
        "sentence just before.",
        "And he did this himself in the last illness of which he died. He ordered the very few "
        "penitential Psalms of David to be copied for him. As he lay in bed during his "
        "sickness, he would look at these sheets hanging on the wall and read them. And he wept "
        "freely and constantly. He did not want his attention broken by anyone. So about ten "
        "days before he left the body, he asked those of us who were there to let no one come in "
        "to him. The only exceptions were the hours when the doctors came to examine him, or "
        "when food was brought to him. This was kept and done, and he had all that time free for "
        "prayer. Up to the very moment of his last illness he preached the Word of God in the "
        "church. He preached without ceasing, with vigour and power, with a clear mind and sound "
        "judgment.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is Weiskotten's English as printed. Where it has 'the shortest "
             "penitential Psalms of David', the Latin on the facing page reads Psalmos Davidicos, "
             "qui sunt paucissimi de poenitentia, 'the Psalms of David on repentance, which are "
             "very few'; modern_rendering follows the Latin."),
        _src("lpc.source.possidius-vita-augustini-weiskotten1919",
             f"Life of Augustine, chapter XXXI; English at {POSSIDIUS}, lines 4924-4938; Latin "
             f"on the facing page, lines 4887-4899"),
        1,
        ["participant asks how Augustine prepared for death",
         "participant asks whether Augustine practised the repentance he taught",
         "participant asks what the penitential psalms meant to Augustine"],
        ["participant wants the moment of his death -- lpc.quote.he-slept-with-his-fathers "
         "gives that",
         "participant wants the whole story -- lpc.story.the-psalms-on-the-wall gives that"],
        ["The passage does not name the psalms; the speaker must not supply which ones.",
         "'This' refers to repentance before death, from the sentence before; the speaker must "
         "not read it as something else."],
        f"Possidius, Life of Augustine, chapter XXXI. English in Weiskotten's translation at "
        f"{POSSIDIUS}, lines 4924-4938; Latin on the facing page of the same edition, lines "
        "4887-4899. The sentence before it, on Augustine's teaching that even baptized "
        "Christians should not die without repentance, is left out; the story "
        "lpc.story.the-psalms-on-the-wall tells it. The spaced semicolon is the OCR's. The "
        "passage carries the story lpc.story.the-psalms-on-the-wall.",
    )

    emit_quote(
        "he-slept-with-his-fathers",
        "with sight and hearing unimpaired, while we stood by and watched and prayed, \"he slept "
        "with his fathers,\" as it is written, \"well-nourished in a good old age.\"",
        "lpc.figure.possidius",
        "verbatim",
        "A modern listener may not know 'he slept with his fathers'. It is the Bible's way of "
        "saying a man died, and Possidius uses it of Augustine. He stresses that Augustine died "
        "with his sight and hearing sound, and that Possidius and others were there.",
        "His sight and hearing were unimpaired. While we stood by, "
        "watching and praying, “he slept with his fathers,” as it is written, “well nourished in "
        "a good old age.”",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.possidius-vita-augustini-weiskotten1919",
             f"Life of Augustine, chapter XXXI; English at {POSSIDIUS}, lines 4979-4981; Latin "
             f"on the facing page, lines 4940-4942"),
        1,
        ["participant asks how Augustine died",
         "participant asks who was with Augustine when he died"],
        ["participant wants his last weeks -- lpc.quote.the-psalms-hung-upon-the-wall gives "
         "that"],
        ["The passage does not give the day or the cause of death; the speaker must not supply "
         "either.",
         "The phrases in quotation marks are Scripture as Possidius uses it; the speaker must "
         "not present them as Augustine's own words."],
        f"Possidius, Life of Augustine, chapter XXXI. English in Weiskotten's translation at "
        f"{POSSIDIUS}, lines 4979-4981. The edition prints the Latin on facing pages, and the "
        "English sentence breaks across a page. Its opening clause, 'With all the members of "
        "his body intact,', stands on line 4938, before the facing Latin page (lines "
        "4939-4978), and is left out; the text field begins after the page. The Latin of the "
        "whole sentence begins on line 4899 and runs to line 4942. The biblical phrases echo 1 Kings ii. 10 and Genesis xv. 15. The "
        "passage carries the story lpc.story.the-psalms-on-the-wall.",
    )

    # --- lpc.force.transmission-institutionally-dominant-side ---------------
    emit_quote(
        "thirteen-letters-sent-to-rome",
        "And what I did, these thirteen letters sent forth at various times declare to you, "
        "which I have transmitted to you; in which neither counsel to the clergy, nor exhortation "
        "to the confessors, nor rebuke, when it was necessary, to the exiles, nor my appeals and "
        "persuasions to the whole brotherhood, that they should entreat the mercy of God, were "
        "wanting to the full extent that, according to the law of faith and the fear of God, "
        "with the Lord’s help, my poor abilities could endeavour.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may picture a published book of letters. Cyprian sent copies of "
        "thirteen of his own letters to the clergy at Rome, to show them what he had done while "
        "in hiding. The confessors are those who had confessed Christ before the magistrates.",
        "These thirteen letters show you what I did. I sent them out at different times, and I "
        "have passed them on to you. Nothing was missing from them, as far as my poor "
        "abilities could manage, with the Lord's help, under the law of faith and fear of God. There was advice to the clergy and encouragement to the confessors. "
        "When it was needed, there was rebuke to the exiles. And there were my appeals to the "
        "whole brotherhood, urging them to beg for God's mercy.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.cyprian-epistles",
             f"Epistle XIV (Oxford Ep. 20), section 2; English at {ANF05}, lines 30188-30195; "
             f"Latin at {EPIST_LAT}, lines 2983-2989"),
        2,
        ["participant asks how Cyprian's letters were kept and passed on",
         "participant asks how Cyprian accounted for his time in hiding"],
        ["participant asks about a letter Cyprian suspected was altered -- "
         "lpc.quote.the-paper-itself gives that"],
        ["The passage does not list the thirteen letters; the speaker must not supply which "
         "ones they were."],
        f"Cyprian, Epistle XIV in the ANF numbering (20 in the Oxford numbering), section 2. "
        f"English in the ANF translation at {ANF05}, lines 30188-30195. Latin in Hartel's "
        f"edition at {EPIST_LAT}, lines 2983-2989. The passage carries the force "
        "lpc.force.transmission-institutionally-dominant-side.",
    )

    # --- lpc.force.confessors-claim-to-grant-peace --------------------------
    emit_quote(
        "thousands-of-certificates-daily",
        "Moreover, when I found that those who had polluted their hands and mouths with "
        "sacrilegious contact, or had no less infected their consciences with wicked "
        "certificates, were everywhere soliciting the martyrs, and were also corrupting the "
        "confessors with importunate and excessive entreaties, so that, without any "
        "discrimination or examination of the individuals themselves, thousands of certificates "
        "were daily given, contrary to the law of the Gospel, I wrote letters in which I recalled "
        "by my advice, as much as possible, the martyrs and confessors to the Lord’s commands.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may take both 'certificates' to be one document. The 'wicked "
        "certificates' are the Decian papers saying a person had sacrificed. The thousands given "
        "daily are the confessors' letters of peace for the lapsed. Latin calls both libelli.",
        "Some had stained their hands and mouths by touching what was sacrilege. Others had "
        "stained their consciences no less with wicked certificates. I found that these people "
        "were begging the martyrs everywhere. They were also corrupting the confessors with "
        "pushy and excessive pleas. As a result, thousands of certificates were given every day, "
        "against the law of the Gospel. No one sorted or examined the people themselves. So I "
        "wrote letters to call the martyrs and confessors back to the Lord's commands, as far as "
        "my advice could.",
        conf("A", "verified-direct", "load-bearing", "Documented", None),
        _src("lpc.source.cyprian-epistles",
             f"Epistle XIV (Oxford Ep. 20), section 2; English at {ANF05}, lines 30198-30207; "
             f"Latin at {EPIST_LAT}, lines 2992-3012"),
        1,
        ["participant asks how many letters of peace the confessors gave",
         "participant asks why Cyprian objected to the confessors' certificates"],
        ["participant asks what a certificate of peace said -- "
         "lpc.quote.such-a-one-with-his-friends gives that"],
        ["'Thousands' is Cyprian's own word in a dispute; the speaker must not present it as a "
         "count."],
        f"Cyprian, Epistle XIV in the ANF numbering (20 in the Oxford numbering), section 2. "
        f"English in the ANF translation at {ANF05}, lines 30198-30207. Latin in Hartel's "
        f"edition at {EPIST_LAT}, lines 2992-3012. The passage carries the force "
        "lpc.force.confessors-claim-to-grant-peace.",
    )

    # --- lpc.force.transmission-institutionally-dominant-side ---------------
    emit_quote(
        "the-paper-itself",
        "I have, moreover, read another epistle, in which neither the person who wrote nor the "
        "persons to whom it was written were plainly declared; and inasmuch as in the same letter "
        "both the writing and the matter, and even the paper itself, gave me the idea that "
        "something had been taken away, or had been changed from the original, I have sent you "
        "back the epistle as it actually came to hand, that you may examine whether it is the "
        "very same which you gave to Crementius the sub-deacon, to carry. For it is a very "
        "serious thing if the truth of a clerical letter is corrupted by any falsehood or deceit.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may hear 'clerical' as office work. Cyprian means a letter from the "
        "clergy. He checks a letter from Rome by its handwriting, its content and its paper, and "
        "sends it back to be compared with what was sent.",
        "I have also read another letter. In it, neither the writer nor the people it was "
        "written to were clearly named. In that letter the handwriting, the content and even "
        "the paper itself made me think something was removed or changed from the original. So "
        "I have sent the letter back to you just as it reached me. You can check whether it is "
        "the very one you gave to Crementius the subdeacon to carry. For it is a very serious "
        "thing if the truth of a letter from the clergy is corrupted by any lie or deceit.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. modern_rendering follows Hartel's "
             "Latin where the English misleads: 'writing' renders scriptura, the handwriting; "
             "'the matter' renders sensus, the content; and 'clerical' renders clericae, of the "
             "clergy."),
        _src("lpc.source.cyprian-epistles",
             f"Epistle III (Oxford Ep. 9), section 2; English at {ANF05}, lines 28926-28937; "
             f"Latin at {EPIST_LAT}, lines 1229-1236"),
        2,
        ["participant asks whether letters were ever forged or altered",
         "participant asks how a bishop checked that a letter was genuine"],
        ["participant asks how Cyprian passed on his own letters -- "
         "lpc.quote.thirteen-letters-sent-to-rome gives that"],
        ["The passage does not say what had been changed, or by whom; the speaker must not "
         "supply either."],
        f"Cyprian, Epistle III in the ANF numbering (9 in the Oxford numbering), section 2. "
        f"English in the ANF translation at {ANF05}, lines 28926-28937. Latin in Hartel's "
        f"edition at {EPIST_LAT}, lines 1229-1236. A translator's note inside the passage is "
        "stripped. The passage carries the force "
        "lpc.force.transmission-institutionally-dominant-side.",
    )

    # --- lpc.force.augustine-engagement-cyprian-conciliar-acts and ----------
    # --- lpc.gravity.conciliar-authority-theory ------------------------------
    emit_quote(
        "earlier-councils-corrected-by-later",
        "But who can fail to be aware that the sacred canon of Scripture, both of the Old and "
        "New Testament, is confined within its own limits, and that it stands so absolutely in a "
        "superior position to all later letters of the bishops, that about it we can hold no "
        "manner of doubt or disputation whether what is confessedly contained in it is right and "
        "true; but that all the letters of bishops which have been written, or are being "
        "written, since the closing of the canon, are liable to be refuted if there be anything "
        "contained in them which strays from the truth, either by the discourse of some one who "
        "happens to be wiser in the matter than themselves, or by the weightier authority and "
        "more learned experience of other bishops, by the authority of Councils; and further, "
        "that the Councils themselves, which are held in the several districts and provinces, "
        "must yield, beyond all possibility of doubt, to the authority of plenary Councils which "
        "are formed for the whole Christian world; and that even of the plenary Councils, the "
        "earlier are often corrected by those which follow them, when, by some actual "
        "experiment, things are brought to light which were before concealed, and that is known "
        "which previously lay hid, and this without any whirlwind of sacrilegious pride, without "
        "any puffing of the neck through arrogance, without any strife of envious hatred, simply "
        "with holy humility, catholic peace, and Christian charity?",
        "lpc.figure.augustine",
        "verbatim",
        "A modern listener may hear 'experiment' as a laboratory test and 'charity' as giving to "
        "the poor. Augustine means experience of events, and love. A 'plenary' council is a full "
        "council of the whole church. He uses this ladder of authority to say Cyprian's council "
        "could be wrong without Cyprian being cut off.",
        "But who does not know this? The holy canon of Scripture, both Old and New Testament, is "
        "held within its own limits. It stands far above all later letters of bishops. So no one "
        "may doubt or dispute whether what is clearly in it is right and true. But bishops' "
        "letters, written since the canon was closed or still being written, may be shown wrong "
        "if anything in them strays from the truth. This may come through the word of someone "
        "wiser in the matter. It may come through the weightier authority and greater learning "
        "of other bishops, or through councils. Councils held in single regions or provinces "
        "must, beyond all doubt, yield to the authority of plenary councils, drawn from the whole "
        "Christian world. And even among plenary councils, the earlier are often corrected by "
        "the later. This happens when some experience of events brings to light what was hidden, "
        "and what lay concealed becomes known. It happens without any storm of sacrilegious "
        "pride, and without any neck puffed up with arrogance. It happens without any quarrel of "
        "envy and hatred. It happens simply with holy humility, catholic peace and Christian "
        "love.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the NPNF English as printed. modern_rendering follows "
             "Petschenig's Latin where the English misleads: 'by some actual experiment' renders "
             "aliquo experimento rerum, 'some experience of events'; 'refuted' renders "
             "reprehendi, 'shown wrong'; and 'charity' renders caritate, 'love'. The rhetorical "
             "question of the Latin is given as a question followed by statements."),
        _src("lpc.source.augustine-on-baptism-against-the-donatists",
             "On Baptism, Against the Donatists, book II, chapter 3, section 4; English at "
             "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, lines 11301-11304; Latin "
             "at cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt"
             ", lines 10209-10247"),
        1,
        ["participant asks how Augustine could say Cyprian's council was wrong",
         "participant asks whether a council could correct an earlier council",
         "participant asks what 'plenary councils' meant to Augustine"],
        ["participant wants Cyprian's own view of councils -- lpc.quote.bishop-of-bishops "
         "gives that"],
        ["The passage does not name which later council corrected which earlier one; the "
         "speaker must not supply one.",
         "'Catholic' here means the universal church's peace; the speaker must not read it as "
         "a modern denomination."],
        "Augustine, On Baptism, Against the Donatists, book II, chapter 3, section 4. English in "
        "the NPNF translation at cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, "
        "lines 11301-11304. Latin in Petschenig's "
        "edition at cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_"
        "petschenig1908-1910.txt, lines 10209-10247. The section's opening address to the "
        "Donatists is left out. The passage carries the force "
        "lpc.force.augustine-engagement-cyprian-conciliar-acts and the gravity "
        "lpc.gravity.conciliar-authority-theory.",
    )

    # --- lpc.gravity.grace-and-human-incapacity -----------------------------
    emit_quote(
        "boast-in-nothing-since-nothing-is-our-own",
        "That we must boast in nothing, since nothing is our own. In the Gospel according to "
        "John: “No one can receive anything, except it were given him from heaven.” Also in the "
        "first Epistle of Paul to the Corinthians: “For what hast thou that thou hast not "
        "received? But if thou hast received it, why boastest thou, as if thou hadst not "
        "received it?”",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may take the first line as a sermon. It is a heading in Cyprian's "
        "Testimonies, a handbook of proof texts, with the Scripture that supports it set out "
        "below. Augustine later quoted the heading many times against the Pelagians.",
        "We must boast in nothing, since nothing is our own. The Gospel according to John says, "
        "“No one can receive anything unless it is given to him from heaven.” Paul's first "
        "letter to the Corinthians also says, “What do you have that you did not receive? And if "
        "you received it, why do you boast as if you had not received it?”",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. The source gives the two proof texts "
             "with bare labels ('In the Gospel according to John:'); modern_rendering adds the "
             "verb 'says' to each so that it reads as a sentence. The Latin heading is In nullo "
             "gloriandum, quando nostrum nihil sit."),
        _src("lpc.source.cyprian-minor-pastoral-treatises",
             f"Three Books of Testimonies against the Jews, book III, heading 4; English at "
             f"{ANF05}, lines 53424-53433; Latin heading at "
             "cic/texts/cyprian_testimoniorum-libri-tres-adversus-judaeos-lat_hartel1868-csel3"
             "-tei.txt, line 3300"),
        2,
        ["participant asks what Cyprian taught about boasting or merit",
         "participant asks which words of Cyprian Augustine used against the Pelagians"],
        ["participant asks how Augustine himself put grace -- "
         "lpc.quote.two-hear-one-scorns-one-rises gives that"],
        ["The words in inner quotation marks are John iii. 27 and 1 Corinthians iv. 7; the "
         "speaker must not present them as Cyprian's own.",
         "The heading does not address the Pelagian controversy, which came long after Cyprian; "
         "the speaker must not present it as a reply to Pelagius."],
        f"Cyprian, Three Books of Testimonies against the Jews (Ad Quirinum), book III, heading "
        f"4. English in the ANF translation at {ANF05}, lines 53424-53433. Latin heading in "
        "Hartel's edition at cic/texts/cyprian_testimoniorum-libri-tres-adversus-judaeos-lat_"
        "hartel1868-csel3-tei.txt, line 3300. The heading's further proof texts (1 Samuel ii. "
        "3-4, Jeremiah ix. 23-24) are left out. Augustine quotes the heading in the "
        "anti-Pelagian works, for example at "
        "cic/texts/npnf105_augustine-anti-pelagian-writings.xml, lines 18089 and 20912. Two "
        "scripture-reference notes inside the passage are stripped. The passage carries the "
        "gravity lpc.gravity.grace-and-human-incapacity.",
    )

    # --- lpc.term.certificates-letters-of-peace -----------------------------
    emit_quote(
        "such-a-one-with-his-friends",
        "For I hear that certificates are so given to some as that it is said, “Let such a one be "
        "received to communion along with his friends,” which was never in any case done by the "
        "martyrs so that a vague and blind petition should by and by heap reproach upon us. For "
        "it opens a wide door to say, “Such a one with his friends;” and twenty or thirty or "
        "more, may be presented to us, who may be asserted to be neighbours and connections, and "
        "freedmen and servants, of the man who receives the certificate. And for this reason I "
        "beg you that you will designate by name in the certificate those whom you yourselves "
        "see, whom you have known, whose penitence you see to be very near to full satisfaction, "
        "and so direct to us letters in conformity with faith and discipline.",
        "lpc.figure.cyprian",
        "verbatim",
        "A modern listener may hear 'his friends' as companions. The Latin, cum suis, means 'with "
        "his own people', his household and kin. Cyprian's objection is that one name opens the "
        "door to a crowd no one has examined. 'Satisfaction' is the penance that makes amends.",
        "For I hear that some certificates are given in a way that says, “Let so-and-so be "
        "received into communion along with his own people.” The martyrs never did this in any "
        "case. Such a vague and blind request will soon heap blame on us. For it opens a wide "
        "door to say, “So-and-so with his own people.” Then twenty or thirty or more may be "
        "brought to us. They may be said to be the relatives, in-laws, freedmen and household of "
        "the man who received the certificate. For this reason I beg you to name in the "
        "certificate those whom you yourselves see and have known. Name those whose repentance "
        "you see is very near to full satisfaction. Then send us letters that agree with faith "
        "and discipline.",
        conf("A", "verified-direct", "load-bearing", "Documented",
             "The text field is the ANF English as printed. modern_rendering follows Hartel's "
             "Latin where the English misleads: 'with his friends' renders cum suis, 'with his "
             "own people'; 'neighbours and connections, and freedmen and servants' renders "
             "propinqui et adfines et liberti ac domestici, 'relatives, in-laws, freedmen and "
             "household'; and 'penitence' renders paenitentiam, 'repentance'."),
        _src("lpc.source.cyprian-epistles",
             f"Epistle X (Oxford Ep. 15), to the martyrs and confessors, section 4; English at "
             f"{ANF05}, lines 29936-29949; Latin at {EPIST_LAT}, lines 2467-2476"),
        2,
        ["participant asks what a confessor's certificate of peace said",
         "participant asks why Cyprian wanted each certificate to name the person"],
        ["participant asks how many certificates were given -- "
         "lpc.quote.thousands-of-certificates-daily gives that"],
        ["'Such a one' stands for a name; the speaker must not supply a real person's name.",
         "The passage does not give a certificate's full wording; the speaker must not invent "
         "one."],
        f"Cyprian, Epistle X in the ANF numbering (15 in the Oxford numbering), section 4. "
        f"English in the ANF translation at {ANF05}, lines 29936-29949. Latin in Hartel's "
        f"edition at {EPIST_LAT}, lines 2467-2476. The section's first sentence, on letters to "
        "the clergy and people, is left out. A page-break tag inside the passage is stripped. "
        "The passage carries the term lpc.term.certificates-letters-of-peace.",
    )


def main() -> None:
    build_stories()
    build_figures()
    build_quotes()
    build_sermon_quotes()
    build_commentary_quotes()
    build_disclosure_quotes()
    build_penitent_peril_quotes()
    build_host_quotes()

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
    assert len(quote_files) == 86, f"expected 86 quote records (bounded set, see docstring), " \
        f"wrote {len(quote_files)}"

    # Reciprocity self-check: every RELATION_PAIRS id must be a record this
    # script actually emitted (story/figure/quote), so relations_for() never
    # silently produces a one-sided edge against an id that doesn't exist.
    all_ids = {Path(p).stem for p in WRITTEN}
    for a, b in RELATION_PAIRS:
        assert a in all_ids, f"RELATION_PAIRS references {a!r}, never emitted"
        assert b in all_ids or b.split(".")[1] in EXTERNAL_RELATION_TYPES, (
            f"RELATION_PAIRS references {b!r}, never emitted"
        )

    print(f"Wrote {len(WRITTEN)} records: {len(story_files)} story, {len(figure_files)} figure, "
          f"{len(quote_files)} quote.")
    for path in WRITTEN:
        print(f"  {path}")


if __name__ == "__main__":
    main()
