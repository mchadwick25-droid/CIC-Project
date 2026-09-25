---
id: gallic.quote.deserter-from-his-service
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
    Documented as Cassian's own text (Institutes X.3, read at its locus for this record) - his own
    description of what accidie does to a monk who gives way to it, named in the same soldier
    idiom the Institutes opens with.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes X.3 (npnf211 div iv.iii.x.iii, file lines 23518-23524): accidie's own end
    point, described as desertion from Christ's service"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks how Cassian names the fault of accidie in the soldier idiom"
  - "participant asks what the Institutes says happens to a monk who keeps leaving his cell"
  prefer_instead:
  - "participant wants the Institutes' own opening statement of the soldier idiom instead - retrieve gallic.quote.institutes-opening-soldier-of-christ"
text: >-
  and so the soldier of Christ becomes a runaway from His service, and
  a deserter, and "entangles himself in secular business," without at
  all pleasing Him to whom he engaged himself.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  Cassian names the same idiom the Institutes opens with - soldier of Christ - to describe its own
  failure: a monk worn down by accidie into visiting other cells becomes, in the same military
  language, a runaway and a deserter. The phrase "entangles himself in secular business" is Paul's
  own words (2 Timothy 2:4), quoted here as Cassian's own description of what desertion looks like.
modern_rendering: >-
  And so the soldier of Christ becomes a runaway from His service, and a deserter. He "gets tangled
  up in the business of everyday life," pleasing not at all the One to whom he pledged himself.
relations:
- type: associated-with
  target: gallic.gravity.soldier-of-christ
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"becomes a runaway from His service"` returns line 23522; read with `sed -n '23516,23524p'`, inside
`<div4 title="Chapter III..." ... id="iv.iii.x.iii">` (Institutes X.3, on accidie). The quoted span
is the final clause of a long sentence describing accidie's progress, "and so the soldier of
Christ..." through "...to whom he engaged himself.", ending at its own period; the sentence's own
earlier clauses (on being drawn away from the cell by repeated visiting) are not carried, since they
do not use the soldier idiom this record exists to document.

Normalization: line breaks joined with single spaces; the source's own curly quotation marks around
the nested Pauline phrase "entangles himself in secular business" are rendered here as straight
double quotes, the same marks in a different Unicode form - this is Scripture quoted inside Cassian's
own sentence (2 Tim. ii. 4, per the source's own endnote), not this record's own added structure.
No word was added, dropped, substituted, or reordered.
