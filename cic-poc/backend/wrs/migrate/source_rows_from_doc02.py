"""S2.1 migrate script - Desert world_core + source records (blueprint S2.1; M2: Desert).

Desert has no registry artifact (.xlsx/.json) to migrate: its source rows
exist only as prose sections in
World-Builds/Desert-Monasticism/CiC_W3_Doc02_Source_Ecology.md (Doc_02).
This script IS the declared mapping: one entry per Doc_02 source, each field
carrying its provenance. Re-running it regenerates the records byte-for-byte.

THE BACKFILL RULE, applied verbatim (Pass 1 SS3.1): migrated rows are
schema_version: 1; ONLY attribution_status, level_of_description,
language/script, and coarse block-level discovery_channel are backfilled
(supplied coarsely where Doc_02's prose does not state them - exactly what
"backfill" licenses); discovery_instrument and discovery_date are NEVER
set - that information is gone and inventing it is the fabricated-precision
failure. Everything else is MIGRATED, not backfilled: verbatim (or
verbatim-excerpted, marked "...") text from Doc_02's own bullets.

Declared field mapping (the R spot-check diffs against this):
  work_author/work_title/work_locus <- section heading, verbatim split
  transmission_path                 <- the section's "Transmission history:" bullet, verbatim
  verification_note                 <- the section's "Confidence:" bullet, verbatim
                                       (Doc_02's compound per-claim confidence cannot be
                                       collapsed to one enum value without a content
                                       change, so the envelope confidence axes stay
                                       UNSET and the full text is carried here)
  source_type                       <- P (SS1-2 voices/narrative), M (SS5 material), S (SS7 scholarship)
  boundary_status                   <- Native (every Doc_02 entry is used as this world's evidence)
  licensed_for                      <- the section's own stated use, condensed from its
                                       headers only (SS1 primary voices / SS2 narrative /
                                       SS5 material / SS7 secondary scholarship)
  genre_form                        <- only where an enum value honestly fits; otherwise unset
  field_state                       <- only where Doc_02 states one
  added                             <- "2026-07-26 (S2.1 migration from Doc_02)"
  ids                               <- srcDES001.. minted here (Desert had no row ids);
                                       stable from this commit forward

Confidence-vocabulary note: Doc_02 (and the Framework Template Part IV per
Doc_02's own terminology note) spells the fifth level "Inferential / Thin";
the schema enum canonicalizes to "Inferential-Thin". No value is set here
(axes unset per above), so no normalization occurs in this step; recorded
for S2.9's Change-Order attention.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "desert_world"

DOC02 = "World-Builds/Desert-Monasticism/CiC_W3_Doc02_Source_Ecology.md"
DOC01 = "World-Builds/Desert-Monasticism/CiC_W3_Doc01_World_Identification.md"

COMMON = {"world_id": "desert-monasticism", "record_type": "source",
          "schema_version": 1, "register": "etic", "review_state": "draft",
          "boundary_status": "Native", "disposition": "in-use"}

ROWS = [
    # ---- SS1 Primary Voices ----
    dict(id="srcDES001", section="1.1",
         work_author="Athanasius of Alexandria", work_title="Life of Antony (Vita Antonii)",
         work_locus="c. 356-362", source_type="P",
         attribution_status="genuine", level_of_description="work",
         language="grc", script="Grek", genre_form="hagiography",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Primary voice (Doc_02 SS1)",
         transmission_path="the Greek text survives complete; an early Latin translation (Evagrius of Antioch, not to be confused with Evagrius Ponticus) circulated within a generation and is the version that reached the West, including Augustine. This means most of this world's international reception ran through a translator's hand, not the Greek original - a transmission dependency this document flags rather than assumes away.",
         verification_note="Documented as to the text's existence, authorship, and approximate date; Contested as to its reliability for specific biographical incident and for the \"unlettered rustic\" characterization it advances (see Section 1.3 below and Doc_01, Section 10)."),
    dict(id="srcDES002", section="1.2",
         work_author="Pachomius / the Pachomian federation", work_title="Pachomian corpus - the Rules and the Lives of Pachomius",
         work_locus="4th c.; Rules in Jerome's Latin 404 CE", source_type="P",
         attribution_status="genuine", level_of_description="corpus",
         language="cop", script="Copt", genre_form="monastic-rule",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Primary voice (Doc_02 SS1); institutional evidence (Doc_02 SS3)",
         transmission_path="a documented, multi-stage translation chain (Coptic -> Greek -> Jerome's Latin for the Rules; multiple independent Coptic and Greek recensions for the Lives) - each stage a real opportunity for editorial shaping that this world's own most internally-produced textual evidence has already passed through before reaching modern readers.",
         verification_note="Widely Accepted as to the corpus's existence, general content, and Pachomian origin; Contested as to specific incident-level historical reliability and version-priority."),
    dict(id="srcDES003", section="1.3",
         work_author="Antony (attributed)", work_title="The Letters of Antony (seven letters)",
         work_locus="4th c.", source_type="P",
         attribution_status="dubium", level_of_description="corpus",
         language="cop", script="Copt", genre_form="letter",
         discovery_channel="builder-prior-knowledge",
         field_state="contested",
         licensed_for="Primary voice (Doc_02 SS1)",
         transmission_path="transmitted almost entirely through translation (Georgian, Latin, Syriac) with only Greek and Coptic fragments surviving directly - an unusually thin and indirect transmission chain for material this potentially significant, and a genuine limitation on how much weight this document places on it.",
         verification_note="Contested as to authenticity (leaning toward authentic, per the balance of manuscript and citation evidence Rubenson assembles, but not Documented); Contested, and more sharply so, as to the Origenist-influence reading specifically."),
    dict(id="srcDES004", section="1.4",
         work_author="Evagrius Ponticus", work_title="Praktikos; Chapters on Prayer (De oratione); Antirrhetikos",
         work_locus="late 4th c.", source_type="P",
         attribution_status="genuine", level_of_description="corpus",
         language="grc", script="Grek",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Primary voice (Doc_02 SS1)",
         transmission_path="this is this world's single most dramatic transmission-history case. Following the 553 condemnation, Evagrius's more speculative works survive substantially in Syriac and Armenian translation - traditions unaffected by the Constantinopolitan decision - while his Greek manuscripts frequently transmit several of his ascetic-practical works - the Chapters on Prayer above all ... - under pseudonymous attribution, chiefly to Nilus of Ancyra, and occasionally to Basil or Gregory of Nazianzus. A reader encountering \"Nilus\" in a Byzantine or Athonite manuscript may be reading Evagrius. This is Constitution Article 22's Transmission History dimension in its starkest possible instance for this world.",
         verification_note="Widely Accepted as to authorship and general content for the ascetic-practical works; Documented as to the 553 condemnation and its effect on transmission; the specific pseudonymous-attribution pattern is Widely Accepted among specialists in the manuscript tradition specifically."),
    dict(id="srcDES005", section="1.5",
         work_author="anonymous compilers (5th-6th c.)", work_title="Apophthegmata Patrum (Sayings of the Desert Fathers)",
         work_locus="oral origins in-window; compiled 5th-6th c.", source_type="P",
         attribution_status="anonymous", level_of_description="corpus",
         language="grc", script="Grek", genre_form="apophthegm-collection",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Primary voice (Doc_02 SS1)",
         transmission_path="oral transmission across at least one, likely several, generations before written compilation; the compilers themselves function as a distinct Author Gravity layer (shapers, not merely transcribers) and should be assessed with the Framework's Narrative Source Author Gravity criteria, not treated as a neutral archive.",
         verification_note="Widely Accepted as to the corpus's general origin in this world's own oral teaching tradition; Contested as to how faithfully any individual saying preserves its original strand-specific context versus reflecting later compilers' own arrangement."),
    dict(id="srcDES006", section="1.6",
         work_author="Syncletica, Theodora, Sarah (attributed)", work_title="The ammas' sayings within the Apophthegmata tradition",
         work_locus="oral origins in-window; compiled 5th-6th c.", source_type="P",
         attribution_status="attributed-later", level_of_description="aggregate-attestation",
         language="grc", script="Grek", genre_form="apophthegm-collection",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Primary voice (Doc_02 SS1); the only direct textual evidence for women's own teaching voice",
         transmission_path="identical mechanism to Section 1.5; no independent transmission stream exists for the ammas' material.",
         verification_note="Widely Accepted that named ammas and their sayings are a genuine, if thin, part of the Apophthegmata tradition; Inferential / Thin for any claim beyond what the surviving sayings themselves state."),
    # ---- SS2 Narrative sources ----
    dict(id="srcDES007", section="2.1",
         work_author="Palladius of Galatia", work_title="Lausiac History",
         work_locus="c. 419-420", source_type="P",
         attribution_status="genuine", level_of_description="work",
         language="grc", script="Grek",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Narrative source (Doc_02 SS2)",
         transmission_path="the Greek original is complicated by an extensive later reception history, including a considerably expanded Latin recension; textual criticism of the Lausiac History's manuscript tradition is itself a specialist field this document has not independently adjudicated.",
         verification_note="Widely Accepted as to authorship, approximate date, and general content; Inferential / Thin as to specific numerical claims (e.g., the Nitria population figure, Doc_01 Section 2.2, corrected per Doc_01 Round 2 review to attribute the ~5,000 figure to Nitria alone)."),
    dict(id="srcDES008", section="2.2",
         work_author="anonymous (Mount of Olives community); Rufinus of Aquileia (Latin adaptation)",
         work_title="Historia Monachorum in Aegypto (Greek, c. 394-395) with Rufinus's Latin translation/adaptation (c. 403)",
         work_locus="c. 394-395 / c. 403", source_type="P",
         attribution_status="anonymous", level_of_description="work",
         language="grc", script="Grek",
         discovery_channel="builder-prior-knowledge",
         field_state="majority",
         licensed_for="Narrative source (Doc_02 SS2)",
         transmission_path="an early and unusually well-documented case - the relationship between the Greek original and Rufinus's Latin version was itself historically disputed (an older view, since superseded, held Rufinus's Latin was the original and the Greek a back-translation); the now-dominant scholarly view ... following C. Butler's philological demonstration, holds the Greek is original and Rufinus's Latin a translation-with-additions.",
         verification_note="Widely Accepted as to the Greek-original-then-Latin-translation relationship (downgraded from Documented per Round 1 review, Finding 3 ...); Inferential / Thin as to the anonymous author's specific identity."),
    # ---- SS5 Material culture ----
    dict(id="srcDES009", section="5.1",
         work_author="French and Swiss archaeological teams (Antoine Guillaumont, discovery 1964)",
         work_title="The Kellia excavations (1965-1990)",
         work_locus="site c. 125 km2, 1,500+ structures", source_type="M",
         attribution_status="genuine", level_of_description="aggregate-attestation",
         language="und",
         discovery_channel="database-search",
         licensed_for="Material culture and daily life (Doc_02 SS5)",
         verification_note="Documented as to the excavation's existence, dates, teams, and general findings; Inferential / Thin as to connecting any specific excavated structure to a specific named figure from the textual tradition."),
    dict(id="srcDES010", section="5.2",
         work_author="Paieous, Nepheros, and correspondents (Melitian community, Hipponon)",
         work_title="The Nepheros archive (4th-c. papyrological correspondence)",
         work_locus="4th c., Heracleopolite nome", source_type="M",
         attribution_status="genuine", level_of_description="corpus",
         language="grc", script="Grek", genre_form="letter",
         discovery_channel="database-search",
         licensed_for="Material/institutional evidence (Doc_02 SS3, SS5); Melitian qualification per SS5.2",
         verification_note="Included on the working assumption - not yet independently verified - that Melitian and Nicene-communion ascetic practice were not organizationally distinct in most day-to-day respects, only in their ecclesial allegiance (Doc_02 SS5.2; open item 5)."),
    dict(id="srcDES011", section="5.3",
         work_author="unknown (contested Pachomian-proximity theory)",
         work_title="The Nag Hammadi codices (discovered 1945)",
         work_locus="Upper Egypt, near the Pachomian federation's territory", source_type="M",
         attribution_status="anonymous", level_of_description="corpus",
         language="cop", script="Copt",
         discovery_channel="database-search",
         field_state="contested",
         licensed_for="Material evidence, relation to this world unresolved (Doc_02 SS5.3; open item 3 - this document adopts neither position)",
         verification_note="Contested: the monastic-origin and burial-as-response-to-Athanasius theory (Robinson; Lundhaug and Jenott) versus private-ownership/grave-goods alternatives. This document does not adopt either position."),
    # ---- SS7 Secondary scholarship ----
    dict(id="srcDES012", section="7",
         work_author="David Brakke", work_title="Athanasius and the Politics of Asceticism (Oxford: Clarendon Press, 1995; reissued as Athanasius and Asceticism, Johns Hopkins University Press, 1998); Demons and the Making of the Monk: Spiritual Combat in Early Christianity (Harvard University Press, 2006)",
         work_locus="1995/2006", source_type="S",
         attribution_status="genuine", level_of_description="corpus",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="step0-seed-list",
         licensed_for="Secondary scholarship (Doc_02 SS7): critical treatment of Athanasius as interested author; demon-combat as constructed category",
         verification_note="Retained per Step 0's explicit instruction (Doc_01, Section 9)."),
    dict(id="srcDES013", section="7",
         work_author="Samuel Rubenson", work_title="The Letters of St. Antony: Monasticism and the Making of a Saint (Fortress Press, 1995; originally published with the subtitle Origenist Theology, Monastic Tradition and the Making of a Saint, Lund University Press, 1990)",
         work_locus="1990/1995", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="step0-seed-list",
         licensed_for="Secondary scholarship (Doc_02 SS7): anchors SS1.3 and the Rubenson/Athanasius tension",
         verification_note="Added per Step 0's instruction."),
    dict(id="srcDES014", section="7",
         work_author="Douglas Burton-Christie", work_title="The Word in the Desert: Scripture and the Quest for Holiness in Early Christian Monasticism (Oxford University Press, 1993)",
         work_locus="1993", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="step0-seed-list",
         licensed_for="Secondary scholarship (Doc_02 SS7): reserved for Doc_05 Interpretive Habits",
         verification_note="Added per Step 0's instruction."),
    dict(id="srcDES015", section="7",
         work_author="James Goehring", work_title="Ascetics, Society, and the Desert: Studies in Early Egyptian Monasticism (Trinity Press International, 1999)",
         work_locus="1999", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="database-search",
         licensed_for="Secondary scholarship (Doc_02 SS7): documentary/papyrological challenge to the flight-to-the-desert narrative",
         verification_note="Not named by Step 0 but surfaced during Doc_01's drafting; specific claims not yet independently verified (Doc_02 open item 4)."),
    dict(id="srcDES016", section="7",
         work_author="Philip Rousseau", work_title="Pachomius: The Making of a Community in Fourth-Century Egypt (University of California Press, 1985)",
         work_locus="1985", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Secondary scholarship (Doc_02 SS7): the standard critical study of the Pachomian sources; anchors SS1.2",
         verification_note="The standard critical study of the Pachomian sources (Doc_02 SS7; no Step-0 annotation)."),
]

WORLD_CORE = {
    "id": "desertcore001", "world_id": "desert-monasticism",
    "record_type": "world_core", "schema_version": 1, "register": "etic",
    "review_state": "draft", "jobs": [7, 3],
    "time_window": {"start_year": 320, "end_year": 430,
                     "note": 'c. 320-430 CE - world_manifest.py period="c. 320-430 CE"; Doc_01 SS2: floor c. 320 (Tabennesi), close c. 430 proposed as directional; Antony\'s pre-floor career (c. 270s-305) is generative background, not a boundary extension (Doc_01 SS2.1).'},
    "horizon": 'Egypt (Nile valley and desert) - Step 0 scope note quoted in Doc_01; the desert margins: Nitria (c. 325-330), Scetis (c. 330), Kellia (c. 338), the Pachomian Thebaid; three organizational strands (solitary, cenobitic, semi-anchoritic) per Doc_01 SS1/SS6.',
    "formation_logic": 'Doc_01 SS1 (verbatim): "withdrawal from settled village and civic life into marginal or genuinely remote land, undertaken as the ascetic project itself - not merely a change of address but a formation method in which distance, solitude, manual labor, and susceptibility to demonic testing are themselves the curriculum."',
    "gravities": [],
    "sources": [{"source_id": "srcDES001"}, {"source_id": "srcDES005"}],
}


def emit_record(rec: dict, body: str, path: Path):
    import yaml
    front = yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=100)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{front}---\n{body}\n", encoding="utf-8", newline="\n")


def main():
    for row in ROWS:
        section = row.pop("section")
        rec = {**COMMON, **row, "jobs": [1, 2]}
        body = (f"Migrated at S2.1 (2026-07-26) from `{DOC02}` Section {section}. "
                f"Mapping and backfill rule: see `wrs/migrate/source_rows_from_doc02.py`. "
                f"Prose fields are verbatim (or verbatim-excerpted, marked '...') from that section.")
        rec["added"] = "2026-07-26 (S2.1 migration from Doc_02)"
        emit_record(rec, body, OUT / "source" / f"{rec['id']}.md")
    emit_record(WORLD_CORE,
                f"Migrated at S2.1 (2026-07-26) from `{DOC01}` (SS1, SS2) and "
                f"`cic-poc/backend/app/world_manifest.py` (period). gravities[] "
                f"deliberately empty until S2.5 authors the gravity records; "
                f"pairing_guidance/cautions arrive at S2.7a.",
                OUT / "world_core" / "desertcore001.md")
    print(f"wrote {len(ROWS)} source records + 1 world_core to {OUT}")


if __name__ == "__main__":
    main()
