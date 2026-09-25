---
id: gallic.quote.castor-anxious-for-egyptian-institutions
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
    Documented as Cassian's own text (Institutes Preface, read at its locus for this record) -
    Cassian's own description of Bishop Castor's request, the founding statement of the south's
    receptive mode toward Egypt.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Preface (npnf211 div iv.ii, file lines 16432-16436): Cassian's account of why Bishop
    Castor asked him to write - a province with no monasteries, wanting Egypt's own institutions
    established in it"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why Cassian wrote the Institutes at all"
  - "participant asks who first asked for Egyptian monastic customs to come to Gaul"
  prefer_instead:
  - "participant wants Cassian's own method for adapting those customs, not just the original request - retrieve gallic.quote.cassian-adapts-egypt-to-gaul"
text: >-
  Since, then, you are anxious that the institutions of the East and
  especially of Egypt should be established in your province, which is
  at present without monasteries
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  Castor is not asking Cassian to invent something new. The request is specifically for Egypt's
  own institutions, transplanted - a province starting with nothing wants the real thing, not a
  local imitation.
modern_rendering: >-
  You are eager, then, to see the East's own institutions set up in your province. You want
  Egypt's institutions most of all. Right now, your province has no monasteries.
relations:
- type: associated-with
  target: gallic.gravity.egypt-as-measure
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"institutions of the East"` returns line 16434; read with `sed -n '16420,16436p'`, inside `<div2
... id="iv.ii">` (Institutes Preface). The quoted span is a complete subordinate clause within a
much longer sentence (Cassian's Preface runs on at length past this clause into an unrelated
disclaimer about his own unworthiness); this record closes the quote at its own natural full stop
("...without monasteries.") rather than continuing into a different topic that does not bear on
this clause's own claim, and rather than force the whole run-on sentence into one record.

Normalization: line breaks joined with single spaces; a translator's footnote identifying Castor
as Bishop of Apta Julia was excluded as apparatus. No word was added, dropped, substituted, or
reordered; no terminal punctuation is added after "monasteries" - the source's own sentence
continues past this point into an unrelated disclaimer about Cassian's own unworthiness, so this
record's `text` field closes at the end of this complete clause without inventing a period the
source does not have at that position (`engine.m1.quote_verbatim` treats a substituted punctuation
mark as a real difference, not a tolerated one).

This span was previously carried, unresolved, inside gallic.gravity.egypt-as-measure's own
`description` field. The host record now paraphrases it in its own voice and
points here for the verbatim wording.
