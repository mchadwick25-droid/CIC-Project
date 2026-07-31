---
id: pahclex013
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
term: pertinacia
aliases:
- stubbornness
- obstinacy
quick_meaning: '*Pertinacia* — stubbornness, obstinacy — is what Pliny found punishable in Christians:
  not the content of their beliefs, but their refusal to recant when given the chance.'
world_meaning: ''
distortion_risk: 'Pliny''s own report treats obstinate refusal as sufficient grounds to act, but never
  fully resolves whether "the name itself" or the conduct associated with it was what actually merited
  punishment — pertinacia names a charge whose own core question the source that reports it leaves open.


  **Confidence:** Inferential-Thin. Whether "the name itself" or the conduct associated with it was what
  actually merited punishment is a question this world''s sole witness to the charge raises but does not
  resolve.'
retrieval:
  tier: 3
  retrieve_when:
  - participant asks about Pliny's interrogation methods, why Christians were punished, or what Romans
    objected to.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about stubbornness in a general sense with no connection to Roman persecution.
  force_llm_vote: false
sources:
- source_id: srcPAHCP07
  author_gravity_note: 'Thin-format chunk (S2.1a declared): pertinacia is Pliny''s own word for what he
    punished - Letters 10.96, the chunk''s whole evidentiary base.'
modern_hearing: A modern reader may assume Christians were persecuted for specific beliefs or practices.
period_sense: 'What Pliny found punishable: not the content of belief but the refusal to recant when given
  the chance - stubbornness as the operative ground, while his own report leaves open whether the name
  itself or the conduct merited punishment (chunk Quick Meaning + World Hearing; thin-format entry by
  the S2.1a declaration).'
prior_sense: 'Roman moral vocabulary: pertinacia as the vice of obstinacy - a Roman''s word for a Roman''s
  complaint; the outsider''s charge IS the prior (the chunk''s framing).'
modern_sense: Christians persecuted for specific beliefs or practices (chunk Modern Hearing).
conceptual_distance_note: 'The chunk''s own Inferential-Thin cap: ''a charge whose own core question the
  source that reports it leaves open'' - the record carries the openness, never resolves it. Standard
  grounding.'
semantic_domain: outsider-legal-charge
grounding_criterion: standard
voice_surface: What the governor punished, by his own account, was not what we believe but that we would
  not stop saying it. Stubbornness, he called it. Whether the name alone or the refusal was the crime,
  his own letter asks and does not answer - and we cannot answer it for him.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: corroborating
  formation_confidence: Inferential-Thin
field_relations:
- type: associated-with
  target_id: pahclex012
  note: Symmetric mirror of pahclex012's edge (the Pliny legal pair).
---
Migrated at the S6.2/PAHC S2.2-equivalent (2026-07-31) from `data/pahc_world/lexicon_chunks/pahclex013_pertinacia.md` (mechanical split; mapping in `wrs/migrate/s62_pahc_s22.py`; aliases parsed under the VG-1a semantics with the preflighted Rule-A drops at birth - the second world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.
