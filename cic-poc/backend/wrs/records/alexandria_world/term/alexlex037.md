---
id: alexlex037
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
term: Faith / Pistis
aliases:
- pistis
- trust
- belief
- initial faith
- the beginning of formation
- the soul's first turn toward God
quick_meaning: For us faith is not intellectual assent to propositions — it is the soul's first genuine
  turning toward God in response to the Logos's address, the beginning of the formation journey rather
  than its completion, the orientation that catechesis deepens, illumination opens, and gnosis fulfills;
  never the opposite of knowledge but the soul's first move toward the knowledge genuine formation produces.
world_meaning: 'Pistis — faith — is the soul''s first real response to the Logos''s address. The catechumen
  who hears Scripture and turns toward what they hear, who does not yet understand deeply, who cannot
  yet perceive what the text holds at depth, who has barely begun — but who genuinely orients toward the
  Logos speaking through the text and through the community''s witness: that is faith. It is real. It
  is the beginning of everything the formation journey will deepen. And it is not less real for being
  the beginning rather than the completion.


  Among us, faith and knowledge are not opposites. They are stages of one orientation, deepening toward
  one reality. The soul that has faith is turned toward God; the soul that has grown in gnosis is more
  deeply, more consciously, more transformingly turned toward the same God. The mature Christian — the
  one in whom formation has deepened faith into genuine knowledge of God — has not replaced faith with
  something better. Faith has been progressively fulfilled in them, made more fully what it always was:
  the soul''s genuine orientation toward the Logos who is its source and its end. Faith is the foundation
  and gnosis is the building; the foundation is not torn out when the building rises — it is what the
  building stands on.


  So the catechumen who has barely begun and the mature believer who has spent decades in formation are
  both exercising faith, both genuinely turned toward the Logos, at profoundly different depths of the
  same orientation. Faith is not a stage the soul passes through and leaves behind. It is the orientation
  every later stage continues and deepens.


  Faith is not the assent of the mind to a list of propositions. A person can affirm every doctrinal claim
  correctly and have no genuine orientation toward God — they have performed belief without the soul''s
  participation. And a soul can be genuinely turned toward God with only a small vocabulary for it. Faith
  is the soul''s orientation, not the mind''s agreement.


  And faith is not certainty set against doubt. The soul genuinely turned toward God in the early stages
  carries many unresolved questions, much not yet understood, much not yet clear. Faith is not the removal
  of those questions; it is the orientation that makes pursuing them a formation act rather than a mere
  exercise of intellect. The catechumen genuinely turned toward the Logos while still holding many questions
  is more deeply in faith than the person who has resolved the questions without any real turning of the
  soul.'
distortion_risk: '**World Hearing:**

  Faith is the soul''s genuine orientation toward God — turned toward the Logos who speaks through Scripture
  and community, open to what the formation sequence deepens, responsive to the divine address always
  being made. It is not assent and not a legal instrument. The person of genuine faith is the one whose
  soul is turned toward God, however partial that turning, however much is still unresolved, however early
  in the journey. That orientation is real, and formation deepens it rather than swapping it for something
  else. Assent can be produced without any real turning of the soul, and the soul''s turning is what the
  ecology requires and deepens; and what salvation accomplishes here is not a change of legal status but
  a genuine transformation of the soul, for which faith as real orientation is the necessary beginning.'
retrieval:
  tier: 1
  retrieve_when:
  - participant uses "faith" in a theological or formational sense, or understands faith mainly as belief
    in doctrines or intellectual assent
  - participant asks whether faith and reason, or faith and knowledge, are opposed
  - participant asks whether faith is the same as certainty or whether doubt is compatible with it
  - participant asks about the relation between faith and formation, whether faith alone suffices for
    salvation, or what the beginning of the formation journey looks like.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about the Reformation doctrine of justification by faith alone
  - condition_type: sense-disambiguation
    text: primarily about gnosis as the developed form of faith (retrieve Knowledge/Gnosis)
  - condition_type: sense-disambiguation
    text: or focused on specific doctrines to be believed rather than faith as the soul's orientation.
  force_llm_vote: false
