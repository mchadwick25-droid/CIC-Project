---
id: fix.quote.identity-collision-saying
world_id: fixture-synthetic
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [F6-P]
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: null
sources:
  - {source_id: fix.source.witness-scroll, locus: "4.1", license: public-domain}
text: "We did not ask what a person had been before the water. We asked only what they carried after it."
speaker_or_author: fix.figure.the-elder
license: verbatim
modern_lens_note: "No significant modern-lens risk identified for this quote."
modern_rendering: "We never asked who you'd been before. We only asked what you carried afterward."
---
Substantive coverage for the identity-collision cell F6-P, paired with
fix.demo.identity-collision for the voice-side spoken non-judgment requirement
(spec §4.2, §4.3 step 5c).

This record populates the identity-collision cell F6-P so
gate_quote_mark_fidelity's own clean-baseline and seeded-defect proof
(fixtures/seeded_defects.yaml, quote-mark-fidelity-text-field-quoted) has
something to check against. `modern_rendering` follows the same
spoken-form convention every real world's quote records follow: a
modern-English translation, not a summary; `text` stays the original,
unquotable on any participant-facing surface.
