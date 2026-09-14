---
id: gallic.search.unopened-volume-sweep
world_id: gallic-monastic-ascetic-christianity
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
query: "Every vendored file under cic/texts/ (per cic/texts/REGISTRY.yaml's 92
  filename entries) whose principal author or subject this world's own build
  documents (Doc_01 World Identification, Doc_02 Source Ecology, Doc_04
  Gravity Discovery, Doc_05 Ecological Reconstruction, Doc_06 Full Lexicon,
  Doc_07 Integrated Ecology Analysis, Doc_08 Forces Document, Doc_09 Story
  Inventory) actually name or discuss, cross-checked against the 44-row
  gallic_Source_Registry.md for any such file never opened or given a row --
  the same shape as the Cappadocian and HAL worlds' own unopened-volume
  sweeps, run for this world instead."
channel: "direct grep of cic/texts/REGISTRY.yaml's 92 filename entries against
  candidate author/subject names, then grepping all nine Gallic world-build
  documents (Doc_01, Doc_02, Doc_04, Doc_05, Doc_06, Doc_07, Doc_08, Doc_09,
  and gallic_Source_Registry.md itself) for each candidate name, 2026-09-10,
  followed by reading each hit in its own surrounding context to confirm or
  clear the match before deciding -- not a keyword count alone."
result: not_found
found_sources: []
note: "NOTHING NEW FOUND SITTING UNOPENED. Every vendored file whose
  principal author or subject this world's own documents actually cite as
  Native or Excluded evidence already has a Source Registry row: the
  Sulpitius/Vincent/Cassian corpus in npnf211 (rows 1-13, 17), Augustine's
  three Gaul-directed anti-Pelagian treatises in npnf105 (rows 14-16), the
  npnf101 letters-gap absence (row 31), Gennadius's own text and Richardson's
  editorial endnote layer in npnf203 (rows 30, 42), Hilary of Poitiers in
  npnf209 (row 33, Excluded), Salvian (row 43), Faustus (row 24), both
  Eucherius works (rows 25-26), Hilary of Arles's Vita Honorati (row 27),
  and Constantius of Lyon's Vita Germani (row 44, Excluded) -- plus the two
  Prosper works and Contra Collatorem, located and rights-checked but not
  yet vendored (rows 28, 29, 32, all honestly disclosed as pending in their
  own rows and in gallic_Source_Registry.md's own document log).
  CANDIDATES CHECKED AND CLEARED, not waved through on a keyword match
  alone: (1) Athanasius/npnf204 -- Doc_01's own row-34 treatment already
  names Vita Antonii as the Excluded Named Comparandum for Sulpitius's
  literary model; npnf204 is 'Select Works and Letters,' not a Vita Antonii
  translation, and no claim in this build's documents draws on npnf204's
  actual contents. Correctly unrowed, not a gap. (2) Jerome/npnf203 and
  npnf206 -- Jerome's own one-line Sulpitius attestation is row 37, Excluded,
  Out-of-Boundary (known only via npnf211's quotation of it, per Doc_02
  SS1.1); Jerome's own De Viris Illustribus chapters inside npnf203 are
  distinct from Gennadius's continuation (row 30) and are not cited by this
  world for anything -- the same kind of adjacent-but-different-author
  material the Cappadocian sweep found inside the same volume for Rufinus.
  Correctly out of scope. (3) Rufinus, inside npnf203 -- not cited by this
  world at all; the only npnf203 content this build uses is Gennadius's
  seven chapters (row 30) and Richardson's endnotes (row 42). (4) Basil,
  Palladius, Origen, Macarius, Julian, Evagrius, Celestine -- each hit
  traced to a false-positive substring ('basilica'), an editorial footnote
  inside an already-rowed volume (Gibson's Palladius note and Heurtley's
  Origen/Newman note inside npnf211, both explicitly marked 'named as
  editorial and not used as source' in Doc_09's own Story Index), a quoted
  ancient-text mention of a figure who has no vendored corpus of his own in
  this world's evidence (Julian Caesar in the Vita Martini narrative; the
  desert fathers Macarius and John as Eucherius names them, row 26; Pope
  Celestine's letter as Gibson's prolegomena report it, not a Celestine text
  in hand), or a cross-world comparison this build's own Doc_07 SS5 draws
  against the already-built desert-monasticism world's text, not a claim
  about this world's own evidence. None points at an unopened, uncited
  vendored file. (5) Benedict/Rule of Benedict -- already row 36, Excluded
  Named Comparandum, correctly named without needing a vendored file (no RB
  text is vendored in cic/texts/ at all). (6) Constantius of Lyon -- already
  row 44.
  NO ADJACENT FINDING of the shape Cappadocian's own sweep surfaced (a
  source cited load-bearing by a sibling document but never given a Registry
  row) turned up here: every candidate this pass checked was either already
  rowed or genuinely out of scope on inspection. This is consistent with,
  not surprising given, gallic_Source_Registry.md's own three full review
  rounds (Round 1, Round 2 substantial-revision, Round 3 bounded spot-check)
  already having hunted specifically for missing sources across three
  successive drafts before this sweep began -- the same reason Cappadocian's
  own B-1a sweep, run after equivalent scrutiny, found only a small residue
  rather than a pile of overlooked volumes. This world's residue is smaller
  still: zero, on this pass."