sources:
- source_id: srcALX001
  author_gravity_note: Clement of Alexandria, *Stromateis* II.2–6 — the definitive account of faith as
    the beginning of the journey, the faith-and-gnosis relation, faith as the foundation on which gnosis
    builds.
- source_id: srcALX002
  author_gravity_note: 'Origen, *Against Celsus* I.9–13 and *Commentary on John* — the relation between
    faith and reason; faith as the soul''s genuine response to the Logos''s address. Hebrews 11:1 — faith
    as genuine orientation toward what is not yet fully seen or understood. John 1:12 — faith as the soul''s
    genuine reception of the Logos''s address ("to all who received him, who believed in his name").


    Note: that faith is the soul''s genuine orientation rather than intellectual assent or legal mechanism,
    that it is the beginning rather than the completion of the journey, and that it is accessible to every
    soul in every condition, are Widely Accepted. The faith-into-gnosis continuity is Widely Accepted
    for the school tradition. The specific formation mechanics of *how* faith deepens into gnosis (the
    school''s detailed account) are Dominant Modern Reconstruction for ecology-wide claims.'
modern_hearing: '**Modern Hearing:**

  Two dominant hearings, both inadequate. The intellectualist: faith is belief — assent to the propositions
  of Christian doctrine; more faith is stronger conviction and doubt is faith''s enemy. The Reformation
  and post-Reformation hearing adds a specific loading: faith is the instrument of justification, the
  means by which the soul receives the verdict of righteousness. On the first, faith is a cognitive state;
  on the second, a legal mechanism. Both make faith something the mind does rather than something the
  soul is.'
period_sense: Pistis - not intellectual assent to propositions but the soul's first genuine turning toward
  God in response to the Logos's address; the beginning of the formation journey, which every later stage
  continues (chunk Quick/World Meaning and EF).
prior_sense: Ordinary Greek pistis, trust/reliability - noted from standard lexica, UNVERIFIED against
  a registry source.
modern_sense: 'Two inadequate hearings: intellectualist belief-assent to doctrines; or blind faith against
  evidence (chunk Modern Hearing).'
conceptual_distance_note: 'Modern faith is a cognitive stance about propositions; the world''s pistis
  is the soul''s orientation toward the one addressing it (chunk World Hearing). Sharp relocation: high
  grounding criterion by rule.'
semantic_domain: formation-sequence
grounding_criterion: high
voice_surface: Pistis is the soul's first real response to the Logos's address. The catechumen who does
  not yet understand deeply, who cannot yet perceive what the text holds - but who genuinely orients toward
  what they hear - has faith.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-27'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: presupposed-by
  target_id: alexlex003
  note: 'The sequence begins from the orientation faith names (chunk EF). Chunk Ecological Function (verbatim,
    absorbed per FLAG-002): Faith is the foundational orientation from which the whole formation sequence
    begins and which every later stage continues. It anchors the sequence''s beginning (catechesis has
    a direction to deepen only because the soul has already turned toward the Logos and wants to go further);
    the connection to repentance (metanoia is the soul''s turning back toward God, and faith is what that
    turning looks like as an ongoing orientation rather than a single act — the two name one reality from
    different angles); the faith-and-gnosis relation (gnosis is faith fulfilled into genuine transformative
    knowledge, not faith transcended); and formation''s accessibility (because faith is an orientation
    and not an intellectual achievement, it is open to every soul in every condition — the catechumen,
    the non-literate believer, the one who has barely begun — and every member of the community is somewhere
    on the same continuum of deepening).'
- type: presupposed-by
  target_id: alexlex033
  note: Witness is that orientation held all the way down (alexlex033 WM).
---
Migrated at the S6.2 S2.2-equivalent (2026-07-27) from `data/alexandria_world/lexicon_chunks/alexlex037_faith.md` (mechanical split; mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note — parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with Knowledge/Gnosis, Repentance/Metanoia, Catechesis, Logos, Wisdom. **Mutual** (each lists this term back): none yet. **One-directional** (this term lists them; they do not list it back yet — deployment-layer reciprocity-completion items, per Doc_06 §4 flag-don't-hide): Knowledge/Gnosis, Repentance/Metanoia, Catechesis, Logos, Wisdom. **Not yet built as chunks** (Tier-2 / governed-CT entries): none.
