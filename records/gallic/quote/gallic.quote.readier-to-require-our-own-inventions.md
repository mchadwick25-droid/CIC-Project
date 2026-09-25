---
id: gallic.quote.readier-to-require-our-own-inventions
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
    Documented as Cassian's own text (Institutes II.3-4, read at its locus for this record) - his
    own named fault, naming what happens when a community does not wait to learn the elders' own
    system before making rules of its own.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes II.3-4 (npnf211 div iv.iii.ii.iii, file lines 17090-17098): Cassian naming the
    fault of self-appointed authority and self-invented rules"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks what Cassian names as the specific failure when reception logic is not followed"
  - "participant wants the negative case (invented rules) rather than the positive standard"
  prefer_instead:
  - "participant wants Cassian's own positive statement of the standard instead - retrieve gallic.quote.allegiance-to-antiquity-not-a-few"
text: >-
  And so we see that there is a variety of rules and regulations in use
  throughout other districts, because we often have the audacity to
  preside over a monastery without even having learnt the system of
  the Elders, and appoint ourselves Abbots before we have, as we ought,
  professed ourselves disciples, and are readier to require the
  observance of our own inventions than to preserve the well-tried
  teaching of our predecessors.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  Cassian names a specific, ordinary failure here, not an abstract principle: a community's rules
  vary from place to place because someone became an abbot without first being a disciple, and then
  preferred enforcing their own inventions to keeping the elders' well-tried teaching. The fault is
  sequence as much as content - ruling before being ruled.
modern_rendering: >-
  And so we see different rules and regulations in use throughout other districts. This is because
  we often have the audacity to take charge of a monastery. We do so without even having learned
  the system of the Elders. We make ourselves Abbots before we have, as we ought, formally bound
  ourselves as disciples. We are readier to demand that our own inventions be kept than to preserve
  the tried and tested teaching of those before us.
relations:
- type: associated-with
  target: gallic.force.legitimacy-by-reception
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"appoint ourselves Abbots before we have"` returns line 17095; read with `sed -n '17088,17098p'`,
inside `<div4 title="Chapter III/IV..." ... id="iv.iii.ii.iii">` (Institutes II, on the sequence of
monastic formation). The quoted span is one complete sentence, "And so we see that there is a
variety..." through "...teaching of our predecessors.", ending at its own period.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
