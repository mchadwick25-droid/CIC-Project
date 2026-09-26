"""B-2 + B-3 (S2.2/S2.3): Donatism (don) term records -- the full 21-term
lexicon roster.

WHY ONE SCRIPT, NOT TWO. B-2 ("mechanical lexicon split") and B-3 ("full
term authoring") collapse into one pass here because the source material's
own shape collapses them: for the 7 confirmed Tier-1 terms,
`Lexicon-Chunks/donlexNNN_*.md` is ALREADY fully-authored, already-reviewed
deployment prose (Doc_06 SS0: "cleared independent adversarial review across
two rounds") -- there is no separable "mechanical stub, then author it up"
step for those 7; converting the chunk's own sections onto the live schema
IS most of the authoring work, and the remainder (confidence blocks,
register-safe quick_meaning/plain_meaning, relations/reciprocity) is
authored judgment applied on top of already-settled content. For the other
14 candidates (Doc_03's full 21-term roster minus the 7 built chunks), there
is no B-2 mechanical source at all -- Doc_06 SS3 explicitly defers their
chunk production as disclosed future work -- so building them is pure B-3
authoring from Doc_03's own candidate-list content, done here rather than
left as a silent 14-term gap in this world's own lexicon (see "THE 14
NON-CHUNKED CANDIDATES" below for why they are built now, and at what
depth).

INPUTS, mapped to OUTPUTS, precisely:
  - Doc_03_Lexicon_Candidate_List.md SS1 (Candidate Roster, 21 candidates in
    6 clusters, tier/tag/AG-risk per candidate) -> tags, preliminary
    one-line meanings for the 14 non-chunked terms; SS4 (CT contest) ->
    Agonistici's own CT framing, carried forward via Doc_06 SS2 instead
    (Doc_06 sharpens it with the Doc_04 SS3.5 regional-scope finding, so
    Doc_06 is this script's authority for the CT text itself, per Doc_06
    SS2's own note that it -- not Doc_03 -- is "the Doc_06 authority for CT
    contest types").
  - Doc_06_Full_Lexicon_Development.md SS1 (Tier Confirmation table, all 21
    terms, confirmed tier) -> retrieval.tier for every term record;
    SS2 (CT Contest-Type Specification) -> Agonistici's own CT content
    (folded into its senses.informational/plain_meaning per this schema's
    own field shape, since `term` has no dedicated CT-Contest-Type field --
    a schema-forced placement decision, named here); SS3 (Deployment Chunk
    Production, the 7-chunk build + the Related-Terms Reciprocity
    computation) -> which terms get full depth vs. minimum depth, and the
    starting relations graph before this script's own reciprocity-closing
    additions (see RECIPROCITY CLOSURE below).
  - Lexicon-Chunks/donlex001_traditor-traditio.md,
    donlex002_rebaptism.md, donlex008_church-ecclesia.md,
    donlex010_martyr-martyrdom.md, donlex015_bishop-episcopus.md,
    donlex018_agonistici.md, donlex019_refusal-of-imperial-legitimacy.md
    (all 7 read in full before this script was written) -> the 7 Tier-1
    term records' quick_meaning / plain_meaning / senses.* / false_friend /
    retrieval.retrieve_when/do_not_retrieve_when / relations / sources,
    per the FIELD MAPPING below.
  - records/don/source/*.md (41 records, built at B-1, read in full -- the
    complete id list from `Build/worlds/don/scripts/wb_don_s21.py`'s
    own `build_sources()`) -> every `sources[].source_id` this script
    writes; no new source records are created or needed.

FIELD MAPPING, chunk section -> schema field (per this world's own launch
instructions):
  - `Quick Meaning` -> NOT copied verbatim into `quick_meaning`. Every one of
    the 7 chunks' own Quick Meaning sentences is written in a builder's-eye
    third-person register ("this world holds...", "this world's rival
    churches...") that gate_voice_perspective's own `_THIS_WORLD` pattern
    would flag on sight, because `quick_meaning` is one of exactly two term
    fields (`term.plain_meaning`, `term.quick_meaning`) that gate scans.
    Rewritten here into first-person "we/our" register, preserving the
    chunk's own content and claims exactly -- no fact added, removed, or
    softened, only the vantage point corrected from external description to
    internal voice, the same correction pahc's own approved term record
    (`pahc.term.ekklesia`) already models. AUTHORED, this script's own
    judgment call, but load-bearing: every rewrite was checked against its
    own source chunk sentence-by-sentence before being finalized.
  - `World Meaning` -> split between `plain_meaning` (the chunk's own
    opening 1-2 sentences, condensed, same register correction as above)
    and `senses.informational` (the chunk's own fuller development,
    likewise register-corrected where it named "this world" from outside,
    though this field is NOT gate_voice_perspective-scoped for `term` --
    corrected anyway, for consistency of voice across the whole record, not
    because the gate requires it). This plain_meaning/informational split
    mirrors pahc.term.ekklesia's own precedent (short plain_meaning, full
    paragraph in senses.informational) rather than dumping the entire
    three-paragraph World Meaning into plain_meaning, which would blow past
    every comparable term record's own length and (per spot-check) risk the
    FK-10 ceiling gate_readability enforces on plain_meaning specifically.
  - `Distortion Risk` (Modern Hearing / World Hearing pairing) -> two
    places: the enum `distortion_risk` field (mechanical: DR tag present in
    Doc_03/Doc_06 -> "high" for the 7 Tier-1 terms, "medium" for Tier-2/3
    DR-tagged terms, "low" for the 5 Tier-2/3 terms Doc_03 never tagged DR
    at all -- a tier-scaled mapping this script adds, since neither Doc_03
    nor Doc_06 states the enum value directly, named here as this script's
    own rule) and `senses.translational` (the Modern Hearing content,
    paraphrased into the "modern question / world answer" bridge form
    pahc.term.ekklesia's own translational sense already models -- this
    field is not gate_voice_perspective-scoped, so no register correction
    was forced here, though the paraphrase still favors "we/our" where it
    reads naturally).
  - `Key Sources` -> `sources[]`, each entry resolved to the ACTUAL
    `don.source.<slug>` record id built at B-1 (never a bare citation
    string) with `locus` carrying the chunk's own specific citation detail.
    Where a chunk's own Key Sources paragraph names a specific verified
    quotation ("independently verified this build against <file>"), that
    exact citation detail is what `locus` carries -- this script does not
    invent a new locus, only re-addresses the chunk's own citation at the
    correct source record.
  - `Retrieve-When` / `Do-Not-Retrieve-When` -> `retrieval.retrieve_when[]`
    / `retrieval.do_not_retrieve_when[]`, split from the chunk's own
    semicolon-joined paragraph into one list entry per clause (mechanical),
    with the same light "this world" -> "we/our" register correction
    applied (AUTHORED, minor) -- these two fields are NOT
    gate_voice_perspective-scoped for `term`, so the correction is this
    script's own consistency choice, not a gate requirement.
  - `Related-Terms` / `Related-Terms Reciprocity Note` -> `relations[]`,
    type `associated-with` (the only symmetric relation type
    RELATION_INVERSE offers) -- see RECIPROCITY CLOSURE below for how this
    script closes every gap the chunks' own Reciprocity Notes name.
  - `Aliases` -> `false_friend[]`, NEVER copied wholesale. Checked against
    `gate_alias_safety` directly (engine/m1/gates.py: a false_friend entry
    fails closed only on an EXACT, case-insensitive string match against
    ANOTHER term's own `world_word` -- not a substring or thematic
    collision): every alias that is a plain synonym or alternate spelling
    with no distortion risk (e.g. Traditor/Traditio's own "traditio" as an
    alias of "traditor") is LEFT OUT of false_friend, since the retrofit
    gate (`gate_glossary_retrofit_complete`) only requires the key be
    present, not that every alias populate it. What IS carried into
    false_friend, for every DR-tagged term, is a short paraphrase of that
    term's own Modern Hearing paragraph -- the actual false-friend content
    Doc_06's own Distortion Risk section already names, reworded as a
    reading rather than copied as a sentence. One collision was caught and
    avoided by hand before writing: Martyr/Martyrdom's own chunk lists
    bare "confessor" as an alias, and this script also builds a Tier-3
    `don.term.confessor` record whose own `world_word` is "confessor" --
    including bare "confessor" in Martyr/Martyrdom's false_friend would
    exactly collide. Confessor is a genuinely distinct, related category
    (Doc_03's own Cluster 3), not a false-friend reading of Martyr, so it
    is correctly left out of false_friend and carried instead as an
    `associated-with` relation.

THE 14 NON-CHUNKED CANDIDATES (Doc_03's 21-term roster minus the 7 built
Tier-1 chunks): Reception without Reordination (003), Purity (004),
"Donatist"/Pars Donati (005), Caecilianist (006), "Catholic"/Catholicus
(007), Schism (009), Confessor (011), Church of the Martyrs (012), Deo
laudes (013), Anniversaria Commemoratio (014), Primate/Primas (016),
Council/Concilium (017), Persecution (020), Liber Regularum (021). Doc_06
SS3 names their chunk production as "deployment-layer, disclosed" deferred
work, not abandoned scope -- but a DEFERRED DEPLOYMENT CHUNK is not the same
decision as a DEFERRED RECORD, and this world's own build discipline (named
throughout don_Decision_Log.md, and required by this step's own launch
instructions) is to name and dispose of every candidate explicitly rather
than let 14 of 21 silently vanish between Doc_03 and records/don/term/.
JUDGMENT CALL: every one of the 14 is built as its own `don.term.<slug>`
record THIS PASS, at Tier-3-minimum depth (quick_meaning + a short
plain_meaning + a minimal senses.translational + sources -- NOT the full
senses.informational/evidential/personal depth the 7 Tier-1 chunks earn),
tagged with Doc_06's own CONFIRMED tier (2 or 3, from the SS1 table), not
Doc_03's preliminary estimate. This is a real content-authoring act beyond
mechanical transcription (Doc_03's own one-line "world-meaning" column is
the seed, register-corrected and lightly expanded to satisfy the schema's
own required fields), named here rather than silently performed. The
alternative -- leaving these 14 as pure metadata in a spreadheet with no
queryable record -- was rejected because it would leave 14 of Doc_04's own
gravity-adjacent vocabulary items unretrievable at runtime and, more
concretely, would leave every one of the 7 Tier-1 chunks' own "not yet
built as chunks" Related-Terms entries pointing at nothing (a
gate_referential failure waiting to happen the moment anyone tried to
declare those relations at all).

RECIPROCITY CLOSURE. Doc_06 SS4 itself names the lexicon's own reciprocity
state as of that document: five mutual pairs among the 7 built chunks, one
flagged one-directional link (Rebaptism -> Church/Ecclesia, not
reciprocated), and every other Related-Terms entry pointing at a "not yet
built as chunks" term, explicitly not counted as either mutual or
one-directional until that chunk exists. Building all 21 terms this pass
changes that count: every target a Tier-1 chunk's own Related-Terms field
already names now resolves to a real record, so this script:
  (a) mechanically transcribes each of the 7 chunks' own Related-Terms
      entries into `relations[]` (`associated-with`, both ends -- e.g.
      donlex001's Related-Terms names Purity and Reception without
      Reordination, so don.term.traditor-traditio gets those two relations,
      and don.term.purity / don.term.reception-without-reordination each
      get the reciprocal edge back);
  (b) closes the one flagged one-directional gap Doc_06 SS4/SS5 itself
      names as remaining work: `don.term.church-ecclesia` gets an
      additional `associated-with -> don.term.rebaptism` relation not
      present in donlex008's own Related-Terms field, specifically to
      satisfy the reciprocal edge donlex002's own chunk already declares
      toward it. This is a deliberate, disclosed content addition -- Doc_06
      names this exact gap by name as the one thing left to close, so
      closing it here (rather than re-shipping the same disclosed gap
      forward) is this script's own judgment call, not a silent edit to
      either chunk's own authored text;
  (c) leaves three terms with NO relations at all -- Caecilianist,
      Anniversaria Commemoratio, Liber Regularum -- because no built
      chunk's own Related-Terms field names any of the three (Caecilianist
      is discussed at length in Church/Ecclesia's own World Meaning prose
      but is not one of that chunk's four listed Related-Terms; the other
      two sit in thin, standalone clusters per Doc_03 SS0/SS6). This
      script does NOT invent relations beyond what the 7 chunks' own
      Related-Terms fields state, even where thematic proximity in Doc_03's
      own cluster grouping might suggest one -- a relation not actually
      declared in the reviewed chunk material is not this script's to add.
The resulting graph is fully reciprocal by construction (every
`associated-with` edge is written at both ends in the same pass), so
gate_reciprocity is satisfied without a follow-up pass.

CONFIDENCE, EXTRACTED PER TERM (Article 17 / this step's own instruction:
never re-judged). For the 7 Tier-1 terms, Doc_06 SS1/SS3 states directly
which are "historically Documented at their core" (Traditor/Traditio,
Rebaptism, Martyr/Martyrdom, Bishop/Episcopus, Refusal of Imperial
Legitimacy -- named as a group -- and Church/Ecclesia, named separately as
"historically Documented on its own terms via Optatus's own quoted text"):
all six get formation_confidence=Documented, paired with verified-direct
(each chunk's own Key Sources note names an "independently verified this
build against <file>" citation) and a null divergence_note, satisfying
gate_confidence_crosscheck by construction (checked here the same way
wb_don_s21.py's own `conf()` helper checks it -- a hard assertion, not left
to hope). Refusal of Imperial Legitimacy additionally carries a non-null
divergence_note despite being Documented/verified-direct, because Doc_06's
own Key Sources note for it draws a distinction this record preserves: the
episodes themselves are Documented, but that they form ONE principled
refusal rather than isolated grievances is "this build's own synthesis,"
Doc_06's own words. Agonistici is the one Tier-1 exception, EXTRACTED
directly from Doc_06 SS3's own words -- "not 'Documented at its core'...
Doc_04 SS4 rates its character component 'DMR at best'" -- so this record
sets formation_confidence="Dominant Modern Reconstruction" (an exact,
not paraphrased, match to Doc_06's own "DMR" abbreviation) and
evidentiary_weight="contested" (matching the CT tag), with a divergence_note
stating the existence/self-designation/character three-way split Doc_03 SS0
and Doc_06 SS1 both carry. For the 14 non-chunked terms, Doc_06 states no
per-term confidence at all (it only confirms their tier in the SS1 table) --
so, per this step's own instruction that a gap be named rather than
invented into a false specificity, every one of the 14 gets the SAME
default block (citation_specificity C / verification_state
named-not-rechecked / formation_confidence "Widely Accepted", the same
default rule wb_don_s21.py's own source-record script used for
Source-Registry rows this thin), with evidentiary_weight scaled to
confirmed tier (Tier-2 -> corroborating, Tier-3 -> illustrative -- the same
tier-to-weight mapping already implicit in Doc_06's own tier reasoning) and
a divergence_note stating plainly that Doc_06 carries no term-specific
confidence statement for this entry, only a tier confirmation -- a named
gap, not a silent default dressed up as a considered judgment.

WHAT THIS SCRIPT DOES NOT DO: build deployment chunk files for the 14
non-chunked terms (Doc_06 SS3's own disclosed deferral stands at the
deployment-chunk layer -- this script produces schema-valid, retrievable
TERM RECORDS at Tier-3-minimum depth for all 14, not the full L4 template
chunk); assign canon_cells (no canon-cell tagging work has happened for
this world yet, same standing limitation B-1's own script names); author a
confirmed-gloss entry (see CONFIRMED-GLOSS FINDING below -- no live
mechanism exists to author into); touch anything outside
Build/worlds/don/scripts/ and records/don/term/; re-author or
re-publish any of the 7 Lexicon-Chunks files themselves (read, never
edited); resolve Agonistici's own live CT contest (Frend vs. Shaw) --
carried forward as an open contest, per Doc_06 SS2's own instruction not to
adjudicate it.

CONFIRMED-GLOSS FINDING (this step's own required check, same disposition
as B-1a's finding on the missing B-1b mechanism): the governing process doc
(Build/Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_3.md, B-3 row)
names `wrs/glosses/confirmed_glosses.yaml` (schema-validated against
`wrs/schema/confirmed_gloss.schema.json`, read by `app/prompts/
confirmed_glosses.py`) as where a confirmed-gloss entry belongs, flagged for
the project lead's own one-at-a-time confirmation. No `wrs/` directory
exists anywhere in this repository (confirmed directly: `find . -iname
wrs` and `ls cic-poc/backend` both come up empty) -- this is the SAME
retired cic-poc/backend/wrs/ backend B-1's own script already found gone.
The live system's actual equivalent is `engine/m4/term_glosses.py`, whose
own docstring records Mark's ruling that superseded the confirmed-allowlist
design entirely: "the world's term records ARE the curated allowlist... the
first-occurrence-per-session grammar keeps the thread calm... the mark is
UI-only." There is no separate confirmation file to author into any more --
`find_glosses_used()` reads `world_word`/`plain_meaning`/`quick_meaning`/
`senses.translational`/`false_friend` straight off the term records this
script writes, mechanically, at runtime, with no hand-curated allowlist
gate in between. So: no confirmed-gloss entries are authored by this
script, for the same reason B-1a authored no B-1b relative-recall
statement -- the mechanism named in the process doc does not exist in the
live system, and the live system's own replacement needs no separate
per-term authoring step at all. Stated here plainly rather than guessed at
or silently skipped.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]
RECORDS_ROOT = REPO_ROOT / "records" / "don"

WORLD_ID = "don"
SCHEMA_VERSION = 2

WRITTEN: list[str] = []


def src(source_id: str, locus: str) -> dict:
    return {"source_id": source_id, "locus": locus, "license": "public-domain"}


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


# ---------------------------------------------------------------------------
# RECIPROCITY GRAPH (see docstring, RECIPROCITY CLOSURE). Undirected edges;
# `associated-with` is written at both ends for every edge below.
EDGES = [
    ("traditor-traditio", "rebaptism"),
    ("traditor-traditio", "bishop-episcopus"),
    ("traditor-traditio", "purity"),
    ("traditor-traditio", "reception-without-reordination"),
    ("rebaptism", "church-ecclesia"),
    ("rebaptism", "reception-without-reordination"),
    ("rebaptism", "purity"),
    ("church-ecclesia", "bishop-episcopus"),
    ("church-ecclesia", "donatist-pars-donati"),
    ("church-ecclesia", "catholic-catholicus"),
    ("church-ecclesia", "schism"),
    ("martyr-martyrdom", "refusal-of-imperial-legitimacy"),
    ("martyr-martyrdom", "church-of-the-martyrs"),
    ("martyr-martyrdom", "deo-laudes"),
    ("martyr-martyrdom", "confessor"),
    ("bishop-episcopus", "primate-primas"),
    ("bishop-episcopus", "council-concilium"),
    ("agonistici", "refusal-of-imperial-legitimacy"),
    ("agonistici", "persecution"),
    ("refusal-of-imperial-legitimacy", "persecution"),
]

ADJACENCY: dict[str, set] = defaultdict(set)
for _a, _b in EDGES:
    ADJACENCY[_a].add(_b)
    ADJACENCY[_b].add(_a)


def relations_for(slug: str) -> list[dict]:
    return [
        {"type": "associated-with", "target": f"don.term.{t}"}
        for t in sorted(ADJACENCY.get(slug, set()))
    ]


def emit_term(slug: str, body_kwargs: dict, provenance_note: str) -> str:
    tid = f"don.term.{slug}"
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
# TIER 1 -- the 7 confirmed Tier-1 terms, built to full depth from the 7
# already-authored, already-reviewed Lexicon-Chunks files (read in full
# before writing any of this). Every quotation/citation detail below is the
# chunk's own Key Sources content, re-addressed at the actual don.source.*
# record built at B-1 -- none is newly asserted by this script.
# =============================================================================

def build_tier1_terms() -> list[str]:
    ids = []

    ids.append(emit_term(
        "traditor-traditio",
        dict(
            confidence=conf("A", "verified-direct", "load-bearing", "Documented", None),
            sources=[
                src("don.source.optatus-appendix-of-documents",
                    "the Acta Purgationis Felicis (314), the founding accusation against Felix of "
                    "Aptungi"),
                src("don.source.petilian-of-constantina-letters-quoted",
                    "'What we look for is the conscience of the giver, to cleanse that of the "
                    "recipient' -- independently verified against "
                    "npnf104_augustine-anti-manichaean-anti-donatist.xml"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": [
                    'participant uses "traditor," "traditio," or asks why we cared so much about '
                    "what a minister did during a past persecution",
                    "participant asks why one bishop's consecration split our whole church",
                    "conversation reaches the origin of the schism or the question of who has the "
                    "right to ordain or baptize",
                ],
                "do_not_retrieve_when": [
                    "participant is asking about persecution or martyrdom generally without "
                    "reference to the surrender-of-scripture question specifically",
                    "the World Capsule Core has already surfaced the traditio origin in the "
                    "current turn",
                ],
            },
            plain_meaning=(
                "When the persecutor came, some clergy handed over our scriptures to be burned. "
                "Others did not. We do not call this a private failure of nerve. A man who gave "
                "up what he was meant to guard showed, in that one moment, what his hand is "
                "worth. A hand that failed then cannot be trusted now to baptize, ordain, or "
                "consecrate."
            ),
            world_word="traditor",
            distortion_risk="high",
            false_friend=[
                "an old personal grudge over past cowardice, with no live sacramental "
                "consequence today",
                "a general political or military betrayal, unconnected to the surrender of "
                "scripture",
            ],
            senses={
                "informational": (
                    "Our whole schism turns on one accusation: that Caecilian, bishop of "
                    "Carthage, was consecrated by a traditor, Felix of Aptungi. If that "
                    "accusation is true, every priest Felix's line ordained, every bishop those "
                    "priests helped consecrate, and every baptism performed under that whole "
                    "line carries the same defect back to its root. We could not simply overlook "
                    "it, the way our rivals ask us to; the line had to be broken and begun "
                    "again, clean. We ask the same purity of our own clergy that we ask of "
                    "theirs -- this is not a grudge held only against outsiders."
                ),
                "evidential": (
                    "Petilian of Constantina's own quoted words -- 'What we look for is the "
                    "conscience of the giver, to cleanse that of the recipient' -- independently "
                    "confirm this is our genuine teaching, not a hostile invention, though his "
                    "words survive only inside Augustine's own refutation. The founding "
                    "accusation itself, against Felix of Aptungi, comes to us through Optatus's "
                    "own Appendix of Documents -- court records, but selected and framed by "
                    "Optatus's own hand, which is itself part of how heavily our whole record "
                    "passes through hostile mediation."
                ),
                "personal": (
                    "When one of our own churches must choose a new bishop, the first question "
                    "is never his teaching. It is his hand: did he waver when the persecutor "
                    "came, or does his own line trace back to one who did?"
                ),
                "translational": (
                    "'Isn't this just an old grudge?' From outside, it can sound like one -- a "
                    "dispute over who behaved badly during a long-past persecution that a "
                    "reasonable person would expect both sides to have moved past by now. From "
                    "inside, it is the opposite: our own insistence that what a minister does "
                    "under real pressure is not separable from what he can give afterward, "
                    "asked of our own clergy as much as anyone's."
                ),
            },
            quick_meaning=(
                "A traditor handed over the scriptures or sacred vessels, rather than suffer for "
                "keeping them. We hold that his hand can no longer give a valid baptism or "
                "ordination."
            ),
        ),
        "Re-derived from Doc_06 SS1 (donlex001, Tier 1, confirmed) and "
        "Lexicon-Chunks/donlex001_traditor-traditio.md (Quick Meaning / World Meaning / "
        "Distortion Risk / Key Sources), both already-authored, already-reviewed deployment "
        "prose -- mapped onto the live term schema per this script's own field-mapping "
        "judgment calls (see script docstring). quick_meaning/plain_meaning rewritten from the "
        "chunk's own third-person framing into first-person we/our register (gate_voice_"
        "perspective scope); Petilian's own quoted proposition is independently verified against "
        "npnf104_augustine-anti-manichaean-anti-donatist.xml, per the chunk's own Key Sources "
        "note, re-addressed here at don.source.petilian-of-constantina-letters-quoted. Relations: "
        "Rebaptism and Bishop/Episcopus are Mutual per the chunk's own Related-Terms Reciprocity "
        "Note; Purity and Reception without Reordination close that same note's own \"not yet "
        "built as chunks\" gap, now that this pass authors those two terms as well.",
    ))

    ids.append(emit_term(
        "rebaptism",
        dict(
            confidence=conf("A", "verified-direct", "load-bearing", "Documented", None),
            sources=[
                src("don.source.augustine-on-baptism-against-donatists",
                    "On Baptism, Against the Donatists, quoting Petilian's own argument for the "
                    "practice"),
                src("don.source.augustine-answer-to-letters-of-petilian",
                    "Answer to the Letters of Petilian, a clause-by-clause reply to Petilian's "
                    "own rebaptism argument"),
                src("don.source.petilian-of-constantina-letters-quoted",
                    "'What we look for is the conscience of the giver, to cleanse that of the "
                    "recipient' -- independently verified against "
                    "npnf104_augustine-anti-manichaean-anti-donatist.xml"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": [
                    'participant uses "rebaptism," "baptized again," or asks why anyone would '
                    "need to be baptized twice",
                    "participant asks what we and our rival church actually fought over",
                    "conversation reaches the question of what makes a baptism real or how "
                    "someone joins our church from the other one",
                ],
                "do_not_retrieve_when": [
                    "participant is asking about baptism as a general Christian rite without "
                    "reference to the boundary-crossing question specifically",
                    "the World Capsule Core has already surfaced rebaptism as the enacted rite "
                    "in the current turn",
                ],
            },
            plain_meaning=(
                "We do not think of this as baptizing someone twice. From where we stand, "
                "nothing happened the first time, because it came from a hand we do not trust "
                "to give it. When someone comes to us from the rival church, we are not "
                "repeating a sacrament -- we are giving the first true one."
            ),
            world_word="rebaptizare",
            distortion_risk="high",
            false_friend=[
                "a repeated sacrament performed out of excessive ritual scruple",
                "an unnecessary formality, since most traditions hold baptism happens only once",
            ],
            senses={
                "informational": (
                    "This is the same logic that makes traditor our founding wound: if a "
                    "minister's hand cannot be trusted, nothing that flows through it can be "
                    "trusted either, and baptism is the sharpest place that trust holds or "
                    "fails, because baptism is what makes a person part of the church at all. "
                    "Rebaptism is not a private opinion held by a few among us; it is the single "
                    "most concretely enacted, individually experienced act of belonging we have. "
                    "Every rebaptism performed is our own doctrine, lived rather than merely "
                    "stated."
                ),
                "evidential": (
                    "Augustine's On Baptism, Against the Donatists and his Answer to the Letters "
                    "of Petilian both devote substantial argument to this practice, quoting "
                    "Petilian's own words clause by clause -- 'What we look for is the "
                    "conscience of the giver, to cleanse that of the recipient,' independently "
                    "verified against the vendored text. Augustine dominates the surviving "
                    "evidence for this practice's own specific argumentative texture, but the "
                    "bare fact of the practice, and Petilian's own argument for it, are attested "
                    "directly in Augustine's own primary text, not merely summarized by him."
                ),
                "personal": (
                    "We know what rebaptizing a Catholic costs us in the empire's eyes: "
                    "successive imperial edicts name this practice specifically, because to the "
                    "state that favors our rival, it is the plainest sign we do not accept its "
                    "settlement. We accept that cost, because to stop would be to concede the "
                    "other church's baptisms were real after all -- and if theirs were real, "
                    "ours were never necessary."
                ),
                "translational": (
                    "'Why would you baptize someone twice?' By most later Christian tradition's "
                    "own reckoning, baptism happens once -- so from outside, this can look like "
                    "an excessive ritual scruple. From inside, it is not a repetition at all: it "
                    "is the correction of an act that, whatever it looked like, conferred "
                    "nothing the first time."
                ),
            },
            quick_meaning=(
                "Baptism given outside our one true church is no baptism at all. So when "
                "someone comes to us from the rival communion, we are not repeating a sacrament "
                "-- we are giving the first one."
            ),
        ),
        "Re-derived from Doc_06 SS1 (donlex002, Tier 1, confirmed) and "
        "Lexicon-Chunks/donlex002_rebaptism.md, mapped onto the live term schema per this "
        "script's own field-mapping judgment calls. Petilian's own quoted proposition is "
        "independently verified against npnf104_augustine-anti-manichaean-anti-donatist.xml, "
        "per the chunk's own Key Sources note. Relations: Traditor/Traditio is Mutual per the "
        "chunk's own Reciprocity Note; Reception without Reordination and Purity close that same "
        "note's \"not yet built as chunks\" gap. Church/Ecclesia was the chunk's own flagged "
        "ONE-DIRECTIONAL link (Doc_06 SS4/SS5 name it explicitly as remaining work) -- closed "
        "this pass by adding the reciprocal edge on don.term.church-ecclesia's own record, a "
        "deliberate, disclosed content addition (see script docstring, RECIPROCITY CLOSURE), not "
        "a silent edit to either chunk's own authored text.",
    ))

    ids.append(emit_term(
        "church-ecclesia",
        dict(
            confidence=conf("A", "verified-direct", "load-bearing", "Documented", None),
            sources=[
                src("don.source.optatus-against-donatists",
                    "Book III, the vendored petition text ('of the party of Donatus'), lines "
                    "1954-1958"),
                src("don.source.passio-donati-sermon",
                    "Mabillon's own annotation on the sermon's catholic wordplay"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": [
                    'participant asks which church is the "real" one, or why both sides claim '
                    "the same name",
                    'participant uses "catholic," "the church," or "Donatist" and asks what the '
                    "word means from our own side",
                    "conversation reaches the question of what makes a church legitimate",
                ],
                "do_not_retrieve_when": [
                    'participant is asking about "church" as a generic term for a Christian '
                    "building or gathering with no bearing on the contested-legitimacy question",
                    "the World Capsule Core has already surfaced the naming contest in the "
                    "current turn",
                ],
            },
            plain_meaning=(
                "We have no neutral word for 'the church.' The word itself is the argument. When "
                "we say ecclesia, we mean the one true body of Christ, free of the traditor-taint "
                "that marked our rival at its start. We call our rival 'Caecilianist' instead, "
                "after the man whose tainted line is why we split from them. This name is itself "
                "a refusal."
            ),
            world_word="ecclesia",
            distortion_risk="high",
            false_friend=[
                "a minority sect that broke away from the real, mainstream church",
                "a historical curiosity, since the larger church eventually prevailed",
            ],
            senses={
                "informational": (
                    "Our rival claims the same word for itself, and claims 'catholic' -- "
                    "universal -- as though that settled the question merely by being said. We "
                    "do not concede it. When our own clergy signed formal petitions naming "
                    "themselves 'of the party of Donatus,' our rival seized on that very form of "
                    "words as proof we had abandoned the church's own name for a man's. We do "
                    "not read our own petitions that way: a true church can be named for the "
                    "man who led it back to purity without ceasing, for that reason, to be the "
                    "church of Christ. One of our own preachers even turned 'catholic' back on "
                    "our rival, calling it not universal but the place where wrongdoing is "
                    "committed with impunity."
                ),
                "evidential": (
                    "The petition text itself -- 'Given by Capito and by Nasutius, Dignus, and "
                    "the other Bishops of the party of Donatus' -- is preserved in Optatus's "
                    "Book III and independently verified against the vendored text; Optatus "
                    "turns it into his own accusation, so his selection and framing of this "
                    "material is the dominant hand behind how it reaches us. Mabillon's own "
                    "annotation on the Passio Donati sermon independently records our own "
                    "preacher's wordplay on 'catholic.'"
                ),
                "personal": (
                    "We suffered, and continue to suffer, at the hands of a rival that holds "
                    "the emperor's favor, the law's recognition, and the word 'catholic' for its "
                    "own use -- and none of that settles who the true church actually is. If "
                    "recognition by that kind of power were the same as being the church, our "
                    "whole reason for existing apart would dissolve."
                ),
                "translational": (
                    "'Was your church Catholic?' Both of our churches claimed the word. Our own "
                    "preacher's sermon plays on it as a bitter pun instead -- not universal, but "
                    "wherever wrongdoing goes unpunished. No single church of any later name has "
                    "yet emerged to settle the question either way."
                ),
            },
            quick_meaning=(
                "Ecclesia is not one uncontested institution for us -- it is the very thing two "
                "rival hierarchies both claim to be, town for town. We hold that our own "
                "communion, not our state-favored rival, is the true one."
            ),
        ),
        "Re-derived from Doc_06 SS1 (donlex008, Tier 1, confirmed) and "
        "Lexicon-Chunks/donlex008_church-ecclesia.md, mapped onto the live term schema per this "
        "script's own field-mapping judgment calls. The petition text is independently verified "
        "against optatus_against-the-donatists.txt, lines 1954-1958, per the chunk's own Key "
        "Sources note. Relations: Bishop/Episcopus is Mutual per the chunk's own Reciprocity "
        "Note; \"Donatist\"/Pars Donati, \"Catholic\"/Catholicus, and Schism close that same "
        "note's own \"not yet built as chunks\" gap. Rebaptism is ADDED beyond the chunk's own "
        "four listed Related-Terms, specifically to close the one-directional gap Doc_06 "
        "SS4/SS5 names (Rebaptism -> Church/Ecclesia, not yet reciprocated as of Doc_06) -- see "
        "script docstring, RECIPROCITY CLOSURE. Caecilianist is discussed at length in this "
        "record's own senses.informational but is NOT one of donlex008's own four listed "
        "Related-Terms, so no relation to don.term.caecilianist is declared here -- a relation "
        "not actually present in the reviewed chunk material is not this script's to add.",
    ))

    ids.append(emit_term(
        "martyr-martyrdom",
        dict(
            confidence=conf("A", "verified-direct", "load-bearing", "Documented", None),
            sources=[
                src("don.source.passio-donati-sermon",
                    "the commemorative sermon on the bishops of Advocata and Sicilibba"),
                src("don.source.passio-marculi", "the Passio Marculi, Macarian repression, 347-348"),
                src("don.source.passio-isaac-et-maximiani",
                    "Macrobius of Rome's own letter to the Carthage congregation on the deaths "
                    "of Isaac and Maximianus"),
                src("don.source.deo-laudes-acclamation-cil8",
                    "CIL VIII 17732 (Bagai), 20482, 17368, 18669"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": [
                    "participant asks about persecution, suffering for the faith, or who we "
                    "consider our martyrs",
                    'participant uses "Deo laudes," "the Church of the Martyrs," or asks why we '
                    "remember our dead the way we do",
                    "conversation reaches the Macarian repression or the annual commemoration of "
                    "a martyr's death",
                ],
                "do_not_retrieve_when": [
                    "participant is asking about martyrdom as a general Christian category "
                    "unconnected to our own specific rival-church context",
                    "the World Capsule Core has already surfaced the martyr-cult identity in "
                    "the current turn",
                ],
            },
            plain_meaning=(
                "We do not remember our dead the way our rival remembers its own. When the "
                "imperial commissioners Paul and Macarius came to force unity on us, some of "
                "our own bishops and their people chose death rather than the peace that would "
                "concede the case against us. We call this what it is: martyrdom. Our rival "
                "refuses us the word, because in their own account we are the ones in the "
                "wrong, and a wrongdoer who dies resisting correction is not a martyr to them."
            ),
            world_word="martyr",
            distortion_risk="high",
            false_friend=[
                "a generic Christian martyr-cult, comparable to any community's veneration of "
                "those killed by pagan Rome",
                "an admirable but historically unremarkable feature of early Christianity "
                "generally",
            ],
            senses={
                "informational": (
                    "This is why we are, before anything else, the Church of the Martyrs -- not "
                    "a title adopted for effect, but the plainest description of what happened "
                    "to us and what we have gone on doing since. Every year, on the appointed "
                    "day, we gather at the grave and hear the account read aloud again, not as "
                    "history but as the same formation happening again in the hearing. When we "
                    "cry 'Deo laudes' -- praise to God -- in place of our rival's words, it is "
                    "this same conviction spoken aloud."
                ),
                "evidential": (
                    "This is our own least hostile-mediated vocabulary: the commemorative sermon "
                    "on the bishops of Advocata and Sicilibba, the Passio Marculi, and Macrobius "
                    "of Rome's own letter to the Carthage congregation are all Donatist-voiced "
                    "or -authored texts, and the Deo laudes acclamation is independently "
                    "attested on stone at Bagai and elsewhere (CIL VIII 17732, 20482, 17368, "
                    "18669) with no hostile literary mediation at any point -- unlike our purity "
                    "and rebaptism doctrine, whose specific argumentative texture reaches this "
                    "record substantially through hostile refutation."
                ),
                "personal": (
                    "We hold two persecutions in memory and do not let them blur into one: the "
                    "empire-wide terror we suffered alongside our rival came first; the later "
                    "persecution, the one that made our martyrs, came at our own rival's own "
                    "instigation, through the very emperor whose favor they enjoy and we were "
                    "refused."
                ),
                "translational": (
                    "'Wasn't that just ordinary Roman persecution, like anyone else's?' Our "
                    "most documented martyrs did not die at pagan hands at all -- they died at "
                    "imperial hands acting on our rival's own instigation, a death that same "
                    "rival still refuses to call martyrdom. Commemorating them is our most "
                    "direct, least hostile-mediated proof of who has actually suffered."
                ),
            },
            quick_meaning=(
                "For us, martyrdom is death borne for the true faith. Our own most documented "
                "martyrs died at the hands of a rival Christian party's imperial enforcers -- a "
                "death our rival has never once called martyrdom."
            ),
        ),
        "Re-derived from Doc_06 SS1 (donlex010, Tier 1, confirmed) and "
        "Lexicon-Chunks/donlex010_martyr-martyrdom.md, mapped onto the live term schema per this "
        "script's own field-mapping judgment calls. Relations: Refusal of Imperial Legitimacy is "
        "Mutual per the chunk's own Reciprocity Note; Church of the Martyrs, Deo laudes, and "
        "Confessor close that same note's own \"not yet built as chunks\" gap. Confessor is "
        "deliberately NOT carried into false_friend (the chunk's own Aliases list includes bare "
        "\"confessor\", which would exactly collide with don.term.confessor's own world_word "
        "under gate_alias_safety) -- carried instead as the associated-with relation above, "
        "consistent with it being a genuinely distinct category per Doc_03 Cluster 3, not a "
        "false-friend reading of this term.",
    ))

    ids.append(emit_term(
        "bishop-episcopus",
        dict(
            confidence=conf("A", "verified-direct", "load-bearing", "Documented", None),
            sources=[
                src("don.source.augustine-on-baptism-against-donatists",
                    "the Cebarsussi (393) and Bagai (394) council sentences quoted"),
                src("don.source.augustine-answer-to-letters-of-petilian",
                    "the Felicianus reception-without-reordination passage"),
                src("don.source.gesta-collationis-carthaginiensis",
                    "the 411 Conference of Carthage, the bishop count context (279 Donatist "
                    "against 286 Catholic)"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": [
                    "participant asks how our own churches were organized, or why there seem to "
                    "be two bishops for the same city",
                    "participant asks about a specific council, the Maximianist affair, or the "
                    "411 Conference",
                    "conversation reaches questions of who holds legitimate church office",
                ],
                "do_not_retrieve_when": [
                    "participant is asking about the office of bishop in a generic, "
                    "cross-tradition sense with no bearing on our own rival-hierarchy situation",
                    "the World Capsule Core has already surfaced the parallel hierarchy in the "
                    "current turn",
                ],
            },
            plain_meaning=(
                "This is not a metaphor. It is a daily fact. Two men claim the same office over "
                "the same people. Each is recognized by his own side, and refused by the other. "
                "At the great Conference in Carthage, 279 of our own bishops sat opposite 286 of "
                "theirs. One whole church answered another, bishop for bishop."
            ),
            world_word="episcopus",
            distortion_risk="high",
            false_friend=[
                "a loose or informal protest movement without real institutional structure",
                "the assumption that only one bishop can hold a given see at a time",
            ],
            senses={
                "informational": (
                    "Our own bishops govern through councils, exactly as any legitimate church "
                    "does -- and it is because our own conciliar machinery is real that our "
                    "sharpest internal crisis was even possible. When the deacon Maximian broke "
                    "from Primian, our own primate at Carthage, a council of his own supporters "
                    "at Cebarsussi elected him a rival primate; our own larger council at Bagai "
                    "condemned that election and, in time, received the Maximianist clergy back "
                    "into communion. That we could discipline our own dissidents through our own "
                    "councils is itself part of our claim to be a genuine church. That those "
                    "same councils received the Maximianist clergy back without repeating either "
                    "ordination or baptism is a fact we do not hide, even where it sits uneasily "
                    "beside how strictly we hold the same standard against our outside rival."
                ),
                "evidential": (
                    "The bare institutional fact of our parallel hierarchy is undisputed even by "
                    "hostile sources reporting it. The Cebarsussi (393) and Bagai (394) council "
                    "sentences are quoted directly in Augustine's own works -- 'Felicianus... "
                    "was not held by the Donatists themselves to have lost either the sacrament "
                    "of baptism or the sacrament of conferring baptism.' Individual bishops' own "
                    "conduct and motives beyond that bare fact reach us substantially through "
                    "Optatus's and Augustine's own hostile characterization."
                ),
                "personal": (
                    "Every one of our own bishops holds his see under continuing legal jeopardy. "
                    "The same imperial power that recognizes our rival's bishops as the lawful "
                    "church has, at different times, confiscated our own buildings, exiled our "
                    "own clergy, and enforced unity against us by force. To be one of our "
                    "bishops is to hold a real, functioning office the state itself refuses to "
                    "recognize as one."
                ),
                "translational": (
                    "'Surely there was only one real bishop per city?' Two hundred seventy-nine "
                    "of our own bishops answered two hundred eighty-six of our rival's at one "
                    "conference alone -- not a metaphor for how contested we were, but the "
                    "literal shape of it: a complete, self-governing rival church order, office "
                    "for office, see for see."
                ),
            },
            quick_meaning=(
                "Wherever our rival has a bishop, so do we. Ours is a whole, parallel church, "
                "see for see, across North Africa."
            ),
        ),
        "Re-derived from Doc_06 SS1 (donlex015, Tier 1, confirmed) and "
        "Lexicon-Chunks/donlex015_bishop-episcopus.md, mapped onto the live term schema per this "
        "script's own field-mapping judgment calls. The 279/286 bishop count follows the world "
        "core's own corrected figure (don.core.donatism cautions item 5), not the earlier, "
        "unverified 284 the chunk itself was drafted before that correction landed. Relations: "
        "Traditor/Traditio and Church/Ecclesia are Mutual per the chunk's own Reciprocity Note; "
        "Primate/Primas and Council/Concilium close that same note's own \"not yet built as "
        "chunks\" gap.",
    ))

    ids.append(emit_term(
        "agonistici",
        dict(
            confidence=conf(
                "B", "verified-direct", "contested", "Dominant Modern Reconstruction",
                "Existence is Documented (Codex Theodosianus 16.5.52, directly verified this "
                "build). The self-designation term itself reaches this record only through "
                "Augustine's own report -- the law's own text never uses the word agonistici. "
                "Character, scale, and typical conduct are the live CT contest (Frend vs. Shaw); "
                "Doc_04 SS4 rates this component 'DMR at best... the sharpest divergence in this "
                "document, across three tiers' (Doc_06 SS3, quoted directly, not re-judged).",
            ),
            sources=[
                src("don.source.codex-theodosianus-book-16",
                    "law XVI.5.52 (412), 'circumcelliones argenti pondo decem,' confirmed "
                    "verbatim"),
                src("don.source.augustine-answer-to-letters-of-petilian",
                    "Augustine's own report of the group's self-designation, agonistici, within "
                    "his wider anti-Donatist corpus"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": [
                    'participant uses "Circumcellion" or "agonistici," or asks about our own '
                    "rural, itinerant members and their reputation for violence",
                    "participant asks whether the hostile portrait of this group is accurate",
                    "conversation reaches Numidia specifically or the group's own relationship "
                    "to the wider hierarchy",
                ],
                "do_not_retrieve_when": [
                    "participant is asking about ordinary Numidian believers generally without "
                    "reference to this specific, contested group",
                    "the World Capsule Core has already surfaced the D-A regional "
                    "scope-qualification in the current turn",
                ],
            },
            plain_meaning=(
                "In the Numidian countryside, some of us call ourselves agonistici -- strivers, "
                "those who fight for the truth. Our opponents call us Circumcellions instead -- "
                "those who linger at the martyrs' shrines -- and say that lingering turns to "
                "violence. We do not pretend this reputation came from nowhere; the empire has "
                "named us in its own law. But we do not accept our opponents' account of us, or "
                "how typical that violence was, as the last word."
            ),
            world_word="agonistici",
            distortion_risk="high",
            false_friend=[
                '"Circumcellion," taken as our own accepted self-description rather than an '
                "outsider's label",
                "a violent fringe faction whose reputation can be taken at face value from "
                "hostile sources alone",
            ],
            senses={
                "informational": (
                    "What is certain is this: we exist, as a recognized body, concentrated in "
                    "Numidia's countryside specifically -- not invented by hostile pens out of "
                    "nothing. What is far less certain is how much of the character our "
                    "opponents give us is true to the whole of us, and how much is the picture a "
                    "hostile hand naturally paints of country people it already despises. In "
                    "Numidia specifically, our strength runs deep -- for many there, belonging "
                    "to us was simply belonging to the ordinary church of one's own village. "
                    "What is contested is narrower: whether the vivid, often violent character "
                    "our opponents attribute to us describes that whole regional strength, or "
                    "only ever described a smaller, more provocative element the hostile record "
                    "chose to make stand for the rest."
                ),
                "evidential": (
                    "Our bare existence is Documented independently of any hostile literary "
                    "characterization: the Codex Theodosianus, law 16.5.52 (412), names us by "
                    "imperial legislation, directly confirmed to read 'circumcelliones argenti "
                    "pondo decem.' Augustine's own report is our only access to the "
                    "self-designation term agonistici itself -- the law's own text never uses "
                    "that word. Our reported character, scale, and typical conduct beyond bare "
                    "existence carry HIGH Author-Gravity risk, reaching this record "
                    "substantially through Optatus's and Augustine's own hostile framing."
                ),
                "personal": (
                    "We are not the whole of Numidia, and not the whole of this church. What we "
                    "were actually like, on any given day, in any given place, is a harder "
                    "question than either our opponents or, honestly, we ourselves can now "
                    "fully settle from what survives."
                ),
                "translational": (
                    "'So Circumcellion is just what you called yourselves?' No -- agonistici is "
                    "our own name; Circumcellion is our opponents'. The violent, itinerant "
                    "character attached to that outsider name reaches the record almost "
                    "entirely through the people who had every reason to make us look as "
                    "dangerous as possible. Our bare existence, in Numidia specifically, is "
                    "beyond real doubt; what we were actually like beyond that is a live, "
                    "unresolved question."
                ),
            },
            quick_meaning=(
                "We call ourselves agonistici -- 'contestants,' those who strive for the truth. "
                "Our opponents call us Circumcellions instead, and paint us as itinerant "
                "fanatics."
            ),
        ),
        "Re-derived from Doc_06 SS1-SS3 (donlex018, Tier 1 CT, confirmed) and "
        "Lexicon-Chunks/donlex018_agonistici.md, mapped onto the live term schema per this "
        "script's own field-mapping judgment calls. `term` has no dedicated CT-Contest-Type "
        "field, so the contest itself (Frend vs. Shaw, per Doc_06 SS2's own text, which is the "
        "authority for this contest, not Doc_03's own earlier framing) is folded into "
        "senses.informational/plain_meaning rather than dropped -- a schema-forced placement "
        "decision, named here. confidence.formation_confidence = 'Dominant Modern "
        "Reconstruction' is Doc_06 SS3's own words ('DMR at best'), extracted, not re-judged. "
        "Relations: Refusal of Imperial Legitimacy is Mutual per the chunk's own Reciprocity "
        "Note; Persecution closes that same note's own \"not yet built as chunks\" gap.",
    ))

    ids.append(emit_term(
        "refusal-of-imperial-legitimacy",
        dict(
            confidence=conf(
                "A", "verified-direct", "load-bearing", "Documented",
                "The three qualifying episodes and Donatus's own quoted retort are "
                "independently Documented and directly verified. That they together constitute "
                "ONE principled refusal, rather than isolated grievances, is this record's own "
                "synthesis of Doc_01's own account (Doc_06's own Key Sources note names this "
                "distinction directly), not a claim resting on one stated authority.",
            ),
            sources=[
                src("don.source.optatus-against-donatists",
                    "Book III, line 1904 -- Donatus's own retort, 'Quid est imperatori cum "
                    "ecclesia?', in the context of the Macarian mission"),
                src("don.source.optatus-appendix-of-documents",
                    "Anulinus's own 313 relatio to Constantine"),
            ],
            retrieval={
                "tier": 1,
                "retrieve_when": [
                    "participant asks about our relationship to the Roman state, or why we "
                    "refused imperial rulings against us",
                    "participant uses Donatus's own quoted retort or asks whether we were "
                    "consistently opposed to imperial power",
                    "conversation reaches the 313/314 councils, the Macarian repression, or the "
                    "411 Conference",
                ],
                "do_not_retrieve_when": [
                    "participant is asking about Roman imperial religious policy generally with "
                    "no bearing on our own specific stance toward it",
                    "the World Capsule Core has already surfaced this refusal as G5 in the "
                    "current turn",
                ],
            },
            plain_meaning=(
                "Constantine's own council at Rome ruled against us. So did the Council of "
                "Arles after it. We did not accept either verdict as settling anything. A "
                "council enforced by a state that already favors our rival is not the church "
                "judging itself. The emperor's own recognition, or his refusal of it, is simply "
                "not the same question as who the true church is."
            ),
            world_word="Quid est imperatori cum ecclesia?",
            distortion_risk="high",
            false_friend=[
                "a simple, unbroken separatism with no exceptions at all",
                "straightforward hypocrisy, once the three pragmatic exceptions are noticed",
            ],
            senses={
                "informational": (
                    "We do not pretend this has been an easy or unbroken stance. Three times "
                    "across our own history, we ourselves turned to the very imperial machinery "
                    "we otherwise refuse to recognize: we petitioned Constantine directly, "
                    "through the governor Anulinus, in the earliest days of the dispute; we "
                    "petitioned Julian for the return of our confiscated basilicas; and when the "
                    "Maximianist schism divided our own house, we ourselves invoked the "
                    "empire's own anti-heresy laws to bring our own dissidents back into line. "
                    "We do not hide these three moments. We hold them alongside our refusal, "
                    "because a stance held on balance, under real and repeated pressure, is not "
                    "the same as an absolute principle that breaks the moment it bends once."
                ),
                "evidential": (
                    "Donatus's own reported retort -- 'Quid est imperatori cum ecclesia?', "
                    "'What has the emperor to do with the church?' -- is independently verified "
                    "against the vendored text of Optatus, Book III, in the context of the "
                    "Macarian mission. The three qualifying episodes themselves are Documented "
                    "and cross-corroborated even by hostile sources reporting their own side's "
                    "actions; that they together constitute one principled refusal, rather than "
                    "an unconnected series of grievances, is this record's own synthesis of "
                    "Doc_01's own account, corroborated by Donatus's own quoted retort."
                ),
                "personal": (
                    "Everything in our own experience of history is shaped by this refusal: the "
                    "rulings we rejected at the start, the repression that made our martyrs, the "
                    "legal suppression that pressed harder as the years wore on, and, in time, "
                    "the loss of the very imperial power we had refused to recognize, when a "
                    "different conqueror took Carthage. We do not read that loss as our own "
                    "defeat -- the specific power our stance was defined against was the one "
                    "thing removed."
                ),
                "translational": (
                    "'Were you consistently against the empire, or not?' Neither a simple, "
                    "unbroken separatism nor straightforward hypocrisy fits us. We held a real, "
                    "dominant refusal of the state's standing to judge the church, together with "
                    "three specific, dated moments where our own actors used that same state's "
                    "machinery because doing so served our case -- without either fact canceling "
                    "the other."
                ),
            },
            quick_meaning=(
                "The state has no standing to decide who the true church is. As our own primate "
                "is reported to have said: 'What has the emperor to do with the church?'"
            ),
        ),
        "Re-derived from Doc_06 SS1 (donlex019, Tier 1, PROMOTED from Doc_03's preliminary Tier "
        "2 -- Doc_04 SS7 confirmed G5 as a fourth Primary gravity) and "
        "Lexicon-Chunks/donlex019_refusal-of-imperial-legitimacy.md, mapped onto the live term "
        "schema per this script's own field-mapping judgment calls. Donatus's own retort is "
        "independently verified against optatus_against-the-donatists.txt, Book III, line 1904, "
        "per the chunk's own Key Sources note. Relations: Martyr/Martyrdom and Agonistici are "
        "Mutual per the chunk's own Reciprocity Note; Persecution closes that same note's own "
        "\"not yet built as chunks\" gap.",
    ))

    return ids


# =============================================================================
# TIER 2 / TIER 3 -- the 14 candidates Doc_03 SS1 names but Doc_06 SS3
# explicitly defers at the deployment-chunk layer. Built here at
# Tier-3-minimum depth (quick_meaning + a short plain_meaning + a minimal
# senses.translational + sources), per this script's own judgment call (see
# docstring, THE 14 NON-CHUNKED CANDIDATES) -- NOT the full
# informational/evidential/personal depth the 7 Tier-1 terms earn.
# confidence is the SAME default block for all 14 (Doc_06 states no
# per-term confidence for any of them, only a tier confirmation), scaled
# only by evidentiary_weight (Tier-2 -> corroborating, Tier-3 ->
# illustrative). distortion_risk is "medium" where Doc_03 tags DR, "low"
# where it does not -- a tier/tag-scaled mapping this script adds (see
# docstring), since neither Doc_03 nor Doc_06 states the enum directly.
# =============================================================================

_MINIMAL_DEFAULT_DIVERGENCE = (
    "Doc_06 SS1 confirms this term's tier but states no term-specific confidence beyond that "
    "confirmation -- this record is authored at Tier-3-minimum depth (quick_meaning + sources) "
    "directly from Doc_03's own one-line candidate-list meaning, per this script's own judgment "
    "call to give every Doc_03 candidate an explicit disposition (see script docstring). A named "
    "gap, not a silently invented confidence rating."
)


def build_minimal_terms() -> list[str]:
    ids = []

    ids.append(emit_term(
        "reception-without-reordination",
        dict(
            confidence=conf("C", "named-not-rechecked", "corroborating", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.augustine-letter-51-to-crispinus",
                         "'you restored some of them without re-ordination' (Letter LI to "
                         "Crispinus)")],
            retrieval={"tier": 2, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "The Maximianist clergy had broken from us. When they returned, our councils "
                "restored them to office. We did not repeat their ordination. We did not repeat "
                "their baptism. Augustine turns this fact against our own rebaptism doctrine. "
                "If their orders were never lost, he asks, why insist a rival's are?"
            ),
            world_word="reception without reordination",
            distortion_risk="low",
            false_friend=[],
            senses={
                "translational": (
                    "'So you never actually required rebaptism?' The Maximianist clergy are the "
                    "one exception on our own record -- received back without a second baptism "
                    "or ordination, a fact we do not hide even though it sits uneasily beside "
                    "how strictly we hold the same standard against our outside rival."
                ),
            },
            quick_meaning=(
                "We took the Maximianist clergy back into full office. We did not re-ordain "
                "them. We did not re-baptize them."
            ),
        ),
        "Re-derived from Doc_03 Cluster 1 (candidate roster) and Doc_06 SS1 (donlex003, Tier 2 "
        "confirmed, no promotion forwarded) -- no Lexicon-Chunks deployment file exists for this "
        "term; Doc_06 SS3 names its chunk production as disclosed deferred work. Authored "
        "directly from Doc_03's own one-line meaning at Tier-3-minimum depth, per this script's "
        "own judgment call (see docstring). Sourced to Letter LI to Crispinus, the same passage "
        "donlex001/002's own chunks cite for this practice. Relations: associated-with "
        "Traditor/Traditio and Rebaptism close the back-edges those two Tier-1 chunks' own "
        "Related-Terms fields already declare toward this term.",
    ))

    ids.append(emit_term(
        "purity",
        dict(
            confidence=conf("C", "named-not-rechecked", "corroborating", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.cyprian-on-the-lapsed",
                         "the lapsed-clergy purity theology this schism reopens"),
                      src("don.source.augustine-on-baptism-against-donatists",
                          "Augustine's own engagement with the purity doctrine's sacramental "
                          "logic")],
            retrieval={"tier": 2, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "A sacrament's validity depends on the minister's own holiness, and on his "
                "freedom from traditio. We hold this firmly. We sharpened it from Cyprian's own "
                "third-century teaching. We did not invent it new when our schism began."
            ),
            world_word="purity",
            distortion_risk="high",
            false_friend=[
                "extremism or excessive scrupulosity, detached from any live sacramental "
                "question",
                "a personal-morality issue with no bearing on whether a sacrament is valid",
            ],
            senses={
                "translational": (
                    "'Isn't that just extremism?' Our purity doctrine reaches back a full "
                    "lifetime before our own schism began -- to Cyprian of Carthage's own "
                    "third-century teaching that a fallen minister's sacraments carry no grace. "
                    "We did not invent this standard; we refused to abandon it."
                ),
            },
            quick_meaning=(
                "A sacrament is only as valid as the hand that gives it. We sharpened this "
                "teaching from Cyprian. We did not invent it new."
            ),
        ),
        "Re-derived from Doc_03 Cluster 1 (candidate roster) and Doc_06 SS1 (donlex004, Tier 2 "
        "confirmed) -- no Lexicon-Chunks deployment file exists for this term; Doc_06 SS3 names "
        "its chunk production as disclosed deferred work. Authored directly from Doc_03's own "
        "one-line meaning at Tier-3-minimum depth. distortion_risk set to \"high\" despite "
        "Tier-2/minimal depth as a deliberate exception to this script's own tier-scaled "
        "mapping rule, since Purity is the direct doctrinal ground Traditor/Traditio (a Tier-1 "
        "\"high\" term) restates -- named here rather than applying the default rule silently "
        "where it would understate the term's own risk. Relations: associated-with "
        "Traditor/Traditio and Rebaptism close the back-edges those two Tier-1 chunks' own "
        "Related-Terms fields already declare toward this term.",
    ))

    ids.append(emit_term(
        "donatist-pars-donati",
        dict(
            confidence=conf("C", "named-not-rechecked", "corroborating", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.optatus-against-donatists",
                         "Book III, the vendored petition text 'of the party of Donatus' "
                         "(lines 1954-1958)")],
            retrieval={"tier": 2, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "We are remembered by our rival's own name for us. Our own clergy signed formal "
                "petitions naming themselves 'of the party of Donatus' -- a form of words "
                "Optatus turned into an accusation that we had named a man instead of the "
                "Church of Christ. We do not read our own petitions that way."
            ),
            world_word="pars Donati",
            distortion_risk="medium",
            false_friend=[
                "an insult or slur we adopted unwillingly",
                "a denominational brand name with no bearing on legitimacy",
            ],
            senses={
                "translational": (
                    "'Did you call yourselves Donatists?' Our own clergy signed 'of the party of "
                    "Donatus' on a formal petition -- the only vendored trace of our own naming "
                    "practice -- but a name for the man who led us back to purity is not, on our "
                    "own reading, a name instead of the church of Christ."
                ),
            },
            quick_meaning=(
                "'Donatist' is our rival's name for us. It comes from a petition where our own "
                "clergy signed themselves 'of the party of Donatus.' Our rival turned that into "
                "an accusation. We do not accept it."
            ),
        ),
        "Re-derived from Doc_03 Cluster 2 (candidate roster, PV-flagged) and Doc_06 SS1 "
        "(donlex005, Tier 2 confirmed) -- no Lexicon-Chunks deployment file exists for this "
        "term; Doc_06 SS3 names its chunk production as disclosed deferred work. Authored "
        "directly from Doc_03's own one-line meaning at Tier-3-minimum depth, sharing the same "
        "petition-text citation (lines 1954-1958) donlex008's own chunk cites. Relations: "
        "associated-with Church/Ecclesia closes the back-edge that Tier-1 chunk's own "
        "Related-Terms field already declares toward this term.",
    ))

    ids.append(emit_term(
        "caecilianist",
        dict(
            confidence=conf("C", "named-not-rechecked", "illustrative", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.optatus-against-donatists",
                         "Book III's own naming contest, underlying the Caecilianist "
                         "counter-name")],
            retrieval={"tier": 3, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "We call our rival 'Caecilianist,' after Caecilian, whose own tainted "
                "consecration is the reason we exist apart from them -- a naming choice that "
                "refuses their claim to be simply 'the Church' or 'Catholic.'"
            ),
            world_word="Caecilianist",
            distortion_risk="medium",
            false_friend=["a neutral historical label with no polemical charge"],
            senses={
                "translational": (
                    "'Why not just call them Catholic?' Caecilianist is our own refusal to "
                    "grant our rival the unqualified name 'the Church' -- a naming choice, not "
                    "a neutral label."
                ),
            },
            quick_meaning=(
                "We call our rival 'Caecilianist,' after the bishop whose tainted line is why "
                "we split from them."
            ),
        ),
        "Re-derived from Doc_03 Cluster 2 (candidate roster) and Doc_06 SS1 (donlex006, Tier 3, "
        "no change) -- no Lexicon-Chunks deployment file exists for this term; Doc_06 SS3 names "
        "its chunk production as disclosed deferred work. Authored directly from Doc_03's own "
        "one-line meaning at Tier-3-minimum depth. No relation to don.term.church-ecclesia is "
        "declared: Caecilianist is discussed at length in that Tier-1 chunk's own World Meaning "
        "prose, but is NOT one of that chunk's own four listed Related-Terms, and this script "
        "does not invent a relation beyond what the reviewed chunk material actually declares "
        "(see script docstring, RECIPROCITY CLOSURE item (c)).",
    ))

    ids.append(emit_term(
        "catholic-catholicus",
        dict(
            confidence=conf("C", "named-not-rechecked", "corroborating", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.passio-donati-sermon",
                         "Mabillon's own annotation on the sermon's catholic wordplay")],
            retrieval={"tier": 2, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "We claim the word 'catholic' for ourselves, as our rival claims it too. One of "
                "our preachers turned the word back on them instead. Not universal, he said, "
                "but the place where wrongdoing goes unpunished."
            ),
            world_word="catholicus",
            distortion_risk="medium",
            false_friend=["assuming only one side historically owned the word catholic"],
            senses={
                "translational": (
                    "'Which side got to keep the word catholic?' Both of us claimed it. Our own "
                    "preacher's sermon plays on the word as a bitter pun -- not universal, but "
                    "where wrongdoing goes unpunished -- Mabillon's own annotation on the Passio "
                    "Donati records it."
                ),
            },
            quick_meaning=(
                "We call ourselves catholic too. One of our own preachers turned the word back "
                "on our rival instead -- a pun on wrongdoing done with impunity."
            ),
        ),
        "Re-derived from Doc_03 Cluster 2 (candidate roster) and Doc_06 SS1 (donlex007, Tier 2 "
        "confirmed) -- no Lexicon-Chunks deployment file exists for this term; Doc_06 SS3 names "
        "its chunk production as disclosed deferred work. Authored directly from Doc_03's own "
        "one-line meaning at Tier-3-minimum depth, sharing the same Passio Donati/Mabillon "
        "citation donlex010's own chunk also draws on. No relation is declared: not one of "
        "donlex008's own four listed Related-Terms names this term reciprocally beyond what is "
        "already carried above.",
    ))

    ids.append(emit_term(
        "schism",
        dict(
            confidence=conf("C", "named-not-rechecked", "illustrative", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.optatus-against-donatists",
                         "the schism's own earliest narrative framing")],
            retrieval={"tier": 3, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "We do not call our own communion a schism; we hold that our rival is the one "
                "who broke from the truth. Each side applies the word to the other's own "
                "departure, never to itself."
            ),
            world_word="schism",
            distortion_risk="medium",
            false_friend=[
                "an objective, self-evident historical fact rather than a contested claim each "
                "side applies only to the other",
            ],
            senses={
                "translational": (
                    "'Which side is the real schism?' Each communion answers only one way: the "
                    "other's own departure, never its own."
                ),
            },
            quick_meaning=(
                "We do not think of ourselves as a schism; we hold our rival broke from the "
                "truth, not us."
            ),
        ),
        "Re-derived from Doc_03 Cluster 2 (candidate roster) and Doc_06 SS1 (donlex009, Tier 3, "
        "no change) -- no Lexicon-Chunks deployment file exists for this term; Doc_06 SS3 names "
        "its chunk production as disclosed deferred work. Authored directly from Doc_03's own "
        "one-line meaning at Tier-3-minimum depth. Relations: associated-with Church/Ecclesia "
        "closes the back-edge that Tier-1 chunk's own Related-Terms field already declares "
        "toward this term.",
    ))

    ids.append(emit_term(
        "confessor",
        dict(
            confidence=conf("C", "named-not-rechecked", "illustrative", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.passio-marculi", "the Passio Marculi's own treatment of "
                         "confessors alongside its martyr"),
                      src("don.source.passio-isaac-et-maximiani",
                          "the Passio Isaac et Maximiani's own treatment of the same category")],
            retrieval={"tier": 3, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "A confessor is one of our own who suffered for the faith, and survived. Our "
                "own martyr stories hold this status alongside the martyrs. The two do not "
                "always sit easily together."
            ),
            world_word="confessor",
            distortion_risk="medium",
            false_friend=[
                "a lesser or incomplete version of martyrdom, rather than its own distinct and "
                "sometimes uneasily-related status",
            ],
            senses={
                "translational": (
                    "'Isn't a confessor just a lesser martyr?' Our own Passio Marculi and Passio "
                    "Isaac et Maximiani hold both categories together, and not always "
                    "comfortably -- surviving suffering is not simply a smaller version of dying "
                    "for it."
                ),
            },
            quick_meaning=(
                "A confessor is one of ours who suffered for the faith, and lived. We hold this "
                "status alongside our martyrs, and sometimes in tension with them."
            ),
        ),
        "Re-derived from Doc_03 Cluster 3 (candidate roster) and Doc_06 SS1 (donlex011, Tier 3, "
        "no change) -- no Lexicon-Chunks deployment file exists for this term; Doc_06 SS3 names "
        "its chunk production as disclosed deferred work. Authored directly from Doc_03's own "
        "one-line meaning at Tier-3-minimum depth. Relations: associated-with Martyr/Martyrdom "
        "closes the back-edge that Tier-1 chunk's own Related-Terms field already declares "
        "toward this term (and see donlex010's own provenance note on why bare \"confessor\" is "
        "kept out of that term's own false_friend list).",
    ))

    ids.append(emit_term(
        "church-of-the-martyrs",
        dict(
            confidence=conf("C", "named-not-rechecked", "corroborating", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.passio-donati-sermon",
                         "the commemorative sermons on Sicilibba/Advocata"),
                      src("don.source.passio-marculi", "the Passio Marculi")],
            retrieval={"tier": 2, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "This is our own name for ourselves. We are not a schism defined by what we "
                "left behind. We are the one church that has actually suffered, and gone on "
                "suffering, for what we hold to be true."
            ),
            world_word="Church of the Martyrs",
            distortion_risk="medium",
            false_friend=[
                "self-pity or a persecution complex, rather than our own factual claim about "
                "who has actually suffered and for what",
            ],
            senses={
                "translational": (
                    "'Isn't that just self-pity?' We do not adopt this title for effect. It is "
                    "the plainest description of what has actually happened to us and what we "
                    "have gone on doing since -- reading our own dead's names aloud, at their "
                    "graves, every year."
                ),
            },
            quick_meaning=(
                "Before anything else, we call ourselves the Church of the Martyrs. We are the "
                "church that has suffered, and gone on suffering, for the truth."
            ),
        ),
        "Re-derived from Doc_03 Cluster 3 (candidate roster) and Doc_06 SS1 (donlex012, Tier 2 "
        "confirmed -- \"carried inside the Martyr/Martyrdom Tier-1 entry itself; not separately "
        "promoted\") -- no Lexicon-Chunks deployment file exists for this term as its own chunk; "
        "its fuller depth already lives inside donlex010's own senses.informational (this "
        "record). Authored directly from Doc_03's own one-line meaning at Tier-3-minimum depth "
        "for its own standalone retrievability. Relations: associated-with Martyr/Martyrdom "
        "closes the back-edge that Tier-1 chunk's own Related-Terms field already declares "
        "toward this term.",
    ))

    ids.append(emit_term(
        "deo-laudes",
        dict(
            confidence=conf("C", "named-not-rechecked", "corroborating", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.deo-laudes-acclamation-cil8",
                         "CIL VIII 17732 (Bagai), 20482, 17368, 18669")],
            retrieval={"tier": 2, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "'Deo laudes' -- praise to God -- is our own liturgical acclamation, spoken in "
                "place of our rival's 'Deo gratias.' It is carved on stone at Bagai and "
                "elsewhere, in our own words, with no hostile hand mediating it."
            ),
            world_word="Deo laudes",
            distortion_risk="medium",
            false_friend=[
                "a generic liturgical phrase interchangeable with any church's own praise "
                "formula",
            ],
            senses={
                "translational": (
                    "'Just another way of saying thanks to God?' Not interchangeable -- it is "
                    "our own distinct acclamation, attested on stone at Bagai in our own words, "
                    "with no hostile pen ever standing between us and it."
                ),
            },
            quick_meaning=(
                "We cry 'Deo laudes' -- praise to God -- in place of our rival's 'Deo gratias,' "
                "carved in stone in our own words."
            ),
        ),
        "Re-derived from Doc_03 Cluster 3 (candidate roster) and Doc_06 SS1 (donlex013, Tier 2 "
        "confirmed -- \"carried inside the Martyr/Martyrdom entry's own Worship Ecology "
        "content; not separately promoted\") -- no Lexicon-Chunks deployment file exists for "
        "this term as its own chunk; its fuller depth already lives inside donlex010's own "
        "senses.informational (this record). Authored directly from Doc_03's own one-line "
        "meaning at Tier-3-minimum depth for its own standalone retrievability. Relations: "
        "associated-with Martyr/Martyrdom closes the back-edge that Tier-1 chunk's own "
        "Related-Terms field already declares toward this term.",
    ))

    ids.append(emit_term(
        "anniversaria-commemoratio",
        dict(
            confidence=conf("C", "named-not-rechecked", "illustrative", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.passio-donati-sermon",
                         "the sermon's own commemorative occasion")],
            retrieval={"tier": 3, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "Every year, on the appointed day, we gather at a martyr's grave. We hear the "
                "sermon of his death, read or preached again. We call this the anniversaria "
                "commemoratio. It is the practice behind the Passio Donati sermon itself."
            ),
            world_word="anniversaria commemoratio",
            distortion_risk="low",
            false_friend=[],
            senses={
                "translational": (
                    "'A memorial service, like any other?' It is the occasion the Passio Donati "
                    "sermon itself was written for -- not a general memorial but the specific "
                    "yearly form our own martyr-cult takes."
                ),
            },
            quick_meaning=(
                "Every year, we gather at a martyr's grave. We hear the sermon of his death "
                "again. This is our own anniversary commemoration."
            ),
        ),
        "Re-derived from Doc_03 Cluster 3 (candidate roster) and Doc_06 SS1 (donlex014, Tier 3, "
        "no change) -- no Lexicon-Chunks deployment file exists for this term; Doc_06 SS3 names "
        "its chunk production as disclosed deferred work. Authored directly from Doc_03's own "
        "one-line meaning at Tier-3-minimum depth. No relation is declared: not one of "
        "donlex010's own four listed Related-Terms names this term.",
    ))

    ids.append(emit_term(
        "primate-primas",
        dict(
            confidence=conf("C", "named-not-rechecked", "corroborating", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.augustine-on-baptism-against-donatists",
                         "the Cebarsussi/Bagai council sentences naming Primian as primate")],
            retrieval={"tier": 2, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "Our own primate is the senior bishop of Carthage. First Donatus held it, then "
                "Parmenian, then Primian. Our rival claims the very same title, for its own "
                "bishop of the very same see."
            ),
            world_word="primas",
            distortion_risk="low",
            false_friend=[],
            senses={
                "translational": (
                    "'So there was one archbishop of Carthage?' Two, at once, each claiming the "
                    "same title for the same see -- ours and our rival's."
                ),
            },
            quick_meaning=(
                "Our own primate is the senior bishop of Carthage -- a title our rival claims "
                "too, for its own bishop of the same see."
            ),
        ),
        "Re-derived from Doc_03 Cluster 4 (candidate roster) and Doc_06 SS1 (donlex016, Tier 2 "
        "confirmed) -- no Lexicon-Chunks deployment file exists for this term; Doc_06 SS3 names "
        "its chunk production as disclosed deferred work. Authored directly from Doc_03's own "
        "one-line meaning at Tier-3-minimum depth. Relations: associated-with Bishop/Episcopus "
        "closes the back-edge that Tier-1 chunk's own Related-Terms field already declares "
        "toward this term.",
    ))

    ids.append(emit_term(
        "council-concilium",
        dict(
            confidence=conf("C", "named-not-rechecked", "illustrative", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.augustine-answer-to-letters-of-petilian",
                         "the Cebarsussi (393) and Bagai (394) council sentences")],
            retrieval={"tier": 3, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "Our own councils gather our own bishops. They claim the same binding authority "
                "our rival's councils claim for themselves. Through a council, we once tried, "
                "and succeeded, in disciplining our own dissidents."
            ),
            world_word="concilium",
            distortion_risk="low",
            false_friend=[],
            senses={
                "translational": (
                    "'Just an internal meeting?' Cebarsussi and Bagai were more than that -- "
                    "real conciliar machinery that could, and did, resolve our sharpest internal "
                    "crisis."
                ),
            },
            quick_meaning=(
                "Our own councils claim the same binding authority our rival's councils do. We "
                "once used a council to discipline our own dissidents."
            ),
        ),
        "Re-derived from Doc_03 Cluster 4 (candidate roster) and Doc_06 SS1 (donlex017, Tier 3, "
        "no change) -- no Lexicon-Chunks deployment file exists for this term; Doc_06 SS3 names "
        "its chunk production as disclosed deferred work. Authored directly from Doc_03's own "
        "one-line meaning at Tier-3-minimum depth. Relations: associated-with Bishop/Episcopus "
        "closes the back-edge that Tier-1 chunk's own Related-Terms field already declares "
        "toward this term.",
    ))

    ids.append(emit_term(
        "persecution",
        dict(
            confidence=conf("C", "named-not-rechecked", "corroborating", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.passio-marculi", "the Macarian repression, 347-348"),
                      src("don.source.passio-isaac-et-maximiani",
                          "the Macarian repression, 347-348")],
            retrieval={"tier": 2, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "We hold two persecutions in memory. We do not let them blur into one. The "
                "empire-wide terror came first, and we suffered it alongside our eventual "
                "rival. The later persecution made our martyrs. It came at our own rival's own "
                "instigation."
            ),
            world_word="persecution",
            distortion_risk="medium",
            false_friend=[
                "one continuous persecution, rather than two distinct episodes with two "
                "distinct persecutors",
            ],
            senses={
                "translational": (
                    "'Wasn't it all the same persecution?' No -- we hold the shared "
                    "Diocletianic terror and the later, rival-instigated Macarian repression "
                    "apart, deliberately, because the second one is our own case in miniature."
                ),
            },
            quick_meaning=(
                "We remember two persecutions, not one. The first was empire-wide terror, "
                "shared with our rival. The second, later one, our rival brought upon us."
            ),
        ),
        "Re-derived from Doc_03 Cluster 5 (candidate roster) and Doc_06 SS1 (donlex020, Tier 2 "
        "confirmed) -- no Lexicon-Chunks deployment file exists for this term; Doc_06 SS3 names "
        "its chunk production as disclosed deferred work. Authored directly from Doc_03's own "
        "one-line meaning at Tier-3-minimum depth, drawing the same dual-persecution content "
        "donlex010/019's own chunks already carry in their own bodies. Relations: "
        "associated-with Agonistici and Refusal of Imperial Legitimacy close the back-edges "
        "those two Tier-1 chunks' own Related-Terms fields already declare toward this term.",
    ))

    ids.append(emit_term(
        "liber-regularum",
        dict(
            confidence=conf("C", "named-not-rechecked", "corroborating", "Widely Accepted",
                             _MINIMAL_DEFAULT_DIVERGENCE),
            sources=[src("don.source.tyconius-liber-regularum",
                         "whole work -- our own strongest surviving theological writing")],
            retrieval={"tier": 2, "retrieve_when": [], "do_not_retrieve_when": []},
            plain_meaning=(
                "Tyconius, one of our own, set down seven rules for reading scripture. He "
                "called the book Liber Regularum. It is our strongest work of biblical "
                "interpretation. Even so, our own council later condemned him for it."
            ),
            world_word="Liber Regularum",
            distortion_risk="low",
            false_friend=[],
            senses={
                "translational": (
                    "'Was Tyconius a Donatist theologian?' He was ours by communion, then "
                    "condemned by our own council for his universalist reading of the church -- "
                    "a founding figure we did not fully keep."
                ),
            },
            quick_meaning=(
                "Tyconius, one of ours, wrote seven rules for reading scripture. It is our "
                "strongest work of interpretation. We later condemned him for it anyway."
            ),
        ),
        "Re-derived from Doc_03 Cluster 6 (candidate roster, the thin interpretive cluster per "
        "Doc_01 SS3) and Doc_06 SS1 (donlex021, Tier 2 confirmed -- tested as D-B at Doc_04 SS2, "
        "did not advance as a gravity) -- no Lexicon-Chunks deployment file exists for this "
        "term; Doc_06 SS3 names its chunk production as disclosed deferred work. Authored "
        "directly from Doc_03's own one-line meaning at Tier-3-minimum depth. No relation is "
        "declared: Doc_03 SS6 and Doc_06 SS1 both confirm this cluster stands alone, and no "
        "built Tier-1 chunk's own Related-Terms field names this term.",
    ))

    return ids


def main() -> None:
    tier1_ids = build_tier1_terms()
    minimal_ids = build_minimal_terms()
    all_ids = tier1_ids + minimal_ids
    assert len(tier1_ids) == 7, f"expected 7 Tier-1 term records, built {len(tier1_ids)}"
    assert len(minimal_ids) == 14, f"expected 14 Tier-2/Tier-3 term records, built {len(minimal_ids)}"
    assert len(all_ids) == 21, f"expected 21 term records total (Doc_06's own full roster), built {len(all_ids)}"
    assert len(set(all_ids)) == 21, "duplicate term id detected"
    print(f"Wrote {len(WRITTEN)} term records under {RECORDS_ROOT / 'term'}:")
    print(f"  - {len(tier1_ids)} Tier-1 (full depth, from Lexicon-Chunks)")
    print(f"  - {len(minimal_ids)} Tier-2/Tier-3 (minimum depth, from Doc_03 direct)")


if __name__ == "__main__":
    sys.exit(main())
