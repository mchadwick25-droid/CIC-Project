---
id: gallic.quote.cassian-clothes-kept-until-excellence-of-progress
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Documented as Cassian's own text (Institutes IV.6, read at its locus for this record) - his own
    explanation of why a novice's worldly clothes are kept rather than disposed of.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "IV.6 (npnf211 div iv.iii.iv.vi, file lines 18678-18682): the steward keeping a novice's
    worldly clothes until his progress is proven"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what happens to a novice's own clothes when he joins the monastery"
  - "participant wants Cassian's own reason the clothes are kept, not disposed of at once"
  prefer_instead:
  - "participant wants the idiom of dress read as armour instead - retrieve gallic.quote.institutes-opening-soldier-of-christ"
text: >-
  But those clothes, which he laid aside, are consigned to the care of
  the steward and kept until by different sorts of temptations and
  trials they can recognize the excellence of his progress and life
  and endurance.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  Cassian's own chapter title states the point directly: this explains why the clothes are kept at
  all, not thrown away or given to the poor immediately. The keeping is provisional - the chapter
  goes on to say the clothes are given away once the community judges the novice's progress genuine.
modern_rendering: >-
  But the clothes he took off are handed over to the care of the steward. They are kept until the
  excellence of his progress, his life and his endurance can be recognized through different kinds
  of temptations and trials.
relations:
- type: associated-with
  target: gallic.force.army-and-rank-before
use_note:
  means: "Cassian explains in Institutes IV.6 that a novice's worldly clothes are kept by the steward until trials have proven his progress."
  not_for:
    - "a claim that the clothes are kept permanently, when the chapter says they are given away once progress is proven"
    - "Gallic practice, when Cassian describes the Egyptian coenobia"
  years: {from: 415, to: 426}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"excellence of his progress"` returns line 18681; read with `sed -n '18674,18684p'`, inside `<div4
title="Chapter VI. The reason why the clothes of the renunciants with which they joined the
monastery are preserved by the steward." ... id="iv.iii.iv.vi">`. The quoted span is one complete
sentence, "But those clothes..." through "...life and endurance.", ending at its own period.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
