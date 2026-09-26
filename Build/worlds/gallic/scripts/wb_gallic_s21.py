"""B-1 (S2.1): Gallic Monastic-Ascetic Christianity (gallic) source + world_core records.

WHAT THIS SCRIPT DOES. Converts this world's completed Phase A documents
(Doc_01 through Doc_10, all Approved to Proceed) into WRS records under
records/gallic/{source,world_core}/, per the live schema (engine/m1/schemas.py)
and gate battery (engine/m1/gates.py). This is the FIRST record-authoring pass
for this world; no `gallic` records existed anywhere before this script ran
(confirmed: no records/gallic/ directory, no `gallic` entry in records/worlds.yaml).

Built following the one located predecessor script's own pattern and
disclosure discipline exactly: Build/worlds/cappadocian/scripts/wb_cappadocian_s21.py
(the only prior B-1 authoring script under the current, post-cic-poc-retirement
tooling; read in full before writing this one). No newer precedent exists as
of this build (recon confirmed via CAPPADOCIAN_BUILD_LEDGER.md plus a fresh
records/worlds.yaml read: Cappadocian remains the only world that has gone
through B-1 through B-9 on the live engine/m1-m3 system as of 2026-09-10).

INPUTS, mapped to OUTPUTS, precisely:
  - Build/worlds/gallic/gallic_Source_Registry.md
    (44 rows) -> the 36 `source` records (ROWS below). Only rows with Boundary
    Status "Native" become records. The 8 Excluded rows -- row 4 (Dialogue I /
    Postumianus's Egyptian travel, Named Comparandum -- desert-monasticism's
    own territory), row 33 (Hilary of Poitiers, Named Comparandum -- belongs
    to the separate, unbuilt gallic-nicene-episcopate), row 34 (Athanasius's
    Vita Antonii, Named Comparandum -- desert-monasticism's founding text),
    row 35 (the rest of Augustine's corpus, Named Comparandum -- the single
    highest-risk unconstrained-generation reach for a grace-controversy
    world), row 36 (Rule of Benedict, Named Comparandum -- era-3, not this
    world's own text), rows 37-38 (Jerome's and Augustine's one-line
    attestations of Sulpitius, Out-of-Boundary -- third-party testimony only,
    belonging to other worlds' own corpora), and row 44 (Constantius of
    Lyon's Vita Germani, Named Comparandum -- a literary-model relationship
    only, no documented connection to this world's own circle) -- are
    deliberately NOT emitted as this world's own source records, exactly as
    the Registry itself disposes them.
  - gallic_Doc01_World_Identification.md SS2 -> world_core.time_window
    (c. 360-450, the working floor and the working ceiling, both argued
    against their strongest counter-evidence rather than asserted).
  - gallic_Doc05_Ecological_Reconstruction.md / gallic_Doc07_Integrated_Ecology_Analysis.md
    -> world_core.formation_logic (the reception grammar -- G4 "received,
    not invented" as the single axis run through every lens -- and the
    monk-bishop capture pattern, G1).
  - gallic_Doc05_Ecological_Reconstruction.md SS1.3/SS10 (Missing Voices),
    gallic_Doc09_Story_Inventory.md SS8 (Absent Stories), and the Source
    Registry's own named gaps -> world_core.thinness / .cautions /
    .thin_topics.

MECHANICAL vs AUTHORED, field by field (so a reviewer can tell what to
re-check against the Registry directly vs what required this script's own
reading and judgment), following the Cappadocian precedent's own discipline
exactly:
  - id, world_id, record_type, schema_version, status, register, canon_cells:
    MECHANICAL -- register="etic" for every source record (a source record
    describes an external text, not the world's own first-person voice,
    matching hal.source.*/cappadocian.source.* precedent); canon_cells=[]
    throughout, since no canon-cell tagging work has happened yet at this
    build step.
  - author / work / edition: AUTHORED, per row, by hand. The Registry's own
    `Source` column is one free-text cell mixing author, work-with-scope, and
    (often) a vendored file path -- splitting it into three schema fields
    required reading each row's own Verification Note, not a mechanical
    regex split (e.g. row 11 and row 31 have no "work" in the ordinary sense
    -- they document an EDITION-LEVEL ABSENCE, not a held text, and both
    needed honest, non-fabricated phrasing rather than empty required
    fields).
  - rights_status: AUTHORED per row via the RIGHTS dict below (six buckets:
    "vv" vendored + independently verified/rights-checked in the same build
    session that produced this Registry -- rows 24-27, 43, all dated
    2026-09-09; "v" vendored earlier and not rechecked at the rights level
    this pass; "na" not yet acquired as an open text; "ic" in-copyright,
    deliberately excluded -- none in this world's 36 Native rows, named for
    completeness with the Cappadocian precedent; "nt" no single specific
    text identified (a named person/pattern, not a held work); "absence" no
    text exists to hold rights over because the row's own subject IS a
    documented absence from a vendored edition -- rows 11 and 31 specifically).
    No row is left blank; gate_rights fails closed on blank.
  - attribution_status: AUTHORED per row. Default "attributed". Row 5 (the
    Doubtful Letters) carries the Registry's own 2026-08-26 ruling verbatim
    (filed under the attributed name AND as pseudepigraphal literature) --
    the one row in this world's Registry with a real, disclosed authorship
    complication.
  - discovery_channel: AUTHORED via dc() below, keyed to the SAME
    verification-state judgment as confidence.verification_state so the two
    fields never silently disagree, naming the Source Registry row number
    for traceability (also mirrored into external_ids.gallic_source_registry_row).
  - confidence.citation_specificity: MECHANICAL -- copied directly from the
    Registry's own Confidence (A-E) column. Six rows in this Registry carry a
    SPLIT confidence (e.g. row 8 "A (dedication/dating) / C (content)"; row 9
    "A (dedication text) / B (editorial identification) / C (content, except
    Conf. XIII)") -- per this script's own judgment call, the record carries
    the HIGHEST of the split tiers (matching what the row is most
    specifically and directly attested for), with the full split stated in
    the record's own divergence_note so the caveat is never silently
    dropped.
  - confidence.verification_state: AUTHORED, via the same explicit rule the
    Cappadocian precedent used, stated here so it can be checked against the
    Registry text directly:
      * A Verification Note stating the text (or the relevant passage) was
        "read directly", "read in full", "confirmed directly", or
        "re-verified" THIS Registry's own build session -> verified-direct.
      * A Verification Note citing an already-vendored text with a real but
        lighter check (identity/completeness confirmed, content not deeply
        read; or content read but not the specific citation at issue) ->
        verified-via-authority.
      * A Verification Note that explicitly hedges ("full text not read",
        "text itself not read", "not independently read", "not yet
        examined beyond location", "not independently verified this
        session") OR the text is named but not yet acquired/located ->
        named-not-rechecked.
      * Registry Confidence C, uniformly (by the Template's own definition,
        a named author/scholar without a pinpointed locus this build has
        independently checked) -> named-not-rechecked.
      * Registry Confidence D (no named author or specific text, a general
        pattern known via one attributed clause) -> unverified.
    No Native row in this Registry carries an E rating (confirmed by a
    direct grep of the live table before writing this script).
  - confidence.evidentiary_weight: AUTHORED per row from the Registry's own
    Licensed For column. `load-bearing` for this world's own Native primary
    voice content (Sulpitius, Cassian, Vincent, Eucherius, Hilary of Arles,
    Salvian, Faustus, Prosper's own primary texts); `corroborating` for rows
    that verify or contextualize rather than themselves being this world's
    voice (Augustine's three Gaul-directed treatises -- explicitly marked
    "(context)" in the Registry itself; Gennadius; Richardson's editorial
    apparatus; the edition-level absence rows 11 and 31; Contra Collatorem,
    an external critique); `illustrative` for the thinnest, most marginal
    citations (Noris, Tillemont, Farrar -- rows 39-41, each known only via a
    single quoted clause inside another vendored text). `contested` (a real
    enum value) is not used in this world's 36 Native rows -- no row's own
    OBJECT-level genuineness (as opposed to a scholarly-attribution dispute
    carried in attribution_status) is disputed in this Registry.
  - confidence.formation_confidence: AUTHORED per row, Article 17's five-
    level vocabulary, deliberately NOT derived from citation_specificity.
    Default Widely Accepted for any row not otherwise flagged. Documented is
    reserved for rows this record can honestly pair with verified-direct
    AND whose underlying claim (a text's existence, authorship, and basic
    content) is not itself part of a live scholarly dispute this build's own
    documents carry as Contested -- rows 1, 7, 11, 13, 15, 30, 31, 43.
    Contested for row 3 (Dialogues) specifically, where this world's own
    Doc_01 SS2.1/Doc_02 names a genuine, unresolved open discrepancy between
    the vendored text's own three-Dialogue structure and Gennadius's
    description of "two divisions" -- named at Doc_02 SS3/SS13 item 11, not
    resolved by this record. Inferential-Thin for rows resting on a named-
    but-unlocated or genuinely thin citation with no content in hand (39,
    40, 41 -- Noris, Tillemont, Farrar, each attested only via one quoted
    clause inside another text this build has read).
  - confidence.divergence_note: null by default; populated with a short,
    honest sentence wherever a row's formation_confidence, or its own
    SPLIT citation-specificity tier, needs explaining -- e.g. rows 8 and 9
    (the dedication/content confidence splits, and row 9's own withdrawn
    "doubly evidenced" claim, Registry Round 2 N4); row 3 (the Gennadius
    "two divisions" discrepancy); row 5 (the pseudepigraphal ruling). Per
    the conf() helper below, this script hard-asserts gate_confidence_
    crosscheck's own rule (Documented + null divergence_note requires
    verified-direct) at construction time, not left to hope.
  - sources / relations (on EACH source record): left empty by design, a
    judgment call matching the Cappadocian precedent exactly -- populating
    cross-references between source records now would require reciprocal
    `relations` entries on both sides (gate_reciprocity) for no benefit this
    step actually needs. The world_core record DOES populate `sources`,
    referencing a handful of the richest source ids created in this same
    run -- those resolve cleanly under gate_referential since both records
    are emitted together.

WORLD_ID: this world has never been given a `world_id` value anywhere in the
live system (records/worlds.yaml has no `gallic` entry at all -- confirmed by
reading it directly before writing this script, alongside the other 8
registered world keys: fix, alx, desert, pahc, hal, syr, ijc, cappadocian).
This script mints `gallic-monastic-ascetic-christianity`, matching this
world's own Atlas census identifier and G0 case-document naming (the world
code `gallic` used throughout every prior Phase A document is the directory/
record-id prefix, not the full world_id -- the same relationship
`cappadocian`/`cappadocian-trinitarian` and `ijc`/`imperial-juridical` already
carry). This is a judgment call for a later world-admission step
(records/worlds.yaml) to ratify, not override -- recorded here, not silently
assumed, per the Cappadocian precedent's own disclosure of the identical
judgment call.

SCRIPT LOCATION: Build/worlds/gallic/scripts/,
matching the Cappadocian precedent's own placement rationale exactly: this is
build tooling for ONE world, reads that world's own documents by relative
path, and has no reason to live inside the shared engine.

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells (no canon-cell tagging work
has happened for this world yet -- expected, per the Cappadocian precedent,
to leave canon-coverage/narratability/etc. trivially incomplete at this
step); register `gallic` in records/worlds.yaml (a later admission-track
step); touch any other world's records; resolve the reserved one-world-or-
two-nodes question (Doc_01 SS6; carried forward exactly as Doc_01-09 and
Doc_10 leave it, in world_core.cautions below).
"""
from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[3]  # .../CIC-Project
RECORDS_ROOT = REPO_ROOT / "records" / "gallic"

