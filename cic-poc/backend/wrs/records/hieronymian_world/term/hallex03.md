---
id: hallex03
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
term: Renuntiatio
aliases:
- Renunciation
quick_meaning: The formal, voluntary giving-up of wealth, marriage prospects, and worldly status as an
  act of Christian devotion.
world_meaning: 'To renounce, in this world, was not a single gesture but a sustained unmaking of one''s
  former position — the sale or redirection of inherited property, the closing-off of the marriage that
  would have secured a family''s alliances, the plain dress that announced, to anyone who had known the
  person before, that something fundamental had changed. It was not private. A senator''s daughter who
  renounced was seen to renounce, by family who protested, by a Rome that judged, by a church that both
  praised and, sometimes, suspected the praise itself of excess. Renunciation in this world was public,
  costly, and, in more than one telling, taken further than the body could comfortably sustain — grief
  and material need followed those who gave the most.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: Anchors G2 (Primary gravity); the material source of *patrocinium*;
  presupposed by *xenodochium* and *nosocomium*; central to *virginitas* and *vidua* as their practical
  expression.'
distortion_risk: '**Modern Hearing:**

  Likely to read renunciation as a private spiritual discipline, comparable to modern voluntary simplicity
  or minimalism.


  **World Hearing:**

  A public, family-disrupting, socially contested act with real material and relational costs, not a private
  lifestyle choice.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks why Paula/Eustochium/Fabiola gave away their wealth
  - participant asks about ascetic renunciation generally.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: 'Ep. 108 (Paula), Ep. 22 (Eustochium), Ep. 77 (Fabiola). Author Gravity note: all
    three sources are Jerome''s own idealizing epitaph/exhortation genre; whether the practice''s totality
    reflects genuine complete self-impoverishment or rhetorical amplification is Contested.'
period_sense: 'A sustained public unmaking of one''s former position, not a single private gesture: property
  sold or redirected, marriage prospects closed, plain dress announcing the change to a Rome that judged
  - praised by the church and sometimes suspected of excess, with grief and material need following those
  who gave the most (chunk Quick/World Meaning).'
prior_sense: The ordinary Latin renuntiatio - a formal announcement of withdrawal, the giving-up of an
  office or claim - the civic surface the ascetic use specializes; a builder note, UNVERIFIED against
  this build's own docs.
modern_sense: A private spiritual discipline, comparable to modern voluntary simplicity or minimalism
  (chunk Modern Hearing).
conceptual_distance_note: 'The modern frame is private lifestyle choice; this world''s renunciation was
  public, family-disrupting, and socially contested, with real material and relational costs - a senator''s
  daughter was SEEN to renounce (chunk World Hearing). Sharp gap: high grounding criterion by rule.'
semantic_domain: wealth-renunciation
grounding_criterion: high
voice_surface: To renounce among us was not to simplify one's life; it was to unmake one's place. The
  land sold or turned to other hands, the marriage that would have bound two houses declined, the plain
  dress that told everyone who had known you before that something fundamental had changed - all of it
  public, all of it judged, and for those who gave the most, grief and want followed.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: material-source-of
  target_id: hallex06
  note: 'Renounced wealth is what a patron sustains a scholar''s work WITH - ''the material source of
    patrocinium'' in this chunk''s own EF words. Chunk Ecological Function (verbatim, absorbed per FLAG-002):
    Anchors G2 (Primary gravity); the material source of *patrocinium*; presupposed by *xenodochium* and
    *nosocomium*; central to *virginitas* and *vidua* as their practical expression.'
- type: presupposed-by
  target_id: hallex06
  note: Mirror of hallex06's presupposes edge (the Desert material-source-of/presupposes pairing).
- type: presupposed-by
  target_id: hallex14
  note: 'Mirror of hallex14''s presupposes edge: this chunk''s EF names renuntiatio as ''presupposed by
    xenodochium and nosocomium''. NOTE: the xenodochium half of that EF sentence names a never-built term
    - the not-yet-built-partner class, declared, no edge possible.'
- type: associated-with
  target_id: hallex04
  note: 'This chunk''s EF: ''central to virginitas and vidua as their practical expression'' - association,
    no hierarchy (the categories are formation states, renunciation their enacted form).'
- type: associated-with
  target_id: hallex05
  note: Same EF sentence, the vidua half - the second-half-of-life renunciation 'chosen again' (hal_lex05
    World Meaning); symmetric both ways.
- type: presupposes
  target_id: hallex10
  note: Matrona standing 'is precisely what made large-scale renunciation possible at all' (hal_lex10
    World Meaning) - the social-historical precondition.
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex03_renuntiatio.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.
