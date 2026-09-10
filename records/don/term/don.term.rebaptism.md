---
id: don.term.rebaptism
world_id: don
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F4-I
relations:
- type: associated-with
  target: don.term.church-ecclesia
- type: associated-with
  target: don.term.purity
- type: associated-with
  target: don.term.reception-without-reordination
- type: associated-with
  target: don.term.traditor-traditio
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: don.source.augustine-on-baptism-against-donatists
  locus: On Baptism, Against the Donatists, quoting Petilian's own argument for the practice
  license: public-domain
- source_id: don.source.augustine-answer-to-letters-of-petilian
  locus: Answer to the Letters of Petilian, a clause-by-clause reply to Petilian's own rebaptism argument
  license: public-domain
- source_id: don.source.petilian-of-constantina-letters-quoted
  locus: '''What we look for is the conscience of the giver, to cleanse that of the recipient'' -- independently
    verified against npnf104_augustine-anti-manichaean-anti-donatist.xml'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant uses "rebaptism," "baptized again," or asks why anyone would need to be baptized twice
  - participant asks what we and our rival church actually fought over
  - conversation reaches the question of what makes a baptism real or how someone joins our church from
    the other one
  do_not_retrieve_when:
  - participant is asking about baptism as a general Christian rite without reference to the boundary-crossing
    question specifically
  - the World Capsule Core has already surfaced rebaptism as the enacted rite in the current turn
plain_meaning: We do not think of this as baptizing someone twice. From where we stand, nothing happened
  the first time, because it came from a hand we do not trust to give it. When someone comes to us from
  the rival church, we are not repeating a sacrament -- we are giving the first true one.
world_word: rebaptizare
distortion_risk: high
false_friend:
- a repeated sacrament performed out of excessive ritual scruple
- an unnecessary formality, since most traditions hold baptism happens only once
senses:
  informational: 'This is the same logic that makes traditor our founding wound: if a minister''s hand
    cannot be trusted, nothing that flows through it can be trusted either, and baptism is the sharpest
    place that trust holds or fails, because baptism is what makes a person part of the church at all.
    Rebaptism is not a private opinion held by a few among us; it is the single most concretely enacted,
    individually experienced act of belonging we have. Every rebaptism performed is our own doctrine,
    lived rather than merely stated.'
  evidential: Augustine's On Baptism, Against the Donatists and his Answer to the Letters of Petilian
    both devote substantial argument to this practice, quoting Petilian's own words clause by clause --
    'What we look for is the conscience of the giver, to cleanse that of the recipient,' independently
    verified against the vendored text. Augustine dominates the surviving evidence for this practice's
    own specific argumentative texture, but the bare fact of the practice, and Petilian's own argument
    for it, are attested directly in Augustine's own primary text, not merely summarized by him.
  personal: 'We know what rebaptizing a Catholic costs us in the empire''s eyes: successive imperial edicts
    name this practice specifically, because to the state that favors our rival, it is the plainest sign
    we do not accept its settlement. We accept that cost, because to stop would be to concede the other
    church''s baptisms were real after all -- and if theirs were real, ours were never necessary.'
  translational: '''Why would you baptize someone twice?'' By most later Christian tradition''s own reckoning,
    baptism happens once -- so from outside, this can look like an excessive ritual scruple. From inside,
    it is not a repetition at all: it is the correction of an act that, whatever it looked like, conferred
    nothing the first time.'
quick_meaning: Baptism given outside our one true church is no baptism at all. So when someone comes to
  us from the rival communion, we are not repeating a sacrament -- we are giving the first one.
---
Re-derived from Doc_06 SS1 (donlex002, Tier 1, confirmed) and Lexicon-Chunks/donlex002_rebaptism.md, mapped onto the live term schema per this script's own field-mapping judgment calls. Petilian's own quoted proposition is independently verified against npnf104_augustine-anti-manichaean-anti-donatist.xml, per the chunk's own Key Sources note. Relations: Traditor/Traditio is Mutual per the chunk's own Reciprocity Note; Reception without Reordination and Purity close that same note's "not yet built as chunks" gap. Church/Ecclesia was the chunk's own flagged ONE-DIRECTIONAL link (Doc_06 SS4/SS5 name it explicitly as remaining work) -- closed this pass by adding the reciprocal edge on don.term.church-ecclesia's own record, a deliberate, disclosed content addition (see script docstring, RECIPROCITY CLOSURE), not a silent edit to either chunk's own authored text.
