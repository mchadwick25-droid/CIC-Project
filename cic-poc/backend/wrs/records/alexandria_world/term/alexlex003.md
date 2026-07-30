---
id: alexlex003
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
term: Catechesis
aliases:
- catechumenate
- catechetical instruction
- the catechumen
- formation in the faith
- preparation for baptism
- Christian formation
quick_meaning: For this world catechesis is the long, community-held, Scripture-formed process through
  which a person is gradually shaped into Christian life — not taught a set of doctrines to agree with,
  but formed into a new way of perceiving and inhabiting the world, under the divine Teacher who works
  through the community's own practices.
world_meaning: 'Catechesis does not begin with what a person knows. It begins with who they are — and
  with the recognition that who they are needs to change.


  When someone comes to us and asks to enter, we do not sit them down for an examination. They have come
  for a transformation, and that is what we begin. We do not hand over a list of doctrines to accept,
  a set of rules to keep, and a date for the ceremony. We receive them as a catechumen — one who is being
  formed, one who is hearing, one whose soul is being turned toward a new center — and we begin the slow
  work of letting that formation actually happen.


  That slow work is what catechesis names. It is ordered: the catechumen moves through recognized stages,
  each a deeper entry into what we are and what is being asked of the one entering. It is graduated, because
  the divine pedagogy does not give everything at once. The Logos meets each person where they are, and
  catechesis is how we meet the catechumen where they are while drawing them toward where they are not
  yet.


  Through these stages the two great pressures of our life do their work. The catechumen hears Scripture
  — not as a reader forming a private opinion, but as one being formed by our shared reading of a living
  voice that addresses them. The catechumen shares in worship, not yet at the Eucharist but enough that
  our life begins to become theirs. The catechumen is formed in how they live — not by a rulebook but
  by what a person shaped among us actually looks like: generous, humble, honest, patient, awake to the
  poor. And the catechumen meets the hard discovery of how much is still unformed, how far the soul still
  is from what we are being changed into.


  Baptism is not the end of this. It is the decisive crossing within it — the moment the catechumen passes
  a visible boundary into our full life together. But the formation that led there does not stop there;
  it deepens. The baptized go on through further stages — illumination, the deepening of knowledge, the
  slow emergence of wisdom, the growth of participation — in the same shape: our practices, the divine
  pedagogy working through them, the soul receiving what it is ready to receive and being made ready to
  receive more.


  What catechesis is not: it is not a doctrinal exam, not a class that transfers information, not a friendly
  initiation into a circle. It is how a person who has not yet been formed to receive Scripture as deep
  formative reality begins, over time, to be formed by it — and how that person is first turned toward
  the transformation of the soul toward God.'
distortion_risk: '**World Hearing:**

  The formation of a person, not the transfer of information. Someone who has heard everything and can
  repeat everything, but whose desire has not been reordered and whose life has not learned to fast and
  pray and give, has not been catechized — the community has spoken, but the formation has not occurred.
  Catechesis takes time not because there is so much to transmit but because formation is what time is
  for: the soul needs the same realities met again and again, in different modes, until the encounter
  changes what it loves.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how someone becomes a Christian or enters the community, about the catechumenate,
    or about the stages before baptism
  - participant uses "catechumen," "catechist," or "instruction in the faith"
  - participant asks why Christian formation takes time rather than happening in a single event, or how
    formation happens in community rather than privately
  - participant treats becoming a Christian as agreeing to doctrines or passing an exam.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking primarily about what the school taught at depth rather than about entry-formation
      (retrieve Wisdom or the school-tradition terms)
  - condition_type: sense-disambiguation
    text: participant is asking about baptism itself rather than the process leading to it
  - condition_type: sense-disambiguation
    text: the conversation is about advanced formation (illumination, wisdom) rather than initial entry.
  force_llm_vote: false
sources:
- source_id: srcALX001
  author_gravity_note: Clement of Alexandria, *Paedagogus* I (graduated formation under Christ the Pedagogue
    — the theological ground of the catechumenal shape).
- source_id: srcALX002
  author_gravity_note: 'Origen, Homilies (public scriptural formation of the gathered community — catechesis
    in action). Gregory Thaumaturgus, *Address of Thanksgiving to Origen* (a first-person account of what
    formation through Origen''s teaching was like, from the student''s side). Eusebius, *Church History*
    V–VI (the catechetical school and its succession from Pantaenus through Origen).


    Note: catechesis as a graduated, community-based formation process, and the conviction that formation
    takes time, are Widely Accepted across the horizon. The specific sequence of catechumenal stages is
    Dominant Modern Reconstruction, unevenly attested.'
- source_id: srcALX009
  author_gravity_note: Claims about the school's *formal institutional structure and succession* rest
    heavily on Eusebius, who carries HIGH Author-Gravity risk for institutional detail — the formation
    practice is far better attested than the institutional history, and whether the school was a formal
    institution is itself contested (see the Catechetical School / Didaskaleion entry, alexlex059).
