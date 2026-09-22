---
id: ijc.quote.augustine-vigil-hymns
world_id: imperial-juridical
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: ijc.source.augustine-confessions
  locus: IX.7 (npnf101 lines 13766-13775)
  license: public-domain
text: The pious people kept guard in the church, prepared to die with their bishop, Thy servant. There
  my mother, Thy handmaid, bearing a chief part of those cares and watchings, lived in prayer. ... At
  this time it was instituted that, after the manner of the Eastern Church, hymns and psalms should be
  sung, lest the people should pine away in the tediousness of sorrow; which custom, retained from then
  till now, is imitated by many, yea, by almost all of Thy congregations throughout the rest of the world.
speaker_or_author: "Augustine of Hippo, Confessions 9.7"
license: verbatim
modern_lens_note: >-
  'Thy'/'Thy handmaid'/'Thy servant' are the translation's own devotional register for direct
  address to God (this passage is prayer, addressed to God, not narration addressed to a reader) -
  an artifact of the English rendering, not this world's own chancery idiom.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what ordinary people did when their church was threatened"
  - "participant asks what they sang and why singing started"
relations:
- {type: illustrates, target: ijc.story.vigil-in-basilica}
---
Text verified verbatim against the vendored file 2026-08-21. The
ellipsis marks one omitted sentence ("We, still unmelted by the heat of
Thy Spirit, were yet moved by the astonished and disturbed city") -
Augustine's own interior state, left out with the omission MARKED
because his own formation belongs to another world's corpus; editorial
notes stripped per the edition's conventions. The one
independent eyewitness to any Ambrose confrontation, and the record's
one direct glimpse of an ordinary congregation's interior - fear given
singing to stand inside.

FIXED 2026-08-26 (cross-world transparency audit): speaker_or_author
used to carry "(licensed for this world as eyewitness to Milan, 386,
only)" - a build-team scope note that citation_cards.py/StoryMark.tsx
render verbatim to the participant as this quote's speaker line. The
speaker line now just names Augustine and the locus. NARROW LICENSE:
this quote is licensed for use in this world (ijc) specifically, as
Augustine's own eyewitness testimony to events at Milan in 386 - not
for reuse as general testimony in any other world's corpus.
