---
id: don.contested.bishop-count-411-conference
world_id: donatism
record_type: contested_claim
schema_version: 2
status: ready
register: etic
canon_cells:
- F2-E
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: null
sources:
- source_id: don.source.migne-pl11-collatio-carthaginiensis
  locus: 'cic/texts/pl11-zeno-optatus-collatio-carthaginiensis_migne.txt, line 73363: ''...licis 286,
    et ex Donalislarum parte 279'''
  license: public-domain
- source_id: don.source.gesta-collationis-carthaginiensis
  locus: the acts' own numbered interventions (e.g. acts 20, 24, 26, 50, 99, 108, 121, 253, 266, 268,
    Emeritus's own recorded interventions), the transcript this tally summarizes
  license: public-domain
relations:
- type: associated-with
  target: don.gravity.parallel-hierarchy
claim: 'The 411 Conference of Carthage''s own bishop count is a simple, settled fact, available without
  complication directly from the *Gesta*''s own text: 279 Donatist bishops seated against 286 Catholic.'
held_against:
- This figure was not settled through most of this world's own construction history. An unverified '284
  Donatist' figure propagated silently since this world's earliest construction document (Step0_Movement_Scope_Confirmation.md,
  written before the Gesta Collationis Carthaginiensis itself was vendored) through Doc_01, Doc_02, Doc_04,
  Doc_05, Doc_07, Doc_08, Doc_09, Lexicon-Chunks/donlex015, and multiple Representative-phase documents,
  never checked directly against the primary source before this correction.
- The corrected figure rests on one located tally, at one line (73363) of a 19th-century Migne scan this
  world's own Registry independently flags as 'notably poor OCR quality even by this corpus's own standards'
  -- legible despite that, but not a manuscript-certain reading placed beyond all doubt by the correction
  alone.
- The located tally ('...licis 286, et ex Donalislarum parte 279') is Migne's own editorial/summary apparatus
  surrounding the acts, not necessarily the acta's own verbatim tally list -- a distinction Doc_02 SS1's
  own correction paragraph carries explicitly as a caveat, not one the correction itself resolves away.
concedes: '279 Donatist against 286 Catholic is the best-attested figure available and the one every current
  site in this world''s own build now carries. The correction away from 284 is not itself in serious doubt:
  the scan''s ''Donalislarum'' is a recognizable, checkable OCR error for ''Donatistarum,'' not a guess,
  and the 286 Catholic figure was already correct throughout. What remains genuinely open is only the
  finer-grained certainty the ''simple, settled fact'' framing implies -- this is the one located tally,
  from an editorial apparatus, on a scan of independently-flagged poor quality, not a cross-checked or
  independently-corroborated figure the way, for example, the Deo laudes acclamation''s own epigraphic
  text is.'
divergence_partners:
- don.source.migne-pl11-collatio-carthaginiensis
- don.source.gesta-collationis-carthaginiensis
use_note:
  means: "The best-attested reading seats 279 Donatist and 286 Catholic bishops at the 411 Conference, but rests on one editorial tally from a poor scan."
  not_for:
    - "a claim that the earlier 284 Donatist figure is correct"
    - "a claim that the figure is cross-checked or independently corroborated"
  years: {from: 411, to: 411}
  status: reviewed
---
Re-derived from Doc_02_Source_Ecology.md SS1's own 'Bishop-count correction at the 411 Conference' paragraph and don_Decision_Log.md's own 'World-build bishop-count correction (284 -> 279)' entry (grepped by header, not read in full at 745 lines -- the relevant paragraphs were read in full). relations[] carries the one gravity edge (G4, don.gravity.parallel-hierarchy) named in this script's own docstring under RECIPROCITY -- G4's own manifestations[] field already states this corrected figure directly. This record does not touch Cyprian, Augustine, or the rebaptism question, and does not bear on Article 29 Limb 2 in any way -- see this script's own docstring, THE TWO RESERVED QUESTIONS, item 2.
