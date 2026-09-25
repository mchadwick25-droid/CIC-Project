---
id: gallic.quote.martin-and-the-unattested-tomb
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Sulpitius's own narration of the episode (Vita ch. XI); the reason given for
    Martin's caution is reported by Sulpitius as Martin's own stated words ("he said"), but the
    surrounding narration is Sulpitius's, not a direct quotation of Martin throughout.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. XI (npnf211 div ii.ii.xii, file lines 1176-1183): Martin's caution before an unattested martyr's tomb, before he tests it"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why Martin refused to venerate a tomb others already treated as a martyr's"
  - "participant asks how Martin tested a claim against tradition before acting on it"
  prefer_instead:
  - "participant asks what happened after Martin went to the tomb - this record carries only his reasoning beforehand, not the test itself"
text: >-
  He did so, he said, because he had great scruples on these points,
  inasmuch as no steady tradition respecting them had come down from
  antiquity. Having, therefore, for a time kept away from the place, by
  no means wishing to lessen the religious veneration with which it was
  regarded, because he was as yet uncertain, but, at the same time not
  lending his authority to the opinion of the multitude, lest a mere
  superstition should obtain a firmer footing, he one day went out to
  the place, taking a few brethren with him as companions.
speaker_or_author: Sulpitius Severus, narrating Martin's reason
license: verbatim
modern_lens_note: >-
  This is the Tours node's one episode carrying this gravity, against the south's much larger cluster
  of statements from Cassian and Vincent. Martin does not dismiss the tomb outright, and he does not
  simply defer to the crowd's devotion either - he holds off until he can test the claim for himself,
  because no verified tradition had come down about it. The caution and the eventual test (recounted
  later in the same chapter) are of a piece: tradition, not popular opinion, is what would have
  settled the question for him.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.gravity.received-not-invented
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "no
steady tradition"` returns one hit, line 1177, and `grep -n "opinion of the multitude"` one hit, line
1181, both inside `<div3 title="Chapter XI. Martin demolishes an Altar consecrated to a Robber." ...
id="ii.ii.xii">`. The two flagged fragments sit in a single continuous passage, lines 1176-1183: "He
did so, he said, because he had great scruples on these points, inasmuch as no steady tradition
respecting them had come down from antiquity. Having, therefore, for a time kept away from the place,
by no means wishing to lessen the religious veneration with which it was regarded, because he was as
yet uncertain, but, at the same time not lending his authority to the opinion of the multitude, lest a
mere superstition should obtain a firmer footing, he one day went out to the place, taking a few
brethren with him as companions." Both are carried together as one record rather than split, matching
their place in a single continuous stretch of Sulpitius's narration.

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
