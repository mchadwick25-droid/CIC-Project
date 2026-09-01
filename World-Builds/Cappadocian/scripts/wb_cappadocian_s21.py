"""B-1 (S2.1): Nicene-Cappadocian (cappadocian) source + world_core records.

WHAT THIS SCRIPT DOES. Converts this world's completed Phase A documents into
WRS records under records/cappadocian/{source,world_core}/, per the live
schema (engine/m1/schemas.py) and gate battery (engine/m1/gates.py). This is
the FIRST record-authoring pass for this world; no cappadocian records
existed before this script ran.

INPUTS, mapped to OUTPUTS, precisely:
  - World-Builds/Nicene-Cappadocian/cappadocian_Source_Registry.md (116 rows,
    Parts A-H) -> the 110 `source` records (ROWS below). Only rows with
    Boundary Status "Native" become records. The 6 Excluded rows -- Part A's
    four pre-adjudicated Named Comparanda (rows 1-4: Athanasius/Alexandria
    corpus, the Egyptian desert corpus, later Basilian/Byzantine Cappadocia,
    Evagrius' post-Cappadocian corpus), row 64 (the Homoian establishment's
    own imperial acts, Named Comparandum), and row 116 (Armenian Christian
    literature, Out-of-Boundary, post-405) -- are deliberately NOT emitted as
    this world's own source records; they belong to other worlds or are
    refused material, exactly as the Registry itself disposes them.
  - cappadocian_Doc_01_World_Identification.md -> world_core.time_window,
    .horizon (the corrected self-description naming Eupsychius, not "the
    peace after the last martyrs").
  - cappadocian_Integrated_Ecology_Analysis.md (filename is Doc_07, despite
    the "Doc_07" label the orchestrating brief used) SS2E/SS3/SS5 ->
    world_core.formation_logic.
  - cappadocian_Doc_02_Source_Ecology.md SS6 (missing voices), SS9
    (confidence map) + the Source Registry's own named gaps ->
    world_core.thinness / .cautions / .thin_topics.

MECHANICAL vs AUTHORED, field by field (so a reviewer can tell what to
re-check against the Registry directly vs what required this script's own
reading and judgment):
  - id, world_id, record_type, schema_version, status, register, canon_cells:
    MECHANICAL -- fixed per envelope convention (register="etic" for every
    source record, matching hal.source.* precedent: a source record
    describes an external text, not the world's own first-person voice;
    canon_cells=[] throughout, since no canon-cell tagging work has happened
    yet at this build step).
  - author / work / edition: AUTHORED, per row, by hand. The Registry's own
    `Source` column is ONE free-text cell mixing author, work-with-scope,
    and (sometimes) a vendored file path or translator/press/year in one
    string (e.g. row 8's "Basil, canons 40 and 42 (on marriages of enslaved
    persons without an owner's consent)"). Splitting that cell into three
    schema fields is NOT a mechanical regex split -- e.g. row 56 has no
    author in the ordinary sense (a biographical fact about Evagrius, not a
    text of his own) and row 70 has no independent text at all (attested
    only inside his son's oration) -- both required reading the row's own
    Verification Note to decide how to phrase author/work/edition honestly
    rather than leaving the schema's required, non-blank fields empty or
    fabricating specificity the Registry itself doesn't have. Where the
    Registry names a `cic/texts/...` vendored file, that path is carried
    into `edition`, matching hal.source.augustine-city-of-god's own
    precedent exactly.
  - rights_status: AUTHORED per row via the RIGHTS_* dict below (5 buckets:
    vendored+session-verified, vendored+earlier-session, in-copyright and
    manifest-excluded by design, not-yet-acquired, or "no text exists to
    hold rights over"). Every vendored file's rights are independently
    confirmed Public Domain per CAPPADOCIAN_BUILD_LEDGER.md SS9 and
    cic/engine/texts_registry.py -- checked against that registry's actual
    filenames (grep, 2026-08-31 session) before this script was written, not
    assumed from the Source Registry's own prose. No row is left blank;
    gate_rights fails closed on blank, and several rows (unacquired,
    in-copyright, fact-only) required an honest non-blank negative
    statement rather than a false positive.
  - attribution_status: AUTHORED per row. Default "attributed". Carried
    honestly as a short descriptive phrase (never forced into a binary the
    schema doesn't require -- it's a free string) wherever the Registry's
    own Verification Note flags contested or disputed authorship: rows 12
    (Basil-Libanius, majority-forgery view), 23 (Ep. 38, reassigned by
    Cavallin/Hubner/Zachhuber/Drecoll to Gregory of Nyssa), 25 (Liturgy of
    St Basil, core vs. transmitted-wording split), 26 (Ep. 8, generally
    Evagrius not Basil), 27 (Apollinaris correspondence, contested in
    antiquity), 67 (Address of Thanksgiving to Origen), 68 (the Thaumaturgus
    creed), 81 (the Philocalia's compiling attribution).
  - discovery_channel: AUTHORED via dc() below, keyed to the SAME
    verification-state judgment as confidence.verification_state (next
    paragraph) so the two fields never silently disagree, and naming the
    Source Registry row number for traceability (also mirrored into
    external_ids.cappadocian_source_registry_row -- a judgment call: the
    schema has no dedicated Registry-row field, and putting the number in a
    queryable object field, not only in prose, makes future cross-checking
    against the Registry mechanical rather than requiring a text search).
  - confidence.citation_specificity: MECHANICAL -- copied directly from the
    Registry's own Confidence (A-E) column. The brief's own framing note
    (both axes use the same letter grades) makes this the one field with no
    real judgment call in it.
  - confidence.verification_state: AUTHORED, but via one explicit, fully
    mechanical-once-decided rule (not a per-row guess), stated here so it
    can be checked against the Registry text directly:
      * Registry Confidence A (the 9 rows this build session itself opened
        and confirmed complete -- rows 18, 21, 22, 33, 48, 57, 63, 71, 72,
        per the Registry's own SS"A-B distinction" note) -> verified-direct.
      * Registry Confidence B, where the row's own Verification Note cites
        an already-vendored cic/texts/ file with NO further hedge on this
        specific citation (a bare "Within npnf208." or equivalent) ->
        verified-via-authority: a real, checkable, rights-confirmed text
        stands behind the claim, just not reopened by this session.
      * Registry Confidence B where the note EITHER hedges this specific
        citation ("not independently re-checked against the specific canon
        numbers this session", "not re-verified this session", "no
        independent text exists to verify against") OR the text is not
        vendored at all (named but unacquired, or deliberately excluded as
        in-copyright) -> named-not-rechecked.
      * Registry Confidence C (by the template's own definition, a named
        author/scholar without a pinpointed locus) -> named-not-rechecked,
        uniformly -- C-tier is inherently "named, not independently
        checked" in the Registry's own vocabulary.
      * Registry Confidence D (no named author or text at all -- a general
        regional/period pattern) -> unverified. No Native row in this
        Registry carries an E rating (the Registry's own three review
        rounds moved every genuinely-named row up to at least C; only
        Excluded rows 3/64/116 remain at D and none at E among Natives).
    This rule was applied by reading each row's own Verification Note
    against it, not by a script transforming the Confidence letter alone --
    two rows with the same letter can and do land in different verification
    states here (contrast row 7, bare "Within npnf208.", against row 8,
    "not independently re-checked against the specific canon numbers this
    session" -- both Confidence B, different verification_state).
  - confidence.evidentiary_weight: AUTHORED per row from the Registry's own
    Licensed For column, per the brief's own instruction. `contested` (a
    real enum value, not a fallback) is used narrowly and only where the
    SOURCE OBJECT's own genuineness or exact identity, not merely its
    authorship attribution, is disputed: row 12 (majority-forgery view of
    the correspondence itself), row 25 (the transmitted liturgy's wording),
    row 68 (the creed's own authenticity), row 81 (the Philocalia's
    compiling act itself now Contested). Authorship disputes that don't
    touch the object's own genuineness (23, 26, 27, 67) are carried in
    attribution_status instead, keeping the two axes independent.
  - confidence.formation_confidence: AUTHORED per row, Article 17's five-
    level vocabulary, deliberately NOT derived from citation_specificity
    (the brief's own central warning). Default Widely Accepted for any row
    not otherwise flagged -- a text's existence/basic content being
    standard and undisputed, without THIS session's own direct check, is
    Widely Accepted, not Documented; Documented is reserved for rows this
    record can honestly pair with verified-direct (see the crosscheck note
    below). Overridden per row where the Registry/Doc_02 itself names a
    stronger or weaker state: Contested for rows 12, 23, 25, 26, 27, 60
    (Gangra's own date), 67, 68, 81, and for the Part F rows that are
    themselves one side of one of Doc_02 SS5's eleven named "Contested"
    debates (McGuckin/McLynn on debate 6; Silvas/Clark on debate 2;
    Ayres/Behr/Barnes/Anatolios/Beeley/Coakley on debate 1; Caner/Stewart on
    debate 8; Drecoll on the Ep. 38 question); Dominant Modern
    Reconstruction for rows 28 (the Maraval/Pouchet redating literature --
    Doc_01's own chronology finding rests on exactly this), 96 (Sterk), and
    97 (Holman), matching Doc_02 SS9's own explicit DMR list; Inferential-
    Thin for rows resting on a named-but-unlocated or genuinely thin
    citation with no content in hand (39, 40, 54, 65, 74, 84).
  - confidence.divergence_note: null by default; populated with a short,
    honest sentence wherever a row's formation_confidence needed explaining
    against its verification_state (e.g. row 48, the Life of Macrina: text
    verified-direct this session, but formation_confidence is held at
    Widely Accepted rather than Documented because Doc_02 SS1.4 itself
    downgrades Macrina's recoverability, not because this session's own
    textual check was incomplete) -- gate_confidence_crosscheck's own rule
    (Documented + null divergence_note requires verified-direct) is
    satisfied by construction: this script never emits Documented without
    either verified-direct or a divergence_note, checked in emit_source()
    itself as a hard assertion, not left to hope.
  - sources / relations (on EACH source record): left empty by design, a
    judgment call. The task brief expects gate_referential/gate_reciprocity
    trivially clean at this step; populating cross-references between
    source records now would require reciprocal `relations` entries on both
    sides (gate_reciprocity) for no benefit this step actually needs. The
    world_core record DOES populate `sources`, referencing a handful of the
    richest source ids created in this same run -- those resolve cleanly
    under gate_referential since both records are emitted together.

WORLD_ID: this world has never been given a `world_id` value anywhere in the
live system (worlds.yaml has no `cappadocian` entry at all yet -- confirmed
by reading it directly before writing this script). Following this project's
own convention (kebab-case, derived from the world's registry name, e.g.
hieronymian-ascetic-literary, imperial-juridical, syriac-edessa-nisibis),
this script mints `nicene-cappadocian` and uses it throughout. This is a
judgment call for a later world-admission step (worlds.yaml) to ratify, not
override -- recorded here, not silently assumed.

SCRIPT LOCATION: placed at World-Builds/Nicene-Cappadocian/scripts/, a new
directory. No prior new-world build under the current (post cic-poc
retirement) tooling has established a canonical location for these
authoring scripts -- the one located predecessor (cic-poc/backend/wrs/
migrate/s62_hal_s21.py, inspected via `git show` for its shape only, since
its own field names target a fully retired schema) lived inside the retired
backend tree, which no longer exists. Placing this script beside the
world's own Phase A documents (rather than under engine/ or records/) is
this script's own judgment call: it is build tooling for ONE world, reads
that world's own documents by relative path, and has no reason to live
inside the shared engine.

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells (no canon-cell tagging work
has happened for this world yet -- expected, per the brief, to leave
canon-coverage/narratability/etc. trivially incomplete at this step);
register `cappadocian` in records/worlds.yaml (out of scope for S2.1, a
later admission-track step); touch any other world's records.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]  # .../CIC-Project
RECORDS_ROOT = REPO_ROOT / "records" / "cappadocian"

WORLD_ID = "nicene-cappadocian"
SCHEMA_VERSION = 2

# ---------------------------------------------------------------------------
# Shared edition strings for vendored NPNF/ANF volumes cited by many rows.
# Filenames checked directly against cic/engine/texts_registry.py's own
# ENTRIES tuple (grep, 2026-08-31) before use here -- not copied blind from
# the Registry's own prose.
NPNF208 = ("Nicene and Post-Nicene Fathers, 2nd series, vol. 8 (Basil: Letters and Select "
           "Works), ed. Schaff, vendored as cic/texts/npnf208_basil-letters-select-works.xml")
NPNF207 = ("Nicene and Post-Nicene Fathers, 2nd series, vol. 7 (Cyril of Jerusalem, Gregory "
           "Nazianzen), ed. Schaff, vendored as cic/texts/npnf207_cyril-jerusalem-gregory-"
           "nazianzen.xml (covers the Orations; among the ~245 letters, only Epp. 101, 102, 202)")
NPNF205 = ("Nicene and Post-Nicene Fathers, 2nd series, vol. 5 (Gregory of Nyssa: Dogmatic, "
           "Ascetic, and Moral Treatises, Letters), ed. Schaff, vendored as "
           "cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt")
NPNF203 = ("Nicene and Post-Nicene Fathers, 2nd series, vol. 3 (Theodoret, Jerome, Gennadius, "
           "Rufinus), ed. Schaff, vendored as cic/texts/npnf203_theodoret-jerome-gennadius-"
           "rufinus.xml")
NPNF202 = ("Nicene and Post-Nicene Fathers, 2nd series, vol. 2 (Socrates, Sozomen: "
           "Ecclesiastical Histories), ed. Schaff, vendored as cic/texts/"
           "npnf202_socrates-sozomen-ecclesiastical-histories.xml")
NPNF214 = ("Nicene and Post-Nicene Fathers, 2nd series, vol. 14 (The Seven Ecumenical "
           "Councils), ed. Schaff, vendored as cic/texts/npnf214_seven-ecumenical-councils.xml")
ANF05 = ("Ante-Nicene Fathers, vol. 5 (Hippolytus, Cyprian, Caius, Novatian, Appendix), ed. "
         "Roberts & Donaldson, vendored as cic/texts/anf05_hippolytus-cyprian-caius-"
         "novatian.xml")
ANF06 = ("Ante-Nicene Fathers, vol. 6 (Gregory Thaumaturgus, Dionysius, Julius Africanus, "
         "Methodius, Arnobius), ed. Roberts & Donaldson, vendored as cic/texts/anf06_gregory-"
         "thaumaturgus-dionysius-julius-africanus-methodius-arnobius.xml")

RIGHTS = {
    "vv": ("public-domain; vendored in cic/texts/ and independently verified (identity, "
           "completeness, provenance) by this build session before vendoring "
           "(CAPPADOCIAN_BUILD_LEDGER.md SS9)."),
    "v": ("public-domain; vendored in cic/texts/, rights independently confirmed "
          "(cic/engine/texts_registry.py) in an earlier session, not re-checked by this "
          "citation session (CAPPADOCIAN_BUILD_LEDGER.md SS9)."),
    "na": ("not independently verified this session; row not yet acquired as an open text -- "
           "named for completeness per the Source Registry's own checkpoint rule (every source "
           "a Doc_02 claim rests on gets a row, acquired or not)."),
    "ic": ("in-copyright modern scholarship or translation; deliberately excluded from the "
           "vendoring manifest on rights grounds, not merely unacquired (Source Registry Part F "
           "note) -- not independently verified this session."),
    "nt": ("not applicable in the ordinary sense -- no single specific text has been identified "
           "for this row; it names a person, general pattern, or unlocated corpus rather than a "
           "held text. Not independently verified this session."),
    "fact": ("not applicable in the ordinary sense -- no text exists to hold rights over; this "
             "row records a biographical/documentary fact, not a copyrighted or public-domain "
             "work."),
}


def dc(num: int, verify: str) -> str:
    if verify == "verified-direct":
        return (f"builder-prior-knowledge; Source Registry row {num}; the file itself was "
                 "independently verified for identity, completeness, and provenance by this "
                 "build session before vendoring (CAPPADOCIAN_BUILD_LEDGER.md SS9).")
    if verify == "verified-via-authority":
        return (f"builder-prior-knowledge; Source Registry row {num}; a named, vendored text "
                 "already sitting in cic/texts/ (present since an earlier session), not "
                 "reopened to recheck this specific citation this session.")
    if verify == "named-not-rechecked":
        return (f"builder-prior-knowledge; Source Registry row {num}; a specific named source "
                 "(author, translator, edition, or witness) that this session did not "
                 "independently check against primary content -- either its own specific locus "
                 "was not reopened in an already-vendored file, or the named text has not yet "
                 "been acquired at all (see rights_status for which).")
    if verify == "unverified":
        return (f"builder-prior-knowledge; Source Registry row {num}; a general regional/period "
                 "pattern with no single named author or text of its own.")
    raise ValueError(verify)


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


WRITTEN: list[str] = []


def emit_source(num, slug, author, work, edition, rights_key, attribution,
                 cite, verify, weight, formation, divergence, body):
    payload = {
        "id": f"cappadocian.source.{slug}",
        "world_id": WORLD_ID,
        "record_type": "source",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "etic",
        "canon_cells": [],
        "confidence": conf(cite, verify, weight, formation, divergence),
        "sources": [],
        "relations": [],
        "author": author,
        "work": work,
        "edition": edition,
        "rights_status": RIGHTS[rights_key],
        "attribution_status": attribution,
        "discovery_channel": dc(num, verify),
        "external_ids": {"cappadocian_source_registry_row": num},
    }
    out_dir = RECORDS_ROOT / "source"
    out_dir.mkdir(parents=True, exist_ok=True)
    front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    text = f"---\n{front}---\n{body.strip()}\n"
    path = out_dir / f"{payload['id']}.md"
    path.write_text(text, encoding="utf-8")
    WRITTEN.append(str(path))
    return payload["id"]


def build_sources() -> dict[str, str]:
    ids: dict[str, str] = {}

    # --- Part B: Basil of Caesarea (Registry rows 5-30) ---------------------
    ids["basil-letters-general-corpus"] = emit_source(
        5, "basil-letters-general-corpus", "Basil of Caesarea (c. 329/30-377)",
        "Basil's Letters, general corpus (300+ letters, c. 360s-370s)", NPNF208, "v", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "Grounds the Trinitarian-confession, doxology, and bishop-as-public-patron gravity "
        "candidates and the famine narrative (Registry row 5; Doc_01 SS2; Doc_02 SS8 Tier 1). "
        "File vendored since 2026-08-15, not re-verified against specific loci this session; "
        "the more targeted citations below (canonical letters, the Eustathius-rupture letters, "
        "etc.) carry their own, more specific verification status.")
    ids["basil-canonical-letters-to-amphilochius"] = emit_source(
        6, "basil-canonical-letters-to-amphilochius", "Basil of Caesarea",
        "Basil's canonical letters as a body, addressed to Amphilochius of Iconium "
        "(Epp. 188, 199, 217)", NPNF208, "v", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "Doc_02 SS2's 'single best window this world offers on ordinary village sin and the "
        "church's discipline of it' (row 6). Honest caveat carried forward: Doc_02 SS2 names "
        "'Basil's canonical letters' without giving these three specific numbers -- 188, 199, "
        "and 217 are supplied from general scholarly knowledge of Basil's corpus, not "
        "independently re-verified against the vendored file's own text this session. Canon 21 "
        "within Ep. 199 (see the next record) is the single sharpest instance.")
    ids["basil-epistle-199-canon-21"] = emit_source(
        7, "basil-epistle-199-canon-21", "Basil of Caesarea",
        "Basil, canonical Epistle 199 (to Amphilochius), specifically canon 21 -- not to be "
        "confused with the separate Epistle 21, a different letter entirely", NPNF208, "v",
        "attributed", "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "SS6.1's sharpest in-world acknowledgment of gendered discipline: Basil grades "
        "adultery's penance unequally by sex (the wife punished, the husband not) and states "
        "plainly he cannot account for the double standard (row 7; Doc_02 SS6.1). Cite as "
        "'canon 21' or 'Ep. 199, canon 21' -- never as 'Epistle 21', per Doc_02 SS6.1's own "
        "flagged confusion risk.")
    ids["basil-canons-40-42-enslaved-marriage"] = emit_source(
        8, "basil-canons-40-42-enslaved-marriage", "Basil of Caesarea",
        "Basil, canons 40 and 42 (on marriages of enslaved persons contracted without an "
        "owner's consent)", NPNF208, "v", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "SS6.3's against-the-grain evidence on the enslaved: a legal question about whose "
        "consent is required for an enslaved person's marriage, not whether the institution "
        "itself may stand (row 8; Doc_07 SS2J). Not independently re-checked against the "
        "specific canon numbers this session -- carried at the Registry's own honest caveat.")
    ids["basil-chorepiscopoi-letters"] = emit_source(
        9, "basil-chorepiscopoi-letters", "Basil of Caesarea",
        "Basil, the chorepiscopoi letters (Epp. 53, 54)", NPNF208, "v", "attributed",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "SS6.2's against-the-grain window on rural clergy, ordination-selling, and village "
        "clergy numbers (row 9; Doc_02 SS6.2).")
    ids["basil-eustathius-rupture-letters"] = emit_source(
        10, "basil-eustathius-rupture-letters", "Basil of Caesarea",
        "Basil, the Eustathius-rupture letters (Epp. 119, 128, 130, 223, 226, 244, 251)",
        NPNF208, "v", "attributed", "B", "verified-via-authority", "load-bearing",
        "Widely Accepted", None,
        "Grounds the Basil/Eustathius rupture (Doc_02 SS8 Tier 1 story candidate; Doc_01 SS3's "
        "pneumatological-rupture fracture line) and this Registry's own choice to license it to "
        "the Eustathius-debt/Small-Asketikon question (row 10). Divergence carried forward "
        "honestly, not silently resolved: Doc_02 SS8 calls this rupture 'the hinge of SS5 "
        "debate (10)' (the oikonomia/reserve-motives debate); the Registry instead licenses it "
        "primarily to the Eustathius-debt question as the closer fit -- flagged as a divergence "
        "from Doc_02's own cross-reference, a Doc_02-level call to resolve, not this record's. "
        "Epp. 204 and 223 also ground the Macrina the Elder datum (next record).")
    ids["basil-macrina-the-elder-letters"] = emit_source(
        11, "basil-macrina-the-elder-letters", "Basil of Caesarea",
        "Basil, Epistles 204 and 223 (Macrina the Elder, transmission of Gregory Thaumaturgus' "
        "own teaching)", NPNF208, "v", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "Macrina the Elder -- this world's single most valuable non-male-mediated female "
        "formation datum, not filtered through her granddaughter's literary frame (row 11; "
        "Doc_02 SS1.4, SS6.1).")
    ids["basil-libanius-correspondence"] = emit_source(
        12, "basil-libanius-correspondence", "Basil of Caesarea (disputed correspondent: "
        "Libanius of Antioch)", "Basil-Libanius correspondence (Epistles 335-359)", NPNF208, "v",
        "contested (majority view among Libanius scholars: the entire exchange is a known "
        "forgery, with a proposed forger's motive on record; if genuine, rare direct contact "
        "with a leading pagan intellectual -- if forged, as the majority holds, it cannot "
        "ground that contact at all)",
        "B", "verified-via-authority", "contested", "Contested",
        "Majority scholarship (Doc_02 SS1.1, SS1.6) holds this correspondence a known forgery. "
        "Citation-reliability B reflects that specific letters are named and locatable within "
        "an already-vendored file, not that the underlying contact is real -- never cite this "
        "record as evidence of genuine Basil-Libanius contact without flagging the forgery "
        "question at every use, per Doc_02's own instruction and Registry row 12/debate (11).",
        "Licensed only for SS5 debate (11): the correspondence's own genuineness, carried as "
        "its own named debate -- never for a standalone claim of genuine contact.")
    ids["basil-on-the-holy-spirit"] = emit_source(
        13, "basil-on-the-holy-spirit", "Basil of Caesarea",
        "Basil, On the Holy Spirit (c. 375)", NPNF208, "v", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "Grounds the doxology-controversy gravity/Tier 1 story candidate, SS2's "
        "unwritten-customs liturgical evidence, and SS5 debate (10), the oikonomia/reserve "
        "question (row 13). Occasioned by controversy over Basil's own doxology, per the "
        "treatise's own account.")
    ids["basil-against-eunomius"] = emit_source(
        14, "basil-against-eunomius", "Basil of Caesarea",
        "Basil, Against Eunomius (books 1-3; later books spurious, Widely Accepted)", NPNF208,
        "v", "attributed", "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "Grounds the Trinitarian-confession gravity's Eunomian-contest question and Eunomius' "
        "own First Apology's role as the rare two-sided control (row 14; Doc_01 SS1). No "
        "complete open English translation of this work exists (row 24, DelCogliano & "
        "Radde-Gallwitz 2011, is copyrighted and excluded from this manifest) -- a real scope "
        "limit of the acquired edition, not a fresh gap this row itself creates.")
    ids["basil-hexaemeron-homilies"] = emit_source(
        15, "basil-hexaemeron-homilies", "Basil of Caesarea",
        "Basil, the Hexaemeron homilies", NPNF208, "v", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "Congregational preaching-culture evidence (Doc_02 SS2), completed by Gregory of "
        "Nyssa's On the Making of Man (row 47).")
    ids["basil-moral-famine-homilies"] = emit_source(
        16, "basil-moral-famine-homilies", "Basil of Caesarea",
        "Basil, the moral/famine homilies (on famine and drought; the rich fool's barns; "
        "against usury, envy, anger, drunkenness; on the Forty Martyrs and local martyrs)",
        NPNF208, "v", "attributed", "B", "verified-via-authority", "load-bearing",
        "Widely Accepted", None,
        "Grounds the famine-of-368/9 Tier 1 story candidate (Doc_02 SS8), the "
        "poor-institutionalized gravity candidate, and the martyr-homily record (row 20).")
    ids["basil-antiphonal-psalmody-baptismal-letters"] = emit_source(
        17, "basil-antiphonal-psalmody-baptismal-letters", "Basil of Caesarea",
        "Basil's letter defending antiphonal night psalmody against Neocaesarean criticism, "
        "and his baptismal protreptic to delay-prone catechumens", NPNF208, "v", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The liturgical-evidence section (Doc_02 SS2): worship reconstructed from preachers "
        "describing it. Specific letters named by Doc_02 SS2 but not independently isolated by "
        "exact number this session (row 17).")
    ids["basil-asketikon-longer-shorter-rules"] = emit_source(
        18, "basil-asketikon-longer-shorter-rules", "Basil of Caesarea",
        "Basil, the Asketikon -- the Great Asketikon: complete Longer and Shorter Rules, the "
        "Moralia, and the wider ascetic corpus",
        "Clarke's 1925 translation, vendored as "
        "cic/texts/basil_ascetic-works-longer-shorter-rules_clarke1925.txt", "vv", "attributed",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "Grounds the ascetic-communal-movement gravity candidate, SS6.3's runaway-slave "
        "provisions, SS6.4's Shorter Rules against-the-grain community voice, and SS6.7's "
        "Longer Rule 15 on children (row 18). Verified this session: confirmed complete "
        "against its own table of contents (Introduction, Praevia Institutio Ascetica, "
        "Sermones Ascetici, De Iudicio Dei, De Fide, the Moralia, the Longer Rules, the Shorter "
        "Rules) -- this is the Great Asketikon; the non-Greek Small Asketikon (next-but-one "
        "record) remains a distinct, unfilled acquisition.")
    ids["basil-small-asketikon"] = emit_source(
        19, "basil-small-asketikon", "Basil of Caesarea",
        "Basil's Small Asketikon (non-Greek: Rufinus' Latin translation, 397; a Syriac "
        "version, earliest manuscript late 5th century) -- does not survive in Greek at all",
        "Named witnesses only (Rufinus' 397 Latin translation; a dated Syriac manuscript "
        "tradition) -- no open English translation located this session or previously", "na",
        "attributed", "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "Grounds SS1.1's Small/Great Asketikon distinction and SS6.6's non-Greek-transmission "
        "correction (row 19). A real, identifiable recension awaiting acquisition, not 'no "
        "traceable source' -- Gribomont's textual work (row 100) establishes this recension's "
        "priority over the Great Asketikon from exactly these non-Greek witnesses, itself "
        "load-bearing for SS1.1/SS6.6 even without the text in hand.")
    ids["basil-martyr-homilies-forty-gordius-julitta-mamas"] = emit_source(
        20, "basil-martyr-homilies-forty-gordius-julitta-mamas", "Basil of Caesarea",
        "Basil, martyr homilies on the Forty of Sebaste, Gordius, Julitta, and Mamas", NPNF208,
        "v", "attributed", "B", "verified-via-authority", "load-bearing", "Widely Accepted",
        None,
        "The Forty Martyrs Tier 2 story candidate (Doc_02 SS8) and the martyrs'-festival "
        "gravity candidate (row 20).")
    ids["basil-address-to-young-men"] = emit_source(
        21, "basil-address-to-young-men", "Basil of Caesarea",
        "Basil, Address to Young Men on the Right Use of Greek Literature",
        "Padelford's 1902 translation, vendored as "
        "cic/texts/basil_address-to-young-men_padelford1902.txt", "vv", "attributed",
        "A", "verified-direct", "load-bearing", "Documented",
        "The translator attribution (Padelford, 1902) rests on this world's own manifest "
        "citation, not on a title page inside the vendored transcription itself, which does "
        "not name its translator -- the WORK's completeness is verified-direct; the specific "
        "translator credit is carried at this lower confidence, named honestly rather than "
        "silently upgraded.",
        "Grounds the paideia-converted gravity candidate (row 21). Confirmed complete this "
        "session (translator's Outline, all ten chapters, closing paragraph, full 68-entry "
        "footnote set).")
    ids["morison-st-basil-and-his-rule"] = emit_source(
        22, "morison-st-basil-and-his-rule", "E. F. Morison",
        "St. Basil and His Rule: A Study in Early Monasticism (Oxford, 1912)",
        "Vendored as cic/texts/morison_st-basil-and-his-rule_1912.txt", "vv", "attributed",
        "A", "verified-direct", "illustrative", "Documented", None,
        "Supplementary reading for the Asketikon (row 18); Appendix A/B carry translated "
        "primary excerpts of Basil's own Proem to the Longer and Shorter Rules; chapter XI "
        "('Women, Children, and Slaves') is a further against-the-grain candidate for SS6, not "
        "yet drawn on (row 22). A bonus acquisition, not currently cited by Doc_02 at all -- "
        "included for completeness and future use, weighted illustrative rather than "
        "load-bearing on that honest basis.")
    ids["basil-epistle-38-ousia-hypostasis"] = emit_source(
        23, "basil-epistle-38-ousia-hypostasis", "Basil of Caesarea (contested; see "
        "attribution_status)", "Basil, canonical Epistle 38 (on ousia/hypostasis) -- this "
        "world's flagship Tier 1 lexicon citation", NPNF208, "v",
        "contested (transmitted under both Basil's and his brother Gregory of Nyssa's names; "
        "reassigned by a substantial body of modern scholarship -- Cavallin, Hubner, Zachhuber, "
        "with Drecoll leaning the same way -- to Gregory of Nyssa)",
        "B", "verified-via-authority", "load-bearing", "Contested",
        "cappadocianlex001_ousia-hypostasis.md currently states only that the letter is "
        "'transmitted under both Basil's and his brother's names -- attribution contested, "
        "carried,' without naming a preferred author or citing the letter by number -- this "
        "record's fuller attribution detail (row 23) should not be read as already reflected "
        "there; that lexicon file may need its own update, flagged here rather than assumed.",
        "This world's flagship Trinitarian-vocabulary citation (row 23). The letter's text and "
        "transmission are not in question -- only who wrote it -- so evidentiary_weight stays "
        "load-bearing while formation_confidence carries the authorship dispute.")
    ids["delcogliano-radde-gallwitz-against-eunomius-translation"] = emit_source(
        24, "delcogliano-radde-gallwitz-against-eunomius-translation", "Mark DelCogliano & "
        "Andrew Radde-Gallwitz (translators)",
        "Against Eunomius (Fathers of the Church 122, 2011) -- the only complete English "
        "translation of Basil's Against Eunomius",
        "Fathers of the Church series, vol. 122, 2011 -- copyrighted, not vendored", "ic",
        "attributed", "B", "named-not-rechecked", "illustrative", "Widely Accepted", None,
        "Would complete row 14's translation coverage of Against Eunomius if acquired (row 24). "
        "Named specifically by Doc_02 SS1.1 as the one complete translation -- translators, "
        "series, and year all named, hence B per the Registry's own rule regardless of "
        "acquisition status.")
    ids["liturgy-of-st-basil"] = emit_source(
        25, "liturgy-of-st-basil", "Attributed to Basil of Caesarea (split attribution; see "
        "attribution_status)", "The 'Liturgy of St Basil' (transmitted anaphora)",
        "No vendored or independently locatable edition this session", "nt",
        "contested (a Basilian core, argued substantially from the Egyptian recension E-BAS, "
        "is Dominant Modern Reconstruction; the transmitted Byzantine text's exact wording as "
        "Basil's own is Contested -- this record deliberately does not resolve the split "
        "further)",
        "B", "named-not-rechecked", "contested", "Contested", None,
        "The doxology/worship gravity candidate; SS2's liturgical-evidence section (row 25). A "
        "specific, identifiable liturgical text, hence B -- not locatable as a vendored primary "
        "edition this session, so this record grounds only the fact and shape of the "
        "attribution question, never the transmitted text's specific wording as Basil's own.")
    ids["basil-epistle-8-evagrius"] = emit_source(
        26, "basil-epistle-8-evagrius", "Generally attributed to Evagrius Ponticus, not Basil "
        "of Caesarea (transmitted under Basil's name)", "Basil's Epistle 8", NPNF208, "v",
        "contested (generally attributed to Evagrius Ponticus, not Basil, though transmitted "
        "under Basil's name -- Doc_02 SS1.1's own attribution-discipline claim)",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "Doc_02 SS1.1's own named case where this world's record must flag authorship at every "
        "use rather than cite silently under Basil's name (row 26). Per the Registry's own "
        "rule, Boundary Status is assessed by what a source speaks for, never by confidence in "
        "an authorship claim about it -- Native regardless of who actually wrote it; the "
        "authorship caution lives here in attribution_status, not in a Boundary exclusion.")
    ids["basil-apollinaris-correspondence"] = emit_source(
        27, "basil-apollinaris-correspondence", "Attributed to Basil of Caesarea and "
        "Apollinaris of Laodicea (contested)", "Basil, the Apollinaris correspondence "
        "(Epistles 361-364)", NPNF208, "v",
        "contested (in antiquity itself, per Doc_02 SS1.1)",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "A further named case of contested correspondence this record must flag rather than "
        "cite silently, alongside row 26 (row 27; Doc_02 SS1.1).")
    ids["maraval-pouchet-basil-death-redating"] = emit_source(
        28, "maraval-pouchet-basil-death-redating", "Pierre Maraval (1988) and Jean-Robert "
        "Pouchet (1992)", "The redating literature for Basil's death year (377, not the "
        "traditional 378/379)",
        "In-copyright modern scholarship, not vendored", "ic", "attributed",
        "C", "named-not-rechecked", "load-bearing", "Dominant Modern Reconstruction", None,
        "Basil's death year 377 (Doc_01 SS1's dependent chronology; Doc_02 SS1.1, SS5 debate "
        "(3), SS9) -- Doc_02's own words call this 'the single most load-bearing uncited "
        "scholarship' in an earlier draft, since this date 'moves a dependent chain, not one "
        "isolated date' (row 28): Basil's episcopal election, his letter sequence, and "
        "Macrina's own death date at Doc_01 SS1 all compute backward from it.")
    ids["cavallin-hubner-zachhuber-epistle-38-reassignment"] = emit_source(
        29, "cavallin-hubner-zachhuber-epistle-38-reassignment", "Anders Cavallin, Reinhard "
        "Hubner, and Johannes Zachhuber", "Scholarship arguing Epistle 38's reassignment from "
        "Basil to Gregory of Nyssa", "In-copyright modern scholarship, not vendored", "ic",
        "attributed", "C", "named-not-rechecked", "corroborating", "Contested", None,
        "Grounds row 23's Ep. 38 authorship question (row 29). The template's C tier ('tied to "
        "a real author/work') is satisfied by the named authors even without a specific work "
        "title.")
    ids["rudberg-basil-letter-collection-manuscripts"] = emit_source(
        30, "rudberg-basil-letter-collection-manuscripts", "S. Y. Rudberg",
        "Scholarship on the manuscript families and growth of Basil's letter collection",
        "In-copyright modern scholarship, not vendored", "ic", "attributed",
        "C", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "Grounds row 5's own transmission-history claim, alongside Fedwick (row 102), for the "
        "letter collection's studied, not-fully-recoverable curation history (row 30; Doc_02 "
        "SS1.1).")

    # --- Part B: Gregory of Nazianzus (Registry rows 31-40) -----------------
    ids["gregory-nazianzus-orations-general-corpus"] = emit_source(
        31, "gregory-nazianzus-orations-general-corpus", "Gregory of Nazianzus (c. 329/30-c. 390)",
        "Gregory of Nazianzus, Orations (general corpus; among ~245 letters, covers only "
        "Epp. 101, 102, 202)", NPNF207, "v", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "Grounds the Trinitarian-confession gravity (the five Theological Orations) and the "
        "stillness-vs-office pull gravity candidate (Oration 2, next-but-three record) (row "
        "31). Coverage gap named: the Sasima letters, Ep. 58, and Ep. 197 are gaps within this "
        "same acquisition (rows 39, 40), not separately acquirable this session.")
    ids["gregory-nazianzus-oration-14-love-of-poor"] = emit_source(
        32, "gregory-nazianzus-oration-14-love-of-poor", "Gregory of Nazianzus",
        "Gregory of Nazianzus, Oration 14, On the Love of the Poor", NPNF207, "v", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "The poor-institutionalized gravity candidate (row 32). Named specifically (bolded) by "
        "Doc_02 SS1.2 alongside the Theological Orations, the funeral orations, and Oration 2 "
        "-- given its own record rather than folded silently into the general corpus.")
    ids["gregory-nazianzus-invectives-against-julian"] = emit_source(
        33, "gregory-nazianzus-invectives-against-julian", "Gregory of Nazianzus",
        "Gregory of Nazianzus, Orations 4 and 5 (First and Second Invectives Against Julian)",
        "King's 1888 translation, transcribed by Roger Pearse, vendored as "
        "cic/texts/gregory-nazianzen_first-invective-against-julian_king1888.txt and "
        "cic/texts/gregory-nazianzen_second-invective-against-julian_king1888.txt", "vv",
        "attributed", "A", "verified-direct", "load-bearing", "Documented", None,
        "Julian's persecution of this world (Doc_01 SS4); the old-religion-pressing-on-this-"
        "world material (row 33). Not covered by the vendored npnf207 edition, per Doc_02 "
        "SS1.2's own note -- these two files close that specific gap. Both orations confirmed "
        "complete this session against King's 1888 translation.")
    ids["gregory-nazianzus-oration-43-funeral-encomium-basil"] = emit_source(
        34, "gregory-nazianzus-oration-43-funeral-encomium-basil", "Gregory of Nazianzus",
        "Gregory of Nazianzus, Oration 43 (funeral encomium on Basil, c. 381/2)", NPNF207, "v",
        "attributed", "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "Doc_02 SS8 Tier 1: the Valens/Modestus confrontation, the Epiphany liturgy of 372, "
        "Basil's death and funeral (incl. the funeral-crowd claim of Jews and pagans present, "
        "PENDING CONFIRMATION against the acquired text), the famine leadership narrative, the "
        "poorhouse complex ('the new city') (row 34). Genre caution carried forward: Tier 1 as "
        "Gregory's public telling within living memory of eyewitnesses, simultaneously "
        "genre-shaped encomium with a friendship to repair posthumously (Doc_02 SS3).")
    ids["gregory-nazianzus-oration-2-flight-from-ordination"] = emit_source(
        35, "gregory-nazianzus-oration-2-flight-from-ordination", "Gregory of Nazianzus",
        "Gregory of Nazianzus, Oration 2 (apology for his flight from ordination)", NPNF207,
        "v", "attributed", "B", "verified-via-authority", "load-bearing", "Widely Accepted",
        None, "The stillness-vs-office pull gravity candidate (row 35).")
    ids["gregory-nazianzus-de-vita-sua"] = emit_source(
        36, "gregory-nazianzus-de-vita-sua", "Gregory of Nazianzus",
        "Gregory of Nazianzus, De vita sua and the autobiographical poems", NPNF207, "v",
        "attributed", "B", "named-not-rechecked", "load-bearing", "Widely Accepted",
        "McLynn's and Elm's self-fashioning caution (Doc_02 SS1.2, SS5 debate 6) applies at "
        "full strength: Nazianzen's self-account of Constantinople 379-381 is a retrospective "
        "literary construction of a man justifying his own life, not a transcript.",
        "Doc_02 SS8 Tier 1: Constantinople 379-381 (the Anastasia chapel, the Easter violence, "
        "the Theological Orations, the resignation) (row 36). Poetic-corpus coverage not "
        "independently confirmed line-by-line this session.")
    ids["gregory-nazianzus-will-manumission"] = emit_source(
        37, "gregory-nazianzus-will-manumission", "Gregory of Nazianzus",
        "Gregory of Nazianzus' will (manumits slaves he owned)",
        "Cited at work level per Doc_02 SS1.2/SS6.3; no specific vendored edition independently "
        "matched this session", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted",
        "Doc_02 SS1.2 treats the will's existence as Documented; this record's own citation is "
        "at work level only, with no specific edition independently re-checked this session -- "
        "carried at Widely Accepted, the sourcing gap named rather than silently upgraded.",
        "SS6.3's against-the-grain evidence on the enslaved (row 37). Its details, including "
        "the manumission, are cited at work level only.")
    ids["gregory-nazianzus-funeral-orations-caesarius-gorgonia-elder-gregory"] = emit_source(
        38, "gregory-nazianzus-funeral-orations-caesarius-gorgonia-elder-gregory",
        "Gregory of Nazianzus", "Gregory of Nazianzus, the funeral orations on Caesarius, "
        "Gorgonia, and the elder Gregory", NPNF207, "v", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "The household-formation-lineage gravity candidate; Gorgonia as one of patristic "
        "literature's few extended married-laywoman portraits; the elder Gregory's former "
        "Hypsistarian sect (SS6.8) (row 38). Doc_02 SS3 flags Tier 3 idealization on Tier 1 "
        "family fact throughout.")
    ids["gregory-nazianzus-epistle-197-theosebia"] = emit_source(
        39, "gregory-nazianzus-epistle-197-theosebia", "Gregory of Nazianzus",
        "Gregory of Nazianzus, Epistle 197 (consolation to Gregory of Nyssa, honoring "
        "Theosebia)", "Not within the vendored npnf207 edition (which covers only Epp. 101, "
        "102, 202) -- a named, currently unlocated acquisition gap", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Inferential-Thin", None,
        "SS6.1's Theosebia datum (row 39). Doc_02 SS6 itself cautions this praise is "
        "corroboration from within the same friendship network the world's whole record leans "
        "on, not independent of it in the stronger sense the word might suggest; whether "
        "Theosebia was Nyssen's wife or his sister is itself disputed.")
    ids["gregory-nazianzus-sasima-letters"] = emit_source(
        40, "gregory-nazianzus-sasima-letters", "Gregory of Nazianzus",
        "Gregory of Nazianzus, the Sasima letters (48-50) and Epistle 58",
        "Not within the vendored npnf207 edition -- a named, currently unfilled acquisition "
        "gap", "na", "attributed", "B", "named-not-rechecked", "corroborating", "Inferential-Thin",
        None,
        "The Sasima-affair Tier 1 story candidate (Doc_02 SS8) (row 40). Doc_02 SS8's Sasima "
        "story tier currently rests on Nazianzen's Orations and De vita sua (rows 31, 36), not "
        "on these specific letters -- a real, currently unfilled gap, not silently assumed "
        "covered.")

    # --- Part B: Gregory of Nyssa (Registry rows 41-56) ----------------------
    ids["gregory-nyssa-general-dogmatic-ascetic-corpus"] = emit_source(
        41, "gregory-nyssa-general-dogmatic-ascetic-corpus", "Gregory of Nyssa (c. 335-after "
        "394)", "Gregory of Nyssa, general dogmatic/ascetic corpus", NPNF205, "v", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "The Trinitarian-confession gravity candidate; multiple lexicon and story-tier "
        "candidates named below (row 41). Confirmed-absent list carried forward per the G1 "
        "manifest's own audit: does NOT include Ad Graecos (row 54), the Life of Macrina (row "
        "48), the Song of Songs/Ecclesiastes/Beatitudes/Lord's Prayer homilies (row 52), or the "
        "Forty Martyrs/Theodore the Recruit homilies (row 53) -- separate records below where "
        "acquired, named gaps where not.")
    ids["gregory-nyssa-against-eunomius"] = emit_source(
        42, "gregory-nyssa-against-eunomius", "Gregory of Nyssa",
        "Gregory of Nyssa, Against Eunomius (continuing his dead brother Basil's fight)",
        NPNF205, "v", "attributed", "B", "verified-via-authority", "load-bearing",
        "Widely Accepted", None,
        "The Trinitarian-confession gravity candidate's Eunomian-contest question (Doc_01 SS1) "
        "(row 42). Citation-format trap carried forward: the acquired edition's 'Book II' is in "
        "fact the separate Refutation of Eunomius' Confession under a pre-Jaeger book division "
        "-- flag at every use.")
    ids["gregory-nyssa-on-the-holy-spirit"] = emit_source(
        43, "gregory-nyssa-on-the-holy-spirit", "Gregory of Nyssa",
        "Gregory of Nyssa, On the Holy Spirit and the sermons on the Deity of the Son and "
        "Spirit", NPNF205, "v", "attributed", "B", "verified-via-authority", "load-bearing",
        "Widely Accepted", None,
        "The doxology/Trinitarian-confession gravity candidates (row 43). The "
        "popularly-circulated 'money-changers and bath-attendants' line is Doc_02's own "
        "flagged paraphrase, not a verified direct quotation -- carry that caution forward at "
        "every use.")
    ids["gregory-nyssa-ad-ablabium"] = emit_source(
        44, "gregory-nyssa-ad-ablabium", "Gregory of Nyssa",
        "Gregory of Nyssa, Ad Ablabium (On Not Three Gods)", NPNF205, "v", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "SS5 debate (1): the social-trinitarian misreading question, with Ayres' 'On Not Three "
        "People' (row 105, in Coakley's edited volume row 112) as the actual argument against "
        "that misreading (row 44).")
    ids["gregory-nyssa-ad-eustathium"] = emit_source(
        45, "gregory-nyssa-ad-eustathium", "Gregory of Nyssa",
        "Gregory of Nyssa, Ad Eustathium (On the Holy Trinity)", NPNF205, "v", "attributed",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "The same social-trinitarian question as the previous record (row 45).")
    ids["gregory-nyssa-catechetical-oration"] = emit_source(
        46, "gregory-nyssa-catechetical-oration", "Gregory of Nyssa",
        "Gregory of Nyssa, Catechetical Oration", NPNF205, "v", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "This world's most systematic catechesis -- the household->catechesis->baptism "
        "formation-ecology pattern (Doc_01 SS1) (row 46).")
    ids["gregory-nyssa-on-the-making-of-man"] = emit_source(
        47, "gregory-nyssa-on-the-making-of-man", "Gregory of Nyssa",
        "Gregory of Nyssa, On the Making of Man", NPNF205, "v", "attributed",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "Completes Basil's Hexaemeron (row 15) -- family-continuation evidence for the "
        "survivorship-pattern finding (Doc_02 SS7) (row 47).")
    ids["gregory-nyssa-life-of-macrina"] = emit_source(
        48, "gregory-nyssa-life-of-macrina", "Gregory of Nyssa",
        "Gregory of Nyssa, the Life of St. Macrina",
        "Clarke's 1916 translation, vendored as "
        "cic/texts/gregory-nyssa_life-of-macrina_clarke1916.txt (superseding an earlier "
        "introduction-only upload, cic/texts/gregory-nyssa_life-of-macrina-introduction-only_"
        "clarke1916.txt, kept per the Registry's own no-deletion practice, redundant with this "
        "row)", "vv", "attributed", "A", "verified-direct", "load-bearing", "Widely Accepted",
        "Verified-direct here confirms the TEXT is complete, not that its content is "
        "Documented history: Gregory of Nyssa's deliberate Socratic-Platonic literary framing "
        "(Macrina as Diotima/Socrates at the deathbed) runs throughout (Doc_02 SS1.3-1.4). Per "
        "Doc_02 SS1.4's own words, Macrina's historical leadership of the Annisa community is "
        "Widely Accepted; her own words are not recoverable as hers -- carried at Widely "
        "Accepted rather than upgraded to Documented on the strength of this session's textual "
        "verification alone.",
        "This world's entire primary-text basis for Macrina (SS1.4); the Macrina-deathbed/"
        "funeral Tier 1 story candidate (SS8); SS5 debate (2), Macrina's recoverability; SS6.3's "
        "freed-maidservant evidence; the Naucratius-death and Macrina's-refusal-of-remarriage "
        "Tier 3 story candidates (row 48). Confirmed complete this session (introduction "
        "through Macrina's death, funeral -- Bishop Araxius presiding -- and the volume's own "
        "colophon).")
    ids["gregory-nyssa-on-the-soul-and-resurrection"] = emit_source(
        49, "gregory-nyssa-on-the-soul-and-resurrection", "Gregory of Nyssa",
        "Gregory of Nyssa, On the Soul and Resurrection", NPNF205, "v", "attributed",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "The world's consolation-culture evidence (Doc_02 SS3) (row 49). Genre: Christian "
        "Phaedo, staged at the same deathbed as the Vita -- used as evidence of how this circle "
        "wanted grief and hope held, not as a transcript.")
    ids["gregory-nyssa-on-virginity"] = emit_source(
        50, "gregory-nyssa-on-virginity", "Gregory of Nyssa",
        "Gregory of Nyssa, On Virginity", NPNF205, "v", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "The ascetic-communal-movement gravity candidate (row 50).")
    ids["gregory-nyssa-life-of-gregory-thaumaturgus"] = emit_source(
        51, "gregory-nyssa-life-of-gregory-thaumaturgus", "Gregory of Nyssa",
        "Gregory of Nyssa, the Life of Gregory Thaumaturgus", NPNF205, "v", "attributed",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "The Thaumaturgus-cycle Tier 3 story candidate (SS8); the third-century "
        "founding-memory initiating force (row 51). Hagiography at a century's distance -- "
        "genre-flagged throughout per Doc_02 SS3.")
    ids["gregory-nyssa-song-of-songs-ecclesiastes-beatitudes-homilies"] = emit_source(
        52, "gregory-nyssa-song-of-songs-ecclesiastes-beatitudes-homilies", "Gregory of Nyssa",
        "Gregory of Nyssa, homilies on the Song of Songs, Ecclesiastes (incl. the fourth "
        "homily's anti-slaveholding argument), the Beatitudes, and the Lord's Prayer",
        "Confirmed absent from the vendored npnf205 per row 41's own note (the G1 manifest "
        "audit specifically flagged these homilies as excluded) -- a named, currently "
        "unlocated acquisition gap", "na", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "SS6.3's central anti-slavery evidence -- 'antiquity's sharpest surviving protest "
        "against slavery itself' (row 52). The 'who can buy the image of God?' line is Doc_02's "
        "own flagged paraphrase of the argument's thrust, not a verified direct quotation of "
        "the (unacquired) Greek -- carry that caution forward at every use until a checked "
        "translation is in hand.")
    ids["gregory-nyssa-forty-martyrs-theodore-recruit-homilies"] = emit_source(
        53, "gregory-nyssa-forty-martyrs-theodore-recruit-homilies", "Gregory of Nyssa",
        "Gregory of Nyssa's homilies on the Forty Martyrs of Sebaste and on Theodore the "
        "Recruit", "Confirmed absent from the vendored npnf205 per row 41's own note -- a "
        "named, currently unlocated acquisition gap", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The martyrs'-festival gravity candidate; the Forty Martyrs Tier 2 story candidate "
        "(Doc_02 SS8), alongside Basil's own homilies on the Forty (row 20) (row 53).")
    ids["gregory-nyssa-ad-graecos"] = emit_source(
        54, "gregory-nyssa-ad-graecos", "Gregory of Nyssa",
        "Gregory of Nyssa, Ad Graecos ex communibus notionibus",
        "Confirmed absent from the vendored npnf205 per row 41's own note; Doc_02 SS1.3's own "
        "correction states plainly it 'remains ungrounded and belongs in the manifest's gap "
        "list'", "na", "attributed", "B", "named-not-rechecked", "illustrative",
        "Inferential-Thin",
        None, "The Trinitarian-confession gravity candidate (row 54). A specific, identifiable "
        "named work, real and traceable, simply unacquired -- this record grounds only the "
        "fact of the work's existence, never its content, which is not in hand.")
    ids["gregory-nyssa-love-of-the-poor-lepers-consolation"] = emit_source(
        55, "gregory-nyssa-love-of-the-poor-lepers-consolation", "Gregory of Nyssa",
        "Gregory of Nyssa, On the Love of the Poor / On the Treatment of Lepers (De pauperibus "
        "amandis I-II), consolation pieces (incl. on infants' early deaths), and On "
        "Pilgrimages", NPNF205, "v", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "The poor-institutionalized gravity candidate (row 55). Letters, incl. On Pilgrimages, "
        "confirmed present per Doc_02 SS1.3's own correction to an earlier manifest error.")
    ids["evagrius-ponticus-cappadocian-formation-fact"] = emit_source(
        56, "evagrius-ponticus-cappadocian-formation-fact",
        "No primary author of his own -- this record grounds a biographical fact about "
        "Evagrius Ponticus (formed and ordained within this circle), not a text he wrote",
        "Evagrius Ponticus' formation and ordination by this circle (the fact, not a corpus -- "
        "no Cappadocian-period text of his own survives)",
        "No edition -- no Cappadocian-period text of Evagrius' own survives; his later, "
        "post-departure corpus is a Named Comparandum belonging to the registered Desert "
        "world (Source Registry row 4), Excluded from this world", "fact",
        "attributed (uncontested biographical fact)",
        "C", "named-not-rechecked", "illustrative", "Widely Accepted", None,
        "Evidence for this world's own formation reach (Doc_01 SS2) (row 56). Type corrected "
        "to S per the Registry's own note -- there is no primary text of his own to be Type P "
        "about.")

    # --- Part B: The opponents (Registry rows 57-63) -------------------------
    ids["eunomius-first-apology"] = emit_source(
        57, "eunomius-first-apology", "Eunomius of Cyzicus",
        "Eunomius, the First Apology",
        "Whiston's 1711 translation, re-edited by Roger Pearse with Vaggione's chapter "
        "numbering, vendored as cic/texts/eunomius_first-apology_whiston1711.txt", "vv",
        "attributed", "A", "verified-direct", "load-bearing", "Documented", None,
        "The Trinitarian-confession gravity's Eunomian-contest question; the rare two-sided "
        "control on Basil/Nyssen's own polemic (Doc_01 SS4) (row 57). Confirmed complete this "
        "session: chapters I-XXVIII (incl. the appended Confession of Faith as ch. XXVIII) and "
        "the full 23-entry footnote set.")
    ids["eunomius-apology-for-the-apology"] = emit_source(
        58, "eunomius-apology-for-the-apology", "Eunomius of Cyzicus",
        "Eunomius, the Apology for the Apology (survives only as quoted inside Gregory of "
        "Nyssa's refutation)",
        "Accessed only via cappadocian.source.gregory-nyssa-against-eunomius (NPNF205) -- "
        "adversarial transmission, no independent text exists to verify against", "v",
        "attributed (Eunomius); transmitted only via hostile quotation -- flag adversarial "
        "transmission at every use",
        "C", "named-not-rechecked", "corroborating", "Widely Accepted",
        "The fragments' origin in Eunomius' own hand is broadly accepted; they reach us "
        "filtered through his opponent's refutation (Doc_02 SS1.5) -- flag adversarial "
        "transmission at every use, never treat Nyssen's framing of them as neutral.",
        "The Eunomian-contest question, row 57's cross-reference (row 58). No independent text "
        "exists to verify against.")
    ids["eunomius-confession-of-383"] = emit_source(
        59, "eunomius-confession-of-383", "Eunomius of Cyzicus",
        "Eunomius, the confession of 383",
        "Not independently located as a vendored text this session; named for completeness per "
        "Doc_02 SS1.5/Doc_01 SS4's mention that it 'survives independently'", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The Eunomian-contest question (row 59). A specific, dated, named document -- existence "
        "uncontroversial, content not in hand this session.")
    ids["gangra-canons"] = emit_source(
        60, "gangra-canons", "The Council of Gangra (collective conciliar acts, anonymous)",
        "The Gangra canons (twenty canons censuring 'those around Eustathius')", NPNF214, "v",
        "attributed to the council collectively; date genuinely Contested across a wide range "
        "(c. 340s-370s, not 'within a decade' as an earlier draft claimed)",
        "B", "named-not-rechecked", "load-bearing", "Contested",
        "Date is genuinely Contested across a wide range (c. 340s-370s) per Doc_01 SS3's own "
        "correction -- if Gangra falls in the 350s rather than the 340s, it censures Eustathius "
        "as Basil's own sitting ascetic mentor during Basil's formative years, not settled "
        "pre-history, a live question for Doc_04's classification of the household-lineage "
        "gravity.",
        "The radical-ascetic fracture line (Doc_01 SS3, fracture line 1); SS6.1's "
        "against-the-grain evidence on radical female ascetics (canons 13, 17); SS6.3's "
        "against-the-grain evidence on the enslaved (canon 3) (row 60). Not independently "
        "re-checked against the specific canon numbers this session; read against the grain "
        "per Doc_02 SS1.5/SS2 -- the era's best evidence for what the radicals actually did.")
    ids["epiphanius-on-eustathius-pneumatomachians"] = emit_source(
        61, "epiphanius-on-eustathius-pneumatomachians", "Epiphanius of Salamis",
        "Epiphanius on Eustathius and the Pneumatomachians",
        "Not independently located as a vendored text this session; a named author, no "
        "specific work title given", "na", "attributed",
        "C", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The pneumatological-rupture fracture line (Doc_01 SS3, fracture line 2) (row 61). A "
        "named author satisfies the template's C tier even without a specific work title.")
    ids["church-historians-socrates-sozomen-theodoret"] = emit_source(
        62, "church-historians-socrates-sozomen-theodoret", "Socrates Scholasticus, Sozomen, "
        "and Theodoret (fifth-century church historians)",
        "The church historians' Ecclesiastical Histories -- secondary narrative sources, never "
        "this world's own voice, all fifth-century, all outside the c. 394 horizon",
        "Socrates and Sozomen vendored as cic/texts/npnf202_socrates-sozomen-ecclesiastical-"
        "histories.xml; Theodoret vendored as cic/texts/npnf203_theodoret-jerome-gennadius-"
        "rufinus.xml", "v", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "Constantinople 360 (via Socrates HE 2.41, SS2); the Homoian-establishment "
        "reconstruction; the Julian-persecution episode (row 62). Files present since "
        "2026-08-15, not re-verified against the specific loci Doc_02 cites this session. "
        "Correction carried forward: the funeral-crowd claim (Jews and pagans mourning Basil) "
        "is Doc_02 SS8's own attribution to Oration 43 (row 34), not to the church historians.")
    ids["photius-epitome-philostorgius"] = emit_source(
        63, "photius-epitome-philostorgius", "Photius of Constantinople (epitomizing "
        "Philostorgius' Ecclesiastical History)",
        "Photius' Epitome of Philostorgius' Ecclesiastical History -- the one surviving "
        "Eunomian narrative frame",
        "Walford's 1855 translation, vendored as "
        "cic/texts/philostorgius_ecclesiastical-history_walford1855.txt", "vv",
        "attributed to Philostorgius, filtered through Photius' own hostile epitome -- carry "
        "that filtering forward at every use",
        "A", "verified-direct", "corroborating", "Widely Accepted",
        "Filtered twice over, through Photius' own hostile epitome of a condemned Eunomian "
        "historian. This session's own direct verification confirms the epitome's "
        "completeness, not the neutrality of what it reports -- carried at Widely Accepted, "
        "not Documented, per Doc_02 SS1.6's own double-filtering caution.",
        "The one surviving Eunomian narrative frame (Doc_02 SS1.6) (row 63). Confirmed complete "
        "this session: all twelve books, the translator's Biographical Notice, and the full "
        "241-entry footnote set.")

    # --- Part B: Other primary voices, work-level (Registry rows 65-76; -----
    # row 64 is Excluded/Named Comparandum, not emitted) ---------------------
    ids["amphilochius-of-iconium-own-works"] = emit_source(
        65, "amphilochius-of-iconium-own-works", "Amphilochius of Iconium",
        "Amphilochius of Iconium's own works (canonical letters, etc.)",
        "No open English edition located this session or previously", "nt", "attributed",
        "C", "named-not-rechecked", "illustrative", "Inferential-Thin", None,
        "Records a real, named person and role (Nazianzen's cousin, addressee of On the Holy "
        "Spirit and the canonical letters, junior circle member) without an accessible text of "
        "his own to verify against (row 65). The Lycaonia/Iconium geographic-scope extension "
        "and the 381 law's Asian-diocese bishop are grounded via OTHER records (row 79, the "
        "church historians), never via this record's own unlocated text.")
    ids["gregory-thaumaturgus-canonical-epistle"] = emit_source(
        66, "gregory-thaumaturgus-canonical-epistle", "Gregory Thaumaturgus (3rd century)",
        "Gregory Thaumaturgus, the Canonical Epistle", ANF06, "v", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The third-century founding-memory initiating force (Doc_01 SS4); the Thaumaturgus "
        "mission (Doc_01 SS1) (row 66). File present since 2026-08-15, not re-verified this "
        "session.")
    ids["gregory-thaumaturgus-address-of-thanksgiving-to-origen"] = emit_source(
        67, "gregory-thaumaturgus-address-of-thanksgiving-to-origen",
        "Traditionally Gregory Thaumaturgus (attribution questioned)",
        "Gregory Thaumaturgus, the Address of Thanksgiving to Origen", ANF06, "v",
        "contested (attribution questioned in recent scholarship, per Doc_02 SS1.6/SS9)",
        "B", "verified-via-authority", "corroborating", "Contested", None,
        "The Origen-via-Caesarea-Maritima transmission channel (Doc_01 SS2) (row 67).")
    ids["gregory-thaumaturgus-creed"] = emit_source(
        68, "gregory-thaumaturgus-creed",
        "Attributed to Gregory Thaumaturgus (authenticity Contested)",
        "The creed attributed to Gregory Thaumaturgus, transmitted only via Gregory of Nyssa's "
        "Life of Gregory Thaumaturgus, a century later",
        "Transmitted solely inside cappadocian.source.gregory-nyssa-life-of-gregory-"
        "thaumaturgus (NPNF205, row 51)", "v",
        "contested (authenticity Contested, per Doc_01 SS1)",
        "B", "verified-via-authority", "contested", "Contested", None,
        "The Thaumaturgus-cycle Tier 3 story candidate (row 68). Carried at the lower "
        "confidence Doc_01 SS1 specifies for the underlying claim (Contested authenticity).")
    ids["firmilian-of-caesarea-epistle-74-75"] = emit_source(
        69, "firmilian-of-caesarea-epistle-74-75", "Firmilian of Caesarea (3rd century)",
        "Firmilian of Caesarea, Epistle 74 (ANF/older numbering) / 75 (modern CSEL/Hartel "
        "numbering), preserved inside Cyprian's own corpus", ANF05, "v", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "Third-century pre-boundary inheritance evidence (Doc_01 SS1) (row 69). File present "
        "since 2026-08-15, not re-verified this session. Cite both numberings per Doc_02 "
        "SS1.6's own instruction.")
    ids["elder-gregory-of-nazianzus-hypsistarian"] = emit_source(
        70, "elder-gregory-of-nazianzus-hypsistarian",
        "No independent author -- attested only within his son Gregory of Nazianzus' funeral "
        "oration",
        "The elder Gregory of Nazianzus' (bishop-father) biography and former Hypsistarian "
        "affiliation, as reported within his son's funeral oration",
        "Within cappadocian.source.gregory-nazianzus-funeral-orations-caesarius-gorgonia-"
        "elder-gregory (NPNF207, row 38) -- no independent text", "v", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "SS6.8's Hypsistarian minority datum (row 70). A window on the region's pre-Nicene "
        "religious mixture.")
    ids["julian-letter-to-the-athenians"] = emit_source(
        71, "julian-letter-to-the-athenians", "Julian (Roman emperor, 'the Apostate')",
        "Julian, the Letter to the Athenians",
        "Wright's 1913 translation, vendored as "
        "cic/texts/julian_letter-to-the-athenians_wright1913.txt", "vv", "attributed",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "Julian's break with the Christian household that raised him (Doc_01 SS4) (row 71). "
        "Confirmed complete this session against its own cited Loeb pagination (pp. 245-293) "
        "and the full 39-entry footnote set.")
    ids["julian-rescript-on-christian-teachers"] = emit_source(
        72, "julian-rescript-on-christian-teachers", "Julian (Roman emperor)",
        "Julian, the Rescript on Christian Teachers (Epistle 36), within Julian's Letters 1-73",
        "Wright's 1923 translation, vendored as "
        "cic/texts/julian_letters-1-73_wright1923.txt", "vv", "attributed",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "Julian's actual measures against this world's own metropolis (Doc_01 SS4); the "
        "school-legislation institutional evidence (SS2) (row 72). Letter 36 confirmed present "
        "and complete this session, in its correct sequence between Letters 35 and 37, with "
        "its own footnotes. The surrounding 72 letters (correspondence with Priscus, Libanius, "
        "Maximus of Ephesus, and others) are a bonus acquisition, not yet individually matched "
        "to Doc_02 claims -- flagged for a future pass.")
    ids["codex-theodosianus-13-3-5-school-law"] = emit_source(
        73, "codex-theodosianus-13-3-5-school-law", "The Roman imperial chancery under Julian "
        "(collective/anonymous legal act)",
        "The general school law of June 362 (Codex Theodosianus 13.3.5)",
        "The Mommsen-Meyer Latin text is public domain per Doc_02 SS2, but not acquired into "
        "cic/texts/ this session", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "Julian's school legislation as external-force evidence (Doc_01 SS4; Doc_02 SS2), "
        "distinguished from row 72's Rescript as two separate measures (row 73). Does not "
        "itself name Christians, per Doc_02 SS2 -- the Rescript (row 72) does the actual "
        "discriminatory work.")
    ids["julians-measures-against-caesarea"] = emit_source(
        74, "julians-measures-against-caesarea", "No named author or text -- attested only via "
        "the general historical record",
        "Julian's direct measures against Caesarea (civic-roll removal, fines, clergy "
        "conscription, church-property seizure)",
        "No specific text or author is named for this claim beyond the general historical "
        "record", "nt", "attributed",
        "D", "unverified", "corroborating", "Widely Accepted",
        "Doc_01 SS4/SS5 states this correction as Documented but does not itself name the "
        "specific source it rests on beyond the general historical record -- no author or text "
        "is named, hence D per the template's own definition. Carried here at Widely Accepted, "
        "the sourcing gap named rather than silently upgraded to Documented on no named basis.",
        "Julian's persecution of this world's own metropolis (Doc_01 SS4) (row 74). An earlier "
        "draft's claim that this traces to Basil's letters (row 5) and the church historians "
        "(row 62) is not directly stated in either Doc_01 or Doc_02 and remains removed rather "
        "than asserted without a named basis -- flagged for a future pass to locate the "
        "specific citation.")
    ids["libanius-paideia-witness"] = emit_source(
        75, "libanius-paideia-witness", "Libanius of Antioch",
        "Libanius' genuine relevance as an external witness to the paideia network, "
        "independent of the disputed Basil correspondence (row 12)",
        "No independently vendored Libanius text; his relevance rests on his general "
        "historical role, per Doc_02 SS1.6", "nt", "attributed",
        "C", "named-not-rechecked", "illustrative", "Widely Accepted", None,
        "The paideia-converted gravity candidate (row 75). A real named figure without a "
        "pinpointed locus. His Monody on Julian (in the same 1888 King volume that supplied "
        "row 33's companion orations) was not supplied and remains an optional further "
        "acquisition.")
    ids["jerome-de-viris-illustribus"] = emit_source(
        76, "jerome-de-viris-illustribus", "Jerome",
        "Jerome, De viris illustribus (392) -- the earliest external catalogue of what "
        "circulated under Basil, both Gregorys, and Amphilochius' names", NPNF203, "v",
        "attributed", "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "SS1.6's earliest external catalogue datum (row 76). File present since 2026-08-15, not "
        "re-verified this session against the specific entries Doc_02 cites. Correction "
        "carried forward: DVI's 'Eustathius' entry is Eustathius of Antioch, not Eustathius of "
        "Sebaste -- do not cite it as covering this world's own Eustathius.")

    # --- Part C: Institutional, Legal, and Liturgical Evidence (rows 77-81) -
    ids["nicaea-325-subscription-lists"] = emit_source(
        77, "nicaea-325-subscription-lists", "The Council of Nicaea (325, collective "
        "conciliar record)", "Nicaea (325), subscription lists",
        "No open edition of the subscription lists themselves located; attested via "
        "secondary literature rather than an acquired primary edition", "na", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "The 325 beginning-boundary decision (Doc_01 SS1) (row 77). Leontius of Caesarea's "
        "subscription is a specific, named, well-attested fact.")
    ids["constantinople-381-and-its-creed"] = emit_source(
        78, "constantinople-381-and-its-creed", "The Council of Constantinople (381, "
        "collective conciliar record)", "Constantinople 381 and its creed", NPNF214, "v",
        "attributed", "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "The 381 ecological-break gravity dissolution (Doc_01 SS4a) (row 78). File present "
        "since 2026-08-15, not re-verified this session.")
    ids["imperial-communion-law-of-381"] = emit_source(
        79, "imperial-communion-law-of-381", "The Roman imperial chancery under Theodosius I "
        "(collective/anonymous legal act)",
        "The imperial communion law of 381 (Codex Theodosianus 16.1.3, 30 July 381), naming "
        "Helladius, Otreius, Gregory of Nyssa, and Amphilochius",
        "The Pharr 1952 English translation is copyrighted and excluded (row 80); the "
        "Mommsen-Meyer Latin text is public domain but not acquired into cic/texts/ this "
        "session", "na", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "The 381 ecological break's authority-change evidence (Doc_01 SS4a) (row 79). The "
        "specific bishops it names are independently well attested via Van Dam (row 95) and "
        "the general secondary literature named in Part F, not resting solely on this "
        "unacquired primary text.")
    ids["pharr-theodosian-code-translation"] = emit_source(
        80, "pharr-theodosian-code-translation", "Clyde Pharr (translator)",
        "The Theodosian Code (1952) -- the full English translation",
        "In-copyright, 1952 translation, not vendored", "ic", "attributed",
        "B", "named-not-rechecked", "illustrative", "Widely Accepted", None,
        "Would ground rows 73 and 79 directly if acquired (row 80). A specific named "
        "translator, title, and year -- the same relationship row 24 (DelCogliano & "
        "Radde-Gallwitz) bears to Against Eunomius.")
    ids["origen-philocalia"] = emit_source(
        81, "origen-philocalia", "Origen (anthologized text); traditionally compiled by Basil "
        "of Caesarea and Gregory of Nazianzus",
        "The Philocalia, the Origen anthology traditionally compiled by Basil and Nazianzen",
        "Lewis' 1911 translation, vendored (for the Alexandria world, 2026-08-21) as "
        "cic/texts/origen_philocalia_lewis1911.txt", "v",
        "contested (the traditional Basil-Nazianzen compiling attribution is now Contested in "
        "the scholarship)",
        "B", "named-not-rechecked", "contested", "Contested", None,
        "SS5 debate (5): the Philocalia's own attribution; SS5 debate (9)'s Origenism-"
        "transmission question; the Origen-via-Caesarea-Maritima transmission channel (Doc_01 "
        "SS2) (row 81). Boundary is Native despite the anthology's contents being Origen's own "
        "writing: what this world's own record actually claims is the compiling act -- two of "
        "this world's own authors, at Caesarea Maritima, selecting and transmitting Origen's "
        "passages -- distinct from citing Origen's underlying works as this world's own voice.")

    # --- Part D: Formation Narrative Sources beyond Part B (rows 82-83) -----
    ids["gregory-nyssa-in-xl-martyres-ii"] = emit_source(
        82, "gregory-nyssa-in-xl-martyres-ii", "Gregory of Nyssa",
        "Gregory of Nyssa, In XL Martyres II (Emmelia's role in acquiring and enshrining the "
        "Forty Martyrs' relics at the Annisa estate shrine)",
        "Confirmed absent from the vendored npnf205 -- independently confirmed by a direct "
        "text search of cic/texts/npnf205_gregory-nyssa-dogmatic-treatises.txt (zero "
        "occurrences of 'Forty Martyrs' or 'XL Martyres')", "na", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "SS6.1's against-the-grain evidence of a woman's formation-agency; the Annisa "
        "estate-shrine material-culture record (row 113) (row 82). A specific named work, "
        "grouped with row 53 rather than duplicating it as a separate acquisition target -- an "
        "earlier draft wrongly claimed this text was within the vendored npnf205, directly "
        "contradicted by row 41's and row 53's own notes and by this direct search.")
    ids["eupsychius-of-caesareas-feast"] = emit_source(
        83, "eupsychius-of-caesareas-feast", "Basil of Caesarea (attests the feast; no "
        "dedicated homily by anyone is attested)",
        "Eupsychius of Caesarea's martyrdom (362) and its annual 7 September feast at Caesarea "
        "-- attested via invitations in Basil's letters; no In Eupsychium homily is attested by "
        "anyone", NPNF208, "v", "attributed",
        "C", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "Eupsychius' martyrdom and its annual feast, Doc_02 SS8's newly-added Tier 1 story "
        "candidate -- and this world's own corrected self-description (row 83). Correction "
        "carried forward at full strength: an earlier Registry draft named this row 'homilies "
        "on Eupsychius' feast' by Basil and Gregory of Nyssa -- Doc_02 SS3 is explicit that no "
        "In Eupsychium homily is attested by anyone (unlike the Forty, Gordius, Julitta, and "
        "Mamas homilies at row 20); only the feast itself is Documented. The martyrdom's "
        "narrative content, absent a homily, would most likely come from Sozomen HE 5.11 (row "
        "62), an external source, never from an in-world preached source.")

    # --- Part E: Material Culture and Daily Life Sources (rows 84-88) -------
    ids["martyrium-shrine-panegyris-pattern"] = emit_source(
        84, "martyrium-shrine-panegyris-pattern",
        "No single named author -- a general regional pattern attested collectively across "
        "multiple homilies",
        "The martyrium/shrine panegyris pattern of rural Anatolia (feast-day festivals "
        "combining liturgy, market, and crowd) -- text-attested, not excavated",
        "Attested collectively via the homilies naming festival crowds (rows 16, 20, 53, and "
        "115); no independent material-culture edition of its own", "nt", "attributed",
        "D", "unverified", "corroborating", "Inferential-Thin", None,
        "The martyrs'-festival gravity candidate (row 84). General regional pattern, no single "
        "author or text named for the pattern itself.")
    ids["caesareas-poorhouse-hospital-complex"] = emit_source(
        85, "caesareas-poorhouse-hospital-complex", "No single named author -- an institution "
        "attested via Basil's letters and Nazianzen's Oration 43",
        "Caesarea's suburban poorhouse-hospital complex (Documented as an institution; "
        "physical remains not securely identified)",
        "Attested via cappadocian.source.basil-letters-general-corpus (NPNF208, row 5) and "
        "cappadocian.source.gregory-nazianzus-oration-43-funeral-encomium-basil (NPNF207, row "
        "34)", "v", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "The poor-institutionalized gravity candidate (row 85). Doc_02 SS2's own correction: do "
        "not call it 'the Basileias,' a later name (Sozomen), not this world's own word.")
    ids["imperial-road-frontier-context"] = emit_source(
        86, "imperial-road-frontier-context",
        "No single named author -- general regional/imperial history",
        "The imperial road-and-frontier context (Armenian frontier military traffic)",
        "General regional history, no specific text acquired or identified", "nt", "attributed",
        "D", "unverified", "illustrative", "Widely Accepted", None,
        "The larger-world-embedding orientation (Doc_01 SS4) (row 86). Parallel to row 87's own "
        "explicit ruling: standard, uncontested regional history is Widely Accepted on its own "
        "terms, whether or not a citable primary source exists for it.")
    ids["cappadocia-regional-social-economic-profile"] = emit_source(
        87, "cappadocia-regional-social-economic-profile",
        "No single named primary author -- rests substantially on modern secondary "
        "scholarship (Van Dam, Mitchell) that the manifest correctly excludes as copyrighted",
        "Cappadocia's regional social-economic profile (great-estate agriculture, the "
        "slave-exporting-region byword, the honor-economy, curial flight)",
        "No primary-source registry row can ever ground this specific paragraph, per Doc_02 "
        "SS4's own honest statement -- the grounding is Part F's secondary scholarship (rows "
        "95, 99), correctly excluded from cic/texts/ as copyrighted", "ic", "attributed",
        "C", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The larger-world-embedding orientation (Doc_01 SS4); the region-as-slave-exporting-"
        "economy claim in SS6.3 (row 87). Carried EXACTLY as Doc_02 SS4/SS9 itself states it: "
        "'Widely Accepted, flagged registry-support-pending' -- a claim about the state of "
        "scholarship, not about thin evidence; what is missing is a citable primary source, a "
        "sourcing/rights question, not an epistemic downgrade. The project-lead decision Doc_02 "
        "names (whether such background counts as citable-but-not-quotable, or must be "
        "downgraded) remains open, not resolved by this record.")
    ids["julians-general-hellenic-reclamation-project"] = emit_source(
        88, "julians-general-hellenic-reclamation-project", "Julian (Roman emperor)",
        "Julian's own general project of reclaiming Greek learning for the old gods (as "
        "distinct from row 73's specific school law and row 72's specific Rescript)",
        "General characterization drawn from Julian's own corpus (rows 71-72) and the "
        "secondary literature, not a separately citable primary text of its own", "nt",
        "attributed", "D", "unverified", "illustrative", "Widely Accepted", None,
        "The paideia-converted gravity candidate's own contested pressure (Doc_01 SS4) (row "
        "88).")

    # --- Part F: Secondary Scholarship (rows 89-112) -------------------------
    # All Native (subject is this world's own material, per the template's own
    # rule); none vendored (in-copyright modern scholarship, correctly
    # excluded from cic/texts/ by the manifest -- a rights question, not a
    # Boundary one). All Registry Confidence C -> named-not-rechecked.
    def scholarship(num, slug, author, work, weight, formation, licensed_for):
        return emit_source(
            num, slug, author, work, "In-copyright modern scholarship, not vendored", "ic",
            "attributed", "C", "named-not-rechecked", weight, formation, None, licensed_for)

    ids["rousseau-basil-of-caesarea"] = scholarship(
        89, "rousseau-basil-of-caesarea", "Philip Rousseau", "Basil of Caesarea",
        "corroborating", "Widely Accepted",
        "The de-idealized reading of Basil throughout Doc_02 SS1.1 (row 89).")
    ids["mcguckin-gregory-of-nazianzus-biography"] = scholarship(
        90, "mcguckin-gregory-of-nazianzus-biography", "John McGuckin",
        "St Gregory of Nazianzus: An Intellectual Biography", "corroborating", "Contested",
        "The sympathetic Nazianzen reconstruction, SS5 debate (6) -- generally treats "
        "Nazianzen's self-presentation as recoverable history rather than a caution against it "
        "(row 90).")
    ids["mclynn-gregory-nazianzens-basil"] = scholarship(
        91, "mclynn-gregory-nazianzens-basil", "Neil McLynn",
        "'Gregory Nazianzen's Basil: The Literary Construction of a Christian Friendship'",
        "corroborating", "Contested",
        "The self-fashioning/self-reporting caution on Nazianzen, SS1.2/SS5 debate (6) -- the "
        "position an earlier draft wrongly attributed to McGuckin instead (row 91).")
    ids["silvas-asketikon-and-macrina-the-younger"] = scholarship(
        92, "silvas-asketikon-and-macrina-the-younger", "Anna Silvas",
        "The Asketikon of St Basil the Great; Macrina the Younger", "corroborating", "Contested",
        "The Asketikon's textual history (rows 18-19); the maximal-Macrina reading, SS5 debate "
        "(2) (row 92). Two specific named works.")
    ids["elm-virgins-of-god-sons-of-hellenism"] = scholarship(
        93, "elm-virgins-of-god-sons-of-hellenism", "Susanna Elm",
        "Virgins of God; Sons of Hellenism", "corroborating", "Widely Accepted",
        "The ascetic movement's female/radical breadth pre-Basilian-ordering; the Nazianzen-"
        "Julian paideia contest (row 93). Two specific named works.")
    ids["clark-the-lady-vanishes"] = scholarship(
        94, "clark-the-lady-vanishes", "Elizabeth A. Clark",
        "'The Lady Vanishes,' Church History 67 (1998)", "corroborating", "Contested",
        "The skeptical position on Macrina's recoverability, SS5 debate (2) (row 94).")
    ids["van-dam-cappadocia-trilogy"] = scholarship(
        95, "van-dam-cappadocia-trilogy", "Raymond Van Dam",
        "The Cappadocia trilogy (Kingdom of Snow; Families and Friends; Becoming Christian)",
        "load-bearing", "Widely Accepted",
        "Region, family, and friendship as this world's real machinery; the SS4 social-economic "
        "background (row 87); the 381 communion law's bishops (row 79) (row 95). Three "
        "specific named works.")
    ids["sterk-renouncing-the-world"] = scholarship(
        96, "sterk-renouncing-the-world", "Andrea Sterk",
        "Renouncing the World Yet Leading the Church", "load-bearing",
        "Dominant Modern Reconstruction",
        "The monk-bishop-model synthesis, Doc_02 SS9's own explicit 'Dominant Modern "
        "Reconstruction' entry (row 96).")
    ids["holman-the-hungry-are-dying"] = scholarship(
        97, "holman-the-hungry-are-dying", "Susan Holman", "The Hungry Are Dying",
        "load-bearing", "Dominant Modern Reconstruction",
        "The poverty homilies and poorhouse complex in civic context, Doc_02 SS9's own explicit "
        "'Dominant Modern Reconstruction' entry (row 97).")
    ids["brown-poverty-and-leadership"] = scholarship(
        98, "brown-poverty-and-leadership", "Peter Brown",
        "Poverty and Leadership in the Later Roman Empire (2002)", "corroborating",
        "Widely Accepted",
        "Same territory as Holman (row 97) (row 98). Doc_02 SS5 corrects an earlier citation of "
        "Brown's Through the Eye of a Needle (a Latin-West, 350-550 study) to this directly "
        "relevant title.")
    ids["mitchell-anatolia"] = scholarship(
        99, "mitchell-anatolia", "Stephen Mitchell", "Anatolia", "corroborating",
        "Widely Accepted",
        "The regional social-economic claims, alongside Van Dam (row 95); the SS4 background "
        "(row 87) (row 99).")
    ids["gribomont-asketikon-textual-history"] = scholarship(
        100, "gribomont-asketikon-textual-history", "Jean Gribomont",
        "The Asketikon's textual history; Basil's debt to Eustathius", "load-bearing",
        "Widely Accepted",
        "The Small Asketikon's priority (row 19); SS5 debate (4) (row 100). Named author, cited "
        "for his textual-critical work; no single work title given in either Doc_01 or Doc_02, "
        "not independently re-checked this session -- his finding on the Small Asketikon's "
        "priority is itself 'load-bearing... not a footnote' per Doc_02's own words.")
    ids["drecoll-basil-trinitarian-development"] = scholarship(
        101, "drecoll-basil-trinitarian-development", "Volker Drecoll",
        "Standard scholarship on Basil's trinitarian development", "corroborating", "Contested",
        "The Ep. 38 authorship question, row 23 -- Drecoll's own position leans toward Hubner's "
        "reassignment (row 101).")
    ids["fedwick-bibliotheca-basiliana-universalis"] = scholarship(
        102, "fedwick-bibliotheca-basiliana-universalis", "Paul Fedwick",
        "Bibliotheca Basiliana Universalis", "corroborating", "Widely Accepted",
        "Basil's manuscript transmission, SS1.1, alongside Rudberg (row 30) (row 102).")
    ids["caner-wandering-begging-monks"] = scholarship(
        103, "caner-wandering-begging-monks", "Daniel Caner", "Wandering, Begging Monks",
        "corroborating", "Contested",
        "The radical-ascetic background, SS5 debate (8), the coherence of 'Messalianism' as a "
        "movement (row 103).")
    ids["stewart-working-the-earth-of-the-heart"] = scholarship(
        104, "stewart-working-the-earth-of-the-heart", "Columba Stewart",
        "'Working the Earth of the Heart'", "corroborating", "Contested",
        "Messalianism specifically, SS5 debate (8) -- previously credited to Caner alone (row "
        "104).")
    ids["ayres-nicaea-and-its-legacy"] = scholarship(
        105, "ayres-nicaea-and-its-legacy", "Lewis Ayres",
        "Nicaea and Its Legacy; 'On Not Three People' (in Coakley, ed., row 112)",
        "load-bearing", "Contested",
        "The anti-de-Regnon case, SS5 debate (1); the direct argument against the "
        "social-trinitarian misreading of Ad Ablabium (row 44) (row 105).")
    ids["behr-the-nicene-faith"] = scholarship(
        106, "behr-the-nicene-faith", "John Behr", "The Nicene Faith", "corroborating",
        "Contested", "SS5 debate (1) -- a distinct, substantially exegetical-soteriological "
        "project, not merged with Ayres (row 106).")
    ids["barnes-cappadocian-settlement-scholarship"] = scholarship(
        107, "barnes-cappadocian-settlement-scholarship", "Michel Rene Barnes",
        "Scholarship dismantling the older 'Cappadocian settlement' textbook narrative",
        "corroborating", "Contested",
        "SS5 debate (1), alongside Ayres and Behr, not folded into them (row 107).")
    ids["anatolios-retrieving-nicaea"] = scholarship(
        108, "anatolios-retrieving-nicaea", "Khaled Anatolios", "Retrieving Nicaea",
        "corroborating", "Contested", "The pro-Nicene reconstruction, SS5 debate (1) (row 108).")
    ids["daley-gregory-of-nazianzus"] = scholarship(
        109, "daley-gregory-of-nazianzus", "Brian Daley", "Gregory of Nazianzus",
        "illustrative", "Widely Accepted", "Nazianzen studies generally (row 109).")
    ids["beeley-nazianzens-trinitarian-theology"] = scholarship(
        110, "beeley-nazianzens-trinitarian-theology", "Christopher Beeley",
        "A major recent monograph on Nazianzen's Trinitarian theology", "corroborating",
        "Contested", "SS5 debate (1), the 'Cappadocian settlement' debate (row 110).")
    ids["ludlow-nyssens-modern-reception"] = scholarship(
        111, "ludlow-nyssens-modern-reception", "Morwenna Ludlow",
        "Scholarship on Gregory of Nyssa's modern reception", "illustrative", "Widely Accepted",
        "Nyssen's modern reception as a named risk (reading 20th-century Nyssen back into the "
        "4th century) (row 111).")
    ids["coakley-rethinking-gregory-of-nyssa"] = scholarship(
        112, "coakley-rethinking-gregory-of-nyssa", "Sarah Coakley, ed.",
        "Re-thinking Gregory of Nyssa (2003, an edited volume)", "corroborating", "Contested",
        "The framing introduction to the Ad Ablabium debate, SS5 debate (1) -- the volume's own "
        "introduction frames the case; Ayres' essay within it (row 105) makes the actual "
        "argument (row 112).")

    # --- Part G: Additions from the second review round (rows 113-115; -----
    # row 116 is Excluded/Out-of-Boundary, not emitted) ----------------------
    ids["annisa-estate-shrine"] = emit_source(
        113, "annisa-estate-shrine",
        "No independent author -- attested via Gregory of Nyssa's Life of St. Macrina",
        "The family estate-shrine at Annisa (Vita Macrinae's own description -- "
        "text-attested archaeology, not excavated certainty)",
        "Within cappadocian.source.gregory-nyssa-life-of-macrina (row 48, verified-direct "
        "this session)", "vv", "attributed",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "Row 82's In XL Martyres II citation; the poor/formation-ecology gravity candidates "
        "(row 113). A specific, locatable textual attestation, not an independent "
        "material-culture source of its own.")
    ids["gregory-nazianzus-oration-on-baptism"] = emit_source(
        114, "gregory-nazianzus-oration-on-baptism", "Gregory of Nazianzus",
        "Gregory of Nazianzus' oration on baptism (likely Oration 40)", NPNF207, "v",
        "attributed", "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The baptismal-culture liturgical evidence (Doc_02 SS2), alongside Basil's own "
        "baptismal protreptic (row 17) (row 114). Named specifically by Doc_02 SS2, though not "
        "independently isolated by its specific oration number this session.")
    ids["gregory-nazianzus-on-the-mamas-festival"] = emit_source(
        115, "gregory-nazianzus-on-the-mamas-festival", "Gregory of Nazianzus",
        "Gregory of Nazianzus on the Mamas festival", NPNF207, "v", "attributed",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "The martyrium/shrine panegyris material-culture record (row 84); the "
        "martyrs'-festival gravity candidate (row 115). Distinct from Basil's own Mamas "
        "homily (already counted within row 20).")

    return ids


def build_world_core(source_ids: dict[str, str]) -> str:
    """world_id 'nicene-cappadocian' and id 'cappadocian.core.nicene-cappadocian' -- both this
    script's own naming judgment calls (see module docstring).

    time_window.end = 394, NOT 381, is this record's own judgment call, argued explicitly: Doc_01
    SS1/SS4a names TWO candidate closing dates and is careful to keep them distinct -- 381 is the
    ECOLOGICAL BREAK (the situational gravity dissolves by victory; formation, worship's live
    stakes, authority, and interpretation all change at that point) and 394 is a SEPARATE, later
    EVIDENTIARY HORIZON (the death or last secure attestation of the founding generation's own
    last survivors). Doc_01 itself is explicit that 394 is not itself an ecological finding --
    SS4a's own conclusion states plainly "this section supplies the 381 argument; it does not,
    and should not be read to, argue 394 itself into an ecological finding." But comparing how
    time_window is actually USED by an existing, real record (hal.core.hieronymian):  HAL's own
    time_window (382-420) runs to Jerome's DEATH YEAR, not to any earlier "the argument's live
    stakes changed" moment inside that span -- it is the FULL span the voice can draw on. Applying
    that same convention here means time_window.end must be 394 (the founding generation's own
    evidentiary horizon), not 381: the thirteen years of post-381 pastoral consolidation are
    still inside what this world's own voice may draw on (Gregory of Nyssa's own later work,
    e.g., falls 382-394), even though 381 is what this record's own `formation_logic` and
    `horizon` name as the moment that changed what kind of world it was. Using 381 here would
    silently exclude real, in-window evidence (rows 42-50 and more, all citing Nyssa's corpus
    which runs past 381) from what the time_window claims the voice can draw on -- an error this
    record does not make.
    """
    horizon = (
        "The Nicene-confessing churches of Cappadocia and Pontus, c. 325 - c. 394: the "
        "formation ecology of the communities that held, defended, and -- after 381 -- "
        "inherited the imperial establishment of the Nicene confession in this region, whose "
        "surviving voice is Basil of Caesarea, Gregory of Nazianzus, Gregory of Nyssa, and the "
        "households and congregations around them (Doc_01 SS1). Not a claim to the region's "
        "whole population: the Homoian court church, the Eunomian movement, the Hypsistarian "
        "sect, and the region's Jewish and old-religion populations are this world's boundary "
        "and rivals, not itself. Begins c. 325 as the empire-wide persecutions end and Nicaea "
        "frames the confession Cappadocian and Pontic bishops (Leontius of Caesarea among "
        "them) subscribe to. Two distinct closing dates are named rather than collapsed into "
        "one: the ecological break falls at 381, when the Council of Constantinople and the "
        "Theodosian settlement dissolve, by victory, the situational gravity -- 'the contested "
        "church under the contested empire' -- this world's whole life had organized around "
        "(Doc_01 SS4a); this record's own time_window instead runs to c. 394, the softer, "
        "later evidentiary horizon -- the death or last secure attestation of the founding "
        "generation's own last survivors (Gregory of Nyssa, c. 394; Peter of Sebaste, last "
        "attested c. 391) -- so that the thirteen years of pastoral consolidation after 381 "
        "remain inside what this voice may draw on, distinct from what organized its "
        "formation. This world's own working self-description, corrected from an earlier and "
        "very likely false claim ('the peace after the last martyrs'): the churches of "
        "Cappadocia and Pontus that held the faith of Nicaea, from the years after the great "
        "persecutions to the death of the last of the great household -- years that cost us "
        "Eupsychius too, at Caesarea, under the last of the persecuting emperors. Geography: "
        "Cappadocia proper (Caesarea, Nazianzus, Nyssa, Tyana), Pontus along the Iris valley "
        "(Annisa, Neocaesarea), Armenia Minor (Sebaste), and Lycaonia so far as Iconium's see "
        "(Amphilochius) enters this world's own canonical-letter evidence (Doc_01 SS1)."
    )
    formation_logic = (
        "Formation as doxology institutionalized under hostile weather: this world binds "
        "every register of life -- word, household, wealth, learning, grief -- into the right "
        "glorification of a God no mind can compass, so that precision of confession and "
        "mercy toward the image-bearer become one trained reverence, eusebeia (Doc_07 SS2E). "
        "The mechanism is reception before analysis, repetition before articulation: the "
        "baptismal formula is said over a person before they can weigh it; the psalms are "
        "sung until they interpret the singer; customs are kept because they were handed "
        "down, defended later if ever; doctrine arrives as the explanation of what the "
        "community already does, not the reverse. Authority runs through distributed, "
        "portable carriers -- formula, custom, psalm, household elder, recognized ascetic "
        "holiness -- rather than a stable institutional center, precisely because for most of "
        "this world's span the imperial court, the great sees, and the councils were "
        "adversarial or absent (Doc_07 SS2C, SS3). The formed person is the reverent "
        "householder at minimum and, for some, the conscripted bishop: one seized for office "
        "because they did not want it, trained to hold fine distinctions -- ousia/hypostasis, "
        "graded penance, graded reception of the returning heretic -- not as walls but as "
        "instruments of exactness in the service of communion (Doc_07 SS2D). The system's one "
        "named enemy, met at every scale, is presumption: the tongue that defines God, the "
        "ambition that seeks the chair, the granary that forgets whose surplus it holds "
        "(Doc_07 SS5)."
    )
    thinness = (
        "Richest in the letters, orations, and treatises of Basil of Caesarea, Gregory of "
        "Nazianzus, and Gregory of Nyssa, and in the women they chose to commemorate -- "
        "Macrina, Emmelia, Gorgonia, Theosebia, Macrina the Elder -- as they chose to present "
        "them (Doc_02 SS1, SS6). Thin-to-silent structurally: no text composed by any woman of "
        "this world survives in her own words; the plateau countryside and its non-elite, "
        "non-Greek-speaking faithful appear only as objects of famine relief, festival "
        "crowds, and canonical discipline, never as speakers (Doc_02 SS6.2, SS6.6); the "
        "enslaved appear only through legislation about them (Basil's canons 40/42, the "
        "Asketikon's runaway-slave provisions, Gangra canon 3) and two acts of individual "
        "manumission (Gregory of Nazianzus' will; the Vita's freed maidservant) -- never in "
        "their own voice, despite one preacher's sharp protest against the institution itself "
        "(Gregory of Nyssa's Ecclesiastes homilies) having no documented reception in the "
        "world's own legal practice (Doc_07 SS2J); the defeated parties -- Eustathius, the "
        "Pneumatomachians, the Homoian church, the Gangra radicals -- survive only inside "
        "their opponents' polemic, with the sole partial exception of Eunomius' own First "
        "Apology and 383 confession (Doc_02 SS1.5, SS6); material culture beyond two "
        "text-attested institutions (the martyr-shrine panegyris and Caesarea's poorhouse-"
        "hospital complex) is essentially unrecovered -- no securely identified physical "
        "remains for either (Doc_07 SS2I)."
    )
    cautions = (
        "1) AUTHOR GRAVITY: nearly the entire record is three men's own hand -- Basil, "
        "Gregory of Nazianzus, Gregory of Nyssa -- one extended family and one friendship "
        "network (Doc_01 SS1, SS3; Doc_02 SS6). Never convert their narrative richness or "
        "institutional dominance into independent corroboration; the family-transmission "
        "pattern (Nazianzen editing his own letters, Nyssen completing and defending his "
        "brother's works) means the archive is partly a family memorial (Doc_02 SS7). 2) "
        "SELF-DESCRIPTION CORRECTED: the prior draft's self-description -- 'the peace after "
        "the last martyrs' -- is very likely factually wrong. Eupsychius of Caesarea was "
        "executed under Julian in 362, inside this world's own span, and his cult (an annual "
        "7 September feast at Caesarea) is attested in Basil's own letters; no homily on him "
        "is attested by anyone, only the feast itself (Doc_01 SS1; Source Registry row 83, "
        "correcting an earlier draft's fabricated 'homilies on Eupsychius' claim). 3) LITERARY "
        "FRAMING: Macrina the Younger's entire record reaches us through her brother Gregory "
        "of Nyssa's deliberate Socratic-Platonic literary framing (Macrina as Diotima at the "
        "deathbed) -- her historical leadership of the Annisa community is Widely Accepted, "
        "her own words are not recoverable (Doc_02 SS1.4). 4) CONTESTED AUTHORSHIP: canonical "
        "Epistle 38 (on ousia/hypostasis), this world's flagship Trinitarian-vocabulary "
        "citation, is reassigned by a substantial body of modern scholarship (Cavallin, "
        "Hubner, Zachhuber, with Drecoll leaning the same way) from Basil to Gregory of Nyssa "
        "(Source Registry row 23) -- never cite it as settled-Basilian without this flag. 5) "
        "DISPUTED CORRESPONDENCE: the Basil-Libanius letters (Epp. 335-359) are held by the "
        "majority of Libanius scholars to be an outright forgery, with a proposed forger's "
        "motive on record -- never cite as evidence of genuine contact between Basil and the "
        "pagan rhetor without flagging this as contested at every use (Source Registry row "
        "12). 6) UNACQUIRED TEXTS, NAMED AS GAPS, NOT SMOOTHED PAST: no complete open-license "
        "English translation of Basil's Against Eunomius exists -- the only complete "
        "translation (DelCogliano & Radde-Gallwitz, 2011) is copyrighted and outside this "
        "project's manifest (Source Registry rows 14, 24); Basil's Small Asketikon -- the "
        "non-Greek recension (Rufinus' 397 Latin translation; a Syriac version) that "
        "Gribomont's textual work shows has PRIORITY over the Great Asketikon usually read -- "
        "was never acquired as an open text this session; its existence and priority are "
        "load-bearing for this world's own ascetic-history self-understanding even without the "
        "text in hand (Source Registry row 19). 7) BRIEF ESTABLISHMENT, THINLY DOCUMENTED: "
        "this world's own record of being pressed by a hostile court across most of its span "
        "must not be silently converted into innocence-by-default about what its own leaders "
        "did once establishment arrived in 381 -- what they did with that brief victory, in "
        "the thirteen years before this world's own evidentiary horizon (394), is thinly "
        "documented in this corpus (Doc_07 SS3, SS2J). 8) The Gangra canons' date is genuinely "
        "Contested across a wide range (c. 340s-370s, not 'within a decade' as an earlier "
        "draft claimed) -- if Gangra falls in the 350s rather than the 340s, it censures "
        "Eustathius as Basil's own sitting ascetic mentor during Basil's formative years, not "
        "settled pre-history (Doc_01 SS3)."
    )
    thin_topics = [
        {"keywords": ["women's own words", "Macrina's own voice", "Gorgonia", "Theosebia",
                      "sisterhoods"],
         "note": "No text composed by any woman of this world survives; everything reaches us "
                 "through male authors, chiefly Gregory of Nyssa's literary framing of "
                 "Macrina."},
        {"keywords": ["plateau villages", "rural non-elite", "non-Greek-speaking faithful",
                      "peasant religion"],
         "note": "The countryside appears only as an object of famine relief, festival crowds, "
                 "and canonical discipline -- never as a speaking subject; almost no evidence "
                 "is independent of the metropolitan sees' own writing about it."},
        {"keywords": ["enslaved persons", "slavery", "slaveholding", "manumission"],
         "note": "The enslaved appear only through legislation about them and two acts of "
                 "individual manumission; Gregory of Nyssa's protest against slaveholding "
                 "itself has no documented reception in the world's own canon law."},
        {"keywords": ["Small Asketikon", "complete Against Eunomius translation",
                      "unacquired texts"],
         "note": "Basil's Small Asketikon (non-Greek recension) and the only complete English "
                 "translation of Against Eunomius (DelCogliano and Radde-Gallwitz, 2011, "
                 "copyrighted) were not acquired as open texts this build."},
        {"keywords": ["Eustathius own words", "Pneumatomachians", "Homoian church",
                      "defeated parties"],
         "note": "The world's own internal and external opponents survive almost entirely "
                 "through hostile transmission; Eunomius' First Apology and 383 confession are "
                 "the rare partial exception."},
        {"keywords": ["archaeology", "excavation", "material remains", "poorhouse remains"],
         "note": "No securely identified physical remains exist for either of this world's two "
                 "documented institutions (the martyr shrine, the poorhouse-hospital "
                 "complex)."},
    ]
    sources = [
        {"source_id": source_ids["basil-letters-general-corpus"],
         "locus": "passim -- the world's central institutional and pastoral voice",
         "license": "public-domain"},
        {"source_id": source_ids["gregory-nazianzus-orations-general-corpus"],
         "locus": "the five Theological Orations and the funeral encomium on Basil (Or. 43)",
         "license": "public-domain"},
        {"source_id": source_ids["gregory-nyssa-general-dogmatic-ascetic-corpus"],
         "locus": "passim -- Trinitarian, catechetical, and ascetic corpus",
         "license": "public-domain"},
        {"source_id": source_ids["gregory-nyssa-life-of-macrina"],
         "locus": "whole work",
         "license": "public-domain"},
        {"source_id": source_ids["eupsychius-of-caesareas-feast"],
         "locus": "whole -- grounds the corrected self-description",
         "license": "public-domain"},
    ]
    payload = {
        "id": "cappadocian.core.nicene-cappadocian",
        "world_id": WORLD_ID,
        "record_type": "world_core",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("B", "verified-via-authority", "load-bearing",
                            "Dominant Modern Reconstruction", None),
        "sources": sources,
        "relations": [],
        "time_window": {"start": 325, "end": 394},
        "horizon": horizon,
        "formation_logic": formation_logic,
        "thinness": thinness,
        "cautions": cautions,
        "thin_topics": thin_topics,
    }
    out_dir = RECORDS_ROOT / "world_core"
    out_dir.mkdir(parents=True, exist_ok=True)
    front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    body = (
        "Built from cappadocian_Doc_01_World_Identification.md (SS1, SS4a: the corrected "
        "self-description naming Eupsychius; the two-date boundary argument), "
        "cappadocian_Integrated_Ecology_Analysis.md SS2E/SS3/SS5 (formation_logic), and "
        "cappadocian_Doc_02_Source_Ecology.md SS6/SS9 plus the Source Registry's own named "
        "gaps (thinness/cautions/thin_topics). world_id 'nicene-cappadocian' and "
        "time_window.end=394 (not 381) are this script's own judgment calls, argued in the "
        "build_world_core() docstring above the payload in wb_cappadocian_s21.py.\n\n"
        "No Representative content appears in this record (Doc_01 constraint honored)."
    )
    text = f"---\n{front}---\n{body}\n"
    path = out_dir / f"{payload['id']}.md"
    path.write_text(text, encoding="utf-8")
    WRITTEN.append(str(path))
    return payload["id"]


def main() -> None:
    source_ids = build_sources()
    assert len(source_ids) == 110, f"expected 110 source records, built {len(source_ids)}"
    world_core_id = build_world_core(source_ids)
    print(f"Wrote {len(WRITTEN)} records:")
    print(f"  - {len(source_ids)} source records under {RECORDS_ROOT / 'source'}")
    print(f"  - 1 world_core record ({world_core_id}) under {RECORDS_ROOT / 'world_core'}")


if __name__ == "__main__":
    sys.exit(main())
