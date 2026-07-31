"""S6.2/HAL - S2.1-equivalent: world_core + source rows (world 4,
Hieronymian Ascetic-Literary; the Desert/ALX prose-derived pattern -
no deployed structured registry exists for this world, unlike Syriac).

Source: hal_Doc_02_Source_Ecology.md (Approved to proceed; Rounds 1-2
review complete), read in full. hal_Doc_01 (Approved) supplies the
world_core. Declared mapping:

- Rows follow Doc_02's own sections: SS1 primary voices' texts, SS2
  secondary voices' texts, SS4 scholarship, SS5-6 formation-narrative /
  material sources. The four named women (SS1.2-1.5) authored NO
  surviving text - they are figures (S2.4), not source rows; their
  mediation-through-Jerome caveats ride the Jerome rows' notes.
- Doc_02's own confidence language and REVIEW-FLAGGED caveats carried
  VERBATIM where load-bearing: the Marcella-correspondence list's
  Inferential/Thin pending-verification caveat (srcHAL001); the
  Palladius DO-NOT-CITE-until-located flag (srcHAL008, in
  licensed_for); the Cain-essay unverified Ep.24/Ep.127 pairing
  (srcHAL012); the Wilson-Kastner/Krumeich neither-read-in-full
  characterization caveat (srcHAL018/019).
- Backfill rule: no discovery_instrument/discovery_date on migrated
  rows; discovery_channel per the fleet convention (P/M ->
  builder-prior-knowledge; S -> field-bibliography).
- Vita Pauli predates the 382 boundary - carried INSIDE the vitae
  corpus row as declared formative background (Doc_02 SS1.1's own
  framing), not silently in-window.
- Egeria: Native with license restricted to pilgrimage-infrastructure
  context (her text does not describe Jerome's community - Doc_02 SS6
  verbatim); the ALX reception-license precedent.
- The SS6 documentary/material NON-finding ('no papyri, ostraca, or
  administrative records identified... a significant evidentiary gap')
  is a gap statement, not a source - recorded in the checkpoint and
  the core's horizon, never manufactured into a row.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "hieronymian_world"
WID = "hieronymian-ascetic-literary"
DOC02 = "World-Builds/Hieronymian-Ascetic-Literary/hal_Doc_02_Source_Ecology.md"
DOC01 = "World-Builds/Hieronymian-Ascetic-Literary/hal_Doc_01_World_Identification_Boundaries_Orientation.md"

COMMON = {"world_id": WID, "record_type": "source", "schema_version": 1,
          "register": "etic", "review_state": "draft",
          "disposition": "in-use", "jobs": [1, 2]}


def P(id_, title, locus, licensed, note, author="Jerome", lang="lat",
      script="Latn", level="work", attribution="genuine", genre=None,
      boundary="Native"):
    r = {**COMMON, "id": id_, "source_type": "P",
         "boundary_status": boundary, "attribution_status": attribution,
         "level_of_description": level, "language": lang, "script": script,
         "discovery_channel": "builder-prior-knowledge",
         "work_title": title, "work_locus": locus,
         "licensed_for": licensed, "verification_note": note}
    if author:
        r["work_author"] = author
    if genre:
        r["genre_form"] = genre
    return r


def S(id_, author, title, locus, licensed, note, level="work", genre=None):
    r = {**COMMON, "id": id_, "source_type": "S", "boundary_status": "Native",
         "attribution_status": "genuine", "level_of_description": level,
         "language": "eng", "script": "Latn",
         "discovery_channel": "field-bibliography",
         "work_author": author, "work_title": title, "work_locus": locus,
         "licensed_for": licensed, "verification_note": note}
    if genre:
        r["genre_form"] = genre
    return r


ROWS = [
 P("srcHAL001",
   ("The Epistulae (Letters) of Jerome - incl. Ep. 22 (384, to "
    "Eustochium, De virginitate servanda, with the 'Ciceronian, not a "
    "Christian' dream); Ep. 46 ('Paula and Eustochium to Marcella' - "
    "Widely Accepted as Jerome's own composition in the women's names, "
    "per Nautin and Cain); the Marcella correspondence; Ep. 77 (399, "
    "obituary for Fabiola); Ep. 107 (to Laeta, on the younger Paula's "
    "education); Ep. 108 (404, Epitaphium Sanctae Paulae); Ep. 127 "
    "(412, obituary for Marcella, to Principia)"),
   "382-420",
   ("The single most important source for this world's ecology (Doc_02 "
    "SS1.1). Voice, story, and confidence work - ALWAYS under the SS3 "
    "Author Gravity discounts: the obituaries are literary epitaphs in "
    "a classical rhetorical genre, not neutral biography; the letter "
    "collections were curated (in part by Jerome himself) rather than "
    "preserved neutrally; every account of the four named women "
    "reaches this world solely through Jerome's hand."),
   ("Doc_02 SS1.1 verbatim caveat, carried at full strength: the "
    "specific Marcella-correspondence list 'Epp. 23-29, 32, 34, 37, "
    "40-44 in the standard numbering' is carried at Inferential/Thin "
    "confidence, PENDING INDEPENDENT VERIFICATION against Cain's "
    "critical apparatus, 'and is not to be relied on for any specific "
    "claim until so verified.' Documented that Jerome wrote these "
    "texts and that they say what they say; Contested-to-"
    "Inferential/Thin for many specific biographical and chronological "
    "details they report."),
   level="corpus", genre="letter"),
 P("srcHAL002",
   ("The Vulgate - Gospels revised against the Greek c. 382-384 "
    "(Rome); Old Testament translated substantially from Hebrew c. "
    "390-405 (Bethlehem), under the Hebraica veritas principle"),
   "382-405",
   ("The world's defining textual project (hal_lex01/hal_lex02's "
    "ground). Confidence per Doc_02: the project's outline Documented; "
    "Jerome's own account of his Hebrew fluency Contested (Williams - "
    "retrospectively embellished self-presentation)."),
   ("Doc_02 SS1.1; Doc_01 SS3.1 carries the Hebrew-fluency contest at "
    "Contested, unresolved."),
   level="corpus"),
 P("srcHAL003",
   ("Jerome's biblical commentaries produced at Bethlehem (Ephesians, "
    "Galatians, Titus, Matthew [398], Isaiah [18 books], and others), "
    "consistently dedicated to and framed as responses to requests "
    "from Paula, Eustochium, or Marcella"),
   "386-420",
   ("Documented (Doc_02 SS1.1) - and the dedications are themselves "
    "primary evidence of the women's commissioning role in the "
    "world's textual-asceticism ecology."),
   "Doc_02 SS1.1: the dedication pattern is Documented.",
   level="corpus", genre="commentary"),
 P("srcHAL004",
   ("Jerome's hagiographic/ascetic-literary vitae: Vita Pauli (c. "
    "374-375, Antioch period - PREDATES this world's 382 boundary, "
    "included as formative background to the genre Jerome brings to "
    "Bethlehem, not as a within-world source, per Doc_02's own "
    "framing); Vita Malchi (c. 391); Vita Hilarionis (c. 390)"),
   "c. 374-391",
   ("Formation-narrative sources (Doc_02 SS5): models of ascetic "
    "heroism informing the community's self-understanding - "
    "hagiographic romance with acknowledged legendary elements, "
    "historical reliability of specific events Inferential/Thin "
    "(Tier 3/4 per the Story Tier framework)."),
   ("Doc_02 SS1.1 + SS5: Author Gravity risk HIGH - consciously "
    "literary productions giving Latin Christianity its own "
    "desert-hagiographic genre."),
   level="corpus", genre="hagiography"),
 P("srcHAL005",
   "Apologia adversus Rufinum (addressed to Pammachius and Marcella)",
   "401-403",
   ("Documented primary evidence for the Origenist controversy's "
    "effect on the community - AS POLEMIC: requires Author Gravity "
    "discounting for every characterization of Rufinus and Bishop "
    "John of Jerusalem (Doc_02 SS1.1 verbatim)."),
   "Doc_02 SS1.1.", genre="polemic"),
 P("srcHAL006",
   "De Viris Illustribus - Jerome's catalogue of Christian writers",
   "392",
   ("Jerome's self-presentation and corroboration of some biographical "
    "details - e.g. the Didymus connection, which is NOT attested in "
    "Ep. 108 itself (Doc_02 SS1.1/SS2.4: the in-person 385-386 "
    "Alexandria meeting is Contested/Inferential-Thin)."),
   "Doc_02 SS1.1, SS2.4."),
 P("srcHAL007",
   "Apologia contra Hieronymum",
   "401",
   ("The only substantial surviving account of this world's central "
    "internal fracture written by someone other than Jerome - "
    "evidentially valuable precisely for that, equally polemical in "
    "the opposite direction, same Author Gravity discounting (Doc_02 "
    "SS2.1 verbatim; the '401' date is Doc_02's own Round-correction "
    "from an earlier '400')."),
   ("Doc_02 SS2.1: Documented that the controversy and exchange "
    "occurred; Contested whose characterization is more accurate."),
   author="Rufinus of Aquileia", genre="polemic"),
 P("srcHAL008",
   "Lausiac History (the Paula-circle material)",
   "c. 419-420",
   ("Doc_02 SS2.2's flag carried VERBATIM as this row's license: 'do "
    "not cite a specific claim from Palladius until the passage is "
    "located and confirmed' - the reported more-critical outside "
    "perspective on Paula's circle (Paula 'in some sense hindered or "
    "overshadowed by Jerome's direction') could not be pinned to an "
    "exact chapter/section in the build's research pass. Context-"
    "level use only until then."),
   ("Doc_02 SS2.2 + SS3.4: the one substantial near-contemporary "
    "non-Jerome account; transmission history complex (multiple "
    "recensions), unverified detail flagged."),
   author="Palladius of Galatia", lang="grc", script="Grek",
   genre="hagiography"),
 P("srcHAL009",
   ("The Jerome-Augustine correspondence (Jerome's Ep. 112 = "
    "Augustine's Ep. 75, and related letters) - the Hebrew-versus-"
    "Septuagint dispute, incl. the Oea 'ivy/gourd' congregational "
    "incident"),
   "c. 394-405",
   ("Documented (Doc_02 SS2.3); the external contemporary test of the "
    "world's defining textual-authority commitment. Augustine's own "
    "build (World #8) is NOT read or drawn on beyond what this "
    "correspondence itself establishes - Doc_02's own cross-build "
    "boundary, carried as this row's license restriction."),
   "Doc_02 SS2.3.", author="Jerome / Augustine of Hippo",
   level="corpus", genre="letter"),
 S("srcHAL010", "Andrew Cain", "The Letters of Jerome (OUP, 2009)", "2009",
   ("The critical-edition backbone for confidence calibration on "
    "letter authenticity and dating (Doc_02 SS4) - treats the letters "
    "as self-conscious rhetorical constructions of Jerome's own "
    "authority. Confidence-judgment apparatus only, never voice "
    "content."),
   "Doc_02 SS4; 'Claiming Marcella' = its ch. 3 (Round-1 verified).",
   genre="monograph"),
 S("srcHAL011", "Andrew Cain", "Jerome's Epitaph on Paula (OUP, 2013)", "2013",
   ("The Ep. 108 critical apparatus (Doc_02 SS4) - confidence work on "
    "the Paula material."),
   "Doc_02 SS4.", genre="monograph"),
 S("srcHAL012", "Andrew Cain",
   ("\"Rethinking Jerome's Portraits of Holy Women,\" in Jerome of "
    "Stridon: His Life, Writings and Legacy (eds. Cain & Lossl, "
    "Ashgate, 2009)"),
   "2009",
   ("The analysis most directly applicable to Ep. 127 (the Marcella "
    "obituary as propagandistic hagiographic portrait) - Doc_02 "
    "SS1.4's cited ground for the self-vindication reading."),
   ("Doc_02 SS1.4's own review flag carried VERBATIM: the specific "
    "claim that the essay treats Ep. 127 ALONGSIDE Ep. 24 (Asella) "
    "'was introduced during citation correction and has not itself "
    "been independently verified against the essay's full text; "
    "flagged for confirmation before being relied upon for any "
    "specific downstream claim.'")),
 S("srcHAL013", "Megan Hale Williams",
   "The Monk and the Book (Chicago, 2006)", "2006",
   ("The key source for the Contested status of Jerome's "
    "Hebrew-fluency claims (Doc_02 SS4) - strongly Jerome-centric by "
    "design; the women's patronage as infrastructure for Jerome's "
    "self-fashioning."),
   "Doc_02 SS4.", genre="monograph"),
 S("srcHAL014", "J.N.D. Kelly",
   "Jerome: His Life, Writings, and Controversies (1975)", "1975",
   ("The classic biographical synthesis (Doc_02 SS4) - explicitly "
    "Jerome-centric, predating the discourse-critical/feminist "
    "historiographical turn; used with that dating in view."),
   "Doc_02 SS4; the c. 331 birth-year position (vs Rebenich's c. 347).",
   genre="monograph"),
 S("srcHAL015", "Stefan Rebenich",
   "Jerome (Routledge, 2002); Hieronymus und sein Kreis (1992)", "1992-2002",
   ("The key source for the patronage-authority-mode analysis (Doc_01 "
    "SS3.3, SS8.1; Doc_02 SS4): Jerome positioning himself as "
    "spiritual leader of wealthy Christian intellectuals who could "
    "fund him."),
   "Doc_02 SS4; the c. 347 birth-year position.", level="corpus"),
 S("srcHAL016", "Elizabeth A. Clark",
   ("The Origenist Controversy (Princeton, 1992); \"The Lady "
    "Vanishes\" (Church History, 1998)"),
   "1992-1998",
   ("The pivotal methodological voice for the whole approach to the "
    "women (Doc_02 SS4): elite women recoverable only through "
    "male-authored texts' 'social logic' - the co-constitution "
    "constraint the build's Preamble-level honesty is directly "
    "indebted to, named explicitly."),
   "Doc_02 SS4.", level="corpus"),
 S("srcHAL017", "Kate Cooper",
   "The Virgin and the Bride (Harvard, 1996/1999)", "1996-1999",
   ("A serious methodological CHALLENGE carried as such (Doc_02 SS4): "
    "idealized women as rhetorical instruments in male "
    "status-competition - the 'women-as-terrain' reading this world's "
    "construction must answer, not ignore."),
   "Doc_02 SS4.", genre="monograph"),
 S("srcHAL018", "Patricia Wilson-Kastner et al.",
   "A Lost Tradition: Women Writers of the Early Church (1981)", "1981",
   ("Recovery-oriented scholarship centering the women's agency "
    "(Doc_02 SS4) - used only with its own caveat attached."),
   ("Doc_02 SS4's caveat VERBATIM: the characterization given 'is "
    "carried at Inferential/Thin confidence... neither was "
    "independently read in full' by the build's research pass.")),
 S("srcHAL019", "Christa Krumeich",
   "Hieronymus und die christlichen feminae clarissimae (1993)", "1993",
   ("Recovery-oriented scholarship (Doc_02 SS4) - same restricted "
    "use as srcHAL018."),
   ("Same Doc_02 SS4 caveat as srcHAL018: characterization at "
    "Inferential/Thin, not independently read in full.")),
 S("srcHAL020", "Barbara Feichtinger",
   "Apostolae Apostolorum (1995)", "1995",
   ("The interpretive posture Doc_05 ADOPTS (Doc_02 SS4): female "
    "asceticism under Jerome's direction as genuinely dialectical - "
    "both liberation and coercion - found more defensible than either "
    "a purely celebratory or purely instrumentalizing reading."),
   "Doc_02 SS4.", genre="monograph"),
 P("srcHAL021",
   ("Bethlehem/Nativity-site archaeology (the broader site record; "
    "later Byzantine and Crusader building phases complicate it)"),
   "4th-5th c. site record",
   ("Doc_02 SS6 verbatim: NO specific archaeological remains "
    "attributable to Jerome's monastery, Paula's convent, or the "
    "hospice have been independently verified as distinct excavated "
    "structures - any specific spatial claim is Inferential/Thin "
    "until verified; SOME 4th/5th-c. monastic building activity near "
    "the Nativity site is Widely Accepted from the broader record."),
   "Doc_02 SS6.", author=None, lang="zxx", script="Zxxx",
   level="aggregate-attestation"),
 P("srcHAL022",
   "Egeria, Itinerarium (the Holy Land pilgrimage-infrastructure account)",
   "c. 381-384",
   ("Context ONLY, per Doc_02 SS6 verbatim: near-contemporary evidence "
    "of the wider pilgrimage infrastructure - 'though Egeria's own "
    "text does not specifically describe Jerome's community.' Never "
    "cited as evidence about this world's own institutions."),
   "Doc_02 SS6.", author="Egeria", genre="letter"),
]

CORE = {
    "world_id": WID, "record_type": "world_core", "schema_version": 1,
    "jobs": [1, 5], "register": "etic", "review_state": "draft",
    "id": "halcore001",
    "time_window": {
        "start_year": 382, "end_year": 420,
        "note": ("382 = Jerome's arrival in Rome converging with "
                 "Marcella's already-established Aventine household "
                 "(Doc_01 SS1.1 - a deliberate choice against 385 and "
                 "against the 340s, both rejected with reasons); 420 = "
                 "the INSTITUTIONAL-CONTINUITY terminus, explicitly not "
                 "a Jerome-biography privileging: Eustochium's death "
                 "(418/419/420, Contested across a three-year window) "
                 "and Jerome's (420, year Widely Accepted, exact day "
                 "Inferential/Thin) cluster within one-two years; the "
                 "world closes when BOTH resident-leadership threads "
                 "have ended, and no clean order or interval between "
                 "the two deaths may be asserted (Doc_01 SS1.2, "
                 "carried forward as instructed)."),
    },
    "horizon": (
        "A generational close: every voice constituting the "
        "Jerome-and-the-women relationship is gone within a few years "
        "of one another - Paula 404, Marcella 410 (in the Gothic sack "
        "of Rome, removing the Rome pole a decade early: the final "
        "decade is Bethlehem-concentrated in a way the earlier decades "
        "were not, an asymmetry to keep visible, Doc_01 SS1.3), "
        "Eustochium 418-420, Jerome 420. Internal to the window, not "
        "boundary events: the 385 Rome rupture and Bethlehem "
        "relocation; the Origenist controversy and the Rufinus rupture "
        "(c. 393-403); Paula's death and Eustochium's succession "
        "(404); the 416 Pelagian attack on the monastery. Geography "
        "BIPOLAR by structural finding, not narrative convenience: "
        "Bethlehem (the double monastery + hospice) AND Rome (the "
        "Aventine circle) as continuously active poles (Doc_01 SS2). "
        "Standing evidentiary gaps carried from Doc_02: no papyri, "
        "ostraca, or administrative records specific to the community "
        "identified (SS6, 'a significant evidentiary gap'); the "
        "women's own unmediated voice structurally absent, every "
        "account through Jerome's hand alone (SS7.3, the Article-20 "
        "affirmative duty verbatim-in-substance)."),
    "formation_logic": (
        'Doc_01 SS5.1 verbatim: this world\'s recurring formation '
        'ecology is organized around "textual asceticism: the fusion '
        'of ascetic renunciation (fasting, celibacy/continence, wealth '
        'divestment, manual and scriptorium labor) with '
        'scholarly-literary production (biblical translation, '
        'commentary, epistolary spiritual direction, hagiographic '
        'literature) as a single, mutually reinforcing formation '
        'practice - not as two separate activities occurring in the '
        'same community... the ecology does not treat scholarship as a '
        'distraction from asceticism or asceticism as a precondition '
        'merely tolerated around scholarship."'),
    "gravities": [],
    "sources": [{"source_id": "srcHAL001"}, {"source_id": "srcHAL002"}],
}


def main():
    (OUT / "source").mkdir(parents=True, exist_ok=True)
    (OUT / "world_core").mkdir(parents=True, exist_ok=True)
    for rec in ROWS:
        emit_record(rec, (
            f"Migrated at S6.2/HAL S2.1-equivalent (2026-07-31) from "
            f"`{DOC02}` (prose-derived, the Desert/ALX pattern - no "
            f"deployed structured registry exists for this world; "
            f"mapping declared in `wrs/migrate/s62_hal_s21.py`). "
            f"Doc_02's own confidence language and review-flagged "
            f"caveats carried verbatim where load-bearing."),
            OUT / "source" / f"{rec['id']}.md")
    emit_record(CORE, (
        f"Migrated at S6.2/HAL S2.1-equivalent (2026-07-31) from "
        f"`{DOC01}` (SS1 temporal boundaries incl. the "
        f"institutional-continuity terminus reasoning; SS2 bipolar "
        f"geography; SS5.1 formation logic verbatim). gravities[] "
        f"deliberately empty until the S2.5-equivalent; "
        f"pairing_guidance/cautions/telos/living_traditions arrive at "
        f"the S2.7a-equivalent per the standing conventions."),
        OUT / "world_core" / "halcore001.md")
    print(f"emitted {len(ROWS)} source rows + halcore001")


if __name__ == "__main__":
    main()
