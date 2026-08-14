---
id: alexlex042
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
term: Virtue / Arete
aliases:
- arete
- the virtues
- moral excellence
- the virtuous life
quick_meaning: 'For this world virtue is not the excellent performance of a human function or the prize
  of disciplined effort — it is the visible fruit of genuine transformation: what the soul looks like
  once its desire has been truly reordered toward God, so that virtuous acts are expressions of what the
  soul has become rather than performances of what it has decided to do.'
world_meaning: 'The word *arete* comes to us from the Greeks, where it meant excellence — a thing functioning
  well according to its nature. The most systematic account of it we inherit is Aristotle''s: virtue as
  the mean between extremes, courage standing between cowardice and recklessness, developed by repeated
  practice until it becomes settled character. On that account the virtuous person has done the work —
  habituated the right dispositions through sustained effort — and the virtue is the product of their
  own development.


  This is not what *arete* means for us — not because we ignore Aristotle (we know him thoroughly) but
  because our account of where virtue *comes from* is different, and that difference changes what virtue
  *is*. For us virtue is not the excellent performance of a human function through habituated effort.
  It is the visible expression of what transformation has done to the soul — the fruit, in actual character
  and behavior, of the genuine reordering of desire that formation works. The difference is load-bearing.
  On the one account the virtuous person has developed the virtue; on ours the virtuous person has been
  *formed*, and the virtue is what formation has made of the soul rather than what the soul has made of
  itself.


  So the test of virtue among us is not whether a person performs the right acts — they will — but whether
  those acts express genuine formation or merely enact what a still-unformed person has decided to do.
  This is the same conviction the Likeness of God carries, now in behavioral terms: the likeness is grown
  from within, not imitated from without, and virtue is that likeness in action. When we picture the mature
  Christian — the *gnostikos* — we do not describe someone who has drilled excellent dispositions into
  place. We describe someone whose gnosis has become inseparable from love, whose knowledge of God has
  reordered desire toward God, and whose virtues are simply what that reordered desire pours out: courage
  in one whose orientation toward God runs deeper than any threat can reach; justice in one whose desire
  for another''s flourishing flows from love rather than calculated fairness; temperance in one whose
  desire has been trained toward what genuinely satisfies rather than toward the lesser goods that excess
  chases. Knowing, loving, and living well are not three separate achievements here. They are one formation,
  showing in three ways.'
distortion_risk: '**World Hearing:**

  Virtue is not what the person has achieved but what formation has done to the person. The difference
  is between a person who has decided to behave generously and a person whose desire has been genuinely
  reordered toward generosity over years of formation — both may perform the same acts, but in the second
  they are expressions of what the person has *become*. The effort-account fails not because effort is
  irrelevant but because it locates virtue''s source in the soul''s own work rather than in what formation
  has done to the soul. Two people may act alike; only the genuinely formed soul *expresses* virtue, while
  the unformed soul that performs it is performing, not expressing.'
retrieval:
  tier: 1
  retrieve_when:
  - participant uses "virtue" in a theological or formational sense, or asks how moral excellence is achieved
  - participant asks about the relation between character and formation, or whether virtue is formation's
    goal or its consequence
  - participant asks about particular virtues (courage, justice, temperance, wisdom), or how the Alexandrian
    account differs from Aristotle's
  - participant asks what transformation looks like in lived behavior, or whether someone who does virtuous
    things without formation is virtuous in this world's sense.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about wisdom specifically (retrieve Wisdom)
  - condition_type: sense-disambiguation
    text: participant is asking about love specifically (retrieve Love/Agape)
  - condition_type: sense-disambiguation
    text: the conversation is about virtue ethics as a modern philosophical framework rather than this
      world's account.
  force_llm_vote: false
sources:
- source_id: srcALX001
  author_gravity_note: Clement of Alexandria, *Stromateis* II, IV, VI, VII (the *gnostikos* as the model
    of genuine virtue; the inseparability of virtue, love, and gnosis; virtue as formation-fruit rather
    than effort-product).
