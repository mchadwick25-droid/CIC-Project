---
id: halstory11
world_id: hieronymian-ascetic-literary
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
title: Translating a Book of Scripture
narrative_tier:
  tier: 4
  justification: No single source narrates one complete translation process start to finish as a unified
    scene; this reconstructs the typical shape from independently attested stages. Every element is traceable
    — nothing is invented. This story's subject (biblical translation) was, on this world's own evidence,
    performed by exactly one person throughout the household's whole span — composite in method, but not
    in subject. This document does not claim this describes a specific attested episode.
text: 'This is how the typical shape of the work went, not as a single remembered event but as the pattern
  this household''s scholar followed across many books: consultation with a Hebrew teacher over a difficult
  word or passage; the labor of rendering it into Latin against both the received Greek and the Hebrew
  itself; and, at the end, a preface — written to defend the choices made, anticipate the objections that
  would come, and dedicate the finished work to the household member whose question or request had occasioned
  it.'
attested_occasion: Tier-4 composite of the translation process's typical shape - consultation with a Hebrew
  teacher, rendering against Greek and Hebrew both, the defensive preface and its dedication - reconstructed
  from independently attested stages (the prefaces; the documented dedication pattern of the Bethlehem
  commentaries); 'composite in method, but not in subject' - on this world's own evidence the work was
  performed by exactly one person, which is why this record is owned by the scholar's figure and not the
  community (the chunk's own Tier Justification, quoted; the CO-P2-06 call documented in the S2.4 checkpoint).
tellable_as: scene
owner_figure_id: halfig001
voice_surface: 'This is how the work went, book by book - not one remembered afternoon but the pattern
  of a working life: the teacher consulted, the word weighed against two tongues, and at the end a preface
  to defend the choices and a dedication to the one whose asking had begun it. One man''s own singular
  practice, reconstructed from its attested stages - and never told as a single attested day. Of how fluent
  the Hebrew finally was, we claim no more than our record can carry. Usage guidance (chunk, verbatim):
  Appropriate as reconstruction of typical scholarly practice, explicitly marked as such, and explicitly
  marked as reconstructing one scholar''s own singular practice, not a generalizable household practice.
  Must not be used to assert this scholar''s Hebrew fluency at higher confidence than the wider construction
  record establishes (Contested).'
confidence_line: Inferential/Thin (always, for Tier 4)
retrieval:
  tier: 4
  retrieve_when:
  - Participant asks how the translation project actually worked, step by step
  - participant asks what it took to produce a corrected biblical book.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant asks whether this describes a specific, individually-attested translation episode
      (it does not — this is reconstructed typical process, and this limitation must be named if the participant
      probes).
  force_llm_vote: false
sources:
- source_id: srcHAL023
  locus: 'Composite - elements per the chunk''s own Source Identification table (parked verbatim in this
    record''s body; the monastic-template element of halstory10 is declared analogy, Doc_01 SS6/Doc_08,
    no row owed): Composite — see Source Identification below'
- source_id: srcHAL003
  locus: 'Composite - elements per the chunk''s own Source Identification table (parked verbatim in this
    record''s body; the monastic-template element of halstory10 is declared analogy, Doc_01 SS6/Doc_08,
    no row owed): Composite — see Source Identification below'
gravity_links:
- gravity_id: halgrav001
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at
    S2.5): Illuminates the *Hebraica veritas* gravity''s actual working mechanism and the *praefatio*/*epistula*
    transmission apparatus together — showing how the abstract textual-authority commitment was actually
    produced, book by book.'
- gravity_id: halgrav004
  note: Named in the same FEC (full text on this record's first gravity link).
---
Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from `data/hieronymian_world/story_chunks/hal_story11_translating-a-book.md` (mapping in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX-SYR S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illuminates the *Hebraica veritas* gravity's actual working mechanism and the *praefatio*/*epistula* transmission apparatus together — showing how the abstract textual-authority commitment was actually produced, book by book.

[Source Identification - the composite's own element-to-source table, parked verbatim (CO-P2-06 composite convention)] **Element: consultation with a Hebrew teacher.** Source: Jerome's own references to named Jewish teachers in his prefaces (Doc_01 §3.1).
**Element: rendering against both Greek and Hebrew.** Source: Jerome's prefaces generally, defending his method (Doc_06 entry 13).
**Element: the defensive preface, anticipating objection.** Source: the extensive surviving corpus of Jerome's prefaces (Doc_06 entry 13).
**Element: dedication to a household member who requested the work.** Source: Doc_02 §1.1 (dedication pattern documented across Jerome's Bethlehem-period commentaries).

[Absent Story Note - the chunk's own honest-brevity rule, parked verbatim] This chunk does not claim to describe any single, specific, individually-attested instance of translation — no source narrates one complete episode from consultation to finished preface. If a participant asks whether this happened exactly this way on a specific occasion, the honest answer is that this is the typical shape reconstructed from separate attested stages, not a remembered single event.
