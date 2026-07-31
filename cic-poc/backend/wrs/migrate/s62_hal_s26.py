"""S6.2/HAL - S2.6-equivalent: contested_claim records.

5 records: the Standard's Primary-gravity minimum (G1 -> halclaim001,
G2 -> halclaim002, G3 -> halclaim003) + the S2.2 CT parking
(hal_lex08's Origenism Contest Type -> halclaim004) + the Tensional
gravity's own Contested core (Marcella's standing -> halclaim005).

Routing decisions, DECLARED:
- The Hebrew-fluency contest (hallex12's split; Doc_01 Open Issue #2)
  is FOLDED into halclaim001 as a challenge, not a sixth claim -
  Doc_04 SS1 itself merged Hebrew-study-as-practice into G1 because
  practice and principle 'are not evidenced as separable in this
  world's own sources' (halgrav008's not-advanced reason); splitting
  them at the claim layer would undo the document's own merge.
- The Eustochium 418/419/420 terminus clustering, the Marcella-list
  apparatus caveat, and the 384-385 formal-synod question are NOT
  claims: the first is a dating dispute in the scholarship (the SYR
  Kosinski/Burgess precedent - lives in halcore001 + halfig004), the
  second a verification item (pre-freeze re-sweep), the third an
  Inferential/Thin non-assertion already carried by halstory02/2A-4.
- NO Pelagianism claim: Doc_08's completed CT decision - an
  acknowledged internal uncertainty is not a Contested Tradition
  without an identifiable external scholarly contest; the attack's
  record lives in halstory04/halforce3A2.

Conventions carried:
- claim text emic; challenges name their challengers; concedes treats
  'our own record does not tell us' as data; pressure_response from
  the S2.5 force layers.
- divergence_partners mapped against the partner worlds' own LIVE
  claim records: halclaim001 -> alexclaim001 (scripture-hermeneutic
  formation claims - the SYR syrclaim001 class, third member);
  halclaim002 -> desertclaim001 (shapes of asceticism - the
  syrclaim002 class, third member); halclaim003 -> alexclaim004
  (non-office authority currencies); halclaim004 -> alexclaim005
  (Origen's legacy held with unease THERE, renounced urgently HERE -
  the fleet's first claim pair where one world contests the OTHER
  world's own teacher). partner_claim_id SET; reverse enrichment
  stays S6.3.
- FLAG-014 closed for HAL AT THE CAUSING STEP: contested_claim_ids
  populated on the carrying terms now (01/02/12 -> 001; 03 -> 002;
  06 -> 003; 08 -> 004; 11 -> 005).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BACKEND = HERE.parents[1]
sys.path.insert(0, str(HERE))

from source_rows_from_doc02 import emit_record
from s62_hal_s23 import read_record, write_record

OUT = BACKEND / "wrs" / "records" / "hieronymian_world"
WID = "hieronymian-ascetic-literary"


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
 C("halclaim001",
   ("When the word passed from Hebrew into Greek, something of its "
    "precision was lost - not through malice, but through the ordinary "
    "friction of moving between tongues - and a scholar who returns to "
    "the Hebrew recovers what the Greek, however venerable, cannot "
    "fully carry. We do not despise the Greek; we love it and quote it "
    "constantly. But when the two disagree, the Hebrew is heard first, "
    "and we have borne the cost of saying so: a congregation's anger "
    "over a changed word, years with a teacher outside our faith, and "
    "the standing charge of tampering with what the church already "
    "trusted."),
   [{"challenge": ("The received-text side of the church's own argument, "
                   "in its most serious form: Augustine's letters "
                   "pressing that abandoning the Septuagint's received "
                   "authority endangers the continuity and unity of a "
                   "church that has prayed and preached from one text "
                   "for generations - resistance from serious churchmen "
                   "for serious reasons, independently attested in the "
                   "challenger's own surviving letters (the rare "
                   "two-sided case; hal_lex01 Distortion Risk; "
                   "halstory03)."),
     "challenger": ("Augustine and the wider Latin consensus for the "
                    "Septuagint's received authority"),
     "sources": [{"source_id": "srcHAL009"}]},
    {"challenge": ("The content-level contest, folded here per Doc_04's "
                   "own merge of practice into principle: how far the "
                   "Hebrew competence underneath the principle actually "
                   "extended is separately and seriously Contested in "
                   "the scholarship (Williams; Doc_01 Open Issue #2) - "
                   "the grammar training under it is solidly attested, "
                   "the fluency it supposedly enabled is not (hallex12's "
                   "two confidence levels, held apart)."),
     "challenger": ("the modern scholarship on Jerome's Hebrew "
                    "competence (Williams)"),
     "sources": [{"source_id": "srcHAL013"}]},
    {"challenge": ("The world's own evidence base, read against its "
                   "Author Gravity: the principle's articulation "
                   "survives almost entirely in Jerome's own voice (the "
                   "prefaces - by genre a single-voice, self-justifying "
                   "source type, hal_lex13's own caveat); its "
                   "CONTESTEDNESS is independently attested, its content "
                   "is not (Doc_04 G1's generation flag)."),
     "challenger": ("the record's own single-voicedness (the preface "
                    "genre's self-justifying character)"),
     "sources": [{"source_id": "srcHAL023"}]}],
   ("Whether the congregations who prayed the older words ever came to "
    "hear ours as truer, our record mostly does not tell us - what "
    "survives is the scholar's own defense, preface by preface, and "
    "the anger at Oea. And how deep the Hebrew finally ran, we claim "
    "no more than our record can carry: the labor is documented; the "
    "mastery is argued about."),
   ("Under the Augustine dispute this commitment INTENSIFIED - "
    "articulated and refined specifically in response to the contest, "
    "never softened to end it (halforce2A2); at its sole defender's "
    "death it TRANSFORMED - from live, argued project to fixed, "
    "undefended text (halforce3B2). The argument was constitutive: "
    "remove the contest and the surviving articulation itself is "
    "different."),
   [{"world_id": "alexandria-catechetical",
     "note": ("The scripture-hermeneutic class's third member (with "
              "syrclaim001): all three worlds hold scripture-engagement "
              "as itself formative - but Alexandria's depth runs "
              "through the GREEK text's allegorical depths opened to "
              "the prepared soul, while this world's claim is that the "
              "Greek itself must be corrected against the Hebrew "
              "beneath it. Same seriousness about the text; this world "
              "contests the very textual foundation the partner world "
              "reads from."),
     "partner_claim_id": "alexclaim001"}],
   ["srcHAL001", "srcHAL023", "srcHAL009", "srcHAL013"]),
 C("halclaim002",
   ("To renounce among us is to unmake one's place in public: the land "
    "sold or redirected, the marriage that would have bound two houses "
    "declined, plain dress announcing the change to a Rome that "
    "judged. It is not private simplicity; it is a costly, watched, "
    "family-disrupting act - and from the same emptied purse rose a "
    "monastery, a convent, a house of welcome, and in Rome a hospital "
    "for the sick gathered in from the streets."),
   [{"challenge": ("The evidence's own shape, per Doc_04's Round-1 "
                   "correction carried without softening: the pattern "
                   "is attested across three letters BY ONE AUTHOR IN "
                   "ONE IDEALIZING GENRE (the epitaph and exhortation) "
                   "- not independent attestation; the actual "
                   "independent corroboration is the social-historical "
                   "scholarship on senatorial renunciation, whose named "
                   "standard work (Brown 2012) this migration's own "
                   "registry does not yet hold (the S2.1b miss, "
                   "pre-freeze re-sweep)."),
     "challenger": ("the one-author-one-genre evidence base, read "
                    "against the epitaph genre's idealizing "
                    "conventions"),
     "sources": [{"source_id": "srcHAL011"}, {"source_id": "srcHAL012"}]},
    {"challenge": ("The unresolved tension the household's own memory "
                   "holds: Paula gave until her household could not say "
                   "where the wealth had gone, AND she still built at "
                   "scale - total poverty and continuing capacity told "
                   "together, without resolving which was truer "
                   "(halstory06's own frame; the scale of Fabiola's "
                   "foundation likewise not independently verified)."),
     "challenger": "the record's own unresolved poverty-vs-capacity tension"},
    {"challenge": ("This world's own contemporaries: a resilient pagan "
                   "senatorial culture that read renunciation as "
                   "betrayal of family and rank - mockery and "
                   "suspicion, not admiration; and within the church, "
                   "praise that sometimes suspected itself of excess "
                   "(Blaesilla's death laid at the teacher's door) "
                   "(halforce2A1; halstory02)."),
     "challenger": ("the senatorial culture the renouncers left "
                    "(and the city's blame after Blaesilla)"),
     "sources": [{"source_id": "srcHAL017"}]}],
   ("Where each fortune precisely went, and at what pace, our record "
    "does not tell us - the epitaphs remember meaning, not "
    "accounting. And Blaesilla we carry as our own cost: the severity "
    "that broke her health came from the discipline we praised."),
   ("HELD, and if anything deepened, across every pressure the span "
    "brought - the pagan backlash, the 384-385 crisis, the relocation "
    "itself (the practice funded the move that the crisis forced) "
    "(halforce1A1/2A1/2A4)."),
   [{"world_id": "desert-monasticism",
     "note": ("The shapes-of-asceticism class's third member (with "
              "syrclaim002): the desert holds withdrawal as the most "
              "demanding engagement; Syriac holds refusal within town "
              "and kin; this world holds ARISTOCRATIC UNMAKING - "
              "renunciation exercised from senatorial wealth, publicly "
              "watched, that then funds a monastic settlement adapting "
              "the desert's own template at one remove (the household's "
              "desert romances are its literary answer to the Egyptian "
              "stories, halstory09). Same seriousness about the "
              "renounced body; a third geography - the emptied "
              "household."),
     "partner_claim_id": "desertclaim001"}],
   ["srcHAL001", "srcHAL017", "srcHAL020"]),
 C("halclaim003",
   ("Ask where authority lived among us and the honest answer is not a "
    "bishop's seat. It lived in being trusted, and being funded, by "
    "those with the wealth to make the work possible - a scholar's "
    "whole labor resting on whether a widow's fortune continued to "
    "back him. This is not background to our life; it is close to how "
    "our world actually worked, and it made our authority genuinely "
    "vulnerable: when favor died and rumor turned, there was no "
    "office to fall back on."),
   [{"challenge": ("The rival mode this world's own era took as normal: "
                   "episcopal and territorial authority - ordination, "
                   "office, the see - against which this world's "
                   "patronage-based standing is the differentiation "
                   "axis itself (Doc_01 SS8.1); the era's default "
                   "answer to 'where does authority live' was the "
                   "bishop's, not this world's."),
     "challenger": "the episcopal-territorial authority mode of this world's own era"},
    {"challenge": ("The evidentiary split, named at Doc_04: the "
                   "interpretive frame (patronage as the career's "
                   "structure) is genuinely independent scholarly "
                   "consensus (Rebenich, Cain) - but the specific "
                   "financial mechanics rest on Jerome's own account, "
                   "one interested voice on where the money moved."),
     "challenger": ("the single-voiced financial mechanics under an "
                    "independently-framed structure"),
     "sources": [{"source_id": "srcHAL015"}, {"source_id": "srcHAL010"}]}],
   ("What the patrons themselves would have said of the relationship - "
    "Paula's own account of her funding, Marcella's of her backing - "
    "our record does not tell us: the pens that survive are the "
    "funded scholar's, not the funding women's (Doc_02's Author "
    "Gravity; the 'Lady Vanishes' problem the scholarship names)."),
   ("SHIFTED but never fractured: the 384-385 crisis moved the "
    "structure from Rome-based, clerically-entangled patronage to the "
    "more insulated Bethlehem arrangement - the material chain (Paula) "
    "held while the clerical chain (Damasus) failed, which is the "
    "claim's own proof: the funded relationship outlived the office's "
    "favor (halforce2A4)."),
   [{"world_id": "alexandria-catechetical",
     "note": ("Two non-office authority currencies, mapped against "
              "Alexandria's own live claim: there, the teacher's "
              "authority is demonstrated WISDOM enacted as "
              "accompaniment (trusted because others saw that he saw); "
              "here, authority is trusted RELATIONSHIP sustained by "
              "wealth (trusted, and funded). Both worlds locate real "
              "authority outside episcopal office; the currencies - "
              "seen wisdom vs funded trust - are genuinely different, "
              "and this world's own Tensional counter-current "
              "(Marcella, halclaim005) is the place where the two "
              "currencies meet in one person."),
     "partner_claim_id": "alexclaim004"}],
   ["srcHAL015", "srcHAL010", "srcHAL001"]),
 C("halclaim004",
   ("We had learned to read scripture, more than we liked to admit, "
    "from a teacher whose specific conclusions - souls before this "
    "life, the nature of the resurrected body - we then had to "
    "renounce, urgently and in public, once the wider church turned "
    "against them. A friend who had translated beside us would not "
    "renounce as fully or as fast, and became from then on the target "
    "of some of our own harshest writing. The quarrel was never only "
    "doctrine: it was about which teacher's account of our own "
    "faithfulness would be believed."),
   [{"challenge": ("The named, ongoing scholarly contest (the hal_lex08 "
                   "Contest Type, unparked here): whether the "
                   "controversy was doctrinal or personal/political in "
                   "substance is genuinely, actively debated in the "
                   "literature this construction draws on (Clark's "
                   "Origenist Controversy is the anchor study) - and "
                   "this world's record does not resolve it: both "
                   "Apologiae survive, each framing the other's "
                   "motives, neither privileged (halstory03a's own "
                   "rule)."),
     "challenger": ("the scholarship's doctrinal-vs-political contest "
                    "(Clark), held open by the two-sided record "
                    "itself"),
     "sources": [{"source_id": "srcHAL016"}, {"source_id": "srcHAL005"},
                 {"source_id": "srcHAL007"}]}],
   ("Whether doctrine or the friendship's breaking weighed more, we do "
    "not decide - our own record holds both readings in tension, and "
    "the fiercest words on both sides were written by men who had "
    "once worked from one desk. What the renounced teachings meant to "
    "us BEFORE the renunciation, our record shows mostly through "
    "what the renouncing cost."),
   ("Absorbed by an already-established pattern rather than generating "
    "a new one: the controversy was conducted through, and "
    "threatened, the patronage network itself (the polemic's own "
    "addressees are patrons), replaying 2A-4's relational-rupture "
    "exposure inside the community - one friend's alliance lost where "
    "one patron's protection had been lost before "
    "(halforce2B1/2A4)."),
   [{"world_id": "alexandria-catechetical",
     "note": ("The fleet's first claim pair where one world contests "
              "the OTHER world's own teacher: Alexandria holds "
              "Origen's speculative teaching as exploration offered "
              "under the Rule of Faith - inheritance and unease held "
              "together within its own horizon; this world, two "
              "centuries on, is where that unease became rupture - "
              "the same teachings renounced urgently and in public "
              "under a church that had turned. The partner world's "
              "'held with unease' and this world's 'renounced at "
              "cost' are two moments of one tradition's self-"
              "correction, and neither world's claim resolves whether "
              "the correction was doctrinally necessary or "
              "politically driven."),
     "partner_claim_id": "alexclaim005"}],
   ["srcHAL005", "srcHAL007", "srcHAL016"]),
 C("halclaim005",
   ("There was a house in Rome where clergy brought the hardest "
    "scriptural questions - and the one who answered held no office "
    "at all. Her standing was real: earned by demonstrated learning, "
    "exercised in person, in her own house, on her own authority, "
    "from her own settled wealth - needing no one's patronage. Even "
    "before the scholar left, she disputed his answers - to learn, he "
    "says, not to win."),
   [{"challenge": ("The evidence's whole weight rests on one source: "
                   "Jerome's own memorial letter (Ep. 127), written "
                   "after her death, for purposes that include his own "
                   "vindication against Origenist critics (Cain's "
                   "reading) - single-source, post-mortem, "
                   "self-interested; Contested by this world's own "
                   "five-level vocabulary, and the very letter that "
                   "attests her standing enlists it in the author's "
                   "own defense (Doc_04 G5's Cross-Check; srcHAL001's "
                   "Marcella-list caveat and srcHAL012's unverified "
                   "pairing flag both bear here)."),
     "challenger": ("the single-voice, post-mortem, self-vindicating "
                    "character of the sole attestation (Cain)"),
     "sources": [{"source_id": "srcHAL001"}, {"source_id": "srcHAL012"},
                 {"source_id": "srcHAL010"}]},
    {"challenge": ("The double modern distortion, both directions "
                   "wrong: overclaiming this as independent "
                   "theological authority equivalent to ordained "
                   "office, or dismissing it as merely social and "
                   "therefore unimportant - the record supports "
                   "neither; and Doc_04's direct test found the "
                   "authority the SAME underlying currency as the "
                   "scholar's own, held in a different, materially "
                   "independent position - not a rival structure (the "
                   "Open-Issue-#7 resolution; strand-singular NOT "
                   "reopened)."),
     "challenger": ("the overclaim/dismiss double misreading (hallex11 "
                    "Distortion Risk; the strand-test's own finding)")}],
   ("How often the clergy came, and with what questions, no record "
    "but his remains to say - the extent and frequency of the "
    "consultations are not usable as documented fact, only as this "
    "world's own remembered account (halstory07's rule, which "
    "governs every telling). We never tell it as rivalry: the trust "
    "was of one kind, differently held."),
   ("HELD through the 385 departure - the very event that created "
    "the space for the independent Roman role; FRACTURED at the 410 "
    "sack and her death soon after - an external ending-force "
    "terminating the Rome pole outright; the commemorating letter "
    "itself is controversy-shaped (the G5-M/G6 reshaping cell: her "
    "remembered authority deployed in the author's own vindication) "
    "(halforce1B1/2A4/3A1)."),
   None,
   ["srcHAL001", "srcHAL012", "srcHAL010"]),
]

# FLAG-014 at the causing step: contested_claim_ids on the carrying terms
CARRIERS = {
    "hallex01": ["halclaim001"],
    "hallex02": ["halclaim001"],
    "hallex12": ["halclaim001"],
    "hallex03": ["halclaim002"],
    "hallex06": ["halclaim003"],
    "hallex08": ["halclaim004"],
    "hallex11": ["halclaim005"],
}


def main():
    (OUT / "contested_claim").mkdir(exist_ok=True)
    for rec in CLAIMS:
        emit_record(rec,
                    ("S6.2/HAL S2.6-equivalent contested_claim record "
                     "(2026-07-31). Contest routing: the Primary-gravity "
                     "minimum (G1/G2/G3) + the hal_lex08 CT parking "
                     "(Origenism) + the Tensional gravity's Contested "
                     "core (Marcella). The Hebrew-fluency contest folded "
                     "into halclaim001 per Doc_04's own practice-into-"
                     "principle merge; Eustochium clustering / "
                     "Marcella-list caveat / formal-synod question / "
                     "Pelagianism-no-CT all declared non-claims (see "
                     "wrs/migrate/s62_hal_s26.py). Divergence partners "
                     "mapped against LIVE partner records (alexclaim001, "
                     "desertclaim001, alexclaim004, alexclaim005) - "
                     "partner_claim_id set, reverse enrichment stays "
                     "S6.3."),
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