WORLD_ID = "gallic-monastic-ascetic-christianity"
SCHEMA_VERSION = 2

# ---------------------------------------------------------------------------
# Shared edition strings for vendored files cited by many rows. Filenames
# checked directly against gallic_Source_Registry.md's own citations (this
# world's Registry names the vendored cic/texts/ file inline per row, unlike
# some sibling worlds' Registries which require a separate cross-check) --
# not copied blind.
NPNF211 = ("Nicene and Post-Nicene Fathers, 2nd series, vol. 11 (Sulpitius Severus, Vincent of "
           "Lerins, John Cassian), tr. Alexander Roberts / C. A. Heurtley / Edgar C. S. Gibson, "
           "ed. Schaff and Wace, vendored as "
           "cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml")
NPNF203 = ("Nicene and Post-Nicene Fathers, 2nd series, vol. 3 (Theodoret, Jerome, Gennadius, "
           "Rufinus), tr. Ernest Cushing Richardson, ed. Schaff and Wace, vendored as "
           "cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml")
NPNF105 = ("Nicene and Post-Nicene Fathers, 1st series, vol. 5 (Augustine: Anti-Pelagian "
           "Writings), tr. Peter Holmes and Robert Ernest Wallis, ed. Philip Schaff, Introduction "
           "by Benjamin B. Warfield, vendored as cic/texts/npnf105_augustine-anti-pelagian-writings.xml")
NPNF101 = ("Nicene and Post-Nicene Fathers, 1st series, vol. 1 (Augustine: Confessions and "
           "Letters), ed. Philip Schaff, vendored as cic/texts/npnf101_augustine-confessions-letters.xml")
FAUSTUS = ("Faustus of Riez, De gratia libri duo, in Fausti Reiensis Praeter sermones "
           "pseudo-eusebianos opera: accedunt Ruricii epistulae, ed. Engelbrecht, CSEL vol. 21 "
           "(Vienna: Tempsky, 1891), vendored as "
           "cic/texts/faustus-riez_de-gratia-and-collected-works_engelbrecht1891.txt")
EUCHERIUS_CONTEMPTU = ("Eucherius of Lyon, De Contemptu Mundi (\"The World Contemned\"), tr. "
                       "Henry Vaughan (1654), vendored as "
                       "cic/texts/eucherius-lyon_de-contemptu-mundi_vaughan1654.txt")
