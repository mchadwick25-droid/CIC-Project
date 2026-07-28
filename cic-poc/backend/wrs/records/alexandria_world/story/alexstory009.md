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
text: Late in this world's life, under an emperor determined to break the Church's hold on the empire
  once and for all, a persecution fell on Egypt with a severity the earlier pressures had not matched.
  It struck widely — not only teachers and bishops, as earlier persecutions had concentrated on, but ordinary
  believers across every rank of the community, so that this world's own reckoning of time came, from
  that point, to be counted from the years of this persecution's beginning rather than by any other marker.
  The tradition kept by the wider church of Egypt names many who were killed for their faith in these
  years and holds their witness as central to what it means to have been faithful under ultimate pressure.
  What this persecution reached, unlike the schools and the reading-rooms, was the whole breadth of the
  community — the believers this world's other stories cannot otherwise reach, formed not through Scripture
  read at depth but through the same fire that reached the teacher generations before.
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
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory009_coptic-martyrs.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

[Formation Ecology Connection — parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] This story illustrates T4 (Martyrdom vs. Contemplative-Ascent), and Doc_04 §3.6 names T4 as the one gravity in this world's whole ecology whose evidence plausibly reached every stratum of the community, not only the literate and learned — though the martyr's own interior remains Inferential-Thin even so. It stands alongside Antony's contemplative pole (alexstory005) as this world's two competing pictures of a completed formed life. It also connects to Doc_08's ongoing force of persecution (2A-3) at its most severe and widely-felt instance across the whole span.
