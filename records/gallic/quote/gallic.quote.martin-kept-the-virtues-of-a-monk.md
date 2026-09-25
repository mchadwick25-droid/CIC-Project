---
id: gallic.quote.martin-kept-the-virtues-of-a-monk
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
    Widely Accepted: Documented as Sulpitius's own text (Vita ch. X, read at its locus for this
    record), his own summary judgment of Martin's conduct once in office, written by someone who
    claims to have visited Martin at Tours and questioned those who had lived with him.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. X (npnf211 div ii.ii.xi, file lines 1117-1125): Sulpitius's summary of how Martin conducted himself as bishop"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether becoming bishop changed Martin, or what he kept from his monastic life once in office"
  - "conversation reaches the monk-bishop and needs the north's own statement that the two roles did not cancel each other"
  prefer_instead:
  - "participant wants the election story itself - retrieve gallic.quote.ruricius-and-the-vote-for-tours instead, or alongside"
text: >-
  Full alike of dignity and courtesy, he kept up the position of a bishop properly, yet in such a way
  as not to lay aside the objects and virtues of a monk.
speaker_or_author: gallic.figure.sulpitius
license: verbatim
modern_lens_note: >-
  A modern reader might expect the office to have changed the man. Sulpitius states the opposite as a
  single balanced sentence: dignity fit for a bishop, held together with the plain "objects" - the
  ordinary tools and habits - of a monk. Neither role is described as winning out over the other.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.story.election-at-tours
---
Verified directly against the vendored cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml.
`grep -n "objects and virtues of a monk"` returns one hit, line 1125. The chapter div is `<div3
title="Chapter X. Martin as Bishop of Tours." ... id="ii.ii.xi">` (line 1111), paragraph `ii.ii.xi-p2`
(lines 1117-1125). The quoted sentence runs "Full alike of dignity and courtesy, he kept up the position
/ of a bishop properly, yet / in such a way as not to lay aside the objects and virtues of a monk."
(lines 1123-1125), a complete sentence, preceded by "There was the same humility in his heart, and the
same homeliness in his garments." - left out here as a separate sentence making the same point, not
part of this one.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single spaces.
No word was added, dropped, substituted, or reordered.

speaker_or_author is gallic.figure.sulpitius: this is Sulpitius's own summary judgment in the Life of
Martin.
