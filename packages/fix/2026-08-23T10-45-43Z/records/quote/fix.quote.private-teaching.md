---
id: fix.quote.private-teaching
world_id: fixture-synthetic
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: C
  verification_state: named-not-rechecked
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: "Attributed by the secondary summary only; the primary scroll does not record this teaching as spoken aloud, only copied privately - the license reflects that."
sources:
  - {source_id: fix.source.secondary-summary, locus: "5.1", license: public-domain}
text: "What is written for the initiate alone is not for the crowd, and not for the voice to speak."
speaker_or_author: fix.figure.the-elder
license: do-not-voice
modern_lens_note: "No significant modern-lens risk identified for this quote."
---
The do-not-voice positive case (Artifact-1 §4): ships in quotes.json (M2) so a
violation is recognizable, but the voice must never speak it. The quote-recording
DEFECT mutates a copy's license field to an invalid enum value ("maybe") instead of
one of verbatim | paraphrase-only | do-not-voice.
