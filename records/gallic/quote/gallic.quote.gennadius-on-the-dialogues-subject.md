---
id: gallic.quote.gennadius-on-the-dialogues-subject
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
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as Gennadius's own near-contemporary description (De Viris Illustribus ch.
    XIX, read at its locus for this record) of the Dialogues' own subject - independent ancient
    testimony, not Sulpitius's own self-description.
sources:
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: "ch. XIX (npnf203 div v.iv.xx, file lines 42545-42552): Gennadius's description of the
    Dialogues as a comparison of the Eastern monks and St. Martin"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks what the Dialogues were actually about, from an outside witness"
  - "participant asks for independent confirmation of what Sulpitius wrote"
  prefer_instead:
  - "participant wants the Dialogues' own comparative claims directly - retrieve gallic.quote.postumianus-you-have-conquered-all-the-eremites or gallic.quote.europe-will-not-yield-having-only-martin"
text: >-
  He also wrote a Conference between Postumianus and Gallus, in which
  he himself acted as mediator and judge of the debate. The subject
  matter was the manner of life of the oriental monks and of St.
  Martin—a sort of dialogue in two divisions.
speaker_or_author: Gennadius of Marseilles, De Viris Illustribus
license: verbatim
modern_lens_note: >-
  Gennadius is an independent, near-contemporary witness (writing c. 495), not Sulpitius describing
  his own work - his plain statement that the Dialogues set the Eastern monks and Martin side by
  side is outside confirmation that the comparison was the book's own actual subject, not a later
  reading imposed on it.
modern_rendering: >-
  He also wrote a Conference between Postumianus and Gallus. In it he himself acted as mediator
  and judge of the debate. Its subject was the way of life of the eastern monks and of St.
  Martin. It is a kind of dialogue in two parts.
relations:
- type: associated-with
  target: gallic.gravity.egypt-as-measure
---
Verified directly against cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml. `grep -n
"manner of life of the oriental monks"` returns line 42550; read with `sed -n '42544,42552p'`. The
quoted span runs across two sentences, "He also wrote a Conference..." through "...dialogue in two
divisions.", ending at the second sentence's own period.

Normalization: line breaks joined with single spaces; the source's own italic markup (`<i>`) around
work-titles was dropped, the same normalization the fleet applies to plain-text rendering of
italicized titles elsewhere. No word was added, dropped, substituted, or reordered.

speaker_or_author is a plain string: no gallic.figure record exists for Gennadius.