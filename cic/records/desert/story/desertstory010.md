---
world_id: desert-monasticism
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
id: desertstory010
title: Amma Theodora among the named mothers (allusion only)
narrative_tier:
  tier: 2
  justification: 'Named amma genuinely attested: Widely Accepted that Theodora and her sayings are a real,
    if thin, part of the Apophthegmata tradition (Doc_02 §1.6; Doc_06 §1.6''s plural-voices flag); Inferential
    / Thin for any claim beyond what the surviving sayings themselves state. No individual saying of hers
    is vetted into this build''s record - which is why this record licenses allusion only, never scene-telling
    or quotation (CO-P2-07).'
text: The tradition preserves sayings under Amma Theodora's name. She is one of the named mothers whose
  tested words the Apophthegmata kept. Her words were passed down through the same later-compiled apparatus
  as the male-attributed sayings, with a much smaller surviving sample. This build carries none of her
  individual sayings whole. What can be told is that she is real, named, and attested. Her material is
  thin. This is said plainly, rather than filled in.
attested_occasion: None carried - her attestation in this build is corpus-level (the ammas' sayings within
  the Apophthegmata tradition, srcDES006); no individual saying with its occasion is vetted into the record.
tellable_as: allusion-only
voice_surface: Amma Theodora is among the named mothers whose tested words the tradition kept. What we
  can tell of her is real but thin, and we say so plainly rather than filling the silence.
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about Theodora by name, or about the desert mothers/ammas beyond Sarah
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant asks for a specific saying or scene of hers - the record licenses acknowledgment
      only; the honest-thinness answer is the content
  - condition_type: sense-disambiguation
    text: the question is a general one about women in this life, answerable first by the vetted Sarah
      story - this allusion record is for name-specific or beyond-Sarah asks (its own retrieve-when scope)
  force_llm_vote: false
sources:
- source_id: srcDES006
  author_gravity_note: Widely Accepted that the named ammas and their sayings are a genuine, if thin,
    part of the Apophthegmata tradition; Inferential / Thin beyond what the sayings themselves state (Doc_02
    §1.6).
owner_figure_id: desertfig008
chunk_slug: amma-theodora-among-the-named-mothers
---
CO-P2-07 allusion-only story record (2026-07-27): attested-fact text only - no saying invented, no material imported from outside the build's record.

S3.4 (2026-07-27): beyond-Sarah guard added as an evaluable DNRW - the record's own retrieve-when scope, now enforceable (the cross-encoder cannot read scoping semantics; the guard vote can).

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field at
FK grade 16.5 / FRE 38.2 - two dash/semicolon-joined sentences each carrying a chain of qualifying clauses.
Per Mark's decision to extend the readability pass to story records, both are split at their own existing
dash and semicolon boundaries into shorter sentences, plus one plain-synonym substitution ("transmitted"
-> "passed down"). No hedge or claim is dropped - the honest-thinness framing ("real, named, and attested,"
"her material is thin," "said plainly rather than filled in") and the attestation basis (the same
later-compiled apparatus as the male-attributed sayings, a much smaller surviving sample, no individual
saying carried whole) are unchanged. Re-scored: FK 6.4 / FRE 68.1, clearing both thresholds.
