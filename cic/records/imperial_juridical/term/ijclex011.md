---
id: ijclex011
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
term: basilica (as contested institutional space)
aliases:
- church building
- basilica standoff
quick_meaning: 'Not only a building. It is the ground where the question of who commands the church''s own space, emperor or bishop, was actually fought out. That night, it was held.'
world_meaning: See Quick Meaning above; this term's own fuller treatment lives in the *Imperator intra
  Ecclesiam* entry, of which this is one physical, load-bearing detail.
distortion_risk: in this world's own 386 record specifically, the building itself is inseparable from
  the confrontation that made it consequential.
retrieval:
  tier: 3
  retrieve_when:
  - participant asks specifically about the physical building at the center of the 386 Milan standoff.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the participant's real question is about the standoff's own meaning or Ambrose's own formula
      (retrieve the Imperator entry instead).
  force_llm_vote: false
sources:
- source_id: srcIJC38
  author_gravity_note: 'No Key Sources by design (S2.1a): the basilica term''s evidence is the Milan basilica
    complex itself (registry row 38) plus the 386 standoff texts already carried by imperator-intra-ecclesiam''s
    own sources.'
- source_id: srcIJC37
  author_gravity_note: 'Old St. Peter''s (row 37): the Constantinian monumental expression the chunk''s
    World Meaning describes.'
modern_hearing: a modern participant may treat "basilica" as purely an architectural term.
semantic_domain: material culture - contested sacred space
modern_sense: '''Basilica'' as an architectural style term or any big church (chunk Modern Hearing).'
period_sense: Not only a building - the physical ground on which the question of who commands the church's
  own space, emperor or bishop, was actually fought and, that night in 386, held.
prior_sense: Roman civic basilica - the law-court/market hall form adapted for Christian assembly; a builder
  note, UNVERIFIED.
grounding_criterion: high
conceptual_distance_note: 'GROUNDING (the enum''s free-text companion, carried here): The Milan basilica
  complex itself (row 38) + Old St. Peter''s as the alliance''s monumental expression (row 37) - material
  rows; the standoff texts ride ijclex005''s sources (the S2.2 source-defaults declaration). | DISTANCE:
  No Key Sources section by design - material-culture evidence class (S2.1a).'
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
voice_surface: '''For us, a basilica is not only a building - it is the physical ground on which the question
  of who commands the church''s own space, emperor or bishop, was actually fought and, that night, held.'''
field_relations:
- type: associated-with
  target_id: ijclex005
  note: 'Symmetric mirror: the sermon and its ground (no chunk EF by design - S2.2 declaration).'
- type: associated-with
  target_id: ijclex004
  note: 'Symmetric mirror: communion-space against imperial demand.'
contested_claim_ids: []
chunk_slug: basilica
chunk_related_line: Imperator intra Ecclesiam, non supra Ecclesiam, communio
---
Migrated at the S6.2/IJC S2.2-equivalent (2026-07-31) from `data/imperial_juridical_world/lexicon_chunks/ijclex011_basilica.md` (mechanical split; mapping and alias authoring tables in `wrs/migrate/s62_ijc_s22.py` - the FLAG-035 corrections and the one Rule-A birth drop declared there; the third world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Final Assembly Instruction - parked at the S2.2-equivalent; typed home per the splitter docstring] Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0 (Tier 3: World Meaning brief, Ecological Function and Key Sources omitted per Template instruction). No brackets or builder notes remain. CT tag not applied.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 2 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
