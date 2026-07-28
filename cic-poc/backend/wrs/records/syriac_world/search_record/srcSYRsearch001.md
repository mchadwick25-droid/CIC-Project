---
id: srcSYRsearch001
world_id: syriac-edessa-nisibis
record_type: search_record
schema_version: 1
register: etic
review_state: draft
jobs:
- 1
sampling_strategy: Purposive, not comprehensive (Booth's standard) - EXPLICITLY SCOPED AS A MIGRATION-TIME
  SEARCH (2026-07-28, S6.2/SYR S2.1a), documenting this sweep only, never the original build's own discovery
  process (unrecoverable by design per the backfill rule). Second sweep under the governing V7.4 Step
  2 standard (ALX precedent srcALXsearch001).
types_sought:
- works load-bearing in the deployed chunks' own Key Sources / story Source lines but absent from the
  S2.1 rows
- works named by the build docs' own correction text (Doc_02 SS3 Revision-Log class) but row-less
- critical editions and standard translations (deferred to the pre-freeze re-sweep, ALX pattern)
approaches:
  deployed-chunk-key-sources-sweep: 1
  composite-row-string-adjudication: 1
  build-doc-correction-text-read: 1
  row-diff: 1
years_searched:
  from: 1894
  to: 2026
languages_searched:
- en
inclusion_exclusions: 'Included: every chunk-cited or correction-text-named work no row covered at work-or-corpus
  level, each adjudicated against the FULL composite string of the nearest existing row before being called
  a miss. Excluded: Scripture (native by the Framework''s own rule); works inside existing composite rows
  (Valavanolickal -> row 10; Harvey -> row 32; Malki -> row 33; Bar Ebroyo -> row 42; Amar -> row 34);
  edition-level detail of rowed works (Doctrina Addai eds. Howard 1981 / Lollar 2023 -> row 20, deferred
  to the pre-freeze re-sweep per the ALX editions rule); second-order apparatus (Acts of Miles + Synodicon
  Orientale are the GEDSH Papa-bar-Aggai entry''s OWN sources, not chunk-load-bearing - flagged to the
  pre-freeze re-sweep rather than rowed second-hand).'
terms_tried:
- term: Key Sources sections + story Source lines, all 19 deployed Syriac chunks (diff vs rows)
  productive: true
- term: composite-row verbatim pulls for adjudication (rows 26/29/42/47/51)
  productive: true
- term: Doc_02 SS3 / Doc_03 SS1.2 correction-text read (the qyama-specific Griffith citations)
  productive: true
- term: Doc_02 CSCO/Beck edition-table check
  productive: false
- term: row-diff re-run after adding the eight sweep rows
  productive: false
instruments:
- deployed-chunk Key-Sources sweep (the productive instrument; wrs/migrate/s62_syr_sweep.py)
- 'composite-row-string adjudication (prevented four false misses: Valavanolickal/Harvey/Malki/Bar-Ebroyo)'
- 'NOT ACCESSED, logged as coverage limits of this migration-time sweep: BIBP; L''Annee philologique;
  Oxford Bibliographies; the Hugoye cumulative index; a systematic GEDSH pass (row 51 + srcSYR058 carry
  entries ad hoc). Re-run before world-freeze.'
---
Saturation statement (V7.4 Step 2; migration-time scope): the last searches of this sweep returned nothing new - the Doc_02 CSCO/Beck edition-table check re-surfaced only already-rowed Ephrem corpora, and the row-diff re-run after adding the eight sweep rows found no remaining row-less citation at work or corpus level across all 19 chunks. Five instruments remain unsearched (BIBP; L'Annee philologique; Oxford Bibliographies; the Hugoye cumulative index; a systematic GEDSH pass) and are recorded as COVERAGE LIMITS, not satisfied searches; the pre-freeze re-sweep must run them.

Sweep provenance: wrs/migrate/s62_syr_sweep.py (this file is the sweep log; the eight added rows srcSYR054-061 carry real discovery_channel/instrument/date, unlike the migrated srcSYR001-053 whose historical discovery data is unrecoverable by design).

Open verification items carried forward (named, not silent): (1) FLAG-025 - syrlex002 and syrlex007 both cite Griffith 1991 with the mis-pointer '(Source Registry #26, cross-checked)'; srcSYR056 is the citation's true home; the chunk text correction rides the S2.8 render, never a silent patch. (2) The syrlex003 Valavanolickal 2005-vs-2011 printing flag (Doc_03's own open flag) - a row-10 verification item for the pre-freeze re-sweep. (3) srcSYR061's journal language (und, declared). (4) Acts of Miles + Synodicon Orientale - second-order GEDSH apparatus, pre-freeze re-sweep candidates if any chunk comes to cite them directly. (5) Coverage finding routed to S2.2: syrlex005 (memra) and syrlex008 (mar) are Tier-3 chunks with NO Key Sources section - correct for their tier's thin format; their term records must source from front-matter alone.

Pre-freeze re-sweep (2026-07-28): the three S2.1b relative-recall/PRESS findings rowed as srcSYR062-064 (the Acts of Thomas registry-completeness row; the Liber Graduum Excluded row carrying Doc_02 SS1's own decision into the registry; Griffith 1995) - each verification_note declares the work not independently examined this session. The FIVE named coverage limits (BIBP; L'Annee philologique; Oxford Bibliographies; the Hugoye cumulative index; the systematic GEDSH pass) STAND - no database access this session; srcSYR061's journal-language 'und' also stands; saturation is NOT claimed improved beyond the recall-instrument closure. See wrs/migrate/s62_syr_presweep.py.
