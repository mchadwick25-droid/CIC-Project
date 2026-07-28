"""S6.2/Syriac - S2.6-equivalent: contested_claim records.

5 records: the Standard's Primary-gravity minimum (C1 -> syrclaim001,
C2 -> syrclaim002) + the three routed contests from the S2.2 parkings
and the sensitive entry (da-Mhallete naming -> syrclaim003, Catholicos
application -> syrclaim004, anti-Jewish representativeness ->
syrclaim005).

Conventions carried:
- claim text emic (the world's own voice); challenges name their
  challengers; concedes treats 'our own record does not tell us' as
  data; pressure_response from the S2.5 force layers.
- divergence_partners mapped against the partner worlds' own live
  claim records where a real counterpart exists: syrclaim001 ->
  alexclaim001 (typological raza-reading vs allegorical depth-reading,
  both scripture-hermeneutic formation claims); syrclaim002 ->
  desertclaim001 (town-refusal vs desert-withdrawal - the two worlds'
  opposed shapes of asceticism). partner_claim_id SET (the schema's
  'once it exists' condition met); reverse enrichment stays S6.3.
- FLAG-014 closed for Syriac AT THE CAUSING STEP: contested_claim_ids
  populated on the carrying terms at authoring time (001; 002+007;
  006; 009; 010).
- The Kosinski/Burgess, Jacob-death-date, and Voobus disputes already
  live in the force/story layers - not duplicated as claims here (they
  are dating disputes in the scholarship, not contested claims the
  world's own voice holds).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record
from s62_syr_s23 import read_record, write_record

OUT = BACKEND / "wrs" / "records" / "syriac_world"
WID = "syriac-edessa-nisibis"


def C(id_, claim, held, concedes, pressure, partners, srcs):
    rec = {"world_id": WID, "record_type": "contested_claim",
           "schema_version": 1, "jobs": [8], "register": "emic",
           "review_state": "draft", "id": id_,
           "sources": [{"source_id": s} for s in srcs],
           "claim": claim, "held_against": held, "concedes": concedes,
           "pressure_response": pressure}
    if partners:
        rec["divergence_partners"] = partners
    return rec


CLAIMS = [
 C("syrclaim001",
   ("A raza is bound to the shrara it signifies and carries something of "
    "that truth's own hidden power. To read Scripture, or creation "
    "itself, rightly is to perceive connections already woven into the "
    "world by its Maker - not connections a clever interpreter invents - "
    "and so our theology is sung into the body in madrashe rather than "
    "argued in syllogisms: the hymn is itself the argument, and the "
    "formed eye is itself the method."),
   [{"challenge": ("The modern representational account of symbol - a "
                   "chosen stand-in, replaceable by another sign, related "
                   "to its referent only by convention - which hears "
                   "'just a metaphor' where this world claims real "
                   "participation (the syrlex001 Modern Hearing; the "
                   "Platonic/allegorical contrast object Doc_03 SS1.1 "
                   "names)."),
     "challenger": "the modern representational theory of symbol",
     "sources": [{"source_id": "srcSYR029"}]},
    {"challenge": ("The world's own evidence base, read against its "
                   "author concentration: the fullest articulation "
                   "(hayla kasya, 'hidden power') is substantially "
                   "Brock's synthesis of EPHREM specifically; Aphrahat's "
                   "cognate usage is real but plainly lighter, one "
                   "exegetical tool among several - and any claim that "
                   "this method organized the WHOLE world's reading, "
                   "beyond its one overwhelming voice, is capped at "
                   "Dominant Modern Reconstruction (Doc_04 C1; Doc_08 "
                   "1B-1; the dominance effect, Doc_02 SS3)."),
     "challenger": ("the world's own transmission record, read against "
                    "the Ephrem dominance effect"),
     "sources": [{"source_id": "srcSYR010"}, {"source_id": "srcSYR029"}]}],
   ("Whether every believer - the unlettered, the ordinary household, "
    "the majority whose voices transmission did not carry - read and "
    "heard by raza the way our teacher sang it, our own record does not "
    "tell us. What survives is the clerical-ascetic teaching register; "
    "the pew's own hearing is not attested."),
   ("Under sustained pressure from rivals singing in the same forms - "
    "Bardaisan's circle, Mani's hymnody - this way of reading "
    "INTENSIFIED rather than fractured: sharpened into explicit polemic "
    "in the Prose Refutations and Contra Haereses, deployed more "
    "pointedly, never abandoned (Doc_04 C1 forces-connection; "
    "syrforce2A2)."),
   [{"world_id": "alexandria-catechetical",
     "note": ("A real counterpart claim, mapped against Alexandria's own "
              "live record: both worlds hold Scripture-reading as itself "
              "formative and perceptual (a capacity of the formed eye/"
              "soul, not a decoding skill) - but Alexandria's depth runs "
              "through philosophical preparation and allegorical ascent "
              "(preparation -> depths), while this world's raza binds "
              "symbol to truth WITHOUT the Greek categorical apparatus, "
              "sung rather than argued. Same conviction that reading "
              "transforms; genuinely different machinery."),
     "partner_claim_id": "alexclaim001"}],
   ["srcSYR001", "srcSYR009", "srcSYR010", "srcSYR029"]),
 C("syrclaim002",
   ("To take the qyama is to stand for a promise that does not end - a "
    "lifelong vow of celibacy and watchfulness lived among one's own "
    "kin, in town, inside ordinary community life: our askesis is "
    "refusal within the world, not flight from it. The Ihidaya's "
    "singleness participates, in the very root of the name, in the "
    "Only-Begotten's own undividedness - our discipline and our "
    "confession are one word."),
   [{"challenge": ("Later monastic categories read backward: 'monk,' "
                   "'nun,' 'monastery,' enclosure and rule - the "
                   "desert-and-cloister shape assumed as what a vowed "
                   "celibate order must be, when this order's own "
                   "town-resident, kin-embedded shape is genuinely "
                   "different and less institutionally fixed (syrlex002 "
                   "Modern/World Hearing)."),
     "challenger": "later monasticism's categories, retrojected"},
    {"challenge": ("The scholarship on the order's internal structure: "
                   "existence, vowed celibacy, and fourth-century "
                   "attestation are solidly evidenced, but whether the "
                   "qyama had a settled rule, enclosure practice, or "
                   "internal hierarchy is thinly and contestedly "
                   "documented - Contested/Inferential-Thin, not to be "
                   "presented as settled (syrlex002 CT; Doc_02 SS2's "
                   "caution on Malki's continuous-stratum treatment)."),
     "challenger": ("the modern scholarship on the order's structure "
                    "(Harvey; Malki, used cautiously per Doc_02)"),
     "sources": [{"source_id": "srcSYR032"}, {"source_id": "srcSYR033"}]},
    {"challenge": ("The later tradition's claim that Ephrem personally "
                   "organized and led the bnat qyama as his own choirs - "
                   "resting on Jacob of Serugh's 6th-century panegyric "
                   "and the 6th-century Vita Ephraemi, OUTSIDE this "
                   "world's own 200-410 window, and excluded from this "
                   "claim's evidentiary basis entirely at Doc_04 Round "
                   "2 (told among us only as syrstory007, a later "
                   "teacher's loving memory, named as such)."),
     "challenger": "the 6th-century hagiographic tradition",
     "sources": [{"source_id": "srcSYR045"}, {"source_id": "srcSYR059"}]}],
   ("What the vow's daily interior was - and what formal shape the "
    "order carried beyond its existence, its celibacy, and its "
    "town-embedded character - our own record does not tell us. The "
    "bnat qyama sang; their own unmediated voice is not among what "
    "survives (Doc_02 SS7)."),
   ("This institution HELD steadily across the window - Doc_04 found no "
    "forces-dynamic and manufactured none; its one documented "
    "downstream relationship is reshaping the world's own authority "
    "plurality (the vowed pathway standing alongside episcopal office, "
    "C2xC4)."),
   [{"world_id": "desert-monasticism",
     "note": ("The two worlds' opposed shapes of asceticism, mapped "
              "against Desert's own live record: the desert holds "
              "withdrawal as the most demanding form of engagement "
              "(departure as the claim); this world holds refusal "
              "WITHIN town and kin as its own askesis - a vowed life "
              "that never leaves. Same seriousness about the vowed "
              "body; opposed geographies of where the discipline "
              "lives. The syrlex002 chunk's own retrieve-when names "
              "exactly this confusion risk."),
     "partner_claim_id": "desertclaim001"}],
   ["srcSYR010", "srcSYR013", "srcSYR032", "srcSYR033"]),
 C("syrclaim003",
   ("When we say the Gospel we mean one continuous story - the harmony "
    "Tatian wove, read at the lectern, quoted by Aphrahat, commented "
    "whole by Ephrem. What our own tongues called that book in our own "
    "years, our record does not settle: Ephrem's Commentary calls it "
    "simply the Gospel."),
   [{"challenge": ("The assumption that 'Ewangeliyon da-Mhallete' was a "
                   "settled, established vernacular label throughout the "
                   "period: Theodoret's 420s-430s account of confiscating "
                   "'more than two hundred such books' is in GREEK and "
                   "never uses the Syriac phrase - it attests the "
                   "Diatessaron's suppression, not the name; per "
                   "Crawford's peer-reviewed work the name's earliest "
                   "secure Syriac witness may be an anonymous gloss in "
                   "the Syriac translation of Eusebius's Ecclesiastical "
                   "History, roughly contemporary with Theodoret - the "
                   "dating is UNRESOLVED, not settled to either side of "
                   "the 410 boundary (syrlex006 CT)."),
     "challenger": ("the scholarship on the name's earliest attestation "
                    "(Theodoret's Greek testimony; Crawford)"),
     "sources": [{"source_id": "srcSYR043"}, {"source_id": "srcSYR028"}]}],
   ("Whether the name 'da-Mhallete' was in use during our own years, our "
    "record does not tell us - the practice is well attested throughout "
    "the window; the label is not clearly a settled anchor point one "
    "way or the other."),
   ("The practice itself HELD steadily across the whole window; its "
    "supersession by the separated Gospels is this world's own closing "
    "transition, not a mid-window response (Doc_04 C5; syrforce3B2 - "
    "with the Voobus contest of Rabbula's personal role carried there, "
    "not resolved here)."),
   None,
   ["srcSYR009", "srcSYR010", "srcSYR011", "srcSYR028"]),
 C("syrclaim004",
   ("No one among us called any bishop 'Catholicos.' Our churches knew "
    "real leaders and real quarrels over precedence - Papa's claim to "
    "primacy, and Miles of Susa and Aqib-Alaha who withstood it - but "
    "the single named office came later, laid back over our years by "
    "those who came after."),
   [{"challenge": ("The traditional Church-of-the-East succession, which "
                   "records an unbroken titled line back through Papa "
                   "bar Aggai ('Catholicos' from c. 315) to the first "
                   "century - resting at least in part on the Acts of "
                   "Mari (a text dated anywhere from the sixth to the "
                   "eighth century) and on the chronicle tradition "
                   "(Chronicle of Seert; Bar Hebraeus; as reconstructed "
                   "by Fiey), chronicle-derived and hagiographically "
                   "inflected rather than contemporary attestation "
                   "(syrlex009; Doc_02 SS11)."),
     "challenger": ("the later Church-of-the-East chronicle and "
                    "succession tradition"),
     "sources": [{"source_id": "srcSYR042"}]}],
   ("What titles WERE in contemporary use for Persian church leadership "
    "beyond 'bishop,' our record does not tell us; the contest is "
    "weighed on the balance of evidence (the title's absence from "
    "in-window sources), not on a proven negative - which is why this "
    "claim's own confidence is Contested rather than Documented "
    "(syrlex009 CT: 'contested - the balance of evidence indicates it "
    "was not' in contemporary use)."),
   ("The underlying authority structure this later title tidies over "
    "was itself FRACTURED by persecution within our own years - the "
    "twenty-year silence after Barba'shmin's death - and was settled "
    "only from outside, at the 410 Synod, at this world's own closing "
    "edge (the C4 arc; syrforce2A1/3A2/3B1)."),
   None,
   ["srcSYR010", "srcSYR042", "srcSYR051"]),
 C("syrclaim005",
   ("A real portion of our teacher's surviving work - on the order of "
    "four of the twenty-three Demonstrations - argues against Jewish "
    "practice and interpretation: circumcision, the Sabbath, dietary "
    "law, the dating of Passover. We name this plainly as our own "
    "record's real, sustained thread, carrying real contempt; we own it "
    "as our own life's fault, without inventing a companion account of "
    "others among us who warned against it, and without an answering "
    "Jewish voice to set beside it - for none survives in our record."),
   [{"challenge": ("The representativeness question, genuinely contested "
                   "in the scholarship: Koltun-Fromm's own reading "
                   "treats this material as a live, localized exchange "
                   "specific to Aphrahat's own community - 'a "
                   "reconstructed conversation,' one side's account of "
                   "an argument, not a transcript - against any reading "
                   "that would take it as a generic literary topos "
                   "speaking for Persian Christianity as a whole "
                   "(syrlex010 Key Sources; Doc_02's own "
                   "representativeness flag)."),
     "challenger": ("the scholarship on the material's scope "
                    "(Koltun-Fromm's localized-exchange reading vs the "
                    "generic-topos reading)"),
     "sources": [{"source_id": "srcSYR031"}]},
    {"challenge": ("The structural absence of the other side: every word "
                   "of the exchange survives only in Aphrahat's own "
                   "voice; no independent Jewish source from his own "
                   "time and place confirms, corrects, or answers his "
                   "characterization of the disagreement."),
     "challenger": "the record's own one-sidedness, named as evidence",
     "sources": [{"source_id": "srcSYR030"}]}],
   ("The other side of the exchange - and how far this polemic "
    "represents Persian Christianity beyond Aphrahat's own community - "
    "our record does not tell us. This claim asserts the thread's "
    "reality and our honest ownership of it; it asserts nothing about "
    "how Jewish people or practice should be regarded, then or now "
    "(the syrlex010 Standing Distortion-Risk Note's own boundary, "
    "which governs every retrieval of this material)."),
   ("Held as one side of a real, historically situated argument this "
    "community understood itself to be having; the record gives no "
    "evidence of the exchange's own later course within the window, "
    "and this world's runtime never renews the argument on its merits "
    "(the force_llm_vote gate + the Standing Note's posture)."),
   None,
   ["srcSYR010", "srcSYR030", "srcSYR031"]),
]

# FLAG-014 at the causing step: contested_claim_ids on the carrying terms
CARRIERS = {
    "syrlex001": ["syrclaim001"],
    "syrlex002": ["syrclaim002"],
    "syrlex007": ["syrclaim002"],
    "syrlex006": ["syrclaim003"],
    "syrlex009": ["syrclaim004"],
    "syrlex010": ["syrclaim005"],
}


def main():
    for rec in CLAIMS:
        emit_record(rec,
                    ("S6.2/SYR S2.6-equivalent contested_claim record "
                     "(2026-07-28). Contest routing: the S2.2 CT parkings "
                     "(syrlex002/006/009) + the Primary-gravity minimum "
                     "(C1, C2) + the sensitive entry's representativeness "
                     "contest. Divergence partners mapped against the "
                     "partner worlds' own LIVE claim records "
                     "(alexclaim001; desertclaim001) - partner_claim_id "
                     "set, reverse enrichment stays S6.3. See "
                     "wrs/migrate/s62_syr_s26.py."),
                    OUT / "contested_claim" / f"{rec['id']}.md")
    for tid, cids in CARRIERS.items():
        path = OUT / "term" / f"{tid}.md"
        front, body = read_record(path)
        front["contested_claim_ids"] = cids
        write_record(path, front, body)
    print(f"wrote {len(CLAIMS)} claims; contested_claim_ids on "
          f"{len(CARRIERS)} carrying terms (FLAG-014 at the causing step)")


if __name__ == "__main__":
    main()
