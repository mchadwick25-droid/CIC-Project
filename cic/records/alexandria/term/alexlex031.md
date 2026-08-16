---
id: alexlex031
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
term: Rule of Faith / Regula Fidei
aliases:
- regula fidei
- the received deposit
- the apostolic deposit
- the canon of faith
- what has been received
quick_meaning: 'For us the Rule of Faith is not the Nicene Creed and not a doctrinal checklist — it is
  the received apostolic deposit we carry across the generations: the inherited understanding of who Christ
  is, what the Scriptures mean, and what Christian life requires, which sets the bounds of what interpretation
  may claim and what formation may produce, and to which teacher and bishop are equally accountable.'
world_meaning: 'There is a phrase that runs through our formation life and steadies us whenever interpretation
  threatens to drift: *what has always been taught, what has always been believed, what has always been
  received.* The Rule of Faith is the name for what that phrase points at.


  The Rule of Faith is not a document, and it is not the Nicene Creed. The Creed is a specific formulation
  of one part of what the Rule carries, made at a particular moment to defend one dimension of our inheritance
  against one challenge. The Rule itself is broader than any document that states it — it is the living
  inheritance that the succession of apostles, teachers, and bishops has carried from our origin to now,
  present in what we have always taught, always practiced, and always formed toward. In its broadly shared
  contours it carries who Christ is, what the Scriptures are about, the arc of salvation our whole formation
  is built around, and what Christian life requires as essential rather than optional. These are not propositions
  to be ticked off; they are the shape of what we have received, recognizable even when its wording varies.


  What the Rule does among us is give interpretation its tether. An allegorical reading that arrives somewhere
  the Rule has always guarded against has gone wrong, however ingenious it is. A formation practice that
  produces a community life or a belief the inheritance has always refused has produced the wrong thing,
  however coherent it looks from inside. Every interpreting community has to answer one question: who
  decides what the text means and the practice requires, and what constrains the deciding? Our answer
  is: what has been handed down. Not what has been most recently argued. Not what has been most brilliantly
  demonstrated. What has been received.


  This is why the Rule binds teacher and bishop alike. Neither authority may claim to stand above the
  deposit. A teacher whose interpretation contradicts what has always been received is not a wise teacher
  however gifted — wisdom that breaks with the inheritance is not the wisdom we trust. A bishop who governs
  against the Rule is not a faithful bishop however legitimate — an office meant to guard the inheritance
  cannot legitimately override it. The Rule is what holds the Teacher–Bishop tension together as a tension
  inside one community: both are accountable to something neither controls.


  Our own moment has asked something new of the Rule. Before, it worked mostly as custodial continuity
  — the deposit we carry forward, the anchor against drift. The Arian controversy asked it to do more:
  to hold a boundary against a sophisticated challenge that came from *within*, that argued from the same
  Scriptures, used the same vocabulary, and claimed to be the more faithful account of what had always
  been meant. The older challenges we knew came from outside; this one had bishops who believed it and
  councils that endorsed it. So the Rule''s custodial work had to become, at the same time, an enforced
  boundary. The Nicene Creed is the form that enforcement took — a formulation precise enough to exclude
  the Arian alternative, held now not as old deposit alone but as our most recently won clarity. When
  the bishop of Alexandria enforces the homoousios he is doing what bishops have always done, guarding
  the Rule, but in a form the earlier bishop was never asked for: holding a specific boundary won at cost.
  Athanasius was exiled five times, and we who hold what the council clarified know what holding it has
  cost.


  Even so, the older clarification holds: the council settled what the Rule requires about the Son''s
  nature; it did not make the council the interpreter of everything the Rule carries. The bishop enforces
  the homoousios; he does not thereby become the sole determiner of the Rule''s whole meaning. Teacher
  and bishop remain accountable to the Rule as the broader inheritance, of which the Nicene confession
  is one crucial, recently clarified part. And we do not pretend the Rule''s *full* extent is settled
  among us. What it includes beyond its shared contours — whether it reaches to specific positions on
  the soul''s origin, whether it permits or limits the reading of particular texts, how far it constrains
  the speculative inheritance we received from Origen, whether the Creed exhausts it or only specifies
  part of it — these are live questions in our own reflection, not closed ones. The shared contours we
  hold without reservation; the exact reach of the Rule in the harder territory is the ground of genuine
  and ongoing struggle.'
