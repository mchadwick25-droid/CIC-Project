---
id: hal.quote.hindered-by-jerome
world_id: hieronymian-ascetic-literary
record_type: quote
schema_version: 2
status: ready
register: etic
canon_cells:
- F6-I
- F2-E
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Documented
  divergence_note: >-
    This record's own text elides one bare inline endnote number this edition's own scan
    carries ("Paula,276 mother") - confirmed against the file's own numbered endnotes
    section ("276. 2 Cf. XXXVI. 6."), not a real second name or number attached to Paula.
    This file's own real endnote sequence is interleaved with page numbers, bracketed
    chapter numbers, and irregular gaps closely enough that an automated walk of the notes
    list cannot be verified to track it correctly end to end, so verification_state is
    verified-via-authority rather than verified-direct: the elision is confirmed by direct
    inspection, not by an automated gate.
sources:
- source_id: hal.source.palladius-lausiac
  locus: ch. 41 sec. 2 (file line 475)
  license: public-domain
text: 'Among them was the Roman lady Paula, mother of Toxotius, a woman of great
  distinction in the spiritual life. She was hindered by a certain Jerome from Dalmatia.
  For though she was able to surpass all, having great abilities, he hindered her by his
  jealousy, having induced her to serve his own plan.'
modern_rendering: >-
  Among them was the Roman lady Paula, mother of Toxotius, a woman of great distinction
  in the spiritual life. A certain Jerome from Dalmatia hindered her. She had great
  abilities and could have surpassed everyone, but his jealousy held her back -- he had
  led her to serve his own plan instead.
speaker_or_author: 'Palladius of Galatia, Lausiac History 41 (trans. Clarke)'
license: verbatim
modern_lens_note: '"Jealousy" carries the older sense of envy over standing or advantage, not a personal or romantic sense.'
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what outsiders made of the relationship at the centre of this circle"
  - "participant asks whether a woman's own work was overshadowed by the man she funded"
relations:
- type: associated-with
  target: hal.quote.paula-escaped-his-envy
use_note:
  means: "Palladius's Lausiac History says Jerome's jealousy hindered Paula, who could have surpassed all, by inducing her to serve his own plan."
  not_for:
    - "a settled verdict on the Paula-Jerome relationship; Palladius wrote from a milieu hostile to Jerome"
    - "this world's own voice; it is an outside, adverse witness"
    - "a claim that 'jealousy' here means romantic jealousy"
  years: {from: 386, to: 420}
  status: reviewed
---
Read word for word against the vendored Clarke translation by direct
inspection (a footnote number in the raw file, 'Paula,276', is left out of
the quoted text). The state is verified-via-authority rather than
verified-direct because the automated check does not pass a bare footnote
number; the divergence note says so. THE COUNTER-WITNESS QUOTE: the one independent near-contemporary
characterization of the world's central relationship, and it contradicts
Jerome's own. Register etic - this is testimony ABOUT the world from
outside and against it, never the world's own voice; its use is honesty
under pressure (F2-E: what would hold up; F6-I: the hardest true things),
always paired with its own bias (Palladius writes from an
Origenist-adjacent milieu hostile to Jerome -
hal.contested.paula-jerome-relationship carries the full contest).
Speaker given as a source-string: Palladius has no figure record, as an
outside author, matching the corpus's outside-witness discipline.
