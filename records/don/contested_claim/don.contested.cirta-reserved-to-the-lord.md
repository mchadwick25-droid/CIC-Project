---
id: don.contested.cirta-reserved-to-the-lord
world_id: donatism
record_type: contested_claim
schema_version: 2
status: draft
register: etic
canon_cells:
- F1-I
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: null
sources:
- source_id: don.source.optatus-against-donatists
  locus: Against the Donatists I.14 (cic/texts/optatus_against-the-donatists.txt, lines 181-192) -- the
    narrated account
  license: public-domain
- source_id: don.source.optatus-appendix-of-documents
  locus: the Acts of the Council of Cirta (305) themselves, part of Optatus's own Appendix, the documentary
    layer the narration in Book I draws on
  license: public-domain
relations:
- type: associated-with
  target: don.gravity.ministerial-purity
claim: 'The Council of Cirta''s (305) ''reserved to the Lord'' ruling on the traditor question -- no one
  present found guilty, no one cleared -- was an act of evasion: an implicit admission of guilt the assembled
  bishops declined to name outright, exactly as Optatus tells the story to argue.'
held_against:
- This world's own later tradition would plausibly describe the same ruling differently -- as an act of
  mercy, or of realistic humility about what could actually be verified under the conditions the Diocletianic
  persecution had just imposed -- rather than as a cover for guilt (Story-Chunks/donstory007_council-of-cirta.md,
  Usage Guidance).
- 'The bare sequence of events does not itself establish evasive intent: three bishops not themselves
  accused (Victor of Garba, Felix of Rotarium, Nabor of Centurio) were specifically the ones asked for
  judgment and specifically the ones who recommended reservation -- a structural detail at least as consistent
  with a considered judicial choice (no untainted judge present felt able to rule on an unverifiable charge)
  as with collective evasion by the interested parties themselves.'
- The only surviving account of this council is Optatus's own (Against the Donatists I.14) -- this world's
  own later opponent, telling the story specifically to argue that the movement's founders were traditores
  absolving one another. No Donatist-authored or Donatist-voiced account of this specific council survives
  to confirm any alternative reading of the ruling's own meaning directly.
concedes: 'The bare facts of what happened at Cirta are Documented and not in dispute: the council met;
  the traditor question was put to those gathered; several admitted responsibility; Purpurius''s counter-taunt
  against Secundus; the nephew''s advice to remit the matter to God; the three unaccused bishops'' own
  judgment that the case ought to be reserved to the Lord; Secundus''s ''Sit down, all''; the assembly''s
  ''Thanks be to God'' in response; no verdict either way. What is genuinely contested is not any of this
  sequence but its own MEANING -- evasion, as Optatus''s own hostile frame has it, or principled restraint,
  as this world''s own plausible alternative reading has it -- and this record does not resolve that question,
  since no surviving Donatist-authored account of this council exists to settle it either way (matching
  donstory007''s own Usage Guidance precisely: ''the Representative should be prepared to sit with that
  complication rather than resolve it toward whichever side is more comfortable'').'
divergence_partners:
- don.source.optatus-against-donatists
- don.source.optatus-appendix-of-documents
use_note:
  means: "Whether the 305 Cirta ruling to reserve the traditor question to the Lord was evasion, as Optatus tells it, or mercy or humility about what could be verified, is contested."
  not_for:
    - "a claim that the ruling was plainly an implicit admission of guilt"
    - "a claim that the ruling is settled as an act of mercy or humility"
  years: {from: 305, to: 305}
  status: provisional
---
Re-derived from Story-Chunks/donstory007_council-of-cirta.md, read in full this session -- its own Formation Ecology Connection section already ties this material directly to G1 ('Ministerial Purity / Traditor-Free Sacramental Validity... but as a complicating case rather than a simple illustration'), and its own Usage Guidance already states this exact contest ('Optatus's own characterization... should not be adopted uncritically... while being honest that no surviving Donatist-authored account of this specific council exists to confirm that alternative reading directly') -- this record gives that already-argued contest its own dedicated contested_claim treatment rather than leaving it inside a story chunk's own Usage Guidance prose, per this step's own launch brief. relations[] carries one gravity edge (G1) named in this script's own docstring under RECIPROCITY. Distinct from don.contested.circumcellion-character: a different council, a different sole source (Optatus alone, no CTh 16.5.52 or Registry-row-24 material involved), and a different kind of contest (what a specific ruling MEANT, not a group's own character and scale) -- not a duplicate treatment of the same underlying material. Does not touch Article 29 Limb 2: Optatus is not one of the two figures (Cyprian, Augustine) that gate names, and the ruling's own meaning is not a present-day-tradition-mediation question.
