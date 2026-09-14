"""B-1 (S2.1): Donatism (`don`) source + world_core records.

WHAT THIS SCRIPT DOES. Converts this world's completed Phase A documents into
WRS records under records/don/{source,world_core}/, per the live schema
(engine/m1/schemas.py) and gate battery (engine/m1/gates.py). This is the
FIRST record-authoring pass for this world; no `don` records existed before
this script ran (records/don/ did not exist at all -- confirmed by listing
records/ directly, not assumed).

INPUTS, mapped to OUTPUTS, precisely:
  - World-Builds/Donatism/Source_Registry.md -> the 55 `source` records
    (ROWS below). The Registry's table holds 56 numbered rows, counted
    mechanically off the table markup, not taken from any prior estimate.
    Fifty-five carry Boundary Status "Native"; ONE (row 29, Novatian's
    *De Trinitate* and Novatianist material generally) carries Boundary
    Status "**Excluded**" with Exclusion Reason "**Named Comparandum**"
    and a Licensed-For field reading "N/A -- excluded". It is deliberately
    NOT emitted, following the cappadocian precedent exactly
    (World-Builds/Cappadocian/scripts/wb_cappadocian_s21.py: "Only rows
    with Boundary Status 'Native' become records... the 6 Excluded rows...
    are deliberately NOT emitted as this world's own source records...
    exactly as the Registry itself disposes them"). Emitting row 29 as a
    `don` source record would assert, in the one field a downstream reader
    trusts, that Novatian is a source for this world -- which is the exact
    temptation that row exists to guard against. Flagged upward rather
    than silently dropped; see the B-1 handback note.
  - Source_Acquisition_Manifest.md ss1/ss2/ss3 -> rights_status. The
    Manifest, not the Registry, is what actually sorts every named work
    into public-domain-and-vendored (ss1, G1-G7), in-copyright-recorded-
    not-requested (ss2), or consultation-only-never-vendored (ss3).
  - Doc_01_World_Identification_Boundaries_Orientation.md ss1, ss2, ss5,
    ss7 -> world_core.time_window, .horizon, .cautions.
  - Doc_07_Integrated_Ecology_Analysis.md ss2I, ss3A, ss5, ss6 ->
    world_core.formation_logic.
  - Doc_02_Source_Ecology.md ss6 (Source Asymmetries and Missing Voices),
    ss8 (Confidence Map), ss9 (open items) + Doc_07 ss7 (Gaps and Limits)
    -> world_core.thinness / .cautions / .thin_topics.

MECHANICAL vs AUTHORED, field by field, so a reviewer can tell what to
re-check against the Registry directly and what required this script's own
reading and judgment:

  - id, world_id, record_type, schema_version, status, register,
    canon_cells, relations: MECHANICAL. register="etic" for every source
    record (a source record describes an external text, not this world's
    own first-person voice -- hal/cappadocian precedent); register="emic"
    on world_core, same as every built world. canon_cells=[] throughout:
    no canon-cell tagging work has happened for this world yet.
    schema_version=2, matching every currently-built world.

  - world_id: "donatism". MECHANICAL from this task's own instruction, and
    independently consistent with the one other place this world already
    has a stable identifier in the live system: cic/corpus-map/
    donatism.yaml's own `atlas_id: donatism`, which is the census movement
    id and the join key. records/worlds.yaml has NO `don` entry at all
    (confirmed by reading it directly), so no registry value is being
    contradicted; registering the world there is a later admission-track
    step, out of scope here, exactly as it was for cappadocian at its own
    B-1. `don` remains the short directory/id-prefix code; `donatism` is
    the world-identifier slug. The two are deliberately different, as they
    are for alx/alexandria-catechetical and hal/hieronymian-ascetic-
    literary.

  - author / work / edition: AUTHORED, per row, by hand. The Registry's
    `Source` column is ONE free-text cell that mixes author, work-with-
    scope, edition, translator, press, and year in a single string (row 1
    carries all six; row 27, "*Deo laudes* acclamation (epigraphic)",
    carries none of them). Splitting that cell into three schema fields is
    NOT a mechanical regex split. Several rows have no author in the
    ordinary sense at all -- row 27 (an epigraphic acclamation), row 28
    (a field category with no named publication), row 30 (a person
    attested only inside two other authors' narratives), row 2 (a
    documentary dossier whose selection is Optatus's own act) -- and each
    required reading that row's own Verification Note to phrase
    author/work/edition honestly rather than leaving a required non-blank
    field empty or inventing specificity the Registry does not have.
    Where the Registry names a `cic/texts/...` vendored file, that path is
    carried into `edition` verbatim, matching hal/cappadocian precedent
    and giving gate_edition_rights_consistency a real path to check.

  - rights_status: AUTHORED per row via the RIGHTS_* constants below (five
    buckets, keyed to the Acquisition Manifest's own three sections, not
    to the Registry's prose):
      * VENDORED_VERIFIED  -- public domain, vendored in cic/texts/, and
        the file's own identity/provenance directly confirmed by the build
        session that vendored or re-checked it (Manifest ss1 G1-G7 and the
        Registry's own Verification Notes).
      * VENDORED_INHERITED -- public domain, vendored in cic/texts/ since
        an earlier session as part of the shared library (the NPNF/ANF
        volumes), rights basis established there and not re-checked by
        this compilation pass.
      * INCOPYRIGHT_RECORDED -- in copyright, Manifest ss2 ("confirmed
        unavailable in public domain, recorded not requested"). A real
        acquisition finding, not an oversight.
      * CONSULTATION_ONLY -- in copyright, Manifest ss3 ("never vendored"
        -- modern secondary scholarship and reference instruments this
        build cites and paraphrases but never quotes as licensed material).
      * NO_EDITION_HELD -- no edition or publication is named anywhere in
        the Registry or the Manifest, so there is no rights position to
        state. Used for exactly two rows (22, 28) and stated as a negative
        rather than papered over with a plausible-sounding default.
    No row is left blank: gate_rights fails closed on blank, and the last
    three buckets each required an honest non-blank negative rather than a
    false positive. Every vendored file named in an `edition` field was
    checked to exist on disk before this script was written (a direct
    listing of cic/texts/, not a claim read off the Registry), and each
    one's own provenance header states Public Domain -- none is the CC BY
    file gate_edition_rights_consistency's second check exists for.

  - attribution_status: AUTHORED per row. Default "attributed". Carried as
    a short descriptive phrase, never forced into a binary the schema does
    not require, wherever the Registry's own Verification Note flags a
    contested, anonymous, mediated, or editorially-supplied attribution:
    rows 1 (translator attributed on external bibliographic grounds, not
    from the file's own text), 2 (documentary, but selected and
    transmitted by Optatus), 12 (Petilian, surviving only inside his
    opponent's quotation), 15 (Tyconius's own standing in the communion
    deliberately left open), 19 (the Donatist rubric is Mabillon's and
    Migne's, not the Passio's own self-description), 20 (Macrobius named
    by the work's own explicit, correcting the row's own conventional
    title), 21 (Donatist provenance assumed by Doc_01, not asserted by the
    text), 22 (transmission history genuinely contested), 27, 28, 30, 50
    (authorship proposed by one vendored authority, contested by another,
    adopted by neither).

  - discovery_channel: AUTHORED per row, taken from the Registry's own
    Discovery column (channel / instrument / date) and keyed to the SAME
    verification judgment as confidence.verification_state, so the two
    fields can never silently disagree. The Registry row number is named
    in the prose AND mirrored into external_ids.don_source_registry_row --
    a judgment call: the schema has no dedicated Registry-row field, and
    putting the number in a queryable object field rather than only in
    prose makes future cross-checking mechanical. Dates are given in the
    Registry's own ISO form here because discovery_channel is NOT one of
    gate_no_build_attribution's compiled fields -- world_core's four
    compiled fields deliberately carry no ISO date at all.

  - confidence.citation_specificity: MECHANICAL. Copied straight from the
    Registry's own Confidence (A-E) column. This is the one field in the
    record with no judgment in it.

  - confidence.verification_state: AUTHORED, but through the Registry's
    OWN stated calibration rule (its ss"Confidence calibration rule"
    paragraph), applied row by row against each row's Verification Note
    rather than transformed from the letter alone:
      * Registry A ("every specific thing this row's Licensed-For field
        names was itself directly read and verified against the vendored
        text this session") -> verified-direct.
      * Registry B where the row's Verification Note names an already-
        vendored cic/texts/ file whose identity was directly confirmed,
        with the hedge attaching to further collation rather than to the
        licensed claim -> verified-via-authority.
      * Registry B where the named work is NOT vendored at all (in
        copyright, or consultation-only) -> named-not-rechecked. A
        bibliographic record externally verified is not a text checked.
      * Registry C -> named-not-rechecked, uniformly. By the Registry's
        own definition C is "tied to a real author or work but no specific
        locus is pinpointed" -- inherently named-not-checked.
    TWO rows depart from the letter-to-state mapping, and both departures
    are stated here rather than buried:
      * Row 55 (Migne PL XI, the *Gesta*): Registry Confidence B, but
        verification_state=verified-direct. The Registry's own note
        records that the specific Licensed-For content -- numbered
        conference acts, Emeritus of Caesarea speaking, 28 confirmed
        occurrences -- WAS directly read and quoted this session; the B
        is held deliberately because most of the ~144,000-line volume is
        unread, which is a citation-specificity fact, not a verification
        fact. Keeping the two axes independent is the whole point of
        having two axes.
      * Row 28 (Numidian basilica archaeology): Registry Confidence C, but
        verification_state=unverified, the more conservative value. The
        row names no author, no work, no publication, and no site report
        anywhere -- which is the Registry's own definition of D, not C.
        This script does not renumber the Registry's own Confidence
        column (MECHANICAL, copied as C), but it declines to certify a
        verification state the row cannot support, and says so in the
        record's own body.

  - confidence.evidentiary_weight: AUTHORED per row from the Registry's
    own Licensed-For column. `contested` is used narrowly and only where
    the SOURCE OBJECT's own genuineness, identity, or transmission -- not
    merely a thesis argued in it -- is disputed: row 22 alone (the *Acta
    Saturnini*'s Donatist-versus-Catholic transmission history, which
    Step0 ss3 B2 directs be "treated as contested, not a clean witness").
    A contested THESIS inside a genuine book (Frend's social-substrate
    reading, row 23; Tengstrom, row 46) is carried in
    formation_confidence=Contested instead, keeping the two axes
    independent -- the cappadocian precedent's own rule, applied here to
    a different set of rows. `illustrative` is used where the Registry
    itself says the row licenses no specific claim yet (rows 21, 52, 53),
    or licenses only general framing (rows 26, 34, 46).

  - confidence.formation_confidence: AUTHORED per row, Article 17's five-
    level vocabulary, deliberately NOT derived from citation_specificity.
    `Documented` is used only where this record can honestly pair it with
    verified-direct AND the claim the row licenses is the text's own
    confirmed content rather than a reconstruction resting on it -- twelve
    rows (3, 4, 6, 16, 27, 32, 39, 41, 47, 48, 51, 54). Rows 19, 20, 21, 37,
    40, 49, 50, 55, 56 are verified-direct but held BELOW Documented,
    because what each was directly checked for (a heading, an explicit, a
    presence-and-extent confirmation) is narrower than the claim the
    Registry licenses from it -- row 19's Macarian dating rests on Frend,
    not on the Passio's own heading, which gives a day and no year at all.
    `Contested` is used where Doc_02 ss8 itself bands the material that
    way (rows 22, 23, 28, 46, 50). No row is assigned `Documented` without
    verified-direct or a divergence_note, checked as a hard assertion in
    emit_source() rather than left to hope -- gate_confidence_crosscheck's
    own rule, satisfied by construction.

  - confidence.divergence_note: AUTHORED. Null only where the row has
    nothing to disclose. Populated on 54 of 55 rows (the exception is row
    8, Cyprian's De Lapsis, which has nothing to disclose) -- deliberately high,
    because this Registry's Verification Notes are unusually full of real,
    disclosed limits (three unreconciled dates for Optatus; a heading that
    dates a Passio to a day with no year; a 1907 selection standing in for
    an unvendored critical edition; two vendored authorities dating the
    same sermon 23 years apart), and dropping those on the floor at
    compilation is exactly the failure this field exists to prevent.

  - sources / relations on each source record: left empty by design.
    Populating cross-references between source records would require
    reciprocal `relations` entries on both sides for gate_reciprocity, for
    no benefit this step needs. The world_core record DOES populate
    `sources`, referencing seven source ids created in this same run --
    they resolve cleanly under gate_referential because both are emitted
    together.

WORLD_CORE SLUG: `don.core.donatism`. The fleet's own eight world_core
records use a short slug naming the world itself or its core identity
(alx.core.alexandria, syr.core.syriac, desert.core.desert,
cappadocian.core.cappadocian, hal.core.hieronymian, ijc.core.imperial-
juridical, pahc.core.house-church). `donatism` follows the majority shape
-- the world's own registry name -- and matches the corpus map's own
`atlas_id`, so the id, the world_id, and the census join key all read the
same word. A descriptive alternative was considered and rejected:
`don.core.church-of-the-martyrs` is this world's own self-designation
(Doc_01 ss1) and would read beautifully, but minting a self-designation as
the record's permanent id asserts an identity claim in an address, and the
id is permanent while the identity discussion (Doc_01 ss1's Living
Tradition Status is still PENDING) is not. `don.core.african-church` was
also considered and rejected as actively wrong: this world is one of two
rival communions contesting the same African region, not the African
church.

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells (no canon-cell tagging has
happened for this world); register `don` in records/worlds.yaml (a later
admission-track step); emit any record type other than source and
world_core; touch any other world's records; emit Registry row 29.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_ROOT = REPO_ROOT / "records" / "don"
TEXTS_DIR = REPO_ROOT / "cic" / "texts"

WORLD_ID = "donatism"
SCHEMA_VERSION = 2

# ---------------------------------------------------------------- rights ---
RIGHTS_VENDORED_VERIFIED = (
    "public-domain; vendored in cic/texts/ and its identity and provenance directly confirmed by the "
    "build session that vendored or re-checked it (Source_Acquisition_Manifest.md SS1, G1-G7; the "
    "vendored file's own provenance header states Public Domain). Not re-opened for a rights re-check "
    "by this compilation pass."
)
RIGHTS_VENDORED_INHERITED = (
    "public-domain; vendored in cic/texts/ as part of the shared patristic library since an earlier "
    "session, rights basis established there (the file's own provenance header states Public Domain) "
    "and not re-checked by this compilation pass."
)
RIGHTS_INCOPYRIGHT_RECORDED = (
    "in-copyright; confirmed unavailable in the public domain and recorded not requested "
    "(Source_Acquisition_Manifest.md SS2). Not vendored, and not a vendoring candidate -- committing it "
    "would be redistribution, per cic/texts/README.md's own rule. Consultable through a library without "
    "being vendored, which is a different thing from unusable."
)
RIGHTS_CONSULTATION_ONLY = (
    "in-copyright modern scholarship; consultation-only, never vendored "
    "(Source_Acquisition_Manifest.md SS3). Cited and paraphrased by this build, never quoted as licensed "
    "vendored material. Bibliographic record only -- the volume itself was not opened by this "
    "compilation pass."
)
RIGHTS_NO_EDITION_HELD = (
    "No rights position is stated, because no edition or publication is named for this row anywhere in "
    "Source_Registry.md or Source_Acquisition_Manifest.md. Not vendored; nothing to vendor until a "
    "specific edition or publication is identified. Recorded as an honest negative rather than defaulted "
    "to a plausible-sounding status this build has not established."
)

# ------------------------------------------------------------------ rows ---
# Each entry: row, slug, author, work, edition, rights, attribution,
# discovery, (cite, verif, weight, formation), divergence, body.
ROWS: list[dict] = [
    dict(
        row=1, slug="optatus-against-the-donatists",
        author="Optatus of Milevis",
        work="Against the Donatists (De schismate Donatistarum), Books I-VII (c. 366-367, revised c. 385)",
        edition="English translation by O.R. Vassall-Phillips (London: Longmans, Green & Co., 1917), "
                "vendored as cic/texts/optatus_against-the-donatists.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Optatus of Milevis. The 1917 translation's attribution to "
                    "O.R. Vassall-Phillips rests on external bibliographic grounds recorded in the "
                    "vendored file's own header -- the file's own text does not name a translator.",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01. Registry row 1. Not "
                  "independently re-collated against the full text this pass beyond the checks logged at "
                  "Registry rows 30 and 1 themselves.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Three dates for the work appear across this build's own sources and are NOT "
                   "reconciled: the corpus map and the Registry's own heading give c. 366-367 revised "
                   "c. 385; the vendored file's own apparatus says about 370; the file's own provenance "
                   "header says c. 366-393. All three point to the same two-edition history and none is "
                   "treated as more authoritative. Ziwsa's critical edition (Registry row 38) is "
                   "vendored but its apparatus has not been read for that purpose; Labrousse (row 44) "
                   "has not been acquired.",
        body="This world's earliest substantial narrative source: hostile and external to it, but "
             "contemporary and primary, not secondary (Doc_01 SS2). Licensed for the schism-origins "
             "narrative, the World #6/#8 boundary evidence at Doc_01 SS6, and the Lucilla material "
             "(Registry row 30). Corpus map role: context; used as hostile/etic narrative per its own "
             "genre, never as neutral report. AUTHORED here rather than copied: the Registry's Source "
             "cell packs author, work, book range, two composition dates, translator, press, and year "
             "into one string; splitting it into author/work/edition and deciding which of the three "
             "circulating dates the `work` field should carry was this compilation's own judgment, "
             "resolved by carrying the Registry's own heading and disclosing the other two in "
             "divergence_note rather than picking a winner.",
    ),
    dict(
        row=2, slug="optatus-appendix-of-documents",
        author="Various -- Roman court officials, conciliar scribes, and the emperor Constantine; "
               "assembled and transmitted as Optatus of Milevis's own appendix",
        work="Appendix of Documents (the anti-Donatist dossier): Acta Purgationis Felicis (314), "
             "Gesta apud Zenophilum (320), Constantine's letters, the Council of Arles' 314 letter to "
             "Silvester, Acts of the Council of Cirta (305, date disputed), Anulinus's relatio (313)",
        edition="Within cic/texts/optatus_against-the-donatists.txt (the appendix printed with the 1917 "
                "Vassall-Phillips translation, mapped as Appendices I-XVI); a related but not "
                "confirmed-identical ten-document appendix stands in Ziwsa's critical edition "
                "(Registry row 38)",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="documentary. The individual items are genuine court acts, conciliar acts, and "
                    "imperial correspondence, but their selection and transmission is Optatus's own act "
                    "-- this dossier sits inside, not outside, this world's Author Gravity "
                    "concentration (Registry row 2).",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01. Registry row 2.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="The Council of Cirta's own date is genuinely contested in the scholarship (305 "
                   "versus 307 or later), and Doc_02 SS8 bands it as Contested; the Registry carries "
                   "305 with the dispute marked in the row itself. The corpus map separately flags "
                   "Ziwsa's ten-document appendix as related in kind to this sixteen-item one but not "
                   "confirmed identical in content -- the two document sets have not been compared.",
        body="The contemporary legal-documentary record of the schism's initiating events (Doc_01 SS5, "
             "Cells 1A/1B) and of the 313 appeal to Constantine (Doc_01 SS5, SS6). AUTHORED: this row "
             "has no author in the ordinary sense, and the `author` field states the compound reality "
             "rather than either fabricating a single name or leaving a schema-required field to say "
             "nothing.",
    ),
    dict(
        row=3, slug="augustine-on-baptism-against-the-donatists",
        author="Augustine of Hippo",
        work="On Baptism, Against the Donatists (De baptismo contra Donatistas), 7 books, c. 400",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. IV, vendored as "
                "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml; the critical Latin text "
                "(De baptismo libri septem) also stands in the Petschenig CSEL volume, Registry row 39",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01; Book I chapters 1 and 5: "
                  "direct text search and read against "
                  "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml / 2026-09-01. "
                  "Registry row 3.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="The A rating, and this record's Documented, cover Book I chapters 1 and 5 only -- "
                   "the Maximianist rebaptism-consistency argument, character-verified against the "
                   "vendored file. The remaining six books were not independently re-collated and are "
                   "not the basis of any claim drawn from this row.",
        body="Licensed for rebaptism theology, the ecclesial-purity gravity candidate (Doc_01 SS3), and "
             "the Maximianist rebaptism-consistency argument quoted directly at Book I ch. 1 SS2 and "
             "ch. 5 SS7 (Doc_02 SS1). Doc_01 SS4's binding on the Maximianist material is discharged "
             "directly from this row, not from Registry rows 17 or 18. Corpus map role: tradition -- "
             "this is this world's opponent writing against it, and the Writing-From-Inside Principle "
             "(Article 23) governs how a Representative eventually characterises him.",
    ),
    dict(
        row=4, slug="augustine-answer-to-petilian",
        author="Augustine of Hippo",
        work="Answer to the Letters of Petilian, the Donatist (Contra litteras Petiliani), 3 books "
             "(Book I c. 400, Book III c. 401-402 on the NPNF Prolegomena's own dating, Registry row 31)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. IV, vendored as "
                "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml. The critical Latin text "
                "(CSEL 52, Pars II) is confirmed ABSENT from the vendored Petschenig scan (Registry "
                "row 39) -- checked directly, found only as a cross-reference abbreviation.",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01; the Optatus Gildonianus "
                  "passages (II.9, II.23, II.84) and the Felicianus passage (II.52): direct text search "
                  "and read against cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml / "
                  "2026-09-01. Registry row 4.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Two disclosures the Registry makes and this record carries rather than smooths. "
                   "(1) The identification of Optatus Gildonianus as a DONATIST BISHOP of Thamugadi "
                   "rather than an imperial official is stated in the companion volume's editorial note "
                   "on On Baptism II.11.16, not in this work's own endnotes -- an editor's "
                   "identification, not the text's. (2) The phrase 'whom you hold to be a priest' "
                   "(II.52.120) refers to Felicianus of Musti, named by its own preceding sentence, and "
                   "must not be attached to Optatus Gildonianus. The remainder of the work was not "
                   "re-collated.",
        body="The fullest surviving Donatist voice IN THE VENDORED CORPUS -- Petilian of Constantina's "
             "own letters, preserved entirely inside their refutation, quoted clause by clause "
             "(Registry row 12 carries that voice as its own row). Also licensed for the Optatus "
             "Gildonianus material: a Donatist bishop 'advancing with a military force' whom the "
             "Donatists 'were afraid to condemn though they had long known his wickedness' (II.9), "
             "confirming he was never convicted.",
    ),
    dict(
        row=5, slug="augustine-correction-of-the-donatists",
        author="Augustine of Hippo",
        work="The Correction of the Donatists (De correctione Donatistarum, Letter 185, c. 417), "
             "addressed to the tribune Boniface",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. IV, vendored as "
                "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01. Registry row 5. Addressee "
                  "and date confirmed against Doc_01 SS2 -- a cross-check against this build's own "
                  "document, not against the text.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="The confirmation logged for this row is a cross-check of addressee and date against "
                   "Doc_01 SS2, not a reading of the letter itself. A vendored, rights-confirmed text "
                   "stands behind the citation; this pass did not reopen it.",
        body="Augustine's after-the-fact defence of imperial coercion against this world, and one of "
             "Doc_01 SS2's named Historical Catalysts. Licensed for the imperial-coercion defence and "
             "the World #6 boundary discussion (Doc_01 SS6). Read against this world's own "
             "refusal-of-imperial-legitimacy gravity, this is the opposing case stated by the party "
             "that won it.",
    ),
    dict(
        row=6, slug="augustine-donatist-correspondence",
        author="Augustine of Hippo",
        work="Donatist correspondence: Letters XXIII, XLIII, XLIV, LIII, LXXVI, LXXXVII, LXXXVIII, "
             "LXXXIX, XCIII, CXXXIX, CLXXIII (11 letters)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. I, vendored as "
                "cic/texts/npnf101_augustine-confessions-letters.xml; split from a 168-letter volume by "
                "its own div3 markup",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01; Letter LXXXVII and Letter "
                  "XLIII: direct text search and read against "
                  "cic/texts/npnf101_augustine-confessions-letters.xml / 2026-09-01. Registry row 6.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="The A rating, and this record's Documented, cover two of the eleven letters -- "
                   "LXXXVII and XLIII, both read in full and character-verified. The other nine were "
                   "not re-collated. Two further limits the Registry states and this record carries: "
                   "Letter LXXXVII is licensed for its conciliar-authority reproach ONLY (SS6, which "
                   "names the Maximianists explicitly) and NOT for any claim that the proconsular "
                   "machinery was invoked specifically against them -- SS7-SS8 concern the civil powers "
                   "and Romans 13 generally and do not mention them. And the corpus map's own stated "
                   "warrant for classifying this cluster `role: context`, distinct from rows 3-5's "
                   "`role: tradition`, is internally inconsistent (Doc_02 SS1): an observed discrepancy "
                   "in a generated file, recorded here, not corrected here.",
        body="Licensed for the broader Donatist-Caecilianist exchange. Letter XLIII SS26 is licensed "
             "separately and specifically for the second, unnamed woman behind the Maximianist "
             "schism's own council against Primian, whom Augustine himself parallels to Lucilla in the "
             "same paragraph (Doc_02 SS6; Registry row 30) -- read in full, dated a.d. 397 in the "
             "vendored volume.",
    ),
    dict(
        row=7, slug="cyprian-epistles",
        author="Cyprian of Carthage",
        work="Epistles",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01; corpus map role `antecedent`, "
                  "ruled 2026-08-26. Registry row 7. Not independently re-collated.",
        cite="B", verif="named-not-rechecked", weight="load-bearing", formation="Widely Accepted",
        divergence="Vendored and rights-confirmed, but the Registry's own note hedges the citation "
                   "itself -- 'not independently re-collated this session' -- so this record does not "
                   "claim verification via authority for a specific locus it cannot name. Antecedent, "
                   "not native: Cyprian sits inside not-yet-built World #8 on the Step 0 Conclusion's "
                   "own placement, and this world's reliance on him is an inheritance from a shared "
                   "root rather than a claim on him (Doc_01 SS6).",
        body="Load-bearing for this world's own formation logic, not merely background: Doc_01 SS5 and "
             "SS6 make the Cyprianic rigorist tradition -- rebaptism theology, ministerial-purity "
             "concerns -- this world's direct doctrinal and institutional inheritance, not an invention "
             "at 311/312. Licensed for the A1/A2 continuity reasoning (Step0 SS2) and the "
             "rebaptism-theology origin (Doc_01 SS5).",
    ),
    dict(
        row=8, slug="cyprian-de-lapsis",
        author="Cyprian of Carthage",
        work="On the Lapsed (De lapsis)",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01; corpus map role `antecedent`, "
                  "ruled 2026-08-26. Registry row 8.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Widely Accepted",
        divergence=None,
        body="Licensed for the traditio and lapsed-clergy theological background (Doc_01 SS5) -- the "
             "third-century argument about how to treat those who failed under persecution, which this "
             "world's own founding dispute reopens two persecutions later over a different question "
             "(surrendering scripture, not sacrificing).",
    ),
    dict(
        row=9, slug="cyprian-de-unitate",
        author="Cyprian of Carthage",
        work="On the Unity of the Church (De unitate ecclesiae)",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01; corpus map role `antecedent`, "
                  "ruled 2026-08-26. Registry row 9.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Widely Accepted",
        divergence="The corpus map's own note records that this treatise 'was written against the "
                   "Novatianist schism among others' -- which is why the Registry keeps a Named "
                   "Comparandum row (row 29) guarding against reading Novatianism into this world's "
                   "own rebaptism practice. That comparandum row is deliberately not compiled as a "
                   "source record for this world; see the world_core record's own body.",
        body="Licensed for ecclesial purity and unity theological background.",
    ),
    dict(
        row=10, slug="seventh-council-of-carthage-256-anf05",
        author="Cyprian of Carthage and the eighty-seven bishops of the Seventh Council of Carthage",
        work="The Seventh Council of Carthage under Cyprian (September 256), on the baptism of heretics "
             "-- as recorded within the Cyprianic corpus",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01; corpus map role `antecedent`, "
                  "corpus-map confidence `assigned`. Registry row 10.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="A DISTINCT ENTRY from Registry row 11, which is a second telling of the same "
                   "council from a conciliar-history vantage at lower confidence. Doc_02 SS1 and SS9 "
                   "item 6 both direct that the two must not be merged and that row 11 must never be "
                   "cited at this row's confidence.",
        body="The rebaptism precedent this world's own founders read themselves as continuing: the "
             "council at which the African episcopate, against Rome, held that baptism outside the true "
             "church is no baptism. Licensed for that precedent and for the A1/A2 continuity reasoning.",
    ),
    dict(
        row=11, slug="acts-council-of-carthage-under-cyprian-npnf214",
        author="The Council of Carthage under Cyprian (256), as transmitted in the seven-ecumenical-"
               "councils volume",
        work="The Acts of the Council of Carthage under Cyprian (256) -- the conciliar-history telling, "
             "distinct from the Cyprianic-corpus record at Registry row 10",
        edition="Nicene and Post-Nicene Fathers, Series II, vol. XIV, vendored as "
                "cic/texts/npnf214_seven-ecumenical-councils.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01; corpus map role `tradition`, "
                  "corpus-map confidence `provisional`. Registry row 11.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Two things this record must not be silently smoothed on. (1) The vendored volume's "
                   "own section heading dates the council 'a.d. 257'; the Registry follows the corpus "
                   "map's September-256 dating as the historically established date and records the "
                   "volume's own heading as a discrepancy worth noting, not a second date to reconcile. "
                   "(2) This row is NOT to be cited at Registry row 10's confidence -- same event, "
                   "different evidentiary strength, kept distinct on Doc_02 SS1 and SS9 item 6's own "
                   "instruction.",
        body="Kept as its own row precisely so that a future claim cannot quietly inherit row 10's "
             "assigned confidence by way of this provisional telling.",
    ),
    dict(
        row=12, slug="petilian-of-constantina-letters",
        author="Petilian of Constantina (Cirta), Donatist bishop",
        work="Petilian's letters, surviving only as quoted -- clause by clause -- inside Augustine's "
             "Answer to the Letters of Petilian (Registry row 4)",
        edition="No independent edition exists. Held within "
                "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, inside its refutation.",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed to Petilian of Constantina by Augustine's own quotation. No independent "
                    "manuscript transmission survives; paraphrase is distinguished from direct "
                    "quotation only where the containing text makes that checkable (Registry row 12).",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01. Registry row 12.",
        cite="C", verif="named-not-rechecked", weight="load-bearing", formation="Widely Accepted",
        divergence="Doc_02 SS8 bands any claim about Petilian's own fuller argument, beyond what "
                   "Augustine's selection preserves, as Inferential/Thin. This record's Widely Accepted "
                   "covers the existence and preserved substance of the quoted voice, not the shape of "
                   "the argument Augustine chose not to reproduce. The selection effect is not "
                   "incidental to this source -- it IS this source.",
        body="This world's own fullest surviving primary voice in the vendored corpus (Doc_02 SS2), and "
             "one of only two well-attested named Donatist figures who reach us with a distinct "
             "evidentiary channel -- Petilian via hostile quotation, Emeritus of Caesarea via the 411 "
             "court transcript (Registry rows 14, 55). Monceaux's Tome VI (Registry row 53) opens with "
             "a dedicated chapter on Petilian that has not been read and could corroborate or complicate "
             "this row.",
    ),
    dict(
        row=13, slug="code-of-canons-african-church-419",
        author="The Council of Carthage (419) and the African episcopate whose earlier canons it "
               "compiles",
        work="The Code of Canons of the African Church (Council of Carthage, 419)",
        edition="Nicene and Post-Nicene Fathers, Series II, vol. XIV, vendored as "
                "cic/texts/npnf214_seven-ecumenical-councils.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/donatism.yaml / 2026-09-01; corpus map role `context`, "
                  "corpus-map confidence `provisional`. Registry row 13.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="The canons mostly originate c. 397-407: this register compiles rather than "
                   "legislates fresh (Step0_Movement_Scope_Confirmation.md SS3, B1). A claim dated to "
                   "419 from this source is dating the compilation, not the canon.",
        body="The institutional record of Donatist-clergy reception on the Caecilianist side -- the "
             "receiving church's own administrative trace of the contest, from within this world's own "
             "window and its own region.",
    ),
    dict(
        row=14, slug="gesta-collationis-carthaginiensis-411",
        author="The notaries of the 411 Conference of Carthage, under the tribune and notary Marcellinus",
        work="Gesta Collationis Carthaginiensis -- the acts of the 411 Conference of Carthage",
        edition="The modern critical editions -- Serge Lancel (ed.), Actes de la Conference de Carthage "
                "en 411, Sources Chretiennes 194, 195, 224, 373 (Paris: Cerf, 1972-1991), and Gesta "
                "conlationis Carthaginiensis anno 411, CCSL 149A (Turnhout: Brepols, 1974) -- are in "
                "copyright and NOT vendored. The public-domain route actually held is the Migne "
                "Patrologia Latina Tomus XI printing, vendored as "
                "cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt (Registry row 55).",
        rights=RIGHTS_INCOPYRIGHT_RECORDED,
        attribution="documentary -- an imperial court transcript, not an authored work. Its mediation "
                    "is a notary's own choices about what to record, not an adversary's selection for "
                    "the purpose of refutation (Doc_02 SS6).",
        discovery="builder-prior-knowledge, cross-checked via WebSearch / 2026-09-01; CORRECTED by "
                  "direct text search and read against "
                  "cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt / 2026-09-07. "
                  "Registry row 14.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="This row carried a WRONG determination for six days and the correction is part of "
                   "the record, not tidied away: the original 'confirmed unavailable in the public "
                   "domain' finding was made without working network access to actually check it. A "
                   "full Migne printing of the Gesta itself is public domain and is now vendored "
                   "(Registry row 55). Confidence is held at B, not raised: the vendored file's text "
                   "has not been read in full or excerpted to a clean boundary, and this row's Author "
                   "Gravity assessment has not been performed against it.",
        body="The single most structurally different piece of evidence this world has: Donatist "
             "bishops' own recorded words at length, in real exchange with named Catholic bishops and "
             "the presiding tribune -- Emeritus of Caesarea foremost, with numbered acts naming him "
             "speaking. It does not remove all mediation, but it removes the specific mediation "
             "mechanism this world's central evidentiary problem names throughout Doc_02: selection by "
             "an adversary FOR THE PURPOSE OF REFUTATION. Doc_02 SS9 item 1a(i) names a systematic "
             "reading of the Donatist bishops' recorded interventions as real, substantive future work.",
    ),
    dict(
        row=15, slug="tyconius-liber-regularum",
        author="Tyconius",
        work="Liber Regularum (The Book of Rules)",
        edition="F.C. Burkitt's 1894 critical edition (Registry row 41), vendored as "
                "cic/texts/tyconius_liber-regularum_burkitt1894.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Tyconius. His formal standing within the Donatist communion is "
                    "DELIBERATELY LEFT OPEN (Doc_01 SS4): the standard account holds that Parmenian and "
                    "a Donatist council condemned him c. 380 over his universalist ecclesiology and "
                    "that he never joined the Catholic church, and no clerical office is attested for "
                    "him. Doc_01 SS4 finds him a condemned individual dissenting voice, not the head of "
                    "a rival pattern of communal life -- strand-singular, on a finding that does not "
                    "take a position on his own formal standing.",
        discovery="builder-prior-knowledge, cross-checked via WebSearch / 2026-09-01; file identity "
                  "directly confirmed against cic/texts/tyconius_liber-regularum_burkitt1894.txt. "
                  "Registry row 15; Source_Acquisition_Manifest.md SS1 G1 discharged.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="What was confirmed is the file's identity -- preface, table of contents, and "
                   "introduction all present and correctly naming Tyconius and the Liber Regularum. "
                   "What was NOT done is the thing this text was acquired for: the seven Rules' own "
                   "doctrinal content has not been read, so the Author Gravity assessment Doc_02 SS1 "
                   "names as the single largest available correction to this world's own Author Gravity "
                   "concentration remains unperformed. The file is raw, uncorrected OCR.",
        body="The one substantial independently-surviving Donatist-side interpretive text, and Doc_01 "
             "SS3's own strongest counter-example to this world's otherwise thin and largely reactive "
             "doctrinal record. Doc_07 SS3B declines to open a separate Interpretive Ecology lens for "
             "this world precisely because Tyconius is the single case and its content is already "
             "carried inside the Doctrinal/Philosophical lens.",
    ),
    dict(
        row=16, slug="codex-theodosianus-book-16",
        author="Roman imperial legislation, fourth and fifth centuries, compiled 438",
        work="Codex Theodosianus, Book 16 -- including 16.5.52 on the circumcelliones and the 405 Edict "
             "of Unity",
        edition="Th. Mommsen and Paul M. Meyer (eds.), Theodosiani Libri XVI, Voluminis I Pars "
                "Posterior: Textus cum Apparatu (Berlin: Weidmann, 1905), vendored as "
                "cic/texts/theodosianus-16_mommsen-meyer1905.txt (Registry row 51)",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="documentary",
        discovery="builder-prior-knowledge, cross-checked via WebSearch / 2026-09-01; direct text "
                  "search and read against cic/texts/theodosianus-16_mommsen-meyer1905.txt / "
                  "2026-09-07. Registry row 16, upgraded to A on that reading.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Two findings this record carries because they bound what the row licenses. (1) Law "
                   "XVI.5.52, headed '412 Ian. 30', was read in full and contains 'circumcelliones "
                   "argenti pondo decem' verbatim -- a graduated fine schedule by social rank for "
                   "Donatists who do not return to the Catholic church, with Circumcellions the only "
                   "listed rank assessed in silver rather than gold. (2) The agonistici self-"
                   "designation does NOT appear anywhere in this file (checked directly, zero matches): "
                   "it is confirmed NOT to be Theodosian Code vocabulary, and its own source passage "
                   "remains unidentified (Doc_02 SS9 item 1a(v)). Beyond 16.5.52 and Book XVI's heading "
                   "structure, the text has not been collated.",
        body="The independent, non-polemical attestation that the Circumcellion group existed as its "
             "own legally-marked category -- the evidentiary hinge Doc_01 SS7 item 2 and Doc_02 SS6 "
             "both turn on when separating the group's attested existence from its "
             "hostile-polemically-shaped characterisation. Five prior acquisition attempts for this "
             "edition all returned the wrong volume (the Prolegomena, not Book 16's text), and a sixth "
             "download was rejected outright on source-integrity grounds; the standing 16.5.52 citation "
             "gap is closed by the edition itself, not by a substitute.",
    ),
    dict(
        row=17, slug="augustine-contra-cresconium",
        author="Augustine of Hippo",
        work="Contra Cresconium, 4 books (c. 406; some scholarship as late as 409)",
        edition="Michael Petschenig (ed.), CSEL 51/53 (Registry row 39), vendored as "
                "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="builder-prior-knowledge (Doc_01 SS4 binding) / field knowledge / 2026-09-01; file "
                  "presence and identity confirmed by direct file check against "
                  "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt. "
                  "Registry row 17; Source_Acquisition_Manifest.md SS1 G5 discharged.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Widely Accepted",
        divergence="Identity confirmed -- headed 'CONTRA CRESCONIVM', four books, with its own internal "
                   "book-division markers -- but this row's specific Licensed-For content (Cresconius's "
                   "own arguments, the fuller rebaptism material, the Bagai proceedings in more detail) "
                   "has NOT been read; confidence stays at B until it is. Doc_02 SS9 item 10 flags that "
                   "the Maximianist-reception material currently resting on the NPNF Prolegomena's "
                   "summary (Registry row 31) should be re-verified against this primary Latin text in "
                   "a future pass, and is not upgraded merely because the text is now accessible. "
                   "HOMONYM FLAG: the Maximian of this work (the deposed deacon whose 393 consecration "
                   "names the Maximianist schism) is a different person from the martyr Maximian of the "
                   "Passio Isaac et Maximiani (Registry row 20).",
        body="Corroborating rather than load-bearing by the Registry's own disposition: Doc_01 SS4's "
             "binding on the Maximianist material is discharged directly from Augustine's vendored "
             "On Baptism (Registry row 3), not from this row.",
    ),
    dict(
        row=18, slug="augustine-contra-epistulam-parmeniani",
        author="Augustine of Hippo",
        work="Contra epistulam Parmeniani, 3 books (c. 400)",
        edition="Michael Petschenig (ed.), CSEL 51/53 (Registry row 39), vendored as "
                "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="builder-prior-knowledge (Doc_01 SS4 binding) / field knowledge / 2026-09-01; file "
                  "presence and identity confirmed by direct file check against "
                  "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt. "
                  "Registry row 18; Source_Acquisition_Manifest.md SS1 G5 discharged.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Widely Accepted",
        divergence="Identity confirmed by the work's own closing formula ('Explicit liber tertius sci "
                   "augustini epi. contra parmeniani epistolam'), but the specific Cebarsussi and Bagai "
                   "sentence quotations this row is licensed for have NOT been read; confidence stays "
                   "at B until they are. The same Maximian/Maximian homonym flagged at Registry row 17 "
                   "applies here.",
        body="Licensed for the Maximianist schism's own conciliar sentences as Augustine quotes them, "
             "and for Parmenian's own position -- Parmenian being the Donatist bishop of Carthage whose "
             "letter this answers, and Optatus of Milevis's own opposing subject (Doc_01 SS2).",
    ),
    dict(
        row=19, slug="passio-marculi",
        author="Anonymous (Donatist)",
        work="Passio Marculi -- the passion of Marculus, killed under the imperial commissioner Macarius",
        edition="J.-P. Migne (ed.), Patrologia Latina vol. 8, the Monumenta Vetera ad Donatistarum "
                "historiam pertinentia; vendored (relevant excerpt only) as "
                "cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="anonymous. The Donatist designation comes from Mabillon's and Migne's own "
                    "descriptive catalogue rubric ('PASSIO MARCULI SACERDOTIS DONATISTAE, QUI SUB "
                    "MACARIO INTERFECTUS A DONATISTIS PRO MARTYRE HABEBATUR'), NOT from the Passio's "
                    "own self-description, whose own heading reads simply 'INCIPIT PASSIO BENEDICTI "
                    "MARTYRIS MARCULI' (Registry row 19).",
        discovery="builder-prior-knowledge, cross-checked via WebSearch (Patrologia Latina vol. 8, "
                  "cols. 760-766) / 2026-09-01; direct text search and read against "
                  "cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt / 2026-09-01. Registry row 19; "
                  "Source_Acquisition_Manifest.md SS1 G4 discharged.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Widely Accepted",
        divergence="Held BELOW Documented despite verified-direct, and the reason matters. What was "
                   "directly read is the Passio's own heading, which gives '8 (al. die 5) kal. "
                   "decembris' -- A DAY ONLY, NO YEAR. The 'ANNO DOMINI 348' above the catalogue entry "
                   "is the volume's own dated section marker, not a date the Passio itself states, and "
                   "the 347-348 Macarian-repression dating rests on the standard field literature "
                   "(Frend, Registry row 23), not on the text. The Migne column numbers 760-766, "
                   "carried over from a WebSearch finding, are not independently re-confirmed -- no "
                   "inline column marker was found in this OCR. No free public-domain English "
                   "translation was found; Tilley's standard modern edition (row 35) is in copyright.",
        body="One of the martyr narratives at the centre of this world's own identity (Doc_01 SS1) and "
             "one of the four texts that speak AS Donatists rather than being spoken about (Doc_02 "
             "SS6). Subject to the five-item formation-narrative evaluation at Doc_02 SS4. Monceaux "
             "(Registry row 40) is a second, independent public-domain route to it.",
    ),
    dict(
        row=20, slug="passio-isaac-et-maximiani",
        author="Macrobius, Donatist bishop (described in the same volume as the Donatists' own hidden "
               "bishop in the city of Rome)",
        work="Passio Isaac et Maximiani -- in the vendored text, Macrobius's own letter to the "
             "congregation of Carthage on the passion of the martyrs Isaac and Maximianus",
        edition="J.-P. Migne (ed.), Patrologia Latina vol. 8, the Monumenta Vetera ad Donatistarum "
                "historiam pertinentia; vendored (relevant excerpt only) as "
                "cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Macrobius by the work's own rubric ('PASSIO MAXIMIANI ET ISAAC "
                    "DONATISTARUM AUCTORE MACROBIO') and its own explicit ('Explicit epistola "
                    "beatissimi martyris Macrobi ad plebem Karthaginis...'). This corrects the row's "
                    "own conventional title: it is Macrobius's own letter to a congregation, NOT an "
                    "anonymous passio with an epistle appended to it (Registry row 20).",
        discovery="builder-prior-knowledge, cross-checked via WebSearch (Patrologia Latina vol. 8) / "
                  "2026-09-01; direct text search and read against "
                  "cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt / 2026-09-01. Registry row 20; "
                  "Source_Acquisition_Manifest.md SS1 G4 discharged.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Widely Accepted",
        divergence="Held BELOW Documented for the same reason as Registry row 19: the 347-348 Macarian "
                   "dating rests on the standard field literature, not on this text's own heading. "
                   "HOMONYM FLAG: the Maximian martyred here is a different person from the Maximian of "
                   "the Maximianist schism (Registry rows 17, 18) -- both are prominent in this "
                   "Registry and the two are easy to conflate.",
        body="A named Donatist bishop writing in his own voice to his own congregation -- one of the "
             "very few places in this world's record where that happens without a hostile hand in "
             "between. Doc_07 SS4 identifies this letter's burning, joyful eagerness as the source of "
             "the specific emotional register this world's Experiential lens can document at all: "
             "persecution did not merely happen to this world's emotional life, it produced the texts "
             "that emotional life can be read from.",
    ),
    dict(
        row=21, slug="liber-genealogus",
        author="Anonymous African compiler",
        work="Liber Genealogus -- transmitted as Additamentum II to the Chronographus Anni CCCLIIII",
        edition="Theodor Mommsen (ed.), Chronica Minora Saec. IV-VII, Vol. I, MGH Auctores "
                "Antiquissimi IX (Berlin: Weidmann, 1892), vendored as "
                "cic/texts/chronica-minora-liber-genealogus_mommsen1892.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="anonymous. Donatist provenance is ASSUMED by Doc_01 SS5 Cell 3B and is not "
                    "asserted by the text itself; what Mommsen's own editorial introduction confirms is "
                    "the African, early-fifth-century composition and the manuscript recensions' own "
                    "internal datings, not a confessional attribution (Registry row 21).",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01; direct text search and read "
                  "against cic/texts/chronica-minora-liber-genealogus_mommsen1892.txt / 2026-09-08. "
                  "Registry row 21, upgraded on that reading.",
        cite="A", verif="verified-direct", weight="illustrative", formation="Widely Accepted",
        divergence="The A rating covers EXISTENCE, IDENTITY, PUBLICATION DATE, AND MOMMSEN'S OWN DATING "
                   "DISCUSSION ONLY -- not a content-integration pass. The genealogical content itself, "
                   "and the remainder of this multi-text MGH volume, have not been read for any "
                   "specific Donatism claim. Mommsen dates composition to the start of the fifth "
                   "century in Africa, with recensions internally dated to 427 (Sangallensis), 438 "
                   "(Florentinus), and 455 (Lucensis, via a Geiseric regnal-year reference) -- all "
                   "within or immediately adjacent to this world's own 311-439 window.",
        body="evidentiary_weight is `illustrative` because the Registry itself says so: this row is "
             "'not yet licensed for any specific claim', with its use to be determined at Doc_09. "
             "Recorded here at that weight rather than promoted on the strength of the acquisition.",
    ),
    dict(
        row=22, slug="acta-saturnini-abitinian-martyrs",
        author="Anonymous",
        work="Acts of the Abitinian Martyrs (Acta Saturnini) -- the 304 Diocletianic persecution",
        edition="No edition is named. Not vendored; no specific printing, translation, or manuscript "
                "basis is identified anywhere in Source_Registry.md or "
                "Source_Acquisition_Manifest.md.",
        rights=RIGHTS_NO_EDITION_HELD,
        attribution="anonymous, and the transmission history itself is genuinely contested in the "
                    "scholarship -- whether the surviving text is a Donatist or a Catholic transmission "
                    "is not settled. Step0_Movement_Scope_Confirmation.md SS3 B2 directs that it be "
                    "treated as contested, not as a clean witness for either party.",
        discovery="builder-prior-knowledge / field knowledge (Step0 build thread) / 2026-09-01. "
                  "Registry row 22. Flagged in the Registry's own priority second-opinion review list.",
        cite="C", verif="named-not-rechecked", weight="contested", formation="Contested",
        divergence="The one row in this Registry where evidentiary_weight is `contested` rather than "
                   "the contest being carried in formation_confidence alone: what is disputed here is "
                   "the SOURCE OBJECT's own transmission and confessional provenance, not a thesis "
                   "argued about it. No edition is held, so nothing about this text has been checked "
                   "against a text at all.",
        body="Named for the martyr-cult narrative of the 304 Diocletianic persecution and carried into "
             "Doc_02 SS4's five-item formation-narrative evaluation -- but carried as a contested "
             "witness. AUTHORED, and flagged upward: this is one of only two rows in the whole Registry "
             "for which no edition and no rights position exists to state, and rights_status says that "
             "as a negative rather than defaulting to a plausible-sounding status this build has not "
             "established.",
    ),
    dict(
        row=23, slug="frend-the-donatist-church",
        author="W.H.C. Frend",
        work="The Donatist Church: A Movement of Protest in Roman North Africa (Oxford, 1952)",
        edition="Oxford, 1952 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge, with the bibliographic record externally "
                  "verified against publisher records / 2026-09-01. Registry row 23. Flagged in the "
                  "Registry's own priority second-opinion review list.",
        cite="B", verif="named-not-rechecked", weight="corroborating", formation="Contested",
        divergence="The contest here is a THESIS inside a genuine book, not the book's own genuineness "
                   "-- so it is carried in formation_confidence, not in evidentiary_weight. Frend's "
                   "native-social-protest reading of Donatism's rural strength is named by Doc_02 SS5 "
                   "and SS8 as contested rather than settled, and the Registry flags this row for "
                   "priority second-opinion review BEFORE that thesis specifically supports any claim: "
                   "it is the most contested single argument this Registry draws on it for. Shaw "
                   "(Registry row 24) is the standard corrective; Tengstrom (row 46) and Brown (row 26) "
                   "are the other named counterpoints.",
        body="The standard field reference for the movement's general history, the Circumcellion "
             "question, and the rural/urban and cultural-environment context, including terminal-record "
             "material. Not independently re-read; the bibliographic record was externally verified.",
    ),
    dict(
        row=24, slug="shaw-sacred-violence",
        author="Brent Shaw",
        work="Sacred Violence: African Christians and Sectarian Hatred in the Age of Augustine "
             "(Cambridge, 2011)",
        edition="Cambridge University Press, 2011 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge, with the bibliographic record externally "
                  "verified against publisher records / 2026-09-01. Registry row 24. Flagged in the "
                  "Registry's own priority second-opinion review list.",
        cite="B", verif="named-not-rechecked", weight="corroborating",
        formation="Dominant Modern Reconstruction",
        divergence="Doc_02 SS8 puts the reading of the Circumcellion category as substantially, though "
                   "not wholly, a hostile rhetorical construction at Dominant Modern Reconstruction, "
                   "and Shaw is the standard treatment of that shaping -- hence DMR here rather than "
                   "Widely Accepted. The Registry flags this row for priority second-opinion review "
                   "before it supports the specific corrective-to-Frend claim beyond general "
                   "orientation.",
        body="The standard corrective to Frend's social-substrate reading (Doc_02 SS5), and the field's "
             "standard treatment of how hostile polemic shaped the Circumcellion/agonistici picture. "
             "Doc_02 SS6 keeps the group's ATTESTED EXISTENCE (Codex Theodosianus 16.5.52, Registry "
             "rows 16 and 51) rigorously separate from its polemically-shaped CHARACTERISATION, which "
             "is what this row bears on.",
    ),
    dict(
        row=25, slug="tilley-bible-in-christian-north-africa",
        author="Maureen A. Tilley",
        work="The Bible in Christian North Africa: The Donatist World (Fortress Press, 1997)",
        edition="Fortress Press, 1997 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge, with the bibliographic record externally "
                  "verified / 2026-09-01. Registry row 25. Flagged in the Registry's own priority "
                  "second-opinion review list, and separately at Doc_02 SS9 item 3.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Recalled from general field knowledge and NOT independently checked -- flagged for "
                   "priority second-opinion review before supporting any specific vivid claim, because "
                   "it is licensed for a load-bearing category (Donatist hermeneutics and "
                   "self-understanding) on a discovery channel that was not independently re-collated. "
                   "That combination is precisely the Registry's own review trigger.",
        body="Licensed for Donatist hermeneutics and self-understanding -- the interpretive side of "
             "this world that its own vendored corpus is thinnest on outside Tyconius.",
    ),
    dict(
        row=26, slug="brown-religion-and-society-and-augustine-biography",
        author="Peter Brown",
        work="Religion and Society in the Age of Saint Augustine (1972) / Augustine of Hippo: A "
             "Biography (1967, revised 2000)",
        edition="Consultation-only, never vendored (Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge, with the bibliographic record externally "
                  "verified / 2026-09-01. Registry row 26.",
        cite="B", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Licensed for GENERAL HISTORICAL FRAMING ONLY and explicitly NOT for vivid, specific "
                   "claims about this world's own internal life on their own -- hence illustrative "
                   "weight. Deliberately NOT flagged for priority second-opinion review: the Registry's "
                   "own reasoning is that this row's license already excludes it from supporting a "
                   "vivid, specific claim, which is the exact condition the review trigger tests for. "
                   "Standard synthesis scholarship, not specialist on this movement.",
        body="Cited at Doc_02 SS5 as a corrective, on that same general-framing basis, to Frend's "
             "social-substrate reading (Registry row 23).",
    ),
    dict(
        row=27, slug="deo-laudes-acclamation",
        author="Anonymous Donatist dedicators and inscribers (epigraphic)",
        work="The Deo laudes acclamation: CIL VIII 17732 (two pillars near Bagai, now preserved at "
             "Khenchela, reading DEO LAVDES twice), with CIL VIII 20482, 17368, and 18669",
        edition="Within CIL VIII, Supplementum, Pars II (Cagnat and Schmidt, 1894), vendored as "
                "cic/texts/cil8-supplementum-numidiae_cagnat-schmidt1894.txt (Registry row 48)",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="anonymous and epigraphic. The Donatist identification is the CIL editors' own, "
                    "stated in their note on 17732: 'Uti [Deo] gratias... catholicorum, ita [Deo] "
                    "laudes signum ac tessera fuit Donatistarum, quorum sedes primariae erant Bagai et "
                    "Thamugadi.'",
        discovery="builder-prior-knowledge (recognized field category) / field knowledge / 2026-09-01; "
                  "RESOLVED to specific catalogued inscriptions by direct text search and read against "
                  "cic/texts/cil8-supplementum-numidiae_cagnat-schmidt1894.txt / 2026-09-01. "
                  "Registry row 27; this resolution cleared the row's own standing priority-review "
                  "flag.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="One inscription must not be counted twice: CIL VIII 20482's editorial note ('Deo "
                   "laudes (de hoc signo Donatistarum cf. supra ad n. 17732)') is a DIRECT "
                   "CROSS-REFERENCE to 17732's own identification, not a second, independent "
                   "attestation of the Donatist association. Four catalogued attestations of the "
                   "acclamation stand; one editorial identification underlies them.",
        body="This world's strongest single evidentiary anchor, and Doc_07 SS5 says why: it is the "
             "material evidence that survived with no literary mediation at all. Everything else in "
             "this world's record survives in inverse proportion to how directly it can be checked "
             "without a hostile hand in between -- this stone does not. The primary witness comes from "
             "Bagai itself, one of the two Donatist seats the editors' own note names.",
    ),
    dict(
        row=28, slug="numidian-basilica-archaeology",
        author="No named author -- a recognized field category, not a specific publication",
        work="Numidian basilica archaeology, general",
        edition="No edition. No specific site report, excavation record, or publication is named "
                "anywhere in Source_Registry.md, Doc_02_Source_Ecology.md, or "
                "Source_Acquisition_Manifest.md.",
        rights=RIGHTS_NO_EDITION_HELD,
        attribution="none -- no publication, excavator, or site report is named, so there is nothing to "
                    "attribute.",
        discovery="builder-prior-knowledge (recognized field category) / field knowledge / 2026-09-01. "
                  "Registry row 28. Flagged in the Registry's own priority second-opinion review list, "
                  "and separately at Doc_02 SS9 item 2.",
        cite="C", verif="unverified", weight="illustrative", formation="Contested",
        divergence="AUTHORED DEPARTURE, stated rather than buried. The Registry grades this row "
                   "Confidence C; citation_specificity above copies that grade mechanically and does "
                   "not renumber it. But verification_state is set to `unverified`, not the "
                   "`named-not-rechecked` that C rows otherwise take here, because this row names no "
                   "author, no work, no publication, and no site report -- which is the Registry's own "
                   "definition of D ('genre/tradition-level attribution with no specific text or author "
                   "named'), not of C ('tied to a real author or work but no specific locus is "
                   "pinpointed'). Certifying anything stronger would be certifying a check that has "
                   "nothing to check against. Doc_02 SS8 independently bands the extent and specific "
                   "attribution of this material as Contested.",
        body="Named for Authority Structures material evidence and carried honestly as a gap rather "
             "than a source. Doc_07 SS7 calls the Material lens genuinely uneven for this world -- "
             "strong on epigraphy (Registry rows 27, 48), honestly undone on basilica archaeology. "
             "Duval's Loca sanctorum Africae (Registry row 43) is the standard instrument that would "
             "move this off a generality, and it is in copyright and consultation-only.",
    ),
    # Registry row 29 (Novatian, De Trinitate and Novatianist material generally) is
    # deliberately NOT emitted: Boundary Status "Excluded", Exclusion Reason "Named
    # Comparandum", Licensed For "N/A -- excluded". See the module docstring.
    dict(
        row=30, slug="lucilla-and-the-second-unnamed-woman",
        author="No independent author -- Lucilla of Carthage and a second, unnamed woman, attested only "
               "inside Optatus's and Augustine's own narratives",
        work="The Lucilla material: Optatus, Against the Donatists I.16 ('The quarrel of Lucilla "
             "against Caecilian'); and the parallel, unnamed woman behind the Maximianist council "
             "against Primian, Augustine, Letter XLIII SS26 (a.d. 397)",
        edition="Within cic/texts/optatus_against-the-donatists.txt and "
                "cic/texts/npnf101_augustine-confessions-letters.xml",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attested, not authored. Neither woman left a text; both reach us entirely inside "
                    "hostile narrative, and the second is never named at all.",
        discovery="direct text search and read against cic/texts/optatus_against-the-donatists.txt "
                  "(13 occurrences) and cic/texts/npnf101_augustine-confessions-letters.xml / "
                  "2026-09-01. Registry row 30.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Widely Accepted",
        divergence="Three limits held open rather than closed. (1) Doc_02 SS8 bands any claim about "
                   "Lucilla's own motivations, private character, or theological commitments beyond "
                   "what Optatus's hostile narrative attributes to her as Inferential/Thin -- the "
                   "reconstruction Doc_02 SS6 permits stays inside what the against-the-grain textual "
                   "trace actually supports: a named woman of means with the standing to make a rival "
                   "consecration happen. (2) The second woman's own NAME is not supplied by the "
                   "vendored corpus and remains open (Doc_02 SS9 item 5). (3) Optatus's translator's "
                   "apparatus cites an Augustine letter numbered 'clxii' for the second woman; that "
                   "content is identified in NPNF's Letter XLIII, but the formal numbering equivalence "
                   "is NOT asserted -- only the content is, and the apparatus is very likely drawing on "
                   "an older, pre-standard letter-numbering scheme.",
        body="The Article 20 Affirmative Duty discharge for this world (Doc_02 SS6), and its secondary "
             "reconstruction prong exercised once. The point is not that a hostile source mentions a "
             "woman; it is that Optatus's own accusation only lands if her agency and standing were "
             "real -- wealth, a household, the capacity to make or unmake a bishop. A hostile source "
             "that NEEDS a woman's real power in order to blame her is a specific against-the-grain "
             "textual trace, not an absence. Augustine draws the Lucilla parallel himself, by name, in "
             "the same paragraph, and leaves the second woman unnamed. A Doc_09 Story Inventory "
             "candidate.",
    ),
    dict(
        row=31, slug="npnf-prolegomena-analysis-anti-donatist-writings",
        author="The Nicene and Post-Nicene Fathers editorial apparatus (Series I, vol. IV), "
               "nineteenth-century scholarly summary",
        work="'Chapter II. -- An Analysis of Augustin's Writings Against the Donatists', Prolegomena to "
             "NPNF Series I vol. IV",
        edition="Within cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="editorial -- a nineteenth-century scholarly synthesis, not a primary Donatist or "
                    "Maximianist voice. Typed S in the Registry accordingly, and not a substitute for "
                    "acquiring the primary texts themselves.",
        discovery="direct text search and read against "
                  "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml / 2026-09-01. "
                  "Registry row 31.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="The Cresconius passage Doc_02 SS1 quotes through this Prolegomena -- that the Synod "
                   "'had granted a season of delay during which all who returned should be held "
                   "innocent... the baptism of these was valid' -- is a DONATIST APOLOGETIC CLAIM "
                   "AUGUSTINE REJECTS, not an agreed fact, and Doc_02 quotes it as such. This row is "
                   "explicitly NOT the primary evidence for the Maximianist reception itself, which "
                   "Doc_02 SS1 draws directly from Augustine's On Baptism (Registry row 3). Doc_02 SS9 "
                   "item 10 directs that the claims currently resting on this summary be re-verified "
                   "against the primary Latin text now that it is vendored.",
        body="Licensed for the dating of Contra Cresconium and Contra epistulam Parmeniani; the earlier "
             "Psalmus contra Partem Donati rhetorical parallel (Registry row 37); and the dating of "
             "Answer to the Letters of Petilian (Book I c. 400, Book III c. 401-402), which Doc_02 SS2 "
             "uses to bracket Petilian's own letters.",
    ),
    dict(
        row=32, slug="gregory-the-great-register-of-letters",
        author="Gregory the Great (Pope Gregory I)",
        work="Register of Letters (Registrum Epistolarum) -- the 590s correspondence concerning the "
             "North African church",
        edition="Partially held via the 1907 Turchi themed selection, which draws its text directly "
                "from the Ewald-Hartmann critical edition with explicit concordance to it, vendored as "
                "cic/texts/gregory-great_epistolae-selectae_turchi1907.txt (Registry row 54). The "
                "complete Ewald-Hartmann Registrum Epistolarum Tomus I (Libri I-VII, Berlin, 1891) "
                "remains unvendored.",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="builder-prior-knowledge, carried from Doc_02 SS3/SS7's own citation gap / field "
                  "knowledge / 2026-09-01; direct text search and read against "
                  "cic/texts/gregory-great_epistolae-selectae_turchi1907.txt / 2026-09-07. Registry "
                  "row 32, upgraded on that reading and REMOVED from the Registry's priority "
                  "second-opinion review list on the same ground.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Four letters were directly read and each carries its own concordance to the "
                   "critical edition: Turchi Ep. LXXXII = Ewald II.46 (to Columbus of Numidia, on a "
                   "bishop corrupted into permitting a Donatist bishop, 592); Ep. LXXXIV = Ewald IV.32 "
                   "(to the praetorian prefect Pantaleon, on the Donatists' growing audacia, 594); "
                   "Ep. LXXXVI = Ewald IV.35 (to Victor and Columbus, urging a council, 594); Ep. "
                   "LXXXVII = Hartmann V.3 (to Dominicus of Carthage, 594). What is NOT covered: this "
                   "selection draws nothing from Book I, so it neither confirms nor contradicts this "
                   "build's own separately-checked I.72 and I.75 (Doc_02 SS9 item 1a(iv)).",
        body="The terminal-record fixing point (Doc_02 SS3, SS7). These letters sit some 153-155 years "
             "AFTER this world's own 439 construction window closes, and Doc_01 SS2 is precise about "
             "what that means: 439 marks the removal of the Roman imperial, Catholic-aligned "
             "adjudicating and coercing power this world's whole refusal pattern is defined against -- "
             "not the end of the two-party contest, which these letters show still requiring a pope's "
             "direct personal attention. The letters sharpen the terminus of attestation; they are not "
             "a new claim about the movement's scale, doctrine, or self-understanding at that date.",
    ),
    dict(
        row=33, slug="augustine-de-doctrina-christiana-iii",
        author="Augustine of Hippo",
        work="De Doctrina Christiana, Book III",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. II, vendored as "
                "cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="builder-prior-knowledge; file existence and content confirmed by direct file check "
                  "against cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml (27 "
                  "occurrences of 'Tichonius' confirmed) / 2026-09-01. Registry row 33. Flagged in the "
                  "Registry's own priority second-opinion review list.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Widely Accepted",
        divergence="What was confirmed is file presence and 27 occurrences of Tyconius's name -- not "
                   "Book III's specific Tyconian-rules content, which was not re-read. Licensed "
                   "NARROWLY for the influence claim (that Tyconius shaped Augustine's own "
                   "hermeneutics) and NOT for De Doctrina Christiana's own content generally; flagged "
                   "for priority second-opinion review before supporting any claim more specific than "
                   "the influence relationship itself.",
        body="The trace of this world's one substantial interpretive theologian in his own opponent's "
             "hermeneutics -- a genuine, and unusual, direction of influence for a world whose evidence "
             "otherwise runs almost entirely the other way.",
    ),
    dict(
        row=34, slug="ebbeler-augustine-epistolography",
        author="Jennifer Ebbeler",
        work="Work on Augustine's epistolography, general -- no specific title is named in the Source "
             "Registry",
        edition="No specific edition named; consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="carried forward from Step0_Movement_Scope_Confirmation.md SS4 item 5's own binding "
                  "source-matrix correction / Step0 build thread / 2026-09-01. Registry row 34. NOT "
                  "builder-prior-knowledge, and excluded from the Registry's priority review list on "
                  "that ground rather than by oversight.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="SUPPORTING CITATION ONLY, should her work be drawn on later in this build -- NOT "
                   "licensed as a primary source for any Donatism-specific claim (Step0 SS4 item 5). "
                   "Not independently checked against a specific text, since Doc_02 currently cites her "
                   "for no claim at all. The row exists to carry a binding correction forward, not to "
                   "support anything yet.",
        body="Doc_01 SS7 item 4 binds Doc_02 and the Source Registry to carry the Ebbeler citation-"
             "scope correction (supporting, not primary) forward; this record is where that binding "
             "lands in the record-native schema.",
    ),
    dict(
        row=35, slug="tilley-donatist-martyr-stories",
        author="Maureen A. Tilley (translator)",
        work="Donatist Martyr Stories: The Church in Conflict in Roman North Africa, Translated Texts "
             "for Historians 24 (Liverpool University Press, 1996)",
        edition="Liverpool University Press, 1996 -- in copyright, recorded not requested "
                "(Source_Acquisition_Manifest.md SS2). Not vendored.",
        rights=RIGHTS_INCOPYRIGHT_RECORDED,
        attribution="attributed",
        discovery="builder-prior-knowledge, cross-checked via WebSearch / 2026-09-01. Registry row 35.",
        cite="B", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="The bibliographic record (title, series, publisher, year) was externally verified; "
                   "the volume itself has NOT been opened, so its exact contents, chapter titles, and "
                   "translation choices are not confirmed. It is the standard English edition of the "
                   "Donatist martyr-narrative corpus and would cover Registry rows 19, 20, and 22 if "
                   "acquired -- rows 19 and 20 currently rest on raw Latin OCR with no free "
                   "public-domain English translation found.",
        body="A named gap, not a smoothed-over one. In copyright is a rights finding, not a judgment "
             "that the work is unusable: it can be bought or consulted through a library, which is a "
             "legitimate research path distinct from placing a file in cic/texts/.",
    ),
    dict(
        row=36, slug="maier-le-dossier-du-donatisme",
        author="Jean-Louis Maier",
        work="Le Dossier du Donatisme, 2 vols., Texte und Untersuchungen 134/135 (Berlin: "
             "Akademie-Verlag, 1987/1989)",
        edition="Akademie-Verlag (now De Gruyter), 1987/1989 -- in copyright, recorded not requested "
                "(Source_Acquisition_Manifest.md SS2). Not vendored.",
        rights=RIGHTS_INCOPYRIGHT_RECORDED,
        attribution="attributed",
        discovery="builder-prior-knowledge, cross-checked via WebSearch / 2026-09-01. Registry row 36.",
        cite="B", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Bibliographic record externally verified (title, series, publisher, volume dates); "
                   "contents not independently checked against the volumes. Volume II's 361-750 span "
                   "bears directly on the terminal-record question Doc_02 SS3 and SS7 work through.",
        body="The standard collected documentary dossier of Donatist sources -- the single instrument "
             "that would most efficiently close this world's scattered-documentation problem, and the "
             "one it cannot vendor.",
    ),
    dict(
        row=37, slug="augustine-psalmus-contra-partem-donati",
        author="Augustine of Hippo",
        work="Psalmus contra Partem Donati -- an abecedarian psalm, dated only to Augustine's "
             "presbyterate on the NPNF Prolegomena's own chronological arrangement",
        edition="Michael Petschenig (ed.), CSEL 51/53, vendored as "
                "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. The poem's own Retractationes entry, reproduced separately in the same "
                    "file, describes it as running the alphabet through V with an epilogue in place of "
                    "the final three letters -- matching the vendored text.",
        discovery="direct text search and read against "
                  "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt / "
                  "2026-09-02, during a Registry-reconciliation pass. Registry row 37.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Confidence A reflects the poem's own CONFIRMED PRESENCE AND IDENTITY -- the heading "
                   "'PSALMUS CONTRA PARTEM DONATI', the 'A' stanza opening 'Abundantia peccatorum...', "
                   "the full critical apparatus, and the closing 'EXPLICIT ABECEDARIUM AVGUSTINI... "
                   "Amen' at verse 288 -- NOT a re-verification of the claims drawn from it. "
                   "Specifically NOT yet checked: whether the poem contains, verbatim, the Maximianist-"
                   "restoration rhetorical question Doc_02 SS1 quotes via the NPNF Prolegomena "
                   "(Registry row 31). A targeted search found extensive rebaptism-rhetoric verses "
                   "(e.g. 'ex quibus si erat Macarius, nos quid uis rebaptizare?', naming Macarius "
                   "rather than the Maximianists) but did not locate that exact question; Doc_02's "
                   "citation of it continues to rest on row 31.",
        body="Found UNREGISTERED inside a file already vendored for three other rows, because that "
             "file's contents had been checked against two specific Explicit/Incipit markers rather "
             "than searched end to end -- a real acquisition finding, recorded as such. Licensed for "
             "the earliest attested use of the Maximianist-reception argument in rhetorical form, "
             "pre-dating Contra Cresconium (Doc_02 SS1), and for its own rebaptism polemic generally.",
    ),
    dict(
        row=38, slug="ziwsa-optatus-libri-vii-csel26",
        author="Karl Ziwsa (editor); Optatus of Milevis (author)",
        work="S. Optati Milevitani libri VII, Corpus Scriptorum Ecclesiasticorum Latinorum (CSEL) 26",
        edition="Prague/Vienna/Leipzig: F. Tempsky / G. Freytag, 1893; vendored as "
                "cic/texts/optatus_libri-vii-critical_ziwsa1893.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. Title page confirmed: EX RECOGNITIONE CAROLI ZIWSA, MDCCCLXXXXIII.",
        discovery="builder-prior-knowledge, cross-checked via WebSearch / 2026-09-01; file identity "
                  "confirmed by direct file check against "
                  "cic/texts/optatus_libri-vii-critical_ziwsa1893.txt. Registry row 38; "
                  "Source_Acquisition_Manifest.md SS1 G2 discharged.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Widely Accepted",
        divergence="Identity confirmed as the genuine CSEL 26 edition -- title page and the Gesta "
                   "Purgationis Felicis appendix document both present. But the thing this edition was "
                   "acquired to do has NOT been done: the apparatus criticus has not been read, so the "
                   "second-edition and book-count question Registry row 1's own Verification Note "
                   "leaves open is still open (Doc_02 SS9 item 13). Raw, uncorrected OCR.",
        body="The critical Latin edition underlying the vendored 1917 translation (Registry row 1), and "
             "the specific instrument that would settle the second-edition question from the primary "
             "apparatus rather than from a 1917 translator's own footnotes.",
    ),
    dict(
        row=39, slug="petschenig-scripta-contra-donatistas-csel51-53",
        author="Michael Petschenig (editor); Augustine of Hippo (author)",
        work="Sancti Aureli Augustini Scripta contra Donatistas, CSEL 51 and 53",
        edition="Vienna: Tempsky / Leipzig: Freytag, 1908 and 1910; vendored as "
                "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="builder-prior-knowledge, cross-checked via WebSearch / 2026-09-01; file identity and "
                  "contents directly verified by file check against "
                  "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt. "
                  "Registry row 39; Source_Acquisition_Manifest.md SS1 G5 discharged.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="A real bibliographic finding, carried rather than summarised away: the scan's only "
                   "surviving title page identifies itself as 'Pars I' (CSEL 51), but the text runs "
                   "past that title page's own stated three-item contents into further works confirmed "
                   "by their own Explicit/Incipit markers, with no second title page captured. The "
                   "volume's consolidated errata resolves it -- it corrects both 'VOL. LI' and "
                   "'VOL. LIII' by name, confirming a library binding of Pars I AND Pars III together, "
                   "Pars III's title page evidently lost to the scan. Pars II (CSEL 52, Contra litteras "
                   "Petiliani) is confirmed ABSENT, checked directly. This corrects this build's own "
                   "earlier guidance that Contra Cresconium and Contra epistulam Parmeniani sat in "
                   "separately-acquired volumes.",
        body="The critical Latin edition standing behind Registry rows 17, 18, 37, and 56 -- four "
             "distinct works in one vendored file, two of which (the Psalmus, row 37; Contra "
             "Gaudentium, row 56) were found in it only after it had already been vendored for "
             "something else.",
    ),
    dict(
        row=40, slug="monceaux-histoire-litteraire-tome5",
        author="Paul Monceaux",
        work="Histoire litteraire de l'Afrique chretienne depuis les origines jusqu'a l'invasion arabe, "
             "Tome V: Saint Optat et les premiers ecrivains donatistes",
        edition="Paris: Ernest Leroux, 1920; vendored as "
                "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome5_1920.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. Type CORRECTED in the Registry from P to S: this is modern (1920) "
                    "secondary scholarship interpreting the primary material, not itself a primary text "
                    "from within this world's own documented span.",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01; file identity and contents "
                  "directly verified by file read against "
                  "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome5_1920.txt. Registry "
                  "row 40; Source_Acquisition_Manifest.md SS1 G6 discharged for this tome.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Widely Accepted",
        divergence="Directly read for the Tyconius chapter (eight or more specific characterisations "
                   "checked verbatim, all accurate) and for the Passio Donati material. But EXPLICITLY "
                   "NOT LICENSED for Monceaux's own footnoted primary-source citations -- Augustine's "
                   "Epistle 93.10.43-45 and Contra epistulam Parmeniani I.1, offered as his "
                   "biographical sources for Tyconius -- which have not themselves been checked against "
                   "the vendored corpus (Doc_02 SS9 item 11), though both works now could be. Tomes IV "
                   "and VI (Registry rows 52, 53), more directly on-topic than this one, are now also "
                   "vendored and have not been cross-checked against this row's findings.",
        body="A second, independent public-domain route to the Macarian-repression Passiones (Registry "
             "rows 19, 20), and the fuller of the two vendored authorities on the Passio Donati "
             "(row 50). Monceaux names the three martyr texts as a deliberate trio: 'Un sermon: la "
             "Passio Donati. Un recit: la Passio Marculi. Une lettre: la Passio Maximiani et Isaac' -- "
             "confirmed verbatim -- and cites Migne columns that corroborate this Registry's own row "
             "19/20 column citation. French-language; no public-domain English translation exists.",
    ),
    dict(
        row=41, slug="burkitt-book-of-rules-of-tyconius",
        author="F.C. Burkitt (editor); Tyconius (author)",
        work="The Book of Rules of Tyconius, Newly Edited from the MSS., Texts and Studies III/I",
        edition="Cambridge University Press, 1894; vendored as "
                "cic/texts/tyconius_liber-regularum_burkitt1894.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. Preface, table of contents, and introduction all present and correctly "
                    "naming F.C. Burkitt as editor and Tyconius as author.",
        discovery="builder-prior-knowledge; file identity and rights basis confirmed by direct file "
                  "check against cic/texts/tyconius_liber-regularum_burkitt1894.txt / 2026-09-01. "
                  "Registry row 41; Source_Acquisition_Manifest.md SS1 G1 discharged.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Documented",
        divergence="Public domain confirmed on two independent grounds -- the hosting archive's own "
                   "copyright-evidence record for this item, and the 1894 publication date alone. But "
                   "the file is raw, uncorrected OCR with visible Greek-letter substitution into Latin "
                   "words and garbled proper nouns: ANY specific quotation drawn from it needs a visual "
                   "cross-check against its own surrounding context before being relied on for a "
                   "verbatim claim. Latin critical text with an English scholarly introduction; there "
                   "is no English translation of the Rules themselves in this edition, and the only "
                   "modern one (Babcock, SBL 1989) is in copyright.",
        body="The public-domain critical edition attaching to Registry row 15's work -- the edition "
             "that makes this world's one substantial independently-surviving interpretive text "
             "actually readable.",
    ),
    dict(
        row=42, slug="mandouze-prosopographie-afrique-chretienne",
        author="Andre Mandouze",
        work="Prosopographie chretienne du Bas-Empire, I: Prosopographie de l'Afrique chretienne "
             "(303-533) (Paris: CNRS, 1982)",
        edition="CNRS, 1982 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01. Registry row 42. Flagged in "
                  "the Registry's own priority second-opinion review list.",
        cite="B", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Bibliographic record from field knowledge, not independently checked against the "
                   "volume -- flagged for priority second-opinion review BEFORE any specific "
                   "identification or dating claim drawn from it is treated as settled. That flag "
                   "matters here more than for most rows: this is the instrument that would fix and "
                   "cross-reference Lucilla, Felicianus of Musti, Praetextatus of Assuris, Petilian of "
                   "Constantina, and Emeritus of Caesarea to their attesting texts, and would carry "
                   "Registry row 30's second, unnamed woman as far as the evidence allows.",
        body="The field's standard prosopographical instrument for this world's named -- and unnamed -- "
             "individuals, and one this build cannot vendor.",
    ),
    dict(
        row=43, slug="duval-loca-sanctorum-africae",
        author="Yvette Duval",
        work="Loca sanctorum Africae: le culte des martyrs en Afrique du IVe au VIIe siecle, 2 vols., "
             "Collection de l'Ecole francaise de Rome 58 (Rome, 1982)",
        edition="Ecole francaise de Rome, 1982 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01. Registry row 43. Flagged in "
                  "the Registry's own priority second-opinion review list.",
        cite="B", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Bibliographic record from field knowledge, not independently checked against the "
                   "volumes. Typed S/M in the Registry -- both secondary scholarship and a material-"
                   "evidence instrument. It is the evidentiary basis that Doc_02 SS5's Deo laudes and "
                   "basilica-archaeology bullets and SS4's martyr-cult ecology name as a category "
                   "WITHOUT YET EXPLOITING: named, not used.",
        body="The standard epigraphic and topographic corpus of the African martyr cult -- the "
             "instrument that would move Registry row 28 (Numidian basilica archaeology) off a "
             "generality, and the reason that row stands as an honest gap rather than a source.",
    ),
    dict(
        row=44, slug="labrousse-optat-de-mileve-sc412-413",
        author="Mireille Labrousse (editor and translator); Optatus of Milevis (author)",
        work="Optat de Mileve: Traite contre les donatistes, Sources Chretiennes 412-413",
        edition="Paris: Cerf, 1995-1996 -- in copyright, recorded not requested "
                "(Source_Acquisition_Manifest.md SS2). Not vendored.",
        rights=RIGHTS_INCOPYRIGHT_RECORDED,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01. Registry row 44.",
        cite="B", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Bibliographic record from field knowledge, not independently checked against the "
                   "volumes. This is the CURRENT critical edition and French translation of Registry "
                   "row 1's work, standing alongside Ziwsa (row 38, the public-domain route) as the "
                   "current-scholarship route to the second-edition question row 1's own Verification "
                   "Note leaves open.",
        body="Named so the gap is visible: the question row 1 leaves open has two possible instruments, "
             "one vendored and unread, one unvendorable.",
    ),
    dict(
        row=45, slug="edwards-optatus-against-the-donatists-tth27",
        author="Mark Edwards (translator); Optatus of Milevis (author)",
        work="Optatus: Against the Donatists, Translated Texts for Historians 27",
        edition="Liverpool University Press, 1997 -- in copyright, recorded not requested "
                "(Source_Acquisition_Manifest.md SS2). Not vendored.",
        rights=RIGHTS_INCOPYRIGHT_RECORDED,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01. Registry row 45.",
        cite="B", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Bibliographic record from field knowledge, not independently checked against the "
                   "volume. The modern standard English translation of Registry row 1's work and an "
                   "alternative to the vendored 1917 Vassall-Phillips translation -- which is the "
                   "translation this world's whole Optatus evidence currently runs through, and whose "
                   "own translator attribution rests on external bibliographic grounds rather than on "
                   "the file's own text.",
        body="Named as a gap with a specific consequence: this world reads its earliest substantial "
             "narrative source through a century-old translation, and the modern one is out of reach.",
    ),
    dict(
        row=46, slug="tengstrom-donatisten-und-katholiken",
        author="Emin Tengstrom",
        work="Donatisten und Katholiken: soziale, wirtschaftliche und politische Aspekte einer "
             "nordafrikanischen Kirchenspaltung (Goteborg: Elanders, 1964)",
        edition="Elanders, 1964 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01. Registry row 46. Flagged in "
                  "the Registry's own priority second-opinion review list.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Contested",
        divergence="The Registry states plainly that this row's bibliographic record sits at LOWER "
                   "confidence than the other rows in its table -- the volume's exact argument is "
                   "recalled less precisely -- and flags it for priority second-opinion review BEFORE "
                   "it supports any claim at all. `illustrative` weight follows from that, not from any "
                   "judgment about the book. formation_confidence is Contested because it is one side "
                   "of the same contested social-reading debate as Frend (Registry row 23).",
        body="A social, economic, and political reading of the schism, cited in the field literature as "
             "a counterpoint to Frend's own thesis. Recorded at the confidence the Registry itself "
             "claims for it, which is deliberately low.",
    ),
    dict(
        row=47, slug="augustine-letter-51-to-crispinus",
        author="Augustine of Hippo",
        work="Letter LI, 'To Crispinus' (a.d. 399 or 400)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. I, vendored as "
                "cic/texts/npnf101_augustine-confessions-letters.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="direct text search and read against "
                  "cic/texts/npnf101_augustine-confessions-letters.xml / 2026-09-01. Registry row 47.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Directly read and quoted: 'you restored some of them without re-ordination, and "
                   "accepted their baptism as valid'; and 'why have you harshly persecuted the "
                   "Maximianists by the help of judges... [and driven] them, by the din of controversy, "
                   "the authority of edicts, and the violence of soldiery, from those buildings for "
                   "worship which they possessed.' Two limits held open. (1) This is a HOSTILE WITNESS "
                   "reporting his opponents' practice inside his own polemic -- direct testimony, not "
                   "an independent Donatist record. (2) Letter LXX, on the same subject, is present in "
                   "the vendored volume only as an editorial headnote saying it is left untranslated "
                   "because it covers the same ground -- a materially different status from unvendored, "
                   "and the route by which this letter was found.",
        body="Load-bearing for the finding Doc_01 SS4's whole Strand Determination turns on: the "
             "mainstream Donatist party received returning Maximianist clergy WITHOUT reordination or "
             "rebaptism, which is proof the mainstream party itself recognised Maximianist orders and "
             "sacraments as valid -- a shared formation pattern, not the distinct one Article 21 "
             "requires for strand status. Also direct testimony to the Donatist party's own use of the "
             "civil courts and armed force against the Maximianists, one of the three named "
             "qualifications on this world's otherwise dominant refusal-of-imperial-legitimacy pattern "
             "(Doc_01 SS5; Doc_07 SS4, SS6).",
    ),
    dict(
        row=48, slug="cil-viii-supplementum-numidiae",
        author="Rene Cagnat and Johannes Schmidt (editors)",
        work="Corpus Inscriptionum Latinarum, vol. VIII, Supplementum, Pars II: Inscriptionum "
             "Provinciae Numidiae Latinarum Supplementum",
        edition="Berlin: Reimer, 1894; vendored as "
                "cic/texts/cil8-supplementum-numidiae_cagnat-schmidt1894.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01; file identity and contents "
                  "directly verified by file check against "
                  "cic/texts/cil8-supplementum-numidiae_cagnat-schmidt1894.txt. Registry row 48; "
                  "Source_Acquisition_Manifest.md SS1 G7 discharged.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="This is the NUMIDIA SUPPLEMENT FASCICLE specifically, not the 1881 main volume -- "
                   "Numidia being this world's own Donatist heartland province, which is why this "
                   "fascicle and not another was acquired. Public domain on the 1894 date; the scan's "
                   "own front matter documents a 1991 preservation facsimile of the original, which is "
                   "a reproduction, not a new copyrighted edition.",
        body="The instrument that moved Registry row 27's Deo laudes claim off a recognized-category "
             "generality and onto specific catalogued inscriptions, and in doing so cleared that row's "
             "own standing priority-review flag. An acquisition that changed an evidentiary status "
             "rather than merely adding a volume.",
    ),
    dict(
        row=49, slug="boyd-ecclesiastical-edicts-theodosian-code",
        author="William K. Boyd",
        work="The Ecclesiastical Edicts of the Theodosian Code (Studies in History, Economics and "
             "Public Law, Columbia University, Vol. XXIV)",
        edition="New York: Columbia University Press / Macmillan, 1905; vendored as "
                "cic/texts/boyd_ecclesiastical-edicts-theodosian-code_1905.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. Confirmed a genuine 1905 Columbia University monograph, bound together "
                    "in the scanned volume with two unrelated studies, neither of which this build "
                    "cites.",
        discovery="Mark, DOCX upload, after this build thread named the archive search results and "
                  "recommended this specific item; contents confirmed by direct file check against "
                  "cic/texts/boyd_ecclesiastical-edicts-theodosian-code_1905.txt / 2026-09-01. "
                  "Registry row 49.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Two confirmed ABSENCES bound what this row licenses, and both were checked "
                   "directly. (1) Law 16.5.52's own text is NOT quoted anywhere in this file -- this "
                   "row does not license it; Mommsen and Meyer (Registry row 51) does. (2) The term "
                   "agonistici does not appear here either; Boyd uses 'Circumcellions' throughout. "
                   "Separately, Doc_02 SS3 flags Boyd's own one-sentence characterisation of the group "
                   "as an uncritical restatement of Augustine's and Optatus's hostile framing -- NOT "
                   "corroborating evidence of the group's character. Acquired as a stopgap while the "
                   "critical edition remained unlocated; now supplemented rather than needed as a "
                   "substitute.",
        body="Corroborating narrative history of the Donatist-targeted legislation in Codex "
             "Theodosianus Book 16 Title 5, including the 405 Edict of Unity (xvi.5.38-39) and the "
             "surrounding sequence xvi.5.3-58, with individual laws quoted verbatim in Latin naming the "
             "Donatists directly.",
    ),
    dict(
        row=50, slug="passio-donati-sermon",
        author="Anonymous Donatist preacher; Monceaux proposes Carthage's own Donatist bishop, possibly "
               "Donatus the Great, as an eyewitness -- proposed, not adopted",
        work="Anonymous Donatist sermon, manuscript title De passione sanctorum Donati et Advocati, "
             "known under its standard scholarly name as the Passio Donati",
        edition="Edited by Jean Mabillon in his Monumenta Vetera ad Donatistarum historiam pertinentia, "
                "printed in Migne, Patrologia Latina vol. 8; vendored (relevant excerpt only) as "
                "cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt. Treated at chapter length by "
                "Monceaux (Registry row 40).",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="anonymous, and the title itself is contested. Mabillon judges 'Donati' in the "
                    "manuscript title 'alien to the sermon itself' without proposing a replacement; "
                    "Monceaux proposes the title is a corruption of Sermo de Passione Donati episcopi "
                    "Advocatensis (or Avioccalensis), naming the bishop of Advocata who died, rather "
                    "than two martyrs literally called Donatus and Advocatus. Neither reading is "
                    "adopted here.",
        discovery="direct text search and read against "
                  "cic/texts/monumenta-vetera-donatistarum_migne-pl8.txt, found INCIDENTALLY while "
                  "vendoring Registry rows 19-20; Monceaux's competing account independently verified "
                  "against cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome5_1920.txt / "
                  "2026-09-02. Registry row 50.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Contested",
        divergence="TWO VENDORED AUTHORITIES GIVE DIFFERENT ACCOUNTS AND NEITHER IS ADOPTED. Mabillon's "
                   "own admonitio dates the persecution to circa 340, external to the sermon's own "
                   "text, cross-referencing Optatus's chronology and Sardica's 347 date for Caecilian's "
                   "death; he glosses the sermon's 'memoratus episcopus' as Honoratus of Sicilibba, one "
                   "of the wounded named in the narrative. Monceaux, reading the sermon's own text "
                   "rather than only Mabillon's apparatus, dates the persecution precisely to 12 March "
                   "317 and composition to circa 320, from the text's own reference to a 'persecution "
                   "of Caecilianus' tied to Constantine's 316 edict of union; proposes an eyewitness "
                   "Donatist bishop of Carthage as preacher; and reports the persecution as "
                   "multi-basilica fighting with the bishop of Sicilibba gravely wounded and the bishop "
                   "of Advocata/Avioccala killed with numerous faithful -- not a single unnamed death. "
                   "Licensed for existence, genre, and the dating/authorship/title QUESTION as reported "
                   "from both; NOT for a settled dating or authorship, and not for its own full Latin "
                   "content beyond the passages checked.",
        body="A genuine surviving Donatist-AUTHORED primary voice -- the scarcest category this world "
             "has, and the reason Doc_02 SS6 counts the Migne acquisition as a real rather than token "
             "correction to this world's Author Gravity concentration. Found incidentally, not "
             "requested. Doc_02 SS9 item 12 flags its own full Latin content, and Mabillon's "
             "Leontius/Ursacius cross-references, as unread work that could now be done against "
             "already-vendored texts.",
    ),
    dict(
        row=51, slug="mommsen-meyer-theodosiani-libri-xvi",
        author="Theodor Mommsen and Paul M. Meyer (editors)",
        work="Theodosiani Libri XVI cum Constitutionibus Sirmondianis et Leges Novellae ad Theodosianum "
             "Pertinentes, Voluminis I Pars Posterior: Textus cum Apparatu",
        edition="Berlin: Weidmann, 1905; vendored as "
                "cic/texts/theodosianus-16_mommsen-meyer1905.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. Title page confirmed: 'VOLVMINIS I PARS POSTERIOR' and 'EDIDERVNT TH. "
                    "MOMMSEN et PAVLVS M. MEYER'.",
        discovery="A sibling research session's finding, relayed through this build's own launch "
                  "instructions and then INDEPENDENTLY RE-VERIFIED by direct fetch and read of the "
                  "primary text itself rather than accepted on the relay's own account; direct text "
                  "search and read against cic/texts/theodosianus-16_mommsen-meyer1905.txt / "
                  "2026-09-07. Registry row 51; Source_Acquisition_Manifest.md SS1 G3 discharged.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="All 16 Books present; Book XVI located; law XVI.5.52, headed '412 Ian. 30', read in "
                   "full and confirmed to contain 'circumcelliones argenti pondo decem' verbatim. The "
                   "term agonistici does NOT appear anywhere in this file (checked directly, zero "
                   "matches). Beyond 16.5.52 and Book XVI's heading structure, the remainder -- Books "
                   "I-XV and the rest of Book XVI's own laws -- has not been independently read or "
                   "collated against any claim. Five prior acquisition attempts returned the wrong "
                   "volume (the Prolegomena, Vol. I Pars Prior); a sixth download from a site calling "
                   "itself sourcelibrary.org was REJECTED OUTRIGHT on source-integrity grounds, an "
                   "unlicensed translation carrying a systematic invisible Unicode payload, and that "
                   "site is barred from future acquisition.",
        body="The primary critical-edition text behind Registry row 16, and the row that supersedes "
             "Boyd (row 49) as the primary-source basis for the Circumcellion attestation. Closing this "
             "took six attempts across three sessions; the root blocker was a network egress block, not "
             "a bad search, and the record says so.",
    ),
    dict(
        row=52, slug="monceaux-histoire-litteraire-tome4",
        author="Paul Monceaux",
        work="Histoire litteraire de l'Afrique chretienne depuis les origines jusqu'a l'invasion arabe, "
             "Tome IV: Le Donatisme",
        edition="Paris: Ernest Leroux, 1912; vendored as "
                "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome4_1912.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. Dated 1912 from the TITLE PAGE, not from catalog metadata: the hosting "
                    "archive's own catalog wrongly shows 1901, the series' start year misapplied "
                    "uniformly to every tome.",
        discovery="direct file check (title page and chapter-heading survey only) against "
                  "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome4_1912.txt / "
                  "2026-09-07. Registry row 52; Source_Acquisition_Manifest.md SS1 G6's remainder.",
        cite="A", verif="verified-direct", weight="illustrative", formation="Widely Accepted",
        divergence="Confidence A covers EXISTENCE, IDENTITY, PUBLICATION DATE, AND CHAPTER-LEVEL "
                   "TOPICAL SCOPE ONLY. NOT read beyond the title page and four confirmed chapter "
                   "headings -- I. 'L'Eglise Donatiste', II. 'Les Documents Donatistes ou Relatifs [au "
                   "Donatisme]', III. 'Les Actes des Conciles', IV. 'L'Epigraphie Donatiste'. No "
                   "specific claim, quotation, or citation from this tome's body text has been checked. "
                   "evidentiary_weight is illustrative because the Registry itself says the row is not "
                   "yet cited in support of any specific claim.",
        body="Monceaux's own first dedicated Donatism volume, and more directly on-topic than the Tome "
             "V already integrated (Registry row 40) -- a dedicated sources-and-councils-and-epigraphy "
             "treatment sitting unread. Named as an open item for a future Doc_02/Doc_04 revision pass "
             "(Doc_02 SS9 item 1a(iii)), not integrated.",
    ),
    dict(
        row=53, slug="monceaux-histoire-litteraire-tome6",
        author="Paul Monceaux",
        work="Histoire litteraire de l'Afrique chretienne depuis les origines jusqu'a l'invasion arabe, "
             "Tome VI: La Litterature Donatiste au temps de saint Augustin",
        edition="Paris: Editions Ernest Leroux, 1922; vendored as "
                "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome6_1922.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. Dated 1922 from the title page, with the same catalog-date caveat as "
                    "Tome IV (Registry row 52).",
        discovery="direct file check (title page and chapter-heading survey only) against "
                  "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome6_1922.txt / "
                  "2026-09-07. Registry row 53; Source_Acquisition_Manifest.md SS1 G6's remainder.",
        cite="A", verif="verified-direct", weight="illustrative", formation="Widely Accepted",
        divergence="Confidence A covers existence, identity, publication date, and chapter-level scope "
                   "only. Nine chapters confirmed by their own headings, each a dedicated study of a "
                   "named Donatist figure or genre already present elsewhere in this Registry -- I. "
                   "'Petilianus de Constantine' (Registry row 12's own voice), III. 'Primianus de "
                   "Carthage', IV. 'Emeritus de Caesarea' (row 14's bishop), V. 'Gaudentius de "
                   "Thamugadi' (row 56), VI. 'Fulgentius le Donatiste', VII. 'Anonymes Donatistes', "
                   "VIII. 'Litterature Epistolaire', IX. 'Les Orateurs Donatistes' (chapter II's "
                   "heading was not captured by the survey). SEVEN of the nine chapters are entirely "
                   "unread, INCLUDING chapter I on Petilian himself.",
        body="The most directly on-topic unread volume this world holds: a chapter-by-chapter treatment "
             "of exactly the Donatist figures whose own voices this world's Registry is thinnest on. "
             "Named as an open item (Doc_02 SS9 item 1a(iii)), not integrated.",
    ),
    dict(
        row=54, slug="turchi-gregorii-magni-epistolae-selectae",
        author="Nicola Turchi (editor); Gregory the Great (author)",
        work="Bibliotheca Sanctorum Patrum et Scriptorum Ecclesiasticorum, Series VII (Scriptores Medii "
             "Aevi), Voluminis I Pars I: Sancti Gregorii Magni Epistolae Selectae",
        edition="Rome: Apud Directionem Bibliothecae Ss. Patrum, 1907; vendored as "
                "cic/texts/gregory-great_epistolae-selectae_turchi1907.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. The front matter states directly that the text and annotations are "
                    "taken FROM the Ewald-Hartmann critical edition, and every included letter carries "
                    "the editors' own explicit concordance to it.",
        discovery="found via a Google Books search after two prior sessions' exhaustive archive "
                  "searches for the Ewald-Hartmann edition itself came up empty; direct text search and "
                  "read against cic/texts/gregory-great_epistolae-selectae_turchi1907.txt / 2026-09-07. "
                  "Registry row 54.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="THIS IS A THEMED SELECTION, NOT THE COMPLETE REGISTER -- its own title page states "
                   "'Pars I' and its back matter confirms a Pars II exists, not located. The four "
                   "Donatist-subject letters were found by a full-file search for 'Donatist' and its "
                   "Latin case forms, not a page-by-page read, and the remainder of the 548-page "
                   "selection was not re-collated for Donatist content beyond that search. It draws "
                   "nothing from Book I, so it neither confirms nor contradicts Registry row 32's "
                   "separately-verified I.72 and I.75. The complete Ewald-Hartmann Tomus I, if "
                   "vendored, would supersede this row as the primary route.",
        body="The vendored route to Registry row 32's terminal-record claim. Four letters, each with "
             "its own concordance: Ep. LXXXII = Ewald II.46 (592); Ep. LXXXIV = Ewald IV.32 (594); "
             "Ep. LXXXVI = Ewald IV.35 (594); Ep. LXXXVII = Hartmann V.3 (594). A footnote in the last "
             "quotes F. Homes Dudden's Gregory the Great (1905) on a 594 Council at Carthage against "
             "the Donatists, possibly at Gregory's own instigation.",
    ),
    dict(
        row=55, slug="migne-pl11-collatio-carthaginiensis",
        author="J.-P. Migne (editor); various late-antique authors and the recorders of the 411 "
               "Conference acts",
        work="Patrologiae Cursus Completus, Series Latina, Tomus XI -- the volume bundling Zeno of "
             "Verona's works with a substantial Optatus/Donatism cluster, including the Gesta "
             "Collationis Carthaginiensis itself (col. 1223)",
        edition="Paris, compiled 1840s-1850s; vendored as "
                "cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="documentary for the Gesta itself -- numbered conference acts naming their own "
                    "speakers. Editorial for the volume's framing: the Optatus material reprinted here "
                    "is Francois Baudouin's sixteenth-century edition and the Collatio material Jean "
                    "Dalle's, per the vendored file's own provenance header.",
        discovery="found via direct archive search after Registry row 14's 2026-09-01 'confirmed "
                  "unavailable' determination turned out to have been made without working network "
                  "access; direct text search and read against "
                  "cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt / 2026-09-07. "
                  "Registry row 55.",
        cite="B", verif="verified-direct", weight="load-bearing", formation="Widely Accepted",
        divergence="AUTHORED DEPARTURE from the letter-to-state mapping, stated rather than buried. The "
                   "Registry holds this row at Confidence B because MOST OF THIS ~5MB, 144,000-line "
                   "VOLUME HAS NOT BEEN READ -- a citation-specificity fact. But the specific content "
                   "this row is licensed for WAS directly read and quoted: numbered acts present and "
                   "legible ('268. Emeritus episcopus dixit... 269. Alypius episcopus Ecclesiae "
                   "catholicae dixit... 270. Adeodatus episcopus dixit'), Marcellinus named throughout "
                   "as presiding tribunus et notarius, and at least 28 occurrences of 'Emeritus' "
                   "confirmed by search. verification_state therefore reads verified-direct while "
                   "citation_specificity stays B, keeping the two axes independent. THREE UNRESOLVED "
                   "ITEMS in the same volume, per its own printed Elenchus: a Historia Donatistarum "
                   "(col. 771); a SECOND, DIFFERENT critical edition of Optatus's Seven Books (col. "
                   "883, distinct from both Registry row 1's translation and row 38's Ziwsa); and a "
                   "Monumenta vetera ad Historiam Donatistarum pertinentia section (col. 1170) carrying "
                   "the IDENTICAL Latin title to the already-vendored PL vol. 8 file (rows 19, 20, 50). "
                   "Whether these are the same material under different volume numbers or two "
                   "independently overlapping compilations is genuinely open. The Gesta's own column "
                   "boundary against Balduin's following Historia Collationis was not established -- "
                   "this scan's OCR column markers are not reliably sequential.",
        body="The public-domain route to Registry row 14's Gesta, and the correction of a wrong "
             "'confirmed unavailable' finding. This corpus's own worst OCR quality on record for a text "
             "of this significance (Doc_02 SS6), which bounds how far the correction can currently be "
             "exploited.",
    ),
    dict(
        row=56, slug="augustine-contra-gaudentium",
        author="Augustine of Hippo",
        work="Contra Gaudentium Donatistarum Episcopum, Libri II (c. 420) -- Augustine's own last "
             "anti-Donatist work",
        edition="Michael Petschenig (ed.), CSEL 51/53 (Registry row 39), vendored as "
                "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt, "
                "running roughly 12,000 lines from that file's own internal heading 'LIBER PRIMVS' "
                "under 'XII. Contra Gaudentium'",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. Augustine states his own citation convention up front -- 'quando "
                    "ponimus uerba Gaudentii, non dicamus \"Gaudentius dixit\", sed \"uerba "
                    "epistulae\"' -- confirming the work alternates Gaudentius's own quoted letter-text "
                    "with Augustine's responses throughout.",
        discovery="found by direct search of an already-vendored file, NOT builder-prior-knowledge -- "
                  "which is why the Registry's own priority second-opinion review trigger does not "
                  "reach this row; direct text search and read against "
                  "cic/texts/augustini_scripta-contra-donatistas-pars-i-iii_petschenig1908-1910.txt / "
                  "2026-09-08, sibling research session. Registry row 56.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Widely Accepted",
        divergence="Confidence A reflects the work's CONFIRMED PRESENCE, EXTENT, AND QUOTATION METHOD "
                   "ONLY. Neither book's specific content has been read beyond the opening, and NO "
                   "claim from Gaudentius's own words has yet been drawn into this world's build from "
                   "this row -- which is why formation_confidence is held at Widely Accepted rather "
                   "than Documented despite the direct verification.",
        body="A further body of preserved, genuine Donatist voice alongside Petilian (Registry rows 4, "
             "12): Gaudentius of Thamugada's own two rescript letters to the tribune Dulcitius, quoted "
             "verbatim throughout by Augustine's own stated method -- the same preserved-primary-voice "
             "structure already relied on for Petilian. Found complete and previously unnoticed inside "
             "a file vendored for other rows entirely, the second such find in this Registry (Registry "
             "row 37 was the first). Corroborates Monceaux's Tome VI chapter V, 'Gaudentius de "
             "Thamugadi' (row 53), which is itself unread.",
    ),
]

# ------------------------------------------------------------- world_core ---
TIME_WINDOW = {"start": 311, "end": 439}

HORIZON = (
    "The rigorist alternative communion of Roman North Africa, c. 311/312 - 439: the church that "
    "split from the North African Catholic party over whether sacraments and ordinations given by "
    "clergy suspected of having surrendered the scriptures under the Diocletianic persecution are "
    "valid at all, and that then lived as a complete parallel church - its own bishops, its own "
    "basilicas, its own line of ordination - contesting the rival communion town for town across "
    "Africa Proconsularis, Numidia, Byzacena, and Mauretania (Doc_01 SS1-SS2). Carthage holds both "
    "rival bishoprics from the outset and is the site of the decisive 411 Conference; Numidia is this "
    "communion's own heartland, numerically dominant, the origin region of several of its most "
    "prominent bishops and of the Circumcellion phenomenon; Cirta, as Constantina, is Petilian's see. "
    "This is not a doctrinal heresy: the confession here is standard North African Latin Trinitarian "
    "and Christological orthodoxy, and what is contested is legitimacy - who the true church is, and "
    "whose hand can validly give what the church gives (Doc_01 SS1). Two dates open the window rather "
    "than one, because the sources support both and not a choice between them: the disputed election "
    "and consecration of Caecilian as bishop of Carthage falls in 311 or 312 depending on how the "
    "transition from persecution to episcopal election is dated, and the traditio accusation against "
    "his consecrator Felix of Aptungi produced the rival consecration of Majorinus, succeeded from "
    "c. 313 by Donatus, from whom the movement takes its name. The window closes at the Vandal "
    "capture of Carthage in 439 - and that close means one specific thing, not a general end. What 439 "
    "removes is the Roman imperial state as the Catholic-aligned adjudicating and coercing power that "
    "this communion's whole refusal-of-imperial-legitimacy pattern is defined against, and on which "
    "every one of its Historical Pressures depends (Doc_01 SS2). The two-party contest itself does "
    "not end there: it persists under Vandal and then Byzantine rule for roughly a further century and "
    "a half, falling silent only after Gregory the Great's correspondence in the 590s - four letters "
    "of his, directly read, still urge suppression, a council, and an inquiry into Donatist rebaptism "
    "in Numidia (Doc_02 SS7). No continuous line to any present-day communion is documented at any "
    "point, and this world's own Living Tradition Status is not confirmed. This world's own "
    "self-description is the Church of the Martyrs: the pure, persecuted, true church, holding an "
    "unbroken traditor-free ordination line against a rival it regards as tainted and, from 312 "
    "onward, state-favored."
)

FORMATION_LOGIC = (
    "One conviction, lived out through purity, rite, memory, and refusal, rather than four "
    "commitments that happen to coexist: we are the pure, persecuted, true church, proved by what we "
    "will not concede and by what we have suffered for refusing to concede it (Doc_07 SS2I, SS5). A "
    "fully formed member holds without qualification that a sacrament's validity rises and falls on "
    "the giver's own unbroken purity, and has been rebaptized - deliberately, individually, bodily - "
    "into the one communion whose ministers can be trusted to give it. THE MECHANISM IS NOT TEACHING. "
    "Formation here does not run through speculative doctrine or a developed interpretive tradition; "
    "this world argues one question, sacramental validity, with real rigor, and almost nothing else "
    "(Doc_07 SS2D, SS5). It runs instead through three things a person does and undergoes: an enacted "
    "threshold crossed once and bodily (rebaptism); repeated commemorative narration, the community's "
    "own dead held by name, at the grave, on the appointed day, their account read aloud so the same "
    "conviction happens again in the hearing; and lived legal jeopardy, a whole church existing under "
    "continuous external legal pressure punctuated by episodes of acute persecution. A person is "
    "formed less by being taught a doctrine than by doing the rite, hearing the story, and living "
    "inside the pressure that the doctrine and the story both explain. THE ARC runs from that "
    "threshold, through a parallel institutional life under jeopardy, toward maturity that looks like "
    "the martyr - not necessarily literal death, but the settled readiness the martyr narratives hold "
    "up as the ideal: suffering chosen over a peace that would concede the rival's legitimacy. TWO "
    "PERSECUTIONS ARE HELD DISTINCT, NOT MERGED (Doc_07 SS3A): the empire-wide Diocletianic "
    "persecution, suffered alongside the eventual rival before the schism existed, supplies the "
    "traditio accusation the whole doctrinal argument stands on; the later Macarian repression of "
    "347-348, suffered AT that same rival's own instigation, supplies the named martyrs actually "
    "commemorated. A formed member can say precisely which persecution grounds the accusation and "
    "which grounds the grief. AND THE SYSTEM WAS BUILT TO SURVIVE AN OSCILLATING STATE. This is not a "
    "fixed structure persecution happened to interrupt; it is one built, from its founding moment, to "
    "be lived under a power that could tip without warning from coercion to toleration to renewed "
    "suppression - which is exactly why the refusal is held with three specific pragmatic exceptions "
    "rather than absolute purity of principle (the 313 appeal to Constantine, the 361 petition to "
    "Julian, and the 390s invocation of imperial and proconsular machinery against the Maximianists), "
    "each falling at a moment the external power briefly offered something to gain by engaging it "
    "(Doc_07 SS4). To be formed here was to hold an absolute conviction and a named, undenied "
    "exception to it in the same breath without experiencing that as contradiction: the gap was held "
    "openly, inside the same conviction, stated plainly in the same texts that state the doctrine at "
    "its most absolute, and naming it was never thought to require closing it (Doc_07 SS6)."
)

THINNESS = (
    "One pattern, repeating at every scale: this world's evidence survives in INVERSE proportion to "
    "how directly it can be checked without a hostile hand mediating it (Doc_07 SS5). Nearly all "
    "vendored textual material passed through Catholic hands - Optatus of Milevis and Augustine of "
    "Hippo - before reaching us, and this severe Author Gravity concentration is named as this world's "
    "CENTRAL evidentiary problem, not a background caveat (Doc_01 SS7 item 1; Doc_02 SS6). Donatist "
    "literature survives almost entirely as quotation embedded inside its own refutations. Richest, "
    "accordingly, in what the opponents argued about at length: the purity doctrine and its rebaptism "
    "consequence, the legal and institutional shape of the schism, the conciliar and imperial "
    "documentary record, and the martyr narratives - and, unusually, in one stratum of material that "
    "escaped that mediation entirely, the Deo laudes acclamation cut in stone, this world's strongest "
    "single anchor precisely because it was never textual to begin with. THE SKEW IS NOT THE USUAL "
    "ONE. Donatism was, for substantial regions and periods, the numerically dominant church, not an "
    "elite minority current: its ordinary members are not a separate, thin population but the bulk of "
    "the movement itself, unreachable in their own words for reasons of institutional loss rather than "
    "social marginality (Doc_02 SS6; Doc_01 SS2). Thin to silent, structurally: the ordinary "
    "believer's own interior life, known mostly through what opponents chose to argue against; the "
    "feelings a hostile-mediated record does not preserve - fear, doubt, quiet defection, a traditor's "
    "own interior life - as against the vindication and defiant joy that DO survive, because those "
    "survive in the martyr texts that no opponent filtered (Doc_07 SS2B, SS5); speculative and "
    "hermeneutical theology beyond Tyconius's single case, a genuine disclosed absence independently "
    "confirmed by four separate construction documents rather than an unexplored one (Doc_01 SS3; "
    "Doc_07 SS3B, SS7); the physical rooms - Numidian basilica archaeology remains honestly undone, "
    "with no specific site report named anywhere in this world's source ecology, so that this world "
    "knows its own acclamation far better than the room it was spoken in; women, save for one named "
    "wealthy Carthaginian laywoman preserved only inside the founding hostile narrative's explanation "
    "for why the schism happened at all, and a second woman behind the Maximianist schism whom "
    "Augustine parallels to her and never names; and a Donatist-authored institutional record of this "
    "world's own external forces - no surviving Donatist chronicle of Arles, no Donatist "
    "administrative account of the Macarian repression, only the martyr-cult narrative response to it "
    "(Doc_02 SS6)."
)

CAUTIONS = (
    "1) AUTHOR GRAVITY, NAMED AS THE CENTRAL PROBLEM: nearly the whole textual record is this "
    "communion's own opponents writing against it. Never convert Optatus's or Augustine's narrative "
    "richness or documentary specificity into independent corroboration - including the Maximianist "
    "episode, which reaches us almost entirely through Augustine's own quotation and must be marked as "
    "such (Doc_01 SS7 item 1). Even the documentary dossier appended to Optatus, genuine court and "
    "conciliar acts though its items are, sits inside that concentration: the selection is his own act "
    "(Registry row 2). 2) THE FOUR CORRECTIONS ARE REAL BUT BOUNDED: four texts speak AS Donatists "
    "rather than being spoken about - the Passio Donati sermon, the Passio Marculi, Macrobius's own "
    "letter, and Tyconius's Liber Regularum - and the 411 conference transcript records Donatist "
    "bishops' own words without an adversary selecting them for refutation. Every one is short or "
    "occasional against the scale of the opposing corpus, and the transcript's vendored scan carries "
    "this corpus's worst OCR on record for a text of that significance (Doc_02 SS6). 3) FRENDS THESIS "
    "IS CONTESTED, NOT SETTLED: the native-social-protest reading of this world's rural strength and "
    "of the Circumcellions is the most contested single argument this world's Registry draws on, with "
    "Shaw, Brown, and Tengstrom as named counterpoints; it is flagged for priority second-opinion "
    "review before it supports any specific claim (Registry rows 23, 24, 26, 46). 4) THE CIRCUMCELLION "
    "SPLIT MUST BE HELD: the group's EXISTENCE is independently attested outside hostile polemic - "
    "Codex Theodosianus 16.5.52 fines circumcelliones ten pounds of silver, the only rank of ten fined "
    "in silver rather than gold - but its CHARACTERISATION is substantially shaped by that polemic, "
    "and the two must never be merged (Doc_01 SS7 item 2; Doc_02 SS6). Their own self-designation, "
    "agonistici, is confirmed ABSENT from the Theodosian Code and its source passage in Augustine "
    "remains unidentified. 5) TWO VENDORED AUTHORITIES DISAGREE ABOUT THE PASSIO DONATI and neither is "
    "adopted: Mabillon dates the persecution circa 340; Monceaux dates it to 12 March 317 with "
    "composition circa 320, proposes an eyewitness Donatist bishop of Carthage as preacher, and "
    "resolves the title differently. Never cite a settled date or author for it (Doc_02 SS4, SS8). "
    "6) THE MARTYR PASSIONES DO NOT DATE THEMSELVES: the Passio Marculi's own heading gives a day and "
    "no year, and the 347-348 Macarian dating rests on the standard field literature, not on the "
    "texts. 7) HOMONYMS, EASILY CONFLATED: the Maximian of the Maximianist schism (a deposed deacon, "
    "393) is a different person from the martyr Maximian of the Passio Isaac et Maximiani; the Optatus "
    "who was Donatist bishop of Thamugadi is not Optatus of Milevis, the Catholic polemicist. 8) THE "
    "REFUSAL IS DOMINANT, NOT ABSOLUTE: this communion turned to imperial or proconsular machinery at "
    "three specific points - 313, 361, and the 390s against its own Maximianist dissidents - and its "
    "councils received returning Maximianist clergy without reordination or rebaptism at all. These "
    "are not embarrassments to manage; this world's own record states them plainly in the same texts "
    "that state the doctrine at its most absolute (Doc_01 SS5; Doc_07 SS6). 9) STRAND-SINGULAR, "
    "TESTED: both Tyconius and the Maximianist episode were tested against Article 21's bar and "
    "rejected on the record, not overlooked - Tyconius as a condemned individual dissenting voice with "
    "no attested following or distinct communal practice, the Maximianists as a dispute over who "
    "should hold a see rather than a distinct pattern of communal life (Doc_01 SS4). Tyconius's own "
    "formal standing within the communion is deliberately left open. 10) UNREAD MATERIAL, NAMED AS "
    "GAPS: Monceaux's two dedicated Donatism volumes are vendored and essentially unread, including a "
    "whole chapter on Petilian, whose voice this world is otherwise thinnest on; the Gesta's "
    "transcript has been read for one full act; Contra Gaudentium's preserved Donatist letters are "
    "confirmed present and unread; and the standard modern instruments - Tilley's martyr-story "
    "translations, Maier's documentary dossier, Mandouze's prosopography, Duval's martyr-cult corpus - "
    "are all in copyright and unvendorable. 11) NO SEARCH RECORD EXISTS: no per-search log was kept "
    "during this world's source work, unlike some sibling worlds; the Registry's Discovery column was "
    "reconstructed alongside its own drafting rather than logged contemporaneously, and its own "
    "Saturation Statement declines to claim completeness - no fresh field-bibliography sweep against "
    "standard reference instruments has been run."
)

THIN_TOPICS = [
    {
        "keywords": ["ordinary believer", "interior life", "daily household life", "village religion",
                     "what an ordinary week felt like"],
        "note": "The bulk of this movement, not a thin minority within it - and unreachable in its own "
                "words. What is known comes mostly through what opponents chose to argue against, not "
                "through any account these households left of themselves.",
    },
    {
        "keywords": ["fear", "doubt", "wavering", "quiet defection", "a traditor's own experience"],
        "note": "A hostile-mediated record structurally does not preserve these. The feelings that DO "
                "survive - vindication, defiant joy - survive because they sit in the martyr texts no "
                "opponent filtered.",
    },
    {
        "keywords": ["women's own words", "Lucilla's own account", "the second unnamed woman",
                     "female participation"],
        "note": "No woman of this world left a text. Lucilla survives only inside the founding hostile "
                "narrative's explanation for why the schism happened; the woman behind the Maximianist "
                "schism is paralleled to her by Augustine and never named at all.",
    },
    {
        "keywords": ["basilica archaeology", "excavation", "what the buildings looked like",
                     "material remains", "the room where the washing happened"],
        "note": "No specific site report, excavation record, or publication is named anywhere in this "
                "world's source ecology. The acclamation cut in stone is known far better than the "
                "room it was spoken in.",
    },
    {
        "keywords": ["speculative theology", "hermeneutics beyond Tyconius", "biblical interpretation",
                     "the wider councils' reasoning"],
        "note": "This world argues one question - sacramental validity - with real rigor and almost "
                "nothing else. Tyconius's Book of Rules is the single substantial exception, and even "
                "its own seven Rules have not been read into this build.",
    },
    {
        "keywords": ["Circumcellion conduct", "agonistici", "what the circumcellions actually did"],
        "note": "Their existence is settled by imperial legislation; their character is known only "
                "through hostile polemic. Their own self-designation is confirmed absent from the "
                "imperial law and its source passage is unidentified.",
    },
    {
        "keywords": ["Donatist chronicle", "Donatist account of Arles",
                     "Donatist record of the Macarian repression", "institutional self-defense"],
        "note": "This world's external forces survive almost entirely through the acting or allied "
                "party's own documentation of them. No Donatist chronicle, administrative record, or "
                "documentary self-defense of these events survives - only the martyr-cult narrative "
                "response.",
    },
    {
        "keywords": ["after 439", "Vandal period", "Byzantine Africa", "living descendant",
                     "what became of the movement"],
        "note": "The contest continues under Vandal and Byzantine rule for roughly a century and a "
                "half beyond this window, falling silent after Gregory the Great's 590s "
                "correspondence. No continuous line to any present-day communion is documented at any "
                "point.",
    },
]

WORLD_CORE_SOURCES = [
    {"source_id": "don.source.optatus-against-the-donatists",
     "locus": "Books I-VII, esp. I.16", "license": "public-domain"},
    {"source_id": "don.source.augustine-answer-to-petilian",
     "locus": "3 books -- Petilian's own letters quoted clause by clause", "license": "public-domain"},
    {"source_id": "don.source.tyconius-liber-regularum",
     "locus": "whole work -- the one substantial independently-surviving interpretive text",
     "license": "public-domain"},
    {"source_id": "don.source.passio-marculi",
     "locus": "whole work", "license": "public-domain"},
    {"source_id": "don.source.passio-isaac-et-maximiani",
     "locus": "whole work -- Macrobius's own letter to the Carthage congregation",
     "license": "public-domain"},
    {"source_id": "don.source.deo-laudes-acclamation",
     "locus": "CIL VIII 17732, with 20482, 17368, 18669", "license": "public-domain"},
    {"source_id": "don.source.gesta-collationis-carthaginiensis-411",
     "locus": "the 411 conference acts, via the vendored Migne printing (Registry row 55)",
     "license": "public-domain"},
    {"source_id": "don.source.codex-theodosianus-book-16",
     "locus": "16.5.52 (412 Ian. 30); the 405 Edict of Unity", "license": "public-domain"},
]

WORLD_CORE_BODY = """Built from Doc_01_World_Identification_Boundaries_Orientation.md (SS1 identity and Living Tradition Status, SS2 the two-date opening and the precise meaning of the 439 close, SS4 the strand determination, SS5 the preliminary six-cell forces sketch, SS7 the open items binding later steps), Doc_07_Integrated_Ecology_Analysis.md (SS2I formation logic, SS3A the two-persecution memory structure, SS4 forces as integration lens, SS5 cross-lens synthesis, SS6 the integrative observation, SS7 gaps and limits), and Doc_02_Source_Ecology.md (SS6 source asymmetries and missing voices, SS7 the terminal-record disclosure, SS8 confidence map, SS9 open items) together with Source_Registry.md's own named gaps and its Discovery-methodology and Saturation statements.