EUCHERIUS_LAUDE = ("Eucherius of Lyon, De Laude Eremi (to Hilary of Arles, c. 428), Latin, "
                    "extracted from Migne Patrologia Latina 50 (1846), vendored as "
                    "cic/texts/eucherius-lyon_de-laude-eremi_migne-pl50.txt")
HILARY_ARLES = ("Hilary of Arles, Sermo de Vita Sancti Honorati, Latin, extracted from Migne "
                 "Patrologia Latina 50 (1846), vendored as "
                 "cic/texts/hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt")
SALVIAN = ("Salvian of Marseilles, On the Government of God (De Gubernatione Dei), tr. Eva M. "
           "Sanford (1930), vendored as cic/texts/salvian_on-the-government-of-god_sanford1930.txt")

RIGHTS = {
    "vv": ("public-domain; vendored in cic/texts/ 2026-09-09 and independently rights-verified "
           "(archive.org public-domain/rights metadata directly checked; title, editor, date, "
           "and contents independently re-verified) within the same build session that produced "
           "this world's own Source Registry."),
    "v": ("public-domain; vendored in cic/texts/, rights confirmed as part of this world's own "
          "corpus-map assignment; not independently re-checked at the rights level by this "
          "authoring pass specifically."),
    "na": ("not independently verified this session; row not yet acquired as an open text -- "
           "named for completeness per the Source Registry's own checkpoint rule (every source a "
           "Doc_02 claim rests on gets a row, acquired or not)."),
    "nt": ("not applicable in the ordinary sense -- no single specific text has been identified "
           "for this row; it names a general pattern, or a work known only via a single quoted "
           "clause inside another vendored text, rather than a held text of its own. Not "
           "independently verified this session."),
    "absence": ("not applicable -- no text exists to hold rights over. This row's own subject is "
                "a documented absence from a vendored edition (what the edition does NOT contain), "
                "not a held work."),
}


