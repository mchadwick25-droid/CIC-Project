---
id: alexstory009
world_id: alexandria-catechetical
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
title: The Coptic Martyrs — The Era of the Martyrs
narrative_tier:
  tier: 3
  justification: 'The persecution itself is a documented historical event, independently attested well
    beyond this world''s own sources, with a severity and scope not seriously disputed. The *specific
    martyr acts* — named individuals, particular circumstances of their deaths, specific miracles or dialogues
    attributed to them — belong to the hagiographic martyrological tradition and carry the same genre
    conventions as other hagiography in this inventory: real evidence of what the community believed faithful
    witness looked like, not historical reporting of individual events. This event-versus-acts split mirrors
    the same discipline applied at alexstory003.'
text: Late in this world's life, a persecution fell on Egypt with a severity the earlier pressures had
  not matched. It came under an emperor determined to break the Church's hold on the empire once and
  for all. It struck widely, not only teachers and bishops, as earlier persecutions had concentrated
  on. It also struck ordinary believers across every rank of the community. So this world's own reckoning
  of time changed. From that point on, years were counted from this persecution's beginning, rather than
  by any other marker. The tradition kept by the wider church of Egypt names many who were killed for
  their faith in these years. It holds their witness as central to what it means to have been faithful
  under ultimate pressure. What this persecution reached, unlike the schools and the reading-rooms, was
  the whole breadth of the community. [These are] the believers this world's other stories cannot otherwise
  reach. They were formed not through Scripture read at depth but through the same fire that reached
  the teacher generations before.
attested_occasion: The Coptic martyr memory - the Diocletianic persecution (303-311) remembered so deeply
  the Coptic church dates its calendar (Anno Martyrum) from Diocletian's accession (284).
tellable_as: scene
owner_figure_id: alexfig012
voice_surface: 'The martyrs we name are the community''s own kept memory - a whole calendar begins from
  their era, and we tell it as the community''s remembering. Usage guidance (chunk, verbatim): The persecution''s
  severity and reach may be offered with confidence as documented history — it is the one persecution
  in this world''s record attested to have struck the whole community, not only its teachers. Specific
  martyr acts, where named, should be carried as the community''s own hagiographic memory, not as secured
  historical particulars. The martyr''s own interior — what the experience felt like, from inside — is
  not narrated here or anywhere in this inventory; this world can tell what it believed martyrdom produced
  in a formed soul, never what the martyr themselves felt in the moment. This is a named absence (Doc_09
  §3), not a gap to be filled.'
retrieval:
  tier: 3
  retrieve_when:
  - participant asks about martyrdom as this world's own formation mode reaching every stratum of the
    community, not only the learned
  - participant asks about T4 (Martyrdom vs. Contemplative-Ascent) from the martyr's own pole.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant presses for the martyr's own felt interior experience — that remains Inferential-Thin
      and is a named absence (Doc_09 §3), not supplied by this or any story
  - condition_type: sense-disambiguation
    text: participant wants specific named martyrs' acts narrated as secure historical particulars — the
      persecution is documented, the specific acts are hagiographic.
  force_llm_vote: false
sources:
- source_id: srcALX025
  locus: The Coptic martyrological tradition; the Diocletianic persecution (303–311 CE; the Anno Martyrum
    reckoned from Diocletian's 284 accession)
gravity_links:
- gravity_id: alexgrav009
  note: 'This story illustrates the tension between martyrdom and contemplative ascent, which is the one tension
    in this world''s whole ecology whose evidence plausibly reached every stratum of the community, not only
    the literate and learned - though the martyr''s own interior remains thin even so. It stands alongside
    Antony''s contemplative pole as one of this world''s two competing pictures of a completed formed life.
    It also connects to the ongoing pressure of persecution at its most severe and widely-felt instance
    across the whole span.'
confidence_line: Documented (the persecution as event) / Contested (the specific martyr acts)
chunk_slug: coptic-martyrs
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory009_coptic-martyrs.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

S2.5-equivalent (2026-07-27): the parked Formation Ecology Connection converted to typed gravity_links[] (CO-P2-04 - FEC verbatim on the first link's note); see wrs/migrate/s62_alx_s25.py.

CO-P2-16 (2026-07-28): confidence_line backfilled verbatim from the deployed chunk's Confidence front-matter line (live retrieval-context metadata); see wrs/migrate/s62_alx_s29_co16.py.

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field at
FK grade 18.7 / FRE 35.3 - four sentences, each stacking a lead-in clause onto a long "so that ... rather
than" or "and holds ... " tail. Per Mark's decision to extend the readability pass to story records, each
sentence is split at its own existing comma, "but," or "and" boundary, plus one light rewording ("came ...
to be counted" -> "changed. From that point on, years were counted") to let the reckoning-of-time clause
stand as its own sentence, and one bracketed supplied phrase ([These are]) for a clause with no subject of
its own. No fact, hedge, or attribution is dropped - the emperor, the persecution's unmatched severity, its
reach past teachers and bishops into every rank of believers, the calendar reckoned from its start, the
church's kept tradition of the martyrs' names, and the closing claim that this persecution alone reached
the whole community are all unchanged. Re-scored: FK 8.4 / FRE 62.6, clearing both thresholds.
