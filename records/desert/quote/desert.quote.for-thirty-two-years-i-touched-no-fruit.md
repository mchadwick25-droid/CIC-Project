---
id: desert.quote.for-thirty-two-years-i-touched-no-fruit
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Palladius's own report, gathered on visits he describes making. He names his informants where he has them, and marks what he heard from the man himself.
sources:
- source_id: desert.source.palladius-lausiac-history
  locus: >-
    Lausiac History ch. XLV (Philoromus), in Clarke's translation (palladius_lausiac-history_clarke1918.txt)
  license: public-domain
text: >-
  He renounced the world in the days of Julian the infamous Emperor, and spoke to him with boldness. Julian ordered him to be shaved and buffeted by boys. He endured the ordeal patiently and expressed his thanks to Julian, as he told us himself. ... He told us this: "For thirty-two years I touched no fruit." Once when timidity attacked him, in order to get rid of it, he shut himself up in a tomb for six years.
modern_rendering: >-
  He renounced the world in the days of the infamous Emperor Julian. He spoke to Julian with
  boldness. Julian ordered him shaved and beaten by boys. He endured this ordeal patiently, and he
  expressed his thanks to Julian, as he himself told us. ... He told us this: "For thirty-two years,
  I did not touch fruit." Once, when fear attacked him, in order to get rid of it, he shut himself in
  a tomb for six years.
speaker_or_author: Palladius, reporting Philoromus of Galatia in his own words
license: verbatim
modern_lens_note: >-
  Asked whether they were born again, this world answers with a date and a discipline rather than an experience: a life renounced in a named emperor's reign, and then counted in years of not touching fruit. 'As he told us himself' and 'He told us this' mark the two places Palladius claims first-hand speech. The ellipsis spans his account of the fight against fornication and gluttony.
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks whether people here were born again or converted"
  - "participant asks how someone here would describe what happened to them"
  - "participant asks whether there was a moment their life changed"
relations:
- type: associated-with
  target: desert.dw.born-again
---
This record fills canon cell F4-T. desert.dw.born-again alone serves this cell, citing this chapter
for "the day he took up this life, in his own words".

Chosen over the alternative locus the same cell offered (Vita SS16, on the shortness of life
against the ages to come) because this one is a participant speaking in the first person about his
own turning, which is what the cell's question actually asks for.

The text field carries no stray literal backslashes before quote marks (a YAML folded-scalar
authoring artifact, not real source characters). Verification cannot yet clear past "world" early in
the first sentence: the source has a page-break marker ("world |146 in the days") that the automated
verification gate does not strip - a pipe-plus-digits form, distinct from the bare-digit and
bracketed forms already found elsewhere.
