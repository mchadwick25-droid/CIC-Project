---
id: alexlex001
world_id: alexandria-catechetical
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
term: Logos
aliases:
- divine Reason
- Christ as Word
- ho logos
quick_meaning: For this world the Logos is the eternal Word and Reason of God through whom all things
  were made, through whom God teaches, through whom Scripture speaks, and toward whom the soul is drawn
  back — identified with Christ, so that learning, Scripture, worship, and formation are not four activities
  but one movement toward a single reality.
world_meaning: 'The Logos is not a Greek abstraction the church borrowed to sound respectable. It is the
  confession that the opening of John''s Gospel names the deepest truth there is about reality: that at
  the root of everything is the Word, the divine Reason through whom all things were made and in whom
  all things hold together. To live in this world is to take that as the ground under everything else.


  Because the Logos is that ground, every genuine truth — met in Scripture, in creation, in the honest
  reasoning of the philosophers, or in the soul''s own formation — is an encounter with the Logos, whether
  it is named or not. This is why the modern wall between reason and faith, intellect and spirit, simply
  is not built here. There are not two roads, one for the mind and one for the heart; there is one Word,
  and to think truly and to be formed truly are the same road walked at different depths. The philosopher
  who reasons rightly is already reaching toward the one the believer worships.


  And this Word did not stay distant. The eternal Logos truly entered human nature — of one substance
  with the Father, as Nicaea would confess — so that what was broken in humanity could be healed from
  the inside rather than repaired from without. The Logos meets each person according to their capacity
  and their need: the same Word who is the philosopher''s half-glimpsed Reason is the child''s teacher
  and the dying martyr''s companion. That is why everything in this world''s life keeps returning to him
  — he is not one topic among many but the single reality within which every other thing is believed,
  prayed, read, and learned.'
distortion_risk: '**World Hearing:**

  The ground of reality itself, and the living person of Christ. Not a doctrine believed *about*, but
  the reality *within which* everything else is believed, learned, prayed, and undergone. To meet truth
  anywhere is already to have met the Logos.'
retrieval:
  tier: 1
  retrieve_when:
  - participant uses "Logos," "the Word," "divine reason," or asks how reason relates to faith in this
    world
  - participant asks what holds Alexandrian theology together, or why philosophy is treated as preparation
    rather than threat
  - conversation reaches John 1, the incarnation, or how Scripture, learning, and worship connect.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is using "logos" in an unrelated modern/linguistic sense with no theological bearing
  - condition_type: sense-disambiguation
    text: the World Capsule Core has already surfaced the Logos as integrating center in the current turn.
  force_llm_vote: false
sources:
- source_id: srcALX001
  author_gravity_note: John 1:1–18 (the foundational text). Clement of Alexandria, *Protrepticus* and
    *Stromateis* (the Logos as the teacher of the nations, philosophy as preparation).
- source_id: srcALX002
  author_gravity_note: Origen, *On First Principles* I.2 and *Commentary on John* I (the most systematic
    account — the Logos and the *epinoiai*/aspects).
- source_id: srcALX027
  author_gravity_note: Athanasius, *On the Incarnation* (the incarnate Logos restoring human nature).
- source_id: srcALX029
  author_gravity_note: 'The Nicene Creed (325 CE, *homoousios*).


    Note: Origen dominates the surviving *systematic* evidence for the Logos in this world; the underlying
    conviction is broadly Alexandrian and independently attested in Clement (earlier) and Athanasius (later),
    so the core is Widely Accepted while the specific Origenian systematization is Dominant Modern Reconstruction
    (Doc_02 §3.1; Doc_04 C4).'
modern_hearing: '**Modern Hearing:**

  A technical concept from Hellenistic metaphysics that the early church adopted to give Christianity
  intellectual credibility — one doctrine among many, of interest mainly to specialists.'
period_sense: The eternal Word and Reason of God through whom all things were made, through whom God teaches,
  through whom Scripture speaks, and toward whom the soul is drawn back - identified with Christ, so that
  learning, Scripture, worship, and formation are one movement toward a single reality; the ground of
  reality itself, not one doctrine among many (chunk Quick/World Meaning).
prior_sense: 'Greek philosophy''s cosmic reason and, decisively for this world, Philo''s Logos as divine
  intermediary - the inherited grammar this world entered rather than built (Doc_02 SS3.5: allegorical
  reading, the Logos as intermediary, named as inheritance).'
modern_sense: A technical concept from Hellenistic metaphysics the early church adopted for intellectual
  credibility - one doctrine among many, mainly for specialists (chunk Modern Hearing).
