---
id: cappadocian.search.unopened-volume-sweep
world_id: cappadocian-trinitarian
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
  divergence_note: >-
    One candidate was a homonym worth naming as such, the same shape HAL's own
    sweep already hit on this exact volume: npnf201 (Eusebius of Caesarea's
    Church History) was flagged because Doc_01 names "Eusebius" among Basil's
    correspondents -- but that Eusebius is Eusebius OF SAMOSATA, a distinct
    fourth-century bishop, not Eusebius Pamphili the historian. HAL's own
    unopened-volume-sweep record hit the same file for the same reason with a
    different name (Jerome's own praenomen, Eusebius Hieronymus). Two different
    homonyms, one recurring trap.
sources: []
query: "Every vendored file under cic/texts/ (per cic/engine/texts_registry.py's
  full ENTRIES list, ~50 files) whose principal author or subject this world's
  own build documents (Doc_01 World Identification, Doc_02 Source Ecology,
  Doc_06 Full Lexicon, the G1 Scope and Source Acquisition Manifest) actually
  name or discuss, cross-checked against the 116-row cappadocian_Source_Registry.md
  for any such file never opened or given a row -- the same shape as HAL's own
  unopened-volume-sweep, run for this world instead."
channel: "direct reading of cic/engine/texts_registry.py's ENTRIES list and
  cappadocian_Source_Registry.md's 116 rows, 2026-08-31, cross-checked by
  grepping every Cappadocian world-build document for each vendored volume's
  principal author or subject, then reading the flagged candidates' own
  internal structure (npnf201's and npnf203's div1 headers, read directly, not
  assumed from their filenames) to confirm or clear each match before deciding"
result: not_found
found_sources: []
note: "NOTHING NEW FOUND SITTING UNOPENED. Every vendored file whose principal
  author or subject this world's own documents actually discuss already has a
  Source Registry row: the Basil corpus (rows 5-30), both Gregorys' corpora
  (rows 31-40, 41-56), Gregory Thaumaturgus (rows 66-68), Firmilian of Caesarea
  (row 69), Jerome's De viris illustribus within npnf203 (row 76), the church
  historians Socrates/Sozomen/Theodoret (row 62), the conciliar volume npnf214
  (rows 60, 78), and all nine files this session itself vendored and verified
  directly (rows 18, 21, 22, 33, 48, 57, 63, 71, 72).
  THREE NEAR-MISSES CHECKED AND CLEARED, not waved through on a keyword match
  alone: (1) Hilary of Poitiers (npnf209) -- named twice in Doc_01, but read in
  context both times he is used only as a Western-boundary comparandum ('Hilary
  and the Latin West'; 'Hilary's exiled protest' against Auxentius at Milan) to
  throw this world's own Eastern texture into relief, never as this world's own
  evidentiary voice -- the same treatment Part A already gives Athanasius (row
  1) and the Homoian church (row 64). Correctly unrowed, not a gap. (2)
  Eusebius/npnf201 -- see divergence_note: a homonym, not a hit. (3) Rufinus,
  inside npnf203 -- that volume's own div1 structure (read directly) shows its
  Rufinus material is titled 'Life and Works of Rufinus with Jerome's Apology
  Against Rufinus': the Jerome-Rufinus Origenist-controversy material, already
  the Hieronymian-Ascetic-Literary world's own domain (srcHAL005/srcHAL007 per
  that world's own registry), not this one. Rufinus's own genuine relevance
  HERE -- his 397 Latin translation of Basil's Small Asketikon (already named,
  row 19) and his own continuation of Eusebius' history (books X-XI, covering
  324-395, in-window) -- is real, but neither is what sits inside this vendored
  file, and Rufinus's own history is not vendored anywhere in cic/texts/ at
  all. That is a genuine absence, but an acquisition question, not a discovery-
  sweep miss -- named in the companion coverage-check review's PRESS answer as
  an honorable mention, not claimed here as a found source, since no vendored
  text backs it. ALSO CHECKED, ZERO MENTIONS ANYWHERE IN THIS WORLD'S OWN
  DOCUMENTS, correctly out of scope rather than gaps: Chrysostom (npnf109-114),
  Methodius of Olympus and Novatian (both in anf06/anf05), Dionysius of
  Alexandria (anf06). Origen's own corpus (anf04, anf09) was checked too: it
  belongs to the registered Alexandria world by the same logic Part A's row 1
  already applies to Athanasius -- only the Cappadocian compiling act itself
  (the Philocalia, row 81) is this world's own evidence, and that is already
  rowed. ONE ADJACENT FINDING, outside this record's own query but surfaced by
  the same pass and worth naming plainly rather than filing separately and
  silently: Gregory of Nyssa's Life of Moses is cited three times as a Key Text
  in Doc_06 (akatalepsia, epinoia/energeia, epektasis) and was explicitly named
  as a real, still-open gap in the G1 manifest's own 'honest gaps' list --
  yet is the ONE item on that same gap list that never received
  a Source Registry row, while every other item on it did (Against Eunomius ->
  row 24; the Small Asketikon -> row 19; Ad Graecos -> row 54; Eunomius' 383
  confession -> row 59; Epiphanius/Amphilochius -> rows 61/65; Nicaea
  subscription lists -> row 77; the Theodosian Code provisions -> rows
  73/79/80). This is not a vendored-but-unopened file (it was never vendored at
  all), so it does not belong in found_sources here, but it is exactly the kind
  of gap this sweep exists to surface and is carried into the companion
  coverage-check review's PRESS answer rather than left unmentioned."
