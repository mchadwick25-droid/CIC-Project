"""S2.1a - Desert migration-time discovery sweep (blueprint S2.1a; SS11-A per F2).

Scoped honestly as a MIGRATION-TIME check, not a reconstruction of the
original build's discovery process: the backfill rule forbids inventing
discovery data for existing rows, and this step never touches them. The
sweep below was run 2026-07-26 with the instruments named in the
search_record; every new row carries REAL discovery data
(discovery_instrument + discovery_date) because the discovery genuinely
happened now.

Instruments used and their honest access notes (also in the search_record):
  - Web bibliographic search + citation verification against publisher/
    catalogue pages (Oxford University Press, sourceschretiennes.org,
    Semantic Scholar, Cambridge Core) - the sweep's workhorse.
  - Coptic Congress "Preliminary Bibliography: Research in Egyptian
    Monasticism 2012-2016" (copticcongress2016.org) - a genuine field
    bibliography surfaced during the sweep.
  - The Oxford Handbook of Christian Monasticism (Kaczynski ed., OUP 2020)
    used as a reference-work checklist, not added as an evidence row.
  - CPG used as an author-corpus checklist for Athanasius/Evagrius coverage;
    CPG numbers NOT independently re-verified against the printed Clavis
    (doc 12's own caution) and therefore not recorded on rows.
  - BIBP and L'Annee philologique: NOT ACCESSIBLE from this environment
    (subscription interfaces) - recorded as coverage limits, not searched.
  - Oxford Bibliographies: searched for a dedicated "Desert Fathers" entry;
    none found - a null result, recorded in terms_tried.

Dispositions: 8 works ADDED as srcDES017-024 (4 already load-bearing in
Doc_02's own prose but row-less: Gould, Veilleux, Lundhaug & Jenott, and
the missing critical edition of the world's central text; 4 that any
specialist bibliography of this world holds: Ward's translation, Harmless,
Chitty, Wipszycka). 4 works surfaced and EXCLUDED with reasons (below) -
the gate checks every disposition has a row or a logged exclusion.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import COMMON, emit_record, OUT

SWEEP_DATE = "2026-07-26"

EXCLUDED = [
    ("John Wortley (trans.), The Anonymous Sayings of the Desert Fathers (Cambridge, 2013)",
     "translation coverage of the Apophthegmata adequate via srcDES021 for this purposive migration-time scope; lead for S2.4 quote work"),
    ("Jean-Claude Guy (ed.), Les Apophtegmes des Peres, SC 387/474/498 (critical edition, Systematic Collection)",
     "no current record cites the Systematic Collection specifically; reserved as a research lead for S2.4/S2.5 quote-fidelity work rather than added row-first"),
    ("Peter Brown, 'The Rise and Function of the Holy Man in Late Antiquity' (JRS 61, 1971)",
     "analytic-lens scholarship on the holy-man category beyond this world's own record; Doc_05-class lead, not source-ecology evidence"),
    ("Bernice M. Kaczynski (ed.), The Oxford Handbook of Christian Monasticism (OUP, 2020)",
     "used as a sweep instrument (reference-work checklist), not an evidence row"),
]

NEW_ROWS = [
    dict(id="srcDES017",
         work_author="Graham Gould", work_title="The Desert Fathers on Monastic Community (Oxford Early Christian Studies, Oxford University Press, 1993)",
         work_locus="1993", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="backward-snowball", snowball_parent="srcDES003",
         discovery_instrument="followed from Doc_02 SS1.3's own citation of Gould's counter-position; citation verified against academic.oup.com",
         discovery_date=SWEEP_DATE,
         licensed_for="Secondary scholarship: the named counter-position to Rubenson on the Letters' Origenist reading (Doc_02 SS1.3; Doc_01 SS10)",
         verification_note="Load-bearing in Doc_02's own SS1.3 argument yet had no registry row - the exact gap class this sweep exists to catch."),
    dict(id="srcDES018",
         work_author="Armand Veilleux (trans.)", work_title="Pachomian Koinonia, 3 vols. (Cistercian Publications, 1980-1982)",
         work_locus="1980-1982", source_type="S",
         attribution_status="genuine", level_of_description="corpus",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="backward-snowball", snowball_parent="srcDES002",
         discovery_instrument="followed from Doc_02 SS1.2's version-priority debate (Rousseau and Veilleux's differing positions, via Doc_01 SS10); publication verified by web search",
         discovery_date=SWEEP_DATE,
         licensed_for="Standard English translation corpus of the Pachomian dossier; the named second position in the version-priority debate srcDES002 carries",
         verification_note="Named in the build's own prose (via Doc_01 SS10) without a row."),
    dict(id="srcDES019",
         work_author="Hugo Lundhaug and Lance Jenott", work_title="The Monastic Origins of the Nag Hammadi Codices (Mohr Siebeck, 2015)",
         work_locus="2015", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="backward-snowball", snowball_parent="srcDES011",
         discovery_instrument="followed from Doc_02 SS5.3's named position-holders; verified via Google Books/Semantic Scholar",
         discovery_date=SWEEP_DATE,
         field_state="contested",
         licensed_for="The developed monastic-origin position on srcDES011's open question (Doc_02 SS5.3, open item 3 - neither position adopted)",
         verification_note="Named in Doc_02 SS5.3 without a row; its addition does not resolve the contested question, it sources the position."),
    dict(id="srcDES020",
         work_author="G.J.M. Bartelink (ed.)", work_title="Athanase d'Alexandrie, Vie d'Antoine - introduction, texte critique, traduction, notes et index (Sources Chretiennes 400, Cerf, 1994)",
         work_locus="SC 400, 1994", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="fra", script="Latn",
         edition_status="critical",
         discovery_channel="field-bibliography",
         discovery_instrument="reference-work sweep (critical-edition coverage check for the world's central text); verified against sourceschretiennes.org/collection/sc400 (edition based on ~50 collated manuscripts)",
         discovery_date=SWEEP_DATE,
         licensed_for="The critical edition of srcDES001's text - the registry previously named no edition for the Vita Antonii at all",
         verification_note="Verified directly against the Sources Chretiennes catalogue page 2026-07-26."),
    dict(id="srcDES021",
         work_author="Benedicta Ward (trans.)", work_title="The Sayings of the Desert Fathers: The Alphabetical Collection (Mowbray, 1975)",
         work_locus="1975", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn",
         discovery_channel="field-bibliography",
         discovery_instrument="reference-work sweep (standard-translation coverage check for the world's central corpus); verified via Cambridge Core review citation",
         discovery_date=SWEEP_DATE,
         licensed_for="Standard English translation of the Alphabetical Collection (srcDES005/srcDES006's corpus) - the translation-used row S2.4's quote records will need",
         verification_note="Added at migration time so quote records can carry a real translation_used reference."),
    dict(id="srcDES022",
         work_author="William Harmless", work_title="Desert Christians: An Introduction to the Literature of Early Monasticism (Oxford University Press, 2004)",
         work_locus="2004", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         discovery_instrument="reference-work sweep; verified against global.oup.com product page",
         discovery_date=SWEEP_DATE,
         licensed_for="Standard literature introduction to this world's sources - orientation and cross-checking",
         verification_note="A work any specialist bibliography of this world holds; absent from the purposive registry."),
    dict(id="srcDES023",
         work_author="Derwas J. Chitty", work_title="The Desert a City: An Introduction to the Study of Egyptian and Palestinian Monasticism under the Christian Empire (Blackwell, 1966)",
         work_locus="1966", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         discovery_instrument="reference-work sweep; publication corroborated via web references (not publisher-direct)",
         discovery_date=SWEEP_DATE,
         licensed_for="The classic survey of this world's settlement history - historiographic baseline",
         verification_note="Citation corroborated via secondary web references only (verified-via-authority grade, not publisher-direct)."),
    dict(id="srcDES024",
         work_author="Ewa Wipszycka", work_title="The Second Gift of the Nile: Monks and Monasteries in Late Antique Egypt (JJP Supplement, 2018)",
         work_locus="2018", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         discovery_instrument="reference-work sweep + Coptic Congress preliminary bibliography; citation corroborated via recent scholarly bibliographies",
         discovery_date=SWEEP_DATE,
         licensed_for="Major papyrological-institutional synthesis - directly reinforces Doc_02 SS5's documentary register (Nepheros, economic embeddedness)",
         verification_note="Citation corroborated via scholarly-bibliography references; complements srcDES010/srcDES015's documentary line."),
]

SEARCH_RECORD = {
    "id": "srcDESsearch001", "world_id": "desert-monasticism",
    "record_type": "search_record", "schema_version": 1, "register": "etic",
    "review_state": "draft", "jobs": [1],
    "sampling_strategy": "Purposive, not comprehensive (Booth's standard) - EXPLICITLY SCOPED AS A MIGRATION-TIME SEARCH (2026-07-26, S2.1a per F2), documenting this sweep only, never the original build's own discovery process (which the backfill rule leaves unrecoverable by design).",
    "types_sought": ["critical editions of the world's central texts",
                      "standard English translations", "major monographs",
                      "papyrological/institutional syntheses",
                      "works load-bearing in Doc_02's own prose but absent from its registry"],
    "approaches": {"field-bibliography": 5, "backward-snowball": 3},
    "years_searched": {"from": 1966, "to": 2026},
    "languages_searched": ["en", "fr"],
    "inclusion_exclusions": "Included: works a specialist bibliography of Egyptian desert monasticism holds, plus every work Doc_02's own arguments cite without a row. Excluded with logged reasons (see s21a_discovery_sweep.py EXCLUDED): Wortley (translation overlap), Guy SC editions (reserved lead for quote work), Brown 1971 (analytic-lens, Doc_05-class), Oxford Handbook (instrument, not evidence).",
    "terms_tried": [
        {"term": "Oxford Bibliographies dedicated 'Desert Fathers' entry", "productive": False},
        {"term": "BIBP (Base d'Information Bibliographique en Patristique) subject search", "productive": False},
        {"term": "L'Annee philologique subject search", "productive": False},
        {"term": "Oxford Handbook of Christian Monasticism (Egypt chapters) checklist", "productive": True},
        {"term": "Coptic Congress preliminary bibliography, Egyptian monasticism 2012-2016", "productive": True},
        {"term": "critical edition Vita Antonii Sources Chretiennes", "productive": True},
        {"term": "Pachomian Koinonia Veilleux Cistercian", "productive": True},
        {"term": "Lundhaug Jenott Monastic Origins Nag Hammadi", "productive": True},
        {"term": "Gould Desert Fathers Monastic Community", "productive": True},
    ],
    "instruments": [
        "web bibliographic search + publisher/catalogue verification (OUP, sourceschretiennes.org, Semantic Scholar, Cambridge Core)",
        "Coptic Congress 'Research in Egyptian Monasticism 2012-2016' preliminary bibliography",
        "Oxford Handbook of Christian Monasticism (reference-work checklist)",
        "CPG as author-corpus checklist (numbers not re-verified against the printed Clavis - doc 12 caution)",
        "NOT ACCESSIBLE, logged as coverage limits: BIBP; L'Annee philologique",
    ],
}

SATURATION = (
    "Saturation statement (SS4.3's supply-side criterion, migration-time scope): "
    "the last searches of this sweep returned nothing new - the Oxford "
    "Bibliographies check found no dedicated Desert Fathers entry (null), and "
    "the final reference-work passes re-surfaced only works already "
    "dispositioned (Harmless, Chitty, Wipszycka, Ward, and the four "
    "named-in-prose works). Two instruments remain unsearched (BIBP, L'Annee "
    "philologique - inaccessible from this environment) and are recorded as "
    "COVERAGE LIMITS of this migration-time sweep, not as satisfied searches; "
    "a future session with access should re-run the sweep against them before "
    "world-freeze."
)


def main():
    for row in NEW_ROWS:
        rec = {**COMMON, **row, "jobs": [1, 2],
               "added": f"{SWEEP_DATE} (S2.1a migration-time discovery sweep)"}
        body = (f"Added at S2.1a (migration-time discovery sweep, {SWEEP_DATE}) with real "
                f"discovery data. Sweep log: `wrs/migrate/s21a_discovery_sweep.py`; "
                f"search record: srcDESsearch001.")
        emit_record(rec, body, OUT / "source" / f"{rec['id']}.md")
    emit_record(SEARCH_RECORD, SATURATION, OUT / "search_record" / "srcDESsearch001.md")
    print(f"wrote {len(NEW_ROWS)} new source rows + search_record; "
          f"{len(EXCLUDED)} exclusions logged in EXCLUDED")


if __name__ == "__main__":
    main()