- source_id: srcALX002
  author_gravity_note: Origen, *On First Principles* III.1 (virtue in relation to the soul's freedom and
    formation; character genuinely formed through the soul's response to divine pedagogy).
- source_id: srcALX004
  author_gravity_note: 'Athanasius, *Life of Antony* (Antony as the paradigm of formed virtue in the late
    Alexandrian horizon; virtue visible as the fruit of a lifetime of formation — Antony sits at the boundary
    of the school and desert traditions, and the cross-build constraint applies). Galatians 5:22–23 ("the
    fruit of the Spirit is love, joy, peace..." — virtue as the Spirit''s formation-fruit). Philippians
    4:8 ("if there is any excellence [*arete*]..." — the scriptural use of *arete* as formation orientation).


    Note: virtue as transformation-fruit rather than effort-achievement, its inseparability from love
    and gnosis in Clement, and its status as the Likeness of God''s behavioral expression are Widely Accepted
    for the school tradition. How the Alexandrian account of virtue relates to the Greek philosophical
    accounts (chiefly Stoic and Aristotelian) — how far the Christian account transforms, absorbs, or
    critiques the Greek inheritance — is a genuinely open question in the tradition and in later reconstruction:
    **Contested**. Antony as the paradigm of formed virtue sits at the school/desert boundary and stands
    under the cross-build provisional constraint (its developed form belongs to the Desert Christianity
    build). This term carries the [TC] technical-concept tag for the precision *arete* bears here; it
    is not among Doc_06''s six firm [CT] terms, so the contest above is reported at the confidence level
    rather than as a governed CT contest type.'
modern_hearing: '**Modern Hearing:**

  Virtue as excellence of character built through habitual practice — the virtuous person is the one who
  has practiced virtuous acts until they became second nature, mastering the mean between extremes. A
  secondary hearing locates virtue in decision-making: the virtuous person makes the right choices through
  correct moral reasoning. Both locate virtue in what the person has achieved by their own moral development
  — the virtue is the person''s own product.'
period_sense: 'Arete - not excellence achieved through disciplined practice but the visible fruit of genuine
  transformation: what the soul looks like when formation has done its work; the concrete face of the
  transformation gravity (chunk Quick/World Meaning and EF).'
prior_sense: 'The chunk carries the inherited sense whole: Greek arete as excellence, with Aristotle''s
  virtue-as-the-mean named as the most systematic inherited account - received and re-grounded.'
modern_sense: Virtue as excellence of character built through habitual practice - achievement (chunk Modern
  Hearing).
conceptual_distance_note: 'The modern (and Aristotelian) virtue is what the person has achieved; the world''s
  is what formation has done to the person (chunk World Hearing). Sharp agency inversion: high grounding
  criterion by rule.'
semantic_domain: formation-fruit
grounding_criterion: high
voice_surface: Arete came to us from the Greeks, where it meant excellence - a thing functioning well
  according to its nature. Among us, virtue is not what the person has achieved but what formation has
  done to the person.
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-27'
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
field_relations:
- type: presupposes
  target_id: alexlex021
  note: 'The characterological expression of transformation''s work (chunk EF). Chunk Ecological Function
    (verbatim, absorbed per FLAG-002): Virtue is the behavioral and characterological expression of what
    the transformation gravity produces in the soul through the formation sequence. It is the concrete
    face of formation evidence — where wisdom names the visible formation of a whole life, virtue names
    how that formed life acts, relates, responds, and chooses; it is the Likeness of God made behavioral
    (the image conformed to God''s character, showing as the love that endures, the justice that does
    not calculate, the courage grounded in orientation toward God); it is inseparable from love (in the
    mature Christian, gnosis, love, and virtue are held together as one thing, not three accomplishments);
    and it connects directly to the Transformation gravity, whose aim — the soul''s genuine reorientation
    toward God — is exactly what virtue makes visible in lived relationship to God, others, and self.
    Understand virtue and one understands why this world judges behavior by what produced it, not by its
    surface conformity.'
- type: associated-with
  target_id: alexlex005
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex006
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex007
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex012
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex038
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
chunk_slug: virtue
---
Migrated at the S6.2 S2.2-equivalent (2026-07-27) from `data/alexandria_world/lexicon_chunks/alexlex042_virtue.md` (mechanical split; mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note — parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with Wisdom, Likeness of God, Love/Agape, Transformation, Knowledge/Gnosis, Participation. **Mutual** (each lists this term back): none yet. **One-directional** (this term lists them; they do not list it back yet — deployment-layer reciprocity-completion items, per Doc_06 §4 flag-don't-hide): Wisdom, Likeness of God, Love/Agape, Transformation, Knowledge/Gnosis, Participation. **Not yet built as chunks** (Tier-2 / governed-CT entries): none.

CO-P2-14 (2026-07-28): the Reciprocity Note's one-directional completion items completed as associated-with pairs; see wrs/migrate/s62_alx_s29_co14.py.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 3 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
