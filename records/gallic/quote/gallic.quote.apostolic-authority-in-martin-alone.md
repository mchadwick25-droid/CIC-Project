---
id: gallic.quote.apostolic-authority-in-martin-alone
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
    Documented as Sulpitius's own narration (Vita ch. XX) of the bishops' assembly before Emperor
    Maximus. The underlying event (the assembly, Martin's conduct there) is Widely Accepted history;
    the wording itself, carried here, is Sulpitius's own characterization.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. XX (npnf211 div ii.ii.xxi, file lines 1562-1565): Sulpitius contrasts the bishops' flattery of Maximus with Martin's own bearing"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how Martin conducted himself before secular power, compared to other bishops"
  - "participant asks what 'apostolic authority' meant to this world, in contrast to court favor"
  prefer_instead:
  - "participant is asking about Maximus's usurpation itself as a political event - this record carries Sulpitius's judgment of Martin's bearing, not a history of the reign"
text: >-
  while the priestly dignity had, with degenerate submissiveness, taken a
  second place to the royal retinue, in Martin alone, apostolic
  authority continued to assert itself.
speaker_or_author: Sulpitius Severus, narrating
license: verbatim
modern_lens_note: >-
  This is Sulpitius's own verdict, not a report of anything Martin said. Bishops flattering the
  usurper Maximus is the backdrop; Martin's refusal to do so is what Sulpitius calls "apostolic
  authority." The word choice matters: Sulpitius does not credit Martin's stance to personal courage
  alone but names it with the same authority he elsewhere claims for the apostles themselves - the
  clearest single line in the Vita crediting Martin with an authority that outranks the episcopate
  around him.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.gravity.authority-ambivalence
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"apostolic authority continued to assert itself"` returns one hit, line 1565, inside `<div3
title="Chapter XX. How Martin acted towards the Emperor Maximus." ... id="ii.ii.xxi">` (printed
heading "Chapter XX.", div id one higher). The excerpted clause runs lines 1562-1565: "while the
priestly dignity had, with degenerate submissiveness, taken a second place to the royal retinue, in
Martin alone, apostolic authority continued to assert itself." This is drawn from inside a single
very long sentence describing the bishops' assembly before Maximus; only the contrastive clause
naming Martin is carried here, not the full run-on sentence.

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
