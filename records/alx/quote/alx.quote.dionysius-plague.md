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
  divergence_note: null
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
  years: {from: 260, to: 260}
  status: reviewed
reading_card:
  setting: Dionysius, bishop of Alexandria, writing to his churches before Easter during a plague; Eusebius
    quotes it.
  source_says: For Christians the plague was a test. Most nursed the sick and died with them, a death
    'lacking nothing of martyrdom'.
  historians_conclude:
    text: The construction record rates Eusebius's word-for-word quotations, as here, above his own narration.
    confidence: Documented
  contributes: It shows care for the dying as witness, close to martyrdom.
  whose_view: A bishop praising his own flock. He says 'most', not all, and frames the pagans sharply.
  open: McGiffert dates it before Easter 263 and doubts it was a regular festal letter.
  reads_differently_today: '''Brethren'' means the whole community, women and men. It is the translation''s
    period word, not a sign only men nursed.'
  sources:
    setting: alx.source.eusebius-historia-ecclesiastica, HE VII.22.1, npnf201 lines 41017-41030
    source_says: alx.source.eusebius-historia-ecclesiastica, HE VII.22.6-10, npnf201 lines 41058-41110
    historians_conclude: 'Build/worlds/alx/Doc_02_Source_Ecology.md §3.6 (Eusebius: lower risk for verbatim
      quotation of documents); alx.source.eusebius-historia-ecclesiastica, work field; level from alx.quote.dionysius-plague
      confidence.formation_confidence (Documented)'
    contributes: alx.term.martys; alx.term.agape
    whose_view: alx.quote.dionysius-plague, use_note.not_for; alx.story.plague-nursing, absent_detail
    open: McGiffert's note to HE VII.22.1, npnf201 lines 41020-41030; alx.story.plague-nursing, absent_detail
    reads_differently_today: alx.quote.dionysius-plague, modern_lens_note
---
Dionysius's own words on the plague of c. 260 - what the community DID
when death filled the city. This is Eusebius's strong mode (verbatim
document quotation), so the HIGH-risk institutional screen does not
apply; the double transmission (his letter, Eusebius's quotation) is
carried on the sources. Serves F5-I (what did you do when someone was
sick/dying) and F6-P (where was God in suffering - answered by witness,
not theodicy). Verified verbatim.