distortion_risk: '**World Hearing:**

  The Rule is neither a checklist nor an anti-interpretive constraint. It is our living formation inheritance
  — what the apostolic community received, practiced, and handed down about who Christ is, what the Scriptures
  mean, and what Christian life requires — broader than any creedal wording and deeper than any propositional
  summary. It is not opposed to genuine interpretation; it is what gives interpretation its direction
  and its tether. A reading that arrives where the Rule has always pointed has not been fenced in by it
  — it has been confirmed by it. A reading that arrives where the Rule has always guarded against has
  not broken through to new truth — it has lost the inheritance Scripture''s depths are addressed to.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about the Rule of Faith or regula fidei
  - participant asks what constrains scriptural interpretation here, or what makes an allegorical reading
    legitimate or illegitimate
  - participant asks about tradition and its relationship to Scripture
  - participant asks what both teacher and bishop are accountable to, or how the community's formation
    inheritance is protected
  - participant asks how the Rule of Faith relates to the Nicene Creed.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about the Nicene Creed specifically as a conciliar formulation (the Creed
      is part of what the Rule carries but is not the same thing)
  - condition_type: sense-disambiguation
    text: participant is asking primarily about teacher or bishop authority (retrieve Teacher or Bishop)
  - condition_type: sense-disambiguation
    text: participant is asking about Scripture as a formation instrument (retrieve Scripture).
  force_llm_vote: false
sources:
- source_id: srcALX031
  author_gravity_note: Irenaeus of Lyon, *Against Heresies* I.10 — the earliest systematic account of
    the Rule as the apostolic deposit the church receives and teaches uniformly across regions (pre-Alexandrian
    but formative for how Alexandria receives the concept).
- source_id: srcALX001
  author_gravity_note: Clement of Alexandria, *Stromateis* VII.16 — the Rule as the constraint within
    which allegorical interpretation operates.
- source_id: srcALX002
  author_gravity_note: Origen, *On First Principles* Preface — the Rule as what the church has always
    taught, within which Origen explicitly places his speculations as further inquiry rather than replacement
    of the deposit (the single most important text for how he understood his relation to the Rule).
- source_id: srcALX003
  author_gravity_note: Athanasius, *Defense of the Nicene Definition* — the Creed as a specific formulation
    of what the Rule requires about the Son's nature.
- source_id: srcALX032
  author_gravity_note: 'Tertullian, *Prescription Against Heretics* 12–19 — the Rule as what the apostolic
    communities received and hand down, prior to and constraining of individual interpretation.


    Note: that the Rule is the received deposit constraining both teacher and bishop, that it is broader
    than any single creedal formulation, and that its broadly shared contours (Christ, Scripture, salvation,
    Christian life) hold, are all Widely Accepted.'
- source_id: srcALX029
  author_gravity_note: That the Nicene Creed specifies one dimension of the Rule is Widely Accepted post-Nicaea.
    But the Rule's specific extent in the harder theological territory — its relation to Origen's speculative
    inheritance especially — is genuinely Contested, both within the tradition's own reflection and in
    modern study; this chunk carries that as live question, not settled fact. The claim that the post-Nicene
    boundary function differs from the earlier custodial function in *kind* rather than only in degree
    is the build's Dominant Modern Reconstruction of what the sources show; the fact that the homoousios
    became an enforced boundary against an intra-Christian alternative is Widely Accepted.
modern_hearing: '**Modern Hearing:**

  Two inadequate hearings. First, the Rule of Faith *is* the creed — a doctrinal checklist of propositions:
  hold the listed beliefs and interpretation is in bounds, contradict them and it is out. Second, the
  Rule of Faith is the dead hand of tradition — a conservative brake that keeps the interpreter from reaching
  genuinely new understanding, the mechanism for domesticating what Scripture might actually say.'
