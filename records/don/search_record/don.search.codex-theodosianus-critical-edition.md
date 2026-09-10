---
id: don.search.codex-theodosianus-critical-edition
world_id: don
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
query: 'Th. Mommsen and Paul M. Meyer''s critical Latin edition of the Codex Theodosianus, Book 16 (Theodosiani
  Libri XVI cum Constitutionibus Sirmondianis, Berlin: Weidmann, 1905) -- specifically law 16.5.52 (the
  circumcelliones fine clause) and the term agonistici'
channel: 'Mark''s manual archive.org-download-and-DOCX-upload channel, five attempts, 2026-09-01 (Source_Acquisition_Manifest.md
  SS1 G3; don_Decision_Log.md, "G3 acquisition attempts, five tried, none vendored"); direct network fetch
  from archive.org''s own download endpoint once this build''s outbound network access was confirmed working,
  2026-09-07 (don_Decision_Log.md, "New session: network access confirmed working")'
result: found
found_sources:
- don.source.mommsen-meyer-theodosiani-libri-xvi
- don.source.codex-theodosianus-book-16
note: 'FIVE ATTEMPTS FAILED, THEN SUCCEEDED. Attempt 1 and attempts 3-5 all resolved to the same wrong
  item, `theodosianilibri02code` -- Mommsen''s own Prolegomena in Theodosianum (Vol. I, Pars Prior: manuscript-tradition
  and textual-critical apparatus), not Book 16''s own legal text; no agonistici/circumcelliones material
  and no 405 Edict of Unity found in it. Attempt 2 was a DOCX from a site calling itself "sourcelibrary.org"
  (self-described as serving "scholars, seekers and AI systems"): rejected outright, not on licence grounds
  alone -- it was an English paraphrase with inline glosses, not a transcription of the Latin critical
  edition, licensed CC BY-SA 4.0 (not public domain), and carried a long run of invisible zero-width Unicode
  characters embedded after nearly every paragraph, which the site''s own front matter labelled a hidden
  "provenance mark." STANDING CAUTION, named in don_Decision_Log.md itself for this and future worlds''
  acquisitions: sourcelibrary.org (and any similarly self-described "for AI systems" text-processing intermediary)
  should not be used as a vendoring source, independent of its licence terms, given this embedded hidden-character
  payload -- a build-process/security caution, not a Donatism-content one, so carried here rather than
  duplicated into world_core.cautions. G3 was PAUSED, not discharged, after these five attempts (Boyd
  1905 substituted in the meantime -- see don.search.boyd-theodosian-code-substitute). SUCCESS, 2026-09-07:
  once this build''s own outbound network access was confirmed working (tested directly against archive.org
  before anything else that session), the correct item -- `theodosianilibr01sirmgoog`, Voluminis I Pars
  Posterior: Textus cum Apparatu -- was located and fetched directly. All 16 Books confirmed present,
  Book XVI located, and law XVI.5.52 (headed "412 Ian. 30") read in full and confirmed to contain "circumcelliones
  argenti pondo decem" verbatim -- a graduated fine schedule by social rank, Circumcellions assessed a
  silver (not gold) fine unlike every other rank. The agonistici self-designation term was independently
  searched for directly (zero matches) and confirmed NOT Theodosian Code vocabulary -- its own source
  passage remains unidentified, a smaller, still-open item (Doc_02 SS9).'
---
Read together with don.search.boyd-theodosian-code-substitute (a separate, independent discovery episode -- a different search, for a different work, run while this one was still unresolved). Untried leads named in the Manifest and never needed once the correct item was found: `theodosianilibri0002unse`, `theodosianilibri00codeuoft`, the Gothofredus 17th-century edition (BRes1409271-1409277).
