---
id: don.story.gesta-apud-zenophilum
world_id: don
record_type: story
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: don.source.optatus-appendix-of-documents
  locus: Gesta apud Zenophilum; cic/texts/optatus_against-the-donatists.txt, lines 6194-6880
  license: public-domain
- source_id: don.source.augustine-donatist-correspondence-eleven-letters
  locus: Letter XLIII, corroborating Nundinarius's own disclosure; cic/texts/npnf101_augustine-confessions-letters.xml,
    lines 28040-28069
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks for this tradition's most documentary, least narrated evidence -- an actual court
    transcript rather than a later narrative account
  - participant asks whether the traditio-era financial disputes were ever formally investigated
  - conversation needs a story corroborated by two independent sources rather than one
  do_not_retrieve_when:
  - participant wants the earlier, more narrative account of how the dispute first arose (don.story.lucilla-consecration-dispute
    is the origin story this proceeding investigates)
  - participant is asking about the forgery investigation into Felix of Aptungi specifically (don.story.acta-purgationis-felicis
    covers that separate 314 proceeding)
relations:
- type: associated-with
  target: don.story.lucilla-consecration-dispute
- type: associated-with
  target: don.figure.lucilla
- type: associated-with
  target: don.figure.optatus
narrative_tier: 1
narrative_tier_justification: 'Tier 1 at its strongest available in this corpus (Doc_09 SS3): a literal
  court transcript, named deponents, a precise date (320), and a historically credible claim independently
  corroborated by a second primary source (Augustine''s Letter XLIII) written from the opposing side,
  decades later, with no evident coordination between the two accounts (Story-Chunks/donstory005, Tier
  Justification).'
tellable_as: The formal inquiry into what happened to Lucilla's money, seven years after the fact
text: 'In 320, before the consular official Zenophilus, a formal inquiry was opened into what had actually
  happened to the church''s own money.


  Witnesses were called and questioned directly, under record: Nundinarius, a deacon; Saturninus; Victor;
  Castus; Crescentianus. The specific question Zenophilus put to them was pointed and financial, not doctrinal
  -- had four hundred pieces of silver, received from Lucilla, actually reached the poor, as had been
  claimed, or had it gone elsewhere?


  The transcript preserves the exchange as it happened: names given, questions asked, answers recorded.
  This is not a later writer''s summary of what he understood to have occurred; it is the proceeding itself,
  set down as it was heard.


  Decades afterward, Augustine would refer back to this very episode in a letter of his own, recalling
  that Nundinarius, the same deacon, "in the heat of passion revealed many secrets," among them that the
  founding of a rival altar in Carthage had been made possible by money that had come from Lucilla. Two
  witnesses, writing on opposite sides of the schism and decades apart, describe the same underlying fact.'
absent_detail: None beyond what the transcript itself does not cover -- the proceeding does not explain
  why the money was misapplied in the first place, only that it was investigated and that a deacon later
  admitted knowledge of it.
modern_contrast: A modern reader might assume ancient religious disputes left no paper trail beyond one
  side's own later argument. This proceeding is the opposite -- a formal, cross-examined transcript, corroborated
  decades later by a hostile witness who had every reason to let the matter drop and did not.
---
Mapped directly from Story-Chunks/donstory005_gesta-apud-zenophilum.md. citation_specificity/verification_state held at A/verified-direct, matching the chunk's own 'among the strongest Tier 1 candidates' framing and its own corroboration claim.