period_sense: 'Not the Nicene Creed and not a doctrinal checklist - the received apostolic deposit carried
  across generations: what has always been taught, believed, and received; the constraint holding the
  Teacher-Bishop tension together, which both are accountable to and neither may override (chunk Quick/World
  Meaning and EF).'
prior_sense: Received through the pre-Alexandrian rule-of-faith tradition the chunk's own Key Sources
  carry (Irenaeus's apostolic deposit, Tertullian's Prescription) - reception-formative texts rowed at
  the sweep (srcALX031/032).
modern_sense: Either the creed as a doctrinal checklist, or an anti-interpretive constraint (chunk Modern
  Hearing).
conceptual_distance_note: 'The modern object is a list to hold; the world''s Rule is a living formation
  inheritance within which interpretation works (chunk World Hearing). Sharp gap of kind: high grounding
  criterion by rule.'
semantic_domain: formation-authority
grounding_criterion: high
voice_surface: What has always been taught, what has always been believed, what has always been received
  - the Rule of Faith is the name for what that phrase points at. It steadies us whenever interpretation
  threatens to drift.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-27'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: presupposed-by
  target_id: alexlex029
  note: 'The teacher is accountable to the received inheritance (chunk EF). Chunk Ecological Function
    (verbatim, absorbed per FLAG-002): The Rule of Faith is the received constraint that holds the Teacher–Bishop
    tension together — the inheritance both are accountable to and neither may override. It anchors interpretive
    legitimacy (the allegorical practice, the Christological orientation, and the school''s depth reading
    are all exercised within what the Rule guards); the shared accountability that makes the Teacher–Bishop
    tension a tension within one community rather than a split into two; and the community''s continuity
    across time (individual teachers and bishops come and go, and the Rule is what carries our identity
    through the changes). The bishop''s guardianship of the Rule is custodial, not interpretive-final:
    he keeps the inheritance continuous across generations, while the teacher carries the interpretive
    practice by which the Rule is read at depth — guardianship is exercised on behalf of what the Rule
    carries, not as a privilege of deciding what it means.'
- type: presupposed-by
  target_id: alexlex030
  note: The bishop guards what was received - the same accountability from the office pole (chunk EF).
- type: associated-with
  target_id: alexlex014
  note: 'CO-P2-13 (Mark, 2026-07-28): the chunks'' own mutual Related-Terms cross-reference, typed as
    symmetric association - no hierarchy claimed (both sides'' Reciprocity Notes, verbatim in the record
    bodies, attest the pair).'
- type: associated-with
  target_id: alexlex003
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex015
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
  target_id: alexlex043
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
chunk_slug: rule-of-faith
---
Migrated at the S6.2 S2.2-equivalent (2026-07-27) from `data/alexandria_world/lexicon_chunks/alexlex031_rule-of-faith.md` (mechanical split; mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note — parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with Teacher/Didaskalos, Bishop/Episkopos, Scripture, Allegory, Christological Reading, Christ, Son of God. **Mutual** (each lists this term back): Teacher/Didaskalos, Bishop/Episkopos, Scripture. **One-directional** (this term lists them; they do not list it back yet — deployment-layer reciprocity-completion items, per Doc_06 §4 flag-don't-hide): Allegory, Christological Reading, Christ, Son of God. **Not yet built as chunks** (Tier-2 / governed-CT entries): none.

CO-P2-13 (2026-07-28): the Reciprocity Note's mutual cross-references now carry typed associated-with edges; see wrs/migrate/s62_alx_s29_co13.py.

CO-P2-14 (2026-07-28): the Reciprocity Note's one-directional completion items completed as associated-with pairs; see wrs/migrate/s62_alx_s29_co14.py.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` was already `verified-via-authority` under the old fleet-wide default; re-examined against this term's own linked sources[] and their discovery_channel disclosures, that value is CONFIRMED (not simply carried over unchecked). **Flagged as a judgment call**: mixed signal: 3/6 linked sources show active-discovery channels, 3/6 show builder-prior-knowledge; this record's own prose does not independently state its verification story, so the grade rests on inference from source-linkage metadata rather than an explicit first-person statement — noted here rather than re-asserted as settled fact.
