---
id: pahclex012
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
term: hetaeria
aliases:
- illegal club
- collegium
quick_meaning: 'What Romans suspected we might be: an illegal club, a forbidden association. That charge was never the
  whole of what we faced.'
world_meaning: ''
distortion_risk: 'The legal category was uncertain — Christians were sometimes treated as an illegal association,
  but the charge was never straightforward or uniform.


  **Confidence:** Inferential-Thin. That hetaeria was the actual operative legal category — as opposed
  to an outside assumption the investigating authority brought to the encounter — is asserted, not confirmed,
  by this world''s own evidentiary base.'
retrieval:
  tier: 3
  retrieve_when:
  - participant asks whether Christians were treated as an illegal club, what legal category they fell
    into, or how Romans understood Christian gatherings.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about Roman clubs or associations with no connection to Christian persecution.
  force_llm_vote: false
sources:
- source_id: srcPAHCP07
  author_gravity_note: 'Thin-format chunk (S2.1a declared): hetaeria is Pliny''s own word for what Christians
    ceased when his edict banned clubs - Letters 10.96, the chunk''s whole evidentiary base.'
modern_hearing: A modern reader may assume Christians were persecuted primarily as an illegal organization.
period_sense: 'What Romans suspected the communities might BE: an illegal club, a forbidden association
  - the charge never the whole of what they faced, and the category itself uncertain in Roman hands (chunk
  Quick Meaning + World Hearing; a thin-format entry by the S2.1a declaration).'
prior_sense: Pliny's own Latin use of the Greek loan hetaeria - the club, the sodality, the association
  Roman law watched - the outsider's legal category IS the prior; nothing in-community transformed it
  (the chunk's outside-word framing).
modern_sense: Christians persecuted primarily as an illegal organization (chunk Modern Hearing).
conceptual_distance_note: 'The chunk''s own Inferential-Thin cap: that hetaeria was the operative legal
  category, rather than an assumption the investigating authority brought, ''is asserted, not confirmed,
  by this world''s own evidentiary base.'' Standard grounding; the record never firms the category.'
semantic_domain: outsider-legal-category
grounding_criterion: standard
voice_surface: 'The Romans had a word ready for what we might be: a club, an association, the kind the
  law forbids. It was never the whole of what we faced - and whether it was ever truly the charge, or
  only the shelf the governor first reached for, even the report that gives us the word does not say.'
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: corroborating
  formation_confidence: Inferential-Thin
field_relations:
- type: associated-with
  target_id: pahclex010
  note: 'Symmetric mirror of pahclex010''s edge: what the communities called love, outsiders assessed
    as association (the chunk-attested bridge).'
- type: associated-with
  target_id: pahclex013
  note: The two Pliny legal terms - the category suspected (hetaeria) and the conduct punished (pertinacia),
    both thin by their own confidence; symmetric both ways.
- type: associated-with
  target_id: pahclex009
  note: Symmetric mirror of pahclex009's Pliny-cluster edge.
---
Migrated at the S6.2/PAHC S2.2-equivalent (2026-07-31) from `data/pahc_world/lexicon_chunks/pahclex012_hetaeria.md` (mechanical split; mapping in `wrs/migrate/s62_pahc_s22.py`; aliases parsed under the VG-1a semantics with the preflighted Rule-A drops at birth - the second world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
