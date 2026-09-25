---
id: gallic.quote.customs-delivered-to-us-by-the-fathers
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
    Documented as Cassian's own text (Institutes Preface, read at its locus for this record) - his
    own description, in the same sentence as Castor's request, of the Egyptian customs as
    themselves received from the Fathers, not invented by Cassian or by Egypt itself.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Preface (npnf211 div iv.ii, file lines 16442-16446): Cassian describing the Egyptian and
    Palestinian customs as themselves handed down by the Fathers"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether Cassian claims the Egyptian customs themselves were received, not invented"
  - "participant wants the reception logic applied to Egypt's own practice, not just to Gaul's request for it"
  prefer_instead:
  - "participant wants Castor's own request that opens this same sentence - retrieve gallic.quote.castor-anxious-for-egyptian-institutions"
text: >-
  the customs of the monasteries which we have seen observed throughout
  Egypt and Palestine, as they were there delivered to us by the
  Fathers
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  This clause sits later in the same long sentence as Castor's own request (carried in
  gallic.quote.castor-anxious-for-egyptian-institutions). It matters on its own because it applies
  the same reception logic one level deeper: not only does Gaul receive from Egypt, but Egypt's own
  practice is itself something received from the Fathers, not something Egypt originated.
modern_rendering: >-
  You ask me to describe the customs of the monasteries. We have seen these customs kept throughout
  Egypt and Palestine, handed down to us there by the Fathers.
relations:
- type: associated-with
  target: gallic.force.legitimacy-by-reception
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"the customs of the monasteries which we have seen observed"` returns line 16444; read with `sed -n
'16438,16447p'`, inside `<div2 ... id="iv.ii">` (Institutes Preface), the same long sentence as
gallic.quote.castor-anxious-for-egyptian-institutions but a later clause in it, separated from that
record's own closing point ("...without monasteries.") by an intervening clause about Castor's own
perfection and eloquence that neither record carries. The quoted span is a complete subordinate
clause, "the customs of the monasteries..." through "...delivered to us by the Fathers", closing at
the clause's own natural boundary (a semicolon in the source) rather than continuing into the next,
unrelated clause about simple language for the brethren.

Normalization: line breaks joined with single spaces; a translator's endnote identifying Castor as
Bishop of Apta Julia sits earlier in this same sentence, outside this quoted span. No word was
added, dropped, substituted, or reordered; no terminal punctuation is added - the source's own
sentence continues past this clause, so this record's `text` field closes without inventing a period
the source does not have at this position.
