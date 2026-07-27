---
id: fixlex001
world_id: fixture-world
record_type: term
schema_version: 1
jobs: [4, 6, 7]
register: emic
confidence: {citation_specificity: B, verification_state: verified-via-authority, evidentiary_weight: corroborating, formation_confidence: Widely Accepted}
sources:
  - {source_id: fixsrc001, locus: "Dem. 6.1", licensed_for: "voice", author_gravity_note: "fixture note"}
eviction_priority: 3
cache_stability: static
grounding_criterion: high
review_state: draft
term: "fixterm"
aliases: ["fixture term"]
original_script: "(fixture script)"
period_sense: "What the word meant inside the fixture world."
prior_sense: "none-attested"
modern_sense: "What a modern participant means by it."
conceptual_distance_note: "Sharp then-vs-now gap; high-criterion by rule."
semantic_domain: "fixture-domain"
field_relations:
  - {type: presupposes, target_id: fixlex002, note: "fixture edge"}
quick_meaning: "One plain-register sentence for reachability."
voice_surface: "How the fixture representative may actually say it."
world_meaning: "The full scholarly treatment, Levels 2/3 only."
distortion_risk: "Modern hearing flattens it."
modern_hearing: "A modern ear hears a different thing."
retrieval:
  tier: 1
  retrieve_when: ["participant asks about the fixture term"]
  do_not_retrieve_when:
    - {condition_type: sense-disambiguation, text: "participant means the unrelated modern sense"}
  force_llm_vote: true
contested_claim_ids: [fixcc001]
---
