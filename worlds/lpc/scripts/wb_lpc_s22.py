"""B-2 (S2.2): Latin Pastoral-Congregational Christianity (`lpc`) term
records -- the full 19-term lexicon roster.

WHY ONE SCRIPT, NOT A MECHANICAL/AUTHORED SPLIT. don's own sibling script
(`worlds/don/scripts/wb_don_s22_s23.py`) combined B-2 and B-3 because only 7
of Donatism's own 21 candidate terms had a built deployment chunk; the other
14 needed pure B-3 authoring from Doc_03's own one-line candidate entries.
`lpc` has no such split: Doc_06 SS0 states plainly that its own co-produced
Step 6 deliverable is "nineteen self-contained deployment chunks written to
the L4 template" -- ALL NINETEEN of `lpc`'s own candidate terms (Doc_03's
eighteen, plus one Doc_06 itself added at SS2.4 -- "certificates",
`lpclex019`) are already fully-authored, already-reviewed deployment prose,
independently re-reviewed across three rounds (`Lexicon_Deployment_Index.md`
SS167-169: "Round 1 returned REVISION REQUIRED... Round 2... Round 3...
judging the deliverable adequate to proceed to Doc_07"). So this step is
`lpc`'s own B-2 alone: converting nineteen already-settled chunks onto the
live schema is the whole of the mechanical work, with the same shape of
authored judgment on top (confidence blocks, register-safe quick_meaning/
plain_meaning, relations/reciprocity, and two schema-forced placement
decisions for CT Contest Type and Reported-Experience Status, neither of
which `term` has a dedicated field for) that don's own script names for its
own 7 built chunks. No "B-3 full authoring from a one-line candidate" task
exists here at all -- named explicitly so its absence is not mistaken for an
oversight.

INPUTS, mapped to OUTPUTS, precisely:
  - Lexicon-Chunks/lpclex001_...md through lpclex019_...md (all 19 read in
    full before this script was written) -> every term record's
    quick_meaning / plain_meaning / senses.* / false_friend / distortion_risk
    / retrieval.retrieve_when / retrieval.prefer_instead / relations /
    sources, per the FIELD MAPPING below. Each chunk is already-authored,
    already-reviewed L4-template prose; this script's own reading and
    judgment sits on top of it, not in place of it.
  - Doc_06_Full_Lexicon_Development.md SS2 (Final Tier Classification, the
    7/12/0 split and the ground for each) -> retrieval.tier and this
    record's own confirmation that Doc_03's preliminary tier is NOT what is
    carried forward (four terms moved down, two moved up from a mis-drafted
    Tier 3, one term added outright -- Doc_06's tier, not Doc_03's estimate,
    is authoritative and is what this script reads).
  - Doc_06 SS3 (CT tagging, the three contest types actually specified) and
    SS4 (Distortion Risk pattern) -> the CT-fold content in senses.
    informational for grace/schism/"compel them to come in" (see CT
    CONTEST TYPE FINDING below) and this script's own distortion_risk enum
    mapping (see DISTORTION_RISK MAPPING below).
  - Lexicon_Deployment_Index.md SS1 (Master Table, every tag column),
    SS5 (Related-Terms Reciprocity Check: "122 links across 19 entries --
    61 reciprocal pairs, zero one-way") and SS6 (Author-Gravity Cross-Check)
    -> the RELATED-TERMS GRAPH below (built from each chunk's own
    Related-Terms line, not copied from the Index's own restatement of it,
    though the two agree by construction -- see RELATED-TERMS GRAPH) and
    each term's confidence.divergence_note where Author-Gravity-Risk is Yes.
  - records/lpc/source/*.md (207 records, built at B-1, read in full --
    the complete id list from `worlds/lpc/scripts/wb_lpc_s21.py`'s own
    `ROWS`) -> every `sources[].source_id` this script writes, cross-checked
    against the Registry row each chunk's own Key Sources section actually
    cites (confirmed present on disk before this script was written; see
    ROW_TO_SOURCE below).

FIELD MAPPING, chunk section -> schema field (per this world's own launch
instructions, matching the discipline don's own script states for itself):
  - `Quick Meaning` -> `quick_meaning`, lightly carried, NOT rewritten for
    register the way don's own chunks needed: `lpc`'s own Lexicon-Chunks are
    already written "For us, ..." -- first-person emic register throughout,
    unlike don's own third-person "this world holds..." chunks. Checked
    directly: no chunk's own Quick Meaning or World Meaning uses "this
    world" or "the world's" (gate_voice_perspective's own scanned forms) --
    the one exception, disclosed rather than silently dropped, is
    `lpclex007_grace.md`'s own World Meaning, which opens with a stray,
    apparently mis-pasted line -- "Reported as the world's own
    self-understanding -- not assessed for historical accuracy; confidence
    calibration applies to the historical-event layer only" -- duplicated
    verbatim from that same chunk's own Reported-Experience Status section
    below it. That sentence is manifestly template boilerplate landing in
    the wrong section, not authored World Meaning content, and it is the
    one sentence in any chunk that would trip gate_voice_perspective's own
    "the world's..." pattern; it is left out of plain_meaning/senses.
    informational for that reason, flagged here as a `lpc`-thread finding
    rather than fixed in the chunk itself (Doc_06/the chunks are another
    thread's approved-to-proceed content; see WHAT THIS SCRIPT DOES NOT DO).
  - `World Meaning` -> split, the same pahc.term.ekklesia-precedent split
    don's own script names: `plain_meaning` gets a condensed 1-3 sentence
    version (kept under gate_readability's FK-10 ceiling), and
    `senses.informational` gets the fuller development, folding in the
    chunk's own `Ecological Function` paragraph (a section this schema has
    no dedicated field for -- the same "schema has no dedicated field"
    situation don's own script names for CT content, resolved the same way,
    by folding it into `senses.informational` rather than dropping it).
  - `Distortion Risk` (Modern Hearing / World Hearing) -> `senses.
    translational` (the paired contrast, kept as a pairing rather than
    blended, per this world's own L4 template discipline) and the
    `distortion_risk` enum -- see DISTORTION_RISK MAPPING below for why this
    is NOT a bare copy of the [DR] tag.
  - `Key Sources` -> `sources[]`, each entry resolved to the actual
    `lpc.source.<slug>` record built at B-1 via ROW_TO_SOURCE (never a bare
    citation string), AND `senses.evidential`, which carries the same
    paragraph's own Author-Gravity note, editorial-apparatus warning, phase
    bound, or citation caution in first-person register -- whichever the
    chunk's own Key Sources section actually discloses. `confidence.
    divergence_note` carries a shorter, confidence-relevant distillation of
    the same disclosure, per CONFIDENCE, PER TERM below.
  - `CT Contest Type` (grace, schism, "compel them to come in" only) ->
    folded into `senses.informational` as a clearly separated closing
    paragraph, per CT CONTEST TYPE FINDING below -- `term` has no dedicated
    CT-Contest-Type field, the same schema gap don's own script names for
    `don.term.agonistici`.
  - `Reported-Experience Status` (grace only) -> folded into `senses.
    informational` alongside the CT content, for the same schema-gap
    reason; see REPORTED-EXPERIENCE FINDING below.
  - `Retrieve-When` / `Do-Not-Retrieve-When` -> `retrieval.retrieve_when[]`
    / `retrieval.prefer_instead[]`, split from each chunk's own
    semicolon-joined line into one list entry per clause (mechanical).
    NOT a straight `do_not_retrieve_when` carry: Build-Plan.md Stage 4a
    retired that field in favor of `retrieval.prefer_instead` (redirect)
    and envelope-level `claim_guards` (barred-claim guard) --
    `gate_retrieval_negatives_structured` fails closed on any populated
    `do_not_retrieve_when`. Checked directly against `engine.prose.
    GUARD_MARKERS` (does not say / must not supply / not attested / do not
    invent / does not attest / no source / must not): NONE of the 19
    chunks' own Do-Not-Retrieve-When clauses match a guard-marker phrase --
    every one is a retrieval-scoping redirect ("that is the one episcopate
    and bishop of bishops", "that is catechesis"), never a barred-claim
    guard -- so every clause across all 19 terms resolves to `prefer_
    instead`, and `claim_guards` is empty on every record in this batch, a
    finding rather than an omission.
  - `Aliases` -> NOT copied wholesale into `false_friend`, the same
    don's-own-script rule restated for this world's own risk shape: every
    chunk here (unlike most of don's own 14 non-chunked terms) carries a
    real, substantive Modern-Hearing-vs-World-Hearing pairing regardless of
    [DR] tag (Doc_06 SS4: "Every entry carries its own paired Modern
    Hearing / World Hearing lines"), so `false_friend` is populated for
    every one of the 19 from that pairing's own Modern Hearing content,
    reworded as a short reading rather than copied as a sentence -- never a
    bare alias string, and never a string that exactly equals another
    term's own `world_word` (checked directly against every one of the 19
    `world_word` values chosen below, to stay clear of gate_alias_safety
    before this script runs, not merely at gate time).

RELATED-TERMS GRAPH. Built directly from each of the 19 chunks' own
Related-Terms line (never from `Lexicon_Deployment_Index.md`'s own
restatement of them, though the two agree by construction): every declared
edge is added to an undirected adjacency set, so a term A whose own
Related-Terms names term B gets `associated-with -> B`, and B gets the
reciprocal `associated-with -> A` back, regardless of whether B's own
chunk-authored Related-Terms line happened to name A back. Checked
directly, the 19 chunks' own declared lines already are fully
reciprocal -- summing all 19 lines' own entry counts gives exactly 122,
matching `Lexicon_Deployment_Index.md` SS5's own count ("122 links across
19 entries -- 61 reciprocal pairs, zero one-way") -- so this script's own
edge-set construction closes no gap Doc_06 did not already close; it is
run this way regardless, the same discipline don's own script uses (build
the graph from source, don't trust a summary of it), so that a future
change to any one chunk's Related-Terms line cannot silently desynchronize
this record set from the Index's own claim.

DISTORTION_RISK MAPPING. NOT a bare copy of the [DR] tag. `Lexicon_
Deployment_Index.md` SS3 discloses, in its own words, a real, carried
tension in `lpc`'s own upstream documents: "`suffrage` carries no [DR]
although Doc_06 SS4 names it a sharpest-case distortion -- a real tension
between the tag set and the prose, recorded here rather than left to a
later pass to rediscover." Overriding the tag to "high" for `suffrage`
alone, on this script's own reading of the prose, would be this script
quietly re-deciding a call that belongs to the Doc_06/Index thread, not to
B-2 -- exactly the "doc-hygiene fix on content that isn't your own thread's"
case CLAUDE.md's own default-actions table says to flag, not touch. So
this script maps mechanically from the tag: the 9 terms Lexicon_Deployment_
Index.md SS3 lists under [DR] (the flock, the lapsed, confessor, communion,
heresy, grace, "the people", "compel them to come in", "certificates") get
`distortion_risk: high`; every other term's own Distortion Risk section is
real but the tag was not applied, so this script maps those to `medium` (8
terms: reconciliation, preaching, catechesis, suffrage, bishop of bishops,
plenary Council, the one episcopate, schism) except `libelli` and
`libellatici/sacrificati`, whose own Modern Hearing lines are markedly
thinner than every other term's own (one sentence each, "may picture a
formal identity/canonical document" -- no false-friend claim beyond
that), mapped to `low`. `suffrage`'s own carried tag/prose tension is
stated again, term-by-term, in its own confidence.divergence_note below,
not silently resolved.

CT CONTEST TYPE FINDING (schema-forced placement, same finding don's own
script names for `don.term.agonistici`). `term` has no dedicated
CT-Contest-Type field. Doc_06 SS3 specifies a real contest type for each of
the three CT-tagged terms (grace, schism, "compel them to come in"), never
templated -- Round 1 "verified all three as specific and non-templated." All
three are folded into `senses.informational` as a distinctly separated
closing paragraph naming the contest type verbatim from Doc_06 SS3 and
stating, per the chunk's own words, what the entry therefore does not do.

REPORTED-EXPERIENCE FINDING (schema-forced placement, `grace` only). `term`
has no dedicated Reported-Experience-Status field either. `lpclex007_
grace.md` is the one chunk in this batch carrying that L4-template section
at all (LDF Part V; used "where the term's meaning is historically
uncertain but formationally central"). Its own verbatim marker -- "Reported
as the world's own self-understanding -- not assessed for historical
accuracy; confidence calibration applies to the historical-event layer
only" -- is folded into `don.term.grace`'s own `senses.informational`,
immediately alongside the CT-fold paragraph, rather than dropped for lack
of a field to hold it in. (This is the one piece of chunk prose this
script folds in as a genuinely templated marker rather than paraphrased
prose -- it is a status marker, not a claim, and is carried verbatim for
that reason.)

CONFIDENCE, PER TERM (Article 17 / this step's own instruction: extracted,
never re-judged where the chunk states it directly). One entry states its
own formation_confidence explicitly rather than leaving this script to
infer it, and that statement governs: `lpclex005_communion.md`'s own Key
Sources section states, in full -- "The underlying primary-source facts
reach Documented. The synthesis -- that these constitute one named
cross-phase gravity rather than two separate historical facts -- is this
build's own reasoning, at Widely Accepted, and Doc_04 SS3 flags the
divergence rather than upgrading it." Since the TERM RECORD is exactly
that synthesis (one named term, "communion," for a pattern read off both
bishops' conduct across more than one text), `lpc.term.communion` is set
formation_confidence="Widely Accepted", not "Documented", though its own
underlying quoted facts (the 256 preface, `On Baptism`) are independently
Documented and directly cited in senses.evidential. Every other term's
formation_confidence is judged per this script's own reading of its
chunk's Key Sources/Author Gravity/tier-note content, following the
same evidentiary-weight-vs-tier independence don's own script states
(a term ecologically peripheral enough to sit at Tier 2 can still be
`load-bearing` for a real, Documented, if narrow, claim -- "bishop of
bishops" and "plenary Council" are exactly this: sole textual ground of a
real Supporting/conciliar-authority axis, Tier 2 only because Doc_04/Doc_05
find no evidence the axis reached ordinary formation). `libelli` and
`libellatici/sacrificati` are the two Inferential-Thin entries in this
batch, on the same ground `wb_lpc_s21.py`'s own row-38 departure states for
Numidian basilica archaeology: `libelli`'s own Latin headword is absent
from this world's vendored corpus altogether (its own chunk: "A direct
check finds the Latin headword absent from this world's vendored English
corpus altogether"), and `libellatici`/`sacrificati`'s own two-way
classification reaches this record as a 19th-century editorial endnote on
a different, Confidence-C text, not as Cyprian's own words -- both real,
named gaps, not filled with a confidence rating the source cannot support.
`evidentiary_weight="contested"` is used nowhere in this batch, the same
`wb_lpc_s21.py`-stated rule extended here: no term's underlying SOURCE
OBJECT is disputed in the narrow sense that value is reserved for; the
three CT tags name a live scholarly contest about MEANING/RELATIONSHIP,
kept on its own, independent axis (senses.informational's own CT-fold
paragraph and, secondarily, confidence.divergence_note), never smuggled
into evidentiary_weight.

WHAT THIS SCRIPT DOES NOT DO: build or edit any Lexicon-Chunks file (read,
never edited -- all 19 are Doc_06's own already-reviewed, Approved-to-
proceed content); resolve the `suffrage` DR-tag/prose tension named above
(flagged, not fixed -- another thread's content); assign canon_cells (no
canon-cell tagging work has happened for this world yet, the same standing
limitation `wb_lpc_s21.py` names); author a confirmed-gloss entry (the same
retired-mechanism finding don's own script states at length applies
identically here -- `engine/m4/term_glosses.py` reads term records
directly, mechanically, at runtime; no separate allowlist file exists to
author into); touch anything outside `worlds/lpc/scripts/` and
`records/lpc/term/`; build story/figure/quote/gravity/force/
contested_claim/honest_limit/doctrinal_witness/ambient records (later
parts, explicitly out of scope for this step).
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]
RECORDS_ROOT = REPO_ROOT / "records" / "lpc"

WORLD_ID = "latin-pastoral-congregational-christianity"
SCHEMA_VERSION = 2

WRITTEN: list[str] = []

# Registry row -> the actual lpc.source.* record id built at B-1
# (wb_lpc_s21.py). Confirmed against records/lpc/source/ directly before
# this script was written, not assumed from the row number alone.
ROW_TO_SOURCE = {
    1: "cyprian-epistles",
    2: "cyprian-de-lapsis",
    3: "cyprian-de-unitate",
    4: "cyprian-seventh-council-of-carthage",
    5: "cyprian-minor-pastoral-treatises",
    7: "pontius-life-and-passion-of-cyprian",
    8: "anonymous-against-novatian-and-on-rebaptism",
    9: "augustine-confessions",
    11: "augustine-general-correspondence",
    12: "augustine-correction-of-the-donatists",
    13: "augustine-on-baptism-against-the-donatists",
    15: "augustine-on-the-catechising-of-the-uninstructed",
    18: "augustine-creedal-catechetical-works",
    19: "augustine-sermons-on-selected-lessons",
    21: "augustine-tractates-on-john-and-related-exegesis",
    23: "augustine-anti-pelagian-corpus",
    43: "augustine-letter-93-to-vincentius",
    192: "possidius-vita-augustini-weiskotten1919",
}


def src(row: int, locus: str) -> dict:
    return {"source_id": f"lpc.source.{ROW_TO_SOURCE[row]}", "locus": locus, "license": "public-domain"}


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


def split_clauses(text: str) -> list[str]:
    return [c.strip() for c in text.split(";") if c.strip()]


# ---------------------------------------------------------------------------
# RELATED-TERMS GRAPH (see docstring, RELATED-TERMS GRAPH). Each list below
# is a direct, mechanical transcription of that chunk's own front-matter
# Related-Terms line. Undirected edges; `associated-with` is written at
# both ends for every edge, regardless of whether the target's own line
# names the source back (checked: every one already does -- see docstring).
# ---------------------------------------------------------------------------
RELATED_TERMS = {
    "the-flock": [
        "the-lapsed", "reconciliation-penitential-discipline", "confessor", "communion",
        "preaching", "catechesis", "the-people", "suffrage", "bishop-of-bishops",
        "the-one-episcopate", "schism", "compel-them-to-come-in", "certificates-letters-of-peace",
    ],
    "the-lapsed": [
        "the-flock", "reconciliation-penitential-discipline", "confessor", "communion",
        "grace", "libelli", "libellatici-sacrificati", "certificates-letters-of-peace",
    ],
    "reconciliation-penitential-discipline": [
        "the-flock", "the-lapsed", "confessor", "communion", "heresy", "grace",
        "the-people", "the-one-episcopate", "libelli", "libellatici-sacrificati", "certificates-letters-of-peace",
    ],
    "confessor": ["the-flock", "the-lapsed", "reconciliation-penitential-discipline", "communion", "certificates-letters-of-peace"],
    "communion": [
        "the-flock", "the-lapsed", "reconciliation-penitential-discipline", "confessor", "heresy",
        "preaching", "catechesis", "the-people", "bishop-of-bishops", "plenary-council",
        "the-one-episcopate", "schism", "compel-them-to-come-in", "certificates-letters-of-peace",
    ],
    "heresy": [
        "reconciliation-penitential-discipline", "communion", "catechesis", "bishop-of-bishops",
        "plenary-council", "the-one-episcopate", "schism", "compel-them-to-come-in",
    ],
    "grace": ["the-lapsed", "reconciliation-penitential-discipline", "preaching", "catechesis", "compel-them-to-come-in"],
    "preaching": ["the-flock", "communion", "grace", "catechesis", "the-people"],
    "catechesis": ["the-flock", "communion", "heresy", "grace", "preaching"],
    "the-people": ["the-flock", "reconciliation-penitential-discipline", "communion", "preaching", "suffrage"],
    "suffrage": ["the-flock", "the-people", "the-one-episcopate"],
    "bishop-of-bishops": ["the-flock", "communion", "heresy", "plenary-council", "the-one-episcopate"],
    "plenary-council": ["communion", "heresy", "bishop-of-bishops", "the-one-episcopate"],
    "the-one-episcopate": [
        "the-flock", "reconciliation-penitential-discipline", "communion", "heresy", "suffrage",
        "bishop-of-bishops", "plenary-council", "schism",
    ],
    "schism": ["the-flock", "communion", "heresy", "the-one-episcopate", "compel-them-to-come-in"],
    "compel-them-to-come-in": ["the-flock", "communion", "heresy", "grace", "schism"],
    "libelli": ["the-lapsed", "reconciliation-penitential-discipline", "libellatici-sacrificati", "certificates-letters-of-peace"],
    "libellatici-sacrificati": ["the-lapsed", "reconciliation-penitential-discipline", "libelli"],
    "certificates-letters-of-peace": ["the-flock", "the-lapsed", "reconciliation-penitential-discipline", "confessor", "communion", "libelli"],
}

ADJACENCY: dict[str, set] = defaultdict(set)
for _slug, _targets in RELATED_TERMS.items():
    for _t in _targets:
        ADJACENCY[_slug].add(_t)
        ADJACENCY[_t].add(_slug)

_total_declared = sum(len(v) for v in RELATED_TERMS.values())
assert _total_declared == 122, f"expected 122 declared Related-Terms links (Index SS5), got {_total_declared}"
_total_pairs = sum(len(v) for v in ADJACENCY.values()) // 2
assert _total_pairs == 61, f"expected 61 reciprocal pairs (Index SS5), got {_total_pairs}"


def relations_for(slug: str) -> list[dict]:
    return [{"type": "associated-with", "target": f"lpc.term.{t}"} for t in sorted(ADJACENCY.get(slug, set()))]


def emit_term(slug: str, body_kwargs: dict, provenance_note: str) -> str:
    tid = f"lpc.term.{slug}"
    payload = {
        "id": tid,
        "world_id": WORLD_ID,
        "record_type": "term",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "relations": relations_for(slug),
        **body_kwargs,
    }
    out_dir = RECORDS_ROOT / "term"
    out_dir.mkdir(parents=True, exist_ok=True)
    front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    text = f"---\n{front}---\n{provenance_note.strip()}\n"
    path = out_dir / f"{tid}.md"
    path.write_text(text, encoding="utf-8")
    WRITTEN.append(str(path))
    return tid


# =============================================================================
# TIER 1 -- seven entries (Doc_06 SS2.1): the flock, the lapsed,
# reconciliation / penitential discipline, confessor, communion, heresy,
# grace. Full ecological treatment, from already-authored, already-reviewed
# Lexicon-Chunks read in full before writing any of this.
# =============================================================================

def build_tier1_terms() -> list[str]:
    ids = []

    ids.append(emit_term(
        "the-flock",
        dict(
            confidence=conf(
                "A", "verified-direct", "load-bearing", "Documented",
                "The dense verbal evidence for this term is Cyprian's own; Augustine's use of the "
                "same image is real but far less frequent. Our claim that this is a cross-phase "
                "pattern rests on both bishops' own conduct of the office, not on matching word-counts "
                "in each phase (Author-Gravity-Risk: Yes, Lexicon_Deployment_Index.md SS6).",
            ),
            sources=[
                src(2, "De Lapsis 4 -- 'it is the shepherd that is chiefly wounded in the wound of "
                       "his flock'"),
                src(1, "the watch-keeping passage on a shepherd's charge to keep watch over the "
                       "flock, and the relief provision for 'those who have stood with unshaken "
                       "faith and have not forsaken Christ's flock'"),
                src(3, "De Unitate's own citation of John 10:16, 'one flock and one shepherd'"),
                src(5, "further pastoral treatises carrying the same shepherd/flock/pastor image"),
                src(19, "Sermon I's own cognate image of gathering 'into His fold'"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": split_clauses(
                    "participant asks what a bishop was or did; participant asks about pastoral "
                    "authority, or about the relationship between a bishop and ordinary believers; "
                    "participant uses shepherd or pastor language; conversation reaches the question "
                    "of who a bishop answers to"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about episcopal jurisdiction between sees rather than "
                    "about a bishop's charge over his own congregation -- ask about the one episcopate "
                    "or bishop of bishops instead"
                ),
            },
            plain_meaning=(
                "A bishop, for us, is not an officer of some wider institution, dropped into a "
                "posting. He is given a people. He preaches to them, baptizes them, and buries "
                "them, and when they fail it is not a problem he manages but a wound he carries. "
                "The charge runs both ways: he answers for his flock, and his flock can stand in "
                "front of his seat and refuse to leave until he hears them."
            ),
            world_word="the flock",
            distortion_risk="high",
            false_friend=[
                "a soft, sentimental way of describing churchgoers, with a passive congregation "
                "and a gently benevolent pastor",
                "a bishop understood as a remote regional administrator rather than the man who "
                "preaches to these people himself and knows who did not come",
            ],
            senses={
                "informational": (
                    "Nothing else about our office makes sense without this. We keep a penitential "
                    "road open because a shepherd does not write off a sheep. We preach every week "
                    "because these particular people, not an audience in general, must be fed. Who "
                    "may baptize, and who may be received back, are urgent questions because they "
                    "are questions about our own people's standing, not abstractions. This term "
                    "anchors nearly everything else we hold: penitential discipline and "
                    "reconciliation are what a shepherd does with a sheep that has failed; preaching "
                    "and catechesis are the office's own ordinary work; communion is the standing of "
                    "those inside the charge; the one episcopate is what many such charges make "
                    "together; and our two conciliar formulas argue about how the holders of those "
                    "charges relate to each other."
                ),
                "evidential": (
                    "Cyprian's own words carry this image throughout, directly quoted and "
                    "re-verified at source: 'it is the shepherd that is chiefly wounded in the wound "
                    "of his flock,' and the charge to keep watch over the flock or answer for "
                    "neglect, as those before us did. A full sweep of Cyprian's own vendored corpus "
                    "returns 113 combined occurrences of flock, shepherd, and pastor language. "
                    "Augustine's own Sermons carry the cognate fold image, though far less densely. "
                    "The dense verbal evidence is Cyprian's; our cross-phase claim rests on "
                    "conduct, not on comparable word-counts."
                ),
                "personal": (
                    "A man who holds this office and has no particular people has not got the "
                    "office at all."
                ),
                "translational": (
                    "A modern listener often hears 'flock' as soft and a little patronizing -- "
                    "pious language for churchgoers, gentle on the pastor's side, passive on "
                    "theirs, and 'bishop' as a regional administrator several removes from ordinary "
                    "life. We do not mean either. The flock is a charge that can be lost, and its "
                    "failure is reckoned to the one who holds it. Our people are not passive: they "
                    "elect, they demand, and they can force a bishop's hand. And the bishop is not "
                    "remote -- he is the man who preached to you on Sunday and knows which of you "
                    "did not come."
                ),
            },
            quick_meaning=(
                "For us, the flock is not the church in general. It is the particular people one "
                "bishop is answerable for, and answerable to, by name, week after week, in one "
                "place."
            ),
        ),
        "Re-derived from Doc_06 SS2.1 (lpclex001, Tier 1, G1 Primary -- 'the ecological hub; Doc_05 "
        "SS9.1 finds every lens passes through it') and Lexicon-Chunks/lpclex001_the-flock.md, "
        "already-authored, already-reviewed deployment prose -- mapped onto the live term schema per "
        "this script's own field-mapping judgment calls (see script docstring). No register "
        "correction was needed: the chunk's own Quick Meaning and World Meaning are already written "
        "'For us, ...', first-person emic throughout, unlike don's own third-person source chunks. "
        "Ecological Function folded into senses.informational (schema has no dedicated field). "
        "Relations: this term's own Related-Terms line names thirteen other terms, all built this "
        "pass; see RELATED_TERMS/ADJACENCY.",
    ))

    ids.append(emit_term(
        "the-lapsed",
        dict(
            confidence=conf(
                "B", "verified-direct", "load-bearing", "Documented",
                "The regulating, disciplining voice throughout this crisis is Cyprian's own, as "
                "presiding bishop and as the party whose middle position ultimately prevailed. No "
                "lapsed believer's own account of undergoing the process survives anywhere in this "
                "corpus (Author-Gravity-Risk: Yes). The clean two-way split between those who "
                "sacrificed and those who only bought the certificate reaches us as a 19th-century "
                "editorial endnote on a different, Confidence-C text (lpc.term.libellatici-"
                "sacrificati), not as Cyprian's own classification in De Lapsis; what is Cyprian's "
                "own, and what this entry's own account actually rests on, is the refusal to let "
                "either group's failure be final.",
            ),
            sources=[
                src(2, "De Lapsis, the founding document of the controversy, directly quoted "
                       "throughout"),
                src(1, "the Epistles' own lapsed-crisis correspondence, including Epistles XX-XXI, "
                       "two lay confessors' own first-person voices"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": split_clauses(
                    "participant asks what happened to Christians who gave in under persecution; "
                    "participant asks about apostasy, backsliding, or whether a serious failure can "
                    "be forgiven; conversation reaches the Decian persecution or the certificates"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about heresy or schism -- leaving the church by "
                    "conviction -- rather than about failing it under compulsion; ask about heresy "
                    "or schism instead"
                ),
            },
            plain_meaning=(
                "The lapsed are our own people who complied with the order to sacrifice during the "
                "persecution -- some by sacrificing, some only by paying for a certificate that "
                "said they had. They are not strangers and not enemies. They sat where we sit, and "
                "now they are asking to come back."
            ),
            world_word="the lapsed",
            distortion_risk="high",
            false_friend=[
                "a gentle, gradual falling-away from faith, comparable to a modern believer who "
                "drifts from church over years",
                "a private matter of personal conviction, with no public consequence for standing "
                "in the community",
            ],
            senses={
                "informational": (
                    "What a persecution like this does is not kill a church outright -- it empties "
                    "one at a table, one certificate at a time, and leaves the survivors in a room "
                    "with the people who did not hold. Two demands arrive at once, and both are "
                    "serious: those who stood say the fallen cannot simply be taken back as if "
                    "nothing was weighed, and the fallen themselves ask to be let back in. To say "
                    "they are finished would say a single hour under pressure decides a life. To "
                    "let them straight back would say the hour was nothing. So neither is said: "
                    "there is a road, it is walked in the open, and it ends inside. This term "
                    "generates our whole penitential apparatus -- reconciliation exists because the "
                    "lapsed exist, and the confessors' own rival claim to grant peace exists "
                    "because there is peace to be granted. It is the concrete instance of communion "
                    "as a status: a thing lost and regained, not simply possessed or not."
                ),
                "evidential": (
                    "De Lapsis (Confidence B) is the founding document, directly quoted throughout; "
                    "the Epistles' own lapsed-crisis correspondence (Confidence A) carries the "
                    "working detail, including Epistles XX-XXI, in which two lay confessors discuss "
                    "a specific reconciliation in their own first-person voices. A full sweep "
                    "returns 96 occurrences of the exact phrase 'the lapsed' in Cyprian's own "
                    "corpus, 114 of the bare word. The regulating voice throughout is Cyprian's "
                    "own; no lapsed believer's own account of the process survives anywhere in our "
                    "corpus."
                ),
                "translational": (
                    "A modern listener often hears a category of lapsed or lapsed-Catholic "
                    "believers -- people who drifted away, stopped attending, lost interest. Gentle, "
                    "gradual, private. We mean something else entirely: a documented act under "
                    "state compulsion, on a specific occasion, with a certificate as evidence, "
                    "carrying a public consequence for standing in the community. The lapsed did "
                    "not drift off. They stayed, and asked to be readmitted, and we had to decide "
                    "in public what to do with them."
                ),
            },
            quick_meaning=(
                "For us, the lapsed are our own people. Under threat, they gave in to the order to "
                "sacrifice, and now they want to come back."
            ),
        ),
        "Re-derived from Doc_06 SS2.1 (lpclex002, Tier 1, G2 Primary -- 'the subject of this world's "
        "founding crisis') and Lexicon-Chunks/lpclex002_the-lapsed.md. citation_specificity set to B "
        "(De Lapsis, row 2, is this term's own founding-document ground; the Epistles corroborate at "
        "A). The two-way libellatici/sacrificati classification's editorial provenance is disclosed "
        "in confidence.divergence_note per the chunk's own explicit caution, not smoothed into "
        "Documented fact. Relations: eight terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "reconciliation-penitential-discipline",
        dict(
            confidence=conf(
                "A", "verified-direct", "load-bearing", "Documented",
                "Epistles XX-XXI are our own rare exception to the episcopal-voice monopoly -- two "
                "lay confessors, neither yet ordained, writing to each other in the first person "
                "(Author-Gravity-Risk: Yes). Even there the transaction itself is clerical and "
                "confessor-side; the reconciled believer does not speak anywhere in our record.",
            ),
            sources=[
                src(1, "the Epistles carry the process in operation, including Epistles XX-XXI"),
                src(2, "De Lapsis carries the argument for episcopal control of the process"),
                src(7, "Pontius reports Cyprian's own conduct of the office more broadly"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": split_clauses(
                    "participant asks how someone got back in after failing; participant asks about "
                    "penance, confession, or forgiveness as a process rather than a feeling; "
                    "participant asks who had the authority to readmit"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about baptism as entry into the church for the first "
                    "time rather than about return after failure -- ask about catechesis or heresy "
                    "instead"
                ),
            },
            plain_meaning=(
                "Discipline is the road; reconciliation is the arrival. What matters is that it "
                "is a road at all. There is an order to it, the order takes time, and everyone "
                "can see it."
            ),
            world_word="reconciliation",
            distortion_risk="medium",
            false_friend=[
                "a private sacramental confession, a few minutes long, said alone with no public "
                "witness",
                "a therapeutic reconciliation between two parties, complete once both simply feel "
                "differently toward each other",
            ],
            senses={
                "informational": (
                    "Discipline is the road; reconciliation is the arrival -- two names for one "
                    "thing. What matters is that it is a road at all: there is an order to it, the "
                    "order takes time, and it is visible. The visibility is not cruelty. A failure "
                    "that happened in public cannot be undone in private, because the people who "
                    "watched the failure are the same people who must receive the person "
                    "afterwards. And the bishop holds it -- not because he is more forgiving than "
                    "anyone else, but because peace granted by whoever feels moved to grant it is a "
                    "favour, not the church's own peace. This is the operative half of our second "
                    "founding gravity, the working end of the flock: what a shepherd actually does "
                    "with a sheep that has failed. It presupposes the lapsed as its subject, and it "
                    "generates our tension with the confessors, whose own claim to grant peace "
                    "directly is what forced this whole process into existence."
                ),
                "evidential": (
                    "The Epistles (Confidence A) carry the process in operation, including "
                    "Epistles XX-XXI; De Lapsis (Confidence B) carries the argument for episcopal "
                    "control of it; Pontius reports Cyprian's own conduct of the office more "
                    "broadly. A full sweep returns 31 corpus-wide occurrences of 'penitence,' 20 of "
                    "them inside the Epistles alone. Epistles XX-XXI are our rare exception to the "
                    "episcopal-voice monopoly -- two lay confessors, neither yet ordained, writing "
                    "to each other in the first person -- but even there the transaction is "
                    "clerical and confessor-side; the reconciled believer never speaks."
                ),
                "translational": (
                    "A modern listener may hear either a brief private confession behind a screen, "
                    "or a therapeutic notion of reconciliation -- repair achieved once both parties "
                    "feel differently. Neither is private and neither is primarily about feeling for "
                    "us. This is a public, staged, community-witnessed process with an examined "
                    "entry, a real duration, and a formal act of readmission at the end, controlled "
                    "by one office. What it restores is standing, and the whole community can see "
                    "it being restored."
                ),
            },
            quick_meaning=(
                "For us, reconciliation is not a quiet, private pardon. It is a public road that a "
                "failed member walks, in stages, back into the community."
            ),
        ),
        "Re-derived from Doc_06 SS2.1 (lpclex003, Tier 1, G2 Primary -- 'the operative half: what "
        "this world does with the lapsed') and Lexicon-Chunks/lpclex003_reconciliation-penitential-"
        "discipline.md. Relations: eleven terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "confessor",
        dict(
            confidence=conf(
                "A", "verified-direct", "load-bearing", "Documented",
                "The evidence base for this term is essentially one Registry row (the Epistles) "
                "read through one lexicon entry, disclosed at generation rather than discovered "
                "afterwards (Author-Gravity-Risk: Yes). A phase bound was established by a check, "
                "not assumed: a sweep of all eight vendored Augustine volumes returns twenty "
                "occurrences of the stem against roughly 150 in Cyprian's one volume, and none "
                "carries this sense -- this term belongs to Cyprian's phase and does not cross into "
                "Augustine's.",
            ),
            sources=[
                src(1, "the Epistles are the primary evidence, including Epistles XX-XXI, whose own "
                       "title-line the Registry gives as 'the confessors'"),
                src(2, "De Lapsis 2 -- 'We look with glad countenances upon confessors illustrious "
                       "with the heraldry of a good name... The white-robed cohort of Christ's "
                       "soldiers is here'"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": split_clauses(
                    "participant asks who the confessors were, or about martyrs versus survivors; "
                    "participant asks who had authority besides bishops; conversation reaches "
                    "the question of whether suffering confers standing"
                ),
                "prefer_instead": split_clauses(
                    "the participant is using confessor in the later sense of a priest who hears "
                    "confession -- a different office entirely -- ask about the later, sacramental "
                    "sense instead; or the participant is asking about a martyr, who died, rather "
                    "than a confessor, who survived"
                ),
            },
            plain_meaning=(
                "For us, a confessor is one who was interrogated for the Name and did not deny it, "
                "and lived. That standing, bought at that price, is the strongest rival we have to "
                "a bishop's own authority."
            ),
            world_word="confessor",
            distortion_risk="high",
            false_friend=[
                "a priest whose office is to hear other people's confessions, the later, Western, "
                "sacramental sense of the word",
                "a vague honorific for any saintly figure, with no specific claim on church "
                "authority attached",
            ],
            senses={
                "informational": (
                    "You were taken, you were asked, and you did not say what they wanted. Then, "
                    "unlike the others, you came back. Everyone knows which of us it is, because it "
                    "happened where people could see. What follows is not a quiet honour -- it is a "
                    "claim. Someone who stood in front of a magistrate and held will not easily "
                    "accept that they have nothing to say about the ones who did not hold, so they "
                    "write letters naming a lapsed person who may come back, and the people named "
                    "expect to be received. Against that stands the conviction that the church's "
                    "own peace is not any one person's to give out of their own suffering, however "
                    "real. Both positions are held in earnest, and this is our named tension point: "
                    "the reason penitential discipline takes the insistent, repeatedly restated "
                    "form it does -- built against a claim that already existed and had to be "
                    "answered, not invented in a vacuum. It is bounded: it belongs to the "
                    "persecution and does not outlive it."
                ),
                "evidential": (
                    "The Epistles are our primary evidence, including Epistles XX-XXI, whose own "
                    "title-line the Registry gives as 'the confessors'; De Lapsis carries the "
                    "regulating argument, directly quoted -- 'We look with glad countenances upon "
                    "confessors illustrious with the heraldry of a good name.' A full sweep returns "
                    "roughly 150 occurrences of 'confessor' in Cyprian's own corpus -- our single "
                    "most frequent crisis-specific term, ahead of communion, schism, and the lapsed "
                    "individually -- with 128 inside the Epistles alone. The evidence base is "
                    "essentially one Registry row read through one lexicon entry."
                ),
                "translational": (
                    "A modern listener will almost certainly hear 'confessor' as a priest who "
                    "hears confessions -- the later, Western, sacramental sense -- or a vague "
                    "honorific for a saintly figure. We mean the opposite direction entirely: not "
                    "one who hears confession, but one who made confession, under interrogation, at "
                    "real risk, and survived. The word names what was done to us and what we did "
                    "not say, and it carries a claim on the church's own decisions rather than an "
                    "office within its ministry."
                ),
            },
            quick_meaning=(
                "For us, a confessor is someone who was asked to deny the faith, and did not, and "
                "lived. That standing is the strongest rival we have to a bishop."
            ),
        ),
        "Re-derived from Doc_06 SS2.1 (lpclex004, Tier 1, G8 Tensional -- 'Doc_05 SS9.2 names it the "
        "ecology's tension point, and it is load-bearing for the two entries above') and "
        "Lexicon-Chunks/lpclex004_confessor.md. Relations: five terms per this term's own "
        "Related-Terms line.",
    ))

    ids.append(emit_term(
        "communion",
        dict(
            confidence=conf(
                "A", "verified-direct", "load-bearing", "Widely Accepted",
                "The chunk's own Key Sources section states this precisely rather than leaving it "
                "to inference: 'The underlying primary-source facts reach Documented. The synthesis "
                "-- that these constitute one named cross-phase gravity rather than two separate "
                "historical facts -- is this build's own reasoning, at Widely Accepted, and Doc_04 "
                "SS3 flags the divergence rather than upgrading it.' This term record IS that "
                "synthesis, so its own formation_confidence follows the synthesis's own rating, not "
                "the underlying quoted facts' rating. Doc_03 itself characterizes the pattern the "
                "same way: inferred from both bishops' conduct across more than one text, not a "
                "term either bishop names as such.",
            ),
            sources=[
                src(4, "the 256 Council preface -- 'It remains, that upon this same matter each of "
                       "us should bring forward what we think, judging no man, nor rejecting any "
                       "one from the right of communion, if he should think differently from us'"),
                src(13, "On Baptism, Against the Donatists -- Augustine disputing Cyprian's own "
                        "specific rebaptism ruling at book length without placing him outside"),
                src(12, "Letter 185's own pastoral-corrective register, recovering a separated party "
                        "rather than expelling one still inside"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": split_clauses(
                    "participant asks what excommunication meant, or what it meant to be in or out "
                    "of communion; participant asks how disagreement was handled; participant asks "
                    "whether bishops who disagreed sharply stayed in fellowship"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking specifically about the Eucharist as a rite rather "
                    "than about communion as a standing within the body -- ask about the rite "
                    "specifically instead"
                ),
            },
            plain_meaning=(
                "For us, communion is a formal standing within the one body -- a status we can "
                "lose and be given back. Its hardest test is that it survives sharp disagreement "
                "between the people who hold it."
            ),
            world_word="communion",
            distortion_risk="high",
            false_friend=[
                "a specific liturgical rite alone, going up to receive, with no broader sense of "
                "standing attached",
                "a general warmth of fellowship and mutual good feeling, so that any real "
                "disagreement looks like a failure of it",
            ],
            senses={
                "informational": (
                    "It is not warmth and not the rite by itself. It is where you stand -- inside "
                    "or placed outside -- and the whole community knows which, because the "
                    "consequences are public: whether you are received, whether you may come to the "
                    "table, whether your standing is the one you had before. What is remarkable is "
                    "what it survives. Two of us can hold opposite positions on the sharpest "
                    "question either will ever argue, and neither puts the other outside communion "
                    "for it. It holds across more than one lifetime, too: a century on, one bishop "
                    "argues at book length that the first one's ruling was wrong, and argues with "
                    "him, not against his memory as an outsider's. Communion is the name of "
                    "belonging itself for us, so nearly everything else touches it: reconciliation "
                    "is its restoration, the lapsed are those who lost it, heresy and schism are the "
                    "questions of its boundary, and our two conciliar formulas argue about how its "
                    "holders relate."
                ),
                "evidential": (
                    "The 256 Council preface carries our governing statement, directly quoted and "
                    "re-verified at source: 'judging no man, nor rejecting any one from the right of "
                    "communion, if he should think differently from us.' On Baptism, Against the "
                    "Donatists is the conduct evidence for the second phase -- disputing Cyprian's "
                    "specific ruling at book length without placing him outside; Letter 185 carries "
                    "the pastoral-corrective register. A full sweep returns roughly 120 occurrences "
                    "in Cyprian's corpus alone. The underlying quoted facts reach Documented; that "
                    "they together name one cross-phase pattern, rather than two separate facts, is "
                    "our own synthesis."
                ),
                "translational": (
                    "A modern listener is likely to hear either a specific liturgical rite -- going "
                    "up to receive -- or a general warmth of fellowship, and the second makes "
                    "disagreement look like a failure of communion. We mean a formal, structural "
                    "status of standing within the body, with public consequences, that is not "
                    "dissolved by disagreement. Disagreement is expected among us; what would break "
                    "communion is not arguing but separating."
                ),
            },
            quick_meaning=(
                "For us, communion is a real standing inside the one body. You can lose it, and "
                "you can be given it back. It can survive sharp disagreement between the people "
                "who hold it."
            ),
        ),
        "Re-derived from Doc_06 SS2.1 (lpclex005, Tier 1, G3 Primary -- 'the name of belonging "
        "itself in this world') and Lexicon-Chunks/lpclex005_communion.md. formation_confidence set "
        "to Widely Accepted rather than Documented, per the chunk's own explicit self-rating (see "
        "script docstring, CONFIDENCE PER TERM) -- this is the one term in this batch where the "
        "chunk states its own formation_confidence directly rather than leaving this script to "
        "infer it. Relations: fourteen terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "heresy",
        dict(
            confidence=conf(
                "A", "verified-direct", "load-bearing", "Documented",
                "De Unitate predates the Stephen controversy by several years and does not carry "
                "Cyprian's own anti-Stephen argument; the phrase episcopatus unus est is not "
                "evidence for that dispute, and this entry uses De Unitate for its general "
                "ecclesiology only. That row also carries an unresolved two-recension question for "
                "chapters 4-5 (one form, the 'Primacy Text,' more favourable to Roman primacy), on "
                "which nothing in this entry depends.",
            ),
            sources=[
                src(1, "the Epistles' own rebaptism correspondence"),
                src(4, "the 256 Council's own rebaptism ruling"),
                src(3, "De Unitate supplies the ecclesiology beneath the ruling -- 'He can no longer "
                       "have God for his Father, who has not the Church for his mother'"),
                src(13, "On Baptism, Against the Donatists -- 'As the baptized person, if he depart "
                        "from the unity of the Church, does not thereby lose the sacrament of "
                        "baptism, so also he who is ordained... does not lose the sacrament of "
                        "conferring baptism. For neither sacrament may be wronged'"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": split_clauses(
                    "participant asks about rebaptism, or whether baptism outside the church "
                    "counted; participant asks what heresy meant; participant asks why Cyprian and "
                    "Augustine disagreed; conversation reaches the Donatist question"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about doctrinal error in general, or about a later "
                    "inquisitorial sense of heresy, rather than about the validity of a specific act "
                    "performed outside one communion -- ask about the specific validity question "
                    "instead"
                ),
            },
            plain_meaning=(
                "For us, this word does not ask which belief is wrong. It asks one question: does "
                "a baptism given outside our one church count at all? We answer that question "
                "twice, in two different ways, a century apart."
            ),
            world_word="heresy",
            distortion_risk="high",
            false_friend=[
                "a settled, malicious deviation from an agreed orthodoxy, charged by an institution "
                "already confident of its own correctness",
                "an inquisitorial verdict with a foregone conclusion, rather than a genuinely open "
                "question argued at book length by both sides",
            ],
            senses={
                "informational": (
                    "Someone arrives who was washed elsewhere, by people who are not us. Is that "
                    "person baptized? One answer, Cyprian's own: no. What is given outside is not "
                    "given, because there is nothing outside to give it, so bring them to the "
                    "water. That is not a technicality; it follows from taking the one body "
                    "seriously, and it is ruled on in council and defended against Rome at real "
                    "cost. The other answer, a century and a third later, from a man arguing against "
                    "that very ruling: what was given outside was truly given, and does no good "
                    "where the person stands; bring them in, and what they already carry will begin "
                    "to work. The question does not go away between the two answers -- it gets "
                    "harder, because by the second time it is not one convert at the door but an "
                    "entire rival hierarchy holding the same towns. This is the question on which "
                    "communion is tested hardest, and the one that makes the boundary of the church "
                    "concrete rather than notional. It bears directly on reconciliation -- whether a "
                    "returning person is received or re-made -- and on the one episcopate, since a "
                    "rival consecration's validity decides whether the rival's own bishops are "
                    "bishops at all."
                ),
                "evidential": (
                    "The Epistles' rebaptism correspondence and the 256 Council's own ruling carry "
                    "Cyprian's side; De Unitate supplies the ecclesiology beneath it, directly "
                    "quoted -- 'He can no longer have God for his Father, who has not the Church for "
                    "his mother.' On Baptism, Against the Donatists carries Augustine's contrary "
                    "position, argued at length; the ordination passage quoted above is re-verified "
                    "at source, and a full sweep returns 687 occurrences of 'baptism' within that "
                    "one treatise. De Unitate's own general ecclesiology is used here; it predates "
                    "the Stephen controversy and does not carry Cyprian's own anti-Stephen argument."
                ),
                "translational": (
                    "A modern listener is likely to hear 'heresy' as settled, malicious deviation "
                    "from an agreed orthodoxy -- a charge levelled by an institution confident of "
                    "its own correctness, with a foregone conclusion. We mean a genuinely open "
                    "question, argued at book length by both sides, about whether a specific act "
                    "performed outside one communion is valid. Our two most respected figures answer "
                    "it in opposite directions, and the later one argues against the earlier one's "
                    "ruling while treating him as unquestionably inside the church."
                ),
            },
            quick_meaning=(
                "For us, this word does not ask which belief is wrong. It asks whether a baptism "
                "given outside our one church counts at all."
            ),
        ),
        "Re-derived from Doc_06 SS2.1 (lpclex006, Tier 1, G6 Primary -- 'the question on which "
        "communion is tested hardest') and Lexicon-Chunks/lpclex006_heresy.md. CT tag not applied, "
        "confirming rather than re-deriving Doc_03's own judgment that this in-world disagreement "
        "is not a live scholarly contest in Article 26's sense. Relations: eight terms per this "
        "term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "grace",
        dict(
            confidence=conf(
                "B", "verified-via-authority", "load-bearing", "Documented",
                "The entire evidentiary base for this term is one voice (Augustine) within one "
                "evidence stream (the anti-Pelagian corpus), flagged at generation rather than "
                "discovered afterwards (Author-Gravity-Risk: Yes). No Pelagian first-person answer "
                "survives in our own record. This term also carries a live scholarly contest, kept "
                "on its own, independent axis from this historical-fact rating -- see senses."
                "informational's own closing paragraph for the contest itself, per Doc_06 SS3.",
            ),
            sources=[
                src(23, "the anti-Pelagian corpus, licensed directly for the grace/sufficiency-test "
                        "gravity candidate; a full sweep, scoped to its own thirteen works, returns "
                        "1,798 raw / 1,665 markup-stripped occurrences of 'grace' -- by a wide "
                        "margin the highest raw-frequency count of any term in this lexicon"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": split_clauses(
                    "participant uses the word grace; participant asks about free will, merit, "
                    "predestination, or whether people can be good on their own; conversation "
                    "reaches Pelagius or the anti-Pelagian controversy"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about grace as a general modern religious "
                    "pleasantry or as gracefulness, or the conversation sits in Cyprian's own phase, "
                    "where this controversy does not yet exist -- ask about a Cyprian-phase term "
                    "instead"
                ),
            },
            plain_meaning=(
                "For us, grace names the insistence that no one's own effort is ever sufficient on "
                "its own. Whatever good a person manages was given to them before they managed it."
            ),
            world_word="grace",
            distortion_risk="high",
            false_friend=[
                "a warm general benevolence, or 'grace under pressure,' with no specific claim about "
                "the priority of divine action over human capacity",
                "a denominational shibboleth in a Protestant-Catholic argument the participant may "
                "already hold an opinion about",
            ],
            senses={
                "informational": (
                    "The claim is simple to state and hard to sit with: you did not start it. "
                    "Whatever you have made of yourself, something was given first, and subtract the "
                    "gift and nothing is left that would have moved -- not a boost to an effort "
                    "already under way, but the beginning of the effort. We argue this against a "
                    "real opponent who is not a fool: God commanded it, therefore it can be done; a "
                    "person who tries can obey. We refuse that, at length, again and again, because "
                    "the alternative makes all of pastoral work a matter of exhorting people to try "
                    "harder. And it lands in the congregation, not only in argument: the person who "
                    "has failed is told the failure is not the last word, and also that the recovery "
                    "will not be their own achievement. Grace is the one gravity in our own ecology "
                    "that is formation content rather than formation medium -- a sustained "
                    "catechetical and polemical project, propagated through preaching and "
                    "catechesis, structurally like penitential discipline in addressing the "
                    "compromised believer, but in a different register. It is also freestanding: "
                    "nothing else in our ecology depends on it resolving one way or the other."
                    "\n\n"
                    "This term also carries a live scholarly contest, kept apart from the historical "
                    "question of what Augustine himself wrote. Doc_06 names it Relationship to "
                    "present-day traditions, secondarily Meaning: the contest runs over how our own "
                    "historical position stands to the way living traditions use the word now -- the "
                    "Reformation-era and later appropriations, the Catholic-Protestant disagreements "
                    "that ran through them, and the modern scholarly reassessment of whether the "
                    "position we argue against is the one Pelagius himself actually held. A listener "
                    "arriving with this word is very often arriving from inside one of those later "
                    "arguments, not ours. This entry does not present our own anti-Pelagian position "
                    "as the settled meaning of the word across Christian history, and it does not "
                    "characterize Pelagius -- how we characterize our own opponents belongs "
                    "elsewhere, not to this lexicon."
                    "\n\n"
                    "Reported as our own self-understanding, not assessed here for historical "
                    "accuracy; confidence calibration applies to the historical-event layer only. "
                    "This term's formational centrality is exceptionally well evidenced -- the "
                    "highest raw frequency in this lexicon, across thirteen dedicated works -- and "
                    "what this status covers is the World Meaning above as a first-person rendering "
                    "of the conviction: how it was held and taught from inside, not a historical "
                    "assessment of the doctrine's own correctness."
                ),
                "evidential": (
                    "The anti-Pelagian corpus (Confidence B), licensed directly for this term, "
                    "carries the whole evidentiary base. A full sweep, scoped to its own thirteen "
                    "works and excluding the introductory essay, dedications, and indexes, returns "
                    "1,798 raw occurrences of 'grace' (1,665 markup-stripped) -- by a wide margin the "
                    "single highest raw-frequency count in this lexicon. The entire evidentiary base "
                    "is one voice within one evidence stream; the density of the evidence could "
                    "easily read as breadth, and is not. No Pelagian first-person answer survives in "
                    "our own Native record. This term belongs to Augustine's own phase; no "
                    "Pelagian-anthropology-equivalent material exists anywhere in Cyprian's corpus, "
                    "since the controversy postdates him by over a century."
                ),
                "translational": (
                    "A modern listener is likely to hear grace as a warm general benevolence, or as "
                    "'grace under pressure,' or as a denominational shibboleth they may already have "
                    "an opinion about, and to hear our anti-Pelagian position as harsh determinism. "
                    "We mean a specific and contested claim about the priority of divine action over "
                    "human capacity, argued against a named opponent over roughly a decade, with "
                    "direct consequences for how a congregation is taught, how failure is handled, "
                    "and what a pastor can reasonably ask of anyone."
                ),
            },
            quick_meaning=(
                "For us, grace means this: no one's own effort is ever enough. Whatever good a "
                "person does was given to them first."
            ),
        ),
        "Re-derived from Doc_06 SS2.1 (lpclex007, Tier 1, G7 Supporting -- 'the one gravity that is "
        "formation content rather than medium, and the highest-frequency term in the corpus by a "
        "wide margin') and Lexicon-Chunks/lpclex007_grace.md. CT Contest Type and Reported-"
        "Experience Status both folded into senses.informational as separated closing paragraphs -- "
        "`term` has no dedicated field for either (see script docstring, CT CONTEST TYPE FINDING and "
        "REPORTED-EXPERIENCE FINDING). The Reported-Experience marker is carried near-verbatim from "
        "the chunk's own Reported-Experience Status section; the chunk's own World Meaning opens "
        "with the identical sentence mis-pasted a section early, which this record does not repeat "
        "in plain_meaning or the informational paragraph's own opening (see script docstring, FIELD "
        "MAPPING, first bullet) -- flagged there, not silently carried forward twice. Relations: "
        "five terms per this term's own Related-Terms line.",
    ))

    return ids


# =============================================================================
# TIER 2 -- twelve entries (Doc_06 SS2.2-SS2.4): four moved down from Doc_03's
# Tier 1 proposal on an ecological finding (preaching, catechesis, bishop of
# bishops, plenary Council), one held at Tier 2 against the pull of its own
# risk profile (compel them to come in), two corrected upward from a
# mis-drafted Tier 3 (libelli, libellatici/sacrificati), and one term Doc_03
# never surfaced at all, added by the project lead's direction (certificates).
# Doc_06's own rule governs depth here, not this script's: "Tier 2 entries
# should not omit sections present in Tier 1 entries. Depth should compress;
# structure should not fragment" -- every one of these twelve still carries a
# real senses.informational/evidential/translational, not a stub.
# =============================================================================

def build_tier2_terms() -> list[str]:
    ids = []

    ids.append(emit_term(
        "preaching",
        dict(
            confidence=conf("A", "verified-direct", "corroborating", "Documented",
                             "Down-tiered from Doc_03's own Tier 1 proposal, which rested on raw "
                             "frequency (119 occurrences of 'preach' within the Sermons alone). "
                             "Doc_05 SS5.2's own ecological finding is that this gravity functions "
                             "as the medium the other gravities are taught and enforced through, "
                             "not as an independently organizing force -- raw frequency measured the "
                             "volume of the channel, not the weight of what it carries."),
            sources=[
                src(19, "the Sermons, roughly 97 sermons, about 308,000 words; Sermon I.1 -- 'I am "
                        "not speaking to hearts that are deaf, and to minds that will disdain the "
                        "word, but this your longing expectation is a prayer for me'"),
                src(21, "the Tractates on John, exegetical preaching"),
                src(5, "Cyprian's own pastoral treatises, several originally preached or read to "
                       "the Carthaginian church"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks what happened at a service, or what a bishop actually did "
                    "week to week; participant asks how ordinary believers learned anything; "
                    "participant asks about sermons"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about instruction of those not yet baptized rather "
                    "than the weekly address to the baptized -- ask about catechesis instead"
                ),
            },
            plain_meaning=(
                "You are baptized, so you are in the room. Week by week, the same voice works on "
                "you. It is not a lecture and not a show. It is the man in charge of you, telling "
                "you to your face what he thinks you need."
            ),
            world_word="preaching",
            distortion_risk="medium",
            false_friend=[
                "a stern moralizing monologue, or a polished performance piece, assumed to be one "
                "component of a service among several rather than the central formative act",
            ],
            senses={
                "informational": (
                    "You are baptized, so you are in the room, and week by week the same voice "
                    "works on you. It is not a lecture and not entertainment; it is the man "
                    "answerable for you saying what he thinks you need, to your faces, knowing "
                    "which of you are missing. Preaching is the medium, not itself an organizing "
                    "force: it is how the flock's own answerability, our discipline's decisions, "
                    "and our grace controversy actually arrive at a believer. Catechesis is its "
                    "paired term, distinguished by audience. This is how our formation is "
                    "delivered -- by voice, weekly, in person, by the same man who administers "
                    "everything else."
                ),
                "evidential": (
                    "The Sermons carry this term's own evidence; a full sweep returns 119 "
                    "occurrences of 'preach' within their own bounds alone, and Sermon I.1's own "
                    "opening -- quoted above -- is directly re-verified at source. Doc_03 flagged "
                    "this Tier 1 on that raw frequency; Doc_05 SS5.2 found the underlying ecological "
                    "role is as the medium the other gravities are taught through, not an "
                    "independently organizing force, which is why this term now sits at Tier 2."
                ),
                "translational": (
                    "A modern listener may hear either a stern moralizing monologue or a polished "
                    "performance piece, and assume it is one component of a service among several. "
                    "For us it was the central formative act of ordinary life, delivered by the "
                    "person personally answerable for the hearers, occasional and responsive rather "
                    "than scripted, and openly aware of what it competed with for people's own "
                    "attention."
                ),
            },
            quick_meaning=(
                "For us, preaching is the weekly talk to those already baptized. It is how nearly "
                "everything else we hold reaches an ordinary believer."
            ),
        ),
        "Re-derived from Doc_06 SS2.2 (lpclex008, down-tiered to Tier 2 -- 'the single largest "
        "divergence in this world between textual abundance and ecological weight') and "
        "Lexicon-Chunks/lpclex008_preaching.md. Relations: five terms per this term's own "
        "Related-Terms line.",
    ))

    ids.append(emit_term(
        "catechesis",
        dict(
            confidence=conf("B", "verified-via-authority", "corroborating", "Documented",
                             "Attested through dedicated treatises rather than raw recurrence of a "
                             "headword -- a different, but not weaker, kind of ground: a manual "
                             "written to instruct instructors is stronger evidence of a practice's "
                             "own centrality than word-frequency alone would be. Down-tiered from "
                             "Doc_03's own Tier 1 proposal alongside preaching, on the same Doc_05 "
                             "SS5.2 medium-not-force finding."),
            sources=[
                src(15, "On the Catechising of the Uninstructed, a manual for the practice itself, "
                        "not merely an instance of it"),
                src(18, "the creedal works, teaching catechumens the baptismal creed directly"),
                src(9, "the Confessions, narrating a catechumenate and baptism from the inside"),
                src(5, "On the Lord's Prayer, catechetical exposition of the church's own set "
                       "prayer"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks how someone joined this church; participant asks about "
                    "catechumens, or what happened before baptism; participant asks what new "
                    "believers were taught"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about the weekly address to the baptized rather "
                    "than instruction before baptism -- ask about preaching instead"
                ),
            },
            plain_meaning=(
                "You are taught before you are washed. We tell you what you are joining before "
                "you join it. You say the creed back, and then we baptize you."
            ),
            world_word="catechesis",
            distortion_risk="medium",
            false_friend=[
                "a children's catechism -- rote question-and-answer, memorized young, faintly dry",
            ],
            senses={
                "informational": (
                    "You are taught before you are washed. That order is not an accident: you are "
                    "told what you are joining before you join it, and you say it back before "
                    "anyone washes you. There is enough of this work that a manual gets written for "
                    "the people who do it -- not a record of one instance but a book about how to do "
                    "it at all, including what to do when the person in front of you is bored, or "
                    "clever, or frightened. Catechesis is the other half of our formation medium, "
                    "distinguished from preaching by audience. It is where the creed enters, which "
                    "makes it the practical route by which our own boundary questions and our own "
                    "account of grace first reach a person."
                ),
                "evidential": (
                    "On the Catechising of the Uninstructed is a manual for the practice itself, not "
                    "merely an instance of it; the creedal works teach the baptismal creed to "
                    "catechumens directly; the Confessions narrate a catechumenate and baptism from "
                    "the inside; On the Lord's Prayer is catechetical exposition of our own set "
                    "prayer. This term is attested through dedicated treatises rather than raw "
                    "headword recurrence -- a manual written to instruct instructors is stronger "
                    "evidence of centrality than word-frequency would be."
                ),
                "translational": (
                    "A modern listener may hear a children's catechism -- rote question-and-answer, "
                    "memorized young, faintly dry. We mean adult instruction, before baptism, of "
                    "people making a consequential change of standing, taken seriously enough that a "
                    "working manual for instructors exists."
                ),
            },
            quick_meaning=(
                "For us, catechesis means teaching people before they are baptized. We teach them "
                "the creed, and the basics of belief, before the water, not after it."
            ),
        ),
        "Re-derived from Doc_06 SS2.2 (lpclex009, down-tiered to Tier 2 alongside preaching) and "
        "Lexicon-Chunks/lpclex009_catechesis.md. Relations: five terms per this term's own "
        "Related-Terms line.",
    ))

    ids.append(emit_term(
        "the-people",
        dict(
            confidence=conf("A", "verified-direct", "corroborating", "Documented",
                             "This world's own corpus does not attest the Latin plebs as either "
                             "bishop's own word: a sweep of the vendored Cyprian corpus returns "
                             "exactly three occurrences, all three inside the 19th-century American "
                             "editor's own introductory and elucidatory prose, none inside Cyprian's "
                             "own letters. 'The people' is this corpus's own recurring English "
                             "rendering for the congregation as an acting body, disclosed here as a "
                             "working handle rather than an attested headword."),
            sources=[
                src(1, "Epistle XXXIX, addressed to the people concerning five schismatic "
                       "presbyters"),
                src(11, "Letter CXXVI carries the Hippo episode; Augustine's own account of "
                        "accepting the episcopate cites 'the love of Valerius and the importunity "
                        "of the people'"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks whether ordinary believers had any say; participant asks how "
                    "bishops were chosen; participant asks whether the laity could push back "
                    "against clergy"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about the congregation as the object of pastoral "
                    "care rather than as an acting body -- ask about the flock instead"
                ),
            },
            plain_meaning=(
                "We are not a silent audience. We put men into office, and we say so out loud. We "
                "can stand in front of a bishop's own seat and refuse to go home."
            ),
            world_word="the people",
            distortion_risk="high",
            false_friend=[
                "a passive congregation with no real leverage over its own clergy",
                "a modern democratic electorate, with a formal ballot and a fixed voting procedure",
            ],
            senses={
                "informational": (
                    "We are not an audience. We put men into office and say so out loud; we can "
                    "also stand in front of a bishop's own seat and refuse to go home. At Hippo in "
                    "411 the people wanted a particular wealthy man made their presbyter and did not "
                    "get him; they clamoured, they abused another bishop present, and when told the "
                    "bishop was bound by a promise they grew still more excited, calculating the "
                    "promise might break. He held his ground. Real leverage, loudly exercised, and "
                    "finally bounded by one man's refusal -- that is the shape of it. This is the "
                    "active face of the flock and the ground of suffrage."
                ),
                "evidential": (
                    "Epistle XXXIX is addressed to the people concerning five schismatic "
                    "presbyters; Letter CXXVI carries the Hippo episode, re-verified at source; "
                    "Augustine's own account cites 'the love of Valerius and the importunity of the "
                    "people.' Our own corpus does not attest the Latin plebs as either bishop's own "
                    "word -- a sweep returns exactly three occurrences, all inside the 19th-century "
                    "editor's own prose, none inside Cyprian's own letters -- so 'the people' is our "
                    "corpus's own recurring English rendering, not an attested Latin headword."
                ),
                "translational": (
                    "A modern listener may hear either a passive congregation or a modern "
                    "democratic electorate with formal voting rights. Neither is right. A corporate "
                    "body whose consent and demand genuinely constitute a call to office, and which "
                    "can be exerted disruptively, but which holds no procedural mechanism and can "
                    "still be refused."
                ),
            },
            quick_meaning=(
                "For us, 'the people' names the congregation when it acts. They consent, they "
                "demand, and they elect -- unlike the flock, which is the congregation being cared "
                "for."
            ),
        ),
        "Re-derived from Doc_03 Section A (candidate roster, Tier 2 -- 'supporting and "
        "disambiguating the suffrage entry') and Doc_06 SS2's own Tier 2 confirmation, plus "
        "Lexicon-Chunks/lpclex010_the-people.md. Relations: five terms per this term's own "
        "Related-Terms line.",
    ))

    ids.append(emit_term(
        "suffrage",
        dict(
            confidence=conf("A", "verified-direct", "corroborating", "Documented",
                             "The pattern is attested through different figures and different words "
                             "-- and at the same office (the episcopate) in both phases, per the "
                             "project lead's own ruling of 2026-09-16 -- not one recurring term. "
                             "Named as a pattern, not presented as a shared vocabulary item. Carried "
                             "tension, flagged rather than resolved here: Lexicon_Deployment_Index."
                             "md SS3 records that this term carries no [DR] tag although Doc_06 SS4 "
                             "names it a sharpest-case distortion ('suffrage' hears as a modern "
                             "franchise); this script maps distortion_risk from the tag set as "
                             "recorded, per its own docstring (DISTORTION_RISK MAPPING), rather than "
                             "silently override another thread's own classification."),
            sources=[
                src(1, "Epistle XXXIX -- 'your suffrage and God's judgment,' against a rival "
                       "faction's 'ancient venom'"),
                src(7, "Pontius's Life of Cyprian, a third, non-episcopal witness -- 'by the "
                       "judgment of God and the favour of the people, he was chosen to the office "
                       "of the priesthood and the degree of the episcopate while still a neophyte'"),
                src(11, "Letters XXXI and CCXIII carry Augustine's own accounts"),
                src(192, "Possidius's Vita, read in full; chapters IV and VIII carry Augustine's own "
                         "two offices"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks how Cyprian or Augustine came to office; participant asks "
                    "whether anyone wanted these jobs; participant asks about reluctance to be "
                    "ordained"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about the congregation's ongoing authority "
                    "generally rather than the specific act of calling someone to office -- ask "
                    "about the people instead"
                ),
            },
            plain_meaning=(
                "Cyprian's own word for what put him in office was suffrage. A rival group opposed "
                "him, but the people chose him anyway."
            ),
            world_word="suffrage",
            distortion_risk="medium",
            false_friend=[
                "the right to vote, with an expected franchise, a ballot, and a fixed procedure",
            ],
            senses={
                "informational": (
                    "Cyprian's own word for what elected him is 'your suffrage and God's judgment,' "
                    "set against a rival faction's 'ancient venom.' A deacon who knew him reports "
                    "the same thing from outside: chosen 'by the judgment of God and the favour of "
                    "the people... while still a neophyte.' The pattern recurs in the second phase "
                    "but not identically: Augustine was seized into the presbyterate at Hippo "
                    "against his own wishes; his episcopate came by his predecessor's designation "
                    "and consecration, and, at the same event, by the acclamation of all who heard "
                    "it, which he refused before yielding under compulsion. This is the entry point "
                    "of the flock: how a man acquires the charge he will then be answerable for, "
                    "and why our authority carries an obligation running back toward the people."
                ),
                "evidential": (
                    "Epistle XXXIX is directly quoted and re-verified at source; Pontius's Life of "
                    "Cyprian is a third, non-episcopal witness, likewise re-verified; Letters XXXI "
                    "and CCXIII carry Augustine's own accounts. Possidius's Vita has been read in "
                    "full, and chapters IV and VIII are what this entry's own account of Augustine's "
                    "two offices rests on. The pattern is attested through different figures and "
                    "different words, at the same office in both phases, not one recurring term."
                ),
                "translational": (
                    "A modern listener will hear 'suffrage' as the right to vote, and expect a "
                    "franchise, a ballot, and a procedure. We mean neither. A corporate acclamation "
                    "that carries real constitutive force, in a community where the man acclaimed "
                    "is expected to resist and where an organized faction can oppose without "
                    "stopping it."
                ),
            },
            quick_meaning=(
                "For us, suffrage is the voice of the people that puts a man into office. It often "
                "goes against his own wishes."
            ),
        ),
        "Re-derived from Doc_03 Section A (Tier 2, cross-phase pattern) and Doc_06 SS2's own Tier 2 "
        "confirmation, plus Lexicon-Chunks/lpclex011_suffrage.md. No [PV] tag, matching Doc_03's own "
        "explicit rule-out by name. Relations: three terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "bishop-of-bishops",
        dict(
            confidence=conf("A", "verified-direct", "load-bearing", "Documented",
                             "The vendored ANF text prints an editor's remark inside this passage -- "
                             "reading it as a rebuke of Stephen of Rome specifically. That is the "
                             "19th-century American editor's own reading of Cyprian's motive, not "
                             "Cyprian's own words, and no claim in this entry rests on the formula "
                             "being aimed at Stephen. Doc_04 finds no evidence that ordinary "
                             "believers, catechumens, or most clergy in either phase were formed by, "
                             "or aware of, this question -- the formula's own existence is "
                             "Documented; its reach into ordinary formation is not evidenced, which "
                             "is why this term sits at Tier 2 despite that Documented status."),
            sources=[
                src(4, "the 256 Council preface -- 'For neither does any of us set himself up as a "
                       "bishop of bishops, nor by tyrannical terror does any compel his colleague to "
                       "the necessity of obedience; since every bishop... has his own proper right "
                       "of judgment'"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks whether one bishop could overrule another; participant asks "
                    "about church government, councils, or the origins of papal authority; "
                    "participant asks how disputes between bishops were settled"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about a bishop's own authority over his own "
                    "congregation rather than about bishops' authority over each other -- ask about "
                    "the flock instead"
                ),
            },
            plain_meaning=(
                "For us, this is a simple rule, said at the start of a council: no bishop stands "
                "over another. Each bishop judges for himself, and answers for it elsewhere."
            ),
            world_word="bishop of bishops",
            distortion_risk="medium",
            false_friend=[
                "an early anti-papal manifesto",
                "a modern constitutional principle about the separation of powers among equal "
                "branches of government",
            ],
            senses={
                "informational": (
                    "Said out loud by the man presiding, before the voting begins, at the council "
                    "that will rule on the sharpest question in the room: no one of us sets himself "
                    "up as a bishop of bishops, and none compels a colleague by tyrannical terror, "
                    "since every bishop holds his own proper right of judgment. It is a statement "
                    "about what a council is -- not a tribunal handing down a verdict that binds the "
                    "unwilling, but a gathering of men each of whom says what he holds and answers "
                    "for it to someone other than the man in the chair. Together with plenary "
                    "Council, this forms our own conciliar-authority pair, and the two are "
                    "incompatible. It underwrites communion's own capacity to survive disagreement: "
                    "if no one can compel a colleague, disagreement need not mean separation."
                ),
                "evidential": (
                    "The 256 Council preface is directly quoted and re-verified at source, and "
                    "re-quoted across nine independent review rounds. The vendored text prints an "
                    "editor's remark inside this passage reading it as a rebuke of Stephen of Rome; "
                    "that is the 19th-century editor's own reading of motive, not Cyprian's words, "
                    "and nothing here rests on it. Doc_04 finds no evidence this question reached "
                    "ordinary believers, catechumens, or most clergy in either phase -- the formula "
                    "is real and Documented; its reach into ordinary life is not evidenced."
                ),
                "translational": (
                    "A modern listener is likely to hear an early anti-papal manifesto, or a "
                    "democratic constitutional principle about separated powers. We mean neither -- "
                    "a working statement of how a council among equals proceeds, made by the man "
                    "chairing it, inside a shared conviction that the episcopate is one undivided "
                    "office rather than a hierarchy of ranks."
                ),
            },
            quick_meaning=(
                "For us, no bishop stands over the others. Each one judges for himself, and "
                "answers for it elsewhere."
            ),
        ),
        "Re-derived from Doc_06 SS2.2 (lpclex012, down-tiered to Tier 2 -- 'no evidence that "
        "ordinary believers... were formed by, or even aware of, this question') and "
        "Lexicon-Chunks/lpclex012_bishop-of-bishops.md. AUTHORED call, not chunk-stated: "
        "evidentiary_weight set to load-bearing despite Tier 2. The chunk itself never uses "
        "the term; this script infers it because the formula is the sole textual ground of a "
        "real, Documented Supporting gravity (the conciliar-authority axis), which Doc_04 SS7 "
        "item 2 forbids suppressing -- Tier and evidentiary_weight are independent axes, the "
        "same rule don's own script states. "
        "Relations: five terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "plenary-council",
        dict(
            confidence=conf("A", "verified-direct", "load-bearing", "Documented",
                             "AUTHORED call, not chunk-stated: evidentiary_weight set to "
                             "load-bearing despite this term's own Tier 2 placement, on the "
                             "same independent-axes reasoning as the paired bishop-of-bishops "
                             "entry -- neither chunk (lpclex012, lpclex013) uses the term "
                             "itself. Augustine's own formula is spoken in defence of overturning "
                             "Cyprian's specific ruling; his institutional interest in the argument "
                             "runs opposite to Cyprian's in the paired bishop-of-bishops entry, "
                             "which is why this record does not treat the two formulas as "
                             "reconcilable restatements of one theory (Author-Gravity-Risk: Yes). "
                             "The same ecological bound as the paired entry applies: no evidence "
                             "this question reached ordinary formation in either phase."),
            sources=[
                src(13, "On Baptism, Against the Donatists II.3 -- 'The Councils themselves, which "
                        "are held in the several districts and provinces, must yield, beyond all "
                        "possibility of doubt, to the authority of plenary Councils which are "
                        "formed for the whole Christian world; and... even of the plenary Councils, "
                        "the earlier are often corrected by those which follow them'"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks whether church councils could be wrong, or could be "
                    "corrected; participant asks how Augustine justified overturning Cyprian's "
                    "ruling; participant asks about conciliar authority or development of doctrine"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about a specific council's own decisions rather than "
                    "about the theory of conciliar authority itself -- ask about the specific "
                    "council instead"
                ),
            },
            plain_meaning=(
                "Two ideas sit in one sentence here. A small council yields to a wider one -- that "
                "is a hierarchy. But even the widest council can later be corrected, because the "
                "church learns."
            ),
            world_word="plenary Council",
            distortion_risk="medium",
            false_friend=[
                "a straightforward claim of centralized institutional authority, missing that the "
                "same sentence makes that authority revisable",
            ],
            senses={
                "informational": (
                    "Two moves sit in one sentence, and the second is the surprising one. Narrower "
                    "yields to wider -- that is a hierarchy. But the widest is itself revisable, "
                    "because the church learns. A past ruling is authoritative and correctable at "
                    "the same time, which is precisely what a man needs who intends to honour a "
                    "predecessor while overturning what he decided. This is the hinge of our own "
                    "interpretive tradition: it makes a prior ruling into a body of arguable "
                    "precedent rather than fixed deposit. It is deployed specifically against the "
                    "earlier ruling on heresy and rebaptism, and it stands in direct contradiction "
                    "to the paired bishop-of-bishops formula."
                ),
                "evidential": (
                    "On Baptism, Against the Donatists II.3 is directly quoted and re-verified at "
                    "source; a full sweep returns 31 occurrences of 'plenary' within the treatise "
                    "itself. Augustine's own formula is spoken in defence of overturning Cyprian's "
                    "specific ruling, his institutional interest running opposite to Cyprian's own "
                    "in the paired entry. The same ecological bound as that paired entry applies: no "
                    "evidence this question reached ordinary formation in either phase."
                ),
                "translational": (
                    "A modern listener is likely to hear a straightforward claim of centralized "
                    "institutional authority -- Rome or a general council laying down the law -- and "
                    "miss that the same sentence makes that authority revisable. We mean a layered, "
                    "self-correcting account: wider bodies outrank narrower ones, and the widest are "
                    "corrected by later ones as understanding develops, both asserted together by "
                    "one man using both halves at once."
                ),
            },
            quick_meaning=(
                "For us, this is the other rule: small councils yield to bigger ones. Even the "
                "biggest council can later be corrected."
            ),
        ),
        "Re-derived from Doc_06 SS2.2 (lpclex013, down-tiered to Tier 2 alongside bishop-of-bishops) "
        "and Lexicon-Chunks/lpclex013_plenary-council.md. evidentiary_weight set to load-bearing on "
        "the same independent-axis reasoning as its paired entry (see bishop-of-bishops' own "
        "provenance note). Relations: four terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "the-one-episcopate",
        dict(
            confidence=conf("B", "verified-via-authority", "corroborating", "Documented",
                             "De Unitate predates the Stephen controversy by several years and does "
                             "not carry Cyprian's own anti-Stephen argument; the phrase episcopatus "
                             "unus est is not evidence for that dispute, and this entry uses the "
                             "treatise for its general ecclesiology only, per Doc_03's own explicit "
                             "instruction that the caution be carried forward. That row also carries "
                             "an unresolved two-recension question for chapters 4-5, on which "
                             "nothing in this entry depends."),
            sources=[
                src(3, "De Unitate, Cyprian's own ecclesiology of the single, undivided episcopate"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks what held the bishops together, or what made them one "
                    "church rather than many; participant asks about the theological basis of "
                    "church unity"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about a specific bishop's own charge over his own "
                    "congregation rather than the shared office itself -- ask about the flock "
                    "instead"
                ),
            },
            plain_meaning=(
                "For us, the episcopate is a single, undivided office held corporately. Each "
                "bishop holds the whole of it in his own place, not a share of it."
            ),
            world_word="the one episcopate",
            distortion_risk="medium",
            false_friend=[
                "a bureaucratic hierarchy of ranked officers",
                "a loose federation of independent congregations, each with authority all its own",
            ],
            senses={
                "informational": (
                    "This is not a federation of independent officers and not a chain of command. "
                    "One office, held entire by each man who holds it, in the place where he holds "
                    "it. A colleague's judgment cannot simply be overridden, because he is not "
                    "holding a lesser portion, and separation is so serious for exactly the same "
                    "reason: to break from the body is not to leave an organization but to step "
                    "outside the thing itself. This is the doctrinal ground beneath both conciliar "
                    "formulas -- the reason the egalitarian principle can be stated at all, and the "
                    "thing the hierarchical one has to work within. It also underwrites communion "
                    "and gives schism its own real gravity."
                ),
                "evidential": (
                    "De Unitate carries this ecclesiology. The treatise predates the Stephen "
                    "controversy by several years and does not carry Cyprian's own anti-Stephen "
                    "argument; the phrase episcopatus unus est is not evidence for that dispute, "
                    "and this entry draws on the treatise for its general ecclesiology alone. The "
                    "treatise also carries an unresolved two-recension question for chapters 4-5 -- "
                    "one form, the 'Primacy Text,' more favourable to Roman primacy -- on which "
                    "nothing here depends."
                ),
                "translational": (
                    "A modern listener may hear either a bureaucratic hierarchy or a loose "
                    "association of independent congregations. We mean neither: a single office "
                    "shared corporately and held whole by each holder, which makes both equality "
                    "among bishops and the seriousness of separation follow from the same "
                    "conviction."
                ),
            },
            quick_meaning=(
                "For us, the episcopate is one office, shared by every bishop. Each bishop holds "
                "the whole of it, not just a part."
            ),
        ),
        "Re-derived from Doc_03 Section C (Tier 2, doctrinal ground beneath the paired formulas) "
        "and Doc_06 SS2's own Tier 2 confirmation, plus Lexicon-Chunks/lpclex014_the-one-"
        "episcopate.md. Relations: eight terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "schism",
        dict(
            confidence=conf("B", "verified-via-authority", "corroborating", "Documented",
                             "How this world characterizes its own opponents -- the Donatists "
                             "specifically -- belongs to a later, separate step and this world's "
                             "eventual Representative, not to this lexicon; this entry names the "
                             "general concept only and does not characterize Donatism."),
            sources=[
                src(3, "De Unitate, the general treatise on schism and the one episcopate"),
                src(13, "On Baptism, Against the Donatists, the cross-phase grounding"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks what schism meant, or how it differs from heresy; "
                    "participant asks about division in the early church; conversation reaches the "
                    "Donatists or the Novatianists"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about the validity of sacraments performed outside "
                    "the church rather than about division itself -- ask about heresy instead"
                ),
            },
            plain_meaning=(
                "We argue hard, and we stay. Schism is the other thing: when arguing stops, and a "
                "new altar and a new bishop appear in the same town."
            ),
            world_word="schism",
            distortion_risk="medium",
            false_friend=[
                "a normal, unremarkable feature of a plural religious landscape, carrying no great "
                "weight",
            ],
            senses={
                "informational": (
                    "Disagreement is not this. We argue hard, and stay. Schism is the other thing: "
                    "when the arguing stops being argument and becomes a separate altar, a separate "
                    "bishop, a separate people in the same town. The difference is not the intensity "
                    "of the dispute; it is whether anyone walked out. Schism is the negative "
                    "boundary of communion and the thing the one episcopate exists to make "
                    "intelligible. It is also where we draw our own line against our neighbours: "
                    "the conviction that disagreement is survivable and separation is not."
                    "\n\n"
                    "This term also carries a live scholarly contest. Doc_06 names it Application to "
                    "this world, secondarily Historical scope: whether the heresy/schism distinction "
                    "was as stable in this period as later usage implies, and how far the category "
                    "in practice describes a real ecclesial situation as against a polemical "
                    "instrument used by the side that eventually prevailed. The North African case "
                    "is the field's own central example. This entry does not present the "
                    "distinction as a neutral technical taxonomy, and it does not settle whether our "
                    "own application of the category to our rivals was accurate."
                ),
                "evidential": (
                    "De Unitate is the general treatise on schism and the one episcopate; On "
                    "Baptism, Against the Donatists supplies the cross-phase grounding. A full "
                    "sweep returns 103 occurrences of 'schism' in Cyprian's corpus alone. How this "
                    "world characterizes its own opponents belongs to a later, separate step, not "
                    "to this entry, which names the general concept only."
                ),
                "translational": (
                    "A modern listener is likely to hear denominational difference -- a normal, "
                    "unremarkable feature of a plural religious landscape. We mean a tearing of a "
                    "single body, with real consequences for standing, sacraments, and ordinary life "
                    "in a town where both parties are present -- not one option among many, but the "
                    "outcome we organize ourselves to avoid."
                ),
            },
            quick_meaning=(
                "For us, schism means a real split inside the one body of bishops, over belief or "
                "over practice. It is a tear, not a mere argument."
            ),
        ),
        "Re-derived from Doc_06 SS2/SS3 (lpclex015, Tier 2, CT tagged -- Application to this world, "
        "secondarily Historical scope) and Lexicon-Chunks/lpclex015_schism.md. CT Contest Type "
        "folded into senses.informational per this script's own schema-forced placement rule. "
        "Relations: five terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "compel-them-to-come-in",
        dict(
            confidence=conf("A", "verified-direct", "corroborating", "Documented",
                             "This doctrine is known in our own corpus only through Augustine's own "
                             "advocacy, in his own defence, with no Donatist first-person answer "
                             "surviving in our Native record (Author-Gravity-Risk: Yes). The "
                             "vendored volume's own 19th-century preface calls this doctrine 'a "
                             "false exegesis' and 'least satisfactory to Protestant readers' -- that "
                             "is the editor's own theological verdict, not Augustine's and not "
                             "ours, and it is excluded entirely from this record."),
            sources=[
                src(12, "Letter 185, SS25-26, the imperial-coercion defence"),
                src(43, "Letter XCIII, SS17, the retrospective account of the earlier, contrary "
                        "opinion"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks whether force was used against dissenters; participant "
                    "raises religious persecution, tolerance, or church and state; participant asks "
                    "about the Donatists' own treatment"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about penitential discipline applied to members "
                    "inside the community rather than compulsion against a separated party -- ask "
                    "about reconciliation instead"
                ),
            },
            plain_meaning=(
                "For us, this is a late argument, and it goes against an earlier view of our own. "
                "A Christian ruler may rightly use force to bring a separated group back into the "
                "one communion."
            ),
            world_word="compel them to come in",
            distortion_risk="high",
            false_friend=[
                "a straightforward endorsement of religious persecution, attached to later "
                "inquisitions and wars of religion as if it were our own settled position "
                "throughout",
            ],
            senses={
                "informational": (
                    "The argument turns on a parable: a householder's feast, the invited guests "
                    "excuse themselves, and the servant is sent to the highways and hedges to "
                    "compel them to come in, that the house may be filled. It was not said 'compel' "
                    "of those who came first, because the early church could not compel -- it was "
                    "only growing toward the strength in which it could. The later church can, and "
                    "so may. This is the end of a three-phase development, and our own record does "
                    "not permit compressing it into one position: an early opinion, by later "
                    "account, against any coercion at all; then a real but narrow solicitation of "
                    "legal protection, argued and not granted; and only later the sustained defence "
                    "of broader compulsion, after an argued change of mind. Cyprian never solicits "
                    "state power at all, and nothing in his own phase corresponds to this. It is "
                    "where our second phase meets the power available to it, and the sharpest test "
                    "of our own claim that communion is preserved rather than broken: the coercion "
                    "is argued as recovering a separated party, not expelling one still inside. It "
                    "is not an organizing force of our own ecology, and that is a finding rather "
                    "than an omission -- nothing in this ecology organizes around it; the shift "
                    "changes the instruments available to a bishop, not the thing a bishop is."
                    "\n\n"
                    "This term also carries a live scholarly contest. Doc_06 names it Relationship "
                    "to present-day traditions, secondarily Meaning: it is the single most-cited "
                    "patristic warrant in the modern historiography of religious coercion, and the "
                    "argument runs over how far this position is the ancestor of later inquisitorial "
                    "practice, how far our own framing as pastoral correction should be credited, "
                    "and whether the three-phase development is a genuine change of mind or a "
                    "retrospective self-presentation. This entry does not adjudicate that "
                    "historiographical question, does not endorse or condemn the position, and does "
                    "not characterize the Donatists."
                ),
                "evidential": (
                    "Letter 185, SS25-26, the imperial-coercion defence, and Letter XCIII, SS17, the "
                    "retrospective account of the earlier opinion, are both directly quoted and "
                    "re-verified. The parable exegesis is Augustine's own, re-verified at source. "
                    "This doctrine is known in our own corpus only through Augustine's own "
                    "advocacy, in his own defence, with no Donatist first-person answer surviving "
                    "in our Native record; he writes from a position of increasing institutional "
                    "confidence relative to Donatism. The vendored volume's own 19th-century preface "
                    "calls this doctrine 'a false exegesis' and 'least satisfactory to Protestant "
                    "readers' -- the editor's own judgement, not Augustine's and not ours, excluded "
                    "entirely from this record."
                ),
                "translational": (
                    "A modern listener is likely to hear a straightforward endorsement of religious "
                    "persecution, and to attach it to later inquisitions and wars of religion as if "
                    "it were our own settled position throughout. We mean a late, argued position, "
                    "reached against the author's own earlier opinion, defended in the idiom of "
                    "correction and recovery rather than punishment -- in a world where the same "
                    "author's predecessor a century earlier had no access to state power at all and "
                    "never sought it."
                ),
            },
            quick_meaning=(
                "For us, this is a late argument. A Christian ruler may use force to bring a "
                "separated group back into the one communion."
            ),
        ),
        "Re-derived from Doc_06 SS2.3 ('the hard case'; 'by a distance the single most dangerous "
        "term in this lexicon,' retained at Tier 2 on Doc_04 SS2's own finding that it does not "
        "organize this ecology) and Lexicon-Chunks/lpclex016_compel-them-to-come-in.md. CT Contest "
        "Type folded into senses.informational per this script's own schema-forced placement rule; "
        "the editorial Protestant-editor verdict is named and excluded, never absorbed into any "
        "field here. Relations: five terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "libelli",
        dict(
            confidence=conf(
                "D", "unverified", "illustrative", "Inferential-Thin",
                "A direct check finds the Latin headword absent from this world's own vendored "
                "English corpus altogether. The volume's single occurrence of the word-family sits "
                "in the Introductory Notice to the anonymous treatise against Novatian, not in De "
                "Lapsis. This term is carried as supporting reference vocabulary for the lapsed, on "
                "Doc_01's own gloss rather than on attestation in this world's own primary text -- a "
                "named gap, not filled with a confidence rating the source cannot support. Compare "
                "lpc.term.certificates-letters-of-peace, which attests the English word the translation actually "
                "uses for the confessors' own opposite-direction document.",
            ),
            sources=[
                src(8, "the Introductory Notice to the anonymous treatise against Novatian -- the "
                       "volume's own single occurrence of the 'libell-' word-family, not an "
                       "occurrence of 'libelli' bare, and not inside De Lapsis"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks how the persecution was actually administered; participant "
                    "asks what a certificate was, or how someone could lapse without sacrificing"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about the category of persons rather than the "
                    "document itself -- ask about the lapsed instead; also: this corpus uses the "
                    "bare word certificate for two different documents travelling in opposite "
                    "directions -- this is the one the empire issued, which made a person lapsed; "
                    "the confessors' own letter of peace, which asks the church to take a person "
                    "back, is a separate term (certificates) and a participant asking simply what a "
                    "certificate was should be pointed to both"
                ),
            },
            plain_meaning=(
                "Rome did not ask anyone to renounce Christ in writing. It asked for a sacrifice, "
                "then wrote down that one had been made. Some people paid money for that paper "
                "instead of sacrificing at all."
            ),
            world_word="libelli",
            distortion_risk="low",
            false_friend=[
                "a formal identity document or licence, in the modern administrative sense",
            ],
            senses={
                "informational": (
                    "The empire did not ask anyone to renounce Christ in writing. It asked for a "
                    "sacrifice, and then wrote down that one had been made. A demand satisfied with "
                    "money rather than incense produced a class of people who had not, in their own "
                    "minds, worshipped anything, and who nonetheless held a document saying they "
                    "had. This is the administrative fact underneath the lapsed, and therefore "
                    "underneath our whole penitential discipline and the confessor-authority "
                    "tension: the crisis was documentary rather than merely moral."
                ),
                "evidential": (
                    "Doc_01's own gloss is the operative source for this term's meaning. A direct "
                    "check finds the Latin headword absent from our vendored English corpus "
                    "altogether; the volume's one occurrence of the word-family sits in the "
                    "Introductory Notice to the anonymous treatise against Novatian, not in De "
                    "Lapsis. This term is carried as supporting reference vocabulary, on the gloss "
                    "rather than direct primary-text attestation."
                ),
                "translational": (
                    "A modern listener may picture a formal identity document or licence. We mean a "
                    "compliance record produced by an empire-wide administrative demand, whose "
                    "existence is exactly what made failure documentary and public rather than "
                    "private."
                ),
            },
            quick_meaning=(
                "The libelli were papers given to people who obeyed the order to sacrifice. This "
                "paper is what made a person one of the lapsed."
            ),
        ),
        "Re-derived from Doc_06 SS2.3 (lpclex017, corrected upward from a mis-drafted Tier 3 -- "
        "'the source disclosure is the entire justification for how the entry is treated') and "
        "Lexicon-Chunks/lpclex017_libelli.md. formation_confidence set to Inferential-Thin for the "
        "specific claim that this Latin word is this world's own vocabulary item, distinct from the "
        "underlying historical mechanism, which is Documented via lpc.term.certificates-letters-of-peace' own "
        "English-language attestation (see script docstring, CONFIDENCE PER TERM). Relations: four "
        "terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "libellatici-sacrificati",
        dict(
            confidence=conf(
                "C", "verified-direct", "illustrative", "Inferential-Thin",
                "This classification reaches this record as the vendored English edition's own "
                "19th-century editorial endnote, attached to the anonymous treatise against "
                "Novatian, not to an independently re-verified passage of De Lapsis in Cyprian's "
                "own words. It is disclosed as editorial rather than as this world's own two-way "
                "classification, carried for recognizability, not as a claim about Cyprian's own "
                "terminology -- the lowest-attested item in this lexicon.",
            ),
            sources=[
                src(8, "the Introductory Notice's own editorial endnote -- '(1) Libellatici, those "
                       "who had compounded with the heathen, and bought off from offering "
                       "sacrifice; and (2) Sacrificati, those who had actually offered sacrifice to "
                       "idols. Different degrees of discipline were awarded, but all were admitted "
                       "to pardon finally'"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks whether all the lapsed were treated the same; participant "
                    "asks about degrees of failure under persecution"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about the general category or the process of "
                    "return rather than the internal distinction -- ask about the lapsed or "
                    "reconciliation instead"
                ),
            },
            plain_meaning=(
                "Not everyone who failed, failed the same way, and we knew it. One person paid "
                "money and got a paper. Another stood at the altar and did the deed. Both are "
                "outside now, and both ask to come back."
            ),
            world_word="libellatici / sacrificati",
            distortion_risk="low",
            false_friend=[
                "a formal canonical taxonomy fixed by the church itself and applied uniformly "
                "across every case",
            ],
            senses={
                "informational": (
                    "Not everyone who failed failed the same way, and the community knew it. One "
                    "person handed over money and walked away with a paper; another stood at the "
                    "altar and did the thing. Both are outside, and both ask to come back, and it "
                    "would be false to pretend the two acts weigh the same, so the road back is "
                    "longer for one than the other. What does not change is where the road ends. "
                    "This is the graduation inside penitential discipline -- the reason "
                    "reconciliation is a process with stages rather than a single yes or no."
                ),
                "evidential": (
                    "This classification reaches this record as the vendored edition's own "
                    "19th-century editorial endnote, attached to the anonymous treatise against "
                    "Novatian (Confidence C), not to an independently re-verified passage of De "
                    "Lapsis in Cyprian's own words. It is disclosed as editorial, carried for "
                    "recognizability rather than as a claim about Cyprian's own terminology -- the "
                    "World Meaning above is written to the substance of graduated penance, which "
                    "Cyprian's own correspondence does attest, not to the editor's specific labels."
                ),
                "translational": (
                    "A modern listener may assume a formal canonical taxonomy, fixed by the church "
                    "itself and applied uniformly. We mean a real practical distinction in how "
                    "gravely a failure was reckoned, inside a process whose outcome was the same in "
                    "the end: a road back that all of us could walk."
                ),
            },
            quick_meaning=(
                "This is our two-way split of the lapsed. One group bought their way out of the "
                "sacrifice. The other group sacrificed."
            ),
        ),
        "Re-derived from Doc_06 SS2.3 (lpclex018, corrected upward from a mis-drafted Tier 3) and "
        "Lexicon-Chunks/lpclex018_libellatici-sacrificati.md. verification_state set to verified-"
        "direct despite Confidence C: the editor's own wording is directly quoted and checked, even "
        "though citation_specificity stays at the Registry's own C letter -- the same independent-"
        "axis rule wb_lpc_s21.py states for its own Registry-B/verification-state mapping. "
        "Relations: three terms per this term's own Related-Terms line.",
    ))

    ids.append(emit_term(
        "certificates-letters-of-peace",
        dict(
            confidence=conf(
                "A", "verified-direct", "corroborating", "Documented",
                "The regulating voice is Cyprian's throughout, as with every entry in this "
                "cluster; the confessors' own certificates do not survive, and what survives is "
                "Cyprian quoting, paraphrasing, and objecting to them (Author-Gravity-Risk: Yes). "
                "This entry's own first draft misquoted an editorial endnote's wording as Cyprian's "
                "own -- 'thousands of certificates were given, against the Gospel law' -- when "
                "Cyprian's own text reads 'were daily given, contrary to the law of the Gospel'; "
                "the correction is disclosed here rather than silently fixed, per this world's own "
                "editorial-apparatus register (Lexicon_Deployment_Index.md SS7).",
            ),
            sources=[
                src(1, "Cyprian's own crisis correspondence, Epistle XIV -- 'designate by name in "
                       "the certificate those whom you yourselves see, whom you have known, whose "
                       "penitence you see to be very near to full satisfaction'; 'Let such a one be "
                       "received to communion along with his friends'; 'thousands of certificates "
                       "were daily given, contrary to the law of the Gospel'"),
            ],
            retrieval={
                "tier": 2,
                "retrieve_when": split_clauses(
                    "participant asks how the confessors actually granted peace, or by what means; "
                    "participant asks what a certificate was; participant asks how the dispute "
                    "between Cyprian and the confessors worked in practice; conversation reaches "
                    "the mechanics of readmitting the lapsed"
                ),
                "prefer_instead": split_clauses(
                    "the participant is asking about the Decian sacrifice-certificate that made "
                    "someone lapsed in the first place, a different document travelling in the "
                    "opposite direction -- see libelli; both entries answer to the bare word "
                    "'certificate,' and whichever is retrieved should surface the other's existence "
                    "rather than answer as if its own referent were the only one"
                ),
            },
            plain_meaning=(
                "A confessor who stood before the judge writes to the bishop. He names one lapsed "
                "person and asks that they be let back in. This letter is how a confessor made his "
                "claim real."
            ),
            world_word="certificate",
            distortion_risk="high",
            false_friend=[
                "the same document as the Decian sacrifice-certificate, rather than the opposite "
                "one -- a request to be readmitted, not a record of prior compliance",
                "a devotional or ceremonial gesture rather than an administratively real, "
                "regulated instrument issued in the thousands",
            ],
            senses={
                "informational": (
                    "The claim is not made in the abstract; it is made on paper, and the paper "
                    "arrives. A confessor who stood before the magistrate writes to the bishop and "
                    "asks that a named person be received. Cyprian does not say such letters should "
                    "not exist -- he says they must name the person, and be written by someone who "
                    "actually knows them and has judged their penitence. What actually arrives is "
                    "often not that: a name, and an open door behind it, so that whoever can claim "
                    "to be a friend or neighbour of the person named walks through on that same "
                    "paper. The scale is real -- thousands of certificates, by his own account. So "
                    "the argument is not whether the confessors' own suffering counts; it is whether "
                    "a certificate is a judgment about a particular person, made by someone who "
                    "knows them, or a token that can be spent. This is the mechanism behind the "
                    "confessor-authority tension, and without it that tension is a claim with no "
                    "instrument: the lapsed are the subject, reconciliation is the road, the "
                    "confessor is the claimant, and the certificate is the thing that moves between "
                    "them."
                ),
                "evidential": (
                    "Cyprian's own crisis correspondence carries the whole argument, re-verified at "
                    "source, scoped to his own division of the vendored text. 'Certificate' and "
                    "'certificates' occur 42 times within that division, of which 4 sit inside "
                    "editorial notes, leaving 38 in Cyprian's own text -- the figure that attests "
                    "the term, not the naive 42. This entry's own first draft misquoted the editor's "
                    "own endnote wording as Cyprian's own; the correction is disclosed rather than "
                    "smoothed over. The confessors' own certificates do not survive; what survives "
                    "is Cyprian quoting, paraphrasing, and objecting to them, though Epistles XX-XXI "
                    "do preserve two confessors writing in their own first-person voices about a "
                    "specific reconciliation, as close as our record comes to their own side."
                ),
                "translational": (
                    "A modern listener who has just heard about the sacrifice-certificate will "
                    "assume this is the same document, or a version of it, and will tend to hear "
                    "'letter of peace' as a devotional gesture. We mean the opposite document, "
                    "travelling the opposite way: the sacrifice-certificate proves compliance with "
                    "the empire and made a person lapsed; this certificate asks the church to take "
                    "that person back. It is administratively real -- issued in thousands, argued "
                    "over by name, and regulated in writing."
                ),
            },
            quick_meaning=(
                "For us, a certificate is a letter a confessor sends the bishop. It asks that one "
                "named lapsed person be let back into communion."
            ),
        ),
        "Re-derived from Doc_06 SS2.4 (lpclex019, Tier 2, the one term Doc_03 did not surface -- "
        "'without it, this lexicon describes the confessor-authority tension without naming the "
        "instrument the tension was conducted with'; added on the project lead's own direction of "
        "2026-09-15) and Lexicon-Chunks/lpclex019_certificates-letters-of-peace.md. world_word set "
        "to the singular 'certificate' rather than the chunk's own multi-word Term line, matching "
        "the chunk's own Quick Meaning register and avoiding a false-friend collision with "
        "lpc.term.libelli's own distinct headword. Relations: six terms per this term's own "
        "Related-Terms line.",
    ))

    return ids


def main() -> None:
    tier1_ids = build_tier1_terms()
    tier2_ids = build_tier2_terms()
    all_ids = tier1_ids + tier2_ids
    assert len(tier1_ids) == 7, f"expected 7 Tier-1 term records, built {len(tier1_ids)}"
    assert len(tier2_ids) == 12, f"expected 12 Tier-2 term records, built {len(tier2_ids)}"
    assert len(all_ids) == 19, f"expected 19 term records total (Doc_06's own full roster), built {len(all_ids)}"
    assert len(set(all_ids)) == 19, "duplicate term id detected"
    print(f"Wrote {len(WRITTEN)} term records under {RECORDS_ROOT / 'term'}:")
    print(f"  - {len(tier1_ids)} Tier-1 (full depth, from Lexicon-Chunks)")
    print(f"  - {len(tier2_ids)} Tier-2 (compressed depth, structure not fragmented, from "
          f"Lexicon-Chunks)")


if __name__ == "__main__":
    sys.exit(main())
