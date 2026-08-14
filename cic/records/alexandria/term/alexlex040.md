---
id: alexlex040
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
term: Mystery / Mysterion
aliases:
- mysterion
- the mysteries
- sacred mystery
- divine mystery
- mystery of Scripture
- sacramental mystery
quick_meaning: For this world mystery (*mysterion*) is not what is unknown but what is known only from
  within — the depth of divine reality that exceeds the surface of any approach to it, that Scripture
  holds and formation progressively opens, that the sacramental practices enact, and whose fullness awaits
  the end; mystery is not a problem to be solved but a depth to be entered.
world_meaning: 'The Greek *mysterion* does not mean puzzle, or secret, or unsolved problem. It means,
  roughly, a sacred reality that is accessible from within but cannot be adequately said from without.
  Someone standing outside a mystery can describe its surface, and describe it intelligently. Someone
  who has been brought inside it — who has entered it, who lives within it — knows from inside what no
  outside description can fully convey. Mystery is the inside-character of what divine pedagogy provides
  and what formation progressively opens.


  Mystery governs the graduated shape of our formation. Every stage opens a depth the previous stage could
  not see — not because the earlier stage was inadequate, but because each depth requires the formation
  the earlier stage gave in order to be received. The catechumen stands at the beginning of that opening:
  the mysteries of Scripture, of the sacramental practices, of the whole sequence are real and present
  but not yet fully received, because reception waits on the formation that catechesis, illumination,
  and gnosis progressively provide. The one further along — the *gnostikos* — perceives depths the catechumen
  cannot yet receive, and is aware that depths remain that their own formation has not yet opened. Mystery
  governs from the beginning to the end: the full knowledge of God is reserved for the consummation that
  theosis names.


  Mystery characterizes Scripture. Scripture holds depths that formed perception is required to receive
  — genuinely present, genuinely open to the reader whose formation has prepared them, genuinely exceeding
  any single encounter''s power to exhaust. Every real reading opens something; every real reading leaves
  more to be opened. The Divine Pedagogue has placed these depths in the text — Origen''s own contribution
  is the "stumbling blocks" argument, that difficulties were deliberately set to drive the formed reader
  deeper — and the sequence is the progressive opening of what the text holds.


  Mystery also characterizes the sacramental practices. The Eucharist and Baptism are mysteries in the
  ancient technical sense: enacted sacred realities whose meaning is received by the initiated from within
  the enacted participation, not fully conveyable in abstract terms to the uninitiated. What the Eucharist
  enacts — a genuine share in the Logos''s self-giving — is not captured by saying "it is a meal," or
  even "it is the body and blood of Christ" if that phrase is held without the inside understanding of
  what enacted participation in the Logos''s life means.


  And mystery keeps us humble before the end. No stage of formation gives complete knowledge of God. The
  deepest formation opens a depth that reveals a further depth; the wisest person perceives more fully
  what remains beyond any created perception of the uncreated God. This is not a defect of formation but
  the right relation between the finite soul and the infinite God who is its end. Formation progressively
  opens what mystery preserves: the always-more, not yet fully received, to be fully received only at
  the completion theosis names.'
distortion_risk: '**World Hearing:**

  Mystery is not the absence of explanation waiting to be filled. It is the inside-character of what exceeds
  adequate outside expression — the depth known from within that cannot be fully conveyed from without.
  Explaining a mystery does not dissolve it; entering it more deeply shows that the depth you have opened
  has deeper depths still. The one who has gone furthest into Scripture, who has been formed most fully
  into a share in divine life, is not the person who has finally left mystery behind by reaching complete
  knowledge. They are the person most aware that the God they are being formed toward infinitely exceeds
  any creaturely reception of it. Mystery is not ignorance; it is the condition of genuine knowledge of
  the infinite. And it is not reserved for an inner circle: every member of the community inhabits the
  mysteries — the catechumen in baptism, the whole community in the Eucharist, every believer in the daily
  meeting with Scripture''s address. What differs is the depth of reception, not access; the unlettered
  believer is not shut out of the mysteries but inhabits them at the depth their formation has reached.'
retrieval:
  tier: 1
  retrieve_when:
  - participant uses "mystery" or "mysterion" in a theological or formational sense, or asks what the
    early church meant by it
  - participant asks why Scripture contains passages that seem impenetrable, or what lies beneath the
    surface of a text or a practice
  - participant asks what the "mysteries" of the faith are, or about the link between the sacramental
    practices and hidden meaning
  - participant asks why God does not simply make divine things directly accessible, or about the reservation
    of full knowledge for the end.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant means "mystery" in the popular sense of a detective story or an unsolved puzzle
  - condition_type: sense-disambiguation
    text: participant is asking specifically about allegory as a reading method (retrieve Allegory) or
      about the sacraments without reference to their mystery-dimension
  - condition_type: sense-disambiguation
    text: the World Capsule Core has already treated the inside-character of formation's depths in the
      current turn.
  force_llm_vote: false
sources:
- source_id: srcALX001
  author_gravity_note: Clement of Alexandria, *Stromateis* I, V — mystery as the inside-character of divine
    knowledge, the movement from surface to depth in Scripture and formation.
- source_id: srcALX002
  author_gravity_note: Origen, *On First Principles* IV — the depths of Scripture as mystery, what the
    formed nous receives that the unformed reader cannot see.
