---
id: cappadocian.term.koinonia
world_id: cappadocian-trinitarian
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: The anti-solitary argument and the communal institution's existence are Documented
    via the Asketikon's own text (verified-direct). What is not attested at the same strength is the lived
    day-to-day interior of any specific house -- inferential beyond what the legislation itself describes
    -- and the Life of Macrina's own presentation carries Gregory's deliberate literary framing (flagged
    at that source's own record).
sources:
- source_id: cappadocian.source.basil-asketikon-longer-shorter-rules
  locus: the Longer Rules' argument against the solitary life
  license: public-domain
- source_id: cappadocian.source.gangra-canons
  locus: the disorder the ordering answered
  license: public-domain
- source_id: cappadocian.source.gregory-nyssa-life-of-macrina
  locus: the household become community -- Gregory's own presentation
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - monasticism, community, or whether faith can be private
  - why these people lived together or held goods in common
  - the hermit ideal versus community
  prefer_instead:
  - the question is specifically about the poorhouse and charity -- retrieve philoptochia/Basileias instead
relations:
- type: associated-with
  target: cappadocian.term.adelphotes
- type: associated-with
  target: cappadocian.term.askesis
- type: associated-with
  target: cappadocian.term.basileias
- type: associated-with
  target: cappadocian.term.eikon
- type: associated-with
  target: cappadocian.term.hesychia
- type: associated-with
  target: cappadocian.term.kanon-kanonikai
- type: associated-with
  target: cappadocian.term.philoptochia
plain_meaning: We taught that people are made for life together, not for life alone. Even the
  strictest renunciation of the world was ordered into community. Ascetics prayed together, worked together,
  and held goods in common. They kept a door open for guests.
world_word: koinōnia
false_friend:
- '''community'' as a warm but optional add-on to private faith'
- monasticism as an escape from other people
- shared life as small-group socializing
senses:
  informational: 'This world''s anthropology is unashamedly social: the human being is a communal creature,
    and the solitary life fails not because it is too hard but because it has no one to serve -- whose
    feet will you wash alone, the Rules ask, and how will you learn humility with no one to obey? So renunciation
    itself was ordered into brotherhoods and sisterhoods with a common table and a guest-door.'
  evidential: The anti-solitary argument is Documented as Basil's own, in the Asketikon's Longer Rules;
    the communal institution's real existence is Documented. What is not attested at the same strength
    is the lived day-to-day interior of any specific house -- inferential beyond what the legislation
    itself describes, and the Life of Macrina's own presentation carries Gregory's deliberate literary
    framing (flagged at that source's own record).
  personal: The radicals censured at Gangra were not condemned for wanting holiness -- they were condemned
    for seceding from the common body to get it. For this world, holiness pursued alone, against the church's
    own fellowship, had already missed the point of holiness.
  translational: '''Isn''t community just one style of religious life among others, and the solitary hermit
    another equally valid one?'' -- this world ranked them: the shared table, common goods, and a door
    for guests were the shape salvation itself was believed to take, not one lifestyle option next to
    another.'
quick_meaning: Communion, or common life. The shared life we believed every person is made for.
distortion_risk: high
use_note:
  means: "Koinonia meant common life, the belief that people are made for life together, so even strict renunciation was ordered into community."
  not_for:
    - "community as an optional add-on to private faith"
    - "the Gangra radicals as condemned for seeking holiness, when the charge was seceding from the common body"
    - "the lived interior of any one house, which the legislation does not describe"
    - "the brotherhood as an institution, which sits in cappadocian.term.adelphotes"
  years: {from: 340, to: 379}
  status: reviewed
---
Built from Doc_06 entry 6 (Tier 1). RECONCILIATION (this pass): the built deployment chunk cappadocianlex003_koinonia.md carries a stale Related-Terms line ('...hesychia, eusebeia') that Doc_06 itself flags as drifted from its own current entry (Master Index derivation note: 'lex003 has drifted... flagged for reconciliation at chunk production'). This record's relations[] are authored from Doc_06 Index E row 6's current, correct list -- adelphotes, askesis, philoptochia, hesychia, kanon-kanonikai (T3), eikon, Basileias -- not from the stale chunk.
