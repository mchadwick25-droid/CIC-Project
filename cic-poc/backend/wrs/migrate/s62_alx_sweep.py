"""S6.2/Alexandria - S2.1a-equivalent discovery sweep (+ search_record).

THE FIRST SWEEP UNDER THE GOVERNING V7.4 STEP 2 STANDARD (adopted at
S6.1): search_record kept as searches happen with real instrument/date
per search; field-bibliography instruments dispositioned or logged as
coverage limits; saturation statement naming the last unproductive
searches (Completion Standard V1.0 SSA source row).

What this sweep did (migration-time scope per F2, like Desert's):

1. DEPLOYED-CHUNK KEY-SOURCES SWEEP (the productive instrument): every
   `## Key Sources` section of the 45 deployed lexicon chunks
   (data/alexandria_world/lexicon_chunks/) grep-swept and diffed
   against srcALX001-026. Findings: SIX load-bearing, row-less works -
   headed by Athanasius's On the Incarnation, the single most-cited
   work in the whole deployed lexicon, which the S2.1 rows covered
   only implicitly under the ALX003 corpus title.
2. BUILD-DOC SATURATION PASSES (unproductive - the saturation
   evidence): asterisked work-title greps over Doc_05 and Doc_09
   re-surfaced only already-rowed works (Address -> srcALX007, Contra
   Celsum -> srcALX002/015, Apophthegmata -> srcALX011) and non-work
   phrases; the row-diff after adding the six found nothing further.
3. COVERAGE LIMITS, logged not satisfied: BIBP and L'Annee philologique
   (inaccessible from this environment); the Oxford Bibliographies
   current-scholarship check and CPG-against-printed-Clavis
   re-verification not performed. Recorded as limits of this
   migration-time sweep; re-run before world-freeze.

Boundary judgment, logged for the S2.1b coverage check to contest: the
three pre-Alexandrian reception-formative texts (Ignatius, Irenaeus,
Tertullian) enter as Native under the Construction Framework V7.4's own
native-not-exclusive rule ("real traditions inherit from and cite one
another constantly"), with licensed_for restricted to
reception-evidence - the chunks cite them for how Alexandria RECEIVED
their concepts, never as Alexandrian voices.

Deterministic; re-run regenerates byte-for-byte.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "alexandria_world"

COMMON = {"world_id": "alexandria-catechetical", "record_type": "source",
          "schema_version": 1, "register": "etic", "review_state": "draft",
          "boundary_status": "Native", "disposition": "in-use"}

SWEEP_DATE = "2026-07-27"
SWEEP_INSTRUMENT = ("deployed-chunk Key-Sources sweep (grep over the 45 "
                    "data/alexandria_world/lexicon_chunks Key Sources "
                    "sections, diffed against srcALX001-026; "
                    "wrs/migrate/s62_alx_sweep.py)")

ROWS = [
    dict(id="srcALX027",
         work_author="Athanasius", work_title="On the Incarnation (De incarnatione)",
         work_locus="early career, before c. 328 (conventional; dating debated)",
         source_type="P", attribution_status="genuine", level_of_description="work",
         language="grc", script="Grek",
         discovery_channel="backward-snowball", discovery_instrument=SWEEP_INSTRUMENT,
         discovery_date=SWEEP_DATE,
         licensed_for=("The single most-cited work across the deployed lexicon's Key Sources "
                       "(theosis, restoration, image/likeness, resurrection, sin-as-disorientation, "
                       "the ch. 54 deification formula); surfaced at sweep as work-level "
                       "load-bearing - the S2.1 rows carried it only implicitly inside "
                       "srcALX003's corpus title"),
         verification_note=("Added at S6.2 sweep with real discovery data. Work-level row for a "
                            "text the deployed chunks cite by chapter (chs. 1-10, 3-8, 20-32, 54); "
                            "authorship undisputed; precise dating conventional.")),
    dict(id="srcALX028",
         work_author="Clement of Alexandria", work_title="Quis Dives Salvetur (Who Is the Rich Man That Shall Be Saved?)",
         work_locus="c. 190-210", source_type="P",
         attribution_status="genuine", level_of_description="work",
         language="grc", script="Grek", genre_form="homily",
         discovery_channel="backward-snowball", discovery_instrument=SWEEP_INSTRUMENT,
         discovery_date=SWEEP_DATE,
         licensed_for=("Cited by the deployed Eucharist and ekklesia chunks (participation; the "
                       "community gathered around the Logos); row-less at S2.1 because "
                       "srcALX001's title names only the trilogy"),
         verification_note="Added at S6.2 sweep with real discovery data; authorship undisputed."),
    dict(id="srcALX029",
         work_author="Council of Nicaea", work_title="The Nicene Creed",
         work_locus="325 CE", source_type="P",
         attribution_status="genuine", level_of_description="work",
         language="grc", script="Grek", genre_form="conciliar-act",
         discovery_channel="backward-snowball", discovery_instrument=SWEEP_INSTRUMENT,
         discovery_date=SWEEP_DATE,
         licensed_for=("Cited repeatedly by the deployed chunks (homoousios; 'God from God, Light "
                       "from Light'; the post-325 confession) - the doctrinal-boundary text of the "
                       "world's own late horizon (Doc_01 SS2.3a: Nicaea internal, not a boundary)"),
         verification_note="Added at S6.2 sweep with real discovery data; the 325 text as received in the world's own confession and Athanasius's defense."),
    dict(id="srcALX030",
         work_author="Ignatius of Antioch", work_title="Letters",
         work_locus="early 2nd c. (pre-horizon)", source_type="P",
         attribution_status="genuine", level_of_description="corpus",
         language="grc", script="Grek", genre_form="letter",
         discovery_channel="backward-snowball", discovery_instrument=SWEEP_INSTRUMENT,
         discovery_date=SWEEP_DATE,
         licensed_for=("RECEPTION-EVIDENCE ONLY: the deployed episcopate and mysterion chunks cite "
                       "Ignatius as 'pre-Alexandrian but formative for this world's episcopal "
                       "theology' - evidence of what Alexandria received, never an Alexandrian "
                       "voice (V7.4 native-not-exclusive rule; judgment logged for the S2.1b "
                       "coverage check)"),
         verification_note="Added at S6.2 sweep with real discovery data. Middle-recension authenticity is the scholarly standard position; pre-horizon provenance is exactly why licensed_for is restricted."),
    dict(id="srcALX031",
         work_author="Irenaeus of Lyon", work_title="Against Heresies",
         work_locus="c. 180 (pre/extra-horizon)", source_type="P",
         attribution_status="genuine", level_of_description="work",
         language="grc", script="Grek", genre_form="polemic",
         discovery_channel="backward-snowball", discovery_instrument=SWEEP_INSTRUMENT,
         discovery_date=SWEEP_DATE,
         licensed_for=("RECEPTION-EVIDENCE ONLY: cited by the Rule-of-Faith and oikonomia chunks "
                       "as 'pre-Alexandrian, but formative for how the term is received here' "
                       "(recapitulation; the Rule as apostolic deposit) - same restriction and "
                       "logged judgment as srcALX030"),
         verification_note="Added at S6.2 sweep with real discovery data."),
    dict(id="srcALX032",
         work_author="Tertullian", work_title="Prescription Against Heretics",
         work_locus="c. 200 (extra-horizon, Latin North Africa)", source_type="P",
         attribution_status="genuine", level_of_description="work",
         language="lat", script="Latn", genre_form="polemic",
         discovery_channel="backward-snowball", discovery_instrument=SWEEP_INSTRUMENT,
         discovery_date=SWEEP_DATE,
         licensed_for=("RECEPTION-EVIDENCE ONLY: cited once, by the Rule-of-Faith chunk (the Rule "
                       "as what apostolic communities hand down) - same restriction and logged "
                       "judgment as srcALX030"),
         verification_note="Added at S6.2 sweep with real discovery data; the single lightest-use sweep row, added because the Rule-of-Faith chunk's Key Sources names it as load-bearing for that entry."),
]

SEARCH_RECORD = {
    "id": "srcALXsearch001", "world_id": "alexandria-catechetical",
    "record_type": "search_record", "schema_version": 1, "register": "etic",
    "review_state": "draft", "jobs": [1],
    "sampling_strategy": ("Purposive, not comprehensive (Booth's standard) - EXPLICITLY SCOPED AS A "
                          "MIGRATION-TIME SEARCH (2026-07-27, S6.2 per F2), documenting this sweep "
                          "only, never the original build's own discovery process (unrecoverable by "
                          "design per the backfill rule). FIRST SWEEP UNDER THE GOVERNING V7.4 "
                          "STEP 2 STANDARD (S6.1)."),
    "types_sought": [
        "works load-bearing in the deployed chunks' own Key Sources but absent from the S2.1 rows",
        "works load-bearing in Doc_05/Doc_09 prose but row-less",
        "critical editions and standard translations (deferred to pre-freeze re-sweep)",
    ],
    "approaches": {"deployed-chunk-key-sources-sweep": 1, "build-doc-title-grep": 2,
                   "row-diff": 1},
    "years_searched": {"from": 1966, "to": 2026},
    "languages_searched": ["en"],
    "inclusion_exclusions": ("Included: every work the deployed chunks' Key Sources cite that no "
                             "row covered at work-or-corpus level. Excluded: Scripture (native by "
                             "the Framework's own rule, never rowed separately); works already "
                             "covered at corpus level (all Origen citations resolve into "
                             "srcALX002's named corpus; Festal Letters/Orations/Serapion/"
                             "Marcellinus/Defense resolve into srcALX003's corpus title); "
                             "'Anno Martyrum' (an era-name, not a work)."),
    "terms_tried": [
        {"term": "Key Sources sections, all 45 deployed lexicon chunks (grep + diff vs rows)",
         "productive": True},
        {"term": "Doc_05 asterisked work-title grep", "productive": False},
        {"term": "Doc_09 asterisked work-title grep", "productive": False},
        {"term": "row-diff re-run after adding the six sweep rows", "productive": False},
    ],
    "instruments": [
        "deployed-chunk Key-Sources sweep (the productive instrument; wrs/migrate/s62_alx_sweep.py)",
        "Doc_05/Doc_09 asterisked-title greps (saturation passes)",
        ("NOT ACCESSED, logged as coverage limits of this migration-time sweep: BIBP; L'Annee "
         "philologique; the Oxford Bibliographies current-scholarship check; CPG re-verification "
         "against the printed Clavis. Re-run before world-freeze."),
    ],
}

SATURATION_BODY = (
    "Saturation statement (the governing V7.4 Step 2 standard's requirement, first applied here; "
    "migration-time scope): the last searches of this sweep returned nothing new - the Doc_05 and "
    "Doc_09 asterisked-title greps re-surfaced only already-rowed works (the Address -> srcALX007, "
    "Contra Celsum -> srcALX002/srcALX015, Apophthegmata -> srcALX011) and non-work phrases, and "
    "the row-diff re-run after adding the six sweep rows found no remaining row-less citation at "
    "work or corpus level. Four instruments remain unsearched (BIBP; L'Annee philologique; Oxford "
    "Bibliographies; CPG-against-printed-Clavis) and are recorded as COVERAGE LIMITS of this "
    "migration-time sweep, not as satisfied searches; the pre-freeze re-sweep must run them.\n\n"
    "Sweep provenance: wrs/migrate/s62_alx_sweep.py (this file is the sweep log; the six added "
    "rows srcALX027-032 carry real discovery_channel/instrument/date, unlike the migrated "
    "srcALX001-026 whose historical discovery data is unrecoverable by design)."
)


def emit_record(rec: dict, body: str, path: Path):
    import yaml
    front = yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=100)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{front}---\n{body}\n", encoding="utf-8", newline="\n")


def main():
    for row in ROWS:
        rec = {**COMMON, **dict(row), "jobs": [1, 2]}
        rec["added"] = f"{SWEEP_DATE} (S6.2 S2.1a-equivalent discovery sweep)"
        body = (f"Added at the S6.2 sweep ({SWEEP_DATE}) with REAL discovery data. "
                f"Sweep log: `wrs/migrate/s62_alx_sweep.py`; search record: srcALXsearch001.")
        emit_record(rec, body, OUT / "source" / f"{rec['id']}.md")
    emit_record(SEARCH_RECORD, SATURATION_BODY,
                OUT / "search_record" / "srcALXsearch001.md")
    print(f"wrote {len(ROWS)} sweep rows + srcALXsearch001 to {OUT}")


if __name__ == "__main__":
    main()
