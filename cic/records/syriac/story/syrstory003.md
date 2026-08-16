---
id: syrstory003
world_id: syriac-edessa-nisibis
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
title: Jacob of Nisibis at the Council of Nicaea
narrative_tier:
  tier: 2
  justification: Two independent later sources (Theodoret, Gennadius) and a modern scholarly reconstruction
    of the actual subscription lists (Honigmann) converge on Jacob's attendance, which is why this sits
    at Tier 2 (collected tradition, traceable to the world's own community memory of its bishop, with
    attribution reasonably though not certainly secure) rather than Tier 1 — no contemporary 4th-century
    document independently confirms it, and Paul Peeters's foundational source-critical study of the whole
    Jacob dossier (1920) treats the broader body of material about him as legend with an uncertain historical
    core. Nicaea attendance specifically, however, is the best-attested single claim within that dossier,
    distinct from and more secure than the miracle material treated separately at Tier 3.
text: Jacob, bishop of Nisibis from around 309, is remembered as one of the bishops present at the Council
  of Nicaea in 325. He stood among those who opposed the Arian teaching. The lists of signers that survive
  and record his name are late. They are composite manuscripts, pieced together by modern scholars rather
  than a single document from that time. These lists place him at the seventy-seventh position among the
  gathered bishops. Later church historians wrote a century or more afterward. They remembered him for
  his part in standing against Arius's teaching at the council.
attested_occasion: 'Nicaea, 325: Jacob bishop of Nisibis (from c. 309) among the signatories - the surviving
  lists are late composite manuscripts reconstructed by modern scholarship (Honigmann, position 77), and
  no contemporary fourth-century document independently confirms the anti-Arian role later historians
  remembered him for (chunk Story Text/front matter).'
tellable_as: background-fact
owner_figure_id: syrfig003
voice_surface: |-
  We name Jacob among those who stood at Nicaea, because the kept lists carry his name. We also say plainly what those lists are: late copies. And the memory of his part against Arius is a later historian's, not ours. Usage guidance (chunk, verbatim): The Representative may draw on this as part of the tradition's own memory of Jacob: "Jacob, our bishop of Nisibis, stood at Nicaea among those who would not bend to Arius's teaching." The Representative should not claim firsthand or contemporary documentary certainty for this — if pressed, it may be acknowledged as what the tradition remembers of him rather than an unbroken eyewitness record.

  **Additional guidance:** Keep this story distinct from the siege-deliverance legend (Tier 3) in any single telling — conflating a comparatively well-attested institutional fact with a clearly legendary miracle account would blur a distinction this world's own evidence requires holding onto.
confidence_line: Widely Accepted (attendance and anti-Arian stance); Contested (specific attribution —
  no contemporary 4th-century document independently confirms it)
retrieval:
  tier: 2
  retrieve_when:
  - participant asks how this world connects to the wider, Greek-speaking imperial church
  - participant asks about Jacob of Nisibis's standing or authority
  - conversation touches this world's own relationship to Nicene orthodoxy specifically.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant wants a first-person account of the Council itself (no such account survives from
      this world)
  - condition_type: sense-disambiguation
    text: participant is conflating this with the siege-deliverance legend (see the separate Tier 3 story,
      "Jacob of Nisibis and the Deliverance of the City") — the two should not be blended into one telling.
  force_llm_vote: false
sources:
- source_id: srcSYR044
  locus: 'Theodoret of Cyrrhus, Historia Ecclesiastica and Historia Religiosa I; Gennadius of Marseille,
    De Viris Illustribus, Supplement, ch. 1; Nicene subscription lists as reconstructed by Ernest Honigmann,
    "La liste originale des Pères de Nicée," Byzantion 14 (1939): 17-76 (Jacob at position 77); Paul Peeters,
    "La légende de saint Jacques de Nisibe," Analecta Bollandiana 38 (1920): 285-373 (source-critical
    assessment of the wider Jacob dossier)'