---
THE SHAPE THIS WORLD'S OWN SWEEP TOOK, run the same way Cappadocian's and
HAL's were and landing at the same "nothing new" result Cappadocian's did.

Three independent adversarial review rounds already ran against
gallic_Source_Registry.md before this sweep began (gallic_Doc02_Review_Round1.md,
gallic_Doc02_Review_Round2.md, gallic_Doc02_SpotCheck_Round3.md), each one
hunting specifically for missing or mishandled sources across three
successive revisions (a Round-1 draft, corrected and expanded through Round
2, then held to a Round-3 bounded spot-check that itself caught two
false-fix claims on unrelated cells). By the time this sweep started, the
obvious misses were already found and fixed by that process, not by this
one -- exactly Cappadocian's own sweep's finding about its own Registry's
history. What a discovery sweep run after that kind of scrutiny should
expect to find is not a pile of overlooked volumes but, at most, a small
residue. This pass found none: every candidate name checked either resolved
to an already-rowed source, an editorial footnote inside an already-rowed
volume, a quoted ancient figure with no vendored corpus of his own in this
world's evidence base, or a cross-world comparison this build's own
documents draw against a different, already-built world's material.

WHY THE NEAR-MISSES MATTERED TO CHECK ANYWAY, even though all of them
cleared. A sweep that only re-confirms what three review rounds already
found clean earns nothing on its own. The Gibson-Palladius and
Heurtley-Origen footnote hits specifically are worth sitting with: both are
inside npnf211, the single volume this world draws the overwhelming
majority of its Native evidence from, and both are places a less careful
pass could have mistaken an editor's own citation for this world's own
voice -- exactly the discipline Doc_02's own preamble (SS0) names as the
failure mode this build has repeatedly had to correct for (Richardson's
endnote layer being mistaken for Gennadius's own ancient words, corrected at
Registry rows 30/42, is the same shape of error). Both were already caught
and marked "editorial, not source" in Doc_09's own Story Index before this
sweep ran; this sweep independently re-confirms that discipline held, not
merely that a keyword search returned hits.

WHAT THIS RESULT MEANS FOR B-1. This world's Source Registry's own
completeness claim -- every source this build's documents cite as Native or
Excluded evidence has a checkpoint row -- is not merely asserted here but
independently tested against the full vendored-text library and found to
hold, with zero residue. B-1's 36 source records and its one world_core
record rest on a Registry this sweep did not find any gap in.
