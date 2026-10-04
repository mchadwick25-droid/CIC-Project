---
id: alx.quote.dionysius-plague
world_id: alexandria-catechetical
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F5-I
- F6-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Eusebius quotes the letter but gives no year. The date, shortly before Easter 263, is the NPNF editor's inference in his note on VII.22.
sources:
- source_id: alx.source.eusebius-historia-ecclesiastica
  locus: VII.22 (npnf201 lines 41084-41090; Dionysius's festal letter quoted verbatim by Eusebius)
  license: public-domain
- source_id: alx.source.dionysius-extant-fragments
  locus: 'the same letter, in a different translation, in the collected fragments - ANF06
    Epistle XII, lines 11396-11545, carries a differently worded translation of this
    passage, e.g. "Certainly very many of our brethren... did not spare
    themselves, but kept by each other, and visited the sick" vs. the npnf201
    wording quoted in text'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what happened in an epidemic and what Christians did"
  - "participant asks how they cared for the dying and buried the dead"
  - "participant asks what outsiders noticed about their behaviour in a crisis"
relations:
- type: associated-with
  target: alx.story.plague-nursing
text: The most of our brethren were unsparing in their exceeding love and brotherly kindness. They held
  fast to each other and visited the sick fearlessly, and ministered to them continually, serving them
  in Christ. And they died with them most joyfully, taking the affliction of others, and drawing the sickness
  from their neighbors to themselves and willingly receiving their pains.
modern_rendering: >-
  Most of our people held nothing back in their overflowing love and
  kindness toward one another. They stayed close to each other, visited
  the sick without fear, and cared for them continually, serving them in
  Christ. And they died alongside them most joyfully. They took on
  others' suffering, drawing the sickness from their neighbors onto
  themselves, and willingly taking on their pain.
speaker_or_author: alx.figure.dionysius
license: verbatim
modern_lens_note: >
  Mild risk: 'brethren' is this translation's period-standard rendering for
  the whole community, not a claim that only men are in view - the same
  translation-convention note as dionysius-nepos.
use_note:
  means: "Dionysius's festal letter, quoted by Eusebius at VII.22, says most Christians fearlessly nursed the plague-sick and died with them, taking on their sickness."
  not_for:
    - "a claim that every Christian stayed, when Dionysius says 'the most of our brethren'"
    - "a theodicy explaining why God allowed the plague"
    - "an outsider's report, when this is the bishop praising his own flock"
  years: {from: 262, to: 263}
  status: reviewed
---