def dc(num: int, verify: str) -> str:
    if verify == "verified-direct":
        return (f"builder-direct-read; Source Registry row {num}; the passage or text at issue "
                 "was read directly, in full or at its own specific locus, within this world's "
                 "own Source Registry build session.")
    if verify == "verified-via-authority":
        return (f"builder-direct-read; Source Registry row {num}; a named, vendored text already "
                 "sitting in cic/texts/, checked for identity/completeness/placement but not "
                 "reopened to verify this specific citation at the depth a verified-direct rating "
                 "would require.")
    if verify == "named-not-rechecked":
        return (f"builder-prior-knowledge; Source Registry row {num}; a specific named source "
                 "(author, translator, edition, or witness) whose full text this build session "
                 "did not independently read -- either its own specific locus was not opened in "
                 "an already-vendored file, or the named text has not yet been acquired at all "
                 "(see rights_status for which).")
    if verify == "unverified":
        return (f"builder-prior-knowledge; Source Registry row {num}; a general pattern or "
                 "attribution known via one quoted clause, with no independently locatable text "
                 "of its own.")
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
        "id": f"gallic.source.{slug}",
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
        "external_ids": {"gallic_source_registry_row": num},
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

    # --- Tours node: Sulpitius Severus (rows 1-3, 5-6) ----------------------
    ids["sulpitius-vita-martini"] = emit_source(
        1, "sulpitius-vita-martini", "Sulpitius Severus (c. 363 - c. 425)",
        "On the Life of St. Martin (Vita Martini)", NPNF211, "v", "attributed",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "This world's single richest narrative source, grounding Martin's formation, the "
        "election, the discharge-before-Caesar scene, the raising of the catechumen, and the "
        "Amiens cloak vision (row 1; Doc_09 gallicstory001-004). Preface and Chapter I read "
        "directly and verbatim-quoted at this Registry's own construction; the fuller narrative "
        "is read chapter-by-chapter across Doc_04/05/07/09 and cited there with its own div id.")
    ids["sulpitius-letters"] = emit_source(
        2, "sulpitius-letters", "Sulpitius Severus",
        "The Letters (three undisputed: to Eusebius, to Aurelius, to Bassula -- Ep. III on "
        "Martin's death)", NPNF211, "v", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "Ep. III grounds the death-and-funeral story (row 2; Doc_09 gallicstory007). Existence, "
        "count, and placement confirmed via structural TOC at this Registry's own build; the "
        "full text of Ep. III was subsequently read in full at Doc_09 construction (npnf211 div "
        "ii.iii.iii) -- a fresh verification distinct from and later than this Registry's own "
        "session-scoped B rating, which this record carries honestly rather than silently "
        "upgrading.")
    ids["sulpitius-dialogues-ii-iii"] = emit_source(
        3, "sulpitius-dialogues-ii-iii", "Sulpitius Severus",
        "Dialogues II-III (the Martin material: the Treves/Ithacian-communion episode, Brictio, "
        "the tomb scruple, further virtus narratives)", NPNF211, "v", "attributed",
        "A", "verified-direct", "load-bearing", "Contested", (
            "Gennadius's own text (row 30, ch. XIX) describes the whole work as \"a Conference "
            "between Postumianus and Gallus... in two divisions,\" against this world's own "
            "vendored three-Dialogue structure -- an open discrepancy, named at Doc_02 SS3/SS13 "
            "item 11, not resolved by this record or any prior document in this build."),
        "Read for frame narrative and structural placement; the Martin-material chapters (II.2-4, "
        "III.11-17) are read at their own loci across Doc_04/05/07/09 (gallicstory005, 006). The "
        "Gennadius discrepancy is carried as a live, disclosed tension, not silently resolved "
        "toward either structure.")
    ids["sulpitius-doubtful-letters"] = emit_source(
        5, "sulpitius-doubtful-letters", "Sulpitius Severus (attributed)",
        "The Doubtful Letters -- at least eight letters, two to Claudia confirmed", NPNF211, "v",
        "attributed to Sulpitius by tradition; ruled 2026-08-26 to be filed both under the "
        "attributed name and as pseudepigraphal literature -- genuineness itself is the open "
        "question this attribution status discloses, not merely authorship detail",
        "A", "verified-direct", "corroborating", "Widely Accepted", (
            "Genuineness contested by tradition (hence 'Doubtful'); this world's own build ruled "
            "2026-08-26 to carry both the attributed name and the pseudepigraphal-literature "
            "classification rather than choosing one, per the Registry's own disclosure "
            "discipline."),
        "Grounds Claudia as this world's elite-women's-correspondence trace (Doc_05 SS1.3, not an "
        "ordinary-participant trace). Both Claudia letters' openings read directly at this "
        "Registry's own construction.")
    ids["sulpitius-sacred-history"] = emit_source(
        6, "sulpitius-sacred-history", "Sulpitius Severus",
        "The Sacred History (Chronica), 2 books", NPNF211, "v", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "World-chronicle framing; grounds the earlier phase of the Priscillianist-affair "
        "narrative (SH II.50, distinct from but related to Dial. III.11-13 -- Doc_09 "
        "gallicstory005's own M13 correction keeps the two accounts distinct rather than treating "
        "them as one converging narrative). Introduction read directly at this Registry's own "
        "construction; SH II.50 itself was subsequently read in full at Doc_04/Doc_09 "
        "construction (npnf211 div ii.vi.ii.l), a fresh verification this record notes without "
        "silently upgrading the Registry's own session-scoped B rating.")

    # --- Lerins-Marseilles node: John Cassian (rows 7-12) -------------------
    ids["cassian-institutes"] = emit_source(
        7, "cassian-institutes", "John Cassian (c. 360 - c. 435)",
        "The Twelve Books on the Institutes of the Coenobia", NPNF211, "v", "attributed",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "Grounds the Egyptian-to-Gallic transmission-and-adaptation program in full: the girdle, "
        "the canonical hours, the Gallic Gloria (a thing this world's own text says it does NOT "
        "share with the East, Inst. II.8), the entrance sequence, the eight-faults order of "
        "battle, and the Castor/Apta Julia dedication (Doc_04/05, chunk 007). Preface read in "
        "full; Book I ch. X's dress passage read and verbatim-quoted, including its own "
        "translator's-omission footnote, at this Registry's own construction.")
    ids["cassian-conferences-part-i"] = emit_source(
        8, "cassian-conferences-part-i", "John Cassian",
        "The Conferences, Part I (Conferences I-X, dedicated to Helladius and Leontius)", NPNF211,
        "v", "attributed",
        "A", "verified-direct", "load-bearing", "Widely Accepted", (
            "Registry's own split rating: A for the dedication text and its own chronology "
            "anchor (completed shortly after Castor's death, 426), C for the fuller content of "
            "Conferences I-X generally, per the Registry's own Round 1 correction confirming this "
            "dating clause belongs to Part I, not Part II."),
        "Purity of heart and the archer (Conf. I.4-7, chunk 006), the money-changer (I.20), "
        "Paphnutius on the beginning of a good will (III.19, gallicstory011). Dedication note "
        "read directly and re-verified against its own full surrounding context at this "
        "Registry's own construction.")
    ids["cassian-conferences-part-ii"] = emit_source(
        9, "cassian-conferences-part-ii", "John Cassian",
        "The Conferences, Part II (Conferences XI-XVII, to two unnamed 'holy brothers,' one "
        "presiding over 'a large monastery' -- editorially identified as Honoratus and Eucherius)",
        NPNF211, "v", "attributed",
        "A", "verified-direct", "load-bearing", "Widely Accepted", (
            "Registry's own three-way split: A for the dedication text itself, B for the "
            "editorial (row 17) identification of the dedicatees as Lerins's Honoratus and "
            "Eucherius -- independently corroborated only for Lerins's own existence by Gennadius "
            "(row 30), not for the Cassian-dedication link itself, a claim the Registry's own "
            "Round 2 fix explicitly WITHDREW after finding it rested on a different abbot a "
            "decade later -- and C for content generally, except Conference XIII (grace and "
            "human effort, gallicstory013), which this Registry rates higher."),
        "Archebius carried off to a see (Conf. XI.2, gallicstory012); Germanus's scruple and the "
        "husbandman (XIII.1-3, gallicstory013); the co-operating grace and the declared limit "
        "(XIII.13, XIII.18); Nesteros on exorcists (XV.7). Dedication note read and re-verified "
        "verbatim at this Registry's own construction; XI.2-3 and XIII in full at Doc_09.")
    ids["cassian-conferences-part-iii"] = emit_source(
        10, "cassian-conferences-part-iii", "John Cassian",
        "The Conferences, Part III (Conferences XVIII-XXIV, dedicated to Jovinianus, Minervius, "
        "Leontius, and Theodore)", NPNF211, "v", "attributed",
        "B", "verified-direct", "load-bearing", "Widely Accepted", None,
        "The fathers received 'into their cells' (Pref. III); Paphnutius and the hidden book "
        "(XVIII.15, gallicstory011); the Sarabaite (XVIII.7). Dedication addressees corrected "
        "against the volume's own Introduction text at this Registry's own construction.")
    ids["cassian-conferences-xii-xxii-absence"] = emit_source(
        11, "cassian-conferences-xii-xxii-absence", "Not applicable -- this row documents an edition-level absence, not an authored work.",
        "The absence, in this vendored NPNF edition specifically, of Conferences XII ('On "
        "Chastity') and XXII ('On Nocturnal Illusions')",
        NPNF211, "absence", "not applicable -- this row documents an edition-level absence, not "
        "an authored work",
        "A", "verified-direct", "corroborating", "Documented", None,
        "The single most consequential transmission-gap finding in this world's build: this "
        "world's own vendored English text does not contain these two conferences at all -- "
        "confirmed directly, Conf. XII marked 'Not translated,' Conf. XXII marked 'This "
        "Conference is omitted.' Grounds Doc_05 SS1.2/SS7.3's chastity-and-body Missing Voices "
        "finding and Doc_09 SS8 item 6's Absent Story on the sexual body. Not the same shape of "
        "finding as row 31 (a different, general editorial-selection omission) -- this one is "
        "unexplained in the text and plausibly content-motivated.")
    ids["cassian-de-incarnatione"] = emit_source(
        12, "cassian-de-incarnatione", "John Cassian",
        "The Seven Books on the Incarnation of the Lord, Against Nestorius", "Corpus-map assigned; specific vendored file/edition not independently confirmed by this authoring pass (see body note).", "v", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "Author-tradition basis; the Leo/Celestine transmission context, independently confirmed "
        "by Gennadius's own text (row 30) -- a genuine upward correction from an earlier "
        "backwards confidence arrow (Registry Round 2 N8). Existence and corpus-map assignment "
        "confirmed via the G1 manifest; the text itself has not been read at any point in this "
        "build.")

    # --- Lerins node: Vincent of Lerins (row 13) ----------------------------
    ids["vincent-commonitory"] = emit_source(
        13, "vincent-commonitory", "Vincent of Lerins (d. before 450, probably shortly after 434)",
        "The Commonitory", NPNF211, "v", "attributed",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "This world's own explicit interpretive rule (universality, antiquity, consent against "
        "novelty, chunk 011/012); the southern node's insider self-understanding; the Augustine-"
        "silence pattern. Introduction and the full 33-chapter plus 3-appendix structure read "
        "directly at this Registry's own construction; the 434 date is itself Documented by "
        "internal reference to the Council of Ephesus (431), independently confirmed.")

    # --- Context only: Augustine's three Gaul-directed treatises (rows 14-16) ---
    ids["augustine-on-rebuke-and-grace"] = emit_source(
        14, "augustine-on-rebuke-and-grace", "Augustine of Hippo",
        "On Rebuke and Grace (De Correptione et Gratia) -- context only, addressed to Hadrumetum, "
        "the provoking text for the Gallic monks' objections", NPNF105, "v", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "Explicitly marked (context) by this world's own Registry -- provisional in the "
        "corpus-map, licensed only as background to the Massilian objection, never as this "
        "world's own voice (Doc_04 SS7; Registry row 35's own guard). Addressee and date "
        "confirmed via the G1 manifest; the treatise's own text has not been read directly at "
        "any point in this build.")
    ids["augustine-on-predestination"] = emit_source(
        15, "augustine-on-predestination", "Augustine of Hippo",
        "On the Predestination of the Saints -- context only, the fullest statement of the "
        "Massilian position currently in this project's own library", NPNF105, "v", "attributed",
        "A", "verified-direct", "corroborating", "Widely Accepted", None,
        "Grounds the '(reliquiae Pelagianorum)'/'Massilians' footnote and the 'two laymen' clause "
        "this world's own construction records draw on for the controversy's own naming history "
        "(Doc_01 SS7). Not this world's own voice -- the fuller reports, Augustine's Letters "
        "225-226, exist and are simply unvendored (row 31). Opening chapters read directly, "
        "including the named footnote and clause, both re-verified in full at this Registry's own "
        "construction.")
    ids["augustine-on-the-gift-of-perseverance"] = emit_source(
        16, "augustine-on-the-gift-of-perseverance", "Augustine of Hippo",
        "On the Gift of Perseverance -- context only, companion/continuation of row 15", NPNF105,
        "v", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "Existence and companion relationship confirmed via row 15 and the G1 manifest; not "
        "independently read at any point in this build.")

    # --- Editorial apparatus (row 17) ---------------------------------------
    ids["npnf-editorial-apparatus"] = emit_source(
        17, "npnf-editorial-apparatus", "Philip Schaff (general editor, Series I); Henry Wace "
        "(general editor, Series II); Alexander Roberts (translator, Sulpitius); C. A. Heurtley "
        "(translator, Vincent); Edgar C. S. Gibson (translator, Cassian); Peter Holmes and Robert "
        "Ernest Wallis (translators, Augustine's anti-Pelagian writings); Benjamin B. Warfield "
        "(Introduction author, NPNF I.5)",
        "The editorial introductions and apparatus to NPNF Series II vol. 11 and Series I vol. 5",
        f"{NPNF211}; {NPNF105}", "v", "attributed",
        "A", "verified-direct", "corroborating", "Widely Accepted", None,
        "Chronology corroboration throughout Doc_01/Doc_02 (Author Gravity Assessment, Doc_02 "
        "SS2). None of these three introductions is anonymous -- each is signed on its own "
        "volume's own title page with full institutional position, confirmed by this Registry's "
        "own direct read of each title page.")

    # --- Secondary scholarship (rows 18-23) ---------------------------------
    ids["stancliffe-martin-hagiographer"] = emit_source(
        18, "stancliffe-martin-hagiographer", "Clare Stancliffe",
        "St. Martin and His Hagiographer (Clarendon, 1983)", "Not yet vendored in cic/texts/ -- named and located but not acquired as of this authoring pass.", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "Sulpitius's own reliability as a source; the right instrument for the Sulpitius-"
        "Pelagianism question (Gennadius ch. XIX) and for the Vita Antonii modelling question "
        "(row 34's own comparandum reasoning) -- both left genuinely open in this build, reserved "
        "for Stancliffe (Doc_09 SS9 item 5). Existence, thesis, and publication details "
        "independently verified via live research; full text not read.")
    ids["leyser-authority-and-asceticism"] = emit_source(
        19, "leyser-authority-and-asceticism", "Conrad Leyser",
        "Authority and Asceticism from Augustine to Gregory the Great (Clarendon, 2000)", "Not yet vendored in cic/texts/ -- named and located but not acquired as of this authoring pass.",
        "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "Cassian's own authority and its standing via the Leo commission (row 12). Existence, "
        "thesis, and publication details independently verified via live research; full text not "
        "read.")
    ids["mathisen-ecclesiastical-factionalism"] = emit_source(
        20, "mathisen-ecclesiastical-factionalism", "Ralph W. Mathisen",
        "Ecclesiastical Factionalism and Religious Controversy in Fifth-Century Gaul "
        "(CUA Press, 1989)", "Not yet vendored in cic/texts/ -- named and located but not acquired as of this authoring pass.", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The Lerins circle's own political consolidation -- Doc_01 SS2.4's corrected argument "
        "that this process rises through Hilary of Arles's own tenure (430-449), already inside "
        "this world's own window, not after it. Existence, thesis, and publication details "
        "independently verified via live research; full text not read.")
    ids["chadwick-john-cassian"] = emit_source(
        21, "chadwick-john-cassian", "Owen Chadwick",
        "John Cassian (1950; 2nd ed. 1968)", "Not yet vendored in cic/texts/ -- named and located but not acquired as of this authoring pass.", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "One pole of the Conference XIII / Augustine chronology debate this world's own build "
        "carries Contested and does not resolve (Doc_01 SS7; chunks 008/009 [CT]). Existence and "
        "general reputation independently verified via live research; full text not read.")
    ids["casiday-tradition-and-theology"] = emit_source(
        22, "casiday-tradition-and-theology", "Augustine Casiday",
        "Tradition and Theology in St John Cassian (OUP, 2007)", "Not yet vendored in cic/texts/ -- named and located but not acquired as of this authoring pass.", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The other pole of the same chronology debate. Existence, thesis, and publication details "
        "independently verified via live research; full text not read.")
    ids["weaver-divine-grace-and-human-agency"] = emit_source(
        23, "weaver-divine-grace-and-human-agency", "Rebecca Harden Weaver",
        "Divine Grace and Human Agency: A Study of the Semi-Pelagian Controversy (Mercer, 1996)",
        "Not yet vendored in cic/texts/ -- named and located but not acquired as of this "
        "authoring pass.", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The controversy's own standard modern monograph, closing this world's largest "
        "independent-recall gap. Existence and general subject independently verified via live "
        "research; full text not read.")

    # --- Lerins-Marseilles primary voices vendored 2026-09-09 (rows 24-27) --
    ids["faustus-de-gratia"] = emit_source(
        24, "faustus-de-gratia", "Faustus of Riez (third abbot of Lerins from c. 433; later "
        "bishop of Riez)",
        "De gratia libri duo", FAUSTUS, "vv", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "The most direct surviving Massilian-side answer to Augustine, written from inside this "
        "world's own institutional network decades past its own working ceiling (Doc_01 SS2.4). "
        "Gennadius's own English-summarized doctrine (row 30) is real content-evidence in hand "
        "even before this text's own vendoring -- prevenient, grace-invites-and-precedes-the-will "
        "theology, complicating a simple grace-vs-free-will reading of the controversy. Vendored "
        "and rights-verified 2026-09-09; Latin only, the treatise body itself remains unread "
        "beyond identity/contents verification -- the only English translation (Stucco, Brepols, "
        "2023) is recent and in copyright, so no translation effort has been made.")
    ids["eucherius-de-contemptu-mundi"] = emit_source(
        25, "eucherius-de-contemptu-mundi", "Eucherius of Lyon",
        "De Contemptu Mundi ('The World Contemned')", EUCHERIUS_CONTEMPTU, "vv", "attributed",
        "B", "verified-direct", "load-bearing", "Widely Accepted", None,
        "A third Lerins-insider voice, in English -- Vaughan's 1654 translation. Vendored and "
        "rights-verified 2026-09-09; the complete 31-page CCEL text was fetched and confirmed "
        "complete (front matter through Index of Scripture References) at this Registry's own "
        "construction.")
    ids["eucherius-de-laude-eremi"] = emit_source(
        26, "eucherius-de-laude-eremi", "Eucherius of Lyon",
        "De Laude Eremi (to Hilary of Arles, c. 428)", EUCHERIUS_LAUDE, "vv", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "The island as a harbour for the shipwrecked; the Egyptian fathers' 'crying signs' "
        "(Doc_04 G2/G6; gallicstory014's own Formation Ecology Connection). Vendored and "
        "rights-verified 2026-09-09, Latin only; not yet examined beyond location and identity at "
        "this Registry's own construction -- the specific rendered phrases used downstream (Doc_04, "
        "Doc_09) were located and read at their own build steps, each carrying Inferential-Thin "
        "wording status of its own, disclosed at those loci, not claimed here.")
    ids["hilary-arles-vita-honorati"] = emit_source(
        27, "hilary-arles-vita-honorati", "Hilary of Arles (Honoratus's own disciple and "
        "successor at Arles)",
        "Sermo de Vita Sancti Honorati", HILARY_ARLES, "vv", "attributed",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", (
            "The wording this text supplies is Inferential-Thin throughout this world's build "
            "(this builder's own renderings of rough OCR of the Latin, presence checkable by grep "
            "but sense not verified against a critical edition) -- disclosed at every downstream "
            "locus (Doc_04 SS10 item 6; Doc_06 SS5 item 2; gallicstory014, which states this in "
            "voice as 'as far as those words can be read'). The row's own existence and identity "
            "are independently attested by Gennadius (row 30, ch. LXX: 'his Life of Saint "
            "Honoratus, his predecessor')."),
        "This world's own founding narrative for Lerins -- previously entirely absent from the "
        "vendored library until this Registry's own build session. Vendored and rights-verified "
        "2026-09-09, extracted from the full Migne PL 50 volume; also carries at least one "
        "further short genuine letter of Hilary's, not separately bounded (see the vendored "
        "file's own header).")

    # --- Prosper of Aquitaine, pending intake (rows 28-29) ------------------
    ids["prosper-carmen-de-ingratis"] = emit_source(
        28, "prosper-carmen-de-ingratis", "Prosper of Aquitaine",
        "Carmen de Ingratis", "Not yet vendored in cic/texts/ -- named and located but not acquired as of this authoring pass.", "na", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "The Gallic-born, pro-Augustine dissenting voice -- this world's own controversy heard "
        "from its Augustinian side, by a Gaul rather than by Augustine himself. Located and "
        "rights-checked via the 1744 Opera omnia (archive.org); Latin only; pending intake, not "
        "yet vendored.")
    ids["prosper-pro-augustino-responsiones"] = emit_source(
        29, "prosper-pro-augustino-responsiones", "Prosper of Aquitaine",
        "Pro Augustino Responsiones", "Not yet vendored in cic/texts/ -- named and located but not acquired as of this authoring pass.", "na", "attributed",
        "B", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "Same Gallic-Augustinian voice as row 28, same volume. Located and rights-checked; Latin "
        "only; internal division against Migne's modern sub-titles not confirmed; pending intake.")

    # --- Gennadius, the near-contemporary corroborating witness (row 30) ---
    ids["gennadius-de-viris-illustribus"] = emit_source(
        30, "gennadius-de-viris-illustribus", "Gennadius of Marseilles (writing c. 495, just "
        "after this world's own working ceiling)",
        "De Viris Illustribus", NPNF203, "v", "attributed",
        "A", "verified-direct", "corroborating", "Documented", None,
        "Independent near-contemporary corroboration for Sulpitius (ch. XIX), Cassian (LXII), "
        "Eucherius (LXIV), Vincentius (LXV), Hilary of Arles (LXX), Prosper (LXXXV), and Faustus "
        "(LXXXVI) -- seven chapters read directly and in full, verbatim-quoted throughout this "
        "world's build. Corroborating rather than load-bearing: this world's Representative draws "
        "on the IN-WINDOW facts Gennadius attests, never on Gennadius's own post-window words as "
        "this world's own voice (the same discipline the Cappadocian precedent applies to its own "
        "analogous corroborating witness). Richardson's own bracketed dating endnotes to these "
        "chapters are a distinct, later editorial layer -- see row 42, not this record.")

    # --- Edition-level absence: Augustine's letters to/about Gaul (row 31) --
    ids["augustine-letters-221-226-absence"] = emit_source(
        31, "augustine-letters-221-226-absence", "Not applicable -- this row documents an edition-level absence, not an authored work.",
        "The absence, from this vendored edition (npnf101), of Augustine's Letters 221-226 "
        "(including Epp. 225-226, Prosper's and Hilary's own letters to Augustine)", NPNF101,
        "absence", "not applicable -- this row documents an edition-level absence, not an "
        "authored work",
        "A", "verified-direct", "corroborating", "Documented", None,
        "The actual Massilian reports, in the reporters' own words, are the single most "
        "consequential unvendored source for this world's central controversy -- and their "
        "absence is a declared, general editorial-selection omission, not a content-motivated "
        "one: npnf101's own Prefatory Note states 225-226 are omitted as 'letters written by "
        "others to Augustin' (not his own) and 221-224 as 'miscellaneous smaller letters,' with "
        "Pelagian-controversy material cross-referenced, not suppressed, to NPNF's three "
        "dedicated anti-Pelagian volumes. Confirmed directly at this Registry's own construction: "
        "the vendored letter sequence runs CCXX to CCXXVII; the Prefatory Note states the "
        "Benedictine edition holds 272 letters, of which 160 are translated in this volume.")

    # --- External critique (row 32) -----------------------------------------
    ids["prosper-contra-collatorem"] = emit_source(
        32, "prosper-contra-collatorem", "Prosper of Aquitaine",
        "Contra Collatorem -- a twelve-proposition critique of Cassian's Conference XIII, "
        "extracted from Cassian's own text and judged in part orthodox, in part erroneous, "
        "without ever naming Cassian directly", "Not yet vendored in cic/texts/ -- named and located but not acquired as of this authoring pass.", "na", "attributed",
        "B", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "Independent ancient confirmation that this world's grace controversy was a live literary "
        "fight within participants' own lifetimes. Title, a detailed content description, and its "
        "edition ('given in Gazet's edition of Cassian') are named inside NPNF211's own Cassian "
        "prolegomena, already read in full at rows 7-10's own discovery; no accessible modern "
        "edition or vendoring path has yet been identified.")

    # --- Thin, marginal citations known only via a single quoted clause -----
    ids["noris-historia-pelagiana"] = emit_source(
        39, "noris-historia-pelagiana", "Cardinal Noris (Enrico Noris)",
        "Historia Pelagiana (1673)", "No specific edition identified; known only via a quoted clause inside an already-vendored text (see body note).", "nt", "attributed",
        "C", "named-not-rechecked", "illustrative", "Inferential-Thin", None,
        "General reference only -- no specific Doc_02 claim currently rests on this row (two "
        "specific claims it once licensed were removed from Doc_02 when the underlying material "
        "was corrected, and this row's own Licensed For was updated to match). Known only via "
        "NPNF211's own quotation (Latin, untranslated in that volume); not independently read or "
        "located as an accessible edition.")
    ids["tillemont-vincent-martyrology-doubt"] = emit_source(
        40, "tillemont-vincent-martyrology-doubt", "Louis-Sebastien Le Nain de Tillemont",
        "(unnamed work) -- a doubt attributed to him regarding Vincent of Lerins's place in the "
        "Roman Martyrology", "No specific edition identified; known only via a quoted clause inside an already-vendored text (see body note).", "nt", "attributed",
        "D", "unverified", "illustrative", "Inferential-Thin", None,
        "Known only via one attributed clause inside NPNF211's own Introduction; no specific work "
        "or locus named in what this build has read.")
    ids["farrar-lives-of-the-fathers"] = emit_source(
        41, "farrar-lives-of-the-fathers", "Archdeacon Farrar",
        "Lives of the Fathers, vol. i, p. 628", "No specific edition identified; known only via a quoted clause inside an already-vendored text (see body note).", "nt", "attributed",
        "C", "named-not-rechecked", "illustrative", "Inferential-Thin", None,
        "Martin's own posthumous fame ('from Armenia to Egypt'). Known only via NPNF211's own "
        "quotation, with a specific volume/page given; not independently read.")

    # --- Modern editorial apparatus, distinct from Gennadius's ancient text (row 42) ---
    ids["richardson-gennadius-endnotes"] = emit_source(
        42, "richardson-gennadius-endnotes", "Ernest Cushing Richardson",
        "Editorial apparatus (bracketed dating endnotes) to Gennadius's De Viris Illustribus, "
        "NPNF Series II vol. 3", NPNF203, "v", "attributed",
        "A", "verified-direct", "corroborating", "Widely Accepted", None,
        "A distinct, modern, third editorial layer used and assessed throughout this world's "
        "build (e.g. the Sulpitius, Cassian, Vincent, and Hilary of Arles date attributions) -- "
        "carefully kept distinct from row 30's own ancient text, the discipline this world's own "
        "Doc_02 SS0 names as the one this build repeatedly had to re-learn. Endnotes read "
        "directly alongside the chapters they annotate at this Registry's own construction.")

    # --- Salvian of Marseilles, the fourth Lerins-circle voice (row 43) -----
    ids["salvian-on-the-government-of-god"] = emit_source(
        43, "salvian-on-the-government-of-god", "Salvian of Marseilles",
        "On the Government of God (De Gubernatione Dei)", SALVIAN, "vv", "attributed",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "A genuine additional Lerins-circle authorial voice, direct primary evidence for the "
        "barbarian-pressure and moral-collapse forces material (Doc_04, Doc_08 Force 2A-5) -- but "
        "NOT licensed for the grace/free-will controversy specifically, since Salvian is not a "
        "documented party to the Cassian-Augustine-Prosper argument the way Faustus or Prosper "
        "are. Verified directly against two already-vendored primary sources, not the "
        "translator's own claim alone: Hilary of Arles's own funeral sermon for Honoratus (row "
        "27) names him 'charorum suorum unus' -- one of Honoratus's own dear associates -- and "
        "Gennadius (row 30) independently corroborates his career and standing.")

    return ids


