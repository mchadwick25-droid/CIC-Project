---
id: ijclex007
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
term: concilium (synodos)
aliases:
- synod
- ecumenical council
quick_meaning: A council is where bishops gather, under imperial summons, to settle what the whole church
  must hold — and, in our own record, what a council settles does not always stay settled.
world_meaning: 'We do not resolve our own deepest disputes by one bishop''s word alone, however great
  his see. We gather — hundreds of us, summoned by the emperor''s own authority to travel, at real cost,
  to one place — and there we argue, and vote, and issue canons that bind. This is our own chief instrument
  for settling what must be settled at the level of the whole church rather than one see. And yet our
  own record does not let us pretend this instrument always works as it was meant to: the same council
  that settled Christ''s own nature at Chalcedon also produced a canon on Constantinople''s own rank that
  Rome would not receive, so that the very meeting meant to produce lasting unity produced, on that count,
  a lasting division instead.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: The council is the shared mechanism through which *primatus*,
  *presbeia*, and *haeresis* alike are asserted and contested — it does not organize the ecology independently
  so much as it is the arena in which the world''s own organizing claims are repeatedly brought to trial.'
distortion_risk: in this world's own record, a council's own vote does not settle a question merely by
  being taken — reception by the sees whose communion matters is a separate, sometimes withheld, act.
retrieval:
  tier: 2
  retrieve_when:
  - participant asks how doctrinal disputes were actually resolved, or asks about a specific council (Nicaea,
    Constantinople, Chalcedon).
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the question concerns one council's specific content rather than the mechanism of conciliar
      authority itself.
  force_llm_vote: false
sources:
- source_id: srcIJC09
  author_gravity_note: The Acts and Canons of Nicaea, Constantinople (381), and Chalcedon (451).
modern_hearing: a modern participant may assume a council functions like a modern legislative body, producing
  a clean majority outcome all parties then accept.
semantic_domain: juridical mechanism - conciliar process
modern_sense: '''Church council'' as a parliament whose vote settles matters - reception assumed automatic
  (chunk World Hearing''s counterpoint).'
period_sense: 'Where bishops gather under imperial summons to settle what the whole church must hold -
  and what a council settles does not always stay settled: reception by the sees whose communion matters
  is a separate, sometimes withheld, act.'
prior_sense: Latin concilium - any convened assembly, civic or sacred; a builder note, UNVERIFIED.
grounding_criterion: high
conceptual_distance_note: 'GROUNDING (the enum''s free-text companion, carried here): The three conciliar
  acts rows (9, 10, 11) - the world''s own initiating, middle, and closing councils. | DISTANCE: ''council''
  dropped at birth under Rule A - the surface rides the confirmed gloss ''a council (concilium)''.'
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
voice_surface: '''A council is where bishops gather, under imperial summons, to settle what the whole
  church must hold - and, in our own record, what a council settles does not always stay settled.'''
field_relations:
- type: tension-with
  target_id: ijclex001
  note: 'Chunk Ecological Function (verbatim, absorbed per FLAG-002): The council is the shared mechanism
    through which *primatus*, *presbeia*, and *haeresis* alike are asserted and contested — it does not
    organize the ecology independently so much as it is the arena in which the world''s own organizing
    claims are repeatedly brought to trial. Symmetric mirror: the letter-vs-council tension.'
- type: presupposed-by
  target_id: ijclex002
  note: 'Symmetric inverse: the presbeia claim exists in canon form - the council is its arena.'
- type: associated-with
  target_id: ijclex008
  note: Councils are where haeresis is named - the arena's exclusion verdicts; symmetric.
- type: tension-with
  target_id: ijclex009
  note: The Tome received AT a council yet claiming an authority not FROM the council - Canon 28's counter-claim
    is the same tension from the other side; symmetric.
contested_claim_ids: []
---
Migrated at the S6.2/IJC S2.2-equivalent (2026-07-31) from `data/imperial_juridical_world/lexicon_chunks/ijclex007_concilium.md` (mechanical split; mapping and alias authoring tables in `wrs/migrate/s62_ijc_s22.py` - the FLAG-035 corrections and the one Rule-A birth drop declared there; the third world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Final Assembly Instruction - parked at the S2.2-equivalent; typed home per the splitter docstring] Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0. No brackets or builder notes remain. CT tag not applied.