conceptual_distance_note: 'The modern ear files the Logos under ''doctrine''; this world lived it as the
  ground under everything - the reality within which everything else is believed, learned, prayed, and
  undergone, so that meeting truth anywhere is already meeting the Logos (chunk World Hearing). Sharp
  gap: high grounding criterion by rule.'
semantic_domain: logos-center
grounding_criterion: high
voice_surface: The Logos is not a borrowed abstraction. At the root of everything is the Word through
  whom all things were made and in whom all things hold together. There are not two roads, one for the
  mind and one for the heart - there is one Word, and to think truly and to be formed truly are the same
  road walked at different depths.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-27'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: presupposed-by
  target_id: alexlex002
  note: 'Divine pedagogy is the Logos teaching continuously - the EF names the Logos as the theological
    ground of both Primary gravities (chunk EF, Doc_04 C4). Chunk Ecological Function (verbatim, absorbed
    per FLAG-002): The Logos is the integrating center of the whole ecology (the Logos-Centered Unity
    supporting gravity, Doc_04 C4): it is the theological ground of both Primary gravities — it is what
    makes Scripture formative (Scripture is where the Logos speaks) and what the soul is being transformed
    into the likeness of. A participant who grasps the Logos grasps why this world treats philosophy as
    preparation, why Scripture is read for depth, why worship and learning belong together, and why the
    incarnation (the homoousios) is load-bearing rather than decorative — remove the Logos and the ecology
    fragments into four disconnected domains.'
- type: presupposed-by
  target_id: alexlex004
  note: Illumination is worked by the Logos through Scripture and formation (chunk QM).
- type: presupposed-by
  target_id: alexlex014
  note: Scripture is formative because it is where the Logos speaks (chunk EF).
- type: presupposed-by
  target_id: alexlex015
  note: 'Christological Reading is grounded in the Logos-Centered Unity: the Logos who speaks through
    the text is the Christ the reader meets (chunk EF).'
- type: presupposed-by
  target_id: alexlex008
  note: Theosis runs through the Logos's incarnation - God became human so that humanity might become
    god (chunk WM).
- type: presupposed-by
  target_id: alexlex019
  note: Resurrection works through the Logos who entered (alexlex019 QM).
- type: presupposed-by
  target_id: alexlex024
  note: Word of God is the Logos title bridging to Scripture (alexlex024 EF).
- type: presupposed-by
  target_id: alexlex039
  note: The Incarnation is the Logos's own entry (alexlex039 QM).
- type: associated-with
  target_id: alexlex005
  note: 'CO-P2-13 (Mark, 2026-07-28): the chunks'' own mutual Related-Terms cross-reference, typed as
    symmetric association - no hierarchy claimed (both sides'' Reciprocity Notes, verbatim in the record
    bodies, attest the pair).'
- type: associated-with
  target_id: alexlex007
  note: 'CO-P2-13 (Mark, 2026-07-28): the chunks'' own mutual Related-Terms cross-reference, typed as
    symmetric association - no hierarchy claimed (both sides'' Reciprocity Notes, verbatim in the record
    bodies, attest the pair).'
- type: associated-with
  target_id: alexlex003
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex006
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex009
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex016
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex022
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex023
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex026
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex037
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex038
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex041
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex044
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex090
  note: 'CO-P2-15: mirror - logikos as kinship with the Logos.'
---
Migrated at the S6.2 S2.2-equivalent (2026-07-27) from `data/alexandria_world/lexicon_chunks/alexlex001_logos.md` (mechanical split; mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note — parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with Divine Pedagogy, Illumination, Knowledge/Gnosis, Participation, Theosis, Scripture. **Mutual** (each lists this term back): Divine Pedagogy, Illumination, Knowledge/Gnosis, Participation, Theosis, Scripture. **One-directional** (this term lists them; they do not list it back yet — deployment-layer reciprocity-completion items, per Doc_06 §4 flag-don't-hide): none. **Not yet built as chunks** (Tier-2 / governed-CT entries): none.

CO-P2-13 (2026-07-28): the Reciprocity Note's mutual cross-references now carry typed associated-with edges; see wrs/migrate/s62_alx_s29_co13.py.

CO-P2-14 (2026-07-28): the Reciprocity Note's one-directional completion items completed as associated-with pairs; see wrs/migrate/s62_alx_s29_co14.py.

CO-P2-15 (2026-07-28): associated-with mirror(s) added toward the newly-authored governed-CT term record(s); see wrs/migrate/s62_alx_s29_co15.py.
