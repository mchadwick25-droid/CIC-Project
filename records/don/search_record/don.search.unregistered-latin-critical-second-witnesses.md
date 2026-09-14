---
id: don.search.unregistered-latin-critical-second-witnesses
world_id: donatism
record_type: search_record
schema_version: 2
status: draft
register: etic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: Both files are genuinely usable, in-scope second-witness resources per cic/texts/INTAKE.md's
    own convention (an original-language critical edition cross-checking, never replacing, an already-Native
    English translation) -- but neither has been read for any specific Donatism claim, and neither yet
    has a Source_Registry.md row of its own, so this record's own formation_confidence stays at Widely
    Accepted rather than Documented for the underlying works themselves (Cyprian's corpus; Augustine's
    letters), which this world's OTHER, English-translation rows already carry at a higher confidence
    where directly read.
sources: []
query: Every file under cic/texts/ that is Donatism-relevant on its face but cited by NEITHER a Source_Registry.md
  row nor a cic/corpus-map/donatism.yaml entry -- the second of B-1's two named discrepancies (wb_don_s21.py's
  own docstring, "DISCREPANCIES" item 4)
channel: Direct `ls cic/texts/` plus this session's own read of each candidate file's own provenance header
  and content, cross-checked against Source_Registry.md's full table and cic/corpus-map/donatism.yaml
  by grep
result: found
found_sources: []
note: 'TWO FILES, BOTH GENUINE, BOTH STILL UNREGISTERED. (1) cyprian_opera-omnia-critical_hartel-csel3-pars1-2.txt
  -- Wilhelm Hartel''s critical Latin edition (CSEL 3, Pars I-II, 1868/1871), covering the treatises through
  the Sententiae Episcoporum (the 87 bishops'' sentences at the 256 Council of Carthage) and Epistulae
  I-LXXXI in full. This is the Latin original standing behind the ANF English translation Source_Registry.md
  rows 7-11 already cite as Native for the rebaptism-precedent and traditio/lapsed-clergy background --
  a second-witness apparatus for material this world already draws on, per its own provenance header,
  not a new primary claim. (2) augustine_epistulae-critical_goldbacher-csel57-pars4.txt -- Alois Goldbacher''s
  critical Latin edition (CSEL 57, 1911), covering Epistulae 185-270 -- a range that DIRECTLY INCLUDES
  Letter 185 (Source_Registry.md row 5, The Correction of the Donatists), already Native via the vendored
  NPNF English translation. This file''s own provenance header states the second-witness caveat explicitly:
  never primary evidence on its own, only for cross-checking a specific reading against the NPNF translation
  this world''s own records actually cite. NEITHER FILE HAS BEEN READ for any specific claim by any session
  to date, and neither has a Registry row of its own -- this sweep''s own disposition is that BOTH belong
  in a future Doc_02/Registry revision pass, as edition-level rows paralleling rows 38 (Ziwsa/Optatus),
  39 (Petschenig/Augustine-contra-Donatistas), and 51 (Mommsen-Meyer/Codex Theodosianus) -- not created
  here, since minting a new Source_Registry.md row is that document''s own act, out of this record-native
  authoring step''s own scope (records/don/source/ is not touched by this sweep).'
---
The DISCREPANCIES section of wb_don_s21.py's own docstring separately names three OTHER corpus-map entries with no Registry row (Contra Fulgentium Donatistam, De Baptismo's Latin critical text, De Unico Baptismo contra Petilianum) -- those already have a corpus-map entry, unlike the two files named here, which have neither a Registry row NOR a corpus-map entry; that separate, smaller gap is left as B-1's own docstring already named it, not re-litigated by this sweep.
