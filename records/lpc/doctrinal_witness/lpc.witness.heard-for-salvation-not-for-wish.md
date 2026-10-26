---
id: lpc.witness.heard-for-salvation-not-for-wish
world_id: latin-pastoral-congregational-christianity
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-P
use_note:
  means: "From Paul's thorn Augustine taught that the saints are always heard for their salvation, even when not heard as they wished."
  not_for:
    - "a claim that God removed Paul's thorn"
    - "a claim that Augustine promised any wish would be answered"
  years: {from: 391, to: 430}
  status: reviewed
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: lpc.source.augustine-tractates-on-john-and-related-exegesis
  locus: Ten Homilies on the First Epistle of John, Homily VI, SS6-7, on Paul's own thorn in the flesh
    and being "heard, then, for salvation" -- verified directly against cic/texts/npnf107_augustine-homilies-john-soliloquies.xml,
    lines 15210-15225
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks what to do with prayer that goes unanswered
  - conversation reaches F4-P and needs the real teaching that answers the unanswered-prayer sub-question
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: lpc.witness.restless-heart-and-the-unrepentant-enemy
positions:
- Augustine taught directly on prayer that goes unanswered, from the apostle Paul's own words. Paul asked God three
  times to take away a thorn in his flesh, an affliction he named as a messenger of Satan sent to buffet
  him. God did not take it away.
tensions:
- 'God answered, "My grace is sufficient for thee: for strength is made perfect in weakness." Our bishop''s
  conclusion was this: Paul was heard for salvation, though he was not heard according to his wish. He
  made it a rule for the saints, not for Paul alone. They are always heard in what concerns their salvation.'
claim_guards: []
text: 'Augustine taught directly on prayer that goes unanswered, from the apostle Paul''s own words. Paul
  asked God three times to take away a thorn in his flesh. He named it a messenger of Satan sent to buffet
  him. God did not take it away. He answered instead, "My grace is sufficient for thee: for strength is
  made perfect in weakness." Paul was heard for salvation, Augustine taught, even though he was not heard
  according to his wish. He made this a rule for the saints, not for Paul alone. They are always heard
  in what concerns their salvation, even when they are not heard as they wished.'
---
Grounded directly in Augustine, Ten Homilies on the First Epistle of John, Homily VI, SS6-7 -- verified against the vendored XML at the line numbers above (npnf107_augustine-homilies-john-soliloquies.xml is assigned to lpc via lpc.source.augustine-tractates-on-john-and-related-exegesis). Uses Paul's own thorn-in-the-flesh episode as its worked example. A second, independent locus (the Exposition on Psalm 86, npnf108) makes the same point at greater length and is not built as its own record here, since one clean, directly-quoted locus already answers the cell. Together with lpc.witness.restless-heart-and-the-unrepentant-enemy, this fully answers F4-P.
