---
id: fixcc001
world_id: fixture-world
record_type: contested_claim
schema_version: 1
jobs: [8]
register: emic
review_state: draft
claim: "The fixture world holds X, in its own terms."
held_against:
  - challenge: "But surely not-X?"
    challenger: "The fixture opponents"
    sources: [{source_id: fixsrc001, locus: "Dem. 6.3"}]
concedes: "Our own record does not tell us Y."
pressure_response: "Argues from practice, then goes silent."
divergence_partners:
  - {world_id: other-fixture-world, note: "diverges on X per its own Doc_04"}
---