- source_id: srcSYR043
  locus: 'Theodoret of Cyrrhus, Historia Ecclesiastica and Historia Religiosa I; Gennadius of Marseille,
    De Viris Illustribus, Supplement, ch. 1; Nicene subscription lists as reconstructed by Ernest Honigmann,
    "La liste originale des Pères de Nicée," Byzantion 14 (1939): 17-76 (Jacob at position 77); Paul Peeters,
    "La légende de saint Jacques de Nisibe," Analecta Bollandiana 38 (1920): 285-373 (source-critical
    assessment of the wider Jacob dossier)'
- source_id: srcSYR049
  locus: 'Theodoret of Cyrrhus, Historia Ecclesiastica and Historia Religiosa I; Gennadius of Marseille,
    De Viris Illustribus, Supplement, ch. 1; Nicene subscription lists as reconstructed by Ernest Honigmann,
    "La liste originale des Pères de Nicée," Byzantion 14 (1939): 17-76 (Jacob at position 77); Paul Peeters,
    "La légende de saint Jacques de Nisibe," Analecta Bollandiana 38 (1920): 285-373 (source-critical
    assessment of the wider Jacob dossier)'
- source_id: srcSYR050
  locus: 'Theodoret of Cyrrhus, Historia Ecclesiastica and Historia Religiosa I; Gennadius of Marseille,
    De Viris Illustribus, Supplement, ch. 1; Nicene subscription lists as reconstructed by Ernest Honigmann,
    "La liste originale des Pères de Nicée," Byzantion 14 (1939): 17-76 (Jacob at position 77); Paul Peeters,
    "La légende de saint Jacques de Nisibe," Analecta Bollandiana 38 (1920): 285-373 (source-critical
    assessment of the wider Jacob dossier)'
gravity_links:
- gravity_id: syrgrav004
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at S2.5):
    This ties Nisibis, and through Jacob the formation of Ephrem as his student, to the wider imperial
    church at the very moment that church was defining itself against Arius - even though our own way of
    doing theology runs on poetry and type, quite unlike the philosophical categories of those debates. It
    is also a modest point about authority among us: Jacob''s standing as bishop is, in this one case,
    unusually well attested from outside, in contrast to the ambiguity around Aphrahat''s. That contrast is
    worth keeping rather than flattening.'
chunk_slug: jacob-nisibis-nicaea
---
Migrated at the S6.2/SYR S2.4-equivalent (2026-07-28) from `data/syriac_world/story_chunks/syrstory003_jacob-nisibis-nicaea.md` (mapping in `wrs/migrate/s62_syr_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] This story ties Nisibis — and through Jacob, Ephrem's own formation as his traditional student — to the wider imperial-conciliar church at the very moment (325 CE) that church was defining itself against Arianism, even though this world's own formation logic (Doc_07, Section 2B) runs on a poetic-typological method quite unlike the philosophical-categorical mode of the Nicene debates themselves. It is a modest but real data point for C4 (Authority-Structure Ambiguity): Jacob's own episcopal standing is, in this one instance, unusually well-external-attested compared to the ambiguity Doc_04/07 found surrounding Aphrahat's status — a contrast worth preserving rather than flattening.

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field (three
sentences, the second and third each stacking multiple appositive and participial clauses) at FK grade
16.9 / FRE 25.7. Per Mark's decision to extend the readability pass to story records, the three sentences
are split into seven shorter ones along their own existing clause boundaries, with a few plain-synonym
swaps ("reconstructed" -> "pieced together," "assembled" -> "gathered," "resisting" -> "standing against").
No fact, name, or hedge is dropped - Jacob's bishopric from around 309, his presence at Nicaea in 325,
the lateness and composite nature of the signatory lists, the seventy-seventh position, and the "later
historian, not contemporary" hedge on the anti-Arian attribution are all unchanged. Re-scored: FK 8.2 /
FRE 60.4, clearing both thresholds.
