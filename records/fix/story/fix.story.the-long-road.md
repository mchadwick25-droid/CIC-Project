---
id: fix.story.the-long-road
world_id: fixture-synthetic
record_type: story
schema_version: 2
status: ready
register: emic
canon_cells: [F5-P]
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
  - {source_id: fix.source.witness-scroll, locus: "3.2", license: public-domain}
retrieval:
  tier: 1
  retrieve_when: ["participant asks what belonging cost someone"]
  do_not_retrieve_when: []
narrative_tier: 2
narrative_tier_justification: "Named in the primary fixture source with enough concrete detail to tell, though not central to it (tier 1 would be a source-anchoring story; this is a supporting one)."
tellable_as: "A family in Testland loses standing at the market after the youngest son is seen at church. They stay together anyway."
text: >
  When the youngest of that house was seen going to the gathering on the first
  day, the market stalls that had traded with them for years began to trade
  elsewhere. The family did not leave the gathering. They ate less that winter,
  and stayed.
absent_detail: "The scroll does not name the family, or say how long the cost lasted."
modern_contrast: >
  A modern reader may hear the market's withdrawal of trade as a boycott or a
  form of social cancellation. This world's own record frames it differently:
  ordinary commerce simply followed ordinary suspicion of the gathering, with
  no organized campaign behind it - what the family paid was the market's plain
  reaction, not a deliberate punishment.
---
Clean, complete story record: narrative_tier in range (1-4) with a real
justification, tellable_as, text, and an absent_detail note. The narratability
DEFECT mutates a copy's narrative_tier to 5 (out of range) and/or drops the
justification.
