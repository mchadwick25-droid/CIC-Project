---
id: desert.quote.god-is-not-a-body
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: etic
canon_cells:
- F6-I
- F3-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    THE WORDING IS RUFINUS', NOT ORIGEN'S. De Principiis survives whole only in Rufinus' Latin of
    398, made during the controversy by a partisan who says in his own prologue that he corrected
    what he judged corrupted - so this is a translation of a translation, and the Greek behind this
    particular sentence does not survive to check it. What is NOT in doubt is that this is the
    position the anthropomorphite monks were reacting against: on that the historians and the
    doctrine agree. Cite it as the doctrine at issue, never as Origen's own sentence.
sources:
- source_id: desert.source.origen-de-principiis
  locus: >-
    De Principiis I.1.6, in Rufinus' Latin and the ANF English (anf04, file line 22800)
  license: public-domain
text: >-
  God, therefore, is not to be thought of as being either a body or as existing in a body, but as
  an uncompounded intellectual nature, admitting within Himself no addition of any kind; so that He
  cannot be believed to have within him a greater and a less, but is such that He is in all parts
  Μονάς, and, so to speak, ῾Ενάς, and is the mind and source from which all intellectual nature or
  mind takes its beginning.
modern_rendering: >-
  So we must not think of God as a body, or as existing inside a body. God is an uncompounded
  intellectual nature. Nothing can be added to him in any way. So we cannot believe that he has
  within him a greater part and a lesser part. He is, in every part, Μονάς -- and, so to speak,
  ῾Ενάς. He is the mind and the source from which every intellectual nature, every mind, takes its
  beginning.
speaker_or_author: Origen, in Rufinus' Latin of De Principiis
license: verbatim
modern_lens_note: >-
  "Monas" and "Henas" (Μονάς and ῾Ενάς in the record's own text field) are Greek left untranslated in
  the ANF - unit and oneness. A modern reader will find this uncontroversial to
  the point of dullness: of course God has no body. That reaction is the reason the record exists.
  In 399 an Egyptian bishop said something like it in a festal letter and monks in the desert were
  furious, because if God has no body then the image of God in Genesis is not a face, and a man who
  has spent forty years praying to a face is being told he was praying to nothing. Read the
  sentence knowing what it takes away, not what it asserts.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what the argument or controversy about Origen was actually about"
  - "participant asks whether God has a body or a face, or what it meant to be made in God's image"
  - "participant asks why a bishop's letter could enrage monks in the desert"
relations:
- type: associated-with
  target: desert.force.origenist-controversy
- type: associated-with
  target: desert.gravity.evagrian-systematization
use_note:
  means: "Rufinus's Latin of Origen's De Principiis states that God is an uncompounded intellectual nature, neither a body nor existing in a body."
  not_for:
    - "the sentence as Origen's own Greek wording"
    - "evidence that desert monks read De Principiis"
    - "a desert voice, when it is the doctrine the anthropomorphite monks reacted against"
  years: {from: 398, to: 400}
  status: provisional
---
Verified verbatim against the vendored file at line 22800.
The ANF prints the Latin "Simplex intellectualis natura" as
an inline editorial note after "uncompounded intellectual nature"; the
note is excised.

The text field carries the source's own Greek script for Μονάς/῾Ενάς exactly, including its
polytonic accent forms (which differ at the codepoint level from the modern monotonic accented
letters one would type by default), not a Latin-letter transliteration ("Monas"/"Henas").

Registered because desert.force.origenist-controversy could say a fight
happened and could not say what about. This is the content. It is the
first line of Origen this world holds.
