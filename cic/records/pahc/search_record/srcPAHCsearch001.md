---
id: srcPAHCsearch001
world_id: post-apostolic-house-church
record_type: search_record
schema_version: 1
register: etic
review_state: draft
jobs:
- 1
sampling_strategy: Purposive, not comprehensive (Booth's standard) - EXPLICITLY SCOPED AS A MIGRATION-TIME
  SEARCH (2026-07-31, S6.2/PAHC S2.1a), documenting this sweep only, never the original build's own discovery
  process (unrecoverable by design per the backfill rule). Fourth sweep under the governing V7.4 Step
  2 standard (ALX/SYR/HAL precedents).
types_sought:
- works load-bearing in the deployed chunks' own Key Sources / story Source lines but absent from the
  S2.1 rows
- critical editions and standard translations (deferred to the pre-freeze re-sweep, fleet rule)
approaches:
  deployed-chunk-citation-sweep: 1
  registry-tag-verification: 1
years_searched:
  from: 1975
  to: 2026
languages_searched:
- en
inclusion_exclusions: 'Included: every chunk-cited work checked at work level - RESULT: ZERO misses, the
  fleet''s first clean sweep (the machine-registry world''s own build discipline: story Source lines carry
  inline registry tags; lexicon citations resolve by name to registered P-rows). Excluded with reasons:
  the Epistle of Barnabas 18-20 (pahclex007''s OWN note declares it outside this world''s defined source
  set - the chunk draws the boundary, honored not re-litigated); Hermas Mandate 11 (pahclex008''s topical-parallel
  caveat; the work itself is rowed as P05); the Roberts-Donaldson/ANF translation (pahclex010''s verification
  citation - editions class, pre-freeze re-sweep).'
terms_tried:
- term: 'story Source-line registry tags, all 13 stories (mechanical: every ''Registry Pnn'' tag has a
    row)'
  productive: false
- term: lexicon Key Sources name-resolution, all 11 sectioned chunks + 2 thin-format front matters
  productive: false
instruments:
- 'S2.1a deployed-chunk sweep (all 26 PAHC chunks: 11 lexicon Key Sources sections + 2 thin-format chunks
  + 13 story Source lines, diffed against the 73 machine-registry rows; wrs/migrate/s62_pahc_sweep.py)'
- 'NOT ACCESSED, logged as coverage limits of this migration-time sweep: BIBP; L''Annee philologique;
  Oxford Bibliographies. The registry''s own priority_review_flag queue (49 flagged rows in the FINAL_v2
  workbook) is the build''s own review instrument, already absorbed row-by-row via the verbatim assessment
  fields. Re-run before world-freeze.'
---
Saturation statement (V7.4 Step 2; migration-time scope): the citation sweep found ZERO row-less citations at work level across all 26 chunks - the fleet's first clean sweep, a product of the original build's own machine registry (story chunks cite by inline registry tag; the registry was already reconciled json==xlsx at the world-open survey). The named coverage limits (BIBP; L'Annee philologique; Oxford Bibliographies) are recorded as LIMITS, not satisfied searches; the pre-freeze re-sweep must address them plus the ANF/Roberts-Donaldson editions item.

Sweep provenance: wrs/migrate/s62_pahc_sweep.py (this file is the sweep log; it emits no source rows because none were owed - the mechanical tag-check re-runs on every invocation).
