---
id: ijcstory003
world_id: imperial-juridical-christianity
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 4
register: emic
review_state: draft
cache_stability: static
title: The Bees of Milan
text: 'Paulinus tells it this way. While Ambrose lay as an infant in the courtyard of his father''s house,
  a swarm of bees came down upon his face, going in and out of his open mouth, and left again. [It] left
  him unharmed, having done nothing but rest there a while. His father, seeing it, said that if the child
  lived, he would become something great.


  The bees left honey where they had touched him, so the story is told, or so it was told to explain what
  needed no further sign. [This was] a life that would come, in its own way, to be as full of speech as
  any voice this world''s own record preserves.'
confidence_line: Contested (for the formation portrait it offers of Ambrose); Inferential/Thin (for the
  specific event claimed)
attested_occasion: Paulinus of Milan, Vita Ambrosii — written at Augustine's own request, some fifteen
  to twenty years after Ambrose's death (c. 412–413)
tellable_as: scene
owner_figure_id: ijcfig005
narrative_tier:
  tier: 3
  justification: 'Tier 3 (Attributed Tradition): the genre markers are explicit — this is hagiography,
    written by someone in Ambrose''s own circle (his former secretary) at a patron''s request, decades
    after the events it claims to describe, and it uses a recognizable topos (an infant marked by an animal
    omen) that recurs in other saints'' lives of the period rather than being unique to Ambrose. The formation
    ideal it communicates — that greatness announces itself even in infancy — is real and worth carrying;
    the specific claimed event is not.'
voice_surface: 'Usage guidance (chunk, verbatim): The Representative may offer this story as the tradition''s
  own account of what a formed and gifted life looks like, explicitly naming its hagiographic character:
  "This is how the tradition remembers Ambrose''s own beginning..." The Representative must not present
  the bee-swarm as a documented biographical event, and should be prepared, if asked, to distinguish this
  legendary material plainly from Ambrose''s own well-attested adult conduct (told in `ijcstory004`).'
gravity_links: []
retrieval:
  tier: 3
  retrieve_when:
  - participant asks about Ambrose's own childhood or early life, or about legendary/hagiographic material
    connected to him specifically.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the participant's question concerns Ambrose's actual documented adult conduct (the 386 standoff,
      the confrontations with Theodosius) — retrieve ijcstory004 or the historical record instead, not
      this legend.
  force_llm_vote: false
sources:
- source_id: srcIJC22
chunk_slug: the-bees-of-milan
---
Migrated at the S6.2/IJC S2.4-equivalent (2026-07-31) from `data/imperial_juridical_world/story_chunks/ijcstory003_the-bees-of-milan.md` (mechanical split; ownership map in `wrs/migrate/s62_ijc_s24.py`).

[Formation Ecology Connection - parked at the S2.4-equivalent; converted to gravity_links at the S2.5-equivalent per CO-P2-04] This story tells us nothing documented about Ambrose's childhood - this world's record has no reliable window into that at all. What it does show is how this world's later memory of him worked: a man whose adult eloquence and willingness to face down power was, within a generation of his death, already being read backward into an infancy that had to have announced it. It is a genuine instance of how this world built memory, applied to one life rather than to an institution.

[Final Assembly Instruction - parked verbatim as assembly provenance] Completed per `L4-Templates/Story_Repository_Chunk_Template.md` V1.0. No brackets or builder notes remain. Tier/Confidence alignment confirmed (Tier 3 → Contested for portrait, Inferential/Thin for the specific event).

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field at
FK grade 13.5 / FRE 65.9 - a colon-joined opening sentence describing the bee swarm in one long run, and
a closing sentence joining a colon and an appositive into a single dense clause. Per Mark's decision to
extend the readability pass to story records, both sentences are split at their own existing colon and
dash boundaries, with two bracketed supplied subjects ("[It]", "[This was]") added where the resulting
clauses had no subject of their own to stand alone, matching this project's existing quote-record
convention. No fact, hedge, quotation, or attribution is dropped - Paulinus's attribution, the bee-swarm
episode, the father's remark, and the closing comparison to Ambrose's eloquence are all unchanged.
Re-scored: FK 6.2 / FRE 85.1, clearing both thresholds.
