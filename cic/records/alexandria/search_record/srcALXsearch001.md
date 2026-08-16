---
id: srcALXsearch001
world_id: alexandria-catechetical
record_type: search_record
schema_version: 1
register: etic
review_state: draft
jobs:
- 1
sampling_strategy: Purposive, not comprehensive (Booth's standard) - EXPLICITLY SCOPED AS A MIGRATION-TIME
  SEARCH (2026-07-27, S6.2 per F2), documenting this sweep only, never the original build's own discovery
  process (unrecoverable by design per the backfill rule). FIRST SWEEP UNDER THE GOVERNING V7.4 STEP 2
  STANDARD (S6.1).
types_sought:
- works load-bearing in the deployed chunks' own Key Sources but absent from the S2.1 rows
- works load-bearing in Doc_05/Doc_09 prose but row-less
- critical editions and standard translations (deferred to pre-freeze re-sweep)
approaches:
  deployed-chunk-key-sources-sweep: 1
  build-doc-title-grep: 2
  row-diff: 1
years_searched:
  from: 1966
  to: 2026
languages_searched:
- en
inclusion_exclusions: 'Included: every work the deployed chunks'' Key Sources cite that no row covered
  at work-or-corpus level. Excluded: Scripture (native by the Framework''s own rule, never rowed separately);
  works already covered at corpus level (all Origen citations resolve into srcALX002''s named corpus;
  Festal Letters/Orations/Serapion/Marcellinus/Defense resolve into srcALX003''s corpus title); ''Anno
  Martyrum'' (an era-name, not a work).'
terms_tried:
- term: Key Sources sections, all 45 deployed lexicon chunks (grep + diff vs rows)
  productive: true
- term: Doc_05 asterisked work-title grep
  productive: false
- term: Doc_09 asterisked work-title grep
  productive: false
- term: row-diff re-run after adding the six sweep rows
  productive: false
instruments:
- deployed-chunk Key-Sources sweep (the productive instrument; wrs/migrate/s62_alx_sweep.py)
- Doc_05/Doc_09 asterisked-title greps (saturation passes)
- 'NOT ACCESSED, logged as coverage limits of this migration-time sweep: BIBP; L''Annee philologique;
  the Oxford Bibliographies current-scholarship check; CPG re-verification against the printed Clavis.
  Re-run before world-freeze.'
---
Saturation statement (the governing V7.4 Step 2 standard's requirement, first applied here; migration-time scope): the last searches of this sweep returned nothing new - the Doc_05 and Doc_09 asterisked-title greps re-surfaced only already-rowed works (the Address -> srcALX007, Contra Celsum -> srcALX002/srcALX015, Apophthegmata -> srcALX011) and non-work phrases, and the row-diff re-run after adding the six sweep rows found no remaining row-less citation at work or corpus level. Four instruments remain unsearched (BIBP; L'Annee philologique; Oxford Bibliographies; CPG-against-printed-Clavis) and are recorded as COVERAGE LIMITS of this migration-time sweep, not as satisfied searches; the pre-freeze re-sweep must run them.

Sweep provenance: wrs/migrate/s62_alx_sweep.py (this file is the sweep log; the six added rows srcALX027-032 carry real discovery_channel/instrument/date, unlike the migrated srcALX001-026 whose historical discovery data is unrecoverable by design).

Pre-freeze re-sweep (2026-07-28): the four S2.1b relative-recall/PRESS misses rowed as srcALX034-037 (Haas, Crouzel, Osborn, Roberts - the S-row scholarship-apparatus class; each verification_note declares the work not independently examined this session). The four named coverage limits (BIBP, L'Annee philologique, Oxford Bibliographies, CPG) STAND - no database access this session; saturation is NOT claimed improved beyond the recall-instrument closure. See wrs/migrate/s62_alx_presweep.py.