def build_world_core(source_ids: dict[str, str]) -> str:
    payload = {
        "id": "gallic.core.gallic",
        "world_id": WORLD_ID,
        "record_type": "world_core",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("B", "verified-direct", "load-bearing", "Widely Accepted", (
            "The temporal floor is conditional on the reserved one-world-or-two-nodes question "
            "(Doc_01 SS2.1); if a future Step 0 act finds two lineages rather than one strand-"
            "singular world, the southern node's own floor moves to c. 400-410 and this record's "
            "own time_window would need re-examination, not silently assumed settled here."
        )),
        "sources": [
            {"source_id": source_ids["sulpitius-vita-martini"],
             "locus": "passim -- the Tours node's own central narrative voice",
             "license": "public-domain"},
            {"source_id": source_ids["cassian-institutes"],
             "locus": "passim -- the Lerins-Marseilles node's own received program",
             "license": "public-domain"},
            {"source_id": source_ids["vincent-commonitory"],
             "locus": "passim -- this world's own explicit interpretive rule",
             "license": "public-domain"},
            {"source_id": source_ids["gennadius-de-viris-illustribus"],
             "locus": "chs. XIX, LXII, LXIV, LXV, LXX, LXXXV, LXXXVI -- independent near-"
                      "contemporary corroboration across both nodes",
             "license": "public-domain"},
        ],
        "relations": [],
        "time_window": {"start": 360, "end": 450},
        "horizon": (
            "Our span opens with Martin, discharged from Caesar's service, first gathering "
            "brethren near the town where the bishop Hilary protected him -- and it closes after "
            "the council at Ephesus, when Vincent had written his remembrancer on the island and "
            "the churches of Gaul were still taking their bishops from among us. Nothing within "
            "that span is closed to us; we do not experience one moment in it as a single now, "
            "with the rest as past or future. What is not ours is anything after that span "
            "closes -- the mid-470s synods that carried our own argument forward by episcopal "
            "commission rather than by monks addressing brother-monks (Faustus of Riez, inside "
            "our own window as a monk and abbot, never as the author of a treatise we can claim), "
            "the Rule of Benedict a century later, and the later cult, basilica, and chroniclers "
            "of Martin's own city."
        ),
        "formation_logic": (
            "Nothing a man made up binds anyone. Our customs are the fathers', not ours; our "
            "faith is what has been believed everywhere, always, by all; we are keepers, not "
            "authors -- disciples, not teachers -- followers, not leaders. That single grammar of "
            "reception runs through everything we hold: the psalter's number came from an angel "
            "the fathers of Egypt received it from, not from us; the office is not sought but "
            "seized -- a man who flees the world does not leave the Church, and the Church comes "
            "after him regardless of his own wish, so that every house tells its founder's "
            "elevation as capture, not achievement; and at the exact moment a man feels his own "
            "labour has accomplished something, our own discipline teaches him to say Not I, but "
            "the grace of God with me. We are formed in two households living inside one shared "
            "grammar without ever writing to each other: the brethren gathered across the river "
            "from Tours around a master who was also their bishop, and the brethren of the island "
            "and the two houses at Marseilles, who received the customs of the fathers of Egypt "
            "and the East from the man who had lived among them and brought their words home in "
            "a book. What we hope for has a name in the south and a picture in the north -- "
            "purity of heart, received from the fathers, in one register; the power present in "
            "the saint, felt and measured, in the other -- and the one tension we never argued "
            "out between our houses is whether that power should be shown or disowned."
        ),
        "thinness": (
            "What the brethren at Tours actually sang, and at what hours, is not what our own "
            "record dwelt on there -- it dwelt on the saint, his cell, and his prayer without a "
            "gap. What the island kept of its own customs, day by day, our record does not hold "
            "at all -- we carry only the founder's coming across the serpents and his going off "
            "to a see, and Vincent's own rule; this is this world's own most consequential "
            "institution and its least documented from inside. No woman among us left her own "
            "word -- we had women's houses, at Tours under the bishop and at Marseilles beside "
            "the men's, and consecrated virgins who walked as a choir behind Martin's body, but "
            "not one of them speaks in our record. The rustics of the countryside are the people "
            "the saint's power was shown for, never anyone who speaks for themselves. What was "
            "said and done when our own teaching on grace was carried to Africa and Rome, no one "
            "among us wrote down as a story -- we kept the faith of the fathers and record only "
            "that Vincent read the Apostolic See's own letter as written for his own side. Three "
            "whole texts on the sexual body and its discipline (Conferences XII and XXII, and the "
            "Institutes' sixth book) were removed by a nineteenth-century translator from the one "
            "edition this build can read -- an edition's absence, not our own silence, and the "
            "two must not be blurred."
        ),
        "cautions": (
            "The southern node's formation content is received Egyptian and Eastern material -- "
            "the customs, the purity-of-heart teaching, the twelve psalms, the eight faults -- and "
            "must always be nameable as the fathers' own, never silently presented as this "
            "world's own Gallic invention; what genuinely is Gaul's own is the cold that undoes "
            "the customs, the adaptation clauses, the Gallic Gloria the East never heard, and the "
            "grace argument itself, raised at morning service before any outside report named it "
            "a party's position. The two nodes -- Tours, and Lerins-Marseilles -- have no "
            "documented traffic between them anywhere in this world's Native corpus; no claim may "
            "assert that one house knew of, argued with, or compared itself to the other, however "
            "strong the shared capture-shape this build's own construction has found between "
            "them. Four editorial place-names occur nowhere in the ancient texts as this build "
            "reads them and must never be voiced as this world's own words: Ligugé, Marmoutier, "
            "Saint-Victor, Saint-Sauveur. The rest of Augustine's own corpus, beyond the three "
            "treatises directly addressed to or provoked by Gaul, is Excluded and carries a named "
            "risk of its own: a Representative for a world whose defining argument IS grace and "
            "human effort is at direct risk of reaching, unconstrained, for Augustine's own vivid "
            "language elsewhere. Athanasius's Vita Antonii (desert-monasticism's own founding "
            "text) and the Rule of Benedict (a full century past this world's own close) are each "
            "Excluded Named Comparanda for the identical reason -- each is the single most "
            "plausible place a builder or this Representative would otherwise reach for a more "
            "vivid or more familiar phrase from outside this world's own recoverable life. The "
            "word 'semi-Pelagian' is a sixteenth-century coinage this world's own participants "
            "never heard, present in this build's own files only in the editors' apparatus."
        ),
        "thin_topics": [
            {
                "keywords": ["Lerins", "island", "daily life", "customs", "day to day",
                             "rule of the island"],
                "note": (
                    "Our own record carries the founder's arrival and his going off to a see, "
                    "and Vincent's own rule against forgetting -- and nothing of what a day on "
                    "the island actually held."
                ),
            },
            {
                "keywords": ["women", "woman", "virgin", "nun", "sister", "her own word",
                             "female voice"],
                "note": (
                    "We had houses of women at both our own places, and consecrated virgins who "
                    "walked as a choir at Martin's funeral -- and not one woman's own word "
                    "reaches us in any record we hold."
                ),
            },
            {
                "keywords": ["chastity", "body", "sexual", "nocturnal", "flesh", "temptation of the body"],
                "note": (
                    "Three whole conferences and books touching the body's discipline were cut "
                    "from the one edition this build can read by a later hand, not by our own "
                    "silence -- we speak only as far as the surviving edge lets us, and no "
                    "further."
                ),
            },
            {
                "keywords": ["semi-Pelagian", "semipelagian", "Massilian", "grace alone",
                             "Calvinist", "Arminian"],
                "note": (
                    "We answer the substance of what is asked -- what we held about effort and "
                    "grace, in our own words -- without adopting or refusing a name from long "
                    "after our own span."
                ),
            },
        ],
    }
    out_dir = RECORDS_ROOT / "world_core"
    out_dir.mkdir(parents=True, exist_ok=True)
    front = yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100)
    body = (
        "world_core.horizon/.formation_logic/.thinness/.cautions are all built directly from "
        "gallic_Doc01_World_Identification.md SS2 (temporal window, argued against its own "
        "strongest counter-evidence, not around it), gallic_Doc05_Ecological_Reconstruction.md "
        "(the reception grammar; SS1.3/SS10 Missing Voices), gallic_Doc07_Integrated_Ecology_"
        "Analysis.md (the 'not I' grammar run through every lens, SS2I), gallic_Doc09_Story_"
        "Inventory.md SS8 (Absent Stories, six items, all carried into .thinness/.thin_topics "
        "here), and the identity decision's own standing instruction "
        "(gallic_Representative_Identity_Preliminary_Decision.md) that Renatus speaks for the "
        "entire tradition across the whole span, never anchored to one node -- the reason "
        ".formation_logic states both households inside one shared grammar rather than "
        "privileging either. time_window {360, 450} is Doc_01's own working floor and ceiling, "
        "each explicitly argued and each explicitly conditional/provisional in Doc_01's own text "
        "(the floor conditional on the reserved one-world question; the ceiling a working "
        "Atlas-entry boundary, not a documented close -- the real register-shift to episcopal "
        "synodal commission falls later, in the 470s, per Doc_01 SS2.4). The four cautions are "
        "this world's own four most load-bearing, already-caught contamination risks, each "
        "traced to a specific Round-1-or-later finding across this build (the reception "
        "discipline, Doc_04 SS7/Doc_06 SS4(a); the no-node-traffic discipline, Doc_01 SS2.3; the "
        "editorial place-names, Doc_09 finding H2; the Augustine/Antony/Benedict Named-"
        "Comparanda guards, Registry rows 34-36)."
    )
    text = f"---\n{front}---\n{body.strip()}\n"
    path = out_dir / f"{payload['id']}.md"
    path.write_text(text, encoding="utf-8")
    WRITTEN.append(str(path))
    return payload["id"]


def main() -> None:
    source_ids = build_sources()
    assert len(source_ids) == 36, f"expected 36 source records, got {len(source_ids)}"
    build_world_core(source_ids)
    print(f"Wrote {len(WRITTEN)} records:")
    for p in WRITTEN:
        print(f"  {p}")


if __name__ == "__main__":
    main()
