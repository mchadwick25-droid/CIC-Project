---
id: ijclex006
world_id: imperial-juridical-christianity
record_type: term
schema_version: 1
jobs:
- 1
- 2
- 4
- 6
register: emic
review_state: draft
cache_stability: static
term: homoousios
aliases:
- of one substance
- of one being with the Father
- consubstantial
quick_meaning: 'The Son is of one and the same being as the Father. Not merely like him. Sharing, undivided, the very being that makes the Father God.'
world_meaning: 'This is the word our councils settled on when a plainer word — "like" — was found to leave
  too much unclosed. We do not hold to it lightly or as a mere formula recited without weight; even Eusebius
  himself, present when it was first confessed, wrote home to his own church explaining the caution with
  which he received it. That a man so close to the founding of our own alliance could hold this word at
  arm''s length, even while signing it, tells us this was never an easy or obvious settlement — it was
  won, argued, and in places imposed, not simply always known.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: This term is the doctrinal content our councils and our Tomes
  exist to defend and assert — it does not organize our own institutional life independently, the way
  *primatus* or *communio* does, but it is what those institutions repeatedly act to protect.'
distortion_risk: this world's own record shows the word itself remaining genuinely contested — held, resisted,
  and at times set aside by imperial command — for decades after it was first confessed.
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about the Nicene Creed's own central claim
  - conversation touches Leo's Tome or the councils' own doctrinal content directly.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the conversation is really about homoios or the Homoian imperial establishment specifically
      (retrieve that chunk instead).
  force_llm_vote: false
sources:
- source_id: srcIJC12
  author_gravity_note: The Acts and Canons of Nicaea (325); Leo I's Tome to Flavian, which assumes and
    builds on this settlement.
modern_hearing: a modern participant may assume this word was uncontested once Nicaea spoke it, a settled
  formula from 325 onward.
original_script: ὁμοούσιος
semantic_domain: doctrinal formula - Trinitarian confession
modern_sense: '''Consubstantial'' as a settled creedal word whose acceptance was immediate - the decades
  of resistance invisible (chunk World Hearing''s own counterpoint).'
period_sense: Of one and the same being as the Father - not merely like him; the word itself remaining
  genuinely contested, held, resisted, at times set aside by imperial command, for decades after first
  confessed.
prior_sense: Greek homoousios - 'of the same substance/being'; pre-Nicene history (Paul of Samosata's
  condemnation context) is a builder note, UNVERIFIED.
grounding_criterion: high
conceptual_distance_note: 'GROUNDING (the enum''s free-text companion, carried here): Nicaea''s own creed
  (row 9) + Leo''s Tome assuming and building on the settlement (row 12). | DISTANCE: The CT contest:
  whether the word''s eventual victory was doctrinal necessity or imperial enforcement is contested between
  present traditions; not resolved here.'
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Contested
voice_surface: '''We hold the Son to be of one and the same being as the Father - not merely like him,
  but sharing, undivided, the very being that makes the Father God.'''
field_relations:
- type: tension-with
  target_id: ijclex003
  note: 'Chunk Ecological Function (verbatim, absorbed per FLAG-002): This term is the doctrinal content
    our councils and our Tomes exist to defend and assert — it does not organize our own institutional
    life independently, the way *primatus* or *communio* does, but it is what those institutions repeatedly
    act to protect. Symmetric mirror of the formula rivalry.'
- type: associated-with
  target_id: ijclex001
  note: 'Symmetric mirror: the content the see''s instruments defend.'
- type: associated-with
  target_id: ijclex002
  note: 'Symmetric mirror: the settlement both strands claim to guard.'
- type: presupposed-by
  target_id: ijclex009
  note: The Tome builds on this settlement (the EF's own 'what those institutions act to protect'); inverse
    pair with ijclex009's presupposes.
- type: presupposed-by
  target_id: ijclex013
  note: 'Added 2026-08-16 (T3 gospel-question follow-on): pro nobis states what the one who is of one
    being with the Father did; correctly saying what he accomplished depends on correctly saying who he
    is first. Inverse pair with ijclex013''s presupposes.'
contested_claim_ids:
- ijcclaim004
---
Migrated at the S6.2/IJC S2.2-equivalent (2026-07-31) from `data/imperial_juridical_world/lexicon_chunks/ijclex006_homoousios.md` (mechanical split; mapping and alias authoring tables in `wrs/migrate/s62_ijc_s22.py` - the FLAG-035 corrections and the one Rule-A birth drop declared there; the third world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[CT Contest Type - parked at the S2.2-equivalent; typed home per the splitter docstring] **Meaning:** Eusebius's own hedged subscription is direct evidence of genuine, contemporaneous contest over what this word actually committed a subscriber to — not only a matter of later disagreement about an originally settled meaning.

[Final Assembly Instruction - parked at the S2.2-equivalent; typed home per the splitter docstring] Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0. No brackets or builder notes remain; CT Contest Type completed per Doc_06 §3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
