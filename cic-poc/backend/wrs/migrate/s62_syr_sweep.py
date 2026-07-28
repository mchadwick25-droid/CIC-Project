"""S6.2/Syriac - S2.1a-equivalent: discovery sweep rows + search record.

THE SWEEP (the ALX 'On the Incarnation class'): works load-bearing in the
deployed chunks' own Key Sources / front-matter Source lines but absent
from the S2.1 rows at work-or-corpus level, plus works named by the build
docs' own correction text. All 19 deployed chunks read (10 lexicon Key
Sources sections + 9 story front-matter Source lines); every candidate
adjudicated against the FULL composite string of the nearest existing row
(26/29/42/47/51 pulled verbatim) before being called a miss.

EIGHT ROWS (srcSYR054-061), each with REAL discovery data (unlike the
migrated 001-053, whose historical discovery is unrecoverable by design):

- 054 Wickes 2019 (syrlex004's load-bearing scholarship; row 1 is Wickes'
  2015 TRANSLATION - a different work).
- 055 Brock, CHECL ch. 33 (2004) (syrlex004; also Doc_02 SS3's own
  'dominance effect' warrant; row 29's Brock composite does NOT contain it).
- 056 Griffith, The Harp 4 (1991) (syrlex002 AND syrlex007 both cite it
  with the pointer '(Source Registry #26, cross-checked)' - row 26's
  actual string does NOT contain it -> FLAG-025, filed this step).
- 057 Griffith, Eulogema chapter (1993) (Doc_02 SS3's correction and
  Doc_03 SS1.2 name it as the second qyama-specific Griffith citation).
- 058 GEDSH entries s.v. 'Ihidaya' (Kitchen), 'Papa bar Aggai', 'Basil of
  Caesarea' (syrlex007/syrlex009/syrstory008; row 51's aggregate names
  FOUR OTHER entries, not these three).
- 059 the Syriac Vita Ephraemi itself (P; 6th c.) (syrstory008's primary
  text; row 34 is Amar's STUDY of the Vita tradition, not the text).
- 060 Rousseau 1957-58 (syrstory008 legend scholarship; French).
- 061 Muraviev 2015 (syrstory008 legend scholarship; journal language
  unverified this session -> und, declared).

DECLARED NON-ROWS (in srcSYRsearch001, not silent): Doctrina Addai
editions Howard 1981/Lollar 2023 (edition-level detail of row 20's work;
the ALX pattern defers editions/translations to the pre-freeze re-sweep);
Acts of Miles + Synodicon Orientale (the GEDSH Papa-bar-Aggai entry's OWN
apparatus, second-order - flagged to the pre-freeze re-sweep rather than
rowed second-hand; Bar Ebroyo = row 42, Aphrahat Dem 14 = row 10);
Valavanolickal (inside row 10's composite; the syrlex003 2005-vs-2011
printing flag is a row-10 verification item, not a rowless work);
Harvey/Malki (rows 32/33 - checked, present).

COVERAGE FINDING (routed to S2.2, recorded in the checkpoint): syrlex005
(memra) and syrlex008 (mar) are Tier-3 chunks carrying NO Key Sources
section - correct for their tier's thin format, but the S2.2 split must
source their term records from front-matter alone.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from s62_alx_source_rows import emit_record  # noqa: E402

OUT = HERE.parent / "records" / "syriac_world"

SWEEP_INSTRUMENT = (
    "S2.1a deployed-chunk Key-Sources sweep (all 19 Syriac chunks: 10 "
    "lexicon Key Sources sections + 9 story front-matter Source lines, "
    "diffed against the S2.1 rows with the nearest composite row strings "
    "pulled verbatim for adjudication; wrs/migrate/s62_syr_sweep.py)")
DOC_INSTRUMENT = (
    "Doc_02 SS3 / Doc_03 SS1.2 correction-text read during sweep "
    "adjudication (the corrected qyama-specific Griffith citations)")

COMMON = {
    "world_id": "syriac-edessa-nisibis",
    "record_type": "source",
    "schema_version": 1,
    "register": "etic",
    "review_state": "draft",
    "disposition": "in-use",
    "discovery_date": "2026-07-28",
    "added": "2026-07-28 (S6.2/SYR S2.1a sweep)",
    "jobs": [1, 2],
}

S_COMMON = {**COMMON, "source_type": "S", "boundary_status": "Native",
            "attribution_status": "genuine", "language": "eng",
            "script": "Latn", "level_of_description": "work",
            "discovery_channel": "backward-snowball",
            "discovery_instrument": SWEEP_INSTRUMENT}

ROWS = [
    {**S_COMMON, "id": "srcSYR054",
     "genre_form": "monograph",
     "work_author": "Jeffrey Wickes",
     "work_title": ("Bible and Poetry in Late Antique Mesopotamia: "
                    "Ephrem's Hymns on Faith (University of California "
                    "Press, 2019)"),
     "work_locus": "2019",
     "licensed_for": ("Secondary scholarship: the load-bearing study "
                      "behind syrlex004 (madrasha) - confidence-judgment "
                      "apparatus only, never voice content."),
     "verification_note": ("Cited in syrlex004's Key Sources; absent from "
                           "every S2.1 row (row 1 is Wickes' 2015 Hymns "
                           "on Faith TRANSLATION - a different work). Not "
                           "independently examined this session; registry "
                           "presence closes the coverage gap.")},
    {**S_COMMON, "id": "srcSYR055",
     "work_author": "Sebastian Brock",
     "work_title": ("\"Ephrem and the Syriac Tradition,\" in The "
                    "Cambridge History of Early Christian Literature "
                    "(2004): 361-372"),
     "work_locus": "2004",
     "licensed_for": ("Secondary scholarship: syrlex004's Key Sources and "
                      "Doc_02 SS3's own 'dominance effect' warrant (corpus-"
                      "size inference) - confidence-judgment apparatus "
                      "only, never voice content."),
     "verification_note": ("Cited in syrlex004's Key Sources and Doc_02 "
                           "SS3; row 29's Brock composite (Luminous Eye / "
                           "Hymns on Paradise trans. / Harp of the "
                           "Spirit) does NOT contain it. genre_form unset: "
                           "a book chapter fits no enum value honestly. "
                           "Not independently examined this session.")},
    {**S_COMMON, "id": "srcSYR056",
     "genre_form": "journal-article",
     "work_author": "Sidney Griffith",
     "work_title": ("\"'Singles' in God's Service: Thoughts on the "
                    "Ihidaye from the Works of Aphrahat and Ephraem the "
                    "Syrian,\" The Harp 4 (1991): 145-59"),
     "work_locus": "1991",
     "licensed_for": ("Secondary scholarship: the qyama/ihidaya-specific "
                      "Griffith citation carried by syrlex002 and "
                      "syrlex007 - confidence-judgment apparatus only, "
                      "never voice content."),
     "verification_note": ("Cited in syrlex002 AND syrlex007, both with "
                           "the pointer '(Source Registry #26, cross-"
                           "checked)' - row 26's actual string (Faith "
                           "Adoring the Mystery / 1986 Deacon of Edessa / "
                           "2002 JCSSS) does NOT contain it: the chunks' "
                           "cross-reference is mis-pointered (FLAG-025). "
                           "Doc_02 SS3's correction and Doc_03 SS1.2 name "
                           "this article (with the 1993 Eulogema chapter, "
                           "srcSYR057) as the real qyama-specific Griffith "
                           "citations, explicitly NOT Faith Adoring the "
                           "Mystery. This row is the citation's true "
                           "registry home.")},
    {**S_COMMON, "id": "srcSYR057",
     "discovery_instrument": DOC_INSTRUMENT,
     "work_author": "Sidney Griffith",
     "work_title": ("\"Monks, 'Singles,' and the 'Sons of the "
                    "Covenant',\" in Eulogema: Studies in Honor of Robert "
                    "Taft, S.J. (Studia Anselmiana 110, 1993): 141-60"),
     "work_locus": "1993",
     "licensed_for": ("Secondary scholarship: the second qyama-specific "
                      "Griffith citation per Doc_02 SS3's correction and "
                      "Doc_03 SS1.2 - confidence-judgment apparatus only, "
                      "never voice content."),
     "verification_note": ("Named by Doc_02 SS3 (Corrected 2026-07-08) and "
                           "Doc_03 SS1.2 as a qyama-specific citation; not "
                           "cited by any deployed chunk directly and "
                           "absent from every row. Title ellipsis as "
                           "Doc_03 carries it, expanded from the Studia "
                           "Anselmiana series data. genre_form unset: a "
                           "book chapter fits no enum value honestly. Not "
                           "independently examined this session.")},
    {**S_COMMON, "id": "srcSYR058",
     "genre_form": "reference-work",
     "level_of_description": "aggregate-attestation",
     "work_title": ("Gorgias Encyclopedic Dictionary of the Syriac "
                    "Heritage (GEDSH): s.v. \"Ihidaya\" (Robert A. "
                    "Kitchen); s.v. \"Papa bar Aggai\""),
     "work_locus": "2011",
     "licensed_for": ("Reference-work entries for cross-verification "
                      "(the row-51 class): the two GEDSH entries the "
                      "deployed chunks cite that row 51's own list does "
                      "not name - confidence-judgment apparatus only, "
                      "never voice content."),
     "verification_note": ("Cited in syrlex007 (Ihidaya) and syrlex009 "
                           "(Papa bar Aggai); row 51's aggregate names "
                           "three OTHER entries ('Ephrem, Life of' "
                           "[Amar]; 'Basil of Caesarea' [on the legendary "
                           "meeting - which COVERS syrstory008's GEDSH "
                           "citation, adjudicated against row 51's own "
                           "bracket note]; 'Aphrahat' [Brock]) plus "
                           "Asmussen. Same cross-verification-only use as "
                           "row 51's own verification_note declares.")},
    {**COMMON, "id": "srcSYR059",
     "source_type": "P", "boundary_status": "Native",
     "attribution_status": "anonymous", "language": "syr",
     "script": "Syrc", "level_of_description": "work",
     "genre_form": "hagiography",
     "discovery_channel": "backward-snowball",
     "discovery_instrument": SWEEP_INSTRUMENT,
     "work_title": "The Syriac Vita Ephraemi (6th c.)",
     "work_locus": "6th c.",
     "licensed_for": ("Later-tradition legend material ONLY (6th-century "
                      "hagiography, outside the 200-410 window's own "
                      "witness): licensed solely for direct participant "
                      "engagement with the Ephrem-Basil legend under "
                      "syrstory008's own retrieve-when rule (never "
                      "proactive, always with its correction attached), "
                      "and never as evidence for 200-410 fact claims.")   ,
     "verification_note": ("syrstory008's front-matter primary text; also "
                           "named in syrlex002's Author-Gravity note as "
                           "the later hagiographic stratum. Row 34 is "
                           "Amar's edition/STUDY of the Vita tradition, "
                           "not the text itself. Native per the row-42 "
                           "precedent (later witnesses TO this world's own "
                           "figures row as Native with time-restricted "
                           "licensing, not Out-of-Boundary).")},
    {**S_COMMON, "id": "srcSYR060",
     "genre_form": "journal-article", "language": "fra",
     "work_author": "O. Rousseau",
     "work_title": ("\"La rencontre de S. Ephrem et de S. Basile,\" "
                    "L'Orient Syrien 2-3 (1957-58)"),
     "work_locus": "1957-58",
     "licensed_for": ("Secondary scholarship on the Ephrem-Basil legend "
                      "(syrstory008's correction apparatus) - confidence-"
                      "judgment apparatus only, never voice content."),
     "verification_note": ("Cited in syrstory008's Source line; absent "
                           "from every row. Not independently examined "
                           "this session.")},
    {**S_COMMON, "id": "srcSYR061",
     "genre_form": "journal-article", "language": "und",
     "script": "Zyyy",
     "work_author": "Alexei Muraviev",
     "work_title": ("\"Early Syriac Version of the Encounter of Basil of "
                    "Caesarea and Ephrem the Syrian,\" Vestnik Drevney "
                    "Istorii 4 (2015)"),
     "work_locus": "2015",
     "licensed_for": ("Secondary scholarship on the Ephrem-Basil legend "
                      "(syrstory008's correction apparatus) - confidence-"
                      "judgment apparatus only, never voice content."),
     "verification_note": ("Cited in syrstory008's Source line; absent "
                           "from every row. Language 'und' DECLARED: "
                           "Vestnik Drevney Istorii is a Russian-language "
                           "journal but the chunk carries an English "
                           "title, and the article's actual language was "
                           "not verified this session - resolve at the "
                           "pre-freeze re-sweep. Not independently "
                           "examined this session.")},
]

SEARCH = {
    "id": "srcSYRsearch001",
    "world_id": "syriac-edessa-nisibis",
    "record_type": "search_record",
    "schema_version": 1,
    "register": "etic",
    "review_state": "draft",
    "jobs": [1],
    "sampling_strategy": (
        "Purposive, not comprehensive (Booth's standard) - EXPLICITLY "
        "SCOPED AS A MIGRATION-TIME SEARCH (2026-07-28, S6.2/SYR S2.1a), "
        "documenting this sweep only, never the original build's own "
        "discovery process (unrecoverable by design per the backfill "
        "rule). Second sweep under the governing V7.4 Step 2 standard "
        "(ALX precedent srcALXsearch001)."),
    "types_sought": [
        ("works load-bearing in the deployed chunks' own Key Sources / "
         "story Source lines but absent from the S2.1 rows"),
        ("works named by the build docs' own correction text (Doc_02 SS3 "
         "Revision-Log class) but row-less"),
        ("critical editions and standard translations (deferred to the "
         "pre-freeze re-sweep, ALX pattern)"),
    ],
    "approaches": {
        "deployed-chunk-key-sources-sweep": 1,
        "composite-row-string-adjudication": 1,
        "build-doc-correction-text-read": 1,
        "row-diff": 1,
    },
    "years_searched": {"from": 1894, "to": 2026},
    "languages_searched": ["en"],
    "inclusion_exclusions": (
        "Included: every chunk-cited or correction-text-named work no row "
        "covered at work-or-corpus level, each adjudicated against the "
        "FULL composite string of the nearest existing row before being "
        "called a miss. Excluded: Scripture (native by the Framework's "
        "own rule); works inside existing composite rows (Valavanolickal "
        "-> row 10; Harvey -> row 32; Malki -> row 33; Bar Ebroyo -> row "
        "42; Amar -> row 34); edition-level detail of rowed works "
        "(Doctrina Addai eds. Howard 1981 / Lollar 2023 -> row 20, "
        "deferred to the pre-freeze re-sweep per the ALX editions rule); "
        "second-order apparatus (Acts of Miles + Synodicon Orientale are "
        "the GEDSH Papa-bar-Aggai entry's OWN sources, not chunk-load-"
        "bearing - flagged to the pre-freeze re-sweep rather than rowed "
        "second-hand)."),
    "terms_tried": [
        {"term": ("Key Sources sections + story Source lines, all 19 "
                  "deployed Syriac chunks (diff vs rows)"),
         "productive": True},
        {"term": ("composite-row verbatim pulls for adjudication (rows "
                  "26/29/42/47/51)"),
         "productive": True},
        {"term": ("Doc_02 SS3 / Doc_03 SS1.2 correction-text read (the "
                  "qyama-specific Griffith citations)"),
         "productive": True},
        {"term": "Doc_02 CSCO/Beck edition-table check", "productive": False},
        {"term": ("row-diff re-run after adding the eight sweep rows"),
         "productive": False},
    ],
    "instruments": [
        ("deployed-chunk Key-Sources sweep (the productive instrument; "
         "wrs/migrate/s62_syr_sweep.py)"),
        ("composite-row-string adjudication (prevented four false "
         "misses: Valavanolickal/Harvey/Malki/Bar-Ebroyo)"),
        ("NOT ACCESSED, logged as coverage limits of this migration-time "
         "sweep: BIBP; L'Annee philologique; Oxford Bibliographies; the "
         "Hugoye cumulative index; a systematic GEDSH pass (row 51 + "
         "srcSYR058 carry entries ad hoc). Re-run before world-freeze."),
    ],
}

SEARCH_BODY = (
    "Saturation statement (V7.4 Step 2; migration-time scope): the last "
    "searches of this sweep returned nothing new - the Doc_02 CSCO/Beck "
    "edition-table check re-surfaced only already-rowed Ephrem corpora, "
    "and the row-diff re-run after adding the eight sweep rows found no "
    "remaining row-less citation at work or corpus level across all 19 "
    "chunks. Five instruments remain unsearched (BIBP; L'Annee "
    "philologique; Oxford Bibliographies; the Hugoye cumulative index; a "
    "systematic GEDSH pass) and are recorded as COVERAGE LIMITS, not "
    "satisfied searches; the pre-freeze re-sweep must run them.\n\n"
    "Sweep provenance: wrs/migrate/s62_syr_sweep.py (this file is the "
    "sweep log; the eight added rows srcSYR054-061 carry real "
    "discovery_channel/instrument/date, unlike the migrated srcSYR001-053 "
    "whose historical discovery data is unrecoverable by design).\n\n"
    "Open verification items carried forward (named, not silent): (1) "
    "FLAG-025 - syrlex002 and syrlex007 both cite Griffith 1991 with the "
    "mis-pointer '(Source Registry #26, cross-checked)'; srcSYR056 is the "
    "citation's true home; the chunk text correction rides the S2.8 "
    "render, never a silent patch. (2) The syrlex003 Valavanolickal "
    "2005-vs-2011 printing flag (Doc_03's own open flag) - a row-10 "
    "verification item for the pre-freeze re-sweep. (3) srcSYR061's "
    "journal language (und, declared). (4) Acts of Miles + Synodicon "
    "Orientale - second-order GEDSH apparatus, pre-freeze re-sweep "
    "candidates if any chunk comes to cite them directly. (5) Coverage "
    "finding routed to S2.2: syrlex005 (memra) and syrlex008 (mar) are "
    "Tier-3 chunks with NO Key Sources section - correct for their "
    "tier's thin format; their term records must source from front-"
    "matter alone.")


def main():
    for rec in ROWS:
        body = ("Rowed at the S6.2/SYR S2.1a sweep (2026-07-28) with real "
                "discovery data (the sweep instrument itself). See "
                "wrs/migrate/s62_syr_sweep.py and srcSYRsearch001.")
        emit_record(rec, body, OUT / "source" / f"{rec['id']}.md")
    (OUT / "search_record").mkdir(exist_ok=True)
    emit_record(SEARCH, SEARCH_BODY,
                OUT / "search_record" / "srcSYRsearch001.md")
    print(f"emitted {len(ROWS)} sweep rows + srcSYRsearch001")


if __name__ == "__main__":
    main()