WORLD_ID: `donatism`. This world has no entry in records/worlds.yaml at all, so no registry value is being contradicted; `donatism` matches cic/corpus-map/donatism.yaml's own `atlas_id`, which is the census movement id and the join key, so the record id prefix (`don`), the world_id (`donatism`), and the census join all read consistently. Registering the world in records/worlds.yaml is a later admission-track step, out of scope for this first record-authoring pass, exactly as it was for the sibling world compiled before this one.

TIME_WINDOW: start 311, end 439. The Registry and Doc_01 both carry the opening as 311/312 rather than resolving it - the sources support both years and not a choice between them - and the schema's time_window takes a single integer, so the earlier of the two carried years is used and the doubled opening is stated in `horizon` rather than silently collapsed. The 439 close is Doc_01 SS2's own, and its precise meaning (the removal of the Roman imperial adjudicating power, not the end of the two-party contest) is carried in `horizon` too, because the distinction is one Doc_01 SS2 insists must not be conflated.

WHAT THIS RECORD DOES NOT CLAIM. Living Tradition Status is PENDING and is a project-lead act this compilation cannot perform (Doc_01 SS1); `horizon` states the no-documented-descendant finding without resolving Article 29's gate. The Representative does not appear in this record, and no Representative content is compiled into it.

REGISTRY ROW 29 IS NOT COMPILED AS A SOURCE RECORD FOR THIS WORLD, and the omission is deliberate, not an error to be corrected later. That row - Novatian's De Trinitate and Novatianist material generally - carries Boundary Status "Excluded", Exclusion Reason "Named Comparandum", and a Licensed-For field reading "N/A -- excluded". It exists in the Registry precisely to guard against a concrete temptation: Novatian's De Trinitate sits in the SAME vendored volume as this world's own Cyprianic antecedent corpus (Registry rows 7-10), so a builder working through that volume for Cyprian is already inside the file that contains Novatian, and the corpus map's own note on Cyprian's De Unitate records that it "was written against the Novatianist schism among others." Novatianism is a different, earlier rigorist schism (Rome, c. 251) that also practiced rebaptism - a genuine surface similarity. None of that makes it evidence for, or continuous with, this world's own rebaptism practice or ecclesiology, which arose independently and later, over a different dispute. Emitting it as a `don` source record would assert, in the one field a downstream reader trusts, exactly the thing the row exists to deny. Fifty-five of the Registry's fifty-six rows are compiled; this is the one that is not.
"""


# ------------------------------------------------------------------ emit ---
def _yaml_dump(payload: dict) -> str:
    return yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False)


def _write(path: Path, payload: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + _yaml_dump(payload) + "---\n" + body.strip() + "\n", encoding="utf-8")


def emit_source(r: dict) -> Path:
    rid = f"don.source.{r['slug']}"
    conf = {
        "citation_specificity": r["cite"],
        "verification_state": r["verif"],
        "evidentiary_weight": r["weight"],
        "formation_confidence": r["formation"],
        "divergence_note": r.get("divergence"),
    }
    # gate_confidence_crosscheck, satisfied by construction rather than by hope.
    if conf["formation_confidence"] == "Documented" and conf["divergence_note"] is None:
        assert conf["verification_state"] == "verified-direct", rid
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "source",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "etic",
        "canon_cells": [],
        "confidence": conf,
        "sources": [],
        "relations": [],
        "author": r["author"],
        "work": r["work"],
        "edition": r["edition"],
        "rights_status": r["rights"],
        "attribution_status": r["attribution"],
        "discovery_channel": r["discovery"],
        "external_ids": {"don_source_registry_row": r["row"]},
    }
    path = OUT_ROOT / "source" / f"{rid}.md"
    _write(path, payload, r["body"])
    return path


def emit_world_core() -> Path:
    rid = "don.core.donatism"
    payload = {
        "id": rid,
        "world_id": WORLD_ID,
        "record_type": "world_core",
        "schema_version": SCHEMA_VERSION,
        "status": "draft",
        "register": "emic",
        "canon_cells": [],
        "confidence": {
            "citation_specificity": "B",
            "verification_state": "verified-via-authority",
            "evidentiary_weight": "load-bearing",
            "formation_confidence": "Dominant Modern Reconstruction",
            "divergence_note": (
                "This record synthesises nine completed construction documents rather than reading a "
                "text directly, so verification runs via those documents' own authority, not via a "
                "primary source reopened here. Doc_07 SS7 names the synthesis's own central claim - "
                "that purity, once adopted, necessarily generates rite, memory, institution, and "
                "political posture as a single logical unfolding rather than four separately-arrived-at "
                "commitments - as this build's own synthetic judgment, not a claim stated in any single "
                "source, and directs external scholarly review to test whether it overstates the "
                "coherence of what was on the ground a more contingent and locally variable movement."
            ),
        },
        "sources": WORLD_CORE_SOURCES,
        "relations": [],
        "time_window": TIME_WINDOW,
        "horizon": HORIZON,
        "formation_logic": FORMATION_LOGIC,
        "thinness": THINNESS,
        "cautions": CAUTIONS,
        "thin_topics": THIN_TOPICS,
    }
    path = OUT_ROOT / "world_core" / f"{rid}.md"
    _write(path, payload, WORLD_CORE_BODY)
    return path


def main() -> int:
    slugs = [r["slug"] for r in ROWS]
    assert len(slugs) == len(set(slugs)), "duplicate slug"
    rows = [r["row"] for r in ROWS]
    assert rows == sorted(rows), "rows out of order"
    assert 29 not in rows, "row 29 is Excluded/Named Comparandum and must not be emitted"
    assert len(ROWS) == 55, f"expected 55 Native rows, got {len(ROWS)}"

    written = [emit_source(r) for r in ROWS]
    written.append(emit_world_core())
    for p in written:
        print(p.relative_to(REPO_ROOT))
    print(f"\n{len(written)} records written "
          f"({len(ROWS)} source + 1 world_core); Registry row 29 deliberately not emitted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
