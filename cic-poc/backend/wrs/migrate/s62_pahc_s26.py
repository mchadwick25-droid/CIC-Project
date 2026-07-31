"""S6.2/PAHC - S2.6-equivalent: contested_claim records.

5 records: the Primary-gravity minimum (G02 -> pahcclaim001, G07 ->
pahcclaim002) + the CT parkings unparked (the episkopos
secured-vs-argued contest, absorbing pahclex001's AND pahclex002's
parkings plus the Ignatius three-way authenticity dispute ->
pahcclaim003; the agape/eucharist identity question -> pahcclaim004)
+ the ministrae role question -> pahcclaim005.

Routing decisions, DECLARED:
- The Ignatius authenticity three-way dispute (Trajanic / redated /
  pseudepigraphic) is FOLDED into pahcclaim003 as a challenge, not a
  sixth claim: it is the evidentiary substrate of the Strand-A side,
  and the story/figure records already carry it at telling-time.
- The Justin-representativeness CT (pahclex004's parking) is FOLDED
  into pahcclaim002 as a challenge (it contests the G07 claim's
  evidence, not a separate position of the world's voice).
- NON-CLAIMS with reasons: the Two Ways single-source cap
  (evidence-character carried in records, not a contest between
  positions); hetaeria/pertinacia's Inferential-Thin (the same);
  the 1 Clement dating range, the Polycarp splice question, and
  Hermas's staging (dating disputes in the scholarship - the SYR
  Kosinski/Burgess class, living in the story/figure records).

Divergence partners - THE FIRST FIVE-WORLD PARTNER FIELD:
- pahcclaim003 -> alexclaim004 AND halclaim003 (the
  where-authority-lives class, now three-membered: seen wisdom /
  funded trust / office argued between two strands).
- pahcclaim005 -> halclaim005 (the fleet's women's-standing
  single-source pair: the consulted widow known through her
  teacher's memorial letter; the servant-women known through their
  persecutor's report - each world holding one voice's evidence
  with its own honesty discipline).
- pahcclaim001/002/004: partnerless, declared (no counterpart claim
  lives in any frozen world's record; none manufactured).

FLAG-014 closed for PAHC AT THE CAUSING STEP: contested_claim_ids on
the carrying terms (001/002/006 -> 003; 003 -> 001; 004 -> 002;
010 -> 004; 009 -> 005).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(BACKEND))
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record
from s62_pahc_s23 import read_record, write_record

OUT = BACKEND / "wrs" / "records" / "pahc_world"
WID = "post-apostolic-house-church"


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
 C("pahcclaim001",
   ("The ekklesia in Antioch and the ekklesia in Rome and the ekklesia "
    "in Corinth are one ekklesia - not because we share a structure or "
    "answer to a common office, but because the letters traveling "
    "between us carry the proof that we belong to something larger "
    "than the room we gather in. When a letter arrives from a sister "
    "church it is never only news: it is the assurance that others, "
    "under another roof, hold the same name and face the same "
    "questions. Our unity is exercised by courier and copyist - "
    "Rome's long letter to Corinth, the letters gathered at Smyrna "
    "and forwarded to Philippi at their own asking."),
   [{"challenge": ("The record's own filter, named without flinching: "
                   "the network that carried our letters also DECIDED "
                   "which survived - what had institutional backing or "
                   "later apologetic value was copied on; what was "
                   "vulnerable or marginal was structurally less likely "
                   "to survive regardless of how common it was. The "
                   "network is 'a selection effect, not a neutral "
                   "pipe' - so the unity we can show you is the unity "
                   "the survivors attest (Doc_08 2B-2; the "
                   "Affirmative-Duty disclosure)."),
     "challenger": ("the transmission record's own survivorship "
                    "filter"),
     "sources": [{"source_id": "srcPAHCP01"}]},
    {"challenge": ("The uniformity question, genuinely contested in "
                   "the scholarship: documented contact, "
                   "infrastructure, and shared language establish ONE "
                   "CONNECTED network - but the further inference of "
                   "one doctrinally and institutionally UNIFORM body "
                   "is actively contested (Bauer, extended by "
                   "Ehrman and Robinson-Koester; counter-critiques "
                   "operate inside the same regionally-differentiated "
                   "frame) - which is exactly why our own record "
                   "carries strands rather than declaring one mind "
                   "(Doc_01 SS4/SS6)."),
     "challenger": ("the regional-differentiation scholarship (the "
                    "Bauer line)"),
     "sources": [{"source_id": "srcPAHCS02"}]}],
   ("What moved between us that no one kept, and which churches "
    "wrote whose letters no one copied on, our record cannot tell us "
    "- the network's own filter stands between us and the whole of "
    "our own correspondence. And connectedness is not sameness: our "
    "letters prove we held one name across many cities; they do not "
    "prove we held one mind, and our own strands show we did not."),
   ("HELD across every pressure the span brought - indeed the "
    "network intensified under pressure rather than fracturing "
    "(Ignatius relying on it precisely because he traveled under "
    "guard; the martyr narrative itself traveling the same roads); "
    "its material precondition (one connected, Greek-legible "
    "Mediterranean) never failed within the window "
    "(pahcforce1A1/2B2)."),
   None,
   ["srcPAHCP02", "srcPAHCP03", "srcPAHCP04"]),
 C("pahcclaim002",
   ("Whatever else has been decided or left open among us, we gather "
    "to give thanks over bread and cup, and that table does more of "
    "our ongoing forming than anything else we do. And we say "
    "plainly what our own record shows: the form varies. One "
    "handbook gives thanks cup-first for vine and knowledge and "
    "gathering, with no supper story told at all; Rome's own account "
    "runs reading, discourse, prayer, thanksgiving 'according to his "
    "ability,' and a collection for whoever is in need; the letters "
    "from Antioch bind the table to the bishop. The constancy is the "
    "table itself, not any one order of it."),
   [{"challenge": ("The representativeness contest (pahclex004's own "
                   "CT, unparked here): whether Justin's fuller, more "
                   "explained account represents a network-wide "
                   "template or one community's own development - the "
                   "fullest account must not be read as most "
                   "representative simply for being most explained "
                   "(the chunk's own methodological caution; "
                   "Bradshaw's liturgical-diversity thesis vs "
                   "Ferguson)."),
     "challenger": ("the network-template question (Bradshaw's "
                    "caution)"),
     "sources": [{"source_id": "srcPAHCP06"}, {"source_id": "srcPAHCS50"}]},
    {"challenge": ("Strand A's own validity claim pressing against "
                   "the diversity: Ignatius counts valid only the "
                   "eucharist under the bishop or his appointee - a "
                   "claim that, taken as network fact, would unmake "
                   "the very variety our record attests; held as one "
                   "strand's instruction (and possibly aspiration "
                   "rather than settled practice - the open Doc_01 "
                   "question), never as the whole world's rule."),
     "challenger": ("the Strand-A validity instruction read as "
                    "network norm"),
     "sources": [{"source_id": "srcPAHCP03"}]}],
   ("Which order was oldest, which most widely kept, whether any "
    "household's table matched another's exactly - our record does "
    "not tell us; it preserves three genuinely different orders and "
    "no umpire among them. We will not average them into one 'early "
    "eucharist' that no community actually kept."),
   ("HELD as the central recurring practice across all three "
    "regions and both strands throughout the window - the "
    "diversity itself persisting because no pressure ever forced "
    "one form onto the others (pahcgrav007; Doc_07 SS3's unevenness "
    "finding)."),
   None,
   ["srcPAHCP01", "srcPAHCP03", "srcPAHCP06"]),
 C("pahcclaim003",
   ("Who leads among us is a live question, not a settled office - "
    "and we hold both of our own answers without declaring either "
    "wrong. In some households one episkopos stands at the center "
    "and obedience to him is the very shape of unity; in others a "
    "council of presbyters governs together and nothing is felt "
    "missing. The same man is addressed as bishop by one "
    "correspondent and names himself 'one of the presbyters' in his "
    "own letter. Authority among us is argued for - urgently, "
    "letter after letter - precisely because those who walked with "
    "the Lord are gone and continuity must now be claimed rather "
    "than pointed to."),
   [{"challenge": ("The term's own double contest (pahclex001's CT, "
                   "unparked): whether Strand A's monarchical "
                   "episkopos names an already-secured office or one "
                   "still being argued into existence - and whether "
                   "that pattern was an emerging network-wide norm or "
                   "a regional peculiarity of Antioch/Asia Minor. "
                   "This world's own evidence does not settle "
                   "either."),
     "challenger": ("the secured-vs-argued and network-vs-regional "
                    "contest (the term's own CT)"),
     "sources": [{"source_id": "srcPAHCP03"}, {"source_id": "srcPAHCP02"}]},
    {"challenge": ("The evidentiary substrate itself, three ways "
                   "(the Ignatius authenticity dispute, folded here "
                   "as the Strand-A side's foundation): traditional "
                   "Trajanic dating; a 130s-140s redating; a "
                   "pseudepigraphic 160-180 reading in which the "
                   "letters are a later composition using Ignatius "
                   "as vehicle for a developed monarchical program. "
                   "The majority position is followed, the minority "
                   "never erased - and G01's Strand-A content, G04, "
                   "and G05 all rest on this one voice (the Ignatius "
                   "vulnerability, Doc_04 SS3)."),
     "challenger": ("the three-way authenticity/dating dispute "
                    "(Huebner/Lechner line vs the majority)"),
     "sources": [{"source_id": "srcPAHCP03"}, {"source_id": "srcPAHCS43"}]},
    {"challenge": ("Polycarp's own both-readings self-designation "
                   "(pahclex002's CT, unparked): institutional "
                   "humility within an already-secured system, or "
                   "evidence the monarchical program had not yet "
                   "been locally adopted - both readings live, "
                   "neither forced."),
     "challenger": "the Polycarp self-designation question",
     "sources": [{"source_id": "srcPAHCP04"}]}],
   ("Which of our two answers was older, which would prevail, and "
    "whether Strand A described a reality or argued for an "
    "aspiration - our own record holds these open; the resolution "
    "our world never produced arrived only as our world closed "
    "(monepiscopacy dominant by c. 200, latest in Rome). We do not "
    "read the ending back into the argument."),
   ("The question INTENSIFIED under every force the span brought - "
    "the eyewitness loss generated it, state pressure sharpened it "
    "(a condemned man deploying his own death as argument), and "
    "its very unevenness preserved the plurality: no pressure ever "
    "grew severe enough to force one strand's answer onto the "
    "other (pahcforce1A2/2A1; Doc_07 SS3). Its resolution is the "
    "world's own closing boundary (pahcforce3B1)."),
   [{"world_id": "alexandria-catechetical",
     "note": ("The where-authority-lives class, now three-membered: "
              "Alexandria's teacher-line authority rests on "
              "demonstrated wisdom enacted as accompaniment; this "
              "world's rests on office actively argued between two "
              "strands - neither settled succession nor seen wisdom, "
              "but the argument itself as the era's condition. Same "
              "question, a third genuinely different answer."),
     "partner_claim_id": "alexclaim004"},
    {"world_id": "hieronymian-ascetic-literary",
     "note": ("The class's second member: the Hieronymian world "
              "answers the same question with funded trust "
              "(patronage as the actual authority structure) - and "
              "sits POST-resolution (its era's default is the "
              "bishop's seat this world's argument had not yet "
              "settled). The two claims bracket the office's "
              "history: argued here, assumed-and-bypassed there."),
     "partner_claim_id": "halclaim003"}],
   ["srcPAHCP02", "srcPAHCP03", "srcPAHCP04", "srcPAHCP05"]),
 C("pahcclaim004",
   ("We share a meal that carries love's own name - agape - and we "
    "will not force our evidence to say more about it than it does. "
    "Ignatius sets the agape under the bishop's oversight; Pliny's "
    "prisoners described an ordinary and harmless meal taken after "
    "reassembling. Whether these name one table or two - whether "
    "the love-feast and the thanksgiving are the same practice, "
    "related practices, or distinct - our record holds both "
    "descriptions without an answer, and we keep it so."),
   [{"challenge": ("The identity question itself (pahclex010's CT, "
                   "unparked): same practice, related practices in "
                   "different communities, or unconnected - "
                   "'aware they may name the same thing or two "
                   "things, without forcing an answer that our "
                   "evidence does not give us' (the chunk's own "
                   "discipline). The entry's own corrected history "
                   "(an earlier draft mis-anchored the label; fixed "
                   "against Smyrnaeans 8's Greek) rides the record "
                   "verbatim."),
     "challenger": ("the agape/eucharist cross-identification "
                    "question"),
     "sources": [{"source_id": "srcPAHCP03"}, {"source_id": "srcPAHCP07"}]}],
   ("Which reading is right, our record does not say - and the "
    "discipline of this entry is that not-forcing IS the honest "
    "position: a world whose tables genuinely varied cannot be made "
    "to answer a question its own evidence never asked."),
   ("Held open across the window; the label's oversight-condition "
    "(Ignatius) belongs to the same Strand-A fusion of table and "
    "authority the world's other records carry "
    "(pahcgrav007/pahcgrav001)."),
   None,
   ["srcPAHCP03", "srcPAHCP07"]),
 C("pahcclaim005",
   ("Women hold recognized service among us - and the word the "
    "record keeps for two of them is not ours. Pliny tortured two "
    "enslaved women he called ministrae to learn what we do; what "
    "he names is real, and what their service was in their own "
    "eyes our record does not give us in their own words. We hold "
    "the evidence honestly rather than overclaiming: recognized "
    "service, attested from outside, under torture."),
   [{"challenge": ("The role question (the chunk's own split, "
                   "carried at the record's conservative side): "
                   "whether 'ministrae' translates our own diakonoi, "
                   "whether it names a recognized office at all, and "
                   "whether their service matched any other "
                   "community's use of the name - Inferential-Thin "
                   "by the chunk's own confidence, and not settled "
                   "by this world's own evidence."),
     "challenger": ("the ministrae/diakonoi correspondence question"),
     "sources": [{"source_id": "srcPAHCP07"}]},
    {"challenge": ("The double modern distortion, both directions "
                   "wrong (the chunk's own Modern Hearing): an "
                   "egalitarian early church matching modern "
                   "ideals, or women with no leadership roles at "
                   "all - the record supports neither."),
     "challenger": "the overclaim/dismiss double misreading"}],
   ("What the two women would say of their own work, we cannot "
    "give you - and we will not put words in the mouths of women "
    "who were made to speak under torture. The evidence's "
    "extraction is part of the evidence: ancient jurists "
    "themselves distrusted what torture produced."),
   ("The service itself is attested across the record (women "
    "holding this service alongside men in some communities, "
    "pahclex005); the outside pressure that produced this "
    "particular attestation is the same G03 exposure the world "
    "organized real parts of its life around (pahcforce2A1)."),
   [{"world_id": "hieronymian-ascetic-literary",
     "note": ("The fleet's women's-standing single-source pair: the "
              "Hieronymian world's consulted widow is known through "
              "ONE voice - her teacher's own memorial letter, "
              "written for purposes that include his vindication; "
              "this world's serving women are known through ONE "
              "voice - their persecutor's report, extracted under "
              "torture. Two worlds, two single attestations, two "
              "honesty disciplines: never overclaim the standing, "
              "never dismiss it, never put words in the women's "
              "mouths. The pair teaches what the sources CANNOT "
              "say louder than what they can."),
     "partner_claim_id": "halclaim005"}],
   ["srcPAHCP07"]),
]

CARRIERS = {
    "pahclex001": ["pahcclaim003"],
    "pahclex002": ["pahcclaim003"],
    "pahclex006": ["pahcclaim003"],
    "pahclex003": ["pahcclaim001"],
    "pahclex004": ["pahcclaim002"],
    "pahclex010": ["pahcclaim004"],
    "pahclex009": ["pahcclaim005"],
}


def main():
    (OUT / "contested_claim").mkdir(exist_ok=True)
    for rec in CLAIMS:
        emit_record(rec,
                    ("S6.2/PAHC S2.6-equivalent contested_claim record "
                     "(2026-07-31). Contest routing per "
                     "wrs/migrate/s62_pahc_s26.py: the Primary minimum "
                     "(G02/G07) + the four CT parkings unparked "
                     "(episkopos + Polycarp absorbed into claim003 with "
                     "the Ignatius three-way dispute; Justin-"
                     "representativeness into claim002; agape/eucharist "
                     "= claim004) + ministrae (claim005). Partners: the "
                     "first FIVE-world field - claim003 -> alexclaim004 "
                     "+ halclaim003 (the where-authority-lives class); "
                     "claim005 -> halclaim005 (the women's-standing "
                     "single-source pair); 001/002/004 partnerless, "
                     "declared."),
                    OUT / "contested_claim" / f"{rec['id']}.md")
    for tid, cids in CARRIERS.items():
        path = OUT / "term" / f"{tid}.md"
        front, body = read_record(path)
        front["contested_claim_ids"] = cids
        write_record(path, front, body)
    print(f"wrote {len(CLAIMS)} claims; contested_claim_ids on "
          f"{len(CARRIERS)} carrying terms (FLAG-014 at the causing "
          f"step)")


if __name__ == "__main__":
    main()
