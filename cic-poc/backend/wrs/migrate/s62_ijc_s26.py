"""S6.2/IJC - S2.6-equivalent: 5 contested claims, absorbing the four
CT Contest Type parkings (primatus, presbeia, homoousios, haeresis)
and covering the three Primary gravities (the FLAG-014 rule closed at
the causing step: every Primary gravity carries at least one claim).

THE IN-WORLD PARTNER PAIR (a fleet first): ijcclaim001 (Strand A's
primacy) and ijcclaim002 (Strand B's throne-rank) are DIVERGENCE
PARTNERS WITH EACH OTHER - the world's own central contest carried as
two claims in two strand-voices (the Plural-Voices device at claim
level), each holding the other as its nearest rival. Cross-world
partners ride live claim ids:
- ijcclaim001 <-> pahcclaim003 (the where-authority-lives class gains
  its FOURTH member: argued office there, office-now-claiming-
  settledness here - the ending-not-read-back discipline seen from
  the settling side) + halclaim003 (trust vs office).
- ijcclaim004 <-> alexclaim003 (the fleet's second same-doctrine-
  different-carriage pair, the halclaim004<->alexclaim005 class:
  homoousios held SIMPLY there, resisted-hedged-set-aside-by-command
  within living memory here).
"""
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from source_rows_from_doc02 import emit_record

BACKEND = HERE.parents[1]
OUT = BACKEND / "wrs" / "records" / "imperial_juridical_world"
WID = "imperial-juridical-christianity"

