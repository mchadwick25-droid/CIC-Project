---
id: hal.quote.ever-let-the-bridegroom-sport-with-you
world_id: hieronymian-ascetic-literary
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- C-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Jerome's own writing and circulated by him as a letter, which in this circle means a public document with an argument to win, not private correspondence. He is an advocate for the ascetic life throughout, and his portraits are shaped to persuade.
sources:
- source_id: hal.source.jerome-ep22
  locus: >-
    Letter XXII (to Eustochium), sec. 25 (npnf206_jerome-principal-works.xml)
  license: public-domain
text: >-
  Ever let the privacy of your chamber guard you; ever let the Bridegroom sport with you within. Do you pray? You speak to the Bridegroom. Do you read? He speaks to you. When sleep overtakes you He will come behind and put His hand through the hole of the door, and your heart shall be moved for Him; and you will awake and rise up and say: "I am sick of love."...
modern_rendering: >-
  Always let the privacy of your chamber guard you; always let the
  Bridegroom delight with you within. Do you pray? You speak to the
  Bridegroom. Do you read? He speaks to you. When sleep overtakes you,
  he will come behind and put his hand through the opening of the door,
  and your heart shall be moved for him; and you will awake and rise up
  and say: 'I am sick with love.'
speaker_or_author: Jerome, Letter XXII to Eustochium
license: verbatim
modern_lens_note: >-
  This is what 'who was Jesus to you' looks like in this world, and it is startling if you expect doctrine: Christ is addressed as the Bridegroom of the Song of Songs, and prayer and reading are the two halves of a conversation with him. 'Sport' translates a verb of play, not of sex; the erotic charge is real and is scriptural, taken wholesale from the Song. Written by a man in his forties to a girl in her teens, which is part of what a reader should see.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks who Jesus was to the people of this world"
  - "participant asks whether Christ was someone they related to personally"
  - "participant asks what prayer and reading were for here"
relations:
- type: associated-with
  target: hal.dw.was-jesus-god
---
Opened 2026-08-27 for C-T, which hal.dw.was-jesus-god served alone with no quote. That witness
cites this exact locus for "devotion to Christ as Lord and Bridegroom" and could not show it.

Chosen over the Apology against Rufinus, which the same witness also cites, because the Apology is
Jerome defending his orthodoxy under attack and this is Jerome saying what Christ was to the people
he was forming. A cell asking who Jesus was should be voiced by devotion rather than by a
disclaimer.

MODERN RENDERING AUTHORED (2026-08-29, hal register pass; Mark's standing quote ruling: spoken form is a modern-English translation, not a summary - original wording stays as text, shown at Level 3).

Quote-verbatim gate fix (2026-09-22): removed a stray literal backslash before the closing quote mark
in `text` (a YAML folded-scalar authoring bug, not a real source character). Separately, the record's
own closing quote mark stood in for a full stop - the source's sentence continues into an extended
Song-of-Songs dialogue (the Bridegroom's own reply, then a further meditation on not seeking Him in
the streets). Marked with a trailing ellipsis rather than restored: the record's gloss is specifically
about prayer and reading as the two halves of a conversation with Christ, complete at "I am sick of
love"; the extended dialogue that follows is a different, larger argument this record isn't citing for.
