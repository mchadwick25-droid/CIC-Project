---
id: fix.contested.founding-date
world_id: fixture-synthetic
record_type: contested_claim
schema_version: 2
status: ready
register: etic
canon_cells: [C-I]
confidence:
  citation_specificity: C
  verification_state: named-not-rechecked
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: "The two fixture sources disagree on when the Testland gathering began; neither is verified-direct on this specific point, so this record stays etic and contested rather than resolved."
sources:
  - {source_id: fix.source.witness-scroll, locus: "1.1"}
  - {source_id: fix.source.secondary-summary, locus: "1.1"}
claim: "The Testland gathering began in the first year of the synthetic window (year 100)."
held_against: ["fix.source.secondary-summary places it a full season later than fix.source.witness-scroll does"]
concedes: "The exact founding month is not recoverable from either fixture source."
divergence_partners: [fix.source.witness-scroll, fix.source.secondary-summary]
use_note:
  means: "Testland's own record dates the gathering's start to year 100, and the claim is held as disputed."
  not_for:
    - "a settled founding date"
    - "a date for any real church"
  years: {from: 100, to: 100}
  status: provisional
---
Fixture contested_claim record - the one type whose field shape Artifact-1 §4
does specify explicitly (claim, held_against[], concedes, divergence_partners[]).