CLAIMS = [
 {"id": "ijcclaim001",
  "claim": ("A claim is settled when it is received at this see and "
            "confirmed as consonant with what the apostle himself held "
            "- not merely because a council votes on it, or because an "
            "emperor is present when the vote is taken. What was given "
            "to Peter was given to the one who holds his seat after "
            "him: the spiritual warrant IS the juridical warrant, one "
            "claim, not a religious cover over a political one."),
  "held_against": [
   {"challenge": ("The CT contest (ijclex001's parking, unparked): "
                  "whether this world's own primacy claim is the "
                  "origin of a divinely-instituted office or a "
                  "historically contingent institutional development "
                  "is a live contest between present-day traditions; "
                  "this claim does not resolve it."),
    "challenger": "present-day traditions on both sides (CT class)",
    "sources": [{"source_id": "srcIJC29"}]},
   {"challenge": ("Strand B's own counter, contemporaneous and in "
                  "canon form: rank follows the throne (Canon 3, "
                  "Canon 28) - Leo's written rejection is itself proof "
                  "the claim was contested AT THE TIME, not only by "
                  "later historians."),
    "challenger": "the Constantinopolitan see (ijcclaim002's voice)",
    "sources": [{"source_id": "srcIJC10"}, {"source_id": "srcIJC11"}]}],
  "concedes": ("The contested decretal block under Damasus's name is "
               "not ours to lean on (Registry row 15, dubium - the "
               "chunk's own Author-Gravity note); and the argument did "
               "not close inside our own window: Chalcedon ended with "
               "the two claims standing against each other in writing, "
               "and what became of them afterward is not this world's "
               "own record to tell."),
  "pressure_response": ("Intensified across the whole span: Rome's own "
                        "declining political centrality (2A-2) pushed "
                        "the claim FROM imperial-adjacency TOWARD "
                        "apostolic inheritance - the claim's ground "
                        "hardened precisely as the city's worldly rank "
                        "fell (Doc_04 C1's forces notation; force "
                        "1A-1's layer4)."),
  "divergence_partners": [
   {"world_id": WID, "partner_claim_id": "ijcclaim002",
    "note": ("THE IN-WORLD PARTNER PAIR (fleet first): the world's "
             "central contest carried as two strand-voiced claims, "
             "each the other's nearest rival - never flattened into "
             "one 'we'.")},
   {"world_id": "post-apostolic-house-church",
    "partner_claim_id": "pahcclaim003",
    "note": ("The where-authority-lives class, now FOUR-membered: "
             "PAHC argues the office into existence; this world "
             "claims the office settled and inherited. The "
             "ending-not-read-back discipline runs BOTH ways at a "
             "shared table: their argument must not borrow our "
             "settledness, and our settledness must not be read back "
             "as having been obvious in their rooms.")},
   {"world_id": "hieronymian-ascetic-literary",
    "partner_claim_id": "halclaim003",
    "note": ("Office vs earned trust: the Hieronymian household's "
             "authority lived in tested learning and funded trust, "
             "never a seat - the same era, the same city part of the "
             "time, a different ground entirely.")}],
  "sources": [{"source_id": "srcIJC04"}, {"source_id": "srcIJC12"},
              {"source_id": "srcIJC13"}, {"source_id": "srcIJC14"}],
  "term": "ijclex001"},
 {"id": "ijcclaim002",
  "claim": ("A see's rank follows the throne it stands beside: "
            "Constantinople is second only because it is where the "
            "emperor now sits - New Rome beside old Rome, and that is "
            "reason enough. The empire's own defense of orthodoxy is "
            "itself a religious fact, not a political convenience, and "
            "nearness to where that defense is conducted is honest "
            "ground for honor."),
  "held_against": [
   {"challenge": ("The CT contest (ijclex002's parking, unparked): "
                  "whether Canon 3/Canon 28's 'New Rome' reasoning "
                  "describes an accepted fact or asserts a novel "
                  "juridical claim dressed as description is itself "
                  "contested - Leo's rejection is direct evidence of "
                  "contemporaneous contest."),
    "challenger": "the Roman see (ijcclaim001's voice) + Leo in writing",
    "sources": [{"source_id": "srcIJC13"}]}],
  "concedes": ("Our own self-understanding survives primarily in "
               "conciliar acts, not in an individual advocate's own "
               "extended writing - the record's own asymmetry with the "
               "rival claim (the chunk's own contrast; the S2.1b "
               "Dagron gap rides here). And the canon we cite was "
               "rejected, in writing, by the see it ranked second - "
               "received unevenly, not everywhere."),
  "pressure_response": ("Rose with the city: the claim's strength "
                        "tracks Constantinople's own political rank "
                        "across the window (Doc_01 SS2) - made in "
                        "canon form at 381, remade sharper at 451, "
                        "answered in writing both times."),
  "divergence_partners": [
   {"world_id": WID, "partner_claim_id": "ijcclaim001",
    "note": "The in-world partner pair's other half."}],
  "sources": [{"source_id": "srcIJC10"}, {"source_id": "srcIJC11"}],
  "term": "ijclex002"},
 {"id": "ijcclaim003",
  "claim": ("The emperor's favor bought the church standing, buildings, "
            "and an arena - and it could not buy the altar: what "
            "belongs to God is not the emperor's to command, because "
            "the emperor stands within the Church, not above it. The "
            "alliance is real, and it has limits the alliance itself "
            "cannot set."),
  "held_against": [
   {"challenge": ("The Homoian decades are the standing counter- "
                  "evidence: under Constantius II and Valens the "
                  "imperial church ITSELF held the confession later "
                  "condemned - the alliance's limits held by Ambrose "
                  "in 386 were NOT held everywhere or always; for "
                  "real stretches imperial command DID set doctrine's "
                  "public terms."),
    "challenger": "this world's own record (the homoios honesty)",
    "sources": [{"source_id": "srcIJC23"}, {"source_id": "srcIJC33"}]}],
  "concedes": ("Our founding accounts of the alliance itself diverge "
               "in their specifics (Eusebius's oath-reported vision; "
               "Lactantius's earlier dream) and we hold the divergence "
               "open rather than harmonizing it - the founding moment "
               "is genuinely unsettled at exactly the level of detail "
               "a harmonized memory would have smoothed (ijcstory002's "
               "own FEC). And Strand C's limit-claim did not persist "
               "as an independent stream to our close (Doc_01 SS4)."),
  "pressure_response": ("The alliance's meaning MIGRATED under the "
                        "West's collapse (force 2A-2 reshaping 1A-1): "
                        "an alliance with an emperor decreasingly "
                        "present in Rome pushed Strand A toward "
                        "grounds no throne could move."),
  "divergence_partners": [
   {"world_id": "post-apostolic-house-church",
    "partner_claim_id": "pahcclaim001",
    "note": ("Before and after the sword: PAHC's unity was proved by "
             "letters under threat of a name and an accusation; this "
             "world's church stands beside the throne that once "
             "hunted it - the two worlds bracket the alliance the "
             "way HAL/PAHC bracket the office.")}],
  "sources": [{"source_id": "srcIJC01"}, {"source_id": "srcIJC03"},
              {"source_id": "srcIJC07"}, {"source_id": "srcIJC16"}],
  "term": "ijclex005"},
 {"id": "ijcclaim004",
  "claim": ("We hold the Son to be of one and the same being as the "
            "Father - and we will not pretend the word came easily: "
            "the confession we now defend was resisted, hedged at the "
            "moment of subscription, and for real stretches set aside "
            "by imperial command, within living memory of men who "
            "sat in our own councils."),
  "held_against": [
   {"challenge": ("The CT contest (ijclex006's parking, unparked): "
                  "Eusebius's own hedged subscription is direct "
                  "evidence of genuine, contemporaneous contest over "
                  "what the word actually committed a subscriber to - "
                  "not only later disagreement about an originally "
                  "settled meaning."),
    "challenger": "Eusebius's own subscription letter (the hedge)",
    "sources": [{"source_id": "srcIJC01"}, {"source_id": "srcIJC09"}]}],
  "concedes": ("Whether the word's eventual victory owed more to "
               "doctrinal necessity or to imperial enforcement is a "
               "contest between present traditions our record does "
               "not settle (the CT's own scope); what we can say is "
               "only what our own window shows - decades of genuine "
               "contest, ended inside our window by law as much as "
               "by argument."),
  "pressure_response": ("Enforcement inverted twice within the window "
                        "(Nicaea -> the Homoian establishment -> "
                        "Thessalonica 380): the confession's public "
                        "standing tracked imperial policy oscillation "
                        "(force 2A-1) more closely than our own "
                        "telling likes to admit."),
  "divergence_partners": [
   {"world_id": "alexandria-catechetical",
    "partner_claim_id": "alexclaim003",
    "note": ("The fleet's SECOND same-doctrine-different-carriage "
             "pair (the halclaim004<->alexclaim005 class): Alexandria "
             "confesses homoousios SIMPLY, as the school's settled "
             "inheritance; this world carries the same word with its "
             "decades of resistance, hedged subscriptions, and "
             "imperial reversals showing. Same confession, opposite "
             "textures - a table holding both must let each world's "
             "carriage stand.")}],
  "sources": [{"source_id": "srcIJC09"}, {"source_id": "srcIJC12"},
              {"source_id": "srcIJC33"}],
  "term": "ijclex006"},
 {"id": "ijcclaim005",
  "claim": ("Among us a teaching can be placed outside the law itself, "
            "not only outside the church's own fellowship - haeresis "
            "is a juridical exclusion as much as a theological one, "
            "and the two kinds of exclusion are simultaneous and "
            "mutually constituting, not sequential."),
  "held_against": [
   {"challenge": ("The CT contest (ijclex008's parking, unparked): "
                  "whether law-backed doctrinal exclusion was the "
                  "faith's corruption by power or its responsible "
                  "consolidation is a live contest between present "
                  "traditions; this claim does not resolve it."),
    "challenger": "present-day traditions on both sides (CT class)",
    "sources": [{"source_id": "srcIJC16"}]},
   {"challenge": ("The historical-scope contest (the chunk's own "
                  "second CT layer): whether the category was settled "
                  "from Nicaea onward or became so only gradually, "
                  "alongside and partly through the Theodosian Code's "
                  "own legal innovations, is contested in the modern "
                  "scholarship this record draws on."),
    "challenger": "the modern scholarship (rows 33-34's own debates)",
    "sources": [{"source_id": "srcIJC33"}]}],
  "concedes": ("The machinery's own history keeps us honest: the same "
               "juridical instruments that name and exclude enforced, "
               "at another point in our own record, the very teaching "
               "later so named (the homoios decades) - we cannot "
               "present the category as if it had only ever pointed "
               "one direction."),
  "pressure_response": ("Sharpened by establishment: before "
                        "Thessalonica (380) exclusion was "
                        "ecclesial; after it, legal - the category's "
                        "force grew with the alliance itself (G3's "
                        "own divergence note carried: mechanism "
                        "Documented, the Homoian decades' specific "
                        "content Widely Accepted only)."),
  "divergence_partners": [
   {"world_id": "post-apostolic-house-church",
    "partner_claim_id": "pahcclaim002",
    "note": ("The rival table before and after the law: PAHC refuses "
             "a rival's table as worship-and-belonging with NO law "
             "behind it and no certainty of closure; this world's "
             "refusal carries a legal code. The pair teaches what "
             "establishment changes - and what it does not (the "
             "refusal's religious core precedes the law).")}],
  "sources": [{"source_id": "srcIJC16"}, {"source_id": "srcIJC09"}],
  "term": "ijclex008"},
]


