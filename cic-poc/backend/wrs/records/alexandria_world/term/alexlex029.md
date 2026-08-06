---
id: alexlex029
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
term: Teacher / Didaskalos
aliases:
- didaskalos
- Christian teacher
- spiritual guide
- formation guide
- the wise teacher
- catechist
quick_meaning: For us the didaskalos is not someone who delivers information but someone who accompanies
  formation — a teacher whose authority rests on the wisdom the community can see has genuinely formed
  them, whose practice is opening Scripture's depths in the student's presence rather than explaining
  them, so that the student begins to see by being present while the teacher sees.
world_meaning: 'The question we ask of a teacher is not *who appointed you?* It is *what have you become,
  and can you see what the student cannot yet see?* That is the whole ground of a teacher''s authority
  among us.


  The didaskalos''s authority rests on wisdom that is actually visible. Not claimed wisdom, and not a
  title conferred — the teacher is recognized in the community as someone in whom formation has genuinely
  done its work, and that recognition is the authorization. This makes the teacher''s authority a strange
  and strong thing at once. It is vulnerable, because there is no office to fall back on: a teacher whom
  the community no longer recognizes as genuinely formed has lost the very ground they stood on. And it
  is powerful, because it cannot be taken away by maneuver: a community that sees wisdom in a person cannot
  simply be told to stop seeing it. Two authorities live in our common life on two different grounds —
  the teacher''s, resting on what a person has become, and the bishop''s, resting on the apostolic office
  — and neither one dissolves into the other. That is the root of the Teacher–Bishop tension we carry.


  The one whom formation has genuinely made wise is, for us, the same person as the true teacher. What
  the long sequence of formation produces in a soul — genuine contact with God deepening into a wisdom
  that has soaked through the whole life — is exactly what makes that soul able to form others. So the
  teacher''s authorization and the teacher''s own formation are not two things. What formation has made
  in the teacher is what makes the teaching trustworthy.


  And the teaching itself is not the handing over of a content. It is accompaniment. When a teacher opens
  a passage of Scripture in front of a student who has been prepared to begin perceiving, the teacher
  is not explaining the text and passing the explanation across. The teacher is attending to what the
  text holds, and letting the student be present while that attending happens. Perception is caught, not
  transferred. The student who has been genuinely taught has not mainly collected more information; they
  have begun to see, because someone saw in their presence and the seeing was contagious.


  We do not pretend that this authority sits comfortably beside the bishop''s. In this season the bishop
  of Alexandria governs the community''s formation life, and the school''s teaching works within that
  governance rather than above it or alongside it as an equal. We hold that honestly. And we hold, just
  as honestly, that the authority a teacher carries when a text opens under their attention is not the
  bishop''s to grant or to withdraw — it rests on what the teacher has been formed to see. Both are true
  at once. The one who governs the community''s formation and the one who opens Scripture''s depths hold
  different kinds of authority; that the first now governs the second does not make it the same as surpassing
  it.'
distortion_risk: '**World Hearing:**

  The didaskalos''s authority rests on what the teacher has become, not on what the teacher knows. To
  encounter a genuine teacher is not first to receive information but to meet a person in whom formation
  has done its work and, in that meeting, to be drawn toward perceiving what they perceive. It is not
  a gentler theory of the same information-transfer; it is a different kind of transaction — accompaniment
  toward a perception the student''s own formation is progressively making possible.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks what the teacher does in this world's formation, or what makes a teacher authoritative
    here
  - participant asks about Clement or Origen as teachers and what kind of authority they carried
  - participant asks how teacher authority relates to bishop authority, or how teaching here differs from
    delivering information
  - participant uses "didaskalos" or "teacher" in the context of Christian formation
  - conversation reaches who carried the school's teaching tradition.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking primarily about the bishop's formation function (retrieve Bishop)
  - condition_type: sense-disambiguation
    text: about catechesis as the process the teacher governs (retrieve Catechesis)
  - condition_type: sense-disambiguation
    text: about what constrains teacher authority (retrieve Rule of Faith)
  - condition_type: sense-disambiguation
    text: or the World Capsule Core has already surfaced the Teacher–Bishop tension this turn.
  force_llm_vote: false
sources:
- source_id: srcALX002
  author_gravity_note: Gregory Thaumaturgus, *Address of Thanksgiving to Origen* (the first-person account
    from the student's side of what a genuine teacher produces — not the teacher's opinions but genuine
    encounter with the realities the teacher perceived).
- source_id: srcALX001
  author_gravity_note: Clement of Alexandria, *Stromateis* I, VI, VII (the *gnostikos* as, at once, the
    portrait of the true teacher). Origen, *On First Principles* Preface, and *Against Celsus* III.48
    (accompanying the student through formation; forming perception rather than delivering information).
- source_id: srcALX009
  author_gravity_note: 'Eusebius, *Church History* V–VI (the succession of Alexandrian teachers).


    Note: that the teacher''s authority is recognized rather than positional, and that teaching is accompaniment
    rather than information delivery, is Widely Accepted for the school tradition; the Teacher–Bishop
    tension as a live structural feature is Widely Accepted. But the *institutional* form in which these
    teachers stood — a chartered school with a continuous succession — is Contested (this is the **Didaskaleion
    / Catechetical-School** contest, governed as the firm contested-tradition term `alexlex059`; see the
    Carried Contest note below); the teacher-succession list depends heavily on Eusebius, who carries
    HIGH Author-Gravity risk, and should be held at Dominant Modern Reconstruction. The specific contours
    of the Origen–Demetrius episode as the tension''s paradigmatic instance are likewise Dominant Modern
    Reconstruction (Eusebius-mediated).'
