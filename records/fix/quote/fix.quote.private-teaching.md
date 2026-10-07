---
id: fix.quote.private-teaching
world_id: fixture-synthetic
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [C-P]
confidence:
  citation_specificity: C
  verification_state: named-not-rechecked
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: "Attributed by the secondary summary only; the primary scroll does not record this teaching as spoken aloud, only copied privately - the license reflects that."
sources:
  - {source_id: fix.source.secondary-summary, locus: "5.1", license: public-domain}
text: "What is written for the initiate alone is not for the crowd, and not for the voice to speak."
modern_rendering: >-
  What is written for the initiate alone is not for the crowd, and not for the voice to
  speak.
speaker_or_author: fix.figure.the-elder
license: paraphrase-only
modern_lens_note: "No significant modern-lens risk identified for this quote."
use_note:
  means: "Testland held some teaching back for the initiated alone."
  not_for:
    - "the content of that private teaching"
  years: {from: 100, to: 100}
  status: provisional
---
The paraphrase-only positive case: this record's own divergence_note names a
genuinely fragile attribution (the secondary summary only; the primary scroll
never confirms the teaching was spoken aloud), so its license reflects that -
gate_quote_mark_fidelity (engine/m1/gates.py) must never let a world_front
render this material inside quotation marks, from either `text` or
`modern_rendering`, regardless of whether it happens to match. The
quote-recording DEFECT mutates a copy's license field to an invalid enum
value ("maybe") instead of one of verbatim | paraphrase-only.
