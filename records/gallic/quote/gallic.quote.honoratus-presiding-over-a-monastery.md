---
id: gallic.quote.honoratus-presiding-over-a-monastery
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted: Documented as Cassian's own text (Conferences Preface II, read at its locus for
    this record), addressed to "holy brothers Honoratus and Eucherius." Cassian names neither man's
    monastery; that the one "presiding ... over a large monastery" is Honoratus of Lerins is the
    editorial apparatus's identification, carried as such and not treated as Cassian's own statement.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'Conferences Preface II (npnf211 div iv.v.i): "one of you, presiding as he does over a large monastery of the brethren"'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks why Cassian dedicated this part of his book to an abbot about to become a bishop"
  - "participant asks how Cassian describes Honoratus in his own words"
  prefer_instead:
  - "participant wants the encounter with Archebius itself - retrieve gallic.quote.archebius-carried-off-to-panephysis or gallic.quote.archebius-see-the-old-men"
text: >-
  presiding as he does over a large monastery of the brethren
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  A modern reader might take this as a stock compliment in a dedication. It is also the only
  description Cassian gives of the man he is addressing - not a name for the place, not a title, but
  the fact of governing a large community of brothers. The identification with Lerins and Honoratus is
  the editorial apparatus's inference, not a claim in Cassian's own sentence.
modern_rendering: >-
  leading, as he does, a large monastery of brothers
relations:
- type: associated-with
  target: gallic.story.bishop-archebius
use_note:
  means: "Cassian describes one of the two brothers he addresses in Conferences Part II as presiding over a large monastery of brethren."
  not_for:
    - "Cassian's own naming of Lerins, when that identification is the editors'"
    - "a claim that Honoratus was already a bishop when addressed"
  years: {from: 426, to: 426}
  status: reviewed
---
Verified directly against the vendored cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml.
`grep -n "presiding as he does over a large"` returns one hit, line 36724. The div is `<div3
title="Preface." ... id="iv.v.i">` (line 36709), paragraph `iv.v.i-p1` (lines 36717-36732), addressed
to "holy brothers Honoratus and Eucherius." The quoted phrase runs "one of you, presiding as he does
over a large / monastery of the brethren, is hoping that his congregation..." (lines 36724-36725); the
excerpt begins at "presiding," dropping the sentence's own lead-in "one of you,".

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single space.
No word was added, dropped, substituted, or reordered.

speaker_or_author is gallic.figure.cassian: the words describe Honoratus but are Cassian's own, from
his dedication.