---
THE SHAPE THIS WORLD'S OWN SWEEP TOOK, run the same way HAL's was and landing
differently.

HAL's sweep found three volumes worth opening among twelve candidates because
that world's own list was built mechanically (every volume of an author HAL
already opens elsewhere) and needed the sharper question "does this specific
volume answer something this world asks and cannot otherwise answer." This
world's list was different in kind: three rounds of independent adversarial
review already ran against the Source Registry before this sweep began (see
CAPPADOCIAN_BUILD_LEDGER.md SS10), each one hunting specifically for missing
sources across three successive drafts (99 -> 112 -> 116 rows). By the time
this sweep started, the obvious misses were already found and fixed by that
process, not by this one. What a discovery sweep run AFTER that kind of
scrutiny should expect to find is not a pile of overlooked volumes but, at
most, a small residue -- and that is what turned up: zero vendored-but-unrowed
files, three near-misses that needed checking rather than assuming, and one
real gap that was never about a vendored file in the first place.

WHY THE NEAR-MISSES MATTERED TO CHECK ANYWAY, even though all three cleared.
A sweep that only re-confirms what three review rounds already found clean
earns nothing. The Eusebius/npnf201 homonym specifically is worth sitting with:
it is the SAME FILE that tripped HAL's own sweep, for the same underlying
reason (a name inside this world's own text matching a different, unrelated
historical Eusebius) but a different specific name doing the tripping. That is
not a coincidence worth ignoring -- "Eusebius" is simply a common enough late-
antique name that any keyword-only check against npnf201 will misfire close to
every time it is run, for whichever world runs it. A tool built to automate
this kind of sweep in the future should know that going in, not rediscover it
per world.

WHAT THE ONE ADJACENT FINDING MEANS FOR THE REGISTRY, stated plainly rather
than softened. The Source Registry's own checkpoint promise is that "every
source Doc_02 SSSS1-6 and Doc_01 name has a row." Doc_02 itself never names
Life of Moses (confirmed by direct grep -- zero matches), so the Registry's own
stated completeness rule was not technically broken. But Doc_06, a document
that exists and was built using this world's own sources, names it three times
as load-bearing for Tier 1/2 lexicon entries, and the G1 manifest already
flagged it by name as a real omission a full day before the Registry was even
drafted. A Registry that is complete relative to Doc_02 alone but silent on a
source its own sibling document leans on three times is not fully complete in
the sense a working bibliography needs to be, whatever its own checkpoint
literally required. That gap is named here and carried to the coverage-check
review's PRESS answer, not resolved by this record -- acquisition is a
pre-freeze re-sweep matter, not a B-1a discovery-sweep matter.
