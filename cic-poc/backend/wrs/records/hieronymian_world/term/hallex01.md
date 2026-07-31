---
id: hallex01
world_id: hieronymian-ascetic-literary
record_type: term
schema_version: 1
jobs:
- 1
- 2
- 4
- 6
register: emic
review_state: draft
cache_stability: static
term: Hebraica veritas
aliases:
- Hebrew truth
- Hebrew textual authority
quick_meaning: The conviction that the Hebrew text of scripture, not the Greek translation long used in
  Latin worship, carries the truth closest to what God actually said.
world_meaning: 'To hold to *Hebraica veritas* is to believe that when the word given to Moses or the prophets
  passed from Hebrew into Greek, something of its precision was lost — not through malice, but through
  the ordinary friction of moving between tongues — and that a scholar who returns to the Hebrew recovers
  what the Greek, however venerable, cannot fully carry. This conviction does not despise the Greek; the
  Greek is loved and known and quoted constantly. But when the two disagree, the Hebrew is heard first.
  This is costly to hold: it means telling a congregation used to one word (a gourd, shading a prophet)
  that the word is now another (a climbing vine), and bearing the anger that follows. It means years spent
  with a teacher who does not share the faith the labor serves, because only such a teacher can supply
  what is needed. It means answering, again and again, the charge of tampering with what the church already
  trusts. To hold *Hebraica veritas* in this world is to have chosen a harder, more contested truth over
  an easier, more settled one, and to keep choosing it under real pressure.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: Anchors G1 (Primary gravity); the organizing commitment behind
  the whole translation project (*Vulgata*); the direct cause of the Augustine correspondence and the
  Oea controversy; presupposed by every commentary produced at Bethlehem.'
distortion_risk: '**Modern Hearing:**

  A modern participant is likely to hear this as a straightforwardly correct scholarly method — "of course
  you translate from the original language" — and miss that it was a genuinely contested, destabilizing
  position in its own time, resisted by serious churchmen (Augustine) for serious reasons (continuity
  of the church''s received text), not merely by the ignorant or the reactionary.


  **World Hearing:**

  This world heard *Hebraica veritas* as a claim with real stakes for the church''s continuity and unity,
  not a neutral methodological improvement — adopting it meant accepting that a translation the whole
  Latin church had prayed and preached from for generations had drifted from its Hebrew source and needed
  to be tested against it.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about the Vulgate/translation project
  - participant asks why Jerome used Hebrew instead of Greek/Septuagint
  - conversation reaches the Augustine correspondence or the Jonah "gourd/ivy" controversy
  - participant asks about biblical translation authority generally.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this term in the current turn
  - condition_type: anachronism-guard
    text: participant is asking about a modern translation-theory question unrelated to this world's own
      controversy.
  force_llm_vote: false
sources:
- source_id: srcHAL009
  author_gravity_note: 'Jerome''s own prefaces (*Praefatio*) are the primary source for the principle''s
    articulation; the Jerome-Augustine correspondence (Ep. 112 = Augustine''s Ep. 75) for its contest;
    the Oea "ivy/gourd" incident (Jonah 4:6) for its concrete cost. Author Gravity note: the principle''s
    own articulation survives almost entirely in Jerome''s voice; its contestedness is independently attested
    via Augustine, but its content is not.'
period_sense: 'The conviction that the Hebrew text of scripture, not the long-used Greek, carries the
  truth closest to what God said - held not as neutral method but as a costly, actively contested commitment:
  it meant years with a Hebrew teacher outside the faith, telling congregations that a familiar word was
  now another, and answering, repeatedly, the charge of tampering with what the church already trusted
  (chunk Quick/World Meaning).'
prior_sense: 'The contrast object is the church''s own received practice: the Greek translation ''long
  used in Latin worship'' - venerable, loved, constantly quoted - whose authority the phrase deliberately
  relativizes (chunk World Meaning). As a fixed two-word phrase it is this world''s own polemical coinage,
  not a transformed inheritance - a builder note, UNVERIFIED against this build''s own docs, which do
  not develop the phrase''s history.'
modern_sense: '''Of course you translate from the original language'' - heard as a straightforwardly correct
  scholarly method, with the period resistance filed under ignorance or reaction (chunk Modern Hearing).'
conceptual_distance_note: 'The modern ear hears settled method; this world heard a claim with real stakes
  for the church''s continuity - serious churchmen (Augustine) resisted it for serious reasons, and adopting
  it meant conceding that the text the whole Latin church prayed from had drifted from its source (chunk
  World Hearing). Sharp gap: high grounding criterion by rule.'
semantic_domain: hebrew-textual-authority
grounding_criterion: high
voice_surface: To hold to the Hebrew truth is to believe that when the word passed from Hebrew into Greek,
  something of its precision was lost - and that a scholar who returns to the Hebrew recovers what the
  Greek, however venerable, cannot fully carry. We did not hold this comfortably. It cost us a teacher
  hired from outside our faith, the anger of congregations over a gourd become a vine, and the standing
  charge of tampering with what the church already trusted.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: presupposed-by
  target_id: hallex02
  note: 'The translation project is this principle''s material product (hal_lex02''s own EF: ''The material
    product of Hebraica veritas''). Chunk Ecological Function (verbatim, absorbed per FLAG-002): Anchors
    G1 (Primary gravity); the organizing commitment behind the whole translation project (*Vulgata*);
    the direct cause of the Augustine correspondence and the Oea controversy; presupposed by every commentary
    produced at Bethlehem.'
- type: presupposes
  target_id: hallex13
  note: The prefaces are 'where the Hebraica veritas commitment is actually argued, book by book, not
    merely asserted' (hal_lex13 World Meaning) - the Desert material-source-of/presupposes pairing; srcHAL023
    is the corpus row.
- type: presupposes
  target_id: hallex12
  note: The classical grammar training 'is what made the later philological labor possible at all' (hal_lex12
    World Meaning) - the documented foundation under the contested Hebrew-fluency claims.
- type: associated-with
  target_id: hallex07
  note: 'The Augustine dispute over this principle was ''conducted'' as letters (hal_lex07 World Meaning:
    ''a furious exchange with a former friend turned theological opponent''; srcHAL009) - association,
    no hierarchy (CO-P2-13 pattern); symmetric mirror on hallex07.'
- type: associated-with
  target_id: hallex08
  note: 'Symmetric mirror of hallex08''s edge: the Origenist rupture ''reshapes the Hebraica veritas project''
    (hal_lex08 EF) - the Augustine dispute is its downstream test.'
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex01_hebraica-veritas.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.
