---
id: gallic.quote.allegiance-to-antiquity-not-a-few
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
    Documented as Cassian's own text (Institutes I.2, read at its locus for this record) - his own
    statement of the standard by which a custom is judged legitimate, given while explaining why
    the Egyptian fathers rejected sackcloth.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes I.2 (npnf211 div iv.iii.i.ii, file lines 16667-16671): Cassian's own statement
    that allegiance is owed to antiquity and consent, not to a few individuals' own inventions"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what standard Cassian gives for whether a monastic custom is legitimate"
  - "participant asks how the south's own reception logic is stated in Cassian's own words"
  prefer_instead:
  - "participant wants Vincent's own parallel statement of the same standard - retrieve a Comm. ch. 2 record where one exists"
text: >-
  For we ought to give unhesitating allegiance and unquestioning
  obedience, not to those customs and rules which the will of a few
  have introduced, but to those which a long standing antiquity and
  numbers of the holy fathers have passed on by an unanimous decision
  to those that come after.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  This sentence appears inside a discussion of dress (why the Egyptian fathers rejected sackcloth),
  but it states a general rule, not a dress rule alone: obedience belongs to what long-standing
  antiquity and a broad consent of the fathers have handed on, not to what one person or a few
  people happen to prefer.
modern_rendering: >-
  For we ought to give loyalty without hesitation and obedience without question. But we should not
  give them to customs and rules that the will of a few has brought in. We should give them to
  those that long-standing antiquity and many holy fathers have handed on to those who come after.
  They did so by a unanimous decision.
relations:
- type: associated-with
  target: gallic.force.legitimacy-by-reception
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"unhesitating allegiance and"` returns line 16668; read with `sed -n '16664,16672p'`, inside `<div4
title="Chapter II..." ... id="iv.iii.i.ii">` (Institutes I.2, on the sackcloth rejected by the
Egyptian fathers). The quoted span is one complete sentence, "For we ought to give unhesitating
allegiance..." through "...to those that come after.", ending at its own period.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