modern_hearing: '**Modern Hearing:**

  The modern university classroom maps onto "teacher" so easily the distortion is nearly invisible — the
  one at the front of the room who knows the material and transmits it, whose authority is credentialed
  expertise, where the transaction is complete once the student can show they received what was sent.
  On this hearing the better-informed teacher is the better teacher, and formation is a soft or secondary
  category.'
period_sense: Not someone who delivers information but someone who accompanies formation - a teacher whose
  authority rests on wisdom the community can see has genuinely formed them; one pole of the Teacher-Bishop
  authority tension (chunk Quick Meaning and EF).
prior_sense: Ordinary Greek didaskalos, teacher/instructor - noted from standard lexica, UNVERIFIED against
  a registry source.
modern_sense: The university classroom's teacher - the one at the front of the room delivering content;
  the distortion nearly invisible because the mapping is so easy (chunk Modern Hearing).
conceptual_distance_note: 'Modern teaching authority rests on knowing; the world''s rested on having become
  - visible wisdom, not credentials (chunk World Hearing). Sharp ground shift: high grounding criterion
  by rule.'
semantic_domain: formation-authority
grounding_criterion: high
voice_surface: 'The question we ask of a teacher is not: who appointed you? It is: what have you become,
  and can you see what the student cannot yet see?'
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-27'
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
field_relations:
- type: presupposes
  target_id: alexlex006
  note: 'The didaskalos''s authority rests on demonstrated wisdom (chunk WM/EF). Chunk Ecological Function
    (verbatim, absorbed per FLAG-002): The teacher is one of the two primary formation authorities in
    the ecology — the pole of the Teacher–Bishop tension that grounds authority in demonstrated wisdom
    rather than in office. The teacher anchors the school''s formation capacity (the guided opening of
    Scripture''s depths that the episcopal channels do not themselves provide), the continuity of the
    Alexandrian interpretive tradition (the allegorical, multilevel reading is carried and handed on chiefly
    by teachers), and the visible demonstration that formation produces something real — the teacher is
    formation''s fruit and its continuing instrument at once. A participant who grasps the teacher grasps
    why the Teacher–Bishop tension is a genuine structural feature of this world and not a mere personal
    rivalry: if teacher authority were only delegated episcopal authority, the tension would collapse
    into hierarchy, and it does not.'
- type: tension-with
  target_id: alexlex030
  note: 'The Teacher-Bishop tension both EFs name: authority grounded in demonstrated wisdom vs apostolic
    office - held, not resolved (chunk EF both entries).'
- type: presupposes
  target_id: alexlex031
  note: The teacher answers to the received inheritance (alexlex031 EF).
- type: associated-with
  target_id: alexlex002
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex003
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex005
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex035
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex043
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
Migrated at the S6.2 S2.2-equivalent (2026-07-27) from `data/alexandria_world/lexicon_chunks/alexlex029_teacher.md` (mechanical split; mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note — parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with Bishop/Episkopos, Rule of Faith, Divine Pedagogy, Wisdom, Knowledge/Gnosis, Catechesis. **Mutual** (each lists this term back): Bishop/Episkopos, Rule of Faith. **One-directional** (this term lists them; they do not list it back yet — deployment-layer reciprocity-completion items, per Doc_06 §4 flag-don't-hide): Divine Pedagogy, Wisdom, Knowledge/Gnosis, Catechesis. **Not yet built as chunks** (Tier-2 / governed-CT entries): none.

[Carried Contest — the Didaskaleion / Catechetical-School (`alexlex059`) — parked at the S2.2-equivalent; home arrives with the contested_claim records (S2.6-equivalent) / S2.3 authoring] The teacher is where a participant most directly meets a contest that is *governed elsewhere*. **Teacher is not itself one of this world's firm contested-tradition terms** (those are the six: Apokatastasis, Nous, Logikos, Fall/Descent, Homoousios, Catechetical-School/Didaskaleion). It surfaces the **Didaskaleion / Catechetical-School** contest — carried as the firm [CT] term `alexlex059`, contest type **Historical scope** — because the institutional-school question is felt most directly at the figure of the teacher.

The contest (per `alexlex059` / Doc_01 §1.2): it is genuinely disputed whether the Alexandrian *didaskaleion* was a formal institution with a continuous teaching succession, or a looser teaching tradition retrospectively formalized by Eusebius. Van den Broek (1995) and van den Hoek (1997) deny a formal institution before Origen; Scholten (1995) affirms an institution but as a theological school rather than a catechumen-training school. Eusebius, the main source for the succession, carries HIGH Author-Gravity risk.

This chunk therefore does not assert a settled, orderly institution behind the teacher. What is well-attested is the *kind* of authority the teacher held — grounded in demonstrated wisdom and enacted as accompaniment — and that authority does not depend on the institutional question being resolved. The Teacher–Bishop authority tension is a genuine tension in this world and is held open here, not resolved: the post-Nicene configuration shifts the balance decisively toward episcopal governance without dissolving the teacher's distinct ground.

S2.6-equivalent (2026-07-27): contested_claim_ids populated at claim-authoring time (the FLAG-014 sequencing gap closed for this world); see wrs/migrate/s62_alx_s26.py for the linking rationale.

CO-P2-14 (2026-07-28): the Reciprocity Note's one-directional completion items completed as associated-with pairs; see wrs/migrate/s62_alx_s29_co14.py.

CO-P2-15 (2026-07-28): associated-with mirror(s) added toward the newly-authored governed-CT term record(s); see wrs/migrate/s62_alx_s29_co15.py.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 3 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
