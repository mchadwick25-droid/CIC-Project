---
id: srcIJCsearch001
world_id: imperial-juridical-christianity
record_type: search_record
schema_version: 1
register: etic
review_state: draft
jobs:
- 1
sampling_strategy: 'Purposive (Booth''s standard) - the S2.1a MIGRATION-TIME SWEEP (2026-07-31): every
  citation surface in the 18 deployed chunks verified against the 38-row registry; documents THIS sweep
  only.'
types_sought:
- story-chunk Source lines (6)
- lexicon Key Sources sections (10; ijclex011/012 carry none by design - material-culture terms whose
  evidence classes are rows 36-38)
- in-chunk registry citations (the 'Source Registry row 15' currency, live in two Author-Gravity notes)
approaches:
  chunk-citation-extraction: 1
  registry-row-mapping: 1
  distinguishing-phrase grep: 1
years_searched:
  from: 312
  to: 2026
languages_searched:
- en
- la
- grc
inclusion_exclusions: 'Included: every work named on a deployed citation surface. Result: ZERO MISS ROWS
  - the fleet''s second clean sweep (PAHC first). The registry''s own append-only discipline plus its
  Round-2 co-equal review with Doc_02 evidently held the chunk-to-registry chain closed at build time.'
terms_tried:
- term: the 16 mapped citation surfaces, each grep-confirmed
  productive: true
- term: any chunk-cited work without a registry row
  productive: false
instruments:
- 'S6.2/IJC S2.1a sweep (2026-07-31): wrs/migrate/s62_ijc_sweep.py - this file is the sweep log; the chunk->row
  mapping is declared in its docstring and verified mechanically on every run.'
---
Saturation statement (V7.4; sweep scope): all 16 citation-bearing chunks map to existing rows; the two chunks without Key Sources (basilica, martyrium) are material-culture terms whose evidence classes are the registry's own rows 36-38, declared not missing. Relative recall and PRESS run at S2.1b (reviews/S6.2_IJC_s21b_coverage.md).

Provenance: wrs/migrate/s62_ijc_sweep.py.
