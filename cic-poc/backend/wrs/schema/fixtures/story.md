---
id: fixstory001
world_id: fixture-world
record_type: story
schema_version: 1
jobs: [1, 3]
register: emic
review_state: draft
title: "The Fixture Story"
narrative_tier: {tier: 2, justification: "Attested in the fixture collection; incident-level detail contested."}
text: "The story itself, at full depth."
owner_figure_id: fixfig001
attested_occasion: "Elders visiting to test the fixture."
tellable_as: scene
voice_surface: "How the world tells it, when it tells it."
retrieval:
  tier: 2
  retrieve_when: ["participant asks about fixture humility"]
  do_not_retrieve_when: []
  force_llm_vote: false
sources:
  - {source_id: fixsrc001, locus: "Apoph. 1"}
---
