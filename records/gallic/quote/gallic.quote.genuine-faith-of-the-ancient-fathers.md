---
id: gallic.quote.genuine-faith-of-the-ancient-fathers
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
  formation_confidence: Documented
  divergence_note: >-
    Documented as Cassian's own text (Institutes XII.19, read at its locus for this record) - his
    own name for the teaching just stated, tying humility toward God to what he claims is the
    fathers' own inherited faith.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes XII.19 (npnf211 div iv.iii.xii.xix, file lines 25392-25394): Cassian naming the
    humility-and-grace teaching as the ancient fathers' own genuine faith"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks how Cassian names his own grace teaching, in relation to the elders"
  - "participant asks what Cassian claims for the pedigree of this teaching"
  prefer_instead:
  - "participant wants the fuller statement of the teaching itself - retrieve gallic.quote.perfection-not-gained-without-grace"
text: >-
  This then is that humility towards God, this is that genuine faith of
  the ancient fathers which still remains intact among their
  successors.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  Cassian is not introducing a new idea here - he is naming one just stated as something old,
  claiming it as the fathers' own faith, still intact in the generation that received it from them.
  The claim to continuity is his own, made in his own words.
modern_rendering: >-
  This, then, is that humility toward God. This is that genuine faith of the ancient fathers,
  which still remains intact among their successors.
relations:
- type: associated-with
  target: gallic.force.received-programs-logic
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"still remains intact among their successors"` returns line 25394; read with `sed -n '25389,25395p'`,
inside `<div4 title="Chapter XIX..." ... id="iv.iii.xii.xix">` (Institutes XII.19, its own opening
sentence). The quoted span is one complete sentence, "This then is that humility..." through
"...still remains intact among their successors.", ending at its own period.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
