---
id: fixgrav001
world_id: fixture-world
record_type: gravity
schema_version: 1
jobs: [5]
register: etic
review_state: draft
name: "Fixture Gravity"
six_tests:
  repetition: {verdict: pass, note: "fixture"}
  dependency: {verdict: pass}
  formation: {verdict: pass}
  explanatory: {verdict: partial}
  persistence: {verdict: pass}
  interaction: {verdict: pass}
classification: Primary
confidence_crosscheck: "Cross-checked against fixture confidence rows."
interaction:
  - {type: reinforcing, target_id: fixgrav002, note: "fixture edge", changes_to: competing, at: "c. 350"}
---
