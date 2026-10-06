---
id: gallic.quote.institutes-not-mine-but-the-fathers
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
    Documented as Cassian's own preface statement, opening the First Part of the Conferences,
    disclaiming personal authorship of the teaching he is about to transmit.
sources:
- source_id: gallic.source.cassian-conferences-part-i
  locus: "Preface to the First Conferences (npnf211 div iv.iv.i, file lines 25931-25932): Cassian's own description of what the Institutes are"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks whether Cassian claimed to have invented monastic teaching himself"
  - "participant asks how Cassian described his own role in writing the Institutes"
  prefer_instead:
  - "participant wants the full preface sentence in context - this record carries the short, self-contained phrase only"
text: >-
  the Institutes which are not mine but the fathers'
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  This short phrase, inside a longer preface sentence, is Cassian's own disclaimer at the start of the
  Conferences: he presents himself as a channel for the fathers' teaching, not its author. It is the
  same posture Vincent takes independently in the Commonitory - "not an author but a keeper" - two
  writers making the identical claim about their own work, in their own words.
modern_rendering: >-
  the Institutes, which are not mine but the fathers'
relations:
- type: associated-with
  target: gallic.gravity.received-not-invented
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"may now by the reception of the Institutes"` returns one hit, line 25931, inside `<div3
title="Preface." ... id="iv.iv.i">`, itself within `<div2 title="The Conferences of John Cassian.
Part I. Containing Conferences I-X." ... id="iv.iv">`. The full clause reads (lines 25931-25932): "may
now by the reception of the Institutes which are not mine but the fathers', mount by a pure insight
to the merits..." This record carries only the short, self-contained noun phrase "the Institutes
which are not mine but the fathers'" - the clause the host record's flagged span isolated - dropping
the surrounding sentence's own unrelated grammar ("may now by the reception of... mount by a pure
insight to the merits of Israel"), which is Cassian's own extended figure about Jacob and Israel, not
part of the claim being carried here.

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
