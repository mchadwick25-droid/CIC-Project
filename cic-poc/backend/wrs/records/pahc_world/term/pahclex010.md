---
id: pahclex010
world_id: post-apostolic-house-church
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
term: agape (as label)
aliases:
- love-feast
- agape meal
quick_meaning: '*Agape* names the common meal — love''s own name given to an ordinary act of feeding people
  at one table — though whether it is the same as the eucharist, a separate meal, or something else is
  not yet settled among us.'
world_meaning: 'We share a meal that goes by love''s own name: agape. What we do at that table — feeding
  the stranger, the widow, the orphan, alongside the household — is called love because it is love made
  visible in bread and cup shared.


  Ignatius uses the word in his letter to the Smyrnaeans: "It is not permitted without the bishop to baptize
  or to hold an agape." Here the agape is named as something the bishop oversees, something that can be
  held rightly or wrongly depending on who presides. Whether Ignatius means the eucharistic meal itself
  or a separate common meal, his words do not fully settle.


  And from the outside, Pliny reports that Christians gather to share "ordinary and harmless food" — but
  whether the meal he describes is the same practice Ignatius names, or something different, is a question
  we have not resolved. We hold both descriptions together, aware they may name the same thing or two
  things, without forcing an answer that our evidence does not give us.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: This term bridges the worship cluster and the outside-pressure
  cluster: it names a practice central to community formation (agape ↔ eucharistia) while also touching
  what outsiders observed (agape ↔ hetaeria).'
distortion_risk: 'In this world, the relationship between the agape meal and the eucharistic thanksgiving
  is still being worked out, varying from community to community.


  **Living Tradition Note:**

  This entry describes this world''s own formation ecology (c.70–200 CE). It makes no claim about how
  present-day traditions (such as Moravian Lovefeasts, Methodist love-feasts, or similar practices) currently
  define or practice the agape meal.


  **Confidence:**

  Documented that "agape" is a primary-source-anchored term for a real communal meal requiring the bishop''s
  own approval (Ignatius''s own usage, verified). Contested whether that meal is the same practice, a
  related practice in a different community, or an unconnected one from the second meal Pliny''s outside
  report separately describes — this world''s own evidentiary base does not resolve which reading is correct
  (see CT Contest Type below).'
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about the love-feast, agape, common meals, or the relationship between the meal and
    the eucharist.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about the word "agape" as love in general with no connection to a communal
      meal.
  force_llm_vote: false
sources:
- source_id: srcPAHCP03
  author_gravity_note: Ignatius, Letter to the Smyrnaeans 8 (agape requiring the bishop — ἀγάπην ποιεῖν
    in the Greek; verified against the Roberts-Donaldson/ANF translation).
- source_id: srcPAHCP07
  author_gravity_note: 'Pliny, Letters 10.96 (the separate, second-meal description this label is also
    proposed for, using no equivalent term at all — remains a source for the still-open cross-identification
    question).


    Note: an earlier draft of this entry cited only Pliny and stated that the "agape" label was not primary-source-anchored
    — this was incorrect. Ignatius''s own letter, already cited elsewhere in this world''s lexicon for
    a different clause in the same chapter, uses this exact term for a real communal practice. This entry
    has been corrected accordingly.'
modern_hearing: A modern reader may assume either that agape and eucharist were always separate, or that
  they were always the same.
period_sense: The meal that goes by love's own name - feeding stranger, widow, orphan alongside the household;
  Ignatius names it under the bishop's oversight ('not permitted without the bishop to baptize or to hold
  an agape'); whether his agape is the eucharistic meal or a separate table, and whether Pliny's 'ordinary
  and harmless food' is the same practice, the evidence does not settle - both held without forcing an
  answer (chunk Quick/World Meaning).
prior_sense: Agape as the communities' own love-word (the LXX/NT inheritance) applied as a MEAL's label
  - love made visible in shared bread; the label's application, not the word, is what this entry tracks
  (chunk framing).
modern_sense: Agape and eucharist assumed either always separate or always identical (chunk Modern Hearing).
conceptual_distance_note: The relationship 'is still being worked out, varying from community to community'
  (chunk World Hearing) - an unresolved-identity entry whose whole discipline is not forcing the identification;
  the entry's own correction note (an earlier draft mis-stated the primary anchoring; fixed against Smyrnaeans
  8's Greek) rides the chunk verbatim. Standard grounding.
semantic_domain: love-feast-label
grounding_criterion: standard
voice_surface: We share a meal that carries love's own name. What we do there - the stranger fed beside
  the household - is love made visible in bread and cup. Whether the agape Ignatius sets under the bishop
  and the harmless meal Pliny's prisoners described are one table or two, we do not force our evidence
  to say.
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: corroborating
  formation_confidence: Documented
field_relations:
- type: associated-with
  target_id: pahclex004
  note: 'The chunk''s own EF bridge: agape <-> eucharistia within the worship cluster. Chunk Ecological
    Function (verbatim, absorbed per FLAG-002): This term bridges the worship cluster and the outside-pressure
    cluster: it names a practice central to community formation (agape ↔ eucharistia) while also touching
    what outsiders observed (agape ↔ hetaeria).'
- type: associated-with
  target_id: pahclex012
  note: 'The chunk''s own EF bridge: agape <-> hetaeria - what the communities called love, outsiders
    assessed as association; symmetric mirror.'
---
Migrated at the S6.2/PAHC S2.2-equivalent (2026-07-31) from `data/pahc_world/lexicon_chunks/pahclex010_agape-label.md` (mechanical split; mapping in `wrs/migrate/s62_pahc_s22.py`; aliases parsed under the VG-1a semantics with the preflighted Rule-A drops at birth - the second world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[CT Contest Type - parked at the S2.2-equivalent; home arrives with the contested_claim records (S2.6-equivalent) / S2.3 authoring] **Historical scope** — whether Ignatius's love-feast and Pliny's described meal are the same practice, related practices in different communities, or unconnected.
