---
id: desertstory006
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
title: Amma Sarah's Answer to the Visiting Elders
narrative_tier:
  tier: 2
  justification: Same basis as Stories 004-005. Confidence is Widely Accepted for the saying's place in
    the tradition; Inferential / Thin for the specific narrated encounter's historicity.
text: 'The tradition tells that when some elder monks came to Amma Sarah intending to test or humble her,
  saying, "Be careful not to become conceited, thinking to yourself, ''Look, anchorites are coming to
  see me, a mere woman,''" she answered: "According to nature I am a woman, but not according to my thoughts.
  It is I who am a man and you who are women."'
attested_occasion: Visiting elder monks coming to test or humble her as a woman (Apophthegmata, Sarah,
  Alphabetical Collection).
tellable_as: scene
voice_surface: 'The tradition tells that Amma Sarah answered them - a pointed reversal under a hostile
  frame, flattened neither into equality nor inferiority claims. Usage guidance (chunk, verbatim): Told
  as tradition. Given the genuine thinness of surviving material specifically attributed to named ammas
  (Doc_02 §1.6''s own flagged asymmetry), this story should be used, not held back, when the conversation
  reaches questions of women''s presence and authority in this world -- but the Representative should
  be honest that this is one of only a small number of directly attributed sayings surviving for named
  ammas, not evidence of a fuller corpus that happens not to have been included here.


  **On the content itself:** the saying is a pointed reversal, not an egalitarian "no difference" claim
  -- Sarah affirms a difference in nature while claiming manliness in thought, turning the elders'' own
  test back on them. It should not be flattened into either "this tradition held women equal" or "this
  tradition held women inferior." Held honestly, it is closer to defiance under a hostile frame than to
  either simple reading.'
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about women's presence, authority, or teaching voice in this world
  - participant raises a claim that this tradition held women as spiritually lesser
  - conversation reaches gravity 3 (elder-mediated authority exercised by a woman) or gravity 5 (diakrisis
    deployed against a direct social challenge).
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant asks for a fuller corpus of named ammas' own sayings beyond what this world's own
      record supplies -- see the Honest Limits treatment in the Permanent Prompt and World Capsule Core
      instead, which names this thinness directly rather than filling it
  - condition_type: sense-disambiguation
    text: conversation seeks to flatten this saying into a simple claim of gender equality or into a claim
      of misogyny -- the saying itself refuses both readings, and so should the Representative (see Usage
      Guidance).
  force_llm_vote: false
sources:
- source_id: srcDES005
  author_gravity_note: Widely Accepted (the saying's place in the tradition); Inferential / Thin (the specific
    narrated encounter's historicity)
- source_id: srcDES021
  author_gravity_note: 'Source line (chunk): Apophthegmata Patrum, Sarah (Alphabetical Collection)'
owner_figure_id: desertfig006
gravity_links:
- gravity_id: desertgrav003
  note: This is this world's single clearest direct textual evidence for the ammas' own teaching voice
    (Doc_02 §1.6; Doc_06 §1.6), directly illustrating both gravity 3 (elder-mediated authority, exercised
    here by a woman under direct challenge) and gravity 5 (diakrisis, deployed against a social test rather
    than an interior thought). It is also the specific saying an earlier World Capsule Core draft paraphrased
    inaccurately -- softened into a generic equal-natures claim the source does not make (see `CapsuleCore_Review_Round1.md`,
    Finding S4, and `CapsuleCore_Review_Round2.md`'s confirmation of the fix) -- and separately, in live
    adversarial testing, given an invented occasion in one response (elders asking why she prayed a certain
    way, rather than the attested elders coming to test/humble her about being a woman), while the saying's
    own content was rendered accurately elsewhere in the same test pass (see `LiveTest_Scoring_Review.md`,
    the Confidence-Under-Thinness Turn 4 finding). This Story Text is the source-accurate version and
    should be treated as the canonical wording.
- gravity_id: desertgrav005
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
---
Migrated at S2.4 (2026-07-27) from `data/desert_world/story_chunks/desertstory006_sarah-answer-to-elders.md` (Story Text / Tier Justification / Usage Guidance verbatim from the chunk's own sections; occasion and telling-formula per chunk + Doc_09a). Tier-4 owner gap: see FLAG-003.

CO-P2-04 (2026-07-27): parked FLAG-004 sections restructured into gravity_links[] (FEC verbatim on the first link) and, for this record's tier-4 table, per-element sources[] entries.
