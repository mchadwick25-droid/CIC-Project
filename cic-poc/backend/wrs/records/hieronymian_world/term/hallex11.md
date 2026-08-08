---
id: hallex11
world_id: hieronymian-ascetic-literary
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
term: Exegesis (as practiced authority)
aliases:
- Marcella's exegetical authority
- scriptural authority without office
quick_meaning: The recognition of someone as authoritative on disputed scriptural questions through demonstrated
  learning, exercised in person, apart from any clerical office — the standing at least one woman in this
  world held in her own right.
world_meaning: 'In this world, being consulted on a hard scriptural question was itself a form of authority,
  and it did not require ordination to hold it. When the scholar who had trained a Roman household in
  this kind of reading left for the Holy Land, at least one member of that household did not lose the
  standing his teaching had helped establish in her — clergy, later, came to her own house with the questions
  they could no longer bring to him directly. This was a real standing, held and exercised in her own
  right.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: The clearest evidence for the one real counter-current in this household''s life - a way of holding authority that runs against the main pattern without displacing it, and that cannot honestly be left out. It does not amount to a separate strand within the household: on what survives, this is the same kind of authority the traveling scholar holds, occupying a different position rather than being different in kind.'
distortion_risk: '**Modern Hearing:**

  Risk of either overclaiming this as full independent theological authority equivalent to ordained office,
  or dismissing it as merely social/informal and therefore unimportant.


  **World Hearing:**

  A real, recognized, but non-office-based form of authority — neither equivalent to ordination nor merely
  informal influence; its own distinct thing, understood on its own terms within this world''s authority
  logic.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about Marcella specifically
  - participant asks whether any woman in this world held recognized theological authority
  - participant asks how scriptural questions were resolved without a bishop present.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn
  - condition_type: sense-disambiguation
    text: participant is asking about formal ordained authority (direct them instead to Patrocinium).
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: 'Ep. 127 (Marcella, to Principia) — the **sole** source. Author Gravity note: single-source,
    Contested, authored by Jerome after the subject''s death for his own partly self-vindicating purposes.
    This is the single most Author-Gravity-constrained entry in this lexicon.'
period_sense: 'Recognition as authoritative on disputed scriptural questions through demonstrated learning,
  exercised in person, apart from any clerical office - the standing at least one woman (Marcella) held
  in her own right: after the teacher left for the Holy Land, clergy came to her own house with the questions
  they could no longer bring to him. SINGLE-SOURCE DISCIPLINE (the authored home of the S2.2 parking):
  this standing is attested in Jerome''s own memorial letter (Ep. 127) - a single-voice source; srcHAL001''s
  Marcella-list caveat and srcHAL012''s unverified Ep.24/127-pairing flag both bear on this entry, and
  the claim is held as real but single-attested, never independently corroborated.'
prior_sense: none-attested - this is the build's own descriptive label for a practice (the syrlex010 class),
  not an inherited term; the register is the practiced standing itself.
modern_sense: Either overclaimed as full independent theological authority equivalent to ordained office,
  or dismissed as merely social, informal, and therefore unimportant (chunk Modern Hearing - a DOUBLE
  distortion, both directions wrong).
conceptual_distance_note: 'A real, recognized, but non-office-based form of authority - neither equivalent
  to ordination nor mere influence; ''its own distinct thing, understood on its own terms within this
  world''s authority logic'' (chunk World Hearing). The chunk''s EF records the strand-test result honestly:
  a difference in POSITION, not in KIND, from the dominant authority mode. Sharp double-sided gap: high
  grounding criterion. The parked Reported-Experience Status text remains verbatim in this record''s body.'
semantic_domain: practiced-exegetical-authority
grounding_criterion: high
voice_surface: 'There was a house in Rome where clergy brought the questions they could not settle - and
  the one who answered held no office at all. Her standing was real: earned by demonstrated learning,
  exercised in person, recognized by the very men whose ordination gave them what she did not have. We
  say this carefully, for it comes to us in one voice only - the teacher''s own letter, written in her
  memory.'
confidence:
  citation_specificity: A
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
field_relations:
- type: presupposes
  target_id: hallex05
  note: 'The standing is exercised from within the vidua category, not virginity (hal_lex05 EF, near-verbatim).
    Chunk Ecological Function (verbatim, absorbed per FLAG-002): The clearest evidence for the one real counter-current in this household''s life - a way of holding authority that runs against the main pattern without displacing it, and that cannot honestly be left out. It does not amount to a separate strand within the household: on what survives, this is the same kind of authority the traveling scholar holds, occupying a different position rather than being different in kind.'
- type: tension-with
  target_id: hallex06
  note: 'This chunk''s EF: ''the evidentiary core of this world''s one Tensional gravity - a genuine counter-current
    within the ecology'' against the patronage authority structure; tested and found a difference in position,
    not in kind - the tension is real and the honesty about its limits rides with it. Symmetric both ways.'
- type: associated-with
  target_id: hallex07
  note: The standing's exercise at distance rode the letter (hal_lex07's medium) - association, no hierarchy;
    symmetric mirror on hallex07.
contested_claim_ids:
- halclaim005
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex11_exegesis-practiced-authority.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.

[Reported-Experience Status - parked at the S2.2-equivalent; home arrives with the contested_claim records (S2.6-equivalent) / S2.3 authoring] Reported as this world's own self-understanding of Marcella's standing — not independently assessed for historical accuracy beyond the source-critical caveats above; formationally central to the ecology's Tensional counter-current even where its precise historical texture cannot be independently confirmed beyond Jerome's own account.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
