"""S2.6 - Desert contested_claim records (blueprint S2.6; Pass 1 SS3.7, job 8).

One record per Primary gravity (the SS11 minimum): Doc_04 SS6's Primary set
is 1 (withdrawal), 2 (spiritual combat), 3 (elder authority), 4 (manual
labor), 5 (diakrisis), 7 (practical scriptural engagement).

Field discipline:
- claim: what the world actually holds, in the world's own terms - drawn
  from the lexicon chunks' World Meaning / World Hearing text and Doc_04's
  own gravity language, not invented.
- held_against[]: ONLY challenges actually contested in the record, by a
  named challenger, with sources. Where a gravity has no preserved
  contested exchange, the entry names the documented counter-evidence the
  record itself carries (e.g. withdrawal's rhetoric vs. the papyrological/
  archaeological embeddedness record) rather than inventing a dialogue.
  Build-inferred tensions that are NOT exchanges in sources (e.g. Doc_04
  SS2's labor-vs-contemplative-reading cell) are deliberately excluded.
- concedes: the world's genuine unsettledness, as data - each drawn from a
  documented open item (Doc_04 SS8, Doc_08's no-adjudication finding, the
  chunks' own plural-voices flags and compiler-mediation caveats).
- pressure_response: how the world characteristically responds when pushed,
  grounded in the record's own documented patterns (terse saying, enacted
  answer, redirection toward moderation, person-measured counsel) - plain
  register, no invented aphorisms (S2.3 review lesson).
- divergence_partners[]: mapped against the five unmigrated worlds' OWN
  Doc_04 documents (read for this step): PAHC CiC_W1_Doc04 FINAL (Primary
  G02 correspondence network, G07 eucharistic variation; G01 authority
  consolidation Supporting/Contested; G06 household NOT a gravity),
  Alexandria Doc_04 SS4 (Primary C1 scripture-as-formative / C2 soul-
  transformation; T1 teacher-bishop; T4 martyrdom-vs-contemplative; askesis
  "not confirmed on urban evidence... developed form desert-attributed"),
  HAL hal_Doc_04 SS3 (Primary G1 hebraica veritas, G2 ascetic self-
  impoverishment, G3 patronage-as-authority; G4 letter-writing Supporting),
  Imperial-Juridical Doc_04 SS4 (Primary 1 juridical primacy, 2 church-
  state alliance, 3 orthodoxy-enforcement; Tensional 6 sacramental/moral
  vs institutional/positional authority), Syriac Doc_04 SS4 (Primary C1
  typological method, C2 covenanted ascetic life; Supporting C5
  Diatessaron; Tensional C4 authority-structure ambiguity).
  partner_claim_id is left unset everywhere - that is S6.3's enrichment,
  once partners carry their own contested_claim records (F1 withdrawn:
  mapping against the partners' live documents IS SS11-A's requirement).

No partner-world file is written (Touches: contested_claim/ only).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record

OUT = BACKEND / "wrs" / "records" / "desert_world"

COMMON = {"world_id": "desert-monasticism", "record_type": "contested_claim",
          "schema_version": 1, "jobs": [8], "register": "emic",
          "review_state": "draft"}

CLAIMS = [
 dict(
  id="desertclaim001",
  name="Withdrawal is itself the formation",
  sources=[{"source_id": "srcDES001"}, {"source_id": "srcDES009"},
           {"source_id": "srcDES010"}, {"source_id": "srcDES015"}],
  claim=("Withdrawal from settled life is not escape but the most demanding "
         "form of engagement - the departure is itself the formation, a "
         "direct, sustained confrontation with interior reality that "
         "ordinary settled life allowed a person to avoid, taking the place "
         "of the total self-offering martyrdom had previously supplied. "
         "Distance, solitude, and exposure to interior struggle are the "
         "curriculum, not preparation for it."),
  held_against=[
   {"challenge": ("The world's own documentary and archaeological record "
                  "stands against the rhetoric of total separation: "
                  "Kellia's commercial infrastructure and the Nepheros "
                  "correspondence document ongoing economic and social "
                  "entanglement with village life throughout the world's "
                  "span. The world kept its withdrawal claim without "
                  "conceding it - the tension is documented as standing, "
                  "never resolved in the world's own voice (Doc_04 "
                  "candidate 8, Tensional; Doc_08 2A-i)."),
    "challenger": ("the world's own papyrological and archaeological "
                   "record, read against its literary self-presentation"),
    "sources": [{"source_id": "srcDES009"}, {"source_id": "srcDES010"},
                {"source_id": "srcDES015"}]},
  ],
  concedes=("How the rhetoric of total separation squared with the "
            "practiced reality of village-linked economy, our own preserved "
            "voice does not say - the world did not thematize this tension "
            "in its own surviving teaching (Doc_08 2A-i); and whether the "
            "embeddedness pattern was world-wide or concentrated in Lower "
            "Egypt remains at Contested/Inferential confidence in the "
            "record (Doc_04 SS3, candidate 8)."),
  pressure_response=("Answers with the practice, not a defense: the "
                     "record's documented answers about withdrawal come as "
                     "terse sayings measured to the asker - flee, be "
                     "silent, be still, given to one man's situation - "
                     "not as a general case argued for settled life's "
                     "critics."),
  divergence_partners=[
   {"world_id": "alexandria-catechetical",
    "note": ("Their Doc_04 locates formation in the urban school - C1's "
             "reading/school/lectionary practice-cluster and C2's "
             "soul-transformation are city practices; their own index "
             "table holds askesis 'not confirmed on urban evidence,' its "
             "developed form desert-attributed. Formation without "
             "departure vs. departure as formation - a genuine "
             "divergence, documented on both sides.")},
   {"world_id": "syriac-edessa-nisibis",
    "note": ("Their Doc_04 Primary C2 is the covenanted ascetic life - "
             "asceticism lived within the town congregation as a "
             "covenant-standing, not a geographic departure. Their "
             "ascetics stay; this world's leave.")},
   {"world_id": "hieronymian-ascetic-literary",
    "note": ("Their Doc_04 Primary G2 (ascetic self-impoverishment) "
             "operates inside G3's patronage-as-authority networks and "
             "G4's letter-writing medium - renunciation conducted within "
             "elite literary society, not by leaving settled life for "
             "marginal land.")},
   {"world_id": "post-apostolic-house-church",
    "note": ("Their Doc_04 tested the household (G06) and found ordinary "
             "household assembly the world's basic unit - formation "
             "located inside ordinary social structures; no withdrawal "
             "dimension exists in their gravity set.")},
   {"world_id": "imperial-juridical-christianity",
    "note": ("Their Doc_04 Primary 2 is the church-state alliance and its "
             "limits - a formation ecology built on civic and imperial "
             "engagement, the direct opposite direction of travel from "
             "withdrawal.")},
  ]),

 dict(
  id="desertclaim002",
  name="The thoughts are the battlefield",
  sources=[{"source_id": "srcDES001"}, {"source_id": "srcDES004"},
           {"source_id": "srcDES005"}],
  claim=("The unwanted, intrusive thought is the primary site of spiritual "
         "combat. The thoughts are morally and spiritually significant "
         "regardless of ultimate metaphysical status, requiring active "
         "discernment and disclosure to an elder - a relational practice, "
         "not merely a private one."),
  held_against=[
   {"challenge": ("The assault itself, as the tradition's own paradigm "
                  "portrait stages it: the enclosure in the tombs (Vita "
                  "Antonii chs. 8-10), the combat endured and not "
                  "conceded. The record's Tier-3 handling marks this as "
                  "the tradition's portrait of the combat - hagiographic "
                  "genre, not incident report - but the portrait is "
                  "itself the world's own statement that the battle is "
                  "real and can be met."),
    "challenger": ("the demonic assault, as the world's own portrait "
                   "stages the contest"),
    "sources": [{"source_id": "srcDES001"}]},
  ],
  concedes=("A single settled taxonomy of the thoughts was never this "
            "world's common property: the eight-fold scheme is one "
            "teacher's systematization, concentrated among the more "
            "intellectually systematic ascetics and not attested with "
            "comparable precision elsewhere (the record's own "
            "plural-voices flag). How the thoughts' ultimate metaphysical "
            "status was understood across all three strands, our own "
            "record does not tell us with one voice."),
  pressure_response=("Meets the pushed question with practice, not theory: "
                     "the thought is to be named aloud to an elder, and "
                     "the counsel measured to the person. Where a "
                     "systematic account is demanded, the world's general "
                     "voice steps back to the terse saying; the "
                     "systematic register belongs to one teacher's "
                     "strand, not the world's common speech."),
  divergence_partners=[
   {"world_id": "alexandria-catechetical",
    "note": ("Their Doc_04 Primary C2 frames interior life as "
             "transformation of the soul toward God under divine "
             "pedagogy (Supporting C3) - an educational ascent, not a "
             "battlefield; their T4 tension (martyrdom vs. contemplative "
             "ascent) contests the interior life on a different axis "
             "entirely.")},
   {"world_id": "post-apostolic-house-church",
    "note": ("Their Doc_04 G04 (martyrdom as meaning-response, "
             "Supporting) locates the contested interior site in witness "
             "under state pressure (G03) - the struggle is against the "
             "external threat and its meaning, not the intrusive "
             "thought.")},
   {"world_id": "syriac-edessa-nisibis",
    "note": ("Their Doc_04 Supporting C6 is endurance under persecution "
             "- combat externalized as endurance in the body and the "
             "community; no thought-taxonomy dimension appears in their "
             "gravity set.")},
  ]),

 dict(
  id="desertclaim003",
  name="Authority is earned discernment, not office",
  sources=[{"source_id": "srcDES002"}, {"source_id": "srcDES005"},
           {"source_id": "srcDES006"}],
  claim=("Among this world's more solitary and semi-communal ascetics - "
         "the strands whose voice the sayings tradition chiefly preserves "
         "- spiritual authority (abba, amma, geron) is earned through "
         "recognized discernment and transmitted through direct personal "
         "relationship, not conferred by formal ecclesiastical office. A "
         "disciple's disclosure of interior thoughts to an elder is itself "
         "spiritually necessary, and the elder's counsel is authoritative "
         "guidance, not one input among many. The communal-rule strand "
         "constitutes authority differently - that contest is this "
         "record's own subject."),
  held_against=[
   {"challenge": ("Visiting elder monks came to Amma Sarah intending to "
                  "test or humble her as a woman - a direct challenge to "
                  "who may bear this authority, met and not conceded: her "
                  "answer held the ground, and the tradition preserved "
                  "the exchange with her authority intact."),
    "challenger": "visiting elder monks, in the Apophthegmata's own record",
    "sources": [{"source_id": "srcDES006"}]},
   {"challenge": ("The office-based model inside this same world: the "
                  "Pachomian Rule constituted authority through formal "
                  "offices, making the elder model structurally secondary "
                  "in that strand. The person-based model persisted "
                  "alongside it, unresolved, across the world's whole "
                  "span (Doc_04 candidate 10; desertgrav010) - held, not "
                  "conceded, and never adjudicated."),
    "challenger": ("the communal-rule strand's formal office structure, "
                   "in the Pachomian corpus"),
    "sources": [{"source_id": "srcDES002"}]},
  ],
  concedes=("By what procedure discernment was recognized in an elder, our "
            "own record does not tell us - recognition operated without "
            "documented mechanism. And no internal means of adjudicating "
            "between the person-based and office-based models ever "
            "developed within the world's own span (Doc_08 2B-i/3B-i): "
            "which model constitutes legitimate authority, the world "
            "never settled. The ammas' surviving material is thin "
            "relative to the male-centered bulk of the record."),
  pressure_response=("Enacts rather than argues: pressed to join the "
                     "council judging a brother, Moses answers the summons "
                     "with an enacted image of his own sins and one "
                     "sentence. The characteristic move under challenge is "
                     "deflection toward one's own faults, not defense of "
                     "one's standing."),
  divergence_partners=[
   {"world_id": "imperial-juridical-christianity",
    "note": ("Their Doc_04 Primary 1 grounds authority in juridical "
             "primacy-claiming - office, see-rank, and law; their own "
             "Tensional 6 (sacramental/moral vs. institutional/"
             "positional authority) fights this same axis from the "
             "institutional side. Direct, documented divergence.")},
   {"world_id": "post-apostolic-house-church",
    "note": ("Their Doc_04 G01 (authority consolidation - the emerging "
             "episkopos/presbyteros structure) is Supporting on their "
             "own Contested-confidence finding, but its direction is "
             "office-consolidation - the trajectory this world's elder "
             "model stands apart from.")},
   {"world_id": "alexandria-catechetical",
    "note": ("Their Doc_04 T1 (teacher-bishop tension) contests "
             "person-vs-office inside their own world - but their "
             "teacher's authority is scholastic and institutional (the "
             "school), not the desert's relationally-transmitted "
             "discernment; kin question, genuinely different answer.")},
   {"world_id": "hieronymian-ascetic-literary",
    "note": ("Their Doc_04 Primary G3 makes patronage the authority "
             "structure - standing constituted through elite patronage "
             "and reputation networks, a third basis distinct from both "
             "office and recognized discernment.")},
  ]),

 dict(
  id="desertclaim004",
  name="Manual labor is ascetic discipline in itself",
  sources=[{"source_id": "srcDES005"}, {"source_id": "srcDES009"},
           {"source_id": "srcDES010"}],
  claim=("Manual labor - chiefly rope and basket work - is ascetic "
         "discipline in its own right, not incidental subsistence: it "
         "occupies the hands and structures the day precisely so the mind "
         "remains available for prayer and combat with the thoughts, "
         "sustains the ascetic materially, and funds almsgiving beyond "
         "the settlement."),
  held_against=[
   {"challenge": ("Withdrawal's own rhetoric of total separation stands "
                  "against labor's practice: selling handiwork bound "
                  "ascetics into ongoing village economy, documented "
                  "directly in the Nepheros correspondence and Kellia's "
                  "excavated commercial infrastructure. The world held "
                  "labor as discipline anyway - the record's own "
                  "documented tension (the cheironaxia record's "
                  "ecological function names it), met by practice rather "
                  "than resolved in principle."),
    "challenger": ("withdrawal's rhetoric of total separation, in the "
                   "world's literary self-presentation"),
    "sources": [{"source_id": "srcDES009"}, {"source_id": "srcDES010"}]},
  ],
  concedes=("Whether the documented economic life is this world's "
            "mainstream practice or a Melitian community's - the Nepheros "
            "archive is Melitian, and the working assumption that "
            "Melitian and Nicene-communion ascetic practice were "
            "organizationally indistinguishable in day-to-day respects "
            "remains unverified (the record's own stated limitation). Our "
            "own record does not settle it."),
  pressure_response=("Responds by describing the practice, not by "
                     "theorizing it: the day structured around handwork "
                     "and prayer together is offered as the answer. The "
                     "world does not defend labor with argument; it "
                     "points at the work."),
  divergence_partners=[
   {"world_id": "hieronymian-ascetic-literary",
    "note": ("Their Doc_04 makes the formative work literary - G1's "
             "translation project and G4's letter-writing medium - and "
             "sustains it through G3's patronage, not handwork. What "
             "counts as the work that forms is genuinely divergent.")},
   {"world_id": "alexandria-catechetical",
    "note": ("Their Doc_04 C1 practice-cluster makes reading and study "
             "the formative labor - the school's work, not the hands'. "
             "No manual-labor dimension appears in their gravity set.")},
   {"world_id": "post-apostolic-house-church",
    "note": ("In their Doc_04 the household's ordinary work is simply "
             "ordinary life - G06 (household) was tested and does not "
             "reach gravity status, and no ascetic-discipline reading of "
             "labor appears; labor as formation is this world's claim, "
             "not theirs.")},
  ]),

 dict(
  id="desertclaim005",
  name="Diakrisis is the master virtue",
  sources=[{"source_id": "srcDES005"}, {"source_id": "srcDES021"}],
  claim=("Right judgment between competing courses, spirits, and thoughts "
         "- diakrisis - is the master virtue governing every other "
         "discipline: how much withdrawal, how much combat, how much "
         "labor, which authority to submit to. It is a skill developed "
         "relationally under an elder and oriented against self-deception, "
         "because one's own judgment is exactly what ascetic excess and "
         "vainglory can distort."),
  held_against=[
   {"challenge": ("The disciple's zeal for extremity - the record's "
                  "recurring exchange: a disciple requests an extreme "
                  "practice and the elder redirects toward something more "
                  "moderate, insisting intensity be discerned rather than "
                  "imitated wholesale. Met repeatedly across named "
                  "elders; the moderating claim never conceded to the "
                  "zeal it governs."),
    "challenger": ("the ascetic's own zeal for extreme practice, in the "
                   "Apophthegmata's recurring elder-disciple exchanges"),
    "sources": [{"source_id": "srcDES005"}]},
   {"challenge": ("A council at Scetis, pressing Moses to come and judge "
                  "a brother's fault - the demand that discernment become "
                  "adjudication. Met by enacted refusal: he came when "
                  "pressed, carrying the image of his own sins, and the "
                  "council's demand yielded to his answer."),
    "challenger": "the council at Scetis, in the Apophthegmata's record",
    "sources": [{"source_id": "srcDES005"}, {"source_id": "srcDES021"}]},
  ],
  concedes=("By what test a claimed discernment could be shown false, our "
            "own record does not say in general terms - the record "
            "answers person-by-person, occasion-by-occasion, and the "
            "compilers' later arrangement stands between us and any "
            "exchange's original context (the record's own "
            "compiler-mediation caveat, Contested)."),
  pressure_response=("Redirects rather than rules: the characteristic "
                     "answer to how-much is measured to the asker, not "
                     "stated as a law. Pressed for a verdict on another "
                     "person, the world's exemplar answers with his own "
                     "faults instead."),
  divergence_partners=[
   {"world_id": "imperial-juridical-christianity",
    "note": ("Their Doc_04 institutionalizes right judgment - Primary 1 "
             "and 3 decide by council, canon, and imperial enforcement, "
             "with Supporting 5's doctrinal precision-seeking as the "
             "instrument. Adjudication by formal mechanism vs. "
             "person-measured discernment - direct divergence.")},
   {"world_id": "alexandria-catechetical",
    "note": ("Their Doc_04 Supporting C3 (divine pedagogy) forms "
             "judgment through ordered instruction - the school's "
             "curriculum as the shaping mechanism, not the elder's "
             "occasion-measured counsel.")},
   {"world_id": "syriac-edessa-nisibis",
    "note": ("Their Doc_04 Supporting C3 is heresiological "
             "self-definition - right and wrong discerned by "
             "boundary-drawing against rival movements, a communal and "
             "polemical mechanism rather than a person-formed virtue.")},
  ]),

 dict(
  id="desertclaim006",
  name="Scripture is engaged practically, not systematically",
  sources=[{"source_id": "srcDES001"}, {"source_id": "srcDES004"},
           {"source_id": "srcDES005"}],
  claim=("Scripture is engaged practically and occasionally - deployed "
         "within sayings, measured to a specific disciple's situation - "
         "not expounded systematically. Hearing a text is expected to "
         "issue in doing it; teaching that could not be reduced to a "
         "portable saying largely does not survive in the world's own "
         "idiom."),
  held_against=[
   {"challenge": ("The systematic mode was present and available inside "
                  "the world's own record: one notably systematic teacher "
                  "wrote sustained treatises, and his strand carried a "
                  "fully systematized alternative. The world's broad "
                  "practice held its occasional, applied idiom anyway - "
                  "the saying, not the treatise, remained the common "
                  "vehicle; the systematic register stayed one "
                  "sub-population's achievement."),
    "challenger": ("the systematic-treatise mode, present in the world's "
                   "own record through its one notably systematic "
                   "teacher"),
    "sources": [{"source_id": "srcDES004"}, {"source_id": "srcDES005"}]},
  ],
  concedes=("How scripture functioned in the communal-rule strand "
            "specifically, our record documents more thinly than for the "
            "other strands; part of this claim's basis is an absence - "
            "the lack of a surviving systematic exegetical corpus - not "
            "positive attestation alone (Doc_04's own softest-Primary "
            "flag on this gravity); and the compilers' arrangement stands "
            "between any individual saying and its original occasion."),
  pressure_response=("Answers a question about scripture with a text "
                     "applied to the occasion - the verse handed back as "
                     "something to do. Pressed for exposition, the "
                     "world's voice returns to the concrete case in front "
                     "of it."),
  divergence_partners=[
   {"world_id": "alexandria-catechetical",
    "note": ("Their Doc_04 Primary C1 makes scripture a deep formative "
             "reality engaged through the systematic reading/school/"
             "lectionary cluster - the documented contrast Desert Doc_04 "
             "itself cites in generating this gravity (Doc_01 SS4's "
             "World #2 comparison). The strongest divergence pairing in "
             "the set.")},
   {"world_id": "hieronymian-ascetic-literary",
    "note": ("Their Doc_04 Primary G1 (hebraica veritas) engages "
             "scripture philologically - translation from the Hebrew as "
             "the governing principle, a scholarly-critical mode with no "
             "parallel in this world's occasional, applied idiom.")},
   {"world_id": "syriac-edessa-nisibis",
    "note": ("Their Doc_04 Primary C1 is the symbolic/typological "
             "method, with the Diatessaron as normative gospel "
             "(Supporting C5) - scripture engaged through type, symbol, "
             "and harmony, systematic in its own distinct register.")},
  ]),
]


def main() -> None:
    outdir = OUT / "contested_claim"
    outdir.mkdir(parents=True, exist_ok=True)
    for c in CLAIMS:
        rec = dict(COMMON)
        rec.update(c)
        # SS3.7 defines no name field for this type - the claim is the
        # identity; the short label lives in the body line only.
        label = rec.pop("name")
        body = (f"{label}. S2.6 contested_claim record (2026-07-27). Claim text from "
                "the world's own record (lexicon chunks' World Meaning/World "
                "Hearing; Doc_04 SS6); held_against traced to documented "
                "contests only; divergence_partners mapped against the five "
                "partner worlds' own Doc_04 documents (SS11-A's live-worlds "
                "requirement, F1 withdrawn); partner_claim_id deferred to "
                "S6.3.")
        emit_record(rec, body, outdir / f"{c['id']}.md")
    print(f"wrote {len(CLAIMS)} contested_claim records -> {outdir}")


if __name__ == "__main__":
    main()
