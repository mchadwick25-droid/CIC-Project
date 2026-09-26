"""B-1 (S2.1), lpc equivalent: Latin Pastoral-Congregational Christianity (`lpc`)
source + world_core records.

WHAT THIS SCRIPT DOES. Converts this world's completed Phase A documents into
WRS records under records/lpc/{source,world_core}/, per the live schema
(engine/m1/schemas.py) and gate battery (engine/m1/gates.py). This is the
FIRST record-authoring pass for this world; no `lpc` records existed before
this script ran (records/lpc/ did not exist at all -- confirmed by listing
records/ directly, not assumed). This is the direct methodological equivalent
of Build/worlds/don/scripts/wb_don_s21.py's own B-1 pass, run against `lpc`'s own
inputs, at roughly four times don's own scale (207 Native rows against don's
55) -- the per-row authoring below is scaled to what each row's own
Verification Note actually contains, not padded to match don's own prose
length: `lpc`'s Source_Registry.md is itself far denser for its ~30 primary
Cyprian/Augustine rows and, from Round 3 onward, far terser for the ~150
recall-test/PRESS secondary-scholarship rows it repeatedly adds ("Not
currently vendored. In copyright; consultation-only. Flagged for priority
second-opinion review..." -- often the row's entire Verification Note). This
script's own per-row prose follows that same shape rather than inventing
depth the row itself does not carry.

INPUTS, mapped to OUTPUTS, precisely:
  - Build/worlds/lpc/Source_Registry.md -> the 207 `source` records (ROWS below).
    The Registry's table holds 212 numbered rows, counted mechanically off
    the table's own final row number (212), not taken from any prior
    estimate or from the document's own header, which states plainly that it
    "has never been able to state [the row count] reliably by hand." FIVE
    carry Boundary Status "Excluded": row 28 (*The Passion of the Scillitan
    Martyrs*, 180 CE, Named Comparandum -- predates this world's own c. 246
    start by 66 years), row 29 (Tertullian's corpus generally, Named
    Comparandum -- "credited with forging" this world's own theological
    vocabulary "without Tertullian himself being this world's own voice",
    Doc_01 SS7), row 98 (Maier, *L'épiscopat de l'Afrique romaine, vandale et
    byzantine*, Out-of-Boundary -- extends through the Vandal/Byzantine
    periods past this world's own 430 close), row 128 (Wolff, *Littérature,
    politique et religion en Afrique vandale*, Out-of-Boundary -- entirely
    after 430), and row 204, which carries a DUAL disposition on its own two
    physical portions and is Excluded on BOTH: its Scillitan-Martyrs portion
    mirrors row 28 exactly (a second-witness Latin/Greek text of the same
    excluded work), and its Perpetua-and-Felicitas portion is not merely
    Excluded but ASSIGNED TO A THIRD WORLD ENTIRELY -- `tertullian-s-voice`,
    on Mark's own prior 2026-08-26 ruling, independently reconfirmed this
    session -- neither portion is Native to `lpc` on any reading. All five
    are deliberately NOT emitted, following the don/cappadocian precedent
    exactly (wb_don_s21.py's own module docstring: "Only rows with Boundary
    Status 'Native' become... records... deliberately NOT emitted...
    Flagged upward rather than silently dropped"). Flagged upward rather
    than silently dropped; see the B-1 handback note.
  - Source_Acquisition_Manifest.md SS1-SS3 -> rights_status. Unlike don's own
    Manifest, `lpc`'s own three-bucket split does not need re-deriving from
    prose: SS3 STATES ITS OWN MEMBERSHIP RULE DIRECTLY -- "every Native,
    Confidence-C-or-below Registry row whose Verification Note says 'in
    copyright' and 'consultation-only' or 'not a vendoring candidate' is in
    this category" -- rather than don's Manifest, which required inferring
    three buckets (ss1/ss2/ss3) from separate section headings. Checking a
    row against that rule directly, the way the Manifest's own SS3 instructs,
    IS the mechanical half of this field; author/work/edition/divergence
    remain authored per row exactly as they are for don. `lpc`'s own SS1
    (G1-G9, all now closed or all-but-closed as of this session) supplies the
    small set of newly-vendored Latin critical editions (rows 191-212, 88)
    and the handful of "standing reference" rows superseded by them (e.g.
    row 39 by rows 191/194, row 61 by rows 193/195/196, row 40 by row 205,
    row 56 by rows 206-208, row 78/67 by row 209, row 89 by row 210, row 90
    by row 211, row 99 by row 212).
  - Doc_01_World_Identification_Boundaries_Orientation.md SS1, SS2, SS5, SS7
    -> world_core.time_window, .horizon, .cautions.
  - Doc_07_Integrated_Ecology_Analysis.md SS2I, SS3A, SS5, SS6 ->
    world_core.formation_logic.
  - Doc_02_Source_Ecology.md SS6 (Source Asymmetries and Missing Voices), SS8
    (Confidence Map), SS9 (open items) + Doc_07 SS7 (Gaps and Limits) ->
    world_core.thinness / .cautions / .thin_topics.

MECHANICAL vs AUTHORED, field by field, so a reviewer can tell what to
re-check against the Registry directly and what required this script's own
reading and judgment -- the same discipline don's own script states for
itself, applied here to a differently-shaped Registry:

  - id, world_id, record_type, schema_version, status, register, canon_cells,
    relations: MECHANICAL. register="etic" for every source record (a source
    record describes an external text, not this world's own first-person
    voice); register="emic" on world_core. canon_cells=[] throughout: no
    canon-cell tagging work has happened for this world yet. schema_version=2,
    matching every currently-built world.

  - world_id: "latin-pastoral-congregational-christianity". MECHANICAL from
    this task's own instruction and independently consistent with the one
    other place this world already has a stable identifier in the live
    system: cic/corpus-map/latin-pastoral-congregational-christianity.yaml's
    own `atlas_id: latin-pastoral-congregational-christianity`, the census
    movement id and join key. records/worlds.yaml has NO `lpc` entry at all
    (confirmed by reading it directly), so no registry value is contradicted;
    registering the world there is a later admission-track step, out of
    scope here, exactly as it was for don. `lpc` remains the short
    directory/id-prefix code; the long slug is the world-identifier.

  - author / work / edition: AUTHORED, per row, by hand, reading each row's
    own Source cell and Verification Note. `lpc`'s own Registry packs the
    same six kinds of information (author, work-with-scope, edition,
    translator/editor, press, year) into one free-text Source cell that don's
    own script describes for its sibling world, and splitting it is equally
    not a mechanical regex split here. Several rows required real judgment
    to phrase honestly: row 6 (a pseudo-Cyprianic body kept under Cyprian's
    own name by a corpus-map ruling, ALSO filed a second time under a
    pseudepigrapha shelf -- "a work circulating under a name that is not its
    author's is a pseudepigraphon by definition"); row 41 (the *Acta
    Proconsularia*, which never received its own numbered vendoring but is
    now folded, unread as its own object, inside row 194's Hartel Pars III
    file -- this record's own `edition` field names row 194's actual file
    rather than inventing a standalone one the Registry itself does not
    claim); row 43 (Augustine's Letter XCIII, which the census assigns to
    `donatism` with no `lpc` role at all, yet which Doc_01 SS5 and the
    Registry itself hold Native on the Template's own second test -- drawn
    on directly as this world's own first-person account of Augustine's
    change of mind, not as evidence about Donatism's side); and row 65 (the
    411 Conference acts), this Registry's own richest single row -- fourteen
    numbered acts in which Augustine speaks, independently counted and
    quoted, inside a vendored file this world's own corpus-map now assigns
    `role: context` -- whose own Licensed-For nonetheless stays exactly
    where it started (the Conference's ordinary, undisputed date), a
    disclosed gap between what was found and what is drawn on that this
    record does not paper over. Where the Registry names a `cic/texts/...`
    vendored file, or the corpus-map's own `_staging` entry names one for a
    row the Registry itself leaves unstated, that path is carried into
    `edition` verbatim (cross-checked directly against
    cic/corpus-map/latin-pastoral-congregational-christianity.yaml, not
    guessed); a small number of rows name no specific file in either place,
    and this record says so rather than inventing one.

  - rights_status: AUTHORED per row via the RIGHTS_* constants below, three
    buckets (a genuine simplification from don's five, not a shortcut around
    don's own reasoning -- see below):
      * VENDORED_VERIFIED -- public domain, vendored in cic/texts/, and the
        specific content this row licenses was itself directly read and
        verified, either across Doc_01's own nine adversarial review rounds
        (this world's original ANF05/NPNF corpus) or by this build session's
        own direct archive.org fetch-and-verify (Source_Acquisition_
        Manifest.md SS1's G1-G9 fulfillments, rows 88 and 191-212).
      * VENDORED_INHERITED -- public domain, vendored in cic/texts/ as part
        of the corpus map's own pre-existing inventory (`role: tradition`,
        `confidence: assigned`), carried into this world's construction
        without this row's own specific locus being independently
        re-collated this pass.
      * CONSULTATION_ONLY -- in-copyright, never vendored, per
        Source_Acquisition_Manifest.md SS3's own stated membership rule,
        quoted in full above. Unlike don's own Manifest, `lpc`'s SS3 draws
        no distinction between an in-copyright PRIMARY edition (e.g. row 58,
        the current critical Cyprian corpus) and in-copyright SECONDARY
        scholarship (e.g. row 30, Peter Brown's biography) -- SS3 states
        this itself: "rows in this category span Types P, P/S, M, and L as
        well as S... [and] share the operational fact that matters... in
        copyright, never vendored, no acquisition decision needed...
        regardless of which Registry Type each one carries." Collapsing
        don's own INCOPYRIGHT_RECORDED/CONSULTATION_ONLY split into one
        bucket here is therefore not this script's own simplification; it is
        `lpc`'s own governing document declining to draw the distinction don's
        own Manifest draws for a different world.
      * NO_EDITION_HELD -- no edition or publication is named anywhere in
        the Registry or the Manifest for this row's own object, so there is
        no rights position to state. Used for exactly one row (38, Numidian
        basilica archaeology generally -- a recognized field category with
        no author, work, or excavation report named at all) and stated as a
        negative rather than papered over with a plausible-sounding default.
    No row is left blank: gate_rights fails closed on blank, and the last two
    buckets each required an honest non-blank negative rather than a false
    positive. Every vendored file named in an `edition` field was checked to
    exist on disk before this script was written (a direct listing of
    cic/texts/, not a claim read off the Registry).

  - attribution_status: AUTHORED per row. Default "attributed". Populated
    with a short descriptive phrase, never forced into a binary the schema
    does not require, wherever the Registry's own Verification Note flags a
    contested, anonymous, mediated, pseudepigraphal, or editorially-supplied
    attribution: rows 6, 8, 19 (Divjak's own spelling correction, "Epistolae"
    not "Epistulae"), 21 (Codex Theodosianus, documentary), 25 (a documentary
    conciliar/legal body), 27 (Optatus, provisionally double-placed on the
    census), 41 (attested only inside a larger vendored volume, no
    independent transmission of its own), 43 (Augustine's own words, but a
    letter the census assigns to a different world), 50 (Passio Donati-style
    contested authorship is a don-world matter, not repeated here -- no `lpc`
    row shares that exact shape), 55 (Passio Isaac/Marculi-style anonymous
    martyr texts are likewise a don-world matter, not repeated here), 88
    (transcribed at a named non-scholarly host, edition ancestry unstated),
    103, 127, 70, 86, 87, 96 (Native-but-unlicensed rows, whose own
    Verification Notes state plainly why no boundary exclusion applies), 194
    (the *Vita Caecilii Cypriani*, "vulgo adscripta" to Pontius per its own
    heading), 204 excluded, and 205 (Harnack's own edition, an interpretive
    supplement, not an independent recension).

  - discovery_channel: AUTHORED per row, taken from the Registry's own
    Discovery column and, for the great majority of rows added from Round 2
    onward, from the row's own Verification Note, since the Registry's own
    Discovery methodology note states plainly that no per-search
    `records/lpc/search_record/` log was kept and that column reflects the
    corpus map for primary sources and this session's own WebSearch queries
    for secondary scholarship "where a search was actually run." The
    Registry row number is named in the prose AND mirrored into
    external_ids.lpc_source_registry_row, the same judgment call don's own
    script makes for the same reason: the schema has no dedicated
    Registry-row field, and a queryable object field makes future
    cross-checking mechanical.

  - confidence.citation_specificity: MECHANICAL. Copied straight from the
    Registry's own Confidence (A-E) column, including the two rows whose
    own header states a letter was raised or corrected in place (row 56,
    raised C->B on a resolved public-domain finding; row 88, held at C
    deliberately distinct from row 44's own B).

  - confidence.verification_state: AUTHORED, through the Registry's OWN
    stated calibration rule (Source_Registry.md's own "Confidence
    calibration rule, per the Template" paragraph, quoted at line 10 of that
    file), applied row by row rather than transformed from the letter alone:
      * Registry A -> verified-direct. Every Confidence-A row in this
        Registry states its own direct check in the same Verification Note
        that earns the letter -- unlike don's Registry, no `lpc` row reaches
        A without stating one, so this mapping needed no case-by-case
        judgment call the way don's row 55/28 pair did.
      * Registry B where the underlying work IS vendored (the corpus map's
        own `role: tradition`, `confidence: assigned` entry) -> verified-
        via-authority: the licensed claim rests on a real, checkable vendored
        text, even where this specific pass did not re-collate it locus by
        locus.
      * Registry B where the named work is NOT vendored (bibliographic
        record WebSearch-confirmed, the work itself never opened) ->
        named-not-rechecked. A bibliographic record externally verified is
        not a text checked -- don's own rule, applied here to `lpc`'s own
        much larger population of exactly this shape (rows 30-33, 36, and
        several later-round additions).
      * Registry C, and Registry D where the row nonetheless names a real
        author and work (the great majority of `lpc`'s own D rows: 134, 136,
        146, 147, 151, 159 all name a specific reference work, article, or
        thesis) -> named-not-rechecked, by the Registry's own definition of C
        ("tied to a real author or work but no specific locus is pinpointed")
        extended to a D row that in substance meets the same bar -- UNLESS
        the row's own Verification Note states that this build session
        directly opened and confirmed the object itself (a title page, an
        opening/closing line, a table of contents, an OCR-quality sample),
        in which case verified-direct is used instead, even though
        citation_specificity stays at the Registry's own C or D letter. This
        is not a second departure invented for this world; it is don's own
        script's rule for its own row 55 (Migne PL11), restated:
        citation_specificity answers whether the row's own LICENSED CLAIM
        was checked at a specific, exploitable locus; verification_state
        answers whether the OBJECT ITSELF was directly opened this session.
        The two axes are independent by the schema's own design, and `lpc`'s
        own Registry -- unlike don's -- populates this exact combination
        densely, across the whole 2026-09-08 vendoring pass (rows 89, 90,
        99, 191, 193-203, 205-212): each was fetched and its own identity
        confirmed directly, while the specific claim it would license has
        mostly not yet been read out and exploited -- which is exactly why
        citation_specificity stays where the Registry's own table leaves it
        rather than being silently raised.
    ONE row departs from even that fuller mapping, stated here rather than
    buried, the same discipline don's own script applies to its own two
    departures: row 38 (Numidian basilica archaeology) is graded Confidence
    D by the Registry's own table, but this script does not renumber that
    grade (MECHANICAL, copied as D) while declining to certify a
    verification state the row cannot support: no author, work, or
    excavation report is named at all -- there is no object here for any
    session to have opened -- which is the Registry's own definition of
    nothing-to-check-against rather than of a real-but-unpinpointed locus.
    verification_state is therefore set to `unverified`, the more
    conservative value, and the record's own body says so.

  - confidence.evidentiary_weight: AUTHORED per row from the Registry's own
    Licensed-For column. `load-bearing` is used where the row grounds a
    specific, named claim this world's own construction (Doc_01 or Doc_02)
    actually makes and relies on. `corroborating` is used where a row
    supports or sharpens an existing claim without itself being the ground
    of it. `illustrative` is used, by far the most common weight in this
    Registry, wherever a row's own Licensed-For reads "Not currently
    licensed for a specific claim" or "noted for completeness" -- a
    deliberate, disclosed non-use, not a downgrade. `contested` is not used
    anywhere in this pass: unlike don's Registry, no `lpc` row disputes its
    own SOURCE OBJECT's genuineness or transmission in the narrow way don's
    Acta Saturnini row does; the closest candidates (the De Unitate
    two-recension question, row 3; the Divjak discovery-date disagreement,
    row 49) are disclosed in each row's own divergence_note instead, keeping
    the two axes independent, the same rule don's own script states for its
    own Frend/Tengstrom rows.

  - confidence.formation_confidence: AUTHORED per row, Article 17's five-
    level vocabulary, deliberately NOT derived from citation_specificity.
    `Documented` is used only where this record can honestly pair it with
    verified-direct, or with a stated divergence_note (gate_confidence_
    crosscheck's own rule: Documented + divergence_note=null requires
    verified-direct; Documented + a real divergence_note is never flagged
    regardless of verification_state, and this script's own emit_source()
    asserts the stronger of the two rather than leaving it to hope, matching
    don's own hard assertion). `Widely Accepted` is the default for the
    great bulk of this Registry's own secondary-scholarship population --
    real, checkable, uncontested bibliographic facts about standard field
    literature, not settled claims about this world's own internal life.
    `Contested` is used where this world's own construction documents
    genuinely does not consider a question closed: the conciliar-authority
    axis (Doc_01 SS8 item 10, rows 4 and 13's own divergence notes) and the
    De Unitate two-recension question (row 3). `Inferential-Thin` is used
    for row 38 alone among source rows, matching its own `unverified`
    departure above -- Doc_02 SS8's own Confidence Map independently bands
    "the material/epigraphic conditions of worship at Carthage or Hippo
    specifically" at Inferential-Thin, for the same reason.

  - confidence.divergence_note: AUTHORED. Null only where a row's own
    Verification Note genuinely discloses nothing beyond what MECHANICAL
    fields already carry -- rare in this Registry, whose entire discipline
    is disclosure-first, and populated on all but a small handful of the 207
    rows for exactly that reason (a higher fraction than don's own 54/55,
    not because this script tried harder but because `lpc`'s own Registry
    is built that way).

  - sources / relations on each source record: left empty by design, the
    same reasoning don's own script gives: populating cross-references
    between source records would require reciprocal `relations` entries on
    both sides for gate_reciprocity, for no benefit this step needs. The
    world_core record DOES populate `sources`, referencing eight source ids
    created in this same run.

WORLD_CORE SLUG: `lpc.core.latin-pastoral-congregational-christianity`. The
fleet's own eight (now nine, with don) world_core records use a short slug
naming the world itself; `latin-pastoral-congregational-christianity` matches
the corpus map's own `atlas_id`, so the id, the world_id, and the census join
key all read the same phrase, the identical reasoning don's own script gives
for its own `donatism` choice. No shorter self-designation is available or
appropriate here the way don's script considered and rejected
`church-of-the-martyrs`: this world's own Doc_01 SS1 states directly that its
Living Tradition Status confirmation "names no single heir... ancestral to
the Western church before its divisions" -- there is no single in-world
self-designation this record could mint as an id without asserting an
identity claim (a single line of descent) the confirmation itself declines to
make.

WHAT THIS SCRIPT DOES NOT DO: assign canon_cells (no canon-cell tagging has
happened for this world); register `lpc` in records/worlds.yaml (a later
admission-track step); emit any record type other than source and
world_core; touch any other world's records; emit Registry rows 28, 29, 98,
128, or 204.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
OUT_ROOT = REPO_ROOT / "records" / "lpc"
TEXTS_DIR = REPO_ROOT / "cic" / "texts"

WORLD_ID = "latin-pastoral-congregational-christianity"
SCHEMA_VERSION = 2

# ---------------------------------------------------------------- rights ---
RIGHTS_VENDORED_VERIFIED = (
    "public-domain; vendored in cic/texts/, and the specific content this row licenses was "
    "directly read and verified -- either across Doc_01's own nine adversarial review rounds, or "
    "by this build session's own direct archive.org fetch-and-verify pass "
    "(Source_Acquisition_Manifest.md SS1). Not re-opened for a rights re-check by this "
    "compilation pass."
)
RIGHTS_VENDORED_INHERITED = (
    "public-domain; vendored in cic/texts/ as part of the corpus map's own pre-existing "
    "inventory (role: tradition, confidence: assigned), carried into this world's construction "
    "without this row's own specific locus being independently re-collated this pass."
)
RIGHTS_CONSULTATION_ONLY = (
    "in-copyright; never vendored, consultation-only, per Source_Acquisition_Manifest.md SS3's "
    "own stated membership rule -- 'every Native, Confidence-C-or-below Registry row whose "
    "Verification Note says \"in copyright\" and \"consultation-only\" or \"not a vendoring "
    "candidate\" is in this category' -- spanning primary editions and secondary scholarship "
    "alike, per that same rule. Cited and consulted by this build, never quoted as licensed "
    "vendored material."
)
RIGHTS_CONSULTATION_ONLY_B = (
    "in-copyright; never vendored, consultation-only. This row sits above "
    "Source_Acquisition_Manifest.md \u00a7SS3's own stated Confidence-C-or-below "
    "membership rule (it is Confidence B, not C-or-below), so that rule is not cited "
    "for it -- the substantive classification (in-copyright, never vendored, "
    "consultation-only) rests on the Registry row's own Verification Note directly, "
    "not on SS3's categorical rule. Cited and consulted by this build, never quoted "
    "as licensed vendored material."
)
RIGHTS_NO_EDITION_HELD = (
    "No rights position is stated, because no edition, publication, author, or excavation "
    "report is named for this row anywhere in Source_Registry.md or "
    "Source_Acquisition_Manifest.md -- a recognized field category with nothing to vendor until "
    "a specific instrument is identified. Recorded as an honest negative rather than defaulted "
    "to a plausible-sounding status this build has not established."
)

# ------------------------------------------------------------------ rows ---
ROWS: list[dict] = [
    dict(
        row=1, slug="cyprian-epistles",
        author="Cyprian of Carthage",
        work="The Epistles (82 letters, including letters TO Cyprian from Rome, Cornelius, the "
             "confessors, and Firmilian of Caesarea)",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Cyprian, though the corpus embeds letters by others (Cornelius, "
                    "the Roman clergy, Firmilian, the confessors) under his own name, per the corpus "
                    "map's own note on the whole body's attribution -- not every letter in it is "
                    "demonstrably Cyprian's own composition.",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01; direct verification against "
                  "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml, div3 id=\"iv.iv.xxxix\", "
                  "\"iv.iv.xx\", \"iv.iv.xxi\" / 2026-09-01.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="A citation error stood in this build for six days and the correction is part of "
                   "the record, not tidied away: 'your suffrage and God's judgment' and 'ancient "
                   "venom' were first mis-cited to Epistle XL ('To Cornelius, on His Refusal to "
                   "Receive Novatian's Ordination'), which contains neither phrase -- both occur in "
                   "Epistle XXXIX instead (lpc_Decision_Log.md, 2026-09-01). Epistles XX-XXI "
                   "('Celerinus to Lucian' / 'Lucian Replies to Celerinus') are directly re-verified "
                   "as this world's own lay-confessor first-person voice, licensed specifically for "
                   "Doc_02 SS6's Article 20 discharge -- two confessors writing to each other, "
                   "neither yet ordained.",
        body="This world's central Cyprian-phase documentary corpus: the Decian persecution and "
             "lapsed crisis, the Felicissimus schism, the Novatianist rival consecration at Rome, "
             "and the rebaptism controversy with Stephen. Licensed for Cyprian's own election "
             "language and for primary-gravity/strand evidence throughout Doc_01.",
    ),
    dict(
        row=2, slug="cyprian-de-lapsis",
        author="Cyprian of Carthage",
        work="On the Lapsed (De Lapsis)",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Not independently re-collated line-by-line this session; its subject matter is "
                   "confirmed throughout Doc_01's own construction rather than through a fresh "
                   "locus-level check here.",
        body="The founding document of the penitential controversy (Doc_01 SS2) and the "
             "lapsed-reconciliation gravity (Doc_01 SS3; Doc_07's G2, Penitential Discipline).",
    ),
    dict(
        row=3, slug="cyprian-de-unitate",
        author="Cyprian of Carthage",
        work="On the Unity of the Church (De Unitate)",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01; read from Doc_01's own finding, not an independent locus check / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Contested",
        divergence="Confidence B rather than A because De Unitate 5 does not carry Cyprian's own "
                   "anti-Stephen position -- the treatise predates the Stephen rebaptism controversy "
                   "by several years (Doc_01 SS7); a finding about what this row is NOT licensed for, "
                   "not an independent locus check. De Unitate 4-5 also survives in two recensions, "
                   "one (the 'Primacy Text') reading more favourably to Roman primacy -- a "
                   "transmission fact Doc_01 SS7 names and does not resolve; Registry row 51 "
                   "(Bévenot's critical edition) is the instrument that would actually close it, not "
                   "yet acquired (in copyright).",
        body="The classic treatise on schism and the one episcopate, written amid the Novatianist and "
             "Felicissimus crises (Doc_01 SS2, SS7) -- general subject-matter only; NOT licensed for "
             "Cyprian's own anti-Stephen position or the conciliar-authority claim, both of which "
             "belong to row 4's own 256 preface.",
    ),
    dict(
        row=4, slug="cyprian-seventh-council-of-carthage",
        author="Cyprian of Carthage and the African episcopate in council",
        work="The Seventh Council of Carthage under Cyprian (on the baptism of heretics, 256; the "
             "vendored edition's own heading dates it a.d. 258)",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. The reciprocal clause 'can no more be judged by another than he "
                    "himself can judge another' is Cyprian's own continuous text, not editorial "
                    "bracketing -- the brackets in the vendored edition at that point belong to a "
                    "separate editorial gloss following the clause, distinguished directly against "
                    "the source.",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01; direct verification against "
                  "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml / 2026-09-01.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="The vendored edition's own heading dates this council a.d. 258; modern "
                   "scholarship and this world's own construction follow 256 throughout, and the "
                   "divergence is disclosed rather than silently resolved -- a third date alongside "
                   "row 42's own npnf214 heading of a.d. 257 for the identical event, on the same "
                   "disclosure standard.",
        body="Cyprian's own conciliar-authority theory in his own first-person-plural words as "
             "presiding bishop -- 'neither does any of us set himself up as a bishop of bishops... "
             "every bishop, according to the allowance of his liberty and power, has his own proper "
             "right of judgment' -- the egalitarian axis of Article 21's conciliar-authority test "
             "(Doc_01 SS4, SS5, SS7; Doc_07's G5). Licensed for this conciliar-authority claim "
             "specifically; row 3 does not carry it.",
    ),
    dict(
        row=5, slug="cyprian-minor-pastoral-treatises",
        author="Cyprian of Carthage",
        work="Minor treatises, grouped: An Address to Demetrianus, Exhortation to Martyrdom (Ad "
             "Fortunatum), On Jealousy and Envy, On Works and Alms, On the Advantage of Patience, On "
             "the Dress of Virgins, On the Lord's Prayer, On the Mortality (De Mortalitate), On the "
             "Vanity of Idols, Three Books of Testimonies Against the Jews (Ad Quirinum)",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed to Cyprian for nine of the ten; On the Vanity of Idols carries the "
                    "corpus map's own confidence: provisional flag, its authenticity questioned "
                    "(it compiles Tertullian and Minucius Felix).",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Not individually re-collated this session beyond what Doc_01 already establishes "
                   "for the plague material. Tertullian dependency, per Doc_01 SS8 item 5's own "
                   "binding: the corpus map's own notes record four of these ten treatises as "
                   "directly reworking or depending on Tertullian (On the Advantage of Patience, On "
                   "the Dress of Virgins, On the Lord's Prayer, On the Vanity of Idols) -- Tertullian "
                   "himself is Excluded as a Named Comparandum (row 29) and is not this world's own "
                   "voice.",
        body="Pastoral discipline, catechetical method, congregational piety, and the Carthage plague "
             "(Doc_01 SS2, SS3, SS6); De Mortalitate specifically for the epidemic gravity and Doc_07's "
             "own emotional-ecology finding (the shepherd 'wailing with the wailing').",
    ),
    dict(
        row=6, slug="pseudo-cyprianic-treatises",
        author="Anonymous, transmitted under Cyprian's own name",
        work="Treatises attributed to Cyprian on questionable authority: On the Public Shows; On the "
             "Glory of Martyrdom; Of the Discipline and Advantage of Chastity; Exhortation to "
             "Repentance",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="pseudo-Cyprianic. Kept under Cyprian's own name per the corpus map's own "
                    "2026-08-26 ruling (transmitted-author shelf, not re-attributed), and filed a "
                    "SECOND time under an apocryphal-and-pseudepigraphal-literature shelf on that same "
                    "ruling's own reasoning -- 'a work circulating under a name that is not its "
                    "author's is a pseudepigraphon by definition.' Two of the four pieces are widely "
                    "attributed to Novatian in modern scholarship, per the corpus map's own note.",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="This row's own double-shelving is disclosed rather than resolved: the same body "
                   "sits under this world's own tradition entry and under a genre-level pseudepigrapha "
                   "category at once, on the corpus map's own recorded reasoning, not this "
                   "compilation's own choice.",
        body="Named for completeness only; not currently licensed for any specific claim this world's "
             "own construction makes.",
    ),
    dict(
        row=7, slug="pontius-life-and-passion-of-cyprian",
        author="Pontius the Deacon",
        work="The Life and Passion of Cyprian, Bishop and Martyr",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01; direct verification against "
                  "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml / 2026-09-01.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Licensed for Cyprian's own election specifically and for Pontius's own presence "
                   "at the Curubis exile; NOT licensed for Cyprian's own conversion generally (SSSS2-4 "
                   "of the Life), which has not been independently checked this session. A full-text "
                   "sweep confirms the Life nowhere states that Cyprian himself ordained Pontius -- a "
                   "claim this record does not make, having checked.",
        body="Cyprian's own election ('by the judgment of God and the favour of the people, he was "
             "chosen to the office of the priesthood and the degree of the episcopate while still a "
             "neophyte') and formation-narrative evidence generally (Doc_02 SS4). Author Gravity risk "
             "named directly: written by a deacon with every personal and institutional reason to "
             "idealize his own bishop, after that bishop's own martyrdom had already begun to be "
             "venerated (Doc_02 SS4).",
    ),
    dict(
        row=8, slug="anonymous-against-novatian-and-on-rebaptism",
        author="Anonymous",
        work="Treatise Against the Heretic Novatian (c. 255) and Treatise on Re-baptism (De "
             "Rebaptismate)",
        edition="Ante-Nicene Fathers vol. V, vendored as "
                "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="anonymous",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently re-collated this session.",
        body="The Novatianist rival consecration (Doc_01 SS4) and the pro-Roman side of the rebaptism "
             "controversy.",
    ),
    dict(
        row=9, slug="augustine-confessions",
        author="Augustine of Hippo",
        work="Confessions",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. I, vendored as "
                "cic/texts/npnf101_augustine-confessions-letters.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Not independently re-collated line-by-line this session beyond the dates Doc_01 "
                   "already establishes. A Latin critical text is now separately vendored and directly "
                   "verified as row 197 (Knöll's CSEL 33), corroborating this translation's own base "
                   "text without re-checking this specific English rendering locus by locus.",
        body="Augustine's own conversion narrative (386-387); the founding first-person document of "
             "this world's own Augustine half (Doc_01 SS2).",
    ),
    dict(
        row=10, slug="augustine-jerome-correspondence",
        author="Augustine of Hippo",
        work="Letters -- the Augustine-Jerome correspondence (17 letters, ~52,892 words)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. I, vendored as "
                "cic/texts/npnf101_augustine-confessions-letters.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed; deliberately double-placed with the Hieronymian world (Doc_01 SS7), "
                    "per Mark's own 2026-08-26 split ruling -- 'the exchange contains Jerome's own "
                    "letters... and Augustine's, which are the Latin pastoral world's.'",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Widely Accepted",
        divergence="A deliberate shared-material double-placement (Doc_01 SS7, Doc_02 SS1) rather "
                   "than a boundary breach: the corpus map assigns this cluster tradition to both "
                   "worlds, since a two-sided correspondence has voice on both sides. Not "
                   "independently re-collated line-by-line this session.",
        body="This world's own side of a two-sided exchange with the Hieronymian world, per Mark's own "
             "split ruling.",
    ),
    dict(
        row=11, slug="augustine-general-correspondence",
        author="Augustine of Hippo",
        work="Letters -- the general correspondence (138 of the vendored volume's own 168 letters, "
             "~258,018 words; the remaining 30 are the Jerome cluster (row 10), an 11-letter Donatist "
             "cluster, and a 2-letter Pelagian cluster, neither of the latter two covered by this "
             "row). Completeness qualifier: this is the vendored 19th-century NPNF selection, not the "
             "full modern corpus -- Divjak's 1975 find added 29 further letters (CSEL 88, 1981; row "
             "49), not represented here",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. I, vendored as "
                "cic/texts/npnf101_augustine-confessions-letters.xml",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/_staging/npnf101_augustine-confessions-letters.yaml / "
                  "2026-09-01; Letters XXXI, CCXIII, CXXVI, CCXI: direct text search and read against "
                  "cic/texts/npnf101_augustine-confessions-letters.xml / 2026-09-01.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Confidence A covers two things: a body-level characterization of all 138 letters "
                   "('ordinary episcopal correspondence... friendship') and four specifically located "
                   "letters (XXXI, CCXIII, CXXVI, CCXI), all four directly re-verified against "
                   "source. The general characterization of the other 134 is NOT independently "
                   "checked -- named as an open question for a future review round rather than "
                   "resolved by this row's own say-so, the same shape of reasoning row 3 already "
                   "carries for its own Confidence B. Letter XXXI SS4 and Letter CCXIII SS4 ground "
                   "Doc_01's own ordination account; Letters CXXVI and CCXI ground Doc_02 SS6's "
                   "Article 20 discharge.",
        body="Ordinary episcopal correspondence -- pastoral advice, administration, consolation, "
             "friendship (Doc_01 SS6, SS7); Letter CXXVI (to Albina, a.d. 411, the Pinianus-ordination "
             "riot) and Letter CCXI (to the Nuns of Hippo, a.d. 423, the monastic revolt), licensed "
             "specifically for Doc_02 SS6's Article 20 discharge.",
    ),
    dict(
        row=12, slug="augustine-correction-of-the-donatists",
        author="Augustine of Hippo",
        work="The Correction of the Donatists (Letter 185, c. 417), addressed to the tribune Boniface",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. IV, vendored as "
                "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01; direct verification against "
                  "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml / 2026-09-01.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Chapter 7 SSSS23-29 directly re-verified, including the council NPNF's own "
                   "editorial footnote dates 401 (not Augustine's own text, which does not date it), "
                   "the Theodosian fine, 'we carried our point... envoys were sent to the court of "
                   "the Count', and SS26's own record that the petition was not granted. The same "
                   "distinction applies to CTh XVI.5.21 (392, the actual fine cited here), the 401 "
                   "council, and CTh XVI.5.52 (412, a different Donatist-specific schedule this row "
                   "does NOT license) -- three different years under different emperors, easily "
                   "collapsed into each other (row 44's own caution).",
        body="The imperial-coercion defence and the two-register argument (pastoral-corrective and "
             "imperial-duty); Doc_01's own central state-power finding (SS4, SS7, SS9). Also assigned "
             "to imperial-juridical-christianity's own corpus map, per that world's own "
             "double-placement.",
    ),
    dict(
        row=13, slug="augustine-on-baptism-against-the-donatists",
        author="Augustine of Hippo",
        work="On Baptism, Against the Donatists (7 books, c. 400)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. IV, vendored as "
                "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01; I.1.2, II.3, III ch.2 SS2, VI ch.2: direct verification against "
                  "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml, Book and Chapter "
                  "loci recomputed programmatically from the vendored markup, across Doc_01's nine "
                  "review rounds / 2026-09-01.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="The Donatist-patrimony claim -- that the Donatists themselves appealed to "
                   "Cyprian's own authority and the 256 council's own judgments for their rebaptism "
                   "doctrine -- rests on Book III ch. 2 SS2's own continuous text, Augustine's own "
                   "words, directly re-verified, corroborated by editorial framing (the NPNF preface's "
                   "own quotation of Retractationes II.18; Books II/VI/VII's own editorial argumenta, "
                   "not Augustine's own first-person words at those specific headings) rather than "
                   "resting on four independently-Augustine loci. This is Augustine's own testimony "
                   "that the Donatists made this appeal, not an independent Donatist-authored source "
                   "making it in their own words.",
        body="The validity of schismatic baptism/ordination; a major conduit for Cyprian's own "
             "conciliar acts, argued through at length (Doc_01 SS5, SS7; Doc_07's G6); and the "
             "Donatist-patrimony claim at Doc_02 SS2's own Transmission History entry for Cyprian.",
    ),
    dict(
        row=14, slug="augustine-answer-to-petilian",
        author="Augustine of Hippo",
        work="Answer to the Letters of Petilian, the Donatist (3 books)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. IV, vendored as "
                "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Native but not drawn on for a specific claim: this world's own material does not "
                   "depend on characterizing the Donatist side of this dispute (Doc_02 SS1); the "
                   "sibling Donatism build's own Registry (its own row 4) directly verifies this same "
                   "work for its own purposes.",
        body="The most extensive surviving Donatist voice preserved inside the vendored corpus, in "
             "Augustine's own refutation -- named here for completeness, drawn on by the sibling "
             "Donatism build rather than by this world's own Doc_01.",
    ),
    dict(
        row=15, slug="augustine-on-the-catechising-of-the-uninstructed",
        author="Augustine of Hippo",
        work="On the Catechising of the Uninstructed",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. III, vendored as "
                "cic/texts/npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Not independently re-collated this session.",
        body="Congregational formation practice -- how to teach beginners (Doc_02 SS1, SS4 below); "
             "written for the Carthaginian deacon Deogratias, 'as near the center of this entry as a "
             "work can sit' per the corpus map's own note.",
    ),
    dict(
        row=16, slug="augustine-on-christian-doctrine",
        author="Augustine of Hippo",
        work="On Christian Doctrine (Books I-IV)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. II, vendored as "
                "cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml; the Latin original "
                "(Bruder's 1838 Maurist-text edition) is separately vendored as row 200",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently re-collated this session. Row 200's own Latin vendoring is NOT "
                   "a modern critical edition (CSEL 80 is, and is confirmed in copyright) -- disclosed "
                   "there rather than treated as equivalent.",
        body="Augustine's manual for interpreters and preachers of Scripture; Book IV on Christian "
             "eloquence -- congregational teaching practice (Doc_02 SS1).",
    ),
    dict(
        row=17, slug="augustine-the-enchiridion",
        author="Augustine of Hippo",
        work="The Enchiridion (On Faith, Hope, and Love)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. III, vendored as "
                "cic/texts/npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml; the Latin "
                "original (Bruder's 1838 Maurist-text edition) is separately vendored as row 200",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Not independently re-collated this session.",
        body="Handbook of the faith for the layman Laurentius -- catechetical-pastoral by design "
             "(Doc_02 SS1).",
    ),
    dict(
        row=18, slug="augustine-creedal-catechetical-works",
        author="Augustine of Hippo",
        work="A Treatise on Faith and the Creed, On the Creed: A Sermon to Catechumens, Concerning "
             "Faith of Things Not Seen",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. III, vendored as "
                "cic/texts/npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Not independently re-collated this session for all three works.",
        body="Creedal/catechetical instruction preached to catechumens and North African bishops "
             "(Doc_02 SS1); the baptismal-validity liturgical-evidence category Doc_02 SS5 and SS9 "
             "item 9 name.",
    ),
    dict(
        row=19, slug="augustine-sermons-on-selected-lessons",
        author="Augustine of Hippo",
        work="Sermons on Selected Lessons of the New Testament (~97 sermons, ~308,000 words). "
             "Completeness qualifier: this is the vendored 19th-century NPNF sermon body, not the "
             "full modern corpus -- the 1990 Dolbeau/Mainz find added 26 further sermons (published "
             "1996; row 50), not represented here",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. VI, vendored as "
                "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Assigned as one body per the granularity rule; not independently re-collated "
                   "line-by-line this session. Sermon 299/D, a possible further primary-source "
                   "candidate on the pre-boundary Scillitan Martyrs (row 171), is independently checked "
                   "and confirmed ABSENT from this vendored file -- zero hits for '299' or 'CCXCIX' -- "
                   "and from the corpus map; row 189 (Morin's 1930 critical edition) names where the "
                   "primary text would have to come from if this world's construction ever needs it.",
        body="The defining material of this world's own pastoral-congregational entry -- sermons "
             "preached to Augustine's own congregations at Hippo and Carthage (Doc_02 SS1).",
    ),
    dict(
        row=20, slug="augustine-expositions-on-the-psalms",
        author="Augustine of Hippo",
        work="Expositions on the Book of Psalms (Enarrationes in Psalmos) (~695,000 words)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. VIII, vendored as "
                "cic/texts/npnf108_augustine-exposition-psalms.xml; the Latin original (Migne's 1861 "
                "printing of the Maurist text) is separately vendored as row 201",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Not independently re-collated this session; anti-Donatist polemic surfaces "
                   "diffusely per the corpus map's own note, no separate id claimed. This is this "
                   "world's own largest single vendored body, and row 175 (Fiedrowicz) is the only "
                   "dedicated secondary study named for it, itself not vendored.",
        body="Ordinary preached and dictated congregational exposition, 392-420, at Hippo and Carthage "
             "(Doc_02 SS1).",
    ),
    dict(
        row=21, slug="augustine-tractates-on-john-and-related-exegesis",
        author="Augustine of Hippo",
        work="Tractates on the Gospel of John (124 tractates, ~412,000 words), Ten Homilies on the "
             "First Epistle of John, Our Lord's Sermon on the Mount, The Harmony of the Gospels",
        edition="Nicene and Post-Nicene Fathers, Series I, vols. VI and VII, vendored as "
                "cic/texts/npnf106_augustine-sermon-mount-harmony-gospels-homilies.xml and "
                "cic/texts/npnf107_augustine-homilies-john-soliloquies.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Not independently re-collated this session across the four grouped works.",
        body="Congregational exegetical preaching at Hippo, c. 391-420s (Doc_02 SS1).",
    ),
    dict(
        row=22, slug="augustine-anti-manichaean-corpus",
        author="Augustine of Hippo",
        work="Anti-Manichaean corpus, grouped: Acts... Against Fortunatus, Against the Epistle of "
             "Manichaeus, Concerning the Nature of Good, On Two Souls, On the Morals of the Catholic "
             "Church / of the Manichaeans, On the Profit of Believing, Reply to Faustus the "
             "Manichaean",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. IV, vendored as "
                "cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Double-assigned to manichaeism for several works, per the corpus map's own note; "
                   "not independently re-collated this session.",
        body="Augustine's own nine years as a Manichaean auditor before conversion; the "
             "'refusing a purity/sufficiency test' gravity candidate (Doc_01 SS6; Doc_07's G7, Grace "
             "and Human Incapacity).",
    ),
    dict(
        row=23, slug="augustine-anti-pelagian-corpus",
        author="Augustine of Hippo",
        work="Anti-Pelagian corpus, thirteen works, c. 412-429: On the Merits and Forgiveness of Sins, "
             "On the Spirit and the Letter, On Nature and Grace, On the Proceedings of Pelagius, On "
             "Man's Perfection in Righteousness, On the Grace of Christ and on Original Sin, On "
             "Marriage and Concupiscence, On the Soul and its Origin, On Grace and Free Will, On "
             "Rebuke and Grace, On the Predestination of the Saints, On the Gift of Perseverance, and "
             "Against Two Letters of the Pelagians",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. V, vendored as "
                "cic/texts/npnf105_augustine-anti-pelagian-writings.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed for twelve of the thirteen; the thirteenth, On the Soul and its "
                    "Origin, carries the corpus map's own confidence: provisional flag -- 'Not "
                    "addressed to Pelagians... the doubt is whether the pelagianism id should stand; "
                    "latin-pastoral-congregational-christianity is not in doubt,' a doubt this row "
                    "carries rather than rounds away.",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Not independently re-collated this session across the thirteen grouped works; "
                   "double-assigned to pelagianism for twelve of them.",
        body="The Pelagian controversy, 410s-420s (Doc_01 SS2); grace/sufficiency-test gravity "
             "candidate (Doc_07's G7 -- the densest textual object in this world's own vocabulary, "
             "1,798 raw occurrences across these thirteen works per Doc_03).",
    ),
    dict(
        row=24, slug="augustine-city-of-god",
        author="Augustine of Hippo",
        work="City of God (Books I-XXII)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. II, vendored as "
                "cic/texts/npnf102_augustine-city-of-god-christian-doctrine.xml; the Latin original "
                "(Hoffmann's CSEL 40) is separately vendored as rows 198-199",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently re-collated this session; not double-assigned to any other "
                   "world per the corpus map's own note (Mark's own ruling).",
        body="Written at Hippo, 413-427, occasioned by the sack of Rome (410) -- Augustine's own "
             "largest work.",
    ),
    dict(
        row=25, slug="augustine-further-doctrinal-and-moral-treatises",
        author="Augustine of Hippo",
        work="On the Holy Trinity and other doctrinal/moral treatises not already grouped above: Of "
             "Holy Virginity, On Continence, On the Good of Marriage, On the Good of Widowhood, On "
             "Care to Be Had for the Dead, On Patience, On Lying / Against Lying, Of the Work of "
             "Monks, On Nature and Grace, Soliloquies -- disposition note: On Nature and Grace stands "
             "in this row's own title list but is licensed and independently checked only at row 23, "
             "not at this row",
        edition="Nicene and Post-Nicene Fathers, Series I, vols. III and VII, vendored as "
                "cic/texts/npnf103_augustine-holy-trinity-doctrinal-moral-treatises.xml and "
                "cic/texts/npnf107_augustine-homilies-john-soliloquies.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed, several double-assigned elsewhere per their own corpus-map notes, "
                    "except Soliloquies, confidence: provisional in the corpus map's own record -- 'a "
                    "philosophical dialogue, not pastoral work from Hippo... the doubt worth a "
                    "reviewer's eye is whether the Cassiciacum period should also touch "
                    "ambrosian-milan-standalone... not asserted here.'",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Soliloquies was written 386-387 at Cassiciacum near Milan -- before Augustine's "
                   "baptism, his return to Africa, and outside Doc_01's own stated geography -- yet "
                   "reaches this world's own construction record only through his corpus. Held Native "
                   "but flagged, on the same 'held for want of a better home' basis the corpus map "
                   "itself states, rather than resolving the question the corpus map leaves open.",
        body="Of the Work of Monks specifically for North African monastic life inside this entry "
             "(Doc_01 SS6); On Nature and Grace is NOT licensed here (see row 23). Not otherwise "
             "currently licensed for a specific claim.",
    ),
    dict(
        row=26, slug="code-of-canons-of-the-african-church-419",
        author="The Council of Carthage (419) and the African episcopate under Aurelius and "
               "Augustine",
        work="The Code of Canons of the African Church (Council of Carthage, 419)",
        edition="Nicene and Post-Nicene Fathers, Series II, vol. XIV, vendored as "
                "cic/texts/npnf214_seven-ecumenical-councils.xml; the Latin original (Bruns's 1839 "
                "edition) is separately vendored as row 202",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="documentary; attributed to the conciliar body",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Not independently re-collated this session; the Apiarius affair's own duration "
                   "(419, running to c. 426) is directly re-verified in Doc_01's own construction "
                   "against secondary characterization, not against this primary text directly.",
        body="The institutional skeleton of this world's own conciliar life (Doc_01 SS2, on the "
             "Apiarius affair) -- a jurisdictional dispute Doc_01 SS2 names rather than smooths "
             "(Doc_07 SS2E).",
    ),
    dict(
        row=71, slug="dekkers-fraipont-enarrationes-in-psalmos-ccsl",
        author="E. Dekkers and J. Fraipont (editors); Augustine of Hippo (author)",
        work="Enarrationes in Psalmos, CCSL 38-40 (Turnhout: Brepols, 1956)",
        edition="Brepols, 1956 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate. A Latin original is separately vendored, but from a "
                "different, pre-critical edition (Migne's 1861 printing, row 201, not this one).",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to the editors, Augustine as author",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked against a specific volume or locus.",
        body="Licensed for row 20 -- the critical edition of the ~695,000-word Psalm-exposition body, "
             "the largest single thing in the vendored corpus, with no edition of any kind previously "
             "named.",
    ),
    dict(
        row=72, slug="oeuvres-de-saint-augustin-traites-anti-donatistes-ba",
        author="G. Finaert (translator)",
        work="Œuvres de saint Augustin, 4e série: Traités anti-donatistes, Bibliothèque "
             "Augustinienne 28-32 (Bruges: Desclée de Brouwer, 1963-68)",
        edition="Desclée de Brouwer, 1963-68 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Finaert as translator",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Licensed for rows 12-13, an alternative critical French edition and translation of this "
             "world's central anti-Donatist works.",
    ),
    dict(
        row=73, slug="works-of-saint-augustine-21st-century",
        author="J. E. Rotelle / B. Ramsey (editors); R. Teske and E. Hill (translators)",
        work="The Works of Saint Augustine: A Translation for the 21st Century (New York: New City "
             "Press, 1990- ), esp. Letters II/1-II/4 (incl. Divjak 1*-29*) and Sermons III/1-III/11 "
             "(incl. the Dolbeau sermons)",
        edition="New City Press, 1990- -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to the editors and translators named",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="The accessible modern translation of the Divjak letters and Dolbeau sermons rows 49-50 "
             "name as completeness qualifiers on rows 11 and 19.",
    ),
    dict(
        row=74, slug="lepelley-les-cites-de-lafrique-romaine",
        author="Claude Lepelley",
        work="Les cités de l'Afrique romaine au Bas-Empire, 2 vols. (Paris: Études Augustiniennes, "
             "1979, 1981)",
        edition="Études Augustiniennes, 1979/1981 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- the standard study of North African "
             "civic life in this world's own period.",
    ),
    dict(
        row=75, slug="perler-maier-les-voyages-de-saint-augustin",
        author="Othmar Perler (with J.-L. Maier)",
        work="Les voyages de saint Augustin, Études Augustiniennes 36 (Paris, 1969)",
        edition="Études Augustiniennes, 1969 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- Augustine's own itinerary and "
             "chronology.",
    ),
    dict(
        row=76, slug="la-bonnardiere-recherches-de-chronologie-augustinienne",
        author="Anne-Marie La Bonnardière",
        work="Recherches de chronologie augustinienne (Paris: Études Augustiniennes, 1965)",
        edition="Études Augustiniennes, 1965 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Licensed for row 62's own provenance note -- the documentation Mandouze's "
             "Prosopographie (row 62) was compiled in part from.",
    ),
    dict(
        row=77, slug="dunn-cyprian-and-the-bishops-of-rome",
        author="Geoffrey D. Dunn",
        work="Cyprian and the Bishops of Rome: Questions of Papal Primacy in the Early Church, Early "
             "Christian Studies 11 (Strathfield: St Pauls, 2007)",
        edition="St Pauls, 2007 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. The first of four distinct Dunn works this Registry "
                   "names (rows 112, 157, 173 are the others), each on a different specific question.",
        body="Not currently licensed for a specific claim -- Cyprian's own relationship to Rome, "
             "adjacent to the rebaptism controversy.",
    ),
    dict(
        row=78, slug="knoll-augustine-retractationum-csel36",
        author="Pius Knöll (editor); Augustine of Hippo (author)",
        work="Augustine, Retractationum libri duo, CSEL 36 (Vienna: F. Tempsky / Leipzig: G. "
             "Freytag, 1902)",
        edition="Now vendored, row 209 (2026-09-08), closing Manifest G6; vendored as "
                "cic/texts/augustine_retractationes-lat_knoll-csel36.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02; resolved by G6's own fulfillment / 2026-09-08.",
        cite="C", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="No prior session, across multiple search rounds, had located this identifier -- "
                   "disclosed rather than filled with an invented placeholder. Public domain (1902); "
                   "located by opening Getty-hosted CSEL-Augustine volumes directly by number, since "
                   "their own archive.org metadata carries no per-volume title/editor/year.",
        body="Licensed for the Retractationes II.18 citation row 13 holds only at second hand -- the "
             "CSEL critical edition of the work quoted by NPNF's own editor at row 13's own preface "
             "locus; public domain, unlike row 67's own Mutzenbecher (CCSL 57, in copyright).",
    ),
    dict(
        row=79, slug="harmless-augustine-and-the-catechumenate",
        author="William Harmless",
        work="Augustine and the Catechumenate (Collegeville: Liturgical Press, 1995; rev. ed. 2014)",
        edition="Liturgical Press, 1995/2014 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Licensed for the liturgical-evidence gap Doc_02 SS5 and SS9 item 9 name, and rows 15, "
             "17-18.",
    ),
    dict(
        row=80, slug="lawless-augustine-of-hippo-and-his-monastic-rule",
        author="George Lawless",
        work="Augustine of Hippo and his Monastic Rule (Oxford: Clarendon Press, 1987)",
        edition="Clarendon Press, 1987 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked. Prints the Praeceptum, the Ordo Monasterii, and Letter "
                   "CCXI itself.",
        body="Licensed for the textual question Doc_02 SS6 names for Letter CCXI and the Augustinian "
             "Rule.",
    ),
    dict(
        row=81, slug="rebillard-christians-and-their-many-identities",
        author="Éric Rebillard",
        work="Christians and Their Many Identities in Late Antiquity, North Africa, 200-450 CE "
             "(Ithaca: Cornell University Press, 2012)",
        edition="Cornell University Press, 2012 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="By the same author as row 35, a different book -- checked and kept distinct.",
        body="Licensed for the Article 20 ordinary-believer gap Doc_02 SS6 names.",
    ),
    dict(
        row=82, slug="ennabli-carthage-une-metropole-chretienne",
        author="Liliane Ennabli",
        work="Carthage: une métropole chrétienne du IVe à la fin du VIIe siècle, Études "
             "d'Antiquités africaines, pref. André Mandouze (Paris: CNRS Éditions, 1997)",
        edition="CNRS Éditions, 1997 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed, prefaced by the author of row 62 (Mandouze)",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked. Row 188 (Laporte, 2015) later challenges row 63's own "
                   "Hippo identification; no comparable challenge is named against this row's own "
                   "Carthage material.",
        body="Licensed for row 38, alongside row 63 -- row 63 (Marec) closes the excavation gap for "
             "Hippo Regius; Ennabli is the Carthage counterpart.",
    ),
    dict(
        row=83, slug="uhalde-expectations-of-justice",
        author="Kevin Uhalde",
        work="Expectations of Justice in the Age of Augustine (Philadelphia: University of "
             "Pennsylvania Press, 2007)",
        edition="University of Pennsylvania Press, 2007 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- the audientia episcopalis and penance, "
             "this world's own pastoral-congregational subject.",
    ),
    dict(
        row=84, slug="harrison-the-art-of-listening-in-the-early-church",
        author="Carol Harrison",
        work="The Art of Listening in the Early Church (Oxford: Oxford University Press, 2013)",
        edition="Oxford University Press, 2013 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Licensed for rows 19-21 and the liturgical-evidence gap -- preaching, catechesis, and "
             "prayer as heard by a congregation.",
    ),
    dict(
        row=85, slug="vetus-latina-beuron",
        author="Erzabtei Beuron (editors)",
        work="Vetus Latina: Die Reste der altlateinischen Bibel (Freiburg: Herder, 1949- )",
        edition="Herder, 1949- -- in copyright (ongoing series), never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to the Beuron Vetus Latina Institute",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked; an ongoing series with no single completion date.",
        body="Licensed for rows 5 and 34 -- the Old Latin biblical text both anchor figures quote "
             "from, rather than the Vulgate.",
    ),
    dict(
        row=86, slug="dodaro-christ-and-the-just-society",
        author="Robert Dodaro",
        work="Christ and the Just Society in the Thought of Augustine (Cambridge: Cambridge "
             "University Press, 2004)",
        edition="Cambridge University Press, 2004 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Native, unlicensed: no era/place/tradition mismatch against Doc_01 exists, so "
                   "'Out-of-Boundary' does not apply; carries no Licensed-For target on the same "
                   "footing as row 70 (Markus), for the same reason -- Augustine's own political "
                   "theology and ethics, topically narrow rather than boundary-mismatched.",
        body="Not currently licensed for any specific claim -- Augustine's own political theology and "
             "ethics, the same topical ground row 70 (Markus) sits on.",
    ),
    dict(
        row=87, slug="chadwick-augustine-of-hippo-a-life",
        author="Henry Chadwick",
        work="Augustine of Hippo: A Life (Oxford: Oxford University Press, 2009)",
        edition="Oxford University Press, 2009 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Native, unlicensed: redundancy with an already-held Native source (rows 30, 31) "
                   "is not a Boundary Check failure under the Template (no era/place/tradition "
                   "mismatch against Doc_01 exists); the Template has no Exclusion Reason for "
                   "'redundant,' and a Native row with nothing currently licensed, per row 6's own "
                   "pattern, is the correct fit.",
        body="A short biography, redundant with rows 30 (Brown) and 31 (Lancel), both already Native "
             "and already the standard biographical framing this Registry relies on.",
    ),
    dict(
        row=88, slug="codex-theodosianus-latin-library-transcription",
        author="Unattributed transcribers, The Latin Library",
        work="Codex Theodosianus (Imperatori Theodosiani Codex), full text (all 16 books), as "
             "transcribed at The Latin Library (thelatinlibrary.com/theodosius.html)",
        edition="Vendored as cic/texts/codex-theodosianus_latinlibrary.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="documentary (Roman imperial legislation); the transcription's own critical-"
                    "edition ancestry is unstated -- The Latin Library does not say which edition its "
                    "transcription follows, and its own site policy disclaims its texts as 'not "
                    "intended for research purposes nor as substitutes for critical editions.'",
        discovery="Project lead direct supply (downloaded book by book and compiled into one "
                  "document) / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Public domain on The Latin Library's own site-wide declaration, a genuinely "
                   "different rights basis from row 44's Oxford Text Archive file (CC BY-NC-SA, not "
                   "vendorable) -- the reason this exists as a second entry rather than a note on row "
                   "44. The embedded cross-references to the Breviary of Alaric suggest descent from "
                   "an edition using Mommsen's own numbering, but this is NOT independently confirmed "
                   "line-by-line against row 44's own file. Row 44 remains the higher-confidence "
                   "source for exact wording; this row the one actually committed to cic/texts/.",
        body="The same imperial-statute background row 44 licenses -- not currently drawn on directly "
             "for a specific claim.",
    ),
    dict(
        row=89, slug="von-soden-die-cyprianische-briefsammlung",
        author="Hans von Soden",
        work="Die cyprianische Briefsammlung: Geschichte ihrer Entstehung und Überlieferung, Texte "
             "und Untersuchungen 25.3 (Leipzig: J. C. Hinrichs, 1904)",
        edition="Now vendored, row 210 (2026-09-08), closing Manifest G7; vendored as "
                "cic/texts/vonsoden_cyprianische-briefsammlung-deu_1904.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02; resolved by G7's own fulfillment / 2026-09-08.",
        cite="C", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Public domain (1904), title page, Vorwort, and closing colophon directly "
                   "verified. Flagged for priority second-opinion review before it supports any "
                   "specific claim. The same problem this monograph studies is what produced this "
                   "build's own historical Ep. XL/Epistle XXXIX citation error -- this source would "
                   "have let a reviewer catch that error at its own root rather than nine Doc_01 "
                   "review rounds in.",
        body="Licensed for the letter-ordering and attribution questions row 1 carries open -- the "
             "corpus's own embedding of letters by others under Cyprian's own name, and the "
             "multiple-numbering confusion row 46 answers only by hand.",
    ),
    dict(
        row=90, slug="von-soden-prosopographie-des-afrikanischen-episkopats",
        author="Hans von Soden",
        work="Die Prosopographie des afrikanischen Episkopats zur Zeit Cyprians, Quellen und "
             "Forschungen aus italienischen Archiven und Bibliotheken 12 (Rome, 1909), pp. 247-270",
        edition="Now vendored, row 211 (2026-09-08), closing Manifest G8; vendored as "
                "cic/texts/vonsoden_prosopographie-afrikanischer-episkopat-deu_1909.txt, sliced to "
                "the article's own page range",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02; resolved by G8's own fulfillment / 2026-09-08.",
        cite="C", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Public domain (1909); the article's own heading and closing paragraph directly "
                   "verified. Flagged for priority second-opinion review before it supports any "
                   "specific claim. The same public-domain volume also carries an unrequested, "
                   "related von Soden article on the rebaptism controversy, named for a future round "
                   "rather than vendored outside this row's own scope.",
        body="Licensed for the person-identification gap row 62 (Mandouze) cannot reach -- Mandouze's "
             "own range begins at 303, forty-five years after Cyprian's death, covering none of the "
             "eighty-seven bishops rows 4 and 42 turn on.",
    ),
    dict(
        row=91, slug="saxer-vie-liturgique-et-quotidienne-a-carthage",
        author="Victor Saxer",
        work="Vie liturgique et quotidienne à Carthage vers le milieu du IIIe siècle: le témoignage "
             "de saint Cyprien et de ses contemporains d'Afrique, Studi di antichità cristiana 29 "
             "(Vatican City: Pontificio Istituto di Archeologia Cristiana, 1969; 2nd ed. 1984)",
        edition="Pontificio Istituto di Archeologia Cristiana, 1969/1984 -- in copyright, never "
                "vendored (Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="454 pages reconstructing Carthage's own liturgical and daily life directly from "
                   "Cyprian's own letters and treatises -- the reading Doc_02 SS5 says nobody has yet "
                   "given rows 1-5. Flagged for priority second-opinion review before it supports any "
                   "specific claim.",
        body="Licensed for the liturgical-evidence category at Doc_02 SS5 and SS9 item 9, and rows 4, "
             "5, and 13 -- the Cyprian-phase counterpart to row 79 (Harmless, Augustine's "
             "catechumenate).",
    ),
    dict(
        row=92, slug="verbraken-etudes-critiques-sermons-authentiques",
        author="Pierre-Patrick Verbraken",
        work="Études critiques sur les sermons authentiques de saint Augustin, Instrumenta "
             "Patristica 12 (Steenbrugge: Sint-Pietersabdij / The Hague: Nijhoff, 1976)",
        edition="Sint-Pietersabdij / Nijhoff, 1976 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- the standard critical inventory of which "
             "sermons in row 19's body are authentic, an instrument this Registry holds in no form.",
    ),
    dict(
        row=93, slug="drobner-augustinus-von-hippo-sermones-ad-populum",
        author="Hubertus R. Drobner",
        work="Augustinus von Hippo: Sermones ad populum. Überlieferung und Bestand, Bibliographie, "
             "Indices, Supplements to Vigiliae Christianae 49 (Leiden: Brill, 2000)",
        edition="Brill, 2000 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- the standard transmission-and-"
             "bibliography handbook for row 19's corpus, complementing row 92.",
    ),
    dict(
        row=94, slug="dossey-peasant-and-empire-in-christian-north-africa",
        author="Leslie Dossey",
        work="Peasant and Empire in Christian North Africa, Transformation of the Classical Heritage "
             "47 (Berkeley: University of California Press, 2010)",
        edition="University of California Press, 2010 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for the Punic/Berber-substrate and ordinary-believer gaps at Doc_02 SS5, SS6, "
             "and SS9 -- the one open question this document set has carried unmoved since Doc_01.",
    ),
    dict(
        row=95, slug="hamman-la-vie-quotidienne-en-afrique-du-nord",
        author="Adalbert-G. Hamman",
        work="La vie quotidienne en Afrique du Nord au temps de saint Augustin (Paris: Hachette, "
             "1979)",
        edition="Hachette, 1979 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- daily life in North Africa in Augustine's "
             "own period, serving Doc_02 SS5's social-historical bullet.",
    ),
    dict(
        row=96, slug="courcelle-recherches-sur-les-confessions",
        author="Pierre Courcelle",
        work="Recherches sur les Confessions de saint Augustin (Paris: E. de Boccard, 1950; 2nd ed. "
             "1968)",
        edition="E. de Boccard, 1950/1968 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Builder's own call: rowed Native rather than excluded. Row 9 (the Confessions) is "
                   "this world's own primary text, and Courcelle is a standard study of it, on the "
                   "same footing as row 53 (O'Donnell's own modern commentary) -- not of Augustine's "
                   "political theology generally, the topical ground rows 70 and 86 are "
                   "Native-but-unlicensed on.",
        body="Not currently licensed for a specific claim -- the standard critical study of the "
             "Confessions' (row 9) own literary sources and Milan-period philosophical background, "
             "alongside row 53's modern commentary.",
    ),
    dict(
        row=97, slug="jensen-living-water",
        author="Robin M. Jensen",
        work="Living Water: Images, Symbols, and Settings of Early Christian Baptism, Supplements to "
             "Vigiliae Christianae 105 (Leiden: Brill, 2011)",
        edition="Brill, 2011 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for the baptismal-validity liturgical-evidence gap Doc_02 SS5 and SS9 item 9 "
             "name, alongside row 79 (Augustine's catechumenate) and row 91 (Saxer, Cyprian-phase) -- "
             "baptismal rites, material settings, and symbolism specifically, on the rite whose valid "
             "administration is one of this world's two anchor controversies (rows 4, 13).",
    ),
    dict(
        row=53, slug="odonnell-augustine-confessions-critical-commentary",
        author="James J. O'Donnell (editor)",
        work="Augustine: Confessions, 3 vols. (Oxford: Clarendon Press, 1992)",
        edition="Clarendon Press, 1992 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to O'Donnell as editor",
        discovery="WebSearch this session (publisher and journal-review records, Church History) / "
                  "2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="The standard modern critical commentary on the Confessions (row 9), volume I a revised "
             "Latin text and introduction, volumes II-III a line-by-line commentary.",
    ),
    dict(
        row=54, slug="brent-cyprian-and-roman-carthage",
        author="Allen Brent",
        work="Cyprian and Roman Carthage (Cambridge: Cambridge University Press, 2010)",
        edition="Cambridge University Press, 2010 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session (publisher, ISBN, and review records, Bryn Mawr Classical "
                  "Review, Journal of Roman Studies) / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="A modern monograph on Cyprian's own intellectual and political context in mid-third-"
             "century Carthage, directly on this world's own Cyprian-phase subject matter.",
    ),
    dict(
        row=55, slug="sage-cyprian",
        author="Michael M. Sage",
        work="Cyprian, Patristic Monograph Series 1 (Cambridge, MA: The Philadelphia Patristic "
             "Foundation, 1975)",
        edition="The Philadelphia Patristic Foundation, 1975 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session (journal-review records, Classical Review, Church History) "
                  "/ 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Two journal notices disagree on the place of publication, disclosed rather than "
                   "silently picked: 'Cambridge, Mass.' (Classical Review) versus 'Philadelphia' "
                   "(Church History), both naming the same publisher. Flagged for priority second-"
                   "opinion review before it supports any specific claim.",
        body="An older but standard full-length modern biography of Cyprian, alongside Burns's own "
             "more recent one (row 32).",
    ),
    dict(
        row=56, slug="monceaux-histoire-litteraire-afrique-chretienne-standing-reference",
        author="Paul Monceaux",
        work="Histoire littéraire de l'Afrique chrétienne depuis les origines jusqu'à l'invasion "
             "arabe, 7 vols. (Paris: E. Leroux, 1901-1923): I. Tertullien et les origines; II. Saint "
             "Cyprien et son temps; III. Le IVe siècle, d'Arnobe à Victorin; IV. Le Donatisme; V. "
             "Saint Optat et les premiers écrivains donatistes; VI. La littérature donatiste au temps "
             "de saint Augustin; VII. Saint Augustin et le donatisme (1923)",
        edition="Vols. I-III now vendored, rows 206-208 (2026-09-08), closing Manifest G5 in full; "
                "vols. IV-VI already vendored in the shared corpus under the sibling Donatism build's "
                "own former G6; vol. VII not requested by either world.",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="WebSearch this session / 2026-09-01; extent/rights re-verified / 2026-09-02.",
        cite="B", verif="verified-via-authority", weight="illustrative", formation="Widely Accepted",
        divergence="Raised from C to B this revision: public domain status resolved rather than "
                   "hedged -- Monceaux died in 1941, but vols. I-III (1901-05) are public domain on "
                   "their own imprint dates alone, independent of the author's death date. Cyprian "
                   "falls within vols. I-III (vol. II, Saint Cyprien et son temps); Augustine is the "
                   "subject of vol. VII (1923), not cited here, since only vols. I-III were "
                   "independently checked this revision. Not licensed for a specific claim.",
        body="The older, foundational literary history of African Christianity.",
    ),
    dict(
        row=57, slug="dekkers-gaar-clavis-patrum-latinorum",
        author="Eligius Dekkers and Aemilius Gaar (editors)",
        work="Clavis Patrum Latinorum, editio tertia aucta et emendata (Turnhout: Brepols; "
             "Steenbrugge: Sint-Pietersabdij, 1995)",
        edition="Brepols, 1995 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session (Brepols's own series record and library catalogues) / "
                  "2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="This Registry's own first genuine Type L entry (Period Lexicon, per the "
                   "Template's own definition -- a Latin-keyed catalogue of the very corpus this "
                   "world draws on). Flagged for priority second-opinion review before it supports "
                   "any specific claim.",
        body="The standard reference instrument for identifying and dating the transmitted Latin "
             "patristic corpus, including the pseudo-Cyprianic body row 6 currently resolves by hand "
             "from the corpus map's own note alone.",
    ),
    dict(
        row=58, slug="ccsl3-sancti-cypriani-episcopi-opera",
        author="R. Weber, M. Bévenot, M. Simonetti, C. Moreschini, G. F. Diercks (editors); Cyprian "
               "of Carthage (author)",
        work="Sancti Cypriani episcopi opera, Corpus Christianorum Series Latina (CCSL) 3 (1972), 3A "
             "(1976), 3B-3D Epistulae (1994-1999), with further parts continuing since (Turnhout: "
             "Brepols)",
        edition="Brepols, 1972-1999+ -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to the successive editors, Cyprian as author",
        discovery="WebSearch this session (Brepols's own series record and journal citations) / "
                  "2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Naming this edition does not itself close row 3's own open two-recension "
                   "question, which requires reading this edition's own apparatus. 'CCSL' and "
                   "'Corpus Christianorum' appeared nowhere in this world's build before this row -- "
                   "the sharpest single gap this round found. Flagged for priority second-opinion "
                   "review before it supports any specific claim.",
        body="The current critical edition of the entire Cyprianic corpus, licensed for the "
             "edition-level and recension questions rows 1, 2, 3, and 39 currently carry open.",
    ),
    dict(
        row=59, slug="munier-concilia-africae",
        author="Charles Munier (editor)",
        work="Concilia Africae a. 345 - a. 525, CCSL 149 (Turnhout: Brepols, 1974)",
        edition="Brepols, 1974 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Munier as editor",
        discovery="WebSearch this session (Brepols's own series record) / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim. "
                   "No earlier, public-domain printing of the African conciliar corpus has been "
                   "named or ruled out for this row -- disclosed as an open lead rather than acted on "
                   "(row 65's own Verification Note).",
        body="Licensed for row 26's own Apiarius-affair claim -- row 26 concedes its own duration "
             "claim rests on secondary characterization rather than this primary text directly; "
             "Munier is the critical edition of the whole African conciliar corpus that would let "
             "row 26 be checked at all.",
    ),
    dict(
        row=60, slug="duval-loca-sanctorum-africae",
        author="Yvette Duval",
        work="Loca sanctorum Africae: le culte des martyrs en Afrique du IVe au VIIe siècle, 2 vols., "
             "Collection de l'École française de Rome 58 (Rome: École française de Rome, 1982)",
        edition="École française de Rome, 1982 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session (library catalogue and journal-review records) / "
                  "2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="This row is disclosed as physically sitting out of numeric order in the table, "
                   "between rows 193 and 60's own numeric neighbors -- a deliberate, disclosed "
                   "placement, not an error. Flagged for priority second-opinion review before it "
                   "supports any specific claim. A different Duval from row 129/146 (Noël Duval) and "
                   "row 170 (Yves-Marie Duval), each independently checked and unrelated.",
        body="Licensed for rows 37 and 38 -- this Registry's entire material-evidence layer (CIL VIII, "
             "no inscription named; basilica archaeology, Confidence D, 'only the category' named); "
             "Duval is the standard corpus of African martyr-cult inscriptions with archaeological "
             "context, the instrument that would turn row 38 from a category into evidence.",
    ),
    dict(
        row=61, slug="goldbacher-augustine-epistulae-standing-reference",
        author="Alois Goldbacher (editor); Augustine of Hippo (author)",
        work="S. Aureli Augustini Hipponiensis episcopi Epistulae, CSEL 34/1 (1895), 34/2 (1898), 44 "
             "(1904), 57 (1911), 58 (1923) (Vindobonae: F. Tempsky)",
        edition="Pars I-IV all now vendored (rows 193, 195, 196, 2026-09-08); only Pars V (CSEL 58, "
                "praefatio and indices, no letter text of its own) remains unacquired -- this row is "
                "kept as the standing reference for the full five-part edition; rows 193, 195, and "
                "196 carry the actually-committed files.",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="WebSearch this session (Internet Archive holdings and the CSEL series record) / "
                  "2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="load-bearing", formation="Widely Accepted",
        divergence="The sharpest bibliography gap this Registry names at the time it was drafted: 51 "
                   "of 73 census works at the time rested on a 19th-century English translation with "
                   "no critical edition named beneath it. Would also settle the letter-numbering "
                   "confusion row 46 (Clarke) was rowed to answer only by hand -- the same class of "
                   "confusion that produced the Ep. XL/Epistle XXXIX error this build spent two rounds "
                   "propagating and correcting.",
        body="The critical Latin edition of the general correspondence and the Jerome and Donatist-"
             "cluster letters, two of those rows at Confidence A resting on a 19th-century English "
             "translation with no critical edition named beneath it.",
    ),
    dict(
        row=62, slug="mandouze-prosopographie-de-lafrique-chretienne",
        author="André Mandouze",
        work="Prosopographie chrétienne du Bas-Empire, I: Prosopographie de l'Afrique chrétienne "
             "(303-533) (Paris: Éditions du Centre National de la Recherche Scientifique, 1982), "
             "1323 pp.",
        edition="CNRS, 1982 -- consultation-only, never vendored (Source_Acquisition_Manifest.md "
                "SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session (Journal of Ecclesiastical History review, CNRS Éditions "
                  "series record) / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Mandouze's own range begins in 303, forty-five years after Cyprian's death, "
                   "covering none of the eighty-seven bishops rows 4 and 42 turn on -- a gap row 90 "
                   "(von Soden) partly closes instead. Flagged for priority second-opinion review "
                   "before it supports any specific claim.",
        body="Licensed for person-identification and dating across rows 1, 11, 12, 26, 42, and 45 -- "
             "this world's own construction repeatedly turns on identifying named individuals with no "
             "prosopographical instrument behind any of it.",
    ),
    dict(
        row=63, slug="marec-monuments-chretiens-dhippone",
        author="Erwan Marec",
        work="Monuments chrétiens d'Hippone, ville épiscopale de saint Augustin, pref. Jean Lassus "
             "(Paris: Arts et Métiers Graphiques, 1958), 260 pp.",
        edition="Arts et Métiers Graphiques, 1958 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session (library catalogue records) / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim. "
                   "Row 188 (Laporte, 2015) is a later, sharper challenge to this excavation's own "
                   "identification of the Hippo Regius basilica -- neither has been re-read this "
                   "session.",
        body="Licensed for row 38 -- Marec directed the excavations at Hippo Regius and this is the "
             "report of the Christian monuments there, one of this world's own two named cities.",
    ),
    dict(
        row=64, slug="labrousse-optat-de-mileve-critical-edition",
        author="Mireille Labrousse (editor and translator); Optatus of Milevis (author)",
        work="Optat de Milève, Traité contre les donatistes, Sources Chrétiennes 412-413 (Paris: "
             "Cerf, 1995-1996)",
        edition="Cerf, 1995-1996 -- in copyright, never vendored (Source_Acquisition_Manifest.md "
                "SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Labrousse as editor/translator, Optatus as author",
        discovery="WebSearch this session (sourceschretiennes.org's own catalogue) / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Karl Ziwsa's public-domain CSEL 26 (1893) critical Latin text of Optatus is "
                   "already vendored in the shared corpus and is the edition of first resort for row "
                   "27; this edition remains real value as a modern check on it, in copyright, "
                   "consultation-only.",
        body="A critical French edition of Optatus's own text (row 27).",
    ),
    dict(
        row=65, slug="lancel-actes-de-la-conference-de-carthage-411",
        author="Serge Lancel (editor and translator)",
        work="Actes de la Conférence de Carthage en 411, Sources Chrétiennes 194, 195 (1972), 224 "
             "(1975), 373 (1991) (Paris: Cerf)",
        edition="Lancel's own Cerf critical edition is in copyright, consultation-only. The Gesta "
                "themselves are separable from it, and are available: a full Migne Patrologia Latina "
                "XI printing was located and vendored by the sibling Donatism build as "
                "cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt, public domain on the "
                "same by-date basis this corpus already accepts for its other Migne PL volumes, and "
                "the corpus map now assigns it to this world too "
                "(cic/corpus-map/latin-pastoral-congregational-christianity.yaml, role: context, "
                "confidence: provisional, added 2026-09-13 on the project lead's own decision).",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="Lancel's own edition is attributed to him as editor/translator; the Gesta "
                    "themselves are documentary -- an imperial court transcript, with named delegates "
                    "and speakers.",
        discovery="WebSearch this session (the series' own catalogue) / 2026-09-02; content "
                  "independently verified directly against "
                  "cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt, not taken from the "
                  "sibling build's own account of it / 2026-09-13.",
        cite="C", verif="verified-direct", weight="illustrative", formation="Widely Accepted",
        divergence="This Registry's own richest single find, and its own Licensed-For nonetheless "
                   "stays exactly where it started -- a disclosed gap between what was found and what "
                   "is drawn on. Augustine is a named disputant in TWO ways: listed among the seven "
                   "Catholic actores in the delegate roster, and speaking in his own recorded voice in "
                   "the numbered acts -- an OCR-tolerant line-initial scan returns FOURTEEN numbered "
                   "acts in which he speaks (50, 53, 98, 158, 160, 162, 187, 189, 201, 206, 257, 265, "
                   "267, 272), a floor, not a count, given this scan's poor OCR. Doc_02 SS1's own "
                   "'post-411 Conference' phrase still rests on the Conference's own ordinary, "
                   "undisputed date, NOT on any reading of the acts, so no claim currently made in "
                   "this world's construction depends on this correction -- what it opens is a live, "
                   "recorded primary route to Augustine's own voice, available to Doc_04 and not yet "
                   "drawn on by it. Two residual instances of the same defect shape (a modern "
                   "in-copyright edition marked 'not a vendoring candidate' where an earlier printing "
                   "carries a different rights position never checked) are disclosed rather than acted "
                   "on: row 58 (CCSL 3, whose predecessor Hartel is already vendored at row 191) and "
                   "row 59 (Munier's CCSL 149, with no earlier printing named).",
        body="Not currently licensed for a specific claim beyond the Conference's own ordinary, "
             "undisputed date -- but a live, recorded primary route to Augustine's own voice at the "
             "411 Conference now sits in this world's own vendored corpus, bearing directly on his "
             "institutional confidence in that period, available to Doc_04 and not yet drawn on by "
             "it.",
    ),
    dict(
        row=66, slug="mohrmann-etudes-sur-le-latin-des-chretiens",
        author="Christine Mohrmann",
        work="Études sur le latin des chrétiens, 4 vols. (Rome: Edizioni di Storia e Letteratura, "
             "1958-1977)",
        edition="Edizioni di Storia e Letteratura, 1958-1977 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session (library catalogue records) / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="A second genuine Type L entry alongside row 57 (Dekkers).",
        body="The standard scholarly instrument on Christian Latin as a distinct register, directly "
             "serving Doc_03's own instruction (SS9 item 7) to draw candidate terms from the primary "
             "corpus's own vocabulary rather than generic scholarly labels.",
    ),
    dict(
        row=67, slug="mutzenbecher-retractationum-ccsl57",
        author="Almut Mutzenbecher (editor); Augustine of Hippo (author)",
        work="Retractationum libri II, CCSL 57 (Turnhout: Brepols, 1984)",
        edition="Brepols, 1984 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate. Knöll's own CSEL 36 edition of the same text (row 78) is "
                "the public-domain route, now vendored as row 209.",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Mutzenbecher as editor, Augustine as author",
        discovery="WebSearch this session (Brepols's own series record) / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Named because the Retractationes was not vendored anywhere in this corpus at the "
                   "time this row was drafted; row 209 (Knöll's CSEL 36) has since closed that gap on "
                   "a public-domain footing.",
        body="The current scholarly critical edition of the work row 13's Retractationes II.18 "
             "citation holds only at second hand.",
    ),
    dict(
        row=68, slug="merdinger-rome-and-the-african-church",
        author="J. E. Merdinger",
        work="Rome and the African Church in the Time of Augustine (New Haven: Yale University "
             "Press, 1997)",
        edition="Yale University Press, 1997 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session (publisher and journal-review records) / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently re-read.",
        body="The standard modern study of the Apiarius affair (row 26) and Rome's own relationship "
             "with the African church, alongside row 59 (Munier's conciliar edition).",
    ),
    dict(
        row=69, slug="hermanowicz-possidius-of-calama",
        author="Erika T. Hermanowicz",
        work="Possidius of Calama: A Study of the North African Episcopate in the Age of Augustine, "
             "Oxford Early Christian Studies (Oxford: Oxford University Press, 2008)",
        edition="Oxford University Press, 2008 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session (publisher and series records) / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently re-read.",
        body="A modern monograph directly on row 45's own author (Possidius) and this world's own "
             "episcopate as an institution.",
    ),
    dict(
        row=70, slug="markus-saeculum",
        author="R. A. Markus",
        work="Saeculum: History and Society in the Theology of St Augustine (Cambridge: Cambridge "
             "University Press, 1970; rev. ed. 1988)",
        edition="Cambridge University Press, 1970/1988 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Native, but not currently licensed for any specific claim. Markus's own subject, "
                   "Augustine of Hippo writing within this world's own 395-430 window, creates no era/"
                   "place/tradition mismatch, so 'Out-of-Boundary' does not apply -- the actual reason "
                   "this row carries no Licensed-For target is topical narrowness (Augustine's own "
                   "political theology specifically, not this world's own pastoral-congregational "
                   "subject matter), which is not a Boundary Check failure under the Template, the "
                   "same footing row 6 already establishes for a Native source with nothing currently "
                   "licensed.",
        body="A foundational, widely-cited study of Augustine's own political theology and philosophy "
             "of history specifically -- Native, but rowed rather than excluded, per CF V7.4's own "
             "'rowed, or excluded with a reason' rule.",
    ),
    dict(
        row=30, slug="brown-augustine-of-hippo-biography",
        author="Peter Brown",
        work="Augustine of Hippo: A Biography (Berkeley: University of California Press, 1967; rev. "
             "ed. with epilogue, 2000)",
        edition="Berkeley: University of California Press, 1967 / 2000 -- consultation-only, never "
                "vendored (Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY_B,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge, WebSearch-verified against publisher "
                  "and bookseller records / 2026-09-01.",
        cite="B", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="The 2000 revised edition exists in significant part because of the Divjak (row 49) "
                   "and Dolbeau (row 50) discoveries -- that specific claim is licensed at rows 49-50, "
                   "not at this row, since this row's own Licensed-For excludes 'vivid, specific "
                   "claims' of that kind (Doc_02 SS1). Standard, foundational modern biography, not "
                   "independently re-read.",
        body="General biographical and historical framing of Augustine's own career -- not licensed "
             "for vivid, specific claims about this world's own internal congregational life on its "
             "own.",
    ),
    dict(
        row=31, slug="lancel-saint-augustine",
        author="Serge Lancel",
        work="Saint Augustine, trans. Antonia Nevill (London: SCM Press, 2002; French original Saint "
             "Augustin, Paris: Librairie Arthème Fayard, 1999)",
        edition="SCM Press, 2002 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY_B,
        attribution="attributed",
        discovery="WebSearch / 2026-09-01; re-verified via WebSearch (two independent contemporary "
                  "journal reviews, both via Cambridge Core) / 2026-09-02.",
        cite="B", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="The English publication year, previously flagged for priority second-opinion "
                   "review, is now confirmed by two independent journal reviews citing the identical "
                   "imprint; flag resolved, translator name added. Standard modern biography, not "
                   "independently re-read.",
        body="Biographical framing of Augustine placed specifically in his African homeland and "
             "culture, a corrective emphasis to more diffusely 'Late Antique' framings.",
    ),
    dict(
        row=32, slug="burns-cyprian-the-bishop",
        author="J. Patout Burns Jr.",
        work="Cyprian the Bishop, Routledge Early Church Monographs (London: Routledge, hardback "
             "2001 / paperback 2002)",
        edition="Routledge, 2001/2002 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY_B,
        attribution="attributed",
        discovery="WebSearch / 2026-09-01; re-verified via WebSearch (ISBN/catalogue cross-check) / "
                  "2026-09-02.",
        cite="B", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="A genuine two-edition case, not a citation error: hardback 2001, paperback 2002; "
                   "this Registry's own citation (2002) matches the paperback. Both editions "
                   "independently confirmed; still not independently re-read.",
        body="Cyprian's own social and pastoral governance of the Carthaginian congregation during "
             "the Decian persecution and its aftermath -- directly on this world's own central "
             "Cyprian-phase gravity (Doc_01 SS3).",
    ),
    dict(
        row=33, slug="burns-jensen-christianity-in-roman-africa",
        author="J. Patout Burns Jr. and Robin M. Jensen",
        work="Christianity in Roman Africa: The Development of Its Practices and Beliefs (Grand "
             "Rapids, MI: Eerdmans, 2014)",
        edition="Eerdmans, 2014 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed, with G. W. Clarke, S. T. Stevens, W. Tabbernee, and M. A. Tilley as "
                    "collaborators",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01; re-verified via WebSearch "
                  "(four independent scholarly citations plus the publisher's own catalogue page, "
                  "five sources in total) / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Bibliographic details independently verified across five sources this revision, "
                   "matching rows 30-32's own WebSearch-verified-but-not-independently-read pattern "
                   "(Confidence B there); this row's own Confidence letter is left at C pending a "
                   "project-lead decision, since a Confidence-rating change is a substantial revision "
                   "under CO-022 not self-applied post-disposition -- flagged for that decision, not "
                   "for further second-opinion review, which this update has already satisfied.",
        body="The standard modern synthesis of North African Christian practice, liturgy, and "
             "material/social life across this world's own full span.",
    ),
    dict(
        row=34, slug="fahey-cyprian-and-the-bible",
        author="Michael A. Fahey",
        work="Cyprian and the Bible: A Study in Third-Century Exegesis (Tübingen: J.C.B. Mohr, 1971)",
        edition="J.C.B. Mohr, 1971 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Recalled from general field knowledge, not independently checked or "
                   "bibliographically re-verified via WebSearch in any pass. Flagged for priority "
                   "second-opinion review before it supports any specific claim (Doc_02 SS9 item 3).",
        body="Cyprian's own biblical/catechetical method -- licensed only for the Ad Quirinum "
             "testimonia material (row 5), if drawn on.",
    ),
    dict(
        row=35, slug="rebillard-care-of-the-dead-in-late-antiquity",
        author="Éric Rebillard",
        work="The Care of the Dead in Late Antiquity, trans. Elizabeth Trapnell Rawlings and Jeanine "
             "Routier-Pucci (Ithaca: Cornell University Press, 2009)",
        edition="Cornell University Press, 2009 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Recalled from general field knowledge, not independently checked or "
                   "bibliographically re-verified via WebSearch in any pass. Flagged for priority "
                   "second-opinion review before it supports any specific claim (Doc_02 SS9 item 3).",
        body="If drawn on: burial practice and congregational piety around death, on the same subject "
             "as Augustine's own On Care to Be Had for the Dead (row 25).",
    ),
    dict(
        row=36, slug="shaw-sacred-violence",
        author="Brent D. Shaw",
        work="Sacred Violence: African Christians and Sectarian Hatred in the Age of Augustine "
             "(Cambridge: Cambridge University Press, 2011)",
        edition="Cambridge University Press, 2011 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY_B,
        attribution="attributed",
        discovery="the sibling Donatism build's own Registry, row 24 / 2026-09-01. Relied on rather "
                  "than independently re-verified here.",
        cite="B", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Already independently bibliographically verified in the sibling Donatism build's "
                   "own Registry (its own row 24), which this document relies on rather than "
                   "re-verifying; not independently re-read this session.",
        body="The standard modern treatment of the Donatist/Circumcellion violence Augustine's own "
             "coercion argument (row 12) responds to -- background context for the coercive-capacity "
             "axis (Doc_01 SS4), not itself evidence of this world's own internal life.",
    ),
    dict(
        row=37, slug="cil-viii-inscriptiones-africae-latinae",
        author="Rene Cagnat, Johannes Schmidt, and successive editors",
        work="Corpus Inscriptionum Latinarum, vol. VIII, Inscriptiones Africae Latinae (Berlin: "
             "Reimer, 1881-, with supplements)",
        edition="the Numidia supplement is vendored in the shared corpus as "
                "cic/texts/cil8-supplementum-numidiae_cagnat-schmidt1894.txt, discharged 2026-09-01 "
                "on the sibling Donatism build's own former G7 request, and directly usable by this "
                "document",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed to the successive CIL editors",
        discovery="the sibling Donatism build's own Registry, row 48 / 2026-09-01.",
        cite="B", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently re-checked against a specific volume or inscription this "
                   "session. Flagged for priority second-opinion review before it supports any "
                   "specific inscription claim (Doc_02 SS5, SS9 item 2). Row 136 (L'Année épigraphique) "
                   "is the standing modern successor instrument covering what CIL VIII's own "
                   "nineteenth-century compilation cannot.",
        body="The standard epigraphic corpus for Roman North Africa -- Carthage and Hippo's own "
             "material/inscriptional record, if consulted (Doc_02 SS5).",
    ),
    dict(
        row=38, slug="numidian-proconsular-basilica-archaeology",
        author="No named author -- a recognized field category, not a specific publication",
        work="Numidian/Proconsular-Africa basilica archaeology at Carthage and Hippo Regius "
             "specifically (general category)",
        edition="No edition. No specific site report, excavation record, or publication is named "
                "anywhere in Source_Registry.md or Source_Acquisition_Manifest.md for this row's own "
                "category itself.",
        rights=RIGHTS_NO_EDITION_HELD,
        attribution="none -- no publication, excavator, or site report is named at this row, so there "
                    "is nothing to attribute.",
        discovery="builder-prior-knowledge (recognized field category, comparable to the sibling "
                  "Donatism build's own row 28) / field knowledge / 2026-09-01.",
        cite="D", verif="unverified", weight="illustrative", formation="Inferential-Thin",
        divergence="AUTHORED DEPARTURE, stated rather than buried. This row names no author, no work, "
                   "and no site report -- the Registry's own definition of D "
                   "('genre/tradition-level attribution with no specific text or author named'), not "
                   "of a real-but-unpinpointed C-level locus -- so verification_state is set to "
                   "`unverified` rather than `named-not-rechecked`. Both cities specifically now have "
                   "a named excavation report (row 63, Marec, for Hippo Regius; row 82, Ennabli, for "
                   "Carthage), each licensed directly for this row, but neither has itself been "
                   "independently re-read this session (Doc_02 SS5). Doc_02 SS8 independently bands "
                   "the material/epigraphic conditions of worship at this world's two cities as "
                   "Inferential-Thin.",
        body="Not currently licensed for a specific claim -- the material/spatial conditions of this "
             "world's own worship spaces, carried honestly as a gap rather than a source. Doc_07 SS2G "
             "calls this world's material dimension 'document-borne rather than excavated' and "
             "'unexcavated,' not empty.",
    ),
    dict(
        row=39, slug="hartel-cyprian-opera-omnia-csel3-standing-reference",
        author="Wilhelm (Guilelmus) von Hartel (editor); Cyprian of Carthage (author)",
        work="S. Thasci Caecili Cypriani opera omnia, Corpus Scriptorum Ecclesiasticorum Latinorum "
             "(CSEL) 3.1-3.3 (Vienna: C. Geroldi filius, 1868-1871)",
        edition="NOT the base text of the vendored ANF05 translation (ANF05's own introductory "
                "notice states its base is Migne's text, not Hartel's); superseded as the current "
                "critical edition by CCSL 3 (row 58). Pars I-II now vendored as row 191 (2026-09-05); "
                "Pars III now also vendored as row 194 (2026-09-08) -- this row is kept as the "
                "standing reference to the edition as a whole; rows 191 and 194 carry the actually-"
                "committed files.",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. The editor's forename is Wilhelm, not Karl (confirmed against the "
                    "CSEL series record).",
        discovery="WebSearch this session / 2026-09-01; ANF05's own introductory notice, read "
                  "directly, for the base-text correction / 2026-09-01.",
        cite="B", verif="verified-via-authority", weight="corroborating", formation="Widely Accepted",
        divergence="A real bibliographic finding disclosed rather than smoothed away: ANF05's own "
                   "Cyprian translator is named on the same page (Rev. Ernest Wallis), and this "
                   "edition is an independent, later critical apparatus alongside the vendored "
                   "translation, not that translation's own source text. The full CSEL 3 edition "
                   "(Pars I-III) is now vendored in this corpus, at rows 191 and 194, not under this "
                   "row's own number.",
        body="An independent, 19th-century critical edition to check the vendored Migne-based "
             "translation against, and, for the Cyprian corpus specifically, the only edition at this "
             "level of rigor actually acquirable under this project's public-domain-only vendoring "
             "rule.",
    ),
    dict(
        row=40, slug="pontius-vita-cypriani-alternative-editions-standing-reference",
        author="Adolf Harnack (editor) and Michele Pellegrino (editor); Pontius the Deacon (author)",
        work="Alternative critical editions of Pontius's Vita Cypriani (row 7): A. Harnack (ed.), Das "
             "Leben Cyprians von Pontius (Leipzig, 1913); M. Pellegrino (ed.), Ponzio: Vita e martirio "
             "di San Cipriano (Alba: Edizioni Paoline, 1955 -- see row 48)",
        edition="Harnack's own 1913 edition is now vendored, row 205 (2026-09-08), closing Manifest "
                "G2 -- this row is kept as the standing reference for both named editions; "
                "Pellegrino's remains in copyright and unvendored.",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Harnack and Pellegrino respectively, as editors of Pontius's Life",
        discovery="WebSearch this session / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not vendored under this row's own number, and neither located at a specific URL "
                   "this original session -- named from a single WebSearch result summarizing modern "
                   "critical editions, not independently corroborated by a second search at the time "
                   "this row was drafted. Pellegrino's 1955 edition is in copyright (row 48); "
                   "Harnack's 1913 edition is the only one of the two with a plausible public-domain "
                   "status, and is now vendored as row 205.",
        body="Alternative critical editions of, or a check against, the already-vendored ANF English "
             "translation of Pontius's Life (row 7).",
    ),
    dict(
        row=41, slug="acta-proconsularia-sancti-cypriani",
        author="An unnamed imperial notary or court recorder",
        work="Acta Proconsularia Sancti Cypriani (the official trial record of Cyprian's own "
             "martyrdom, 258)",
        edition="No independent edition or URL was ever located under this row's own number. Now "
                "vendored inside row 194 -- Hartel's CSEL 3 Pars III includes the Acta Proconsularia "
                "immediately after the Vita (pp. CX-CXIV of the printed volume), as "
                "cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="documentary -- an official trial record, distinct in genre from Pontius's "
                    "hagiographic Life (row 7); attested only inside row 194's larger vendored file, "
                    "with no independent transmission of its own named anywhere in this Registry.",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01; resolved by G1's own Pars "
                  "III fulfillment, independently confirmed present at pp. CX-CXIV / 2026-09-08.",
        cite="D", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Named from general field knowledge that such acts survive and are frequently "
                   "printed alongside Pontius's Life in critical editions, not independently verified "
                   "as a separately locatable public-domain text under this row's own number at the "
                   "time it was drafted. Row 194's own vendoring closes the acquisition question but "
                   "has not itself been read specifically for this text's own content beyond "
                   "confirming its presence and page range.",
        body="Not currently licensed for a specific claim -- the one strictly documentary (as opposed "
             "to hagiographic) record of Cyprian's own death, distinct in genre from Pontius's Life.",
    ),
    dict(
        row=42, slug="acts-of-council-of-carthage-under-cyprian-npnf214",
        author="The Council of Carthage under Cyprian (256), as transmitted in the seven-ecumenical-"
               "councils volume",
        work="The Acts of the Council of Carthage under Cyprian (256 per modern scholarship; the "
             "npnf214 volume's own headings date it a.d. 257, twice) -- an npnf214 telling, distinct "
             "from row 4's anf05 telling of the same council",
        edition="Nicene and Post-Nicene Fathers, Series II, vol. XIV, vendored as "
                "cic/texts/npnf214_seven-ecumenical-councils.xml",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed to the conciliar body; the 'above eighty-four bishops' figure is a "
                    "quotation, inside npnf214's own editorial Introductory Note, of the twelfth-"
                    "century Byzantine canonist Zonaras -- not a second independent transmission of "
                    "the event, and not in tension with row 4's own 'Eighty-Seven Bishops,' which the "
                    "corpus map's own note on this entry independently agrees with.",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="A DISTINCT ENTRY from row 4, kept distinct rather than merged, per Doc_01 SS7's "
                   "own established practice for this exact council -- NOT to be cited at row 4's own "
                   "Confidence A. Not currently drawn on for any specific claim: the Donatist-"
                   "patrimony claim is grounded on row 13 instead, consistent with this row's own "
                   "Confidence C and its own unchecked locus.",
        body="Kept as its own row precisely so that a future claim cannot quietly inherit row 4's "
             "assigned confidence by way of this provisional telling (Doc_02 SS1).",
    ),
    dict(
        row=43, slug="augustine-letter-93-to-vincentius",
        author="Augustine of Hippo",
        work="Letter XCIII (to Vincentius, a.d. 408 on the NPNF heading)",
        edition="Nicene and Post-Nicene Fathers, Series I, vol. I, vendored as "
                "cic/texts/npnf101_augustine-confessions-letters.xml",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. This letter sits inside the corpus map's own Donatist-letters "
                    "sub-corpus per cic/corpus-map/_staging/npnf101_augustine-confessions-"
                    "letters.yaml (role: context, assigned to donatism, and to NO role for this "
                    "world) -- an honestly-disclosed boundary case, not papered over. Held Native here "
                    "on the Registry Template's own second test: 'the question this check asks is "
                    "never \"does another world already have this\" -- it is simply \"was this "
                    "source actually used, inherited, or drawn on as part of this world's own "
                    "formation, on this world's own evidence?\"' -- and this letter is Augustine's own "
                    "first-person, in-boundary account of his own change of mind, drawn on directly "
                    "by Doc_01 SS7, not as evidence about Donatism's own side of anything.",
        discovery="corpus map / cic/corpus-map/_staging/npnf101_augustine-confessions-letters.yaml / "
                  "2026-09-01; direct verification against "
                  "cic/texts/npnf101_augustine-confessions-letters.xml across Doc_01's nine review "
                  "rounds / 2026-09-01.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Licensed narrowly for Augustine's own biographical/opinion-change claim -- 'my "
                   "opinion was, that no one should be coerced into the unity of Christ... this "
                   "opinion of mine was overcome... by the conclusive instances to which they could "
                   "point' (SS17) -- NOT for characterizing the Donatist side of the dispute this "
                   "letter occurs within, which row 11 explicitly excludes and this row does not "
                   "repeat.",
        body="Augustine's own first-person account of his earlier opinion against any coercion, one "
             "phase of the three-phase state-power arc Doc_01 SS7 reports (early opinion against any "
             "coercion, by his own retrospective account; a real but narrow solicitation of legal "
             "protection, argued but not granted, at the 401 council row 12 records; a later, "
             "sustained defence of broader compulsion).",
    ),
    dict(
        row=44, slug="codex-theodosianus-mommsen-meyer",
        author="Theodor Mommsen and Paul M. Meyer (editors)",
        work="Codex Theodosianus, ed. Th. Mommsen and P. M. Meyer, Theodosiani libri XVI cum "
             "Constitutionibus Sirmondianis (Berlin: Weidmann, 1905), full text (all 16 books)",
        edition="Vendored, held in the shared corpus as "
                "cic/texts/theodosianus-16_mommsen-meyer1905.txt, the same identifier the sibling "
                "Donatism build vendored (its own G3, discharged in full 2026-09-07)",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="documentary -- Roman imperial legislation, compiled 438 from statutes of the "
                    "fourth and fifth centuries",
        discovery="the sibling Donatism build's own Registry, row 16, and Manifest, G3 / 2026-09-01.",
        cite="B", verif="verified-via-authority", weight="load-bearing", formation="Widely Accepted",
        divergence="Confidence deliberately left at B, not raised: this row's own Licensed-For content "
                   "has NOT been read against the vendored file by this world's own construction, so "
                   "the calibration rule's own bar for a higher letter is not met. The provision "
                   "behind Augustine's own Letter 185 SS25 is CTh XVI.5.21 (392), NOT CTh XVI.5.52 "
                   "(412, the graduated Donatist-specific silver-fine schedule that belongs to the "
                   "sibling Donatism build) -- the two are easy to collapse into each other and this "
                   "row does not. Two copies of this edition exist on two different rights bases: an "
                   "Oxford Text Archive CC BY-NC-SA legacy transcription, supplied by the project lead "
                   "but never vendored (not out-of-copyright), and this row's own Google Books scan, "
                   "independently public domain by its 1905 date. A third, differently-sourced copy "
                   "of unstated critical ancestry is row 88.",
        body="The underlying imperial statute behind the Theodosian-law fine Augustine's own Letter "
             "185 SS25 cites (row 12) -- not currently drawn on directly, since Doc_01's own "
             "state-power finding rests on Augustine's own primary account rather than the statute's "
             "own text.",
    ),
    dict(
        row=45, slug="possidius-vita-augustini-standing-reference",
        author="Possidius, bishop of Calama",
        work="Sancti Augustini Vita (Life of Augustine)",
        edition="Now vendored as row 192 (2026-09-05) -- this row is kept as the standing reference; "
                "row 192 carries the actually-committed file, "
                "cic/texts/possidius_vita-augustini_weiskotten1919.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Possidius, bishop of Calama and Augustine's own friend of nearly "
                    "forty years",
        discovery="Doc_01 SS5's own disclosure / field knowledge / 2026-09-01; resolved by G3's own "
                  "fulfillment / 2026-09-05.",
        cite="C", verif="named-not-rechecked", weight="load-bearing", formation="Widely Accepted",
        divergence="Named in Doc_01 SS5 as 'not vendored in this corpus' at this row's own original "
                   "drafting -- the source of NPNF's own editorial note on the Megalius/primate-of-"
                   "Numidia identification. Now vendored under row 192, and read in full "
                   "(all thirty-one chapters, Review-Artifacts/Possidius_Full_Read_2026-09-16.md) -- "
                   "this row is the standing reference to the work, row 192 the fulfillment record.",
        body="Augustine's own formation-narrative counterpart to Pontius's Life of Cyprian (row 7); "
             "the source, via NPNF's own editorial apparatus, for the Megalius/primate-of-Numidia "
             "identification Doc_01 SS5 names.",
    ),
    dict(
        row=46, slug="clarke-letters-of-st-cyprian",
        author="G. W. Clarke (translator)",
        work="The Letters of St. Cyprian of Carthage, Ancient Christian Writers 43, 44, 46, 47 (New "
             "York: Newman Press, 1984-1989)",
        edition="Newman Press, 1984-1989 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked against a specific volume or locus, not corroborated by "
                   "an independent WebSearch. Flagged for priority second-opinion review before it "
                   "supports any specific claim -- the instrument that would settle this world's own "
                   "multiple-numbering confusion (Migne order, Oxford numbers, CSEL numbers) directly, "
                   "the exact confusion behind row 1's own Ep. XL/Epistle XXXIX citation error.",
        body="The standard modern English translation and historical commentary on row 1's own "
             "corpus.",
    ),
    dict(
        row=47, slug="van-der-meer-augustine-the-bishop",
        author="F. van der Meer",
        work="Augustine the Bishop: The Life and Work of a Father of the Church, trans. Brian "
             "Battershaw and G.R. Lamb (London: Sheed & Ward, 1961)",
        edition="Sheed & Ward, 1961 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="builder-prior-knowledge / field knowledge / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked against a specific chapter or claim, not corroborated "
                   "by an independent WebSearch. Flagged for priority second-opinion review before it "
                   "supports any specific claim -- the standard modern study of Augustine's own actual "
                   "pastoral, congregational, and liturgical practice at Hippo, the same gap the "
                   "missing liturgical-evidence assessment (Doc_02 SS9 item 9) reflects from another "
                   "angle.",
        body="The standard modern study of Augustine's own actual pastoral, congregational, and "
             "liturgical practice at Hippo, directly on this world's own named subject.",
    ),
    dict(
        row=48, slug="pellegrino-vita-e-martirio-di-san-cipriano",
        author="Michele Pellegrino (editor); Pontius the Deacon (author)",
        work="Ponzio: Vita e martirio di San Cipriano (Alba: Edizioni Paoline, 1955)",
        edition="Edizioni Paoline, 1955 -- consultation-only, never vendored "
                "(Source_Acquisition_Manifest.md SS3); in copyright as of 1955 in most jurisdictions, "
                "unlike Harnack's 1913 edition (row 40, now row 205)",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Pellegrino as editor, Pontius as author",
        discovery="WebSearch this session (second search, correcting Manifest G2's own earlier 'year "
                  "not identified' note) / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="This row is disclosed as physically sitting out of numeric order in the table "
                   "below row 41 -- a deliberate, disclosed placement, since it sits beside and "
                   "corrects row 40, not an error (Source_Registry.md's own disclosed-placement rule). "
                   "Superseded row 40's own 'year not identified' note for this specific edition; "
                   "Harnack 1913 (now vendored, row 205) remains the more promising public-domain lead "
                   "of the two named at row 40.",
        body="The specific edition row 40 named without a confirmed year; year and editor's first "
             "name both confirmed by a second search this revision.",
    ),
    dict(
        row=49, slug="divjak-epistolae-ex-duobus-codicibus",
        author="Johannes Divjak (editor); Augustine of Hippo (author)",
        work="Epistolae ex duobus codicibus nuper in lucem prolatae ('Epistolae,' not 'Epistulae,' "
             "per the printed title's own spelling), CSEL 88 (Vienna, 1981) -- the 'Divjak letters,' "
             "29 previously unknown letters of Augustine, found by Divjak in 1975 in the Bibliothèque "
             "Municipale de Marseille",
        edition="Vienna, 1981 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="The find's own discovery date is disclosed as genuinely uncertain rather than "
                   "settled: live search returns '1969' in at least one journal-adjacent account and "
                   "'1974' in another; this row carries 1975 (the year Divjak found the manuscript in "
                   "Marseille, independently re-confirmed), on the same disclosure standard rows 4 and "
                   "42 apply to their own council-date divergence. No specific letter or locus "
                   "independently checked.",
        body="Licensed alongside row 50 for Doc_02 SS1's own claim that Peter Brown's 2000 revised "
             "biography (row 30) exists in significant part because of this and the Dolbeau find; "
             "also a completeness qualifier on row 11 (the vendored 138-letter general-correspondence "
             "body is the 19th-century NPNF selection, not the full modern corpus).",
    ),
    dict(
        row=50, slug="dolbeau-vingt-six-sermons-au-peuple-dafrique",
        author="François Dolbeau (editor); Augustine of Hippo (author)",
        work="Vingt-six sermons au peuple d'Afrique (Paris: Institut d'Études Augustiniennes, 1996) "
             "-- 26 previously unknown sermons of Augustine, identified by Dolbeau in a mid-15th-"
             "century Mainz manuscript catalogued in 1990",
        edition="Paris, 1996 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch this session / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="No specific sermon or locus independently checked.",
        body="Licensed alongside row 49 for Doc_02 SS1's Brown-2000 claim; also a completeness "
             "qualifier on row 19 (the vendored ~97-sermon NPNF body is not the full modern corpus).",
    ),
    dict(
        row=51, slug="bevenot-de-lapsis-and-de-unitate-critical-edition",
        author="Maurice Bévenot (editor and translator); Cyprian of Carthage (author)",
        work="Cyprian: De Lapsis and De Ecclesiae Catholicae Unitate, Oxford Early Christian Texts "
             "(Oxford: Clarendon Press, 1971)",
        edition="Clarendon Press, 1971 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Bévenot as editor and translator, Cyprian as author",
        discovery="WebSearch this session (publisher and journal-review records) / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Naming this edition does not itself close row 3's own open two-recension "
                   "question -- that would require reading this edition's own apparatus, not merely "
                   "acquiring or naming it.",
        body="Licensed for the De Unitate two-recension question at row 3 -- Bévenot is the scholar "
             "whose own critical edition resolves which of the two surviving recensions of De Unitate "
             "4-5 (one the 'Primacy Text') is prior, a question row 3 currently carries as unresolved.",
    ),
    dict(
        row=52, slug="fitzgerald-augustine-through-the-ages",
        author="Allan D. Fitzgerald (editor)",
        work="Augustine through the Ages: An Encyclopedia (Grand Rapids: Eerdmans, 1999)",
        edition="Eerdmans, 1999 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Fitzgerald as editor",
        discovery="WebSearch this session / 2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="This row is disclosed as physically sitting out of numeric order in the table, "
                   "between rows 194 and 195 -- a deliberate, disclosed placement (it is edited in "
                   "place rather than moved), not an error. Type S, not L: the Template's own Type L "
                   "(Period Lexicon) is defined as keyed to the period's own language, and a 1999 "
                   "English-language encyclopedia does not meet that definition, however useful -- "
                   "row 57 (Dekkers's Clavis Patrum Latinorum) is this Registry's own actual first "
                   "Type L entry. A second candidate, Mayer's multi-volume, still-in-progress, "
                   "German-language Augustinus-Lexikon, was considered and not rowed here.",
        body="A modern reference instrument for date, work-identification, and terminological control "
             "across rows 9-25 -- a world whose Augustine rows alone number over fifty works.",
    ),
    dict(
        row=27, slug="optatus-against-the-donatists",
        author="Optatus of Milevis",
        work="Against the Donatists (Books I-VII)",
        edition="vendored as cic/texts/optatus_against-the-donatists.txt",
        rights=RIGHTS_VENDORED_INHERITED,
        attribution="attributed to Optatus of Milevis; provisionally double-placed on the census -- "
                    "cic/corpus-map/donatism.yaml carries its OWN Optatus entry (role: context, "
                    "confidence: assigned, 'Assigned twice with different roles, deliberately') -- "
                    "tradition here, context there, a deliberate double-placement, not a defect "
                    "(Doc_02 SS1).",
        discovery="corpus map / cic/corpus-map/latin-pastoral-congregational-christianity.yaml / "
                  "2026-09-01.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Provisional Latin home for the Catholic side of the Donatist schism, per the "
                   "corpus map's own note -- 'Mark may prefer another Latin home for a Numidian "
                   "polemicist.' NOT drawn on for a specific claim in this world's own Doc_01 or "
                   "Doc_02: Optatus's Against the Donatists is Catholic-side anti-Donatist polemic, "
                   "not evidence of this world's own ordinary pastoral-congregational life the way "
                   "Cyprian's and Augustine's own corpora are.",
        body="Named for completeness and for the corpus-map placement question Doc_01 SS8 item 2 "
             "hands to Doc_02 -- left standing rather than re-homed, since re-homing a census entry "
             "is outside this build thread's own editing authority (Doc_02 SS1, SS9 item 11).",
    ),
    dict(
        row=99, slug="delehaye-passions-des-martyrs-genres-litteraires-standing-reference",
        author="Hippolyte Delehaye, S.J.",
        work="Les Passions des martyrs et les genres littéraires, Subsidia Hagiographica 13b "
             "(Brussels: Société des Bollandistes, 1921; 2nd ed. 1966)",
        edition="Now vendored, row 212 (2026-09-08), closing Manifest G9; vendored as "
                "cic/texts/delehaye_passions-martyrs-genres-litteraires-fra_1921.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02; resolved by G9's own fulfillment / 2026-09-08.",
        cite="C", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Public domain (1921); title page, Préface, all six chapters, and the closing "
                   "Table des Matières directly verified, confirming the volume is not truncated. The "
                   "Manifest's own 'Subsidia Hagiographica 13b' series designation is flagged as "
                   "unverifiable from this scan itself, disclosed as an open gap rather than asserted "
                   "with false confidence.",
        body="Licensed for the Author Gravity risk assessment of Pontius's Life at Doc_02 SS2 and SS4 "
             "-- that assessment names the risk directly but had no scholarly instrument for what the "
             "passio/formation-biography genre reliably preserves and where it reliably shapes; "
             "Delehaye's is the foundational modern study of exactly that.",
    ),
    dict(
        row=100, slug="bibliotheca-hagiographica-latina",
        author="Socii Bollandiani (editors)",
        work="Bibliotheca Hagiographica Latina antiquae et mediae aetatis (Brussels: Société des "
             "Bollandistes, 1898-1901; Supplementum, 1911; Novum Supplementum, ed. H. Fros, Subsidia "
             "Hagiographica 70, 1986)",
        edition="Société des Bollandistes, 1898-1986 -- never vendored (Source_Acquisition_"
                "Manifest.md SS3); mixed rights, disclosed rather than treated as one item -- the "
                "base volumes and the 1911 Supplementum are public domain, the 1986 Novum "
                "Supplementum is in copyright",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Held consultation-only as a set rather than split into a partial vendoring "
                   "candidate, a builder's judgment call rather than a review instruction. Flagged "
                   "for priority second-opinion review before it supports any specific claim.",
        body="Licensed for dating and identifying Pontius's Life (BHL 2041) and the Acta "
             "Proconsularia (row 41) -- this Registry's first hagiography-specific reference "
             "instrument, alongside Dekkers's Clavis (row 57) for the wider patristic corpus.",
    ),
    dict(
        row=101, slug="bobertz-cyprian-of-carthage-priest-and-patron",
        author="Charles A. Bobertz",
        work="Cyprian of Carthage: Priest and Patron, Studia Patristica Supplements 12 (Leuven: "
             "Peeters, 2023)",
        edition="Peeters, 2023 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked. A related but distinct question from row 32 (Burns)'s "
                   "own coverage of Cyprian's social governance during and after the Decian "
                   "persecution.",
        body="Licensed for row 1's own election language -- 'your suffrage and God's judgment' -- and "
             "Doc_02 SS2's Representativeness discussion, which builds directly on the patron-bishop "
             "dynamic that language implies.",
    ),
    dict(
        row=102, slug="cameron-christ-meets-me-everywhere",
        author="Michael Cameron",
        work="Christ Meets Me Everywhere: Augustine's Early Figurative Exegesis, Oxford Studies in "
             "Historical Theology (Oxford: Oxford University Press, 2012)",
        edition="Oxford University Press, 2012 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. A different, earlier Cameron work from row 121's own "
                   "'Valerius of Hippo: A Profile.'",
        body="Not currently licensed for a specific claim -- a secondary instrument for rows 19-21 "
             "(Augustine's own preaching and exegesis), one of this world's largest primary bodies "
             "with no study of its own method previously named.",
    ),
    dict(
        row=103, slug="clark-monica-an-ordinary-saint",
        author="Gillian Clark",
        work="Monica: An Ordinary Saint, Women in Antiquity (Oxford: Oxford University Press, 2015)",
        edition="Oxford University Press, 2015 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Native, unlicensed. Monica's 387 death falls inside this world's own 246-430 "
                   "boundary, and a topical/scope ground -- 'outside this world's own Carthage/Hippo "
                   "congregational-life focus' -- is not one the Template's own narrow Out-of-"
                   "Boundary definition supports. Sits on the same footing as rows 70, 86, 87, and "
                   "127: Native, unlicensed, rather than forcing a geographic argument this row's own "
                   "Verification Note does not actually make.",
        body="Not currently licensed for any specific claim -- Monica's death (387) falls before "
             "Augustine's own ordination as presbyter (391), so her presence is his own pre-clerical "
             "formation-narrative material, not evidence of congregational life under either bishop's "
             "own active ministry (Doc_02 SS6).",
    ),
    dict(
        row=104, slug="donna-st-cyprian-letters-fotc",
        author="Sister Rose Bernard Donna (translator); Cyprian of Carthage (author)",
        work="St. Cyprian: Letters (1-81), The Fathers of the Church 51 (Washington: Catholic "
             "University of America Press, 1964)",
        edition="Catholic University of America Press, 1964 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Donna as translator, Cyprian as author",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. A second, independent modern English translation of "
                   "Cyprian's own letters, from a different tradition than Clarke's ACW rendering "
                   "(row 46).",
        body="Not currently licensed for a specific claim.",
    ),
    dict(
        row=105, slug="deferrari-saint-cyprian-treatises-fotc",
        author="Roy J. Deferrari et al. (translators); Cyprian of Carthage (author)",
        work="Saint Cyprian: Treatises, The Fathers of the Church 36 (Washington: Catholic "
             "University of America Press, 1958)",
        edition="Catholic University of America Press, 1958 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Deferrari et al. as translators, Cyprian as author",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. A modern parallel translation to ANF05's own rendering "
                   "of row 5's minor treatises.",
        body="Not currently licensed for a specific claim.",
    ),
    dict(
        row=106, slug="parsons-saint-augustine-letters-fotc",
        author="Sister Wilfrid Parsons (translator); Augustine of Hippo (author)",
        work="Saint Augustine: Letters, The Fathers of the Church 12, 18, 20, 30, 32, 5 vols. "
             "(Washington: Catholic University of America Press, 1951-1956)",
        edition="Catholic University of America Press, 1951-1956 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Parsons as translator, Augustine as author",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Not independently checked. This direct, complete rendering has existed since the "
                   "1950s and is the version most seminary and university libraries actually hold. "
                   "Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for rows 10, 11, and 43 -- those rows rest at Confidence A on the 19th-century "
             "NPNF translation alone, with no modern English alternative previously named.",
    ),
    dict(
        row=107, slug="stevens-kalinowski-vanderleest-bir-ftouha",
        author="Susan T. Stevens, Angela V. Kalinowski, and Hans Vanderleest",
        work="Bir Ftouha: A Pilgrimage Church Complex at Carthage, Journal of Roman Archaeology "
             "Supplementary Series 59 (Portsmouth, RI: JRA, 2005)",
        edition="JRA, 2005 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not "
                "a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 38's own Confidence-D gap ('only the category,' no specific site "
             "report named) and row 82 (Ennabli, a citywide overview) -- a full excavation monograph "
             "for a specific Carthage church complex.",
    ),
    dict(
        row=108, slug="stevens-bir-el-knissia",
        author="Susan T. Stevens",
        work="Bir el Knissia at Carthage: A Rediscovered Cemetery Church, Report No. 1, Journal of "
             "Roman Archaeology Supplementary Series 7 (Ann Arbor: JRA, 1993)",
        edition="JRA, 1993 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not "
                "a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A second, earlier Carthage excavation report by the same excavator as row "
                   "107.",
        body="Licensed for the same gap as row 107.",
    ),
    dict(
        row=109, slug="jones-martindale-morris-plre-vol1",
        author="A. H. M. Jones, J. R. Martindale, and J. Morris",
        work="The Prosopography of the Later Roman Empire, Vol. I: A.D. 260-395 (Cambridge: "
             "Cambridge University Press, 1971)",
        edition="Cambridge University Press, 1971 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for identifying and dating the imperial officials named only by office in "
             "rows 12, 43, 44, and 88 -- this Registry's own prosopographical instruments (rows 62, "
             "90) are Africa/Cyprian-specific and do not reach the wider imperial administration.",
    ),
    dict(
        row=110, slug="martindale-plre-vol2",
        author="J. R. Martindale",
        work="The Prosopography of the Later Roman Empire, Vol. II: A.D. 395-527 (Cambridge: "
             "Cambridge University Press, 1980)",
        edition="Cambridge University Press, 1980 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim. "
                   "Same licensing as row 109, specifically for Augustine's own episcopal period.",
        body="Count Marcellinus and the 411 Conference of Carthage (row 65) fall inside this volume's "
             "own range.",
    ),
    dict(
        row=111, slug="alexander-threshing-floor-parable-411-conference",
        author="James S. Alexander",
        work="'A Note on the Interpretation of the Parable of the Threshing Floor at the Conference "
             "of Carthage of A.D. 411,' Journal of Theological Studies 24.2 (1973): 512-519",
        edition="JTS, 1973 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not "
                "a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 65's own 411 Conference of Carthage material -- a specific interpretive "
             "crux row 65's own bare edition citation does not itself unpack.",
    ),
    dict(
        row=112, slug="dunn-heresy-and-schism-according-to-cyprian",
        author="Geoffrey D. Dunn",
        work="'Heresy and Schism according to Cyprian of Carthage,' Journal of Theological Studies "
             "55.2 (2004): 551-574",
        edition="JTS, 2004 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not "
                "a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim. "
                   "A second, distinct Dunn work from row 77's own monograph.",
        body="Licensed for Doc_02 SS2's Representativeness discussion of Cyprian's own ecclesiology "
             "directly.",
    ),
    dict(
        row=113, slug="granfield-episcopal-elections-in-cyprian",
        author="Patrick Granfield",
        work="'Episcopal Elections in Cyprian: Clerical and Lay Participation,' Theological Studies "
             "37.1 (1976): 41-52",
        edition="Theological Studies, 1976 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 1 directly -- the electoral mechanism behind Cyprian's own central "
             "citation, 'your suffrage and God's judgment,' which no other row addresses at this "
             "level; row 101 (Bobertz) addresses the wider patron-bishop dynamic, a related but "
             "distinct question.",
    ),
    dict(
        row=114, slug="chronica-tertulliana-et-cyprianea",
        author="F. Chapot, S. Deléani, F. Dolbeau, J.-C. Fredouille, M.-Y. Perrin, and P. Petitmengin",
        work="'Chronica Tertullianea et Cyprianea' (an annually recurring bibliographic survey, "
             "published each year in the Revue des Études Augustiniennes et Patristiques since the "
             "mid-1970s, broadened since 1986 to cover all Latin Christian literature to the death "
             "of Cyprian)",
        edition="Revue des Études Augustiniennes et Patristiques, ongoing -- in copyright, never "
                "vendored (Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to the successive named compilers",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A standing, recurring verification channel, distinct in kind from this "
                   "Registry's static reference catalogues (CPL, row 57; BHL, row 100).",
        body="Licensed for the field-bibliography-sweep gap Doc_02 SS9 item 6 already discloses as "
             "unclosed.",
    ),
    dict(
        row=115, slug="greenslade-early-latin-theology-lcc",
        author="S. L. Greenslade (editor and translator)",
        work="Early Latin Theology: Selections from Tertullian, Cyprian, Ambrose and Jerome, "
             "Library of Christian Classics 5 (London: SCM Press, 1956)",
        edition="SCM Press, 1956 -- in copyright, never vendored (Source_Acquisition_Manifest.md "
                "SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Greenslade as editor/translator",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- a further, independent modern English "
             "translation tradition for Cyprian's shorter works, British/ecumenical rather than "
             "American Catholic (rows 104-105) or the already-vendored 19th-century ANF.",
    ),
    dict(
        row=116, slug="outler-augustine-confessions-and-enchiridion-lcc",
        author="Albert C. Outler (translator and editor); Augustine of Hippo (author)",
        work="Augustine: Confessions and Enchiridion, Library of Christian Classics 7 (Philadelphia: "
             "Westminster Press, 1955)",
        edition="Westminster Press, 1955 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Outler as translator/editor, Augustine as author",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. Distinct from row 53's O'Donnell critical edition, "
                   "which does not itself carry sustained theological commentary.",
        body="Not currently licensed for a specific claim -- a mid-century translation-with-"
             "commentary of the Confessions and Enchiridion.",
    ),
    dict(
        row=117, slug="hexter-metamorphosis-of-sodom",
        author="Ralph J. Hexter",
        work="'The Metamorphosis of Sodom: The Ps.-Cyprian De Sodoma as an Ovidian Episode,' "
             "Traditio 44 (1988): 1-36",
        edition="Traditio, 1988 -- in copyright, never vendored (Source_Acquisition_Manifest.md "
                "SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 6's own pseudo-Cyprianic-corpus disclosure -- row 6 names four "
             "specific works but not De Sodoma, a further text transmitted under Cyprian's own name "
             "that row 6's own boundary note does not currently reach.",
    ),
    dict(
        row=118, slug="claussen-peregrinatio-and-peregrini",
        author="M. A. Claussen",
        work="'Peregrinatio and Peregrini in Augustine's City of God,' Traditio 46 (1991): 33-75",
        edition="Traditio, 1991 -- in copyright, never vendored (Source_Acquisition_Manifest.md "
                "SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 24 -- City of God, this Registry's largest single primary text, "
             "currently with no secondary instrument of any kind attached to it.",
    ),
    dict(
        row=119, slug="alexis-baker-ad-quirinum-book-three",
        author="Andy Alexis-Baker",
        work="'Ad Quirinum Book Three and Cyprian's Catechumenate,' Journal of Early Christian "
             "Studies 17.3 (2009): 357-380",
        edition="JECS, 2009 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- the catechumenate-specific use of row 5 "
             "(Ad Quirinum), alongside row 34's more general Fahey study of the same text.",
    ),
    dict(
        row=120, slug="burns-situating-and-studying-augustines-sermons",
        author="J. Patout Burns",
        work="'Situating and Studying Augustine's Sermons,' Journal of Early Christian Studies 26.2 "
             "(2018): 307-322",
        edition="JECS, 2018 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim. "
                   "A third, distinct Burns work from rows 32-33 -- a review-essay on Augustine's own "
                   "sermon-dating methodology.",
        body="Licensed for row 19 and the liturgical-evidence gap Doc_02 SS5/SS9 item 9 already "
             "discloses.",
    ),
    dict(
        row=121, slug="cameron-valerius-of-hippo-a-profile",
        author="Michael Cameron",
        work="'Valerius of Hippo: A Profile,' Augustinian Studies 40.1 (2009): 5-26",
        edition="Augustinian Studies, 2009 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A different, later Cameron work from row 102's own study of Augustine's "
                   "exegesis.",
        body="Licensed for row 11 directly -- Valerius is quoted directly at Doc_01 SS5/SS9 and Doc_02 "
             "SS2 (Letter XXXI SS4), but no row previously licensed any secondary study of him at all.",
    ),
    dict(
        row=122, slug="gillette-augustine-and-perpetuas-words",
        author="Gertrude Gillette",
        work="'Augustine and the Significance of Perpetua's Words: \"And I Was a Man,\"' "
             "Augustinian Studies 32.1 (2001): 115-126",
        edition="Augustinian Studies, 2001 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. Augustine's own Sermons 280-281 on Perpetua and Felicitas are native, "
                   "in-boundary preaching material -- distinct from the Passion of Perpetua itself, "
                   "which predates this world's own c. 246 start (the same ground row 28 is excluded "
                   "on).",
        body="Licensed for Doc_02 SS6's own Article 20/gender discussion -- a further data point "
             "alongside Albina/CCXI that SS6 does not currently name.",
    ),
    dict(
        row=123, slug="lambot-les-manuscrits-des-sermons-de-saint-augustin",
        author="Cyrille Lambot",
        work="'Les manuscrits des sermons de saint Augustin utilisés par les Mauristes,' Revue "
             "Bénédictine 79 (1969): 98-114",
        edition="Revue Bénédictine, 1969 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 19 -- the manuscript-transmission study behind the vendored NPNF "
             "sermon translation, the same gap row 89 (von Soden) closes for Cyprian's letters, "
             "applied here to Augustine's sermons.",
    ),
    dict(
        row=124, slug="chapman-les-interpolations-dans-le-traite-de-unitate",
        author="John Chapman",
        work="'Les interpolations dans le traité de S. Cyprien sur l'Unité de l'Église,' Revue "
             "Bénédictine 19 (1902): 246-254, 357-373; 20 (1903): 26-51",
        edition="Revue Bénédictine, 1902-1903 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Contested",
        divergence="Flagged for priority second-opinion review before it supports any specific claim. "
                   "The foundational study that first identified and argued the two-recension "
                   "interpolation thesis row 3 carries as its own open question -- seven decades "
                   "before Bévenot's own critical edition (row 51).",
        body="Licensed for row 3's own open two-recension ('Primacy Text') question.",
    ),
    dict(
        row=125, slug="cross-livingstone-oxford-dictionary-christian-church",
        author="F. L. Cross and E. A. Livingstone (editors)",
        work="The Oxford Dictionary of the Christian Church, 3rd ed. (Oxford: Oxford University "
             "Press, 1997)",
        edition="Oxford University Press, 1997 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Cross and Livingstone as editors",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- a further general reference instrument "
             "alongside row 52 (Fitzgerald's Augustine through the Ages) and row 57 (Dekkers's "
             "Clavis).",
    ),
    dict(
        row=126, slug="gaumer-augustines-cyprian",
        author="Matthew Alan Gaumer",
        work="Augustine's Cyprian: Authority in Roman Africa, Brill's Series in Church History 73 "
             "(Leiden: Brill, 2016)",
        edition="Brill, 2016 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for Doc_01 SS8 item 10 and Doc_02 SS2's Transmission History entry for Cyprian "
             "-- the book-length modern study of Augustine devising his own authority in continuous, "
             "contested dialogue with Cyprian's own.",
    ),
    dict(
        row=127, slug="hollingworth-saint-augustine-of-hippo-intellectual-biography",
        author="Miles Hollingworth",
        work="Saint Augustine of Hippo: An Intellectual Biography (Oxford: Oxford University Press, "
             "2013)",
        edition="Oxford University Press, 2013 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Native, unlicensed, on the same footing as row 87 (Chadwick), for the same "
                   "reason.",
        body="Not currently licensed for any specific claim -- a further single-author modern "
             "Augustine biography relying primarily on the Confessions, redundant with rows 30 "
             "(Brown) and 31 (Lancel).",
    ),
    dict(
        row=129, slug="duval-caillet-eglises-doubles-hippo",
        author="Noël Duval and Jean-Pierre Caillet (editors)",
        work="'Les églises doubles et les familles d'églises,' Antiquité Tardive 4 (1996), incl. its "
             "own North Africa/Hippo Regius dossier",
        edition="Antiquité Tardive, 1996 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim. "
                   "This Noël Duval is checked and distinct from row 60's own Yvette Duval and row "
                   "170's own Yves-Marie Duval.",
        body="Licensed for row 38, alongside rows 63 and 82 -- the double-church question for North "
             "Africa specifically.",
    ),
    dict(
        row=130, slug="boodts-navigating-augustines-sermons",
        author="Shari Boodts",
        work="'Navigating the Vast Tradition of St. Augustine's Sermons: Old Instruments and New "
             "Approaches,' Augustiniana 69.1 (2019): 83-115",
        edition="Augustiniana, 2019 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 19/106 -- a modern methodological survey of the sermon corpus's own "
             "transmission, alongside row 123 (Lambot).",
    ),
    dict(
        row=131, slug="yates-augustinian-concupiscence-pre-augustinian",
        author="Jonathan P. Yates",
        work="'Was There \"Augustinian\" Concupiscence in Pre-Augustinian North Africa?' "
             "Augustiniana 51.1/2 (2001): 39-56",
        edition="Augustiniana, 2001 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- the pre-Augustinian North African "
             "theological background the anti-Pelagian/original-sin corpus named at Doc_02 SS1 "
             "inherits.",
    ),
    dict(
        row=132, slug="villegas-marin-legimus-supra-magistrum",
        author="Raúl Villegas Marín",
        work="'Legimus supra magistrum non esse discipulum: Pope Celestine I, the \"Augustinian "
             "Controversy,\" and the Clerical Cursus Honorum,' Sacris Erudiri 58 (2019): 305-320",
        edition="Sacris Erudiri, 2019 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. Celestine I's own pontificate falls squarely within Augustine's own later "
                   "episcopate.",
        body="Licensed for the Apiarius-affair material at Doc_02 SS1/row 26.",
    ),
    dict(
        row=133, slug="lagouanere-notion-de-prochain-dolbeau-11",
        author="Jérôme Lagouanère",
        work="'La notion de prochain d'Augustin au début de son épiscopat: le rôle matriciel du "
             "sermon De dilectione Dei et proximi (Sermon Dolbeau 11),' Sacris Erudiri 54 (2015)",
        edition="Sacris Erudiri, 2015 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 19/50 -- a study of a specific Dolbeau sermon from the corpus rows "
             "49-50 already discuss.",
    ),
    dict(
        row=134, slug="bibliographia-patristica",
        author="Successive editors (De Gruyter)",
        work="Bibliographia Patristica: Internationale Patristische Bibliographie (Berlin: De "
             "Gruyter, 1956-1997)",
        edition="De Gruyter, 1956-1997 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed to the successive series editors",
        discovery="WebSearch / 2026-09-02.",
        cite="D", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. The bibliography itself ceased publication in 1997 "
                   "and cannot be consulted for anything after that date.",
        body="Not currently licensed for a specific claim -- a reference instrument alongside row 57 "
             "(Dekkers's Clavis), named for completeness.",
    ),
    dict(
        row=135, slug="leone-christianity-and-paganism-north-africa",
        author="Anna Leone",
        work="'Christianity and Paganism, IV: North Africa,' ch. 9 in The Cambridge History of "
             "Christianity, Vol. 2: Constantine to c.600, eds. Casiday and Norris (Cambridge: "
             "Cambridge University Press, 2007), 231-247",
        edition="Cambridge University Press, 2007 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for Doc_02 SS5's own 'Surrounding cultural and religious environment' "
             "paragraph directly -- a modern synthesis on the Christianity/paganism-in-North-Africa "
             "question that paragraph raises but cites no specific instrument for.",
    ),
    dict(
        row=136, slug="lannee-epigraphique",
        author="Successive editors (Presses Universitaires de France)",
        work="L'Année épigraphique (Paris: Presses Universitaires de France, 1888- )",
        edition="PUF, 1888- -- in copyright, ongoing, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed to the successive series editors",
        discovery="WebSearch / 2026-09-02.",
        cite="D", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. An ongoing series with no single completion date.",
        body="Licensed for row 37 directly -- the standing modern successor instrument to CIL VIII, "
             "covering inscriptions published in the 140-plus years CIL VIII's own nineteenth-century "
             "compilation date cannot capture.",
    ),
    dict(
        row=137, slug="chabi-augustines-eucharistic-spirituality",
        author="Kolawole Chabi",
        work="'Augustine's Eucharistic Spirituality in his Easter Sermons,' Augustinianum 59.2 "
             "(2019): 475-504",
        edition="Augustinianum, 2019 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for Doc_02 SS5's own liturgical-evidence paragraph and SS9 item 9 directly -- a "
             "study of Augustine's own Easter preaching specifically as Eucharistic/liturgical "
             "evidence.",
    ),
    dict(
        row=138, slug="di-berardino-encyclopedia-of-the-early-church",
        author="Angelo Di Berardino (editor)",
        work="Encyclopedia of the Early Church, trans. Adrian Walford, 2 vols. (Cambridge: James "
             "Clarke & Co., 1992)",
        edition="James Clarke & Co., 1992 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Di Berardino as editor, Walford as translator",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- a further general reference instrument "
             "alongside row 52 (Fitzgerald) and row 57 (Dekkers).",
    ),
    dict(
        row=139, slug="brown-augustines-appropriation-of-cyprians-tropes",
        author="Phillip Brown",
        work="'Augustine's Appropriation of Cyprian's Unitive Tropes from De Ecclesiae Catholicae "
             "Unitate within his In Iohannis Euangelium Tractatus 1-16,' Studia Patristica CXVIII "
             "(Papers of the Eighteenth International Conference on Patristic Studies, Oxford 2019, "
             "Vol. 15: Augustine and his Writings) (Leuven: Peeters)",
        edition="Peeters -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not a "
                "vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 13's own Book III ch. 2 SS2 patrimony material -- a modern study of "
             "Augustine's own direct textual reuse of Cyprian's De Unitate language.",
    ),
    dict(
        row=140, slug="godoy-orthodoxy-heresy-episcopal-authority",
        author="Victor A. Godoy",
        work="'Orthodoxy, Heresy and Episcopal Authority in the Third-Century Church: The Debates "
             "between Cyprian of Carthage, the Laxist and the Rigorist Clergy,' Studia Patristica C "
             "(Papers of the Sixth British Patristics Conference, Birmingham, 2016) (Leuven: "
             "Peeters)",
        edition="Peeters -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not a "
                "vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- the laxist-rigorist clergy dispute "
             "Cyprian's own letters document, adjacent to the lapsed/Felicissimus material at Doc_01 "
             "SS2-3 and rows 1-2.",
    ),
    dict(
        row=141, slug="esquivel-penance-and-ecclesial-purity",
        author="Matthew Esquivel",
        work="'Penance and Ecclesial Purity: The Divine Urgency Behind Cyprian's Response to the "
             "Decian Persecution,' Studia Patristica CXXVI (Oxford 2019 proceedings) (Leuven: "
             "Peeters)",
        edition="Peeters -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not a "
                "vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for the lapsed-reconciliation gravity, Doc_01 SS3 and row 2 (De Lapsis) "
             "directly.",
    ),
    dict(
        row=142, slug="gassman-late-antique-preacher-in-action-ep29",
        author="M. Gassman",
        work="'A Late Antique Preacher in Action: Augustine, Ep. 29,' Journal of Late Antiquity 15.1 "
             "(Spring 2022)",
        edition="Journal of Late Antiquity, 2022 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. A study of one specific, dated preaching episode.",
        body="Not currently licensed for a specific claim -- rows 15-16's catechetical/preaching "
             "material and Doc_02 SS1.",
    ),
    dict(
        row=143, slug="shaw-augustine-and-men-of-imperial-power",
        author="Brent D. Shaw",
        work="'Augustine and Men of Imperial Power,' Journal of Late Antiquity 8.1 (Spring 2015): "
             "32-61",
        edition="Journal of Late Antiquity, 2015 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A second, distinct Shaw work from row 36, on Augustine's own relations "
                   "with imperial officials by name.",
        body="Licensed for row 12/43's state-power material.",
    ),
    dict(
        row=144, slug="leppin-bischofsmartyrium-als-stellvertretung",
        author="Volker Leppin",
        work="'Das Bischofsmartyrium als Stellvertretung bei Cyprian von Karthago,' Zeitschrift für "
             "Antikes Christentum / Journal of Ancient Christianity 4.2 (2000): 255-269",
        edition="ZAC, 2000 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not "
                "a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 7 and Doc_02 SS4's Pontius/martyrdom-as-representation Author Gravity "
             "material.",
    ),
    dict(
        row=145, slug="engberg-education-self-affirmation-ad-donatum",
        author="Jakob Engberg",
        work="'The education and (self-)affirmation of (recent or potential) converts: the case of "
             "Cyprian and the Ad Donatum,' Zeitschrift für Antikes Christentum 16 (2012): 129-144",
        edition="ZAC, 2012 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not "
                "a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 5, Cyprian's own Ad Donatum conversion narrative.",
    ),
    dict(
        row=146, slug="noel-duval-notes-depigraphie-chretienne-africaine",
        author="Noël Duval",
        work="'Notes d'épigraphie chrétienne africaine,' Karthago: Revue d'archéologie africaine "
             "VII (Paris: Klincksieck, 1958)",
        edition="Klincksieck, 1958 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="D", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. This Noël Duval is checked and distinct from row 60's Yvette Duval, row "
                   "129's own different 1996 article by the same Noël Duval on a different subject, "
                   "and row 170's Yves-Marie Duval.",
        body="Licensed for row 37/38's African-epigraphy material, alongside row 60 and row 136.",
    ),
    dict(
        row=147, slug="howard-vandal-occupation-of-hippo-regius",
        author="E. C. Howard",
        work="'A Note on the Vandal Occupation of Hippo Regius,' The Journal of Roman Studies 14 "
             "(1924): 257-258",
        edition="JRS, 1924 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not "
                "a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="D", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Old scholarship (1924), superseded on some points; named for completeness rather "
                   "than as a current-standard citation.",
        body="Licensed for Source_Acquisition_Manifest.md G3 (Possidius) and the Megalius/primate-"
             "of-Numidia geographic question Doc_01 SS5/SS9 already discloses as resting on an "
             "unvendored source.",
    ),
    dict(
        row=148, slug="millar-local-cultures-in-the-roman-empire",
        author="Fergus Millar",
        work="'Local Cultures in the Roman Empire: Libyan, Punic and Latin in Roman Africa,' The "
             "Journal of Roman Studies 58 (1968): 126-151",
        edition="JRS, 1968 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not "
                "a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for Doc_02 SS5/SS6's own named, still-open Punic/Berber substrate-culture "
             "question directly -- the single most-cited modern study of the linguistic-cultural "
             "question that open item turns on.",
    ),
    dict(
        row=149, slug="smither-pastoral-lessons-augustine-women",
        author="Edward L. Smither",
        work="'Pastoral lessons from Augustine's theological correspondence with women,' HTS "
             "Teologiese Studies / Theological Studies 72.4 (2016)",
        edition="HTS Teologiese Studies, 2016 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. The sharpest of Round 11's three PRESS answers -- closes the gender-data-"
                   "point gap Round 11's own M1 finding named at Doc_02 SS6.",
        body="Licensed for Doc_02 SS6's own Gender/Article 20 discussion directly -- a survey of "
             "Augustine's own theological correspondence with fifteen different named women, of "
             "which SS6 currently names three (Albina, the Nuns of Hippo, and Sermons 280-281 on "
             "Perpetua and Felicitas).",
    ),
    dict(
        row=150, slug="taylor-cyprian-reconciliation-of-apostates",
        author="John Hammond Taylor",
        work="'St. Cyprian and the Reconciliation of Apostates,' Theological Studies 3.1 (Fall "
             "1942): 27-46",
        edition="Theological Studies, 1942 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 1's own 'your suffrage and God's judgment' material and the "
             "lapsed-controversy gravity, Doc_01 SS2-3 directly -- the libelli pacis mechanism "
             "Cyprian's own letters document him resisting and regularizing, which no current row "
             "addresses directly.",
    ),
    dict(
        row=151, slug="hudson-cyprianic-ecclesiology-thesis",
        author="Lauren Hudson",
        work="'Cyprianic Ecclesiology: Redefining the Office of the Christian Bishop' (M.A. thesis, "
             "Georgia Southern University, 2013)",
        edition="Georgia Southern University, 2013 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="D", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Named because it is real and checkable, not because it is strong -- flagged "
                   "explicitly as a graduate thesis rather than a peer-reviewed monograph or journal "
                   "article, the weakest lead of this round's own three PRESS answers. A build "
                   "thread may reasonably decline this candidate in favor of a stronger instrument on "
                   "the same question.",
        body="Licensed, if drawn on, for Cyprian's own 'neophyte bishop' controversy (the charge, "
             "from the five opposing presbyters named at row 1, that his rapid rise from recent "
             "convert to bishop lacked legitimacy).",
    ),
    dict(
        row=152, slug="fredouille-lhumanite-vue-den-haut",
        author="Jean-Claude Fredouille",
        work="'L'Humanité vue d'en haut (Cyprien, Ad Donatum, 6-13),' Vigiliae Christianae 64 "
             "(2010): 445-455",
        edition="Vigiliae Christianae, 2010 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Contested",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A close study bearing on row 3's own open two-recension/influence "
                   "question at Doc_02 SS2.",
        body="Licensed for row 3's own two-recension/influence question at Doc_02 SS2.",
    ),
    dict(
        row=153, slug="murphy-as-far-as-my-poor-memory-suggested",
        author="Edwina Murphy",
        work="\"'As far as my poor memory suggested': Cyprian's compilation of Ad Quirinum,\" "
             "Vigiliae Christianae 68 (2014): 533-550",
        edition="Vigiliae Christianae, 2014 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 5's Ad Quirinum material -- the testimonia collection's own "
             "compilation history.",
    ),
    dict(
        row=154, slug="amidon-procedure-of-cyprians-synods",
        author="Philip R. Amidon",
        work="'The Procedure of St. Cyprian's Synods,' Vigiliae Christianae 37.4 (1983): 328-339",
        edition="Vigiliae Christianae, 1983 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 4's own conciliar-authority material directly -- how Cyprian's synods "
             "actually ran procedurally, the mechanism behind the 256 preface's own words.",
    ),
    dict(
        row=155, slug="van-oort-young-augustines-knowledge-of-manichaeism",
        author="Johannes van Oort",
        work="'The young Augustine's knowledge of Manichaeism: An analysis of the Confessiones and "
             "some other relevant texts,' Vigiliae Christianae 62 (2008): 441-466",
        edition="Vigiliae Christianae, 2008 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 22's anti-Manichaean corpus and Doc_01 SS6's own gravity candidate on "
             "Augustine's Manichaean decade.",
    ),
    dict(
        row=156, slug="gassman-cyprians-early-career",
        author="Mattias Gassman",
        work="'Cyprian's Early Career in the Church of Carthage,' Journal of Ecclesiastical History "
             "70.1 (2019): 1-17",
        edition="JEH, 2019 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); not "
                "a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A second, distinct Gassman work from row 142, on Cyprian's own "
                   "under-documented early episcopate.",
        body="Licensed for Doc_02 SS2's Cyprian Visibility entry.",
    ),
    dict(
        row=157, slug="dunn-white-crown-of-works",
        author="Geoffrey D. Dunn",
        work="'The White Crown of Works: Cyprian's Early Pastoral Ministry of Almsgiving in "
             "Carthage,' Church History 73.4 (2004): 715-740",
        edition="Church History, 2004 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A third, distinct Dunn work from rows 77/112.",
        body="Licensed for row 5's own almsgiving/pastoral material and Doc_02 SS2's Visibility "
             "entry.",
    ),
    dict(
        row=158, slug="clarke-secular-profession-of-cyprian",
        author="G. W. Clarke",
        work="'The Secular Profession of St Cyprian of Carthage,' Latomus 24.3 (1965): 633-638",
        edition="Latomus, 1965 -- in copyright, never vendored (Source_Acquisition_Manifest.md "
                "SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A second, distinct Clarke work from row 46's own ACW translation.",
        body="Licensed for Doc_01 SS2's own beginning-point discussion -- Cyprian's own "
             "pre-conversion rhetorical career.",
    ),
    dict(
        row=159, slug="delehaye-cyprien-dantioche-et-cyprien-de-carthage",
        author="Hippolyte Delehaye",
        work="'Cyprien d'Antioche et Cyprien de Carthage,' Analecta Bollandiana 39 (1921): 314-332",
        edition="Analecta Bollandiana, 1921 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="D", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="A second, distinct Delehaye work from row 99, this one an article rather than "
                   "the monograph.",
        body="Licensed for SS4's Pontius/genre-risk material -- the hagiographic conflation of "
             "'Cyprian of Antioch,' the legendary magician-saint, with this world's own Cyprian of "
             "Carthage.",
    ),
    dict(
        row=160, slug="kotze-reading-psalm-4-to-the-manichaeans",
        author="Annemaré Kotzé",
        work="'Reading Psalm 4 to the Manichaeans,' Vigiliae Christianae 55 (2001): 119-136",
        edition="Vigiliae Christianae, 2001 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. A closer reading of one specific Augustine "
                   "anti-Manichaean text, alongside row 155 for the Manichaean-auditor gap.",
        body="Not currently licensed for a specific claim.",
    ),
    dict(
        row=161, slug="finn-dupont-preaching-adam",
        author="Douglas E. Finn and Anthony Dupont",
        work="'Preaching Adam in John Chrysostom and Augustine of Hippo,' Vigiliae Christianae 73.2 "
             "(2019): 190-217",
        edition="Vigiliae Christianae, 2019 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. A different Finn from row 190's own Thomas M. Finn, "
                   "checked and distinguished.",
        body="Not currently licensed for a specific claim -- Doc_02 SS1's sermon material and the "
             "anti-Pelagian corpus, a comparative study useful for Doc_03's own vocabulary-drawing "
             "instruction.",
    ),
    dict(
        row=162, slug="ferguson-baptism-in-the-early-church",
        author="Everett Ferguson",
        work="Baptism in the Early Church: History, Theology, and Liturgy in the First Five "
             "Centuries (Grand Rapids: Eerdmans, 2009)",
        edition="Eerdmans, 2009 -- in copyright, never vendored (Source_Acquisition_Manifest.md "
                "SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for the liturgical-evidence gap Doc_02 SS5 and SS9 item 9 both explicitly "
             "name -- the standard modern reference covering exactly this world's own span for "
             "baptismal theology, rite, and practice, treating Cyprian's own rebaptism controversy "
             "directly.",
    ),
    dict(
        row=163, slug="odonnell-augustine-a-new-biography",
        author="James J. O'Donnell",
        work="Augustine: A New Biography (New York: Ecco/HarperCollins, 2005; published in the UK "
             "as Augustine, Sinner and Saint, London: Profile Books, 2005)",
        edition="Ecco/HarperCollins, 2005 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. A distinct work from row 53's own O'Donnell critical "
                   "Confessions commentary, by the same author.",
        body="Not currently licensed for a specific claim -- general biographical framing alongside "
             "rows 30 (Brown) and 31 (Lancel).",
    ),
    dict(
        row=164, slug="humfress-orthodoxy-and-the-courts",
        author="Caroline Humfress",
        work="Orthodoxy and the Courts in Late Antiquity (Oxford: Oxford University Press, 2007)",
        edition="Oxford University Press, 2007 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 12's imperial-coercion material and rows 44/88's Codex Theodosianus "
             "entries -- the standard modern legal-historical study of how late-antique ecclesiastical "
             "and civil courts actually interacted.",
    ),
    dict(
        row=165, slug="dupont-original-sin-in-tertullian-and-cyprian",
        author="Anthony Dupont",
        work="'Original Sin in Tertullian and Cyprian: Conceptual Presence and Pre-Augustinian "
             "Content?' Revue des Études Augustiniennes et Patristiques 63.1 (2017): 1-29",
        edition="REAP, 2017 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for Doc_01 SS7's own Tertullian-forging claim and Doc_02 SS2's own "
             "Cyprian-Tertullian dependency discussion.",
    ),
    dict(
        row=166, slug="courcelle-possidius-et-les-confessions",
        author="Pierre Courcelle",
        work="'Possidius et les \"Confessions\" de saint Augustin,' Recherches de Science "
             "Religieuse 39 (1951): 428-442 (Mélanges Jules Lebreton II)",
        edition="Recherches de Science Religieuse, 1951 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A second, distinct Courcelle work from row 96.",
        body="Licensed for Source_Acquisition_Manifest.md G3 and Doc_02 SS4/SS9 item 1's own "
             "formation-narrative gap -- the earliest scholarly treatment of how Possidius's own "
             "Vita relates to the Confessions (row 9).",
    ),
    dict(
        row=167, slug="christol-notables-et-chretiens",
        author="Michel Christol",
        work="'Notables et chrétiens: les enseignements des Lettres de Cyprien de Carthage,' "
             "Cahiers du Centre Gustave Glotz 27 (2016): 361-376",
        edition="Cahiers du Centre Gustave Glotz, 2016 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 1's own election language and Doc_02 SS2's Representativeness entry -- "
             "a prosopographical study of the notables named in Cyprian's own letters.",
    ),
    dict(
        row=168, slug="methuen-firmilian-and-the-doubtful-baptisms",
        author="Charlotte Methuen",
        work="\"'The very deceitfulness of devils': Firmilian and the doubtful baptisms of a woman "
             "possessed by demons,\" Studies in Church History 52 (2016): 49-64",
        edition="Studies in Church History, 2016 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 1's own Firmilian material -- the only secondary-scholarship treatment "
             "of that letter this Registry holds.",
    ),
    dict(
        row=169, slug="demoustier-ontologie-de-leglise-selon-cyprien",
        author="A. Demoustier",
        work="'L'ontologie de l'Église selon saint Cyprien,' Recherches de Science Religieuse 52.4 "
             "(1964): 554-588",
        edition="Recherches de Science Religieuse, 1964 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 4's own conciliar-authority material and Doc_02 SS2's Influence entry "
             "-- a foundational modern study of Cyprian's own ecclesiology.",
    ),
    dict(
        row=170, slug="yves-marie-duval-cyprien-chez-ambroise",
        author="Yves-Marie Duval",
        work="'Sur une page de saint Cyprien chez saint Ambroise. Hexameron, 6, 8, 47 et De habitu "
             "virginum, 15-17,' Revue des Études Augustiniennes 16 (1970): 25-34",
        edition="REA, 1970 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A third, distinct Duval, checked against and unrelated to row 60 (Yvette "
                   "Duval) and rows 129/146 (Noël Duval).",
        body="Licensed for row 5's own On the Dress of Virgins material -- a study of Cyprian's own "
             "reception in Ambrose specifically on that treatise.",
    ),
    dict(
        row=171, slug="marin-agostino-celebra-i-martiri-scillitani",
        author="Marcello Marin",
        work="'Agostino celebra i martiri Scillitani: il sermo 299/D,' Vetera Christianorum 19 "
             "(1982): 341-360",
        edition="Vetera Christianorum, 1982 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02; verified absent / direct XML check / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="A possible further primary-source candidate (Augustine's own Sermon 299/D, on "
                   "the pre-boundary Scillitan Martyrs) -- CHECKED DIRECTLY: Sermon 299/D is confirmed "
                   "absent from this world's vendored NPNF corpus (row 19's own file contains exactly "
                   "97 sermons, I-XCVII; no '299' or 'CCXCIX' reference anywhere) and from the corpus "
                   "map. Row 189 (Morin's 1930 critical edition) names where the primary text would "
                   "have to come from if this world's construction ever needs it. Flagged for "
                   "priority second-opinion review before it supports any specific claim.",
        body="Licensed alongside row 122 for SS6's own gender/Article-20 material -- a possible "
             "further primary-source candidate, now confirmed absent from this world's own vendored "
             "corpus.",
    ),
    dict(
        row=172, slug="veronese-cipriano-di-cartagine-in-oriente",
        author="Maria Veronese",
        work="'Πρῶτος τῶν τότε Κυπριανός. Cipriano di Cartagine in Oriente,' Vetera Christianorum "
             "43 (2006): 245-265",
        edition="Vetera Christianorum, 2006 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for Doc_02 SS2's own Transmission History entry for Cyprian -- his own "
             "reception in the Greek East.",
    ),
    dict(
        row=173, slug="dunn-cyprian-episcopal-synod-of-late-254",
        author="Geoffrey D. Dunn",
        work="'Cyprian of Carthage and the Episcopal Synod of Late 254,' Revue des Études "
             "Augustiniennes 48 (2002): 229-247",
        edition="REA, 2002 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A fourth, distinct Dunn work, from rows 77, 112, and 157.",
        body="Licensed for row 4's own conciliar material.",
    ),
    dict(
        row=174, slug="casias-women-in-late-antique-north-africa",
        author="Cassandra M. M. Casias",
        work="'Women in Late Antique North Africa (in the Writings of Augustine and Other Church "
             "Fathers),' Oxford Research Encyclopedia of African History (Oxford University Press, "
             "online 15 September 2022)",
        edition="Oxford University Press, 2022 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for SS6's own Gender/Article 20 discharge -- a modern reference-encyclopedia "
             "synthesis of women's status across the corpus this world already draws on.",
    ),
    dict(
        row=175, slug="fiedrowicz-psalmus-vox-totius-christi",
        author="Michael Fiedrowicz",
        work="Psalmus vox totius Christi: Studien zu Augustins \"Enarrationes in Psalmos\" "
             "(Freiburg/Basel/Vienna: Herder, 1997)",
        edition="Herder, 1997 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 20 directly -- the ~695,000-word Enarrationes, this Registry's "
             "largest single body, currently carries no dedicated secondary study of any kind.",
    ),
    dict(
        row=176, slug="bonner-st-augustine-of-hippo-life-and-controversies",
        author="Gerald Bonner",
        work="St Augustine of Hippo: Life and Controversies (London: SCM Press, 1963; rev. ed. "
             "Norwich: Canterbury Press, 1986; further reprint 2002)",
        edition="SCM Press / Canterbury Press, 1963/1986/2002 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. A fourth modern Augustine biography alongside rows 30 "
                   "(Brown), 31 (Lancel), and 163 (O'Donnell).",
        body="Not currently licensed for a specific claim.",
    ),
    dict(
        row=177, slug="harper-the-fate-of-rome",
        author="Kyle Harper",
        work="The Fate of Rome: Climate, Disease, and the End of an Empire, The Princeton History of "
             "the Ancient World (Princeton: Princeton University Press, 2017)",
        edition="Princeton University Press, 2017 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 5's own De Mortalitate material and Doc_01's own epidemic gravity -- "
             "the modern historical study of the epidemiological/environmental context of the "
             "'Plague of Cyprian.'",
    ),
    dict(
        row=178, slug="van-den-eynde-double-edition-de-unitate",
        author="D. van den Eynde",
        work="'La double édition du De unitate de S. Cyprien,' Revue d'Histoire Ecclésiastique 29 "
             "(1933): 5-24",
        edition="RHE, 1933 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Contested",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. The original scholarly identification of the textual problem row 51's "
                   "edition is cited to resolve.",
        body="Licensed for row 3's own two-recension question and row 51's own Bévenot-edition "
             "Licensed-For.",
    ),
    dict(
        row=179, slug="huebner-plague-of-cyprian-revised-view",
        author="Sabine R. Huebner",
        work="\"The 'Plague of Cyprian': A revised view of the origin and spread of a 3rd-c. CE "
             "pandemic,\" Journal of Roman Archaeology 34.1 (2021): 151-174",
        edition="JRA, 2021 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A revising counter-view to row 177's own framing, not a duplicate of it.",
        body="Licensed alongside row 177 (Harper) for Doc_02 SS1's De Mortalitate/plague material and "
             "Doc_01's own epidemic gravity candidate.",
    ),
    dict(
        row=180, slug="saumagne-saint-cyprien-pape-dafrique",
        author="Charles Saumagne",
        work="Saint Cyprien, évêque de Carthage, \"Pape\" d'Afrique (248-258): Contribution à "
             "l'étude des \"persécutions\" de Dèce et de Valérien, Études d'Antiquités Africaines "
             "(Paris: Éditions du CNRS, 1975)",
        edition="Éditions du CNRS, 1975 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for Doc_01 SS2/SS3's own Decian/Valerianic persecution material and Doc_02 "
             "SS2's Cyprian Visibility entry -- a book-length study of exactly Cyprian's own "
             "persecution-era episcopate.",
    ),
    dict(
        row=181, slug="schindler-augustin-augustinismus",
        author="Alfred Schindler",
        work="'Augustin/Augustinismus,' Theologische Realenzyklopädie, Band 4 (Berlin: De Gruyter, "
             "1979), 646-698",
        edition="De Gruyter, 1979 -- in copyright, never vendored (Source_Acquisition_Manifest.md "
                "SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- a synthetic reference-encyclopedia "
             "treatment of Augustine's whole career and reception, licensed generally for Doc_02 "
             "SS2's own Augustine Author Gravity entries.",
    ),
    dict(
        row=182, slug="rebillard-augustine-oxford-bibliographies",
        author="Éric Rebillard",
        work="Augustine: Oxford Bibliographies Online Research Guide (Oxford: Oxford University "
             "Press, 2010)",
        edition="Oxford University Press, 2010 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. A different Rebillard work from row 35, a different "
                   "genre.",
        body="Not currently licensed for a specific claim -- general bibliographic orientation.",
    ),
    dict(
        row=183, slug="markschies-cyprianus-new-pauly",
        author="Christoph Markschies",
        work="'Cyprianus,' Brill's New Pauly (Leiden: Brill, online)",
        edition="Brill, online -- in copyright, never vendored (Source_Acquisition_Manifest.md "
                "SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked.",
        body="Not currently licensed for a specific claim -- a concise modern reference-encyclopedia "
             "synthesis, licensed generally for Doc_02 SS2's own Cyprian entries.",
    ),
    dict(
        row=184, slug="teske-augustine-st-new-catholic-encyclopedia",
        author="R. J. Teske",
        work="'Augustine, St.,' New Catholic Encyclopedia, 2nd ed., vol. 1 (Detroit: Gale/Catholic "
             "University of America, 2003)",
        edition="Gale/Catholic University of America, 2003 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="Not independently checked. A different Teske work from row 73's own translation "
                   "credit.",
        body="Not currently licensed for a specific claim -- licensed generally for Doc_02 SS2's own "
             "Augustine entries.",
    ),
    dict(
        row=185, slug="hunter-from-rigor-to-reconciliation",
        author="David G. Hunter",
        work="'From Rigor to Reconciliation: Cyprian of Carthage on Changing Penitential Practice,' "
             "in Changing the Church: Transformations of Christian Belief, Practice, and Life, eds. "
             "Mark D. Chapman and Vladimir Latinovic (Cham: Palgrave Macmillan, 2021), 13-20",
        edition="Palgrave Macmillan, 2021 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 2's own De Lapsis/lapsed-reconciliation gravity material -- a recent, "
             "focused treatment of Cyprian's own penitential-practice development.",
    ),
    dict(
        row=186, slug="norton-episcopal-elections-250-600",
        author="Peter Norton",
        work="Episcopal Elections 250-600: Hierarchy and Popular Will in Late Antiquity, Oxford "
             "Classical Monographs (Oxford: Oxford University Press/Clarendon Press, 2007)",
        edition="Oxford University Press/Clarendon Press, 2007 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific claim.",
        body="Licensed for row 1's own election language ('your suffrage and God's judgment') and "
             "Doc_02 SS2's Representativeness discussion -- a book-length modern study of episcopal "
             "elections spanning exactly Cyprian's own century onward.",
    ),
    dict(
        row=187, slug="bevenot-cyprian-von-karthago-tre",
        author="Maurice Bévenot",
        work="'Cyprian von Karthago,' Theologische Realenzyklopädie, Band VIII (Berlin/New York: De "
             "Gruyter, 1981), 246-254",
        edition="De Gruyter, 1981 -- in copyright, never vendored (Source_Acquisition_Manifest.md "
                "SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A later, encyclopedia-format work by row 51's own editor.",
        body="Licensed alongside row 178 and rows 3/51 for the same De Unitate question.",
    ),
    dict(
        row=188, slug="laporte-hippone-la-vraie-basilique",
        author="Jean-Pierre Laporte",
        work="'Hippone: à la recherche de la (vraie) basilique de saint Augustin,' Revue d'Études "
             "Augustiniennes et Patristiques 61 (2015): 299-324",
        edition="REAP, 2015 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Contested",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. The specific, sharpest modern challenge to row 63 (Marec, 1958)'s own "
                   "identification of the Hippo Regius basilica, proposing an alternative location.",
        body="Licensed against row 63 (Marec) and Doc_02 SS5's own basilica-archaeology material "
             "directly.",
    ),
    dict(
        row=189, slug="morin-sermones-post-maurinos-reperti",
        author="Germain Morin (editor); Augustine of Hippo (author)",
        work="Sancti Augustini sermones post Maurinos reperti, in Miscellanea Agostiniana, vol. 1 "
             "(Rome: Tipografia Poliglotta Vaticana, 1930)",
        edition="Tipografia Poliglotta Vaticana, 1930 -- in copyright, never vendored "
                "(Source_Acquisition_Manifest.md SS3); not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY,
        attribution="attributed to Morin as editor, Augustine as author",
        discovery="WebSearch / 2026-09-02.",
        cite="D", verif="named-not-rechecked", weight="illustrative", formation="Widely Accepted",
        divergence="A direct check this round confirmed Sermon 299/D (row 171's own candidate) is not "
                   "present in this world's vendored NPNF corpus or the corpus map; this row names "
                   "where the primary text would have to come from if this world's construction ever "
                   "needs it.",
        body="Licensed for row 171's own open verification question and alongside rows 49-50 "
             "(Divjak, Dolbeau) as a further completeness qualifier on rows 11 and 19 -- the critical "
             "edition in which Augustine's post-Maurist sermons were first collected and published.",
    ),
    dict(
        row=190, slug="finn-it-happened-one-saturday-night",
        author="Thomas M. Finn",
        work="'It Happened One Saturday Night: Ritual and Conversion in Augustine's North Africa,' "
             "Journal of the American Academy of Religion LVIII/4 (Winter 1990): 589-616",
        edition="JAAR, 1990 -- in copyright, never vendored (Source_Acquisition_Manifest.md SS3); "
                "not a vendoring candidate",
        rights=RIGHTS_CONSULTATION_ONLY, attribution="attributed",
        discovery="WebSearch / 2026-09-02.",
        cite="C", verif="named-not-rechecked", weight="corroborating", formation="Widely Accepted",
        divergence="Flagged for priority second-opinion review before it supports any specific "
                   "claim. A different Finn from row 161's own Douglas E. Finn.",
        body="Licensed for the liturgical-evidence gap Doc_02 SS5 and SS9 item 9 both explicitly name "
             "as unaddressed -- the structure and lived experience of the Lenten/Easter Vigil "
             "baptismal rite in Augustine's own North Africa, read as ritual rather than as doctrinal "
             "argument.",
    ),
    dict(
        row=191, slug="hartel-cyprian-opera-omnia-csel3-pars1-2",
        author="Wilhelm (Guilelmus) Hartel (editor); Cyprian of Carthage (author)",
        work="S. Thasci Caecili Cypriani opera omnia, CSEL 3, Pars I (treatises, 1868) and Pars II "
             "(Epistulae I-LXXXI, 1871)",
        edition="Vendored as cic/texts/cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Project lead direct supply / 2026-09-05.",
        cite="C", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Public domain (1868/1871), the archive.org item identifier "
                   "(sthascicaecilic01hartgoog) independently confirmed matching the vendored file "
                   "character for character at both ends. OCR quality assessed directly this session, "
                   "sampled at multiple points spanning the full document: the running Latin text "
                   "reads coherently and without truncation throughout; the apparatus criticus shows "
                   "meaningfully more degradation, disclosed in the file's own header rather than "
                   "treated as pristine. Covers Pars I and II only -- Pars III (the spuria, Vita, and "
                   "Acta Proconsularia) is now also vendored, as row 194. Original-language witness "
                   "(Latin) -- second-witness caveat applies per cic/texts/INTAKE.md: never primary "
                   "evidence for a Representative on its own, only for cross-checking a specific "
                   "reading against the vendored ANF05 English translation (row 1). Confidence "
                   "deliberately held at C rather than raised: the specific claims row 1 licenses have "
                   "not themselves been re-collated against this Latin text, only the file's own "
                   "identity and OCR quality.",
        body="The critical Latin edition row 39 names, now actually vendored -- the Latin original "
             "behind the already-vendored ANF05 English translation of Cyprian's own corpus (which "
             "follows Migne's text, not Hartel's), and an independent check on that translation's own "
             "base text.",
    ),
    dict(
        row=192, slug="possidius-vita-augustini-weiskotten1919",
        author="Possidius, bishop of Calama (author); Herbert T. Weiskotten (editor and translator)",
        work="Sancti Augustini Vita Scripta a Possidio Episcopo (Life of Augustine)",
        edition="Princeton: Princeton University Press; London: Humphrey Milford, Oxford University "
                "Press, 1919; vendored as cic/texts/possidius_vita-augustini_weiskotten1919.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Project lead direct supply / 2026-09-05.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Public domain by date (1919), for both Weiskotten's Latin critical text and his "
                   "own English translation. A genuinely bilingual edition -- because the complete "
                   "English translation is present throughout, this row's Confidence is A, the "
                   "ordinary-primary-evidence footing, not the second-witness-only footing rows 88 "
                   "and 191 carry. The archive.org item identifier (sanctiaugustiniv00possrich) is "
                   "independently confirmed matching the vendored file's own text byte-for-byte at "
                   "both ends. OCR quality assessed directly: the English translation reads coherently "
                   "throughout, including at Possidius's own closing epilogue on his forty years' "
                   "friendship with Augustine; the Latin apparatus criticus and manuscript-collation "
                   "tables carry more noise. Read in full, all thirty-one chapters, in this session "
                   "(Review-Artifacts/Possidius_Full_Read_2026-09-16.md).",
        body="G3, this world's own highest-priority open request, now vendored -- Augustine's own "
             "companion for decades, and the direct counterpart to Pontius's already-vendored Life of "
             "Cyprian (row 7); closes the one-sided formation-narrative gap Doc_02 SS4 and SS9 name, "
             "and is the underlying source, via NPNF's own editorial apparatus, for the Megalius/"
             "primate-of-Numidia identification Doc_01 SS5 discloses.",
    ),
    dict(
        row=193, slug="goldbacher-augustine-epistulae-csel57-pars4",
        author="Alois Goldbacher (editor); Augustine of Hippo (author)",
        work="S. Aureli Augustini Hipponiensis episcopi Epistulae, Pars IV (Epistulae CLXXXV-CCLXX), "
             "CSEL 57",
        edition="Vindobonae: F. Tempsky; Lipsiae: G. Freytag, 1911; vendored as "
                "cic/texts/augustine_epistulae-critical_goldbacher-csel57-pars4.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Project lead direct supply / 2026-09-05.",
        cite="C", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Public domain by date (1911); archive.org item (CSEL57) independently confirmed "
                   "matching the vendored file character for character at both ends. OCR quality "
                   "quantified, not just sampled qualitatively: the running Latin letter text reads "
                   "coherently at every point sampled, including the collection's own final lines "
                   "(Epistle 270's own closing); a direct paragraph-level scan for heavy "
                   "garbage-symbol corruption found roughly 2.6% of all paragraphs (636 of 24,350) "
                   "affected, concentrated in the apparatus criticus and editorial notes -- "
                   "measurably worse than rows 191 and 88's own qualitative assessments. Original-"
                   "language witness (Latin), no facing translation -- second-witness caveat applies "
                   "per cic/texts/INTAKE.md: never primary evidence on its own, only for "
                   "cross-checking a specific reading against the vendored NPNF translation.",
        body="Part of the edition row 61 names, now actually vendored -- the Latin original behind "
             "the already-vendored NPNF translation of exactly this letter range, including Letter 185 "
             "itself (row 12), the first letter in this file's own range.",
    ),
    dict(
        row=194, slug="cyprian-opera-spuria-vita-pontius-acta-proconsularia-csel3-pars3",
        author="Wilhelm (Guilelmus) Hartel (editor); disputed works transmitted under Cyprian's own "
               "name; Pontius the Deacon (Vita, vulgo adscripta); the notaries of the 258 trial "
               "record (Acta Proconsularia)",
        work="Cyprian, Opera Spuria (disputed works transmitted under his name); Vita Caecilii "
             "Cypriani, attributed to Pontius the deacon; Acta Proconsularia Sancti Cypriani -- CSEL "
             "3, Pars III",
        edition="Vindobonae: C. Geroldi filius, 1871; vendored as "
                "cic/texts/cyprian_opera-spuria-vita-pontius-lat_hartel-csel3-pars3.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="mixed. The Opera Spuria are pseudepigraphal, per row 6's own disclosure; the "
                    "Vita is 'vulgo adscripta' (commonly attributed) to Pontius the deacon, per the "
                    "volume's own heading -- an attribution this record carries in the volume's own "
                    "qualified terms rather than flattening to a plain 'by Pontius'; the Acta "
                    "Proconsularia are documentary, an imperial court's own trial record.",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Public domain by date (1871). Fetched directly via archive.org item "
                   "corpusscriptorum03cypruoft; title page and the Vita's own heading directly "
                   "verified, quoted here in normalized form (the file's own OCR reads 'iiiilgo' for "
                   "'uulgo,' and similar ordinary letter-confusion, disclosed rather than left "
                   "silent). A real extraction hazard caught and corrected: the scanned volume is "
                   "physically bound together with CSEL 4 (Arnobius, Adversus Nationes), independently "
                   "confirmed cut before vendoring. Original-language witness (Latin), no facing "
                   "translation -- second-witness caveat applies per cic/texts/INTAKE.md.",
        body="The Vita specifically as this world's own Cyprian-side formation-narrative material, "
             "corroborating the already-vendored ANF05 English translation (row 7) at its own Latin "
             "source; the Acta Proconsularia as Cyprian's own trial and martyrdom record, not "
             "previously vendored in any form (closing row 41's own open request).",
    ),
    dict(
        row=195, slug="goldbacher-augustine-epistulae-csel34",
        author="Alois Goldbacher (editor); Augustine of Hippo (author)",
        work="S. Aureli Augustini Hipponiensis episcopi Epistulae, Pars I-II (Epistulae I-CXXIII), "
             "CSEL 34/1 (1895) and 34/2 (1898)",
        edition="Pragae/Vindobonae/Lipsiae: F. Tempsky/G. Freytag; vendored as "
                "cic/texts/augustine_epistulae-1-123-lat_goldbacher-csel34.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Public domain by date (1895/1898). Fetched directly via archive.org item "
                   "sanctiaureliaugu34augu; both title pages, Epistle 1's own opening line, and "
                   "Epistle 123's own closing manuscript-explicit apparatus note directly verified. "
                   "Running Latin text reads cleanly throughout; apparatus criticus carries ordinary "
                   "sigla-level OCR noise. Original-language witness (Latin), no facing translation -- "
                   "second-witness caveat applies per cic/texts/INTAKE.md.",
        body="Part of the edition row 61 names -- the Latin original behind the already-vendored NPNF "
             "translation of Augustine's general correspondence (row 11) and the Jerome cluster (row "
             "10) for this letter range.",
    ),
    dict(
        row=196, slug="goldbacher-augustine-epistulae-csel44",
        author="Alois Goldbacher (editor); Augustine of Hippo (author)",
        work="S. Aureli Augustini Hipponiensis episcopi Epistulae, Pars III (Epistulae "
             "CXXIV-CLXXXIV A), CSEL 44",
        edition="Vindobonae: F. Tempsky; Lipsiae: G. Freytag, 1904; vendored as "
                "cic/texts/augustine_epistulae-124-184a-lat_goldbacher-csel44.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Public domain by date (1904). Fetched directly via archive.org item "
                   "sanctiaureliaugu44augu; title page and Epistle 124's own opening line directly "
                   "verified; the collection's own true end (Epistle 184A) directly confirmed, not "
                   "truncated. Letter 185 is NOT in this range -- independently confirmed absent (zero "
                   "hits for 'CLXXXV' as a standalone heading); it is at its own Latin source in row "
                   "193 instead. Original-language witness (Latin) -- second-witness caveat applies "
                   "per cic/texts/INTAKE.md.",
        body="Part of the edition row 61 names -- the Latin original behind the already-vendored NPNF "
             "translation for Epistulae 124-184A.",
    ),
    dict(
        row=197, slug="knoll-augustine-confessiones-csel33",
        author="Pius Knoll [Knöll] (editor); Augustine of Hippo (author)",
        work="S. Aureli Augustini Confessionum Libri XIII, CSEL 33 (Sect. I Pars 1)",
        edition="Pragae/Vindobonae/Lipsiae: F. Tempsky/G. Freytag, 1896; vendored as "
                "cic/texts/augustine_confessiones-lat_knoll-csel33.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Documented",
        divergence="Not a Manifest G-item -- a new find closing a prior total absence of an original-"
                   "language witness for this text. Public domain by date (1896). Fetched via "
                   "archive.org item sanctiaureliaugu33augu -- explicitly NOT item "
                   "sanctiaureliaugu0033augu, independently confirmed to be a 1962 Johnson Reprint "
                   "Corporation facsimile and excluded. Title page, all thirteen book headings, the "
                   "opening line, and the closing Index Scriptorum all directly verified. Original-"
                   "language witness (Latin) -- second-witness caveat applies per "
                   "cic/texts/INTAKE.md.",
        body="Latin original standing behind the already-vendored NPNF translation of the Confessions "
             "(row 9) -- this world's own founding first-person document of Augustine's conversion "
             "narrative.",
    ),
    dict(
        row=198, slug="hoffmann-augustine-civitate-dei-csel40-pars1",
        author="Emanuel Hoffmann (editor); Augustine of Hippo (author)",
        work="De Civitate Dei, Libri I-XIII, CSEL 40 Pars I",
        edition="Pragae/Vindobonae/Lipsiae: F. Tempsky/G. Freytag, 1899; vendored as "
                "cic/texts/augustine_civitate-dei-1-13-lat_hoffmann-csel40-1.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Documented",
        divergence="Not a Manifest G-item. Public domain by date (1899). Fetched via archive.org item "
                   "sanctiaureliaugu401augu -- explicitly NOT items corpusscriptorum0040unse or "
                   "corpusscriptorum0040unse_o8i0, both independently confirmed to be 1962 Johnson "
                   "Reprint facsimiles and excluded. Title page, all thirteen book headings (running "
                   "heads confirmed for every book), and Book XIII's own closing line directly "
                   "verified. Companion file: row 199 (Books XIV-XXII). Original-language witness "
                   "(Latin) -- second-witness caveat applies per cic/texts/INTAKE.md.",
        body="Latin original standing behind the already-vendored NPNF translation of City of God "
             "(row 24).",
    ),
    dict(
        row=199, slug="hoffmann-augustine-civitate-dei-csel40-pars2",
        author="Emanuel Hoffmann (editor); Augustine of Hippo (author)",
        work="De Civitate Dei, Libri XIV-XXII, CSEL 40 Pars II",
        edition="Pragae/Vindobonae/Lipsiae: F. Tempsky/G. Freytag, 1900; vendored as "
                "cic/texts/augustine_civitate-dei-14-22-lat_hoffmann-csel40-2.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Documented",
        divergence="Not a Manifest G-item. Public domain by date (1900). Fetched via archive.org item "
                   "sanctiaureliaugu402augu -- the same two 1962 Johnson Reprint traps as row 198 "
                   "independently checked and excluded. Title page, all nine book headings, Book "
                   "XXII's own closing prayer, and the work's own closing indices directly verified. "
                   "Companion file: row 198 (Books I-XIII). Original-language witness (Latin) -- "
                   "second-witness caveat applies per cic/texts/INTAKE.md.",
        body="Latin original standing behind the already-vendored NPNF translation of City of God "
             "(row 24).",
    ),
    dict(
        row=200, slug="bruder-doctrina-christiana-enchiridion-maurist",
        author="Carl Hermann Bruder (editor); Augustine of Hippo (author)",
        work="De Doctrina Christiana Libri Quatuor, et Enchiridion ad Laurentium (Maurist text, "
             "editio stereotypa)",
        edition="Lipsiae: C. Tauchnitii, 1838; vendored as "
                "cic/texts/augustine_doctrina-christiana-enchiridion-lat_bruder1838.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Documented",
        divergence="Not a Manifest G-item. Public domain by date (1838) and archive.org's own "
                   "NOT_IN_COPYRIGHT determination. Fetched via archive.org item "
                   "dedoctrinachrist00augu. NOT a modern critical edition -- Bruder's own preface "
                   "states plainly this is not a critical text, disclosed rather than treated as "
                   "equivalent to CSEL 80; CSEL 80 (ed. Green, 1963) is independently confirmed in "
                   "copyright and must never be vendored (this file's own text contains zero hits for "
                   "'CSEL'/'Green'/'1963'/'copyright', independently checked). The exact internal "
                   "boundary between the two works is located precisely, at Book IV c. XXXI's own "
                   "close. Original-language witness (Latin) -- second-witness caveat applies per "
                   "cic/texts/INTAKE.md.",
        body="Latin original standing behind the already-vendored NPNF translations of both On "
             "Christian Doctrine (row 16) and the Enchiridion (row 17) -- two distinct works in one "
             "file.",
    ),
    dict(
        row=201, slug="migne-augustine-enarrationes-in-psalmos-pl36-37",
        author="Jacques-Paul Migne (editor); Augustine of Hippo (author)",
        work="Sancti Aurelii Augustini Enarrationes in Psalmos (complete, Psalms 1-150), Patrologiae "
             "Cursus Completus, Series Latina, Tomus XXXVI-XXXVII (Maurist text)",
        edition="Parisiis: J.-P. Migne, 1861; vendored as "
                "cic/texts/augustine_enarrationes-in-psalmos-lat_migne-pl36-37.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed. One appendix (a second, alternate Psalm 14 exposition) is flagged "
                    "by the Maurist editors' own footnote as not Augustine's own work.",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Documented",
        divergence="Not a Manifest G-item -- closes a prior total absence of an original-language "
                   "witness for this world's largest body of vendored material (~695,000 words in "
                   "English translation). Public domain by date (1861). Fetched via archive.org item "
                   "patrologiae_cursus_completus_lat_vol_036, binding PL 36 and PL 37 together. "
                   "Completeness independently checked, not assumed: all 150 psalms confirmed present "
                   "by their own headings, tolerantly re-parsed after a strict first pass under-"
                   "counted by 27 (all subsequently located and confirmed genuine). NOT a modern "
                   "critical edition (CCSL 38-40 is the modern standard; not vendored, in copyright, "
                   "row 71). Original-language witness (Latin) -- second-witness caveat applies per "
                   "cic/texts/INTAKE.md.",
        body="Latin original standing behind the already-vendored NPNF translation of the Expositions "
             "on the Psalms (row 20) -- this world's single largest vendored work.",
    ),
    dict(
        row=202, slug="bruns-codex-canonum-ecclesiae-africanae",
        author="Hermann Theodor Bruns (editor); the Council of Carthage (419) and the African "
               "episcopate whose earlier canons it compiles",
        work="Canones Apostolorum et Conciliorum Saeculorum IV-VII, Pars Prior (Bibliotheca "
             "Ecclesiastica) -- includes the Codex Canonum Ecclesiae Africanae (Council of Carthage, "
             "419)",
        edition="Berolini: G. Reimeri, 1839; vendored as "
                "cic/texts/codex-canonum-ecclesiae-africanae_bruns-pars1-1839.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="documentary; attributed to the conciliar body",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="corroborating", formation="Documented",
        divergence="Not a Manifest G-item. Public domain by date (1839). Fetched via archive.org item "
                   "canonesapostolo00brungoog; the Codex's own opening and its own heading directly "
                   "verified. Independently confirmed distinct from item canonesapostolo01brungoog "
                   "(Pars Altera -- the Spanish/Gallic/Italian/English councils), directly checked and "
                   "found to carry no African material at all. This volume also carries several other, "
                   "unrelated 4th-5th c. councils bound in the same scan, vendored whole rather than "
                   "fragmented, per this Registry's own large-multi-part-body convention -- not "
                   "separately catalogued as distinct census works. Original-language witness (Latin) "
                   "-- second-witness caveat applies per cic/texts/INTAKE.md.",
        body="Latin original standing behind the already-vendored NPNF2-14 translation of the Code of "
             "Canons of the African Church (row 26) -- this world's own institutional skeleton for its "
             "conciliar life.",
    ),
    dict(
        row=203, slug="prosper-epitoma-chronicon-mommsen1892",
        author="Prosper of Aquitaine (author); Theodor Mommsen (editor)",
        work="Epitoma Chronicon, with its African continuations",
        edition="Chronica Minora Saec. IV-VII, Vol. I (Monumenta Germaniae Historica, Auctorum "
                "Antiquissimorum Tomus IX) (Berolini: Weidmann, 1892); vendored as "
                "cic/texts/prosper_chronica-minora-1-lat_mommsen1892.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Prosper of Aquitaine, a contemporary Gallic chronicler",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Not a Manifest G-item -- closes a prior total absence of any contemporary "
                   "chronicle witness to this world's own close. Public domain by date (1892). "
                   "Fetched via archive.org item chronicaminorasa09momm -- the same item a sibling "
                   "Donatism-world build thread uses, under a different filename, for a different "
                   "target text in the same volume; a genuine naming correction on the sibling "
                   "session's own file is disclosed rather than repeated here. Both end-window entries "
                   "independently located and quoted: Augustine's death, year 430; the Vandal capture "
                   "of Carthage, year 439 -- a different city than Hippo, nine years after Augustine's "
                   "death, and NOT itself part of Doc_01's own end-boundary reasoning. This world's "
                   "corpus map assigns this row role: context, not tradition -- external, not this "
                   "tradition's own voice. Original-language witness (Latin) -- second-witness caveat "
                   "applies per cic/texts/INTAKE.md.",
        body="This world's own end-window (Augustine's death, 430; the Vandal capture of Carthage, "
             "439), now independently attested by a contemporary Latin chronicle where previously this "
             "world's construction held none -- directly corroborating Doc_01's own 430 end-boundary.",
    ),
    dict(
        row=205, slug="harnack-vita-cypriani-commentary",
        author="Adolf Harnack (editor and translator); Pontius the Deacon (author)",
        work="Das Leben Cyprians von Pontius: Die erste christliche Biographie (Texte und "
             "Untersuchungen zur Geschichte der altchristlichen Literatur, 3. Reihe, 9. Band, Heft 3)",
        edition="Leipzig: J. C. Hinrichs, 1913; vendored as "
                "cic/texts/harnack_vita-cypriani-commentary-lat-deu_1913.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed to Harnack as editor/translator, Pontius as the Vita's own author",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="C", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Closes Source_Acquisition_Manifest.md G2 -- no prior session had ever located an "
                   "identifier for this specific edition; Pellegrino's 1955 alternative (row 48) was "
                   "independently confirmed in copyright and was never a viable candidate. Public "
                   "domain by date (1913; Harnack himself died 1930, so also public domain under "
                   "life+70 since 2001). Fetched via archive.org item texteunduntersuc3839akad, "
                   "sliced to Harnack's own Heft 3 only; title page, table of contents, the Latin "
                   "text's own opening and closing lines, and Harnack's own statement of method "
                   "directly verified. This is Hartel's own CSEL 3 text with Harnack's noted "
                   "deviations, plus commentary and the first published German translation -- NOT an "
                   "independent new recension, an interpretive supplement to row 194's Latin text. "
                   "Consultation-only per cic/texts/INTAKE.md -- the bulk of the file is "
                   "German-language scholarship, not itself Cyprianic primary text.",
        body="A modern critical study and commentary on the already-vendored Vita Cypriani (row 7/row "
             "194), available for future consultation on textual and interpretive questions.",
    ),
    dict(
        row=206, slug="monceaux-histoire-litteraire-tome1",
        author="Paul Monceaux",
        work="Histoire littéraire de l'Afrique chrétienne depuis les origines jusqu'à l'invasion "
             "arabe, Tome Premier: Tertullien et les origines",
        edition="Paris: Ernest Leroux, 1901; vendored as "
                "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome1_1901.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="C", verif="verified-direct", weight="illustrative", formation="Widely Accepted",
        divergence="Closes one-third of Source_Acquisition_Manifest.md G5. Public domain by date "
                   "(1901; author died 1941, immaterial to the date-based determination). Fetched via "
                   "archive.org item histoirelittra01moncuoft; title page and the printer's own "
                   "closing colophon directly verified. A Manifest lead corrected this session: the "
                   "Manifest's own prior-named lead for vol. I, item histoirelittra00moncuoft, was "
                   "independently opened and found to actually be Tome Cinquième (1920), already "
                   "vendored on the sibling Donatism build's own branch, not Tome Premier -- corrected "
                   "accordingly. Consultation-only content per cic/texts/INTAKE.md.",
        body="Not currently licensed for any specific claim -- consultation-only background on "
             "Tertullian and the origins of African Christian literature.",
    ),
    dict(
        row=207, slug="monceaux-histoire-litteraire-tome2",
        author="Paul Monceaux",
        work="Histoire littéraire de l'Afrique chrétienne depuis les origines jusqu'à l'invasion "
             "arabe, Tome Deuxième: Saint Cyprien et son temps",
        edition="Paris: Ernest Leroux, 1902; vendored as "
                "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome2_1902.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="C", verif="verified-direct", weight="illustrative", formation="Widely Accepted",
        divergence="Closes another third of Source_Acquisition_Manifest.md G5. Public domain by date "
                   "(1902). Fetched via archive.org item histoirelittra02moncuoft; title page and the "
                   "volume's own closing appendix (on Cyprian's tomb and basilicas at Carthage) "
                   "directly verified. Independently corroborated against the Bibliothèque nationale "
                   "de France's own SRU catalogue record for the Manifest's already-named Gallica "
                   "lead, confirming the same Tome 2 identity. Consultation-only content per "
                   "cic/texts/INTAKE.md.",
        body="Not currently licensed for any specific claim -- consultation-only literary-historical "
             "treatment of Cyprian's own place in the wider African Christian-Latin tradition, the "
             "volume this world's own G5 request names as most directly relevant.",
    ),
    dict(
        row=208, slug="monceaux-histoire-litteraire-tome3",
        author="Paul Monceaux",
        work="Histoire littéraire de l'Afrique chrétienne depuis les origines jusqu'à l'invasion "
             "arabe, Tome Troisième: Le IVe siècle, d'Arnobe à Victorin",
        edition="Paris: Ernest Leroux, 1905; vendored as "
                "cic/texts/monceaux_histoire-litteraire-afrique-chretienne-tome3_1905.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="C", verif="verified-direct", weight="illustrative", formation="Widely Accepted",
        divergence="Closes the final third of Source_Acquisition_Manifest.md G5 (vols. I-III now "
                   "complete; vols. IV-VI already vendored in the shared corpus under the sibling "
                   "Donatism build's own G6; vol. VII, reaching Augustine, was never requested by "
                   "either world). Public domain by date (1905; the title page reads 1905, the BnF's "
                   "own catalogue gives 1906 for the same volume, both pre-1930 and immaterial to the "
                   "determination). Fetched via archive.org item histoirelitterai03monc_0; title page "
                   "and the printer's own closing colophon directly verified. Consultation-only "
                   "content per cic/texts/INTAKE.md.",
        body="Not currently licensed for any specific claim -- consultation-only, fourth-century "
             "African literature outside this world's own core Cyprian/Augustine focus.",
    ),
    dict(
        row=209, slug="knoll-augustine-retractationes-csel36",
        author="Pius Knöll (editor); Augustine of Hippo (author)",
        work="Sancti Aureli Augustini Retractationum Libri Duo, CSEL 36 (Sect. I Pars 2)",
        edition="Vindobonae: F. Tempsky; Lipsiae: G. Freytag, 1902; vendored as "
                "cic/texts/augustine_retractationes-lat_knoll-csel36.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="A", verif="verified-direct", weight="load-bearing", formation="Documented",
        divergence="Closes Source_Acquisition_Manifest.md G6 -- no prior session, across multiple "
                   "search rounds, had ever located this identifier; located this session by opening "
                   "archive.org items by volume number directly, since the Getty-hosted CSEL-Augustine "
                   "series carries no per-volume title/editor/year in its own metadata. Public domain "
                   "by date (1902). Fetched via archive.org item sanctiaureliaugu36augu; title page, "
                   "the Praefatio's own opening, the Prologus, both Books in full, and the closing "
                   "indices all directly verified. Original-language witness (Latin) -- second-"
                   "witness caveat applies per cic/texts/INTAKE.md.",
        body="Closes, at its own public-domain source, a citation row 13 previously disclosed as held "
             "only at second hand, via an NPNF editor's own quotation of Retractationes II.18 -- the "
             "Retractationes are not otherwise vendored in English translation anywhere in this "
             "corpus.",
    ),
    dict(
        row=210, slug="von-soden-cyprianische-briefsammlung",
        author="Hans (Freiherr) von Soden",
        work="Die cyprianische Briefsammlung: Geschichte ihrer Entstehung und Überlieferung, Texte "
             "und Untersuchungen, Neue Folge, 10. Band, Heft 3",
        edition="Leipzig: J. C. Hinrichs, 1904; vendored as "
                "cic/texts/vonsoden_cyprianische-briefsammlung-deu_1904.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="C", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Closes Source_Acquisition_Manifest.md G7. Public domain by date (1904). Fetched "
                   "via archive.org item diecyprianische00unkngoog; title page, the Vorwort (dated "
                   "November 1903), and the closing colophon directly verified. The same problem this "
                   "monograph studies is what produced this build's own historical Ep. XL/Epistle "
                   "XXXIX citation error -- this source would have let a reviewer catch that error at "
                   "its own root rather than nine Doc_01 review rounds in. Consultation-only content "
                   "per cic/texts/INTAKE.md.",
        body="The standard study of how Cyprian's own letter collection was formed, ordered, and "
             "transmitted, directly on the same problem row 1 and Doc_02 SS2's own Limitations entry "
             "name.",
    ),
    dict(
        row=211, slug="von-soden-prosopographie-afrikanischer-episkopat",
        author="Hans von Soden",
        work="Die Prosopographie des afrikanischen Episkopats zur Zeit Cyprians, Quellen und "
             "Forschungen aus italienischen Archiven und Bibliotheken 12, pp. 247-270",
        edition="Rome, 1909; vendored (sliced to this article's own page range) as "
                "cic/texts/vonsoden_prosopographie-afrikanischer-episkopat-deu_1909.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="C", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Closes Source_Acquisition_Manifest.md G8 -- no prior session had ever located an "
                   "identifier for this specific article, a short piece bound inside a periodical "
                   "volume and discoverable only via the serial's own title. Public domain by date "
                   "(1909). Fetched via archive.org item quellenundforsch12deutuoft (the full serial "
                   "volume), sliced to this article's own heading through its own closing paragraph, "
                   "directly verified. The same public-domain volume also carries a related, "
                   "unrequested von Soden article on the rebaptism controversy, named for a future "
                   "round rather than vendored outside this row's own scope. Consultation-only "
                   "content per cic/texts/INTAKE.md.",
        body="The only named instrument in this Registry for identifying and dating the bishops of "
             "Cyprian's own African episcopate specifically (rows 4 and 42), a gap Mandouze's "
             "Prosopographie (row 62) cannot reach, since Mandouze's own range begins in 303.",
    ),
    dict(
        row=212, slug="delehaye-passions-des-martyrs-genres-litteraires",
        author="Hippolyte Delehaye, S.J.",
        work="Les Passions des martyrs et les genres littéraires",
        edition="Bruxelles: Société des Bollandistes, 1921; vendored as "
                "cic/texts/delehaye_passions-martyrs-genres-litteraires-fra_1921.txt",
        rights=RIGHTS_VENDORED_VERIFIED,
        attribution="attributed",
        discovery="Fable research agent (this session) / archive.org direct fetch / 2026-09-08.",
        cite="C", verif="verified-direct", weight="corroborating", formation="Widely Accepted",
        divergence="Closes Source_Acquisition_Manifest.md G9. Public domain by date (1921). Fetched "
                   "via archive.org item lespassionsdesm00dele; title page, the Préface (dated 'fête "
                   "de la Toussaint, 1920'), all six chapters, and the closing Table des Matières "
                   "directly verified, confirming the volume is not truncated. The Manifest's own "
                   "'Subsidia Hagiographica 13b' series designation is flagged as unverifiable from "
                   "this scan -- no such statement appears anywhere in this item's own OCR text or "
                   "catalogue metadata, nor in a second copy independently checked; carried as an "
                   "open, disclosed gap rather than asserted with false confidence. Consultation-only "
                   "content per cic/texts/INTAKE.md.",
        body="Licensed for Doc_02's own Author Gravity assessment of Pontius's Life (row 7/row 194) -- "
             "the foundational modern study of what the passio/formation-biography genre reliably "
             "preserves and where it reliably shapes, an instrument this Registry has never before "
             "held any form of.",
    ),
]

# ------------------------------------------------------------- world_core ---
TIME_WINDOW = {"start": 246, "end": 430}

HORIZON = (
    "The formation of ordinary Latin North African Christianity as territorial, congregational, "
    "pastoral life under episcopal office, c. 246-430 CE: Cyprian of Carthage navigating the "
    "Decian persecution, plague, and schism as a working bishop (248/249-258), and Augustine of "
    "Hippo preaching, catechizing, and administering the sacraments for his own congregation a "
    "century later (391/395-430) -- bounded by two bishops' ordinary care of an entire local flock, "
    "not by a single continuous institutional narrative across the century between them (Doc_01 "
    "SS1). A world of ordinary pastors and their own congregations, not of courts, councils "
    "convened to settle empire-wide jurisdiction, or ascetic withdrawal from congregational life: "
    "its formation logic is pastoral and sacramental before it is juridical (Doc_01 SS1). Carthage, "
    "the metropolitan see of Africa Proconsularis and the most populous Latin Christian city "
    "outside Rome through most of this world's own span; Hippo Regius, a substantial port city, "
    "civilly usually placed in Africa Proconsularis but ecclesiastically Numidian -- Augustine's own "
    "second anchor is a provincial bishop answerable within a different provincial structure than "
    "the primatial see whose wider African councils he nonetheless attended (Doc_01 SS2). The "
    "beginning point is Cyprian's own conversion and rise, by congregational acclamation over five "
    "presbyters' recorded opposition, to the episcopate of Carthage (c. 246-249); the close is "
    "Augustine's death at Hippo, 28 August 430, during the Vandal siege of the city -- a real "
    "ecological rupture of the same kind that opens this world, not merely a convenient life-span "
    "boundary (Doc_01 SS2). The century between the two bishops (258-391) is a genuine documentary "
    "silence IN THIS WORLD'S OWN RECORD, not a general absence of evidence about the period: it is "
    "richly attested, but almost entirely through sources that are Donatism's own territory, not "
    "this world's own surviving voice (Doc_01 SS5, SS8; Doc_02 SS7). Strand-singular, on Doc_01 "
    "SS5's own Article 21 finding: the two phases share the same formation emphasis, practice, and "
    "ecological orientation, and the real, substantial authority-structure differences between them "
    "(a bishop's coercive capacity relative to a rival hierarchy; a rival consecration's own "
    "sacramental validity; and, the axis Doc_01 SS8 item 10 holds open rather than fully settled, "
    "conciliar-authority theory) do not clearly touch a bishop's own ordinary exercise of authority "
    "toward his own flock, which is what this world's own recurring gravities are actually about. "
    "This world's own Article 3 coherence rests not on continuous self-documentation across the "
    "gap but on a checkable, in-world fact its own surviving corpus attests: Augustine's own church "
    "documents itself as the same catholic communion Cyprian had led, arguing with him rather than "
    "against his own standing (Doc_01 SS5). Living Tradition Status: CONFIRMED by the "
    "project lead, with no single named heir -- this world's own core content, an ordinary bishop's "
    "territorial, sacramental, congregational care of a local flock, is close to the default self-"
    "understanding of the parish or diocesan ministry of most historic Christian communions that "
    "retained the office of bishop or pastor at all, ancestral to the Western church before its own "
    "divisions rather than a claim particular to one see's own succession (Doc_01 SS1). This world's "
    "own self-understanding is not a movement with a founding rupture to narrate; it experiences "
    "itself as the ordinary church (Doc_07 SS2C)."
)

FORMATION_LOGIC = (
    "What a person is actually being formed into: a member of a body that can hold them through "
    "their own failure (Doc_07 SS2I). Every lens converges on the same shape -- a rite that ends in "
    "restoration, a pastor who will not stand apart from those who failed, a refusal of any single "
    "decisive test, a graded road back rather than a verdict, one named man answerable for these "
    "particular people, and a boundary that disagreement does not breach (Doc_07 SS2I). THE MECHANISM "
    "IS RITE-GENERATES-DOCTRINE, not the reverse: this world's two defining crises are not doctrinal "
    "disputes with liturgical consequences but rite disputes argued in doctrinal terms -- the "
    "rebaptism controversy is a dispute over the valid administration of baptism, the lapsed "
    "controversy a dispute over the rite of penitential reconciliation, and three of the four "
    "Primary gravities ARE disputes about rites, the fourth the office that administers them "
    "(Doc_07 SS2A, per Doc_05 SS3.1). THE GRAVITY SPINE (Doc_07 SS2, preliminary characterization, "
    "Doc_04's own six-test assessment): Primary -- G1 Pastoral Office as Territorial Flock-Keeping, "
    "G2 Penitential Discipline, G3 Collegial Communion Preserved Despite Disagreement, G6 "
    "Sacramental and Ordination Validity Across the Boundary; Supporting -- G4 Preaching and "
    "Catechesis, G5 Conciliar Authority Theory, G7 Grace and Human Incapacity; Tensional -- G8 "
    "Confessor-Authority vs. Episcopal-Regulated Peace. THE RECURRING MOVE, underneath otherwise "
    "unrelated positions: this world characteristically refuses to let a single factor be decisive "
    "-- Cyprian refuses to let one act under persecution permanently determine membership; Augustine "
    "refuses to let a minister's purity determine a sacrament's validity, and refuses to let a "
    "believer's unaided will determine their standing before God (Doc_07 SS2D). THE INTERNAL RULE "
    "THAT KEEPS DISAGREEMENT FROM BECOMING SEPARATION (G3) is this world's most characteristic "
    "structure: 'judging no man, nor rejecting any one from the right of communion, if he should "
    "think differently from us,' said by the man presiding over the council that will decide the "
    "sharpest question in the room -- and a century and a third later, Augustine argues at book "
    "length that that man's ruling was wrong, and never places him outside (Doc_07 SS2H). "
    "PENITENTIAL DISCIPLINE IS A FUNCTIONING LEGAL SYSTEM, not a devotional practice: an examined "
    "entry, graded severity, a defined duration, a competent authority, a formal act of restoration "
    "-- and this world's law exists to bring failed members back, not to order relations between "
    "sees and the state the way World #6's own juridical life does (Doc_07 SS2E). TWO PRESSURES "
    "PRODUCED TWO NEW CLASSES OF PERSON IN ONE YEAR: the Decian edict created the lapsed and the "
    "confessors' own claim on reconciliation in the same administrative stroke, and G2/G8 are the "
    "community's response to having both in the room at once (Doc_07 SS4). THE SYSTEM METABOLIZES "
    "CRISIS INTO TEACHING: persecution produces De Lapsis and a penitential order; plague produces "
    "De Mortalitate; the rival communion produces a book-length argument about baptism; Pelagian "
    "anthropology produces thirteen works -- every external pressure on record arrives at an "
    "ordinary believer transformed into a sermon, a catechesis, or a decision about the table "
    "(Doc_07 SS4). THE INTEGRATIVE OBSERVATION: to be formed here was to be somebody's -- and to "
    "discover that this was a stronger fact about you than your own failure was. A named man is "
    "answerable for you; the community is answerable for what it does with you when you fail; the "
    "road back is walked where the people who watched you fall are the ones who have to receive "
    "you. This world argues ferociously -- about water, about councils, about grace -- and it argues "
    "INSIDE a bond it will not break, because the bond is the thing it actually believes in (Doc_07 "
    "SS6)."
)

THINNESS = (
    "Not a hostile-source problem the way the sibling Donatism build's own evidentiary situation "
    "is -- both anchor voices speak in their own words, as bishops of the tradition this world's own "
    "construction centers on, not as an opponent's quotation. This world holds the largest and most "
    "direct primary-source base of any confirmed world in the portfolio to date (Doc_02 SS1). The "
    "asymmetry here is narrower and different in kind: two named, elite, male, clerical voices carry "
    "nearly this entire world's own surviving record across a 184-year span (Doc_02 SS6). THE SKEW IS "
    "NARROWER THAN A BLANKET NEGATIVE WOULD SUGGEST, NOT ABSENT: the non-episcopal clergyman is "
    "Pontius, a deacon, whose extended first-person account is the whole subject of this world's own "
    "formation-narrative work; two lay believers' own letters survive in their own words (Epistles XX "
    "and XXI, two confessors writing to each other, neither yet ordained); and named women appear in "
    "real narrative weight -- Letter CXXVI to Albina and Letter CCXI to the Nuns of Hippo, plus "
    "Sermons 280-281 on Perpetua and Felicitas -- though the Affirmative Duty's secondary, bounded-"
    "reconstruction prong has not yet been exercised on any of the three (Doc_02 SS6, SS9). What "
    "remains true: no source anywhere in this world's own vendored corpus is authored by an ordinary "
    "lay believer writing about ordinary congregational life as such, rather than about a specific "
    "crisis that drew a bishop's own attention and thereby survival. NARRATIVE/MYTHIC THINNESS IS A "
    "POSITIVE FACT ABOUT THIS WORLD, NOT A GAP IN ITS RECORD: this world has no founding narrative, "
    "no origin myth, and remembers itself overwhelmingly through what it taught rather than what it "
    "narrated about itself -- a community that understands itself as the ordinary church, doing the "
    "ordinary work of pastoring the people in front of it, has no founding rupture to narrate and "
    "does not experience itself as needing one (Doc_07 SS2C, SS7). MATERIAL EVIDENCE IS UNEXCAVATED, "
    "NOT EMPTY: no site report, inscription catalogue, or excavation record has been independently "
    "verified in this build, and this world has no distinctive liturgical epigraphic marker of the "
    "kind the sibling Donatism build can point to; but real material evidence is textual -- an "
    "apse, a raised clergy seating area, steps, and a congregational floor, recovered from a "
    "pastoral letter rather than a trench (Doc_02 SS5; Doc_07 SS2G). THE 133-YEAR DOCUMENTARY "
    "SILENCE (258-391) IS A GENUINE SILENCE IN THIS WORLD'S OWN RECORD, never to be filled from the "
    "neighboring Donatism world whose sources do cover the interval, and never an occasion for meta-"
    "commentary about what did or did not survive to be documented (Doc_01 SS5; Doc_02 SS7). THE "
    "LITURGICAL MATERIAL HAS NEVER BEEN READ AS LITURGICAL EVIDENCE: the works that argue this "
    "world's two anchor controversies presuppose, without independently describing, the specific "
    "rite of administration each argues about -- named as the highest-value unblocked task in the "
    "build, not yet done (Doc_02 SS5, SS9; Doc_07 SS8). THE PUNIC- AND BERBER-SPEAKING RURAL "
    "SUBSTRATE is named but not resolved: this world's surviving sources overwhelmingly preserve the "
    "literate, Latin-trained episcopal voice, and how deeply the underlying substrate culture shaped "
    "ordinary congregational life specifically is not answered by anything identified in this build "
    "(Doc_01 SS2; Doc_02 SS6). THE 411 GESTA REMAINS SUBSTANTIALLY UNEXPLOITED: a live, recorded "
    "primary route to Augustine's own voice among named Donatist bishops -- he speaks in at least "
    "fourteen numbered acts -- sits in this world's own vendored corpus and bears on the conciliar-"
    "authority gravity, but is not yet drawn on by any completed construction document (Registry row "
    "65; Doc_07 SS7, SS8)."
)

CAUTIONS = (
    "1) TWO-BISHOP MEDIATION IS NOT AUTHOR GRAVITY IN THE DONATIST SENSE, BUT IT IS REAL: both anchor "
    "voices are this tradition's own, in their own words, at enormous length -- what is thin is not "
    "the un-hostile record but the NON-EPISCOPAL one, and a reader should not mistake Augustine's own "
    "episcopal dominance for the whole of this world's own voice (Doc_02 SS2; Doc_07 SS2B). 2) THE "
    "CENTURY GAP (258-391) IS DONATISM'S OWN TERRITORY, NOT THIS WORLD'S: never characterize what "
    "happened in that interval from this world's own vendored corpus, which holds nothing dated "
    "inside it; the Donatist schism sits among this world's own Historical Pressures and is Article "
    "23's future concern for how a Representative characterizes an opponent, never this world's own "
    "voice to borrow (Doc_01 SS7; Doc_02 SS1, SS6). 3) TWO NAMED COMPARANDA GUARD REAL, SPECIFIC "
    "TEMPTATIONS, NOT MERELY DATE OR PLACE MISMATCHES: Tertullian's own corpus (Excluded, row 29) is "
    "credited with FORGING the Latin theological vocabulary Cyprian works within and Augustine "
    "inherits at one further remove, WITHOUT Tertullian himself being this world's own voice -- a "
    "builder reaching for his own words to characterize Cyprian's or Augustine's preaching would be "
    "borrowing a different world's own primary voice; and the Passion of the Scillitan Martyrs (180 "
    "CE, Excluded, row 28, mirrored by a second-witness Latin/Greek text at row 204) predates this "
    "world's own boundary by 66 years and is NOT this world's own primary evidence for characterizing "
    "Cyprian's own congregation, however tempting the corpus map's own 'direct root of the "
    "Carthaginian congregational tradition' language reads (Doc_01 SS7; Doc_02 SS1). 4) THE STATE-"
    "POWER ARC IS THREE PHASES, NOT TWO, AND NEVER A SINGLE STATIC LABEL: Cyprian never solicits state "
    "power at all; Augustine's own relationship develops from an early opinion against any coercion "
    "(by his own retrospective account), through a real but narrow solicitation of legal protection "
    "argued for but in the event not granted early in his own episcopate, to a later, sustained "
    "defence of broader compulsion already in force -- never compress this into 'present but late' "
    "(Doc_01 SS7). 5) A FINE AT CTh XVI.5.21 (392) IS NOT THE SAME PROVISION AS CTh XVI.5.52 (412): "
    "the two, and the 401 council Letter 185 SS25 records between them, are three different years "
    "under different emperors, easily collapsed into each other -- XVI.5.52's own graduated Donatist-"
    "specific silver-fine schedule belongs to the sibling Donatism build, not this one (Registry rows "
    "12, 44). 6) THE CONCILIAR-AUTHORITY AXIS (G5) IS HELD OPEN, NOT SETTLED: Cyprian's own "
    "egalitarian, non-coercive theory of inter-episcopal authority and Augustine's own hierarchical, "
    "correctable one are real, substantial differences Doc_01 SS8 item 10 names and does not consider "
    "fully closed -- Doc_04 Round 9 finds a determinate Framework classification reachable from its "
    "own premises but not yet run, and the strand-singular finding itself carries a disclosed "
    "reopening caveat on exactly this axis (Doc_01 SS4, SS5, SS8 item 10; Doc_07 SS2D, SS8). 7) THE "
    "DE UNITATE TWO-RECENSION QUESTION IS UNRESOLVED: De Unitate 4-5 survives in two recensions, one "
    "(the 'Primacy Text') reading more favourably to Roman primacy, and nothing in this world's own "
    "construction record rests on which is prior (Doc_01 SS7; Registry row 3). 8) OPTATUS IS "
    "DELIBERATELY DOUBLE-PLACED ON THE CENSUS AND NOT DRAWN ON: Optatus's Against the Donatists is "
    "Catholic-side anti-Donatist polemic, not evidence of this world's own ordinary pastoral-"
    "congregational life the way Cyprian's and Augustine's own corpora are -- the placement question "
    "is a corpus-map census matter outside this compilation's own editing authority, not a claim on "
    "which world he actually belongs to (Doc_02 SS1; Registry row 27). 9) THE 411 GESTA'S OWN RICH "
    "DISCOVERY DOES NOT WIDEN WHAT IT LICENSES: fourteen numbered acts of Augustine speaking among "
    "named Donatist bishops are independently counted and quoted, but this world's own construction "
    "still rests the Conference's own date on its ordinary, undisputed dating, not on any reading of "
    "the acts -- available to future work, not yet drawn on (Registry row 65). 10) THE V7.4 FIELD-"
    "BIBLIOGRAPHY SWEEP PROPER REMAINS UNRUN: fourteen rounds of a ten-item recall test and PRESS "
    "question, each drawing on instruments the prior rounds had not used, returned 0/10 in every round "
    "but one -- real, repeated evidence of the sweep's own cost, not a substitute for running it "
    "(Source_Registry.md's own Saturation statement; Doc_02 SS9 item 6). 11) THIS COMPILATION'S OWN "
    "SOURCE OF TRUTH WAS ITSELF UNDER OPEN REVIEW AT THE TIME OF COMPILATION: Source_Registry.md's own "
    "header states it was returned to independent review after its own prior disposition, and that "
    "review had not yet returned as of this pass -- this compilation rests on the Registry as it read "
    "at that moment, not "
    "on a review verdict that had not yet arrived, and any finding that review returns should be "
    "checked against these records before they are treated as settled."
)

THIN_TOPICS = [
    {
        "keywords": ["ordinary believer", "lay experience", "what an ordinary week felt like",
                     "village religion", "an ordinary congregant's own words"],
        "note": "No source anywhere in this world's own vendored corpus is authored by an ordinary "
                "lay believer writing about ordinary congregational life as such, rather than about a "
                "specific crisis that drew a bishop's own attention and thereby survival.",
    },
    {
        "keywords": ["Punic", "Berber", "rural substrate", "non-elite congregational life",
                     "linguistic substrate culture"],
        "note": "This world's surviving sources overwhelmingly preserve the literate, Latin-trained "
                "episcopal voice. How deeply the underlying Punic/Berber substrate culture shaped "
                "ordinary congregational life specifically is a genuine open question this build "
                "has not answered.",
    },
    {
        "keywords": ["women's own words", "female interior life", "what Albina actually thought",
                     "the nuns of Hippo's own grievance"],
        "note": "Albina, the Nuns of Hippo, and Sermons 280-281 on Perpetua and Felicitas are real, "
                "narratively weighty data points, but each reaches this world's own record through "
                "Augustine's own framing of it, and the Affirmative Duty's own bounded-reconstruction "
                "test has not yet been run against any of them.",
    },
    {
        "keywords": ["basilica archaeology", "excavation", "what the buildings looked like",
                     "material remains", "the physical setting of worship"],
        "note": "No site report, inscription catalogue, or excavation record has been independently "
                "verified in this build. Real material evidence exists, but it is document-borne, "
                "recovered from a pastoral letter describing a basilica's own apse and steps, not "
                "from a trench -- unexcavated, not empty.",
    },
    {
        "keywords": ["founding narrative", "origin myth", "how this world tells its own story",
                     "a story rather than a case"],
        "note": "This world has no founding narrative and no origin myth, and the thinness is a "
                "positive fact about its own self-understanding, not a coverage failure: a community "
                "that experiences itself as the ordinary church has no founding rupture to narrate.",
    },
    {
        "keywords": ["the century gap", "258 to 391", "what happened between Cyprian and Augustine",
                     "the documentary silence"],
        "note": "A genuine 133-year silence in THIS world's own record, richly attested elsewhere "
                "only through sources that are Donatism's own territory. Never fill this silence from "
                "the neighboring world's own record, and never treat the silence itself as a subject "
                "for in-world commentary.",
    },
    {
        "keywords": ["liturgical rite's own form", "what the baptism actually looked like",
                     "the penitential rite's own steps", "worship as practiced rather than argued"],
        "note": "The works arguing this world's two anchor controversies presuppose, without "
                "independently describing, the rite each argues about. This material has never been "
                "read specifically as liturgical evidence -- named as the highest-value unblocked "
                "task in the build, not yet done.",
    },
    {
        "keywords": ["conciliar authority", "who could overrule a council",
                     "Cyprian versus Augustine on councils"],
        "note": "A real, substantial, and disclosed disagreement Doc_01 does not consider fully "
                "settled and Doc_04 finds reachable-but-unrun on its own premises: Cyprian's own "
                "egalitarian, non-coercive theory against Augustine's own hierarchical, correctable "
                "one.",
    },
]

WORLD_CORE_SOURCES = [
    {"source_id": "lpc.source.cyprian-epistles",
     "locus": "82 letters, esp. Epistle XXXIX's own election language and Epistles XX-XXI",
     "license": "public-domain"},
    {"source_id": "lpc.source.pontius-life-and-passion-of-cyprian",
     "locus": "whole work -- Cyprian's own election and the Curubis exile", "license": "public-domain"},
    {"source_id": "lpc.source.possidius-vita-augustini-weiskotten1919",
     "locus": "whole work, read in full -- Augustine's own formation-narrative counterpart to "
              "Pontius's Life", "license": "public-domain"},
    {"source_id": "lpc.source.augustine-confessions",
     "locus": "whole work -- Augustine's own conversion narrative", "license": "public-domain"},
    {"source_id": "lpc.source.augustine-on-baptism-against-the-donatists",
     "locus": "I.1.2, II.3, III ch. 2 SS2, VI ch. 2", "license": "public-domain"},
    {"source_id": "lpc.source.augustine-correction-of-the-donatists",
     "locus": "ch. 7 SSSS23-29 -- the imperial-coercion defence", "license": "public-domain"},
    {"source_id": "lpc.source.augustine-letter-93-to-vincentius",
     "locus": "SS17 -- Augustine's own account of his earlier opinion against coercion",
     "license": "public-domain"},
    {"source_id": "lpc.source.code-of-canons-of-the-african-church-419",
     "locus": "whole work -- the institutional skeleton of this world's own conciliar life",
     "license": "public-domain"},
]

WORLD_CORE_BODY = """Built from Doc_01_World_Identification_Boundaries_Orientation.md (SS1 identity and Living Tradition Status, SS2 the boundary dates and their own reasoning, SS4 the World Separation Criteria and the three named authority-structure axes, SS5 the Strand Determination and the Article 3 answer, SS7 the World #6/#9/#4 continuity-and-distinction discharge, SS8 open items), Doc_07_Integrated_Ecology_Analysis.md (SS2 the nine integration lenses, SS3A Memory Structures, SS5 Cross-Lens Synthesis, SS6 the Integrative Observation, SS7 Gaps and Limits), and Doc_02_Source_Ecology.md (SS2 Author Gravity Assessment, SS6 Source Asymmetries and Missing Voices, SS7 the century-gap disclosure, SS8 the Confidence Map, SS9 open items) together with Source_Registry.md's own named gaps, its Discovery-methodology and Saturation statements, and Source_Acquisition_Manifest.md's own G1-G9 record.

WORLD_ID: `latin-pastoral-congregational-christianity`. This world has no entry in records/worlds.yaml at all, so no registry value is being contradicted; the slug matches cic/corpus-map/latin-pastoral-congregational-christianity.yaml's own `atlas_id`, which is the census movement id and the join key, so the record id prefix (`lpc`), the world_id, and the census join all read consistently. Registering the world in records/worlds.yaml is a later admission-track step, out of scope for this first record-authoring pass, exactly as it was for the sibling Donatism world compiled before this one.

TIME_WINDOW: start 246, end 430. Doc_01's own beginning point is Cyprian's conversion and rise to the episcopate, "c. 246-249" as a single approximate range rather than don's own doubled 311/312 opening; the earlier boundary year is carried in the schema's own single integer, with the fuller two-to-three-year interval and the two bishops' own different conversion-to-office intervals stated in `horizon` instead of collapsed. The 430 close is Augustine's own death during the Vandal siege of Hippo -- Doc_01 SS2 argues it is a real ecological rupture of the same kind that opens this world, not merely a biographical endpoint, and `horizon` carries that argument rather than only the date.

WHAT THIS RECORD DOES NOT CLAIM. This world's Living Tradition Status is already CONFIRMED (Doc_01 SS1, 2026-09-16, by the project lead) -- unlike don's own world_core, which reports a still-PENDING status, this record's own `horizon` states the confirmed finding directly, including its own "no single named heir" qualification, since that is what the confirmation itself says rather than a further act this compilation performs. The Representative does not appear in this record, and no Representative content is compiled into it.

REGISTRY ROWS 28, 29, 98, 128, AND 204 ARE NOT COMPILED AS SOURCE RECORDS FOR THIS WORLD, and the omission is deliberate, not an error to be corrected later. Row 28 (the Passion of the Scillitan Martyrs, 180 CE) and row 29 (Tertullian's corpus generally) are Named Comparanda, on the same footing don's own Registry row 29 (Novatian) models: each guards against a real, specific temptation (borrowing a genuine ancestor-text or a genuine influence-source as though it were this world's own primary voice) rather than merely marking a date or place mismatch. Rows 98 (Maier, L'épiscopat de l'Afrique romaine, vandale et byzantine) and 128 (Wolff, Littérature, politique et religion en Afrique vandale) are Out-of-Boundary: both extend through, or begin after, the Vandal/Byzantine periods past this world's own 430 close. Row 204 carries a dual disposition on its own two physical portions, and BOTH are excluded from this world on independent grounds: its Scillitan-Martyrs portion mirrors row 28's own Excluded disposition exactly (a second-witness Latin/Greek text of the same excluded work), and its Perpetua-and-Felicitas portion is assigned to a THIRD world entirely -- `tertullian-s-voice`, on Mark's own prior 2026-08-26 ruling, independently reconfirmed this session -- so neither portion is Native to `lpc` on any reading. 207 of the Registry's 212 rows are compiled; these five are not.
"""


# ------------------------------------------------------------------ emit ---
def _yaml_dump(payload: dict) -> str:
    return yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=100, default_flow_style=False)


def _write(path: Path, payload: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + _yaml_dump(payload) + "---\n" + body.strip() + "\n", encoding="utf-8")


def emit_source(r: dict) -> Path:
    rid = f"lpc.source.{r['slug']}"
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
        "external_ids": {"lpc_source_registry_row": r["row"]},
    }
    path = OUT_ROOT / "source" / f"{rid}.md"
    _write(path, payload, r["body"])
    return path


def emit_world_core() -> Path:
    rid = "lpc.core.latin-pastoral-congregational-christianity"
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
                "This record synthesises nine completed construction documents (Doc_01, Doc_02, "
                "Doc_07, and the Registry/Manifest pair they both rest on) rather than reading a "
                "text directly, so verification runs via those documents' own authority, not via a "
                "primary source reopened here. Doc_07 SS2I's own convergence finding -- that formation "
                "here runs through rite, penitential discipline, and communion preserved despite "
                "disagreement as one integrated mechanism rather than four separately-arrived-at "
                "concerns -- is this build's own synthetic judgment, stated as such at Doc_07 SS5, "
                "not a claim any single source states in those terms; external scholarly review "
                "should test whether it overstates the coherence of what was, on the ground, a more "
                "locally variable and contingent pastoral practice across two centuries and two "
                "cities. A further, disclosed uncertainty this record carries forward rather than "
                "resolves: Doc_01 SS8 item 10's own conciliar-authority axis (G5) is held open, not "
                "settled, and the strand-singular finding this record's own horizon states carries an "
                "explicit reopening caveat on exactly that axis."
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


EXCLUDED_ROWS = {28, 29, 98, 128, 204}


def main() -> int:
    slugs = [r["slug"] for r in ROWS]
    assert len(slugs) == len(set(slugs)), "duplicate slug"
    rows = sorted(r["row"] for r in ROWS)
    assert len(rows) == len(set(rows)), "duplicate row number"
    assert not (set(rows) & EXCLUDED_ROWS), (
        "an Excluded/Out-of-Boundary row (28, 29, 98, 128, or 204) is being emitted as a source "
        "record -- see the module docstring's own account of why each is excluded"
    )
    assert set(rows) == set(range(1, 213)) - EXCLUDED_ROWS, (
        f"row set does not match Source_Registry.md's own 212 rows minus the 5 excluded: "
        f"missing={sorted((set(range(1, 213)) - EXCLUDED_ROWS) - set(rows))}, "
        f"unexpected={sorted(set(rows) - (set(range(1, 213)) - EXCLUDED_ROWS))}"
    )
    assert len(ROWS) == 207, f"expected 207 Native rows, got {len(ROWS)}"

    ordered = sorted(ROWS, key=lambda r: r["row"])
    written = [emit_source(r) for r in ordered]
    written.append(emit_world_core())
    for p in written:
        print(p.relative_to(REPO_ROOT))
    print(f"\n{len(written)} records written "
          f"({len(ROWS)} source + 1 world_core); Registry rows 28, 29, 98, 128, and 204 "
          f"deliberately not emitted.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

