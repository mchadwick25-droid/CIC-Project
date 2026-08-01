---
id: ijclex010
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
term: Nea Rhōmē
aliases:
- New Rome
- Constantinople as New Rome
- Nea Rhome
quick_meaning: We are New Rome — not old Rome's rival, but old Rome's own successor in the place where
  the empire itself now actually governs.
world_meaning: 'Written from Strand B''s own voice. Constantine did not build a city and merely give it
  a grand name. He gave it the name of the city whose place it was taking as the seat of empire, and we
  have held that name as a claim, not a decoration — this is where the emperor now resides, where the
  councils now gather, where the church''s own defense is now actually conducted. Old Rome remains old
  Rome, and we do not deny her her own honor. But honor that follows an apostle''s grave is not the only
  honor a see may rightly claim, and ours follows the throne itself.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: *Nea Rhōmē* is the specific geographic-political fact *presbeia*''s
  own rank-claim rests on — narrower than *presbeia* itself, which it supports rather than stands independently
  of.'
distortion_risk: in this world's own record, the name functions as the stated premise of a real, contested
  juridical claim (Canon 3, Canon 28), not as decoration.
retrieval:
  tier: 2
  retrieve_when:
  - participant asks specifically why Constantinople calls itself "New Rome," or asks about the city's
    own founding as a capital.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the question concerns the rank-claim itself rather than the city's own designation (retrieve
      presbeia instead).
  force_llm_vote: false
sources:
- source_id: srcIJC10
  author_gravity_note: Canon 3 of Constantinople (381); Canon 28 of Chalcedon (451).
modern_hearing: a modern participant may hear "New Rome" as mere honorific flattery, a city naming itself
  grandly with no operative claim behind it.
original_script: Νέα Ῥώμη
semantic_domain: political-geographic premise - the new capital
modern_sense: '''Byzantium/Istanbul trivia'' - a renaming; the juridical work the name does invisible
  (chunk Modern Hearing).'
period_sense: '''We are New Rome - not old Rome''s rival, but old Rome''s own successor in the place where
  the empire itself now actually governs'' - the stated premise of a real, contested juridical claim (Canon
  3, Canon 28), not decoration.'
prior_sense: Constantinople dedicated 330 as Constantine's capital; the name's official standing vs honorific
  currency is a builder note, UNVERIFIED.
grounding_criterion: high
conceptual_distance_note: 'GROUNDING (the enum''s free-text companion, carried here): Canon 3 (row 10)
  and Canon 28 (row 11) - the claim''s own two canonical instances. | DISTANCE: Narrower than presbeia,
  which it supports rather than stands independently of (the EF''s own scoping).'
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
voice_surface: '''We are New Rome - not old Rome''s rival, but old Rome''s own successor in the place
  where the empire itself now actually governs.'''
field_relations:
- type: presupposed-by
  target_id: ijclex002
  note: 'Chunk Ecological Function (verbatim, absorbed per FLAG-002): *Nea Rhōmē* is the specific geographic-political
    fact *presbeia*''s own rank-claim rests on — narrower than *presbeia* itself, which it supports rather
    than stands independently of. Inverse pair with presbeia''s presupposes.'
- type: tension-with
  target_id: ijclex001
  note: 'Symmetric mirror: the geographic ground of the rank contest.'
contested_claim_ids: []
---
Migrated at the S6.2/IJC S2.2-equivalent (2026-07-31) from `data/imperial_juridical_world/lexicon_chunks/ijclex010_nea_rhome.md` (mechanical split; mapping and alias authoring tables in `wrs/migrate/s62_ijc_s22.py` - the FLAG-035 corrections and the one Rule-A birth drop declared there; the third world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Final Assembly Instruction - parked at the S2.2-equivalent; typed home per the splitter docstring] Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0. No brackets or builder notes remain. CT tag not applied at the entry level — the underlying "New Rome" reasoning's contested status is carried by the linked *presbeia* entry, which carries the CT tag directly.