def main():
    for c in CLAIMS:
        term = c.pop("term")
        rec = {"id": c["id"], "world_id": WID,
               "record_type": "contested_claim", "schema_version": 1,
               "jobs": [1, 2, 4], "register": "emic",
               "review_state": "draft", **{k: v for k, v in c.items()
                                           if k != "id"}}
        emit_record(rec, ("Authored at the S6.2/IJC S2.6-equivalent "
                          "(2026-07-31); absorbs the CT Contest Type "
                          f"parking of {term} where one exists; "
                          "reasoning in wrs/migrate/s62_ijc_s26.py."),
                    OUT / "contested_claim" / f"{c['id']}.md")
        # wire the term's contested_claim_ids
        tp = OUT / "term" / f"{term}.md"
        txt = tp.read_text(encoding="utf-8")
        front, _, body = txt[4:].partition("\n---\n")
        f = yaml.safe_load(front)
        ids = set(f.get("contested_claim_ids") or [])
        ids.add(c["id"])
        f["contested_claim_ids"] = sorted(ids)
        fy = yaml.safe_dump(f, sort_keys=False, allow_unicode=True,
                            width=100)
        tp.write_text(f"---\n{fy}---\n{body}", encoding="utf-8",
                      newline="\n")
    print("5 contested claims + term wiring (in-world partner pair "
          "ijcclaim001<->002, a fleet first; cross-world partners: "
          "pahcclaim003+halclaim003, alexclaim003, pahcclaim001, "
          "pahcclaim002)")


if __name__ == "__main__":
    main()