- source_id: srcALX030
  author_gravity_note: 'Ignatius of Antioch, *Letter to the Ephesians* 19 — mystery in the sacramental
    sense, the Incarnation and the community''s enacted mysteries. Ephesians 3:3–6 ("the mystery of Christ"
    revealed in the apostolic proclamation). Colossians 1:26–27 ("the mystery hidden for ages... Christ
    in you, the hope of glory") — the already-but-not-yet dimension.


    Note: mystery as the inside-character of what formation progressively opens, its governance of the
    sequence''s progressive structure, the enacted meaning of the sacramental mysteries, and the reservation
    of full knowledge for the end are **Widely Accepted**; the mystery-account of Scripture''s depths
    is most securely attested for the school tradition. Origen''s systematic account of Scripture''s mystery-levels
    is his distinctive contribution — **Dominant Modern Reconstruction** as an ecology-wide claim — while
    the shared conviction that Scripture contains depths is independently attested in Clement.'
modern_hearing: '**Modern Hearing:**

  "Mystery" now most often means something not yet explained — a puzzle awaiting solution, a problem still
  open. On that reading mystery is what exists before explanation arrives, and once the explanation comes
  the mystery dissolves. Applied to faith, it makes mystery either a placeholder for explanation still
  to come or a permanent admission that some things simply cannot be known. A second modern hearing —
  shaped by popular esotericism — treats mystery as secret teaching reserved for an elite inner circle:
  the mysteries as the hidden doctrines the outer circle does not get.'
period_sense: 'Mysterion - not what is unknown but what is known only from within: the depth of divine
  reality exceeding the surface of any approach; what governs formation''s graduated character and preserves
  the always-more (chunk Quick/World Meaning and EF).'
prior_sense: The Greek mystery-vocabulary of initiated knowledge stands behind the word - noted from standard
  accounts, UNVERIFIED against a registry source; the chunk's own definition ('accessible from within,
  not adequately sayable from without') is the world's received sense.
modern_sense: Something not yet explained - a puzzle awaiting solution (chunk Modern Hearing).
conceptual_distance_note: 'The modern mystery dissolves when solved; the world''s mysterion deepens as
  entered - inside-character, not information gap (chunk World Hearing). Sharp inversion: high grounding
  criterion by rule.'
semantic_domain: divine-agency
grounding_criterion: high
voice_surface: Mysterion does not mean puzzle, or secret, or unsolved problem. It means a sacred reality
  accessible from within - one that cannot be adequately said from without.
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-27'
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
field_relations:
- type: presupposed-by
  target_id: alexlex003
  note: 'The graduated catechumenal shape enacts the mystery''s from-within character (chunk EF: governs
    the graduated structure). Chunk Ecological Function (verbatim, absorbed per FLAG-002): Mystery governs
    the graduated character of formation and preserves the always-more that the end awaits. It anchors
    the sequence''s progressive structure (each stage — catechesis, illumination, gnosis, wisdom, participation
    — opens a depth the previous stage could not receive; the depths are not withheld but require the
    formation that makes reception possible). It names the inside-character of Scripture''s formative
    depth (the Logos''s presence in the text, received by the formed nous, exhausted by no external analysis)
    and the enacted meaning of the sacramental practices (Baptism and Eucharist as mysteries whose meaning
    is had from within the enacted participation). And it is what divine pedagogy looks like from the
    receiving end: because God teaches progressively through the depths of Scripture, creation, and formation,
    mystery is always present as the always-more that formation keeps opening. Its historical breadth
    — creation, Incarnation, the end — is the *oikonomia* seen as depth rather than as arrangement.'
- type: associated-with
  target_id: alexlex041
  note: 'CO-P2-13 (Mark, 2026-07-28): the chunks'' own mutual Related-Terms cross-reference, typed as
    symmetric association - no hierarchy claimed (both sides'' Reciprocity Notes, verbatim in the record
    bodies, attest the pair).'
- type: associated-with
  target_id: alexlex002
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex004
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex014
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex025
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
- type: associated-with
  target_id: alexlex026
  note: 'CO-P2-14 (Mark, 2026-07-28): Doc_06 SS4''s one-directional completion item, COMPLETED as the
    symmetric association the flag-don''t-hide discipline held it open for - the chunk''s own cross-reference,
    mutualized per the build''s declared intent.'
chunk_slug: mystery
---
Migrated at the S6.2 S2.2-equivalent (2026-07-27) from `data/alexandria_world/lexicon_chunks/alexlex040_mystery.md` (mechanical split; mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note — parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with Divine Pedagogy, Scripture, Illumination, Eucharist, Baptism, Oikonomia. **Mutual** (each lists this term back): Oikonomia. **One-directional** (this term lists them; they do not list it back yet — deployment-layer reciprocity-completion items, per Doc_06 §4 flag-don't-hide): Divine Pedagogy, Scripture, Illumination, Eucharist, Baptism. **Not yet built as chunks** (Tier-2 / governed-CT entries): none.

CO-P2-13 (2026-07-28): the Reciprocity Note's mutual cross-references now carry typed associated-with edges; see wrs/migrate/s62_alx_s29_co13.py.

CO-P2-14 (2026-07-28): the Reciprocity Note's one-directional completion items completed as associated-with pairs; see wrs/migrate/s62_alx_s29_co14.py.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`, cross-checked against this term's own linked sources[] and their discovery_channel disclosures. **Flagged as a judgment call**: mixed signal: 1/3 linked sources show active-discovery channels, 2/3 show builder-prior-knowledge; this record's own prose does not independently state its verification story, so the grade rests on inference from source-linkage metadata rather than an explicit first-person statement — noted here rather than re-asserted as settled fact.
