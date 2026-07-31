---
id: srcHALsearch001
world_id: hieronymian-ascetic-literary
record_type: search_record
schema_version: 1
register: etic
review_state: draft
jobs:
- 1
sampling_strategy: Purposive, not comprehensive (Booth's standard) - EXPLICITLY SCOPED AS A MIGRATION-TIME
  SEARCH (2026-07-31, S6.2/HAL S2.1a), documenting this sweep only, never the original build's own discovery
  process (unrecoverable by design per the backfill rule). Third sweep under the governing V7.4 Step 2
  standard (ALX/SYR precedents).
types_sought:
- works load-bearing in the deployed chunks' own Key Sources / story Source lines but absent from the
  S2.1 rows
- critical editions and standard translations (deferred to the pre-freeze re-sweep, fleet rule)
approaches:
  deployed-chunk-key-sources-sweep: 1
  row-diff: 1
years_searched:
  from: 1975
  to: 2026
languages_searched:
- en
inclusion_exclusions: 'Included: every chunk-cited work no row covered at work-or-corpus level (one found:
  the Praefationes corpus). Excluded: works inside existing corpus rows (all Epistulae citations incl.
  the Riparius letter -> srcHAL001; the two Apologiae -> 005/007; the vitae -> 004; the Augustine correspondence
  -> 009; Rebenich/Cain -> 015/010); the Perseus critical-text verification (editions class, pre-freeze
  re-sweep); the UNNAMED ''general social-historical scholarship on senatorial households'' aggregate
  (hal_lex05/10 - no work named, none manufactured; the S2.1b PRESS names candidates if any belong); composite
  stories'' Source Identification tables (S2.4''s own layer).'
terms_tried:
- term: Key Sources sections + story Source lines, all 27 deployed HAL chunks (diff vs rows)
  productive: true
- term: row-diff re-run after adding srcHAL023
  productive: false
instruments:
- deployed-chunk Key-Sources sweep (the productive instrument; wrs/migrate/s62_hal_sweep.py)
- 'NOT ACCESSED, logged as coverage limits of this migration-time sweep: BIBP; L''Annee philologique;
  Oxford Bibliographies; PLUS this world''s own two Doc_02-flagged verification items, which STAND as
  open until someone with the texts runs them - the Marcella-correspondence list vs Cain''s critical apparatus
  (srcHAL001''s own caveat) and the Palladius passage hunt (srcHAL008''s do-not-cite license). Re-run
  before world-freeze.'
---
Saturation statement (V7.4 Step 2; migration-time scope): the row-diff re-run after adding srcHAL023 found no remaining row-less citation at work or corpus level across all 27 chunks. The named coverage limits (BIBP; L'Annee philologique; Oxford Bibliographies) and this world's own two Doc_02-flagged verification items (the Marcella-list apparatus check; the Palladius passage location) are recorded as LIMITS, not satisfied searches; the pre-freeze re-sweep must address them.

Sweep provenance: wrs/migrate/s62_hal_sweep.py (this file is the sweep log; srcHAL023 carries real discovery data, unlike the migrated srcHAL001-022 whose historical discovery is unrecoverable by design).
