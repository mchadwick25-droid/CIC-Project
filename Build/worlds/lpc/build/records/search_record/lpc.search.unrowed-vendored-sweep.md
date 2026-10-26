---
id: lpc.search.unrowed-vendored-sweep
world_id: latin-pastoral-congregational-christianity
record_type: search_record
schema_version: 2
status: draft
register: etic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: null
sources: []
query: Which files already in cic/texts/ bear on lpc (Latin North Africa, c. 246-430) and are neither
  rowed in Source_Registry.md nor given a line in its holdings dispositions table?
channel: 'python -m engine.m9.cli holdings lpc (1,495 vendored files); the lpc corpus map (215 works,
  112 source files) compared by file name with Source_Registry.md and Doc_02; the Registry holdings dispositions
  table (56 files: 42 Out of scope, 14 Deferred); a filename scan of cic/texts/ by author and place words;
  a keyword scan of the other corpus maps for Cyprian, Augustine, Carthage, Hippo and related words. Run
  2026-10-26.'
result: found
found_sources: []
note: 'Result: one real gap, the Hefele English volumes (own record). Corpus map against Registry: 112
  files; all but five are named by file name in the Registry; of those five, npnf103 and npnf105 are named
  by their volume prefix, npnf102 and npnf108 are held in substance by rows 16, 24 and 20 and cited by
  file name in the source records augustine-city-of-god, augustine-on-christian-doctrine and augustine-expositions-on-the-psalms,
  and mansi tomus 2 (Council of Arles, 314) is declared in Doc_02 as having no Registry row. Declared
  non-rows with reasons are listed in the coverage-check document. Not checked: the 1,336 files with no
  coverage entry beyond the filename and keyword scans; the Registry rows 214 to 308 were not re-read
  for accuracy.'
---
The sweep did not edit the Library. Files that need a disposition line, a row or a note are named in the coverage-check document for the lpc build thread.
