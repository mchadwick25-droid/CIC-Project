"""B-1 (S2.1): Donatism (don) source + world_core records.

WHAT THIS SCRIPT DOES. Converts this world's completed Phase A construction
documents into record-native records under records/don/{source,world_core}/,
per the live schema (engine/m1/schemas.py) and gate battery (engine/m1/gates.py).
This is the FIRST record-authoring pass for this world; no don records existed
before this script ran. This is B-1 of a 9-step record-native build pipeline
(B-1 through B-9) -- source records and the world_core record only. Lexicon,
gravity, contested-claim, and every other record type are later steps' own
work, not touched here. The governing process document (Ministry/Technology/
CiC_Record_Native_World_Build_Process_V1_3.md) describes a retired backend
(cic-poc/backend/wrs/, s62_<code>_s2X.py) that no longer exists in this repo;
this script targets the live system instead, confirmed directly against
engine/m1/schemas.py and engine/m1/gates.py before writing anything, and
follows World-Builds/Cappadocian/scripts/wb_cappadocian_s21.py's own docstring
and code-pattern discipline (the one surviving, real, current template for
this exact step) -- read in full before this script was written, not touched
by it, and not itself re-run or edited here.

INPUTS, mapped to OUTPUTS, precisely:
  - World-Builds/Donatism/Source_Registry.md (56 numbered rows, one markdown
    table) -> the 41 `source` records (ROWS below) whose own row is judged
    VENDORED (see "VENDORED VS NOT" below) and whose own Boundary Status is
    Native, not Excluded. 15 rows are not converted: 5 are Excluded as a
    Named Comparandum (row 29, Novatian) or simply not vendored despite being
    Native (rows 22, 23, 24, 25, 26, 28, 34, 35, 36, 42, 43, 44, 45, 46 -- 14
    rows of secondary scholarship, an epigraphic/archaeological generality,
    or a contested-transmission narrative, none backed by a file this
    session found under cic/texts/).
  - Doc_01_World_Identification_Boundaries_Orientation.md SS1-SS2 ->
    world_core.time_window, .horizon (the 311/312-439 boundary and its own
    reasoning; the world's own file-code `don`, stated at Doc_01 line 4).
  - Doc_07_Integrated_Ecology_Analysis.md SS2I (Formation Logic) ->
    world_core.formation_logic.
  - Doc_02_Source_Ecology.md SS6 (Source Asymmetries and Missing Voices), SS8
    (Confidence Map), Doc_07 SS7 (Gaps and Limits), and Doc_09_Story_Inventory.md
    SS8 (Absent Stories) -> world_core.thinness / .cautions / .thin_topics.
  - cic/corpus-map/donatism.yaml (34 works, not the ~35 this step's own launch
    instructions estimated -- an exact count, corrected here) -> cross-checked
    against every vendored row below for role (context/tradition/antecedent)
    and file identity; discrepancies against Source_Registry.md are named in
    "DISCREPANCIES" below, not silently resolved either way.

VENDORED VS NOT -- the one judgment call this script's own launch instructions
name explicitly and require named here: only rows this script confirms are
backed by a real file under cic/texts/ become source records this step, NOT
every Native row (unlike Cappadocian's own precedent at this same step, which
emitted every Native row, vendored or not, into a five-bucket rights_status).
This world's own launch instructions are explicit that this step draws the
line at vendored-ness itself, not at Boundary Status alone, so this script
follows that instruction rather than Cappadocian's own broader precedent.
Determining "vendored" was NOT a single mechanical string search, because
Source_Registry.md's own prose is inconsistent about restating a file path
in every row: some rows bold **Vendored** with the cic/texts/ path inline
(the majority, rows 14-21, 27, 30-33, 37-41, 47-56); others rely silently on
cic/corpus-map/donatism.yaml's own source_file field for the same fact,
never repeating a cic/texts/ path in the row's own prose at all (rows 1, 2,
5, 7-13) -- this script cross-checked every one of those against the corpus
map directly and confirmed the corpus map's own source_file exists on disk
before treating the row as vendored. Three further rows needed a specific
reading of their own Verification Note rather than either mechanical check:
row 12 (Petilian's letters exist only as quotations inside row 4's own
vendored file, not as an independent text -- judged vendored on that basis,
via row 4's file); row 14 (the row's own named edition, Lancel's SC/CCSL
critical text, is NOT vendored, but the row's own 2026-09-07 update states
the same acts are separately, substantively preserved in row 55's Migne
file -- judged vendored via that cross-reference, not via row 14's own
named edition); row 32 (Gregory the Great's Register is explicitly
"partially vendored via row 54" -- judged vendored on that stated basis,
not as the complete critical edition the row's own Source column names).
Five rows are Type S (secondary scholarship) but ARE vendored because the
scholarly work itself is the thing sitting in cic/texts/, not a claim about
an unvendored primary text: row 31 (a 19th-century Prolegomena bound inside
the same vendored NPNF104 file as rows 3/4), and rows 40, 49, 52, 53
(Monceaux and Boyd monographs, themselves vendored files). Every file this
script cites was independently checked this same session (grep against the
file's own header) to confirm it exists under cic/texts/ and states Public
Domain with no CC BY or other open-license marker -- not assumed from either
the Registry's or the corpus map's own prose alone.

MECHANICAL vs AUTHORED, field by field:
  - id, world_id, record_type, schema_version, status, register, canon_cells:
    MECHANICAL -- fixed per envelope convention. register="etic" for every
    source record (a source record describes an external text, not this
    world's own first-person voice, matching hal/cappadocian precedent).
    canon_cells=[] throughout -- no canon-cell tagging work has happened yet
    at this build step.
  - author / work / edition: AUTHORED, per row, by hand, splitting the
    Registry's own single free-text Source column (which mixes author,
    work-with-scope, and sometimes a vendored file path or translator/press/
    year) into three schema fields. Several rows have no author in the
    ordinary sense (row 27, an anonymous epigraphic acclamation; row 12,
    Petilian's own words known only as Augustine's quotations) or represent
    a datum attested across two already-separately-recorded works rather
    than a standalone text of its own (row 30, Lucilla and a second,
    unnamed woman, attested across rows 1 and 6's own files) -- each such
    row required reading its own Verification Note to phrase author/work
    honestly rather than leaving the schema's required, non-blank fields
    empty or fabricating specificity the Registry itself does not have.
  - rights_status: AUTHORED via the single RIGHTS["pd"] entry below. Every
    one of the 17 distinct files this world's 41 vendored rows cite was
    independently checked this session (grep against the file's own
    provenance header, not the Registry's or corpus map's own prose) and
    confirmed Public Domain with zero CC BY hits -- so, unlike Cappadocian's
    five-bucket rights system (which had to carry not-yet-acquired and
    in-copyright rows too), this world's 41 vendored rows need only one
    rights bucket. gate_edition_rights_consistency was checked against this
    directly before writing: it would fire only if a cited file's own
    header states an open licence rather than public domain, and none of
    the 17 files this script cites does.
  - attribution_status: AUTHORED per row. Default "attributed". A
    descriptive phrase (never forced into a binary the schema does not
    require) wherever the Registry's own Verification Note flags a genuine
    authorship or identity question: row 12 (Petilian's letters, recoverable
    only through his opponent's own selection), row 30 (Lucilla and a second
    woman, attested only through hostile/incidental narration, not authors
    of a text of their own), row 50 (the Passio Donati's proposed preacher,
    "possibly Donatus the Great" per Monceaux, explicitly not confirmed and
    contested against Mabillon's own non-identification).
  - discovery_channel: AUTHORED per row via dc(row, note), naming the
    Registry's own row number and a short paraphrase of that row's own
    Discovery column -- deliberately NOT Cappadocian's own fixed four-value,
    verification-state-keyed vocabulary (verified-direct/-via-authority/
    named-not-rechecked/unverified mapped onto one fixed sentence each).
    This registry's own Discovery column is far more heterogeneous than
    Cappadocian's -- corpus-map citation, direct grep-and-read, WebSearch,
    Mark's manual DOCX upload, a sibling research session's own find, a
    direct network fetch -- and collapsing that variety into four fixed
    sentences would lose real, checkable provenance detail this Registry
    itself records. external_ids carries the same row number in queryable
    form: {"don_source_registry_row": num}.
  - confidence.citation_specificity: MECHANICAL -- copied directly from the
    Registry's own Confidence (A/B/C; no D or E rating appears among this
    world's 41 vendored rows) column, per that Registry's own stated
    calibration rule (Source_Registry.md's own opening paragraph): A is
    used where the row's own Licensed-For content was itself directly read
    and verified against the vendored text this session; B where a specific
    work or locus is named accurately but was not independently re-checked
    against the vendored text this session at all; C where a source is tied
    to a real author or work but no specific locus is pinpointed.
  - confidence.verification_state: AUTHORED, but via one explicit,
    mechanical-once-decided rule, stated here so it can be checked against
    the Registry text directly, and DIFFERENT from Cappadocian's own rule in
    one respect named below:
      * Registry Confidence A -> verified-direct.
      * Registry Confidence B -> verified-via-authority, UNIFORMLY. This is
        the one place this script's rule differs from Cappadocian's own:
        Cappadocian's B tier needed a hedge-detection step (two rows with
        the same letter could land in different verification states,
        depending on whether the row's own note hedged the specific
        citation). This Registry's own B tier already builds "not
        independently re-checked against the vendored text this session"
        into its own definition (see the calibration rule quoted above) --
        every B row this script emits is, by that definition alone, both
        genuinely vendored (per "VENDORED VS NOT" above) and specifically
        named/locatable, which is exactly verified-via-authority's own
        meaning (a real, checkable text stands behind the claim, just not
        reopened this session) with no further per-row hedge-reading
        needed.
      * Registry Confidence C -> named-not-rechecked, uniformly (tied to a
        real author/work, no specific locus pinpointed -- the same rule
        Cappadocian's own script used for its C tier).
  - confidence.evidentiary_weight: AUTHORED per row from the Licensed-For
    column. "load-bearing" default for rows explicitly grounding a specific
    named claim this world's Doc_0X material rests on. "corroborating" for
    rows licensed as secondary or parallel support to a load-bearing row.
    "illustrative" for rows this Registry's own prose states are "not yet
    licensed for any specific claim" or "named as an open item for a future
    revision pass" -- rows 21, 32 (no, see below), 52, 53 specifically (the
    Liber Genealogus and the two Monceaux tomes whose own body text has not
    yet been read for any claim). "contested" (a real enum value, used
    narrowly) only for row 50, where the source OBJECT's own dating and
    proposed authorship, not merely a claim drawn from it, are reported from
    two disagreeing named authorities and deliberately not resolved.
  - confidence.formation_confidence: AUTHORED per row, via a rule this
    script adds to Cappadocian's own (Cappadocian's script did not need this
    distinction, because none of its "Documented" candidates were secondary
    scholarship): "Documented" is reserved for Type P/M (primary-text or
    material) rows this record can honestly pair with verified-direct AND
    whose own underlying fact is a plain, uncontested textual or epigraphic
    reality (a law's own wording, an inscription's own text, a letter's own
    content) -- never for Type S (secondary scholarship) rows, even where
    the row's own EXISTENCE and TEXT were verified-direct this session,
    because confirming that a modern monograph exists and was opened is not
    the same claim as its own historical content being settled fact. Type S
    rows are capped at "Widely Accepted" by default, or "Dominant Modern
    Reconstruction" where the row specifically supersedes an older account
    on a contested dating/identification question with real force (row 40,
    Monceaux's Tome V, against Mabillon's own narrower apparatus for the
    Passio Donati's dating). "Contested" is reserved for row 50 itself,
    whose own dating and proposed authorship this record deliberately does
    not resolve between two disagreeing authorities. Every other row
    defaults to "Widely Accepted": a text's existence and basic content
    being standard and undisputed, without this session's own independent
    recheck, is Widely Accepted, not Documented.
  - confidence.divergence_note: null by default; populated with a short,
    honest sentence wherever a row's own evidentiary_weight or
    formation_confidence needs explaining against its own verification_state
    or confidence tier (row 21, illustrative despite verified-direct; row
    32, load-bearing but only partially vendored; row 50, contested despite
    verified-direct; rows 52/53, illustrative despite verified-direct, at
    title/chapter-heading level only; row 54, load-bearing but a themed
    selection, not the complete Register; row 55, load-bearing but most of
    a ~5MB volume unread, with an unreconciled possible file-duplication
    question named in its own row). gate_confidence_crosscheck's own rule
    (formation_confidence=Documented + null divergence_note requires
    verification_state=verified-direct) is satisfied by construction: every
    "Documented" row this script emits also carries verified-direct,
    checked in conf() itself as a hard assertion, not left to hope.
  - sources / relations (on EACH source record): left empty by design, the
    same judgment call Cappadocian's own script names and for the same
    reason -- this step's own brief expects gate_referential/gate_reciprocity
    trivially clean, and populating cross-references between source records
    now would require reciprocal `relations` entries for no benefit this
    step needs. The world_core record DOES populate `sources`, referencing a
    handful of the richest source ids created in this same run, which
    resolve cleanly under gate_referential since both records are emitted
    together.

DISCREPANCIES between Source_Registry.md and cic/corpus-map/donatism.yaml,
named rather than silently resolved either way:
  1. The corpus map lists three works using the same vendored file as rows
     17/18/37/39/56 (augustini_scripta-contra-donatistas-pars-i-iii_
     petschenig1908-1910.txt) that have NO Source_Registry.md row of their
     own at all: "Contra (Adversus) Fulgentium Donatistam," "De Baptismo
     (libri septem)" (the Latin critical text of row 3's own work), and "De
     Unico Baptismo contra Petilianum" (companion to row 4). Not converted
     to source records here -- no Registry row licenses them, and this
     step's own brief converts Registry rows, not corpus-map entries
     directly -- but named as a gap a future Doc_02/Registry revision pass
     could close, the same way the corpus map itself already names three
     Monceaux tomes as "an open item for a future Doc_02 revision pass."
  2. Registry row 56 (Contra Gaudentium, added 2026-09-08) has no
     corpus-map entry at all -- found and vendored after the corpus map's
     own most recent merge, per the Registry's own dated note.
  3. Registry row 22 (Acts of the Abitinian Martyrs / Acta Saturnini) has no
     corpus-map entry and no vendored file this script found -- carried at
     field knowledge only, excluded here as not-vendored.
  4. Three files this script confirmed exist under cic/texts/ are cited by
     NEITHER a Source_Registry.md row nor a corpus-map entry for donatism:
     possidius_vita-augustini_weiskotten1919.txt,
     cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt (a Latin critical
     edition of Cyprian, distinct from the anf05 English translation rows
     7-10 actually cite), and augustine_epistulae-critical_goldbacher-
     csel57-pars4.txt (a Latin critical edition of Augustine's letters,
     distinct from the npnf101 English translation rows 5/6/30/47 actually
     cite). Not converted to source records here for the same reason as
     item 1 above -- no Registry row licenses them -- named as a possible
     acquisition-manifest/Registry gap for a future pass, not silently
     used.

WORLD_ID: "don", Doc_01's own stated file-code (line 4: "**World file-code:**
`don`"), not minted by this script -- unlike Cappadocian, which had to choose
a world_id because its world had never been given one anywhere in the live
system. No judgment call needed here.

SCRIPT LOCATION: World-Builds/Donatism/scripts/, matching Cappadocian's own
precedent exactly (build tooling for one world, reading that world's own
documents by relative path, with no reason to live inside the shared engine).

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells (no canon-cell tagging work
has happened for this world yet); register `don` in records/worlds.yaml
(B-9, a later step); run the M2 compiler; touch World-Builds/Cappadocian/ or
any file outside World-Builds/Donatism/scripts/, records/don/source/, and
records/don/world_core/; convert the 14 not-vendored Native rows or the one
Excluded row into source records (see "INPUTS" above); resolve either of the
two genuinely open Registry questions named in cautions below (the Passio
Donati's own dating/authorship; whether the pl11 Migne volume's own
"Monumenta vetera" section duplicates the already-vendored monumenta-vetera-
donatistarum_migne-pl8.txt file, row 55's own still-open question).
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]  # .../cic-project
RECORDS_ROOT = REPO_ROOT / "records" / "don"

WORLD_ID = "don"
SCHEMA_VERSION = 2

# ---------------------------------------------------------------------------
# Shared edition strings for vendored files cited by multiple rows. Every
# filename below was checked directly against `ls cic/texts/` and its own
# provenance header (grep for "public domain" / "cc by") this session, not
# copied blind from the Registry's or corpus map's own prose.
NPNF101 = ("Nicene and Post-Nicene Fathers, 1st series, vol. 1 (Augustine: Confessions, "
           "Letters), ed. Schaff, vendored as cic/texts/npnf101_augustine-confessions-letters.xml")
NPNF102 = ("Nicene and Post-Nicene Fathers, 1st series, vol. 2 (Augustine: City of God, "
           "Christian Doctrine), ed. Schaff, vendored as "
           "cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml")
NPNF104 = ("Nicene and Post-Nicene Fathers, 1st series, vol. 4 (Augustine: Anti-Manichaean, "
           "Anti-Donatist Writings), ed. Schaff, vendored as "
           "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml")
NPNF214 = ("Nicene and Post-Nicene Fathers, 2nd series, vol. 14 (The Seven Ecumenical "
           "Councils), ed. Schaff, vendored as cic/texts/npnf214_seven-ecumenical-councils.xml")
ANF05 = ("Ante-Nicene Fathers, vol. 5 (Hippolytus, Cyprian, Caius, Novatian, Appendix), ed. "
         "Roberts & Donaldson, vendored as cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml")
PETSCHENIG = ("Michael Petschenig (ed.), Sancti Aureli Augustini Scripta contra Donatistas, "
              "CSEL 51 and 53 (Vienna: Tempsky / Leipzig: Freytag, 1908 and 1910), vendored as "
              "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt")
MONUMENTA_PL8 = ("J. Mabillon / J.-P. Migne (eds.), Monumenta Vetera ad Donatistarum historiam "
                 "pertinentia, in Patrologia Latina vol. 8, vendored as "
                 "cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt")
CIL8 = ("Corpus Inscriptionum Latinarum, vol. VIII, Supplementum, Pars II (Numidia), ed. Cagnat "
        "& Schmidt (Berlin, 1894), vendored as "
        "cic/texts/cil8-supplementum-numidiae_cagnat-schmidt1894.txt")
THEODOSIANUS16 = ("Th. Mommsen & Paul M. Meyer (eds.), Theodosiani Libri XVI, Voluminis I Pars "
                  "Posterior: Textus cum Apparatu (Berlin, 1905), vendored as "
                  "cic/texts/theodosianus-16_mommsen-meyer1905.txt")

RIGHTS = {
    "pd": ("public-domain; vendored in cic/texts/. This script's own authoring session "
           "(2026-09-10) directly checked the vendored file's own provenance header for every "
           "file cited below (grep for 'public domain' / 'cc by' against each file's own text) "
           "and confirmed each states Public Domain, with no CC BY or other open-license marker "
           "found in any of the seventeen distinct files this world's Registry rows cite -- not "
           "assumed from the Registry's or corpus map's own prose alone."),
}


def dc(row: int, note: str) -> str:
    return f"Source Registry row {row}; {note}"


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


def emit_source(row, slug, author, work, edition, rights_key, attribution, discovery_note,
                 cite, verify, weight, formation, divergence, body):
    payload = {
        "id": f"don.source.{slug}",
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
        "discovery_channel": dc(row, discovery_note),
        "external_ids": {"don_source_registry_row": row},
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

    # --- Rows 1-2: Optatus of Milevis and his own Appendix ------------------
    ids["optatus-against-donatists"] = emit_source(
        1, "optatus-against-donatists", "Optatus of Milevis",
        "Against the Donatists, Books I-VII (c. 366-367; a revised second edition c. 385)",
        "English translation by O.R. Vassall-Phillips (Longmans, Green & Co., 1917), vendored as "
        "cic/texts/optatus_against-the-donatists.txt", "pd", "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: context",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "This world's earliest substantial narrative source, hostile and external but contemporary "
        "and primary (Doc_01 SS2) -- grounds the schism-origins narrative and the World #6/#8 "
        "boundary reasoning. Three dates for the work's own two-edition history appear across this "
        "build's own sources (c. 366-367/rev. 385; 'about 370'; 'c. 366-393 CE') and are not "
        "reconciled here, pending the translator's own Preface or a critical apparatus (Ziwsa, row "
        "38, vendored but not yet read for this purpose; Labrousse, row 44, not acquired). Lucilla's "
        "own role in the schism's founding (I.16) is carried at row 30's own record.")
    ids["optatus-appendix-of-documents"] = emit_source(
        2, "optatus-appendix-of-documents", "Optatus of Milevis (compiler)",
        "Optatus's own Appendix of Documents: Acta Purgationis Felicis (314), Gesta apud "
        "Zenophilum (320), Constantine's letters, the Council of Arles' 314 letter to Silvester, "
        "Acts of the Council of Cirta (305, date disputed), Anulinus's relatio (313)",
        "vendored as cic/texts/optatus_against-the-donatists.txt (same volume as row 1)", "pd",
        "attributed", "corpus map / cic/corpus-map/donatism.yaml, role: context",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "The initiating events of the schism (Doc_01 SS5, Cell 1A/1B) and the 313 appeal to "
        "Constantine (Doc_01 SS5, SS6), transmitted as a documentary appendix by Optatus's own "
        "selecting hand -- the contents are court acts and correspondence, but the selection and "
        "transmission are Optatus's own act, sitting inside this world's Author Gravity "
        "concentration rather than outside it.")

    # --- Rows 3-6, 47: Augustine's anti-Donatist and Donatist-subject corpus
    ids["augustine-on-baptism-against-donatists"] = emit_source(
        3, "augustine-on-baptism-against-donatists", "Augustine of Hippo",
        "On Baptism, Against the Donatists (7 books, c. 400)", NPNF104, "pd", "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: tradition; Book I chs. 1, 5: direct "
        "text search / grep and read against the vendored file, 2026-09-01",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "The central treatise on the validity of schismatic baptism and a major conduit for "
        "Cyprian, argued through the acts of Cyprian's own baptismal councils at length (corpus "
        "map role: tradition). Book I chapters 1 and 5 were directly read and character-verified "
        "this session, quoted for the Maximianist rebaptism-consistency argument (Doc_02 SS1); the "
        "remaining six books were not independently re-collated and are not the basis of any "
        "specific claim this world's construction draws from this row.")
    ids["augustine-answer-to-letters-of-petilian"] = emit_source(
        4, "augustine-answer-to-letters-of-petilian", "Augustine of Hippo",
        "Answer to the Letters of Petilian (3 books)", NPNF104, "pd", "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: tradition; Optatus Gildonianus and "
        "Felicianus passages: direct text search / grep and read against the vendored file, "
        "2026-09-01",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "The fullest surviving Donatist voice in the vendored corpus, preserved entirely inside its "
        "own refutation -- Petilian's own quoted words are carried at row 12's own record. The "
        "Optatus Gildonianus passages (II.9, II.23, II.84) and the Felicianus of Musti passage "
        "(II.52) were read in context this session; Optatus Gildonianus's identification as a "
        "Donatist bishop, not an imperial official, is stated in row 3's own companion volume "
        "rather than in this row's own endnotes. The remainder of the work was not independently "
        "re-collated.")
    ids["augustine-correction-of-donatists-letter-185"] = emit_source(
        5, "augustine-correction-of-donatists-letter-185", "Augustine of Hippo",
        "The Correction of the Donatists (Letter 185, c. 417)", NPNF104, "pd", "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: tradition",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "The classic defense of imperial coercion against the Donatists, addressed to the tribune "
        "Boniface -- grounds the imperial-coercion defense and the World #6 boundary discussion "
        "(Doc_01 SS6). Its own near-fatal attack account against the Catholic bishop Maximianus of "
        "Bagai (404) is a rare hostile-side allegation this world has no surviving side of its own "
        "to answer (Doc_09 SS8 item 3). Addressee and date confirmed against Doc_01 SS2; not "
        "independently re-checked against the vendored text's own wording this session -- carried "
        "via the corpus map's own source_file, which this script directly confirmed exists and is "
        "public domain.")
    ids["augustine-donatist-correspondence-eleven-letters"] = emit_source(
        6, "augustine-donatist-correspondence-eleven-letters", "Augustine of Hippo",
        "Augustine's Donatist correspondence: Letters XXIII, XLIII, XLIV, LIII, LXXVI, LXXXVII, "
        "LXXXVIII, LXXXIX, XCIII, CXXXIX, CLXXIII (11 letters)", NPNF101, "pd", "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: context; Letter LXXXVII and Letter "
        "XLIII: direct text search / grep and read against the vendored file, 2026-09-01",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "The broader Donatist-Caecilianist exchange, split from a 168-letter volume by the corpus "
        "map's own div3 markup (Mark's 2026-08-26 ruling) and classified role: context, distinct "
        "from the anti-Donatist treatises' own role: tradition. Letters LXXXVII (the Maximianist "
        "affair's conciliar-authority reproach, SS6-SS8 only) and XLIII SS26 (the second, unnamed "
        "woman parallel to Lucilla, carried at row 30) were both read in full this session; the "
        "remaining nine letters were not independently re-collated. Letter LXXXVIII's own body text "
        "is Doc_09's source for the presbyter-beating allegation against the Donatist bishop "
        "Proculeianus (Doc_09 SS8 item 3).")
    ids["augustine-letter-51-to-crispinus"] = emit_source(
        47, "augustine-letter-51-to-crispinus", "Augustine of Hippo",
        'Letter LI, "To Crispinus" (a.d. 399 or 400)', NPNF101, "pd", "attributed",
        "direct text search / grep and read against the vendored file, 2026-09-01",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "The mainstream Donatist party's own reception of Maximianist clergy without reordination, "
        "and Augustine's direct testimony to that party's own use of civil courts and armed force "
        "against the Maximianists (Doc_02 SS1) -- directly read and quoted this session ('you "
        "restored some of them without re-ordination'). Letter LXX, on the same subject, is present "
        "in the vendored volume only as an editorial headnote left untranslated as covering the "
        "same ground -- a materially different status from unvendored, and the route by which this "
        "letter was found.")

    # --- Rows 7-11: the Cyprianic antecedent corpus and its conciliar record
    ids["cyprian-epistles"] = emit_source(
        7, "cyprian-epistles", "Cyprian of Carthage", "Epistles", ANF05, "pd", "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: antecedent, ruled 2026-08-26",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "Antecedent, not tradition (corpus map role: antecedent, ruled 2026-08-26): Cyprian died "
        "fifty years before the schism and was never a Donatist, but both sides argued from his own "
        "rebaptism practice and purity ecclesiology -- grounds the A1/A2 continuity reasoning "
        "(Step0 SS2) and the rebaptism-theology origin (Doc_01 SS5). Not independently re-collated "
        "this session.")
    ids["cyprian-on-the-lapsed"] = emit_source(
        8, "cyprian-on-the-lapsed", "Cyprian of Carthage", "On the Lapsed (De Lapsis)", ANF05,
        "pd", "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: antecedent, ruled 2026-08-26",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "Antecedent tradition (corpus map role: antecedent, ruled 2026-08-26) for the traditio/"
        "lapsed-clergy theological background this schism reopens (Doc_01 SS5). Not independently "
        "re-collated this session.")
    ids["cyprian-on-the-unity-of-the-church"] = emit_source(
        9, "cyprian-on-the-unity-of-the-church", "Cyprian of Carthage",
        "On the Unity of the Church (De Unitate)", ANF05, "pd", "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: antecedent, ruled 2026-08-26",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "Antecedent tradition (corpus map role: antecedent, ruled 2026-08-26) for the ecclesial-"
        "purity/unity theological background. Written against the Novatianist schism among others "
        "(the corpus map's own note) -- the same shared-volume proximity that makes row 29's "
        "Novatian comparandum a live temptation to guard against, not evidence of continuity "
        "between the two schisms.")
    ids["cyprian-seventh-council-of-carthage-rebaptism"] = emit_source(
        10, "cyprian-seventh-council-of-carthage-rebaptism", "The Cyprianic corpus's own record",
        "The Seventh Council of Carthage (256, on the rebaptism of heretics), under Cyprian",
        ANF05, "pd", "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: antecedent, confidence: assigned",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "The Donatists' own standing proof that African tradition required rebaptism of those "
        "baptized outside the church (the corpus map's own note) -- rebaptism precedent and A1/A2 "
        "continuity reasoning. Kept distinct from row 11's own record of the same event, per Doc_02 "
        "SS1/SS9 item 6 -- not to be merged or cited at row 11's confidence.")
    ids["acts-of-council-of-carthage-under-cyprian"] = emit_source(
        11, "acts-of-council-of-carthage-under-cyprian", "The council's own acts, as transmitted",
        "The Acts of the Council of Carthage under Cyprian (256, on baptism)", NPNF214, "pd",
        "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: tradition, confidence: provisional",
        "C", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The same 256 rebaptism council as row 10, told from a conciliar-history vantage (corpus "
        "map role: tradition, confidence: provisional) -- kept distinct from row 10 and not to be "
        "cited at row 10's confidence (Doc_02 SS1/SS9 item 6). The vendored volume's own section "
        "heading dates the council 'a.d. 257'; this record follows the corpus map's own "
        "September-256 dating as historically established and records the volume's own heading as "
        "a discrepancy worth noting, not a second date to reconcile.")

    # --- Row 12: Petilian, quoted only -------------------------------------
    ids["petilian-of-constantina-letters-quoted"] = emit_source(
        12, "petilian-of-constantina-letters-quoted", "Petilian of Constantina (Donatist bishop "
        "of Cirta)",
        "Petilian's own letters, as quoted and answered inside Augustine's Answer to the Letters "
        "of Petilian (row 4)", NPNF104, "pd",
        "attributed, but recoverable only through his opponent's own selection and framing -- no "
        "independent text of Petilian's own letters survives outside this quotation",
        "corpus map / cic/corpus-map/donatism.yaml (via row 4's own work entry)",
        "C", "named-not-rechecked", "load-bearing", "Widely Accepted", None,
        "This world's own fullest surviving primary voice in the vendored corpus (Doc_02 SS2) -- "
        "not independently checkable outside Augustine's own quotation. Paraphrase is distinguished "
        "from direct quotation where checkable, but no claim of completeness is made: Augustine's "
        "own selection, made for the purpose of refutation, is this record's only access to "
        "Petilian's argument (Doc_01 SS7 item 1).")

    # --- Row 13: the African Church's own 419 canons -----------------------
    ids["code-of-canons-african-church-419"] = emit_source(
        13, "code-of-canons-african-church-419", "The Council of Carthage, 419 (compiling body)",
        "The Code of Canons of the African Church (Council of Carthage, 419)", NPNF214, "pd",
        "attributed",
        "corpus map / cic/corpus-map/donatism.yaml, role: context, confidence: provisional",
        "C", "named-not-rechecked", "corroborating", "Widely Accepted", None,
        "The Catholic side's own institutional record of Donatist-clergy reception (corpus map "
        "role: context, confidence: provisional) -- most canons originate c. 397-407, and the "
        "register compiles rather than legislates fresh (Step0_Movement_Scope_Confirmation.md SS3, "
        "B1).")

    # --- Rows 14-15: the Gesta and Tyconius ---------------------------------
    ids["gesta-collationis-carthaginiensis"] = emit_source(
        14, "gesta-collationis-carthaginiensis", "The 411 Conference of Carthage (official "
        "proceeding)",
        "Gesta Collationis Carthaginiensis (Acts of the 411 Conference), as an event and text -- "
        "the modern critical edition (Serge Lancel, Sources Chretiennes 194/195/224/373 and CCSL "
        "149A) remains in-copyright and is not vendored",
        "the same acts are separately, substantively preserved in a Migne Patrologia Latina "
        "printing, vendored as cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt "
        "(row 55's own file)", "pd", "attributed",
        "builder-prior-knowledge, cross-checked via WebSearch, 2026-09-01; corrected: direct text "
        "search / grep and read against row 55's own file, 2026-09-07",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "Donatist bishops' own recorded words at length -- Emeritus of Caesarea foremost, with at "
        "least ten of his own numbered interventions confirmed this session via row 55's file, "
        "including '268. Emeritus episcopus dixit...' (corrected 2026-09-07 from an earlier, "
        "network-access-limited 'confirmed unavailable' finding). This world's own two "
        "best-attested named Donatist figures -- Petilian via hostile quotation (row 12), Emeritus "
        "via this court transcript -- now each have a distinct, differently-mediated evidentiary "
        "channel (Doc_02 SS6). Confidence held at B, not A: the transcript's own text has not yet "
        "been read in full, and this row's own Author Gravity assessment has not yet been performed "
        "against it.")
    ids["tyconius-liber-regularum"] = emit_source(
        15, "tyconius-liber-regularum", "Tyconius", "Liber Regularum (Book of Rules)",
        "vendored as cic/texts/tyconius_liber-regularum_burkitt1894.txt; the critical edition "
        "itself is carried at row 41", "pd", "attributed",
        "builder-prior-knowledge, cross-checked via WebSearch, 2026-09-01",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "This world's own strongest surviving theological writing from within the movement's own "
        "intellectual orbit, not a hostile quotation or an outside description (the corpus map's "
        "own note) -- grounds Tyconius's own theology and the Strand Determination provisionality "
        "(Doc_01 SS4). The file's identity as the genuine Burkitt 1894 edition was confirmed this "
        "session (preface, table of contents, introduction all present), which unblocks the Author "
        "Gravity correction Doc_02 SS1 names as the single largest available to this world's own "
        "Author Gravity concentration -- but that assessment, and a reading of the seven Rules' own "
        "doctrinal content, has not itself been performed this session.")

    # --- Row 16: the Theodosian Code's own Book 16 --------------------------
    ids["codex-theodosianus-book-16"] = emit_source(
        16, "codex-theodosianus-book-16", "The Theodosian Code (imperial compilation)",
        "Codex Theodosianus, Book 16 (including 16.5.52 on the circumcelliones, and the 405 Edict "
        "of Unity)",
        "Mommsen & Meyer's 1905 critical edition, vendored as "
        "cic/texts/theodosianus-16_mommsen-meyer1905.txt (row 51's own file)", "pd", "attributed",
        "builder-prior-knowledge, cross-checked via WebSearch, 2026-09-01; direct text search / "
        "grep and read against the vendored file, 2026-09-07",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "Imperial legal record and the Circumcellions'/agonistici's own independent attestation "
        "outside hostile polemic (Step0_Movement_Scope_Confirmation.md SS2, A5) -- law XVI.5.52 "
        "(headed '412 Ian. 30') was located and read in full this session, confirmed to contain "
        "'circumcelliones argenti pondo decem' verbatim, a graduated fine schedule assessing "
        "Circumcellions a silver, not gold, fine unlike every other listed rank. The term "
        "agonistici does not appear anywhere in this file (checked directly, zero matches) -- "
        "confirmed not to be Theodosian Code vocabulary; its own source passage in Augustine's "
        "corpus remains unidentified (Doc_02 SS6, SS9). This closes a standing citation gap after "
        "five prior acquisition attempts returned the wrong volume (don_Decision_Log.md).")

    # --- Rows 17-18, 37, 39, 56: the Petschenig volume's further contents --
    ids["augustine-contra-cresconium"] = emit_source(
        17, "augustine-contra-cresconium", "Augustine of Hippo",
        "Contra Cresconium (4 books, c. 406, some scholarship as late as 409)", PETSCHENIG, "pd",
        "attributed",
        "builder-prior-knowledge (Doc_01 SS4 binding), 2026-09-01; file presence and identity "
        "confirmed via direct file check, 2026-09-01",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "Further Maximianist-schism rebaptism-argument material beyond what row 3 already "
        "establishes directly (Doc_02 SS1) -- Augustine's reply to the Donatist grammarian "
        "Cresconius, who had himself answered row 18's Contra epistulam Parmeniani. Headed 'CONTRA "
        "CRESCONIVM,' four books, confirmed present this session by its own internal Explicit/"
        "Incipit markers; the row's own specific Licensed-For claim (the fuller rebaptism argument, "
        "the Bagai proceedings) is available in the vendored text but has not itself been read this "
        "session. The Maximian named here (the deposed deacon of the Maximianist schism) is a "
        "different person from the martyr Maximian of row 20's Passio.")
    ids["augustine-contra-epistulam-parmeniani"] = emit_source(
        18, "augustine-contra-epistulam-parmeniani", "Augustine of Hippo",
        "Contra epistulam Parmeniani (3 books, c. 400)", PETSCHENIG, "pd", "attributed",
        "builder-prior-knowledge (Doc_01 SS4 binding), 2026-09-01; file presence and identity "
        "confirmed via direct file check, 2026-09-01",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted", None,
        "The Maximianist schism's own Cebarsussi/Bagai sentences, quoted, and Parmenian's own "
        "position -- confirmed present this session by its own closing formula ('Explicit liber "
        "tertius sci augustini epi. contra parmeniani epistolam'). The specific Cebarsussi/Bagai "
        "sentence quotations this row's Licensed-For names are available in the vendored text but "
        "have not themselves been read this session. The same Maximian/Maximian homonym flagged at "
        "row 17 applies here.")
    ids["augustine-psalmus-contra-partem-donati"] = emit_source(
        37, "augustine-psalmus-contra-partem-donati", "Augustine of Hippo",
        "Psalmus contra Partem Donati (Abecedarian psalm; dated only to Augustine's presbyterate)",
        PETSCHENIG, "pd", "attributed",
        "direct text search / grep and read against the vendored file, 2026-09-02",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "Augustine's own most directly popular-register anti-Donatist composition, and the earliest "
        "attested rhetorical use of the Maximianist-reception argument, pre-dating Contra "
        "Cresconium (Doc_02 SS1) -- the poem's own full Latin text (not merely row 31's Prolegomena "
        "summary of it) was found, unregistered, inside row 17/18's own file and confirmed this "
        "session from its own heading through its own closing marker at verse 288. The exact "
        "Maximianist-restoration rhetorical question Doc_02 SS1 quotes via row 31 was not itself "
        "located in a targeted search this session, though extensive rebaptism-rhetoric verses "
        "were found.")
    ids["petschenig-scripta-contra-donatistas"] = emit_source(
        39, "petschenig-scripta-contra-donatistas", "Michael Petschenig (ed.)",
        "Sancti Aureli Augustini Scripta contra Donatistas, CSEL 51 and 53 (Vienna/Leipzig, 1908 "
        "and 1910)", PETSCHENIG, "pd", "attributed",
        "builder-prior-knowledge, cross-checked via WebSearch, 2026-09-01; file identity and "
        "contents directly verified via direct file check, 2026-09-01",
        "A", "verified-direct", "corroborating", "Documented", None,
        "The critical Latin edition of Augustine's anti-Donatist works including Contra Cresconium "
        "and Contra epistulam Parmeniani (rows 17, 18) -- the edition those two rows currently "
        "lack. Confirmed this session to be a library binding of Pars I (CSEL 51) and Pars III "
        "(CSEL 53) together (an errata section explicitly corrects both volume numbers), also "
        "carrying De Unico Baptismo and Contra Fulgentium Donatistam, the Psalmus (row 37), and "
        "Contra Gaudentium (row 56) -- all confirmed present in this single file, across this and a "
        "later session.")
    ids["augustine-contra-gaudentium"] = emit_source(
        56, "augustine-contra-gaudentium", "Augustine of Hippo",
        "Contra Gaudentium Donatistarum Episcopum, Libri II (c. 420)", PETSCHENIG, "pd",
        "attributed",
        "sibling research session (session_01WLxhNbVhjkf1R2SAh8dxxT), direct text search / grep "
        "and read against the vendored file, 2026-09-08",
        "A", "verified-direct", "load-bearing", "Widely Accepted",
        "Confidence A here reflects the work's own confirmed presence, extent, and quotation "
        "method only -- no specific claim from Gaudentius's own words has yet been drawn into this "
        "world's own build from this row.",
        "Gaudentius of Thamugada's own two letters, quoted verbatim throughout by Augustine's own "
        "stated citation method ('when we set down Gaudentius's words, let us not say Gaudentius "
        "said, but words of the letter') -- a further body of preserved, genuine Donatist voice "
        "alongside rows 4/12's Petilian material, and Augustine's own last anti-Donatist work. "
        "Found already present, unregistered, inside the already-vendored Petschenig file, running "
        "roughly 12,000 lines from its own internal 'LIBER PRIMVS' heading.")

    # --- Rows 19-20, 50: the martyr Passiones of Migne PL8 ------------------
    ids["passio-marculi"] = emit_source(
        19, "passio-marculi", "Anonymous Donatist author",
        "Passio Benedicti Martyris Marculi (Passio Marculi), c. 348", MONUMENTA_PL8, "pd",
        "attributed",
        "builder-prior-knowledge, cross-checked via WebSearch (Patrologia Latina vol. 8, cols. "
        "760-766), 2026-09-01; direct text search / grep and read against the vendored file, "
        "2026-09-01",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "Martyr-cult narrative for the Macarian repression (347-348) and part of Doc_02 SS4's "
        "five-item formation-narrative evaluation -- the Passio's own heading was directly "
        "confirmed this session; the editorial rubric attributing it to 'Marculus... held by the "
        "Donatists to be a martyr' is Mabillon's and Migne's own descriptive framing, not the "
        "Passio's self-description, and the Macarian-repression dating rests on standard field "
        "literature (Frend), not the text's own heading. No free public-domain English translation "
        "exists; Tilley (row 35) and Monceaux (row 40) are named acquisition routes for a fuller "
        "apparatus.")
    ids["passio-isaac-et-maximiani"] = emit_source(
        20, "passio-isaac-et-maximiani", "Macrobius (letter); anonymous Donatist author "
        "(narrative)",
        "Passio SS. Martyrum Isaac et Maximiani, cum epistula Macrobii ad ecclesiam "
        "Carthaginiensem, c. 348", MONUMENTA_PL8, "pd", "attributed",
        "builder-prior-knowledge, cross-checked via WebSearch (Patrologia Latina vol. 8), "
        "2026-09-01; direct text search / grep and read against the vendored file, 2026-09-01",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "A second martyr-cult narrative for the Macarian repression, with an appended first-person "
        "letter from the martyr Macrobius himself to the church at Carthage -- a documented "
        "instance of direct Donatist epistolary voice, not only narrative about a martyr. Confirmed "
        "this session by its own rubric and explicit, naming Macrobius further as 'the Donatists' "
        "own hidden bishop in the city of Rome.' The Maximian martyred here is a different person "
        "from the Maximian of the Maximianist schism (rows 17-18) -- a homonym flagged in both "
        "directions.")
    ids["passio-donati-sermon"] = emit_source(
        50, "passio-donati-sermon", "Anonymous Donatist preacher (proposed, not confirmed: "
        "Donatus the Great, per Monceaux)",
        "Sermo de Passione Donati episcopi Advocatensis/Avioccalensis, manuscript title De "
        "passione sanctorum Donati et Advocati, known as the Passio Donati",
        "as edited by Jean Mabillon in Monumenta Vetera ad Donatistarum historiam pertinentia, "
        "printed in Migne, Patrologia Latina vol. 8, vendored as cic/texts/monumenta-vetera-"
        "donatistarum_migne-pl8.txt (the same file as rows 19-20, found incidentally while "
        "vendoring them)", "pd",
        "contested: Mabillon's own admonitio dates the persecution to c. 340 without proposing an "
        "author or resolving the title; Monceaux (row 40) dates it to 12 March 317 (composition c. "
        "320) and proposes the preacher was Carthage's Donatist bishop, possibly Donatus the "
        "Great -- neither dating nor authorship is adopted as settled here",
        "direct text search / grep and read against the vendored file, found incidentally while "
        "vendoring rows 19-20; Monceaux's competing account independently verified against row "
        "40's own file, 2026-09-02",
        "A", "verified-direct", "contested", "Contested",
        "Formation_confidence is held at Contested, not Documented, despite verified-direct: the "
        "sermon's own presence, genre, and existence are directly confirmed, but its date and "
        "proposed author are reported from two competing vendored authorities that this record "
        "deliberately does not resolve between (Doc_02 SS8).",
        "A genuine surviving Donatist-authored primary voice -- the scarcest category this world's "
        "own Discovery methodology and Doc_02 SS6 name -- commemorating a persecution under "
        "Leontius and Ursacius. Licensed for its own existence and genre, and for its dating, "
        "authorship, massacre-scale account, and title question as reported from the two competing "
        "authorities above; not licensed for a settled dating or authorship, nor for its own full "
        "Latin content beyond the passages checked this session.")

    # --- Row 21: the Liber Genealogus ---------------------------------------
    ids["liber-genealogus"] = emit_source(
        21, "liber-genealogus", "Anonymous North African chronicler",
        "Liber Genealogus (Additamentum II to the Chronographus Anni CCCLIIII)",
        "Theodor Mommsen (ed.), Chronica Minora Saec. IV-VII, Vol. I, MGH Auctores Antiquissimi "
        "IX (Berlin: Weidmann, 1892), vendored as "
        "cic/texts/chronica-minora-liber-genealogus_mommsen1892.txt", "pd", "attributed",
        "builder-prior-knowledge, 2026-09-01; direct text search / grep and read against the "
        "vendored file, 2026-09-08",
        "A", "verified-direct", "illustrative", "Widely Accepted",
        "Confidence and verification reflect the manuscript's own confirmed presence, identity, "
        "and dating discussion only (this row's own calibration note) -- this row is not yet "
        "licensed for any specific Donatism claim, so evidentiary_weight stays illustrative rather "
        "than load-bearing until a future pass draws a claim from its own genealogical content.",
        "Chronological/genealogical content only, use to be determined at Doc_09. Scholarship "
        "since Monceaux reads it as Donatist-affiliated on internal grounds, not independently "
        "verified against the text itself this session. The surviving manuscript recensions' own "
        "consular/regnal references (427, 438, 455) confirm a provenance within or immediately "
        "adjacent to this world's own 311-439 window.")

    # --- Row 27, 48: the Deo laudes acclamation and its own CIL instrument --
    ids["cil8-numidia-supplement"] = emit_source(
        48, "cil8-numidia-supplement", "R. Cagnat and J. Schmidt (eds.)",
        "Corpus Inscriptionum Latinarum, vol. VIII, Supplementum, Pars II: Inscriptionum "
        "Provinciae Numidiae Latinarum Supplementum (Berlin: Reimer, 1894)", CIL8, "pd",
        "attributed",
        "builder-prior-knowledge, 2026-09-01; file identity and contents directly verified via "
        "direct file check, 2026-09-01",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "The standard epigraphic corpus for Numidia, this world's own Donatist heartland province "
        "-- the instrument that moved row 27's Deo laudes claim off a recognized-category "
        "generality onto specific catalogued inscriptions. Confirmed this session as the genuine "
        "1894 CIL Numidia supplement fascicle (not the 1881 main volume); public domain, with the "
        "scan's own front matter documenting a 1991 University of Minnesota preservation facsimile "
        "of the original.")
    ids["deo-laudes-acclamation-cil8"] = emit_source(
        27, "deo-laudes-acclamation-cil8", "Unknown Donatist dedicators (epigraphic)",
        "The Deo laudes acclamation, attested at CIL VIII 17732 (Bagai), 20482, 17368, and 18669",
        CIL8, "pd", "attributed",
        "builder-prior-knowledge (recognized field category), 2026-09-01; direct text search / "
        "grep and read against the vendored file, 2026-09-01",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "Worship/liturgical distinctiveness evidence (Doc_02 SS5) -- CIL VIII 17732, found on two "
        "pillars near Bagai itself, reads 'DEO LAVDES' twice, with the editors' own note "
        "identifying it as the Donatists' own sign and token, as 'Deo gratias' was the Catholics'. "
        "Four catalogued attestations in total, the strongest from Bagai itself, one of the two "
        "Donatist seats CIL VIII names for it -- resolved this session from a recognized field "
        "category onto specific catalogued inscriptions via row 48's own now-vendored text.")

    # --- Row 30: Lucilla and the second, unnamed Maximianist-schism woman --
    ids["lucilla-and-second-woman-maximianist"] = emit_source(
        30, "lucilla-and-second-woman-maximianist", "Optatus of Milevis (I.16); Augustine of "
        "Hippo (Letter XLIII SS26)",
        "Lucilla's own role at the schism's founding, and a second, unnamed woman behind the "
        "Maximianist schism's own council against Primian, as attested and paralleled by name in "
        "these two already-vendored passages",
        "optatus_against-the-donatists.txt (row 1's file) and "
        "npnf101_augustine-confessions-letters.xml (row 6's file)", "pd", "attributed",
        "direct text search / grep and read against both vendored files, 2026-09-01",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "Gender/Affirmative Duty discharge (Doc_02 SS6) and a Doc_09 Story Inventory candidate -- "
        "Optatus I.16 describes Lucilla, a wealthy Carthaginian laywoman, as the schism's own "
        "proximate cause ('at her instigation, and through her bribes'); Augustine's Letter XLIII "
        "SS26 draws Lucilla's own name into a direct parallel with a second, unnamed woman behind "
        "the later Maximianist council against Primian. Both passages were directly read and "
        "confirmed this session (13 occurrences in the Optatus file). The vendored edition's own "
        "translator's apparatus cites an Augustine letter numbered 'clxii' that does not match "
        "NPNF's own Letter CLXII -- very likely an older, pre-standard numbering scheme; the "
        "content is identified and vendored, but that specific numbering equivalence is not "
        "asserted.")

    # --- Row 31: the NPNF104 Prolegomena's own scholarly analysis ----------
    ids["npnf104-prolegomena-analysis"] = emit_source(
        31, "npnf104-prolegomena-analysis", "Unnamed 19th-century editor",
        '"Chapter II. -- An Analysis of Augustin\'s Writings Against the Donatists," Prolegomena '
        "to NPNF Series I, vol. IV", NPNF104, "pd", "attributed",
        "direct text search / grep and read against the vendored file, 2026-09-01",
        "A", "verified-direct", "corroborating", "Widely Accepted", None,
        "A 19th-century scholarly synthesis, not a primary Donatist or Maximianist voice -- dates "
        "Contra Cresconium and Contra epistulam Parmeniani, and is the source Doc_02 SS1 quotes for "
        "a Donatist apologetic claim about the Maximianist reception (a claim Augustine rejects, "
        "not an agreed fact). Not the primary evidence for the Maximianist reception itself, which "
        "Doc_02 SS1 draws directly from row 3. Directly read this session in the vendored file.")

    # --- Rows 32, 54: Gregory the Great's own Donatist-subject letters -----
    ids["gregory-great-epistolae-selectae-turchi"] = emit_source(
        54, "gregory-great-epistolae-selectae-turchi", "Gregory the Great; ed. Nicola Turchi",
        "Bibliotheca Sanctorum Patrum et Scriptorum Ecclesiasticorum, Series VII, Voluminis I "
        "Pars I: Sancti Gregorii Magni Epistolae Selectae (Rome, 1907)",
        "cic/texts/gregory-great_epistolae-selectae_turchi1907.txt", "pd", "attributed",
        "direct text search / grep and read against the vendored file, 2026-09-07",
        "A", "verified-direct", "load-bearing", "Widely Accepted",
        "A themed selection, not the complete Register (row 32) -- its own front matter states its "
        "text and annotations are taken from the Ewald-Hartmann edition, with each included letter "
        "carrying an explicit concordance to it; the complete Register beyond these four letters "
        "was not found in this selection this session.",
        "Four specific Donatist-subject letters of Gregory the Great, directly confirmed this "
        "session by a full-file search: Ep. LXXXII (to Columbus of Numidia, 592, ordering an "
        "inquiry into a bishop corrupted by Donatist bribery), Ep. LXXXIV (to Pantaleon, 594, "
        "urging suppression), Ep. LXXXVI (to Victor and Columbus, 594, urging a council), and Ep. "
        "LXXXVII (to Dominicus of Carthage, 594, on a council's own penalty clause) -- the "
        "terminus-of-attestation point for this world's own record, sharpened to four named, "
        "dated letters (Doc_02 SS7).")
    ids["gregory-great-register-of-letters"] = emit_source(
        32, "gregory-great-register-of-letters", "Gregory the Great",
        "Register of Letters (590s correspondence concerning the North African church)",
        "the complete Ewald-Hartmann critical edition (Registrum Epistolarum, Berlin, 1891) "
        "remains unvendored; a themed selection drawing directly from it is vendored at row 54's "
        "own file", "pd", "attributed",
        "builder-prior-knowledge (carried from Doc_02 SS3/SS7 citation gap), 2026-09-01; direct "
        "text search / grep and read against row 54's own file, 2026-09-07",
        "A", "verified-direct", "load-bearing", "Widely Accepted",
        "Partially vendored via row 54's themed 1907 selection, not the complete critical "
        "edition -- four specific, directly-read letters (592-594 CE) now license this row, but "
        "the general Register beyond those four remains a citation gap, not a settled claim.",
        "The terminal-record fixing point (Doc_02 SS3, SS7) -- Doc_01 SS2's own construction-window "
        "boundary (439) marks the removal of the Roman-imperial adjudicating power, not the end of "
        "the underlying two-party contest, which Gregory's own correspondence shows continuing "
        "into the 590s. Four letters directly confirmed this session name the Donatists explicitly; "
        "see row 54's own record for the letters themselves.")

    # --- Row 33: De Doctrina Christiana's own Tyconius influence -----------
    ids["augustine-de-doctrina-christiana-book3"] = emit_source(
        33, "augustine-de-doctrina-christiana-book3", "Augustine of Hippo",
        "De Doctrina Christiana, Book III", NPNF102, "pd", "attributed",
        "builder-prior-knowledge, file existence and content confirmed via direct file check, "
        "2026-09-01",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "Licensed narrowly for Tyconius's own influence on Augustine's hermeneutics (Doc_02 SS1), "
        "not for De Doctrina Christiana's own content generally. File presence and 27 occurrences "
        "of 'Tichonius' were confirmed directly this session; Book III's own specific Tyconian-"
        "rules content was not independently re-read this session -- flagged for priority "
        "second-opinion review before supporting any claim more specific than the influence "
        "relationship itself (Registry's own 'Priority second-opinion review flags' section).")

    # --- Rows 38, 41, 51: the critical editions attaching to rows 1, 15, 16
    ids["ziwsa-critical-edition-optatus"] = emit_source(
        38, "ziwsa-critical-edition-optatus", "Karl Ziwsa (ed.)",
        "S. Optati Milevitani libri VII, Corpus Scriptorum Ecclesiasticorum Latinorum (CSEL) 26 "
        "(Prague/Vienna/Leipzig, 1893)", "cic/texts/optatus_libri-vii-critical_ziwsa1893.txt",
        "pd", "attributed",
        "builder-prior-knowledge, cross-checked via WebSearch, 2026-09-01",
        "B", "verified-via-authority", "corroborating", "Widely Accepted", None,
        "The critical Latin edition attaching to row 1's own work -- the specific instrument that "
        "would settle the second-edition question row 1's own Verification Note leaves open, in "
        "place of the 1917 translator's own footnote. Confirmed this session as the genuine CSEL "
        "26 edition (title page, and the Gesta Purgationis Felicis appendix document both "
        "present); the second-edition/book-count question has not itself been settled this "
        "session -- the apparatus criticus has not yet been read for that purpose.")
    ids["burkitt-liber-regularum-edition"] = emit_source(
        41, "burkitt-liber-regularum-edition", "F.C. Burkitt (ed.)",
        "The Book of Rules of Tyconius, Newly Edited from the MSS., Texts and Studies III/I "
        "(Cambridge University Press, 1894)",
        "cic/texts/tyconius_liber-regularum_burkitt1894.txt", "pd", "attributed",
        "builder-prior-knowledge, file identity and rights basis confirmed via direct file check, "
        "2026-09-01",
        "A", "verified-direct", "corroborating", "Documented", None,
        "The public-domain critical Latin edition attaching to row 15's own work -- confirmed this "
        "session as the genuine Burkitt 1894 edition (preface, table of contents, introduction all "
        "present, correctly naming editor and author). Public domain confirmed on two independent "
        "grounds: archive.org's own copyright-evidence record and the 1894 publication date alone. "
        "Raw, uncorrected OCR with visible Greek-letter substitution into Latin words -- any "
        "specific quotation drawn from it needs visual cross-check before being relied on "
        "verbatim.")
    ids["mommsen-meyer-theodosiani-libri-xvi"] = emit_source(
        51, "mommsen-meyer-theodosiani-libri-xvi", "Th. Mommsen and Paul M. Meyer (eds.)",
        "Theodosiani Libri XVI cum Constitutionibus Sirmondianis et Leges Novellae ad "
        "Theodosianum Pertinentes, Voluminis I Pars Posterior: Textus cum Apparatu (Berlin: "
        "Weidmann, 1905)", THEODOSIANUS16, "pd", "attributed",
        "sibling research session's finding, independently re-verified via direct text search / "
        "grep and read against the vendored file, 2026-09-07",
        "A", "verified-direct", "load-bearing", "Documented", None,
        "The primary critical-edition text of law 16.5.52 (row 16) and of Book XVI generally, "
        "superseding row 49 (Boyd) as the primary-source basis for row 16's own Author Gravity "
        "assessment -- located after five prior acquisition attempts each returned the wrong "
        "volume (the Prolegomena, not this Pars Posterior text volume). Confirmed this session: "
        "all 16 Books present, Book XVI located, law XVI.5.52 read in full and confirmed to "
        "contain 'circumcelliones argenti pondo decem' verbatim. The agonistici term does not "
        "appear anywhere in this file either (checked directly, zero matches).")

    # --- Row 40, 52, 53: Monceaux's three-tome Donatism series -------------
    ids["monceaux-histoire-litteraire-tome5"] = emit_source(
        40, "monceaux-histoire-litteraire-tome5", "Paul Monceaux",
        "Histoire litteraire de l'Afrique chretienne, Tome V: Saint Optat et les premiers "
        "ecrivains donatistes (Paris: Ernest Leroux, 1920)",
        "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome5_1920.txt", "pd",
        "attributed",
        "builder-prior-knowledge, 2026-09-01; file identity and contents directly verified via "
        "direct file check, 2026-09-01",
        "A", "verified-direct", "corroborating", "Dominant Modern Reconstruction", None,
        "A second, independent public-domain route to the Macarian-repression Passiones (rows 19, "
        "20); Tyconius's biography and reception; and the Passio Donati sermon's own dating, "
        "proposed authorship, and title question (Doc_02 SS1, SS2, SS4) -- read this session for a "
        "dedicated Tyconius chapter and the Passio Donati material, dating that persecution to 12 "
        "March 317 (composition c. 320) against Mabillon's own narrower c. 340 apparatus (row 50's "
        "own record carries the resulting Contested finding). Not licensed for Monceaux's own "
        "footnoted primary-source citations, not themselves checked against the vendored corpus "
        "this session.")
    ids["monceaux-histoire-litteraire-tome4"] = emit_source(
        52, "monceaux-histoire-litteraire-tome4", "Paul Monceaux",
        "Histoire litteraire de l'Afrique chretienne, Tome IV: Le Donatisme (Paris: Ernest "
        "Leroux, 1912)", "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome4_1912.txt",
        "pd", "attributed",
        "direct file check (title page and chapter-heading survey only), 2026-09-07",
        "A", "verified-direct", "illustrative", "Widely Accepted",
        "Confidence A here reflects the title page and four chapter headings confirmed this "
        "session only ('L'Eglise Donatiste,' 'Les Documents Donatistes,' 'Les Actes des Conciles,' "
        "'L'Epigraphie Donatiste') -- no specific claim, quotation, or citation from this tome's "
        "own body text has been checked, so evidentiary_weight stays illustrative rather than "
        "load-bearing.",
        "Monceaux's own first dedicated Donatism volume -- more directly on-topic than Tome V (row "
        "40) for this world's own Doc_02/Doc_04 material, named as an open item for a future "
        "revision pass rather than read through and integrated here.")
    ids["monceaux-histoire-litteraire-tome6"] = emit_source(
        53, "monceaux-histoire-litteraire-tome6", "Paul Monceaux",
        "Histoire litteraire de l'Afrique chretienne, Tome VI: La Litterature Donatiste (au "
        "temps de saint Augustin) (Paris: Editions Ernest Leroux, 1922)",
        "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome6_1922.txt", "pd",
        "attributed",
        "direct file check (title page and chapter-heading survey only), 2026-09-07",
        "A", "verified-direct", "illustrative", "Widely Accepted",
        "Confidence A here reflects the title page and nine chapter headings confirmed this "
        "session only, each a dedicated study of one named Donatist figure or genre already "
        "present elsewhere in this Registry (Petilianus, row 12; Emeritus, row 14; and others) -- "
        "no specific claim, quotation, or citation from this tome's own body text has been "
        "checked.",
        "Companion to row 52 (Tome IV), same acquisition round -- named as an open item for a "
        "future Doc_02/Doc_04 revision pass rather than read through and integrated here.")

    # --- Row 49: Boyd's own corroborating narrative history ----------------
    ids["boyd-ecclesiastical-edicts-theodosian-code"] = emit_source(
        49, "boyd-ecclesiastical-edicts-theodosian-code", "William K. Boyd",
        "The Ecclesiastical Edicts of the Theodosian Code (Studies in History, Economics and "
        "Public Law, Columbia University, Vol. XXIV, 1905)",
        "cic/texts/boyd_ecclesiastical-edicts-theodosian-code_1905.txt", "pd", "attributed",
        "Mark, DOCX upload naming the archive.org search results and recommending this item; "
        "direct file check against the vendored file, 2026-09-01",
        "A", "verified-direct", "corroborating", "Widely Accepted", None,
        "Corroborating narrative history of Donatist-targeted legislation in Codex Theodosianus "
        "Book 16 Title 5 (row 16), with several individual laws quoted verbatim naming the "
        "Donatists directly -- confirmed this session to be a genuine 1905 Columbia University "
        "monograph. Does not license 16.5.52 itself, which is not quoted anywhere in this file, "
        "nor the agonistici term, which does not appear here either -- Boyd uses only "
        "'Circumcellions' throughout, itself a small data point on how the field's own terminology "
        "has shifted since (Doc_02 SS6), too thin a sample to generalize from.")

    # --- Row 55: the Migne PL11 volume's own Gesta cluster ------------------
    ids["migne-pl11-collatio-carthaginiensis"] = emit_source(
        55, "migne-pl11-collatio-carthaginiensis", "J.-P. Migne (ed.)",
        "Patrologiae Cursus Completus, Series Latina, Tomus XI -- the volume bundling Zeno of "
        "Verona's own works with a substantial Optatus/Donatism-material cluster, including the "
        "Gesta Collationis Carthaginiensis itself (col. 1223)",
        "cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt", "pd", "attributed",
        "direct archive.org search / direct text search and read against the vendored file, "
        "2026-09-07",
        "B", "verified-via-authority", "load-bearing", "Widely Accepted",
        "Confidence held at B, not A, because most of this bundled ~5MB, 144,000-line volume has "
        "not been read this session -- its own printed table of contents names further "
        "Donatism-relevant items not yet evaluated, including a section carrying the identical "
        "Latin title to row 19/20's own file, not reconciled this session as either the same "
        "material misattributed to different volume numbers or two independently overlapping "
        "compilations.",
        "Real, substantive Gesta conference-acts content -- Donatist bishops' own recorded words at "
        "the 411 Conference (row 14), specifically Emeritus of Caesarea, confirmed at least 28 "
        "occurrences in the file. Found after row 14's own 2026-09-01 'confirmed unavailable' "
        "determination turned out to have been made without working network access to actually "
        "check it (2026-09-07). Only the Gesta section itself was spot-checked this session; the "
        "precise column boundary separating it from Balduin's own following narrative was not "
        "established.")

    return ids


def build_world_core(source_ids: dict[str, str]) -> str:
    horizon = (
        "Roman North Africa (Africa Proconsularis, Numidia, Byzacena, Mauretania), Latin-speaking, "
        "c. 311/312-439 CE: a rigorist alternative communion that split from the North African "
        "Catholic church over the validity of sacraments and ordinations administered by clergy "
        "suspected of having surrendered scripture during the Diocletianic persecution. The schism "
        "opens with the disputed 311/312 election and consecration of Caecilian as bishop of "
        "Carthage and the traditio accusation against his consecrator, Felix of Aptungi, which "
        "produced the rival consecration of Majorinus (succeeded from c. 313 by Donatus, from whom "
        "the movement's name derives); it closes at the Vandal capture of Carthage in 439, which "
        "removes the Roman imperial state as the Catholic-aligned adjudicating and coercing power "
        "this world's entire refusal-of-imperial-legitimacy pattern is defined against (Doc_01 SS2). "
        "Geographic centers: Carthage, seat of both rival bishoprics from the outset and site of "
        "the decisive 411 Conference; Numidia, the region of Donatism's greatest institutional "
        "strength; Cirta (Constantina), see of Petilian, one of the movement's most prominent "
        "bishops. This is a world of contested legitimacy and parallel institutional life, not a "
        "doctrinal heresy: a communion holding standard North African Latin Trinitarian and "
        "Christological confession while claiming to be the one true, pure 'Church of the Martyrs' "
        "against a rival it regarded as traditor-tainted and, from 312 onward, state-favored "
        "(Doc_01 SS1). Participation spans bishops and clergy of a full parallel hierarchy down to "
        "a broad lay base -- for substantial periods and regions the numerically dominant church, "
        "not an elite minority current (Doc_01 SS2)."
    )
    formation_logic = (
        "A fully formed member of this world holds, without qualification, that a sacrament's "
        "validity rises and falls on the giver's own unbroken purity, and has been rebaptized -- "
        "deliberately, individually, bodily -- into the one communion whose ministers can be "
        "trusted to give it. That same member holds the community's own dead by name, at the "
        "grave, on the appointed day, and hears their account so the same conviction happens again "
        "in the hearing; and refuses the state's own standing to settle who the true church is, "
        "while not treating that refusal as requiring absolute, unbending consistency at every "
        "moment (Doc_07 SS2I). Formation happens less through speculative teaching or a developed "
        "interpretive tradition -- doctrine and philosophy beyond the purity/rebaptism cluster are "
        "genuinely thin here -- than through enacted threshold-crossing (rebaptism), repeated "
        "commemorative narration (the annual reading at the martyr's grave), and lived legal "
        "jeopardy (a parallel church existing under continuous external legal pressure). Entry is "
        "the rebaptism itself, a specific, dated, individually experienced threshold; the middle of "
        "formation is lived inside a parallel institutional life under continuous jeopardy, "
        "punctuated by episodes of acute persecution that intensify rather than interrupt the "
        "community's own commemorative practice; maturity looks like the martyr -- not necessarily "
        "literal death, but the settled readiness the martyr narratives hold up as the community's "
        "own formation ideal, suffering chosen over the peace that would concede the rival's own "
        "legitimacy. The whole system is one conviction lived out through purity, rite, memory, and "
        "refusal: we are the pure, persecuted, true church, proved by what we will not concede and "
        "by what we have suffered for refusing to concede it -- a system built, from its own "
        "founding moment, to be lived under an unpredictable, oscillating external power, so that "
        "even its own qualifications (the three pragmatic turns toward imperial machinery in 313, "
        "361, and the 390s; the unrebaptized reception of returning Maximianist clergy) are held "
        "openly alongside the doctrine's own absolute statement, not hidden as embarrassments or "
        "treated as proof the doctrine was hollow (Doc_07 SS4, SS6)."
    )
    thinness = (
        "Richest in the hostile-but-primary narrative of Optatus and the vast anti-Donatist corpus "
        "of Augustine, in the Codex Theodosianus's own imperial legislation, and in this world's "
        "own small set of surviving self-authored texts (Tyconius's Liber Regularum, two martyr "
        "Passiones, a fragmentary letter of the martyr Macrobius, and the newly recovered Gesta "
        "Collationis Carthaginiensis court transcript); thinner on the ordinary Numidian believer's "
        "own words despite being, for long stretches, the numerically dominant church, on the "
        "Circumcellions'/agonistici's own typical conduct beyond their bare legislative attestation, "
        "on any woman's own voice beyond Lucilla's and one unnamed parallel (both named only inside "
        "hostile or incidental narration), and on this world's own account of specific violent "
        "episodes its opponents allege against it. Structurally, nearly the entire record passed "
        "through Catholic hands (Optatus, Augustine) before reaching us -- a severe selection "
        "effect this world's own construction names as its central evidentiary problem, not a "
        "background caveat: evidence survives in inverse proportion to how directly it can be "
        "checked without a hostile hand mediating it (Doc_01 SS7 item 1; Doc_02 SS6; Doc_07 SS5). "
        "Basilica archaeology beyond epigraphy remains genuinely undone (Confidence C, not "
        "independently verified this construction pass); the ordinary believer's interior life -- "
        "doubt, fear, a traditor's own account of surrendering scripture -- is a register a "
        "hostile-mediated record structurally does not preserve, however well it preserves this "
        "world's own vindicated, defiant register in the martyr texts (Doc_07 SS7)."
    )
    cautions = (
        "1) AUTHOR GRAVITY: nearly the entire vendored record passes through the hostile "
        "Caecilianist/Catholic side (Optatus, Augustine) before reaching us -- named as this "
        "world's own central evidentiary problem, not a background caveat (Doc_01 SS7 item 1; "
        "Doc_02 SS6). The Maximianist internal-schism material (caution 3 below) is a leading case: "
        "it reaches us almost entirely through Augustine's own quotation and must be marked as "
        "such, never treated as independent attestation. 2) CIRCUMCELLIONS/AGONISTICI: existence "
        "and self-designation are independently attested outside hostile polemic -- Codex "
        "Theodosianus 16.5.52 sets a distinct silver fine for the group by name -- but their "
        "typical conduct, scale, and relationship to the wider hierarchy remain substantially "
        "Augustine's and Optatus's own hostile framing, not independently checkable at present "
        "(Doc_02 SS6). The group's own self-designation term, agonistici, does not appear anywhere "
        "in the vendored Theodosian Code text; its specific source passage in Augustine's own "
        "corpus remains unidentified. 3) MAXIMIANIST SCHISM (393-398): the mainstream Donatist "
        "party's own reception of the Maximianist clergy back without reordination or rebaptism is, "
        "on the record's own logic, proof the mainstream party recognized Maximianist orders and "
        "sacraments as valid -- never cite the episode as a strand-status difference (Doc_01 SS4 "
        "finds this world strand-singular after testing it) or smooth past what the reception "
        "itself concedes. 4) PASSIO DONATI DATING/AUTHORSHIP CONTESTED: two competing vendored "
        "authorities give different accounts -- Mabillon dates the underlying persecution to c. 340 "
        "without proposing an author; Monceaux dates it to 12 March 317 (composition c. 320) and "
        "proposes the preacher was Carthage's Donatist bishop, possibly Donatus the Great. Neither "
        "is adopted as settled (Doc_02 SS4, SS8). 5) BISHOP COUNT AT THE 411 CONFERENCE: 279 "
        "Donatist against 286 Catholic bishops seated -- corrected from an earlier, "
        "unverified 284 figure that had circulated in this world's own build (Doc_01 SS5; Doc_02 "
        "SS1, SS8). Use 279/286, not 284. 6) TERMINAL RECORD VS. CONSTRUCTION WINDOW: this world's "
        "own 439 construction-window close marks the removal of the Roman-imperial, "
        "Catholic-aligned adjudicating power its refusal-of-imperial-legitimacy pattern is defined "
        "against -- not the end of the underlying two-party contest, which Gregory the Great's own "
        "correspondence (partially vendored, row 54) shows continuing into the 590s, with no "
        "attestation of an organized Donatist body and no documented line to any present-day "
        "communion thereafter (Doc_01 SS1, SS2; Doc_02 SS7). 7) LIVING TRADITION STATUS PENDING: "
        "whether Constitution Article 29's gate attaches at all -- on the no-documented-descendant "
        "question, or on this world's own mediated contact through Cyprian and Augustine, both of "
        "contested standing among present-day traditions -- is the project lead's own call at "
        "freeze, not resolved by this record (Doc_01 SS1). 8) SCALE, NOT ELITE SKEW: unlike several "
        "other confirmed worlds, this world's sourcing problem is not that an elite minority "
        "current speaks for a larger silent population -- Donatism was, for substantial periods and "
        "regions, the numerically dominant church. The ordinary-believer gap here is a "
        "source-mediation problem, not a scale problem (Doc_02 SS6). 9) EBBELER CITATION SCOPE: "
        "Jennifer Ebbeler's own work on Augustine's epistolography is a supporting citation only, "
        "carried forward from Step 0's own binding correction -- never a primary source for a "
        "Donatism-specific claim (Doc_01 SS7 item 4). 10) TRANSLATOR/EDITOR APPARATUS MISTAKEN FOR "
        "PRIMARY CONTENT: a recurring, tracked failure mode across this world's own build -- a "
        "footnote or endnote's own gloss mistaken for the primary text's own content or citation "
        "chain (three confirmed instances; Doc_09 Section 9 item 5) -- check a claim against the "
        "vendored primary text itself, not only against an apparatus describing it."
    )
    thin_topics = [
        {"keywords": ["ordinary believer", "Numidian peasant", "laity", "non-elite"],
         "note": "The numerically dominant population across long stretches of this world's own "
                 "history is attested only through hostile or institutional intermediaries, never "
                 "in its own words -- a source-mediation problem, not a scale problem."},
        {"keywords": ["Circumcellion", "agonistici", "itinerant", "rural violence"],
         "note": "Existence and self-designation are independently attested by imperial law "
                 "(Codex Theodosianus 16.5.52), but the group's typical conduct, scale, and "
                 "relationship to the wider hierarchy remain substantially hostile framing; the "
                 "self-designation term's own source passage in Augustine's corpus is "
                 "unidentified."},
        {"keywords": ["women", "Lucilla", "gender"],
         "note": "One named woman (Lucilla) at the schism's founding, and one unnamed second "
                 "woman at the Maximianist schism, both attested only through hostile or "
                 "incidental narration; no ordinary or Caecilianist-side woman is individually "
                 "attested."},
        {"keywords": ["interior life", "doubt", "fear", "wavering", "traditor's own account"],
         "note": "A hostile-mediated record structurally preserves this world's own vindicated, "
                 "defiant register in the martyr texts, not doubt, fear, or a traditor's own "
                 "account of surrendering scripture."},
        {"keywords": ["basilica archaeology", "material remains", "excavation"],
         "note": "Epigraphy is strong (the Deo laudes acclamation); basilica archaeology beyond "
                 "it is genuinely undone, Confidence C, not independently verified this "
                 "construction pass."},
        {"keywords": ["Bagai violence", "Circumcellion atrocity", "Donatist self-defense"],
         "note": "Hostile sources record specific, dated allegations (forced rebaptism of the "
                 "Mappalians; the attack on Maximianus of Bagai) in detail; this world has no "
                 "surviving account of its own side of any of them."},
        {"keywords": ["Tyconius", "formal communion status", "excommunication"],
         "note": "Condemned by a Donatist council over his universalist ecclesiology but never "
                 "joined the Catholic church; his own formal standing within the communion is "
                 "deliberately left open, not resolved."},
    ]
    sources = [
        {"source_id": source_ids["augustine-answer-to-letters-of-petilian"],
         "locus": "passim -- this world's fullest surviving primary voice, quoted", "license": "public-domain"},
        {"source_id": source_ids["optatus-against-donatists"],
         "locus": "passim -- the schism's own earliest narrative source", "license": "public-domain"},
        {"source_id": source_ids["tyconius-liber-regularum"],
         "locus": "whole work -- this world's own strongest surviving theological writing",
         "license": "public-domain"},
        {"source_id": source_ids["gesta-collationis-carthaginiensis"],
         "locus": "the 411 Conference acts, Emeritus of Caesarea's own numbered interventions",
         "license": "public-domain"},
        {"source_id": source_ids["codex-theodosianus-book-16"],
         "locus": "16.5.52, the circumcelliones fine clause", "license": "public-domain"},
        {"source_id": source_ids["lucilla-and-second-woman-maximianist"],
         "locus": "Optatus I.16; Augustine, Letter XLIII SS26", "license": "public-domain"},
    ]
    payload = {
        "id": "don.core.donatism",
        "world_id": WORLD_ID,
        "record_type": "world_core",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": conf("B", "verified-via-authority", "load-bearing", "Widely Accepted", None),
        "sources": sources,
        "relations": [],
        "time_window": {"start": 311, "end": 439},
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
        "Built from Doc_01_World_Identification_Boundaries_Orientation.md SS1-SS2 (time_window, "
        "horizon), Doc_07_Integrated_Ecology_Analysis.md SS2I (formation_logic), and "
        "Doc_02_Source_Ecology.md SS6/SS8 plus Doc_07 SS7 and Doc_09_Story_Inventory.md SS8 "
        "(thinness/cautions/thin_topics). time_window.start=311 (rather than 312) is this script's "
        "own judgment call among the two years Doc_01 SS2 itself carries without resolving to a "
        "false precision the sources do not support -- argued in this script's own docstring, not "
        "silently picked. world_id 'don' is Doc_01's own stated file-code (line 4), not minted by "
        "this script.\n\n"
        "No Representative content appears in this record (Doc_01 constraint honored; this world's "
        "own Representative material lives in World-Builds/Donatism/Representative/ and "
        "don_World_Capsule_Core.md, neither read into this record)."
    )
    text = f"---\n{front}---\n{body}\n"
    path = out_dir / f"{payload['id']}.md"
    path.write_text(text, encoding="utf-8")
    WRITTEN.append(str(path))
    return payload["id"]


def main() -> None:
    source_ids = build_sources()
    assert len(source_ids) == 41, f"expected 41 source records, built {len(source_ids)}"
    world_core_id = build_world_core(source_ids)
    print(f"Wrote {len(WRITTEN)} records:")
    print(f"  - {len(source_ids)} source records under {RECORDS_ROOT / 'source'}")
    print(f"  - 1 world_core record ({world_core_id}) under {RECORDS_ROOT / 'world_core'}")


if __name__ == "__main__":
    sys.exit(main())
