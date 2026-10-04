---
id: gallic.quote.no-steady-tradition-from-antiquity
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as Sulpitius's own text (Vita ch. XI, read at its locus for this record) - his
    own report of Martin's stated reason for withholding belief, one named ancient witness rather
    than independent corroboration.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. XI (npnf211 div ii.ii.xii, file lines 1170-1178): Martin's own
    reason, as Sulpitius reports it, for questioning a local martyr cult"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks whether Martin himself applied a reception standard to local cult and memory"
  - "participant wants an episode from Tours applying the same logic the south states systematically"
  prefer_instead:
  - "participant wants the south's own systematic statement of the same standard - retrieve gallic.quote.antiquity-and-the-fathers-unanimous-decision"
text: >-
  He did so, he said, because he had great scruples on these points,
  inasmuch as no steady tradition respecting them had come down from
  antiquity.
speaker_or_author: "Sulpitius Severus, narrating, reporting Martin's own reason"
license: verbatim
modern_lens_note: >-
  Martin's own reason for hesitating over the tomb is not doubt about miracles or holiness in
  general - it is the specific absence of a steady tradition handed down from antiquity about who
  was buried there. The same reception standard the south states as a rule, Martin applies here to
  one local cult.
modern_rendering: >-
  He did this, he said, because he had serious doubts of conscience about these matters. He had
  these doubts because no steady tradition about them had come down from antiquity.
relations:
- type: associated-with
  target: gallic.force.legitimacy-by-reception
use_note:
  means: "Sulpitius reports Martin's stated reason for doubting a local martyr cult: no steady tradition about it had come down from antiquity."
  not_for:
    - "a general rejection of martyr cults or miracles"
    - "Vincent's formal test of antiquity and consent, which sits in gallic.quote.believed-everywhere-always-by-all"
    - "a separate witness from gallic.quote.martin-and-the-unattested-tomb, which opens with this same sentence and does not reach the tomb's test"
  years: {from: 397, to: 397}
  status: reviewed
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"no steady tradition respecting"` returns line 1177; read with `sed -n '1168,1178p'`, inside `<div3
title="Chapter XI. Martin demolishes an Altar consecrated to a Robber." ... id="ii.ii.xii">`. The
quoted span is one complete sentence, "He did so, he said..." through "...come down from
antiquity.", ending at its own period.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
