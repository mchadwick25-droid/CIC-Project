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
  test_1: {verdict: pass, note: "fixture"}
  test_2: {verdict: pass}
  test_3: {verdict: pass}
  test_4: {verdict: partial}
  test_5: {verdict: pass}
  test_6: {verdict: pass}
classification: Primary
confidence_crosscheck: "Cross-checked against fixture confidence rows."
interaction:
  - {type: reinforcing, target_id: fixgrav002, note: "fixture edge", changes_to: competing, at: "c. 350"}
---
