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
    Quote-verbatim gate note (2026-09-23, item 2 of the P3 registration queue): this record's
    own text already elides one bare inline endnote number this edition's own scan carries
    ("Paula,276 mother", disclosed in the body below since 2026-08-21) - independently
    confirmed against the file's own numbered endnotes section ("276. 2 Cf. XXXVI. 6."), not a
    real second name or number attached to Paula. An edition-level rule that walks the notes
    list in sequence to tell a footnote number from real digit content was attempted
    (cic/texts/REGISTRY.yaml's own history) and works on a clean synthetic case, but this
    file's own real sequence is interleaved with page numbers, bracketed chapter numbers, and
    irregular gaps closely enough that a general walk cannot be verified to track it correctly
    end to end - flagged for a ruling rather than shipped un-verified. verification_state
    lowered from verified-direct to verified-via-authority to reflect that the elision is
    confirmed by direct inspection, not by an automated gate.
sources:
- source_id: hal.source.palladius-lausiac
  locus: ch. 41 (file lines 473-475)
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
---
Verified verbatim 2026-08-21 against the vendored Clarke translation (a
footnote-number artifact in the raw file, 'Paula,276', is elided from the
quoted text - disclosed here per independent review Round 1, 2026-08-21,
which found this elision unlike the corpus's other quote records had not
been noted). THE COUNTER-WITNESS QUOTE: the one independent near-contemporary
characterization of the world's central relationship, and it contradicts
Jerome's own. Register etic - this is testimony ABOUT the world from
outside and against it, never the world's own voice; its use is honesty
under pressure (F2-E: what would hold up; F6-I: the hardest true things),
always paired with its own bias (Palladius writes from an
Origenist-adjacent milieu hostile to Jerome -
hal.contested.paula-jerome-relationship carries the full contest).
Speaker given as a source-string: Palladius has no figure record, as an
outside author, matching the corpus's outside-witness discipline.
