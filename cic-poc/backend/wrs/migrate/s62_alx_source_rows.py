"""S6.2 migrate script - Alexandria world_core + source records (S2.1-equivalent;
fleet order per decisions/S6.2_M_fleet_order.md: Alexandria first).

Alexandria's source rows exist as structured prose in
World-Builds/Alexandria-Catechetical-School/Doc_02_Source_Ecology.md
(SS3 Author Gravity five-dimension entries; SS4 verified secondary
scholarship; SS5 narrative/hagiographic sources with provisional tiers;
SS8 material culture). This script IS the declared mapping, mirroring
wrs/migrate/source_rows_from_doc02.py (Desert's) conventions exactly.
Re-running regenerates the records byte-for-byte.

THE BACKFILL RULE, applied verbatim (Pass 1 SS3.1 / Completion Standard
V1.0 SSA source row): ONLY attribution_status, level_of_description,
language/script, and coarse block-level discovery_channel are
backfilled; discovery_instrument and discovery_date are NEVER set for
migrated rows (that information is gone; inventing it is the
fabricated-precision failure). Everything else is MIGRATED: verbatim
(or verbatim-excerpted, marked "...") text from Doc_02's own bullets.

Declared field mapping (the R spot-check diffs against this):
  work_author/work_title/work_locus <- section heading, verbatim split
  transmission_path                 <- the entry's "Transmission history:" bullet, verbatim
  verification_note                 <- the entry's Risk/Confidence/Tier text, verbatim-excerpted
                                       (compound per-claim confidence is carried whole;
                                       envelope confidence axes stay UNSET)
  source_type                       <- P (SS3 voices + SS5 narrative), S (SS4), M (SS8)
  boundary_status                   <- Native, EXCEPT Philo (SS3.5: "diagnostic, not a
                                       source within the world") -> Excluded / Named
                                       Comparandum, Doc_02's own words carried
  licensed_for                      <- the entry's own stated use, condensed from its
                                       section headers + risk classification
  field_state                      <- only where Doc_02 states one (e.g. the named
                                       live debate; cross-build provisional flags)
  added                             <- "2026-07-27 (S6.2 migration from Doc_02)"
  ids                               <- srcALX001.. minted here; stable from this commit

Cross-build provisional flags (Doc_01 SS3.3) are carried in
verification_note verbatim - the desert-attribution question is held
open by the SOURCE ROWS, exactly as Doc_02 holds it.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "alexandria_world"

DOC02 = "World-Builds/Alexandria-Catechetical-School/Doc_02_Source_Ecology.md"
DOC01 = "World-Builds/Alexandria-Catechetical-School/Doc_01_World_Identification_Boundaries_Orientation.md"

COMMON = {"world_id": "alexandria-catechetical", "record_type": "source",
          "schema_version": 1, "register": "etic", "review_state": "draft",
          "boundary_status": "Native", "disposition": "in-use"}

ROWS = [
    # ---- SS3 Author Gravity: primary voices ----
    dict(id="srcALX001", section="3.2",
         work_author="Clement of Alexandria", work_title="Protreptikos; Paedagogus; Stromateis",
         work_locus="c. 150-215", source_type="P",
         attribution_status="genuine", level_of_description="corpus",
         language="grc", script="Grek",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Primary voice (Doc_02 SS3.2); Streams 5 and 6 with named over-representation risk",
         transmission_path="Greek text survives reasonably directly; the Stromateis is textually difficult but not adversarially transmitted.",
         verification_note="Visibility: Significant (Protreptikos, Paedagogus, Stromateis survive), but much catechetical/homiletical work is lost. Risk: High for Streams 5 and 6 specifically (his concentration there can make them look more ecologically central than they were)."),
    dict(id="srcALX002", section="3.1",
         work_author="Origen", work_title="Surviving corpus (commentaries, homilies, De principiis, Contra Celsum)",
         work_locus="c. 185-254; Caesarea from c. 231-234", source_type="P",
         attribution_status="genuine", level_of_description="corpus",
         language="grc", script="Grek",
         discovery_channel="builder-prior-knowledge",
         field_state="contested",
         licensed_for="Primary voice (Doc_02 SS3.1); Streams 1, 2, 4, 5, 6 - under the standing SYSTEMIC Author-Gravity screen",
         transmission_path="A large part of his corpus survives only in Latin translation - Rufinus, who softened doctrinally suspect passages, and Jerome, who (after turning against him) quoted him to discredit him. Fine-grained claims about Origen's precise positions must be held with this adversarial/edited transmission in view.",
         verification_note="Risk classification: SYSTEMIC. Multiple candidate gravities are attested primarily through Origen. The Author-Gravity screening question must stay active throughout: is this the ecology's pattern, or Origen's? His evidence also clusters mid-horizon, compounding author-dominance with period-dominance. Named live debate carried, not resolved (Doc_02 SS4): the relationship between Origen's own theology and the \"Origenism\" condemned in 553."),
    dict(id="srcALX003", section="3.3",
         work_author="Athanasius", work_title="Anti-Arian corpus; Festal Letters; apologetic and pastoral works",
         work_locus="c. 296-373; post-Nicene concentration", source_type="P",
         attribution_status="genuine", level_of_description="corpus",
         language="grc", script="Grek",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Primary voice (Doc_02 SS3.3); late-horizon episcopal perspective - must not characterize the pre-Nicene period",
         transmission_path="Well-transmitted in Greek, with significant Coptic and Syriac witnesses expanding the corpus (Brakke).",
         verification_note="Representativeness: Partial; a bishop addressing his community - the perspective is episcopal, not the community describing itself. Risk: Stream 12 over-representation for the late horizon."),
    dict(id="srcALX004", section="5.2",
         work_author="Athanasius", work_title="Life of Antony",
         work_locus="c. 356-362", source_type="P",
         attribution_status="genuine", level_of_description="work",
         language="grc", script="Grek", genre_form="hagiography",
         discovery_channel="builder-prior-knowledge",
         field_state="contested",
         licensed_for="Formation narrative (Doc_02 SS5.2), Tier 3 (Attributed/Hagiographic Tradition); links Alexandrian theology to monasticism",
         transmission_path="Within living memory of its subject; hagiographic conventions (call narrative, temptation sequence, exemplary death) shape the whole.",
         verification_note="The formation ideal it communicates is credible evidence; the specific episodes (visions, demonic combat, miracles) are not historical reporting. Tier 3. Cross-build note: where used as evidence of the desert tradition's own formation logic, the cross-build constraint applies regardless of framing (Doc_01 SS3.3); and Rubenson's literate-Antony argument means even the \"unlettered\" premise is contested."),
    dict(id="srcALX005", section="3.4",
         work_author="Didymus the Blind", work_title="Tura commentaries (Psalms, Job, Zechariah)",
         work_locus="c. 313-398; recovered 1941", source_type="P",
         attribution_status="genuine", level_of_description="corpus",
         language="grc", script="Grek", genre_form="commentary",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Primary voice (Doc_02 SS3.4); carries Origenian exegesis into the late 4th century",
         transmission_path="Lost for centuries after his posthumous association with condemned Origenism; recovered only in the 20th century (the Tura find, 1941).",
         verification_note="Risk: Moderate - confirms and extends Origen's patterns without introducing new ones (which can create an illusion of independent corroboration where it is really the same tradition)."),
    dict(id="srcALX006", section="3.6",
         work_author="Dionysius of Alexandria", work_title="Letters and fragments (via Eusebius)",
         work_locus="bishop c. 248-264", source_type="P",
         attribution_status="genuine", level_of_description="corpus",
         language="grc", script="Grek", genre_form="letter",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Primary voice, thinly and mediately attested (Doc_02 SS3.6); Streams 7 and 8 (teacher-to-bishop transition; Decian crisis governance)",
         transmission_path="Doubly mediated - his own selection of what to write, then Eusebius's selection of what to preserve; almost nothing survives unmediated.",
         verification_note="Risk classification: Moderate, inheriting Eusebius's transmission risk on top of his own. Concentrates on discipline, authority, and crisis rather than ordinary formation."),
    dict(id="srcALX007", section="3.6",
         work_author="Gregory Thaumaturgus", work_title="Address of Thanksgiving to Origen",
         work_locus="delivered c. 238", source_type="P",
         attribution_status="genuine", level_of_description="work",
         language="grc", script="Grek",
         discovery_channel="builder-prior-knowledge",
         licensed_for="First-person formation-narrative (Doc_02 SS3.6, SS5.1), Tier 1 at the narrative level; the best single witness to the teacher-student formation relationship",
         transmission_path="Direct Greek manuscript transmission, no adversarial translation layer - but the authenticity and dating were questioned by Nautin and reaffirmed by later scholarship (Markschies, Mitchell), so the c. 238 dating is carried with that named caveat.",
         verification_note="Risk classification: Low, with the Nautin authenticity/dating caveat attached wherever the Address is dated or relied on. A single student's-eye view - one gifted pupil, not the school's ordinary student; epideictic genre idealizes (though it does not fabricate)."),
    dict(id="srcALX008", section="3.5",
         work_author="Philo of Alexandria", work_title="Corpus (diagnostic use only)",
         work_locus="c. 20 BCE - c. 50 CE", source_type="P",
         attribution_status="genuine", level_of_description="corpus",
         language="grc", script="Grek",
         discovery_channel="builder-prior-knowledge",
         boundary_status="Excluded", exclusion_reason="Named Comparandum",
         licensed_for="Diagnostic only (Doc_02 SS3.5): to distinguish what Alexandrian Christians inherited from what they transformed or invented - never evidence for Christian formation practice",
         transmission_path="Jewish, pre-horizon, and absent from the evidence streams.",
         verification_note="Doc_02 SS3.5 verbatim: \"diagnostic, not a source within the world.\" Confidence: Widely Accepted for the Philonic inheritance as inherited grammar (Runia 1993; van den Hoek 1988)."),
    # ---- SS3.6/SS5 narrative sources ----
    dict(id="srcALX009", section="3.6",
         work_author="Eusebius of Caesarea", work_title="Ecclesiastical History",
         work_locus="c. 260-339; HE early 4th c.", source_type="P",
         attribution_status="genuine", level_of_description="work",
         language="grc", script="Grek",
         # genre_form unset: the enum has no historiography value and the
         # backfill rule is "only where an enum value honestly fits"
         discovery_channel="builder-prior-knowledge",
         field_state="contested",
         licensed_for="Secondary narrative source (Doc_02 SS3.6): the primary - often sole - scaffolding for pre-4th-century institutional history and school personnel; HIGH-risk screen for institutional/succession/biographical claims",
         transmission_path="The Greek text survives reasonably directly; the risk is interpretive, not textual - the danger is trusting his construction of institutional order, not a corrupted text.",
         verification_note="Risk classification: HIGH for institutional/succession/biographical claims specifically (lower for his verbatim quotation of documents, e.g. Dionysius's letters). His account of an orderly head-succession has been questioned by modern scholars as more institutionally orderly than the independent evidence supports - the direct basis of the Doc_01 SS1.2 Contested finding on the didaskaleion's institutional form."),
    dict(id="srcALX010", section="3.6",
         work_author="Palladius", work_title="Lausiac History",
         work_locus="c. 419-420; author c. 363-420s", source_type="P",
         attribution_status="genuine", level_of_description="work",
         language="grc", script="Grek", genre_form="hagiography",
         discovery_channel="builder-prior-knowledge",
         field_state="contested",
         licensed_for="Hagiographic/travel narrative (Doc_02 SS3.6, SS5.3): Tier 1 for Palladius's own direct encounters (including Didymus); Tier 3 for received accounts",
         transmission_path="Survives in multiple Greek recensions with live textual scholarship and later editorial accretions - attribution of specific material to Palladius's own witness is not always secure.",
         verification_note="Risk classification: Moderate - high value for personally-witnessed material (notably his meeting with Didymus), lower for received accounts; the desert-formation content additionally carries the cross-build provisional flag (world-attribution held open, Doc_01 SS3.3)."),
    dict(id="srcALX011", section="5.4",
         work_author="anonymous compilers", work_title="Apophthegmata Patrum",
         work_locus="collected late 4th-5th c.", source_type="P",
         attribution_status="anonymous", level_of_description="corpus",
         language="grc", script="Grek", genre_form="apophthegm-collection",
         discovery_channel="builder-prior-knowledge",
         field_state="contested",
         licensed_for="Collected traditional material (Doc_02 SS5.4), Tier 2; cross-build provisional (world-attribution held open)",
         transmission_path="The collection tradition is well-attested; individual attributions (Antony, Macarius, Poemen, and others, plus anonymous material) carry only moderate confidence.",
         verification_note="Tier 2 (Collected Traditional Material). Cross-build provisional (world-attribution held open) - Doc_01 SS3.3; the same corpus is a Desert-world primary source (srcDES005), and which world's evidence any given saying is remains a held-open question, not a settled fact."),
    dict(id="srcALX012", section="5.5",
         work_author="Jerome", work_title="On Illustrious Men; Letters",
         work_locus="late 4th c.", source_type="P",
         attribution_status="genuine", level_of_description="corpus",
         language="lat", script="Latn",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Narrative source (Doc_02 SS5.5): Tier 1 for his own direct testimony (including brief study with Didymus)",
         transmission_path="Direct Latin transmission; the interpretive risk is positional, not textual.",
         verification_note="Tier 1 for his own direct testimony, with the explicit caveat that his later anti-Origenist position colors his retrospective treatment of Origen-associated figures."),
    # ---- SS4 Secondary scholarship (all independently verified for Doc_02) ----
    dict(id="srcALX013", section="4",
         work_author="Frances M. Young", work_title="Biblical Exegesis and the Formation of Christian Culture (Cambridge UP, 1997)",
         work_locus="1997", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): the leading treatment of patristic exegesis as formation; shapes how Streams 1, 2, 5 are read",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    dict(id="srcALX014", section="4",
         work_author="Annewies van den Hoek", work_title="Clement of Alexandria and His Use of Philo in the Stromateis (Brill, 1988)",
         work_locus="1988", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): grounds the Philonic-inheritance claim (Stream 6; SS3.5)",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    dict(id="srcALX015", section="4",
         work_author="Henry Chadwick", work_title="Early Christian Thought and the Classical Tradition (Clarendon, 1966); Origen: Contra Celsum (CUP, 1953)",
         work_locus="1966; 1953", source_type="S",
         attribution_status="genuine", level_of_description="corpus",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): the standard framing of Justin/Clement/Origen's engagement with Greek philosophy, and the standard English Contra Celsum",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    dict(id="srcALX016", section="4",
         work_author="Andrew Louth", work_title="The Origins of the Christian Mystical Tradition: From Plato to Denys (Clarendon, 1981; 2nd ed. 2007)",
         work_locus="1981/2007", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): the Platonic shaping of Christian contemplative theology; informs Stream 4",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    dict(id="srcALX017", section="4",
         work_author="Rowan Williams", work_title="Arius: Heresy and Tradition (DLT 1987; rev. SCM 2001)",
         work_locus="1987/2001", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): situates Arius within the Origenian Alexandrian tradition - reframes Stream 12 as internal to this world's own intellectual descent",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    dict(id="srcALX018", section="4",
         work_author="Samuel Rubenson", work_title="The Letters of St. Antony (Lund 1990; Fortress 1995)",
         work_locus="1990/1995", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): the literate-Antony argument; directly bears on the desert world-attribution question (Stream 9; SS6)",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17. Cuts against any simple reading of Antony as proof that desert formation diverged from the learned gravity."),
    dict(id="srcALX019", section="4",
         work_author="David Brakke", work_title="Athanasius and the Politics of Asceticism (Clarendon, 1995); Demons and the Making of the Monk (Harvard, 2006)",
         work_locus="1995; 2006", source_type="S",
         attribution_status="genuine", level_of_description="corpus",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): the Life of Antony as episcopal politics; demonic combat as constitutive of monastic self-formation; a caution for Streams 4, 9, 12",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    dict(id="srcALX020", section="4",
         work_author="Birger A. Pearson", work_title="Gnosticism and Christianity in Roman and Coptic Egypt (T&T Clark, 2004)",
         work_locus="2004", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): the diversity of Egyptian Christian textual culture (incl. Nag Hammadi) the Gnostic-refusal streams were drawn against",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    dict(id="srcALX021", section="4",
         work_author="Ewa Wipszycka", work_title="The Alexandrian Church: People and Institutions (JJP Suppl. 25, 2015); Moines et communautes monastiques en Egypte (JJP Suppl. 11, 2009)",
         work_locus="2015; 2009", source_type="S",
         attribution_status="genuine", level_of_description="corpus",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): the leading papyrological/documentary reconstruction of Egyptian church institutions; a primary corrective to the literary sources' elite bias",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    dict(id="srcALX022", section="4",
         work_author="Roger S. Bagnall", work_title="Egypt in Late Antiquity (Princeton UP, 1993)",
         work_locus="1993", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): the standard documentary reconstruction of late-antique Egyptian society, economy, literacy; grounds SS6 and SS8",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    dict(id="srcALX023", section="4",
         work_author="Peter Brown", work_title="The World of Late Antiquity (1971); The Body and Society (1988)",
         work_locus="1971; 1988", source_type="S",
         attribution_status="genuine", level_of_description="corpus",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): the social-religious world of late antiquity and the meaning of asceticism/renunciation",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    dict(id="srcALX024", section="4",
         work_author="David T. Runia", work_title="Philo in Early Christian Literature: A Survey (Van Gorcum/Fortress, 1993)",
         work_locus="1993", source_type="S",
         attribution_status="genuine", level_of_description="work",
         language="eng", script="Latn", genre_form="monograph",
         discovery_channel="field-bibliography",
         licensed_for="Secondary scholarship (Doc_02 SS4): the standard survey of Philo's Christian reception, with major attention to Clement, Origen, and Didymus (SS3.5)",
         verification_note="Independently verified for Doc_02 (author, title, year), 2026-07-17."),
    # ---- SS8 Material culture ----
    dict(id="srcALX025", section="8",
         work_author="(documentary corpus)", work_title="Oxyrhynchus and Fayum/Delta papyri (Christian content)",
         work_locus="2nd-4th c. papyri", source_type="M",
         attribution_status="anonymous", level_of_description="corpus",
         language="grc", script="Grek",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Material/documentary evidence (Doc_02 SS8): often the only direct, non-elite-authored, unmediated trace of ordinary Christian life",
         transmission_path="Fragmentary, frequently decontextualized, but direct where Christian content is identifiable.",
         verification_note="Confidence: Moderate (Doc_02 SS8 verbatim: \"fragmentary, frequently decontextualized, but direct where Christian content is identifiable\")."),
    dict(id="srcALX026", section="8",
         work_author="(archaeological corpus)", work_title="Egyptian Christian archaeology (baptisteries, church buildings, funerary evidence)",
         work_locus="3rd-5th c. sites", source_type="M",
         attribution_status="anonymous", level_of_description="corpus",
         language="und", script="Zyyy",
         discovery_channel="builder-prior-knowledge",
         licensed_for="Material evidence (Doc_02 SS8): spatial ordering of worship (where catechumens stood versus the faithful); Christian-indigenous mortuary interaction",
         transmission_path="Alexandria's own remains are fragmentary (continuous rebuilding, coastal subsidence); the usable archaeology is elsewhere in Egypt.",
         verification_note="Confidence: Limited for Alexandria specifically; Moderate for broader Egyptian Christian archaeology (Doc_02 SS8 verbatim)."),
]

WORLD_CORE = {
    "id": "alexcore001", "world_id": "alexandria-catechetical",
    "record_type": "world_core", "schema_version": 1, "register": "etic",
    "review_state": "draft", "jobs": [7, 3],
    "time_window": {"start_year": 150, "end_year": 400,
                    "note": 'c. 150-400 CE - Doc_01 SS2.1 candidate horizon; floor: latter 2nd century (Clement\'s Alexandrian activity c. 180s-202 as the earliest richly-attested formation activity; Pantaenus boundary-adjacent); close: c. 400, deliberately upstream of the 451 Chalcedon fracture (Doc_01 SS2.3), with the SS2.4 flag that a tighter marker (the first Origenist controversy c. 399-400) stays open. The Markan foundation is a later foundation-narrative, not a historical beginning (Doc_01 SS2.2).'},
    "horizon": 'Alexandria and Egypt, the broad reading per OG-3 (confirmed by Mark, 2026-07-17): "Alexandrian Christianity (Catechetical-Formation World)" - the catechetical-formation tradition is its anchor and namesake, not its boundary (Doc_01 SS1; folder label notwithstanding). Nicaea 325 internal, not a boundary (Doc_01 SS2.3a); monastic emergence held open vs the Desert cross-build boundary (Doc_01 SS2.3c, SS3.3).',
    "formation_logic": 'Doc_01 SS2.3 (verbatim): "the catechetical-formation logic (transformation through Scripture read at depth, worship, teaching, and philosophical engagement)" - persisting across 325 CE; the record is heavily weighted toward the literate Greek-speaking stratum, and evidential visibility is not ecological visibility (Doc_02 SS1, Article 17).',
    "gravities": [],
    "sources": [{"source_id": "srcALX001"}, {"source_id": "srcALX002"}],
}


def emit_record(rec: dict, body: str, path: Path):
    import yaml
    front = yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=100)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{front}---\n{body}\n", encoding="utf-8", newline="\n")


def main():
    for row in ROWS:
        row = dict(row)
        section = row.pop("section")
        rec = {**COMMON, **row, "jobs": [1, 2]}
        body = (f"Migrated at S6.2 (2026-07-27) from `{DOC02}` Section {section}. "
                f"Mapping and backfill rule: see `wrs/migrate/s62_alx_source_rows.py`. "
                f"Prose fields are verbatim (or verbatim-excerpted, marked '...') from that section.")
        rec["added"] = "2026-07-27 (S6.2 migration from Doc_02)"
        emit_record(rec, body, OUT / "source" / f"{rec['id']}.md")
    emit_record(WORLD_CORE,
                f"Migrated at S6.2 (2026-07-27) from `{DOC01}` (SS1, SS2, OG-3 resolution) and "
                f"`{DOC02}` SS1. gravities[] deliberately empty until the S2.5-equivalent "
                f"authors the gravity records; pairing_guidance/cautions arrive at the "
                f"S2.7a-equivalent.",
                OUT / "world_core" / "alexcore001.md")
    print(f"wrote {len(ROWS)} source records + 1 world_core to {OUT}")


if __name__ == "__main__":
    main()