modern_hearing: '**Modern Hearing:**

  "Catechism" as a booklet of doctrinal questions and answers to be memorized — a transfer of correct
  information, completed when the person can recite the right answers. The catechist delivers content;
  the catechumen retains it.'
period_sense: The long, community-held, Scripture-formed process through which a person is gradually shaped
  into Christian life - begun from who the person is, not what they know; a transformation undertaken,
  not a doctrine-list accepted (chunk Quick/World Meaning).
prior_sense: Ordinary Greek katechein, to instruct by word of mouth - noted from standard lexica, UNVERIFIED
  against a registry source; the build's own documents develop the world's practice, not the word's earlier
  career.
modern_sense: '''Catechism'' as a booklet of doctrinal questions and answers to memorize - information
  transfer, completed on recitation (chunk Modern Hearing).'
conceptual_distance_note: 'The modern object is a text mastered; the world''s practice is a person formed
  - someone who can repeat everything but whose desire is unreordered has not yet begun (chunk World Hearing).
  Sharp gap: high grounding criterion by rule.'
semantic_domain: formation-sequence
grounding_criterion: high
voice_surface: When someone comes to us and asks to enter, we do not sit them down for an examination.
  They have come for a transformation, and that is what we begin. Catechesis does not begin with what
  a person knows - it begins with who they are.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-27'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: presupposed-by
  target_id: alexlex004
  note: 'Catechesis initiates the movement illumination carries forward - the EF names it the entry mechanism
    of the whole ecology (chunk EF). Chunk Ecological Function (verbatim, absorbed per FLAG-002): Catechesis
    is the entry mechanism of the whole formation ecology: it initiates the movement that Scripture-as-formative
    reality (Doc_04 C1) and the transformation of the soul (C2) carry forward, and it is ordered from
    the start by the Divine Pedagogy supporting gravity (C3), which is why it is graduated rather than
    delivered all at once. Every later dimension — illumination, knowledge, wisdom, participation — presupposes
    that a person has been catechetically formed enough to receive it, so the sequence begins here. A
    participant who grasps catechesis grasps why formation is ecclesial rather than private (the whole
    community forms the catechumen, so the community''s integrity is itself formative), why it is held
    within the Rule of Faith (the catechumen is received into a shared inhabitation of Scripture, not
    given a private reading), and why the question of who governs catechetical formation — the school
    teacher or the bishop''s community — is one of the live tensions of this world.'
- type: presupposes
  target_id: alexlex002
  note: The practice enacts the divine teaching - remove the conviction that God is always teaching and
    catechesis loses its ground (chunk EF).
- type: presupposes
  target_id: alexlex013
  note: 'Formation is invitation, not programming: it works through the soul''s genuine response - remove
    autexousia and catechesis becomes manipulation (alexlex013 WM).'
- type: presupposed-by
  target_id: alexlex025
  note: Baptism is the threshold catechesis leads toward (alexlex025 EF).
- type: presupposes
  target_id: alexlex032
  note: The person came having turned - catechesis deepens the turn (alexlex032 EF).
- type: presupposes
  target_id: alexlex037
  note: The sequence begins from faith's orientation (alexlex037 EF).
- type: presupposes
  target_id: alexlex040
  note: The graduated shape enacts the mystery's from-within character (alexlex040 EF).
- type: associated-with
  target_id: alexlex001
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex029
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex030
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex031
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex034
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex059
  note: 'CO-P2-15: the governed contest this term carries is surfaced at the partner term (Doc_06 SS3''s
    CT-surfacing convention).'
contested_claim_ids:
- alexclaim004
---
Migrated at the S6.2 S2.2-equivalent (2026-07-27) from `data/alexandria_world/lexicon_chunks/alexlex003_catechesis.md` (mechanical split; mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note — parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with Divine Pedagogy, Illumination, Logos, Baptism, Rule of Faith. **Mutual** (each lists this term back): Divine Pedagogy, Illumination, Baptism. **One-directional** (this term lists them; they do not list it back yet — deployment-layer reciprocity-completion items, per Doc_06 §4 flag-don't-hide): Logos, Rule of Faith. **Not yet built as chunks** (Tier-2 / governed-CT entries): none.

S2.6-equivalent (2026-07-27): contested_claim_ids populated at claim-authoring time (the FLAG-014 sequencing gap closed for this world); see wrs/migrate/s62_alx_s26.py for the linking rationale.

CO-P2-14 (2026-07-28): the Reciprocity Note's one-directional completion items completed as associated-with pairs; see wrs/migrate/s62_alx_s29_co14.py.

CO-P2-15 (2026-07-28): associated-with mirror(s) added toward the newly-authored governed-CT term record(s); see wrs/migrate/s62_alx_s29_co15.py.
